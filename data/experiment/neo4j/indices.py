"""
indices.py — Índice full-text Lucene sobre el grafo cargado en Neo4j + tests
dirigidos contra los dos defectos conocidos de alcanzabilidad del índice
léxico in-memory (que solo tokeniza label + id).

Índice creado
-------------
  nodos_fulltext: FULLTEXT sobre :Nodo(label, descripcion, description)
    - `label`: paridad con el índice in-memory.
    - `descripcion` y `description`: la mejora a demostrar — el grafo usa
      ambas claves (1.863 nodos con `descripcion`, 1.101 con `description`);
      indexar solo una dejaría un cuarto del grafo sin cobertura semántica.
    - `nota_fuente` EXCLUIDA (decisión): solo 2 nodos la tienen y su contenido
      es meta-anotación editorial sobre la extracción ("descripcion verbatim
      del inciso…", "el label es interpretativo…"), no contenido normativo;
      indexarla agregaría ruido léxico (p. ej. "verbatim", "PDF") sin aportar
      alcanzabilidad regulatoria.
  Analyzer: `spanish` (stemming + stopwords castellanas de Lucene). El default
  `standard-no-stop-words` no stemmea: "asociación mutual" no matchearía
  "asociaciones mutuales" de la descripcion — precisamente el caso BKL-0003.

Tests dirigidos (se corren con `python indices.py`)
---------------------------------------------------
  (a) BKL-0003 — la búsqueda "asociación mutual" (y variantes) debe encontrar
      Excepcion_otros_proveedores_no_financieros_de_credito_alcanzados_por_
      las_normas_sobre_prov_5f95b9.
      NOTA de estado: en el grafo vigente el label de ese nodo YA fue
      enriquecido en capa KG con "asociación mutual o cooperativa"
      (recuperación léxica, laudo C6), de modo que el índice de label+id
      también lo encuentra hoy. La mejora estructural del full-text se
      demuestra con el sub-test (a2): queries con texto verbatim del inciso
      que vive SOLO en la `descripcion` ("excepto que se trate de…") — ahí
      el índice de label+id no tiene señal discriminante y el full-text sí.
      El full-text vuelve innecesario el parche de label como mecanismo de
      alcanzabilidad: toda descripcion queda indexada de fábrica.
  (b) BKL-0027 — los 7 vecinos entrantes `miembro_de` de
      Sujeto_rol_sujeto_obligado_proteccion deben recuperarse tanto con
      query de dirección explícita como con query bidireccional.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from conexion import abrir_driver  # noqa: E402

INDICE_FULLTEXT = "nodos_fulltext"

NODO_BKL0003 = ("Excepcion_otros_proveedores_no_financieros_de_credito_"
                "alcanzados_por_las_normas_sobre_prov_5f95b9")
NODO_BKL0027 = "Sujeto_rol_sujeto_obligado_proteccion"


def crear_indice(driver) -> None:
    with driver.session() as session:
        session.run(
            f"CREATE FULLTEXT INDEX {INDICE_FULLTEXT} IF NOT EXISTS "
            "FOR (n:Nodo) ON EACH [n.label, n.descripcion, n.description] "
            "OPTIONS {indexConfig: {`fulltext.analyzer`: 'spanish'}}"
        ).consume()
        session.run("CALL db.awaitIndexes(300)").consume()
    print(f"índice {INDICE_FULLTEXT} creado y online (analyzer=spanish).")


def buscar_fulltext(session, consulta: str, limite: int = 10) -> list:
    res = session.run(
        f"CALL db.index.fulltext.queryNodes('{INDICE_FULLTEXT}', $q) "
        "YIELD node, score RETURN node.id AS id, node.type AS type, "
        "node.label AS label, score ORDER BY score DESC LIMIT $lim",
        q=consulta, lim=limite,
    )
    return [dict(r) for r in res]


def test_bkl_0003(driver) -> bool:
    """'asociación mutual' y variantes deben rankear el nodo de la excepción."""
    variantes = [
        "asociación mutual",
        "asociacion mutual",           # sin tilde
        "asociaciones mutuales",       # plural (forma de la descripcion)
        "mutual cooperativa crédito",
    ]
    ok_global = True
    with driver.session() as session:
        for v in variantes:
            hits = buscar_fulltext(session, v, limite=10)
            pos = next((i for i, h in enumerate(hits) if h["id"] == NODO_BKL0003), None)
            estado = f"✓ pos {pos + 1}/10" if pos is not None else "✗ NO aparece en top-10"
            print(f"  [BKL-0003] {v!r:38s} -> {estado}  ({len(hits)} hits)")
            if pos is None:
                ok_global = False
    return ok_global


def test_bkl_0003_descripcion(driver) -> bool:
    """Sub-test (a2): fragmentos verbatim del inciso presentes SOLO en la
    descripcion (no en label/id) deben rankear el nodo en el top-3."""
    fragmentos = [
        "excepto que se trate de asociaciones mutuales",   # verbatim inciso
        "otros proveedores no financieros de crédito",     # arranque verbatim
    ]
    ok_global = True
    with driver.session() as session:
        for frag in fragmentos:
            hits = buscar_fulltext(session, frag, limite=10)
            pos = next((i for i, h in enumerate(hits) if h["id"] == NODO_BKL0003), None)
            estado = f"✓ pos {pos + 1}/10" if pos is not None and pos < 3 else \
                     (f"~ pos {pos + 1}/10 (fuera del top-3)" if pos is not None
                      else "✗ NO aparece en top-10")
            print(f"  [BKL-0003/desc] {frag!r:52s} -> {estado}")
            if pos is None or pos >= 3:
                ok_global = False
    return ok_global


def test_bkl_0027(driver) -> bool:
    """Los 7 miembro_de entrantes al rol deben salir en query dirigida y bidireccional."""
    ok = True
    with driver.session() as session:
        dirigida = session.run(
            "MATCH (m:Nodo)-[r:miembro_de]->(rol:Nodo {id: $id}) "
            "RETURN m.id AS id ORDER BY id", id=NODO_BKL0027,
        ).value("id")
        print(f"  [BKL-0027] dirección explícita (entrantes): {len(dirigida)} miembros")
        for mid in dirigida:
            print(f"      - {mid}")
        if len(dirigida) != 7:
            ok = False

        bidi = session.run(
            "MATCH (rol:Nodo {id: $id})-[r:miembro_de]-(m:Nodo) "
            "RETURN m.id AS id ORDER BY id", id=NODO_BKL0027,
        ).value("id")
        print(f"  [BKL-0027] bidireccional: {len(bidi)} miembros "
              f"({'mismo conjunto ✓' if sorted(bidi) == sorted(dirigida) else 'DIFIERE ✗'})")
        if sorted(bidi) != sorted(dirigida):
            ok = False
    return ok


def main():
    driver = abrir_driver()
    try:
        crear_indice(driver)
        print("\ntest BKL-0003 (variantes de 'asociación mutual'):")
        ok_a = test_bkl_0003(driver)
        print("\ntest BKL-0003/desc (verbatim solo-descripcion — la mejora estructural):")
        ok_a2 = test_bkl_0003_descripcion(driver)
        print("\ntest BKL-0027 (vecinos entrantes del rol de sujetos):")
        ok_b = test_bkl_0027(driver)
    finally:
        driver.close()
    print(f"\nRESULTADO: BKL-0003 {'OK' if ok_a else 'FALLA'} | "
          f"BKL-0003/desc {'OK' if ok_a2 else 'FALLA'} | "
          f"BKL-0027 {'OK' if ok_b else 'FALLA'}")
    sys.exit(0 if (ok_a and ok_a2 and ok_b) else 1)


if __name__ == "__main__":
    main()
