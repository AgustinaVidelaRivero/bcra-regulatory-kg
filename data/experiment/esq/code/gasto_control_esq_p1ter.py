"""
gasto_control_esq_p1ter.py — Gasto real de la re-corrida P1″ del control
(U-ESQ-1e.c) recomputado desde sus DOS fuentes primarias, con cruce entre
ellas (mismo patrón que gasto_control_esq_p1bis.py, que queda intacto para
la corrida P1′):

  1. cache/esq_control_p1ter.db (la .db PROPIA de la re-corrida P1″);
  2. control/extracciones_control_esq_p1ter.jsonl.

Uso:  .venv/bin/python3 -B data/experiment/esq/code/gasto_control_esq_p1ter.py
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
import runner_control_esq_p1ter as rt      # noqa: E402

JSONL = cc.CONTROL_DIR / rt.JSONL_P1TER


def main() -> int:
    db = g.gasto_db(rt.DB_P1TER)
    jl = g.gasto_jsonl(JSONL)
    cruza = (db is not None and jl is not None
             and db["usd"] == jl["usd"]
             and all(db[k] == jl[k] for k in
                     ("input_tokens", "output_tokens",
                      "cache_write_tokens", "cache_read_tokens")))
    print(json.dumps({
        "tarifas_usd_mtok": {**cc.P_E1, "ancla": "runner_corpus.py:76-78"},
        "desde_db": db if db else {"db": str(rt.DB_P1TER), "error": "no existe"},
        "desde_jsonl": jl if jl else {"jsonl": str(JSONL), "error": "no existe"},
        "fuentes_cruzan": cruza,
        "nota": ("pueden diferir si hubo reanudación (el jsonl repite la unidad, "
                 "la db no re-paga) — en ese caso manda la db"),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
