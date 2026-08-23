# Extracción verbatim — microsoft/harrier-oss-v1-0.6b

Solo extracción y contraste. Sin interpretación ni recomendación.

## 0. Fuentes y su procedencia

| fuente | qué es | sha256 local |
|---|---|---|
| `model_cards_U-A2.0b/harrier__README.md` | la model card | `8c571701c467aa0ca60b7e9739e8ea5e1db38614616a67677cd231410392aa81` |
| `harrier__config_sentence_transformers.json` | prompts preconfigurados | (en `manifest.txt`) |
| `harrier__1_Pooling_config.json` | pooling | (en `manifest.txt`) |
| `harrier__modules.json` | pipeline de Sentence Transformers | (en `manifest.txt`) |
| `harrier__config.json` | arquitectura | (en `manifest.txt`) |
| `harrier__tokenizer_config.json` | tokenizador | (en `manifest.txt`) |

**Revisión exacta del repo usada en el entregable 3** (de `e3_entorno.json`):
`f9b9dc8d367d443f2479d27aa5d8d2850c0774ee`

**¿Repo del autor con README propio?** No hay. El listado de archivos del repo
de HuggingFace es, completo:
`.gitattributes, 1_Pooling/config.json, README.md, added_tokens.json,
chat_template.jinja, config.json, config_sentence_transformers.json,
merges.txt, model.safetensors, modules.json, mteb_v2_eval_prompts.json,
special_tokens_map.json, tokenizer.json, tokenizer_config.json, vocab.json`.
Los únicos enlaces externos de la card son a las otras dos tallas del modelo,
al leaderboard de MTEB y al repo de terceros
`https://github.com/embeddings-benchmark/mteb`. No hay repo de código de los
autores. **La model card es la única fuente de los autores.**

## 1. Prefijo / instrucción de query y de documento

### 1.a Preconfigurados — `config_sentence_transformers.json`, verbatim e íntegro

```json
{
  "prompts": {
    "web_search_query": "Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: ",
    "sts_query": "Instruct: Retrieve semantically similar text\nQuery: ",
    "bitext_query": "Instruct: Retrieve parallel sentences\nQuery: "
  },
  "default_prompt_name": null,
  "similarity_fn_name": "cosine"
}
```

No hay ninguna entrada de prompt de documento. `default_prompt_name` es `null`.

### 1.b Ejemplo de uso con Sentence Transformers — README, verbatim

```python
query_embeddings = model.encode(queries, prompt_name="web_search_query")
document_embeddings = model.encode(documents)
```

Y el párrafo que le sigue, verbatim:

> Have a look at [config_sentence_transformers.json](config_sentence_transformers.json) for the prompts that are pre-configured, such as `web_search_query`, `sts_query`, and `bitext_query`. You can also use a custom instruction directly via e.g. `model.encode(queries, prompt="Instruct: Retrieve semantically similar text\nQuery: ")`.

### 1.c Ejemplo de uso con Transformers — README, verbatim

```python
def get_detailed_instruct(task_description: str, query: str) -> str:
    return f'Instruct: {task_description}\nQuery: {query}'


# Each query must come with a one-sentence instruction that describes the task
task = 'Given a web search query, retrieve relevant passages that answer the query'
queries = [
    get_detailed_instruct(task, 'how much protein should a female eat'),
    get_detailed_instruct(task, 'summit define')
]
# No need to add instruction for retrieval documents
documents = [
```

### 1.d FAQ 1 — README, verbatim e íntegra

> **1. Do I need to add instructions to the query?**
>
> Yes, this is how the model is trained, otherwise you will see a performance degradation.
> The task definition should be a one-sentence instruction that describes the task.
> This is a way to customize text embeddings for different scenarios through natural language instructions.
>
> On the other hand, there is no need to add instructions to the document side.

### 1.e ¿Difieren query y documento?

Sí. La fuente lo dice de tres maneras: no define prompt de documento; el
ejemplo de ST llama `model.encode(documents)` sin `prompt_name`; el ejemplo de
Transformers lleva el comentario `# No need to add instruction for retrieval
documents`; y la FAQ 1 dice "there is no need to add instructions to the
document side".

### 1.f Prompts de evaluación

README, verbatim:

> The evaluation prompts used for each task are also available at [mteb_v2_eval_prompts.json](mteb_v2_eval_prompts.json).

Ese archivo es un diccionario de 131 entradas, una por tarea de MTEB v2 (por
ejemplo `"AlloprofReranking-query": "Given a question, retrieve passages that
answer the question"`). **No declara un prompt por defecto para "retrieval" en
general**: cada tarea tiene el suyo.

## 2. Normalización de vectores

README, FAQ 3, verbatim e íntegra:

> **3. What pooling strategy does this model use?**
>
> The model uses **last-token pooling** — the embedding of the last non-padding token is used as the sentence representation.
> The embedding is then L2-normalized. This is handled automatically when using Sentence Transformers.

README, descripción del modelo, verbatim:

> The models use decoder-only architectures with last-token pooling and L2 normalization to produce dense text embeddings.

README, ejemplo de Transformers, verbatim:

```python
# normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
```

`modules.json`, verbatim e íntegro (el módulo 2 es la normalización):

```json
[
  {
    "idx": 0,
    "name": "0",
    "path": "",
    "type": "sentence_transformers.models.Transformer"
  },
  {
    "idx": 1,
    "name": "1",
    "path": "1_Pooling",
    "type": "sentence_transformers.models.Pooling"
  },
  {
    "idx": 2,
    "name": "2",
    "path": "2_Normalize",
    "type": "sentence_transformers.models.Normalize"
  }
]
```

## 3. Estrategia de pooling

Además de la FAQ 3 y la descripción ya citadas, el README trae la
implementación de referencia, verbatim:

```python
def last_token_pool(last_hidden_states: Tensor, attention_mask: Tensor) -> Tensor:
    left_padding = (attention_mask[:, -1].sum() == attention_mask.shape[0])
    if left_padding:
        return last_hidden_states[:, -1]
    else:
        sequence_lengths = attention_mask.sum(dim=1) - 1
        batch_size = last_hidden_states.shape[0]
        return last_hidden_states[torch.arange(batch_size, device=last_hidden_states.device), sequence_lengths]
```

`1_Pooling/config.json`, verbatim e íntegro:

```json
{
  "word_embedding_dimension": 1024,
  "pooling_mode_cls_token": false,
  "pooling_mode_mean_tokens": false,
  "pooling_mode_max_tokens": false,
  "pooling_mode_mean_sqrt_len_tokens": false,
  "pooling_mode_weightedmean_tokens": false,
  "pooling_mode_lasttoken": true,
  "include_prompt": true
}
```

## 4. trust_remote_code

**No declarado en la fuente.** La cadena `trust_remote_code` no aparece en la
model card. `config.json` declara `"architectures": ["Qwen3Model"]` y
`"model_type": "qwen3"`, y no contiene `auto_map`.

## 5. Versión mínima de transformers / sentence-transformers

**No declarado en la fuente.** La model card no enuncia ningún mínimo. El
único número de versión que aparece en los archivos del repo es
`"transformers_version": "4.57.6"` dentro de `config.json`, que registra la
versión con la que se guardó el modelo, no un mínimo.

Lo más cercano a una advertencia de versión es la FAQ 2, verbatim e íntegra:

> **2. Why are my reproduced results slightly different from reported in the model card?**
>
> Different versions of `transformers` and `pytorch` could cause negligible but non-zero performance differences.

## 6. Longitud máxima

Tres valores en la fuente, que no coinciden entre sí:

- README, tabla de modelos, columna **Max Tokens**: `32,768` para las tres
  tallas (`harrier-oss-v1-270m`, `harrier-oss-v1-0.6b`, `harrier-oss-v1-27b`).
- README, ejemplo de Transformers, verbatim:
  ```python
  max_length = 32768
  # Tokenize the input texts
  batch_dict = tokenizer(input_texts, max_length=max_length, padding=True, truncation=True, return_tensors='pt')
  ```
- `config.json`: `"max_position_embeddings": 32768`
- `tokenizer_config.json`: `"model_max_length": 131072`

El repo **no** trae `sentence_bert_config.json`, que es donde Sentence
Transformers busca `max_seq_length`.

## 7. Dimensión del vector

- README, tabla de modelos, fila `harrier-oss-v1-0.6b`, columna **Embedding
  Dimension**: `1,024`.
- `1_Pooling/config.json`: `"word_embedding_dimension": 1024`.
- `config.json`: `"hidden_size": 1024`.

## 8. Advertencias de los autores

Las únicas del documento son las dos FAQ ya citadas íntegras (§1.d y §5):
degradación de desempeño si se omite la instrucción en la query, y diferencias
"negligible but non-zero" por versiones distintas de `transformers` y
`pytorch`.

No hay sección de limitaciones, sesgos, uso previsto, ni disclaimer.
**No declarado en la fuente.**

Datos de contexto que la card sí declara, verbatim:

> harrier-oss-v1 is a family of multilingual text embedding models developed by Microsoft.

> The models achieve state-of-the-art results on the [Multilingual MTEB v2](https://huggingface.co/spaces/mteb/leaderboard) benchmark as of the release date.

> All models are trained with contrastive learning objectives on a large-scale mixture of multilingual datasets covering diverse tasks.
> The 270m and 0.6b variants are additionally trained with knowledge distillation from larger embedding models.

Y sobre idiomas, verbatim (el fragmento donde aparece el español):

> The models are trained on multilingual data and support a wide range of languages,
> including but not limited to: Arabic, Bulgarian, Catalan, Czech, Danish, German, Greek, English, Spanish, …

## 9. Licencia

- Frontmatter YAML de la model card: `license: mit`
- Metadato del repo (`cardData.license` vía la API de HuggingFace): `mit`
- **Texto de la licencia: no declarado en la fuente.** El repo no contiene
  archivo `LICENSE` ni `LICENSE.md` (ver el listado completo de archivos en
  §0), y la model card no reproduce ni enlaza el texto.
- Referencia canónica del identificador declarado: SPDX `MIT`,
  https://opensource.org/license/mit

## 10. Valores efectivamente aplicados en el entregable 3

De `e3_medicion.py` (verbatim del código) y `e3_resultados/harrier.json`:

```python
  "harrier": dict(repo="microsoft/harrier-oss-v1-0.6b",
                  q=dict(prompt_name="web_search_query"), d=dict(), trc=False),
```

```python
    m = SentenceTransformer(cfg["repo"], device="mps", trust_remote_code=cfg["trc"],
                            model_kwargs={"dtype": torch.float32})
    m.max_seq_length = MAX_SEQ
```

```python
            v = m.encode([textos[i] for i in g], batch_size=len(g), convert_to_numpy=True,
                         normalize_embeddings=True, show_progress_bar=False, **kw)
```

Constantes: `TOKEN_BUDGET = 8448`, `GRUPO_MAX = 32`, `MAX_SEQ = 16384`,
`TOPK = 10`, `DTYPE = "float32"`.
Registrado en la salida: `max_seq_length_efectivo: 16384`, `dim: 1024`,
`n_grupos_docs: 93`, `t_carga_s: 68.3`, `t_indexacion_s: 427.9`,
`sha_docs: 12d284d5bce0d1d58f1e4437c47f2177b3145813586069ca72f9103309b28b65`,
determinismo `embeddings_byte_identicos: true`, `rankings_identicos: true`.
Librerías: torch 2.13.0, transformers 5.15.1, sentence-transformers 6.0.0,
tokenizers 0.22.2, numpy 2.5.2.

## 11. Contraste card ↔ aplicado

| punto | card | aplicado | ¿difiere? |
|---|---|---|---|
| prompt de query | `prompt_name="web_search_query"` | `prompt_name="web_search_query"` | no |
| prompt de documento | `model.encode(documents)`, sin prompt | `d=dict()`, sin prompt | no |
| pooling | last-token (`pooling_mode_lasttoken: true`) | el del repo, sin override | no |
| normalización | L2, automática en ST (módulo `2_Normalize`) | módulo del repo **+** `normalize_embeddings=True` explícito | forma sí, valor no: la segunda normalización L2 sobre un vector ya L2-normalizado es idempotente |
| dimensión | 1.024 | 1.024 (medido) | no |
| trust_remote_code | no declarado en la fuente | `False` | no comparable |
| versión mínima de librería | no declarado en la fuente | transformers 5.15.1 / ST 6.0.0 | no comparable |
| **dtype** | `model_kwargs={"dtype": "auto"}` → `config.json` declara `"dtype": "bfloat16"` | `model_kwargs={"dtype": torch.float32}` | **SÍ — desvío declarado** |
| **dispositivo** | `model.cuda()` en el ejemplo de Transformers | `device="mps"` | **SÍ — desvío declarado** |
| **longitud máxima** | `max_length = 32768` | `max_seq_length = 16384` | **SÍ — desvío declarado** |
| batch | no declarado en la fuente | presupuesto de tokens 8.448, grupo máximo 32 | no comparable |
| similitud | `"similarity_fn_name": "cosine"` | coseno sobre vectores L2-normalizados | no |

### Los tres desvíos, declarados

1. **dtype `float32` en lugar de `auto` (= `bfloat16`).** Motivo registrado en
   `reglas_puntuacion_declaradas.md` y en el reporte: la precisión numérica se
   igualó entre los cinco modelos para no dejarla como variable libre.
   `float32` es mayor precisión que la que declara `config.json`, no menor.
2. **`device="mps"` en lugar de `cuda`.** El mandato fija ejecución local en
   Apple Silicon; no hay CUDA en la máquina.
3. **`max_seq_length = 16384` en lugar de `32768`.** Es la política de truncado
   única de los cinco modelos. Consecuencia medida sobre este corpus: **ninguna**
   — el pasaje más largo tiene 8.233 tokens con el tokenizador de este modelo
   (`e2_truncamiento.json`: `chunks_truncados: 0` contra la ventana declarada
   de 32.768, y `mayor_chunk_tokens: 8233`), de modo que ni 16.384 ni 32.768
   truncan un solo pasaje.

Un cuarto punto que no es desvío pero conviene dejar asentado: la card usa
`model.encode(queries, prompt_name="web_search_query")` para recuperación y
ofrece además instrucciones personalizadas; en el bake-off **no** se
personalizó la instrucción ni se la tradujo al castellano — se usó la
preconfigurada tal cual.
