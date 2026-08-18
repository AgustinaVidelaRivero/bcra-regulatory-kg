"""
comun_corrida.py — Infraestructura común de la CORRIDA de la ablación de
retrieval (U-A1.4, plan de tesis carril A / bloque A1). Todo lo que fija el
pre-registro sellado (`../preregistro_ablacion.md`, commit 68c79dc) se LEE de
los archivos sellados de `..` (celdas/, pares/, manifest) y se verifica por
sha256; nada de eso se edita ni se re-tipea acá.

Provee:
  - rutas propias de la corrida (trazas/, cache/, resultados/, selftest_out/);
  - constantes pre-registradas por REFERENCIA al §4/§5/§6 del pre-registro
    (semillas de orden y bootstrap, nº de remuestreos, umbrales de P1–P6,
    n mínimo por clase, orden de celdas);
  - carga verificada de las celdas (sha de archivo + sha de prompt + sha de
    specs contra `celdas/manifest_celdas.json`) y de los pares
    (`pares/pares_v3.json` contra `pares/manifest_pares_v3.txt`);
  - construcción de casos (par × variante) y orden aleatorio con semilla
    `orden-ablacion-v1` (mismo orden en las 4 celdas);
  - namespace de caché por celda (§4): `agent|gfp=<sha KG-Refinado>|cv=<sha
    harness>+<sha celda>|think=0`;
  - verificación de `KG_Meta.kg_sha256` en el contenedor Neo4j;
  - índice de anclas de KG-Refinado (censo, sin contenedores) para la métrica.
"""

from __future__ import annotations

import hashlib
import json
import random
import sys
from pathlib import Path

CORRIDA_DIR = Path(__file__).resolve().parent               # …/ablacion_retrieval/corrida
ABLACION_DIR = CORRIDA_DIR.parent
if str(ABLACION_DIR) not in sys.path:
    sys.path.insert(0, str(ABLACION_DIR))

from comun_ablacion import (ABLACION_DIR as _ABL, CELDAS_DIR, EVAL_DIR,  # noqa: E402
                            KG_REFINADO_PATH, KG_REFINADO_SHA256, PARES_DIR,
                            PIEZAS_SELLADAS, REPO_DIR, rel_repo, sha256_de,
                            verificar_piezas)
assert _ABL == ABLACION_DIR

import llm_cache as lc  # noqa: E402  (cuarteto: solo import)

# --------------------------------------------------------------------------- #
# Rutas propias                                                                #
# --------------------------------------------------------------------------- #
TRAZAS_DIR = CORRIDA_DIR / "trazas"          # trazas/<celda_id>/<caso>.json (se commitean)
CACHE_DIR = CORRIDA_DIR / "cache"            # dbs por celda (gitignore local)
RESULTADOS_DIR = CORRIDA_DIR / "resultados"  # replay + análisis (se commitean)
SELFTEST_DIR = CORRIDA_DIR / "selftest_out"  # selftest (gitignore local)

# --------------------------------------------------------------------------- #
# Constantes pre-registradas (por referencia al pre-registro sellado)          #
# --------------------------------------------------------------------------- #
UNIDAD = "U-A1.4"
GRAFO = "KG_Refinado"                                     # clave de neo4j/grafos.py
ORDEN_CELDAS = ["C00_booleano_v1", "C10_bm25_v1", "C01_booleano_v2", "C11_bm25_v2"]  # §4
SEMILLA_ORDEN = "orden-ablacion-v1"                       # §4
SEMILLA_BOOTSTRAP = "bootstrap-ablacion-v1"               # §4
N_BOOTSTRAP = 10_000                                      # §4
VARIANTES = ("literal", "antilexica")
ESTRATOS = ("E-A", "E-B", "E-D", "E-E")                   # sin E-C (laudo 2)
COHORTE_DIRIGIDA = {"E-A", "E-B", "E-C", "E-D"}
UMBRALES = {                                              # §5 [LAUDO 4]
    "P1_gate_delta_c": 0.15,
    "P2_factor_brecha": 0.5,
    "P3_margen": 0.05,
    "P5_aditividad": 0.10,
    "P6_margen_vista": 0.10,
    "n_min_pares_clase": 8,
}
MANIFEST_CELDAS = CELDAS_DIR / "manifest_celdas.json"
MANIFEST_PARES = PARES_DIR / "manifest_pares_v3.txt"
PARES_JSON = PARES_DIR / "pares_v3.json"
VALIDACION_JSON = PARES_DIR / "validacion_v3.json"

# Referencia publicada (EV2 base, KG-Refinado; pre-registro §5 y §6). Solo
# agregados publicados: ningún material EV2 se abre (principio 7).
EV2_RESUMEN_V3 = (ABLACION_DIR.parent / "ev2_corrida" / "trazas" / "ev2_base_v3"
                  / "resumen_ev2_base_v3.json")


def sha_texto(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def sha_json(obj) -> str:
    return sha_texto(json.dumps(obj, ensure_ascii=False, sort_keys=True))


# --------------------------------------------------------------------------- #
# Celdas selladas                                                              #
# --------------------------------------------------------------------------- #
def cargar_manifest_celdas() -> dict:
    with MANIFEST_CELDAS.open(encoding="utf-8") as f:
        return json.load(f)


def cargar_celda(celda_id: str, manifest: dict | None = None) -> dict:
    """Carga `celdas/celda_<id>.json` y ABORTA si difiere de lo sellado:
    sha256 del archivo, del prompt del sistema y de las specs (recomputados)
    contra `manifest_celdas.json`. Devuelve el dict de la celda con
    `archivo_sha256` agregado."""
    manifest = manifest or cargar_manifest_celdas()
    if celda_id not in manifest["celdas"]:
        raise KeyError(f"celda desconocida: {celda_id!r}; válidas: {list(manifest['celdas'])}")
    m = manifest["celdas"][celda_id]
    path = ABLACION_DIR / m["archivo"]
    sha_arch = sha256_de(path)
    if sha_arch != m["archivo_sha256"]:
        raise RuntimeError(f"{celda_id}: sha del archivo {sha_arch} != sellado {m['archivo_sha256']}")
    with path.open(encoding="utf-8") as f:
        celda = json.load(f)
    if sha_texto(celda["system_prompt"]) != m["system_prompt_sha256"] \
            or celda["system_prompt_sha256"] != m["system_prompt_sha256"]:
        raise RuntimeError(f"{celda_id}: sha del prompt del sistema no coincide con el manifest")
    if sha_json(celda["tools_specs"]) != m["tools_specs_sha256"] \
            or celda["tools_specs_sha256"] != m["tools_specs_sha256"]:
        raise RuntimeError(f"{celda_id}: sha de las specs no coincide con el manifest")
    if celda["retriever"] != m["retriever"] or celda["tools"] != m["tools"]:
        raise RuntimeError(f"{celda_id}: factores del archivo != manifest")
    if celda["backend"]["kg_sha256"] != KG_REFINADO_SHA256:
        raise RuntimeError(f"{celda_id}: kg_sha256 de la celda != KG-Refinado")
    celda = dict(celda)
    celda["archivo_sha256"] = sha_arch
    celda["archivo"] = m["archivo"]
    return celda


def cargar_celdas() -> dict[str, dict]:
    m = cargar_manifest_celdas()
    if m["orden_celdas"] != ORDEN_CELDAS:
        raise RuntimeError("orden de celdas del manifest != ORDEN_CELDAS pre-registrado")
    return {cid: cargar_celda(cid, m) for cid in ORDEN_CELDAS}


def sha_harness() -> str:
    """sha256 sellado del harness (PIEZAS_SELLADAS), verificado contra el archivo."""
    path, esperado = PIEZAS_SELLADAS["harness.py"]
    actual = sha256_de(path)
    if actual != esperado:
        raise RuntimeError(f"harness.py: sha {actual} != sellado {esperado}")
    return actual


def namespace_celda(celda: dict) -> str:
    """§4: `agent|gfp=<sha KG-Refinado>|cv=<sha harness>+<sha celda>|think=0`
    (armado con `llm_cache.make_namespace`, sin re-tipear el formato)."""
    return lc.make_namespace("agent",
                             code_ver=f"{sha_harness()}+{celda['archivo_sha256']}",
                             graph_fp=KG_REFINADO_SHA256, thinking=False)


# --------------------------------------------------------------------------- #
# Pares sellados y casos                                                       #
# --------------------------------------------------------------------------- #
def _sha_en_manifest_pares(nombre_archivo: str) -> str:
    for linea in MANIFEST_PARES.read_text(encoding="utf-8").splitlines():
        partes = linea.split()
        if len(partes) >= 2 and partes[1].endswith("/" + nombre_archivo):
            return partes[0]
    raise KeyError(f"{nombre_archivo} no está en {rel_repo(MANIFEST_PARES)}")


def cargar_pares(verificar_sha: bool = True) -> list[dict]:
    """Los pares aptos sellados (`pares/pares_v3.json` → `pares`), verificando
    el sha256 del archivo contra `manifest_pares_v3.txt`."""
    if verificar_sha:
        esperado = _sha_en_manifest_pares("pares_v3.json")
        actual = sha256_de(PARES_JSON)
        if actual != esperado:
            raise RuntimeError(f"pares_v3.json: sha {actual} != manifest {esperado}")
    with PARES_JSON.open(encoding="utf-8") as f:
        data = json.load(f)
    if data["config"]["kg_sha256"] != KG_REFINADO_SHA256:
        raise RuntimeError("pares_v3.json: kg_sha256 != KG-Refinado")
    return data["pares"]


def cargar_validacion() -> dict:
    esperado = _sha_en_manifest_pares("validacion_v3.json")
    actual = sha256_de(VALIDACION_JSON)
    if actual != esperado:
        raise RuntimeError(f"validacion_v3.json: sha {actual} != manifest {esperado}")
    with VALIDACION_JSON.open(encoding="utf-8") as f:
        return json.load(f)


def huerfanos_p6() -> dict[str, list[str]]:
    """{sample_id: [ids de nodos gold huérfanos de label]} marcados ex-ante
    (`validacion_v3.json` → `huerfanos_p6.por_par`)."""
    v = cargar_validacion()["huerfanos_p6"]
    return {sid: [h["nodo"] for h in lista] for sid, lista in v["por_par"].items()}


def construir_casos(pares: list[dict]) -> list[dict]:
    """(par × variante): id `<sample_id>::<variante>` (patrón EV2)."""
    casos = []
    for p in pares:
        for variante in VARIANTES:
            casos.append({"caso_id": f"{p['sample_id']}::{variante}",
                          "sample_id": p["sample_id"], "variante": variante,
                          "estrato": p["estrato"], "sub_estrato": p.get("sub_estrato"),
                          "pregunta": p[variante]})
    return casos


def orden_resuelto(pares: list[dict]) -> list[dict]:
    """Orden de corrida (§4): casos ordenados por caso_id, luego
    `random.Random('orden-ablacion-v1').shuffle` — idéntico en las 4 celdas."""
    casos = sorted(construir_casos(pares), key=lambda c: c["caso_id"])
    random.Random(SEMILLA_ORDEN).shuffle(casos)
    for i, c in enumerate(casos, 1):
        c["pos_orden"] = i
    return casos


def sanitizar(caso_id: str) -> str:
    return caso_id.replace("::", "__")


# --------------------------------------------------------------------------- #
# Neo4j: verificación del grafo cargado                                        #
# --------------------------------------------------------------------------- #
def verificar_kg_meta(driver, grafo: str = GRAFO) -> dict:
    """Aborta si `KG_Meta.kg_sha256` del contenedor != sha de KG-Refinado."""
    with driver.session() as s:
        rec = s.run("MATCH (m:KG_Meta {grafo: $g}) RETURN properties(m) AS p", g=grafo).single()
    meta = rec["p"] if rec else None
    if not meta or meta.get("kg_sha256") != KG_REFINADO_SHA256:
        raise RuntimeError(f"KG_Meta de {grafo} ausente o con sha distinto: {meta}")
    return meta


# --------------------------------------------------------------------------- #
# Censo de anclas en KG-Refinado (métrica por ancla)                           #
# --------------------------------------------------------------------------- #
def indice_anclas_refinado():
    """AnclaIndex (resolucion.py, sin editar) sobre el kg.json crudo de
    KG-Refinado con sha verificado (contenedores excluidos por defecto)."""
    from comun import load_kg_raw  # sinteticas
    from resolucion import AnclaIndex
    return AnclaIndex(load_kg_raw(KG_REFINADO_PATH, verificar_sha=True))


def kg_vacio_refinado():
    """KnowledgeGraph vacío con `.path` = KG-Refinado (para graph_fingerprint
    de llm_cache y para el __init__ del harness, patrón agente_v2)."""
    from loader import KnowledgeGraph
    return KnowledgeGraph(run_key=f"ablacion:{GRAFO}", path=KG_REFINADO_PATH,
                          nodes=[], edges=[], raw_node_count=0, raw_edge_count=0, merges=[])


if __name__ == "__main__":
    print("piezas selladas:")
    verificar_piezas()
    celdas = cargar_celdas()
    print("celdas OK:", {k: v["archivo_sha256"][:12] for k, v in celdas.items()})
    pares = cargar_pares()
    orden = orden_resuelto(pares)
    print(f"pares {len(pares)} → casos {len(orden)}; primeros 5 del orden {SEMILLA_ORDEN}:",
          [c["caso_id"] for c in orden[:5]])
    print("namespace C00:", namespace_celda(celdas["C00_booleano_v1"]))
    print("huérfanos P6:", {k: len(v) for k, v in huerfanos_p6().items()})
