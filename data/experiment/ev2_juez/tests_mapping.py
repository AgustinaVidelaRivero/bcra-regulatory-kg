"""
tests_mapping.py — Tests de respuesta conocida del mapping (§2 y §4 del
pre-registro). Cubren los cuatro casos del mapping por pregunta, la agregación
modal con sus tres desenlaces (unánime, mayoría 2-de-3, sin consenso) y la
precedencia de la regla de adjudicación. Offline, sin API.

Correr:  .venv/bin/python data/experiment/ev2_juez/tests_mapping.py
"""

from __future__ import annotations

import sys

from mapping import veredicto_modal, veredicto_pregunta

CHECKS: list[tuple[str, bool]] = []


def check(nombre: str, cond: bool) -> None:
    CHECKS.append((nombre, cond))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")


def espera_error(fn, *args) -> bool:
    try:
        fn(*args)
        return False
    except ValueError:
        return True


def main() -> int:
    print("== veredicto_modal (§4) ==")
    check("unánime cumplido", veredicto_modal(["cumplido"] * 3) == "cumplido")
    check("unánime no_cumplido", veredicto_modal(["no_cumplido"] * 3) == "no_cumplido")
    check("unánime dudoso", veredicto_modal(["dudoso"] * 3) == "dudoso")
    check("mayoría 2-1 cumplido",
          veredicto_modal(["cumplido", "no_cumplido", "cumplido"]) == "cumplido")
    check("mayoría 2-1 dudoso",
          veredicto_modal(["dudoso", "dudoso", "cumplido"]) == "dudoso")
    check("tres distintos → sin_consenso",
          veredicto_modal(["cumplido", "no_cumplido", "dudoso"]) == "sin_consenso")
    check("veredicto inválido rechazado", espera_error(veredicto_modal, ["cumplida"] * 3))
    check("lista vacía rechazada", espera_error(veredicto_modal, []))

    print("== veredicto_pregunta (§2) — los cuatro casos del mapping ==")
    check("todos cumplido → correcto",
          veredicto_pregunta(["cumplido", "cumplido", "cumplido"]) == "correcto")
    check("cero cumplido → incorrecto",
          veredicto_pregunta(["no_cumplido", "no_cumplido"]) == "incorrecto")
    check("mezcla → parcial",
          veredicto_pregunta(["cumplido", "no_cumplido", "cumplido"]) == "parcial")
    check("un dudoso → requiere_adjudicacion",
          veredicto_pregunta(["cumplido", "dudoso", "cumplido"]) == "requiere_adjudicacion")
    check("un sin_consenso → requiere_adjudicacion",
          veredicto_pregunta(["sin_consenso", "no_cumplido"]) == "requiere_adjudicacion")

    print("== precedencia y bordes ==")
    check("dudoso gana aunque el resto sea todo cumplido",
          veredicto_pregunta(["cumplido", "cumplido", "dudoso"]) == "requiere_adjudicacion")
    check("dudoso gana aunque el resto sea todo no_cumplido",
          veredicto_pregunta(["no_cumplido", "dudoso"]) == "requiere_adjudicacion")
    check("un solo criterio cumplido → correcto", veredicto_pregunta(["cumplido"]) == "correcto")
    check("un solo criterio no_cumplido → incorrecto",
          veredicto_pregunta(["no_cumplido"]) == "incorrecto")
    check("un solo criterio dudoso → requiere_adjudicacion",
          veredicto_pregunta(["dudoso"]) == "requiere_adjudicacion")
    check("modal inválido rechazado", espera_error(veredicto_pregunta, ["quizas"]))
    check("lista vacía rechazada", espera_error(veredicto_pregunta, []))

    fallos = [n for n, ok in CHECKS if not ok]
    print(f"\nRESULTADO: {'PASS ✅' if not fallos else 'FAIL ❌'} "
          f"({len(CHECKS) - len(fallos)}/{len(CHECKS)} checks)")
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.exit(main())
