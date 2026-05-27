"""
Utilidades de normalización superficial.

Estrategia schema-light puro:
- slug_label: para identificar entidades por nombre. Lowercase + strip acentos + snake_case.
  Sin heurística de plurales (decisión del usuario): "banco" y "bancos" son slugs distintos.
- slug_type: idéntica función, aplicada a tipos.
- slug_predicate: idéntica función, aplicada a predicados.

El backstop estructural matchea sobre el slug_type normalizado.
"""

import re
import unicodedata


def _surface_normalize(s: str) -> str:
    s = s.lower().strip()
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = s.strip("_")
    return s


slug_label = _surface_normalize
slug_type = _surface_normalize
slug_predicate = _surface_normalize


# Patrones del backstop estructural (decisión del usuario en preassembly checkpoint)
BACKSTOP_PATTERNS = [
    re.compile(r"^comunicacion_(a|b)"),
    re.compile(r"^ley(_nacional)?$"),
    re.compile(r"^decreto"),
    re.compile(r"^resolucion"),
    re.compile(r"^circular"),
]


def matches_backstop(normalized_type: str) -> bool:
    """True si el tipo normalizado matchea alguno de los 5 patrones del backstop."""
    return any(p.search(normalized_type) for p in BACKSTOP_PATTERNS)


if __name__ == "__main__":
    tests = [
        ("BCRA", "bcra"),
        ("Banco Central de la República Argentina", "banco_central_de_la_republica_argentina"),
        ("Sujeto Obligado", "sujeto_obligado"),
        ("Comunicación A 1234", "comunicacion_a_1234"),
        ("Categoría especial", "categoria_especial"),
        ("Persona humana ó jurídica", "persona_humana_o_juridica"),
    ]
    for inp, expected in tests:
        got = slug_label(inp)
        ok = "OK" if got == expected else "FAIL"
        print(f"{ok}  {inp!r:<55} -> {got!r:<55} (expected {expected!r})")

    backstop_tests = [
        ("Comunicación A 1234", True),
        ("Comunicación BCRA", False),  # no matchea ^comunicacion_(a|b)\b porque va a ser 'comunicacion_bcra'
        ("Ley", True),
        ("Ley Nacional", True),
        ("Ley 24.240", False),  # matchea ^ley_? Sí. Veamos
        ("Decreto 1234", True),
        ("Resolución BCRA", True),
        ("Circular OPRAC", True),
        ("Sujeto regulado", False),
    ]
    print("\nBackstop:")
    for inp, expected in backstop_tests:
        norm = slug_type(inp)
        got = matches_backstop(norm)
        ok = "OK" if got == expected else "WARN"
        print(f"{ok}  {inp!r:<35} -> {norm!r:<35} matches={got} (expected {expected})")
