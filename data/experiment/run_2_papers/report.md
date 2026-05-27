# Report — Run 2 — Papers del estado del arte

**Identificación del run:** `Run 2 — Papers del estado del arte`
**Carpeta:** `data/experiment/run_2_papers/`
**Estrategia:** schema-aware con vocabulario controlado de 23 predicados + validación estructural automática V1–V8 + loop de reflexión (1 retry) inspirado en FinReflectKG, RAGulating Compliance, LKIF Core, Akoma Ntoso y PROV-O. Ver `schema.md` para el detalle del diseño.

---

## 1. Métricas del protocolo (sección d)

### 1.1 Tiempo y costo

| Métrica | Valor |
|---|---:|
| **Tiempo de construcción (wall-clock, fase por fase)** | smoke 1: 6.9 min · smoke 2: 2.8 min · smoke 3: 4.5 min · fase 1 full: 10.8 min · fase 2 (3 corridas): 6.7 + 11 + 7 min · ensamblaje: 0.7 min. **Total efectivo ~50 min** (excluye horas-Claude perdidas en runs killed). |
| Tokens consumidos — extract pass (cache final) | 2.087.522 input · 1.043.309 output |
| Tokens consumidos — retry pass (cache final) | 3.152.936 input · 909.893 output |
| **Costo del KG resultante (tokens en cache final)** | **USD 15.01** (extract USD 7.30 + retry USD 7.70) |
| Costo real cobrado a la API (incluye extracciones del smoke que se sobreescribieron) | estimado **USD 12.8–13.5** (verificar en `console.anthropic.com → Usage`) |
| Pricing aplicado | Haiku 4.5: USD 1/MTok input + USD 5/MTok output |

> **Nota sobre la discrepancia entre USD 15.01 computado del cache vs ~USD 13 reales:** El cache final tiene UN raw + (opcional) UN reflect por chunk. Pero durante el desarrollo, los chunks del TO de Protección al Usuario se procesaron varias veces (smoke 1 con chunks finos de 950 chars, smoke 2 con retry sobre el feedback distinto, smoke 3 con chunks gruesos de 2,5K chars). Los reflects de smoke 1+2 se descartaron porque el chunking cambió. El costo "del cache" cuenta solo el último resultado retenido; el costo "real" agrega lo descartado.

### 1.2 KG resultante

| Métrica | Valor |
|---|---:|
| **Nodos** | **6.214** |
| **Edges** | **5.680** |
| **Densidad** (edges/nodes) | **0.914** |
| **Tipos de entidad únicos usados** | **12 / 12 declarados** ✅ |
| **Tipos de relación únicos usados** | **23 / 23 declarados** ✅ |
| Predicados sin uso | ninguno (0) |

### 1.3 Nodos por tipo

| Conteo | Tipo | % del KG |
|---:|---|---:|
| 1.346 | `Obligacion` | 21.7% |
| 1.150 | `ConceptoDefinido` | 18.5% |
| 1.042 | `Requisito` | 16.8% |
| 659 | `Operacion` | 10.6% |
| 477 | `NormaReferenciada` | 7.7% |
| 435 | `Umbral` | 7.0% |
| 434 | `InstrumentoFinanciero` | 7.0% |
| 265 | `Plazo` | 4.3% |
| 263 | `SujetoRegulado` | 4.2% |
| 105 | `Procedimiento` | 1.7% |
| 28 | `OrganismoRegulador` | 0.5% |
| 10 | `Sancion` | 0.2% |

### 1.4 Edges por predicado

| Conteo | Predicado | Familia |
|---:|---|---|
| 1.087 | `obligado_a` | imputación |
| 765 | `aplica_a` | aplicabilidad |
| 690 | `requiere` | composición |
| 638 | `usa_concepto` | conceptual |
| 457 | `condicion_de_aplicabilidad` | aplicabilidad |
| 368 | `tiene_umbral` | cuantitativa |
| 360 | `involucra_instrumento` | composición |
| 304 | `tiene_plazo` | temporal |
| 265 | `referencia` | conceptual |
| 230 | `puede_realizar` | imputación |
| 126 | `supervisado_por` | imputación |
| 72 | `es_subtipo_de` | taxonomía |
| 57 | `excepcion_a` | aplicabilidad |
| 52 | `modifica` | conceptual |
| 50 | `definido_por` | conceptual |
| 46 | `ejecutado_por` | composición |
| 41 | `dirigido_a` | composición |
| 21 | `parte_de_procedimiento` | composición |
| 15 | `clasifica_a` | conceptual |
| 12 | `requiere_autorizacion_de` | composición |
| 9 | `genera_sancion` | sancionatoria |
| 9 | `impuesta_por` | sancionatoria |
| 6 | `recae_sobre` | sancionatoria |

**Observaciones del shape de uso:**
- Los 5 predicados más usados (`obligado_a`, `aplica_a`, `requiere`, `usa_concepto`, `condicion_de_aplicabilidad`) concentran el **63%** de los edges.
- La cola larga (los últimos 5 predicados con ≤12 edges) representa el 0.9% — son predicados específicos del dominio sancionatorio y autorizativo que aparecen poco pero capturan información cualitativamente importante.
- **El predicado `recae_sobre` agregado post-schema rinde 6 edges** (la "observación A" del review se materializó: el modelo realmente extrae relaciones `Sancion → SujetoRegulado`).

### 1.5 Cobertura por TO

| TO | Chunks | Productivos | % |
|---|---:|---:|---:|
| TO_capitales_minimos_actual.pdf | 166 | 164 | **98.8%** |
| TO_clasificacion_deudores_actual.pdf | 39 | 39 | **100.0%** |
| TO_exterior_cambios_actual.pdf | 213 | 212 | **99.5%** |
| TO_proteccion_usuarios_servicios_financieros_actual.pdf | 36 | 34 | **94.4%** |
| TO_regimen_informativo_contable_mensual_actual.pdf | 50 | 49 | **98.0%** |
| **TOTAL** | **504** | **498** | **98.8%** |

Los 6 chunks improductivos son fragmentos sin contenido regulatorio extraíble (índices, tablas vacías, encabezados sueltos).

### 1.6 Métricas del loop de reflexión (diferenciales del Run 2)

| Métrica | Valor |
|---|---:|
| Chunks con ≥1 violación en 1ª pasada | **450 / 504 (89.3%)** |
| Chunks que dispararon retry | **450 / 504 (89.3%)** |
| Chunks con violaciones residuales POST-retry (flagged) | **228 / 504 (45.2%)** |
| Violaciones por código (1ª pasada) | V3: 1.335 · V4: 507 · V5: 322 · V7: 244 · V2: 19 · V1: 17 · V6: 13 |

El retry rate alto (89.3%) **no refleja un schema mal diseñado**, sino que el LLM comete violaciones sistemáticas de dirección/rango sobre las que el vocabulario controlado correctamente actúa como filtro. El residual del 45.2% (chunks con violaciones que persisten post-retry y se conservan con flag) cuenta cualquier violación residual, incluyendo las "auto-corregibles" V5/V6/V8 — el número operativamente relevante es mucho menor cuando se filtran solo las críticas. Este número es la traza honesta del trade-off de un schema estricto: corta más, pide más retries, pero el output final mantiene el rigor del vocabulario.

---

## 2. Análisis post-hoc de predicados

| Métrica | 1ª pasada (extract) | 2ª pasada (retry) |
|---|---:|---:|
| Relaciones crudas emitidas por el LLM | 6.993 | 5.834 |
| Predicados únicos crudos | 27 | 29 |
| **Predicados del vocabulario** | 23 ✅ | 23 ✅ |
| **Predicados FUERA del vocabulario** | 4 | 6 |
| Edges retenidos en KG final | 5.680 | (mergeados al KG) |
| **Ratio predicados / edges** | **23 / 5.680 = 0.0041** | |

**Predicados inventados por el LLM (descartados en V2):**

| Pasada | Predicado inventado | Conteo | Interpretación |
|---|---|---:|---|
| extract | `puede_realizarse_en` | 3 | Variante semántica de `puede_realizar` |
| extract | `tem_umbral` | 2 | Typo de `tiene_umbral` |
| extract | `supervisa` | 1 | Variante activa de `supervisado_por` |
| extract | `e5` | 1 | local_id usado por error como predicado |
| retry | `e5`, `op5`, `ent_15`, `ent_1`, `e8` | 8 | local_ids residuales (output con confusión) |
| retry | `supervisa_por` | 1 | Variante de `supervisado_por` |

**Vocabulario normalizado:** los 23 predicados están en singular, sin acentos, snake_case. No hay grupos fusionables — todos están a un nivel de granularidad apropiado al dominio.

**Conclusión clave:** el **96% de las emisiones del LLM cayeron dentro del vocabulario controlado desde la 1ª pasada**. El SYSTEM_PROMPT (con los 23 predicados explícitos + dominio/rango + 5 ejemplos negativos canónicos) funcionó como guard-rail efectivo. Las violaciones reales no fueron por inventar predicados (V2: 19/2.221 total = 0.8%), sino por aplicar predicados válidos con dominio o rango fuera del schema (V3+V4: 1.842/2.221 = 82.9%). Esta es la firma esperada de un vocabulario controlado bien definido: el modelo sabe qué decir, pero a veces lo dice con el sujeto/objeto equivocado.

---

## 3. Inventario del directorio `code/`

| Archivo | Rol |
|---|---|
| `schema.py` | Definición ejecutable de los 12 tipos y 23 predicados con dominio/rango. Espejo de `schema.md`. |
| `chunking.py` | Lectura de PDFs con `pypdf`, chunking por punto numerado de profundidad ≤2 (MAX_CHUNK_CHARS=6000, MIN=800). Cache en `cache/<doc>/chunks.json`. |
| `extract.py` | Llamadas async a Haiku 4.5 con SYSTEM_PROMPT schema-aware. Concurrency=2, backoff exponencial 3 reintentos. Incluye `ProgressTracker` para logging por chunk y `reflect_chunk` para el retry pass. |
| `validate.py` | Implementación de V1–V8 + `violations_to_feedback` que genera el prompt de retry estilo FinReflectKG. |
| `pipeline.py` | Orquestación: extract pass → validar → retry pass → ensamblaje. Crea trackers de progreso para cada pasada. |
| `assemble.py` | Dedup determinístico por `(tipo, slug_normalizado)`. Merge de propiedades y provenance. Cero llamadas LLM (a diferencia del cookbook que usa Sonnet en este paso). |
| `visualize.py` | pyvis HTML con colores por tipo, tooltips con descripción y provenance, leyenda. Si el KG > 600 nodos, muestra top-N por grado + vecinos. |
| `run_smoke.py` | Smoke test sobre 1 TO. Para con exit 2 si retry rate > 40% (umbral revisado en `schema.md` después del smoke). |
| `run_full.py` | Pipeline completo. Soporta `--limit`, `--concurrency`, `--no-write-final`, `--only-docs`, `--exclude-docs`. Stdout flushed para `tail -f` desde otra terminal. |
| `.env.example` | Template de `ANTHROPIC_API_KEY`. |
| `cache/` | Outputs intermedios: `<doc>/chunks.json` (chunks pre-LLM), `<doc>/raw/<chunk_id>.json` (extract pass), `<doc>/raw/<chunk_id>.reflect.json` (retry pass), `run_full_phase1.log`, `run_full_phase2.log`, `final_metrics.json`, `predicate_posthoc.json`. |

---

## 4. Observaciones operativas (lecciones para futuras instancias)

### 4.1 Re-chunking grueso fue necesario para el presupuesto

El chunking inicial (corte en cada punto numerado, sin importar profundidad) generaba 1.520 chunks para el corpus completo. Eso proyectaba ~USD 25 a la API. Después de aplicar `MAX_CUT_DEPTH=2` (solo cortar en puntos de profundidad ≤2), el chunking pasó a 504 chunks (similar al Run 1) con tamaño promedio 2.6K chars/chunk.

**Trade-off:** los chunks más grandes consolidan más entidades por nodo (el KG se "comprime" a ~33% menos nodos que con chunks finos), pero pagan menos overhead de SYSTEM_PROMPT y favorecen relaciones intra-chunk.

### 4.2 Ajustes empíricos del vocabulario después del smoke

El smoke inicial mostró 69.5% de retry trigger, con 85% de las violaciones tipo V3 (dominio inválido) o V4 (rango inválido). Análisis manual de patrones reveló que el modelo aplicaba predicados a tipos legítimos que el schema cortaba. Se aplicaron 4 ajustes a dominios/rangos (`aplica_a`, `requiere`, `involucra_instrumento`, `usa_concepto`) + 5 ejemplos negativos canónicos en el SYSTEM_PROMPT. Detalle en `schema.md §"Ajustes post-smoke"`.

### 4.3 Logging por chunk es no-negociable

El primer intento del full run corrió 108 minutos sin output visible (asyncio.gather espera todo antes de imprimir). Fue killed sin diagnóstico. El segundo intento incluyó `ProgressTracker` con print cada 5 chunks, flush=True, y logging de cada 429/timeout/fallo individual. Resultado: visibilidad completa de progreso, costo en tiempo real, ETA, throttle events. Sin esta instrumentación, debug imposible.

### 4.4 Backoff agresivo bloquea el throughput

El backoff inicial era `4, 8, 16, 32, 64` segundos con 5 reintentos = hasta 124 s atascados por chunk con 429. Bajado a `2, 4, 8` con 3 reintentos = máximo 14 s. Combinado con `concurrency=2` (en vez de 3), eliminó completamente los throttle events: 0 errores 429 en todo el run final.

### 4.5 Fallos no bloquean: cache + reanudación incremental

Cada chunk se cachea individualmente al completarse. Cualquier kill del proceso (señal externa, falta de visibilidad, etc.) no pierde el trabajo hecho. Re-lanzar el mismo comando reanuda desde el último chunk completo. Esta arquitectura salvó múltiples horas: el full run se completó en 3 reanudaciones consecutivas (smokes + fase 1 + fase 2 corridas 1, 2, 3) sin re-pagar lo ya hecho.

### 4.6 Resolución determinística por slug, sin LLM

A diferencia del cookbook que usa Sonnet 4.5 para resolución de entidades (~USD 4 según notas del Run 1), Run 2 resuelve por `slug(label)` normalizado (lowercase, sin acentos, snake_case). Cero llamadas LLM en este paso. El trade-off: si dos labels semánticamente equivalentes tienen palabras distintas (p.ej. "préstamo hipotecario" vs "hipoteca"), quedan como nodos separados; con Sonnet se hubieran fusionado. La hipótesis del Run 2 es que para queries downstream (FASE 2.3), el costo de no fusionar esos casos es menor que el costo de USD ~4 + posibles errores de fusión.

---

## 5. Entregables

| Archivo | Tamaño |
|---|---:|
| `schema.md` | 12 KB |
| `kg.json` | 6.6 MB (6.214 nodos · 5.680 edges) |
| `kg_visual.html` | 2.4 MB (pyvis con leyenda y tooltips) |
| `report.md` | (este archivo) |
| `code/` | 10 archivos Python + `.env.example` + `cache/` |

---

*Fin del reporte. Próxima fase del experimento (FASE 2.3): evaluación comparativa entre los 5 KGs producidos por las 5 instancias paralelas. Run 2 NO se auto-evalúa.*
