"""
run_manual.py — Corre UNA pregunta del pool por vez (loop manual de la Fase 2.3).

Ejecuta una sola pregunta (por id) de un pool tipo dev_pool.json contra un grafo,
imprime un bloque de análisis, y ANEXA la traza a un archivo por corrida
(trazas/manual_<run>.json), recalculando los totales. Si la pregunta ya estaba
en el archivo, la reemplaza (idempotente).

Uso:
  python3 run_manual.py --run run_3 --id CQ-001
  python3 run_manual.py --run run_3 --id CQ-001 --pool queries/dev_pool.json
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from dotenv import load_dotenv

from loader import load_graph, EVAL_DIR
from harness import GraphAgent, TRAZAS_DIR, MODEL, TEMPERATURE, MAX_TOOL_CALLS


def _load_pool(path: Path) -> list:
    data = json.load(open(path, encoding="utf-8"))
    if isinstance(data, dict) and "preguntas" in data:
        return data["preguntas"]
    if isinstance(data, list):
        return data
    raise ValueError(f"Formato de pool no reconocido: {path}")


def _corrida_path(run_key: str) -> Path:
    return TRAZAS_DIR / f"manual_{run_key}.json"


def _append_trace(run_key: str, kg_path: str, tr_dict: dict) -> Path:
    TRAZAS_DIR.mkdir(parents=True, exist_ok=True)
    p = _corrida_path(run_key)
    if p.exists():
        payload = json.load(open(p, encoding="utf-8"))
    else:
        payload = {
            "corrida": {"run_key": run_key, "tipo": "loop_manual", "model": MODEL,
                        "temperature": TEMPERATURE, "max_tool_calls": MAX_TOOL_CALLS,
                        "source_kg": kg_path},
            "trazas": [],
        }
    payload["trazas"] = [t for t in payload["trazas"] if t.get("qid") != tr_dict["qid"]]
    payload["trazas"].append(tr_dict)
    ts = payload["trazas"]
    payload["totales"] = {
        "n_preguntas": len(ts),
        "tokens_in": sum(t["tokens_in"] for t in ts),
        "tokens_out": sum(t["tokens_out"] for t in ts),
        "cache_read": sum(t["cache_read"] for t in ts),
        "cache_write": sum(t["cache_write"] for t in ts),
        "costo_usd": round(sum(t["cost_usd"] for t in ts), 6),
        "latencia_total_s": round(sum(t["latency_s"] for t in ts), 3),
    }
    with open(p, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    return p


def _print_block(tr, q):
    fj = tr.final_json or {}
    print("=" * 80)
    print(f"[{tr.qid}] {tr.question}")
    if q.get("categoria"):
        print(f"  categoria={q['categoria']} dificultad={q.get('dificultad')} "
              f"tos_fuente={q.get('tos_fuente')}")
    print(f"  stop={tr.final_stop_reason} tools={tr.tool_calls_used} "
          f"hit_limit={tr.hit_tool_limit} trunc_maxtok={tr.truncated_max_tokens} "
          f"parse_ok={tr.parse_ok}")
    print(f"  respondible={fj.get('respondible')} | n_citas={len(fj.get('citas') or [])} "
          f"| unseen_raw={len(tr.citations_unseen_raw)} "
          f"unseen_norm={len(tr.citations_unseen_normalized)}")
    print(f"  tokens_in={tr.tokens_in} tokens_out={tr.tokens_out} "
          f"costo=${tr.cost_usd:.5f} latencia={tr.latency_s}s")
    if tr.error:
        print(f"  ERROR: {tr.error}")
    print("  secuencia de tools:")
    for s in tr.steps:
        inp = json.dumps(s["input"], ensure_ascii=False)
        print(f"    {s['n']:>2}. {s['tool']}({inp})")
    print("  respuesta:", (fj.get("respuesta", "") or "")[:500])
    print("  citas:", json.dumps(fj.get("citas"), ensure_ascii=False))
    if tr.citations_unseen_normalized:
        print("  CITAS NO-FIELES (normalizado):",
              json.dumps(tr.citations_unseen_normalized, ensure_ascii=False))
    print("=" * 80)


def main():
    load_dotenv(EVAL_DIR / ".env")
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--id", required=True, dest="qid")
    ap.add_argument("--pool", default=str(EVAL_DIR / "queries" / "dev_pool.json"))
    args = ap.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit(f"ERROR: ANTHROPIC_API_KEY no seteada en {EVAL_DIR/'.env'}")

    pool = _load_pool(Path(args.pool))
    q = next((x for x in pool if x.get("id") == args.qid), None)
    if q is None:
        raise SystemExit(f"id '{args.qid}' no está en {args.pool}")

    kg = load_graph(args.run)
    agent = GraphAgent(kg)
    tr = agent.ask(q["id"], q["pregunta"])
    _print_block(tr, q)
    p = _append_trace(args.run, str(kg.path), vars(tr))
    print(f"Anexado a: {p}")


if __name__ == "__main__":
    main()
