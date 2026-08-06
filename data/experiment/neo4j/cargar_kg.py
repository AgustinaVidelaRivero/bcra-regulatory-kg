"""
cargar_kg.py — Carga del grafo vigente (reensamblado_v3) en Neo4j Community.

Lee el kg.json vía `load_graph_from_path` del loader de evaluación (solo
IMPORT: el cuarteto hasheado no se edita) y lo vuelca a Neo4j. El kg.json es
read-only; antes de cargar se verifica su sha256 contra el valor sellado.

Modelo de datos en Neo4j
------------------------
- Cada nodo lleva el label común :Nodo (habilita la constraint de unicidad de
  id y las queries globales) más un label por su `type` (:Obligacion, :Sujeto,
  etc. — 7 tipos).
- Propiedades del nodo: `id`, `type`, `label` + las properties semánticas
  aplanadas con su nombre original (verificado: sin colisiones con id/type/
  label; valores str, bool o list[str] — todos tipos nativos de Neo4j).
  Además se guardan dos propiedades JSON canónicas:
    * `props_json`        — json.dumps de la dict `properties` normalizada por
                            el loader (fuente exacta de reconstrucción para el
                            adaptador de tools; el aplanado es para indexación
                            y consulta ad-hoc).
    * `provenances_json`  — json.dumps de la lista `provenances` normalizada.
- Cada arista se crea con su `relation` como tipo de relationship (16 tipos,
  todos identificadores válidos), con `provenances_json` (las aristas de este
  grafo no tienen properties semánticas tras el loader; se verificó vacío).

Decisión de adaptador: adapter_key=None (adaptador nulo), la MISMA convención
con la que la app registra reensamblado_v3 (app/main.py): el loader pliega solo
la `provenance` primaria; la lista acumulada `provenances` del JSON crudo y
`rol_fuente` no llegan al harness (paridad de interfaz). Neo4j almacena la
vista del loader — exactamente lo que ve el GraphIndex in-memory — para que la
equivalencia de tools sea comparable 1:1.

Uso
---
  python cargar_kg.py                  # verifica sha, borra la db y carga todo
  python cargar_kg.py --solo-verificar # solo conteos + muestreo (sin recargar)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

NEO4J_DIR = Path(__file__).resolve().parent
EXPERIMENT_DIR = NEO4J_DIR.parent
EVAL_DIR = EXPERIMENT_DIR / "evaluacion"
sys.path.insert(0, str(EVAL_DIR))
sys.path.insert(0, str(NEO4J_DIR))

from loader import load_graph_from_path  # noqa: E402
from conexion import abrir_driver  # noqa: E402

KG_PATH = EXPERIMENT_DIR / "grafo_v2" / "reensamblado_v3" / "kg.json"
KG_SHA256 = "26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571"

# Conteos sellados del grafo vigente (acta de promoción 2026-07-31).
NODOS_ESPERADOS = 4469
ARISTAS_ESPERADAS = 8073

BATCH = 1000
SEED_MUESTREO = 20260806  # fecha de la unidad; fija el muestreo reproducible


def verificar_sha(path: Path) -> None:
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    if h != KG_SHA256:
        raise SystemExit(
            f"ABORTO: sha256 de {path} = {h}\n"
            f"        esperado          = {KG_SHA256}\n"
            "El grafo insumo no coincide con el sellado; no se carga nada."
        )
    print(f"sha256 verificado: {h} ✓")


def cargar_kg():
    return load_graph_from_path(KG_PATH, adapter_key=None)


def _fila_nodo(n) -> dict:
    fila = {
        "id": n.id,
        "type": n.type,
        "label": n.label,
        "props_json": json.dumps(n.properties, ensure_ascii=False, sort_keys=True),
        "provenances_json": json.dumps(n.provenances, ensure_ascii=False),
    }
    for k, v in n.properties.items():
        if k not in fila:  # sin colisiones verificadas; defensa por las dudas
            fila[k] = v
    return fila


def cargar_en_neo4j(driver, kg) -> None:
    with driver.session() as session:
        session.run(
            "CREATE CONSTRAINT nodo_id IF NOT EXISTS "
            "FOR (n:Nodo) REQUIRE n.id IS UNIQUE"
        ).consume()
        # Base limpia: la db se repuebla entera en cada carga (4.5k nodos; el
        # borrado completo en una transacción es viable a esta escala).
        session.run("MATCH (n) DETACH DELETE n").consume()

        # Nodos, agrupados por type (un label Neo4j por type + :Nodo común).
        por_tipo = {}
        for n in kg.nodes:
            por_tipo.setdefault(n.type, []).append(_fila_nodo(n))
        for tipo, filas in por_tipo.items():
            for i in range(0, len(filas), BATCH):
                session.run(
                    f"UNWIND $filas AS fila CREATE (n:Nodo:`{tipo}`) SET n = fila",
                    filas=filas[i:i + BATCH],
                ).consume()

        # Aristas, agrupadas por relation (un relationship type por relation).
        # `orden` = posición de la arista en kg.edges: permite reproducir en el
        # adaptador el orden de inserción que ver_vecinos in-memory expone
        # (Neo4j no garantiza orden de retorno sin ORDER BY).
        por_rel = {}
        for idx, e in enumerate(kg.edges):
            por_rel.setdefault(e.relation, []).append({
                "source": e.source,
                "target": e.target,
                "orden": idx,
                "provenances_json": json.dumps(e.provenances, ensure_ascii=False),
            })
        for rel, filas in por_rel.items():
            for i in range(0, len(filas), BATCH):
                session.run(
                    "UNWIND $filas AS fila "
                    "MATCH (s:Nodo {id: fila.source}), (t:Nodo {id: fila.target}) "
                    f"CREATE (s)-[r:`{rel}`]->(t) "
                    "SET r.orden = fila.orden, "
                    "    r.provenances_json = fila.provenances_json",
                    filas=filas[i:i + BATCH],
                ).consume()


def verificar_carga(driver, kg, n_muestra: int = 20) -> bool:
    """Conteos exactos + muestreo reproducible comparado campo por campo.

    La comparación de id/type/label/properties es contra el kg.json CRUDO
    (con las properties normalizadas por el loader, que para este grafo con
    adaptador nulo son idénticas a las crudas). Las provenances almacenadas
    son la vista del loader (solo la primaria); el JSON crudo trae además la
    lista acumulada `provenances`, que por decisión de paridad de interfaz
    no llega al harness — la diferencia se reporta, no se oculta.
    """
    import random

    crudo = json.loads(KG_PATH.read_text(encoding="utf-8"))
    crudo_por_id = {n["id"]: n for n in crudo["nodes"]}

    with driver.session() as session:
        n_nodos = session.run("MATCH (n:Nodo) RETURN count(n) AS c").single()["c"]
        n_aristas = session.run("MATCH ()-[r]->() RETURN count(r) AS c").single()["c"]

        ok = True
        print(f"conteo nodos   Neo4j={n_nodos}  esperado={NODOS_ESPERADOS} "
              f"{'✓' if n_nodos == NODOS_ESPERADOS else '✗'}")
        print(f"conteo aristas Neo4j={n_aristas}  esperado={ARISTAS_ESPERADAS} "
              f"{'✓' if n_aristas == ARISTAS_ESPERADAS else '✗'}")
        ok = ok and n_nodos == NODOS_ESPERADOS and n_aristas == ARISTAS_ESPERADAS

        rng = random.Random(SEED_MUESTREO)
        muestra = rng.sample(kg.nodes, n_muestra)
        print(f"\nmuestreo de {n_muestra} nodos (seed={SEED_MUESTREO}):")
        for n in muestra:
            rec = session.run(
                "MATCH (m:Nodo {id: $id}) "
                "RETURN m.type AS type, m.label AS label, "
                "       m.props_json AS pj, m.provenances_json AS vj, labels(m) AS ls",
                id=n.id,
            ).single()
            if rec is None:
                print(f"  ✗ {n.id}: NO ESTÁ en Neo4j")
                ok = False
                continue
            raw = crudo_por_id[n.id]
            fallas = []
            if rec["type"] != raw["type"]:
                fallas.append(f"type: {rec['type']!r} != {raw['type']!r}")
            if rec["label"] != raw["label"]:
                fallas.append("label difiere")
            if json.loads(rec["pj"]) != (raw.get("properties") or {}):
                fallas.append("properties difieren del kg.json crudo")
            if json.loads(rec["pj"]) != n.properties:
                fallas.append("properties difieren del loader")
            if json.loads(rec["vj"]) != n.provenances:
                fallas.append("provenances difieren del loader")
            if set(rec["ls"]) != {"Nodo", raw["type"]}:
                fallas.append(f"labels Neo4j inesperados: {rec['ls']}")
            n_prov_crudo = len(raw.get("provenances") or [])
            nota_prov = ("" if n_prov_crudo <= 1 else
                         f"  [crudo trae {n_prov_crudo} provenances; "
                         "almacenada la primaria (vista loader)]")
            if fallas:
                print(f"  ✗ {n.id}: " + "; ".join(fallas))
                ok = False
            else:
                print(f"  ✓ {n.id} ({raw['type']}){nota_prov}")
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--solo-verificar", action="store_true",
                    help="no recarga: solo conteos + muestreo")
    args = ap.parse_args()

    verificar_sha(KG_PATH)
    kg = cargar_kg()
    print(f"loader: {len(kg.nodes)} nodos / {len(kg.edges)} aristas "
          f"(raw {kg.raw_node_count}/{kg.raw_edge_count}, merges={len(kg.merges)})")

    driver = abrir_driver()
    try:
        if not args.solo_verificar:
            cargar_en_neo4j(driver, kg)
            print("carga completa.")
        ok = verificar_carga(driver, kg)
    finally:
        driver.close()

    print("\nVERIFICACIÓN:", "OK" if ok else "CON FALLAS")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
