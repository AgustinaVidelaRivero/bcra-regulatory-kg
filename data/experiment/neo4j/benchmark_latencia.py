"""
benchmark_latencia.py — Latencia de buscar_nodos: in-memory vs Neo4j.

Consultas: las 50 más frecuentes extraídas de las llamadas reales a
buscar_nodos en data/experiment/evaluacion/posthoc_run/traces/ (5.173
llamadas, 2.409 únicas — la frecuencia pondera la carga de trabajo real).

Backends medidos (misma consulta, 50 repeticiones por consulta por backend,
3 repeticiones de warmup descartadas):
  a) in-memory     — GraphIndex.buscar_nodos del harness (import, sin editar).
  b) neo4j-fulltext— Neo4jIndex.buscar_nodos (índice Lucene nodos_fulltext).
  c) neo4j-label   — lookup exacto por label con índice RANGE nodo_label:
                     piso de round-trip bolt + b-tree, para separar el costo
                     de red/protocolo del costo del scoring full-text.

Métricas: mediana y p95 en ms sobre TODAS las mediciones (consulta × rep),
más el rango de medianas por consulta. Salida: tabla en stdout + detalle en
benchmark_resultados.json (junto a este script).

Nota metodológica: (a) corre en el mismo proceso Python (sin red); (b) y (c)
pagan round-trip bolt a localhost. Es la comparación relevante para decidir
la migración: el agente pagaría ese round-trip en cada tool call.
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
EVAL_DIR = NEO4J_DIR.parent / "evaluacion"
sys.path.insert(0, str(EVAL_DIR))
sys.path.insert(0, str(NEO4J_DIR))

from loader import load_graph_from_path  # noqa: E402
from harness import GraphIndex  # noqa: E402
from conexion import abrir_driver  # noqa: E402
from neo4j_index import Neo4jIndex  # noqa: E402
from cargar_kg import KG_PATH  # noqa: E402

TRACES_DIR = EVAL_DIR / "posthoc_run" / "traces"
SALIDA_JSON = NEO4J_DIR / "benchmark_resultados.json"

N_CONSULTAS = 50
N_REPS = 50
N_WARMUP = 3


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


def medir(fn, consultas) -> dict:
    """50 reps por consulta (3 warmup descartadas). Tiempos en ms."""
    tiempos_globales, medianas_por_consulta = [], []
    for q in consultas:
        for _ in range(N_WARMUP):
            fn(q)
        ts = []
        for _ in range(N_REPS):
            t0 = time.perf_counter()
            fn(q)
            ts.append((time.perf_counter() - t0) * 1000.0)
        tiempos_globales.extend(ts)
        medianas_por_consulta.append(statistics.median(ts))
    tiempos_globales.sort()
    n = len(tiempos_globales)
    return {
        "n_mediciones": n,
        "mediana_ms": round(statistics.median(tiempos_globales), 3),
        "p95_ms": round(tiempos_globales[min(n - 1, int(n * 0.95))], 3),
        "mediana_por_consulta_min_ms": round(min(medianas_por_consulta), 3),
        "mediana_por_consulta_max_ms": round(max(medianas_por_consulta), 3),
    }


def main():
    consultas = extraer_consultas()
    print(f"consultas del benchmark: {len(consultas)} (top frecuencia, "
          f"{N_REPS} reps c/u + {N_WARMUP} warmup)")

    kg = load_graph_from_path(KG_PATH, adapter_key=None)
    gi = GraphIndex(kg)
    driver = abrir_driver()
    ni = Neo4jIndex(driver)

    # Índice RANGE para el baseline de label exacto (idempotente).
    with driver.session() as session:
        session.run("CREATE INDEX nodo_label IF NOT EXISTS "
                    "FOR (n:Nodo) ON (n.label)").consume()
        session.run("CALL db.awaitIndexes(300)").consume()

    def label_exacto(q):
        with driver.session() as session:
            return session.run(
                "MATCH (n:Nodo) WHERE n.label = $q "
                "RETURN n.id, n.type, n.label LIMIT 10", q=q,
            ).data()

    resultados = {}
    try:
        for nombre, fn in [
            ("in-memory (GraphIndex)", lambda q: gi.buscar_nodos(q)),
            ("neo4j full-text (Neo4jIndex)", lambda q: ni.buscar_nodos(q)),
            ("neo4j label exacto (RANGE)", label_exacto),
        ]:
            print(f"  midiendo: {nombre} …")
            resultados[nombre] = medir(fn, consultas)
    finally:
        driver.close()

    print(f"\n{'backend':32s} {'N':>6s} {'mediana':>9s} {'p95':>9s} "
          f"{'med.min':>9s} {'med.max':>9s}")
    for nombre, r in resultados.items():
        print(f"{nombre:32s} {r['n_mediciones']:6d} {r['mediana_ms']:8.3f}m "
              f"{r['p95_ms']:8.3f}m {r['mediana_por_consulta_min_ms']:8.3f}m "
              f"{r['mediana_por_consulta_max_ms']:8.3f}m")

    SALIDA_JSON.write_text(
        json.dumps({"consultas": consultas, "config": {
            "n_consultas": len(consultas), "n_reps": N_REPS,
            "n_warmup": N_WARMUP},
            "resultados": resultados}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\ndetalle -> {SALIDA_JSON.name}")


if __name__ == "__main__":
    main()
