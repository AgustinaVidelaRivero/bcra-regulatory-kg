"""
latencia_tools_v2.py — Latencia INFORMATIVA por tool, v1 vs v2, sobre los casos
del selftest (U-A1.2). Solo registro; sin conclusiones. Sin API, USD 0.

Backends medidos por tool:
  v1 in-memory   : GraphIndex del harness (lo que corre hoy en el pipeline).
  v1 neo4j       : Neo4jIndex modo 'paridad' de A1.1 (mismas tools v1 sobre Neo4j;
                   ver_nodo/ver_vecinos son idénticos en ambos modos).
  v2             : ToolsV2 (buscar_nodos_v2 = fulltext; ver_vecinos_v2 bidireccional
                   paginada; ver_nodo_v2 adaptador).
Los casos de ver_vecinos v2 miden la llamada bidireccional completa (página 1,
40 por dirección) — que devuelve MÁS que la v1 'ambas' cuando hay metadatos por
relación; el tamaño del payload (chars serializados) se registra junto a la
latencia para que la comparación sea legible.

Salida: latencia_tools_v2_resultados.json (los tiempos NO son determinísticos;
los tamaños de payload sí).
"""

from __future__ import annotations

import json
import statistics
import sys
import time
from pathlib import Path

AGENTE_V2_DIR = Path(__file__).resolve().parent
NEO4J_DIR = AGENTE_V2_DIR.parent / "neo4j"
for _p in (str(NEO4J_DIR), str(AGENTE_V2_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from grafos import GRAFOS, CLAVES, cargar_vista_runtime  # noqa: E402
from conexion import abrir_driver  # noqa: E402
from harness import GraphIndex  # noqa: E402
from neo4j_index import Neo4jIndex  # noqa: E402
from tools_v2 import ToolsV2  # noqa: E402
from selftest_tools_v2 import (CASOS_BUSQUEDA, NODO_BKL0027, NODO_BKL0022, HUB_BKL0022,  # noqa: E402
                               NODO_BKL0003, REL_BKL0027, Derivado, ser)

REPS = 20
WARMUP = 2
SALIDA = AGENTE_V2_DIR / "latencia_tools_v2_resultados.json"


def medir(fn, reps=REPS) -> dict:
    for _ in range(WARMUP):
        r = fn()
    ts = []
    for _ in range(reps):
        t0 = time.perf_counter()
        r = fn()
        ts.append((time.perf_counter() - t0) * 1000.0)
    ts.sort()
    return {"mediana_ms": round(statistics.median(ts), 3), "p95_ms": round(ts[int(len(ts) * 0.95) - 1], 3),
            "min_ms": round(ts[0], 3), "max_ms": round(ts[-1], 3), "payload_chars": len(ser(r))}


def agregar(filas: list) -> dict:
    meds = [f["mediana_ms"] for f in filas]
    p95 = [f["p95_ms"] for f in filas]
    return {"casos": len(filas), "mediana_de_medianas_ms": round(statistics.median(meds), 3),
            "p95_de_p95_ms": round(max(p95), 3) if p95 else None,
            "med_min_ms": round(min(meds), 3), "med_max_ms": round(max(meds), 3),
            "payload_chars_mediana": statistics.median([f["payload_chars"] for f in filas])}


def main():
    driver = abrir_driver()
    salida = {"unidad": "U-A1.2", "reps": REPS, "warmup": WARMUP, "por_grafo": {}}
    for clave in CLAVES:
        kg = cargar_vista_runtime(clave)
        der = Derivado(kg)
        gi = GraphIndex(kg)
        ni = Neo4jIndex(driver, grafo=clave, modo="paridad")
        t2 = ToolsV2(driver, grafo=clave)
        print(f"\n######## {clave} ########")
        # --- casos ---
        consultas = []
        for caso, spec in CASOS_BUSQUEDA.items():
            consultas.extend(spec["consultas"])
        if NODO_BKL0022 in der.by_id:
            lab = der.by_id[NODO_BKL0022].label
            consultas.extend(lab.split() + [lab, "grupo 2"])
        ids_nodo = [x for x in (NODO_BKL0027, NODO_BKL0022, HUB_BKL0022, NODO_BKL0003, der.hub_max("entrantes")) if x in der.by_id]
        casos_vec = [(nid, None) for nid in (NODO_BKL0027, HUB_BKL0022, der.hub_max("entrantes"), der.hub_max("salientes")) if nid in der.by_id]
        casos_vec += [(NODO_BKL0027, REL_BKL0027), (HUB_BKL0022, "subclase_de")]
        casos_vec = [c for c in casos_vec if c[0] in der.by_id]

        res = {"buscar_nodos": {"v1_inmemory": [], "v1_neo4j_paridad": [], "v2_fulltext": []},
               "ver_nodo": {"v1_inmemory": [], "v1_neo4j": [], "v2": []},
               "ver_vecinos": {"v1_inmemory_ambas": [], "v1_neo4j_ambas": [], "v2_bidireccional_p1": [], "v2_bidireccional_filtro": []}}
        for c in consultas:
            res["buscar_nodos"]["v1_inmemory"].append({"caso": c, **medir(lambda: gi.buscar_nodos(c))})
            res["buscar_nodos"]["v1_neo4j_paridad"].append({"caso": c, **medir(lambda: ni.buscar_nodos(c))})
            res["buscar_nodos"]["v2_fulltext"].append({"caso": c, **medir(lambda: t2.buscar_nodos_v2(c))})
        for nid in ids_nodo:
            res["ver_nodo"]["v1_inmemory"].append({"caso": nid, **medir(lambda: gi.ver_nodo(nid))})
            res["ver_nodo"]["v1_neo4j"].append({"caso": nid, **medir(lambda: ni.ver_nodo(nid))})
            res["ver_nodo"]["v2"].append({"caso": nid, **medir(lambda: t2.ver_nodo_v2(nid))})
        for nid, rel in casos_vec:
            if rel is None:
                res["ver_vecinos"]["v1_inmemory_ambas"].append({"caso": nid, **medir(lambda: gi.ver_vecinos(nid))})
                res["ver_vecinos"]["v1_neo4j_ambas"].append({"caso": nid, **medir(lambda: ni.ver_vecinos(nid))})
                res["ver_vecinos"]["v2_bidireccional_p1"].append({"caso": nid, **medir(lambda: t2.ver_vecinos_v2(nid))})
            else:
                res["ver_vecinos"]["v2_bidireccional_filtro"].append({"caso": f"{nid}|{rel}", **medir(lambda: t2.ver_vecinos_v2(nid, relacion=rel))})
        agg = {tool: {b: agregar(f) for b, f in bk.items() if f} for tool, bk in res.items()}
        for tool, bk in agg.items():
            for b, a in bk.items():
                print(f"  {tool:12s} {b:26s} casos={a['casos']:3d} mediana={a['mediana_de_medianas_ms']:8.3f} ms  p95={a['p95_de_p95_ms']:8.3f}  payload_med={a['payload_chars_mediana']}")
        salida["por_grafo"][clave] = {"agregado": agg, "detalle": res}
    driver.close()
    SALIDA.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nsalida: {SALIDA}")


if __name__ == "__main__":
    main()
