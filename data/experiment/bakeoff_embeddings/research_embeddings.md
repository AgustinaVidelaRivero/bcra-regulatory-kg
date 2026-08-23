# U-A2.0b-research — relevamiento de modelos de embeddings candidatos

Unidad de APOYO al laudo. No recomiendo ninguno: la elección es laudo de la autora.
Costo de API: USD 0. Escrituras: sólo dentro del scratchpad de la sesión.

---

## 1. Método de lectura del leaderboard (declarado)

**Qué intenté primero.** `https://huggingface.co/spaces/mteb/leaderboard` es un Space
dinámico: el HTML servido en esa URL es sólo el shell de la aplicación. Lo verifiqué
con una descarga estática, que devolvió título, contador de likes, "Running on CPU
Upgrade" y el mensaje de carga, **sin ninguna fila de tabla**. Confirmo entonces
explícitamente: **la URL del Space no es legible de forma estática**.

**Qué usé en su lugar.** Cargué el Space en un navegador real (renderizado JS
completo) apuntando al host del iframe donde el Space sirve su aplicación:

- URL exacta leída: `https://mteb-leaderboard.hf.space/benchmark/MTEB(spa%2C%20v1)`
- (índice de benchmarks: `https://mteb-leaderboard.hf.space/benchmarks`)

Sobre la página ya renderizada extraje el DOM de las dos tablas (`Model leaderboard`
y `Per-task scores`) celda por celda, para no depender del texto aplanado (que
desalinea columnas en los modelos con resultados incompletos).

**Ventana del snapshot:** 2026-08-18, 21:35–21:47 EDT (2026-08-19, 01:35–01:47 UTC).

**No reconstruí ninguna posición de memoria.** Todo número de esta sección viene de
esa lectura, y quedó volcado a:

- `mteb_snapshot/mteb_spa_v1_ranking_por_retr.tsv` (los 30 modelos con puntaje de retrieval)
- `mteb_snapshot/mteb_spa_v1_pertask_candidatos.tsv` (desagregado por tarea de los candidatos)

Los datos de model card vienen de descargas directas de los README y `config.json`
crudos de HuggingFace, guardados en `mteb_snapshot/` (comando reproducible:
`curl -sSL https://huggingface.co/<id>/raw/main/README.md`).

---

## 2. El subconjunto español: qué es y qué tan poblado está

El benchmark español registrado en MTEB se llama **`MTEB(spa, v1)`**, rotulado
"Spanish" en el leaderboard. Descripción textual de la propia página:

> "Spanish text embedding quality across classification, clustering, pair
> classification, reranking, retrieval, and semantic similarity."

Metadatos que declara la página: LANGUAGES 2 · TASKS 16 · TASK TYPES 6 · MODELS 29.

**Las 5 tareas de retrieval que componen la columna `Retr.`** son
`MintakaRetrieval`, `MIRACLRetrievalHardNegatives.v2`, `SpanishPassageRetrievalS2P`,
`SpanishPassageRetrievalS2S` y `XPQARetrieval`. La pestaña "TASK INFORMATION" no
llegó a renderizar su tabla en mi lectura, así que **lo verifiqué por aritmética**
(verificación mía, no dato del leaderboard): el promedio simple de esas 5 columnas
reproduce la columna `Retr.` de los cinco modelos que revisé, al centésimo —
p. ej. jina-v5-text-small (42.65+56.83+49.47+75.42+59.17)/5 = 56.708 → `Retr.` 56.71;
bge-m3 → 49.396 → 49.40. Cálculo en `mteb_snapshot/mteb_spa_v1_pertask_candidatos.tsv`.

**Advertencias estructurales del leaderboard que condicionan la lectura:**

1. **Cobertura muy parcial.** La tabla lista **219 filas de modelo**, pero **sólo 30
   tienen valor en la columna `Retr.`**. Modelos que la autora podría esperar como
   candidatos naturales — `Qwen/Qwen3-Embedding-0.6B`, `google/embeddinggemma-300m`,
   `ibm-granite/granite-embedding-311m-multilingual-r2`, `microsoft/harrier-oss-v1-0.6b`,
   `nomic-ai/nomic-embed-text-v2-moe`, `Alibaba-NLP/gte-multilingual-base`,
   `Snowflake/snowflake-arctic-embed-l-v2.0` — **no tienen puntaje de retrieval en
   `MTEB(spa, v1)`** y por eso quedan fuera de este relevamiento: no puedo reportar un
   número que la fuente no publica.
2. **No existe un benchmark de retrieval-only en español.** En la lista completa de 76
   benchmarks registrados hay RTEB para inglés, alemán, francés, japonés y finés
   (`RTEB(eng, beta)`, `RTEB(deu, beta)`, `RTEB(fra, beta)`, `RTEB(jpn, beta)`,
   `RTEB(fin, beta)`), y no hay variante española. Por eso el único puntaje de
   retrieval en español disponible es la columna `Retr.` de `MTEB(spa, v1)`.
3. **Marca de contaminación por tarea.** El leaderboard pinta ⚠️ sobre celdas
   individuales, con este tooltip textual: *"Model lists this task in its training
   datasets — score is not zero-shot."* Tres de los cuatro candidatos la tienen sobre
   `MIRACLRetrievalHardNegatives.v2` (una de las 5 tareas de retrieval). El cuarto
   (jina v5) no la tiene en ninguna tarea, pero su columna "Zero-shot" es `⚠️ NA`,
   es decir: **no se sabe**, porque no declara sus datos de entrenamiento.
4. **La columna "Rank" no ordena por retrieval** sino por el agregado. Por eso abajo
   reporto dos posiciones distintas y las distingo.

---

## 3. Filtros aplicados

| Filtro declarado por la autora | Cómo lo apliqué |
|---|---|
| tarea RETRIEVAL | columna `Retr.` de `MTEB(spa, v1)`; descarto todo modelo sin valor ahí |
| español o multilingüe con español declarado | `MTEB(spa, v1)` + lista de idiomas de la model card (reporto por candidato si `es` figura o no) |
| corre local en laptop | ≤ ~1B parámetros (restricción M4 / MPS declarada por la autora) |
| licencia abierta, uso en investigación publicable | licencia del repo HF; marco explícitamente la no-comercial |

Aplicando los cuatro filtros sobre los 30 modelos con puntaje de retrieval quedan,
ordenados por `Retr.`: jina-v5-text-small (56.71), jina-v5-text-nano (56.32),
e5-large-instruct (51.74), F2LLM-v2-0.6B (51.34), e5-large (50.51), F2LLM-v2-330M
(49.73), bge-m3 (49.40), bekko-a25m (48.13), e5-base (46.45), y bajando.

Traigo **4 candidatos** (la familia jina v5 cuenta como uno, con sus dos tamaños,
porque comparten licencia, requisitos y protocolo de uso íntegramente). Los elegí
para cubrir el espacio de decisión, no por mérito: el mejor puntaje bajo licencia
no comercial (C1), el mejor bajo licencia permisiva (C2), el de trazabilidad de
entrenamiento más completa (C3), y el de ventana larga con más recorrido de uso (C4).

---

## 4. Tabla comparativa

Leyenda de fuente: **[LB]** = leaderboard MTEB · **[MC]** = model card / config del
autor en HuggingFace · **[med]** = medición mía sobre el listado de archivos de HF.

| | C1a jina-v5-text-small | C1b jina-v5-text-nano | C2 multilingual-e5-large-instruct | C3 F2LLM-v2-0.6B | C4 bge-m3 |
|---|---|---|---|---|---|
| id HuggingFace | `jinaai/jina-embeddings-v5-text-small` | `jinaai/jina-embeddings-v5-text-nano` | `intfloat/multilingual-e5-large-instruct` | `codefuse-ai/F2LLM-v2-0.6B` | `BAAI/bge-m3` |
| Rank en `MTEB(spa,v1)` (col. Rank, agregado) [LB] | #2 | #5 | #12 | #10 | #16 |
| Posición al ordenar por `Retr.` (30 modelos) [med sobre LB] | 7ª | 9ª | 12ª | 13ª | 16ª |
| **`Retr.` español** [LB] | **56.71** | **56.32** | **51.74** | **51.34** | **49.40** |
| Mean (Task) / Mean (TaskType) [LB] | 68.19 / 68.37 | 66.80 / 66.68 | 65.77 / 65.83 | 69.37 / 71.49 | 64.76 / 66.33 |
| Zero-shot [LB] | ⚠️ NA | ⚠️ NA | 87% | 75% | 87% |
| ⚠️ "entrenado en la tarea" sobre tareas de retrieval [LB] | ninguna | ninguna | sí, `MIRACLRetrievalHardNegatives.v2` | sí, `MIRACLRetrievalHardNegatives.v2` | sí, `MIRACLRetrievalHardNegatives.v2` |
| Openness [LB] | 3 de 6 | 3 de 6 | 4 de 6 | **6 de 6** | 5 de 6 |
| Parámetros [LB] | 596M | 212M | 560M | 596M | 568M |
| Parámetros [MC] | 677M | 239M | no declarado (dice "24 layers") | no declarado (nombre: 0.6B) | no declarado |
| Dimensión del vector [MC] | 1024 (Matryoshka 32–1024) | 768 (Matryoshka 32–768) | 1024 | 1024 | 1024 |
| Longitud máx. de secuencia [MC] | 32768 | 8192 (ver contradicción §5.1) | 512 | no declarada en la card; `config.json` 40960 | 8192 |
| **Pasajes de E0 truncados (de 1.763)** | **0** | **0** | **78** | **0** | **0** |
| Licencia | **CC-BY-NC-4.0** (no comercial) | **CC-BY-NC-4.0** (no comercial) | MIT | Apache-2.0 | MIT |
| Publicación | card: 18-feb-2026; repo HF creado 22-ene-2026 | card: 18-feb-2026; repo HF creado 22-ene-2026 | repo HF creado 08-feb-2024; paper arXiv 2402.05672 | repo HF creado 02-mar-2026; paper arXiv 2603.19223 | repo HF creado 27-ene-2024; paper arXiv 2402.03216 |
| `trust_remote_code` | **sí** | **sí** | no | no | no |
| Prefijo query ≠ prefijo doc | sí (`"Query: "` / `"Document: "`) | sí (`"Query: "` / `"Document: "`) | sí (instrucción en query, doc **sin** prefijo) | sí (instrucción en query, doc vacío) | **no** (sin prefijos) |
| Normalización exigida | no declarado | no declarado | sí (código de la card normaliza L2) | sí (código de la card normaliza L2) | no declarado |
| Versión mínima de librería [MC] | `transformers>=4.57.0`, `torch>=2.8.0`, `peft>=0.15.2` | ídem | no declarada | no declarada | no declarada |
| MPS / Apple Silicon en card o repo | **no mencionado** | **no mencionado** | **no mencionado** | **no mencionado** | **no mencionado** |
| Tiempo de indexación de 1.763 pasajes | no declarado en la fuente | no declarado en la fuente | no declarado en la fuente | no declarado en la fuente | no declarado en la fuente |
| Peso de los archivos de modelo [med] | 1,19 GB (`model.safetensors`, BF16) | no medido | 1,12 GB (`model.safetensors`, F16) | 1,19 GB (`model.safetensors`, BF16) | 2,27 GB (`pytorch_model.bin`, F32) |
| RAM/VRAM requerida | no declarada en la fuente | no declarada en la fuente | no declarada en la fuente | no declarada en la fuente | no declarada en la fuente |

### Desagregado por tarea de retrieval en español [LB]

| tarea | C1a small | C1b nano | C2 e5-l-instruct | C3 F2LLM-0.6B | C4 bge-m3 |
|---|---|---|---|---|---|
| MintakaRetrieval | 42.65 | 45.66 | 34.51 | 34.94 | 22.34 |
| MIRACLRetrievalHardNegatives.v2 | 56.83 | 55.95 | 54.14 ⚠️ | 51.68 ⚠️ | 57.27 ⚠️ |
| SpanishPassageRetrievalS2P | 49.47 | 50.97 | 42.63 | 35.83 | 44.02 |
| SpanishPassageRetrievalS2S | 75.42 | 71.89 | 71.49 | 74.18 | 70.37 |
| XPQARetrieval | 59.17 | 57.16 | 55.94 | 60.04 | 52.98 |

Lo señalo porque el agregado esconde dispersión: `SpanishPassageRetrievalS2P` —
consulta corta contra pasaje, que es la forma más parecida al caso de E0 — separa a
los candidatos de manera distinta al promedio (C4 le gana a C3 por 8,2 puntos ahí,
y le pierde por 1,9 en el agregado).

---

## 5. Fichas por candidato

### 5.1 C1 — familia `jina-embeddings-v5-text` (small y nano)

**Ids exactos:** `jinaai/jina-embeddings-v5-text-small`, `jinaai/jina-embeddings-v5-text-nano`.

**Puntajes [LB, `MTEB(spa, v1)`]** — small: Rank #2 del benchmark, `Retr.` **56.71**,
7ª al ordenar por `Retr.` entre los 30 modelos con ese puntaje, 1ª entre los abiertos
de ≤1B. nano: Rank #5, `Retr.` **56.32**, 9ª. Ambos con `Rerank` (MIRACLReranking)
64.58 y 63.73. Columna Zero-shot: **`⚠️ NA`** en ambos.

**Parámetros — dato en conflicto entre fuentes.** [LB] dice 596M (small) y 212M (nano).
[MC] dice "Parameters | 677M" y "239M". El listado de archivos [med] da un
`model.safetensors` de 1.192.133.208 bytes para small, consistente con ~596M
parámetros en BF16. No resuelvo la discrepancia: la reporto.

**Dimensión del vector [MC]:** small 1024 (Matryoshka 32/64/128/256/512/768/1024);
nano 768 (Matryoshka 32/64/128/256/512/768). Pooling: last-token.

**Base [MC]:** small sobre `Qwen/Qwen3-0.6B-Base`; nano sobre `EuroBERT/EuroBERT-210m`.

**Licencia:** `cc-by-nc-4.0`. Cita textual de la card: *"jina-embeddings-v5-text-small
is licensed under CC BY-NC 4.0. For commercial use, please contact us."* Es abierta y
sirve para investigación publicable; **no** habilita uso comercial. Lo marco porque es
el único candidato con esa restricción.

**Publicación [MC]:** *"released on February 18, 2026"*. Repo HF creado 2026-01-22,
última modificación 2026-04-15. Paper: arXiv 2602.15547.

**Idioma:** el frontmatter declara sólo `multilingual` (sin lista de idiomas). La card
afirma *"it supports 119+ languages"* (small). **El español no aparece enumerado
explícitamente en la card**; el respaldo de español es el puntaje en `MTEB(spa, v1)`.

**Detalles de uso [MC]:**
- Prefijos **asimétricos**: `config_sentence_transformers.json` declara
  `prompts: {"query": "Query: ", "document": "Document: "}`, con
  `default_prompt_name: "document"`. En la API de la card se pasa además
  `task="retrieval"` y `prompt_name="query"` / `prompt_name="document"`.
- `trust_remote_code=True` **obligatorio** (el `config.json` mapea `AutoModel` a
  `modeling_jina_embeddings_v5.JinaEmbeddingsV5Model`).
- Versiones mínimas declaradas: `transformers>=4.57.0`, `torch>=2.8.0`, `peft>=0.15.2`.
  `flash-attention` "recommended but not mandatory"; `sentence-transformers` opcional.
- Normalización de vectores: **no declarado**. `similarity_fn_name: "cosine"`.
- Advertencias de los autores: `dtype=torch.bfloat16` viene comentado como
  *"Recommended for GPUs"*; el código de ejemplo selecciona dispositivo con
  `torch.device("cuda" if torch.cuda.is_available() else "cpu")` — es decir, **cae a
  CPU, no a MPS**, salvo que se cambie a mano. La card no menciona MPS ni Apple Silicon.
- Existen variantes por tarea con el adapter fusionado (`...-text-small-retrieval`, etc.)
  para vLLM / TEI / ONNX.

**Longitud máxima y truncamiento sobre E0:**
- small: 32768 [MC y `config.json` `max_position_embeddings: 32768`]. Máximo de E0
  ~6.500 tokens → **0 de 1.763 pasajes truncados**.
- nano: **contradicción interna de la card**. La tabla dice
  `Max Sequence Length | 8192` y el `config.json` dice `max_position_embeddings: 8192`,
  pero la prosa afirma *"supports multilingual text up to 32K tokens"*. Con 8192 —
  el valor de la tabla y del config — igual son **0 de 1.763 truncados**.

**Tiempo de indexación de 1.763 pasajes:** no declarado en la fuente.
**RAM/VRAM:** no declarada en la fuente. Archivo de pesos: 1,19 GB (BF16) [med].

---

### 5.2 C2 — `intfloat/multilingual-e5-large-instruct`

**Id exacto:** `intfloat/multilingual-e5-large-instruct`.

**Puntajes [LB, `MTEB(spa, v1)`]:** Rank #12 del benchmark, `Retr.` **51.74**, 12ª al
ordenar por `Retr.`. `Rerank` 53.13 (el más bajo de los cuatro candidatos).
Zero-shot 87%. ⚠️ "entrenado en la tarea" sobre `MIRACLRetrievalHardNegatives.v2`
(54.14) y sobre `MIRACLReranking`.

**Parámetros:** 560M [LB]; el `model.safetensors` declara 559.890.432 parámetros en F16
[med]. La card **no** da cifra de parámetros: dice *"This model has 24 layers and the
embedding size is 1024."*

**Dimensión del vector [MC]:** 1024.

**Licencia:** `mit` (frontmatter del repo). Sin restricción de uso.

**Publicación:** repo HF creado 2024-02-08, última modificación 2025-07-10 [med, API HF].
La card no declara fecha; el paper asociado es arXiv 2402.05672 (2024).

**Idioma:** el frontmatter enumera 93 códigos de idioma (más la etiqueta `multilingual`)
y **`es` figura explícitamente**.
La card: *"It supports 100 languages from xlm-roberta, but low-resource languages may
see performance degradation."* Inicializado desde `xlm-roberta-large`.

**Detalles de uso [MC]:**
- Prefijos **asimétricos y obligatorios**. Query:
  `f'Instruct: {task_description}\nQuery: {query}'`, con `task_description` una
  instrucción de una oración, p. ej. *"Given a web search query, retrieve relevant
  passages that answer the query"*. Documento: **sin prefijo**. Cita textual del FAQ:
  *"Yes, this is how the model is trained, otherwise you will see a performance
  degradation. […] On the other hand, there is no need to add instructions to the
  document side."*
- Normalización: **sí**, el código de la card la aplica —
  `F.normalize(embeddings, p=2, dim=1)` en la vía `transformers`, y
  `normalize_embeddings=True` en la vía `sentence-transformers`.
- `trust_remote_code`: no se usa (arquitectura `XLMRobertaModel` nativa).
- Versión mínima de librería: **no declarada**. El `config_sentence_transformers.json`
  registra que fue guardado con `sentence_transformers 2.4.0.dev0` / `transformers 4.37.0`
  (eso es la versión de guardado, no un mínimo declarado).
- Advertencias de los autores: sección *Limitations* — *"Long texts will be truncated to
  at most 512 tokens."* Y FAQ 3: la similitud coseno se distribuye entre 0.7 y 1.0 por
  la temperatura 0.01 de InfoNCE, *"what matters is the relative order of the scores
  instead of the absolute values"*. Relevante si se piensa fijar un umbral absoluto.

**Longitud máxima y truncamiento sobre E0:** **512** tokens (card, y `config.json`
`max_position_embeddings: 514` → 512 útiles). Contra la distribución declarada de E0
(mediana ~80, p90 ~310, p99 ~1.165, máx ~6.500), **se truncarían los 78 pasajes que la
autora declara por encima de ~512 tokens**, es decir 4,4% del corpus; el peor caso
pierde ~92% de su contenido (6.500 → 512). Es el único de los cuatro que trunca.

**Tiempo de indexación de 1.763 pasajes:** no declarado en la fuente.
**RAM/VRAM:** no declarada en la fuente. Archivo de pesos: 1,12 GB (F16) [med].

---

### 5.3 C3 — `codefuse-ai/F2LLM-v2-0.6B`

**Id exacto:** `codefuse-ai/F2LLM-v2-0.6B`.

**Puntajes [LB, `MTEB(spa, v1)`]:** Rank #10 del benchmark, `Retr.` **51.34**, 13ª al
ordenar por `Retr.`. `Rerank` 61.19. Zero-shot 75%. Openness **6 de 6 dimensiones**
(la más alta de la tabla). ⚠️ "entrenado en la tarea" sobre
`MIRACLRetrievalHardNegatives.v2` (51.68), `MIRACLReranking`, `STS22` y `XNLI`.

Es la escala más chica de una familia cuyas escalas grandes dominan el retrieval
español del leaderboard: 14B → 60.98 (2ª), 8B → 59.94, 4B → 58.63, 1.7B → 55.19.
Las tres escalas menores (80M/160M/330M) son, según la card, *"pruned and trained from
the 0.6B base model"*.

**Parámetros:** 596M [LB]; `model.safetensors` declara 596.049.920 en BF16 [med].
La card no da cifra explícita más allá del nombre. Arquitectura `Qwen3Model`,
28 capas, `hidden_size` 1024.

**Dimensión del vector [MC]:** 1024 (la salida del ejemplo es `(1024,)`).
Pooling: última posición no-pad (EOS).

**Licencia:** `apache-2.0`. Sin restricción de uso.

**Publicación:** repo HF creado 2026-03-02, última modificación 2026-07-31 [med, API HF].
Paper: arXiv 2603.19223 (2026). La card no declara fecha de release en prosa.

**Idioma:** el frontmatter enumera 87 idiomas y **`es` figura explícitamente**
(cuarto de la lista). La card: *"supports more than 200 languages, with a particular
emphasis on previously underserved mid- and low-resource languages."*

**Apertura declarada [MC]:** *"F2LLM-v2 is fully open. We release base models in 5 sizes,
instruct models in 8 sizes, the training data, the training code, and intermediate
checkpoints."* Los checkpoints intermedios están en la rama `intermediate_checkpoints`.
Es lo que sostiene el Openness 6/6 del leaderboard.

**Detalles de uso [MC]:**
- Prefijos **asimétricos**. `config_sentence_transformers.json` declara
  `prompts: {"query": "Instruct: Given a question, retrieve passages that can help
  answer the question.\nQuery: ", "document": ""}` — documento **sin** prefijo.
  Con `sentence-transformers` se usan `model.encode_query()` / `model.encode_document()`.
- Instrucciones personalizables, formato declarado: `Instruct: your_instruction\nQuery:`.
  Regla textual: *"for retrieval and reranking tasks: use the prompt for queries; do not
  prepend the prompt to documents/passages"*. Para tareas simétricas (STS, clustering,
  bitext) *"you can encode the documents either with or without prompts"*.
- Normalización: **sí**, el código de la card aplica `F.normalize(embeddings, p=2, dim=1)`.
  `similarity_fn_name: "cosine"`.
- `trust_remote_code`: no se usa.
- Versión mínima de librería: **no declarada**. El `config.json` registra
  `transformers_version: "4.51.0"` (versión de guardado, no un mínimo declarado);
  como la arquitectura es `Qwen3Model`, hace falta un `transformers` que la soporte.
- Advertencias de los autores: el ejemplo fija `torch_dtype=torch.bfloat16` y
  `device="cuda:0"` / `device_map={'': 0}` — **el código de la card asume CUDA de forma
  explícita** y habría que reescribir esa línea para MPS. La card no menciona MPS ni
  Apple Silicon.

**Longitud máxima y truncamiento sobre E0:** la card **no declara** longitud máxima.
El `config.json` da `max_position_embeddings: 40960` y el `tokenizer_config.json` da
`model_max_length: 131072`. Con cualquiera de los dos, **0 de 1.763 pasajes truncados**.

**Tiempo de indexación de 1.763 pasajes:** no declarado en la fuente.
**RAM/VRAM:** no declarada en la fuente. Archivo de pesos: 1,19 GB (BF16) [med].

---

### 5.4 C4 — `BAAI/bge-m3`

**Id exacto:** `BAAI/bge-m3`.

**Puntajes [LB, `MTEB(spa, v1)`]:** Rank #16 del benchmark, `Retr.` **49.40**, 16ª al
ordenar por `Retr.`. `Rerank` **63.97** (el más alto de los cuatro candidatos, y 6º entre
los 151 modelos con puntaje de reranking en este benchmark). Zero-shot 87%. Openness 5 de 6. ⚠️ "entrenado en la tarea" sobre
`MIRACLRetrievalHardNegatives.v2` (57.27 — su mejor tarea de retrieval, y la más alta
de los cuatro candidatos en esa tarea) y sobre `MIRACLReranking`.

Perfil desparejo: es el mejor de los cuatro en `MIRACLRetrievalHardNegatives.v2` (57.27,
marcada como no zero-shot) y el peor por lejos en `MintakaRetrieval` (22.34, contra
42.65 de C1a).

**Parámetros:** 568M [LB]. **La card no declara cantidad de parámetros** y el repo no
publica `safetensors` con metadatos de conteo — sólo `pytorch_model.bin` de 2,27 GB en
F32 [med]. Arquitectura `XLMRobertaModel`, 24 capas, `hidden_size` 1024.

**Dimensión del vector [MC]:** 1024 (tabla de la card: `bge-m3 | 1024 | 8192`).

**Licencia:** `mit` (frontmatter del repo). Sin restricción de uso.

**Publicación:** repo HF creado 2024-01-27, última modificación 2024-07-03 [med, API HF].
Es el más antiguo de los cuatro y el que hace más tiempo no se actualiza.
Paper: arXiv 2402.03216.

**Idioma:** el frontmatter **no** enumera idiomas. La card afirma *"It can support more
than 100 working languages"* pero **no los lista**, así que el español **no está
declarado nominalmente en la model card**; el respaldo es el puntaje en `MTEB(spa, v1)`.
Base: `xlm-roberta`, extendido a 8192 posiciones vía RetroMAE.

**Detalles de uso [MC]:**
- Prefijos: **ninguno**, y es simétrico. Cita textual del FAQ: *"The only difference is
  that the BGE-M3 model no longer requires adding instructions to the queries."*
  Es el único de los cuatro sin prefijos, lo que simplifica el pipeline.
- Normalización: **no declarado** explícitamente en la card (no hay mención de
  `normalize` en el README).
- `trust_remote_code`: no se usa.
- Versión mínima de librería: **no declarada**. La vía recomendada es
  `pip install -U FlagEmbedding` y `BGEM3FlagModel`, sin pin de versión.
  `config_sentence_transformers.json` registra guardado con ST 2.2.2 / transformers 4.33.0.
- Salida multi-función: dense (`dense_vecs`), sparse (lexical weights) y multi-vector
  (ColBERT) en una sola pasada. Para un índice denso se toma `['dense_vecs']`.
- Advertencias de los autores: *"Setting use_fp16 to True speeds up computation with a
  slight performance degradation"*; sobre `max_passage_length`, *"a smaller max length
  leads to a lower latency"*. Recomendación de pipeline: *"hybrid retrieval +
  re-ranking"*. La card no menciona MPS ni Apple Silicon, y el README del repo
  `FlagOpen/FlagEmbedding` tampoco (grep sobre `mps`/`apple silicon`/`metal`/`macos`:
  cero coincidencias).

**Longitud máxima y truncamiento sobre E0:** **8192** tokens
(`sentence_bert_config.json`: `"max_seq_length": 8192`; `config.json`:
`max_position_embeddings: 8194`; card: *"up to 8192 tokens"*). Máximo de E0 ~6.500 →
**0 de 1.763 pasajes truncados**. Nota de la card: bajar `max_length` acelera el
encoding, y el default de algunos ejemplos es menor a 8192 — hay que fijarlo a mano.

**Tiempo de indexación de 1.763 pasajes:** no declarado en la fuente.
**RAM/VRAM:** no declarada en la fuente. Archivo de pesos: 2,27 GB (F32) [med] — el
doble que los otros tres, por estar publicado sin cuantizar.

---

## 6. Cinco salvedades que condicionan cualquier laudo sobre esta tabla

1. **El conteo de truncamiento arrastra un tokenizador no declarado.** Las cifras de E0
   (mediana ~80, p90 ~310, p99 ~1.165, máx ~6.500; 78 chunks sobre ~512) vienen del
   mandato y no dicen con qué tokenizador se midieron. C2 y C4 usan el SentencePiece de
   XLM-R (vocab 250.002); C1a y C3 usan el BPE de Qwen (vocab 151.936); C1b usa el de
   EuroBERT. **Los tres dan conteos distintos sobre el mismo texto**, y para español
   técnico la diferencia no es despreciable. El "78 pasajes truncados" de C2 es el número
   de la autora, no un número medido con el tokenizador de C2. Si esa cifra va a decidir
   el laudo, conviene recontarla con `AutoTokenizer` de cada candidato — es gratis y local.
2. **Ningún candidato documenta MPS/Apple Silicon**, ni en su model card ni en el README
   de su repo upstream. Dos de ellos (C1, C3) traen código de ejemplo que asume CUDA
   explícitamente. No infiero de ahí que no funcionen en MPS: infiero que **la fuente no
   lo declara**, y que el soporte habría que verificarlo empíricamente.
3. **Ninguna fuente publica tiempo de indexación** para ningún tamaño de corpus. No hay
   dato que reportar sobre los 1.763 pasajes, y no lo estimo.
4. **Tres de los cuatro candidatos tienen contaminación declarada** en una de las cinco
   tareas de retrieval (`MIRACLRetrievalHardNegatives.v2`). El cuarto (C1) no tiene la
   marca, pero su Zero-shot es `NA` porque no declara datos de entrenamiento — ausencia
   de marca no es evidencia de limpieza. Si la autora quiere un puntaje sin sospecha de
   contaminación, la comparación honesta es sobre las cuatro tareas restantes, y ahí el
   orden entre C2/C3/C4 cambia (ver desagregado en §4).
5. **El leaderboard es un proxy, no el experimento.** Ninguna de las 5 tareas de
   `MTEB(spa, v1)` es texto regulatorio: son preguntas Wikidata (Mintaka), pasajes
   multilingües (MIRACL), pasajes en español general (SpanishPassageRetrieval) y QA de
   producto (XPQA). Las diferencias de 2–5 puntos entre C1/C2/C3/C4 no son
   necesariamente transferibles a los TO del BCRA.

---

## 7. Archivos de evidencia (todos en el scratchpad de la sesión)

| archivo | qué es |
|---|---|
| `mteb_snapshot/mteb_spa_v1_ranking_por_retr.tsv` | los 30 modelos de `MTEB(spa,v1)` con puntaje de retrieval, ordenados por `Retr.` |
| `mteb_snapshot/mteb_spa_v1_pertask_candidatos.tsv` | desagregado por las 5 tareas de retrieval + verificación aritmética de la columna `Retr.` |
| `mteb_snapshot/<org>_<modelo>_README.md` | model cards crudas descargadas de HF (5 modelos) |
| `mteb_snapshot/<org>_<modelo>_config.json` | `config.json` crudos (longitud máxima, hidden size, arquitectura) |
| `mteb_snapshot/<org>_<modelo>_config_sentence_transformers.json` | prompts de query/documento declarados por los autores |
| `mteb_snapshot/<org>_<modelo>_sentence_bert_config.json` | `max_seq_length` donde el autor lo publica |
| `mteb_snapshot/flagembedding_README.md`, `unilm_e5_README.md`, `f2llm_gh_README.md` | READMEs de los repos upstream, usados para el grep de MPS/Apple Silicon |

Comandos que reproducen las descargas:

```bash
curl -sSL "https://huggingface.co/<id>/raw/main/README.md"
curl -sSL "https://huggingface.co/<id>/raw/main/config.json"
curl -sS  "https://huggingface.co/api/models/<id>"
curl -sS  "https://huggingface.co/api/models/<id>/tree/main"
```

El leaderboard no se reproduce con `curl`: requiere navegador con JS sobre
`https://mteb-leaderboard.hf.space/benchmark/MTEB(spa%2C%20v1)`.

La ampliación de §8 agrega el directorio `mteb_snapshot_multi/`; su inventario está
en §8.8.

---

## 8. AMPLIACIÓN — candidatos fuertes que el subconjunto español no cubre

Ampliación de la misma unidad, pedida después de la primera entrega. Motivo: en §2
quedó registrado que modelos como `Qwen/Qwen3-Embedding-0.6B` salieron del
relevamiento **por falta de dato, no por desempeño**. Esta sección los recupera
mirando el benchmark multilingüe general. Costo de API: USD 0.

### 8.1 Método y snapshot

Mismo método declarado en §1: el Space no es legible de forma estática, así que
cargué la aplicación en un navegador real y extraje el DOM celda por celda.

- URL exacta leída: `https://mteb-leaderboard.hf.space/benchmark/MTEB(Multilingual%2C%20v2)`
- Pestañas usadas: `SUMMARY`, `PERFORMANCE PER TASK`, `PERFORMANCE PER LANGUAGE`
- URL de contraste (para verificar la ausencia de fila española):
  `https://mteb-leaderboard.hf.space/benchmark/MTEB(spa%2C%20v1)`

**Ventana del snapshot de la ampliación: 2026-08-19, 17:21–17:37 EDT
(21:21–21:37 UTC).** Es un snapshot distinto y posterior al de §1 (2026-08-18);
los números de §2–§7 NO se re-leyeron y siguen siendo los del 18 de agosto.

Las model cards de los candidatos nuevos se descargaron el 2026-08-19 con
`curl -sSL https://huggingface.co/<id>/raw/main/README.md` y quedaron en
`mteb_snapshot_multi/`.

### 8.2 Qué es el benchmark multilingüe y qué mide su columna `Retr.`

Nombre exacto: **`MTEB(Multilingual, v2)`**, rotulado "Multilingual" en el
leaderboard. Descripción textual de la propia página:

> "MMTEB measures multilingual text embedding quality across 250+ languages spanning
> classification, clustering, retrieval semantic similarity and more, driven by
> curated community contributions."

Metadatos que declara la página: LANGUAGES 1037 · TASKS 131 · TASK TYPES 9 ·
MODELS 85. La tabla lista **446 filas de modelo**, de las cuales **177 tienen valor
en la columna `Retr.`**.

**La columna `Retr.` es el promedio de 18 tareas de retrieval**, que enumero completas
en `mteb_snapshot_multi/mmteb_v2_retr_18_tareas.tsv`: `AILAStatutes`, `ArguAna`,
`BelebeleRetrieval`, `CovidRetrieval`, `HagridRetrieval`,
`LegalBenchCorporateLobbying`, `LEMBPasskeyRetrieval`,
`MIRACLRetrievalHardNegatives`, `MLQARetrieval`, `SCIDOCS`, `SpartQA`,
`StackOverflowQA`, `StatcanDialogueDatasetRetrieval`, `TempReasonL1`, `TRECCOVID`,
`TwitterHjerneRetrieval`, `WikipediaRetrievalMultilingual`, `WinoGrande`.

**Verificación mía** (no dato del leaderboard, igual que en §2): calculé la media
simple de esas 18 columnas para los 9 candidatos y reproduce la columna `Retr.`
al centésimo en 8 de 9; el noveno (`arctic-embed-m-v2.0`) da 54.835 contra 54.83
publicado, diferencia de redondeo de 0,01. Cálculo reproducible en
`mteb_snapshot_multi/mmteb_v2_retr_18_tareas.tsv` + la tabla de §8.4.

**Confirmación independiente desde una model card:** la card de
`granite-embedding-311m-multilingual-r2` afirma textualmente *"scores **65.2** on
Multilingual MTEB Retrieval (18 tasks)"* — coincide con el 65.21 que leí en el
leaderboard, y confirma por una segunda fuente que son 18 tareas.

**Advertencia que hay que tener presente y que el leaderboard no señala:
ninguna de esas 18 tareas es específica del español.** Cuatro de ellas son
multilingües y contienen español entre sus idiomas (`BelebeleRetrieval`,
`MLQARetrieval`, `MIRACLRetrievalHardNegatives`, `WikipediaRetrievalMultilingual`),
las otras catorce son monolingües en inglés o de dominio (legal, código,
biomédico, razonamiento). **El `Retr.` de esta sección NO es un puntaje de
retrieval en español**: es un puntaje de retrieval multilingüe agregado. Esa es la
diferencia central con la columna `Retr.` de §2, y es la razón por la que esta
sección amplía el relevamiento pero no lo reemplaza.

### 8.3 Filtros aplicados y qué quedó afuera

Los cuatro criterios pedidos, y cómo los apliqué:

| criterio | cómo lo apliqué |
|---|---|
| licencia permisiva (Apache/MIT o equivalente, NO CC-BY-NC) | campo `license` del repo HF vía `https://huggingface.co/api/models/<id>` |
| ≤1B parámetros | columna `Parameters` del leaderboard, contrastada con el conteo de `safetensors` de la API de HF |
| ventana ≥8.192 tokens | longitud declarada por el autor (model card / `sentence_bert_config.json` / `config.json`), en ese orden de prioridad |
| sin fila de retrieval en `MTEB(spa, v1)` | verificado modelo por modelo sobre la tabla del benchmark español (celda `Retr.` vacía o modelo ausente) |

De los 123 modelos ≤1B con puntaje de retrieval multilingüe, **9 pasan los cuatro
filtros**. Los que quedaron afuera y por qué están en
`mteb_snapshot_multi/mmteb_v2_excluidos_con_motivo.tsv`; destaco los tres casos que
me parecen importantes para que no se relean como omisiones:

- **`google/embeddinggemma-300m`** (308M, `Retr.` 62.49) — **excluido por licencia**:
  el campo `license` del repo dice `gemma`, no Apache ni MIT. Son los términos
  propios de Google, con restricciones de uso; no es una licencia permisiva en el
  sentido del criterio. Lo nombro explícitamente porque por puntaje y tamaño habría
  entrado, y la exclusión es jurídica, no técnica.
- **`jinaai/jina-embeddings-v3`** (572M, `Retr.` 55.76) — excluido por `cc-by-nc-4.0`,
  igual que la familia v5 de §5.1.
- **La familia `BidirLM` (270M / 0.6B / 1B, `Retr.` 54.59 / 59.06 / 61.61)** —
  excluidos por ventana. Acá hubo un conflicto entre fuentes que resolví con la
  fuente del autor: el `config.json` declara `max_position_embeddings` de 32768–40960
  (herencia de los modelos base Gemma3 y Qwen3), pero **la tabla de la propia model
  card declara `512`** para las cinco escalas, y el `sentence_bert_config.json`
  también dice `"max_seq_length": 512`. Mando la card. Mismo caso con
  `nomic-embed-text-v2-moe` y las dos `KaLM-embedding-multilingual-mini` (512 según
  `sentence_bert_config.json`; la card de KaLM no lo declara).

### 8.4 Los 9 candidatos

Leyenda de fuente igual que en §4: **[LB]** = leaderboard · **[MC]** = model card /
config del autor · **[med]** = medición o cálculo mío.

Todos: `Retr.` de `MTEB(Multilingual, v2)`, snapshot 2026-08-19 17:21–17:37 EDT.
Ninguno tiene fila de retrieval en `MTEB(spa, v1)` [LB, verificado uno por uno].

| # | modelo | `Retr.` [LB] | pos. por `Retr.` (de 177) [med] | Rank col. del LB | params [LB] | dim | ventana declarada [MC] | licencia | ⚠️ contaminación | español declarado en la card |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `geevec-ai/geevec-embeddings-1.0-lite` | **70.91** | 5ª | #233 | 366M | 1024 (card: "hasta 4096") | 32.768 | apache-2.0 | **0 tareas** | **no declarado** |
| 2 | `microsoft/harrier-oss-v1-0.6b` | **70.75** | 7ª | #10 | 596M | 1024 | 32.768 | mit | **28 tareas**, 5 de ellas de retrieval | **sí, "Spanish"** |
| 3 | `microsoft/harrier-oss-v1-270m` | 66.38 | 15ª | #17 | 268M | 640 | 32.768 | mit | **28 tareas**, 5 de ellas de retrieval | **sí, "Spanish"** |
| 4 | `perplexity-ai/pplx-embed-v1-0.6b` | 65.41 | 19ª | #237 | 596M | 1024 | 32K | mit | 1 tarea (retrieval) | **no declarado** |
| 5 | `ibm-granite/granite-embedding-311m-multilingual-r2` | 65.21 | 20ª | #71 | 312M | 768 | 32.768 | apache-2.0 | 5 tareas, **las 5 de retrieval** | **sí, "Spanish (es)"** |
| 6 | `Qwen/Qwen3-Embedding-0.6B` | 64.65 | 24ª | #18 | 596M | 1024 | 32k | apache-2.0 | 1 tarea (retrieval) | **no declarado** |
| 7 | `ibm-granite/granite-embedding-97m-multilingual-r2` | 60.32 | 38ª | #86 | 97M | 384 | 32.768 | apache-2.0 | 5 tareas, **las 5 de retrieval** | **sí, "Spanish (es)"** |
| 8 | `Snowflake/snowflake-arctic-embed-l-v2.0` | 58.36 | 48ª | #61 | 568M | 1024 | 8.192 | apache-2.0 | 1 tarea (retrieval) | **sí** (frontmatter, 74 idiomas) |
| 9 | `Snowflake/snowflake-arctic-embed-m-v2.0` | 54.83 | 65ª | #74 | 305M | 768 | 8.192 | apache-2.0 | 1 tarea (retrieval) | **sí** (frontmatter, 74 idiomas) |

Para comparar: los cuatro candidatos de §5 en esta misma columna `Retr.` de
`MTEB(Multilingual, v2)` dan `jina-v5-text-small` 64.88 (22ª),
`jina-v5-text-nano` 63.26 (29ª), `F2LLM-v2-0.6B` 59.30 (43ª),
`multilingual-e5-large-instruct` 57.11 (55ª) y `bge-m3` 54.59 (66ª). Es decir:
**los candidatos 1 a 6 de esta sección quedan por encima del mejor candidato de §5
en retrieval multilingüe** — que es exactamente el sesgo que la ampliación buscaba
detectar. Con la salvedad de 8.2: es retrieval multilingüe, no retrieval español.

Sobre la columna "Rank" del leaderboard: `geevec-lite` (#233) y `pplx-embed`
(#237) tienen ranking muy bajo porque **corrieron sólo 18 de las 131 tareas** — las
18 de retrieval, ninguna otra. Su `Retr.` es por lo tanto plenamente comparable
(mismas 18 tareas que todos los demás, lo verifiqué), pero **no tienen agregado
general** y su posición en la columna Rank no significa nada sobre su calidad.
Los otros siete corrieron las 131 tareas (`arctic-m-v2.0`, 130).

### 8.5 Notas por candidato

**1. `geevec-ai/geevec-embeddings-1.0-lite`** — apache-2.0 [API HF]. Repo creado
2026-04-02, modificado 2026-07-24 [med]. Card: *"Total Parameters: 349M activated /
366M total"*, *"Context Length: 32,768"*, *"Embedding dimension: Up to 4096, supports
user-defined output dimensions ranging from 256 to 4096"* — el `config.json` da
`hidden_size: 1024`, así que **card y config no coinciden en la dimensión**; reporto
las dos. Arquitectura `Qwen3PseudoMoEModelModel`. La card **cita su propio 70.91 en
"MMTEB(Multilingual, v2) retrieval task ... (as of 2026/04/02)"**, que coincide con
lo que leí. Uso: `trust_remote_code=True`, vía `FlagEmbedding` con
`query_instruction_format="Instruct: {}\nQuery: {}"` y ruteo de dominio
(`general`/`coding`/`reasoning`). Idiomas: el frontmatter **no** los enumera; la card
sólo dice *"general-purpose multilingual retrieval"*. **Español no declarado en la
fuente.** Contaminación: 0 tareas marcadas.

**2 y 3. `microsoft/harrier-oss-v1-0.6b` y `-270m`** — mit [API HF]. Repos creados
2026-03-30. Card: tabla propia con `270m | 640 dim | 32.768 tokens | MTEB v2 69.0/66.5`.
Español **declarado nominalmente**: *"including but not limited to: Arabic, Bulgarian,
Catalan, Czech, Danish, German, Greek, English, **Spanish**, …"*. Uso: pooling de
último token y **normalización L2 automática con Sentence Transformers**; prompts
preconfigurados (`web_search_query`, `sts_query`, `bitext_query`) y formato
`Instruct: {task}\nQuery: {query}`; documentos sin instrucción. La card fija
`max_length = 32768` en su ejemplo. **Es el candidato con más contaminación
declarada de los nueve: 28 tareas marcadas**, de las cuales **5 pertenecen a las 18
de retrieval** (`MIRACLRetrievalHardNegatives`, `SpartQA`,
`StatcanDialogueDatasetRetrieval`, `TempReasonL1`, `WinoGrande`); las otras 23 son de
clasificación, STS y bitext. Zero-shot [LB]: 78%, el más bajo de los nueve.

**4. `perplexity-ai/pplx-embed-v1-0.6b`** — mit [API HF]. Repo creado 2026-01-14,
modificado 2026-06-02. Card: `1024` dimensiones, contexto `32K`, pooling `Mean`,
columna "Instruction: **No**". **Advertencia fuerte y textual de los autores:**
*"`pplx-embed-v1` and `pplx-embed-context-v1` natively produce *unnormalized*
int8-quantized embeddings. Ensure that you compare them via *cosine similarity*."*
Y una decisión de diseño declarada: *"We deliberately **avoid** this requirement:
you can embed the text you want to index directly, without having to choose or
maintain an instruction prefix."* Idiomas: el frontmatter dice sólo
`language: - multilingual`. **Español no declarado en la fuente.** Contaminación:
1 tarea (`MIRACLRetrievalHardNegatives`).

**5 y 7. `ibm-granite/granite-embedding-{311m,97m}-multilingual-r2`** — apache-2.0
[API HF]. Repos creados 2026-04-20, modificados 2026-05-18. Card: *"768-dimensional
vectors with a context length of up to 32,768 tokens"* (311m) y *"384-dimensional …
32,768"* (97m); `sentence_bert_config.json` confirma `"max_seq_length": 32768`, el
único par de los nueve donde la ventana está declarada en las dos fuentes.
Español **declarado nominalmente** dentro de los 52 idiomas de soporte reforzado:
*"… Slovenian (sl), **Spanish (es)**, Swahili (sw), …"*; la card distingue
*"supports **200+ languages** (based on the multilingual pretraining corpus)"* de
esos 52 *"that receive explicit retrieval-pair and cross-lingual training"*.
Matryoshka: 768/512/384/256/128 (311m). Normalización L2 en el código de la card.
Advertencia de los autores: *"Longer texts will be truncated to the 32,768-token
context limit"* y *"Performance varies across languages"*. Contaminación: 5 tareas, y
**las 5 pertenecen a las 18 de retrieval** (`MIRACLRetrievalHardNegatives`, `SpartQA`,
`StatcanDialogueDatasetRetrieval`, `TempReasonL1`, `WinoGrande`). Es decir: 5 de los
18 sumandos de su `Retr.` están marcados como no zero-shot — la proporción más alta
de los nueve, empatada con harrier en cantidad pero sobre un total de marcas mucho
menor.

**6. `Qwen/Qwen3-Embedding-0.6B`** — apache-2.0 [API HF]. Repo creado 2025-06-03,
modificado 2026-04-20. Card: *"Supported Languages: 100+ Languages"*,
*"Context Length: 32k"*, *"Embedding Dimension: Up to 1024, supports user-defined
output dimensions ranging from 32 to 1024"*. **Los 100+ idiomas no se enumeran:
español no declarado nominalmente en la fuente.** Uso:
`config_sentence_transformers.json` declara `prompts: {"query": "Instruct: Given a
web search query, retrieve relevant passages that answer the query\nQuery:",
"document": ""}` — asimétrico, documento sin prefijo. Advertencias de los autores:
*"not using an `instruct` on the query side can lead to a drop in retrieval
performance by approximately 1% to 5%"* y *"we also advise users to write their
instructions in English, as most instructions utilized during the model training
process were originally written in English"* — lo segundo importa para un corpus en
castellano. Contaminación: 1 tarea (`MIRACLRetrievalHardNegatives`).

**8 y 9. `Snowflake/snowflake-arctic-embed-{l,m}-v2.0`** — apache-2.0 [API HF].
Repos creados 2024-11-08. Son los dos más antiguos de esta sección y los dos de
ventana más chica: **8.192**, y la card explica de dónde sale —
*"arctic-embed-l-v2.0 builds on BAAI/bge-m3-retromae which can support a context
window of up to 8192 via the use of RoPE"* (la `m` se apoya en
`Alibaba-NLP/gte-multilingual-base`). Dimensiones 1024 y 768. Español declarado en
el frontmatter (74 idiomas, `es` incluido) [MC]. Uso: prefijo **sólo en la query**
(`query_prefix = 'query: '`, documentos sin prefijo), normalización L2 explícita en
el código, `max_length=8192` en el tokenizer; **la `m-v2.0` requiere
`trust_remote_code=True`** (arquitectura `GteModel`), la `l-v2.0` no lo usa en el
código de la card. MRL a 256 dimensiones. Contaminación: 1 tarea cada una.

Sobre la ventana y el corpus de E0: los nueve tienen ventana ≥8.192 y el máximo de E0
es ~6.500 tokens, así que **ninguno truncaría pasajes** — con la misma salvedad del
tokenizador que planteé en §6.1.

### 8.6 Hallazgo lateral: la columna "Spanish" del benchmark multilingüe

La pestaña `PERFORMANCE PER LANGUAGE` de `MTEB(Multilingual, v2)` tiene una columna
**`Spanish`** con valor para 285 modelos — incluidos los nueve de esta sección, que
no tienen fila de retrieval en `MTEB(spa, v1)`. Los valores están en
`mteb_snapshot_multi/mmteb_v2_candidatos_sin_fila_spa.tsv`. Los extremos entre los
nueve: `harrier-oss-v1-0.6b` 92.34 (6ª de 285) y `granite-97m-r2` 54.86 (143ª).

**No la uso como puntaje de retrieval en español, y recomiendo no leerla así.**
Dos razones, ambas verificables:

1. **El leaderboard no declara qué agrega esa columna.** A diferencia de las columnas
   por tipo de tarea, el encabezado `Spanish` no trae tooltip explicativo; inspeccioné
   su HTML y sólo contiene el rótulo. No hay fuente que diga si promedia todas las
   tareas con español, sólo algunas, o con qué ponderación.
2. **La magnitud demuestra que no es retrieval.** `multilingual-e5-large-instruct`
   marca **91.65** en esa columna y **51.74** en la columna `Retr.` de
   `MTEB(spa, v1)` (§4). Una diferencia de 40 puntos sobre el mismo modelo y el mismo
   idioma sólo se explica porque la columna `Spanish` está dominada por tareas de
   clasificación, STS y bitext, donde los puntajes viven arriba de 85.

Es, eso sí, el único número por-idioma español que el leaderboard publica para
modelos sin fila en `MTEB(spa, v1)`, y por eso lo dejo registrado con su caveat.

### 8.7 Salvedades propias de esta ampliación

1. **El `Retr.` de esta sección no es español.** Ya está en §8.2, lo repito porque es
   el error de lectura más fácil de cometer: 14 de las 18 tareas no tienen español.
   Un modelo puede liderar acá y rendir peor que `bge-m3` sobre los TO del BCRA.
2. **Tres de los nueve no declaran español** (`geevec-lite`, `pplx-embed`,
   `Qwen3-Embedding-0.6B`). Dicen "multilingüe" o "100+ idiomas" sin enumerar. No
   infiero que soporten español: la fuente no lo declara, y son justamente los tres
   sin ninguna evidencia española directa (ni fila en `MTEB(spa, v1)`, ni lista de
   idiomas).
3. **`geevec-lite` y `pplx-embed` corrieron sólo el subconjunto de retrieval** (18 de
   131 tareas). Su `Retr.` es comparable; cualquier otra columna suya no existe.
4. **La contaminación no es homogénea, y donde más pega es justo en retrieval.**
   Contando sólo las 18 tareas que forman la columna `Retr.`: `harrier` (ambos
   tamaños) y `granite-r2` (ambos tamaños) tienen **5 de 18 sumandos marcados** como
   no zero-shot; `pplx`, `Qwen3-0.6B` y los dos `arctic` tienen 1; `geevec-lite`
   tiene 0. Las cinco tareas marcadas son las mismas en los cuatro casos:
   `MIRACLRetrievalHardNegatives`, `SpartQA`, `StatcanDialogueDatasetRetrieval`,
   `TempReasonL1` y `WinoGrande`. Si el criterio de la autora es minimizar sospecha
   de contaminación en retrieval, el orden de la tabla de §8.4 cambia.
5. **Dos snapshots distintos conviven en este documento.** §2–§7 son del 2026-08-18;
   §8 es del 2026-08-19. No mezclé números entre ambos salvo donde lo digo
   explícitamente (la comparación de §8.4 con los candidatos de §5, que leí en el
   snapshot del 19).
6. **Nada de esta sección se probó localmente**: ni MPS, ni tiempos, ni calidad sobre
   el corpus. Sigue siendo relevamiento de fuentes publicadas.

### 8.8 Archivos de evidencia de la ampliación

| archivo | qué es |
|---|---|
| `mteb_snapshot_multi/mmteb_v2_candidatos_sin_fila_spa.tsv` | los 9 candidatos con todas las columnas reportadas |
| `mteb_snapshot_multi/mmteb_v2_excluidos_con_motivo.tsv` | los 14 modelos descartados, con motivo y fuente del motivo |
| `mteb_snapshot_multi/mmteb_v2_retr_18_tareas.tsv` | las 18 tareas que componen la columna `Retr.` |
| `mteb_snapshot_multi/<org>_<modelo>_README.md` | model cards crudas de los 18 modelos revisados |
| `mteb_snapshot_multi/<org>_<modelo>_config.json` | `config.json` crudos (ventana, hidden size, arquitectura) |
| `mteb_snapshot_multi/<org>_<modelo>_sentence_bert_config.json` | `max_seq_length` declarado, donde existe |
| `mteb_snapshot_multi/<org>_<modelo>_config_sentence_transformers.json` | prompts de query/documento declarados |
| `mteb_snapshot_multi/<org>_<modelo>_api.json` | respuesta de `https://huggingface.co/api/models/<id>` (licencia, fechas, conteo de parámetros) |
