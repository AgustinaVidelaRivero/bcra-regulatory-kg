"""
gasto_control_esq.py — Gasto real del control de instrumento recomputado desde
las DOS fuentes primarias, con cruce entre ellas (patrón gasto_dbs_r1.py):

  1. la .db de caché propia (esq/cache/esq_control.db): tokens de la tabla
     `cache`, una fila por miss pagado; hits por run_label en `access_log`;
  2. el usage persistido por unidad en control/extracciones_control_esq.jsonl.

Precios: runner_corpus.py:76-78 (in 1,00 / out 5,00 USD/MTok); los
multiplicadores de caché (write 1,25× / read 0,10× sobre el precio de entrada)
son los vigentes de la documentación oficial y coinciden con esa ancla.

Uso:  .venv/bin/python3 -B data/experiment/esq/code/gasto_control_esq.py
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_control_esq as cc             # noqa: E402

DB = cc.CACHE_DIR / "esq_control.db"
JSONL = cc.CONTROL_DIR / "extracciones_control_esq.jsonl"


def gasto_db(path: Path) -> dict | None:
    if not path.exists():
        return None
    conn = sqlite3.connect(str(path))
    n, i, o, cr_, cw = conn.execute(
        "SELECT COUNT(*), COALESCE(SUM(input_tokens),0), COALESCE(SUM(output_tokens),0), "
        "COALESCE(SUM(cache_read_tokens),0), COALESCE(SUM(cache_write_tokens),0) FROM cache"
    ).fetchone()
    hits = {k: int(v or 0) for k, v in conn.execute(
        "SELECT run_label, SUM(hit) FROM access_log GROUP BY run_label")}
    namespaces = sorted(r[0] for r in conn.execute("SELECT DISTINCT namespace FROM cache"))
    conn.close()
    agg = {"input_tokens": i, "output_tokens": o,
           "cache_write_tokens": cw, "cache_read_tokens": cr_}
    return {"db": path.name, "filas_miss": n, **agg,
            "hits_por_label": hits, "namespaces": namespaces,
            "usd": round(cc.costo_usd_desde_usage(agg), 6)}


def gasto_jsonl(path: Path) -> dict | None:
    if not path.exists():
        return None
    usages = []
    with path.open(encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                usages.append(json.loads(linea).get("usage") or {})
    agg = cc.agregar_usage(usages)
    return {"jsonl": path.name, **agg,
            "usd": round(cc.costo_usd_desde_usage(agg), 6)}


def main() -> int:
    db = gasto_db(DB)
    jl = gasto_jsonl(JSONL)
    cruza = (db is not None and jl is not None
             and db["usd"] == jl["usd"]
             and all(db[k] == jl[k] for k in
                     ("input_tokens", "output_tokens",
                      "cache_write_tokens", "cache_read_tokens")))
    print(json.dumps({
        "tarifas_usd_mtok": {**cc.P_E1, "ancla": "runner_corpus.py:76-78"},
        "desde_db": db if db else {"db": str(DB), "error": "no existe"},
        "desde_jsonl": jl if jl else {"jsonl": str(JSONL), "error": "no existe"},
        "fuentes_cruzan": cruza,
        "nota": ("pueden diferir si hubo reanudación (el jsonl repite la unidad, "
                 "la db no re-paga) — en ese caso manda la db, que es la fuente "
                 "de lo efectivamente pagado"),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
