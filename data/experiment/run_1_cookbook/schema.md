# Schema — Run 1: Cookbook de Anthropic

> **Run ID:** `Run 1 — Cookbook de Anthropic`
> **Carpeta:** `data/experiment/run_1_cookbook/`
> **Fecha de diseño:** 2026-05-23

---

## 1. Estrategia

Aplicar la metodología del [cookbook oficial de Anthropic sobre construcción de Knowledge Graphs con LLMs](https://platform.claude.com/cookbook/capabilities-knowledge-graph-guide) al dominio regulatorio del BCRA, manteniendo fidelidad al pipeline de 6 etapas del cookbook y adaptando *únicamente* los tipos de entidad al dominio (porque los tipos del cookbook —`PERSON`, `ORGANIZATION`, `LOCATION`, `EVENT`, `ARTIFACT`— son del dominio biográfico/histórico y no encajan en regulación financiera).

El esqueleto metodológico se preserva:

1. **Document Corpus Building** — los 5 PDFs del subset.
2. **Entity & Relation Extraction** — una llamada Haiku por chunk con `messages.parse()` y schema Pydantic `ExtractedGraph(entities=[...], relations=[...])`.
3. **Entity Resolution** — clustering por tipo con Sonnet usando descripciones para desambiguar.
4. **Graph Assembly** — NetworkX `MultiDiGraph` + serialización al formato JSON del protocolo.
5. **Hub Summarization** — perfiles enriquecidos para los nodos de mayor grado (Sonnet). *Se ejecuta en este run.*
6. **Multi-hop Querying** — **NO se ejecuta**. Es evaluación, no construcción; el protocolo lo deriva a la FASE 2.3.

---

## 2. Tipos de entidad (10)

Los tipos están enraizados en el lenguaje observado de los 5 TOs. Cada uno tiene **definición operativa** (cuándo extraerlo), **ejemplos** del corpus y **anti-ejemplos** (qué NO encaja). Los anti-ejemplos importan: filtran la tentación de modelar jerarquía documental o estructuras parásitas.

### 2.1. `REGULATED_SUBJECT`
**Definición.** Persona jurídica o categoría de sujeto a la que la norma le impone obligaciones u otorga derechos.
**Ejemplos.** "entidad financiera", "PSPCP", "proveedor no financiero de crédito", "casa de cambio", "empresa no financiera emisora de tarjeta de crédito", "sujeto obligado", "exportador", "importador", "usuario de servicios financieros", "cliente del sector privado no financiero".
**Anti-ejemplos.** El BCRA no es REGULATED_SUBJECT — es REGULATOR. Un banco específico mencionado por nombre tampoco encaja (los TOs hablan en categorías abstractas, no nombran bancos individuales).

### 2.2. `REGULATOR`
**Definición.** Órgano público u organismo con potestad regulatoria, supervisora o sancionatoria.
**Ejemplos.** "BCRA", "SEFyC" (Superintendencia de Entidades Financieras y Cambiarias), "Gerencia Principal de Exterior y Cambios", "Autoridad de Aplicación".

### 2.3. `OPERATION`
**Definición.** Una operación regulada (acción concreta y bien tipificada) que un sujeto regulado puede ejecutar y a la que la norma le aplica condiciones.
**Ejemplos.** "cobro de exportación de bienes", "pago de importación", "compra de divisas en el MULC", "otorgamiento de crédito al sector privado no financiero", "cesión de cartera con responsabilidad", "operación de titulización", "operación DvP", "suscripción primaria de títulos públicos".
**Anti-ejemplos.** No usar para procesos administrativos internos (eso es `PROCESS`).

### 2.4. `REQUIREMENT`
**Definición.** Una exigencia *cuantitativa o cualitativa* que la norma impone (umbral, ratio, plazo, obligación de hacer/no hacer, exclusión, condición de aplicación).
**Ejemplos.** "exigencia de capital mínimo por riesgo de crédito", "integración mínima", "plazo de presentación del régimen informativo", "ponderador de riesgo del 20%", "obligación de informar comisiones al BCRA", "requisito de debida diligencia", "límite del 2,5% de la RPC".

### 2.5. `CONCEPT`
**Definición.** Término técnico-jurídico definido o usado de manera estable por la norma. Sirve para construir el vocabulario semántico del KG.
**Ejemplos.** "deudor", "responsabilidad patrimonial computable (RPC)", "cartera comercial", "cartera de consumo", "contrato de adhesión", "Mercado Único y Libre de Cambios (MULC)", "factor de conversión crediticia (CCF)", "cobertura del riesgo de crédito (CRC)", "garantía preferida 'A'", "trato digno".

### 2.6. `INSTRUMENT`
**Definición.** Instrumento, activo, producto o garantía financiera referido por la norma como objeto de regulación.
**Ejemplos.** "cheque", "garantía hipotecaria", "título de deuda", "derivado de crédito", "fondo común de inversión", "tarjeta de crédito", "tarjeta de compra".

### 2.7. `CLASSIFICATION`
**Definición.** Categoría o nivel definido por la norma como esquema clasificatorio cerrado.
**Ejemplos.** "Situación 1 — En situación normal", "Situación 5 — Irrecuperable", "categorías de carteras", "Método simple", "Método integral", "código de consolidación 3".

### 2.8. `PROCESS`
**Definición.** Procedimiento administrativo interno del sujeto regulado o del regulador, distinto de una operación de mercado.
**Ejemplos.** "procedimiento de análisis de cartera", "recategorización obligatoria", "tarea de clasificación", "conciliación de estados contables trimestrales", "actuación de oficio del BCRA".

### 2.9. `SANCTION`
**Definición.** Consecuencia jurídica o económica por incumplimiento.
**Ejemplos.** "incumplimiento al capital mínimo", "sanción por la Sección 5 de Protección al Usuario", "suspensión de la observancia de regulaciones técnicas".

### 2.10. `REPORT_ITEM`
**Definición.** Item específico del Régimen Informativo: código contable, partida, planilla o modelo de información.
**Ejemplos.** "Código 22100000", "partida 60500000", "Modelo de información — Sección 4", "información sobre base consolidada mensual".
**Anti-ejemplos.** "Sección 4 del RI Contable Mensual" no es un nodo (jerarquía documental); el *modelo de información* descripto en esa sección sí lo es.

---

## 3. Predicados (relaciones)

Siguiendo el cookbook, los predicados se modelan como **verb phrases cortos en español**, sin tipado cerrado a priori. El cookbook deja predicados como `str` libre y los analiza post-hoc; mantengo esa fidelidad.

**Familia de predicados esperados** (no taxativo, son guidance para el prompt de extracción):

| Predicado | Dominio típico | Rango típico |
|---|---|---|
| `regula` | REGULATOR | REGULATED_SUBJECT / OPERATION |
| `está_sujeto_a` | REGULATED_SUBJECT | REQUIREMENT |
| `realiza` | REGULATED_SUBJECT | OPERATION |
| `aplica_a` | REQUIREMENT | OPERATION / REGULATED_SUBJECT / INSTRUMENT |
| `excluye` | REQUIREMENT | OPERATION / INSTRUMENT |
| `requiere` | REQUIREMENT / OPERATION | INSTRUMENT / CONCEPT |
| `pondera` | REQUIREMENT | INSTRUMENT |
| `pertenece_a_categoría` | REGULATED_SUBJECT / OPERATION | CLASSIFICATION |
| `se_clasifica_como` | OPERATION / CONCEPT | CLASSIFICATION |
| `define` | CONCEPT | CONCEPT |
| `informa_a` | REGULATED_SUBJECT | REGULATOR |
| `genera_obligación_de_reportar` | OPERATION | REPORT_ITEM |
| `tiene_componente` | CONCEPT | CONCEPT |
| `sanciona` | REGULATOR | SANCTION |
| `aplica_sanción_por_incumplir` | SANCTION | REQUIREMENT |

El modelo es libre de proponer otros predicados; la lista es orientativa y se analiza post-hoc en `report.md`.

---

## 4. Convenciones de IDs

- **Convención del ID del nodo.** Slug en *snake_case* del nombre canónico, prefijado por las primeras tres letras del tipo: `reg_entidad_financiera`, `con_responsabilidad_patrimonial_computable`, `ope_pago_de_importacion`, `cla_situacion_5_irrecuperable`, `rep_codigo_22100000`.
- **Unicidad.** Garantizada por construcción: el alias-to-canonical map asegura que cada surface form distinto cae sobre un único canónico → un único slug.
- **Estabilidad.** El slug se calcula deterministamente del canónico, NO depende del orden de extracción ni de la cantidad de re-runs.

---

## 5. Propiedades del nodo

| Propiedad | Tipo | Obligatoriedad | Fuente |
|---|---|---|---|
| `version` | string | obligatoria | Última Com. "A" del TO al que pertenece (ej. `"A 8418"` para Capitales Mínimos) — registrada al chunkear |
| `description` | string | obligatoria | One-sentence grounded description producida por Haiku (cookbook §2.1 "Entity description") |
| `aliases` | list[string] | obligatoria | Surface forms agrupados durante entity resolution |
| `source_to` | string | obligatoria | Nombre conceptual del TO de origen (uno de los 5) — útil para auditar cobertura |
| `mention_count` | int | informativa | Nº de chunks donde el canónico apareció |

`provenance` es **propiedad-del-elemento-del-grafo en el JSON top-level** (no anidado dentro de `properties`), como exige el protocolo §b.

---

## 6. Propiedades del edge

Edges del cookbook llevan únicamente `predicate`. Yo conservo eso y agrego `provenance` (obligatorio por protocolo).

Si una misma tripleta `(source, predicate, target)` aparece en N chunks distintos, **se conserva como UN solo edge** y se registra la primera ocurrencia en `provenance`, listando el resto en `properties.other_locations` (opcional, sólo si N > 1). Esto evita inflar artificialmente la densidad del grafo.

---

## 7. Decisiones de chunking

- **Unidad de chunk:** una **página** del PDF. Mantiene `provenance.location` numéricamente trivial ("p. 31") y respeta el flujo narrativo de los TOs (que mayormente respetan el límite de página por punto).
- **Mínimo de tokens:** si una página tiene menos de ~200 tokens (típicamente las páginas de cierre o de continuación de listado de Comunicaciones), se fusiona con la siguiente; `provenance.location` registra el rango ("pp. 200–201").
- **Páginas de índice y de listado de Comunicaciones del final.** Se procesan igual que el resto (Haiku decide qué es central), pero el prompt instruye explícitamente "no extraigas la jerarquía documental ni el listado de Comunicaciones como entidades" — esto codifica la regla del protocolo en el prompt.
- **No se chunkea por sección.** Detectar secciones requeriría parsing estructural del PDF y agregaría una variable de diseño no estándar del cookbook. Mantengo la simplicidad del cookbook ("pass entire document text to extraction prompt in one call", adaptado a chunk=página por escala).

---

## 8. Conflictos cookbook ↔ protocolo y cómo se resuelven

Las reglas no negociables del protocolo (§c) ganan ante cualquier sugerencia divergente del cookbook. Conflictos identificados:

| # | Cookbook | Protocolo | Resolución |
|---|---|---|---|
| 1 | Entity types fijos (`PERSON`/`ORG`/`LOC`/`EVENT`/`ARTIFACT`) del dominio biográfico | "el schema emerge del dominio" (§c y plantilla §1) | Reemplazo por los 10 tipos regulatorios de la §2. Conservo la metodología (Pydantic, descripciones grounded). |
| 2 | El cookbook a veces modela documentos como nodos (ej. "Apollo_11" doc) | "Los nodos NO son jerarquía documental" (§c.1) | Los TOs y secciones jamás son nodos. Van a `provenance.source_doc` y `provenance.location`. Codificado en el prompt de extracción. |
| 3 | El cookbook no modela versión | "Versión como atributo del nodo, propiedad `version`" (§c.2) | Agrego `properties.version` con la última Com. "A" del TO. Sin árboles de revisión. |
| 4 | El cookbook no modela provenance estructurada | "Provenance OBLIGATORIO en cada nodo y cada edge" (§b) | Provenance fina por chunk-página implementada en el ensamblaje. |
| 5 | ID del cookbook = nombre canónico literal | "Convención de ID libre, único" (§b) | Slug en snake_case prefijado por tipo. Decisión estilística mía. |
| 6 | El cookbook recomienda Sonnet para resolución | "Modelo de extracción: Claude Haiku" (plantilla §Restricciones) | El protocolo sólo restringe la **extracción** (etapa 2). Resolución (etapa 3) y hub summarization (etapa 5) usan Sonnet por fidelidad al cookbook. Decisión documentada en `report.md` §"Modelos por etapa". |
| 7 | Hub summarization es etapa estándar del cookbook | El protocolo no la pide ni la prohíbe | Se ejecuta. Es parte de la **construcción** del KG (enriquece nodos hub), no es evaluación. |
| 8 | Multi-hop querying es etapa estándar del cookbook | "NO evaluar tu propio KG" (plantilla §Restricciones) | **Skip.** La evaluación es comparativa y se hace en FASE 2.3. |

---

## 9. Cómo influyó la estrategia en el schema

La estrategia "fidelidad al cookbook" tiene tres efectos visibles en el diseño:

1. **Tipos de entidad relativamente *abiertos*.** El cookbook no propone una ontología cerrada del dominio jurídico-regulatorio; sólo prescribe el método. Por eso los 10 tipos son medio-granulares (ni 4 categorías como en el cookbook original, ni 30+ como en ontologías formales tipo OWL del estado del arte). El compromiso es: suficientes tipos para que la disambiguation por tipo (cookbook §3) tenga señal, pero pocos suficientes para que Haiku no se confunda en el structured output.
2. **Predicados libres en lugar de un vocabulario controlado.** El cookbook usa `predicate: str` libre y deja el análisis para post-hoc; lo replico. Esto contrasta con estrategias que importan vocabularios como [SKOS](https://www.w3.org/2004/02/skos/), [PROV-O](https://www.w3.org/TR/prov-o/) o predicados de leyes (LKIF/Akoma Ntoso).
3. **Hub summarization incluida.** El cookbook la considera parte del KG (no de su evaluación). Otras estrategias del experimento pueden saltarla; este run no.

---

## 10. Cómo se valida el output

`code/06_validate_and_report.py` chequea:

- `kg.json` parseable.
- `provenance` presente y no vacío en cada nodo y cada edge.
- IDs únicos en `nodes[].id`.
- Toda `edges[].source` y `edges[].target` referencia un `nodes[].id` existente.
- Ningún `nodes[].label` ni `properties.description` matchea regex de jerarquía documental (`r"^(Sección|Punto|Capítulo|Artículo)\s+\d"` o `r"^\s*[A-Z]\s+\d{3,5}\s*$"` para comunicaciones).
- Conteos por `type` consistentes con la sección §2 del schema (10 tipos esperados; cualquier tipo extra que Haiku haya inventado se reporta para auditoría).

---

## 11. Granularidad de las relaciones: intra-chunk por diseño

Esta es una decisión metodológica **fiel al cookbook** que merece ser explícita en la comparación con las otras estrategias del experimento.

### 11.1. Qué decide cada llamada

Cada llamada a Haiku en la etapa 2 ve un único chunk (una página, eventualmente fusionada con su vecina cuando es corta). La **regla 6 del `SYSTEM_PROMPT`** lo formaliza:

> *"Cada `source` y `target` de una relación DEBE estar entre las entidades extraídas en este mismo fragmento."*

En consecuencia, **el modelo nunca propone una relación entre dos entidades que viven en chunks distintos**. Las relaciones nacen siempre dentro de un chunk.

### 11.2. Por qué — fidelidad al cookbook

El cookbook hace exactamente lo mismo: una llamada de extracción por documento, structured output con `entities` y `relations` co-locadas, sin razonamiento cross-documento en esa etapa. La cita del cookbook §5 ("Every relation must connect two entities you extracted") es la versión textual de mi regla 6.

La razón es metodológica: una llamada por chunk con structured output **constrained** (Pydantic schema) es lo que vuelve al pipeline barato, escalable y auditable. Si pidiéramos relaciones inter-chunk, tendríamos que (a) leer múltiples chunks por llamada — costo cuadrático — o (b) hacer un segundo paso de relation-mining sobre todo el grafo — fuera del pipeline del cookbook.

### 11.3. Cómo emergen las relaciones inter-chunk

Aunque ninguna llamada individual cruza chunks, **el KG resultante sí tiene conectividad inter-chunk**, vía dos mecanismos:

1. **Unificación al canónico en la etapa 3 (Entity Resolution).** Si el chunk A extrae *"entidad financiera está_sujeto_a exigencia de capital mínimo"* y el chunk B (de otro TO) extrae *"las entidades están_sujetas_a la obligación de informar comisiones"*, después de resolver `entidad financiera` ↔ `las entidades` → canónico común `entidad financiera`, el nodo canónico hereda ambos edges. El nodo termina conectado a `req_exigencia_de_capital_minimo` (vía chunk A) y a `req_obligacion_de_informar_comisiones` (vía chunk B). El "puente" inter-chunk lo construye la resolución, no la extracción.

2. **Provenance que registra co-ocurrencia.** Cada nodo lleva `properties.mention_count` y opcionalmente `properties.other_locations`, y cada edge dedupado lleva `properties.other_locations`. Eso documenta los chunks que aportaron evidencia al mismo nodo/edge sin necesidad de que el LLM lo haga explícito.

### 11.4. Implicancia para la evaluación (FASE 2.3)

Una pregunta como *"¿qué obligaciones tiene una entidad financiera respecto del régimen informativo?"* es **multi-hop por construcción**: el nodo `rsj_entidad_financiera` se conecta vía edges nacidos en chunks distintos a múltiples `REQUIREMENT` y `REPORT_ITEM`. La conectividad existe; lo que falta es un agente que la recorra (multi-hop querying, etapa 6 del cookbook que **no** se ejecuta en este run por protocolo).

### 11.5. Comparabilidad con las otras estrategias

Las otras 4 instancias del experimento pueden tomar decisiones distintas: usar embeddings para linkar entidades cross-chunk antes de extraer, hacer dos pasadas (extracción + segundo paso explícito de relation-mining sobre el grafo agregado), forzar predicados desde un vocabulario controlado, etc. Esta sección hace **visible** que este run NO toma ninguna de esas decisiones: queda con el modelo más conservador del cookbook (intra-chunk extraction + cross-chunk unification by entity resolution).
