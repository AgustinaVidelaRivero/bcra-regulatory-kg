"""B6.1, tanda 1, T4, primer tramo, punto 5: data/experiment/tanda1/t3/muestras/unidades_a_la_vista_T4.json (la ruta del mandato firmado
de U-MED-VERIF-FICHAS, que T4 completa), desde las fichas del material de las ocho muestras que se leen y el grafo sin cola, con la regla
de la decisión de la autora del 18/10/2026 (punto 1.1). Solo lee.

  - Las ocho muestras: cola, aceptadas:items, aceptadas:no_items, vigilancia:2 y vigilancia:7 (material de T3,
    tanda1/t3/muestras/material/) y vigilancia:1, vigilancia:3 y la observacion:12 rehecha (material de este tramo,
    tanda1/t4/muestras/material/). La observación (12) de T3 no se lee y no entra.
  - La regla (punto 1.1): suma la extracción propia de cada unidad, en cualquier versión:
      - la unidad de cada ficha de unidad (versión final) o de cola (versión primera, el primer intento);
      - las unidades de procedencia (`provenances`) de todo otro nodo que muestre una ficha, incluido un Sujeto con una sola unidad de
        procedencia (versión final: el grafo sin cola);
      - no suma un nodo TextoOrdenado (su procedencia es el TO entero) ni un Sujeto con más de una unidad de procedencia (un sujeto
        fusionado: su procedencia son todas sus menciones).
    Los nodos que muestra una ficha: en una ficha de unidad, los suyos y los dos extremos de cada arista; en una de arista, sus dos
    nodos; en una de (1), el nodo Condicion y el otro nodo de cada arista; en una de (3), los nodos del grupo.
  - Por muestra: el chunk_id de cada unidad, qué versión muestra («final», «primera» o «las dos») y por qué la suma: «ficha de unidad»,
    «ficha de cola» o el tipo del nodo.
  - Como información, sin cambiar la regla:
      - las unidades que quedarían con la regla de T3 (todas las unidades de procedencia de todo nodo, sin excepciones);
      - el control de las aristas que muestran las fichas de (1) y de la (12): cuántas tienen su unidad de procedencia fuera de la lista.
  - No calcula si quedan 30 en la población de U-MED-VERIF.
Uso: python3 -I -B unidades_a_la_vista_t4t1.py <raíz> <material de T3> <material de T4> <salida.json>
"""
import hashlib
import json
import sys
from collections import Counter, OrderedDict
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, MAT3, MAT4, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve(), Path(sys.argv[4])
KG = RAIZ / "data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b_sincola/r2/kg.json"
KG_SHA = "384a6d5bc139cd7b74d86840c68e7034b7a9bcb4bc26da7c61567f3f053e624e"
MAT3_SHA = "b90a7c5ba48384784b8ca70644e41dc271898adb124ec71734aae758cec26196"  # material_t4.json de T3 (FRENO T3, §9)
MUESTRAS = [("cola", MAT3), ("aceptadas:items", MAT3), ("aceptadas:no_items", MAT3), ("vigilancia:2", MAT3), ("vigilancia:7", MAT3),
            ("vigilancia:1", MAT4), ("vigilancia:3", MAT4), ("observacion:12", MAT4)]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


kgb = KG.read_bytes()
assert sha(kgb) == KG_SHA
kg = json.loads(kgb)
nodos = {n["id"]: n for n in kg["nodes"]}
i3, i4 = (json.loads((d / n).read_text(encoding="utf-8")) for d, n in ((MAT3, "material_t4.json"), (MAT4, "material_t4_tramo1.json")))
hora = datetime.now().astimezone().isoformat(timespec="seconds")
assert datetime.fromisoformat(hora) > max(datetime.fromisoformat(i3["hora"]), datetime.fromisoformat(i4["hora"]))


def unidades_de(nid: str) -> set:
    return {p["chunk_id"] for p in (nodos[nid].get("provenances") or []) if p.get("chunk_id")}


def suma(nid: str) -> bool:
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
                   ("material_t4_T3_sha256", sha((MAT3 / "material_t4.json").read_bytes())),
                   ("material_t4_tramo1_sha256", sha((MAT4 / "material_t4_tramo1.json").read_bytes())),
                   ("regla", "decisión de la autora del 18/10/2026 (punto 1.1): la unidad de cada ficha de unidad (final) o de cola "
                             "(primera); las unidades de procedencia de todo otro nodo que muestre una ficha (final), incluido un Sujeto "
                             "con una sola unidad de procedencia; no suman un TextoOrdenado ni un Sujeto con más de una unidad de "
                             "procedencia"),
                   ("muestras", OrderedDict())])
assert res["material_t4_T3_sha256"] == MAT3_SHA, "el material de T3 no es el del T3a"
union, union_t3 = {}, set()
for m, MAT in MUESTRAS:
    nom = m.replace(":", "_")
    fichas = [json.loads(x) for x in (MAT / nom / f"fichas_{nom}.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    vis, por = {}, {}
    t3 = set()
    no_suman = Counter()
    aristas_fuera = []

    def poner(cid: str, version: str, razon: str) -> None:
        vis.setdefault(cid, set()).add(version)
        por.setdefault(cid, set()).add(razon)
    for f in fichas:
        x = f["material"]
        if "entidades" in x:                                 # cola: primer intento
            poner(f["id"], "primera", "ficha de cola")
            t3.add(f["id"])
            continue
        if "nodos" in x and "aristas" in x:
            poner(f["id"], "final", "ficha de unidad")
            t3.add(f["id"])
        for nid in nodos_de_la_ficha(x):
            t3 |= unidades_de(nid)
            if not suma(nid):
                no_suman[nodos[nid]["type"] + (" (más de una unidad)" if nodos[nid]["type"] == "Sujeto" else "")] += 1
                continue
            for cid in unidades_de(nid):
                poner(cid, "final", nodos[nid]["type"])
        aristas_fuera += [c for c in aristas_de_la_ficha(x) if c and c not in vis]
    filas = [{"chunk_id": c, "version": ("las dos" if len(vis[c]) == 2 else next(iter(vis[c]))), "por": sorted(por[c])}
             for c in sorted(vis)]
    res["muestras"][m] = OrderedDict([
        ("material", "tanda1/t3/muestras/material" if MAT == MAT3 else "tanda1/t4/muestras/material"),
        ("fichas", len(fichas)), ("unidades_a_la_vista", len(filas)), ("por_version", dict(Counter(r["version"] for r in filas))),
        ("por_razon", dict(Counter(z for r in filas for z in r["por"]).most_common())),
        ("nodos_mostrados_que_no_suman", dict(no_suman.most_common())),
        ("informacion_con_la_regla_de_T3", len(t3)),
        ("informacion_aristas_con_su_unidad_fuera_de_la_lista", len(aristas_fuera)),
        ("unidades", filas)])
    for c, v in vis.items():
        union.setdefault(c, set()).update(v)
    union_t3 |= t3
res["todas_las_muestras"] = OrderedDict([
    ("unidades_a_la_vista", len(union)),
    ("por_version", dict(Counter("las dos" if len(v) == 2 else next(iter(v)) for v in union.values()))),
    ("informacion_con_la_regla_de_T3", len(union_t3))])
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for m, x in res["muestras"].items():
    print(f"{m}: {x['fichas']} fichas → {x['unidades_a_la_vista']} unidades {x['por_version']} {x['por_razon']}; no suman "
          f"{x['nodos_mostrados_que_no_suman']}; con la regla de T3 {x['informacion_con_la_regla_de_T3']}; aristas con su unidad fuera "
          f"{x['informacion_aristas_con_su_unidad_fuera_de_la_lista']}")
print("todas:", dict(res["todas_las_muestras"]), "| hora", hora, "| sha256", sha(OUT.read_bytes()))
