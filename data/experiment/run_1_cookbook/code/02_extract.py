"""
02_extract.py — Etapa 2 del cookbook: Entity & Relation Extraction.

Por cada chunk de cache/chunks.jsonl, una llamada a Claude Haiku con
structured output (Pydantic schema `ExtractedGraph`) para extraer
entidades y relaciones grounded en ese chunk.

Optimizaciones implementadas:
  - Prompt caching del system block (~1.5K tokens estáticos → cache_read en
    llamadas 2+ a ~10x menos costo).
  - Retry con tenacity ante RateLimitError / APITimeoutError / overloaded.
  - Concurrency baja (3) para no pegar el rate limit de output tokens/min.
  - max_tokens=2048 (chunks productivos no superan ~1700 out).

Modelo: claude-haiku-4-5 (extracción de alto volumen, costo/velocidad).
Idempotencia: si raw_extractions.jsonl ya contiene el chunk_id, se saltea.
Budget guard: aborta si el costo acumulado pasa BUDGET_USD_ABORT.

Output:
  cache/raw_extractions.jsonl  → 1 línea por chunk: {chunk_id, entities, relations, usage}
  cache/cost_extraction.json   → ledger (input/output/cache_write/cache_read tokens)
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (
    CACHE_DIR,
    CostLedger,
    ExtractedGraph,
    assert_under_budget,
    load_ledger,
    read_jsonl,
    require_api_key,
    save_ledger,
    write_jsonl,
)

CHUNKS_PATH = CACHE_DIR / "chunks.jsonl"
EXTRACTIONS_PATH = CACHE_DIR / "raw_extractions.jsonl"
STAGE = "extraction"

EXTRACTION_MODEL = "claude-haiku-4-5"
MAX_CONCURRENCY = 3                 # bajado de 8 — rate limit es 10K output tok/min
MAX_TOKENS_OUT = 2048               # bajado de 4096 — chunks productivos peakean ~1700

# Retry parameters
RETRY_MAX_ATTEMPTS = 6
RETRY_WAIT_MIN = 4                  # segundos
RETRY_WAIT_MAX = 60

# Heurísticas de skip de chunks no-productivos (ahorra ~15% de llamadas Haiku
# sin tocar la cobertura de contenido normativo).
import re as _re
_INDEX_LINE_RE = _re.compile(r"^\s*(secci[oó]n|punto)\s+[\divxlc]+\.\s", _re.I)
_COMA_LINE_RE = _re.compile(r'^\s*[“"]?\s*[AB]\s*[”"]?\s*[\-:]?\s*\d{3,5}\s*[:\.\-]')
_HEADER_RE = _re.compile(r"última comunicación incorporada|texto ordenado al", _re.I)


def is_non_productive_chunk(text: str) -> tuple[bool, str]:
    """
    Decide si un chunk es índice / encabezado / listado de Comunicaciones — y
    por lo tanto skippeable sin gastar Haiku. Devuelve (skip, motivo).

    Heurísticas (todas deben ser de bajo falso positivo — preferimos pagar
    un chunk de más a perder contenido normativo):

    1. Texto muy corto (<400 chars) + matchea header del TO → encabezado.
    2. Índice: ≥6 líneas que matchean "Sección N." o "Punto N.M." y constituyen
       >50% de las líneas no-vacías.
    3. Listado de Comunicaciones: ≥10 líneas que matchean "A 1234:" / "B 9876:"
       y constituyen >50% de las líneas no-vacías.
    """
    if not text or not text.strip():
        return True, "empty_text"

    body = text.strip()
    lines = [l for l in body.splitlines() if l.strip()]

    # 1) Encabezado/portada
    if len(body) < 400 and _HEADER_RE.search(body):
        return True, "header_page"

    if not lines:
        return True, "empty_lines"

    # 2) Índice
    index_lines = sum(1 for l in lines if _INDEX_LINE_RE.search(l))
    if index_lines >= 6 and index_lines / len(lines) > 0.5:
        return True, f"index_page (index_lines={index_lines}/{len(lines)})"

    # 3) Listado de Comunicaciones vinculadas
    com_lines = sum(1 for l in lines if _COMA_LINE_RE.search(l))
    if com_lines >= 10 and com_lines / len(lines) > 0.5:
        return True, f"comunicaciones_listing (com_lines={com_lines}/{len(lines)})"

    return False, ""

# ---------------------------------------------------------------------------
# Prompts — adaptación del EXTRACTION_PROMPT del cookbook
# ---------------------------------------------------------------------------
# El SYSTEM_PROMPT concentra toda la INSTRUCCIÓN ESTÁTICA (reglas + lista de
# tipos), para que entre completa en un único bloque cacheado (prompt caching
# requiere mínimo ~1024 tokens para que el cache valga la pena).
# El USER_PROMPT_TEMPLATE queda con SOLO el texto variable del chunk.
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """Sos un extractor de Knowledge Graph para regulación financiera del Banco Central de la República Argentina (BCRA).

Tu trabajo es extraer entidades regulatorias y relaciones de un fragmento de un Texto Ordenado del BCRA, devolviendo un grafo bien tipado.

Reglas duras:
1. Los nodos son ENTIDADES REGULATORIAS REALES (sujetos regulados, reguladores, operaciones, exigencias, conceptos definidos, instrumentos financieros, clasificaciones, procesos, sanciones, items del régimen informativo).
2. NUNCA extraigas como entidad: "Sección X.Y", "Punto 3.4", "Comunicación A 1234", "Capítulo", "Artículo". Eso es jerarquía documental y va en provenance, no como nodo.
3. NUNCA extraigas el TO mismo ("Capitales Mínimos", "Clasificación de Deudores", etc.) como entidad. Es el documento fuente.
4. Cada `description` debe ser una oración corta GROUNDED en este fragmento — sirve para desambiguar entidades con nombres similares en la etapa de resolución.
5. Predicados: verb phrases cortas en español snake_case (ej. "está_sujeto_a", "aplica_a", "regula", "informa_a", "pondera"). No prosa larga.
6. Cada `source` y `target` de una relación DEBE estar entre las entidades extraídas en este mismo fragmento.

Tipos de entidad permitidos (elegí uno por entidad):
- REGULATED_SUBJECT: persona jurídica o categoría regulada (entidad financiera, PSPCP, casa de cambio, exportador, usuario, sujeto obligado).
- REGULATOR: órgano con potestad regulatoria/supervisora (BCRA, SEFyC, Gerencia Principal de Exterior y Cambios).
- OPERATION: operación regulada (cobro de exportación, pago de importación, otorgamiento de crédito, compra de divisas).
- REQUIREMENT: exigencia cuantitativa o cualitativa, plazo, ratio, ponderador, obligación de hacer/no hacer.
- CONCEPT: término jurídico-técnico definido o usado de manera estable (RPC, deudor, MULC, CCF, garantía preferida).
- INSTRUMENT: instrumento, activo o garantía (cheque, título de deuda, derivado, garantía hipotecaria, tarjeta de crédito).
- CLASSIFICATION: categoría o nivel definido (Situación 1, Situación 5, cartera comercial, Método simple, código de consolidación).
- PROCESS: procedimiento administrativo (análisis de cartera, recategorización obligatoria, debida diligencia).
- SANCTION: consecuencia jurídica/económica por incumplimiento.
- REPORT_ITEM: código contable, partida, modelo de información del régimen informativo (ej. Código 22100000).

Si el fragmento es índice, encabezado, o listado de Comunicaciones sin contenido normativo, devolvé entities=[] y relations=[]."""


USER_PROMPT_TEMPLATE = """Fragmento del Texto Ordenado "{to_label}" (versión vigente: {version}, ubicación: {location}):

<fragmento>
{text}
</fragmento>

Extraé las entidades centrales y sus relaciones."""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def already_extracted_ids() -> set[str]:
    rows = read_jsonl(EXTRACTIONS_PATH)
    return {r["chunk_id"] for r in rows}


def build_user_prompt(chunk: dict) -> str:
    return USER_PROMPT_TEMPLATE.format(
        to_label=chunk["to"].replace("_", " ").title(),
        version=chunk["version"],
        location=chunk["location_label"],
        text=chunk["text"],
    )


# ---------------------------------------------------------------------------
# Llamada a la API — STUB. Se implementa cuando se autorice gastar tokens.
# ---------------------------------------------------------------------------

async def call_haiku_extract(client, chunk: dict) -> tuple[ExtractedGraph, dict]:
    """
    Llama a Haiku con structured output (tool_use forzado al schema Pydantic)
    y prompt caching del system block.

    Devuelve (ExtractedGraph, usage_dict) con cuatro buckets de tokens:
        usage_dict = {
            "input_tokens": int,                # tokens del user msg (no cacheable)
            "output_tokens": int,
            "cache_creation_input_tokens": int, # primera vez que se cachea el system
            "cache_read_input_tokens": int,     # lecturas cacheadas del system
            "model": EXTRACTION_MODEL,
        }

    Retry con backoff exponencial ante RateLimitError, APITimeoutError y errores
    transitorios (5xx / overloaded).
    """
    import anthropic
    from tenacity import (
        AsyncRetrying,
        retry_if_exception_type,
        stop_after_attempt,
        wait_random_exponential,
    )

    schema = ExtractedGraph.model_json_schema()

    retryable = (
        anthropic.RateLimitError,
        anthropic.APITimeoutError,
        anthropic.APIConnectionError,
        anthropic.InternalServerError,
    )

    async for attempt in AsyncRetrying(
        retry=retry_if_exception_type(retryable),
        wait=wait_random_exponential(min=RETRY_WAIT_MIN, max=RETRY_WAIT_MAX),
        stop=stop_after_attempt(RETRY_MAX_ATTEMPTS),
        reraise=True,
    ):
        with attempt:
            msg = await client.messages.create(
                model=EXTRACTION_MODEL,
                max_tokens=MAX_TOKENS_OUT,
                system=[{
                    "type": "text",
                    "text": SYSTEM_PROMPT,
                    "cache_control": {"type": "ephemeral"},
                }],
                messages=[{"role": "user", "content": build_user_prompt(chunk)}],
                tools=[{
                    "name": "emit_graph",
                    "description": "Emite el grafo extraído del fragmento del Texto Ordenado.",
                    "input_schema": schema,
                }],
                tool_choice={"type": "tool", "name": "emit_graph"},
            )

    # Encontrar el bloque tool_use (el modelo puede emitir text + tool_use).
    tool_block = None
    for b in msg.content:
        if getattr(b, "type", None) == "tool_use":
            tool_block = b
            break
    if tool_block is None:
        raise RuntimeError(
            f"Haiku no emitió tool_use para chunk={chunk['chunk_id']} "
            f"(stop_reason={msg.stop_reason})"
        )

    # Validación con fallback: si Haiku inventa un type fuera del enum,
    # filtramos esa entidad y reconstruimos. Mejor perder 1 entidad que el chunk entero.
    from common import ENTITY_TYPES as _VALID_TYPES
    try:
        graph = ExtractedGraph.model_validate(tool_block.input)
    except Exception:
        raw = tool_block.input if isinstance(tool_block.input, dict) else {}
        cleaned_entities = []
        invalid_types = []
        for e in raw.get("entities", []) or []:
            if isinstance(e, dict) and e.get("type") in _VALID_TYPES:
                cleaned_entities.append(e)
            elif isinstance(e, dict):
                invalid_types.append(e.get("type"))
        cleaned_names = {e["name"] for e in cleaned_entities if isinstance(e.get("name"), str)}
        cleaned_relations = [
            r for r in (raw.get("relations") or [])
            if isinstance(r, dict)
            and r.get("source") in cleaned_names
            and r.get("target") in cleaned_names
        ]
        graph = ExtractedGraph.model_validate({
            "entities": cleaned_entities,
            "relations": cleaned_relations,
        })
        if invalid_types:
            print(
                f"[02_extract] WARN chunk={chunk['chunk_id']}: descartadas {len(invalid_types)} "
                f"entidades con type fuera del schema: {sorted(set(invalid_types))}"
            )

    usage = {
        "input_tokens": msg.usage.input_tokens,
        "output_tokens": msg.usage.output_tokens,
        "cache_creation_input_tokens": getattr(msg.usage, "cache_creation_input_tokens", 0) or 0,
        "cache_read_input_tokens": getattr(msg.usage, "cache_read_input_tokens", 0) or 0,
        "model": EXTRACTION_MODEL,
    }
    return graph, usage


# ---------------------------------------------------------------------------
# Worker
# ---------------------------------------------------------------------------

async def extract_one(client, chunk: dict, sem: asyncio.Semaphore, ledger: CostLedger) -> dict | None:
    async with sem:
        try:
            graph, usage = await call_haiku_extract(client, chunk)
        except NotImplementedError:
            raise
        except Exception as e:
            print(f"[02_extract] ERROR chunk={chunk['chunk_id']}: {type(e).__name__}: {e}")
            return None

        ledger.record(
            usage["model"],
            usage["input_tokens"],
            usage["output_tokens"],
            cache_creation_tokens=usage.get("cache_creation_input_tokens", 0),
            cache_read_tokens=usage.get("cache_read_input_tokens", 0),
        )
        assert_under_budget()  # aborta si pasamos el margen

        return {
            "chunk_id": chunk["chunk_id"],
            "to": chunk["to"],
            "source_doc": chunk["source_doc"],
            "location": chunk["location_label"],
            "version": chunk["version"],
            "entities": [e.model_dump() for e in graph.entities],
            "relations": [r.model_dump() for r in graph.relations],
            "usage": usage,
        }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def amain(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Etapa 2: extracción con Haiku.")
    parser.add_argument("--limit", type=int, default=None, help="Procesa sólo los primeros N chunks (smoke test).")
    parser.add_argument("--to", type=str, default=None, help="Filtra a un TO específico (ej. proteccion_usuarios).")
    parser.add_argument("--force", action="store_true", help="Re-procesa chunks aunque ya estén en raw_extractions.jsonl.")
    args = parser.parse_args(argv)

    if not CHUNKS_PATH.exists():
        print(f"[02_extract] Falta {CHUNKS_PATH}. Corré 01_load_corpus.py primero.")
        return 1

    chunks = read_jsonl(CHUNKS_PATH)
    if args.to:
        chunks = [c for c in chunks if c["to"] == args.to]
    if not args.force:
        done = already_extracted_ids()
        chunks = [c for c in chunks if c["chunk_id"] not in done]
    if args.limit:
        chunks = chunks[: args.limit]

    if not chunks:
        print("[02_extract] Nada para procesar.")
        return 0

    # Pre-filtro heurístico: skippea chunks no-productivos sin gastar Haiku.
    # Se persisten como entradas con usage="heuristic_skip" para mantener
    # idempotencia + cobertura reportable.
    to_call: list[dict] = []
    skipped = 0
    import json as _json
    for c in chunks:
        skip, reason = is_non_productive_chunk(c["text"])
        if skip:
            row = {
                "chunk_id": c["chunk_id"],
                "to": c["to"],
                "source_doc": c["source_doc"],
                "location": c["location_label"],
                "version": c["version"],
                "entities": [],
                "relations": [],
                "usage": {"input_tokens": 0, "output_tokens": 0,
                          "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0,
                          "model": "heuristic_skip", "skip_reason": reason},
            }
            with EXTRACTIONS_PATH.open("a", encoding="utf-8") as fh:
                fh.write(_json.dumps(row, ensure_ascii=False) + "\n")
            skipped += 1
        else:
            to_call.append(c)

    print(f"[02_extract] Skipped por heurística: {skipped} chunks (índice/encabezado/listado Com.A).")
    if not to_call:
        print("[02_extract] No quedan chunks productivos para llamar a Haiku.")
        return 0

    print(f"[02_extract] Llamando a {EXTRACTION_MODEL} para {len(to_call)} chunks (concurrency={MAX_CONCURRENCY}).")
    chunks = to_call
    assert_under_budget()

    require_api_key()
    import anthropic
    client = anthropic.AsyncAnthropic()

    ledger = load_ledger(STAGE)
    sem = asyncio.Semaphore(MAX_CONCURRENCY)
    tasks = [extract_one(client, c, sem, ledger) for c in chunks]
    rows = []
    for fut in asyncio.as_completed(tasks):
        row = await fut
        if row is not None:
            rows.append(row)
            # Append-mode persist por seguridad: si crashea, no perdemos lo extraído.
            with EXTRACTIONS_PATH.open("a", encoding="utf-8") as fh:
                import json as _json
                fh.write(_json.dumps(row, ensure_ascii=False) + "\n")
            save_ledger(STAGE, ledger)

    save_ledger(STAGE, ledger)
    print(f"[02_extract] OK · {len(rows)} chunks extraídos · USD acumulado etapa: {ledger.total_usd:.4f}")
    return 0


def main(argv: list[str] | None = None) -> int:
    return asyncio.run(amain(argv))


if __name__ == "__main__":
    raise SystemExit(main())
