# d2 — "How to Become a Graph Architect With Zero Experience (Full Course)" (Khairallah)

**Origen:** https://x.com/eng_khairallah1/status/2083131009986396282 (artículo) + hilo https://x.com/eng_khairallah1/status/2083262928485044343 (promoción con link al PDF del playbook)
**Fecha aproximada:** 2026-07-31 (ambos posts; ~369 K y ~176 K reproducciones al 2026-08-02)
**Etiqueta:** divulgación — no citable; ideas rastreables a fuentes primarias.
**Nota de captura:** el texto no llegó pegado con el mandato; este archivo se construyó desde las URLs de origen (navegador, 2026-08-02) como **resumen estructurado fiel** — el texto verbatim completo queda para pegado directo de la autora (sección al pie).

## Resumen estructurado (20 pasos en 5 fases)

Roadmap de autoformación "de cero a graph architect", organizado como progresión loop → grafo:

- **Fase 1 — dominar el loop (1-4):** qué es un loop (acción, resultado, chequeo, condición de repetición); construir uno; **el verificador lo es todo** (un loop con verificador débil produce "basura confiada rápido"); los cuatro modos de falla del loop a escala (no ramifica, no paraleliza, no impone checkpoints entre pasos, ante falla solo reintenta).
- **Fase 2 — modelo mental del grafo (5-9):** tres primitivas (nodos, aristas, estado); **paso 6, la idea que el proyecto mapea: no todo nodo es un LLM — "un chequeo simple debe ser una función, no un modelo"**; sobreusar LLMs es la forma más común de volver un grafo lento, caro y frágil; aristas condicionales; diseño deliberado del estado compartido; elegir UN framework de orquestación (menciona LangGraph como punto de partida común).
- **Fase 3 — patrones centrales (10-14):** router, orchestrator-worker, fan-out/fan-in paralelo, evaluator-optimizer, human-in-the-loop gate para todo lo irreversible.
- **Fase 4 — confiabilidad (15-18):** gates de validación con parada dura, caminos de recuperación diseñados (fallback, escalar a humano, fallar seguro — no reintentar para siempre), checkpoints con persistencia de estado (pausar/reanudar), observabilidad (tracing con replay por corrida).
- **Fase 5 — juicio (19-20):** **cuándo NO construir un grafo** (la habilidad más senior: la mayoría de las tareas no lo necesitan; un grafo prematuro te regala un problema de sistemas distribuidos); diseñar para producción, evals y equipo (suite de evaluación tras cada cambio, documentación mantenible).

Cierra con: los cuatro atascos típicos (saltear la fase 1, coleccionar frameworks, sobre-ingeniería post-patrones, quedarse en "corre" sin llegar a "es confiable"), qué se ve la competencia en cada fase, y un FAQ (no hace falta teoría de grafos; el término puede desaparecer pero la habilidad — "diseñar sistemas confiables alrededor de modelos no confiables" — persiste bajo cualquier nombre).

## El hilo (+ contexto de procedencia del playbook)

El hilo promocional del mismo autor afirma que "dos seniors de Anthropic" produjeron el playbook y que "Karpathy se sumó a Anthropic hace cinco semanas", y enlaza como "original link" un Google Drive con el archivo `Graph-Engineering-Athropic-Karpathy-Loop.pdf` — **el mismo nombre de archivo del PDF incorporado como 08**, cuya portada declara explícitamente NO estar afiliada ni endosada por Karpathy ni Anthropic. Las afirmaciones del hilo contradicen la portada del propio documento y quedan registradas como claims virales no verificables (consistente con la crítica (b) de la ficha 08).

## Ideas que este repo mapea

- Paso 6 ("chequeo simple = función, no modelo") → ficha 08, tabla de correspondencias (containment por capa determinística).
- Verificador estricto como núcleo del loop; gates de validación; human gate → vocabulario de contraste para mecanismos ya construidos del proyecto (juez, gates, circuito revisor-ejecutor).

## Texto verbatim

No se almacena el texto completo de terceros; la fuente es la URL de origen.