"""
costo_p3b2.py — U-PROMPT-R2, P3b-2 (USD 0, sin API): el costo re-estimado de la pareada (P4) y de U-REEXT-T0 con lo
que agrega P3b, como delta sobre la base de P1 (p1/salida/censo_p1.json: escenario B central, el prefijo congelado
en P2, y la estimación de P4), con sus mismas calibraciones y tarifas:
  - prefijo: +Δ caracteres del system (P2 → re-congelado) × la recta de 3 parámetros de P1 (tokens por carácter
    del system); el tool schema no cambia. Se lee en cada llamada de E1 (tarifa de lectura) y se escribe en las
    escrituras de caché de la base;
  - mensaje de E1: el delta exacto de caracteres por unidad (prompt_r2b.build_user_message_r2b contra el borrador
    de P1, mensaje_r2_borrador.build_user_message_r2) sobre la e0-r2 de la tanda 0 × tokens por carácter de mensaje;
  - salida de E1 por g: los ítems nuevos × los caracteres por ítem de la composición de P1 (F1-A: 133.245 entre 706)
    × tokens por carácter de salida; E3 renderiza el 70 % de esos caracteres, como en P1;
  - E3: la NOTA de las omisiones (i) como cota alta, en todas las llamadas de E3 (la tanda 0 no tiene categorías);
  - reintentos del ratchet: el prefijo, la parte del mensaje que crece y el aviso de la nota (defensa 1);
  - j: los 4 reintentos que la lectura con reparo daría en la tanda 0 (p3b/salida/lazo_e3_p3b.json), a la tarifa
    r2 del reintento de E1 (censo_p1, pata_e3_base) más una re-verificación de E3.
No estima la salida de a y b (modalidad y consecuencia copiadas) ni la de h: la mide P4.

Escribe solo en --salida (costo_p3b2.json). Sobre una copia del repo (regla l).

Uso (desde la raíz de la copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3b2/costo_p3b2.py --salida DIR
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PR2 = AQUI.parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for p in (REX / "e1_extractor", REX / "e3_verificador", PR2 / "p1"):
    sys.path.insert(0, str(p))
import comun_e1  # noqa: E402
import prompt_r2b as P  # noqa: E402
import prompt_v3_b54 as v3  # noqa: E402
import prompt_e3  # noqa: E402
import ratchet_e3  # noqa: E402
import mensaje_r2_borrador as MB  # noqa: E402

CENSO = PR2 / "p1" / "salida" / "censo_p1.json"
LAZO = PR2 / "p3b" / "salida" / "lazo_e3_p3b.json"
MENSAJE_P3B = PR2 / "p3b" / "salida" / "mensaje_p3b.json"          # ítems antes y después de g (P3b-1)
E0_R2 = REX / "e0_chunking" / "salida_tanda0_r2"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
PREC = {"in": 1.00, "out": 5.00, "cw": 1.25, "cr": 0.10}         # E1, USD/MTok (runner_corpus.py:18)
PREC_E3 = {"in": 2.00, "out": 10.00, "cw": 2.50, "cr": 0.20}      # E3 (runner_corpus.py:19)
F1A_CHARS, F1A_ITEMS = 133245, 706                                 # diseno_prefijo_r2.md, tabla de deltas (F1-A)
RENDER_E3 = 0.7                                                    # fracción renderizada en E3 (P1)
FIJOS_P4 = ("cap::1.2", "ric::9.2.1", "cla::5.1.1.1", "pro::1.1.2.5", "cap::6.2.2.6")
BKL0035 = ("ctacte::8.3::intro", "ctacte::8.4::intro", "ctacte::6.4.7::intro")
N_P4_OTROS = 40 + 8 + 8                                            # sorteados, fuera de muestra nuevo y casos F1-A


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    sal = ap.parse_args().salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    sal.mkdir(parents=True, exist_ok=True)
    censo = json.loads(CENSO.read_text(encoding="utf-8"))
    lazo = json.loads(LAZO.read_text(encoding="utf-8"))["corridas"]["salida_dirigida"]["costos"]
    k_sys = censo["calibracion"]["prefijo"]["recta_3p"][1]
    k_msg = censo["calibracion"]["mensaje"]["tokens_por_caracter"]
    k_out = censo["calibracion"]["salida"]["tokens_por_caracter"]
    base = censo["costos"]["B_central"]
    p4 = censo["estimacion_p4"]["total"]
    t0 = censo["tanda0_fases_cerradas"]
    n = t0["n_e1"]
    llamadas_e3, reint = t0["e3_tokens"]["llamadas"], t0["e3_tokens"]["reintentos_e1"]
    n_escr = base["escrituras_de_cache"]

    d_sys = len(P.PREFIJO_SISTEMA_R2B) - len(P.PREFIJO_SISTEMA_R2B_P2)
    d_pref_tok = d_sys * k_sys
    chunks = comun_e1.cargar_chunks(TOS, e0_dir=E0_R2)
    d_msg = {c["id"]: len(P.build_user_message_r2b(c)) - len(MB.build_user_message_r2(
        c, v3.ROL_POR_TO_V3, comun_e1.puntos_admitidos, comun_e1.es_mini_chunk)) for c in chunks}
    cambian = [k for k, v in d_msg.items() if v]
    d_msg_tot = sum(d_msg.values())
    g = json.loads(MENSAJE_P3B.read_text(encoding="utf-8"))["g_items"]
    items_hoy, items_p3b = g["hoy"], sum(1 for c in chunks if P.es_item(c))
    assert items_p3b == g["con_la_regla_nueva"], "la regla g implementada no da el conteo del diseño"
    nuevos = items_p3b - items_hoy
    d_out_chars = nuevos * F1A_CHARS / F1A_ITEMS
    nota_tok = len(prompt_e3.NOTA_E3_OMISIONES) * k_msg
    aviso_tok = (len(ratchet_e3.AVISO_NOTA_REINTENTO) + 2) * k_msg
    r2_reint = p4["pata_e3_base"]["reintento_e1_r2_usd"]

    # ---- U-REEXT-T0 (2.434 unidades) ----
    t = {
        "e1_prefijo_lecturas": (n - n_escr) * d_pref_tok * PREC["cr"] / 1e6,
        "e1_prefijo_escrituras": n_escr * d_pref_tok * PREC["cw"] / 1e6,
        "e1_mensaje": d_msg_tot * k_msg * PREC["in"] / 1e6,
        "e1_salida_items_g": d_out_chars * k_out * PREC["out"] / 1e6,
        "e3_render_salida_g": RENDER_E3 * d_out_chars * k_msg * PREC_E3["in"] / 1e6 * (llamadas_e3 / n),
        "e3_nota_omisiones_cota_alta": llamadas_e3 * nota_tok * PREC_E3["in"] / 1e6,
        "reintentos_prefijo": reint * d_pref_tok * PREC["cr"] / 1e6,
        "reintentos_mensaje": reint / n * d_msg_tot * k_msg * PREC["in"] / 1e6,
        "reintentos_aviso_de_la_nota": reint * aviso_tok * PREC["in"] / 1e6,
        "j_reintentos_tras_la_lectura": 4 * (r2_reint + lazo["e3_usd_por_llamada"]),
    }
    delta_t0 = sum(t.values())
    nuevo_t0 = base["total_usd"] + delta_t0

    # ---- P4, la pareada ----
    por_unidad_msg = d_msg_tot / n
    por_unidad_out = d_out_chars / n
    llamadas_p4 = len(FIJOS_P4) + len(BKL0035) + N_P4_OTROS
    msg_p4_chars = sum(d_msg.get(i, 0) for i in FIJOS_P4 + BKL0035) + N_P4_OTROS * por_unidad_msg
    q = {
        "prefijo_lecturas": (llamadas_p4 - 1) * d_pref_tok * PREC["cr"] / 1e6,
        "prefijo_escritura": d_pref_tok * PREC["cw"] / 1e6,
        "mensaje": msg_p4_chars * k_msg * PREC["in"] / 1e6,
        "salida_items_g": llamadas_p4 * por_unidad_out * k_out * PREC["out"] / 1e6,
        "pata_e3_nota_omisiones_central": 4 * nota_tok * PREC_E3["in"] / 1e6,
    }
    q_alto_extra = 4 * nota_tok * PREC_E3["in"] / 1e6 + 4 * (d_pref_tok * PREC["cr"] + aviso_tok * PREC["in"]) / 1e6
    delta_p4 = sum(q.values())
    res = {
        "comando": "data/experiment/prompt_r2/p3b2/costo_p3b2.py --salida DIR",
        "base": {"fuente": "p1/salida/censo_p1.json (costos.B_central, estimacion_p4.total)",
                 "u_reext_t0_central_usd": base["total_usd"], "p4_central_usd": p4["central"],
                 "p4_alto_usd": p4["alto"]},
        "prefijo": {"caracteres_system_p2": len(P.PREFIJO_SISTEMA_R2B_P2),
                    "caracteres_system_p3b": len(P.PREFIJO_SISTEMA_R2B), "delta_caracteres": d_sys,
                    "tokens_por_caracter_system": k_sys, "delta_tokens": round(d_pref_tok, 1),
                    "tokens_base_recta_3p": base["prefijo_tokens"],
                    "tokens_estimados": round(base["prefijo_tokens"] + d_pref_tok)},
        "mensaje": {"unidades": len(chunks), "unidades_que_cambian": len(cambian),
                    "delta_caracteres_total": d_msg_tot, "delta_tokens_total": round(d_msg_tot * k_msg)},
        "salida_g": {"items_hoy": items_hoy, "items_p3b": items_p3b, "items_nuevos": nuevos,
                     "caracteres_por_item": round(F1A_CHARS / F1A_ITEMS, 1), "delta_caracteres": round(d_out_chars),
                     "delta_tokens": round(d_out_chars * k_out)},
        "nota_e3_tokens": round(nota_tok, 1), "aviso_reintento_tokens": round(aviso_tok, 1),
        "llamadas_e3_tanda0": llamadas_e3, "reintentos_e1_tanda0": reint,
        "u_reext_t0": {"componentes_usd": {k: round(v, 4) for k, v in t.items()}, "delta_usd": round(delta_t0, 4),
                       "central_usd": round(nuevo_t0, 2), "con_factor_1_4_usd": round(nuevo_t0 * 1.4, 2),
                       "tope_usd": 69},
        "p4": {"llamadas_e1_brazo_nuevo": llamadas_p4, "componentes_usd": {k: round(v, 5) for k, v in q.items()},
               "delta_central_usd": round(delta_p4, 4), "delta_alto_usd": round(delta_p4 + q_alto_extra, 4),
               "central_usd": round(p4["central"] + delta_p4, 4),
               "alto_usd": round(p4["alto"] + delta_p4 + q_alto_extra, 4)},
        "no_estimado": "salida de a y b (modalidad y consecuencia copiadas) y de h; la mide P4",
    }
    (sal / "costo_p3b2.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: res[k] for k in ("prefijo", "mensaje", "salida_g", "u_reext_t0", "p4")}, ensure_ascii=False,
                     indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
