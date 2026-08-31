"""
gasto_control_esq_p1bis.py — Gasto real de la RE-CORRIDA del control
(U-ESQ-1d.d) recomputado desde sus DOS fuentes primarias, con cruce entre
ellas (mismo patrón que gasto_control_esq.py, que queda intacto para el
control original):

  1. cache/esq_control_p1bis.db (la .db PROPIA de la re-corrida);
  2. control/extracciones_control_esq_p1bis.jsonl.

Uso:  .venv/bin/python3 -B data/experiment/esq/code/gasto_control_esq_p1bis.py
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
import runner_control_esq_p1bis as rp      # noqa: E402

JSONL = cc.CONTROL_DIR / rp.JSONL_P1BIS


def main() -> int:
    db = g.gasto_db(rp.DB_P1BIS)
    jl = g.gasto_jsonl(JSONL)
    cruza = (db is not None and jl is not None
             and db["usd"] == jl["usd"]
             and all(db[k] == jl[k] for k in
                     ("input_tokens", "output_tokens",
                      "cache_write_tokens", "cache_read_tokens")))
    print(json.dumps({
        "tarifas_usd_mtok": {**cc.P_E1, "ancla": "runner_corpus.py:76-78"},
        "desde_db": db if db else {"db": str(rp.DB_P1BIS), "error": "no existe"},
        "desde_jsonl": jl if jl else {"jsonl": str(JSONL), "error": "no existe"},
        "fuentes_cruzan": cruza,
        "nota": ("pueden diferir si hubo reanudación (el jsonl repite la unidad, "
                 "la db no re-paga) — en ese caso manda la db"),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
