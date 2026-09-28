#!/usr/bin/env python3
"""U-MED-EJEMPLO-2, Paso 3 — Búsqueda full-text sobre nodos con la pregunta literal (referencia).

1. Neo4jIndex(driver, grafo='KG_Reextraido_r1', modo='fulltext').buscar_nodos(pregunta, 10):
   exactamente lo que ve el agente (neo4j_index.py:121-128, 169-203).
2. Para exponer el puntaje (Neo4jIndex no lo devuelve), la MISMA llamada al índice que
   neo4j_index.py:176-186 (misma cadena Lucene = " ".join(_tokens(pregunta)), mismo orden
   ORDER BY score DESC, size(label) ASC, id ASC) devolviendo score y sin recorte, en sesión READ.
   Se verifica que su top-10 coincide en ids y orden con el de (1).
Procedencias: las de kg.json (lista completa) y la vista runtime guardada en Neo4j.
Escribe únicamente en /tmp/u_med_ejemplo/.
Uso: PYTHONDONTWRITEBYTECODE=1 <REPO>/.venv/bin/python umed2_analista_paso3_fulltext.py <REPO>
"""
import hashlib, json, sys
from pathlib import Path

REPO = Path(sys.argv[1])
sys.path.insert(0, str(REPO / "data/experiment/neo4j"))
from conexion import abrir_driver  # noqa: E402
from neo4j_index import Neo4jIndex  # noqa: E402  (sin modificar)
from harness import _tokens  # noqa: E402  (solo import del cuarteto; path agregado por grafos)

OUT = Path("/tmp/u_med_ejemplo")
PFX = "umed2_analista_"
GRAFO = "KG_Reextraido_r1"
KG = REPO / "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json"
KG_SHA = "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"
PREGUNTA = ("Para una entidad financiera, ¿qué condiciones hacen que los créditos para consumo o "
            "vivienda deban clasificarse en la cartera comercial?")
P2 = OUT / "umed2_analista_paso2_resultado.json"


def main():
    raw = KG.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == KG_SHA
    kg = json.loads(raw)
    nodos = {n["id"]: n for n in kg["nodes"]}
    p2 = json.loads(P2.read_text(encoding="utf-8"))
    de_punto = {k: set(v) for k, v in p2["nodos_por_punto"].items()}
    primarios = {n["id"] for n in p2["nodos"] if n["primaria_chunk_id"] in ("cla::5.1.1.1", "cla::3.7")}

    driver = abrir_driver()
    try:
        idx = Neo4jIndex(driver, grafo=GRAFO, modo="fulltext")
        res_agente = idx.buscar_nodos(PREGUNTA, 10)
        q_lucene = " ".join(_tokens(PREGUNTA))
        q_score = (f"CALL db.index.fulltext.queryNodes('{idx.indice}', $q) YIELD node, score "
                   "WITH node, score ORDER BY score DESC, size(node.label) ASC, node.id ASC "
                   "RETURN node.id AS id, node.type AS type, node.label AS label, "
                   "node.provenances_json AS vj, score")
        with driver.session(default_access_mode="READ") as ses:
            todos = ses.run(q_score, q=q_lucene).data()
    finally:
        driver.close()

    ids_agente = [r["id"] for r in res_agente["resultados"]]
    orden_coincide = ids_agente == [f["id"] for f in todos[:10]]
    total_coincide = res_agente["total_con_match"] == len(todos)
    rango = {f["id"]: (r, f["score"]) for r, f in enumerate(todos, 1)}

    def procs(i):
        n = nodos[i]
        ps = list(n.get("provenances") or [])
        return [p.get("chunk_id") for p in ps]

    top10 = []
    for r, f in enumerate(todos[:10], 1):
        top10.append({"rango": r, "id": f["id"], "type": f["type"], "label": f["label"],
                      "procedencias_kg_chunk_ids": procs(f["id"]),
                      "procedencia_runtime_neo4j": json.loads(f["vj"]), "puntaje": f["score"],
                      "tokens_matcheados_agente": res_agente["resultados"][r - 1]["tokens_matcheados"]})

    def mejor(ids):
        rs = sorted((rango[i][0], rango[i][1], i) for i in ids if i in rango)
        return {"mejor_rango": rs[0][0] if rs else None,
                "detalle": [{"id": i, "rango": r, "puntaje": s} for r, s, i in rs],
                "sin_hit": sorted(i for i in ids if i not in rango)}

    salida = {"pregunta": PREGUNTA, "consulta_lucene": q_lucene, "indice": idx.indice,
              "total_con_match_agente": res_agente["total_con_match"], "n_hits_consulta_score": len(todos),
              "verif_top10_mismo_orden_que_Neo4jIndex": orden_coincide,
              "verif_total_igual": total_coincide,
              "consulta_score": q_score,
              "resultado_Neo4jIndex": res_agente, "top10": top10,
              "nodos_de_5_1_1_1": mejor(de_punto["cla::5.1.1.1"]),
              "nodos_de_3_7": mejor(de_punto["cla::3.7"]),
              "nodos_de_5_1_1_1_solo_primaria": mejor(de_punto["cla::5.1.1.1"] & primarios),
              "nodos_de_3_7_solo_primaria": mejor(de_punto["cla::3.7"] & primarios)}
    (OUT / f"{PFX}paso3_resultado.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    print("consulta_lucene:", q_lucene)
    print("indice:", idx.indice, "| total:", res_agente["total_con_match"], len(todos),
          "| orden coincide:", orden_coincide, "| total coincide:", total_coincide)
    for t in top10:
        print(t["rango"], round(t["puntaje"], 4), t["type"], "|", t["label"], "|", t["id"], "|",
              t["procedencias_kg_chunk_ids"] if len(t["procedencias_kg_chunk_ids"]) <= 3
              else f"{len(t['procedencias_kg_chunk_ids'])} procedencias", "|", t["procedencia_runtime_neo4j"])
    for k in ("nodos_de_5_1_1_1", "nodos_de_3_7", "nodos_de_5_1_1_1_solo_primaria", "nodos_de_3_7_solo_primaria"):
        print(k, json.dumps(salida[k], ensure_ascii=False))


if __name__ == "__main__":
    main()
