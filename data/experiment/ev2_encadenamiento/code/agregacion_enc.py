"""
agregacion_enc.py — Agregación por PAR (pregunta, grafo) de las N=3 re-corridas
del agente, en código, según protocolo §3 (docs/protocolo_corrida_ev2.md):

  "Agregación de las 3 re-corridas: mayoría; un empate triple
   correcto/parcial/incorrecto resuelve a parcial (mediana categórica sobre el
   orden incorrecto < parcial < correcto)."

Entrada: los 3 veredictos por pregunta (mapping §2 del juez, uno por
re-corrida juzgada). La corrida base es DISPARADOR: no vota.

Dominio de cada voto: correcto / parcial / incorrecto — más
`requiere_adjudicacion`, que el mapping §2 emite cuando algún criterio quedó
`dudoso` o `sin_consenso` (el veredicto lo pone la adjudicación humana, no el
mapping). El protocolo §3 no contempla ese cuarto valor; regla de ESTA unidad
(declarada, sujeta a laudo de la mesa antes de usarse sobre datos reales):
  - si los 3 votos están en {correcto, parcial, incorrecto}: mayoría (≥2), y
    empate triple → parcial (mediana categórica);
  - si algún voto es requiere_adjudicacion: el par queda DECIDIDO solo si el
    resultado es INVARIANTE a cómo se resuelva cada voto pendiente (p. ej.
    correcto/correcto/req_adj → correcto: ya hay mayoría); si el resultado
    depende de la adjudicación pendiente, el par queda
    `requiere_adjudicacion` (se persiste la distribución completa).
Ninguna otra regla; ninguna discreción.

Auditoría simétrica (§3): tasa de flip descendente = pares auditados cuyo
agregado de las 3 re-corridas es parcial/incorrecto (base: correcto); se
reporta además el detalle por re-corrida individual.
"""

from __future__ import annotations

from collections import Counter
from itertools import product

RESUELTOS = ("incorrecto", "parcial", "correcto")          # orden de la mediana categórica
PENDIENTE = "requiere_adjudicacion"
VOTOS_VALIDOS = RESUELTOS + (PENDIENTE,)
N_REPS = 3


def _mayoria_o_mediana(votos: list[str]) -> str:
    """Los 3 votos resueltos. Mayoría estricta (> N/2) o mediana categórica
    (con 3 categorías distintas y N=3, la mediana es siempre 'parcial')."""
    valor, n = Counter(votos).most_common(1)[0]
    if n > len(votos) / 2:
        return valor
    ordenados = sorted(votos, key=RESUELTOS.index)
    return ordenados[len(ordenados) // 2]


def agregar_par(votos: list[str]) -> str:
    """Veredicto final del par a partir de los veredictos por pregunta de las 3
    re-corridas juzgadas. Ver docstring del módulo."""
    if len(votos) != N_REPS:
        raise ValueError(f"se esperaban {N_REPS} votos, llegaron {len(votos)}")
    for v in votos:
        if v not in VOTOS_VALIDOS:
            raise ValueError(f"voto inválido: {v!r}")
    pend = [i for i, v in enumerate(votos) if v == PENDIENTE]
    if not pend:
        return _mayoria_o_mediana(list(votos))
    resultados = set()
    for combo in product(RESUELTOS, repeat=len(pend)):
        vs = list(votos)
        for i, r in zip(pend, combo):
            vs[i] = r
        resultados.add(_mayoria_o_mediana(vs))
    return resultados.pop() if len(resultados) == 1 else PENDIENTE


def detalle_par(votos: list[str]) -> dict:
    """Agregado + cómo se llegó (para el reporte): distribución, unanimidad,
    vía (mayoria / mediana_empate_triple / invariante_con_pendiente /
    pendiente_de_adjudicacion)."""
    final = agregar_par(votos)
    c = Counter(votos)
    if PENDIENTE in c:
        via = "invariante_con_pendiente" if final != PENDIENTE else "pendiente_de_adjudicacion"
    elif c.most_common(1)[0][1] > N_REPS / 2:
        via = "unanime" if c.most_common(1)[0][1] == N_REPS else "mayoria_2_de_3"
    else:
        via = "mediana_empate_triple"
    return {"votos": list(votos), "distribucion": dict(c), "final": final, "via": via,
            "unanime": len(c) == 1}


def flip_descendente(veredicto_base: str, final: str) -> str | None:
    """Auditoría §3 (base 'correcto'): 'flip' si el agregado bajó a
    parcial/incorrecto; 'sin_flip' si sigue correcto; 'pendiente' si el
    agregado requiere adjudicación. None si la base no era correcto."""
    if veredicto_base != "correcto":
        return None
    if final == "correcto":
        return "sin_flip"
    if final == PENDIENTE:
        return "pendiente"
    return "flip"
