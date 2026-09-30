"""
u_umbral_u2.py — U-UMBRAL, etapa U2: muestra de `limita`, trazas y
dimensionamientos para los dos ejes (USD 0).

Mandato: docs/mandatos/UUMBRAL_investigacion.md (firmado el 30/09/2026), con las
precisiones de la autora al aprobar U1 (commit e81ed69). Solo lectura: no llama
a ninguna API, no usa Neo4j, no edita nada fuera del directorio de salida.
Reutiliza por import las regex y el prototipo de u_umbral_u1.py (c14, P6,
D-REL/A-REL, normalización D-N1) sin cambiarlos, e importa `e0_tablas.py` sin
editarlo.

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/u_umbral_u2.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/u_umbral_u2.py --salida DIR

Escribe muestra_limita_30.csv, u2_muestra_trazas.json y u2_muestra_trazas.md.
Salida determinística (sin fechas ni rutas absolutas): la doble corrida tiene que
dar archivos idénticos byte a byte. La planilla se genera y se sella; el script
no la lee para juzgarla.

DECLARACIONES (fijadas antes de aplicar; se repiten en el .md):

D-SORTEO · Medición 4. Población: aristas con relation = "limita" de
  KG-Tanda0-Desarrollo-r1, en el orden de `edges` del kg.json, ordenadas con
  sort estable por la clave (source, target). Se comprueba que no hay pares
  (source, target) repetidos. Sorteo: random.Random(20260930).sample(range(N), 30)
  sobre los índices de esa lista ordenada, sin reemplazo (Python del .venv del
  repo, 3.10). Las filas de la planilla van en el orden del sorteo, con su
  índice en la lista ordenada. Texto de E0: el `texto` propio y la `herencia`
  de cada chunk_id de las procedencias de la arista, en orden de aparición.

D-C14 · Regex de cuantía: la de U1 (comando [c14] del tablero tal como está
  escrito), sin cambios, importada de u_umbral_u1.VARIANTES["c14"].

D-C14PAR · Variante con nombre propio «c14_par», declarada antes de aplicarla
  (precisión 1 de la autora): idéntica a c14 salvo en el plazo, que admite
  entre el número y la unidad un número entre paréntesis, en cifras o en
  letras de la lista LETRAS de U1 («2 (dos) años», «diez (10) años»). Sin
  paréntesis, exige el mismo espacio que c14. c14_eur de U1 se reporta solo
  como variante informativa.

D-CRIT · Medición 5. Un criterio de preguntas_ev2_fidelidad.json tiene cuantía
  según una regex si la regex encuentra algo en su `criterio` o en su
  `cita_textual`. El diagnóstico se corre sobre los criterios con cuantía según
  c14 o según c14_par; cada fila dice con cuál de las dos (o las dos).

D-VALOR · Valor de un criterio: los triples del prototipo P6 de U1
  (extraer_p6) sobre `criterio` y sobre `cita_textual` (unión), más los
  «literales»: los tramos que encuentra c14_par en esos dos textos y que tienen
  al menos un dígito, normalizados con D-N1. Un criterio con cuantía sin
  triples ni literales queda como «valor no extraíble» y no se diagnostica.

D-CONTIENE · Un texto contiene el valor si sus triples P6 comparten al menos
  uno con los del criterio, o si algún literal del criterio es subcadena del
  texto normalizado con D-N1. Un nodo contiene el valor si lo contiene su
  `descripcion`, su `umbral` o su `plazo`. Se excluyen TextoOrdenado, Sujeto y
  Comunicacion.

D-ANCLA · Un nodo está en el ancla de la pregunta («to:punto») si alguna de
  sus procedencias tiene ese `to` y un `punto` igual al del ancla o que empieza
  con el del ancla seguido de «.» (puntos descendientes).

D-RECIBIDO · En una traza base (C3, `ev2_c3_dev_mem`; C4, `ev2_c4_dev_neo4j`),
  un nodo fue recibido si su id aparece en algún resultado de `buscar_nodos`,
  como vecino en algún resultado de `ver_vecinos` (salientes o entrantes) o
  como id de una salida de `ver_nodo` sin error (`steps_full`).

D-VISIBLE · El valor fue visible para el agente desde un nodo del ancla si ese
  nodo aparece en un resultado de `buscar_nodos` cuyo `label` o
  `resumen_propiedades` contiene el valor (D-CONTIENE), o como vecino en
  `ver_vecinos` con `vecino_label` que lo contiene, o si el agente le hizo
  `ver_nodo` (la salida trae las properties completas).

D-RESPUESTA · El valor está en la respuesta si `trace.final_json.respuesta`
  (o `trace.final_raw` si no hay final_json) lo contiene según D-CONTIENE.
  Es un control léxico: no dice si la respuesta cumple el criterio.

D-CLASE · Cadena, en orden: «grafo» si ningún nodo del ancla contiene el
  valor; «búsqueda» si hay nodos del ancla con el valor y el agente no recibió
  ninguno; «navegación» si recibió alguno pero el valor no le fue visible;
  «visible» en otro caso. Cruce con D-RESPUESTA: visible y en la respuesta →
  «llega»; visible y no en la respuesta → «generación»; grafo, búsqueda o
  navegación con el valor en la respuesta → «en la respuesta por otra vía»;
  sin el valor en la respuesta → la clase de la cadena. Es un diagnóstico por
  reglas sobre material de desarrollo, no un resultado sobre EV2.

D-TABLA-1.2 · Demostración puntual (precisión 2.ii), no un verificador
  general: para cada Restriccion con umbral anclada en cap::1.2, la clase del
  sujeto se toma de su descripción («restantes entidades» → columna
  «Restantes entidades», si no «bancos» → columna «Bancos»), y el monto
  esperado es el de esa columna en la tabla de e0_tablas asignada a cap::1.2
  (cap::tabla000: fila de encabezados y última fila de cifras). Se compara con
  el monto del umbral (primer número con puntos o dígitos del campo).

D-ESTIM · Dimensionamiento del llenado por un modelo (decisión 6):
  ESTIMACIÓN NO VERIFICADA. Subconjuntos: nodos de los cuatro tipos con
  cuantía según c14, y de ellos los sin campo. Una llamada por chunk distinto
  del subconjunto. Tokens de entrada variables = (caracteres del texto propio
  y heredado de cada chunk + caracteres de las descripciones del subconjunto)
  / 3,471 (ratio de prosa de INFORME_E1_FASEA.md:141). Supuestos NO
  VERIFICADOS: prompt fijo de 1.500 tokens (escritura de caché en la primera
  llamada, lectura en las demás) y 60 tokens de salida por nodo. Tarifas
  USD/MTok: entrada 1,00; salida 5,00; escritura de caché 1,25; lectura 0,10
  (runner_faseB_e1.py:41). Referencia aparte: USD 0,0166 por unidad de E1+E3
  (docs/laudo_release_r2_pipeline.md:46) por el número de chunks.

D-REL-DIM · Dimensionamiento de los umbrales relacionales (precisión 2.iv):
  nodos de los cuatro tipos con cuantía según c14 en los que dispara D-REL o
  A-REL de U1 (u_umbral_u1.RE_REL) o la regla de «equivalente»; se cuentan por
  forma (base con «de/del/sobre», «veces» + artículo, «equivalente» antes de un
  monto), por tipo, con y sin campo.

D-COB · Cobertura de aristas de los demás portadores de valor (eje de
  esquema), por grafo: Obligacion con `plazo` y sin arista saliente `regula`
  ni `condiciona` (las Obligacion→Operacion del prefijo); Obligacion con
  cuantía según c14, sin campo, y sin esas aristas; Excepcion con cuantía según
  c14 y sin `exceptua` ni `exceptua_obligacion` saliente. Declarada antes de
  computarla, después de la corrida de prueba del resto de U2.

AGREGADOS TRAS LA CORRIDA DE PRUEBA (30/09/2026; rotulados como posteriores; la
medición 5 se reporta con y sin ellos):

A-P6PAR · En la corrida de prueba, EV2F-015#3 («180 días corridos», ancla
  ext:3.13.1) salió «grafo», pero el ancla tiene el nodo
  Condicion_plazo_minimo_180_dias… con «180 (ciento ochenta) días corridos»:
  P6 no reconoce un número en letras de varias palabras entre paréntesis. En
  U2, y solo para el valor de la medición 5, se suman a los triples P6 dos
  formas de plazo: cifra seguida de paréntesis sin dígitos (hasta 40
  caracteres) y unidad («180 (ciento ochenta) días»), y cifra entre paréntesis
  seguida de unidad («ciento ochenta (180) días»). El prototipo P6 de U1 no se
  cambia.
"""

from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import json
import random
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import u_umbral_u1 as u1  # noqa: E402 — solo import; no se modifica

KG_DEV = u1.GRAFOS[0]
assert KG_DEV[0] == "desarrollo"
SEMILLA = 20260930
N_MUESTRA = 30
PREGUNTAS = "data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json"
TRAZAS = {"C3": "data/experiment/ev2_tanda0/trazas/ev2_c3_dev_mem",
          "C4": "data/experiment/ev2_tanda0/trazas/ev2_c4_dev_neo4j"}
COL_VACIA = "el destino es el objeto del tope (sí / no / no decidible)"
RATIO_CHARS_TOKEN = 3.471
PROMPT_FIJO_TOK = 1500
SALIDA_TOK_POR_NODO = 60
P_IN, P_OUT, P_CW, P_CR = 1.00, 5.00, 1.25, 0.10
REF_E1E3_POR_UNIDAD = 0.0166

C14 = u1.VARIANTES["c14"]
C14_PAR = dict(C14)
C14_PAR["plazo"] = re.compile(
    r"\b" + u1._NUM_C14 + r"(?:\s+|\s*\((?:\d+|" + u1._ALT_LETRAS + r")\)\s*)" + u1._UNID + r"\b"
    r"|d[ií]as\s+(?:h[aá]biles|corridos)", re.I)
REGEX_CRIT = {"c14": C14, "c14_par": C14_PAR, "c14_eur": u1.VARIANTES["c14_eur"]}


def cargar(ruta: str):
    return json.load(open(REPO / ruta, encoding="utf-8"))


def texto_e0(chunks: dict, cids: list[str]) -> tuple[str, str]:
    propio, heredado = [], []
    for c in cids:
        ch = chunks.get(c)
        if ch is None:
            propio.append(f"[{c}] (chunk no encontrado en E0)")
            continue
        propio.append(f"[{c}] {ch['texto']}")
        her = " || ".join(h.get("texto", "") for h in ch.get("herencia") or [])
        heredado.append(f"[{c}] {her}")
    return "\n\n".join(propio), "\n\n".join(heredado)


# ------------------------------------------------------------------ medición 4

def medicion_4(kg: dict, chunks: dict) -> tuple[dict, str]:
    by_id = {n["id"]: n for n in kg["nodes"]}
    lim = [e for e in kg["edges"] if e["relation"] == "limita"]
    lista = sorted(lim, key=lambda e: (e["source"], e["target"]))
    pares = collections.Counter((e["source"], e["target"]) for e in lista)
    repetidos = sum(1 for v in pares.values() if v > 1)
    if repetidos:
        raise SystemExit(f"D-SORTEO: {repetidos} pares (source, target) repetidos. Se frena.")
    idx = random.Random(SEMILLA).sample(range(len(lista)), N_MUESTRA)
    buf = io.StringIO()
    w = csv.writer(buf, quoting=csv.QUOTE_ALL, lineterminator="\n")
    cab = ["n_sorteo", "indice_en_lista_ordenada", "restriccion_id", "restriccion_label",
           "restriccion_tipo", "restriccion_descripcion", "restriccion_umbral",
           "operacion_id", "operacion_label", "operacion_descripcion", "chunk_ids",
           "texto_e0_propio", "texto_e0_heredado", COL_VACIA]
    w.writerow(cab)
    for k, i in enumerate(idx, start=1):
        e = lista[i]
        s, t = by_id.get(e["source"], {}), by_id.get(e["target"], {})
        cids = []
        for pv in e.get("provenances") or ([e["provenance"]] if e.get("provenance") else []):
            c = pv.get("chunk_id")
            if c and c not in cids:
                cids.append(c)
        prop_txt, her_txt = texto_e0(chunks, cids)
        w.writerow([k, i, e["source"], s.get("label", ""), u1.props(s).get("tipo", ""),
                    u1.props(s).get("descripcion", ""), u1.props(s).get("umbral", "") or "",
                    e["target"], t.get("label", ""), u1.props(t).get("descripcion", ""),
                    " | ".join(cids), prop_txt, her_txt, ""])
    info = {"poblacion": len(lista), "pares_repetidos": repetidos, "semilla": SEMILLA,
            "n": N_MUESTRA, "indices_sorteados": idx, "columnas": cab,
            "python": sys.version.split()[0]}
    return info, buf.getvalue()


# ------------------------------------------------------------------ medición 5

_cache_trip: dict[str, set] = {}
_cache_norm: dict[str, str] = {}


def norm(texto: str) -> str:
    if texto not in _cache_norm:
        _cache_norm[texto] = u1.norm1(texto)
    return _cache_norm[texto]


# A-P6PAR (agregado tras la corrida de prueba de U2; ver el docstring)
_UNID_P6 = r"(d[ií]as?|mes(?:es)?|a[ñn]os?|horas?|semanas?)\b"
RE_P6PAR = [
    re.compile(r"(?<![\w.,])(\d+)\s*\([^()\d]{1,40}\)\s*" + _UNID_P6, re.I),
    re.compile(r"\((\d+)\)\s*" + _UNID_P6, re.I),
]
USAR_A_P6PAR = {"activo": True}


def triples(texto) -> set:
    t = u1.nfc(texto)
    clave = (USAR_A_P6PAR["activo"], t)
    if clave not in _cache_trip:
        tr = set(map(tuple, u1.extraer_p6(t)["triples"]))
        if USAR_A_P6PAR["activo"]:
            for p in RE_P6PAR:
                for m in p.finditer(t):
                    unidad = next(c for r, c in u1.UNIDAD_T if r.match(m.group(2)))
                    tr.add(("plazo", u1.dec_str(u1.parse_num(m.group(1))), unidad))
        _cache_trip[clave] = tr
    return _cache_trip[clave]


def contiene(textos: list, trip: set, lits: list[str]) -> str | None:
    tt = set()
    for x in textos:
        if x:
            tt |= triples(x)
    if tt & trip:
        return "triple"
    nt = [norm(x) for x in textos if x]
    for lit in lits:
        if any(lit in x for x in nt):
            return "literal"
    return None


def textos_nodo(n: dict) -> list:
    p = u1.props(n)
    return [p.get("descripcion"), u1.campo(n, "umbral"), u1.campo(n, "plazo")]


def en_ancla(n: dict, to: str, punto: str) -> bool:
    for pv in u1.provs(n):
        if pv.get("to") != to:
            continue
        p = str(pv.get("punto") or "")
        if p == punto or p.startswith(punto + "."):
            return True
    return False


def leer_traza(ruta: Path) -> dict:
    t = json.load(open(ruta, encoding="utf-8"))
    busq, vec, vn = collections.defaultdict(list), collections.defaultdict(list), set()
    for s in t.get("steps_full") or []:
        o = s.get("output")
        if not isinstance(o, dict):
            continue
        if s["tool"] == "buscar_nodos":
            for r in o.get("resultados") or []:
                busq[r["id"]].append([r.get("label") or "", r.get("resumen_propiedades") or ""])
        elif s["tool"] == "ver_vecinos":
            for lado in ("salientes", "entrantes"):
                for v in o.get(lado) or []:
                    vec[v["vecino_id"]].append(v.get("vecino_label") or "")
        elif s["tool"] == "ver_nodo":
            if "error" not in o and o.get("id"):
                vn.add(o["id"])
    tr = t.get("trace") or {}
    fj = tr.get("final_json") or {}
    resp = fj.get("respuesta") if isinstance(fj, dict) and fj.get("respuesta") else (tr.get("final_raw") or "")
    return {"busq": busq, "vec": vec, "ver_nodo": vn, "respuesta": resp,
            "hit_tool_limit": tr.get("hit_tool_limit"), "tool_calls_used": tr.get("tool_calls_used")}


def medicion_5(kg: dict) -> dict:
    preg = cargar(PREGUNTAS)["preguntas"]
    nodos = [n for n in kg["nodes"] if n["type"] not in u1.TIPOS_NO_CONTENIDO]
    trazas = {}
    for celda, d in TRAZAS.items():
        trazas[celda] = {q["id"]: leer_traza(REPO / d / f"{q['id']}.json") for q in preg}
    filas = []
    n_crit = 0
    for q in preg:
        to_a, punto_a = q["gold"]["ancla"][0].split(":", 1)
        for i, c in enumerate(q["gold"]["criterios"]):
            n_crit += 1
            txts = [c.get("criterio") or "", c.get("cita_textual") or ""]
            flags = {r: any(u1.spans_cuantia(u1.nfc(x), pats) for x in txts)
                     for r, pats in REGEX_CRIT.items()}
            if not (flags["c14"] or flags["c14_par"]):
                if flags["c14_eur"]:
                    filas.append({"qid": q["id"], "criterio_idx": i, "regex": flags,
                                  "solo_c14_eur": True})
                continue
            trip = set()
            for x in txts:
                trip |= triples(x)
            lits = []
            for x in txts:
                xn = u1.nfc(x)
                for s, e, _ in u1.spans_cuantia(xn, C14_PAR):
                    tramo = xn[s:e]
                    if re.search(r"\d", tramo):
                        ln = u1.norm1(tramo)
                        if ln not in lits:
                            lits.append(ln)
            fila = {"qid": q["id"], "criterio_idx": i, "to": to_a, "ancla": q["gold"]["ancla"][0],
                    "criterio": c.get("criterio"), "cita_textual": c.get("cita_textual"),
                    "regex": flags, "triples": sorted(trip), "literales": lits}
            if not trip and not lits:
                fila["clase"] = {"C3": "valor no extraíble", "C4": "valor no extraíble"}
                filas.append(fila)
                continue
            con_valor = [n for n in nodos if contiene(textos_nodo(n), trip, lits)]
            ancla = [n for n in con_valor if en_ancla(n, to_a, punto_a)]
            fila["nodos_ancla_con_valor"] = sorted(n["id"] for n in ancla)
            fila["n_nodos_fuera_del_ancla_con_valor"] = len(con_valor) - len(ancla)
            fila["nodos_ancla_con_valor_por_tipo"] = u1.contar(n["type"] for n in ancla)
            fila["celdas"] = {}
            fila["clase"] = {}
            for celda in TRAZAS:
                tz = trazas[celda][q["id"]]
                ids = {n["id"] for n in ancla}
                rec_b = sorted(ids & set(tz["busq"]))
                rec_v = sorted(ids & set(tz["vec"]))
                vn = sorted(ids & tz["ver_nodo"])
                recibidos = set(rec_b) | set(rec_v) | set(vn)
                vis = set()
                for nid in rec_b:
                    if any(contiene([lab, res], trip, lits) for lab, res in tz["busq"][nid]):
                        vis.add(nid)
                for nid in rec_v:
                    if any(contiene([lab], trip, lits) for lab in tz["vec"][nid]):
                        vis.add(nid)
                vis |= set(vn)
                en_resp = bool(contiene([tz["respuesta"]], trip, lits))
                if not ancla:
                    cadena = "grafo"
                elif not recibidos:
                    cadena = "búsqueda"
                elif not vis:
                    cadena = "navegación"
                else:
                    cadena = "visible"
                if cadena == "visible":
                    clase = "llega" if en_resp else "generación"
                else:
                    clase = "en la respuesta por otra vía" if en_resp else cadena
                fila["celdas"][celda] = {"recibidos_buscar_nodos": rec_b, "recibidos_ver_vecinos": rec_v,
                                         "ver_nodo": vn, "valor_visible_desde": sorted(vis),
                                         "valor_en_respuesta": en_resp, "cadena": cadena,
                                         "hit_tool_limit": tz["hit_tool_limit"]}
                fila["clase"][celda] = clase
            filas.append(fila)

    def resumen(pred):
        out = {}
        for celda in TRAZAS:
            out[celda] = u1.contar(f["clase"][celda] for f in filas
                                   if not f.get("solo_c14_eur") and pred(f))
        return out

    diag = [f for f in filas if not f.get("solo_c14_eur")]
    return {
        "preguntas": len(preg), "criterios": n_crit,
        "criterios_con_cuantia": {
            "c14": sum(1 for f in diag if f["regex"]["c14"]),
            "c14_par": sum(1 for f in diag if f["regex"]["c14_par"]),
            "solo_c14_par": sum(1 for f in diag if f["regex"]["c14_par"] and not f["regex"]["c14"]),
            "c14_eur_informativo": sum(1 for f in filas if f["regex"]["c14_eur"]),
            "solo_c14_eur_informativo": sum(1 for f in filas if f.get("solo_c14_eur")),
            "preguntas_con_algun_criterio_c14": len({f["qid"] for f in diag if f["regex"]["c14"]}),
        },
        "clases_c14": resumen(lambda f: f["regex"]["c14"]),
        "clases_solo_c14_par": resumen(lambda f: not f["regex"]["c14"]),
        "filas": filas,
    }


# ------------------------------------------------------------------ cap::1.2 contra la tabla

def demostracion_cap_1_2(kg: dict, chunks_cap: list) -> dict:
    sys.path.insert(0, str(REPO / u1.E0_TABLAS_DIR))
    import e0_tablas  # noqa: E402 — se importa sin editar
    man = cargar(u1.MANIFIESTO)
    pdf = next(t["pdf"] for t in man["tos"] if t["id"] == "cap")
    art = e0_tablas.parsear_to(REPO / pdf, "cap")
    asig = u1.asignar_tablas({"cap": art}, {"cap": chunks_cap})["por_chunk"].get("cap::1.2", [])
    tid = asig[0]["tabla"] if asig else None
    tabla = next((t for t in art["tablas_logicas"] if t["id"] == tid), None)
    if tabla is None:
        return {"tabla": None}
    filas = tabla["segmentos"][0]["filas"]
    cab = [u1.norm1(c or "") for c in filas[0]]
    cifras = [(c or "").strip() for c in filas[-1]]
    col = {}
    for h, v in zip(cab, cifras):
        if h.startswith("restantes entidades"):
            col["restantes"] = v
        elif h.startswith("bancos"):
            col["bancos"] = v
    out = []
    for n in kg["nodes"]:
        if n["type"] != "Restriccion" or "cap::1.2" not in u1.chunk_ids(n) or not u1.campo(n, "umbral"):
            continue
        d = u1.norm1(u1.props(n).get("descripcion"))
        clase = "restantes" if "restantes entidades" in d else ("bancos" if "bancos" in d else None)
        m = re.search(r"\d[\d.]*", u1.campo(n, "umbral"))
        monto = m.group(0) if m else None
        esperado = col.get(clase)
        out.append({"id": n["id"], "clase_por_descripcion": clase, "umbral": u1.campo(n, "umbral"),
                    "monto_umbral": monto, "monto_tabla": esperado,
                    "coincide_con_tabla": monto == esperado})
    return {"tabla": tid, "encabezados": cab, "cifras": cifras, "columnas": col, "restricciones": out}


# ------------------------------------------------------------------ dimensionamientos

def dim_relacionales(grafos: dict) -> dict:
    out = {}
    for g, k in grafos.items():
        c = collections.defaultdict(collections.Counter)
        for n in k["nodes"]:
            if n["type"] not in u1.TIPOS_CUANTIA:
                continue
            d = u1.nfc(u1.props(n).get("descripcion"))
            if not u1.spans_cuantia(d, C14):
                continue
            base = bool(u1.RE_REL[0].search(d))
            veces = bool(u1.RE_REL[1].search(d))
            equiv = False
            for tipo, p in u1.P6:
                if tipo.startswith("monto"):
                    for m in p.finditer(d):
                        if u1.RE_EQUIV.search(d[max(0, m.start() - 40):m.start()]):
                            equiv = True
            rel = base or veces or equiv
            est = "con_campo" if u1.con_campo(n) else "sin_campo"
            x = c[n["type"]]
            x["con_cuantia"] += 1
            x["relacional"] += rel
            x["relacional_" + est] += rel
            x["forma_base_de_del_sobre"] += base
            x["forma_veces_articulo"] += veces
            x["forma_equivalente_monto"] += equiv
        tot = collections.Counter()
        for x in c.values():
            tot.update(x)
        out[g] = {"por_tipo": {t: dict(sorted(c[t].items())) for t in u1.TIPOS_CUANTIA if t in c},
                  "total": dict(sorted(tot.items()))}
    return out


def cobertura_otros(grafos: dict) -> dict:
    out = {}
    for g, k in grafos.items():
        sal = collections.defaultdict(set)
        for e in k["edges"]:
            sal[e["source"]].add(e["relation"])
        c = collections.Counter()
        for n in k["nodes"]:
            cq = bool(u1.spans_cuantia(u1.nfc(u1.props(n).get("descripcion")), C14))
            if n["type"] == "Obligacion":
                sin_op = not (sal[n["id"]] & {"regula", "condiciona"})
                if u1.campo(n, "plazo"):
                    c["obligacion_con_plazo"] += 1
                    c["obligacion_con_plazo_sin_regula_ni_condiciona"] += sin_op
                if cq and not u1.con_campo(n):
                    c["obligacion_con_cuantia_sin_campo"] += 1
                    c["obligacion_con_cuantia_sin_campo_sin_regula_ni_condiciona"] += sin_op
            elif n["type"] == "Excepcion" and cq:
                c["excepcion_con_cuantia"] += 1
                c["excepcion_con_cuantia_sin_exceptua"] += not (sal[n["id"]] & {"exceptua", "exceptua_obligacion"})
        out[g] = dict(sorted(c.items()))
    return out


def dim_modelo(grafos: dict, chunks: dict) -> dict:
    out = {}
    for g, k in grafos.items():
        res = {}
        for sub in ("con_cuantia", "con_cuantia_sin_campo"):
            ns = [n for n in k["nodes"] if n["type"] in u1.TIPOS_CUANTIA
                  and u1.spans_cuantia(u1.nfc(u1.props(n).get("descripcion")), C14)
                  and (sub == "con_cuantia" or not u1.con_campo(n))]
            cids = sorted({c for n in ns for c in u1.chunk_ids(n) if c in chunks})
            ch_chars = sum(len(chunks[c]["texto"]) + sum(len(h.get("texto", "")) for h in chunks[c].get("herencia") or [])
                           for c in cids)
            d_chars = sum(len(str(u1.props(n).get("descripcion") or "")) for n in ns)
            tok_var = (ch_chars + d_chars) / RATIO_CHARS_TOKEN
            llamadas = len(cids)
            tok_out = SALIDA_TOK_POR_NODO * len(ns)
            costo = (tok_var * P_IN + PROMPT_FIJO_TOK * P_CW + PROMPT_FIJO_TOK * max(0, llamadas - 1) * P_CR
                     + tok_out * P_OUT) / 1e6
            res[sub] = {"nodos": len(ns), "chunks_llamadas": llamadas, "chars_chunks": ch_chars,
                        "chars_descripciones": d_chars, "tokens_entrada_variables": round(tok_var),
                        "tokens_salida": tok_out, "costo_usd_estimado_NO_VERIFICADO": round(costo, 4),
                        "referencia_e1e3_usd": round(REF_E1E3_POR_UNIDAD * llamadas, 4)}
        out[g] = res
    return out


# ------------------------------------------------------------------ md

def escribir_md(res: dict, sha_csv: str) -> str:
    T = u1.tabla
    L = []
    cmd = "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/u_umbral_u2.py"
    L.append("# U-UMBRAL · U2 — Muestra de `limita`, trazas y dimensionamientos\n")
    L.append("Mandato: `docs/mandatos/UUMBRAL_investigacion.md` (firmado el 30/09/2026), con las precisiones "
             "de la autora al aprobar U1 (`e81ed69`). USD 0: sin API y sin Neo4j. EV2 y las trazas son "
             "material de desarrollo: la medición 5 es un diagnóstico, no un resultado (principio 7).\n")
    L.append(f"Comando que reproduce este archivo, `u2_muestra_trazas.json` y `muestra_limita_30.csv`:\n\n```\n{cmd}\n```\n")
    L.append("## Entradas\n")
    L.append(T([[x["nombre"], f"`{x['ruta']}`", f"`{x['sha256'][:16]}…`"] for x in res["entradas"]["grafos"]],
               ["Grafo", "Ruta", "sha256"]))
    L.append(f"\nPreguntas: `{PREGUNTAS}` (sha256 `{res['entradas']['preguntas_sha256'][:16]}…`). Trazas base: "
             f"`{TRAZAS['C3']}/` y `{TRAZAS['C4']}/` (40 cada una; sha256 del conjunto, concatenando los sha "
             f"de los archivos en orden: C3 `{res['entradas']['trazas_sha256']['C3'][:16]}…`, C4 "
             f"`{res['entradas']['trazas_sha256']['C4'][:16]}…`). E0: `{u1.E0_DIR}`.\n")
    L.append("## Declaraciones previas a la medición\n")
    for k, v in res["declaraciones"].items():
        L.append(f"- **{k}.** {v}")
    L.append("\n### Agregados tras la corrida de prueba (rotulados como posteriores)\n")
    for k, v in res["agregados_tras_corrida_de_prueba"].items():
        L.append(f"- **{k}.** {v}")
    L.append("")

    m4 = res["medicion_4"]
    L.append("## Medición 4 — Muestra de 30 aristas `limita`\n")
    L.append(f"Población: {m4['poblacion']} aristas `limita` de KG-Tanda0-Desarrollo-r1; pares (source, target) "
             f"repetidos: {m4['pares_repetidos']}. Semilla {m4['semilla']}, n = {m4['n']}, Python {m4['python']}. "
             f"Índices sorteados (en la lista ordenada): {m4['indices_sorteados']}.\n")
    L.append(f"Planilla `muestra_limita_30.csv`: {m4['n']} filas más la de encabezados; sha256 `{sha_csv}`. "
             f"La columna «{COL_VACIA}» va vacía. Nadie la lee en esta unidad; quién lee lo decide la autora "
             f"(checklist P15 y Q12).\n")

    m5 = res["medicion_5"]
    cc = m5["criterios_con_cuantia"]
    L.append("## Medición 5 — Dónde se pierde el valor en las trazas (diagnóstico)\n")
    L.append(f"Criterios: {m5['criterios']} en {m5['preguntas']} preguntas. Con cuantía según c14: **{cc['c14']}** "
             f"(en {cc['preguntas_con_algun_criterio_c14']} preguntas); según c14_par: {cc['c14_par']} "
             f"({cc['solo_c14_par']} solo por c14_par). Informativo, c14_eur: {cc['c14_eur_informativo']} "
             f"({cc['solo_c14_eur_informativo']} solo por c14_eur).\n")
    clases = ["llega", "generación", "navegación", "búsqueda", "grafo", "en la respuesta por otra vía",
              "valor no extraíble"]
    filas = []
    for nombre, clave in (("c14", "clases_c14"), ("solo c14_par", "clases_solo_c14_par")):
        for celda in TRAZAS:
            r = m5[clave][celda]
            filas.append([nombre, celda] + [r.get(c, 0) for c in clases] + [sum(r.values())])
    L.append(T(filas, ["Criterios", "Celda"] + clases + ["Total"]))
    ms = res["medicion_5_sin_A_P6PAR"]
    L.append("\nLa misma tabla sin A-P6PAR (solo con lo declarado antes de la corrida de prueba):\n")
    filas = []
    for nombre, clave in (("c14", "clases_c14"), ("solo c14_par", "clases_solo_c14_par")):
        for celda in TRAZAS:
            r = ms[clave][celda]
            filas.append([nombre, celda] + [r.get(c, 0) for c in clases] + [sum(r.values())])
    L.append(T(filas, ["Criterios", "Celda"] + clases + ["Total"]))
    L.append("\nPor criterio (valor = triples P6 o literales; «ancla» = nodos del ancla con el valor; fuera = "
             "nodos con el valor fuera del ancla):\n")
    filas = []
    for f in m5["filas"]:
        if f.get("solo_c14_eur"):
            continue
        val = "; ".join(f"{a}:{b} {c}" for a, b, c in f["triples"]) or "; ".join(f["literales"])
        rg = "c14" if f["regex"]["c14"] else "c14_par"
        sin = ms["clase_por_criterio"].get(f"{f['qid']}#{f['criterio_idx']}", {})
        filas.append([f"{f['qid']}#{f['criterio_idx']}", f["ancla"], rg, val[:60],
                      len(f.get("nodos_ancla_con_valor", [])), f.get("n_nodos_fuera_del_ancla_con_valor", "—"),
                      f["clase"]["C3"], f["clase"]["C4"], f"{sin.get('C3')} / {sin.get('C4')}"])
    L.append(T(filas, ["Criterio", "Ancla", "Regex", "Valor", "Nodos ancla", "Fuera", "C3", "C4",
                       "C3 / C4 sin A-P6PAR"]))
    L.append("")

    dm = res["cap_1_2_contra_tabla"]
    L.append("## Demostración puntual: `cap::1.2` contra el parser de tablas (D-TABLA-1.2)\n")
    L.append(f"Tabla asignada: `{dm.get('tabla')}`; encabezados {dm.get('encabezados')}; cifras {dm.get('cifras')}.\n")
    L.append(T([[f"`{x['id'][:60]}…`", x["clase_por_descripcion"], x["umbral"], x["monto_tabla"],
                 "sí" if x["coincide_con_tabla"] else "NO"] for x in dm.get("restricciones", [])],
               ["Restriccion", "Clase según la descripción", "umbral", "Monto en la tabla", "Coincide"]))
    L.append("")

    dr = res["dim_relacionales"]
    L.append("## Dimensionamiento de los umbrales relacionales (D-REL-DIM)\n")
    cl = ["con_cuantia", "relacional", "relacional_con_campo", "relacional_sin_campo",
          "forma_base_de_del_sobre", "forma_veces_articulo", "forma_equivalente_monto"]
    filas = []
    for g, r in dr.items():
        for t, x in r["por_tipo"].items():
            filas.append([g, t] + [x.get(c, 0) for c in cl])
        filas.append([g, "**total**"] + [r["total"].get(c, 0) for c in cl])
    L.append(T(filas, ["Grafo", "Tipo", "Con cuantía (c14)", "Relacional", "Relacional con campo",
                       "Relacional sin campo", "Forma: % o veces + de/del/sobre", "Forma: veces + artículo",
                       "Forma: equivalente + monto"]))
    L.append("\nLas formas no son excluyentes: un nodo puede tener más de una.\n")

    co = res["cobertura_otros_portadores"]
    L.append("## Cobertura de aristas de los demás portadores de valor (D-COB)\n")
    cl = ["obligacion_con_plazo", "obligacion_con_plazo_sin_regula_ni_condiciona",
          "obligacion_con_cuantia_sin_campo", "obligacion_con_cuantia_sin_campo_sin_regula_ni_condiciona",
          "excepcion_con_cuantia", "excepcion_con_cuantia_sin_exceptua"]
    L.append(T([[g] + [x.get(c, 0) for c in cl] for g, x in co.items()],
               ["Grafo", "Obligacion con plazo", "…sin regula ni condiciona", "Obligacion con cuantía sin campo",
                "…sin regula ni condiciona", "Excepcion con cuantía", "…sin exceptua(_obligacion)"]))
    L.append("")

    dmod = res["dim_modelo"]
    L.append("## Dimensionamiento del llenado por un modelo (D-ESTIM) — ESTIMACIÓN NO VERIFICADA\n")
    filas = []
    for g, r in dmod.items():
        for sub, x in r.items():
            filas.append([g, sub, x["nodos"], x["chunks_llamadas"], x["tokens_entrada_variables"],
                          x["tokens_salida"], x["costo_usd_estimado_NO_VERIFICADO"], x["referencia_e1e3_usd"]])
    L.append(T(filas, ["Grafo", "Subconjunto", "Nodos", "Llamadas (chunks)", "Tokens de entrada variables",
                       "Tokens de salida", "USD estimado (NO VERIFICADO)", "Referencia E1+E3 × chunks (USD)"]))
    L.append("\nSupuestos NO VERIFICADOS: prompt fijo de 1.500 tokens y 60 tokens de salida por nodo. La fórmula "
             "y las tarifas están en D-ESTIM.\n")
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ main

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default=str(AQUI))
    args = ap.parse_args()
    salida = Path(args.salida)
    salida.mkdir(parents=True, exist_ok=True)

    entradas = {"grafos": []}
    grafos = {}
    for g, nombre, ruta, sha in u1.GRAFOS:
        s = u1.sha256(REPO / ruta)
        if s != sha:
            raise SystemExit(f"sha256 de {ruta} = {s}; esperado {sha}. Se frena.")
        entradas["grafos"].append({"clave": g, "nombre": nombre, "ruta": ruta, "sha256": s})
        grafos[g] = cargar(ruta)
    entradas["preguntas_sha256"] = u1.sha256(REPO / PREGUNTAS)
    entradas["trazas_sha256"] = {}
    for celda, d in TRAZAS.items():
        h = "".join(u1.sha256(p) for p in sorted((REPO / d).glob("EV2F-*.json")))
        entradas["trazas_sha256"][celda] = hashlib.sha256(h.encode()).hexdigest()

    man = cargar(u1.MANIFIESTO)
    chunks, chunks_por_to = {}, {}
    for t in man["tos"]:
        lista = cargar(f"{u1.E0_DIR}/chunks_{t['id']}.json")
        chunks_por_to[t["id"]] = lista
        for c in lista:
            chunks[c["id"]] = c

    doc = __doc__.split("DECLARACIONES (fijadas antes de aplicar; se repiten en el .md):")[1]
    previas, agregados = doc.split("AGREGADOS TRAS LA CORRIDA DE PRUEBA", 1)
    agregados = agregados.split(":\n", 1)[1]

    def bloques(texto: str, pref: str) -> dict:
        out = {}
        for b in re.split(r"\n(?=" + pref + r"-[A-Z0-9.-]+ · )", texto.strip()):
            nombre, cuerpo = b.split(" · ", 1)
            out[nombre.strip()] = re.sub(r"\s+", " ", cuerpo).strip()
        return out

    decl = bloques(previas, "D")
    agreg = bloques(agregados, "A")

    m4, csv_txt = medicion_4(grafos["desarrollo"], chunks)
    (salida / "muestra_limita_30.csv").write_text(csv_txt, encoding="utf-8")
    sha_csv = u1.sha256(salida / "muestra_limita_30.csv")

    USAR_A_P6PAR["activo"] = False
    m5_base = medicion_5(grafos["desarrollo"])
    m5_sin = {k: m5_base[k] for k in ("criterios_con_cuantia", "clases_c14", "clases_solo_c14_par")}
    m5_sin["clase_por_criterio"] = {f"{f['qid']}#{f['criterio_idx']}": f["clase"]
                                    for f in m5_base["filas"] if not f.get("solo_c14_eur")}
    USAR_A_P6PAR["activo"] = True
    m5 = medicion_5(grafos["desarrollo"])

    res = {
        "unidad": "U-UMBRAL", "etapa": "U2",
        "comando": "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/u_umbral_u2.py",
        "declaraciones": decl, "agregados_tras_corrida_de_prueba": agreg, "entradas": entradas,
        "medicion_4": dict(m4, sha256_csv=sha_csv),
        "medicion_5": m5,
        "medicion_5_sin_A_P6PAR": m5_sin,
        "cap_1_2_contra_tabla": demostracion_cap_1_2(grafos["desarrollo"], chunks_por_to["cap"]),
        "dim_relacionales": dim_relacionales(grafos),
        "cobertura_otros_portadores": cobertura_otros(grafos),
        "dim_modelo": dim_modelo({g: grafos[g] for g in ("desarrollo", "diez")}, chunks),
    }
    (salida / "u2_muestra_trazas.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (salida / "u2_muestra_trazas.md").write_text(escribir_md(res, sha_csv), encoding="utf-8")
    for f in ("muestra_limita_30.csv", "u2_muestra_trazas.json", "u2_muestra_trazas.md"):
        print(f"escrito: {salida / f}")


if __name__ == "__main__":
    main()
