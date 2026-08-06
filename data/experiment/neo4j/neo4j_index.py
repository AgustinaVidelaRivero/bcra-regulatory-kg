"""
neo4j_index.py — Adaptador de las 3 tools del agente contra Neo4j.

Expone la MISMA interfaz que `GraphIndex` del harness (buscar_nodos /
ver_nodo / ver_vecinos, mismas firmas y mismos formatos de retorno), pero
resolviendo contra el grafo cargado en Neo4j por cargar_kg.py. NO está
inyectado en el harness ni en el pipeline de evaluación: queda listo para
inyección futura.

Decisiones de diseño
--------------------
1. `buscar_nodos` usa el índice full-text `nodos_fulltext` (label +
   descripcion + description, analyzer spanish). Esto es una divergencia
   DELIBERADA respecto del índice in-memory (que solo tokeniza label + id):
   la alcanzabilidad vía descripcion es la mejora que motiva la migración.
   El ranking es el score de Lucene (desc), con desempate determinístico
   por longitud de label y luego id (mismos desempates que el in-memory).
2. Paridad de formato estricta: el payload de salida usa exactamente las
   mismas claves que el in-memory. `tokens_matcheados` se calcula con la
   misma fórmula del harness (tokens de la consulta ∩ tokens de label+id,
   vía los helpers importados del harness — solo import, sin ediciones);
   puede valer 0 para hits que Lucene encontró vía descripcion: ese 0 es
   señal honesta de que el hit NO era alcanzable con el índice viejo. El
   score de Lucene NO se expone, para no alterar el payload que ve el agente.
3. La query del usuario se tokeniza con `_tokens` del harness (lowercase,
   sin acentos, alfanumérico) y se une con espacios (semántica OR de
   Lucene). Eso neutraliza los caracteres reservados de la sintaxis Lucene
   y replica el comportamiento tolerante del in-memory.
4. `ver_nodo` y `ver_vecinos` reconstruyen properties/provenances desde las
   propiedades canónicas `props_json` / `provenances_json` (fidelidad
   exacta al modelo del loader). `ver_vecinos` ordena por `r.orden`
   (posición de la arista en kg.edges) para reproducir el orden de
   inserción que expone el in-memory.

Uso
---
  from neo4j_index import Neo4jIndex
  from conexion import abrir_driver
  idx = Neo4jIndex(abrir_driver())
  idx.buscar_nodos("asociación mutual")
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

NEO4J_DIR = Path(__file__).resolve().parent
EVAL_DIR = NEO4J_DIR.parent / "evaluacion"
sys.path.insert(0, str(EVAL_DIR))
sys.path.insert(0, str(NEO4J_DIR))

# Solo IMPORT del cuarteto hasheado (no se edita): helpers léxicos idénticos.
from harness import _tokens, _short_props  # noqa: E402
from indices import INDICE_FULLTEXT  # noqa: E402


class Neo4jIndex:
    """Las 3 tools del agente resueltas contra Neo4j (misma interfaz que GraphIndex)."""

    def __init__(self, driver, indice_fulltext: str = INDICE_FULLTEXT):
        self.driver = driver
        self.indice = indice_fulltext

    # --- tool 1 ---
    def buscar_nodos(self, consulta: str, limite: int = 10) -> dict:
        toks = _tokens(consulta)
        if not toks:
            return {"consulta": consulta, "resultados": [], "total": 0}
        try:
            limite = max(1, min(int(limite), 50))
        except (TypeError, ValueError):
            limite = 10
        q_lucene = " ".join(toks)
        # Agregación server-side: el conteo total se resuelve en Neo4j y solo
        # el top-K viaja al cliente (props_json se lee únicamente para el
        # slice). Traer todos los hits al cliente multiplicaba ~20x la
        # latencia en consultas con cientos de matches.
        with self.driver.session() as session:
            rec = session.run(
                f"CALL db.index.fulltext.queryNodes('{self.indice}', $q) "
                "YIELD node, score "
                "WITH node, score "
                "ORDER BY score DESC, size(node.label) ASC, node.id ASC "
                "WITH collect(node) AS ns "
                "RETURN size(ns) AS total, "
                "       [x IN ns[0..$lim] | {id: x.id, type: x.type, "
                "        label: x.label, pj: x.props_json}] AS top",
                q=q_lucene, lim=limite,
            ).single()
        q_set = set(toks)
        resultados = [
            {
                "id": r["id"],
                "type": r["type"],
                "label": r["label"],
                "tokens_matcheados": len(q_set & set(_tokens(r["label"] or "")
                                                     + _tokens(r["id"] or ""))),
                "resumen_propiedades": _short_props(json.loads(r["pj"])),
            }
            for r in rec["top"]
        ]
        return {
            "consulta": consulta,
            "total_con_match": rec["total"],
            "resultados": resultados,
        }

    # --- tool 2 ---
    def ver_nodo(self, id: str) -> dict:
        with self.driver.session() as session:
            rec = session.run(
                "MATCH (n:Nodo {id: $id}) "
                "RETURN n.type AS type, n.label AS label, "
                "       n.props_json AS pj, n.provenances_json AS vj",
                id=id,
            ).single()
        if rec is None:
            return {"error": f"No existe un nodo con id '{id}'.",
                    "sugerencia": "Usá buscar_nodos para encontrar el id correcto."}
        return {
            "id": id,
            "type": rec["type"],
            "label": rec["label"],
            "properties": json.loads(rec["pj"]),
            "provenances": json.loads(rec["vj"]),
        }

    # --- tool 3 ---
    def ver_vecinos(self, id: str, direccion: str = "ambas", limite: int = 40) -> dict:
        with self.driver.session() as session:
            rec = session.run(
                "MATCH (n:Nodo {id: $id}) RETURN n.label AS label", id=id,
            ).single()
            if rec is None:
                return {"error": f"No existe un nodo con id '{id}'.",
                        "sugerencia": "Usá buscar_nodos para encontrar el id correcto."}
            direccion = (direccion or "ambas").lower()
            if direccion not in ("ambas", "salientes", "entrantes"):
                direccion = "ambas"

            out = session.run(
                "MATCH (n:Nodo {id: $id})-[r]->(v:Nodo) "
                "RETURN type(r) AS relation, v.id AS vecino_id, "
                "       v.label AS vecino_label, r.provenances_json AS vj "
                "ORDER BY r.orden", id=id,
            ).data()
            inn = session.run(
                "MATCH (n:Nodo {id: $id})<-[r]-(v:Nodo) "
                "RETURN type(r) AS relation, v.id AS vecino_id, "
                "       v.label AS vecino_label, r.provenances_json AS vj "
                "ORDER BY r.orden", id=id,
            ).data()

        def _fila(r):
            return {
                "relation": r["relation"],
                "vecino_id": r["vecino_id"],
                "vecino_label": r["vecino_label"],
                "provenances": json.loads(r["vj"]),
            }

        res = {
            "id": id,
            "label": rec["label"],
            "n_salientes_total": len(out),
            "n_entrantes_total": len(inn),
        }
        if direccion in ("ambas", "salientes"):
            filas = [_fila(r) for r in out]
            res["salientes"] = filas[:limite]
            res["salientes_truncado"] = len(filas) > limite
        if direccion in ("ambas", "entrantes"):
            filas = [_fila(r) for r in inn]
            res["entrantes"] = filas[:limite]
            res["entrantes_truncado"] = len(filas) > limite
        return res
