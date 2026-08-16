# Reporte de desacuerdos y adjudicaciones — calibración juez EV2 v1 sobre U6

Prompt sha256: `fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455`
Orden: semilla `juez-calibracion-v1`, N=3

## Resumen

- Preguntas: 25 — acuerdo 12 · desacuerdo 8 · requiere_adjudicacion 5
- Acuerdo sobre las decididas: 12/20
- Matriz (humano → juez): correcto→correcto: 1, correcto→incorrecto: 1, correcto→parcial: 4, correcto→requiere_adjudicacion: 1, incorrecto→incorrecto: 2, incorrecto→requiere_adjudicacion: 1, parcial→correcto: 2, parcial→incorrecto: 1, parcial→parcial: 9, parcial→requiere_adjudicacion: 3
- Proxy por criterio: correcta→todos cumplido 9/21; incorrecta→ninguno cumplido 12/13
- No-determinismo: pares unánimes 86/92; modales {'no_cumplido': 54, 'cumplido': 32, 'dudoso': 5, 'sin_consenso': 1}; todos los veredictos {'no_cumplido': 164, 'cumplido': 97, 'dudoso': 15}
- Clasificación auxiliar modal vs flag respondible: U6-021:contenido/flag=False; U6-012:abstencion/flag=False

---

# A. Desacuerdos (juez decidió distinto del humano)

## U6-021 — humano: **correcto** · juez (mapping): **parcial** [DESACUERDO]

**Pregunta:** Al informar la exigencia por riesgo de mercado, ¿con los valores de qué fecha se determina el total, y cómo debe identificarse por moneda la partida de exigencia por riesgo general de tasa de interés?

**Respuesta del agente (íntegra):**

> Según la regulación del BCRA, la exigencia por riesgo de mercado se determina con los valores que se registren al último día del período de información (n). Específicamente, la obligación establece que 'La exigencia por riesgo de mercado se determinará con los valores que se registren al último día del período de información (n), calculada como suma de códigos específicos (311000/xx + 312000/xx + 313000/xx + 315000/xx + 314000/xx)'. Respecto a cómo debe identificarse por moneda la partida de exigencia por riesgo general de tasa de interés, la información disponible en el grafo indica que 'Se consignará el valor de la exigencia por riesgo general de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del punto 6.2.2. de las normas sobre Capitales mínimos de las entidades financieras', pero no especifica explícitamente en el grafo cómo debe identificarse por moneda esta partida.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: False

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La exigencia por riesgo de mercado se determina con los valores registrados al último día del período de información (n).
- cita del gold: «4.1.1.1. La exigencia por riesgo de mercado se determinará con los valores que se registren al último día del período de información (n), y el total surgirá de la siguiente suma:»
- rep 1 [cumplido] fragmento: «la exigencia por riesgo de mercado se determina con los valores que se registren al último día del período de información (n)» — La respuesta reproduce fielmente el contenido normativo del criterio, indicando que la exigencia se determina con los valores del último día del período de información (n).
- rep 2 [cumplido] fragmento: «la exigencia por riesgo de mercado se determina con los valores que se registren al último día del período de información (n)» — La respuesta reproduce fielmente el contenido normativo del criterio, indicando que la exigencia se determina con los valores del último día del período de información (n).
- rep 3 [cumplido] fragmento: «la exigencia por riesgo de mercado se determina con los valores que se registren al último día del período de información (n)» — La respuesta reproduce fielmente el contenido normativo del criterio, indicando que la exigencia se determina con los valores del último día del período de información (n).
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La exigencia por riesgo general de tasa de interés (código 311200/xx) se determina por cada moneda, y la partida se identifica según su moneda de origen con la codificación de la tabla T0003 del SISCEN, excluidas las monedas no referenciadas con código SWIFT.
- cita del gold: «La determinación de esta exigencia se efectuará por cada moneda, a cuyos efectos la presente partida se identificará según su moneda de origen de acuerdo con la codificación prevista en el Sistema Centralizado de requerimientos informativos (SISCEN), tabla T0003, de la que se excluirán aquellas que no estén referenciadas con el código SWIFT.»
- rep 1 [no_cumplido] fragmento: «no especifica explícitamente en el grafo cómo debe identificarse por moneda esta partida» — La respuesta reconoce explícitamente que no puede informar cómo se identifica por moneda la partida, omitiendo los elementos normativos exigidos: determinación por cada moneda, codificación según tabla T0003 del SISCEN y exclusión de monedas sin código SWIFT.
- rep 2 [no_cumplido] fragmento: «no especifica explícitamente en el grafo cómo debe identificarse por moneda esta partida» — La respuesta reconoce explícitamente que no puede informar cómo se identifica por moneda la partida, omitiendo por completo la referencia a la tabla T0003 del SISCEN y la exclusión de monedas sin código SWIFT que exige el criterio.
- rep 3 [no_cumplido] fragmento: «no especifica explícitamente en el grafo cómo debe identificarse por moneda esta partida» — La respuesta reconoce explícitamente que no puede informar cómo se identifica por moneda la partida, omitiendo los elementos normativos exigidos: determinación por cada moneda, codificación según tabla T0003 del SISCEN y exclusión de monedas sin código SWIFT.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Las monedas residuales, de corresponder, se identifican con el código de moneda 9999.
- cita del gold: «De corresponder, las monedas residuales (puntos 6.2.2.2. y 6.2.2.7. de las normas sobre “Capitales mínimos de las entidades financieras”) se identificarán con código de moneda 9999.»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento la identificación de monedas residuales con el código 9999, ausencia total del contenido exigido por el criterio.
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento la identificación de monedas residuales con el código 9999, contenido exigido por el criterio.
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento la identificación de monedas residuales con el código 9999, ni hace referencia a los puntos 6.2.2.2. y 6.2.2.7. de las normas sobre Capitales mínimos.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

## U6-008 — humano: **parcial** · juez (mapping): **correcto** [DESACUERDO]

**Pregunta:** El contrato de un financiamiento exige que los cobros de nuestras exportaciones queden retenidos en una cuenta de garantía hasta una fecha posterior al vencimiento del plazo de liquidación del permiso de embarque. ¿Puede ampliarse ese plazo, hasta cuándo, y con qué límite en función de los servicios de deuda a pagar?

**Respuesta del agente (íntegra):**

> Sí, el plazo puede ampliarse. Según la regulación del BCRA, cuando el contrato de financiamiento exige que los cobros de exportaciones permanezcan depositados en una cuenta de garantía hasta una fecha posterior al vencimiento del plazo de liquidación del permiso de embarque, el exportador podrá solicitar ampliación del plazo hasta el quinto día hábil posterior a esa fecha de depósito.
> 
> Respecto al límite en función de los servicios de deuda: se admite que los fondos originados en el cobro de exportaciones sean acumulados en cuentas destinadas a garantizar la cancelación de vencimientos de deuda, hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: Sí: si la fecha hasta la cual los cobros deben permanecer depositados según el contrato de financiamiento es posterior al vencimiento del plazo de liquidación del permiso, el exportador puede solicitar la ampliación de ese plazo.
- cita del gold: «En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento del plazo para la liquidación de divisas del permiso, el exportador podrá solicitar que este plazo sea ampliado»
- rep 1 [cumplido] fragmento: «cuando el contrato de financiamiento exige que los cobros de exportaciones permanezcan depositados en una cuenta de garantía hasta una fecha posterior al vencimiento del plazo de liquidación del permiso de embarque, el exportador podrá solicitar ampliación del plazo» — La respuesta reproduce fielmente la condición normativa: fecha de depósito posterior al vencimiento del plazo de liquidación habilita al exportador a solicitar la ampliación, con los mismos sujetos y calificadores que la cita.
- rep 2 [cumplido] fragmento: «cuando el contrato de financiamiento exige que los cobros de exportaciones permanezcan depositados en una cuenta de garantía hasta una fecha posterior al vencimiento del plazo de liquidación del permiso de embarque, el exportador podrá solicitar ampliación del plazo» — La respuesta reproduce fielmente la condición normativa: fecha de depósito posterior al vencimiento del plazo de liquidación habilita al exportador a solicitar la ampliación, con los mismos sujetos y calificadores que la cita.
- rep 3 [cumplido] fragmento: «cuando el contrato de financiamiento exige que los cobros de exportaciones permanezcan depositados en una cuenta de garantía hasta una fecha posterior al vencimiento del plazo de liquidación del permiso de embarque, el exportador podrá solicitar ampliación del plazo» — La respuesta reproduce fielmente la condición normativa: fecha de depósito posterior al vencimiento del plazo de liquidación habilita al exportador a solicitar la ampliación, con los mismos sujetos y calificadores que la cita.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La ampliación es hasta el quinto día hábil posterior a la fecha hasta la cual los fondos deben permanecer depositados.
- cita del gold: «el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha.»
- rep 1 [cumplido] fragmento: «el exportador podrá solicitar ampliación del plazo hasta el quinto día hábil posterior a esa fecha de depósito» — La respuesta indica exactamente el mismo límite temporal que la norma: quinto día hábil posterior a la fecha hasta la cual los fondos deben permanecer depositados.
- rep 2 [cumplido] fragmento: «el exportador podrá solicitar ampliación del plazo hasta el quinto día hábil posterior a esa fecha de depósito» — La respuesta indica exactamente el mismo límite temporal que la norma: quinto día hábil posterior a la fecha hasta la cual los fondos deben permanecer depositados.
- rep 3 [cumplido] fragmento: «el exportador podrá solicitar ampliación del plazo hasta el quinto día hábil posterior a esa fecha de depósito» — La respuesta indica exactamente el mismo límite temporal que la norma: quinto día hábil posterior a la fecha hasta la cual los fondos deben permanecer depositados.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La opción está limitada hasta alcanzar el 125% de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario.
- cita del gold: «Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario.»
- rep 1 [cumplido] fragmento: «se admite que los fondos originados en el cobro de exportaciones sean acumulados en cuentas destinadas a garantizar la cancelación de vencimientos de deuda, hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario» — La respuesta reproduce el porcentaje (125%), los conceptos (capital e intereses) y el horizonte temporal (mes corriente y siguientes 6 meses calendario) en términos equivalentes a la cita normativa.
- rep 2 [cumplido] fragmento: «se admite que los fondos originados en el cobro de exportaciones sean acumulados en cuentas destinadas a garantizar la cancelación de vencimientos de deuda, hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario» — La respuesta reproduce el porcentaje (125%), los conceptos (capital e intereses) y el horizonte temporal (mes corriente y siguientes 6 meses calendario) en términos equivalentes a la cita normativa.
- rep 3 [cumplido] fragmento: «se admite que los fondos originados en el cobro de exportaciones sean acumulados en cuentas destinadas a garantizar la cancelación de vencimientos de deuda, hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario» — La respuesta reproduce el porcentaje (125%), los conceptos (capital e intereses) y el período (mes corriente más los siguientes 6 meses calendario) en términos equivalentes a la cita normativa.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

## U6-004 — humano: **correcto** · juez (mapping): **incorrecto** [DESACUERDO]

**Pregunta:** Antes de darle a una empresa acceso al mercado de cambios para un pago al exterior, ¿qué declaración jurada sobre activos externos líquidos y CEDEARs debe presentar el cliente, y a partir de qué valor de tenencias pasa a necesitarse la conformidad previa del BCRA?

**Respuesta del agente (íntegra):**

> Antes de dar acceso al mercado de cambios para un pago al exterior, la entidad debe contar con una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles. A partir de un valor superior al equivalente de USD 100.000 (dólares estadounidenses cien mil) en CEDEARs y/o activos externos líquidos disponibles, la entidad deberá contar con la conformidad previa del BCRA. Si el cliente declara que no posee, al inicio del día, CEDEARs y/o activos externos líquidos disponibles que conjuntamente tengan un valor superior a USD 100.000, la conformidad previa del BCRA no es requerida.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Salvo que cuente con la declaración jurada del cliente al momento del acceso, la entidad debe contar con la conformidad previa del BCRA.
- cita del gold: «La entidad deberá contar con la conformidad previa del BCRA excepto que cuente al momento de acceso al mercado de cambios con una declaración jurada del cliente en la que deje constancia de que:»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona que la conformidad previa del BCRA es la regla general y que la declaración jurada opera como excepción a esa regla; en cambio, presenta la declaración jurada como un requisito previo sin explicitar esa estructura normativa.
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona que la conformidad previa del BCRA es el requisito general y que la declaración jurada opera como excepción a ese requisito; en cambio, presenta la declaración jurada como el requisito principal y la conformidad previa como consecuencia de superar el umbral, invirtiendo la lógica normativa.
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona que la conformidad previa del BCRA es el requisito general y que la declaración jurada opera como excepción a ese requisito; en cambio, presenta la declaración jurada como el requisito principal y la conformidad previa como consecuencia de superar el umbral, invirtiendo la lógica normativa.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 2 → modal **no_cumplido** (['dudoso', 'no_cumplido', 'no_cumplido']) ⚠ no unánime
- criterio: La declaración jurada debe dejar constancia de que la totalidad de las tenencias de moneda extranjera en el país del cliente están depositadas en cuentas en entidades financieras y de que, al inicio del día en que solicita el acceso, no poseía CEDEARs y/o activos externos líquidos disponibles que conjuntamente superen el equivalente de USD 100.000.
- cita del gold: «3.16.2.1. La totalidad de sus tenencias de moneda extranjera en el país se encuentran depositadas en cuentas en entidades financieras y que no poseía, al inicio del día en que solicita el acceso al mercado, certificados de depósitos argentinos representativos de acciones extranjeras (CEDEARs) y/o activos externos líquidos disponibles que conjuntamente tengan un valor superior al equivalente de USD 100.000 (dólares estadounidenses cien mil).»
- rep 1 [dudoso] fragmento: «una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles» — La respuesta menciona las tenencias en cuentas de entidades financieras y los CEDEARs/activos externos líquidos, pero no reproduce el requisito de que la totalidad de las tenencias de moneda extranjera en el país estén depositadas en cuentas financieras (condición afirmativa), sino que lo presenta de forma ambigua; tampoco queda claro si la declaración debe afirmar que no se supera el umbral al inicio del día.
- rep 2 [no_cumplido] fragmento: «la entidad debe contar con una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles» — La respuesta omite el requisito de que la declaración jurada deje constancia de que la TOTALIDAD de las tenencias de moneda extranjera en el país están depositadas en cuentas en entidades financieras; solo menciona las tenencias de manera genérica sin ese calificador esencial.
- rep 3 [no_cumplido] fragmento: «la entidad debe contar con una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles» — La respuesta omite el requisito de que la declaración jurada deje constancia de que la TOTALIDAD de las tenencias de moneda extranjera en el país están depositadas en cuentas en entidades financieras; solo menciona las tenencias de manera genérica sin ese calificador esencial.
- pre-clasificación mecánica del par: **evidencia** (nulos=0/3, no_verbatim=0/3, fragmentos_distintos=2)

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: El umbral a partir del cual las tenencias hacen necesaria la conformidad previa del BCRA es un valor conjunto superior al equivalente de USD 100.000 (cien mil dólares estadounidenses); si el cliente supera ese monto, la entidad puede aceptar alternativamente una declaración jurada de que no se excede el monto al considerar las situaciones previstas en los incisos i) a vii).
- cita del gold: «En el caso de que el cliente tuviera activos externos líquidos disponibles y/o CEDEARs por un monto superior al establecido en el primer párrafo, la entidad también podrá aceptar una declaración jurada del cliente en la que deje constancia que no se excede tal monto al considerar que, parcial o totalmente, los activos externos líquidos:»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona la posibilidad alternativa de que, cuando el cliente supera el umbral de USD 100.000, la entidad pueda aceptar una declaración jurada en la que el cliente deje constancia de que no excede ese monto al considerar las situaciones previstas en los incisos i) a vii).
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en absoluto la posibilidad alternativa de que, cuando el cliente supera el umbral de USD 100.000, la entidad pueda aceptar una declaración jurada en la que el cliente deje constancia de que no excede ese monto al considerar las situaciones previstas en los incisos i) a vii).
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona la posibilidad alternativa de que, cuando el cliente supera el umbral de USD 100.000, la entidad pueda aceptar una declaración jurada en la que el cliente deje constancia de que no excede ese monto al considerar las situaciones previstas en los incisos i) a vii).
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 4 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La declaración jurada también debe incluir el compromiso de liquidar en el mercado de cambios, dentro de los 5 días hábiles de su puesta a disposición, los fondos que reciba en el exterior por cobro de préstamos a terceros, cobro de depósitos a plazo o venta de activos adquiridos/constituidos/otorgados con posterioridad al 28/05/20.
- cita del gold: «3.16.2.2. Se compromete a liquidar en el mercado de cambios, dentro de los 5 (cinco) días hábiles de su puesta a disposición, aquellos fondos que reciba en el exterior originados en el cobro de préstamos otorgados a terceros, el cobro de un depósito a plazo o de la venta de cualquier tipo de activo, cuando el activo hubiera sido adquirido, el depósito constituido o el préstamo otorgado con posterioridad al 28/05/20.»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no hace ninguna mención al compromiso de liquidar en el mercado de cambios, dentro de los 5 días hábiles, los fondos recibidos en el exterior por cobro de préstamos, depósitos a plazo o venta de activos constituidos/otorgados con posterioridad al 28/05/20.
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento el compromiso de liquidar en el mercado de cambios, dentro de los 5 días hábiles de su puesta a disposición, los fondos recibidos en el exterior por cobro de préstamos, depósitos a plazo o venta de activos constituidos/otorgados con posterioridad al 28/05/20.
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento el compromiso de liquidar en el mercado de cambios, dentro de los 5 días hábiles de su puesta a disposición, los fondos recibidos en el exterior por cobro de préstamos, depósitos a plazo o venta de activos constituidos/otorgados con posterioridad al 28/05/20.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

## U6-002 — humano: **correcto** · juez (mapping): **parcial** [DESACUERDO]

**Pregunta:** Una sociedad local quiere girar dividendos a sus accionistas del exterior. ¿Qué debe verificar el banco respecto de los balances de la empresa y del monto aprobado por la asamblea antes de dar curso a la transferencia?

**Respuesta del agente (íntegra):**

> Antes de dar curso a la transferencia de dividendos al exterior, el banco debe verificar dos requisitos principales:
> 
> 1. **Balances cerrados y auditados**: Las utilidades y dividendos deben corresponder a balances cerrados y auditados.
> 
> 2. **Monto aprobado por asamblea**: El monto total abonado por concepto de utilidades y dividendos a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: Las utilidades y dividendos a girar deben corresponder a balances cerrados y auditados.
- cita del gold: «3.4.1. Las utilidades y dividendos correspondan a balances cerrados y auditados.»
- rep 1 [cumplido] fragmento: «Las utilidades y dividendos deben corresponder a balances cerrados y auditados.» — La respuesta reproduce fielmente el contenido del criterio, indicando que las utilidades y dividendos deben corresponder a balances cerrados y auditados, en línea exacta con la cita normativa.
- rep 2 [cumplido] fragmento: «Las utilidades y dividendos deben corresponder a balances cerrados y auditados.» — La respuesta reproduce fielmente el contenido del criterio, indicando que las utilidades y dividendos deben corresponder a balances cerrados y auditados, en línea exacta con la cita normativa.
- rep 3 [cumplido] fragmento: «Las utilidades y dividendos deben corresponder a balances cerrados y auditados.» — La respuesta reproduce fielmente el contenido del criterio, indicando que las utilidades y dividendos deben corresponder a balances cerrados y auditados, en línea con la cita normativa.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: El monto total abonado por este concepto a accionistas no residentes, incluido el pago que se solicita, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.
- cita del gold: «3.4.2. El monto total abonado por este concepto a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no supere el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.»
- rep 1 [cumplido] fragmento: «El monto total abonado por concepto de utilidades y dividendos a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.» — La respuesta reproduce con equivalencia normativa precisa el criterio, incluyendo todos los elementos relevantes: monto total abonado, accionistas no residentes, inclusión del pago solicitado, límite en moneda local y determinación por asamblea.
- rep 2 [cumplido] fragmento: «El monto total abonado por concepto de utilidades y dividendos a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.» — La respuesta reproduce con equivalencia normativa precisa todos los elementos del criterio: monto total abonado, accionistas no residentes, inclusión del pago solicitado, límite en moneda local y distribución por asamblea.
- rep 3 [cumplido] fragmento: «El monto total abonado por concepto de utilidades y dividendos a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.» — La respuesta reproduce con equivalencia normativa precisa el criterio, incluyendo todos los elementos relevantes: monto total, accionistas no residentes, pago en curso, límite en moneda local y distribución por asamblea.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La entidad debe contar con una declaración jurada firmada por el representante legal de la empresa residente o un apoderado con facultades suficientes.
- cita del gold: «La entidad deberá contar con una declaración jurada firmada por el representante legal de la empresa residente o un apoderado con facultades suficientes para asumir este compromiso en nombre de la empresa.»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento la obligación de contar con una declaración jurada firmada por el representante legal o apoderado con facultades suficientes, requisito exigido por el criterio.
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento la obligación de contar con una declaración jurada firmada por el representante legal o apoderado con facultades suficientes, requisito exigido por el criterio.
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento la obligación de contar con una declaración jurada firmada por el representante legal o apoderado con facultades suficientes.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

## U6-024 — humano: **parcial** · juez (mapping): **correcto** [DESACUERDO]

**Pregunta:** ¿Qué características de identificación y ubicación deben cumplir el botón de arrepentimiento y el botón de baja en el home banking para que el usuario pueda revocar una contratación o rescindir un servicio en el mismo acto?

**Respuesta del agente (íntegra):**

> Según la regulación del BCRA, el botón de arrepentimiento y el botón de baja en el home banking deben cumplir con las siguientes características de identificación y ubicación:
> 
> **Identificación:** Deberán estar identificados con la leyenda 'botón de arrepentimiento' o 'botón de baja', según corresponda.
> 
> **Ubicación:** Encontrarse ubicados en un lugar destacado –en cuanto a visibilidad y tamaño– del primer acceso del servicio de banca por Internet (home banking) o mecanismo similar, a los fines de que el usuario pueda proceder en el mismo acto a la efectiva revocación o rescisión del producto o servicio.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: Los hipervínculos deben estar identificados con la leyenda “botón de arrepentimiento” o “botón de baja”, según corresponda.
- cita del gold: «En ambos casos, deberán estar identificados con la leyenda “botón de arrepentimiento” o “botón de baja”, según corresponda»
- rep 1 [cumplido] fragmento: «Deberán estar identificados con la leyenda 'botón de arrepentimiento' o 'botón de baja', según corresponda.» — La respuesta reproduce fielmente el requisito de identificación con las leyendas exigidas, incluyendo el calificador 'según corresponda'.
- rep 2 [cumplido] fragmento: «Deberán estar identificados con la leyenda 'botón de arrepentimiento' o 'botón de baja', según corresponda.» — La respuesta reproduce fielmente el requisito de identificación con las leyendas exigidas, incluyendo el calificador 'según corresponda'.
- rep 3 [cumplido] fragmento: «Deberán estar identificados con la leyenda 'botón de arrepentimiento' o 'botón de baja', según corresponda.» — La respuesta reproduce fielmente el contenido del criterio, indicando la leyenda exacta y la condicionalidad 'según corresponda', en equivalencia directa con la cita normativa.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: Deben ubicarse en un lugar destacado —en cuanto a visibilidad y tamaño— del primer acceso del servicio de banca por Internet (home banking) o mecanismo similar.
- cita del gold: «encontrarse ubicados en un lugar destacado –en cuanto a visibilidad y tamaño– del primer acceso de su servicio de banca por Internet –home banking– o mecanismo similar»
- rep 1 [cumplido] fragmento: «Encontrarse ubicados en un lugar destacado –en cuanto a visibilidad y tamaño– del primer acceso del servicio de banca por Internet (home banking) o mecanismo similar» — La respuesta reproduce con exactitud los calificadores de visibilidad, tamaño y la referencia al primer acceso del home banking o mecanismo similar.
- rep 2 [cumplido] fragmento: «Encontrarse ubicados en un lugar destacado –en cuanto a visibilidad y tamaño– del primer acceso del servicio de banca por Internet (home banking) o mecanismo similar» — La respuesta reproduce con exactitud los calificadores de visibilidad, tamaño y la referencia al primer acceso del home banking o mecanismo similar.
- rep 3 [cumplido] fragmento: «Encontrarse ubicados en un lugar destacado –en cuanto a visibilidad y tamaño– del primer acceso del servicio de banca por Internet (home banking) o mecanismo similar» — La respuesta reproduce con precisión los calificadores normativos (visibilidad, tamaño, primer acceso, home banking o mecanismo similar), cumpliendo íntegramente el criterio.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La finalidad es que el usuario pueda proceder en el mismo acto a la efectiva revocación o rescisión del producto o servicio.
- cita del gold: «a los fines de que el usuario pueda proceder en el mismo acto a la efectiva revocación o rescisión del producto o servicio, según corresponda.»
- rep 1 [cumplido] fragmento: «a los fines de que el usuario pueda proceder en el mismo acto a la efectiva revocación o rescisión del producto o servicio.» — La respuesta refleja fielmente la finalidad normativa, incluyendo la expresión 'en el mismo acto' y la referencia a la revocación o rescisión del producto o servicio.
- rep 2 [cumplido] fragmento: «a los fines de que el usuario pueda proceder en el mismo acto a la efectiva revocación o rescisión del producto o servicio.» — La respuesta refleja fielmente la finalidad normativa, incluyendo la expresión 'en el mismo acto' y la referencia a la revocación o rescisión del producto o servicio.
- rep 3 [cumplido] fragmento: «a los fines de que el usuario pueda proceder en el mismo acto a la efectiva revocación o rescisión del producto o servicio.» — La respuesta refleja fielmente la finalidad normativa, incluyendo los elementos clave: mismo acto, efectiva revocación o rescisión, y producto o servicio.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

## U6-017 — humano: **correcto** · juez (mapping): **parcial** [DESACUERDO]

**Pregunta:** ¿A partir de qué magnitud de financiaciones la clasificación de un deudor y el cálculo de sus previsiones requieren la aprobación previa del Directorio de la entidad, y qué mayoría se exige cuando se trata de clientes vinculados?

**Respuesta del agente (íntegra):**

> La clasificación de un deudor y el cálculo de sus previsiones requieren aprobación previa del Directorio o Consejo de Administración cuando las financiaciones excedan del 2,5% de la RPC (Responsabilidad Patrimonial Computable) de la entidad financiera del mes anterior. La aprobación debe ser por mayoría simple en los casos ordinarios, pero se exige una mayoría de dos tercios cuando se trata de clientes vinculados.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La aprobación previa del Directorio (o Consejo de Administración o autoridad equivalente) se requiere para la clasificación y el cálculo de previsiones por financiaciones que excedan el 2,5 % de la RPC de la entidad del mes anterior al que corresponda.
- cita del gold: «por financiaciones que excedan del 2,5 % de la RPC de la entidad financiera del mes anterior al que corresponda, deberán contar con la previa aprobación de los miembros del Directorio o Consejo de Administración»
- rep 1 [cumplido] fragmento: «requieren aprobación previa del Directorio o Consejo de Administración cuando las financiaciones excedan del 2,5% de la RPC (Responsabilidad Patrimonial Computable) de la entidad financiera del mes anterior» — La respuesta reproduce fielmente el umbral del 2,5% de la RPC del mes anterior y los órganos requeridos (Directorio o Consejo de Administración), en línea con la cita normativa.
- rep 2 [cumplido] fragmento: «requieren aprobación previa del Directorio o Consejo de Administración cuando las financiaciones excedan del 2,5% de la RPC (Responsabilidad Patrimonial Computable) de la entidad financiera del mes anterior» — La respuesta reproduce fielmente el umbral del 2,5% de la RPC del mes anterior y los órganos requeridos (Directorio o Consejo de Administración), en línea con la cita normativa.
- rep 3 [cumplido] fragmento: «requieren aprobación previa del Directorio o Consejo de Administración cuando las financiaciones excedan del 2,5% de la RPC (Responsabilidad Patrimonial Computable) de la entidad financiera del mes anterior» — La respuesta reproduce fielmente el umbral del 2,5% de la RPC del mes anterior y los órganos requeridos (Directorio o Consejo de Administración), en línea con la cita normativa.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La aprobación es por mayoría simple, y cuando se trata de clientes vinculados se exige dos tercios de la totalidad de los miembros.
- cita del gold: «–por mayoría simple o, cuando se trate de clientes vinculados, de dos tercios de la totalidad de los miembros– o autoridad equivalente de la entidad financiera prestamista.»
- rep 1 [cumplido] fragmento: «La aprobación debe ser por mayoría simple en los casos ordinarios, pero se exige una mayoría de dos tercios cuando se trata de clientes vinculados.» — La respuesta refleja correctamente ambas mayorías: simple para el caso general y dos tercios para clientes vinculados, conforme a la cita normativa; aunque omite el calificador 'de la totalidad de los miembros', el contenido esencial coincide.
- rep 2 [cumplido] fragmento: «La aprobación debe ser por mayoría simple en los casos ordinarios, pero se exige una mayoría de dos tercios cuando se trata de clientes vinculados.» — La respuesta refleja correctamente ambas mayorías exigidas por la norma: mayoría simple para el caso general y dos tercios para clientes vinculados, aunque omite el detalle de que los dos tercios se calculan sobre la totalidad de los miembros, lo cual no altera sustancialmente el contenido normativo exigido por el criterio.
- rep 3 [cumplido] fragmento: «La aprobación debe ser por mayoría simple en los casos ordinarios, pero se exige una mayoría de dos tercios cuando se trata de clientes vinculados.» — La respuesta refleja correctamente ambas mayorías: simple para el caso general y dos tercios para clientes vinculados, conforme a la cita normativa; omite el detalle 'de la totalidad de los miembros' pero no altera el alcance sustancial del criterio.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La conformidad debe referirse, con opinión fundada, tanto a la clasificación asignada a cada deudor como al nivel de las previsiones calculadas.
- cita del gold: «Dicha conformidad estará referida –con opinión fundada en todos los casos– tanto a la clasificación asignada a cada uno de los deudores comprendidos como al nivel de las previsiones calculadas.»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento que la conformidad debe referirse, con opinión fundada, tanto a la clasificación asignada a cada deudor como al nivel de las previsiones calculadas.
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento que la conformidad debe estar referida con opinión fundada tanto a la clasificación asignada a cada deudor como al nivel de las previsiones calculadas.
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento que la conformidad debe referirse con opinión fundada tanto a la clasificación del deudor como al nivel de las previsiones calculadas.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

## U6-009 — humano: **parcial** · juez (mapping): **incorrecto** [DESACUERDO]

**Pregunta:** Para pagar al exterior una importación que ya cuenta con registro de ingreso aduanero bajo el SEPAIMPO, ¿qué documentación y verificaciones debe completar la entidad antes de dar acceso al mercado de cambios?

**Respuesta del agente (íntegra):**

> Para pagar al exterior una importación que ya cuenta con registro de ingreso aduanero bajo SEPAIMPO, la entidad debe completar las siguientes documentaciones y verificaciones antes de dar acceso al mercado de cambios: (1) Contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO); (2) Contar con constancia del registro aduanero del ingreso de bienes que originan el pago; (3) Contar con la convalidación de la situación de la operación en el sistema online implementado por el BCRA al momento de dar acceso al mercado de cambios.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La entidad debe certificar (como entidad de seguimiento de la oficialización, o contar con certificación de la entidad responsable) que cuenta con la constancia del registro aduanero del ingreso de los bienes, copia de la factura comercial emitida en el exterior a nombre del importador residente (con emisor, importador, cantidad y descripción de la mercadería, condición de venta y valor) y copia del Documento de Transporte.
- cita del gold: «i) Cuenta con constancia del registro aduanero del ingreso al país de los bienes que originan el pago a cancelarse. ii) Cuenta con copia de factura comercial emitida en el exterior a nombre del cliente residente en el país, que efectúa la compra al exterior, donde conste nombre y dirección del emisor, nombre del importador argentino, la cantidad y descripción de la mercadería, condición de venta y valor de la factura. iii) Cuenta con copia del Documento de Transporte (Conocimiento de Embarque – Carta de Porte – Guía Aérea).»
- rep 1 [no_cumplido] fragmento: «Contar con constancia del registro aduanero del ingreso de bienes que originan el pago» — La respuesta menciona la constancia del registro aduanero, pero omite completamente la copia de la factura comercial (con todos sus requisitos: nombre y dirección del emisor, nombre del importador, cantidad y descripción de la mercadería, condición de venta y valor) y la copia del Documento de Transporte, que son elementos exigidos por el criterio.
- rep 2 [no_cumplido] fragmento: «Contar con constancia del registro aduanero del ingreso de bienes que originan el pago» — La respuesta menciona la constancia del registro aduanero, pero omite completamente los otros dos elementos exigidos por el criterio: la copia de la factura comercial (con todos sus datos: nombre y dirección del emisor, nombre del importador, cantidad y descripción de la mercadería, condición de venta y valor) y la copia del Documento de Transporte.
- rep 3 [no_cumplido] fragmento: «Contar con constancia del registro aduanero del ingreso de bienes que originan el pago» — La respuesta menciona la constancia del registro aduanero, pero omite completamente los otros dos requisitos exigidos por el criterio: la copia de la factura comercial (con todos sus elementos: nombre y dirección del emisor, nombre del importador, cantidad y descripción de la mercadería, condición de venta y valor) y la copia del Documento de Transporte.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Debe verificar que la información de la factura comercial y del Documento de Transporte sea consistente con los registros aduaneros, y que la documentación permita establecer la fecha de vencimiento de la obligación (o que no tiene vencimiento pactado).
- cita del gold: «iv) Que la información que surge de la factura comercial y del Documento de Transporte sea consistente con la que figura en los registros aduaneros, considerando las normas de declaración aduanera aplicables. v) Que la documentación presentada le permita establecer la fecha de vencimiento de la obligación con el exterior por parte del importador o, en su defecto, que la operación no tiene una fecha de vencimiento pactada.»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento la verificación de consistencia entre la factura comercial/Documento de Transporte y los registros aduaneros, ni la verificación de la fecha de vencimiento de la obligación con el exterior.
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento la verificación de consistencia entre la factura comercial/Documento de Transporte y los registros aduaneros, ni la verificación de la fecha de vencimiento de la obligación con el exterior.
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento la verificación de consistencia entre la factura comercial/Documento de Transporte y los registros aduaneros, ni la verificación de la fecha de vencimiento de la obligación con el exterior.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Debe verificar que el total de pagos imputados a la oficialización, incluido el que se solicita, no supere el monto facturado en la condición de compra pactada, y que el beneficiario sea el proveedor del exterior (o la entidad/agencia que financió la compra, o el no residente que compró el crédito).
- cita del gold: «vii) Que el total de los pagos realizados con imputación a la oficialización de importación, incluyendo el pago cuyo curso se está solicitando, no supera el monto facturado en la condición de compra pactada. viii) Que el beneficiario del pago a realizar sea el proveedor del exterior o, en su caso, la entidad financiera del exterior o la agencia oficial de crédito que financió la compra al proveedor del exterior»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no hace ninguna referencia a la verificación de que el total de pagos imputados a la oficialización no supere el monto facturado, ni a la verificación de la identidad del beneficiario del pago.
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no hace ninguna referencia a la verificación de que el total de pagos imputados a la oficialización no supere el monto facturado, ni a la verificación de que el beneficiario sea el proveedor del exterior o la entidad/agencia que financió la compra.
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no hace ninguna referencia a la verificación de que el total de pagos imputados no supere el monto facturado, ni a la verificación de que el beneficiario sea el proveedor del exterior o la entidad/agencia que financió la compra.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 4 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La venta de divisas debe cursarse con débito en cuentas del cliente en entidades financieras locales y el pago no debe realizarse antes de la fecha de vencimiento de la obligación con el exterior.
- cita del gold: «10.3.2.2. La venta de las divisas es cursada con débito en cuentas del cliente en entidades financieras locales por alguna de las modalidades de medios de pago vigentes. 10.3.2.3. El pago no se realiza con anterioridad a la fecha de vencimiento de la obligación con el exterior.»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona el requisito de que la venta de divisas se curse con débito en cuentas del cliente en entidades financieras locales, ni la prohibición de realizar el pago antes de la fecha de vencimiento de la obligación.
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona el requisito de que la venta de divisas se curse con débito en cuentas del cliente en entidades financieras locales, ni la prohibición de realizar el pago antes de la fecha de vencimiento de la obligación con el exterior.
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona el requisito de que la venta de divisas se curse con débito en cuentas del cliente en entidades financieras locales, ni la prohibición de realizar el pago antes de la fecha de vencimiento de la obligación con el exterior.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 5 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Debe contar con una declaración jurada del importador (o su representante legal/apoderado) comprometiéndose a liquidar en el mercado de cambios, dentro de los 20 días hábiles de su puesta a disposición, las divisas que perciba en devolución de pagos de importaciones efectuados con acceso al mercado.
- cita del gold: «10.3.2.4. Declaración jurada comprometiéndose a liquidar en el mercado de cambios, dentro de los 20 (veinte) días hábiles de su puesta a disposición, las divisas que pudiera percibir en devolución de pagos de importaciones efectuados con acceso al mercado de cambios. Esta declaración deberá ser firmada por el importador o quien ejerza su representación legal o un apoderado con facultades suficientes para asumir este compromiso en nombre del importador.»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no hace ninguna referencia a la declaración jurada del importador comprometiéndose a liquidar en el mercado de cambios, dentro de los 20 días hábiles, las divisas percibidas en devolución de pagos de importaciones.
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no hace ninguna referencia a la declaración jurada del importador comprometiéndose a liquidar en el mercado de cambios, dentro de los 20 días hábiles, las divisas percibidas en devolución de pagos de importaciones.
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no hace ninguna referencia a la declaración jurada del importador comprometiéndose a liquidar en el mercado de cambios, dentro de los 20 días hábiles, las divisas percibidas en devolución de pagos de importaciones.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

## U6-023 — humano: **correcto** · juez (mapping): **parcial** [DESACUERDO]

**Pregunta:** ¿Puede una entidad rechazar una solicitud de financiación basándose únicamente en la edad del solicitante cuando sus ingresos proyectados son suficientes, y qué papel juega la posibilidad de contratar un seguro de vida sobre saldo deudor?

**Respuesta del agente (íntegra):**

> No. Según la regulación del BCRA, una entidad **no puede rechazar una solicitud de financiación basándose únicamente en la edad del solicitante cuando su nivel de ingresos proyectados sea suficiente y sea posible tomar cobertura por su riesgo de muerte mediante la contratación de un seguro de vida sobre saldo deudor**.
> 
> El seguro de vida sobre saldo deudor juega un papel **fundamental** en esta regulación: es una de las dos condiciones que debe cumplirse para que la prohibición de rechazo por edad sea aplicable. Específicamente, la entidad debe poder tomar cobertura del riesgo de muerte del solicitante mediante este seguro.
> 
> La regulación establece que los sujetos obligados deben contratar un seguro sobre saldo deudor con cobertura de fallecimiento e invalidez total permanente respecto de aquellas financiaciones otorgadas a personas humanas. Alternativamente, pueden autoasegurar estos riesgos. En ambos casos, la cobertura debe extinguir totalmente el monto adeudado en caso de fallecimiento o invalidez total permanente del deudor.
> 
> En resumen: la edad por sí sola no es motivo válido de rechazo si concurren dos requisitos: (1) ingresos proyectados suficientes, y (2) posibilidad de contratar un seguro de vida sobre saldo deudor.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: No: no corresponde rechazar solicitudes de financiación por el solo dato de la edad del solicitante cuando su nivel de ingresos proyectados es suficiente y es posible tomar cobertura por riesgo de muerte mediante un seguro de vida sobre saldo deudor.
- cita del gold: «En particular, no corresponderá el rechazo de solicitudes de financiación por el solo dato de la edad del solicitante, cuando su nivel de ingresos proyectados sea suficiente y sea posible tomar cobertura por su riesgo de muerte mediante la contratación de un seguro de vida sobre saldo deudor.»
- rep 1 [cumplido] fragmento: «una entidad no puede rechazar una solicitud de financiación basándose únicamente en la edad del solicitante cuando su nivel de ingresos proyectados sea suficiente y sea posible tomar cobertura por su riesgo de muerte mediante la contratación de un seguro de vida sobre saldo deudor» — La respuesta reproduce fielmente los tres elementos del criterio: rechazo por solo dato de edad, ingresos proyectados suficientes y posibilidad de contratar seguro de vida sobre saldo deudor, en equivalencia normativa directa con la cita.
- rep 2 [cumplido] fragmento: «una entidad no puede rechazar una solicitud de financiación basándose únicamente en la edad del solicitante cuando su nivel de ingresos proyectados sea suficiente y sea posible tomar cobertura por su riesgo de muerte mediante la contratación de un seguro de vida sobre saldo deudor» — La respuesta reproduce fielmente los tres elementos del criterio: rechazo por solo dato de edad, ingresos proyectados suficientes y posibilidad de contratar seguro de vida sobre saldo deudor, con los mismos calificadores y sujetos.
- rep 3 [cumplido] fragmento: «una entidad no puede rechazar una solicitud de financiación basándose únicamente en la edad del solicitante cuando su nivel de ingresos proyectados sea suficiente y sea posible tomar cobertura por su riesgo de muerte mediante la contratación de un seguro de vida sobre saldo deudor» — La respuesta reproduce fielmente los tres elementos del criterio: rechazo por solo dato de edad, ingresos proyectados suficientes y posibilidad de contratar seguro de vida sobre saldo deudor, con los mismos calificadores y sujetos.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La posibilidad de contratar el seguro de vida sobre saldo deudor es lo que habilita cubrir el riesgo de muerte, pero la decisión de contratar o no dicho seguro es del sujeto obligado.
- cita del gold: «Ello, no obstante, será decisión del sujeto obligado contratar o no dicho seguro.»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento que la decisión de contratar o no el seguro de vida sobre saldo deudor es del sujeto obligado; de hecho, presenta la contratación del seguro como una obligación, lo cual contradice este criterio.
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento que la decisión de contratar o no el seguro de vida sobre saldo deudor es del sujeto obligado; de hecho, presenta el seguro como condición necesaria para la prohibición de rechazo, sin aclarar esa facultad discrecional.
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento que la decisión de contratar o no el seguro de vida sobre saldo deudor es del sujeto obligado; de hecho, presenta la posibilidad de contratar el seguro como condición necesaria para la prohibición de rechazo, sin aclarar esa facultad discrecional.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: El rechazo por edad se enmarca en la prohibición de trato discriminatorio: la edad es uno de los motivos por los que los sujetos obligados deben prevenir actos u omisiones discriminatorios.
- cita del gold: «Los sujetos obligados deberán adoptar los recaudos necesarios a los efectos de prevenir particularmente los actos u omisiones discriminatorios determinados por motivos tales como raza, religión, nacionalidad, ideología, opinión política o gremial, edad, sexo, posición económica, condición social o caracteres físicos.»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no enmarca el rechazo por edad dentro de una prohibición general de trato discriminatorio ni menciona que la edad es uno de los motivos por los que los sujetos obligados deben prevenir actos u omisiones discriminatorios.
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no hace ninguna referencia al marco de prohibición de trato discriminatorio ni menciona que la edad es uno de los motivos por los que los sujetos obligados deben prevenir actos u omisiones discriminatorios.
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento que el rechazo por edad se enmarca en una prohibición general de trato discriminatorio ni enumera los demás motivos de discriminación que los sujetos obligados deben prevenir.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

---

# B. requiere_adjudicacion (el instrumento no decidió)

## U6-005 — humano: **parcial** · juez (mapping): **requiere_adjudicacion** [ADJUDICACIÓN]

**Pregunta:** Una persona jurídica quiere operar compraventa de títulos valores con liquidación en moneda extranjera. ¿Por qué mecanismos puede abonar esas operaciones y qué formas de pago están expresamente vedadas?

**Respuesta del agente (íntegra):**

> Una persona jurídica que opera compraventa de títulos valores con liquidación en moneda extranjera puede abonar esas operaciones mediante los siguientes mecanismos: (1) transferencia de fondos, (2) cable sobre cuentas bancarias, o (3) cable sobre cuenta de terceros en el exterior.
> 
> Respecto a las formas de pago expresamente vedadas, la regulación del BCRA prohíbe la liquidación de estas operaciones mediante billetes extranjeros.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **dudoso** (['no_cumplido', 'dudoso', 'dudoso']) ⚠ no unánime
- criterio: Puede abonar mediante transferencia de fondos desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales.
- cita del gold: «mediante transferencia de fondos desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales; o»
- rep 1 [no_cumplido] fragmento: «transferencia de fondos» — La respuesta menciona 'transferencia de fondos' de forma genérica, pero omite los calificadores normativos esenciales: que debe ser desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales.
- rep 2 [dudoso] fragmento: «transferencia de fondos» — La respuesta menciona 'transferencia de fondos' pero omite los calificadores normativos esenciales: que debe ser desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales. La omisión de esos calificadores impide confirmar equivalencia normativa plena.
- rep 3 [dudoso] fragmento: «transferencia de fondos» — La respuesta menciona 'transferencia de fondos' pero omite los calificadores normativos esenciales: que debe ser desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales. La omisión de esos calificadores impide confirmar equivalencia normativa plena.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **dudoso** (['no_cumplido', 'dudoso', 'dudoso']) ⚠ no unánime
- criterio: Puede abonar contra cable sobre cuentas bancarias a nombre del cliente en una entidad del exterior que no esté constituida en países o territorios donde no se aplican (o no suficientemente) las Recomendaciones del GAFI.
- cita del gold: «contra cable sobre cuentas bancarias a nombre del cliente en una entidad del exterior que no esté constituida en países o territorios donde no se aplican o no se aplican suficientemente las Recomendaciones del Grupo de Acción Financiera Internacional.»
- rep 1 [no_cumplido] fragmento: «cable sobre cuentas bancarias» — La respuesta menciona 'cable sobre cuentas bancarias' pero omite los calificadores normativos: que la cuenta debe estar a nombre del cliente y que la entidad del exterior no debe estar constituida en países o territorios no cooperantes según GAFI.
- rep 2 [dudoso] fragmento: «cable sobre cuentas bancarias» — La respuesta menciona 'cable sobre cuentas bancarias' pero omite la condición normativa de que la cuenta debe estar a nombre del cliente y que la entidad del exterior no debe estar constituida en países o territorios no cooperantes según GAFI, lo que altera el alcance del mecanismo.
- rep 3 [dudoso] fragmento: «cable sobre cuentas bancarias» — La respuesta menciona 'cable sobre cuentas bancarias' pero omite la condición normativa de que la cuenta debe estar a nombre del cliente y que la entidad del exterior no debe estar constituida en países o territorios no cooperantes según GAFI, lo que altera el alcance del mecanismo.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Puede abonar contra cable sobre una cuenta de terceros en el exterior (no radicada en jurisdicciones no cooperantes según GAFI) únicamente en el caso de venta de bonos BOPREAL adquiridos en suscripción primaria por operaciones elegibles (puntos 4.4., 4.5., 4.6.1. y 4.7.).
- cita del gold: «contra cable sobre una cuenta de terceros en el exterior que no se encuentre radicada en países o territorios donde no se aplican o no se aplican suficientemente las Recomendaciones del Grupo de Acción Financiera Internacional, cuando se trate de la venta de bonos BOPREAL adquiridos por el vendedor en una suscripción primaria por operaciones elegibles en los puntos 4.4., 4.5., 4.6.1. y 4.7.»
- rep 1 [no_cumplido] fragmento: «cable sobre cuenta de terceros en el exterior» — La respuesta menciona 'cable sobre cuenta de terceros en el exterior' sin indicar la restricción fundamental: que esta modalidad solo aplica para la venta de bonos BOPREAL adquiridos en suscripción primaria por operaciones elegibles en los puntos específicos, ni la exclusión de jurisdicciones no cooperantes según GAFI.
- rep 2 [no_cumplido] fragmento: «cable sobre cuenta de terceros en el exterior» — La respuesta menciona el cable sobre cuenta de terceros en el exterior sin ninguna de las condiciones restrictivas exigidas por la norma: que no esté radicada en jurisdicciones no cooperantes según GAFI y que se trate exclusivamente de venta de bonos BOPREAL adquiridos en suscripción primaria por operaciones elegibles en los puntos específicos.
- rep 3 [no_cumplido] fragmento: «cable sobre cuenta de terceros en el exterior» — La respuesta menciona el cable sobre cuenta de terceros en el exterior como mecanismo general, sin reflejar la condición normativa esencial de que esta modalidad está restringida exclusivamente a la venta de bonos BOPREAL adquiridos en suscripción primaria por operaciones elegibles en los puntos específicos (4.4., 4.5., 4.6.1. y 4.7.), ni la restricción de jurisdicciones GAFI.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 4 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Está expresamente vedado liquidar estas operaciones mediante el pago en billetes en moneda extranjera o mediante su depósito en cuentas custodia o en cuentas de terceros (salvo las operaciones contra cable con cuentas de terceros del punto 4.3.2.3.).
- cita del gold: «En ningún caso se permite la liquidación de estas operaciones mediante el pago en billetes en moneda extranjera o mediante su depósito en cuentas custodia o en cuentas de terceros, excepto que se trate de operaciones contra cable que utilicen cuentas de terceros en el marco de lo contemplado en el punto 4.3.2.3.»
- rep 1 [no_cumplido] fragmento: «la regulación del BCRA prohíbe la liquidación de estas operaciones mediante billetes extranjeros» — La respuesta solo menciona la prohibición de billetes en moneda extranjera, pero omite las otras dos formas vedadas: el depósito en cuentas custodia y el depósito en cuentas de terceros (con la excepción prevista para operaciones contra cable del punto 4.3.2.3.).
- rep 2 [no_cumplido] fragmento: «la regulación del BCRA prohíbe la liquidación de estas operaciones mediante billetes extranjeros» — La respuesta solo menciona la prohibición de pago en billetes en moneda extranjera, pero omite las otras dos formas vedadas expresamente: el depósito en cuentas custodia y el depósito en cuentas de terceros (con la excepción prevista para operaciones contra cable del punto 4.3.2.3.).
- rep 3 [no_cumplido] fragmento: «la regulación del BCRA prohíbe la liquidación de estas operaciones mediante billetes extranjeros» — La respuesta solo menciona la prohibición de pago en billetes, pero omite las otras dos formas vedadas expresamente por la norma: el depósito en cuentas custodia y el depósito en cuentas de terceros (con la excepción prevista para operaciones contra cable del punto 4.3.2.3.).
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

## U6-010 — humano: **parcial** · juez (mapping): **requiere_adjudicacion** [ADJUDICACIÓN]

**Pregunta:** Mi empresa debe intereses por una deuda comercial con su proveedor del exterior. ¿A partir de qué momento puede acceder al mercado de cambios para pagarlos y qué se necesita si quisiera precancelarlos antes del vencimiento?

**Respuesta del agente (íntegra):**

> Según la regulación del BCRA:
> 
> **Momento de acceso al mercado de cambios para pagar intereses:**
> El acceso al mercado de cambios para pagar intereses de deudas comerciales tiene lugar **a partir de la fecha de vencimiento del interés a pagar**.
> 
> **Para precancelar intereses antes del vencimiento:**
> Si desea precancelar los intereses antes de la fecha de vencimiento, se requiere **conformidad previa del BCRA**. Esta conformidad es necesaria para acceder al mercado de cambios para precancelar los servicios de intereses de deudas comerciales por importaciones de bienes y servicios, en casos distintos a VPU-RIGI.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: El acceso al mercado de cambios para pagar los intereses tiene lugar a partir de la fecha de vencimiento del interés a pagar.
- cita del gold: «3.3.2. El acceso al mercado de cambios tiene lugar a partir de la fecha de vencimiento del interés a pagar.»
- rep 1 [cumplido] fragmento: «El acceso al mercado de cambios para pagar intereses de deudas comerciales tiene lugar a partir de la fecha de vencimiento del interés a pagar.» — La respuesta reproduce fielmente el contenido del criterio, indicando que el acceso al mercado de cambios ocurre a partir de la fecha de vencimiento del interés a pagar, con los mismos sujetos y condiciones.
- rep 2 [cumplido] fragmento: «El acceso al mercado de cambios para pagar intereses de deudas comerciales tiene lugar a partir de la fecha de vencimiento del interés a pagar.» — La respuesta reproduce fielmente el contenido del criterio, indicando que el acceso al mercado de cambios ocurre a partir de la fecha de vencimiento del interés a pagar.
- rep 3 [cumplido] fragmento: «El acceso al mercado de cambios para pagar intereses de deudas comerciales tiene lugar a partir de la fecha de vencimiento del interés a pagar.» — La respuesta reproduce fielmente el contenido del criterio, indicando que el acceso al mercado de cambios ocurre a partir de la fecha de vencimiento del interés a pagar.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: Para precancelar los intereses antes del vencimiento se requiere la conformidad previa del BCRA.
- cita del gold: «En los restantes casos se requerirá la conformidad previa del BCRA para acceder al mercado de cambios para precancelar los servicios de intereses de deudas comerciales por importaciones de bienes y servicios.»
- rep 1 [cumplido] fragmento: «Si desea precancelar los intereses antes de la fecha de vencimiento, se requiere conformidad previa del BCRA. Esta conformidad es necesaria para acceder al mercado de cambios para precancelar los servicios de intereses de deudas comerciales por importaciones de bienes y servicios, en casos distintos a VPU-RIGI.» — La respuesta refleja fielmente el requisito de conformidad previa del BCRA para precancelar servicios de intereses de deudas comerciales por importaciones de bienes y servicios, coincidiendo con la cita normativa.
- rep 2 [cumplido] fragmento: «Si desea precancelar los intereses antes de la fecha de vencimiento, se requiere conformidad previa del BCRA. Esta conformidad es necesaria para acceder al mercado de cambios para precancelar los servicios de intereses de deudas comerciales por importaciones de bienes y servicios, en casos distintos a VPU-RIGI.» — La respuesta refleja correctamente que la conformidad previa del BCRA es el requisito para precancelar intereses de deudas comerciales por importaciones de bienes y servicios, en línea con la cita normativa.
- rep 3 [cumplido] fragmento: «Si desea precancelar los intereses antes de la fecha de vencimiento, se requiere conformidad previa del BCRA. Esta conformidad es necesaria para acceder al mercado de cambios para precancelar los servicios de intereses de deudas comerciales por importaciones de bienes y servicios, en casos distintos a VPU-RIGI.» — La respuesta refleja correctamente que la precancelación de intereses de deudas comerciales por importaciones requiere conformidad previa del BCRA, con los mismos sujetos y alcance que la cita normativa.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **dudoso** (['no_cumplido', 'dudoso', 'dudoso']) ⚠ no unánime
- criterio: El requisito de esperar al vencimiento no aplica si el cliente es un Vehículo de Proyecto Único (VPU) adherido al RIGI que concreta el pago en el marco del punto 14.2.1.
- cita del gold: «Este requisito no resultará aplicable si el cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que concreta el pago en el marco de lo previsto en el punto 14.2.1.»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta menciona la excepción VPU-RIGI solo de manera tangencial al referirse a 'casos distintos a VPU-RIGI', pero no explica que el requisito de esperar al vencimiento no aplica si el cliente es un VPU adherido al RIGI que concreta el pago en el marco del punto 14.2.1, que es el contenido específico exigido por el criterio.
- rep 2 [dudoso] fragmento: «en casos distintos a VPU-RIGI» — La respuesta menciona la excepción VPU-RIGI solo de forma tangencial y abreviada ('en casos distintos a VPU-RIGI'), sin explicitar que el requisito de esperar al vencimiento no aplica cuando el cliente es un Vehículo de Proyecto Único adherido al RIGI que concreta el pago en el marco del punto 14.2.1, lo que hace ambigua la cobertura del criterio.
- rep 3 [dudoso] fragmento: «en casos distintos a VPU-RIGI» — La respuesta menciona tangencialmente la excepción VPU-RIGI al señalar 'en casos distintos a VPU-RIGI', pero no desarrolla el contenido normativo del criterio: que el requisito de esperar al vencimiento no aplica si el cliente es un VPU adherido al RIGI que concreta el pago en el marco del punto 14.2.1. La mención es demasiado escueta para confirmar que refleja fielmente la excepción.
- pre-clasificación mecánica del par: **evidencia** (nulos=1/3, no_verbatim=0/3, fragmentos_distintos=2)

## U6-013 — humano: **correcto** · juez (mapping): **requiere_adjudicacion** [ADJUDICACIÓN]

**Pregunta:** Bajo el método simple de cobertura del riesgo de crédito con activos en garantía, ¿qué condiciones de plazo y de valuación debe cumplir la garantía para ser reconocida, y qué ponderador mínimo recibe la parte cubierta de la exposición?

**Respuesta del agente (íntegra):**

> Bajo el método simple de cobertura del riesgo de crédito con activos en garantía, la garantía debe cumplir las siguientes condiciones:
> 
> **Condiciones de Plazo:**
> - La cobertura del riesgo de crédito debe tener un plazo de vencimiento original de al menos un año, o un plazo residual superior a tres meses. No se reconocerá cobertura con plazo de vencimiento original inferior a un año o residual no mayor a tres meses.
> - No se permite descalce de plazos de vencimiento entre la exposición y el activo admitido como garantía bajo el método simple.
> 
> **Condiciones de Valuación:**
> - El activo recibido en garantía debe contar con una valuación a precios de mercado con una frecuencia mínima mensual.
> 
> **Ponderador Mínimo de la Parte Cubierta:**
> - La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20%, salvo lo dispuesto en excepciones específicas (punto 5.3.1.3).

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **sin_consenso** (['dudoso', 'cumplido', 'no_cumplido']) ⚠ no unánime
- criterio: Condición de plazo: la exposición debe estar cubierta durante todo el plazo de vencimiento contractual; no se admite el descalce de plazos de vencimiento.
- cita del gold: «Para que la CRC sea reconocida, la exposición deberá estar cubierta durante todo el plazo de vencimiento contractual (no se admitirá el descalce de plazos de vencimiento)»
- rep 1 [dudoso] fragmento: «No se permite descalce de plazos de vencimiento entre la exposición y el activo admitido como garantía bajo el método simple.» — La respuesta menciona la prohibición de descalce de plazos, pero no recoge el requisito específico de que la exposición debe estar cubierta durante todo el plazo de vencimiento contractual; además, agrega condiciones sobre plazo mínimo de un año o residual superior a tres meses que no forman parte del criterio evaluado, lo que genera ambigüedad sobre si la condición normativa exacta está reflejada.
- rep 2 [cumplido] fragmento: «No se permite descalce de plazos de vencimiento entre la exposición y el activo admitido como garantía bajo el método simple.» — La respuesta recoge la prohibición del descalce de plazos de vencimiento. Sin embargo, omite la condición de que la exposición debe estar cubierta durante todo el plazo de vencimiento contractual; aun así, la prohibición del descalce es el núcleo normativo del criterio y está presente, por lo que se considera cumplido.
- rep 3 [no_cumplido] fragmento: «La cobertura del riesgo de crédito debe tener un plazo de vencimiento original de al menos un año, o un plazo residual superior a tres meses. No se reconocerá cobertura con plazo de vencimiento original inferior a un año o residual no mayor a tres meses.» — La norma exige que la exposición esté cubierta durante todo el plazo de vencimiento contractual, sin admitir descalce de plazos. La respuesta introduce condiciones de plazo mínimo (un año de vencimiento original o tres meses residual) que no figuran en el criterio y que contradicen la regla normativa, que no establece umbrales de plazo sino la cobertura total del plazo contractual.
- pre-clasificación mecánica del par: **evidencia** (nulos=0/3, no_verbatim=0/3, fragmentos_distintos=2)

### criterio 2 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Condición de valuación: el activo recibido en garantía debe estar entre los listados en el punto 5.3.1.2. y contar con valuación a precios de mercado con frecuencia mínima mensual.
- cita del gold: «el activo recibido en garantía se limitará a aquellos listados en el punto 5.3.1.2. y contar con una valuación a precios de mercado con una frecuencia mínima mensual.»
- rep 1 [no_cumplido] fragmento: «El activo recibido en garantía debe contar con una valuación a precios de mercado con una frecuencia mínima mensual.» — La respuesta recoge la condición de valuación a precios de mercado con frecuencia mínima mensual, pero omite el requisito de que el activo debe estar limitado a aquellos listados en el punto 5.3.1.2., que es parte integral de la condición normativa exigida por el criterio.
- rep 2 [no_cumplido] fragmento: «El activo recibido en garantía debe contar con una valuación a precios de mercado con una frecuencia mínima mensual.» — La respuesta menciona la valuación a precios de mercado con frecuencia mínima mensual, pero omite el requisito de que el activo debe estar entre los listados en el punto 5.3.1.2., que es una condición exigida expresamente por la norma y el criterio.
- rep 3 [no_cumplido] fragmento: «El activo recibido en garantía debe contar con una valuación a precios de mercado con una frecuencia mínima mensual.» — La respuesta recoge la condición de valuación a precios de mercado con frecuencia mínima mensual, pero omite el requisito de que el activo se limite a aquellos listados en el punto 5.3.1.2., que es parte integral de la condición normativa.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La parte cubierta de la exposición recibe el ponderador de riesgo del activo recibido en garantía, sujeto a un mínimo del 20% (salvo las excepciones del punto 5.3.1.3.).
- cita del gold: «La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% –salvo lo dispuesto en el punto 5.3.1.3.–. A la parte no cubierta se le aplicará el ponderador de riesgo que le corresponda según el tipo de exposición de que se trate.»
- rep 1 [cumplido] fragmento: «La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20%, salvo lo dispuesto en excepciones específicas (punto 5.3.1.3.).» — La respuesta reproduce fielmente el contenido normativo del criterio: ponderador del activo en garantía con mínimo del 20% y la salvedad del punto 5.3.1.3.
- rep 2 [cumplido] fragmento: «La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20%, salvo lo dispuesto en excepciones específicas (punto 5.3.1.3.).» — La respuesta reproduce fielmente el ponderador mínimo del 20% para la parte cubierta y la remisión a las excepciones del punto 5.3.1.3., coincidiendo con la cita normativa.
- rep 3 [cumplido] fragmento: «La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20%, salvo lo dispuesto en excepciones específicas (punto 5.3.1.3.).» — La respuesta refleja fielmente el contenido normativo: ponderador del activo en garantía con mínimo del 20% y la salvedad del punto 5.3.1.3., coincidiendo con la cita textual.
- pre-clasificación mecánica del par: **evidencia** (nulos=0/3, no_verbatim=3/3, fragmentos_distintos=1)

## U6-001 — humano: **incorrecto** · juez (mapping): **requiere_adjudicacion** [ADJUDICACIÓN]

**Pregunta:** Una empresa cobró una exportación y tiene los fondos en su cuenta en moneda extranjera en un banco local. ¿Bajo qué condiciones puede aplicar esas divisas directamente a un pago que tendría acceso al mercado de cambios, sin liquidarlas previamente a pesos, y cómo juegan los límites mensuales del concepto en ese mecanismo?

**Respuesta del agente (íntegra):**

> Una empresa que cobró una exportación y tiene fondos en moneda extranjera en una cuenta local puede aplicar esas divisas directamente a un pago con acceso al mercado de cambios sin liquidarlas previamente a pesos, bajo el mecanismo de 'Aplicación de divisas de cobros de exportaciones' (Punto 7.3). Las condiciones son: (1) debe certificarse que los bienes exportados o las divisas cobradas por ellos fueron utilizados para cancelar capital, intereses y/o gastos de financiamiento, pagar utilidades y dividendos, o concretar repatriación de inversión directa; (2) la entidad debe contar con una certificación de aplicación emitida por la encargada del seguimiento de la operación a cuya cancelación se aplicaron las divisas; (3) debe solicitarse un número de identificación APX; (4) debe nominarse una entidad única para el seguimiento. Respecto a los límites mensuales, la regulación establece un límite mensual de compra por concepto de USD 200 (dólares estadounidenses doscientos) en el mes calendario, en el conjunto de las entidades y por el conjunto de los conceptos señalados. La fecha de aplicación de las divisas estará dada por la fecha de efectiva cancelación del concepto al cual se aplicaron las divisas de cobros de exportaciones.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: El ejercicio de la excepción (aplicación directa de las divisas sin liquidarlas) debe efectuarse dentro del plazo aplicable a la operación para la liquidación de los fondos en el mercado de cambios.
- cita del gold: «2.7.1. El ejercicio de la excepción se efectúe dentro del plazo para la liquidación de los fondos en el mercado de cambios que sea aplicable a la operación.»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento que el ejercicio de la excepción debe efectuarse dentro del plazo aplicable a la operación para la liquidación de los fondos en el mercado de cambios. Este requisito está completamente ausente.
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento que el ejercicio de la excepción debe efectuarse dentro del plazo aplicable a la operación para la liquidación de los fondos en el mercado de cambios. Este requisito está completamente ausente.
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento que el ejercicio de la excepción debe efectuarse dentro del plazo aplicable a la operación para la liquidación de los fondos en el mercado de cambios. Este requisito está completamente ausente.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 2 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Los fondos deben haber permanecido, hasta el ejercicio de la excepción, acreditados en cuentas en moneda extranjera de titularidad del cliente en entidades financieras locales (o, si fueron percibidos en el exterior, ingresados a nombre del cliente en cuentas de corresponsalía de una entidad local).
- cita del gold: «2.7.2. Los fondos hayan permanecido hasta el ejercicio de la excepción acreditados en cuentas en moneda extranjera de titularidad del cliente en entidades financieras locales o, en el caso de fondos percibidos en el exterior, ingresados a nombre del cliente en cuentas de corresponsalía de una entidad local.»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona el requisito de que los fondos hayan permanecido acreditados en cuentas en moneda extranjera de titularidad del cliente en entidades financieras locales (o ingresados en cuentas de corresponsalía) hasta el ejercicio de la excepción. Este requisito está completamente ausente.
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona el requisito de que los fondos hayan permanecido acreditados en cuentas en moneda extranjera de titularidad del cliente en entidades financieras locales (o ingresados en cuentas de corresponsalía) hasta el ejercicio de la excepción. Este requisito está completamente ausente.
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona el requisito de que los fondos hayan permanecido acreditados en cuentas en moneda extranjera de titularidad del cliente en entidades financieras locales (o ingresados en cuentas de corresponsalía) hasta el ejercicio de la excepción. Este requisito está completamente ausente.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 3 → modal **dudoso** (['dudoso', 'dudoso', 'dudoso'])
- criterio: Los fondos deben aplicarse de manera simultánea con el ejercicio de la excepción a operaciones por las que la normativa cambiaria permite el acceso al mercado de cambios contra moneda local, respetando los límites previstos para cada concepto involucrado.
- cita del gold: «2.7.3. Los fondos en moneda extranjera sean aplicados de manera simultánea con el ejercicio de la excepción a operaciones por las cuales la normativa cambiaria vigente permite el acceso al mercado de cambios contra moneda local, considerando los límites previstos para cada concepto involucrado.»
- rep 1 [dudoso] fragmento: «los fondos en moneda extranjera sean aplicados de manera simultánea con el ejercicio de la excepción a operaciones por las cuales la normativa cambiaria vigente permite el acceso al mercado de cambios contra moneda local, considerando los límites previstos para cada concepto involucrado» — La respuesta menciona que el mecanismo aplica a pagos 'con acceso al mercado de cambios' y alude a límites por concepto, pero no menciona explícitamente la simultaneidad ni reproduce con claridad suficiente todos los elementos del criterio (simultáneo + acceso al MLC + límites por concepto), lo que genera ambigüedad sobre si el criterio se cumple fielmente.
- rep 2 [dudoso] fragmento: «los fondos en moneda extranjera sean aplicados de manera simultánea con el ejercicio de la excepción a operaciones por las cuales la normativa cambiaria vigente permite el acceso al mercado de cambios contra moneda local, considerando los límites previstos para cada concepto involucrado» — La respuesta menciona que los fondos pueden aplicarse directamente a un pago con acceso al mercado de cambios y refiere a límites por concepto, pero no menciona explícitamente la simultaneidad ni reproduce con claridad suficiente todos los elementos del criterio (acceso al mercado contra moneda local, límites por concepto involucrado), lo que genera ambigüedad sobre si el criterio está plenamente cubierto.
- rep 3 [dudoso] fragmento: «los fondos en moneda extranjera sean aplicados de manera simultánea con el ejercicio de la excepción a operaciones por las cuales la normativa cambiaria vigente permite el acceso al mercado de cambios contra moneda local, considerando los límites previstos para cada concepto involucrado» — La respuesta menciona que la empresa puede aplicar divisas directamente a un pago con acceso al mercado de cambios y alude a límites por concepto, pero no explicita el requisito de simultaneidad ni la condición de que sean operaciones que permiten acceso al mercado contra moneda local; la referencia a límites por concepto es tangencial y no claramente vinculada a este requisito.
- pre-clasificación mecánica del par: **evidencia** (nulos=0/3, no_verbatim=3/3, fragmentos_distintos=1)

### criterio 4 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La utilización del mecanismo debe resultar neutral en materia fiscal.
- cita del gold: «2.7.4. La utilización de este mecanismo deberá resultar neutral en materia fiscal.»
- rep 1 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento el requisito de neutralidad fiscal en la utilización del mecanismo. Este requisito está completamente ausente.
- rep 2 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento el requisito de neutralidad fiscal en la utilización del mecanismo. Este requisito está completamente ausente.
- rep 3 [no_cumplido] fragmento: null (ausencia) — La respuesta no menciona en ningún momento el requisito de neutralidad fiscal en la utilización del mecanismo. Este requisito está completamente ausente.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 5 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Respecto de los límites mensuales: la operación se registra con dos boletos sin movimiento de pesos (compra y venta) y el monto aplicado bajo este mecanismo se computa a los efectos de los límites mensuales aplicables al concepto; además debe contarse con una declaración jurada del cliente en la que deja constancia de que conoce que los fondos se computan para los límites del concepto de venta de cambio y que no los excede.
- cita del gold: «A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin movimiento de pesos, por los conceptos de compra y venta que correspondan, computándose el monto por el cual se utiliza este mecanismo a los efectos de los límites mensuales que pudieran ser aplicables según el caso. En todos los casos se deberá contar con una declaración jurada del cliente en la que deja constancia de tener conocimiento de que los fondos que se aplican bajo esta modalidad serán computados a los efectos del cálculo de los límites que normativamente correspondan al concepto de venta de cambio que corresponda y que no los excede.»
- rep 1 [no_cumplido] fragmento: «la regulación establece un límite mensual de compra por concepto de USD 200 (dólares estadounidenses doscientos) en el mes calendario, en el conjunto de las entidades y por el conjunto de los conceptos señalados» — La respuesta menciona un límite mensual de USD 200 que no corresponde al contenido del criterio, y omite completamente los dos elementos centrales exigidos: la confección de dos boletos sin movimiento de pesos (compra y venta) y la declaración jurada del cliente sobre el cómputo de los fondos hacia los límites del concepto de venta.
- rep 2 [no_cumplido] fragmento: «la regulación establece un límite mensual de compra por concepto de USD 200 (dólares estadounidenses doscientos) en el mes calendario, en el conjunto de las entidades y por el conjunto de los conceptos señalados» — La respuesta menciona un límite mensual de USD 200 que no corresponde al contenido del criterio, y no menciona los dos boletos sin movimiento de pesos ni la declaración jurada del cliente sobre el cómputo de los fondos para los límites del concepto de venta de cambio, que son los elementos centrales exigidos por el criterio.
- rep 3 [no_cumplido] fragmento: «la regulación establece un límite mensual de compra por concepto de USD 200 (dólares estadounidenses doscientos) en el mes calendario, en el conjunto de las entidades y por el conjunto de los conceptos señalados» — La respuesta menciona un límite mensual de USD 200 que no corresponde al contenido del criterio (que trata sobre dos boletos sin movimiento de pesos, cómputo del monto a los límites del concepto y declaración jurada del cliente); no menciona los boletos sin movimiento de pesos, ni el cómputo específico a los límites del concepto de venta, ni la declaración jurada requerida.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

## U6-022 — humano: **parcial** · juez (mapping): **requiere_adjudicacion** [ADJUDICACIÓN]

**Pregunta:** En los modelos de información complementaria del cálculo del riesgo de tasa de interés en la cartera de inversión, ¿con qué apertura por monedas se presentan los cuadros y qué dimensiones —escenarios, bandas temporales, tipo de tasa— se utilizan para informar los activos y pasivos susceptibles de estandarización?

**Respuesta del agente (íntegra):**

> En los modelos de información complementaria del cálculo del riesgo de tasa de interés en la cartera de inversión, los cuadros se presentan con apertura por las siguientes monedas: pesos (cuadros 11.2.1 a) y 11.2.2 a)), pesos actualizables y dólares estadounidenses (cuadros 11.2.1 b) y 11.2.2 a)), siempre que se trate de exposiciones relevantes (superiores al 5% de los activos o pasivos de la cartera de inversión).
> 
> Las dimensiones utilizadas para informar los activos y pasivos susceptibles e no susceptibles de estandarización son: (1) Bandas temporales: clasificación por bandas temporales (0 a 19); (2) Escenarios: escenarios base y de perturbación; (3) Tipo de tasa: pesos no actualizables, pesos actualizables y dólares estadounidenses.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Los cuadros se abren por moneda: el cuadro 11.2.1. a) para posiciones en pesos (no actualizables y actualizables) y el cuadro 11.2.1. b) para posiciones en dólares estadounidenses.
- cita del gold: «La información se referirá a posiciones en pesos -cuadros 11.2.1 a) y 11.2.2 a)- y en dólares estadounidenses -cuadros 11.2.1 b) y 11.2.2 b)-, siempre que se trate de exposiciones relevantes (superiores al 5 % de los activos o pasivos de la cartera de inversión), considerando lo indicado en el punto 1.2.»
- rep 1 [no_cumplido] fragmento: «pesos (cuadros 11.2.1 a) y 11.2.2 a)), pesos actualizables y dólares estadounidenses (cuadros 11.2.1 b) y 11.2.2 a))» — La respuesta asigna incorrectamente los cuadros: indica que el cuadro 11.2.1 b) corresponde a 'pesos actualizables y dólares estadounidenses' y repite el cuadro 11.2.2 a) para dólares, cuando la norma establece que el cuadro 11.2.1 a) es para posiciones en pesos y el 11.2.1 b) para dólares estadounidenses, con el cuadro 11.2.2 b) para dólares.
- rep 2 [no_cumplido] fragmento: «pesos (cuadros 11.2.1 a) y 11.2.2 a)), pesos actualizables y dólares estadounidenses (cuadros 11.2.1 b) y 11.2.2 a))» — La respuesta asigna incorrectamente los cuadros: indica que el cuadro 11.2.1 b) corresponde a 'pesos actualizables y dólares estadounidenses' y repite el cuadro 11.2.2 a) para ambas monedas, cuando la norma establece que el cuadro 11.2.1 b) es exclusivamente para dólares estadounidenses y el cuadro 11.2.2 b) (no 11.2.2 a)) corresponde a esa moneda.
- rep 3 [no_cumplido] fragmento: «pesos (cuadros 11.2.1 a) y 11.2.2 a)), pesos actualizables y dólares estadounidenses (cuadros 11.2.1 b) y 11.2.2 a))» — La respuesta asigna incorrectamente los cuadros: indica que el cuadro 11.2.1 b) corresponde a 'pesos actualizables y dólares estadounidenses' y repite el cuadro 11.2.2 a), cuando la norma establece que el cuadro 11.2.1 a) es para posiciones en pesos y el 11.2.1 b) para dólares estadounidenses, con el cuadro 11.2.2 b) para dólares.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Los activos susceptibles de estandarización se informan abiertos por tipo de tasa: a tasa de interés fija, a tasa variable, a tasa fija con opciones automáticas implícitas y a tasa variable con opciones automáticas implícitas.
- cita del gold: «Activos susceptibles de estandarización a tasa de interés fija Activos susceptibles de estandarización a tasa de interés variable Activos susceptibles de estandarización a tasa de interés fija con opciones automáticas implícitas Activos susceptibles de estandarización a tasa de interés variable con opciones automáticas implícitas»
- rep 1 [no_cumplido] fragmento: «Tipo de tasa: pesos no actualizables, pesos actualizables y dólares estadounidenses.» — La respuesta describe el tipo de tasa como monedas (pesos no actualizables, pesos actualizables, dólares), en lugar de la apertura normativa que exige: tasa fija, tasa variable, tasa fija con opciones automáticas implícitas y tasa variable con opciones automáticas implícitas.
- rep 2 [no_cumplido] fragmento: «Tipo de tasa: pesos no actualizables, pesos actualizables y dólares estadounidenses.» — La respuesta describe el tipo de tasa como las monedas (pesos no actualizables, pesos actualizables, dólares), en lugar de la apertura normativa que exige distinguir tasa fija, tasa variable, tasa fija con opciones automáticas implícitas y tasa variable con opciones automáticas implícitas para los activos susceptibles de estandarización.
- rep 3 [no_cumplido] fragmento: «Tipo de tasa: pesos no actualizables, pesos actualizables y dólares estadounidenses.» — La respuesta describe el tipo de tasa como monedas (pesos no actualizables, pesos actualizables, dólares), en lugar de la apertura normativa que exige: tasa fija, tasa variable, tasa fija con opciones automáticas implícitas y tasa variable con opciones automáticas implícitas.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Los pasivos susceptibles de estandarización se informan con la misma apertura por tipo de tasa (fija, variable, fija con opciones automáticas implícitas y variable con opciones automáticas implícitas).
- cita del gold: «Pasivos susceptibles de estandarización a tasa de interés fija Pasivos susceptibles de estandarización a tasa de interés variable Pasivos susceptibles de estandarización a tasa de interés fija con opciones automáticas implícitas Pasivos susceptibles de estandarización a tasa de interés variable con opciones automáticas implícitas»
- rep 1 [no_cumplido] fragmento: «Tipo de tasa: pesos no actualizables, pesos actualizables y dólares estadounidenses.» — Al igual que para los activos, la respuesta no menciona la apertura de los pasivos susceptibles de estandarización por tipo de tasa (fija, variable, fija con opciones automáticas implícitas, variable con opciones automáticas implícitas) exigida por la norma.
- rep 2 [no_cumplido] fragmento: «Tipo de tasa: pesos no actualizables, pesos actualizables y dólares estadounidenses.» — Al igual que para los activos, la respuesta no menciona la apertura por tipo de tasa (fija, variable, fija con opciones automáticas implícitas, variable con opciones automáticas implícitas) para los pasivos susceptibles de estandarización.
- rep 3 [no_cumplido] fragmento: «Tipo de tasa: pesos no actualizables, pesos actualizables y dólares estadounidenses.» — Al igual que para los activos, la respuesta no menciona la apertura de los pasivos susceptibles de estandarización por tasa fija, variable, fija con opciones automáticas implícitas y variable con opciones automáticas implícitas.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 4 → modal **dudoso** (['dudoso', 'dudoso', 'dudoso'])
- criterio: Los flujos se asignan a 19 bandas temporales predefinidas (o a sus puntos medios) para cada escenario de perturbación de tasas de interés.
- cita del gold: «Los citados flujos de fondos nocionales futuros se asignarán a 19 bandas temporales predefinidas o sus puntos medios (tabla 1) para cada escenario de perturbación de tasas de interés (tabla 2).»
- rep 1 [dudoso] fragmento: «Bandas temporales: clasificación por bandas temporales (0 a 19)» — La respuesta menciona 19 bandas temporales y escenarios de perturbación por separado, lo que es parcialmente compatible con la norma, pero no indica explícitamente que los flujos se asignan a esas bandas o sus puntos medios para cada escenario de perturbación, dejando ambigua la relación entre ambas dimensiones.
- rep 2 [dudoso] fragmento: «Bandas temporales: clasificación por bandas temporales (0 a 19)» — La respuesta menciona bandas temporales de 0 a 19, lo que es compatible con las 19 bandas predefinidas de la norma, pero no menciona la asignación a puntos medios ni la vinculación explícita a cada escenario de perturbación de tasas de interés, dejando el cumplimiento parcialmente ambiguo.
- rep 3 [dudoso] fragmento: «Bandas temporales: clasificación por bandas temporales (0 a 19)» — La respuesta menciona 19 bandas temporales y escenarios de perturbación por separado, lo que es parcialmente compatible con la norma, pero no indica explícitamente que los flujos se asignan a esas bandas o sus puntos medios para cada escenario de perturbación, dejando ambigua la relación entre ambas dimensiones.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 5 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Los escenarios previstos son 0 a 6, y en la banda 0 se informan los saldos a fin del último mes del trimestre.
- cita del gold: «Deberán informar los flujos asignados a todas las bandas o puntos medios para cada uno de los escenarios previstos (0 a 6). En la banda 0 (cero) se informarán los saldos a fin del último mes del trimestre.»
- rep 1 [no_cumplido] fragmento: «Escenarios: escenarios base y de perturbación» — La respuesta menciona genéricamente 'escenarios base y de perturbación' pero no especifica que los escenarios son 0 a 6 ni que en la banda 0 se informan los saldos a fin del último mes del trimestre, ambos elementos exigidos por la norma.
- rep 2 [no_cumplido] fragmento: «Escenarios: escenarios base y de perturbación» — La respuesta solo menciona 'escenarios base y de perturbación' de forma genérica, sin especificar que los escenarios son 0 a 6 ni que en la banda 0 se informan los saldos a fin del último mes del trimestre, como exige la norma.
- rep 3 [no_cumplido] fragmento: «Escenarios: escenarios base y de perturbación» — La respuesta menciona genéricamente 'escenarios base y de perturbación' pero no especifica que los escenarios son 0 a 6 ni que en la banda 0 se informan los saldos a fin del último mes del trimestre, ambos elementos exigidos por el criterio.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))
