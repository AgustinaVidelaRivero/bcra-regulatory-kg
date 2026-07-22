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

---

## Fase 2.5 — Refinamiento del grafo (pipeline como Skill)

> **Numeración canónica (según los informes de la autora):** 2.3 = evaluación congelada; 2.3+ = instrumentación post-hoc (`llm_cache.py`, `runners/run_posthoc.py`); **2.4 = verificador** (`verificador.py`, `pdf_locate.py`); **2.5 = refinamiento**. Versiones previas de este documento llamaban "2.4" al refinamiento — eso era incorrecto.

La FASE 2.3 cerró con un ganador. La FASE 2.5 toma ese grafo y lo **refina iterativamente**: detectar dónde falla el sistema, atribuir la causa, proponer cambios, aplicarlos y demostrar mejora medible. El pipeline se empaqueta como una **Skill de Claude** para que el ciclo sea repetible, barato y confiable (workflow congelado, no loop agéntico que redescubre el camino cada vez).

### Resultado heredado de la Fase 2.3

- **Grafo ganador: Run 3 (PPF Core).** Seleccionado por consistencia multidimensional (correctitud, cadenas de excepción, estabilidad, abstención, precisión de citas) sobre `eval_set_v1` (23 preguntas), con N=3 repeticiones y veredicto modal. Juez v2.1.1 (dos pasos). Esta selección está **congelada** — no se reabre en 2.5.
- Archivos congelados de 2.3 en `data/experiment/evaluacion/`: `loader.py`, `harness.py`, `judge.py`, `run_frozen.py`.

### Infraestructura construida (semana del 16-24 jun, en `data/experiment/evaluacion/`)

- **`llm_cache.py`** — caché + captura del crudo. Envuelve el cliente Anthropic, guarda el objeto completo de la API (`resp.model_dump()`: tokens, razonamiento, stop_reason) en SQLite. Key = hash determinístico (prompt+modelo+temp+tools+thinking). Namespace versionado (code_version + graph_fingerprint + flag `think=0/1`). Write-through (resumible ante kill). Tests: `tests/test_llm_cache.py`.
- **`runners/run_posthoc.py`** — runner instrumentado. `ParamOverrideClient` por encima de la caché inyecta thinking/temp sin tocar el harness congelado. En thinking-OFF el override es identidad → request byte-idéntico al frozen. Flags `--thinking`/`--reps`/`--run all`, modos `--preflight`/`--verify-replay`.
- **`verifier_pilot.py`** — verificador de calidad del KG. Para cada claim fallido: recupera el nodo de la traza, localiza el pasaje en el PDF, compara (¿nodo fiel al PDF? ¿agente fiel al nodo?), clasifica con árbol auditable. Taxonomía: contenido_kg, completitud_kg, estructural_kg (defectos del KG) / desvio_agente, falla_abstencion (defectos del agente) / provenance_imprecisa. Haiku para mapeo claim→nodo, Opus para clasificación. Calibrado contra juicio manual (piloto de 10), escalado a 382 claims.

### Resultados de la evaluación cualitativa (frozen, no se re-corre sin decisión de mentores)

> Aclaración de alcance: lo "frozen" es la **evaluación comparativa de los 5 grafos** (la que seleccionó al ganador). El pipeline de refinamiento de 2.5 (Paso 2) SÍ corre el agente RAG, pero **solo sobre la copia de trabajo de run_3**, para generar trazas de diagnóstico — no re-corre ni reabre la comparación de los 5.


- Re-corrida post-hoc: 5 grafos × 23 preguntas × 2 condiciones (thinking OFF/ON) = **230 trazas** en `posthoc_run/traces/{off,on}/run_X/`. **N=1** (con caché, N=3 colapsa en copias) → sirve para análisis cualitativo, NO reconfirma el ganador con el rigor del frozen. **Pregunta abierta para Lucho: ¿reconfirmación N=3 sin caché, o alcanza el análisis cualitativo?**
- Mapa de defectos (382 claims fallidos): ~38% defecto del KG, ~49% del agente, ~12% falso positivo del juez.
- **Provenance depurada:** la dimensión `provenance_imprecisa` salió 60 nodos en bruto, ~42% eran artefactos de localización (el localizador agarraba el índice del PDF en vez del cuerpo). Depurada calibrando contra juicio manual (11/12). Reales: 34 (techo). Mapa depurado en `posthoc_run/pilot_verificador/mapa_depurado.json`.
- **Ranking por grafo tras depurar (nodos defectuosos):** run_4=15, run_3=16 (empate en la punta), run_1=22, run_5=30, run_2=33. **Hallazgo abierto:** el mapa NO contradice a run_3; empata con run_4 en fidelidad de contenido, run_3 gana por las otras dimensiones del frozen. La ventaja de run_3 está en cómo el agente navega el grafo, no en el contenido. (A discutir con mentores.)
- Hallazgo meta: el juez es inestable (mismo claim+nodo → veredicto distinto OFF/ON en CQ-020, CQ-014) → parte del "efecto thinking" es ruido de medición.

### Dataset de evaluación (estado actual)

- **`eval_set_v1.json`** (23 preguntas) — el original, intacto. Generado a ciegas.
- **`eval_set_v2.json`** (31 preguntas) — v1 + 8 nuevas (CQ-040 a CQ-047), generadas a ciegas contra los PDFs (instancia separada que NO vio los grafos), verificadas contra el cuerpo de los PDFs. Distribución: factual_directa 10, multi_norma 9, cadena_restriccion_excepcion 8, unanswerable 4. **Las 8 nuevas son de tipo difícil (multi_norma + cadena)** porque el sistema acierta las factuales y falla en razonamiento multi-salto.
- **Hallazgo del corpus:** el subset de 5 TOs tiene techo de dificultad multi-norma — la mayoría de las referencias cruzadas apuntan FUERA del subset. CQ-025 (v1) apunta a un TO fuera del corpus; marcada como caso de expansión de corpus, a decidir con Lucho.
- **Diagnóstico de las fallas de run_3 sobre v1:** acierta 83% efectivo; falla en 5 preguntas (CQ-017, 020, 025, 031, +034 secundaria), y las 5 son **grafo-atribuibles** (ninguna es límite de razonamiento del agente). Esto es ideal: el pipeline de refinamiento del grafo puede moverlas.

### CAMBIO DE REGLAS respecto de 2.3 (importante)

- En 2.3 los `kg.json` eran **READ-ONLY congelados**. En 2.5 esa congelación se levanta **SOLO para el grafo ganador (run_3)**, y SOLO bajo el flujo controlado del pipeline de refinamiento (paso 5: aplicar cambios y demostrar mejora). Los otros 4 grafos siguen congelados.
- El refinamiento NO es edición libre: cada cambio al grafo debe (a) derivar de un defecto detectado y atribuido en el paso 3, (b) aplicarse de forma trazable, (c) demostrarse con re-corrida del MISMO dataset (side-by-side antes/después).
- **El refinamiento trabaja SIEMPRE sobre una copia de run_3** (ej. `run_3_refinamiento/`), nunca sobre el `run_3` original. El `run_3` ganador del frozen queda intacto como baseline inmutable, para que el side-by-side del Paso 5 compare contra él. (Si más adelante un refinamiento demuestra mejora y se decide "promoverlo", esa es una decisión explícita y registrada, no una edición silenciosa del original.)

### El pipeline de refinamiento (5 pasos — diseño en curso)

1. **Dataset** — partir de un set de queries difícil. NO generado por el agente que refina (sesgo). Usar `eval_set_v2`.
2. **Generar trazas** — ejecutar las queries con el agente RAG sobre el grafo (runner + caché ya construidos).
3. **Analizar trazas (agéntico)** — el agente investiga dónde y por qué se rompe, y atribuye (grafo vs agente). DEBE arrancar desde "¿por qué falló?", NO desde "mirá el nodo" (evitar sesgo de atribución hacia el KG — preocupación explícita de Lucho). Calibrar contra las 5 fallas ya diagnosticadas a mano antes de soltar libertad.
4. **Sugerir cambios** — tres palancas: grafo/esquema, prompt del agente RAG, o expansión de corpus. El agente elige según el defecto.
5. **Aplicar y demostrar** — aplicar el cambio, re-correr el MISMO dataset, mostrar mejora side-by-side. Usar caché para no re-pagar lo no cambiado.

### Skill de refinamiento

- Se empaqueta como Skill de Claude (`skill-creator` de Anthropic instalado en `~/.claude/skills/` como referencia y herramienta).
- Heurística de diseño (del skill-creator): fijar duro SOLO lo que rompe el pipeline si el agente lo hace distinto (ej. usar el mismo dataset para demostrar); todo lo demás, default razonado + criterio del agente. El acceso del verificador al grafo NO se fija como "mirá el grafo" (eso sesga); se da como herramienta que el agente decide usar.

### Reglas operativas de la fase

- NO commits — los maneja la autora.
- Reportes verificables: rutas y números exactos de parseo real, nunca estimaciones.
- Validar un paso antes de avanzar (calibrar contra juicio manual antes de escalar). Patrón consistente del proyecto.
- Trabajo nuevo de 2.5 vive en `data/experiment/evaluacion/` (o subcarpeta dedicada del refinamiento, a definir).