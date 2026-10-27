#!/usr/bin/env python3
"""lanzar_agente_r5_prueba.py — El lanzador de una sesión de la corrida en seco de agentes/lanzar_lote_paralelo_r5.py
(U-BANCO-R5-a), a USD 0: el de prueba de N6 (paralelo/lanzar_agente_n6_prueba.py, solo import) con una configuración de juguete
de esta carpeta, la que nombra la variable RCINCO_CONFIG_AGENTES (relativa al banco; por defecto, config_agentes_r5_A.json).

El lote le pasa solo los argumentos de agentes/lanzar_agente.py, así que la configuración llega por el entorno del lote. Las dos
configuraciones de juguete son la de N6 con otro corte_R5: así una sesión del lote corre con el R5 A (32, 30 y 1,80) o con el B
(47, 45 y 3,30), y el lote ve el R5 de cada una en su comando y en su meta, como en la corrida real.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent.parent
if str(AQUI.parent) not in sys.path:
    sys.path.insert(0, str(AQUI.parent))
import lanzar_agente_n6_prueba as N6             # noqa: E402  (solo import)

CONFIG_POR_DEFECTO = "paralelo/seco_r5/config_agentes_r5_A.json"


def main() -> int:
    rel = os.environ.get("RCINCO_CONFIG_AGENTES") or CONFIG_POR_DEFECTO
    p = (BANCO_DIR / rel).resolve()
    if p.parent != AQUI or not p.name.startswith("config_agentes_r5_") or not p.is_file():
        raise SystemExit(f"ABORTO: {rel} no es una configuración de juguete de paralelo/seco_r5/")
    sys.argv[1:] = [*sys.argv[1:], "--config-agentes", str(p)]
    return N6.main()


if __name__ == "__main__":
    raise SystemExit(main())
