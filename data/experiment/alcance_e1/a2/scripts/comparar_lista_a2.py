"""U-ALCANCE-E1, A2: compara la lista de la tanda 1 que regenera lote_tramo1_S2.sh (sobre la E0 corregida y el registro de
alcance de HEAD) con la commiteada (data/experiment/segmentacion_oficial_e0r2/s2/lista_tanda1_S2.json), clave por clave y
fila por fila, y dice qué difiere. Solo lee. Uso: python3 -I -B comparar_lista_a2.py <regenerada> <commiteada> <salida.json>"""
import json
import sys
from pathlib import Path

a, b = (json.loads(Path(p).read_text(encoding="utf-8")) for p in sys.argv[1:3])
res = {"claves_iguales": list(a) == list(b), "claves_distintas": [k for k in a if a[k] != b.get(k)],
       "fuentes_distintas": [], "filas_distintas": []}
for g in a["fuentes"]:
    for f in a["fuentes"][g]:
        if a["fuentes"][g][f] != b["fuentes"][g].get(f):
            res["fuentes_distintas"].append({"grupo": g, "archivo": f, "commiteada": b["fuentes"][g].get(f),
                                             "regenerada": a["fuentes"][g][f]})
for fa, fb in zip(a["filas"], b["filas"]):
    if fa != fb:
        res["filas_distintas"].append({"to": fa["to"], "campos": {k: {"commiteada": fb.get(k), "regenerada": fa.get(k)}
                                                                  for k in fa if fa.get(k) != fb.get(k)}})
res["lista_final_igual"] = a["lista_final"] == b["lista_final"]
res["U_igual"] = a["U"] == b["U"]
res["filas_mismo_orden_y_cantidad"] = [f["to"] for f in a["filas"]] == [f["to"] for f in b["filas"]]
Path(sys.argv[3]).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k != "filas_distintas"}, ensure_ascii=False)[:800])
print("filas distintas:", [(f["to"], list(f["campos"])) for f in res["filas_distintas"]])
