"""
Extracción de tripletas con Claude Haiku 4.5.

Estrategia: schema-light puro. SYSTEM_PROMPT no impone tipos ni predicados.

Características:
- Concurrency 3 (lección 3 del Run 1).
- Pydantic strict con `relations` default_factory=list (lección 4 del Run 1).
- Cache por chunk en code/cache/extract/. Idempotente: si existe, no reprocesa.
- Distingue:
    * Empty outputs (entities=[] y relations=[]) → contador empty_outputs.
      NO va a _failures.jsonl. Es señal del corpus.
    * Pydantic fails (output que no parsea) → _failures.jsonl. Skip chunk.
      NO inventamos fallback estructurado.
- Logging por chunk con flush=True (lección 3 del Run 2 del Cookbook).
- Backoff conservador: 3 reintentos, base 2.0, máx ~14s por chunk (lección 4 Run 2).

Modelo: claude-haiku-4-5 (alias estable; ver Anthropic docs).
"""

import asyncio
import json
import os
import random
import sys
import time
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field, ValidationError
from anthropic import AsyncAnthropic, APIStatusError, APIError
from dotenv import load_dotenv

# Cargar .env local de la carpeta code/. La key vive ahí (copiada por la autora).
load_dotenv(Path(__file__).resolve().parent / ".env", override=True)

from system_prompt import SYSTEM_PROMPT

# --- Configuración ---
MODEL = "claude-haiku-4-5"
MAX_TOKENS_OUT = 16384  # Haiku 4.5 soporta hasta 64K. 16K es seguro y deja margen para chunks densos.
CONCURRENCY = 3
MAX_RETRIES = 3
BACKOFF_BASE = 2.0
TEMPERATURE = 0.0  # determinismo para reproducibilidad

CHUNKS_DIR = Path(__file__).resolve().parent / "cache" / "chunks"
EXTRACT_DIR = Path(__file__).resolve().parent / "cache" / "extract"
EXTRACT_DIR.mkdir(parents=True, exist_ok=True)
FAILURES_PATH = EXTRACT_DIR / "_failures.jsonl"


# --- Pydantic schemas ---

class Entity(BaseModel):
    name: str
    type: str
    description: str = ""
    location_hint: str = ""

    class Config:
        extra = "forbid"


class Relation(BaseModel):
    source: str
    target: str
    predicate: str
    location_hint: str = ""

    class Config:
        extra = "forbid"


class Extraction(BaseModel):
    entities: list[Entity]
    relations: list[Relation] = Field(default_factory=list)

    class Config:
        extra = "forbid"


# --- Cliente ---
client = AsyncAnthropic()  # usa ANTHROPIC_API_KEY del env


# --- Utilidades ---

def chunk_cache_path(source_pdf: str, chunk_id: str) -> Path:
    base = source_pdf.replace(".pdf", "")
    return EXTRACT_DIR / f"{base}__{chunk_id}.json"


def already_extracted(source_pdf: str, chunk_id: str) -> bool:
    p = chunk_cache_path(source_pdf, chunk_id)
    if not p.exists():
        return False
    # Cacheamos sólo respuestas exitosas (sin error). Run 2 lesson 5.
    try:
        data = json.loads(p.read_text())
        return data.get("error") is None and data.get("status") in ("ok", "empty")
    except Exception:
        return False


def append_failure(record: dict) -> None:
    with FAILURES_PATH.open("a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def strip_code_fences(text: str) -> str:
    """
    Devuelve solo el JSON limpio. Tolera:
    - Texto antes y/o después del ``` (el modelo a veces agrega justificaciones).
    - Code fence opcional con language tag (```json).
    - Sin code fence (parse directo del input strip).
    Estrategia: si hay un ``` en cualquier lado, tomo el contenido del PRIMER bloque
    delimitado por ```. Si no hay code fence, devuelvo el texto strip.
    """
    t = text.strip()
    if "```" in t:
        # encontrar el primer ``` y el siguiente ``` después
        first = t.find("```")
        # avanzar más allá de ``` y de la posible language tag en la misma línea
        after_first = t.find("\n", first)
        if after_first == -1:
            # extraño: ``` sin newline después; fallback al strip simple
            return t.replace("```json", "").replace("```", "").strip()
        body_start = after_first + 1
        second = t.find("```", body_start)
        if second == -1:
            # no se cerró; tomar hasta el final
            return t[body_start:].strip()
        return t[body_start:second].strip()
    return t


# --- Llamada con retries ---

async def _call_haiku(user_message: str) -> tuple[str, dict]:
    """
    Llama Haiku con backoff exponencial.
    Devuelve (text, usage_dict).
    Levanta excepción si todos los retries fallan.
    """
    last_exc: Optional[BaseException] = None
    for attempt in range(MAX_RETRIES):
        try:
            resp = await client.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS_OUT,
                temperature=TEMPERATURE,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_message}],
            )
            text_blocks = [b.text for b in resp.content if hasattr(b, "text")]
            text = "".join(text_blocks)
            usage = {
                "input_tokens": getattr(resp.usage, "input_tokens", 0),
                "output_tokens": getattr(resp.usage, "output_tokens", 0),
            }
            return text, usage
        except APIStatusError as e:
            last_exc = e
            # 429, 529 → retry con backoff
            if e.status_code in (429, 529, 500, 502, 503, 504):
                sleep_s = (BACKOFF_BASE ** attempt) + random.uniform(0, 0.5)
                print(f"  [retry] {e.status_code} attempt {attempt+1}/{MAX_RETRIES}, sleeping {sleep_s:.1f}s", flush=True)
                await asyncio.sleep(sleep_s)
                continue
            raise
        except APIError as e:
            last_exc = e
            sleep_s = (BACKOFF_BASE ** attempt) + random.uniform(0, 0.5)
            print(f"  [retry] APIError attempt {attempt+1}/{MAX_RETRIES}, sleeping {sleep_s:.1f}s: {e}", flush=True)
            await asyncio.sleep(sleep_s)
    assert last_exc is not None
    raise last_exc


# --- Extracción por chunk ---

def build_user_message(chunk: dict, source_pdf: str) -> str:
    page_range = f"p.{chunk['page_start']}" if chunk["page_start"] == chunk["page_end"] else f"p.{chunk['page_start']}-{chunk['page_end']}"
    return (
        f"[TO: {source_pdf}, {page_range}]\n\n"
        f"{chunk['text']}"
    )


async def extract_one(chunk: dict, source_pdf: str, sem: asyncio.Semaphore, progress: dict) -> dict:
    chunk_id = chunk["chunk_id"]
    out_path = chunk_cache_path(source_pdf, chunk_id)

    if already_extracted(source_pdf, chunk_id):
        progress["cached"] += 1
        return {"status": "cached"}

    async with sem:
        user_msg = build_user_message(chunk, source_pdf)
        try:
            text, usage = await _call_haiku(user_msg)
        except Exception as e:
            err = {"chunk_id": chunk_id, "source_pdf": source_pdf, "error_kind": "api_error", "error": str(e)}
            append_failure(err)
            progress["failed_api"] += 1
            print(f"  [FAIL api] {source_pdf} {chunk_id}: {e}", flush=True)
            return {"status": "api_fail", "error": str(e)}

        # Parseo
        clean = strip_code_fences(text)
        try:
            raw_obj = json.loads(clean)
        except json.JSONDecodeError as e:
            err = {
                "chunk_id": chunk_id,
                "source_pdf": source_pdf,
                "error_kind": "json_decode",
                "error": str(e),
                "raw_output": text[:4000],
            }
            append_failure(err)
            progress["failed_parse"] += 1
            print(f"  [FAIL parse] {source_pdf} {chunk_id}: {e}", flush=True)
            return {"status": "parse_fail", "error": str(e)}

        # Validación Pydantic
        try:
            extraction = Extraction.model_validate(raw_obj)
        except ValidationError as e:
            err = {
                "chunk_id": chunk_id,
                "source_pdf": source_pdf,
                "error_kind": "pydantic",
                "error": str(e),
                "raw_output": text[:4000],
            }
            append_failure(err)
            progress["failed_pydantic"] += 1
            print(f"  [FAIL pydantic] {source_pdf} {chunk_id}: {len(e.errors())} errors", flush=True)
            return {"status": "pydantic_fail", "error": str(e)}

        # Éxito — distinguir empty vs ok
        is_empty = len(extraction.entities) == 0 and len(extraction.relations) == 0
        status = "empty" if is_empty else "ok"
        if is_empty:
            progress["empty"] += 1
        else:
            progress["ok"] += 1
            progress["n_entities"] += len(extraction.entities)
            progress["n_relations"] += len(extraction.relations)

        # Persistir
        payload = {
            "status": status,
            "source_pdf": source_pdf,
            "chunk_id": chunk_id,
            "page_start": chunk["page_start"],
            "page_end": chunk["page_end"],
            "entities": [e.model_dump() for e in extraction.entities],
            "relations": [r.model_dump() for r in extraction.relations],
            "usage": usage,
            "error": None,
        }
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

        progress["input_tokens"] += usage["input_tokens"]
        progress["output_tokens"] += usage["output_tokens"]

        # Log cada 5 chunks
        progress["done"] += 1
        if progress["done"] % 5 == 0 or progress["done"] == progress["total"]:
            elapsed = time.time() - progress["t0"]
            rate = progress["done"] / elapsed if elapsed > 0 else 0
            # Haiku 4.5 pricing: $1/MTok in, $5/MTok out (Oct-2025 según docs)
            cost = progress["input_tokens"] * 1.0 / 1e6 + progress["output_tokens"] * 5.0 / 1e6
            eta_s = (progress["total"] - progress["done"]) / rate if rate > 0 else float("inf")
            print(
                f"[progress] {progress['done']}/{progress['total']} "
                f"({100*progress['done']/progress['total']:.1f}%) | "
                f"ok={progress['ok']} empty={progress['empty']} fails={progress['failed_api']+progress['failed_parse']+progress['failed_pydantic']} | "
                f"in={progress['input_tokens']} out={progress['output_tokens']} | "
                f"~${cost:.3f} | rate {rate*60:.1f}/min | ETA {eta_s/60:.1f}min",
                flush=True,
            )

        return {"status": status}


# --- Driver ---

async def run_pdf(source_pdf: str, limit: Optional[int] = None) -> dict:
    chunks_file = CHUNKS_DIR / f"{source_pdf.replace('.pdf', '')}.json"
    if not chunks_file.exists():
        raise FileNotFoundError(f"No chunks file: {chunks_file}. Run chunk.py first.")
    data = json.loads(chunks_file.read_text())
    chunks = data["chunks"]
    if limit:
        chunks = chunks[:limit]

    progress = {
        "total": len(chunks),
        "done": 0,
        "cached": 0,
        "ok": 0,
        "empty": 0,
        "failed_api": 0,
        "failed_parse": 0,
        "failed_pydantic": 0,
        "n_entities": 0,
        "n_relations": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "t0": time.time(),
    }

    # Pre-cuenta cacheados
    for c in chunks:
        if already_extracted(source_pdf, c["chunk_id"]):
            progress["cached"] += 1

    print(f"[run] {source_pdf}: {len(chunks)} chunks total, {progress['cached']} cached", flush=True)
    progress["total"] = len(chunks) - progress["cached"]  # solo los que realmente vamos a procesar
    if progress["total"] == 0:
        print(f"[run] {source_pdf}: nothing to do, all cached.", flush=True)

    sem = asyncio.Semaphore(CONCURRENCY)
    tasks = [extract_one(c, source_pdf, sem, progress) for c in chunks]
    await asyncio.gather(*tasks)

    elapsed = time.time() - progress["t0"]
    cost = progress["input_tokens"] * 1.0 / 1e6 + progress["output_tokens"] * 5.0 / 1e6
    print(
        f"[done] {source_pdf}: ok={progress['ok']} empty={progress['empty']} "
        f"fails={progress['failed_api']+progress['failed_parse']+progress['failed_pydantic']} | "
        f"entities={progress['n_entities']} relations={progress['n_relations']} | "
        f"tokens in/out {progress['input_tokens']}/{progress['output_tokens']} | "
        f"cost ~${cost:.3f} | wall {elapsed/60:.1f}min",
        flush=True,
    )
    return progress


def main():
    if len(sys.argv) < 2:
        print("Uso: python extract.py <source_pdf.pdf> [limit]", file=sys.stderr)
        sys.exit(2)
    source_pdf = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else None
    asyncio.run(run_pdf(source_pdf, limit=limit))


if __name__ == "__main__":
    main()
