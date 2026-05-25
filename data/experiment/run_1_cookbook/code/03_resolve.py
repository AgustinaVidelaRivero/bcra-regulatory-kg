"""
03_resolve.py — Etapa 3 del cookbook: Entity Resolution / Deduplication.

Agrupa entidades por `type` y, para cada tipo, llama a Claude Sonnet con
RESOLVE_PROMPT (adaptado del cookbook §5) para clusterizar surface forms
en canonicals. Cada surface form aparece en exactamente UN cluster (el
cookbook lo exige para evitar silent data loss).

Modelo: claude-sonnet-4-6 (resolución/síntesis con razonamiento).
Salidas:
  cache/alias_to_canonical.json   → {alias: canonical}
  cache/canonical_info.json        → {canonical: {"type": ..., "aliases": [...], "descriptions": [...]}}
  cache/cost_resolution.json       → ledger

NOTA: scaffolding. La lógica de API (`call_sonnet_resolve`) es stub.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (
    CACHE_DIR,
    ENTITY_TYPES,
    CostLedger,
    ResolvedClusters,
    assert_under_budget,
    load_ledger,
    read_jsonl,
    require_api_key,
    save_ledger,
    write_json,
)

EXTRACTIONS_PATH = CACHE_DIR / "raw_extractions.jsonl"
ALIAS_MAP_PATH = CACHE_DIR / "alias_to_canonical.json"
CANONICAL_INFO_PATH = CACHE_DIR / "canonical_info.json"
STAGE = "resolution"

RESOLUTION_MODEL = "claude-sonnet-4-6"
MAX_TOKENS_OUT = 8000               # subido de 4096 — output truncaba en types densos

# Si un tipo tiene > N entidades, se "blocking" en lotes; cookbook §9 recomienda
# para 10K+ entidades. 100/batch es seguro ahora que el parsing es defensivo
# (call_sonnet_resolve cae a singletons fallback si Sonnet trunca).
MAX_ENTITIES_PER_CALL = 100


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

RESOLVE_PROMPT = """Estas son entidades del tipo {entity_type} extraídas de varios fragmentos del corpus regulatorio del BCRA. Algunas son surface forms distintos de la misma entidad real (ej. "entidad financiera", "entidades financieras", "EE.FF.", "las entidades").

<entidades>
{entity_list}
</entidades>

Agrupalas en clusters. Reglas duras:
1. Cada nombre de la lista debe aparecer en EXACTAMENTE UN cluster en `aliases`. No omitas ninguno: si una entidad es genuinamente distinta de las demás, dale su propio cluster de un solo elemento.
2. Usá las descripciones para evitar fusiones erróneas. Dos entidades con el mismo nombre pero distinta función (ej. "Comisión" como cargo vs "Comisión" como órgano colegiado) NO se fusionan.
3. El `canonical` debe ser la forma más completa y no-ambigua. Preferí formas con sigla expandida: "Mercado Único y Libre de Cambios (MULC)" sobre "MULC" sola. Singular sobre plural cuando refieran a la categoría ("entidad financiera" no "entidades financieras").
4. Si una sigla y su expansión son la misma entidad ("RPC" y "responsabilidad patrimonial computable"), fusionalas en un cluster con canonical expandido.
"""


def format_entity_list(entities: list[dict]) -> str:
    """Una entidad por línea, formato '- {name}: {description}'."""
    return "\n".join(f"- {e['name']}: {e['description']}" for e in entities)


# ---------------------------------------------------------------------------
# Llamada API — STUB
# ---------------------------------------------------------------------------

def call_sonnet_resolve(client, entity_type: str, entities: list[dict]) -> tuple[ResolvedClusters, dict]:
    """Cluster surface forms por tipo. Cookbook §5.

    Parsing defensivo: si Sonnet devuelve {} o falta `clusters`, devolvemos
    `clusters=[]` y `fallback_singletons()` cubrirá todos los nombres.
    """
    schema = ResolvedClusters.model_json_schema()
    msg = client.messages.create(
        model=RESOLUTION_MODEL,
        max_tokens=MAX_TOKENS_OUT,
        messages=[{
            "role": "user",
            "content": RESOLVE_PROMPT.format(
                entity_type=entity_type,
                entity_list=format_entity_list(entities),
            ),
        }],
        tools=[{
            "name": "emit_clusters",
            "description": "Emite los clusters de resolución de entidades.",
            "input_schema": schema,
        }],
        tool_choice={"type": "tool", "name": "emit_clusters"},
    )
    tool_block = None
    for b in msg.content:
        if getattr(b, "type", None) == "tool_use":
            tool_block = b
            break

    usage = {
        "input_tokens": msg.usage.input_tokens,
        "output_tokens": msg.usage.output_tokens,
        "model": RESOLUTION_MODEL,
    }

    if tool_block is None:
        print(f"[03_resolve] WARN {entity_type}: Sonnet no emitió tool_use "
              f"(stop_reason={msg.stop_reason}). Usando singletons fallback.")
        return ResolvedClusters(clusters=[]), usage

    raw = tool_block.input if isinstance(tool_block.input, dict) else {}
    if not raw or "clusters" not in raw or not isinstance(raw["clusters"], list):
        print(f"[03_resolve] WARN {entity_type}: tool_use con payload vacío/inválido "
              f"({list(raw.keys()) if isinstance(raw, dict) else type(raw).__name__}). "
              "Usando singletons fallback.")
        return ResolvedClusters(clusters=[]), usage

    try:
        clusters = ResolvedClusters.model_validate(raw)
    except Exception as e:
        print(f"[03_resolve] WARN {entity_type}: validation falló ({type(e).__name__}). "
              "Usando singletons fallback.")
        clusters = ResolvedClusters(clusters=[])
    return clusters, usage


# ---------------------------------------------------------------------------
# Lógica de agregación y fallback
# ---------------------------------------------------------------------------

def collect_entities_by_type(extractions: list[dict]) -> dict[str, list[dict]]:
    """
    Junta entidades del JSONL de extracciones por tipo, deduplicando por (name, description).
    Mantiene una descripción "representativa" por surface name (la primera vista).
    """
    by_type: dict[str, list[dict]] = defaultdict(list)
    seen: dict[str, set[str]] = defaultdict(set)
    for row in extractions:
        for e in row["entities"]:
            etype = e["type"]
            name = e["name"].strip()
            if not name:
                continue
            if name in seen[etype]:
                continue
            seen[etype].add(name)
            by_type[etype].append({
                "name": name,
                "description": e.get("description", ""),
            })
    return by_type


def fallback_singletons(input_entities: list[dict], clusters: ResolvedClusters) -> list[dict]:
    """
    Cookbook §5 "silent name loss": si la API se olvidó algún nombre,
    creamos un cluster singleton para él (canonical = name).
    """
    seen_aliases: set[str] = set()
    for c in clusters.clusters:
        for a in c.aliases:
            seen_aliases.add(a)
    missing = [e for e in input_entities if e["name"] not in seen_aliases]
    return [{"canonical": m["name"], "aliases": [m["name"]]} for m in missing]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Etapa 3: entity resolution con Sonnet.")
    parser.add_argument("--force", action="store_true", help="Re-corre la resolución aunque ya haya outputs.")
    args = parser.parse_args(argv)

    if ALIAS_MAP_PATH.exists() and not args.force:
        print(f"[03_resolve] {ALIAS_MAP_PATH} ya existe. Usá --force para re-resolver.")
        return 0

    if not EXTRACTIONS_PATH.exists():
        print(f"[03_resolve] Falta {EXTRACTIONS_PATH}. Corré 02_extract.py primero.")
        return 1

    extractions = read_jsonl(EXTRACTIONS_PATH)
    by_type = collect_entities_by_type(extractions)

    print("[03_resolve] Entidades únicas por tipo:")
    for etype in ENTITY_TYPES:
        print(f"  - {etype}: {len(by_type.get(etype, []))}")

    assert_under_budget()

    require_api_key()
    import anthropic
    client = anthropic.Anthropic()

    ledger = load_ledger(STAGE)
    alias_to_canonical: dict[str, str] = {}
    canonical_info: dict[str, dict] = {}

    for etype in ENTITY_TYPES:
        ents = by_type.get(etype, [])
        if not ents:
            continue
        print(f"[03_resolve] Resolviendo {etype} ({len(ents)} entidades)…")

        # Si superamos MAX_ENTITIES_PER_CALL, partir en bloques.
        # Para este corpus probablemente nunca, pero el código lo soporta.
        all_clusters_for_type = []
        for i in range(0, len(ents), MAX_ENTITIES_PER_CALL):
            block = ents[i : i + MAX_ENTITIES_PER_CALL]
            clusters, usage = call_sonnet_resolve(client, etype, block)
            ledger.record(usage["model"], usage["input_tokens"], usage["output_tokens"])
            assert_under_budget()
            all_clusters_for_type.extend([c.model_dump() for c in clusters.clusters])

            # Fallback singletons para nombres olvidados en este bloque
            from common import ResolvedClusters as _RC  # noqa
            recovered = fallback_singletons(block, clusters)
            all_clusters_for_type.extend(recovered)

        # Poblar maps
        desc_by_name = {e["name"]: e["description"] for e in ents}
        for c in all_clusters_for_type:
            canon = c["canonical"]
            aliases = c["aliases"]
            canonical_info.setdefault(canon, {
                "type": etype,
                "aliases": [],
                "descriptions": [],
            })
            for a in aliases:
                if a not in canonical_info[canon]["aliases"]:
                    canonical_info[canon]["aliases"].append(a)
                if a in desc_by_name and desc_by_name[a] not in canonical_info[canon]["descriptions"]:
                    canonical_info[canon]["descriptions"].append(desc_by_name[a])
                alias_to_canonical[a] = canon

    write_json(ALIAS_MAP_PATH, alias_to_canonical)
    write_json(CANONICAL_INFO_PATH, canonical_info)
    save_ledger(STAGE, ledger)

    print(f"[03_resolve] OK · canónicos: {len(canonical_info)} · aliases: {len(alias_to_canonical)}")
    print(f"[03_resolve] USD etapa: {ledger.total_usd:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
