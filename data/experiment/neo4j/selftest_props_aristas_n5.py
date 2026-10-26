"""
selftest_props_aristas_n5.py — U-NAV-DISENO, N5 (decisión 6): selftest de la exportación de las propiedades de las
aristas a Neo4j (cargar_kg.PROPS_ARISTA_N5 y MARCAS_ARISTA_N5), sobre un grafo SINTÉTICO de seis nodos.

Los grafos r2b del registro no traen `no_verificada_e3` ni aristas de sujeto derivado; este grafo trae cada caso:
`alcance`, `destino` y `evidencia` de una remite_a; las marcas de la cola (`cola_humana`, `cola_chunks`, `estado_e3`);
`no_verificada_e3` y `rol_fuente` fuera de `properties`; un valor dict (va como json) y una arista sin ninguna.

Casos (S1 a S8):
  S1  las propiedades llegan a Neo4j con su valor y su tipo, solo en las aristas que las traen;
  S2  paridad loader = Neo4j de esas propiedades (huella_props_aristas_*);
  S3  dos cargas dejan el mismo estado (idempotencia);
  S4  `estado_sin_props_n5` es el `estado` de la misma carga sin esas propiedades ni la clave de KG_Meta (se las
      quita de Neo4j y se recalcula `estado`);
  S5  `contenido` es el mismo con y sin esas propiedades;
  S6  las tres tools de hoy dan lo mismo en Neo4j y en memoria (ver_vecinos y ver_nodo byte a byte, modo paridad);
  S7  si la vista no está alineada con el crudo, las marcas de fuera de `properties` no se exportan;
  S8  KG_Meta lleva `props_aristas` con la lista exportada.
Al terminar borra de Neo4j el grafo sintético, su KG_Meta, su índice y su constraint. El kg.json sintético vive en un
directorio temporal fuera del repo que se borra al salir; por eso `cargar_kg.rel_repo` (que solo arma el `kg_path` del
KG_Meta y exige una ruta bajo el repo) se reemplaza en memoria, en este proceso, por una que da el nombre del archivo.

Uso: NEO4J_URI=bolt://... .venv/bin/python -B selftest_props_aristas_n5.py   (sale con 1 si falla un caso)
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

NEO4J_DIR = Path(__file__).resolve().parent
CODE_T0 = NEO4J_DIR.parent / "tanda0" / "code"
for _p in (str(NEO4J_DIR), str(CODE_T0)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import comun_tanda0 as T0  # noqa: E402  (registro en memoria de la vista gen3)
import grafos as G  # noqa: E402
import cargar_kg as CK  # noqa: E402
from harness import GraphIndex  # noqa: E402  (solo IMPORT del cuarteto)
from neo4j_index import Neo4jIndex  # noqa: E402

CLAVE = "KG_Selftest_PropsAristas_N5"
EV2_KEY = "selftest_props_aristas_n5"


def _prov(punto: str) -> dict:
    return {"to": "sint", "archivo": "TO_sintetico.pdf", "punto": punto, "rol_documental": "punto_propio",
            "tramo": f"tramo de {punto}", "tramo_verificado": "exacta", "chunk_id": f"sint::{punto}",
            "paginas": [1], "ancestros": []}


def grafo_sintetico() -> dict:
    nodos = [{"id": f"N{i}", "type": t, "label": f"nodo sintético {i}",
              "properties": {"descripcion": f"descripción {i}"}, "provenance": _prov(f"1.{i}"),
              "provenances": [_prov(f"1.{i}")]} for i, t in
             enumerate(["Obligacion", "Condicion", "Sujeto", "Excepcion", "Restriccion", "TextoOrdenado"], 1)]
    def arista(s, r, t, props=None, **fuera):
        e = {"source": s, "target": t, "relation": r, "provenance": _prov("1.1"), "provenances": [_prov("1.1")],
             "properties": props or {}}
        e.update(fuera)
        return e
    aristas = [
        arista("N1", "remite_a", "N2", {"alcance": "interna", "destino": "sint::1.2", "evidencia": "conforme al punto 1.2."}),
        arista("N1", "aplica_a", "N3", rol_fuente="derivada_del_alcance"),
        arista("N4", "exceptua", "N1", no_verificada_e3=True),
        arista("N5", "limita", "N1", {"cola_humana": "true", "cola_chunks": ["sint::1.5"], "estado_e3": "cola_humana"}),
        arista("N2", "condiciona", "N1", {"alcance": {"de": "dict", "va": "como json"}}),
        arista("N1", "establecida_en", "N6"),
    ]
    return {"nodes": nodos, "edges": aristas}


def main() -> int:
    fallas = []

    def caso(nombre: str, ok: bool, detalle: str = "") -> None:
        print(f"  {'✓' if ok else '✗'} {nombre}{(' — ' + detalle) if detalle else ''}")
        if not ok:
            fallas.append(nombre)

    with tempfile.TemporaryDirectory(prefix="selftest_props_n5_") as tmp:
        path = Path(tmp) / "kg.json"
        path.write_text(json.dumps(grafo_sintetico(), ensure_ascii=False), encoding="utf-8")
        T0.TANDA0[EV2_KEY] = {"path": path, "sha256": G.sha256_de(path), "label": "selftest_props_n5_mem"}
        T0.registrar_tanda0()
        G.GRAFOS[CLAVE] = {"nombre_canonico": "KG-Selftest-PropsAristas-N5", "label": CLAVE, "path": path,
                           "sha256": G.sha256_de(path), "commit_sellado": "SINTETICO", "n_nodos": 6, "n_aristas": 6,
                           "ev2_key": EV2_KEY, "vista_runtime": "comun_tanda0.cargar_runtime_gen3 (sintético)",
                           "indice_fulltext": "nodos_fulltext_kg_selftest_propsaristas_n5"}
        kg = T0.cargar_runtime_gen3(EV2_KEY)
        CK.rel_repo = lambda p: f"(sintético, temporal)/{Path(p).name}"
        driver = CK.abrir_driver()
        try:
            CK.cargar_en_neo4j(driver, kg, CLAVE)
            with driver.session() as s:
                filas = s.run(f"MATCH (a:`{CLAVE}`)-[r]->(b:`{CLAVE}`) RETURN r.orden AS o, type(r) AS rel, "
                              "properties(r) AS p ORDER BY r.orden").data()
            p = {f["o"]: {k: v for k, v in f["p"].items() if k not in ("orden", "provenances_json")} for f in filas}
            esperado = {0: {"alcance": "interna", "destino": "sint::1.2", "evidencia": "conforme al punto 1.2."},
                        1: {"rol_fuente": "derivada_del_alcance"}, 2: {"no_verificada_e3": True},
                        3: {"cola_humana": "true", "cola_chunks": ["sint::1.5"], "estado_e3": "cola_humana"},
                        4: {"alcance": json.dumps({"de": "dict", "va": "como json"}, ensure_ascii=False)}, 5: {}}
            caso("S1 propiedades en Neo4j, con su valor y su tipo", p == esperado,
                 "" if p == esperado else f"leído {p}")
            pl, pn = CK.huella_props_aristas_loader(kg, CLAVE), CK.huella_props_aristas_neo4j(driver, CLAVE)
            caso("S2 paridad loader = Neo4j de las propiedades", pl == pn)
            h1 = CK.huella_neo4j(driver, CLAVE)
            CK.cargar_en_neo4j(driver, kg, CLAVE)
            h2 = CK.huella_neo4j(driver, CLAVE)
            caso("S3 idempotencia (dos cargas, mismo estado)", h1 == h2)
            meta = CK.leer_meta(driver, CLAVE)
            caso("S8 KG_Meta.props_aristas", meta.get(CK.CLAVE_META_N5) == list(CK.EXPORTADAS_ARISTA_N5),
                 str(meta.get(CK.CLAVE_META_N5)))
            gi, ni = GraphIndex(kg), Neo4jIndex(driver, grafo=CLAVE, modo="paridad")
            iguales = all(json.dumps(gi.ver_vecinos(n, d), ensure_ascii=False)
                          == json.dumps(ni.ver_vecinos(n, d), ensure_ascii=False)
                          for n in ("N1", "N2", "N3", "N4", "N5", "N6") for d in ("ambas", "salientes", "entrantes"))
            iguales &= all(json.dumps(gi.ver_nodo(n), ensure_ascii=False) == json.dumps(ni.ver_nodo(n), ensure_ascii=False)
                           for n in ("N1", "N2", "N3", "N4", "N5", "N6", "inexistente"))
            caso("S6 las tres tools de hoy, iguales en Neo4j y en memoria", iguales)
            quitar = ", ".join(f"r.{k}" for k in CK.EXPORTADAS_ARISTA_N5)
            with driver.session() as s:
                s.run(f"MATCH (:`{CLAVE}`)-[r]->(:`{CLAVE}`) REMOVE {quitar}").consume()
                s.run(f"MATCH (m:KG_Meta {{grafo: $g}}) REMOVE m.{CK.CLAVE_META_N5}", g=CLAVE).consume()
            h3 = CK.huella_neo4j(driver, CLAVE)
            caso("S4 estado_sin_props_n5 = estado sin esas propiedades", h3["estado"] == h2["estado_sin_props_n5"])
            caso("S5 contenido igual con y sin esas propiedades", h3["contenido"] == h2["contenido"])
            kg.edges.reverse()
            n5 = CK.props_aristas_n5(kg, CLAVE)
            sin_marcas = not n5["alineadas"] and all(not (set(f) & set(CK.MARCAS_ARISTA_N5)) for f in n5["filas"])
            caso("S7 vista no alineada: sin las marcas de fuera de properties", sin_marcas)
            kg.edges.reverse()
        finally:
            with driver.session() as s:
                s.run(f"MATCH (n:`{CLAVE}`) DETACH DELETE n").consume()
                s.run("MATCH (m:KG_Meta {grafo: $g}) DELETE m", g=CLAVE).consume()
                s.run(f"DROP INDEX {G.GRAFOS[CLAVE]['indice_fulltext']} IF EXISTS").consume()
                s.run(f"DROP CONSTRAINT {CLAVE.lower()}_id IF EXISTS").consume()
                quedan = s.run(f"MATCH (n:`{CLAVE}`) RETURN count(n) AS c").single()["c"]
            driver.close()
            print(f"  limpieza: nodos del grafo sintético que quedan en Neo4j = {quedan}")
    print(f"\nSELFTEST props aristas N5: {'OK' if not fallas else 'FALLAS: ' + ', '.join(fallas)}")
    return 0 if not fallas else 1


if __name__ == "__main__":
    sys.exit(main())
