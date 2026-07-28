#!/usr/bin/env python3
"""Deriva las copias por corrida del mandato (PASO 2, formato de registro):
`evaluacion_escalon1/corridas/<grafo>/<id>_r<N>.json` con respuesta final,
traza de tools truncada (steps del harness), pasos, tokens y costo.

Solo LEE las trazas del runner (posthoc_run/traces/escalon1_r{N}/{grafo}/)
y escribe dentro de evaluacion_escalon1/. No toca nada congelado.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
TRACES = HERE.parent / "evaluacion" / "posthoc_run" / "traces"
OUT = HERE / "corridas"
GRAFOS = ("run_3", "grafo_v2")
REPS = (1, 2, 3)

n_out = 0
for g in GRAFOS:
    (OUT / g).mkdir(parents=True, exist_ok=True)
    for rep in REPS:
        src_dir = TRACES / f"escalon1_r{rep}" / g
        for f in sorted(src_dir.glob("EV1-*.json")):
            reps = json.load(open(f, encoding="utf-8"))
            assert len(reps) == 1, f"{f}: esperaba 1 rep, hay {len(reps)}"
            r = reps[0]
            t = r["trace"]
            derived = {
                "id": r["qid"],
                "grafo": g,
                "replica": rep,
                "failed_trace": r["failed_trace"],
                "respuesta_final": t.get("final_json"),
                "respuesta_cruda": t.get("final_raw"),
                "pasos": t.get("tool_calls_used"),
                "hit_tool_limit": t.get("hit_tool_limit"),
                "traza_tools_truncada": t.get("steps"),
                "tokens": {
                    "in": t.get("tokens_in"), "out": t.get("tokens_out"),
                    "cache_read": t.get("cache_read"),
                    "cache_write": t.get("cache_write"),
                },
                "costo_usd": {
                    "agente": t.get("cost_usd"),
                    "juez": r.get("judge_cost"),
                    "total": round((t.get("cost_usd") or 0)
                                   + (r.get("judge_cost") or 0), 6),
                },
            }
            out_f = OUT / g / f"{r['qid']}_r{rep}.json"
            json.dump(derived, open(out_f, "w", encoding="utf-8"),
                      ensure_ascii=False, indent=2)
            n_out += 1
print(f"OK: {n_out} archivos derivados en {OUT}")
