"""
comun_esq3b.py — Paths, constantes y cliente de la unidad U-ESQ-3b (corrida
pareada de dos brazos sobre el esquema retocado).

Gobernado por:
  - data/experiment/esq/laudo_ESQ-3a_retoques.md (0a76549, FIRMADO 02/09/2026)
  - data/experiment/esq/prerregistro_esq3b.md    (01bf046, FIRMADO 02/09/2026)

Diseño sellado que este módulo implementa sin re-decidir:
  - Brazo BASE: las extracciones ya persistidas de ESQ-2 (sellos a7788c1) —
    NO se re-corre, cuesta USD 0 y `cobertura/` es de SOLO LECTURA.
  - Brazo NUEVO: las mismas unidades con el prefijo retocado
    (prompt_esq3b.build_request_kwargs_retocado).
  - Tope propio DURO de la unidad: USD 1,00 (pre-registro §5), cableado en el
    cliente (proyección pre-llamada) y re-chequeado por el runner.

Decisiones de caching (docs/decisiones_caching_extraccion.md), vinculantes:
  - D1: prefijo retocado estable con cache_control ephemeral (lo arma
    prompt_esq3b; nada variable por chunk entra antes del breakpoint).
  - D2: todo costo con la fórmula de caching (costo_usd_desde_usage).
  - D3: component propio "esq3b_pareado_e1" en logs/cache_usage.jsonl.
  - D4: corrida SECUENCIAL (un cliente, un loop; el runner lo respeta).
  - D5: no aplica (esto es extracción, no evaluación).

Caché: db PROPIA NUEVA `esq/cache/esq_3b.db` (gitignorada), namespace propio
`esq3b_pareado_e1` con el hash del prefijo RETOCADO como candado (namespace por
prefijo-hash). Distinto por construcción del de producción y del de ESQ-2: esta
unidad no puede leer ni pisar una sola key ajena.

Tarifas y modelo: verbatim de
data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py:76-78
(claude-haiku-4-5 — 1,00 / 5,00 / 1,25 / 0,10 USD/MTok); el selftest verifica
la transcripción contra ese archivo sin importarlo. El modelo REALMENTE usado
se resuelve por llamada desde el `raw_json` de la db (patrón U-ESQ-2).
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

COBERTURA_DIR = UNIDAD_DIR / "cobertura"            # ESQ-2 — SOLO LECTURA
ORDEN_DIR = COBERTURA_DIR / "orden"                 # selecciones (se AGREGA un archivo)
WORKSHEET_ESQ2 = COBERTURA_DIR / "fichas" / "worksheet_fichas_esq2.json"

ESQ3B_DIR = UNIDAD_DIR / "esq3b"                    # salidas propias de la unidad
EXTRACCIONES_DIR = ESQ3B_DIR / "extracciones"
FICHAS_DIR = ESQ3B_DIR / "fichas"

CACHE_DIR = UNIDAD_DIR / "cache"                    # gitignorada (esq/.gitignore)
SELFTEST_DIR = UNIDAD_DIR / "selftest_out"          # gitignorada

DB_ESQ3B = CACHE_DIR / "esq_3b.db"                  # db PROPIA NUEVA de la unidad
# dbs de la saga ESQ + de producción: la propia no colisiona con ninguna
# (guarda del selftest).
DBS_AJENAS = (
    CACHE_DIR / "esq_cobertura.db",
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
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_e1        # noqa: E402,F401  (agrega grafo_v2/code y evaluacion al path)
import prompt_e1       # noqa: E402  — se importa, jamás se edita
import llm_cache as lc  # noqa: E402  — se ENVUELVE, jamás se edita
import prompt_esq3b as pr  # noqa: E402  — prefijo retocado de la unidad

# ----------------------- universo (heredado de ESQ-2) ----------------------- #
TOS_ESQ2 = ("ayccef", "expaef", "opefci", "adrei", "cryl",
            "actgar", "prevmi", "lavdin", "traval", "ctacor")
ESCALADO_E0 = EXP_DIR / "escalado_prep" / "e0_dry"

# ----------------------- tarifas / modelo / tope ---------------------------- #
# Verbatim runner_corpus.py:76-78 (corrida sellada del corpus).
MODEL_E1 = "claude-haiku-4-5"
P_E1 = dict(precio_in_por_mtok=1.00, precio_out_por_mtok=5.00,
            precio_cache_write_por_mtok=1.25, precio_cache_read_por_mtok=0.10)

TOPE_USD = 1.00          # pre-registro ESQ-3b §5 — tope propio de la unidad, duro

# ----------------------- namespace y candados ------------------------------- #
DOMAIN = "esq3b_pareado_e1"
CODE_VER = "esq3b-pareado-v1"

# Candado del prefijo de PRODUCCIÓN sobre el que se aplican los retoques: si
# prompt_e1 cambia, el retoque estaría sobre otro texto base y el selftest FRENA.
PREFIJO_HASH_PRODUCCION_ESPERADO = pr.PREFIJO_HASH_PRODUCCION_ESPERADO


def namespace_esq3b() -> str:
    """Namespace propio: dominio propio + code-ver propio + hash del prefijo
    RETOCADO (namespace por prefijo-hash; precedente cliente_e1.namespace_e1 y
    comun_cobertura_esq2.namespace_cobertura). Distinto por construcción del de
    producción, del de ESQ-2 y de los de la saga ESQ."""
    return lc.make_namespace(
        DOMAIN,
        code_ver=f"{CODE_VER}-p{pr.PREFIJO_HASH_RETOCADO}",
        thinking=False,
    )


def namespace_produccion() -> str:
    """Namespace de la caché de producción flag-off — SOLO para las guardas de
    no-colisión, en lectura."""
    import cliente_e1
    return cliente_e1.namespace_e1(canal_abierto=False)


def namespace_cobertura_esq2() -> str:
    """Namespace de U-ESQ-2 — SOLO para la guarda de no-colisión."""
    return lc.make_namespace(
        "esq2_cobertura_e1",
        code_ver=f"esq2-cobertura-v1-p{prompt_e1.prefijo_hash(False)}",
        thinking=False,
    )


# ----------------------- carga de chunks (solo lectura) --------------------- #
def cargar_chunks_esq2(tos: tuple[str, ...] = TOS_ESQ2) -> list[dict]:
    """Chunks E0 de escalado_prep en orden estable. Solo lectura."""
    chunks: list[dict] = []
    for to in tos:
        path = ESCALADO_E0 / to / f"chunks_{to}.json"
        with path.open(encoding="utf-8") as f:
            chunks.extend(json.load(f))
    return chunks


def cargar_extracciones_esq2(tos: tuple[str, ...] = TOS_ESQ2) -> dict[str, dict]:
    """Extracciones persistidas de ESQ-2 (brazo BASE, sellos a7788c1).
    SOLO LECTURA: esta unidad no escribe una línea en cobertura/<to>/."""
    regs: dict[str, dict] = {}
    for to in tos:
        regs.update(cargar_jsonl_last_wins(
            COBERTURA_DIR / to / f"extracciones_e1_{to}.jsonl"))
    return regs


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
    """Freno duro pre-llamada: gasto acumulado + proyección conservadora de UNA
    llamada fría > tope ⇒ TopeExcedido, la llamada no sale."""
    if gasto_usd + proyeccion_usd > tope_usd:
        raise TopeExcedido(
            f"gasto acumulado USD {gasto_usd:.4f} + proyección "
            f"{proyeccion_usd:.4f} supera el tope {tope_usd:.2f}")


class ClienteEsq3b:
    """Cliente real de la unidad — patrón de cliente_e1.ClienteE1Real COPIADO
    (el módulo de producción no se toca) con: db propia NUEVA, namespace propio,
    component propio en el log D3, tope duro USD 1,00. Contabilidad D2 sobre
    misses; los hits de la caché local no cuestan ni se loguean (no son
    responses de la API)."""

    COMPONENT = "esq3b_pareado_e1"

    def __init__(self, *, precio_in_por_mtok: float, precio_out_por_mtok: float,
                 precio_cache_write_por_mtok: float, precio_cache_read_por_mtok: float,
                 tope_usd: float, run_label: str, db_path: Path = DB_ESQ3B):
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
            namespace=namespace_esq3b(),
            thinking_enabled=False,
            run_label=run_label,
        )
        self.gasto_usd = 0.0  # solo misses (fórmula D2)
        self.llamadas = 0
        self.llamadas_hit = 0
        # Proyección conservadora de una llamada fría: prefijo RETOCADO completo
        # como cache write + variable mediana + salida máxima.
        self._proyeccion_usd = (
            8000 / 1e6 * self.p_cw
            + 1000 / 1e6 * self.p_in
            + pr.MAX_OUTPUT_TOKENS / 1e6 * self.p_out
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
    """Conexión SQLite estrictamente de solo lectura (URI mode=ro)."""
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def tool_input_de_raw(raw_json: str):
    """Input del primer bloque tool_use del crudo persistido en la caché."""
    raw = json.loads(raw_json)
    for block in raw.get("content") or []:
        if isinstance(block, dict) and block.get("type") == "tool_use":
            return block.get("input")
    return None


def modelo_de_raw(raw_json: str):
    """Modelo RESUELTO por llamada, leído del crudo (no el alias pedido)."""
    return json.loads(raw_json).get("model")


# ----------------------- jsonl helpers -------------------------------------- #
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
