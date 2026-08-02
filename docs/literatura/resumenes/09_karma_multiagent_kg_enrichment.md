# 09 — KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment (mini-ficha)

## Cita (IEEE)

Y. Lu, W. Wu, X. Zhao, R. Peng, and J. Wang, "KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment," *arXiv preprint* arXiv:2502.06472v2 [cs.CL], Jan. 2026 (v1: Feb. 2025). [Online]. Available: https://arxiv.org/abs/2502.06472

Nota: el pie de página del PDF indica "39th Conference on Neural Information Processing Systems (NeurIPS 2025)".

Archivo: `papers/09_karma_multiagent_kg_enrichment.pdf` (26 pp.: 9 de cuerpo + apéndice §8–9, descargado de arXiv el 2026-08-02, verificado: abre y corresponde al paper).

## TL;DR

Framework multi-agente para **enriquecer** (no construir desde cero) un KG existente a partir de literatura científica. Nueve agentes LLM especializados bajo un Central Controller: Ingestion, Reader (scoring de relevancia por segmento), Summarizer, Entity Extraction (NER LLM + normalización por embeddings contra el KG), Relationship Extraction (clasificador multi-label sobre pares), Schema Alignment (tipa entidades/relaciones nuevas contra el schema del KG), Conflict Resolution (debate LLM Agree/Contradict contra tripletas existentes) y Evaluator (agrega confianza/claridad/relevancia y decide integración por umbral). Proof-of-concept sobre 1.200 artículos de PubMed en tres dominios biomédicos (genómica 720, proteómica 360, metabolómica 120) con tres backbones (GLM-4 9B, GPT-4o, DeepSeek-v3): hasta 38.230 entidades nuevas, 83,1 % de correctitud LLM-verificada, 18,6 % de aristas conflictivas removidas. Ablations muestran que Summarizer, Conflict Resolution y Evaluator aportan cada uno.

## Qué agentes propone

Pipeline jerárquico de 9 roles (§3.2–3.10): IA (normalización de documentos), RA (segmentación + descarte por relevancia contra el KG), SA (condensación), EEA (NER + normalización de menciones a entidades canónicas vía distancia en espacio de embeddings, con umbral ρ para flaggear entidades nuevas), REA (distribución de probabilidad sobre K tipos de relación, multi-label por umbral θ_r), SAA (asigna tipo del schema a entidades/relaciones nuevas, o las flaggea para revisión), CRA (detección de contradicciones vía prompt de debate; descarte o cola de revisión experta según confianza), EA (score global = media de confianza+claridad+relevancia ≥ Θ para integrar). La verificación cruzada entre agentes es la innovación declarada.

## Qué evalúa

Sin gold standard (§4.3, decisión explícita de los autores): (i) **core metrics** auto-puntuadas por el propio sistema (confianza, claridad, relevancia medias); (ii) **estadísticas de grafo** (coverage gain = entidades nuevas, connectivity gain = aumento de grado); (iii) **quality indicators**: conflict ratio, correctitud juzgada por un LLM hold-out (R_LC), coherencia QA (C_QA = fracción de respuestas *plausibles* derivadas del KG para un set curado de preguntas de dominio, juzgada por LLM) y evaluación humana por dos expertos (R_HE, sin acuerdo inter-anotador reportado). Ablations por remoción de agente.

## Qué NO evalúa (crítica)

- **Sin evaluación funcional downstream real** — la misma crítica que este repo ya le hace a 03 (JKEM): C_QA es lo más cercano a una evaluación funcional, pero mide "plausibilidad" de respuestas derivadas del grafo según un juez LLM, sin ground truth por pregunta, sin set de preguntas publicado y sin métrica de correctitud de respuesta final contra referencia. No hay tarea downstream (QA con respuestas verificables, razonamiento, retrieval) con score independiente del propio stack LLM.
- **Sin baseline de recuperación**: no compara contra vector-RAG, GraphRAG ni ningún sistema externo; el único baseline es un single-agent (GLM-4) del propio setup.
- **Evaluación mayormente autorreferencial**: confianza/claridad/relevancia las produce el Evaluator del propio pipeline; la correctitud la juzga otro LLM. El componente humano (2 expertos, escala 0-1) no reporta IAA ni protocolo.
- **Reproducibilidad parcial**: el apéndice (§8.3–8.12, pp. 13–23) incluye plantillas de prompt de los 9 agentes, pero cada una está rotulada "LLM Prompt Template (Illustrative Example)" y §8.2 las describe como extensibles con few-shot/negativos — no son los prompts exactos de corrida. Los umbrales del método (δ de relevancia, ρ de entidad nueva, θ_r de relación, Θ de integración) aparecen solo simbólicamente: ningún valor numérico en cuerpo ni apéndice. Sin repositorio de código (cero menciones en las 26 pp.).
- **Sin métricas de resolución de entidades** (compression, false/missed merge): la normalización por embeddings (§3.6) no se evalúa por separado.
- Costo reportado solo como distribuciones de tokens/tiempo (Fig. 3), sin dólares ni comparación de eficiencia con un pipeline no multi-agente.

## Relevancia para este proyecto

Antecedente directo de arquitectura multi-agente por rol para construcción/enriquecimiento de KG (mapea al contraste extracción/resolución/verificación de este proyecto), con verificación cruzada y conflict resolution como agentes de primera clase. Su hueco (evaluación estructural + LLM-judge, sin downstream con referencia) es exactamente el que la evaluación extrínseca de esta tesis cubre. Candidato de diseño para la spec de la re-extracción única (ver `docs/literatura/mapa_incorporacion_graph_eng.md`).
