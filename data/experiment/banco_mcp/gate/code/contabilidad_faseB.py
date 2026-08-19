#!/usr/bin/env python3
"""contabilidad_faseB.py — Gasto real de la FASE B, por dos lecturas.

Lectura 1 (la declarada como fuente de contabilidad): `total_cost_usd` que
devuelve `claude -p --output-format json` por sesión.

Lectura 2 (control): el gasto recomputado desde los CONTEOS DE TOKENS de la
misma salida (`modelUsage`) por los precios oficiales verificados el día de la
corrida (`gate/faseB_predeclaracion.md` §3). Existe porque las dos no
coinciden, y el hallazgo se reporta en vez de elegir el número que convenga.

Uso:
  contabilidad_faseB.py --runs <dir con run_*.json> [--extra <archivo.json> ...]
"""
from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

# USD por millón de tokens (documentación oficial, verificada el 2026-08-18)
PRECIOS = {
    "claude-sonnet-5":            {"in": 2.00, "cache_w": 2.50, "cache_r": 0.20, "out": 10.00},
    "claude-haiku-4-5-20251001":  {"in": 1.00, "cache_w": 1.25, "cache_r": 0.10, "out": 5.00},
}


def costo_oficial(mu: dict) -> float:
    t = 0.0
    for modelo, u in mu.items():
        p = PRECIOS.get(modelo)
        if p is None:
            raise SystemExit(f"modelo sin precio declarado: {modelo}. FRENAR.")
        t += (u.get("inputTokens", 0) * p["in"] + u.get("cacheCreationInputTokens", 0) * p["cache_w"]
              + u.get("cacheReadInputTokens", 0) * p["cache_r"] + u.get("outputTokens", 0) * p["out"]) / 1e6
    return t


def cargar(p: str) -> dict:
    s = Path(p).read_text(encoding="utf-8")
    return json.loads(s[s.find("{"):])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", required=True)
    ap.add_argument("--extra", nargs="*", default=[])
    ap.add_argument("--out", type=Path, default=None)
    a = ap.parse_args()
    filas = []
    for p in sorted(glob.glob(f"{a.runs}/run_*.json")) + list(a.extra):
        d = cargar(p)
        etiqueta = d.get("_gate", {}).get("caso") or Path(p).stem
        cli = float(d.get("total_cost_usd") or 0.0)
        ofi = costo_oficial(d.get("modelUsage", {}))
        filas.append({"etiqueta": etiqueta, "session_id": d.get("session_id"),
                      "num_turns": d.get("num_turns"), "is_error": d.get("is_error"),
                      "subtype": d.get("subtype"), "modelos": sorted(d.get("modelUsage", {})),
                      "costo_cli_usd": round(cli, 6), "costo_precios_oficiales_usd": round(ofi, 6)})
    tot_cli = sum(f["costo_cli_usd"] for f in filas)
    tot_ofi = sum(f["costo_precios_oficiales_usd"] for f in filas)
    res = {"n_sesiones": len(filas),
           "total_cli_usd": round(tot_cli, 4),
           "total_precios_oficiales_usd": round(tot_ofi, 4),
           "razon_cli_sobre_oficial": round(tot_cli / tot_ofi, 2) if tot_ofi else None,
           "tope_autorizado_usd": 2.00, "freno_declarado_usd": 1.50,
           "precios_usados": PRECIOS, "por_sesion": filas}
    txt = json.dumps(res, ensure_ascii=False, indent=2)
    print(txt)
    if a.out:
        a.out.parent.mkdir(parents=True, exist_ok=True)
        a.out.write_text(txt + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
