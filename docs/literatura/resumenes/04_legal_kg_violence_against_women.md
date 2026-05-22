# 04 — Automated Creation of the Legal Knowledge Graph Addressing Legislation on Violence Against Women

## Cita (IEEE)
C. d'Amato, G. Rubini, F. Didio, D. Francioso, F. Z. Amara, and N. Fanizzi, "Automated Creation of the Legal Knowledge Graph Addressing Legislation on Violence Against Women: Resource, Methodology and Lessons Learned," *arXiv preprint* arXiv:2508.06368v1, Aug. 2025. [Online]. Available: https://arxiv.org/abs/2508.06368

## TL;DR
Resource paper que construye un Legal KG sobre 73 sentencias del European Court of Human Rights relativas a violencia contra mujeres (proyecto PREJUST4WOMAN), comparando dos pipelines: uno bottom-up tradicional (Selenium + BeautifulSoup + RDFLib + ontología manual sobre ECLI/Wikidata) y otro basado en LLMs (GPT-4o + Mixtral 8x22b con RAG + few-shot prompting). El primer pipeline produce un KG denso (10.325 tripletas) y FAIR-compliant; el segundo, ontología-only sin instancias, evaluado con 13 competency questions sobre 5 documentos (61,5 % consistencia full-text, 56,9 % sub-part). La evaluación es mayormente cualitativa y los métodos son comparados con métricas no estandarizadas — útil como referencia metodológica más que como evidencia empírica fuerte.

## Problema que ataca
Faltan KGs legales públicos, FAIR-compliant, queryables vía SPARQL y reusables que cubran violencia de género. Las soluciones existentes en derecho (Lynx, ManyLaws) o no se interconectan con vocabularios estándar, o requieren esfuerzo manual costoso. Quieren proveer un recurso público y simultáneamente comparar metodologías de construcción.

## Propuesta técnica

**Pipeline A — Bottom-up tradicional** (6 pasos):
1. *Data collection*: Selenium 4 scrapea HUDOC (HTTP del ECHR), descarga PDF + HTML para 73 sentencias seleccionadas por expertos en derecho internacional. Identificadas con ECLI (formato `ECLI:CE:ECHR:año:fecha+caso`).
2. *Knowledge extraction*: BeautifulSoup parsea HTML; clase `ECHRDocument` envuelve cada sentencia; nombres de Estados se mapean a URIs de Wikidata.
3. *Triple generation*: 10.325 tripletas, 22 predicados distintos, 5.185 entidades distintas. Serialización en RDF/Turtle vía RDFLib (con dedup automático).
4. *Ontology creation*: comienzan formalizando 13 competency questions (CQs); reusan vocabularios existentes (ECLI, ELI, EuroVoc, SKOS, dcterms); definen clases nuevas (`DomesticLaw`, `InternationalLaw`, `StrasbourgCaseLaw`) y propiedades nuevas (`applicationNumbers`, `importanceLevel`, `respondentStates`, `involvedArticles`, `unanimousDecisionIndicators`).
5. *KG construction*: merge de tripletas; vinculación a Wikidata; visualización vía PyVis, RDF Grapher y Neo4j.
6. *SPARQL endpoint*: implementado en Flask con SPARQL 1.1 sobre RDFLib (formularios HTML para query y resultados).

**Pipeline B — LLM-based** (5 sub-pasos):
1. *Document preparation*: dos modos — (a) full-text de la sentencia, (b) sub-part curada por experto.
2. *RAG creation*: BERT-M2 (vía TogetherEmbedding de LangChain) + FAISS como vector store. Un RAG por documento sirve de "contexto no paramétrico" al LLM.
3. *Base ontology creation*: GPT-4o genera la ontología base (clases tipo `Abuse`, `LegalCase`, `ObjectProperty`); Mixtral 8x22b la enriquece iterativamente con zero-shot prompts; revisión manual final para limpiar duplicados.
4. *KG creation*: prompts few-shot por documento; merge de mini-KGs en uno unificado.
5. *CQ generation & answering*: Mixtral genera CQs desde la ontología; el mismo modelo responde con zero-shot prompts; verificación manual contra el texto fuente.

Adicionalmente describen un **NLP pipeline** (NLTK preprocess + SpaCy POS tagging + extracción subj-verb-obj), pero **solo lo aplican a un documento** como punto de comparación, no como pipeline de producción.

## Dataset / Dominio
- **Fuente**: HUDOC / European Court of Human Rights.
- **Cantidad**: 73 sentencias y decisiones en inglés (65 judgments + 8 decisions) seleccionadas por expertos en derecho internacional. Para el pipeline LLM solo 5 documentos.
- **Idioma**: inglés.
- **Dominio**: jurisprudencia europea sobre violencia contra mujeres.
- **Distribución**: dataset PREJUST4WOMAN publicado bajo CC-BY 4.0, DOI 10.5281/zenodo.15270173, registrado en LOD Cloud.

## Métricas
- **Competency Question score (0–5)**: cada CQ recibe un puntaje cualitativo entre 0 y 5 según consistencia entre la respuesta y el texto fuente (criterio de scoring no detallado en el paper).
- **Total CQ score** sobre 13 CQs × 5 puntos = 65 máximo por estrategia.
- Para el pipeline bottom-up no se da un score numérico equivalente — solo se afirma que "addressed all CQs".

## Resultados principales

**Pipeline bottom-up:**
- 10.325 tripletas, 22 predicados, 5.185 entidades.
- Ontología de 583,7 KB (rica en clases y propiedades).
- KG público en Zenodo + LOD Cloud + SPARQL endpoint funcional.

**Pipeline LLM:**
- Ontología de 6,4 KB con 12 clases, 9 object properties, 17 data properties.
- Sin instancias pobladas: "captures the conceptual structure of the domain without populated example instances".
- CQ score full-text: **40/65 (61,5 %)**.
- CQ score sub-part: **37/65 (56,9 %)**.

**Comparación cualitativa (Tabla 3 del paper)**: el bottom-up gana en precisión y alineación semántica; el LLM gana en velocidad y escalabilidad. Conclusión: son complementarios. Mixtral consistentemente generaba elementos similares en distintos documentos, sugiriendo que captura patrones estructurales — pero también que tiene poca variabilidad útil.

## Limitaciones reconocidas por los autores
- LLM-based: hallucinations, token limits, inconsistencias, requiere validación manual extensa.
- Bottom-up: labor-intensivo, dependiente de ontología predefinida, menos adaptable a patrones novedosos.
- Mixtral 8x22b incapaz de generar la ontología base sin GPT-4o como bootstrap.
- Generalidad: solo evaluado en violencia contra mujeres + ECHR; futuro trabajo extender a otros dominios.

## Limitaciones NO reconocidas (lectura crítica)
- **Métricas no estandarizadas y mal definidas**: la escala 0–5 por CQ no está documentada (¿qué significa 3?) y se aplica sobre solo 13 CQs × 5 docs = 65 puntos máximos. Un score = 3 podría querer decir cualquier cosa.
- **Comparación apples-to-oranges**: el bottom-up tiene 10.325 tripletas sobre 73 documentos; el LLM tiene una ontología sin instancias sobre 5 documentos. El "score" del bottom-up nunca se cuantifica con la misma métrica. La afirmación "ambos enfoques son complementarios" es más narrativa que evidencia.
- **El pipeline LLM no produce instancias del KG**, solo el T-Box. Eso socava la comparación: no se está comparando "construcción del KG" vs "construcción del KG", sino "construcción de KG poblado vs ontología vacía".
- **El "NLP pipeline" alternativo se aplica a un solo documento** y no se reporta su salida cuantitativa. Es un cameo, no una comparación.
- **Sample size tiny para LLM**: 5 documentos. Cualquier afirmación estadística es ruido.
- **No miden faithfulness / hallucination cuantitativamente**: solo "manual verification". Sin tasa específica de errores por categoría.
- **Multi-LLM no es una verdadera ablación**: GPT-4o y Mixtral se usan en roles distintos (uno bootstrap, otro enriquecimiento), no se compara head-to-head.
- **Costo de inferencia LLM no reportado**: ¿cuántos tokens? ¿cuánto cuesta generar el KG con GPT-4o + Mixtral?
- **No hay evaluación end-to-end de QA**: el RAG se usa para construir el KG, no para responder preguntas legales reales. La afirmación de que "predictive justice = link prediction sobre el KG" se postula pero no se pone a prueba.
- **Errores tipográficos/de redacción**: nombres de autores con orden incorrecto en la primera línea ("Didio Franceso", "Francioso Donato"), inversión que arrastra al BibTeX y que sugiere revisión liviana.
- **Selectivamente reusables**: el pipeline LLM publica código, pero la integración entre los dos pipelines (la "merge" futura) no está implementada.
- **No discuten conflict resolution** cuando una sentencia supersede a otra — crítico en derecho.
- **Citan JKEM** (paper 03 de mi lista) sin notar que tampoco evaluó downstream — la literatura de KG legal sigue circular.

## Relevancia para mi tesis
**Qué tomar prestado:**
- **El framework FAIR + competency questions** es directamente aplicable a mi tesis. Definir CQs concretas (e.g., "¿qué Comunicación del BCRA regula la clasificación de deudores en situación 2?") y validar el KG contra ellas es buena práctica metodológica defendible.
- **La comparación bottom-up vs LLM-based** es un patrón a copiar parcialmente: yo puedo presentar un pipeline schema-driven con LLM (con esquema) vs uno schema-light (LLM extrae todo) y comparar.
- **Reusar vocabularios existentes** (ECLI, ELI, dcterms, SKOS) para no reinventar — en BCRA puedo mapear a EuroVoc para conceptos económicos, plus algún vocabulario regulatorio si existe (Akoma Ntoso para legislación, FRBR para versiones).
- **SPARQL endpoint con Flask + RDFLib**: stack ligero y replicable; encaja con mi setup actual de RDFLib en el repo.
- **Tabla 3 (comparativa de paradigmas)**: la dicotomía bottom-up vs LLM-based es buen marco para el capítulo 2 de la tesis.
- **Métrica CQ como complemento (no reemplazo) de métricas de QA**: las CQs evalúan la cobertura del esquema; las métricas de QA tipo RAGAS evalúan el uso. Ambas son útiles.

**Qué hueco deja para mi novedad:**
- **No hace QA real**: el paper construye el KG y lo valida contra CQs, pero no integra con RAG para responder preguntas factuales. Mi tesis sí.
- **No compara KG-RAG vs vector-RAG**: nadie compara enfoques de retrieval en el corpus legal en este paper.
- **Idioma inglés sobre jurisprudencia europea**: falta cobertura en castellano sobre regulación financiera. Mi tesis llena esa esquina.
- **Pipeline LLM sin instancias**: yo puedo poblar instancias y comparar fielmente.
- **Faithfulness y citation accuracy**: no se miden; pueden ser mi contribución empírica central.
- **Volumen pequeño**: 73 documentos. El Digesto BCRA tiene cientos de Comunicaciones; mi tesis trabaja a más escala.
- **Ningún paper de la lista del mentor mide costo/latencia**: oportunidad clara.
