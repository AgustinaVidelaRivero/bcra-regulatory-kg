"""
estimacion.py — Estimación PARAMETRIZADA del costo de una pasada de calibración
del juez de fidelidad EV2: 25 casos × N=3 repeticiones (etapa 2.e del mandato).

Qué se mide y qué se asume (todo visible en la salida):
  - MEDIDO: chars del system prompt real, y chars de pregunta+respuesta de los
    25 casos reales de U6 (lectura local, sin API).
  - PARÁMETRO: cantidad de criterios por pregunta (K) y chars por criterio
    (criterio + cita textual) — los criterios reales aún no existen; default
    K=4.1 (promedio del gold EV2: 164 criterios / 40 preguntas, número público
    del pre-registro) y 420 chars (criterio ~150 + cita ~250 + formato).
  - PARÁMETRO: chars por token (default 3.6, heurística castellano técnico).
  - PARÁMETRO: tokens de salida por llamada = base + K × por_criterio
    (defaults 40 y 90, del tamaño del JSON scripteado del selftest con
    justificaciones de ~120 chars — ver selftest_out/medicion_selftest.json).
  - PRECIOS: variables de línea de comandos (USD por MTok). Sin precios, el
    script emite solo tokens y la fórmula; el costo lo imprime únicamente con
    --precio-in y --precio-out provistos (la autorización de la etapa 3 llega
    con precios y tope; acá no se hardcodea ninguno).

Sin prompt caching en v1 (el system viaja completo en cada llamada; posible
ahorro futuro, se declara y no se descuenta).

Uso:
  .venv/bin/python data/experiment/ev2_juez/estimacion.py
  .venv/bin/python data/experiment/ev2_juez/estimacion.py \
      --precio-in <USD/MTok de entrada> --precio-out <USD/MTok de salida>
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import juez
from driver_calibracion import cargar_preguntas, cargar_respuestas

JUEZ_DIR = Path(__file__).resolve().parent


def main() -> int:
    ap = argparse.ArgumentParser(description="Estimación de costo de la calibración")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--k-criterios", type=float, default=4.1,
                    help="criterios por pregunta (parámetro; default 164/40 del gold EV2)")
    ap.add_argument("--chars-criterio", type=float, default=420.0,
                    help="chars por criterio con su cita y formato (parámetro)")
    ap.add_argument("--chars-por-token", type=float, default=3.6,
                    help="heurística chars→tokens para castellano técnico")
    ap.add_argument("--out-tokens-base", type=float, default=40.0)
    ap.add_argument("--out-tokens-por-criterio", type=float, default=90.0)
    ap.add_argument("--precio-in", type=float, default=None, help="USD por MTok de entrada")
    ap.add_argument("--precio-out", type=float, default=None, help="USD por MTok de salida")
    args = ap.parse_args()

    preguntas = cargar_preguntas()
    respuestas = cargar_respuestas()
    cpt = args.chars_por_token

    chars_system = len(juez.PROMPT_JUEZ)
    chars_casos = {q: len(preguntas[q]["pregunta"]) + len(respuestas[q]["respuesta"])
                   for q in preguntas}
    chars_criterios = args.k_criterios * args.chars_criterio
    overhead_chars = 120  # rótulos fijos del mensaje de usuario (PREGUNTA:/RESPUESTA:/…)

    in_por_llamada = {q: (chars_system + c + chars_criterios + overhead_chars) / cpt
                      for q, c in chars_casos.items()}
    out_por_llamada = args.out_tokens_base + args.k_criterios * args.out_tokens_por_criterio

    n_llamadas = len(preguntas) * args.reps
    tokens_in = sum(in_por_llamada.values()) * args.reps
    tokens_out = out_por_llamada * n_llamadas

    resumen = {
        "n_casos": len(preguntas),
        "reps": args.reps,
        "n_llamadas": n_llamadas,
        "medido": {
            "chars_system_prompt": chars_system,
            "chars_pregunta_respuesta_total_25": sum(chars_casos.values()),
            "chars_pregunta_respuesta_mediana": sorted(chars_casos.values())[len(chars_casos) // 2],
        },
        "parametros": {
            "k_criterios": args.k_criterios,
            "chars_criterio": args.chars_criterio,
            "chars_por_token": cpt,
            "out_tokens_base": args.out_tokens_base,
            "out_tokens_por_criterio": args.out_tokens_por_criterio,
        },
        "estimacion_tokens": {
            "input_por_llamada_promedio": round(tokens_in / n_llamadas),
            "output_por_llamada": round(out_por_llamada),
            "input_total": round(tokens_in),
            "output_total": round(tokens_out),
        },
        "formula_costo_usd": "input_total/1e6 * precio_in + output_total/1e6 * precio_out",
        "nota_prompt_caching": "sin prompt caching en v1; el system se paga entero en cada llamada",
    }
    if args.precio_in is not None and args.precio_out is not None:
        resumen["precios_usd_mtok"] = {"in": args.precio_in, "out": args.precio_out}
        resumen["costo_estimado_usd"] = round(
            tokens_in / 1e6 * args.precio_in + tokens_out / 1e6 * args.precio_out, 4)

    salida = JUEZ_DIR / "selftest_out" / "estimacion_calibracion.json"
    salida.parent.mkdir(exist_ok=True)
    salida.write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(resumen, ensure_ascii=False, indent=2))
    print(f"\n→ {salida}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
