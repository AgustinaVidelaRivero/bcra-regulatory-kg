"""
estimacion_control_esq.py — Estimación previa (USD 0, sin API) del control de
instrumento de ESQ-1, contra el presupuesto USD 0,32 y el tope parcial 0,50.

Dos estimaciones, ambas con la aritmética a la vista:
  1. La sellada del scoping §5.3 «Control de instrumento»:
     40 × 0,00771679 + 1 × 10.383 × 1,25/1e6 = 0,3217 → USD 0,32.
  2. Una anclada por unidad: el usage REAL de las 40 unidades seleccionadas en
     la corrida cerrada de producción (input y output verbatim de sus
     registros), con los dos supuestos del scoping §5.2.1 aplicados encima
     (output +10 %; prefijo abierto 10.383 tok). Más fina porque las 40 no
     son unidades promedio: se eligieron por patología.

Salida: control/estimacion_control_esq.{json,md} y
control/orden/seleccion_control_esq.json (la lista de las 40 con su brazo).

Uso:  .venv/bin/python3 -B data/experiment/esq/code/estimacion_control_esq.py
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_control_esq as cc             # noqa: E402
import runner_control_esq as rc            # noqa: E402

SUPUESTO_OUT = 1.10          # scoping §5.2.1 (output +10 %, SUPUESTO)
PREF_ABIERTO = cc.PREF_ABIERTO_SUPUESTO_TOK   # 10.383 tok (SUPUESTO +400)


def estimar() -> dict:
    universo = cc.cargar_universo()
    seleccion = cc.seleccionar(universo)
    rc.persistir_orden(seleccion, universo, cc.ORDEN_DIR)

    p = cc.P_E1
    # --- 1. estimación sellada del scoping §5.3 ---
    r_open_scoping = 0.00771679
    est_sellada = 40 * r_open_scoping + 1 * PREF_ABIERTO * p["precio_cache_write_por_mtok"] / 1e6

    # --- 2. estimación anclada por unidad ---
    agg40 = cc.usage_produccion_de(universo, [s["chunk_id"] for s in seleccion])
    n = agg40["n"]
    in_tot, out_tot = agg40["input_tokens"], agg40["output_tokens"]
    usd_in = in_tot * p["precio_in_por_mtok"] / 1e6
    usd_out = out_tot * SUPUESTO_OUT * p["precio_out_por_mtok"] / 1e6
    usd_cr = 39 * PREF_ABIERTO * p["precio_cache_read_por_mtok"] / 1e6
    usd_cw = 1 * PREF_ABIERTO * p["precio_cache_write_por_mtok"] / 1e6
    est_anclada = usd_in + usd_out + usd_cr + usd_cw

    return {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "presupuesto_usd": cc.PRESUPUESTO_USD,
        "tope_parcial_usd": cc.TOPE_PARCIAL_USD,
        "tarifas_usd_mtok": {**p, "ancla": "runner_corpus.py:76-78"},
        "supuestos_declarados": {
            "output_recargo": "+10 % (scoping §5.2.1, SUPUESTO no medido; "
                              "el control lo mide)",
            "prefijo_abierto_tok": PREF_ABIERTO,
        },
        "estimacion_sellada_scoping_5_3": {
            "formula": "40 × 0,00771679 + 1 × 10.383 × 1,25/1e6",
            "corrida_usd": round(40 * r_open_scoping, 6),
            "escritura_usd": round(PREF_ABIERTO * p["precio_cache_write_por_mtok"] / 1e6, 6),
            "total_usd": round(est_sellada, 4),
        },
        "estimacion_anclada_40_unidades": {
            "n_unidades_con_usage": n,
            "input_tokens_40u_produccion": in_tot,
            "output_tokens_40u_produccion": out_tot,
            "formula": ("in×1,00/1e6 + out×1,10×5,00/1e6 + 39×10.383×0,10/1e6 "
                        "+ 1×10.383×1,25/1e6"),
            "usd_input": round(usd_in, 6),
            "usd_output_con_supuesto": round(usd_out, 6),
            "usd_cache_read": round(usd_cr, 6),
            "usd_cache_write": round(usd_cw, 6),
            "total_usd": round(est_anclada, 4),
        },
        "sensibilidad_supuesto_output": [
            {"output_supuesto": f"+{round((m - 1) * 100)} %",
             "total_usd": round(usd_in + out_tot * m * p["precio_out_por_mtok"] / 1e6
                                + usd_cr + usd_cw, 4)}
            for m in (1.0, 1.1, 1.2, 1.3)
        ],
        "contra_presupuesto": {
            "sellada_dentro_de_0_32": est_sellada <= cc.PRESUPUESTO_USD + 0.005,
            "anclada_dentro_de_0_32": est_anclada <= cc.PRESUPUESTO_USD + 0.005,
            "ambas_bajo_tope_parcial_0_50": max(est_sellada, est_anclada) < cc.TOPE_PARCIAL_USD,
        },
        "seleccion_resumen": {
            "por_brazo": {b: sum(1 for s in seleccion if s["brazo"] == b)
                          for b in ("A", "B", "C")},
            "por_to": {t: sum(1 for s in seleccion if s["to"] == t)
                       for t in cc.TOS},
        },
    }


def render_md(e: dict) -> str:
    s, a = e["estimacion_sellada_scoping_5_3"], e["estimacion_anclada_40_unidades"]
    return "\n".join([
        "# Estimación previa — control de instrumento de ESQ-1 (U-ESQ-1c, USD 0)",
        "",
        f"Generada {e['generado']}. Presupuesto **USD {e['presupuesto_usd']:.2f}** "
        f"(scoping §5.3), tope parcial **USD {e['tope_parcial_usd']:.2f}** (mandato).",
        f"Tarifas: {e['tarifas_usd_mtok']['ancla']} — in 1,00 / out 5,00 / "
        "cache write 1,25 / cache read 0,10 USD/MTok.",
        "",
        "## 1. Estimación sellada (scoping §5.3 «Control de instrumento»)",
        "```",
        f"corrida    40 × 0,00771679                = USD {s['corrida_usd']:.6f}",
        f"escritura   1 × 10.383 × 1,25/1e6         = USD {s['escritura_usd']:.6f}",
        f"                                            ─────────",
        f"                                            USD {s['total_usd']:.4f}",
        "```",
        "",
        "## 2. Estimación anclada en el usage real de las 40 unidades",
        "",
        f"Input y output de esas 40 unidades en la corrida cerrada de producción "
        f"(sus registros en `corpus_v2/salida/*/extracciones_e1.jsonl`): "
        f"{a['input_tokens_40u_produccion']} tok in, "
        f"{a['output_tokens_40u_produccion']} tok out "
        f"({a['n_unidades_con_usage']} unidades con usage). Supuestos del scoping "
        "§5.2.1 encima: output +10 %, prefijo abierto 10.383 tok.",
        "```",
        f"input       {a['input_tokens_40u_produccion']} × 1,00/1e6          = USD {a['usd_input']:.6f}",
        f"output      {a['output_tokens_40u_produccion']} × 1,10 × 5,00/1e6  = USD {a['usd_output_con_supuesto']:.6f}",
        f"cache read  39 × 10.383 × 0,10/1e6        = USD {a['usd_cache_read']:.6f}",
        f"cache write  1 × 10.383 × 1,25/1e6        = USD {a['usd_cache_write']:.6f}",
        f"                                            ─────────",
        f"                                            USD {a['total_usd']:.4f}",
        "```",
        "",
        "## 3. Sensibilidad del supuesto de output (estimación anclada)",
        "",
        "| output supuesto | total USD |",
        "|---|--:|",
        *[f"| {x['output_supuesto']} | {x['total_usd']:.4f} |"
          for x in e["sensibilidad_supuesto_output"]],
        "",
        "## 4. Contra el presupuesto",
        "",
        f"- sellada ≤ 0,32: **{e['contra_presupuesto']['sellada_dentro_de_0_32']}**",
        f"- anclada ≤ 0,32: **{e['contra_presupuesto']['anclada_dentro_de_0_32']}**",
        f"- ambas < tope parcial 0,50: **{e['contra_presupuesto']['ambas_bajo_tope_parcial_0_50']}**",
        "",
        "Discrepancia a decidir en el freno de autorización: la estimación "
        "sellada del scoping (0,32) presupone unidades de output promedio; las "
        "40 del control son output-pesadas por construcción (se eligieron por "
        "omisiones y presión de firma). La anclada supera el presupuesto y "
        "queda bajo el tope parcial 0,50 hasta output +30 %. La decisión de "
        "gasto es de la autora.",
        "",
        "Selección: " + json.dumps(e["seleccion_resumen"], ensure_ascii=False)
        + " — lista completa con brazo en `orden/seleccion_control_esq.json`.",
        "",
    ])


def main() -> int:
    e = estimar()
    cc.CONTROL_DIR.mkdir(parents=True, exist_ok=True)
    (cc.CONTROL_DIR / "estimacion_control_esq.json").write_text(
        json.dumps(e, ensure_ascii=False, indent=1), encoding="utf-8")
    (cc.CONTROL_DIR / "estimacion_control_esq.md").write_text(
        render_md(e), encoding="utf-8")
    print(f"sellada: USD {e['estimacion_sellada_scoping_5_3']['total_usd']:.4f} | "
          f"anclada: USD {e['estimacion_anclada_40_unidades']['total_usd']:.4f} | "
          f"presupuesto {e['presupuesto_usd']} | tope parcial {e['tope_parcial_usd']}")
    print(f"-> {cc.CONTROL_DIR / 'estimacion_control_esq.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
