# Datos verificados para las slides del esquema — run_3 (ppf_core)

Fuentes: `run_3_ppf_core/schema.md` (definiciones y decisiones, citadas con línea) y
`run_3_ppf_core/kg.json` vía `loader.load_graph('run_3')` (conteos por parseo real).
Solo datos; el armado de slides es aparte.

## 5. Metadatos de contexto (primero, para dimensionar)

- **Nodos:** 4050 (raw en kg.json: 4050)
- **Aristas:** 6634 (raw: 6634)
- **Documentos fuente (TOs) con provenance en el grafo:** 5 — TO_capitales_minimos_actual.pdf, TO_clasificacion_deudores_actual.pdf, TO_exterior_cambios_actual.pdf, TO_proteccion_usuarios_servicios_financieros_actual.pdf, TO_regimen_informativo_contable_mensual_actual.pdf
- Densidad: 1.64 aristas/nodo

## 1. Los 7 tipos de entidad — definición (schema.md §2) + conteo real

| Tipo | Nodos en run_3 | Definición (verbatim) |
|---|---|---|
| **Comunicacion** | 699 | Una Comunicación A, B o C del BCRA, citada como fuente normativa dentro del Texto Ordenado. Es el acto administrativo concreto que crea o modifica una norma. |
| **TextoOrdenado** | 5 | Uno de los 5 PDFs del subset. Es el documento consolidado vigente que agrupa muchas Comunicaciones sobre una misma materia. |
| **EntidadFinanciera** | 130 | El sujeto regulado: bancos, casas de cambio, EFNB (Entidades Financieras No Bancarias), fideicomisos financieros, EPE (Empresas Proveedoras Externas), etc. Puede ser una categoría abstracta (`"bancos comerciales"`, `"entidades financieras"`) o una entidad nominada cuando el TO la cita por nombre. |
| **Operacion** | 892 | Un acto regulado por el BCRA: financiación, depósito, transferencia, compra/venta de moneda extranjera, clasificación de deudor, presentación de información, etc. |
| **Restriccion** | 818 | Una prohibición o un límite cuantitativo/cualitativo sobre una Operación o sobre el comportamiento de una EntidadFinanciera. Deontológicamente: "no se puede", "no superará", "queda prohibido". |
| **Excepcion** | 258 | Una condición que suspende o relaja una Restricción o una Obligación específica. "Salvo cuando", "excepto si", "no aplicará a". |
| **Obligacion** | 1248 | Un deber positivo: la entidad regulada DEBE hacer algo. Presentar, informar, calcular, integrar, clasificar, asignar, comunicar. |

Suma por tipo: 4050 · sin tipos fuera del schema

## 2. Las 12 relaciones — dominio→rango y semántica (schema.md §3) + conteo real

| Relación | Dominio | Rango | Aristas en run_3 | Semántica (verbatim) |
|---|---|---|---|---|
| `establecida_en` | {Restriccion, Obligacion, Excepcion, Operacion} | TextoOrdenado | 2453 | El TO es la fuente normativa explícita del nodo source. Conecta cada pieza de contenido normativo con el TO donde aparece. |
| `referencia` | TextoOrdenado | Comunicacion | 558 | El TO cita a la Comunicación como acto que creó/define alguna de sus secciones. |
| `modificada_por` | TextoOrdenado | Comunicacion | 57 | La Comunicación modifica al TO (típicamente posterior a la versión original consolidada). |
| `aplica_a` | {Restriccion, Obligacion} | EntidadFinanciera | 1464 | El sujeto regulado de la norma. "Esta restricción aplica a los bancos comerciales." |
| `regula` | {Restriccion, Obligacion} | Operacion | 716 | La operación regulada. "Esta restricción regula las financiaciones al sector público." |
| `exceptua` | Excepcion | Restriccion | 174 | La Excepción suspende/relaja la Restricción. |
| `exceptua_obligacion` | Excepcion | Obligacion | 76 | La Excepción suspende/relaja la Obligación. (Predicado separado de `exceptua` para preservar el tipo del rango en queries.) |
| `prohibe` | Restriccion | Operacion | 131 | Forma fuerte de `regula`: la restricción prohíbe completamente la operación. Subtipo de `regula` cuando `Restriccion.tipo = "prohibicion"`. |
| `limita` | Restriccion | Operacion | 570 | Forma cuantitativa de `regula`: la restricción pone un tope sin prohibir. Subtipo de `regula` cuando `Restriccion.tipo = "limite_cuantitativo" | "limite_cualitativo"`. |
| `ejecuta` | EntidadFinanciera | Operacion | 204 | La entidad realiza la operación. Permite consultar "¿qué operaciones hacen los bancos?". |
| `requiere` | Operacion | Obligacion | 53 | La operación requiere cumplir la obligación. "Una transferencia al exterior requiere presentar el formulario X." |
| `condiciona` | Obligacion | Operacion | 178 | La obligación habilita/condiciona la operación (dirección inversa a `requiere`, útil para queries desde la obligación). |

Suma por relación: 6634 · sin relaciones fuera del schema

## 3. Subgrafo ejemplar — candidatos (criterios: 3-5 vecinos, ≥3 relaciones distintas, tema entendible, provenances pobladas en nodo y aristas)

Candidatos que cumplen los 4 criterios en todo el grafo: 1085 (con tema 'entendible' según filtro léxico: 153). Se muestran los 3 primeros.

### Candidato 1 — `Obligacion_liquidar_en_mercado_de_cambios`

- **label:** Liquidar en mercado de cambios
- **type:** Obligacion
- **description:** Deberán ser liquidadas en el mercado de cambios como requisito para el posterior acceso a éste a los efectos de atender sus servicios de capital y/o intereses con moneda extranjera en el país
- **provenances del nodo:** [{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 2.5. Títulos de deuda u otros valores representativos de deuda denominados y pagadero"}]
- **5 vecinos, 5 relaciones distintas**

| Arista | Vecino (label) | Vecino (type) | Provenance de la arista |
|---|---|---|---|
| `—establecida_en→` | Exterior y Cambios | TextoOrdenado | [{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 2.5. Títulos de deuda u otros valores representativ |
| `—aplica_a→` | Residentes | EntidadFinanciera | [{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 2.5. Títulos de deuda u otros valores representativ |
| `—regula→` | Liquidación en mercado de cambios | Operacion | [{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 2.5. Títulos de deuda u otros valores representativ |
| `←requiere—` | Emisión de títulos de deuda | Operacion | [{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 2.5. Títulos de deuda u otros valores representativ |
| `—condiciona→` | Pagos por servicios de no residentes | Operacion | [{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 2.5. Títulos de deuda u otros valores representativ |

### Candidato 2 — `Obligacion_dicha_revision_que_podra_estar_a_cargo_de_la_auditoria_interna_de_la_entidad_deb`

- **label:** Revisar clasificaciones de clientes según umbral
- **type:** Obligacion
- **description:** Dicha revisión –que podrá estar a cargo de la auditoría interna de la entidad– deberá comprender obligatoriamente a los clientes cuyo endeudamiento total en pesos y en moneda extranjera (por las financiaciones comprendidas) supere el 1 % de la responsabilidad patrimonial computable de la entidad del mes anterior al de la clasificación o el equivalente al importe de referencia establecido en el punto 3.7., de ambos el menor, y alcanzar como mínimo el 20 % de la cartera activa total.
- **provenances del nodo:** [{"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 3.5. Responsabilidad de la tarea de clasificación."}]
- **4 vecinos, 4 relaciones distintas**

| Arista | Vecino (label) | Vecino (type) | Provenance de la arista |
|---|---|---|---|
| `—establecida_en→` | Clasificación de Deudores | TextoOrdenado | [{"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 3.5. Responsabilidad de la tarea de clasifica |
| `—aplica_a→` | Sujetos obligados | EntidadFinanciera | [{"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 3.5. Responsabilidad de la tarea de clasifica |
| `—regula→` | Revisión de clasificaciones asignadas | Operacion | [{"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 3.5. Responsabilidad de la tarea de clasifica |
| `←requiere—` | Tarea de clasificación de deudores | Operacion | [{"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 3.5. Responsabilidad de la tarea de clasifica |

### Candidato 3 — `Obligacion_se_compromete_a_liquidar_en_el_mercado_de_cambios_dentro_de_los_5_cinco_dias_hab`

- **label:** Liquidación en mercado de cambios
- **type:** Obligacion
- **description:** Se compromete a liquidar en el mercado de cambios, dentro de los 5 (cinco) días hábiles de su puesta a disposición, aquellos fondos que reciba en el exterior originados en el cobro de préstamos otorgados a terceros, el cobro de un depósito a plazo o de la venta de cualquier tipo de activo, cuando el activo hubiera sido adquirido, el depósito constituido o el préstamo otorgado con posterioridad al 28/05/20
- **provenances del nodo:** [{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 3.16. Requisitos complementarios para los egresos por el mercado de cambios. (parte 1)"}]
- **4 vecinos, 4 relaciones distintas**

| Arista | Vecino (label) | Vecino (type) | Provenance de la arista |
|---|---|---|---|
| `—establecida_en→` | Exterior y Cambios | TextoOrdenado | [{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 3.16. Requisitos complementarios para los egresos p |
| `—aplica_a→` | Sujetos obligados | EntidadFinanciera | [{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 3.16. Requisitos complementarios para los egresos p |
| `—condiciona→` | Cobro de préstamos al exterior | Operacion | [{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 3.16. Requisitos complementarios para los egresos p |
| `←exceptua_obligacion—` | Excepción operaciones específicas | Excepcion | [{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 3.16. Requisitos complementarios para los egresos p |

## 4. Decisiones de diseño documentadas (verbatim de schema.md, con ubicación)

### Schema cerrado — nada emerge del corpus

(schema.md, líneas 3–4)

> **Estrategia:** *schema-based ESTRICTO* sobre 7 entidades core declaradas en la propuesta de tesis original. El schema es cerrado: 7 tipos de entidad, 12 tipos de relación. Nada emerge del corpus, nada se infiere por el LLM fuera de esta lista. Toda tripleta cuyo predicado no esté listado o cuyo dominio/rango violen la tabla se descarta en post-proceso.

### Por qué 'Artículo' sale del schema (§1)

(schema.md, líneas 15–24)

> En los Textos Ordenados del BCRA, "Artículo X" es una **etiqueta de ubicación**, no una entidad regulatoria. Ejemplo de Capitales Mínimos:
> 
> > *"Artículo 12. — Las entidades financieras deben mantener, en todo momento, una integración de capital mínimo no inferior al 8% del total de activos ponderados por riesgo."*
> 
> Si modelo "Artículo 12" como nodo, el grafo se convierte en una taxonomía de etiquetas (`Artículo 12 --tiene_contenido--> Restricción X`). La estructura documental se mete adentro del grafo, lo cual:
> 
> 1. **Viola la regla del mentor.** Un consultor que pregunta *"¿qué operaciones de crédito están limitadas por capital mínimo?"* no quiere navegar artículos: quiere `Restriccion --limita--> Operacion`.
> 2. **Es redundante.** La ubicación documental ya está garantizada por el campo `provenance.location` del protocolo (sección b), que reserva exactamente ese slot.
> 3. **Infla el grafo sin información útil.** Cada Restricción/Obligación viene "envuelta" en un Artículo que solo agrega ruido al consultar.

### La unidad regulatoria real (§1: cómo se decide el tipo de un nodo)

(schema.md, líneas 27–34)

> El contenido normativo bajo un artículo SIEMPRE es una de tres cosas:
> 
> - **Restricción** — "no se puede", "no podrá superar", "se prohíbe", "el monto no excederá".
> - **Obligación** — "deberán presentar", "informarán mensualmente", "calcularán según", "asignarán categoría".
> - **Excepción** — "salvo cuando", "excepto si", "no aplicará a", "están exceptuadas".
> 
> La etiqueta "Artículo 12" envuelve a una o varias de éstas. Modelar a éstas y dejar `"Artículo 12"` en `provenance.location` preserva 100% de la trazabilidad sin contaminar el grafo con la jerarquía documental.

### Por qué 'Obligación' entra como séptima entidad (§1)

(schema.md, líneas 37–46)

> "Artículo" se reemplaza por **Obligación**. Razones:
> 
> - Las Restricciones y Excepciones son deontológicamente negativas (prohíben o exceptúan). Pero el corpus BCRA tiene un cuerpo masivo de deber positivo: presentar regímenes informativos, calcular ratios, clasificar deudores, asignar categorías. Eso NO es una Restricción ("no podés") — es una Obligación ("tenés que").
> - Sin Obligación, el Régimen Informativo Contable Mensual (1 de los 5 TOs del subset) y gran parte de Protección al Usuario quedan sin entidad nativa que los represente, forzando a modelarlos como "Restricción de no-cumplir-X", que es semánticamente forzado.
> - La distinción Restricción/Obligación es estándar en lógica deóntica (prohibición vs. obligación) y es una distinción que un evaluador downstream usaría naturalmente al consultar.
> 
> **Compromiso:** se mantienen las 7 entidades de la propuesta original — `Artículo` se reemplaza por `Obligación`. La cardinalidad de 7 no cambia.
> 
> ---

### Notas sobre los predicados (§3): prohibe/limita/regula · requiere/condiciona · exceptua/exceptua_obligacion

(schema.md, líneas 167–170)

> - **`prohibe` vs `limita` vs `regula`.** Decidí desdoblar `regula` en dos subtipos (`prohibe`, `limita`) porque la diferencia es semánticamente crítica downstream: una consulta como "¿qué operaciones están totalmente prohibidas?" debe poder filtrar por `prohibe` sin confundirse con limitaciones cuantitativas. `regula` se mantiene como predicado paraguas para Obligaciones (que no son ni prohíbe ni limita).
> - **`requiere` vs `condiciona`.** Direcciones inversas del mismo hecho (operación↔obligación). Las dos están listadas porque pyvis no permite query bidireccional natural y modelarla en ambas direcciones simplifica las consultas downstream sin inflar el grafo (1 hecho real → 2 edges).
> - **`exceptua` y `exceptua_obligacion` separados.** Mantener tipos distintos en el rango permite filtrar por dominio en consultas tipo "todas las restricciones con al menos una excepción" sin tener que inspeccionar `properties` del target.

### Reglas de validación post-extracción (§4)

(schema.md, líneas 177–181)

> 1. **Predicado debe estar en la lista de 12.** Cualquier otro se descarta.
> 2. **Dominio y rango deben coincidir** con la tabla. Ej.: `Restriccion --exceptua--> X` es inválido (`exceptua` requiere `Excepcion` como dominio); se descarta.
> 3. **Tipo de entidad debe estar en {Comunicacion, TextoOrdenado, EntidadFinanciera, Operacion, Restriccion, Excepcion, Obligacion}.** Cualquier otro se descarta (incluye y especialmente: "Articulo", "Punto", "Seccion", "Inciso", "Capitulo" — todos jerarquía documental rechazada).
> 4. **Deduplicación por slug normalizado.** ID de cada nodo es `<tipo>_<slug>` donde slug es la propiedad clave normalizada (lowercase, sin acentos, sin espacios). Si dos extracciones producen el mismo (tipo, slug), se fusionan: properties se unifica (last-write-wins por simplicidad) y se conserva la primera provenance vista.

### Cardinalidades esperadas (§5)

(schema.md, líneas 186–193)

> - **TextoOrdenado:** exactamente 5 nodos.
> - **Comunicacion:** decenas a cientos (cada TO cita ~20-50 Comunicaciones modificatorias).
> - **EntidadFinanciera:** decenas (es una taxonomía finita: tipos de entidades reguladas + alguna nominada). Se espera dedup agresiva.
> - **Operacion:** cientos.
> - **Restriccion, Obligacion, Excepcion:** masa principal del grafo (cientos a miles cada uno).
> 
> Densidad esperada: ~2-3 edges/nodo (cada Restricción/Obligación tiene típicamente 2-4 edges: `establecida_en`, `aplica_a`, `regula`, opcionalmente `exceptua`/`exceptuada_por`).

### La tensión coherencia/expresividad e hipótesis del experimento (§6, completo)

(schema.md, líneas 198–203)

> La estrategia *schema-based ESTRICTO* maximiza **coherencia** (todo nodo tiene tipo válido, todo edge tiene predicado válido con dominio/rango correctos) y minimiza la **expresividad** (cualquier fenómeno regulatorio que no encaje en las 7 cajas se pierde o se fuerza a una caja vecina).
> 
> Hipótesis (a comprobar en FASE 2.3): este KG va a ser muy bueno para preguntas que mapeen naturalmente a las 7 entidades (ej. "¿qué operaciones están prohibidas para casas de cambio?", "¿qué obligaciones tiene un banco al financiar al sector público?", "¿qué excepciones hay a la prohibición de…?") y peor para preguntas que requieran conceptos fuera del schema (ej. "¿qué cambió entre 2023 y 2024?" no se va a poder responder bien sin nodos de versión/tiempo, que el schema no modela; "¿qué dice el TO sobre fraude bancario?" si "fraude" no es ni una Operación ni una Restricción ni Obligación en el corpus, no aparece como concepto).
> 
> El experimento es justamente medir esa tensión: ¿paga el costo de rigidez la coherencia que aporta?
