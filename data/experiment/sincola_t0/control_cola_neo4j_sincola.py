"""U-SINCOLA-T0, SC2, punto 3: control de que ningún nodo cargado en Neo4j lleva la marca de la cola humana, para los dos
grafos evaluados sin la cola (patrón de data/experiment/reext_t0/t3/control_cola_neo4j.py, que controlaba lo inverso en
los r2b: que la marca llegara). Para cada clave KG_Tanda0_*_r2b_sincola de data/experiment/neo4j/grafos.py: verifica el
sha256 del kg.json, cuenta en el kg.json los nodos y aristas con properties.cola_humana == "true" (esperado 0) y en
Neo4j, bajo la etiqueta del grafo, los nodos con n.cola_humana = 'true', con la marca dentro de n.props_json o con
n.cola_chunks (esperado 0), los nodos y aristas totales contra n_nodos y n_aristas del registro, y KG_Meta.kg_sha256
contra el sha256 del archivo. Solo lee (kg.json y consultas MATCH). Determinístico, USD 0.

Uso (desde la raíz del repo): python -B data/experiment/sincola_t0/control_cola_neo4j_sincola.py --out ARCHIVO.json
"""
import argparse
import hashlib
import json
import sys
from collections import OrderedDict
from pathlib import Path

NEO4J_DIR = Path(__file__).resolve().parents[1] / "neo4j"   # data/experiment/neo4j
if str(NEO4J_DIR) not in sys.path:
    sys.path.insert(0, str(NEO4J_DIR))

import grafos as G   # noqa: E402
from conexion import abrir_driver   # noqa: E402

CLAVES = ["KG_Tanda0_Diez_r2b_sincola", "KG_Tanda0_Desarrollo_r2b_sincola"]
CLAVES_MARCA = ("cola_humana", "cola_chunks", "estado_e3")

ap = argparse.ArgumentParser()
ap.add_argument("--out", type=Path, required=True)
a = ap.parse_args()


def marcado(x) -> bool:
    return (x.get("properties") or {}).get("cola_humana") == "true"


salida = OrderedDict([("unidad", "U-SINCOLA-T0, SC2, punto 3 (control de la marca de la cola en Neo4j)"), ("grafos", OrderedDict())])
driver = abrir_driver()
try:
    for clave in CLAVES:
        g = G.GRAFOS[clave]
        label = g["label"]
        G.verificar_sha(clave)
        kg = json.loads(g["path"].read_text(encoding="utf-8"))
        n_kg_marca = sum(1 for n in kg["nodes"] if marcado(n))
        e_kg_marca = sum(1 for e in kg["edges"] if marcado(e))
        n_kg_clave = sum(1 for o in kg["nodes"] + kg["edges"] if any(k in (o.get("properties") or {}) for k in CLAVES_MARCA))
        with driver.session() as s:
            n_neo = s.run(f"MATCH (n:`{label}`) RETURN count(n) AS c").single()["c"]
            e_neo = s.run(f"MATCH (:`{label}`)-[r]->(:`{label}`) RETURN count(r) AS c").single()["c"]
            n_marca = s.run(f"MATCH (n:`{label}`) WHERE n.cola_humana = 'true' RETURN count(n) AS c").single()["c"]
            n_pj = s.run(f"MATCH (n:`{label}`) WHERE n.props_json CONTAINS '\"cola_humana\"' RETURN count(n) AS c").single()["c"]
            n_cc = s.run(f"MATCH (n:`{label}`) WHERE n.cola_chunks IS NOT NULL RETURN count(n) AS c").single()["c"]
            n_e3 = s.run(f"MATCH (n:`{label}`) WHERE n.estado_e3 IS NOT NULL OR n.props_json CONTAINS '\"estado_e3\"' RETURN count(n) AS c").single()["c"]
            meta = s.run("MATCH (m:KG_Meta {grafo: $g}) RETURN properties(m) AS p", g=clave).single()
            meta = meta["p"] if meta else None
        sha_archivo = hashlib.sha256(g["path"].read_bytes()).hexdigest()
        salida["grafos"][clave] = OrderedDict([
            ("label", label), ("kg_sha256_registro", g["sha256"]), ("sha256_archivo", sha_archivo),
            ("kg_nodos_con_marca", n_kg_marca), ("kg_aristas_con_marca", e_kg_marca), ("kg_objetos_con_alguna_clave_de_marca", n_kg_clave),
            ("neo4j_nodos", n_neo), ("neo4j_aristas", e_neo), ("registro_n_nodos", g["n_nodos"]), ("registro_n_aristas", g["n_aristas"]),
            ("neo4j_nodos_cola_humana_true", n_marca), ("neo4j_nodos_con_cola_humana_en_props_json", n_pj),
            ("neo4j_nodos_con_cola_chunks", n_cc), ("neo4j_nodos_con_estado_e3", n_e3),
            ("kg_meta", meta), ("kg_meta_sha_igual_archivo", bool(meta) and meta.get("kg_sha256") == sha_archivo),
            ("kg_meta_commit_sellado", (meta or {}).get("commit_sellado")),
            ("ok", n_kg_marca == 0 and e_kg_marca == 0 and n_kg_clave == 0 and n_marca == 0 and n_pj == 0 and n_cc == 0 and n_e3 == 0
                   and n_neo == g["n_nodos"] and e_neo == g["n_aristas"] and bool(meta) and meta.get("kg_sha256") == sha_archivo),
        ])
finally:
    driver.close()
salida["ok"] = all(r["ok"] for r in salida["grafos"].values())
a.out.parent.mkdir(parents=True, exist_ok=True)
a.out.write_text(json.dumps(salida, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
for clave, r in salida["grafos"].items():
    print(clave, "| kg marcas nodos/aristas:", r["kg_nodos_con_marca"], r["kg_aristas_con_marca"], "| neo4j nodos/aristas:", r["neo4j_nodos"], r["neo4j_aristas"],
          "| neo4j con marca:", r["neo4j_nodos_cola_humana_true"], r["neo4j_nodos_con_cola_humana_en_props_json"], r["neo4j_nodos_con_cola_chunks"], r["neo4j_nodos_con_estado_e3"],
          "| KG_Meta sha igual:", r["kg_meta_sha_igual_archivo"], "commit_sellado:", r["kg_meta_commit_sellado"], "| ok:", r["ok"])
print("CONTROL COLA NEO4J:", "OK" if salida["ok"] else "CON FALLAS")
