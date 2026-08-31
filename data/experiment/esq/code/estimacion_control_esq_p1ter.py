"""
estimacion_control_esq_p1ter.py — Estimación previa REFRESCADA (USD 0, sin
API) de la re-corrida P1″ del control (U-ESQ-1e.c: A′ 10 dopadas + C 10
limpias), contra el tope parcial USD 0,50 del mandato.

Ancla nueva y mejor que la de U-ESQ-1d: el usage REAL de la corrida P1′
(control/extracciones_control_esq_p1bis.jsonl) — MISMAS 20 unidades, mismo
modo abierto, mismo modelo; el prefijo solo difiere en los dos cierres
neutralizados (delta estimado por len/3,5, cota conservadora). El output por
unidad puede variar (los cierres neutralizados podrían cambiar QUÉ emite el
modelo), por eso la sensibilidad llega a ×1,5.

Salida: control/estimacion_control_esq_p1ter.{json,md}.
Uso:  .venv/bin/python3 -B data/experiment/esq/code/estimacion_control_esq_p1ter.py
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
import runner_control_esq_p1bis as rp      # noqa: E402
import runner_control_esq_p1ter as rt      # noqa: E402
import prompt_e1                           # noqa: E402

CHARS_POR_TOK = 3.5    # cota conservadora castellano (menos chars/tok = más tok)


def estimar() -> dict:
    p = cc.P_E1
    fx = rp.cargar_fixtures()
    seleccion = rp.seleccion_p1bis(fx)
    regs_p1bis = rc.cargar_jsonl_last_wins(cc.CONTROL_DIR / rp.JSONL_P1BIS)

    ids = [s["chunk_id"] for s in seleccion]
    faltan = [c for c in ids if c not in regs_p1bis]
    if faltan:
        raise rc.Freno(f"unidades sin usage P1' para anclar: {faltan}")

    in_p1bis = sum((regs_p1bis[c]["usage"] or {}).get("input_tokens", 0) for c in ids)
    out_p1bis = sum((regs_p1bis[c]["usage"] or {}).get("output_tokens", 0) for c in ids)

    # Prefijo P1'': el medido de P1' + delta de los dos cierres (len/3,5).
    pref_p1bis = max((regs_p1bis[c]["usage"] or {}).get("cache_write_tokens", 0)
                     for c in ids)
    delta_cierres = int((
        (len(prompt_e1.CIERRE_CATALOGO_ABIERTO) - len(prompt_e1.CIERRE_CATALOGO_PROD))
        + (len(prompt_e1.CIERRE_REGLA4_ABIERTO) - len(prompt_e1.CIERRE_REGLA4_PROD))
    ) / CHARS_POR_TOK) + 1
    pref_p1ter = pref_p1bis + delta_cierres

    def total(mult_out: float) -> float:
        usd_in = in_p1bis * p["precio_in_por_mtok"] / 1e6
        usd_out = out_p1bis * mult_out * p["precio_out_por_mtok"] / 1e6
        usd_cr = 19 * pref_p1ter * p["precio_cache_read_por_mtok"] / 1e6
        usd_cw = 1 * pref_p1ter * p["precio_cache_write_por_mtok"] / 1e6
        return usd_in + usd_out + usd_cr + usd_cw

    est = total(1.0)
    return {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "tope_parcial_usd": cc.TOPE_PARCIAL_USD,
        "tarifas_usd_mtok": {**p, "ancla": "runner_corpus.py:76-78"},
        "anclas_medidas": {
            "fuente": ("usage real de la corrida P1' "
                       f"({rp.JSONL_P1BIS}): mismas 20 unidades, mismo modo"),
            "input_tokens_p1bis_20u": in_p1bis,
            "output_tokens_p1bis_20u": out_p1bis,
            "prefijo_p1bis_medido_tok": pref_p1bis,
            "delta_cierres_tok_est": delta_cierres,
            "prefijo_p1ter_estimado_tok": pref_p1ter,
        },
        "formula": ("in_p1bis×1,00/1e6 + out_p1bis×mult×5,00/1e6 + "
                    "19×pref×0,10/1e6 + 1×pref×1,25/1e6"),
        "total_usd": round(est, 4),
        "sensibilidad_output": [
            {"mult_out": m, "total_usd": round(total(m), 4)}
            for m in (1.0, 1.1, 1.3, 1.5)],
        "contra_tope": {
            "bajo_tope_0_50_hasta_out_x1_5": total(1.5) < cc.TOPE_PARCIAL_USD},
    }


def render_md(e: dict) -> str:
    a = e["anclas_medidas"]
    return "\n".join([
        "# Estimación previa — re-corrida del control P1″ (U-ESQ-1e, USD 0)",
        "",
        f"Generada {e['generado']}. Tope parcial **USD {e['tope_parcial_usd']:.2f}** "
        "(mandato U-ESQ-1e.c). Tarifas runner_corpus.py:76-78.",
        "",
        "## Ancla (medida, no supuesta)",
        f"- {a['fuente']}",
        f"- input 20 u (P1′ medido): {a['input_tokens_p1bis_20u']} tok; "
        f"output 20 u (P1′ medido): {a['output_tokens_p1bis_20u']} tok",
        f"- prefijo P1″: {a['prefijo_p1bis_medido_tok']} tok medidos (P1′) "
        f"+ {a['delta_cierres_tok_est']} tok (delta cierres) = "
        f"**{a['prefijo_p1ter_estimado_tok']} tok**",
        "",
        "## Cuenta",
        "```",
        f"{e['formula']}",
        f"TOTAL (mult ×1,0)             USD {e['total_usd']:.4f}",
        "```",
        "",
        "## Sensibilidad (multiplicador sobre el output medido en P1′)",
        "",
        "| mult out | total USD |",
        "|---|--:|",
        *[f"| ×{x['mult_out']} | {x['total_usd']:.4f} |"
          for x in e["sensibilidad_output"]],
        "",
        f"Bajo el tope 0,50 hasta ×1,5: "
        f"**{e['contra_tope']['bajo_tope_0_50_hasta_out_x1_5']}**",
        "",
    ])


def main() -> int:
    e = estimar()
    (cc.CONTROL_DIR / "estimacion_control_esq_p1ter.json").write_text(
        json.dumps(e, ensure_ascii=False, indent=1), encoding="utf-8")
    (cc.CONTROL_DIR / "estimacion_control_esq_p1ter.md").write_text(
        render_md(e), encoding="utf-8")
    print(f"total estimado: USD {e['total_usd']:.4f} | tope {e['tope_parcial_usd']}")
    print(f"-> {cc.CONTROL_DIR / 'estimacion_control_esq_p1ter.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
