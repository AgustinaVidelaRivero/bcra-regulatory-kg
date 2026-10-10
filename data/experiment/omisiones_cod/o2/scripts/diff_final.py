"""U-OMISIONES-COD, O2 — la versión del diff declarado que va a `omisiones_cod/o2/salidas/`: la de `diff_declarado.py`, con la
causa «J» de las `remite_a` que siguen separada por la corrida sin J (`j_descomposicion.py`): «J» si el cambio es solo de J,
«J y G-r» si también cambia de HEAD a sin J, y «G-r» si cambia solo de HEAD a sin J (la procedencia del primer nodo de un grupo
con un nodo de G-r). Recuenta las causas y escribe una fila por línea. Solo lee sus entradas.
Uso: python3 -I diff_final.py <diff_declarado.json> <j_descomposicion.json> --out <json>"""
import json, sys
from collections import Counter
from pathlib import Path
d = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")); j = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
out = Path(sys.argv[4])
L = j["listas"]; solo_j, j_gr, solo_gr = set(L["solo_J"]), set(L["J_y_G_r"]), set(L["solo_G_r"])
assert solo_j.isdisjoint(j_gr) and solo_j.isdisjoint(solo_gr) and j_gr.isdisjoint(solo_gr)
n = 0
for x in d["lista"]:
    if x["objeto"] == "arista" and x["causa"] == "J":
        c = x["clave"]
        x["causa"] = "J" if c in solo_j else "J y G-r" if c in j_gr else "G-r" if c in solo_gr else "sin_causa"
        if x["causa"] == "G-r":
            x["detalle"] = "procedencia del primer nodo de un grupo con un nodo de G-r (cambia sin J)"
        n += 1
cnt = Counter(f'{x["objeto"]}|{x["cambio"].split(" ")[0]}|{x["causa"]}' for x in d["lista"])
d["por_objeto_cambio_y_causa"] = dict(sorted(cnt.items()))
d["sin_causa"] = [x for x in d["lista"] if x["causa"] == "sin_causa"]
d["nota"] = ("causa «J» separada con la corrida sin J (j_aislado_<grafo>.json, j_descomposicion_<grafo>.json): "
             f"{n} filas revisadas")
cab = {k: v for k, v in d.items() if k != "lista"}
txt = json.dumps(cab, ensure_ascii=False, indent=1)[:-2] + ',\n "lista": [\n' + \
      ",\n".join(json.dumps(x, ensure_ascii=False) for x in d["lista"]) + "\n ]\n}\n"
json.loads(txt)
out.write_text(txt, encoding="utf-8")
print(json.dumps(d["por_objeto_cambio_y_causa"], ensure_ascii=False), "sin_causa", len(d["sin_causa"]))
