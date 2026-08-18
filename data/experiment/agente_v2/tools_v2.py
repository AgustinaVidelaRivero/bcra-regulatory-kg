"""
tools_v2.py — Tools v2 del agente KG-RAG sobre Neo4j (U-A1.2, plan de tesis
carril A / bloque A1).

Módulo APARTE del harness congelado: `GraphIndex`, `GraphAgent`, `TOOLS`,
`SYSTEM_PROMPT` y `MODEL` de `data/experiment/evaluacion/harness.py` NO se
editan; de allí solo se IMPORTAN los helpers léxicos (`_tokens`,
`_short_props`) — vía `neo4j_index` — y, en `agente_v2.py`, el loop del
agente. El backend Neo4j (`data/experiment/neo4j/`, U-A1.1) tampoco se
reescribe: `Neo4jIndex` se importa y se usa tal cual (modo `fulltext` para la
búsqueda; `ver_nodo` reutilizado sin cambios).

Las tres tools y su relación con el backlog
-------------------------------------------
  buscar_nodos_v2(consulta, limite=10)
      BM25 de Lucene sobre label + descripcion + description + id_texto
      (índice por grafo de A1.1, analyzer `spanish`). MISMA firma de salida
      que la tool actual: {consulta, total_con_match, resultados:[{id, type,
      label, tokens_matcheados, resumen_propiedades}]}, mismo clamp de
      `limite` (1..50; no entero → 10) y mismo retorno para consulta sin
      tokens ({consulta, resultados:[], total:0}). Cambios de spec
      DECLARADOS (semánticos, sin cambio de claves): `total_con_match` cuenta
      hits del índice (≥1 término tras stemming/stopwords en alguno de los
      cuatro campos) y `tokens_matcheados` puede valer 0 (hit solo vía
      descripción). Es exactamente `Neo4jIndex(modo='fulltext').buscar_nodos`.
      Defecto que ataca: alcanzabilidad léxica por label/id solamente
      (CQ-031 / CQN2-015 en docs/decision_backend_grafo.md §1; BKL-0003,
      BKL-0022 como huérfano léxico). La medición real es A1.4.

  ver_vecinos_v2(id, relacion=None, pagina=1, por_pagina=40)
      BIDIRECCIONAL SIEMPRE: salientes y entrantes en una sola llamada,
      separadas y rotuladas; NO existe parámetro `direccion` — el defecto
      BKL-0027 (el agente pidió 'salientes', recibió 0 y nunca pidió los 168
      entrantes que el propio output declaraba) queda resuelto por diseño,
      no por default. Filtro opcional por tipo de relación exacto.
      Paginación por OFFSET (número de página 1-based, ventana `por_pagina`
      por dirección) sobre el orden estable `r.orden` (posición de la arista
      en kg.edges, el mismo orden que el in-memory): stateless, reproducible
      y trivialmente auditable — un cursor opaco no aporta nada sobre un
      orden total fijo y sin escrituras concurrentes. Cada dirección
      declara total (con filtro), cantidad de páginas, página siguiente
      (null si no hay más) y conteo por relación (sin filtro). Defecto que
      ataca: BKL-0022 (huérfano léxico visible solo si cae dentro de la
      ventana de 40 de ver_vecinos — con paginación es alcanzable en alguna
      página cualquiera sea su posición) y BKL-0027.
      Default por_pagina=40, justificado contra la ventana actual (40):
        (i) mismo techo de payload por llamada que v1 (v1 'ambas' ya devuelve
            hasta 40+40 filas; mediana 297 / 244 chars por ítem de arista
            medidos sobre todas las aristas de cada grafo, ver README §C.4) — la
            variable de A1.4 es el alcance (bidireccionalidad + paginación +
            filtro), no el tamaño de cada respuesta;
        (ii) la ventana solo actúa en la cola: 11/4.469 (KG-Refinado) y
            12/6.178 (KG-Reextraído) nodos superan 40 en alguna dirección
            (medido en el selftest), así que 40 resuelve en una página el
            99,7 % de los nodos y la paginación queda como mecanismo de cola;
        (iii) el huérfano de BKL-0022 está hoy en la posición 7 de sus 145
            entrantes: con 40 sigue en la página 1 (y con cualquier ventana
            menor, en la página ceil(7/w) — el selftest lo muestra).
      El máximo de `por_pagina` también es 40 (no se permite superar el
      techo de v1 por llamada).

  ver_nodo_v2(id)
      SIN cambio: adaptador fino sobre `Neo4jIndex.ver_nodo` (byte-idéntico
      al harness, verificado en A1.1). Se declara así.

  contexto_de(id, saltos<=2, presupuesto_tokens)  — NO IMPLEMENTADA
      Punto de extensión declarado (firma + semántica del presupuesto) para
      que A1.4 decida. Lanza NotImplementedError.

Formato de salida de ver_vecinos_v2 (claves de primer nivel, en este orden)
-------------------------------------------------------------------------
  id, label,
  n_salientes_total, n_entrantes_total          (sin filtro; claves de v1)
  filtro_relacion (str|null), pagina, por_pagina,
  salientes_total, salientes_paginas, salientes_pagina_siguiente,
  salientes_por_relacion ({relacion: conteo}, sin filtro),
  salientes: [{relation, vecino_id, vecino_label, provenances}],
  entrantes_total, entrantes_paginas, entrantes_pagina_siguiente,
  entrantes_por_relacion, entrantes: [...]
Las dos listas viven en el PRIMER NIVEL del dict (no anidadas en sub-dicts):
`GraphAgent._collect_provs` (harness, importado sin cambios por
GraphAgentV2) recorre solo `result.values()` que son listas de dicts con
`provenances`; un layout anidado dejaría las provenances de ver_vecinos_v2
fuera de `seen_provenances` y toda cita saldría "no vista". El selftest lo
verifica.
Ítems de las listas: mismas claves y mismo contenido que v1 (`relation`,
`vecino_id`, `vecino_label`, `provenances`) en el mismo orden (`r.orden`).

Uso
---
  from tools_v2 import ToolsV2
  from conexion import abrir_driver
  t = ToolsV2(abrir_driver(), grafo="KG_Refinado")
  t.ver_vecinos_v2("Sujeto_rol_sujeto_obligado_proteccion", relacion="miembro_de")
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

AGENTE_V2_DIR = Path(__file__).resolve().parent
NEO4J_DIR = AGENTE_V2_DIR.parent / "neo4j"
for _p in (str(NEO4J_DIR), str(AGENTE_V2_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from grafos import GRAFOS, GRAFO_DEFAULT  # noqa: E402  (A1.1; agrega EVAL_DIR al path)
from neo4j_index import Neo4jIndex  # noqa: E402  (A1.1; solo import)

SPECS_PATH = AGENTE_V2_DIR / "specs_tools_v2.json"

# Defaults declarados de las tools v2.
LIMITE_DEFAULT = 10          # = harness (buscar_nodos)
POR_PAGINA_DEFAULT = 40      # = ventana actual de ver_vecinos (justificación en el docstring)
POR_PAGINA_MAX = 40          # techo de payload por llamada = v1
NOMBRES_API = ("buscar_nodos", "ver_nodo", "ver_vecinos")   # nombres que ve el modelo (= v1)


def cargar_specs() -> list:
    """TOOLS_V2: las specs JSON que lee el modelo (archivo propio, no el harness)."""
    with open(SPECS_PATH, encoding="utf-8") as f:
        specs = json.load(f)
    nombres = tuple(s["name"] for s in specs)
    if nombres != NOMBRES_API:
        raise ValueError(f"specs_tools_v2.json: nombres {nombres} != {NOMBRES_API}")
    return specs


TOOLS_V2 = cargar_specs()


class ToolsV2:
    """Las tres tools v2 resueltas contra Neo4j (Neo4jIndex de A1.1, modo fulltext)."""

    def __init__(self, driver, grafo: str = GRAFO_DEFAULT):
        if grafo not in GRAFOS:
            raise KeyError(f"grafo desconocido: {grafo!r}; válidos: {list(GRAFOS)}")
        self.driver = driver
        self.grafo = grafo
        self.label = GRAFOS[grafo]["label"]
        # buscar_nodos_v2 = modo fulltext de A1.1; ver_nodo idéntico en ambos modos.
        self.index = Neo4jIndex(driver, grafo=grafo, modo="fulltext")

    # ------------------------------------------------------------------ #
    # tool 1 — buscar_nodos_v2
    # ------------------------------------------------------------------ #
    def buscar_nodos_v2(self, consulta: str, limite: int = LIMITE_DEFAULT) -> dict:
        """BM25 (índice full-text por grafo). Misma firma de salida que la tool actual."""
        return self.index.buscar_nodos(consulta, limite)

    # ------------------------------------------------------------------ #
    # tool 2 — ver_nodo_v2 (adaptador fino, sin cambio)
    # ------------------------------------------------------------------ #
    def ver_nodo_v2(self, id: str) -> dict:
        return self.index.ver_nodo(id)

    # ------------------------------------------------------------------ #
    # tool 3 — ver_vecinos_v2
    # ------------------------------------------------------------------ #
    @staticmethod
    def _entero(v, default: int, minimo: int, maximo: int | None) -> int:
        try:
            x = int(v)
        except (TypeError, ValueError):
            return default
        if isinstance(v, bool):
            return default
        x = max(minimo, x)
        if maximo is not None:
            x = min(x, maximo)
        return x

    def ver_vecinos_v2(self, id: str, relacion: str | None = None,
                       pagina: int = 1, por_pagina: int = POR_PAGINA_DEFAULT) -> dict:
        pagina = self._entero(pagina, 1, 1, None)
        por_pagina = self._entero(por_pagina, POR_PAGINA_DEFAULT, 1, POR_PAGINA_MAX)
        if relacion is not None and not isinstance(relacion, str):
            relacion = str(relacion)
        if relacion == "":
            relacion = None
        L = self.label
        skip = (pagina - 1) * por_pagina

        with self.driver.session() as session:
            rec = session.run(
                f"MATCH (n:`{L}` {{id: $id}}) RETURN n.label AS label", id=id).single()
            if rec is None:
                return {"error": f"No existe un nodo con id '{id}'.",
                        "sugerencia": "Usá buscar_nodos para encontrar el id correcto."}

            def _conteos(patron: str) -> dict:
                filas = session.run(
                    f"MATCH (n:`{L}` {{id: $id}}){patron}(:`{L}`) "
                    "RETURN type(r) AS rel, count(*) AS c", id=id).data()
                # Orden determinístico en Python (conteo desc, nombre asc);
                # no se delega a la collation del servidor.
                return {f["rel"]: f["c"] for f in
                        sorted(filas, key=lambda f: (-f["c"], f["rel"]))}

            def _pagina(patron: str) -> list:
                filas = session.run(
                    f"MATCH (n:`{L}` {{id: $id}}){patron}(v:`{L}`) "
                    "WHERE $rel IS NULL OR type(r) = $rel "
                    "RETURN type(r) AS relation, v.id AS vecino_id, "
                    "       v.label AS vecino_label, r.provenances_json AS vj "
                    "ORDER BY r.orden SKIP $skip LIMIT $lim",
                    id=id, rel=relacion, skip=skip, lim=por_pagina).data()
                return [{"relation": f["relation"], "vecino_id": f["vecino_id"],
                         "vecino_label": f["vecino_label"],
                         "provenances": json.loads(f["vj"])} for f in filas]

            out_rel = _conteos("-[r]->")
            in_rel = _conteos("<-[r]-")
            out_items = _pagina("-[r]->")
            in_items = _pagina("<-[r]-")

        def _bloque(prefijo: str, por_rel: dict, items: list) -> dict:
            total_sf = sum(por_rel.values())
            total = por_rel.get(relacion, 0) if relacion is not None else total_sf
            paginas = (total + por_pagina - 1) // por_pagina if total else 0
            return {
                f"{prefijo}_total": total,
                f"{prefijo}_paginas": paginas,
                f"{prefijo}_pagina_siguiente": (pagina + 1) if pagina < paginas else None,
                f"{prefijo}_por_relacion": por_rel,
                prefijo: items,
            }

        res = {
            "id": id,
            "label": rec["label"],
            "n_salientes_total": sum(out_rel.values()),
            "n_entrantes_total": sum(in_rel.values()),
            "filtro_relacion": relacion,
            "pagina": pagina,
            "por_pagina": por_pagina,
        }
        res.update(_bloque("salientes", out_rel, out_items))
        res.update(_bloque("entrantes", in_rel, in_items))
        return res

    # ------------------------------------------------------------------ #
    # punto de extensión — contexto_de (NO implementada en A1.2)
    # ------------------------------------------------------------------ #
    def contexto_de(self, id: str, saltos: int = 1, presupuesto_tokens: int = 2000) -> dict:
        """PUNTO DE EXTENSIÓN (A1.4 decide). No implementada.

        Firma propuesta: contexto_de(id, saltos<=2, presupuesto_tokens).
        Semántica declarada del presupuesto en tokens:
          - Recorrido en anchura desde `id` hasta `saltos` (1 o 2; >2 se
            rechaza) en AMBAS direcciones, orden determinístico (salto asc,
            luego `r.orden` asc de la arista que introduce cada nodo).
          - Cada ítem (nodo abierto = type/label/properties/provenances +
            aristas que lo conectan) se serializa como lo haría el harness
            (`json.dumps(x, ensure_ascii=False)`); su costo se estima con un
            estimador FIJO y determinístico declarado en la implementación
            (p. ej. ceil(len(serializado)/4)), sin llamar a un tokenizer
            remoto ni a la API (costo 0, reproducible byte a byte).
          - Se agregan ítems en ese orden mientras el acumulado ≤
            presupuesto_tokens; el primero que no entra corta el recorrido.
          - La salida DECLARA: presupuesto_tokens, tokens_estimados,
            estimador (nombre/fórmula), saltos, n_incluidos, n_omitidos,
            truncado (bool) y las provenances en listas de primer nivel
            (compatibles con GraphAgent._collect_provs).
        Nada de esto se implementa en A1.2: queda como firma para que A1.4
        decida si la tool entra en el experimento y con qué default.
        """
        raise NotImplementedError(
            "contexto_de: punto de extensión declarado en A1.2, no implementado "
            "(firma: contexto_de(id, saltos<=2, presupuesto_tokens); ver docstring).")

    # ------------------------------------------------------------------ #
    # despacho por nombre de API (lo usa GraphAgentV2._run_tool)
    # ------------------------------------------------------------------ #
    def despachar(self, name: str, args: dict):
        args = args or {}
        if name == "buscar_nodos":
            return self.buscar_nodos_v2(args.get("consulta", ""),
                                        args.get("limite", LIMITE_DEFAULT))
        if name == "ver_nodo":
            return self.ver_nodo_v2(args.get("id", ""))
        if name == "ver_vecinos":
            return self.ver_vecinos_v2(args.get("id", ""),
                                       relacion=args.get("relacion"),
                                       pagina=args.get("pagina", 1),
                                       por_pagina=args.get("por_pagina", POR_PAGINA_DEFAULT))
        return {"error": f"tool desconocida: {name}"}
