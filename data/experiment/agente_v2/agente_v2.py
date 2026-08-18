"""
agente_v2.py — GraphAgentV2: el agente del harness con las TOOLS v2 sobre
Neo4j (U-A1.2). Subclase de `GraphAgent`; el harness congelado NO se edita.

Qué es IGUAL al harness (por import, no por copia): MODEL, TEMPERATURE,
MAX_TOKENS, MAX_TOOL_CALLS, SYSTEM_PROMPT (default), QuestionTrace,
_truncate, _extract_json, _cita_fiel, _apply_cache_breakpoint, precios,
`_collect_provs` (heredado), el mensaje de límite de tool calls.

Qué cambia: `_run_tool` despacha a `ToolsV2` (tools_v2.py) y el request a la
API lleva `tools=TOOLS_V2` (specs_tools_v2.json). Como `GraphAgent.ask` lee
`TOOLS` y `SYSTEM_PROMPT` como globales del módulo harness en cada llamada,
no hay forma de inyectar otras specs sin editar el harness o copiar el loop:
se COPIA `ask` con exactamente DOS sustituciones (`system=SYSTEM_PROMPT` →
`system=self.system_prompt`; `tools=TOOLS` → `tools=self.tools`). El selftest
verifica textualmente que el fuente de `GraphAgentV2.ask` es el de
`GraphAgent.ask` con esas dos sustituciones y ninguna otra diferencia, así el
loop no puede divergir silenciosamente.

Prompt del sistema: por default el del harness, VERBATIM (la variable de
A1.4 son las tools, no el prompt). El prompt del harness nombra las tools y
su semántica v1 ("búsqueda léxica de nodos por label/id";
"ver_vecinos(id, direccion)"); con las tools v2 esas dos frases quedan
desactualizadas. El ajuste mínimo se expone como `SYSTEM_PROMPT_V2_PROPUESTO`
(derivado del original por dos reemplazos de una frase cada uno, con
aserción de unicidad) y se activa SOLO con `prompt='propuesto'`; queda
pendiente de laudo — no se da por bueno en esta unidad.

Nombres de las tools que ve el modelo: los MISMOS que v1 (`buscar_nodos`,
`ver_nodo`, `ver_vecinos`) — así el prompt del harness sigue nombrando tools
existentes sin edición y las herramientas de análisis de trazas que cuentan
llamadas por nombre siguen aplicando; la distinción v1/v2 va en los
metadatos del agente (`backend`) y en los argumentos nuevos de las llamadas
(`relacion`, `pagina`, `por_pagina`). Los nombres de los métodos Python
llevan sufijo `_v2`.

Sin API en A1.2: la clase se define y se prueba solo su despacho de tools con
un cliente dummy. Correr el agente real (A1.4) exige declarar un namespace de
caché propio (payloads y specs distintos → llamadas distintas; ver
docs/decisiones_caching_extraccion.md y la skill llm-capture).

Uso
---
  from agente_v2 import GraphAgentV2
  from conexion import abrir_driver
  ag = GraphAgentV2(abrir_driver(), grafo="KG_Refinado")     # client=None -> anthropic.Anthropic()
  # ag.ask(qid, pregunta) -> QuestionTrace (paga API; fuera de A1.2)
"""

from __future__ import annotations

import inspect
import json
import sys
import time
from pathlib import Path

AGENTE_V2_DIR = Path(__file__).resolve().parent
NEO4J_DIR = AGENTE_V2_DIR.parent / "neo4j"
for _p in (str(NEO4J_DIR), str(AGENTE_V2_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from grafos import GRAFOS, GRAFO_DEFAULT  # noqa: E402  (A1.1)
from loader import KnowledgeGraph  # noqa: E402  (cuarteto: solo import)
import harness  # noqa: E402  (cuarteto: solo import)
from harness import (  # noqa: E402
    GraphAgent, QuestionTrace, MODEL, TEMPERATURE, MAX_TOKENS, MAX_TOOL_CALLS,
    SYSTEM_PROMPT, PRICE_IN_PER_M, PRICE_OUT_PER_M, CACHE_WRITE_MULT,
    CACHE_READ_MULT, _truncate, _extract_json, _cita_fiel, _apply_cache_breakpoint,
)
from tools_v2 import ToolsV2, TOOLS_V2  # noqa: E402

# --------------------------------------------------------------------------- #
# Prompt del sistema: harness verbatim (default) + ajuste mínimo PROPUESTO     #
# --------------------------------------------------------------------------- #
# Cada reemplazo toca UNA frase del prompt original y exige que aparezca
# exactamente una vez (si el harness cambiara, esto falla ruidosamente).
_REEMPLAZOS_PROMPT = [
    (
        "- buscar_nodos(consulta, limite): búsqueda léxica de nodos por label/id. Empezá \\\n"
        "siempre por acá para encontrar puntos de entrada.",
        "- buscar_nodos(consulta, limite): búsqueda de texto completo (BM25) de nodos por \\\n"
        "label, id y descripción. Empezá siempre por acá para encontrar puntos de entrada.",
    ),
    (
        "- ver_vecinos(id, direccion): devuelve los edges (relaciones) entrantes/salientes \\\n"
        "de un nodo, con el vecino y las provenances del edge.",
        "- ver_vecinos(id, relacion, pagina): devuelve los edges (relaciones) entrantes y \\\n"
        "salientes de un nodo en una sola llamada, paginados y filtrables por relación, con el \\\n"
        "vecino y las provenances del edge.",
    ),
]


def _prompt_propuesto() -> str:
    # El SYSTEM_PROMPT del harness es un literal con continuaciones de línea
    # ("\<newline>"): en runtime esas continuaciones NO existen, así que los
    # patrones se aplican sobre el texto ya unido.
    p = SYSTEM_PROMPT
    for viejo, nuevo in _REEMPLAZOS_PROMPT:
        viejo_rt = viejo.replace("\\\n", "")
        nuevo_rt = nuevo.replace("\\\n", "")
        n = p.count(viejo_rt)
        if n != 1:
            raise RuntimeError(f"prompt del harness: la frase esperada aparece {n} veces: {viejo_rt!r}")
        p = p.replace(viejo_rt, nuevo_rt)
    return p


SYSTEM_PROMPT_V2_PROPUESTO = _prompt_propuesto()
PROMPTS = {"harness": SYSTEM_PROMPT, "propuesto": SYSTEM_PROMPT_V2_PROPUESTO}


def _kg_vacio(grafo: str) -> KnowledgeGraph:
    # Igual que agente_neo4j.GraphAgentNeo4j: el __init__ del harness exige un
    # KnowledgeGraph para armar su GraphIndex; se le da uno vacío para que no
    # exista un índice in-memory paralelo (segunda fuente de verdad silenciosa).
    g = GRAFOS[grafo]
    return KnowledgeGraph(run_key=f"neo4j_v2:{grafo}", path=g["path"],
                          nodes=[], edges=[], raw_node_count=0, raw_edge_count=0,
                          merges=[])


class GraphAgentV2(GraphAgent):
    """GraphAgent del harness con tools v2 (ToolsV2 sobre Neo4j) y specs v2."""

    def __init__(self, driver, grafo: str = GRAFO_DEFAULT, client=None,
                 cache_conversation=False, prompt: str = "harness"):
        if prompt not in PROMPTS:
            raise ValueError(f"prompt desconocido: {prompt!r}; válidos: {list(PROMPTS)}")
        super().__init__(_kg_vacio(grafo), client=client,
                         cache_conversation=cache_conversation)
        self.tools_v2 = ToolsV2(driver, grafo=grafo)
        self.index = self.tools_v2.index      # Neo4jIndex fulltext (por si algo lo consulta)
        self.tools = TOOLS_V2                  # specs que ve el modelo
        self.prompt_variante = prompt
        self.system_prompt = PROMPTS[prompt]

    def _run_tool(self, name: str, args: dict):
        return self.tools_v2.despachar(name, args or {})

    @property
    def backend(self) -> dict:
        g = GRAFOS[self.tools_v2.grafo]
        return {"backend": "neo4j", "tools_version": "v2", "grafo": self.tools_v2.grafo,
                "nombre_canonico": g["nombre_canonico"], "kg_sha256": g["sha256"],
                "modo_busqueda": "fulltext", "indice_fulltext": self.tools_v2.index.indice,
                "prompt": self.prompt_variante, "model": MODEL}

    # ------------------------------------------------------------------ #
    # ask: COPIA del harness (líneas 467-582 de harness.py) con exactamente
    # dos sustituciones (system=..., tools=...). Verificado textualmente en
    # el selftest contra `inspect.getsource(GraphAgent.ask)`.
    # ------------------------------------------------------------------ #
    def ask(self, qid: str, question: str) -> QuestionTrace:
        tr = QuestionTrace(qid=qid, question=question)
        seen = set()
        messages = [{"role": "user", "content": question}]
        t0 = time.monotonic()
        force_final = False
        try:
            while True:
                if self.cache_conversation:
                    _apply_cache_breakpoint(messages)
                kwargs = dict(model=MODEL, max_tokens=MAX_TOKENS,
                              temperature=TEMPERATURE, system=self.system_prompt,
                              messages=messages, tools=self.tools)
                if force_final:
                    # Mantener `tools` en el request (el historial tiene bloques
                    # tool_use; omitir tools haría que la API lo rechace) pero
                    # prohibir nuevas tool calls para forzar la respuesta final.
                    kwargs["tool_choice"] = {"type": "none"}
                c0 = time.monotonic()
                resp = self.client.messages.create(**kwargs)
                dt = time.monotonic() - c0

                u = resp.usage
                cin = getattr(u, "cache_read_input_tokens", 0) or 0
                cwr = getattr(u, "cache_creation_input_tokens", 0) or 0
                tr.tokens_in += u.input_tokens
                tr.tokens_out += u.output_tokens
                tr.cache_read += cin
                tr.cache_write += cwr
                tr.api_calls.append({
                    "stop_reason": resp.stop_reason,
                    "input_tokens": u.input_tokens, "output_tokens": u.output_tokens,
                    "cache_read": cin, "cache_write": cwr,
                    "latency_s": round(dt, 3),
                })

                if resp.stop_reason == "tool_use":
                    messages.append({"role": "assistant", "content": resp.content})
                    tool_results = []
                    for block in resp.content:
                        if block.type != "tool_use":
                            continue
                        tr.tool_calls_used += 1
                        result = self._run_tool(block.name, block.input or {})
                        self._collect_provs(result, seen, tr.seen_provenances)
                        result_str = json.dumps(result, ensure_ascii=False)
                        tr.steps.append({
                            "n": tr.tool_calls_used,
                            "tool": block.name,
                            "input": block.input,
                            "output_truncado": _truncate(result_str),
                            "output_chars": len(result_str),
                        })
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result_str,
                        })
                    messages.append({"role": "user", "content": tool_results})

                    if tr.tool_calls_used >= MAX_TOOL_CALLS:
                        tr.hit_tool_limit = True
                        force_final = True
                        messages.append({
                            "role": "user",
                            "content": ("Alcanzaste el límite de 15 tool calls. "
                                        "Respondé AHORA con el JSON final según el "
                                        "formato indicado, usando solo la evidencia "
                                        "ya recolectada."),
                        })
                    continue

                # end_turn / max_tokens / forced final: respuesta final
                tr.final_stop_reason = resp.stop_reason
                if resp.stop_reason == "max_tokens":
                    tr.truncated_max_tokens = True
                final_text = "".join(
                    b.text for b in resp.content if getattr(b, "type", "") == "text"
                )
                tr.final_raw = final_text
                parsed, err = _extract_json(final_text)
                if parsed is not None:
                    tr.final_json = parsed
                    tr.parse_ok = True
                    # validar citas contra provenances vistas (raw + normalizado)
                    seen_keys = {(p["source_doc"], p["location"])
                                 for p in tr.seen_provenances}
                    for c in (parsed.get("citas") or []):
                        if isinstance(c, dict):
                            key = (c.get("source_doc"), c.get("location"))
                            if key not in seen_keys:
                                tr.citations_unseen_raw.append(c)
                            if not _cita_fiel(c, tr.seen_provenances):
                                tr.citations_unseen_normalized.append(c)
                elif tr.truncated_max_tokens:
                    # No es un parse error genuino: el JSON quedó cortado porque
                    # la respuesta alcanzó max_tokens. Se distingue explícitamente.
                    tr.parse_error = (
                        f"JSON truncado por max_tokens ({MAX_TOKENS}); "
                        f"NO es un parse error genuino. Detalle del parser: {err}"
                    )
                else:
                    tr.parse_error = err
                break
        except Exception as e:  # noqa: BLE001 — loguear cualquier fallo de API/parse
            tr.error = f"{type(e).__name__}: {e}"

        tr.latency_s = round(time.monotonic() - t0, 3)
        tr.cost_usd = round(
            (tr.tokens_in * PRICE_IN_PER_M
             + tr.cache_write * PRICE_IN_PER_M * CACHE_WRITE_MULT
             + tr.cache_read * PRICE_IN_PER_M * CACHE_READ_MULT) / 1e6
            + (tr.tokens_out * PRICE_OUT_PER_M) / 1e6,
            6,
        )
        return tr


# --------------------------------------------------------------------------- #
# Verificación textual del loop copiado (la usa el selftest; también se puede
# invocar a mano).
# --------------------------------------------------------------------------- #
SUSTITUCIONES_ASK = (("system=SYSTEM_PROMPT,", "system=self.system_prompt,"),
                     ("tools=TOOLS)", "tools=self.tools)"))


def verificar_ask_copiado() -> dict:
    """True si fuente(GraphAgentV2.ask) == fuente(GraphAgent.ask) con las dos
    sustituciones declaradas y NINGUNA otra diferencia."""
    orig = inspect.getsource(GraphAgent.ask)
    copia = inspect.getsource(GraphAgentV2.ask)
    esperado = orig
    conteos = {}
    for viejo, nuevo in SUSTITUCIONES_ASK:
        conteos[viejo] = esperado.count(viejo)
        esperado = esperado.replace(viejo, nuevo)
    return {"identico_salvo_sustituciones": copia == esperado,
            "conteo_sustituciones": conteos,
            "lineas_ask_harness": len(orig.splitlines()),
            "lineas_ask_v2": len(copia.splitlines())}


if __name__ == "__main__":
    print(json.dumps(verificar_ask_copiado(), ensure_ascii=False, indent=1))
    print("--- SYSTEM_PROMPT_V2_PROPUESTO ---")
    print(SYSTEM_PROMPT_V2_PROPUESTO)
