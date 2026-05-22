# 00 — RAGulating Compliance: A Multi-Agent Knowledge Graph for Regulatory QA

## Cita (IEEE)
B. Agarwal, H. S. Jomraj, S. Kaplunov, J. Krolick, and V. Rojkova, "RAGulating Compliance: A Multi-Agent Knowledge Graph for Regulatory QA," *arXiv preprint* arXiv:2508.09893v1, Aug. 2025. [Online]. Available: https://arxiv.org/abs/2508.09893

## TL;DR
Paper industrial de MasterControl AI Research que propone un sistema multi-agente sobre regulación FDA / eCFR (healthcare, pharma, medical devices) combinando (1) construcción schema-light/ontology-free de tripletas SPO, (2) embeddings co-localizados de tripletas + sus secciones de texto fuente en una única vector DB con trazabilidad, y (3) un pipeline de QA agente. Los resultados reportados son ambiguos: la mejora con tripletas vs sin tripletas en *section overlap* depende fuertemente del umbral de similitud (mejora con θ=0,75, empeora con θ=0,50 y 0,60), y la mejora en *answer accuracy* es marginal (4,71 → 4,73 en escala 1–5). Es la referencia más directa para mi tesis BCRA pero su evaluación es débil — exactamente el hueco que mi tesis puede cerrar con métricas más rigurosas.

## Problema que ataca
Compliance regulatorio (FDA, eCFR, normativa médica/farmacéutica) requiere QA preciso, verificable y trazable. Los LLMs por sí solos alucinan y no tienen domain expertise. RAG vainilla puede recuperar fragmentos irrelevantes. ¿Cómo combinar KG estructurado + RAG + multi-agente para garantizar respuestas grounded y auditables?

## Propuesta técnica
**Tres bloques principales:**

1. **Schema-light KG construction**: rechazan ontologías predefinidas (DBpedia, YAGO) en favor de extracción bottom-up. Justifican que la regulación cambia rápido y los formatos varían. Ilustran con un sub-grafo construido sobre eCFR Chapter I, Subchapter B, Part 117, Subpart E (Withdrawal of QF Exemption) — secciones §§117.257, 117.260, 117.264, 117.267 — donde tripletas convergen sobre el mismo timeframe de "15 días para apelar".

2. **Triplet-Based Embeddings con provenance unificado**:
   - Particionado del corpus C en secciones atómicas: `Ω: C → X = {x_1, ..., x_m}`.
   - Pipeline de extracción: `Φ(Ω(C)) = {t_i = (s_i, p_i, o_i)}`.
   - Función de linking: `Λ: T → 2^X` mapea cada tripleta a sus secciones fuente — clave para trazabilidad.
   - Función de embedding `E: X ∪ T → R^d` aplicada a una representación textual concatenada `f(t_i) = concat(s_i, p_i, o_i)`.
   - Index vectorial unificado: `V = {(e_{t_i}, t_i, Λ(t_i))}`.
   - Modelo de embedding propio basado en transformer/BERT, entrenado sobre texto del eCFR.
   - **Recuperación**: dado query Q, `e_Q = E(Q)`, top-k por cosine: `T_Q = TopK(sim(e_Q, e_{t_i}))`, y se obtiene texto asociado `X_Q = ⋃_{t_i ∈ T_Q} Λ(t_i)`.
   - **Generación final**: `A = Γ(Q, T_Q, X_Q)` con un LLM que recibe pregunta + tripletas + texto.

3. **Multi-agent orchestration**:
   - Document Ingestion Agent (segmenta texto, captura metadata).
   - Extraction Agent (LLM SPO).
   - Normalization & Cleaning Agent (dedup, standardización, sinónimos).
   - Triplet Store & Indexing Agent (embed + vector DB).
   - Retrieval Agent (búsqueda semántica).
   - Story-Building Agent (compila chunks en narrativa coherente).
   - Generation Agent (respuesta final).
   - Adicionalmente: visualización interactiva del subgrafo recuperado.

## Dataset / Dominio
- **Corpus**: Electronic Code of Federal Regulations (eCFR) y FDA guidance documents.
- **Sub-corpus específico mostrado**: Title 21, Chapter I, Subchapter B, Part 117 (Current Good Manufacturing Practice, Hazard Analysis, and Risk-Based Preventive Controls for Human Food), específicamente Subpart E (Withdrawal of QF Exemption).
- **Idioma**: inglés.
- **Cantidad**: no especificado el tamaño total de tripletas / secciones / KG.
- Foco: healthcare, pharma, medical devices.

## Métricas
1. **Section Overlap**: `O(R, G) = |R ∩ G| / |R|` donde R = secciones recuperadas, G = ground-truth (sección target + sus referenciadas). Calculado a tres umbrales de similitud: θ ∈ {0,50; 0,60; 0,75}.
2. **Answer Accuracy**: escala Likert 1–5 evaluada por un LLM_eval o experto del dominio, comparando la respuesta del sistema contra la respuesta de referencia generada por LLM_gen.
3. **Navigation Metrics**:
   - **Average Degree** del grafo de tripletas.
   - **Unconnected sections** que pasan a estar conectadas vía tripletas compartidas.
   - **Average Shortest Path** entre secciones relacionadas.
4. **Triplet Overlap Across Sections**: `Nav(S') = (1/k) Σ |T(s_ij) ∩ T(s_mℓ)| / |T(s_ij) ∪ T(s_mℓ)|` (Jaccard) sobre pares relacionados.

## Resultados principales

**Tabla 1 (cuerpo del paper):**

| Métrica | Sin tripletas | Con tripletas |
|---|---|---|
| Overlap @ θ=0,50 | 0,0812 | 0,0745 |
| Overlap @ θ=0,60 | 0,2700 | 0,2143 |
| **Overlap @ θ=0,75** (stricter) | 0,1684 | **0,2888** |
| Answer Accuracy (1–5) | 4,71 | 4,73 |
| Average Degree | 1,2939 | 1,6080 |
| Unconnected → Connected | 5.014 unconnected | 5.011 connected |
| Avg. Shortest Path | 2,0167 | 1,3300 |

Conclusión narrativa de los autores: *"Triplets yield highest accuracy at higher threshold. Triplets network significantly enhances connectivity and navigation."*

## Limitaciones reconocidas por los autores
- Schema-light expone a **vocabulary fragmentation**; canonicalización y entity resolution son contramedidas.
- La calidad de extracción afecta directamente la integridad del KG.
- Razonamientos profundos o restricciones temporales pueden requerir lógica simbólica complementaria.
- Pipelines RAG requieren optimización de embedding/index/retrieval.
- Necesidad de incremental update mechanisms para corpus que cambia.
- Multi-step / chained reasoning aún limitado.

## Limitaciones NO reconocidas (lectura crítica)
- **Cherry-picking del threshold**: a θ=0,50 y θ=0,60 las tripletas **empeoran** el section overlap (0,0812→0,0745 y 0,2700→0,2143). Solo a θ=0,75 hay mejora (0,1684→0,2888). El paper destaca solamente el último número en bold ("highest accuracy"). Una lectura honesta diría que el efecto de las tripletas es no monótono y depende del umbral elegido.
- **Mejora en answer accuracy es despreciable**: 4,71 → 4,73 (Δ = 0,02 sobre 5). En cualquier estudio con N pequeño esto cae dentro del ruido. No se reportan tamaños de muestra, intervalos de confianza ni tests de significancia.
- **Sample size no reportado**: ¿cuántas secciones samplearon? ¿cuántas preguntas generaron? Imposible saber.
- **El "5014 unconnected → 5011 connected"** se presenta sin denominador. ¿De cuántas secciones totales? ¿5011 conectadas significa 99 %, 50 %, 5 %? Frase cosmética sin información.
- **Sin baseline competitivo**: solo comparan "con tripletas" vs "sin tripletas" en su propio sistema. No se compara contra GraphRAG (Microsoft), naive vector-RAG con BGE/OpenAI embeddings, ni QA-RAG estándar.
- **Custom embedding model no validado**: dicen entrenar un BERT propio sobre eCFR pero no comparan contra embeddings off-the-shelf — punto crítico para un paper de embeddings.
- **No hay análisis de costo / latencia / throughput**: 7 agentes en pipeline implican overhead. Cero datos.
- **Multi-agent claim mostly rebranding**: cada "agente" corresponde a un paso típico de RAG (chunk, extract, embed, retrieve, generate). No hay evidencia de que la modularidad-como-agentes aporte beneficio funcional sobre un monolítico.
- **Sin evaluación de hallucination tasa específica**: solo afirman cualitativamente que se reducen.
- **Sin reproducibilidad**: no publican código, datos, prompts ni el modelo de embedding entrenado. Paper industrial de MasterControl con producto comercial detrás — eso explica pero no justifica.
- **El concepto "ontology-free" se contrapone a una dicotomía falsa**: emergent schemas son inevitables si haces canonicalización; el paper mismo lo reconoce vagamente. Esquemas mínimos / partial pueden ser superiores a "ningún schema".
- **No abordan versionado temporal**: ¿qué pasa cuando una guidance de 2023 es enmendada en 2025? Mismo gap que en los demás papers.
- **El framing como compliance assistant es débil empíricamente**: nadie validó que un compliance officer use el sistema y reduzca errores. Use case está postulado, no demostrado.
- **Citation accuracy específica no medida**: dicen que provenance permite "auditing" pero no evalúan en qué proporción la respuesta efectivamente cita la fuente correcta — la métrica más relevante para mi tesis.
- **Referencias academicamente débiles**: incluyen `[FDA25]` (FDA Guidance Documents, no es paper) y `[Wei00]` (URL hacia IEEE book listing genérico). Aspecto de paper industrial con bibliografía liviana.

## Relevancia para mi tesis
**Qué tomar prestado** (este es el paper más directamente relevante):
- **Provenance-as-design**: la función `Λ: T → 2^X` que vincula cada tripleta a sus secciones fuente es exactamente el patrón que necesito para citation accuracy en BCRA. Cada tripleta extraída de la Comunicación A debe tener pointer al artículo+inciso original. Voy a copiar este diseño.
- **Triplet + text co-embedding en una sola vector DB**: simplifica la arquitectura — una sola búsqueda recupera tripletas y, vía Λ, sus textos asociados. Más limpio que mantener Neo4j separado del vector store.
- **Métrica de section overlap a múltiples umbrales**: voy a reportar yo también con θ ∈ {0,5; 0,6; 0,75} para ser comparable.
- **Métricas de navegación (Average Degree, Avg. Shortest Path)**: si las normativas BCRA tienen referencias cruzadas (las Comunicaciones A típicamente referencian artículos de la LEF, otras Com. A previas, etc.), métricas de conectividad muestran si el KG captura ese tejido.
- **Schema-light como ablation comparison**: este paper hace schema-light; mi tesis puede comparar schema-light vs schema-based directamente sobre BCRA — algo que ningún paper hace head-to-head.
- **Multi-agent decomposition** como justificación de ingeniería de software (modularidad para reentrenar componentes sin romper el resto). Útil aunque el "rebranding" sea cierto.
- **Visualización interactiva de subgrafo recuperado** como UX add-on: vale para credit scoring justifiable.

**Qué hueco deja para mi novedad** (este paper es la baseline más cercana a mi tesis):
- **Evaluación rigurosa de faithfulness/hallucination/citation accuracy**: el paper no las mide. Mi tesis sí debe (RAGAS, FActScore, manual eval).
- **Comparación cabeza a cabeza KG-RAG vs vector-RAG con baselines fuertes**: el paper solo compara "con vs sin triplets" en su propio sistema. Yo puedo comparar contra GraphRAG, QA-RAG estándar, hybrid retrieval, etc.
- **Schema-based vs schema-light en mismo corpus**: no se hace en ningún paper. Mi tesis puede aportar este experimento.
- **Idioma castellano + regulación financiera latinoamericana**: el paper es inglés + FDA/eCFR/healthcare. Extender a BCRA es contribución de dominio per se.
- **Sample size, IC, significancia**: el paper no los reporta. Yo debo hacerlo bien.
- **Reproducibilidad**: si yo publico código, datos de evaluación y prompts, ya estoy mejor que el paper de MasterControl.
- **Cost/latency/throughput**: nunca medido. Mi tesis puede aportar evidencia empírica para casos de uso productivos.
- **Versiones temporales / actualización incremental**: futuro work declarado pero no implementado. Hueco real para mi tesis dado que las Comunicaciones A se actualizan constantemente.
