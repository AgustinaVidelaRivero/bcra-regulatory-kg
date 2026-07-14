"""
verificador.py — Verificador agéntico de calidad del KG (Paso 3 de la skill kg-refinement, Fase 2.4).

v5: taxonomía de DOS CAPAS por REFERENCIA — el system prompt se ENSAMBLA en runtime leyendo
references/taxonomia.md de la skill (capas, tablas de causas, regla de precedencia, árbol de
decisión, piezas de evidencia, atribución múltiple). Hardcodeado queda SOLO: rol, procedimiento
en fases (con la FASE C partida en C1-síntoma / C2-causa), contrato de salida y ejemplos
resueltos (en vocabulario v2, de run_1/run_5 — nunca de run_3 ni de los casos del dev set).
El contrato ya NO incluye auto-reporte de confianza; en su lugar hay VALIDACIÓN PROGRAMÁTICA
del JSON (con UN reintento ante error específico; si falla de nuevo → formato_invalido, fallo
ruidoso) y DETECTORES post-proceso (flag_encuadre_invertido, flag_contexto, tokens). El
ensamblado NUNCA lee referencias_dev_set.md ni casos_control.md (guard programático).

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
import importlib.util
import json
import re
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
MAX_TOKENS = 8192            # v4: la salida creció (extraccion_traza + quotes verbatim); 4096 arriesgaba truncar el JSON final
MAX_TOOL_CALLS = 40                 # techo de seguridad alto: cuántas usar es criterio del agente
TRUNC = 1200                        # truncado de outputs de tool EN LA TRAZA de auditoría (no en el prompt al modelo)
TRUNC_THINK = 1500                  # v4 (CAMBIO 5c): truncado del thinking del agente POR TURNO en el contexto

DB_PATH = EVAL_DIR / "cache" / "verificador.db"   # separada de calls.db y verifier_pilot.db
CODE_VER = "verificador-v5"   # v5: taxonomía v2 por referencia + FASE C partida (C1 síntoma / C2 causa) + validación programática + detectores. v1..v4 intactos bajo sus namespaces.

# Taxonomía v2 CERRADA (los NOMBRES, para validación programática; el CONTENIDO — tablas,
# precedencia, árbol — viene POR REFERENCIA de references/taxonomia.md, ver taxonomia_section()).
SINTOMAS_CAPA1 = ["faithfulness", "noise_sensitivity", "context_recall"]
CATEGORIAS_GRAFO = ["contenido_kg", "completitud_kg", "estructural_kg", "provenance_imprecisa",
                    "alcanzabilidad_kg"]
CATEGORIAS_AGENTE = ["navegación", "alucinacion_agente"]
CATEGORIAS_NINGUNO = ["sin_defecto"]
CATEGORIAS_INDETERMINADO = ["frontera_no_determinada"]
LADO_POR_CAUSA = {**{c: "grafo" for c in CATEGORIAS_GRAFO},
                  **{c: "agente" for c in CATEGORIAS_AGENTE},
                  **{c: "ninguno" for c in CATEGORIAS_NINGUNO},
                  **{c: "indeterminado" for c in CATEGORIAS_INDETERMINADO}}
BUSQUEDAS_OBLIGATORIAS = {"completitud_kg", "alcanzabilidad_kg", "frontera_no_determinada"}

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
# System prompt v5 — ENSAMBLADO en runtime: taxonomía POR REFERENCIA           #
# (references/taxonomia.md) + rol/fases/contrato/ejemplos hardcodeados.        #
# --------------------------------------------------------------------------- #
# Única fuente externa permitida del ensamblado. El guard de _assert_fuentes()
# garantiza que NO se lean referencias_dev_set.md ni casos_control.md.
TAXONOMIA_MD = EVAL_DIR.parents[2] / ".claude" / "skills" / "kg-refinement" / "references" / "taxonomia.md"
_FUENTES_PROHIBIDAS = ("referencias_dev_set", "casos_control")

_TAXONOMIA_CACHE: str | None = None
_PROMPT_CACHE: str | None = None


def taxonomia_section() -> str:
    """Extrae de references/taxonomia.md el bloque de la taxonomía v2 que va POR REFERENCIA
    al prompt: Capa 1 (con la regla de precedencia POR PATA), Capa 2 (tablas de causas con su
    evidencia) y el árbol de decisión capa 1 → capa 2. Fallo RUIDOSO si los marcadores no están
    (preferimos abortar a degradar a un prompt sin taxonomía o con una copia vieja)."""
    global _TAXONOMIA_CACHE
    if _TAXONOMIA_CACHE is not None:
        return _TAXONOMIA_CACHE
    if not TAXONOMIA_MD.exists():
        raise RuntimeError(f"No se encontró {TAXONOMIA_MD}. El prompt v5 se ensambla desde ese "
                           "archivo; sin él no hay taxonomía. Abortando.")
    txt = TAXONOMIA_MD.read_text(encoding="utf-8")
    ini = txt.find("## Capa 1")
    fin = txt.find("## Las tres piezas")
    if ini == -1 or fin == -1 or fin <= ini:
        raise RuntimeError(f"Marcadores '## Capa 1' / '## Las tres piezas' no encontrados "
                           f"en {TAXONOMIA_MD}: la estructura cambió. Abortando (no se degrada).")
    sec = txt[ini:fin].rstrip().rstrip("-").rstrip()
    # Sanitización de referencias cruzadas (decisión 9): taxonomia.md apunta a los materiales
    # de calibración ("Ver CQ-017 en `casos_control.md`", "(ver `casos_control.md`)") que el
    # verificador NUNCA debe ver ni mencionar. Se remueven los PUNTEROS (no contenido de la
    # taxonomía). Si tras sanitizar queda alguna mención, _assert_fuentes aborta ruidoso.
    sec = re.sub(r"\s*Ver CQ-\d+ en `casos_control\.md`\.", "", sec)
    sec = re.sub(r"\s*y con la regla de calibración \(ver `casos_control\.md`\)", "", sec)
    sec = re.sub(r"\s*\(ver `casos_control\.md`\)", "", sec)
    _assert_fuentes(sec, str(TAXONOMIA_MD))
    if re.search(r"\bCQ-\d+\b", sec):
        raise RuntimeError(f"La sección ensamblada desde {TAXONOMIA_MD} menciona casos concretos "
                           "(CQ-*) tras la sanitización: eso filtra material de calibración al "
                           "prompt. Abortando.")
    _TAXONOMIA_CACHE = sec
    return _TAXONOMIA_CACHE


def _assert_fuentes(texto: str, origen: str) -> None:
    """Guard (decisión 9): el material ensamblado no puede levantar las referencias de
    calibración (dev set) ni el gate (casos-control)."""
    hits = [f for f in _FUENTES_PROHIBIDAS if f in texto]
    if hits:
        raise RuntimeError(f"El material de {origen} menciona fuentes prohibidas para el prompt "
                           f"del verificador: {hits}. Abortando.")


_PROMPT_HEAD = """\
Sos un VERIFICADOR DE CALIDAD de un Knowledge Graph (KG) regulatorio del BCRA. Te doy UNA falla \
del sistema KG-RAG (una pregunta cuya respuesta el juez marcó como incorrecta) y tenés que \
investigar POR QUÉ falló y ATRIBUIR la causa con evidencia, dentro de la taxonomía de DOS CAPAS \
(sección TAXONOMÍA). Toda atribución emite el PAR {sintoma_capa1, causa_capa2}.

MÉTODO (obligatorio, es lo que hace válida la atribución):
1. Arrancá desde el SÍNTOMA ("esta respuesta falló"), NO desde el nodo. NO asumas de entrada que \
el problema es el grafo ni que es el agente: empezar mirando un nodo predispone a culpar al grafo.
2. Recolectá EVIDENCIA ANTES de concluir. No formes una hipótesis de entrada y busques solo lo que \
la confirma.
3. Cada atribución lleva las TRES piezas de evidencia de la sección TAXONOMÍA (afirmación / nodo / \
fuente), con anclaje textual {quote, ubicacion}. El cruce de las tres decide el par.
4. DESCOMPONÉ la pregunta en sus PATAS (partí de la descomposición del juez que viene en el \
contexto) y tratá cada una por separado: una falla puede romperse en una pata y estar bien en otra. \
Investigá la fuente de CADA pata fallida antes de concluir: \
una pata sin verificar es evidencia FALTANTE.
5. No cierres por COINCIDENCIA SUPERFICIAL. Que un nodo comparta palabras con la pregunta no \
significa que la responda. Antes de cerrar, chequeá: (a) ¿leíste con leer_pasaje_pdf la fuente de \
cada pata fallida?; (b) ¿abriste con ver_nodo el CONTENIDO de los nodos que vas a citar (no \
solo su label/resumen)? Si alguna respuesta es "no", no concluyas todavía.

PROCEDIMIENTO (en este orden — cada fase alimenta a la siguiente):
FASE A — EXTRACCIÓN (SOLO con el contexto que te di, sin tools). De la traza, extraé y listá:
  A1. cada tool call del agente con sus argumentos;
  A2. qué devolvió cada una, y si el resultado era PERTINENTE a la pregunta o no;
  A3. si existe, en qué paso el agente tomó la decisión que llevó al error (con cita textual); si \
el agente actuó bien sobre lo que tenía, declaralo explícitamente — esa constatación es evidencia \
de lado GRAFO, no un campo vacío;
  A4. si hay thinking en la trayectoria: el fragmento donde razona esa decisión (si en A3 no hay \
decisión errónea, queda en null por esa razón);
  A5. las patas de la pregunta según la descomposición del juez (step1, viene en el contexto).
El resultado de esta fase va TAL CUAL en el campo "extraccion_traza" del JSON final.
FASE B — INVESTIGACIÓN: por cada pata fallida, el cruce de las tres fuentes (afirmación / nodo / \
PDF) con las tools. Si el contexto trae el ESQUEMA DEL GRAFO, \
usalo para razonar qué nodo/arista DEBERÍA existir para responder, y chequeá si existe. Si una pata quedó \
sin su dato (context_recall), probá VOS si el nodo portador se alcanza buscando con los términos \
de la PREGUNTA — esa prueba decide navegación vs alcanzabilidad_kg (árbol).
FASE C — ATRIBUCIÓN, en DOS sub-fases (recién acá etiquetás):
  C1 — SÍNTOMA: por cada pata/claim fallido, clasificá el síntoma (capa 1) aplicando la REGLA DE \
PRECEDENCIA POR PATA de la sección TAXONOMÍA, en su orden.
  C2 — CAUSA: por cada síntoma clasificado, respondé SU pregunta decisoria del ÁRBOL DE DECISIÓN \
(capa 2) y emití el par {sintoma_capa1, causa_capa2}. Una causa sin síntoma clasificado NO valida.

TOOLS (para la FASE B; cuáles y cuántas veces es tu criterio):
- buscar_nodos / ver_nodo / ver_vecinos: exploran el MISMO grafo que usó el agente. Podés mirar \
CUALQUIER nodo, no solo los que el agente vio. OJO: buscar_nodos indexa SOLO label e id (no las \
descriptions).
- leer_pasaje_pdf(source_doc, location): qué dice realmente el PDF fuente.

REGLA OPERATIVA DE ANCLAJE: si el quote que necesitás de la trayectoria quedó cortado por el \
truncado (…), NO completes de memoria: re-abrí la fuente con las tools y citá desde ahí. EXCEPCIÓN — el thinking NO se puede re-abrir: \
citá lo que hay y declaralo cortado.

--- TAXONOMÍA (dos capas, CERRADA — no inventes categorías; si algo no entra, decilo en el \
razonamiento) ---
"""

_PROMPT_TAIL = """

EVIDENCIA Y JERARQUÍA (reglas del contrato):
- Cada pieza de evidencia es {quote, ubicacion}: quote VERBATIM (tal cual la tool o la traza, NO \
parafraseado); ubicacion = id de nodo / source_doc+location del PDF / "paso N de la trayectoria" \
/ "respuesta final".
- "busquedas" (lista de {consulta, resultado}) es OBLIGATORIO para completitud_kg, \
alcanzabilidad_kg y frontera_no_determinada; para el resto, incluilo si una búsqueda tuya fue \
parte de la evidencia. frontera_no_determinada exige además "entre" (las DOS causas en disputa) \
y "evidencia_faltante" (qué evidencia decidiría el caso).
- ATRIBUCIÓN MÚLTIPLE: "jerarquia": "primaria" = mueve el veredicto; "secundaria" = presente pero \
no rompe la respuesta. Puede haber MÁS DE UNA primaria (patas independientes rotas por defectos \
distintos; usá el campo "pata"). Toda atribución lleva igual sus tres piezas.
- sin_defecto (falso positivo del juez) es de ÚLTIMO RECURSO: exige descartar activamente cada \
defecto de la taxonomía y documentar el descarte en el razonamiento.

EJEMPLOS RESUELTOS — ADVERTENCIAS: (a) son de OTROS grafos (run_1, run_5): sus nodos y valores no \
tienen por qué existir en el que investigás; enseñan el MÉTODO, no hechos del dominio. (b) No \
asumas que tu caso se parece a alguno: la atribución sale de TU evidencia.

EJEMPLO 1 — {noise_sensitivity, contenido_kg}, run_5. El agente respondió "1.500 millones" a la \
exigencia básica de un banco; el juez lo marcó falso. C1: claim SOPORTADO por nodo consultado e \
incorrecto contra el PDF → noise_sensitivity. C2: ¿el nodo es fiel al PDF? Contradice (valor de \
un período vencido) → contenido_kg, primaria.
  afirmacion: {"quote": "La exigencia básica de capital mínimo para un banco es de 1.500 millones \
de pesos.", "ubicacion": "respuesta final"}
  nodo: {"quote": "Integración de capital mínimo según categoría: 1.500 millones de pesos para \
Bancos, 700 millones para Restantes entidades (…) en período 01/06/24 a 31/12/24", "ubicacion": \
"exigencia_basica_de_capital (abierto por el agente)"}
  fuente: {"quote": "1.2. Exigencia básica. Según la clase de entidad, serán las siguientes \
exigencias básicas: Bancos Restantes entidades (…) -En millones de pesos- 5.000 2.500", \
"ubicacion": "TO_capitales_minimos_actual.pdf, Punto 1.2"}
El circuito se rompe en el nodo, no en el agente.

EJEMPLO 2 — {faithfulness, alucinacion_agente} modo (b), run_1. El juez marcó no_soportado la \
glosa "SEFYC significa Superintendencia de Entidades Financieras y Cambios". C1: ningún nodo de \
la trayectoria soporta esa expansión → faithfulness. C2: ¿el grafo tenía el dato afirmado? \
Búsqueda documentada: ningún nodo porta esa expansión; ¿el PDF? Tampoco la afirma (la sigla real \
del corpus es "Cambiarias", no "Cambios") → alucinacion_agente modo (b), secundaria (sin nodo que \
exhibir: la evidencia es la constancia de búsqueda + la verificación negativa del PDF).
  busquedas: [{"consulta": "SEFYC significado superintendencia", "resultado": "nodos que usan la \
sigla sin expandirla"}, {"consulta": "superintendencia \
entidades financieras cambios", "resultado": "ningún nodo ni pasaje afirma la expansión 'y Cambios'"}]
  afirmacion: {"quote": "SEFYC (Superintendencia de Entidades Financieras y Cambios)", \
"ubicacion": "respuesta final"}
  nodo: {"quote": "Valoración otorgada por SEFYC en última inspección respecto a entidad, \
sistemas informáticos y responsables de control interno, que reduce límites de riesgo \
operacional.", "ubicacion": "cla_calificacion_1_2_o_3_sefyc (usa la sigla sin expandirla)"}
  fuente: {"quote": "(verificación negativa: el pasaje del límite de riesgo operacional usa la \
sigla sin la expansión afirmada)", "ubicacion": "TO_capitales_minimos_actual.pdf, punto del \
límite de riesgo operacional"}

EJEMPLO 3 — {noise_sensitivity, sin_defecto} (falso positivo del juez), run_5. El juez marcó \
falso "con débito en cuenta, el límite mensual es USD 200". C1: soportado por nodo consultado → \
noise_sensitivity. C2: ¿el nodo es fiel al PDF? SÍ (USD 200 con débito; USD 100 en efectivo) → \
sin_defecto, primaria — vale porque el descarte de cada defecto quedó documentado.
  afirmacion: {"quote": "Si la operación de compra de moneda extranjera para atesorar se realiza \
con débito en cuenta, el límite mensual es USD 200 en el mes calendario.", "ubicacion": \
"respuesta final"}
  nodo: {"quote": "El cliente no puede superar el equivalente a USD 200 en el mes calendario en \
el conjunto de entidades y conceptos permitidos.", "ubicacion": "limite_mensual_de_usd_200 \
(abierto por el agente)"}
  fuente: {"quote": "3.9.1. El cliente no supere, en el mes calendario (…) el equivalente a USD \
200 (…) 3.9.2. La operación se curse con débito en cuenta del cliente (…) Si el cliente utiliza \
efectivo el monto comprado (…) no supere el equivalente a USD 100", "ubicacion": \
"TO_exterior_cambios_actual.pdf, Puntos 3.9.1-3.9.2"}

EJEMPLO NEGATIVO — error frecuente, NO HACER (run_1): en la misma pregunta de la exigencia \
básica, un verificador anterior etiquetó completitud_kg ("el valor no está en el grafo") para el \
claim de la fórmula general — TENIENDO el nodo portador del valor (cla_bancos: "…capital mínimo \
de 1.500 millones de pesos en el período 01/06/24 al 31/12/24") EN SU PROPIA EVIDENCIA del claim \
central de la misma falla. El dato no "faltaba": estaba, desactualizado → {noise_sensitivity, \
contenido_kg}. LECCIÓN: antes de atribuir completitud_kg, chequeá tu PROPIA evidencia ya juntada — \
la constancia de búsqueda incluye lo que ya viste en esta investigación.

SALIDA: cuando tengas evidencia suficiente, respondé con UN ÚNICO objeto JSON válido, sin texto \
adicional ni markdown, con exactamente esta forma (sin campos extra):
{
  "extraccion_traza": {
    "tool_calls": [
      {"paso": 1, "tool": "<tool>", "args": "<argumentos>",
       "devolvio": "<resumen>", "pertinente": true}
    ],
    "paso_decision_error": {"paso": 0, "quote": "<cita textual del paso de la decisión errónea>"} | null,
    "decision_agente_correcta": "<solo si paso_decision_error es null: por qué actuó bien>",
    "thinking_decision": "<fragmento del thinking de esa decisión; null si no hay thinking o no hay decisión errónea>",
    "patas": ["<patas según el step1 del juez>"]
  },
  "atribuciones": [
    {
      "sintoma_capa1": "faithfulness|noise_sensitivity|context_recall",
      "causa_capa2": "<una causa de la capa 2 de la TAXONOMÍA>",
      "lado": "grafo|agente|ninguno|indeterminado",
      "jerarquia": "primaria|secundaria",
      "pata": "<opcional: qué pata cubre>",
      "entre": ["<solo frontera: las DOS causas en disputa>"],
      "evidencia_faltante": "<solo frontera: qué evidencia decidiría el caso>",
      "evidencia": {
        "afirmacion": {"quote": "<VERBATIM: qué afirmó el agente>",
                       "ubicacion": "<'respuesta final' o 'paso N'>"},
        "nodo": {"quote": "<VERBATIM: contenido del/los nodo(s), o 'ninguno'>",
                 "ubicacion": "<id(s) de nodo>"},
        "fuente": {"quote": "<VERBATIM: qué dice el PDF>",
                   "ubicacion": "<source_doc + location>"}
      },
      "busquedas": [
        {"consulta": "<términos>", "resultado": "<resumen>"}
      ]
    }
  ],
  "razonamiento": "<cadena evidencia→conclusión>"
}

NO incluyas palanca de cambio ni nivel de riesgo: eso es del Paso 4, no tuyo."""


def system_prompt() -> str:
    """Ensambla el prompt v5 (cacheado). La taxonomía viene POR REFERENCIA de taxonomia.md:
    si ese archivo cambia, el prompt cambia solo (nada de la taxonomía vive hardcodeado acá)."""
    global _PROMPT_CACHE
    if _PROMPT_CACHE is None:
        prompt = _PROMPT_HEAD + taxonomia_section() + _PROMPT_TAIL
        _assert_fuentes(prompt, "el prompt ensamblado")
        _PROMPT_CACHE = prompt
    return _PROMPT_CACHE


# --------------------------------------------------------------------------- #
# Esquema del grafo (v4, CAMBIO 4) — levantado del repo, NO hardcodeado        #
# --------------------------------------------------------------------------- #
SCHEMA_BASE = EVAL_DIR.parent / "run_3_ppf_core"   # el esquema inyectado es el de ppf_core (run_3)

_ESQUEMA_CACHE: str | None = None


def esquema_grafo_section() -> str:
    """Arma la sección '--- ESQUEMA DEL GRAFO ---' desde las fuentes del repo:
      · run_3_ppf_core/code/schema.py — ENTITY_TYPES / PREDICATES / DOMAIN_RANGE (autoritativo).
      · run_3_ppf_core/schema.md     — definición por tipo (§2) y semántica por predicado (§3).
    Fallo RUIDOSO si algo falta o no parsea completo (mismo principio que el graph_fingerprint:
    preferimos abortar a degradar en silencio a una sección vacía)."""
    global _ESQUEMA_CACHE
    if _ESQUEMA_CACHE is not None:
        return _ESQUEMA_CACHE

    schema_py = SCHEMA_BASE / "code" / "schema.py"
    schema_md = SCHEMA_BASE / "schema.md"
    if not schema_py.exists() or not schema_md.exists():
        raise RuntimeError(f"Esquema de ppf_core no encontrado en {SCHEMA_BASE} "
                           "(faltan code/schema.py y/o schema.md). Abortando: no se degrada a sección vacía.")

    spec = importlib.util.spec_from_file_location("_ppf_schema", schema_py)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    types, preds, dr = mod.ENTITY_TYPES, mod.PREDICATES, mod.DOMAIN_RANGE
    if len(types) != 7 or len(preds) != 12:
        raise RuntimeError(f"Esquema inesperado en {schema_py}: {len(types)} tipos / {len(preds)} "
                           "predicados (se esperaban 7 / 12). Abortando.")

    txt = schema_md.read_text(encoding="utf-8")
    # Definición por tipo: '### 2.N <Tipo>' seguido de '**Definición.** <línea>'.
    defs = {m.group(1): m.group(2).strip() for m in
            re.finditer(r"###\s+2\.\d+\s+(\w+)\s*\n+\*\*Definición\.\*\*\s+([^\n]+)", txt)}
    # Semántica por predicado: columna final de la tabla de §3. Una celda puede contener
    # pipes escapados (\|) — p. ej. la fila de `limita` — así que la celda es ((?:\\\||[^|])+).
    _cell = r"(?:\\\||[^|\n])+"
    sems = {m.group(1): m.group(2).replace("\\|", "|").strip() for m in
            re.finditer(rf"^\|\s*\d+\s*\|\s*`(\w+)`\s*\|{_cell}\|{_cell}\|\s*({_cell}?)\s*\|\s*$",
                        txt, re.M)}
    faltantes = [t for t in types if t not in defs] + [p for p in preds if p not in sems]
    if faltantes:
        raise RuntimeError(f"schema.md no trae descripción para: {faltantes}. Abortando: no se degrada.")

    lines = ["TIPOS DE ENTIDAD (7):"]
    lines += [f"  - {t}: {defs[t]}" for t in types]
    lines.append("RELACIONES (12) — dominio → rango — semántica:")
    for p in preds:
        dom, ran = dr[p]
        lines.append(f"  - {p}: {{{', '.join(sorted(dom))}}} → {{{', '.join(sorted(ran))}}} — {sems[p]}")
    _ESQUEMA_CACHE = "\n".join(lines)
    return _ESQUEMA_CACHE


# --------------------------------------------------------------------------- #
# Construcción del contexto de la falla (trayectoria como CONTEXTO inicial)    #
# --------------------------------------------------------------------------- #
def _thinking_por_turno(rep: dict, steps: list) -> dict:
    """v4 (CAMBIO 5c): extrae los bloques thinking de raw_turns_agent (el crudo íntegro que
    guarda la captura), mapeados al n del PRIMER tool call de su turno. El turno final (sin
    tools) va con clave None. Trazas OFF no tienen bloques thinking → dict vacío.

    JOIN VERIFICADO raw↔steps (corre SIEMPRE, también en trazas OFF sin thinking): las dos
    numeraciones salen de conteos independientes (steps del loop del harness al ejecutar;
    acá, re-contando los tool_use del crudo). Una desalineación es CORRUPCIÓN DE DATOS de la
    traza, no un problema del render del thinking → fallo ruidoso, nunca intercalar en
    silencio en el paso equivocado."""
    out = {}
    n = 0  # numeración de steps: consecutiva sobre los tool_use en orden de turno
    for turn in rep.get("raw_turns_agent") or []:
        raw = (turn or {}).get("raw") or {}
        content = raw.get("content") or []
        think = "\n".join(b.get("thinking") or "" for b in content
                          if isinstance(b, dict) and b.get("type") == "thinking").strip()
        first_n = None
        for b in content:
            if not (isinstance(b, dict) and b.get("type") == "tool_use"):
                continue
            n += 1
            if first_n is None:
                first_n = n
            s = steps[n - 1] if n <= len(steps) else {}
            if not (s.get("n") == n and s.get("tool") == b.get("name")
                    and json.dumps(s.get("input"), sort_keys=True, ensure_ascii=False)
                    == json.dumps(b.get("input"), sort_keys=True, ensure_ascii=False)):
                raise RuntimeError(
                    f"Desalineación raw_turns_agent↔steps en el paso n={n}: steps dice "
                    f"{s.get('tool')}({json.dumps(s.get('input'), ensure_ascii=False)}) y el crudo "
                    f"dice {b.get('name')}({json.dumps(b.get('input'), ensure_ascii=False)}). "
                    "Esto es corrupción de datos de la traza (dos conteos que deben coincidir): "
                    "revisá la integridad de la traza antes de seguir.")
        if think:
            out[first_n] = think
    if n != len(steps):
        raise RuntimeError(
            f"Desalineación de totales raw_turns_agent↔steps: {n} tool_use en el crudo vs "
            f"{len(steps)} steps en la traza. Corrupción de datos de la traza: revisá su "
            "integridad antes de seguir.")
    return out


def _cut_think(t: str) -> str:
    """Truncado por turno con declaración explícita del corte (regla anti-invención:
    un quote de thinking cortado se cita cortado, no se completa)."""
    if len(t) <= TRUNC_THINK:
        return t
    return t[:TRUNC_THINK] + f"… [THINKING CORTADO POR TRUNCADO: +{len(t) - TRUNC_THINK} chars no mostrados]"


def build_falla_context(label: str, run: str, qid: str) -> dict:
    """Arma el prompt inicial de la falla a partir de la traza post-hoc. Devuelve
    {pregunta, contexto, n_seen, n_claims_fallidos}. La trayectoria + nodos vistos van como
    CONTEXTO (no como tool): el verificador parte de lo que el agente hizo y vio.

    v5: el esquema documentado solo existe para ppf_core (run_3). Para otros runs (p. ej. el
    dev set sobre run_1/run_5) la sección lo declara EXPLÍCITAMENTE ausente — inyectar el
    esquema equivocado es peor que no inyectar ninguno, y callarlo sería degradar en silencio."""
    if run.startswith("run_3"):
        esquema_txt = esquema_grafo_section()
    else:
        esquema_txt = ("(No hay esquema documentado registrado para este grafo — el esquema del "
                       "repo es de otro run y NO se inyecta. Inferí tipos y relaciones desde lo "
                       "que devuelvan las tools; no asumas el esquema de otro grafo.)")
    rep = load_rep(label, run, qid)
    tr = rep.get("trace") or {}
    pregunta = tr.get("question") or ""
    final = tr.get("final_json") or {}
    categoria = rep.get("categoria")

    # Descomposición del juez (step1, completo — v4 CAMBIO 5a).
    step1 = ((rep.get("judge") or {}).get("step1")) or {}
    d = []
    patas_j = step1.get("patas_de_la_pregunta") or []
    d.append("patas de la pregunta:")
    d += [f"  - {p}" for p in patas_j] or ["  (ninguna)"]
    afirms = step1.get("afirmaciones_verificables") or []
    d.append("afirmaciones verificables extraídas de la respuesta:")
    d += [f'  - [{"central" if a.get("central") else "no central"}] "{a.get("enunciado")}"'
          for a in afirms] or ["  (ninguna)"]
    alcance = step1.get("reportes_de_alcance") or []
    if alcance:
        d.append("reportes de alcance declarados por el agente:")
        d += [f"  - {a}" for a in alcance]
    descomposicion = "\n".join(d)

    # Síntoma: las afirmaciones que el juez marcó incorrectas.
    verifs = ((rep.get("judge") or {}).get("step2") or {}).get("verificaciones") or []
    fallidos = [v for v in verifs if v.get("verdict") in ("falso", "no_soportado")]
    if fallidos:
        sintoma = "\n".join(
            f'  - [{v.get("verdict")}{"/central" if v.get("central") else ""}] "{v.get("enunciado")}"'
            for v in fallidos)
    else:
        sintoma = "  (el juez no expuso afirmaciones desagregadas; revisá la respuesta final completa)"

    # Afirmaciones que el juez aprobó (v4 CAMBIO 5b) — sección aparte, para no re-litigar.
    aprobados = [v for v in verifs if v.get("verdict") == "verdadero"]
    if aprobados:
        aprobados_txt = "\n".join(
            f'  - [OK{"/central" if v.get("central") else ""}] "{v.get("enunciado")}"'
            for v in aprobados)
    else:
        aprobados_txt = "  (ninguna)"

    # Trayectoria del agente: qué tools llamó y qué vio (truncado, como en la traza),
    # con el thinking de cada turno intercalado si existe (v4 CAMBIO 5c; trazas OFF no tienen).
    steps = tr.get("steps") or []
    thinks = _thinking_por_turno(rep, steps)
    if steps:
        parts = []
        for s in steps:
            if s.get("n") in thinks:
                parts.append(f'  [thinking del agente, turno que arranca en el paso {s.get("n")}]:'
                             f'\n       {_cut_think(thinks[s["n"]])}')
            parts.append(
                f'  {s.get("n")}. {s.get("tool")}({json.dumps(s.get("input"), ensure_ascii=False)})'
                f'\n       → {(s.get("output_truncado") or "")}')
        if None in thinks:
            parts.append(f'  [thinking del agente, antes de la respuesta final]:'
                         f'\n       {_cut_think(thinks[None])}')
        traj = "\n".join(parts)
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

--- DESCOMPOSICIÓN DEL JUEZ (step1) ---
{descomposicion}

--- SÍNTOMA: afirmaciones que el juez marcó incorrectas ---
{sintoma}

--- AFIRMACIONES QUE EL JUEZ APROBÓ — no re-litigar ---
{aprobados_txt}

--- RESPUESTA FINAL DEL AGENTE ---
respuesta: {final.get('respuesta')}
citas: {citas}
respondible (declarado por el agente): {final.get('respondible')}

--- TRAYECTORIA DEL AGENTE (qué tools llamó y qué devolvieron; thinking por turno si existe) ---
{traj}

--- NODOS QUE EL AGENTE VIO (contenido íntegro, sin truncar) ---
{nodos_txt}

--- ESQUEMA DEL GRAFO ---
{esquema_txt}

Investigá por qué falló y atribuí la causa con evidencia, siguiendo el método. Podés consultar \
CUALQUIER nodo del grafo {run} (no solo los de arriba) y leer el PDF fuente con las tools. \
Cuando tengas evidencia suficiente, devolvé el JSON del contrato."""

    return {"pregunta": pregunta, "categoria": categoria, "contexto": contexto,
            "n_seen": len(seen), "n_claims_fallidos": len(fallidos)}


# --------------------------------------------------------------------------- #
# Validación programática del contrato (v5, decisión 5) + detectores (dec. 6)  #
# --------------------------------------------------------------------------- #
def validar_contrato(fj) -> list[str]:
    """Valida la salida del modelo contra el contrato v5. Devuelve la lista de errores
    (vacía = válido). Campos exactos, pares completos, busquedas donde es obligatorio."""
    if not isinstance(fj, dict):
        return ["la salida no es un objeto JSON"]
    errs: list[str] = []
    requeridos = {"extraccion_traza", "atribuciones", "razonamiento"}
    extras = sorted(set(fj) - requeridos)
    if extras:
        errs.append(f"campos fuera del contrato: {extras} (el contrato v5 no acepta campos extra)")
    for k in sorted(requeridos - set(fj)):
        errs.append(f"falta el campo obligatorio '{k}'")
    ats = fj.get("atribuciones")
    if not isinstance(ats, list) or not ats:
        errs.append("'atribuciones' debe ser una lista NO vacía")
        return errs
    for i, a in enumerate(ats):
        pre = f"atribuciones[{i}]"
        if not isinstance(a, dict):
            errs.append(f"{pre} no es un objeto"); continue
        s, c = a.get("sintoma_capa1"), a.get("causa_capa2")
        if s not in SINTOMAS_CAPA1:
            errs.append(f"{pre}.sintoma_capa1 inválido: {s!r} (debe ser uno de {SINTOMAS_CAPA1}) — "
                        "una causa sin síntoma clasificado no valida")
        if c not in LADO_POR_CAUSA:
            errs.append(f"{pre}.causa_capa2 inválida: {c!r} (taxonomía cerrada: "
                        f"{sorted(LADO_POR_CAUSA)})")
        elif a.get("lado") != LADO_POR_CAUSA[c]:
            errs.append(f"{pre}.lado {a.get('lado')!r} no corresponde a '{c}' "
                        f"(esperado {LADO_POR_CAUSA[c]!r})")
        if a.get("jerarquia") not in ("primaria", "secundaria"):
            errs.append(f"{pre}.jerarquia inválida: {a.get('jerarquia')!r} (primaria|secundaria)")
        ev = a.get("evidencia")
        if not isinstance(ev, dict):
            errs.append(f"{pre}.evidencia falta o no es objeto")
        else:
            for pieza in ("afirmacion", "nodo", "fuente"):
                o = ev.get(pieza)
                if not (isinstance(o, dict) and str(o.get("quote") or "").strip()
                        and str(o.get("ubicacion") or "").strip()):
                    errs.append(f"{pre}.evidencia.{pieza} debe ser {{quote, ubicacion}} no vacíos")
        if c in BUSQUEDAS_OBLIGATORIAS:
            b = a.get("busquedas")
            if not (isinstance(b, list) and b and all(
                    isinstance(x, dict) and str(x.get("consulta") or "").strip()
                    and str(x.get("resultado") or "").strip() for x in b)):
                errs.append(f"{pre}: 'busquedas' (lista no vacía de {{consulta, resultado}}) es "
                            f"OBLIGATORIO para '{c}'")
        if c == "frontera_no_determinada":
            e = a.get("entre")
            if not (isinstance(e, list) and len(e) == 2):
                errs.append(f"{pre}.entre debe nombrar exactamente las DOS causas en disputa")
            if not str(a.get("evidencia_faltante") or "").strip():
                errs.append(f"{pre}.evidencia_faltante es obligatorio para frontera_no_determinada")
    return errs


_NEG_RE = re.compile(r"\b0 nodos|ning[uú]n|no encontr|sin resultado|no devolv|no aparec|no exist",
                     re.IGNORECASE)


def detectores_post(atribuciones: list, tool_calls_used: int, api_calls: list,
                    tokens_in: int, tokens_out: int) -> dict:
    """Detectores programáticos post-proceso (v5, decisión 6). Van al JSON de salida del caso,
    NUNCA al prompt. flag_encuadre_invertido: atribución lado agente cuyas busquedas documentadas
    no hallaron el nodo (todas negativas, o evidencia.nodo vacía/'ninguno') — el patrón del
    encuadre invertido que motivó el árbol."""
    flag_encuadre = False
    for a in atribuciones or []:
        if not isinstance(a, dict) or a.get("lado") != "agente":
            continue
        busq = a.get("busquedas") or []
        if not busq:
            continue
        nodo_q = str(((a.get("evidencia") or {}).get("nodo") or {}).get("quote") or "").strip()
        sin_nodo = nodo_q.lower() in ("", "ninguno", "(ninguno)", "null", "n/a")
        todas_negativas = all(_NEG_RE.search(str(x.get("resultado") or "")) for x in busq
                              if isinstance(x, dict))
        if sin_nodo or todas_negativas:
            flag_encuadre = True
            break
    flag_contexto = (tool_calls_used >= MAX_TOOL_CALLS
                     or any(c.get("stop_reason") == "max_tokens" for c in api_calls or []))
    return {
        "flag_encuadre_invertido": flag_encuadre,
        "flag_contexto": flag_contexto,
        "tool_calls_usadas": tool_calls_used,
        "max_tool_calls": MAX_TOOL_CALLS,
        "tokens_in": tokens_in,
        "tokens_out": tokens_out,
    }


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
        errores_formato: list[str] = []
        format_retries = 0
        force_final = False
        t0 = time.monotonic()
        try:
            while True:
                kwargs = dict(model=MODEL_VERIF, max_tokens=MAX_TOKENS,
                              system=system_prompt(), messages=messages, tools=VERIF_TOOLS)
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

                # respuesta final → VALIDACIÓN PROGRAMÁTICA (v5): un único reintento con el
                # error específico; si vuelve a fallar, formato_invalido (ruidoso, no silencioso).
                final_raw = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
                final_json = _extract_json(final_raw)
                errores_formato = validar_contrato(final_json)
                if errores_formato and format_retries == 0:
                    format_retries = 1
                    messages.append({"role": "assistant", "content": resp.content})
                    messages.append({"role": "user", "content": (
                        "Tu JSON NO valida contra el contrato:\n- "
                        + "\n- ".join(errores_formato)
                        + "\nDevolvé el JSON COMPLETO corregido — un único objeto, sin texto "
                          "adicional ni campos extra.")})
                    force_final = True
                    continue
                break
        except Exception as e:  # loguear cualquier fallo de API/parse sin tumbar la corrida
            error = f"{type(e).__name__}: {e}"

        # Contrato autoritativo: id_falla/run los fija el orquestador, no el modelo.
        fj = final_json if isinstance(final_json, dict) else {}
        atribuciones = fj.get("atribuciones") or []
        return {
            "id_falla": id_falla,
            "run": run,
            "extraccion_traza": fj.get("extraccion_traza"),
            "atribuciones": atribuciones,
            "razonamiento": fj.get("razonamiento"),
            "formato_invalido": bool(errores_formato) or error is not None,
            "errores_formato": errores_formato,
            # detectores programáticos (v5, decisión 6) — post-proceso, nunca en el prompt:
            "detectores": detectores_post(atribuciones, tool_calls_used, api_calls,
                                          tokens_in, tokens_out),
            # auditoría (no es parte del contrato, ayuda a calibrar):
            "_meta": {
                "parse_ok": isinstance(final_json, dict) and "atribuciones" in fj,
                "format_retries": format_retries,
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
def _parse_casos(spec: str | None, archivo: str | None) -> list[tuple[str, str, str]]:
    """Parsea --casos "off/run_5/CQ-017,on/run_1/CQ-019" o --casos-file (un caso por línea,
    mismo formato; '#' comenta). Devuelve [(label, run, qid), ...]. Fallo ruidoso ante formato roto."""
    raw: list[str] = []
    if spec:
        raw += [c.strip() for c in spec.split(",") if c.strip()]
    if archivo:
        for line in Path(archivo).read_text(encoding="utf-8").splitlines():
            line = line.split("#", 1)[0].strip()
            if line:
                raw.append(line)
    casos = []
    for c in raw:
        partes = c.split("/")
        if len(partes) != 3 or partes[0] not in ("off", "on"):
            raise SystemExit(f"Caso mal formado: {c!r} (esperado label/run/CQ, p. ej. off/run_5/CQ-017)")
        casos.append((partes[0], partes[1], partes[2]))
    return casos


def main():
    ap = argparse.ArgumentParser(description="Verificador agéntico de atribución (Paso 3, v5).")
    ap.add_argument("--label", default="off", help="off|on (subcarpeta de posthoc_run/traces)")
    ap.add_argument("--run", default="run_3", help="run_1..run_5 (def. run_3)")
    ap.add_argument("--qid", default="CQ-017", help="id de la pregunta a investigar")
    ap.add_argument("--casos", default=None,
                    help='RUNNER (dev set u otra lista): casos "label/run/CQ" separados por coma.')
    ap.add_argument("--casos-file", default=None,
                    help="RUNNER: archivo con un caso label/run/CQ por línea ('#' comenta).")
    ap.add_argument("--out", default=str(EVAL_DIR / "posthoc_run" / "dev_set" / "salidas_v5"),
                    help="Directorio de salida del runner (un JSON por caso).")
    ap.add_argument("--context", action="store_true",
                    help="OFFLINE: arma e imprime el contexto de la falla + el tool set, SIN llamar a la API.")
    ap.add_argument("--prompt", action="store_true",
                    help="OFFLINE: ensambla e imprime el system prompt v5 (taxonomía por referencia), SIN API.")
    args = ap.parse_args()

    if args.prompt:
        p = system_prompt()
        print(p)
        print(f"\n== {len(p)} caracteres (ensamblado desde {TAXONOMIA_MD}) ==", file=sys.stderr)
        return 0

    if args.context:
        # Modo de revisión del cableado: no requiere API ni gasta.
        ctx = build_falla_context(args.label, args.run, args.qid)
        print(f"== CONTEXTO de la falla {args.run}/{args.qid} (label={args.label}) ==")
        print(f"   nodos vistos recuperados: {ctx['n_seen']} | claims fallidos: {ctx['n_claims_fallidos']}")
        print(f"   tools del verificador: {[t['name'] for t in VERIF_TOOLS]}")
        print("\n" + ctx["contexto"])
        return 0

    # Modo real (requiere API). NO se ejecuta como parte de la construcción; lo dispara la iteración.
    from dotenv import load_dotenv
    import os, anthropic
    load_dotenv(EVAL_DIR / ".env")
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit("ANTHROPIC_API_KEY no seteada en evaluacion/.env")
    real = anthropic.Anthropic(max_retries=3)

    casos = _parse_casos(args.casos, args.casos_file)
    if casos:
        # RUNNER (decisión 8): lista arbitraria de fallas, un JSON por caso, kg cacheado por run.
        outdir = Path(args.out)
        outdir.mkdir(parents=True, exist_ok=True)
        kg_cache: dict = {}
        for label, run, qid in casos:
            print(f"[runner] investigando {label}/{run}/{qid} …", flush=True)
            rec = investigar_falla(real, label, run, qid, _kg_cache=kg_cache)
            rec["_meta"]["label"] = label
            dest = outdir / f"{label}_{run}_{qid}.json"
            dest.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
            det = rec["detectores"]
            print(f"[runner]   → {dest.name} · atribuciones={len(rec['atribuciones'])} · "
                  f"formato_invalido={rec['formato_invalido']} · "
                  f"tools={det['tool_calls_usadas']}/{det['max_tool_calls']} · "
                  f"flags: encuadre={det['flag_encuadre_invertido']} contexto={det['flag_contexto']}",
                  flush=True)
        return 0

    rec = investigar_falla(real, args.label, args.run, args.qid)
    print(json.dumps(rec, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
