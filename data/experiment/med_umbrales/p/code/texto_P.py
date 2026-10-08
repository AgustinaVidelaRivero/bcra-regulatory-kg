"""
texto_P.py — U-MED-UMBRALES, etapa P, tramo P-a: cláusula de un elemento y resaltado de su cuantía, sobre el texto
completo de la unidad de E0 (propio y heredado, unidos por salto: validador_r2.texto_completo, validador_r2.py:232-235).

Va aparte de comun_P.py para no cambiar ese módulo después del sello del acta (su sha256 está en acta_sorteo_P.json).
comun_P.clausula queda sin uso: la regla vigente es la de este módulo.

Regla de corte de la cláusula (mandato P-a, punto 5, declarada acá):
  - punto y coma;
  - punto seguido de espacio y de una mayúscula, de un número de punto («3.7.») o del fin del texto;
  - salto de línea solo si abre un ítem («i)», «a)», «1.», «2.3.1.», guion o viñeta), si el renglón anterior termina en
    dos puntos, o si es la unión entre el texto propio y un bloque heredado (o entre dos bloques heredados).
  El texto de E0 conserva los cortes de renglón del PDF («refinancia-» + salto): un salto de línea cualquiera no corta,
  porque partiría la oración en renglones y dejaría fuera marcadores del renglón anterior.
"""
from __future__ import annotations

import re

_RE_PUNTO = re.compile(r"\.(?=\s+(?:[A-ZÁÉÍÓÚÑ¿«(\"]|\d+\.\d)|\s*$)")
_RE_ITEM = re.compile(r"\n[ \t]*(?:[ivxlcIVXLC]+\)|[a-zñA-ZÑ]\)|\d+(?:\.\d+)*\.(?:\s|$)|\d+\)|[-–—•·]\s)")


def uniones(chunk: dict) -> list[int]:
    """Posiciones, en el texto completo, de los saltos que unen el texto propio y los bloques heredados."""
    out, pos = [], len(chunk.get("texto") or "")
    for h in chunk.get("herencia") or []:
        out.append(pos)
        pos += 1 + len(h.get("texto") or "")
    return out


def cortes(texto: str, duros: list[int]) -> list[tuple[int, int]]:
    """Cortes (inicio, fin) del separador: la cláusula empieza en fin y termina en inicio."""
    cs = [(m.start(), m.end()) for m in re.finditer(";", texto)]
    cs += [(m.start(), m.end()) for m in _RE_PUNTO.finditer(texto)]
    cs += [(m.start(), m.start() + 1) for m in _RE_ITEM.finditer(texto)]
    cs += [(m.start(), m.start() + 1) for m in re.finditer(r":[ \t]*\n", texto)]
    cs += [(p, p + 1) for p in duros]
    return sorted(set(cs))


def clausula(texto: str, ini: int, fin: int, duros: list[int]) -> tuple[int, int]:
    a, b = 0, len(texto)
    for x, y in cortes(texto, duros):
        if y <= ini:
            a = y
        elif x >= fin:
            b = x + (1 if texto[x] == "." else 0)
            break
    return a, b


def para_mostrar(s: str) -> str:
    """Une los cortes de renglón con guion y los saltos, para mostrar la cláusula en una línea."""
    return " ".join(re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", s).split())


def ajustar_cuantia(texto: str, span: tuple[int, int], cuantia: str, plegar) -> tuple[int, int]:
    """El span por tokens de R-NORM deja fuera los signos («%», «$»); si el literal de la cuantía (sin distinguir
    mayúsculas, tildes ni espacios) empieza en el mismo lugar, se usa su span completo."""
    toks = re.findall(r"\S+", plegar(cuantia))
    if not toks:
        return span
    pat = re.compile(r"\s*".join(re.escape(t) for t in toks))
    p = plegar(texto)
    for m in pat.finditer(p, max(0, span[0] - 3), min(len(p), span[1] + 3 + len(cuantia))):
        if abs(m.start() - span[0]) <= 3 and m.end() >= span[1]:
            return m.start(), m.end()
    return span
