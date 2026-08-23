"""
comun_r1.py — Infraestructura común de U-B1.8: fidelidad EV2 de KG-Reextraído-r1
(pre-registro data/experiment/ev2_r1/preregistro_ev2_r1.md; protocolo
docs/protocolo_corrida_ev2.md; método docs/preregistro_evaluacion_fidelidad_ev2.md).

Extiende EN MEMORIA el circuito sellado de EV2 al grafo r1; ningún módulo
sellado se edita en disco (los sha se verifican al inicio y al cierre de cada
etapa). Concretamente:
  - registra la entrada "r1" en el dict comun_ev2.GRAFOS (el mismo objeto que
    ven runner_ev2 y las verificaciones: verificar_grafos pasa a exigir 4/4);
  - reemplaza en memoria el despachador de vista runtime (comun_ev2.cargar_runtime
    y la referencia importada runner_ev2.cargar_runtime) por uno que atiende
    "r1" y delega los demás grafos sin cambios.

Adaptador de provenance de r1 (pre-registro §2): r1 conserva archivo/punto en
cada provenance (y agrega chunk_id/paginas/ancestros, que NO viajan al censo ni
a las tools). Se reutiliza comun_ev2._map_prov_v2 — el mismo mapeo de la vista
v2 de la corrida base:
  - vista RUNTIME: provenance PRIMARIA mapeada, dataclasses y merge del loader
    congelado (patrón exacto de comun_ev2._cargar_runtime_v2);
  - vista de CENSO: `provenances` completas mapeadas.

Semillas y nombres pre-declarados (pre-registro §4): orden del agente
`orden-ev2-r1`; ids opacos base EV2R1- (salt `juez-ev2-r1`) y §7 EV2E1-
(salt `juez-ev2-r1-enc`); label del agente base `ev2_r1_base`; dbs bajo
ev2_r1/cache/ (gitignorado).
"""

from __future__ import annotations

import hashlib
import json
import random
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
UNIDAD_DIR = CODE_DIR.parent                       # data/experiment/ev2_r1
EXP_DIR = UNIDAD_DIR.parent                        # data/experiment
REPO_DIR = EXP_DIR.parent.parent

CORRIDA_DIR = EXP_DIR / "ev2_corrida"
FIDELIDAD_EVAL_DIR = EXP_DIR / "ev2_fidelidad_eval"
ENC_DIR = EXP_DIR / "ev2_encadenamiento"
JUEZ_DIR = EXP_DIR / "ev2_juez"

for _p in (CORRIDA_DIR / "code", FIDELIDAD_EVAL_DIR / "code", ENC_DIR / "code"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import comun_ev2 as ce                     # noqa: E402  (corrida base, sin editar)
import runner_ev2 as rv                    # noqa: E402  (runner base, sin editar)
import comun_fidelidad as cf               # noqa: E402  (pipeline ciego del juez)
from comun_fidelidad import juez, mapping  # noqa: E402  (juez congelado)
from loader import Edge, KnowledgeGraph, Node, _merge_nodes  # noqa: E402
from resolucion import AnclaIndex          # noqa: E402

# --------------------------------------------------------------------------- #
# Rutas de esta unidad                                                        #
# --------------------------------------------------------------------------- #
ORDEN_DIR = UNIDAD_DIR / "orden"
CENSO_DIR = UNIDAD_DIR / "censo"
CACHE_DIR = UNIDAD_DIR / "cache"
TRAZAS_DIR = UNIDAD_DIR / "trazas"
JUEZ_OUT_DIR = UNIDAD_DIR / "juez_out"
DESANON_DIR = UNIDAD_DIR / "desanonimizacion_SOLO_MESA"
ESTIMACION_DIR = UNIDAD_DIR / "estimacion"
SELLOS_DIR = UNIDAD_DIR / "sellos"
SELFTEST_DIR = UNIDAD_DIR / "selftest_out"

# --------------------------------------------------------------------------- #
# El grafo r1 (pre-registro §0) y su registro en memoria                       #
# --------------------------------------------------------------------------- #
R1_KEY = "r1"
R1 = {
    "path": EXP_DIR / "reextraccion_v2" / "corpus_v2" / "salida_r1" / "kg.json",
    "sha256": "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a",
    "label": "ev2_r1_base",
}

SEMILLA_ORDEN_R1 = "orden-ev2-r1"          # pre-registro §4 (agente)
SEMILLA_ORDEN_JUEZ = "juez-ev2-r1"         # orden ciego del juez base
SEMILLA_ORDEN_JUEZ_ENC = "juez-ev2-r1-enc"
SEMILLA_AUDITORIA = "auditoria-ev2-r1"
SEMILLA_MUESTRA = "adjudicacion-ev2-r1"    # mandato
SEMILLA_WORKSHEET = "worksheet-ev2-r1"

SAL_ID_BASE = "juez-ev2-r1"
PREFIJO_BASE = "EV2R1-"
SAL_ID_ENC = "juez-ev2-r1-enc"
PREFIJO_ENC = "EV2E1-"
SAL_ID_FICHA = "worksheet-ev2-r1"
PREFIJO_FICHA = "ADJ1-"

DB_PREFIX_JUEZ = "ev2_r1_eval"             # cache/ev2_r1_eval_r{1,2,3}.db
LABEL_JUEZ = "ev2_r1_eval_r{rep}"
LABEL_ENC = "ev2_r1_enc_r{rep}"            # agente §7
DB_PREFIX_JUEZ_ENC = "ev2_r1_enc_juez"
LABEL_JUEZ_ENC = "ev2_r1_enc_juez_r{rep}"
REPS_JUEZ = 3
REPS_AGENTE_ENC = 3

GOLD_SHA256_ESPERADO = "1d58733699c325c90510e1ead5f18eac6c3cd970ee3b0ab7ff141da539162b40"


def _cargar_runtime_r1() -> KnowledgeGraph:
    """Vista runtime de r1: provenance PRIMARIA mapeada a {source_doc, location}
    con las dataclasses y el merge del loader congelado — patrón idéntico a
    comun_ev2._cargar_runtime_v2 (la vista v2 de la corrida base)."""
    path = R1["path"]
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    raw_nodes = []
    for n in data.get("nodes", []):
        p = ce._map_prov_v2(n.get("provenance") or {})
        raw_nodes.append(Node(
            id=n.get("id"), type=n.get("type"), label=n.get("label"),
            properties=dict(n.get("properties") or {}),
            provenances=[p] if p else [],
        ))
    nodes, merges = _merge_nodes(raw_nodes)
    edges = []
    for e in data.get("edges", []):
        p = ce._map_prov_v2(e.get("provenance") or {})
        edges.append(Edge(
            source=e.get("source"), target=e.get("target"),
            relation=e.get("relation"),
            properties=dict(e.get("properties") or {}),
            provenances=[p] if p else [],
        ))
    return KnowledgeGraph(
        run_key="salida_r1", path=path, nodes=nodes, edges=edges,
        raw_node_count=len(data.get("nodes", [])),
        raw_edge_count=len(data.get("edges", [])),
        merges=merges,
    )


_CARGAR_RUNTIME_ORIG = ce.cargar_runtime


def _cargar_runtime_ext(grafo: str) -> KnowledgeGraph:
    if grafo == R1_KEY:
        return _cargar_runtime_r1()
    return _CARGAR_RUNTIME_ORIG(grafo)


def registrar_r1() -> None:
    """Registro EN MEMORIA de r1 (idempotente): entrada en GRAFOS (dict
    compartido: runner_ev2.GRAFOS es el mismo objeto) + despachador de runtime
    en comun_ev2 y en la referencia importada por runner_ev2."""
    ce.GRAFOS[R1_KEY] = R1
    ce.cargar_runtime = _cargar_runtime_ext
    rv.cargar_runtime = _cargar_runtime_ext


registrar_r1()


# --------------------------------------------------------------------------- #
# Vista de censo y AnclaIndex de r1                                            #
# --------------------------------------------------------------------------- #
def cargar_censo_raw_r1() -> dict:
    """kg.json de r1 con `provenances` COMPLETAS en shape {source_doc, location}
    (mismo mapeo que la vista de censo v2 de comun_ev2.cargar_censo_raw)."""
    with open(R1["path"], encoding="utf-8") as f:
        data = json.load(f)
    nodes = []
    for n in data.get("nodes", []):
        n = dict(n)
        provs = [ce._map_prov_v2(p) for p in (n.get("provenances") or
                                              ([n.get("provenance")] if n.get("provenance") else []))]
        n["provenances"] = [p for p in provs if p]
        nodes.append(n)
    return {"nodes": nodes, "edges": data.get("edges", [])}


def indice_anclas_r1() -> AnclaIndex:
    """AnclaIndex (regla sellada: match exacto, contenedores >10 excluidos)
    sobre la vista de censo de r1."""
    return AnclaIndex(cargar_censo_raw_r1())


# --------------------------------------------------------------------------- #
# Sellos                                                                       #
# --------------------------------------------------------------------------- #
def sha256_path(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def sha256_texto(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def rel_repo(p: Path) -> str:
    return str(Path(p).resolve().relative_to(REPO_DIR))


def verificar_sellos(verbose: bool = False) -> dict:
    """Instrumento congelado (prompt/juez/mapping + cuarteto + gold, vía
    comun_fidelidad.verificar_sellos), los CUATRO grafos (r1 registrado:
    comun_ev2.verificar_grafos exige 4/4) y sha de los módulos sellados que
    esta unidad importa. Levanta si algo difiere de lo esperado."""
    s = cf.verificar_sellos()                     # prompt v1, juez.py, mapping.py, cuarteto, gold
    if s["gold"] != GOLD_SHA256_ESPERADO:
        raise RuntimeError(f"gold alterado: {s['gold']}")
    g = ce.verificar_grafos(verbose=verbose)      # 4/4 (incluye r1) o levanta
    for k, v in g.items():
        s[f"grafo_{k}"] = v
    for nombre, p in (
        ("comun_ev2.py", CORRIDA_DIR / "code" / "comun_ev2.py"),
        ("runner_ev2.py", CORRIDA_DIR / "code" / "runner_ev2.py"),
        ("metrica_ev2.py", CORRIDA_DIR / "code" / "metrica_ev2.py"),
        ("comun_fidelidad.py", FIDELIDAD_EVAL_DIR / "code" / "comun_fidelidad.py"),
        ("pipeline_fidelidad.py", FIDELIDAD_EVAL_DIR / "code" / "pipeline_fidelidad.py"),
        ("agregacion_enc.py", ENC_DIR / "code" / "agregacion_enc.py"),
        ("resolucion.py", EXP_DIR / "exploracion" / "sinteticas" / "resolucion.py"),
        ("metrica.py", EXP_DIR / "exploracion" / "sinteticas" / "metrica.py"),
    ):
        s[nombre] = sha256_path(p)
    return s


def escribir_sellos(nombre: str) -> Path:
    SELLOS_DIR.mkdir(parents=True, exist_ok=True)
    s = verificar_sellos()
    p = SELLOS_DIR / nombre
    p.write_text("".join(f"{v}  {k}\n" for k, v in s.items()), encoding="utf-8")
    return p


# --------------------------------------------------------------------------- #
# Casos y orden del agente (solo eje de fidelidad; semilla orden-ev2-r1)       #
# --------------------------------------------------------------------------- #
def casos_fidelidad_r1() -> list[dict]:
    """Los 40 casos de fidelidad en el orden pre-declarado: lista ordenada por
    id sellado → random.Random('orden-ev2-r1').shuffle (pre-registro §4). El
    eje de navegabilidad NO corre en esta unidad."""
    casos = [{"caso_id": p["id"], "eje": "fidelidad", "pregunta": p["pregunta"]}
             for p in ce.cargar_fidelidad()]
    if len(casos) != 40 or len({c["caso_id"] for c in casos}) != 40:
        raise ValueError(f"se esperaban 40 casos de fidelidad únicos: {len(casos)}")
    casos.sort(key=lambda c: c["caso_id"])
    random.Random(SEMILLA_ORDEN_R1).shuffle(casos)
    for pos, c in enumerate(casos, 1):
        c["pos_orden_global"] = pos
    return casos


def persistir_orden(casos: list[dict]) -> Path:
    """Persiste (o verifica, si ya existe) el orden del agente."""
    ORDEN_DIR.mkdir(parents=True, exist_ok=True)
    p = ORDEN_DIR / "orden_agente_r1.json"
    obj = {"semilla": SEMILLA_ORDEN_R1,
           "regla": "40 casos de fidelidad ordenados por caso_id → random.Random(semilla).shuffle",
           "n": len(casos),
           "casos_en_orden": [c["caso_id"] for c in casos]}
    nuevo = json.dumps(obj, ensure_ascii=False, indent=2)
    if p.exists():
        if p.read_text(encoding="utf-8") != nuevo:
            raise RuntimeError(f"{p} ya existe y difiere de lo recomputado")
    else:
        p.write_text(nuevo, encoding="utf-8")
    return p


# --------------------------------------------------------------------------- #
# Ids opacos (base y §7)                                                       #
# --------------------------------------------------------------------------- #
def id_opaco_base(id_pregunta: str, sha_resp: str) -> str:
    return PREFIJO_BASE + sha256_texto(f"{SAL_ID_BASE}|{id_pregunta}|{R1_KEY}|{sha_resp}")[:10]


def id_opaco_enc(id_pregunta: str, rep: int, sha_resp: str) -> str:
    return PREFIJO_ENC + sha256_texto(f"{SAL_ID_ENC}|{id_pregunta}|{R1_KEY}|{rep}|{sha_resp}")[:10]


def id_ficha(id_pregunta: str, sha_resp: str) -> str:
    return PREFIJO_FICHA + sha256_texto(f"{SAL_ID_FICHA}|{id_pregunta}|{sha_resp}")[:8]


def label_juez(rep: int) -> str:
    return LABEL_JUEZ.format(rep=rep)


def label_enc(rep: int) -> str:
    return LABEL_ENC.format(rep=rep)


def label_juez_enc(rep: int) -> str:
    return LABEL_JUEZ_ENC.format(rep=rep)
