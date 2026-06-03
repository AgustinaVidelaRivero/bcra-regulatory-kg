"""
Las 7 lentes originales del Run 5, especificadas por la autora del experimento.

NO toca kg.json. Solo análisis sobre el KG congelado. Output se pega en report.md
sección D.

  Lente 1 — Consistencia core vs emergente: misma entidad léxica con type distinto.
  Lente 2 — Cierre core↔core: violaciones + direcciones invertidas en los 5 cerrados.
  Lente 3 — Familias semánticas de predicados emergentes.
  Lente 4 — Tipos emergentes near-dup + ¿Concepto es cajón de sastre?
  Lente 5 — Duplicados léxicos de nodos post-dedup.
  Lente 6 — Fragmentación profundizada: TOs en el componente principal.
  Lente 7 — Calidad de labels por tipo.
"""

from __future__ import annotations

import json
import random
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

RUN_DIR = Path(__file__).resolve().parent.parent
KG_PATH = RUN_DIR / "kg.json"

CORE_TYPES = {"EntidadFinanciera", "Operacion", "Restriccion", "Excepcion"}
CORE_RELATIONS_DOMAIN_RANGE = {
    # predicado → (dominio, rango)  (rango como set si es unión)
    "realiza":      ("EntidadFinanciera", {"Operacion"}),
    "aplica_a":     ("Restriccion",       {"Operacion"}),
    "recae_sobre":  ("Restriccion",       {"EntidadFinanciera"}),
    "excepciona_a": ("Excepcion",         {"Restriccion"}),
    "exime_a":      ("Excepcion",         {"EntidadFinanciera", "Operacion"}),
}


def _strip_combining(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c)
    )


def _norm(s: str) -> str:
    s = _strip_combining(s).lower().strip()
    return re.sub(r"\s+", " ", s)


def _plural_canon(norm: str) -> str:
    if norm.endswith("es") and len(norm) > 5:
        return norm[:-2]
    if norm.endswith("s") and len(norm) > 4:
        return norm[:-1]
    return norm


# Familias semánticas curadas a partir de la inspección manual de top predicados.
# La pertenencia a una familia es lectura del autor del Run, no normalización
# vinculante del schema (que dice predicados libres en 3ra persona singular).
PREDICATE_FAMILIES = {
    "obligación / requerimiento": [
        "requiere", "obliga", "obliga_a", "exige", "demanda",
        "debe_cumplir", "debe_garantizar", "debe_presentar", "debe_proporcionar",
        "debe_adoptar", "debe_elaborar", "está_obligado_a", "está_obligada_a",
        "condiciona", "impone", "fuerza_a",
    ],
    "definición / inclusión": [
        "define", "comprende", "incluye", "abarca", "contiene", "engloba",
        "agrupa", "categoriza", "tipifica", "es_un",
        "forma_parte_de", "compone", "integra",
    ],
    "regulación / normativa": [
        "regula", "rige", "norma", "establece", "fija", "determina",
        "autoriza", "habilita", "permite", "prohibe", "prohíbe",
        "supervisa", "controla", "vigila", "fiscaliza",
    ],
    "modificación / actualización": [
        "modifica", "altera", "actualiza", "ajusta", "corrige", "reemplaza",
        "sustituye", "revoca", "anula", "extiende", "amplía",
    ],
    "información / reporte": [
        "informa_a", "reporta", "presenta", "comunica_a", "notifica",
        "declara_a", "registra", "documenta", "publica",
    ],
    "cálculo / cuantificación": [
        "calcula", "computa", "determina_por", "calcula_por", "expresa_en",
        "ajusta_por", "diferencia_por", "se_mide_en", "se_mide_con",
    ],
    "referencia / vínculo": [
        "referencia", "refiere_a", "remite_a", "menciona", "cita",
        "vincula_a", "se_relaciona_con", "asocia_a", "conecta_con",
    ],
    "alcance / aplicabilidad": [
        "alcanza_a", "afecta_a", "incide_en", "se_aplica_a", "se_extiende_a",
        "rige_para", "comprende_a",
    ],
    "exclusión / excepción": [
        "excluye", "exceptúa", "exonera", "no_aplica_a", "no_alcanza_a",
        "deja_fuera", "exime", "libera_de",
    ],
    "atribución / propiedad": [
        "tiene", "posee", "cuenta_con", "presenta_atributo", "es_propietario_de",
        "es_otorgada_por", "es_emitida_por", "es_administrada_por",
    ],
}


def lente_1_consistencia_core_emergente(nodes: list[dict]) -> None:
    """Misma entidad léxica con type distinto en el KG."""
    print("=" * 72)
    print("LENTE 1 — Consistencia core vs emergente")
    print("=" * 72)
    by_norm: dict[str, list[dict]] = defaultdict(list)
    for n in nodes:
        by_norm[_plural_canon(_norm(n["label"]))].append(n)

    inconsistent = []
    for norm, group in by_norm.items():
        types = {n["type"] for n in group}
        if len(types) > 1:
            inconsistent.append((norm, group))

    print(f"Total grupos de nodos con label normalizado idéntico: "
          f"{sum(1 for v in by_norm.values() if len(v) > 1)}")
    print(f"De esos, grupos con TYPE distinto entre miembros: {len(inconsistent)}")
    print()
    if not inconsistent:
        print("(ninguno — señal de consistencia perfecta)")
        return

    # Ordenar por más severo: que involucre un tipo core mezclado con emergente
    def severity(group):
        types = {n["type"] for n in group}
        core_count = len(types & CORE_TYPES)
        return -core_count, -len(group)

    inconsistent.sort(key=lambda x: severity(x[1]))
    print("Ejemplos (top 8 por severidad):")
    for norm, group in inconsistent[:8]:
        types = Counter(n["type"] for n in group)
        sample_label = group[0]["label"]
        print(f"  norm={norm!r}")
        print(f"    sample label: {sample_label!r}")
        print(f"    types: {dict(types)}")
        # Mostrar 1 location de cada tipo
        seen_types = set()
        for n in group:
            if n["type"] in seen_types:
                continue
            seen_types.add(n["type"])
            loc = n["provenance"]["location"][:60]
            print(f"      [{n['type']}] loc: {loc}")
        print()


def lente_2_cierre_core_core(nodes: list[dict], edges: list[dict]) -> None:
    """Violaciones del cierre core↔core: predicado no canónico o dominio/rango invertido."""
    print("=" * 72)
    print("LENTE 2 — Cierre core↔core")
    print("=" * 72)
    type_of = {n["id"]: n["type"] for n in nodes}

    # Pasada 1: edges donde source y target son core ¿predicado válido?
    core_core_edges = []
    for e in edges:
        ts = type_of.get(e["source"])
        tt = type_of.get(e["target"])
        if ts in CORE_TYPES and tt in CORE_TYPES:
            core_core_edges.append((ts, tt, e["relation"], e))

    print(f"Total edges core→core: {len(core_core_edges)}")

    valid_preds = set(CORE_RELATIONS_DOMAIN_RANGE.keys())
    non_canonical = [(ts, tt, rel, e) for ts, tt, rel, e in core_core_edges if rel not in valid_preds]
    print(f"Edges core→core con predicado NO canónico: {len(non_canonical)} "
          f"({100*len(non_canonical)/max(1,len(core_core_edges)):.1f}%)")
    nc_preds = Counter(rel for _, _, rel, _ in non_canonical)
    print(f"Top 10 predicados ofensores:")
    for rel, n in nc_preds.most_common(10):
        # Sample
        sample = next((e for ts, tt, r, e in non_canonical if r == rel), None)
        ts_sample = type_of.get(sample["source"], "?") if sample else "?"
        tt_sample = type_of.get(sample["target"], "?") if sample else "?"
        print(f"  {rel:<25} ×{n}   ej: {ts_sample}→{tt_sample}")
    print()

    # Pasada 2: edges con predicado canónico pero dominio/rango invertido o mal.
    print("Validación de dominio/rango para los 5 predicados canónicos:")
    for pred, (expected_dom, expected_ranges) in CORE_RELATIONS_DOMAIN_RANGE.items():
        edges_p = [(ts, tt, e) for ts, tt, rel, e in core_core_edges if rel == pred]
        ok = 0
        bad_dom = 0
        bad_range = 0
        inversions = 0
        bad_samples: list[tuple[str, str]] = []
        for ts, tt, e in edges_p:
            if ts == expected_dom and tt in expected_ranges:
                ok += 1
            elif tt == expected_dom and ts in expected_ranges:
                inversions += 1
                bad_samples.append((ts, tt))
            elif ts != expected_dom:
                bad_dom += 1
                bad_samples.append((ts, tt))
            else:
                bad_range += 1
                bad_samples.append((ts, tt))
        print(f"  {pred:<14} dom={expected_dom:<18} rng={sorted(expected_ranges)}")
        print(f"      ok={ok}  invertidos={inversions}  dominio_mal={bad_dom}  rango_mal={bad_range}  total={len(edges_p)}")
        if bad_samples:
            sample_str = ", ".join(f"{a}→{b}" for a, b in bad_samples[:3])
            print(f"      ej_invalidos: {sample_str}")
    print()


def lente_3_familias_predicados(edges: list[dict]) -> None:
    """Agrupar top 100 predicados emergentes en familias semánticas."""
    print("=" * 72)
    print("LENTE 3 — Familias semánticas de predicados emergentes")
    print("=" * 72)
    by_rel = Counter(e["relation"] for e in edges)
    core_set = set(CORE_RELATIONS_DOMAIN_RANGE.keys())
    emergent_preds = [(p, c) for p, c in by_rel.most_common() if p not in core_set]
    top100 = emergent_preds[:100]
    print(f"Predicados emergentes únicos: {len(emergent_preds)}")
    print(f"Top 100 emergentes cubren {sum(c for _, c in top100)} / "
          f"{sum(c for _, c in emergent_preds)} edges emergentes "
          f"({100*sum(c for _, c in top100)/max(1,sum(c for _,c in emergent_preds)):.1f}%)")
    print()

    # Mapeo: normalizamos cada predicado y buscamos coincidencia con alguna familia.
    def family_of(pred: str) -> str | None:
        norm = _norm(pred)
        for fam, members in PREDICATE_FAMILIES.items():
            for m in members:
                if _norm(m) == norm:
                    return fam
                # Coincidencia parcial: el predicado contiene el miembro o viceversa
                if _norm(m) in norm or norm in _norm(m):
                    # Solo si comparten >= 5 chars de raíz
                    if min(len(_norm(m)), len(norm)) >= 5:
                        return fam
        return None

    fam_counts: dict[str, list[tuple[str, int]]] = defaultdict(list)
    unmatched: list[tuple[str, int]] = []
    for pred, count in top100:
        fam = family_of(pred)
        if fam:
            fam_counts[fam].append((pred, count))
        else:
            unmatched.append((pred, count))

    print(f"Familias semánticas pobladas: {len(fam_counts)} / {len(PREDICATE_FAMILIES)} declaradas")
    print()
    for fam in sorted(fam_counts, key=lambda f: -sum(c for _, c in fam_counts[f])):
        members = sorted(fam_counts[fam], key=lambda x: -x[1])
        total = sum(c for _, c in members)
        print(f"  [{fam}] — {len(members)} predicados, {total} edges")
        for pred, c in members[:8]:
            print(f"    {pred:<28} ×{c}")
        if len(members) > 8:
            print(f"    ... y {len(members)-8} más")
        print()

    print(f"Predicados del top 100 NO mapeados a ninguna familia: {len(unmatched)}")
    for pred, c in unmatched[:20]:
        print(f"  {pred:<28} ×{c}")
    print()
    # Cuántos colapsarían si cada familia fuera 1 predicado
    collapse_total = sum(len(v) for v in fam_counts.values())
    print(f"Si cada familia colapsara a 1 predicado canónico:")
    print(f"  {collapse_total} predicados → {len([f for f in fam_counts if fam_counts[f]])} predicados")
    print(f"  (reducción de {collapse_total - len(fam_counts)} predicados únicos en el top 100)")
    print()


def lente_4_tipos_emergentes(nodes: list[dict], seed: int = 42) -> None:
    """Near-dups entre tipos emergentes + lectura honesta de Concepto."""
    print("=" * 72)
    print("LENTE 4 — Tipos emergentes (near-dups) y ¿Concepto es cajón de sastre?")
    print("=" * 72)
    type_counts = Counter(n["type"] for n in nodes)
    emergent_types = {t: c for t, c in type_counts.items() if t not in CORE_TYPES}
    print(f"Tipos emergentes únicos: {len(emergent_types)}")
    print()
    print("Inventario completo (orden por conteo desc):")
    for t, c in sorted(emergent_types.items(), key=lambda x: -x[1]):
        print(f"  {t:<28} {c}")
    print()

    # Near-dups por normalización léxica
    print("Pares de tipos emergentes con normalización léxica cercana:")
    type_names = list(emergent_types.keys())
    pairs_found = 0
    for i, t1 in enumerate(type_names):
        for t2 in type_names[i + 1:]:
            n1, n2 = _norm(t1), _norm(t2)
            # Comparte prefijo largo o uno contiene al otro
            if n1 == n2:
                pass  # imposible en este punto
            elif n1 in n2 or n2 in n1:
                if min(len(n1), len(n2)) >= 5:
                    print(f"  {t1!r} ({emergent_types[t1]}) ↔ {t2!r} ({emergent_types[t2]})")
                    pairs_found += 1
            else:
                # Distancia de Levenshtein heurística simple por longitud común
                # Solo flaggemos si comparten >= 80% de chars
                pass
    if pairs_found == 0:
        print("  (ninguno por substring)")
    print()
    # Inspección manual: tipo con typo obvio (NormaSuprior)
    typo_candidates = [t for t in emergent_types if "Suprior" in t or "Inferior" in t]
    if typo_candidates:
        print(f"Typos detectados manualmente: {typo_candidates}")
        print()

    # Concepto basurero?
    print("--- ¿Concepto es cajón de sastre? Muestra aleatoria de 20 labels ---")
    random.seed(seed)
    concepto_nodes = [n for n in nodes if n["type"] == "Concepto"]
    sample = random.sample(concepto_nodes, min(20, len(concepto_nodes)))
    for n in sample:
        loc = n["provenance"]["location"][:50]
        print(f"  • {n['label']!r:<60}  [{n['provenance']['source_doc'][:30]}, {loc}]")
    print()


def lente_5_dups_lexicos_post_dedup(nodes: list[dict]) -> None:
    """Parejas de nodos sospechosamente similares que el dedup no fusionó."""
    print("=" * 72)
    print("LENTE 5 — Duplicados léxicos de nodos post-dedup")
    print("=" * 72)
    # Agrupar por norma + plural_canon
    by_key: dict[tuple, list[dict]] = defaultdict(list)
    for n in nodes:
        norm = _norm(n["label"])
        pc = _plural_canon(norm)
        # Para EntidadFinanciera incluir categoria en la clave (consistente con assemble)
        if n["type"] == "EntidadFinanciera":
            cat = (n.get("properties") or {}).get("categoria")
            key = (n["type"], pc, cat)
        else:
            key = (n["type"], pc, None)
        by_key[key].append(n)

    # Heurística laxa: pares de claves donde el plural_canon de uno está contenido en el otro
    print(f"Nodos post-dedup: {len(nodes)}")
    keys = list(by_key.keys())
    suspect_pairs: dict[str, list[tuple[str, str, int, int]]] = defaultdict(list)
    for i in range(len(keys)):
        ti, pi, _ = keys[i]
        for j in range(i + 1, len(keys)):
            tj, pj, _ = keys[j]
            if ti != tj:
                continue
            if pi == pj:
                continue
            # Substring containment laxo
            if (pi in pj and len(pi) >= 5 and len(pj) <= len(pi) + 30) or \
               (pj in pi and len(pj) >= 5 and len(pi) <= len(pj) + 30):
                lbl_i = by_key[keys[i]][0]["label"]
                lbl_j = by_key[keys[j]][0]["label"]
                ci = len(by_key[keys[i]])
                cj = len(by_key[keys[j]])
                suspect_pairs[ti].append((lbl_i, lbl_j, ci, cj))

    total = sum(len(v) for v in suspect_pairs.values())
    print(f"Pares sospechosos (substring + mismo tipo, plural-canon distinto): {total}")
    print()
    for t in sorted(suspect_pairs, key=lambda x: -len(suspect_pairs[x])):
        pairs = suspect_pairs[t]
        marker = "[CORE]" if t in CORE_TYPES else "      "
        print(f"  {marker} {t} — {len(pairs)} parejas (top 15):")
        for a, b, ca, cb in pairs[:15]:
            print(f"    {a!r}  ↔  {b!r}")
        print()


def lente_6_fragmentacion_TOs(nodes: list[dict], edges: list[dict]) -> None:
    """¿El componente principal conecta los 5 TOs? Distribución por TO en el principal."""
    print("=" * 72)
    print("LENTE 6 — Fragmentación: TOs en el componente principal")
    print("=" * 72)
    adj: dict[str, set[str]] = defaultdict(set)
    for e in edges:
        adj[e["source"]].add(e["target"])
        adj[e["target"]].add(e["source"])
    # Componentes
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
    components.sort(key=len, reverse=True)
    by_id = {n["id"]: n for n in nodes}

    print(f"Componentes no triviales: {len(components)}")
    if not components:
        return
    main = components[0]
    print(f"Componente principal: {len(main)} nodos ({100*len(main)/len(nodes):.1f}% del grafo)")
    print()
    # Distribución por TO en el componente principal
    doc_in_main = Counter(by_id[nid]["provenance"]["source_doc"] for nid in main)
    print("Distribución por TO en el componente PRINCIPAL:")
    for d, n in sorted(doc_in_main.items(), key=lambda x: -x[1]):
        print(f"  {d[:55]:<55} {n}")
    print()
    print("Distribución por TO en el grafo TOTAL (para comparar):")
    doc_total = Counter(n["provenance"]["source_doc"] for n in nodes)
    for d, n in sorted(doc_total.items(), key=lambda x: -x[1]):
        in_main = doc_in_main.get(d, 0)
        pct = 100 * in_main / max(1, n)
        print(f"  {d[:55]:<55} total={n:>5}  en_principal={in_main:>5}  ({pct:.1f}%)")
    print()
    print("Top 5 componentes no triviales (después del principal):")
    for i, comp in enumerate(components[1:6], start=2):
        docs = Counter(by_id[nid]["provenance"]["source_doc"] for nid in comp)
        types = Counter(by_id[nid]["type"] for nid in comp)
        labels = [by_id[nid]["label"] for nid in list(comp)[:5]]
        print(f"  #{i}: {len(comp)} nodos")
        print(f"      docs: {dict(docs)}")
        print(f"      types: {dict(types)}")
        print(f"      labels muestra: {labels}")
    print()


def lente_7_calidad_labels(nodes: list[dict]) -> None:
    """Distribución de longitud de label por tipo + outliers + labels-frase."""
    print("=" * 72)
    print("LENTE 7 — Calidad de labels por tipo")
    print("=" * 72)
    by_type: dict[str, list[str]] = defaultdict(list)
    for n in nodes:
        by_type[n["type"]].append(n["label"])

    print(f"{'tipo':<28} {'n':>5} {'min':>4} {'med':>4} {'mean':>5} {'p95':>4} {'max':>4}  {'>8w':>5}  {'%>8':>5}")
    rows = []
    for t, labels in by_type.items():
        ws = sorted(len(l.split()) for l in labels)
        n = len(ws)
        mean_w = sum(ws) / n
        median_w = ws[n // 2]
        p95_w = ws[int(n * 0.95)] if n > 1 else ws[0]
        over8 = sum(1 for w in ws if w > 8)
        rows.append((t, n, ws[0], median_w, mean_w, p95_w, ws[-1], over8))
    rows.sort(key=lambda r: -r[1])
    for t, n, mn, me, av, p9, mx, o8 in rows:
        pct = 100 * o8 / n
        marker = "[CORE]" if t in CORE_TYPES else "      "
        print(f"  {marker} {t:<22} {n:>5} {mn:>4} {me:>4} {av:>5.1f} {p9:>4} {mx:>4}  {o8:>5}  {pct:>5.1f}%")
    print()

    # Top 10 labels-frase por tipo (solo tipos con al menos un >8)
    print("Top 10 labels-frase por tipo (labels >8 palabras):")
    for t, labels in by_type.items():
        long_labels = [l for l in labels if len(l.split()) > 8]
        if not long_labels:
            continue
        marker = "[CORE]" if t in CORE_TYPES else "      "
        print(f"  {marker} {t}: {len(long_labels)} labels-frase")
        for l in sorted(long_labels, key=lambda x: -len(x.split()))[:10]:
            print(f"    ({len(l.split())}w)  {l!r}")
        print()


def main() -> None:
    kg = json.loads(KG_PATH.read_text(encoding="utf-8"))
    nodes = kg["nodes"]
    edges = kg["edges"]
    print(f"Cargado kg.json: {len(nodes)} nodos, {len(edges)} edges\n")
    lente_1_consistencia_core_emergente(nodes)
    lente_2_cierre_core_core(nodes, edges)
    lente_3_familias_predicados(edges)
    lente_4_tipos_emergentes(nodes)
    lente_5_dups_lexicos_post_dedup(nodes)
    lente_6_fragmentacion_TOs(nodes, edges)
    lente_7_calidad_labels(nodes)


if __name__ == "__main__":
    main()
