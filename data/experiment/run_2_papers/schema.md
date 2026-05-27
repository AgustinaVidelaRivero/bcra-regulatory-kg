# Schema — Run 2: Papers del estado del arte

**Run:** `Run 2 — Papers del estado del arte`
**Estrategia:** schema-aware con vocabulario controlado de predicados, validación estructural automática post-extracción y loop de reflexión (1 retry) sobre chunks con violaciones.

Este schema combina aportes de:

- **FinReflectKG** (Arun et al., *ICAIF 2025*) — loop de feedback iterativo con validación estructural automática.
- **RAGulating Compliance** — schema-light multi-agente con co-grounding de tripletas con el texto fuente.
- **LKIF Core** (Legal Knowledge Interchange Format) — ontología legal con modalidades deónticas.
- **Akoma Ntoso** — XML schema legal con cross-references explícitas y separación documento / contenido.
- **PROV-O** — modelo de provenance del W3C.

---

## 1. Filosofía de diseño

El cookbook (Run 1) deja el vocabulario de relaciones **abierto**: el LLM nombra cada predicado libremente. Eso produce alta verbosidad (sinónimos, casing distinto, plurales, acentos) y un schema implícito que solo se conoce *post-hoc*. Mi hipótesis es que un **vocabulario controlado declarado a priori**, combinado con **validación estructural automática** y un **loop de reflexión** sobre las violaciones, produce un KG más navegable, con menos ruido de predicados y con tipado más útil para queries downstream — al costo de:

- Algo de cobertura (relaciones que no caben en ningún predicado se descartan).
- Algo de costo extra por el retry de chunks con violaciones.

El schema es **schema-aware** (a diferencia del schema-light puro): tipos cerrados, predicados cerrados, dominio/rango declarados. Pero `properties` y `label` son libres (eso es lo que toma de RAGulating: no canonicalizamos el contenido natural, solo la estructura).

---

## 2. Tipos de entidad (12)

Los nodos representan **entidades regulatorias del contenido**, NO la jerarquía documental (regla 1 del protocolo: `"Punto 3.16.3.4"` no es nodo, va en `provenance.location`).

| # | Tipo | Definición operativa | Correspondencia |
|---|---|---|---|
| 1 | `SujetoRegulado` | Persona física o jurídica a la que la norma le impone deberes o le habilita facultades. P. ej.: entidades financieras, bancos comerciales, casas de cambio, usuarios de servicios financieros, fiduciarios. | LKIF: `Agent` + `Role`. Akoma Ntoso: `TLCRole`. |
| 2 | `OrganismoRegulador` | Autoridad que emite, supervisa, recibe informes o impone sanciones. P. ej.: BCRA, SEFyC, UIF, AFIP, CNV. | LKIF: `Authority` (subclase de `Agent`). |
| 3 | `Obligacion` | Deber, prohibición o facultad que la norma establece. La modalidad deóntica va en `properties.modalidad ∈ {obligacion, prohibicion, facultad}`. | LKIF: `Obligation` / `Prohibition` / `Permission` (modalidades deónticas unificadas en un solo tipo con discriminador). |
| 4 | `Operacion` | Acción/transacción regulada. P. ej.: compra de divisas, otorgamiento de préstamo, transferencia al exterior, depósito a plazo fijo. | LKIF: `Action` / `Process`. |
| 5 | `ConceptoDefinido` | Definición técnica o legal establecida por la norma. P. ej.: "deudor en situación 1", "patrimonio neto computable", "cliente financiero", "moneda extranjera". | LKIF: `LegalConcept`. |
| 6 | `Requisito` | Condición técnica/operativa que se debe cumplir para realizar una operación o satisfacer una obligación. P. ej.: "presentar declaración jurada", "contar con sistema informático apto". | (Sin correspondencia directa LKIF; análogo a `Condition` en ontologías legales aplicadas.) |
| 7 | `Umbral` | Valor numérico/cuantitativo que activa, limita o califica una obligación u operación. P. ej.: "8% de RPC", "USD 10.000 mensuales", "30% del activo". | (Modelado de primera clase para permitir reuso entre obligaciones.) |
| 8 | `Plazo` | Especificación temporal. P. ej.: "mensual", "30 días corridos", "primer día hábil del mes siguiente". | (Modelado de primera clase por mismo motivo: reuso.) |
| 9 | `Procedimiento` | Secuencia operativa estructurada que debe seguirse. P. ej.: "presentación del Régimen Informativo Contable Mensual", "procedimiento de reclamo del usuario financiero". | LKIF: `Process`. |
| 10 | `Sancion` | Consecuencia por incumplimiento. P. ej.: multa, suspensión, observación, intimación. | LKIF: `Sanction` (no estándar pero usual en aplicaciones legales). |
| 11 | `InstrumentoFinanciero` | Producto, contrato o instrumento regulado. P. ej.: préstamo hipotecario, depósito a plazo, garantía prendaria, fideicomiso financiero, tarjeta de crédito. | (Específico de dominio financiero.) |
| 12 | `NormaReferenciada` | Otra norma citada por el TO. P. ej.: Ley 21.526, Decreto 540/24, Comunicación "A" 7891, otro Texto Ordenado. | LKIF: `LegalSource`. Akoma Ntoso: cross-reference target. |

**Propiedades comunes recomendadas** (no obligatorias, libres por nodo):

- `version`: por defecto `"vigente_2026-05"` (los TOs del subset reflejan la versión vigente).
- `modalidad`: solo para `Obligacion` ∈ `{obligacion, prohibicion, facultad}`.
- `valor` y `unidad`: para `Umbral` (p. ej. `valor: "8"`, `unidad: "porcentaje_rpc"`).
- `duracion` y `unidad`: para `Plazo` (p. ej. `duracion: "30"`, `unidad: "dias_corridos"`).

---

## 3. Vocabulario controlado de predicados (22)

Cada predicado tiene **dominio** (tipo de la entidad sujeto) y **rango** (tipo de la entidad objeto) declarados. La validación estructural los chequea automáticamente.

### 3.1 Relaciones de imputación (quién está obligado a qué)

| # | Predicado | Dominio | Rango | Definición |
|---|---|---|---|---|
| 1 | `obligado_a` | `SujetoRegulado` | `Obligacion` | El sujeto regulado tiene asignada esta obligación (en cualquiera de sus modalidades). |
| 2 | `puede_realizar` | `SujetoRegulado` | `Operacion` | El sujeto está habilitado para realizar la operación. |
| 3 | `supervisado_por` | `SujetoRegulado` \| `Operacion` | `OrganismoRegulador` | El sujeto u operación está bajo supervisión del organismo. |

### 3.2 Relaciones de aplicabilidad (sobre qué aplica una norma)

| # | Predicado | Dominio | Rango | Definición |
|---|---|---|---|---|
| 4 | `aplica_a` | `Obligacion` | `SujetoRegulado` \| `Operacion` \| `InstrumentoFinanciero` | La obligación se aplica al sujeto, operación o instrumento. |
| 5 | `condicion_de_aplicabilidad` | `Requisito` | `Obligacion` \| `Operacion` | La obligación o la operación solo aplica si se cumple este requisito (precondición normativa). |
| 6 | `excepcion_a` | `Obligacion` | `Obligacion` | Esta obligación constituye una excepción a otra obligación. |

### 3.3 Relaciones de composición operativa

| # | Predicado | Dominio | Rango | Definición |
|---|---|---|---|---|
| 7 | `requiere` | `Obligacion` \| `Operacion` \| `Procedimiento` | `Requisito` | Para satisfacer la obligación / realizar la operación / ejecutar el procedimiento se necesita cumplir este requisito (precondición operativa, distinta de `condicion_de_aplicabilidad`). |
| 8 | `involucra_instrumento` | `Operacion` | `InstrumentoFinanciero` | La operación opera sobre o usa este instrumento. |
| 9 | `requiere_autorizacion_de` | `Operacion` | `OrganismoRegulador` | La operación requiere autorización previa del organismo. |
| 10 | `parte_de_procedimiento` | `Operacion` \| `Requisito` | `Procedimiento` | La operación o el requisito es parte de un procedimiento más amplio. |
| 11 | `ejecutado_por` | `Procedimiento` | `SujetoRegulado` | El procedimiento debe ejecutarlo este sujeto. |
| 12 | `dirigido_a` | `Procedimiento` | `OrganismoRegulador` | El procedimiento se presenta o se dirige a este organismo. |

### 3.4 Relaciones cuantitativas y temporales

| # | Predicado | Dominio | Rango | Definición |
|---|---|---|---|---|
| 13 | `tiene_plazo` | `Obligacion` \| `Operacion` \| `Procedimiento` | `Plazo` | La obligación, operación o procedimiento debe cumplirse en este plazo. |
| 14 | `tiene_umbral` | `Obligacion` \| `Operacion` \| `InstrumentoFinanciero` | `Umbral` | La obligación, operación o instrumento está sujeto a este umbral cuantitativo. |

### 3.5 Relaciones sancionatorias

| # | Predicado | Dominio | Rango | Definición |
|---|---|---|---|---|
| 15 | `genera_sancion` | `Obligacion` | `Sancion` | El incumplimiento de la obligación genera esta sanción. |
| 16 | `impuesta_por` | `Sancion` | `OrganismoRegulador` | La sanción es impuesta por este organismo. |
| 17 | `recae_sobre` | `Sancion` | `SujetoRegulado` | La sanción se impone a este sujeto regulado. (Agregado en revisión post-schema: cubre el caso `Sancion → SujetoRegulado` sin desbordar el dominio de `aplica_a`.) |

### 3.6 Relaciones conceptuales y referenciales

| # | Predicado | Dominio | Rango | Definición |
|---|---|---|---|---|
| 18 | `definido_por` | `ConceptoDefinido` | `NormaReferenciada` | El concepto está definido por una norma externa citada. |
| 19 | `usa_concepto` | `Obligacion` \| `Operacion` \| `Requisito` \| `Procedimiento` | `ConceptoDefinido` | La entidad invoca el concepto definido (p. ej. una obligación de clasificar deudores "usa el concepto" de "deudor en situación 1"). |
| 20 | `clasifica_a` | `Obligacion` \| `Procedimiento` | `ConceptoDefinido` | La obligación o procedimiento produce una clasificación según el concepto (p. ej. el procedimiento de evaluación clasifica al deudor). |
| 21 | `referencia` | `Obligacion` \| `Operacion` \| `ConceptoDefinido` \| `Procedimiento` \| `Requisito` | `NormaReferenciada` | La entidad referencia o se remite a una norma externa (Akoma Ntoso-style cross-reference). |
| 22 | `modifica` | `NormaReferenciada` | `NormaReferenciada` | Una norma modifica, complementa, deroga o sustituye a otra (PROV-O `wasDerivedFrom`-style). |

### 3.7 Taxonomía

| # | Predicado | Dominio | Rango | Definición |
|---|---|---|---|---|
| 23 | `es_subtipo_de` | mismo tipo | mismo tipo | Relación de subsunción taxonómica. Dominio y rango deben ser del **mismo** tipo de entidad. P. ej.: `InstrumentoFinanciero "préstamo hipotecario" es_subtipo_de InstrumentoFinanciero "préstamo"`. |

**Total: 23 predicados con dominio y rango declarados.**

---

### Notas de revisión post-schema (no bloqueantes, anotadas para el smoke)

- **Observación A — cubierta.** Agregado predicado `recae_sobre` (S17) para `Sancion → SujetoRegulado`. Evita que Haiku invente `aplica_a` con dominio incorrecto.
- **Observación B — bajo observación.** Distinguir `referencia` (cita genérica) de `definido_por` (cita que constituye la definición del concepto) puede confundir al modelo. Si en el smoke aparece confusión, se refuerza en el SYSTEM_PROMPT.
- **Observación C — anotada.** `SujetoRegulado` NO es dominio válido de `tiene_umbral`. Si el corpus tiene casos como "el sujeto debe cumplir con un umbral mínimo de patrimonio", se modela indirectamente vía la `Obligacion` que aplica al sujeto y que `tiene_umbral`. Es modelado intencional, no carencia del schema.

---

### Ajustes post-smoke (basados en evidencia empírica sobre Protección al Usuario)

El smoke test sobre el TO de Protección al Usuario (95 chunks) mostró un retry rate inicial del **69.5 %**, muy por encima del umbral de parada de 40 % definido en §6. El **85 %** de las violaciones fueron de tipo V3 (dominio inválido) o V4 (rango inválido), y los patrones más recurrentes no fueron errores aleatorios sino **usos semánticamente legítimos que el schema cortaba**. Después de revisar manualmente los patrones, se aplicaron cuatro ajustes mínimos al vocabulario controlado y dos refuerzos al pipeline:

| # | Predicado | Cambio | Justificación empírica |
|---|---|---|---|
| 1 | `aplica_a` | Rango += `Procedimiento`, `ConceptoDefinido` | El modelo correctamente extraía "obligación se aplica al procedimiento de reclamo" y "obligación se aplica al concepto de protección del usuario". |
| 2 | `requiere` | Dominio += `InstrumentoFinanciero`, `Sancion` | "El préstamo requiere garantía" y "la sanción requiere notificación previa" son lecturas correctas del corpus. |
| 3 | `involucra_instrumento` | Dominio += `Obligacion` | Muchas obligaciones se refieren a instrumentos sin pasar por una operación explícita. |
| 4 | `usa_concepto` | Dominio += `ConceptoDefinido` | Las definiciones del BCRA se apoyan frecuentemente en otros conceptos definidos (encadenamiento de definiciones). |

Y dos refuerzos sin tocar el vocabulario:

- **SYSTEM_PROMPT** ahora incluye una sección "ERRORES FRECUENTES QUE NO QUIERO VER" con 5 ejemplos canónicos negativos (basados en los patrones observados), incluida la inversión típica `Obligacion --condicion_de_aplicabilidad--> Requisito` que el modelo hacía con frecuencia (lo correcto es al revés).
- **V7 endurecida**: la regex ahora detecta jerarquía documental *embebida* en el label (`"sujeto obligado del punto 3.2.1.1"`), no solo al inicio del label.

**Decisión metodológica:** estos ajustes se documentan acá como derivados empíricamente del smoke, no como diseño previo. Es coherente con el espíritu del paper *FinReflectKG*: usar las violaciones detectadas para mejorar el schema, no solo para reextraer. El KG final (FASE 2.2 entregable) usa el schema con estos 4 ajustes ya aplicados. El total de predicados sigue siendo 23 (no se agregaron predicados nuevos, solo se expandieron dominios/rangos de 4 existentes).

---

## 4. Convención de IDs

`{tipo_snake_case}:{slug_label}` donde `slug_label` es la versión normalizada del `label` (lowercase, sin acentos, espacios → `_`, sin puntuación). Ejemplos:

- `sujeto_regulado:entidad_financiera`
- `obligacion:clasificar_deudores_mensualmente`
- `umbral:8_porciento_rpc`
- `plazo:mensual`
- `norma_referenciada:ley_21526`

La **deduplicación** se hace por `(tipo, slug)`: dos nodos con mismo tipo y slug se mergean (sus `properties` y sus `provenance` se acumulan en listas).

---

## 5. Validación estructural automática (FinReflectKG)

Después de cada llamada de extracción, el pipeline ejecuta sobre el output crudo de cada chunk los siguientes chequeos. Cada violación que matchee se cuenta en métricas y se incluye en el feedback del retry.

| Chequeo | Regla | Acción si falla |
|---|---|---|
| **V1** Tipo de entidad válido | `node.type ∈ {los 12 tipos}` | Descartar el nodo. Marcar chunk para retry. |
| **V2** Predicado válido | `edge.relation ∈ {los 22 predicados}` | Descartar el edge. Marcar chunk para retry. |
| **V3** Dominio respetado | `type(edge.source) ∈ dominio(edge.relation)` | Descartar el edge. Marcar chunk para retry. |
| **V4** Rango respetado | `type(edge.target) ∈ rango(edge.relation)` | Descartar el edge. Marcar chunk para retry. |
| **V5** Endpoints existen | Los `source` y `target` de cada edge corresponden a nodos extraídos en el mismo chunk. | Descartar el edge. Marcar chunk para retry. |
| **V6** Modalidad deóntica | Si `node.type == Obligacion` entonces `node.properties.modalidad ∈ {obligacion, prohibicion, facultad}`. | Asignar `obligacion` por defecto + warning (no es retry-triggering). |
| **V7** Nodo no es jerarquía documental | `node.label` no es de la forma `"Punto N.N.N"`, `"Sección X"`, `"Capítulo Y"`. (Heurística regex.) | Descartar el nodo. Marcar chunk para retry. |
| **V8** Provenance completa | `provenance.source_doc` y `provenance.location` no vacíos. | Rellenar con valores del chunk (no requiere retry). |

Un chunk se marca para retry **si al menos una violación V1-V5 o V7 ocurre** (las violaciones "auto-corregibles" V6 y V8 no disparan retry).

---

## 6. Loop de reflexión (FinReflectKG)

Para cada chunk marcado, **se hace UN retry** (máximo) con un prompt que incluye:

1. El texto original del chunk.
2. El output crudo de la extracción anterior.
3. La lista explícita de violaciones detectadas, con sugerencias concretas:
   - Si `V1/V2`: "Los siguientes tipos/predicados no son válidos: [...]. Usá solo: [lista cerrada del schema]."
   - Si `V3/V4`: "El predicado `X` solo admite sujeto de tipo `A|B` y objeto de tipo `C`. Reformulá o descartá la tripleta."
   - Si `V7`: "Los siguientes labels parecen referencias documentales y NO deben ser nodos: [...]. Esa información va en `provenance.location`."

Si después del retry el chunk **sigue con violaciones**, se conservan los nodos/edges que sí pasaron la validación (descartando los que fallaron) y el chunk se marca con `flag: post_retry_violations` en el reporte. No se hacen más retries (límite duro: 1, para acotar costo).

**Límite de seguridad:** si más del **40% de los chunks** del smoke test requiere retry, se reporta y se para antes del full run para discutir.

---

## 7. Tabla de aporte por paper

| Aporte concreto al schema/pipeline | FinReflectKG | RAGulating | LKIF Core | Akoma Ntoso | PROV-O |
|---|:---:|:---:|:---:|:---:|:---:|
| Vocabulario controlado de predicados (a priori) | | ✔ (filosofía schema-light + dominio cerrado) | ✔ (predicados deónticos canonizados) | | |
| Tipos de entidad con discriminador deóntico (`Obligacion.modalidad`) | | | ✔ (Obligation/Prohibition/Permission) | | |
| Distinción `SujetoRegulado` / `OrganismoRegulador` | | | ✔ (Agent / Authority) | | |
| `NormaReferenciada` como tipo de primera clase | | | ✔ (LegalSource) | ✔ (cross-reference target) | |
| Predicado `referencia` (cross-references explícitas) | | | | ✔ | |
| Predicado `modifica` entre normas (derivación) | | | | | ✔ (`wasDerivedFrom`) |
| Validación estructural automática post-extracción | ✔ | | | | |
| Loop de retry con feedback explícito al modelo | ✔ | | | | |
| Métricas de violaciones reportadas | ✔ | | | | |
| Co-grounding de tripletas con texto fuente (provenance.location obligatoria + chunk-level granularity) | | ✔ | | | ✔ |
| `properties` y `label` libres (no se canonicaliza el contenido natural) | | ✔ (schema-light en el contenido) | | | |
| Regla "jerarquía documental NO es nodo" reforzada en validación V7 | | | | ✔ (separación documento / norma) | |
| Resolución determinística por `(tipo, slug)`, sin LLM en resolución | | ✔ (multi-agente: extracción y resolución separados, pero acá resolución es regla-based para acotar costo) | | | |

---

## 8. Lo que este schema NO modela (decisiones explícitas)

- **Jerarquía documental** (Punto 3.16.3.4, Sección II, Anexo I): NO son nodos. Van en `provenance.location`. (Refuerza regla 1 del protocolo + V7.)
- **Versiones históricas separadas**: solo modelo la versión vigente. `properties.version = "vigente_2026-05"` por defecto.
- **Comunicaciones "A" del BCRA como nodos de contenido**: no aplica al subset (los TOs ya consolidan el contenido vigente). Si aparecen, se modelan como `NormaReferenciada` (referencia externa), nunca como fuente de contenido.
- **Roles funcionales finos dentro de `SujetoRegulado`** (oficial de cumplimiento, gerente financiero, etc.): se modelan como propiedades del sujeto o se ignoran si no aparecen como entidad regulada en su propio derecho.
- **Tripletas con predicado fuera del vocabulario**: se descartan en validación, no se intenta inventar nuevos predicados.

---

## 9. Cómo se evalúa en `report.md` (post-hoc)

- Conteo de nodos por tipo y edges por predicado (sección d del protocolo).
- **Métrica diferencial del Run 2:** porcentaje de chunks con violaciones (V1-V5, V7) en primera pasada; porcentaje que requirió retry; costo del retry; chunks con violaciones residuales post-retry.
- Densidad y cobertura por TO.
- Análisis post-hoc de predicados: nº de predicados realmente usados (de los 22 declarados), distribución por uso, predicados huérfanos (declarados y nunca usados).
