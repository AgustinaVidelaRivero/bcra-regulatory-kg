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
CODE_VER = "verificador-v4"   # v4: rediseño según mentores (abstención de primera clase + anclaje textual + procedimiento en fases + esquema/juez/thinking en contexto + ejemplos resueltos). v1/v2/v3 intactos bajo sus namespaces.

# Taxonomía CERRADA (espejo de references/taxonomia.md de la skill).
CATEGORIAS_GRAFO = ["contenido_kg", "completitud_kg", "estructural_kg", "provenance_imprecisa"]
CATEGORIAS_AGENTE = ["navegación", "generación-de-más"]
CATEGORIAS_INDETERMINADO = ["frontera_no_determinada"]   # v4: abstención de primera clase

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
4. DESCOMPONÉ la pregunta en sus PATAS (sub-preguntas; partí de la descomposición del juez que viene \
en el contexto) y tratá cada una por separado: una falla \
puede romperse en una pata y estar bien en otra. Investigá la fuente de CADA pata fallida antes de \
concluir. "No miré la otra pata" NO es "la otra pata está bien": una pata sin verificar es evidencia \
FALTANTE, no evidencia a favor de ninguna conclusión.
5. No cierres por COINCIDENCIA SUPERFICIAL. Que un nodo comparta palabras con la pregunta no \
significa que la responda. Antes de dar por cerrada la investigación, chequeá: (a) ¿leíste con \
leer_pasaje_pdf la fuente de cada pata fallida?; (b) ¿abriste con ver_nodo el CONTENIDO de los nodos \
que vas a citar como evidencia, en vez de quedarte con el label o el resumen de buscar_nodos? Si \
alguna respuesta es "no", seguí investigando o bajá la confianza — no concluyas todavía.

PROCEDIMIENTO (en este orden — cada fase alimenta a la siguiente):
FASE A — EXTRACCIÓN (antes de investigar; se hace SOLO con el contexto que te di, sin tools). \
De la traza, extraé y listá:
  A1. cada tool call del agente con sus argumentos;
  A2. qué devolvió cada una, y si el resultado era PERTINENTE a la pregunta o no;
  A3. si existe, en qué paso el agente tomó la decisión que llevó al error (con cita textual de ese \
paso); si el agente actuó correctamente sobre la información que tenía (p. ej. citó fiel un nodo \
defectuoso), declaralo explícitamente: "no hay paso de decisión erróneo del agente" — esa \
constatación es evidencia de lado GRAFO, no un campo vacío;
  A4. si hay thinking disponible en la trayectoria: el fragmento donde razona esa decisión (si en A3 \
no hay decisión errónea, esto también queda en null por esa razón, no solo por ausencia de thinking);
  A5. las patas de la pregunta según la descomposición del juez (step1, viene en el contexto).
El resultado de esta fase va TAL CUAL en el campo "extraccion_traza" del JSON final.
FASE B — INVESTIGACIÓN: por cada pata fallida, el cruce de las tres fuentes (afirmación / nodo / \
PDF) usando las tools, siguiendo el método de arriba. Usá el ESQUEMA DEL GRAFO (viene en el \
contexto) para razonar qué nodo/arista DEBERÍA existir para responder la pregunta, y chequeá si \
existe: si la pregunta necesita conectar una entidad de tipo X con una de tipo Y y el esquema tiene \
la relación Z para eso, buscá si esa arista está.
FASE C — ATRIBUCIÓN: recién acá etiquetás (o te abstenés con frontera_no_determinada), con los \
anclajes del bloque ANCLAJE TEXTUAL.

TENÉS ESTAS TOOLS (para la FASE B; cuáles usar y cuántas veces es tu criterio):
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
- Abstención (lado="indeterminado"):
  · frontera_no_determinada — tras investigar a fondo, la evidencia no alcanza para decidir entre \
DOS categorías (típicamente navegación vs completitud_kg).

DISCRIMINAR navegación (agente) de defecto de GRAFO — es el error más fácil de cometer:
Antes de atribuir `navegación`, CONFIRMÁ que existe en el grafo un nodo que efectivamente RESPONDE \
la pregunta (su contenido contesta lo que se pregunta), no apenas un nodo que la MENCIONA o comparte \
palabras. Buscá ese nodo vos y abrilo con ver_nodo para leer su contenido:
  · Encontrás un nodo fiel y pertinente que responde, y el agente igual no lo usó → `navegación`.
  · El nodo "parecido" menciona el tema pero dice otra cosa, o contradice el PDF → `contenido_kg` (grafo).
  · NINGÚN nodo del grafo responde la pregunta (aunque el PDF sí tenga el dato) → `completitud_kg` \
(grafo) SI tu búsqueda fue exhaustiva; si no podés garantizarlo, ver la bifurcación de abajo.
No confundas "el dato no está / está mal en el grafo" (defecto de GRAFO) con "el agente no lo \
encontró" (navegación): son lados opuestos, y la diferencia se decide buscando VOS el nodo que \
respondería. Esa búsqueda tuya tiene TRES salidas, no dos:
  · Encontraste el nodo que responde → `navegación`, exhibiéndolo (quote de su CONTENIDO, no del label).
  · NO lo encontraste Y tu búsqueda fue exhaustiva (cubriste los términos plausibles, documentados) → \
`completitud_kg`, con la constancia de búsqueda como evidencia.
  · NO lo encontraste pero NO podés garantizar exhaustividad (espacio de sinónimos grande, resultados \
ambiguos, te acercás al límite de tool calls) → `frontera_no_determinada`.
La abstención es el tercer camino de ESTA decisión, no una categoría aparte que compite con ella.
sin_defecto (falso positivo del juez) es la atribución de ÚLTIMO RECURSO. Solo se usa tras descartar \
ACTIVAMENTE cada defecto: contenido (¿un nodo contradice el PDF?), completitud (¿falta info que el PDF \
tiene?), estructura (¿falta nodo/arista que conecte las patas?), provenance (¿las citas apuntan a \
donde está el dato?), navegación (¿había un nodo que respondía y no se usó?). Solo si ninguno aplica \
tras buscarlos uno por uno. La carga de la prueba es ALTA: tenés que decir qué descartaste y cómo. \
Ante la duda entre un defecto sutil y un falso positivo del juez, seguí investigando el defecto — no \
es sin_defecto.

ABSTENCIÓN (frontera_no_determinada): una etiqueta equivocada es PEOR que una abstención honesta; \
adivinar no es atribuir. Si tras investigar a fondo la evidencia no alcanza para decidir entre dos \
categorías (típicamente navegación vs completitud_kg), abstenete con frontera_no_determinada. NO es \
una salida fácil — exige TRES cosas:
(a) documentar qué buscaste y qué encontraste (campo "busquedas": términos usados, qué devolvió cada una);
(b) nombrar las DOS categorías entre las que no podés decidir (campo "entre");
(c) declarar explícitamente qué evidencia faltante decidiría el caso (campo "evidencia_faltante") — \
p. ej.: "si existiera un nodo X que dijera Y, sería navegación; no lo encontré tras N búsquedas con \
términos [...], pero no puedo garantizar que no exista".

ATRIBUCIÓN MÚLTIPLE: una falla puede tener UNA O MÁS causas. Por cada una marcá su jerarquía:
- "primaria": mueve el veredicto (es lo que hace fallar la respuesta).
- "secundaria": está presente pero no es lo que rompe la respuesta (p. ej. un defecto de estilo).
Puede haber MÁS DE UNA primaria: si la pregunta tiene patas independientes y un defecto distinto \
rompe cada pata, cada uno es primario. Usá el campo "pata" para indicar qué parte de la pregunta \
cubre cada atribución cuando aplique.

ANCLAJE TEXTUAL (obligatorio): la etiqueta tiene que estar anclada: si no podés citar textualmente \
el lugar exacto donde se rompe el circuito, no tenés evidencia suficiente para esa etiqueta. Cada \
pieza de evidencia es un objeto {quote, ubicacion}:
- "quote": cita VERBATIM (copiada tal cual de la tool o de la traza, NO parafraseada).
- "ubicacion": dónde vive el quote — id de nodo, source_doc+location del PDF, o "paso N de la \
trayectoria" / "respuesta final" del agente.
Si el quote que necesitás de la trayectoria quedó cortado por el truncado (…), NO completes de \
memoria: re-abrí la fuente con las tools (ver_nodo / leer_pasaje_pdf) y citá desde ahí. \
EXCEPCIÓN — el thinking del agente NO se puede re-abrir con ninguna tool: si el fragmento que \
necesitás quedó cortado por el truncado, citá lo que hay y declaralo cortado — no lo completes.
Reglas por categoría:
- Para `navegación`, el quote obligatorio es del CONTENIDO del nodo que respondía (lo que devuelve \
ver_nodo), NO su label.
- Para `completitud_kg`, el quote es del PDF (el dato que falta), acompañado de la constancia de \
búsqueda en el campo "busquedas" (qué términos usaste, qué devolvió cada búsqueda).
- El campo "busquedas" es OBLIGATORIO para `completitud_kg` y `frontera_no_determinada`; para el \
resto, incluilo si una búsqueda tuya fue parte de la evidencia.

EJEMPLOS RESUELTOS (de otros grafos del mismo corpus):
ADVERTENCIAS: (a) Estos ejemplos son de OTROS grafos (run_1, run_5): sus nodos y sus valores NO \
existen necesariamente en el grafo que estás investigando. Enseñan el MÉTODO, no hechos del dominio. \
(b) No asumas que tu caso se parece a alguno de estos: la atribución sale de TU evidencia, no de la \
analogía superficial con un ejemplo.

EJEMPLO 1 — contenido_kg (lado grafo), run_5:
Síntoma: ante "¿Cuál es la exigencia básica de capital mínimo para un banco?" el agente respondió \
"1.500 millones de pesos" y el juez marcó falso ese claim central.
Evidencia:
  afirmacion: {"quote": "La exigencia básica de capital mínimo para un banco es de 1.500 millones \
de pesos.", "ubicacion": "respuesta final"}
  nodo: {"quote": "Integración de capital mínimo según categoría: 1.500 millones de pesos para \
Bancos, 700 millones para Restantes entidades (…) en período 01/06/24 a 31/12/24", "ubicacion": \
"exigencia_basica_de_capital"}
  fuente: {"quote": "1.2. Exigencia básica. Según la clase de entidad, serán las siguientes \
exigencias básicas: Bancos (…) -En millones de pesos- 5.000 2.500", "ubicacion": \
"TO_capitales_minimos_actual.pdf, Punto 1.2"}
Atribución: contenido_kg, primaria. El agente fue fiel al nodo; el nodo tiene un valor \
desactualizado (tabla de un período vencido) que contradice el PDF vigente. El circuito se rompe \
en el nodo, no en el agente.

EJEMPLO 2 — generación-de-más (lado agente), run_1:
Síntoma: ante "¿hasta cuántos días de atraso (…) 'situación normal'?" la respuesta central fue \
correcta (31 días), pero el juez marcó no_soportado la glosa "Esta normativa es del BCRA".
Evidencia:
  afirmacion: {"quote": "Esta normativa es del BCRA (Banco Central de la República Argentina).", \
"ubicacion": "respuesta final"}
  nodo: {"quote": "Plazo máximo tolerable de retraso en el pago de obligaciones que permite \
mantener la clasificación de situación normal si el cliente cancela sin nueva financiación.", \
"ubicacion": "req_atrasos_de_hasta_31_dias_compatibles_con_clasificacion_de_situacion_normal \
(abierto por el agente en el paso 3)"}
  fuente: {"quote": "Comprende los clientes que atienden en forma puntual el pago de sus \
obligaciones o con atrasos que no superan los 31 días.", "ubicacion": \
"TO_clasificacion_deudores_actual.pdf, Punto 7.2.1"}
Atribución: generación-de-más, secundaria. El claim es fácticamente CIERTO, pero ningún nodo \
visto lo soporta — "el contenido es correcto" no cierra la investigación: la pregunta sigue \
siendo por qué el juez lo marcó. El grafo tenía el dato y el agente lo usó bien en la pata \
central; el defecto es la glosa agregada sin soporte.

EJEMPLO 3 — la bifurcación resuelta por búsqueda documentada, run_1:
Síntoma: la pregunta pedía el valor de la exigencia básica para un banco; el claim investigado \
(secundario, no_soportado) fue la fórmula general — fiel al nodo req_capital_minimo, que no \
contiene el valor. ¿Es completitud_kg ("el valor no está en el grafo")?
busquedas: [
  {"consulta": "5.000 millones", "resultado": "0 nodos pertinentes"},
  {"consulta": "millones de pesos", "resultado": "cla_bancos (1.500 millones, período \
01/06/24-31/12/24) y rsj_restantes_entidades_financieras (2.500 millones)"}
]
Evidencia:
  afirmacion: {"quote": "La exigencia de capital mínimo total debe ser el mayor valor entre la \
exigencia básica y la suma de los riesgos de crédito, mercado y operacional.", "ubicacion": \
"respuesta final"}
  nodo: {"quote": "Categoría de entidades financieras que debe mantener capital mínimo de 1.500 \
millones de pesos en el período 01/06/24 al 31/12/24.", "ubicacion": "cla_bancos (encontrado por \
la búsqueda del verificador, no usado por el agente)"}
  fuente: {"quote": "1.2. Exigencia básica. Según la clase de entidad, serán las siguientes \
exigencias básicas: Bancos (…) -En millones de pesos- 5.000 2.500", "ubicacion": \
"TO_capitales_minimos_actual.pdf, Punto 1.2"}
Atribución: contenido_kg, primaria. El nodo con el valor EXISTE pero está desactualizado: el dato \
no "falta", está mal. completitud_kg habría exigido que la búsqueda documentada NO encontrara \
ningún nodo portador del valor. La constancia de búsqueda es lo único que distingue "falta" de \
"está mal" de "no lo encontré yo". Nota: un verificador anterior etiquetó este claim como \
completitud con confianza ALTA teniendo cla_bancos en su propia evidencia del claim central de \
la misma pregunta — la confianza declarada no sustituye la búsqueda.

SALIDA: cuando tengas evidencia suficiente, respondé con UN ÚNICO objeto JSON válido, sin texto \
adicional ni markdown, con exactamente esta forma:
{
  "extraccion_traza": {
    "tool_calls": [
      {"paso": 1, "tool": "<tool>", "args": "<argumentos>",
       "devolvio": "<qué devolvió, resumido>", "pertinente": true}
    ],
    "paso_decision_error": {"paso": 0, "quote": "<cita textual del paso donde se tomó la decisión que llevó al error>"} | null,
    "decision_agente_correcta": "<SOLO si paso_decision_error es null: por qué el agente actuó bien sobre lo que tenía>",
    "thinking_decision": "<fragmento del thinking donde razona esa decisión; null si no hay thinking O si no hay decisión errónea (A3)>",
    "patas": ["<las patas de la pregunta según el step1 del juez>"]
  },
  "atribuciones": [
    {
      "categoria": "<una de la taxonomía cerrada>",
      "lado": "grafo|agente|ninguno|indeterminado",
      "jerarquia": "primaria|secundaria",
      "pata": "<opcional: qué parte de la pregunta cubre>",
      "entre": ["<SOLO para frontera_no_determinada: las DOS categorías entre las que no podés decidir>"],
      "evidencia_faltante": "<SOLO para frontera_no_determinada: qué evidencia decidiría el caso>",
      "evidencia": {
        "afirmacion": {"quote": "<VERBATIM: qué afirmó el agente>",
                       "ubicacion": "<'respuesta final' o 'paso N de la trayectoria'>"},
        "nodo": {"quote": "<VERBATIM: contenido del/los nodo(s), o 'ninguno'>",
                 "ubicacion": "<id(s) de nodo>"},
        "fuente": {"quote": "<VERBATIM: qué dice el PDF>",
                   "ubicacion": "<source_doc + location>"}
      },
      "busquedas": [
        {"consulta": "<términos usados>", "resultado": "<qué devolvió, resumido>"}
      ]
    }
  ],
  "razonamiento": "<cadena evidencia→conclusión que justifica las atribuciones>",
  "confianza": "alta|media|baja"
}

CONFIANZA: "alta" SOLO si verificaste todas las patas contra la fuente y abriste el contenido de los \
nodos pertinentes. Si quedó una pata sin verificar, o si concluís `sin_defecto` o `navegación` sin \
haber buscado activamente el nodo que respondería, la confianza es a lo sumo "media". \
sin_defecto con confianza "alta" requiere documentar qué defectos descartaste activamente; sin ese \
descarte explícito, es a lo sumo "baja". \
Para `frontera_no_determinada` la confianza NO califica la atribución (no tiene sentido "alta \
confianza en que no sé"): califica la CALIDAD DE LA BÚSQUEDA documentada — "alta" = búsqueda amplia \
y documentada con términos y resultados (campo "busquedas" completo); "baja" = investigación cortada \
(límite de tool calls, resultados sin abrir).

NO incluyas palanca de cambio ni nivel de riesgo: eso es del Paso 4, no tuyo."""


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
    CONTEXTO (no como tool): el verificador parte de lo que el agente hizo y vio."""
    if not run.startswith("run_3"):
        raise RuntimeError(f"El esquema inyectado en el contexto es el de ppf_core (run_3); no hay "
                           f"esquema registrado para '{run}'. Abortando: inyectar el esquema equivocado "
                           "es peor que no inyectar ninguno.")
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
{esquema_grafo_section()}

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
            "extraccion_traza": (final_json or {}).get("extraccion_traza") if isinstance(final_json, dict) else None,
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
