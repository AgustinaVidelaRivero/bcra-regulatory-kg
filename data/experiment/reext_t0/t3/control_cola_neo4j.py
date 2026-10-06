"""U-REEXT-T0, T3, punto 4: control de que la marca de la cola humana llega a Neo4j.

Para cada grafo r2b registrado en data/experiment/neo4j/grafos.py, compara los nodos y las aristas del kg.json que
llevan properties.cola_humana == "true" con lo que hay en Neo4j bajo la etiqueta del grafo: la propiedad aplanada
n.cola_humana, la misma marca dentro de n.props_json y la lista n.cola_chunks; en las aristas, cualquier propiedad que
no sea de la carga (orden, provenances_json). Solo lee: el kg.json y Neo4j (consultas MATCH). Determinístico, USD 0.

Uso (desde la raíz del repo): python -B data/experiment/reext_t0/t3/control_cola_neo4j.py --out ARCHIVO.json
"""
import argparse
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path

NEO4J_DIR = Path(__file__).resolve().parents[2] / "neo4j"   # data/experiment/neo4j
if str(NEO4J_DIR) not in sys.path:
    sys.path.insert(0, str(NEO4J_DIR))

import grafos as G   # noqa: E402
from conexion import abrir_driver   # noqa: E402

CLAVES = ["KG_Tanda0_Diez_r2b", "KG_Tanda0_Desarrollo_r2b"]
PROPS_CARGA_ARISTA = {"orden", "provenances_json"}

ap = argparse.ArgumentParser()
ap.add_argument("--out", type=Path, required=True)
a = ap.parse_args()


def marcado(x) -> bool:
    return (x.get("properties") or {}).get("cola_humana") == "true"


salida = OrderedDict([("unidad", "U-REEXT-T0, T3, punto 4"), ("grafos", OrderedDict())])
driver = abrir_driver()
try:
    for clave in CLAVES:
        g = G.GRAFOS[clave]
        label = g["label"]
        G.verificar_sha(clave)
        kg = json.loads(g["path"].read_text(encoding="utf-8"))
        ids_kg = {n["id"] for n in kg["nodes"] if marcado(n)}
        chunks_kg = {n["id"]: sorted((n["properties"] or {}).get("cola_chunks") or []) for n in kg["nodes"] if marcado(n)}
        aristas_kg = sum(1 for e in kg["edges"] if marcado(e))
        with driver.session() as s:
            filas = s.run(f"MATCH (n:`{label}`) WHERE n.cola_humana = 'true' "
                          "RETURN n.id AS id, n.type AS type, n.props_json AS pj, n.cola_chunks AS cc").data()
            n_pj = s.run(f"MATCH (n:`{label}`) WHERE n.props_json CONTAINS '\"cola_humana\": \"true\"' "
                         "RETURN count(n) AS c").single()["c"]
            props_arista = s.run(f"MATCH (:`{label}`)-[r]->(:`{label}`) UNWIND keys(r) AS k "
                                 "RETURN k, count(*) AS c ORDER BY k").data()
        ids_neo = {f["id"] for f in filas}
        pj_ok = sum(1 for f in filas if json.loads(f["pj"]).get("cola_humana") == "true")
        cc_ok = sum(1 for f in filas if sorted(f["cc"] or []) == chunks_kg.get(f["id"]))
        extra = [p for p in props_arista if p["k"] not in PROPS_CARGA_ARISTA]
        salida["grafos"][clave] = OrderedDict([
            ("label", label), ("kg_sha256", g["sha256"]),
            ("nodos_con_marca_kg", len(ids_kg)), ("nodos_con_marca_neo4j", len(ids_neo)),
            ("mismos_ids", ids_kg == ids_neo),
            ("solo_en_kg", sorted(ids_kg - ids_neo)), ("solo_en_neo4j", sorted(ids_neo - ids_kg)),
            ("marca_en_props_json", pj_ok), ("nodos_con_marca_en_props_json_por_consulta", n_pj),
            ("cola_chunks_iguales_al_kg", cc_ok),
            ("nodos_con_marca_por_tipo", dict(sorted(Counter(f["type"] for f in filas).items()))),
            ("aristas_con_marca_kg", aristas_kg),
            ("propiedades_de_arista_en_neo4j", {p["k"]: p["c"] for p in props_arista}),
            ("aristas_con_marca_neo4j", 0 if not extra else None),
            ("nota_aristas", "cargar_kg.cargar_en_neo4j crea cada arista solo con orden y provenances_json: las "
                             "properties de las aristas del kg.json, la marca de la cola incluida, no se cargan."),
            ("ok_nodos", ids_kg == ids_neo and pj_ok == len(ids_kg) == n_pj and cc_ok == len(ids_kg)),
        ])
finally:
    driver.close()
a.out.write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for clave, r in salida["grafos"].items():
    print(clave, "nodos kg/neo4j:", r["nodos_con_marca_kg"], r["nodos_con_marca_neo4j"], "mismos ids:", r["mismos_ids"],
          "props_json:", r["marca_en_props_json"], "cola_chunks:", r["cola_chunks_iguales_al_kg"],
          "aristas kg:", r["aristas_con_marca_kg"], "props arista neo4j:", r["propiedades_de_arista_en_neo4j"],
          "ok_nodos:", r["ok_nodos"])
