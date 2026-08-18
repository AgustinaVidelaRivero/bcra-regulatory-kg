"""
agente_celda.py — Backend de tools y agente POR CELDA de la ablación (U-A1.4).

Cada celda sellada (`../celdas/celda_<id>.json`, verificada por sha en
`comun_corrida.cargar_celda`) declara su prompt del sistema, sus specs y el
backend de cada tool (pre-registro §1). Acá se ensambla EXACTAMENTE eso:

  BackendCelda(driver, celda): despacho determinístico de las tres tools
      contra Neo4j según los factores de la celda —
        buscar_nodos : Neo4jIndex(modo='paridad'|'fulltext').buscar_nodos(consulta, limite)
                       (fulltext == ToolsV2.buscar_nodos_v2, es el mismo Neo4jIndex)
        ver_nodo     : Neo4jIndex.ver_nodo(id)            [idéntico en todas]
        ver_vecinos  : v1 -> Neo4jIndex.ver_vecinos(id, direccion)   (firma del harness)
                       v2 -> ToolsV2.ver_vecinos_v2(id, relacion, pagina, por_pagina)
      Los argumentos se leen de `args` con los MISMOS defaults que
      `harness.GraphAgent._run_tool` (v1) y `ToolsV2.despachar` (v2).
      Se usa tanto en el agente (corrida) como en el re-ejecutor v2-aware del
      replay (`replay_ablacion.py`), así el replay ejecuta el mismo despacho.

  AgenteCelda(GraphAgentV2): el agente Haiku congelado del harness con
      `ask` = copia verificada (2 sustituciones, agente_v2) y, POR CELDA,
      `system_prompt` / `tools` cargados de la celda sellada y `_run_tool`
      despachando a BackendCelda. Captura el output ÍNTEGRO de cada tool call
      (steps_full, patrón runner_ev2.FullCaptureAgent) más la latencia por
      llamada de tool. Sin API acá: el cliente se inyecta (real o falso).

Invariantes verificados en construcción (fallan ruidosamente):
  - control C00: system_prompt == harness.SYSTEM_PROMPT y tools == harness.TOOLS;
  - C11: system_prompt == SYSTEM_PROMPT_V2_PROPUESTO y tools == TOOLS_V2;
  - sha del prompt y de las specs cargadas == manifest sellado.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

CORRIDA_DIR = Path(__file__).resolve().parent
if str(CORRIDA_DIR) not in sys.path:
    sys.path.insert(0, str(CORRIDA_DIR))

from comun_corrida import GRAFO, KG_REFINADO_SHA256, sha_json, sha_texto  # noqa: E402

import harness  # noqa: E402  (cuarteto: solo import)
from agente_v2 import (GraphAgentV2, SYSTEM_PROMPT_V2_PROPUESTO,  # noqa: E402
                       verificar_ask_copiado)
from neo4j_index import Neo4jIndex  # noqa: E402  (A1.1)
from tools_v2 import LIMITE_DEFAULT, POR_PAGINA_DEFAULT, TOOLS_V2, ToolsV2  # noqa: E402  (A1.2)


class BackendCelda:
    """Las 3 tools resueltas contra Neo4j según los factores de la celda."""

    def __init__(self, driver, celda: dict, grafo: str = GRAFO):
        self.celda_id = celda["celda_id"]
        self.retriever = celda["retriever"]      # 'booleano' | 'bm25'
        self.tools_version = celda["tools"]      # 'v1' | 'v2'
        if self.retriever not in ("booleano", "bm25") or self.tools_version not in ("v1", "v2"):
            raise ValueError(f"factores desconocidos en {self.celda_id}")
        self.driver = driver
        self.grafo = grafo
        self.index_paridad = Neo4jIndex(driver, grafo=grafo, modo="paridad")
        self.tools_v2 = ToolsV2(driver, grafo=grafo)          # su .index es fulltext
        self.index_fulltext = self.tools_v2.index
        self.index_busqueda = self.index_fulltext if self.retriever == "bm25" else self.index_paridad

    # --- misma interfaz que Neo4jIndex/GraphIndex (v1) ---
    def buscar_nodos(self, consulta: str, limite=LIMITE_DEFAULT) -> dict:
        return self.index_busqueda.buscar_nodos(consulta, limite)

    def ver_nodo(self, id: str) -> dict:
        return self.index_paridad.ver_nodo(id)      # byte-idéntico en ambos modos

    def ver_vecinos(self, id: str, direccion: str = "ambas") -> dict:
        if self.tools_version != "v1":
            raise RuntimeError(f"{self.celda_id}: ver_vecinos v1 llamada en una celda v2")
        return self.index_paridad.ver_vecinos(id, direccion)

    def ver_vecinos_v2(self, id: str, relacion=None, pagina=1, por_pagina=POR_PAGINA_DEFAULT) -> dict:
        if self.tools_version != "v2":
            raise RuntimeError(f"{self.celda_id}: ver_vecinos v2 llamada en una celda v1")
        return self.tools_v2.ver_vecinos_v2(id, relacion=relacion, pagina=pagina, por_pagina=por_pagina)

    # --- despacho por nombre de API con los defaults del harness / ToolsV2 ---
    def despachar(self, name: str, args: dict):
        args = args or {}
        if name == "buscar_nodos":
            return self.buscar_nodos(args.get("consulta", ""), args.get("limite", LIMITE_DEFAULT))
        if name == "ver_nodo":
            return self.ver_nodo(args.get("id", ""))
        if name == "ver_vecinos":
            if self.tools_version == "v1":
                return self.ver_vecinos(args.get("id", ""), args.get("direccion", "ambas"))
            return self.ver_vecinos_v2(args.get("id", ""), relacion=args.get("relacion"),
                                       pagina=args.get("pagina", 1),
                                       por_pagina=args.get("por_pagina", POR_PAGINA_DEFAULT))
        return {"error": f"tool desconocida: {name}"}

    def reejecutar_step(self, step: dict):
        """Firma compatible con `metrica._reejecutar_step(index, step)`
        (se inyecta como `lambda index, step: index.reejecutar_step(step)`)."""
        return self.despachar(step.get("tool"), step.get("input") or {})

    @property
    def descripcion(self) -> dict:
        return {"backend": "neo4j", "grafo": self.grafo, "kg_sha256": KG_REFINADO_SHA256,
                "retriever": self.retriever, "modo_busqueda": self.index_busqueda.modo,
                "indice_fulltext": self.index_fulltext.indice, "tools": self.tools_version}


def reejecutar_step_celda(index, step: dict):
    """Re-ejecutor v2-aware para inyectar en `metrica._reejecutar_step`:
    `index` debe ser un BackendCelda (v1 o v2). Para celdas v1 el pre-registro
    exige `metrica._reejecutar_step` original con un Neo4jIndex; este se usa
    solo en las celdas v2 (y en tests)."""
    return index.reejecutar_step(step)


class AgenteCelda(GraphAgentV2):
    """GraphAgentV2 (loop del harness verificado) con prompt/specs/backend de UNA celda."""

    def __init__(self, driver, celda: dict, client=None, cache_conversation: bool = True,
                 manifest_celda: dict | None = None):
        super().__init__(driver, grafo=GRAFO, client=client,
                         cache_conversation=cache_conversation, prompt="harness")
        self.celda = celda
        self.celda_id = celda["celda_id"]
        self.backend_celda = BackendCelda(driver, celda, grafo=GRAFO)
        self.index = self.backend_celda.index_busqueda   # por si algo consulta .index
        self.system_prompt = celda["system_prompt"]
        self.tools = celda["tools_specs"]
        self.full_outputs: list = []
        self._verificar(manifest_celda)

    def _verificar(self, manifest_celda: dict | None) -> None:
        if sha_texto(self.system_prompt) != self.celda["system_prompt_sha256"]:
            raise RuntimeError(f"{self.celda_id}: prompt cargado != sha de la celda")
        if sha_json(self.tools) != self.celda["tools_specs_sha256"]:
            raise RuntimeError(f"{self.celda_id}: specs cargadas != sha de la celda")
        if manifest_celda is not None:
            if (manifest_celda["system_prompt_sha256"] != self.celda["system_prompt_sha256"]
                    or manifest_celda["tools_specs_sha256"] != self.celda["tools_specs_sha256"]):
                raise RuntimeError(f"{self.celda_id}: sha de la celda != manifest sellado")
        if self.celda_id == "C00_booleano_v1":
            assert self.system_prompt == harness.SYSTEM_PROMPT, "C00: prompt != harness verbatim"
            assert self.tools == harness.TOOLS, "C00: specs != harness.TOOLS verbatim"
        if self.celda_id == "C11_bm25_v2":
            assert self.system_prompt == SYSTEM_PROMPT_V2_PROPUESTO, "C11: prompt != A1.2 verbatim"
            assert self.tools == TOOLS_V2, "C11: specs != TOOLS_V2 verbatim"
        v = verificar_ask_copiado()
        if not v["identico_salvo_sustituciones"]:
            raise RuntimeError("GraphAgentV2.ask ya no es la copia verificada del harness")

    def _run_tool(self, name: str, args: dict):
        t0 = time.monotonic()
        result = self.backend_celda.despachar(name, args or {})
        dt = time.monotonic() - t0
        s = json.dumps(result, ensure_ascii=False)
        self.full_outputs.append({"n": len(self.full_outputs) + 1, "tool": name,
                                  "input": args, "output": result, "output_chars": len(s),
                                  "latency_tool_s": round(dt, 4)})
        return result

    def ask_capturando(self, qid: str, question: str):
        self.full_outputs = []
        tr = self.ask(qid, question)
        return tr, list(self.full_outputs)

    @property
    def backend(self) -> dict:
        d = dict(self.backend_celda.descripcion)
        d.update({"celda_id": self.celda_id, "system_prompt_sha256": self.celda["system_prompt_sha256"],
                  "tools_specs_sha256": self.celda["tools_specs_sha256"],
                  "celda_archivo_sha256": self.celda.get("archivo_sha256"), "model": harness.MODEL})
        return d
