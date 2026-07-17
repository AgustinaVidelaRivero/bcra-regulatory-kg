"""main.py — App local mínima sobre los grafos del repo (U1: esqueleto).

Descubrimiento de grafos al iniciar (glob de data/experiment/*/kg.json) y
endpoint GET /runs. Toda carga de grafos pasa por load_graph_from_path()
del loader de la Fase 2.3; acá no se parsea ningún kg.json a mano.

Arranque, desde la raíz del repo:
    uvicorn app.main:app --port 8000
"""

import sys
from pathlib import Path

from fastapi import FastAPI

REPO_ROOT = Path(__file__).resolve().parent.parent
EXPERIMENT_DIR = REPO_ROOT / "data" / "experiment"
EVALUACION_DIR = EXPERIMENT_DIR / "evaluacion"

# El loader vive fuera de un package; se importa por sys.path.
sys.path.insert(0, str(EVALUACION_DIR))
from loader import load_graph_from_path  # noqa: E402

# Al agregar un grafo nuevo con provenance múltiple, registrar acá su adapter_key.
ADAPTER_KEYS = {
    "run_1_cookbook": "run_1",
    "run_2_papers": "run_2",
    "run_3_ppf_core": "run_3",
    "run_4_schema_light": "run_4",
    "run_5_hybrid": "run_5",
}


def _discover_runs() -> list:
    """Un objeto {id, ruta, nodos, aristas} por directorio con kg.json; si un
    grafo no carga, el run entra como {id, ruta, error} sin romper el arranque."""
    runs = []
    for kg_path in sorted(EXPERIMENT_DIR.glob("*/kg.json")):
        run_id = kg_path.parent.name
        ruta = str(kg_path.relative_to(REPO_ROOT))
        try:
            kg = load_graph_from_path(kg_path, adapter_key=ADAPTER_KEYS.get(run_id))
            runs.append({"id": run_id, "ruta": ruta,
                         "nodos": len(kg.nodes), "aristas": len(kg.edges)})
        except Exception as e:
            runs.append({"id": run_id, "ruta": ruta,
                         "error": f"{type(e).__name__}: {e}"})
    return runs


app = FastAPI(title="bcra-regulatory-kg — app local")
RUNS = _discover_runs()


@app.get("/runs")
def get_runs() -> list:
    return RUNS
