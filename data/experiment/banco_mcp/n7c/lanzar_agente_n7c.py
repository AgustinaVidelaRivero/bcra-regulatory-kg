#!/usr/bin/env python3
"""lanzar_agente_n7c.py — El lanzador de una sesión de B2 de N7c (el octavo cambio, D-B2-6): lanzar_agente_n6.lanzar tal cual
(n6/lanzar_agente_n6.py, importado sin editarlo), con la configuración de agentes de B2 (n7c/config_agentes_n7c.json) fija.
El lanzador del lote le pasa solo las entradas de lanzar_agente.py (agentes/lanzar_lote_paralelo.py:291-293) y
lanzar_agente_n6.py toma entonces su propia configuración (n6/lanzar_agente_n6.py:31, :36, :58), que no tiene los brazos de
B2; por eso la configuración va fija acá, con la forma de n6/seco/lanzar_agente_n6_seco.py.
Lo nombran como su lanzador las dos entradas: la de B2 y la del humo. El humo arma su orden y sus lotes con su propia
configuración (n7c/config_agentes_n7c_humo.json, la de B2 salvo las repeticiones), y cada sesión se prepara con la de B2, cuyos
brazos son, byte a byte, los mismos (lo controla correr_n7c.precondiciones antes de lanzar nada).
Uso: lo lanza el lote (--brazo, --id, --pregunta, --out, --modo, --via, --sesiones y --timeout-s).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI.parent / "n6") not in sys.path:
    sys.path.insert(0, str(AQUI.parent / "n6"))
import lanzar_agente_n6 as LN6     # noqa: E402  (HEAD, sin editar)

CONFIG_B2 = AQUI / "config_agentes_n7c.json"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--brazo", required=True)
    ap.add_argument("--id", required=True)
    ap.add_argument("--pregunta", required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--modo", choices=["real", "init"], default="init")
    ap.add_argument("--via", choices=["api", "bedrock"], default="api")
    ap.add_argument("--sesiones", type=Path, default=LN6.LA.BANCO_SESIONES)
    ap.add_argument("--timeout-s", type=float, default=1800.0)
    a = ap.parse_args()
    meta = LN6.lanzar(a.brazo, a.id, a.pregunta, a.out, a.modo, a.via, None, a.timeout_s, a.sesiones, CONFIG_B2)
    print(json.dumps({"brazo": a.brazo, "modo": a.modo, "completa": meta["completitud_R3"]["completa"],
                      "costo": meta["tokens_R9"]["costo_recomputado"]["total_usd"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
