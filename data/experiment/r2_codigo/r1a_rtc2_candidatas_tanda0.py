"""U-R2-CODIGO, R1.a — candidatas de R-TC2 en los diez TOs de la tanda 0.

Lista toda tabla de `find_tables()` que R-TC descarta solo por `min_filas`,
con exactamente 2 filas y que pasaría R-TC con 3 (zonas y columnas), y dice
si pasa la guarda numérica de R-TC2 (segunda fila con al menos
MIN_CELDAS_NUMERICAS_FILA2 celdas numéricas). Las que no la pasan son lo que
R-TC2 deja afuera a propósito (banners) o por alcance (tablas de una fila de
datos sin cifras, filas colapsadas). USD 0.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \\
    data/experiment/r2_codigo/r1a_rtc2_candidatas_tanda0.py \\
    --out data/experiment/r2_codigo/r1a_rtc2_candidatas_tanda0.json
"""

from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

import pdfplumber

REPO = Path(__file__).resolve().parents[3]
E0DIR = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking"
MANIFIESTO = REPO / "data" / "experiment" / "reextraccion_v2" / "manifiestos" / "tanda0_10tos.json"
sys.path.insert(0, str(E0DIR))
import correr_e0 as C  # noqa: E402
import e0_tablas as e0t  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    man = json.loads(MANIFIESTO.read_text(encoding="utf-8"))
    candidatas = []
    for t in sorted(man["tos"], key=lambda x: x["id"]):
        with pdfplumber.open(str(REPO / t["pdf"])) as pdf:
            for pi, page in enumerate(pdf.pages, start=1):
                alto = float(page.height)
                for ti, tb in enumerate(page.find_tables()):
                    filas = tb.extract()
                    n_f = len(filas)
                    n_c = max((len(f) for f in filas), default=0)
                    es, motivo = e0t.clasificar_tabla_contenido(n_f, n_c, tb.bbox, alto)
                    if es or motivo != "min_filas" or n_f != 2:
                        continue
                    pasaria, _ = e0t.clasificar_tabla_contenido(e0t.MIN_FILAS_TC, n_c, tb.bbox, alto)
                    if not pasaria:
                        continue
                    num = sum(1 for c in filas[1] if e0t._es_numerica(c))
                    candidatas.append({
                        "to": t["id"], "pagina": pi, "indice_en_pagina": ti,
                        "n_cols": n_c, "celdas_numericas_fila2": num,
                        "pasa_guarda": num >= C.MIN_CELDAS_NUMERICAS_FILA2,
                        "primera_celda": (filas[0][0] or "") if filas[0] else "",
                        "filas": filas if (filas[0][0] or "") != "B.C.R.A." else None})
    excluidas = [c for c in candidatas if not c["pasa_guarda"]]
    out = {
        "unidad": "U-R2-CODIGO", "etapa": "R1.a",
        "candidatas": len(candidatas),
        "pasan_guarda": sum(1 for c in candidatas if c["pasa_guarda"]),
        "excluidas_por_primera_celda": dict(sorted(collections.Counter(
            "B.C.R.A." if c["primera_celda"] == "B.C.R.A." else "otra"
            for c in excluidas).items())),
        "detalle": [c for c in candidatas if c["primera_celda"] != "B.C.R.A."],
    }
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                           encoding="utf-8")


if __name__ == "__main__":
    main()
