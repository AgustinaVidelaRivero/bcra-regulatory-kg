# Worksheet de adjudicación humana — fidelidad EV2 de KG-Reextraído-r1 (U-B1.8)

Adjudicación según §6 del pre-registro del método
(`docs/preregistro_evaluacion_fidelidad_ev2.md`, commit be8a84f) y el
pre-registro de la unidad (`data/experiment/ev2_r1/preregistro_ev2_r1.md`,
commit 6c5507b). Fichas en orden aleatorizado (semilla `worksheet-ev2-r1`), numeradas
1..13. Cada ficha trae: TO y ancla del gold, la pregunta, la respuesta
COMPLETA del sistema y los criterios del gold sellado con su cita textual.

## Instrucciones

1. Adjudicar contra el PDF del Texto Ordenado indicado (ancla como punto de
   partida) y contra el gold sellado
   (`data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json`),
   **criterio por criterio**.
2. Para cada criterio marcar exactamente uno: `cumplido` (la respuesta
   satisface lo que el criterio exige, conforme a la norma) o `no_cumplido`
   (no lo satisface, lo contradice, o no lo trata). No hay opción "dudoso":
   la adjudicación resuelve.
3. **No poner veredicto de pregunta a ojo.** El veredicto de la pregunta lo
   computa el mapping §2 en código a partir de las marcas por criterio
   (todos cumplidos → correcto; ninguno → incorrecto; mezcla → parcial).
4. Las marcas se vuelcan en `worksheet_adjudicacion_r1.json` (campo
   `veredicto` de cada criterio, en la ficha del mismo `id_ficha`);
   `observaciones` es libre y opcional. Este `.md` es la vista de lectura.
5. Cada ficha se adjudica por sí sola. Las fichas no indican de qué corrida
   proviene la respuesta ni qué veredicto recibió, y no debe intentarse
   inferirlo.

Marcas válidas: `cumplido` | `no_cumplido`.

---


## Ficha 1 — `ADJ1-ada33829`

**TO:** Clasificación de Deudores (`cla`) · **Ancla del gold:** cla:4.1

**Pregunta:**

¿Con qué lógica se estructuran los niveles en los que se agrupa a los clientes al clasificarlos como deudores?

**Respuesta del sistema (completa):**

> Los niveles en que se agrupan los clientes al clasificarlos como deudores se estructuran con una lógica basada en el grado de cumplimiento de las obligaciones financieras y la capacidad de pago. La estructura comprende los siguientes niveles:
> 
> 1. **Situación Normal**: El cliente debe presentar una situación financiera líquida, con bajo nivel y adecuada estructura de endeudamiento en relación con su capacidad de ganancia, y mostrar una alta capacidad de pago de las deudas (capital e intereses) en las condiciones pactadas.
> 
> 2. **Con Problemas Potencial**: Caracterizado por atrasos recurrentes respecto de condiciones contractuales.
> 
> 3. **Riesgo Medio**: Comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días.
> 
> 4. **Con Problemas**: Incluye incumplimientos de hasta 180 días respecto de condiciones contractuales.
> 
> 5. **Alto Riesgo de Insolvencia**: Situación en que el cliente demuestra improbabilidad de atender la totalidad de sus compromisos financieros.
> 
> 6. **Irrecuperable**: La categoría más severa de clasificación.
> 
> La lógica de estructuración es progresiva, basada principalmente en: (a) el grado de cumplimiento de las obligaciones contractuales, (b) la duración y recurrencia de los atrasos en días, y (c) la capacidad financiera demostrada del cliente para atender sus compromisos. Los niveles avanzan desde situaciones de normalidad hacia categorías de mayor riesgo conforme se incrementan los incumplimientos y atrasos.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que los niveles agrupan a los clientes en orden decreciente de calidad.
  - Cita textual del TO: «niveles de agrupamiento de los clientes en orden decreciente de calidad»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe indicar que el orden está en razón directa al riesgo de incobrabilidad derivado de las situaciones que presentan.
  - Cita textual del TO: «en razón directa al riesgo de incobrabilidad que se deriva de las situaciones que presentan»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 2 — `ADJ1-1d3c01e5`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:10.8

**Pregunta:**

Una deuda con el exterior por importación de bienes dejó de encuadrar como deuda comercial. ¿Cómo se cursa su cancelación por el mercado de cambios y con qué concepto se registra?

**Respuesta del sistema (completa):**

> Cuando una deuda con el exterior por importación de bienes deja de encuadrar como deuda comercial, su cancelación por el mercado de cambios se cursa conforme a las normas aplicables para la cancelación de servicios de capital de préstamos financieros. Específicamente, los pagos por deudas originadas en importaciones de bienes que no encuadren como deudas comerciales de importación se regirán por las normas que sean aplicables para la cancelación de servicios de capital de préstamos financieros. El concepto de registro es entonces 'servicios de capital de préstamos financieros' en lugar de 'deuda comercial'. El acceso al mercado de cambios para atender estos servicios de capital e intereses está condicionado al previo ingreso y liquidación en el mercado de cambios.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que además de las condiciones de acceso aplicables se cumplen las normas de cancelación de deudas financieras.
  - Cita textual del TO: «más las normas que sean aplicables a la cancelación de deudas financieras»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar que la certificación de la entidad de seguimiento deja constancia de que el pago se cursa como deuda financiera.
  - Cita textual del TO: «deberá constar que el pago debe cursarse de acuerdo con las normas aplicables a la cancelación de deudas financieras»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar el concepto del boleto de venta: pagos de principal de deudas financieras con el exterior originadas en importaciones de bienes.
  - Cita textual del TO: «P13. Pagos de principal de deudas financieras con el exterior originadas en importaciones de bienes»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 3 — `ADJ1-8b2faed3`

**TO:** Capitales Mínimos de las Entidades Financieras (`cap`) · **Ancla del gold:** cap:2.4

**Pregunta:**

¿Qué exige la normativa de capitales mínimos a las entidades del grupo 1 en materia de debida diligencia sobre sus contrapartes, y a qué exposiciones no se aplica?

**Respuesta del sistema (completa):**

> La normativa de capitales mínimos exige a las entidades del grupo 1 llevar a cabo un proceso de debida diligencia sobre sus contrapartes al momento del otorgamiento del crédito y con frecuencia mínima anual, a fin de contar con una adecuada comprensión del perfil de riesgo y las características de sus contrapartes.
> 
> No se aplica la debida diligencia a las exposiciones previstas en el punto 2.11, que incluyen: (i) exposiciones a acciones (definidas conforme al punto 2.11.3), (ii) exposiciones a deuda subordinada e instrumentos de capital que no reúnen las características para ser considerados como acciones, y (iii) demás instrumentos de capital emitidos por empresas y/o entidades financieras.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar la oportunidad y frecuencia: al otorgamiento del crédito y con frecuencia mínima anual.
  - Cita textual del TO: «al momento del otorgamiento del crédito y con frecuencia mínima anual»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe indicar el objetivo: una adecuada comprensión del perfil de riesgo y las características de las contrapartes.
  - Cita textual del TO: «puedan contar con una adecuada comprensión del perfil de riesgo y las características de sus contrapartes»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe señalar la proporcionalidad respecto de la dimensión de la entidad y la complejidad de sus operaciones.
  - Cita textual del TO: «deberá ser proporcional a la dimensión e importancia económica de las entidades financieras y a la naturaleza y complejidad de sus operaciones»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe indicar que la entidad demuestra a la SEFYC que los ponderadores asignados son adecuados a los perfiles de riesgo.
  - Cita textual del TO: «deberán demostrar a la SEFYC que los ponderadores de riesgo asignados son adecuados a los perfiles de riesgo de sus contrapartes»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe aclarar que el requerimiento no se aplica a exposiciones a gobiernos y bancos centrales.
  - Cita textual del TO: «Este requerimiento no será de aplicación para el caso de exposiciones a gobiernos y bancos centrales»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 4 — `ADJ1-567e7f99`

**TO:** Protección de los Usuarios de Servicios Financieros (`pro`) · **Ancla del gold:** pro:2.5

**Pregunta:**

Un banco quiere subir una comisión, crear otra para un producto nuevo y reducir una tercera. ¿Qué debe informar al BCRA en cada caso y en qué momento?

**Respuesta del sistema (completa):**

> Un banco debe informar al BCRA sobre cambios en comisiones de la siguiente manera:
> 
> 1. **AUMENTOS DE COMISIONES**: Deben ser **previamente informados al BCRA** (antes de implementarlos). La notificación debe realizarse por la vía consignada en la normativa.
> 
> 2. **CREACIÓN DE COMISIONES PARA NUEVOS PRODUCTOS**: Las altas de comisiones de nuevos productos y/o servicios que deseen comercializar deben ser **previamente informadas al BCRA** (antes de implementarlas). También debe utilizarse la vía consignada en la normativa.
> 
> 3. **REDUCCIONES DE COMISIONES**: Deben ser informadas al BCRA **dentro de los treinta (30) días corridos siguientes de su aplicación** (es decir, después de implementarlas).
> 
> En resumen: los aumentos y nuevas comisiones requieren aprobación previa del BCRA, mientras que las reducciones se comunican dentro de 30 días después de aplicarlas.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que las comisiones y cargos se informan mediante el régimen informativo establecido al efecto.
  - Cita textual del TO: «mediante el régimen informativo establecido»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe indicar que altas y aumentos se informan previamente al BCRA y luego se notifican a los usuarios.
  - Cita textual del TO: «deberán ser previamente informados al BCRA por la vía consignada en el párrafo precedente y luego ser notificadas a los usuarios»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que las reducciones pueden aplicarse sin demora.
  - Cita textual del TO: «Las reducciones en las comisiones y/o cargos podrán aplicarse sin demora»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe indicar el plazo de 30 días corridos para informar las reducciones aplicadas.
  - Cita textual del TO: «deberán ser informadas al BCRA dentro de los treinta (30) días corridos siguientes de su aplicación»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 5 — `ADJ1-883e85a3`

**TO:** Capitales Mínimos de las Entidades Financieras (`cap`) · **Ancla del gold:** cap:2.11

**Pregunta:**

¿Cómo deben clasificar los bancos sus exposiciones a instrumentos y con qué criterios se determina si un instrumento se trata como una acción?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA, los bancos deben clasificar sus exposiciones a instrumentos de la siguiente manera:
> 
> **Clasificación general de exposiciones a instrumentos:**
> - Las entidades financieras del Grupo 1 deben clasificar las exposiciones a: (i) acciones, (ii) demás instrumentos de capital emitidos por empresas y/o entidades financieras.
> - Las entidades financieras del Grupo 2 deben clasificar las exposiciones a: (i) deuda subordinada emitida por empresas y/o entidades financieras, y (ii) participaciones en el capital emitido por empresas y/o entidades financieras.
> 
> **Criterios para determinar si un instrumento se trata como una acción:**
> Los bancos deben tener en cuenta la realidad económica del instrumento para determinar si una exposición debe ser tratada como una acción. Específicamente, un instrumento NO debe ser clasificado como acción si:
> 
> 1. Incorpora una obligación para el emisor y el contrato establece u otorga al emisor la opción de cancelar la obligación mediante la emisión de una cantidad fija de sus acciones y/o una cantidad variable de sus acciones donde cualquier cambio del valor de la obligación es atribuible y proporcional al cambio del valor de mercado de un número fijo de acciones del emisor multiplicado por un factor predeterminado.
> 
> 2. Incorpora una obligación para el emisor y el tenedor cuenta con la opción de exigir el pago de la obligación con acciones.
> 
> 3. Incorpora una obligación para el emisor y tiene la característica de que el emisor puede diferir indefinidamente el pago de la obligación.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe mencionar que la clasificación del grupo 1 incluye la deuda subordinada emitida por empresas y/o entidades financieras.
  - Cita textual del TO: «Deuda subordinada emitida por empresas y/o entidades financieras»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe indicar que para tratar una exposición como acción se tiene en cuenta la realidad económica del instrumento.
  - Cita textual del TO: «deberán tener en cuenta la realidad económica del instrumento»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe incluir las participaciones directas e indirectas en el patrimonio y las utilidades, con o sin derecho a voto.
  - Cita textual del TO: «Participaciones directas e indirectas en el patrimonio y las utilidades de las entidades financieras y las empresas, con o sin derecho a voto»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar la condición de representar un derecho residual sobre los activos o utilidades del emisor.
  - Cita textual del TO: «Representan un derecho residual sobre los activos o las utilidades del emisor»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 6 — `ADJ1-6781d8e5`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:13.5

**Pregunta:**

Un banco emitió una carta de crédito para garantizar una importación de servicios y ahora debe afrontar el pago. ¿Qué condiciones tiene que verificar para su propio acceso al mercado de cambios?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA, las entidades que emitieron una carta de crédito para garantizar importación de servicios deben verificar condiciones específicas para acceder al mercado de cambios al momento del pago. La normativa establece que el acceso al mercado de cambios está condicionado al cumplimiento de condiciones enumeradas en el Punto 3.11.1 del Texto Ordenado de Exterior y Cambios. Para pagos de servicios, deben verificarse requisitos aplicables según los Puntos 13.2.1 o 13.2.2, incluyendo documentación que demuestre que la fecha de vencimiento de la financiación era compatible con los plazos previstos. Sin embargo, la información disponible en el grafo no permite detallar exhaustivamente todas las condiciones específicas que debe verificar el banco.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que las entidades tienen acceso para pagos propios por cartas de crédito o letras avaladas que garantizan importaciones de servicios.
  - Cita textual del TO: «Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe señalar que se verifica el cumplimiento de las condiciones aplicables según la fecha de emisión u otorgamiento.
  - Cita textual del TO: «cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que para instrumentos emitidos desde el 13/12/23 la operación garantizada debía ser un servicio prestado o devengado a partir de esa fecha.
  - Cita textual del TO: «la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar la regla de plazo: el plazo del servicio más otros 15 días corridos desde la fecha estimada de prestación o devengamiento.
  - Cita textual del TO: «más otros 15 (quince) días corridos a la fecha estimada de prestación o devengamiento del servicio»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 7 — `ADJ1-cd109f5d`

**TO:** Clasificación de Deudores (`cla`) · **Ancla del gold:** cla:2.1

**Pregunta:**

¿Qué financiaciones quedan comprendidas a los fines de la clasificación de deudores?

**Respuesta del sistema (completa):**

> El Knowledge Graph contiene referencias a 'financiaciones comprendidas' en el contexto de la clasificación de deudores, indicando que cada cliente y la totalidad de sus financiaciones comprendidas debe incluirse en una de cinco categorías de clasificación (Punto 6.5). También se menciona que la cartera comercial abarca todas las financiaciones comprendidas, con excepción de algunas (Punto 5.1.1). Sin embargo, la información disponible en el grafo no proporciona una definición explícita ni una lista exhaustiva de qué financiaciones específicamente quedan comprendidas a los fines de la clasificación de deudores.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe incluir los préstamos con capitales, diferencias de cotización e intereses devengados, sin deducir previsiones.
  - Cita textual del TO: «Préstamos (capitales, diferencias de cotización e intereses devengados a cobrar)»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe incluir los créditos por arrendamientos financieros sin deducir previsiones.
  - Cita textual del TO: «Créditos por arrendamientos financieros sin deducir las correspondientes previsiones»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe incluir responsabilidades eventuales como los avales otorgados sobre cheques de pago diferido.
  - Cita textual del TO: «Avales otorgados sobre cheques de pago diferido»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe incluir las obligaciones negociables, incluso las subordinadas.
  - Cita textual del TO: «Obligaciones negociables –incluye las subordinadas– y títulos de deuda de fideicomisos»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 8 — `ADJ1-d80a95f3`

**TO:** Capitales Mínimos de las Entidades Financieras (`cap`) · **Ancla del gold:** cap:6.5

**Pregunta:**

¿Cómo se mide la exposición para la exigencia de capital por riesgo de posiciones en commodities y qué compensaciones entre posiciones se admiten?

**Respuesta del sistema (completa):**

> La exposición para la exigencia de capital por riesgo de posiciones en commodities se mide aplicando la exigencia a la posición total en cada commodity. La medición se basa en el cálculo de posiciones abiertas mediante neteamiento de posiciones cortas y largas.
> 
> Respecto a las compensaciones entre posiciones, la regulación establece limitaciones significativas:
> 
> 1. **Prohibición de compensación entre diferentes productos básicos**: No se admite la compensación entre posiciones en diferentes productos básicos ni entre subcategorías diferentes del mismo producto básico.
> 
> 2. **Compensación permitida dentro del mismo subyacente**: Se permite la compensación de posiciones compradas y vendidas en la misma exposición subyacente, cuando la posición vendida tenga la misma duración que la posición comprada o su vida residual sea al menos un año. En este caso, se calcula la posición comprada neta (posición comprada bruta menos la posición vendida).
> 
> 3. **Compensación por banda temporal**: Se permite la compensación de posiciones compradas y vendidas dentro de cada banda temporal, aunque con una desestimación vertical aplicable a las posiciones compensadas.
> 
> 4. **Capital adicional**: Las entidades deben observar un requerimiento de capital adicional del 3% de la posición bruta (largas más cortas) en cada producto básico por riesgos de base, de tasa de interés y de brecha a futuro.
> 
> En síntesis, las compensaciones se admiten únicamente dentro del mismo subyacente y banda temporal, pero no entre diferentes productos básicos o subcategorías.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe dar la definición de producto básico: todo producto físico negociado o negociable en un mercado secundario.
  - Cita textual del TO: «todo producto físico negociado o negociable en un mercado secundario»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe indicar que las posiciones cortas y largas se netean solo si se trata del mismo producto básico.
  - Cita textual del TO: «Las posiciones cortas y largas podrán netearse a efectos de calcular las posiciones abiertas»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe aclarar que no se admite compensación entre productos básicos distintos ni entre subcategorías diferentes del mismo producto.
  - Cita textual del TO: «No se admite la compensación entre posiciones en diferentes productos básicos ni entre subcategorías diferentes del mismo producto básico»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe indicar que cada posición se expresa en la unidad estándar de medida correspondiente.
  - Cita textual del TO: «en términos de la correspondiente unidad estándar de medida (barriles, kilos, gramos, etc.)»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe indicar que la posición neta se convierte a pesos con el precio al contado.
  - Cita textual del TO: «se convertirá a pesos utilizando su precio al contado»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 9 — `ADJ1-edbf539d`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:13.5

**Pregunta:**

Un banco emitió una carta de crédito para garantizar una importación de servicios y ahora debe afrontar el pago. ¿Qué condiciones tiene que verificar para su propio acceso al mercado de cambios?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA, para que un banco pueda acceder al mercado de cambios a fin de pagar una carta de crédito emitida para garantizar una importación de servicios, debe verificar el cumplimiento de condiciones específicas. Las entidades están facultadas a dar acceso al mercado de cambios para cursar pagos de servicios de no residentes cuando se cumplan los requisitos aplicables. En particular, para pagos de capital de deudas originadas en importación de servicios prestados o devengados a partir del 13/12/23, las entidades podrán dar acceso al mercado de cambios cuando se cumplan los requisitos normativos aplicables. Asimismo, para pagos de intereses de deudas comerciales por importaciones de servicios, las entidades deben verificar que se cumplan las condiciones especificadas en la normativa. La operación debe cumplir con los restantes requisitos normativos aplicables. El acceso al mercado de cambios está condicionado al cumplimiento de las siguientes condiciones enumeradas en la normativa, aunque la información disponible no detalla exhaustivamente cada una de ellas en los resultados obtenidos.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que las entidades tienen acceso para pagos propios por cartas de crédito o letras avaladas que garantizan importaciones de servicios.
  - Cita textual del TO: «Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe señalar que se verifica el cumplimiento de las condiciones aplicables según la fecha de emisión u otorgamiento.
  - Cita textual del TO: «cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que para instrumentos emitidos desde el 13/12/23 la operación garantizada debía ser un servicio prestado o devengado a partir de esa fecha.
  - Cita textual del TO: «la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar la regla de plazo: el plazo del servicio más otros 15 días corridos desde la fecha estimada de prestación o devengamiento.
  - Cita textual del TO: «más otros 15 (quince) días corridos a la fecha estimada de prestación o devengamiento del servicio»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 10 — `ADJ1-39f39a84`

**TO:** Clasificación de Deudores (`cla`) · **Ancla del gold:** cla:6.1

**Pregunta:**

¿Sobre qué información se practica la revisión de la cartera comercial para clasificar a los deudores?

**Respuesta del sistema (completa):**

> La revisión de la cartera comercial para clasificar a los deudores se practica sobre la base de información financiera actualizada. Específicamente, los clientes deben proporcionar información financiera actualizada que incluye: (1) estados financieros o contables según corresponda, (2) información complementaria, y (3) proyectos de inversión. Además, las entidades deben contar con un adecuado sistema de información que permita conocer en forma regular la situación financiera y económica del cliente, asegurando que la información sea consistente.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que la revisión se basa en información financiera actualizada.
  - Cita textual del TO: «se practicará sobre la base de la información financiera»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar estados financieros o contables e información complementaria (proyectos de inversión, etc.).
  - Cita textual del TO: «estados financieros o contables –según corresponda– e información complementaria»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que la información la proporcionan los clientes ante requerimiento de las entidades.
  - Cita textual del TO: «que deberán proporcionar los clientes ante requerimiento de las»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar la aplicación de parámetros válidos para cada sector y otras circunstancias de la actividad económica.
  - Cita textual del TO: «aplicando parámetros válidos para cada sector y considerando otras circunstancias»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 11 — `ADJ1-9e3a589f`

**TO:** Protección de los Usuarios de Servicios Financieros (`pro`) · **Ancla del gold:** pro:4.4

**Pregunta:**

¿En qué casos inicia el BCRA actuaciones de oficio en materia de protección de usuarios de servicios financieros?

**Respuesta del sistema (completa):**

> El BCRA inicia actuaciones de oficio en materia de protección de usuarios de servicios financieros en los siguientes casos: (1) cuando revistan urgencia o gravedad, y (2) en las cuestiones que, detectadas como consecuencia de lo previsto en los puntos precedentes o en el marco de su actuación como autoridad de supervisión, considere puedan afectar a los usuarios en forma general.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que el BCRA inicia de oficio acciones correctivas en casos que revistan urgencia o gravedad.
  - Cita textual del TO: «El BCRA iniciará de oficio acciones correctivas en aquellos casos que revistan urgencia o gravedad»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar las cuestiones detectadas en su actuación como supervisor que puedan afectar a los usuarios en forma general.
  - Cita textual del TO: «considere puedan afectar a los usuarios en forma general»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 12 — `ADJ1-a5231498`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:3.17

**Pregunta:**

Una petrolera beneficiaria del régimen de acceso a divisas por producción incremental obtuvo la certificación correspondiente. ¿Qué operaciones puede cursar con esa certificación y quién es responsable de emitirla?

**Respuesta del sistema (completa):**

> Con la Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22), una petrolera beneficiaria puede cursar las siguientes operaciones: (1) Acceso al mercado de cambios; (2) Giro de divisas por utilidades y dividendos; (3) Repatriación de inversión directa. La certificación es emitida por una entidad financiera local única, que debe ser nominada por los beneficiarios del Régimen de acceso a divisas para la producción incremental de petróleo (RADPIP) y/o Régimen de acceso a divisas para la producción incremental de gas natural (RADPIGN). Esta entidad financiera es responsable de emitir las certificaciones y remitirlas a las entidades por las cuales el cliente desee acceder al mercado de cambios.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que el acceso es por hasta el monto de la certificación.
  - Cita textual del TO: «podrá acceder al mercado de cambios por hasta el monto de la certificación»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar los pagos de capital de deudas por importación de bienes con registro aduanero hasta el 12/12/23.
  - Cita textual del TO: «Pagos de capital de deudas originadas en la importación de bienes con registro de ingreso aduanero hasta el 12/12/23»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe mencionar los pagos de utilidades y dividendos a accionistas no residentes.
  - Cita textual del TO: «Pagos de utilidades y dividendos a accionistas no residentes»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe indicar que el beneficiario nomina una única entidad financiera local responsable de emitir las certificaciones.
  - Cita textual del TO: «deberán nominar una única entidad financiera local que será la responsable de emitir las»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 13 — `ADJ1-2e4e9c2c`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:2.6

**Pregunta:**

Una empresa de software inscripta en el registro de beneficiarios de la economía del conocimiento quiere quedar exceptuada de liquidar los cobros de sus exportaciones. ¿Qué condiciones debe cumplir y cómo funciona la certificación que lo habilita?

**Respuesta del sistema (completa):**

> Una empresa de software inscripta en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento puede quedar exceptuada de liquidar los cobros de sus exportaciones cumpliendo las siguientes condiciones:
> 
> **Condiciones principales:**
> 1. Estar inscripta en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento (Decreto 679/22).
> 2. Que los cobros de exportaciones de bienes y servicios ingresen dentro de los plazos normativos establecidos.
> 3. Contar con una "Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22)" por el equivalente del monto que se pretende no liquidar.
> 
> **Funcionamiento de la certificación:**
> 1. El beneficiario debe nominar una única entidad financiera local que será responsable de emitir las certificaciones y remitirlas a las entidades por las cuales el cliente desee concretar los ingresos de sus cobros de exportaciones.
> 2. La entidad nominada puede emitir estas certificaciones para cada período trimestral de referencia posterior a la inscripción del cliente en el registro, cuando se verifiquen la totalidad de los requisitos establecidos.
> 3. La entidad deberá verificar, previamente a emitir cada certificación, el cumplimiento de los requisitos establecidos a la fecha de emisión de la certificación.
> 4. La emisión de una certificación por parte de la entidad implica que, a la fecha de su emisión, se verifican todos los requisitos normativos previstos en la normativa.
> 5. El ejercicio de la excepción debe efectuarse dentro del plazo para la liquidación de los fondos en el mercado de cambios que sea aplicable a la operación.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que los cobros tienen que haber ingresado por el mercado de cambios en los plazos establecidos.
  - Cita textual del TO: «hayan ingresado por el mercado de cambios en los plazos establecidos en cada caso»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar la exigencia de contar con la certificación de incremento de exportaciones asociadas a la economía del conocimiento.
  - Cita textual del TO: «cuenten con una “Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22)”»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe señalar que el beneficiario nomina una única entidad financiera local responsable de emitir las certificaciones.
  - Cita textual del TO: «El beneficiario deberá nominar una única entidad financiera local que será la responsable de emitir las “Certificaciones de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22)”»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe indicar el tope del 30 % del incremento de los cobros de exportaciones respecto de igual trimestre de 2021.
  - Cita textual del TO: «no supera al equivalente en dólares estadounidenses al 30% (treinta por ciento) del incremento de los cobros de exportaciones de bienes y servicios»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---
