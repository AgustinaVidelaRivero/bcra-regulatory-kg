#!/usr/bin/env python3
"""lanzar_agente_n6_seco.py — El lanzador de una sesión de la corrida en seco de N6: lanzar_agente_n6.lanzar tal cual, con la
configuración de agentes de juguete (n6/seco/config_agentes_seco_n6.json) en lugar de la de N6. El lanzador del lote le pasa
solo las entradas de lanzar_agente.py, así que la configuración va fija acá, como en paralelo/seco_r5/lanzar_agente_r5_prueba.py.
Uso: lo lanza el lote de la corrida en seco (la entrada seca lo nombra como su lanzador).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI.parent) not in sys.path:
    sys.path.insert(0, str(AQUI.parent))
import lanzar_agente_n6 as LN6     # noqa: E402

CONFIG_SECO = AQUI / "config_agentes_seco_n6.json"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--brazo", required=True)
    ap.add_argument("--id", required=True)
    ap.add_argument("--pregunta", required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--modo", choices=["real", "init"], default="init")
    ap.add_argument("--via", choices=["api", "bedrock"], default="api")
    ap.add_argument("--sesiones", type=Path, required=True)
    ap.add_argument("--timeout-s", type=float, default=600.0)
    a = ap.parse_args()
    meta = LN6.lanzar(a.brazo, a.id, a.pregunta, a.out, a.modo, a.via, None, a.timeout_s, a.sesiones, CONFIG_SECO)
    print(json.dumps({"brazo": a.brazo, "completa": meta["completitud_R3"]["completa"],
                      "costo": meta["tokens_R9"]["costo_recomputado"]["total_usd"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
