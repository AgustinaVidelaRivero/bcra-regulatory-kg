## Unidad `ext::7.1.1::intro` (intro)
- herencia: [encabezado 7.1.1] 7.1.1. Exportaciones oficializadas a partir del 02/09/19.
- texto propio: El contravalor en divisas de la exportación hasta alcanzar el valor facturado según la
condición de venta pactada deberá ingresarse al país y liquidarse en el mercado de
cambios.
En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al
Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad
de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198
de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicios resultará
aplicable lo dispuesto en los puntos 14.1.1. y 14.1.2., según corresponda.
El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse
en los siguientes plazos a computar desde la fecha del cumplido de embarque
otorgado por la Aduana:
- entidades de la unidad:
  - `e1` Operacion: Ingreso y liquidación de contravalor en divisas — Ingreso al país y liquidación en el mercado de cambios del contravalor en divisas de la exportación hasta alcanzar el valor facturado según la condición de venta pactada.
  - `e2` Obligacion: Ingreso y liquidación de divisas en plazos establecidos — El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse en los plazos establecidos a computar desde la fecha del cumplido de embarque otorgado por la Aduana.
  - `e3` Condicion: Cliente es VPU adherido al RIGI con declaración de beneficios — El cliente es un Vehículo de Proyecto Único (VPU) adherido al RIGI que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios del artículo 198 de la Ley 27.742 en materia de c
  - `e4` Excepcion: Excepción régimen de cobro para VPU-RIGI — Cuando el cliente sea un VPU adherido al RIGI que declaró hacer uso de los beneficios del artículo 198 de la Ley 27.742, resulta aplicable lo dispuesto en los puntos 14.1.1. y 14.1.2., según correspon
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e4; e2 regula e1
- NODOS A CLASIFICAR:
  - **caso 1** Excepcion `e4`: Excepción régimen de cobro para VPU-RIGI | descripcion: Cuando el cliente sea un VPU adherido al RIGI que declaró hacer uso de los beneficios del artículo 198 de la Ley 27.742, resulta aplicable lo dispuesto en los puntos 14.1.1. y 14.1.2., según corresponda, en lugar de los plazos generales de ingreso y liquidación. | tramo: resultará aplicable lo dispuesto en los puntos 14.1.1. y 14.1.2., según corresponda.

## Unidad `ext::10.4.2.4` (item)
- herencia: **[abre la lista]** [intro 10.4.2] La entidad podrá dar acceso al mercado de cambios para el pago al exterior en la
medida que verifique previamente que se cumplen la totalidad de los siguientes
requisitos:
- texto propio: 10.4.2.4. Cuenta con la declaración jurada del cliente de que se compromete a
demostrar el registro del ingreso aduanero de los bienes dentro del plazo
que corresponda según tipo de bien a importar, o en su defecto, proceder
en ese plazo a la liquidación en el mercado de cambios de los fondos en
moneda extranjera asociados a la devolución del pago efectuado.
En el caso de pagos anticipados de bienes de capital, el plazo para
demostrar el registro de ingreso aduanero será de 270 (doscientos setenta)
días corridos a partir de la fecha de acceso al mercado de cambios. A tal
efecto, se deberán considerar las posiciones arancelarias clasificadas
como BK (Bien de Capital) en la Nomenclatura Común del MERCOSUR
(Decreto 690/02 y complementarias).
Para el resto de los bienes, el plazo será de 90 (noventa) días corridos a
partir de la fecha de acceso al mercado de cambios.
En el caso de que un mismo pago anticipado incluya bienes de capital y
bienes que no lo son, la operación se regirá por el plazo del tipo de bien
que represente una mayor proporción del valor total abonado.
Si la nacionalización de los bienes requiere un plazo mayor y el pago
anticipado se concreta en su totalidad en el marco de lo previsto en los
puntos 10.10.2.3. a 10.10.2.6. o 10.10.2.14.ii), la entidad podrá considerar
que el referido plazo se extiende hasta la fecha que surge de sumar 15
(quince) días corridos a la fecha estimada de arribo de los bienes. La
entidad deberá reportar la extensión otorgada en el SEPAIMPO.
Si el proveedor del exterior es una contraparte vinculada con el importador
o se necesiten plazos mayores para la oficialización del despacho de
importación, se requerirá contar con la previa conformidad del BCRA antes
del acceso al mercado de cambios.
Los pedidos al BCRA deben ser canalizado
- entidades de la unidad:
  - `e1` Operacion: Acceso al mercado de cambios para pago anticipado — Acceso al mercado de cambios para el pago al exterior de importaciones con registro de ingreso aduanero pendiente
  - `e2` Obligacion: Verificar requisitos previos — acceso al mercado de cambios — La entidad deberá verificar previamente que se cumplen la totalidad de los requisitos antes de dar acceso al mercado de cambios para el pago al exterior
  - `e3` Condicion: Declaración jurada del cliente sobre registro aduanero — El cliente debe contar con declaración jurada del cliente comprometiéndose a demostrar el registro del ingreso aduanero dentro del plazo correspondiente según tipo de bien, o proceder a la liquidación
  - `e4` Condicion: Plazo 270 días — bienes de capital — Para pagos anticipados de bienes de capital, el plazo para demostrar el registro de ingreso aduanero es de 270 días corridos a partir de la fecha de acceso al mercado de cambios
  - `e5` Definicion: Bienes de Capital (BK) — Posiciones arancelarias clasificadas como BK (Bien de Capital) en la Nomenclatura Común del MERCOSUR conforme al Decreto 690/02 y complementarias
  - `e6` Condicion: Plazo 90 días — resto de bienes — Para bienes que no son de capital, el plazo para demostrar el registro de ingreso aduanero es de 90 días corridos a partir de la fecha de acceso al mercado de cambios
  - `e7` Condicion: Plazo según proporción — bienes mixtos — Cuando un pago anticipado incluye tanto bienes de capital como otros bienes, se aplica el plazo del tipo de bien que represente mayor proporción del valor total abonado
  - `e8` Excepcion: Extensión de plazo — nacionalización con mayor duración — Cuando la nacionalización requiere plazo mayor y el pago se concreta conforme a los puntos 10.10.2.3 a 10.10.2.6 o 10.10.2.14.ii), la entidad puede extender el plazo hasta 15 días corridos después de 
  - `e9` Obligacion: Reportar extensión de plazo en SEPAIMPO — La entidad debe reportar la extensión de plazo otorgada en el SEPAIMPO
  - `e10` Restriccion: Conformidad previa del BCRA — contraparte vinculada o plazos mayores — Se requiere previa conformidad del BCRA antes del acceso al mercado de cambios cuando el proveedor del exterior es contraparte vinculada con el importador o se necesiten plazos mayores para la oficial
  - `e11` Obligacion: Canalizar pedidos al BCRA — entidad autorizada — Los pedidos al BCRA para conformidad previa deben ser canalizados por una entidad autorizada a realizar este tipo de pago
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e1; e4 condicion_de e1; e6 condicion_de e1; e7 condicion_de e1; e10 condicion_de e1; e1 requiere e2; e1 requiere e9; e1 requiere e11
- NODOS A CLASIFICAR:
  - **caso 2** Excepcion `e8`: Extensión de plazo — nacionalización con mayor duración | descripcion: Cuando la nacionalización requiere plazo mayor y el pago se concreta conforme a los puntos 10.10.2.3 a 10.10.2.6 o 10.10.2.14.ii), la entidad puede extender el plazo hasta 15 días corridos después de la fecha estimada de arribo de los bienes | tramo: Si la nacionalización de los bienes requiere un plazo mayor y el pago anticipado se concreta en su totalidad en el marco de lo previsto en los puntos 10.10.2.3. a 10.10.2.6. o 10.10.2.14.ii), la entidad podrá considerar que el referido plazo se extiende hasta la fecha que surge de sumar 15 (quince) días corridos a la fecha estimada de arribo de los bienes

## Unidad `ext::13.2.4` (item)
- herencia: **[abre la lista]** [intro 13.2] Las entidades podrán dar acceso al mercado de cambios para cursar pagos de servicios de
no residentes que fueron o serán prestados a partir del 13/12/23 cuando, adicionalmente a
los restantes requisitos normativos aplicables, la operación queda comprendida en algunas
de las situaciones que se detallan a continuación:
- texto propio: 13.2.4. el pago corresponde a una operación que encuadra en el concepto “S30. Servicios
de fletes por operaciones de importaciones de bienes” y se concreta a partir de la
fecha de prestación del servicio.
En caso de tratarse de fletes de una operación de importación encuadrada en lo
previsto en el punto 10.10.2.1., el pago podrá realizarse a partir del embarque de los
bienes en origen.
- entidades de la unidad:
  - `e1` Operacion: Pago de servicios de fletes por importación — Pago de servicios de fletes por operaciones de importación de bienes, que se concreta a partir de la fecha de prestación del servicio.
  - `e2` Condicion: Prestación del servicio — pago de fletes — El pago se concreta a partir de la fecha de prestación del servicio.
  - `e3` Excepcion: Excepción fletes importación punto 10.10.2.1 — pago desde embarque — Cuando los fletes corresponden a una operación de importación encuadrada en el punto 10.10.2.1, el pago puede realizarse a partir del embarque de los bienes en origen, en lugar de desde la fecha de pr
  - `e4` Obligacion: Acceso al mercado de cambios — pago servicios no residentes — Las entidades podrán dar acceso al mercado de cambios para cursar pagos de servicios de no residentes cuando la operación encuadra en el concepto S30 (servicios de fletes por importaciones de bienes) 
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 3** Excepcion `e3`: Excepción fletes importación punto 10.10.2.1 — pago desde embarque | descripcion: Cuando los fletes corresponden a una operación de importación encuadrada en el punto 10.10.2.1, el pago puede realizarse a partir del embarque de los bienes en origen, en lugar de desde la fecha de prestación del servicio. | tramo: En caso de tratarse de fletes de una operación de importación encuadrada en lo previsto en el punto 10.10.2.1., el pago podrá realizarse a partir del embarque de los bienes en origen.

## Unidad `cla::7.1` (punto_no_item)
- herencia: [encabezado S7] Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
- texto propio: 7.1. Criterio de clasificación.
Sin perjuicio de que los análisis previos al otorgamiento de las financiaciones y refinanciaciones
también deben guardar relación con la capacidad de pago de los deudores, evaluando la afec-
tación de sus ingresos periódicos por la totalidad de los compromisos de crédito asumidos, la
clasificación de estos clientes se efectuará considerando -al cabo de cada mes- exclusivamente
pautas objetivas vinculadas al grado de cumplimiento de las correspondientes obligaciones o su
situación jurídica, las informaciones que surjan de la “Central de deudores del sistema financie-
ro” –cuando reflejen niveles de calidad inferiores al asignado por la entidad–, de la base de
“Deudores en situación irregular de ex entidades financieras” y la situación que surja de la apli-
cación de las pautas de refinanciación. En caso de discrepancias, se deberá considerar la pau-
ta que indique el mayor nivel de riesgo de incobrabilidad.
Se entiende que el cumplimiento de las obligaciones a que se refieren las citadas pautas tiene
lugar cuando no se recurra a nuevas financiaciones o refinanciaciones destinadas a cancelar
obligaciones preexistentes, cualquiera sea la modalidad (prórrogas, esperas, ampliaciones de
plazo o márgenes -sean tales modalidades expresas o tácitas-, disminuciones en los importes
de las cuotas o pagos, renovaciones, reestructuraciones, etc.). En el caso de refinanciaciones,
a fin de determinar una mejora en la clasificación del deudor, corresponderá tener en cuenta las
pautas específicas previstas en cada una de las categorías.
A esos efectos, no se considerarán dentro de ese concepto las refinanciaciones otorgadas a
productores cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emer-
gencia Agropecuaria, sin perjuicio de
- entidades de la unidad:
  - `e1` Operacion: Clasificación de clientes de cartera consumo/vivienda — Clasificación de clientes de cartera para consumo o vivienda considerando pautas objetivas vinculadas al grado de cumplimiento de obligaciones o situación jurídica, evaluada al cabo de cada mes
  - `e2` Obligacion: Análisis previos al otorgamiento — capacidad de pago — Los análisis previos al otorgamiento de financiaciones y refinanciaciones deben guardar relación con la capacidad de pago de los deudores, evaluando la afectación de sus ingresos periódicos por la tot
  - `e3` Condicion: Información de Central de deudores — nivel inferior — Cuando las informaciones de la Central de deudores del sistema financiero reflejen niveles de calidad inferiores al asignado por la entidad
  - `e4` Condicion: Información de base de deudores en situación irregular — Información de la base de Deudores en situación irregular de ex entidades financieras
  - `e5` Condicion: Situación de aplicación de pautas de refinanciación — La situación que surja de la aplicación de las pautas de refinanciación
  - `e6` Restriccion: Discrepancias — aplicar pauta de mayor riesgo — En caso de discrepancias entre pautas de clasificación, debe considerarse la pauta que indique el mayor nivel de riesgo de incobrabilidad
  - `e7` Definicion: Cumplimiento de obligaciones — exclusión de nuevas financiaciones — El cumplimiento de obligaciones tiene lugar cuando no se recurra a nuevas financiaciones o refinanciaciones destinadas a cancelar obligaciones preexistentes, cualquiera sea la modalidad (prórrogas, es
  - `e8` Obligacion: Mejora de clasificación en refinanciaciones — pautas específicas — En refinanciaciones, para determinar mejora en la clasificación del deudor debe tenerse en cuenta las pautas específicas previstas en cada una de las categorías
  - `e9` Excepcion: Excepción refinanciaciones — productores Ley Emergencia Agropecuaria — No se consideran refinanciaciones las otorgadas a productores cuando resulten de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria
  - `e10` Restriccion: Productores Emergencia Agropecuaria — sin mejora por emergencia — El tratamiento en el marco de la Ley de Emergencia Agropecuaria no podrá implicar mejoramiento de clasificación en función de situación preexistente a la emergencia, ni extenderse más allá de la vigen
  - `e11` Obligacion: Mora en atraso — consideración al fin de emergencia — A los fines de la clasificación, debe tenerse en cuenta la mora en el atraso de obligaciones para el momento en que concluya la vigencia de la emergencia declarada
  - `e12` Obligacion: Mejora de clasificación en refinanciaciones — cuotas mínimas o porcentaje — Para determinar mejora en clasificación de deudor recategorizado por atraso en obligaciones refinanciadas, debe tenerse en cuenta cancelación de cuotas mínimas (pago periódico, mensual o bimestral) o 
  - `e13` Restriccion: Atraso mayor a 31 días — prohibición de mejora — No se podrán efectuar mejoras en clasificaciones de clientes que registren atraso mayor a 31 días en pago de obligaciones refinanciadas
  - `e14` Definicion: Cobros no aplicados y quitas — no computables para mejora — Los cobros no aplicados y quitas concedidas previamente a la refinanciación reducen el importe de la obligación sujeta a refinanciación y no son computables para mejora de clasificación según parámetr
  - `e15` Potestad: Imputación de cobros no aplicados y quitas — criterio de entidad — Cada entidad podrá optar por el criterio de imputación de cobros no aplicados y quitas a la cancelación de deuda objeto de refinanciación, sin perjuicio de otras disposiciones aplicables
  - `e16` Obligacion: Pagos anticipados — cómputo en cuotas o porcentaje — Pagos por adelantado y anticipos efectuados en oportunidad de refinanciación o posteriormente serán computados en término de cuotas o porcentaje de amortización de capital según modalidad de pago, en 
  - `e17` Definicion: Facilidades adicionales — no consideradas nuevas financiaciones — Facilidades adicionales sobre márgenes vigentes acordados que impliquen nuevos desembolsos y no superen el 10% del cupo de última evaluación crediticia, no se consideran nuevas financiaciones
  - `e18` Definicion: Renovaciones de crédito capital trabajo — no consideradas nuevas financiaciones — Renovaciones periódicas de crédito para capital de trabajo y nuevas financiaciones/refinanciaciones asociadas a mayor inversión por expansión de actividades no se consideran nuevas financiaciones
  - `e19` Condicion: Consistencia con curso normal de negocios — Facilidades y renovaciones deben ser consistentes con curso normal de negocios y debe existir capacidad para atender resto de obligaciones financieras
  - `e20` Condicion: Capacidad para atender obligaciones financieras — Debe existir capacidad para atender el resto de las obligaciones financieras
  - `e21` Excepcion: Excepción márgenes de crédito — no refinanciación si no se supera límite — Cuando márgenes de crédito por líneas específicas se excedan, no se consideran refinanciaciones si no se supera límite de asistencia máxima acordada por todo concepto según capacidad de pago
  - `e22` Excepcion: Excepción evaluación capacidad pago — métodos específicos o monto reducido — No es obligatoria evaluación de capacidad de pago por ingresos del prestatario cuando se utilicen métodos específicos de evaluación o se trate de deudores por préstamos de monto reducido
  - `e23` Potestad: Asistencia crediticia — no obsta evaluación de otras facilidades — El otorgamiento de asistencia crediticia de monto reducido no obsta a que para otras facilidades crediticias al mismo prestatario deba observarse evaluación de capacidad de pago
- relaciones del crudo (sin establecida_en ni de sujeto): e2 regula e1; e8 regula e1; e12 regula e1; e16 regula e1
- NODOS A CLASIFICAR:
  - **caso 4** Excepcion `e21`: Excepción márgenes de crédito — no refinanciación si no se supera límite | descripcion: Cuando márgenes de crédito por líneas específicas se excedan, no se consideran refinanciaciones si no se supera límite de asistencia máxima acordada por todo concepto según capacidad de pago | tramo: Cuando se hayan asignado al deudor márgenes de crédito por líneas de préstamo específicas y éstos se excedan, tales situaciones no serán consideradas refinanciaciones siempre que no se supere el límite de la asistencia máxima que le haya sido acordada por todo concepto en función de su capacidad de pago, según el acápite ii) del punto 1.1.3.2. de las normas sobre "Gestión crediticia"
  - **caso 80** Excepcion `e22`: Excepción evaluación capacidad pago — métodos específicos o monto reducido | descripcion: No es obligatoria evaluación de capacidad de pago por ingresos del prestatario cuando se utilicen métodos específicos de evaluación o se trate de deudores por préstamos de monto reducido | tramo: No será obligatoria la evaluación de la capacidad de pago en función de los ingresos del prestatario, en la medida en que se utilicen métodos específicos de evaluación o se trate de deudores por préstamos de monto reducido en los términos del punto 1.1.3.3. de las normas sobre "Gestión crediticia"
  - **caso 91** Excepcion `e9`: Excepción refinanciaciones — productores Ley Emergencia Agropecuaria | descripcion: No se consideran refinanciaciones las otorgadas a productores cuando resulten de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria | tramo: no se considerarán dentro de ese concepto las refinanciaciones otorgadas a productores cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria
  - **caso 149** Condicion `e20`: Capacidad para atender obligaciones financieras | descripcion: Debe existir capacidad para atender el resto de las obligaciones financieras | tramo: exista capacidad para atender el resto de las obligaciones financieras
  - **caso 159** Condicion `e19`: Consistencia con curso normal de negocios | descripcion: Facilidades y renovaciones deben ser consistentes con curso normal de negocios y debe existir capacidad para atender resto de obligaciones financieras | tramo: Ello, en la medida en que sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras
  - **caso 195** Condicion `e4`: Información de base de deudores en situación irregular | descripcion: Información de la base de Deudores en situación irregular de ex entidades financieras | tramo: de la base de "Deudores en situación irregular de ex entidades financieras"
  - **caso 196** Condicion `e3`: Información de Central de deudores — nivel inferior | descripcion: Cuando las informaciones de la Central de deudores del sistema financiero reflejen niveles de calidad inferiores al asignado por la entidad | tramo: las informaciones que surjan de la "Central de deudores del sistema financiero" –cuando reflejen niveles de calidad inferiores al asignado por la entidad–
  - **caso 245** Condicion `e5`: Situación de aplicación de pautas de refinanciación | descripcion: La situación que surja de la aplicación de las pautas de refinanciación | tramo: la situación que surja de la aplicación de las pautas de refinanciación

## Unidad `ctacte::3.3.7` (punto_no_item)
- herencia: [encabezado 3.3] 3.3. Reproducción de firmas digitalizadas para el libramiento de cheques en formato papel.
- texto propio: 3.3.7. Solicitudes.
Deberán efectuarse mediante nota dirigida a la Gerencia Principal de Seguridad de la In-
formación, suscripta por personal de nivel no inferior a subgerente general. En caso de
no existir dicha jerarquía, la pertinente presentación estará a cargo de la autoridad supe-
rior y del funcionario administrativo de mayor categoría, respectivamente.
- entidades de la unidad:
  - `e1` Obligacion: Solicitudes mediante nota a Gerencia Principal — Las solicitudes de reproducción de firmas digitalizadas para libramiento de cheques en formato papel deberán efectuarse mediante nota dirigida a la Gerencia Principal de Seguridad de la Información.
  - `e2` Restriccion: Suscripción por personal nivel no inferior a subgerente — La nota debe estar suscripta por personal de nivel no inferior a subgerente general.
  - `e3` Excepcion: Excepción cuando no existe jerarquía de subgerente — Cuando no existe la jerarquía de subgerente general, la presentación estará a cargo de la autoridad superior y del funcionario administrativo de mayor categoría.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 5** Excepcion `e3`: Excepción cuando no existe jerarquía de subgerente | descripcion: Cuando no existe la jerarquía de subgerente general, la presentación estará a cargo de la autoridad superior y del funcionario administrativo de mayor categoría. | tramo: En caso de no existir dicha jerarquía, la pertinente presentación estará a cargo de la autoridad superior y del funcionario administrativo de mayor categoría, respectivamente

## Unidad `ext::10.5.5.3` (punto_no_item)
- herencia: [intro 10.5] Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del
02/09/19 estará sujeto a un seguimiento desde la fecha de acceso al mercado de cambios
hasta la fecha en que se produzca su regularización.
Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se
demuestre ante la entidad encargada del seguimiento de ese pago, y por hasta el monto
girado, la existencia de: | [intro 10.5] i) el registro de ingreso aduanero a su nombre o a nombre de un tercero en la medida | [intro 10.5] que se cumplan las condiciones establecidas en la presente normativa; y/o | [intro 10.5] ii) la liquidación en el mercado de cambios de las divisas asociadas a la devolución del | [intro 10.5] pago efectuado; y/o | [intro 10.5] iii) otras formas de regularización previstas en la presente norma según las condiciones | [intro 10.5] y límites establecidos en cada caso; y/o | [intro 10.5] iv) la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la | [intro 10.5] operación. El pedido solo podrá ser tramitado por la entidad encargada del
seguimiento del pago y deberá estar debidamente justificado por ésta. | [intro 10.5.5] Las prórrogas del plazo para la demostración del registro de ingreso aduanero de
importación serán concedidas por la entidad a cargo del seguimiento del pago
realizado sin registro de ingreso aduanero, dentro de las condiciones que establece la
presente normativa o con la previa conformidad del BCRA.
Estas prórrogas deberán ser registradas por la entidad encargada del seguimiento del
pago en el sistema SEPAIMPO.
- texto propio: 10.5.5.3. Otras causales ajenas a la voluntad de decisión del importador.
En los casos de demoras en el registro de ingreso aduanero de la
oficialización de importación, por causales ajenas a la voluntad de decisión
del importador que afecten a la mayor parte del monto pendiente de
regularización de la operación, la entidad interviniente podrá otorgar una
extensión de los plazos establecidos precedentemente, que no podrá
superar los 545 (quinientos cuarenta y cinco) días corridos para los pagos
anticipados de bienes de capital o los 365 (trescientos sesenta y cinco)
días corridos para los restantes pagos, contándose los plazos indicados
desde la fecha de acceso al mercado de cambios.
Son ejemplos de causales ajenas a la voluntad de decisión del importador
las demoras motivadas en la producción y/o en el embarque por parte del
proveedor del exterior no derivadas en incumplimientos del importador, en
problemas de transporte, en la obtención de certificaciones necesarias para
la oficialización de la importación de los bienes o actuaciones
administrativas aduaneras que impliquen la imposibilidad de oficializar
hasta su resolución. En sentido contrario, la demora en efectuar la
oficialización por decisiones del importador motivadas en cuestiones
financieras o de mercado no está comprendida entre las causales
admitidas.
La documentación que avale la causal de la demora que respalda la
ampliación del plazo otorgada por la entidad, deberá quedar archivada en
la entidad a disposición del BCRA.
Agotados los plazos que puede otorgar la entidad a cargo del seguimiento,
esta última podrá solicitar la conformidad del BCRA para una ampliación
mayor en la medida que subsistan causales de demora ajenas al
importador.
- entidades de la unidad:
  - `e1` Condicion: Demoras por causales ajenas a voluntad importador — Demoras en el registro de ingreso aduanero por causales ajenas a la voluntad del importador que afecten a la mayor parte del monto pendiente de regularización
  - `e2` Potestad: Otorgar extensión de plazos — demoras ajenas a voluntad — La entidad interviniente puede otorgar una extensión de los plazos para demostración del registro de ingreso aduanero cuando concurren causales ajenas a la voluntad del importador
  - `e3` Restriccion: Tope 545 días — extensión bienes de capital — La extensión de plazos para pagos anticipados de bienes de capital no podrá superar 545 días corridos contados desde la fecha de acceso al mercado de cambios
  - `e4` Restriccion: Tope 365 días — extensión restantes pagos — La extensión de plazos para restantes pagos no podrá superar 365 días corridos contados desde la fecha de acceso al mercado de cambios
  - `e5` Definicion: Causales ajenas a voluntad del importador — Demoras motivadas en la producción y/o embarque por proveedor del exterior no derivadas en incumplimientos del importador, problemas de transporte, obtención de certificaciones necesarias para oficial
  - `e6` Excepcion: Excepción — demoras por decisiones financieras o de mercado — Demoras en la oficialización por decisiones del importador motivadas en cuestiones financieras o de mercado no califican como causales ajenas a la voluntad del importador
  - `e7` Obligacion: Archivar documentación que avale causal de demora — La entidad debe archivar la documentación que avale la causal de demora que respalda la ampliación del plazo, manteniéndola a disposición del BCRA
  - `e8` Potestad: Solicitar conformidad BCRA — ampliación mayor de plazo — La entidad a cargo del seguimiento puede solicitar conformidad del BCRA para una ampliación mayor de plazo cuando subsistan causales de demora ajenas al importador y se hayan agotado los plazos que la
- relaciones del crudo (sin establecida_en ni de sujeto): e1 condicion_de e2; e3 limita e2; e4 limita e2
- NODOS A CLASIFICAR:
  - **caso 6** Excepcion `e6`: Excepción — demoras por decisiones financieras o de mercado | descripcion: Demoras en la oficialización por decisiones del importador motivadas en cuestiones financieras o de mercado no califican como causales ajenas a la voluntad del importador | tramo: En sentido contrario, la demora en efectuar la oficialización por decisiones del importador motivadas en cuestiones financieras o de mercado no está comprendida entre las causales admitidas

## Unidad `ext::3.11.3::cierre` (cierre)
- herencia: [encabezado 3.11.3] 3.11.3. Las entidades podrán dar acceso al mercado de cambios a los residentes con
- texto propio: El acceso también podrá ser dado a los fideicomisos constituidos en el país para
garantizar la atención de los servicios de capital e intereses de tales endeudamientos.
- entidades de la unidad:
  - `e1` Operacion: Acceso al mercado de cambios — residentes — Las entidades podrán dar acceso al mercado de cambios a los residentes con aplicación específica para egresos por endeudamientos.
  - `e2` Excepcion: Extensión a fideicomisos — acceso mercado cambios — El acceso al mercado de cambios se extiende también a los fideicomisos constituidos en el país para garantizar la atención de los servicios de capital e intereses de tales endeudamientos.
  - `e3` Potestad: Facultad de dar acceso — entidades — Las entidades quedan facultadas para dar acceso al mercado de cambios a los residentes y a los fideicomisos constituidos en el país para garantizar servicios de capital e intereses de endeudamientos.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 7** Excepcion `e2`: Extensión a fideicomisos — acceso mercado cambios | descripcion: El acceso al mercado de cambios se extiende también a los fideicomisos constituidos en el país para garantizar la atención de los servicios de capital e intereses de tales endeudamientos. | tramo: El acceso también podrá ser dado a los fideicomisos constituidos en el país para garantizar la atención de los servicios de capital e intereses de tales endeudamientos

## Unidad `ext::3.11.3.1` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | **[abre la lista]** [intro 3.11.3] endeudamientos comprendidos en el punto 7.9. originados a partir del 07/01/21
(únicamente originados a partir del 08/08/25 en el caso de aquellos comprendidos en
el punto 7.9.1.4.) o prefinanciaciones de exportaciones comprendidas en el punto
7.8.5., para la compra de moneda extranjera para la constitución de las garantías en
cuentas en moneda extranjera abiertas en entidades financieras locales o en el
exterior –cuando se trate de un endeudamiento financiero comprendido en el punto
3.5. o las p | [cierre 3.11.3] El acceso también podrá ser dado a los fideicomisos constituidos en el país para
garantizar la atención de los servicios de capital e intereses de tales endeudamientos.
- texto propio: 3.11.3.1. las compras se realicen en forma simultánea con la liquidación de divisas
y/o a partir de fondos ingresados a nombre del exportador en una cuenta
de corresponsalía en el exterior de una entidad local; y
- entidades de la unidad:
  - `e1` Operacion: Acceso al mercado de cambios para compra de moneda extranjera — Acceso al mercado de cambios para compra de moneda extranjera destinada a constituir garantías en cuentas en moneda extranjera, para residentes con endeudamientos o prefinanciaciones de exportaciones 
  - `e2` Potestad: Facultad de dar acceso al mercado de cambios — Las entidades quedan facultadas a dar acceso al mercado de cambios a los residentes bajo las condiciones especificadas
  - `e3` Condicion: Compras simultáneas con liquidación de divisas — Las compras deben realizarse en forma simultánea con la liquidación de divisas
  - `e4` Condicion: Fondos desde cuenta de corresponsalía en el exterior — Las compras pueden realizarse a partir de fondos ingresados a nombre del exportador en una cuenta de corresponsalía en el exterior de una entidad local
  - `e5` Excepcion: Acceso para fideicomisos constituidos en el país — El acceso al mercado de cambios también se extiende a los fideicomisos constituidos en el país para garantizar la atención de servicios de capital e intereses de los endeudamientos
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e2; e4 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 8** Excepcion `e5`: Acceso para fideicomisos constituidos en el país | descripcion: El acceso al mercado de cambios también se extiende a los fideicomisos constituidos en el país para garantizar la atención de servicios de capital e intereses de los endeudamientos | tramo: El acceso también podrá ser dado a los fideicomisos constituidos en el país para garantizar la atención de los servicios de capital e intereses de tales endeudamientos

## Unidad `cla::6.5.2.1` (punto_no_item)
- herencia: [intro 6.5] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudor | [encabezado 6.5.2] 6.5.2. Con seguimiento especial.
- texto propio: 6.5.2.1. En observación.
El análisis del flujo de fondos del cliente demuestra que, al momento de realizar-
se, puede atender la totalidad de sus compromisos financieros.
Sin embargo, existen situaciones posibles que, de no ser controladas o corregi-
das oportunamente, podrían comprometer la capacidad futura de pago del clien-
te.
Entre los indicadores que pueden reflejar esta situación se destacan que el clien-
te:
i) Presente una buena situación financiera y de rentabilidad, con moderado en-
deudamiento y adecuado flujo de fondos para el pago de las deudas por capi-
tal e intereses. El flujo de fondos tiende a debilitarse para afrontar los pagos
dado que es sumamente sensible a la variación de una o dos variables, sobre
las cuales existe un significativo grado de incertidumbre, siendo especialmen-
te susceptible a cambios en circunstancias vinculadas al sector.
ii) Incurra en atrasos de hasta 90 días en los pagos de sus obligaciones. Se en-
tenderá que el cliente efectúa el pago de sus obligaciones cuando no recurre
a nueva financiación directa o indirecta de la entidad.
En el análisis que se lleve a cabo deberá tenerse en cuenta, de corresponder,
la eventual incidencia que en su capacidad de pago pueda tener la situación
en la que se encuentran los demás integrantes del grupo de contrapartes co-
nectadas al cual pertenece.
iii) Cuente con una dirección calificada y honesta.
iv) Tenga un adecuado sistema de información que permita conocer en forma re-
gular la situación financiera y económica del cliente. La información es consis-
tente. Cuando las financiaciones cuenten con garantías preferidas “B”, según-
las normas aplicables en esa materia, la entidad podrá requerir esa informa-
ción con la frecuencia que le permita efectuar la evaluación del deudor obser-
vando l
- entidades de la unidad:
  - `e1` Definicion: En observación — clasificación de deudor — Categoría de clasificación de deudor en la que el cliente puede atender la totalidad de sus compromisos financieros al momento del análisis, pero existen situaciones posibles que, de no ser controlada
  - `e2` Condicion: Buena situación financiera con flujo sensible — El cliente presenta buena situación financiera y rentabilidad con moderado endeudamiento y adecuado flujo de fondos, pero el flujo tiende a debilitarse por ser sumamente sensible a la variación de una
  - `e3` Condicion: Atrasos de hasta 90 días en pagos — El cliente incurre en atrasos de hasta 90 días en los pagos de sus obligaciones.
  - `e4` Condicion: Dirección calificada y honesta — El cliente cuenta con una dirección calificada y honesta.
  - `e5` Condicion: Sistema de información adecuado — El cliente tiene un adecuado sistema de información que permite conocer en forma regular su situación financiera y económica, y la información es consistente.
  - `e6` Condicion: Sector con tendencia cuestionable — El cliente pertenece a un sector de la actividad económica o ramo de negocios cuya tendencia futura presenta aspectos cuestionables, posibilidad de baja en los ingresos, aumento de la competencia o de
  - `e7` Condicion: Convenios de pago de concordatos con cancelación mínima — El cliente mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo acuerdos preventivos extrajudiciales homologados) a vencer o arreglos privados con
  - `e8` Condicion: Arreglos privados con opinión de auditor externo — El cliente mantiene arreglos privados con la entidad financiera que cuentan con la opinión del auditor externo sobre la factibilidad del cumplimiento de la refinanciación, cuando se haya cancelado al 
  - `e9` Condicion: Refinanciación con quitas de capital — El cliente ha refinanciado su deuda con otorgamiento de quitas de capital y, de acuerdo con la metodología del punto 2.2.7 de las normas sobre Previsiones mínimas por riesgo de incobrabilidad, corresp
  - `e10` Obligacion: Considerar incidencia de grupo de contrapartes conectadas — En el análisis debe tenerse en cuenta, de corresponder, la eventual incidencia que en la capacidad de pago del cliente pueda tener la situación de los demás integrantes del grupo de contrapartes conec
  - `e11` Obligacion: Requerir información con frecuencia según garantías preferidas — Cuando las financiaciones cuenten con garantías preferidas B, la entidad podrá requerir la información con la frecuencia que le permita efectuar la evaluación del deudor, observando la periodicidad mí
  - `e12` Excepcion: Reclasificación a situación normal por pago de intereses — El deudor puede reclasificarse al nivel superior (en situación normal) cuando se haya cumplido con el pago sin haber incurrido en atrasos superiores a 31 días de la totalidad de los intereses devengad
  - `e13` Excepcion: Reclasificación a situación normal por concordatos y arreglos — El deudor puede reclasificarse a situación normal cuando se observen las situaciones de los apartados vi) (convenios de pago de concordatos) y vii) (arreglos privados con opinión de auditor), si se ob
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1; e3 condicion_de e1; e4 condicion_de e1; e5 condicion_de e1; e6 condicion_de e1; e7 condicion_de e1; e8 condicion_de e1; e9 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 9** Excepcion `e13`: Reclasificación a situación normal por concordatos y arreglos | descripcion: El deudor puede reclasificarse a situación normal cuando se observen las situaciones de los apartados vi) (convenios de pago de concordatos) y vii) (arreglos privados con opinión de auditor), si se observan además las otras condiciones previstas para esa categoría. | tramo: Cuando se observen las situaciones a que se refieren los apartados vi) y vii), podrá reclasificarse al deudor en situación normal si se observan, además, las otras condiciones previstas para esa categoría.
  - **caso 10** Excepcion `e12`: Reclasificación a situación normal por pago de intereses | descripcion: El deudor puede reclasificarse al nivel superior (en situación normal) cuando se haya cumplido con el pago sin haber incurrido en atrasos superiores a 31 días de la totalidad de los intereses devengados, siempre que se observen las otras condiciones previstas. | tramo: Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a 31 días de la totalidad de los intereses devengados, podrá reclasificárselo en el nivel superior ("en situación normal") siempre que además se observen las otras condiciones previstas en la correspondiente categoría.

## Unidad `ctacte::5.1.6` (punto_no_item)
- herencia: [encabezado 5.1] 5.1. Endoso.
- texto propio: 5.1.6. El endoso que no contenga las especificaciones establecidas en el punto 5.1.4. no per-
judica al título ni a su transmisibilidad, no pudiendo ser rechazado por esa deficiencia.
- entidades de la unidad:
  - `e1` Operacion: Endoso sin especificaciones del punto 5.1.4 — Endoso que no contiene las especificaciones establecidas en el punto 5.1.4
  - `e2` Restriccion: Prohibición de rechazar endoso por deficiencia de especificaciones — No puede ser rechazado el endoso por la deficiencia de especificaciones del punto 5.1.4
  - `e3` Excepcion: Excepción — endoso deficiente no perjudica transmisibilidad — El endoso que no contiene las especificaciones del punto 5.1.4 no perjudica al título ni a su transmisibilidad
- relaciones del crudo (sin establecida_en ni de sujeto): e2 prohibe e1
- NODOS A CLASIFICAR:
  - **caso 11** Excepcion `e3`: Excepción — endoso deficiente no perjudica transmisibilidad | descripcion: El endoso que no contiene las especificaciones del punto 5.1.4 no perjudica al título ni a su transmisibilidad | tramo: no perjudica al título ni a su transmisibilidad

## Unidad `cap::3.2.1.1` (punto_no_item)
- herencia: [intro 3.2] Las participaciones en fondos (carteras de activos) imputadas a la cartera de inversión
–incluidas las exposiciones fuera de balance, tales como los compromisos de suscripciones fu-
turas– se deberán tratar de acuerdo con uno o más de los siguientes enfoques: de transparen-
cia (“look-through approach”, LTA), reglamentario (“mandate-based approach”, MBA) y residual
(“fall-back approach”, FBA). | [intro 3.2] Quedan comprendidas las participaciones en fondos comunes regidos por la Ley 24.083 de
Fondos Comunes de Inversión y en fideicomisos –en este último caso, en la medida en que el
riesgo de la inversión no se estructure a través de instrumentos que se emitan con distinta pre-
lación para el cobro, tales como títulos de deuda y certificados de participación–, imputados a
la cartera de inversión. | [encabezado 3.2.1] 3.2.1. Enfoques.
- texto propio: 3.2.1.1. Enfoque de transparencia (LTA).
Las exposiciones con el fondo deberán ponderarse como si fueran exposiciones
directas de la entidad financiera.
Este enfoque deberá utilizarse cuando se verifiquen las siguientes condiciones
en forma concurrente:
i) La entidad financiera reciba información suficiente y con adecuada fre-
cuencia acerca de las exposiciones subyacentes.
Esta condición se considerará satisfecha si el fondo provee información fi-
nanciera con una frecuencia mínima trimestral y el grado de detalle de la in-
formación es suficiente para el cálculo de los ponderadores de riesgo.
ii) La información a que se refiere el acápite i) haya sido verificada por un ter-
cero independiente.
Esta condición se considerará satisfecha si las exposiciones subyacentes
son verificadas por un tercero independiente –tal como la entidad deposita-
ria o custodio, el agente de control y revisión de fideicomisos o, cuando fue-
re aplicable, un auditor externo o la compañía gerente–.
En el caso de las exposiciones subyacentes a las operaciones con deriva-
dos realizadas por el fondo –toda vez que esos subyacentes den origen a
una ponderación por riesgo de crédito– y de las exposiciones al riesgo de
crédito de contraparte concomitantes, en lugar de calcular el ajuste de va-
luación del crédito (CVA) asociado a esas exposiciones por derivados de
acuerdo con el punto 4.2.2., se deberá multiplicar la exposición al riesgo de
crédito de contraparte por un factor de 1,5 antes de aplicar el ponderador
que corresponda a la contraparte. Cuando el CVA no sea aplicable tampo-
co lo será el factor de 1,5. Tal es el caso de: (i) las exposiciones con CCP y
(ii) las operaciones de financiación con títulos valores (“Securities Financing
Transactions”, SFT).
Las entidades financieras podrán basar
- entidades de la unidad:
  - `e1` Operacion: Ponderación de exposiciones con fondos — Las exposiciones con el fondo se ponderan como si fueran exposiciones directas de la entidad financiera.
  - `e2` Obligacion: Utilizar LTA cuando se verifican condiciones — El enfoque de transparencia (LTA) deberá utilizarse cuando se verifiquen las siguientes condiciones en forma concurrente.
  - `e3` Condicion: Información suficiente y frecuencia trimestral — La entidad financiera recibe información suficiente y con adecuada frecuencia acerca de las exposiciones subyacentes, satisfecha si el fondo provee información financiera con frecuencia mínima trimest
  - `e4` Condicion: Verificación por tercero independiente — La información sobre exposiciones subyacentes ha sido verificada por un tercero independiente: entidad depositaria o custodio, agente de control y revisión de fideicomisos, auditor externo o compañía 
  - `e5` Excepcion: Excepción CVA — exposiciones con derivados — Para exposiciones subyacentes a operaciones con derivados realizadas por el fondo que den origen a ponderación por riesgo de crédito, en lugar de calcular CVA según punto 4.2.2., se multiplica la expo
  - `e6` Excepcion: No aplicación del factor 1,5 — CCP y SFT — El factor de 1,5 no se aplica cuando CVA no es aplicable: en exposiciones con entidades de contraparte central (CCP) y en operaciones de financiación con títulos valores (Securities Financing Transact
  - `e7` Potestad: Basarse en cálculos de terceros para ponderadores — Las entidades financieras pueden basarse en cálculos de terceros para determinar los ponderadores de riesgo a aplicar a inversiones en fondos (ponderadores de subyacentes) si carecen de información ne
  - `e8` Restriccion: Ponderador 1,2 veces cuando se usan cálculos de terceros — Cuando se utilizan cálculos de terceros para determinar ponderadores, el ponderador a aplicar será 1,2 veces el ponderador que correspondería a una exposición directa.
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e2; e4 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 12** Excepcion `e6`: No aplicación del factor 1,5 — CCP y SFT | descripcion: El factor de 1,5 no se aplica cuando CVA no es aplicable: en exposiciones con entidades de contraparte central (CCP) y en operaciones de financiación con títulos valores (Securities Financing Transactions, SFT). | tramo: Cuando el CVA no sea aplicable tampoco lo será el factor de 1,5. Tal es el caso de: (i) las exposiciones con CCP y (ii) las operaciones de financiación con títulos valores ("Securities Financing Transactions", SFT).
  - **caso 101** Excepcion `e5`: Excepción CVA — exposiciones con derivados | descripcion: Para exposiciones subyacentes a operaciones con derivados realizadas por el fondo que den origen a ponderación por riesgo de crédito, en lugar de calcular CVA según punto 4.2.2., se multiplica la exposición al riesgo de crédito de contraparte por factor de 1,5 antes de aplicar el ponderador de la contraparte. | tramo: En el caso de las exposiciones subyacentes a las operaciones con derivados realizadas por el fondo –toda vez que esos subyacentes den origen a una ponderación por riesgo de crédito– y de las exposiciones al riesgo de crédito de contraparte concomitantes, en lugar de calcular el ajuste de valuación del crédito (CVA) asociado a esas exposiciones por derivados de acuerdo con el punto 4.2.2., se deberá multiplicar la exposición al riesgo de crédito de contraparte por un factor de 1,5 antes de aplicar el ponderador que corresponda a la contraparte.

## Unidad `cap::4.3.1.4` (punto_no_item)
- herencia: [intro 4.3] contraparte central.
Comprende a aquellas exposiciones de las entidades financieras con entidades de contrapar-
te central (CCP) que se originen en derivados OTC o negociados en mercados de valores y
en operaciones de financiación con títulos valores (“Securities Financing Transactions”, SFT)
y operaciones de liquidación diferida –definidas en el punto 4.2.–.
No están comprendidas las exposiciones originadas en operaciones al contado y que involu-
cren títulos valores, oro o moneda extranjera, c | [encabezado 4.3.1] 4.3.1. Definiciones.
- texto propio: 4.3.1.4. Margen inicial: es la garantía efectivamente constituida por un miembro
compensador o por un cliente para mitigar la exposición potencial futura de
la CCP respecto del miembro compensador debida a los posibles cambios
futuros en el valor de sus transacciones. A los efectos de la exigencia de
capital, el margen inicial no comprende los aportes a la CCP en concepto
de acuerdos para la absorción mancomunada –mutualización– de pérdi-
das. En el caso de que la CCP pueda usar el margen inicial para absorber
pérdidas en forma mancomunada entre los miembros compensadores, di-
cho margen se tratará como una exposición a un fondo de garantía para
incumplimientos. Además, incluye a los activos en garantía depositados
por un miembro compensador o cliente en exceso del monto mínimo re-
querido, siempre que la CCP o el miembro compensador pueda, de co-
rresponder, impedir que el miembro compensador o cliente, según el caso,
retire ese exceso.
- entidades de la unidad:
  - `e1` Definicion: Margen inicial — garantía de miembro compensador — Garantía efectivamente constituida por un miembro compensador o por un cliente para mitigar la exposición potencial futura de la CCP respecto del miembro compensador debida a los posibles cambios futu
  - `e2` Excepcion: Exclusión de aportes a CCP por mutualización de pérdidas — El margen inicial no comprende los aportes a la CCP en concepto de acuerdos para la absorción mancomunada de pérdidas, a los efectos de la exigencia de capital.
  - `e3` Operacion: Tratamiento de margen inicial como exposición a fondo de garantía — Cuando la CCP puede usar el margen inicial para absorber pérdidas en forma mancomunada entre los miembros compensadores, ese margen se trata como una exposición a un fondo de garantía para incumplimie
  - `e4` Definicion: Margen inicial — inclusión de activos en garantía en exceso — Incluye a los activos en garantía depositados por un miembro compensador o cliente en exceso del monto mínimo requerido, siempre que la CCP o el miembro compensador pueda, de corresponder, impedir que
  - `e5` Condicion: Condición — CCP puede usar margen inicial para absorber pérdidas — La CCP puede usar el margen inicial para absorber pérdidas en forma mancomunada entre los miembros compensadores.
  - `e6` Condicion: Condición — CCP o miembro puede impedir retiro de exceso — La CCP o el miembro compensador puede impedir que el miembro compensador o cliente retire el exceso de activos en garantía.
- relaciones del crudo (sin establecida_en ni de sujeto): e5 condicion_de e3; e6 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 13** Excepcion `e2`: Exclusión de aportes a CCP por mutualización de pérdidas | descripcion: El margen inicial no comprende los aportes a la CCP en concepto de acuerdos para la absorción mancomunada de pérdidas, a los efectos de la exigencia de capital. | tramo: A los efectos de la exigencia de capital, el margen inicial no comprende los aportes a la CCP en concepto de acuerdos para la absorción mancomunada –mutualización– de pérdidas

## Unidad `ctacte::1.5.2.11` (punto_no_item)
- herencia: [intro 1.5] En sus cláusulas se deberá prever, como mínimo: | [encabezado 1.5.2] 1.5.2. Obligaciones de la entidad.
- texto propio: 1.5.2.11. Informar al BCRA los rechazos de cheques por defectos formales, los rechazos
a la registración de los de pago diferido, así como los producidos por insuficien-
te provisión de fondos en cuenta o por no contar con autorización para girar en
descubierto y las multas satisfechas por los responsables.
Para los casos en que las multas hubieren sido abonadas y se efectúe una noti-
ficación errónea al BCRA, que determine la inhabilitación automática del cliente,
se deberá prever en los contratos que la entidad compensará al cliente los gas-
tos que le origine la solución de tal situación mediante su crédito en la cuenta
del cliente, estimándose que ello no debe ser inferior a una vez el importe de las
multas de que se trate. Dicho pago no exime a la entidad de las responsabilida-
des civiles que pudieren corresponder en su relación con el cliente.
- entidades de la unidad:
  - `e1` Obligacion: Informar al BCRA rechazos de cheques — Informar al BCRA los rechazos de cheques por defectos formales, los rechazos a la registración de los de pago diferido, los producidos por insuficiente provisión de fondos en cuenta o por no contar co
  - `e2` Obligacion: Compensar al cliente gastos por notificación errónea — Prever en los contratos que la entidad compensará al cliente los gastos que le origine la solución de la situación derivada de una notificación errónea al BCRA que determine la inhabilitación automáti
  - `e3` Restriccion: Monto mínimo compensación — notificación errónea — El monto de la compensación al cliente no debe ser inferior a una vez el importe de las multas de que se trate.
  - `e4` Condicion: Notificación errónea al BCRA con inhabilitación automática — Las multas hubieren sido abonadas y se efectúe una notificación errónea al BCRA que determine la inhabilitación automática del cliente.
  - `e5` Excepcion: Excepción responsabilidades civiles — compensación — El pago de la compensación no exime a la entidad de las responsabilidades civiles que pudieren corresponder en su relación con el cliente.
- relaciones del crudo (sin establecida_en ni de sujeto): e4 condicion_de e2; e3 limita e2
- NODOS A CLASIFICAR:
  - **caso 14** Excepcion `e5`: Excepción responsabilidades civiles — compensación | descripcion: El pago de la compensación no exime a la entidad de las responsabilidades civiles que pudieren corresponder en su relación con el cliente. | tramo: Dicho pago no exime a la entidad de las responsabilidades civiles que pudieren corresponder en su relación con el cliente.

## Unidad `ext::7.10.4` (punto_no_item)
- herencia: [intro 7.10] del régimen de fomento de inversión para las exportaciones (Decreto 234/21).
- texto propio: 7.10.4. Los casos previstos en el punto 1) del artículo 8° bis incorporado por el Decreto
836/21 al Decreto 234/21, podrán aplicar durante 2 (dos) años calendario
consecutivos por cada año calendario en que no se hiciera uso del beneficio, hasta el
40% (cuarenta por ciento) del valor de los permisos embarcados durante los años en
que se haga uso del beneficio ampliado, en la medida que el monto anual aplicado no
supere el equivalente al 40% (cuarenta por ciento) del monto bruto de las divisas
ingresadas para financiar el desarrollo del proyecto que genera las exportaciones
aplicadas.
Se podrá acceder a la opción indicada en el párrafo precedente una vez transcurrido
el segundo año calendario desde el primer ingreso de divisas que dan inicio al
proyecto. Dicho plazo podrá computarse como parte del período de no utilización que
da lugar al uso del beneficio ampliado.
Adicionalmente a lo previsto en el primer párrafo del punto 7.10.3. los fondos también
podrán permanecer en cuentas bancarias de entidades financieras del exterior que
no estén constituidas en países o territorios donde no se aplican o no se aplican
suficientemente las recomendaciones del Grupo de Acción de Financiera
Internacional.
- entidades de la unidad:
  - `e1` Operacion: Aplicación ampliada de cobros de exportaciones — Aplicación ampliada del beneficio de cobros de exportaciones de bienes durante 2 años calendario consecutivos por cada año calendario en que no se hizo uso del beneficio, en el marco del régimen de fo
  - `e2` Restriccion: Límite 40% valor permisos embarcados — El monto del beneficio ampliado no podrá superar el 40% del valor de los permisos embarcados durante los años en que se haga uso del beneficio ampliado.
  - `e3` Restriccion: Límite 40% monto bruto divisas ingresadas — El monto anual aplicado no podrá superar el equivalente al 40% del monto bruto de las divisas ingresadas para financiar el desarrollo del proyecto que genera las exportaciones aplicadas.
  - `e4` Condicion: Transcurso de segundo año desde primer ingreso — La opción de aplicación ampliada del beneficio solo puede ejercerse una vez transcurrido el segundo año calendario desde el primer ingreso de divisas que dan inicio al proyecto.
  - `e5` Excepcion: Cómputo del plazo como período de no utilización — El plazo de dos años desde el primer ingreso de divisas puede computarse como parte del período de no utilización que da lugar al uso del beneficio ampliado.
  - `e6` Potestad: Permanencia de fondos en cuentas del exterior — Los fondos pueden permanecer en cuentas bancarias de entidades financieras del exterior que no estén constituidas en países o territorios donde no se aplican o no se aplican suficientemente las recome
- relaciones del crudo (sin establecida_en ni de sujeto): e2 limita e1; e3 limita e1; e4 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 15** Excepcion `e5`: Cómputo del plazo como período de no utilización | descripcion: El plazo de dos años desde el primer ingreso de divisas puede computarse como parte del período de no utilización que da lugar al uso del beneficio ampliado. | tramo: Dicho plazo podrá computarse como parte del período de no utilización que da lugar al uso del beneficio ampliado

## Unidad `ctacte::6.4.6.1` (item)
- herencia: **[abre la lista]** [encabezado 6.4.6] 6.4.6. No corresponderá la comunicación al BCRA de los rechazos motivados por:
- texto propio: 6.4.6.1. La falsificación o adulteración de cheques.
Será requisito indispensable que el cuentacorrentista cumpla la exigencia a que
se refiere el punto 7.3.3.2. i). En el supuesto de adulteración, el rechazo del
cheque no se comunicará cuando existan fondos suficientes para pagarlo de no
haberse producido el hecho doloso.
- entidades de la unidad:
  - `e1` Excepcion: Excepción rechazo adulteración — comunicación al BCRA — El rechazo del cheque por adulteración no se comunica al BCRA cuando existen fondos suficientes para pagarlo de no haberse producido el hecho doloso.
  - `c1` Condicion: Fondos suficientes para pago sin adulteración — Que existan fondos suficientes en la cuenta para pagar el cheque si no se hubiera producido la adulteración.
  - `o1` Obligacion: Cumplimiento exigencia punto 7.3.3.2.i — falsificación/adulteración — El cuentacorrentista debe cumplir la exigencia a que se refiere el punto 7.3.3.2.i) como requisito indispensable para la no comunicación del rechazo por falsificación o adulteración de cheques.
  - `e2` Excepcion: Excepción rechazo falsificación — comunicación al BCRA — No corresponde comunicar al BCRA los rechazos motivados por falsificación o adulteración de cheques.
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 16** Excepcion `e1`: Excepción rechazo adulteración — comunicación al BCRA | descripcion: El rechazo del cheque por adulteración no se comunica al BCRA cuando existen fondos suficientes para pagarlo de no haberse producido el hecho doloso. | tramo: En el supuesto de adulteración, el rechazo del cheque no se comunicará cuando existan fondos suficientes para pagarlo de no haberse producido el hecho doloso.
  - **caso 78** Excepcion `e2`: Excepción rechazo falsificación — comunicación al BCRA | descripcion: No corresponde comunicar al BCRA los rechazos motivados por falsificación o adulteración de cheques. | tramo: La falsificación o adulteración de cheques.

## Unidad `ext::8.5.17.7` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.7. Régimen de equipaje (artículos 488 al 505 de la Ley 22.415).
- entidades de la unidad:
  - `e1` Operacion: Régimen de equipaje — operación aduanera — Operación aduanera correspondiente al régimen de equipaje regulado en los artículos 488 al 505 de la Ley 22.415, exceptuada del seguimiento de negociaciones de divisas por exportaciones de bienes.
  - `e2` Excepcion: Excepción régimen de equipaje — seguimiento — El régimen de equipaje queda exceptuado del seguimiento de negociaciones de divisas por exportaciones de bienes.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 17** Excepcion `e2`: Excepción régimen de equipaje — seguimiento | descripcion: El régimen de equipaje queda exceptuado del seguimiento de negociaciones de divisas por exportaciones de bienes. | tramo: Régimen de equipaje (artículos 488 al 505 de la Ley 22.415)

## Unidad `ext::8.5.17.8` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.8. Régimen de exportación para compensar envíos con deficiencias
(artículos 573 al 577 de la Ley 22.415).
- entidades de la unidad:
  - `e1` Operacion: Régimen de exportación para compensar envíos con deficiencias — Régimen de exportación para compensar envíos con deficiencias, regulado por los artículos 573 al 577 de la Ley 22.415
  - `e2` Excepcion: Excepción seguimiento — régimen de exportación para compensar envíos — El régimen de exportación para compensar envíos con deficiencias queda exceptuado del seguimiento de permisos de embarque
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 18** Excepcion `e2`: Excepción seguimiento — régimen de exportación para compensar envíos | descripcion: El régimen de exportación para compensar envíos con deficiencias queda exceptuado del seguimiento de permisos de embarque | tramo: Régimen de exportación para compensar envíos con deficiencias

## Unidad `ext::8.5.17.3` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.3. Régimen de pacotilla (artículos 517 al 528 de la Ley 22.415).
- entidades de la unidad:
  - `e1` Operacion: Régimen de pacotilla — Operación aduanera exceptuada del seguimiento de divisas por exportaciones, regulada por los artículos 517 al 528 de la Ley 22.415
  - `e2` Excepcion: Excepción pacotilla — seguimiento de divisas — El régimen de pacotilla queda exceptuado del seguimiento de divisas por exportaciones de bienes
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 19** Excepcion `e2`: Excepción pacotilla — seguimiento de divisas | descripcion: El régimen de pacotilla queda exceptuado del seguimiento de divisas por exportaciones de bienes | tramo: Régimen de pacotilla (artículos 517 al 528 de la Ley 22.415)

## Unidad `ext::8.5.17.13` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.13. Régimen de removido (artículos 386 al 396 de la Ley 22.415).
- entidades de la unidad:
  - `e1` Operacion: Régimen de removido — operación aduanera — Operación aduanera exceptuada del seguimiento de negociaciones de divisas por exportaciones de bienes, regulada por los artículos 386 al 396 de la Ley 22.415 (Régimen de removido).
  - `e2` Excepcion: Excepción removido — seguimiento de divisas — El régimen de removido queda exceptuado del seguimiento de negociaciones de divisas por exportaciones de bienes.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 20** Excepcion `e2`: Excepción removido — seguimiento de divisas | descripcion: El régimen de removido queda exceptuado del seguimiento de negociaciones de divisas por exportaciones de bienes. | tramo: Régimen de removido (artículos 386 al 396 de la Ley 22.415)

## Unidad `ext::14.4::cierre` (cierre)
- herencia: [encabezado 14.4] 14.4. Requisito complementario para egresos para un VPU que prevé hacer uso de los beneficios
- texto propio: Este requisito complementario no resultará aplicable cuando el acceso al mercado de
cambios del VPU sea con el objeto de realizar alguna de las siguientes operaciones:
i) pagos de intereses admitidos por las financiaciones contempladas en los puntos
14.2.1.1. al 14.2.1.11.
ii) pagos de utilidades y dividendos a accionistas no residentes admitidos en el punto
14.2.2.
iii) pagos de capital de las financiaciones locales contempladas en los puntos 14.2.1.3.
al 14.2.1.5.
- entidades de la unidad:
  - `e1` Excepcion: Excepción acceso mercado cambios VPU — El requisito complementario para egresos no aplica cuando el VPU accede al mercado de cambios para realizar operaciones de pago de intereses, utilidades, dividendos o capital de financiaciones especif
  - `e2` Operacion: Pago de intereses — financiaciones RIGI — Pago de intereses admitidos por las financiaciones contempladas en los puntos 14.2.1.1. al 14.2.1.11.
  - `e3` Operacion: Pago de utilidades y dividendos — accionistas no residentes — Pago de utilidades y dividendos a accionistas no residentes admitidos en el punto 14.2.2.
  - `e4` Operacion: Pago de capital — financiaciones locales RIGI — Pago de capital de las financiaciones locales contempladas en los puntos 14.2.1.3. al 14.2.1.5.
  - `e5` Condicion: Supuesto — pago de intereses admitidos — Cuando el acceso al mercado de cambios sea para realizar pagos de intereses admitidos por las financiaciones especificadas
  - `e6` Condicion: Supuesto — pago de utilidades y dividendos — Cuando el acceso al mercado de cambios sea para realizar pagos de utilidades y dividendos a accionistas no residentes admitidos
  - `e7` Condicion: Supuesto — pago de capital financiaciones locales — Cuando el acceso al mercado de cambios sea para realizar pagos de capital de las financiaciones locales especificadas
- relaciones del crudo (sin establecida_en ni de sujeto): e5 condicion_de e1; e6 condicion_de e1; e7 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 21** Excepcion `e1`: Excepción acceso mercado cambios VPU | descripcion: El requisito complementario para egresos no aplica cuando el VPU accede al mercado de cambios para realizar operaciones de pago de intereses, utilidades, dividendos o capital de financiaciones especificadas | tramo: Este requisito complementario no resultará aplicable cuando el acceso al mercado de cambios del VPU sea con el objeto de realizar alguna de las siguientes operaciones

## Unidad `ext::10.4.2.6` (item)
- herencia: **[abre la lista]** [intro 10.4.2] La entidad podrá dar acceso al mercado de cambios para el pago al exterior en la
medida que verifique previamente que se cumplen la totalidad de los siguientes
requisitos:
- texto propio: 10.4.2.6. El cliente no registra situaciones de demora en la regularización de pagos
con registro de ingreso aduanero pendiente realizados a partir del 02/09/19.
Los pagos de importaciones de bienes con registro de ingreso aduanero
pendiente concretados entre el 02/09/19 y el 31/10/19, por operaciones
comprendidas en los puntos 10.4.1.2. a 10.4.1.4., que no se encuentren
regularizados según lo previsto en el punto 10.5. son considerados en
situación de demora a partir del 02/11/20.
Las entidades deberán consultar en el apartado “Régimen Informativo
SEPAIMPO” del sitio www3.bcra.gob.ar, si el cliente registra en el sistema
demoras en el conjunto de las entidades.
Este requisito no será de aplicación para:
i) el sector público;
ii) todas las organizaciones empresariales, cualquiera sea su forma
societaria, en donde el Estado Nacional tenga participación mayoritaria
en el capital o en la formación de las decisiones societarias;
iii)los fideicomisos constituidos con aportes del sector público nacional; y
iv)las personas jurídicas que tengan a su cargo la provisión de
medicamentos críticos a pacientes cuando realicen pagos anticipados
por ese tipo de bienes a ingresar por Solicitud Particular por el
beneficiario de dicha cobertura médica.
- entidades de la unidad:
  - `e1` Condicion: Cliente sin demoras en regularización de pagos — El cliente no registra situaciones de demora en la regularización de pagos con registro de ingreso aduanero pendiente realizados a partir del 02/09/19. Se consideran en situación de demora los pagos d
  - `e2` Obligacion: Consultar demoras en Régimen Informativo SEPAIMPO — Las entidades deberán consultar en el apartado Régimen Informativo SEPAIMPO del sitio www3.bcra.gob.ar si el cliente registra en el sistema demoras en el conjunto de las entidades
  - `e3` Excepcion: Excepción sector público — El requisito de que el cliente no registre situaciones de demora no será de aplicación para el sector público
  - `e4` Excepcion: Excepción organizaciones con participación estatal mayoritaria — El requisito de que el cliente no registre situaciones de demora no será de aplicación para todas las organizaciones empresariales, cualquiera sea su forma societaria, en donde el Estado Nacional teng
  - `e5` Excepcion: Excepción fideicomisos con aportes del sector público — El requisito de que el cliente no registre situaciones de demora no será de aplicación para los fideicomisos constituidos con aportes del sector público nacional
  - `e6` Excepcion: Excepción personas jurídicas proveedoras de medicamentos críticos — El requisito de que el cliente no registre situaciones de demora no será de aplicación para las personas jurídicas que tengan a su cargo la provisión de medicamentos críticos a pacientes cuando realic
  - `e7` Operacion: Pago anticipado de importación con registro aduanero pendiente — Pagos de importaciones de bienes con registro de ingreso aduanero pendiente realizados a partir del 02/09/19
- relaciones del crudo (sin establecida_en ni de sujeto): e1 condicion_de e7
- NODOS A CLASIFICAR:
  - **caso 22** Excepcion `e5`: Excepción fideicomisos con aportes del sector público | descripcion: El requisito de que el cliente no registre situaciones de demora no será de aplicación para los fideicomisos constituidos con aportes del sector público nacional | tramo: los fideicomisos constituidos con aportes del sector público nacional
  - **caso 23** Excepcion `e6`: Excepción personas jurídicas proveedoras de medicamentos críticos | descripcion: El requisito de que el cliente no registre situaciones de demora no será de aplicación para las personas jurídicas que tengan a su cargo la provisión de medicamentos críticos a pacientes cuando realicen pagos anticipados por ese tipo de bienes a ingresar por Solicitud Particular por el beneficiario de dicha cobertura médica | tramo: las personas jurídicas que tengan a su cargo la provisión de medicamentos críticos a pacientes cuando realicen pagos anticipados por ese tipo de bienes a ingresar por Solicitud Particular por el beneficiario de dicha cobertura médica
  - **caso 24** Excepcion `e3`: Excepción sector público | descripcion: El requisito de que el cliente no registre situaciones de demora no será de aplicación para el sector público | tramo: el sector público
  - **caso 25** Excepcion `e4`: Excepción organizaciones con participación estatal mayoritaria | descripcion: El requisito de que el cliente no registre situaciones de demora no será de aplicación para todas las organizaciones empresariales, cualquiera sea su forma societaria, en donde el Estado Nacional tenga participación mayoritaria en el capital o en la formación de las decisiones societarias | tramo: todas las organizaciones empresariales, cualquiera sea su forma societaria, en donde el Estado Nacional tenga participación mayoritaria en el capital o en la formación de las decisiones societarias

## Unidad `cap::2.5.6` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca | [encabezado 2.5] 2.5. Criterios para la determinación de los activos ponderados por riesgo.
- texto propio: 2.5.6. El tratamiento otorgado a la exposición al sector público no financiero no será de aplica-
ción en las operaciones con contrapartes a las cuales el BCRA les haya otorgado el tra-
tamiento previsto para las personas del sector privado no financiero. En estos casos, co-
rresponderá considerarlas como exposiciones a empresas del sector privado no finan-
ciero.
- entidades de la unidad:
  - `e1` Operacion: Operaciones con contrapartes tratadas como sector privado — Operaciones con contrapartes que el BCRA ha tratado como personas del sector privado no financiero, que deben considerarse como exposiciones a empresas del sector privado no financiero.
  - `e2` Excepcion: Excepción tratamiento sector público no financiero — El tratamiento de exposición al sector público no financiero no aplica cuando el BCRA ha otorgado a la contraparte el tratamiento de persona del sector privado no financiero.
  - `e3` Condicion: Condición: BCRA otorgó tratamiento sector privado — Supuesto en que el BCRA ha otorgado a la contraparte el tratamiento de persona del sector privado no financiero.
  - `e4` Obligacion: Consideración como exposición sector privado — Las entidades financieras deben considerar las operaciones con contrapartes tratadas como sector privado no financiero como exposiciones a empresas del sector privado no financiero.
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e2; e3 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 26** Excepcion `e2`: Excepción tratamiento sector público no financiero | descripcion: El tratamiento de exposición al sector público no financiero no aplica cuando el BCRA ha otorgado a la contraparte el tratamiento de persona del sector privado no financiero. | tramo: El tratamiento otorgado a la exposición al sector público no financiero no será de aplicación en las operaciones con contrapartes a las cuales el BCRA les haya otorgado el tratamiento previsto para las personas del sector privado no financiero

## Unidad `cap::4.2.1::intro` (intro)
- herencia: [encabezado 4.2.1] 4.2.1. Exposición al riesgo de crédito de contraparte.
- texto propio: La exposición al riesgo de crédito de contraparte (EAD) se calculará por separado para
cada conjunto de neteo (“netting set”, NS) y se determinará del siguiente modo:
donde:
α = 1,40.
CR: costo de reposición calculado de acuerdo con el punto 4.2.1.1.
EPF: exposición potencial futura calculado de acuerdo con el punto 4.2.1.2.
El cálculo del CR y de la EPF diferirá según que los conjuntos de neteo estén sujetos o
no al intercambio de márgenes de variación:
− Operaciones sin margen de variación: el CR representa la pérdida que ocurriría
ante el incumplimiento de la contraparte y la liquidación inmediata de sus opera-
ciones y la EPF adicionará el incremento probable de la exposición, calculado de
modo conservador, en el horizonte temporal de un año a partir de la fecha de
cálculo.
− Operaciones con margen de variación: el CR representa la pérdida que ocurriría
ante el incumplimiento de la contraparte –en el presente o en el futuro– si la liqui-
dación y reposición de las operaciones fueran instantáneas. Dado que puede ha-
ber un lapso –período de riesgo de margen (“MPOR”)– entre el último intercambio
de garantías antes del incumplimiento y la reposición, el adicional por la EPF re-
presenta el potencial cambio de valor de las operaciones durante ese período.
En ambos casos, y a los efectos de determinar el costo de reposición, el aforo de los
activos recibidos en garantía (excepto efectivo) representará el cambio potencial del
valor de dicha garantía durante el período relevante –un año, para las operaciones sin
márgenes, y el período de riesgo de margen, para las operaciones con márgenes–.
Además:
− La EAD para un conjunto de neteo con márgenes de variación tendrá como límite
superior la EAD que resultaría para el mismo conjunto si no los tuviera.
− La EAD de un conjunto 
- entidades de la unidad:
  - `e1` Operacion: Cálculo de EAD por conjunto de neteo — Cálculo de la exposición al riesgo de crédito de contraparte (EAD) por separado para cada conjunto de neteo, determinada mediante fórmula que incorpora costo de reposición (CR) y exposición potencial 
  - `e2` Definicion: CR — Costo de reposición — Costo de reposición, calculado de acuerdo con el punto 4.2.1.1.
  - `e3` Definicion: EPF — Exposición potencial futura — Exposición potencial futura, calculada de acuerdo con el punto 4.2.1.2.
  - `e4` Condicion: Operaciones sin margen de variación — Supuesto en que los conjuntos de neteo no están sujetos al intercambio de márgenes de variación: CR representa la pérdida ante incumplimiento y liquidación inmediata; EPF adiciona el incremento probab
  - `e5` Condicion: Operaciones con margen de variación — Supuesto en que los conjuntos de neteo están sujetos al intercambio de márgenes de variación: CR representa la pérdida ante incumplimiento si liquidación y reposición fueran instantáneas; EPF represen
  - `e6` Obligacion: Aforo de activos recibidos en garantía — A los efectos de determinar el costo de reposición, el aforo de los activos recibidos en garantía (excepto efectivo) deberá representar el cambio potencial del valor de dicha garantía durante el perío
  - `e7` Restriccion: Límite superior EAD con márgenes de variación — La EAD para un conjunto de neteo con márgenes de variación no podrá exceder la EAD que resultaría para el mismo conjunto sin márgenes de variación.
  - `e8` Excepcion: EAD cero para opciones vendidas — Excepción a la exigencia de EAD positiva: la EAD de un conjunto de neteo que comprende solo opciones vendidas puede ser cero cuando se hayan cobrado todas las primas y las opciones no estén incluidas 
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 27** Excepcion `e8`: EAD cero para opciones vendidas | descripcion: Excepción a la exigencia de EAD positiva: la EAD de un conjunto de neteo que comprende solo opciones vendidas puede ser cero cuando se hayan cobrado todas las primas y las opciones no estén incluidas en acuerdos de neteo con otros productos ni en constitución de márgenes. | tramo: La EAD de un conjunto de neteo que sólo comprende opciones vendidas podrá ser cero cuando hayan sido cobradas todas las primas y en tanto dichas opciones no estén comprendidas en acuerdos de neteo que incluyan otros productos o la constitución de márgenes.
  - **caso 209** Condicion `e5`: Operaciones con margen de variación | descripcion: Supuesto en que los conjuntos de neteo están sujetos al intercambio de márgenes de variación: CR representa la pérdida ante incumplimiento si liquidación y reposición fueran instantáneas; EPF representa el cambio potencial de valor durante el período de riesgo de margen (MPOR). | tramo: Operaciones con margen de variación: el CR representa la pérdida que ocurriría ante el incumplimiento de la contraparte –en el presente o en el futuro– si la liquidación y reposición de las operaciones fueran instantáneas. Dado que puede haber un lapso –período de riesgo de margen ("MPOR")– entre el último intercambio de garantías antes del incumplimiento y la reposición, el adicional por la EPF representa el potencial cambio de valor de las operaciones durante ese período.
  - **caso 210** Condicion `e4`: Operaciones sin margen de variación | descripcion: Supuesto en que los conjuntos de neteo no están sujetos al intercambio de márgenes de variación: CR representa la pérdida ante incumplimiento y liquidación inmediata; EPF adiciona el incremento probable de exposición en horizonte de un año. | tramo: Operaciones sin margen de variación: el CR representa la pérdida que ocurriría ante el incumplimiento de la contraparte y la liquidación inmediata de sus operaciones y la EPF adicionará el incremento probable de la exposición, calculado de modo conservador, en el horizonte temporal de un año a partir de la fecha de cálculo.

## Unidad `cap::3.1.11.2` (punto_no_item)
- herencia: [intro 3.1] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi-
cional o sintética, o a una estructura con similares características.
La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con-
ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de
deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset-
Backed Securities”, ABS) y bonos de tit | [intro 3.1.11] Los ponderadores de riesgo a aplicar a las posiciones de una titulización y a las exposi-
ciones subyacentes de una retitulización para la determinación de la exigencia de capi-
tal se establecerán empleando las disposiciones de este punto.
Las posiciones de titulización a las que no se les pueda aplicar el enfoque estandariza-
do deberán ser ponderadas al 1250 %.
- texto propio: 3.1.11.2. Cálculo de las variables.
i) K .
SA
Es la exigencia de capital promedio de las exposiciones subyacentes; es
decir, el ratio entre la suma de las exposiciones subyacentes ponderadas
por riesgo y la suma de las exposiciones subyacentes, todo multiplicado
por 8 %. El cálculo deberá reflejar los efectos de cualquier cobertura del
riesgo de crédito que corresponda aplicar a las exposiciones subyacentes
(individualmente o al conjunto). K es un porcentaje entre cero y cien; es
SA
decir, si el ponderador de riesgo medio ponderado fuera 100 %, K será
SA
igual a 8 %.
Cuando la estructura involucre a un SPE, se considerará que todas las ex-
posiciones del SPE vinculadas a la titulización integran el conjunto de acti-
vos subyacentes. Esto incluye a los activos en los que ha invertido el SPE,
las reservas (“reserve accounts”), las cuentas de efectivo en garantía y los
derechos frente a las contrapartes por “swaps” de tasa de interés o de mo-
neda. No obstante, a los fines del cálculo de la exigencia de capital, la en-
tidad podrá excluir del conjunto de activos subyacentes a las exposiciones
del SPE si puede demostrar que el riesgo no afecta a su posición de tituli-
zación o, en su defecto, que el riesgo es insignificante porque, por ejemplo,
ha sido mitigado.
En el caso de las titulizaciones sintéticas a las que se aporten fondos, se
deberán computar para el cálculo del K los montos recibidos por los ins-
SA
trumentos con vinculación crediticia (“credit linked note”) u otros pasivos
suscriptos por el SPE, cuando dichos importes sirvan como garantía del
repago de la exposición titulizada en cuestión y el riesgo de incumplimiento
esté sujeto a la asignación de pérdidas por tramos. Ello a menos que la en-
tidad pueda demostrar que el riesgo de incumplimiento es insignifican
- entidades de la unidad:
  - `e1` Definicion: K_SA: exigencia de capital promedio subyacente — Exigencia de capital promedio de las exposiciones subyacentes, calculada como el ratio entre la suma de las exposiciones subyacentes ponderadas por riesgo y la suma de las exposiciones subyacentes, mu
  - `e2` Obligacion: Reflejo de coberturas de riesgo en cálculo K_SA — El cálculo de K_SA deberá reflejar los efectos de cualquier cobertura del riesgo de crédito que corresponda aplicar a las exposiciones subyacentes, ya sea individualmente o al conjunto.
  - `e3` Obligacion: Inclusión de exposiciones SPE en activos subyacentes — Cuando la estructura involucre a un SPE, todas las exposiciones del SPE vinculadas a la titulización integran el conjunto de activos subyacentes, incluyendo los activos en los que ha invertido el SPE,
  - `e4` Excepcion: Exclusión de exposiciones SPE si riesgo no afecta o es insignificante — Excepción a la inclusión de exposiciones del SPE: la entidad puede excluirlas del cálculo de K_SA si demuestra que el riesgo no afecta su posición de titulización o que el riesgo es insignificante por
  - `e5` Obligacion: Cómputo de fondos en titulizaciones sintéticas para K_SA — En titulizaciones sintéticas con aporte de fondos, deben computarse para el cálculo de K_SA los montos recibidos por instrumentos con vinculación crediticia u otros pasivos suscritos por el SPE, cuand
  - `e6` Excepcion: Exclusión de cómputo si riesgo de incumplimiento es insignificante — Excepción al cómputo de montos de instrumentos con vinculación crediticia: no se computan si la entidad demuestra que el riesgo de incumplimiento es insignificante.
  - `e7` Obligacion: Cálculo K_SA con monto bruto sin previsión ni descuento — Cuando la entidad ha constituido previsión específica o tiene descuento no reembolsable en el precio de compra, el cálculo de K_SA debe efectuarse usando el monto bruto de la exposición, sin deducir l
  - `e8` Definicion: W: ratio de exposiciones subyacentes en mora — Ratio entre el monto nominal de las exposiciones subyacentes en mora y el monto nominal de las exposiciones subyacentes.
  - `e9` Definicion: Exposiciones en mora: atrasos 90+ días, quiebra, ejecución, bienes inmuebles, incumplimiento — Exposiciones subyacentes con atrasos en pagos de 90 días o más, sujetas a procedimientos de quiebra o concurso, en proceso de ejecución, consistentes en bienes inmuebles adquiridos en defensa del créd
  - `e10` Obligacion: W cero para posiciones de titulización en retitulizaciones — En retitulizaciones con cartera subyacente mixta (tramos de titulización y otros activos), W es cero para posiciones de titulización y la correspondiente según norma para activos subyacentes que no so
  - `e11` Definicion: K_A: exigencia de capital ajustada por mora — Exigencia de capital ajustada, obtenida a partir de K_SA y W conforme a una expresión matemática (no confiable por ser fórmula).
  - `e12` Obligacion: Cálculo separado K_A por subconjunto en retitulizaciones — En retitulizaciones con cartera subyacente mixta, debe calcularse K_A por separado para cada subconjunto, aplicando W por separado según lo previsto para cada tipo de activo.
  - `e13` Obligacion: K_A para retitulización como promedio ponderado por exposición nominal — K_A para la exposición a una retitulización es el promedio ponderado por la exposición nominal de los K_A correspondientes a cada subconjunto.
  - `e14` Obligacion: Ajuste K_A si desconocimiento ≤5% cumplimiento exposiciones — Si se desconoce la situación de cumplimiento de 5 % o menos de las exposiciones subyacentes, debe ajustarse el cálculo de K_A.
  - `e15` Restriccion: Ponderación 1250% si desconocimiento >5% cumplimiento — Si la entidad desconoce la situación de cumplimiento para más del 5 % de la posición de titulización, ésta debe ponderarse al 1250 %.
  - `e16` Definicion: K_SSFA(K_A): exigencia de capital por posición de titulización — Exigencia de capital por unidad de posición de titulización, calculada conforme a una expresión matemática (no confiable por ser fórmula) con parámetro p que varía según criterios STC y tipo de tituli
  - `e17` Definicion: Parámetro p=0,5 si titulización cumple criterios STC — Parámetro p toma valor 0,5 si la titulización cumple con los criterios STC del punto 3.1.14.
  - `e18` Definicion: Parámetro p=1 si titulización no cumple criterios STC — Parámetro p toma valor 1 si la titulización no cumple con los criterios STC del punto 3.1.14.
  - `e19` Definicion: Parámetro p=1,5 si retitulización — Parámetro p toma valor 1,5 si se trata de una retitulización.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 28** Excepcion `e4`: Exclusión de exposiciones SPE si riesgo no afecta o es insignificante | descripcion: Excepción a la inclusión de exposiciones del SPE: la entidad puede excluirlas del cálculo de K_SA si demuestra que el riesgo no afecta su posición de titulización o que el riesgo es insignificante por haber sido mitigado. | tramo: a los fines del cálculo de la exigencia de capital, la entidad podrá excluir del conjunto de activos subyacentes a las exposiciones del SPE si puede demostrar que el riesgo no afecta a su posición de titulización o, en su defecto, que el riesgo es insignificante porque, por ejemplo, ha sido mitigado
  - **caso 30** Excepcion `e6`: Exclusión de cómputo si riesgo de incumplimiento es insignificante | descripcion: Excepción al cómputo de montos de instrumentos con vinculación crediticia: no se computan si la entidad demuestra que el riesgo de incumplimiento es insignificante. | tramo: Ello a menos que la entidad pueda demostrar que el riesgo de incumplimiento es insignificante

## Unidad `docvig::2.1.3` (punto_no_item)
- herencia: [encabezado 2.1] 2.1. De hasta 75 años al 31.12.14.
- texto propio: 2.1.3. A partir del año de otorgada la residencia permanente o temporaria en el país.
Documento Nacional de Identidad digital (DNI-d).
De existir prueba en contrario del país de domicilio, aplicará el punto 2.1.2.
En todos los casos deberá acreditarse la categoría de residencia, su vigencia y el tiempo de
radicación a partir de documentación emitida por la DNM.
El DNI-d en formato credencial virtual para dispositivos móviles inteligentes podrá ser exhibido
en las casas operativas de las entidades financieras en la medida que se observen las disposi-
ciones contenidas en el punto 2.12. de las normas sobre “Medidas mínimas de seguridad en
entidades financieras”.
- entidades de la unidad:
  - `e1` Operacion: Emisión DNI digital — Emisión del Documento Nacional de Identidad digital (DNI-d) para extranjeros a partir del año de otorgada la residencia permanente o temporaria en el país.
  - `e2` Obligacion: Acreditación categoría residencia y vigencia — Deber de acreditar la categoría de residencia, su vigencia y el tiempo de radicación a partir de documentación emitida por la Dirección Nacional de Migraciones (DNM).
  - `e3` Potestad: Exhibición DNI-d en formato credencial virtual — Facultad de exhibir el DNI-d en formato credencial virtual para dispositivos móviles inteligentes en las casas operativas de las entidades financieras, condicionada a la observancia de las disposicion
  - `e4` Excepcion: Excepción prueba contraria domicilio — Excepción a la norma de residencia permanente o temporaria: si existe prueba en contrario del país de domicilio, se aplica el punto 2.1.2.
  - `e5` Condicion: Observancia disposiciones seguridad — Condición para la exhibición del DNI-d en formato credencial virtual: observancia de las disposiciones del punto 2.12 de las normas sobre Medidas mínimas de seguridad en entidades financieras.
- relaciones del crudo (sin establecida_en ni de sujeto): e5 condicion_de e3
- NODOS A CLASIFICAR:
  - **caso 29** Excepcion `e4`: Excepción prueba contraria domicilio | descripcion: Excepción a la norma de residencia permanente o temporaria: si existe prueba en contrario del país de domicilio, se aplica el punto 2.1.2. | tramo: De existir prueba en contrario del país de domicilio, aplicará el punto 2.1.2.

## Unidad `cap::5.3.1.1` (punto_no_item)
- herencia: [chapeau_seccion S5] A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o
parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera
de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las
técnicas previstas en el punto 5.1.
La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia-
ción con títulos valores (securities financing transactions, SFT) –co | [intro 5.3] La aplicación de la técnica de cobertura mediante activos admitidos como garantía dependerá
del método elegido. | [intro 5.3.1] Con este método, el ponderador de riesgo de la contraparte se sustituye por el pondera-
dor de riesgo del activo mediante el cual se cubre –parcial o totalmente– la exposición
–conforme a la tabla de ponderadores prevista en la Sección 2.–.
- texto propio: 5.3.1.1. Aplicación.
Para que la CRC sea reconocida, la exposición deberá estar cubierta durante
todo el plazo de vencimiento contractual (no se admitirá el descalce de plazos
de vencimiento) y el activo recibido en garantía se limitará a aquellos listados
en el punto 5.3.1.2. y contar con una valuación a precios de mercado con una
frecuencia mínima mensual.
La parte de la exposición cubierta recibirá el ponderador de riesgo correspon-
diente al activo recibido en garantía, pero estará sujeta a un mínimo del 20%
–salvo lo dispuesto en el punto 5.3.1.3.–. A la parte no cubierta se le aplicará el
ponderador de riesgo que le corresponda según el tipo de exposición de que se
trate.
Se admitirá el descalce de monedas entre la exposición y el activo admitido
como garantía, pero en ese caso no será necesaria la aplicación de tratamiento
alguno.
- entidades de la unidad:
  - `e1` Condicion: Cobertura durante todo plazo vencimiento — La exposición debe estar cubierta durante todo el plazo de vencimiento contractual, sin admitirse descalce de plazos de vencimiento.
  - `e2` Restriccion: Prohibición descalce plazos vencimiento — No se admitirá el descalce de plazos de vencimiento entre la exposición y el activo recibido en garantía.
  - `e3` Restriccion: Limitación activos admitidos como garantía — El activo recibido en garantía se limitará a aquellos listados en el punto 5.3.1.2.
  - `e4` Obligacion: Valuación activo garantía frecuencia mensual — El activo recibido en garantía debe contar con una valuación a precios de mercado con una frecuencia mínima mensual.
  - `e5` Restriccion: Ponderador mínimo 20% parte cubierta — La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20%.
  - `e6` Excepcion: Excepción ponderador mínimo 20% — Excepción al ponderador mínimo del 20% conforme a lo dispuesto en el punto 5.3.1.3.
  - `e7` Obligacion: Aplicación ponderador parte no cubierta — A la parte no cubierta se le aplicará el ponderador de riesgo que le corresponda según el tipo de exposición de que se trate.
  - `e8` Potestad: Permiso descalce monedas sin tratamiento — Se admite el descalce de monedas entre la exposición y el activo admitido como garantía, sin necesidad de aplicar tratamiento alguno.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 31** Excepcion `e6`: Excepción ponderador mínimo 20% | descripcion: Excepción al ponderador mínimo del 20% conforme a lo dispuesto en el punto 5.3.1.3. | tramo: salvo lo dispuesto en el punto 5.3.1.3.
  - **caso 150** Condicion `e1`: Cobertura durante todo plazo vencimiento | descripcion: La exposición debe estar cubierta durante todo el plazo de vencimiento contractual, sin admitirse descalce de plazos de vencimiento. | tramo: la exposición deberá estar cubierta durante todo el plazo de vencimiento contractual

## Unidad `ext::3.5.6.6` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.5] exterior.
Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o
intereses de títulos de deuda con registro público en el exterior, otros endeudamientos
financieros con el exterior y títulos de deuda con registro público en el país denominados en
moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las
siguientes condiciones: | **[abre la lista]** [intro 3.5.6] para la cancelación de capital e intereses de endeudamientos financieros
comprendidos en este punto 3.5. cuando el acreedor sea una contraparte vinculada al
deudor.
Este requisito no resultará aplicable cuando la operación encuadre en alguna de las
siguientes situaciones: | [cierre 3.5.6] Las deudas comprendidas en este punto continuarán sujetas a la conformidad previa
aun cuando existiese una modificación del acreedor o del deudor que conlleve a que
ya no exista una vinculación entre el acreedor y el deudor residente.
- texto propio: 3.5.6.6. se trate de un pago de intereses que se concreta simultáneamente con la
liquidación por el importe al menos equivalente de:
i) nuevos endeudamientos financieros comprendidos en este punto 3.5.
con una vida promedio no inferior a 2 (dos) años y que contemplen
como mínimo 1 (un) año de gracia para el pago de capital, en ambos
casos contados desde la fecha en que se concreta el acceso al
mercado.
ii) nuevos aportes de inversión directa de no residentes.
Los endeudamientos financieros y/o los aportes de inversión extranjera
directa, que no podrán ser computados a los efectos de otros mecanismos
considerados en la normativa cambiaria, podrán ser ingresados y liquidados
por el deudor que cancela los intereses o por otra empresa residente
perteneciente a su grupo económico.
- entidades de la unidad:
  - `e1` Excepcion: Excepción — pago simultáneo de intereses con nuevo endeudamiento — Excepción al requisito de conformidad previa del BCRA cuando el pago de intereses se concreta simultáneamente con la liquidación de nuevos endeudamientos financieros con vida promedio no inferior a 2 
  - `e2` Excepcion: Excepción — pago simultáneo de intereses con aportes de inversión directa — Excepción al requisito de conformidad previa del BCRA cuando el pago de intereses se concreta simultáneamente con la liquidación de nuevos aportes de inversión directa de no residentes.
  - `e3` Restriccion: Prohibición — cómputo de endeudamientos en otros mecanismos — Los endeudamientos financieros y los aportes de inversión extranjera directa que se utilizan para cumplir con la excepción no podrán ser computados a los efectos de otros mecanismos considerados en la
  - `e4` Operacion: Ingreso y liquidación de endeudamientos e inversión extranjera — Ingreso y liquidación de endeudamientos financieros y/o aportes de inversión extranjera directa, que pueden ser realizados por el deudor que cancela los intereses o por otra empresa residente pertenec
  - `e5` Condicion: Condición — simultaneidad de pago de intereses y liquidación — El pago de intereses debe concretarse simultáneamente con la liquidación de nuevos endeudamientos o aportes de inversión.
- relaciones del crudo (sin establecida_en ni de sujeto): e5 condicion_de e1; e5 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 32** Excepcion `e1`: Excepción — pago simultáneo de intereses con nuevo endeudamiento | descripcion: Excepción al requisito de conformidad previa del BCRA cuando el pago de intereses se concreta simultáneamente con la liquidación de nuevos endeudamientos financieros con vida promedio no inferior a 2 años y con mínimo 1 año de gracia para el pago de capital. | tramo: se trate de un pago de intereses que se concreta simultáneamente con la liquidación por el importe al menos equivalente de: i) nuevos endeudamientos financieros comprendidos en este punto 3.5. con una vida promedio no inferior a 2 (dos) años y que contemplen como mínimo 1 (un) año de gracia para el pago de capital, en ambos casos contados desde la fecha en que se concreta el acceso al mercado.
  - **caso 33** Excepcion `e2`: Excepción — pago simultáneo de intereses con aportes de inversión directa | descripcion: Excepción al requisito de conformidad previa del BCRA cuando el pago de intereses se concreta simultáneamente con la liquidación de nuevos aportes de inversión directa de no residentes. | tramo: se trate de un pago de intereses que se concreta simultáneamente con la liquidación por el importe al menos equivalente de: ii) nuevos aportes de inversión directa de no residentes.

## Unidad `ext::2.2.2.1` (item)
- herencia: **[abre la lista]** [intro 2.2.2] servicios que ingresen en los plazos normativos previstos y encuadren en las
siguientes situaciones:
- texto propio: 2.2.2.1. Se trata de cobros de exportaciones de servicios prestados por personas
humanas y se cumplen la totalidad de las siguientes condiciones:
i) Las operaciones correspondan a los siguientes códigos de concepto:
S01 Mantenimiento y reparaciones.
S07 Servicios de construcción.
S12 Servicios de telecomunicaciones.
S13 Servicios de informática.
S14 Servicios de información.
S15 Cargos por el uso de la propiedad intelectual.
S16 Servicios de investigación y desarrollo.
S17 Servicios jurídicos, contables y gerenciales.
S18 Servicios de publicidad, investigación de mercado y encuestas
de opinión pública.
S19 Servicios arquitectónicos, de ingeniería y otros servicios
técnicos.
S21 Servicios relacionados con el comercio.
S22 Otros servicios empresariales.
S23 Servicios audiovisuales y conexos.
S24 Otros servicios personales, culturales y recreativos.
S27 Otros servicios de salud.
S28 Enseñanzas educativas.
ii) Los fondos sean acreditados en cuentas en moneda extranjera de
titularidad del cliente en entidades financieras locales.
iii) El cliente no ha utilizado este mecanismo por un monto superior al
equivalente de USD 36.000 (dólares estadounidenses treinta y seis mil)
en el año calendario, en el conjunto de las entidades y por el conjunto
de los conceptos comprendidos.
iv)La entidad interviniente cuenta con una declaración jurada del
exportador en la que deje constancia de que no supera el límite anual
establecido en el conjunto de las entidades y por el conjunto de los
conceptos comprendidos.
v) La utilización de este mecanismo deberá resultar neutra en materia
fiscal.
A los efectos del registro de estas operaciones se deberán confeccionar dos
boletos sin movimiento de pesos, el boleto de compra se realizará por el
concepto de servicios que corresponda y el boleto de vent
- entidades de la unidad:
  - `e1` Excepcion: Excepción cobros exportaciones servicios personas humanas — Excepción de la obligación de liquidación para cobros de exportaciones de servicios prestados por personas humanas que cumplan las condiciones especificadas
  - `c1` Condicion: Códigos de concepto de servicios específicos — Las operaciones deben corresponder a uno de los códigos de concepto de servicios enumerados: S01, S07, S12, S13, S14, S15, S16, S17, S18, S19, S21, S22, S23, S24, S27, S28
  - `c2` Condicion: Acreditación en cuentas moneda extranjera — Los fondos deben ser acreditados en cuentas en moneda extranjera de titularidad del cliente en entidades financieras locales
  - `c3` Condicion: Límite anual USD 36.000 por cliente — El cliente no ha utilizado este mecanismo por un monto superior al equivalente de USD 36.000 en el año calendario, considerando el conjunto de las entidades y el conjunto de los conceptos
  - `c4` Condicion: Declaración jurada del exportador — La entidad interviniente debe contar con una declaración jurada del exportador que deje constancia de que no supera el límite anual establecido en el conjunto de las entidades y por el conjunto de los
  - `c5` Condicion: Neutralidad fiscal — La utilización de este mecanismo debe resultar neutra en materia fiscal
  - `o1` Obligacion: Confección de dos boletos sin movimiento de pesos — Para el registro de estas operaciones se deben confeccionar dos boletos sin movimiento de pesos: el boleto de compra por el concepto de servicios que corresponda y el boleto de venta bajo el código de
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1; c2 condicion_de e1; c3 condicion_de e1; c4 condicion_de e1; c5 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 34** Excepcion `e1`: Excepción cobros exportaciones servicios personas humanas | descripcion: Excepción de la obligación de liquidación para cobros de exportaciones de servicios prestados por personas humanas que cumplan las condiciones especificadas | tramo: Quedarán exceptuados de la obligación de liquidación los cobros de exportaciones de servicios que ingresen en los plazos normativos previstos y encuadren en las siguientes situaciones: Se trata de cobros de exportaciones de servicios prestados por personas humanas y se cumplen la totalidad de las siguientes condiciones

## Unidad `cap::8.4.2.2` (punto_no_item)
- herencia: [encabezado 8.4.2] 8.4.2. Conceptos deducibles aplicables, según corresponda, a los distintos niveles de capital.
- texto propio: 8.4.2.2. Inversiones en instrumentos computables como capital regulatorio de entidades
financieras y de empresas de servicios complementarios de la actividad finan-
ciera, no sujetas a supervisión consolidada, y compañías de seguro, cuando la
entidad posea más del 10 % del capital social ordinario de la emisora, o cuando
la emisora sea subsidiaria de la entidad financiera.
Criterios:
i) Las inversiones incluyen las participaciones directas, indirectas y sintéticas.
A estos efectos se entiende como participación indirecta a la inversión de
una entidad financiera en otra entidad o empresa no sujeta a supervisión
consolidada, que a su vez tiene una participación en el capital de otra enti-
dad financiera o empresa que no consolida con la primera. La participación
sintética se refiere a la inversión que una entidad financiera realiza en un ins-
trumento cuyo valor está directamente relacionado al valor del capital de otra
entidad financiera o empresa no sujeta a supervisión consolidada.
ii) Se incluye la posición comprada neta; es decir, la posición comprada bruta
menos la posición vendida en la misma exposición subyacente, cuando ésta
tenga la misma duración que la posición comprada o su vida residual sea al
menos un año.
iii) Podrán excluirse las tenencias de títulos valores suscriptos para ser coloca-
dos en el plazo de cinco días hábiles.
iv) Las inversiones en instrumentos de capital que no cumplan con los criterios
para ser clasificados como CO , CA o PN de la entidad financiera serán
n1 n1 c
considerados como CO –acciones ordinarias– a los efectos de este ajuste
n1
regulatorio.
El importe de estas participaciones -teniendo en cuenta el tipo de instrumento
de que se trate- deberá deducirse de cada uno de los correspondientes niveles
de capital de la entidad financiera
- entidades de la unidad:
  - `e1` Operacion: Inversiones en instrumentos computables como capital regulatorio — Inversiones en instrumentos computables como capital regulatorio de entidades financieras, empresas de servicios complementarios no sujetas a supervisión consolidada y compañías de seguro, realizadas 
  - `e2` Definicion: Participación indirecta — Inversión de una entidad financiera en otra entidad o empresa no sujeta a supervisión consolidada, que a su vez tiene una participación en el capital de otra entidad financiera o empresa que no consol
  - `e3` Definicion: Participación sintética — Inversión que una entidad financiera realiza en un instrumento cuyo valor está directamente relacionado al valor del capital de otra entidad financiera o empresa no sujeta a supervisión consolidada
  - `e4` Definicion: Posición comprada neta — Posición comprada bruta menos la posición vendida en la misma exposición subyacente, cuando ésta tenga la misma duración que la posición comprada o su vida residual sea al menos un año
  - `e5` Excepcion: Exclusión tenencias títulos valores para colocación — Exclusión de tenencias de títulos valores suscriptos para ser colocados dentro del plazo de cinco días hábiles de la deducción de capital
  - `e6` Obligacion: Clasificación como CO n1 de inversiones que no cumplen criterios — Las inversiones en instrumentos de capital que no cumplan con los criterios para ser clasificados como CO n1, CA n1 o PN c de la entidad financiera deben ser consideradas como CO n1 (acciones ordinari
  - `e7` Obligacion: Deducción de participaciones de niveles de capital — El importe de las participaciones, teniendo en cuenta el tipo de instrumento, debe deducirse de cada uno de los correspondientes niveles de capital de la entidad financiera
  - `e8` Obligacion: Deducción del remanente del nivel superior — Si la entidad financiera carece de suficiente capital para efectuar la deducción de un nivel particular de capital, el remanente debe deducirse del nivel inmediato superior
  - `e9` Condicion: Posesión más del 10% del capital social ordinario — Supuesto en que la entidad posee más del 10% del capital social ordinario de la emisora
  - `e10` Condicion: Emisora subsidiaria de la entidad financiera — Supuesto en que la emisora es subsidiaria de la entidad financiera
  - `e11` Condicion: Vida residual al menos un año — Supuesto en que la posición vendida tenga la misma duración que la posición comprada o su vida residual sea al menos un año
- relaciones del crudo (sin establecida_en ni de sujeto): e9 condicion_de e1; e10 condicion_de e1; e11 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 35** Excepcion `e5`: Exclusión tenencias títulos valores para colocación | descripcion: Exclusión de tenencias de títulos valores suscriptos para ser colocados dentro del plazo de cinco días hábiles de la deducción de capital | tramo: Podrán excluirse las tenencias de títulos valores suscriptos para ser colocados en el plazo de cinco días hábiles

## Unidad `cap::6.3.2.2` (punto_no_item)
- herencia: [intro 6.3] La exigencia de capital por el riesgo de mantener posiciones en acciones en la cartera de ne-
gociación alcanza a las posiciones compradas y vendidas en acciones ordinarias, títulos de
deuda convertibles que se comporten como acciones y los compromisos para adquirir o ven-
der acciones, así como en todo otro instrumento que tenga un comportamiento en el mercado
similar al de las acciones, excluyendo a las acciones preferidas no convertibles, a las que se
aplicará la exigencia por riesgo de tasa  | [intro 6.3.2] A excepción de las opciones sobre acciones e índices bursátiles, que se tratan en el
punto 6.6., los restantes derivados sobre acciones y las posiciones fuera de balance
sensibles a los cambios en los precios de mercado deberán incluirse en el cómputo de
la exigencia. Esto comprende a los futuros, “forwards” y “swaps”, tanto de acciones in-
dividuales como de índices bursátiles. Los derivados se convertirán en posiciones en su
correspondiente subyacente.
- texto propio: 6.3.2.2. Exigencia de capital por derivados sobre acciones.
i) Exigencia de capital por riesgo específico y por riesgo general de merca-
do.
Cada posición compensada con una acción o índice bursátil idéntico podrá
ser neteada en su totalidad, dando lugar a una única posición neta, vendi-
da o comprada, sobre la que se aplicarán las exigencias de capital por
riesgo específico y riesgo general de mercado.
El riesgo de tasa de interés del derivado se computará conforme a lo indi-
cado en el punto 6.2.
ii) Exigencia de capital por índices.
Además de la exigencia por riesgo general de mercado, se aplicará una
exigencia de capital adicional de 2% de la posición neta, comprada o ven-
dida, en contratos sobre índices calculados sobre carteras diversificadas
de acciones a los efectos de cubrir factores tales como los riesgos de eje-
cución. Será objeto de revisión por parte de la Superintendencia de Enti-
dades Financieras y Cambiarias que el ponderador de 2% se aplique sólo
a índices bien diversificados y no, por ejemplo, a índices sectoriales.
iii) Arbitraje.
a) En el caso de las siguientes estrategias de arbitraje relacionadas con
futuros, la exigencia de capital adicional de 2% del acápite ii) prece-
dente se podrá aplicar sólo a uno de los índices (quedando exenta la
posición contraria):
- cuando la entidad asuma la posición contraria en exactamente el
mismo índice pero a distintos vencimientos o mercados;
- cuando la entidad mantenga la posición opuesta en contratos a
idéntica fecha pero en índices diferentes, aunque similares, a cuyo
efecto deberá tener a disposición de la Superintendencia de Enti-
dades Financieras y Cambiarias evidencia de que ambos índices
contienen suficientes componentes comunes como para justificar
tal compensación.
b) Se aplicará una exigencia de c
- entidades de la unidad:
  - `e1` Operacion: Neteado de posición derivada con subyacente idéntico — Neteado en su totalidad de una posición derivada compensada con una acción o índice bursátil idéntico, dando lugar a una única posición neta, vendida o comprada, sobre la que se aplicarán las exigenci
  - `e2` Obligacion: Aplicación de exigencias de capital por riesgo específico y general — Aplicación de exigencias de capital por riesgo específico y riesgo general de mercado sobre la posición neta resultante del neteado de derivados con subyacente idéntico.
  - `e3` Obligacion: Cómputo de riesgo de tasa de interés del derivado — El riesgo de tasa de interés del derivado se computará conforme a lo indicado en el punto 6.2.
  - `e4` Restriccion: Exigencia adicional 2% — índices diversificados — Exigencia de capital adicional de 2% de la posición neta, comprada o vendida, en contratos sobre índices calculados sobre carteras diversificadas de acciones a los efectos de cubrir factores tales com
  - `e5` Potestad: Revisión de aplicación del ponderador 2% — Superintendencia — La Superintendencia de Entidades Financieras y Cambiarias revisará que el ponderador de 2% se aplique sólo a índices bien diversificados y no a índices sectoriales.
  - `e6` Excepcion: Exención exigencia 2% — arbitraje mismo índice distintos vencimientos — Exención de la exigencia de capital adicional de 2% cuando la entidad asume la posición contraria en exactamente el mismo índice pero a distintos vencimientos o mercados, quedando exenta la posición c
  - `e7` Excepcion: Exención exigencia 2% — arbitraje índices diferentes similares — Exención de la exigencia de capital adicional de 2% cuando la entidad mantiene la posición opuesta en contratos a idéntica fecha pero en índices diferentes, aunque similares, siempre que tenga a dispo
  - `e8` Condicion: Condición — evidencia de componentes comunes en índices — Que la entidad tenga a disposición de la Superintendencia de Entidades Financieras y Cambiarias evidencia de que ambos índices contienen suficientes componentes comunes como para justificar la compens
  - `e9` Restriccion: Exigencia 4% — arbitraje futuro índice amplio con canasta acciones — Exigencia de capital de 4% a las posiciones que surjan de estrategias de arbitraje en las que un futuro sobre un índice amplio se calce con una canasta de acciones, que refleja los riesgos de divergen
  - `e10` Condicion: Condición — estrategia deliberada y vigilada — Que la estrategia de arbitraje haya sido adoptada en forma deliberada y se vigile y gestione en forma particularizada.
  - `e11` Condicion: Condición — canasta representa al menos 90% del índice — Que la composición de la canasta de acciones represente al menos el 90% del índice si se descompone en sus componentes nocionales.
  - `e12` Obligacion: Tratamiento de excedentes — posiciones abiertas — Cualquier valor excedente de las acciones que componen la canasta por encima del valor del futuro o cualquier valor excedente del futuro sobre el valor de la canasta se considerará como una posición a
  - `e13` Potestad: Compensación de posiciones contrarias — mercados diferentes — Facultad de compensar posiciones contrarias, incluso tratándose de posiciones en mercados diferentes o de certificados de depósito de acciones, sin aplicar exigencias de capital, siempre que se tengan
  - `e14` Condicion: Condición — consideración de costos de conversión — Que se tengan en cuenta todos los costos de conversión, cuando los hubiera, en la compensación de posiciones contrarias en mercados diferentes o de certificados de depósito de acciones.
  - `e15` Obligacion: Cómputo de riesgo de tipo de cambio — posiciones compensadas — Todo riesgo de tipo de cambio que surja de posiciones compensadas en mercados diferentes o de certificados de depósito de acciones deberá computarse según se establece en el punto 6.4.
- relaciones del crudo (sin establecida_en ni de sujeto): e8 condicion_de e7; e10 condicion_de e9; e11 condicion_de e9; e14 condicion_de e13
- NODOS A CLASIFICAR:
  - **caso 36** Excepcion `e6`: Exención exigencia 2% — arbitraje mismo índice distintos vencimientos | descripcion: Exención de la exigencia de capital adicional de 2% cuando la entidad asume la posición contraria en exactamente el mismo índice pero a distintos vencimientos o mercados, quedando exenta la posición contraria. | tramo: cuando la entidad asuma la posición contraria en exactamente el mismo índice pero a distintos vencimientos o mercados
  - **caso 37** Excepcion `e7`: Exención exigencia 2% — arbitraje índices diferentes similares | descripcion: Exención de la exigencia de capital adicional de 2% cuando la entidad mantiene la posición opuesta en contratos a idéntica fecha pero en índices diferentes, aunque similares, siempre que tenga a disposición de la Superintendencia evidencia de que ambos índices contienen suficientes componentes comunes como para justificar tal compensación. | tramo: cuando la entidad mantenga la posición opuesta en contratos a idéntica fecha pero en índices diferentes, aunque similares

## Unidad `ext::8.5.17.15` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.15. Exportaciones desde el Territorio Nacional Continental al área franca (art.
18 de la Ley 19.640).
En cuanto a las exportaciones desde el Territorio Nacional Continental al
área franca, la exención de ingreso de divisas es procedente en tanto
supongan abastecimiento del área franca y no exista ulterior
reexportación (a decisión de la Dirección General de Aduanas, según el
apartado primero del art. 17 del Decreto 9.208/72).
- entidades de la unidad:
  - `e1` Operacion: Exportación desde Territorio Nacional Continental al área franca — Exportación de bienes desde el Territorio Nacional Continental al área franca, sujeta a que supongan abastecimiento del área franca y no exista ulterior reexportación
  - `e2` Excepcion: Exención ingreso divisas — exportaciones área franca — Exención del requisito de ingreso de divisas para exportaciones al área franca, cuando supongan abastecimiento del área franca y no exista ulterior reexportación
  - `e3` Condicion: Abastecimiento del área franca sin reexportación — La operación debe suponer abastecimiento del área franca y no debe existir ulterior reexportación
  - `e4` Potestad: Decisión Dirección General de Aduanas sobre reexportación — La Dirección General de Aduanas tiene facultad para decidir sobre la procedencia de la exención en casos de reexportación, conforme al apartado primero del art. 17 del Decreto 9.208/72
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 38** Excepcion `e2`: Exención ingreso divisas — exportaciones área franca | descripcion: Exención del requisito de ingreso de divisas para exportaciones al área franca, cuando supongan abastecimiento del área franca y no exista ulterior reexportación | tramo: la exención de ingreso de divisas es procedente en tanto supongan abastecimiento del área franca y no exista ulterior reexportación

## Unidad `ext::8.5.17.14` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.14. Exportaciones del Área Aduanera Especial a las áreas francas nacionales
y al resto del territorio de la Nación.
En cuanto a las exportaciones del Área Aduanera Especial al área franca,
la exención de ingreso de divisas es procedente en tanto supongan
abastecimiento mismo del área franca y no exista ulterior reexportación (a
decisión de la Dirección General de Aduanas, según el apartado segundo
del art. 12 del Decreto 9.208/72).
- entidades de la unidad:
  - `e1` Operacion: Exportación Área Aduanera Especial a áreas francas — Exportaciones del Área Aduanera Especial a las áreas francas nacionales y al resto del territorio de la Nación, exceptuadas del seguimiento de divisas cuando suponen abastecimiento del área franca sin
  - `e2` Excepcion: Exención seguimiento — exportaciones Área Aduanera Especial — Exención del seguimiento de ingreso de divisas para exportaciones del Área Aduanera Especial a áreas francas cuando suponen abastecimiento del área franca y no existe ulterior reexportación
  - `e3` Condicion: Abastecimiento área franca sin reexportación — La operación supone abastecimiento del área franca y no existe ulterior reexportación
  - `e4` Potestad: Decisión Dirección General de Aduanas — procedencia exención — La Dirección General de Aduanas decide sobre la procedencia de la exención de ingreso de divisas, según el apartado segundo del artículo 12 del Decreto 9.208/72
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 39** Excepcion `e2`: Exención seguimiento — exportaciones Área Aduanera Especial | descripcion: Exención del seguimiento de ingreso de divisas para exportaciones del Área Aduanera Especial a áreas francas cuando suponen abastecimiento del área franca y no existe ulterior reexportación | tramo: la exención de ingreso de divisas es procedente en tanto supongan abastecimiento mismo del área franca y no exista ulterior reexportación

## Unidad `cap::4.3.3.1` (punto_no_item)
- herencia: [intro 4.3] contraparte central.
Comprende a aquellas exposiciones de las entidades financieras con entidades de contrapar-
te central (CCP) que se originen en derivados OTC o negociados en mercados de valores y
en operaciones de financiación con títulos valores (“Securities Financing Transactions”, SFT)
y operaciones de liquidación diferida –definidas en el punto 4.2.–.
No están comprendidas las exposiciones originadas en operaciones al contado y que involu-
cren títulos valores, oro o moneda extranjera, c | [encabezado 4.3.3] 4.3.3. Exposiciones a entidades de contraparte central calificadas.
- texto propio: 4.3.3.1. Exposiciones por operaciones de negociación.
i) Exposiciones de los miembros compensadores con las CCP.
a) La entidad financiera que actúe en carácter de miembro compensa-
dor de una CCP por operaciones propias deberá aplicar un pondera-
dor de riesgo del 2 % a sus exposiciones con la CCP originadas en
operaciones de derivados –OTC o negociados en mercados de valo-
res–, de financiación con títulos valores (SFT) y de liquidación diferi-
da. Cuando la entidad financiera preste servicios de compensación a
clientes, aplicará el ponderador de riesgo del 2 % a la exposición con
la CCP que se origina si, en caso de incumplimiento de la CCP, la
entidad financiera se viera obligada –como miembro compensador a
reembolsar al cliente toda pérdida debido al cambio de valor de sus
transacciones. El ponderador de riesgo aplicado a los activos en ga-
rantía aportados por la entidad financiera a una CCP deberá determi-
narse de acuerdo con lo establecido en los párrafos primero a tercero
del acápite iv) del presente punto.
b) La exposición debida a dichas operaciones se calculará conforme al
enfoque estandarizado para el riesgo de crédito de contraparte (SA-
CCR) establecido en el punto 4.2. para los derivados OTC o negó
ciados en mercados de valores y operaciones de liquidación diferida,
y a lo previsto en la Sección 5. para las SFT.
No se aplicará el plazo mínimo de veinte días hábiles para el cálculo
del período de riesgo de margen (MPOR) de los conjuntos de neteo
en los que se verifiquen más de 5.000 operaciones en la medida en
que no existan disputas pendientes y que dicho conjunto no contenga
garantías ilíquidas u operaciones exóticas. Idéntico criterio se aplica-
rá para la determinación del período de mantenimiento mínimo (T )
M
utilizado en el cálculo de los aforos de
- entidades de la unidad:
  - `e1` Operacion: Exposiciones por operaciones de negociación — miembros compensadores con CCP — Exposiciones de los miembros compensadores con las CCP originadas en operaciones de derivados (OTC o negociados en mercados de valores), de financiación con títulos valores (SFT) y de liquidación dife
  - `e2` Restriccion: Ponderador 2% — exposiciones miembro compensador con CCP (operaciones propias) — Ponderador de riesgo del 2% aplicable a exposiciones de miembro compensador con CCP por operaciones propias (derivados OTC, derivados negociados en mercados de valores, SFT, liquidación diferida).
  - `e3` Restriccion: Ponderador 2% — exposiciones miembro compensador con CCP (servicios de compensación a clientes) — Ponderador de riesgo del 2% aplicable a exposición con CCP cuando miembro compensador presta servicios de compensación a clientes y se vería obligado a reembolsar pérdidas por cambio de valor de trans
  - `e4` Obligacion: Determinación ponderador — activos en garantía a CCP — El ponderador de riesgo de activos en garantía aportados a CCP debe determinarse conforme a lo establecido en los párrafos primero a tercero del acápite iv).
  - `e5` Obligacion: Cálculo exposición — enfoque estandarizado (SA-CCR) — La exposición debe calcularse conforme al enfoque estandarizado para riesgo de crédito de contraparte (SA-CCR) del punto 4.2 para derivados OTC, derivados negociados en mercados de valores y operacion
  - `e6` Excepcion: Excepción MPOR mínimo 20 días — conjuntos con más de 5.000 operaciones — No se aplica el plazo mínimo de 20 días hábiles para cálculo de MPOR en conjuntos de neteo con más de 5.000 operaciones, siempre que no existan disputas pendientes y no contengan garantías ilíquidas u
  - `e6a` Condicion: Condición — no existan disputas pendientes — No existan disputas pendientes en el conjunto de neteo.
  - `e6b` Condicion: Condición — conjunto no contenga garantías ilíquidas u operaciones exóticas — El conjunto de neteo no contenga garantías ilíquidas u operaciones exóticas.
  - `e7` Obligacion: Aplicación idéntico criterio — período de mantenimiento mínimo (TM) en SFT — Idéntico criterio de excepción al plazo mínimo se aplicará para determinación del período de mantenimiento mínimo (TM) en cálculo de aforos de SFT del punto 5.3.2.3.
  - `e8` Restriccion: MPOR mínimo 10 días — derivados OTC con CCP — Se utilizará un MPOR mínimo de 10 días para cálculo de exposiciones a CCP por operaciones de derivados OTC.
  - `e9` Restriccion: Horizonte temporal mínimo 1 año o plazo residual — margen de variación sin protección — Cuando CCP recibe margen de variación y activo del miembro compensador no está protegido contra insolvencia de CCP, horizonte temporal de riesgo mínimo será el menor entre 1 año y plazo residual de op
  - `e10` Operacion: Operaciones con CCP en jurisdicciones con validez legal de liquidación neta — Operaciones con CCP radicadas en jurisdicciones donde liquidación por saldos netos en caso de incumplimiento tiene validez legal, independientemente de insolvencia o quiebra de contraparte.
  - `e11` Obligacion: Cálculo costo de reposición neto — operaciones con CCP — Costo de reposición total de contratos relevantes puede calcularse como costo de reposición neto, siempre que conjunto de operaciones compensables cumpla requisitos de validez legal del punto 5.3.2.5 
  - `e12` Definicion: Acuerdo de neteo — interpretación inclusiva — Incluye todo acuerdo de neteo con validez legal que reconozca derechos de compensación legalmente exigibles, cuando las disposiciones refieran a 'acuerdo marco de neteo' o 'contrato de neteo con una c
  - `e13` Obligacion: Tratamiento individual de transacciones — sin cumplimiento de requisitos de neteo — Si entidad financiera no puede demostrar que acuerdos de neteo cumplen requisitos, cada transacción individual se considerará como conjunto de neteo separado para cálculo de exposición por operaciones
  - `e14` Operacion: Exposiciones de miembros compensadores con sus clientes — Exposiciones de miembros compensadores con sus clientes en operaciones compensadas.
  - `e15` Obligacion: Consideración exposición bilateral — miembro compensador con cliente — Miembro compensador debe considerar su exposición con cliente (incluyendo potencial exposición CVA) como operación bilateral, independientemente de si garantiza operación o actúa como intermediario en
  - `e16` Restriccion: MPOR mínimo 5 días — exposición miembro compensador con clientes — Miembros compensadores pueden calcular exigencia por exposición a clientes aplicando período de riesgo de margen mínimo de 5 días, dado que período de liquidación (close-out) para operaciones compensa
  - `e17` Obligacion: Utilización EAD reducida — cálculo CVA — La EAD reducida debe utilizarse también para cálculo del ajuste de valuación de crédito (CVA) del punto 4.2.3.
  - `e18` Potestad: Reconocimiento garantía — tramo CCP-miembro y miembro-cliente — Miembro compensador puede reconocer garantía recibida de cliente y transferida a CCP tanto para tramo CCP-miembro compensador como para tramo miembro compensador-cliente.
  - `e19` Obligacion: Mitigación exposición — margen inicial de clientes — El margen inicial aportado por clientes al miembro compensador mitiga su exposición respecto de sus clientes.
  - `e20` Obligacion: Aplicación idéntico tratamiento — estructuras multinivel de clientes — Idéntico tratamiento de garantía se aplica a estructuras multinivel de clientes (entre clientes de nivel superior e inferior).
  - `e21` Operacion: Exposiciones de clientes — transacción con miembro compensador como intermediario — Transacción realizada por cliente de miembro compensador donde miembro compensador actúa como intermediario financiero (realiza transacción con CCP por indicación del cliente).
  - `e22` Potestad: Tratamiento exposición cliente — condiciones de protección cumplidas — Exposición de cliente hacia miembro compensador puede recibir tratamiento del acápite i) si se cumplen condiciones de protección especificadas.
  - `e23` Condicion: Condición — identificación de transacciones y protección de garantías — CCP identifica transacciones como transacciones de clientes y garantías son mantenidas bajo acuerdos que impiden pérdidas del cliente por: (i) falta de pago/insolvencia del miembro compensador; (ii) f
  - `e24` Obligacion: Transferencia de garantía — ausencia de impedimentos legales — En caso de impago o insolvencia del miembro compensador, no habrá impedimentos legales (salvo orden judicial a la que cliente tiene derecho) para transferir garantía de clientes a CCP, otro miembro co
  - `e25` Obligacion: Revisión legal adecuada — acuerdos de protección de garantías — Cliente debe haber realizado revisión legal adecuada (y llevarla a cabo cuando sea necesario para asegurar aplicabilidad continua) y contar con fundamentos para concluir que acuerdos serán legales, vá
  - `e26` Condicion: Condición — portabilidad de transacciones y transferencia a valor de mercado — Leyes, regulaciones y acuerdos hacen altamente probable la portabilidad de transacciones: transacciones compensadoras del miembro en impago/insolvencia serán concluidas por CCP; posiciones y garantías
  - `e27` Obligacion: Cumplimiento idénticas condiciones — exposición de cliente con CCP y estructuras multinivel — Idénticas condiciones deben cumplirse para tratamiento de exposición de cliente con CCP (cuando cumplimiento garantizado por miembro compensador) y para exposiciones de clientes de nivel inferior con 
  - `e28` Restriccion: Ponderador 4% — cliente sin protección contra insolvencia conjunta — Cuando cliente no está protegido contra pérdidas por falta de pago/insolvencia conjunta del miembro compensador y alguno de sus clientes, pero se cumplen otras condiciones, exposición recibe ponderado
  - `e29` Obligacion: Tratamiento como operación bilateral — cliente sin cumplimiento de requisitos — Cuando cliente no cumple requisitos de protección, exposición con miembro compensador (incluyendo exposición potencial CVA) debe tratarse como operación bilateral.
  - `e30` Operacion: Tratamiento de garantías — activos constituidos en garantía de operaciones — Tratamiento de activos constituidos en garantía de operaciones con CCP.
  - `e31` Obligacion: Aplicación ponderador según cartera — activos en garantía — Activo constituido en garantía recibe ponderador según normas, considerando qué tratamiento (cartera de negociación o inversión) hubiera recibido si no hubiera sido depositado en CCP.
  - `e32` Restriccion: Riesgo de crédito de contraparte — garantías no protegidas contra quiebra — Cuando activos se coloquen en garantía sin protección contra quiebra de CCP o miembro compensador, entidad financiera debe reconocer riesgo de crédito por posibilidad de pérdidas por calidad creditici
  - `e33` Obligacion: Sujeción a requisito SA-CCR — activos en garantía — Activos constituidos en garantía están sujetos al requisito de riesgo de crédito de contraparte (SA-CCR) del punto 4.2, incluyendo incremento por aforos del punto 5.3.2.3, computados conforme acápite 
  - `e34` Restriccion: Ponderador 2% — garantías incluidas en exposición por operaciones (CCP) — Cuando CCP recibe activos en garantía, se aplica ponderador del 2% a garantías incluidas en definición de exposición por operaciones.
  - `e35` Obligacion: Aplicación ponderador CCP — garantías para otros fines — Ponderador de riesgo correspondiente a CCP se aplica a activos o garantías aportados para otros fines.
  - `e36` Obligacion: Consideración para NICA — garantía depositada sin protección — Garantía depositada sin protección en caso de quiebra debe considerarse para Monto Neto de Garantía Independiente (NICA) del acápite v) punto 4.2.1.1.
  - `e37` Excepcion: Excepción exigencia de capital — garantía de miembro compensador protegida — Garantía de miembro compensador (efectivo, títulos, otros activos, excesos de márgenes) mantenida por custodio y protegida contra quiebra de CCP no está sujeta a exigencia de capital por riesgo de cré
  - `e38` Definicion: Custodio — definición — Fiduciario o agente que mantiene activos bajo título que no acuerda derechos al custodio ni a sus acreedores y garantiza que no se obstaculizará judicialmente devolución de activos en caso de quiebra 
  - `e39` Excepcion: Excepción exigencia de capital — garantía de cliente protegida — Garantía de cliente mantenida por custodio y protegida contra quiebra de CCP, miembro compensador y otros clientes no está sujeta a exigencia de capital por riesgo de crédito de contraparte.
  - `e40` Restriccion: Ponderador 2% — garantía de cliente mantenida por CCP (condiciones cumplidas) — Si garantía de cliente es mantenida por CCP sin protección contra su quiebra, se aplica ponderador de riesgo del 2% si se cumplen condiciones a) y b) del acápite iii).
  - `e41` Restriccion: Ponderador 4% — garantía de cliente mantenida por CCP (condición anteúltima) — Se aplica ponderador de riesgo del 4% si se da el caso del anteúltimo párrafo del acápite iii) (cliente sin protección contra insolvencia conjunta).
- relaciones del crudo (sin establecida_en ni de sujeto): e6a condicion_de e6; e6b condicion_de e6; e23 condicion_de e22; e26 condicion_de e22
- NODOS A CLASIFICAR:
  - **caso 40** Excepcion `e39`: Excepción exigencia de capital — garantía de cliente protegida | descripcion: Garantía de cliente mantenida por custodio y protegida contra quiebra de CCP, miembro compensador y otros clientes no está sujeta a exigencia de capital por riesgo de crédito de contraparte. | tramo: La garantía constituida por un cliente, mantenida por un custodio y protegida de la quiebra de la CCP y del miembro compensador y sus otros clientes no está sujeta a exigencia de capital por riesgo de crédito de contraparte.
  - **caso 41** Excepcion `e37`: Excepción exigencia de capital — garantía de miembro compensador protegida | descripcion: Garantía de miembro compensador (efectivo, títulos, otros activos, excesos de márgenes) mantenida por custodio y protegida contra quiebra de CCP no está sujeta a exigencia de capital por riesgo de crédito de contraparte (ponderador o EAD = 0). | tramo: La garantía constituida por el miembro compensador –incluyendo efectivo, títulos valores y otros activos constituidos como garantías, así como los excesos a los márgenes inicial o de variación– mantenida por un custodio y protegida de la quiebra de la CCP, no está sujeta a la exigencia de capital por la exposición al riesgo de crédito de contraparte –esto es, el ponderador de riesgo o la EAD es igual a cero–.
  - **caso 85** Excepcion `e6`: Excepción MPOR mínimo 20 días — conjuntos con más de 5.000 operaciones | descripcion: No se aplica el plazo mínimo de 20 días hábiles para cálculo de MPOR en conjuntos de neteo con más de 5.000 operaciones, siempre que no existan disputas pendientes y no contengan garantías ilíquidas u operaciones exóticas. | tramo: No se aplicará el plazo mínimo de veinte días hábiles para el cálculo del período de riesgo de margen (MPOR) de los conjuntos de neteo en los que se verifiquen más de 5.000 operaciones en la medida en que no existan disputas pendientes y que dicho conjunto no contenga garantías ilíquidas u operaciones exóticas.

## Unidad `cap::7.1.1.1` (punto_no_item)
- herencia: [chapeau_seccion S7] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en grupo 1 y grupo 2, conforme a lo previsto en la Sección 2. | [intro 7.1] Se determinará mensualmente por la siguiente expresión: | [intro 7.1] C = BIC x ILM | [intro 7.1] RO | [intro 7.1] Donde:
C : exigencia de capital por riesgo operacional. | [intro 7.1] RO | [intro 7.1] BIC: componente del indicador de negocio, que es el producto del indicador de negocio (BI) | [intro 7.1] por una serie de coeficientes marginales (α), calculado según lo previsto en el punto | [intro 7.1] i | [intro 7.1] 7.1.2. | [intro 7.1] ILM: multiplicador de pérdida interna igual a 1.
Los activos ponderados por riesgo (APR) para el riesgo operacional son iguales a 12,5 veces el
C . | [intro 7.1] RO | [intro 7.1.1] El BI es una aproximación al riesgo operacional a partir de la información de los estados
financieros. Se determinará por la siguiente expresión: | [intro 7.1.1] BI = VA (ILDC + SC + FC + RM ) | [intro 7.1.1] Prom Prom Prom Prom | [intro 7.1.1] ILDC : Componente de intereses, arrendamientos y dividendos. Se determinará por la | [intro 7.1.1] Prom | [intro 7.1.1] siguiente expresión:
Mín. [VA (ingresos por intereses – egresos por intereses);
5% x activos que devengan intereses] + ingresos por dividendos | [intro 7.1.1] SC : Componente de servicios. Se determinará por la siguiente expresión: | [intro 7.1.1] Prom | [intro 7.1.1] Máx. [otros ingresos por operaciones; otros egresos por operaciones] + Máx.
[ingresos por honorarios y comisiones; egresos por honorarios y comisiones] | [intro 7.1.1] FC : Componente financiero. Se determinará por la siguiente expresión: | [intro 7.1.1] Prom | [intro 7.1.1] VA (resultado neto de cartera de negociación) + VA (resultado neto de cartera
de inversión) | [intro 7.1.1] RM : Resultado monetario total | [intro 7.1.1] Prom | [intro 7.1.1] VA: Valor absoluto.
Cada término dentro de los 3 componentes y el resultado monetario debe ser calculado
como el promedio de los valores de los 3 últimos períodos consecutivos de 12 meses an-
teriores al mes en que se efectúa el cálculo, expresados en moneda homogénea al cierre
del período de cálculo de 36 meses: t, t-1 y t-2. Se debe determinar, en primer lugar, el
valor de las partidas netas que correspondan (por ejemplo, ingresos por intereses menos
egresos por intereses) para cada período de
- texto propio: 7.1.1.1. Definición de los componentes del indicador de negocio (BI):
i) Componente de intereses, arrendamientos y dividendos (ILDC).
a) Ingresos por intereses y ajustes por índices: es el total de los intereses y
ajustes generados por los activos financieros y por los arrendamientos fi-
nancieros.
Se incluyen, entre otros:
- Los intereses y ajustes generados por los instrumentos financieros me-
didos a costo amortizado –por ejemplo, los préstamos y adelantos– y a
valor razonable con cambios en otro resultado integral (ORI) y los ingre-
sos generados por los arrendamientos financieros.
- Los intereses de instrumentos financieros derivados contabilizados co-
mo coberturas –siempre que sean identificables–.
- Todo otro interés y ajuste generado por un activo.
b) Egresos por intereses: es el total de los intereses y ajustes generados por
los pasivos financieros y los intereses y ajustes correspondientes a los
arrendamientos financieros cuando la entidad sea arrendataria.
Se incluyen, entre otros:
- Los intereses y ajustes generados por los instrumentos financieros me-
didos a costo amortizado –por ejemplo, los depósitos– y a valor razona-
ble con cambios en otro resultado integral (ORI) y los egresos genera-
dos por los arrendamientos financieros.
- Los intereses de instrumentos financieros derivados contabilizados co-
mo coberturas –siempre que sean identificables–.
- Todo otro interés y ajuste generado por un pasivo.
c) Activos que devengan intereses: importe bruto al cierre del mes anterior al
que se efectúa el cálculo para cada uno de los 3 años del total de los acti-
vos a tasa de interés o ajustes asimilables –aunque estuvieran en mora y
se hubiera suspendido el devengamiento de los accesorios– y de los acti-
vos dados en arrendamiento financiero. No se computan las 
- entidades de la unidad:
  - `e1` Definicion: ILDC — Componente de intereses, arrendamientos y dividendos — Comprende: (a) ingresos por intereses y ajustes generados por activos financieros y arrendamientos financieros, incluyendo instrumentos a costo amortizado, a valor razonable con cambios en ORI, deriva
  - `e2` Definicion: SC — Componente de servicios — Comprende: (a) ingresos por honorarios y comisiones: ingresos por asesoramiento y prestación de servicios, incluso a través de terceros, incluyendo servicios por cuenta de clientes relacionados con em
  - `e3` Definicion: FC — Componente financiero — Comprende: (a) resultado neto de la cartera de negociación (conforme a lo establecido en punto 6.1.2), conformado por el resultado neto de activos y pasivos mantenidos para negociación (títulos de deu
  - `e4` Definicion: RM — Resultado monetario total — Resultado monetario total, no medido en valores absolutos.
  - `e5` Restriccion: Exclusión — Negocios de seguros o reaseguros — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: ingresos y gastos de negocios de seguros o reaseguros, que se realizan en carácter de agente institorio o a través de subsidiar
  - `e6` Restriccion: Exclusión — Pago de pólizas y cobro de indemnizaciones — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: pago de pólizas y cobro de indemnizaciones por las coberturas de seguros o reaseguros.
  - `e7` Restriccion: Exclusión — Gastos administrativos — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: gastos administrativos, incluidos gastos de personal, comisiones pagadas por la contratación externa de servicios no financiero
  - `e8` Restriccion: Exclusión — Recupero de gastos administrativos — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: recupero de gastos administrativos, incluido el recupero de pagos efectuados por cuenta de clientes (tales como impuestos pagad
  - `e9` Restriccion: Exclusión — Gastos en inmuebles y activos fijos — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: gastos en inmuebles y otros activos fijos, excepto los derivados de eventos de pérdida por riesgo operacional.
  - `e10` Excepcion: Excepción — Gastos en inmuebles por pérdida operacional — Gastos en inmuebles y otros activos fijos derivados de eventos de pérdida por riesgo operacional sí contribuyen a las partidas del BI.
  - `e11` Restriccion: Exclusión — Depreciación o amortización — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: depreciación o amortización de activos tangibles e intangibles.
  - `e12` Restriccion: Exclusión — Provisiones por compromisos — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: provisiones por compromisos asumidos o sus reversiones, salvo provisiones relacionadas con eventos de pérdidas por riesgo opera
  - `e13` Excepcion: Excepción — Provisiones por riesgo operacional — Provisiones relacionadas con eventos de pérdidas por riesgo operacional sí contribuyen a las partidas del BI.
  - `e14` Restriccion: Exclusión — Deterioro de activos — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: deterioro del valor de activos financieros y no financieros o sus reversiones, inversiones en subsidiarias, joint ventures o as
  - `e15` Restriccion: Exclusión — Cambios en llave de negocios — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: cambios en la llave de negocios reconocidos en resultados.
  - `e16` Restriccion: Exclusión — Impuesto a las ganancias — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: impuesto a las ganancias corriente y diferido.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 42** Excepcion `e10`: Excepción — Gastos en inmuebles por pérdida operacional | descripcion: Gastos en inmuebles y otros activos fijos derivados de eventos de pérdida por riesgo operacional sí contribuyen a las partidas del BI. | tramo: excepto los derivados de eventos de pérdida por riesgo operacional
  - **caso 105** Excepcion `e13`: Excepción — Provisiones por riesgo operacional | descripcion: Provisiones relacionadas con eventos de pérdidas por riesgo operacional sí contribuyen a las partidas del BI. | tramo: salvo provisiones relacionadas con eventos de pérdidas por riesgo operacional

## Unidad `cap::8.3.2.7` (punto_no_item)
- herencia: [intro 8.3.2] n1
- texto propio: 8.3.2.7. Discrecionalidad en el pago de dividendos/cupones de interés:
i) la entidad financiera podrá –en todo momento y a su entera discreción–
cancelar pagos en concepto de dividendos o intereses;
ii) lo señalado en el acápite anterior no deberá constituir de por sí un incum-
plimiento, ni facultar a los tenedores a exigir la conversión en acciones or-
dinarias. Asimismo, no debe imponer restricciones a la entidad financiera,
salvo en relación con las distribuciones de dividendos a los titulares de ac-
ciones ordinarias.
- entidades de la unidad:
  - `e1` Potestad: Cancelación discrecional de dividendos/intereses — La entidad financiera tiene la facultad de cancelar en todo momento y a su entera discreción los pagos en concepto de dividendos o intereses.
  - `e2` Excepcion: No constituye incumplimiento — cancelación de dividendos/intereses — La cancelación discrecional de dividendos o intereses no constituye por sí sola un incumplimiento de los requisitos de los instrumentos incluidos en el CA.
  - `e3` Excepcion: No faculta conversión en acciones ordinarias — cancelación de dividendos/intereses — La cancelación discrecional de dividendos o intereses no faculta a los tenedores a exigir la conversión en acciones ordinarias.
  - `e4` Restriccion: Límite cualitativo — restricciones a distribuciones de dividendos ordinarios — La cancelación discrecional de dividendos o intereses no debe imponer restricciones a la entidad financiera, excepto en relación con las distribuciones de dividendos a los titulares de acciones ordina
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 43** Excepcion `e2`: No constituye incumplimiento — cancelación de dividendos/intereses | descripcion: La cancelación discrecional de dividendos o intereses no constituye por sí sola un incumplimiento de los requisitos de los instrumentos incluidos en el CA. | tramo: lo señalado en el acápite anterior no deberá constituir de por sí un incumplimiento
  - **caso 44** Excepcion `e3`: No faculta conversión en acciones ordinarias — cancelación de dividendos/intereses | descripcion: La cancelación discrecional de dividendos o intereses no faculta a los tenedores a exigir la conversión en acciones ordinarias. | tramo: facultar a los tenedores a exigir la conversión en acciones or-
dinarias. Asimismo, no

## Unidad `ext::9.2` (punto_no_item)
- herencia: [encabezado S9] Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.
- texto propio: 9.2. Entidad nominada por el exportador.
Por cada operación comprendida el exportador deberá seleccionar una entidad como
responsable de su seguimiento.
Esta entidad será la única responsable de emitir los certificados de aplicación que habilitan
que los cobros de exportaciones puedan ser imputados a los permisos correspondientes.
En el caso de financiaciones otorgadas por entidades financieras locales, el seguimiento
estará a cargo de la entidad que otorgó la financiación hasta su cancelación total.
Para las operaciones comprendidas en los puntos 9.1.6. y 9.1.7. el seguimiento quedará a
cargo de la entidad nominada en cumplimiento a lo establecido en los puntos 7.9. o 7.10.
En el caso de las operaciones comprendidas en el punto 9.1.8. el seguimiento quedará a
cargo de la entidad que, a pedido del exportador y luego de verificar el cumplimiento de los
requisitos previstos en el punto 7.11., realizó el registro de la operación ante el BCRA.
En los restantes casos, el seguimiento quedará inicialmente a cargo de la entidad que dé
curso a la liquidación por el mercado de cambios, pudiendo el exportador modificarla
posteriormente en la medida que no se hayan registrado aplicaciones de divisas a la
cancelación de ésta.
En caso de que el exportador solicite el cambio, la entidad a cargo del seguimiento deberá
notificarle la voluntad del exportador a la nueva entidad. La constancia de aceptación por
parte de esta última liberará a la entidad previa de sus obligaciones hacia adelante.
- entidades de la unidad:
  - `e1` Operacion: Selección de entidad responsable de seguimiento — El exportador debe seleccionar una entidad como responsable del seguimiento de cada operación comprendida en la sección 9.
  - `e2` Obligacion: Emisión de certificados de aplicación — La entidad nominada es la única responsable de emitir los certificados de aplicación que habilitan que los cobros de exportaciones puedan ser imputados a los permisos correspondientes.
  - `e3` Obligacion: Seguimiento a cargo de entidad financiera otorgante — Cuando la financiación es otorgada por entidades financieras locales, el seguimiento estará a cargo de la entidad que otorgó la financiación hasta su cancelación total.
  - `e4` Obligacion: Seguimiento según puntos 7.9 o 7.10 — Para las operaciones comprendidas en los puntos 9.1.6 y 9.1.7, el seguimiento quedará a cargo de la entidad nominada en cumplimiento a lo establecido en los puntos 7.9 o 7.10.
  - `e5` Obligacion: Seguimiento a cargo de entidad registrante — Para las operaciones comprendidas en el punto 9.1.8, el seguimiento quedará a cargo de la entidad que, a pedido del exportador y luego de verificar el cumplimiento de los requisitos previstos en el pu
  - `e6` Obligacion: Seguimiento inicial a cargo de entidad liquidadora — En los restantes casos, el seguimiento quedará inicialmente a cargo de la entidad que dé curso a la liquidación por el mercado de cambios.
  - `e7` Potestad: Modificación de entidad responsable por exportador — El exportador puede modificar la entidad responsable del seguimiento posteriormente, siempre que no se hayan registrado aplicaciones de divisas a la cancelación de la operación.
  - `e8` Obligacion: Notificación de cambio de entidad — Cuando el exportador solicita cambiar la entidad responsable del seguimiento, la entidad actual debe notificar la voluntad del exportador a la nueva entidad.
  - `e9` Excepcion: Liberación de obligaciones por aceptación — La constancia de aceptación de la nueva entidad libera a la entidad previa de sus obligaciones hacia adelante.
  - `e10` Condicion: Condición: no se hayan registrado aplicaciones de divisas — La modificación de la entidad responsable solo es posible si no se han registrado aplicaciones de divisas a la cancelación de la operación.
- relaciones del crudo (sin establecida_en ni de sujeto): e10 condicion_de e7
- NODOS A CLASIFICAR:
  - **caso 45** Excepcion `e9`: Liberación de obligaciones por aceptación | descripcion: La constancia de aceptación de la nueva entidad libera a la entidad previa de sus obligaciones hacia adelante. | tramo: La constancia de aceptación por parte de esta última liberará a la entidad previa de sus obligaciones hacia adelante

## Unidad `pagjub::1.5` (punto_no_item)
- herencia: [encabezado S1] Sección 1. Disposiciones generales.
- texto propio: 1.5. Delegación de funciones.
Los responsables de la rendición de cuentas de este sistema de pagos podrán, a su vez, dele-
gar en terceros dicha presentación, así como la suscripción de la correspondiente declaración
jurada.
Con tal propósito deberán dirigir una nota a la Gerencia de Cuentas Corrientes del BCRA, sus-
cripta por los funcionarios responsables designados conforme a la metodología del punto 1.4.,
procediendo a la delegación correspondiente, haciendo explícitos los apellidos y nombres, tipo
y N° de documento de identidad de cada uno de los delegados y acompañando el registro de
las pertinentes firmas (Fórm. 2570, integrada bajo las modalidades de práctica).
Esta delegación será válida sólo a los efectos operativos del presente régimen, sin perjuicio de
las responsabilidades que les caben a los funcionarios designados por las entidades participan-
tes conforme a lo establecido en el punto 1.4.
- entidades de la unidad:
  - `e1` Potestad: Delegación de funciones de rendición de cuentas — Los responsables de la rendición de cuentas podrán delegar en terceros la presentación y la suscripción de la declaración jurada.
  - `e2` Obligacion: Notificación a Gerencia de Cuentas Corrientes del BCRA — Deber de dirigir una nota a la Gerencia de Cuentas Corrientes del BCRA, suscripta por los funcionarios responsables designados conforme al punto 1.4, con los datos de los delegados (apellidos, nombres
  - `e3` Restriccion: Validez limitada a efectos operativos del régimen — La delegación es válida solo a los efectos operativos del presente régimen, sin perjuicio de las responsabilidades de los funcionarios designados.
  - `e4` Excepcion: Excepción de responsabilidades de funcionarios designados — La delegación no exime de responsabilidades a los funcionarios designados por las entidades participantes conforme al punto 1.4.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 46** Excepcion `e4`: Excepción de responsabilidades de funcionarios designados | descripcion: La delegación no exime de responsabilidades a los funcionarios designados por las entidades participantes conforme al punto 1.4. | tramo: sin perjuicio de las responsabilidades que les caben a los funcionarios designados por las entidades participantes conforme a lo establecido en el punto 1.4.

## Unidad `lingob::6.2.2.4` (item)
- herencia: **[abre la lista]** [intro 6.2.2] Las entidades financieras con una significativa dimensión, complejidad, importancia
económica y perfil de riesgo -considerando el grupo económico al cual pertenezcan-
deben tener un Comité a nivel del Directorio que vigile el diseño del sistema de incenti-
vos económicos al personal y su implementación, el cual debe reunir las siguientes ca-
racterísticas:
- texto propio: 6.2.2.4. Asegurar que se lleve a cabo una evaluación anual del sistema de incentivos
económicos al personal -la que puede ser encargada a un organismo externo-,
conducida en forma independiente de la Alta Gerencia de la entidad y puesta a
disposición de la Superintendencia de Entidades Financieras y Cambiarias.
- entidades de la unidad:
  - `e1` Obligacion: Evaluación anual del sistema de incentivos — Las entidades financieras con significativa dimensión, complejidad, importancia económica y perfil de riesgo deben asegurar que se lleve a cabo una evaluación anual del sistema de incentivos económico
  - `e2` Condicion: Evaluación conducida independientemente de Alta Gerencia — La evaluación debe ser conducida en forma independiente de la Alta Gerencia de la entidad
  - `e3` Obligacion: Puesta a disposición de la Superintendencia — La evaluación anual del sistema de incentivos debe ser puesta a disposición de la Superintendencia de Entidades Financieras y Cambiarias
  - `e4` Excepcion: Encargo a organismo externo — evaluación anual — La evaluación anual del sistema de incentivos económicos al personal puede ser encargada a un organismo externo, en lugar de ser realizada internamente
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 47** Excepcion `e4`: Encargo a organismo externo — evaluación anual | descripcion: La evaluación anual del sistema de incentivos económicos al personal puede ser encargada a un organismo externo, en lugar de ser realizada internamente | tramo: la que puede ser encargada a un organismo externo

## Unidad `ext::8.5.17.12` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.12. Régimen de exportación en consignación (mientras permanezca dentro
del régimen, según el Decreto 637/79).
- entidades de la unidad:
  - `e1` Operacion: Exportación en consignación — Exportación de bienes bajo régimen de consignación, mientras permanezca dentro del régimen conforme al Decreto 637/79
  - `e2` Excepcion: Excepción seguimiento — exportación en consignación — La exportación en consignación queda exceptuada del seguimiento de divisas por exportaciones de bienes, por el valor que corresponda a esta operación aduanera
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 48** Excepcion `e2`: Excepción seguimiento — exportación en consignación | descripcion: La exportación en consignación queda exceptuada del seguimiento de divisas por exportaciones de bienes, por el valor que corresponda a esta operación aduanera | tramo: Régimen de exportación en consignación (mientras permanezca dentro del régimen, según el Decreto 637/79)

## Unidad `ctacte::10.1` (punto_no_item)
- herencia: [encabezado S10] Sección 10. Avisos.
- texto propio: 10.1. Aspectos generales.
Los avisos que, en cumplimiento de la Ley de Cheques y de la presente reglamentación, co-
rresponda enviar a los libradores, a los titulares de cuentas corrientes, a los presentantes o
tenedores de cheques, o a los avalistas deberán cursarse, preferentemente mediante la utili-
zación de mecanismos electrónicos de comunicación, dentro de las 48 horas hábiles de pro-
ducida la causa que determine la obligación de envío.
La falta de recepción por parte del librador o del cuentacorrentista de los avisos a que aluden
las presentes normas no enervarán los efectos de las medidas previstas (inclusión en la
“Central de cheques rechazados” y en la “Central de cuentacorrentistas inhabilitados”).
- entidades de la unidad:
  - `e1` Obligacion: Envío de avisos mediante mecanismos electrónicos — Envío de avisos requeridos por la Ley de Cheques y la reglamentación a libradores, titulares de cuentas corrientes, presentantes, tenedores de cheques o avalistas, preferentemente mediante mecanismos 
  - `e2` Excepcion: Falta de recepción no enerva efectos de medidas — La falta de recepción de los avisos por parte del librador o del cuentacorrentista no suspende los efectos de las medidas previstas (inclusión en la Central de cheques rechazados y en la Central de cu
  - `e3` Operacion: Inclusión en Central de cheques rechazados — Inclusión del librador o cuentacorrentista en la Central de cheques rechazados como consecuencia del rechazo de cheques.
  - `e4` Operacion: Inclusión en Central de cuentacorrentistas inhabilitados — Inclusión del cuentacorrentista en la Central de cuentacorrentistas inhabilitados como consecuencia del incumplimiento de obligaciones.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 49** Excepcion `e2`: Falta de recepción no enerva efectos de medidas | descripcion: La falta de recepción de los avisos por parte del librador o del cuentacorrentista no suspende los efectos de las medidas previstas (inclusión en la Central de cheques rechazados y en la Central de cuentacorrentistas inhabilitados). | tramo: La falta de recepción por parte del librador o del cuentacorrentista de los avisos a que aluden las presentes normas no enervarán los efectos de las medidas previstas

## Unidad `cap::3.1.14.1` (punto_no_item)
- herencia: [intro 3.1] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi-
cional o sintética, o a una estructura con similares características.
La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con-
ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de
deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset-
Backed Securities”, ABS) y bonos de tit | [intro 3.1.14] A los fines de establecer el ponderador de riesgo a aplicar de acuerdo con el enfoque
estandarizado –punto 3.1.11.–, una titulización se considerará simple, transparente y
comparable (STC) si:
-se trata de una titulización tradicional que no constituye un programa ABCP;
- involucra una transferencia real de activos –en los términos del acápite v) del punto | [intro 3.1.14] 3.1.14.1.–; y | [intro 3.1.14] - cumple con la totalidad de los criterios previstos en el presente punto (en adelante, | [intro 3.1.14] “criterios STC”). | [intro 3.1.14] El originante/fiduciario deberá divulgar toda la información necesaria respecto de la
transacción que permita a los inversores determinar si la titulización cumple con los cri-
terios STC. En base a la información provista, el inversor deberá realizar sus propias
evaluaciones respecto del cumplimiento de estos criterios previo a la aplicación del en-
foque estandarizado.
Para las posiciones retenidas en las que el originante haya transferido el riesgo de
acuerdo con lo establecido en los puntos 
- texto propio: 3.1.14.1. Riesgo de los activos subyacentes.
i) Naturaleza de los activos.
Los activos subyacentes deberán estar constituidos por documentos a
cobrar o derechos de crédito de carácter homogéneo en cuanto a su tipo,
jurisdicción, legislación aplicable y moneda y sus flujos de fondos deberán
estar contractualmente identificados, ser periódicos y consistir exclusiva-
mente en pagos del principal e intereses o de arrendamientos financieros.
La homogeneidad de los activos subyacentes deberá evaluarse teniendo
en consideración los siguientes principios:
a) La naturaleza de los activos deberá ser tal que los inversores, al reali-
zar el proceso de debida diligencia, no necesiten analizar ni evaluar
perfiles o factores de riesgo, crediticios o legales, sustancialmente dife-
rentes entre sí.
b) La homogeneidad se deberá evaluar en función de factores y perfiles
de riesgo comunes al conjunto de los activos.
c) Los documentos y créditos incluidos en la titulización deberán constituir
obligaciones estándares, en términos de derechos de cobro y/o rentas
de los activos y generar un flujo de pago a los inversores periódico y
claramente definido –tal como el flujo que generan las facilidades que
proveen las tarjetas de crédito–.
d) El reembolso a los inversores en la titulización deberá provenir princi-
palmente del producido de los activos subyacentes y no deberá de-
pender de modo sustancial de la refinanciación de los créditos. Se po-
drá contar con la refinanciación o venta de los subyacentes siempre
que las operaciones a refinanciar estén suficientemente distribuidas en
el conjunto de los activos titulizados y que sus valores residuales no
sean significativos.
Las tasas de interés o de descuento de referencia deberán ser tasas de
interés de mercado y de fácil consulta –tales como 
- entidades de la unidad:
  - `e1` Obligacion: Homogeneidad de activos subyacentes — Los activos subyacentes deben ser homogéneos en tipo, jurisdicción, legislación aplicable y moneda. La homogeneidad se evalúa considerando que los inversores no necesiten analizar perfiles o factores 
  - `e2` Obligacion: Flujos de fondos contractualmente identificados — Los flujos de fondos de los activos subyacentes deben estar contractualmente identificados, ser periódicos y consistir exclusivamente en pagos del principal e intereses o de arrendamientos financieros
  - `e3` Obligacion: Reembolso a inversores desde activos subyacentes — El reembolso a los inversores debe provenir principalmente del producido de los activos subyacentes y no debe depender sustancialmente de la refinanciación de los créditos. Se puede contar con refinan
  - `e4` Obligacion: Tasas de interés de mercado y fácil consulta — Las tasas de interés o de descuento de referencia deben ser tasas de mercado y de fácil consulta, tales como tasas interbancarias, tasas establecidas por el BCRA o tasas sectoriales que reflejen el co
  - `e5` Obligacion: Información verificable sobre pérdidas e incumplimientos — Debe contarse con información verificable sobre pérdidas e incumplimientos de activos con características de riesgo sustancialmente similares a los de la titulización durante un período suficientement
  - `e6` Obligacion: Disponibilidad de fuentes de información y acceso a datos — Las fuentes de información, el acceso a los datos y los fundamentos que demuestren la similitud con los activos titulizados deben estar disponibles para todos los participantes del mercado.
  - `e7` Obligacion: Experiencia del originante en financiaciones similares — El originante de la titulización y el acreedor inicial de los créditos titulizados deben contar con experiencia suficiente en el otorgamiento de financiaciones similares a las titulizadas.
  - `e8` Condicion: Desempeño verificado mínimo 5 años exposiciones minoristas — Para exposiciones minoristas que se ajusten a la definición del punto 2.8.1 (sin exclusiones) y cumplan el criterio del punto 2.8.3.1, el desempeño del originante y acreedor inicial debe verificarse d
  - `e9` Condicion: Desempeño verificado 7 años resto de exposiciones — Para exposiciones distintas a las minoristas del punto 2.8.1, el desempeño del originante y acreedor inicial debe verificarse durante 7 años, para evitar que se originen carteras con el solo fin de tr
  - `e10` Restriccion: Prohibición de transferencia de activos en mora — No se pueden transferir activos en situación de incumplimiento o mora, ni obligaciones respecto de las cuales haya evidencia de incremento sustancial en pérdidas esperadas o que se encuentren en gesti
  - `e11` Obligacion: Verificación de no quiebra en 3 años previos — El obligado al pago no debe haber sido sometido a proceso de quiebra o reestructuración de deuda por dificultades financieras en los 3 años previos a la originación, salvo aplicación del período de 2 
  - `e12` Obligacion: Verificación de historial de crédito favorable — El obligado al pago no debe contar con historial de crédito desfavorable en algún registro público de crédito.
  - `e13` Obligacion: Verificación de evaluación de riesgo de incumplimiento — El obligado al pago no debe contar con evaluación de agencia de calificación de créditos o credit scoring que anticipen riesgo de incumplimiento significativo.
  - `e14` Obligacion: Verificación de ausencia de litigios — El documento a cobrar o derecho de crédito transferido no debe ser objeto de litigios entre el obligado y el acreedor original.
  - `e15` Condicion: Análisis de condiciones dentro de 45 días previos — El análisis de las condiciones de cumplimiento debe realizarse dentro de los 45 días previos a la transferencia de activos, sin evidencia de deterioro en el estado de cumplimiento.
  - `e16` Obligacion: Registro de al menos un pago previo a inclusión — Al momento de inclusión del activo en la cartera de subyacentes debe haberse registrado al menos un pago, excepto para estructuras sobre activos rotativos como tarjetas de crédito, facturas y otras ex
  - `e17` Obligacion: Demostración de estándares de originación uniformes — El originante debe demostrar al inversor que los activos transferidos fueron generados en el curso normal de su negocio bajo estándares de originación uniformes y consistentes.
  - `e18` Obligacion: Comunicación de cambios en estándares de originación — Cuando los estándares de originación se vean afectados por cambios, el originante debe comunicar el momento y propósito de las modificaciones.
  - `e19` Restriccion: Estándares no menos rigurosos que activos retenidos — Los estándares de originación no deben ser menos rigurosos que aquellos aplicados a los activos retenidos por el originante.
  - `e20` Obligacion: Criterios de originación sólidos y prudentes — Los documentos a cobrar o derechos de crédito titulizados deben satisfacer criterios de originación sólidos y prudentes que incluyan evaluación de la capacidad e intención de los obligados de cumplir 
  - `e21` Obligacion: Originación en curso normal del negocio carteras atomizadas — Para carteras atomizadas, los documentos o derechos deben originarse en el curso normal del negocio del originante y sus flujos de fondos esperados deben permitir atender las obligaciones de la tituli
  - `e22` Obligacion: Revisión de estándares de originación de terceros — Cuando los activos sean adquiridos a terceros, el originante/fiduciario debe revisar los estándares de originación de esos terceros (verificando existencia y calidad) y constatar que el acreedor origi
  - `e23` Restriccion: Prohibición de gestión activa y discrecional de cartera — El desempeño de la titulización no debe depender de selección de subyacentes mediante gestión activa y discrecional de la cartera.
  - `e24` Obligacion: Selección de activos sujeta a criterios de elegibilidad — La selección de activos debe estar sujeta a criterios de elegibilidad claramente definidos, tales como tamaño de la obligación, edad del sujeto de crédito y ratios LTV, DTI y/o DSC.
  - `e25` Excepcion: Excepción gestión activa incorporación en períodos de rotación — La incorporación de créditos en períodos de rotación o su sustitución/recompra por incumplimiento de cláusulas contractuales no se considera gestión activa de la cartera cuando la selección no es disc
  - `e26` Restriccion: Prohibición de selección discrecional post-titulización — Los documentos a cobrar y créditos transferidos después de la fecha de concreción de la titulización no deben ser seleccionados de manera discrecional ni gestionados de forma activa.
  - `e27` Obligacion: Cesión efectiva de derechos de crédito — Debe realizarse cesión efectiva de derechos para cumplir con transferencia real: (a) documentos constituyan deuda de obligados conste en cláusulas; (b) estén fuera del alcance del cedente, acreedores 
  - `e28` Obligacion: Garantía de no afectación de activos en cesión — El contrato de cesión debe contener cláusulas por las cuales el originante garantice que los documentos a cobrar o créditos transferidos no están afectados en garantía ni sujetos a condición o gravame
  - `e29` Obligacion: Opinión legal independiente sobre transferencia real — La documentación de la titulización debe incluir opinión legal independiente que respalde que la transferencia real y cesión de derechos bajo legislación aplicable se ajustan a los requisitos de cesió
  - `e30` Obligacion: Demostración de obstáculos legales y métodos de ejercicio de derechos — Si la legislación aplicable no se ajusta a los requisitos de cesión efectiva, debe demostrarse la existencia de obstáculos e informarse el método disponible para que inversores ejerzan derechos contra
  - `e31` Obligacion: Información de condiciones que retrasen transferencia de activos — Debe informarse toda condición o evento que pueda retrasar o impedir la transferencia de activos subyacentes a la titulización, así como cualquier factor que afecte el perfeccionamiento oportuno de re
  - `e32` Obligacion: Información inicial a nivel de préstamo o características de riesgo — Debe contarse con suficiente información a nivel de cada préstamo o, para carteras atomizadas, datos sobre características de riesgo relevantes resumidas a nivel de cada tramo de activos subyacentes, 
  - `e33` Obligacion: Información periódica trimestral durante vida de titulización — Debe suministrarse al menos trimestralmente durante la vida de la titulización datos a nivel de préstamos o, para carteras atomizadas, datos resumidos a nivel de cada tramo de activos subyacentes, así
  - `e34` Condicion: Fechas de corte de datos alineadas con emisión de informes — Las fechas de corte de los datos deben estar alineadas con las utilizadas para la emisión de los informes.
  - `e35` Obligacion: Revisión de cartera inicial por contador público independiente — La cartera inicial debe ser revisada por un contador público independiente para generar confianza respecto de la exactitud de la información sobre activos subyacentes y del cumplimiento de requisitos 
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 50** Excepcion `e25`: Excepción gestión activa incorporación en períodos de rotación | descripcion: La incorporación de créditos en períodos de rotación o su sustitución/recompra por incumplimiento de cláusulas contractuales no se considera gestión activa de la cartera cuando la selección no es discrecional. | tramo: En la medida en que la selección no sea discrecional, la incorporación de créditos en los períodos de rotación o su sustitución o recompra debido al incumplimiento de cláusulas contractuales no se considerará una gestión activa de la cartera
  - **caso 135** Condicion `e15`: Análisis de condiciones dentro de 45 días previos | descripcion: El análisis de las condiciones de cumplimiento debe realizarse dentro de los 45 días previos a la transferencia de activos, sin evidencia de deterioro en el estado de cumplimiento. | tramo: El análisis de estas condiciones deberá ser llevado a cabo por el originante o fiduciario dentro de los 45 días previos a la fecha de la transferencia de los activos
  - **caso 175** Condicion `e9`: Desempeño verificado 7 años resto de exposiciones | descripcion: Para exposiciones distintas a las minoristas del punto 2.8.1, el desempeño del originante y acreedor inicial debe verificarse durante 7 años, para evitar que se originen carteras con el solo fin de transferirlas. | tramo: Para el resto de las exposiciones, el desempeño deberá verificarse durante 7 años
  - **caso 176** Condicion `e8`: Desempeño verificado mínimo 5 años exposiciones minoristas | descripcion: Para exposiciones minoristas que se ajusten a la definición del punto 2.8.1 (sin exclusiones) y cumplan el criterio del punto 2.8.3.1, el desempeño del originante y acreedor inicial debe verificarse durante un período mínimo de 5 años. | tramo: El desempeño se deberá verificar durante un período mínimo de 5 años en el caso de las exposiciones minoristas que se ajusten a la definición prevista en el punto 2.8.1. –sin considerar las exclusiones allí previstas– y que cumplan con el criterio previsto en el punto 2.8.3.1.
  - **caso 189** Condicion `e34`: Fechas de corte de datos alineadas con emisión de informes | descripcion: Las fechas de corte de los datos deben estar alineadas con las utilizadas para la emisión de los informes. | tramo: Las fechas de corte de los datos deberán estar en línea con las utilizadas para la emisión de los informes
