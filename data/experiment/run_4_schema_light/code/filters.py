"""
Filtros post-extracción meta-textuales.

Máximo 8 patrones (decisión de diseño con la autora).
Si necesitamos más, iteramos el SYSTEM_PROMPT en lugar de filtrar post-hoc.

Estos patrones buscan eliminar entities cuyo `name` es claramente una
auto-referencia documental que el modelo, a pesar del SYSTEM_PROMPT,
pudo haber extraído.
"""

import re
from typing import Iterable

# 8 patrones máximos. Lowercase + sin acentos para matchear el name normalizado.
# Cada patrón es una regex que se aplica sobre el name normalizado superficialmente.
META_TEXTUAL_PATTERNS = [
    r"^(el|la|los|las)\s+(presente|presentes)\b",        # "el presente texto", "la presente reglamentación"
    r"^(este|esta|estos|estas)\s+(punto|inciso|articulo|capitulo|seccion|anexo|cuadro|parrafo)\b",
    r"^(lo|la)\s+(dispuesto|establecido|previsto|indicado|señalado)\b",
    r"^nota\s+al\s+pie\b",
    r"^(el|la)\s+(siguiente|anterior)\s+(cuadro|tabla|parrafo|punto|inciso)\b",
    r"^(punto|inciso|articulo|capitulo|seccion|anexo|comunicaci[oó]n|texto\s+ordenado)\s+[a-z0-9\.\-]+",  # "Punto 3.16.3.4"
    r"^(parrafo|sub.?parrafo)\s+\w+",
    r"^(el|la|los|las)\s+(mismo|mismos|misma|mismas|cita[do]s?)\b",
]

_COMPILED = [re.compile(p, re.IGNORECASE) for p in META_TEXTUAL_PATTERNS]


def normalize_for_filter(s: str) -> str:
    """Lowercase + strip acentos para matchear contra patrones."""
    import unicodedata
    s = s.lower().strip()
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    # colapsar whitespace
    s = re.sub(r"\s+", " ", s)
    return s


def is_meta_textual(name: str) -> bool:
    """True si el name matchea cualquiera de los 8 patrones meta-textuales."""
    n = normalize_for_filter(name)
    return any(p.search(n) for p in _COMPILED)


def filter_entities(entities: Iterable[dict]) -> tuple[list[dict], list[dict]]:
    """
    Separa entities en (kept, dropped).
    `dropped` es para reportar cuántas se filtraron y por qué.
    """
    kept, dropped = [], []
    for e in entities:
        if is_meta_textual(e.get("name", "")):
            dropped.append(e)
        else:
            kept.append(e)
    return kept, dropped


if __name__ == "__main__":
    # Smoke test del filtro
    tests = [
        "El presente texto",
        "BCRA",
        "Punto 3.16.3.4",
        "Banco comercial privado",
        "La presente reglamentación",
        "Comunicación A 7259",
        "Nota al pie",
        "Entidad financiera de Grupo A",
        "El siguiente cuadro",
        "Lo dispuesto en el párrafo anterior",
        "Anexo I",
    ]
    for t in tests:
        print(f"{'DROP' if is_meta_textual(t) else 'KEEP'}  {t}")
