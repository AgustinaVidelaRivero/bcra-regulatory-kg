# 02 — Iterative Zero-Shot LLM Prompting for Knowledge Graph Construction

## Cita (IEEE)
S. Carta, A. Giuliani, L. Piano, A. S. Podda, L. Pompianu, and S. G. Tiddia, "Iterative Zero-Shot LLM Prompting for Knowledge Graph Construction," *arXiv preprint* arXiv:2307.01128v1, Jul. 2023. [Online]. Available: https://arxiv.org/abs/2307.01128

## TL;DR
Pipeline para construir KGs sobre texto no estructurado usando exclusivamente GPT-3.5 con prompts zero-shot iterativos, sin ejemplos ni KBs externos. Decompone el problema en tres etapas (extracción de tripletas candidatas, resolución de entidades/predicados, inferencia de esquema) y reporta P/R/F1 altos sobre un corpus turístico de Cerdeña. La mayor debilidad es que no compara contra ningún baseline y solo evalúa en un dominio acotado de 44 páginas.

## Problema que ataca
La construcción automática de KGs requiere combinar NER + RE + entity resolution + schema design, con métodos típicamente supervisados que dependen de anotación humana, ontologías predefinidas o KBs externas (como DBpedia). Esto restringe la escalabilidad y portabilidad a dominios nuevos. El paper apunta a generar KGs sin anotaciones humanas, sin ejemplos few-shot y sin recursos externos.

## Propuesta técnica
El sistema es una secuencia de prompts a GPT-3.5-turbo-0301 (temperatura = 0 para determinismo) organizada en tres módulos:

1. **Candidate Triplet Extraction**: el texto se parte en chunks deslizantes con un *summary* acumulativo entre chunks para preservar contexto global. Por cada chunk se ejecutan tres prompts: (a) extracción de entidades (cada una con label, descripción y lista de tipos/hiperónimos); (b) "Phrase Selection + Mention Recognition + Relation Extraction" iterativo entrada por entidad — para cada entidad e_i se selecciona la sub-porción de texto T_iG que la describe, se identifican qué otras entidades del set E aparecen en T_iG (usando una lista numerada con respuestas yes/no) y luego se extraen tripletas RDF entre ellas; (c) "predicate description" final para canonicalizar el predicado con una descripción genérica (no instance-specific).

2. **Entity/Predicate Resolution**: clustering por similitud combinada (Levenshtein del label + cosine sobre embeddings con Universal Sentence Encoder de la descripción + similitud de tipos para entidades). Pesos empíricos α=0.35, β=0.65 (entidades) y γ=0.25, δ=0.75 (relaciones). Umbrales también empíricos. Cada cluster va a un prompt de "cluster disambiguation" donde GPT-3.5 separa los subconjuntos verdaderamente equivalentes; un tercer prompt ("concept shrinkage") elige una etiqueta única para representar al grupo.

3. **Schema Inference**: bottom-up. A partir de los tipos asociados a entidades, se prompt-genera un hipernónimo común por cluster ("hypernym generation"), se mergean entre clusters ("hierarchical agglomeration") y se itera hasta llegar a un único cluster raíz. La relación entre niveles es siempre `is type of`.

Cada respuesta del modelo pasa por dos validaciones automáticas: (i) *pattern matching* con regex sobre el formato pedido y (ii) *consistency check* sobre el preserve de pares label/ID en listas numeradas.

## Dataset / Dominio
- SardegnaTurismo (sitio oficial de turismo de Cerdeña, versión inglesa).
- 44 páginas focalizadas en Cagliari y alrededores.
- Promedio ~660 tokens por documento, máximo ~1.100 tokens (cabe en una sola ventana de GPT-3.5; **no se prueba el split de texto**).
- Idioma: inglés.
- Dominio: turismo (open-domain según los autores; en la práctica, single-domain).

## Métricas
- **P_E**: precisión de entidades.
- **R_E**: recall de entidades (estimado contra una "ground truth de entidades omitidas" construida por los anotadores en base a los tipos extraídos).
- **F1_E**: F-score de entidades.
- **P_T**: precisión de tipos asignados a entidades.
- **P_R**: precisión de tripletas (no se mide recall de tripletas — los autores lo justifican por costo de anotación).
- **σ_E** y **σ_R**: porcentaje de descripciones de entidad / relaciones que provienen del conocimiento interno del LLM en lugar del texto (proxy de alucinación).

## Resultados principales
KG generado: **761 entidades**, **616 tripletas**, **~500 nodos de esquema**, **~600 aristas de esquema**.

| Métrica | P_E | R_E | F1_E | P_T | P_R | σ_E | σ_R |
|---|---|---|---|---|---|---|---|
| Score (%) | 98,82 | 93,18 | 95,92 | 85,71 | 75,31 | 9,20 | 0,00 |

Sin tabla comparativa contra baselines.

## Limitaciones reconocidas por los autores
- "There are yet no proven state-of-the-art tools to assume as a baseline" — no comparan con nada.
- Solo se midió recall para entidades, no para tripletas (anotar todas las relaciones omitidas es prohibitivo).
- No se probó el módulo de text-split porque los documentos individuales caben en la ventana de GPT-3.5.
- Trabajo "preliminar"; planean comparaciones futuras.

## Limitaciones NO reconocidas (lectura crítica)
- **Ground truth construido por los mismos autores y dependiente del schema extraído por el modelo**: la lista de entidades "missed" se restringe a los tipos que el propio modelo extrajo. Esto sesga el recall hacia arriba — entidades de tipos no descubiertos no cuentan como faltantes.
- **El experimento es sobre un único dominio acotado (turismo)**, lo que contradice la afirmación "open-domain" del título. Su pipeline asume implícitamente texto descriptivo simple; no se prueba sobre dominios técnicos, jurídicos ni regulatorios.
- **Costo y latencia ignorados**: el pipeline hace O(N · |E|) llamadas al LLM por documento (una por cada entidad para Phrase Selection + Mention Recognition + Relation Extraction). Para corpus grandes esto es financieramente y temporalmente prohibitivo, pero no se reporta cost/throughput.
- **σ_R = 0 % es engañoso**: significa que no se detectaron relaciones inferidas del conocimiento del modelo, no que no haya alucinaciones. El 24,69 % de tripletas incorrectas (1 − P_R) sigue siendo ruido.
- **Pesos de similitud y umbrales empíricos sin barrido sistemático**: α, β, γ, δ y los thresholds de clustering se fijaron a ojo. Sin análisis de sensibilidad.
- **Single LLM (GPT-3.5)**: no se evalúa robustez a otros modelos. Los prompts pueden ser muy específicos a esa familia.
- **No hay QA ni evaluación down-stream**: el KG no se usa para nada (RAG, búsqueda, razonamiento). Es solo construcción.
- **Reproducibilidad**: el paper menciona los prompts pero no los publica completos en el cuerpo; el lector queda sin la receta exacta.
- **Inter-annotator agreement no reportado** para "several assessors".
- **Multilingüismo no abordado**: solo inglés. La pipeline depende de la calidad del LLM en el idioma destino.

## Relevancia para mi tesis
**Qué tomar prestado:**
- **El patrón "iterative zero-shot prompting"** es directamente aplicable a la extracción sobre normativa BCRA: en vez de pedirle a un LLM "extraé todas las tripletas" de una Comunicación A entera, segmentar en chunks, pedir entidades primero, y luego iterar tripleta por tripleta entidad por entidad.
- **La idea de canonicalizar predicados con descripción genérica** (no instance-specific) es importantísima para que el KG sea consultable: en regulación BCRA queremos predicados como `requiere_previsionamiento_de` o `regula_a`, no `dice_que_los_bancos_deben_X`.
- **Validación automática por regex + consistency check sobre listas numeradas**: esquema barato de aplicar y reduce tripletas mal formadas.
- **Esquema bottom-up via hypernym generation**: si decido construir el schema BCRA inductivamente en lugar de a mano, este es un punto de partida.
- **Sigma score como proxy de hallucination**: una métrica simple y barata que puedo incluir.

**Qué hueco deja para mi novedad:**
- **Cero comparación contra otros métodos**: mi tesis puede aportar exactamente lo que ellos faltan — comparar KG-RAG contra embedding-RAG (y opcionalmente contra OpenIE+KG, ClauseIE+KG).
- **Dominio turístico ≠ regulación financiera en castellano**: aplicar y adaptar la metodología es contribución per se, especialmente porque la jerga BCRA y la estructura artículo/inciso tienen restricciones que no aparecen en texto turístico libre.
- **No miden faithfulness ni citation accuracy en QA**: mi tesis sí debe medirlas con métricas estándar (RAGAS, FActScore, manual eval con anotadores).
- **Costo no reportado**: para ingeniería en producción (scoring crediticio justificable), el costo del KG construction matters. Mi tesis puede medirlo y reportarlo como parte de la comparación.
- **Single-LLM dependency**: puedo evaluar con varios LLMs (GPT-4o, Claude, Llama-3) y reportar variabilidad.
