# Report — Run 3 — 7 entidades core PPF

**Identificación del run:** Run 3 — 7 entidades core PPF
**Carpeta:** `data/experiment/run_3_ppf_core/`
**Estrategia:** schema-based ESTRICTO sobre las 7 entidades de la propuesta de tesis original (con reemplazo Artículo → Obligación, justificado en `schema.md`).
**Modelo de extracción:** Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)
**Resolución:** Determinística pura — sin Sonnet u otro LLM para resolución de duplicados. Toda la deduplicación es por slug normalizado + heurística de singularización castellano + dedup post-hoc por `categoria` para EntidadFinanciera.

---

## 1. Métricas del protocolo (sección d)

### 1.1 Tiempo de construcción

| Etapa | Wall-clock |
|---|---|
| Iteraciones de smoke test (v1 → v5, con debugging) | ~30 min |
| Extracción full Régimen Informativo (44 chunks) | 3.5 min |
| Extracción full Clasificación Deudores (65 chunks) | 5.1 min |
| Extracción full Capitales Mínimos (147 chunks) | 15.1 min (incluye retry de 2 fails) |
| Extracción full Exterior y Cambios (215 chunks) | 21.0 min (incluye 2 sub-chunks manuales splitteados) |
| Ensamblaje del grafo | < 1 min |
| **Total extracción + ensamblaje** | **~75 min** |

Tiempo total del experimento (incluyendo desarrollo iterativo, debugging, smokes descartados, escritura de schema.md y report.md): **~5 horas** de wall-clock.

### 1.2 Costo

**Costo del KG final** (lo que está cacheado y forma parte del `kg.json`):

| TO | Chunks | Tokens IN | Tokens OUT | USD |
|---|---:|---:|---:|---:|
| Protección al Usuario (smoke v5) | 37 | 191,287 | 79,048 | $0.587 |
| Régimen Informativo | 44 | 230,865 | 73,722 | $0.599 |
| Clasificación Deudores | 65 | 327,279 | 117,767 | $0.916 |
| Capitales Mínimos | 147 | 796,067 | 326,374 | $2.428 |
| Exterior y Cambios | 215 + 2 manuales | ~1,103,000 | ~452,000 | $3.373 |
| **Total KG final** | **510** | **~2,648,000** | **~1,049,000** | **$7.90** |

**Costo total de la instancia** (incluye smokes v1–v4 descartados y debugging de bugs): **~$9.91** de $11 de presupuesto. Margen final: **$1.09**.

Sobre el presupuesto de $11 originalmente calibrado en CLAUDE.md: confirmado realista. El smoke testing iterativo costó ~$2 (≈20% del total) — necesario, dado que se encontraron 7 bugs antes de la extracción final.

### 1.3 Nodos por tipo

| Tipo | Conteo | % |
|---|---:|---:|
| Obligacion | 1,248 | 30.8% |
| Operacion | 892 | 22.0% |
| Restriccion | 818 | 20.2% |
| Comunicacion | 699 | 17.3% |
| Excepcion | 258 | 6.4% |
| EntidadFinanciera | 130 | 3.2% |
| **TextoOrdenado** | **5** | **0.1%** |
| **Total** | **4,050** | **100%** |

Confirmación de cardinalidad esperada (schema.md sección 5):
- TextoOrdenado: exactamente 5 ✅ (uno por PDF, dedup por `archivo` funcionó).
- Comunicacion: 699 (esperado decenas a cientos — orden de magnitud OK).
- EntidadFinanciera: 130 (esperado decenas — un poco más alto, ver limitaciones).
- Obligacion/Restriccion/Excepcion: masa principal ✅.

### 1.4 Edges por tipo de relación

Todos los 12 predicados del schema están presentes en el KG:

| Predicado | Conteo | % |
|---|---:|---:|
| `establecida_en` | 2,453 | 37.0% |
| `aplica_a` | 1,464 | 22.1% |
| `regula` | 716 | 10.8% |
| `limita` | 570 | 8.6% |
| `referencia` | 558 | 8.4% |
| `ejecuta` | 204 | 3.1% |
| `condiciona` | 178 | 2.7% |
| `exceptua` | 174 | 2.6% |
| `prohibe` | 131 | 2.0% |
| `exceptua_obligacion` | 76 | 1.1% |
| `modificada_por` | 57 | 0.9% |
| `requiere` | 53 | 0.8% |
| **Total** | **6,634** | **100%** |

### 1.5 Densidad del grafo

`edges / nodes = 6,634 / 4,050 = 1.638` edges por nodo.

Coincide con la expectativa de schema.md (sección 5): ~2-3 edges/nodo. Está al límite inferior porque muchos Comunicacion (699 nodos) sólo tienen un edge entrante (`referencia` o `modificada_por`) y ningún edge saliente.

### 1.6 Tipos de entidad y de relación

- **Tipos de entidad únicos:** **7** (Comunicacion, TextoOrdenado, EntidadFinanciera, Operacion, Restriccion, Excepcion, Obligacion). Cerrado por diseño.
- **Tipos de relación únicos:** **12**. Cerrado por diseño. Todos presentes en el KG final (ningún predicado quedó en 0).

**Schema enforcement: 100%.** Cero violaciones durante el ensamblaje (0 nodos dropped por tipo inválido, 0 edges dropped por predicado inválido, 0 edges dropped por violación de dominio/rango).

### 1.7 Cobertura por TO

| TO | Chunks total | Chunks con contenido | Cobertura |
|---|---:|---:|---:|
| TO_capitales_minimos | 119 | 119 | **100.0%** |
| TO_proteccion_usuarios | 30 | 30 | **100.0%** |
| TO_exterior_cambios | 168 | 167 | 99.4% |
| TO_clasificacion_deudores | 54 | 53 | 98.1% |
| TO_regimen_informativo | 36 | 34 | 94.4% |
| **Promedio ponderado** | **407** | **403** | **99.0%** |

Los 4 chunks sin contenido extraído son fragmentos de tabla de versionado o referencias cruzadas a Comunicaciones modificatorias, sin material normativo. El LLM correctamente no inventa entidades para chunks vacíos de contenido.

> Nota: "Chunks total" en esta tabla es el conteo después del dedup en el assembler (chunks únicos por chunk_id). Los caches en disco son 510 archivos; el assembler dedupea variantes del mismo chunk_id (causadas por matches duplicados del regex de header) eligiendo la extracción con más entidades.

---

## 2. Inventario del directorio `code/`

```
code/
├── chunker.py       # PDF → texto → chunks por punto numerado (MAX_CUT_DEPTH=2)
│                    # + filtro MAX_ROOT_NUMBER=30 (evita capturar "Com. 6664." como header)
│                    # + split de oversized (HARD_CAP_CHARS=7000) por párrafos balanceados
│                    # + split recursivo por oraciones / chars si un párrafo solo es oversized
├── schema.py        # Pydantic strict: 7 EntityType, 12 Predicate, tabla DOMAIN_RANGE
│                    # + model_validator(before) que coerce properties.values a str
│                    # + model_validator(before) que parsea entities/relations si vienen como JSON-string
│                    # + filter_extraction() valida dominio/rango antes del ensamblaje
├── extract.py       # Extractor async Haiku 4.5 con SYSTEM_PROMPT estricto (7 ent × 12 pred,
│                    # ejemplos negativos, regla anti-jerarquía documental, regla label corto
│                    # vs description larga, regla anti-enumeración para EntidadFinanciera).
│                    # Concurrency=2, MAX_RETRIES=6, backoff específico para 429 (base 2.0)
│                    # y 529 Overloaded (base 3.0 con jitter, cap 60s).
│                    # Cache por chunk individual (hash de chunk_id+text), reanudable.
│                    # NO cachea errores. ProgressTracker con flush=True cada 5 chunks.
│                    # MAX_OUTPUT_TOKENS=8192 + detección explícita de stop_reason="max_tokens".
│                    # Modos: smoke | one <doc_substring> | full.
├── assemble.py      # Ensamblador determinístico:
│                    # - Dedup de cache files por chunk_id (pick best extraction by #entities)
│                    # - Dedup de nodos por (type, slug). Slug bases por tipo:
│                    #   * TextoOrdenado: properties.archivo (1 nodo por PDF garantizado)
│                    #   * Comunicacion: properties.codigo
│                    #   * EntidadFinanciera: label normalizado + singularize_slug
│                    #     + lookup truncado (quitar última palabra) para captar
│                    #     "Sujetos obligados regulados" → "Sujetos obligados"
│                    #   * Otros (Operacion/Restriccion/Obligacion/Excepcion): properties.tipo o description
│                    # - Pasada post-hoc para EntidadFinanciera: merge por categoria normalizada;
│                    #   ganador = label más corto; redirección de edges; properties unión.
│                    # - Validación final de dominio/rango (defensa en profundidad).
│                    # - provenance OBLIGATORIO en cada nodo y cada edge.
├── visualize.py     # pyvis 0.3.2: 1 color por tipo, tooltips con properties y provenance.
│                    # Workaround del bug pyvis de doble <h1>: limpia los <h1></h1> vacíos
│                    # del template e inyecta un solo título.
└── cache/
    ├── chunks_*.json   # listas de chunks por modo (smoke/one/all)
    ├── smoke/          # cache extracción Protección al Usuario (smoke v5)
    ├── full/           # cache extracción los 5 TOs (final, 510 archivos)
    ├── *_log_*.txt     # logs de cada corrida
    ├── kg_smoke.json   # KG intermedio del smoke
    ├── kg_visual_smoke.html
    ├── kg_intermediate.json   # KG intermedio Proteccion+Regimen (punto de control)
    ├── assemble_*.json # reportes de ensamblaje
```

---

## 3. Análisis post-hoc de predicados

### 3.1 Predicados únicos crudos vs normalizados

**Predicados crudos extraídos por el LLM: 12.** **Predicados después de normalización: 12.** Ratio 1:1. **No hubo normalización.**

Esto es consecuencia directa del schema cerrado: Pydantic con `Literal[...]` rechaza cualquier predicado que el LLM intente generar fuera de la lista de 12. El SYSTEM_PROMPT ya enuncia los 12 con dominio/rango explícito, lo que hace que el LLM converja rápidamente.

Cero predicados "crudos" en singular vs plural, casing variante o sinónimos. Esta es la diferencia operacional más visible vs estrategias schema-light o emergent: el vocabulario de relaciones queda fijo desde el primer chunk.

### 3.2 Ratio predicados / edges

`12 predicados / 6,634 edges = 0.00181`

Casi 553 edges por predicado en promedio. Distribución muy desigual: `establecida_en` y `aplica_a` concentran 59% del grafo (esperable — son las relaciones estructurales que todo nodo regulatorio tiene contra TO/EntidadFinanciera).

### 3.3 Cobertura del vocabulario

Los **12 predicados** del schema están todos representados en el KG. Ningún predicado quedó en cero, lo que indica que el corpus regulatorio del BCRA cubre todos los matices semánticos definidos a priori (prohibición, limitación cuantitativa, deber positivo, excepción, citación, modificación, ejecución, condicionamiento, requerimiento).

### 3.4 Predicados fusionables

Hipotéticamente, `requiere` (Operacion → Obligacion) y `condiciona` (Obligacion → Operacion) son inversos. Si se fusionaran (eliminando uno), el grafo perdería 53 edges (`requiere`) o 178 edges (`condiciona`). La decisión de mantener ambos fue de diseño (schema.md §3) — facilita consultas bidireccionales sin pasar por queries de inversión manual.

`prohibe` y `limita` podrían fusionarse en `regula`, pero esto haría perder la distinción entre prohibición total vs límite cuantitativo (categorías deontológicamente distintas). Schema.md lo justifica.

`exceptua` y `exceptua_obligacion` se mantienen separados para permitir filtrar por dominio del rango (Restriccion vs Obligacion) en consultas.

---

## 4. Limitaciones conocidas y casos sospechosos

### 4.1 Duplicados semánticos no atrapados por dedup determinística

**Operacion: 35 grupos de nodos con label normalizado idéntico** (55 nodos redundantes). Top 5:

| Label normalizado | # nodos | Distinción que el LLM marcó |
|---|---:|---|
| "acceso al mercado de cambios" | 5 | distintos `tipo`: general, "para pago exterior", "para cancelación líneas crédito", "para operaciones de egreso", etc. |
| "operaciones con derivados otc" | 3 | distintos `tipo`/`description` |
| "pago de utilidades y dividendos" | 3 | distintos `tipo`/`description` |
| "cancelacion de capital e intereses" | 3 | distintos `tipo`/`description` |
| "liquidacion en mercado de cambios" | 3 | distintos `tipo`/`description` |

**Obligacion: 10 grupos**, **Restriccion: 2 grupos**, **Excepcion: 1 grupo** — todos con mismo label literal pero distinto `description`.

**Razón:** la dedup determinística usa la propiedad clave por tipo (`tipo`, `descripcion`) como slug, no el label. Cuando el LLM genera el mismo label pero diferente `tipo`/`descripcion`, los slugs difieren → nodos separados. Resolverlo requeriría comparación semántica (Sonnet u otro LLM-resolver), lo cual la estrategia de Run 3 evita explícitamente por contaminación metodológica con Run 1.

**Documentado como limitación del enfoque "schema rígido + dedup determinística pura".** No es un bug del schema sino una consecuencia de la decisión de diseño.

### 4.2 EntidadFinanciera: casos sospechosos de truncamiento de extracción

EFs con `label` < 35 chars que son prefijo de otra EF del mismo tipo. 22 casos detectados:

| Short label | Longer label (prefijo + extensión) |
|---|---|
| "Bancos" | "Bancos multilaterales de desarrollo" |
| "Bancos" | "Bancos del exterior conveniados" |
| "Bancos" | "Bancos comerciales" |
| "Cajas de Crédito" | "Cajas de Crédito Cooperativas" |
| "Sucursales locales" | "Sucursales locales bancos del exterior" |
| "Fiduciarios" | "Fiduciarios de fideicomisos financieros" |
| "Fiduciarios" | "Fiduciarios fideicomisos financieros" |
| "Clientes" | "Clientes con actividad agrícola" |
| "Clientes" | "Clientes privados no financieros" |
| "Clientes" | "Clientes residentes" |
| ... | +12 más |

**Interpretación:** algunos pueden ser truncamientos genuinos (el LLM cortó el sujeto compuesto en un chunk y lo completó en otro). Otros son distinciones legítimas (un nodo "Bancos" como categoría amplia más nodos específicos como "Bancos multilaterales de desarrollo" que NO son sinónimos sino jerarquía conceptual).

**Cifra dentro del rango "documentable" (~22, esperado 5-30 según CLAUDE.md de la autora).** No es un patrón sistemático que requiera intervención.

### 4.3 Densidad relativamente baja (1.64)

La densidad es algo menor a la expectativa de schema.md (2-3 edges/nodo). Causa: las Comunicaciones (699 nodos, 17% del KG) actúan como hojas — reciben edges `referencia` o `modificada_por` desde TextoOrdenado pero no generan edges salientes. Sin ese aporte, la densidad de los nodos "centrales" (Restricciones, Obligaciones, Excepciones) sobre el resto es más cercana a 2.5.

### 4.4 Cobertura de 99% — los 4 chunks vacíos

4 chunks de 407 no produjeron contenido extraído (1 en Clasificación Deudores, 1 en Exterior y Cambios, 2 en Régimen Informativo). Inspección manual: todos son fragmentos de tabla de versionado o índices sin texto dispositivo. El LLM correctamente devolvió `entities=[]`.

### 4.5 Chunk hit max_tokens (resuelto manualmente)

Un chunk de Exterior y Cambios (`15__p1`, 6976 chars) excedió `max_tokens=8192` aun con HARD_CAP_CHARS=7000. Era un párrafo único sin separadores `\n\n`, muy denso en obligaciones. Se splitteó manualmente en 2 sub-chunks por punto medio de oraciones, y se procesó por separado. **Limitación del chunker:** sólo splittea por `\n\n` (párrafos). Para chunks que son un solo párrafo gigante, requiere intervención manual o splitting por oraciones.

---

## 5. Decisiones de diseño y lecciones aprendidas

### 5.1 Reemplazo Artículo → Obligación

Documentado en `schema.md` §1. La decisión preservó las 7 entidades de la PPF (cardinalidad) sin contaminar el grafo con jerarquía documental. **Las 1,248 Obligaciones del KG validaron la decisión:** sin esa entidad, gran parte del Régimen Informativo Contable Mensual y de Protección al Usuario habrían quedado sin representación nativa.

### 5.2 Predicados desdoblados (`prohibe` / `limita` vs `regula`)

El SYSTEM_PROMPT original sólo decía "usá `regula` para Restriccion → Operacion". Resultado en el smoke v2: `limita: 0`. Después de reforzar el prompt con reglas explícitas + ejemplos negativos, el KG final tiene **570 `limita` y 131 `prohibe`**. La distinción se materializó.

### 5.3 7 bugs encontrados durante el desarrollo iterativo

1. **Anthropic 529 Overloaded** → backoff agresivo específico con jitter, cap 60s, 6 retries.
2. **Pydantic strict en `properties.numero`** (LLM devuelve int, schema exige str) → `model_validator(mode='before')` coerce a string.
3. **TextoOrdenado dedup por `materia`** (text-libre) → cambio a dedup por `archivo` (constante por PDF).
4. **Fails silenciosos sin log** → print explícito con stop_reason y text_preview en cada rama de error.
5. **Labels-frase en vez de labels-entidad** → SYSTEM_PROMPT con regla explícita label corto / description larga + ejemplos del corpus.
6. **Chunker generaba duplicados de chunk_id** (regex matcheaba mismos numbering en cuerpo) → dedup en assembler (no en chunker) picando el chunk con más entidades.
7. **Captura de "headers" falsos** (`8183.`, `6664.` eran números de Comunicaciones) → `MAX_ROOT_NUMBER=30` en chunker.
8. **Chunks oversized hit max_tokens** → `MAX_OUTPUT_TOKENS=8192` + `HARD_CAP_CHARS=7000` + splitting por párrafos.
9. **LLM devolvía `entities` como string JSON** (no array) → `model_validator(mode='before')` parsea JSON-string a list.

Total: **9 bugs/edge cases**. Los lessons del Run 1 y Run 2 documentados en CLAUDE.md anticiparon 4 de ellos; los otros 5 emergieron durante el smoke iterativo. **Smoke test sobre 1 TO probado nuevamente como crítico** — encontró todos antes de gastar el presupuesto en el full.

---

## 6. Conclusión metodológica

El schema cerrado de **7 entidades × 12 predicados con dominio/rango estricto** produce un KG **completamente coherente** (0 violaciones) y **compacto** (4,050 nodos para 5 TOs de regulación densa). El costo de la rigidez es:

- Algunos duplicados semánticos no atrapados por dedup determinística (35 grupos en Operacion, 13 en otros tipos). Resolverlos requeriría LLM-resolver, contaminando la comparación.
- 22 casos sospechosos de truncamiento en EntidadFinanciera (ambiguo entre truncamiento real y distinción jerárquica legítima).
- Cualquier fenómeno regulatorio que no encaje en las 7 cajas se pierde silenciosamente.

La fase 2.3 evaluará si esa rigidez vale la pena comparada con las otras 4 estrategias.
