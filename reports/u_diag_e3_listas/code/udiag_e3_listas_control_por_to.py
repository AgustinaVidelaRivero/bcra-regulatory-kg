"""U-DIAG-E3-LISTAS: control del confusor por TO. Para cada TO: unidades ítem y no ítem, y cuántas de cada grupo
están en la cola (74), tienen flag «cola_humana» (29) o tuvieron reintento del ratchet. Solo lectura.

Uso: python control_por_to.py <copia> <salida_dir>
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

COPIA = Path(sys.argv[1]).resolve()
SAL = Path(sys.argv[2]).resolve()
SALIDA = COPIA / "data" / "experiment" / "reextraccion_v2" / "corpus_tanda0" / "salida_r2b"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")


def jl(p):
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


U = {u["chunk_id"]: u for u in json.loads((SAL / "fase1_unidades.json").read_text(encoding="utf-8"))}
cola, reint = {}, set()
for to in TOS:
    cola.update({r["chunk_id"]: r["flag"] for r in jl(SALIDA / to / "cola_humana.jsonl")})
    reint |= {r["chunk_id"] for r in jl(SALIDA / to / "reintentos_e3.jsonl")}
t = defaultdict(lambda: defaultdict(int))
for cid, u in U.items():
    g = "item" if u["linea_item"] else "no_item"
    for clave, cond in (("unidades", True), ("cola74", cid in cola), ("cola_humana29", cola.get(cid) == "cola_humana"),
                        ("reintento", cid in reint)):
        if cond:
            t[(u["to"], g)][clave] += 1
            t[("TOTAL", g)][clave] += 1
out = {f"{to}|{g}": dict(v) for (to, g), v in sorted(t.items())}
(SAL / "control_por_to.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for k, v in out.items():
    print(f"{k:16s} unidades={v.get('unidades',0):5d} cola74={v.get('cola74',0):3d} cola_humana29={v.get('cola_humana29',0):3d} reintento={v.get('reintento',0):4d}")
