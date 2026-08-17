"""
tests_agregacion.py — Tests de respuesta conocida de agregacion_enc.py
(protocolo §3): los cuatro desenlaces sobre votos resueltos (mayoría correcto /
mayoría parcial / mayoría incorrecto / empate triple → parcial), unanimidad,
la regla declarada para votos requiere_adjudicacion (invariante vs pendiente),
la tasa de flip de la auditoría y los rechazos de entrada inválida. Offline.

Correr:  .venv/bin/python -B data/experiment/ev2_encadenamiento/code/tests_agregacion.py
"""

from __future__ import annotations

import sys
from itertools import permutations, product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from agregacion_enc import (PENDIENTE, RESUELTOS, agregar_par, detalle_par,   # noqa: E402
                            flip_descendente)

CHECKS: list[tuple[str, bool]] = []


def check(nombre: str, cond: bool) -> None:
    CHECKS.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")


def espera_error(fn, *args) -> bool:
    try:
        fn(*args)
        return False
    except ValueError:
        return True


def main() -> int:
    print("== 4 desenlaces sobre votos resueltos ==")
    check("mayoría correcto (2-1)", agregar_par(["correcto", "parcial", "correcto"]) == "correcto")
    check("mayoría parcial (2-1)", agregar_par(["parcial", "incorrecto", "parcial"]) == "parcial")
    check("mayoría incorrecto (2-1)", agregar_par(["incorrecto", "incorrecto", "correcto"]) == "incorrecto")
    check("empate triple → parcial (mediana categórica)",
          agregar_par(["correcto", "parcial", "incorrecto"]) == "parcial")
    check("empate triple → parcial en TODAS las permutaciones",
          all(agregar_par(list(p)) == "parcial" for p in permutations(RESUELTOS)))
    check("unánime correcto / parcial / incorrecto",
          all(agregar_par([v] * 3) == v for v in RESUELTOS))
    check("mayoría 2-de-3 en toda posición (correcto vs incorrecto)",
          all(agregar_par(vs) == "correcto" for vs in (["correcto", "correcto", "incorrecto"],
                                                       ["correcto", "incorrecto", "correcto"],
                                                       ["incorrecto", "correcto", "correcto"])))
    # exhaustivo: las 27 combinaciones de votos resueltos
    ok = True
    for vs in product(RESUELTOS, repeat=3):
        from collections import Counter
        c = Counter(vs)
        esperado = c.most_common(1)[0][0] if c.most_common(1)[0][1] >= 2 else "parcial"
        ok &= agregar_par(list(vs)) == esperado
    check("27/27 combinaciones resueltas: mayoría o parcial", ok)

    print("== votos requiere_adjudicacion (regla declarada) ==")
    check("correcto/correcto/req_adj → correcto (invariante: ya hay mayoría)",
          agregar_par(["correcto", "correcto", PENDIENTE]) == "correcto")
    check("incorrecto/req_adj/incorrecto → incorrecto (invariante)",
          agregar_par(["incorrecto", PENDIENTE, "incorrecto"]) == "incorrecto")
    check("parcial/parcial/req_adj → parcial", agregar_par(["parcial", "parcial", PENDIENTE]) == "parcial")
    check("correcto/incorrecto/req_adj → PENDIENTE (depende de la adjudicación)",
          agregar_par(["correcto", "incorrecto", PENDIENTE]) == PENDIENTE)
    check("correcto/parcial/req_adj → PENDIENTE (correcto si adj=correcto; parcial si no)",
          agregar_par(["correcto", "parcial", PENDIENTE]) == PENDIENTE)
    check("parcial/incorrecto/req_adj → PENDIENTE",
          agregar_par(["parcial", "incorrecto", PENDIENTE]) == PENDIENTE)
    check("correcto/req_adj/req_adj → PENDIENTE", agregar_par(["correcto", PENDIENTE, PENDIENTE]) == PENDIENTE)
    check("req_adj ×3 → PENDIENTE", agregar_par([PENDIENTE] * 3) == PENDIENTE)
    check("con pendientes: decidido ⇔ invariante (chequeo exhaustivo de 37 combinaciones)",
          all((agregar_par(list(vs)) != PENDIENTE) ==
              (len({agregar_par([r if v == PENDIENTE else v for v, r in zip(vs, combo)])
                    for combo in product(RESUELTOS, repeat=3)}) == 1)
              for vs in product(RESUELTOS + (PENDIENTE,), repeat=3) if PENDIENTE in vs))

    print("== detalle_par (vías) ==")
    check("vía unanime", detalle_par(["parcial"] * 3)["via"] == "unanime")
    check("vía mayoria_2_de_3", detalle_par(["correcto", "parcial", "correcto"])["via"] == "mayoria_2_de_3")
    check("vía mediana_empate_triple", detalle_par(["correcto", "parcial", "incorrecto"])["via"] == "mediana_empate_triple")
    check("vía invariante_con_pendiente", detalle_par(["correcto", "correcto", PENDIENTE])["via"] == "invariante_con_pendiente")
    check("vía pendiente_de_adjudicacion", detalle_par(["correcto", "incorrecto", PENDIENTE])["via"] == "pendiente_de_adjudicacion")
    check("detalle conserva distribución completa",
          detalle_par(["correcto", "parcial", "correcto"])["distribucion"] == {"correcto": 2, "parcial": 1})

    print("== flip descendente (auditoría) ==")
    check("correcto → correcto: sin_flip", flip_descendente("correcto", "correcto") == "sin_flip")
    check("correcto → parcial: flip", flip_descendente("correcto", "parcial") == "flip")
    check("correcto → incorrecto: flip", flip_descendente("correcto", "incorrecto") == "flip")
    check("correcto → req_adj: pendiente", flip_descendente("correcto", PENDIENTE) == "pendiente")
    check("base no-correcto: None (no aplica)", flip_descendente("parcial", "correcto") is None)

    print("== entradas inválidas ==")
    check("2 votos → ValueError", espera_error(agregar_par, ["correcto", "parcial"]))
    check("4 votos → ValueError", espera_error(agregar_par, ["correcto"] * 4))
    check("voto fuera de dominio → ValueError", espera_error(agregar_par, ["correcto", "dudoso", "parcial"]))
    check("voto vacío → ValueError", espera_error(agregar_par, ["correcto", "", "parcial"]))

    fallos = [n for n, ok in CHECKS if not ok]
    print(f"\nRESULTADO: {'PASS' if not fallos else 'FAIL'} ({len(CHECKS) - len(fallos)}/{len(CHECKS)} checks)")
    return 0 if not fallos else 1


if __name__ == "__main__":
    raise SystemExit(main())
