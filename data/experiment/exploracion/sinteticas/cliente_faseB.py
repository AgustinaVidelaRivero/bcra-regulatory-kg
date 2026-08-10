"""
cliente_faseB.py — Implementación REAL de generador.ClienteLLM para la fase B,
envuelta en la caché del proyecto (llm_cache.CachingClient, never-pay-twice).

Patrón de la skill llm-capture: el script nace envuelto en la caché; el
cuarteto (loader/harness/judge/llm_cache) se importa, jamás se edita.

Cadena:  ClienteFaseB ─▶ CachingClient ─▶ anthropic.Anthropic(max_retries=3)

Decisiones de dominio (checklist "dominio nuevo" de la skill):
  - .db PROPIA: cache/sinteticas_faseB.db bajo ESTE directorio (el mandato de
    la unidad exige todo lo persistido bajo sinteticas/; misma capa SQLite).
  - CODE_VER manual "sinteticas-faseB-v1": el comportamiento del dominio lo
    definen generador.py + runner_faseB.py, no los fuentes hasheados del
    pipeline principal. BUMPEAR A MANO si cambian prompts o lógica (con
    CODE_VER manual, editar estos scripts NO invalida la caché sola).
  - Sin graph_fp: como el juez, estas llamadas no consumen el grafo en
    runtime — el contenido del sample viaja ÍNTEGRO en el prompt, así que la
    key del request ya captura toda variación de grafo/semilla.
  - thinking=False (no autorizado; el namespace lleva think=0).

Modelo y tope (autorización de fase B):
  - claude-sonnet-5, temperature 0, max_tokens 1024.
  - Precio autorizado: USD 2 / MTok entrada, USD 10 / MTok salida.
  - TOPE DURO: USD 4,00 sobre tokens REALES (solo misses; los hits de caché
    no pagan). Si el gasto acumulado + el costo proyectado de la próxima
    llamada supera el tope, se aborta con TopeExcedido ANTES de llamar.
"""

from __future__ import annotations

import sys
from pathlib import Path

from comun import EVAL_DIR
from generador import ClienteLLM

sys.path.insert(0, str(EVAL_DIR))
import llm_cache as lc  # noqa: E402

MODELO = "claude-sonnet-5"
# Peculiaridades de claude-sonnet-5 verificadas en las primeras llamadas
# reales de esta unidad (+ referencia claude-api skill):
#   - RECHAZA `temperature` (400 "deprecated for this model"): no se pasa.
#   - Thinking ADAPTATIVO ACTIVO POR DEFECTO si se omite `thinking`, y
#     max_tokens limita thinking + respuesta JUNTOS: una llamada gastó ~960
#     tokens de salida en un bloque thinking y cortó el JSON por max_tokens.
#     Para este dominio (preguntas cortas y veredictos JSON, sin tools) se
#     DESHABILITA explícitamente: {"type": "disabled"} es aceptado en Sonnet 5
#     y mantiene el gasto alineado con la estimación sellada.
THINKING = {"type": "disabled"}
MAX_TOKENS = 1536

PRECIO_IN_POR_MTOK = 2.0     # USD, autorización fase B (vigente al 2026-08)
PRECIO_OUT_POR_MTOK = 10.0
TOPE_USD = 4.00
# Proyección conservadora de la próxima llamada para el chequeo de tope:
# el prompt más grande medido (~1.2k tok) + salida máxima (1024 tok).
PROYECCION_LLAMADA_USD = (1500 * PRECIO_IN_POR_MTOK
                          + MAX_TOKENS * PRECIO_OUT_POR_MTOK) / 1e6

CODE_VER = "sinteticas-faseB-v1"
DOMAIN = "sinteticas"
RUN_LABEL = "sinteticas_faseB"
DB_PATH = Path(__file__).resolve().parent / "cache" / "sinteticas_faseB.db"


class TopeExcedido(RuntimeError):
    pass


class ClienteFaseB(ClienteLLM):
    """Cliente real con caché, contabilidad de gasto y tope duro."""

    def __init__(self, db_path: Path = DB_PATH, run_label: str = RUN_LABEL):
        import anthropic
        db_path.parent.mkdir(parents=True, exist_ok=True)
        real = anthropic.Anthropic(max_retries=3)
        self.cache = lc.CachingClient(
            real,
            domain=DOMAIN,
            db_path=db_path,
            namespace=lc.make_namespace(DOMAIN, code_ver=CODE_VER,
                                        thinking=False),
            thinking_enabled=False,
            run_label=run_label,
        )
        self.gasto_usd = 0.0          # solo misses (tokens realmente pagados)
        self.llamadas = 0
        self.llamadas_hit = 0

    def generar(self, prompt: str) -> str:
        if self.gasto_usd + PROYECCION_LLAMADA_USD > TOPE_USD:
            raise TopeExcedido(
                f"gasto acumulado USD {self.gasto_usd:.4f} + proyección "
                f"{PROYECCION_LLAMADA_USD:.4f} supera el tope {TOPE_USD:.2f}")
        antes = dict(self.cache._stats)
        resp = self.cache.messages.create(
            model=MODELO,
            max_tokens=MAX_TOKENS,
            thinking=THINKING,
            messages=[{"role": "user", "content": prompt}],
        )
        despues = self.cache._stats
        fue_miss = despues["misses"] > antes["misses"]
        self.llamadas += 1
        if fue_miss:
            din = despues["tokens_in"] - antes["tokens_in"]
            dout = despues["tokens_out"] - antes["tokens_out"]
            self.gasto_usd += (din * PRECIO_IN_POR_MTOK
                               + dout * PRECIO_OUT_POR_MTOK) / 1e6
        else:
            self.llamadas_hit += 1
        return "".join(b.text for b in resp.content
                       if getattr(b, "type", "") == "text")

    def resumen(self) -> dict:
        s = self.cache.stats()
        return {
            "modelo": MODELO,
            "llamadas": self.llamadas,
            "hits_cache": self.llamadas_hit,
            "gasto_usd_real": round(self.gasto_usd, 4),
            "tope_usd": TOPE_USD,
            "precio_por_mtok": {"in": PRECIO_IN_POR_MTOK,
                                "out": PRECIO_OUT_POR_MTOK},
            "cache_stats": s,
        }

    def close(self):
        self.cache.close()
