# literatura/ — bibliografía de la tesis

Convención: los PDFs viven en `papers/` como `NN_snake_case.pdf`; cada paper con lectura
profunda tiene su resumen homónimo en `resumenes/` (cita IEEE, TL;DR, crítica). El
análisis transversal está en `comparativa.md` (tabla de los papers 00-06) y `gaps.md`
(huecos de la literatura que la tesis ataca). Las citas BibTeX van en `bibliography.bib`.

## Índice (una línea por paper)

- **00** — *RAGulating Compliance: A Multi-Agent Knowledge Graph for Regulatory QA* (arXiv:2508.09893, 2025) — la referencia más directa: KG-RAG multi-agente sobre regulación FDA/eCFR con evaluación débil y sin baselines externos — el hueco exacto que la tesis cierra con métricas rigurosas.
- **01** — *Knowledge Graph Anchored Information Extraction for Domain-Specific Insights* (arXiv:2104.08936, 2021) — IE pre-LLM sobre regulación financiera de EE. UU.; antecedente del enfoque "task-based" (schema chico anclado a la tarea, no ontología del dominio completo).
- **02** — *Iterative Zero-Shot LLM Prompting for Knowledge Graph Construction* (arXiv:2307.01128, 2023) — construcción de KG solo con prompts zero-shot en 3 etapas; antecedente metodológico de la resolución de entidades/predicados por LLM, sin baselines.
- **03** — *Construction of Legal Knowledge Graph Based on Knowledge-Enhanced Large Language Models* (JKEM; Information 15(11):666, 2024) — prefix-tuning para NER+RC conjunto sobre esquema legal cerrado; contraejemplo útil: construye el grafo y nunca lo evalúa downstream.
- **04** — *Automated Creation of the Legal Knowledge Graph Addressing Legislation on Violence Against Women* (arXiv:2508.06368, 2025) — comparación bottom-up tradicional vs pipeline LLM sobre sentencias del TEDH; referencia metodológica para evaluación por competency questions.
- **05** — *CORE-KG: An LLM-Driven Knowledge Graph Construction Framework for Human Smuggling Networks* (arXiv:2506.21607, 2025) — GraphRAG + coreferencia por tipo + prompt anti-boilerplate sobre texto legal; útil por las técnicas de limpieza, evaluación estructural (no funcional).
- **06** — *LINK-KG: LLM-Driven Coreference-Resolved Knowledge Graphs for Human Smuggling Networks* (arXiv:2510.26486, 2025) — extensión de 05: coreferencia en 3 etapas con prompt cache para documentos largos; relevante si el corpus escala a TOs extensos.
- **07** — *Graphs Meet AI Agents: Taxonomy, Progress, and Future Opportunities* (arXiv:2506.18019v3, 2025) — survey de la taxonomía grafos×agentes; lo uso para posicionar el marco teórico de la tesis dentro de esa taxonomía y para el desafío abierto de evaluación que el survey releva.
- **08** — *Graph Engineering Systems* (playbook, literatura gris, 2025) — práctica de ingeniería de sistemas agénticos sobre grafos; insumo de diseño, NO fuente citable: en la tesis se citan las fuentes primarias que este material referencia.
