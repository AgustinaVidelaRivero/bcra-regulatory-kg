"""B6.1, tanda final, T3, punto 7.6: data/experiment/tanda_final/t3/muestras/unidades_a_la_vista_T4.json, desde las fichas del material
de las ocho muestras y el grafo de la tanda sin la cola, con data/experiment/tanda1/t4/scripts/unidades_a_la_vista_t4t1.py copiado y
adaptado. Solo lee.

  - Las ocho muestras: cola, aceptadas:items, aceptadas:no_items, vigilancia:2 y vigilancia:7 (material_t4_t3f_tf.py) y vigilancia:1,
    vigilancia:3 y observacion:12 (material_t4t1_tf.py), en <material>/<muestra>/.
  - La regla, la del punto 7.6 del «seguí» de T3: por muestra, el chunk_id de cada unidad cuya extracción aparece en el material y qué
    versión muestra («final», «primera» o «las dos»); la unidad de cada ficha de unidad (final) o de cola (primera, el primer intento);
    de un nodo que muestra una ficha, todas las unidades de su procedencia (`provenances`); de una arista, las de sus dos nodos.
    Los nodos que muestra una ficha: en una ficha de unidad, los suyos y los dos extremos de cada arista; en una de arista, sus dos
    nodos; en una de (1), el nodo Condicion y el otro nodo de cada arista; en una de (3), los nodos del grupo.
  - Como información, sin cambiar la regla: las unidades con la regla del T4 de la tanda 1 (decisión del 18/10/2026, punto 1.1: no
    suman un TextoOrdenado ni un Sujeto con más de una unidad de procedencia), y el control de las aristas que muestran las fichas de
    (1) y de la (12): cuántas tienen su unidad de procedencia fuera de la lista.
Uso: python3 -I -B unidades_a_la_vista_tf.py <raíz> <material> <doble_corrida_tf.json> <salida.json>
"""
import hashlib
import json
import sys
from collections import Counter, OrderedDict
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, MAT, DC, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3]), Path(sys.argv[4])
KG = RAIZ / "data/experiment/reextraccion_v2/corpus_tanda_final/ens_98_r2b_sincola/r2/kg.json"
dc = json.loads(DC.read_text(encoding="utf-8"))["doble_corrida"]["tf98_sincola"]
assert dc["kg_sha256"][0] == dc["kg_sha256"][1] and dc["carpeta"].endswith("ens_98_r2b_sincola")
KG_SHA = dc["kg_sha256"][0]
MUESTRAS = ["cola", "aceptadas:items", "aceptadas:no_items", "vigilancia:2", "vigilancia:7", "vigilancia:1", "vigilancia:3",
            "observacion:12"]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


kgb = KG.read_bytes()
assert sha(kgb) == KG_SHA
kg = json.loads(kgb)
nodos = {n["id"]: n for n in kg["nodes"]}
i3, i4 = (json.loads((MAT / n).read_text(encoding="utf-8")) for n in ("material_t4_t3f_tf.json", "material_t4t1_tf.json"))
assert set(i3["muestras"]) | set(i4["muestras"]) == set(MUESTRAS) and i3["grafo_sha256"] == i4["grafo_sha256"] == KG_SHA
hora = datetime.now().astimezone().isoformat(timespec="seconds")
assert datetime.fromisoformat(hora) > max(datetime.fromisoformat(i3["hora"]), datetime.fromisoformat(i4["hora"]))


def unidades_de(nid: str) -> set:
    return {p["chunk_id"] for p in (nodos[nid].get("provenances") or []) if p.get("chunk_id")}


def suma_1_1(nid: str) -> bool:
    t = nodos[nid]["type"]
    return not (t == "TextoOrdenado" or (t == "Sujeto" and len(unidades_de(nid)) > 1))


def nodos_de_la_ficha(x: dict) -> set:
    if "nodos" in x and "aristas" in x:                      # ficha de unidad (T3)
        return {n["id"] for n in x["nodos"]} | {a[k]["id"] for a in x["aristas"] for k in ("source", "target")}
    if "nodo" in x:                                          # ficha de (1)
        return {x["nodo"]["id"]} | {a["otro_nodo"]["id"] for a in x["aristas"]}
    if "grupo" in x:                                         # ficha de (3)
        return {n["id"] for n in x["nodos"]}
    return {x["origen"]["id"], x["destino"]["id"]}           # ficha de arista


def aristas_de_la_ficha(x: dict) -> list:
    if "nodo" in x:
        return [a.get("procedencia", {}).get("chunk_id") for a in x["aristas"]]
    if "origen" in x:
        return [x["arista"].get("procedencia", {}).get("chunk_id")]
    return []


res = OrderedDict([("hora", hora), ("grafo_sha256", KG_SHA),
                   ("material_t4_t3f_tf_sha256", sha((MAT / "material_t4_t3f_tf.json").read_bytes())),
                   ("material_t4t1_tf_sha256", sha((MAT / "material_t4t1_tf.json").read_bytes())),
                   ("regla", "la del punto 7.6 del «seguí» de T3: la unidad de cada ficha de unidad (final) o de cola (primera); de un "
                             "nodo que muestra una ficha, todas las unidades de su procedencia (final); de una arista, las de sus dos nodos"),
                   ("muestras", OrderedDict())])
union, union_11 = {}, set()
for m in MUESTRAS:
    nom = m.replace(":", "_")
    fichas = [json.loads(x) for x in (MAT / nom / f"fichas_{nom}.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    vis, por = {}, {}
    r11 = set()
    no_suman_11 = Counter()
    aristas_fuera = []

    def poner(cid: str, version: str, razon: str) -> None:
        vis.setdefault(cid, set()).add(version)
        por.setdefault(cid, set()).add(razon)
    for f in fichas:
        x = f["material"]
        if "entidades" in x:                                 # cola: primer intento
            poner(f["id"], "primera", "ficha de cola")
            r11.add(f["id"])
            continue
        if "nodos" in x and "aristas" in x:
            poner(f["id"], "final", "ficha de unidad")
            r11.add(f["id"])
        for nid in nodos_de_la_ficha(x):
            for cid in unidades_de(nid):
                poner(cid, "final", nodos[nid]["type"])
            if suma_1_1(nid):
                r11 |= unidades_de(nid)
            else:
                no_suman_11[nodos[nid]["type"] + (" (más de una unidad)" if nodos[nid]["type"] == "Sujeto" else "")] += 1
        aristas_fuera += [c for c in aristas_de_la_ficha(x) if c and c not in vis]
    filas = [{"chunk_id": c, "version": ("las dos" if len(vis[c]) == 2 else next(iter(vis[c]))), "por": sorted(por[c])}
             for c in sorted(vis)]
    res["muestras"][m] = OrderedDict([
        ("fichas", len(fichas)), ("unidades_a_la_vista", len(filas)), ("por_version", dict(Counter(r["version"] for r in filas))),
        ("por_razon", dict(Counter(z for r in filas for z in r["por"]).most_common())),
        ("informacion_con_la_regla_1_1_de_la_tanda_1", len(r11)),
        ("informacion_nodos_que_no_suman_con_la_regla_1_1", dict(no_suman_11.most_common())),
        ("informacion_aristas_con_su_unidad_fuera_de_la_lista", len(aristas_fuera)),
        ("unidades", filas)])
    for c, v in vis.items():
        union.setdefault(c, set()).update(v)
    union_11 |= r11
res["todas_las_muestras"] = OrderedDict([
    ("unidades_a_la_vista", len(union)),
    ("por_version", dict(Counter("las dos" if len(v) == 2 else next(iter(v)) for v in union.values()))),
    ("informacion_con_la_regla_1_1_de_la_tanda_1", len(union_11))])
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for m, x in res["muestras"].items():
    print(f"{m}: {x['fichas']} fichas → {x['unidades_a_la_vista']} unidades {x['por_version']} {x['por_razon']}; con la regla 1.1 "
          f"{x['informacion_con_la_regla_1_1_de_la_tanda_1']} (no suman {x['informacion_nodos_que_no_suman_con_la_regla_1_1']}); aristas "
          f"con su unidad fuera {x['informacion_aristas_con_su_unidad_fuera_de_la_lista']}")
print("todas:", dict(res["todas_las_muestras"]), "| hora", hora, "| sha256", sha(OUT.read_bytes()))
