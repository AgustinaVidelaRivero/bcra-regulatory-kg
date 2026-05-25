# Memoria del proyecto — bcra-regulatory-kg

Tesis de grado de Ingeniería en IA (UdeSA, Agustina Videla Rivero) sobre un Knowledge Graph regulatorio del BCRA. La FASE 2.2 del proyecto lanza 5 instancias paralelas de Claude Code, cada una con una estrategia distinta de diseño de schema, sobre el subset compartido en `data/experiment/subset/`. Cada instancia trabaja aislada dentro de `data/experiment/run_X_*/` y NO lee las carpetas de los otros runs.

Documentos fuente de verdad (leer antes de empezar cualquier instancia):
- `docs/schema/experiment_protocol.md` — protocolo común (subset, formato JSON, reglas de modelado, métricas).
- `docs/schema/experiment_instance_template.md` — pasos operativos por instancia.

---

## Lecciones del Run 1 (para futuras instancias paralelas)

### 1. El presupuesto real es ~USD 11 por instancia, no USD 5

El protocolo original fijaba un límite de USD 5 de inferencia por instancia. Los datos reales del Run 1 sobre los 5 TOs (543 chunks, ~338 K tokens de contenido) muestran que el corpus regulatorio del BCRA exige un presupuesto sustancialmente mayor:

- **Extracción Haiku** (527 chunks productivos): **USD 5.59**
- **Resolución Sonnet** (~5 K entidades únicas en 57 batches): **USD 4.40**
- **Hub summarization** (top 15 hubs con Sonnet): **USD 0.55**
- **Total Run 1: USD 10.54**

La estimación inicial de USD 2.65 fue ~3 × optimista. Causas:

- Los chunks reales tienen ~3.000 tokens de input y ~1.500 de output (no ~1.000 y ~300 como se asumió originalmente), porque el dominio regulatorio es denso en obligaciones por página y el cookbook pide `description` grounded por entidad.
- La resolución Sonnet se desvía mucho cuando los batches son grandes (100 entidades) porque el output crece con el tamaño del batch (~4 K tokens/call). Output a $15/MTok domina el costo.

**Para Runs 2-5:** asumir un presupuesto realista de **USD 11 por instancia**. La autora va a actualizar `experiment_instance_template.md` para reflejar esto. Si la estrategia evita la etapa de resolución con Sonnet (p. ej. resolución determinística por reglas o por embeddings locales), el presupuesto baja considerablemente — pero la decisión es de la estrategia, no del protocolo.

### 2. Smoke test sobre 1 TO antes del full run es buena práctica

Antes de lanzar el pipeline sobre los 5 TOs, conviene correrlo entero sobre **1 TO chico** (Protección al Usuario, 36 chunks, ~5 % del corpus) y revisar. Sirve para:

- **Ajustar concurrency** según el rate limit real del tier de API (en el caso del Run 1, había que bajar de 8 a 3 concurrent calls para evitar 429s en Haiku 4.5 con 10 K out tok/min).
- **Descubrir bugs en el pipeline** sin pagarlos sobre todo el corpus (en el Run 1 aparecieron: Pydantic strict en `relations`, tipos fuera del enum, slug collisions por mayúsculas/acentos, parsing defensivo necesario en resolución).
- **Re-proyectar costos con datos reales**, ajustando estimaciones de tokens/chunk antes de comprometer el presupuesto.

El smoke del Run 1 costó USD 0.72 y reveló los 6 problemas que de otro modo hubieran roto el full run a mitad de camino. Inversión que se paga sola.

---

## Restricciones operativas que todas las instancias respetan

- `data/experiment/subset/` es **READ-ONLY**: leer los 5 PDFs, jamás escribir ahí.
- Escribir SOLO dentro de la propia carpeta de run (`data/experiment/run_X_*/`).
- NO leer las carpetas de otros runs aunque existan.
- NO commits — los maneja la autora manualmente.
- Modelo de extracción: Claude Haiku (protocolo).
- NO evaluar el propio KG — la evaluación es comparativa y se hace en la FASE 2.3.
