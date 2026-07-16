"""capa_deterministica.py — capa determinística del verificador: D2 (decisor de la frontera
navegación / alcanzabilidad_kg), D3 (validador de quotes de aplicacion_erronea) y D4
(política de triage a nivel caso). Punto de entrada compuesto: aplicar_capa (D2 → D3 → D4).

Módulo que no modifica congelados (verificador.py, harness.py, taxonomia.md,
casos_control.md, test_alcanzabilidad.py). Consume la salida del verificador (JSON de caso
con repeticiones) y el módulo D1 (test_alcanzabilidad).

SEMÁNTICA PRE-REGISTRADA DE D2 (verbatim del pedido de implementación)
----------------------------------------------------------------------
- Recorre las repeticiones válidas (formato_invalido=false). Para cada atribución cuyo par
  (sintoma_capa1, causa_capa2) sea exactamente (context_recall, navegación) o
  (context_recall, alcanzabilidad_kg):
  a. Extrae el portador_id: busca en evidencia.nodo.ubicacion (y como fallback en
     evidencia.nodo.quote) un id de nodo EXISTENTE en el grafo del run, por match exacto de
     substring contra la lista de ids del kg. Si encuentra cero o más de uno distintos → NO
     corrige: anota capa_d = {modulo: "D2", accion: "sin_portador_extraible", triage: true}
     y sigue.
  b. Con portador_id único: corre test_alcanzabilidad.evaluar_alcanzabilidad con la pregunta
     y las consultas buscar_nodos de la traza post-hoc del caso, y los tokens expuestos vía
     tokens_expuestos_de_trace. alcanzable=False → causa_capa2 := alcanzabilidad_kg;
     alcanzable=True → causa_capa2 := navegación.
  c. Anota SIEMPRE capa_d en la atribución: {modulo: "D2", emision_llm: <causa original>,
     decision_codigo: <causa final>, discrepancia: <bool>, alcanzable: <bool>,
     evidencia_d1: <dict de D1 SIN la lista completa de consultas; conservá
     n_consultas_simuladas, la lista de consultas con en_top10=true, y el mejor rank>}.
- Atribuciones con otros pares: intactas, sin capa_d.
- Recomputa el voto con la regla del protocolo (mayoría estricta ≥2 sobre reps válidas,
  sobre el multiconjunto de pares primarios YA corregidos; sin mayoría → triage) y lo emite
  como voto_capa_d, preservando el voto original intacto en el JSON de salida.
- El dict de salida es el caso_json completo + las anotaciones + un bloque resumen_capa_d:
  {reps_tocadas, atribuciones_corregidas, discrepancias, triage}.

Notas de implementación (no alteran la semántica de arriba):
- La causa "navegación" se reconoce en sus dos grafías (con y sin acento) por robustez de
  fuente; la decisión de código se emite SIEMPRE con la grafía de la taxonomía
  ("navegación" / "alcanzabilidad_kg").
- `run` acepta la clave del run (str) o un harness.GraphIndex ya construido (tests con grafo
  sintético, sin disco), igual que en D1.
- Los insumos de D1 (pregunta, consultas del agente, tokens expuestos) salen de la traza
  post-hoc (`trace_path`); para tests sin disco pueden inyectarse por parámetro
  (pregunta/consultas_agente/tokens_expuestos). Exactamente una de las dos vías es
  obligatoria.
- El match de substring del extractor exige ids completos como los escribe el verificador
  (la evidencia del contrato usa el id verbatim en `ubicacion`); si más de un id distinto
  del kg matchea (p. ej. un id contenido en otro), se cae a `sin_portador_extraible` por la
  regla pre-registrada — sin heurísticas de desempate.
- El recomputo del voto usa como clave de cada rep válida el MULTICONJUNTO ordenado de sus
  pares primarios corregidos (misma noción de clave que el voto programático del
  verificador); las reps inválidas no votan.

SEMÁNTICA PRE-REGISTRADA DE D3 (verbatim del pedido de implementación)
----------------------------------------------------------------------
- Para cada atribución de cada rep válida con causa_capa2 == "aplicacion_erronea":
  a. Extrae portador con el MISMO extractor de D2 (_extraer_portador). Sin portador único →
     capa_d = {modulo: "D3", accion: "sin_portador_extraible", triage: true}.
  b. Con portador: verifica que evidencia.nodo.quote esté contenido VERBATIM-NORMALIZADO
     (lowercase, sin acentos vía la normalización de harness, espacios colapsados) en el
     contenido del nodo (label + valores de properties, mismo blob normalizado). Verifica →
     capa_d = {modulo: "D3", quote_verificado: true}. No verifica → capa_d = {modulo: "D3",
     quote_verificado: false, accion: "quote_no_verificable", triage: true}.
- D3 NUNCA cambia causa_capa2.

LIMITACIÓN DE D3 (documentada): D3 verifica la condición COMPUTABLE necesaria — que el quote
exista en el contenido del nodo —, no la suficiente: que el quote sea una DECLARACIÓN DE
ALCANCE (cartera, régimen, sección; test v2.6 de la taxonomía). Esa lectura es semántica y
queda para el humano del triage. Un quote verificado NO valida la atribución; un quote no
verificable sí la manda a triage.

SEMÁNTICA PRE-REGISTRADA DE D4 (verbatim del pedido de implementación)
----------------------------------------------------------------------
- Reglas de triage a nivel caso, sobre el JSON ya pasado por D2 y D3. Emite bloque
  triage_capa_d = {triage: bool, motivos: [...], flags: [...]}:
  - R1 exoneracion_total: la clave ganadora de voto_capa_d es vacía (sin pares primarios) →
    triage, motivo "exoneracion_total".
  - R2 aplicacion_erronea_presente: cualquier atribución (post-D3) con causa
    aplicacion_erronea → triage, motivo "aplicacion_erronea_bajo_revision" (medida TEMPORAL
    documentada: sesgo medido sin mitigar; revisable con evidencia fresca).
  - R3 propagacion: cualquier capa_d con triage:true (de D2 o D3) → triage, motivo
    "modulo_deterministico_sin_decision".
  - R4 voto_dividido: voto_capa_d.flag_voto_dividido == true → triage, motivo
    "voto_dividido".
  - Los motivos se acumulan (lista, sin duplicados); triage = lista no vacía.

SEMÁNTICA PRE-REGISTRADA DE D5 (verbatim del pedido de implementación)
----------------------------------------------------------------------
- Gatillo: toda atribución de rep válida cuya causa_capa2 (YA corregida por D2) sea
  "completitud_kg" o "alucinacion_agente".
- Extracción de literales, SOLO de evidencia.afirmacion.quote y del campo pata, por regex
  cerrada (documentada como constante):
  (a) montos: USD/US$ seguido de número (con puntos de miles opcionales);
  (b) códigos numéricos de 5+ dígitos;
  (c) referencias a puntos de AL MENOS dos niveles: \\d+\\.\\d+(\\.\\d+)* (descartá las de
      un solo nivel tipo "1.1" solas: demasiado genéricas — limitación documentada).
  Sin literales extraíbles → capa_d = {modulo: "D5", accion: "sin_literales", banderas: []}
  y sigue (sin triage).
- Barrido: cada literal, normalizado (lowercase, sin acentos, espacios colapsados), por
  substring contra el blob normalizado de id + label + properties de cada nodo del kg — SIN
  provenances (pre-registrado: las provenances citan puntos por diseño y meterían ruido de
  metadatos).
- Filtro de exposición: para cada nodo candidato, verificá si su id aparece como substring
  en ALGÚN output COMPLETO re-ejecutado de la traza (helper
  test_alcanzabilidad.outputs_completos_de_trace). Candidato EXPUESTO → descartado (el
  agente lo tuvo a la vista; si lo descartó mal, ese punto ciego queda documentado como
  limitación).
- Para cada candidato NO expuesto: corré D1 (evaluar_alcanzabilidad, con los mismos insumos
  que D2 usa) y emití bandera: {literal, candidato_id, alcanzable: <bool>, mejor_rank,
  expuesto: false}.
- Anotación por atribución gatillada: capa_d = {modulo: "D5", literales: [...],
  candidatos_evaluados: <n>, banderas: [...], triage: <true si banderas no vacía>}. D5 NUNCA
  cambia causa_capa2 ni jerarquías.
- Nota: si la atribución ya tiene capa_d de otro módulo, guardá la de D5 bajo la clave
  capa_d5 (los módulos no se pisan).

Notas de implementación de D3/D4/D5 (no alteran la semántica de arriba):
- El capa_d de D3 incluye además `portador_id` (mismo criterio informativo que D2).
- D4 recorre las atribuciones de las reps VÁLIDAS (las inválidas no votan ni disparan
  reglas); exige `voto_capa_d` presente (el bloque lo produce D2) — sin él, ValueError.
- `flags` de triage_capa_d: detalle de procedencia de cada disparo (regla + rep + pata),
  determinístico, sin duplicados.
- Reglas de D4 con D5 integrado: R5 = cualquier bandera de D5 → triage, motivo
  "posible_portador_no_considerado". R3 sigue cubriendo los triage de módulos SIN DECISIÓN
  (acciones sin_portador_extraible / quote_no_verificable de D2/D3); el triage de D5 por
  banderas dispara R5, no R3 (D5 con banderas SÍ decidió: encontró candidatos).
- Regla de "un solo nivel" de la extracción (c): la regex base \\d+\\.\\d+(\\.\\d+)* con el
  descarte de un nivel equivale a exigir al menos dos puntos ("1.1.2" sí; "1.1"/"3.9" no) —
  limitación documentada: referencias de dos componentes no disparan barrido.
- Los literales se barren tal como se extraen (sin canonicalizar variantes USD/US$/u$s entre
  sí); el blob del nodo incluye claves y valores de properties.
- Patrón (d) "coeficiente_decimal" (extensión 2026-07-15): \\d+,\\d+ — decimales con COMA,
  la notación normativa argentina de coeficientes y alícuotas — con guarda de límites (no
  precedido ni seguido por dígito, para no capturar dentro de números mayores). MOTIVACIÓN
  POR MECANISMO (no por un caso del gate): el error documentado de barrido léxico en la
  construcción de la vara — las variantes "0.08"/"0,08" y "APRc"/"APR_c" dieron
  presente/ausente según la grafía (docs/evidencia_vara_v3/verificaciones_vara_v3.md §3b) —
  es exactamente la clase de omisión que D5 existe para atajar. LIMITACIÓN SIMÉTRICA
  documentada: los decimales con PUNTO ("0.08") NO se extraen — colisionan con las
  referencias a puntos normativos de un nivel ("3.9"), que la extracción (c) descarta por
  genéricas. Comportamiento fijado para números con punto de miles ("1.100,50"): la guarda
  es por dígito adyacente, y el punto de miles no es dígito, así que se extrae el tramo
  decimal posterior al último punto ("100,50") — fijado en test.
- `candidatos_evaluados` = candidatos únicos hallados por el barrido (los EXPUESTOS se
  descartan y se cuentan aparte en `candidatos_expuestos_descartados`; los NO expuestos
  pasan por D1 y emiten bandera).
- aplicar_d5 acepta las mismas dos vías de insumos que aplicar_d2, más `outputs_completos`
  inyectable (lista de str) para tests sin disco; con `trace_path` sale de
  outputs_completos_de_trace.
SEMÁNTICA PRE-REGISTRADA DE D6 (verbatim del pedido de implementación — v6.1-D)
-------------------------------------------------------------------------------
- El síntoma del caso se extrae de la traza post-hoc con el MISMO filtro que
  build_falla_context (verificador.py:547; el filtro de claims reprobados vive en las líneas
  583-591: verdict ∈ {falso, no_soportado} sobre judge.step2.verificaciones):
  F = claims reprobados del juez post-hoc (enunciado + centralidad); P = patas con
  cobertura "no_cubierta" (judge.step2.cobertura_patas).
- R6a — atribución sin síntoma: si F y P están VACÍOS y alguna rep válida contiene una
  atribución con causa_capa2 ∉ {sin_defecto}: anotá en cada una
  capa_d6={regla:"R6a", accion:"atribucion_sin_sintoma"} y marcá el caso para triage. NO
  reescribas causas ni jerarquías (el síntoma vacío es información para el humano, no
  licencia para inventar el veredicto correcto).
- R6b — jerarquía acotada por centralidad: para cada atribución PRIMARIA de rep válida con
  sintoma_capa1 ∈ {noise_sensitivity, faithfulness}: mapeá su evidencia.afirmacion.quote
  contra los enunciados de F por substring normalizado (lowercase, sin acentos, espacios
  colapsados; en ambas direcciones — quote⊆enunciado o enunciado⊆quote). Si mapea SOLO a
  claims secundarios → degradá jerarquia a "secundaria" y anotá capa_d6={regla:"R6b",
  emision_llm:"primaria", decision_codigo:"secundaria", claim_mapeado:<enunciado>}. Si mapea
  a algún central → intacta. Si no mapea a NINGÚN claim de F → capa_d6={regla:"R6b",
  accion:"claim_no_mapeado"} + triage (sin degradar: sin mapeo no hay hecho que autorice
  reescritura). Las primarias de context_recall no se degradan por R6b (su síntoma son
  patas, no claims); si P está vacío y F no, una primaria context_recall queda cubierta por
  la lógica de R6a solo si TODO el síntoma está vacío — si F no está vacío, anotala como
  capa_d6={regla:"R6b", accion:"context_recall_sin_pata"} + triage.
- Justificación (por mecanismo): la severidad de la atribución no puede exceder la severidad
  del síntoma declarado — F y P son hechos del INPUT del instrumento, computables por código.

Notas de implementación de D6 (no alteran la semántica de arriba):
- Cuando F y P están AMBOS vacíos rige R6a sola (R6b no corre por separado: todo el síntoma
  está vacío y la anotación por atribución ya la hace R6a).
- La anotación de D6 vive bajo la clave `capa_d6` (los módulos no se pisan).
- Orden del pipeline v6.1-D: D2 → D3 → D5 → D6 → RECOMPUTO FINAL del voto (`voto_capa_d`
  sobre jerarquías post-D6; el `voto` original queda intacto y el voto previo a D6 se
  preserva como `voto_pre_d6`, informativo) → D4, que suma dos motivos: R6a →
  "atribucion_sin_sintoma"; R6b claim_no_mapeado / context_recall_sin_pata →
  "atribucion_no_verificable". version_capa := "v6.1-D(2026-07)". El CLI no cambia de firma.
- Insumos de D6: con trace_path salen de _sintoma_de_trace; para tests sin disco se inyectan
  sintoma_F/sintoma_P (listas, pueden ser vacías; None = no provisto → error).

- aplicar_capa(caso_json, run, trace_path) corre el pipeline completo en el orden de arriba.
  Acepta la misma inyección de insumos de D1 que aplicar_d2 (tests sin disco).
"""

import argparse
import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import re

from harness import GraphIndex                      # congelado — solo import
from test_alcanzabilidad import (                   # D1 — solo import
    evaluar_alcanzabilidad,
    tokens_expuestos_de_trace,
    outputs_completos_de_trace,
    _index_de,
)

FRONTERA_NAV = {"navegación", "navegacion"}
CAUSA_NAV = "navegación"
CAUSA_ALC = "alcanzabilidad_kg"


def _en_frontera(atrib):
    return (
        atrib.get("sintoma_capa1") == "context_recall"
        and atrib.get("causa_capa2") in (FRONTERA_NAV | {CAUSA_ALC})
    )


def _extraer_portador(atrib, ids_kg):
    """Ids del kg presentes por substring exacto en evidencia.nodo.ubicacion
    (fallback: evidencia.nodo.quote). Devuelve (portador_id | None, n_distintos)."""
    ev = (atrib.get("evidencia") or {}).get("nodo") or {}
    for campo in ("ubicacion", "quote"):
        texto = ev.get(campo) or ""
        matches = sorted({nid for nid in ids_kg if nid in texto})
        if matches:
            return (matches[0], 1) if len(matches) == 1 else (None, len(matches))
    return (None, 0)


def _evidencia_d1_reducida(d1):
    """Dict de D1 sin la lista completa de consultas: n_consultas_simuladas, las consultas
    con en_top10=true, y el mejor rank."""
    ranks = [c["rank"] for c in d1["consultas"] if c["rank"] is not None]
    return {
        "alcanzable": d1["alcanzable"],
        "n_consultas_simuladas": d1["n_consultas_simuladas"],
        "consultas_en_top10": [c for c in d1["consultas"] if c["en_top10"]],
        "mejor_rank": min(ranks) if ranks else None,
    }


def _clave_primarias(rep):
    """Multiconjunto ordenado de pares primarios de la rep (sobre causas ya corregidas)."""
    pares = sorted(
        (a.get("sintoma_capa1"), a.get("causa_capa2"))
        for a in rep.get("atribuciones") or []
        if a.get("jerarquia") == "primaria"
    )
    return tuple(pares)


def _recomputar_voto(reps):
    """Regla del protocolo: mayoría estricta ≥2 sobre reps válidas; sin mayoría → triage."""
    validas = [(i + 1, r) for i, r in enumerate(reps) if not r.get("formato_invalido")]
    conteo = {}
    for n, r in validas:
        conteo.setdefault(_clave_primarias(r), []).append(n)
    orden = sorted(conteo.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    ganadora = orden[0] if orden else None
    hay_mayoria = ganadora is not None and len(ganadora[1]) >= 2
    return {
        "resultado": "mayoria" if hay_mayoria else "frontera_no_determinada",
        "flag_voto_dividido": not hay_mayoria,
        "pares_primarios_ganadores": [list(p) for p in ganadora[0]] if hay_mayoria else None,
        "votos_ganadores": len(ganadora[1]) if hay_mayoria else None,
        "reps_validas": [n for n, _ in validas],
        "conteo": [
            {"pares_primarios": [list(p) for p in clave], "votos": len(ns), "reps": ns}
            for clave, ns in orden
        ],
    }


def aplicar_d2(caso_json, run, trace_path=None, *,
               pregunta=None, consultas_agente=None, tokens_expuestos=None):
    """Aplica el decisor D2 según la semántica pre-registrada del docstring del módulo.

    Insumos de D1: o bien `trace_path` (traza post-hoc del caso: de ahí salen la pregunta,
    las consultas buscar_nodos y los tokens expuestos), o bien los tres inyectados
    (pregunta, consultas_agente, tokens_expuestos) para tests sin disco."""
    index = _index_de(run)
    ids_kg = list(index.by_id.keys())

    if trace_path is not None:
        elem = json.load(open(trace_path))[0]
        pregunta = elem["trace"]["question"]
        consultas_agente = [s["input"]["consulta"] for s in elem["trace"]["steps"]
                            if s.get("tool") == "buscar_nodos"]
        tokens_expuestos = tokens_expuestos_de_trace(trace_path, index=index)
    elif pregunta is None or consultas_agente is None or tokens_expuestos is None:
        raise ValueError("falta trace_path, o la terna pregunta/consultas_agente/tokens_expuestos")

    salida = copy.deepcopy(caso_json)
    cache_d1 = {}
    reps_tocadas, corregidas, discrepancias, triage = set(), 0, 0, 0

    for i, rep in enumerate(salida.get("repeticiones") or [], 1):
        if rep.get("formato_invalido"):
            continue
        for atrib in rep.get("atribuciones") or []:
            if not _en_frontera(atrib):
                continue
            reps_tocadas.add(i)
            portador, n_ids = _extraer_portador(atrib, ids_kg)
            if portador is None:
                atrib["capa_d"] = {"modulo": "D2", "accion": "sin_portador_extraible",
                                   "triage": True}
                triage += 1
                continue
            if portador not in cache_d1:
                cache_d1[portador] = evaluar_alcanzabilidad(
                    portador, pregunta, consultas_agente, tokens_expuestos, index)
            d1 = cache_d1[portador]
            emision = atrib["causa_capa2"]
            decision = CAUSA_NAV if d1["alcanzable"] else CAUSA_ALC
            atrib["capa_d"] = {
                "modulo": "D2",
                "portador_id": portador,
                "emision_llm": emision,
                "decision_codigo": decision,
                "discrepancia": decision != emision and not (
                    decision == CAUSA_NAV and emision in FRONTERA_NAV),
                "alcanzable": d1["alcanzable"],
                "evidencia_d1": _evidencia_d1_reducida(d1),
            }
            atrib["causa_capa2"] = decision
            corregidas += 1
            if atrib["capa_d"]["discrepancia"]:
                discrepancias += 1

    salida["voto_capa_d"] = _recomputar_voto(salida.get("repeticiones") or [])
    salida["resumen_capa_d"] = {
        "reps_tocadas": sorted(reps_tocadas),
        "atribuciones_corregidas": corregidas,
        "discrepancias": discrepancias,
        "triage": triage,
    }
    return salida


# --------------------------------------------------------------------------- #
# D3 — validador de quotes de aplicacion_erronea                               #
# --------------------------------------------------------------------------- #
def _norm_texto(s):
    """lowercase + sin acentos (normalización de harness) + espacios colapsados."""
    from harness import _strip_accents
    return " ".join(_strip_accents(str(s or "").lower()).split())


def _blob_nodo(nodo):
    """Contenido del nodo para la verificación de quote: label + valores de properties."""
    partes = [nodo.label or ""]
    partes += [str(v) for v in (nodo.properties or {}).values()]
    return _norm_texto(" ".join(partes))


def aplicar_d3(caso_json, run):
    """Aplica el validador D3 según la semántica pre-registrada del docstring del módulo.
    D3 NUNCA cambia causa_capa2: solo anota capa_d (verificación computable del quote;
    la lectura de alcance es semántica y queda para el humano del triage)."""
    index = _index_de(run)
    ids_kg = list(index.by_id.keys())
    salida = copy.deepcopy(caso_json)

    for rep in salida.get("repeticiones") or []:
        if rep.get("formato_invalido"):
            continue
        for atrib in rep.get("atribuciones") or []:
            if atrib.get("causa_capa2") != "aplicacion_erronea":
                continue
            portador, _ = _extraer_portador(atrib, ids_kg)
            if portador is None:
                atrib["capa_d"] = {"modulo": "D3", "accion": "sin_portador_extraible",
                                   "triage": True}
                continue
            quote = ((atrib.get("evidencia") or {}).get("nodo") or {}).get("quote") or ""
            verificado = _norm_texto(quote) in _blob_nodo(index.by_id[portador])
            if verificado:
                atrib["capa_d"] = {"modulo": "D3", "portador_id": portador,
                                   "quote_verificado": True}
            else:
                atrib["capa_d"] = {"modulo": "D3", "portador_id": portador,
                                   "quote_verificado": False,
                                   "accion": "quote_no_verificable", "triage": True}
    return salida


# --------------------------------------------------------------------------- #
# D5 — diligencia determinística de causas de ausencia                         #
# --------------------------------------------------------------------------- #
CAUSAS_GATILLO_D5 = ("completitud_kg", "alucinacion_agente")

# Regex CERRADA de extracción de literales (ver semántica D5 en el docstring):
RE_LITERALES_D5 = {
    "monto_usd": re.compile(r"(?i)(?:usd|us\$|u\$s)\s*\d+(?:\.\d{3})*"),
    "codigo_numerico": re.compile(r"\d{5,}"),
    # "al menos dos niveles": la base \d+\.\d+(\.\d+)* con descarte de un solo nivel
    # equivale a exigir al menos dos puntos ("1.1.2" sí; "1.1"/"3.9" no).
    "punto_normativo": re.compile(r"\d+\.\d+(?:\.\d+)+"),
    # decimales con COMA (coeficientes/alícuotas); guarda de límites por dígito adyacente.
    # Ver la nota "coeficiente_decimal" del docstring (motivación por mecanismo y limitación
    # simétrica: decimales con punto NO se extraen).
    "coeficiente_decimal": re.compile(r"(?<!\d)\d+,\d+(?!\d)"),
}


def _extraer_literales_d5(atrib):
    """Literales de evidencia.afirmacion.quote y del campo pata, en orden determinístico,
    deduplicados (por su forma normalizada)."""
    quote = ((atrib.get("evidencia") or {}).get("afirmacion") or {}).get("quote") or ""
    pata = atrib.get("pata") or ""
    literales, vistos = [], set()
    for texto in (quote, pata):
        for nombre in ("monto_usd", "codigo_numerico", "punto_normativo",
                       "coeficiente_decimal"):
            for m in RE_LITERALES_D5[nombre].finditer(texto):
                lit = m.group(0)
                clave = _norm_texto(lit)
                if clave not in vistos:
                    vistos.add(clave)
                    literales.append(lit)
    return literales


def _blob_nodo_d5(nodo):
    """Blob normalizado de id + label + properties (claves y valores), SIN provenances."""
    props = nodo.properties or {}
    partes = [nodo.id or "", nodo.label or ""]
    partes += [f"{k} {v}" for k, v in props.items()]
    return _norm_texto(" ".join(partes))


def _mejor_rank(d1):
    ranks = [c["rank"] for c in d1["consultas"] if c["rank"] is not None]
    return min(ranks) if ranks else None


def aplicar_d5(caso_json, run, trace_path=None, *,
               pregunta=None, consultas_agente=None, tokens_expuestos=None,
               outputs_completos=None):
    """Aplica la diligencia D5 según la semántica pre-registrada del docstring del módulo.
    D5 NUNCA cambia causa_capa2 ni jerarquías; solo anota (capa_d, o capa_d5 si ya hay
    capa_d de otro módulo)."""
    index = _index_de(run)

    if trace_path is not None:
        elem = json.load(open(trace_path))[0]
        pregunta = elem["trace"]["question"]
        consultas_agente = [s["input"]["consulta"] for s in elem["trace"]["steps"]
                            if s.get("tool") == "buscar_nodos"]
        tokens_expuestos = tokens_expuestos_de_trace(trace_path, index=index)
        outputs_completos = outputs_completos_de_trace(trace_path, index=index)
    elif (pregunta is None or consultas_agente is None or tokens_expuestos is None
          or outputs_completos is None):
        raise ValueError("falta trace_path, o la cuaterna pregunta/consultas_agente/"
                         "tokens_expuestos/outputs_completos")

    blobs = {n.id: _blob_nodo_d5(n) for n in index.kg.nodes}
    expuesto = {nid: any(nid in out for out in outputs_completos) for nid in blobs}
    cache_d1 = {}
    salida = copy.deepcopy(caso_json)

    for rep in salida.get("repeticiones") or []:
        if rep.get("formato_invalido"):
            continue
        for atrib in rep.get("atribuciones") or []:
            if atrib.get("causa_capa2") not in CAUSAS_GATILLO_D5:
                continue
            literales = _extraer_literales_d5(atrib)
            if not literales:
                anotacion = {"modulo": "D5", "accion": "sin_literales", "banderas": []}
            else:
                candidatos, descartados, banderas = [], 0, []
                vistos = set()
                for lit in literales:
                    lit_n = _norm_texto(lit)
                    for nid, blob in blobs.items():
                        if lit_n in blob and (lit, nid) not in vistos:
                            vistos.add((lit, nid))
                            candidatos.append((lit, nid))
                for lit, nid in candidatos:
                    if expuesto[nid]:
                        descartados += 1
                        continue
                    if nid not in cache_d1:
                        cache_d1[nid] = evaluar_alcanzabilidad(
                            nid, pregunta, consultas_agente, tokens_expuestos, index)
                    d1 = cache_d1[nid]
                    banderas.append({"literal": lit, "candidato_id": nid,
                                     "alcanzable": d1["alcanzable"],
                                     "mejor_rank": _mejor_rank(d1), "expuesto": False})
                anotacion = {"modulo": "D5", "literales": literales,
                             "candidatos_evaluados": len(candidatos),
                             "candidatos_expuestos_descartados": descartados,
                             "banderas": banderas, "triage": bool(banderas)}
            if "capa_d" in atrib:
                atrib["capa_d5"] = anotacion   # los módulos no se pisan
            else:
                atrib["capa_d"] = anotacion
    return salida


# --------------------------------------------------------------------------- #
# D6 — consistencia síntoma↔atribución (v6.1-D)                                #
# --------------------------------------------------------------------------- #
def _sintoma_de_trace(trace_path):
    """Extrae el síntoma del caso desde la traza post-hoc con el MISMO filtro que
    build_falla_context (verificador.py:547; filtro de reprobados en las líneas 583-591:
    `fallidos = [v for v in verifs if v.get("verdict") in ("falso", "no_soportado")]`
    sobre judge.step2.verificaciones). Devuelve (F, P):
      F = [{"enunciado", "central", "verdict"}] — claims reprobados del juez post-hoc;
      P = [pata, ...] — patas con cobertura "no_cubierta" (judge.step2.cobertura_patas).
    Solo lectura; no modifica nada del verificador."""
    elem = json.load(open(trace_path))[0]
    step2 = ((elem.get("judge") or {}).get("step2")) or {}
    verifs = step2.get("verificaciones") or []
    F = [{"enunciado": v.get("enunciado"), "central": bool(v.get("central")),
          "verdict": v.get("verdict")}
         for v in verifs if v.get("verdict") in ("falso", "no_soportado")]
    P = [c.get("pata") for c in (step2.get("cobertura_patas") or [])
         if c.get("cobertura") == "no_cubierta"]
    return F, P


def _mapear_claim(quote, F):
    """Mapa quote↔enunciados de F por substring normalizado, en ambas direcciones.
    Devuelve la lista de claims de F que mapean (en el orden de F)."""
    q = _norm_texto(quote)
    out = []
    for c in F:
        e = _norm_texto(c.get("enunciado"))
        if not q or not e:
            continue
        if q in e or e in q:
            out.append(c)
    return out


def aplicar_d6(caso_json, F, P):
    """Aplica la consistencia síntoma↔atribución (R6a/R6b) según la semántica pre-registrada
    del docstring del módulo. Degrada jerarquías SOLO en el caso autorizado (R6b mapeo
    solo-a-secundarios); nunca reescribe causas."""
    if F is None or P is None:
        raise ValueError("aplicar_d6 requiere F y P (listas, pueden ser vacías)")
    salida = copy.deepcopy(caso_json)
    sintoma_vacio = not F and not P

    for rep in salida.get("repeticiones") or []:
        if rep.get("formato_invalido"):
            continue
        for atrib in rep.get("atribuciones") or []:
            if sintoma_vacio:
                # R6a — rige sola cuando TODO el síntoma está vacío.
                if atrib.get("causa_capa2") not in ("sin_defecto",):
                    atrib["capa_d6"] = {"regla": "R6a", "accion": "atribucion_sin_sintoma"}
                continue
            if atrib.get("jerarquia") != "primaria":
                continue
            sintoma = atrib.get("sintoma_capa1")
            if sintoma == "context_recall":
                if not P and F:
                    atrib["capa_d6"] = {"regla": "R6b", "accion": "context_recall_sin_pata"}
                continue
            if sintoma not in ("noise_sensitivity", "faithfulness"):
                continue
            quote = ((atrib.get("evidencia") or {}).get("afirmacion") or {}).get("quote") or ""
            mapeados = _mapear_claim(quote, F)
            if not mapeados:
                atrib["capa_d6"] = {"regla": "R6b", "accion": "claim_no_mapeado"}
                continue
            if any(c.get("central") for c in mapeados):
                continue  # mapea a un central reprobado: jerarquía intacta
            atrib["jerarquia"] = "secundaria"
            atrib["capa_d6"] = {"regla": "R6b", "emision_llm": "primaria",
                                "decision_codigo": "secundaria",
                                "claim_mapeado": mapeados[0].get("enunciado")}
    return salida


# --------------------------------------------------------------------------- #
# D4 — política de triage a nivel caso                                         #
# --------------------------------------------------------------------------- #
def aplicar_d4(caso_json):
    """Aplica las reglas R1-R4 de triage según la semántica pre-registrada del docstring.
    Opera sobre el JSON ya pasado por D2 y D3 (exige voto_capa_d presente)."""
    salida = copy.deepcopy(caso_json)
    voto = salida.get("voto_capa_d")
    if voto is None:
        raise ValueError("aplicar_d4 requiere un JSON ya pasado por D2 (falta voto_capa_d)")

    motivos, flags = [], []

    def _sumar(motivo, flag):
        if motivo not in motivos:
            motivos.append(motivo)
        if flag not in flags:
            flags.append(flag)

    # R1 exoneracion_total — clave ganadora vacía (sin pares primarios)
    if voto.get("pares_primarios_ganadores") == []:
        _sumar("exoneracion_total",
               f"R1: voto_capa_d con mayoria de clave vacia ({voto.get('votos_ganadores')} votos sin primarias)")

    reps_validas = [(i + 1, r) for i, r in enumerate(salida.get("repeticiones") or [])
                    if not r.get("formato_invalido")]
    for n, rep in reps_validas:
        for j, atrib in enumerate(rep.get("atribuciones") or [], 1):
            # R2 aplicacion_erronea_presente (medida TEMPORAL: sesgo medido sin mitigar;
            # revisable con evidencia fresca)
            if atrib.get("causa_capa2") == "aplicacion_erronea":
                _sumar("aplicacion_erronea_bajo_revision",
                       f"R2: rep {n} atrib {j} ({atrib.get('jerarquia')}) causa aplicacion_erronea")
            for anot in (atrib.get("capa_d") or {}, atrib.get("capa_d5") or {}):
                if not anot:
                    continue
                if anot.get("modulo") == "D5":
                    # R5 — banderas de D5 (candidatos no considerados): D5 SÍ decidió
                    if anot.get("banderas"):
                        _sumar("posible_portador_no_considerado",
                               f"R5: rep {n} atrib {j} — {len(anot['banderas'])} bandera(s) D5")
                elif anot.get("triage") is True:
                    # R3 propagacion — módulos SIN decisión (D2/D3)
                    _sumar("modulo_deterministico_sin_decision",
                           f"R3: rep {n} atrib {j} — {anot.get('modulo')}/{anot.get('accion')}")
            # R6 — consistencia síntoma↔atribución (D6, v6.1-D)
            d6 = atrib.get("capa_d6") or {}
            if d6.get("accion") == "atribucion_sin_sintoma":
                _sumar("atribucion_sin_sintoma",
                       f"R6a: rep {n} atrib {j} — atribución con síntoma vacío")
            elif d6.get("accion") in ("claim_no_mapeado", "context_recall_sin_pata"):
                _sumar("atribucion_no_verificable",
                       f"R6b: rep {n} atrib {j} — {d6.get('accion')}")

    # R4 voto_dividido
    if voto.get("flag_voto_dividido") is True:
        _sumar("voto_dividido", "R4: voto_capa_d.flag_voto_dividido = true")

    salida["triage_capa_d"] = {"triage": bool(motivos), "motivos": motivos, "flags": flags}
    return salida


# --------------------------------------------------------------------------- #
# Punto de entrada compuesto                                                   #
# --------------------------------------------------------------------------- #
VERSION_CAPA = "v6.1-D(2026-07)"


def aplicar_capa(caso_json, run, trace_path=None, *,
                 pregunta=None, consultas_agente=None, tokens_expuestos=None,
                 outputs_completos=None, sintoma_F=None, sintoma_P=None):
    """Compuesto v6.1-D: D2 → D3 → D5 → D6 → recomputo final del voto → D4. Agrega
    version_capa. Misma inyección de insumos de D1 que aplicar_d2 (tests sin disco; D5 suma
    outputs_completos; D6 suma sintoma_F/sintoma_P — con trace_path salen de
    _sintoma_de_trace). El voto previo a D6 queda como voto_pre_d6 (informativo); el voto
    original del verificador queda intacto."""
    index = _index_de(run)
    if trace_path is not None:
        sintoma_F, sintoma_P = _sintoma_de_trace(trace_path)
    elif sintoma_F is None or sintoma_P is None:
        raise ValueError("falta trace_path, o la dupla sintoma_F/sintoma_P (listas)")
    salida = aplicar_d2(caso_json, index, trace_path=trace_path, pregunta=pregunta,
                        consultas_agente=consultas_agente, tokens_expuestos=tokens_expuestos)
    salida = aplicar_d3(salida, index)
    salida = aplicar_d5(salida, index, trace_path=trace_path, pregunta=pregunta,
                        consultas_agente=consultas_agente, tokens_expuestos=tokens_expuestos,
                        outputs_completos=outputs_completos)
    salida = aplicar_d6(salida, sintoma_F, sintoma_P)
    salida["voto_pre_d6"] = salida["voto_capa_d"]
    salida["voto_capa_d"] = _recomputar_voto(salida.get("repeticiones") or [])
    salida = aplicar_d4(salida)
    salida["version_capa"] = VERSION_CAPA
    return salida


# --------------------------------------------------------------------------- #
# CLI                                                                          #
# --------------------------------------------------------------------------- #
def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Capa determinística del verificador — aplicar_capa (D2 → D3 → D4)")
    ap.add_argument("--caso", required=True, help="path al JSON del caso del gate")
    ap.add_argument("--run", required=True, help="clave del run (p. ej. run_3)")
    ap.add_argument("--trace", required=True, help="path a la traza post-hoc del caso")
    ap.add_argument("--out", required=True, help="path del JSON de salida")
    args = ap.parse_args(argv)

    caso = json.load(open(args.caso))
    salida = aplicar_capa(caso, args.run, trace_path=args.trace)
    with open(args.out, "w") as f:
        json.dump(salida, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": args.out,
                      "version_capa": salida["version_capa"],
                      "resumen_capa_d": salida["resumen_capa_d"],
                      "triage_capa_d": salida["triage_capa_d"],
                      "voto_capa_d": salida["voto_capa_d"]},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
