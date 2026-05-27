"""
pipeline.py — Orquesta extracción + validación + retry + ensamblaje.

Función principal: run_pipeline(chunks, cache_dir) → dict con:
  - kg: {"nodes": [...], "edges": [...], "_meta": {...}}
  - metrics: dict con todas las métricas (cobertura, costo, retries, violaciones)
  - violation_samples: list de violaciones reales detectadas (sampleadas)
"""

from __future__ import annotations

import asyncio
import json
import os
import random
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Optional

import anthropic

from assemble import ChunkValidated, assemble
from extract import (
    DEFAULT_CONCURRENCY,
    ExtractionResult,
    ProgressTracker,
    extract_chunks,
    reflect_chunk,
)
from schema import PREDICATE_NAMES, ENTITY_TYPES
from validate import ValidationOutcome, validate, violations_to_feedback


def _count_cached(chunks: list, cache_dir: Optional[Path], suffix: str = "") -> tuple[int, int]:
    """Devuelve (cached, total_chunks). suffix='' para extract, '.reflect' para retry."""
    if cache_dir is None:
        return 0, len(chunks)
    cached = 0
    for c in chunks:
        cp = cache_dir / c.source_doc.replace(".pdf", "") / "raw" / f"{c.chunk_id}{suffix}.json"
        if cp.exists():
            try:
                d = json.load(cp.open())
                if not d.get("error"):
                    cached += 1
            except Exception:
                pass
    return cached, len(chunks)


async def _retry_pass(client, chunks_by_id, extract_results: list[ExtractionResult],
                      first_validations: dict[str, ValidationOutcome],
                      concurrency: int, cache_dir: Optional[Path],
                      tracker: Optional[ProgressTracker] = None) -> dict[str, ExtractionResult]:
    """Para los chunks marcados a retry, hace 1 retry con feedback. Devuelve dict por chunk_id."""
    sem = asyncio.Semaphore(concurrency)
    to_retry = [r for r in extract_results if first_validations[r.chunk_id].triggers_retry]
    if not to_retry:
        return {}

    async def _one(r: ExtractionResult):
        chunk = chunks_by_id[r.chunk_id]
        cp = None
        if cache_dir is not None:
            d = cache_dir / chunk.source_doc.replace(".pdf", "") / "raw"
            d.mkdir(parents=True, exist_ok=True)
            cp = d / f"{chunk.chunk_id}.reflect.json"
            if cp.exists():
                with cp.open() as f:
                    data = json.load(f)
                if not data.get("error"):
                    return ExtractionResult(
                        chunk_id=data["chunk_id"],
                        source_doc=data["source_doc"],
                        location=data["location"],
                        raw_output=data["raw_output"],
                        input_tokens=data["input_tokens"],
                        output_tokens=data["output_tokens"],
                        model=data["model"],
                        pass_kind=data["pass_kind"],
                        error=data.get("error"),
                    )
        feedback = violations_to_feedback(first_validations[r.chunk_id].violations)
        result = await reflect_chunk(client, chunk, r, feedback, sem, tracker=tracker)
        if cp and not result.error:
            with cp.open("w") as f:
                json.dump(result.to_dict(), f, ensure_ascii=False, indent=2)
        if tracker is not None:
            await tracker.update(result)
        return result

    tasks = [asyncio.create_task(_one(r)) for r in to_retry]
    results = await asyncio.gather(*tasks)
    return {r.chunk_id: r for r in results}


def _summarize_violations(viols: list) -> Counter:
    return Counter(v.code for v in viols)


async def run_pipeline(chunks: list, cache_dir: Optional[Path] = None,
                       concurrency: int = DEFAULT_CONCURRENCY,
                       max_violation_samples: int = 30) -> dict:
    """
    Orquesta el pipeline completo sobre `chunks` (lista de Chunk dataclass).
    """
    t0 = time.time()
    chunks_by_id = {c.chunk_id: c for c in chunks}

    # ---- Pasada 1: extracción ----
    cached_extract, total = _count_cached(chunks, cache_dir, suffix="")
    api_calls_extract = total - cached_extract
    print(
        f"[pipeline] PASS 1 extract: {total} chunks total, {cached_extract} cacheados, "
        f"{api_calls_extract} API calls esperadas (concurrency={concurrency})",
        flush=True,
    )
    extract_tracker = ProgressTracker(
        total_expected=max(api_calls_extract, 1), label="extract", print_every=5,
    )
    extract_results = await extract_chunks(
        chunks, concurrency=concurrency, cache_dir=cache_dir, tracker=extract_tracker,
    )
    print(f"[pipeline] PASS 1 done: {extract_tracker.summary()}", flush=True)

    # Validar pasada 1
    first_validations: dict[str, ValidationOutcome] = {}
    for r in extract_results:
        first_validations[r.chunk_id] = validate(r.raw_output, r.source_doc, r.location)

    # ---- Pasada 2: retry sobre los marcados ----
    to_retry_chunks = [chunks_by_id[r.chunk_id] for r in extract_results
                       if first_validations[r.chunk_id].triggers_retry]
    cached_retry, total_retry = _count_cached(to_retry_chunks, cache_dir, suffix=".reflect")
    api_calls_retry = total_retry - cached_retry
    print(
        f"[pipeline] PASS 2 retry: {total_retry} chunks marcados, {cached_retry} cacheados, "
        f"{api_calls_retry} API calls esperadas",
        flush=True,
    )
    retry_tracker = ProgressTracker(
        total_expected=max(api_calls_retry, 1), label="retry", print_every=5,
    )
    client = anthropic.AsyncAnthropic()
    retry_results: dict[str, ExtractionResult] = await _retry_pass(
        client, chunks_by_id, extract_results, first_validations,
        concurrency=concurrency, cache_dir=cache_dir, tracker=retry_tracker,
    )
    print(f"[pipeline] PASS 2 done: {retry_tracker.summary()}", flush=True)

    # Validar pasada 2 (sobre los que se reintentaron)
    second_validations: dict[str, ValidationOutcome] = {}
    for cid, r in retry_results.items():
        second_validations[cid] = validate(r.raw_output, r.source_doc, r.location)

    # Construir lista final de ChunkValidated (toma el mejor de los dos pases)
    validated_chunks: list[ChunkValidated] = []
    post_retry_residual = 0
    for r in extract_results:
        cid = r.chunk_id
        if cid in retry_results:
            outcome = second_validations[cid]
            post_retry_violation = outcome.triggers_retry
            if post_retry_violation:
                post_retry_residual += 1
        else:
            outcome = first_validations[cid]
            post_retry_violation = False
        ch = chunks_by_id[cid]
        validated_chunks.append(ChunkValidated(
            chunk_id=cid,
            source_doc=ch.source_doc,
            location=ch.location,
            clean_entities=outcome.clean_entities,
            clean_relations=outcome.clean_relations,
            post_retry_violation=post_retry_violation,
        ))

    # Ensamblaje
    kg = assemble(validated_chunks)

    # ---------------- Métricas ----------------
    n_chunks = len(chunks)
    productive_chunks = sum(1 for vc in validated_chunks if vc.clean_entities)
    cov_pct = 100.0 * productive_chunks / n_chunks if n_chunks else 0.0

    # Costo
    base_in = sum(r.input_tokens for r in extract_results)
    base_out = sum(r.output_tokens for r in extract_results)
    base_cost = sum(r.cost_usd() for r in extract_results)
    retry_in = sum(r.input_tokens for r in retry_results.values())
    retry_out = sum(r.output_tokens for r in retry_results.values())
    retry_cost = sum(r.cost_usd() for r in retry_results.values())
    total_cost = base_cost + retry_cost

    # Violaciones
    n_chunks_with_violations = sum(
        1 for v in first_validations.values() if v.violations
    )
    n_chunks_with_retry_trigger = sum(
        1 for v in first_validations.values() if v.triggers_retry
    )
    pct_violations = 100.0 * n_chunks_with_violations / n_chunks if n_chunks else 0.0
    pct_retry = 100.0 * n_chunks_with_retry_trigger / n_chunks if n_chunks else 0.0
    pct_residual = 100.0 * post_retry_residual / n_chunks if n_chunks else 0.0

    violation_counter_first = Counter()
    for v in first_validations.values():
        for vio in v.violations:
            violation_counter_first[vio.code] += 1

    # Cobertura por TO
    by_doc_chunks = defaultdict(int)
    by_doc_productive = defaultdict(int)
    for vc in validated_chunks:
        by_doc_chunks[vc.source_doc] += 1
        if vc.clean_entities:
            by_doc_productive[vc.source_doc] += 1
    coverage_by_doc = {
        d: {"chunks": by_doc_chunks[d],
            "productive": by_doc_productive[d],
            "pct": 100.0 * by_doc_productive[d] / by_doc_chunks[d] if by_doc_chunks[d] else 0.0}
        for d in by_doc_chunks
    }

    # Conteos por tipo / por predicado en el KG ensamblado
    nodes_by_type = Counter(n["type"] for n in kg["nodes"])
    edges_by_relation = Counter(e["relation"] for e in kg["edges"])

    # Distribución de predicados (incluye los no usados)
    predicate_distribution = {p: edges_by_relation.get(p, 0) for p in PREDICATE_NAMES}

    # Samples de violaciones (para el reporte)
    all_violations_with_ctx = []
    for cid, vo in first_validations.items():
        for v in vo.violations:
            all_violations_with_ctx.append({
                "chunk_id": cid,
                "code": v.code,
                "severity": v.severity,
                "msg": v.msg,
                "where": v.where,
                "detail": v.detail,
            })
    random.seed(42)
    sample_violations = random.sample(
        all_violations_with_ctx, min(max_violation_samples, len(all_violations_with_ctx))
    ) if all_violations_with_ctx else []

    elapsed = time.time() - t0

    metrics = {
        "n_chunks": n_chunks,
        "productive_chunks": productive_chunks,
        "coverage_pct": cov_pct,
        "coverage_by_doc": coverage_by_doc,
        "elapsed_seconds": round(elapsed, 1),
        "cost": {
            "extraction_usd": round(base_cost, 4),
            "retry_usd": round(retry_cost, 4),
            "total_usd": round(total_cost, 4),
            "retry_pct_of_total": round(100.0 * retry_cost / total_cost, 1) if total_cost else 0.0,
            "extraction_input_tokens": base_in,
            "extraction_output_tokens": base_out,
            "retry_input_tokens": retry_in,
            "retry_output_tokens": retry_out,
        },
        "validation": {
            "chunks_with_any_violation_first_pass": n_chunks_with_violations,
            "pct_chunks_with_violations": round(pct_violations, 1),
            "chunks_triggering_retry": n_chunks_with_retry_trigger,
            "pct_chunks_retry": round(pct_retry, 1),
            "chunks_with_post_retry_residual": post_retry_residual,
            "pct_chunks_post_retry_residual": round(pct_residual, 1),
            "violations_by_code_first_pass": dict(violation_counter_first),
        },
        "kg": {
            "n_nodes": len(kg["nodes"]),
            "n_edges": len(kg["edges"]),
            "density": round(len(kg["edges"]) / len(kg["nodes"]), 3) if kg["nodes"] else 0.0,
            "nodes_by_type": dict(nodes_by_type),
            "edges_by_relation": dict(edges_by_relation),
            "predicate_distribution": predicate_distribution,
            "unused_predicates": [p for p, c in predicate_distribution.items() if c == 0],
        },
    }

    return {
        "kg": kg,
        "metrics": metrics,
        "violation_samples": sample_violations,
    }
