"""
Análisis del smoke para el checkpoint con la autora.

Cuatro reportes:
  1. Ejemplos concretos de Conceptos candidatos a EntidadFinanciera (con texto
     fuente del chunk de origen).
  2. Dedup post-smoke: ensamblaje con heurística de plurales y normalización,
     reportando duplicados léxicos no fusionados.
  3. Estructura del grafo ensamblado: componentes conexos y % de nodos huérfanos.
  4. Calidad de labels: distribución de longitud en palabras, labels-frase.

Este script lee SOLO el cache del smoke (chunks del TO Protección al Usuario).
"""

from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from chunker import chunk_pdf
from models import Chunk

CACHE = Path(__file__).parent / "cache" / "chunks"
CACHE_V1 = Path(__file__).parent / "cache" / "chunks_v1"
SUBSET = Path("/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/subset")
SMOKE_PDF = SUBSET / "TO_proteccion_usuarios_servicios_financieros_actual.pdf"
SMOKE_PREFIX = "to_proteccion_usuarios_servicios_financi__"

CORE_TYPES = {"EntidadFinanciera", "Operacion", "Restriccion", "Excepcion"}
CATEGORIA_VOCAB = {
    "banco_comercial", "banco_inversion", "compania_financiera",
    "caja_credito", "casa_cambio", "agencia_cambio",
    "fideicomiso_financiero", "sgr", "proveedor_no_financiero_credito",
    "otra",
}
PAREN_DOC_RE = re.compile(r"\((?:punto|sección|seccion|anexo|capítulo|capitulo|art\.?)\s", re.IGNORECASE)


def _strip_combining(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c)
    )


def _normalize_label(s: str) -> str:
    """Normalización para dedup determinístico (regla §3.5 del schema)."""
    s = _strip_combining(s).lower().strip()
    s = re.sub(r"\s+", " ", s)
    return s


def _plural_canonical(norm: str) -> str:
    """Heurística simple de plurales: prueba quitar 'es' y 's'."""
    candidates = [norm]
    if norm.endswith("es") and len(norm) > 5:
        candidates.append(norm[:-2])
    if norm.endswith("s") and len(norm) > 4:
        candidates.append(norm[:-1])
    # devolvemos el más corto: es nuestra forma canónica candidata
    return min(candidates, key=len)


def load_smoke_extractions(cache_dir: Path = CACHE) -> list[dict[str, Any]]:
    files = sorted(cache_dir.glob(f"{SMOKE_PREFIX}*.json"))
    return [json.loads(f.read_text(encoding="utf-8")) for f in files]


def load_smoke_chunks() -> dict[str, Chunk]:
    return {c.chunk_id: c for c in chunk_pdf(SMOKE_PDF)}


# ============================================================================
# REPORTE 1 — Candidatos Concepto → EntidadFinanciera
# ============================================================================


def report_concepto_candidates(
    extractions: list[dict[str, Any]], chunks: dict[str, Chunk]
) -> None:
    """
    Selecciona Conceptos cuyo label/description sugieran que podrían ser
    EntidadFinanciera. Filtro: labels que contengan términos típicos de sujetos
    regulados ('entidad', 'sujeto obligado', 'operador', 'fiduciario', 'caja',
    'banco', 'compañía', 'sociedad', 'fondo', 'fideicomiso', 'agencia').
    """
    triggers = re.compile(
        r"\b(entidad|entidades|sujeto[s]? obligado|operador|fiduciar|caja|banco|"
        r"compañía|sociedad|fondo|fideicomis|agencia|proveedor|"
        r"corredor|comisionista|asegurador)\b",
        re.IGNORECASE,
    )
    candidates = []
    seen_norm = set()
    for ext in extractions:
        if not ext.get("parsed_ok"):
            continue
        for e in ext["parsed"]["entities"]:
            if e["type"] != "Concepto":
                continue
            label = e["label"]
            desc = (e.get("properties") or {}).get("description", "")
            if triggers.search(label) or triggers.search(desc):
                norm = _normalize_label(label)
                if norm in seen_norm:
                    continue
                seen_norm.add(norm)
                candidates.append({
                    "chunk_id": ext["chunk_id"],
                    "location": ext["location"],
                    "label": label,
                    "description": desc,
                })

    print("=" * 70)
    print("REPORTE 1 — Conceptos candidatos a ser EntidadFinanciera")
    print("=" * 70)
    print(f"Total candidatos únicos: {len(candidates)}")
    print()

    for ix, c in enumerate(candidates[:10], 1):
        chunk = chunks.get(c["chunk_id"])
        src_text = (chunk.text[:300] if chunk else "<chunk not in chunker>").replace("\n", " ")
        print(f"--- Candidato {ix} ---")
        print(f"  label:        {c['label']}")
        print(f"  description:  {c['description']}")
        print(f"  location:     {c['location']}")
        print(f"  texto fuente: {src_text}...")
        print()


# ============================================================================
# REPORTE 2 — Dedup post-smoke
# ============================================================================


def report_dedup(extractions: list[dict[str, Any]]) -> None:
    """
    Aplica la heurística de dedup del schema §3.5 sobre los nodos del smoke.
    Identifica nodos colapsados (correctamente) y nodos que probablemente
    deberían colapsar pero no lo hicieron (heurística laxa con substring).
    """
    print("=" * 70)
    print("REPORTE 2 — Dedup post-smoke")
    print("=" * 70)

    # Cargar todos los nodos crudos
    raw_nodes = []  # (id, type, label, norm, categoria)
    for ext in extractions:
        if not ext.get("parsed_ok"):
            continue
        for e in ext["parsed"]["entities"]:
            label = e["label"]
            cat = (e.get("properties") or {}).get("categoria", None)
            raw_nodes.append({
                "id": e["id"],
                "type": e["type"],
                "label": label,
                "norm": _normalize_label(label),
                "plural_canon": _plural_canonical(_normalize_label(label)),
                "categoria": cat,
            })

    print(f"Nodos crudos: {len(raw_nodes)}")

    # Aplicar dedup determinístico (regla §3.5):
    # clave canónica = (type, plural_canon, categoria-si-aplica)
    canonical: dict[tuple, list[dict]] = defaultdict(list)
    for n in raw_nodes:
        key_tail = n["categoria"] if n["type"] == "EntidadFinanciera" else None
        key = (n["type"], n["plural_canon"], key_tail)
        canonical[key].append(n)

    merged_groups = [g for g in canonical.values() if len(g) > 1]
    print(f"Nodos después de dedup determinístico: {len(canonical)}")
    print(f"  → Colapsos efectuados: {len(merged_groups)} grupos, "
          f"{sum(len(g)-1 for g in merged_groups)} nodos reducidos")
    print()

    print("Ejemplos de colapsos (top 8 por tamaño de grupo):")
    for g in sorted(merged_groups, key=lambda x: -len(x))[:8]:
        labels_in_g = sorted({n["label"] for n in g})
        print(f"  [{g[0]['type']}] {len(g)} nodos → 1:  {labels_in_g}")
    print()

    # Heurística "duplicados no resueltos": substring + mismo tipo
    print("Posibles duplicados léxicos NO resueltos (substring + mismo tipo):")
    canon_items = list(canonical.items())
    suspect_pairs = []
    for i in range(len(canon_items)):
        ti, key_i, _ = canon_items[i][0][0], canon_items[i][0], canon_items[i][1]
        norm_i = canon_items[i][0][1]
        for j in range(i + 1, len(canon_items)):
            tj = canon_items[j][0][0]
            if ti != tj:
                continue
            norm_j = canon_items[j][0][1]
            if norm_i == norm_j:
                continue
            if (norm_i in norm_j and len(norm_i) >= 5 and len(norm_j) <= len(norm_i) + 30) or \
               (norm_j in norm_i and len(norm_j) >= 5 and len(norm_i) <= len(norm_j) + 30):
                labels_i = sorted({n["label"] for n in canon_items[i][1]})[0]
                labels_j = sorted({n["label"] for n in canon_items[j][1]})[0]
                suspect_pairs.append((ti, labels_i, labels_j))
    suspect_pairs = suspect_pairs[:15]
    for t, a, b in suspect_pairs:
        print(f"  [{t}]  {a!r}  ↔  {b!r}")
    if not suspect_pairs:
        print("  (ninguno detectado por substring)")
    print(f"Total parejas sospechosas: {len(suspect_pairs)}")
    print()


# ============================================================================
# REPORTE 3 — Estructura del grafo ensamblado
# ============================================================================


def report_graph_structure(extractions: list[dict[str, Any]]) -> None:
    """
    Ensambla el grafo del smoke (con dedup determinístico) y reporta
    componentes conexos + nodos huérfanos.
    """
    print("=" * 70)
    print("REPORTE 3 — Estructura del grafo ensamblado")
    print("=" * 70)

    # Dedup y armado de mapa raw_id → canonical_id
    canonical: dict[tuple, str] = {}  # key → first canonical id
    id_map: dict[str, str] = {}  # raw_id → canonical_id
    node_types: dict[str, str] = {}
    node_labels: dict[str, str] = {}

    for ext in extractions:
        if not ext.get("parsed_ok"):
            continue
        for e in ext["parsed"]["entities"]:
            cat = (e.get("properties") or {}).get("categoria", None)
            key = (e["type"], _plural_canonical(_normalize_label(e["label"])),
                   cat if e["type"] == "EntidadFinanciera" else None)
            if key not in canonical:
                canonical[key] = e["id"]
                node_types[e["id"]] = e["type"]
                node_labels[e["id"]] = e["label"]
            id_map[e["id"]] = canonical[key]

    # Edges: solo aceptamos las que tienen source y target en el grafo del MISMO chunk
    edges: list[tuple[str, str, str]] = []
    for ext in extractions:
        if not ext.get("parsed_ok"):
            continue
        chunk_ids = {e["id"] for e in ext["parsed"]["entities"]}
        for r in ext["parsed"]["relations"]:
            if r["source"] not in chunk_ids or r["target"] not in chunk_ids:
                continue  # cross-chunk: omit (decisión Run 5)
            s = id_map.get(r["source"])
            t = id_map.get(r["target"])
            if s and t and s != t:
                edges.append((s, t, r["predicate"]))

    n_nodes = len(canonical)
    n_edges = len(edges)
    print(f"Nodos ensamblados (post-dedup): {n_nodes}")
    print(f"Edges válidos (intra-chunk):    {n_edges}")
    print(f"Densidad (edges/nodes):         {n_edges/max(1,n_nodes):.2f}")

    # Construir adyacencia no dirigida para componentes
    adj: dict[str, set[str]] = defaultdict(set)
    nodes_with_edge: set[str] = set()
    for s, t, _ in edges:
        adj[s].add(t)
        adj[t].add(s)
        nodes_with_edge.add(s)
        nodes_with_edge.add(t)

    orphans = [nid for nid in canonical.values() if nid not in nodes_with_edge]
    print(f"Nodos huérfanos (sin edges):    {len(orphans)} "
          f"({100*len(orphans)/max(1,n_nodes):.1f}%)")

    # Componentes conexos sobre los nodos con edges
    visited: set[str] = set()
    components: list[set[str]] = []
    for nid in adj:
        if nid in visited:
            continue
        stack = [nid]
        comp = set()
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            comp.add(cur)
            stack.extend(adj[cur] - visited)
        components.append(comp)
    # Sumamos los huérfanos como componentes triviales
    total_components = len(components) + len(orphans)
    print(f"Componentes conexos:            {total_components} "
          f"(no triviales: {len(components)}, triviales/huérfanos: {len(orphans)})")
    if components:
        sizes = sorted([len(c) for c in components], reverse=True)
        print(f"  Tamaños top: {sizes[:8]}")
        print(f"  Componente más grande:        {sizes[0]} nodos "
              f"({100*sizes[0]/max(1,n_nodes):.1f}% del grafo)")

    # Tipos huérfanos: qué tipos tienden a quedar sueltos
    orphan_types = Counter(node_types[nid] for nid in orphans)
    print("  Huérfanos por tipo:")
    for t, n in orphan_types.most_common():
        print(f"    {t:<30} {n}")
    print()


# ============================================================================
# REPORTE 4 — Calidad de labels
# ============================================================================


def report_label_quality(extractions: list[dict[str, Any]]) -> None:
    """
    Distribución de longitud (palabras) de los labels. Cuenta >8 (violación de
    Regla 5) y detecta labels-frase (descriptivos verbosos).
    """
    print("=" * 70)
    print("REPORTE 4 — Calidad de labels")
    print("=" * 70)

    labels: list[tuple[str, str]] = []  # (type, label)
    for ext in extractions:
        if not ext.get("parsed_ok"):
            continue
        for e in ext["parsed"]["entities"]:
            labels.append((e["type"], e["label"]))

    total = len(labels)
    lengths = Counter(len(lbl.split()) for _, lbl in labels)
    long_labels = [(t, lbl) for t, lbl in labels if len(lbl.split()) > 8]

    print(f"Total labels: {total}")
    print()
    print("Distribución de longitud (palabras):")
    for n in sorted(lengths):
        bar = "#" * min(50, lengths[n])
        print(f"  {n:>2} palabras: {lengths[n]:>4}  {bar}")
    print()
    avg = sum(n * c for n, c in lengths.items()) / max(1, total)
    median_w = sorted(len(lbl.split()) for _, lbl in labels)[total // 2]
    p95_w = sorted(len(lbl.split()) for _, lbl in labels)[int(total * 0.95)]
    print(f"  promedio: {avg:.2f} palabras")
    print(f"  median:   {median_w}")
    print(f"  p95:      {p95_w}")
    print()
    print(f"Labels > 8 palabras (violación Regla 5): {len(long_labels)} "
          f"({100*len(long_labels)/max(1,total):.1f}%)")
    print()
    print("Ejemplos de labels-frase (los 10 más largos):")
    for t, lbl in sorted(long_labels, key=lambda x: -len(x[1].split()))[:10]:
        print(f"  [{t}] ({len(lbl.split())}w)  {lbl!r}")
    print()


# ============================================================================
# REPORTE 5 — Comparativo v1 vs v2
# ============================================================================


def _summary(extractions: list[dict[str, Any]]) -> dict[str, Any]:
    """Resumen estructurado de un set de extracciones, para comparar."""
    total_ent = 0
    total_rel = 0
    by_type: Counter = Counter()
    cost = 0.0
    parsed_ok = 0
    parsed_fail = 0
    categoria_missing = 0
    categoria_otra = 0
    categoria_by_value: Counter = Counter()
    labels_over_8 = 0
    paren_doc_in_label = 0
    labels_by_type: dict[str, list[str]] = defaultdict(list)
    nodes_by_norm: dict[str, list[tuple[str, str]]] = defaultdict(list)  # norm → [(type, label)]
    predicates: Counter = Counter()

    for ext in extractions:
        cost += ext["input_tokens"] / 1e6 * 1.0 + ext["output_tokens"] / 1e6 * 5.0
        if not ext.get("parsed_ok"):
            parsed_fail += 1
            continue
        parsed_ok += 1
        for e in ext["parsed"]["entities"]:
            total_ent += 1
            by_type[e["type"]] += 1
            label = e["label"]
            labels_by_type[e["type"]].append(label)
            if len(label.split()) > 8:
                labels_over_8 += 1
            if PAREN_DOC_RE.search(label):
                paren_doc_in_label += 1
            norm = _normalize_label(label)
            nodes_by_norm[norm].append((e["type"], label))
            if e["type"] == "EntidadFinanciera":
                cat = (e.get("properties") or {}).get("categoria")
                if not cat:
                    categoria_missing += 1
                elif cat == "otra":
                    categoria_otra += 1
                if cat:
                    categoria_by_value[cat] += 1
        for r in ext["parsed"]["relations"]:
            total_rel += 1
            predicates[r["predicate"]] += 1

    return {
        "total_ent": total_ent,
        "total_rel": total_rel,
        "by_type": by_type,
        "cost": cost,
        "parsed_ok": parsed_ok,
        "parsed_fail": parsed_fail,
        "ef_categoria_missing": categoria_missing,
        "ef_categoria_otra": categoria_otra,
        "ef_categoria_by_value": categoria_by_value,
        "labels_over_8": labels_over_8,
        "paren_doc_in_label": paren_doc_in_label,
        "labels_by_type": labels_by_type,
        "nodes_by_norm": nodes_by_norm,
        "predicates": predicates,
    }


def report_v1_vs_v2() -> None:
    """Compara las extracciones v1 (cache/chunks_v1) y v2 (cache/chunks)."""
    print("=" * 70)
    print("REPORTE 5 — Comparativo v1 vs v2 (post-iteración del schema)")
    print("=" * 70)

    if not CACHE_V1.exists():
        print("(no se encuentra cache/chunks_v1 — v1 no preservada, omitiendo)")
        return

    v1 = _summary(load_smoke_extractions(CACHE_V1))
    v2 = _summary(load_smoke_extractions(CACHE))

    print(f"\nMETRIC                      v1            v2          Δ")
    print(f"  costo                     ${v1['cost']:.4f}      ${v2['cost']:.4f}    "
          f"{'+' if v2['cost'] >= v1['cost'] else ''}{v2['cost']-v1['cost']:+.4f}")
    print(f"  parsed OK                  {v1['parsed_ok']}            {v2['parsed_ok']}           "
          f"{v2['parsed_ok']-v1['parsed_ok']:+d}")
    print(f"  parsed FAIL                {v1['parsed_fail']}             {v2['parsed_fail']}            "
          f"{v2['parsed_fail']-v1['parsed_fail']:+d}")
    print(f"  total entidades            {v1['total_ent']}           {v2['total_ent']}          "
          f"{v2['total_ent']-v1['total_ent']:+d}")
    print(f"  total relaciones           {v1['total_rel']}           {v2['total_rel']}          "
          f"{v2['total_rel']-v1['total_rel']:+d}")
    print()

    print("Distribución de tipos (top 12 por v2):")
    print(f"  {'tipo':<28} {'v1':>6} {'v2':>6}  {'Δ abs':>7}  {'Δ pp':>7}")
    union_types = sorted(set(v1["by_type"]) | set(v2["by_type"]),
                          key=lambda t: -(v2["by_type"].get(t, 0)))
    tot_v1 = max(1, v1["total_ent"])
    tot_v2 = max(1, v2["total_ent"])
    for t in union_types[:12]:
        n1 = v1["by_type"].get(t, 0)
        n2 = v2["by_type"].get(t, 0)
        pp1 = 100 * n1 / tot_v1
        pp2 = 100 * n2 / tot_v2
        marker = "[CORE]" if t in CORE_TYPES else "      "
        print(f"  {marker} {t:<21} {n1:>6} {n2:>6}  {n2-n1:>+7}  {pp2-pp1:>+6.1f}pp")
    print()

    print("EntidadFinanciera — calidad de categoria:")
    print(f"  v1 categoria MISSING:    {v1['ef_categoria_missing']}")
    print(f"  v2 categoria MISSING:    {v2['ef_categoria_missing']}")
    print(f"  v1 categoria=otra:       {v1['ef_categoria_otra']}")
    print(f"  v2 categoria=otra:       {v2['ef_categoria_otra']}")
    print(f"  v2 categorias pobladas:  {dict(v2['ef_categoria_by_value'])}")
    print()

    print("Violaciones de Regla 5 (labels > 8 palabras):")
    print(f"  v1: {v1['labels_over_8']} ({100*v1['labels_over_8']/tot_v1:.1f}%)")
    print(f"  v2: {v2['labels_over_8']} ({100*v2['labels_over_8']/tot_v2:.1f}%)")
    print()

    print("Violaciones de Regla 6 (paréntesis documentales en label):")
    print(f"  v1: {v1['paren_doc_in_label']}")
    print(f"  v2: {v2['paren_doc_in_label']}")
    print()

    print("Movimientos esperados — labels que pasaron de Concepto (v1) a EntidadFinanciera (v2):")
    # Para cada label normalizado, ver cómo se clasificó en cada versión.
    promoted = []  # (label, prev_type)
    demoted = []
    new_in_v2 = []
    lost_from_v1 = []
    norms_v1 = set(v1["nodes_by_norm"].keys())
    norms_v2 = set(v2["nodes_by_norm"].keys())
    for norm in norms_v1 & norms_v2:
        # Tomamos el tipo más frecuente en cada versión.
        t1 = Counter(t for t, _ in v1["nodes_by_norm"][norm]).most_common(1)[0][0]
        t2 = Counter(t for t, _ in v2["nodes_by_norm"][norm]).most_common(1)[0][0]
        sample_label = v2["nodes_by_norm"][norm][0][1]
        if t1 == "Concepto" and t2 == "EntidadFinanciera":
            promoted.append((sample_label, t1, t2))
        elif t1 == "EntidadFinanciera" and t2 == "Concepto":
            demoted.append((sample_label, t1, t2))
        elif t1 != t2:
            pass  # otros cambios menos relevantes
    for norm in norms_v2 - norms_v1:
        t2 = Counter(t for t, _ in v2["nodes_by_norm"][norm]).most_common(1)[0][0]
        sample_label = v2["nodes_by_norm"][norm][0][1]
        if t2 == "EntidadFinanciera":
            new_in_v2.append((sample_label, t2))
    for norm in norms_v1 - norms_v2:
        t1 = Counter(t for t, _ in v1["nodes_by_norm"][norm]).most_common(1)[0][0]
        sample_label = v1["nodes_by_norm"][norm][0][1]
        if t1 == "EntidadFinanciera":
            lost_from_v1.append((sample_label, t1))

    print(f"  Concepto → EntidadFinanciera (promoted): {len(promoted)}")
    for lbl, t1, t2 in promoted[:15]:
        print(f"    {lbl!r}")
    print()
    print(f"  EntidadFinanciera → Concepto (demoted): {len(demoted)}")
    for lbl, t1, t2 in demoted[:10]:
        print(f"    {lbl!r}")
    print()
    print(f"  Labels nuevos en v2 que son EntidadFinanciera: {len(new_in_v2)}")
    for lbl, _ in new_in_v2[:15]:
        print(f"    {lbl!r}")
    print()
    print(f"  EntidadFinanciera de v1 desaparecidas en v2: {len(lost_from_v1)}")
    for lbl, _ in lost_from_v1[:10]:
        print(f"    {lbl!r}")
    print()


def main() -> None:
    extractions = load_smoke_extractions()
    chunks = load_smoke_chunks()
    print(f"[load] {len(extractions)} extracciones cacheadas (v2)")
    print(f"[load] {len(chunks)} chunks (re-derivados del PDF para texto fuente)")
    print()
    report_concepto_candidates(extractions, chunks)
    report_dedup(extractions)
    report_graph_structure(extractions)
    report_label_quality(extractions)
    report_v1_vs_v2()


if __name__ == "__main__":
    main()
