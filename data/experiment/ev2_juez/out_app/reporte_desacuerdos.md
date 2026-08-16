# Reporte de desacuerdos y adjudicaciones — calibración juez EV2 v1 sobre U6 (fuente respuestas: app)

Prompt sha256: `fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455`
Orden: semilla `juez-calibracion-v1`, N=3

## Resumen

- Preguntas: 25 — acuerdo 14 · desacuerdo 6 · requiere_adjudicacion 5
- Acuerdo sobre las decididas: 14/20
- Matriz (humano → juez): correcto→correcto: 1, correcto→parcial: 5, correcto→requiere_adjudicacion: 1, incorrecto→incorrecto: 3, parcial→incorrecto: 1, parcial→parcial: 10, parcial→requiere_adjudicacion: 4
- Proxy por criterio: correcta→todos cumplido 11/21; incorrecta→ninguno cumplido 13/13
- No-determinismo: pares unánimes 87/92; modales {'no_cumplido': 55, 'cumplido': 31, 'dudoso': 6}; todos los veredictos {'no_cumplido': 167, 'cumplido': 94, 'dudoso': 15}
- Fragmentos (276): {'verbatim': 167, 'null': 94, 'no_verbatim': 11, 'fuga_gold': 4} — detalle no-verbatim/fuga_gold: U6-011 c1 r1 [no_cumplido] no_verbatim; U6-011 c1 r2 [no_cumplido] no_verbatim; U6-011 c1 r3 [no_cumplido] no_verbatim; U6-012 c2 r3 [no_cumplido] no_verbatim; U6-012 c3 r3 [no_cumplido] no_verbatim; U6-019 c1 r1 [cumplido] fuga_gold; U6-019 c1 r2 [cumplido] fuga_gold; U6-019 c1 r3 [cumplido] fuga_gold; U6-013 c3 r1 [cumplido] no_verbatim; U6-013 c3 r2 [cumplido] no_verbatim; U6-013 c3 r3 [cumplido] no_verbatim; U6-001 c3 r2 [dudoso] fuga_gold; U6-015 c4 r1 [cumplido] no_verbatim; U6-015 c4 r2 [cumplido] no_verbatim; U6-015 c4 r3 [cumplido] no_verbatim
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
- rep 1 [cumplido] fragmento (verbatim): «el total se determina con los valores que se registren al último día del período de información (n)» — La respuesta reproduce fielmente el contenido normativo: la exigencia por riesgo de mercado se determina con los valores al último día del período de información (n), coincidiendo con la cita.
- rep 2 [cumplido] fragmento (verbatim): «el total se determina con los valores que se registren al último día del período de información (n)» — La respuesta reproduce fielmente el contenido normativo del criterio, indicando que la exigencia se determina con los valores del último día del período de información (n).
- rep 3 [cumplido] fragmento (verbatim): «el total se determina con los valores que se registren al último día del período de información (n)» — La respuesta reproduce fielmente el contenido normativo del criterio, indicando que la exigencia se determina con los valores del último día del período de información (n).
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La exigencia por riesgo general de tasa de interés (código 311200/xx) se determina por cada moneda, y la partida se identifica según su moneda de origen con la codificación de la tabla T0003 del SISCEN, excluidas las monedas no referenciadas con código SWIFT.
- cita del gold: «La determinación de esta exigencia se efectuará por cada moneda, a cuyos efectos la presente partida se identificará según su moneda de origen de acuerdo con la codificación prevista en el Sistema Centralizado de requerimientos informativos (SISCEN), tabla T0003, de la que se excluirán aquellas que no estén referenciadas con el código SWIFT.»
- rep 1 [cumplido] fragmento (verbatim): «la determinación de esta exigencia se efectuará por cada moneda, identificándose la presente partida según su moneda de origen de acuerdo con la codificación prevista en el Sistema Centralizado de requerimientos informativos (SISCEN), tabla T0003, de la que se excluirán aquellas monedas que no estén referenciadas con el código SWIFT.» — La respuesta parafrasea con fidelidad la cita normativa, incluyendo todos los elementos: determinación por moneda, identificación según moneda de origen, tabla T0003 del SISCEN y exclusión de monedas sin código SWIFT.
- rep 2 [cumplido] fragmento (verbatim): «la determinación de esta exigencia se efectuará por cada moneda, identificándose la presente partida según su moneda de origen de acuerdo con la codificación prevista en el Sistema Centralizado de requerimientos informativos (SISCEN), tabla T0003, de la que se excluirán aquellas monedas que no estén referenciadas con el código SWIFT.» — La respuesta parafrasea con fidelidad la cita normativa, incluyendo todos los elementos: determinación por moneda, identificación según moneda de origen, tabla T0003 del SISCEN y exclusión de monedas sin código SWIFT.
- rep 3 [cumplido] fragmento (verbatim): «la determinación de esta exigencia se efectuará por cada moneda, identificándose la presente partida según su moneda de origen de acuerdo con la codificación prevista en el Sistema Centralizado de requerimientos informativos (SISCEN), tabla T0003, de la que se excluirán aquellas monedas que no estén referenciadas con el código SWIFT.» — La respuesta parafrasea con fidelidad la cita normativa, incluyendo todos los elementos: determinación por moneda, identificación según moneda de origen, tabla T0003 del SISCEN y exclusión de monedas sin código SWIFT.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Las monedas residuales, de corresponder, se identifican con el código de moneda 9999.
- cita del gold: «De corresponder, las monedas residuales (puntos 6.2.2.2. y 6.2.2.7. de las normas sobre “Capitales mínimos de las entidades financieras”) se identificarán con código de moneda 9999.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento que las monedas residuales se identifican con el código de moneda 9999, contenido exigido por el criterio.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento que las monedas residuales se identifican con el código de moneda 9999.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento que las monedas residuales se identifican con el código de moneda 9999.
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
- rep 1 [cumplido] fragmento (verbatim): «El monto total abonado por concepto de utilidades y dividendos a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.» — La respuesta parafrasea con precisión el criterio, conservando todos los elementos relevantes: monto total abonado, accionistas no residentes, inclusión del pago solicitado, límite en moneda local y determinación por asamblea.
- rep 2 [cumplido] fragmento (verbatim): «El monto total abonado por concepto de utilidades y dividendos a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.» — La respuesta parafrasea con precisión el criterio, conservando todos los elementos relevantes: monto total abonado, accionistas no residentes, inclusión del pago solicitado, límite en moneda local y determinación por asamblea.
- rep 3 [cumplido] fragmento (verbatim): «El monto total abonado por concepto de utilidades y dividendos a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas.» — La respuesta parafrasea con precisión el criterio, conservando todos los elementos relevantes: monto total abonado, accionistas no residentes, inclusión del pago solicitado, límite en moneda local y determinación por asamblea.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La entidad debe contar con una declaración jurada firmada por el representante legal de la empresa residente o un apoderado con facultades suficientes.
- cita del gold: «La entidad deberá contar con una declaración jurada firmada por el representante legal de la empresa residente o un apoderado con facultades suficientes para asumir este compromiso en nombre de la empresa.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la obligación de contar con una declaración jurada firmada por el representante legal o apoderado con facultades suficientes.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la obligación de contar con una declaración jurada firmada por el representante legal o apoderado con facultades suficientes.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la obligación de contar con una declaración jurada firmada por el representante legal o apoderado con facultades suficientes.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

## U6-017 — humano: **correcto** · juez (mapping): **parcial** [DESACUERDO]

**Pregunta:** ¿A partir de qué magnitud de financiaciones la clasificación de un deudor y el cálculo de sus previsiones requieren la aprobación previa del Directorio de la entidad, y qué mayoría se exige cuando se trata de clientes vinculados?

**Respuesta del agente (íntegra):**

> La clasificación de un deudor y el cálculo de sus previsiones requieren aprobación previa del Directorio o Consejo de Administración cuando las financiaciones excedan del 2,5% de la RPC (Responsabilidad Patrimonial Computable) de la entidad financiera del mes anterior. La aprobación debe ser por mayoría simple en los casos ordinarios, pero se exige una mayoría de dos tercios cuando se trata de clientes vinculados.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La aprobación previa del Directorio (o Consejo de Administración o autoridad equivalente) se requiere para la clasificación y el cálculo de previsiones por financiaciones que excedan el 2,5 % de la RPC de la entidad del mes anterior al que corresponda.
- cita del gold: «por financiaciones que excedan del 2,5 % de la RPC de la entidad financiera del mes anterior al que corresponda, deberán contar con la previa aprobación de los miembros del Directorio o Consejo de Administración»
- rep 1 [cumplido] fragmento (verbatim): «requieren aprobación previa del Directorio o Consejo de Administración cuando las financiaciones excedan del 2,5% de la RPC (Responsabilidad Patrimonial Computable) de la entidad financiera del mes anterior» — La respuesta reproduce fielmente el umbral del 2,5% de la RPC del mes anterior y los órganos requeridos (Directorio o Consejo de Administración), en línea con la cita normativa.
- rep 2 [cumplido] fragmento (verbatim): «requieren aprobación previa del Directorio o Consejo de Administración cuando las financiaciones excedan del 2,5% de la RPC (Responsabilidad Patrimonial Computable) de la entidad financiera del mes anterior» — La respuesta reproduce fielmente el umbral del 2,5% de la RPC del mes anterior y los órganos requeridos (Directorio o Consejo de Administración), en línea con la cita normativa.
- rep 3 [cumplido] fragmento (verbatim): «requieren aprobación previa del Directorio o Consejo de Administración cuando las financiaciones excedan del 2,5% de la RPC (Responsabilidad Patrimonial Computable) de la entidad financiera del mes anterior» — La respuesta reproduce fielmente el umbral del 2,5% de la RPC del mes anterior y los órganos requeridos (Directorio o Consejo de Administración), en línea con la cita normativa.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La aprobación es por mayoría simple, y cuando se trata de clientes vinculados se exige dos tercios de la totalidad de los miembros.
- cita del gold: «–por mayoría simple o, cuando se trate de clientes vinculados, de dos tercios de la totalidad de los miembros– o autoridad equivalente de la entidad financiera prestamista.»
- rep 1 [cumplido] fragmento (verbatim): «La aprobación debe ser por mayoría simple en los casos ordinarios, pero se exige una mayoría de dos tercios cuando se trata de clientes vinculados.» — La respuesta refleja correctamente ambas mayorías exigidas por la norma: mayoría simple para el caso general y dos tercios para clientes vinculados.
- rep 2 [cumplido] fragmento (verbatim): «La aprobación debe ser por mayoría simple en los casos ordinarios, pero se exige una mayoría de dos tercios cuando se trata de clientes vinculados.» — La respuesta refleja correctamente ambas mayorías: simple para el caso general y dos tercios para clientes vinculados, conforme a la cita normativa; omite el detalle 'de la totalidad de los miembros' pero no altera el alcance sustantivo.
- rep 3 [cumplido] fragmento (verbatim): «La aprobación debe ser por mayoría simple en los casos ordinarios, pero se exige una mayoría de dos tercios cuando se trata de clientes vinculados.» — La respuesta refleja correctamente ambas mayorías exigidas por la norma: mayoría simple para el caso general y dos tercios para clientes vinculados.
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
- rep 1 [cumplido] fragmento (verbatim): «no se permite descalce de plazos de vencimiento; la exposición debe estar cubierta durante todo el plazo de vencimiento contractual» — La respuesta reproduce fielmente ambos elementos del criterio: la cobertura durante todo el plazo contractual y la prohibición del descalce de plazos.
- rep 2 [cumplido] fragmento (verbatim): «no se permite descalce de plazos de vencimiento; la exposición debe estar cubierta durante todo el plazo de vencimiento contractual.» — La respuesta reproduce fielmente ambos elementos del criterio: la cobertura durante todo el plazo contractual y la prohibición del descalce de plazos.
- rep 3 [cumplido] fragmento (verbatim): «no se permite descalce de plazos de vencimiento; la exposición debe estar cubierta durante todo el plazo de vencimiento contractual.» — La respuesta reproduce fielmente ambos elementos del criterio: cobertura durante todo el plazo contractual y prohibición de descalce de plazos.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Condición de valuación: el activo recibido en garantía debe estar entre los listados en el punto 5.3.1.2. y contar con valuación a precios de mercado con frecuencia mínima mensual.
- cita del gold: «el activo recibido en garantía se limitará a aquellos listados en el punto 5.3.1.2. y contar con una valuación a precios de mercado con una frecuencia mínima mensual.»
- rep 1 [no_cumplido] fragmento (verbatim): «el activo recibido en garantía debe contar con una valuación a precios de mercado con una frecuencia mínima mensual» — La respuesta menciona la valuación a precios de mercado con frecuencia mínima mensual, pero omite el requisito de que el activo debe estar limitado a aquellos listados en el punto 5.3.1.2., que es parte integral de la condición de valuación según la norma.
- rep 2 [no_cumplido] fragmento (verbatim): «el activo recibido en garantía debe contar con una valuación a precios de mercado con una frecuencia mínima mensual.» — La respuesta menciona la condición de valuación pero omite el requisito de que el activo esté limitado a aquellos listados en el punto 5.3.1.2., que es parte esencial de la condición normativa exigida por el criterio.
- rep 3 [no_cumplido] fragmento (verbatim): «el activo recibido en garantía debe contar con una valuación a precios de mercado con una frecuencia mínima mensual.» — La respuesta menciona la condición de valuación pero omite el requisito de que el activo debe estar entre los listados en el punto 5.3.1.2., que es parte esencial de la condición normativa.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: La parte cubierta de la exposición recibe el ponderador de riesgo del activo recibido en garantía, sujeto a un mínimo del 20% (salvo las excepciones del punto 5.3.1.3.).
- cita del gold: «La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% –salvo lo dispuesto en el punto 5.3.1.3.–. A la parte no cubierta se le aplicará el ponderador de riesgo que le corresponda según el tipo de exposición de que se trate.»
- rep 1 [cumplido] fragmento (no_verbatim): «la parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% (salvo excepciones previstas en el punto 5.3.1.3.)» — La respuesta refleja con exactitud el ponderador mínimo del 20%, la referencia a las excepciones del punto 5.3.1.3. y la lógica de aplicar el ponderador del activo en garantía a la parte cubierta.
- rep 2 [cumplido] fragmento (no_verbatim): «la parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% (salvo excepciones previstas en el punto 5.3.1.3.).» — La respuesta refleja con exactitud el ponderador mínimo del 20%, la referencia al activo en garantía como base del ponderador y la salvedad del punto 5.3.1.3., coincidiendo con la cita normativa.
- rep 3 [cumplido] fragmento (no_verbatim): «la parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% (salvo excepciones previstas en el punto 5.3.1.3.).» — La respuesta refleja fielmente el ponderador mínimo del 20%, la referencia al activo en garantía como base del ponderador y la salvedad del punto 5.3.1.3.
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
- rep 1 [no_cumplido] fragmento (verbatim): «La entidad debe contar con constancia del registro aduanero del ingreso de bienes que originan el pago.» — La respuesta menciona la constancia del registro aduanero, pero omite completamente los otros dos documentos exigidos por el criterio: la copia de la factura comercial (con todos sus elementos: nombre y dirección del emisor, nombre del importador, cantidad y descripción de la mercadería, condición de venta y valor) y la copia del Documento de Transporte.
- rep 2 [no_cumplido] fragmento (verbatim): «La entidad debe contar con constancia del registro aduanero del ingreso de bienes que originan el pago.» — La respuesta menciona la constancia del registro aduanero, pero omite completamente los otros dos documentos exigidos por el criterio: la copia de la factura comercial (con todos sus elementos: nombre y dirección del emisor, nombre del importador, cantidad y descripción de la mercadería, condición de venta y valor) y la copia del Documento de Transporte.
- rep 3 [no_cumplido] fragmento (verbatim): «La entidad debe contar con constancia del registro aduanero del ingreso de bienes que originan el pago.» — La respuesta menciona la constancia del registro aduanero, pero omite completamente los otros dos documentos exigidos por el criterio: la copia de la factura comercial (con todos sus elementos: nombre y dirección del emisor, nombre del importador, cantidad y descripción de la mercadería, condición de venta y valor) y la copia del Documento de Transporte.
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
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia a la verificación de que el total de pagos imputados a la oficialización no supere el monto facturado, ni a la verificación de la identidad del beneficiario del pago.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia a la verificación de que el total de pagos imputados a la oficialización no supere el monto facturado, ni a los requisitos sobre la identidad del beneficiario del pago.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia a la verificación de que el total de pagos imputados a la oficialización no supere el monto facturado, ni a la verificación de que el beneficiario sea el proveedor del exterior o la entidad/agencia que financió la compra.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 4 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La venta de divisas debe cursarse con débito en cuentas del cliente en entidades financieras locales y el pago no debe realizarse antes de la fecha de vencimiento de la obligación con el exterior.
- cita del gold: «10.3.2.2. La venta de las divisas es cursada con débito en cuentas del cliente en entidades financieras locales por alguna de las modalidades de medios de pago vigentes. 10.3.2.3. El pago no se realiza con anterioridad a la fecha de vencimiento de la obligación con el exterior.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona el requisito de que la venta de divisas se curse con débito en cuentas del cliente en entidades financieras locales, ni la prohibición de realizar el pago antes de la fecha de vencimiento de la obligación con el exterior.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona que la venta de divisas deba cursarse con débito en cuentas del cliente en entidades financieras locales, ni que el pago no pueda realizarse antes de la fecha de vencimiento de la obligación con el exterior.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona que la venta de divisas deba cursarse con débito en cuentas del cliente en entidades financieras locales, ni que el pago no pueda realizarse antes de la fecha de vencimiento de la obligación con el exterior.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 5 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Debe contar con una declaración jurada del importador (o su representante legal/apoderado) comprometiéndose a liquidar en el mercado de cambios, dentro de los 20 días hábiles de su puesta a disposición, las divisas que perciba en devolución de pagos de importaciones efectuados con acceso al mercado.
- cita del gold: «10.3.2.4. Declaración jurada comprometiéndose a liquidar en el mercado de cambios, dentro de los 20 (veinte) días hábiles de su puesta a disposición, las divisas que pudiera percibir en devolución de pagos de importaciones efectuados con acceso al mercado de cambios. Esta declaración deberá ser firmada por el importador o quien ejerza su representación legal o un apoderado con facultades suficientes para asumir este compromiso en nombre del importador.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia a la declaración jurada del importador comprometiéndose a liquidar en el mercado de cambios, dentro de los 20 días hábiles, las divisas percibidas en devolución de pagos de importaciones.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia a la declaración jurada del importador comprometiéndose a liquidar en el mercado de cambios las divisas percibidas en devolución dentro de los 20 días hábiles.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia a la declaración jurada del importador comprometiéndose a liquidar en el mercado de cambios, dentro de los 20 días hábiles, las divisas percibidas en devolución de pagos de importaciones.
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
- rep 1 [cumplido] fragmento (verbatim): «una entidad NO puede rechazar una solicitud de financiación basándose únicamente en la edad del solicitante cuando se cumplen dos condiciones simultáneamente: (1) su nivel de ingresos proyectados sea suficiente, y (2) sea posible tomar cobertura por su riesgo de muerte mediante la contratación de un seguro de vida sobre saldo deudor.» — La respuesta reproduce fielmente las dos condiciones que la norma exige para que no corresponda el rechazo por edad: ingresos proyectados suficientes y posibilidad de contratar seguro de vida sobre saldo deudor.
- rep 2 [cumplido] fragmento (verbatim): «una entidad NO puede rechazar una solicitud de financiación basándose únicamente en la edad del solicitante cuando se cumplen dos condiciones simultáneamente: (1) su nivel de ingresos proyectados sea suficiente, y (2) sea posible tomar cobertura por su riesgo de muerte mediante la contratación de un seguro de vida sobre saldo deudor.» — La respuesta reproduce fielmente las dos condiciones acumulativas que la norma exige para que no corresponda el rechazo por edad, con los mismos sujetos, calificadores y modalidades.
- rep 3 [cumplido] fragmento (verbatim): «una entidad NO puede rechazar una solicitud de financiación basándose únicamente en la edad del solicitante cuando se cumplen dos condiciones simultáneamente: (1) su nivel de ingresos proyectados sea suficiente, y (2) sea posible tomar cobertura por su riesgo de muerte mediante la contratación de un seguro de vida sobre saldo deudor.» — La respuesta reproduce fielmente las dos condiciones que la norma exige para que no corresponda el rechazo por edad: ingresos proyectados suficientes y posibilidad de contratar seguro de vida sobre saldo deudor, con los mismos sujetos y calificadores.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La posibilidad de contratar el seguro de vida sobre saldo deudor es lo que habilita cubrir el riesgo de muerte, pero la decisión de contratar o no dicho seguro es del sujeto obligado.
- cita del gold: «Ello, no obstante, será decisión del sujeto obligado contratar o no dicho seguro.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento que la decisión de contratar o no el seguro de vida sobre saldo deudor es del sujeto obligado, omitiendo completamente ese elemento normativo.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento que la decisión de contratar o no el seguro de vida sobre saldo deudor es del sujeto obligado; ese elemento normativo está completamente ausente.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento que la decisión de contratar o no el seguro de vida sobre saldo deudor es del sujeto obligado; ese elemento normativo está completamente ausente.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: El rechazo por edad se enmarca en la prohibición de trato discriminatorio: la edad es uno de los motivos por los que los sujetos obligados deben prevenir actos u omisiones discriminatorios.
- cita del gold: «Los sujetos obligados deberán adoptar los recaudos necesarios a los efectos de prevenir particularmente los actos u omisiones discriminatorios determinados por motivos tales como raza, religión, nacionalidad, ideología, opinión política o gremial, edad, sexo, posición económica, condición social o caracteres físicos.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia al marco de prohibición de trato discriminatorio ni a la lista de motivos (raza, religión, nacionalidad, edad, etc.) en que se encuadra la restricción al rechazo por edad.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia al marco de prohibición de trato discriminatorio ni a la lista de motivos (raza, religión, nacionalidad, edad, etc.) en que se enmarca la regla sobre rechazo por edad.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia al marco de prohibición de trato discriminatorio ni a la lista de motivos (raza, religión, nacionalidad, edad, etc.) que la norma enumera; ese encuadre normativo está totalmente ausente.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

---

# B. requiere_adjudicacion (el instrumento no decidió)

## U6-011 — humano: **parcial** · juez (mapping): **requiere_adjudicacion** [ADJUDICACIÓN]

**Pregunta:** Una entidad financiera en funcionamiento detecta e informa un incumplimiento de su exigencia de capital mínimo. ¿En qué plazo debe encuadrarse o presentar un plan de regularización y saneamiento, y qué restricciones le aplican sobre depósitos y distribución de dividendos mientras tanto?

**Respuesta del agente (íntegra):**

> Cuando una entidad financiera en funcionamiento detecta e informa un incumplimiento de su exigencia de capital mínimo, debe observar los siguientes plazos y restricciones:
> 
> **Plazos de regularización:**
> - Plazo inicial: 10 días hábiles contados desde la fecha en que quede firme el defecto de integración para regularizar el incumplimiento.
> - Si el defecto persiste más allá de 10 días hábiles: la entidad debe presentar un plan de regularización y saneamiento dentro de los 5 días hábiles siguientes.
> 
> **Restricciones durante la regularización:**
> 
> 1. **Sobre depósitos:** No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento (considerando el importe registrado en el código 310000 del Balance de Saldos).
> 
> 2. **Sobre distribución de dividendos:** No podrán distribuirse dividendos en efectivo, ni efectuarse pagos de honorarios, participaciones o gratificaciones provenientes de la distribución de resultados de la entidad. Esta limitación rige mientras los planes de regularización y saneamiento estén pendientes de presentación o, habiéndose presentado, la SEFyC los haya observado o verifique su incumplimiento.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La entidad debe encuadrarse en la exigencia a más tardar en el segundo mes siguiente a aquel en que se registre el incumplimiento, o presentar un plan de regularización y saneamiento dentro de los 30 días corridos siguientes al último día del mes al que corresponda el incumplimiento.
- cita del gold: «La entidad deberá encuadrarse en la exigencia a más tardar en el segundo mes siguiente a aquel en que se registre el incumplimiento, o presentar un plan de regularización y saneamiento dentro de los 30 días corridos siguientes al último día del mes al que corresponda el incumplimiento.»
- rep 1 [no_cumplido] fragmento (no_verbatim): «Plazo inicial: 10 días hábiles contados desde la fecha en que quede firme el defecto de integración para regularizar el incumplimiento. Si el defecto persiste más allá de 10 días hábiles: la entidad debe presentar un plan de regularización y saneamiento dentro de los 5 días hábiles siguientes.» — La respuesta establece plazos en días hábiles (10 y 5) que no coinciden con los plazos normativos: encuadrarse en la exigencia a más tardar en el segundo mes siguiente al incumplimiento, o presentar el plan dentro de los 30 días corridos siguientes al último día del mes del incumplimiento.
- rep 2 [no_cumplido] fragmento (no_verbatim): «Plazo inicial: 10 días hábiles contados desde la fecha en que quede firme el defecto de integración para regularizar el incumplimiento. Si el defecto persiste más allá de 10 días hábiles: la entidad debe presentar un plan de regularización y saneamiento dentro de los 5 días hábiles siguientes.» — La respuesta indica plazos de 10 días hábiles y 5 días hábiles, mientras que la norma establece encuadrarse a más tardar en el segundo mes siguiente al incumplimiento o presentar el plan dentro de los 30 días corridos siguientes al último día del mes del incumplimiento; los plazos son completamente distintos.
- rep 3 [no_cumplido] fragmento (no_verbatim): «Plazo inicial: 10 días hábiles contados desde la fecha en que quede firme el defecto de integración para regularizar el incumplimiento. Si el defecto persiste más allá de 10 días hábiles: la entidad debe presentar un plan de regularización y saneamiento dentro de los 5 días hábiles siguientes.» — La respuesta establece plazos de 10 días hábiles y 5 días hábiles adicionales, mientras que la norma exige encuadrarse en la exigencia a más tardar en el segundo mes siguiente al incumplimiento, o presentar un plan dentro de los 30 días corridos siguientes al último día del mes del incumplimiento; los plazos y su cómputo son completamente distintos.
- pre-clasificación mecánica del par: **evidencia** (nulos=0/3, no_verbatim=3/3, fragmentos_distintos=1)

### criterio 2 → modal **dudoso** (['dudoso', 'no_cumplido', 'dudoso']) ⚠ no unánime
- criterio: Los depósitos (en moneda nacional y extranjera) no pueden exceder el nivel alcanzado durante el mes en que se originó el incumplimiento; el límite se mantiene mientras persista la deficiencia y se computa sobre saldos al último día de cada mes.
- cita del gold: «La obligación de presentar planes determinará que el importe de los depósitos –en moneda nacional y extranjera– no podrá exceder del nivel que haya alcanzado durante el mes en que se originó el incumplimiento. Dicho límite –que se mantendrá mientras persista la deficiencia– y su observancia se computarán a base de los saldos registrados al último día de cada uno de los meses comprendidos.»
- rep 1 [dudoso] fragmento (verbatim): «No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento (considerando el importe registrado en el código 310000 del Balance de Saldos).» — La respuesta recoge correctamente el límite de depósitos referido al mes de origen del incumplimiento, pero omite que el cómputo se realiza sobre saldos al último día de cada mes y que el límite se mantiene mientras persista la deficiencia; además agrega una referencia a un código contable no prevista en la norma, lo que genera ambigüedad sobre si el alcance es equivalente.
- rep 2 [no_cumplido] fragmento (verbatim): «No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento (considerando el importe registrado en el código 310000 del Balance de Saldos).» — La respuesta omite que el límite se computa sobre los saldos al último día de cada mes comprendido y que aplica a depósitos en moneda nacional y extranjera; además agrega una referencia al código 310000 que no figura en la norma, y no menciona que el límite se mantiene mientras persista la deficiencia con la base de cómputo mensual al último día.
- rep 3 [dudoso] fragmento (verbatim): «No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento (considerando el importe registrado en el código 310000 del Balance de Saldos).» — La respuesta recoge correctamente el límite de depósitos referido al mes de origen del incumplimiento, pero omite que el cómputo se realiza sobre saldos al último día de cada mes mientras persista la deficiencia, y la referencia al código 310000 no equivale a esa precisión normativa; la ausencia de ese calificador deja el criterio sin confirmación plena.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: No pueden distribuirse dividendos en efectivo (ni pagarse honorarios, participaciones o gratificaciones provenientes de la distribución de resultados) mientras los planes estén pendientes de presentación o, presentados, la SEFyC los haya observado o verifique su incumplimiento.
- cita del gold: «iii) No podrán distribuirse dividendos en efectivo, ni efectuarse pagos de honorarios, participaciones o gratificaciones provenientes de la distribución de resultados de la entidad. Esta limitación regirá en tanto los planes de regularización y saneamiento estén pendientes de presentación o, habiéndose presentado, la SEFyC los haya observado o verifique su incumplimiento.»
- rep 1 [cumplido] fragmento (verbatim): «No podrán distribuirse dividendos en efectivo, ni efectuarse pagos de honorarios, participaciones o gratificaciones provenientes de la distribución de resultados de la entidad. Esta limitación rige mientras los planes de regularización y saneamiento estén pendientes de presentación o, habiéndose presentado, la SEFyC los haya observado o verifique su incumplimiento.» — La respuesta reproduce fielmente el contenido normativo del criterio, incluyendo los mismos sujetos, modalidades y condiciones de vigencia de la restricción.
- rep 2 [cumplido] fragmento (verbatim): «No podrán distribuirse dividendos en efectivo, ni efectuarse pagos de honorarios, participaciones o gratificaciones provenientes de la distribución de resultados de la entidad. Esta limitación rige mientras los planes de regularización y saneamiento estén pendientes de presentación o, habiéndose presentado, la SEFyC los haya observado o verifique su incumplimiento.» — La respuesta reproduce fielmente el contenido normativo del criterio, incluyendo los mismos sujetos, modalidades y condiciones de vigencia de la restricción.
- rep 3 [cumplido] fragmento (verbatim): «No podrán distribuirse dividendos en efectivo, ni efectuarse pagos de honorarios, participaciones o gratificaciones provenientes de la distribución de resultados de la entidad. Esta limitación rige mientras los planes de regularización y saneamiento estén pendientes de presentación o, habiéndose presentado, la SEFyC los haya observado o verifique su incumplimiento.» — La respuesta reproduce con fidelidad el contenido normativo del criterio, incluyendo los mismos sujetos, modalidades y condiciones de vigencia de la restricción.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

## U6-005 — humano: **parcial** · juez (mapping): **requiere_adjudicacion** [ADJUDICACIÓN]

**Pregunta:** Una persona jurídica quiere operar compraventa de títulos valores con liquidación en moneda extranjera. ¿Por qué mecanismos puede abonar esas operaciones y qué formas de pago están expresamente vedadas?

**Respuesta del agente (íntegra):**

> Una persona jurídica que desee operar compraventa de títulos valores con liquidación en moneda extranjera puede abonar esas operaciones mediante los siguientes mecanismos: (1) transferencia de fondos, (2) cable sobre cuentas bancarias, o (3) cable sobre cuenta de terceros en el exterior. Estos son los únicos mecanismos permitidos según la regulación del BCRA. Sin embargo, el Knowledge Graph no contiene información explícita sobre formas de pago expresamente vedadas para estas operaciones específicas.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: False

### criterio 1 → modal **dudoso** (['dudoso', 'dudoso', 'dudoso'])
- criterio: Puede abonar mediante transferencia de fondos desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales.
- cita del gold: «mediante transferencia de fondos desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales; o»
- rep 1 [dudoso] fragmento (verbatim): «transferencia de fondos» — La respuesta menciona 'transferencia de fondos' pero omite los calificadores normativos esenciales: que debe ser desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales. La versión de la respuesta es demasiado genérica para confirmar equivalencia normativa.
- rep 2 [dudoso] fragmento (verbatim): «transferencia de fondos» — La respuesta menciona 'transferencia de fondos' pero omite los calificadores normativos esenciales: que debe ser desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales. La versión de la respuesta es demasiado genérica para confirmar equivalencia normativa.
- rep 3 [dudoso] fragmento (verbatim): «transferencia de fondos» — La respuesta menciona 'transferencia de fondos' pero omite los calificadores normativos esenciales: que debe ser desde y hacia cuentas a la vista a nombre del cliente en entidades financieras locales. La versión de la respuesta es demasiado genérica para confirmar equivalencia normativa.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **dudoso** (['dudoso', 'dudoso', 'dudoso'])
- criterio: Puede abonar contra cable sobre cuentas bancarias a nombre del cliente en una entidad del exterior que no esté constituida en países o territorios donde no se aplican (o no suficientemente) las Recomendaciones del GAFI.
- cita del gold: «contra cable sobre cuentas bancarias a nombre del cliente en una entidad del exterior que no esté constituida en países o territorios donde no se aplican o no se aplican suficientemente las Recomendaciones del Grupo de Acción Financiera Internacional.»
- rep 1 [dudoso] fragmento (verbatim): «cable sobre cuentas bancarias» — La respuesta menciona 'cable sobre cuentas bancarias' pero omite el calificador crítico de que la cuenta debe estar a nombre del cliente y que la entidad del exterior no debe estar constituida en países o territorios no cooperantes según GAFI, lo que altera el alcance normativo.
- rep 2 [dudoso] fragmento (verbatim): «cable sobre cuentas bancarias» — La respuesta menciona 'cable sobre cuentas bancarias' pero omite el calificador crítico de que la cuenta debe estar a nombre del cliente y que la entidad del exterior no debe estar constituida en países o territorios no cooperantes según GAFI, lo que altera el alcance normativo.
- rep 3 [dudoso] fragmento (verbatim): «cable sobre cuentas bancarias» — La respuesta menciona 'cable sobre cuentas bancarias' pero omite el calificador crítico de que la cuenta debe estar a nombre del cliente y que la entidad del exterior no debe estar constituida en países o territorios no cooperantes según GAFI, lo que altera el alcance normativo.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Puede abonar contra cable sobre una cuenta de terceros en el exterior (no radicada en jurisdicciones no cooperantes según GAFI) únicamente en el caso de venta de bonos BOPREAL adquiridos en suscripción primaria por operaciones elegibles (puntos 4.4., 4.5., 4.6.1. y 4.7.).
- cita del gold: «contra cable sobre una cuenta de terceros en el exterior que no se encuentre radicada en países o territorios donde no se aplican o no se aplican suficientemente las Recomendaciones del Grupo de Acción Financiera Internacional, cuando se trate de la venta de bonos BOPREAL adquiridos por el vendedor en una suscripción primaria por operaciones elegibles en los puntos 4.4., 4.5., 4.6.1. y 4.7.»
- rep 1 [no_cumplido] fragmento (verbatim): «cable sobre cuenta de terceros en el exterior» — La respuesta menciona 'cable sobre cuenta de terceros en el exterior' como mecanismo general, pero omite completamente la restricción normativa esencial: que esta modalidad solo está permitida para la venta de bonos BOPREAL adquiridos en suscripción primaria por operaciones elegibles en los puntos específicos (4.4., 4.5., 4.6.1. y 4.7.), además de la exclusión de jurisdicciones no cooperantes según GAFI.
- rep 2 [no_cumplido] fragmento (verbatim): «cable sobre cuenta de terceros en el exterior» — La respuesta menciona 'cable sobre cuenta de terceros en el exterior' como mecanismo general, pero omite completamente la restricción normativa esencial: que esta modalidad solo está permitida para la venta de bonos BOPREAL adquiridos en suscripción primaria por operaciones elegibles en los puntos específicos (4.4., 4.5., 4.6.1. y 4.7.), y tampoco menciona la exclusión de jurisdicciones no cooperantes según GAFI.
- rep 3 [no_cumplido] fragmento (verbatim): «cable sobre cuenta de terceros en el exterior» — La respuesta menciona 'cable sobre cuenta de terceros en el exterior' como mecanismo general, pero omite completamente la restricción normativa esencial: que esta modalidad solo procede para la venta de bonos BOPREAL adquiridos en suscripción primaria por operaciones elegibles en los puntos específicos (4.4., 4.5., 4.6.1. y 4.7.), ni la exclusión de jurisdicciones no cooperantes según GAFI.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 4 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Está expresamente vedado liquidar estas operaciones mediante el pago en billetes en moneda extranjera o mediante su depósito en cuentas custodia o en cuentas de terceros (salvo las operaciones contra cable con cuentas de terceros del punto 4.3.2.3.).
- cita del gold: «En ningún caso se permite la liquidación de estas operaciones mediante el pago en billetes en moneda extranjera o mediante su depósito en cuentas custodia o en cuentas de terceros, excepto que se trate de operaciones contra cable que utilicen cuentas de terceros en el marco de lo contemplado en el punto 4.3.2.3.»
- rep 1 [no_cumplido] fragmento (verbatim): «el Knowledge Graph no contiene información explícita sobre formas de pago expresamente vedadas para estas operaciones específicas» — La respuesta declara no disponer de información sobre las formas vedadas, por lo que no refleja la prohibición normativa expresa de liquidar mediante pago en billetes en moneda extranjera o mediante depósito en cuentas custodia o cuentas de terceros (salvo la excepción del punto 4.3.2.3.).
- rep 2 [no_cumplido] fragmento (verbatim): «el Knowledge Graph no contiene información explícita sobre formas de pago expresamente vedadas para estas operaciones específicas» — La respuesta declara no disponer de información sobre las formas vedadas, por lo que no refleja en absoluto la prohibición expresa de liquidar mediante pago en billetes en moneda extranjera o mediante depósito en cuentas custodia o cuentas de terceros.
- rep 3 [no_cumplido] fragmento (verbatim): «el Knowledge Graph no contiene información explícita sobre formas de pago expresamente vedadas para estas operaciones específicas» — La respuesta declara no disponer de información sobre las formas vedadas, por lo que no refleja la prohibición expresa de liquidar mediante pago en billetes en moneda extranjera o mediante depósito en cuentas custodia o cuentas de terceros (con la excepción del punto 4.3.2.3.).
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

## U6-004 — humano: **correcto** · juez (mapping): **requiere_adjudicacion** [ADJUDICACIÓN]

**Pregunta:** Antes de darle a una empresa acceso al mercado de cambios para un pago al exterior, ¿qué declaración jurada sobre activos externos líquidos y CEDEARs debe presentar el cliente, y a partir de qué valor de tenencias pasa a necesitarse la conformidad previa del BCRA?

**Respuesta del agente (íntegra):**

> Antes de dar acceso al mercado de cambios para un pago al exterior, la entidad debe contar con una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles. A partir de un valor superior al equivalente de USD 100.000 (dólares estadounidenses cien mil) en CEDEARs y/o activos externos líquidos disponibles, la entidad deberá contar con la conformidad previa del BCRA. Si el cliente declara que no posee, al inicio del día, CEDEARs y/o activos externos líquidos disponibles que conjuntamente tengan un valor superior a USD 100.000, la conformidad previa del BCRA no es requerida.

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: True

### criterio 1 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Salvo que cuente con la declaración jurada del cliente al momento del acceso, la entidad debe contar con la conformidad previa del BCRA.
- cita del gold: «La entidad deberá contar con la conformidad previa del BCRA excepto que cuente al momento de acceso al mercado de cambios con una declaración jurada del cliente en la que deje constancia de que:»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona que la conformidad previa del BCRA es el requisito general y que la declaración jurada opera como excepción a ese requisito; invierte la lógica al presentar la declaración jurada como el mecanismo principal sin explicitar la regla base.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona que la conformidad previa del BCRA es la regla general y que la declaración jurada opera como excepción a esa regla; en cambio, presenta la declaración jurada como un requisito previo sin explicitar esa estructura normativa.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona que la conformidad previa del BCRA es el requisito general y que la declaración jurada opera como excepción a ese requisito; en cambio, presenta la declaración jurada como el requisito principal y la conformidad previa como consecuencia de superar el umbral, invirtiendo la lógica normativa.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 2 → modal **dudoso** (['dudoso', 'dudoso', 'no_cumplido']) ⚠ no unánime
- criterio: La declaración jurada debe dejar constancia de que la totalidad de las tenencias de moneda extranjera en el país del cliente están depositadas en cuentas en entidades financieras y de que, al inicio del día en que solicita el acceso, no poseía CEDEARs y/o activos externos líquidos disponibles que conjuntamente superen el equivalente de USD 100.000.
- cita del gold: «3.16.2.1. La totalidad de sus tenencias de moneda extranjera en el país se encuentran depositadas en cuentas en entidades financieras y que no poseía, al inicio del día en que solicita el acceso al mercado, certificados de depósitos argentinos representativos de acciones extranjeras (CEDEARs) y/o activos externos líquidos disponibles que conjuntamente tengan un valor superior al equivalente de USD 100.000 (dólares estadounidenses cien mil).»
- rep 1 [dudoso] fragmento (verbatim): «una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles» — La respuesta menciona tenencias en cuentas de entidades financieras y CEDEARs/activos externos líquidos, pero no reproduce el requisito normativo de que la totalidad de las tenencias de moneda extranjera en el país estén depositadas en cuentas financieras (condición afirmativa), sino que lo presenta de forma ambigua; además omite la referencia al 'inicio del día' como momento de evaluación de las tenencias.
- rep 2 [dudoso] fragmento (verbatim): «una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles» — La respuesta menciona tenencias en cuentas de entidades financieras y CEDEARs/activos externos líquidos, pero no reproduce el requisito de que la totalidad de las tenencias de moneda extranjera en el país estén depositadas en cuentas financieras (condición afirmativa), ni que al inicio del día no se supere el umbral de USD 100.000; la redacción es ambigua respecto a si ambas condiciones están presentes.
- rep 3 [no_cumplido] fragmento (verbatim): «la entidad debe contar con una declaración jurada del cliente en la que conste sus tenencias de moneda extranjera en cuentas de entidades financieras y CEDEARs/activos externos líquidos disponibles» — La respuesta omite el requisito de que la declaración jurada deje constancia de que la TOTALIDAD de las tenencias de moneda extranjera en el país están depositadas en cuentas en entidades financieras; solo menciona las tenencias sin el calificador de totalidad ni la condición de que estén depositadas.
- pre-clasificación mecánica del par: **evidencia** (nulos=0/3, no_verbatim=0/3, fragmentos_distintos=2)

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: El umbral a partir del cual las tenencias hacen necesaria la conformidad previa del BCRA es un valor conjunto superior al equivalente de USD 100.000 (cien mil dólares estadounidenses); si el cliente supera ese monto, la entidad puede aceptar alternativamente una declaración jurada de que no se excede el monto al considerar las situaciones previstas en los incisos i) a vii).
- cita del gold: «En el caso de que el cliente tuviera activos externos líquidos disponibles y/o CEDEARs por un monto superior al establecido en el primer párrafo, la entidad también podrá aceptar una declaración jurada del cliente en la que deje constancia que no se excede tal monto al considerar que, parcial o totalmente, los activos externos líquidos:»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona la posibilidad alternativa de presentar una declaración jurada que acredite que no se excede el umbral al considerar las situaciones previstas en los incisos i) a vii), que es el contenido específico exigido por este criterio.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona la posibilidad alternativa de que, cuando el cliente supera el umbral de USD 100.000, la entidad pueda aceptar una declaración jurada que acredite que no se excede ese monto al considerar las situaciones previstas en los incisos i) a vii).
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la posibilidad alternativa de presentar una declaración jurada que acredite que no se excede el umbral al considerar las situaciones previstas en los incisos i) a vii), que es la alternativa normativa cuando el cliente supera el monto.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 4 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: La declaración jurada también debe incluir el compromiso de liquidar en el mercado de cambios, dentro de los 5 días hábiles de su puesta a disposición, los fondos que reciba en el exterior por cobro de préstamos a terceros, cobro de depósitos a plazo o venta de activos adquiridos/constituidos/otorgados con posterioridad al 28/05/20.
- cita del gold: «3.16.2.2. Se compromete a liquidar en el mercado de cambios, dentro de los 5 (cinco) días hábiles de su puesta a disposición, aquellos fondos que reciba en el exterior originados en el cobro de préstamos otorgados a terceros, el cobro de un depósito a plazo o de la venta de cualquier tipo de activo, cuando el activo hubiera sido adquirido, el depósito constituido o el préstamo otorgado con posterioridad al 28/05/20.»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna referencia al compromiso de liquidar en el mercado de cambios dentro de los 5 días hábiles los fondos recibidos en el exterior por cobro de préstamos, depósitos a plazo o venta de activos constituidos/otorgados con posterioridad al 28/05/20.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace ninguna mención al compromiso de liquidar en el mercado de cambios, dentro de los 5 días hábiles, los fondos recibidos en el exterior por cobro de préstamos, depósitos a plazo o venta de activos constituidos/otorgados con posterioridad al 28/05/20.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en absoluto el compromiso de liquidar en el mercado de cambios, dentro de los 5 días hábiles, los fondos recibidos en el exterior por cobro de préstamos, depósitos a plazo o venta de activos constituidos/otorgados con posterioridad al 28/05/20.
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
- rep 1 [cumplido] fragmento (verbatim): «El acceso al mercado de cambios tiene lugar a partir de la fecha de vencimiento del interés a pagar.» — La respuesta reproduce de forma casi literal el contenido del criterio, indicando correctamente que el acceso ocurre a partir de la fecha de vencimiento del interés.
- rep 2 [cumplido] fragmento (verbatim): «El acceso al mercado de cambios tiene lugar a partir de la fecha de vencimiento del interés a pagar.» — La respuesta reproduce de forma casi literal el contenido del criterio, indicando que el acceso ocurre a partir de la fecha de vencimiento del interés a pagar.
- rep 3 [cumplido] fragmento (verbatim): «El acceso al mercado de cambios tiene lugar a partir de la fecha de vencimiento del interés a pagar.» — La respuesta reproduce de forma casi literal el contenido del criterio, indicando que el acceso ocurre a partir de la fecha de vencimiento del interés.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 2 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: Para precancelar los intereses antes del vencimiento se requiere la conformidad previa del BCRA.
- cita del gold: «En los restantes casos se requerirá la conformidad previa del BCRA para acceder al mercado de cambios para precancelar los servicios de intereses de deudas comerciales por importaciones de bienes y servicios.»
- rep 1 [cumplido] fragmento (verbatim): «Si desea precancelar los intereses antes del vencimiento, se requerirá la conformidad previa del BCRA para acceder al mercado de cambios.» — La respuesta refleja fielmente el requisito normativo de conformidad previa del BCRA para precancelar servicios de intereses de deudas comerciales antes del vencimiento.
- rep 2 [cumplido] fragmento (verbatim): «Si desea precancelar los intereses antes del vencimiento, se requerirá la conformidad previa del BCRA para acceder al mercado de cambios.» — La respuesta refleja fielmente el requisito normativo de conformidad previa del BCRA para precancelar servicios de intereses de deudas comerciales antes del vencimiento.
- rep 3 [cumplido] fragmento (verbatim): «Si desea precancelar los intereses antes del vencimiento, se requerirá la conformidad previa del BCRA para acceder al mercado de cambios.» — La respuesta refleja fielmente el requisito de conformidad previa del BCRA para precancelar servicios de intereses de deudas comerciales antes del vencimiento.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **dudoso** (['dudoso', 'no_cumplido', 'dudoso']) ⚠ no unánime
- criterio: El requisito de esperar al vencimiento no aplica si el cliente es un Vehículo de Proyecto Único (VPU) adherido al RIGI que concreta el pago en el marco del punto 14.2.1.
- cita del gold: «Este requisito no resultará aplicable si el cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que concreta el pago en el marco de lo previsto en el punto 14.2.1.»
- rep 1 [dudoso] fragmento (verbatim): «Esta conformidad previa es obligatoria en casos distintos a VPU-RIGI.» — La respuesta menciona la excepción VPU-RIGI pero de forma muy escueta y referida solo a la conformidad previa del BCRA para precancelación, sin aclarar que la excepción aplica al requisito de esperar al vencimiento ni que debe concretarse en el marco del punto 14.2.1, lo que genera ambigüedad sobre si el criterio está correctamente reflejado.
- rep 2 [no_cumplido] fragmento (verbatim): «Esta conformidad previa es obligatoria en casos distintos a VPU-RIGI.» — La respuesta menciona la excepción VPU-RIGI solo en relación con la conformidad previa del BCRA para precancelación, pero el criterio exige que la excepción aplique al requisito de esperar al vencimiento (criterio 1), no al de precancelación; además, omite la condición específica de que el pago se concrete en el marco del punto 14.2.1.
- rep 3 [dudoso] fragmento (verbatim): «Esta conformidad previa es obligatoria en casos distintos a VPU-RIGI.» — La respuesta menciona la excepción VPU-RIGI pero de forma muy abreviada y referida solo a la conformidad previa del BCRA para precancelación, sin aclarar que la excepción aplica al requisito de esperar al vencimiento ni que debe concretarse en el marco del punto 14.2.1, lo que hace ambiguo si el criterio está plenamente cubierto.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

## U6-019 — humano: **parcial** · juez (mapping): **requiere_adjudicacion** [ADJUDICACIÓN]

**Pregunta:** ¿Qué aspectos del proceso de clasificación y previsionamiento debe documentar la entidad en su manual de procedimientos, y a disposición de quién debe estar ese manual?

**Respuesta del agente (íntegra):**

> Según la regulación del BCRA, la entidad debe documentar en su Manual de procedimientos de clasificación y previsión los siguientes aspectos: (1) los procedimientos implementados, (2) los niveles que intervienen en el análisis y decisión, y (3) demás aspectos de la clasificación y previsionamiento. Además, debe documentarse el análisis efectuado en la clasificación de los deudores, describiendo los procedimientos implementados de manera que permita apreciar el proceso seguido en la materia. Asimismo, la intervención de terceros en la clasificación debe estar prevista en el Manual. Respecto a la disposición del manual, la información disponible en el grafo indica que debe ser aprobado por el Directorio o autoridad equivalente del sujeto obligado, previa toma de conocimiento del Comité de Auditoría y, según corresponda, del Directivo Responsable de Protección de los Usuarios de Servicios Financieros o del Comité de Protección de los Usuarios de Servicios Financieros. Sin embargo, el grafo no contiene información explícita sobre a disposición de quién específicamente debe estar disponible el manual una vez aprobado (por ejemplo, si debe estar a disposición del personal, auditores internos, auditores externos, o del BCRA).

Clasificación auxiliar (3 reps): ['contenido', 'contenido', 'contenido'] · flag respondible: False

### criterio 1 → modal **cumplido** (['cumplido', 'cumplido', 'cumplido'])
- criterio: El manual debe documentar los procedimientos implementados, de manera que permita apreciar el proceso seguido en la materia.
- cita del gold: «3.3.1. Los procedimientos implementados, de manera que permita apreciar el proceso seguido en la materia.»
- rep 1 [cumplido] fragmento (fuga_gold): «los procedimientos implementados, de manera que permita apreciar el proceso seguido en la materia» — La respuesta reproduce casi textualmente el contenido del criterio, incluyendo el calificador 'de manera que permita apreciar el proceso seguido en la materia'.
- rep 2 [cumplido] fragmento (fuga_gold): «los procedimientos implementados, de manera que permita apreciar el proceso seguido en la materia» — La respuesta reproduce casi textualmente el contenido del criterio, incluyendo el calificador clave 'de manera que permita apreciar el proceso seguido en la materia'.
- rep 3 [cumplido] fragmento (fuga_gold): «los procedimientos implementados, de manera que permita apreciar el proceso seguido en la materia» — La respuesta reproduce casi textualmente el contenido del criterio, incluyendo el calificador clave 'de manera que permita apreciar el proceso seguido en la materia'.
- pre-clasificación mecánica del par: **evidencia** (nulos=0/3, no_verbatim=3/3, fragmentos_distintos=1)

### criterio 2 → modal **dudoso** (['cumplido', 'dudoso', 'dudoso']) ⚠ no unánime
- criterio: Debe documentar los niveles que intervienen en el análisis y decisión del otorgamiento de facilidades, la clasificación de deudores y el previsionamiento, según las atribuciones asignadas y los requisitos de aprobación.
- cita del gold: «3.3.2. Los niveles que intervienen en el análisis y decisión en el otorgamiento de las facilidades, la clasificación de los deudores y el previsionamiento de las acreencias, según las atribuciones que les hayan sido asignadas a cada uno de ellos y conforme a los requisitos establecidos para la aprobación de la clasificación y el previsionamiento.»
- rep 1 [cumplido] fragmento (verbatim): «los niveles que intervienen en el análisis y decisión» — La respuesta menciona los niveles que intervienen en el análisis y decisión, aunque omite los detalles sobre atribuciones asignadas y requisitos de aprobación; sin embargo, el núcleo normativo está presente de forma reconocible.
- rep 2 [dudoso] fragmento (verbatim): «los niveles que intervienen en el análisis y decisión» — La respuesta menciona los niveles que intervienen en el análisis y decisión, pero omite los calificadores normativos relevantes: 'en el otorgamiento de las facilidades', 'según las atribuciones que les hayan sido asignadas a cada uno de ellos' y 'conforme a los requisitos establecidos para la aprobación de la clasificación y el previsionamiento', lo que hace incierto si el criterio se cumple con la misma extensión normativa.
- rep 3 [dudoso] fragmento (verbatim): «los niveles que intervienen en el análisis y decisión» — La respuesta menciona los niveles que intervienen en el análisis y decisión, pero omite los calificadores normativos relevantes: 'en el otorgamiento de las facilidades', 'según las atribuciones que les hayan sido asignadas a cada uno de ellos' y 'conforme a los requisitos establecidos para la aprobación de la clasificación y el previsionamiento', lo que hace incierto si el criterio se cumple con la misma extensión normativa.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))

### criterio 3 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Debe documentar el ejercicio de la opción de agrupar financiaciones comerciales de hasta dos veces el importe de referencia junto con los créditos de consumo o vivienda, y la posibilidad de llevar los legajos en medios magnéticos/electrónicos o en lugar distinto de la radicación de la cuenta.
- cita del gold: «3.3.3. El ejercicio de la opción de agrupar las financiaciones de naturaleza comercial de hasta el equivalente a dos veces el importe de referencia establecido en el punto 3.7., cuenten o no con garantías preferidas, junto con los créditos para consumo o vivienda. 3.3.4. La posibilidad de que los legajos de los clientes se lleven en medios magnéticos, electrónicos u otra tecnología similar o se mantengan en un lugar distinto del de radicación de la cuenta»
- rep 1 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la opción de agrupar financiaciones comerciales de hasta dos veces el importe de referencia junto con créditos de consumo o vivienda, ni la posibilidad de llevar legajos en medios magnéticos/electrónicos o en lugar distinto de la radicación de la cuenta.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la opción de agrupar financiaciones comerciales de hasta dos veces el importe de referencia junto con créditos de consumo o vivienda, ni la posibilidad de llevar legajos en medios magnéticos/electrónicos o en lugar distinto de la radicación de la cuenta.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no menciona en ningún momento la opción de agrupar financiaciones comerciales de hasta dos veces el importe de referencia junto con créditos de consumo o vivienda, ni la posibilidad de llevar legajos en medios magnéticos/electrónicos o en lugar distinto de la radicación de la cuenta.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=3/3))

### criterio 4 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: Debe documentar el procedimiento cuando la clasificación se mantenga en planillas separadas del legajo, y el ejercicio de la opción de encomendar la clasificación a profesionales externos.
- cita del gold: «3.3.5. La descripción del procedimiento adoptado, cuando a los fines de la actualización del legajo del cliente la clasificación asignada se mantenga en planillas separadas, que permita la identificación precisa de la clasificación asignada a cada cliente desde la planilla al legajo y viceversa. 3.3.6. El ejercicio de la opción de encomendar a profesionales externos la tarea de clasificación.»
- rep 1 [no_cumplido] fragmento (verbatim): «la intervención de terceros en la clasificación debe estar prevista en el Manual» — La respuesta alude vagamente a 'intervención de terceros' que podría relacionarse con profesionales externos, pero no menciona el procedimiento para clasificación en planillas separadas del legajo ni describe con suficiente precisión la opción de encomendar la clasificación a profesionales externos como lo exige el criterio.
- rep 2 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace referencia al procedimiento cuando la clasificación se mantiene en planillas separadas del legajo, ni al ejercicio de la opción de encomendar la clasificación a profesionales externos.
- rep 3 [no_cumplido] fragmento (null): null (ausencia) — La respuesta no hace referencia al procedimiento cuando la clasificación se mantiene en planillas separadas del legajo, ni al ejercicio de la opción de encomendar la clasificación a profesionales externos.
- pre-clasificación mecánica del par: **evidencia** (nulos=2/3, no_verbatim=0/3, fragmentos_distintos=2)

### criterio 5 → modal **no_cumplido** (['no_cumplido', 'no_cumplido', 'no_cumplido'])
- criterio: El manual debe estar a disposición permanente de la Superintendencia de Entidades Financieras y Cambiarias.
- cita del gold: «El manual deberá estar a disposición permanente de la Superintendencia de Entidades Financieras y Cambiarias.»
- rep 1 [no_cumplido] fragmento (verbatim): «el grafo no contiene información explícita sobre a disposición de quién específicamente debe estar disponible el manual una vez aprobado» — La respuesta declara explícitamente no disponer de información sobre a disposición de quién debe estar el manual, por lo que no refleja el contenido normativo que exige el criterio (disposición permanente de la Superintendencia de Entidades Financieras y Cambiarias).
- rep 2 [no_cumplido] fragmento (verbatim): «el grafo no contiene información explícita sobre a disposición de quién específicamente debe estar disponible el manual una vez aprobado» — La respuesta declara explícitamente no disponer de información sobre a disposición de quién debe estar el manual, por lo que no refleja el contenido normativo que exige el criterio: que debe estar a disposición permanente de la Superintendencia de Entidades Financieras y Cambiarias.
- rep 3 [no_cumplido] fragmento (verbatim): «el grafo no contiene información explícita sobre a disposición de quién específicamente debe estar disponible el manual una vez aprobado» — La respuesta declara explícitamente no disponer de información sobre a disposición de quién debe estar el manual, por lo que no refleja el contenido normativo que exige el criterio: que debe estar a disposición permanente de la Superintendencia de Entidades Financieras y Cambiarias.
- pre-clasificación mecánica del par: **etiqueta** (fragmento consistente en 3/3 (nulos=0/3))
