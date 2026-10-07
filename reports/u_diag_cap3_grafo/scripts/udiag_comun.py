"""U-DIAG-CAP3-GRAFO: carga común de las fuentes (copias en src/, extraídas con git show d007be8:<ruta>).

Solo lee. No importa código del repo: las funciones de id de E2 (`slugify_full`, `_id_estable`,
`entity_slug_v3`, `entity_slug_r2`) se toman por AST de la copia de `e2_lib.py` y se ejecutan aisladas,
y `bloque_lista` / `es_item` / `rol_documental_de_punto` se toman igual de `prompt_r2b.py` y `comun_e1.py`.
"""
import ast
import glob
import hashlib
import json
import os
import re
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(AQUI, "src")
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
SHA = {
    "diez": "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57",
    "sincola": "e22fae1afc3cf37fbe5b49ee0b220d51d0ec5febc13abeb6ebf7b74226da34fb",
}
CONTENIDO = ("Operacion", "Restriccion", "Excepcion", "Obligacion", "Potestad", "Condicion", "Definicion")
NORMA = ("Obligacion", "Restriccion", "Operacion", "Potestad")


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def cargar_kg(nombre):
    p = os.path.join(SRC, "ens_diez" if nombre == "diez" else "ens_sincola", "kg.json")
    assert sha(p) == SHA[nombre], f"sha del grafo {nombre} distinto"
    return json.load(open(p, encoding="utf-8"))


def _funciones(path, nombres, extra_globals=None):
    src = open(path, encoding="utf-8").read()
    arbol = ast.parse(src)
    partes = []
    for nodo in arbol.body:
        if isinstance(nodo, ast.FunctionDef) and nodo.name in nombres:
            partes.append(ast.get_source_segment(src, nodo))
        elif isinstance(nodo, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id in nombres for t in nodo.targets):
            partes.append(ast.get_source_segment(src, nodo))
    g = {"re": re, "hashlib": hashlib, "unicodedata": unicodedata, "Any": object, "json": json}
    g.update(extra_globals or {})
    exec("from __future__ import annotations\n" + "\n\n".join(partes), g)
    return g


_E2 = _funciones(os.path.join(SRC, "code", "e2_lib.py"),
                 {"slugify_full", "_id_estable", "entity_slug_v3", "entity_slug_r2",
                  "TIPOS_POR_DESCRIPCION_R2", "TIPOS_POR_LABEL_Y_DESCRIPCION_R2", "FASES_R2"})
_PR = _funciones(os.path.join(SRC, "code", "comun_e1.py"), {"es_mini_chunk", "rol_documental_de_punto"})
_PB = _funciones(os.path.join(SRC, "code", "prompt_r2b.py"), {"bloque_lista", "es_item"},
                 {"es_mini_chunk": _PR["es_mini_chunk"]})
entity_slug_r2 = _E2["entity_slug_r2"]
bloque_lista = _PB["bloque_lista"]
es_item = _PB["es_item"]
es_mini_chunk = _PR["es_mini_chunk"]
rol_documental_de_punto = _PR["rol_documental_de_punto"]


def gid_de(e, prov):
    """Id del nodo que E2 r2b da a una entidad validada (e2_lib.ensamblar_r2)."""
    props = dict(e.get("properties") or {})
    if e["type"] == "TextoOrdenado":
        props.setdefault("archivo", prov["archivo"])
    return f"{e['type']}_{entity_slug_r2({'type': e['type'], 'label': e['label'], 'properties': props}, prov, 'r2b')}"


def leer_jsonl(p):
    out = []
    if not os.path.exists(p):
        return out
    with open(p, encoding="utf-8") as f:
        for linea in f:
            if linea.strip():
                out.append(json.loads(linea))
    return out


def last_wins(filas, clave="chunk_id"):
    return {r[clave]: r for r in filas}


def cargar_chunks():
    out = {}
    for t in TOS:
        for c in json.load(open(os.path.join(SRC, "e0_r2b", f"chunks_{t}.json"), encoding="utf-8")):
            out[c["id"]] = c
    return out


def chunk_base(cid, chunks):
    """El chunk de E0 de un chunk_id; las partes `::parteK` caen en su unidad entera."""
    if cid in chunks:
        return chunks[cid]
    return chunks[re.sub(r"::parte\d+$", "", cid)]


def cargar_salida(to):
    d = os.path.join(SRC, "salida_r2b", to)
    return {
        "e1": last_wins(leer_jsonl(os.path.join(d, "extracciones_e1.jsonl"))),
        "reint": {(r["chunk_id"], r["intento"]): r for r in leer_jsonl(os.path.join(d, "reintentos_e3.jsonl"))},
        "finales": last_wins(leer_jsonl(os.path.join(d, "finales.jsonl"))),
        "fin_r2": leer_jsonl(os.path.join(d, f"extracciones_finales_r2_{to}.jsonl")),
        "cola": {r["chunk_id"] for r in leer_jsonl(os.path.join(d, "cola_humana.jsonl"))},
    }


def crudo_aceptado(cid, sal):
    """El crudo que entra a E2 (runner_corpus.entrada_r2): el del reintento que aceptó E3 o el del intento 0."""
    fin = sal["finales"].get(cid)
    if fin is None:
        return None, None
    n = fin.get("n_reintentos") or 0
    cola = fin.get("validacion_final") is None
    if n and not cola:
        r = sal["reint"].get((cid, n))
        return (r or {}).get("tool_input"), f"reintento_{n}"
    return (sal["e1"].get(cid) or {}).get("tool_input_crudo"), "e1"


def vistos_e3(cid, sal):
    """Índices de relaciones del crudo aceptado que vio E3 (runner_corpus.vistos_por_e3), o None."""
    fin = sal["finales"].get(cid)
    if fin is None:
        return None
    cola = fin.get("validacion_final") is None
    val = (sal["e1"].get(cid) or {}).get("validacion") if cola else fin.get("validacion_final")
    if not val or val.get("forma_salida") != "r2":
        return None
    return {"entidades": {x["indice_crudo"] for x in val.get("entidades") or []},
            "relaciones": {x["indice_crudo"] for x in val.get("relaciones") or []},
            "rechazos_e1": val.get("rechazos") or []}


def tipo_unidad(c):
    """ítem / intro / chapeau / cierre / intersticial / punto (no ítem) / sección sin puntos."""
    if es_mini_chunk(c):
        return {"chapeau_seccion": "chapeau"}.get(c.get("rol_bloque"), c.get("rol_bloque"))
    if c["tipo"] == "seccion_sin_puntos":
        return "seccion_sin_puntos"
    return "item" if es_item(c) else "punto_no_item"


def norm(s):
    s = re.sub(r"-\s*\n\s*", "", s or "")
    s = re.sub("[“”«»‘’'\"]", "", s)
    s = re.sub("[–—]", "-", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def wilson(k, n, z=1.959963984540054):
    if n == 0:
        return (None, None)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    m = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)
    return (round((c - m) / d, 3), round((c + m) / d, 3))
