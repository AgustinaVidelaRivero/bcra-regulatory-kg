# Decisiones vigentes de prompt caching en la extracción

Este documento fija las decisiones de prompt caching (Anthropic) que gobiernan
`data/experiment/grafo_v2/code/extract.py` y todo call site LLM de extracción.
Las escribo para que ninguna instancia futura dependa de contexto pegado a
mano: estas cinco decisiones son vinculantes y cualquier cambio que las
contradiga se reporta antes de implementarse.

Anclas verificadas contra `data/experiment/grafo_v2/code/extract.py` a la fecha
de este documento (2026-08-04); si el archivo cambia, las líneas pueden correrse
pero las decisiones siguen vigentes.

## Decisión 1 — Prefijo estático cacheado; el system nunca vuelve a string

El prefijo estático (system prompt con el schema de extracción + tools) va
cacheado con `cache_control {"type": "ephemeral"}` como breakpoint explícito
en el último bloque del prefijo. Nada variable por chunk se agrega antes del
breakpoint: todo lo que cambia por chunk (texto, lista de alcance del TO) va
en el mensaje de usuario, después del breakpoint.

- Ancla: `extract.py:455-461` — `system` como lista de bloques con
  `"cache_control": {"type": "ephemeral"}` sobre `SYSTEM_PROMPT`;
  `extract.py:462` — `tools=[TOOL_SCHEMA]`; `extract.py:464` — lo variable
  por chunk en `messages` (construido por `build_user_message()`,
  `extract.py:389`).

Romper esto rompe el caching **silenciosamente**: la API no falla, solo deja
de haber cache hits y el costo se multiplica sin aviso. En particular, volver
el `system` a string plano elimina el breakpoint, y interpolar cualquier cosa
por-chunk en el system invalida el prefijo en cada request.

## Decisión 2 — El costo se calcula siempre con la fórmula de caching

Todo cálculo de costo de extracción usa la fórmula de
`ProgressTracker.cost_usd`: input no cacheado × precio base, cache write
× 1.25, cache read × 0.10, output × precio de salida. Nunca input+output a
secas — con caching activo, `input_tokens` excluye los tokens cacheados y la
cuenta simple subestima (o malestima) el costo real.

- Ancla: `extract.py:303-312` — propiedad `cost_usd`; constantes de precio en
  `extract.py:65-68` (`PRICE_CACHE_WRITE_PER_MTOK = 1.25`,
  `PRICE_CACHE_READ_PER_MTOK = 0.10`).

## Decisión 3 — Todo call site LLM nuevo de extracción loguea usage

Todo call site LLM nuevo en extracción llama a `log_cache_usage()` con un
`component` distinguible y su `doc`. El log es una línea JSON por response
real de la API, con `input_tokens`, `cache_creation_input_tokens`,
`cache_read_input_tokens` y `output_tokens` — es la única forma de auditar
después si el caching efectivamente funcionó y cuánto costó cada componente.

- Ancla: `extract.py:372-386` — `log_cache_usage(usage, component, doc)`
  escribe a `logs/cache_usage.jsonl` (`CACHE_USAGE_LOG`, `extract.py:77`);
  call site existente en `extract.py:466`
  (`component="extraccion_v2", doc=chunk.doc`). El path está gitignoreado
  (`.gitignore:48`, `logs/`).

## Decisión 4 — Corridas con prefijo idéntico van secuenciales

El caché de un prefijo existe recién cuando la primera response que lo
escribe empieza. Corridas concurrentes con prefijo idéntico lanzadas en frío
pagan cada una el cache write completo en vez de leer el caché de la primera.
Por eso las corridas con prefijo idéntico van secuenciales.

Cuestión abierta registrada, pendiente de laudo: patrón warm-then-parallel
(la primera llamada calienta el caché; las siguientes van en paralelo) para
corridas grandes. No se implementa sin laudo.

## Decisión 5 — El pipeline de evaluación queda EXCLUIDO del caching

El pipeline de evaluación (juez, verificador, S1, harness) queda excluido del
prompt caching de Anthropic: son módulos sellados con caché local propia. No
se aplica `cache_control` ahí, ni directo ni por wrapper. Toda optimización
que toque evaluación se reporta antes de implementarse, sin excepción.
