"""
common.py — Constantes, schemas Pydantic, helpers de I/O y accounting de costo.

Compartido por todos los scripts del pipeline. No tiene side effects al importarse.
"""

from __future__ import annotations

import json
import os
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

# code/ está en data/experiment/run_1_cookbook/code/
CODE_DIR = Path(__file__).resolve().parent
RUN_DIR = CODE_DIR.parent
EXPERIMENT_DIR = RUN_DIR.parent
SUBSET_DIR = EXPERIMENT_DIR / "subset"          # READ-ONLY
CACHE_DIR = CODE_DIR / "cache"
KG_JSON_PATH = RUN_DIR / "kg.json"
REPORT_PATH = RUN_DIR / "report.md"

CACHE_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# .env loading — busca primero en el run, después en el repo root.
# Llamado explícitamente por los scripts que tocan la API.
# ---------------------------------------------------------------------------

def load_env() -> None:
    """Carga ANTHROPIC_API_KEY desde .env del run o del repo root.

    Si la variable ya está en os.environ con contenido no vacío, no la toca.
    Si está vacía o ausente, carga .env con override=True (algunos shells/agents
    inyectan ANTHROPIC_API_KEY="" que rompe el guardrail).
    """
    existing = os.environ.get("ANTHROPIC_API_KEY", "")
    if existing.strip():
        return
    candidates = [
        RUN_DIR / ".env",
        EXPERIMENT_DIR.parent.parent / ".env",   # repo root
    ]
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    for fp in candidates:
        if fp.exists():
            load_dotenv(fp, override=True)
            if os.environ.get("ANTHROPIC_API_KEY", "").strip():
                return


def require_api_key() -> None:
    """Aborta si no hay ANTHROPIC_API_KEY (con contenido) tras intentar cargar .env."""
    load_env()
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit(
            "ANTHROPIC_API_KEY no encontrada. Creá un .env en "
            f"{RUN_DIR}/.env con la línea: ANTHROPIC_API_KEY=sk-ant-..."
        )

# ---------------------------------------------------------------------------
# Subset metadata (del protocolo §a)
# ---------------------------------------------------------------------------

# Mapeo nombre_conceptual -> archivo PDF en subset/.
# El nombre conceptual es el slug humano usado en provenance y reporte de cobertura.
TO_FILES: dict[str, str] = {
    "clasificacion_deudores": "TO_clasificacion_deudores_actual.pdf",
    "capitales_minimos": "TO_capitales_minimos_actual.pdf",
    "exterior_cambios": "TO_exterior_cambios_actual.pdf",
    "proteccion_usuarios": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
    "regimen_informativo_cm": "TO_regimen_informativo_contable_mensual_actual.pdf",
}

# Última Comunicación "A" vigente de cada TO al momento del experimento.
# Se extrae automáticamente en 01_load_corpus.py de la primera página del PDF,
# pero se hardcodea acá como fallback y referencia.
TO_VERSIONS: dict[str, str] = {
    "clasificacion_deudores": "A 8378",
    "capitales_minimos": "A 8418",
    "exterior_cambios": "A 8307",
    "proteccion_usuarios": "A 8433",
    "regimen_informativo_cm": "A 6561",
}

# ---------------------------------------------------------------------------
# Tipos de entidad del schema (ver schema.md §2)
# ---------------------------------------------------------------------------

EntityType = Literal[
    "REGULATED_SUBJECT",
    "REGULATOR",
    "OPERATION",
    "REQUIREMENT",
    "CONCEPT",
    "INSTRUMENT",
    "CLASSIFICATION",
    "PROCESS",
    "SANCTION",
    "REPORT_ITEM",
]

ENTITY_TYPES: tuple[str, ...] = (
    "REGULATED_SUBJECT",
    "REGULATOR",
    "OPERATION",
    "REQUIREMENT",
    "CONCEPT",
    "INSTRUMENT",
    "CLASSIFICATION",
    "PROCESS",
    "SANCTION",
    "REPORT_ITEM",
)

# Prefijos cortos para los IDs de nodo (snake_case slug del canónico).
TYPE_PREFIX: dict[str, str] = {
    "REGULATED_SUBJECT": "rsj",
    "REGULATOR": "reg",
    "OPERATION": "ope",
    "REQUIREMENT": "req",
    "CONCEPT": "con",
    "INSTRUMENT": "ins",
    "CLASSIFICATION": "cla",
    "PROCESS": "prc",
    "SANCTION": "san",
    "REPORT_ITEM": "rep",
}

# ---------------------------------------------------------------------------
# Schemas Pydantic — mirror del cookbook, adaptados al dominio
# ---------------------------------------------------------------------------

class Entity(BaseModel):
    """Una entidad regulatoria extraída de un chunk del TO. Mirror de cookbook §2.1."""
    name: str = Field(description="Nombre canónico o surface form de la entidad.")
    type: EntityType = Field(description="Tipo de entidad según el schema del run.")
    description: str = Field(
        description="Descripción de una oración, fundamentada en este chunk, "
                    "para desambiguar la entidad en la etapa de resolución."
    )


class Relation(BaseModel):
    """Una relación entre dos entidades extraídas del mismo chunk. Mirror de cookbook §2.2."""
    source: str = Field(description="Nombre de la entidad origen (debe estar entre las entidades extraídas).")
    predicate: str = Field(description="Verb phrase corta en español (ej. 'está_sujeto_a', 'aplica_a').")
    target: str = Field(description="Nombre de la entidad destino (debe estar entre las entidades extraídas).")


class ExtractedGraph(BaseModel):
    """Output del structured extraction de un chunk. Mirror de cookbook §2.3.

    `relations` con default vacío: si un chunk sólo declara entidades sin relacionarlas
    explícitamente (suele pasar con definiciones aisladas), no rompemos el parsing.
    """
    entities: list[Entity] = Field(default_factory=list)
    relations: list[Relation] = Field(default_factory=list)


class Cluster(BaseModel):
    """Un cluster de surface forms que refieren a la misma entidad. Mirror de cookbook §2."""
    canonical: str = Field(description="La forma más completa y no-ambigua del nombre.")
    aliases: list[str] = Field(description="Todos los surface forms que mapean a este canónico.")


class ResolvedClusters(BaseModel):
    """Output del entity resolution para un tipo dado. Mirror de cookbook §5."""
    clusters: list[Cluster]


class TimeRange(BaseModel):
    """Para hub summarization. Mirror de cookbook §6."""
    start: str = Field(description='YYYY o YYYY-MM o "unknown".')
    end: str = Field(description='YYYY o YYYY-MM o "unknown" o "ongoing" (norma vigente).')


class EntityProfile(BaseModel):
    """Perfil enriquecido para un nodo hub. Mirror de cookbook §6."""
    summary: str = Field(description="Síntesis factual en 2-3 párrafos.")
    key_facts: list[str] = Field(description="3-5 hechos atómicos trazables al corpus.")
    time_range: TimeRange


# ---------------------------------------------------------------------------
# Cost accounting
# ---------------------------------------------------------------------------

# Precios públicos por millón de tokens (USD), a la fecha del experimento.
# - cache_write: 1.25x el input base (escritura inicial del bloque cacheado).
# - cache_read:  0.10x el input base (lecturas posteriores del bloque cacheado).
PRICES_PER_MTOK: dict[str, dict[str, float]] = {
    "claude-haiku-4-5":   {"input": 1.00, "output": 5.00, "cache_write": 1.25, "cache_read": 0.10},
    "claude-sonnet-4-6":  {"input": 3.00, "output": 15.00, "cache_write": 3.75, "cache_read": 0.30},
}

# Presupuesto del protocolo: USD 5 por instancia.
# Excepción 1 (autorizada tras smoke): USD 5 → USD 10. Razón: smoke mostró que USD 5
#   alcanza para ~60% del corpus.
# Excepción 2 (autorizada tras resolución): USD 10 → USD 11. Razón: la resolución
#   Sonnet costó 3.4x más que lo proyectado por output-tokens más largos de lo
#   esperado en clusters; queda <USD 1 para hub summarization, que pertenece al
#   pipeline del cookbook (no a evaluación). Ambas excepciones documentadas
#   exhaustivamente en report.md §"Excepciones al protocolo".
BUDGET_USD_HARD = 11.00      # límite duro autorizado para Run 1
BUDGET_USD_ABORT = 10.80     # margen de seguridad: aborta si el acumulado pasa esto


@dataclass
class CostLedger:
    """Acumula tokens y costo por modelo. Se persiste por etapa en cache/cost_*.json.

    Cuatro buckets de tokens:
      - input_tokens          → user-msg + system (cuando no se cachea)
      - output_tokens         → respuesta del modelo
      - cache_creation_tokens → primera vez que se escribe un bloque cacheado (1.25x)
      - cache_read_tokens     → lecturas cacheadas (0.10x)
    """
    by_model: dict[str, dict[str, float]]

    @classmethod
    def empty(cls) -> "CostLedger":
        return cls(by_model={})

    def record(
        self,
        model: str,
        input_tokens: int,
        output_tokens: int,
        cache_creation_tokens: int = 0,
        cache_read_tokens: int = 0,
    ) -> float:
        """Registra una llamada y devuelve el USD incurrido por ESTA llamada."""
        if model not in PRICES_PER_MTOK:
            raise ValueError(f"Modelo desconocido para pricing: {model}")
        p = PRICES_PER_MTOK[model]
        usd = (
            input_tokens * p["input"]
            + output_tokens * p["output"]
            + cache_creation_tokens * p.get("cache_write", p["input"])
            + cache_read_tokens * p.get("cache_read", p["input"])
        ) / 1_000_000
        slot = self.by_model.setdefault(
            model,
            {
                "input_tokens": 0,
                "output_tokens": 0,
                "cache_creation_tokens": 0,
                "cache_read_tokens": 0,
                "calls": 0,
                "usd": 0.0,
            },
        )
        # Backward compat con ledgers antiguos sin las nuevas keys
        slot.setdefault("cache_creation_tokens", 0)
        slot.setdefault("cache_read_tokens", 0)
        slot["input_tokens"] += input_tokens
        slot["output_tokens"] += output_tokens
        slot["cache_creation_tokens"] += cache_creation_tokens
        slot["cache_read_tokens"] += cache_read_tokens
        slot["calls"] += 1
        slot["usd"] += usd
        return usd

    @property
    def total_usd(self) -> float:
        return sum(s["usd"] for s in self.by_model.values())

    def to_json(self) -> dict:
        return {
            "by_model": self.by_model,
            "total_usd": round(self.total_usd, 6),
        }


def load_ledger(stage: str) -> CostLedger:
    """Carga el ledger persistido de una etapa (o devuelve uno vacío)."""
    fp = CACHE_DIR / f"cost_{stage}.json"
    if not fp.exists():
        return CostLedger.empty()
    data = json.loads(fp.read_text())
    return CostLedger(by_model=data.get("by_model", {}))


def save_ledger(stage: str, ledger: CostLedger) -> None:
    fp = CACHE_DIR / f"cost_{stage}.json"
    fp.write_text(json.dumps(ledger.to_json(), indent=2))


def total_cost_so_far() -> float:
    """Suma del costo de TODAS las etapas registradas en cache/."""
    total = 0.0
    for fp in CACHE_DIR.glob("cost_*.json"):
        try:
            total += json.loads(fp.read_text()).get("total_usd", 0.0)
        except Exception:
            pass
    return total


def assert_under_budget(margin: float = BUDGET_USD_ABORT) -> None:
    """Aborta si el costo acumulado de todas las etapas pasa `margin` USD."""
    total = total_cost_so_far()
    if total >= margin:
        raise RuntimeError(
            f"Presupuesto excedido: USD {total:.4f} >= USD {margin:.2f} "
            f"(límite duro USD {BUDGET_USD_HARD:.2f}). Abortando."
        )


# ---------------------------------------------------------------------------
# Helpers de slug / canónico
# ---------------------------------------------------------------------------

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """snake_case slug ASCII, idempotente."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower().strip()
    text = _NON_ALNUM.sub("_", text)
    return text.strip("_")


def make_node_id(canonical: str, etype: str) -> str:
    """ID del nodo: <prefijo_tipo>_<slug_del_canónico>. Determinístico."""
    prefix = TYPE_PREFIX.get(etype, "ent")
    return f"{prefix}_{slugify(canonical)}"


# ---------------------------------------------------------------------------
# Helpers de I/O
# ---------------------------------------------------------------------------

def read_jsonl(fp: Path) -> list[dict]:
    if not fp.exists():
        return []
    return [json.loads(line) for line in fp.read_text().splitlines() if line.strip()]


def write_jsonl(fp: Path, rows: list[dict]) -> None:
    fp.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n")


def read_json(fp: Path) -> dict:
    return json.loads(fp.read_text())


def write_json(fp: Path, obj: dict) -> None:
    fp.write_text(json.dumps(obj, ensure_ascii=False, indent=2))


# ---------------------------------------------------------------------------
# Sanity check de jerarquía documental (regla protocolo §c.1)
# ---------------------------------------------------------------------------

DOC_HIERARCHY_PATTERNS = [
    re.compile(r"^\s*(secci[oó]n|punto|cap[ií]tulo|art[ií]culo|t[ií]tulo)\s+[\divxlc]+", re.IGNORECASE),
    re.compile(r'^\s*[“"]?A[”"]?\s*\d{3,5}\s*$'),   # "A 1234" suelto
    re.compile(r'^\s*[“"]?B[”"]?\s*\d{3,5}\s*$'),
    re.compile(r"^\s*comunicaci[oó]n\s+[“\"]?[AB][”\"]?\s*\d", re.IGNORECASE),
]


def is_documental_hierarchy(text: str) -> bool:
    """True si el texto parece referirse a jerarquía documental (regla §c.1)."""
    if not text:
        return False
    for pat in DOC_HIERARCHY_PATTERNS:
        if pat.match(text.strip()):
            return True
    return False
