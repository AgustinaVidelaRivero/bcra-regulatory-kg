#!/usr/bin/env python3
"""controles_a2_2.py — Los controles externos de A2.2, a USD 0, antes de cada paso:

  · los índices de fragmentos (registro, §16, `:545`: «El despacho de A2.2 controla al empezar los sha de los índices de
    mcp_vector/indice/»): el sha256 de cada uno de los 9 archivos de mcp_vector/indice/ contra el de su respaldo (registro, §51,
    `:1799-1801`; `fuera_del_repo/indices_banco/fragmentos_e0_r2b_desarrollo_A2_1/mcp_vector_indice/manifest_respaldo.txt`,
    verificado por la mesa el 19/10/2026), que se copian acá; el del índice BM25 contra el de su configuración; y el de la matriz
    densa (sus bytes float32, como lo calcula `mcp_vector/servidor_mcp_vector.py:136`) contra el de la suya. Si el respaldo está
    en esta máquina, también se compara contra su manifiesto;
  · el grafo en Neo4j (pre-registro, §2, la precondición de A2.1, `:80-81`): KG_Meta del grafo de desarrollo re-sellado con el
    sha256 sellado (`acb26dca…`), sus nodos y aristas, la cantidad de nodos con su label y el índice full-text en línea. El
    usuario y la contraseña son los del contenedor local de desarrollo (`data/experiment/neo4j/conexion.py`).

Imprime solo OK o FRENO por control. Uso: .venv/bin/python -B data/experiment/banco_mcp/a2_2/controles_a2_2.py [--sin-neo4j]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))
import comun_a2_2 as K  # noqa: E402

INDICE_DIR = K.BANCO_DIR / "mcp_vector" / "indice"
RESPALDO = (Path.home() / "INGENIERIA IA" / "TESIS" / "fuera_del_repo" / "indices_banco" / "fragmentos_e0_r2b_desarrollo_A2_1"
            / "mcp_vector_indice" / "manifest_respaldo.txt")
INDICES = {   # el manifest_respaldo.txt de la mesa, tal cual
    "e0_r2b_desarrollo_bm25/indice_bm25.json": "6b5da8b0940e6ae46214b93c541b384a710eb35688264c0138df2e7b4773fc25",
    "e0_r2b_desarrollo_bm25/manifiesto_indice.json": "e30cb7c6552345055f29f9f61df81878409c9a4d5c888f083632967d8224ecca",
    "e0_r2b_desarrollo_bm25/pasajes.json": "d8faf4d2e353658e2764a38ad42c7b3533716923d4e2a8474e69677667cfd543",
    "e0_r2b_desarrollo_denso/embeddings_docs.npy": "4f77eb5cc939b1ca6c35237837b6e7c639d85908298f2ae1cc56774c5a0e48dd",
    "e0_r2b_desarrollo_denso/manifiesto_indice.json": "378e26a25111e874ac7b4712b3e86a65cc317964c6ceb023a356c2d4c8c86c8c",
    "e0_r2b_desarrollo_denso/pasajes.json": "d8faf4d2e353658e2764a38ad42c7b3533716923d4e2a8474e69677667cfd543",
    "embeddings_docs.npy": "c317cd60b402f93d14e16fbefc1da0e7755cca7794f8dca38f3024b67a44b882",
    "manifiesto_indice.json": "56cc004b859985016194397a5e23ad179f9518b3bacc058385812125321de7a1",
    "pasajes.json": "62debe8d8a4c33dd1e6ffce8b1ead5c69a38024ca165c58961955e014ba6cf1d",
}
GRAFO, KG_SHA256, N_NODOS, N_ARISTAS = "KG_Tanda0_Desarrollo_r2b_rs1", "acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31", 6962, 23311
INDICE_FULLTEXT = "nodos_fulltext_kg_tanda0_desarrollo_r2b_rs1"


def verificar_indices(indice_dir: Path = INDICE_DIR, respaldo: Path = RESPALDO) -> dict:
    archivos = sorted(str(p.relative_to(indice_dir)) for p in indice_dir.rglob("*") if p.is_file() and p.name != ".DS_Store")
    if archivos != sorted(INDICES):
        raise K.FrenoA22("mcp_vector/indice/ no tiene los 9 archivos del respaldo")
    mal = [r for r in INDICES if K.sha256_file(indice_dir / r) != INDICES[r]]
    if mal:
        raise K.FrenoA22(f"{len(mal)} archivos de mcp_vector/indice/ no dan el sha256 del respaldo")
    bm = json.loads((K.BANCO_DIR / "mcp_vector" / "config_fragmentos_bm25_r2b.json").read_text(encoding="utf-8"))
    de = json.loads((K.BANCO_DIR / "mcp_vector" / "config_fragmentos_denso_r2b.json").read_text(encoding="utf-8"))
    if INDICES["e0_r2b_desarrollo_bm25/indice_bm25.json"] != bm["sha256_indice_esperado"]:
        raise K.FrenoA22("el índice BM25 no es el de su configuración")
    out = {"n_archivos": len(INDICES), "iguales_al_respaldo": True, "bm25_igual_a_su_config": True}
    try:
        import numpy as np
        E = np.load(indice_dir / "e0_r2b_desarrollo_denso" / "embeddings_docs.npy")
        sha_m = hashlib.sha256(E.astype("float32").tobytes(order="C")).hexdigest()
        if sha_m != de["sha256_matriz_esperado"]:
            raise K.FrenoA22("la matriz densa no es la de su configuración")
        out["matriz_densa_igual_a_su_config"] = True
    except ImportError:
        out["matriz_densa_igual_a_su_config"] = "sin numpy en este intérprete: la controla el servidor al arrancar"
    if respaldo.is_file():
        filas = {l.split()[1]: l.split()[0] for l in respaldo.read_text(encoding="utf-8").splitlines()
                 if l.strip() and not l.startswith("#")}
        if filas != INDICES:
            raise K.FrenoA22("el manifiesto del respaldo no es el que copia este control")
        out["manifiesto_del_respaldo"] = "igual"
    else:
        out["manifiesto_del_respaldo"] = "no está en esta máquina"
    return out


def verificar_neo4j() -> dict:
    neo = K.EXP_DIR / "neo4j"
    if str(neo) not in sys.path:
        sys.path.insert(0, str(neo))
    from conexion import abrir_driver  # noqa: PLC0415
    try:
        driver = abrir_driver()
    except Exception as e:  # noqa: BLE001
        raise K.FrenoA22(f"Neo4j no responde ({type(e).__name__}): levantar el contenedor y cargar el grafo")
    try:
        with driver.session() as s:
            meta = s.run("MATCH (m:KG_Meta {grafo: $g}) RETURN m.kg_sha256 AS sha, m.n_nodos AS n, m.n_aristas AS a",
                         g=GRAFO).single()
            n_label = s.run(f"MATCH (n:`{GRAFO}`) RETURN count(n) AS c").single()["c"]
            idx = s.run("SHOW FULLTEXT INDEXES YIELD name, state WHERE name = $i RETURN state", i=INDICE_FULLTEXT).single()
    finally:
        driver.close()
    if meta is None or meta["sha"] != KG_SHA256 or meta["n"] != N_NODOS or meta["a"] != N_ARISTAS:
        raise K.FrenoA22("el grafo cargado en Neo4j no es el de desarrollo re-sellado")
    if n_label != N_NODOS:
        raise K.FrenoA22("Neo4j no tiene todos los nodos del grafo de desarrollo re-sellado")
    if idx is None or idx["state"] != "ONLINE":
        raise K.FrenoA22("el índice full-text del grafo de desarrollo re-sellado no está en línea")
    return {"grafo": GRAFO, "kg_sha256": KG_SHA256, "n_nodos": N_NODOS, "n_aristas": N_ARISTAS,
            "indice_fulltext": INDICE_FULLTEXT, "estado_indice": "ONLINE"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sin-neo4j", action="store_true")
    a = ap.parse_args()
    ok = True
    for nombre, fn in (("índices de fragmentos", verificar_indices), ("grafo en Neo4j", verificar_neo4j)):
        if nombre == "grafo en Neo4j" and a.sin_neo4j:
            continue
        try:
            r = fn()
            print("OK    ", nombre, json.dumps(r, ensure_ascii=False))
        except K.FrenoA22 as e:
            ok = False
            print("FRENO ", nombre, "—", e)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
