# 06 — LINK-KG: LLM-Driven Coreference-Resolved Knowledge Graphs for Human Smuggling Networks

## Cita (IEEE)
D. Meher, C. Domeniconi, and G. Correa-Cabrera, "LINK-KG: LLM-Driven Coreference-Resolved Knowledge Graphs for Human Smuggling Networks," *arXiv preprint* arXiv:2510.26486v1, Oct. 2025. [Online]. Available: https://arxiv.org/abs/2510.26486

## TL;DR
Extensión directa de CORE-KG (mismos autores) que reemplaza la coreferencia "single-pass" por un pipeline de tres etapas (NER → Mapping → Resolve) con un *Prompt Cache* type-specific que persiste a lo largo de chunks, abordando el "loss-in-the-middle" en documentos largos. Comparado contra GraphRAG y CORE-KG sobre 16 casos (7 cortos y 9 largos), reporta 45,21 % menos duplicación de nodos y 32,22 % menos ruido en promedio. La mejora sobre CORE-KG es marginal en documentos cortos pero significativa en largos — aporte real es el manejo de referencias plurales/role shifts y la escalabilidad a textos largos.

## Problema que ataca
CORE-KG (paper anterior de los mismos autores) usa un único prompt para resolver coreferencias por tipo, lo cual deja de funcionar bien en documentos largos por *loss-in-the-middle* (las menciones del medio reciben menos atención). Además, no maneja bien tres patrones críticos en texto legal: (i) **referencias plurales** ("the defendants" → varios sujetos específicos), (ii) **role shifts** ("the driver" puede ser el imputado en una oración y un agente en otra), (iii) **alias ambiguos** ("the agent" referido a múltiples personas en distintos checkpoints).

## Propuesta técnica
Pipeline en **tres etapas, repetidas secuencialmente para cada uno de los 7 tipos de entidad** (Person, Location, Organization, Route, Means of Transportation, Means of Communication, Smuggled Items):

**Stage 1 — NER-LLM** (por chunk):
- Prompt structured-instruction tipo-específico que extrae `PROPER_NOUN` (nombres explícitos) y `NOUN_PHRASE` (referencias descriptivas o por rol).
- Output JSON con campos `ENTITIES` y `PROPER_NOUN_DESCRIPTION`.
- Formalización: `{e_ij, d_ij} = NER-LLM(x_ij, p-ner)` donde `e_ij` son pares (proper noun, noun phrase) y `d_ij` mapea proper nouns → descripción de rol.

**Stage 2 — Mapping-LLM** (incremental, chunk a chunk):
- Construye un **Prompt Cache** que mapea aliases → canonical names con auxiliary descriptions.
- Cada chunk recibe el cache acumulado hasta ese punto: `{r_{ij+1}, a_{ij+1}} = Mapping-LLM(e_ij, d_ij, r_ij, a_ij, p-map)`.
- Manejo explícito de tres patrones críticos:
  - **Plural mentions**: solo se resuelve a nombres canónicos si **todos** los individuos son nombrados explícitamente; si no, → `null` (decisión conservadora pro-precisión).
  - **Shifting references**: usa contexto inmediato ("the driver in a truck" vs "the driver in a patrol car") para discriminar entre referentes distintos del mismo alias.
  - **Vague aliases**: si no se pueden anclar, → `null`.
- Opcional: **gleaning step** = segunda pasada con el cache global para revisar mappings tempranos a la luz del contexto posterior.
- Output: JSON estricto `RESOLVED_ENTITIES` y `AUXILIARY_DESCRIPTIONS`.

**Stage 3 — Resolve-LLM** (por chunk):
- Reescribe cada chunk substituyendo aliases por nombres canónicos.
- Si un alias mapea a múltiples entidades, inserta el string concatenado.
- Auxiliary descriptions ayudan a desambiguar pero no se incluyen en el output.
- Prompt prohíbe explícitamente alucinación / inferencia más allá del mapping.
- Formalización: `x^resolved_ij = Resolve-LLM(x_ij, R, A, p-resolve)`.
- Los chunks resueltos se mergean para producir el texto resuelto del tipo, que es input del siguiente tipo (loop sobre 7 tipos).

**KG Construction** (idéntico a CORE-KG): GraphRAG con prompt unified que ordena la extracción por tipo + filtering de government-related + definiciones de tipo + few-shot. Output en NetworkX, GraphML, Parquet.

**Inspirado en LLMLINK [Zhu et al. 2025]** (dual LLMs + reference tracking) pero con prompt cache **type-specific** en lugar de un solo cache global, lo cual reduce token usage y bias de mezclar tipos.

**Stack:** LLaMA 3.3 70B vía Ollama, NVIDIA A100 80GB, GraphRAG v0.3.2, chunks de 300 tokens, temperatura = 0, Python 3.12.

## Dataset / Dominio
- **Fuente**: Nexis Uni (judicial cases U.S. federal y state, 1994–2024).
- **Cantidad**: 16 casos seleccionados al azar con query `"human smuggling OR alien smuggling"`.
- **División por longitud**:
  - 7 documentos **cortos** (≤ 2.500 palabras).
  - 9 documentos **largos** (> 2.500 palabras).
- **Sección procesada**: solo "Opinion".
- **Idioma**: inglés.
- **Anonimización**: nombres reemplazados por iniciales tipo "L.R.C.".

## Métricas
- **Node Duplication Rate**: porcentaje de entidades duplicadas (cluster cardinality > 1) sobre total. Detección por `partial_ratio` de RapidFuzz ≥ 75 % + revisión manual SME.
- **Noise Rate**: porcentaje de entidades irrelevantes (boilerplate legal: court, jury, sentencing hearing, etc.) sobre total, evaluado por SME.
- Cualitativo: análisis de misclassifications.

## Resultados principales

**Documentos cortos (7 casos, promedio):**
| Modelo | Total ent. | Dup. (%) | Noise (%) |
|---|---|---|---|
| GraphRAG | 69,57 | 27,02 | 23,59 |
| CORE-KG | 36,43 | 17,00 | 12,41 |
| **LINK-KG** | **34,71** | **10,61** | **12,28** |

**Documentos largos (9 casos, promedio):**
| Modelo | Total ent. | Dup. (%) | Noise (%) |
|---|---|---|---|
| GraphRAG | 143,56 | 36,01 | 40,71 |
| CORE-KG | 59,89 | 26,10 | 22,82 |
| **LINK-KG** | **58,44** | **17,78** | **17,57** |

**Mejoras relativas (LINK-KG vs cada baseline):**
- Cortos: −60,72 % dup vs GraphRAG, −37,59 % vs CORE-KG; −47,96 % noise vs GraphRAG, −1,05 % vs CORE-KG (mejora marginal).
- Largos: −50,63 % dup vs GraphRAG, −31,86 % vs CORE-KG; −56,83 % noise vs GraphRAG, −23,00 % vs CORE-KG.
- **Promedios globales reportados**: −45,21 % dup, −32,22 % noise vs baseline methods.

Resultados cualitativos destacados:
- Case 20: maneja plurales como "the agents", "the border patrolmen" mapeándolos a `S.P. and A.B.`; resuelve "the occupants" / "the passengers" a la lista completa cuando todos están nombrados.
- Case 16: distingue tres tribunales (U.S. District Court, U.S. Supreme Court, U.S. Court of Appeals) usando contexto, no aplicando la canonical entity más cercana ciegamente.

## Limitaciones reconocidas por los autores
- Solo 16 documentos.
- LINK-KG ocasionalmente igualado o ligeramente superado por CORE-KG en docs cortos cuando el total de entidades es bajo (Cases 2, 3, 5).
- Evaluación cualitativa+estructural, no down-stream.

## Limitaciones NO reconocidas (lectura crítica)
- **Self-baseline circular**: comparan contra su propia versión previa (CORE-KG) tuneada. Sin baseline externo independiente.
- **Costo computacional alto**: 3 LLM calls por chunk por tipo (Stage 1 + 2 + 3), más opcional gleaning que dobla Stage 2. Para 7 tipos × N chunks × 3 LLM calls + gleaning, el costo escala muy rápido. Ningún costo/latencia reportado.
- **Sample size todavía pequeño** (16 vs los 20 de CORE-KG). Sin tests de significancia ni intervalos de confianza.
- **Total de entidades varía mucho entre métodos**, lo que distorsiona la interpretación de los porcentajes. Por ejemplo, Case 11: GraphRAG extrae 149 entidades, CORE-KG 37, LINK-KG 64. Con números tan distintos, comparar duplication rate es engañoso — LINK-KG podría estar siendo más agresivo y colapsando entidades legítimamente distintas.
- **No miden recall**: si LINK-KG sub-extrae (menos total entities) podría perder información relevante; las métricas no lo capturan.
- **No ablation entre stages 1/2/3**: ¿cuánto aporta cada uno? ¿el gleaning step es realmente necesario? No se sabe.
- **No comparan sin Prompt Cache**: la innovación principal supuestamente es el cache, pero no hay variante sin cache.
- **Decisión conservadora en plurales**: mapear plurales a `null` cuando no todos están nombrados puede inflar artificialmente la calidad por exclusión, no por resolución.
- **Single LLM (LLaMA 3.3 70B)**: no se evalúa transferibilidad a otros modelos.
- **Loss-in-the-middle no se mide directamente**: se cita como motivación pero no se cuantifica el problema en CORE-KG ni se demuestra que el remedio aborda específicamente eso.
- **Same anonimización** que CORE-KG: dificulta verificación independiente.
- **Sin QA / faithfulness / sin evaluación end-to-end**: el grafo es output, no insumo.
- **Schema cerrado** de 7 tipos para smuggling. Reusabilidad fuera del dominio no demostrada.
- **300-token chunks** es un default pequeño; modelos modernos manejan 4k–128k tokens. La elección no se justifica empíricamente.
- **Naming conventions inconsistentes**: en código se llama LinkKG-HS, en paper LINK-KG. Tipográficamente confuso.

## Relevancia para mi tesis
**Qué tomar prestado:**
- **Prompt Cache type-specific**: la idea de mantener un cache persistente alias→canonical por tipo es altamente aplicable a normativa BCRA. En el corpus regulatorio, "la entidad", "el sujeto obligado", "la institución financiera" pueden referirse a distintas clases de bancos según contexto; un cache por tipo (`EntidadFinanciera`, `OperaciónFinanciera`, `TipoDeRiesgo`) ayuda a mantener coherencia.
- **Pipeline trifásico (NER → Mapping → Resolve)**: arquitectura clara y replicable. Para BCRA puedo adaptarlo a (extracción de menciones → mapping a artículos canónicos → reescritura).
- **Manejo explícito de plurales**: en BCRA hay "los sujetos", "las entidades del Grupo A" — patrones plurales con resolución condicional al contexto; vale la pena adoptar la regla "solo resolver si todos están nombrados".
- **Gleaning step**: pasada de refinamiento global. Útil para corregir mappings tempranos cuando aparecen pistas más adelante.
- **Comparación short vs long documents**: el Digesto BCRA tiene Comunicaciones que van de 1 a 80+ páginas; replicar el split corto/largo y reportar resultados separados es metodológicamente sólido.
- **Prompts JSON estrictos + validación**: práctica defensiva replicable.
- **Mismo stack de CORE-KG**: GraphRAG + Ollama + LLaMA. Open-source y replicable.

**Qué hueco deja para mi novedad:**
- **Cero evaluación funcional / QA / RAG**: hueco persistente.
- **Cero análisis de costo computacional**: con tres LLM calls por chunk por tipo, esto es prohibitivo en producción. Mi tesis puede medir trade-off precision/cost.
- **Dominio smuggling penal vs regulación financiera**: oportunidad de novedad por dominio + idioma.
- **No abordan versiones temporales** (Comunicación A modificada por otra A posterior). Mi tesis sí debe.
- **No comparan con vector-RAG**: hueco que mi tesis cubre directamente.
- **Total de entidades varía sin control**: yo puedo reportar precision Y recall sobre un golden subset anotado por mí.
- **No prueban con otros LLMs**: oportunidad de robustez.
- **No publican un dataset anotado open**: yo puedo aportar un eval set BCRA público.
