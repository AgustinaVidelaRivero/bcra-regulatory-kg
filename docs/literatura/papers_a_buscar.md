# Papers citados en la literatura procesada que conviene seguir

Referencias cruzadas detectadas durante la lectura crítica de los siete papers (00–06) que merecen seguimiento por relevancia directa para mi tesis BCRA. Cada entrada: cita, justificación de tres líneas, y dónde encontrarlo.

---

## Edge et al. (2024) — *From local to global: A graph RAG approach to query-focused summarization*

**Por qué seguirlo:**
1. Es el paper original de **GraphRAG**, el framework de Microsoft sobre el que se construyen CORE-KG y LINK-KG; sin haberlo leído no puedo justificar usarlo o criticarlo como baseline en mi tesis.
2. Define el patrón "build KG with LLM → community detection → query-focused summarization" — directamente comparable al pipeline KG-RAG que mi tesis va a evaluar contra vector-RAG.
3. La implementación open-source (Microsoft graphrag library) es candidata natural a baseline competitivo y bien tuneado.

**Cómo encontrarlo:** arXiv:2404.16130 — https://arxiv.org/abs/2404.16130 — código en https://github.com/microsoft/graphrag

---

## Lewis et al. (2020) — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*

**Por qué seguirlo:**
1. Paper fundacional de RAG citado por papers 00 y 04 como referencia obligada; necesario para el marco teórico del PPF1.
2. Establece la formalización mínima sobre la que después se construyen GraphRAG, KG-RAG y todos los híbridos — sin esta cita la sección 2 del PPF1 queda coja.
3. Contiene la ablation original de retrieval contribution que sirve como template metodológico para mi propio experimento KG-RAG vs vector-RAG.

**Cómo encontrarlo:** NeurIPS 2020 — https://arxiv.org/abs/2005.11401

---

## Del Corro & Gemulla (2013) — *ClausIE: Clause-based open information extraction*

**Por qué seguirlo:**
1. Paper del mentor (Luciano del Corro); citarlo es de buena práctica académica y muestra continuidad metodológica con quien dirige la tesis.
2. ClauseIE es uno de los métodos OIE clásicos referenciados como heurística complementaria al pipeline LLM en el paper 01, y sigue siendo competitivo como baseline pre-LLM en regulación financiera.
3. Comparar la calidad de tripletas extraídas por ClauseIE vs por un LLM moderno sobre el mismo corpus BCRA es un experimento limpio y barato que aporta una pieza concreta de evidencia.

**Cómo encontrarlo:** WWW 2013, pp. 355–366 — https://dl.acm.org/doi/10.1145/2488388.2488420

---

## Pan, Luo, Wang et al. (2024) — *Unifying Large Language Models and Knowledge Graphs: A Roadmap*

**Por qué seguirlo:**
1. Survey en IEEE TKDE 2024 que mapea sistemáticamente los tres paradigmas (KG-augmented LLMs, LLM-augmented KGs, synergized) — el marco teórico que necesito para posicionar mi tesis en la sección de estado del arte.
2. JKEM (paper 03) lo cita como tabla de comparación de métodos; vale leerlo de primera mano para contextualizar mejor la dicotomía Soft Prompts / Pipelined / Fine-tuning.
3. Provee terminología canónica para el PPF1; usar las categorías que propone Pan ahorra defender vocabulario propio.

**Cómo encontrarlo:** IEEE TKDE 36(7):3580–3599 (2024) — https://doi.org/10.1109/TKDE.2024.3352100

---

## Wang et al. (2024) — *LeKUBe: A Legal Knowledge Update Benchmark*

**Por qué seguirlo:**
1. Citado por paper 04 como evidencia de que el versionado/actualización de KGs legales es un problema reconocido — directamente alineado con mi Hueco 4 (versionado temporal de la normativa BCRA).
2. Probablemente provee un benchmark estandarizado de "qué pasa cuando una norma cambia", template que puedo adaptar al ciclo de Comunicaciones A del BCRA.
3. Si su metodología es razonable, me permite reportar una métrica comparable con literatura existente en lugar de inventar una propia.

**Cómo encontrarlo:** arXiv:2407.14192 — https://arxiv.org/abs/2407.14192

---

## Schneider, Rehm, Montiel-Ponsoda et al. (2022) — *Lynx: A knowledge-based AI service platform for content processing, enrichment and analysis for the legal domain*

**Por qué seguirlo:**
1. Lynx es el proyecto europeo más cercano a lo que mi tesis hace en BCRA — KG sobre regulación (GDPR + contract compliance) — y lo citan tanto paper 03 como paper 04 como antecedente en compliance.
2. Tiene una ontología legal publicada que probablemente puede inspirar (o reusarse parcialmente para) propiedades del schema BCRA, ahorrando trabajo de modelado desde cero.
3. Es publicación en revista (*Information Systems*) con peer-review, no preprint; sirve como referencia "robusta" en la sección de estado del arte.

**Cómo encontrarlo:** *Information Systems* 106:101966 (2022) — https://doi.org/10.1016/j.is.2021.101966

---

## Kim & Min (2024) — *From RAG to QA-RAG: Integrating Generative AI for Pharmaceutical Regulatory Compliance Process*

**Por qué seguirlo:**
1. Citado por paper 00 (RAGulating) como antecedente de RAG aplicado a compliance regulatorio — el caso de uso más cercano al mío después de RAGulating mismo.
2. Si tienen métricas de evaluación sobre QA regulatorio (chatbot navegando guidelines), puedo compararlas/adoptarlas para BCRA.
3. Aporta una segunda referencia industrial sobre RAG en regulación, equilibrando el sesgo de RAGulating (también industrial / MasterControl).

**Cómo encontrarlo:** arXiv preprint 2024 — buscar título exacto en arXiv (DOI no especificado en RAGulating).

---

## Zhang & Soh (2024) — *Extract, Define, Canonicalize: An LLM-Based Framework for Knowledge Graph Construction*

**Por qué seguirlo:**
1. Citado por papers 05 y 06 como método de canonicalización LLM-driven; resuelve uno de los problemas técnicos centrales que mi tesis va a enfrentar: cómo unificar formas variantes de la misma entidad regulatoria.
2. Su framework "extract → define → canonicalize" es ortogonal a los pipelines existentes y se puede combinar con cualquier baseline; útil para ablation.
3. Si el método funciona como reportan, puedo usarlo como módulo plug-in en mi pipeline KG-RAG en lugar de reinventarlo.

**Cómo encontrarlo:** arXiv:2404.03868 — https://arxiv.org/abs/2404.03868

---

## Tamašauskaitė & Groth (2022) — *Defining a Knowledge Graph Development Process Through a Systematic Review*

**Por qué seguirlo:**
1. Paper 04 lo usa como columna vertebral metodológica — *"el enfoque general bottom-up"* que customizan; si yo voy a hacer algo parecido, conviene leer la fuente, no la versión adaptada de d'Amato.
2. Es un systematic review en ACM TOSEM 2022, cubre seis pasos canónicos de KG development; mi PPF1 puede mapear sus pasos al contexto BCRA y mostrar trazabilidad metodológica.
3. Citarlo posiciona la tesis dentro de un proceso reconocido en lugar de presentar una metodología ad-hoc — argumento fuerte ante un comité.

**Cómo encontrarlo:** ACM TOSEM 32(1):1–40 (2022) — https://doi.org/10.1145/3522586

---

## Hogan, Blomqvist, Cochez, d'Amato et al. (2021/2022) — *Knowledge Graphs* (Synthesis Lectures)

**Por qué seguirlo:**
1. Texto de referencia canónico sobre KGs (Synthesis Lectures, Morgan & Claypool, también ACM Computing Surveys 2021); lo cita el paper 04 con co-autora d'Amato (autor del paper 04 mismo).
2. Sirve para defender definiciones, terminología y diseño de schema en el PPF1 sin tener que justificar cada concepto desde cero.
3. Una sola cita académica de peso ahorra varias citas más débiles para los conceptos básicos del marco.

**Cómo encontrarlo:** *Knowledge Graphs* — Synthesis Lectures on Data, Semantics, and Knowledge, Morgan & Claypool (2022) — versión survey ACM Computing Surveys 54(4):1–37 (2021), https://doi.org/10.1145/3447772

---

## Kommineni, König-Ries & Samuel (2024) — *From Human Experts to Machines: An LLM Supported Approach to Ontology and Knowledge Graph Construction*

**Por qué seguirlo:**
1. Citado por papers 05 y 06; propone un pipeline semi-automatizado de competency questions + ontology design + RAG-based triple extraction para textos académicos — patrón reusable para regulación.
2. La idea de generar CQs antes de la ontología (en lugar de después) es un loop metodológico interesante para mi diseño de schema BCRA.
3. Si funciona en el dominio académico, vale evaluar si la transferencia al dominio regulatorio mantiene la performance — pregunta empírica concreta para una sección de mi tesis.

**Cómo encontrarlo:** arXiv:2403.08345 — https://arxiv.org/abs/2403.08345

---

## Comentario final sobre prioridades

De estas once referencias, **tres son ineludibles** para mi PPF1: **GraphRAG** (Edge 2024) por ser el baseline competitivo más obvio, **RAG original** (Lewis 2020) por ser fundacional, y **ClauseIE** (Del Corro 2013) por la conexión metodológica + mentor. Las demás caen en orden: *Pan 2024 → Tamašauskaitė 2022 → Hogan 2022 → Lynx 2022 → LeKUBe 2024 → QA-RAG 2024 → Zhang & Soh 2024 → Kommineni 2024.* Si solo tengo tiempo para tres más allá del top, priorizo Pan (marco), Tamašauskaitė (metodología) y LeKUBe (versionado).
