"""Cruce de las 23 ausencias P de D2 con la estructura de E0 del ancla (F1). USD 0.
Uso: python -B cruce_p_f1.py <repo> <out.json>"""
import json, sys
from pathlib import Path
from collections import Counter
R = Path(sys.argv[1]); out = Path(sys.argv[2])
d = json.loads((R / "reports/u_pre_r2/d2_ausencias.json").read_text(encoding="utf-8"))
e0 = R / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0"
def fin(t):
    t = t.rstrip(); return t[-1] if t else ""
chunks = {}
def cs(to):
    if to not in chunks:
        x = json.loads((e0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
        chunks[to] = x["chunks"] if isinstance(x, dict) else x
    return chunks[to]
filas = [f for f in d["filas"] if f["categoria_primaria"] == "P"]
res = {"n_P": len(filas), "anclas": {}, "criterios": Counter(), "detalle": []}
for f in filas:
    to, u = f["ancla"].split(":")
    ids = {c["id"]: c for c in cs(to)}
    titulo = None
    for c in cs(to):
        for h in c.get("herencia") or []:
            if h["tipo"] == "encabezado" and h["unidad_origen"] == u:
                titulo = h["texto"]; break
        if titulo: break
    intro = ids.get(f"{to}::{u}::intro")
    a = res["anclas"].setdefault(f["ancla"], {"titulo": titulo, "fin_titulo": fin(titulo or ""),
                                              "intro": (intro or {}).get("texto", None), "fin_intro": fin((intro or {}).get("texto", "")) if intro else None,
                                              "es_terminal": f"{to}::{u}" in ids, "filas": 0})
    a["filas"] += 1
    for cr in f["criterios"]:
        if cr["categoria"] != "P":
            continue
        e = cr["diagnostico"]["e0"]
        propias = e.get("propias") or []
        her = e.get("solo_herencia") or []
        en_bloque_del_ancla = [p for p in propias if p.startswith(f"{to}::{u}::")]
        clase = ("cita_solo_en_texto_heredado" if her and not propias else
                 "cita_en_bloque_propio_del_ancla" if en_bloque_del_ancla else
                 "cita_en_texto_propio_de_un_descendiente")
        res["criterios"][clase] += 1
        res["detalle"].append({"celda": f["celda"], "pregunta": f["id_pregunta"], "ancla": f["ancla"],
                               "criterio": cr["indice"], "clase": clase, "propias": propias, "solo_herencia": her})
res["criterios"] = dict(res["criterios"])
out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({"n_P": res["n_P"], "criterios": res["criterios"]}, ensure_ascii=False))
for k, v in res["anclas"].items():
    print(k, "| filas", v["filas"], "| terminal", v["es_terminal"], "| titulo:", (v["titulo"] or "")[:90], "| fin", v["fin_titulo"], "| intro:", (v["intro"] or "-")[:90].replace("\n", " "), "| fin_intro", v["fin_intro"])
