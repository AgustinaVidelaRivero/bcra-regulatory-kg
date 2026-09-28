#!/usr/bin/env python3
"""U-FIG-12, Paso 1 — búsqueda sobre los nodos del grafo (paso «1 · Buscar»).

Solo lectura del repositorio y de Neo4j; escribe únicamente en /tmp/u_inv_ejemplo/.
Corre la búsqueda que declara docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py
en sus líneas 51-57 (Neo4jIndex en modo 'fulltext', índice
nodos_fulltext_kg_reextraido_r1, límite 10, grafo KG_Reextraido_r1) SIN ejecutar su
main(), con dos preguntas:
  - «actual»: la de las líneas 48-49 del generador (control contra
    RESULTADO_BUSQUEDA, líneas 59-64), copiada literal;
  - «nueva»: la de la decisión 1 del mandato U-FIG-12.
El puntaje sale de la misma consulta Cypher que usa verificar_busqueda() del
generador (líneas 545-549), con el orden de Neo4jIndex._buscar_fulltext; se
comprueba que su top-10 sea idéntico al de la llamada de la app.
Uso: PYTHONDONTWRITEBYTECODE=1 .venv/bin/python /tmp/u_inv_ejemplo/ufig12_busqueda_nodos.py <raíz del repo>
"""
import hashlib, json, os, sys

sys.dont_write_bytecode = True
RAIZ = os.path.abspath(sys.argv[1])
OUT = "/tmp/u_inv_ejemplo/ufig12_busqueda_nodos_resultado.json"
sys.path.insert(0, os.path.join(RAIZ, "docs/tesis/figuras"))
sys.path.insert(0, os.path.join(RAIZ, "data/experiment/neo4j"))
import generar_figura_norma_a_grafo as base  # noqa: E402  (solo helpers; no se ejecuta main)
from conexion import abrir_driver  # noqa: E402
from neo4j_index import Neo4jIndex  # noqa: E402
from grafos import GRAFOS  # noqa: E402
from harness import _tokens  # noqa: E402

GRAFO, MODO, LIMITE = "KG_Reextraido_r1", "fulltext", 10
PREGUNTAS = {
    "actual": ("¿Puede una empresa pagar dividendos a accionistas del exterior? "
               "¿Qué requisitos debe cumplir?"),
    "nueva": ("Una petrolera que obtuvo la certificación del régimen de acceso a divisas por "
              "producción incremental quiere usarla para pagar dividendos a sus accionistas del "
              "exterior. ¿Qué requisitos debe cumplir?"),
}
# Líneas 59-64 del generador, literal.
RESULTADO_BUSQUEDA_ACTUAL = [("3.17.1.4", True), ("3.4.3", False), ("3.4.2", False), ("3.4.1", False)]
PUNTOS = ["3.17.1.4", "3.4.1", "3.4.2", "3.4.3"]


def main():
    reg = GRAFOS[GRAFO]
    if os.path.abspath(str(reg["path"])) != os.path.abspath(base.KG):
        raise SystemExit("el kg.json del registro no es el del generador")
    sha = hashlib.sha256(open(base.KG, "rb").read()).hexdigest()
    if sha != reg["sha256"]:
        raise SystemExit(f"sha256 del kg.json distinto del registro: {sha}")
    nodos, ids, _, _ = base.cargar()
    id_r = ids["R"]

    driver = abrir_driver()
    indice = Neo4jIndex(driver, grafo=GRAFO, modo=MODO)
    salida = {"grafo": GRAFO, "modo": MODO, "indice": indice.indice, "limite": LIMITE,
              "kg_sha256": sha, "nodo_R": id_r, "preguntas": {}}
    for clave, q in PREGUNTAS.items():
        app = indice.buscar_nodos(q, limite=LIMITE)
        with driver.session() as s:
            ranking = [(r["id"], r["score"]) for r in s.run(
                f"CALL db.index.fulltext.queryNodes('{indice.indice}', $q) YIELD node, score "
                "RETURN node.id AS id, score ORDER BY score DESC, size(node.label) ASC, node.id ASC",
                q=" ".join(_tokens(q)))]
        if [i for i, _ in ranking[:LIMITE]] != [r["id"] for r in app["resultados"]]:
            raise SystemExit(f"[{clave}] el ranking con puntaje no coincide con la llamada de la app")
        if len(ranking) != app["total_con_match"]:
            raise SystemExit(f"[{clave}] total_con_match distinto del ranking completo")

        def fila(r, nid, score):
            n = nodos[nid]
            prov = [{"to": p.get("to"), "punto": p.get("punto"), "rol_documental": p.get("rol_documental")}
                    for p in base.provenances(n)]
            return {"rango": r, "id": nid, "tipo": n["type"], "etiqueta": n.get("label"),
                    "puntaje": score, "puntaje_exacto": repr(score), "procedencias": prov}

        top = [fila(r, nid, sc) for r, (nid, sc) in enumerate(ranking[:LIMITE], 1)]

        def primero(punto, estricto):
            for r, (nid, sc) in enumerate(ranking, 1):
                n = nodos.get(nid)
                if not n:
                    continue
                if estricto and n["type"] not in base.TIPOS_CON_PUNTO:
                    continue
                if any(p.get("to") == "ext" and p.get("punto") == punto
                       and (not estricto or p.get("rol_documental") == "punto_propio")
                       for p in base.provenances(n)):
                    return {"rango": r, "id": nid, "tipo": n["type"], "etiqueta": n.get("label"),
                            "puntaje_exacto": repr(sc)}
            return None

        rango_r = next((r for r, (nid, _) in enumerate(ranking, 1) if nid == id_r), None)
        salida["preguntas"][clave] = {
            "texto": q, "consulta_lucene": " ".join(_tokens(q)),
            "total_con_match": app["total_con_match"], "top10": top,
            "primera_aparicion_cualquier_procedencia": {p: primero(p, False) for p in PUNTOS},
            "primera_aparicion_criterio_generador": {p: primero(p, True) for p in PUNTOS},
            "rango_nodo_R": rango_r,
        }
    driver.close()

    # Control con la pregunta actual: mismo criterio que verificar_busqueda() del generador.
    pa = salida["preguntas"]["actual"]["primera_aparicion_criterio_generador"]
    medido = [(p, pa[p]["rango"] if pa[p] else None) for p in PUNTOS]
    orden = sorted(medido, key=lambda t: (t[1] is None, t[1]))
    esperado = [(p, pos is not None and pos <= LIMITE) for p, pos in orden]
    salida["control_actual"] = {"medido": esperado, "declarado": RESULTADO_BUSQUEDA_ACTUAL,
                                "reproduce": esperado == RESULTADO_BUSQUEDA_ACTUAL}

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(salida, fh, ensure_ascii=False, indent=1)

    for clave, d in salida["preguntas"].items():
        print(f"\n=== pregunta {clave}: {d['texto']}")
        print(f"    consulta Lucene: {d['consulta_lucene']}")
        print(f"    total_con_match: {d['total_con_match']}   rango del nodo R ({id_r}): {d['rango_nodo_R']}")
        for t in d["top10"]:
            prov = [f"{p['to']} {p['punto']} ({p['rol_documental']})" for p in t["procedencias"]]
            corto = "; ".join(prov[:4]) + (f"; … (+{len(prov) - 4}, total {len(prov)})" if len(prov) > 4 else "")
            print(f"  {t['rango']:2d}  {t['puntaje_exacto']:>20s}  {t['tipo']:12s} {t['id']}")
            print(f"        etiqueta: {t['etiqueta']}")
            print(f"        procedencias: {corto}")
        for nombre in ("primera_aparicion_cualquier_procedencia", "primera_aparicion_criterio_generador"):
            print(f"  {nombre}:")
            for p, v in d[nombre].items():
                print(f"    {p:9s} " + (f"rango {v['rango']:4d}  {v['tipo']:12s} {v['id']}  «{v['etiqueta']}»"
                                         if v else "NO APARECE"))
    print(f"\ncontrol pregunta actual: medido {salida['control_actual']['medido']}")
    print(f"                         declarado {RESULTADO_BUSQUEDA_ACTUAL}")
    print(f"                         reproduce: {salida['control_actual']['reproduce']}")
    print(f"\nJSON: {OUT}  sha256 {hashlib.sha256(open(OUT, 'rb').read()).hexdigest()}")


if __name__ == "__main__":
    main()
