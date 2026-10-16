#!/usr/bin/env python3
"""estimar_tramo2.py — Estimación del costo del tramo 2 de A2.1 (USD 0: solo lee metadata).

Cota por sesión desde lo MEDIDO en la corrida 2 de la fase B del banco
(smoke/resultados/faseB_corrida2/meta_*.json, costo R9 recomputado desde tokens con los
precios sellados), en el brazo vectorial, que tiene la misma tool y el mismo agente:
  · P0 y E2E de cada brazo de A2.1 = P0-vector y E2E-vector;
  · SMK-0i de cada brazo = SMK-0i-vector;
  · una sesión de H-B2 = la suma de las SMK-vector de sus preguntas, sin descontar el corte.
Es una cota: en la fase B `limite` era 10 por defecto y en A2.1 el servidor lo acota a 5,
y las sesiones con --max-turns chico cortan antes.

Uso: python3 -B estimar_tramo2.py   (escribe estimacion_tramo2.json junto a este archivo)
"""
from __future__ import annotations

import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
FASE_B = BANCO_DIR / "smoke" / "resultados" / "faseB_corrida2"
BRAZOS = ("fragmentos_bm25", "fragmentos_denso")


def main() -> int:
    costo, p0_ref = {}, None
    for p in sorted(FASE_B.glob("meta_*-vector.json")):
        m = json.loads(p.read_text(encoding="utf-8"))
        costo[m["pregunta_id"].rsplit("-", 1)[0]] = m["tokens_R9"]["costo_recomputado"]["total_usd"]
        if m["pregunta_id"] == "P0-vector":
            primera = next(t for t in m["tokens_R9"]["por_llamada_api"] if t.get("modelo") == m["modelos_R8"]["declarado"])
            p0_ref = primera.get("cache_creation_input_tokens") or primera.get("input_tokens")
    preguntas = [q["id"] for q in json.loads((BANCO_DIR / "smoke" / "preguntas_smoke.json").read_text(encoding="utf-8"))["preguntas"]]
    diseno = json.loads((AQUI / "diseno_HB2.json").read_text(encoding="utf-8"))
    smoke = {f"{k}-{b}": costo[k] for b in BRAZOS for k in ["P0"] + preguntas + ["E2E"]}
    hb2 = {s["id"]: round(sum(costo[i] for i in s["preguntas"]), 6) for s in diseno["sesiones"]}
    t_smoke, t_hb2 = round(sum(smoke.values()), 4), round(sum(hb2.values()), 4)
    est = {"unidad": "A2.1, tramo 1 — estimación del costo del tramo 2 (cota)",
           "comando": "python3 -B data/experiment/banco_mcp/a2_1/estimar_tramo2.py",
           "fuente": "smoke/resultados/faseB_corrida2/meta_*-vector.json (costo R9 recomputado)",
           "costo_medido_faseB_vector_usd": costo, "P0_faseB_referencia": p0_ref,
           "sesiones": {"paso1_smoke": smoke, "paso2_hb2": hb2},
           "n_sesiones": {"paso1_smoke": len(smoke), "paso2_hb2": len(hb2)},
           "costo_estimado_usd": {"paso1_smoke": t_smoke, "paso2_hb2": t_hb2, "total_tramo2": round(t_smoke + t_hb2, 4)},
           "guardas": {"autorizado_tope": 3.0, "freno": 2.0, "freno_proyeccion": 2.4, "max_budget_usd_por_sesion": 0.3,
                       "regla": "antes de cada sesión: acumulado R9 del tramo 2 + 0,30 > freno => FRENO sin lanzar"}}
    (AQUI / "estimacion_tramo2.json").write_text(json.dumps(est, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(est["costo_estimado_usd"], ensure_ascii=False), "| P0 ref", p0_ref)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
