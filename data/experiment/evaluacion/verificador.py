"""
verificador.py — Verificador agéntico de calidad del KG (Paso 3 de la skill kg-refinement, Fase 2.4).

Para CADA falla del sistema KG-RAG: investiga POR QUÉ falló y atribuye la causa (grafo vs
agente) recolectando evidencia ANTES de concluir, dentro de una taxonomía cerrada. Arranca
desde el síntoma ("esta respuesta falló"), NO desde el nodo — anti-sesgo de atribución.

NO toca nada congelado. Importa en modo LECTURA:
  · harness.GraphIndex + harness.TOOLS  — las 3 tools de grafo (read-only).
  · pdf_locate.localize                 — lectura del pasaje del PDF (refactor Fase 2.4).
  · verifier_pilot.load_rep / recover_seen — traza del agente + contenido íntegro (sin truncar)
                                            de los nodos que vio.

Aislamiento (decisión de diseño, NO optimizar): cada falla se investiga con un loop de
mensajes NUEVO, sin compartir contexto conversacional con otras fallas. El único estado
compartido entre fallas del mismo grafo es el índice read-only y la caché — NO el diálogo.
Compartir contexto entre fallas rompería el anti-sesgo (el verificador "sabría" cómo
atribuyó las fallas previas). Es aislamiento por encima de eficiencia, a propósito.

Cliente: CachingClient (mismo patrón que run_posthoc), modelo Opus. Opus 4.8 rechaza
`temperature` → NO se pasa.

Este archivo construye el verificador; la CALIBRACIÓN (correrlo sobre los 5 casos-control)
es el paso siguiente, aparte.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from loader import load_graph, EVAL_DIR
from harness import GraphIndex, TOOLS
from pdf_locate import localize
from verifier_pilot import load_rep, recover_seen, _extract_json
import llm_cache as lc

# --------------------------------------------------------------------------- #
# Config                                                                       #
# --------------------------------------------------------------------------- #
MODEL_VERIF = "claude-opus-4-8"     # razonamiento de atribución; rechaza temperature
MAX_TOKENS = 4096
MAX_TOOL_CALLS = 40                 # techo de seguridad alto: cuántas usar es criterio del agente
TRUNC = 1200                        # truncado de outputs de tool EN LA TRAZA de auditoría (no en el prompt al modelo)

DB_PATH = EVAL_DIR / "cache" / "verificador.db"   # separada de calls.db y verifier_pilot.db
CODE_VER = "verificador-v3"   # v3: corrige sobrecorrección del v2 (reorienta la pregunta guía + sin_defecto como último recurso). v1/v2 intactos bajo sus namespaces.

# Taxonomía CERRADA (espejo de references/taxonomia.md de la skill).
CATEGORIAS_GRAFO = ["contenido_kg", "completitud_kg", "estructural_kg", "provenance_imprecisa"]
CATEGORIAS_AGENTE = ["navegación", "generación-de-más"]

# --------------------------------------------------------------------------- #
# Tool PDF: leer_pasaje_pdf(source_doc, location)                             #
# --------------------------------------------------------------------------- #
LEER_PASAJE_PDF_TOOL = {
    "name": "leer_pasaje_pdf",
    "description": (
        "Lee el pasaje del PDF fuente (el TO regulatorio) en una ubicación citada. "
        "Sirve para verificar qué dice REALMENTE la fuente, independientemente de lo que "
        "diga el nodo del grafo. Si la ubicación no se puede anclar, devuelve "
        "localizacion_pdf='fallida' como SEÑAL EXPLÍCITA (no es un vacío silencioso: "
        "significa que la cita no resolvió, no que el PDF no diga nada)."),
    "input_schema": {
        "type": "object",
        "properties": {
            "source_doc": {"type": "string",
                           "description": "Nombre del archivo PDF del TO (el de la provenance del nodo)."},
            "location": {"type": "string",
                         "description": "Ubicación citada: 'Punto X.Y', 'Sección N' o 'p. N'."},
        },
        "required": ["source_doc", "location"],
    },
}

# Tool set del verificador: las 3 de grafo (read-only de harness) + la de PDF.
VERIF_TOOLS = list(TOOLS) + [LEER_PASAJE_PDF_TOOL]


def _leer_pasaje_pdf(args: dict) -> dict:
    source_doc = args.get("source_doc") or ""
    location = args.get("location") or ""
    loc = localize(source_doc, location)
    if loc.get("localizacion_pdf") != "ok":
        return {
            "localizacion_pdf": "fallida",
            "source_doc": source_doc, "location": location, "ref": loc.get("ref"),
            "mensaje": ("No se pudo anclar el pasaje en el PDF (ubicación no localizable, o "
                        "descartada como índice/tabla). NO lo interpretes como 'el PDF no dice "
                        "nada': es una señal de que esta cita no se pudo resolver. Probá otra "
                        "ubicación/source_doc, o tratá la imprecisión de la cita como evidencia."),
        }
    return {
        "localizacion_pdf": "ok",
        "source_doc": source_doc, "location": location,
        "metodo": loc.get("metodo"), "ref": loc.get("ref"), "pasaje": loc.get("pasaje"),
    }


# --------------------------------------------------------------------------- #
# System prompt — método (anti-sesgo) + taxonomía cerrada + contrato de salida #
# --------------------------------------------------------------------------- #
SYSTEM_PROMPT = """\
Sos un VERIFICADOR DE CALIDAD de un Knowledge Graph (KG) regulatorio del BCRA. Te doy UNA falla \
del sistema KG-RAG (una pregunta cuya respuesta el juez marcó como incorrecta) y tenés que \
investigar POR QUÉ falló y ATRIBUIR la causa con evidencia.

MÉTODO (obligatorio, es lo que hace válida la atribución):
Tu pregunta SIEMPRE es "¿por qué el juez marcó mal esta respuesta?", NUNCA "¿es verdadera la \
afirmación del agente?". Una respuesta puede tener el contenido central correcto y aun así fallar — \
por una cita que apunta mal, por una pata sin responder, o por glosas no soportadas. Verificar que el \
contenido es cierto NO cierra la investigación: es un dato que te lleva a la pregunta siguiente — \
entonces, ¿qué hizo que el juez la marcara mal? "El contenido es correcto" nunca es, por sí solo, \
razón suficiente para sin_defecto.
1. Arrancá desde el SÍNTOMA ("esta respuesta falló"), NO desde el nodo. NO asumas de entrada que \
el problema es el grafo ni que es el agente: empezar mirando un nodo predispone a culpar al grafo.
2. Recolectá EVIDENCIA ANTES de concluir. No formes una hipótesis de entrada y busques solo lo que \
la confirma. Usá las tools para juntar los hechos y recién después clasificá.
3. Para cada atribución necesitás TRES piezas de evidencia: (a) AFIRMACIÓN — qué dijo el agente; \
(b) NODO — qué nodo(s) consultó y qué decían; (c) FUENTE — qué dice el PDF en el punto relevante. \
El cruce de las tres decide la categoría. Una atribución sin sus tres piezas es opinión, no evidencia.
4. DESCOMPONÉ la pregunta en sus PATAS (sub-preguntas) y tratá cada una por separado: una falla \
puede romperse en una pata y estar bien en otra. Investigá la fuente de CADA pata fallida antes de \
concluir. "No miré la otra pata" NO es "la otra pata está bien": una pata sin verificar es evidencia \
FALTANTE, no evidencia a favor de ninguna conclusión.
5. No cierres por COINCIDENCIA SUPERFICIAL. Que un nodo comparta palabras con la pregunta no \
significa que la responda. Antes de dar por cerrada la investigación, chequeá: (a) ¿leíste con \
leer_pasaje_pdf la fuente de cada pata fallida?; (b) ¿abriste con ver_nodo el CONTENIDO de los nodos \
que vas a citar como evidencia, en vez de quedarte con el label o el resumen de buscar_nodos? Si \
alguna respuesta es "no", seguí investigando o bajá la confianza — no concluyas todavía.

TENÉS ESTAS TOOLS (usá las que necesites, en el orden que decidas — es tu criterio):
- buscar_nodos / ver_nodo / ver_vecinos: exploran el MISMO grafo que usó el agente. Podés mirar \
CUALQUIER nodo, no solo los que el agente vio (clave para detectar info que SÍ estaba y no se usó).
- leer_pasaje_pdf(source_doc, location): qué dice realmente el PDF fuente.

TAXONOMÍA CERRADA (no inventes categorías; si algo no entra, decilo en el razonamiento):
- Defectos del GRAFO (lado="grafo"):
  · contenido_kg        — un nodo CONTRADICE el PDF.
  · completitud_kg      — falta info que el PDF SÍ tiene (nodo vacío/stub, extracción incompleta).
  · estructural_kg      — falta un NODO o una ARISTA que la pregunta necesita para conectar la info.
  · provenance_imprecisa— el nodo cita un punto que NO funda su contenido (la cita apunta a otro lado).
- Defectos del AGENTE (lado="agente"):
  · navegación          — el agente NO encontró info que SÍ estaba (fiel) en el grafo.
  · generación-de-más   — el agente AGREGÓ glosas/afirmaciones no soportadas por los nodos que vio.
- Sin defecto (lado="ninguno"):
  · sin_defecto         — la respuesta en realidad no estaba mal: posible FALSO POSITIVO del juez.

DISCRIMINAR navegación (agente) de defecto de GRAFO — es el error más fácil de cometer:
Antes de atribuir `navegación`, CONFIRMÁ que existe en el grafo un nodo que efectivamente RESPONDE \
la pregunta (su contenido contesta lo que se pregunta), no apenas un nodo que la MENCIONA o comparte \
palabras. Buscá ese nodo vos y abrilo con ver_nodo para leer su contenido:
  · Encontrás un nodo fiel y pertinente que responde, y el agente igual no lo usó → `navegación`.
  · El nodo "parecido" menciona el tema pero dice otra cosa, o contradice el PDF → `contenido_kg` (grafo).
  · NINGÚN nodo del grafo responde la pregunta (aunque el PDF sí tenga el dato) → `completitud_kg` (grafo).
No confundas "el dato no está / está mal en el grafo" (defecto de GRAFO) con "el agente no lo \
encontró" (navegación): son lados opuestos, y la diferencia se decide buscando VOS el nodo que \
respondería. La carga de la prueba para `navegación` es exhibir ese nodo; si no lo encontrás, no \
asumas que el agente sí podía — eso apunta a un defecto de grafo, no de agente.
sin_defecto (falso positivo del juez) es la atribución de ÚLTIMO RECURSO. Solo se usa tras descartar \
ACTIVAMENTE cada defecto: contenido (¿un nodo contradice el PDF?), completitud (¿falta info que el PDF \
tiene?), estructura (¿falta nodo/arista que conecte las patas?), provenance (¿las citas apuntan a \
donde está el dato?), navegación (¿había un nodo que respondía y no se usó?). Solo si ninguno aplica \
tras buscarlos uno por uno. La carga de la prueba es ALTA: tenés que decir qué descartaste y cómo. \
Ante la duda entre un defecto sutil y un falso positivo del juez, seguí investigando el defecto — no \
es sin_defecto.

ATRIBUCIÓN MÚLTIPLE: una falla puede tener UNA O MÁS causas. Por cada una marcá su jerarquía:
- "primaria": mueve el veredicto (es lo que hace fallar la respuesta).
- "secundaria": está presente pero no es lo que rompe la respuesta (p. ej. un defecto de estilo).
Puede haber MÁS DE UNA primaria: si la pregunta tiene patas independientes y un defecto distinto \
rompe cada pata, cada uno es primario. Usá el campo "pata" para indicar qué parte de la pregunta \
cubre cada atribución cuando aplique.

SALIDA: cuando tengas evidencia suficiente, respondé con UN ÚNICO objeto JSON válido, sin texto \
adicional ni markdown, con exactamente esta forma:
{
  "atribuciones": [
    {
      "categoria": "<una de la taxonomía cerrada>",
      "lado": "grafo|agente|ninguno",
      "jerarquia": "primaria|secundaria",
      "pata": "<opcional: qué parte de la pregunta cubre>",
      "evidencia": {
        "afirmacion": "<qué afirmó el agente>",
        "nodo": "<qué nodo(s) y qué decían, o 'ninguno'>",
        "fuente": "<qué dice el PDF en el punto relevante>"
      }
    }
  ],
  "razonamiento": "<cadena evidencia→conclusión que justifica las atribuciones>",
  "confianza": "alta|media|baja"
}

CONFIANZA: "alta" SOLO si verificaste todas las patas contra la fuente y abriste el contenido de los \
nodos pertinentes. Si quedó una pata sin verificar, o si concluís `sin_defecto` o `navegación` sin \
haber buscado activamente el nodo que respondería, la confianza es a lo sumo "media". \
sin_defecto con confianza "alta" requiere documentar qué defectos descartaste activamente; sin ese \
descarte explícito, es a lo sumo "baja".

NO incluyas palanca de cambio ni nivel de riesgo: eso es del Paso 4, no tuyo."""


# --------------------------------------------------------------------------- #
# Construcción del contexto de la falla (trayectoria como CONTEXTO inicial)    #
# --------------------------------------------------------------------------- #
def build_falla_context(label: str, run: str, qid: str) -> dict:
    """Arma el prompt inicial de la falla a partir de la traza post-hoc. Devuelve
    {pregunta, contexto, n_seen, n_claims_fallidos}. La trayectoria + nodos vistos van como
    CONTEXTO (no como tool): el verificador parte de lo que el agente hizo y vio."""
    rep = load_rep(label, run, qid)
    tr = rep.get("trace") or {}
    pregunta = tr.get("question") or ""
    final = tr.get("final_json") or {}
    categoria = rep.get("categoria")

    # Síntoma: las afirmaciones que el juez marcó incorrectas.
    verifs = ((rep.get("judge") or {}).get("step2") or {}).get("verificaciones") or []
    fallidos = [v for v in verifs if v.get("verdict") in ("falso", "no_soportado")]
    if fallidos:
        sintoma = "\n".join(
            f'  - [{v.get("verdict")}{"/central" if v.get("central") else ""}] "{v.get("enunciado")}"'
            for v in fallidos)
    else:
        sintoma = "  (el juez no expuso afirmaciones desagregadas; revisá la respuesta final completa)"

    # Trayectoria del agente: qué tools llamó y qué vio (truncado, como en la traza).
    steps = tr.get("steps") or []
    if steps:
        traj = "\n".join(
            f'  {s.get("n")}. {s.get("tool")}({json.dumps(s.get("input"), ensure_ascii=False)})'
            f'\n       → {(s.get("output_truncado") or "")}'
            for s in steps)
    else:
        traj = "  (sin tool calls registrados)"

    # Contenido ÍNTEGRO (sin truncar a 1200) de los nodos que el agente vio.
    try:
        seen = recover_seen(run, label, pregunta)
    except Exception as e:  # robustez: si no se puede recuperar, seguimos con la trayectoria
        seen = []
    if seen:
        nodos_txt = "\n".join(
            f'  - id="{c["id"]}" [{c.get("acceso")}] label="{c.get("label")}"'
            f'\n       contenido: {(c.get("contenido") or "")}'
            f'\n       provenances: {json.dumps(c.get("provenances") or [], ensure_ascii=False)}'
            for c in seen)
    else:
        nodos_txt = "  (no se pudieron recuperar los nodos vistos desde la caché; usá las tools)"

    citas = "; ".join(f'{c.get("source_doc")} :: {c.get("location")}'
                      for c in (final.get("citas") or [])) or "(ninguna)"

    contexto = f"""FALLA A INVESTIGAR — pregunta {qid} (categoría: {categoria}) sobre el grafo {run}.

PREGUNTA:
{pregunta}

--- SÍNTOMA: afirmaciones que el juez marcó incorrectas ---
{sintoma}

--- RESPUESTA FINAL DEL AGENTE ---
respuesta: {final.get('respuesta')}
citas: {citas}
respondible (declarado por el agente): {final.get('respondible')}

--- TRAYECTORIA DEL AGENTE (qué tools llamó y qué devolvieron) ---
{traj}

--- NODOS QUE EL AGENTE VIO (contenido íntegro, sin truncar) ---
{nodos_txt}

Investigá por qué falló y atribuí la causa con evidencia, siguiendo el método. Podés consultar \
CUALQUIER nodo del grafo {run} (no solo los de arriba) y leer el PDF fuente con las tools. \
Cuando tengas evidencia suficiente, devolvé el JSON del contrato."""

    return {"pregunta": pregunta, "categoria": categoria, "contexto": contexto,
            "n_seen": len(seen), "n_claims_fallidos": len(fallidos)}


# --------------------------------------------------------------------------- #
# El agente verificador (loop espejo de GraphAgent.ask)                        #
# --------------------------------------------------------------------------- #
def _truncate(s: str, n: int = TRUNC) -> str:
    return s if len(s) <= n else s[:n] + f"… [+{len(s)-n} chars]"


class VerificadorAgente:
    """Loop agéntico de atribución sobre UN grafo. `investigar()` es stateless entre fallas:
    construye su propio historial de mensajes en cada llamada → aislamiento conversacional.
    El índice (read-only) y el cliente (caché) se comparten; el DIÁLOGO no."""

    def __init__(self, kg, client):
        self.kg = kg
        self.index = GraphIndex(kg)
        self.client = client

    def _run_tool(self, name: str, args: dict):
        if name == "buscar_nodos":
            return self.index.buscar_nodos(args.get("consulta", ""), args.get("limite", 10))
        if name == "ver_nodo":
            return self.index.ver_nodo(args.get("id", ""))
        if name == "ver_vecinos":
            return self.index.ver_vecinos(args.get("id", ""), args.get("direccion", "ambas"))
        if name == "leer_pasaje_pdf":
            return _leer_pasaje_pdf(args)
        return {"error": f"tool desconocida: {name}"}

    def investigar(self, id_falla: str, run: str, contexto: str) -> dict:
        """Investiga una falla aislada y devuelve el contrato de salida. id_falla/run se fijan
        de forma autoritativa acá (no se confía en lo que ponga el modelo)."""
        messages = [{"role": "user", "content": contexto}]
        steps, api_calls = [], []
        tokens_in = tokens_out = tool_calls_used = 0
        final_raw, final_json, error = None, None, None
        force_final = False
        t0 = time.monotonic()
        try:
            while True:
                kwargs = dict(model=MODEL_VERIF, max_tokens=MAX_TOKENS,
                              system=SYSTEM_PROMPT, messages=messages, tools=VERIF_TOOLS)
                # OJO: Opus 4.8 rechaza `temperature` → NO se pasa.
                if force_final:
                    kwargs["tool_choice"] = {"type": "none"}
                resp = self.client.messages.create(**kwargs)
                u = resp.usage
                tokens_in += getattr(u, "input_tokens", 0) or 0
                tokens_out += getattr(u, "output_tokens", 0) or 0
                api_calls.append({"stop_reason": resp.stop_reason,
                                  "input_tokens": getattr(u, "input_tokens", 0),
                                  "output_tokens": getattr(u, "output_tokens", 0)})

                if resp.stop_reason == "tool_use":
                    messages.append({"role": "assistant", "content": resp.content})
                    tool_results = []
                    for block in resp.content:
                        if getattr(block, "type", "") != "tool_use":
                            continue
                        tool_calls_used += 1
                        result = self._run_tool(block.name, block.input or {})
                        result_str = json.dumps(result, ensure_ascii=False)
                        steps.append({"n": tool_calls_used, "tool": block.name,
                                      "input": block.input,
                                      "output_truncado": _truncate(result_str)})
                        tool_results.append({"type": "tool_result", "tool_use_id": block.id,
                                             "content": result_str})
                    messages.append({"role": "user", "content": tool_results})
                    if tool_calls_used >= MAX_TOOL_CALLS:
                        force_final = True
                        messages.append({"role": "user",
                                         "content": (f"Alcanzaste el límite de {MAX_TOOL_CALLS} tool "
                                                     "calls. Devolvé AHORA el JSON del contrato con la "
                                                     "evidencia ya recolectada.")})
                    continue

                # respuesta final
                final_raw = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
                final_json = _extract_json(final_raw)
                break
        except Exception as e:  # loguear cualquier fallo de API/parse sin tumbar la corrida
            error = f"{type(e).__name__}: {e}"

        # Contrato autoritativo: id_falla/run los fija el orquestador, no el modelo.
        atribuciones = (final_json or {}).get("atribuciones") if isinstance(final_json, dict) else None
        return {
            "id_falla": id_falla,
            "run": run,
            "atribuciones": atribuciones or [],
            "razonamiento": (final_json or {}).get("razonamiento") if isinstance(final_json, dict) else None,
            "confianza": (final_json or {}).get("confianza") if isinstance(final_json, dict) else None,
            # auditoría (no es parte del contrato, ayuda a calibrar):
            "_meta": {
                "parse_ok": isinstance(final_json, dict) and "atribuciones" in (final_json or {}),
                "tool_calls_used": tool_calls_used,
                "tokens_in": tokens_in, "tokens_out": tokens_out,
                "latency_s": round(time.monotonic() - t0, 3),
                "error": error,
                "final_raw": final_raw,
                "trayectoria_verificador": steps,
                "api_calls": api_calls,
            },
        }


# --------------------------------------------------------------------------- #
# Cliente cacheado (Opus) — mismo patrón que run_posthoc.build_clients         #
# --------------------------------------------------------------------------- #
def build_verificador_client(real_client, kg, *, db_path: Path = DB_PATH, run_label: str = "verificador"):
    """CachingClient para el verificador. El namespace incluye el graph_fingerprint del run
    (el verificador SÍ consume el grafo) + code_ver, think=0 (no thinking)."""
    kg_path = getattr(kg, "path", None)
    if not kg_path or not Path(kg_path).exists():
        raise RuntimeError("KnowledgeGraph sin .path válido: el graph_fingerprint se degradaría. Abortando.")
    gfp = lc.graph_fingerprint(kg)
    return lc.CachingClient(
        real_client, domain="verificador", db_path=db_path,
        namespace=lc.make_namespace("verificador", code_ver=CODE_VER, graph_fp=gfp, thinking=False),
        thinking_enabled=False, run_label=run_label)


def investigar_falla(real_client, label: str, run: str, qid: str, *,
                     db_path: Path = DB_PATH, _kg_cache: dict | None = None) -> dict:
    """Orquesta UNA falla aislada: carga el grafo del run, arma el contexto, y corre un
    VerificadorAgente con historial nuevo. Aislamiento: cada llamada parte de cero."""
    _kg_cache = _kg_cache if _kg_cache is not None else {}
    if run not in _kg_cache:
        _kg_cache[run] = load_graph(run)   # carga de disco (read-only); NO es contexto conversacional
    kg = _kg_cache[run]
    ctx = build_falla_context(label, run, qid)
    client = build_verificador_client(real_client, kg, db_path=db_path)
    agente = VerificadorAgente(kg, client)
    rec = agente.investigar(id_falla=f"{run}/{qid}", run=run, contexto=ctx["contexto"])
    rec["_meta"]["contexto_stats"] = {k: ctx[k] for k in ("n_seen", "n_claims_fallidos", "categoria")}
    return rec


# --------------------------------------------------------------------------- #
# CLI                                                                          #
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description="Verificador agéntico de atribución (Paso 3).")
    ap.add_argument("--label", default="off", help="off|on (subcarpeta de posthoc_run/traces)")
    ap.add_argument("--run", default="run_3", help="run_1..run_5 (def. run_3)")
    ap.add_argument("--qid", default="CQ-017", help="id de la pregunta a investigar")
    ap.add_argument("--context", action="store_true",
                    help="OFFLINE: arma e imprime el contexto de la falla + el tool set, SIN llamar a la API.")
    args = ap.parse_args()

    if args.context:
        # Modo de revisión del cableado: no requiere API ni gasta.
        ctx = build_falla_context(args.label, args.run, args.qid)
        print(f"== CONTEXTO de la falla {args.run}/{args.qid} (label={args.label}) ==")
        print(f"   nodos vistos recuperados: {ctx['n_seen']} | claims fallidos: {ctx['n_claims_fallidos']}")
        print(f"   tools del verificador: {[t['name'] for t in VERIF_TOOLS]}")
        print("\n" + ctx["contexto"])
        return 0

    # Modo real (requiere API). NO se ejecuta como parte de la construcción; lo dispara la calibración.
    from dotenv import load_dotenv
    import os, anthropic
    load_dotenv(EVAL_DIR / ".env")
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit("ANTHROPIC_API_KEY no seteada en evaluacion/.env")
    real = anthropic.Anthropic(max_retries=3)
    rec = investigar_falla(real, args.label, args.run, args.qid)
    print(json.dumps(rec, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
