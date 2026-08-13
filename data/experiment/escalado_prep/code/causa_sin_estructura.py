"""Causa raíz de los TOs en los que E0 no engancha estructura (H2).

Se corre solo sobre los TOs con 0 secciones o 0 chunks terminales, y separa
tres mecanismos distintos, que exigen reglas distintas:

  A. sin páginas de cuerpo — `clasificar_paginas` marca como `portada` todo lo
     anterior a la primera página con la marca '-Índice-'. Si el TO no publica
     esa marca, ninguna página llega a rol `cuerpo` y el parser no ve nada.
  B. con cuerpo pero sin aparato de secciones — el TO no usa el encabezado
     'Sección N. …' sobre el que E0 ancla toda la jerarquía.
  C. con cuerpo y secciones pero sin puntos numerados x.y — el TO es prosa o
     tablas sin numeración jerárquica.

Salida: ../causa_sin_estructura.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import correr_e0_seco as D  # noqa: E402

E0 = D.E0
PREP = D.PREP


def main() -> None:
    conteos = json.loads((PREP / "e0_dry" / "conteos_e0_dry.json").read_text(encoding="utf-8"))
    objetivo = [i for i, c in conteos.items()
                if c["secciones"] < 1 or c["chunks_terminales"] < 1]

    out = {}
    for ident in sorted(objetivo):
        pdf = PREP / "pdfs" / f"{ident}.pdf"
        paginas = E0.extraer_lineas(pdf)
        roles = E0.clasificar_paginas(paginas)
        textos = [l.texto.strip() for pag in paginas for l in pag]

        n_marca_indice = sum(1 for t in textos if E0.RE_MARCA_INDICE.match(t))
        n_seccion = sum(1 for t in textos if E0.RE_SECCION.match(t))
        n_seccion_en_linea = sum(1 for t in textos if E0.RE_SECCION_EN_LINEA.search(t))
        n_lineas = len(textos)
        n_cuerpo = sum(1 for r in roles if r == "cuerpo")

        if n_lineas == 0:
            causa = "D. PDF sin capa de texto extraíble por pdfplumber"
        elif n_cuerpo == 0:
            causa = ("A. ninguna página alcanza rol 'cuerpo': "
                     + ("no hay marca '-Índice-' que abra el cuerpo"
                        if n_marca_indice == 0 else
                        "hay marca de índice pero el resto cae en otro rol"))
        elif n_seccion == 0 and n_seccion_en_linea == 0:
            causa = "B. hay cuerpo pero el TO no usa el encabezado 'Sección N. …'"
        elif conteos[ident]["secciones"] > 0:
            causa = "C. hay secciones pero ningún punto numerado x.y en el cuerpo"
        else:
            causa = ("B'. hay líneas 'Sección N.' pero no en posición de encabezado "
                     "de página (el parser las toma como contenido)")

        out[ident] = {
            "paginas": len(paginas),
            "lineas_totales": n_lineas,
            "roles_pagina": {r: roles.count(r) for r in sorted(set(roles))},
            "lineas_marca_indice": n_marca_indice,
            "lineas_seccion_encabezado": n_seccion,
            "lineas_seccion_en_cualquier_posicion": n_seccion_en_linea,
            "secciones_parseadas": conteos[ident]["secciones"],
            "chunks_terminales": conteos[ident]["chunks_terminales"],
            "causa": causa,
            "primeras_lineas": textos[:6],
        }
        print(f"{ident:16s} {causa}")

    (PREP / "causa_sin_estructura.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nTOs sin estructura: {len(out)}")


if __name__ == "__main__":
    main()
