# Bake-off de modelos de embeddings sobre el corpus de la tesis

U-A2.0b-bakeoff — apoyo al laudo de la autora. **NO es un laudo y no
recomienda un ganador.** Costo de API: **USD 0** (modelos abiertos, ejecución
local en Apple Silicon M4 / MPS; ninguna llamada a API paga). Repo intacto,
branch `main`, escrituras solo en el scratchpad de la sesión. Principio 7
respetado: no se abrió ningún material EV2 (preguntas, criterios ni trazas).

## 1. Por qué se mide acá y no se lee del ranking

Los rankings MTEB no pueden decidir esta elección: el subconjunto español
tiene cobertura parcial (30 de 219 modelos con puntaje de retrieval; varios
candidatos ausentes por falta de dato, no por desempeño), el ranking
multilingüe promedia 18 tareas de las cuales solo 4 incluyen español, tres de
los candidatos declaran contaminación, y ninguna de esas tareas se parece a
normativa bancaria en castellano. **Los puntajes del ranking no ordenan nada
en este documento**: el orden lo da la medición sobre este corpus.

## 2. Qué se midió

- **Pasajes**: los 1.763 chunks de E0 (`salida_enm01`), universo completo.
- **Consultas**: 100 casos = los 50 pares sintéticos de A1.3 (`pares_v3.json`,
  sellado en `68c79dc`, sha256 verificado contra su manifiesto) × 2 variantes
  (literal y anti-léxica). Material propio, no EV2.
- **Gold**: chunk que contiene la respuesta, bajo dos reglas declaradas y
  selladas ANTES de indexar (`reglas_puntuacion_declaradas.md`,
  sha256 `7fd5608cfe005e1913a7c5703c995a1ca7965bd3ac35afb677f961db4bb28318`).

### 2.1 Composición del pasaje indexado (declarada, no cambia entre modelos)

Se indexa **propio + herencia**, en la forma exacta que E0 sella como
`completo`: `"\n".join([textos de herencia] + [texto propio])`. No es una
composición inventada para esta unidad: reproduce `chars_completo` y
`sha256_completo` de **los 1.763 chunks sin una sola excepción** (verificación
dentro de `construir_gold_y_corpus.py`, con `assert`). Justificación: el texto
propio de un `mini_chunk` es un fragmento ininterpretable solo — el peor caso
del corpus tiene 26 caracteres — y la herencia es exactamente el encabezado de
sección y del punto padre que lo hace legible.

**Esta misma composición es la que usará el brazo RAG en A2.** Queda dicho acá
para que no se re-decida más adelante.

### 2.2 Las dos reglas de puntuación y el tamaño de gold

- **PRINCIPAL R2** — subárbol completo del ancla: exacta ∪ descendientes,
  siempre. 100 casos.
- **CONTROL "gold bien formado"** — subconjunto de pares cuyo gold es
  sustantivo y unívoco: se excluyen los de gold solo-`mini_chunk` y los
  ambiguos (|gold| > 10). **n = 30 casos (15 pares)**. Sobre este subconjunto
  R1 y R2 coinciden par por par (verificado con `assert`), de modo que el
  control es un puro submuestreo del principal: mismas consultas, mismo
  índice, mismo gold, menos casos.

Distribución del tamaño de gold **por regla** (casos):

| regla | mediana | máx | distribución \|gold\| → casos |
|---|---|---|---|
| R2 | 11 | 49 | 1→20, 2→2, 4→2, 5→6, 7→2, 8→8, 9→4, 10→2, 11→6, 12→2, 13→4, 16→6, 18→6, 20→4, 24→4, 25→2, 27→8, 39→2, 40→2, 43→2, 49→6 |
| control | 1 | 8 | 1→20, 2→2, 4→2, 7→2, 8→4 |

Es la razón por la que el análisis se ancla en **recall@1** y en la **brecha
literal − anti-léxica**: con gold de mediana 11 sobre 1.763 pasajes, @10
satura y deja de discriminar.

### 2.3 Lo que se igualó entre modelos

Un solo índice por modelo, las mismas 100 consultas, y estas constantes
idénticas para los cinco: `top-k = 10`; **política de truncado única**
`max_seq_length = 16384` (por encima del pasaje más largo, 8.233 tokens, y por
debajo de la ventana declarada más chica, 32.768 → truncamiento 0 verificado);
**precisión `float32`** en los cinco; similitud **coseno** sobre embeddings
L2-normalizados (las cinco model cards declaran `similarity_fn_name: cosine`);
desempate declarado (score descendente, luego `id` ascendente).

Agrupamiento por **presupuesto de tokens** (8.448 tokens por grupo, máximo 32
textos), no por batch fijo, y el mismo criterio para los cinco. El batch
afecta el tiempo y no el resultado; queda verificado abajo (§6).

## 3. Resultados — regla PRINCIPAL R2 (100 casos: 50 literal + 50 anti-léxica)

| modelo | lit@1 | lit@5 | lit@10 | anti@1 | anti@5 | anti@10 | brecha @1 | brecha @10 | ambas@1 |
|---|---|---|---|---|---|---|---|---|---|
| **bm25** *(control léxico)* | **72%** | 86% | 86% | 16% | 34% | 46% | +56 pp | +40 pp | 44% |
| granite | 46% | 60% | 68% | 22% | 36% | 44% | +24 pp | +24 pp | 34% |
| qwen3 | 44% | 64% | 68% | 24% | 46% | 48% | +20 pp | +20 pp | 34% |
| harrier | 52% | 72% | 76% | **36%** | 50% | 56% | +16 pp | +20 pp | 44% |
| f2llm | 46% | 58% | 68% | 16% | 38% | 46% | +30 pp | +22 pp | 31% |
| jina *(no elegible — licencia)* | 46% | 66% | 70% | 28% | 42% | 50% | +18 pp | +20 pp | 37% |

## 4. Resultados — regla CONTROL "gold bien formado" (30 casos: 15 + 15)

| modelo | lit@1 | lit@5 | lit@10 | anti@1 | anti@5 | anti@10 | brecha @1 | brecha @10 | ambas@1 |
|---|---|---|---|---|---|---|---|---|---|
| **bm25** *(control léxico)* | 60% | 73% | 73% | **0%** | 13% | 13% | +60 pp | +60 pp | 30% |
| granite | 40% | 53% | 53% | 27% | 33% | 40% | +13 pp | +13 pp | 33% |
| qwen3 | 33% | 53% | 60% | 20% | 40% | 47% | +13 pp | +13 pp | 27% |
| harrier | 40% | 60% | 60% | 20% | 40% | 40% | +20 pp | +20 pp | 30% |
| f2llm | 40% | 53% | 60% | 13% | 40% | 47% | +27 pp | +13 pp | 27% |
| jina *(no elegible — licencia)* | 33% | 60% | 67% | 20% | 33% | 33% | +13 pp | +33 pp | 27% |

Con n = 15 por variante, **un caso vale 6,7 pp** (3,3 pp sobre los 30 casos).
Toda diferencia menor a eso en esta tabla es un caso suelto.

## 5. Criterio de lectura declarado ex ante — resultado

El criterio, declarado antes de indexar: *si las dos reglas producen el mismo
orden de modelos, la elección es robusta; si difieren, no se elige, se
reportan ambas tablas y la unidad frena para laudo.* `jina` no participa del
ordenamiento (no elegible); BM25 sí, como piso de referencia.

| lectura | orden bajo R2 | orden bajo control | parejas invertidas |
|---|---|---|---|
| recall@1 **ambas** | `bm25 = harrier > granite = qwen3 > f2llm` | `granite > bm25 = harrier > f2llm = qwen3` | **2** |
| recall@1 **literal** | `bm25 > harrier > f2llm = granite > qwen3` | `bm25 > f2llm = granite = harrier > qwen3` | **0** |
| recall@1 **anti-léxica** | `harrier > qwen3 > granite > bm25 = f2llm` | `granite > harrier = qwen3 > f2llm > bm25` | **2** |

Inversiones concretas: en *ambas*, `bm25` vs `granite` (+10 pp bajo R2 / −3 pp
bajo control) y `granite` vs `harrier` (−10 pp / +3 pp); en *anti-léxica*,
`granite` vs `qwen3` (−2 pp / +7 pp) y `granite` vs `harrier` (−14 pp / +7 pp).

**Los órdenes difieren ⇒ por el criterio declarado, esta unidad NO elige.**

Matiz que corresponde declarar sin adjudicarlo: las cuatro inversiones tienen,
del lado del control, una magnitud de **±3,3 pp o ±6,7 pp** — exactamente uno
o dos casos sobre 30. Es decir, ninguna inversión excede la resolución del
instrumento en el control. Cómo pesar eso frente a la robustez del criterio es
laudo de la autora, no de esta unidad.

## 6. Determinismo, tiempos, truncamiento

| modelo | licencia | params | ventana declarada | chunks truncados | mayor chunk (tok de ESE tokenizador) | t. indexación (s) | dim | doble corrida byte-idéntica |
|---|---|---|---|---|---|---|---|---|
| bm25 *(control léxico)* | — | — | — | no aplica | — | 0,2 | — | determinístico por construcción |
| granite | Apache-2.0 | 312M | 32.768 | **0** (0,0%) | 7.498 | 103,8 | 768 | sí (embeddings y rankings) |
| qwen3 | Apache-2.0 | 596M | 32.768 | **0** (0,0%) | 8.233 | 804,3 | 1024 | sí |
| harrier | MIT | 596M | 32.768 | **0** (0,0%) | 8.233 | 427,9 | 1024 | sí |
| f2llm | Apache-2.0 | 596M | 40.960 | **0** (0,0%) | 8.233 | 435,8 | 1024 | sí |
| jina *(no elegible)* | CC-BY-NC-4.0 | 596M | 32.768 | **0** (0,0%) | 8.232 | 491,9 | 1024 | sí |

**Entregable 2 — recuento de truncamiento, en detalle.** Con el
`AutoTokenizer` de cada modelo sobre los 1.763 pasajes: **ningún modelo trunca
un solo chunk**. La cifra "78 chunks" de mandatos anteriores no es
transferible y queda reemplazada: se midió con un tokenizador y contra una
ventana chica. Para dimensionar de dónde venía, con el tokenizador de Qwen2
este corpus tiene 361 chunks por encima de 512 tokens y 64 por encima de 1.024
— pero 0 por encima de 32.768. Cuatro de los cinco modelos comparten el
tokenizador de Qwen2 y dan conteos idénticos; granite usa el suyo (vocabulario
262.144, tokeniza el castellano más corto: 584.911 tokens de corpus contra
651.274); jina difiere en 1 token en el chunk más largo por su manejo de
tokens especiales. Tabla completa en `e2_truncamiento.json`.

**Caché de HuggingFace**: `~/.cache/huggingface`, **fuera del repo**, **6,5 GB**
tras descargar los cinco modelos. No se redefinió `HF_HOME` para que las
re-corridas no vuelvan a descargar. Revisiones exactas de cada repo de modelo
en `e3_entorno.json`.

**Verificación de que el batching no toca resultados** (relevante porque hubo
que cambiarlo, ver §9): se re-corrió granite con el agrupamiento nuevo y con
liberación de caché de MPS entre grupos, y la matriz de embeddings dio
sha256 idéntico (`5e6b7bf4…b0fc`), con métricas y rankings idénticos.

## 7. Detalles de uso aplicados por modelo

Texto completo con la cita de cada punto en **`detalles_uso_modelos.md`**.
Criterio general: **se usa el prompt que cada modelo trae preconfigurado en su
propio `config_sentence_transformers.json`**, no una instrucción escrita por
mí — es la opción documentada más conservadora y evita meter una variable
libre distinta por modelo. Resumen:

| modelo | prompt de query | prompt de documento | ¿difieren? | pooling | trust_remote_code |
|---|---|---|---|---|---|
| qwen3 | `Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery:` | *(vacío)* | sí | last-token | no |
| granite | *(vacío)* | *(vacío)* | no (simétrico) | CLS | no |
| harrier | `web_search_query` = `Instruct: Given a web search query…\nQuery: ` | *(ninguno definido)* | sí | last-token | no |
| f2llm | `Instruct: Given a question, retrieve passages that can help answer the question.\nQuery: ` | *(vacío)* | sí | last-token | no |
| jina | `Query: ` con `task="retrieval"` | `Document: ` con `task="retrieval"` | sí — **el único que prefija el documento** | custom (`custom_st`) | **sí** |

Sobre **Qwen3** en particular, que el mandato marcó: la instrucción va del lado
de la **query**, no del documento (`"document": ""` en su config; README
"No need to add instruction for retrieval documents"), y **en inglés** —
README línea 54: los autores aconsejan escribirla en inglés porque así fueron
escritas las del entrenamiento. El prompt preconfigurado ya está en inglés y
se usó tal cual, sin traducir ni adaptar al dominio. Omitirla degradaría el
retrieval "approximately 1% to 5%" según los propios autores (README línea
206), así que omitirla habría sido un uso incorrecto documentado.

Puntos donde la model card **no** es clara, declarados: granite, harrier y
f2llm no declaran versión mínima de librería (se usó torch 2.13.0 /
transformers 5.15.1 / sentence-transformers 6.0.0, posteriores a las que sus
propios archivos registran). **Desvío declarado en jina**: su card recomienda
`bfloat16` y `flash_attention_2`; se cargó en `float32` como los otros cuatro
para no dejar la precisión numérica como variable libre — es mayor precisión
que la recomendada, no menor — y flash-attention no se usó (la card la marca
"not mandatory" y no hay build para MPS).

## 8. Excluidos, con su motivo

| excluido | motivo |
|---|---|
| `BAAI/bge-m3` | el más flojo por ambas varas del ranking (49,40 español / 54,59 multilingüe) |
| `google/embeddinggemma-300m` | licencia propia con restricciones — motivo **no técnico** |
| `intfloat/multilingual-e5-large-instruct` | ventana de 512 tokens: trunca este corpus. Orden de magnitud del daño, medido con el tokenizador de Qwen2 y no con el de XLM-R que usa ese modelo (no se lo descargó): 361 de 1.763 chunks superan 512 tokens |
| `geevec/pplx-embed` | no declaran español; sin trayectoria verificable |
| `jinaai/jina-embeddings-v5-text-small` | **medido, pero NO elegible**: CC-BY-NC-4.0. Va en fila aparte y nunca como ganador; se mide solo para cuantificar el costo de la restricción de licencia |

**Costo de la restricción de licencia**, que es para lo único que se midió
jina: bajo R2, jina queda en 37% de recall@1 (ambas) contra 44% de harrier, el
mejor elegible; en anti-léxica@1, 28% contra 36%. Es decir, **en este corpus la
referencia no elegible no supera al mejor elegible en ninguna de las dos
columnas que el laudo declaró como eje del análisis**. La restricción de
licencia no cuesta desempeño acá.

## 9. Incidencias de ejecución, declaradas

1. **OOM de MPS con batch fijo.** La primera versión usaba batch de 16 textos.
   El pasaje más largo (8.233 tokens, `cap::4.2.1.2`) hizo que qwen3 intentara
   reservar 4,04 GiB sobre 18,13 GiB permitidos y abortara. Se reemplazó por
   agrupamiento con presupuesto de tokens (§2.3) y se re-corrió granite: las
   métricas dieron idénticas.
2. **jina bloqueada por agotamiento de memoria.** Con el agrupamiento nuevo,
   jina quedó 44 minutos sin avanzar. Diagnóstico por muestreo del proceso:
   hilo principal 100% del tiempo bloqueado en
   `[_MTLCommandBuffer waitUntilCompleted]` dentro de una copia de MPS, estado
   `stuck`, 16 GB residentes, swap del sistema en 16,5 GB de 17,4 GB — la
   máquina paginaba, no calculaba. Causa: el adaptador LoRA de
   `task="retrieval"` acumulaba memoria a lo largo de los 93 grupos. Se agregó
   `torch.mps.empty_cache()` entre grupos; jina pasó a terminar en 492 s. La
   inocuidad numérica del agregado se verificó re-corriendo granite (§6):
   sha256 de embeddings, métricas y rankings idénticos. Los tiempos de
   indexación de granite reportados incluyen ya esta versión (103,8 s).

## 10. Limitaciones

- **El gold viene de pares generados desde el KG.** Mide recuperación del
  pasaje que contiene la respuesta, **no calidad de respuesta final**.
- **El material ya fue usado para medir y ahora se usa para ELEGIR.** Los pares
  v3 se usaron en A1.4; el modelo que se elija queda ajustado a este material,
  así que **ninguna medición posterior del ganador sobre v3 es independiente**:
  B1.10 debe usar pares frescos. El brazo RAG de A2 se mide sobre EV2, que no
  se toca.
- **recall@k estático no es desempeño agéntico.** En A2 el brazo RAG es un
  agente que itera consultas. Esto es una heurística de selección, no un
  resultado de tesis.
- **El control tiene n = 30 (15 por variante).** Un caso vale 6,7 pp por
  variante. Las inversiones de orden que reporta §5 están todas en ese orden de
  magnitud.
- **La frontera de ancla no coincide con la frontera de chunk** — ver §11. Toda
  la §2.2 existe por eso; el número que se reporte depende de la política de
  descendientes que se declare.
- Una lectura que el bake-off habilita y conviene no perder: **BM25 gana en
  literal@1 por 20 pp sobre el mejor denso y pierde en anti-léxica@1 por 20 pp
  contra el mismo modelo**. En este corpus el aporte del denso es
  específicamente robustez anti-léxica, no recuperación en general.

## 11. Hallazgo registrado para la tesis

Documento completo en **`hallazgo_frontera_ancla_chunk.md`**. Enunciado: las
anclas de *provenance* que el KG hereda de la norma y los límites de chunk de
E0 **no delimitan las mismas unidades de texto**, y el caso peligroso no es el
que falla sino el que resuelve mal en silencio (ancla contenedora cuyo chunk
exacto es solo un `mini_chunk` de arranque). Es la **cuarta aparición** del
mismo fenómeno: censo de EV2
(`data/experiment/ev2_corrida/censo/ausencias_diagnostico.json`), ausencias de
KG-Reextraído (`docs/plan_tesis.md` §A0.4), sensibilidad por descendientes de
A0.2 (`data/experiment/ev2_reporte/salida/atribucion_fallas.md` §5, H1 y H4,
sellada en `85d9fdb` — donde la política de descendientes **cambia la clase
causal atribuida**), y este mapeo. No es un defecto de esta unidad: es una
propiedad del corpus, y toda medición cross-capa tiene que declarar su política
de descendientes antes de medir.

## 12. Reproducción

```
python3 construir_gold_y_corpus.py     # corpus de pasajes + gold bajo las dos reglas
python3 e2_truncamiento.py             # entregable 2
python3 e3_medicion.py {bm25|granite|qwen3|harrier|f2llm|jina}
python3 e4_tablas.py                   # tablas de §3, §4, §5, §6
python3 e3_entorno.py                  # entorno y revisiones de los repos de modelo
```

(con el intérprete de `venv_bakeoff/bin/python` salvo el primero y el segundo,
que solo necesitan `transformers` para el segundo.)

**Esta unidad no propone un ganador. La elección es laudo de la autora.**
