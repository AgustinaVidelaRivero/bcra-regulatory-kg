# Mapa de related work — trabajos de recurso (U-RW-consolidación)

Consolidación del trabajo de related work de la mesa de revisión. Marcas del
mapa de exigencias selladas por la autora el 28/08/2026. Las citas
archivo:línea fueron verificadas contra el repo al transcribir (2026-08-30,
sobre working tree con HEAD `0a296da`); toda discrepancia se reporta en el
informe de la unidad, no se corrige acá.

## §1. Encuadre

Esta tesis es un **trabajo de recurso** (decisión D-h): su objeto es el KG
regulatorio publicado como artefacto, no un método de extracción aislado. El
related work relevante es, por lo tanto, (a) los papers que **publican un KG
como artefacto** — en cualquier disciplina — y (b) lo que la literatura
considera metodológicamente **exigible cuando la construcción usa LLMs**. Este
mapa organiza esas exigencias y marca cuáles ya están cubiertas por el trabajo
hecho y cuáles abren deuda.

## §2. Mapa de exigencias

Formato de cada fila: **exigencia · estado · evidencia · dónde se resuelve**.

| # | Exigencia | Estado | Evidencia | Dónde se resuelve |
|---|---|---|---|---|
| 1 | Comparación contra recursos previos comparables | **CUBIERTA con matiz declarado** | La comparación existe (EV2, mismo set sellado; `docs/tablero.md` §1.b; `docs/nomenclatura_grafos.md`), pero es contra **generaciones anteriores del propio recurso**, porque no existe KG previo del dominio BCRA — la tesis debe decirlo explícitamente. | C1 (escritura). |
| 2 | Caso de estudio sobre la entidad más difícil | **CUBIERTA en material y figura laudada, pendiente de redacción** | Motivación en `docs/diseno_reextraccion_v2.md:204`, requisito U6-008 en `:299`, chequeo en `docs/diseno_ev2.md:91`, `figura_125_r1.svg` laudada y comentada en `docs/tesis/main.tex:121-135` esperando la Idea 5. | C1.1 (redacción, no investigación). |
| 3 | Precisión sobre muestra con adjudicación humana | **PARCIAL** | Respuestas cubiertas (EV2; `adjudicar.py`: fichas pregunta/respuesta/criterios = adjudicación del uso); el recurso, planificado con diseño detallado en B4 (`docs/plan_tesis.md:262-301`; B4.2 = 100 tripletas en tandas de 10, juez calibrado, laudo D-f firmado). | B4, pendiente de ejecución. |
| 4 | Precisión con intervalo de confianza | **ABIERTA** | Cero menciones a Wilson en el repo; los resultados de EV2 se reportan como fracciones peladas. Referencia: YAGO reporta con Wilson a alfa 5% y YAGO3 lo reusa por robustez en muestras chicas. | Pre-registro de B4 (B4.1, aún sin escribir — entra sin retrabajo). |
| 5 | Precisión desagregada por etapa de extracción | **ABIERTA** | B4.3 desagrega por tipo de relación y por TO pero no por etapa E0–E5; la provenance de r1 (`chunk_id`, `paginas`, `estado_e3`) y el campo `capa_pipeline` del backlog (B4.4) lo vuelven barato. Referencia: YAGO reporta precisión por heurística de extracción. | Mismo pre-registro de B4. |
| 6 | Validación contra material posterior a la construcción | **ABIERTA** | Cero menciones en el repo. Referencia: PrimeKG valida con 40 terapias FDA posteriores al corte de datos, verificando ausencia de fuga. | Candidata a B6.3 o unidad propia; a mentores. |
| 7 | Protocolo de actualización del recurso | **PARCIAL** | El circuito de releases y refinamiento existe (B2.8 en `docs/plan_tesis.md:253`, principio 9, release r2, backlog+intake); el hueco real es el protocolo ante **cambio normativo** (el TO cambia: ¿qué pasa con el grafo?). Referencia: PrimeKG publica instrucciones de reconstrucción ante fuentes cambiantes. | B2.8 + C1 (limitaciones o trabajo futuro). |
| 8 | Disponibilidad con identificador persistente + FAIR | **ABIERTA en ejecución, con el qué y el dónde ya decididos** | C2.1 (`docs/plan_tesis.md:442`) especifica release etiquetado + Zenodo/DOI con grafos, sets sellados, gold, scripts y README; falta ejecutarlo y un checklist FAIR explícito. Referencia: el KG legal de violencia de género (paper 04 del proyecto) publica RDF con CC-BY, endpoint y código, y valida con competency questions. | C2.1. |
| 9 | Validación por tarea downstream | **CUBIERTA** | El agente RAG es exactamente eso. Referencia: PrimeKG y MedKGent validan por tarea. | —. |
| 10 | Posición schema-based vs schema-free | **ABIERTA EN CURSO** | Es lo que el carril ESQ resuelve (`docs/plan_tesis.md:303`, T1 bloqueante de B5/B6). Referencia: la survey arXiv:2510.20345 organiza el campo en esos dos paradigmas. | ESQ-3. |

## §3. Lecturas de la reunión — estados finales

Estados finales de la barrida en diagonal (actualizados también en
`docs/lecturas_reunion_2026-08-26.md`):

- **L3** = YAGO (WWW 2007, DOI 10.1145/1242572.1242667) — **leída en diagonal**.
- **L4** = YAGO2 (*Artificial Intelligence* 194, 2013, DOI
  10.1016/j.artint.2012.06.001) — **leída en diagonal**.
- **L5** = YAGO3 (Mahdisoltani, Biega, Suchanek; CIDR 2015) — **identificada,
  leída en diagonal**.
- **L6** = reporte técnico MPI-I-2007-5-003 (dic. 2007, versión extendida de
  YAGO) — **identificado**.
- **L7** = PrimeKG (Chandak, Huang, Zitnik; *Scientific Data* 10:67, 2023,
  DOI 10.1038/s41597-023-01960-3) — **leída en diagonal**; género Data
  Descriptor con Technical Validation.
- **L8** = review de KGs en salud (PMC12995551) — **INACCESIBLE** (reCAPTCHA)
  y es review, no release: baja prioridad, **descartada de lectura seria**.
- **L9** = survey de construcción de KG con LLMs (arXiv:2510.20345, oct.
  2025) — **leída en diagonal**.
- **L10** = DBpedia — página de proyecto, no paper: **usada solo como
  puerta**.

## §4. Descubrimiento (U-RW): tabla de candidatos R1–R15

| # | Título | Autoría | Venue | Año | ID estable | Fr. | TRIAGE 1 — qué recurso y sobre qué corpus | TRIAGE 2 — cómo declara haber evaluado |
|---|---|---|---|---|---|---|---|---|
| R1 | Automated Creation of the Legal Knowledge Graph Addressing Legislation on Violence Against Women: Resource, Methodology and Lessons Learned | Claudia dAmato [apóstrofo probablemente perdido en la conversión], Giuseppe Rubini, Francesco Didio, Donato Francioso, Fatima Zahra Amara, Nicola Fanizzi | preprint arXiv, sin Comments (cs.AI) | 2025 (v1 08/08) | arXiv:2508.06368 · DOI 10.48550/arXiv.2508.06368 | A | KG legal sobre violencia contra la mujer desde sentencias públicas del Tribunal de Justicia de la UE. El título se declara "Resource, Methodology and Lessons Learned". | "Validation via suitable competency questions"; sin métricas ni protocolo en el abstract. No verificado más allá del abstract. |
| R2 | LLM-Assisted Ontology Engineering and Construction of a French Legal Knowledge Graph | Génesis Montenegro, Mokhtar Boumedyen Billami, Catherine Faron, Fabien Gandon, Pierre Monnin | SEMANTiCS 2026, Ghent | 2026 (v1 27/07) | arXiv:2607.24551 · DOI 10.48550/arXiv.2607.24551 | A | KG legal francés anclado en ontología sobre normativa de mantenimiento; dos etapas (ontología desde núcleo SEMLEG → extracción cerrada guiada por ella) sobre muestra estratificada. | Sí: alineamiento de clases casi completo, reducción de duplicados tras fusión, <20% de tripletas con propiedades no vistas, menor cumplimiento de signature exacta que revela dominio-rango nuevos. GPT-4.1 y mistral-large-2512. |
| R3 | LLM-assisted Construction of the United States Legislative Graph | Andrea Colombo, Francesco Cambria | VLDB 2025 Workshop: LLM+Graph | 2025 | vldb.org/2025/Workshops/VLDB-Workshops-2025/LLM+Graph/LLMGraph-2.pdf (sin DOI visible) | A | Property Graph de leyes públicas de EE.UU.: nodos acts/articles, aristas tipadas AMENDS / ABROGATES / IS_LEGAL_BASIS_OF / CITES. XML + HTML + PDF-imagen con OCR; 17.961 leyes. Llama y Mistral fine-tuneados. | Sí, y del tipo que interesa: evaluación manual de muestras de la reclasificación de aristas, con lectura del sesgo del método (conservador, deja lo dudoso en CITES); comparación de conteos contra baseline determinístico XML y contra Eyecite; validation loss ≈0,83 en el extractor de subjects. (Único TRIAGE 2 leído del cuerpo, no del abstract.) |
| R4 | NLP-AKG: Few-Shot Construction of NLP Academic Knowledge Graph Based on LLM | Jiayin Lan, Jiaqi Li, Baoxin Wang, Ming Liu, Dayong Wu, Shijin Wang, Bing Qin | preprint arXiv, sin venue | 2025 (20/02) | arXiv:2502.14192 · DOI 10.48550/arXiv.2502.14192 | A | KG académico de NLP: 620.353 entidades y 2.271.584 relaciones desde 60.826 papers de ACL Anthology. | Solo extrínseca: 3 datasets de QA sobre literatura, con sub-graph community summary. Sin métrica intrínseca de calidad del grafo en el abstract. No verificado más allá del abstract. |
| R5 | TextMineX: Data, Evaluation Framework and Ontology-guided LLM Pipeline for Humanitarian Mine Action | Chenyue Zhou, Gürkan Solmaz, Flavio Cirillo, Kiril Gashteovski, Jonathan Fürst | preprint arXiv, sin venue | v1 18/09/2025, v4 27/01/2026 | arXiv:2509.15098 · DOI 10.48550/arXiv.2509.15098 | A+B | Dataset + framework de evaluación + pipeline guiado por ontología, sobre reportes operativos del Cambodian Mine Action Centre en tripletas sujeto-relación-objeto. | Sí, el diseño más cercano al de esta tesis: tripletas anotadas por humanos más protocolo LLM-as-Judge con mitigación explícita de sesgo de posición en scoring sin referencia. +44,2% accuracy, −22,5% alucinación, +20,9% adherencia de formato con prompts alineados a ontología. |
| R6 | MedKGent: A Large Language Model Agent Framework for Constructing Temporally Evolving Medical Knowledge Graph | Duzhen Zhang, Zixiao Wang, Zhong-Zhi Li, Yahan Yu, Shuncheng Jia, Jiahua Dong, Haotian Xu, Xing Wu, Yingying Zhang, Tielin Zhang, Jie Yang, Xiuying Chen, Le Song | npj Digital Medicine (aceptado, según Comments de arXiv) | v1 17/08/2025, v3 24/07/2026 | arXiv:2508.12393 · DOI 10.48550/arXiv.2508.12393 | A+B | KG médico de 156.275 entidades y 2.971.384 tripletas sobre >10M de abstracts de PubMed (1975–2023). Se autodeclara el mayor KG médico derivado de LLM. | Doble: intrínseca ("automated and expert assessments", validez de tripletas ≈90%) y extrínseca (mejora de RAG en 5 LLMs sobre 7 benchmarks de QA médico). |
| R7 | ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs | Samira Khorshidi, Azadeh Nikfarjam, Suprita Shankar, Yisi Sang, Yash Govind, Hyun Jang, Ali Kasgari, Alexis McClimans, Mohamed Soliman, Vishnu Konda, Ahmed Fakhry, Xiaoguang Qi | preprint arXiv, sin venue | 2025 (04/09) | arXiv:2509.04696 · DOI 10.48550/arXiv.2509.04696 | A+B | Sistema de producción: >9M de páginas de Wikipedia, 19M de hechos ingestados sobre 195 predicados, con snippets de ontología por tipo de entidad. | Precisión 98,8%; cobertura como solapamiento de hasta 48% con KGs de terceros; lag de actualización −50 días. Validación por un segundo LLM ("Grounder") más corroboración. Tamaño y protocolo de auditoría humana no verificados. |
| R8 | A multi-view validation framework for LLM-generated knowledge graphs of chronic kidney disease | Aditya Kumar, Dilpreet Singh, Mario Cypko, Oliver Amft | Int. J. Computer Assisted Radiology and Surgery, 20(12):2523–2528 | 2025 | DOI 10.1007/s11548-025-03495-x · PMCID PMC12689688 | B | KGs por concepto para enfermedad renal crónica con GPT-4; conceptos extraídos de la cohorte CKD de MIMIC-IV v2.2 y convertidos en tripletas dirigidas. | Tres vistas con métrica: plausibilidad semántica (PubMedBERT, 0,79), compatibilidad de tipos contra ontología CKD (Jaccard + fallback, 0,84), importancia estructural (ResourceRank, 0,94). Declara como limitación la ausencia de validación formal por experto humano. |
| R9 | Can LLMs be Knowledge Graph Curators for Validating Triple Insertions? | André Gomes Regino, Julio Cesar dos Reis | Workshop on Generative AI and Knowledge Graphs (GenAIK) | 2025 | ACL Anthology 2025.genaik-1.10, pp. 87–99 (sin DOI en metadatos) | B+C | No publica KG: el LLM como curador que valida inserciones de tripletas RDF en cuatro tareas (alineamiento clase/propiedad, estandarización de URIs, consistencia semántica, corrección sintáctica). | Compara 4 modelos con prompting sistemático por etapa; ventaja de Llama-3-70B-Instruct. El KG/corpus de los experimentos no está identificado en el abstract — no verificado. |
| R10 | Generating Domain-Specific Knowledge Graphs from Large Language Models | Marinela Parović, Ze Li, Jinhua Du | Findings of the ACL 2025, Viena | 2025 | ACL Anthology 2025.findings-acl.602 · DOI 10.18653/v1/2025.findings-acl.602, pp. 11558–11574 | B+C | KGs de dos dominios (libros, landmarks), decenas de miles de entidades/relaciones, extraídos de los parámetros del LLM, no de un corpus documental. Contraste con lo que esta tesis hace. | Contra Wikidata como referencia humana. Hallazgo: la tasa de alucinación crece a medida que el procedimiento avanza, limitando la utilidad práctica a escala. Métricas no verificadas más allá del abstract. |
| R11 | GraphMERT: Efficient and Scalable Distillation of Reliable Knowledge Graphs from Unstructured Data | Margarita Belova, Jiaxin Xiao, Shikhar Tuli, Niraj K. Jha | TMLR 2026 (según Comments de arXiv) | v1 10/10/2025, v2 04/03/2026 | arXiv:2510.09580 · DOI 10.48550/arXiv.2510.09580 | B+C | Encoder de 80M de parámetros que destila KGs desde texto no estructurado; corpus de prueba: papers de PubMed sobre diabetes. | Dos métricas separadas: FActScore (factualidad con procedencia) 69,8% vs 40,2% de un LLM de 32B; ValidityScore (consistencia ontológica) 68,8% vs 43,0%. |
| R12 | Measuring the sensitivity of LLM-based structured extraction to prompt, model, and schema choices in clinical discharge summaries | Martin Murin | preprint arXiv (69 pp., material suplementario) | 2026 (04/06) | arXiv:2606.05970 · DOI 10.48550/arXiv.2606.05970 | C | No publica KG: mide cuánto se mueve la extracción estructurada al variar prompt, modelo y esquema. MIMIC-IV v3.1: 17 flags sí/no/no_documentado y vocabulario de 47 etiquetas. | Reproducibilidad sin ground truth humano, variando una elección por vez: kappa de Cohen entre prompts sobre subconjuntos estratificados por ICD, comparaciones pareadas sobre la misma nota para aislar el modelo, colapso 3→2 valores para aislar el esquema. El desacuerdo se concentra en el eje ausencia-vs-silencio; el modelo pesa más que la redacción del prompt. |
| R13 | Can LLMs be Good Graph Judge for Knowledge Graph Construction? | Haoyu Huang, Chong Chen, Zeang Sheng, Yang Li, Wentao Zhang | EMNLP 2025 Main (según Comments de arXiv) | v1 26/11/2024, v4 26/09/2025 | arXiv:2411.17388 · DOI 10.48550/arXiv.2411.17388 | C | No publica KG: GraphJudge, estrategia centrada en entidades para quitar ruido + LLM fine-tuneado como juez de grafo. Dos pares texto-grafo generales y uno de dominio. | Estado del arte contra baselines. Lo que importa es la premisa declarada: la alucinación no puede pasarse por alto al usar LLMs directamente para construir KGs. Métricas no verificadas. |
| R14 | Improving Automatic Evaluation of LLMs in Biomedical Relation Extraction via LLMs-as-the-Judge | Md Tahmid Rahman Laskar, Israt Jahan, Elham Dolatabadi, Chun Peng, Enamul Hoque, Jimmy Huang | ACL 2025 Main (según Comments de arXiv) | 2025 (01/06) | arXiv:2506.00777 · DOI 10.48550/arXiv.2506.00777 | C | No publica KG: 8 LLMs como jueces evaluando respuestas de 5 LLMs sobre 3 datasets de extracción de relaciones biomédicas. Libera 36.000 muestras anotadas. | Advertencia directa sobre el juez de esta tesis: los jueces LLM arrancan por debajo del 50% de accuracy; el formato de salida estructurado da ~15% de mejora promedio y la adaptación de dominio suma más. Señala que las relaciones extraídas no siguen formato estándar. |
| R15 | Are LLMs Good Annotators for Discourse-level Event Relation Extraction? | Kangda Wei, Aayush Gautam, Ruihong Huang | preprint arXiv, sin venue | v1 28/07/2024, v3 22/02/2025 | arXiv:2407.19568 · DOI 10.48550/arXiv.2407.19568 | C | No publica KG: GPT-3.5 y LLaMA-2 como anotadores de relaciones entre eventos a nivel discurso (correferencia, temporal, causal, subevento) en documentos largos. Datasets no nombrados en el abstract — no verificado. | Contra baselines supervisados y SFT. Catálogo explícito de modos de falla, todos aplicables a texto normativo largo: fabricación de menciones, falla en transitividad entre relaciones, falla en relaciones a larga distancia, degradación con menciones densas; las mejoras por SFT "no escalan bien". |

Nota que acompaña a la tabla (parte del mandato): R1 es duplicado del paper
04 ya presente en la bibliografía del proyecto (la lista de exclusión del
mandato original de U-RW no incluía los papers 00–06), y la franja de otras
disciplinas (alimentos/agricultura/materiales) no rindió — declarado y
aceptado por la mesa.

Resumen de consultas de búsqueda: motor: WebSearch de la sesión original de
U-RW (10 strings), más 17 accesos de verificación por WebFetch / lectura de
PDF. Los strings exactos y el mapeo consulta → candidato están en el paquete
de revisión de esa unidad (`docs/consultas_busqueda_U-RW.md`). Franjas: A rindió
7 candidatos, concentrados en legal y biomédico (la consulta hacia
alimentos/agricultura/materiales no rindió ningún release que sobreviviera
al triage); B rindió 4, varios compartidos con A; C rindió 5, con la
salvedad de que R12/R14/R15 son sobre extracción estructurada y anotación en
general, a leer con esa traducción.

## §5. Selección para lectura en serio

Decidida por la mesa de revisión, **a confirmar por la autora en la unidad
siguiente**:

- **R12** (arXiv:2606.05970) — sensibilidad de la extracción a
  prompt/modelo/esquema: es la pregunta de ESQ con método.
- **R3** (grafo legislativo de EE.UU., VLDB-W 2025) — el más cercano: aristas
  tipadas sobre corpus legal con evaluación manual de muestra y sesgo
  declarado.
- **R5** (TextMineX, arXiv:2509.15098) — juez LLM con mitigación de sesgo de
  posición.
- **R14** (arXiv:2506.00777) — jueces LLM bajo 50% en extracción biomédica:
  la advertencia sobre jueces sin calibrar.

Método declarado para la lectura en serio: **doble pasada independiente**
(mesa e instancia, sin compartir contexto), divergencias como señal.
