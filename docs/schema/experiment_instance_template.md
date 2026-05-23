# Instrucciones para instancia del experimento de diseño de schema

> **Plantilla.** Los placeholders `[NOMBRE_RUN]`, `[ESTRATEGIA]` y `[CARPETA_RUN]` se reemplazan al lanzar cada instancia. Ejemplos de sustitución concretos por instancia:
>
> | Placeholder | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
> |---|---|---|---|---|---|
> | `[NOMBRE_RUN]` | `Run 1 — Cookbook de Anthropic` | `Run 2 — Papers del estado del arte` | `Run 3 — 7 entidades core PPF` | `Run 4 — Schema-light puro` | `Run 5 — Híbrido core + emergente` |
> | `[CARPETA_RUN]` | `run_1_cookbook` | `run_2_papers` | `run_3_ppf_core` | `run_4_schema_light` | `run_5_hybrid` |
> | `[ESTRATEGIA]` | (descripción detallada de la estrategia, varía por instancia) | … | … | … | … |

---

## Sos parte de un experimento comparativo

Estás ejecutando **una de 5 instancias paralelas** de Claude Code. Cada instancia diseña un Knowledge Graph para el mismo corpus regulatorio del BCRA usando una **estrategia de diseño de schema distinta**. Las otras 4 instancias corren al mismo tiempo que vos, cada una con su estrategia; **no se comunican entre sí y vos no debés intentar comunicarte con ellas**. Trabajás de forma aislada.

Después de que las 5 terminen, una fase posterior (que NO hacés vos) va a evaluar los 5 KGs con preguntas complejas para medir empíricamente qué estrategia produjo el schema más útil. Para que esa comparación sea válida, **tu output tiene que cumplir exactamente el formato común** definido abajo. La estrategia es tu variable libre; el formato y las reglas de modelado NO lo son.

**Tu nombre de run asignado:** `[NOMBRE_RUN]`

Usá exactamente este nombre como identificador propio en el `report.md` (sirve para la fase de comparación posterior).

**Tu estrategia asignada:**

[ESTRATEGIA]

**Tu carpeta de trabajo asignada:** `data/experiment/[CARPETA_RUN]/`

Leé el protocolo completo del experimento antes de empezar: `docs/schema/experiment_protocol.md`. Define el subset, el formato de salida, las reglas de modelado y las métricas. Esta plantilla es el resumen operativo; el protocolo es la fuente de verdad.

---

## Pasos que ejecutás (numerados)

### Paso 1 — Diseñar el schema según tu estrategia
Diseñá el conjunto de tipos de entidad y tipos de relación del KG siguiendo tu `[ESTRATEGIA]` asignada. El schema es la variable del experimento: puede ser tan distinto del de las otras instancias como tu estrategia lo dicte. Las únicas restricciones son las reglas de modelado comunes (ver abajo).

### Paso 2 — Documentar el schema en `schema.md`
Escribí `data/experiment/[CARPETA_RUN]/schema.md` con: los tipos de entidad (con definición de cada uno), los tipos de relación (con dominio y rango), las decisiones de diseño y su justificación según la estrategia, y cómo la estrategia influyó en el resultado.

### Paso 3 — Construir el KG sobre los 5 PDFs del subset
Construí el Knowledge Graph extrayendo entidades y relaciones de los 5 PDFs en `data/experiment/subset/` usando el schema del Paso 1. Los 5 PDFs son los Textos Ordenados del subset (ver protocolo, sección a).

**Dónde vive el código:** todo el código de extracción, procesamiento y ensamblaje del JSON vive en `data/experiment/[CARPETA_RUN]/code/`. La estructura interna de `code/` es libre (un solo script, varios módulos, notebooks, lo que la estrategia requiera), siempre que **todo quede dentro de tu carpeta de run**. NO escribas código fuera de `data/experiment/[CARPETA_RUN]/`.

### Paso 4 — Serializar el KG en `kg.json`
Serializá el KG como `data/experiment/[CARPETA_RUN]/kg.json` siguiendo **exactamente** el formato JSON obligatorio (protocolo, sección b). `provenance` obligatorio en cada nodo y cada edge. El JSON debe ser válido y parseable.

### Paso 5 — Generar `report.md` con las métricas
Escribí `data/experiment/[CARPETA_RUN]/report.md` con:

- **Identificación del run.** Encabezado con tu `[NOMBRE_RUN]` exacto, para que la fase de comparación posterior pueda ubicarte.
- **Métricas del protocolo (sección d).** Tiempo de construcción, costo (tokens + USD), nodos por tipo, edges por tipo, densidad, nº de tipos de entidad, nº de tipos de relación, cobertura por TO.
- **Inventario del directorio `code/`.** Lista de cada script/notebook en tu `code/` con 1-2 líneas que describan qué hace (extractor, post-procesador, ensamblador JSON, validador, etc.). Sirve para reproducibilidad y para que la fase de evaluación entienda qué hizo cada estrategia.

---

## Reglas de modelado comunes (no negociables)

Estas valen para las 5 estrategias por igual (protocolo, sección c):

1. **Los nodos son entidades regulatorias reales** (una restricción, una operación, una entidad financiera, una obligación, un concepto). NO son la jerarquía documental. `"Punto 3.16.3.4"` NO es un nodo: va en `provenance.location`.
2. **La versión es un atributo del nodo** (`properties.version`), no una estructura aparte. No sobre-modelar el versionado. Para el experimento basta la versión vigente.
3. **El contenido del KG sale de los Textos Ordenados** del subset. NO usar Comunicaciones A como fuente de contenido.
4. **Documentá tu schema en `schema.md`.** Las entidades y relaciones varían entre estrategias; el formato JSON y estas reglas no.

---

## Restricciones operativas

- **Formato JSON obligatorio**: respetá la estructura de la sección b del protocolo. No negociable. `provenance` obligatorio en nodos y edges.
- **Modelo de extracción**: usá Claude Haiku para la extracción de tripletas. Es un experimento exploratorio, no de producción.
- **Límite de costo**: máximo USD 5 de inferencia para esta instancia. Si te acercás al límite, parreal y reportá lo que tengas.
- **Aislamiento de carpeta**: escribí SOLO dentro de `data/experiment/[CARPETA_RUN]/`. NO toques las carpetas de las otras instancias (`run_*` que no sean la tuya), ni nada fuera de `data/experiment/`.
- **`data/experiment/subset/` es READ-ONLY.** Leés los 5 PDFs desde ahí, NUNCA escribís ahí. No se modifica, no se crean archivos auxiliares en ese directorio (caches, conversiones a texto, índices, embeddings, splits por sección, etc.). Si necesitás pre-procesar los PDFs (extraer texto, chunkear, generar embeddings, hacer índice de páginas), todos esos outputs van a tu carpeta de run — típicamente bajo `data/experiment/[CARPETA_RUN]/code/cache/` o equivalente. El subset compartido se queda intacto para garantizar que las 5 instancias procesan exactamente el mismo input.
- **NO evaluar tu propio KG.** La evaluación es comparativa y la hace una fase posterior. Tu trabajo termina en el Paso 5 (report.md con métricas descriptivas, sin auto-evaluación de calidad).
- **NO hacer commits.** Los maneja la autora manualmente.
- **NO leer ni copiar** el schema o el KG de otras instancias, aunque sus carpetas existan.

---

## Entregable final

Al terminar, tu carpeta `data/experiment/[CARPETA_RUN]/` debe contener **3 archivos + 1 carpeta**:

- `schema.md` — documentación del schema diseñado.
- `kg.json` — el KG serializado en el formato obligatorio.
- `report.md` — las métricas del protocolo + identificación del run + inventario del `code/`.
- `code/` — carpeta con todos los scripts/notebooks usados para extraer, procesar y ensamblar el KG. Estructura interna libre.

Parás ahí. No evalúes, no compares, no commitees.
