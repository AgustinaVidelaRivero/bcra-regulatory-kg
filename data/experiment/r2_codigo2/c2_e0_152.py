"""U-R2-CODIGO-2, C2 — e0-r2 de los 152 TOs de la partición con el código de C2 (USD 0, sin API). Escribe solo en
--salida, que tiene que estar fuera del repo (unos 25 minutos).

Es la misma corrida que `c1f_ric44.py --correr-tos todos` (PDFs de escalado_prep, TOs de
segmentacion_84/b584_particion/conteos_b584.json), con el código de la copia. Con --cola-en-toda-pagina, la cola de
título estricta del punto l rige en toda página de todo TO (y no solo en las de COLA_TITULO_ESTRICTA_E0_R2): es la
medición de la regla general que dejó fuera de C2 los cambios de E0 que mueven ids de la partición
(freno_c2.md, punto l).

La salida con el código anterior a C2 (la base de la comparación de `c2_e0.py`) sale de
`c1f_ric44.py --correr-tos todos --variante base --salida <dir>` corrido sobre una copia de 5c58f38.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo2/c2_e0_152.py --salida <dir> \
      [--cola-en-toda-pagina]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parents[3]
for p in (RAIZ / "data" / "experiment" / "reextraccion_v2" / "e0_chunking", RAIZ / "data" / "experiment" / "reextraccion_v2"):
    sys.path.insert(0, str(p))
import correr_e0 as CE  # noqa: E402

PDFS = RAIZ / "data" / "experiment" / "escalado_prep" / "pdfs"
PARTICION = RAIZ / "data" / "experiment" / "segmentacion_84" / "b584_particion"


class ManifiestoMinimo:
    """Lo que `correr_e0.correr` usa de un manifiesto, para TOs de la partición."""
    tiene_oraculo = False
    mapa_territorio = None

    def __init__(self, ids: list[str]):
        self.ids = list(ids)

    def archivo_de(self, t: str) -> str:
        return f"{t}.pdf"

    def pdf_de(self, t: str) -> Path:
        return PDFS / f"{t}.pdf"


class _TodaPagina(frozenset):
    def __contains__(self, x) -> bool:
        return True


class _ColaEnTodaPagina(dict):
    def get(self, k, default=None):
        return _TodaPagina()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--cola-en-toda-pagina", action="store_true")
    a = ap.parse_args()
    if a.salida.resolve().is_relative_to(RAIZ.resolve()):
        raise SystemExit(f"--salida dentro del repo: {a.salida}")
    if a.cola_en_toda_pagina:
        CE.COLA_TITULO_ESTRICTA_E0_R2 = _ColaEnTodaPagina()
    c = json.loads((PARTICION / "conteos_b584.json").read_text(encoding="utf-8"))
    tos = sorted(t for t, v in c.items() if isinstance(v, dict))
    CE.correr(a.salida, manifiesto=ManifiestoMinimo(tos), version_e0="e0-r2")
    print("listo", len(tos), a.salida)


if __name__ == "__main__":
    main()
