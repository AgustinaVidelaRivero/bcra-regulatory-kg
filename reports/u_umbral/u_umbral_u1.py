"""
u_umbral_u1.py — U-UMBRAL, etapa U1: mediciones sobre los grafos y E0 (USD 0).

Mandato: docs/mandatos/UUMBRAL_investigacion.md (firmado el 30/09/2026).
Solo lectura: no llama a ninguna API, no usa Neo4j, no edita nada fuera del
directorio de salida. Importa `e0_tablas.py` sin editarlo.

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/u_umbral_u1.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/u_umbral_u1.py --salida DIR

Escribe u1_mediciones.json y u1_mediciones.md en el directorio de salida
(por defecto, el de este script). Salida determinística: sin fechas ni rutas
absolutas; la doble corrida tiene que dar archivos idénticos byte a byte.

DECLARACIONES (fijadas antes de aplicar; se repiten en el .md):

D-N1 · Normalización de la medición 1: NFC, después minúsculas (str.lower),
  después toda secuencia de espacios en blanco (incluidos los saltos de línea
  de E0) a un solo espacio, y strip. Nada más: no se quitan tildes, puntuación
  ni guiones de corte de línea. «Literal» = el valor normalizado es subcadena
  del texto normalizado.

D-C14 · Regex de cuantía del comando [c14] de docs/tablero_correcciones.md:136-141,
  implementada tal como la describe la prosa, sobre properties.descripcion en
  NFC y sin distinguir mayúsculas: porcentaje (`\\d+([.,]\\d+)?\\s*%` o «por
  ciento»), `\\bveces\\b`, plazo (número en cifras o en letras de la lista
  LETRAS seguido de día, mes, año, hora o semana, en singular o plural, o
  «días hábiles/corridos») y monto ($, US$, U$S o USD seguidos de cifra, o
  cifra seguida, con «millones de» o «mil» opcionales, de pesos, dólares, USD
  o UVA). «Con campo»: `umbral` o `plazo` no vacío.

D-C14EUR · Variante con nombre propio «c14_eur», declarada ANTES de aplicarla
  (decisión 3 del mandato): idéntica a c14 más «€» entre los prefijos de
  moneda seguidos de cifra. Motivo: c14 literal reproduce los «sin campo» del
  tablero pero da un nodo menos en el total con cuantía de r1, desarrollo y
  diez; el nodo es la Restriccion de cap::2.8.3.3 («equivalente en pesos
  €1.000.000»). Se reportan las dos.

D-PTL · Patrón de tabla linealizada (medición 2), sobre el texto propio del
  chunk (`texto`, sin la herencia) partido en líneas: dispara en una línea
  con dos o más tokens separados por espacios, todos cifras (regex
  RE_TOKEN_CIFRA: signo o paréntesis opcional, prefijo de moneda opcional,
  dígitos con puntos o comas, % opcional), cuando las DOS líneas anteriores
  no están vacías, no tienen ningún dígito y tienen 60 caracteres o menos
  (encabezados cortos). Barrido principal: chunks con
  flags.contenido_tabular falso; los marcados se barren aparte, como dato
  informativo de sensibilidad del patrón.

D-NODOS-CHUNK · Nodos de un chunk: los nodos con alguna procedencia cuyo
  chunk_id es el del chunk, excluidos TextoOrdenado, Sujeto y Comunicacion
  (nodos documentales o de catálogo que llevan procedencia en muchos chunks).

D-TAB · Asignación de las tablas de e0_tablas.parsear_to a chunks: cada
  segmento de tabla (página p) se compara con los chunks del mismo TO cuyo
  campo `paginas` contiene p; puntaje = tamaño de la intersección de
  multiconjuntos entre los tokens de las celdas y los tokens del texto propio
  del chunk, dividido por los tokens de las celdas. El segmento se asigna al
  chunk de puntaje máximo si ese puntaje es 0,5 o más; con empate, a todos los
  empatados, y el empate se registra.

D-P6 · Prototipo del llenado por paso posterior en código (medición 6):
  regex propias, distintas de c14, que extraen triples (tipo, valor, unidad):
  porcentaje (cifra con % o cifra/letras con «por ciento»), veces
  (cifra/letras + «veces»), plazo (cifra/letras, con número entre paréntesis
  opcional, + día, mes, año, hora o semana; «hábiles/corridos» se guarda como
  calificador y no entra en la comparación) y monto (prefijo $, US$, U$S,
  USD, EUR o € + cifra con «millones»/«mil» opcional, o cifra + «millones
  de»/«mil millones de»/«mil» opcional + pesos, dólares, USD, UVA o euros).
  Moneda canónica: $ y pesos → ARS; US$, U$S, USD y dólares → USD; €, EUR y
  euros → EUR; UVA. Número: con coma, la coma es decimal y los puntos son de
  miles; sin coma, `\\d{1,3}(\\.\\d{3})+` es de miles y cualquier otro punto
  es decimal; se quitan puntos y comas finales. Letras: las de LETRAS_VALOR,
  de una sola palabra; una palabra numérica precedida de otra (o de «y» tras
  otra) es un número compuesto: no se extrae y se cuenta como no cubierto.
  Multiplicadores: mil 10^3, millones 10^6, mil millones 10^9.

D-COINC · Regla de coincidencia de la medición 6, fijada antes de comparar.
  F = triples que el prototipo extrae del valor del campo (`umbral` o
  `plazo`); D = triples que extrae de la descripción. Se evalúa en orden:
  «no extrae» si D está vacío; «campo sin cuantía» si F está vacío (el campo
  no tiene un valor que el prototipo reconozca, por ejemplo «mensual»);
  «coincide» si F ⊆ D; «coincide parcial» si F ∩ D no es vacío y F ⊄ D;
  «difiere» si F ∩ D es vacío. La comparación es exacta sobre (tipo, valor
  normalizado como Decimal, unidad canónica).

D-REL · Umbral relacional (detección léxica, no lectura): la descripción
  tiene un porcentaje o «veces» seguido de «de», «del» o «sobre» y una
  palabra (con artículo o posesivo opcional), o la palabra «equivalente» a
  40 caracteres o menos antes de un monto. Marca que el triple no captura la
  base del cálculo.

AGREGADOS TRAS LA CORRIDA DE PRUEBA (30/09/2026; informativos, rotulados como
posteriores: no reemplazan ninguna declaración previa y se reportan aparte):

A-REL · Ampliación de D-REL tras una prueba sintética, antes de reportar:
  «dos veces el patrimonio» no disparaba porque D-REL exige «de» después de
  «veces». Se suma «veces» seguido de artículo o posesivo (el, la, los, las,
  su, sus) y una palabra. La columna «relacional» usa D-REL más A-REL.

A-N1S · Sensibilidad de la medición 1: además de D-N1, se eliminan TODOS los
  espacios en blanco en el valor y en el texto antes de comparar (caso visto
  en la corrida de prueba: «1%» en el campo, «1 %» en E0). Se reporta en
  columnas propias; la literalidad de referencia sigue siendo D-N1.

A-RELLENO · Valores de relleno (detección léxica, no lectura): el valor del
  campo, normalizado con D-N1, es exactamente «n/a», «na», «no aplica»,
  «permanente», o empieza con «no especificad», «sin especificar», «sin
  plazo» o «no se especifica».
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import sys
import unicodedata
from decimal import Decimal, InvalidOperation
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
AQUI = Path(__file__).resolve().parent

GRAFOS = [
    ("desarrollo", "KG-Tanda0-Desarrollo-r1",
     "data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json",
     "eab2fdd01dec4dad026d596a793919e666920fab127d7efb14b5b00857ae64ef"),
    ("r1", "KG-Reextraído-r1",
     "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json",
     "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"),
    ("diez", "KG-Tanda0-Diez-r1",
     "data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1/kg.json",
     "dd42d6d9c0c8379da90ec4ed4e4659157a960a0d1ceaf8af5a008bdd9cad9010"),
]
E0_DIR = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0"
E0_ENM01 = "data/experiment/reextraccion_v2/e0_chunking/salida_enm01"
E0_TABLAS_DIR = "data/experiment/reextraccion_v2/e0_chunking"
MANIFIESTO = "data/experiment/reextraccion_v2/manifiestos/tanda0_10tos.json"
HARNESS = "data/experiment/evaluacion/harness.py"
TOS_DEV = ("pro", "cla", "ric", "cap", "ext")
TIPOS_CUANTIA = ("Restriccion", "Condicion", "Obligacion", "Excepcion")
TIPOS_NO_CONTENIDO = ("TextoOrdenado", "Sujeto", "Comunicacion")
MAX_RESUMEN = 160  # harness.py:110, _short_props(max_len=160)
CONTROL_CHUNK = "cap::1.2"

# Cifras del tablero, fila «Cuantías sin campo estructurado» (:61):
# (sin campo, con cuantía) por grafo, y el desglose de «sin campo» por tipo.
TABLERO_C14 = {
    "r1": (218, 639, {"Restriccion": 63, "Obligacion": 106, "Excepcion": 49}),
    "desarrollo": (287, 606, {"Restriccion": 34, "Condicion": 134,
                              "Obligacion": 76, "Excepcion": 43}),
    "diez": (323, 683, None),
}

# ------------------------------------------------------------------ regex c14

LETRAS = ["un", "una", "uno", "dos", "tres", "cuatro", "cinco", "seis",
          "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce",
          "quince", "dieciséis", "dieciseis", "diecisiete", "dieciocho",
          "diecinueve", "veinte", "veintiuno", "veintiún", "veintiun",
          "veintidós", "veintidos", "veintitrés", "veintitres", "veinticuatro",
          "veinticinco", "veintiséis", "veintiseis", "veintisiete",
          "veintiocho", "veintinueve", "treinta", "cuarenta", "cincuenta",
          "sesenta", "setenta", "ochenta", "noventa", "cien", "ciento"]
_ALT_LETRAS = "|".join(sorted(LETRAS, key=len, reverse=True))
_NUM_C14 = r"(?:\d+|" + _ALT_LETRAS + r")"
_UNID = r"(?:d[ií]as?|mes(?:es)?|a[ñn]os?|horas?|semanas?)"


def _c14(eur: bool) -> dict:
    pref = r"(?:US\$|U\$S|USD|\$" + (r"|€" if eur else "") + r")"
    return {
        "porcentaje": re.compile(r"\d+(?:[.,]\d+)?\s*%|por\s+ciento", re.I),
        "veces": re.compile(r"\bveces\b", re.I),
        "plazo": re.compile(r"\b" + _NUM_C14 + r"\s+" + _UNID + r"\b"
                            r"|d[ií]as\s+(?:h[aá]biles|corridos)", re.I),
        "monto": re.compile(pref + r"\s*\d"
                            r"|\d(?:[\d.,]*)\s*(?:millones\s+de\s+|mil\s+)?"
                            r"(?:pesos|d[oó]lares|USD|UVA)\b", re.I),
    }


VARIANTES = {"c14": _c14(False), "c14_eur": _c14(True)}


def spans_cuantia(texto: str, pats: dict) -> list[tuple[int, int, list]]:
    """Spans de cuantía fusionados (los solapados de distintos sub-patrones
    cuentan como una sola cuantía)."""
    crudos = []
    for tipo, p in pats.items():
        for m in p.finditer(texto):
            crudos.append((m.start(), m.end(), tipo))
    crudos.sort()
    out: list[list] = []
    for s, e, t in crudos:
        if out and s < out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
            if t not in out[-1][2]:
                out[-1][2].append(t)
        else:
            out.append([s, e, [t]])
    return [(s, e, sorted(t)) for s, e, t in out]


def nfc(s) -> str:
    return unicodedata.normalize("NFC", str(s or ""))


def norm1(s) -> str:
    return re.sub(r"\s+", " ", nfc(s).lower()).strip()


# ------------------------------------------------------------------ util

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def props(n: dict) -> dict:
    return n.get("properties") or {}


def campo(n: dict, clave: str) -> str | None:
    v = props(n).get(clave)
    if isinstance(v, str) and v.strip():
        return v
    return None


def con_campo(n: dict) -> bool:
    return bool(campo(n, "umbral") or campo(n, "plazo"))


def provs(n: dict) -> list[dict]:
    p = n.get("provenances")
    if p:
        return p
    return [n["provenance"]] if n.get("provenance") else []


def chunk_ids(n: dict) -> list[str]:
    out = []
    for pv in provs(n):
        c = pv.get("chunk_id")
        if c and c not in out:
            out.append(c)
    return out


def contar(it) -> dict:
    return dict(sorted(collections.Counter(it).items()))


# ------------------------------------------------------------------ medición 1

RE_RELLENO = re.compile(r"^(?:n/a|na|no aplica|permanente)$"
                        r"|^(?:no especificad|sin especificar|sin plazo|no se especifica)")


def sin_espacios(s: str) -> str:
    return re.sub(r"\s+", "", s)


def medicion_1(grafos: dict, chunks: dict) -> dict:
    cache_n: dict[str, tuple[str, str]] = {}

    def textos(cid: str):
        if cid not in cache_n:
            c = chunks[cid]
            p = norm1(c["texto"])
            h = norm1(" ".join(h.get("texto", "") for h in c.get("herencia") or []))
            cache_n[cid] = (p, h, sin_espacios(p), sin_espacios(h))
        return cache_n[cid]

    salida = {}
    for g, k in grafos.items():
        resumen = collections.defaultdict(collections.Counter)
        no_literales = []
        for n in k["nodes"]:
            for clave in ("umbral", "plazo"):
                v = campo(n, clave)
                if v is None:
                    continue
                nv = norm1(v)
                en_desc = nv in norm1(props(n).get("descripcion"))
                cids = chunk_ids(n)
                presentes = [c for c in cids if c in chunks]
                faltantes = [c for c in cids if c not in chunks]
                propio = any(nv in textos(c)[0] for c in presentes)
                heredado = any(nv in textos(c)[1] for c in presentes)
                if not presentes:
                    e0 = "sin_chunk"
                elif propio:
                    e0 = "propio"
                elif heredado:
                    e0 = "solo_heredado"
                else:
                    e0 = "no"
                en_e0 = e0 in ("propio", "solo_heredado")
                # A-N1S (sensibilidad) y A-RELLENO (informativos)
                sv = sin_espacios(nv)
                en_desc_s = sv in sin_espacios(norm1(props(n).get("descripcion")))
                en_e0_s = any(sv in textos(c)[2] or sv in textos(c)[3] for c in presentes)
                relleno = bool(RE_RELLENO.search(nv))
                r = resumen[f"{n['type']}.{clave}"]
                r["A_N1S_en_descripcion"] += en_desc_s
                r["A_N1S_en_e0"] += en_e0_s
                r["A_N1S_descripcion_y_e0"] += en_desc_s and en_e0_s
                r["A_RELLENO"] += relleno
                r["total"] += 1
                r["en_descripcion"] += en_desc
                r["en_e0_propio"] += e0 == "propio"
                r["en_e0_solo_heredado"] += e0 == "solo_heredado"
                r["en_e0"] += en_e0
                r["sin_chunk"] += e0 == "sin_chunk"
                r["descripcion_y_e0"] += en_desc and en_e0
                r["solo_descripcion"] += en_desc and not en_e0
                r["solo_e0"] += en_e0 and not en_desc
                r["ninguno"] += (not en_desc) and (not en_e0)
                if not (en_desc and en_e0):
                    no_literales.append({
                        "id": n["id"], "type": n["type"], "campo": clave,
                        "valor": v, "en_descripcion": en_desc, "e0": e0,
                        "A_N1S_en_descripcion": en_desc_s, "A_N1S_en_e0": en_e0_s,
                        "A_RELLENO": relleno,
                        "chunk_ids": cids, "chunk_ids_no_encontrados": faltantes,
                    })
        claves = ("total", "en_descripcion", "en_e0", "en_e0_propio",
                  "en_e0_solo_heredado", "descripcion_y_e0", "solo_descripcion",
                  "solo_e0", "ninguno", "sin_chunk", "A_N1S_en_descripcion",
                  "A_N1S_en_e0", "A_N1S_descripcion_y_e0", "A_RELLENO")
        por = {t: {c: r[c] for c in claves} for t, r in sorted(resumen.items())}
        total = {c: sum(r[c] for r in resumen.values()) for c in claves}
        salida[g] = {"por_tipo_campo": por, "total": total,
                     "no_literales": no_literales}
    return salida


# ------------------------------------------------------------------ medición 2

RE_TOKEN_CIFRA = re.compile(r"^[(\-–]?(?:US\$|U\$S|\$|€)?\d[\d.,]*%?\)?$")
RE_DIGITO = re.compile(r"\d")
MAX_LARGO_ENCABEZADO = 60


def ptl(texto: str) -> list[dict]:
    lineas = texto.split("\n")
    disparos = []
    for i, linea in enumerate(lineas):
        toks = linea.split()
        if len(toks) < 2 or not all(RE_TOKEN_CIFRA.match(t) for t in toks):
            continue
        if i < 2:
            continue
        prev = [lineas[i - 2].strip(), lineas[i - 1].strip()]
        if all(p and not RE_DIGITO.search(p) and len(p) <= MAX_LARGO_ENCABEZADO
               for p in prev):
            disparos.append({"linea": i, "cifras": linea.strip(),
                             "encabezado": prev})
    return disparos


def asignar_tablas(art_por_to: dict, chunks_por_to: dict) -> dict:
    """chunk_id → lista de segmentos de tabla asignados (regla D-TAB)."""
    asignadas: dict[str, list] = collections.defaultdict(list)
    no_asignados = []
    for to, art in art_por_to.items():
        lista = chunks_por_to[to]
        tok_chunk = {c["id"]: collections.Counter(c["texto"].split()) for c in lista}
        for t in art["tablas_logicas"]:
            for s in t["segmentos"]:
                toks = collections.Counter(
                    x for fila in s["filas"] for c in fila for x in (c or "").split())
                n_tok = sum(toks.values())
                cands = [c["id"] for c in lista if s["pagina"] in (c.get("paginas") or [])]
                puntajes = []
                for cid in cands:
                    inter = sum((toks & tok_chunk[cid]).values())
                    puntajes.append((round(inter / n_tok, 4) if n_tok else 0.0, cid))
                mejor = max((p for p, _ in puntajes), default=0.0)
                elegidos = [cid for p, cid in puntajes if p == mejor] if mejor >= 0.5 else []
                reg = {"tabla": t["id"], "pagina": s["pagina"],
                       "indice_en_pagina": s["indice_en_pagina"],
                       "estado": t["estado"], "causas": t["causas"],
                       "puntaje": mejor, "empate": len(elegidos) > 1,
                       "tokens_celdas": n_tok}
                if elegidos:
                    for cid in elegidos:
                        asignadas[cid].append(reg)
                else:
                    no_asignados.append(dict(reg, candidatos=len(cands)))
    return {"por_chunk": dict(asignadas), "no_asignados": no_asignados}


def medicion_2(grafos, chunks_por_to, art_por_to, nodos_por_chunk, pats):
    asig = asignar_tablas(art_por_to, chunks_por_to)
    por_chunk = asig["por_chunk"]
    grafos_de_to = {to: [g for g in grafos if g == "diez" or to in TOS_DEV]
                    for to in chunks_por_to}

    def resumen_nodos(cid: str, to: str) -> dict:
        out = {}
        for g in grafos_de_to[to]:
            ns = nodos_por_chunk[g].get(cid, [])
            out[g] = {
                "n_nodos": len(ns),
                "con_umbral": [n["id"] for n in ns if campo(n, "umbral")],
                "con_campo": [n["id"] for n in ns if con_campo(n)],
                "con_cuantia_c14": [n["id"] for n in ns
                                    if spans_cuantia(nfc(props(n).get("descripcion")), pats["c14"])],
                "con_cuantia_c14_eur": [n["id"] for n in ns
                                        if spans_cuantia(nfc(props(n).get("descripcion")), pats["c14_eur"])],
            }
        return out

    no_marcados, marcados = [], []
    for to, lista in chunks_por_to.items():
        for c in lista:
            d = ptl(c["texto"])
            fila = {"chunk_id": c["id"], "to": to, "paginas": c.get("paginas"),
                    "dispara": bool(d), "disparos": d,
                    "tablas_e0_tablas": por_chunk.get(c["id"], [])}
            (marcados if c["flags"]["contenido_tabular"] else no_marcados).append(fila)

    disparan = [f for f in no_marcados if f["dispara"]]
    for f in disparan:
        f["nodos"] = resumen_nodos(f["chunk_id"], f["to"])
    solo_tabla = [f for f in no_marcados if f["tablas_e0_tablas"] and not f["dispara"]]
    for f in solo_tabla:
        f["nodos"] = resumen_nodos(f["chunk_id"], f["to"])

    def cruce(filas):
        c = collections.Counter()
        for f in filas:
            c[("dispara" if f["dispara"] else "no_dispara") + "|" +
              ("tabla_e0_tablas" if f["tablas_e0_tablas"] else "sin_tabla_e0_tablas")] += 1
        return dict(sorted(c.items()))

    def por_grafo_de(filas_chunk):
        out = {}
        for g in grafos:
            filas = [f for f in filas_chunk if g in f["nodos"]]
            cu = collections.Counter()
            for f in filas:
                r = f["nodos"][g]
                cu["chunks"] += 1
                cu["sin_nodos"] += r["n_nodos"] == 0
                cu["con_nodo_umbral"] += bool(r["con_umbral"])
                cu["con_nodo_cuantia_c14"] += bool(r["con_cuantia_c14"])
                cu["con_nodo_cuantia_c14_eur"] += bool(r["con_cuantia_c14_eur"])
                cu["con_nodo_umbral_o_cuantia_c14"] += bool(r["con_umbral"] or r["con_cuantia_c14"])
                cu["con_nodo_umbral_o_cuantia_c14_eur"] += bool(r["con_umbral"] or r["con_cuantia_c14_eur"])
                cu["nodos"] += r["n_nodos"]
                cu["nodos_con_umbral"] += len(r["con_umbral"])
                cu["nodos_con_cuantia_c14"] += len(r["con_cuantia_c14"])
            out[g] = dict(sorted(cu.items()))
        return out

    por_grafo = por_grafo_de(disparan)
    por_grafo_solo_tabla = por_grafo_de(solo_tabla)

    control = next((f for f in no_marcados + marcados if f["chunk_id"] == CONTROL_CHUNK), None)
    if control is None or not control["dispara"]:
        raise SystemExit(f"CONTROL FALLIDO: el patrón no dispara en {CONTROL_CHUNK}")

    return {
        "chunks_total": len(no_marcados) + len(marcados),
        "chunks_no_marcados": len(no_marcados),
        "chunks_marcados": len(marcados),
        "no_marcados_que_disparan": len(disparan),
        "no_marcados_que_disparan_por_to": contar(f["to"] for f in disparan),
        "marcados_que_disparan_informativo": sum(1 for f in marcados if f["dispara"]),
        "cruce_no_marcados_patron_x_e0_tablas": cruce(no_marcados),
        "cruce_marcados_patron_x_e0_tablas_informativo": cruce(marcados),
        "nodos_de_los_chunks_que_disparan_por_grafo": por_grafo,
        "nodos_de_los_chunks_con_tabla_e0_tablas_sin_disparo_por_grafo_informativo": por_grafo_solo_tabla,
        "control_cap_1_2": {k: control[k] for k in
                            ("chunk_id", "dispara", "disparos", "tablas_e0_tablas")},
        "chunks_que_disparan": disparan,
        "no_marcados_con_tabla_e0_tablas_sin_disparo": [
            {k: f[k] for k in ("chunk_id", "to", "paginas", "tablas_e0_tablas", "nodos")}
            for f in solo_tabla],
        "e0_tablas_conteos_por_to": {to: art["conteos"] for to, art in art_por_to.items()},
        "e0_tablas_segmentos_no_asignados": asig["no_asignados"],
    }


# ------------------------------------------------------------------ medición 3

def medicion_3(grafos: dict) -> dict:
    salida = {}
    for g, k in grafos.items():
        nodos = [n for n in k["nodes"] if n["type"] in TIPOS_CUANTIA]
        no_nfc = sum(1 for n in nodos
                     if nfc(props(n).get("descripcion")) != str(props(n).get("descripcion") or ""))
        por_var = {}
        for var, pats in VARIANTES.items():
            base = collections.defaultdict(collections.Counter)
            for n in nodos:
                d = nfc(props(n).get("descripcion"))
                sp = spans_cuantia(d, pats)
                if not sp:
                    continue
                t = n["type"]
                cc = con_campo(n)
                b = base[t]
                b["con_cuantia"] += 1
                b["con_campo"] += cc
                b["sin_campo"] += not cc
                if len(sp) >= 2:
                    b["dos_o_mas_cuantias"] += 1
                    b["dos_o_mas_cuantias_sin_campo"] += not cc
                if sp[0][0] >= MAX_RESUMEN:
                    b["todas_despues_de_160"] += 1
                    b["todas_despues_de_160_sin_campo"] += not cc
                if any(s >= MAX_RESUMEN for s, _, _ in sp):
                    b["alguna_despues_de_160"] += 1
                if spans_cuantia(nfc(n.get("label")), pats):
                    b["cuantia_en_label"] += 1
                    b["cuantia_en_label_sin_campo"] += not cc
            claves = ("con_cuantia", "con_campo", "sin_campo", "dos_o_mas_cuantias",
                      "dos_o_mas_cuantias_sin_campo", "todas_despues_de_160",
                      "todas_despues_de_160_sin_campo", "alguna_despues_de_160",
                      "cuantia_en_label", "cuantia_en_label_sin_campo")
            por_tipo = {t: {c: base[t][c] for c in claves} for t in TIPOS_CUANTIA if t in base}
            total = {c: sum(base[t][c] for t in base) for c in claves}
            por_var[var] = {"por_tipo": por_tipo, "total": total}
        tab = TABLERO_C14.get(g)
        repro = None
        if tab:
            sin_t, tot_t, desg = tab
            repro = {}
            for var in VARIANTES:
                tt = por_var[var]["total"]
                ok_desg = desg is None or all(
                    por_var[var]["por_tipo"].get(t, {}).get("sin_campo", 0) == v
                    for t, v in desg.items())
                repro[var] = {"sin_campo": tt["sin_campo"], "con_cuantia": tt["con_cuantia"],
                              "tablero_sin_campo": sin_t, "tablero_con_cuantia": tot_t,
                              "sin_campo_reproduce": tt["sin_campo"] == sin_t and ok_desg,
                              "con_cuantia_reproduce": tt["con_cuantia"] == tot_t}
        solo_eur = []
        for n in nodos:
            d = nfc(props(n).get("descripcion"))
            if spans_cuantia(d, VARIANTES["c14_eur"]) and not spans_cuantia(d, VARIANTES["c14"]):
                solo_eur.append({"id": n["id"], "type": n["type"], "con_campo": con_campo(n),
                                 "chunk_ids": chunk_ids(n)})
        salida[g] = {"variantes": por_var, "reproduce_tablero": repro,
                     "nodos_solo_en_c14_eur": solo_eur,
                     "descripciones_que_cambian_con_nfc": no_nfc}
    return salida


# ------------------------------------------------------------------ medición 6

LETRAS_VALOR = {"un": 1, "una": 1, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4,
                "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9,
                "diez": 10, "once": 11, "doce": 12, "trece": 13, "catorce": 14,
                "quince": 15, "dieciséis": 16, "dieciseis": 16, "diecisiete": 17,
                "dieciocho": 18, "diecinueve": 19, "veinte": 20, "veintiuno": 21,
                "veintiún": 21, "veintiun": 21, "veintidós": 22, "veintidos": 22,
                "veintitrés": 23, "veintitres": 23, "veinticuatro": 24,
                "veinticinco": 25, "veintiséis": 26, "veintiseis": 26,
                "veintisiete": 27, "veintiocho": 28, "veintinueve": 29,
                "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60,
                "setenta": 70, "ochenta": 80, "noventa": 90, "cien": 100}
_ALT_LV = "|".join(sorted(LETRAS_VALOR, key=len, reverse=True))
_NUMW = r"(?:" + _ALT_LV + r")"
_CIFRA = r"\d+(?:[.,]\d+)*"
_NUMP6 = r"(\d+(?:[.,]\d+)?|" + _ALT_LV + r")"

P6 = [
    ("porcentaje", re.compile(r"(?<![\d.,])(\d+(?:[.,]\d+)?)\s*%", re.I)),
    ("porcentaje", re.compile(r"(?<![\w.,])" + _NUMP6 + r"\s+por\s+ciento", re.I)),
    ("veces", re.compile(r"(?<![\w.,])" + _NUMP6 + r"\s+veces\b", re.I)),
    ("plazo", re.compile(r"(?<![\w.,])(\d+|" + _ALT_LV + r")\s*(?:\((\d+|" + _ALT_LV +
                         r")\)\s*)?(d[ií]as?|mes(?:es)?|a[ñn]os?|horas?|semanas?)\b"
                         r"(?:\s+(h[aá]biles|corridos))?", re.I)),
    ("monto_pref", re.compile(r"(US\$|U\$S|USD|EUR|€|\$)\s*(\d[\d.,]*)"
                              r"(?:\s*(mil\s+millones|millones|mil)\b)?", re.I)),
    ("monto_suf", re.compile(r"(?<![\d.,])(\d[\d.,]*)\s*(?:(mil\s+millones\s+de|millones\s+de|mil)\s+)?"
                             r"(pesos|d[oó]lares(?:\s+estadounidenses)?|USD|UVA|euros)\b", re.I)),
]
RE_COMPUESTO_ANTES = re.compile(r"(?:\b(?:" + _ALT_LETRAS + r"|mil)\s+(?:y\s+)?)$", re.I)
RE_REL = [
    # D-REL
    re.compile(r"(?:%|por\s+ciento|veces)\s+(?:de|del|sobre)\s+(?:(?:la|el|los|las|su|sus|dicho|dicha|dichos|dichas|cada)\s+)?[a-záéíóúñ]", re.I),
    # A-REL
    re.compile(r"\bveces\s+(?:el|la|los|las|su|sus)\s+[a-záéíóúñ]", re.I),
]
RE_EQUIV = re.compile(r"equivalente", re.I)

MONEDA = {"$": "ARS", "pesos": "ARS", "us$": "USD", "u$s": "USD", "usd": "USD",
          "dólares": "USD", "dolares": "USD", "dólares estadounidenses": "USD",
          "dolares estadounidenses": "USD", "eur": "EUR", "€": "EUR", "euros": "EUR",
          "uva": "UVA"}
MULT = {None: 1, "mil": 10 ** 3, "millones": 10 ** 6, "mil millones": 10 ** 9,
        "millones de": 10 ** 6, "mil millones de": 10 ** 9}
UNIDAD_T = [(re.compile(r"^d[ií]as?$", re.I), "día"), (re.compile(r"^mes(es)?$", re.I), "mes"),
            (re.compile(r"^a[ñn]os?$", re.I), "año"), (re.compile(r"^horas?$", re.I), "hora"),
            (re.compile(r"^semanas?$", re.I), "semana")]


def parse_num(s: str) -> Decimal | None:
    s = s.strip()
    if s.lower() in LETRAS_VALOR:
        return Decimal(LETRAS_VALOR[s.lower()])
    s = s.rstrip(".,")
    if "," in s:
        s2 = s.replace(".", "").replace(",", ".")
    elif re.fullmatch(r"\d{1,3}(\.\d{3})+", s):
        s2 = s.replace(".", "")
    else:
        s2 = s
    try:
        return Decimal(s2)
    except InvalidOperation:
        return None


def dec_str(d: Decimal) -> str:
    t = format(d.normalize(), "f")
    return t


def compuesto(texto: str, inicio: int, grupo: str) -> bool:
    """El número en letras que empieza en `inicio` está precedido por otra
    palabra numérica (número compuesto: «treinta y cinco», «ciento ochenta»)."""
    if grupo.lower() not in LETRAS_VALOR:
        return False
    return bool(RE_COMPUESTO_ANTES.search(texto[max(0, inicio - 30):inicio]))


def extraer_p6(texto: str) -> dict:
    t = nfc(texto)
    triples = set()
    no_cubiertos = collections.Counter()
    inconsistencias = []
    for tipo, p in P6:
        for m in p.finditer(t):
            if tipo == "porcentaje":
                g = m.group(1)
                if compuesto(t, m.start(1), g):
                    no_cubiertos["letras_compuestas"] += 1
                    continue
                v = parse_num(g)
                if v is not None:
                    triples.add(("porcentaje", dec_str(v), "%"))
            elif tipo == "veces":
                g = m.group(1)
                if compuesto(t, m.start(1), g):
                    no_cubiertos["letras_compuestas"] += 1
                    continue
                v = parse_num(g)
                if v is not None:
                    triples.add(("veces", dec_str(v), "veces"))
            elif tipo == "plazo":
                g1, g2, u = m.group(1), m.group(2), m.group(3)
                if compuesto(t, m.start(1), g1):
                    no_cubiertos["letras_compuestas"] += 1
                    continue
                v1 = parse_num(g1)
                v2 = parse_num(g2) if g2 else None
                if v2 is not None and v1 is not None and v1 != v2:
                    inconsistencias.append(m.group(0))
                v = v1 if v1 is not None else v2
                unidad = next(c for r, c in UNIDAD_T if r.match(u))
                if v is not None:
                    triples.add(("plazo", dec_str(v), unidad))
            elif tipo == "monto_pref":
                mon = MONEDA[m.group(1).lower()]
                v = parse_num(m.group(2))
                mult = MULT[re.sub(r"\s+", " ", m.group(3).lower()) if m.group(3) else None]
                if v is not None:
                    triples.add(("monto", dec_str(v * mult), mon))
            elif tipo == "monto_suf":
                v = parse_num(m.group(1))
                mult = MULT[re.sub(r"\s+", " ", m.group(2).lower()) if m.group(2) else None]
                mon = MONEDA[re.sub(r"\s+", " ", m.group(3).lower())]
                if v is not None:
                    triples.add(("monto", dec_str(v * mult), mon))
    rel = any(r.search(t) for r in RE_REL)
    if not rel:
        for tipo, p in P6:
            if not tipo.startswith("monto"):
                continue
            for m in p.finditer(t):
                if RE_EQUIV.search(t[max(0, m.start() - 40):m.start()]):
                    rel = True
    return {"triples": sorted(triples), "no_cubiertos": dict(no_cubiertos),
            "inconsistencias": inconsistencias, "relacional": rel}


def medicion_6(grafos: dict) -> dict:
    salida = {}
    for g, k in grafos.items():
        # A: acuerdo contra el campo, donde existe
        acuerdo = collections.defaultdict(collections.Counter)
        detalle_difiere = []
        for n in k["nodes"]:
            for clave in ("umbral", "plazo"):
                v = campo(n, clave)
                if v is None:
                    continue
                F = set(map(tuple, extraer_p6(v)["triples"]))
                ed = extraer_p6(props(n).get("descripcion"))
                D = set(map(tuple, ed["triples"]))
                if not D:
                    cat = "no_extrae"
                elif not F:
                    cat = "campo_sin_cuantia"
                elif F <= D:
                    cat = "coincide"
                elif F & D:
                    cat = "coincide_parcial"
                else:
                    cat = "difiere"
                a = acuerdo[f"{n['type']}.{clave}"]
                a[cat] += 1
                a["total"] += 1
                if cat == "no_extrae" and F:
                    a["no_extrae_y_campo_con_cuantia"] += 1
                if cat == "coincide" and len(D) == 1:
                    a["coincide_y_unico_en_descripcion"] += 1
                if cat in ("difiere", "coincide_parcial"):
                    detalle_difiere.append({"id": n["id"], "type": n["type"], "campo": clave,
                                            "valor": v, "F": sorted(F), "D": sorted(D),
                                            "categoria": cat})
        cats = ("total", "coincide", "coincide_y_unico_en_descripcion", "coincide_parcial",
                "difiere", "campo_sin_cuantia", "no_extrae", "no_extrae_y_campo_con_cuantia")
        acuerdo_out = {t: {c: a[c] for c in cats} for t, a in sorted(acuerdo.items())}
        acuerdo_tot = {c: sum(a[c] for a in acuerdo.values()) for c in cats}

        # B: nodos de los cuatro tipos con cuantía (c14_eur ⊇ c14) — cobertura
        cob = collections.defaultdict(collections.Counter)
        ejemplos = collections.defaultdict(list)
        for n in k["nodes"]:
            if n["type"] not in TIPOS_CUANTIA:
                continue
            d = nfc(props(n).get("descripcion"))
            sp = spans_cuantia(d, VARIANTES["c14_eur"])
            en_lit = bool(spans_cuantia(d, VARIANTES["c14"]))
            e = extraer_p6(d)
            nt = len(e["triples"])
            if sp:
                estado = "con_campo" if con_campo(n) else "sin_campo"
                c = cob[estado]
                c["nodos"] += 1
                c["en_c14_literal"] += en_lit
                c["extrae_0"] += nt == 0
                c["extrae_1"] += nt == 1
                c["extrae_2_o_mas"] += nt >= 2
                c["letras_compuestas"] += bool(e["no_cubiertos"].get("letras_compuestas"))
                c["relacional"] += e["relacional"]
                c["inconsistencia_cifra_letras"] += bool(e["inconsistencias"])
                if nt == 0 and len(ejemplos["extrae_0_" + estado]) < 25:
                    ejemplos["extrae_0_" + estado].append({"id": n["id"], "descripcion": d[:240]})
                if e["no_cubiertos"].get("letras_compuestas") and len(ejemplos["letras_compuestas"]) < 25:
                    ejemplos["letras_compuestas"].append({"id": n["id"], "descripcion": d[:240]})
            elif nt:
                c = cob["fuera_de_c14_eur_" + ("con_campo" if con_campo(n) else "sin_campo")]
                c["nodos"] += 1
                c["extrae_1"] += nt == 1
                c["extrae_2_o_mas"] += nt >= 2
                if len(ejemplos["fuera_de_c14"]) < 25:
                    ejemplos["fuera_de_c14"].append({"id": n["id"], "triples": e["triples"],
                                                    "descripcion": d[:240]})
        cob_out = {k2: dict(sorted(v.items())) for k2, v in sorted(cob.items())}
        salida[g] = {"acuerdo_contra_campo": {"por_tipo_campo": acuerdo_out,
                                              "total": acuerdo_tot,
                                              "difiere_o_parcial": detalle_difiere},
                     "cobertura_cuatro_tipos": cob_out,
                     "ejemplos": {k2: v for k2, v in sorted(ejemplos.items())}}
    return salida


# ------------------------------------------------------------------ limita

def medicion_limita(grafos: dict) -> dict:
    salida = {}
    for g, k in grafos.items():
        by_id = {n["id"]: n for n in k["nodes"]}
        salientes = collections.defaultdict(list)
        for e in k["edges"]:
            salientes[e["source"]].append(e)
        limitas = [e for e in k["edges"] if e["relation"] == "limita"]
        src_tipo = contar(by_id[e["source"]]["type"] if e["source"] in by_id else "?" for e in limitas)
        tgt_tipo = contar(by_id[e["target"]]["type"] if e["target"] in by_id else "?" for e in limitas)
        src_rtipo = contar(str(props(by_id[e["source"]]).get("tipo")) for e in limitas
                           if e["source"] in by_id and by_id[e["source"]]["type"] == "Restriccion")
        desde_umbral = sum(1 for e in limitas if e["source"] in by_id and campo(by_id[e["source"]], "umbral"))
        rs = [n for n in k["nodes"] if n["type"] == "Restriccion"]
        n_lim = {n["id"]: len({e["target"] for e in salientes[n["id"]] if e["relation"] == "limita"})
                 for n in rs}
        con_umbral = [n for n in rs if campo(n, "umbral")]
        umbral_sin_limita = [n for n in con_umbral if n_lim[n["id"]] == 0]
        limita_sin_umbral = [n for n in rs if n_lim[n["id"]] > 0 and not campo(n, "umbral")]
        mas_de_una = [n for n in rs if n_lim[n["id"]] > 1]
        rel_de_umbral_sin_limita = contar(
            "+".join(sorted({e["relation"] for e in salientes[n["id"]]
                             if e["target"] in by_id and by_id[e["target"]]["type"] == "Operacion"}))
            or "(ninguna hacia Operacion)" for n in umbral_sin_limita)
        conds = [n for n in k["nodes"] if n["type"] == "Condicion"]
        cond = {}
        for var, pats in VARIANTES.items():
            cq = [n for n in conds if spans_cuantia(nfc(props(n).get("descripcion")), pats)]
            sin = [n for n in cq if not any(e["relation"] == "condicion_de" for e in salientes[n["id"]])]
            cond[var] = {"condiciones": len(conds), "con_cuantia": len(cq),
                         "con_cuantia_sin_condicion_de": len(sin)}
        salida[g] = {
            "limita_total": len(limitas),
            "limita_por_tipo_de_origen": src_tipo,
            "limita_por_tipo_de_destino": tgt_tipo,
            "limita_por_Restriccion_tipo": src_rtipo,
            "limita_desde_Restriccion_con_umbral": desde_umbral,
            "restricciones": len(rs),
            "restricciones_con_umbral": len(con_umbral),
            "restricciones_con_umbral_por_tipo": contar(str(props(n).get("tipo")) for n in con_umbral),
            "restricciones_con_umbral_sin_limita": len(umbral_sin_limita),
            "restricciones_con_umbral_sin_limita_por_tipo": contar(
                str(props(n).get("tipo")) for n in umbral_sin_limita),
            "restricciones_con_umbral_sin_limita_relaciones_a_operacion": rel_de_umbral_sin_limita,
            "restricciones_con_limita_sin_umbral_S18": len(limita_sin_umbral),
            "restricciones_con_limita_sin_umbral_por_tipo": contar(
                str(props(n).get("tipo")) for n in limita_sin_umbral),
            "restricciones_con_limita": sum(1 for v in n_lim.values() if v > 0),
            "restricciones_con_mas_de_una_limita": len(mas_de_una),
            "distribucion_limita_por_restriccion": contar(v for v in n_lim.values() if v > 0),
            "restricciones_con_mas_de_una_limita_ids": sorted(n["id"] for n in mas_de_una),
            "condiciones": cond,
        }
    return salida


# ------------------------------------------------------------------ md

def tabla(filas: list[list], cab: list[str]) -> str:
    out = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    for f in filas:
        out.append("| " + " | ".join(str(x) for x in f) + " |")
    return "\n".join(out)


def escribir_md(res: dict) -> str:
    L = []
    cmd = "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/u_umbral_u1.py"
    L.append("# U-UMBRAL · U1 — Mediciones sobre los grafos y E0\n")
    L.append("Mandato: `docs/mandatos/UUMBRAL_investigacion.md` (firmado el 30/09/2026). "
             "USD 0: sin API y sin Neo4j. Material de desarrollo: nada de esto es un resultado "
             "sobre EV2 (principio 7). Esta etapa mide; no propone ni decide.\n")
    L.append(f"Comando que reproduce todo este archivo y `u1_mediciones.json`:\n\n```\n{cmd}\n```\n")
    L.append("## Entradas y sellos\n")
    filas = [[x["nombre"], f"`{x['ruta']}`", f"`{x['sha256'][:16]}…`"] for x in res["entradas"]["grafos"]]
    L.append(tabla(filas, ["Grafo", "Ruta", "sha256"]))
    L.append("")
    L.append(f"E0: `{E0_DIR}/chunks_<to>.json` de los diez TOs ({res['entradas']['e0']['chunks_total']} "
             f"chunks). Para los cinco de desarrollo, idéntico byte a byte a `{E0_ENM01}` "
             f"(comprobado: {res['entradas']['e0']['dev_identico_a_enm01']}). PDFs del manifiesto "
             f"`{MANIFIESTO}`, sha256 comprobado contra `sha256_pdf`: "
             f"{res['entradas']['pdfs_ok']}. `e0_tablas.py` importado sin editar "
             f"(sha256 `{res['entradas']['e0_tablas_sha256'][:16]}…`). Resumen de `buscar_nodos`: "
             f"`{HARNESS}:110` (`max_len=160`, comprobado en el fuente: "
             f"{res['entradas']['harness_max_len_160']}).\n")
    L.append("## Declaraciones previas a la medición\n")
    for k2, v in res["declaraciones"].items():
        L.append(f"- **{k2}.** {v}")
    L.append("\n### Agregados tras la corrida de prueba (informativos, rotulados como posteriores)\n")
    L.append("Los agregué después de una corrida de prueba, antes de reportar. No reemplazan ninguna "
             "declaración previa y se reportan en columnas propias.\n")
    for k2, v in res["agregados_tras_corrida_de_prueba"].items():
        L.append(f"- **{k2}.** {v}")
    L.append("")

    # medición 1
    m1 = res["medicion_1"]
    L.append("## Medición 1 — Literalidad de `umbral` y `plazo`\n")
    L.append("Pares (nodo, campo) con valor no vacío. «E0» = texto propio o heredado del chunk de "
             "alguna procedencia del nodo. Normalización D-N1.\n")
    filas = []
    for g in m1:
        for t, r in m1[g]["por_tipo_campo"].items():
            filas.append([g, t, r["total"], r["en_descripcion"], r["en_e0"], r["en_e0_propio"],
                          r["en_e0_solo_heredado"], r["descripcion_y_e0"], r["solo_descripcion"],
                          r["solo_e0"], r["ninguno"], r["sin_chunk"]])
        r = m1[g]["total"]
        filas.append([g, "**total**", r["total"], r["en_descripcion"], r["en_e0"], r["en_e0_propio"],
                      r["en_e0_solo_heredado"], r["descripcion_y_e0"], r["solo_descripcion"],
                      r["solo_e0"], r["ninguno"], r["sin_chunk"]])
    L.append(tabla(filas, ["Grafo", "Tipo.campo", "Total", "En descripción", "En E0",
                           "E0 propio", "E0 solo heredado", "Desc. y E0", "Solo desc.",
                           "Solo E0", "Ninguno", "Sin chunk"]))
    L.append("\nInformativo (A-N1S, sin espacios; A-RELLENO, valores de relleno):\n")
    filas = []
    for g in m1:
        for t, r in list(m1[g]["por_tipo_campo"].items()) + [("**total**", m1[g]["total"])]:
            filas.append([g, t, r["total"], r["en_descripcion"], r["A_N1S_en_descripcion"], r["en_e0"],
                          r["A_N1S_en_e0"], r["descripcion_y_e0"], r["A_N1S_descripcion_y_e0"],
                          r["A_RELLENO"]])
    L.append(tabla(filas, ["Grafo", "Tipo.campo", "Total", "En desc. (D-N1)", "En desc. (A-N1S)",
                           "En E0 (D-N1)", "En E0 (A-N1S)", "Desc. y E0 (D-N1)", "Desc. y E0 (A-N1S)",
                           "Relleno (A-RELLENO)"]))
    L.append("\nLa lista completa de valores no literales (no están en la descripción, o no están en "
             "E0) está en `u1_mediciones.json`, clave `medicion_1.<grafo>.no_literales`.\n")

    # medición 2
    m2 = res["medicion_2"]
    L.append("## Medición 2 — Tablas no marcadas por E0\n")
    L.append(f"Chunks de los diez TOs: {m2['chunks_total']} ({m2['chunks_no_marcados']} con "
             f"`contenido_tabular` falso, {m2['chunks_marcados']} marcados). El patrón D-PTL dispara en "
             f"**{m2['no_marcados_que_disparan']}** chunks no marcados, por TO: "
             f"{m2['no_marcados_que_disparan_por_to']}. En los marcados (informativo, sensibilidad del "
             f"patrón): dispara en {m2['marcados_que_disparan_informativo']} de {m2['chunks_marcados']}.\n")
    c = m2["control_cap_1_2"]
    tabs = ", ".join(f"{t['tabla']} (p. {t['pagina']}, {t['estado']}, puntaje {t['puntaje']})"
                     for t in c["tablas_e0_tablas"]) or "ninguna"
    L.append(f"**Caso de control `cap::1.2`:** dispara = {c['dispara']}; línea de cifras "
             f"«{c['disparos'][0]['cifras']}» tras «{c['disparos'][0]['encabezado'][0]}» / "
             f"«{c['disparos'][0]['encabezado'][1]}». `e0_tablas` le asigna: {tabs}.\n")
    L.append("Cruce patrón × `e0_tablas` (regla D-TAB) sobre los chunks no marcados:\n")
    filas = [[k2, v] for k2, v in m2["cruce_no_marcados_patron_x_e0_tablas"].items()]
    L.append(tabla(filas, ["Celda", "Chunks"]))
    L.append("\nMismo cruce sobre los chunks marcados (informativo):\n")
    filas = [[k2, v] for k2, v in m2["cruce_marcados_patron_x_e0_tablas_informativo"].items()]
    L.append(tabla(filas, ["Celda", "Chunks"]))
    L.append("\nNodos de los chunks no marcados que disparan (D-NODOS-CHUNK), por grafo:\n")
    cl = ["chunks", "sin_nodos", "con_nodo_umbral", "con_nodo_cuantia_c14", "con_nodo_cuantia_c14_eur",
          "con_nodo_umbral_o_cuantia_c14", "nodos", "nodos_con_umbral", "nodos_con_cuantia_c14"]
    filas = [[g] + [r.get(x, 0) for x in cl] for g, r in m2["nodos_de_los_chunks_que_disparan_por_grafo"].items()]
    L.append(tabla(filas, ["Grafo", "Chunks", "Sin nodos", "Con nodo con umbral", "Con cuantía c14",
                           "Con cuantía c14_eur", "Umbral o cuantía c14", "Nodos", "Nodos con umbral",
                           "Nodos con cuantía c14"]))
    L.append("\nChunks no marcados que disparan:\n")
    filas = []
    for f in m2["chunks_que_disparan"]:
        tb = ";".join(f"{t['tabla']}({t['estado']})" for t in f["tablas_e0_tablas"]) or "—"
        gg = []
        for g, r in f["nodos"].items():
            gg.append(f"{g}: {r['n_nodos']} n, {len(r['con_umbral'])} umb, {len(r['con_cuantia_c14'])} cuant")
        filas.append([f"`{f['chunk_id']}`", f"«{f['disparos'][0]['cifras'][:40]}»", len(f["disparos"]), tb,
                      "; ".join(gg)])
    L.append(tabla(filas, ["Chunk", "Primera línea de cifras", "Disparos", "Tabla de e0_tablas",
                           "Nodos por grafo"]))
    st = m2["no_marcados_con_tabla_e0_tablas_sin_disparo"]
    L.append(f"\nChunks no marcados a los que `e0_tablas` asigna tabla sin que el patrón dispare "
             f"(informativo): {len(st)}.\n")
    filas = []
    for f in st:
        tb = ";".join(f"{t['tabla']}({t['estado']})" for t in f["tablas_e0_tablas"])
        gg = [f"{g}: {r['n_nodos']} n, {len(r['con_umbral'])} umb, {len(r['con_cuantia_c14'])} cuant"
              for g, r in f["nodos"].items()]
        filas.append([f"`{f['chunk_id']}`", tb, "; ".join(gg)])
    L.append(tabla(filas, ["Chunk", "Tablas de e0_tablas", "Nodos por grafo"]))
    L.append("\nResumen por grafo de esos chunks (informativo):\n")
    cl = ["chunks", "sin_nodos", "con_nodo_umbral", "con_nodo_cuantia_c14", "con_nodo_umbral_o_cuantia_c14",
          "nodos", "nodos_con_umbral", "nodos_con_cuantia_c14"]
    filas = [[g] + [r.get(x, 0) for x in cl] for g, r in
             m2["nodos_de_los_chunks_con_tabla_e0_tablas_sin_disparo_por_grafo_informativo"].items()]
    L.append(tabla(filas, ["Grafo", "Chunks", "Sin nodos", "Con nodo con umbral", "Con cuantía c14",
                           "Umbral o cuantía c14", "Nodos", "Nodos con umbral", "Nodos con cuantía c14"]))
    na = m2["e0_tablas_segmentos_no_asignados"]
    L.append(f"\nSegmentos de `e0_tablas` sin chunk asignado: {len(na)}; de ellos, "
             f"{sum(1 for x in na if x['candidatos'] == 0)} en páginas que ningún chunk declara en "
             f"`paginas`, y {sum(1 for x in na if x['candidatos'] > 0)} con candidatos y puntaje menor "
             f"que 0,5 (lista en el JSON).\n")

    # medición 3
    m3 = res["medicion_3"]
    L.append("## Medición 3 — Cuantías sin campo ([c14] y variante c14_eur)\n")
    L.append("Reproducción de la fila «Cuantías sin campo estructurado» del tablero (`docs/tablero_correcciones.md:61`):\n")
    filas = []
    for g in m3:
        rp = m3[g]["reproduce_tablero"]
        if not rp:
            continue
        for var, r in rp.items():
            filas.append([g, var, f"{r['sin_campo']} de {r['con_cuantia']}",
                          f"{r['tablero_sin_campo']} de {r['tablero_con_cuantia']}",
                          "sí" if r["sin_campo_reproduce"] else "NO",
                          "sí" if r["con_cuantia_reproduce"] else "NO"])
    L.append(tabla(filas, ["Grafo", "Variante", "Medido (sin campo de con cuantía)", "Tablero",
                           "Sin campo reproduce", "Total reproduce"]))
    L.append("")
    for g in m3:
        L.append(f"Nodos que solo detecta c14_eur en {g}: " +
                 (", ".join(f"`{x['id'][:60]}…` ({x['type']}, con campo {x['con_campo']}, {x['chunk_ids']})"
                            for x in m3[g]["nodos_solo_en_c14_eur"]) or "ninguno") + ".")
    L.append("")
    cl = ["con_cuantia", "con_campo", "sin_campo", "dos_o_mas_cuantias", "dos_o_mas_cuantias_sin_campo",
          "todas_despues_de_160", "todas_despues_de_160_sin_campo", "alguna_despues_de_160",
          "cuantia_en_label", "cuantia_en_label_sin_campo"]
    cab = ["Grafo", "Variante", "Tipo", "Con cuantía", "Con campo", "Sin campo", "≥2 cuantías",
           "≥2 y sin campo", "Todas desde 160", "Todas desde 160 y sin campo", "Alguna desde 160",
           "Cuantía en label", "Cuantía en label y sin campo"]
    filas = []
    for g in m3:
        for var, r in m3[g]["variantes"].items():
            for t, x in r["por_tipo"].items():
                filas.append([g, var, t] + [x[c2] for c2 in cl])
            filas.append([g, var, "**total**"] + [r["total"][c2] for c2 in cl])
    L.append(tabla(filas, cab))
    L.append("\n«Todas desde 160»: la primera cuantía empieza en el carácter 160 o después, así que el "
             "resumen de `buscar_nodos` (`harness.py:110-124`, `descripcion[:160]`) no muestra ninguna. "
             "Posiciones sobre la descripción en NFC; descripciones que cambian con NFC: " +
             ", ".join(f"{g} {m3[g]['descripciones_que_cambian_con_nfc']}" for g in m3) + ".\n")

    # medición 6
    m6 = res["medicion_6"]
    L.append("## Medición 6 — Prototipo del llenado por paso posterior en código (D-P6, D-COINC)\n")
    L.append("Acuerdo del prototipo contra `umbral` y `plazo` donde existen:\n")
    cats = ["total", "coincide", "coincide_y_unico_en_descripcion", "coincide_parcial", "difiere",
            "campo_sin_cuantia", "no_extrae", "no_extrae_y_campo_con_cuantia"]
    filas = []
    for g in m6:
        for t, a in m6[g]["acuerdo_contra_campo"]["por_tipo_campo"].items():
            filas.append([g, t] + [a[c2] for c2 in cats])
        a = m6[g]["acuerdo_contra_campo"]["total"]
        filas.append([g, "**total**"] + [a[c2] for c2 in cats])
    L.append(tabla(filas, ["Grafo", "Tipo.campo", "Total", "Coincide", "Coincide y único",
                           "Coincide parcial", "Difiere", "Campo sin cuantía", "No extrae",
                           "No extrae, con cuantía en el campo"]))
    L.append("\n«Coincide y único»: la descripción da un solo triple y es el del campo. «No extrae, con "
             "cuantía en el campo»: desglose de «no extrae» (D-COINC no cambia).\n")
    L.append("\nCobertura sobre los nodos de los cuatro tipos con cuantía (universo c14_eur, que contiene al "
             "de c14 literal), y casos no cubiertos:\n")
    cl = ["nodos", "en_c14_literal", "extrae_0", "extrae_1", "extrae_2_o_mas", "letras_compuestas",
          "relacional", "inconsistencia_cifra_letras"]
    filas = []
    for g in m6:
        for est, x in m6[g]["cobertura_cuatro_tipos"].items():
            filas.append([g, est] + [x.get(c2, "—") for c2 in cl])
    L.append(tabla(filas, ["Grafo", "Grupo", "Nodos", "En c14 literal", "Extrae 0", "Extrae 1",
                           "Extrae ≥2 (varios valores)", "Letras compuestas", "Relacional (D-REL y A-REL)",
                           "Cifra ≠ letras"]))
    L.append("\nGrupos «fuera_de_c14_eur_*»: nodos de los cuatro tipos sin cuantía según c14_eur de los que "
             "el prototipo sí extrae un valor (por ejemplo, la forma «2 (dos) años», con el número en letras entre paréntesis, que c14 no reconoce). "
             "Es un dato del prototipo; c14 no se modifica. Ejemplos y la lista de «difiere» y «coincide "
             "parcial» en el JSON, clave `medicion_6.<grafo>`.\n")

    # limita
    ml = res["limita"]
    L.append("## Aristas `limita` (insumo del atributo de la relación)\n")
    cl = ["limita_total", "limita_desde_Restriccion_con_umbral", "restricciones", "restricciones_con_umbral",
          "restricciones_con_umbral_sin_limita", "restricciones_con_limita",
          "restricciones_con_limita_sin_umbral_S18", "restricciones_con_mas_de_una_limita"]
    filas = [[g] + [ml[g][c2] for c2 in cl] for g in ml]
    L.append(tabla(filas, ["Grafo", "`limita`", "Desde Restriccion con umbral", "Restricciones",
                           "Con umbral", "Con umbral y sin `limita`", "Con `limita`",
                           "Con `limita` y sin umbral (S18)", "Con más de una `limita`"]))
    L.append("")
    for g in ml:
        x = ml[g]
        L.append(f"- **{g}.** Origen de `limita` por tipo: {x['limita_por_tipo_de_origen']}; destino: "
                 f"{x['limita_por_tipo_de_destino']}; por `Restriccion.tipo`: {x['limita_por_Restriccion_tipo']}. "
                 f"Con umbral y sin `limita`, por tipo: {x['restricciones_con_umbral_sin_limita_por_tipo']}; "
                 f"sus relaciones hacia Operacion: {x['restricciones_con_umbral_sin_limita_relaciones_a_operacion']}. "
                 f"Con `limita` y sin umbral, por tipo: {x['restricciones_con_limita_sin_umbral_por_tipo']}. "
                 f"`limita` por Restriccion: {x['distribucion_limita_por_restriccion']}. "
                 f"Condiciones con cuantía y sin `condicion_de`: "
                 + "; ".join(f"{v}: {c2['con_cuantia_sin_condicion_de']} de {c2['con_cuantia']} con cuantía "
                             f"({c2['condiciones']} Condicion)" for v, c2 in x["condiciones"].items()) + ".")
    L.append("")
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
    for g, nombre, ruta, sha in GRAFOS:
        s = sha256(REPO / ruta)
        if s != sha:
            raise SystemExit(f"sha256 de {ruta} = {s}; esperado {sha}. Se frena.")
        entradas["grafos"].append({"clave": g, "nombre": nombre, "ruta": ruta, "sha256": s})
        grafos[g] = json.load(open(REPO / ruta, encoding="utf-8"))

    man = json.load(open(REPO / MANIFIESTO, encoding="utf-8"))
    tos = [t["id"] for t in man["tos"]]
    chunks_por_to, chunks = {}, {}
    e0_sha, dev_ident = {}, {}
    for to in tos:
        p = REPO / E0_DIR / f"chunks_{to}.json"
        e0_sha[to] = sha256(p)
        lista = json.load(open(p, encoding="utf-8"))
        chunks_por_to[to] = lista
        for c in lista:
            chunks[c["id"]] = c
        if to in TOS_DEV:
            dev_ident[to] = sha256(REPO / E0_ENM01 / f"chunks_{to}.json") == e0_sha[to]
    entradas["e0"] = {"dir": E0_DIR, "sha256_por_to": e0_sha,
                      "chunks_total": len(chunks), "dev_identico_a_enm01": all(dev_ident.values())}

    pdfs_ok = True
    entradas["pdfs"] = {}
    for t in man["tos"]:
        s = sha256(REPO / t["pdf"])
        entradas["pdfs"][t["id"]] = {"pdf": t["pdf"], "sha256": s, "coincide_manifiesto": s == t["sha256_pdf"]}
        pdfs_ok &= s == t["sha256_pdf"]
    if not pdfs_ok:
        raise SystemExit("sha256 de algún PDF no coincide con el manifiesto. Se frena.")
    entradas["pdfs_ok"] = pdfs_ok

    src_h = (REPO / HARNESS).read_text(encoding="utf-8")
    entradas["harness_sha256"] = sha256(REPO / HARNESS)
    entradas["harness_max_len_160"] = "def _short_props(props: dict, max_len: int = 160)" in src_h
    entradas["e0_tablas_sha256"] = sha256(REPO / E0_TABLAS_DIR / "e0_tablas.py")

    sys.path.insert(0, str(REPO / E0_TABLAS_DIR))
    import e0_tablas  # noqa: E402 — se importa sin editar
    art_por_to = {t["id"]: e0_tablas.parsear_to(REPO / t["pdf"], t["id"]) for t in man["tos"]}

    nodos_por_chunk = {}
    for g, k in grafos.items():
        d = collections.defaultdict(list)
        for n in k["nodes"]:
            if n["type"] in TIPOS_NO_CONTENIDO:
                continue
            for cid in chunk_ids(n):
                d[cid].append(n)
        nodos_por_chunk[g] = d

    doc = __doc__.split("DECLARACIONES (fijadas antes de aplicar; se repiten en el .md):")[1]
    previas, agregados = doc.split("AGREGADOS TRAS LA CORRIDA DE PRUEBA", 1)
    agregados = agregados.split(":\n", 1)[1]

    def bloques(texto: str, pref: str) -> dict:
        out = {}
        for b in re.split(r"\n(?=" + pref + r"-[A-Z0-9-]+ · )", texto.strip()):
            nombre, cuerpo = b.split(" · ", 1)
            out[nombre.strip()] = re.sub(r"\s+", " ", cuerpo).strip()
        return out

    decl = bloques(previas, "D")
    agreg = bloques(agregados, "A")

    res = {
        "unidad": "U-UMBRAL",
        "etapa": "U1",
        "comando": "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/u_umbral_u1.py",
        "declaraciones": decl,
        "agregados_tras_corrida_de_prueba": agreg,
        "entradas": entradas,
        "medicion_1": medicion_1(grafos, chunks),
        "medicion_2": medicion_2(grafos, chunks_por_to, art_por_to, nodos_por_chunk, VARIANTES),
        "medicion_3": medicion_3(grafos),
        "medicion_6": medicion_6(grafos),
        "limita": medicion_limita(grafos),
    }
    (salida / "u1_mediciones.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (salida / "u1_mediciones.md").write_text(escribir_md(res), encoding="utf-8")
    print(f"escrito: {salida / 'u1_mediciones.json'}")
    print(f"escrito: {salida / 'u1_mediciones.md'}")


if __name__ == "__main__":
    main()
