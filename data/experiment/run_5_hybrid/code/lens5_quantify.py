"""
Cuantificación de las parejas léxicas sospechosas de la Lente 5.

Clasifica cada pareja sospechosa en una de tres categorías mutuamente excluyentes
y reporta conteos total + por tipo de nodo. NO toca kg.json — solo análisis.

Categorías:

  (1) substring_strict — el label más corto es prefijo o sufijo (a nivel
      palabras enteras) del más largo, y el más largo tiene palabras adicionales
      reales. Lectura: refinamiento legítimo (el nodo más largo es una versión
      especializada/subtipo del más corto). NO son duplicados a resolver.

  (2) norm_equivalent — al normalizar más allá de la heurística declarada en
      §3.5 (paréntesis residuales, siglas/abreviaturas, variantes de plural
      internas fuera del último carácter), los dos labels son equivalentes.
      Lectura: duplicado real no fusionado por la heurística determinística.

  (3) ambiguous — no encaja claramente en ninguna de las dos.

Las sub-categorías de norm_equivalent se reportan separadas para inspección:
  norm_eq_paren    — paréntesis residual (ej. "X (BCRA)" vs "X").
  norm_eq_abbrev   — uno es sigla del otro (ej. "CNV" vs "Comisión Nacional de Valores").
  norm_eq_plural   — variantes de plural internas fuera de la heurística sufijal
                     (ej. "Persona humana" vs "Personas humanas").
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


# ---------------------- Clasificador ----------------------


def _strip_parens(words: list[str]) -> list[str]:
    """Quita tokens parentéticos completos y devuelve la lista de palabras restantes."""
    text = " ".join(words)
    text = re.sub(r"\s*\([^)]*\)\s*", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.split()


def _is_sigla_de(short_words: list[str], long_words: list[str]) -> bool:
    """¿short es la sigla del long?  Ej.: 'cnv' ↔ ['comision','nacional','de','valores']"""
    if len(short_words) != 1:
        return False
    sigla = short_words[0].replace(".", "").lower()
    if not (2 <= len(sigla) <= 8):
        return False
    # Iniciales del long (omitiendo preposiciones cortas y conjunciones)
    skip = {"de", "del", "la", "el", "los", "las", "y", "o", "a", "en"}
    initials = "".join(w[0] for w in long_words if w and w not in skip and w[0].isalpha())
    initials = initials.lower()
    return sigla == initials


def _is_plural_internal(words_a: list[str], words_b: list[str]) -> bool:
    """
    Variante de plural/singular fuera de la heurística sufijal. Mismo número de
    palabras, diferencias mínimas word-por-word (prefijo común largo).
    """
    if len(words_a) != len(words_b):
        return False
    any_diff = False
    for wa, wb in zip(words_a, words_b):
        if wa == wb:
            continue
        any_diff = True
        if len(wa) < 3 or len(wb) < 3:
            return False
        # Prefijo común
        common = 0
        for i in range(min(len(wa), len(wb))):
            if wa[i] == wb[i]:
                common += 1
            else:
                break
        if common < min(len(wa), len(wb)) - 2:
            # Diferencia es más que solo final
            return False
    return any_diff


def classify_pair(label_a: str, label_b: str) -> str:
    """
    Clasifica una pareja sospechosa en una de las 3 categorías + sub-categorías.

    ORDEN DE REGLAS: norm_equivalent va PRIMERO. Si no, substring_strict. Si no,
    ambiguous. (El orden importa: "X (BCRA)" vs "X" se debe detectar como
    paréntesis residual, no como substring strict.)
    """
    wa = _norm(label_a).split()
    wb = _norm(label_b).split()
    # Garantizar a ≤ b en longitud de palabras (si empatan, ordenamos por chars).
    if len(wa) > len(wb) or (len(wa) == len(wb) and len(" ".join(wa)) > len(" ".join(wb))):
        wa, wb = wb, wa

    # ==== (1) norm_equivalent — chequeo PRIMERO para no perderlo en substring ====

    # (1a) Paréntesis residual: el más largo, sin paréntesis, iguala al más corto.
    wb_clean = _strip_parens(wb)
    wa_clean = _strip_parens(wa)
    if (wb_clean and wb_clean == wa) or (wa_clean and wa_clean == wb) or (
        wb_clean and wa_clean and wb_clean == wa_clean and wb_clean != wb
    ):
        return "norm_eq_paren"

    # (1b) Sigla / abreviatura.
    if _is_sigla_de(wa, wb) or _is_sigla_de(wb, wa):
        return "norm_eq_abbrev"
    # Paréntesis con sigla — el más largo termina en "(sigla)" que matchea al corto
    full_b = " ".join(wb)
    paren_match = re.search(r"\(([^)]+)\)$", full_b)
    if paren_match:
        sigla_in_paren = paren_match.group(1).strip().split()
        if _is_sigla_de(sigla_in_paren, wa) or " ".join(sigla_in_paren).lower() == " ".join(wa):
            return "norm_eq_abbrev"

    # (1c) Plural interno (mismo número de palabras, diferencias internas fuera de sufijo).
    if _is_plural_internal(wa, wb):
        return "norm_eq_plural"

    # ==== (2) Substring strict — sólo si no entró en norm_equivalent ====
    if len(wb) > len(wa):
        if wb[: len(wa)] == wa:
            return "substring_strict"
        if wb[-len(wa) :] == wa:
            return "substring_strict"

    # ==== (3) Ambiguo ====
    return "ambiguous"


# ---------------------- Reproducción de las parejas sospechosas ----------------------


def find_suspect_pairs(nodes: list[dict]) -> list[dict]:
    """Replica la heurística de lente 5 (substring laxo, mismo tipo, plural-canon distinto)."""
    by_key: dict[tuple, list[dict]] = defaultdict(list)
    for n in nodes:
        norm = _norm(n["label"])
        pc = _plural_canon(norm)
        if n["type"] == "EntidadFinanciera":
            cat = (n.get("properties") or {}).get("categoria")
            key = (n["type"], pc, cat)
        else:
            key = (n["type"], pc, None)
        by_key[key].append(n)

    keys = list(by_key.keys())
    pairs: list[dict] = []
    for i in range(len(keys)):
        ti, pi, _ = keys[i]
        for j in range(i + 1, len(keys)):
            tj, pj, _ = keys[j]
            if ti != tj:
                continue
            if pi == pj:
                continue
            if (pi in pj and len(pi) >= 5 and len(pj) <= len(pi) + 30) or (
                pj in pi and len(pj) >= 5 and len(pi) <= len(pj) + 30
            ):
                lbl_i = by_key[keys[i]][0]["label"]
                lbl_j = by_key[keys[j]][0]["label"]
                pairs.append({
                    "type": ti,
                    "label_a": lbl_i,
                    "label_b": lbl_j,
                })
    return pairs


def main() -> None:
    kg = json.loads(KG_PATH.read_text(encoding="utf-8"))
    nodes = kg["nodes"]
    pairs = find_suspect_pairs(nodes)
    print(f"Parejas sospechosas reproducidas: {len(pairs)}")
    print()

    # Clasificar
    total_counts: Counter = Counter()
    by_type_counts: dict[str, Counter] = defaultdict(Counter)
    samples: dict[str, list[tuple[str, str, str]]] = defaultdict(list)  # category → [(type, a, b)]

    for p in pairs:
        cat = classify_pair(p["label_a"], p["label_b"])
        # Agrupar sub-categorías de norm_eq en una categoría "norm_equivalent"
        if cat.startswith("norm_eq"):
            main_cat = "norm_equivalent"
        else:
            main_cat = cat
        total_counts[main_cat] += 1
        # Sub-categoría se cuenta solo si es distinta del main (evita doble conteo)
        if cat != main_cat:
            total_counts[cat] += 1
        by_type_counts[p["type"]][main_cat] += 1
        if len(samples[cat]) < 6:
            samples[cat].append((p["type"], p["label_a"], p["label_b"]))

    # Reporte
    print("=" * 72)
    print("Lente 5 cuantificada — clasificación de parejas sospechosas")
    print("=" * 72)
    print()
    print(f"  {'categoría':<32} {'parejas':>8}  {'%':>6}")
    total = sum(total_counts[c] for c in ("substring_strict", "norm_equivalent", "ambiguous"))
    for c in ("substring_strict", "norm_equivalent", "ambiguous"):
        n = total_counts[c]
        print(f"  {c:<32} {n:>8}  {100*n/max(1,total):>5.1f}%")
    print(f"  {'TOTAL':<32} {total:>8}")
    print()
    print("  desglose interno de norm_equivalent:")
    for sub in ("norm_eq_paren", "norm_eq_abbrev", "norm_eq_plural"):
        n = total_counts[sub]
        print(f"    {sub:<30} {n:>8}")
    print()

    # Tabla por tipo
    print(f"  Por tipo de nodo:")
    print(f"  {'tipo':<28} {'strict':>8} {'norm_eq':>8} {'ambig':>8} {'total':>8}")
    types_sorted = sorted(by_type_counts.keys(), key=lambda t: -sum(by_type_counts[t].values()))
    for t in types_sorted:
        c = by_type_counts[t]
        ts = c["substring_strict"]
        ne = c["norm_equivalent"]
        am = c["ambiguous"]
        marker = "[CORE]" if t in CORE_TYPES else "      "
        print(f"  {marker} {t:<21} {ts:>8} {ne:>8} {am:>8} {ts+ne+am:>8}")
    print()

    print("=" * 72)
    print("Ejemplos por categoría")
    print("=" * 72)
    for cat in ("substring_strict", "norm_eq_paren", "norm_eq_abbrev", "norm_eq_plural", "ambiguous"):
        print(f"\n[{cat}]")
        for t, a, b in samples[cat][:5]:
            print(f"  [{t}]  {a!r}  ↔  {b!r}")


if __name__ == "__main__":
    main()
