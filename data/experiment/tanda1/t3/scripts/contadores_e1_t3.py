"""B6.1, tanda 1, T3, punto 4: los contadores de E1 del gate (laudo de la release r2, §3; como U-REEXT-T0 T3, reext_t0/freno_t3.md:12):
`tipo_obligacion_requisito_de_estructura` y `tipo_obligacion_normalizados` del resumen de E1 de cada TO de la tanda 1. Solo lee esos
dos campos de <salida>/<TO>/resumen_e1.json (nada de E3). USD 0.
Uso: python3 -I -B contadores_e1_t3.py <raíz> <salida.json>"""
import json
import sys
from pathlib import Path

RAIZ, OUT = Path(sys.argv[1]), Path(sys.argv[2])
man = json.loads((RAIZ / "data/experiment/reextraccion_v2/manifiestos/tanda1_20tos_r2b.json").read_text(encoding="utf-8"))
SAL = RAIZ / "data/experiment/reextraccion_v2/corpus_tanda1/salida_r2b"
CAMPOS = ("tipo_obligacion_requisito_de_estructura", "tipo_obligacion_normalizados")
por_to = {}
for to in man["orden_corrida"]:
    r = json.loads((SAL / to / "resumen_e1.json").read_text(encoding="utf-8"))
    por_to[to] = {c: r.get(c) for c in CAMPOS}
tot = {c: sum(v[c] or 0 for v in por_to.values()) for c in CAMPOS}
OUT.write_text(json.dumps({"por_to": por_to, "total": tot}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(tot, ensure_ascii=False), "| TOs con algún valor distinto de 0:",
      sorted(t for t, v in por_to.items() if any(v[c] for c in CAMPOS)))
