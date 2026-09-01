"""
comun_cobertura_esq2.py — Paths, constantes y cliente de la unidad U-ESQ-2
(test de cobertura del esquema, protocolizado). Gobernado por:
  - docs/laudo_ESQ-2_diseno.md (commit 8dea823, FIRMADO 01/09/2026)
  - data/experiment/esq/prerregistro_esq2.md (commit 2240c9c, FIRMADO 01/09/2026)

Diseño sellado que este módulo implementa sin re-decidir:
  - Universo: los 10 TOs del sorteo sellado de D4 para ESQ-1 (semilla 20260827;
    pre-registro §1) — 762 unidades. Chunks E0 ya calculados en
    escalado_prep/e0_dry/<to>/chunks_<to>.json (SOLO LECTURA).
  - Extracción E1-solo, modo cerrado, flag apagado (canal_abierto=False en todo
    call site), SIN el atajo del rol de alcance (cuarentena D5 heredada: los 10
    archivos no están en ROL_POR_TO — el selftest lo verifica sobre los 762
    mensajes, no lo asume).
  - Caché y namespace PROPIOS (pre-registro §1): db esq/cache/esq_cobertura.db
    (gitignorada) + namespace esq2_cobertura_e1 con el hash del prefijo cerrado
    como candado. El request a la API es byte-idéntico al de producción flag-off
    (build_request_kwargs sin tocar); el namespace propio solo particiona la
    caché local — jamás pisa keys de producción.
  - Tope duro de la unidad: USD 6,50 (laudo §1.i), cableado en el cliente
    (proyección pre-llamada) y re-chequeado por el runner.

Decisiones de caching (docs/decisiones_caching_extraccion.md), heredadas:
  - D1: prefijo estable con cache_control ephemeral — build_request_kwargs
    de producción, sin modificación.
  - D2: todo costo con la fórmula de caching (costo_usd_desde_usage).
  - D3: component propio "esq2_cobertura_e1" en logs/cache_usage.jsonl.
  - D4: corrida SECUENCIAL (un cliente, un loop; el runner lo respeta).

Tarifas y modelo: verbatim de
data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py:76-78
(claude-haiku-4-5 — 1,00 / 5,00 / 1,25 / 0,10 USD/MTok); el selftest verifica
la transcripción contra ese archivo sin importarlo.
"""

from __future__ import annotations

import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent          # data/experiment/esq/code
UNIDAD_DIR = CODE_DIR.parent                        # data/experiment/esq
EXP_DIR = UNIDAD_DIR.parent                         # data/experiment
REPO_DIR = EXP_DIR.parent.parent                    # raíz del repo

COBERTURA_DIR = UNIDAD_DIR / "cobertura"            # salidas de la unidad
ORDEN_DIR = COBERTURA_DIR / "orden"                 # selección de muestra + semillas
CACHE_DIR = UNIDAD_DIR / "cache"                    # gitignorada (esq/.gitignore)
SELFTEST_DIR = UNIDAD_DIR / "selftest_out"          # gitignorada

DB_COBERTURA = CACHE_DIR / "esq_cobertura.db"       # db PROPIA de la unidad
# dbs previas de la saga ESQ + db de producción: la propia no colisiona con
# ninguna (guarda del selftest).
DBS_AJENAS = (
    CACHE_DIR / "esq_control.db",
    CACHE_DIR / "esq_control_p1bis.db",
    CACHE_DIR / "esq_control_p1ter.db",
    CACHE_DIR / "esq_descubrimiento_cal.db",
    EXP_DIR / "reextraccion_v2" / "e1_extractor" / "cache" / "e1_extraccion.db",
    EXP_DIR / "reextraccion_v2" / "e3_verificador" / "cache" / "e1_reintentos.db",
)

E1_DIR = EXP_DIR / "reextraccion_v2" / "e1_extractor"
if str(E1_DIR) not in sys.path:
    sys.path.insert(0, str(E1_DIR))

import comun_e1        # noqa: E402  (agrega grafo_v2/code y evaluacion al path)
import prompt_e1       # noqa: E402
import llm_cache as lc  # noqa: E402  — se ENVUELVE, jamás se edita

# ----------------------- universo sellado (pre-registro §1) ----------------- #
# Los 10 TOs del sorteo sellado D4/ESQ-1 (laudo ESQ-2 §1.iii), en el orden del
# pre-registro §1; también es el orden de corrida (secuencial por TO).
TOS_ESQ2 = ("ayccef", "expaef", "opefci", "adrei", "cryl",
            "actgar", "prevmi", "lavdin", "traval", "ctacor")
N_UNIDADES_ESQ2 = 762   # pre-registro §1; el selftest lo recomputa

ESCALADO_E0 = EXP_DIR / "escalado_prep" / "e0_dry"
ESCALADO_PDFS = EXP_DIR / "escalado_prep" / "pdfs"

# ----------------------- tarifas / modelo / tope ---------------------------- #
# Verbatim runner_corpus.py:76-78 (corrida sellada del corpus).
MODEL_E1 = "claude-haiku-4-5"
P_E1 = dict(precio_in_por_mtok=1.00, precio_out_por_mtok=5.00,
            precio_cache_write_por_mtok=1.25, precio_cache_read_por_mtok=0.10)

TOPE_USD = 6.50          # laudo ESQ-2 §1.i — tope propio de la unidad, duro
SEMILLA_MUESTRA = 20260901   # pre-registro §3 — sorteo de la muestra azarosa

# ----------------------- namespace y candados ------------------------------- #
DOMAIN = "esq2_cobertura_e1"
CODE_VER = "esq2-cobertura-v1"

# Candado del prefijo cerrado de producción: el hash del prefijo flag-off
# vigente al sellar esta unidad. Si prompt_e1 cambia, prefijo_hash(False)
# cambia y el selftest FRENA (el camino flag-off dejó de ser el de producción).
PREFIJO_HASH_CERRADO_ESPERADO = "4793d6152608"


def namespace_cobertura() -> str:
    """Namespace propio de la unidad: dominio propio + code-ver propio + hash
    del prefijo CERRADO (doble candado, precedente cliente_e1.namespace_e1).
    Distinto por construcción del de producción (dominio e1_extraccion) y de
    los de la saga ESQ."""
    return lc.make_namespace(
        DOMAIN,
        code_ver=f"{CODE_VER}-p{prompt_e1.prefijo_hash(False)}",
        thinking=False,
    )


def namespace_produccion() -> str:
    """Namespace de la caché de producción flag-off (cliente_e1.namespace_e1
    con default False) — SOLO para el gate de paridad, en lectura."""
    import cliente_e1
    return cliente_e1.namespace_e1(canal_abierto=False)


# ----------------------- carga de chunks (solo lectura) --------------------- #
def cargar_chunks_esq2(tos: tuple[str, ...] = TOS_ESQ2) -> list[dict]:
    """Chunks E0 de escalado_prep en orden estable (por TO en el orden sellado,
    dentro de cada TO en el orden del archivo). Solo lectura."""
    chunks: list[dict] = []
    for to in tos:
        path = ESCALADO_E0 / to / f"chunks_{to}.json"
        with path.open(encoding="utf-8") as f:
            chunks.extend(json.load(f))
    return chunks


# ----------------------- usage / costo (fórmula D2) ------------------------- #
def agregar_usage(usages: list[dict]) -> dict:
    agg = {"n": 0, "input_tokens": 0, "output_tokens": 0,
           "cache_write_tokens": 0, "cache_read_tokens": 0, "n_escrituras": 0}
    for u in usages:
        if not u:
            continue
        agg["n"] += 1
        for k in ("input_tokens", "output_tokens",
                  "cache_write_tokens", "cache_read_tokens"):
            agg[k] += u.get(k, 0) or 0
        if (u.get("cache_write_tokens") or 0) > 0:
            agg["n_escrituras"] += 1
    return agg


def costo_usd_desde_usage(agg: dict, p: dict = P_E1) -> float:
    """Fórmula D2 (docs/decisiones_caching_extraccion.md:32-42):
    in×P_in + out×P_out + cw×P_cw + cr×P_cr, tokens en MTok."""
    return (agg.get("input_tokens", 0) * p["precio_in_por_mtok"]
            + agg.get("output_tokens", 0) * p["precio_out_por_mtok"]
            + agg.get("cache_write_tokens", 0) * p["precio_cache_write_por_mtok"]
            + agg.get("cache_read_tokens", 0) * p["precio_cache_read_por_mtok"]) / 1e6


# ----------------------- cliente propio (patrón cliente_e1) ----------------- #
class TopeExcedido(RuntimeError):
    pass


CACHE_USAGE_LOG = REPO_DIR / "logs" / "cache_usage.jsonl"   # gitignoreado (logs/)


def chequear_tope(gasto_usd: float, proyeccion_usd: float, tope_usd: float) -> None:
    """Freno duro pre-llamada (mismo criterio que cliente_e1.ClienteE1Real:
    gasto acumulado + proyección conservadora de UNA llamada fría > tope ⇒
    TopeExcedido, la llamada no sale)."""
    if gasto_usd + proyeccion_usd > tope_usd:
        raise TopeExcedido(
            f"gasto acumulado USD {gasto_usd:.4f} + proyección "
            f"{proyeccion_usd:.4f} supera el tope {tope_usd:.2f}")


class ClienteCoberturaEsq2:
    """Cliente real de la unidad — patrón de cliente_e1.ClienteE1Real COPIADO
    (el módulo de producción no se toca) con: db propia, namespace propio,
    component propio en el log D3, tope duro USD 6,50. Contabilidad D2 sobre
    misses; los hits de la caché local no cuestan ni se loguean (no son
    responses de la API)."""

    COMPONENT = "esq2_cobertura_e1"

    def __init__(self, *, precio_in_por_mtok: float, precio_out_por_mtok: float,
                 precio_cache_write_por_mtok: float, precio_cache_read_por_mtok: float,
                 tope_usd: float, run_label: str, db_path: Path = DB_COBERTURA):
        if min(precio_in_por_mtok, precio_out_por_mtok,
               precio_cache_write_por_mtok, precio_cache_read_por_mtok) <= 0 or tope_usd <= 0:
            raise ValueError("precios y tope deben ser positivos (autorización fase d)")
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
            namespace=namespace_cobertura(),
            thinking_enabled=False,
            run_label=run_label,
        )
        self.gasto_usd = 0.0  # solo misses (fórmula D2)
        self.llamadas = 0
        self.llamadas_hit = 0
        # Proyección conservadora de una llamada fría (patrón cliente_e1):
        # prefijo completo como cache write + variable mediana + salida máxima.
        self._proyeccion_usd = (
            6500 / 1e6 * self.p_cw
            + 1000 / 1e6 * self.p_in
            + prompt_e1.MAX_OUTPUT_TOKENS / 1e6 * self.p_out
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


# ----------------------- lectura read-only de una db de caché --------------- #
def conectar_db_readonly(db_path: Path) -> sqlite3.Connection:
    """Conexión SQLite estrictamente de solo lectura (URI mode=ro): ninguna
    escritura es posible — ni tablas, ni access_log, ni pragmas persistentes.
    Es la única forma en que esta unidad toca la db de producción (gate)."""
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def tool_input_de_raw(raw_json: str):
    """Extrae el input del bloque tool_use del crudo persistido en la caché
    (mismo criterio que cliente_e1.extraer_chunk: primer bloque tool_use)."""
    raw = json.loads(raw_json)
    for block in raw.get("content") or []:
        if isinstance(block, dict) and block.get("type") == "tool_use":
            return block.get("input")
    return None


def modelo_de_raw(raw_json: str):
    return json.loads(raw_json).get("model")


# ----------------------- jsonl helpers (patrón runner_corpus) --------------- #
def cargar_jsonl_last_wins(path: Path) -> dict[str, dict]:
    regs: dict[str, dict] = {}
    if path.exists():
        with path.open(encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    r = json.loads(linea)
                    regs[r["chunk_id"]] = r
    return regs
