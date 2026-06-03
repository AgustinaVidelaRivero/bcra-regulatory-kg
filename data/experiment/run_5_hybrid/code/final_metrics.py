"""
Métricas finales del KG ensamblado — Run 5.

Produce las lentes para el checkpoint final:
  1. Distribución de tipos (nodos) — protocolo §d.3
  2. Distribución de predicados (edges) — protocolo §d.4
  3. Densidad del grafo — protocolo §d.5
  4. Cobertura por TO — protocolo §d.8
  5. Fragmentación (componentes conexos, huérfanos)
  6. EntidadFinanciera por categoria + remap reporting
  7. Análisis post-hoc de predicados (canonicalización: case, plurales, sufijos)
"""

from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

RUN_DIR = Path(__file__).resolve().parent.parent
KG_PATH = RUN_DIR / "kg.json"

CORE_TYPES = {"EntidadFinanciera", "Operacion", "Restriccion", "Excepcion"}
CORE_RELATIONS = {"realiza", "aplica_a", "recae_sobre", "excepciona_a", "exime_a"}


def _strip_combining(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c)
    )


def _normalize_pred(p: str) -> str:
    """Normalización para análisis de canonicalización."""
    s = _strip_combining(p).lower().strip()
    s = re.sub(r"_+", "_", s)
    return s


def _plural_canonical(norm: str) -> str:
    if norm.endswith("es") and len(norm) > 5:
        return norm[:-2]
    if norm.endswith("s") and len(norm) > 4:
        return norm[:-1]
    return norm


def main() -> None:
    kg = json.loads(KG_PATH.read_text(encoding="utf-8"))
    nodes = kg["nodes"]
    edges = kg["edges"]

    print("=" * 72)
    print("MÉTRICAS FINALES — Run 5 Híbrido core + emergente")
    print(f"  kg.json: {len(nodes)} nodos, {len(edges)} edges")
    print("=" * 72)
    print()

    # ---- Lente 1: Distribución de tipos ----
    print("LENTE 1 — Distribución de tipos de nodo (protocolo §d.3)")
    print("-" * 72)
    by_type = Counter(n["type"] for n in nodes)
    total_n = len(nodes)
    core_total = sum(by_type[t] for t in CORE_TYPES)
    emergent_total = total_n - core_total
    print(f"  Total CORE: {core_total} ({100*core_total/total_n:.1f}%)")
    print(f"  Total EMERGENT: {emergent_total} ({100*emergent_total/total_n:.1f}%)")
    print()
    for t, n in by_type.most_common():
        marker = "[CORE]" if t in CORE_TYPES else "      "
        print(f"  {marker} {t:<30} {n:>5}  ({100*n/total_n:.1f}%)")
    print(f"  Tipos únicos de entidad: {len(by_type)}")
    print()

    # ---- Lente 2: Distribución de predicados ----
    print("LENTE 2 — Distribución de predicados (protocolo §d.4)")
    print("-" * 72)
    by_rel = Counter(e["relation"] for e in edges)
    total_e = len(edges)
    core_e = sum(by_rel[r] for r in CORE_RELATIONS)
    emergent_e = total_e - core_e
    print(f"  Total edges CORE: {core_e} ({100*core_e/total_e:.1f}%)")
    print(f"  Total edges EMERGENT: {emergent_e} ({100*emergent_e/total_e:.1f}%)")
    print(f"  Predicados únicos: {len(by_rel)}")
    print(f"  Top 20:")
    for p, n in by_rel.most_common(20):
        marker = "[CORE]" if p in CORE_RELATIONS else "      "
        print(f"    {marker} {p:<30} {n:>5}  ({100*n/total_e:.1f}%)")
    print()

    # ---- Lente 3: Densidad ----
    print("LENTE 3 — Densidad del grafo (protocolo §d.5)")
    print("-" * 72)
    print(f"  edges / nodes = {len(edges)} / {len(nodes)} = {len(edges)/len(nodes):.3f}")
    print()

    # ---- Lente 4: Cobertura por TO ----
    print("LENTE 4 — Cobertura por TO (protocolo §d.8)")
    print("-" * 72)
    nodes_by_doc = Counter(n["provenance"]["source_doc"] for n in nodes)
    edges_by_doc = Counter(e["provenance"]["source_doc"] for e in edges)
    docs = sorted(nodes_by_doc.keys())
    for d in docs:
        print(f"  {d[:55]:<55}  nodos={nodes_by_doc[d]:>4}  edges={edges_by_doc.get(d,0):>4}")
    print()

    # ---- Lente 5: Fragmentación ----
    print("LENTE 5 — Fragmentación del grafo")
    print("-" * 72)
    adj: dict[str, set[str]] = defaultdict(set)
    nodes_with_edge: set[str] = set()
    for e in edges:
        adj[e["source"]].add(e["target"])
        adj[e["target"]].add(e["source"])
        nodes_with_edge.add(e["source"])
        nodes_with_edge.add(e["target"])
    all_ids = {n["id"] for n in nodes}
    orphans = all_ids - nodes_with_edge
    # Componentes conexos no triviales
    visited: set[str] = set()
    components: list[set[str]] = []
    for nid in adj:
        if nid in visited:
            continue
        stack = [nid]
        comp: set[str] = set()
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            comp.add(cur)
            stack.extend(adj[cur] - visited)
        components.append(comp)
    component_sizes = sorted([len(c) for c in components], reverse=True)
    print(f"  Total nodos: {len(nodes)}")
    print(f"  Huérfanos (sin edges): {len(orphans)} ({100*len(orphans)/len(nodes):.1f}%)")
    print(f"  Componentes no triviales: {len(components)}")
    print(f"  Componentes totales (no triv + huérfanos): {len(components) + len(orphans)}")
    if component_sizes:
        print(f"  Componente más grande: {component_sizes[0]} nodos ({100*component_sizes[0]/len(nodes):.1f}% del grafo)")
        print(f"  Top 10 tamaños: {component_sizes[:10]}")
    nt_by_type = Counter()
    orphan_by_type = Counter()
    type_of = {n["id"]: n["type"] for n in nodes}
    for oid in orphans:
        orphan_by_type[type_of[oid]] += 1
    print("  Huérfanos por tipo:")
    for t, n in orphan_by_type.most_common(10):
        marker = "[CORE]" if t in CORE_TYPES else "      "
        print(f"    {marker} {t:<25} {n}")
    print()

    # ---- Lente 6: EntidadFinanciera por categoria ----
    print("LENTE 6 — EntidadFinanciera por categoria")
    print("-" * 72)
    ef_nodes = [n for n in nodes if n["type"] == "EntidadFinanciera"]
    cats = Counter((n.get("properties") or {}).get("categoria", "<MISSING>") for n in ef_nodes)
    print(f"  Total EntidadFinanciera: {len(ef_nodes)}")
    for c, n in cats.most_common():
        print(f"    {c:<40} {n}")
    print()

    # ---- Lente 7: Análisis post-hoc de predicados ----
    print("LENTE 7 — Análisis post-hoc de predicados (canonicalización)")
    print("-" * 72)
    raw_preds = list(by_rel.keys())
    # Agrupar por forma normalizada (lowercase + sin acentos + colapso subrayas)
    norm_groups: dict[str, list[str]] = defaultdict(list)
    for p in raw_preds:
        norm_groups[_normalize_pred(p)].append(p)
    # Plural canonical
    plural_groups: dict[str, list[str]] = defaultdict(list)
    for p in raw_preds:
        plural_groups[_plural_canonical(_normalize_pred(p))].append(p)

    case_dupes = {k: v for k, v in norm_groups.items() if len(v) > 1}
    plural_dupes = {
        k: v for k, v in plural_groups.items()
        if len(set(_normalize_pred(x) for x in v)) > 1
    }
    print(f"  Predicados únicos crudos: {len(raw_preds)}")
    print(f"  Predicados únicos post-normalización (lowercase + sin acentos): {len(norm_groups)}")
    print(f"  Predicados únicos post-plural-canonical: {len(plural_groups)}")
    print(f"  Ratio predicados/edges crudo: {len(raw_preds)/len(edges):.3f}")
    print(f"  Ratio predicados/edges post-canonicalización: {len(plural_groups)/len(edges):.3f}")
    print()
    print(f"  Grupos de case/acentos no canónicos (top 10):")
    for k, v in sorted(case_dupes.items(), key=lambda x: -len(x[1]))[:10]:
        print(f"    {k!r}  ←  {v}")
    print()
    print(f"  Grupos por singular/plural (top 10):")
    pl_sorted = [(k, v) for k, v in plural_dupes.items()]
    pl_sorted.sort(key=lambda x: -len(set(_normalize_pred(p) for p in x[1])))
    for k, v in pl_sorted[:10]:
        forms = sorted(set(v))
        print(f"    canónico={k!r}  ←  {forms}")
    print()
    # Predicados que violan tercera persona singular: heurística simple
    third_person_re = re.compile(r"^[a-z]+(_[a-z]+)*$")
    weird = [p for p in raw_preds if p.endswith("_por") or p.endswith("ar") or p.endswith("er") or p.endswith("ir")]
    weird = [p for p in weird if p not in CORE_RELATIONS]
    print(f"  Predicados con morfología sospechosa (infinitivo o sufijo _por): {len(weird)}")
    for w in sorted(weird)[:15]:
        n = by_rel[w]
        print(f"    {w:<30} (×{n})")
    print()


if __name__ == "__main__":
    main()
