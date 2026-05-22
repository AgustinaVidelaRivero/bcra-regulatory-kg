# Huecos en la literatura procesada — oportunidades para mi tesis BCRA

Lectura crítica de los siete papers (00–06). Cada hueco se respalda con presencia/ausencia en al menos dos referencias procesadas. Sin huecos genéricos tipo "se necesita más investigación".

---

## Hueco 1 — Faithfulness y citation accuracy nunca se miden cuantitativamente

**Evidencia en la literatura:**
Ninguno de los siete papers reporta una métrica cuantitativa de fidelidad de la respuesta a la fuente (faithfulness, FActScore, RAGAS Answer Faithfulness/Context Recall) ni de citation accuracy (la respuesta cita correctamente la sección/artículo que la fundamenta). Concretamente:
- **00 (RAGulating)** reporta solo *Section Overlap* (un proxy de retrieval recall) y *Answer Accuracy* en escala Likert 1–5 evaluada por LLM-judge — no mide en qué proporción la respuesta efectivamente puntea al texto fuente correcto. La función `Λ` da provenance a las tripletas, pero esa provenance no se evalúa.
- **04 (VAW)** usa Competency Questions con scoring 0–5 ad-hoc no estandarizado y solamente sobre 13 CQs.
- **01, 02, 03, 05, 06** se quedan en construcción de KG y no producen respuestas a preguntas — directamente no aplica.

**Por qué es un hueco real:**
La motivación principal de KG-RAG sobre regulación es justamente reducir alucinaciones y permitir trazabilidad. Si nadie mide estas dimensiones rigurosamente, la justificación de KG-RAG sobre vector-RAG se queda en intuición. El paper RAGulating, que es el más cercano en espíritu al mío, usa una métrica cualitativa débil (Likert 1–5) y un proxy de retrieval (overlap) que da resultados ambiguos según el threshold. RAGulating no diferencia entre "respondió correctamente" y "respondió correctamente citando el artículo correcto" — la segunda es la que importa para credit scoring justificable bajo BCRA.

**Cómo lo llena mi tesis:**
- Reportar **faithfulness** medido con RAGAS *answer_faithfulness* y FActScore sobre un eval set BCRA.
- Reportar **citation accuracy** específicamente: dado que cada respuesta debe citar la Comunicación A + artículo + inciso fuente, qué proporción de respuestas cita el correcto (precision/recall sobre la cita en sí).
- Comparar tres niveles: (a) sin RAG, (b) vector-RAG, (c) KG-RAG con provenance.
- Anotar el eval set manualmente con las fuentes ground-truth para que las métricas no dependan de LLM-judges.

---

## Hueco 2 — Comparación cabeza a cabeza KG-RAG vs vector-RAG con baselines fuertes e independientes

**Evidencia en la literatura:**
- **00 (RAGulating)** compara únicamente "con tripletas" vs "sin tripletas" *en su propio sistema*; no compara contra GraphRAG (Microsoft), ni vector-RAG con embeddings off-the-shelf (OpenAI ada/text-embedding-3-large, BGE-M3, Cohere), ni hybrid retrieval.
- **04 (VAW)** compara bottom-up vs LLM-based pero ambos son métodos de **construcción** de KG, no comparan KG-RAG vs vector-RAG en QA. Más aún, el pipeline LLM ni siquiera produce instancias del KG (solo ontología vacía).
- **05 (CORE-KG)** compara solo contra GraphRAG vainilla, sin baselines externos. **06 (LINK-KG)** compara contra GraphRAG y CORE-KG (auto-baseline). Ambos miden estructura del grafo, no QA.
- **01, 02, 03** no comparan contra ningún sistema RAG.

**Por qué es un hueco real:**
La pregunta científica básica de mi tesis ("¿KG-RAG es mejor que embedding-RAG para QA regulatoria?") no tiene respuesta empírica clara en la literatura. Los papers que comparan algo, comparan o consigo mismos (RAGulating, LINK-KG) o métodos de construcción equivalentes pero incompatibles (VAW). Sin un experimento head-to-head con baselines fuertes y bien tuneados, las afirmaciones del campo son auto-confirmatorias.

**Cómo lo llena mi tesis:**
- Definir explícitamente los baselines: (a) **vector-RAG vainilla** con BGE-M3 + chunks de 512 tokens, top-k=5; (b) **vector-RAG hybrid** (BM25 + dense); (c) **GraphRAG** (implementación de Microsoft); (d) **mi propuesta KG-RAG** con esquema BCRA.
- Mismo LLM generador para los cuatro (Claude o GPT-4o), mismo conjunto de preguntas, misma rúbrica de evaluación.
- Reportar para cada uno: faithfulness, citation accuracy, retrieval recall@k, latency, cost. Sin cherry-picking de threshold.

---

## Hueco 3 — Ningún experimento sobre castellano técnico-financiero / regulación financiera latinoamericana

**Evidencia en la literatura:**
- Cinco de los seis papers (00, 01, 02, 04, 05, 06) son inglés. Uno (03) es chino sobre derecho penal.
- Cero papers sobre regulación bancaria/financiera en castellano. Cero papers sobre regulación de Banco Central / autoridad monetaria de cualquier país.
- El paper más cercano por dominio (00 RAGulating) es FDA/healthcare/pharma, no banca. El segundo más cercano (01 KG-Anchored IE) es Federal Register US bancario, pero pre-LLM era y sin evaluación.

**Por qué es un hueco real:**
La performance de un LLM en NER/RE/coreference depende fuertemente del idioma y del registro técnico. La normativa BCRA tiene características que no se capturan en los corpus de los papers procesados:
- Jerga financiera específica (previsionamiento, calidades de deudor, exposición ponderada por riesgo).
- Estructura jerárquica artículo / inciso / sub-inciso / acápite.
- Referencias cruzadas frecuentes entre Comunicaciones (Com. A 7146 modifica Com. A 5398, etc.).
- Castellano formal/legal con préstamos del inglés financiero (Basel III, IFRS).
Sin evidencia sobre castellano regulatorio, no se sabe si los métodos propuestos en inglés (extracción schema-light de RAGulating, prefix-tuning de JKEM, prompt cache de LINK-KG) transfieren con la misma calidad. Es plausible que la performance caiga significativamente y que los problemas de fragmentación/duplicación sean distintos.

**Cómo lo llena mi tesis:**
- Es un experimento empírico per se: aplicar las técnicas propuestas a corpus BCRA (castellano) y reportar qué cambia.
- Idealmente comparar el mismo método sobre un sub-corpus en inglés (e.g., paraphrase del marco normativo Basilea) para aislar el efecto del idioma.
- Documentar los modos de falla específicos del castellano financiero (e.g., concordancia de género en relaciones, nominalizaciones tipo "el otorgamiento", siglas BCRA-específicas como LIBO o LELIQ).

---

## Hueco 4 — Versionado temporal e incremental update mechanisms

**Evidencia en la literatura:**
- **00 (RAGulating)** declara como future work: *"Regulatory corpora often change rapidly... We aim to develop incremental update mechanisms... minimizing downtime and ensuring continuous compliance coverage."* No implementado.
- **03 (JKEM)** menciona *"the need for continuous updates to reflect the latest legal developments"* en future work.
- **04 (VAW)** indica future work sobre extensión y unificación de KGs entre dominios pero no aborda el caso "una norma que enmienda otra".
- **05 (CORE-KG) y 06 (LINK-KG)** simplemente ignoran el problema temporal — los casos legales de smuggling tienen fecha pero no se modela versión.
- **01 y 02** no aplica (no hay ciclo de vida del KG).

Ningún paper modela explícitamente:
- Qué hacer cuando una norma supersede / modifica / deroga otra.
- Cómo razonar sobre "qué decía la regulación en 2022" vs "qué dice ahora".
- Cómo decidir si una respuesta debe mencionar la norma derogada (porque aplica a una operación pasada) o solamente la vigente.

**Por qué es un hueco real:**
La normativa BCRA se actualiza constantemente. Las Comunicaciones A se enmiendan, sustituyen, dejan sin efecto. Una pregunta como "¿qué requisitos de previsionamiento aplican al deudor X clasificado en agosto 2024?" requiere razonar sobre la versión vigente *en esa fecha*, no la actual. Un sistema KG-RAG que ignore versionado va a contestar con la norma actual aunque esa norma no aplicara al caso evaluado — error invisible para métricas de QA simples pero crítico para compliance.

**Cómo lo llena mi tesis:**
- Modelar explícitamente en el schema BCRA propiedades de versión: `vigenteDesde`, `vigenteHasta`, `modificadoPor`, `derogadoPor`.
- Implementar al menos una pregunta tipo "as-of-date" en el eval set ("según la regulación vigente al 2023-06-01, ¿qué tasa de previsionamiento corresponde a un deudor en situación 3?").
- Reportar performance separada para preguntas as-of-current vs as-of-date.
- En el PPF1 puede plantearse como contribución "scope incremental" — abordar el subset estable primero, dejar las consultas históricas como entrega 2.

---

## Hueco 5 — Costo, latencia y throughput nunca reportados

**Evidencia en la literatura:**
- **00 (RAGulating)**: pipeline de 7 agentes secuenciales — sin reporte de tokens, costo USD ni latencia.
- **02 (Carta)**: O(N · |E|) llamadas al LLM por documento — costo no reportado.
- **04 (VAW)**: GPT-4o + Mixtral 8x22b vía API en pipeline iterativo — sin métricas de costo.
- **05 (CORE-KG)**: 7 prompts secuenciales por chunk — costo no reportado.
- **06 (LINK-KG)**: 3 prompts × 7 tipos × N chunks + opcional gleaning. Costo computacional alto reconocido implícitamente pero no medido.
- **01, 03**: no aplica el mismo sentido (pre-LLM o prefix-tuning con un solo modelo); pero JKEM tampoco reporta tiempo de fine-tuning.

**Por qué es un hueco real:**
Para que mi tesis tenga relevancia más allá de lo académico, un sistema KG-RAG debe ser costo-efectivo en producción. Si construir el KG cuesta US$ 50.000 en API calls de GPT-4o pero el vector-RAG cuesta US$ 500 con embeddings, la pregunta práctica no es "¿KG-RAG es más fiel?" sino "¿la mejora en fidelidad justifica el aumento de costo?". Ningún paper permite responder esto. Para una tesis que se posiciona en la intersección entre IA y aplicación financiera, este es un punto fácil de aportar y diferenciador.

**Cómo lo llena mi tesis:**
- Reportar para cada método evaluado: **(a)** costo de construcción del KG (USD si se usa API, GPU-horas si es self-hosted); **(b)** costo por pregunta en QA inferencia; **(c)** latencia mediana y p95 por pregunta; **(d)** tokens consumidos.
- Idealmente, gráfico de Pareto: faithfulness vs costo. Si KG-RAG es Pareto-superior a vector-RAG, el resultado es robusto. Si está en la frontera pero no domina, queda como recomendación condicional.

---

## Resumen de la novedad de la tesis frente a la literatura procesada

| Dimensión | Estado en literatura | Mi aporte |
|---|---|---|
| Faithfulness/citation accuracy | No medidas cuantitativamente | Métricas estándar (RAGAS, FActScore) + métrica propia de citation accuracy |
| KG-RAG vs vector-RAG head-to-head | No existe con baselines fuertes | Cuatro baselines bien tuneados sobre el mismo corpus y eval set |
| Castellano regulatorio financiero | Cero papers | Primer estudio sobre BCRA |
| Versionado temporal | Solo declarado como future work | Modelado en schema y al menos un sub-experimento |
| Costo/latencia | Nunca reportado | Pareto de fidelidad-vs-costo |

Cinco huecos = cinco apartados naturales del PPF1 para argumentar contribución. No hace falta cubrir los cinco completos — abrir tres bien y dejar dos como future work declarado es una tesis honesta y bien delimitada.
