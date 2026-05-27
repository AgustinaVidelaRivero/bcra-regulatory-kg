"""Extractor de tripletas por chunk usando Claude Haiku 4.5 con schema cerrado.

Aprendizajes Run 1 + Run 2 incorporados:
- Concurrency=2 para evitar 429 en Haiku 4.5 tier 1.
- Backoff conservador: 3 retries, base 2.0, max ~14s por chunk.
- Cache por chunk individual (reanudable). NO se cachea si error != None.
- ProgressTracker imprime cada 5 chunks con flush=True + costo acumulado + ETA.
- Pydantic relations con default_factory=list (chunks sin relations son OK).
- SYSTEM_PROMPT con regla explícita anti-jerarquía documental + ejemplos negativos.

Uso:
    python extract.py smoke      # corre solo TO Protección al Usuario
    python extract.py full       # corre los 5 TOs completos
"""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
import random
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from anthropic import AsyncAnthropic, APIStatusError, APIConnectionError, RateLimitError
from pydantic import ValidationError

from chunker import Chunk, CHUNKS_DIR, SUBSET, chunk_pdf, chunk_all, save_chunks, load_chunks
from schema import (
    ENTITY_TYPES,
    PREDICATES,
    DOMAIN_RANGE,
    ExtractionOut,
    filter_extraction,
    empty_metrics,
    merge_metrics,
)


# === CONFIG ===

MODEL = "claude-haiku-4-5-20251001"
CONCURRENCY = 2                  # bajado a 2 (Run 2 lección 4): TPM Haiku 4.5 tier 1
MAX_RETRIES = 6                  # subido a 6: overload 529 necesita esperas más largas que rate-limit 429
BACKOFF_BASE = 2.0               # Run 2 lección 4: base 2.0 para 429
OVERLOAD_BACKOFF_BASE = 3.0      # base más agresiva para 529 (Anthropic Overloaded)
MAX_OUTPUT_TOKENS = 8192  # Haiku 4.5 absolute max

# Precios Haiku 4.5 (per MTok) — vigentes a fecha del experimento
PRICE_IN_PER_MTOK = 1.00
PRICE_OUT_PER_MTOK = 5.00


# === SYSTEM PROMPT ===
# Lecciones Run 1 + Run 2: incluir regla anti-jerarquía explícita + ejemplos.

SYSTEM_PROMPT = f"""Sos un extractor de tripletas para un Knowledge Graph regulatorio del BCRA (Banco Central de la República Argentina).

Trabajás con un schema CERRADO y RÍGIDO. NO inventes tipos. NO inventes predicados.

# TIPOS DE ENTIDAD VÁLIDOS (exactamente 7, ningún otro)

1. **Comunicacion**: Una Comunicación A/B/C del BCRA citada en el texto. Ej.: "Com. A 7825", "Comunicación A 7000".
   Properties: codigo (string, ej. "A-7825"), tipo ("A"|"B"|"C"), numero (int).

2. **TextoOrdenado**: El TO consolidado del cual sale el chunk. SIEMPRE incluir un único TextoOrdenado por chunk, derivado del documento fuente. Label = nombre conceptual del TO (ej. "Texto Ordenado de Protección de Usuarios").
   Properties: materia, archivo, version.

3. **EntidadFinanciera**: El sujeto regulado. Bancos, casas de cambio, EFNB, fideicomisos financieros, EPE, etc. Puede ser una categoría abstracta ("bancos comerciales", "entidades financieras") o nominada.
   Properties: categoria (string).

4. **Operacion**: Un acto regulado: financiación, depósito, transferencia, compra/venta de moneda extranjera, clasificación de deudor, presentación informativa, etc.
   Properties: tipo (string).

5. **Restriccion**: Una prohibición o límite cuantitativo/cualitativo. Patrones: "no podrá", "se prohíbe", "el monto no excederá", "el límite es".
   Properties: descripcion (corta, grounded), tipo ("prohibicion"|"limite_cuantitativo"|"limite_cualitativo"), opcional umbral.

6. **Excepcion**: Una condición que suspende/relaja una Restricción u Obligación. Patrones: "salvo", "excepto", "no aplicará cuando", "están exceptuadas".
   Properties: descripcion (corta).

7. **Obligacion**: Un deber positivo. "Deberán presentar", "calcularán", "asignarán", "informarán". Distinto de Restricción.
   Properties: descripcion (corta), tipo ("presentacion_informativa"|"calculo"|"asignacion"|"comunicacion_a_cliente"|"otra"), opcional plazo o frecuencia.

# PREDICADOS VÁLIDOS (exactamente 12, ningún otro)

Cada predicado tiene DOMINIO y RANGO estrictos. Si la dirección o los tipos no coinciden, la tripleta se DESCARTA.

| Predicado | Dominio → Rango |
|---|---|
| `establecida_en` | {{Restriccion, Obligacion, Excepcion, Operacion}} → TextoOrdenado |
| `referencia` | TextoOrdenado → Comunicacion |
| `modificada_por` | TextoOrdenado → Comunicacion |
| `aplica_a` | {{Restriccion, Obligacion}} → EntidadFinanciera |
| `regula` | {{Restriccion, Obligacion}} → Operacion |
| `exceptua` | Excepcion → Restriccion |
| `exceptua_obligacion` | Excepcion → Obligacion |
| `prohibe` | Restriccion → Operacion (USAR cuando Restriccion.tipo = "prohibicion") |
| `limita` | Restriccion → Operacion (USAR cuando Restriccion.tipo = "limite_cuantitativo" o "limite_cualitativo") |
| `ejecuta` | EntidadFinanciera → Operacion |
| `requiere` | Operacion → Obligacion |
| `condiciona` | Obligacion → Operacion |

# REGLAS NO NEGOCIABLES

1. **Los nodos NO son jerarquía documental.** NO crees entidades de tipo "Artículo", "Punto", "Sección", "Capítulo", "Inciso". Si el texto dice "Artículo 12. Las entidades financieras no podrán...", la entidad es la RESTRICCIÓN ("las entidades no podrán..."), no el "Artículo 12". El "Artículo 12" va a `provenance.location` (manejado fuera del LLM).

2. **Cada entidad debe tener un `local_id` único dentro del chunk** (ej. "e1", "e2", "e3"). Las relations usan esos local_ids como source/target.

3. **Las relations son SOLO entre entidades del MISMO chunk.** No referencies entidades externas.

4. **NO inventes tipos ni predicados fuera de las listas.** Si una idea no encaja en las 7 entidades o 12 predicados, NO la incluyas. Es preferible no extraer algo a forzarlo en una caja equivocada.

5. **`label` corto y canónico; la oración del texto va en `properties.description`.** ESTA REGLA ES CRÍTICA — leer con atención.

   Para Obligacion, Restriccion, Excepcion y Operacion:
   - `label`: nombre CANÓNICO de la entidad. Máximo **8 palabras**. Verbo + objeto directo, o sustantivo + modificador. NO copies la oración del corpus.
   - `properties.description`: la oración o cita textual del corpus (acá va el contenido largo, sin tope de palabras).
   - Si dudás entre dos formulaciones para el label, elegí la **más nominal** y la **más corta**.

   Para Comunicacion: `label` es el código corto ("Com. A 7825"). NUNCA copies texto de la comunicación al label.

   Para EntidadFinanciera: `label` es el nombre canónico de la categoría regulada ("Entidades financieras", "Casas de cambio", "PSPCP", "Sujetos obligados"). Máximo 6 palabras. NO incluyas calificadores secundarios en el label ("Entidades financieras reguladas por BCRA" — el "reguladas por BCRA" sobra, ya está en el contexto).

   Para TextoOrdenado: `label` es el nombre conceptual corto ("Protección al Usuario", "Capitales Mínimos", "Exterior y Cambios"). Máximo 5 palabras.

   Ejemplos correctos:
   ✓ Obligacion label: "Informar comisiones al BCRA" / description: "El sujeto obligado deberá informar mensualmente al BCRA todas las comisiones cobradas por cuenta de terceros..."
   ✓ Restriccion label: "Prohibición de cobro diferencial por discapacidad" / description: "No se podrán cobrar comisiones y/o cargos diferenciales a usuarios con dificultades visuales por prestaciones especiales"
   ✓ Operacion label: "Solicitud de financiación" / description: "Solicitud de financiación presentada por un usuario al sujeto obligado"
   ✓ EntidadFinanciera label: "Sujetos obligados" / categoria: "sujetos obligados" (singular y plural se dedupean)

   Ejemplos INCORRECTOS (NO hacer):
   ✗ Obligacion label: "La Gerencia Principal brindará respuesta a consultas del público sobre normativa e información institucional" (108 chars — copia la oración)
   ✗ Restriccion label: "no se podrá reflejar o promover visiones estereotipadas y jerarquizantes de los géneros, androcentrismo, lenguaje sexista..." (>180 chars — copia textual)
   ✗ EntidadFinanciera label: "Entidades financieras, PSPCP, empresas no financieras emisoras de tarjetas y otros proveedores no financieros de crédito" (es una enumeración — ver regla 7)

6. **Siempre incluí un nodo TextoOrdenado con local_id "to" en CADA chunk** (representando el TO del que sale el chunk). Luego conectá las Restriccion/Obligacion/Excepcion del chunk al nodo TextoOrdenado vía `establecida_en`. El label del TextoOrdenado debe ser corto (ver regla 5).

7. **Enumeraciones de EntidadFinanciera: UN NODO POR ENTIDAD.** Si el texto enumera varias entidades reguladas (separadas por comas, "y", "o", "u otros"), generá un nodo POR CADA una. NO crees un único nodo cuyo label sea la enumeración entera.

   Ejemplo del corpus: "...aplica a entidades financieras, PSPCP y PSI..."
   - Generar 3 nodos EntidadFinanciera independientes:
     * label: "Entidades financieras" (categoria: "entidad financiera")
     * label: "PSPCP" (categoria: "proveedor de servicio de pago")
     * label: "PSI" (categoria: "proveedor de servicio de pago iniciador")
   - Y conectar cada uno por separado al resto del grafo con su propio edge `aplica_a`.

   ✗ NO: 1 nodo con label "Entidades financieras, PSPCP y PSI"
   ✓ SÍ: 3 nodos separados, cada uno con su propia relación.

# EJEMPLOS NEGATIVOS (qué NO hacer)

- ❌ Entidad de tipo "Artículo" → usá Restriccion/Obligacion según corresponda. El número de artículo va en provenance.
- ❌ Predicado "regulado_por" o "contiene" o "se_aplica_si" → no están en la lista de 12.
- ❌ Restriccion --aplica_a--> Operacion → MAL, `aplica_a` requiere EntidadFinanciera como rango. Usá `regula` o `prohibe`/`limita`.
- ❌ Restriccion --exceptua--> Operacion → MAL, `exceptua` requiere Excepcion como dominio y Restriccion como rango.
- ❌ Texto plano "Punto 3.2.1." como entidad → es jerarquía documental, va en provenance.

# REGLA `regula` / `prohibe` / `limita` (importante)

Tres predicados Restriccion→Operacion. NO son intercambiables. Elegí según `Restriccion.tipo`:

- Si `Restriccion.tipo = "prohibicion"` → usá `prohibe`. Patrón: "no podrá", "se prohíbe", "queda prohibido". Ejemplo: una restricción que dice "no se podrá cobrar comisiones por X" prohíbe la operación "cobrar comisiones".
- Si `Restriccion.tipo = "limite_cuantitativo"` (hay umbral numérico: %, $, monto) → usá `limita`. Ejemplo: una restricción "alcanzar cobertura mínima del 10%" limita la operación "cobertura de cajeros" con umbral 10%.
- Si `Restriccion.tipo = "limite_cualitativo"` (hay restricción cualitativa sin monto) → usá `limita`. Ejemplo: "deberán operar exclusivamente con entidades autorizadas" limita la operación.
- `regula` queda RESERVADO para Obligacion→Operacion (NO para Restriccion→Operacion). Cuando una Obligacion regula cómo se hace una Operacion, usá `regula`.

✅ Restriccion(tipo=prohibicion) --prohibe--> Operacion
✅ Restriccion(tipo=limite_cuantitativo, umbral="10%") --limita--> Operacion
✅ Restriccion(tipo=limite_cualitativo) --limita--> Operacion
✅ Obligacion --regula--> Operacion
❌ Restriccion(tipo=limite_cuantitativo) --regula--> Operacion  ← MAL, usá `limita`
❌ Restriccion(tipo=prohibicion) --regula--> Operacion  ← MAL, usá `prohibe`

# FORMATO DE SALIDA

Llamá la herramienta `extract_kg_triples` con el schema dado. Si el chunk no tiene contenido normativo extraíble (preámbulo vacío, lista de abreviaturas, etc.), devolvé entities y relations vacíos.
"""


# === TOOL DEFINITION (extract_kg_triples) ===

TOOL_SCHEMA = {
    "name": "extract_kg_triples",
    "description": "Extrae entidades y relaciones del chunk según el schema cerrado de 7 entidades y 12 predicados.",
    "input_schema": {
        "type": "object",
        "properties": {
            "entities": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "local_id": {"type": "string", "description": "Identificador local único dentro del chunk."},
                        "type": {"type": "string", "enum": list(ENTITY_TYPES)},
                        "label": {"type": "string", "description": "Etiqueta legible humana, grounded en el texto."},
                        "properties": {
                            "type": "object",
                            "additionalProperties": {"type": "string"},
                            "description": "Properties de la entidad. Ver definición de cada tipo.",
                        },
                    },
                    "required": ["local_id", "type", "label"],
                    "additionalProperties": False,
                },
            },
            "relations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "source": {"type": "string", "description": "local_id de la entidad source."},
                        "target": {"type": "string", "description": "local_id de la entidad target."},
                        "predicate": {"type": "string", "enum": list(PREDICATES)},
                    },
                    "required": ["source", "target", "predicate"],
                    "additionalProperties": False,
                },
            },
        },
        "required": ["entities", "relations"],
        "additionalProperties": False,
    },
}


# === PROGRESS TRACKER ===

@dataclass
class ProgressTracker:
    total: int
    completed: int = 0
    failed: int = 0
    throttled: int = 0
    total_in_tokens: int = 0
    total_out_tokens: int = 0
    t_start: float = 0.0
    last_window_t: float = 0.0
    last_window_completed: int = 0
    print_every: int = 5

    def start(self) -> None:
        self.t_start = time.time()
        self.last_window_t = self.t_start

    @property
    def cost_usd(self) -> float:
        return (
            self.total_in_tokens / 1_000_000 * PRICE_IN_PER_MTOK
            + self.total_out_tokens / 1_000_000 * PRICE_OUT_PER_MTOK
        )

    def tick(self, in_tok: int, out_tok: int, fail: bool, throttled: int) -> None:
        self.completed += 1
        self.total_in_tokens += in_tok
        self.total_out_tokens += out_tok
        if fail:
            self.failed += 1
        self.throttled += throttled

        if self.completed % self.print_every == 0 or self.completed == self.total:
            now = time.time()
            dt = now - self.last_window_t
            window_n = self.completed - self.last_window_completed
            rate = window_n / dt if dt > 0 else 0.0
            elapsed = now - self.t_start
            remaining = self.total - self.completed
            eta_sec = remaining / rate if rate > 0 else float("inf")
            eta_min = eta_sec / 60.0
            pct = self.completed / self.total * 100
            print(
                f"[{self.completed:4d}/{self.total}] {pct:5.1f}% | "
                f"in={self.total_in_tokens:>9,} out={self.total_out_tokens:>8,} | "
                f"${self.cost_usd:6.3f} | "
                f"{rate*60:5.1f}/min | "
                f"throt={self.throttled} fail={self.failed} | "
                f"ETA {eta_min:5.1f}min",
                flush=True,
            )
            self.last_window_t = now
            self.last_window_completed = self.completed


# === EXTRACTOR ===

def chunk_cache_path(chunk: Chunk, cache_root: Path) -> Path:
    """Path de cache para un chunk individual. Hash determinístico del id+texto."""
    h = hashlib.sha1(f"{chunk.chunk_id}|{chunk.text}".encode("utf-8")).hexdigest()[:12]
    safe = chunk.chunk_id.replace("/", "_").replace("::", "__")[:80]
    return cache_root / f"{safe}__{h}.json"


async def extract_one(
    client: AsyncAnthropic,
    chunk: Chunk,
    cache_root: Path,
    semaphore: asyncio.Semaphore,
    progress: ProgressTracker,
) -> dict[str, Any]:
    """Extrae un chunk, con cache + retry. Devuelve el dict del resultado."""
    cache_path = chunk_cache_path(chunk, cache_root)
    if cache_path.exists():
        try:
            cached = json.loads(cache_path.read_text(encoding="utf-8"))
            if cached.get("error") is None:
                # cache hit válido
                progress.tick(
                    in_tok=cached.get("in_tokens", 0),
                    out_tok=cached.get("out_tokens", 0),
                    fail=False,
                    throttled=0,
                )
                return cached
            # Error cacheado: re-intentar (Run 2 lección 5)
        except Exception:
            pass  # cache corrupto, re-extraer

    user_message = (
        f"Documento fuente: {chunk.doc}\n"
        f"Ubicación: {chunk.location}\n\n"
        f"Texto del chunk:\n```\n{chunk.text}\n```\n\n"
        f"Extraé las entidades y relaciones según el schema. Recordá incluir el nodo TextoOrdenado con local_id='to'."
    )

    last_err: str | None = None
    in_tok = 0
    out_tok = 0
    throttle_events = 0

    async with semaphore:
        for attempt in range(MAX_RETRIES):
            try:
                resp = await client.messages.create(
                    model=MODEL,
                    max_tokens=MAX_OUTPUT_TOKENS,
                    system=SYSTEM_PROMPT,
                    tools=[TOOL_SCHEMA],
                    tool_choice={"type": "tool", "name": "extract_kg_triples"},
                    messages=[{"role": "user", "content": user_message}],
                )
                in_tok = resp.usage.input_tokens
                out_tok = resp.usage.output_tokens

                tool_use = None
                text_blocks: list[str] = []
                for block in resp.content:
                    btype = getattr(block, "type", None)
                    if btype == "tool_use":
                        tool_use = block
                        break
                    if btype == "text":
                        text_blocks.append(getattr(block, "text", ""))

                stop_reason = getattr(resp, "stop_reason", None)
                if stop_reason == "max_tokens":
                    last_err = f"max_tokens_hit in={in_tok} out={out_tok} chunk_chars={len(chunk.text)}"
                    print(f"  [MAX_TOKENS_HIT] {chunk.chunk_id}: in={in_tok} out={out_tok} chars={len(chunk.text)} → CHUNK DEMASIADO GRANDE", flush=True)
                    break

                if tool_use is None:
                    text_preview = (" | ".join(text_blocks))[:300]
                    last_err = f"no_tool_use stop_reason={stop_reason} text={text_preview!r}"
                    print(f"  [no_tool_use] {chunk.chunk_id}: stop_reason={stop_reason} | text_preview={text_preview!r}", flush=True)
                    break  # no es recuperable con retry

                try:
                    parsed = ExtractionOut.model_validate(tool_use.input)
                except ValidationError as ve:
                    last_err = f"pydantic_validation: {str(ve)[:200]}"
                    print(f"  [pydantic_invalid] {chunk.chunk_id}: {str(ve)[:200]}", flush=True)
                    break

                filtered, val_metrics = filter_extraction(parsed)

                result = {
                    "chunk_id": chunk.chunk_id,
                    "doc": chunk.doc,
                    "location": chunk.location,
                    "entities": [e.model_dump() for e in filtered.entities],
                    "relations": [r.model_dump() for r in filtered.relations],
                    "in_tokens": in_tok,
                    "out_tokens": out_tok,
                    "validation": val_metrics,
                    "error": None,
                }
                cache_path.parent.mkdir(parents=True, exist_ok=True)
                cache_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
                progress.tick(in_tok=in_tok, out_tok=out_tok, fail=False, throttled=throttle_events)
                return result

            except RateLimitError as e:
                throttle_events += 1
                wait = (BACKOFF_BASE ** attempt) + 0.5
                print(f"  [throttle] {chunk.chunk_id} attempt {attempt+1}/{MAX_RETRIES}: 429, waiting {wait:.1f}s", flush=True)
                await asyncio.sleep(wait)
                last_err = f"rate_limit: {e}"
            except APIStatusError as e:
                if e.status_code == 529:
                    # Anthropic Overloaded — backoff agresivo con jitter, capeado a 60s
                    throttle_events += 1
                    wait = min(60.0, (OVERLOAD_BACKOFF_BASE ** attempt) + random.uniform(0.5, 2.5))
                    print(f"  [529 overloaded] {chunk.chunk_id} attempt {attempt+1}/{MAX_RETRIES}: waiting {wait:.1f}s", flush=True)
                    await asyncio.sleep(wait)
                    last_err = f"api_529_overloaded: {e}"
                elif e.status_code and e.status_code >= 500:
                    wait = (BACKOFF_BASE ** attempt) + 0.5
                    print(f"  [{e.status_code}] {chunk.chunk_id} attempt {attempt+1}: waiting {wait:.1f}s", flush=True)
                    await asyncio.sleep(wait)
                    last_err = f"api_{e.status_code}: {e}"
                else:
                    last_err = f"api_{e.status_code}: {e}"
                    break
            except APIConnectionError as e:
                wait = (BACKOFF_BASE ** attempt) + 0.5
                print(f"  [conn] {chunk.chunk_id} attempt {attempt+1}: waiting {wait:.1f}s", flush=True)
                await asyncio.sleep(wait)
                last_err = f"connection: {e}"
            except Exception as e:
                last_err = f"unexpected: {type(e).__name__}: {e}"
                print(f"  [unexpected] {chunk.chunk_id}: {last_err}", flush=True)
                break

    # Si llegó acá: falló. NO cachear (Run 2 lección 5).
    progress.tick(in_tok=in_tok, out_tok=out_tok, fail=True, throttled=throttle_events)
    return {
        "chunk_id": chunk.chunk_id,
        "doc": chunk.doc,
        "location": chunk.location,
        "entities": [],
        "relations": [],
        "in_tokens": in_tok,
        "out_tokens": out_tok,
        "validation": empty_metrics(),
        "error": last_err or "unknown",
    }


async def extract_chunks(chunks: list[Chunk], cache_root: Path) -> list[dict[str, Any]]:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY no está set en el environment.")

    client = AsyncAnthropic(api_key=api_key)
    semaphore = asyncio.Semaphore(CONCURRENCY)

    cached_ok = 0
    for c in chunks:
        cp = chunk_cache_path(c, cache_root)
        if cp.exists():
            try:
                d = json.loads(cp.read_text(encoding="utf-8"))
                if d.get("error") is None:
                    cached_ok += 1
            except Exception:
                pass
    if cached_ok > 0:
        print(f"Cache: {cached_ok}/{len(chunks)} chunks ya cacheados (skipping).", flush=True)

    progress = ProgressTracker(total=len(chunks))
    progress.start()

    tasks = [
        extract_one(client, c, cache_root, semaphore, progress)
        for c in chunks
    ]
    results = await asyncio.gather(*tasks)

    elapsed_min = (time.time() - progress.t_start) / 60.0
    print(
        f"\nDONE — completed={progress.completed} failed={progress.failed} "
        f"throttled={progress.throttled} in_tok={progress.total_in_tokens:,} "
        f"out_tok={progress.total_out_tokens:,} cost=${progress.cost_usd:.3f} "
        f"elapsed={elapsed_min:.1f}min",
        flush=True,
    )
    return results


def main() -> int:
    valid_modes = ("smoke", "full", "one")
    if len(sys.argv) < 2 or sys.argv[1] not in valid_modes:
        print("Uso: python extract.py {smoke | full | one <doc_substring>}")
        return 1

    mode = sys.argv[1]

    if mode == "smoke":
        pdf = SUBSET / "TO_proteccion_usuarios_servicios_financieros_actual.pdf"
        chunks = chunk_pdf(pdf)
        cache_root = CHUNKS_DIR / "smoke"
        save_chunks(chunks, CHUNKS_DIR / "chunks_smoke.json")
    elif mode == "one":
        if len(sys.argv) < 3:
            print("Uso: python extract.py one <doc_substring>")
            return 1
        substr = sys.argv[2]
        pdfs = sorted(p for p in SUBSET.glob("*.pdf") if substr in p.name)
        if len(pdfs) != 1:
            print(f"Match ambiguo o nulo para '{substr}': {[p.name for p in pdfs]}")
            return 1
        chunks = chunk_pdf(pdfs[0])
        cache_root = CHUNKS_DIR / "full"  # comparte cache con full (acumulativo)
        # No sobreescribimos chunks_all.json acá; usamos uno temporal por TO
        save_chunks(chunks, CHUNKS_DIR / f"chunks_one_{pdfs[0].stem}.json")
        print(f"Modo one: procesando solo {pdfs[0].name} ({len(chunks)} chunks)", flush=True)
    else:  # full
        pdfs = sorted(SUBSET.glob("*.pdf"))
        chunks = chunk_all(pdfs)
        cache_root = CHUNKS_DIR / "full"
        save_chunks(chunks, CHUNKS_DIR / "chunks_all.json")

    cache_root.mkdir(parents=True, exist_ok=True)
    print(f"Mode: {mode} | chunks: {len(chunks)} | cache_root: {cache_root}", flush=True)

    results = asyncio.run(extract_chunks(chunks, cache_root))

    # Volcar resumen
    summary = {
        "mode": mode,
        "n_chunks": len(chunks),
        "n_results": len(results),
        "n_failed": sum(1 for r in results if r.get("error")),
        "n_entities_total": sum(len(r["entities"]) for r in results),
        "n_relations_total": sum(len(r["relations"]) for r in results),
    }
    print("\nResumen:", json.dumps(summary, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
