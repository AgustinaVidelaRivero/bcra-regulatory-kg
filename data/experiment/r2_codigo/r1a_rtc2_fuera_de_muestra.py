"""U-R2-CODIGO, R1.a — chequeo informativo de R-TC2 fuera de la muestra.

R-TC2 (detección propia de tablas de dos filas, correr_e0.py, sección
«tablas en E0, versión e0-r2») se definió mirando los diez TOs de la tanda 0. Este
script la aplica, con la misma regla, a los PDFs del corpus escalado que no
son de la tanda 0 (`data/experiment/escalado_prep/pdfs/`), con un tope de
páginas por TO, y lista cada detección con sus celdas para leerla.
Informativo: no es parte de la condición de aceptación. USD 0.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \\
    data/experiment/r2_codigo/r1a_rtc2_fuera_de_muestra.py --max-paginas 300 \\
    --out data/experiment/r2_codigo/r1a_rtc2_fuera_de_muestra.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pdfplumber

REPO = Path(__file__).resolve().parents[3]
E0DIR = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking"
PDFS = REPO / "data" / "experiment" / "escalado_prep" / "pdfs"
sys.path.insert(0, str(E0DIR))
import correr_e0 as C  # noqa: E402

TANDA0_NUEVOS = ("ctacte", "docvig", "lingob", "pagjub", "polcre")

# Lectura de cada detección (criterio de r1a_deteccion_tablas.py: verdadero
# positivo = tabla de contenido con una fila de rótulos y una de valores).
LECTURA = {
    ("ceninf", 4): "verdadero positivo: diseño de registro (campo, nombre, tipo, longitud, observaciones)",
    ("snp_spd", 20): "verdadero positivo: tasas de intercambio máximas con sus valores",
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-paginas", type=int, required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    omitidos, detecciones, procesados = [], [], []
    for pdf in sorted(PDFS.glob("*.pdf")):
        to = pdf.stem
        if to in TANDA0_NUEVOS:
            continue
        with pdfplumber.open(str(pdf)) as d:
            n = len(d.pages)
        if n > a.max_paginas:
            omitidos.append({"to": to, "paginas": n})
            continue
        procesados.append(to)
        for t in C.detectar_tablas_dos_filas(pdf, to):
            s = t["segmentos"][0]
            detecciones.append({"to": to, "tabla": t["id"], "pagina": s["pagina"],
                                "estado": t["estado"], "filas": s["filas"],
                                "lectura": LECTURA.get((to, s["pagina"]), "SIN LECTURA")})
    out = {"unidad": "U-R2-CODIGO", "etapa": "R1.a", "informativo": True,
           "max_paginas": a.max_paginas, "tos_procesados": len(procesados),
           "tos_omitidos_por_tamano": omitidos, "detecciones": detecciones,
           "falsos_positivos": sum(1 for x in detecciones
                                   if not x["lectura"].startswith("verdadero"))}
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                           encoding="utf-8")


if __name__ == "__main__":
    main()
