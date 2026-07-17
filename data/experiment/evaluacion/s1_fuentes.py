"""s1_fuentes.py — S1: segunda pasada con fuentes forzadas (v7 = v6.1-D + S1).

Implementa el diseño pre-registrado de docs/diseno_v7_s1.md (§2). DOS componentes
estrictamente separados:

1. FETCH DETERMINÍSTICO (puro, sin API) — construir_paquete_fuentes:
   - Gatillo (diseño §2): atribuciones de reps válidas con causa final en
     {contenido_kg, aplicacion_erronea, estructural_kg, completitud_kg}; y, si el voto del
     caso (voto_capa_d) es de clave vacía CON síntoma no vacío (F/P de _sintoma_de_trace,
     el MISMO filtro que build_falla_context), las atribuciones sin_defecto del caso
     (tipo_gatillo "exoneracion_con_sintoma").
   - Por atribución gatillada: portador vía el extractor PROPIO de S1
     (_extraer_portador_s1 — CORRECCIÓN B4.2, por mecanismo, sin tocar
     capa_deterministica): matchea ids del kg por substring en
     evidencia.nodo.ubicacion (fallback: quote) y, ante múltiples matches, aplica la
     REGLA DEL MAXIMAL ÚNICO — si existe UN id que contiene a todos los demás matcheados
     como substrings, ese es el portador; si no (matches genuinamente distintos) →
     sin_portador_extraible, como la regla pre-registrada de D2. Motivo medido: la
     anidación de ids es propiedad del VOCABULARIO de los grafos (ej. run_4: "comision" ⊂
     "comision_por_precancelacion"); la regla resuelve anidación, NO ambigüedad real.
   - Provenance del portador desde el kg del run — EN CASCADA (CORRECCIÓN B4.2, por
     mecanismo: provenances de preámbulo/carátula que parsean pero no localizan): se
     recorren las provenances parseables por pdf_locate.parse_point EN ORDEN y se usa la
     PRIMERA que LOCALIZA; el paquete registra cada intento (provenances_intentadas: idx,
     location, ref, resultado). Solo si NINGUNA parseable localiza → localizacion_fallida
     (si ninguna parsea → provenance_no_parseable). pdf_locate.localize recupera (a) el
     pasaje del portador CON su
     encabezado y (b) los comparativos:
       * "seccion_madre": el encabezado de la sección madre = PRIMER nivel del punto del
         portador (existe si el punto tiene ≥2 niveles). CORRECCIÓN B3b (por mecanismo,
         hecho b del dry-run de B3): SIEMPRE se emite con estado "omitido" y nota fija —
         los encabezados de primer nivel son carátula sin prosa y localize los falla
         sistemáticamente (sondeo en los 4 TOs) — sin llamar a localize;
       * "punto_general_un_nivel_arriba": mismo prefijo, un nivel arriba (padre inmediato
         del punto del portador; existe como comparativo DISTINTO solo si el punto tiene
         ≥3 niveles — con 2 niveles el padre inmediato COINCIDE con la sección madre y se
         anota como nota mecánica, sin duplicar);
       * "referencia_interna" (CORRECCIÓN B3b, por mecanismo — hecho a del dry-run de B3:
         la conexión relevante vive en el TEXTO del pasaje, no en la jerarquía de
         numeración): menciones a otros puntos/secciones extraídas del texto del pasaje
         del PORTADOR con la regex cerrada RE_REFERENCIAS_INTERNAS (variantes
         "punto X.Y[.Z]", "puntos X.Y y X.Z", "Sección N."), en orden de aparición,
         deduplicadas por (punto, documento de destino), tope
         TOPE_REFERENCIAS_INTERNAS = 3; cada una con su mención de origen verbatim.
         CORRECCIÓN B3c (por mecanismo — hecho de B3b: la regex resolvía intra-documento
         menciones dirigidas a OTRO TO, inyectando texto equivocado): tras cada mención
         se inspecciona una ventana fija de VENTANA_MARCADOR_EXTERNO = 100 chars
         siguientes con la regex cerrada RE_MARCADOR_DOC_EXTERNO ("del TO/Texto Ordenado
         (de las normas) sobre <nombre>" / "de las normas sobre <nombre>"). Sin marcador
         → intra-documento (comportamiento previo). Con marcador: el <nombre> se matchea
         contra el mapa cerrado DOCS_CORPUS (los 5 TOs del experimento, por palabras
         clave normativas); si matchea, la referencia se localiza EN ESE documento
         (regla="referencia_interna_cross_doc", doc_destino anotado); si NO matchea (TO
         fuera del corpus), el comparativo se emite "omitido_fuera_de_corpus" con la
         mención y el marcador verbatim — NUNCA se resuelve intra-documento una mención
         marcada como externa.
     Cada comparativo lleva su regla aplicada (mecánica, sin juicio) y su ESTADO PROPIO
     ("localizado" / "fallido" / "omitido") — que NO fuerza triage (política de estados
     NO BLOQUEANTE, corrección B3b).
   - Estados explícitos del paquete por atribución (el triage fuente_no_verificable de S1
     queda RESERVADO a fallas del PORTADOR):
     "sin_portador_extraible" (cero o >1 ids del kg en la evidencia),
     "provenance_no_parseable" (ninguna provenance del portador parsea a punto/sección),
     "localizacion_fallida" (localize del pasaje del PORTADOR devolvió fallida),
     "completo" (el pasaje del PORTADOR localizó — comparativos fallidos u omitidos NO
     bloquean).

2. JUICIO S1 (la única parte con LLM) — aplicar_s1:
   - Por atribución gatillada con paquete "completo": UNA llamada por repetición (n) al
     modelo del verificador (MODEL_VERIF, importado del instrumento congelado) con
     S1_PROMPT, que presenta la atribución emitida, el contenido del nodo portador y los
     pasajes fuente, y EXIGE el esquema del diseño §2 en JSON estricto:
     alcance_declarado_en_fuente / alcance_en_el_nodo / coinciden ∈ {si, no,
     no_determinable} / causa_confirmada_o_corregida / justificacion_breve.
   - S1 NUNCA borra la emisión de v6.1-D: anota capa_s1 al lado (emision_v61d, salidas S1
     íntegras, corrigio: bool) — el mismo patrón de anotación que capa_d —, recomputa el
     voto como voto_s1 con la regla del protocolo (mayoría estricta ≥2) sobre las causas
     post-S1, preservando intactos voto, voto_capa_d y voto_pre_d6 (si existe).
   - Todo estado de fetch fallido y todo resultado no_determinable (o sin mayoría propia
     de S1 con n>1) → triage_s1 con motivo "fuente_no_verificable".
   - --n habilita repetición + voto propio de S1 por atribución (mayoría estricta
     ≥ n//2+1 sobre la causa de las salidas decididas); la POLÍTICA de N se decide en la
     calibración del dev (B4) — acá queda implementada, no decidida.
   - INSTRUMENTACIÓN (CORRECCIÓN B4.2): el usage REAL de la API (input/output tokens por
     llamada) se persiste en capa_s1 (usage_s1, paralelo a salidas_s1) y agregado en
     resumen_s1 (tokens_in_s1 / tokens_out_s1).
   - ITERACIÓN B4.3 (s1-v0.2-dev — legítima por diseño §4, SOLO contra el dev): (a) el
     input de cada llamada incluye el SÍNTOMA del caso (claims reprobados con veredicto y
     centralidad + patas no cubiertas, de _sintoma_de_trace); (b) el esquema del gatillo
     por causas suma sintoma_del_par (derivado de las marcas del juez, no de la emisión)
     y el voto/las correcciones pasan a ser por PAR (síntoma, causa); (c) el gatillo de
     exoneración usa la RAMA DE COMPLETITUD (S1_PROMPT_EXONERACION: pata + respuesta del
     agente + portador + pasajes — el GT del eval set está PROHIBIDO como input; esquema
     respuesta_en_fuente / presente_en_grafo / causa_confirmada_o_corregida).
   - ITERACIÓN B4.3 r2 (s1-v0.3-dev) — REGLA MECÁNICA DE JERARQUÍA PARA EXONERACIONES
     CORREGIDAS (justificación estructural: la severidad de la atribución queda acotada
     por la severidad del síntoma declarado — el espejo de R6b, que degrada primarias
     ligadas solo a secundarios; acá, promueve una corrección ligada a una pata no
     cubierta): cuando S1 corrige una atribución del gatillo de exoneración
     (sin_defecto → causa de defecto),
       * si el síntoma del caso tiene patas no cubiertas → jerarquia="primaria" y
         pata=<la pata no cubierta> (una sola pata → esa; varias sin mapeo posible → el
         CONJUNTO con nota "mecanica_sin_mapeo" — el mapeo no se inventa);
       * si NO hay patas (corrección sobre síntoma de claims) → jerarquía acotada por la
         centralidad del claim mapeado (la lógica de R6b, con _mapear_claim de
         capa_deterministica): mapea a un central reprobado → primaria; solo secundarios
         o sin mapeo → secundaria.
     jerarquia_original queda anotada en capa_s1; el voto_s1 se recomputa contando estas
     primarias. Las correcciones del gatillo de CAUSAS no cambian de jerarquía por esta
     regla.

Módulo que NO modifica congelados (verificador.py, harness.py, capa_deterministica.py,
test_alcanzabilidad.py, taxonomia.md, las varas): solo los importa. S1 no re-investiga
trayectorias: juzga la atribución emitida contra la fuente (diseño §2, "lo que no cambia").
"""

import argparse
import copy
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from capa_deterministica import (          # reutilización pre-registrada — solo import
    _mapear_claim,
    _norm_texto,
    _recomputar_voto,
    _sintoma_de_trace,
)
from test_alcanzabilidad import _index_de  # resolución run|GraphIndex (mismo patrón D1-D6)
from pdf_locate import parse_point, localize
from verificador import MODEL_VERIF        # el modelo del verificador (import read-only)
from verifier_pilot import _extract_json   # parser JSON ya probado del pipeline

S1_VERSION = "s1-v0.3.1-dev"
# B4.5: tope preventivo = 2× el máximo de output observado en el dev (1.184 tok en
# v0.2 + N=3; el tope viejo era 2048). Un JSON cortado sigue siendo formato_invalido.
S1_MAX_TOKENS = 2368

# B4.5 — vocabulario CERRADO de causas de capa 2, copiado verbatim de taxonomia.md
# (defectos del grafo: líneas 44-48; defectos del agente: líneas 55-58; sin defecto y
# abstención: líneas 62-65). "navegación" se acepta también sin acento (robustez de
# grafía, el mismo criterio de capa_deterministica.FRONTERA_NAV).
CAUSAS_VALIDAS = frozenset({
    "contenido_kg", "completitud_kg", "estructural_kg", "provenance_imprecisa",
    "alcanzabilidad_kg", "navegación", "navegacion", "alucinacion_agente",
    "aplicacion_erronea", "sin_defecto", "frontera_no_determinada"})

CAUSAS_GATILLO_S1 = frozenset(
    {"contenido_kg", "aplicacion_erronea", "estructural_kg", "completitud_kg"})

COINCIDEN_VALORES = ("si", "no", "no_determinable")
SINTOMAS_VALORES = ("context_recall", "noise_sensitivity", "faithfulness")
CAMPOS_S1 = ("alcance_declarado_en_fuente", "alcance_en_el_nodo", "coinciden",
             "sintoma_del_par", "causa_confirmada_o_corregida", "justificacion_breve")
CAMPOS_S1_EXON = ("respuesta_en_fuente", "presente_en_grafo",
                  "causa_confirmada_o_corregida")

S1_PROMPT = """Sos S1, la segunda pasada con fuentes forzadas de un instrumento de atribución de fallas \
sobre un sistema KG-RAG regulatorio (BCRA). NO re-investigás la falla: tu única tarea es juzgar UNA \
atribución ya emitida contra el texto fuente que se te entrega abajo, comparando ALCANCES.

Una atribución dice que un nodo del grafo (el "portador") tiene un defecto de cierta causa. El error \
típico que S1 existe para atajar: tratar como general un contenido que la fuente declara SCOPEADO \
(limitado a una cartera, un grupo, un régimen o un período), o al revés. Por eso el juicio es una \
comparación de alcances, y estás OBLIGADO a transcribirlos antes de decidir.

=== SÍNTOMA DEL CASO (las marcas del juez sobre la respuesta — el input real del instrumento) ===
{sintoma}

=== ATRIBUCIÓN EMITIDA (v6.1-D) ===
{atribucion}

=== NODO PORTADOR ({portador_id}) ===
{nodo}

=== PASAJES FUENTE (verbatim del PDF, recuperados por código desde la provenance del portador) ===
{pasajes}

Respondé ÚNICAMENTE un JSON estricto (sin texto antes ni después) con EXACTAMENTE estas claves:
{{
 "alcance_declarado_en_fuente": "<quote VERBATIM del encabezado/pasaje fuente que declara el alcance \
(copiado carácter a carácter, NO parafraseado)>",
 "alcance_en_el_nodo": "<quote VERBATIM del contenido del nodo que muestra con qué alcance lo trata>",
 "coinciden": "si | no | no_determinable",
 "sintoma_del_par": "context_recall | noise_sensitivity | faithfulness",
 "causa_confirmada_o_corregida": "<la causa emitida si el juicio la confirma, o la causa corregida de la \
taxonomía v2.6.1 (contenido_kg, completitud_kg, estructural_kg, alcanzabilidad_kg, navegación, \
alucinacion_agente, aplicacion_erronea, sin_defecto) si no>",
 "justificacion_breve": "<1 a 3 frases: qué dice el alcance de la fuente, qué hace el nodo/la atribución \
con él, y por qué la causa queda confirmada o corregida>"
}}

Reglas duras:
- Los dos campos de alcance son OBLIGATORIOS y VERBATIM: si no podés transcribir un alcance desde el \
material entregado, no inventes — poné coinciden="no_determinable" y explicá qué falta.
- "coinciden" se refiere a si el alcance con que el nodo/la atribución tratan el contenido COINCIDE con \
el alcance declarado en la fuente.
- "sintoma_del_par" se DERIVA de las marcas del juez presentadas arriba, NO de la emisión original: \
pata no cubierta → context_recall; claim reprobado "falso" → noise_sensitivity; claim reprobado \
"no_soportado" → faithfulness. Elegí el síntoma de la marca que la atribución está explicando.
- Juzgá SOLO con el material entregado (síntoma + atribución + nodo + pasajes). Nada de conocimiento externo.
"""

S1_PROMPT_EXONERACION = """Sos S1, la segunda pasada con fuentes forzadas de un instrumento de atribución \
de fallas sobre un sistema KG-RAG regulatorio (BCRA). Este caso fue EXONERADO (el instrumento no atribuyó \
defecto) pero el juez marcó síntoma: hay al menos una PATA de la pregunta que la respuesta no cubrió. Tu \
única tarea: decidir si los pasajes fuente contienen la información que responde esa pata y si esa \
información está o no en el contenido del grafo presentado. NO re-investigás; juzgás con lo entregado.

=== PATA(S) NO CUBIERTA(S) (marca del juez) ===
{patas}

=== RESPUESTA DEL AGENTE (la que el juez marcó) ===
{respuesta}

=== ATRIBUCIÓN DE EXONERACIÓN EMITIDA (v6.1-D) ===
{atribucion}

=== CONTENIDO DEL GRAFO PRESENTADO — NODO PORTADOR CITADO ({portador_id}) ===
{nodo}

=== PASAJES FUENTE (verbatim del PDF, recuperados por código desde la provenance del portador) ===
{pasajes}

Respondé ÚNICAMENTE un JSON estricto (sin texto antes ni después) con EXACTAMENTE estas claves:
{{
 "respuesta_en_fuente": "<quote VERBATIM del pasaje fuente que responde la pata no cubierta, o null si \
los pasajes entregados NO la responden>",
 "presente_en_grafo": "si | no | no_determinable",
 "causa_confirmada_o_corregida": "<sin_defecto si la exoneración se sostiene; o la causa corregida de la \
taxonomía v2.6.1 (típicamente completitud_kg si la fuente responde la pata y el grafo no la contiene)>"
}}

Reglas duras:
- "respuesta_en_fuente" es VERBATIM o null — no parafrasees, no inventes.
- "presente_en_grafo" responde: ¿la información que responde la pata está en el CONTENIDO DEL GRAFO \
presentado (el nodo portador)? — si los pasajes no responden la pata, poné "no_determinable".
- Juzgá SOLO con el material entregado. Nada de conocimiento externo.
"""


# --------------------------------------------------------------------------- #
# 1. FETCH DETERMINÍSTICO (puro, sin API)                                      #
# --------------------------------------------------------------------------- #
# Regex CERRADA de referencias internas (corrección B3b — hecho a del dry-run de B3):
# variantes "punto X.Y[.Z]" (con o sin punto final), "puntos X.Y y X.Z" (enumeraciones con
# "y"/"e"/","), y "Sección N." (primer nivel con punto). Nada más.
RE_REFERENCIAS_INTERNAS = {
    "punto": re.compile(
        r"(?i)\bpuntos?\s+\d+(?:\.\d+)+\s*\.?(?:\s*(?:,|y|e)\s+\d+(?:\.\d+)+\s*\.?)*"),
    "seccion": re.compile(r"(?i)\bsecci[oó]n\s+(\d+)\."),
}
_RE_NUM_PUNTO = re.compile(r"\d+(?:\.\d+)+")   # extractor de números dentro de la mención
TOPE_REFERENCIAS_INTERNAS = 3

# Marcador de documento externo (corrección B3c): regex CERRADA buscada en una ventana
# fija de VENTANA_MARCADOR_EXTERNO chars a continuación de cada mención capturada.
# Variantes: "del TO sobre <nombre>", "del Texto Ordenado (de las normas) sobre <nombre>",
# "de las normas sobre <nombre>" (con comilla opcional antes del nombre). Nada más.
VENTANA_MARCADOR_EXTERNO = 100
RE_MARCADOR_DOC_EXTERNO = re.compile(
    r"(?i)\b(?:del\s+(?:TO|Texto\s+Ordenado)\s+(?:de\s+las\s+normas\s+)?sobre"
    r"|de\s+las\s+normas\s+sobre)\s+['\"“”]?([A-Za-zÁÉÍÓÚáéíóúñÑüÜ\s\-]+)")

# Mapa CERRADO de los 5 TOs del experimento: palabra clave normativa (normalizada:
# lowercase, sin acentos) → archivo del subset. Un marcador cuyo nombre no matchea ninguna
# clave es un TO FUERA del corpus.
DOCS_CORPUS = {
    "clasificacion de deudores": "TO_clasificacion_deudores_actual.pdf",
    "capitales minimos": "TO_capitales_minimos_actual.pdf",
    "exterior y cambios": "TO_exterior_cambios_actual.pdf",
    "proteccion de los usuarios": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
    "regimen informativo": "TO_regimen_informativo_contable_mensual_actual.pdf",
}

NOTA_MADRE_OMITIDA = ("seccion_madre omitida: encabezado de primer nivel = carátula sin "
                      "prosa — sondeo en los 4 TOs, reporte_b3_s1.md hecho b")
NOTA_FUERA_DE_CORPUS = ("mención dirigida a un TO fuera del corpus del experimento — no "
                        "se resuelve intra-documento (corrección B3c)")


def _doc_de_marcador(ventana):
    """Busca el marcador de documento externo en la ventana posterior a la mención.
    Devuelve (doc_destino, marcador_verbatim): (None, None) sin marcador;
    (<archivo del corpus>, marcador) si el nombre matchea DOCS_CORPUS;
    ("fuera_de_corpus", marcador) si no matchea (TO externo al corpus)."""
    m = RE_MARCADOR_DOC_EXTERNO.search(ventana or "")
    if not m:
        return None, None
    nombre = _norm_texto(re.sub(r"-\s+", "", m.group(1)))  # des-hifenado de corte de línea
    for clave, doc in DOCS_CORPUS.items():
        if clave in nombre:
            return doc, m.group(0).strip()
    return "fuera_de_corpus", m.group(0).strip()


def _referencias_de_pasaje(texto, tope=TOPE_REFERENCIAS_INTERNAS):
    """Menciones a otros puntos/secciones en el texto del pasaje del portador, por la
    regex cerrada RE_REFERENCIAS_INTERNAS: en orden de aparición, deduplicadas por
    (punto, doc_destino), con tope. Cada una con su mención de origen verbatim y — B3c —
    la detección del marcador de documento externo en la ventana fija posterior
    (doc_destino: None = intra; archivo del corpus = cross-doc; "fuera_de_corpus").
    Puro, determinístico."""
    texto = texto or ""
    menciones = []
    for m in RE_REFERENCIAS_INTERNAS["punto"].finditer(texto):
        for num in _RE_NUM_PUNTO.findall(m.group(0)):
            menciones.append((m.start(), num, m.group(0), m.end()))
    for m in RE_REFERENCIAS_INTERNAS["seccion"].finditer(texto):
        menciones.append((m.start(), m.group(1), m.group(0), m.end()))
    menciones.sort(key=lambda t: t[0])
    out, vistos = [], set()
    for _, punto, mencion, fin in menciones:
        doc_destino, marcador = _doc_de_marcador(
            texto[fin:fin + VENTANA_MARCADOR_EXTERNO])
        if (punto, doc_destino) in vistos:
            continue
        vistos.add((punto, doc_destino))
        out.append({"punto": punto, "mencion_verbatim": mencion.strip(),
                    "doc_destino": doc_destino, "marcador_verbatim": marcador})
        if len(out) >= tope:
            break
    return out


def _comparativo_de_referencia(ref, doc_portador):
    """Resuelve UNA referencia a comparativo (regla B3c): sin marcador → localize
    intra-documento; marcador a TO del corpus → localize en el doc de destino
    (regla="referencia_interna_cross_doc"); marcador a TO fuera del corpus → comparativo
    "omitido_fuera_de_corpus" SIN localize (nunca intra-documento)."""
    base = {"tipo": "referencia_interna", "punto": ref["punto"],
            "mencion_verbatim": ref["mencion_verbatim"]}
    if ref["doc_destino"] == "fuera_de_corpus":
        return {**base, "regla": "referencia_interna",
                "marcador_verbatim": ref["marcador_verbatim"],
                "estado": "omitido_fuera_de_corpus", "nota": NOTA_FUERA_DE_CORPUS}
    if ref["doc_destino"]:
        doc, regla = ref["doc_destino"], "referencia_interna_cross_doc"
    else:
        doc, regla = doc_portador, "referencia_interna"
    r = _pasaje_de(doc, f"Punto {ref['punto']}")
    out = {**base, "regla": regla, **r,
           "estado": "localizado" if r["localizacion_pdf"] == "ok" else "fallido"}
    if regla == "referencia_interna_cross_doc":
        out["doc_destino"] = doc
        out["marcador_verbatim"] = ref["marcador_verbatim"]
    return out


def _extraer_portador_s1(atrib, ids_kg):
    """Extractor de portador PROPIO de S1 (B4.2). Matchea ids del kg por substring en
    evidencia.nodo.ubicacion (fallback: quote). Con múltiples matches aplica la REGLA DEL
    MAXIMAL ÚNICO: si UN id contiene a todos los demás matcheados como substrings → ese es
    el portador (la anidación de ids es propiedad del vocabulario de los grafos — ej.
    run_4: "comision" ⊂ "comision_por_precancelacion" — no ambigüedad de cita); si no
    (matches genuinamente distintos) → (None, n) como la regla pre-registrada de D2.
    Devuelve (portador_id | None, n_distintos)."""
    ev = (atrib.get("evidencia") or {}).get("nodo") or {}
    for campo in ("ubicacion", "quote"):
        texto = ev.get(campo) or ""
        matches = sorted({nid for nid in ids_kg if nid in texto})
        if not matches:
            continue
        if len(matches) == 1:
            return (matches[0], 1)
        maximales = [m for m in matches if all(otro in m for otro in matches)]
        if len(maximales) == 1:
            return (maximales[0], len(matches))
        return (None, len(matches))
    return (None, 0)


def _comparativos_de_punto(punto):
    """Regla determinística del diseño §2 (mecánica, sin juicio). Devuelve
    (lista de {tipo, punto, regla}, notas)."""
    niveles = punto.split(".")
    comps, notas = [], []
    if len(niveles) == 1:
        notas.append("sin_comparativos_por_regla: el punto del portador ya es de primer "
                     "nivel (no hay sección madre distinta ni padre un nivel arriba)")
        return comps, notas
    comps.append({"tipo": "seccion_madre", "punto": niveles[0],
                  "regla": "encabezado de la sección madre: primer nivel del punto del portador"})
    if len(niveles) >= 3:
        comps.append({"tipo": "punto_general_un_nivel_arriba",
                      "punto": ".".join(niveles[:-1]),
                      "regla": "mismo prefijo, un nivel arriba (padre inmediato del punto del portador)"})
    else:
        notas.append("padre_inmediato_coincide_con_seccion_madre: el punto tiene 2 niveles; "
                     "el comparativo 'un nivel arriba' es la propia sección madre (no se duplica)")
    return comps, notas


def _pasaje_de(source_doc, location):
    """Envuelve localize registrando la location consultada verbatim."""
    r = localize(source_doc, location)
    return {"source_doc": source_doc, "location_consultada": location,
            "metodo": r["metodo"], "ref": r["ref"], "pasaje": r["pasaje"],
            "localizacion_pdf": r["localizacion_pdf"]}


def construir_paquete_fuentes(caso_json, run, trace_path=None, *,
                              sintoma_F=None, sintoma_P=None):
    """Fetch determinístico de S1 según la semántica pre-registrada del docstring del
    módulo. Puro (sin API): kg + provenances + pdf_locate.

    El síntoma (F, P) sale de la traza post-hoc (`trace_path`, vía _sintoma_de_trace — el
    mismo filtro que build_falla_context) o se inyecta (sintoma_F/sintoma_P, tests sin
    disco). Exactamente una de las dos vías es obligatoria."""
    index = _index_de(run)
    ids_kg = list(index.by_id.keys())

    if trace_path is not None:
        sintoma_F, sintoma_P = _sintoma_de_trace(trace_path)
    elif sintoma_F is None or sintoma_P is None:
        raise ValueError("falta trace_path, o la dupla sintoma_F/sintoma_P (listas)")

    voto = caso_json.get("voto_capa_d")
    if voto is None:
        raise ValueError("construir_paquete_fuentes requiere la salida de la capa "
                         "determinística (falta voto_capa_d)")
    exoneracion_con_sintoma = (
        voto.get("pares_primarios_ganadores") == [] and bool(sintoma_F or sintoma_P))

    entradas = []
    for n_rep, rep in enumerate(caso_json.get("repeticiones") or [], 1):
        if rep.get("formato_invalido"):
            continue
        for j, atrib in enumerate(rep.get("atribuciones") or [], 1):
            causa = atrib.get("causa_capa2")
            if causa in CAUSAS_GATILLO_S1:
                tipo_gatillo = "causa_gatillada"
            elif exoneracion_con_sintoma and causa == "sin_defecto":
                tipo_gatillo = "exoneracion_con_sintoma"
            else:
                continue

            entrada = {
                "id_atribucion": f"rep{n_rep}_atrib{j}",
                "rep": n_rep, "atrib_idx": j,
                "tipo_gatillo": tipo_gatillo,
                "sintoma_capa1": atrib.get("sintoma_capa1"),
                "causa_capa2": causa,
                "jerarquia": atrib.get("jerarquia"),
            }
            portador, n_ids = _extraer_portador_s1(atrib, ids_kg)
            if portador is None:
                entrada.update({"portador_id": None, "n_ids_detectados": n_ids,
                                "estado": "sin_portador_extraible"})
                entradas.append(entrada)
                continue
            entrada["portador_id"] = portador
            entrada["n_ids_detectados"] = n_ids

            # cascada de provenances (B4.2): la PRIMERA parseable QUE LOCALIZA
            provs = index.by_id[portador].provenances or []
            entrada["provenances_total"] = len(provs)
            intentos, elegida = [], None
            for i, p in enumerate(provs):
                pt = parse_point(p.get("location"))
                if not pt:
                    continue
                r = _pasaje_de(p["source_doc"], p["location"])
                intentos.append({"idx": i, "location": p["location"], "ref": r["ref"],
                                 "localizacion_pdf": r["localizacion_pdf"]})
                if r["localizacion_pdf"] == "ok":
                    elegida = (i, p, pt, r)
                    break
            if not intentos:
                entrada.update({"estado": "provenance_no_parseable",
                                "provenances_verbatim": provs})
                entradas.append(entrada)
                continue
            entrada["provenances_intentadas"] = intentos
            if elegida is None:
                entrada["estado"] = "localizacion_fallida"
                entradas.append(entrada)
                continue
            prov_idx, prov_usada, punto, pasaje = elegida
            entrada.update({"provenance": {"source_doc": prov_usada["source_doc"],
                                           "location": prov_usada["location"]},
                            "provenance_usada_idx": prov_idx, "punto_parseado": punto,
                            "pasaje_portador": pasaje})

            comps, notas = _comparativos_de_punto(punto)
            comparativos = []
            for c in comps:
                if c["tipo"] == "seccion_madre":
                    # corrección B3b (hecho b): omitida SIEMPRE, sin llamar a localize
                    comparativos.append({**c, "estado": "omitido",
                                         "nota": NOTA_MADRE_OMITIDA})
                    continue
                r = _pasaje_de(prov_usada["source_doc"], f"Punto {c['punto']}")
                comparativos.append({**c, **r,
                                     "estado": "localizado" if r["localizacion_pdf"] == "ok"
                                     else "fallido"})
            # corrección B3b (hecho a): referencias internas del TEXTO del pasaje;
            # corrección B3c: resolución por marcador de documento externo
            for ref in _referencias_de_pasaje(pasaje["pasaje"]):
                comparativos.append(
                    _comparativo_de_referencia(ref, prov_usada["source_doc"]))
            entrada["comparativos"] = comparativos
            entrada["notas_regla"] = notas
            # política NO BLOQUEANTE (B3b): completo = el PORTADOR localizó
            entrada["estado"] = "completo"
            entradas.append(entrada)

    return {
        "id_falla": caso_json.get("id_falla"),
        "run": caso_json.get("run"),
        "version_s1": S1_VERSION,
        "gatillo_caso": {
            "exoneracion_con_sintoma": exoneracion_con_sintoma,
            "sintoma_F_n": len(sintoma_F),
            "sintoma_P_n": len(sintoma_P),
        },
        "atribuciones": entradas,
    }


# --------------------------------------------------------------------------- #
# 2. JUICIO S1 (LLM) — implementado; su ejecución con API es decisión de B4+   #
# --------------------------------------------------------------------------- #
def _nodo_para_prompt(nodo):
    return json.dumps({"id": nodo.id, "type": nodo.type, "label": nodo.label,
                       "properties": nodo.properties}, ensure_ascii=False, indent=1)


def _pasajes_para_prompt(entrada):
    partes = [f"[PORTADOR — provenance verbatim: {entrada['provenance']['location']!r} "
              f"({entrada['provenance']['source_doc']}); {entrada['pasaje_portador']['ref']}]\n"
              f"{entrada['pasaje_portador']['pasaje']}"]
    for c in entrada.get("comparativos") or []:
        if c["estado"] == "localizado":
            origen = (f"; mención de origen: {c['mencion_verbatim']!r}"
                      if c.get("mencion_verbatim") else "")
            partes.append(f"[COMPARATIVO {c['tipo']} — regla: {c['regla']}{origen}; "
                          f"{c['ref']}]\n{c['pasaje']}")
        else:
            detalle = f": {c['nota']}" if c.get("nota") else ""
            partes.append(f"[COMPARATIVO {c['tipo']} (Punto {c['punto']}) — "
                          f"{c['estado']}{detalle}]")
    for nota in entrada.get("notas_regla") or []:
        partes.append(f"[NOTA MECÁNICA DEL FETCH: {nota}]")
    return "\n\n".join(partes)


def _sintoma_para_prompt(sintoma_F, sintoma_P):
    """Síntoma del caso para el input de S1 (B4.3): claims reprobados con veredicto y
    centralidad + patas no cubiertas — lo que el verificador vio y S1 hasta v0.1 no."""
    partes = []
    for c in sintoma_F or []:
        rot = "CENTRAL" if c.get("central") else "secundario"
        partes.append(f"- claim reprobado ({rot}, verdict={c.get('verdict')}): "
                      f"\"{c.get('enunciado')}\"")
    for p in sintoma_P or []:
        partes.append(f"- pata NO CUBIERTA: \"{p}\"")
    return "\n".join(partes) if partes else "(síntoma vacío)"


def _prompt_s1(atrib, nodo, entrada, sintoma_F=None, sintoma_P=None):
    vista = {k: atrib.get(k) for k in
             ("sintoma_capa1", "causa_capa2", "lado", "jerarquia", "pata", "evidencia")}
    return S1_PROMPT.format(
        sintoma=_sintoma_para_prompt(sintoma_F, sintoma_P),
        atribucion=json.dumps(vista, ensure_ascii=False, indent=1),
        portador_id=entrada["portador_id"],
        nodo=_nodo_para_prompt(nodo),
        pasajes=_pasajes_para_prompt(entrada))


def _prompt_s1_exoneracion(atrib, nodo, entrada, sintoma_P, respuesta_agente):
    vista = {k: atrib.get(k) for k in
             ("sintoma_capa1", "causa_capa2", "lado", "jerarquia", "pata", "evidencia")}
    patas = "\n".join(f"- \"{p}\"" for p in (sintoma_P or [])) or "(sin patas registradas)"
    return S1_PROMPT_EXONERACION.format(
        patas=patas,
        respuesta=respuesta_agente or "(no provista)",
        atribucion=json.dumps(vista, ensure_ascii=False, indent=1),
        portador_id=entrada["portador_id"],
        nodo=_nodo_para_prompt(nodo),
        pasajes=_pasajes_para_prompt(entrada))


def _llamada_s1(client, prompt, model, esquema="causa"):
    """UNA llamada al modelo del verificador; parsea el JSON estricto y valida el esquema
    correspondiente (B4.3: "causa" = comparación de alcances con sintoma_del_par;
    "exoneracion" = rama de completitud). Salida inválida → {"error": ...} (cuenta como no
    decidida). Devuelve (salida, usage) — usage REAL de la API (B4.2)."""
    resp = client.messages.create(model=model, max_tokens=S1_MAX_TOKENS,
                                  messages=[{"role": "user", "content": prompt}])
    u = getattr(resp, "usage", None)
    usage = {"input_tokens": getattr(u, "input_tokens", None),
             "output_tokens": getattr(u, "output_tokens", None)}
    texto = "".join(getattr(b, "text", "") for b in resp.content)
    out = _extract_json(texto)
    if not isinstance(out, dict):
        return {"error": "json_no_parseable", "texto_crudo": texto[:2000]}, usage
    campos = CAMPOS_S1 if esquema == "causa" else CAMPOS_S1_EXON
    faltantes = [k for k in campos if k not in out]
    if faltantes:
        return {"error": f"campos_faltantes:{','.join(faltantes)}", "salida_cruda": out}, usage
    campo_dec = "coinciden" if esquema == "causa" else "presente_en_grafo"
    if out.get(campo_dec) not in COINCIDEN_VALORES:
        return {"error": f"{campo_dec}_invalido:{out.get(campo_dec)!r}", "salida_cruda": out}, usage
    # B4.5 — validación de DOMINIO: valor fuera del vocabulario cerrado → la muestra se
    # trata como no_determinable (no vota) con anotación fuera_de_dominio, valor verbatim
    # preservado. La salida NO se reescribe.
    fuera = []
    if esquema == "causa" and out.get("sintoma_del_par") not in SINTOMAS_VALORES:
        fuera.append({"campo": "sintoma_del_par",
                      "valor_verbatim": out.get("sintoma_del_par")})
    if out.get("causa_confirmada_o_corregida") not in CAUSAS_VALIDAS:
        fuera.append({"campo": "causa_confirmada_o_corregida",
                      "valor_verbatim": out.get("causa_confirmada_o_corregida")})
    if fuera:
        out = {**out, "fuera_de_dominio": fuera}
    return out, usage


def _voto_s1_atrib(salidas, n, esquema="causa"):
    """Voto propio de S1 por atribución: mayoría estricta ≥ n//2+1 sobre las salidas
    DECIDIDAS (campo de decisión ∈ {si, no}); errores y no_determinable no deciden.
    B4.3: en el esquema "causa" la clave del voto es el PAR (sintoma_del_par, causa); en
    "exoneracion" (campo de decisión presente_en_grafo) la clave es la causa sola."""
    umbral = n // 2 + 1
    campo_dec = "coinciden" if esquema == "causa" else "presente_en_grafo"
    decididas = [s for s in salidas
                 if "error" not in s and "fuera_de_dominio" not in s
                 and s.get(campo_dec) in ("si", "no")]
    conteo = {}
    for s in decididas:
        clave = ((s.get("sintoma_del_par"), s["causa_confirmada_o_corregida"])
                 if esquema == "causa" else (None, s["causa_confirmada_o_corregida"]))
        conteo.setdefault(clave, []).append(s)
    orden = sorted(conteo.items(), key=lambda kv: (-len(kv[1]), str(kv[0])))
    ganadora = orden[0] if orden and len(orden[0][1]) >= umbral else None
    return {
        "n": n, "umbral": umbral, "esquema": esquema,
        "decididas": len(decididas),
        "no_decididas": len(salidas) - len(decididas),
        "resultado": "mayoria" if ganadora else "no_determinable",
        "sintoma_ganador": ganadora[0][0] if ganadora else None,
        "causa_ganadora": ganadora[0][1] if ganadora else None,
        "votos_ganadores": len(ganadora[1]) if ganadora else None,
    }


def aplicar_s1(caso_json, run, paquete, n=1, *, client=None, model=MODEL_VERIF,
               sintoma_F=None, sintoma_P=None, respuesta_agente=None):
    """Aplica el juicio S1 según la semántica pre-registrada del docstring del módulo.
    Juzga SOLO las atribuciones con paquete "completo"; el resto va a triage_s1 con motivo
    fuente_no_verificable. NUNCA borra la emisión de v6.1-D: anota capa_s1, recomputa
    voto_s1 y preserva voto / voto_capa_d / voto_pre_d6 intactos.

    B4.3 (s1-v0.2-dev): el input incluye el SÍNTOMA del caso (sintoma_F/sintoma_P — las
    marcas del juez que el verificador vio); el esquema del gatillo por causas exige
    sintoma_del_par y el voto/las correcciones son por PAR (síntoma, causa) — la corrección
    reescribe sintoma_capa1 Y causa_capa2, con la emisión preservada en capa_s1. El gatillo
    de exoneración usa la RAMA DE COMPLETITUD (S1_PROMPT_EXONERACION): pata no cubierta +
    respuesta del agente + portador + pasajes (JAMÁS el GT del eval set); campo de decisión
    presente_en_grafo; una corrección de exoneración fija sintoma_capa1=context_recall (la
    rama se define por la pata no cubierta).

    `client` se inyecta (en producción, el cliente del verificador; en tests, un mock).
    Sin atribuciones a juzgar no se hace ninguna llamada (client puede ser None)."""
    index = _index_de(run)
    salida = copy.deepcopy(caso_json)
    reps = salida.get("repeticiones") or []

    motivos, flags = [], []
    juzgadas = corregidas = no_det = fallidas_fetch = 0
    tokens_in_s1 = tokens_out_s1 = 0

    for entrada in paquete.get("atribuciones") or []:
        atrib = reps[entrada["rep"] - 1]["atribuciones"][entrada["atrib_idx"] - 1]
        base = {"version": S1_VERSION,
                "id_atribucion": entrada["id_atribucion"],
                "tipo_gatillo": entrada["tipo_gatillo"],
                "estado_fetch": entrada["estado"],
                "emision_v61d": {"sintoma_capa1": atrib.get("sintoma_capa1"),
                                 "causa_capa2": atrib.get("causa_capa2"),
                                 "jerarquia": atrib.get("jerarquia")}}
        if entrada["estado"] != "completo":
            atrib["capa_s1"] = {**base, "accion": "fuente_no_verificable",
                                "corrigio": False, "triage": True}
            fallidas_fetch += 1
            if "fuente_no_verificable" not in motivos:
                motivos.append("fuente_no_verificable")
            flags.append(f"S1: {entrada['id_atribucion']} — fetch {entrada['estado']}")
            continue

        if client is None:
            raise ValueError("aplicar_s1 requiere client para juzgar paquetes completos")
        nodo = index.by_id[entrada["portador_id"]]
        if entrada["tipo_gatillo"] == "exoneracion_con_sintoma":
            esquema = "exoneracion"
            prompt = _prompt_s1_exoneracion(atrib, nodo, entrada, sintoma_P,
                                            respuesta_agente)
        else:
            esquema = "causa"
            prompt = _prompt_s1(atrib, nodo, entrada, sintoma_F, sintoma_P)
        llamadas = [_llamada_s1(client, prompt, model, esquema=esquema)
                    for _ in range(n)]
        salidas = [s for s, _ in llamadas]
        usages = [u for _, u in llamadas]
        tokens_in_s1 += sum(u.get("input_tokens") or 0 for u in usages)
        tokens_out_s1 += sum(u.get("output_tokens") or 0 for u in usages)
        voto_atrib = _voto_s1_atrib(salidas, n, esquema=esquema)
        juzgadas += 1

        if voto_atrib["resultado"] != "mayoria":
            atrib["capa_s1"] = {**base, "esquema": esquema,
                                "salidas_s1": salidas, "usage_s1": usages,
                                "voto_s1_atrib": voto_atrib,
                                "accion": "no_determinable", "corrigio": False,
                                "triage": True}
            no_det += 1
            if "fuente_no_verificable" not in motivos:
                motivos.append("fuente_no_verificable")
            flags.append(f"S1: {entrada['id_atribucion']} — no_determinable "
                         f"({voto_atrib['decididas']}/{n} decididas)")
            continue

        causa_final = voto_atrib["causa_ganadora"]
        if esquema == "causa":
            sintoma_final = voto_atrib["sintoma_ganador"]
        else:
            # la rama de exoneración se define por la pata no cubierta: una corrección
            # lleva síntoma context_recall; una confirmación no toca el síntoma
            sintoma_final = ("context_recall" if causa_final != "sin_defecto"
                            else atrib.get("sintoma_capa1"))
        corrigio = (causa_final != atrib.get("causa_capa2")
                    or sintoma_final != atrib.get("sintoma_capa1"))
        anot = {**base, "esquema": esquema,
                "salidas_s1": salidas, "usage_s1": usages,
                "voto_s1_atrib": voto_atrib,
                "corrigio": corrigio,
                "par_post_s1": [sintoma_final, causa_final],
                "causa_post_s1": causa_final,
                "triage": False}
        if corrigio:
            atrib["sintoma_capa1"] = sintoma_final
            atrib["causa_capa2"] = causa_final
            corregidas += 1
            # regla mecánica de jerarquía (B4.3 r2) — SOLO exoneraciones corregidas
            if esquema == "exoneracion" and causa_final != "sin_defecto":
                anot["jerarquia_original"] = atrib.get("jerarquia")
                if sintoma_P:
                    if len(sintoma_P) == 1:
                        atrib["pata"] = sintoma_P[0]
                    else:
                        atrib["pata"] = list(sintoma_P)
                        anot["nota"] = "mecanica_sin_mapeo"
                    atrib["jerarquia"] = "primaria"
                else:
                    quote = ((atrib.get("evidencia") or {}).get("afirmacion")
                             or {}).get("quote") or ""
                    mapeados = _mapear_claim(quote, sintoma_F or [])
                    atrib["jerarquia"] = ("primaria"
                                          if any(c.get("central") for c in mapeados)
                                          else "secundaria")
                    anot["mapeo_claims"] = [c.get("enunciado") for c in mapeados]
                anot["jerarquia_post_s1"] = atrib["jerarquia"]
        atrib["capa_s1"] = anot

    salida["voto_s1"] = _recomputar_voto(reps)
    salida["triage_s1"] = {"triage": bool(motivos), "motivos": motivos, "flags": flags}
    salida["resumen_s1"] = {
        "gatilladas": len(paquete.get("atribuciones") or []),
        "juzgadas_llm": juzgadas,
        "corregidas": corregidas,
        "no_determinable": no_det,
        "fetch_fallido": fallidas_fetch,
        "tokens_in_s1": tokens_in_s1,
        "tokens_out_s1": tokens_out_s1,
        "exoneracion_con_sintoma": paquete.get("gatillo_caso", {}).get(
            "exoneracion_con_sintoma", False),
    }
    salida["version_capa_s1"] = S1_VERSION
    return salida


# --------------------------------------------------------------------------- #
# CLI                                                                          #
# --------------------------------------------------------------------------- #
def _trace_default(caso_json):
    """Traza post-hoc canónica derivada de id_falla (run/CQ-XXX) — mismo layout que usa el
    pipeline: posthoc_run/traces/off/{run}/{qid}.json. Overrideable con --trace."""
    run, qid = caso_json["id_falla"].split("/")
    return Path(__file__).resolve().parent / "posthoc_run" / "traces" / "off" / run / f"{qid}.json"


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="S1 — segunda pasada con fuentes forzadas (v7 = v6.1-D + S1)")
    ap.add_argument("--caso", required=True, help="path al JSON _capa_d (salida de v6.1-D)")
    ap.add_argument("--run", required=True, help="clave del run (p. ej. run_3)")
    ap.add_argument("--out", required=True, help="path del JSON de salida")
    ap.add_argument("--n", type=int, default=1,
                    help="repeticiones del juicio S1 por atribución (política a decidir en B4)")
    ap.add_argument("--solo-fetch", action="store_true",
                    help="corre SOLO el fetch determinístico y emite el paquete (sin API)")
    ap.add_argument("--trace", default=None,
                    help="traza post-hoc del caso (default: derivada de id_falla)")
    args = ap.parse_args(argv)

    caso = json.load(open(args.caso))
    trace = args.trace or _trace_default(caso)
    paquete = construir_paquete_fuentes(caso, args.run, trace_path=trace)

    if args.solo_fetch:
        with open(args.out, "w") as f:
            json.dump(paquete, f, ensure_ascii=False, indent=1)
        print(json.dumps({"out": args.out, "version_s1": S1_VERSION, "solo_fetch": True,
                          "gatillo_caso": paquete["gatillo_caso"],
                          "atribuciones": [{k: e.get(k) for k in
                                            ("id_atribucion", "tipo_gatillo", "estado",
                                             "portador_id")}
                                           for e in paquete["atribuciones"]]},
                         ensure_ascii=False, indent=1))
        return

    # Modo completo (juicio con LLM). La caché / política de N se decide en B4.
    import anthropic
    client = anthropic.Anthropic(max_retries=3)
    sintoma_F, sintoma_P = _sintoma_de_trace(trace)
    elem = json.load(open(trace))[0]
    respuesta_agente = json.dumps(elem["trace"].get("final_json"), ensure_ascii=False,
                                  indent=1)
    salida = aplicar_s1(caso, args.run, paquete, n=args.n, client=client,
                        sintoma_F=sintoma_F, sintoma_P=sintoma_P,
                        respuesta_agente=respuesta_agente)
    with open(args.out, "w") as f:
        json.dump(salida, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": args.out, "version_capa_s1": salida["version_capa_s1"],
                      "resumen_s1": salida["resumen_s1"],
                      "triage_s1": salida["triage_s1"],
                      "voto_s1": salida["voto_s1"]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
