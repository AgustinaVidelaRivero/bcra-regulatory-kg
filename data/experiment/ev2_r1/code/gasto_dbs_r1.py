"""
gasto_dbs_r1.py — Gasto real desde las dbs de caché de U-B1.8 (tokens de la
tabla `cache`, una fila por miss pagado; hits por run_label desde `access_log`).
Los precios se pasan por CLI (verificados contra la documentación oficial el
día de la corrida); los multiplicadores de caché (write 1,25× / read 0,10×
sobre el precio de entrada) son los vigentes de la documentación oficial y
coinciden con los del harness congelado.

Uso:
  .venv/bin/python -B data/experiment/ev2_r1/code/gasto_dbs_r1.py \
      --db cache/ev2_r1_base.db --precio-in 1 --precio-out 5
  (acepta --db repetido; rutas relativas a data/experiment/ev2_r1/)
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
UNIDAD_DIR = CODE_DIR.parent


def gasto_db(path: Path, pin: float, pout: float,
             mult_cw: float = 1.25, mult_cr: float = 0.10) -> dict | None:
    if not path.exists():
        return None
    conn = sqlite3.connect(str(path))
    n, i, o, cr_, cw = conn.execute(
        "SELECT COUNT(*), COALESCE(SUM(input_tokens),0), COALESCE(SUM(output_tokens),0), "
        "COALESCE(SUM(cache_read_tokens),0), COALESCE(SUM(cache_write_tokens),0) FROM cache"
    ).fetchone()
    hits = {k: int(v or 0) for k, v in conn.execute(
        "SELECT run_label, SUM(hit) FROM access_log GROUP BY run_label")}
    accesos = conn.execute("SELECT COUNT(*) FROM access_log").fetchone()[0]
    dominios = sorted(r[0] for r in conn.execute("SELECT DISTINCT domain FROM cache"))
    conn.close()
    usd = (i * pin + o * pout + cw * pin * mult_cw + cr_ * pin * mult_cr) / 1e6
    return {"db": path.name, "filas": n, "input_tokens": i, "output_tokens": o,
            "cache_read_tokens": cr_, "cache_write_tokens": cw,
            "accesos": accesos, "hits_por_label": hits, "hits": sum(hits.values()),
            "dominios": dominios,
            "precios_usd_mtok": {"in": pin, "out": pout, "cache_write": pin * mult_cw,
                                 "cache_read": pin * mult_cr},
            "usd": round(usd, 4)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", action="append", required=True)
    ap.add_argument("--precio-in", type=float, required=True)
    ap.add_argument("--precio-out", type=float, required=True)
    args = ap.parse_args()
    total = 0.0
    out = []
    for d in args.db:
        p = Path(d)
        if not p.is_absolute():
            p = UNIDAD_DIR / p
        g = gasto_db(p, args.precio_in, args.precio_out)
        out.append(g if g else {"db": str(p), "error": "no existe"})
        if g:
            total += g["usd"]
    print(json.dumps({"dbs": out, "total_usd": round(total, 4)},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
