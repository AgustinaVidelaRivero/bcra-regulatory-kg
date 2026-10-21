#!/usr/bin/env python3
"""servidor_mcp_vector.py — Servidor MCP (stdio) del brazo de fragmentos del banco
(U-A2.0-banco, pieza ii; A2.1, tramo 1). Tool ÚNICA:

    buscar_pasajes(consulta, limite) -> {consulta, total_pasajes, resultados: [
        {rank, id, to, unidad, archivo, titulo, tipo, paginas, score, texto}]}

sobre los pasajes de E0 (propio + herencia) del índice que declara la config.
Cada pasaje devuelto cita el TO (`to`, `archivo`) y el punto (`unidad`).

Dos medidas de afinidad, por la clave `afinidad` de la config (A2.1: el
sistema por fragmentos es uno solo, con dos configuraciones que difieren solo
en la medida de afinidad):

  · `denso` (default; la de U-A2.0-banco): embeddings de
    `microsoft/harrier-oss-v1-0.6b` construidos por `construir_indice.py`
    (laudo A2.0b). Reglas selladas (docs/decision_modelo_embeddings.md §7-§8):
    la consulta se codifica CON el prompt preconfigurado `web_search_query`
    del propio repo del modelo; los documentos se codificaron SIN prompt
    (asimetría de los autores; test de asimetría en test_mcp_vector.py);
    similitud coseno (embeddings L2-normalizados por el módulo 2_Normalize
    del modelo ⇒ producto interno), `float32`, `max_seq_length` del manifiesto;
  · `bm25`: BM25 con el analizador `spanish` de Lucene (bm25_fragmentos.py),
    sobre los mismos pasajes. En este modo el proceso no importa numpy,
    torch, sentence-transformers ni el driver del grafo, y no carga el modelo.

En las dos, ranking determinístico con el desempate del bake-off
(e3_medicion.py): score desc, luego id asc. `limite` se acota a
[1, limite_max] con la misma expresión que `GraphIndex._limite` (default 10 si
no es entero, acotado también por limite_max). `limite_max` sale de la config:
50 si no lo declara (U-A2.0-banco); 5 en las configuraciones de A2.1 (D-D,
top-k = 5).

Al arrancar verifica los sha del índice contra su manifiesto y contra la
config (en modo denso, además, el manifiesto contra el sha_docs del bake-off
cuando el índice es el de la E0 vieja; en modo BM25, re-deriva el índice desde
los pasajes con el analizador del proceso y exige el mismo sha): si difieren,
no expone nada.

R1: log íntegro por llamada (comun_banco.LogR1), mismo formato que mcp_kg.
Serialización de la respuesta: `json.dumps(obj, ensure_ascii=False)` — la misma
del harness y del otro brazo, para que el adaptador trate ambos igual.

Uso:
    python3 -B servidor_mcp_vector.py --config config_mcp_vector.json
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
import unicodedata
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
if str(BANCO_DIR) not in sys.path:
    sys.path.insert(0, str(BANCO_DIR))
from comun_banco import (LogR1, cargar_config, rel_repo, serializar_payload,  # noqa: E402
                         sha256_bytes, sha256_file, versiones_entorno)

VERSION_SERVIDOR = "1.0"
NOMBRE_SERVIDOR = "mcp_vector"
CONFIG_DEFAULT = AQUI / "config_mcp_vector.json"
LIMITE_MAX_DEFAULT = 50
# Tope en caracteres del resultado de cada tool en Claude Code (D-6). Sin
# `_meta["anthropic/maxResultSizeChars"]`, el CLI sellado (2.1.241) guarda en
# disco todo resultado de más de 50.000 caracteres; con la anotación, el umbral
# es el valor anotado (hasta 500.000) y el CLI no le aplica a la tool el tope en
# tokens (MAX_MCP_OUTPUT_TOKENS). Mismo valor en todas las tools de los dos
# servidores del banco.
TOPE_CARACTERES_RESULTADO = 200000

TOOL_BUSCAR_PASAJES = {
    "name": "buscar_pasajes",
    "description": ("Búsqueda semántica (embeddings) de pasajes del texto de las normas. "
                    "Devuelve los pasajes más similares a la consulta, cada uno con su "
                    "TO (norma), punto (unidad) y el texto completo del pasaje. Es el "
                    "punto de entrada habitual."),
    "input_schema": {
        "type": "object",
        "properties": {
            "consulta": {"type": "string", "description": "Consulta en lenguaje natural."},
            "limite": {"type": "integer", "description": "Máximo de resultados (def. 10)."},
        },
        "required": ["consulta"],
    },
}
# Lo único que cambia en la definición de la tool según la config (A2.1): el
# nombre de la medida de afinidad y, con limite_max < 10, el default y el tope.
DESCRIPCION_BM25 = ("Búsqueda léxica (BM25) de pasajes del texto de las normas. "
                    "Devuelve los pasajes más similares a la consulta, cada uno con su "
                    "TO (norma), punto (unidad) y el texto completo del pasaje. Es el "
                    "punto de entrada habitual.")


def definicion_tool(afinidad: str = "denso", limite_max: int = LIMITE_MAX_DEFAULT) -> dict:
    """La de U-A2.0-banco tal cual con (denso, 50); para A2.1, la misma con el nombre de la
    medida de afinidad y el tope de `limite` a la vista."""
    t = json.loads(json.dumps(TOOL_BUSCAR_PASAJES))
    if afinidad == "bm25":
        t["description"] = DESCRIPCION_BM25
    if limite_max < 10:
        t["input_schema"]["properties"]["limite"]["description"] = (
            f"Máximo de resultados (def. {limite_max}, máx. {limite_max}).")
    return t


def _limite(limite, limite_max: int = LIMITE_MAX_DEFAULT) -> int:
    # Misma expresión que GraphIndex.buscar_nodos / Neo4jIndex._limite, con el tope de la config.
    try:
        return max(1, min(int(limite), limite_max))
    except (TypeError, ValueError):
        return min(10, limite_max)


def _fila(r: int, p: dict, s: float) -> dict:
    return {"rank": r, "id": p["id"], "to": p["to"], "unidad": p["unidad"],
            "archivo": p["archivo"], "titulo": p["titulo"], "tipo": p["tipo"],
            "paginas": p["paginas"], "score": round(s, 6), "texto": p["texto"]}


class IndiceVectorial:
    def __init__(self, config: dict):
        import numpy as np
        self.dir = (AQUI / config["indice_dir"]).resolve()
        self.man = json.loads((self.dir / "manifiesto_indice.json").read_text(encoding="utf-8"))
        self.E = np.load(self.dir / "embeddings_docs.npy")
        self.pasajes = json.loads((self.dir / "pasajes.json").read_text(encoding="utf-8"))
        self.ids = [p["id"] for p in self.pasajes]
        self.limite_max = int(config.get("limite_max", LIMITE_MAX_DEFAULT))
        # sellos
        import hashlib
        sha_m = hashlib.sha256(self.E.astype("float32").tobytes(order="C")).hexdigest()
        if sha_m != self.man["matriz"]["sha256_matriz"]:
            raise SystemExit(f"ABORTO: sha de la matriz {sha_m} != manifiesto {self.man['matriz']['sha256_matriz']}")
        if sha_m != config["sha256_matriz_esperado"]:
            raise SystemExit(f"ABORTO: sha de la matriz {sha_m} != esperado por config {config['sha256_matriz_esperado']}")
        if self.E.shape[0] != len(self.pasajes):
            raise SystemExit("ABORTO: matriz y pasajes no coinciden en cantidad")
        self.sha_matriz = sha_m
        mcfg = self.man["modelo"]
        self.prompt_name = mcfg["prompt_consultas"]
        self.prompt_texto = mcfg["prompt_consultas_texto"]   # sellado en el manifiesto; se re-verifica al cargar
        self._device = config.get("device", "mps")
        self._m = None
        if config.get("carga_modelo", "perezosa") == "inmediata":
            self._cargar_modelo()

    def _cargar_modelo(self):
        """Carga PEREZOSA (decisión medida): el modelo tarda ~70 s en cargar y
        Claude Code 2.1.196 no espera a un servidor `pending` antes del primer
        turno (la espera está documentada a partir de v2.1.221). Con la carga en
        la primera llamada, `initialize` y `tools/list` responden al instante y
        el servidor figura `connected` con su tool desde el `system/init`. La
        primera `buscar_pasajes` paga la carga; el `timeout` por servidor del
        JSON de MCP cubre esa latencia."""
        if self._m is not None:
            return self._m
        mcfg = self.man["modelo"]
        import torch
        from sentence_transformers import SentenceTransformer
        m = SentenceTransformer(mcfg["repo"], revision=mcfg["revision"], device=self._device,
                                trust_remote_code=False, model_kwargs={"dtype": torch.float32})
        m.max_seq_length = mcfg["max_seq_length"]
        if self.prompt_name not in (m.prompts or {}) or m.prompts[self.prompt_name] != self.prompt_texto:
            raise SystemExit(f"ABORTO: el prompt {self.prompt_name!r} del modelo no coincide con el manifiesto")
        self._m = m
        return m

    @property
    def m(self):
        return self._cargar_modelo()

    def embed_consulta(self, consulta: str, con_prompt: bool = True):
        kw = {"prompt_name": self.prompt_name} if con_prompt else {}
        return self.m.encode([consulta], batch_size=1, convert_to_numpy=True,
                             normalize_embeddings=True, show_progress_bar=False, **kw)[0].astype("float32")

    def buscar_pasajes(self, consulta: str, limite: int = 10) -> dict:
        import numpy as np
        limite = _limite(limite, self.limite_max)
        if not isinstance(consulta, str) or not consulta.strip():
            return {"consulta": consulta, "total_pasajes": len(self.ids), "resultados": []}
        q = self.embed_consulta(consulta, con_prompt=True)
        S = self.E @ q
        idx = np.argsort(-S, kind="stable")[:limite * 3]
        top = sorted(((int(i), float(S[i])) for i in idx), key=lambda kv: (-kv[1], self.ids[kv[0]]))[:limite]
        res = [_fila(r, self.pasajes[i], s) for r, (i, s) in enumerate(top, 1)]
        return {"consulta": consulta, "total_pasajes": len(self.ids), "resultados": res}


class IndiceBM25:
    """Modo BM25 (A2.1): sin numpy, sin modelo. El índice persistido se verifica
    por sha contra el manifiesto y la config, y se re-deriva desde los pasajes
    con el analizador de este proceso: si el analizador cambió, aborta."""

    def __init__(self, config: dict):
        import bm25_fragmentos as BM
        self.BM = BM
        self.dir = (AQUI / config["indice_dir"]).resolve()
        self.man = json.loads((self.dir / "manifiesto_indice.json").read_text(encoding="utf-8"))
        sha_p = sha256_file(self.dir / "pasajes.json")
        if sha_p != self.man["corpus"]["sha256_pasajes_json"]:
            raise SystemExit(f"ABORTO: sha de pasajes.json {sha_p} != manifiesto {self.man['corpus']['sha256_pasajes_json']}")
        self.pasajes = json.loads((self.dir / "pasajes.json").read_text(encoding="utf-8"))
        self.ids = [p["id"] for p in self.pasajes]
        crudo = (self.dir / "indice_bm25.json").read_bytes()
        sha_i = sha256_bytes(crudo)
        if sha_i != self.man["bm25"]["sha256_indice"]:
            raise SystemExit(f"ABORTO: sha del índice BM25 {sha_i} != manifiesto {self.man['bm25']['sha256_indice']}")
        if sha_i != config["sha256_indice_esperado"]:
            raise SystemExit(f"ABORTO: sha del índice BM25 {sha_i} != esperado por config {config['sha256_indice_esperado']}")
        indice = json.loads(crudo.decode("utf-8"))
        if BM.sha256_indice(BM.construir(self.pasajes)) != sha_i or indice["ids"] != self.ids:
            raise SystemExit("ABORTO: el analizador de este proceso no reproduce el índice BM25 persistido")
        self.sha_indice = sha_i
        self.limite_max = int(config.get("limite_max", LIMITE_MAX_DEFAULT))
        self.buscador = BM.Buscador(indice)

    def buscar_pasajes(self, consulta: str, limite: int = 10) -> dict:
        limite = _limite(limite, self.limite_max)
        if not isinstance(consulta, str) or not consulta.strip():
            return {"consulta": consulta, "total_pasajes": len(self.ids), "resultados": []}
        top = self.buscador.buscar(consulta, limite)
        res = [_fila(r, self.pasajes[i], s) for r, (i, s) in enumerate(top, 1)]
        return {"consulta": consulta, "total_pasajes": len(self.ids), "resultados": res}


def construir_indice_de(config: dict):
    afinidad = config.get("afinidad", "denso")
    if afinidad == "denso":
        return IndiceVectorial(config)
    if afinidad == "bm25":
        return IndiceBM25(config)
    raise SystemExit(f"ABORTO: afinidad desconocida en la config: {afinidad!r}")


def construir_servidor(config_path: Path):
    import mcp.types as types
    from mcp.server.lowlevel import Server

    config, config_sha = cargar_config(config_path)
    afinidad = config.get("afinidad", "denso")
    idx = construir_indice_de(config)
    if afinidad == "denso":
        fuente = {"backend": "vectorial_local", "indice_dir": rel_repo(idx.dir),
                  "sha256_matriz": idx.sha_matriz,
                  "sha256_manifiesto": sha256_file(idx.dir / "manifiesto_indice.json"),
                  "sha256_pasajes_json": sha256_file(idx.dir / "pasajes.json"),
                  "n_pasajes": len(idx.ids), "modelo": idx.man["modelo"],
                  "sha_docs_bakeoff": idx.man["matriz"].get("sha_docs_bakeoff"),
                  "coincide_con_bakeoff": idx.man["matriz"].get("coincide_con_bakeoff"),
                  "prompt_consultas_texto": idx.prompt_texto}
        libs = ["mcp", "torch", "transformers", "sentence-transformers", "tokenizers", "numpy"]
    else:
        fuente = {"backend": "bm25_local", "afinidad": "bm25", "indice_dir": rel_repo(idx.dir),
                  "sha256_indice_bm25": idx.sha_indice,
                  "sha256_manifiesto": sha256_file(idx.dir / "manifiesto_indice.json"),
                  "sha256_pasajes_json": sha256_file(idx.dir / "pasajes.json"),
                  "n_pasajes": len(idx.ids), "analizador": idx.BM.ANALIZADOR,
                  "lucene_version": idx.BM.LUCENE_VERSION, "sha256_stop": idx.BM.SHA256_STOP,
                  "unicodedata": unicodedata.unidata_version,
                  "k1": idx.BM.K1, "b": idx.BM.B,
                  "sha256_modulo_bm25": sha256_file(AQUI / "bm25_fragmentos.py")}
        libs = ["mcp"]
    if "manifiesto_e0" in idx.man:
        fuente["manifiesto_e0"] = idx.man["manifiesto_e0"]
    fuente["limite_max"] = idx.limite_max
    log = LogR1(NOMBRE_SERVIDOR, VERSION_SERVIDOR, config, config_sha, fuente,
                versiones_entorno(libs) | {"config_path": rel_repo(config_path)})
    server = Server(NOMBRE_SERVIDOR, version=VERSION_SERVIDOR)
    tool = definicion_tool(afinidad, idx.limite_max)

    @server.list_tools()
    async def _list_tools() -> list[types.Tool]:
        return [types.Tool(name=tool["name"], description=tool["description"], inputSchema=tool["input_schema"],
                           _meta={"anthropic/maxResultSizeChars": TOPE_CARACTERES_RESULTADO})]

    @server.call_tool(validate_input=False)
    async def _call_tool(name: str, arguments: dict):
        t0 = time.perf_counter()
        n, call_id = log.nuevo_call_id()
        try:
            rpc_id = server.request_context.request_id
        except LookupError:
            rpc_id = None
        args = arguments or {}
        try:
            if name == "buscar_pasajes":
                obj = idx.buscar_pasajes(args.get("consulta", ""), args.get("limite", 10))
            else:
                obj = {"error": f"tool desconocida: {name}"}
            out = serializar_payload(obj)
        except Exception as e:
            log.llamada(n, call_id, rpc_id, name, args, None, t0, error=f"{type(e).__name__}: {e}")
            raise
        log.llamada(n, call_id, rpc_id, name, args, out, t0)
        return [types.TextContent(type="text", text=out)]

    return server, log, idx


def _fin_ante_senal(log):
    """C2 (laudo fase B): Claude Code termina el proceso del servidor al cerrar la
    sesión (SIGTERM tras cerrar stdin). Sin esto el `finally` no corre y el log
    R1 queda sin línea `fin` (medido en la corrida 1: 6/6 sesiones del vectorial)."""
    import os
    import signal

    def _handler(signum, frame):
        try:
            log.fin()
        finally:
            os._exit(0)
    signal.signal(signal.SIGTERM, _handler)
    signal.signal(signal.SIGINT, _handler)


async def servir(config_path: Path) -> None:
    from mcp.server.stdio import stdio_server
    server, log, _ = construir_servidor(config_path)
    _fin_ante_senal(log)
    try:
        async with stdio_server() as (r, w):
            await server.run(r, w, server.create_initialization_options())
    finally:
        if not log.cerrado:
            log.fin()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, default=CONFIG_DEFAULT)
    a = ap.parse_args()
    asyncio.run(servir(a.config.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
