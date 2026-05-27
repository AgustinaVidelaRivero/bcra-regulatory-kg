"""
run_full.py — Pipeline completo sobre los 5 TOs del subset.

Procesa los 5 PDFs (incluyendo Protección al Usuario — reusa el cache del
smoke, no rehace llamadas). Ensambla el KG global, genera kg.json,
kg_visual.html y métricas para el report.

Uso:
    python run_full.py [--limit N] [--concurrency N]

Logging (FIX 1 post-mortem):
    - Header con totales esperados (chunks API vs cached).
    - Cada 5 chunks completados: progreso + costo + rate + 429s + ETA.
    - Cada 429/timeout/fallo definitivo: línea individual inmediata.
    - stdout flushed inmediatamente para tail -f en otra terminal.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from chunking import chunk_subset
from pipeline import run_pipeline
from visualize import render


def _load_env():
    env_path = HERE / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            current = os.environ.get(k, "")
            if not current:
                os.environ[k] = v


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None,
                        help="Limit to first N chunks NOT yet cached (for dry-run).")
    parser.add_argument("--concurrency", type=int, default=2,
                        help="Concurrent API calls (default 2, was 3).")
    parser.add_argument("--no-write-final", action="store_true",
                        help="Skip writing kg.json + kg_visual.html (dry-run mode).")
    parser.add_argument("--exclude-docs", type=str, default="",
                        help="Comma-separated doc_ids to EXCLUDE from this run (still chunked, but not sent to LLM).")
    parser.add_argument("--only-docs", type=str, default="",
                        help="Comma-separated doc_ids: process ONLY these (overrides exclude).")
    args = parser.parse_args()

    _load_env()
    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: ANTHROPIC_API_KEY no está seteada. Completá code/.env.", file=sys.stderr, flush=True)
        sys.exit(1)

    repo_root = HERE.parents[3]
    subset = repo_root / "data" / "experiment" / "subset"
    cache_dir = HERE / "cache"
    run_dir = HERE.parent  # data/experiment/run_2_papers

    t_wall = time.time()
    print(f"[run_full] START wall-clock={time.strftime('%H:%M:%S')}", flush=True)
    print("[run_full] Chunking los 5 TOs ...", flush=True)
    docs = chunk_subset(subset, cache_dir)
    all_chunks = []
    excluded = {x.strip() for x in args.exclude_docs.split(",") if x.strip()}
    only = {x.strip() for x in args.only_docs.split(",") if x.strip()}
    for doc_id, chunks in docs.items():
        mark = ""
        if only:
            if doc_id not in only:
                mark = " [SKIPPED — not in --only-docs]"
                print(f"[run_full]   {doc_id}: {len(chunks)} chunks{mark}", flush=True)
                continue
        elif doc_id in excluded:
            mark = " [SKIPPED — in --exclude-docs]"
            print(f"[run_full]   {doc_id}: {len(chunks)} chunks{mark}", flush=True)
            continue
        print(f"[run_full]   {doc_id}: {len(chunks)} chunks", flush=True)
        all_chunks.extend(chunks)
    print(f"[run_full]   chunks a procesar en esta corrida: {len(all_chunks)}", flush=True)

    if args.limit is not None:
        # Filtrar a los primeros N chunks que NO están cacheados (para dry-run)
        not_cached = []
        for c in all_chunks:
            cp = cache_dir / c.source_doc.replace(".pdf", "") / "raw" / f"{c.chunk_id}.json"
            if not cp.exists():
                not_cached.append(c)
        selected_new = not_cached[: args.limit]
        # Para el dry-run, procesar SOLO esos N nuevos (no necesitamos cached para validar logging).
        all_chunks = selected_new
        print(f"[run_full] DRY-RUN MODE: limitando a {len(all_chunks)} chunks NO cacheados", flush=True)
        for c in all_chunks:
            print(f"[run_full]   - {c.chunk_id} ({len(c.text)} chars, {c.source_doc})", flush=True)

    print(f"[run_full] Running pipeline (concurrency={args.concurrency}, Haiku 4.5) ...", flush=True)
    result = asyncio.run(run_pipeline(all_chunks, cache_dir=cache_dir, concurrency=args.concurrency))

    # Persistir métricas
    (cache_dir / "full_metrics.json").write_text(
        json.dumps({
            "metrics": result["metrics"],
            "violation_samples": result["violation_samples"],
        }, ensure_ascii=False, indent=2)
    )

    if not args.no_write_final:
        # kg.json en la carpeta del run (formato sección b del protocolo)
        kg_clean = {"nodes": result["kg"]["nodes"], "edges": result["kg"]["edges"]}
        (run_dir / "kg.json").write_text(json.dumps(kg_clean, ensure_ascii=False, indent=2))

        # Visualización
        render(result["kg"], run_dir / "kg_visual.html")

    wall = time.time() - t_wall
    m = result["metrics"]
    print(f"\n[run_full] DONE wall-clock={wall/60:.1f} min", flush=True)
    print(f"  Nodos: {m['kg']['n_nodes']}  Edges: {m['kg']['n_edges']}  Densidad: {m['kg']['density']}", flush=True)
    print(f"  Costo total reportado por pipeline: USD {m['cost']['total_usd']:.4f}", flush=True)
    print(f"  Retry rate: {m['validation']['pct_chunks_retry']}%", flush=True)
    if not args.no_write_final:
        print(f"  → kg.json + kg_visual.html escritos en {run_dir}", flush=True)
    else:
        print(f"  (--no-write-final: no se escribió kg.json/kg_visual.html)", flush=True)


if __name__ == "__main__":
    main()
