"""U-R2-CODIGO, agregado 9 de las decisiones sobre el freno R3 — diagnóstico,
sin corregir: por qué `correr_e0.py --version-e0 e0-r2` da 0 chunks para TOs de
la partición del corpus escalado. Solo lectura. USD 0.

`correr_e0.correr` (`correr_e0.py:996-1009`) hace, por TO, solo la etapa 1 de la
escalera de E0 (camino vigente: `clasificar_paginas` y `parsear_cuerpo`, con la
regla K en e0-r2). La partición (`segmentacion_84/b584_particion/code/
correr_b584.py:127-147`) agrega dos etapas cuando la 1 no da chunks: la 2
(marcadores B5.8.2) y la 3 (modo sin raíz B5.8.1). Este script corre la etapa 1
de `correr_e0`, legada y e0-r2, sobre los TOs que `conteos_b584.json` marca con
`activado_por_cero_unidades` y cuenta los chunks de cada una (`construir_chunks`
tras las correcciones post-parseo, como `correr_e0`).

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/r4_diag_escalera_e0.py --out <json> \
      [--solo TO1,TO2]
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
E0_DIR = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking"
if str(E0_DIR) not in sys.path:
    sys.path.insert(0, str(E0_DIR))
import e0_lib as E0  # noqa: E402

CONTEOS = REPO / "data" / "experiment" / "segmentacion_84" / "b584_particion" / "conteos_b584.json"
PDFS = REPO / "data" / "experiment" / "escalado_prep" / "pdfs"


def chunks_etapa1(to: str, paginas, roles, r2: bool) -> int:
    if r2:
        rep = E0.titulos_mayusculas_repetidos(paginas, roles)
        res = E0.parsear_cuerpo(to, f"{to}.pdf", paginas, roles, mayusculas_repetidas=rep)
    else:
        res = E0.parsear_cuerpo(to, f"{to}.pdf", paginas, roles)
    res.reasignaciones_continuidad = E0.aplicar_continuidad_enumeracion(res)
    E0.corregir_fronteras_intra_palabra(res)
    return len(E0.construir_chunks(res))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--solo", default=None)
    a = ap.parse_args()
    conteos = json.loads(CONTEOS.read_text(encoding="utf-8"))
    tos = sorted(t for t, v in conteos.items() if isinstance(v, dict) and v.get("activado_por_cero_unidades"))
    if a.solo:
        tos = [t for t in tos if t in a.solo.split(",")]
    filas = []
    for to in tos:
        paginas = E0.extraer_lineas(PDFS / f"{to}.pdf")
        roles = E0.clasificar_paginas(paginas)
        v = conteos[to]
        filas.append({"to": to, "modo_lectura_b584": v.get("modo_lectura"), "marcadores_b582": v.get("marcadores_b582"),
                      "unidades_b584": v.get("unidades_extraccion"),
                      "chunks_etapa1_legada": chunks_etapa1(to, paginas, roles, False),
                      "chunks_etapa1_e0_r2": chunks_etapa1(to, paginas, roles, True)})
        print(json.dumps(filas[-1], ensure_ascii=False), flush=True)
    modos = Counter(v.get("modo_lectura") for v in conteos.values() if isinstance(v, dict))
    out = {"unidad": "U-R2-CODIGO", "etapa": "agregado 9: diagnóstico de la escalera de E0 en correr_e0",
           "tos_particion": sum(modos.values()), "modo_lectura_b584": dict(sorted(modos.items())),
           "tos_activados_por_cero_unidades": len(tos),
           "con_0_chunks_en_etapa1": {"legada": sum(f["chunks_etapa1_legada"] == 0 for f in filas),
                                      "e0_r2": sum(f["chunks_etapa1_e0_r2"] == 0 for f in filas)},
           "filas": filas}
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in out.items() if k != "filas"}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
