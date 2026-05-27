"""
run_smoke.py — Smoke test del pipeline sobre 1 TO (Protección al Usuario).

Uso:
    python run_smoke.py

Salida:
    cache/smoke_metrics.json     métricas + violation samples
    cache/smoke_kg.json          KG ensamblado del smoke
    cache/smoke_summary.md       resumen humano

Stop condition (schema.md §6): si pct_chunks_retry > 40%, imprime ALERT
y exit code 2 (señal al humano de parar antes del full run).
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path

# Local imports (este script vive en code/)
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from chunking import chunk_subset
from pipeline import run_pipeline


# Cargar .env si existe
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
            # Pisar si la variable está ausente O si está presente pero vacía.
            current = os.environ.get(k, "")
            if not current:
                os.environ[k] = v


SMOKE_DOC = "TO_proteccion_usuarios_servicios_financieros_actual"


def main():
    _load_env()
    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: ANTHROPIC_API_KEY no está seteada. Completá code/.env.", file=sys.stderr)
        sys.exit(1)

    repo_root = HERE.parents[3]   # .../bcra-regulatory-kg
    subset = repo_root / "data" / "experiment" / "subset"
    cache_dir = HERE / "cache"

    print(f"Chunking {SMOKE_DOC} ...")
    docs = chunk_subset(subset, cache_dir, only_doc=SMOKE_DOC)
    chunks = docs[SMOKE_DOC]
    print(f"  → {len(chunks)} chunks")

    print(f"Running pipeline (concurrency=3, Haiku 4.5) ...")
    result = asyncio.run(run_pipeline(chunks, cache_dir=cache_dir, concurrency=3))

    # Persistir outputs
    (cache_dir / "smoke_metrics.json").write_text(
        json.dumps({
            "metrics": result["metrics"],
            "violation_samples": result["violation_samples"],
        }, ensure_ascii=False, indent=2)
    )
    (cache_dir / "smoke_kg.json").write_text(
        json.dumps(result["kg"], ensure_ascii=False, indent=2)
    )

    m = result["metrics"]
    summary = []
    summary.append(f"# Smoke test summary — {SMOKE_DOC}\n")
    summary.append(f"- Chunks: {m['n_chunks']}")
    summary.append(f"- Chunks productivos (con ≥1 entity tras validación): {m['productive_chunks']} ({m['coverage_pct']:.1f}%)")
    summary.append(f"- Tiempo: {m['elapsed_seconds']:.1f} s")
    summary.append(f"- Costo extracción base: USD {m['cost']['extraction_usd']:.4f}")
    summary.append(f"- Costo retry: USD {m['cost']['retry_usd']:.4f} ({m['cost']['retry_pct_of_total']:.1f}% del total)")
    summary.append(f"- Costo total smoke: USD {m['cost']['total_usd']:.4f}")
    summary.append(f"- % chunks con ≥1 violación 1ª pasada: {m['validation']['pct_chunks_with_violations']}%")
    summary.append(f"- % chunks que dispararon retry: {m['validation']['pct_chunks_retry']}%")
    summary.append(f"- % chunks con violaciones POST-retry (conservados con flag): {m['validation']['pct_chunks_post_retry_residual']}%")
    summary.append(f"- Violaciones por código (1ª pasada): {m['validation']['violations_by_code_first_pass']}")
    summary.append(f"- Nodos: {m['kg']['n_nodes']}  |  Edges: {m['kg']['n_edges']}  |  Densidad: {m['kg']['density']}")
    summary.append(f"- Nodos por tipo: {m['kg']['nodes_by_type']}")
    summary.append(f"- Edges por predicado: {m['kg']['edges_by_relation']}")
    summary.append(f"- Predicados sin uso: {m['kg']['unused_predicates']}")
    (cache_dir / "smoke_summary.md").write_text("\n".join(summary))

    print("\n".join(summary))

    if m["validation"]["pct_chunks_retry"] > 40.0:
        print("\n*** ALERT *** Retry rate > 40%. Schema demasiado estricto o feedback insuficiente.")
        print("Parar y discutir con humano antes del full run.")
        sys.exit(2)


if __name__ == "__main__":
    main()
