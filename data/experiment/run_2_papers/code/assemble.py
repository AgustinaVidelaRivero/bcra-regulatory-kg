"""
assemble.py — Ensamblaje del KG global a partir de extracciones por chunk.

Pipeline:
1. Por cada chunk, toma el output CLEAN (después de validate.py / reflect.py).
2. Para cada entity, computa el global_id = "{type_snake}:{slug(label)}".
3. Dedup determinístico: dos entities con mismo (type, slug) se mergean
   (properties acumulados, provenances en lista, label = más largo).
4. Mapea cada (chunk_id, local_id) → global_id.
5. Para cada relation, reescribe source/target a global_id, agrega
   provenance y dedup por (source, target, relation).

NO usa LLM. Resolución 100% determinística. Esto es lo que ahorra el
costo de Sonnet del Run 1 cookbook (~USD 4-5).

Salida: el dict que vamos a serializar como kg.json (formato sección b del
protocolo).
"""

from __future__ import annotations

import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable


# ---------------------------------------------------------------------------
# Slug
# ---------------------------------------------------------------------------

_TYPE_TO_SNAKE = {
    "SujetoRegulado": "sujeto_regulado",
    "OrganismoRegulador": "organismo_regulador",
    "Obligacion": "obligacion",
    "Operacion": "operacion",
    "ConceptoDefinido": "concepto_definido",
    "Requisito": "requisito",
    "Umbral": "umbral",
    "Plazo": "plazo",
    "Procedimiento": "procedimiento",
    "Sancion": "sancion",
    "InstrumentoFinanciero": "instrumento_financiero",
    "NormaReferenciada": "norma_referenciada",
}


def _strip_accents(s: str) -> str:
    nfkd = unicodedata.normalize("NFKD", s)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slug_label(label: str) -> str:
    s = _strip_accents(label or "").lower().strip()
    s = _NON_ALNUM.sub("_", s).strip("_")
    s = s[:80]  # cap defensivo
    return s or "unnamed"


def global_id(etype: str, label: str) -> str:
    return f"{_TYPE_TO_SNAKE.get(etype, etype.lower())}:{slug_label(label)}"


# ---------------------------------------------------------------------------
# Ensamblaje
# ---------------------------------------------------------------------------


@dataclass
class ChunkValidated:
    """Lo que cada chunk aporta al ensamblaje (después de validate/reflect)."""
    chunk_id: str
    source_doc: str
    location: str
    clean_entities: list[dict]   # con local_id
    clean_relations: list[dict]  # con local_id source/target
    post_retry_violation: bool = False  # flag §6 schema.md


def _merge_properties(a: dict, b: dict) -> dict:
    """Merge sin perder info. b sobreescribe a en colisión simple, listas concatenadas."""
    out = dict(a)
    for k, v in (b or {}).items():
        if k not in out:
            out[k] = v
            continue
        av = out[k]
        if av == v:
            continue
        # si ambos strings y distintos, los listamos
        if isinstance(av, list):
            if v not in av:
                av.append(v)
        else:
            out[k] = [av, v] if not isinstance(v, list) else [av] + [x for x in v if x != av]
    return out


def assemble(chunks: Iterable[ChunkValidated]) -> dict:
    """
    Devuelve {"nodes": [...], "edges": [...]} en el formato del protocolo §b.
    """
    nodes_by_gid: dict[str, dict] = {}
    edges_by_key: dict[tuple, dict] = {}
    flagged_chunks: list[str] = []

    for ch in chunks:
        if ch.post_retry_violation:
            flagged_chunks.append(ch.chunk_id)

        # map local_id → global_id for this chunk
        local2global: dict[str, str] = {}

        for e in ch.clean_entities:
            gid = global_id(e["type"], e["label"])
            local2global[e["local_id"]] = gid

            prov_entry = {
                "source_doc": ch.source_doc,
                "location": ch.location,
                "chunk_id": ch.chunk_id,
            }

            if gid not in nodes_by_gid:
                nodes_by_gid[gid] = {
                    "id": gid,
                    "type": e["type"],
                    "label": e["label"],
                    "properties": dict(e.get("properties") or {}),
                    "provenance": prov_entry,  # primera provenance principal
                    "_extra_provenances": [],  # provenances adicionales
                    "_alt_labels": set(),
                }
            else:
                node = nodes_by_gid[gid]
                # label más largo gana (más informativo)
                if len(e["label"]) > len(node["label"]):
                    node["_alt_labels"].add(node["label"])
                    node["label"] = e["label"]
                else:
                    if e["label"] != node["label"]:
                        node["_alt_labels"].add(e["label"])
                node["properties"] = _merge_properties(node["properties"], e.get("properties") or {})
                node["_extra_provenances"].append(prov_entry)

        # edges del chunk
        for r in ch.clean_relations:
            s_local = r["source"]
            t_local = r["target"]
            if s_local not in local2global or t_local not in local2global:
                # esto ya debería haberlo filtrado validate.py (V5), pero defensivo
                continue
            s_gid = local2global[s_local]
            t_gid = local2global[t_local]
            key = (s_gid, t_gid, r["relation"])
            prov_entry = {
                "source_doc": ch.source_doc,
                "location": ch.location,
                "chunk_id": ch.chunk_id,
            }
            if key not in edges_by_key:
                edges_by_key[key] = {
                    "source": s_gid,
                    "target": t_gid,
                    "relation": r["relation"],
                    "provenance": prov_entry,
                    "_extra_provenances": [],
                }
            else:
                edges_by_key[key]["_extra_provenances"].append(prov_entry)

    # Empacar a formato final (sección b del protocolo)
    nodes_out: list[dict] = []
    for gid, n in nodes_by_gid.items():
        props = dict(n["properties"])
        if n["_alt_labels"]:
            props["alt_labels"] = sorted(n["_alt_labels"])
        if n["_extra_provenances"]:
            props["additional_provenances"] = n["_extra_provenances"]
        nodes_out.append({
            "id": n["id"],
            "type": n["type"],
            "label": n["label"],
            "properties": props,
            "provenance": n["provenance"],
        })

    edges_out: list[dict] = []
    for e in edges_by_key.values():
        edge = {
            "source": e["source"],
            "target": e["target"],
            "relation": e["relation"],
            "provenance": e["provenance"],
        }
        if e["_extra_provenances"]:
            edge["additional_provenances"] = e["_extra_provenances"]
        edges_out.append(edge)

    return {
        "nodes": nodes_out,
        "edges": edges_out,
        "_meta": {
            "flagged_chunks_post_retry": flagged_chunks,
        },
    }
