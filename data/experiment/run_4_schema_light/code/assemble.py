"""
Ensamblaje final del KG en el formato del protocolo.

Decisiones aplicadas (acordadas con la autora):
- NO clustering automático (opción E). MiniLM produjo fusiones falsas masivas.
- Schema-light puro mantiene su pureza: solo normalización superficial.
- type canónico del nodo = type_raw más frecuente para esa entidad
  (counts dentro de las observaciones del nodo), normalizado superficialmente.
- Backstop estructural sobre type_raw (ya aplicado en preprocess.py, 0 drops).
- Slug dedup sin heurística de plurales.
- provenance OBLIGATORIO en cada nodo y cada edge.

Estructura del kg.json (formato del protocolo, sección b):
{
  "nodes": [
    {
      "id": "<slug>",
      "type": "<tipo canónico normalizado>",
      "label": "<label legible>",
      "properties": {
        "description": "<...>",
        "version": "vigente",   ← regla 2 del protocolo
        "type_raw": ["<lista de todos los type_raw observados>"],
        "name_variants": ["<variantes de name observadas>"]
      },
      "provenance": {  ← una primary provenance (TO + page_range + location_hint del primer chunk)
        "source_doc": "<pdf>",
        "location": "<p.X-Y / Punto Z>"
      }
    }
  ],
  "edges": [
    {
      "source": "<slug>",
      "target": "<slug>",
      "relation": "<predicate normalizado>",
      "provenance": {...},
      "properties": {
        "predicate_raw": "<predicate crudo>"
      }
    }
  ]
}
"""

import json
from collections import Counter
from pathlib import Path

from slug import slug_type

STAGING_PATH = Path(__file__).resolve().parent / "cache" / "staging.json"
KG_PATH = Path(__file__).resolve().parents[1] / "kg.json"  # run_4_schema_light/kg.json
EXTRACT_DIR = Path(__file__).resolve().parent / "cache" / "extract"


def reconstruct_type_counts(node: dict) -> Counter:
    """
    Para elegir el type canónico necesitamos saber la frecuencia ponderada de cada type_raw
    DENTRO de este nodo. La staging tiene type_raw como lista única sin freq.
    Reconstruimos contando del cache de extract.
    """
    # No tenemos esa info en staging directamente. Recorremos cache para este slug.
    # Pero eso es ineficiente. Alternative: agregar conteos en preprocess.
    # Hack temporal: usamos el primer type_raw como canónico (preservando orden de observación).
    raise NotImplementedError


def main():
    staging = json.loads(STAGING_PATH.read_text())
    nodes_in = staging["nodes"]
    edges_in = staging["edges"]

    # --- Reconstruir conteos de type_raw POR NODO ---
    # Para asignar el type canónico, necesitamos saber qué type_raw es el más frecuente
    # para cada slug. La staging no lo trae; lo recomputamos sobre el cache.
    print("[assemble] reconstruyendo conteos de type_raw por nodo desde el cache ...")
    from slug import slug_label
    per_node_typecounts: dict[str, Counter] = {}
    for p in sorted(EXTRACT_DIR.glob("TO_*chunk_*.json")):
        d = json.loads(p.read_text())
        if d["status"] != "ok":
            continue
        for e in d["entities"]:
            slug = slug_label(e["name"])
            if not slug:
                continue
            per_node_typecounts.setdefault(slug, Counter())[e["type"].strip()] += 1

    # --- Construir nodes del kg final ---
    nodes_out = []
    for node in nodes_in:
        slug = node["id"]
        type_counts = per_node_typecounts.get(slug, Counter())
        # type canónico: el más frecuente. Desempate: el más corto, luego alfabético.
        if type_counts:
            paired = sorted(type_counts.items(), key=lambda kv: (-kv[1], len(kv[0]), kv[0]))
            canonical_type_raw = paired[0][0]
            type_canonical = slug_type(canonical_type_raw)
        else:
            type_canonical = ""
            canonical_type_raw = ""

        # primary provenance: la del primer chunk en que aparece
        provs = node["provenance"]
        primary_prov = {
            "source_doc": provs[0]["source_doc"] if provs else "",
            "location": provs[0]["location"] if provs else "",
        }
        # provenance.observations: cuántas observaciones cross-chunk; lista de todas
        all_provs = provs

        node_out = {
            "id": slug,
            "type": type_canonical,
            "label": node["label"],
            "properties": {
                "description": node["properties"].get("description", ""),
                "version": "vigente",   # regla 2 del protocolo
                "type_raw": node["type_raw"],           # lista (sin duplicados de string)
                "type_raw_counts": dict(type_counts),    # freq dentro del nodo
                "name_variants": node["properties"].get("name_variants", []),
                "n_observations": node["properties"].get("n_observations", 1),
                "all_provenances": all_provs,
            },
            "provenance": primary_prov,
        }
        nodes_out.append(node_out)

    # --- Construir edges del kg final ---
    edges_out = []
    for e in edges_in:
        edges_out.append({
            "source": e["source"],
            "target": e["target"],
            "relation": e["predicate"],
            "provenance": {
                "source_doc": e["provenance"]["source_doc"],
                "location": e["provenance"]["location"],
            },
            "properties": {
                "predicate_raw": e["predicate_raw"],
            },
        })

    # --- Escribir kg.json ---
    kg = {"nodes": nodes_out, "edges": edges_out}
    KG_PATH.write_text(json.dumps(kg, ensure_ascii=False, indent=2))
    print(f"[assemble] kg.json → {KG_PATH}")
    print(f"  nodes: {len(nodes_out)}")
    print(f"  edges: {len(edges_out)}")
    print(f"  density (edges/nodes): {len(edges_out)/len(nodes_out):.3f}" if nodes_out else "")

    # Stats útiles
    type_dist = Counter(n["type"] for n in nodes_out)
    print(f"\n  unique canonical types: {len(type_dist)}")
    print(f"  top 10 canonical types:")
    for t, n in type_dist.most_common(10):
        print(f"    {n:>4}  {t}")
    rel_dist = Counter(e["relation"] for e in edges_out)
    print(f"\n  unique predicates (normalized): {len(rel_dist)}")
    print(f"  top 10 predicates:")
    for p, n in rel_dist.most_common(10):
        print(f"    {n:>4}  {p}")


if __name__ == "__main__":
    main()
