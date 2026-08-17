# Worksheet de adjudicación humana — EV2 fidelidad

Adjudicación según §6 del pre-registro (`docs/preregistro_evaluacion_fidelidad_ev2.md`,
commit be8a84f). Fichas en orden aleatorizado (semilla `worksheet-ev2-v1`), numeradas
1..48. Cada ficha trae: TO y ancla del gold, la pregunta, la respuesta COMPLETA
del sistema y los criterios del gold sellado con su cita textual.

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
   (todos cumplidos → correcto; ninguno → incorrecto; mezcla → parcial), vía
   `code/cerrar_adjudicacion.py`.
4. Las marcas se vuelcan en `worksheet_adjudicacion.json` (campo `veredicto`
   de cada criterio, en la ficha del mismo `id_ficha`); `observaciones` es
   libre y opcional. Este `.md` es la vista de lectura.
5. Cada ficha se adjudica por sí sola. Las fichas no indican de qué sistema ni
   de qué corrida proviene la respuesta, y no debe intentarse inferirlo.

Marcas válidas: `cumplido` | `no_cumplido`.

---


## Ficha 1 — `ADJ-13f0a36d`

**TO:** Protección de los Usuarios de Servicios Financieros (`pro`) · **Ancla del gold:** pro:1.3

**Pregunta:**

¿Cómo se articulan las normas de protección de usuarios de servicios financieros con la legislación general de defensa del consumidor, y a quiénes se aplican?

**Respuesta del sistema (completa):**

> Las normas sobre protección de usuarios de servicios financieros se articulan como complementarias de la legislación general de defensa del consumidor. Específicamente, estas normas son complementarias de las disposiciones contenidas en el Código Civil y Comercial de la Nación, la Ley 24.240 de Defensa del Consumidor, la Ley 25.065 de Tarjetas de Crédito, y de las normas emitidas por la Autoridad Nacional de Aplicación de estas leyes.
> 
> En cuanto a los sujetos a los que se aplican:
> 
> 1. **Usuarios de servicios financieros**: Son las contrapartes que se relacionan con los sujetos obligados. Tienen derechos específicos como la protección de su seguridad e intereses económicos, trato equitativo y digno, y libertad de elección en toda relación de consumo.
> 
> 2. **Sujetos obligados**: Son las entidades financieras y otros proveedores de servicios financieros que deben cumplir con las obligaciones de protección al usuario. Estos incluyen bancos, entidades financieras, cajas de crédito cooperativas y otras entidades reguladas por el BCRA.
> 
> La articulación se produce de manera que las normas de protección de usuarios de servicios financieros funcionan como un complemento específico a la legislación general de consumo, estableciendo obligaciones particulares para los sujetos obligados en sus relaciones con los usuarios de servicios financieros.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que las normas son complementarias de la legislación aplicable a las relaciones de consumo.
  - Cita textual del TO: «Las normas sobre “Protección de los usuarios de servicios financieros” son complementarias de las disposiciones contenidas en la legislación y regulaciones aplicables a las relaciones de consumo, en especial de lo previsto en el Código Civil y Comercial de la Nación, en la Ley 24.240 de Defensa del Consumidor, en la Ley 25.065 de Tarjetas de Crédito, y de las normas emitidas por la Autoridad Nacional de Aplicación de estas leyes y, si correspondiese, de la demás legislación y regulaciones emitidas por las autoridades provinciales en cuanto resulte de su jurisdicción y competencia»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar el Código Civil y Comercial, la Ley 24.240 de Defensa del Consumidor y la Ley 25.065 de Tarjetas de Crédito.
  - Cita textual del TO: «24.240 de Defensa del Consumidor, en la Ley 25.065 de Tarjetas de Crédito»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que se aplican a los sujetos obligados de acuerdo a los tipos y funcionalidades de su operatoria particular.
  - Cita textual del TO: «acuerdo a los tipos y funcionalidades de su operatoria particular y a las modalidades de»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 2 — `ADJ-eef4a997`

**TO:** Clasificación de Deudores (`cla`) · **Ancla del gold:** cla:3.5

**Pregunta:**

¿A quién puede encomendar una entidad financiera la tarea de clasificar a sus deudores y qué recaudos exige cada alternativa?

**Respuesta del sistema (completa):**

> Una entidad financiera puede encomendar la tarea de clasificación de deudores a dos alternativas principales:
> 
> 1. **Al sector de créditos de la entidad**: Si opta por esta alternativa, la entidad financiera deberá contar con una oficina independiente que tendrá como función efectuar la revisión de las clasificaciones asignadas a los clientes por el sector de créditos.
> 
> 2. **A la auditoría interna de la entidad**: La revisión de clasificaciones puede estar a cargo de la auditoría interna de la entidad, debiendo comprender obligatoriamente a los clientes cuyo endeudamiento total en pesos y en moneda extranjera supere el 1% de la responsabilidad patrimonial computable de la entidad del mes anterior al de la clasificación o el equivalente al importe de referencia establecido en el punto 3.7 (de ambos el menor), y alcanzar como mínimo el 20% de la cartera activa total.
> 
> En ambos casos, la intervención de terceros no releva a la entidad de su responsabilidad por la clasificación de deudores. Cuando un tercero desarrolle tareas relativas a servicios ofrecidos por los sujetos obligados o en su nombre, ambos serán responsables por el cumplimiento de las normas, debiendo establecerse esto en los instrumentos que acuerden la realización de dichas tareas.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe mencionar la opción de un área independiente del sector de otorgamiento de créditos y garantías.
  - Cita textual del TO: «A un área independiente del sector encargado del otorgamiento de créditos y garantías»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe indicar que si clasifica el propio sector de créditos, una oficina independiente revisa las clasificaciones asignadas.
  - Cita textual del TO: «que tendrá como función efectuar la revisión de las clasificaciones asignadas a los clientes por el sector de créditos»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que la revisión debe estar concluida antes de la presentación del Estado de situación de deudores.
  - Cita textual del TO: «La revisión deberá estar concluida antes de presentarse a la Superintendencia»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar la opción de profesionales externos, sin que ello releve a la entidad de su responsabilidad.
  - Cita textual del TO: «no releva a la entidad de su responsabilidad»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 3 — `ADJ-8fffa849`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:10.8

**Pregunta:**

Una deuda con el exterior por importación de bienes dejó de encuadrar como deuda comercial. ¿Cómo se cursa su cancelación por el mercado de cambios y con qué concepto se registra?

**Respuesta del sistema (completa):**

> Cuando una deuda con el exterior por importación de bienes deja de encuadrar como deuda comercial, se cursa su cancelación mediante el mercado de cambios como un endeudamiento financiero. La operación se registra bajo la categoría de 'Pago capital e intereses endeudamiento financiero' comprendido en el punto 3.5 de la normativa, habilitándose la cancelación de sus servicios de capital e intereses a partir del vencimiento mediante aplicación de cobros de exportaciones de bienes y servicios. Sin embargo, el grafo no especifica el concepto exacto de boleto de cambio ni los detalles precisos del registro cambiario para esta reclasificación.

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


## Ficha 4 — `ADJ-07343665`

**TO:** Clasificación de Deudores (`cla`) · **Ancla del gold:** cla:10.3

**Pregunta:**

Una sociedad de garantía recíproca pagó la deuda de una MiPyME en cumplimiento de la garantía que la respaldaba. ¿Qué obligación de clasificación le cabe y con qué criterios?

**Respuesta del sistema (completa):**

> Una sociedad de garantía recíproca que pagó la deuda de una MiPyME en cumplimiento de la garantía que la respaldaba tiene la obligación de clasificar a esa MiPyME. La clasificación debe realizarse en función de la mora, según los criterios aplicables para la cartera de consumo o vivienda, y por aplicación de las disposiciones previstas en el punto 7.3 (reclasificación obligatoria). Los criterios de clasificación por mora incluyen categorías como: Normal (clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días), Observación (con seguimiento especial), Deficiente e Irrecuperable. La sociedad de garantía recíproca debe ejecutar esta clasificación de deudor como parte de sus obligaciones regulatorias.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que las SGR y los fondos de garantía públicos inscriptos en los registros del BCRA deben clasificar a esas MiPyMEs.
  - Cita textual del TO: «inscriptos en los Registros habilitados en el BCRA deberán clasificar a las MiPyMEs»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe precisar que se clasifica a las MiPyMEs cuyas deudas fueron canceladas en cumplimiento de las garantías.
  - Cita textual del TO: «cuyas deudas hayan sido canceladas en cumplimiento de las garantías que respaldaban las respectivas obligaciones»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que la clasificación es en función de la mora, con los criterios de la cartera de consumo o vivienda.
  - Cita textual del TO: «La clasificación se realizará en función de la mora, según los criterios aplicables para la cartera de»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar la aplicación de la reclasificación obligatoria.
  - Cita textual del TO: «(reclasificación obligatoria)»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 5 — `ADJ-20edbe06`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:13.5

**Pregunta:**

Un banco emitió una carta de crédito para garantizar una importación de servicios y ahora debe afrontar el pago. ¿Qué condiciones tiene que verificar para su propio acceso al mercado de cambios?

**Respuesta del sistema (completa):**

> Para que un banco pueda acceder al mercado de cambios con el fin de pagar una carta de crédito emitida para garantizar una importación de servicios, debe verificar el cumplimiento de condiciones específicas. Según la regulación del BCRA, las entidades podrán dar acceso al mercado de cambios para cursar pagos de servicios de no residentes que fueron o serán prestados a partir del 13/12/23 cuando se cumplan los requisitos aplicables. El pago de capital e intereses de deudas por importación de bienes y servicios se admite a partir del vencimiento. A los efectos del acceso al mercado de cambios, se considera deuda comercial por importación de servicios a los endeudamientos originados en la adquisición de servicios a no residentes que sean análogos a aquellos enunciados en las normas para importación de bienes. El banco, como entidad autorizada a operar en cambios, será responsable de verificar el cumplimiento de las condiciones estipuladas en la normativa que habilitan el acceso al mercado de cambios.

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


## Ficha 6 — `ADJ-7d63cd1b`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:5.7

**Pregunta:**

¿Cuándo debe registrar una entidad ante el BCRA sus operaciones de cambio con clientes, y con qué identificación se registra la operación de un turista extranjero o de un fondo común de inversión?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA, las entidades deben dar cumplimiento a los requisitos de identificación de sus clientes y registro de las operaciones ante el BCRA según el régimen informativo correspondiente (Punto 1.6). El cliente que realiza la operación de cambio deberá ser identificado por la entidad de acuerdo con lo previsto en el punto 5.4.
> 
> Respecto a la identificación específica:
> 
> 1. **Para turistas extranjeros**: Se admite la utilización del número de pasaporte u otro documento habilitante para el ingreso al país, según lo previsto en el Punto 5.4.1, que establece que el cliente deberá presentar un documento de identidad admitido en las normas sobre 'Documentos de identificación en vigencia' u otros documentos habilitantes en el caso de turistas.
> 
> 2. **Para fondos comunes de inversión**: Se utiliza el código asignado por la Comisión Nacional de Valores (CNV) cuando se trate de un fondo común de inversión, según lo previsto en el Punto 5.7.3.2.
> 
> 3. **Identificación general**: Se utilizará CUIT, CUIL, CDI, CIE o DNI del cliente que realiza la operación (Punto 5.7.3).
> 
> Sin embargo, la información disponible en el grafo no especifica explícitamente el plazo exacto (en horas o días) dentro del cual debe registrarse la operación de cambio ante el BCRA.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que se registra ante el BCRA toda operación realizada en el mercado de cambios.
  - Cita textual del TO: «La entidad deberá registrar ante el BCRA toda operación que realice en el mercado de cambios»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe indicar que el registro se realiza en la fecha de concertación.
  - Cita textual del TO: «El registro de esas operaciones se deberá realizar en la fecha de su concertación en el mercado de cambios»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe mencionar los identificadores generales (CUIT, CUIL, CDI, CIE o DNI del cliente).
  - Cita textual del TO: «se utilizará CUIT, CUIL, CDI, CIE o DNI del cliente que realiza la operación»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe indicar que para personas humanas no residentes se admite el pasaporte u otro documento habilitante para el ingreso al país.
  - Cita textual del TO: «Número de pasaporte u otro documento habilitante para el ingreso al país cuando se trate de personas humanas no residentes»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe indicar que para un fondo común de inversión se usa el código asignado por la Comisión Nacional de Valores.
  - Cita textual del TO: «Código asignado por la Comisión Nacional de Valores cuando se trate de un fondo común de inversión»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 7 — `ADJ-80fa6a9d`

**TO:** Clasificación de Deudores (`cla`) · **Ancla del gold:** cla:3.5

**Pregunta:**

¿A quién puede encomendar una entidad financiera la tarea de clasificar a sus deudores y qué recaudos exige cada alternativa?

**Respuesta del sistema (completa):**

> Una entidad financiera puede encomendar la tarea de clasificación de deudores a dos alternativas principales:
> 
> 1. **Al sector de créditos de la propia entidad**: Si opta por esta alternativa, la entidad financiera deberá contar con una oficina independiente que tendrá como función efectuar la revisión de las clasificaciones asignadas a los clientes por el sector de créditos.
> 
> 2. **A la auditoría interna de la entidad**: La revisión de clasificaciones puede estar a cargo de la auditoría interna de la entidad. Esta revisión deberá comprender obligatoriamente a los clientes cuyo endeudamiento total en pesos y en moneda extranjera supere el 1% de la responsabilidad patrimonial computable de la entidad del mes anterior al de la clasificación o el equivalente al importe de referencia establecido en el punto 3.7 (de ambos el menor), y alcanzar como mínimo el 20% de la cartera activa total.
> 
> **Recaudos generales para cualquier alternativa:**
> - La intervención de terceros no releva a la entidad de su responsabilidad por la clasificación finalmente asignada ni de la obligación de conservar los legajos con la información requerida.
> - Cuando un tercero desarrolle tareas relativas a servicios ofrecidos por los sujetos obligados o en su nombre, ambos serán responsables por el cumplimiento de las normas aplicables, lo que deberá establecerse en los instrumentos que acuerden la realización de dichas tareas.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe mencionar la opción de un área independiente del sector de otorgamiento de créditos y garantías.
  - Cita textual del TO: «A un área independiente del sector encargado del otorgamiento de créditos y garantías»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe indicar que si clasifica el propio sector de créditos, una oficina independiente revisa las clasificaciones asignadas.
  - Cita textual del TO: «que tendrá como función efectuar la revisión de las clasificaciones asignadas a los clientes por el sector de créditos»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que la revisión debe estar concluida antes de la presentación del Estado de situación de deudores.
  - Cita textual del TO: «La revisión deberá estar concluida antes de presentarse a la Superintendencia»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar la opción de profesionales externos, sin que ello releve a la entidad de su responsabilidad.
  - Cita textual del TO: «no releva a la entidad de su responsabilidad»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 8 — `ADJ-1156c72a`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:9.5

**Pregunta:**

¿Qué información mínima debe contener la certificación de aplicación de cobros de exportaciones que emite la entidad encargada del seguimiento y en qué moneda se expresan los montos?

**Respuesta del sistema (completa):**

> La certificación de aplicación de cobros de exportaciones que emite la entidad encargada del seguimiento debe contener, como mínimo, la siguiente información: CUIT y denominación del exportador, fecha de emisión de la certificación, permiso de embarque al cual corresponden los cobros aplicados, fecha de aplicación, tipo de operación cancelada, concepto que se canceló (capital y/o interés), moneda y monto de la aplicación imputada al mismo. Respecto a la moneda en que se expresan los montos, la normativa requiere que se especifique la moneda en la certificación, pero no prescribe una moneda única obligatoria para expresar los montos.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe incluir CUIT y denominación del exportador y fecha de emisión de la certificación.
  - Cita textual del TO: «CUIT y denominación del exportador, fecha de emisión de la certificación»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe incluir el permiso de embarque al que corresponden los cobros aplicados y la fecha de aplicación.
  - Cita textual del TO: «permiso de embarque al cual corresponden los cobros aplicados, fecha de aplicación»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe incluir el tipo de operación cancelada, el concepto (capital y/o interés), la moneda y el monto imputado.
  - Cita textual del TO: «tipo de operación cancelada, concepto que se canceló (capital y/o interés), moneda y monto de la aplicación imputada»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe indicar que los montos se expresan en la moneda oportunamente liquidada por el mercado de cambios.
  - Cita textual del TO: «Los montos deberán estar expresados en la moneda que oportunamente fue liquidada por el mercado de cambios»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 9 — `ADJ-5cef4061`

**TO:** Régimen Informativo Contable Mensual (`ric`) · **Ancla del gold:** ric:5.2

**Pregunta:**

Para la exigencia por riesgo operacional del régimen informativo mensual, ¿qué se informa del indicador de negocio y qué componentes lo integran?

**Respuesta del sistema (completa):**

> Para la exigencia por riesgo operacional del régimen informativo mensual, el indicador de negocio (BI) se calcula mediante la expresión: BI = VA_Prom(ILDC + SC + FC + RM), donde VA_Prom representa el valor absoluto del promedio. Los componentes que integran el indicador de negocio son: ILDC (Ingresos por Líneas de Crédito), SC (Servicios y Comisiones), FC (Financieros/Comisiones), y RM (Resultados Misceláneos). Este indicador se utiliza como aproximación al riesgo operacional a partir de información de estados financieros. El promedio que se emplea para el cálculo del BI debe cubrir los últimos 12 meses, con excepciones para operaciones de fusiones y adquisiciones que pueden requerir períodos de 36 meses.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que se informa el BIC calculado.
  - Cita textual del TO: «Se informará el BIC calculado»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe incluir el componente de intereses, arrendamientos y dividendos (ILDC).
  - Cita textual del TO: «ILDC (Prom) - Componente de intereses, arrendamientos y dividendos»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe incluir el componente de servicios (SC).
  - Cita textual del TO: «SC (Prom) - Componente de servicios»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe incluir el componente financiero (FC).
  - Cita textual del TO: «FC (Prom) - Componente financiero»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe incluir el resultado monetario total (RM).
  - Cita textual del TO: «RM (Prom) - Resultado Monetario total»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 10 — `ADJ-d7050380`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:4.6.1

**Pregunta:**

Una empresa local tiene dividendos aprobados por asamblea que siguen pendientes de pago a su accionista del exterior y evalúa suscribir bonos BOPREAL por esa deuda. ¿Qué debe verificar la entidad que concreta la suscripción y con qué tope?

**Respuesta del sistema (completa):**

> La entidad que concrete la suscripción de bonos BOPREAL por dividendos pendientes de pago debe verificar que: (1) la deuda pendiente corresponde a utilidades y dividendos de balances cerrados y auditados, según la documentación que le permite avalar esta condición. Esta verificación debe realizarse previo a la suscripción.
> 
> Respecto al tope de suscripción, los clientes no residentes podrán suscribir Bonos BOPREAL por hasta el equivalente al monto en moneda local de las utilidades y dividendos cobrados a partir del 01/09/19 según la distribución determinada por la asamblea de accionistas, ajustado por el último IPC disponible.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar el tope: hasta el equivalente en moneda local de las utilidades y dividendos pendientes de pago según la distribución de la asamblea.
  - Cita textual del TO: «por hasta el equivalente al monto en moneda local de las utilidades y dividendos pendientes de pago a accionistas no residentes a partir de la distribución determinada por la asamblea de accionistas»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar la documentación que avale que la deuda corresponde a utilidades y dividendos de balances cerrados y auditados.
  - Cita textual del TO: «la deuda pendiente corresponde a utilidades y dividendos de balances cerrados y auditados»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe incluir la declaración de la operación en el Relevamiento de activos y pasivos externos, de corresponder.
  - Cita textual del TO: «La operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar la declaración jurada del cliente de que no utilizó ya este mecanismo por esa deuda.
  - Cita textual del TO: «no ha utilizado ya este mecanismo por esta deuda»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe indicar el boleto de venta de cambio por el concepto de registro de utilidades y dividendos por adjudicación de bonos BOPREAL.
  - Cita textual del TO: «I09. Registro de utilidades y dividendos por adjudicación de bonos BOPREAL»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 11 — `ADJ-154d5c45`

**TO:** Capitales Mínimos de las Entidades Financieras (`cap`) · **Ancla del gold:** cap:4.2

**Pregunta:**

Para las operaciones con derivados OTC de un banco, ¿cómo se determina la exposición al riesgo de crédito de contraparte bajo el enfoque estándar y qué papel juegan los márgenes de variación?

**Respuesta del sistema (completa):**

> Bajo el enfoque estándar (SACCR - Standardised Approach for Counterparty Credit Risk), la exposición al riesgo de crédito de contraparte para operaciones con derivados OTC se determina calculando la EAD (Exposure at Default) por separado para cada conjunto de neteo. La exposición se calcula conforme al enfoque estandarizado para el riesgo de crédito de contraparte (SACCR) establecido en la regulación del BCRA.
> 
> La fórmula fundamental para operaciones sin márgenes de variación es: CR = V - C, donde CR es el costo de reposición (exposición presente respecto de la contraparte), V es el valor actual de mercado de las operaciones con derivados en el conjunto de neteo, y C es el valor neto de los activos recibidos y dados en garantía. El CR no puede tener un valor negativo, estableciéndose un mínimo de 0.
> 
> Respecto al papel de los márgenes de variación: estos juegan un rol limitador en la determinación de la exposición. Específicamente, la EAD para un conjunto de neteo con márgenes de variación tendrá como límite superior la EAD que resultaría para el mismo conjunto si no los tuviera. Esto significa que aunque los márgenes de variación reducen la exposición presente al ajustar diariamente los valores de las posiciones, no pueden reducir la EAD por debajo de lo que sería sin ellos.
> 
> Además, en lugar de calcular el ajuste de valuación del crédito (CVA) para exposiciones por derivados, las entidades deben multiplicar la exposición al riesgo de crédito de contraparte por un factor de 1,5 antes de aplicar el ponderador de riesgo correspondiente.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que la EAD se calcula por separado para cada conjunto de neteo.
  - Cita textual del TO: «La exposición al riesgo de crédito de contraparte (EAD) se calculará por separado para cada conjunto de neteo»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar el factor alfa igual a 1,40.
  - Cita textual del TO: «α = 1,40»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe explicar que el cálculo del costo de reposición y de la exposición potencial futura difiere según haya o no intercambio de márgenes de variación.
  - Cita textual del TO: «El cálculo del CR y de la EPF diferirá según que los conjuntos de neteo estén sujetos o no al intercambio de márgenes de variación»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe indicar el límite superior: la EAD con márgenes de variación no supera la EAD del mismo conjunto sin ellos.
  - Cita textual del TO: «La EAD para un conjunto de neteo con márgenes de variación tendrá como límite superior la EAD que resultaría para el mismo conjunto si no los tuviera»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 12 — `ADJ-6cc24f93`

**TO:** Capitales Mínimos de las Entidades Financieras (`cap`) · **Ancla del gold:** cap:4.2

**Pregunta:**

Para las operaciones con derivados OTC de un banco, ¿cómo se determina la exposición al riesgo de crédito de contraparte bajo el enfoque estándar y qué papel juegan los márgenes de variación?

**Respuesta del sistema (completa):**

> Bajo el enfoque estándar (SA-CCR) para derivados OTC, la exposición al riesgo de crédito de contraparte se determina de manera diferenciada según exista o no intercambio de márgenes de variación:
> 
> **Para operaciones SIN márgenes de variación:**
> El crédito de riesgo (CR) se calcula como: CR = V - C, donde V es el valor actual de mercado de las operaciones con derivados y C es el valor neto de activos en garantía con aforos. Adicionalmente, existe una restricción fundamental: la exposición presente respecto de la contraparte no puede tener un valor negativo.
> 
> **Para operaciones CON márgenes de variación:**
> El CR se define como la mayor exposición que no alcanza a activar un aumento del margen de variación, determinada por la expresión: CR = máx. (V - C; TH + MTA - NICA; 0), donde estos componentes representan el máximo entre el valor neto de la posición y el umbral de margen más el ajuste mínimo de transferencia menos el importe neto en cuenta de garantía.
> 
> **Papel de los márgenes de variación:**
> Los márgenes de variación juegan un papel crucial en la mitigación del riesgo de crédito. Específicamente, la EAD (Exposure at Default) para un conjunto de neteo con márgenes de variación tiene como límite superior la EAD que resultaría para el mismo conjunto si no los tuviera. Esto significa que los márgenes reducen la exposición efectiva al riesgo, pero no pueden eliminarla completamente.
> 
> La exigencia final por riesgo de crédito de contraparte (RCD) en operaciones con derivados OTC surge de la sumatoria de las exposiciones al riesgo de crédito de contraparte determinadas para cada conjunto de neteo, conforme al enfoque estandarizado establecido en las normas de Capitales Mínimos.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que la EAD se calcula por separado para cada conjunto de neteo.
  - Cita textual del TO: «La exposición al riesgo de crédito de contraparte (EAD) se calculará por separado para cada conjunto de neteo»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar el factor alfa igual a 1,40.
  - Cita textual del TO: «α = 1,40»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe explicar que el cálculo del costo de reposición y de la exposición potencial futura difiere según haya o no intercambio de márgenes de variación.
  - Cita textual del TO: «El cálculo del CR y de la EPF diferirá según que los conjuntos de neteo estén sujetos o no al intercambio de márgenes de variación»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe indicar el límite superior: la EAD con márgenes de variación no supera la EAD del mismo conjunto sin ellos.
  - Cita textual del TO: «La EAD para un conjunto de neteo con márgenes de variación tendrá como límite superior la EAD que resultaría para el mismo conjunto si no los tuviera»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 13 — `ADJ-b3d2893a`

**TO:** Capitales Mínimos de las Entidades Financieras (`cap`) · **Ancla del gold:** cap:8.6

**Pregunta:**

Una entidad financiera planea un aumento de capital. ¿En qué forma deben efectuarse los aportes, qué excepciones se admiten y cómo se computan hasta su aprobación?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA, los aportes para aumento de capital deben efectuarse de la siguiente forma:
> 
> **Forma de efectuar los aportes:**
> A los fines de todas las reglamentaciones vinculadas al capital, su integración y aumento, los aportes deben ser efectuados en efectivo.
> 
> **Excepciones admitidas:**
> Se admiten excepciones al requisito de efectivo en el punto 8.6.3, que contempla aportes en instrumentos de deuda y bienes. Cuando se trate de aportes de capital referidos en punto 8.6.3, los instrumentos de deuda deberán encontrarse registrados en el último estado financiero anual o trimestral inmediato anterior a la fecha de convocatoria de la Asamblea. En estos casos, los aportes deberán registrarse a su valor de mercado o, cuando se trate de entidades financieras que realicen oferta pública de sus acciones, al precio que fije la autoridad de contralor competente del correspondiente mercado.
> 
> **Cómputo hasta su aprobación:**
> Hasta tanto se le haya notificado la aprobación de los aportes y en la medida en que éstos hayan sido contabilizados, se deducirán del respectivo componente de la RPC (Reserva de Patrimonio Contable) de la entidad financiera.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar la regla general: los aportes deben ser efectuados en efectivo.
  - Cita textual del TO: «los aportes deben ser efectuados en efectivo»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar que excepcionalmente, con autorización previa de la SEFyC, se admiten otros aportes.
  - Cita textual del TO: «Excepcionalmente, mediando autorización previa de la SEFyC, podrán admitirse aportes en»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe incluir entre las excepciones los títulos valores públicos nacionales.
  - Cita textual del TO: «títulos valores públicos nacionales»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe indicar que esos aportes se registran a su valor de mercado.
  - Cita textual del TO: «los aportes deberán registrarse a su valor de mercado»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe señalar que hasta la notificación de la aprobación los aportes contabilizados se deducen del componente de la RPC.
  - Cita textual del TO: «Hasta tanto se le haya notificado la aprobación de los aportes y en la medida en que éstos hayan sido contabilizados, se deducirán del respectivo componente de la RPC»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 14 — `ADJ-f773f42b`

**TO:** Protección de los Usuarios de Servicios Financieros (`pro`) · **Ancla del gold:** pro:2.4

**Pregunta:**

¿Qué obligaciones de publicidad y de entrega de información tienen los bancos frente a los usuarios respecto de comisiones, contratos de adhesión y copia de los instrumentos suscriptos?

**Respuesta del sistema (completa):**

> Los bancos tienen las siguientes obligaciones de publicidad y entrega de información frente a los usuarios:
> 
> **Sobre Comisiones:**
> - Deben informar las comisiones y cargos asociados al producto o servicio, así como el mecanismo para aplicar cambios a las condiciones pactadas.
> - Los contratos deben contener las comisiones y cargos, así como los términos y condiciones y demás circunstancias conforme a las cuales hayan sido ofrecidos, publicitados y convenidos.
> 
> **Sobre Contratos de Adhesión:**
> - Deben publicar en su sitio de Internet institucional los modelos de contrato de adhesión de todos los productos y/o servicios ofrecidos, discriminando por cada modalidad, plan, producto y/o servicio.
> 
> **Sobre Copia de Instrumentos Suscriptos:**
> - En todos los casos se deberá entregar a los usuarios copia íntegra de los instrumentos que suscriben al momento de solicitar productos o servicios financieros.
> - Los usuarios tienen derecho a recibir información clara, suficiente, veraz y de fácil acceso y visibilidad acerca de los productos y/o servicios que contraten, incluyendo copia de los instrumentos que suscriban.
> - La auditoría interna debe verificar que se proporciona a los usuarios copia de los formularios que firman y ejemplares de los contratos formalizados con el sujeto obligado, en tiempo y forma previstos.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar la entrega en casas operativas de un detalle de productos y servicios precisando la totalidad de comisiones y cargos.
  - Cita textual del TO: «un detalle con las características de los productos y servicios que ofrecen»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar la publicación en el sitio de Internet institucional de los modelos de contrato de adhesión de todos los productos y/o servicios.
  - Cita textual del TO: «deberán publicar en su sitio de Internet institucional los modelos de contrato de adhesión de todos los productos y/o servicios ofrecidos»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que el acceso es por un único hipervínculo en lugar destacado de la página de inicio.
  - Cita textual del TO: «a través de un único hipervínculo y ocupar un lugar destacado»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar la entrega de copia íntegra de los instrumentos suscriptos y la consulta y descarga del contrato por home banking.
  - Cita textual del TO: «la consulta y descarga del contrato suscripto»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 15 — `ADJ-30527501`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:5.10

**Pregunta:**

Trabajo en la mesa de cambios de un banco. Cuando la entidad opera por cuenta propia, ¿en qué casos debe confeccionar boletos de cambio a su propio nombre, con qué fecha se registran esas operaciones y qué movimientos quedan afuera del registro cambiario?

**Respuesta del sistema (completa):**

> Cuando una entidad opera por cuenta propia, debe confeccionar boletos de cambio a su propio nombre en los siguientes casos: (1) cobros o pagos en moneda extranjera por operaciones cambiarias propias en carácter de cliente, y (2) operaciones de cambio, canje o arbitraje con el BCRA y otras entidades financieras o cambiarias del país.
> 
> Estas operaciones propias deberán registrarse en la fecha en que se produce el efecto sobre su PGC (Plan General de Cuentas).
> 
> Quedan excluidos del registro cambiario a nombre de la propia entidad los movimientos en moneda extranjera en el país asociados a su operatoria de créditos y depósitos.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que corresponden boletos a nombre propio por cobros o pagos en moneda extranjera por operaciones cambiarias propias en carácter de cliente.
  - Cita textual del TO: «Cobros o pagos en moneda extranjera por operaciones cambiarias propias en carácter de cliente»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe incluir las operaciones de cambio, canje o arbitraje con el BCRA y otras entidades financieras o cambiarias del país.
  - Cita textual del TO: «Operaciones de cambio, canje o arbitraje con el BCRA y otras entidades financieras o cambiarias del país»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe señalar que las operaciones propias se registran en la fecha en que producen efecto sobre la PGC.
  - Cita textual del TO: «deberán registrarse en la fecha en que se produce el efecto sobre su PGC»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe aclarar que no corresponde registro cambiario a nombre propio por movimientos en moneda extranjera en el país asociados a la operatoria de créditos y depósitos.
  - Cita textual del TO: «No corresponderá realizar registro cambiario a nombre de la propia entidad por movimientos en moneda extranjera en el país asociados a su operatoria de créditos y depósitos»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 16 — `ADJ-1188dd99`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:6.10

**Pregunta:**

Para imputar una donación recibida desde el exterior necesito entender la categoría cambiaria de transferencias corrientes: ¿cómo se define y qué operaciones incluye?

**Respuesta del sistema (completa):**

> Las transferencias corrientes se definen como operaciones en las que un residente de una economía provee bienes, servicios, activos financieros u otros activos no producidos a un residente de otra economía, sin recibir a cambio una contraprestación con valor económico. Las transferencias personales, que forman parte de esta categoría, corresponden a transferencias entre personas humanas, residentes y no residentes, independientemente de la relación entre ellas. Las donaciones recibidas desde el exterior se clasifican como operaciones dentro de la categoría de transferencias corrientes (Punto 6.10 del Texto Ordenado). Estas transferencias corrientes afectan el nivel de ingreso disponible e influyen en el consumo de bienes y servicios. Otras operaciones que se incluyen en esta categoría son las transferencias de fondos de jubilaciones y pensiones, y las transferencias en concepto de ayuda familiar.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe dar la definición: un residente provee bienes, servicios o activos a un residente de otra economía sin contraprestación con valor económico.
  - Cita textual del TO: «un residente de una economía provee bienes, servicios, activos financieros u otros activos no producidos a un residente de otra economía, sin recibir a cambio una contraprestación con valor económico»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe explicar que afectan el ingreso disponible y el consumo del donante y del receptor.
  - Cita textual del TO: «afectan el nivel de ingreso disponible e influyen en el consumo de bienes y servicios»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe mencionar que incluyen transferencias personales, donaciones, jubilaciones y pensiones.
  - Cita textual del TO: «Incluye entre otras las transferencias personales, donaciones, jubilaciones y pensiones»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe precisar que las transferencias personales son entre personas humanas, residentes y no residentes, independientemente de su relación.
  - Cita textual del TO: «corresponden a transferencias entre personas humanas, residentes y no residentes, independientemente de la relación entre ellas»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 17 — `ADJ-b16a650e`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:13.5

**Pregunta:**

Un banco emitió una carta de crédito para garantizar una importación de servicios y ahora debe afrontar el pago. ¿Qué condiciones tiene que verificar para su propio acceso al mercado de cambios?

**Respuesta del sistema (completa):**

> Para acceder al mercado de cambios con el fin de pagar una carta de crédito emitida para garantizar una importación de servicios, el banco debe verificar que se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito. Específicamente: (1) Si la carta fue emitida antes del 13/12/23 y los servicios fueron prestados/devengados hasta el 12/12/23, debe verificar que la operación encuadra en alguna de las situaciones previstas en el punto 13.4 de la normativa. (2) Si la carta fue emitida a partir del 13/12/23, debe contar con documentación que demuestre que al momento de la emisión la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero. El acceso al mercado de cambios está condicionado al cumplimiento de estas condiciones aplicables según la fecha de emisión y el tipo de operación garantizada.

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


## Ficha 18 — `ADJ-9e226344`

**TO:** Protección de los Usuarios de Servicios Financieros (`pro`) · **Ancla del gold:** pro:2.5

**Pregunta:**

Un banco quiere subir una comisión, crear otra para un producto nuevo y reducir una tercera. ¿Qué debe informar al BCRA en cada caso y en qué momento?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA, un banco debe informar al BCRA de manera diferente según el tipo de cambio en comisiones:
> 
> 1. **Aumento de comisión existente**: Debe informar PREVIAMENTE al BCRA antes de implementar el aumento. La notificación debe realizarse por la vía consignada en la normativa.
> 
> 2. **Creación de comisión para producto nuevo**: Debe informar PREVIAMENTE al BCRA antes de comercializar el nuevo producto o servicio con su comisión asociada. También debe realizarse por la vía consignada en la normativa.
> 
> 3. **Reducción de comisión**: Debe informar al BCRA DENTRO DE LOS 30 DÍAS CORRIDOS SIGUIENTES de su aplicación (es decir, después de implementada).
> 
> En resumen: los aumentos y altas de comisiones requieren notificación previa, mientras que las reducciones se informan dentro de 30 días después de aplicadas.

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


## Ficha 19 — `ADJ-0f27d616`

**TO:** Régimen Informativo Contable Mensual (`ric`) · **Ancla del gold:** ric:4.2

**Pregunta:**

¿Qué exigencias componen el modelo de información de riesgo de mercado del régimen informativo mensual y con qué apertura se informa el riesgo de tasa?

**Respuesta del sistema (completa):**

> El modelo de información de riesgo de mercado del régimen informativo mensual está compuesto por las siguientes exigencias: (1) Exigencia por riesgo de tasa (Total, Específico y General); (2) Exigencia por riesgo de acciones (Total, Específico, General y Adicional por derivados); (3) Exigencia por riesgo de opciones; y (4) Exigencia por riesgo de commodities. Respecto al riesgo de tasa específicamente, la información se presenta con apertura por: Total (código 311000/xx), Específico (código 311100/xx) y General (código 311200/xx), donde xx corresponde al día del mes de la información.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe incluir la exigencia por riesgo de tasa con apertura total/específico/general.
  - Cita textual del TO: «Exigencia por riesgo de tasa - Específico»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe incluir la exigencia por riesgo de acciones, con el adicional por derivados.
  - Cita textual del TO: «Exigencia por riesgo de acciones - Adicional por derivados»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe incluir la exigencia por riesgo de tipo de cambio.
  - Cita textual del TO: «Exigencia por riesgo de tipo de cambio»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe incluir la exigencia por riesgo de posiciones en opciones.
  - Cita textual del TO: «Exigencia por riesgo de posiciones en opciones»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe incluir la exigencia por riesgo de posiciones en productos básicos (commodities).
  - Cita textual del TO: «Exigencia por riesgo de posiciones en productos básicos – commodities -»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 20 — `ADJ-f2bc991c`

**TO:** Régimen Informativo Contable Mensual (`ric`) · **Ancla del gold:** ric:9.2

**Pregunta:**

¿Qué tipos de incrementos de exigencia por riesgo de crédito se informan en el régimen informativo mensual y cómo se desagrega cada uno según el estado de la información?

**Respuesta del sistema (completa):**

> En el régimen informativo mensual se informan los siguientes tipos de incrementos de exigencia por riesgo de crédito:
> 
> 1. **Incremento por exceso en la relación de activos inmovilizados**: Se desagrega según el estado de la información en: información en término, fuera de término, incumplimientos reiterados, o determinado por la SEFyC.
> 
> 2. **Incremento por exceso en Grandes Exposiciones al Riesgo de Crédito**: Se desagrega según el estado de la información en: información en término, fuera de término, incumplimientos reiterados, o determinado por la SEFyC.
> 
> 3. **Incremento por exceso en graduación del crédito**: Se desagrega según el estado de la información en: información en término, fuera de término, incumplimientos reiterados, o determinado por la SEFyC.
> 
> 4. **Incremento por exceso en financiamiento al sector público no financiero**: Se desagrega según el estado de la información en: información en término, fuera de término, incumplimientos reiterados, o determinado por la SEFyC.
> 
> 5. **Incremento por excesos en las participaciones en el capital de empresas (inversiones significativas)**: Este tipo de incremento se informa en el régimen informativo mensual.
> 
> Adicionalmente, se computarán incrementos por: exposición crediticia resultante de posiciones no cubiertas por contratos vendidos para cubrir variaciones de precios de productos básicos, utilización de cupos crediticios ampliados, e incrementos por excesos en límites de participación.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe incluir el incremento por exceso en la relación de activos inmovilizados.
  - Cita textual del TO: «Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe incluir el incremento por exceso en Grandes Exposiciones al Riesgo de Crédito.
  - Cita textual del TO: «Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe incluir el incremento por exceso en graduación del crédito.
  - Cita textual del TO: «Incremento de la exigencia por riesgo de crédito por exceso en graduación del crédito»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe incluir el incremento por exceso en financiamiento al sector público no financiero.
  - Cita textual del TO: «Incremento de la exigencia por riesgo de crédito por exceso en financiamiento al sector público no financiero»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe reflejar la desagregación por estado (en término, fuera de término, incumplimientos reiterados, determinado por la SEFyC).
  - Cita textual del TO: «Incumplimientos reiterados»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 21 — `ADJ-cedaef17`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:5.8

**Pregunta:**

Una procesadora de pagos internacional canaliza ingresos de divisas hacia el país a través de la empresa local que la representa. ¿Bajo qué condiciones puede la entidad receptora confeccionar un boleto global diario por esos ingresos?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA, la entidad receptora (empresa local representante de la procesadora de pagos internacional) puede confeccionar un boleto global diario por los ingresos de divisas bajo las siguientes condiciones:
> 
> 1. **Cumplimiento de condiciones específicas**: Se deben cumplir todas las condiciones indicadas para que ingresen divisas a nombre de la empresa local que actúa como representante en el país de la empresa procesadora de pagos.
> 
> 2. **Recepción exclusiva por infraestructura financiera**: La empresa procesadora de pagos debe recibir los fondos exclusivamente a través de la infraestructura financiera de cuentas en entidades financieras, independientemente del medio de pago utilizado por el cliente pagador local del exterior.
> 
> 3. **Documentación requerida**: La entidad debe contar con la certificación de liquidación emitida por la entidad que cursó el ingreso y liquidación de los fondos a nombre de la procesadora de pagos.
> 
> 4. **Información mínima**: Debe informar respecto de los beneficiarios/ordenantes con nombres y apellidos completos, CUIT, CUIL, CDI y montos.
> 
> 5. **Lista detallada**: Se debe requerir una lista detallada de los beneficiarios u ordenantes de los pagos.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que se requiere una lista detallada de los beneficiarios/ordenantes comprendidos en el boleto.
  - Cita textual del TO: «se deberá requerir una lista detallada de los beneficiarios/ordenantes de los pagos comprendidos en dicho boleto»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar el acuerdo que prevea que los fondos se destinen dentro de los 2 días hábiles al pago de los beneficiarios finales.
  - Cita textual del TO: «los fondos ingresados sean destinados dentro de los 2 (dos) días hábiles al pago en el país de quienes resulten beneficiarios finales»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que las transferencias se canalizan por una entidad del exterior con casa matriz o controlante en un país miembro del Comité de Basilea.
  - Cita textual del TO: «se canalicen a través de una entidad financiera del exterior cuya casa matriz o controlante se encuentre radicada en un país miembro del Comité de Supervisión Bancaria de Basilea»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar los programas de prevención del lavado de activos y financiamiento del terrorismo en el grupo de la procesadora.
  - Cita textual del TO: «apliquen programas basados en estándares internacionales para la prevención del lavado de activos y del financiamiento del terrorismo»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe indicar que por cobros de exportaciones la entidad emite, a pedido del exportador, certificación de ingreso y liquidación de divisas.
  - Cita textual del TO: «la entidad receptora de la transferencia emitirá, a pedido del exportador, una certificación de ingreso y liquidación de divisas por los fondos recibidos en moneda local»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 22 — `ADJ-61cfa2dc`

**TO:** Clasificación de Deudores (`cla`) · **Ancla del gold:** cla:10.3

**Pregunta:**

Una sociedad de garantía recíproca pagó la deuda de una MiPyME en cumplimiento de la garantía que la respaldaba. ¿Qué obligación de clasificación le cabe y con qué criterios?

**Respuesta del sistema (completa):**

> Las sociedades de garantía recíproca (SGR) que paguen la deuda de una MiPyME en cumplimiento de la garantía que la respaldaba tienen la obligación de clasificar a esa MiPyME. La clasificación debe realizarse en función de la mora, según los criterios aplicables para la cartera de consumo o vivienda y por aplicación de las disposiciones previstas en el punto 7.3 de la normativa. Los criterios de clasificación general comprenden cinco categorías: (1) En situación normal, (2) Con seguimiento especial (que incluye: en observación, en negociación o con acuerdos de refinanciación, y en tratamiento especial), (3) Con problemas, (4) Con alto riesgo de insolvencia, e (5) Irrecuperable. La clasificación debe realizarse considerando la totalidad de las financiaciones comprendidas del cliente.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que las SGR y los fondos de garantía públicos inscriptos en los registros del BCRA deben clasificar a esas MiPyMEs.
  - Cita textual del TO: «inscriptos en los Registros habilitados en el BCRA deberán clasificar a las MiPyMEs»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe precisar que se clasifica a las MiPyMEs cuyas deudas fueron canceladas en cumplimiento de las garantías.
  - Cita textual del TO: «cuyas deudas hayan sido canceladas en cumplimiento de las garantías que respaldaban las respectivas obligaciones»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que la clasificación es en función de la mora, con los criterios de la cartera de consumo o vivienda.
  - Cita textual del TO: «La clasificación se realizará en función de la mora, según los criterios aplicables para la cartera de»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar la aplicación de la reclasificación obligatoria.
  - Cita textual del TO: «(reclasificación obligatoria)»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 23 — `ADJ-f6066492`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:3.17

**Pregunta:**

Una petrolera beneficiaria del régimen de acceso a divisas por producción incremental obtuvo la certificación correspondiente. ¿Qué operaciones puede cursar con esa certificación y quién es responsable de emitirla?

**Respuesta del sistema (completa):**

> La certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22) es emitida por una única entidad financiera local nominada por los beneficiarios del régimen. Con esa certificación, la petrolera puede cursar operaciones de giro de divisas por utilidades y dividendos hacia el exterior, por el equivalente al valor de utilidades y dividendos que se abona.

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


## Ficha 24 — `ADJ-4e8501c1`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:5.7

**Pregunta:**

¿Cuándo debe registrar una entidad ante el BCRA sus operaciones de cambio con clientes, y con qué identificación se registra la operación de un turista extranjero o de un fondo común de inversión?

**Respuesta del sistema (completa):**

> Según la normativa del BCRA, una entidad debe registrar sus operaciones de cambio con clientes ante el BCRA en la fecha de su concertación en el mercado de cambios.
> 
> Respecto a la identificación de los clientes en el registro:
> 
> 1. **Turista extranjero**: Se admitirá la utilización del número de pasaporte u otro documento habilitante para el ingreso al país cuando se trate de personas humanas no residentes.
> 
> 2. **Fondo común de inversión**: Se admitirá la utilización del código asignado por la Comisión Nacional de Valores cuando se trate de un fondo común de inversión.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que se registra ante el BCRA toda operación realizada en el mercado de cambios.
  - Cita textual del TO: «La entidad deberá registrar ante el BCRA toda operación que realice en el mercado de cambios»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe indicar que el registro se realiza en la fecha de concertación.
  - Cita textual del TO: «El registro de esas operaciones se deberá realizar en la fecha de su concertación en el mercado de cambios»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe mencionar los identificadores generales (CUIT, CUIL, CDI, CIE o DNI del cliente).
  - Cita textual del TO: «se utilizará CUIT, CUIL, CDI, CIE o DNI del cliente que realiza la operación»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe indicar que para personas humanas no residentes se admite el pasaporte u otro documento habilitante para el ingreso al país.
  - Cita textual del TO: «Número de pasaporte u otro documento habilitante para el ingreso al país cuando se trate de personas humanas no residentes»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe indicar que para un fondo común de inversión se usa el código asignado por la Comisión Nacional de Valores.
  - Cita textual del TO: «Código asignado por la Comisión Nacional de Valores cuando se trate de un fondo común de inversión»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 25 — `ADJ-6b4b8444`

**TO:** Clasificación de Deudores (`cla`) · **Ancla del gold:** cla:4.1

**Pregunta:**

¿Con qué lógica se estructuran los niveles en los que se agrupa a los clientes al clasificarlos como deudores?

**Respuesta del sistema (completa):**

> Los niveles en los que se agrupan los clientes al clasificarlos como deudores se estructuran con una lógica basada en el **riesgo de incobrabilidad** y la **capacidad de pago**. La estructura comprende **cinco categorías principales** para la cartera comercial:
> 
> 1. **En situación normal**: Clientes cuyo análisis de flujo de fondos demuestra que pueden atender adecuadamente todos sus compromisos financieros.
> 
> 2. **Con seguimiento especial**: Incluye tres subcategorías:
>    - En observación: Clientes que pueden atender la totalidad de sus compromisos, pero existen factores de riesgo.
>    - En negociación o con acuerdos de refinanciación: Clientes que ante la imposibilidad de pagar en las condiciones pactadas manifiestan fehacientemente su intención de refinanciar.
>    - En tratamiento especial: Clientes con refinanciaciones otorgadas por primera vez dentro del año calendario.
> 
> 3. **Con problemas**: Clientes con deterioro en su situación financiera.
> 
> 4. **Con alto riesgo de insolvencia**: Clientes con atrasos de más de 180 días hasta un año.
> 
> 5. **Irrecuperable**: Clientes insolventes o en quiebra con nula o escasa posibilidad de recuperación, o con atrasos superiores al año.
> 
> La lógica fundamental que estructura estos niveles es que **en caso de discrepancias entre criterios de clasificación, se debe considerar la pauta que indique el mayor nivel de riesgo de incobrabilidad**. Esto significa que los niveles se organizan en una progresión de riesgo creciente, donde cada categoría representa un grado mayor de deterioro en la capacidad de pago y en la probabilidad de recuperación del crédito.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que los niveles agrupan a los clientes en orden decreciente de calidad.
  - Cita textual del TO: «niveles de agrupamiento de los clientes en orden decreciente de calidad»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe indicar que el orden está en razón directa al riesgo de incobrabilidad derivado de las situaciones que presentan.
  - Cita textual del TO: «en razón directa al riesgo de incobrabilidad que se deriva de las situaciones que presentan»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 26 — `ADJ-182df261`

**TO:** Protección de los Usuarios de Servicios Financieros (`pro`) · **Ancla del gold:** pro:2.1

**Pregunta:**

¿Qué derechos básicos tiene un usuario de servicios financieros en toda relación de consumo, y qué deben hacer los sujetos obligados para garantizarlos?

**Respuesta del sistema (completa):**

> Los derechos básicos que tiene un usuario de servicios financieros en toda relación de consumo son:
> 
> 1. **Protección de su seguridad e intereses económicos**: Los usuarios tienen derecho a la protección de su seguridad e intereses económicos.
> 
> 2. **Información clara, suficiente, veraz y de fácil acceso**: Los usuarios tienen derecho a recibir información clara, suficiente, veraz y de fácil acceso y visibilidad acerca de los productos y/o servicios que contraten, incluyendo sus términos y condiciones, así como copia de los instrumentos que suscriban.
> 
> 3. **Libertad de elección**: Los usuarios tienen derecho a la libertad de elección en toda relación de consumo.
> 
> 4. **Trato equitativo y digno**: Los usuarios tienen derecho a condiciones de trato equitativo y digno.
> 
> Para garantizar estos derechos, los sujetos obligados deben:
> 
> 1. **Adoptar acciones necesarias**: Los sujetos obligados deberán adoptar las acciones necesarias para garantizar derechos de protección de seguridad e intereses económicos, información clara y veraz, libertad de elección, y trato equitativo a todos los actuales y potenciales usuarios.
> 
> 2. **Prevenir discriminación**: Los sujetos obligados deberán adoptar los recaudos necesarios a los efectos de prevenir particularmente los actos u omisiones discriminatorios determinados por motivos tales como raza, religión, nacionalidad, ideología, opinión política o gremial, edad, sexo, posición económica, condición social o caracteres físicos.
> 
> 3. **Prohibir trato discriminatorio**: Las políticas, prácticas y procedimientos de los sujetos obligados no podrán representar un trato discriminatorio de los usuarios.
> 
> 4. **Elaborar manual de procedimiento**: Los sujetos obligados deberán explicitar en un manual de procedimiento los pasos y los recaudos que observarán para la atención de las consultas y reclamos de sus usuarios de servicios financieros.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe incluir la protección de su seguridad e intereses económicos.
  - Cita textual del TO: «la protección de su seguridad e intereses económicos»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe incluir el derecho a recibir información clara, suficiente, veraz y de fácil acceso.
  - Cita textual del TO: «recibir información clara, suficiente, veraz y de fácil acceso y visibilidad»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe incluir la libertad de elección.
  - Cita textual del TO: «la libertad de elección»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe incluir condiciones de trato equitativo y digno.
  - Cita textual del TO: «condiciones de trato equitativo y digno»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe indicar que los sujetos obligados aseguran condiciones igualitarias de acceso a los servicios.
  - Cita textual del TO: «asegurarles condiciones igualitarias de acceso a tales servicios»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 27 — `ADJ-9f188992`

**TO:** Capitales Mínimos de las Entidades Financieras (`cap`) · **Ancla del gold:** cap:5.2.1

**Pregunta:**

Antes de computar una cobertura para reducir la exigencia de capital por riesgo de crédito, ¿qué requisitos generales deben cumplir las técnicas de cobertura utilizadas?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA, antes de computar una cobertura para reducir la exigencia de capital por riesgo de crédito, las técnicas de cobertura utilizadas deben cumplir los requisitos establecidos en la Sección 5 de la normativa. Sin embargo, el grafo disponible no contiene el detalle específico de cuáles son esos requisitos generales. La información encontrada solo indica que existe esta obligación de cumplimiento, pero no especifica los requisitos concretos (tales como validez jurídica, exigibilidad, independencia, documentación, etc.) que deben satisfacer las técnicas de cobertura.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que la documentación de la cobertura observa los requisitos legales vigentes y obliga a todas las partes en todas las jurisdicciones.
  - Cita textual del TO: «La documentación vinculada con la CRC deberá observar los requisitos legales vigentes en la materia»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar que no puede existir correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía.
  - Cita textual del TO: «No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que una exposición con cobertura no puede originar un requerimiento de capital mayor que una idéntica sin cobertura.
  - Cita textual del TO: «originará un requerimiento de capital superior al asignado a otra operación idéntica que no cuente con tales coberturas»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe señalar que con múltiples técnicas sobre una misma exposición se divide la exposición y se calculan los activos ponderados por separado.
  - Cita textual del TO: «deberá dividir la exposición en las partes cubiertas por cada tipo de técnica y calcular por separado los activos ponderados por riesgo»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe advertir que el uso de coberturas puede incrementar riesgos residuales (legal, operacional, de liquidez, de mercado, de concentración y estratégico).
  - Cita textual del TO: «puede incrementar –al mismo tiempo– otros riesgos residuales, tales como el riesgo legal, operacional, de liquidez, de mercado, de concentración y estratégico»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 28 — `ADJ-aa52c12d`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:2.6

**Pregunta:**

Una empresa de software inscripta en el registro de beneficiarios de la economía del conocimiento quiere quedar exceptuada de liquidar los cobros de sus exportaciones. ¿Qué condiciones debe cumplir y cómo funciona la certificación que lo habilita?

**Respuesta del sistema (completa):**

> Una empresa de software inscripta en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento (Decreto 679/22) puede quedar exceptuada de liquidar los cobros de sus exportaciones si cumple las siguientes condiciones:
> 
> **Condiciones principales:**
> 1. Estar inscripta en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y ser beneficiaria del Capítulo II del Decreto 679/22.
> 2. Que los cobros correspondan a exportaciones de bienes y servicios vinculados a actividades de la economía del conocimiento.
> 3. Que los fondos en moneda extranjera sean acreditados en una Cuenta especial para el régimen de fomento de la economía del conocimiento (Decreto 679/22).
> 4. Contar con una Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22) por el equivalente del monto que se pretende no liquidar.
> 5. Presentar una declaración jurada del cliente en la que conste que los cobros que dejan de liquidarse corresponden a exportaciones relacionadas con actividades vinculadas a la economía del conocimiento.
> 
> **Funcionamiento de la certificación:**
> La certificación de incremento de exportaciones es emitida por una entidad nominada (generalmente una entidad financiera) y requiere la verificación de requisitos previos a su emisión. La entidad nominada debe constatar la información suministrada antes de emitir cada certificación. La certificación debe ser emitida conforme a los términos previstos en el punto 2.6.2 de la normativa.

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


## Ficha 29 — `ADJ-f5b6657f`

**TO:** Clasificación de Deudores (`cla`) · **Ancla del gold:** cla:3.5

**Pregunta:**

¿A quién puede encomendar una entidad financiera la tarea de clasificar a sus deudores y qué recaudos exige cada alternativa?

**Respuesta del sistema (completa):**

> Una entidad financiera puede encomendar la tarea de clasificación de deudores a dos alternativas principales:
> 
> 1. **Al sector de créditos de la propia entidad**: Si opta por esta alternativa, la entidad financiera deberá contar con una oficina independiente que tendrá como función efectuar la revisión de las clasificaciones asignadas a los clientes por el sector de créditos.
> 
> 2. **A la auditoría interna de la entidad**: La revisión de clasificaciones puede estar a cargo de la auditoría interna de la entidad, debiendo comprender obligatoriamente a los clientes cuyo endeudamiento total en pesos y en moneda extranjera supere el 1% de la responsabilidad patrimonial computable de la entidad del mes anterior al de la clasificación o el equivalente al importe de referencia establecido en el punto 3.7 (de ambos el menor), y alcanzar como mínimo el 20% de la cartera activa total.
> 
> **Recaudos generales**: Independientemente de la alternativa elegida, la intervención de terceros no releva a la entidad de su responsabilidad por la clasificación finalmente asignada ni de la obligación de conservar los legajos con la información requerida. Además, cuando un tercero desarrolle tareas relativas a servicios ofrecidos por los sujetos obligados o en su nombre, ambos serán responsables por el cumplimiento de las normas aplicables, lo que deberá establecerse en los instrumentos que acuerden la realización de dichas tareas.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe mencionar la opción de un área independiente del sector de otorgamiento de créditos y garantías.
  - Cita textual del TO: «A un área independiente del sector encargado del otorgamiento de créditos y garantías»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe indicar que si clasifica el propio sector de créditos, una oficina independiente revisa las clasificaciones asignadas.
  - Cita textual del TO: «que tendrá como función efectuar la revisión de las clasificaciones asignadas a los clientes por el sector de créditos»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que la revisión debe estar concluida antes de la presentación del Estado de situación de deudores.
  - Cita textual del TO: «La revisión deberá estar concluida antes de presentarse a la Superintendencia»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar la opción de profesionales externos, sin que ello releve a la entidad de su responsabilidad.
  - Cita textual del TO: «no releva a la entidad de su responsabilidad»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 30 — `ADJ-cd8b15da`

**TO:** Capitales Mínimos de las Entidades Financieras (`cap`) · **Ancla del gold:** cap:8.3.2

**Pregunta:**

¿Qué requisitos deben cumplir los instrumentos de deuda para computar como capital adicional de nivel uno de una entidad financiera?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA, los instrumentos de deuda que computen como capital adicional de nivel uno deben cumplir con requisitos específicos establecidos en el punto 8.3.2 del Texto Ordenado de Capitales Mínimos. Sin embargo, el Knowledge Graph disponible no contiene el detalle completo de estos requisitos. Se encontró que existe una obligación de que 'los instrumentos incluidos en el CA deberán observar los siguientes requisitos', pero los requisitos específicos no están desarrollados en los nodos accesibles. La regulación también hace referencia a que los instrumentos deben ser subordinados y cumplir con características particulares para ser considerados como capital adicional, pero los detalles concretos de estas características no están disponibles en la información consultada.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que deben estar totalmente suscriptos e integrados.
  - Cita textual del TO: «Estar totalmente suscriptos e integrados»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar la subordinación a depositantes, acreedores quirografarios y deuda subordinada.
  - Cita textual del TO: «Estar subordinados a depositantes, acreedores quirografarios y a deuda subordinada de la entidad financiera»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que no pueden estar asegurados ni cubiertos por garantías del emisor o de un vinculado.
  - Cita textual del TO: «No estar asegurados ni cubiertos por alguna garantía del emisor o de un vinculado»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar que el rescate es posible recién a los cinco años de la emisión y con condiciones (autorización previa de la SEFyC entre ellas).
  - Cita textual del TO: «La entidad financiera podrá rescatarlos –transcurridos un mínimo de cinco años desde su emisión–»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe indicar la discrecionalidad para cancelar pagos de dividendos o intereses en todo momento.
  - Cita textual del TO: «cancelar pagos en concepto de dividendos o intereses»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 31 — `ADJ-15450b19`

**TO:** Clasificación de Deudores (`cla`) · **Ancla del gold:** cla:4.1

**Pregunta:**

¿Con qué lógica se estructuran los niveles en los que se agrupa a los clientes al clasificarlos como deudores?

**Respuesta del sistema (completa):**

> El Knowledge Graph contiene información sobre la clasificación de deudores en el Punto 4.1 del documento TO_clasificacion_deudores_actual.pdf, donde se establece el 'Agrupamiento de clientes por niveles de clasificación' basado en niveles de riesgo de incobrabilidad. Se identificaron varias categorías de clasificación (situación normal, riesgo alto, irrecuperable) con criterios específicos como atrasos máximos de 31 días para situación normal, atrasos hasta 90 días para otras categorías, y atrasos superiores a 180 días para irrecuperable. Sin embargo, la información disponible en el grafo no proporciona una explicación completa y explícita de la lógica estructural que organiza jerárquicamente todos los niveles de agrupamiento.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que los niveles agrupan a los clientes en orden decreciente de calidad.
  - Cita textual del TO: «niveles de agrupamiento de los clientes en orden decreciente de calidad»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe indicar que el orden está en razón directa al riesgo de incobrabilidad derivado de las situaciones que presentan.
  - Cita textual del TO: «en razón directa al riesgo de incobrabilidad que se deriva de las situaciones que presentan»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 32 — `ADJ-ad64454a`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:3.17

**Pregunta:**

Una petrolera beneficiaria del régimen de acceso a divisas por producción incremental obtuvo la certificación correspondiente. ¿Qué operaciones puede cursar con esa certificación y quién es responsable de emitirla?

**Respuesta del sistema (completa):**

> Con la Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22), la petrolera beneficiaria puede: (1) acceder al mercado de cambios para realizar operaciones de compra/venta de divisas, y (2) girar divisas por el equivalente al valor de utilidades y dividendos. La certificación es emitida por una única entidad financiera local que debe ser nominada por los beneficiarios del régimen (RADPIP y/o RADPIGN), siendo esta entidad la responsable de emitir las certificaciones y remitirlas a las entidades por las cuales el cliente desee acceder al mercado de cambios.

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


## Ficha 33 — `ADJ-f659fc57`

**TO:** Capitales Mínimos de las Entidades Financieras (`cap`) · **Ancla del gold:** cap:6.5

**Pregunta:**

¿Cómo se mide la exposición para la exigencia de capital por riesgo de posiciones en commodities y qué compensaciones entre posiciones se admiten?

**Respuesta del sistema (completa):**

> La exposición para la exigencia de capital por riesgo de posiciones en commodities se mide utilizando un modelo de un único factor dentro de cada conjunto de cobertura, que divide el riesgo correspondiente a un mismo tipo de commodity en sus componentes sistemático e idiosincrásico. Para derivados sobre commodities, la exposición se calcula aplicando factores regulatorios específicos al nocional efectivo.
> 
> Respecto a las compensaciones entre posiciones admitidas:
> 
> 1. **Compensación permitida dentro del mismo commodity**: La compensación o cobertura total están permitidas entre todas las operaciones de derivados que hagan referencia al mismo tipo de commodity.
> 
> 2. **Prohibición de compensación entre conjuntos de cobertura**: No se permitirá la compensación o cobertura entre conjuntos de cobertura distintos, tales como energía, metales y productos agrícolas. Estos constituyen conjuntos separados sin posibilidad de compensación cruzada.
> 
> 3. **Factores de escala especiales**: Cuando se aplique a conjuntos de cobertura de derivados sobre bases, el factor de escala correspondiente se multiplicará por 0,5. Cuando se aplique a operaciones sobre volatilidad, el factor se multiplicará por 5.
> 
> En síntesis, la regulación permite compensación plena entre posiciones del mismo commodity, pero prohíbe cualquier compensación entre los tres conjuntos de cobertura principales (energía, metales y productos agrícolas).

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


## Ficha 34 — `ADJ-0afe0c36`

**TO:** Capitales Mínimos de las Entidades Financieras (`cap`) · **Ancla del gold:** cap:6.5

**Pregunta:**

¿Cómo se mide la exposición para la exigencia de capital por riesgo de posiciones en commodities y qué compensaciones entre posiciones se admiten?

**Respuesta del sistema (completa):**

> La exposición para la exigencia de capital por riesgo de posiciones en commodities se mide mediante el cálculo de la posición abierta neta en cada commodity. La metodología incluye: (1) Cálculo de posiciones netas: se incluye la posición comprada neta (posición comprada bruta menos la posición vendida en la misma exposición subyacente, cuando ésta tenga la misma duración o vida residual de al menos un año). (2) Posición bruta: se calcula como la suma de posiciones largas más posiciones cortas en cada producto básico. (3) Capital adicional: las entidades financieras deben observar un requerimiento de capital adicional del 3% de la posición bruta (largas más cortas) en cada producto básico por riesgos de base, de tasa de interés y de brecha a futuro.
> 
> Respecto a las compensaciones entre posiciones, la regulación establece limitaciones significativas: (1) No se admite compensación entre posiciones en diferentes productos básicos ni entre subcategorías diferentes del mismo producto básico. (2) Se permite compensación de posiciones compradas y vendidas dentro de cada banda temporal para el mismo subyacente. (3) La exigencia de capital por riesgo de tipo de cambio y commodities se aplica a la posición total en cada moneda extranjera y commodity de forma individual.

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


## Ficha 35 — `ADJ-f96ca183`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:2.6

**Pregunta:**

Una empresa de software inscripta en el registro de beneficiarios de la economía del conocimiento quiere quedar exceptuada de liquidar los cobros de sus exportaciones. ¿Qué condiciones debe cumplir y cómo funciona la certificación que lo habilita?

**Respuesta del sistema (completa):**

> Una empresa de software inscripta en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento puede quedar exceptuada de liquidar los cobros de sus exportaciones si cumple la totalidad de las siguientes condiciones:
> 
> 1. **Inscripción y beneficiario**: Debe estar inscripta en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y ser beneficiaria de lo dispuesto en el Capítulo II del Decreto 679/22.
> 
> 2. **Tipo de exportaciones**: Los cobros deben corresponder a exportaciones de bienes y servicios que correspondan a actividades de la economía del conocimiento.
> 
> 3. **Ingreso por mercado de cambios**: Los cobros deben haber ingresado por el mercado de cambios en los plazos establecidos en cada caso.
> 
> 4. **Certificación requerida**: El cliente debe contar por el equivalente del monto que se pretende no liquidar con una "Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22)" emitida en los términos previstos en el punto 2.6.2.
> 
> **Funcionamiento de la certificación**: La certificación de incremento de exportaciones es el instrumento que habilita la excepción. Debe ser emitida conforme a lo establecido en el punto 2.6.2 del Texto Ordenado de Exterior y Cambios, y su monto debe ser equivalente al de los cobros que se pretende no liquidar. Esta certificación es requisito previo para acceder a la excepción de liquidación.

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


## Ficha 36 — `ADJ-bebfbbf4`

**TO:** Régimen Informativo Contable Mensual (`ric`) · **Ancla del gold:** ric:4.2

**Pregunta:**

¿Qué exigencias componen el modelo de información de riesgo de mercado del régimen informativo mensual y con qué apertura se informa el riesgo de tasa?

**Respuesta del sistema (completa):**

> Según el régimen informativo mensual del BCRA, el modelo de información de riesgo de mercado se compone de exigencias por: (1) riesgo general de tasa de interés, (2) riesgo específico de tasa de interés, (3) riesgo general de acciones, (4) riesgo específico de acciones, (5) riesgo general de acciones adicional por derivados, y (6) riesgo de moneda y commodities. Respecto al riesgo de tasa de interés, la información se informa con apertura por moneda y banda de plazo, con ponderadores de riesgo aplicables. Las entidades deben informar posiciones compradas y vendidas clasificadas por moneda y banda de plazo en forma mensual.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe incluir la exigencia por riesgo de tasa con apertura total/específico/general.
  - Cita textual del TO: «Exigencia por riesgo de tasa - Específico»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe incluir la exigencia por riesgo de acciones, con el adicional por derivados.
  - Cita textual del TO: «Exigencia por riesgo de acciones - Adicional por derivados»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe incluir la exigencia por riesgo de tipo de cambio.
  - Cita textual del TO: «Exigencia por riesgo de tipo de cambio»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe incluir la exigencia por riesgo de posiciones en opciones.
  - Cita textual del TO: «Exigencia por riesgo de posiciones en opciones»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe incluir la exigencia por riesgo de posiciones en productos básicos (commodities).
  - Cita textual del TO: «Exigencia por riesgo de posiciones en productos básicos – commodities -»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 37 — `ADJ-ac03b407`

**TO:** Capitales Mínimos de las Entidades Financieras (`cap`) · **Ancla del gold:** cap:5.2.1

**Pregunta:**

Antes de computar una cobertura para reducir la exigencia de capital por riesgo de crédito, ¿qué requisitos generales deben cumplir las técnicas de cobertura utilizadas?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA, antes de computar una cobertura para reducir la exigencia de capital por riesgo de crédito, las técnicas de cobertura utilizadas deben cumplir con los requisitos establecidos en la Sección 5 de la normativa. Entre los requisitos específicos identificados se encuentran: (1) que la cobertura del riesgo de crédito tenga un plazo de vencimiento original de al menos un año y un plazo residual superior a tres meses; (2) que las entidades financieras ajusten los valores de la exposición y del activo recibido en garantía para tener en cuenta posibles futuras variaciones; y (3) que la documentación vinculada con la cobertura observe los requisitos legales vigentes. Sin embargo, la regulación remite a la Sección 5 para el detalle completo de los requisitos generales aplicables.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que la documentación de la cobertura observa los requisitos legales vigentes y obliga a todas las partes en todas las jurisdicciones.
  - Cita textual del TO: «La documentación vinculada con la CRC deberá observar los requisitos legales vigentes en la materia»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar que no puede existir correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía.
  - Cita textual del TO: «No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que una exposición con cobertura no puede originar un requerimiento de capital mayor que una idéntica sin cobertura.
  - Cita textual del TO: «originará un requerimiento de capital superior al asignado a otra operación idéntica que no cuente con tales coberturas»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe señalar que con múltiples técnicas sobre una misma exposición se divide la exposición y se calculan los activos ponderados por separado.
  - Cita textual del TO: «deberá dividir la exposición en las partes cubiertas por cada tipo de técnica y calcular por separado los activos ponderados por riesgo»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe advertir que el uso de coberturas puede incrementar riesgos residuales (legal, operacional, de liquidez, de mercado, de concentración y estratégico).
  - Cita textual del TO: «puede incrementar –al mismo tiempo– otros riesgos residuales, tales como el riesgo legal, operacional, de liquidez, de mercado, de concentración y estratégico»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 38 — `ADJ-8e4f2450`

**TO:** Capitales Mínimos de las Entidades Financieras (`cap`) · **Ancla del gold:** cap:4.2

**Pregunta:**

Para las operaciones con derivados OTC de un banco, ¿cómo se determina la exposición al riesgo de crédito de contraparte bajo el enfoque estándar y qué papel juegan los márgenes de variación?

**Respuesta del sistema (completa):**

> Bajo el enfoque estándar (SA-CCR) para derivados OTC, la exposición al riesgo de crédito de contraparte se determina de manera diferenciada según exista o no intercambio de márgenes de variación:
> 
> **Para operaciones SIN márgenes de variación:**
> El crédito de riesgo (CR) se calcula como: CR = V - C, donde V es el valor actual de mercado de las operaciones con derivados y C es el valor neto de activos en garantía con aforos. La exposición presente respecto de la contraparte no puede tener un valor negativo.
> 
> **Para operaciones CON márgenes de variación:**
> El CR se define como la mayor exposición que no alcanza a activar un aumento del margen de variación, determinada por la expresión: CR = máx. (V - C; TH + MTA - NICA; 0), donde estos componentes representan el mayor valor entre la exposición actual y el umbral de margen inicial menos el importe neto en cuenta de compensación.
> 
> **Papel de los márgenes de variación:**
> Los márgenes de variación juegan un papel crucial en la mitigación del riesgo de crédito. La EAD (Exposure at Default) para un conjunto de neteo con márgenes de variación tiene como límite superior la EAD que resultaría para el mismo conjunto si no los tuviera, lo que refleja que los márgenes reducen pero no eliminan la exposición.
> 
> La exigencia final de capital por riesgo de crédito de contraparte (RCD) surge de la sumatoria de las exposiciones al riesgo de crédito de contraparte determinadas para cada conjunto de neteo, conforme al enfoque estandarizado establecido en las normas sobre Capitales Mínimos.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que la EAD se calcula por separado para cada conjunto de neteo.
  - Cita textual del TO: «La exposición al riesgo de crédito de contraparte (EAD) se calculará por separado para cada conjunto de neteo»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar el factor alfa igual a 1,40.
  - Cita textual del TO: «α = 1,40»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe explicar que el cálculo del costo de reposición y de la exposición potencial futura difiere según haya o no intercambio de márgenes de variación.
  - Cita textual del TO: «El cálculo del CR y de la EPF diferirá según que los conjuntos de neteo estén sujetos o no al intercambio de márgenes de variación»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe indicar el límite superior: la EAD con márgenes de variación no supera la EAD del mismo conjunto sin ellos.
  - Cita textual del TO: «La EAD para un conjunto de neteo con márgenes de variación tendrá como límite superior la EAD que resultaría para el mismo conjunto si no los tuviera»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 39 — `ADJ-88b1d0af`

**TO:** Régimen Informativo Contable Mensual (`ric`) · **Ancla del gold:** ric:4.2

**Pregunta:**

¿Qué exigencias componen el modelo de información de riesgo de mercado del régimen informativo mensual y con qué apertura se informa el riesgo de tasa?

**Respuesta del sistema (completa):**

> No se encontró en el Knowledge Graph una descripción completa de todas las exigencias que componen el modelo de información de riesgo de mercado del régimen informativo mensual, ni detalles específicos sobre la apertura con la que se informa el riesgo de tasa. Se identificó que existe un modelo de presentación de exigencia por riesgo de mercado en el Punto 4.2 del régimen, que incluye componentes por riesgo de tasa, riesgo de cambio y riesgo en acciones, pero la información disponible no permite especificar completamente cuáles son todas las exigencias ni la apertura exacta del riesgo de tasa.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe incluir la exigencia por riesgo de tasa con apertura total/específico/general.
  - Cita textual del TO: «Exigencia por riesgo de tasa - Específico»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe incluir la exigencia por riesgo de acciones, con el adicional por derivados.
  - Cita textual del TO: «Exigencia por riesgo de acciones - Adicional por derivados»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe incluir la exigencia por riesgo de tipo de cambio.
  - Cita textual del TO: «Exigencia por riesgo de tipo de cambio»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe incluir la exigencia por riesgo de posiciones en opciones.
  - Cita textual del TO: «Exigencia por riesgo de posiciones en opciones»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe incluir la exigencia por riesgo de posiciones en productos básicos (commodities).
  - Cita textual del TO: «Exigencia por riesgo de posiciones en productos básicos – commodities -»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 40 — `ADJ-202e66d6`

**TO:** Clasificación de Deudores (`cla`) · **Ancla del gold:** cla:3.1

**Pregunta:**

¿Qué deben asegurar los procedimientos de análisis de cartera que desarrolle una entidad financiera para clasificar a sus deudores?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA, los procedimientos de análisis de cartera que desarrolle una entidad financiera para clasificar a sus deudores deben asegurar dos aspectos fundamentales: (1) un análisis adecuado de la situación económica y financiera del deudor, y (2) una revisión periódica de su situación en cuanto a las condiciones objetivas y subjetivas de todos los riesgos asumidos.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe mencionar un análisis adecuado de la situación económica y financiera del deudor.
  - Cita textual del TO: «la situación económica y financiera del deudor»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar la revisión periódica de las condiciones objetivas y subjetivas de todos los riesgos asumidos.
  - Cita textual del TO: «una revisión periódica de su situación en cuanto a las condiciones objetivas y subjetivas de todos los riesgos asumidos»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 41 — `ADJ-db1cacfa`

**TO:** Régimen Informativo Contable Mensual (`ric`) · **Ancla del gold:** ric:12.4

**Pregunta:**

Desde el período de información de abril de 2024, ¿qué cambió en el envío de información consolidada con código de consolidación 3 y qué tratamiento particular recibe el ratio de apalancamiento?

**Respuesta del sistema (completa):**

> Desde el período de información de abril de 2024, se suspendió el envío de informaciones con código de consolidación 3, siendo marzo de 2024 el último período trimestral que corresponde informar con este nivel de consolidación. Sin embargo, el Ratio de apalancamiento recibe un tratamiento particular: se continuará informando con código de consolidación 3 de forma trimestral, pero con una especificidad importante: las operaciones a incluir serán las que correspondan al perímetro de consolidación mensual, considerando de corresponder, los sujetos previstos en el punto 6.2.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar la suspensión del envío de informaciones con código de consolidación 3.
  - Cita textual del TO: «Se suspende el envío de informaciones con código de consolidación 3»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar la excepción prevista para el ratio de apalancamiento.
  - Cita textual del TO: «con la excepción prevista para Ratio de apalancamiento»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que marzo/24 fue el último período trimestral informado con ese nivel de consolidación.
  - Cita textual del TO: «siendo marzo/24 el último período trimestral que corresponde informar con este nivel de consolidación»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe indicar que el ratio de apalancamiento mantiene su frecuencia trimestral.
  - Cita textual del TO: «mantendrá su frecuencia trimestral (datos del mes de cierre de trimestre)»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 42 — `ADJ-b61bd355`

**TO:** Protección de los Usuarios de Servicios Financieros (`pro`) · **Ancla del gold:** pro:2.5

**Pregunta:**

Un banco quiere subir una comisión, crear otra para un producto nuevo y reducir una tercera. ¿Qué debe informar al BCRA en cada caso y en qué momento?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA, un banco debe informar al BCRA sobre cambios en comisiones de la siguiente manera:
> 
> 1. **AUMENTO DE COMISIÓN**: Debe informar **previamente** al BCRA antes de implementar el aumento. La información debe ser comunicada por la vía consignada en la normativa (conforme al régimen informativo establecido).
> 
> 2. **NUEVA COMISIÓN (producto nuevo)**: Debe informar **previamente** al BCRA antes de comercializar el nuevo producto o servicio. Al igual que los aumentos, la comunicación debe realizarse por la vía establecida en el régimen informativo.
> 
> 3. **REDUCCIÓN DE COMISIÓN**: Debe informar al BCRA **dentro de los treinta (30) días corridos siguientes de su aplicación**. A diferencia de los dos casos anteriores, esta comunicación es posterior a la implementación del cambio.
> 
> En todos los casos, la información debe incluir las comisiones y cargos que se cobren a los usuarios de servicios financieros, conforme al régimen informativo establecido por el BCRA. Estas obligaciones aplican a entidades financieras, PSPCP, empresas no financieras emisoras de tarjetas de crédito y/o compra, y otros proveedores no financieros de crédito.

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


## Ficha 43 — `ADJ-cbff1958`

**TO:** Clasificación de Deudores (`cla`) · **Ancla del gold:** cla:4.1

**Pregunta:**

¿Con qué lógica se estructuran los niveles en los que se agrupa a los clientes al clasificarlos como deudores?

**Respuesta del sistema (completa):**

> Los niveles en los que se agrupan los clientes al clasificarlos como deudores se estructuran con una lógica basada en el **análisis de la capacidad de pago y el flujo de fondos del cliente**. La regulación del BCRA establece cinco categorías que forman una escala progresiva de riesgo:
> 
> 1. **En situación normal**: El análisis del flujo de fondos demuestra que el cliente es capaz de atender adecuadamente todos sus compromisos financieros.
> 
> 2. **Con seguimiento especial**: Comprende tres subcategorías:
>    - En observación: El flujo de fondos muestra que puede atender sus compromisos, pero existen factores de riesgo que requieren monitoreo.
>    - En negociación o con acuerdos de refinanciación: Clientes que ante la imposibilidad de pagar en las condiciones pactadas, manifiestan fehacientemente su intención de renegociar.
>    - En tratamiento especial: Refinanciaciones otorgadas por primera vez dentro del año calendario.
> 
> 3. **Con problemas**: El análisis del flujo de fondos demuestra que el cliente tiene problemas para atender normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos, pueden resultar en una pérdida para la entidad.
> 
> 4. **Con alto riesgo de insolvencia**: El análisis del flujo de fondos demuestra que es altamente improbable que el cliente pueda atender la totalidad de sus compromisos financieros.
> 
> 5. **Irrecuperable**: Las deudas se consideran incobrables, aunque podrían tener algún valor de recuperación bajo circunstancias futuras.
> 
> La lógica subyacente es una **evaluación progresiva de la capacidad de pago**, donde cada nivel refleja un grado creciente de deterioro en la capacidad del deudor para cumplir con sus obligaciones financieras.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar que los niveles agrupan a los clientes en orden decreciente de calidad.
  - Cita textual del TO: «niveles de agrupamiento de los clientes en orden decreciente de calidad»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe indicar que el orden está en razón directa al riesgo de incobrabilidad derivado de las situaciones que presentan.
  - Cita textual del TO: «en razón directa al riesgo de incobrabilidad que se deriva de las situaciones que presentan»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 44 — `ADJ-3e268220`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:4.6.1

**Pregunta:**

Una empresa local tiene dividendos aprobados por asamblea que siguen pendientes de pago a su accionista del exterior y evalúa suscribir bonos BOPREAL por esa deuda. ¿Qué debe verificar la entidad que concreta la suscripción y con qué tope?

**Respuesta del sistema (completa):**

> La entidad que concreta la suscripción debe verificar: (1) Documentación de deuda pendiente: que la deuda corresponde a utilidades y dividendos de balances cerrados y auditados; (2) Declaración jurada del acreedor: que los dividendos están pendientes de pago, que no ha utilizado ya este mecanismo por esta deuda, y que toma conocimiento de restricciones de acceso al mercado de cambios; (3) Verificación de origen de fondos: que el monto percibido tiene origen en el cobro en el país desde el 01/09/19 de utilidades y dividendos por balances cerrados y auditados. El tope de suscripción es el equivalente al monto en moneda local de las utilidades y dividendos cobrados a partir del 01/09/19 según la distribución determinada por la asamblea de accionistas, ajustado por el último Índice de Precios al Consumidor (IPC) disponible a la fecha de suscripción.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar el tope: hasta el equivalente en moneda local de las utilidades y dividendos pendientes de pago según la distribución de la asamblea.
  - Cita textual del TO: «por hasta el equivalente al monto en moneda local de las utilidades y dividendos pendientes de pago a accionistas no residentes a partir de la distribución determinada por la asamblea de accionistas»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar la documentación que avale que la deuda corresponde a utilidades y dividendos de balances cerrados y auditados.
  - Cita textual del TO: «la deuda pendiente corresponde a utilidades y dividendos de balances cerrados y auditados»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe incluir la declaración de la operación en el Relevamiento de activos y pasivos externos, de corresponder.
  - Cita textual del TO: «La operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar la declaración jurada del cliente de que no utilizó ya este mecanismo por esa deuda.
  - Cita textual del TO: «no ha utilizado ya este mecanismo por esta deuda»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe indicar el boleto de venta de cambio por el concepto de registro de utilidades y dividendos por adjudicación de bonos BOPREAL.
  - Cita textual del TO: «I09. Registro de utilidades y dividendos por adjudicación de bonos BOPREAL»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 45 — `ADJ-764fb304`

**TO:** Capitales Mínimos de las Entidades Financieras (`cap`) · **Ancla del gold:** cap:8.6

**Pregunta:**

Una entidad financiera planea un aumento de capital. ¿En qué forma deben efectuarse los aportes, qué excepciones se admiten y cómo se computan hasta su aprobación?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA, los aportes de capital en una entidad financiera deben efectuarse de la siguiente forma:
> 
> **Forma de efectuar los aportes:**
> Los aportes de capital deben ser efectuados en efectivo.
> 
> **Excepciones admitidas:**
> Excepcionalmente, mediando autorización previa de la SEFyC (Superintendencia de Entidades Financieras y Cambios), podrán admitirse aportes en:
> - Títulos valores públicos nacionales
> - Instrumentos de regulación monetaria del BCRA
> - Depósitos y otras obligaciones por intermediación financiera de la entidad
> 
> Asimismo, se admiten aportes en especie (bienes de capital), siempre que se demuestre el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte que será computado como ingresado y liquidado en el mercado de cambios.
> 
> **Cómputo hasta su aprobación:**
> Hasta tanto se le haya notificado la aprobación de los aportes, estos se deducirán del respectivo componente de la RPC (Relación de Patrimonio Computable). Esto significa que los aportes no aprobados no se computan como capital hasta que se reciba la notificación formal de su aprobación.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe indicar la regla general: los aportes deben ser efectuados en efectivo.
  - Cita textual del TO: «los aportes deben ser efectuados en efectivo»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe mencionar que excepcionalmente, con autorización previa de la SEFyC, se admiten otros aportes.
  - Cita textual del TO: «Excepcionalmente, mediando autorización previa de la SEFyC, podrán admitirse aportes en»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe incluir entre las excepciones los títulos valores públicos nacionales.
  - Cita textual del TO: «títulos valores públicos nacionales»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe indicar que esos aportes se registran a su valor de mercado.
  - Cita textual del TO: «los aportes deberán registrarse a su valor de mercado»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C5.** Debe señalar que hasta la notificación de la aprobación los aportes contabilizados se deducen del componente de la RPC.
  - Cita textual del TO: «Hasta tanto se le haya notificado la aprobación de los aportes y en la medida en que éstos hayan sido contabilizados, se deducirán del respectivo componente de la RPC»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---


## Ficha 46 — `ADJ-26ff7058`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:13.5

**Pregunta:**

Un banco emitió una carta de crédito para garantizar una importación de servicios y ahora debe afrontar el pago. ¿Qué condiciones tiene que verificar para su propio acceso al mercado de cambios?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA, cuando un banco debe afrontar el pago de una carta de crédito emitida para garantizar una importación de servicios, debe verificar que se cumplen las condiciones previstas en el punto 10.3.2.1. para el acceso al mercado de cambios, con excepción de aquella prevista en el inciso viii). Sin embargo, el Knowledge Graph no contiene el detalle específico de cuáles son esas condiciones individuales del punto 10.3.2.1. que debe verificar el banco para su propio acceso al mercado de cambios en esta situación.

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


## Ficha 47 — `ADJ-169b5314`

**TO:** Exterior y Cambios (`ext`) · **Ancla del gold:** ext:3.17

**Pregunta:**

Una petrolera beneficiaria del régimen de acceso a divisas por producción incremental obtuvo la certificación correspondiente. ¿Qué operaciones puede cursar con esa certificación y quién es responsable de emitirla?

**Respuesta del sistema (completa):**

> La certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22) es emitida por una única entidad financiera local nominada por los beneficiarios del régimen. Con esta certificación, la petrolera beneficiaria puede cursar: (1) acceso al mercado de cambios, y (2) giro de divisas por el equivalente al valor de utilidades y dividendos que se abona.

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


## Ficha 48 — `ADJ-40616ec6`

**TO:** Clasificación de Deudores (`cla`) · **Ancla del gold:** cla:3.5

**Pregunta:**

¿A quién puede encomendar una entidad financiera la tarea de clasificar a sus deudores y qué recaudos exige cada alternativa?

**Respuesta del sistema (completa):**

> Según la regulación del BCRA sobre clasificación de deudores, una entidad financiera puede encomendar la tarea de clasificación de deudores a terceros. Los recaudos exigidos para cada alternativa son: 1) La intervención de terceros en la clasificación debe estar prevista en el Manual de procedimientos de clasificación y previsión de la entidad. 2) La intervención de terceros no releva a la entidad de su responsabilidad por la clasificación finalmente asignada, es decir, la entidad financiera mantiene la responsabilidad integral sobre la clasificación que se asigne, independientemente de si ha encargado la tarea a un tercero. El grafo no especifica quiénes pueden ser esos terceros (por ejemplo, si pueden ser centrales de riesgos, calificadoras u otras entidades) ni detalla requisitos específicos adicionales para cada tipo de tercero.

**Criterios del gold (marcar cumplido / no_cumplido):**

- **C1.** Debe mencionar la opción de un área independiente del sector de otorgamiento de créditos y garantías.
  - Cita textual del TO: «A un área independiente del sector encargado del otorgamiento de créditos y garantías»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C2.** Debe indicar que si clasifica el propio sector de créditos, una oficina independiente revisa las clasificaciones asignadas.
  - Cita textual del TO: «que tendrá como función efectuar la revisión de las clasificaciones asignadas a los clientes por el sector de créditos»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C3.** Debe indicar que la revisión debe estar concluida antes de la presentación del Estado de situación de deudores.
  - Cita textual del TO: «La revisión deberá estar concluida antes de presentarse a la Superintendencia»
  - Marca: `____________`  (cumplido / no_cumplido)
- **C4.** Debe mencionar la opción de profesionales externos, sin que ello releve a la entidad de su responsabilidad.
  - Cita textual del TO: «no releva a la entidad de su responsabilidad»
  - Marca: `____________`  (cumplido / no_cumplido)

**Observaciones (opcional):** ______________________________________

---
