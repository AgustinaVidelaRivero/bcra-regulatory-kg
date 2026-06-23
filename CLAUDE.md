# Memoria del proyecto — bcra-regulatory-kg

Tesis de grado de Ingeniería en IA (UdeSA, Agustina Videla Rivero) sobre un Knowledge Graph regulatorio del BCRA. La FASE 2.2 del proyecto lanza 5 instancias paralelas de Claude Code, cada una con una estrategia distinta de diseño de schema, sobre el subset compartido en `data/experiment/subset/`. Cada instancia trabaja aislada dentro de `data/experiment/run_X_*/` y NO lee las carpetas de los otros runs.

Documentos fuente de verdad (leer antes de empezar cualquier instancia):
- `docs/schema/experiment_protocol.md` — protocolo común (subset, formato JSON, reglas de modelado, métricas).
- `docs/schema/experiment_instance_template.md` — pasos operativos por instancia.

---

## Lecciones del Run 1 (para futuras instancias paralelas)

### 1. El presupuesto real es ~USD 11 por instancia, no USD 5

El protocolo original fijaba un límite de USD 5 de inferencia por instancia. Los datos reales del Run 1 sobre los 5 TOs (543 chunks, ~338 K tokens de contenido) muestran que el corpus regulatorio del BCRA exige un presupuesto sustancialmente mayor:

- **Extracción Haiku** (527 chunks productivos): **USD 5.59**
- **Resolución Sonnet** (~5 K entidades únicas en 57 batches): **USD 4.40**
- **Hub summarization** (top 15 hubs con Sonnet): **USD 0.55**
- **Total Run 1: USD 10.54**

La estimación inicial de USD 2.65 fue ~3 × optimista. Causas:

- Los chunks reales tienen ~3.000 tokens de input y ~1.500 de output (no ~1.000 y ~300 como se asumió originalmente), porque el dominio regulatorio es denso en obligaciones por página y el cookbook pide `description` grounded por entidad.
- La resolución Sonnet se desvía mucho cuando los batches son grandes (100 entidades) porque el output crece con el tamaño del batch (~4 K tokens/call). Output a $15/MTok domina el costo.

**Para Runs 2-5:** asumir un presupuesto realista de **USD 11 por instancia**. La autora va a actualizar `experiment_instance_template.md` para reflejar esto. Si la estrategia evita la etapa de resolución con Sonnet (p. ej. resolución determinística por reglas o por embeddings locales), el presupuesto baja considerablemente — pero la decisión es de la estrategia, no del protocolo.

### 2. Smoke test sobre 1 TO antes del full run es buena práctica

Antes de lanzar el pipeline sobre los 5 TOs, conviene correrlo entero sobre **1 TO chico** (Protección al Usuario, 36 chunks, ~5 % del corpus) y revisar. Sirve para:

- **Ajustar concurrency** según el rate limit real del tier de API (en el caso del Run 1, había que bajar de 8 a 3 concurrent calls para evitar 429s en Haiku 4.5 con 10 K out tok/min).
- **Descubrir bugs en el pipeline** sin pagarlos sobre todo el corpus (en el Run 1 aparecieron: Pydantic strict en `relations`, tipos fuera del enum, slug collisions por mayúsculas/acentos, parsing defensivo necesario en resolución).
- **Re-proyectar costos con datos reales**, ajustando estimaciones de tokens/chunk antes de comprometer el presupuesto.

El smoke del Run 1 costó USD 0.72 y reveló los 6 problemas que de otro modo hubieran roto el full run a mitad de camino. Inversión que se paga sola.

---

## Lecciones del Run 2 (para futuras instancias paralelas)

Cinco fixes operativos que el Run 2 tuvo que descubrir en el camino. Heredar.

### 1. Re-chunking grueso es probable que sea necesario

El chunking inicial del Run 2 cortaba en cada punto numerado (cualquier profundidad: `1.`, `1.1.1.1.`, `1.1.1.1.1.`) y daba 1.520 chunks → proyección ~USD 25, fuera de presupuesto. Aplicar `MAX_CUT_DEPTH=2` (solo cortar en puntos de profundidad ≤2, los subpuntos más profundos quedan acumulados en el padre) bajó a 504 chunks de ~2.6K chars cada uno, similar al Run 1. **Para tu estrategia:** dimensionar el chunking en función del presupuesto, no solo de la granularidad ideal.

### 2. Ajustes empíricos del vocabulario después del smoke

Si tu estrategia usa vocabulario controlado (predicados o tipos cerrados), el smoke probablemente revele patrones recurrentes donde el LLM usa el vocabulario con dominios/rangos legítimos que el schema no contempló. Resistir el impulso de cortar todo y **revisar manualmente los 5-10 patrones más recurrentes** antes de decidir si afilás el prompt o aflojás el schema. En Run 2, 4 ajustes mínimos al schema + 5 ejemplos negativos en el SYSTEM_PROMPT bajaron las violaciones V3+V4 sin sacrificar la diferenciación.

### 3. Logging por chunk es no-negociable

Primer full run del Run 2: corrió 108 minutos sin output (asyncio.gather espera todo antes de imprimir), fue killed sin diagnóstico. Solución: clase `ProgressTracker` que imprime cada 5 chunks con (chunks completados/total + %, costo acumulado, rate chunks/min sobre últimos 5, throttle events, fails, ETA) y loggea cada 429/timeout individual inmediatamente. **Print con `flush=True` siempre**. Sin esto, debug de runs largos es imposible y se queman horas y dólares.

### 4. Backoff conservador no agresivo

Backoff inicial: 5 reintentos con base 4.0 → hasta 124 s atascados por chunk con 429. Bajado a 3 reintentos con base 2.0 → máximo 14 s por chunk. Combinado con `concurrency=2` (no 3), eliminó throttling completamente en el full run final (0 errores 429 sobre ~500 chunks). **Asunción del backoff agresivo (retry largo recupera más) no se cumple con TPM limits de Haiku 4.5 tier 1**: lo que pasa es que tres tareas en backoff serializan el throughput.

### 5. Cache + reanudación incremental es lo que salvó al Run 2

Cada chunk se cachea individualmente al completarse exitosamente. Cualquier kill del proceso (UI accidental, timeout, falta de visibilidad) no pierde el trabajo hecho. Re-lanzar el mismo comando reanuda desde el último chunk completo. El full run del Run 2 se completó en **3 reanudaciones consecutivas** (kill 1 a 42% del extract, kill 2 a 69% del retry, cierre final con los 60 retries pendientes) sin re-pagar lo ya hecho. **Importante:** NO cachear respuestas con `error != None` para que reintenten en runs posteriores. Y al filtrar cache, contar solo las entradas sin error como "cacheadas" para que el `ProgressTracker` no se confunda con el conteo de total esperado.

---

## Restricciones operativas que todas las instancias respetan

- `data/experiment/subset/` es **READ-ONLY**: leer los 5 PDFs, jamás escribir ahí.
- Escribir SOLO dentro de la propia carpeta de run (`data/experiment/run_X_*/`).
- NO leer las carpetas de otros runs aunque existan.
- NO commits — los maneja la autora manualmente.
- Modelo de extracción: Claude Haiku (protocolo).
- NO evaluar el propio KG — la evaluación es comparativa y se hace en la FASE 2.3.

---

## Fase 2.3 — Evaluación downstream (KG-RAG)

La FASE 2.2 dejó los 5 `kg.json` construidos. La FASE 2.3 los compara: se construye un **harness KG-RAG** (un agente que usa el KG como tool) y se corre un set de *competency questions* sobre los 5 grafos para **seleccionar la mejor estrategia de schema**. Proceso incremental: primero exploración manual con pocas queries, después pipeline automatizado con LLM judge.

### Objetivo

Harness KG-RAG **uniforme** sobre los 5 grafos (mismas tools, misma interfaz) para que la comparación entre estrategias sea justa: la única variable es el grafo, no el código que lo consume.

### Decisiones de diseño (tomadas sobre `data/experiment/evaluacion/00_inventario.md`)

1. **Los 5 `kg.json` quedan congelados.** No se editan. Toda normalización de schema ocurre **en memoria**, vía un adaptador (`evaluacion/loader.py`). Las desviaciones de schema están documentadas en `00_inventario.md` §2.2.
2. **Duplicados de Run 5:** los nodos con `id` idéntico (145 ids, 163 instancias extra) se **mergean en uno**, con **unión de `properties` y de `provenances`**. Cada merge se loguea a `evaluacion/logs/run5_merges.json` (en conflicto de `type`/`label`/valor de property se conserva el de la primera instancia y se registran las variantes).
3. **API Anthropic directa** (SDK oficial, no Bedrock), con un `.env` propio en `evaluacion/.env` (`ANTHROPIC_API_KEY=...`).
4. **Provenance uniforme:** las tools del harness devuelven metadata de provenance **`source_doc` + `location`** únicamente, sin resolución al texto del chunk (se descarta `chunk_id` al normalizar).

### Config de modelos

- **Agente respondedor:** `claude-haiku-4-5-20251001` **fijo** para los 5 grafos (misma capacidad de razonamiento para todos → comparación justa).
- **Juez (fase posterior, LLM-as-judge):** modelo mayor, **a definir**.

### Reglas operativas de la fase

- Los `kg.json` son **READ-ONLY** (congelados, decisión 1). El subset de PDFs sigue read-only.
- **Todo el trabajo nuevo vive en `data/experiment/evaluacion/`** (loader, validadores, harness, reportes, logs, `.env`). No se escribe en las carpetas de los runs.
- **Reportes verificables:** rutas exactas y números exactos provenientes de parseo real, nunca estimaciones.
- NO commits — los maneja la autora.
