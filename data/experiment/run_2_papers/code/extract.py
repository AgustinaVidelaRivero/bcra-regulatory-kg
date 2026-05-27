"""
extract.py — Extracción schema-aware de tripletas con Claude Haiku 4.5.

Carga:
- El vocabulario controlado de schema.py.
- Renderiza el SYSTEM_PROMPT incluyendo los 12 tipos y los 23 predicados
  con dominio/rango.
- Llama a la API con concurrency configurable (default 3) para evitar 429.
- Cachea cada respuesta cruda en code/cache/<doc_id>/raw/<chunk_id>.json
  con el modelo, los tokens consumidos y el output JSON parseado.

NO valida acá (eso es validate.py). NO ensambla (eso es assemble.py).
"""

from __future__ import annotations

import asyncio
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import anthropic
from anthropic import APIStatusError, APITimeoutError

from schema import (
    DEFAULT_VERSION,
    DEONTIC_MODALITIES,
    ENTITY_TYPES,
    PREDICATE_NAMES,
    render_entity_types_for_prompt,
    render_predicates_for_prompt,
)


MODEL = "claude-haiku-4-5"
MAX_TOKENS_OUTPUT = 4000
# FIX 3 — concurrency más conservadora: baja presión sobre TPM/output TPM.
DEFAULT_CONCURRENCY = 2
# FIX 2 — backoff menos agresivo: 3 reintentos con base 2.0 → 2s, 4s, 8s = 14s máx por chunk.
# (Antes: 5 con base 4.0 → 4s, 8s, 16s, 32s, 64s = 124s máx por chunk — atascaba el throughput.)
MAX_RETRIES_TRANSIENT = 3
RETRY_BACKOFF_BASE = 2.0


SYSTEM_PROMPT = f"""Sos un extractor de conocimiento regulatorio para el Banco Central de la República Argentina (BCRA). \
Tu trabajo es leer un fragmento de un Texto Ordenado del BCRA y extraer un GRAFO de \
conocimiento estructurado siguiendo un VOCABULARIO CONTROLADO ESTRICTO. \
No inventes tipos ni predicados fuera del vocabulario.

==============================================================================
TIPOS DE ENTIDAD PERMITIDOS (12 — son los ÚNICOS que podés usar)
==============================================================================

{render_entity_types_for_prompt()}

==============================================================================
PREDICADOS PERMITIDOS (23 — son los ÚNICOS que podés usar)
==============================================================================

Para cada predicado se indica DOMINIO (tipos de entidad válidos como sujeto) \
y RANGO (tipos de entidad válidos como objeto). Si una relación no encaja en \
ningún predicado o viola el dominio/rango, DESCARTALA — no inventes uno nuevo.

{render_predicates_for_prompt()}

==============================================================================
ERRORES FRECUENTES QUE NO QUIERO VER (basados en pasadas anteriores)
==============================================================================

INCORRECTO: SujetoRegulado --aplica_a--> Obligacion
CORRECTO:   SujetoRegulado --obligado_a--> Obligacion
  (`aplica_a` siempre tiene a Obligacion como SUJETO, no como objeto.)

INCORRECTO: Obligacion --condicion_de_aplicabilidad--> Requisito
CORRECTO:   Requisito --condicion_de_aplicabilidad--> Obligacion
  (La dirección es: el requisito CONDICIONA a la obligación.)

INCORRECTO: ConceptoDefinido --aplica_a--> ConceptoDefinido (entre dos conceptos)
CORRECTO:   ConceptoDefinido --usa_concepto--> ConceptoDefinido
  (Entre conceptos se usa `usa_concepto`, NO `aplica_a`.)

INCORRECTO: Obligacion --usa_concepto--> Obligacion (entre dos obligaciones)
CORRECTO:   Obligacion --excepcion_a--> Obligacion  (si es excepción)
  o reformular como dos tripletas separadas con un concepto intermedio.

INCORRECTO: Sancion --aplica_a--> SujetoRegulado
CORRECTO:   Sancion --recae_sobre--> SujetoRegulado
  (Para sanciones que recaen sobre un sujeto, usá `recae_sobre`.)

Si una tripleta no encaja en ningún predicado del vocabulario, DESCARTALA. \
NO inventes predicados nuevos. NO fuerces dominios/rangos.

==============================================================================
REGLAS DE MODELADO (NO NEGOCIABLES)
==============================================================================

1. PROHIBIDO modelar la JERARQUÍA DOCUMENTAL como nodos. \
   "Punto 3.16.3.4", "Sección 1", "Capítulo III", "Anexo I" NO son nodos. \
   Esa información va en provenance (no la pongas como entidad, no la incluyas \
   como label, no la metas como tipo). Tampoco pongas referencias \
   a la jerarquía documental DENTRO del label de un nodo regulatorio. \
   MAL: "sujeto obligado del punto 3.2.1.1". BIEN: "sujeto obligado". \
   (Si la distinción importa, va en `properties.description`, NUNCA en `label`.)

2. Si extraés una `Obligacion`, asigná `properties.modalidad` con uno de: \
   {sorted(DEONTIC_MODALITIES)}. Default: "obligacion" si no está claro.

3. Las entidades deben ser CONCEPTOS REGULATORIOS REALES extraídos del texto, \
   NO categorías documentales ni metadatos. Bien: "entidad financiera", "préstamo \
   hipotecario", "30 días corridos". Mal: "punto 3.4", "el presente texto ordenado", \
   "sección de definiciones".

4. NO uses comillas dentro de los labels. Mantené los labels concisos (≤ 80 chars), \
   en minúsculas excepto siglas/nombres propios, sin numeración documental.

5. Los IDs los asigno yo después (vos podés usar IDs locales de tu invención dentro \
   del chunk; solo importa que sean únicos dentro de tu respuesta para conectar \
   entities con relations).

==============================================================================
FORMATO DE SALIDA — devolvé EXACTAMENTE este JSON, sin texto antes ni después
==============================================================================

{{
  "entities": [
    {{
      "local_id": "<id local único en este chunk>",
      "type": "<uno de los 12 tipos permitidos>",
      "label": "<etiqueta legible, ≤ 80 chars>",
      "properties": {{
        "description": "<1-2 oraciones grounded en el texto>",
        "modalidad": "<solo si type==Obligacion>",
        "valor": "<solo si type==Umbral>",
        "unidad": "<solo si type==Umbral o type==Plazo>",
        "duracion": "<solo si type==Plazo>"
      }}
    }}
  ],
  "relations": [
    {{
      "source": "<local_id de una entity de este chunk>",
      "target": "<local_id de otra entity de este chunk>",
      "relation": "<uno de los 23 predicados permitidos>"
    }}
  ]
}}

Si el fragmento NO contiene contenido regulatorio extraíble (encabezados sueltos, \
índice, página en blanco), devolvé `{{"entities": [], "relations": []}}`.

EXTRAÉ con criterio: priorizá tripletas de alta confianza grounded en el texto. \
Mejor poco y correcto que mucho y ruidoso.
"""


def build_reflection_prompt(chunk_text: str, previous_output: dict, violations: list[str]) -> str:
    """Prompt para el retry (estilo FinReflectKG). El SYSTEM_PROMPT se reusa."""
    vio_txt = "\n".join(f"- {v}" for v in violations)
    prev_txt = json.dumps(previous_output, ensure_ascii=False, indent=2)
    return f"""Tu extracción anterior tuvo VIOLACIONES estructurales que debés corregir.

===== TEXTO ORIGINAL DEL FRAGMENTO =====
{chunk_text}

===== TU EXTRACCIÓN ANTERIOR (cruda) =====
{prev_txt}

===== VIOLACIONES DETECTADAS =====
{vio_txt}

===== INSTRUCCIONES DE CORRECCIÓN =====
Reextraé el grafo del fragmento corrigiendo las violaciones. \
Si una tripleta no encaja en NINGÚN predicado del vocabulario, descartala. \
Si una entidad parece referirse a la jerarquía documental, descartala (esa \
información va en provenance, fuera del grafo). Si no podés corregir alguna \
violación sin perder fidelidad al texto, preferí DESCARTAR la tripleta a \
violar dominio/rango.

Devolvé el JSON corregido con EXACTAMENTE el mismo formato de salida que el \
SYSTEM_PROMPT pidió. Sin texto antes ni después.
"""


def build_user_prompt(chunk_text: str, source_doc: str, location: str) -> str:
    return f"""Fragmento de `{source_doc}` ({location}):

\"\"\"
{chunk_text}
\"\"\"

Extraé entidades y relaciones siguiendo el vocabulario controlado del SYSTEM_PROMPT. \
Devolvé SOLO el JSON especificado."""


JSON_OBJECT_RE = re.compile(r"\{.*\}", re.DOTALL)


def _parse_json_response(text: str) -> dict:
    """Tolera prefijos/sufijos del LLM. Lanza ValueError si no parsea."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.IGNORECASE)
        text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = JSON_OBJECT_RE.search(text)
        if not m:
            raise ValueError(f"No JSON object found in response: {text[:200]}")
        return json.loads(m.group(0))


@dataclass
class ExtractionResult:
    chunk_id: str
    source_doc: str
    location: str
    raw_output: dict      # {"entities": [...], "relations": [...]} crudo del LLM
    input_tokens: int
    output_tokens: int
    model: str
    pass_kind: str        # "extract" | "reflect"
    error: Optional[str] = None

    def cost_usd(self) -> float:
        # Pricing Haiku 4.5: $1 / MTok input, $5 / MTok output (refs públicas).
        return self.input_tokens * 1e-6 + self.output_tokens * 5e-6

    def to_dict(self) -> dict:
        return {
            "chunk_id": self.chunk_id,
            "source_doc": self.source_doc,
            "location": self.location,
            "raw_output": self.raw_output,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "model": self.model,
            "pass_kind": self.pass_kind,
            "error": self.error,
        }


async def _call_with_backoff(client, tracker=None, chunk_id="?", **kwargs):
    """Maneja 429 / timeouts con backoff exponencial.

    FIX 2: backoff acotado a 3 reintentos. Si agota, levanta RuntimeError que
    el caller convierte en 'fallo definitivo' (no bloquea el pipeline).
    Loggea cada 429 inmediatamente al stdout (vía tracker) para visibilidad.
    """
    last_exc = None
    for attempt in range(MAX_RETRIES_TRANSIENT):
        try:
            return await client.messages.create(**kwargs)
        except APIStatusError as e:
            last_exc = e
            if e.status_code in (429, 529, 503):
                wait = RETRY_BACKOFF_BASE * (2 ** attempt)
                if tracker is not None:
                    await tracker.note_throttle(e.status_code, chunk_id, attempt, wait)
                await asyncio.sleep(wait)
                continue
            raise
        except APITimeoutError as e:
            last_exc = e
            wait = RETRY_BACKOFF_BASE * (2 ** attempt)
            if tracker is not None:
                await tracker.note_throttle("timeout", chunk_id, attempt, wait)
            await asyncio.sleep(wait)
    raise RuntimeError(f"Exhausted transient retries ({MAX_RETRIES_TRANSIENT}): {last_exc}")


class ProgressTracker:
    """
    FIX 1 — Tracker de progreso compartido para extract+retry passes.
    Imprime stdout cada `print_every` chunks completos con:
      - completed/total + %
      - costo acumulado USD
      - rate (chunks/min) sobre los últimos 5
      - errors (fallos definitivos) y 429s acumulados
      - ETA
    Loggea cada 429/timeout inmediatamente cuando ocurre.
    """

    def __init__(self, total_expected: int, label: str = "extract", print_every: int = 5):
        self.total = max(total_expected, 1)
        self.label = label
        self.completed = 0
        self.errors_definitive = 0
        self.rate429 = 0
        self.cost_so_far = 0.0
        self.in_tok = 0
        self.out_tok = 0
        self.start_ts = time.time()
        self.lock = asyncio.Lock()
        self.recent_ts: list[float] = []
        self.print_every = print_every

    async def note_throttle(self, code, chunk_id: str, attempt: int, wait: float):
        async with self.lock:
            self.rate429 += 1
            print(
                f"[{self.label}] ⚠️  THROTTLE code={code} on {chunk_id} "
                f"(attempt {attempt + 1}/{MAX_RETRIES_TRANSIENT}, backoff {wait:.1f}s) "
                f"| total 429+timeouts so far: {self.rate429}",
                flush=True,
            )

    async def note_definitive_failure(self, chunk_id: str, err: str):
        async with self.lock:
            self.errors_definitive += 1
            print(
                f"[{self.label}] ❌ DEFINITIVE FAIL on {chunk_id}: {err} "
                f"(total fails: {self.errors_definitive})",
                flush=True,
            )

    async def update(self, result: "ExtractionResult"):
        async with self.lock:
            self.completed += 1
            self.cost_so_far += result.cost_usd()
            self.in_tok += result.input_tokens
            self.out_tok += result.output_tokens
            now = time.time()
            self.recent_ts.append(now)
            if len(self.recent_ts) > 5:
                self.recent_ts = self.recent_ts[-5:]
            if self.completed % self.print_every == 0 or self.completed == self.total:
                self._print_status_locked()

    def _print_status_locked(self):
        now = time.time()
        elapsed = now - self.start_ts
        if len(self.recent_ts) >= 2:
            window = self.recent_ts[-1] - self.recent_ts[0]
            recent_rate = (len(self.recent_ts) - 1) / window * 60 if window > 1e-3 else 0.0
        else:
            recent_rate = self.completed / elapsed * 60 if elapsed > 0 else 0.0
        remaining = self.total - self.completed
        eta_s = remaining / (recent_rate / 60) if recent_rate > 0 else float("inf")
        eta_str = f"{eta_s/60:.1f}min" if eta_s != float("inf") else "?"
        print(
            f"[{self.label}] {self.completed}/{self.total} ({100*self.completed/self.total:.1f}%) "
            f"| ${self.cost_so_far:.3f} "
            f"| rate {recent_rate:.1f} chunks/min (last 5) "
            f"| 429s {self.rate429} | fails {self.errors_definitive} "
            f"| ETA {eta_str}",
            flush=True,
        )

    def summary(self) -> dict:
        elapsed = time.time() - self.start_ts
        return {
            "label": self.label,
            "completed": self.completed,
            "total_expected": self.total,
            "elapsed_seconds": round(elapsed, 1),
            "cost_usd": round(self.cost_so_far, 4),
            "input_tokens": self.in_tok,
            "output_tokens": self.out_tok,
            "rate_chunks_per_min_avg": round(self.completed / (elapsed / 60), 1) if elapsed > 0 else 0,
            "throttle_events": self.rate429,
            "definitive_failures": self.errors_definitive,
        }


async def extract_chunk(client, chunk, semaphore, tracker: Optional["ProgressTracker"] = None) -> ExtractionResult:
    async with semaphore:
        user_msg = build_user_prompt(chunk.text, chunk.source_doc, chunk.location)
        try:
            resp = await _call_with_backoff(
                client,
                tracker=tracker,
                chunk_id=chunk.chunk_id,
                model=MODEL,
                max_tokens=MAX_TOKENS_OUTPUT,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_msg}],
            )
            text = "".join(b.text for b in resp.content if b.type == "text")
            try:
                parsed = _parse_json_response(text)
                err = None
            except Exception as e:
                parsed = {"entities": [], "relations": []}
                err = f"JSON parse error: {e}"
            return ExtractionResult(
                chunk_id=chunk.chunk_id,
                source_doc=chunk.source_doc,
                location=chunk.location,
                raw_output=parsed,
                input_tokens=resp.usage.input_tokens,
                output_tokens=resp.usage.output_tokens,
                model=MODEL,
                pass_kind="extract",
                error=err,
            )
        except Exception as e:
            err = f"API error: {e}"
            if tracker is not None:
                await tracker.note_definitive_failure(chunk.chunk_id, str(e)[:120])
            return ExtractionResult(
                chunk_id=chunk.chunk_id,
                source_doc=chunk.source_doc,
                location=chunk.location,
                raw_output={"entities": [], "relations": []},
                input_tokens=0,
                output_tokens=0,
                model=MODEL,
                pass_kind="extract",
                error=err,
            )


async def reflect_chunk(client, chunk, previous: ExtractionResult, violations: list[str],
                        semaphore, tracker: Optional["ProgressTracker"] = None) -> ExtractionResult:
    async with semaphore:
        reflect_msg = build_reflection_prompt(chunk.text, previous.raw_output, violations)
        try:
            resp = await _call_with_backoff(
                client,
                tracker=tracker,
                chunk_id=chunk.chunk_id + ":retry",
                model=MODEL,
                max_tokens=MAX_TOKENS_OUTPUT,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": reflect_msg}],
            )
            text = "".join(b.text for b in resp.content if b.type == "text")
            try:
                parsed = _parse_json_response(text)
                err = None
            except Exception as e:
                parsed = previous.raw_output  # fallback al anterior
                err = f"JSON parse error on retry: {e}"
            return ExtractionResult(
                chunk_id=chunk.chunk_id,
                source_doc=chunk.source_doc,
                location=chunk.location,
                raw_output=parsed,
                input_tokens=resp.usage.input_tokens,
                output_tokens=resp.usage.output_tokens,
                model=MODEL,
                pass_kind="reflect",
                error=err,
            )
        except Exception as e:
            err = f"API error on retry: {e}"
            if tracker is not None:
                await tracker.note_definitive_failure(chunk.chunk_id + ":retry", str(e)[:120])
            return ExtractionResult(
                chunk_id=chunk.chunk_id,
                source_doc=chunk.source_doc,
                location=chunk.location,
                raw_output=previous.raw_output,
                input_tokens=0,
                output_tokens=0,
                model=MODEL,
                pass_kind="reflect",
                error=err,
            )


async def extract_chunks(chunks: list, concurrency: int = DEFAULT_CONCURRENCY,
                         cache_dir: Optional[Path] = None,
                         tracker: Optional[ProgressTracker] = None) -> list[ExtractionResult]:
    """Llama a la API sobre todos los chunks. Cachea por chunk si cache_dir.

    Si `tracker` se provee, lo actualiza por chunk completado.
    """
    client = anthropic.AsyncAnthropic()
    sem = asyncio.Semaphore(concurrency)
    tasks = []

    def _cache_path(chunk):
        if cache_dir is None:
            return None
        d = cache_dir / chunk.source_doc.replace(".pdf", "") / "raw"
        d.mkdir(parents=True, exist_ok=True)
        return d / f"{chunk.chunk_id}.json"

    async def _one(chunk):
        cp = _cache_path(chunk)
        if cp and cp.exists():
            with cp.open() as f:
                d = json.load(f)
            # Si la entrada cacheada tiene error, NO la reusamos — reintentamos.
            if not d.get("error"):
                cached = ExtractionResult(
                    chunk_id=d["chunk_id"],
                    source_doc=d["source_doc"],
                    location=d["location"],
                    raw_output=d["raw_output"],
                    input_tokens=d["input_tokens"],
                    output_tokens=d["output_tokens"],
                    model=d["model"],
                    pass_kind=d["pass_kind"],
                    error=d.get("error"),
                )
                # Cached hits NO cuentan al tracker para que cost/rate reflejen
                # solo API calls reales nuevas (no costo histórico).
                return cached
        r = await extract_chunk(client, chunk, sem, tracker=tracker)
        # Solo cachear si NO hubo error; los errores deben re-intentarse en runs posteriores.
        if cp and not r.error:
            with cp.open("w") as f:
                json.dump(r.to_dict(), f, ensure_ascii=False, indent=2)
        if tracker is not None:
            await tracker.update(r)
        return r

    for c in chunks:
        tasks.append(asyncio.create_task(_one(c)))
    return await asyncio.gather(*tasks)
