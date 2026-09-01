"""
gasto_descubrimiento_cal.py — Gasto real de la calibración del descubrimiento
(U-ESQ-2-cal.c) recomputado desde sus DOS fuentes primarias, con cruce entre
ellas (mismo patrón que gasto_control_esq*.py):

  1. cache/esq_descubrimiento_cal.db (la .db PROPIA del instrumento);
  2. control/descubrimiento_cal.jsonl.

Uso:  .venv/bin/python3 -B data/experiment/esq/code/gasto_descubrimiento_cal.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_control_esq as cc             # noqa: E402
import gasto_control_esq as g              # noqa: E402
import runner_descubrimiento_cal as rd     # noqa: E402

JSONL = cc.CONTROL_DIR / rd.JSONL_DESC


def main() -> int:
    db = g.gasto_db(rd.DB_DESC)
    jl = g.gasto_jsonl(JSONL)
    cruza = (db is not None and jl is not None
             and db["usd"] == jl["usd"]
             and all(db[k] == jl[k] for k in
                     ("input_tokens", "output_tokens",
                      "cache_write_tokens", "cache_read_tokens")))
    print(json.dumps({
        "tarifas_usd_mtok": {**cc.P_E1, "ancla": "runner_corpus.py:76-78"},
        "desde_db": db if db else {"db": str(rd.DB_DESC), "error": "no existe"},
        "desde_jsonl": jl if jl else {"jsonl": str(JSONL), "error": "no existe"},
        "fuentes_cruzan": cruza,
        "nota": ("pueden diferir si hubo reanudación (el jsonl repite la "
                 "unidad, la db no re-paga) — en ese caso manda la db"),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
