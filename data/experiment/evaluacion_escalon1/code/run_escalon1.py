#!/usr/bin/env python3
"""Wrapper de corrida — escalón 1.

Registra la clave `grafo_v2` en el loader congelado EN MEMORIA (patrón
"módulo aparte que importa al loader": los archivos del cuarteto no se
editan, así `code_version` no rota y las cachés existentes quedan intactas)
y delega en `run_posthoc.main()` con los argumentos tal cual.

Config de adaptador de `grafo_v2`: igual a run_5 (`node_extra`/`edge_extra`
= None) porque el assemble v2 emite un único `provenance` dict por
nodo/arista, ids ya deduplicados (el merge genérico del loader es no-op).

Uso (desde cualquier cwd):
    .venv/bin/python data/experiment/evaluacion_escalon1/code/run_escalon1.py \
        --run grafo_v2 --queries <ruta> --reps 1 --label <label> --db <ruta>

NO delega en `runners/validate_loader.py`: ese script escribe su reporte
dentro de `evaluacion/` (zona congelada). Los checks de carga del grafo_v2
se hacen aparte, offline (ver informe de la unidad).
"""
import sys
from pathlib import Path

EVAL_DIR = Path(__file__).resolve().parents[2] / "evaluacion"
sys.path.insert(0, str(EVAL_DIR / "runners"))
sys.path.insert(0, str(EVAL_DIR))

import loader  # noqa: E402

loader.RUN_FILES["grafo_v2"] = loader.EXPERIMENT_DIR / "grafo_v2" / "kg.json"
if "grafo_v2" not in loader.RUN_KEYS:
    loader.RUN_KEYS.append("grafo_v2")  # mutación in-place: propaga a los imports
loader.ADAPTERS["grafo_v2"] = {"node_extra": None, "edge_extra": None}

if __name__ == "__main__":
    import run_posthoc
    sys.exit(run_posthoc.main())
