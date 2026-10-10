"""U-OMISIONES-COD, O2 — grupo C caso por caso sobre el grafo de O2: cada elemento de umbral que tiene base en HEAD, con su
estado en HEAD y en O2 (resuelta, marcada o sin base), su unidad, su origen y su base. Es la lista de los límites de C: las
marcadas («base no resuelta», límite declarado de la v7) y las que quedan sin base (g1). Reusa `estado_base`,
`es_validador` y `chunk_de` de `o1/scripts/medir_grupos_C_L.py`; los ids que G-r cambia se emparejan por tipo y etiqueta.
Solo lee. Uso: python3 -I limites_C_O2.py <r2 HEAD> <r2 O2> --o1-scripts <dir o1/scripts> --out <json>"""
import argparse
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("head", type=Path)
ap.add_argument("o2", type=Path)
ap.add_argument("--o1-scripts", type=Path, required=True)
ap.add_argument("--out", type=Path, required=True)
a = ap.parse_args()
sys.dont_write_bytecode = True  # el módulo se importa del repo: no escribir __pycache__ ahí
sys.path.insert(0, str(a.o1_scripts))
import medir_grupos_C_L as CL  # noqa: E402

A = json.loads((a.head / "kg.json").read_text(encoding="utf-8"))
B = json.loads((a.o2 / "kg.json").read_text(encoding="utf-8"))
na, nb = {n["id"]: n for n in A["nodes"]}, {n["id"]: n for n in B["nodes"]}
por = {}
for i in set(na) - set(nb):
    por.setdefault((na[i]["type"], na[i]["label"]), []).append(i)
ren = {por[(nb[j]["type"], nb[j]["label"])][0]: j for j in set(nb) - set(na)
       if len(por.get((nb[j]["type"], nb[j]["label"]), [])) == 1}
ea = {(ren.get(k[0], k[0]), k[1]): v for k, v in CL.elementos(A).items()}
eb = CL.elementos(B)
filas = []
for k in sorted(ea):
    (n0, x0) = ea[k]
    if not x0.get("base"):
        continue
    if k not in eb:
        filas.append({"nodo": k[0], "i": k[1], "falta_en_o2": True})
        continue
    (n1, x1) = eb[k]
    filas.append(OrderedDict([("nodo", k[0]), ("i", k[1]), ("unidad", CL.chunk_de(n1)),
                              ("origen", "validador" if CL.es_validador(x0) else x0.get("origen")),
                              ("estado_head", CL.estado_base(x0)), ("estado_o2", CL.estado_base(x1)),
                              ("base_head", x0.get("base")), ("base_o2", x1.get("base")),
                              ("destino_o2", x1.get("base_destino")), ("via_o2", x1.get("base_via")),
                              ("cuantia_o2", f'{x1.get("valor")} {x1.get("unidad")}')]))
res = OrderedDict([
    ("elementos_con_base_en_head", len(filas)),
    ("faltan_en_o2", [f for f in filas if f.get("falta_en_o2")]),
    ("por_estado_o2", dict(Counter(f.get("estado_o2") for f in filas))),
    ("por_estado_o2_y_origen", {f"{e}|{o}": n for (e, o), n in sorted(Counter((f.get("estado_o2"), f.get("origen"))
                                                                         for f in filas).items())}),
    ("resueltas", [f for f in filas if f.get("estado_o2") == "resuelta"]),
    ("marcadas", [f for f in filas if f.get("estado_o2") == "marcada"]),
    ("sin_base", [f for f in filas if f.get("estado_o2") == "sin_base"])])
a.out.parent.mkdir(parents=True, exist_ok=True)
a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k not in ("resueltas", "marcadas", "sin_base")}, ensure_ascii=False))
for f in res["resueltas"]:
    print("  resuelta:", f["unidad"], "->", f["destino_o2"], f["via_o2"], f["origen"])
