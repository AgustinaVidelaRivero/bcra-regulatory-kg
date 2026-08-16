# Reporte de desacuerdos y adjudicaciones — calibración juez EV2 v1 sobre U6 (fuente respuestas: app)

Prompt sha256: `fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455`
Orden: semilla `juez-calibracion-v1`, N=3

## Resumen

- Preguntas: 25 — acuerdo 16 · desacuerdo 6 · requiere_adjudicacion 3
- Acuerdo sobre las decididas: 16/22
- Matriz (humano → juez): correcto→correcto: 1, correcto→parcial: 5, correcto→requiere_adjudicacion: 1, incorrecto→incorrecto: 3, parcial→incorrecto: 1, parcial→parcial: 12, parcial→requiere_adjudicacion: 2
- Proxy por criterio: correcta→todos cumplido 12/21; incorrecta→ninguno cumplido 13/13
- No-determinismo: pares unánimes 91/92; modales {'no_cumplido': 55, 'cumplido': 33, 'dudoso': 4}; todos los veredictos {'no_cumplido': 165, 'cumplido': 98, 'dudoso': 13}
- Fragmentos (276): {'verbatim': 155, 'null': 109, 'no_verbatim': 9, 'fuga_gold': 3} — detalle no-verbatim/fuga_gold: U6-011 c1 r1 [no_cumplido] no_verbatim; U6-011 c1 r2 [no_cumplido] no_verbatim; U6-011 c1 r3 [no_cumplido] no_verbatim; U6-019 c1 r1 [cumplido] fuga_gold; U6-019 c1 r2 [cumplido] fuga_gold; U6-019 c1 r3 [cumplido] fuga_gold; U6-013 c3 r1 [cumplido] no_verbatim; U6-013 c3 r2 [cumplido] no_verbatim; U6-013 c3 r3 [cumplido] no_verbatim; U6-015 c4 r1 [cumplido] no_verbatim; U6-015 c4 r2 [cumplido] no_verbatim; U6-015 c4 r3 [cumplido] no_verbatim
- Clasificación auxiliar modal vs flag respondible: U6-005:contenido/flag=False; U6-012:abstencion/flag=False; U6-019:contenido/flag=False; U6-001:contenido/flag=False

---

# A. Desacuerdos (juez decidió distinto del humano)

## U6-021 — humano: **correcto** · juez (mapping): **parcial** [DESACUERDO]

**Pregunta:** Al informar la exigencia por riesgo de mercado, ¿con los valores de qué fecha se determina el total, y cómo debe identificarse por moneda la partida de exigencia por riesgo general de tasa de interés?

**Respuesta del agente (íntegra):**

> Al informar la exigencia por riesgo de mercado, el total se determina con los valores que se registren al último día del período de información (n). Según las normas, se reemplazarán las dos últimas posiciones de cada partida de exigencia por el último día del período que corresponda (ejemplo, xx = 31).
> 
> Respecto a cómo debe identificarse por moneda la partida de exigencia por riesgo general de tasa de interés: la determinación de esta exigencia se efectuará por cada moneda, identificándose la presente partida según su moneda de origen de acuerdo con la codificación prevista en el Sistema Centralizado de requerimientos informativos (SISCEN), tabla T0003, de la que se excluirán aquellas monedas que no estén referenciadas con el código SWIFT.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La exigencia por riesgo de mercado se determina con los valores registrados al último día del período de información (n).
- cita del gold: «4.1.1.1. La exigencia por riesgo de mercado se determinará con los valores que se registren al último día del período de información (n), y el total surgirá de la siguiente suma:»
- rep 1 [cumplido] fragmento (verbatim): «el total se determina con los valores que se registren al último día del período de información (n)» — La respuesta reproduce fielmente el contenido normativo del criterio, indicando que la exigencia se determina con los valores del último día del período de información (n).
- rep 2 [cumplido] fragmento (verbatim): «el total se determina con los valores que se registren al último día del período de información (n)» — La respuesta reproduce fielmente el contenido normativo del criterio, indicando que la exigencia se determina con los valores del último día del período de información (n).
- rep 3 [cumplido] fragmento (verbatim): «el total se determina con los valores que se registren al último día del período de información (n)» — La respuesta reproduce fielmente el contenido normativo del criterio, indicando que la exigencia se determina con los valores del último día del período de información (n).
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La exigencia por riesgo general de tasa de interés (código 311200/xx) se determina por cada moneda, y la partida se identifica según su moneda de origen con la codificación de la tabla T0003 del SISCEN, excluidas las monedas no referenciadas con código SWIFT.
- cita del gold: «La determinación de esta exigencia se efectuará por cada moneda, a cuyos efectos la presente partida se identificará según su moneda de origen de acuerdo con la codificación prevista en el Sistema Centralizado de requerimientos informativos (SISCEN), tabla T0003, de la que se excluirán aquellas que no estén referenciadas con el código SWIFT.»
- rep 1 [cumplido] fragmento (verbatim): «la determinación de esta exigencia se efectuará por cada moneda, identificándose la presente partida según su moneda de origen de acuerdo con la codificación prevista en el Sistema Centralizado de requerimientos informativos (SISCEN), tabla T0003, de la que se excluirán aquellas monedas que no estén referenciadas con el código SWIFT.» — La respuesta reproduce casi textualmente el contenido normativo del criterio, incluyendo la determinación por moneda, la identificación según moneda de origen, la tabla T0003 del SISCEN y la exclusión de monedas sin código SWIFT.
- rep 2 [cumplido] fragmento (verbatim): «la determinación de esta exigencia se efectuará por cada moneda, identificándose la presente partida según su moneda de origen de acuerdo con la codificación prevista en el Sistema Centralizado de requerimientos informativos (SISCEN), tabla T0003, de la que se excluirán aquellas monedas que no estén referenciadas con el código SWIFT.» — La respuesta reproduce casi textualmente el contenido normativo del criterio, incluyendo la determinación por moneda, la identificación según moneda de origen, la tabla T0003 del SISCEN y la exclusión de monedas sin código SWIFT.
- rep 3 [cumplido] fragmento (verbatim): «la determinación de esta exigencia se efectuará por cada moneda, identificándose la presente partida según su moneda de origen de acuerdo con la codificación prevista en el Sistema Centralizado de requerimientos informativos (SISCEN), tabla T0003, de la que se excluirán aquellas monedas que no estén referenciadas con el código SWIFT.» — La respuesta reproduce casi textualmente el contenido normativo del criterio, incluyendo la determinación por moneda, la identificación según moneda de origen, la tabla T0003 del SISCEN y la exclusión de monedas sin código SWIFT.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Las monedas residuales, de corresponder, se identifican con el código de moneda 9999.
- cita del gold: «De corresponder, las monedas residuales (puntos 6.2.2.2. y 6.2.2.7. de las normas sobre “Capitales mínimos de las entidades financieras”) se identificarán con código de moneda 9999.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento que las monedas residuales se identifican con el código 9999, ni hace referencia alguna a monedas residuales.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la identificación de monedas residuales con el código 9999, por lo que el contenido normativo del criterio está ausente.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento que las monedas residuales se identifican con el código 9999, ni hace referencia a las monedas residuales.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

## U6-002 — humano: **correcto** · juez (mapping): **parcial** [DESACUERDO]

**Pregunta:** Una sociedad local quiere girar dividendos a sus accionistas del exterior. ¿Qué debe verificar el banco respecto de los balances de la empresa y del monto aprobado por la asamblea antes de dar curso a la transferencia?

**Respuesta del agente (íntegra):**

> Antes de dar curso a una transferencia de dividendos al exterior, el banco debe verificar dos requisitos principales:
> 
> 1. **Balances cerrados y auditados**: Las utilidades y dividendos deben corresponder a balances cerrados y auditados.
> 
> 2. **Monto aprobado por asamblea**: El monto total abonado por concepto de utilidades y dividendos a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: Las utilidades y dividendos a girar deben corresponder a balances cerrados y auditados.
- cita del gold: «3.4.1. Las utilidades y dividendos correspondan a balances cerrados y auditados.»
- rep 1 [cumplido] fragmento (verbatim): «Las utilidades y dividendos deben corresponder a balances cerrados y auditados.» — La respuesta reproduce fielmente el contenido del criterio, indicando que las utilidades y dividendos deben corresponder a balances cerrados y auditados, en línea exacta con la cita normativa.
- rep 2 [cumplido] fragmento (verbatim): «Las utilidades y dividendos deben corresponder a balances cerrados y auditados.» — La respuesta reproduce fielmente el contenido del criterio, indicando que las utilidades y dividendos deben corresponder a balances cerrados y auditados, en línea exacta con la cita normativa.
- rep 3 [cumplido] fragmento (verbatim): «Las utilidades y dividendos deben corresponder a balances cerrados y auditados.» — La respuesta reproduce fielmente el contenido del criterio, indicando que las utilidades y dividendos deben corresponder a balances cerrados y auditados, en línea exacta con la cita normativa.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: El monto total abonado por este concepto a accionistas no residentes, incluido el pago que se solicita, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.
- cita del gold: «3.4.2. El monto total abonado por este concepto a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no supere el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.»
- rep 1 [cumplido] fragmento (verbatim): «El monto total abonado por concepto de utilidades y dividendos a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.» — La respuesta reproduce con equivalencia normativa completa el criterio, incluyendo todos los elementos relevantes: monto total, accionistas no residentes, pago en curso, límite en moneda local y distribución por asamblea.
- rep 2 [cumplido] fragmento (verbatim): «El monto total abonado por concepto de utilidades y dividendos a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.» — La respuesta reproduce con equivalencia normativa completa el criterio, incluyendo todos los elementos relevantes: monto total abonado, accionistas no residentes, inclusión del pago solicitado, límite en moneda local y distribución por asamblea.
- rep 3 [cumplido] fragmento (verbatim): «El monto total abonado por concepto de utilidades y dividendos a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.» — La respuesta reproduce con equivalencia normativa completa el criterio, incluyendo todos los elementos relevantes: monto total, accionistas no residentes, pago en curso, límite en moneda local y distribución por asamblea.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La entidad debe contar con una declaración jurada firmada por el representante legal de la empresa residente o un apoderado con facultades suficientes.
- cita del gold: «La entidad deberá contar con una declaración jurada firmada por el representante legal de la empresa residente o un apoderado con facultades suficientes para asumir este compromiso en nombre de la empresa.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la exigencia de contar con una declaración jurada firmada por el representante legal o apoderado con facultades suficientes.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la exigencia de contar con una declaración jurada firmada por el representante legal o apoderado con facultades suficientes; ese contenido está completamente ausente.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la exigencia de contar con una declaración jurada firmada por el representante legal o apoderado con facultades suficientes.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

## U6-017 — humano: **correcto** · juez (mapping): **parcial** [DESACUERDO]

**Pregunta:** ¿A partir de qué magnitud de financiaciones la clasificación de un deudor y el cálculo de sus previsiones requieren la aprobación previa del Directorio de la entidad, y qué mayoría se exige cuando se trata de clientes vinculados?

**Respuesta del agente (íntegra):**

> La clasificación de un deudor y el cálculo de sus previsiones requieren aprobación previa del Directorio o Consejo de Administración cuando las financiaciones excedan del 2,5% de la RPC (Responsabilidad Patrimonial Computable) de la entidad financiera del mes anterior. La aprobación debe ser por mayoría simple en los casos ordinarios, pero se exige una mayoría de dos tercios cuando se trata de clientes vinculados.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La aprobación previa del Directorio (o Consejo de Administración o autoridad equivalente) se requiere para la clasificación y el cálculo de previsiones por financiaciones que excedan el 2,5 % de la RPC de la entidad del mes anterior al que corresponda.
- cita del gold: «por financiaciones que excedan del 2,5 % de la RPC de la entidad financiera del mes anterior al que corresponda, deberán contar con la previa aprobación de los miembros del Directorio o Consejo de Administración»
- rep 1 [cumplido] fragmento (verbatim): «requieren aprobación previa del Directorio o Consejo de Administración cuando las financiaciones excedan del 2,5% de la RPC (Responsabilidad Patrimonial Computable) de la entidad financiera del mes anterior» — La respuesta reproduce fielmente el umbral del 2,5% de la RPC del mes anterior y la exigencia de aprobación previa del Directorio o Consejo de Administración, en línea con la cita normativa.
- rep 2 [cumplido] fragmento (verbatim): «requieren aprobación previa del Directorio o Consejo de Administración cuando las financiaciones excedan del 2,5% de la RPC (Responsabilidad Patrimonial Computable) de la entidad financiera del mes anterior» — La respuesta reproduce fielmente el umbral del 2,5% de la RPC del mes anterior y la exigencia de aprobación previa del Directorio o Consejo de Administración, en línea con la cita normativa.
- rep 3 [cumplido] fragmento (verbatim): «requieren aprobación previa del Directorio o Consejo de Administración cuando las financiaciones excedan del 2,5% de la RPC (Responsabilidad Patrimonial Computable) de la entidad financiera del mes anterior» — La respuesta reproduce fielmente el umbral del 2,5% de la RPC del mes anterior y la exigencia de aprobación previa del Directorio o Consejo de Administración, coincidiendo con la cita normativa.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La aprobación es por mayoría simple, y cuando se trata de clientes vinculados se exige dos tercios de la totalidad de los miembros.
- cita del gold: «–por mayoría simple o, cuando se trate de clientes vinculados, de dos tercios de la totalidad de los miembros– o autoridad equivalente de la entidad financiera prestamista.»
- rep 1 [cumplido] fragmento (verbatim): «La aprobación debe ser por mayoría simple en los casos ordinarios, pero se exige una mayoría de dos tercios cuando se trata de clientes vinculados.» — La respuesta refleja correctamente ambas mayorías exigidas por la norma: mayoría simple para el caso general y dos tercios para clientes vinculados, aunque omite el detalle de que los dos tercios se calculan sobre la totalidad de los miembros, lo cual no altera sustancialmente el contenido normativo exigido por el criterio.
- rep 2 [cumplido] fragmento (verbatim): «La aprobación debe ser por mayoría simple en los casos ordinarios, pero se exige una mayoría de dos tercios cuando se trata de clientes vinculados.» — La respuesta refleja correctamente ambas mayorías exigidas por la norma: mayoría simple para el caso general y dos tercios para clientes vinculados, aunque omite el detalle de que los dos tercios se calculan sobre la totalidad de los miembros, lo cual no altera sustancialmente el contenido normativo exigido por el criterio.
- rep 3 [cumplido] fragmento (verbatim): «La aprobación debe ser por mayoría simple en los casos ordinarios, pero se exige una mayoría de dos tercios cuando se trata de clientes vinculados.» — La respuesta refleja correctamente ambas mayorías exigidas por la norma: mayoría simple para el caso general y dos tercios para clientes vinculados, aunque omite el detalle de que los dos tercios son sobre la totalidad de los miembros, lo cual no altera sustancialmente el contenido normativo exigido por el criterio.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La conformidad debe referirse, con opinión fundada, tanto a la clasificación asignada a cada deudor como al nivel de las previsiones calculadas.
- cita del gold: «Dicha conformidad estará referida –con opinión fundada en todos los casos– tanto a la clasificación asignada a cada uno de los deudores comprendidos como al nivel de las previsiones calculadas.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento que la conformidad debe referirse, con opinión fundada, tanto a la clasificación asignada a cada deudor como al nivel de las previsiones calculadas.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento que la conformidad debe referirse, con opinión fundada, tanto a la clasificación asignada a cada deudor como al nivel de las previsiones calculadas.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento que la conformidad debe referirse, con opinión fundada, tanto a la clasificación asignada a cada deudor como al nivel de las previsiones calculadas.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

## U6-013 — humano: **correcto** · juez (mapping): **parcial** [DESACUERDO]

**Pregunta:** Bajo el método simple de cobertura del riesgo de crédito con activos en garantía, ¿qué condiciones de plazo y de valuación debe cumplir la garantía para ser reconocida, y qué ponderador mínimo recibe la parte cubierta de la exposición?

**Respuesta del agente (íntegra):**

> Bajo el método simple de cobertura del riesgo de crédito con activos en garantía, la garantía debe cumplir las siguientes condiciones: (1) Plazo: no se permite descalce de plazos de vencimiento; la exposición debe estar cubierta durante todo el plazo de vencimiento contractual. (2) Valuación: el activo recibido en garantía debe contar con una valuación a precios de mercado con una frecuencia mínima mensual. (3) Ponderador mínimo: la parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% (salvo excepciones previstas en el punto 5.3.1.3).

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: Condición de plazo: la exposición debe estar cubierta durante todo el plazo de vencimiento contractual; no se admite el descalce de plazos de vencimiento.
- cita del gold: «Para que la CRC sea reconocida, la exposición deberá estar cubierta durante todo el plazo de vencimiento contractual (no se admitirá el descalce de plazos de vencimiento)»
- rep 1 [cumplido] fragmento (verbatim): «la exposición debe estar cubierta durante todo el plazo de vencimiento contractual. (2) Valuación» — La respuesta reproduce fielmente la condición de plazo exigida por el criterio, incluyendo la prohibición de descalce de plazos.
- rep 2 [cumplido] fragmento (verbatim): «no se permite descalce de plazos de vencimiento; la exposición debe estar cubierta durante todo el plazo de vencimiento contractual» — La respuesta reproduce fielmente ambos elementos del criterio: la cobertura durante todo el plazo contractual y la no admisión del descalce de plazos.
- rep 3 [cumplido] fragmento (verbatim): «no se permite descalce de plazos de vencimiento; la exposición debe estar cubierta durante todo el plazo de vencimiento contractual» — La respuesta reproduce fielmente ambos elementos del criterio: la cobertura durante todo el plazo contractual y la prohibición del descalce de plazos.
- pre-clasificación mecánica del par: **evidencia** (nulos=0/3, no_verbatim=0/3, fragmentos_distintos=2)

### criterio 2 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Condición de valuación: el activo recibido en garantía debe estar entre los listados en el punto 5.3.1.2. y contar con valuación a precios de mercado con frecuencia mínima mensual.
- cita del gold: «el activo recibido en garantía se limitará a aquellos listados en el punto 5.3.1.2. y contar con una valuación a precios de mercado con una frecuencia mínima mensual.»
- rep 1 [no_cumplido] fragmento (verbatim): «el activo recibido en garantía debe contar con una valuación a precios de mercado con una frecuencia mínima mensual» — La respuesta menciona la valuación a precios de mercado con frecuencia mínima mensual, pero omite la condición de que el activo debe estar entre los listados en el punto 5.3.1.2., que es un requisito normativo exigido por el criterio.
- rep 2 [no_cumplido] fragmento (verbatim): «el activo recibido en garantía debe contar con una valuación a precios de mercado con una frecuencia mínima mensual» — La respuesta menciona la valuación a precios de mercado con frecuencia mínima mensual, pero omite la condición de que el activo debe estar limitado a los listados en el punto 5.3.1.2., que es un requisito exigido por el criterio.
- rep 3 [no_cumplido] fragmento (verbatim): «el activo recibido en garantía debe contar con una valuación a precios de mercado con una frecuencia mínima mensual» — La respuesta menciona la valuación a precios de mercado con frecuencia mínima mensual, pero omite la condición de que el activo debe estar limitado a los listados en el punto 5.3.1.2., que es un requisito exigido por el criterio.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La parte cubierta de la exposición recibe el ponderador de riesgo del activo recibido en garantía, sujeto a un mínimo del 20% (salvo las excepciones del punto 5.3.1.3.).
- cita del gold: «La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% –salvo lo dispuesto en el punto 5.3.1.3.–. A la parte no cubierta se le aplicará el ponderador de riesgo que le corresponda según el tipo de exposición de que se trate.»
- rep 1 [cumplido] fragmento (no_verbatim): «la parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% (salvo excepciones previstas en el punto 5.3.1.3.)» — La respuesta refleja fielmente el ponderador mínimo del 20% aplicable a la parte cubierta y la remisión a las excepciones del punto 5.3.1.3., en línea con la cita normativa.
- rep 2 [cumplido] fragmento (no_verbatim): «la parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% (salvo excepciones previstas en el punto 5.3.1.3.)» — La respuesta refleja fielmente el ponderador del activo en garantía, el mínimo del 20% y la salvedad del punto 5.3.1.3., coincidiendo con la cita normativa.
- rep 3 [cumplido] fragmento (no_verbatim): «la parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% (salvo excepciones previstas en el punto 5.3.1.3.)» — La respuesta refleja fielmente el ponderador mínimo del 20%, la referencia al activo en garantía y la salvedad del punto 5.3.1.3., coincidiendo con la cita normativa.
- pre-clasificación mecánica del par: **evidencia** (nulos=0/3, no_verbatim=3/3, fragmentos_distintos=1)

## U6-009 — humano: **parcial** · juez (mapping): **incorrecto** [DESACUERDO]

**Pregunta:** Para pagar al exterior una importación que ya cuenta con registro de ingreso aduanero bajo el SEPAIMPO, ¿qué documentación y verificaciones debe completar la entidad antes de dar acceso al mercado de cambios?

**Respuesta del agente (íntegra):**

> Para pagar al exterior una importación que ya cuenta con registro de ingreso aduanero bajo SEPAIMPO, la entidad debe completar las siguientes documentación y verificaciones antes de dar acceso al mercado de cambios:
> 
> 1. **Certificación de SEPAIMPO**: La entidad debe contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO).
> 
> 2. **Constancia del registro aduanero**: La entidad debe contar con constancia del registro aduanero del ingreso de bienes que originan el pago.
> 
> 3. **Convalidación en sistema online del BCRA**: La entidad deberá, al momento de dar acceso al mercado de cambios, contar con la convalidación de la situación de la operación en el sistema online implementado por el BCRA a tales efectos.
> 
> Estos son los requisitos principales que la entidad debe verificar y completar antes de otorgar acceso al mercado de cambios para realizar el pago de la importación.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La entidad debe certificar (como entidad de seguimiento de la oficialización, o contar con certificación de la entidad responsable) que cuenta con la constancia del registro aduanero del ingreso de los bienes, copia de la factura comercial emitida en el exterior a nombre del importador residente (con emisor, importador, cantidad y descripción de la mercadería, condición de venta y valor) y copia del Documento de Transporte.
- cita del gold: «i) Cuenta con constancia del registro aduanero del ingreso al país de los bienes que originan el pago a cancelarse. ii) Cuenta con copia de factura comercial emitida en el exterior a nombre del cliente residente en el país, que efectúa la compra al exterior, donde conste nombre y dirección del emisor, nombre del importador argentino, la cantidad y descripción de la mercadería, condición de venta y valor de la factura. iii) Cuenta con copia del Documento de Transporte (Conocimiento de Embarque – Carta de Porte – Guía Aérea).»
- rep 1 [no_cumplido] fragmento (verbatim): «La entidad debe contar con constancia del registro aduanero del ingreso de bienes que originan el pago.» — La respuesta menciona la constancia del registro aduanero, pero omite completamente los otros dos requisitos exigidos por el criterio: la copia de la factura comercial con todos sus elementos (nombre y dirección del emisor, nombre del importador, cantidad y descripción de la mercadería, condición de venta y valor) y la copia del Documento de Transporte.
- rep 2 [no_cumplido] fragmento (verbatim): «La entidad debe contar con constancia del registro aduanero del ingreso de bienes que originan el pago.» — La respuesta menciona la constancia del registro aduanero, pero omite completamente los otros dos requisitos exigidos por el criterio: la copia de la factura comercial con todos sus elementos (nombre y dirección del emisor, nombre del importador, cantidad y descripción de la mercadería, condición de venta y valor) y la copia del Documento de Transporte.
- rep 3 [no_cumplido] fragmento (verbatim): «La entidad debe contar con constancia del registro aduanero del ingreso de bienes que originan el pago.» — La respuesta menciona la constancia del registro aduanero, pero omite completamente los otros dos requisitos exigidos por el criterio: la copia de la factura comercial con todos sus elementos (nombre y dirección del emisor, nombre del importador, cantidad y descripción de la mercadería, condición de venta y valor) y la copia del Documento de Transporte.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Debe verificar que la información de la factura comercial y del Documento de Transporte sea consistente con los registros aduaneros, y que la documentación permita establecer la fecha de vencimiento de la obligación (o que no tiene vencimiento pactado).
- cita del gold: «iv) Que la información que surge de la factura comercial y del Documento de Transporte sea consistente con la que figura en los registros aduaneros, considerando las normas de declaración aduanera aplicables. v) Que la documentación presentada le permita establecer la fecha de vencimiento de la obligación con el exterior por parte del importador o, en su defecto, que la operación no tiene una fecha de vencimiento pactada.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la verificación de consistencia entre la factura comercial/Documento de Transporte y los registros aduaneros, ni la verificación de la fecha de vencimiento de la obligación con el exterior.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la verificación de consistencia entre la factura comercial/Documento de Transporte y los registros aduaneros, ni la verificación de la fecha de vencimiento de la obligación con el exterior.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la verificación de consistencia entre la factura comercial/Documento de Transporte y los registros aduaneros, ni la verificación de la fecha de vencimiento de la obligación con el exterior.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Debe verificar que el total de pagos imputados a la oficialización, incluido el que se solicita, no supere el monto facturado en la condición de compra pactada, y que el beneficiario sea el proveedor del exterior (o la entidad/agencia que financió la compra, o el no residente que compró el crédito).
- cita del gold: «vii) Que el total de los pagos realizados con imputación a la oficialización de importación, incluyendo el pago cuyo curso se está solicitando, no supera el monto facturado en la condición de compra pactada. viii) Que el beneficiario del pago a realizar sea el proveedor del exterior o, en su caso, la entidad financiera del exterior o la agencia oficial de crédito que financió la compra al proveedor del exterior»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia a la verificación de que el total de pagos imputados a la oficialización no supere el monto facturado, ni a la verificación de que el beneficiario sea el proveedor del exterior o la entidad/agencia que financió la compra.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia a la verificación de que el total de pagos imputados a la oficialización no supere el monto facturado, ni a la verificación de que el beneficiario sea el proveedor del exterior o la entidad/agencia que financió la compra.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia a la verificación de que el total de pagos imputados a la oficialización no supere el monto facturado, ni a la verificación de que el beneficiario sea el proveedor del exterior o la entidad/agencia que financió la compra.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 4 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La venta de divisas debe cursarse con débito en cuentas del cliente en entidades financieras locales y el pago no debe realizarse antes de la fecha de vencimiento de la obligación con el exterior.
- cita del gold: «10.3.2.2. La venta de las divisas es cursada con débito en cuentas del cliente en entidades financieras locales por alguna de las modalidades de medios de pago vigentes. 10.3.2.3. El pago no se realiza con anterioridad a la fecha de vencimiento de la obligación con el exterior.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona el requisito de que la venta de divisas se curse con débito en cuentas del cliente en entidades financieras locales, ni la prohibición de realizar el pago antes de la fecha de vencimiento de la obligación con el exterior.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona el requisito de que la venta de divisas se curse con débito en cuentas del cliente en entidades financieras locales, ni la prohibición de realizar el pago antes de la fecha de vencimiento de la obligación con el exterior.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona el requisito de que la venta de divisas se curse con débito en cuentas del cliente en entidades financieras locales, ni la prohibición de realizar el pago antes de la fecha de vencimiento de la obligación con el exterior.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 5 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Debe contar con una declaración jurada del importador (o su representante legal/apoderado) comprometiéndose a liquidar en el mercado de cambios, dentro de los 20 días hábiles de su puesta a disposición, las divisas que perciba en devolución de pagos de importaciones efectuados con acceso al mercado.
- cita del gold: «10.3.2.4. Declaración jurada comprometiéndose a liquidar en el mercado de cambios, dentro de los 20 (veinte) días hábiles de su puesta a disposición, las divisas que pudiera percibir en devolución de pagos de importaciones efectuados con acceso al mercado de cambios. Esta declaración deberá ser firmada por el importador o quien ejerza su representación legal o un apoderado con facultades suficientes para asumir este compromiso en nombre del importador.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia a la declaración jurada del importador comprometiéndose a liquidar en el mercado de cambios, dentro de los 20 días hábiles, las divisas que pudiera percibir en devolución de pagos de importaciones.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia a la declaración jurada del importador comprometiéndose a liquidar en el mercado de cambios, dentro de los 20 días hábiles, las divisas que pudiera percibir en devolución de pagos de importaciones.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia a la declaración jurada del importador comprometiéndose a liquidar en el mercado de cambios, dentro de los 20 días hábiles, las divisas que pudiera percibir en devolución de pagos de importaciones.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

## U6-023 — humano: **correcto** · juez (mapping): **parcial** [DESACUERDO]

**Pregunta:** ¿Puede una entidad rechazar una solicitud de financiación basándose únicamente en la edad del solicitante cuando sus ingresos proyectados son suficientes, y qué papel juega la posibilidad de contratar un seguro de vida sobre saldo deudor?

**Respuesta del agente (íntegra):**

> Según la regulación del BCRA, una entidad NO puede rechazar una solicitud de financiación basándose únicamente en la edad del solicitante cuando se cumplen dos condiciones simultáneamente: (1) su nivel de ingresos proyectados sea suficiente, y (2) sea posible tomar cobertura por su riesgo de muerte mediante la contratación de un seguro de vida sobre saldo deudor.
> 
> El seguro de vida sobre saldo deudor juega un papel fundamental en esta regulación: es una de las dos condiciones esenciales que permite a la entidad otorgar la financiación a pesar de la edad del solicitante. La cobertura debe incluir fallecimiento e invalidez total permanente, y debe extinguir totalmente el monto adeudado en caso de que ocurra alguno de estos eventos. De esta manera, el seguro mitiga el riesgo que la edad del solicitante podría representar para la entidad.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: No: no corresponde rechazar solicitudes de financiación por el solo dato de la edad del solicitante cuando su nivel de ingresos proyectados es suficiente y es posible tomar cobertura por riesgo de muerte mediante un seguro de vida sobre saldo deudor.
- cita del gold: «En particular, no corresponderá el rechazo de solicitudes de financiación por el solo dato de la edad del solicitante, cuando su nivel de ingresos proyectados sea suficiente y sea posible tomar cobertura por su riesgo de muerte mediante la contratación de un seguro de vida sobre saldo deudor.»
- rep 1 [cumplido] fragmento (verbatim): «una entidad NO puede rechazar una solicitud de financiación basándose únicamente en la edad del solicitante cuando se cumplen dos condiciones simultáneamente: (1) su nivel de ingresos proyectados sea suficiente, y (2) sea posible tomar cobertura por su riesgo de muerte mediante la contratación de un seguro de vida sobre saldo deudor.» — La respuesta reproduce fielmente el contenido normativo del criterio: el rechazo por edad no corresponde cuando los ingresos proyectados son suficientes y es posible contratar un seguro de vida sobre saldo deudor, con los mismos sujetos y condiciones.
- rep 2 [cumplido] fragmento (verbatim): «una entidad NO puede rechazar una solicitud de financiación basándose únicamente en la edad del solicitante cuando se cumplen dos condiciones simultáneamente: (1) su nivel de ingresos proyectados sea suficiente, y (2) sea posible tomar cobertura por su riesgo de muerte mediante la contratación de un seguro de vida sobre saldo deudor.» — La respuesta reproduce fielmente el contenido normativo del criterio: el rechazo no corresponde por el solo dato de la edad cuando los ingresos proyectados son suficientes y es posible contratar el seguro de vida sobre saldo deudor, con los mismos sujetos y condiciones.
- rep 3 [cumplido] fragmento (verbatim): «una entidad NO puede rechazar una solicitud de financiación basándose únicamente en la edad del solicitante cuando se cumplen dos condiciones simultáneamente: (1) su nivel de ingresos proyectados sea suficiente, y (2) sea posible tomar cobertura por su riesgo de muerte mediante la contratación de un seguro de vida sobre saldo deudor.» — La respuesta reproduce fielmente el contenido normativo del criterio: el rechazo no corresponde por el solo dato de la edad cuando los ingresos proyectados son suficientes y es posible contratar el seguro de vida sobre saldo deudor, con los mismos sujetos y condiciones.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La posibilidad de contratar el seguro de vida sobre saldo deudor es lo que habilita cubrir el riesgo de muerte, pero la decisión de contratar o no dicho seguro es del sujeto obligado.
- cita del gold: «Ello, no obstante, será decisión del sujeto obligado contratar o no dicho seguro.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento que la decisión de contratar o no el seguro de vida sobre saldo deudor es del sujeto obligado; ese contenido normativo está completamente ausente.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento que la decisión de contratar o no el seguro de vida sobre saldo deudor es del sujeto obligado; ese elemento normativo está completamente ausente.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento que la decisión de contratar o no el seguro de vida sobre saldo deudor es del sujeto obligado; ese elemento normativo está completamente ausente.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: El rechazo por edad se enmarca en la prohibición de trato discriminatorio: la edad es uno de los motivos por los que los sujetos obligados deben prevenir actos u omisiones discriminatorios.
- cita del gold: «Los sujetos obligados deberán adoptar los recaudos necesarios a los efectos de prevenir particularmente los actos u omisiones discriminatorios determinados por motivos tales como raza, religión, nacionalidad, ideología, opinión política o gremial, edad, sexo, posición económica, condición social o caracteres físicos.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia a la prohibición de trato discriminatorio ni a la lista de motivos (raza, religión, edad, etc.) que los sujetos obligados deben prevenir; ese marco normativo está ausente.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia al marco de prohibición de trato discriminatorio ni a la lista de motivos (raza, religión, nacionalidad, edad, etc.) que los sujetos obligados deben prevenir; ese contenido normativo está ausente.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia al marco de prohibición de trato discriminatorio ni a la lista de motivos (raza, religión, nacionalidad, edad, etc.) que los sujetos obligados deben prevenir; ese contenido normativo está ausente.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

---

# B. requiere_adjudicacion (el instrumento no decidió)

## U6-005 — humano: **parcial** · juez (mapping): **requiere_adjudicacion** [ADJUDICACIÓN]

**Pregunta:** Una persona jurídica quiere operar compraventa de títulos valores con liquidación en moneda extranjera. ¿Por qué mecanismos puede abonar esas operaciones y qué formas de pago están expresamente vedadas?

**Respuesta del agente (íntegra):**

> Una persona jurídica que desee operar compraventa de títulos valores con liquidación en moneda extranjera puede abonar esas operaciones mediante los siguientes mecanismos: (1) transferencia de fondos, (2) cable sobre cuentas bancarias, o (3) cable sobre cuenta de terceros en el exterior. Estos son los únicos mecanismos permitidos según la regulación del BCRA. Sin embargo, el Knowledge Graph no contiene información explícita sobre formas de pago expresamente vedadas para estas operaciones específicas.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: False

### criterio 1 → modal **dudoso** (['dudoso', 'dudoso', 'dudoso'])
- criterio: Puede abonar mediante transferencia de fondos desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales.
- cita del gold: «mediante transferencia de fondos desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales; o»
- rep 1 [dudoso] fragmento (verbatim): «transferencia de fondos» — La respuesta menciona 'transferencia de fondos' pero omite los calificadores normativos esenciales: que sea desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales. La versión abreviada es ambigua respecto de si cubre el mismo alcance.
- rep 2 [dudoso] fragmento (verbatim): «transferencia de fondos» — La respuesta menciona 'transferencia de fondos' pero omite los calificadores normativos esenciales: que sea desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales. La versión de la respuesta es más genérica y no permite confirmar que refleja el mismo alcance normativo.
- rep 3 [dudoso] fragmento (verbatim): «transferencia de fondos» — La respuesta menciona 'transferencia de fondos' pero omite los calificadores normativos esenciales: que sea desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales. La versión de la respuesta es más genérica y no permite confirmar que refleja el mismo alcance normativo.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **dudoso** (['dudoso', 'dudoso', 'dudoso'])
- criterio: Puede abonar contra cable sobre cuentas bancarias a nombre del cliente en una entidad del exterior que no esté constituida en países o territorios donde no se aplican (o no suficientemente) las Recomendaciones del GAFI.
- cita del gold: «contra cable sobre cuentas bancarias a nombre del cliente en una entidad del exterior que no esté constituida en países o territorios donde no se aplican o no se aplican suficientemente las Recomendaciones del Grupo de Acción Financiera Internacional.»
- rep 1 [dudoso] fragmento (verbatim): «cable sobre cuentas bancarias» — La respuesta menciona 'cable sobre cuentas bancarias' pero omite que deben estar a nombre del cliente y que la entidad del exterior no debe estar constituida en jurisdicciones no cooperantes según GAFI, calificadores que limitan el alcance normativo.
- rep 2 [dudoso] fragmento (verbatim): «cable sobre cuentas bancarias» — La respuesta menciona 'cable sobre cuentas bancarias' pero omite el calificador crítico de que la cuenta debe estar a nombre del cliente y que la entidad del exterior no debe estar constituida en jurisdicciones no cooperantes según GAFI, lo que altera el alcance normativo.
- rep 3 [dudoso] fragmento (verbatim): «cable sobre cuentas bancarias» — La respuesta menciona 'cable sobre cuentas bancarias' pero omite el calificador crítico de que la cuenta debe estar a nombre del cliente y que la entidad del exterior no debe estar constituida en jurisdicciones no cooperantes según GAFI, lo que altera el alcance normativo.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Puede abonar contra cable sobre una cuenta de terceros en el exterior (no radicada en jurisdicciones no cooperantes según GAFI) únicamente en el caso de venta de bonos BOPREAL adquiridos en suscripción primaria por operaciones elegibles (puntos 4.4., 4.5., 4.6.1. y 4.7.).
- cita del gold: «contra cable sobre una cuenta de terceros en el exterior que no se encuentre radicada en países o territorios donde no se aplican o no se aplican suficientemente las Recomendaciones del Grupo de Acción Financiera Internacional, cuando se trate de la venta de bonos BOPREAL adquiridos por el vendedor en una suscripción primaria por operaciones elegibles en los puntos 4.4., 4.5., 4.6.1. y 4.7.»
- rep 1 [no_cumplido] fragmento (verbatim): «cable sobre cuenta de terceros en el exterior» — La respuesta menciona el cable sobre cuenta de terceros en el exterior pero omite completamente la restricción de que aplica únicamente para la venta de bonos BOPREAL adquiridos en suscripción primaria por operaciones elegibles (puntos 4.4., 4.5., 4.6.1. y 4.7.), lo que cambia sustancialmente el alcance.
- rep 2 [no_cumplido] fragmento (verbatim): «cable sobre cuenta de terceros en el exterior» — La respuesta menciona el cable sobre cuenta de terceros en el exterior pero omite completamente la condición restrictiva esencial: que esta modalidad solo procede para la venta de bonos BOPREAL adquiridos en suscripción primaria por operaciones elegibles en los puntos específicos de la norma, ni la restricción de jurisdicciones GAFI.
- rep 3 [no_cumplido] fragmento (verbatim): «cable sobre cuenta de terceros en el exterior» — La respuesta menciona el cable sobre cuenta de terceros en el exterior pero omite completamente la condición restrictiva esencial: que esta modalidad solo procede para la venta de bonos BOPREAL adquiridos en suscripción primaria por operaciones elegibles en los puntos específicos de la norma, ni la restricción de jurisdicciones GAFI.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 4 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Está expresamente vedado liquidar estas operaciones mediante el pago en billetes en moneda extranjera o mediante su depósito en cuentas custodia o en cuentas de terceros (salvo las operaciones contra cable con cuentas de terceros del punto 4.3.2.3.).
- cita del gold: «En ningún caso se permite la liquidación de estas operaciones mediante el pago en billetes en moneda extranjera o mediante su depósito en cuentas custodia o en cuentas de terceros, excepto que se trate de operaciones contra cable que utilicen cuentas de terceros en el marco de lo contemplado en el punto 4.3.2.3.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta declara explícitamente que el Knowledge Graph no contiene información sobre formas de pago vedadas, por lo que el contenido normativo del criterio —prohibición de pago en billetes, depósito en cuentas custodia o cuentas de terceros— está completamente ausente.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta declara explícitamente que no contiene información sobre formas de pago expresamente vedadas, por lo que el contenido normativo del criterio —prohibición de pago en billetes, depósito en cuentas custodia o cuentas de terceros— está ausente.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta declara explícitamente que no contiene información sobre formas de pago expresamente vedadas, por lo que el contenido normativo del criterio —prohibición de billetes en moneda extranjera, depósito en cuentas custodia o cuentas de terceros— está ausente.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

## U6-004 — humano: **correcto** · juez (mapping): **requiere_adjudicacion** [ADJUDICACIÓN]

**Pregunta:** Antes de darle a una empresa acceso al mercado de cambios para un pago al exterior, ¿qué declaración jurada sobre activos externos líquidos y CEDEARs debe presentar el cliente, y a partir de qué valor de tenencias pasa a necesitarse la conformidad previa del BCRA?

**Respuesta del agente (íntegra):**

> Antes de dar acceso al mercado de cambios para un pago al exterior, la entidad debe contar con una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles. A partir de un valor superior al equivalente de USD 100.000 (dólares estadounidenses cien mil) en CEDEARs y/o activos externos líquidos disponibles, la entidad deberá contar con la conformidad previa del BCRA. Si el cliente declara que no posee, al inicio del día, CEDEARs y/o activos externos líquidos disponibles que conjuntamente tengan un valor superior a USD 100.000, la conformidad previa del BCRA no es requerida.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: Salvo que cuente con la declaración jurada del cliente al momento del acceso, la entidad debe contar con la conformidad previa del BCRA.
- cita del gold: «La entidad deberá contar con la conformidad previa del BCRA excepto que cuente al momento de acceso al mercado de cambios con una declaración jurada del cliente en la que deje constancia de que:»
- rep 1 [cumplido] fragmento (verbatim): «la entidad debe contar con una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles. A partir de un valor superior al equivalente de USD 100.000 (dólares estadounidenses cien mil) en CEDEARs y/o activos externos líquidos disponibles, la entidad deberá contar con la conformidad previa del BCRA.» — La respuesta refleja que la conformidad previa del BCRA se requiere salvo que se cuente con la declaración jurada del cliente, lo cual es equivalente a la estructura normativa del criterio.
- rep 2 [cumplido] fragmento (verbatim): «la entidad debe contar con una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles. A partir de un valor superior al equivalente de USD 100.000 (dólares estadounidenses cien mil) en CEDEARs y/o activos externos líquidos disponibles, la entidad deberá contar con la conformidad previa del BCRA.» — La respuesta refleja que la conformidad previa del BCRA es requerida salvo que se cuente con la declaración jurada del cliente, lo cual es equivalente a la estructura normativa del criterio.
- rep 3 [cumplido] fragmento (verbatim): «la entidad debe contar con una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles. A partir de un valor superior al equivalente de USD 100.000 (dólares estadounidenses cien mil) en CEDEARs y/o activos externos líquidos disponibles, la entidad deberá contar con la conformidad previa del BCRA.» — La respuesta refleja que la conformidad previa del BCRA se requiere salvo que se cuente con la declaración jurada del cliente, lo cual es equivalente a la estructura normativa del criterio.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **dudoso** (['dudoso', 'dudoso', 'dudoso'])
- criterio: La declaración jurada debe dejar constancia de que la totalidad de las tenencias de moneda extranjera en el país del cliente están depositadas en cuentas en entidades financieras y de que, al inicio del día en que solicita el acceso, no poseía CEDEARs y/o activos externos líquidos disponibles que conjuntamente superen el equivalente de USD 100.000.
- cita del gold: «3.16.2.1. La totalidad de sus tenencias de moneda extranjera en el país se encuentran depositadas en cuentas en entidades financieras y que no poseía, al inicio del día en que solicita el acceso al mercado, certificados de depósitos argentinos representativos de acciones extranjeras (CEDEARs) y/o activos externos líquidos disponibles que conjuntamente tengan un valor superior al equivalente de USD 100.000 (dólares estadounidenses cien mil).»
- rep 1 [dudoso] fragmento (verbatim): «la entidad debe contar con una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles» — La respuesta menciona las tenencias en cuentas de entidades financieras y los CEDEARs/activos externos líquidos, pero no indica explícitamente que la declaración jurada debe dejar constancia de que la TOTALIDAD de las tenencias de moneda extranjera en el país están depositadas en cuentas de entidades financieras (como condición separada y acumulativa), lo que genera ambigüedad sobre si se cumple el contenido completo del criterio.
- rep 2 [dudoso] fragmento (verbatim): «la entidad debe contar con una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles» — La respuesta menciona tenencias en cuentas de entidades financieras y CEDEARs/activos externos, pero no indica explícitamente que la declaración debe afirmar que la TOTALIDAD de las tenencias de moneda extranjera en el país están depositadas en cuentas de entidades financieras, ni reproduce con precisión la condición de 'al inicio del día' para el umbral de USD 100.000, aunque este último sí aparece en otra parte de la respuesta.
- rep 3 [dudoso] fragmento (verbatim): «la entidad debe contar con una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles» — La respuesta menciona las tenencias en cuentas de entidades financieras y los CEDEARs/activos externos líquidos, pero no deja claro que la declaración debe afirmar que la TOTALIDAD de las tenencias de moneda extranjera en el país están depositadas en cuentas financieras (como condición separada y acumulativa), lo que genera ambigüedad sobre si se cumple el contenido completo del criterio.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: El umbral a partir del cual las tenencias hacen necesaria la conformidad previa del BCRA es un valor conjunto superior al equivalente de USD 100.000 (cien mil dólares estadounidenses); si el cliente supera ese monto, la entidad puede aceptar alternativamente una declaración jurada de que no se excede el monto al considerar las situaciones previstas en los incisos i) a vii).
- cita del gold: «En el caso de que el cliente tuviera activos externos líquidos disponibles y/o CEDEARs por un monto superior al establecido en el primer párrafo, la entidad también podrá aceptar una declaración jurada del cliente en la que deje constancia que no se excede tal monto al considerar que, parcial o totalmente, los activos externos líquidos:»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la posibilidad alternativa de que, cuando el cliente supera el umbral de USD 100.000, la entidad pueda aceptar una declaración jurada que acredite que no se excede ese monto al considerar las situaciones previstas en los incisos i) a vii).
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la posibilidad alternativa de presentar una declaración jurada que acredite que no se excede el umbral al considerar las situaciones previstas en los incisos i) a vii), que es el contenido normativo específico exigido por este criterio.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la posibilidad alternativa de presentar una declaración jurada que acredite que no se excede el umbral al considerar las situaciones previstas en los incisos i) a vii), que es el contenido específico exigido por este criterio.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 4 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La declaración jurada también debe incluir el compromiso de liquidar en el mercado de cambios, dentro de los 5 días hábiles de su puesta a disposición, los fondos que reciba en el exterior por cobro de préstamos a terceros, cobro de depósitos a plazo o venta de activos adquiridos/constituidos/otorgados con posterioridad al 28/05/20.
- cita del gold: «3.16.2.2. Se compromete a liquidar en el mercado de cambios, dentro de los 5 (cinco) días hábiles de su puesta a disposición, aquellos fondos que reciba en el exterior originados en el cobro de préstamos otorgados a terceros, el cobro de un depósito a plazo o de la venta de cualquier tipo de activo, cuando el activo hubiera sido adquirido, el depósito constituido o el préstamo otorgado con posterioridad al 28/05/20.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia al compromiso de liquidar en el mercado de cambios, dentro de los 5 días hábiles, los fondos recibidos en el exterior por cobro de préstamos, depósitos a plazo o venta de activos constituidos/otorgados con posterioridad al 28/05/20.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia al compromiso de liquidar en el mercado de cambios dentro de los 5 días hábiles los fondos recibidos en el exterior por cobro de préstamos, depósitos a plazo o venta de activos constituidos con posterioridad al 28/05/20.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia al compromiso de liquidar en el mercado de cambios, dentro de los 5 días hábiles, los fondos recibidos en el exterior por cobro de préstamos, depósitos a plazo o venta de activos constituidos/otorgados con posterioridad al 28/05/20.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

## U6-010 — humano: **parcial** · juez (mapping): **requiere_adjudicacion** [ADJUDICACIÓN]

**Pregunta:** Mi empresa debe intereses por una deuda comercial con su proveedor del exterior. ¿A partir de qué momento puede acceder al mercado de cambios para pagarlos y qué se necesita si quisiera precancelarlos antes del vencimiento?

**Respuesta del agente (íntegra):**

> Según la regulación del BCRA:
> 
> 1. **Momento de acceso al mercado de cambios para pagar intereses**: El acceso al mercado de cambios tiene lugar a partir de la fecha de vencimiento del interés a pagar. Sin embargo, las entidades podrán darle acceso al cliente para pagar incluso antes de la fecha de vencimiento los intereses devengados hasta la fecha de acceso que se encuentren impagos.
> 
> 2. **Precancelación antes del vencimiento**: Si desea precancelar los intereses antes del vencimiento, se requerirá la conformidad previa del BCRA para acceder al mercado de cambios. Esta conformidad previa es obligatoria en casos distintos a VPU-RIGI.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: El acceso al mercado de cambios para pagar los intereses tiene lugar a partir de la fecha de vencimiento del interés a pagar.
- cita del gold: «3.3.2. El acceso al mercado de cambios tiene lugar a partir de la fecha de vencimiento del interés a pagar.»
- rep 1 [cumplido] fragmento (verbatim): «El acceso al mercado de cambios tiene lugar a partir de la fecha de vencimiento del interés a pagar.» — La respuesta reproduce de forma casi literal el contenido del criterio, indicando que el acceso ocurre a partir de la fecha de vencimiento del interés a pagar.
- rep 2 [cumplido] fragmento (verbatim): «El acceso al mercado de cambios tiene lugar a partir de la fecha de vencimiento del interés a pagar.» — La respuesta reproduce de forma casi literal el contenido del criterio, indicando que el acceso ocurre a partir de la fecha de vencimiento del interés a pagar.
- rep 3 [cumplido] fragmento (verbatim): «El acceso al mercado de cambios tiene lugar a partir de la fecha de vencimiento del interés a pagar.» — La respuesta reproduce con exactitud el contenido normativo del criterio, indicando que el acceso ocurre a partir de la fecha de vencimiento del interés a pagar.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: Para precancelar los intereses antes del vencimiento se requiere la conformidad previa del BCRA.
- cita del gold: «En los restantes casos se requerirá la conformidad previa del BCRA para acceder al mercado de cambios para precancelar los servicios de intereses de deudas comerciales por importaciones de bienes y servicios.»
- rep 1 [cumplido] fragmento (verbatim): «Si desea precancelar los intereses antes del vencimiento, se requerirá la conformidad previa del BCRA para acceder al mercado de cambios.» — La respuesta refleja fielmente el requisito normativo: conformidad previa del BCRA para precancelar servicios de intereses de deudas comerciales antes del vencimiento.
- rep 2 [cumplido] fragmento (verbatim): «Si desea precancelar los intereses antes del vencimiento, se requerirá la conformidad previa del BCRA para acceder al mercado de cambios.» — La respuesta refleja fielmente el contenido normativo del criterio: la precancelación antes del vencimiento requiere conformidad previa del BCRA.
- rep 3 [cumplido] fragmento (verbatim): «Si desea precancelar los intereses antes del vencimiento, se requerirá la conformidad previa del BCRA para acceder al mercado de cambios.» — La respuesta refleja fielmente el requisito normativo de conformidad previa del BCRA para precancelar servicios de intereses de deudas comerciales antes del vencimiento.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **dudoso** (['dudoso', 'dudoso', 'dudoso'])
- criterio: El requisito de esperar al vencimiento no aplica si el cliente es un Vehículo de Proyecto Único (VPU) adherido al RIGI que concreta el pago en el marco del punto 14.2.1.
- cita del gold: «Este requisito no resultará aplicable si el cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que concreta el pago en el marco de lo previsto en el punto 14.2.1.»
- rep 1 [dudoso] fragmento (verbatim): «Esta conformidad previa es obligatoria en casos distintos a VPU-RIGI.» — La respuesta menciona la excepción VPU-RIGI pero de forma muy escueta y sin precisar que la excepción aplica específicamente al requisito de esperar al vencimiento (criterio 1) ni que debe concretarse en el marco del punto 14.2.1, lo que genera ambigüedad sobre si el contenido normativo exigido está realmente reflejado.
- rep 2 [dudoso] fragmento (verbatim): «Esta conformidad previa es obligatoria en casos distintos a VPU-RIGI.» — La respuesta menciona la excepción VPU-RIGI pero de forma ambigua: no queda claro si se refiere a la excepción al requisito de conformidad previa del BCRA o a la excepción al requisito de esperar al vencimiento, y no menciona la condición de que el pago se concrete en el marco del punto 14.2.1.
- rep 3 [dudoso] fragmento (verbatim): «Esta conformidad previa es obligatoria en casos distintos a VPU-RIGI.» — La respuesta menciona la excepción VPU-RIGI pero de forma ambigua: no queda claro si se refiere a la excepción al requisito de esperar al vencimiento (criterio 3) o a la excepción al requisito de conformidad previa del BCRA (criterio 2), y no menciona la condición de que el pago se concrete en el marco del punto 14.2.1.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))
