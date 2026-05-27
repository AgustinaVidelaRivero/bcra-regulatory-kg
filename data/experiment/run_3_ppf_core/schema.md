# Schema — Run 3 — 7 entidades core PPF

**Estrategia:** *schema-based ESTRICTO* sobre 7 entidades core declaradas en la propuesta de tesis original. El schema es cerrado: 7 tipos de entidad, 12 tipos de relación. Nada emerge del corpus, nada se infiere por el LLM fuera de esta lista. Toda tripleta cuyo predicado no esté listado o cuyo dominio/rango violen la tabla se descarta en post-proceso.

Lo que esta estrategia testea: si fijar a priori una ontología pequeña y cerrada produce un KG más coherente y consultable que dejarla emerger, a costa de quizás perder señal regulatoria que no encaja en las 7 cajas.

---

## 1. Decisión crítica: "Artículo" sale del schema

La propuesta de tesis original lista `Artículo` como una de las 7 entidades core. Eso entra en conflicto con la regla 1 del protocolo (sección c) y con la regla del mentor: los nodos no son jerarquía documental.

### El problema con "Artículo"

En los Textos Ordenados del BCRA, "Artículo X" es una **etiqueta de ubicación**, no una entidad regulatoria. Ejemplo de Capitales Mínimos:

> *"Artículo 12. — Las entidades financieras deben mantener, en todo momento, una integración de capital mínimo no inferior al 8% del total de activos ponderados por riesgo."*

Si modelo "Artículo 12" como nodo, el grafo se convierte en una taxonomía de etiquetas (`Artículo 12 --tiene_contenido--> Restricción X`). La estructura documental se mete adentro del grafo, lo cual:

1. **Viola la regla del mentor.** Un consultor que pregunta *"¿qué operaciones de crédito están limitadas por capital mínimo?"* no quiere navegar artículos: quiere `Restriccion --limita--> Operacion`.
2. **Es redundante.** La ubicación documental ya está garantizada por el campo `provenance.location` del protocolo (sección b), que reserva exactamente ese slot.
3. **Infla el grafo sin información útil.** Cada Restricción/Obligación viene "envuelta" en un Artículo que solo agrega ruido al consultar.

### La unidad regulatoria real

El contenido normativo bajo un artículo SIEMPRE es una de tres cosas:

- **Restricción** — "no se puede", "no podrá superar", "se prohíbe", "el monto no excederá".
- **Obligación** — "deberán presentar", "informarán mensualmente", "calcularán según", "asignarán categoría".
- **Excepción** — "salvo cuando", "excepto si", "no aplicará a", "están exceptuadas".

La etiqueta "Artículo 12" envuelve a una o varias de éstas. Modelar a éstas y dejar `"Artículo 12"` en `provenance.location` preserva 100% de la trazabilidad sin contaminar el grafo con la jerarquía documental.

### Reemplazo: "Obligación" entra como séptima entidad

"Artículo" se reemplaza por **Obligación**. Razones:

- Las Restricciones y Excepciones son deontológicamente negativas (prohíben o exceptúan). Pero el corpus BCRA tiene un cuerpo masivo de deber positivo: presentar regímenes informativos, calcular ratios, clasificar deudores, asignar categorías. Eso NO es una Restricción ("no podés") — es una Obligación ("tenés que").
- Sin Obligación, el Régimen Informativo Contable Mensual (1 de los 5 TOs del subset) y gran parte de Protección al Usuario quedan sin entidad nativa que los represente, forzando a modelarlos como "Restricción de no-cumplir-X", que es semánticamente forzado.
- La distinción Restricción/Obligación es estándar en lógica deóntica (prohibición vs. obligación) y es una distinción que un evaluador downstream usaría naturalmente al consultar.

**Compromiso:** se mantienen las 7 entidades de la propuesta original — `Artículo` se reemplaza por `Obligación`. La cardinalidad de 7 no cambia.

---

## 2. Entidades del schema (7, CERRADAS)

### 2.1 Comunicacion

**Definición.** Una Comunicación A, B o C del BCRA, citada como fuente normativa dentro del Texto Ordenado. Es el acto administrativo concreto que crea o modifica una norma.

**Cómo se reconoce.** Patrones tipo `"Com. A 7825"`, `"Comunicación A 7000"`, `"Comunicado B 12345"`. El TO suele citarlas en el pie de cada sección como "modificada por Com. A NNNN".

**Propiedades obligatorias:**
- `codigo` — string normalizado, ej. `"A-7825"`.
- `tipo` — `"A"`, `"B"` o `"C"`.
- `numero` — entero.

**Propiedades opcionales:** `fecha`, `materia`.

**No es:** un Texto Ordenado (los TOs consolidan muchas Comunicaciones). No es un nodo de contenido normativo (no se modela el cuerpo de la Comunicación — el contenido ya está en el TO).

### 2.2 TextoOrdenado

**Definición.** Uno de los 5 PDFs del subset. Es el documento consolidado vigente que agrupa muchas Comunicaciones sobre una misma materia.

**Cardinalidad esperada:** exactamente 5 nodos en el KG final (uno por PDF).

**Propiedades obligatorias:**
- `materia` — ej. `"clasificacion_deudores"`, `"capitales_minimos"`, `"exterior_cambios"`, `"proteccion_usuarios"`, `"regimen_informativo"`.
- `archivo` — nombre del PDF en `subset/`.
- `version` — la versión vigente del TO (string libre, típicamente `"vigente"` o fecha).

**No es:** una Comunicación (un TO consolida múltiples Comunicaciones). No es un punto o sección (eso vive en `provenance.location`).

### 2.3 EntidadFinanciera

**Definición.** El sujeto regulado: bancos, casas de cambio, EFNB (Entidades Financieras No Bancarias), fideicomisos financieros, EPE (Empresas Proveedoras Externas), etc. Puede ser una categoría abstracta (`"bancos comerciales"`, `"entidades financieras"`) o una entidad nominada cuando el TO la cita por nombre.

**Cómo se reconoce.** Patrones: "las entidades financieras", "los bancos", "las casas de cambio", "fideicomisos financieros", "EFNB", "ALYC", "EPE", etc.

**Propiedades obligatorias:**
- `categoria` — clase abstracta normalizada (ej. `"banco"`, `"casa_de_cambio"`, `"efnb"`, `"fideicomiso_financiero"`, `"entidad_financiera_general"`).

**Propiedades opcionales:** `nombre_propio` cuando aplica (raro en TOs).

**No es:** una Operación que la entidad realiza. No es un cliente o usuario final (eso no se modela como entidad en este schema — el cliente es contexto de la Operación).

### 2.4 Operacion

**Definición.** Un acto regulado por el BCRA: financiación, depósito, transferencia, compra/venta de moneda extranjera, clasificación de deudor, presentación de información, etc.

**Cómo se reconoce.** Verbos sustantivados o sustantivos de acción: "financiaciones", "depósitos", "transferencias al exterior", "operaciones de cambio", "clasificación de deudor", "asignación a categoría", "compra de valores".

**Propiedades obligatorias:**
- `tipo` — string normalizado, ej. `"financiacion"`, `"deposito"`, `"transferencia_exterior"`, `"compra_moneda_extranjera"`, `"clasificacion_deudor"`.

**Propiedades opcionales:** `moneda`, `plazo`, `instrumento`.

**No es:** una Restricción sobre la operación (la Restricción es un nodo separado que se enlaza con `prohibe`/`limita`). No es una Obligación de informar la operación (la Obligación es nodo separado).

### 2.5 Restriccion

**Definición.** Una prohibición o un límite cuantitativo/cualitativo sobre una Operación o sobre el comportamiento de una EntidadFinanciera. Deontológicamente: "no se puede", "no superará", "queda prohibido".

**Cómo se reconoce.** Patrones: "no podrá", "no podrán", "se prohíbe", "queda prohibida", "el monto no excederá", "el límite máximo es", "no superará el X%".

**Propiedades obligatorias:**
- `descripcion` — texto corto (~1-2 oraciones) de la restricción en sí, grounded en el TO.
- `tipo` — `"prohibicion"` o `"limite_cuantitativo"` o `"limite_cualitativo"`.

**Propiedades opcionales:** `umbral` (cuando es cuantitativa, ej. `"8%"`, `"USD 100.000"`).

**No es:** la Operación restringida (esa es un nodo aparte enlazado con `prohibe` o `limita`). No es la Excepción (la Excepción es nodo aparte enlazado con `exceptua`).

### 2.6 Excepcion

**Definición.** Una condición que suspende o relaja una Restricción o una Obligación específica. "Salvo cuando", "excepto si", "no aplicará a".

**Cómo se reconoce.** Patrones: "salvo", "excepto", "no se aplicará cuando", "están exceptuadas", "no comprende a".

**Propiedades obligatorias:**
- `descripcion` — texto corto de la condición de excepción.

**Propiedades opcionales:** `tipo_condicion` (ej. `"temporal"`, `"sujeto"`, `"monto"`).

**No es:** la Restricción/Obligación que exceptúa (esa es nodo aparte, enlace `exceptua` / `exceptua_obligacion`).

### 2.7 Obligacion

**Definición.** Un deber positivo: la entidad regulada DEBE hacer algo. Presentar, informar, calcular, integrar, clasificar, asignar, comunicar.

**Cómo se reconoce.** Patrones: "deberán", "tendrán que", "presentarán", "informarán", "calcularán", "se asignará", "será obligatorio".

**Propiedades obligatorias:**
- `descripcion` — texto corto (~1-2 oraciones) de qué se debe hacer.
- `tipo` — `"presentacion_informativa"`, `"calculo"`, `"asignacion"`, `"comunicacion_a_cliente"`, `"otra"`.

**Propiedades opcionales:** `plazo`, `frecuencia` (ej. `"mensual"`, `"trimestral"`).

**No es:** la Operación que la obligación condiciona (esa es nodo aparte). No es una Restricción (las Obligaciones son deontológicamente positivas; las Restricciones, negativas).

---

## 3. Predicados del schema (12, CERRADOS)

Set cerrado de 12 predicados, con dominio y rango estrictos. Cualquier tripleta cuyo predicado no esté listado o cuyo (source, target) no respete dominio/rango se descarta en post-proceso.

| # | Predicado | Dominio | Rango | Semántica |
|---|---|---|---|---|
| 1 | `establecida_en` | {Restriccion, Obligacion, Excepcion, Operacion} | TextoOrdenado | El TO es la fuente normativa explícita del nodo source. Conecta cada pieza de contenido normativo con el TO donde aparece. |
| 2 | `referencia` | TextoOrdenado | Comunicacion | El TO cita a la Comunicación como acto que creó/define alguna de sus secciones. |
| 3 | `modificada_por` | TextoOrdenado | Comunicacion | La Comunicación modifica al TO (típicamente posterior a la versión original consolidada). |
| 4 | `aplica_a` | {Restriccion, Obligacion} | EntidadFinanciera | El sujeto regulado de la norma. "Esta restricción aplica a los bancos comerciales." |
| 5 | `regula` | {Restriccion, Obligacion} | Operacion | La operación regulada. "Esta restricción regula las financiaciones al sector público." |
| 6 | `exceptua` | Excepcion | Restriccion | La Excepción suspende/relaja la Restricción. |
| 7 | `exceptua_obligacion` | Excepcion | Obligacion | La Excepción suspende/relaja la Obligación. (Predicado separado de `exceptua` para preservar el tipo del rango en queries.) |
| 8 | `prohibe` | Restriccion | Operacion | Forma fuerte de `regula`: la restricción prohíbe completamente la operación. Subtipo de `regula` cuando `Restriccion.tipo = "prohibicion"`. |
| 9 | `limita` | Restriccion | Operacion | Forma cuantitativa de `regula`: la restricción pone un tope sin prohibir. Subtipo de `regula` cuando `Restriccion.tipo = "limite_cuantitativo" \| "limite_cualitativo"`. |
| 10 | `ejecuta` | EntidadFinanciera | Operacion | La entidad realiza la operación. Permite consultar "¿qué operaciones hacen los bancos?". |
| 11 | `requiere` | Operacion | Obligacion | La operación requiere cumplir la obligación. "Una transferencia al exterior requiere presentar el formulario X." |
| 12 | `condiciona` | Obligacion | Operacion | La obligación habilita/condiciona la operación (dirección inversa a `requiere`, útil para queries desde la obligación). |

### Notas sobre los predicados

- **`prohibe` vs `limita` vs `regula`.** Decidí desdoblar `regula` en dos subtipos (`prohibe`, `limita`) porque la diferencia es semánticamente crítica downstream: una consulta como "¿qué operaciones están totalmente prohibidas?" debe poder filtrar por `prohibe` sin confundirse con limitaciones cuantitativas. `regula` se mantiene como predicado paraguas para Obligaciones (que no son ni prohíbe ni limita).
- **`requiere` vs `condiciona`.** Direcciones inversas del mismo hecho (operación↔obligación). Las dos están listadas porque pyvis no permite query bidireccional natural y modelarla en ambas direcciones simplifica las consultas downstream sin inflar el grafo (1 hecho real → 2 edges).
- **`exceptua` y `exceptua_obligacion` separados.** Mantener tipos distintos en el rango permite filtrar por dominio en consultas tipo "todas las restricciones con al menos una excepción" sin tener que inspeccionar `properties` del target.

---

## 4. Reglas de validación (filtros post-extracción)

Todas las tripletas extraídas se filtran contra:

1. **Predicado debe estar en la lista de 12.** Cualquier otro se descarta.
2. **Dominio y rango deben coincidir** con la tabla. Ej.: `Restriccion --exceptua--> X` es inválido (`exceptua` requiere `Excepcion` como dominio); se descarta.
3. **Tipo de entidad debe estar en {Comunicacion, TextoOrdenado, EntidadFinanciera, Operacion, Restriccion, Excepcion, Obligacion}.** Cualquier otro se descarta (incluye y especialmente: "Articulo", "Punto", "Seccion", "Inciso", "Capitulo" — todos jerarquía documental rechazada).
4. **Deduplicación por slug normalizado.** ID de cada nodo es `<tipo>_<slug>` donde slug es la propiedad clave normalizada (lowercase, sin acentos, sin espacios). Si dos extracciones producen el mismo (tipo, slug), se fusionan: properties se unifica (last-write-wins por simplicidad) y se conserva la primera provenance vista.

---

## 5. Restricciones de cardinalidad esperadas

- **TextoOrdenado:** exactamente 5 nodos.
- **Comunicacion:** decenas a cientos (cada TO cita ~20-50 Comunicaciones modificatorias).
- **EntidadFinanciera:** decenas (es una taxonomía finita: tipos de entidades reguladas + alguna nominada). Se espera dedup agresiva.
- **Operacion:** cientos.
- **Restriccion, Obligacion, Excepcion:** masa principal del grafo (cientos a miles cada uno).

Densidad esperada: ~2-3 edges/nodo (cada Restricción/Obligación tiene típicamente 2-4 edges: `establecida_en`, `aplica_a`, `regula`, opcionalmente `exceptua`/`exceptuada_por`).

---

## 6. Cómo la estrategia influye en el resultado esperado

La estrategia *schema-based ESTRICTO* maximiza **coherencia** (todo nodo tiene tipo válido, todo edge tiene predicado válido con dominio/rango correctos) y minimiza la **expresividad** (cualquier fenómeno regulatorio que no encaje en las 7 cajas se pierde o se fuerza a una caja vecina).

Hipótesis (a comprobar en FASE 2.3): este KG va a ser muy bueno para preguntas que mapeen naturalmente a las 7 entidades (ej. "¿qué operaciones están prohibidas para casas de cambio?", "¿qué obligaciones tiene un banco al financiar al sector público?", "¿qué excepciones hay a la prohibición de…?") y peor para preguntas que requieran conceptos fuera del schema (ej. "¿qué cambió entre 2023 y 2024?" no se va a poder responder bien sin nodos de versión/tiempo, que el schema no modela; "¿qué dice el TO sobre fraude bancario?" si "fraude" no es ni una Operación ni una Restricción ni Obligación en el corpus, no aparece como concepto).

El experimento es justamente medir esa tensión: ¿paga el costo de rigidez la coherencia que aporta?
