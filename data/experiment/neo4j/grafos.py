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
    "KG_Reextraido_r1": {
        "nombre_canonico": "KG-Reextraído-r1",
        "label": "KG_Reextraido_r1",
        "path": EXPERIMENT_DIR / "reextraccion_v2" / "corpus_v2" / "salida_r1" / "kg.json",
        "sha256": "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a",
        "commit_sellado": "185e042",
        "commit_medicion_ev2": "774acac",
        "laudo_promocion": "docs/laudo_promocion_r1_vigente.md",
        "n_nodos": 6529,
        "n_aristas": 17772,
        "ev2_key": "r1",
        # r1 no está en el dict GRAFOS de comun_ev2 (módulo sellado): su vista
        # runtime se sirve por el registro en memoria de ev2_r1/code/comun_r1
        # (reemplaza el despachador al importarse, sin editar módulos sellados;
        # misma vista que vio el agente en la medición 774acac).
        "requiere_registro_dir": EXPERIMENT_DIR / "ev2_r1" / "code",
        "vista_runtime": "comun_ev2.cargar_runtime('r1') tras importar comun_r1 (registro en memoria, U-B1.8)",
        "indice_fulltext": "nodos_fulltext_kg_reextraido_r1",
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
    """KnowledgeGraph con la vista runtime EV2 del grafo (import de comun_ev2).
    Si la entrada declara `requiere_registro_dir`, se importa antes el módulo
    que registra su vista en memoria (r1: comun_r1, precedente U-B1.8)."""
    reg = GRAFOS[clave].get("requiere_registro_dir")
    if reg is not None:
        if str(reg) not in sys.path:
            sys.path.insert(0, str(reg))
        import comun_r1  # noqa: F401,E402  (registra la vista de r1 al importarse)
    from comun_ev2 import cargar_runtime  # noqa: E402  (solo import)
    return cargar_runtime(GRAFOS[clave]["ev2_key"])


def rel_repo(path: Path) -> str:
    return str(Path(path).resolve().relative_to(REPO_DIR))
