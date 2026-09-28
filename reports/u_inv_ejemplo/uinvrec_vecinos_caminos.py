#!/usr/bin/env python3
"""U-INV-RECORRIDO, Pasos 2 y 3 — vecinos del nodo R y caminos cortos hasta R.

Solo lectura del repositorio y de Neo4j (solo MATCH/RETURN); escribe únicamente
en /tmp/u_inv_ejemplo/ (prefijo uinvrec_).

- Vecinos: Neo4jIndex.ver_vecinos(id, "ambas") (neo4j_index.py:226-273, tope 40
  por dirección, orden r.orden) y, para ver posiciones más allá del tope, las
  MISMAS dos consultas Cypher sin recorte (neo4j_index.py:238-249). Se comprueba
  que los primeros 40 coincidan con la salida de la herramienta y que el orden
  completo coincida con GraphIndex.ver_vecinos del harness sobre la vista
  runtime de r1 (grafos.cargar_vista_runtime), que es el índice del agente de
  EV2 base / r1.
- Caminos: BFS no dirigido sobre todas las aristas de KG_Reextraido_r1 leídas de
  Neo4j; se enumeran TODOS los caminos más cortos de hasta 3 aristas desde cada
  nodo del top-10 de ufig12_busqueda_nodos_resultado.json (pregunta nueva) hasta R.
- Procedencias: las de kg.json (to, punto, rol_documental; base.provenances del
  generador de figuras) y las que ve el agente (provenances_json de Neo4j).
Uso: PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B /tmp/u_inv_ejemplo/uinvrec_vecinos_caminos.py <raíz del repo>
"""
import collections, hashlib, json, os, sys

sys.dont_write_bytecode = True
RAIZ = os.path.abspath(sys.argv[1])
OUT = "/tmp/u_inv_ejemplo/uinvrec_vecinos_caminos_resultado.json"
TOP10_JSON = "/tmp/u_inv_ejemplo/ufig12_busqueda_nodos_resultado.json"
sys.path.insert(0, os.path.join(RAIZ, "docs/tesis/figuras"))
sys.path.insert(0, os.path.join(RAIZ, "data/experiment/neo4j"))
import generar_figura_norma_a_grafo as base  # noqa: E402  (solo provenances y KG)
from conexion import abrir_driver  # noqa: E402
from neo4j_index import Neo4jIndex  # noqa: E402
from grafos import GRAFOS, cargar_vista_runtime  # noqa: E402
from harness import GraphIndex  # noqa: E402

GRAFO = "KG_Reextraido_r1"
TOPE = 40
PUNTOS_DESTINO = ["3.4.1", "3.4.2", "3.4.3"]
MAX_SALTOS = 3


def prov_kg(n):
    return [{"to": p.get("to"), "punto": p.get("punto"), "rol_documental": p.get("rol_documental")}
            for p in base.provenances(n)]


def main():
    sha = hashlib.sha256(open(base.KG, "rb").read()).hexdigest()
    if sha != GRAFOS[GRAFO]["sha256"]:
        raise SystemExit("sha256 del kg.json distinto del registro")
    kg = json.load(open(base.KG, encoding="utf-8"))
    nodos = {n["id"]: n for n in kg["nodes"]}
    r_ids = [i for i in nodos if i.endswith("8355c7")]
    if len(r_ids) != 1:
        raise SystemExit(f"sufijo 8355c7 no único: {r_ids}")
    R = r_ids[0]
    top10 = json.load(open(TOP10_JSON, encoding="utf-8"))["preguntas"]["nueva"]["top10"]

    driver = abrir_driver()
    idx = Neo4jIndex(driver, grafo=GRAFO, modo="fulltext")
    lab = idx.label
    with driver.session() as s:
        aristas = s.run(f"MATCH (a:`{lab}`)-[r]->(b:`{lab}`) "
                        "RETURN a.id AS a, type(r) AS rel, b.id AS b, r.orden AS orden "
                        "ORDER BY r.orden").data()
        vista = {r["id"]: {"type": r["type"], "label": r["label"], "prov": json.loads(r["vj"])}
                 for r in s.run(f"MATCH (n:`{lab}`) RETURN n.id AS id, n.type AS type, "
                                "n.label AS label, n.provenances_json AS vj").data()}

    def completas(nid):
        with driver.session() as s:
            out = s.run(f"MATCH (n:`{lab}` {{id: $id}})-[r]->(v:`{lab}`) "
                        "RETURN type(r) AS relation, v.id AS vecino_id, r.orden AS orden "
                        "ORDER BY r.orden", id=nid).data()
            inn = s.run(f"MATCH (n:`{lab}` {{id: $id}})<-[r]-(v:`{lab}`) "
                        "RETURN type(r) AS relation, v.id AS vecino_id, r.orden AS orden "
                        "ORDER BY r.orden", id=nid).data()
        return out, inn

    # Vista in-memory del agente de EV2 base / r1, para la paridad de orden.
    gi = GraphIndex(cargar_vista_runtime(GRAFO))
    cache_vec, paridad = {}, {}

    def vecinos(nid):
        if nid in cache_vec:
            return cache_vec[nid]
        out, inn = completas(nid)
        herr = idx.ver_vecinos(nid, "ambas")
        if ([(x["relation"], x["vecino_id"]) for x in herr["salientes"]]
                != [(x["relation"], x["vecino_id"]) for x in out[:TOPE]]
                or [(x["relation"], x["vecino_id"]) for x in herr["entrantes"]]
                != [(x["relation"], x["vecino_id"]) for x in inn[:TOPE]]):
            raise SystemExit(f"la consulta sin recorte no reproduce ver_vecinos en {nid}")
        mem = gi.ver_vecinos(nid, "ambas", limite=10 ** 6)
        paridad[nid] = ([(x["relation"], x["vecino_id"]) for x in mem["salientes"]]
                        == [(x["relation"], x["vecino_id"]) for x in out]
                        and [(x["relation"], x["vecino_id"]) for x in mem["entrantes"]]
                        == [(x["relation"], x["vecino_id"]) for x in inn])
        cache_vec[nid] = (out, inn)
        return out, inn

    def ficha(nid):
        n = nodos[nid]
        return {"id": nid, "sufijo": nid[-6:], "tipo": n["type"], "etiqueta": n.get("label"),
                "procedencias_kg": prov_kg(n), "procedencias_agente": vista[nid]["prov"]}

    # ---------------- Paso 2: aristas de R ----------------
    out, inn = vecinos(R)
    paso2 = []
    for direccion, lista in (("saliente", out), ("entrante", inn)):
        for pos, e in enumerate(lista, 1):
            f = ficha(e["vecino_id"])
            puntos = sorted({p["punto"] for p in f["procedencias_kg"] if p["to"] == "ext"})
            # Posición de R en la lista inversa del otro extremo (la misma arista
            # vista desde allá): entrantes si la arista sale de R, salientes si entra.
            o_out, o_inn = vecinos(e["vecino_id"])
            inversa = o_inn if direccion == "saliente" else o_out
            pos_r = next(i for i, x in enumerate(inversa, 1) if x["orden"] == e["orden"])
            paso2.append({"direccion": direccion, "posicion_en_ver_vecinos": pos,
                          "dentro_del_tope": pos <= TOPE, "relacion": e["relation"],
                          "orden": e["orden"],
                          "R_visto_desde_el_otro_extremo": {
                              "lista": "entrantes" if direccion == "saliente" else "salientes",
                              "posicion": pos_r, "n_total": len(inversa),
                              "dentro_del_tope": pos_r <= TOPE},
                          "otro_extremo": f,
                          "va_a_3_4_x": [p for p in PUNTOS_DESTINO if p in puntos],
                          "es_operacion_de_3_17_1_4": f["tipo"] == "Operacion" and "3.17.1.4" in puntos})

    # ---------------- Paso 3: caminos más cortos (no dirigidos) ----------------
    ady = collections.defaultdict(list)   # nodo -> [(vecino, idx_arista)]
    for k, e in enumerate(aristas):
        ady[e["a"]].append((e["b"], k))
        if e["b"] != e["a"]:
            ady[e["b"]].append((e["a"], k))

    def caminos_mas_cortos(src, dst):
        if src == dst:
            return 0, [[]]
        # BFS por niveles guardando todos los predecesores (por arista).
        dist, pred = {src: 0}, collections.defaultdict(list)
        frontera = [src]
        for d in range(1, MAX_SALTOS + 1):
            nueva = []
            for u in frontera:
                for v, k in ady[u]:
                    if v not in dist:
                        dist[v] = d
                        nueva.append(v)
                    if dist[v] == d:
                        pred[v].append((u, k))
            if dst in dist:
                break
            frontera = nueva
        if dst not in dist:
            return None, []
        res = []

        def atras(v, suf):
            if v == src:
                res.append(list(reversed(suf)))
                return
            for u, k in pred[v]:
                atras(u, suf + [(u, k, v)])
        atras(dst, [])
        return dist[dst], res

    def salto(u, k, v):
        e = aristas[k]
        sentido = "saliente" if e["a"] == u else "entrante"   # visto desde u
        out_u, inn_u = vecinos(u)
        lista = out_u if sentido == "saliente" else inn_u
        pos = next(i for i, x in enumerate(lista, 1) if x["orden"] == e["orden"])
        return {"desde": u[-6:], "relacion": e["rel"], "sentido_desde_nodo_actual": sentido,
                "arista": f"{e['a'][-6:]} -[{e['rel']}]-> {e['b'][-6:]}", "orden": e["orden"],
                "posicion_en_ver_vecinos": pos, "lista": sentido + "s",
                "n_total_en_esa_lista": len(lista), "dentro_del_tope": pos <= TOPE,
                "nodo_siguiente": ficha(v)}

    paso3 = []
    for t in top10:
        d, cams = caminos_mas_cortos(t["id"], R)
        paso3.append({"rango_busqueda": t["rango"], "origen": ficha(t["id"]), "largo": d,
                      "n_caminos_mas_cortos": len(cams),
                      "caminos": [[salto(u, k, v) for (u, k, v) in c] for c in cams]})
    driver.close()

    salida = {"grafo": GRAFO, "kg_sha256": sha, "R": R, "tope_ver_vecinos": TOPE,
              "n_aristas_neo4j": len(aristas), "n_nodos_neo4j": len(vista),
              "paridad_orden_neo4j_vs_graphindex": paridad,
              "paso2_aristas_de_R": paso2, "paso3_caminos": paso3}
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(salida, fh, ensure_ascii=False, indent=1)

    # ---------------- consola ----------------
    def pk(f):
        return "; ".join(f"{p['to']} {p['punto']} ({p['rol_documental']})" for p in f["procedencias_kg"][:4]) + (
            f"; … total {len(f['procedencias_kg'])}" if len(f["procedencias_kg"]) > 4 else "")

    def pa(f):
        ls = [p.get("location") for p in f["procedencias_agente"]]
        return "; ".join(ls[:4]) + (f"; … total {len(ls)}" if len(ls) > 4 else "")

    print(f"aristas {len(aristas)}  nodos {len(vista)}  R = {R}")
    print(f"paridad de orden Neo4j vs GraphIndex (nodos consultados): "
          f"{sum(paridad.values())}/{len(paridad)} idénticos")
    print(f"\nPASO 2 — aristas de R: {len(out)} salientes, {len(inn)} entrantes")
    for a in paso2:
        f = a["otro_extremo"]
        marca = (f"  <-- 3.4.x {a['va_a_3_4_x']}" if a["va_a_3_4_x"] else "") + (
            "  <-- Operacion de 3.17.1.4" if a["es_operacion_de_3_17_1_4"] else "")
        print(f"  {a['direccion']:8s} #{a['posicion_en_ver_vecinos']:<3d} {a['relacion']:18s} "
              f"{f['tipo']:14s} {f['sufijo']}  «{f['etiqueta']}»{marca}")
        print(f"        kg: {pk(f)}")
        print(f"        agente: {pa(f)}")
        rv = a["R_visto_desde_el_otro_extremo"]
        print(f"        R en ver_vecinos del otro extremo: {rv['lista']} #{rv['posicion']} de {rv['n_total']}"
              f"{'' if rv['dentro_del_tope'] else ' — FUERA DEL TOPE'}")
    print("\nPASO 3 — caminos más cortos (≤3 aristas, no dirigidos) hasta R")
    for c in paso3:
        o = c["origen"]
        print(f"\n  [{c['rango_busqueda']}] {o['tipo']} {o['sufijo']} «{o['etiqueta']}»  "
              f"largo {c['largo']}  caminos más cortos: {c['n_caminos_mas_cortos']}")
        for j, cam in enumerate(c["caminos"], 1):
            print(f"    camino {j}:")
            for s in cam:
                f = s["nodo_siguiente"]
                print(f"      {s['arista']}  (desde {s['desde']}: {s['lista']} #{s['posicion_en_ver_vecinos']}"
                      f" de {s['n_total_en_esa_lista']}{'' if s['dentro_del_tope'] else ' — FUERA DEL TOPE'})")
                print(f"        -> {f['tipo']} {f['sufijo']} «{f['etiqueta']}»  kg: {pk(f)} | agente: {pa(f)}")
    print(f"\nJSON: {OUT}  sha256 {hashlib.sha256(open(OUT, 'rb').read()).hexdigest()}")


if __name__ == "__main__":
    main()
