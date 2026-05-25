"""
05_hub_summarize.py — Etapa 5 del cookbook: Hub Summarization.

Para los N nodos con mayor degree (in+out) del KG, llama a Claude Sonnet
con SUMMARIZE_PROMPT del cookbook (adaptado) para generar un perfil
enriquecido (summary 2-3 párrafos + key_facts + time_range) y lo agrega
a `properties.summary` / `properties.key_facts` / `properties.time_range`
de los nodos hub en kg.json.

Modelo: claude-sonnet-4-6.
Budget guard: aborta si el costo acumulado pasa BUDGET_USD_ABORT.

NOTA: scaffolding. `call_sonnet_summarize` es stub.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (
    CACHE_DIR,
    KG_JSON_PATH,
    CostLedger,
    EntityProfile,
    assert_under_budget,
    load_ledger,
    read_json,
    read_jsonl,
    require_api_key,
    save_ledger,
    write_json,
)

EXTRACTIONS_PATH = CACHE_DIR / "raw_extractions.jsonl"
STAGE = "summarization"

SUMMARIZATION_MODEL = "claude-sonnet-4-6"
MAX_TOKENS_OUT = 1500

# Cuántos hubs resumir.
# Cookbook recomienda los top-degree; balanceamos contra presupuesto.
# Con 5-10 hubs y ~10K tokens/call → ~$0.30. Sobra.
TOP_K_HUBS_DEFAULT = 15
HUB_MIN_DEGREE = 3   # umbral mínimo para que un nodo amerite resumen


# ---------------------------------------------------------------------------
# Prompt — adaptado de cookbook §6
# ---------------------------------------------------------------------------

SUMMARIZE_PROMPT = """Generá un perfil de Knowledge Graph para esta entidad regulatoria del corpus del BCRA.

Entidad: {name} (tipo: {etype})

Fragmentos del corpus que mencionan esta entidad:
{excerpts}

Relaciones conocidas en el grafo (origen --[predicado]--> destino):
{relations}

Escribí una síntesis factual de 2-3 párrafos a partir de los fragmentos, resolviendo cualquier contradicción a favor de la afirmación más específica.

Devolvé también 3-5 hechos atómicos (key_facts), cada uno trazable a los fragmentos provistos.

Para el time_range:
- `start`: si la norma menciona fecha de vigencia explícita, usá YYYY o YYYY-MM. Si no, "unknown".
- `end`: para la versión vigente, "ongoing".

No inventes hechos no soportados por los fragmentos.
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def node_degree(kg: dict) -> dict[str, int]:
    """Degree total (in + out) por id de nodo."""
    deg: dict[str, int] = defaultdict(int)
    for e in kg["edges"]:
        deg[e["source"]] += 1
        deg[e["target"]] += 1
    return deg


def select_hubs(kg: dict, top_k: int) -> list[dict]:
    """Devuelve los nodos top-degree (≥ HUB_MIN_DEGREE), hasta top_k."""
    deg = node_degree(kg)
    ranked = sorted(kg["nodes"], key=lambda n: -deg.get(n["id"], 0))
    hubs = [n for n in ranked if deg.get(n["id"], 0) >= HUB_MIN_DEGREE]
    return hubs[:top_k]


def collect_excerpts_for_node(node: dict, extractions: list[dict]) -> str:
    """Recolecta los textos de chunks que mencionan los aliases del nodo."""
    aliases = set(node["properties"].get("aliases", [node["label"]]))
    matched_chunk_ids: list[str] = []
    for row in extractions:
        names_in_row = {e["name"].strip() for e in row["entities"]}
        if names_in_row & aliases:
            matched_chunk_ids.append(row["chunk_id"])
    if not matched_chunk_ids:
        return ""

    # Cargar chunks.jsonl para recuperar el texto
    from common import CACHE_DIR as _CD
    chunks_path = _CD / "chunks.jsonl"
    if not chunks_path.exists():
        return ""
    chunks_by_id = {c["chunk_id"]: c for c in read_jsonl(chunks_path)}

    pieces: list[str] = []
    for cid in matched_chunk_ids[:8]:   # cap para no inflar tokens
        c = chunks_by_id.get(cid)
        if c:
            pieces.append(f"[{c['to']} · {c['location_label']}]\n{c['text'][:1200]}")
    return "\n\n---\n\n".join(pieces)


def collect_relations_for_node(node_id: str, kg: dict) -> str:
    """Serializa edges entrantes y salientes como triples para el prompt."""
    id_to_label = {n["id"]: n["label"] for n in kg["nodes"]}
    out_lines = [
        f"- {node['label']} --[{e['relation']}]--> {id_to_label.get(e['target'], e['target'])}"
        for e in kg["edges"] if e["source"] == node_id
        for node in [next(n for n in kg["nodes"] if n["id"] == node_id)]
    ]
    in_lines = [
        f"- {id_to_label.get(e['source'], e['source'])} --[{e['relation']}]--> {node['label']}"
        for e in kg["edges"] if e["target"] == node_id
        for node in [next(n for n in kg["nodes"] if n["id"] == node_id)]
    ]
    return "\n".join(sorted(set(out_lines + in_lines)))


# ---------------------------------------------------------------------------
# Llamada API — STUB
# ---------------------------------------------------------------------------

def call_sonnet_summarize(client, node: dict, excerpts: str, relations: str) -> tuple[EntityProfile, dict]:
    """Genera EntityProfile (summary + key_facts + time_range) para un hub. Cookbook §6."""
    schema = EntityProfile.model_json_schema()
    msg = client.messages.create(
        model=SUMMARIZATION_MODEL,
        max_tokens=MAX_TOKENS_OUT,
        messages=[{
            "role": "user",
            "content": SUMMARIZE_PROMPT.format(
                name=node["label"],
                etype=node["type"],
                excerpts=excerpts,
                relations=relations,
            ),
        }],
        tools=[{
            "name": "emit_profile",
            "description": "Emite el perfil resumido del nodo hub del KG.",
            "input_schema": schema,
        }],
        tool_choice={"type": "tool", "name": "emit_profile"},
    )
    tool_block = None
    for b in msg.content:
        if getattr(b, "type", None) == "tool_use":
            tool_block = b
            break
    if tool_block is None:
        raise RuntimeError(
            f"Sonnet no emitió tool_use para hub={node['id']} "
            f"(stop_reason={msg.stop_reason})"
        )
    profile = EntityProfile.model_validate(tool_block.input)
    usage = {
        "input_tokens": msg.usage.input_tokens,
        "output_tokens": msg.usage.output_tokens,
        "model": SUMMARIZATION_MODEL,
    }
    return profile, usage


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Etapa 5: hub summarization con Sonnet.")
    parser.add_argument("--top-k", type=int, default=TOP_K_HUBS_DEFAULT, help="Cantidad de hubs a resumir.")
    parser.add_argument("--dry-run", action="store_true", help="Listá hubs candidatos sin llamar a la API.")
    args = parser.parse_args(argv)

    if not KG_JSON_PATH.exists():
        print(f"[05_hub_summarize] Falta {KG_JSON_PATH}. Corré 04_assemble.py primero.")
        return 1
    if not EXTRACTIONS_PATH.exists():
        print(f"[05_hub_summarize] Falta {EXTRACTIONS_PATH}.")
        return 1

    kg = read_json(KG_JSON_PATH)
    hubs = select_hubs(kg, args.top_k)
    print(f"[05_hub_summarize] {len(hubs)} hubs candidatos (degree ≥ {HUB_MIN_DEGREE}):")
    deg = node_degree(kg)
    for h in hubs:
        print(f"  - {h['id']:40s}  deg={deg[h['id']]:3d}  ({h['type']})")

    if args.dry_run:
        return 0

    assert_under_budget()
    require_api_key()
    import anthropic
    client = anthropic.Anthropic()
    ledger = load_ledger(STAGE)

    extractions = read_jsonl(EXTRACTIONS_PATH)
    id_to_node = {n["id"]: n for n in kg["nodes"]}

    skipped_reason: dict[str, int] = defaultdict(int)
    for h in hubs:
        excerpts = collect_excerpts_for_node(h, extractions)
        if not excerpts:
            skipped_reason["no_excerpts"] += 1
            continue
        relations = collect_relations_for_node(h["id"], kg)
        try:
            profile, usage = call_sonnet_summarize(client, h, excerpts, relations)
        except NotImplementedError:
            raise
        except Exception as e:
            print(f"[05_hub_summarize] ERROR en {h['id']}: {type(e).__name__}: {e}")
            skipped_reason["error"] += 1
            continue
        ledger.record(usage["model"], usage["input_tokens"], usage["output_tokens"])
        assert_under_budget()

        node = id_to_node[h["id"]]
        node["properties"]["summary"] = profile.summary
        node["properties"]["key_facts"] = profile.key_facts
        node["properties"]["time_range"] = profile.time_range.model_dump()

    write_json(KG_JSON_PATH, kg)
    save_ledger(STAGE, ledger)

    print(f"[05_hub_summarize] OK · {len(hubs) - sum(skipped_reason.values())} hubs resumidos.")
    if skipped_reason:
        print(f"[05_hub_summarize] Skipped: {dict(skipped_reason)}")
    print(f"[05_hub_summarize] USD etapa: {ledger.total_usd:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
