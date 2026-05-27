"""
Pasos 1-3 del post-procesado (acordados con la autora):

1. Normalización superficial de predicados (lowercase + strip acentos + snake_case).
   Preserva `predicate_raw`. NO fusiona predicados semánticamente — eso es por
   diseño de la estrategia schema-light pura (queremos ver la verbosidad).

2. Dedup de entidades por slug cross-chunk:
   - Slug = slug_label(name). Sin heurística de plurales.
   - Si dos chunks producen entidades con el mismo slug, se fusionan en un nodo:
       * id = slug
       * label = el name más frecuente (desempate: el más corto, luego alfabético)
       * type_raw = lista única de todos los type observados (preserva inconsistencia)
       * description = la description del primer chunk con score más alto
         (donde score = longitud no trivial); las descriptions se preservan en
         _descriptions_observed.
       * provenance = LISTA de provenances (TO + page_range + location_hint)

3. Backstop estructural sobre type_raw normalizado:
   - Dropear entidad si TODOS sus type_raw matchean el backstop.
     (Si una entidad tuvo múltiples tipos crudos y al menos uno NO matchea el
     backstop, NO se dropea — esa entidad existe legítimamente bajo otro tipo).
   - Las relations cuyo source o target fue dropeado se descartan también.
   - Reportar conteos.

Output: code/cache/staging.json con la estructura del KG previa al clustering de tipos.
"""

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from slug import slug_label, slug_predicate, slug_type, matches_backstop

EXTRACT_DIR = Path(__file__).resolve().parent / "cache" / "extract"
STAGING_PATH = Path(__file__).resolve().parent / "cache" / "staging.json"
DEDUP_REPORT_PATH = Path(__file__).resolve().parent / "cache" / "dedup_report.json"
BACKSTOP_REPORT_PATH = Path(__file__).resolve().parent / "cache" / "backstop_report.json"

TOS = [
    "TO_proteccion_usuarios_servicios_financieros_actual",
    "TO_clasificacion_deudores_actual",
    "TO_regimen_informativo_contable_mensual_actual",
    "TO_exterior_cambios_actual",
    "TO_capitales_minimos_actual",
]


def load_all_extractions() -> list[dict]:
    """Carga TODAS las extracciones cacheadas de los 5 TOs (status=ok)."""
    out = []
    for to in TOS:
        for p in sorted(EXTRACT_DIR.glob(f"{to}__chunk_*.json")):
            d = json.loads(p.read_text())
            if d["status"] == "ok":
                out.append(d)
    return out


def make_provenance(ex: dict, location_hint: str = "") -> dict:
    """Provenance de un nodo o edge derivada de un chunk."""
    pgs = f"p.{ex['page_start']}" if ex["page_start"] == ex["page_end"] else f"p.{ex['page_start']}-{ex['page_end']}"
    loc = pgs
    if location_hint:
        loc = f"{pgs} / {location_hint}"
    return {
        "source_doc": f"{ex['source_pdf']}.pdf" if not ex["source_pdf"].endswith(".pdf") else ex["source_pdf"],
        "location": loc,
        "chunk_id": ex["chunk_id"],
    }


def dedup_entities(extractions: list[dict]) -> tuple[dict, dict]:
    """
    Devuelve:
    - nodes_staging: dict[slug -> nodo agregado]
    - dedup_stats: dict para reporting (top-30 slugs más mergeados, type_raw diversity)
    """
    grouped: dict[str, list[tuple[dict, dict]]] = defaultdict(list)
    # cada entry: (entity_raw, extraction_origen)

    for ex in extractions:
        for e in ex["entities"]:
            slug = slug_label(e["name"])
            if not slug:
                continue  # nombres vacíos
            grouped[slug].append((e, ex))

    nodes: dict[str, dict] = {}
    merge_counts: Counter = Counter()
    typeraw_per_slug: dict[str, list[str]] = {}
    namevariants_per_slug: dict[str, list[str]] = {}

    for slug, items in grouped.items():
        merge_counts[slug] = len(items)
        # Decidir label canónico: name más frecuente, desempate por longitud asc, luego alfabético
        name_freq: Counter = Counter()
        for e, _ in items:
            name_freq[e["name"].strip()] += 1
        best_name = sorted(name_freq.items(), key=lambda kv: (-kv[1], len(kv[0]), kv[0]))[0][0]
        namevariants_per_slug[slug] = sorted(name_freq.keys())

        # type_raw: lista única preservando orden de aparición
        seen_types: list[str] = []
        for e, _ in items:
            t = e["type"].strip()
            if t and t not in seen_types:
                seen_types.append(t)
        typeraw_per_slug[slug] = seen_types

        # description: la más informativa (más larga, hasta cierto límite)
        descriptions = [e.get("description", "").strip() for e, _ in items if e.get("description", "").strip()]
        if descriptions:
            best_desc = max(descriptions, key=len)
        else:
            best_desc = ""

        # provenance: lista de todas las observaciones
        provs: list[dict] = []
        for e, ex in items:
            provs.append(make_provenance(ex, e.get("location_hint", "")))

        node = {
            "id": slug,
            "label": best_name,
            "type_raw": seen_types,            # lista (regla del usuario)
            "type_normalized": [slug_type(t) for t in seen_types],
            # type canónico: se agrega después del clustering
            "properties": {
                "description": best_desc,
                "name_variants": sorted(name_freq.keys()) if len(name_freq) > 1 else [],
                "n_observations": len(items),
            },
            "provenance": provs,  # lista; en kg.json final se aplana o se elige una primary
        }
        nodes[slug] = node

    dedup_stats = {
        "total_entities_observed": sum(merge_counts.values()),
        "total_unique_slugs": len(nodes),
        "merge_counts": merge_counts,
        "typeraw_per_slug": typeraw_per_slug,
        "namevariants_per_slug": namevariants_per_slug,
    }
    return nodes, dedup_stats


def apply_backstop(nodes: dict[str, dict]) -> tuple[set[str], dict]:
    """
    Devuelve (slugs_dropped, backstop_stats).
    Una entidad se dropea si TODOS sus type_normalized matchean el backstop.
    Si tiene al menos un tipo crudo que NO matchea, se preserva.
    """
    dropped_slugs: set[str] = set()
    dropped_details = []
    for slug, node in nodes.items():
        types_norm = node["type_normalized"]
        if not types_norm:
            continue
        if all(matches_backstop(t) for t in types_norm):
            dropped_slugs.add(slug)
            dropped_details.append({
                "id": slug,
                "label": node["label"],
                "type_raw": node["type_raw"],
                "type_normalized": types_norm,
            })

    return dropped_slugs, {
        "n_dropped": len(dropped_slugs),
        "details": dropped_details,
    }


def build_relations(extractions: list[dict], nodes: dict[str, dict], dropped_slugs: set[str]) -> tuple[list[dict], dict]:
    """
    Construye los edges:
    - Resolve source/target a slug via slug_label(name).
    - Drop relations cuyo source o target no resuelva a un nodo existente (incluye dropped_slugs).
    - Normalizar predicate superficialmente, preservar predicate_raw.
    - Provenance derivada del chunk.
    """
    edges = []
    n_total = 0
    n_dropped_orphan = 0
    n_dropped_backstop = 0  # source o target borrado por backstop

    valid_slugs = set(nodes.keys()) - dropped_slugs

    for ex in extractions:
        for r in ex["relations"]:
            n_total += 1
            src_slug = slug_label(r["source"])
            tgt_slug = slug_label(r["target"])
            if src_slug in dropped_slugs or tgt_slug in dropped_slugs:
                n_dropped_backstop += 1
                continue
            if src_slug not in valid_slugs or tgt_slug not in valid_slugs:
                n_dropped_orphan += 1
                continue
            edges.append({
                "source": src_slug,
                "target": tgt_slug,
                "predicate": slug_predicate(r["predicate"]),
                "predicate_raw": r["predicate"].strip(),
                "provenance": make_provenance(ex, r.get("location_hint", "")),
            })

    return edges, {
        "n_total_observed": n_total,
        "n_kept": len(edges),
        "n_dropped_orphan": n_dropped_orphan,
        "n_dropped_by_backstop_endpoint": n_dropped_backstop,
    }


def main():
    print("=" * 70)
    print("PREPROCESS — pasos 1-3 (predicates norm, dedup, backstop)")
    print("=" * 70)
    extractions = load_all_extractions()
    print(f"[load] {len(extractions)} extractions (status=ok) cargadas")

    # Paso 2 — dedup
    nodes, dedup_stats = dedup_entities(extractions)
    print(f"[dedup] {dedup_stats['total_entities_observed']} entities crudas → {len(nodes)} slugs únicos")

    # Paso 3 — backstop
    dropped_slugs, backstop_stats = apply_backstop(nodes)
    for slug in dropped_slugs:
        nodes.pop(slug)
    print(f"[backstop] dropped {len(dropped_slugs)} entities por type_raw matching")

    # Paso 1 — predicates + build edges + drop orphan/backstop endpoints
    edges, edge_stats = build_relations(extractions, {**nodes, **{s: {} for s in dropped_slugs}}, dropped_slugs)
    print(f"[edges] {edge_stats['n_total_observed']} relations crudas → {edge_stats['n_kept']} kept "
          f"(dropped {edge_stats['n_dropped_orphan']} orphan + {edge_stats['n_dropped_by_backstop_endpoint']} backstop endpoint)")

    # Persistir staging
    staging = {
        "nodes": list(nodes.values()),
        "edges": edges,
        "stats": {
            "extractions": len(extractions),
            "entities_observed": dedup_stats["total_entities_observed"],
            "nodes_unique_slugs_pre_backstop": dedup_stats["total_unique_slugs"],
            "nodes_dropped_by_backstop": len(dropped_slugs),
            "nodes_final": len(nodes),
            "edges_observed": edge_stats["n_total_observed"],
            "edges_dropped_orphan": edge_stats["n_dropped_orphan"],
            "edges_dropped_by_backstop_endpoint": edge_stats["n_dropped_by_backstop_endpoint"],
            "edges_final": edge_stats["n_kept"],
        },
    }
    STAGING_PATH.write_text(json.dumps(staging, ensure_ascii=False, indent=2))
    print(f"[staging] → {STAGING_PATH}  ({len(nodes)} nodes, {len(edges)} edges)")

    # Reporte de dedup: top 30 slugs más mergeados
    print()
    print("--- DEDUP REPORT: top 30 slugs más mergeados (cross-chunk) ---")
    print(f"{'slug':<45} {'count':>6} {'name_variants':>14} {'type_raw_list':<60}")
    top = dedup_stats["merge_counts"].most_common(30)
    dedup_report = []
    for slug, n in top:
        types = dedup_stats["typeraw_per_slug"].get(slug, [])
        names = dedup_stats["namevariants_per_slug"].get(slug, [])
        types_str = " | ".join(types[:5])
        if len(types) > 5:
            types_str += f" | ... ({len(types)} total)"
        names_str = f"{len(names)}"
        print(f"  {slug[:42]:<45} {n:>6} {names_str:>14} {types_str:<60}")
        dedup_report.append({
            "slug": slug,
            "merge_count": n,
            "name_variants": names,
            "type_raw_distinct": types,
            "type_raw_count": len(types),
        })

    DEDUP_REPORT_PATH.write_text(json.dumps(dedup_report, ensure_ascii=False, indent=2))

    # Reporte de backstop
    print()
    print(f"--- BACKSTOP REPORT ---")
    print(f"Entities (nodes únicos) dropeados: {len(dropped_slugs)}")
    print(f"Relations dropeadas por endpoint en backstop: {edge_stats['n_dropped_by_backstop_endpoint']}")
    if dropped_slugs:
        print()
        print(f"--- Detalle de entities dropeados ---")
        for d in backstop_stats["details"]:
            print(f"  [{d['id']}] label='{d['label']}'  type_raw={d['type_raw']}")
    BACKSTOP_REPORT_PATH.write_text(json.dumps(backstop_stats, ensure_ascii=False, indent=2))

    print()
    print(f"--- STAGING SUMMARY ---")
    print(f"  nodes        : {len(nodes)}")
    print(f"  edges        : {len(edges)}")
    print(f"  edge density : {len(edges)/len(nodes):.2f}" if nodes else "  edge density: -")


if __name__ == "__main__":
    main()
