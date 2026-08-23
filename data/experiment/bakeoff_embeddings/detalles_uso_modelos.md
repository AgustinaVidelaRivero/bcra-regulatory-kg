# Detalles de uso aplicados por modelo, con su cita

Cita = archivo del repositorio del modelo en HuggingFace, descargado con
`huggingface_hub` y conservado en `model_cards/` del paquete de revisión.
La revisión del repo (`sha` del commit) se registra en `e3_entorno.json`.
Criterio general declarado: **se usa el prompt/instrucción que el propio
modelo trae preconfigurado en `config_sentence_transformers.json`**, no una
instrucción escrita por mí. Es la opción documentada más conservadora y evita
introducir una variable libre distinta por modelo.

## Qwen/Qwen3-Embedding-0.6B (Apache-2.0, 596M, ventana 32.768)

- **Instrucción del lado de la QUERY, no del documento.** `config_sentence_transformers.json`:
  `"prompts": {"query": "Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery:", "document": ""}`.
  El README lo repite en el ejemplo de Transformers: "No need to add
  instruction for retrieval documents" (línea 138 y 190 de `README.md`).
- **Instrucción en inglés.** README línea 54: "In multilingual contexts, we
  also advise users to write their instructions in English, as most
  instructions utilized during the model training process were originally
  written in English". El prompt preconfigurado ya está en inglés y se usa tal
  cual, sin traducir ni adaptar al dominio.
- **Magnitud del efecto que reporta el modelo.** README línea 206: "not using
  an `instruct` on the query side can lead to a drop in retrieval performance
  by approximately 1% to 5%". Por eso la instrucción se aplica: omitirla sería
  un uso incorrecto documentado.
- **Pooling**: `1_Pooling/config.json` → `pooling_mode_lasttoken: true`,
  `include_prompt: true`.
- **Normalización**: `modules.json` incluye `sentence_transformers.models.Normalize`
  (módulo 2). Además se normaliza explícitamente en el encode.
- **Versión mínima de librería**: README líneas 66-67: `transformers>=4.51.0`,
  `sentence-transformers>=2.7.0`. Usadas: 5.15.1 y 6.0.0.
- **trust_remote_code**: no requerido (arquitectura `qwen3` nativa).

## ibm-granite/granite-embedding-311m-multilingual-r2 (Apache-2.0, 312M, 32.768)

- **Sin prompt ni instrucción, ni en query ni en documento.**
  `config_sentence_transformers.json`: `"prompts": {"query": "", "document": ""}`.
  El ejemplo del README (`model.encode(input_queries)` / `model.encode(input_passages)`)
  no antepone nada. Es el único de los cinco que es simétrico.
- **Español declarado**: README línea 111 lista "Spanish (es)" entre los 50
  idiomas soportados.
- **Pooling**: `1_Pooling/config.json` → `pooling_mode_cls_token: true`,
  `include_prompt: false`.
- **Normalización**: `modules.json` incluye `Normalize`; el ejemplo de
  Transformers del README además normaliza a mano
  (`torch.nn.functional.normalize`, línea 232).
- **Ventana**: `sentence_bert_config.json` → `max_seq_length: 32768`;
  `config.json` → `max_position_embeddings: 32768`, arquitectura `ModernBertModel`.
- **Versión mínima de librería**: la model card no declara un mínimo explícito.
  Se registra como punto no documentado; se usó ST 6.0.0 / transformers 5.15.1,
  posteriores a las que la propia card dice haber usado para guardar el modelo
  (`config_sentence_transformers.json` → sentence_transformers 5.1.2,
  transformers 4.57.3).
- **MRL**: el modelo soporta truncar dimensiones (README líneas 175-190). NO se
  usa: se emplea la dimensión completa 768, que es el uso por defecto.
- **trust_remote_code**: no requerido.

## microsoft/harrier-oss-v1-0.6b (MIT, 596M, 32.768)

- **Instrucción del lado de la QUERY.** `config_sentence_transformers.json`
  define tres prompts y ninguno para documento:
  `web_search_query` = `"Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: "`,
  más `sts_query` y `bitext_query`.
  Se usa **`web_search_query`**, que es el que el propio README emplea en su
  ejemplo de recuperación: `model.encode(queries, prompt_name="web_search_query")`
  (línea 142). README línea 229: "there is no need to add instructions to the
  document side".
- **Español declarado**: README línea 211 lista "Spanish" entre los idiomas.
- **Pooling**: `1_Pooling/config.json` → `pooling_mode_lasttoken: true`,
  `include_prompt: true`. README línea 107: "decoder-only architectures with
  last-token pooling and L2 normalization".
- **Normalización**: README línea 238: "The embedding is then L2-normalized.
  This is handled automatically when using Sentence Transformers".
- **Versión mínima de librería**: no declarada en la card. Punto no documentado,
  registrado como tal.
- **trust_remote_code**: no requerido (`architectures: ["Qwen3Model"]`).
- **Contaminación declarada**: 5/18 en el ranking multilingüe. Es la razón por
  la que se lo mide acá y no se lo lee del ranking.

## codefuse-ai/F2LLM-v2-0.6B (Apache-2.0, 596M, ventana 40.960)

- **Instrucción del lado de la QUERY.** `config_sentence_transformers.json`:
  `"prompts": {"query": "Instruct: Given a question, retrieve passages that can help answer the question.\nQuery: ", "document": ""}`.
  README líneas 197-198, explícito: "use the prompt for queries" / "do not
  prepend the prompt to documents/passages".
- **Pooling**: `1_Pooling/config.json` → `pooling_mode_lasttoken: true`,
  `include_prompt: true`.
- **Normalización**: `modules.json` incluye `Normalize`; el ejemplo del README
  normaliza a mano (línea 172).
- **Ventana**: `config.json` → `max_position_embeddings: 40960` (la más grande
  de los cinco).
- **Versión mínima de librería**: no declarada. Punto no documentado.
- **trust_remote_code**: no requerido.
- **Punto no claro, resuelto por la opción conservadora**: la card admite
  documentos con o sin prompt para tareas simétricas (línea 200) pero es
  taxativa para recuperación ("do not prepend"). Se aplicó la instrucción
  taxativa: documentos sin prompt.

## jinaai/jina-embeddings-v5-text-small — REFERENCIA NO ELEGIBLE (CC-BY-NC-4.0)

Se mide sólo para cuantificar el costo de la restricción de licencia. Va en
fila aparte y NUNCA se propone como ganador.

- **Prompt en AMBOS lados, y difieren.** `config_sentence_transformers.json`:
  `"prompts": {"query": "Query: ", "document": "Document: "}`,
  `"default_prompt_name": "document"`. Es el único de los cinco que prefija el
  documento.
- **Adaptador de tarea obligatorio**: README líneas 244-257, el encode de
  recuperación se hace con `task="retrieval"` y `prompt_name="query"` /
  `"document"`. El repo trae `adapters/retrieval/` (LoRA), de ahí la
  dependencia `peft`.
- **trust_remote_code=True**: requerido — `config.json` trae `auto_map` a
  `modeling_jina_embeddings_v5.py`, y `modules.json` usa `custom_st.Transformer`.
  El README lo pasa explícitamente (líneas 153 y 232).
- **Versiones mínimas**: README líneas 59-61: `transformers>=4.57.0`,
  `torch>=2.8.0`, `peft>=0.15.2`. Usadas: 5.15.1, 2.13.0, 0.20.0.
- **Desvío declarado**: el README recomienda
  `model_kwargs={"dtype": torch.bfloat16}` "Recommended for GPUs" y
  `flash_attention_2` como opcional. Se cargó en **float32** como los otros
  cuatro, para no dejar la precisión numérica como variable libre entre
  modelos (el mandato exige igualarla); float32 es mayor precisión que la
  recomendada, no menor. flash-attention no se usó (la card la marca "not
  mandatory" y no hay build para MPS).
- **MRL / truncate_dim**: no se usa; dimensión completa.
