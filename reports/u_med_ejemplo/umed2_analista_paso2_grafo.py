#!/usr/bin/env python3
"""U-MED-EJEMPLO-2, Paso 2 — Nodos y aristas de cla::5.1.1.1 y cla::3.7 en r1: kg.json vs Neo4j.

kg.json: data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json (sha256 verificado).
Selección: nodo con alguna procedencia (primaria o de la lista `provenances`) con chunk_id
cla::5.1.1.1 o cla::3.7; se contrasta con archivo+punto (deben coincidir).
Neo4j (label KG_Reextraido_r1): solo consultas MATCH/RETURN, sesión en modo READ.
En Neo4j las procedencias son la vista runtime (primaria mapeada a {source_doc, location},
data/experiment/ev2_corrida/code/comun_ev2.py:134-145, replicado abajo sin importarlo).
Escribe únicamente en /tmp/u_med_ejemplo/.
Uso: PYTHONDONTWRITEBYTECODE=1 <REPO>/.venv/bin/python umed2_analista_paso2_grafo.py <REPO>
"""
import collections, hashlib, json, sys
from pathlib import Path

REPO = Path(sys.argv[1])
sys.path.insert(0, str(REPO / "data/experiment/neo4j"))
from conexion import abrir_driver  # noqa: E402  (solo import)

OUT = Path("/tmp/u_med_ejemplo")
PFX = "umed2_analista_"
KG = REPO / "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json"
KG_SHA = "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"
LABEL = "KG_Reextraido_r1"
ARCHIVO = "TO_clasificacion_deudores_actual.pdf"
PUNTOS = {"cla::5.1.1.1": "5.1.1.1", "cla::3.7": "3.7"}

Q_CONTEO_N = f"MATCH (n:{LABEL}) RETURN count(n) AS n"
Q_CONTEO_E = f"MATCH (:{LABEL})-[r]->(:{LABEL}) RETURN count(r) AS n"
Q_NODOS = (f"MATCH (n:{LABEL}) WHERE n.id IN $ids "
           "RETURN n.id AS id, n.type AS type, n.label AS label, n.provenances_json AS vj ORDER BY n.id")
Q_NODOS_VISTA = (f"MATCH (n:{LABEL}) WHERE n.provenances_json CONTAINS $a OR n.provenances_json CONTAINS $b "
                 "RETURN n.id AS id, n.type AS type, n.label AS label, n.provenances_json AS vj ORDER BY n.id")
Q_ARISTAS = (f"MATCH (s:{LABEL})-[r]->(t:{LABEL}) WHERE s.id IN $ids OR t.id IN $ids "
             "RETURN s.id AS s, s.type AS s_type, s.label AS s_label, type(r) AS rel, "
             "t.id AS t, t.type AS t_type, t.label AS t_label, r.orden AS orden, "
             "r.provenances_json AS vj ORDER BY r.orden")


def map_prov(p):  # réplica de comun_ev2._map_prov_v2 (líneas 134-145)
    if not isinstance(p, dict):
        return None
    punto = (p.get("punto") or "").strip()
    if not punto:
        return None
    if punto.startswith("S") and punto[1:].isdigit():
        location = f"Sección {punto[1:]}"
    else:
        location = f"Punto {punto}"
    return {"source_doc": p.get("archivo"), "location": location}


def procs(x):
    ps = list(x.get("provenances") or [])
    prim = x.get("provenance")
    if prim and prim not in ps:
        ps = [prim] + ps
    return ps


def resumen_procs(x):
    return [{"chunk_id": p.get("chunk_id"), "punto": p.get("punto"), "rol_documental": p.get("rol_documental"),
             **({"chunks_emisores": p["chunks_emisores"]} if "chunks_emisores" in p else {})} for p in procs(x)]


def main():
    raw = KG.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    assert sha == KG_SHA, sha
    kg = json.loads(raw)
    nodos = {n["id"]: n for n in kg["nodes"]}

    # ---- selección en kg.json (dos criterios) ----
    por_chunk, por_punto = collections.defaultdict(set), collections.defaultdict(set)
    for n in kg["nodes"]:
        for p in procs(n):
            if p.get("chunk_id") in PUNTOS:
                por_chunk[p["chunk_id"]].add(n["id"])
            if p.get("archivo") == ARCHIVO and p.get("punto") in PUNTOS.values():
                por_punto["cla::" + p["punto"]].add(n["id"])
    discrepancias = {k: sorted(por_chunk[k] ^ por_punto[k]) for k in PUNTOS if por_chunk[k] != por_punto[k]}
    sel = set().union(*por_chunk.values())
    punto_de = {i: sorted(k for k in PUNTOS if i in por_chunk[k]) for i in sel}

    ficha_nodo = {}
    for i in sorted(sel):
        n = nodos[i]
        ficha_nodo[i] = {"id": i, "type": n["type"], "label": n["label"], "puntos_objetivo": punto_de[i],
                         "primaria_chunk_id": (n.get("provenance") or {}).get("chunk_id"),
                         "n_procedencias": len(procs(n)), "procedencias": resumen_procs(n)}

    aristas = []
    for orden, e in enumerate(kg["edges"]):
        if e["source"] in sel or e["target"] in sel:
            aristas.append({"orden": orden, "source": e["source"], "relation": e["relation"], "target": e["target"],
                            "procedencias_arista": resumen_procs(e)})
    por_nodo = {}
    for i in sorted(sel):
        filas = []
        for a in aristas:
            for direccion, yo, otro in (("saliente", "source", "target"), ("entrante", "target", "source")):
                if a[yo] == i:
                    o = nodos[a[otro]]
                    filas.append({"orden": a["orden"], "relation": a["relation"], "direccion": direccion,
                                  "otro_id": o["id"], "otro_type": o["type"], "otro_label": o["label"],
                                  "otro_procedencias_chunk_ids": [p.get("chunk_id") for p in procs(o)],
                                  "procedencias_arista": a["procedencias_arista"]})
        por_nodo[i] = {"n_salientes": sum(f["direccion"] == "saliente" for f in filas),
                       "n_entrantes": sum(f["direccion"] == "entrante" for f in filas),
                       "por_relacion": dict(collections.Counter(f"{f['direccion']}:{f['relation']}" for f in filas)),
                       "aristas": filas}

    s511, s37 = por_chunk["cla::5.1.1.1"], por_chunk["cla::3.7"]
    ref_entre = [a for a in aristas if a["relation"] == "referencia" and
                 ((a["source"] in s511 and a["target"] in s37) or (a["source"] in s37 and a["target"] in s511))]
    ref_entrantes_37 = []
    for orden, e in enumerate(kg["edges"]):
        if e["relation"] == "referencia" and e["target"] in s37:
            src = nodos[e["source"]]
            ref_entrantes_37.append({"orden": orden, "source": e["source"], "source_type": src["type"],
                                     "source_primaria_chunk_id": (src.get("provenance") or {}).get("chunk_id"),
                                     "target": e["target"],
                                     "arista_chunk_ids": [p.get("chunk_id") for p in procs(e)]})

    # ---- Neo4j (MATCH/RETURN, READ) ----
    consultas = []
    driver = abrir_driver()
    try:
        with driver.session(default_access_mode="READ") as ses:
            def run(q, **kw):
                filas = ses.run(q, **kw).data()
                consultas.append({"consulta": q, "parametros": kw, "n_filas": len(filas)})
                return filas
            n_nodos = run(Q_CONTEO_N)[0]["n"]
            n_aristas = run(Q_CONTEO_E)[0]["n"]
            neo_nodos = run(Q_NODOS, ids=sorted(sel))
            neo_vista = run(Q_NODOS_VISTA, a='"Punto 5.1.1.1"', b='"Punto 3.7"')
            neo_aristas = run(Q_ARISTAS, ids=sorted(sel))
    finally:
        driver.close()

    # comparación de nodos
    kg_n = {i: (nodos[i]["type"], nodos[i]["label"], [map_prov(nodos[i].get("provenance"))]) for i in sel}
    neo_n = {f["id"]: (f["type"], f["label"], json.loads(f["vj"])) for f in neo_nodos}
    nodos_iguales = kg_n == neo_n
    # comparación de aristas (source, relation, target, orden, procedencia runtime)
    kg_e = sorted((a["source"], a["relation"], a["target"], a["orden"],
                   json.dumps([map_prov(kg["edges"][a["orden"]].get("provenance"))], ensure_ascii=False))
                  for a in aristas)
    neo_e = sorted((f["s"], f["rel"], f["t"], f["orden"], json.dumps(json.loads(f["vj"]), ensure_ascii=False))
                   for f in neo_aristas)
    aristas_iguales = kg_e == neo_e
    # extremos: type/label de Neo4j vs kg.json
    extremos_ok = all((nodos[f["s"]]["type"], nodos[f["s"]]["label"], nodos[f["t"]]["type"], nodos[f["t"]]["label"])
                      == (f["s_type"], f["s_label"], f["t_type"], f["t_label"]) for f in neo_aristas)
    # vista runtime: nodos cuya procedencia primaria (mapeada) es cla 5.1.1.1 / 3.7
    vista = [f for f in neo_vista
             if any(p.get("source_doc") == ARCHIVO and p.get("location") in ("Punto 5.1.1.1", "Punto 3.7")
                    for p in json.loads(f["vj"]))]
    kg_primaria = sorted(i for i in sel if ficha_nodo[i]["primaria_chunk_id"] in PUNTOS)

    salida = {
        "kg_path": str(KG.relative_to(REPO)), "kg_sha256": sha,
        "criterio": "procedencia (primaria o lista) con chunk_id cla::5.1.1.1 o cla::3.7; contraste archivo+punto",
        "discrepancias_entre_criterios": discrepancias,
        "nodos_por_punto": {k: sorted(v) for k, v in por_chunk.items()},
        "nodos": list(ficha_nodo.values()),
        "n_aristas_incidentes_distintas": len(aristas),
        "aristas_por_nodo": por_nodo,
        "referencia_entre_5_1_1_1_y_3_7": ref_entre,
        "referencia_entrantes_a_nodos_3_7": ref_entrantes_37,
        "neo4j": {
            "label": LABEL, "conteo_nodos": n_nodos, "conteo_aristas": n_aristas,
            "consultas": consultas,
            "nodos": neo_nodos, "nodos_vista_runtime_en_los_dos_puntos": vista,
            "aristas_incidentes": neo_aristas,
        },
        "comparacion": {
            "nodos_iguales_id_type_label_procedencia_runtime": nodos_iguales,
            "aristas_iguales_source_relation_target_orden_procedencia_runtime": aristas_iguales,
            "n_aristas_kg": len(kg_e), "n_aristas_neo4j": len(neo_e),
            "extremos_type_label_iguales": extremos_ok,
            "vista_runtime_ids": [f["id"] for f in vista],
            "kg_primaria_en_los_dos_puntos_ids": kg_primaria,
            "vista_runtime_igual_a_kg_primaria": sorted(f["id"] for f in vista) == kg_primaria,
        },
    }
    (OUT / f"{PFX}paso2_resultado.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: salida[k] for k in ("kg_sha256", "discrepancias_entre_criterios", "nodos_por_punto",
                                             "n_aristas_incidentes_distintas", "comparacion")}, ensure_ascii=False, indent=1))
    print("neo4j conteos", n_nodos, n_aristas)
    for i, v in por_nodo.items():
        print(i, v["n_salientes"], v["n_entrantes"], v["por_relacion"])
    print("referencia entre 5.1.1.1 y 3.7:", json.dumps(ref_entre, ensure_ascii=False))
    print("referencia entrantes a nodos de 3.7:", len(ref_entrantes_37))


if __name__ == "__main__":
    main()
