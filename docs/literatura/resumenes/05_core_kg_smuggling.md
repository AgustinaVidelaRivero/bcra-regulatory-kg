# 05 — CORE-KG: An LLM-Driven Knowledge Graph Construction Framework for Human Smuggling Networks

## Cita (IEEE)
D. Meher, C. Domeniconi, and G. Correa-Cabrera, "CORE-KG: An LLM-Driven Knowledge Graph Construction Framework for Human Smuggling Networks," *arXiv preprint* arXiv:2506.21607v1, Jun. 2025. [Online]. Available: https://arxiv.org/abs/2506.21607

## TL;DR
CORE-KG es un framework modular construido sobre GraphRAG (Microsoft) que extrae KGs de documentos legales sobre redes de tráfico de personas, agregando dos mejoras clave: coreference resolution secuencial por tipo de entidad (un prompt por tipo) y un prompt de extracción ingenierizado con definiciones de tipo, ordenamiento secuencial y filtrado explícito de boilerplate legal. Reportan reducciones de 33,28 % en duplicación de nodos y 38,37 % en ruido sobre 20 casos comparado contra GraphRAG vanilla con LLaMA 3.3 70B. El paper es metodológicamente útil pero su evaluación es estructural, no funcional — no mide QA ni razonamiento sobre el grafo.

## Problema que ataca
Los grafos construidos con LLMs sobre texto legal sufren tres problemas concurrentes: (i) **fragmentación por aliasing** — la misma entidad ("A.Y.", "Y.", "the defendant", "the driver") se convierte en múltiples nodos no conectados; (ii) **ruido de boilerplate legal** — terms como `Court`, `Appeal`, `Judicial Proceedings` saturan el grafo y diluyen los actores reales; (iii) **misclasificación de tipos** — `United States Magistrate Judge` etiquetado como Organization en lugar de Person, etc. Los métodos rule-based (Mazepa, Shi) no escalan; los LLM-based generan grafos sucios y duplicados.

## Propuesta técnica
**Pipeline en dos pasos:**

1. **Coreference Resolution type-aware (secuencial)**:
   - Se aplica un prompt por cada tipo de entidad (siete en total: Person, Location, Routes, Organization, Means of Transportation, Means of Communication, Smuggled Items).
   - El output del paso *i* es la entrada del paso *i+1*; las menciones se reemplazan por una forma canónica.
   - Cada prompt sigue un formato estándar: persona definition, task description, contexto down-stream, reglas type-specific, few-shot examples.
   - Justificación: si se resuelven múltiples tipos a la vez, hay "attention dilution" y "type drift" (citan Abdelnabi 2024 y Zhou 2023).

2. **Entity-Relationship Extraction + KG Construction** (sobre GraphRAG):
   - Un único prompt unified para los 7 tipos pero con instrucciones de extracción **secuencial** dentro del mismo prompt: primero todas las personas, luego ubicaciones, etc.
   - Componentes adicionales del prompt: (a) **filtering explícito** que indica al LLM remover entidades government-related antes del output, (b) **definiciones de tipo** dentro del prompt para mitigar overgeneralization bias, (c) chain-of-thought structure.
   - Solo se usa la sección "Opinion" del fallo, no el documento completo (filtrado de procedural/statutory).
   - Chunks de 300 tokens (default de GraphRAG); ensamblado en NetworkX → GraphML/Parquet.

**Stack:** LLaMA 3.3 70B servido localmente con Ollama, temperatura = 0, NVIDIA A100 80GB, GraphRAG v0.3.2, embeddings nomic-embed-text declarados pero no usados (la KGC no los necesita), Python 3.12.

## Dataset / Dominio
- **Fuente**: Nexis Uni (acceso institucional).
- **Cantidad**: 20 casos seleccionados al azar con la query `"human smuggling OR alien smuggling"`.
- **Período**: 1994–2024.
- **Tipo**: U.S. federal y state court proceedings.
- **Idioma**: inglés.
- **Sección procesada**: solo "Opinion" (~2.000 palabras por caso).
- **Anonimización**: nombres reales reemplazados por iniciales con punto ("R.").

## Métricas
- **Node Duplication Rate**: número de nodos redundantes (semánticamente equivalentes) ÷ total de nodos. Detección automática vía RapidFuzz `partial_ratio` ≥ 75 % por tipo + revisión manual por SME para falsos positivos.
- **Noise Rate**: número de nodos no informativos (boilerplate legal) ÷ total de nodos × 100. Detección manual por SME.
- **Type Assignment Reliability**: análisis cualitativo de misclassifications.
- **Absolute Drop** = baseline − CORE-KG.
- **Relative Improvement** = (baseline − CORE-KG) / baseline × 100.

## Resultados principales

| Métrica | Baseline (%) | CORE-KG (%) | Absolute Drop (%) | Relative Improvement (%) |
|---|---|---|---|---|
| Node Duplication Rate | 30,38 | 20,27 | 10,11 | **33,28** |
| Noise Rate | 27,41 | 16,89 | 10,52 | **38,37** |

- Mejoras consistentes en los 20 casos (Apéndice A).
- Caso más mejorado: Case 06 (39,76 % → 6,25 % en duplicación).
- Caso más difícil: Case 20 (45,68 % baseline vs 44,90 % CORE-KG, casi sin mejora).
- Errores reconocidos: "border" vs "United States–Mexican border" no resueltos; "United States" como país vs gobierno no desambiguado.

## Limitaciones reconocidas por los autores
- Algunos casos siguen exhibiendo alta duplicación (e.g., Case 20).
- Falta de tracking discursivo global y de role alignment para entidades geopolítica/institucionalmente ancladas.
- Solo evaluación cualitativa+estructural, no down-stream.
- Sample size de 20 casos es preliminar.

## Limitaciones NO reconocidas (lectura crítica)
- **Único baseline**: solo comparan contra GraphRAG vanilla con un mínimo ajuste. No comparan contra Carta et al. 2023 (paper 02, iterative zero-shot), ClauseIE/OpenIE, span-based RE supervisado, ni contra GraphRAG con coref pipelines independientes (e.g., neuralcoref + GraphRAG).
- **Baseline injustamente débil**: parte del 38 % de mejora en ruido viene del filtering explícito de gobierno/court — un truco trivial; un baseline equitativo debería tener el mismo filtering. Sin esa diferencia, la ganancia atribuible a coref puro queda diluida.
- **Sin medición de recall**: las métricas (duplication, noise) son tipo precision/cleanliness; no se mide cuántas entidades importantes el sistema *omite*. CORE-KG podría estar dejando afuera entidades válidas mientras "limpia" el grafo.
- **Sin ablation por componente**: bundle de cuatro mejoras (coref secuencial + extracción secuencial + filtering + type definitions) sin medir el aporte individual de cada una. Imposible decir cuál de las cuatro es load-bearing.
- **Sample tiny (20 docs)** sin tests de significancia ni intervalos de confianza, a pesar de tener case-by-case data en el apéndice.
- **Single-LLM dependency** (LLaMA 3.3 70B); resultados pueden no transferir a GPT-4o o Claude.
- **Threshold de fuzzy matching = 75 %** arbitrario; no hay análisis de sensibilidad.
- **No QA, no razonamiento, no link prediction**: el grafo es el output final; nadie lo *usa*.
- **Schema cerrado y muy específico**: 7 tipos hardcodeados para smuggling. La afirmación "broadly applicable" se mantiene por aspiración, no por evidencia.
- **Solo "Opinion" section**: pierden contexto procedural que en algunos casos contiene información clave (e.g., admisiones en preliminary statements). No se justifica la elección con datos.
- **Anonimización dificulta verificación**: imposible para un revisor reproducir las resoluciones de coref específicas con casos reales.
- **No abordan conflictos jerárquicos**: cuando una sentencia overturned o vacated otra, ¿cómo lo modelan? No hay temporal reasoning.
- **GraphRAG 0.3.2 es vieja**: versiones posteriores tienen mejor extracción y métricas; la comparación se vuelve obsoleta rápido.
- **El concepto de "noise rate" es subjetivo**: lo que es boilerplate para análisis de smuggling networks puede ser señal para otro analista (e.g., trayectoria procesal). Eso no se discute.

## Relevancia para mi tesis
**Qué tomar prestado:**
- **El patrón sequential type-aware coreference** es altamente aplicable a la normativa BCRA: una Comunicación A puede mencionar "la entidad", "el sujeto obligado", "el banco", "la institución financiera" como aliasing de un mismo `EntidadFinanciera`. Aplicar el mismo prompt-per-type ayudará.
- **Filtering explícito de boilerplate**: el corpus BCRA tiene mucho metaboilerplate ("la presente Comunicación", "El Banco Central comunica...", referencias formales). Un prompt con instrucción de descarte temprano ahorra trabajo posterior.
- **In-prompt type definitions con few-shot examples**: combate la overgeneralization bias del LLM. Para BCRA puedo definir tipos como `EntidadRegulada`, `OperaciónFinanciera`, `RequisitoPrudencial`, `FechaDeAplicación`, etc. con ejemplos few-shot.
- **Construir sobre GraphRAG**: framework probado, modular, con KGC + RAG integrados. Buen punto de partida en lugar de reinventar.
- **Métricas estructurales (duplication rate, noise rate)** son baratas de implementar y útiles como proxy de calidad del grafo, complementarias a métricas funcionales.
- **Ablation con LLaMA 3.3 70B vía Ollama**: stack open-source replicable sin costo de API, importante para tesis con presupuesto acotado.

**Qué hueco deja para mi novedad:**
- **No QA, no faithfulness**: idéntico vacío que en los demás papers. Mi tesis llena este hueco midiendo respuestas.
- **Dominio smuggling ≠ regulación financiera**: aplicar el patrón a BCRA es contribución per se, sobre todo porque el aliasing en regulación tiene reglas distintas (el "deudor en situación 2" no es lo mismo que "deudor en situación irregular" — son mismos referentes pero a través de criterios cuantitativos definidos en otra norma).
- **Idioma castellano**: la performance de coref por LLM en castellano técnico-financiero está poco evaluada; aporto evidencia.
- **Ablation completo**: yo puedo desacoplar coref vs filtering vs type definitions y reportar contribución individual.
- **Recall + precision**: yo debería medir ambos, no solo cleanliness.
- **Comparación de LLMs**: GPT-4o vs Claude vs Llama-3 sobre el mismo corpus normativo.
- **Versiones temporales de la normativa**: cuando una Com. A modifica otra, mi schema y pipeline deben razonar sobre versiones — gap explícito que CORE-KG no aborda.
