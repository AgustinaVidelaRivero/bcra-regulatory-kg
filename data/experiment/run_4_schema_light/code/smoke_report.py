"""
Reporte del smoke test (control point 2).

Lee todas las extracciones cacheadas para el TO indicado y produce el
reporte CRUDO que la autora pidió. No canoniza, no fusiona, no filtra
beyond lo que ya hizo extract.py.

Reporta:
- Lista completa de tipos crudos con frecuencia.
- Distribución de longitud de labels (mediana, p90, máximo) en palabras.
- Top 30 predicados crudos por frecuencia + total de predicados únicos.
- Muestra al azar de 20 entities (name + type_raw + provenance + description truncada).
- Cuenta de relations cuyo source o target no resuelve a un nodo extraído (orfandad).
- Cuenta de chunks failed y de chunks con output vacío.
- Costo y métricas agregadas.
"""

import json
import random
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

EXTRACT_DIR = Path(__file__).resolve().parent / "cache" / "extract"
FAILURES_PATH = EXTRACT_DIR / "_failures.jsonl"
CHUNKS_DIR = Path(__file__).resolve().parent / "cache" / "chunks"

SEED = 42  # determinismo para la muestra al azar


def load_extractions(source_pdf: str) -> list[dict]:
    """Lee todas las extracciones cacheadas para este TO."""
    base = source_pdf.replace(".pdf", "")
    results = []
    for p in sorted(EXTRACT_DIR.glob(f"{base}__chunk_*.json")):
        try:
            results.append(json.loads(p.read_text()))
        except Exception as e:
            print(f"[warn] couldn't load {p}: {e}", file=sys.stderr)
    return results


def load_failures(source_pdf: str) -> list[dict]:
    if not FAILURES_PATH.exists():
        return []
    out = []
    for line in FAILURES_PATH.read_text().splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
            if rec.get("source_pdf") == source_pdf:
                out.append(rec)
        except Exception:
            pass
    return out


def main():
    if len(sys.argv) < 2:
        print("Uso: python smoke_report.py <source_pdf.pdf>", file=sys.stderr)
        sys.exit(2)
    source_pdf = sys.argv[1]

    # Total de chunks esperados (desde el cache de chunks)
    chunks_file = CHUNKS_DIR / f"{source_pdf.replace('.pdf', '')}.json"
    total_chunks_expected = json.loads(chunks_file.read_text())["n_chunks"] if chunks_file.exists() else None

    extractions = load_extractions(source_pdf)
    failures = load_failures(source_pdf)

    ok_extractions = [e for e in extractions if e["status"] == "ok"]
    empty_extractions = [e for e in extractions if e["status"] == "empty"]

    # 1. Tipos crudos
    type_counter = Counter()
    label_lens = []  # en palabras
    all_entities = []  # para muestra
    pred_counter = Counter()
    relation_orphan_count = 0
    relation_total = 0

    for ex in ok_extractions:
        # set de nombres declarados en este chunk
        local_names = {e["name"] for e in ex["entities"]}
        for e in ex["entities"]:
            type_counter[e["type"]] += 1
            label_lens.append(len(e["name"].split()))
            all_entities.append({
                "name": e["name"],
                "type_raw": e["type"],
                "description": e.get("description", ""),
                "location_hint": e.get("location_hint", ""),
                "page_start": ex["page_start"],
                "page_end": ex["page_end"],
                "chunk_id": ex["chunk_id"],
                "source_pdf": ex["source_pdf"],
            })
        for r in ex["relations"]:
            relation_total += 1
            pred_counter[r["predicate"]] += 1
            if r["source"] not in local_names or r["target"] not in local_names:
                relation_orphan_count += 1

    # 2. Distribución de longitud de labels
    if label_lens:
        label_lens_sorted = sorted(label_lens)
        median = statistics.median(label_lens_sorted)
        p90 = label_lens_sorted[int(0.9 * (len(label_lens_sorted) - 1))]
        maxlen = max(label_lens_sorted)
        meanlen = statistics.mean(label_lens_sorted)
    else:
        median = p90 = maxlen = meanlen = 0

    # 3. Top 30 predicados
    top_predicates = pred_counter.most_common(30)
    total_unique_predicates = len(pred_counter)

    # 4. Muestra al azar de 20 entities
    random.seed(SEED)
    sample_n = min(20, len(all_entities))
    sample = random.sample(all_entities, sample_n) if all_entities else []

    # 5. Costo y métricas agregadas
    total_input = sum(ex.get("usage", {}).get("input_tokens", 0) for ex in extractions)
    total_output = sum(ex.get("usage", {}).get("output_tokens", 0) for ex in extractions)
    # Haiku 4.5: $1/MTok in, $5/MTok out
    cost = total_input * 1.0 / 1e6 + total_output * 5.0 / 1e6

    # --- IMPRESIÓN ---
    print(f"\n{'='*70}")
    print(f"SMOKE REPORT — {source_pdf}")
    print(f"{'='*70}\n")

    print(f"Chunks totales esperados: {total_chunks_expected}")
    print(f"Chunks procesados (cache): {len(extractions)}")
    print(f"  - status=ok:    {len(ok_extractions)}")
    print(f"  - status=empty: {len(empty_extractions)}  (señal del corpus, NO un fail)")
    print(f"Chunks failed (Pydantic/parse/API): {len(failures)}")
    if failures:
        fail_kinds = Counter(f.get("error_kind") for f in failures)
        for kind, n in fail_kinds.most_common():
            print(f"  - {kind}: {n}")
    print()

    print(f"Costo: ${cost:.3f}  (input={total_input} tok, output={total_output} tok)")
    print()

    print(f"--- Entities y Relations totales (status=ok) ---")
    print(f"Entities totales (con duplicados across chunks): {len(all_entities)}")
    print(f"Relations totales: {relation_total}")
    print(f"Relations con source/target NO en entities del mismo chunk (orfandad): {relation_orphan_count}")
    print()

    print(f"--- Distribución de longitud de label (en palabras) ---")
    print(f"  mediana: {median}")
    print(f"  p90:     {p90}")
    print(f"  máximo:  {maxlen}")
    print(f"  media:   {meanlen:.2f}")
    print()

    print(f"--- TIPOS CRUDOS (frecuencia completa, ordenado descendente) ---")
    print(f"Total únicos: {len(type_counter)}")
    print()
    for t, n in type_counter.most_common():
        print(f"  {n:4d}  {t}")
    print()

    print(f"--- TOP 30 PREDICADOS CRUDOS ---")
    print(f"Total únicos: {total_unique_predicates}")
    print()
    for p, n in top_predicates:
        print(f"  {n:4d}  {p}")
    print()

    print(f"--- MUESTRA AL AZAR DE {sample_n} ENTITIES (seed={SEED}) ---")
    for i, e in enumerate(sample, 1):
        prov = f"{e['source_pdf']} p.{e['page_start']}" + (f"-{e['page_end']}" if e["page_end"] != e["page_start"] else "")
        loc_hint = f" / {e['location_hint']}" if e['location_hint'] else ""
        desc = e["description"]
        if len(desc) > 180:
            desc = desc[:177] + "..."
        print(f"\n  [{i}] name='{e['name']}'")
        print(f"       type_raw='{e['type_raw']}'")
        print(f"       provenance='{prov}{loc_hint}'")
        print(f"       description='{desc}'")
    print()

    # Save the structured payload too, for downstream inspection
    payload = {
        "source_pdf": source_pdf,
        "total_chunks_expected": total_chunks_expected,
        "n_extractions": len(extractions),
        "n_ok": len(ok_extractions),
        "n_empty": len(empty_extractions),
        "n_failures": len(failures),
        "fail_kinds": dict(Counter(f.get("error_kind") for f in failures)),
        "cost_usd": round(cost, 4),
        "input_tokens": total_input,
        "output_tokens": total_output,
        "n_entities_with_dups": len(all_entities),
        "n_relations": relation_total,
        "n_relations_orphan": relation_orphan_count,
        "label_word_len": {
            "median": median,
            "p90": p90,
            "max": maxlen,
            "mean": round(meanlen, 2) if meanlen else 0,
        },
        "n_unique_types": len(type_counter),
        "n_unique_predicates": total_unique_predicates,
        "types_full": type_counter.most_common(),
        "predicates_top30": top_predicates,
        "sample_entities": sample,
    }
    out = Path(__file__).resolve().parent / "cache" / f"smoke_report_{source_pdf.replace('.pdf', '')}.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(f"[smoke_report] structured payload → {out}", flush=True)


if __name__ == "__main__":
    main()
