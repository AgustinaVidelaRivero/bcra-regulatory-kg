"""
comun_esq3b_v2.py — Paths, constantes y cliente de la unidad U-ESQ-3b-v2
(VUELTA 2: corrida pareada de los retoques revisados).

Gobernado por:
  - data/experiment/esq/prerregistro_esq3b_v2.md (40493c9, FIRMADO 02/09/2026)
  - data/experiment/esq/prerregistro_esq3b.md    (01bf046 + Adenda 1 f1fe0d8)
  - tabla de resultados de la vuelta 1           (0c19dc8)

Diseño sellado que este módulo implementa sin re-decidir:
  - Brazos BASE (no se corren, USD 0): para las 15 unidades del objetivo, la
    extracción de la VUELTA 1 (esq3b/extracciones/pareado_esq3b.jsonl, prefijo
    f0a421fb9466, db esq_3b.db); para las 12 de regresión fresca, la
    extracción de ESQ-2 (cobertura/, sellos a7788c1, db esq_cobertura.db).
    Ambas fuentes son de SOLO LECTURA.
  - Brazo NUEVO: las 27 unidades con el prefijo v2
    (prompt_esq3b_v2.build_request_kwargs_v2).
  - Tope propio DURO de la vuelta: USD 0,40 (pre-registro v2 §6), cableado en
    el cliente (proyección pre-llamada) y re-chequeado por el runner.

Decisiones de caching (docs/decisiones_caching_extraccion.md), vinculantes:
  - D1: prefijo v2 estable con cache_control ephemeral (lo arma
    prompt_esq3b_v2; nada variable por chunk entra antes del breakpoint).
  - D2: todo costo con la fórmula de caching (costo_usd_desde_usage, heredada
    de comun_esq3b sin tocar).
  - D3: component propio "esq3b_v2_pareado_e1" en logs/cache_usage.jsonl.
  - D4: corrida SECUENCIAL (un cliente, un loop; el runner lo respeta).
  - D5: no aplica (esto es extracción, no evaluación).

Caché: db PROPIA NUEVA `esq/cache/esq_3b_v2.db` (gitignorada por
esq/.gitignore, patrón cache/), namespace propio por prefijo-hash NUEVO
(el hash del prefijo v2 particiona el namespace): esta vuelta no puede leer
ni pisar una sola key de producción, de ESQ-2 ni de la vuelta 1.

Tarifas y modelo: heredados verbatim de comun_esq3b (que los transcribe de
runner_corpus.py:76-78); el selftest v2 re-verifica la transcripción. El
modelo REALMENTE usado se resuelve por llamada desde el raw_json de la db
(patrón de las corridas previas de la saga).
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent          # data/experiment/esq/code
UNIDAD_DIR = CODE_DIR.parent                        # data/experiment/esq
EXP_DIR = UNIDAD_DIR.parent                         # data/experiment
REPO_DIR = EXP_DIR.parent.parent                    # raíz del repo

if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

# comun_esq3b agrega e1_extractor (y por él grafo_v2/code y evaluacion) al path
# y trae paths de la vuelta 1 + helpers de usage/costo que esta vuelta REUSA
# sin tocar.
import comun_esq3b as c1       # noqa: E402
import llm_cache as lc         # noqa: E402  — se ENVUELVE, jamás se edita
import prompt_esq3b_v2 as pr2  # noqa: E402  — prefijo v2 de la vuelta

# ----------------------- fuentes de la vuelta (solo lectura) ----------------- #
COBERTURA_DIR = c1.COBERTURA_DIR                    # ESQ-2 — SOLO LECTURA
ORDEN_DIR = c1.ORDEN_DIR                            # selecciones (se AGREGA un archivo)
ESQ3B_DIR = c1.ESQ3B_DIR                            # vuelta 1 — SOLO LECTURA
JSONL_V1 = c1.EXTRACCIONES_DIR / "pareado_esq3b.jsonl"
WORKSHEET_V1 = c1.FICHAS_DIR / "worksheet_pareado_esq3b.json"
SELECCION_V1 = c1.ORDEN_DIR / "seleccion_brazos_esq3b.json"
DB_V1 = c1.DB_ESQ3B                                 # esq_3b.db — SOLO LECTURA

# ----------------------- salidas propias de la vuelta ------------------------ #
ESQ3B_V2_DIR = UNIDAD_DIR / "esq3b_v2"
EXTRACCIONES_DIR = ESQ3B_V2_DIR / "extracciones"
FICHAS_DIR = ESQ3B_V2_DIR / "fichas"

CACHE_DIR = c1.CACHE_DIR                            # gitignorada (esq/.gitignore)
SELFTEST_DIR = c1.SELFTEST_DIR                      # gitignorada

DB_V2 = CACHE_DIR / "esq_3b_v2.db"                  # db PROPIA NUEVA de la vuelta
# dbs de la saga + producción + LA VUELTA 1: la propia no colisiona con ninguna.
DBS_AJENAS = tuple(c1.DBS_AJENAS) + (c1.DB_ESQ3B,)

TOS_ESQ2 = c1.TOS_ESQ2

# ----------------------- tarifas / modelo / tope ---------------------------- #
MODEL_E1 = c1.MODEL_E1
P_E1 = dict(c1.P_E1)

TOPE_USD = 0.40          # pre-registro v2 §6 — tope propio de la vuelta, duro

# ----------------------- namespace y candados ------------------------------- #
DOMAIN = "esq3b_v2_pareado_e1"
CODE_VER = "esq3b-v2-pareado-v1"

# Candados de base: el prefijo de PRODUCCIÓN sigue siendo el de ESQ-2 y el
# prefijo v1 sigue siendo el sellado en la Adenda 1 (f0a421fb9466). Si
# cualquiera cambió, el retoque v2 se estaría aplicando sobre otro texto.
PREFIJO_HASH_PRODUCCION_ESPERADO = c1.PREFIJO_HASH_PRODUCCION_ESPERADO
PREFIJO_HASH_V1_ESPERADO = "f0a421fb9466"


def namespace_v2() -> str:
    """Namespace propio de la vuelta: dominio propio + code-ver propio + hash
    del prefijo V2 (namespace por prefijo-hash). Distinto por construcción del
    de producción, del de ESQ-2 y del de la vuelta 1."""
    return lc.make_namespace(
        DOMAIN,
        code_ver=f"{CODE_VER}-p{pr2.PREFIJO_HASH_V2}",
        thinking=False,
    )


def namespace_v1() -> str:
    """Namespace de la vuelta 1 — SOLO para el gate de pareo y las guardas de
    no-colisión, en lectura."""
    return c1.namespace_esq3b()


def namespace_cobertura_esq2() -> str:
    return c1.namespace_cobertura_esq2()


def namespace_produccion() -> str:
    return c1.namespace_produccion()


# ----------------------- cargas (solo lectura) ------------------------------- #
cargar_chunks_esq2 = c1.cargar_chunks_esq2
cargar_extracciones_esq2 = c1.cargar_extracciones_esq2
cargar_jsonl_last_wins = c1.cargar_jsonl_last_wins
conectar_db_readonly = c1.conectar_db_readonly
tool_input_de_raw = c1.tool_input_de_raw
modelo_de_raw = c1.modelo_de_raw

# ----------------------- usage / costo (fórmula D2, heredada) ---------------- #
agregar_usage = c1.agregar_usage
costo_usd_desde_usage = c1.costo_usd_desde_usage

TopeExcedido = c1.TopeExcedido
chequear_tope = c1.chequear_tope

CACHE_USAGE_LOG = c1.CACHE_USAGE_LOG


class ClienteEsq3bV2:
    """Cliente real de la vuelta — patrón de comun_esq3b.ClienteEsq3b COPIADO
    (el módulo de la vuelta 1 no se toca) con: db propia NUEVA esq_3b_v2.db,
    namespace propio por prefijo-hash v2, component propio en el log D3 y tope
    duro USD 0,40. Contabilidad D2 sobre misses; los hits de la caché local no
    cuestan ni se loguean (no son responses de la API)."""

    COMPONENT = "esq3b_v2_pareado_e1"

    def __init__(self, *, precio_in_por_mtok: float, precio_out_por_mtok: float,
                 precio_cache_write_por_mtok: float, precio_cache_read_por_mtok: float,
                 tope_usd: float, run_label: str, db_path: Path = DB_V2):
        if min(precio_in_por_mtok, precio_out_por_mtok,
               precio_cache_write_por_mtok, precio_cache_read_por_mtok) <= 0 or tope_usd <= 0:
            raise ValueError("precios y tope deben ser positivos (autorización fase e)")
        import anthropic  # import local: nada offline lo ejecuta
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
            namespace=namespace_v2(),
            thinking_enabled=False,
            run_label=run_label,
        )
        self.gasto_usd = 0.0  # solo misses (fórmula D2)
        self.llamadas = 0
        self.llamadas_hit = 0
        # Proyección conservadora de una llamada fría: prefijo v2 completo como
        # cache write + variable mediana + salida máxima.
        self._proyeccion_usd = (
            8000 / 1e6 * self.p_cw
            + 1000 / 1e6 * self.p_in
            + pr2.MAX_OUTPUT_TOKENS / 1e6 * self.p_out
        )

    def _log_usage(self, usage, doc: str | None) -> None:
        # D3: una línea JSON por response REAL de la API, component propio.
        CACHE_USAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
        line = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "component": self.COMPONENT,
            "doc": doc,
            "input_tokens": getattr(usage, "input_tokens", None),
            "cache_creation_input_tokens": getattr(usage, "cache_creation_input_tokens", None),
            "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", None),
            "output_tokens": getattr(usage, "output_tokens", None),
        }
        with CACHE_USAGE_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")

    def create(self, *, doc: str | None = None, **kwargs):
        chequear_tope(self.gasto_usd, self._proyeccion_usd, self.tope_usd)
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
