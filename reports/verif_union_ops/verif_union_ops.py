"""VERIF-UNION-OPERACIONES: unión de las Operacion por etiqueta en
KG-Tanda0-Desarrollo-r2a. Solo lee el repo; escribe en el directorio que se
le pasa como argumento (scratchpad).

Uso, desde la raíz del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B <scratchpad>/verif_union_ops.py <dir_salida>

Fuentes:
  - grafo: data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2a/r2/kg.json
  - crudo validado de cada unidad: salida_dirigida/<to>/finales.jsonl
    (validacion_final) y, para la cola humana, extracciones_e1_compact.jsonl
    (la misma selección que entrada_r2, runner_corpus.py@f8dedd4:903-943, el
    commit que generó el grafo);
  - texto de las unidades: e0_chunking/salida_tanda0/chunks_<to>.json (el E0
    del manifiesto tanda0_ens_desarrollo, que ensamblar_tanda0 usa).
La clave de unión se recalcula con la copia de entity_slug_v3 de e2_lib.py
(líneas 90-121), copiada abajo sin cambios de lógica.
"""
import collections
import hashlib
import itertools
import json
import random
import re
import sys
import unicodedata
from pathlib import Path

sys.dont_write_bytecode = True
OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
KG = Path("data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2a/r2/kg.json")
CRUDO = Path("data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida")
E0 = Path("data/experiment/reextraccion_v2/e0_chunking/salida_tanda0")
TOS = ("pro", "cla", "ric", "cap", "ext")
SEMILLA = 20261004
N_MUESTRA = 20


def slugify_full(s):
    if not s:
        return "empty"
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")
    return s or "empty"


def id_operacion(label, tipo):
    full = slugify_full(label or str(tipo or ""))
    return "Operacion_" + f"{full[:80]}_{hashlib.sha1(full.encode('utf-8')).hexdigest()[:6]}"


def jsonl(p):
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


crudo_kg = KG.read_bytes()
kg = json.loads(crudo_kg.decode("utf-8"))
print("sha256 kg.json", hashlib.sha256(crudo_kg).hexdigest())
ops = [n for n in kg["nodes"] if n["type"] == "Operacion"]
OPS = {n["id"]: n for n in ops}

chunks = {}
for to in TOS:
    for c in json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8")):
        chunks[c["id"]] = c

# Instancias de Operacion en el crudo validado, con la selección de entrada_r2.
inst = collections.defaultdict(list)
for to in TOS:
    fin = {r["chunk_id"]: r for r in jsonl(CRUDO / to / "finales.jsonl")}
    e1 = {r["chunk_id"]: r for r in jsonl(CRUDO / to / "extracciones_e1_compact.jsonl")}
    for cid, r in fin.items():
        val = r.get("validacion_final") or (e1.get(cid) or {}).get("validacion")
        if not val:
            continue
        for e in val["entidades"]:
            if e["type"] != "Operacion":
                continue
            p = e.get("properties") or {}
            inst[(to, id_operacion(e.get("label"), p.get("tipo")))].append(
                {"chunk_id": cid, "label": e.get("label"), "tipo": p.get("tipo"),
                 "descripcion": p.get("descripcion")})


def to_de(n):
    return n["provenances"][0]["to"]


def base_id(n):
    """Id sin el sufijo `__<to>` de la colisión entre TOs. Solo el sufijo final:
    un id con el prefijo de 80 caracteres terminado en `_` también lleva `__`."""
    for to in TOS:
        if n["id"].endswith("__" + to):
            return n["id"][: -len("__" + to)]
    return n["id"]


# Control: cada procedencia de cada nodo tiene su instancia en el crudo.
faltan, sobran = [], 0
for n in ops:
    lst = inst.get((to_de(n), base_id(n)), [])
    cids = [i["chunk_id"] for i in lst]
    for p in n["provenances"]:
        if p["chunk_id"] not in cids:
            faltan.append((n["id"], p["chunk_id"]))
    sobran += len(lst) - len(n["provenances"])
print("control crudo->grafo: procedencias sin instancia", len(faltan), faltan[:5],
      "| instancias de mas", sobran)
print("instancias de Operacion en el crudo validado", sum(len(v) for v in inst.values()),
      "| claves (to, id)", len(inst), "| nodos Operacion", len(ops))

# Tarea 1.
print("\n[t1] por documento")
filas = []
for to in TOS:
    nn = [n for n in ops if to_de(n) == to]
    ii = [i for (t, _), v in inst.items() if t == to for i in v]
    multi_punto = [n for n in nn if len({p["punto"] for p in n["provenances"]}) > 1]
    multi_chunk = [n for n in nn if len({p["chunk_id"] for p in n["provenances"]}) > 1]
    fila = {"to": to, "instancias": len(ii), "nodos": len(nn),
            "etiquetas_distintas_nodo": len({n["label"] for n in nn}),
            "etiquetas_crudas_distintas": len({i["label"] for i in ii}),
            "etiquetas_normalizadas_distintas": len({slugify_full(i["label"]) for i in ii}),
            "uniones": sum(len(n["provenances"]) - 1 for n in nn),
            "nodos_mas_de_un_punto": len(multi_punto),
            "nodos_mas_de_una_unidad": len(multi_chunk),
            "uniones_entre_puntos": sum(len({p["punto"] for p in n["provenances"]}) - 1 for n in multi_punto)}
    filas.append(fila)
    print(json.dumps(fila, ensure_ascii=False))
tot = {k: sum(f[k] for f in filas) for k in filas[0] if k != "to"}
print("total", json.dumps(tot, ensure_ascii=False))
print("colision cross-TO:", [n["id"] for n in ops if n["properties"].get("colision_cross_to") == "true"])
print("variantes crudas dentro de un nodo (misma clave, etiqueta distinta):",
      sum(1 for v in inst.values() if len({i["label"] for i in v}) > 1))


def texto_unidad(cid):
    c = chunks.get(cid)
    if c is None:
        return None
    her = " | ".join(h.get("texto", "") for h in c.get("herencia") or [])
    return {"herencia": her, "texto": c["texto"]}


# Tarea 2: las operaciones con procedencias de más de un punto.
t2 = []
for n in ops:
    if len({p["punto"] for p in n["provenances"]}) > 1:
        lst = inst[(to_de(n), base_id(n))]
        t2.append({"id": n["id"], "label": n["label"], "to": to_de(n),
                   "procedencias": [{"chunk_id": p["chunk_id"], "punto": p["punto"],
                                     "rol_documental": p["rol_documental"]} for p in n["provenances"]],
                   "instancias": lst,
                   "textos": {i["chunk_id"]: texto_unidad(i["chunk_id"]) for i in lst}})
(OUT / "t2_insumo.json").write_text(json.dumps(t2, ensure_ascii=False, indent=1), encoding="utf-8")
print("\n[t2] operaciones con mas de un punto", len(t2))

# Tarea 3: regla de pares no unidos.
STOP = {"de", "del", "la", "las", "el", "los", "y", "o", "u", "e", "a", "al", "en", "por", "para",
        "con", "sin", "que", "su", "sus", "un", "una", "unos", "unas", "se", "sobre", "entre",
        "segun", "como", "mas", "otro", "otros", "otra", "otras", "lo"}


def plegar(t):
    if len(t) > 4 and t.endswith("es") and t[-3] in "lnrdzj":
        return t[:-2]
    if len(t) > 3 and t.endswith("s"):
        return t[:-1]
    return t


def palabras(label):
    return frozenset(plegar(t) for t in slugify_full(label).split("_") if t and t not in STOP)


pares = []
for to in TOS:
    nn = sorted((n for n in ops if to_de(n) == to), key=lambda n: n["id"])
    for a, b in itertools.combinations(nn, 2):
        A, B = palabras(a["label"]), palabras(b["label"])
        com = A & B
        if A and B and 2 * len(com) > len(A) and 2 * len(com) > len(B):
            pares.append({"to": to, "a": a["id"], "b": b["id"], "label_a": a["label"], "label_b": b["label"],
                          "comunes": sorted(com), "solo_a": sorted(A - B), "solo_b": sorted(B - A),
                          "iguales_tras_plegar": A == B})
print("\n[t3] palabras vacias", len(STOP))
print("[t3] pares candidatos", len(pares), dict(collections.Counter(p["to"] for p in pares)),
      "| con el mismo conjunto de palabras", sum(p["iguales_tras_plegar"] for p in pares))
rng = random.Random(SEMILLA)
muestra = rng.sample(range(len(pares)), N_MUESTRA)
print("semilla", SEMILLA, "indices de la muestra", muestra)
t3 = []
for k in muestra:
    p = pares[k]
    item = {"indice": k, **p, "instancias": {}, "textos": {}}
    for lado in ("a", "b"):
        n = OPS[p[lado]]
        lst = inst[(to_de(n), base_id(n))]
        item["instancias"][lado] = lst
        for i in lst:
            item["textos"][i["chunk_id"]] = texto_unidad(i["chunk_id"])
    t3.append(item)
(OUT / "t3_pares_todos.json").write_text(json.dumps(pares, ensure_ascii=False, indent=1), encoding="utf-8")
(OUT / "t3_muestra_insumo.json").write_text(json.dumps(t3, ensure_ascii=False, indent=1), encoding="utf-8")

# Tarea 4: el ejemplo.
print("\n[t4] cla::5.1.1 y cla::5.1.1.1")
for cid in sorted(c for c in chunks if c.startswith("cla::5.1.1")):
    print(" unidad", cid, "| tipo", chunks[cid].get("tipo"))
for n in ops:
    cs = {p["chunk_id"] for p in n["provenances"]}
    if cs & {"cla::5.1.1::intro", "cla::5.1.1", "cla::5.1.1.1"}:
        print(" ", n["id"], "|", n["label"], "|", sorted(cs), "|", n["properties"])
for (to, gid), lst in inst.items():
    for i in lst:
        if i["chunk_id"] in ("cla::5.1.1::intro", "cla::5.1.1", "cla::5.1.1.1"):
            print("  crudo", i["chunk_id"], "|", i["label"], "|", i["tipo"], "|", i["descripcion"], "->", gid)
EJ = ("cla::5.1.1::intro", "cla::5.1.1.1")
fin_cla = {r["chunk_id"]: r for r in jsonl(CRUDO / "cla" / "finales.jsonl")}
for cid in EJ:
    val = fin_cla[cid].get("validacion_final") or {}
    print(" entidades del crudo de", cid, "| estado", fin_cla[cid]["estado"], "|",
          [(e["type"], e.get("label")) for e in val.get("entidades", [])])
for n in kg["nodes"]:
    cs = {p.get("chunk_id") for p in n["provenances"]}
    if n["type"] not in ("Sujeto", "TextoOrdenado") and cs & set(EJ):
        print(" nodo de contenido", n["type"], "|", n["label"], "|", sorted(cs & set(EJ)))
ids_ej = {n["id"] for n in ops if {p["chunk_id"] for p in n["provenances"]} & set(EJ)}
print(" pares candidatos de la regla que tocan esas Operacion:", sum(1 for p in pares if {p["a"], p["b"]} & ids_ej))
print(" textos:", json.dumps({cid: texto_unidad(cid) for cid in EJ}, ensure_ascii=False))
dist = [n for n in ops if len({p["punto"] for p in n["provenances"]}) > 1]
print("\n[control] uniones de los 37: suma(procedencias-1)", sum(len(n["provenances"]) - 1 for n in dist),
      "| suma(puntos distintos-1)", sum(len({p["punto"] for p in n["provenances"]}) - 1 for n in dist))
mismo = [n for n in ops if len(n["provenances"]) > 1 and len({p["punto"] for p in n["provenances"]}) == 1]
print("[control] nodos con varias procedencias del mismo punto:", len(mismo),
      [(n["label"], [(p["chunk_id"], p["rol_documental"]) for p in n["provenances"]]) for n in mismo])
