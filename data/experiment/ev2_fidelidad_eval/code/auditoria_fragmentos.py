"""
auditoria_fragmentos.py — Auditoría mecánica de los fragmentos que el juez señala
como evidencia: null / verbatim / fuga_gold / no_verbatim.

Es la MISMA regla que la calibración validó como detector de la limitación
conocida №1 del instrumento (fuga de gold al fragmento; registro_calibracion.md
§8): `_plano` y `estado_fragmento` se copian VERBATIM de
data/experiment/ev2_juez/analisis_acuerdo.py (allí viven anidadas dentro de
main(), por eso no se importan). El selftest verifica que el texto de ambas
funciones sigue siendo idéntico al del archivo de origen.

  - null       : el juez no señaló fragmento (declara ausencia);
  - verbatim   : el fragmento aparece en la respuesta (comparación
                 case-insensitive, tolerante a markdown y comillas);
  - fuga_gold  : el fragmento NO está en la respuesta pero SÍ en la cita
                 textual del gold → el juez copió evidencia del gold;
  - no_verbatim: el fragmento no está ni en la respuesta ni en la cita
                 (concatenaciones, puntuación alterada, paráfrasis).
"""

from __future__ import annotations

from collections import Counter


def _plano(s: str) -> str:
    # comparación de fragmentos tolerante a marcadores markdown y comillas
    # tipográficas (el juez suele devolver el texto sin ** ni «»); no altera letras
    for ch in ("**", "*", "«", "»", "“", "”", "\"", "'", "‘", "’", "`"):
        s = s.replace(ch, "")
    return " ".join(s.split())


def estado_fragmento(fr, texto_resp, cita_gold):
    """null | verbatim | fuga_gold | no_verbatim (comparación case-insensitive
    tolerante a markdown/comillas; 'fuga_gold' = el fragmento está en la cita
    del gold y NO en la respuesta)."""
    if fr is None:
        return "null"
    f = _plano(fr).lower()
    if f in _plano(texto_resp).lower():
        return "verbatim"
    if f in _plano(cita_gold).lower():
        return "fuga_gold"
    return "no_verbatim"


ESTADOS = ("null", "verbatim", "fuga_gold", "no_verbatim")


def auditar_caso(respuesta: str, criterios: list[dict], criterios_agg: list[dict]) -> dict:
    """Para un caso: estado por (criterio, rep) + conteo. `criterios_agg[i]`
    trae `fragmentos_reps` (lista de N) del criterio i (mismo orden del gold)."""
    conteo = Counter()
    por_criterio = []
    for c, ca in zip(criterios, criterios_agg):
        estados = [estado_fragmento(fr, respuesta, c["cita_textual"])
                   for fr in ca["fragmentos_reps"]]
        conteo.update(estados)
        por_criterio.append(estados)
    return {"por_criterio": por_criterio, "conteo": {e: conteo.get(e, 0) for e in ESTADOS}}
