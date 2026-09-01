"""
estimacion_descubrimiento_cal.py — Estimación previa ANCLADA (USD 0, sin API)
de la corrida de calibración del descubrimiento (U-ESQ-2-cal.c: A′ 10 dopadas
+ C 10 limpias), contra el tope parcial USD 0,50 del mandato.

Anclas medidas:
  - INPUT variable por unidad: el usage real de la corrida P1′
    (control/extracciones_control_esq_p1bis.jsonl) — MISMAS 20 unidades,
    mismo texto por unidad. El user message del descubrimiento es MÁS CORTO
    que el de extracción (sin 'Puntos admitidos' ni alcance de sujetos);
    usar el input de P1′ tal cual es cota superior conservadora.
  - PREFIJO: len(contrato del instrumento)/3,5 chars por token (cota
    conservadora castellano). El prefijo del descubrimiento es chico y puede
    quedar BAJO el mínimo cacheable de Haiku 4.5 (4096 tok): se computan los
    DOS escenarios (cacheado y sin caché — sin caché el prefijo se paga como
    input en las 20 llamadas) y manda el peor.
  - OUTPUT: sin ancla medida (instrumento nuevo): escenarios 100/300/600/
    1000 tok por unidad; la referencia del pre-registro §7 (~USD 0,2 las 20)
    cae dentro del rango.

Salida: control/estimacion_descubrimiento_cal.{json,md}.
Uso:  .venv/bin/python3 -B data/experiment/esq/code/estimacion_descubrimiento_cal.py
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
import descubrimiento_cal as dc            # noqa: E402

CHARS_POR_TOK = 3.5


def estimar() -> dict:
    p = cc.P_E1
    fx = rp.cargar_fixtures()
    seleccion = rp.seleccion_p1bis(fx)
    regs = rc.cargar_jsonl_last_wins(cc.CONTROL_DIR / rp.JSONL_P1BIS)
    ids = [s["chunk_id"] for s in seleccion]
    faltan = [c for c in ids if c not in regs]
    if faltan:
        raise rc.Freno(f"unidades sin usage P1' para anclar: {faltan}")

    in_20u = sum((regs[c]["usage"] or {}).get("input_tokens", 0) for c in ids)
    pref_chars = len(dc.PREFIJO_DESCUBRIMIENTO) + len(json.dumps(
        dc.TOOL_DESCUBRIMIENTO, ensure_ascii=False))
    pref_tok = int(pref_chars / CHARS_POR_TOK) + 1

    def total(out_por_u: int, con_cache: bool) -> float:
        usd_in = in_20u * p["precio_in_por_mtok"] / 1e6
        usd_out = 20 * out_por_u * p["precio_out_por_mtok"] / 1e6
        if con_cache:
            usd_pref = (pref_tok * p["precio_cache_write_por_mtok"]
                        + 19 * pref_tok * p["precio_cache_read_por_mtok"]) / 1e6
        else:
            usd_pref = 20 * pref_tok * p["precio_in_por_mtok"] / 1e6
        return usd_in + usd_out + usd_pref

    escenarios = [
        {"out_tok_u": o, "cache": c,
         "total_usd": round(total(o, c), 4)}
        for o in (100, 300, 600, 1000) for c in (True, False)]
    peor = max(e["total_usd"] for e in escenarios)
    return {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "tope_parcial_usd": cc.TOPE_PARCIAL_USD,
        "tarifas_usd_mtok": {**p, "ancla": "runner_corpus.py:76-78"},
        "anclas": {
            "input_20u_p1bis_medido_tok": in_20u,
            "nota_input": ("cota superior: el user message del descubrimiento "
                           "es más corto que el de extracción P1'"),
            "prefijo_estimado_tok": pref_tok,
            "prefijo_chars": pref_chars,
            "nota_prefijo": ("si < 4096 tok, Haiku 4.5 no cachea: escenario "
                             "sin caché paga el prefijo como input x20"),
        },
        "formula": ("in_p1bis×1,00/1e6 + 20×out×5,00/1e6 + prefijo "
                    "(cacheado: 1×1,25 + 19×0,10; sin caché: 20×1,00) /1e6"),
        "escenarios": escenarios,
        "peor_escenario_usd": peor,
        "contra_tope": {"peor_bajo_tope_0_50": peor < cc.TOPE_PARCIAL_USD},
    }


def render_md(e: dict) -> str:
    a = e["anclas"]
    filas = [f"| {x['out_tok_u']} | {'sí' if x['cache'] else 'no'} | "
             f"{x['total_usd']:.4f} |" for x in e["escenarios"]]
    return "\n".join([
        "# Estimación previa — calibración del descubrimiento (U-ESQ-2-cal, USD 0)",
        "",
        f"Generada {e['generado']}. Tope parcial **USD "
        f"{e['tope_parcial_usd']:.2f}** (mandato U-ESQ-2-cal.c). Tarifas "
        "runner_corpus.py:76-78.",
        "",
        "## Anclas (medidas donde las hay)",
        f"- input 20 u (P1′ medido, cota superior): "
        f"{a['input_20u_p1bis_medido_tok']} tok — {a['nota_input']}",
        f"- prefijo del instrumento: {a['prefijo_chars']} chars ≈ "
        f"**{a['prefijo_estimado_tok']} tok** (len/3,5) — {a['nota_prefijo']}",
        "- output: sin ancla (instrumento nuevo) → escenarios",
        "",
        "## Cuenta",
        "```",
        e["formula"],
        "```",
        "",
        "| out tok/u | prefijo cacheado | total USD |",
        "|--:|:--:|--:|",
        *filas,
        "",
        f"Peor escenario: **USD {e['peor_escenario_usd']:.4f}** — bajo el "
        f"tope 0,50: **{e['contra_tope']['peor_bajo_tope_0_50']}**",
        "",
    ])


def main() -> int:
    e = estimar()
    (cc.CONTROL_DIR / "estimacion_descubrimiento_cal.json").write_text(
        json.dumps(e, ensure_ascii=False, indent=1), encoding="utf-8")
    (cc.CONTROL_DIR / "estimacion_descubrimiento_cal.md").write_text(
        render_md(e), encoding="utf-8")
    print(f"peor escenario: USD {e['peor_escenario_usd']:.4f} | "
          f"tope {e['tope_parcial_usd']}")
    print(f"-> {cc.CONTROL_DIR / 'estimacion_descubrimiento_cal.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
