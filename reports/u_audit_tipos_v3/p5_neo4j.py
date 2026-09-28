"""Punto 5: conteos en Neo4j (solo MATCH/RETURN) de KG_Tanda0_Desarrollo_r1."""
import json, sys, collections
sys.path.insert(0, "/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/neo4j")
from conexion import abrir_driver
L = "KG_Tanda0_Desarrollo_r1"
d = abrir_driver()
out = {}
with d.session() as s:
    out["nodos_por_type"] = {r["t"]: r["c"] for r in s.run(f"MATCH (n:`{L}`) RETURN n.type AS t, count(n) AS c ORDER BY t")}
    out["aristas_por_rel"] = {r["rel"]: r["c"] for r in s.run(f"MATCH (:`{L}`)-[r]->(:`{L}`) RETURN type(r) AS rel, count(r) AS c ORDER BY rel")}
    out["labels_por_type_nuevo"] = {r["t"]: r["ok"] for r in s.run(
        f"MATCH (n:`{L}`) WHERE n.type IN ['Condicion','Potestad','Definicion'] "
        "RETURN n.type AS t, sum(CASE WHEN n.type IN labels(n) THEN 1 ELSE 0 END) AS ok ORDER BY t")}
    out["con_descripcion_prop_por_type_nuevo"] = {r["t"]: r["c"] for r in s.run(
        f"MATCH (n:`{L}`) WHERE n.type IN ['Condicion','Potestad','Definicion'] AND n.descripcion IS NOT NULL "
        "RETURN n.type AS t, count(n) AS c ORDER BY t")}
    out["aislados_por_type"] = {r["t"]: r["c"] for r in s.run(
        f"MATCH (n:`{L}`) WHERE NOT (n)--() RETURN n.type AS t, count(n) AS c ORDER BY t")}
d.close()
json.dump(out, open("/tmp/u_audit_tipos/p5_neo4j.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
