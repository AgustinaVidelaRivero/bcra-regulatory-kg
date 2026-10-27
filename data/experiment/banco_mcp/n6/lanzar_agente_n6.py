#!/usr/bin/env python3
"""lanzar_agente_n6.py — Lanza UNA sesión `claude -p` de N6 de U-NAV-DISENO en una de sus configuraciones (un brazo de
n6/config_agentes_n6.json: las 8 del grafo y las 2 de F1), con la interfaz de agentes/lanzar_agente.py, así lo corre el
lanzador del lote (agentes/lanzar_lote_paralelo_r5.py, que pasa solo --brazo, --id, --pregunta, --out, --modo, --via,
--sesiones y --timeout-s).

Es paralelo/lanzar_agente_n6_prueba.lanzar (HEAD, importado sin editarlo) con la configuración de N6 en lugar de la de prueba:
la misma persistencia (prompt, comando, stream, stderr, sesión, log R1 y meta), el mismo entorno de la sesión (la lista
cerrada, con el venv del servidor de fragmentos en todos los brazos) y los mismos archivos de identidad (la configuración y
el código del servidor de cada brazo). Al terminar, la meta suma la configuración de N6 de la sesión y este archivo en el
registro del lanzador. CONFIG cambia solo por --config-agentes (la corrida en seco, que usa su configuración de juguete).

Uso: lanzar_agente_n6.py --brazo kg_T --id X --pregunta "..." --out <dir> --modo real --sesiones <raíz>
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
for _p in (str(BANCO_DIR), str(BANCO_DIR / "paralelo"), str(BANCO_DIR / "agentes")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import lanzar_agente_n6_prueba as LP                    # noqa: E402  (HEAD: solo import)
from comun_banco import rel_repo, sha256_file           # noqa: E402

LA = LP.LA
CONFIG = AQUI / "config_agentes_n6.json"
UNIDAD = "U-NAV-DISENO, N6"


def lanzar(brazo: str, pid: str, pregunta: str, out: Path, modo: str = "init", via: str = "api", cwd: Path | None = None,
           timeout_s: float = 1800.0, sesiones: Path = LA.BANCO_SESIONES, ruta_cfg: Path = CONFIG) -> dict:
    meta = LP.lanzar(brazo, pid, pregunta, out, modo, via, cwd, timeout_s, sesiones, ruta_cfg)
    cfg = LA.cargar(ruta_cfg)
    meta["unidad"] = UNIDAD
    meta["configuracion_n6"] = cfg["brazos"][brazo].get("configuracion_n6")
    meta["config_agentes_n6"] = {"ruta": rel_repo(ruta_cfg), "sha256": sha256_file(ruta_cfg)}
    meta["harness_R10"]["lanzador"] = list(meta["harness_R10"]["lanzador"]) + LA.archivos_lanzador(__file__)
    (out / f"meta_{pid}.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return meta


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--brazo", required=True)
    ap.add_argument("--id", required=True)
    ap.add_argument("--pregunta", required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--modo", choices=["real", "init"], default="init")
    ap.add_argument("--via", choices=["api", "bedrock"], default="api")
    ap.add_argument("--cwd", type=Path, default=None)
    ap.add_argument("--sesiones", type=Path, default=LA.BANCO_SESIONES)
    ap.add_argument("--timeout-s", type=float, default=1800.0)
    ap.add_argument("--config-agentes", type=Path, default=CONFIG)
    a = ap.parse_args()
    meta = lanzar(a.brazo, a.id, a.pregunta, a.out, a.modo, a.via, a.cwd, a.timeout_s, a.sesiones, a.config_agentes)
    print(json.dumps({"brazo": a.brazo, "configuracion_n6": meta.get("configuracion_n6"), "modo": a.modo,
                      "tools_coinciden": meta["inventario_tools_R6"]["coincide"], "completa": meta["completitud_R3"]["completa"],
                      "costo": meta["tokens_R9"]["costo_recomputado"]["total_usd"], "duracion_s": meta["duracion_s"]},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
