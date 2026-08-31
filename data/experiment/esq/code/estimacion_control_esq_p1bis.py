"""
estimacion_control_esq_p1bis.py — Estimación previa (USD 0, sin API) de la
RE-CORRIDA del control (U-ESQ-1d.d: A′ 10 dopadas + C 10 limpias), contra el
tope parcial USD 0,50 del mandato.

Anclas medidas, no supuestos, donde existen:
  - Brazo C: el usage REAL en modo abierto de esas mismas 10 unidades en la
    corrida del control original (control/extracciones_control_esq.jsonl) —
    misma unidad, mismo modo, prefijo casi idéntico (solo cambia la
    description del tool).
  - Brazo A′: el usage cerrado de producción de las 10 unidades BASE, con
    (i) el input incrementado por la cláusula plantada (len/3,5 tok, cota
    conservadora) y (ii) el output multiplicado por el ratio abierto/cerrado
    MEDIDO en el control original sobre sus 40 unidades pareadas.
  - Prefijo: el medido del control original (10.583 tok de cache write) más
    el delta de la description corregida (len/3,5).

Salida: control/estimacion_control_esq_p1bis.{json,md}.
Uso:  .venv/bin/python3 -B data/experiment/esq/code/estimacion_control_esq_p1bis.py
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
import prompt_e1                           # noqa: E402

CHARS_POR_TOK = 3.5    # cota conservadora castellano (menos chars/tok = más tok)


def estimar() -> dict:
    p = cc.P_E1
    fx = rp.cargar_fixtures()
    seleccion = rp.seleccion_p1bis(fx)
    universo = cc.cargar_universo()
    regs_ctrl_orig = rc.cargar_jsonl_last_wins(
        cc.CONTROL_DIR / "extracciones_control_esq.jsonl")

    # Ratio de output abierto/cerrado MEDIDO (40 unidades pareadas del
    # control original).
    ids40 = list(regs_ctrl_orig)
    out_open = sum((regs_ctrl_orig[c].get("usage") or {}).get("output_tokens", 0)
                   for c in ids40)
    out_prod = sum((universo.get(c, {}).get("usage") or {}).get("output_tokens", 0)
                   for c in ids40)
    ratio_out = out_open / out_prod if out_prod else 1.10

    # Prefijo nuevo: medido del control original + delta de la description.
    pref_viejo = 10583   # resumen_control_esq.json → pref_abierto_medido_tok
    delta_desc = int((len(prompt_e1.TOOL_SCHEMA_E1_CANAL_ABIERTO["description"])
                      - len(prompt_e1.TOOL_SCHEMA_E1["description"])) / CHARS_POR_TOK) + 1
    pref_nuevo = pref_viejo + delta_desc

    # Brazo C: usage abierto medido de esas 10 unidades (input variable y out).
    c_ids = [s["chunk_id"] for s in seleccion if s["brazo"] == "C"]
    c_in = sum((regs_ctrl_orig[c]["usage"] or {}).get("input_tokens", 0) for c in c_ids)
    c_out = sum((regs_ctrl_orig[c]["usage"] or {}).get("output_tokens", 0) for c in c_ids)

    # Brazo A′: base cerrada de producción + cláusula; out × ratio medido.
    a_sel = [s for s in seleccion if s["brazo"] == "A'"]
    claus = {d["chunk_id_dopado"]: d["clausula_plantada"] for d in fx["dopadas"]}
    a_in = sum((universo[s["chunk_id_base"]]["usage"] or {}).get("input_tokens", 0)
               + int(len(claus[s["chunk_id"]]) / CHARS_POR_TOK) + 1
               for s in a_sel)
    a_out_base = sum((universo[s["chunk_id_base"]]["usage"] or {}).get("output_tokens", 0)
                     for s in a_sel)
    a_out = a_out_base * ratio_out

    def total(mult_out: float) -> float:
        usd_in = (a_in + c_in) * p["precio_in_por_mtok"] / 1e6
        usd_out = (a_out + c_out) * mult_out * p["precio_out_por_mtok"] / 1e6
        usd_cr = 19 * pref_nuevo * p["precio_cache_read_por_mtok"] / 1e6
        usd_cw = 1 * pref_nuevo * p["precio_cache_write_por_mtok"] / 1e6
        return usd_in + usd_out + usd_cr + usd_cw

    est = total(1.0)
    return {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "tope_parcial_usd": cc.TOPE_PARCIAL_USD,
        "tarifas_usd_mtok": {**p, "ancla": "runner_corpus.py:76-78"},
        "anclas_medidas": {
            "ratio_out_abierto_cerrado_medido": round(ratio_out, 4),
            "fuente_ratio": ("40 unidades pareadas del control original: "
                             f"{out_open} tok abierto / {out_prod} tok cerrado"),
            "prefijo_viejo_medido_tok": pref_viejo,
            "delta_description_tok_est": delta_desc,
            "prefijo_nuevo_estimado_tok": pref_nuevo,
        },
        "brazo_C_usage_abierto_medido": {"input_tokens": c_in, "output_tokens": c_out},
        "brazo_Ap_estimado": {
            "input_tokens_con_clausulas": a_in,
            "output_base_cerrado_tokens": a_out_base,
            "output_estimado_tokens": round(a_out),
        },
        "formula": ("(a_in+c_in)×1,00/1e6 + (a_out+c_out)×5,00/1e6 + "
                    "19×pref×0,10/1e6 + 1×pref×1,25/1e6"),
        "total_usd": round(est, 4),
        "sensibilidad_output": [
            {"mult_out": m, "total_usd": round(total(m), 4)}
            for m in (1.0, 1.1, 1.2, 1.3)],
        "contra_tope": {"bajo_tope_0_50_hasta_out_x1_3": total(1.3) < cc.TOPE_PARCIAL_USD},
    }


def render_md(e: dict) -> str:
    a = e["anclas_medidas"]
    return "\n".join([
        "# Estimación previa — re-corrida del control P1′ (U-ESQ-1d, USD 0)",
        "",
        f"Generada {e['generado']}. Tope parcial **USD {e['tope_parcial_usd']:.2f}** "
        "(mandato U-ESQ-1d.d). Tarifas runner_corpus.py:76-78.",
        "",
        "## Anclas (medidas, no supuestas)",
        f"- ratio output abierto/cerrado medido: **{a['ratio_out_abierto_cerrado_medido']}** "
        f"({a['fuente_ratio']})",
        f"- prefijo abierto nuevo: {a['prefijo_viejo_medido_tok']} tok medidos "
        f"+ {a['delta_description_tok_est']} tok (delta description) = "
        f"**{a['prefijo_nuevo_estimado_tok']} tok**",
        "",
        "## Cuenta",
        "```",
        f"A' input (bases + cláusulas)  {e['brazo_Ap_estimado']['input_tokens_con_clausulas']} tok",
        f"A' output (base × ratio)      {e['brazo_Ap_estimado']['output_estimado_tokens']} tok",
        f"C  input (abierto medido)     {e['brazo_C_usage_abierto_medido']['input_tokens']} tok",
        f"C  output (abierto medido)    {e['brazo_C_usage_abierto_medido']['output_tokens']} tok",
        f"{e['formula']}",
        f"TOTAL                         USD {e['total_usd']:.4f}",
        "```",
        "",
        "## Sensibilidad (multiplicador extra sobre el output estimado)",
        "",
        "| mult out | total USD |",
        "|---|--:|",
        *[f"| ×{x['mult_out']} | {x['total_usd']:.4f} |"
          for x in e["sensibilidad_output"]],
        "",
        f"Bajo el tope 0,50 hasta ×1,3: "
        f"**{e['contra_tope']['bajo_tope_0_50_hasta_out_x1_3']}**",
        "",
    ])


def main() -> int:
    e = estimar()
    (cc.CONTROL_DIR / "estimacion_control_esq_p1bis.json").write_text(
        json.dumps(e, ensure_ascii=False, indent=1), encoding="utf-8")
    (cc.CONTROL_DIR / "estimacion_control_esq_p1bis.md").write_text(
        render_md(e), encoding="utf-8")
    print(f"total estimado: USD {e['total_usd']:.4f} | tope {e['tope_parcial_usd']}")
    print(f"-> {cc.CONTROL_DIR / 'estimacion_control_esq_p1bis.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
