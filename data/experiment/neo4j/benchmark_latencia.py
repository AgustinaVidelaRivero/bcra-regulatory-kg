"""
benchmark_latencia.py — Latencia por tool y backend (SOLO registro; sin conclusiones).

Bloque 1 (heredado de c26cb9b, se conserva): buscar_nodos sobre KG-Refinado con
las 50 consultas reales más frecuentes de las trazas posthoc
(data/experiment/evaluacion/posthoc_run/traces/), 50 reps + 3 warmup, backends:
  a) in-memory        — GraphIndex.buscar_nodos del harness (import, sin editar).
  b) neo4j-fulltext   — Neo4jIndex(modo='fulltext').buscar_nodos (Lucene por grafo).
  c) neo4j-paridad    — Neo4jIndex(modo='paridad').buscar_nodos (NUEVO en A1.1).
  d) neo4j-label      — lookup exacto por label con índice RANGE (piso de
                        round-trip bolt + b-tree).

Bloque 2 (A1.1): los CASOS DEL SELFTEST (test_equivalencia.py: heredados +
generados + borde + BKL), por tool × grafo × backend, 20 reps + 3 warmup por
caso. Backends por tool:
  buscar_nodos : in-memory / neo4j-paridad / neo4j-fulltext
  ver_nodo     : in-memory / neo4j (mismo código en ambos modos: se mide una vez)
  ver_vecinos  : in-memory / neo4j (ídem)

Métricas: mediana y p95 en ms sobre TODAS las mediciones (caso × rep), más el
rango de medianas por caso. Salida: tablas en stdout + detalle en
benchmark_resultados_A11.json (junto a este script). El archivo
benchmark_resultados.json de c26cb9b se CONSERVA intacto.

Nota metodológica: (a) corre en el mismo proceso Python (sin red); los backends
Neo4j pagan round-trip bolt a localhost (contenedor Docker en la misma máquina).
La varianza run-to-run observada en c26cb9b fue ~±20 % en la mediana del
full-text: los decimales no deben sobre-interpretarse.
"""

from __future__ import annotations

import collections
import glob
import json
import statistics
import sys
import time
from pathlib import Path

NEO4J_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(NEO4J_DIR))

from grafos import GRAFOS, CLAVES, EVAL_DIR, cargar_vista_runtime  # noqa: E402
from harness import GraphIndex  # noqa: E402  (solo IMPORT)
from conexion import abrir_driver  # noqa: E402
from neo4j_index import Neo4jIndex  # noqa: E402
from cargar_kg import KG_PATH  # noqa: E402,F401  (compatibilidad c26cb9b)
from test_equivalencia import (  # noqa: E402
    CASOS_VER_NODO, CASOS_VER_VECINOS, CASOS_BUSCAR, CASOS_BUSCAR_BORDE,
    NODO_BKL0027, NODO_BKL0022, HUB_BKL0022, casos_generados, _DEF,
)

TRACES_DIR = EVAL_DIR / "posthoc_run" / "traces"
SALIDA_JSON = NEO4J_DIR / "benchmark_resultados_A11.json"

N_CONSULTAS = 50
N_REPS = 50
N_WARMUP = 3
N_REPS_SELFTEST = 20


def extraer_consultas() -> list:
    """Top-N consultas reales por frecuencia (desempate alfabético estable)."""
    consultas = collections.Counter()
    for a in glob.glob(str(TRACES_DIR / "**" / "*.json"), recursive=True):
        try:
            with open(a, encoding="utf-8") as f:
                d = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue
        for rec in (d if isinstance(d, list) else [d]):
            for s in (rec.get("trace") or {}).get("steps", []):
                if s.get("tool") == "buscar_nodos":
                    c = (s.get("input") or {}).get("consulta")
                    if c:
                        consultas[c] += 1
    orden = sorted(consultas.items(), key=lambda kv: (-kv[1], kv[0]))
    return [c for c, _ in orden[:N_CONSULTAS]]


def medir(fn, casos, n_reps=N_REPS, n_warmup=N_WARMUP) -> dict:
    """n_reps por caso (n_warmup descartadas). Tiempos en ms."""
    tiempos_globales, medianas_por_caso = [], []
    for c in casos:
        for _ in range(n_warmup):
            fn(c)
        ts = []
        for _ in range(n_reps):
            t0 = time.perf_counter()
            fn(c)
            ts.append((time.perf_counter() - t0) * 1000.0)
        tiempos_globales.extend(ts)
        medianas_por_caso.append(statistics.median(ts))
    tiempos_globales.sort()
    n = len(tiempos_globales)
    return {
        "n_casos": len(casos),
        "n_reps": n_reps,
        "n_mediciones": n,
        "mediana_ms": round(statistics.median(tiempos_globales), 3),
        "p95_ms": round(tiempos_globales[min(n - 1, int(n * 0.95))], 3),
        "mediana_por_caso_min_ms": round(min(medianas_por_caso), 3),
        "mediana_por_caso_max_ms": round(max(medianas_por_caso), 3),
    }


def _tabla(titulo, resultados):
    print(f"\n{titulo}")
    print(f"{'backend':44s} {'casos':>5s} {'N':>6s} {'mediana':>9s} {'p95':>9s} "
          f"{'med.min':>9s} {'med.max':>9s}")
    for nombre, r in resultados.items():
        print(f"{nombre:44s} {r['n_casos']:5d} {r['n_mediciones']:6d} {r['mediana_ms']:8.3f}m "
              f"{r['p95_ms']:8.3f}m {r['mediana_por_caso_min_ms']:8.3f}m "
              f"{r['mediana_por_caso_max_ms']:8.3f}m")


def bloque1(driver) -> dict:
    consultas = extraer_consultas()
    print(f"[bloque 1] consultas reales: {len(consultas)} (top frecuencia, "
          f"{N_REPS} reps c/u + {N_WARMUP} warmup) sobre KG_Refinado")
    kg = cargar_vista_runtime("KG_Refinado")
    gi = GraphIndex(kg)
    n_ft = Neo4jIndex(driver, grafo="KG_Refinado", modo="fulltext")
    n_par = Neo4jIndex(driver, grafo="KG_Refinado", modo="paridad")
    with driver.session() as session:
        session.run("CREATE INDEX nodo_label IF NOT EXISTS "
                    "FOR (n:Nodo) ON (n.label)").consume()
        session.run("CALL db.awaitIndexes(300)").consume()

    def label_exacto(q):
        with driver.session() as session:
            return session.run(
                "MATCH (n:KG_Refinado) WHERE n.label = $q "
                "RETURN n.id, n.type, n.label LIMIT 10", q=q,
            ).data()

    resultados = {}
    for nombre, fn in [
        ("in-memory (GraphIndex)", lambda q: gi.buscar_nodos(q)),
        ("neo4j full-text (Neo4jIndex modo=fulltext)", lambda q: n_ft.buscar_nodos(q)),
        ("neo4j paridad (Neo4jIndex modo=paridad)", lambda q: n_par.buscar_nodos(q)),
        ("neo4j label exacto (RANGE)", label_exacto),
    ]:
        print(f"  midiendo: {nombre} …")
        resultados[nombre] = medir(fn, consultas)
    _tabla("[bloque 1] buscar_nodos, 50 consultas reales, KG_Refinado (ms)", resultados)
    return {"consultas": consultas,
            "config": {"n_consultas": len(consultas), "n_reps": N_REPS, "n_warmup": N_WARMUP},
            "resultados": resultados}


def bloque2(driver) -> dict:
    salida = {}
    for clave in CLAVES:
        kg = cargar_vista_runtime(clave)
        gi = GraphIndex(kg)
        n_par = Neo4jIndex(driver, grafo=clave, modo="paridad")
        n_ft = Neo4jIndex(driver, grafo=clave, modo="fulltext")
        gen = casos_generados(kg, clave)

        casos_nodo = [nid for _, nid in gen["ver_nodo"]]
        casos_vec = [(nid, d, lim) for _, nid, d, lim in gen["ver_vecinos"]]
        casos_bus = [(q, lim) for _, q, lim in CASOS_BUSCAR_BORDE] + [(q, _DEF) for _, q in gen["buscar"]]
        if clave == "KG_Refinado":
            casos_nodo = CASOS_VER_NODO + casos_nodo
            casos_vec = [(nid, d, _DEF) for nid, d in CASOS_VER_VECINOS] + casos_vec + [
                (NODO_BKL0027, "salientes", _DEF), (NODO_BKL0027, "entrantes", _DEF),
                (HUB_BKL0022, "entrantes", _DEF)]
            casos_bus = [(q, _DEF) for q in CASOS_BUSCAR] + casos_bus + [
                (gi.by_id[NODO_BKL0022].label, _DEF)]

        def f_bus(idx):
            return lambda c: (idx.buscar_nodos(c[0]) if c[1] is _DEF else idx.buscar_nodos(c[0], c[1]))

        def f_vec(idx):
            return lambda c: (idx.ver_vecinos(c[0], direccion=c[1]) if c[2] is _DEF
                              else idx.ver_vecinos(c[0], direccion=c[1], limite=c[2]))

        res = {}
        print(f"\n[bloque 2] {clave}: {len(casos_bus)} buscar_nodos / {len(casos_nodo)} ver_nodo / "
              f"{len(casos_vec)} ver_vecinos; {N_REPS_SELFTEST} reps + {N_WARMUP} warmup")
        for nombre, fn, casos in [
            ("buscar_nodos | in-memory", f_bus(gi), casos_bus),
            ("buscar_nodos | neo4j paridad", f_bus(n_par), casos_bus),
            ("buscar_nodos | neo4j fulltext", f_bus(n_ft), casos_bus),
            ("ver_nodo | in-memory", lambda c: gi.ver_nodo(c), casos_nodo),
            ("ver_nodo | neo4j (ambos modos)", lambda c: n_par.ver_nodo(c), casos_nodo),
            ("ver_vecinos | in-memory", f_vec(gi), casos_vec),
            ("ver_vecinos | neo4j (ambos modos)", f_vec(n_par), casos_vec),
        ]:
            print(f"  midiendo: {nombre} …")
            res[nombre] = medir(fn, casos, n_reps=N_REPS_SELFTEST)
        _tabla(f"[bloque 2] casos del selftest, {clave} (ms)", res)
        salida[clave] = {"n_casos": {"buscar_nodos": len(casos_bus), "ver_nodo": len(casos_nodo),
                                     "ver_vecinos": len(casos_vec)},
                         "config": {"n_reps": N_REPS_SELFTEST, "n_warmup": N_WARMUP},
                         "resultados": res}
    return salida


def main():
    driver = abrir_driver()
    try:
        b1 = bloque1(driver)
        b2 = bloque2(driver)
    finally:
        driver.close()
    SALIDA_JSON.write_text(
        json.dumps({"bloque1_consultas_reales_kg_refinado": b1,
                    "bloque2_casos_selftest": b2,
                    "grafos": {k: {"sha256": v["sha256"], "n_nodos": v["n_nodos"],
                                   "n_aristas": v["n_aristas"]} for k, v in GRAFOS.items()},
                    "nota": "solo registro de latencias; sin conclusiones"},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\ndetalle -> {SALIDA_JSON.name}")


if __name__ == "__main__":
    main()
