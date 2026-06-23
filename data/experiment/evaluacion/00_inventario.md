# Inventario estructural — Fase 2.3 (KG-RAG)

**Fecha:** 2026-06-09
**Alcance:** infraestructura únicamente (ubicaciones, formato, schema, scripts, API, fuentes). NO se evalúa contenido ni calidad de los grafos.
**Método:** lectura directa de archivos en `data/experiment/`, parseo de los 5 `kg.json` con Python (`json.load`), inspección de `~/.aws/` y variables de entorno. Todos los conteos provienen de parseo real, no de estimaciones. Nada fue modificado.

---

## 1. Los 5 `kg.json` finales: ubicación y tamaño

Cada run tiene **un único** `kg.json` final, en la raíz de su carpeta de run. Bytes exactos vía `stat`:

| Run | Ruta exacta | Tamaño (bytes) | Última modificación | Nodos | Edges |
|-----|-------------|---------------:|--------------------|------:|------:|
| Run 1 (cookbook) | `data/experiment/run_1_cookbook/kg.json` | 4.620.142 | 2026-05-24 18:20 | 4.014 | 4.287 |
| Run 2 (papers) | `data/experiment/run_2_papers/kg.json` | 6.755.760 | 2026-05-26 19:21 | 6.214 | 5.680 |
| Run 3 (ppf_core) | `data/experiment/run_3_ppf_core/kg.json` | 4.843.199 | 2026-05-27 05:28 | 4.050 | 6.634 |
| Run 4 (schema_light) | `data/experiment/run_4_schema_light/kg.json` | 4.701.071 | 2026-05-27 07:48 | 3.298 | 3.434 |
| Run 5 (hybrid) | `data/experiment/run_5_hybrid/kg.json` | 5.210.187 | 2026-05-27 11:28 | 6.095 | 5.764 |

### ¿Cómo sé que estos son los finales (vs. intermedios)?

Búsqueda de cualquier archivo `*kg*.json` en `data/experiment/`. Hay versiones intermedias **solo en Run 2 y Run 3**, y están claramente dentro de `code/cache/` (no en la raíz del run):

- **Run 1:** solo `run_1_cookbook/kg.json`. Sin intermedios.
- **Run 2:** final = `run_2_papers/kg.json`. Intermedio = `run_2_papers/code/cache/smoke_kg.json` (KG del smoke test sobre 1 TO, descartable).
- **Run 3:** final = `run_3_ppf_core/kg.json`. Intermedios = `code/cache/kg_smoke.json` (smoke) y `code/cache/kg_intermediate.json` (pre-ensamblado).
- **Run 4:** solo `run_4_schema_light/kg.json`. Sin intermedios `*kg*`.
- **Run 5:** solo `run_5_hybrid/kg.json`. Sin intermedios `*kg*`.

**Criterio de "final":** (a) ubicación en la raíz del run (los intermedios viven en `code/cache/`); (b) nombre canónico `kg.json` sin sufijo `smoke`/`intermediate`; (c) cada `report.md` del run referencia este archivo como salida. Los 5 son el artefacto canónico de su run.

---

## 2. Schema de cada JSON (nodos, edges, provenance)

### 2.1 Forma común (los 5 comparten el esqueleto)

Los 5 son un objeto JSON con `nodes` (lista) y `edges` (lista). **Estructura compartida:**

- **Nodo:** `id` (str), `type` (str), `label` (str), `properties` (dict), `provenance` (dict).
- **Edge:** `source` (str), `target` (str), `relation` (str), `provenance` (dict).
- **`provenance`** siempre contiene al menos `source_doc` + `location`.

A partir de ahí **difieren** en: claves extra de top-level, campos de provenance, presencia de `properties` en edges, convención de `id`, y vocabulario de `type`/`relation`. Detalle abajo.

### 2.2 Diferencias campo por campo

| Aspecto | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
|---|---|---|---|---|---|
| **Claves top-level** | `nodes`, `edges`, **`_meta`** | `nodes`, `edges` | `nodes`, `edges` | `nodes`, `edges` | `nodes`, `edges` |
| **`_meta`** | ✅ `run_id`, `schema_version` (1.0), `dropped_edges` | ❌ | ❌ | ❌ | ❌ |
| **node.provenance** | `source_doc`, `location` | `source_doc`, `location`, **`chunk_id`** | `source_doc`, `location` | `source_doc`, `location` | `source_doc`, `location` |
| **edge.provenance** | `source_doc`, `location` | `source_doc`, `location`, **`chunk_id`** | `source_doc`, `location` | `source_doc`, `location` | `source_doc`, `location` |
| **edge.properties** | ✅ `weight` (todos); `other_locations` (47) | ❌ no existe | ❌ no existe | ✅ `predicate_raw` (todos) | ❌ no existe |
| **Provenance múltiple** | `properties.other_locations` en 980 nodos / 47 edges | nodos: `properties.additional_provenances` (556); edges: **`additional_provenances`** top-level (36) | nodos: **`additional_provenance`** top-level (10) | nodos: `properties.all_provenances` (todos) | (ninguno separado) |
| **Convención de `id`** | prefijo por tipo: `rsj_…`, `req_…` | `tipo:slug` (con `:`): `obligacion:…` | `Tipo_slug`: `TextoOrdenado_…`, `Comunicacion_a_2136` | slug plano snake_case (sin prefijo) | slug plano snake_case (sin prefijo) |
| **# tipos de nodo distintos** | 10 | 12 | 7 | **858** (type-raw fino) | 20 |
| **# relaciones distintas** | **1.548** (verb phrases libres) | 23 (vocab. controlado) | 12 (vocab. controlado) | **1.578** (libre, con `predicate_raw`) | 511 (semi-controlado) |
| **`id` duplicados** | 0 | 0 | 0 | 0 | ⚠️ **145 ids** repetidos (163 instancias extra) |
| **Edges colgantes** (source/target sin nodo) | 0 | 0 | 0 | 0 | 0 |

**Notas de provenance por estrategia:**
- Solo **Run 2** lleva `chunk_id` en provenance (nodos y edges) → trazabilidad al chunk exacto, útil para el harness RAG.
- Solo **Run 1** trae bloque `_meta` con `dropped_edges` (`missing_node`: 20, `self_loop`: 11, `alias_unmapped`: 94).
- El campo `properties` de los **nodos** es heterogéneo por diseño (cada estrategia modela atributos distintos): Run 1 usa `version/description/aliases/source_to/mention_count` (+ `summary/key_facts/time_range` en 15 hub-nodes); Run 4 usa `type_raw/type_raw_counts/name_variants/n_observations/all_provenances`; Run 3 y Run 5 tienen vocabularios de propiedades muy granulares (`umbral`, `plazo`, `ponderador_*`, `codigo`, etc.).

### 2.3 Implicancias para el harness (a tener en cuenta, no son hallazgos de calidad)

1. **Un loader único necesita normalizar 3 cosas:** (a) `id` con/sin prefijo de tipo y con `:` (Run 2) vs. snake_case plano; (b) ausencia de `properties` en edges de Runs 2/3/5; (c) `chunk_id` presente solo en Run 2.
2. **Run 5 tiene 145 `id` de nodo duplicados** (p. ej. `cobertura_del_riesgo_de_credito` ×3). Un loader que indexe nodos por `id` en un dict **colapsaría** esas entradas silenciosamente — hay que decidir política (mergear, sufijar, o reportar) antes de cargarlo.
3. **Integridad referencial:** en los 5 runs, el 100% de `source`/`target` de cada edge resuelve a un `id` de nodo existente (0 colgantes). Para Runs 1–4 además `id` es único → cargan limpio.

---

## 3. Scripts existentes para cargar / validar / consultar

### 3.1 No existe ningún loader/validador/query **global** para los `kg.json`

`grep` sobre `scripts/`, `src/`, `tests/`, `notebooks/` no encontró código que cargue o consulte los `kg.json` (`json.load` + `nodes/edges`, `networkx`, `rdflib`, `neo4j`): **0 resultados.** El harness KG-RAG de la Fase 2.3 hay que construirlo desde cero.

### 3.2 Lo que sí existe, **por run** (acoplado a cada estrategia)

Cada `data/experiment/run_X/code/` tiene su propio pipeline de construcción (no de consulta). Relevantes para entender/cargar el grafo:

- **Run 1:** `01_load_corpus.py … 07_visualize.py`, `06_validate_and_report.py` (validación), `common.py` (utilidades + carga de API key).
- **Run 2:** `pipeline.py`, `extract.py`, `chunking.py`, `assemble.py`, **`validate.py`**, `visualize.py`, `run_full.py`, `run_smoke.py`.
- **Run 3:** `chunker.py`, `extract.py`, `schema.py`, `assemble.py`, `visualize.py`.
- **Run 4:** `chunk.py`, `extract.py`, `assemble.py`, `cluster_types.py`, `filters.py`, `slug.py`, `preassembly_report.py`, `system_prompt.py`, `visualize.py`.
- **Run 5:** `chunker.py`, `extract.py`, `assemble.py`, `models.py`, `prompts.py`, `lenses.py`, `final_metrics.py`, `visualize.py`.

Cada run tiene además un `visualize.py` que lee su propio `kg.json` — sirve como referencia de **cómo parsea cada estrategia su grafo**, pero ninguno es genérico para los 5.

### 3.3 Scripts a nivel repo

`scripts/`: `download_bcra.py` (scraper del corpus), `report_b4_b5.py`, `retry_persistent_fails.py`, `adhoc/b5_minirun_ext.py`. Ninguno carga/consulta los KG finales. `src/` solo tiene paquetes vacíos (`__init__.py` en `extraction/`, `kg/`, `scraper/`).

---

## 4. Estado de la configuración de API

### 4.1 Método de autenticación de los runs: **Anthropic SDK directo** (no Bedrock)

Los 5 runs llaman a la API con el SDK oficial: `anthropic.Anthropic()` / `anthropic.AsyncAnthropic()`, que lee **`ANTHROPIC_API_KEY`** del entorno. La key se carga desde un `.env` por run (`common.py` en Run 1; `run_full.py`/`run_smoke.py` en Run 2; `extract.py` en Run 3). **Ningún run usa Bedrock ni `boto3`.**

Modelos referenciados en el código:
- **Extracción:** `claude-haiku-4-5` (alias) / `claude-haiku-4-5-20251001` (pinned).
- **Resolución / hub-summarize:** `claude-sonnet-4-6`.

### 4.2 Credenciales presentes hoy

| Credencial | Dónde | Estado |
|---|---|---|
| `ANTHROPIC_API_KEY` (env shell) | variables de entorno actuales | ❌ **No seteada** (solo está `ANTHROPIC_BASE_URL=https://api.anthropic.com`) |
| `.env` por run | `run_1_cookbook/.env`, `run_{2,3,4,5}/code/.env` | ⚠️ Existen los 5, pero la línea `ANTHROPIC_API_KEY=` está **vacía** en todos |
| AWS (Bedrock) | `~/.aws/config` + `~/.aws/credentials` | ✅ Perfil **`tds-group-6`**, región `us-east-2`, con `aws_access_key_id`/`aws_secret_access_key`. **Pero ningún código lo usa.** |

### 4.3 Qué falta para llamar a la API desde un pipeline nuevo

1. **Poblar `ANTHROPIC_API_KEY`** — vía `export` en el shell o en un `.env` de la Fase 2.3. Hoy está vacía en los 5 `.env` y ausente del entorno. **Sin esto no se puede llamar a la API.**
2. **Dependencia `anthropic` no está en `requirements.txt`** — el archivo solo lista `rdflib, pyparsing, requests, pypdf, beautifulsoup4, pandas, jupyter, ipykernel`. El SDK `anthropic` (y `python-dotenv`, usado para cargar `.env`) están instalados en `.venv` pero no declarados. Conviene fijarlos para reproducibilidad del harness.
3. **Decisión Anthropic-directo vs. Bedrock:** la infra existente apunta a Anthropic directo (lo más simple: reusar el patrón `anthropic.AsyncAnthropic()`). Las credenciales AWS existen pero requerirían `AnthropicBedrock`/`boto3` y no hay código previo — descartable salvo que se quiera usar el crédito de `tds-group-6`.

---

## 5. Textos fuente de los 5 TOs

### 5.1 Subset canónico del experimento (READ-ONLY) — **PDF**

`data/experiment/subset/` contiene los 5 PDFs, fuente compartida de los 5 runs:

| Archivo | Bytes |
|---|---:|
| `TO_capitales_minimos_actual.pdf` | 5.616.860 |
| `TO_clasificacion_deudores_actual.pdf` | 2.192.648 |
| `TO_exterior_cambios_actual.pdf` | 2.735.398 |
| `TO_proteccion_usuarios_servicios_financieros_actual.pdf` | 2.502.846 |
| `TO_regimen_informativo_contable_mensual_actual.pdf` | 2.326.012 |

(Solo PDF, sin `.txt` plano del TO completo.)

### 5.2 Texto procesado (chunks) — **JSON/JSONL, por run**

No hay un set de chunks compartido; **cada run rechunkeó por su cuenta** dentro de su `code/cache/`. Conteos reales:

- **Run 1:** `run_1_cookbook/code/cache/chunks.jsonl` → **543** líneas/chunks.
- **Run 2:** un `chunks.json` por TO en `code/cache/<TO>/` → capitales 166, clasificación 39, exterior 213, protección 36, régimen 50 (**504** total). Además guarda chunks crudos individuales (`raw/..._chunk_NNNN.json` y `.reflect.json`).
- **Run 3:** `code/cache/chunks_all.json` → **508** chunks (+ `chunks_one_TO_*.json` por TO y `chunks_smoke.json`).
- **Run 4 / Run 5:** chunkean dentro de su cache (`staging.json` / caches propios); el chunk no se persiste como un único `chunks_all` con el mismo nombre — viven en sus respectivos `code/cache/`.

→ Si el harness necesita el texto fuente para grounding, los chunks **ya trazables a `chunk_id` solo existen en Run 2** (ver §2.2). Para los demás, el grounding va por `provenance.location` (p. ej. `"p. 5"`, `"Punto 1.1.1"`) contra el PDF.

### 5.3 Corpus completo (contexto)

El corpus BCRA completo (161 TOs vigentes) está en `data/raw/01_textos_ordenados/actuales/` (PDFs, gitignored). Los 5 del subset son una copia para el experimento. Hay también `data/raw/.../historicos/`. `data/processed/` y `data/kg/` están vacíos (solo `.gitkeep`).

---

## 6. CLAUDE.md / memoria de proyecto

**Sí existe.** `CLAUDE.md` en la raíz del repo (6.677 bytes, 2026-05-26): documenta la Fase 2.2, lecciones operativas de Runs 1 y 2 (presupuesto real ~USD 11/instancia, smoke test, chunking, logging, backoff, cache/reanudación) y las restricciones operativas (subset read-only, aislamiento entre runs, no-commits). Documentos fuente de verdad citados ahí: `docs/schema/experiment_protocol.md` y `docs/schema/experiment_instance_template.md` (ambos presentes). **No creé ni modifiqué ningún archivo de memoria** — pendiente tu decisión.

---

## Resumen de banderas para la Fase 2.3

1. **No hay loader/validador/query genérico** para los 5 KG — construir desde cero.
2. **Schema casi compartido pero con 5 desviaciones** que un loader debe normalizar: `id` con prefijo/`:` vs. plano, `chunk_id` solo en Run 2, `properties` en edges solo Runs 1/4, `_meta` solo Run 1, provenance múltiple con nombres de campo distintos.
3. **Run 5 tiene 145 `id` de nodo duplicados** — definir política antes de cargar.
4. **API key vacía:** `ANTHROPIC_API_KEY` no está seteada en ningún lado utilizable; hay que poblarla. AWS/`tds-group-6` existe pero no lo usa ningún código.
5. **`anthropic` no está en `requirements.txt`** — declarar dependencias del harness.
6. Integridad referencial de edges: **100% resuelta en los 5** (0 colgantes).
