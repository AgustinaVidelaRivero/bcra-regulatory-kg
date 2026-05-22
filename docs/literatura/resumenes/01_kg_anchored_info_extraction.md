# 01 — Knowledge Graph Anchored Information Extraction for Domain-Specific Insights

## Cita (IEEE)
V. Khetan, K. M. Annervaz, E. Wetherley, E. Eneva, S. Sengupta, and A. E. Fano, "Knowledge Graph Anchored Information Extraction for Domain-Specific Insights," *arXiv preprint* arXiv:2104.08936v2, Apr. 2021. [Online]. Available: https://arxiv.org/abs/2104.08936

## TL;DR
Pipeline NLP pre-LLM (bi-LSTM-CRF + Semantic Role Labeling + extractor de relaciones basado en verbos + OpenIE/ClauseIE) que construye un KG sobre regulación financiera de EE. UU. para detectar cambios en umbrales regulatorios. La novedad declarada es el enfoque "task-based": en vez de modelar todo el dominio, se construye un data-model pequeño anclado a una tarea específica. Es un short paper exploratorio sin métricas cuantitativas reportadas y sin comparación contra baselines.

## Problema que ataca
Las regulaciones bancarias en EE. UU. tienen >180.000 páginas en el Federal Register, se actualizan constantemente, y a 2020 se proyectaban más de US$ 100 mil millones anuales en costos de cumplimiento global. Detectar cambios relevantes manualmente no escala; los autores quieren extraer "lo justo" para enfocar la atención humana en el contenido relevante.

## Propuesta técnica
Construyen un KG semi-automáticamente desde un corpus textual del dominio bancario regulatorio. El pipeline tiene tres etapas:

1. **Modelo de datos task-specific**: definen 7 tipos de entidad relevantes para "cambio en umbral regulatorio" (regulated_activity_threshold, regulatory_authority, etc.). Etiquetan manualmente 131 artículos del Federal Register, anotando ~4.500 oraciones con instancias por entidad que van de 561 (mínimo) a 6.752 (máximo).
2. **Extracción automática**: tres modelos en paralelo: (a) SRL atencional de Tan et al. para identificar predicados y roles, (b) bi-LSTM-CRF entrenado sobre la data anotada + CoNLL 2017 para NER, (c) extractor de relaciones verb-based de Hao et al. Solo se conservan las entidades extraídas por SRL **y** por el NER (intersección). Después se generan tripletas para cada par de entidades.
3. **Construcción del KG**: las tripletas del data-model se enriquecen con OpenIE y ClauseIE (extracción más promiscua) y se mergean con el dataset NIC (FFIEC) que aporta relaciones entre agencias regulatorias, bancos, holdings, etc. El usuario recibe notificaciones por reglas manuales o por similaridad WordNet entre el rol del usuario y los metadatos.

Es un sistema de IE clásico de la era pre-LLM, sin embeddings densos modernos ni transformers. La "novedad" declarada es el principio de hacer un schema reducido orientado a tarea en lugar de una ontología completa del dominio.

## Dataset / Dominio
- Federal Register articles (regulación financiera EE. UU., inglés).
- Title XII del U.S. Code of Federal Regulations (XML masivo).
- National Information Center / FFIEC: catálogo estructurado de bancos, holdings y agencias.
- Anotación: 131 artículos, ~4.500 oraciones, 7 tipos de entidad.
- Idioma: inglés.

## Métricas
**No reportadas.** Los autores explicitan: *"Quantifying results in numerical terms is difficult for the problem we are addressing"* y mencionan una métrica de "summarization" (ratio tamaño-entrada / tamaño-salida) que estaban evaluando al momento de la publicación.

## Resultados principales
- No reportado (no hay tabla de métricas, ni baselines, ni evaluación cuantitativa).
- Validación: "preliminary results, validated manually" — sin acuerdo inter-anotador, sin tamaño de muestra para validación, sin precision/recall/F1.
- Justifican que en su use case "low precision is acceptable as users are able to easily discard any superfluous information that is returned by a high recall" — pero ni siquiera reportan recall.

## Limitaciones reconocidas por los autores
- Tamaño limitado del data-model y de los datos de entrenamiento (mencionan REHession como vía a futuro).
- Trabajo "in its very early stages".
- Razonar sobre el dominio con información de calidad mixta es un desafío abierto.

## Limitaciones NO reconocidas (lectura crítica)
- **Cero evaluación cuantitativa.** No reportan F1 de NER, ni precision/recall de relaciones, ni accuracy de tripletas. Es inaceptable incluso para un short paper.
- **Sin baselines.** No comparan ni con extractores OpenIE puros ni con esquemas alternativos.
- **El argumento "high recall is fine" no se sostiene** sin una medición — podrían tener recall bajísimo y nunca se sabría.
- **El sistema de notificaciones (subscription rules manuales + WordNet) es ad-hoc.** No hay benchmark de calidad de las alertas (¿el usuario las usa? ¿son útiles? ¿hay falsos positivos?).
- **Anotación realizada por los propios autores, presumiblemente** (no se reporta inter-annotator agreement, ni se mencionan anotadores externos), lo que sesga la "validación manual".
- **No se aborda el ciclo de vida del KG** (versiones, conflict resolution cuando una regulación reemplaza a otra) — un problema crítico en regulación.
- **No hay QA ni RAG.** Es solo extracción + alertas — no se evalúa si el KG ayuda a responder preguntas factuales.
- **Pipeline deprecado**: en 2021 ya existía BERT y modelos transformer-based para NER y SRL con mejor performance que bi-LSTM-CRF y los modelos atencionales pre-transformer que usan.

## Relevancia para mi tesis
**Qué tomar prestado:**
- El **principio de schema task-specific**: en BCRA, en lugar de modelar toda la normativa, puedo modelar el subset orientado a "justificación de decisión de credit scoring" (Comunicaciones A, requisitos de previsionamiento, definición de deudor, etc.).
- La idea de **mergear datos estructurados externos** con el KG construido por extracción (en mi caso, datos del BCRA como listado de entidades financieras, comunicaciones vigentes, etc.).
- La motivación cuantitativa (>180.000 páginas, costos billonarios) es citable casi tal cual, adaptada al volumen del Digesto BCRA.
- Referencia ineludible: **ClauseIE [8] = Del Corro & Gemulla 2013**, mi mentor. Útil tanto como herramienta como acercamiento metodológico.

**Qué hueco deja para mi novedad:**
- **Idioma**: ellos trabajan en inglés sobre regulación de EE. UU.; yo en castellano sobre BCRA — dominio y lengua menos cubiertos.
- **Comparación KG-RAG vs vector-RAG con métricas**: ellos no hacen QA ni evalúan; mi tesis debe llenar exactamente ese vacío.
- **Citation accuracy / trazabilidad a artículo+inciso**: ellos no la abordan. Mi tesis puede aportar evaluación rigurosa de *faithfulness*.
- **Era LLM**: el paper es pre-LLM. Mi tesis puede mostrar cuánto cambia el cálculo cuando la extracción la hace un LLM bien promptedo, lo que conecta con los papers 02–06.
