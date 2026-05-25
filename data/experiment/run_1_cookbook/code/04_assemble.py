"""
04_assemble.py — Etapa 4 del cookbook: Graph Assembly.

Construye un nx.MultiDiGraph con las extracciones crudas pasadas por el
alias_to_canonical map; deduplica edges idénticos (mismo source-predicate-target);
serializa al formato JSON del protocolo (§b) en data/experiment/run_1_cookbook/kg.json.

NO usa la API. Sin costo.

Output: ../kg.json (sin hub summaries; 05_hub_summarize.py los agrega)
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (
    CACHE_DIR,
    KG_JSON_PATH,
    is_documental_hierarchy,
    make_node_id,
    read_json,
    read_jsonl,
    write_json,
)

ALIAS_MAP_PATH = CACHE_DIR / "alias_to_canonical.json"
CANONICAL_INFO_PATH = CACHE_DIR / "canonical_info.json"
EXTRACTIONS_PATH = CACHE_DIR / "raw_extractions.jsonl"


# ---------------------------------------------------------------------------
# Ensamblaje
# ---------------------------------------------------------------------------

def build_graph(
    extractions: list[dict],
    alias_to_canonical: dict[str, str],
    canonical_info: dict[str, dict],
) -> dict:
    """
    Devuelve el dict en formato del protocolo §b: {"nodes": [...], "edges": [...]}.

    Para cada nodo (canonical):
      - id: make_node_id(canonical, type)
      - type: del canonical_info
      - label: canonical
      - properties.version: versión del TO de la PRIMERA ocurrencia del canonical
      - properties.description: descripción más larga vista (proxy de "más informativa")
      - properties.aliases: lista de surface forms
      - properties.source_to: TO de la primera ocurrencia
      - properties.mention_count: nº de chunks que mencionan al canonical
      - provenance: source_doc + location de la primera ocurrencia
      - properties.other_locations: opcional, las locations siguientes

    Para cada edge (source, predicate, target) tras pasar por alias_map:
      - dedup por (source, predicate, target) — un solo edge
      - provenance: la primera ocurrencia
      - properties.other_locations: opcional
    """
    # ----------- NODOS -----------
    canonical_first_occurrence: dict[str, dict] = {}     # canonical -> {source_doc, location, version, to}
    canonical_descriptions: dict[str, list[str]] = defaultdict(list)
    canonical_mention_count: Counter[str] = Counter()
    canonical_locations: dict[str, list[dict]] = defaultdict(list)

    for row in extractions:
        for e in row["entities"]:
            name = e["name"].strip()
            canon = alias_to_canonical.get(name)
            if canon is None:
                # No debería pasar (fallback_singletons cubre esto), pero si pasa: dropeamos con warning.
                print(f"[04_assemble] WARN: alias sin canonical map: {name!r} (type={e.get('type')})")
                continue
            if is_documental_hierarchy(name) or is_documental_hierarchy(canon):
                # Doble check de la regla §c.1 — si el modelo se filtró, lo dropeamos acá.
                print(f"[04_assemble] DROP (jerarquía documental): {canon!r}")
                continue
            canonical_mention_count[canon] += 1
            if e.get("description"):
                canonical_descriptions[canon].append(e["description"])
            loc = {
                "source_doc": row["source_doc"],
                "location": row["location"],
                "to": row["to"],
                "version": row["version"],
            }
            canonical_locations[canon].append(loc)
            canonical_first_occurrence.setdefault(canon, loc)

    # Detectar colisiones de slug (dos canónicos distintos generando el mismo id).
    # Pasa cuando dos formas canónicas difieren sólo en acentos/casing/puntuación
    # (ej. "Auditoría interna" vs "auditoria interna"). Fusionamos en el primer canónico
    # registrado para ese slug y redirigimos el alias map al canónico ganador.
    slug_to_canon: dict[str, str] = {}
    canon_redirect: dict[str, str] = {}   # canon perdedor → canon ganador
    for canon, info in canonical_info.items():
        slug = make_node_id(canon, info["type"])
        if slug in slug_to_canon:
            winner = slug_to_canon[slug]
            canon_redirect[canon] = winner
            # Fusionar aliases en el ganador
            for a in info.get("aliases", []):
                if a not in canonical_info[winner]["aliases"]:
                    canonical_info[winner]["aliases"].append(a)
            print(f"[04_assemble] SLUG COLLISION: {canon!r} → fusionado en {winner!r} (slug={slug})")
        else:
            slug_to_canon[slug] = canon

    # Aplicar redirects al alias map y a las estructuras de menciones.
    if canon_redirect:
        for loser, winner in canon_redirect.items():
            # Mover menciones/desc/locations del loser al winner
            canonical_mention_count[winner] += canonical_mention_count.pop(loser, 0)
            canonical_descriptions[winner].extend(canonical_descriptions.pop(loser, []))
            canonical_locations[winner].extend(canonical_locations.pop(loser, []))
            if winner not in canonical_first_occurrence and loser in canonical_first_occurrence:
                canonical_first_occurrence[winner] = canonical_first_occurrence[loser]
            canonical_first_occurrence.pop(loser, None)
        # Reescribir alias_to_canonical para que los aliases del loser apunten al winner
        for alias, canon in list(alias_to_canonical.items()):
            if canon in canon_redirect:
                alias_to_canonical[alias] = canon_redirect[canon]

    nodes: list[dict] = []
    canonical_to_id: dict[str, str] = {}
    for canon, info in canonical_info.items():
        if canon in canon_redirect:
            continue                          # ya fusionado en otro canónico
        if canon not in canonical_first_occurrence:
            # Canonical sin menciones (no debería pasar — viene de las propias extracciones).
            continue
        etype = info["type"]
        node_id = make_node_id(canon, etype)
        canonical_to_id[canon] = node_id
        first = canonical_first_occurrence[canon]
        descs = canonical_descriptions[canon] or info.get("descriptions", [])
        # Description "representativa" = la más larga (proxy razonable para informatividad).
        description = max(descs, key=len, default="")
        other_locs = canonical_locations[canon][1:]  # excluyo la primera (ya está en provenance)
        nodes.append({
            "id": node_id,
            "type": etype,
            "label": canon,
            "properties": {
                "version": first["version"],
                "description": description,
                "aliases": info["aliases"],
                "source_to": first["to"],
                "mention_count": canonical_mention_count[canon],
                **({"other_locations": [
                    {"source_doc": l["source_doc"], "location": l["location"]} for l in other_locs
                ]} if other_locs else {}),
            },
            "provenance": {
                "source_doc": first["source_doc"],
                "location": first["location"],
            },
        })

    # ----------- EDGES -----------
    # Clave de dedup: (source_id, predicate, target_id).
    edges_dedup: dict[tuple[str, str, str], dict] = {}
    edges_other_locs: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    dropped_edges = {"missing_node": 0, "self_loop": 0, "alias_unmapped": 0}

    for row in extractions:
        for r in row["relations"]:
            s_canon = alias_to_canonical.get(r["source"].strip())
            t_canon = alias_to_canonical.get(r["target"].strip())
            if s_canon is None or t_canon is None:
                dropped_edges["alias_unmapped"] += 1
                continue
            s_id = canonical_to_id.get(s_canon)
            t_id = canonical_to_id.get(t_canon)
            if s_id is None or t_id is None:
                dropped_edges["missing_node"] += 1
                continue
            if s_id == t_id:
                dropped_edges["self_loop"] += 1
                continue
            predicate = r["predicate"].strip()
            if not predicate:
                continue
            key = (s_id, predicate, t_id)
            loc = {"source_doc": row["source_doc"], "location": row["location"]}
            if key not in edges_dedup:
                edges_dedup[key] = {
                    "source": s_id,
                    "target": t_id,
                    "relation": predicate,
                    "provenance": loc,
                }
            else:
                edges_other_locs[key].append(loc)

    edges: list[dict] = []
    for key, e in edges_dedup.items():
        others = edges_other_locs.get(key, [])
        if others:
            e["properties"] = {"other_locations": others, "weight": 1 + len(others)}
        else:
            e["properties"] = {"weight": 1}
        edges.append(e)

    kg = {
        "nodes": nodes,
        "edges": edges,
        "_meta": {
            "run_id": "Run 1 — Cookbook de Anthropic",
            "schema_version": "1.0",
            "dropped_edges": dropped_edges,
        },
    }
    return kg


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Etapa 4: ensamblar el KG en formato del protocolo.")
    args = parser.parse_args(argv)

    for fp in (EXTRACTIONS_PATH, ALIAS_MAP_PATH, CANONICAL_INFO_PATH):
        if not fp.exists():
            print(f"[04_assemble] Falta {fp}. Corré las etapas anteriores.")
            return 1

    extractions = read_jsonl(EXTRACTIONS_PATH)
    alias_to_canonical = read_json(ALIAS_MAP_PATH)
    canonical_info = read_json(CANONICAL_INFO_PATH)

    kg = build_graph(extractions, alias_to_canonical, canonical_info)
    write_json(KG_JSON_PATH, kg)

    print(f"[04_assemble] OK · nodes={len(kg['nodes'])} edges={len(kg['edges'])} → {KG_JSON_PATH}")
    print(f"[04_assemble] Edges dropeados: {kg['_meta']['dropped_edges']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
