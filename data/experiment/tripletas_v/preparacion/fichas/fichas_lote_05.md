# U-TRIP-V: fichas del lote 05 (10)

Acta del sorteo `acta_sorteo_V.json` (sha256 `5d6a237e510bcf086db717061dd146eaa9b3181006cb7b1d300164436c720c55`), sellada a las 2026-10-19T14:23:55-03:00; fichas generadas a las 2026-10-19T14:25:19-03:00. Grafo KG-Tanda0-Desarrollo-r2b-sincola-rs1 (`66e745f5…`). Las fichas van en el orden sellado. Criterio (§3.4 del pre-registro): la evidencia sostiene la relación entre esos dos nodos, con sus sujetos, valores, calificadores y modalidad.

Cada ficha trae los dos nodos (tipo, etiqueta, descripción y propiedades), el predicado y la evidencia de cada procedencia: el texto heredado y el propio de la unidad de E0, el tramo literal de cada extremo en esa unidad si lo hay, las páginas y la ruta del PDF con la página. «literal» dice si el tramo está tal cual en el texto (exacta), por tokens (tokens) o no (no).

## V051 · `exceptua_obligacion` · lote_05, 1 de 10

**Origen** — Excepcion «Excepción a permanencia mínima 180 días por categorización inferior» (`Excepcion_no_aplica_la_permanencia_minima_de_180_dias_si_por_aplicacion_de_otras_pautas_co_b3f551`)

- descripción: No aplica la permanencia mínima de 180 días si por aplicación de otras pautas corresponde categorizar al deudor en el nivel inferior
- umbrales (1):
  - valor: 180; unidad: dias; comparacion: minimo_inclusivo; tramo: 180 días

**Predicado** — `exceptua_obligacion`

**Destino** — Obligacion «Permanencia mínima 180 días en categoría con refinanciación y crédito adicional» (`Obligacion_el_deudor_clasificado_en_esta_categoria_que_haya_refinanciado_su_deuda_y_recibid_56ca69`)

- descripción: El deudor clasificado en esta categoría que haya refinanciado su deuda y recibido crédito adicional, mientras dicha financiación adicional no haya sido cancelada, debe permanecer en esta categoría por lo menos 180 días desde la fecha más reciente entre el otorgamiento del crédito adicional o la celebración del acuerdo de refinanciación
- tipo: otra
- umbrales (1):
  - valor: 180; unidad: dias; comparacion: minimo_inclusivo; tramo: por lo menos 180 días

**Evidencia 1 de 1** — `cla::6.5.3.5` · cla · punto 6.5.3.5 · punto_propio · págs. 24

- PDF: `data/experiment/subset/TO_clasificacion_deudores_actual.pdf#page=24`

> *heredado (encabezado, S6, p. 17):* Sección 6. Clasificación de los deudores de la cartera comercial.
>
> *heredado (encabezado, 6.5, p. 19):* 6.5. Niveles de clasificación.
>
> *heredado (intro, 6.5, p. 19):* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si- guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta- llan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi- nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la “Central de deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla- sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con- sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc- tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora- miento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
>
> *heredado (encabezado, 6.5.3, p. 23):* 6.5.3. Con problemas.
>
> *heredado (intro, 6.5.3, p. 23):* El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos, esos problemas pueden resultar en una pérdida para la entidad financiera. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
>
> *propio:* 6.5.3.5. Cuente con refinanciaciones reiteradas y sistemáticas del capital adeudado vin- culadas a una insuficiente capacidad para su pago aun cuando abone los intere- ses y siempre que no haya quitas en el capital, que no se reduzcan las tasas de interés pactadas –salvo que ello derive de las condiciones del mercado– o que no sea necesario aceptar bienes en pago de parte de las obligaciones. Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a 31 días, del 5 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, con más el porcentaje acumulado que pudiera co- rresponder si la refinanciación se hubiera otorgado de haberse encontrado el deudor en categorías inferiores, podrá reclasificárselo en niveles superiores (“en observación” o “en situación normal”) si, además, se observan las otras condi- ciones previstas en la correspondiente categoría. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad”, y en la medida en que dicha financiación adicional no hubiese sido cancelada, de- berá permanecer en esta categoría por lo menos 180 días contados desde la fe- cha en que se otorgó crédito adicional o desde que se celebró el acuerdo de re- financiación, la circunstancia más reciente. Ello, salvo que por aplicación de otras pautas corresponda categorizarlo en el nivel inferior.

- tramo del origen: «Ello, salvo que por aplicación de otras pautas corresponda categorizarlo en el nivel inferior» (literal: exacta)
- tramo del destino: «El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente» (literal: exacta)

---

## V052 · `aplica_a` · lote_05, 2 de 10

**Origen** — Obligacion «Informar altas de comisiones previamente al BCRA» (`Obligacion_las_altas_de_comisiones_de_nuevos_productos_y_o_servicios_y_los_aumentos_en_las__418fea`)

- descripción: Las altas de comisiones de nuevos productos y/o servicios y los aumentos en las comisiones que deseen implementar deberán ser previamente informados al BCRA por la vía consignada en el régimen informativo.
- tipo: reporte_al_supervisor

**Predicado** — `aplica_a`

- tramo del sujeto: «los otros proveedores no financieros de crédito» (literal: exacta)

**Destino** — Sujeto «Proveedores no financieros de crédito» (`Sujeto_proveedor_no_financiero_de_credito`)

- descripción: —
- nivel: clase
- alias: ["PNFC"]

**Evidencia 1 de 1** — `pro::2.5` · pro · punto 2.5 · punto_propio · págs. 21

- PDF: `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=21`

> *heredado (encabezado, S2, p. 5):* Sección 2. Derechos básicos de los usuarios de servicios financieros.
>
> *propio:* 2.5. Información al Banco Central de la República Argentina. Las entidades financieras, los PSPCP, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito que ofrezcan y comerciali- cen productos y/o servicios que se perfeccionan con la firma o aceptación de contratos con cláusulas preestablecidas (contratos de adhesión), deberán informar las comisiones y cargos que cobren a los usuarios de servicios financieros mediante el régimen informativo establecido al efecto. Las altas –comisiones de nuevos productos y/o servicios que deseen comercializar– y los au- mentos en las comisiones que deseen implementar deberán ser previamente informados al BCRA por la vía consignada en el párrafo precedente y luego ser notificadas a los usuarios de servicios financieros. También deberán informar las modificaciones de los cargos. Las reducciones en las comisiones y/o cargos podrán aplicarse sin demora, sin perjuicio de que deberán ser informadas al BCRA dentro de los treinta (30) días corridos siguientes de su apli- cación.

- tramo del origen: «Las altas –comisiones de nuevos productos y/o servicios que deseen comercializar– y los aumentos en las comisiones que deseen implementar deberán ser previamente informados al BCRA por la vía consignada en el párrafo precedente» (literal: exacta)
- tramo del destino: —

---

## V053 · `exceptua` · lote_05, 3 de 10

**Origen** — Excepcion «Excepción: ponderador menor al mínimo en transparencia» (`Excepcion_si_el_ponderador_resultante_del_tratamiento_de_transparencia_es_menor_que_el_pon_2927b7`)

- descripción: Si el ponderador resultante del tratamiento de transparencia es menor que el ponderador mínimo establecido en los apartados a) a c), se podrá aplicar el ponderador menor.

**Predicado** — `exceptua`

**Destino** — Restriccion «Ponderador mínimo 10 % para tramos máxima preferencia STC» (`Restriccion_el_ponderador_resultante_estara_sujeto_a_un_minimo_del_10_para_los_tramos_de_max_d5cf8d`)

- descripción: El ponderador resultante estará sujeto a un mínimo del 10 % para los tramos de máxima preferencia de titulizaciones que cumplan con los criterios STC, y 15 % para los tramos subordinados de esas titulizaciones.
- tipo: limite_cuantitativo
- umbrales (2):
  - valor: 10; unidad: porcentaje; comparacion: coeficiente; tramo: 10 %
  - valor: 15; unidad: porcentaje; comparacion: coeficiente; tramo: 15 %

**Evidencia 1 de 1** — `cap::3.1.11.3` · cap · punto 3.1.11.3 · punto_propio · págs. 44, 45

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=44` · `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=45`

> *heredado (encabezado, S3, p. 29):* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fon- dos.
>
> *heredado (encabezado, 3.1, p. 29):* 3.1. Tratamiento de las titulizaciones.
>
> *heredado (intro, 3.1, p. 29):* Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi- cional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con- ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset- Backed Securities”, ABS) y bonos de titulización hipotecaria (“Mortgage-Backed Securities”, MBS)–, mejoras crediticias, facilidades de liquidez, “swaps” de tasa de interés o de monedas y derivados de crédito. Las reservas (“reserve accounts”), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo tam- bién el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad eco- nómica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una de- terminada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
>
> *heredado (encabezado, 3.1.11, p. 40):* 3.1.11. Enfoque estandarizado.
>
> *heredado (intro, 3.1.11, p. 40):* Los ponderadores de riesgo a aplicar a las posiciones de una titulización y a las exposi- ciones subyacentes de una retitulización para la determinación de la exigencia de capi- tal se establecerán empleando las disposiciones de este punto. Las posiciones de titulización a las que no se les pueda aplicar el enfoque estandariza- do deberán ser ponderadas al 1250 %.
>
> *propio:* 3.1.11.3. Determinación del ponderador de riesgo (RW). El ponderador de riesgo RW a asignar a una posición de titulización se calcu- lará con ajuste a lo siguiente: i) Si D es menor o igual a K , el ponderador será de 1250 %. A ii) Si A es mayor o igual a K , el ponderador será igual a K multiplicado A SSFA(KA) por 12,5. iii) Si K es mayor que A y menor que D, el ponderador será un promedio A ponderado entre 1250 % y 12,5 veces K conforme a la siguiente ex- SSFA(KA) presión: El ponderador para coberturas del riesgo de mercado, tales como “swaps” de moneda o de tasa de interés, se inferirá a partir de una posición de titulización de igual prelación (“pari passu”) con los “swaps” o, si tal posición no existiera, a partir del tramo subordinado más próximo. El ponderador resultante estará sujeto a un mínimo de: a) 15 % para titulizaciones que no cumplan con los criterios STC –punto 3.1.14.–. b) 10 % para los tramos de máxima preferencia de titulizaciones que cumplan con los criterios STC –punto 3.1.14.– y 15 % para los tramos subordinados de esas titulizaciones. c) 100 % para retitulizaciones. Para posiciones de titulización de máxima preferencia se podrá aplicar el tra- tamiento de transparencia (“look-through”) de conformidad con lo previsto en el punto 3.1.6. Si el ponderador que surge de la aplicación de ese tratamiento fuera menor que el ponderador mínimo que corresponda de acuerdo con los apartados a) a c) precedentes, se podrá aplicar el primero.

- tramo del origen: «Si el ponderador que surge de la aplicación de ese tratamiento fuera menor que el ponderador mínimo que corresponda de acuerdo con los apartados a) a c) precedentes, se podrá aplicar el primero.» (literal: exacta)
- tramo del destino: «10 % para los tramos de máxima preferencia de titulizaciones que cumplan con los criterios STC –punto 3.1.14.– y 15 % para los tramos subordinados de esas titulizaciones.» (literal: exacta)

---

## V054 · `condicion_de` · lote_05, 4 de 10

**Origen** — Condicion «Liquidación mediante aplicación directa de moneda extranjera a suscripción primaria» (`Condicion_liquidacion_mediante_aplicacion_directa_de_moneda_extranjera_a_suscripcion_prima_4d6d21`)

- descripción: El requisito de liquidación se considerará cumplimentado cuando el cliente no residente haya aplicado moneda extranjera en forma directa a partir del 23/05/25 a la suscripción primaria de títulos de deuda emitidos por el Tesoro Nacional
- umbrales (1):
  - comparacion: no_determinada; tramo: a partir del 23/05/25

**Predicado** — `condicion_de`

**Destino** — Operacion «Repatriación de servicios de capital, rentas y ventas de inversiones de portafolio» (`Operacion_repatriacion_de_servicios_de_capital_rentas_y_ventas_de_inversiones_de_portafoli_be2a24`)

- descripción: Repatriación por parte de no residentes de servicios de capital, rentas y el producido de las ventas de inversiones de portafolio en instrumentos con cotizaciones en mercados locales autorizados por la Comisión Nacional de Valores, fondos comunes de inversión sin cotización directa conformados por esos instrumentos y/o los depósitos a la vista o a plazo en entidades financieras locales
- tipo: repatriación de inversiones

**Evidencia 1 de 1** — `ext::3.13.1.12` · ext · punto 3.13.1.12 · punto_propio · págs. 39

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=39`

> *heredado (encabezado, S3, p. 16):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
>
> *heredado (chapeau_seccion, S3, p. 16):* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
>
> *heredado (encabezado, 3.13, p. 36):* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
>
> *heredado (intro, 3.13, p. 36):* residentes
>
> *heredado (encabezado, 3.13.1, p. 36):* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
>
> *heredado (intro, 3.13.1, p. 36):* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
>
> *heredado (cierre, 3.13.1, p. 39):* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del “Relevamiento de activos y pasivos externos” el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
>
> *propio:* 3.13.1.12. Repatriación por parte de no residentes de servicios de capital, rentas y el producido de las ventas de inversiones de portafolio en instrumentos con cotizaciones en mercados locales autorizados por la Comisión Nacional de Valores, fondos comunes de inversión sin cotización directa conformados por esos instrumentos y/o los depósitos a la vista o a plazo en entidades financieras locales, siempre que: i) se cuente con la certificación de una entidad financiera local que acredite que la inversión fue constituida con fondos ingresados y liquidados en el mercado local de cambios a partir del 21/04/25. El requisito de liquidación se considerará cumplimentado cuando el cliente no residente haya aplicado moneda extranjera en forma directa a partir del 23/05/25 a la suscripción primaria de títulos de deuda emitidos por el Tesoro Nacional. ii) se cuente con la documentación que demuestre que el monto por el cual se accede al mercado no supera los servicios cobrados y/o el monto efectivamente recibido por la venta de la inversión realizada. En el caso que el cobro de los servicios o venta de la inversión sea percibido en moneda extranjera la repatriación podrá concretarse por hasta el equivalente de ese monto.

- tramo del origen: «El requisito de liquidación se considerará cumplimentado cuando el cliente no residente haya aplicado moneda extranjera en forma directa a partir del 23/05/25 a la suscripción primaria de títulos de deuda emitidos por el Tesoro Nacional» (literal: exacta)
- tramo del destino: «Repatriación por parte de no residentes de servicios de capital, rentas y el producido de las ventas de inversiones de portafolio en instrumentos con cotizaciones en mercados locales autorizados por la Comisión Nacional de Valores, fondos comunes de inversión sin cotización directa conformados por esos instrumentos y/o los depósitos a la vista o a plazo en entidades financieras locales» (literal: exacta)

---

## V055 · `aplica_a` · lote_05, 5 de 10

**Origen** — Obligacion «Informar operaciones realizables con el producto o servicio» (`Obligacion_incluir_en_el_resumen_informativo_las_operaciones_que_se_pueden_realizar_con_el__f3e0cd`)

- descripción: Incluir en el resumen informativo las operaciones que se pueden realizar con el producto o servicio y los canales disponibles para la concreción de las transacciones involucradas.
- tipo: presentacion_informativa

**Predicado** — `aplica_a`

- tramo del sujeto: «Los sujetos obligados» (literal: exacta)

**Destino** — Sujeto «Sujetos obligados (Protección de usuarios)» (`Sujeto_rol_sujeto_obligado_proteccion`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `pro::2.3.1.4` · pro · punto 2.3.1.4 · punto_propio · págs. 10, 11

- PDF: `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=10` · `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=11`

> *heredado (encabezado, S2, p. 5):* Sección 2. Derechos básicos de los usuarios de servicios financieros.
>
> *heredado (encabezado, 2.3, p. 7):* 2.3. Recaudos mínimos de la relación de consumo.
>
> *heredado (encabezado, 2.3.1, p. 7):* 2.3.1. Al momento de la contratación del producto o servicio.
>
> *heredado (intro, 2.3.1, p. 7):* Las entidades financieras, ante requerimientos de apertura de cuentas a la vista por parte de los usuarios de servicios financieros, deberán ofrecer la “Caja de ahorros” en pesos con las prestaciones previstas en el punto 1.8. de las normas sobre “Depósitos de ahorro, cuenta sueldo y especiales” y conservar constancia del ofrecimiento expreso.
>
> *propio:* 2.3.1.4. Resumen informativo del contrato. Los sujetos obligados deberán entregar a los usuarios antes de su formaliza- ción un resumen del contrato en el que se sinteticen, en un lenguaje llano y co- loquial, los términos y alcances de las principales cuestiones que rigen la con- tratación con el objetivo de que el usuario comprenda qué contrata, las cuentas y operaciones que son gratuitas, los costos y riesgos para el usuario asociado a la contratación, enfatizando las cláusulas más significativas para el usuario de acuerdo con las siguientes pautas básicas: i) Las operaciones que se pueden realizar con el producto o servicio de que se trate, así como los canales disponibles para la concreción de las transacciones involucradas. ii) Las comisiones y los cargos asociados al producto o servicio y el meca- nismo para aplicar cambios a las condiciones pactadas según lo dispuesto en el apartado iv) del punto 2.3.4. iii) Los aspectos de gratuidad asociados al producto o servicio contratado. iv) De corresponder, las bonificaciones convenidas, las condiciones para su aplicación y su plazo de vigencia. v) Para las operaciones de financiación de cualquier tipo: todos los aspectos contemplados en el punto 3.2. del TO sobre Tasas de Interés en las Ope- raciones de Crédito. vi) En el caso de préstamos personales, prendarios o hipotecarios y otros préstamos en cuotas: el importe del capital prestado, el monto total a pa- gar, la cantidad de cuotas, periodicidad y fecha de vencimiento, el sistema de amortización de capital y cancelación de intereses. vii) De tratarse de tarjetas de crédito: los límites de compra, de compra en cuotas, de financiación y de adelanto de dinero en efectivo, la forma de de- terminación del pago mínimo y los canales habilitados para consultar la ta- sa de interés vigente. viii) Para cuentas de depósitos y tarjetas de crédito: la periodicidad para la ge- neración del resumen de cuenta y el plazo para su envío, así como el me- canismo y plazo para reclamar en el caso de formular objeciones a algún movimiento o consumo. ix) Para las financiaciones en general, las causales, los efectos de la mora y los procedimientos de ejecución especiales para el caso de las tarjetas de créditos y saldos deudores de las cuentas corrientes. x) Las facultades, procedimientos y canales para la tramitación del cierre de cuentas o de rescisión del contrato. xi) La facultad de revocación según lo establecido en el apartado v) del punto 2.3.1.1. xii) En el caso de multiproductos (paquetes de productos), se deberá informar las cuentas y operaciones gratuitas y especificar el costo de los productos y servicios adicionales, informando sobre lo previsto en el punto 2.3.1.2., comprendiendo también a los seguros ofrecidos por las entidades y a todo tipo de servicios. xiii) Los canales habilitados para la realización de reclamos. xiv) Otras cuestiones particulares que impliquen un riesgo inherente para el usuario.

- tramo del origen: «Las operaciones que se pueden realizar con el producto o servicio de que se trate, así como los canales disponibles para la concreción de las transacciones involucradas.» (literal: exacta)
- tramo del destino: —

---

## V056 · `condicion_de` · lote_05, 6 de 10

**Origen** — Condicion «Documentación estándar para operaciones de pase» (`Condicion_documentacion_estandar_para_operaciones_de_pase__la_documentacion_de_la_operacio_3b2ef8`)

- descripción: La documentación de la operación sea la documentación estándar para las operaciones de pase con los títulos valores en cuestión.

**Predicado** — `condicion_de`

**Destino** — Restriccion «Ponderador 0% — operaciones de pase con participante esencial» (`Restriccion_las_operaciones_de_pase_estaran_sujetas_a_un_ponderador_de_riesgo_del_0_cuando_l_cb3c14`)

- descripción: Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0% cuando la contraparte sea un participante esencial del mercado y se satisfaga la totalidad de las condiciones listadas.
- tipo: limite_cuantitativo
- umbrales (1):
  - valor: 0; unidad: porcentaje; comparacion: coeficiente; tramo: ponderador de riesgo del 0%

**Evidencia 1 de 1** — `cap::5.3.1.3` · cap · punto 5.3.1.3 · punto_propio · págs. 104, 105

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=104` · `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=105`

> *heredado (encabezado, S5, p. 98):* Sección 5. Cobertura del riesgo de crédito.
>
> *heredado (chapeau_seccion, S5, p. 98):* A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las técnicas previstas en el punto 5.1. La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia- ción con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sec- ción 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.
>
> *heredado (encabezado, 5.3, p. 103):* 5.3. Operaciones cubiertas con activos admitidos como garantía.
>
> *heredado (intro, 5.3, p. 103):* La aplicación de la técnica de cobertura mediante activos admitidos como garantía dependerá del método elegido.
>
> *heredado (encabezado, 5.3.1, p. 103):* 5.3.1. Método simple.
>
> *heredado (intro, 5.3.1, p. 103):* Con este método, el ponderador de riesgo de la contraparte se sustituye por el pondera- dor de riesgo del activo mediante el cual se cubre –parcial o totalmente– la exposición –conforme a la tabla de ponderadores prevista en la Sección 2.–.
>
> *propio:* 5.3.1.3. Excepciones a la aplicación del ponderador de riesgo mínimo. El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos: i) Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0% cuando la contraparte sea un “participante esencial del mercado” (punto 5.3.1.4.) y, además, se satisfaga la totalidad de las siguientes condiciones: a) La exposición y el activo recibido en garantía consisten en efectivo o en títulos valores emitidos por el sector público no financiero sujetos a un ponderador de riesgo del 0%. b) La exposición y el activo recibido en garantía estén denominados en la misma moneda. c) El plazo de vencimiento de la operación sea de un día hábil o bien la ex- posición y el activo recibido en garantía se valúen diariamente a precios de mercado y estén sujetos a liquidación/reposición diaria de márgenes. d) Cuando una de las partes incumpla la liquidación/reposición de márge- nes, el tiempo exigido entre la última valuación a precio de mercado pre- via al incumplimiento y la liquidación del activo no supere los cuatro días hábiles. e) La operación se liquide a través de un sistema previamente comprobado para este tipo de operaciones. f) La documentación de la operación sea la documentación estándar para las operaciones de pase con los títulos valores en cuestión. g) La documentación de la operación contemple que, en el caso de que una de las partes incumpla la obligación de entregar efectivo o títulos va- lores o de reponer el margen o cualquier otra obligación, la operación se- rá inmediatamente cancelable. h) Ante cualquier evento de incumplimiento, la entidad financiera conserve el derecho irrestricto y legalmente exigible de tomar inmediatamente po- sesión del activo y liquidarlo para cobrar sus acreencias. ii) Las operaciones de pase en las cuales la contraparte no sea un “participan- te esencial del mercado” (punto 5.3.1.4.), pero que satisfagan las restantes condiciones establecidas en el acápite i), estarán sujetas a un ponderador de riesgo del 10%. iii) Las operaciones en las que la exposición y el activo recibido en garantía es- tén denominados en la misma moneda y el mencionado activo recibido sea efectivo depositado en la entidad financiera, o títulos valores emitidos por el sector público no financiero o instrumentos de regulación monetaria emitidos por el BCRA a los que les corresponda un ponderador de riesgo del 0% y a cuyo valor de mercado se le haya aplicado un aforo de al menos el 20%, es- tarán sujetas a un ponderador de riesgo del 0%.

- tramo del origen: «La documentación de la operación sea la documentación estándar para las operaciones de pase con los títulos valores en cuestión.» (literal: exacta)
- tramo del destino: «Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0% cuando la contraparte sea un "participante esencial del mercado" (punto 5.3.1.4.) y, además, se satisfaga la totalidad de las siguientes condiciones:» (literal: exacta)

---

## V057 · `aplica_a` · lote_05, 7 de 10

**Origen** — Operacion «Deducción de importes de activos por requerimiento SEFyC» (`Operacion_deduccion_de_importes_de_activos_por_requerimiento_sefyc__cap_8_4_1_11_09c733`)

- descripción: Deducción de importes de activos u otros conceptos comprendidos ante requerimiento de la SEFyC, cuando las registraciones contables no reflejen en forma precisa la realidad económica y jurídica de las operaciones o se hayan llevado a cabo acciones o ardides para desnaturalizar o disimular el verdadero carácter o alcance de las operaciones.
- tipo: Deducción de activos

**Predicado** — `aplica_a`

- tramo del sujeto: «las entidades financieras» (literal: exacta)

**Destino** — Sujeto «Entidades financieras» (`Sujeto_entidad_financiera`)

- descripción: —
- nivel: clase
- alias: ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]

**Evidencia 1 de 1** — `cap::8.4.1.11` · cap · punto 8.4.1.11 · punto_propio · págs. 164

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=164`

> *heredado (encabezado, S8, p. 154):* Sección 8. Responsabilidad patrimonial computable.
>
> *heredado (encabezado, 8.4, p. 162):* 8.4. Conceptos deducibles.
>
> *heredado (encabezado, 8.4.1, p. 162):* 8.4.1. Conceptos deducibles del capital ordinario de nivel uno (CD ).
>
> *heredado (intro, 8.4.1, p. 162):* COn1
>
> *propio:* 8.4.1.11. Ante requerimiento que formule la SEFyC y con efectividad a la fecha que en cada caso se indique, las entidades financieras deberán deducir los importes de los activos u otros conceptos comprendidos, cuando de los elementos puestos a disposición de los inspectores actuantes surja que las registraciones contables efectuadas por las entidades no reflejan en forma precisa la realidad económica y jurídica de las operaciones o que se han llevado a cabo acciones o ardides para desnaturalizar o disimular el verdadero carácter o alcance de las operaciones. La afectación de la RPC por aplicación de lo señalado determinará la obligación de verificar el encuadramiento de las distintas normas que utilicen como base la citada responsabilidad, desde el mes en que tenga efecto el requerimiento for- mulado y, en su caso, deberán ingresarse los cargos resultantes dentro del término de 10 días hábiles, contados desde la fecha de notificación del reque- rimiento. En el supuesto de ingreso fuera del término fijado, deberán abonarse los pertinentes intereses por mora que surjan de la aplicación de cada norma infringida.

- tramo del origen: «las entidades financieras deberán deducir los importes de los activos u otros conceptos comprendidos» (literal: exacta)
- tramo del destino: —

---

## V058 · `exceptua` · lote_05, 8 de 10

**Origen** — Excepcion «Excepción — pagarés con oferta pública conforme RG 1.003/24» (`Excepcion_excepcion_a_la_prohibicion_de_acceso_al_mercado_de_cambios_para_el_pago_de_deuda_6cd392`)

- descripción: Excepción a la prohibición de acceso al mercado de cambios para el pago de deudas entre residentes: se permite la cancelación en el país a partir de su vencimiento de capital e intereses de pagarés con oferta pública emitidos conforme a la Resolución General 1.003/24 de la CNV

**Predicado** — `exceptua`

**Destino** — Restriccion «Prohibición acceso mercado cambios — deudas entre residentes» (`Restriccion_se_prohibe_el_acceso_al_mercado_de_cambios_para_el_pago_de_deudas_y_otras_obliga_ee2a38`)

- descripción: Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19, excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de pagarés con oferta pública emitidos conforme a la Resolución General 1.003/24 de la CNV
- tipo: prohibicion

**Evidencia 1 de 1** — `ext::3.6.1.4` · ext · punto 3.6.1.4 · punto_propio · págs. 28

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=28`

> *heredado (encabezado, S3, p. 16):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
>
> *heredado (chapeau_seccion, S3, p. 16):* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
>
> *heredado (encabezado, 3.6, p. 28):* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
>
> *heredado (intro, 3.6, p. 28):* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
>
> *heredado (encabezado, 3.6.1, p. 28):* 3.6.1. Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras
>
> *heredado (intro, 3.6.1, p. 28):* obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19, excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de:
>
> *propio:* 3.6.1.4. pagarés con oferta pública emitidos en el marco de la Resolución General 1.003/24 de la Comisión Nacional de Valores (CNV) y concordantes, denominados y suscriptos en moneda extranjera y cuyos servicios de capital e intereses sean pagaderos en moneda extranjera en el país, en la medida que la totalidad de los fondos obtenidos hayan sido liquidados en el mercado de cambios.

- tramo del origen: «excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de: […] pagarés con oferta pública emitidos en el marco de la Resolución General 1.003/24 de la Comisión Nacional de Valores (CNV) y concordantes, denominados y suscriptos en moneda extranjera y cuyos servicios de capital e intereses sean pagaderos en moneda extranjera en el país» (literal: exacta)
- tramo del destino: «Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19, excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de: […] pagarés con oferta pública emitidos en el marco de la Resolución General 1.003/24 de la Comisión Nacional de Valores (CNV) y concordantes, denominados y suscriptos en moneda extranjera y cuyos servicios de capital e intereses sean pagaderos en moneda extranjera en el país» (literal: exacta)

---

## V059 · `requiere` · lote_05, 9 de 10

**Origen** — Operacion «Designación de entidad financiera para seguimiento» (`Operacion_designacion_de_entidad_financiera_para_seguimiento__ext_7_10_2_4_f34369`)

- descripción: Designación de una entidad financiera local para realizar el seguimiento del proyecto comprendido en el régimen de fomento de inversión para las exportaciones
- tipo: Designación de entidad financiera

**Predicado** — `requiere`

**Destino** — Obligacion «Cumplimentar requerimientos de información del BCRA» (`Obligacion_la_entidad_financiera_designada_debe_cumplimentar_los_requerimientos_de_informac_ab5c64`)

- descripción: La entidad financiera designada debe cumplimentar los requerimientos de información que establezca el BCRA respecto a estas operaciones
- tipo: reporte_al_supervisor

**Evidencia 1 de 1** — `ext::7.10.2.4` · ext · punto 7.10.2.4 · punto_propio · págs. 100, 101

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=100` · `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=101`

> *heredado (encabezado, S7, p. 80):* Sección 7. Cobros de exportaciones de bienes.
>
> *heredado (encabezado, 7.10, p. 99):* 7.10. Operaciones habilitadas para la aplicación de cobros de exportaciones de bienes en el marco
>
> *heredado (intro, 7.10, p. 99):* del régimen de fomento de inversión para las exportaciones (Decreto 234/21).
>
> *heredado (encabezado, 7.10.2, p. 100):* 7.10.2. La aplicación de las divisas a las operaciones señaladas será admitida en la medida
>
> *heredado (intro, 7.10.2, p. 100):* que se verifiquen la totalidad de las siguientes condiciones:
>
> *propio:* 7.10.2.4. Los exportadores que opten por este mecanismo deberán designar una entidad financiera local para que realice el seguimiento del proyecto comprendido en el régimen mencionado, la cual se encargará de: i) Constatar que el exportador posee un “Certificado de Inversión para Exportación” emitido por la Autoridad de Aplicación. ii) Certificar que las exportaciones de bienes cuyos cobros se pretende aplicar están vinculadas al proyecto aprobado por la Autoridad de Aplicación. iii) Efectuar el seguimiento de los permisos de embarques cuyos cobros se pretenda aplicar acorde a lo previsto en el presente punto. iv) Efectuar el registro de las importaciones de bienes de capital que cumplen lo previsto en el punto 7.10.2.2.ii) y realizar el seguimiento de los correspondientes despachos de importación. v) Efectuar el seguimiento de los fondos pendientes de aplicación. vi) Cumplimentar los requerimientos de información que establezca el BCRA respecto a estas operaciones. La entidad nominada por un exportador deberá notificar tal situación al BCRA mediante nota dirigida a la Gerencia Principal de Exterior y Cambios dentro de los 30 (treinta) días corridos de producida su nominación. La nota por presentar en el BCRA deberá contener como mínimo, copia del “Certificado de Inversión para Exportación”, la descripción del proyecto, el monto proyectado a invertir y la composición del financiamiento. Asimismo, deberá notificar al BCRA cada inversión ingresada para financiar el proyecto, informando su monto, sus características y, en caso de que sea un endeudamiento, las condiciones de pago establecidas. En la nota deberá consignarse el número de identificación de la operación (número APX) en el marco del “Seguimiento de anticipos y otras financiaciones de exportación de bienes” e indicar si la operación encuadra en lo previsto en el punto 7.9. En caso de que la inversión corresponda a una operación comprendida en el punto 7.10.2.2.ii) también deberá consignarse en la nota el número de oficialización correspondiente.

- tramo del origen: «Los exportadores que opten por este mecanismo deberán designar una entidad financiera local para que realice el seguimiento del proyecto comprendido en el régimen mencionado» (literal: exacta)
- tramo del destino: «Cumplimentar los requerimientos de información que establezca el BCRA respecto a estas operaciones» (literal: exacta)

---

## V060 · `aplica_a` · lote_05, 10 de 10

**Origen** — Obligacion «Convertir derivados a posiciones nocionales» (`Obligacion_convertir_instrumentos_derivados_futuros_forwards_swaps_y_opciones_tratadas_conf_1a6633`)

- descripción: Convertir instrumentos derivados (futuros, forwards, swaps y opciones tratadas conforme al punto 6.6.3 luego de aplicar el método delta-plus) sobre productos básicos y posiciones fuera de balance afectadas por cambios en precios de productos básicos en posiciones nocionales de esos productos
- tipo: calculo

**Predicado** — `aplica_a`

- tramo del sujeto: «la entidad» (literal: exacta)

**Destino** — Sujeto «Entidades alcanzadas (Capitales Mínimos)» (`Sujeto_rol_alcance_capmin`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `cap::6.5.2` · cap · punto 6.5.2 · punto_propio · págs. 133, 134

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=133` · `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=134`

> *heredado (encabezado, S6, p. 116):* Sección 6. Capital mínimo por riesgo de mercado.
>
> *heredado (encabezado, 6.5, p. 133):* 6.5. Exigencia de capital por riesgo de posiciones en productos básicos –“commodities”–.
>
> *heredado (intro, 6.5, p. 133):* Cubre el riesgo de mantener posiciones en productos básicos, incluidos metales preciosos ex- cepto el oro (tratado en el punto 6.4.). A los fines de estas normas, se define como producto básico (o materia prima) –“commodities”– a todo producto físico negociado o negociable en un mercado secundario.
>
> *propio:* 6.5.2. Medición de la exposición. Las posiciones cortas y largas podrán netearse a efectos de calcular las posiciones abiertas, siempre que se trate de un mismo producto básico. No se admite la compen- sación entre posiciones en diferentes productos básicos ni entre subcategorías diferen- tes del mismo producto básico. Para calcular los requerimientos de capital se deberá expresar cada posición en un pro- ducto básico (al contado y a plazo) en términos de la correspondiente unidad estándar de medida (barriles, kilos, gramos, etc.). La posición neta de cada producto básico se convertirá a pesos utilizando su precio al contado y, si estuviera expresado en moneda extranjera, convirtiéndolo al tipo de cambio de referencia del dólar estadounidense di- fundido por el BCRA vigente al cierre de las operaciones del día. De tratarse de mone- das extranjeras distintas del dólar estadounidense, se convertirán a esta moneda utili- zando los tipos de pase comunicados por la mesa de operaciones del BCRA. Los instrumentos derivados –tales como futuros, “forwards”, “swaps” y las opciones tra- tadas conforme al punto 6.6.3. (luego de aplicar el método delta-plus)– sobre productos básicos y las posiciones fuera de balance a las que les afecten los cambios en los pre- cios de los productos básicos deberán convertirse en posiciones nocionales de esos productos conforme a lo siguiente: − Los futuros y “forwards” deberán expresarse como cantidades nocionales de barriles, kilos, etc. − Los “swaps” en los que un tramo sea un precio fijo y el otro el precio de mercado vi- gente se tratarán como una posición larga si la entidad financiera paga precio fijo y recibe variable, y corta en el caso contrario. − Los “swaps” referidos a diferentes productos básicos no podrán compensarse.

- tramo del origen: «Los instrumentos derivados –tales como futuros, "forwards", "swaps" y las opciones tratadas conforme al punto 6.6.3. (luego de aplicar el método delta-plus)– sobre productos básicos y las posiciones fuera de balance a las que les afecten los cambios en los precios de los productos básicos deberán convertirse en posiciones nocionales de esos productos» (literal: exacta)
- tramo del destino: —

---

