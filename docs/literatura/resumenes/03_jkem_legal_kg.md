# 03 — Construction of Legal Knowledge Graph Based on Knowledge-Enhanced Large Language Models (JKEM)

## Cita (IEEE)
J. Li, L. Qian, P. Liu, and T. Liu, "Construction of Legal Knowledge Graph Based on Knowledge-Enhanced Large Language Models," *Information*, vol. 15, no. 11, p. 666, Oct. 2024, doi: 10.3390/info15110666. [Online]. Available: https://www.mdpi.com/2078-2489/15/11/666

## TL;DR
Construyen un Chinese Legal Knowledge Graph (CLKG) sobre el Código Penal chino aplicando *prefix-tuning* a ChatGLM-6B para hacer NER + RC conjunto sobre un esquema cerrado de 9 tipos de entidad y 2 tipos de relación. Reportan F1 de 90,92 % contra baselines débiles (CRF, BiLSTM, BERT, ChatGLM sin fine-tuning), una mejora relativamente modesta sobre el LLM base. El paper construye un grafo (3.480 tripletas) pero nunca lo evalúa en una tarea downstream — no hay QA, ni RAG, ni razonamiento.

## Problema que ataca
Los KGs legales tradicionales sufren error propagation cuando NER y RC se hacen como tareas independientes; los LLMs prompted directamente son inconsistentes; el fine-tuning completo de un LLM grande es caro. Quieren extraer entidades y relaciones jurídicas conjuntamente desde texto chino del Código Penal con costo computacional bajo.

## Propuesta técnica
La idea central es **prefix-tuning** [Li & Liang, 2021]: se concatena un prefijo entrenable `p = [p1, ..., pm]` (m=256, embeddings continuos) al input del LLM en cada capa de la arquitectura Transformer; solo se entrena `p`, mientras los parámetros θ del LLM permanecen congelados. El prefijo entrenable representa <0,3 % del total de parámetros. La función `y = f([p, x], θ)` mapea texto legal a tripletas de conocimiento, y se optimiza por NLL sobre datos etiquetados.

El esquema del KG es **manual y cerrado**:
- **9 entidades**: Crime, Concept, Constitutive characteristic, Judging standard, Punishment, Legal provision, Judicial interpretation, Defense, Case.
- **2 relaciones**: Entity–With (EW, "entidad asociada con") y Component–Whole (CW, parte/todo).

Anotación con esquema BMEO (Begin/Middle/End/Other a nivel carácter) usando Doccano customizado. Datos divididos 10:1:1 (train/val/test). El KG resultante se almacena en Neo4j.

Fuente del corpus: *The Criminal Law of the People's Republic of China: Annotated Code, 4th ed.* (2018), suplementado con datos de enciclopedia online.

## Dataset / Dominio
- **Idioma**: chino.
- **Dominio**: derecho penal chino.
- **Cobertura**: 460 delitos del Código Penal.
- **Total entidades**: 2.957 (Crime: 460, Concept: 435, Constitutive feature: 433, Judging standard: 394, Punishment: 412, Legal provision: 417, Judicial interpretation: 237, Defense: 169, Case: 169).
- **Total relaciones**: 3.480 (Entity-With: 435, Whole-Part: 3.045).
- **Test set**: 35 instancias por entidad típica (15 para Defense y Case), 254 Whole-Part y 35 Entity-With.

## Métricas
- Accuracy, Recall, F1 a nivel de extracción global y por categoría de entidad/relación.

## Resultados principales

**Comparación contra baselines** (Tabla 5):
| Modelo | Accuracy (%) | Recall (%) | F1 (%) |
|---|---|---|---|
| CRF | 78,65 | 75,60 | 77,09 |
| BiLSTM | 82,30 | 83,16 | 82,73 |
| BERT | 85,72 | 84,91 | 85,31 |
| ChatGLM-6B (untuned) | 86,20 | 85,92 | 86,06 |
| **JKEM (ours)** | **90,78** | **91,06** | **90,92** |

La ganancia sobre el LLM base sin fine-tunear es de **+4,86 % F1 absoluto** (relativa: +5,7 %). Por entidad/relación (Tabla 6): Crime y Defense alcanzan F1 ≥ 98 %; Case es el peor con F1 = 83,2 %; Whole-Part F1 = 98,03 %; Entity-With F1 = 92,84 %.

Hardware reportado: Intel i9-11950H, 32 GB RAM, RTX A4000 8 GB. PRE_SEQ_LEN=256, max_source_length=512, max_target_length=512. 30 epochs.

KG final: 3.480 tripletas en Neo4j.

## Limitaciones reconocidas por los autores
- Necesidad de mostrar casos de uso reales en razonamiento legal (no se hizo).
- Desafíos de despliegue: privacidad, integración con sistemas legales existentes, actualizaciones continuas.
- Aplicación a otras jurisdicciones (solo China cubierta).

## Limitaciones NO reconocidas (lectura crítica)
- **Cero evaluación down-stream**: nunca se prueba si el KG sirve para QA, reasoning, charge prediction, citation lookup ni cualquier otra tarea. Es construcción por la construcción.
- **Esquema relacional pobrísimo**: solo 2 tipos de relación (asociación genérica + parte-todo). Para derecho penal real hace falta `causa`, `excepción_de`, `modifica_a`, `aplicable_si`, `pena_máxima`, `agravante`, etc. La afirmación de que "se puede restaurar completamente el conocimiento legal" con 2 relaciones es inverosímil.
- **Mejora sobre el baseline más fuerte (ChatGLM untuned) es modesta y poco discutida**: +4,86 % F1 con un test set de ~250 ejemplos. Sin intervalos de confianza ni significancia estadística.
- **Baselines son débiles y desactualizados**: CRF, BiLSTM, BERT, ChatGLM sin tuning. No se compara contra GPT-4 zero/few-shot ni span-based RE modernos ni mT5 fine-tuned ni los métodos chinos legales mencionados en related work (Lynx, Tong, Bi, Vuong).
- **Entidades enormes**: algunas entidades (Concept, Punishment, Defense, Case) son textos completos de párrafos. NER sobre spans párrafo-largos no es estándar y dudosamente bien evaluado con BMEO.
- **Datos privados / corpus no publicado**: "Data is contained within the article" — pero solo se publican estadísticas, no el corpus anotado. **No es reproducible.**
- **Inconsistencia de números**: en el texto dicen "90,76 % accuracy, 91,05 % recall, 90,90 % F1", pero Tabla 5 reporta 90,78/91,06/90,92. Sugiere falta de proofreading.
- **Splits estratificados por tipo, no por delito**: esto puede inflar el rendimiento si el modelo memoriza patrones de un mismo crimen visto en train/val/test.
- **Sin error analysis**: ¿qué falla? ¿Por qué Case es peor? Solo se ofrece especulación ("diversidad y complejidad").
- **El framing "knowledge-enhanced" es marketing**: no inyectan conocimiento externo más allá de los datos de entrenamiento; "prior knowledge" simplemente se refiere a los ejemplos etiquetados que se usan para entrenar el prefijo. Es prefix-tuning estándar.
- **Cero análisis de costo**: ¿cuánto tarda anotar 460 delitos con BMEO? ¿Cuántos anotadores? ¿IAA? No se reporta.
- **Calidad del paper limitada**: errores gramaticales, repetición textual literal de sentencias enteras (párrafo "This is to effectively improve..." aparece dos veces), tablas con discrepancias; rasgos típicos de revisión liviana.

## Relevancia para mi tesis
**Qué tomar prestado:**
- **Schema-based con expert-defined entities**: la idea de definir el esquema del CLKG con expertos legales reusando ontologías existentes es directamente aplicable al BCRA. Mi schema-v0.1 ya va por ese camino; este paper lo justifica metodológicamente.
- **Joint NER+RC para evitar error propagation**: punto válido, especialmente relevante porque la normativa BCRA tiene relaciones implícitas entre artículos.
- **Tabla comparativa de paradigmas LLM↔KG (Tabla 1 del paper)**: la dicotomía Soft Prompts vs Pipelined Scheme vs Fine-tuning LLMs es útil de citar en mi marco teórico.
- **Doccano + secondary-development pattern**: si necesito anotar manualmente sub-corpus BCRA, es una herramienta probada.
- **Neo4j como backend**: confirma que es una opción viable también para regulación.

**Qué hueco deja para mi novedad:**
- **No evalúa downstream**: mi tesis ataca exactamente eso — KG-RAG vs vector-RAG sobre QA con métricas de fidelidad.
- **Esquema relacional pobre (2 tipos)**: yo puedo proponer un esquema rico para BCRA con relaciones específicas de regulación financiera (`requiere_capital_de`, `excepcion_para_entidades_tipo`, `comunicacion_supersede`, `aplicable_a_periodo`, etc.).
- **Idioma**: chino vs castellano. El idioma del corpus afecta la calidad de extracción del LLM, y es un factor empírico medible.
- **Reproducibilidad**: si yo publico schema, código y corpus de evaluación, ya estoy mejor que JKEM.
- **No usan retrieval/RAG**: el KG queda guardado en Neo4j sin pipeline de uso. Mi tesis cierra ese loop.
- **Comparación contra LLMs modernos**: yo puedo y debo incluir GPT-4o / Claude / Llama-3 como baselines.
