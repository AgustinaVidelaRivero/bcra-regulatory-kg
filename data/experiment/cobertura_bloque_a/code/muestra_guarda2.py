"""Guarda 2 — muestra para el cotejo A MANO contra el esquema congelado.

REGLA DE SELECCIÓN (fija, declarada ANTES de mirar el contenido, para que la
muestra no se elija a conveniencia):

  Un bloque por cada uno de los DIEZ documentos = el PRIMER bloque de ≥150
  caracteres de la PRIMERA página cuya clase de forma sea `prosa` o `mixta`.
  Si el documento no tiene ninguna página de esas clases, o ninguna alcanza
  los 150 caracteres, se declara SIN MUESTRA y se dice por qué.

La regla cubre los diez documentos (cobertura completa por construcción),
toma el material en su forma más favorable al esquema (prosa) y no permite
elegir el pasaje: es el primero que cumple el largo mínimo.

Uso:  python3 muestra_guarda2.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402
import censo_forma as CF  # noqa: E402
from e0_lib import separar_encabezado_pie  # noqa: E402

LARGO_MIN = 150


def seleccionar(to: str) -> dict:
    paginas, roles, modal, bloques, _d = C.leer_documento(to)
    for i, (lineas, rol) in enumerate(zip(paginas, roles), start=1):
        if rol != C.E0.ROL_CUERPO:
            continue
        contenido, _x, _y = separar_encabezado_pie(lineas)
        cl = CF.clase_forma(CF.densidad_prosa(contenido))
        if cl not in ("prosa", "mixta"):
            continue
        for b in bloques[i]:
            if b.n_chars >= LARGO_MIN:
                return {"to": to, "pagina": b.pagina, "offset": b.offset,
                        "clase_forma_pagina": cl, "n_lineas": b.n_lineas,
                        "n_chars": b.n_chars, "texto": b.texto}
        return {"to": to, "sin_muestra": True,
                "motivo": f"primera pagina {cl} (p.{i}) sin bloque de "
                          f">={LARGO_MIN} caracteres"}
    return {"to": to, "sin_muestra": True,
            "motivo": "ninguna pagina de clase prosa o mixta"}


def main() -> int:
    sel = [seleccionar(to) for to in C.DIEZ]
    salida = C.UNIDAD / "guarda2_muestra.json"
    salida.write_text(json.dumps(
        {"_regla_seleccion": (
            "primer bloque de >=%d caracteres de la primera pagina de clase "
            "prosa o mixta, uno por documento; regla fijada antes de mirar el "
            "contenido" % LARGO_MIN),
         "largo_min": LARGO_MIN,
         "muestras": sel}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for m in sel:
        if m.get("sin_muestra"):
            print(f"--- {m['to']}: SIN MUESTRA — {m['motivo']}")
        else:
            print(f"--- {m['to']} p.{m['pagina']} off.{m['offset']} "
                  f"({m['clase_forma_pagina']}, {m['n_chars']} car.)")
            print(m["texto"])
        print()
    print(f"escrito: {salida.relative_to(C.REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
