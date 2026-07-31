#!/usr/bin/env python3
"""Wrapper de corrida — escalón 1b (protocolo docs/protocolo_escalon1b.md).

Registra EN MEMORIA las claves `grafo_v2` y `reensamblado_v3` en el loader
congelado (patrón "módulo aparte que importa al loader", idéntico a
run_escalon1.py: los archivos del cuarteto no se editan, `code_version` no
rota y las cachés del escalón 1 reponen por hit) y delega en
`run_posthoc.main()` con los argumentos tal cual.

Adaptador de ambos grafos: nulo (`node_extra`/`edge_extra` = None). Para
`reensamblado_v3` esto garantiza la paridad de interfaz del protocolo §1: el
loader pliega solo la `provenance` primaria; el campo `provenances` (lista
acumulada del re-ensamblado) y `rol_fuente` no llegan al harness.

Uso (desde cualquier cwd):
    .venv/bin/python data/experiment/evaluacion_escalon1/code/run_escalon1b.py \
        --run reensamblado_v3 --queries <ruta EV1_runtime.json> --reps 1 \
        --label escalon1b_rN --db <ruta escalon1b_rN.db>
"""
import sys
from pathlib import Path

EVAL_DIR = Path(__file__).resolve().parents[2] / "evaluacion"
sys.path.insert(0, str(EVAL_DIR / "runners"))
sys.path.insert(0, str(EVAL_DIR))

import loader  # noqa: E402

loader.RUN_FILES["grafo_v2"] = loader.EXPERIMENT_DIR / "grafo_v2" / "kg.json"
loader.RUN_FILES["reensamblado_v3"] = (
    loader.EXPERIMENT_DIR / "grafo_v2" / "reensamblado_v3" / "kg.json"
)
for k in ("grafo_v2", "reensamblado_v3"):
    if k not in loader.RUN_KEYS:
        loader.RUN_KEYS.append(k)  # mutación in-place: propaga a los imports
    loader.ADAPTERS[k] = {"node_extra": None, "edge_extra": None}

if __name__ == "__main__":
    import run_posthoc
    sys.exit(run_posthoc.main())
