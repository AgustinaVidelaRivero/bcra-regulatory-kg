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
    # Tanda 0 (B6.0 fase 2a, U-TANDA0-2A E3.c): grafos r1 re-ensamblados con el
    # esquema congelado y perfil v3_b54. Su vista runtime la registra en memoria
    # data/experiment/tanda0/code/comun_tanda0.py, que cargar_vista_runtime importa
    # por el campo requiere_registro_modulo (opción B, autorizada por la autora el
    # 28/09/2026).
    "KG_Tanda0_Desarrollo_r1": {
        "nombre_canonico": "KG-Tanda0-Desarrollo-r1",
        "label": "KG_Tanda0_Desarrollo_r1",
        "path": EXPERIMENT_DIR / "reextraccion_v2" / "corpus_tanda0" / "ens_desarrollo" / "r1" / "kg.json",
        "sha256": "eab2fdd01dec4dad026d596a793919e666920fab127d7efb14b5b00857ae64ef",
        "commit_sellado": "1b8916c",
        "n_nodos": 6378,
        "n_aristas": 15007,
        "ev2_key": "tanda0_ens_desarrollo",
        "requiere_registro_dir": EXPERIMENT_DIR / "tanda0" / "code",
        "requiere_registro_modulo": "comun_tanda0",
        "vista_runtime": "comun_ev2.cargar_runtime('tanda0_ens_desarrollo') tras importar tanda0/code/comun_tanda0 (registro en memoria, patrón comun_r1)",
        "indice_fulltext": "nodos_fulltext_kg_tanda0_desarrollo_r1",
    },
    "KG_Tanda0_Diez_r1": {
        "nombre_canonico": "KG-Tanda0-Diez-r1",
        "label": "KG_Tanda0_Diez_r1",
        "path": EXPERIMENT_DIR / "reextraccion_v2" / "corpus_tanda0" / "ens_diez" / "r1" / "kg.json",
        "sha256": "dd42d6d9c0c8379da90ec4ed4e4659157a960a0d1ceaf8af5a008bdd9cad9010",
        "commit_sellado": "1b8916c",
        "n_nodos": 8256,
        "n_aristas": 18932,
        "ev2_key": "tanda0_ens_diez",
        "requiere_registro_dir": EXPERIMENT_DIR / "tanda0" / "code",
        "requiere_registro_modulo": "comun_tanda0",
        "vista_runtime": "comun_ev2.cargar_runtime('tanda0_ens_diez') tras importar tanda0/code/comun_tanda0 (registro en memoria, patrón comun_r1)",
        "indice_fulltext": "nodos_fulltext_kg_tanda0_diez_r1",
    },
    # Tanda 0, perfil r2b (U-REEXT-T0; T3, punto 4, reemplazadas en T3-bis, punto 5): ensamblados r2b de la
    # re-extracción de la tanda 0, re-ensamblados en T3-bis. Su vista runtime la registra en memoria
    # data/experiment/reext_t0/t3bis/registro_vista_r2b.py (patrón comun_tanda0, sin editarlo).
    # commit_sellado: "PENDIENTE" hasta que la autora selle los grafos (no None: Neo4j no guarda propiedades nulas y
    # cargar_kg.verificar_carga lee la clave de KG_Meta).
    "KG_Tanda0_Desarrollo_r2b": {
        "nombre_canonico": "KG-Tanda0-Desarrollo-r2b",
        "label": "KG_Tanda0_Desarrollo_r2b",
        "path": EXPERIMENT_DIR / "reextraccion_v2" / "corpus_tanda0" / "ens_desarrollo_r2b" / "r2" / "kg.json",
        "sha256": "6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2",
        "commit_sellado": "bbc38dc",
        "n_nodos": 6990,
        "n_aristas": 23445,
        "ev2_key": "tanda0_ens_desarrollo_r2b",
        "requiere_registro_dir": EXPERIMENT_DIR / "reext_t0" / "t3bis",
        "requiere_registro_modulo": "registro_vista_r2b",
        "vista_runtime": "comun_ev2.cargar_runtime('tanda0_ens_desarrollo_r2b') tras importar reext_t0/t3bis/registro_vista_r2b (registro en memoria, patrón comun_tanda0); r2b no se evalúa con EV2",
        "indice_fulltext": "nodos_fulltext_kg_tanda0_desarrollo_r2b",
    },
    "KG_Tanda0_Diez_r2b": {
        "nombre_canonico": "KG-Tanda0-Diez-r2b",
        "label": "KG_Tanda0_Diez_r2b",
        "path": EXPERIMENT_DIR / "reextraccion_v2" / "corpus_tanda0" / "ens_diez_r2b" / "r2" / "kg.json",
        "sha256": "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57",
        "commit_sellado": "bbc38dc",
        "n_nodos": 8816,
        "n_aristas": 27632,
        "ev2_key": "tanda0_ens_diez_r2b",
        "requiere_registro_dir": EXPERIMENT_DIR / "reext_t0" / "t3bis",
        "requiere_registro_modulo": "registro_vista_r2b",
        "vista_runtime": "comun_ev2.cargar_runtime('tanda0_ens_diez_r2b') tras importar reext_t0/t3bis/registro_vista_r2b (registro en memoria, patrón comun_tanda0); r2b no se evalúa con EV2",
        "indice_fulltext": "nodos_fulltext_kg_tanda0_diez_r2b",
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
        import importlib  # noqa: E402
        # default comun_r1: comportamiento idéntico para las entradas existentes
        importlib.import_module(GRAFOS[clave].get("requiere_registro_modulo", "comun_r1"))
    from comun_ev2 import cargar_runtime  # noqa: E402  (solo import)
    return cargar_runtime(GRAFOS[clave]["ev2_key"])


def rel_repo(path: Path) -> str:
    return str(Path(path).resolve().relative_to(REPO_DIR))
