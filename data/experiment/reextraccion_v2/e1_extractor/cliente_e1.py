"""
cliente_e1.py — Cliente LLM inyectable para E1 (T2), patrón fase A/B de
sinteticas (cliente_faseB.py) + skill llm-capture.

FASE A (esta unidad): PROHIBICIÓN ABSOLUTA de llamadas a APIs de LLM. El
selftest usa SOLO StubClienteE1 (offline). ClienteE1Real existe como código
para la fase B pero exige construcción explícita con precios y tope
autorizados — no puede usarse "por accidente".

Cadena fase B:  ClienteE1Real ─▶ llm_cache.CachingClient ─▶ anthropic.Anthropic

Decisiones de dominio (checklist "dominio nuevo" de la skill llm-capture):
  - llm_cache se ENVUELVE, jamás se edita (cuarteto intocable).
  - .db PROPIA: cache/e1_extraccion.db bajo ESTE directorio (mandato: todo
    bajo e1_extractor/), misma capa SQLite del proyecto.
  - CODE_VER manual "e1-extractor-v1" + hash del prefijo estable en el
    namespace: cambiar el prompt o el tool schema invalida la caché aunque la
    key ya cubra el request íntegro (doble candado, precedente extract.py v2).
    BUMPEAR CODE_VER a mano si cambia la lógica sin cambiar el prompt.
  - Sin graph_fp: la extracción no consume ningún grafo en runtime — el chunk
    viaja íntegro en el prompt, la key del request captura toda variación.
  - thinking=False (no autorizado; el namespace lleva think=0).

Decisiones de caching de extracción (docs/decisiones_caching_extraccion.md):
  - D1: el request que construye prompt_e1.build_request_kwargs lleva el
    system como lista de bloques con cache_control ephemeral; este cliente lo
    pasa tal cual (jamás lo vuelve string).
  - D2: el gasto se computa con la fórmula de caching (input no cacheado ×
    P_in + cache write × P_cache_write + cache read × P_cache_read + output ×
    P_out) — nunca input+output a secas.
  - D3: todo response REAL de la API se loguea en logs/cache_usage.jsonl con
    component="reextraccion_v2_e1" y su doc (los hits de la caché local no se
    loguean: no son responses de la API).
  - D4: corridas con prefijo idéntico van SECUENCIALES (el runner de fase B
    debe respetarlo; este cliente es sincrónico, no abre concurrencia).
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import comun_e1
from comun_e1 import BASE, REPO
import prompt_e1

import llm_cache as lc  # data/experiment/evaluacion/llm_cache.py — solo import

CODE_VER = "e1-extractor-v1"
DOMAIN = "e1_extraccion"
DB_PATH = BASE / "cache" / "e1_extraccion.db"
CACHE_USAGE_LOG = REPO / "logs" / "cache_usage.jsonl"  # gitignoreado (logs/)


def namespace_e1(canal_abierto: bool = False) -> str:
    """Namespace de la caché local: dominio + code-version propio + hash del
    prefijo estable + flag de thinking. El hash del prefijo hace explícito el
    candado que la key del request ya da implícitamente. Con canal_abierto
    (experimental, explícito) el hash es el del prefijo con canal abierto:
    namespace DISTINTO → partición de caché; con el default False el
    namespace es IDÉNTICO al de producción."""
    return lc.make_namespace(
        DOMAIN,
        code_ver=f"{CODE_VER}-p{prompt_e1.prefijo_hash(canal_abierto)}",
        thinking=False,
    )


class TopeExcedido(RuntimeError):
    pass


class StubClienteE1:
    """Cliente offline para el selftest: devuelve tool inputs enlatados, jamás
    toca la red. Registra cada request recibido para que el selftest pueda
    asertar sobre el prefijo (identidad entre chunks, breakpoint declarado)."""

    class _Bloque:
        def __init__(self, tool_input):
            self.type = "tool_use"
            self.name = prompt_e1.NOMBRE_TOOL
            self.input = tool_input

    class _Usage:
        input_tokens = 0
        output_tokens = 0
        cache_creation_input_tokens = 0
        cache_read_input_tokens = 0

    class _Respuesta:
        def __init__(self, tool_input):
            self.content = [StubClienteE1._Bloque(tool_input)]
            self.stop_reason = "tool_use"
            self.usage = StubClienteE1._Usage()

    def __init__(self, tool_inputs: list):
        """tool_inputs: cola de inputs a devolver, en orden de llamada."""
        self._cola = list(tool_inputs)
        self.requests_recibidos: list[dict] = []
        self.messages = self  # imita client.messages.create

    def create(self, **kwargs):
        self.requests_recibidos.append(kwargs)
        if not self._cola:
            raise RuntimeError("StubClienteE1: cola de respuestas agotada")
        return StubClienteE1._Respuesta(self._cola.pop(0))


class ClienteE1Real:
    """Cliente real con caché never-pay-twice, contabilidad D2 y tope duro.
    SOLO fase B: exige precios y tope explícitos (autorización con precios
    resueltos); sin ellos no se construye."""

    def __init__(
        self,
        *,
        precio_in_por_mtok: float,
        precio_out_por_mtok: float,
        precio_cache_write_por_mtok: float,
        precio_cache_read_por_mtok: float,
        tope_usd: float,
        run_label: str,
        db_path: Path = DB_PATH,
        canal_abierto: bool = False,
    ):
        if min(precio_in_por_mtok, precio_out_por_mtok,
               precio_cache_write_por_mtok, precio_cache_read_por_mtok) <= 0 or tope_usd <= 0:
            raise ValueError("precios y tope deben ser positivos (autorización fase B)")
        import anthropic  # import local: la fase A jamás lo ejecuta
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.p_in = precio_in_por_mtok
        self.p_out = precio_out_por_mtok
        self.p_cw = precio_cache_write_por_mtok
        self.p_cr = precio_cache_read_por_mtok
        self.tope_usd = tope_usd
        self.cache = lc.CachingClient(
            anthropic.Anthropic(max_retries=3),
            domain=DOMAIN,
            db_path=db_path,
            namespace=namespace_e1(canal_abierto),
            thinking_enabled=False,
            run_label=run_label,
        )
        self.gasto_usd = 0.0  # solo misses (fórmula D2)
        self.llamadas = 0
        self.llamadas_hit = 0
        # Proyección conservadora de una llamada fría para el chequeo de tope:
        # prefijo completo como cache write + variable mediana + salida máxima.
        self._proyeccion_usd = (
            6500 / 1e6 * self.p_cw
            + 1000 / 1e6 * self.p_in
            + prompt_e1.MAX_OUTPUT_TOKENS / 1e6 * self.p_out
        )

    def _log_usage(self, usage, doc: str | None) -> None:
        # Decisión 3: una línea JSON por response REAL de la API.
        CACHE_USAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
        line = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "component": "reextraccion_v2_e1",
            "doc": doc,
            "input_tokens": getattr(usage, "input_tokens", None),
            "cache_creation_input_tokens": getattr(usage, "cache_creation_input_tokens", None),
            "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", None),
            "output_tokens": getattr(usage, "output_tokens", None),
        }
        with CACHE_USAGE_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")

    def create(self, *, doc: str | None = None, **kwargs):
        if self.gasto_usd + self._proyeccion_usd > self.tope_usd:
            raise TopeExcedido(
                f"gasto acumulado USD {self.gasto_usd:.4f} + proyección "
                f"{self._proyeccion_usd:.4f} supera el tope {self.tope_usd:.2f}")
        antes = dict(self.cache._stats)
        resp = self.cache.messages.create(**kwargs)
        despues = self.cache._stats
        fue_miss = despues["misses"] > antes["misses"]
        self.llamadas += 1
        if fue_miss:
            self._log_usage(resp.usage, doc)
            d_in = despues["tokens_in"] - antes["tokens_in"]
            d_out = despues["tokens_out"] - antes["tokens_out"]
            d_cw = despues["cache_write"] - antes["cache_write"]
            d_cr = despues["cache_read"] - antes["cache_read"]
            self.gasto_usd += (
                d_in * self.p_in + d_out * self.p_out
                + d_cw * self.p_cw + d_cr * self.p_cr
            ) / 1e6
        else:
            self.llamadas_hit += 1
        return resp

    def resumen(self) -> dict:
        return {
            "llamadas": self.llamadas,
            "hits_cache_local": self.llamadas_hit,
            "gasto_usd_real": round(self.gasto_usd, 4),
            "tope_usd": self.tope_usd,
            "precios_por_mtok": {"in": self.p_in, "out": self.p_out,
                                 "cache_write": self.p_cw, "cache_read": self.p_cr},
            "cache_stats": self.cache.stats(),
        }

    def close(self) -> None:
        self.cache.close()


def extraer_chunk(cliente, chunk: dict, model: str, canal_abierto: bool = False) -> dict:
    """Camino común stub/real: construye el request determinístico del chunk,
    llama al cliente inyectado y devuelve el tool input crudo (la validación
    es de validador_e1, separada). El cliente real recibe además doc= para el
    log de usage (Decisión 3). canal_abierto debe coincidir con el del cliente
    real (mismo prefijo → mismo namespace); se pasa explícito, jamás se infiere."""
    kwargs = prompt_e1.build_request_kwargs(chunk, model=model, canal_abierto=canal_abierto)
    if isinstance(cliente, ClienteE1Real):
        resp = cliente.create(doc=chunk["archivo"], **kwargs)
    else:
        resp = cliente.messages.create(**kwargs)

    tool_use = None
    for block in resp.content:
        if getattr(block, "type", None) == "tool_use":
            tool_use = block
            break
    return {
        "chunk_id": chunk["id"],
        "stop_reason": getattr(resp, "stop_reason", None),
        "tool_input": tool_use.input if tool_use is not None else None,
        "error": None if tool_use is not None else "no_tool_use",
    }
