"""Prevalencia de F1 y del vinculo entre unidades en la muestra azarosa de ESQ-2 (Wilson 95 %),
exposicion estructural (item de lista o bloque que abre lista) en la muestra y en la particion. USD 0.
Uso: python -B prevalencia.py <repo> <out.json>"""
import json, sys, math
from pathlib import Path
from collections import Counter
R = Path(sys.argv[1]); out = Path(sys.argv[2])
def wilson(x, n, z=1.959963984540054):
    p = x / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return round(c - h, 4), round(c + h, 4)
sel = json.loads((R / "data/experiment/esq/cobertura/orden/seleccion_muestra_esq2.json").read_text(encoding="utf-8"))
W = json.loads((R / "data/experiment/esq/cobertura/fichas/worksheet_fichas_esq2.json").read_text(encoding="utf-8"))
az = set(sel["azarosa"]); fichas = {x["chunk_id"]: x for x in W["fichas"]}
F1 = {11, 13, 48, 52, 64}; VIN = {18, 39, 61, 72}
az_f = [fichas[c] for c in az]
x_f1 = sum(1 for f in az_f if f["n"] in F1); x_v = sum(1 for f in az_f if f["n"] in VIN)
n = len(az_f)
P = R / "data/experiment/segmentacion_84/b584_particion"
def fin(t):
    t = t.rstrip(); return t[-1] if t else ""
def expuesta(c):
    her = c.get("herencia") or []
    if c.get("tipo") == "punto_terminal" and her and fin(her[-1]["texto"]) == ":":
        return "item_de_lista"
    if c.get("tipo") == "mini_chunk" and c.get("rol_bloque") in ("intro", "chapeau_seccion") and fin(c["texto"]) == ":":
        return "bloque_que_abre_lista"
    return None
part = Counter(); por_id = {}
for a in sorted(P.glob("*/chunks_*.json")):
    d = json.loads(a.read_text(encoding="utf-8")); cs = d["chunks"] if isinstance(d, dict) else d
    for c in cs:
        e = expuesta(c); part["unidades"] += 1
        if e: part[e] += 1; part["expuestas"] += 1
        por_id[c["id"]] = e
mues = Counter(); f1_exp = Counter(); faltan = []
for f in az_f:
    if f["chunk_id"] not in por_id:
        faltan.append(f["chunk_id"]); continue
    e = por_id[f["chunk_id"]]
    mues["expuestas" if e else "no_expuestas"] += 1
    if f["n"] in F1:
        f1_exp["F1_expuesta" if e else "F1_no_expuesta"] += 1
res = {
    "n_azarosa": n,
    "F1": {"x": x_f1, "n": n, "p": round(x_f1 / n, 4), "wilson95": wilson(x_f1, n)},
    "vinculo": {"x": x_v, "n": n, "p": round(x_v / n, 4), "wilson95": wilson(x_v, n)},
    "particion": dict(part),
    "muestra_azarosa_exposicion": dict(mues), "F1_por_exposicion": dict(f1_exp), "chunks_azarosos_sin_id_en_particion": faltan,
}
U = part["unidades"]
res["implicado_particion"] = {
    "F1_tasa_global_x_U": [round(res["F1"]["wilson95"][0] * U), round(res["F1"]["p"] * U), round(res["F1"]["wilson95"][1] * U)],
    "vinculo_tasa_global_x_U": [round(res["vinculo"]["wilson95"][0] * U), round(res["vinculo"]["p"] * U), round(res["vinculo"]["wilson95"][1] * U)],
}
ne = mues["expuestas"]; xe = f1_exp["F1_expuesta"]
if ne:
    res["F1_condicional_expuestas"] = {"x": xe, "n": ne, "p": round(xe / ne, 4), "wilson95": wilson(xe, ne),
                                       "implicado_sobre_expuestas_particion": [round(wilson(xe, ne)[0] * part["expuestas"]), round(xe / ne * part["expuestas"]), round(wilson(xe, ne)[1] * part["expuestas"])]}
out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
