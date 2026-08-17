"""
grafos.py — Registro de los grafos que el backend Neo4j carga y sirve (U-A1.1).

Nomenclatura canónica: docs/nomenclatura_grafos.md. Cada entrada fija el path
sellado, el sha256 esperado (verificado ANTES de cualquier carga), los conteos
sellados, el label Neo4j que separa el grafo dentro de la única db de
Community (:KG_Refinado / :KG_Reextraido), el nombre de su índice full-text y
la vista RUNTIME con la que el harness lo ve.

Vista runtime (decisión): se reutiliza `cargar_runtime` de
data/experiment/ev2_corrida/code/comun_ev2.py (solo IMPORT), porque es la
vista exacta que vio el agente en EV2 — el mapa causal de U-A0 (clases
alcanzabilidad / vista_no_consultada) se midió sobre esas vistas:
  - KG-Refinado  -> loader.load_graph_from_path(path, adapter_key=None)
                    (idéntico a lo que ya hacía cargar_kg.py en c26cb9b).
  - KG-Reextraído-> provenance PRIMARIA {to, archivo, punto} mapeada en memoria
                    a {source_doc, location} con las dataclasses y el merge del
                    loader congelado (sin ese mapeo el adaptador nulo dejaría
                    al grafo sin provenances y el agente no podría citar).
El kg.json no se toca en ningún caso.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

NEO4J_DIR = Path(__file__).resolve().parent
EXPERIMENT_DIR = NEO4J_DIR.parent
REPO_DIR = EXPERIMENT_DIR.parents[1]
EVAL_DIR = EXPERIMENT_DIR / "evaluacion"
EV2_CODE_DIR = EXPERIMENT_DIR / "ev2_corrida" / "code"
for _p in (str(EVAL_DIR), str(EV2_CODE_DIR), str(NEO4J_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

GRAFOS = {
    "KG_Refinado": {
        "nombre_canonico": "KG-Refinado",
        "label": "KG_Refinado",
        "path": EXPERIMENT_DIR / "grafo_v2" / "reensamblado_v3" / "kg.json",
        "sha256": "26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571",
        "commit_sellado": "05984e1",
        "n_nodos": 4469,
        "n_aristas": 8073,
        "ev2_key": "v3",
        "vista_runtime": "comun_ev2.cargar_runtime('v3') = loader.load_graph_from_path(path, adapter_key=None)",
        "indice_fulltext": "nodos_fulltext_kg_refinado",
    },
    "KG_Reextraido": {
        "nombre_canonico": "KG-Reextraído",
        "label": "KG_Reextraido",
        "path": EXPERIMENT_DIR / "reextraccion_v2" / "corpus_v2" / "salida" / "kg.json",
        "sha256": "8e2eadee57b48e00ccb51ade9a953ba1469001fe089c45d97c4307ccf2725581",
        "commit_sellado": "5273c0c",
        "n_nodos": 6178,
        "n_aristas": 11415,
        "ev2_key": "v2",
        "vista_runtime": "comun_ev2.cargar_runtime('v2') (provenance primaria mapeada a {source_doc, location}; dataclasses + merge del loader congelado)",
        "indice_fulltext": "nodos_fulltext_kg_reextraido",
    },
}
CLAVES = list(GRAFOS.keys())
GRAFO_DEFAULT = "KG_Refinado"   # el grafo vigente (docs/tablero.md); compatibilidad con c26cb9b


def sha256_de(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def verificar_sha(clave: str) -> str:
    """Aborta si el kg.json no coincide con el sha sellado. Devuelve el sha."""
    g = GRAFOS[clave]
    h = sha256_de(g["path"])
    if h != g["sha256"]:
        raise SystemExit(
            f"ABORTO: sha256 de {g['path']} = {h}\n"
            f"        esperado ({clave}) = {g['sha256']}\n"
            "El grafo insumo no coincide con el sellado; no se carga nada."
        )
    return h


def cargar_vista_runtime(clave: str):
    """KnowledgeGraph con la vista runtime EV2 del grafo (import de comun_ev2)."""
    from comun_ev2 import cargar_runtime  # noqa: E402  (solo import)
    return cargar_runtime(GRAFOS[clave]["ev2_key"])


def rel_repo(path: Path) -> str:
    return str(Path(path).resolve().relative_to(REPO_DIR))
