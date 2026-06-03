"""
Extractor del Run 5 — Híbrido core + emergente.

Pipeline:
1. Chunkea los PDFs del subset (chunker.py).
2. Para cada chunk, llama a Claude Haiku 4.5 con SYSTEM_PROMPT + USER_PROMPT_TEMPLATE.
3. Parsea la respuesta como ChunkExtraction (entities + relations sin provenance).
4. **Inyecta provenance** desde el contexto del chunk en cada entity y cada relation.
5. Cachea por chunk_id (resumible si se mata el proceso).
6. Loggea progreso cada N chunks con costo acumulado, rate, ETA (lección Run 2 #3).

Concurrency=3 (lección Run 1 #3). Backoff conservador 3 reintentos base 2.0
(lección Run 2 #4). Cache por chunk individual, sin cachear errores (lección Run 2 #5).
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
import time
from collections import deque
from pathlib import Path
from typing import Any

from anthropic import AsyncAnthropic, APIStatusError
from pydantic import ValidationError

from chunker import chunk_pdf
from models import Chunk, ChunkExtraction, KGEdge, KGNode, Provenance
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE


# ---------- Configuración ----------

MODEL = "claude-haiku-4-5"
MAX_TOKENS = 8192  # 4096 dejó truncados 3/48 en el smoke (output JSON cortado a mitad)
CONCURRENCY = 3  # lección Run 1 #3
MAX_RETRIES = 3
RETRY_BASE = 2.0  # lección Run 2 #4
LOG_EVERY = 5  # lección Run 2 #3

# Pricing Haiku 4.5 (USD por MTok) — al 2025-Q4.
PRICE_IN_USD_PER_MTOK = 1.00
PRICE_OUT_USD_PER_MTOK = 5.00

RUN_DIR = Path(__file__).resolve().parent.parent  # data/experiment/run_5_hybrid/
CACHE_DIR = RUN_DIR / "code" / "cache" / "chunks"
LOGS_DIR = RUN_DIR / "code" / "cache" / "logs"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

SUBSET_DIR = Path("/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/subset")


# ---------- Helpers ----------


def _parse_json_strict(raw: str) -> dict[str, Any]:
    """
    Parsea JSON tolerando bloques markdown y texto suelto alrededor.
    """
    # Quita fences ```json ... ``` o ``` ... ```
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
    if fenced:
        return json.loads(fenced.group(1))
    # Si no, busca el primer objeto JSON balanceado.
    start = raw.find("{")
    if start < 0:
        raise ValueError("No JSON object found in model output")
    # Busca el cierre balanceado.
    depth = 0
    for i in range(start, len(raw)):
        if raw[i] == "{":
            depth += 1
        elif raw[i] == "}":
            depth -= 1
            if depth == 0:
                return json.loads(raw[start : i + 1])
    raise ValueError("Unbalanced JSON in model output")


# ============================================================================
# INYECCIÓN DE PROVENANCE — el pedazo crítico que pidió la autora del experimento.
# ============================================================================


def hydrate_with_provenance(
    extraction: ChunkExtraction, chunk: Chunk
) -> tuple[list[KGNode], list[KGEdge]]:
    """
    Toma lo que devolvió el modelo (sin provenance) y le adosa provenance desde
    el contexto del chunk de origen.

    El modelo NO emite provenance (decisión 3.7 de schema.md): el pipeline la
    inyecta usando el (source_doc, location) que el chunker ya conoce. Eso evita
    alucinaciones de ubicación, ahorra tokens de salida y mantiene la
    trazabilidad 100% determinística.
    """
    prov = Provenance(source_doc=chunk.source_doc, location=chunk.location)
    nodes = [
        KGNode(
            id=e.id,
            type=e.type,
            label=e.label,
            properties=e.properties,
            provenance=prov,  # ← inyectada acá, no viene del modelo
        )
        for e in extraction.entities
    ]
    edges = [
        KGEdge(
            source=r.source,
            target=r.target,
            relation=r.predicate,
            provenance=prov,  # ← inyectada acá, no viene del modelo
        )
        for r in extraction.relations
    ]
    return nodes, edges


# ============================================================================


# ---------- Cache ----------


def cache_path(chunk_id: str) -> Path:
    return CACHE_DIR / f"{chunk_id}.json"


def load_cached(chunk_id: str) -> dict[str, Any] | None:
    p = cache_path(chunk_id)
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None
    # Lección Run 2 #5: no consideramos válida una entrada con error.
    if data.get("error"):
        return None
    return data


def save_cached(chunk_id: str, payload: dict[str, Any]) -> None:
    cache_path(chunk_id).write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )


# ---------- Llamada al modelo ----------


class ProgressTracker:
    """Logging por chunk (lección Run 2 #3): cada LOG_EVERY chunks imprime
    estado con flush=True. También trackea 429s y fails individualmente."""

    def __init__(self, total: int, already_done: int):
        self.total = total
        self.done = already_done
        self.failed = 0
        self.throttled = 0
        self.cost_in_usd = 0.0
        self.cost_out_usd = 0.0
        self.recent_times: deque[float] = deque(maxlen=LOG_EVERY)
        self.t0 = time.time()
        self._last_log_done = already_done
        print(
            f"[start] total={total}  cached={already_done}  pending={total - already_done}",
            flush=True,
        )

    @property
    def cost_total(self) -> float:
        return self.cost_in_usd + self.cost_out_usd

    def on_429(self, chunk_id: str, attempt: int, sleep_s: float) -> None:
        self.throttled += 1
        print(
            f"  [429] {chunk_id}  attempt={attempt}  sleep={sleep_s:.1f}s",
            flush=True,
        )

    def on_fail(self, chunk_id: str, err: str) -> None:
        self.failed += 1
        print(f"  [FAIL] {chunk_id}  err={err[:200]}", flush=True)

    def on_done(
        self, chunk_id: str, in_tok: int, out_tok: int, cached: bool
    ) -> None:
        self.done += 1
        self.recent_times.append(time.time())
        if not cached:
            self.cost_in_usd += in_tok * PRICE_IN_USD_PER_MTOK / 1_000_000
            self.cost_out_usd += out_tok * PRICE_OUT_USD_PER_MTOK / 1_000_000

        if self.done - self._last_log_done >= LOG_EVERY:
            self._log()
            self._last_log_done = self.done

    def _log(self) -> None:
        elapsed = time.time() - self.t0
        rate = 0.0
        if len(self.recent_times) >= 2:
            window_s = self.recent_times[-1] - self.recent_times[0]
            if window_s > 0:
                rate = (len(self.recent_times) - 1) / window_s * 60
        pct = 100 * self.done / max(1, self.total)
        remaining = self.total - self.done
        eta_min = remaining / rate if rate > 0 else float("inf")
        print(
            f"[{self.done}/{self.total}  {pct:.1f}%]  "
            f"cost=${self.cost_total:.3f}  "
            f"rate={rate:.1f}/min  "
            f"429s={self.throttled}  fails={self.failed}  "
            f"eta={eta_min:.0f}min  elapsed={elapsed/60:.1f}min",
            flush=True,
        )

    def final(self) -> None:
        elapsed = time.time() - self.t0
        print(
            f"\n[done] {self.done}/{self.total}  "
            f"cost=${self.cost_total:.4f}  "
            f"(in=${self.cost_in_usd:.4f}  out=${self.cost_out_usd:.4f})  "
            f"429s={self.throttled}  fails={self.failed}  "
            f"elapsed={elapsed/60:.1f}min",
            flush=True,
        )


async def call_model(
    client: AsyncAnthropic, chunk: Chunk, tracker: ProgressTracker
) -> dict[str, Any]:
    """Llama a Haiku con reintentos. Devuelve el dict cacheado (con tokens)."""
    user_prompt = USER_PROMPT_TEMPLATE.format(
        source_doc=chunk.source_doc,
        location=chunk.location,
        chunk_text=chunk.text,
    )
    last_err: str | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = await client.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_prompt}],
            )
            raw_text = "".join(
                getattr(b, "text", "") for b in resp.content if getattr(b, "type", "") == "text"
            )
            in_tok = resp.usage.input_tokens
            out_tok = resp.usage.output_tokens
            return {
                "chunk_id": chunk.chunk_id,
                "source_doc": chunk.source_doc,
                "location": chunk.location,
                "raw_output": raw_text,
                "input_tokens": in_tok,
                "output_tokens": out_tok,
                "attempt": attempt,
                "error": None,
            }
        except APIStatusError as e:
            last_err = f"APIStatusError {e.status_code}: {str(e)[:300]}"
            if e.status_code == 429 and attempt < MAX_RETRIES:
                sleep_s = RETRY_BASE**attempt
                tracker.on_429(chunk.chunk_id, attempt, sleep_s)
                await asyncio.sleep(sleep_s)
                continue
            break
        except Exception as e:  # noqa: BLE001
            last_err = f"{type(e).__name__}: {str(e)[:300]}"
            if attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_BASE**attempt)
                continue
            break

    return {
        "chunk_id": chunk.chunk_id,
        "source_doc": chunk.source_doc,
        "location": chunk.location,
        "raw_output": None,
        "input_tokens": 0,
        "output_tokens": 0,
        "attempt": MAX_RETRIES,
        "error": last_err or "unknown",
    }


async def process_chunk(
    client: AsyncAnthropic,
    chunk: Chunk,
    sem: asyncio.Semaphore,
    tracker: ProgressTracker,
) -> None:
    cached = load_cached(chunk.chunk_id)
    if cached is not None:
        tracker.on_done(chunk.chunk_id, 0, 0, cached=True)
        return

    async with sem:
        result = await call_model(client, chunk, tracker)

    if result["error"]:
        # NO cacheamos errores (lección Run 2 #5) → reintenta en próximo run.
        tracker.on_fail(chunk.chunk_id, result["error"])
        return

    # Validamos parsing y schema acá para no propagar basura. Pero igual cacheamos
    # el raw_output crudo (lo que devolvió el modelo) y el resultado validado.
    raw = result["raw_output"] or ""
    try:
        parsed = _parse_json_strict(raw)
        extraction = ChunkExtraction.model_validate(parsed)
        result["parsed_ok"] = True
        result["entities_count"] = len(extraction.entities)
        result["relations_count"] = len(extraction.relations)
        result["parsed"] = extraction.model_dump()
    except (ValueError, ValidationError, json.JSONDecodeError) as e:
        # Lo guardamos con flag, pero NO como error (raw está, se puede recuperar después).
        result["parsed_ok"] = False
        result["parse_error"] = f"{type(e).__name__}: {str(e)[:300]}"
        result["entities_count"] = 0
        result["relations_count"] = 0
        result["parsed"] = None

    save_cached(chunk.chunk_id, result)
    tracker.on_done(
        chunk.chunk_id, result["input_tokens"], result["output_tokens"], cached=False
    )


def _load_local_dotenv() -> None:
    """
    Loader minimal de .env en el mismo directorio del script. Solo soporta líneas
    KEY=value (sin export, sin comillas obligatorias, sin interpolación). Respeta
    valores no-vacíos preexistentes en el entorno, pero sobreescribe cadenas
    vacías (el harness exporta ANTHROPIC_API_KEY="" por defecto).
    """
    env_path = Path(__file__).resolve().parent / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if not key:
            continue
        existing = os.environ.get(key, "")
        if not existing:  # unset o vacío → cargar del .env
            os.environ[key] = value


async def run_extraction(chunks: list[Chunk]) -> None:
    _load_local_dotenv()
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY no está seteada en el entorno", file=sys.stderr)
        sys.exit(2)

    already_done = sum(1 for c in chunks if load_cached(c.chunk_id) is not None)
    tracker = ProgressTracker(total=len(chunks), already_done=already_done)
    sem = asyncio.Semaphore(CONCURRENCY)

    client = AsyncAnthropic(api_key=api_key)
    tasks = [process_chunk(client, c, sem, tracker) for c in chunks]
    await asyncio.gather(*tasks)
    tracker.final()


# ---------- CLI ----------


def collect_chunks(pdfs: list[Path]) -> list[Chunk]:
    all_chunks: list[Chunk] = []
    for pdf in pdfs:
        cs = chunk_pdf(pdf)
        print(f"  {pdf.name}: {len(cs)} chunks", flush=True)
        all_chunks.extend(cs)
    return all_chunks


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--mode",
        choices=["smoke", "full", "chunks-only"],
        required=True,
        help="smoke=1 TO chico; full=5 TOs; chunks-only=solo reporta chunking sin llamar API",
    )
    args = ap.parse_args()

    if args.mode == "smoke":
        pdfs = [SUBSET_DIR / "TO_proteccion_usuarios_servicios_financieros_actual.pdf"]
    else:
        pdfs = sorted(SUBSET_DIR.glob("TO_*.pdf"))

    print(f"[chunking] {len(pdfs)} PDFs", flush=True)
    chunks = collect_chunks(pdfs)
    print(f"[chunking] total chunks: {len(chunks)}", flush=True)

    if args.mode == "chunks-only":
        sizes = sorted(len(c.text) for c in chunks)
        if sizes:
            print(
                f"[chunking] size_chars: min={sizes[0]}  median={sizes[len(sizes)//2]}  max={sizes[-1]}",
                flush=True,
            )
        return

    asyncio.run(run_extraction(chunks))


if __name__ == "__main__":
    main()
