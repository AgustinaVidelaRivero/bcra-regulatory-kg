"""
estimacion_ablacion.py — Estimación de costo de la fase B de U-A1.4 (pre-registro
§6), PARAMETRIZADA: la fórmula deja los precios como variables y se resuelve
con la tarifa del modelo del agente (Haiku, `harness.MODEL`), a RE-VERIFICAR
contra la documentación oficial en la autorización.

Tokens por traza: agregados PUBLICADOS de EV2 base sobre KG-Refinado
(`ev2_corrida/trazas/ev2_base_v3/resumen_ev2_base_v3.json`: `cache_stats`
de la corrida completa — 168 trazas, hit_rate 0 — y `costo_usd` por caso, del
que se toma la fracción navegabilidad). Ningún archivo de trazas EV2 se abre
(principio 7): solo el resumen agregado.

Fórmula (la del harness, sin precios; harness.py:576-579):
  costo = Σ_trazas [T_in·P_in + T_cw·1,25·P_in + T_cr·0,10·P_in + T_out·P_out] / 1e6

Número de trazas: DERIVADO de pares/pares_v3.json (n_pares × 2 variantes ×
4 celdas). Escenarios: base (tokens medios EV2), navegabilidad (ajuste por la
razón costo nav / costo total de EV2 base v3), +20 % (payload v2 y trazas
BM25 de largo desconocido, §6). Tope laudado: USD 20 (cuota por celda 5).

Uso: .venv/bin/python -B estimacion_ablacion.py [--precio-in 1.00 --precio-out 5.00]
     → resultados/estimacion_ablacion.json
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

CORRIDA_DIR = Path(__file__).resolve().parent
if str(CORRIDA_DIR) not in sys.path:
    sys.path.insert(0, str(CORRIDA_DIR))

from comun_corrida import EV2_RESUMEN_V3, ORDEN_CELDAS, RESULTADOS_DIR, VARIANTES, cargar_pares, rel_repo  # noqa: E402
import harness  # noqa: E402

TOPE_LAUDADO_USD = 20.0      # pre-registro §6 [LAUDO 5]
FACTOR_INCERTIDUMBRE = 1.20  # §6: payload v2 ≈ +1–2 %, trazas BM25 de largo desconocido


def estimar(precio_in: float, precio_out: float) -> dict:
    with EV2_RESUMEN_V3.open(encoding="utf-8") as f:
        res = json.load(f)
    st = res["cache_stats"]
    n_ev2 = res["n_casos_corridos"]
    assert st["hit_rate"] == 0.0, "el resumen EV2 v3 no es una corrida fresca"
    T = {k: st[k] / n_ev2 for k in ("tokens_in", "tokens_out", "cache_read", "cache_write")}
    nav = [c for c in res["casos"] if c["eje"] == "navegabilidad"]
    costo_total_ev2 = sum(c["costo_usd"] for c in res["casos"])
    costo_nav_ev2 = sum(c["costo_usd"] for c in nav)
    por_traza_total = costo_total_ev2 / n_ev2
    por_traza_nav = costo_nav_ev2 / len(nav)
    factor_nav = por_traza_nav / por_traza_total

    def costo(t_in, t_out, t_cr, t_cw, p_in, p_out):
        return (t_in * p_in + t_cw * p_in * harness.CACHE_WRITE_MULT + t_cr * p_in * harness.CACHE_READ_MULT
                + t_out * p_out) / 1e6

    n_pares = len(cargar_pares())
    n_trazas = n_pares * len(VARIANTES) * len(ORDEN_CELDAS)
    c_traza = costo(T["tokens_in"], T["tokens_out"], T["cache_read"], T["cache_write"], precio_in, precio_out)
    escenarios = {
        "base_tokens_medios_ev2": {"usd_por_traza": round(c_traza, 5), "usd_total": round(c_traza * n_trazas, 2)},
        "navegabilidad_ajustada": {"usd_por_traza": round(c_traza * factor_nav, 5),
                                   "usd_total": round(c_traza * factor_nav * n_trazas, 2)},
        "base_mas_20pct": {"usd_por_traza": round(c_traza * FACTOR_INCERTIDUMBRE, 5),
                           "usd_total": round(c_traza * FACTOR_INCERTIDUMBRE * n_trazas, 2)},
    }
    # Con los precios del harness (1/5) el costo por traza EV2 publicado se reproduce exactamente:
    check_harness = round(costo(T["tokens_in"], T["tokens_out"], T["cache_read"], T["cache_write"],
                                harness.PRICE_IN_PER_M, harness.PRICE_OUT_PER_M), 5)
    return {
        "unidad": "U-A1.4", "generado": datetime.now().isoformat(timespec="seconds"),
        "modelo_agente": harness.MODEL,
        "precios_usd_por_mtok": {"in": precio_in, "out": precio_out,
                                 "nota": "tarifa de Haiku 4.5 (= harness.PRICE_*), a re-verificar contra la documentación oficial en la autorización"},
        "formula": "Σ_trazas [T_in·P_in + T_cw·1,25·P_in + T_cr·0,10·P_in + T_out·P_out] / 1e6 (harness.py:576-579)",
        "fuente_tokens": {"archivo": rel_repo(EV2_RESUMEN_V3), "n_trazas_fuente": n_ev2,
                          "tokens_medios_por_traza": {k: round(v, 1) for k, v in T.items()},
                          "usd_por_traza_publicado_total": round(por_traza_total, 5),
                          "usd_por_traza_publicado_navegabilidad": round(por_traza_nav, 5),
                          "n_trazas_navegabilidad_fuente": len(nav), "factor_navegabilidad": round(factor_nav, 4),
                          "check_formula_con_precios_harness_usd_por_traza": check_harness},
        "n_pares": n_pares, "n_variantes": len(VARIANTES), "n_celdas": len(ORDEN_CELDAS), "n_trazas": n_trazas,
        "escenarios": escenarios,
        "tope_laudado_usd": TOPE_LAUDADO_USD, "cuota_por_celda_usd": TOPE_LAUDADO_USD / len(ORDEN_CELDAS),
        "cuota_por_celda_vs_estimacion_celda": {k: round(v["usd_total"] / len(ORDEN_CELDAS), 2) for k, v in escenarios.items()},
        "todos_bajo_tope": all(v["usd_total"] <= TOPE_LAUDADO_USD for v in escenarios.values()),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--precio-in", type=float, default=harness.PRICE_IN_PER_M)
    ap.add_argument("--precio-out", type=float, default=harness.PRICE_OUT_PER_M)
    args = ap.parse_args()
    e = estimar(args.precio_in, args.precio_out)
    RESULTADOS_DIR.mkdir(parents=True, exist_ok=True)
    p = RESULTADOS_DIR / "estimacion_ablacion.json"
    p.write_text(json.dumps(e, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(e, ensure_ascii=False, indent=2))
    print("→", rel_repo(p))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
