"""
estimacion_fidelidad.py — Estimación PARAMETRIZADA del costo de la fase B
(120 respuestas × N=3 = 360 llamadas al juez), SIN precios (fase A.d).

Qué se mide (offline, sin API):
  - MEDIDO: chars de los 120 mensajes REALES que viajarían al juez (system +
    usuario), construidos con juez.construir_kwargs sobre la vista ciega
    (carga/mensajes_reales_medicion.json, escrito por preparar_carga.py).
  - MEDIDO: ratio chars→tokens de entrada del MISMO instrumento en las 75
    llamadas reales de la calibración válida (dbs cache_app/juez_calibracion_
    app_r{1,2,3}.db: chars de request_json vs input_tokens facturados; misma
    system prompt, mismo formato de mensaje, mismo modelo). Se usa la mediana
    y se reporta el rango (min/max) como banda.
  - MEDIDO: tokens de salida por llamada en esas 75 llamadas, en función del
    número de criterios K (ajuste lineal out = a + b·K por mínimos cuadrados,
    más el máximo observado por K como cota superior).
  - PARÁMETRO: N=3 (pre-registro §4). Sin prompt caching (v1 del juez lo
    ignora; el system se paga entero en cada llamada), max_tokens 3000.
  - PRECIOS: solo como variables de CLI; sin ellos el script emite tokens y
    la fórmula. Nada se hardcodea.

Uso:
  .venv/bin/python -B data/experiment/ev2_fidelidad_eval/code/estimacion_fidelidad.py
  .venv/bin/python -B .../estimacion_fidelidad.py --precio-in <USD/MTok> --precio-out <USD/MTok>
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import statistics as st
import sys
from collections import defaultdict
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CODE_DIR))
import comun_fidelidad as cf   # noqa: E402
from comun_fidelidad import juez  # noqa: E402

CALIB_DBS = [cf.JUEZ_DIR / "cache_app" / f"juez_calibracion_app_r{r}.db" for r in (1, 2, 3)]
EST_DIR = cf.UNIDAD_DIR / "estimacion"


def medir_calibracion() -> dict:
    """chars/token de entrada y out-tokens por K, desde las 75 llamadas reales."""
    ratios, out_por_k, filas = [], defaultdict(list), 0
    prompt_ok = True
    for p in CALIB_DBS:
        conn = sqlite3.connect(str(p))
        for i, o, rj in conn.execute("SELECT input_tokens, output_tokens, request_json FROM cache"):
            r = json.loads(rj)
            u = r["messages"][0]["content"]
            chars = len(r["system"]) + len(u)
            k = int(u.split("CRITERIOS (", 1)[1].split(")", 1)[0])
            ratios.append(chars / i)
            out_por_k[k].append(o)
            filas += 1
            prompt_ok &= (r["system"] == juez.PROMPT_JUEZ and r["model"] == juez.MODELO)
        conn.close()
    # ajuste lineal out = a + b·K
    xs = [k for k, v in out_por_k.items() for _ in v]
    ys = [o for v in out_por_k.values() for o in v]
    mx, my = st.mean(xs), st.mean(ys)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    a = my - b * mx
    return {"n_llamadas_calibracion": filas, "mismo_prompt_y_modelo": prompt_ok,
            "chars_por_token_in": {"mediana": round(st.median(ratios), 4),
                                   "min": round(min(ratios), 4), "max": round(max(ratios), 4)},
            "out_tokens_por_k": {k: {"n": len(v), "media": round(st.mean(v), 1), "max": max(v)}
                                 for k, v in sorted(out_por_k.items())},
            "ajuste_out": {"a": round(a, 2), "b": round(b, 2), "formula": "out ≈ a + b·K"}}


def main() -> int:
    ap = argparse.ArgumentParser(description="Estimación de la fase B (sin precios por defecto)")
    ap.add_argument("--reps", type=int, default=cf.REPS)
    ap.add_argument("--precio-in", type=float, default=None, help="USD por MTok de entrada")
    ap.add_argument("--precio-out", type=float, default=None, help="USD por MTok de salida")
    args = ap.parse_args()

    med_path = cf.CARGA_DIR / "mensajes_reales_medicion.json"
    med = json.loads(med_path.read_text(encoding="utf-8"))
    if med["prompt_sha256"] != cf.PROMPT_SHA256_ESPERADO or med["n"] != cf.N_RESPUESTAS:
        raise RuntimeError("medición de mensajes no corresponde al prompt v1 / 120 respuestas")
    cal = medir_calibracion()
    cpt = cal["chars_por_token_in"]
    a, b = cal["ajuste_out"]["a"], cal["ajuste_out"]["b"]

    chars_total_una_pasada = sum(m["chars_system"] + m["chars_usuario"] for m in med["mensajes"])
    n_llam = med["n"] * args.reps
    tin_med = chars_total_una_pasada / cpt["mediana"] * args.reps
    tin_max = chars_total_una_pasada / cpt["min"] * args.reps      # menos chars/token → más tokens
    tin_min = chars_total_una_pasada / cpt["max"] * args.reps
    ks = [m["n_criterios"] for m in med["mensajes"]]
    tout_med = sum(a + b * k for k in ks) * args.reps
    # cota superior de salida: máximo observado por K en calibración (K=2..5 cubre el gold EV2)
    max_por_k = {int(k): v["max"] for k, v in cal["out_tokens_por_k"].items()}
    tout_max = sum(max_por_k.get(k, a + b * k) for k in ks) * args.reps

    resumen = {
        "n_respuestas": med["n"], "reps": args.reps, "n_llamadas": n_llam,
        "modelo": med["modelo"], "max_tokens": med["max_tokens"], "prompt_sha256": med["prompt_sha256"],
        "medido_mensajes_reales": {
            "chars_system": med["mensajes"][0]["chars_system"],
            "chars_usuario_total_120": sum(m["chars_usuario"] for m in med["mensajes"]),
            "chars_usuario_mediana": st.median(m["chars_usuario"] for m in med["mensajes"]),
            "chars_usuario_max": max(m["chars_usuario"] for m in med["mensajes"]),
            "chars_total_una_pasada": chars_total_una_pasada,
            "criterios_por_mensaje": dict(sorted(__import__("collections").Counter(ks).items())),
        },
        "medido_calibracion": cal,
        "estimacion_tokens": {
            "input_total": {"central": round(tin_med), "banda_min": round(tin_min), "banda_max": round(tin_max)},
            "output_total": {"central": round(tout_med), "cota_max_observada": round(tout_max)},
            "input_por_llamada_promedio": round(tin_med / n_llam),
            "output_por_llamada_promedio": round(tout_med / n_llam),
        },
        "formula_costo_usd": "input_total/1e6 × precio_in + output_total/1e6 × precio_out",
        "notas": ["sin prompt caching (system pagado entero por llamada, como en calibración)",
                  "ratio chars→tokens y salida por K medidos sobre las 75 llamadas reales de "
                  "calibración (mismo prompt, modelo y formato); las respuestas de EV2 son más largas "
                  "que las de U6, por eso la entrada se estima con los chars REALES de los 120 mensajes",
                  "el freno por proyección de la fase B recalcula el gasto real desde las dbs antes de cada llamada"],
    }
    if args.precio_in is not None and args.precio_out is not None:
        resumen["precios_usd_mtok"] = {"in": args.precio_in, "out": args.precio_out}
        c = lambda ti, to: round(ti / 1e6 * args.precio_in + to / 1e6 * args.precio_out, 4)
        resumen["costo_estimado_usd"] = {"central": c(tin_med, tout_med),
                                         "banda_max": c(tin_max, tout_max),
                                         "banda_min": c(tin_min, tout_med)}
    EST_DIR.mkdir(exist_ok=True)
    (EST_DIR / "estimacion_fase_b.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2),
                                                    encoding="utf-8")
    md = ["# Estimación fase B — fidelidad EV2 (120 × N=3 = 360 llamadas al juez v1)", "",
          f"- Mensajes reales medidos: {med['n']} (chars system {resumen['medido_mensajes_reales']['chars_system']}; "
          f"usuario total {resumen['medido_mensajes_reales']['chars_usuario_total_120']}, mediana "
          f"{resumen['medido_mensajes_reales']['chars_usuario_mediana']}, máx {resumen['medido_mensajes_reales']['chars_usuario_max']}); "
          f"criterios por mensaje {resumen['medido_mensajes_reales']['criterios_por_mensaje']}.",
          f"- Calibración (75 llamadas reales, mismo prompt/modelo: {cal['mismo_prompt_y_modelo']}): chars/token de entrada "
          f"mediana {cpt['mediana']} [{cpt['min']}, {cpt['max']}]; salida ≈ {a} + {b}·K tokens; máx observado por K "
          f"{ {k: v['max'] for k, v in cal['out_tokens_por_k'].items()} }.",
          f"- Tokens estimados ({n_llam} llamadas): entrada central {round(tin_med)} [{round(tin_min)}, {round(tin_max)}]; "
          f"salida central {round(tout_med)} (cota máx observada {round(tout_max)}).",
          f"- Fórmula: {resumen['formula_costo_usd']}. Sin precios en este archivo.", ""]
    if "costo_estimado_usd" in resumen:
        md.append(f"- Con precios {resumen['precios_usd_mtok']}: {resumen['costo_estimado_usd']}")
    (EST_DIR / "estimacion_fase_b.md").write_text("\n".join(md), encoding="utf-8")
    print(json.dumps(resumen, ensure_ascii=False, indent=2))
    print(f"\n→ {EST_DIR / 'estimacion_fase_b.json'}\n→ {EST_DIR / 'estimacion_fase_b.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
