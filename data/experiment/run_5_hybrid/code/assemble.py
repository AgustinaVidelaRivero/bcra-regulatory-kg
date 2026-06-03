"""
Ensamblador del KG — Run 5 Híbrido core + emergente.

Lee los chunks cacheados en cache/chunks/ y construye el kg.json final siguiendo
el formato obligatorio del protocolo §b.

POST-PROCESAMIENTO DETERMINÍSTICO (no iteración del schema):

1. **`canonicalize_categoria`** — Si `EntidadFinanciera.properties.categoria` no
   pertenece al vocabulario controlado de §3.5, se mapea a `"otra"`. **NUNCA**
   se mapea a un superset interpretado (p. ej. `proveedor_no_financiero_credito`
   o `compania_financiera`) — esa decisión sería regulatoria post-hoc debatible.
   El vocabulario declara `"otra"` justamente para casos no canónicos.

2. **Dedup determinístico** — Reglas §3.5:
   - Normalización del label: lowercase + sin acentos (NFD) + colapso de espacios.
   - Heurística simple de plurales: prueba quitar 'es' y 's' si len >= 4.
   - `EntidadFinanciera`: deduplica por (norm_label, categoria) — misma norma con
     categoría distinta son nodos distintos (refinamiento legítimo del schema).
   - Otros tipos: deduplica por (type, norm_label).
   - Edges con (source, target, relation) idénticos post-mapeo colapsan a 1.

3. **Inyección de provenance** — Cada nodo y edge lleva `provenance` del PRIMER
   chunk en el que apareció. Las menciones adicionales se conservan internamente
   pero no se serializan (el protocolo §b define `provenance` singular).

4. **Filtro de jerarquía documental** — Si un nodo tiene label que matchea
   patrones de referencia documental ("Punto X", "Sección Y", "Anexo Z",
   "Capítulo W"), se descarta. Refuerzo post-hoc de Regla 6.

5. **Self-loops** — Edges con source == target post-dedup se descartan.

Los clusters léxicos ambiguos NO resueltos por la heurística determinística
quedan como nodos separados (limitación declarada en §3.6, sin uso de LLM).
"""

from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from models import KGEdge, KGNode, KnowledgeGraph, Provenance


CACHE = Path(__file__).parent / "cache" / "chunks"
RUN_DIR = Path(__file__).resolve().parent.parent  # data/experiment/run_5_hybrid/

CORE_TYPES = {"EntidadFinanciera", "Operacion", "Restriccion", "Excepcion"}
CORE_RELATIONS = {"realiza", "aplica_a", "recae_sobre", "excepciona_a", "exime_a"}

CONTROLLED_VOCAB = {
    "banco_comercial",
    "banco_inversion",
    "compania_financiera",
    "caja_credito",
    "casa_cambio",
    "agencia_cambio",
    "fideicomiso_financiero",
    "sgr",
    "proveedor_no_financiero_credito",
    "otra",
}

# Patrones de jerarquía documental — refuerzo post-hoc de Regla 6.
# Requiere un dígito o romano después del nombre para evitar falsos positivos
# (p. ej. "Punto de unión del tramo (A)" es contenido regulatorio, no jerarquía).
DOC_HIERARCHY_RE = re.compile(
    r"^(punto|secci[óo]n|cap[íi]tulo|anexo|art[íi]culo|art\.)\s+(\d|[ivxlcdm]+(\s|$))",
    re.IGNORECASE,
)


# ---------- Helpers determinísticos ----------


def canonicalize_categoria(cat: str | None) -> str:
    """
    Mapea cualquier categoría a `"otra"` si no está en el vocabulario controlado.
    NO se mapea a supersets — mapear a un superset interpretado introduciría una
    decisión regulatoria post-hoc debatible.
    """
    if not cat:
        return "otra"
    return cat if cat in CONTROLLED_VOCAB else "otra"


def _strip_combining(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c)
    )


def _normalize_label(s: str) -> str:
    """lowercase + sin acentos + colapso de espacios + recorte."""
    s = _strip_combining(s).lower().strip()
    s = re.sub(r"\s+", " ", s)
    return s


def _plural_canonical(norm: str) -> str:
    """Forma canónica candidata: la más corta entre la norma y sus singularizaciones."""
    candidates = [norm]
    if norm.endswith("es") and len(norm) > 5:
        candidates.append(norm[:-2])
    if norm.endswith("s") and len(norm) > 4:
        candidates.append(norm[:-1])
    return min(candidates, key=len)


def _slug_id(label: str, type_: str, categoria: str | None = None) -> str:
    """ID canónico estable, derivado del label normalizado."""
    base = _strip_combining(label).lower()
    base = re.sub(r"[^a-z0-9]+", "_", base).strip("_")
    base = base[:60]
    suffix = ""
    if type_ == "EntidadFinanciera" and categoria:
        suffix = f"__{categoria}"
    return f"{base}{suffix}" if base else f"node_{type_.lower()}{suffix}"


def _is_doc_hierarchy_label(label: str) -> bool:
    return bool(DOC_HIERARCHY_RE.match(label.strip()))


# ---------- Carga del cache ----------


def load_all_extractions() -> list[dict[str, Any]]:
    files = sorted(CACHE.glob("*.json"))
    out = []
    for f in files:
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
            if d.get("parsed_ok") and not d.get("error"):
                out.append(d)
        except Exception:
            continue
    return out


# ---------- Ensamblaje ----------


def assemble(extractions: list[dict[str, Any]]) -> tuple[KnowledgeGraph, dict[str, Any]]:
    """
    Ensambla el KG con dedup determinístico. Retorna (kg, stats).
    """
    # Mapas: clave canónica → primer KGNode visto
    nodes_by_key: dict[tuple, KGNode] = {}
    # raw_id (de un chunk) → canonical_id (en el KG final)
    raw_id_to_canonical: dict[str, str] = {}
    # Para reportar mapeos de categoria no canónica
    categoria_remaps: Counter = Counter()  # (raw_cat) -> n
    # Nodos filtrados por jerarquía documental
    filtered_doc_hierarchy: list[tuple[str, str]] = []
    # Edges crudos antes de dedup
    raw_edges: list[tuple[str, str, str, Provenance]] = []

    stats = {
        "extractions": len(extractions),
        "raw_nodes": 0,
        "raw_edges": 0,
        "filtered_doc_hierarchy": 0,
        "self_loops": 0,
        "cross_chunk_edges_dropped": 0,
        "categoria_remap_to_otra": 0,
        "categoria_remap_sources": Counter(),
        "nodes_final": 0,
        "edges_final": 0,
        "edges_collapsed": 0,
    }

    # ---- Pasada 1: nodos ----
    for ext in extractions:
        source_doc = ext["source_doc"]
        location = ext["location"]
        prov = Provenance(source_doc=source_doc, location=location)

        # Mapa local del chunk: raw_id (lo que el LLM puso) → canonical_id final
        # (mismo chunk puede tener el mismo id repetido, pero asumimos que el LLM
        # no se contradice intra-chunk).
        local_map: dict[str, str] = {}

        for e in ext["parsed"]["entities"]:
            stats["raw_nodes"] += 1
            label = e["label"].strip()
            type_ = e["type"]
            props_raw = dict(e.get("properties") or {})

            # Filtro de jerarquía documental
            if _is_doc_hierarchy_label(label):
                stats["filtered_doc_hierarchy"] += 1
                filtered_doc_hierarchy.append((type_, label))
                continue

            # Canonicalización de categoria para EntidadFinanciera
            if type_ == "EntidadFinanciera":
                raw_cat = props_raw.get("categoria")
                canon_cat = canonicalize_categoria(raw_cat)
                if raw_cat and raw_cat != canon_cat:
                    stats["categoria_remap_to_otra"] += 1
                    stats["categoria_remap_sources"][raw_cat] += 1
                props_raw["categoria"] = canon_cat
            else:
                # Para tipos no-EntidadFinanciera, removemos categoria si el modelo
                # la puso por error (no aplica a esos tipos en el schema).
                props_raw.pop("categoria", None)

            # Clave canónica para dedup
            norm = _normalize_label(label)
            pc = _plural_canonical(norm)
            if type_ == "EntidadFinanciera":
                key = (type_, pc, props_raw.get("categoria"))
                canon_id = _slug_id(label, type_, props_raw.get("categoria"))
            else:
                key = (type_, pc, None)
                canon_id = _slug_id(label, type_)

            if key in nodes_by_key:
                # Ya existía — mergear properties (suma de descripciones, etc).
                existing = nodes_by_key[key]
                existing_props = dict(existing.properties)
                # Mantener la description más larga (suele ser la más informativa).
                new_desc = props_raw.get("description", "")
                old_desc = existing_props.get("description", "")
                if len(new_desc) > len(old_desc):
                    existing_props["description"] = new_desc
                # categoria ya validada, no se sobreescribe.
                existing.properties = existing_props
                local_map[e["id"]] = existing.id
            else:
                node = KGNode(
                    id=canon_id,
                    type=type_,
                    label=label,
                    properties=props_raw,
                    provenance=prov,
                )
                nodes_by_key[key] = node
                local_map[e["id"]] = canon_id

        # ---- Pasada 1b: edges del chunk (solo intra-chunk, ids válidos) ----
        local_ids = {e["id"] for e in ext["parsed"]["entities"]}
        for r in ext["parsed"]["relations"]:
            stats["raw_edges"] += 1
            if r["source"] not in local_ids or r["target"] not in local_ids:
                stats["cross_chunk_edges_dropped"] += 1
                continue
            s_canon = local_map.get(r["source"])
            t_canon = local_map.get(r["target"])
            if not s_canon or not t_canon:
                # source/target fue filtrado por jerarquía documental
                continue
            if s_canon == t_canon:
                stats["self_loops"] += 1
                continue
            raw_edges.append((s_canon, t_canon, r["predicate"], prov))

    # ---- Pasada 2: dedup de edges ----
    seen_edges: dict[tuple[str, str, str], KGEdge] = {}
    for s, t, rel, prov in raw_edges:
        key = (s, t, rel)
        if key in seen_edges:
            stats["edges_collapsed"] += 1
            continue
        seen_edges[key] = KGEdge(source=s, target=t, relation=rel, provenance=prov)

    stats["nodes_final"] = len(nodes_by_key)
    stats["edges_final"] = len(seen_edges)
    stats["filtered_doc_hierarchy_examples"] = filtered_doc_hierarchy[:10]

    kg = KnowledgeGraph(
        nodes=list(nodes_by_key.values()),
        edges=list(seen_edges.values()),
    )
    return kg, stats


# ---------- CLI ----------


def main() -> None:
    extractions = load_all_extractions()
    print(f"[load] {len(extractions)} extracciones parseadas OK")

    kg, stats = assemble(extractions)

    out_path = RUN_DIR / "kg.json"
    payload = kg.model_dump(mode="json")
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[write] {out_path}")
    print()
    print("=== STATS ===")
    for k, v in stats.items():
        if isinstance(v, Counter):
            print(f"  {k}: {dict(v)}")
        else:
            print(f"  {k}: {v}")
    print()

    # Resumen rápido para checkpoint
    from collections import Counter as _C
    by_type = _C(n.type for n in kg.nodes)
    by_rel = _C(e.relation for e in kg.edges)
    print("=== Distribución por tipo de nodo ===")
    for t, n in by_type.most_common():
        marker = "[CORE]" if t in CORE_TYPES else "      "
        print(f"  {marker} {t:<30} {n}")
    print(f"  TOTAL: {sum(by_type.values())} nodos")
    print()
    print("=== Top 15 predicados ===")
    for p, n in by_rel.most_common(15):
        marker = "[CORE]" if p in CORE_RELATIONS else "      "
        print(f"  {marker} {p:<30} {n}")
    print(f"  TOTAL: {sum(by_rel.values())} edges  |  {len(by_rel)} predicados únicos")
    print()
    print(f"Densidad: {len(kg.edges)/max(1,len(kg.nodes)):.3f} edges/nodo")


if __name__ == "__main__":
    main()
