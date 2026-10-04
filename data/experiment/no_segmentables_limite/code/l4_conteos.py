"""U-NOSEG-LIMITE, L4 — conteos crudos por estrato y clase de `l4_planilla.csv` (lectura asistida).
Escribe `l4_conteos.json` y `l4_conteos.md`. Sin porcentajes.

Uso: PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/no_segmentables_limite/code/l4_conteos.py
"""
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
CLASES = ("tabla de códigos", "formulario o planilla", "ficha de cuenta con criterio de imputación",
          "prosa normativa", "historial o índice", "otro")
filas = list(csv.DictReader((OUT / "l4_planilla.csv").open(encoding="utf-8")))
assert len(filas) == 59 and all(f["revision_autora"] == "" for f in filas)
por = defaultdict(Counter)
pres = defaultdict(Counter)
for f in filas:
    assert f["clase"] in CLASES, f
    por[f["estrato"]][f["clase"]] += 1
    pres[f["estrato"]][f["prescribe"]] += 1
res = {e: {"n": sum(por[e].values()), "clases": dict(por[e]), "prescribe": dict(pres[e])} for e in sorted(por)}
res["_total"] = {"n": len(filas), "clases": dict(Counter(f["clase"] for f in filas)),
                 "prescribe": dict(Counter(f["prescribe"] for f in filas))}
(OUT / "l4_conteos.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
L = ["# L4 — conteos crudos por estrato (code/l4_conteos.py sobre l4_planilla.csv)", "",
     "| estrato | n | " + " | ".join(CLASES) + " | prescribe sí | prescribe no |", "|---|--:|" + "--:|" * (len(CLASES) + 2)]
for e in sorted(por):
    L.append(f"| {e} | {res[e]['n']} | " + " | ".join(str(por[e][c]) for c in CLASES)
             + f" | {pres[e]['sí']} | {pres[e]['no']} |")
t = res["_total"]
L.append(f"| total | {t['n']} | " + " | ".join(str(t['clases'].get(c, 0)) for c in CLASES)
         + f" | {t['prescribe'].get('sí', 0)} | {t['prescribe'].get('no', 0)} |")
(OUT / "l4_conteos.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("\n".join(L))
