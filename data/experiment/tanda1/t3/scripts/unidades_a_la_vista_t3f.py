"""B6.1, tanda 1, T3, punto 7.6: data/experiment/tanda1/t3/muestras/unidades_a_la_vista_T4.json, desde las fichas del material (lo que
T4 muestra) y el grafo sin cola. Decisión de la autora del 17/10/2026, para U-MED-VERIF (registro, decisión 9 del 18/10/2026): toda
unidad cuya extracción aparece en el material de T4, en cualquier versión, y cuál.
  - Por muestra, el chunk_id de cada unidad a la vista y qué versión muestra el material: «final» (el grafo sin cola), «primera» (el
    primer intento, en la cola) o «las dos».
  - Una unidad de una ficha de unidad está a la vista, con la versión de su ficha. De un nodo que muestra una ficha, todas las unidades de
    su procedencia (`provenances`); de una arista, las de sus dos nodos. En las fichas de la cola no hay nodos del grafo: está a la vista
    la unidad, en su primera versión.
  - Como información, sin cambiar la regla: cuántas unidades quedan a la vista solo por un nodo TextoOrdenado o Sujeto (su procedencia
    es la del TO entero o la de todas las menciones de un sujeto fusionado).
  - T4 le suma después lo que agregue la ampliación.
Uso: python3 -I -B unidades_a_la_vista_t3f.py <raíz> <material> <salida.json>
"""
import hashlib
import json
import sys
from collections import Counter, OrderedDict
from datetime import datetime
from pathlib import Path

RAIZ, MAT, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3])
KG = RAIZ / "data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b_sincola/r2/kg.json"
KG_SHA = "384a6d5bc139cd7b74d86840c68e7034b7a9bcb4bc26da7c61567f3f053e624e"
AMPLIOS = ("TextoOrdenado", "Sujeto")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


kgb = KG.read_bytes()
assert sha(kgb) == KG_SHA
kg = json.loads(kgb)
nodos = {n["id"]: n for n in kg["nodes"]}
mat = json.loads((MAT / "material_t4.json").read_text(encoding="utf-8"))
hora = datetime.now().astimezone().isoformat(timespec="seconds")
assert datetime.fromisoformat(hora) > datetime.fromisoformat(mat["hora"])


def unidades_de(nid: str) -> set:
    return {p["chunk_id"] for p in (nodos[nid].get("provenances") or []) if p.get("chunk_id")}


res = OrderedDict([("hora", hora), ("grafo_sha256", KG_SHA), ("material_t4_sha256", sha((MAT / "material_t4.json").read_bytes())),
                   ("regla", "de un nodo, todas las unidades de su procedencia; de una arista, las de sus dos nodos; la unidad de cada ficha "
                             "de unidad, con su versión"), ("muestras", OrderedDict())])
union = {}
for m in mat["muestras"]:
    nom = m.replace(":", "_")
    fichas = [json.loads(x) for x in (MAT / nom / f"fichas_{nom}.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    vis, via = {}, {}

    def poner(cid: str, version: str, por: str) -> None:
        vis.setdefault(cid, set()).add(version)
        via.setdefault(cid, set()).add(por)
    for f in fichas:
        x = f["material"]
        if "entidades" in x:                      # cola: primer intento
            poner(f["id"], "primera", "unidad de la ficha")
            continue
        if "nodos" in x:                          # ficha de unidad
            poner(f["id"], "final", "unidad de la ficha")
            ids = {n["id"] for n in x["nodos"]} | {a[k]["id"] for a in x["aristas"] for k in ("source", "target")}
        else:                                     # ficha de arista
            ids = {x["origen"]["id"], x["destino"]["id"]}
        for nid in ids:
            for cid in unidades_de(nid):
                poner(cid, "final", nodos[nid]["type"])
    filas = sorted(({"chunk_id": c, "version": ("las dos" if len(v) == 2 else next(iter(v)))} for c, v in vis.items()),
                   key=lambda r: r["chunk_id"])
    solo_amplios = sorted(c for c, p in via.items() if p <= set(AMPLIOS))
    res["muestras"][m] = OrderedDict([("fichas", len(fichas)), ("unidades_a_la_vista", len(filas)),
                                      ("por_version", dict(Counter(r["version"] for r in filas))),
                                      ("informacion_solo_por_TextoOrdenado_o_Sujeto", len(solo_amplios)), ("unidades", filas)])
    for c, v in vis.items():
        union.setdefault(c, set()).update(v)
res["todas_las_muestras"] = {"unidades_a_la_vista": len(union),
                             "por_version": dict(Counter("las dos" if len(v) == 2 else next(iter(v)) for v in union.values()))}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for m, x in res["muestras"].items():
    print(f"{m}: {x['fichas']} fichas → {x['unidades_a_la_vista']} unidades {x['por_version']}; solo por TextoOrdenado o Sujeto "
          f"{x['informacion_solo_por_TextoOrdenado_o_Sujeto']}")
print("todas:", res["todas_las_muestras"], "| hora", hora, "| sha256", sha(OUT.read_bytes()))
