# U-E3-LISTAS, O3 (b): intento 0 contra final, por unidad (sin API)

## ext::2.6.1.2 — final: reintento_1:companero (aceptado_tras_reintento); cambió
Entidades 1 → 4; relaciones 0 → 3.
- Entran: Condicion «condicion: certificacion incremento exportaciones economia conocimiento»; Condicion «condicion: montos divisas no alcanzados por otro tratamiento cambiario»; Definicion «sujeto alcanzado: personas juridicas inscriptas registro nacional beneficiarios»; Excepcion «excepcion liquidacion cobros exportaciones economia conocimiento»
- Salen: Condicion «certificacion de incremento de exportaciones»
- Relaciones que entran: aplica_a excepcion liquidacion cobros exportaciones economia conocimiento sujeto_beneficiario_economia_conocimiento; condicion_de condicion: certificacion incremento exportaciones economia conocimiento excepcion liquidacion cobros exportaciones economia conocimiento; condicion_de condicion: montos divisas no alcanzados por otro tratamiento cambiario excepcion liquidacion cobros exportaciones economia conocimiento

## ext::3.13.1.1 — final: reintento_1:companero (aceptado_tras_reintento); cambió
Entidades 1 → 2; relaciones 0 → 0.
- Entran: Definicion «organismos internacionales — agencias oficiales de credito»; Excepcion «excepcion — repatriacion inversiones no residentes»
- Salen: Excepcion «excepcion organismos internacionales y agencias oficiales»

## ext::3.13.1.6 — final: reintento_1:companero (aceptado_tras_reintento); cambió
Entidades 2 → 5; relaciones 1 → 3.
- Entran: Excepcion «excepcion conformidad previa transferencias beneficios estatales»; Operacion «compras moneda extranjera no residentes»; Operacion «repatriacion inversiones no residentes»; Operacion «transferencias a cuentas bancarias exterior personas humanas»; Restriccion «conformidad previa bcra repatriacion»
- Salen: Condicion «fondos asociados a beneficios estatales»; Operacion «transferencias a cuentas bancarias en el exterior»
- Relaciones que entran: exceptua excepcion conformidad previa transferencias beneficios estatales conformidad previa bcra repatriacion; limita conformidad previa bcra repatriacion compras moneda extranjera no residentes; limita conformidad previa bcra repatriacion repatriacion inversiones no residentes
- Relaciones que salen: condicion_de fondos asociados a beneficios estatales transferencias a cuentas bancarias en el exterior

## ext::3.16.2.1 — final: reintento_1:companero (aceptado_tras_reintento); cambió
Entidades 12 → 13; relaciones 0 → 7.
- Entran: Condicion «activos transferidos a cuenta de corresponsalia»; Condicion «activos utilizados durante la jornada para pagos en mercado local»; Condicion «ausencia de cedears y activos externos liquidos superiores a usd 100.000»; Condicion «fondos de cobros de exportaciones o enajenacion de activos no financieros»; Condicion «fondos de desembolsos de endeudamientos ultimos 180 dias»; Condicion «fondos de emisiones de titulos de deuda ultimos 120 dias»; Condicion «fondos de endeudamientos financieros punto 3.5»; Condicion «fondos de ventas de titulos valores con liquidacion en moneda extranjera»; Excepcion «exclusion de fondos de reserva o garantia en el exterior»; Obligacion «constar en declaracion jurada valor de activos externos liquidos y montos asignados»; Potestad «facultad de aceptar declaracion jurada cuando activos externos liquidos superan usd 100.000»
- Salen: Condicion «no posesion de cedears y activos externos liquidos superiores a usd 100.000»; Excepcion «excepcion — activos externos liquidos utilizados para pagos en mercado local»; Excepcion «excepcion — activos transferidos a cuenta de corresponsalia»; Excepcion «excepcion — fondos de cobros de exportaciones y enajenacion de activos»; Excepcion «excepcion — fondos de desembolsos de endeudamientos desde 29/11/24»; Excepcion «excepcion — fondos de emisiones de titulos de deuda ultimos 120 dias»; Excepcion «excepcion — fondos de endeudamientos financieros punto 3.5.»; Excepcion «excepcion — fondos de ventas de titulos valores punto 3.16.3.6.iii)»; Obligacion «declaracion jurada — constar valor de activos externos liquidos y montos asignados»; Restriccion «exclusion de fondos de reserva o garantia de activos externos liquidos»
- Cambian de descripción: Condicion «tenencias de moneda extranjera depositadas en entidades financieras»; Definicion «activos externos liquidos»
- Relaciones que entran: condicion_de activos transferidos a cuenta de corresponsalia facultad de aceptar declaracion jurada cuando activos externos liquidos superan usd 100.000; condicion_de activos utilizados durante la jornada para pagos en mercado local facultad de aceptar declaracion jurada cuando activos externos liquidos superan usd 100.000; condicion_de fondos de cobros de exportaciones o enajenacion de activos no financieros facultad de aceptar declaracion jurada cuando activos externos liquidos superan usd 100.000; condicion_de fondos de desembolsos de endeudamientos ultimos 180 dias facultad de aceptar declaracion jurada cuando activos externos liquidos superan usd 100.000; condicion_de fondos de emisiones de titulos de deuda ultimos 120 dias facultad de aceptar declaracion jurada cuando activos externos liquidos superan usd 100.000; condicion_de fondos de endeudamientos financieros punto 3.5 facultad de aceptar declaracion jurada cuando activos externos liquidos superan usd 100.000; condicion_de fondos de ventas de titulos valores con liquidacion en moneda extranjera facultad de aceptar declaracion jurada cuando activos externos liquidos superan usd 100.000

## ext::3.18.1.1 — final: e1 (cola_humana); no cambió
Entidades 3 → 3; relaciones 2 → 2.

## ext::3.3.3.1 — final: reintento_1:companero (aceptado_tras_reintento); cambió
Entidades 1 → 4; relaciones 0 → 5.
- Entran: Condicion «acreedor contraparte vinculada»; Condicion «vencimiento intereses hasta 04/07/24»; Excepcion «excepcion — operaciones propias entidades financieras locales»; Obligacion «conformidad previa bcra — acreedor vinculado»
- Salen: Excepcion «excepcion operaciones propias entidades financieras locales»
- Relaciones que entran: aplica_a conformidad previa bcra — acreedor vinculado sujeto_rol_entidad_autorizada_exterior; aplica_a excepcion — operaciones propias entidades financieras locales sujeto_entidad_financiera; condicion_de acreedor contraparte vinculada conformidad previa bcra — acreedor vinculado; condicion_de vencimiento intereses hasta 04/07/24 conformidad previa bcra — acreedor vinculado; exceptua_obligacion excepcion — operaciones propias entidades financieras locales conformidad previa bcra — acreedor vinculado

## ext::3.3.3.2 — final: reintento_1:companero (aceptado_tras_reintento); cambió
Entidades 1 → 3; relaciones 0 → 2.
- Entran: Condicion «cliente con certificacion aumento exportaciones 2021-2023»; Excepcion «excepcion conformidad previa — certificacion exportaciones»; Obligacion «conformidad previa bcra — intereses contraparte vinculada»
- Salen: Condicion «cliente con certificacion aumento exportaciones»
- Relaciones que entran: condicion_de cliente con certificacion aumento exportaciones 2021-2023 excepcion conformidad previa — certificacion exportaciones; exceptua_obligacion excepcion conformidad previa — certificacion exportaciones conformidad previa bcra — intereses contraparte vinculada

## ext::3.5.3.5 — final: reintento_1:companero (aceptado_tras_reintento); cambió
Entidades 2 → 6; relaciones 1 → 0.
- Entran: Condicion «anterioridad maxima 3 dias habiles»; Condicion «plazo minimo desde emision — titulos 08/11/24 a 20/04/25»; Condicion «plazo minimo desde emision — titulos 21/04/25 a 15/05/25»; Condicion «plazo minimo desde emision — titulos a partir de 16/05/25»; Excepcion «excepcion vpu-rigi — precancelacion de capital e intereses»; Operacion «precancelacion de capital e intereses — vpu-rigi»
- Salen: Condicion «vpu adherido al rigi precancela capital o intereses»; Excepcion «excepcion — acceso al mercado de cambios sin conformidad previa del bcra para vpu rigi»
- Relaciones que salen: condicion_de vpu adherido al rigi precancela capital o intereses excepcion — acceso al mercado de cambios sin conformidad previa del bcra para vpu rigi

## ext::3.5.4.3 — final: reintento_1:companero (aceptado_tras_reintento); cambió
Entidades 1 → 3; relaciones 0 → 2.
- Entran: Condicion «vigencia requisito conformidad previa bcra»; Excepcion «excepcion conformidad previa — condiciones cumplidas»
- Cambian de descripción: Condicion «vida promedio endeudamiento minimo 2 anos»
- Relaciones que entran: condicion_de vida promedio endeudamiento minimo 2 anos excepcion conformidad previa — condiciones cumplidas; condicion_de vigencia requisito conformidad previa bcra excepcion conformidad previa — condiciones cumplidas

## ext::3.5.6.1 — final: e1 (cola_humana); no cambió
Entidades 1 → 1; relaciones 0 → 0.

## ext::3.5.6.2 — final: reintento_1:companero (aceptado_tras_reintento); cambió
Entidades 3 → 4; relaciones 2 → 4.
- Entran: Excepcion «excepcion — vida promedio ≥6 meses y fondos ingresados desde 21/04/25»; Obligacion «conformidad previa bcra — cancelacion endeudamientos con contraparte vinculada»
- Salen: Excepcion «excepcion conformidad previa bcra — endeudamiento con contraparte vinculada»
- Cambian de descripción: Condicion «fondos ingresados y liquidados desde 21/04/25»; Condicion «vida promedio minima 6 meses»
- Relaciones que entran: aplica_a conformidad previa bcra — cancelacion endeudamientos con contraparte vinculada sujeto_rol_entidad_autorizada_exterior; condicion_de fondos ingresados y liquidados desde 21/04/25 excepcion — vida promedio ≥6 meses y fondos ingresados desde 21/04/25; condicion_de vida promedio minima 6 meses excepcion — vida promedio ≥6 meses y fondos ingresados desde 21/04/25; exceptua_obligacion excepcion — vida promedio ≥6 meses y fondos ingresados desde 21/04/25 conformidad previa bcra — cancelacion endeudamientos con contraparte vinculada
- Relaciones que salen: condicion_de fondos ingresados y liquidados desde 21/04/25 excepcion conformidad previa bcra — endeudamiento con contraparte vinculada; condicion_de vida promedio minima 6 meses excepcion conformidad previa bcra — endeudamiento con contraparte vinculada

## ext::3.5.6.7 — final: reintento_1:companero (aceptado_tras_reintento); cambió
Entidades 1 → 4; relaciones 0 → 3.
- Entran: Condicion «endeudamiento encuadra en mecanismo punto 7.11»; Condicion «fecha de acceso consistente con mecanismo punto 7.11»; Excepcion «excepcion conformidad previa — endeudamiento en mecanismo 7.11»; Obligacion «conformidad previa bcra — endeudamientos con acreedor vinculado»
- Salen: Excepcion «excepcion — endeudamiento en mecanismo 7.11»
- Relaciones que entran: condicion_de endeudamiento encuadra en mecanismo punto 7.11 excepcion conformidad previa — endeudamiento en mecanismo 7.11; condicion_de fecha de acceso consistente con mecanismo punto 7.11 excepcion conformidad previa — endeudamiento en mecanismo 7.11; exceptua_obligacion excepcion conformidad previa — endeudamiento en mecanismo 7.11 conformidad previa bcra — endeudamientos con acreedor vinculado

## ext::3.6.1.1 — final: e1 (cola_humana); no cambió
Entidades 3 → 3; relaciones 1 → 1.

## ext::3.6.1.2 — final: reintento_1:companero (aceptado_tras_reintento); cambió
Entidades 2 → 5; relaciones 0 → 4.
- Entran: Condicion «condicion — incremento vida promedio obligaciones»; Condicion «condicion — refinanciamiento deudas punto 3.6.2»; Excepcion «excepcion — cancelacion titulos deuda refinanciamiento»; Operacion «cancelacion en el pais — titulos deuda vencidos»; Restriccion «prohibicion acceso mercado cambios — deudas residentes»
- Salen: Excepcion «excepcion acceso mercado cambios — titulos deuda refinanciamiento»; Operacion «emision titulos deuda refinanciamiento»
- Relaciones que entran: condicion_de condicion — incremento vida promedio obligaciones excepcion — cancelacion titulos deuda refinanciamiento; condicion_de condicion — refinanciamiento deudas punto 3.6.2 excepcion — cancelacion titulos deuda refinanciamiento; exceptua excepcion — cancelacion titulos deuda refinanciamiento prohibicion acceso mercado cambios — deudas residentes; prohibe prohibicion acceso mercado cambios — deudas residentes cancelacion en el pais — titulos deuda vencidos

## ext::3.6.1.6 — final: reintento_1:companero (aceptado_tras_reintento); cambió
Entidades 2 → 6; relaciones 1 → 4.
- Entran: Condicion «deudas concertadas a partir del 01/09/19»; Condicion «refinanciaciones no anticipan vencimientos»; Excepcion «excepcion — cancelacion en pais a partir de vencimiento»; Excepcion «excepcion — reestructuraciones sin desembolsos con refinanciaciones no anticipadas»; Operacion «reestructuracion de deudas sin desembolsos»; Restriccion «prohibicion acceso mercado cambios — deudas entre residentes»
- Salen: Condicion «condicion refinanciaciones no anticipen vencimientos»; Excepcion «excepcion reestructuraciones sin desembolsos»
- Relaciones que entran: condicion_de deudas concertadas a partir del 01/09/19 prohibicion acceso mercado cambios — deudas entre residentes; condicion_de refinanciaciones no anticipan vencimientos excepcion — reestructuraciones sin desembolsos con refinanciaciones no anticipadas; exceptua excepcion — cancelacion en pais a partir de vencimiento prohibicion acceso mercado cambios — deudas entre residentes; exceptua excepcion — reestructuraciones sin desembolsos con refinanciaciones no anticipadas prohibicion acceso mercado cambios — deudas entre residentes
- Relaciones que salen: condicion_de condicion refinanciaciones no anticipen vencimientos excepcion reestructuraciones sin desembolsos

## ext::3.6.4.1 — final: reintento_1:companero (aceptado_tras_reintento); cambió
Entidades 2 → 4; relaciones 2 → 3.
- Entran: Condicion «cumplimiento de totalidad de condiciones del item»; Excepcion «excepcion conformidad previa — financiaciones por consumos en tarjeta»; Operacion «financiacion de consumos en moneda extranjera»; Restriccion «acceso anticipado al mercado de cambios requiere conformidad previa»
- Salen: Condicion «deuda originada en financiacion por tarjeta»; Operacion «financiacion en moneda extranjera por tarjeta»
- Relaciones que entran: aplica_a acceso anticipado al mercado de cambios requiere conformidad previa sujeto_entidad_financiera; condicion_de cumplimiento de totalidad de condiciones del item excepcion conformidad previa — financiaciones por consumos en tarjeta; exceptua excepcion conformidad previa — financiaciones por consumos en tarjeta acceso anticipado al mercado de cambios requiere conformidad previa
- Relaciones que salen: aplica_a financiacion en moneda extranjera por tarjeta sujeto_entidad_financiera; condicion_de deuda originada en financiacion por tarjeta financiacion en moneda extranjera por tarjeta

## ext::3.6.4.2 — final: e1 (cola_humana); no cambió
Entidades 6 → 6; relaciones 5 → 5.
