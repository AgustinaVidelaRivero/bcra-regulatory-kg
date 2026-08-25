"""
anotar_trazas_r1.py — Anota las 40 trazas de ev2_r1_base con `meta.u_b18`
(precedente: runner_enc agregó `meta.encadenamiento` sin alterar claves base).

Motivo (desvío declarado de la etapa 1): `runner_ev2.correr_grafo` persiste
`meta.semilla_orden = comun_ev2.SEMILLA_ORDEN` ("orden-ev2-v1") sin
parametrizarla. El ORDEN REAL de ejecución de esta unidad es el de la semilla
`orden-ev2-r1` (los casos se pasaron explícitos; `meta.pos_orden_global` y
`orden/orden_agente_r1.json` son el registro). Este script agrega el bloque
`meta.u_b18` con la semilla real y VERIFICA que `pos_orden_global` de cada
traza coincide con la posición del caso en orden_agente_r1.json. Ninguna
clave existente se altera. Idempotente.

Uso:  .venv/bin/python -B data/experiment/ev2_r1/code/anotar_trazas_r1.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_r1 as cr    # noqa: E402


def main() -> int:
    orden = json.loads((cr.ORDEN_DIR / "orden_agente_r1.json").read_text(encoding="utf-8"))
    pos_por_caso = {cid: i for i, cid in enumerate(orden["casos_en_orden"], 1)}
    trazas_dir = cr.TRAZAS_DIR / cr.R1["label"]
    anotadas = ya = 0
    for f in sorted(trazas_dir.glob("EV2F-*.json")):
        t = json.loads(f.read_text(encoding="utf-8"))
        m = t["meta"]
        if m["pos_orden_global"] != pos_por_caso[m["caso_id"]]:
            raise RuntimeError(f"{f.name}: pos_orden_global {m['pos_orden_global']} "
                               f"≠ posición en orden_agente_r1.json {pos_por_caso[m['caso_id']]}")
        if "u_b18" in m:
            ya += 1
            continue
        m["u_b18"] = {
            "unidad": "ev2_r1 (U-B1.8)",
            "semilla_orden_real": cr.SEMILLA_ORDEN_R1,
            "orden_persistido": "data/experiment/ev2_r1/orden/orden_agente_r1.json",
            "nota": ("meta.semilla_orden es un campo heredado de runner_ev2 "
                     "(no parametrizado); el orden real de esta corrida es el de "
                     "semilla_orden_real, verificado contra pos_orden_global."),
        }
        f.write_text(json.dumps(t, ensure_ascii=False, indent=2), encoding="utf-8")
        anotadas += 1
    print(f"trazas anotadas: {anotadas}; ya anotadas: {ya}; "
          f"pos_orden_global verificado 40/40")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
