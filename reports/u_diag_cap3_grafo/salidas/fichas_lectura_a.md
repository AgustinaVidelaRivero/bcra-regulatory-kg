# Fichas de lectura de la tarea a (U-DIAG-CAP3-GRAFO)

255 casos, en el orden de `casos_a.json` (tipo, id). Criterio: `criterio_lectura_a.md`.

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

## Unidad `ext::5.13` (punto_no_item)
- herencia: [encabezado S5] Sección 5. Pautas operativas.
- texto propio: 5.13. Operaciones que impliquen importación y/o exportación de moneda nacional.
Las entidades podrán concretar operaciones de cambio que impliquen la importación y/o
exportación de monedas y billetes de pesos argentinos siempre que la contraparte sea alguna
de las previstas en el punto 5.12. Las operaciones que impliquen la importación de billetes de
pesos argentinos quedarán también sujetas a las disposiciones establecidas para la compra
de moneda extranjera por parte de no residentes.
La liquidación de las divisas remitidas a la entidad local por la contraparte para la adquisición
de billetes en moneda local estará exceptuada de lo dispuesto en el primer párrafo del punto
2.9. en la medida que exista un compromiso de la contraparte respecto a que dichos fondos
serán comercializados con el objeto de atender la demanda de turismo y viajes y la
exportación se realice en un plazo no mayor a los 30 (treinta) días corridos de la fecha de
concertación de cambio.
- entidades de la unidad:
  - `e1` Operacion: Importación y/o exportación de moneda nacional — Operaciones de cambio que impliquen la importación y/o exportación de monedas y billetes de pesos argentinos
  - `e2` Condicion: Contraparte prevista en punto 5.12 — La contraparte debe ser alguna de las previstas en el punto 5.12
  - `e3` Restriccion: Importación de billetes pesos — sujeta a disposiciones compra moneda extranjera no residentes — Las operaciones que impliquen la importación de billetes de pesos argentinos quedan sujetas a las disposiciones establecidas para la compra de moneda extranjera por parte de no residentes
  - `e4` Excepcion: Liquidación divisas remitidas — exceptuada punto 2.9 primer párrafo — La liquidación de las divisas remitidas a la entidad local por la contraparte para la adquisición de billetes en moneda local queda exceptuada de lo dispuesto en el primer párrafo del punto 2.9
  - `e5` Condicion: Compromiso contraparte — fondos para turismo y viajes — Debe existir un compromiso de la contraparte de que los fondos serán comercializados para atender la demanda de turismo y viajes
  - `e6` Condicion: Plazo exportación — no mayor a 30 días corridos — La exportación debe realizarse en un plazo no mayor a 30 días corridos desde la fecha de concertación de cambio
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1; e5 condicion_de e4; e6 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 51** Excepcion `e4`: Liquidación divisas remitidas — exceptuada punto 2.9 primer párrafo | descripcion: La liquidación de las divisas remitidas a la entidad local por la contraparte para la adquisición de billetes en moneda local queda exceptuada de lo dispuesto en el primer párrafo del punto 2.9 | tramo: La liquidación de las divisas remitidas a la entidad local por la contraparte para la adquisición de billetes en moneda local estará exceptuada de lo dispuesto en el primer párrafo del punto 2.9

## Unidad `ext::3.16.3::intersticial` (intersticial)
- herencia: [encabezado 3.16.3] 3.16.3. Declaración jurada de clientes que no sean personas humanas residentes respecto a
- texto propio: En caso de que el cliente sea una persona jurídica, para que la operación no quede
comprendida por el requisito de conformidad previa, la entidad deberá contar
adicionalmente con una declaración jurada en la que conste:
- entidades de la unidad:
  - `e1` Condicion: Cliente es persona jurídica — El cliente es una persona jurídica
  - `e2` Excepcion: Excepción conformidad previa — persona jurídica — La operación no queda comprendida por el requisito de conformidad previa cuando se cumplen las condiciones de esta salvedad
  - `e3` Obligacion: Contar con declaración jurada — cliente persona jurídica — La entidad debe contar con una declaración jurada en la que conste la información requerida
- relaciones del crudo (sin establecida_en ni de sujeto): e1 condicion_de e3
- NODOS A CLASIFICAR:
  - **caso 52** Excepcion `e2`: Excepción conformidad previa — persona jurídica | descripcion: La operación no queda comprendida por el requisito de conformidad previa cuando se cumplen las condiciones de esta salvedad | tramo: para que la operación no quede comprendida por el requisito de conformidad previa

## Unidad `cap::4.2.1.2::parte1` (punto_no_item)
- herencia: [intro 4.2] –OTC o negociados en mercados regulados– y con liquidación diferida.
La exigencia computada en este punto –basada en el Enfoque Estándar para la medición de
la exigencia por capital por riesgo de crédito de contraparte (“Standardised Approach for
measuring Counterparty Credit Risk”, SA-CCR)– se aplicará a operaciones con derivados
–OTC o negociados en mercados regulados– y con liquidación diferida, ya que las operacio-
nes de financiación con títulos valores (“Securities Financing Transactions”, | [intro 4.2.1] La exposición al riesgo de crédito de contraparte (EAD) se calculará por separado para
cada conjunto de neteo (“netting set”, NS) y se determinará del siguiente modo:
donde:
α = 1,40.
CR: costo de reposición calculado de acuerdo con el punto 4.2.1.1.
EPF: exposición potencial futura calculado de acuerdo con el punto 4.2.1.2.
El cálculo del CR y de la EPF diferirá según que los conjuntos de neteo estén sujetos o
no al intercambio de márgenes de variación:
− Operaciones sin margen de variación: el | [intro 4.2.1] ante el incumplimiento de la contraparte y la liquidación inmediata de sus opera-
ciones y la EPF adicionará el incremento probable de la exposición, calculado de
modo conservador, en el horizonte temporal de un año a partir de la fecha de
cálculo. | [intro 4.2.1] − Operaciones con margen de variación: el CR representa la pérdida que ocurriría | [intro 4.2.1] ante el incumplimiento de la contraparte –en el presente o en el futuro– si la liqui-
dación y reposición de las operaciones fueran instantáneas. Dado que puede ha-
ber un lapso –período de riesgo de margen (“MPOR”)– entre el último intercambio
de garantías antes del incumplimiento y la reposición, el adicional por la EPF re-
presenta el potencial cambio de valor de las operaciones durante ese período. | [intro 4.2.1] En ambos casos, y a los efectos de determinar el costo de reposición, el aforo de los
activos recibidos en garantía (excepto efectivo) representará el cambio potencial del
valor de dicha garantía durante el período relevante –un año, para las operaciones sin
márgenes, y el período de riesgo de margen, para las operaciones con márgenes–.
Además:
− La EAD para un conjunto de neteo con márgenes de variación tendrá como límite | [intro 4.2.1] superior la EAD que resultaría para el mismo conjunto si no los tuviera. | [intro 4.2.1] − La EAD de un conjunto de neteo que sólo comprende opciones vendidas podrá | [intro 4.2.1] ser cero cuando hayan sido cobradas todas las primas y en tanto dichas opciones
no estén comprendidas en acuerdos de neteo que incluyan otros productos o la
constitución de márgenes.
- texto propio: 4.2.1.2. Cálculo de la EPF.
Resultará del producto entre:
- la suma de los adicionales correspondientes a cada clase de activos; y
- un multiplicador que permite reconocer la garantía en exceso o el valor de
mercado negativo de las operaciones, conforme a la siguiente expresión:
EPF = multiplicador x AdicionalTotal
donde:
es la suma de los adicionales correspondientes a cada clase de activos
–no se reconocen beneficios por diversificación–, calculados de acuerdo con
la metodología expuesta en los acápites viii) a xii) de este punto, y el multi-
plicador se define como:
El multiplicador se reduce a medida que se incrementa la tenencia de garan-
tías en exceso –sujeto a un mínimo de 5 % de la EPF– y operará de la si-
guiente manera:
− Cuando el costo de reposición corriente sea positivo –esto es, cuando el
valor de los activos en garantía sea inferior al valor de mercado neto de los
contratos de derivados– el multiplicador será igual a uno –esto es, el com-
ponente EPF será igual al valor del AdicionalTotal–.
− Cuando el valor de los activos en garantía supere el valor de mercado neto
de los contratos de derivados –garantías en exceso–, el multiplicador será
inferior a la unidad –esto es, el componente EPF será menor que el valor
del AdicionalTotal –.
− El multiplicador se activará –es decir, tomará un valor inferior a la unidad–
también cuando el valor corriente de las operaciones con derivados sea
negativo.
Para determinar el cálculo de la EPF, las operaciones se ajustarán a lo si-
guiente:
− Cada derivado se asignará a una clase de activo sobre la base de su factor
de riesgo principal –que en la mayoría de los casos será el único, definido
por la referencia a un instrumento subyacente, tal como una curva de tasas
de interés en el caso de un “swap” de tasas de interés o
- entidades de la unidad:
  - `e1` Operacion: Cálculo de la exposición potencial futura (EPF) — Cálculo de la exposición potencial futura (EPF) como producto de la suma de adicionales por clase de activos y un multiplicador que reconoce garantía en exceso o valor de mercado negativo
  - `e2` Definicion: AdicionalTotal — suma de adicionales por clase de activos — suma de los adicionales correspondientes a cada clase de activos, sin reconocimiento de beneficios por diversificación, calculados según la metodología de los acápites viii) a xii)
  - `e3` Restriccion: Límite mínimo del multiplicador — garantía en exceso — El multiplicador se reduce según la tenencia de garantías en exceso, con un mínimo del 5% de la EPF
  - `e4` Condicion: Cuando costo de reposición es positivo — Supuesto en que el valor de los activos en garantía es inferior al valor de mercado neto de los contratos de derivados
  - `e5` Obligacion: Multiplicador igual a uno cuando CR positivo — Cuando el costo de reposición sea positivo, el multiplicador toma valor uno, haciendo el EPF igual al AdicionalTotal
  - `e6` Condicion: Cuando valor de garantías en exceso supera valor de mercado neto — Supuesto en que los activos en garantía superan el valor de mercado neto de los contratos de derivados
  - `e7` Obligacion: Multiplicador menor a uno cuando garantías en exceso — Cuando hay garantías en exceso, el multiplicador es inferior a uno, reduciendo el EPF respecto a AdicionalTotal
  - `e8` Condicion: Cuando valor corriente de derivados es negativo — Supuesto en que el valor corriente de las operaciones con derivados es negativo
  - `e9` Obligacion: Asignación del derivado a clase de activo según factor de riesgo principal — Asignación de cada derivado a una clase de activo según su factor de riesgo principal, identificado por el instrumento subyacente
  - `e10` Obligacion: Asignación a clase de activo cuando se identifica claramente el factor principal — Cuando se identifica claramente el factor de riesgo principal, la operación se clasifica en una de cinco clases de activos: tasa de interés, tipo de cambio, crédito, acciones o commodities
  - `e11` Obligacion: Consideración de sensibilidad y volatilidad en derivados complejos — En derivados híbridos con múltiples factores de riesgo, las entidades deben considerar la sensibilidad y volatilidad de los subyacentes para identificar el factor de riesgo principal
  - `e12` Potestad: Potestad de la SEFyC — requerir asignación múltiple en derivados complejos — La SEFyC puede requerir que operaciones complejas se asignen a múltiples clases de activos, con determinación separada del signo y ajuste delta para cada factor de riesgo
  - `e13` Obligacion: Cálculo de adicional por clase de activo usando fórmulas específicas — El adicional para cada clase de activo se calcula mediante fórmulas específicas que determinan la EPE (Expected Positive Exposure) efectiva
  - `e14` Obligacion: Cálculo de nocional ajustado a partir de nocional real o precio — Cálculo del nocional ajustado a partir del nocional real o del precio de la operación
  - `e15` Definicion: Nocional ajustado para derivados de tasa de interés y créditos — Para derivados de tasa de interés y créditos, el nocional ajustado incorpora una medición del plazo (duration) establecida en el acápite ii)
  - `e16` Obligacion: Cálculo de factor plazo para cada operación — Cálculo del factor plazo (MF) para reflejar el horizonte temporal según el tipo de operación: con márgenes o sin márgenes
  - `e17` Obligacion: Aplicación de ajuste delta al nocional ajustado — Aplicación de ajuste delta al nocional ajustado según el tipo de posición (larga/corta) y tipo de instrumento (opción, segmento CDO, otro)
  - `e18` Obligacion: Aplicación de factor de volatilidad al nocional efectivo — Aplicación de un factor de volatilidad al nocional efectivo de cada operación
  - `e19` Obligacion: Separación de operaciones por conjunto de cobertura — Separación de operaciones dentro de cada clase de activo por conjunto de cobertura (hedging set)
  - `e20` Obligacion: Aplicación de método de suma con parámetros de correlación — Aplicación de método de suma para agregar operaciones dentro de cada conjunto y entre conjuntos, utilizando parámetros de correlación para derivados de crédito, acciones y commodities
  - `e21` Definicion: M (vencimiento) — parámetro de tiempo — Última fecha hasta la que podría estar activo el contrato. Se utiliza en el factor plazo para reducir el nocional ajustado de operaciones sin márgenes
  - `e22` Definicion: S (fecha de inicio) — parámetro de tiempo en derivados de interés y crédito — Fecha de inicio del período referenciado en derivados de tasas de interés y créditos. Se utiliza en la definición del plazo regulatorio
  - `e23` Definicion: E (fecha de finalización) — parámetro de tiempo en derivados de interés y crédito — Fecha de finalización del período referenciado en derivados de tasas de interés y créditos. Se utiliza en la definición del plazo regulatorio y categorización por plazos
  - `e24` Definicion: T (fecha de ejercicio) — parámetro de tiempo en opciones — Última fecha de ejercicio de la opción según el contrato. Se utiliza para determinar el delta de la opción
  - `e25` Definicion: Nocional ajustado a nivel de operación — derivados de tasa de interés y créditos — Producto del nocional en pesos y el plazo regulatorio (SD) para derivados de tasa de interés y créditos
  - `e26` Restriccion: Límite mínimo de período de plazo regulatorio — El período de plazo regulatorio tiene un mínimo de 10 días hábiles
  - `e27` Definicion: Nocional ajustado para derivados de tipo de cambio — Nocional del lado expresado en moneda extranjera convertido a pesos; si ambos lados están en moneda extranjera, se toma el mayor de ambos convertidos
  - `e28` Definicion: Nocional ajustado para derivados sobre acciones y commodities — Producto del precio corriente unitario por el número de unidades referenciadas en la operación
  - `e29` Definicion: Nocional ajustado para operaciones sobre volatilidad — Producto de la volatilidad o varianza referenciadas en la operación y el nocional contractual
  - `e30` Obligacion: Observancia de normas especiales para nocionales no claramente definidos — Para operaciones con nocionales no claramente definidos o variables, se deben observar reglas específicas de determinación
  - `e31` Obligacion: Cálculo de nocional para opciones digitales — Para opciones digitales con múltiples retribuciones contingentes, se calcula un nocional por estado y se toma el mayor
  - `e32` Obligacion: Determinación de nocional cuando es fórmula de valores de mercado — Cuando el nocional está definido como fórmula en valores de mercado, se utilizan los valores corrientes para su determinación
  - `e33` Obligacion: Cálculo de nocional promedio ponderado por tiempo en swaps de nocional variable — Para swaps de nocional variable, se utiliza el promedio ponderado por tiempo del nocional durante la vida residual del instrumento
  - `e34` Excepcion: Excepción a promedio ponderado — derivados FX, acciones y commodities — La regla de promedio ponderado por tiempo no aplica a operaciones donde el nocional varía por cambios de precios (derivados FX, acciones, commodities)
  - `e35` Obligacion: Conversión de swaps apalancados a equivalentes no apalancados — Los swaps apalancados se convierten a equivalentes no apalancados; cuando las tasas se multiplican por un factor, el nocional se multiplica por ese factor
  - `e36` Obligacion: Ajuste de nocional por número de intercambios de principal — Para derivados con intercambios múltiples del principal, el nocional se multiplica por el número de intercambios previstos
  - `e37` Obligacion: Ajuste de plazo residual en derivados con reformulación de condiciones — En derivados con reformulación periódica a fair value cero, el plazo residual se calcula hasta la próxima fecha de reformulación
  - `e38` Obligacion: Cálculo de parámetros precio, precio de ejercicio y volatilidad en opciones — Cálculo de parámetros de opciones: precio del subyacente (preferentemente forward), precio de ejercicio (K), fecha de ejercicio (T) y volatilidad conforme a factores regulatorios
  - `e39` Obligacion: Cálculo de parámetros en segmentos CDO — Cálculo de parámetros de segmentos de CDO: punto de unión (A) y punto de separación (D)
  - `e40` Obligacion: Aplicación de factores regulatorios de volatilidad — Aplicación de factores regulatorios de volatilidad específicos por clase de activo al nocional efectivo para obtener la EPE efectiva
  - `e41` Definicion: Conjuntos de cobertura en tasas de interés — Un conjunto de cobertura por cada moneda en derivados sobre tasas de interés
  - `e42` Definicion: Conjuntos de cobertura en derivados FX — Un conjunto de cobertura por cada par de monedas en derivados FX
  - `e43` Definicion: Conjuntos de cobertura en derivados de crédito — Un único conjunto de cobertura para todos los derivados de crédito
  - `e44` Definicion: Conjuntos de cobertura en derivados sobre acciones — Un único conjunto de cobertura para todos los derivados sobre acciones
  - `e45` Definicion: Conjuntos de cobertura en derivados sobre commodities — Cuatro conjuntos de cobertura según categoría: energía, metales, productos agrícolas y otros productos básicos
  - `e46` Obligacion: Asignación de derivados sobre bases a conjuntos de cobertura específicos — Derivados sobre bases denominados en una sola moneda se asignan a conjuntos de cobertura específicos dentro de su clase de activo
  - `e47` Excepcion: Excepción a tratamiento de bases — cross-currency swaps — Los cross-currency swaps no se tratan como derivados sobre bases; reciben el tratamiento de contratos FX ordinarios
  - `e48` Definicion: Conjuntos de cobertura para derivados sobre bases — Un conjunto por cada par de factores de riesgo (cada base específica); posiciones clasificadas como largas o cortas respecto de la base
  - `e49` Restriccion: Multiplicador del factor SF en derivados sobre bases — límite de 0,5 — En conjuntos de cobertura de derivados sobre bases, el factor de volatilidad (SF) se multiplica por 0,5
  - `e50` Definicion: Conjuntos de cobertura para derivados sobre volatilidad — Derivados sobre volatilidad (swaps de varianza/volatilidad, opciones sobre volatilidad real/implícita) se asignan a conjuntos específicos dentro de su clase de activo
  - `e51` Restriccion: Multiplicador del factor SF en derivados sobre volatilidad — límite de 5 — En conjuntos de cobertura de derivados sobre volatilidad, el factor de volatilidad (SF) se multiplica por 5
  - `e52` Definicion: Factor de plazo para operaciones sin margen de variación — Para operaciones sin margen, el horizonte temporal mínimo es el menor entre un año y el plazo residual, con un mínimo de 10 días hábiles
  - `e53` Obligacion: Aplicación de factor plazo a nocional ajustado en operaciones sin margen — Multiplicación del nocional ajustado por un factor de plazo cuyo numerador es el horizonte temporal mínimo y denominador el plazo residual (mínimo 10 días hábiles)
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 53** Excepcion `e34`: Excepción a promedio ponderado — derivados FX, acciones y commodities | descripcion: La regla de promedio ponderado por tiempo no aplica a operaciones donde el nocional varía por cambios de precios (derivados FX, acciones, commodities) | tramo: Esta regla no será aplicable a las operaciones en las que el nocional varía debido a cambios en los precios –tales como los derivados FX, y sobre acciones o "commodities"–
  - **caso 69** Excepcion `e47`: Excepción a tratamiento de bases — cross-currency swaps | descripcion: Los cross-currency swaps no se tratan como derivados sobre bases; reciben el tratamiento de contratos FX ordinarios | tramo: Este tratamiento no se aplicará a los derivados con dos lados flotantes denominados en monedas diferentes –tales como los "cross-currency swaps": acuerdos para intercambiar pagos de principal e intereses de préstamos denominados en dos monedas diferentes–, los que recibirán el tratamiento aplicable a los contratos FX ordinarios
  - **caso 162** Condicion `e4`: Cuando costo de reposición es positivo | descripcion: Supuesto en que el valor de los activos en garantía es inferior al valor de mercado neto de los contratos de derivados | tramo: Cuando el costo de reposición corriente sea positivo –esto es, cuando el valor de los activos en garantía sea inferior al valor de mercado neto de los contratos de derivados–
  - **caso 163** Condicion `e8`: Cuando valor corriente de derivados es negativo | descripcion: Supuesto en que el valor corriente de las operaciones con derivados es negativo | tramo: El multiplicador se activará –es decir, tomará un valor inferior a la unidad– también cuando el valor corriente de las operaciones con derivados sea negativo
  - **caso 164** Condicion `e6`: Cuando valor de garantías en exceso supera valor de mercado neto | descripcion: Supuesto en que los activos en garantía superan el valor de mercado neto de los contratos de derivados | tramo: Cuando el valor de los activos en garantía supere el valor de mercado neto de los contratos de derivados –garantías en exceso–

## Unidad `ctacte::8.6.3` (punto_no_item)
- herencia: [encabezado 8.6] 8.6. Información al Banco Central de la República Argentina.
- texto propio: 8.6.3. El responsable del régimen informativo y el auditor externo de la entidad deberán verifi-
car el cumplimiento de los requisitos y procedimientos establecidos y sus conclusiones
volcadas semestralmente en un informe especial, conforme a las normas que se esta-
blezcan en la materia.
Esta disposición no sustituye la obligación de informar al BCRA los rechazos y/o el pago
de las correspondientes multas, en los plazos establecidos con carácter general (puntos
6.4. y 6.5., respectivamente).
- entidades de la unidad:
  - `e1` Obligacion: Verificación semestral de requisitos y procedimientos — 
  - `e2` Excepcion: No sustituye obligación de informar rechazos y multas — La verificación semestral no sustituye la obligación de informar al BCRA los rechazos y/o el pago de multas en los plazos establecidos con carácter general
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 54** Excepcion `e2`: No sustituye obligación de informar rechazos y multas | descripcion: La verificación semestral no sustituye la obligación de informar al BCRA los rechazos y/o el pago de multas en los plazos establecidos con carácter general | tramo: Esta disposición no sustituye la obligación de informar al BCRA los rechazos y/o el pago de las correspondientes multas, en los plazos establecidos con carácter general

## Unidad `cla::6.5::intro` (intro)
- herencia: [encabezado 6.5] 6.5. Niveles de clasificación.
- texto propio: Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
los fines a que se refiere el punto 6.6.
A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
Tampoco se considerarán dentro de ese concepto las r
- entidades de la unidad:
  - `e1` Operacion: Inclusión de cliente en categoría de clasificación — Cada cliente y la totalidad de sus financiaciones comprendidas se incluirá en una de las cinco categorías de clasificación, definidas según las condiciones detalladas en cada caso.
  - `e2` Definicion: Categorías de clasificación — cinco niveles — Cinco categorías de clasificación de deudores, definidas según las condiciones detalladas en cada caso.
  - `e3` Condicion: Cliente sin asistencia crediticia previa — clasificación por flujo de fondos — Clientes sin asistencia crediticia previa de la entidad que reciben financiaciones que no superen el importe resultante de aplicar el porcentaje de previsiones mínimas sobre el saldo de deuda en la Ce
  - `e4` Potestad: Clasificación por flujo de fondos proyectado — clientes sin asistencia previa — La entidad podrá clasificar a clientes sin asistencia crediticia previa teniendo en cuenta únicamente el análisis del flujo de fondos proyectado, cuando se cumplan las condiciones especificadas.
  - `e5` Excepcion: Exclusión de asistencias — punto 6.6 — Las asistencias crediticias otorgadas a clientes sin asistencia previa no serán consideradas a los fines del punto 6.6.
  - `e6` Definicion: Facilidades adicionales — no refinanciación — Facilidades adicionales sobre márgenes vigentes acordados que impliquen nuevos desembolsos de fondos y no superen el 10 % del cupo asignado en la última evaluación crediticia, no se consideran refinan
  - `e7` Condicion: Facilidades adicionales — consistencia con curso normal de negocios — Las facilidades adicionales deben ser consistentes con el curso normal de los negocios y debe existir capacidad para atender el resto de las obligaciones financieras.
  - `e8` Definicion: Nuevas financiaciones y refinanciaciones — expansión de actividades — Nuevas financiaciones y refinanciaciones asociadas a mayor inversión derivada de expansión de actividades, cuando pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de
  - `e9` Condicion: Flujo de fondos proyectado — capacidad de pago total — Debe demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de las obligaciones financieras.
  - `e10` Excepcion: Refinanciaciones — productores agropecuarios Ley de Emergencia — Las refinanciaciones otorgadas a productores agropecuarios derivadas de la aplicación de disposiciones de la Ley de Emergencia Agropecuaria no se consideran refinanciaciones a los fines de verificació
  - `e11` Obligacion: Consideración de flujo de fondos — productores agropecuarios emergencia — A los fines de la clasificación de productores agropecuarios beneficiarios de la Ley de Emergencia Agropecuaria, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya 
  - `e12` Restriccion: Prohibición mejoramiento de clasificación — productores agropecuarios emergencia — El tratamiento dispensado en el marco de la Ley de Emergencia Agropecuaria no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual preexistente a l
  - `e13` Restriccion: Límite temporal — aplicación emergencia agropecuaria — La aplicación del tratamiento de la Ley de Emergencia Agropecuaria no podrá extenderse más allá de la vigencia fijada para la emergencia.
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e4; e7 condicion_de e6; e9 condicion_de e8
- NODOS A CLASIFICAR:
  - **caso 55** Excepcion `e5`: Exclusión de asistencias — punto 6.6 | descripcion: Las asistencias crediticias otorgadas a clientes sin asistencia previa no serán consideradas a los fines del punto 6.6. | tramo: Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6
  - **caso 68** Excepcion `e10`: Refinanciaciones — productores agropecuarios Ley de Emergencia | descripcion: Las refinanciaciones otorgadas a productores agropecuarios derivadas de la aplicación de disposiciones de la Ley de Emergencia Agropecuaria no se consideran refinanciaciones a los fines de verificación de cumplimiento de obligaciones. | tramo: Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria

## Unidad `ext::6.4` (item)
- herencia: **[abre la lista]** [chapeau_seccion S6] En el marco de estas disposiciones se definen los siguientes conceptos:
- texto propio: 6.4. Operaciones a término.
Comprende las operaciones en las cuales la liquidación está pactada en un plazo mayor a los
2 (dos) días hábiles desde la fecha de su concertación.
En el caso de que se prevea la entrega efectiva de instrumentos operados en el mercado de
cambios, estas operaciones quedan sujetas a la norma cambiaria y se consideran un acceso
al mercado de cambios a concretarse en la fecha de su liquidación.
No están sujetas a estas normas las concertaciones y cancelaciones de operaciones de
futuros en mercados regulados, “forwards”, opciones y cualquier otro tipo de derivado en la
medida que estén instrumentadas bajo ley argentina y su liquidación se efectúe en el país por
compensación en moneda doméstica, sin que pueda generar obligaciones presentes o futuras
de realizar pagos en moneda extranjera.
- entidades de la unidad:
  - `e1` Definicion: Operaciones a término — definición — Operaciones en las cuales la liquidación está pactada en un plazo mayor a los 2 (dos) días hábiles desde la fecha de su concertación.
  - `e2` Condicion: Entrega efectiva de instrumentos — condición — Cuando se prevea la entrega efectiva de instrumentos operados en el mercado de cambios.
  - `e3` Operacion: Acceso al mercado de cambios — operaciones a término — Operaciones a término con entrega efectiva de instrumentos que se consideran un acceso al mercado de cambios a concretarse en la fecha de su liquidación, sujetas a la norma cambiaria.
  - `e4` Excepcion: Excepción — futuros, forwards, opciones y derivados — Las concertaciones y cancelaciones de operaciones de futuros en mercados regulados, forwards, opciones y otros derivados instrumentados bajo ley argentina con liquidación en el país por compensación e
  - `e5` Condicion: Instrumentación bajo ley argentina — condición — Cuando los derivados estén instrumentados bajo ley argentina.
  - `e6` Condicion: Liquidación por compensación en moneda doméstica — condición — Cuando la liquidación se efectúe en el país por compensación en moneda doméstica.
  - `e7` Condicion: Sin obligaciones de pagos en moneda extranjera — condición — Cuando no pueda generar obligaciones presentes o futuras de realizar pagos en moneda extranjera.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e3; e5 condicion_de e4; e6 condicion_de e4; e7 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 56** Excepcion `e4`: Excepción — futuros, forwards, opciones y derivados | descripcion: Las concertaciones y cancelaciones de operaciones de futuros en mercados regulados, forwards, opciones y otros derivados instrumentados bajo ley argentina con liquidación en el país por compensación en moneda doméstica sin obligaciones de pagos en moneda extranjera no están sujetas a estas normas. | tramo: No están sujetas a estas normas las concertaciones y cancelaciones de operaciones de futuros en mercados regulados, "forwards", opciones y cualquier otro tipo de derivado en la medida que estén instrumentadas bajo ley argentina y su liquidación se efectúe en el país por compensación en moneda doméstica, sin que pueda generar obligaciones presentes o futuras de realizar pagos en moneda extranjera.

## Unidad `ext::3.5.1.9` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.5] exterior.
Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o
intereses de títulos de deuda con registro público en el exterior, otros endeudamientos
financieros con el exterior y títulos de deuda con registro público en el país denominados en
moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las
siguientes condiciones: | **[abre la lista]** [intro 3.5.1] un monto equivalente al valor nominal del endeudamiento financiero.
Este requisito se considerará cumplimentado en los siguientes casos:
- texto propio: 3.5.1.9. por los endeudamientos con el exterior originados a partir del 01/09/19 en
una refinanciación del capital y/o intereses de deudas comerciales con el
acreedor del exterior, en la medida que la nueva deuda financiera no anticipe
vencimientos respecto de la deuda comercial refinanciada ni implique la
realización de pagos antes de la fecha en que el cliente hubiera podido
acceder por la deuda comercial en virtud de la normativa aplicable.
Estas condiciones se podrán considerar cumplimentadas para los
endeudamientos con una vida promedio no inferior a los 2 (dos) años
originados entre 27/08/21 y el 12/12/23 en una refinanciación encuadrada en
el punto 20. de la Comunicación A 7626 y concordantes (disposiciones
receptadas oportunamente en el punto 3.20. del Anexo de la Comunicación
A 7914); en la medida que la entidad cuente con una certificación para el
acceso al mercado de cambios emitida, dentro de los 5 (cinco) días hábiles
previos, por la entidad que concretó el registro ante el BCRA con el código
de concepto “P17. Registro de refinanciación de deuda comercial en el
marco del punto 20. de la Comunicación A 7626”.
- entidades de la unidad:
  - `c1` Condicion: Endeudamiento originado a partir del 01/09/19 — El endeudamiento con el exterior debe haber sido originado a partir del 01/09/19
  - `c2` Condicion: Refinanciación de deuda comercial — El endeudamiento debe constituir una refinanciación del capital y/o intereses de deudas comerciales con el acreedor del exterior
  - `r1` Restriccion: No anticipación de vencimientos en refinanciación — La nueva deuda financiera no puede anticipar vencimientos respecto de la deuda comercial refinanciada
  - `r2` Restriccion: No realización de pagos anticipados respecto a deuda comercial — La nueva deuda financiera no puede implicar la realización de pagos antes de la fecha en que el cliente hubiera podido acceder por la deuda comercial en virtud de la normativa aplicable
  - `e1` Excepcion: Excepción vida promedio mínima 2 años — período 27/08/21 a 12/12/23 — Las condiciones de no anticipación de vencimientos y no realización de pagos anticipados se consideran cumplimentadas para endeudamientos con vida promedio no inferior a 2 años originados entre 27/08/
  - `c3` Condicion: Certificación de acceso al mercado de cambios — La entidad debe contar con certificación para acceso al mercado de cambios emitida dentro de 5 días hábiles previos por la entidad que concretó el registro ante el BCRA con código de concepto P17
  - `com1` Comunicacion: Com. A 7626 — 
  - `com2` Comunicacion: Com. A 7914 — 
- relaciones del crudo (sin establecida_en ni de sujeto): to referencia com1; to referencia com2; c1 condicion_de e1; c2 condicion_de e1; c3 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 57** Excepcion `e1`: Excepción vida promedio mínima 2 años — período 27/08/21 a 12/12/23 | descripcion: Las condiciones de no anticipación de vencimientos y no realización de pagos anticipados se consideran cumplimentadas para endeudamientos con vida promedio no inferior a 2 años originados entre 27/08/21 y 12/12/23 en refinanciación conforme punto 20 de Com. A 7626 | tramo: Estas condiciones se podrán considerar cumplimentadas para los endeudamientos con una vida promedio no inferior a los 2 (dos) años originados entre 27/08/21 y el 12/12/23 en una refinanciación encuadrada en el punto 20. de la Comunicación A 7626 y concordantes

## Unidad `cap::3.1.5.3` (punto_no_item)
- herencia: [intro 3.1] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi-
cional o sintética, o a una estructura con similares características.
La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con-
ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de
deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset-
Backed Securities”, ABS) y bonos de tit | [encabezado 3.1.5] 3.1.5. Criterios a observar en el cómputo de la exigencia de capital mínimo.
- texto propio: 3.1.5.3. No se incluirán dentro de las previsiones por riesgo de incobrabilidad computa-
bles del punto 8.2.3.3. las previsiones generales ni las específicas asociadas a
las posiciones de titulización o a las exposiciones subyacentes que están toda-
vía en el activo de la entidad originante. No obstante, las entidades originantes
podrán deducir de las posiciones de titulización ponderadas al 1250 % tanto el
monto de las previsiones específicas como los descuentos no reembolsables en
el precio de adquisición de los activos subyacentes a la titulización. Las previ-
siones específicas asociadas a las posiciones de titulización se considerarán en
el cálculo del importe de la posición de acuerdo con la definición prevista en el
punto 3.1.5.4. Las previsiones generales de las exposiciones subyacentes no se
tendrán en cuenta en ningún cálculo.
- entidades de la unidad:
  - `e1` Restriccion: Exclusión previsiones generales — titulizaciones — No se incluirán dentro de las previsiones por riesgo de incobrabilidad computables las previsiones generales ni las específicas asociadas a las posiciones de titulización o a las exposiciones subyacen
  - `e2` Excepcion: Deducción previsiones específicas — posiciones ponderadas 1250% — Las entidades originantes pueden deducir de las posiciones de titulización ponderadas al 1250% tanto el monto de las previsiones específicas como los descuentos no reembolsables en el precio de adquis
  - `e3` Obligacion: Consideración previsiones específicas — cálculo posición — Las previsiones específicas asociadas a las posiciones de titulización se considerarán en el cálculo del importe de la posición de acuerdo con la definición prevista en el punto 3.1.5.4
  - `e4` Restriccion: Exclusión previsiones generales — exposiciones subyacentes — Las previsiones generales de las exposiciones subyacentes no se tendrán en cuenta en ningún cálculo
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 58** Excepcion `e2`: Deducción previsiones específicas — posiciones ponderadas 1250% | descripcion: Las entidades originantes pueden deducir de las posiciones de titulización ponderadas al 1250% tanto el monto de las previsiones específicas como los descuentos no reembolsables en el precio de adquisición de los activos subyacentes | tramo: las entidades originantes podrán deducir de las posiciones de titulización ponderadas al 1250 % tanto el monto de las previsiones específicas como los descuentos no reembolsables en el precio de adquisición de los activos subyacentes a la titulización

## Unidad `ext::13.4.3` (item)
- herencia: **[abre la lista]** [intro 13.4] Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para
realizar pagos de servicios de no residentes prestados o devengados hasta el 12/12/23,
excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique
que:
- texto propio: 13.4.3. el pago corresponda a la cancelación de deudas por operaciones financiadas o
garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o
agencias oficiales de crédito; o
Las entidades podrán considerar también como operación garantizada por una
agencia oficial de crédito a aquella que se encuentre cubierta por una garantía
emitida por una aseguradora privada por cuenta y orden de un gobierno nacional de
otro país. En todos los casos, la entidad interviniente deberá contar con
documentación en la que conste explícitamente tal situación.
- entidades de la unidad:
  - `c1` Condicion: Pago cancelación deudas operaciones financiadas/garantizadas — El pago debe corresponder a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito.
  - `e1` Excepcion: Operación garantizada por aseguradora privada por cuenta de gobierno — Las entidades pueden considerar como operación garantizada por una agencia oficial de crédito aquella cubierta por garantía emitida por aseguradora privada por cuenta y orden de un gobierno nacional d
  - `o1` Obligacion: Documentación explícita de garantía por aseguradora privada — La entidad interviniente debe contar con documentación que conste explícitamente la situación de cobertura por garantía de aseguradora privada por cuenta y orden de gobierno nacional de otro país.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 59** Excepcion `e1`: Operación garantizada por aseguradora privada por cuenta de gobierno | descripcion: Las entidades pueden considerar como operación garantizada por una agencia oficial de crédito aquella cubierta por garantía emitida por aseguradora privada por cuenta y orden de un gobierno nacional de otro país. | tramo: Las entidades podrán considerar también como operación garantizada por una agencia oficial de crédito a aquella que se encuentre cubierta por una garantía emitida por una aseguradora privada por cuenta y orden de un gobierno nacional de otro país
  - **caso 214** Condicion `c1`: Pago cancelación deudas operaciones financiadas/garantizadas | descripcion: El pago debe corresponder a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito. | tramo: el pago corresponda a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito

## Unidad `ext::8.5.17.22` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.22. Exportaciones a zonas francas nacionales.
- entidades de la unidad:
  - `e1` Operacion: Exportaciones a zonas francas nacionales — Exportaciones de bienes a zonas francas nacionales, operación aduanera exceptuada del seguimiento de divisas por exportaciones
  - `e2` Excepcion: Excepción seguimiento — exportaciones a zonas francas — Las exportaciones a zonas francas nacionales quedan exceptuadas del seguimiento de permisos de embarque por divisas
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 60** Excepcion `e2`: Excepción seguimiento — exportaciones a zonas francas | descripcion: Las exportaciones a zonas francas nacionales quedan exceptuadas del seguimiento de permisos de embarque por divisas | tramo: Exportaciones a zonas francas nacionales

## Unidad `ext::8.5.17.20` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.20. Exportaciones de bienes enviados al exterior con fines promocionales
amparadas por la Resolución 772/92 de Administración Nacional de
Aduanas, hasta un tope de USD 5.000 (dólares estadounidenses cinco
mil).
- entidades de la unidad:
  - `e1` Operacion: Exportación bienes con fines promocionales — Exportaciones de bienes enviados al exterior con fines promocionales amparadas por la Resolución 772/92 de Administración Nacional de Aduanas
  - `e2` Restriccion: Tope USD 5.000 — exportación promocional — El valor de las exportaciones de bienes enviados al exterior con fines promocionales no podrá exceder USD 5.000
  - `e3` Excepcion: Excepción seguimiento — exportación promocional — Las exportaciones de bienes enviados al exterior con fines promocionales amparadas por la Resolución 772/92 de Administración Nacional de Aduanas, hasta un tope de USD 5.000, quedan exceptuadas del se
- relaciones del crudo (sin establecida_en ni de sujeto): e2 limita e1
- NODOS A CLASIFICAR:
  - **caso 61** Excepcion `e3`: Excepción seguimiento — exportación promocional | descripcion: Las exportaciones de bienes enviados al exterior con fines promocionales amparadas por la Resolución 772/92 de Administración Nacional de Aduanas, hasta un tope de USD 5.000, quedan exceptuadas del seguimiento de permisos de embarque | tramo: Exportaciones de bienes enviados al exterior con fines promocionales amparadas por la Resolución 772/92 de Administración Nacional de Aduanas, hasta un tope de USD 5.000 (dólares estadounidenses cinco mil)

## Unidad `cap::2.11.3.5` (item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca | **[abre la lista]** [intro 2.11.3] A los fines de determinar si una exposición debe ser tratada como una acción, las en-
tidades financieras del grupo 1 deberán tener en cuenta la realidad económica del ins-
trumento.
Quedan comprendidas:
- texto propio: 2.11.3.5. Los títulos de deuda y otros valores, los derivados y los vehículos estructu-
rados con el fin de replicar la realidad económica de una acción.
Se incluyen las obligaciones cuyo rendimiento esté vinculado al de las ac-
ciones, y las acciones contabilizadas como un préstamo que se originen en
un canje de deuda por acciones realizado en un proceso de reestructuración
de deudas. El requisito de capitales mínimos que se determine para estos úl-
timos instrumentos no puede ser menor al que le hubiera correspondido de
haber permanecido en la cartera de créditos.
A los fines del cumplimiento de estas disposiciones, la SEFYC podrá recate-
gorizar las posiciones de deuda como posiciones en acciones si advierte que
no se cumplen las condiciones y requisitos que aseguren el adecuado trata-
miento de las tenencias.
Las inversiones en acciones estructuradas con el objeto de replicar la reali-
dad económica de las exposiciones crediticias o de titulizaciones no se con-
siderarán acciones.
- entidades de la unidad:
  - `e1` Operacion: Títulos de deuda replicando acción — Títulos de deuda, otros valores, derivados y vehículos estructurados cuyo fin es replicar la realidad económica de una acción; incluye obligaciones cuyo rendimiento esté vinculado al de las acciones, 
  - `e2` Restriccion: Requisito mínimo capital — acciones de canje — El requisito de capitales mínimos para acciones originadas en canje de deuda no puede ser inferior al que hubiera correspondido si permanecieran en cartera de créditos.
  - `e3` Potestad: Recategorización de posiciones de deuda a acciones — La SEFYC está facultada a recategorizar posiciones de deuda como posiciones en acciones cuando advierte incumplimiento de las condiciones y requisitos para asegurar el adecuado tratamiento de las tene
  - `e4` Condicion: Incumplimiento de condiciones de tratamiento — Supuesto en que la SEFYC advierte que no se cumplen las condiciones y requisitos que aseguren el adecuado tratamiento de las tenencias.
  - `e5` Excepcion: Excepción — acciones estructuradas replicando exposiciones crediticias — Las inversiones en acciones estructuradas cuyo objeto es replicar la realidad económica de exposiciones crediticias o de titulizaciones quedan exceptuadas de ser consideradas acciones.
- relaciones del crudo (sin establecida_en ni de sujeto): e4 condicion_de e3
- NODOS A CLASIFICAR:
  - **caso 62** Excepcion `e5`: Excepción — acciones estructuradas replicando exposiciones crediticias | descripcion: Las inversiones en acciones estructuradas cuyo objeto es replicar la realidad económica de exposiciones crediticias o de titulizaciones quedan exceptuadas de ser consideradas acciones. | tramo: Las inversiones en acciones estructuradas con el objeto de replicar la realidad económica de las exposiciones crediticias o de titulizaciones no se considerarán acciones

## Unidad `pro::2.3.4` (punto_no_item)
- herencia: [encabezado 2.3] 2.3. Recaudos mínimos de la relación de consumo.
- texto propio: 2.3.4. Cambios de condiciones pactadas.
A fin de modificar las condiciones pactadas debe darse la totalidad de las siguientes
condiciones:
i) En el contrato deberán encontrarse taxativamente especificadas las condiciones
que pueden ser objeto de modificación, así como los parámetros o criterios objeti-
vos para su concreción, ajustándose a lo señalado en el punto 2.3.2.
Los incrementos en las tasas de interés, comisiones y/o cargos, además, deben ser
justificados desde el punto de vista técnico y económico, en el marco de lo dispues-
to en el punto 2.3.2.1.
ii) La modificación no debe alterar el objeto del contrato ni importar un desmedro res-
pecto de los productos o servicios contratados.
iii) Consentimiento.
En el caso de que el sujeto obligado pretenda incorporar nuevos conceptos en cali-
dad de comisiones y/o cargos que no hubiesen sido previstos en el contrato o re-
ducir prestaciones contempladas en él, deberá previamente obtener el consenti-
miento expreso del usuario de servicios financieros.
Cuando se trate de modificaciones en los valores de comisiones y/o cargos debi-
damente aceptados por el usuario, su consentimiento al cambio podrá quedar con-
formado por la falta de objeción al mismo dentro del plazo establecido en el acápite
iv).
En los contratos de tarjeta de crédito el consentimiento a modificaciones en las
condiciones pactadas (nuevas comisiones y/o cargos) sólo puede ser dado por el ti-
tular de la cuenta.
iv) Notificaciones. Forma, plazos y efectos.
El usuario de servicios financieros debe ser notificado de las modificaciones que
aplicará el sujeto obligado con una antelación mínima de sesenta (60) días corridos
a su entrada en vigencia. Las modificaciones que resulten económicamente más
beneficiosas para el usuario –por una reducción de los valore
- entidades de la unidad:
  - `c1` Condicion: Especificación taxativa de condiciones modificables — Las condiciones que pueden ser objeto de modificación deben estar taxativamente especificadas en el contrato, junto con los parámetros o criterios objetivos para su concreción, conforme a lo señalado 
  - `o1` Obligacion: Justificación técnica y económica de incrementos en tasas e intereses — Los incrementos en las tasas de interés, comisiones y/o cargos deben ser justificados desde el punto de vista técnico y económico, conforme a lo dispuesto en el punto 2.3.2.1.
  - `r1` Restriccion: Prohibición de alterar objeto del contrato o desmejorar servicios — La modificación de condiciones pactadas no debe alterar el objeto del contrato ni importar un desmedro respecto de los productos o servicios contratados.
  - `o2` Obligacion: Consentimiento expreso para nuevas comisiones o reducción de prestaciones — El sujeto obligado debe obtener previamente el consentimiento expreso del usuario de servicios financieros cuando pretenda incorporar nuevos conceptos en calidad de comisiones y/o cargos no previstos 
  - `e1` Excepcion: Consentimiento por falta de objeción para cambios en valores de comisiones — Para modificaciones en los valores de comisiones y/o cargos debidamente aceptados por el usuario, el consentimiento puede quedar conformado por la falta de objeción dentro del plazo establecido en el 
  - `r2` Restriccion: Consentimiento a modificaciones en tarjeta de crédito solo del titular — En los contratos de tarjeta de crédito, el consentimiento a modificaciones en las condiciones pactadas (nuevas comisiones y/o cargos) solo puede ser dado por el titular de la cuenta.
  - `o3` Obligacion: Notificación con antelación mínima de 60 días — El usuario de servicios financieros debe ser notificado de las modificaciones que aplicará el sujeto obligado con una antelación mínima de sesenta (60) días corridos a su entrada en vigencia.
  - `e2` Excepcion: Excepción notificación para modificaciones económicamente beneficiosas — Las modificaciones que resulten económicamente más beneficiosas para el usuario por reducción de los valores pactados no requieren notificación anticipada.
  - `o4` Obligacion: Notificaciones de cambios de condiciones gratuitas — Las notificaciones por cambios de condiciones pactadas (nuevos conceptos y/o valores o reducción de prestaciones del servicio) deben ser gratuitas para el usuario de servicios financieros.
  - `o5` Obligacion: Forma de notificación: documento escrito o electrónico — Las notificaciones deben efectuarse mediante documento escrito dirigido al domicilio real del usuario, en forma separada de cualquier otra información que remita el sujeto obligado, o por vía electrón
  - `o6` Obligacion: Requisitos de notificación electrónica: claridad, acceso y fecha — Cuando la notificación sea por vía electrónica, debe ser clara, de fácil acceso para el usuario e incluir la fecha de emisión.
  - `o7` Obligacion: Inclusión de leyenda sobre derecho a rescindir — Las notificaciones deben incluir la leyenda: 'Usted podrá optar por rescindir el contrato en cualquier momento antes de la entrada en vigencia del cambio y sin cargo alguno, sin perjuicio de que deber
  - `o8` Obligacion: Inclusión de leyenda sobre Régimen de Transparencia — Las notificaciones deben incluir la leyenda que remite al Régimen de Transparencia del BCRA para comparar costos, características y requisitos de productos y servicios financieros.
  - `o9` Obligacion: Cuadro comparativo de comisiones modificadas — Cuando se modifique el valor de las comisiones especificadas, las notificaciones deben exhibir un cuadro comparativo elaborado y puesto a disposición por la SEFYC.
  - `d1` Definicion: Comisiones de caja de ahorros sujetas a cuadro comparativo — Emisión de tarjetas de débito adicionales; reposición de tarjetas de débito por robo o extravío y uso de cajeros automáticos (fuera de casas operativas de la entidad, de otra entidad y en el exterior)
  - `d2` Definicion: Comisiones de tarjetas de crédito sujetas a cuadro comparativo — Servicio de emisión, renovación, administración o mantenimiento de cuenta; reposición o reimpresión de tarjeta por robo o extravío y tarjetas adicionales.
  - `d3` Definicion: Comisiones específicas de cuenta corriente — Mantenimiento de cuenta y talonario de cheques.
  - `d4` Definicion: Paquete para beneficiarios de prestaciones de seguridad social — Paquete que incluye el servicio de adelanto de haberes jubilatorios, destinado a beneficiarios de prestaciones de la seguridad social.
  - `d5` Definicion: Servicio de mantenimiento de paquetes — Servicio de mantenimiento de paquetes.
  - `c2` Condicion: Concurrencia de todas las condiciones para modificación — Para que sea válida la modificación de condiciones pactadas, deben cumplirse la totalidad de las condiciones enumeradas (i, ii, iii y iv), no basta con alguna de ellas.
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de c2; r1 condicion_de c2; o2 condicion_de c2; o3 condicion_de c2
- NODOS A CLASIFICAR:
  - **caso 63** Excepcion `e2`: Excepción notificación para modificaciones económicamente beneficiosas | descripcion: Las modificaciones que resulten económicamente más beneficiosas para el usuario por reducción de los valores pactados no requieren notificación anticipada. | tramo: Las modificaciones que resulten económicamente más beneficiosas para el usuario –por una reducción de los valores pactados– no requieren notificación anticipada.
  - **caso 103** Excepcion `e1`: Consentimiento por falta de objeción para cambios en valores de comisiones | descripcion: Para modificaciones en los valores de comisiones y/o cargos debidamente aceptados por el usuario, el consentimiento puede quedar conformado por la falta de objeción dentro del plazo establecido en el acápite iv). | tramo: Cuando se trate de modificaciones en los valores de comisiones y/o cargos debidamente aceptados por el usuario, su consentimiento al cambio podrá quedar conformado por la falta de objeción al mismo dentro del plazo establecido en el acápite iv).
  - **caso 152** Condicion `c2`: Concurrencia de todas las condiciones para modificación | descripcion: Para que sea válida la modificación de condiciones pactadas, deben cumplirse la totalidad de las condiciones enumeradas (i, ii, iii y iv), no basta con alguna de ellas. | tramo: A fin de modificar las condiciones pactadas debe darse la totalidad de las siguientes condiciones:

## Unidad `ext::8.5.17.24` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.24. Operaciones de reembarco consignadas mediante los subregímenes
RE01, RE04, RE05, RE06, REP1, REP4 o REP6.
- entidades de la unidad:
  - `e1` Operacion: Reembarco consignado mediante subregímenes aduaneros — Operaciones de reembarco consignadas mediante los subregímenes aduaneros RE01, RE04, RE05, RE06, REP1, REP4 o REP6
  - `e2` Excepcion: Excepción reembarco — seguimiento de permiso de embarque — Las operaciones de reembarco consignadas mediante los subregímenes RE01, RE04, RE05, RE06, REP1, REP4 o REP6 quedan exceptuadas del seguimiento de un permiso de embarque
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 64** Excepcion `e2`: Excepción reembarco — seguimiento de permiso de embarque | descripcion: Las operaciones de reembarco consignadas mediante los subregímenes RE01, RE04, RE05, RE06, REP1, REP4 o REP6 quedan exceptuadas del seguimiento de un permiso de embarque | tramo: Operaciones de reembarco consignadas mediante los subregímenes RE01, RE04, RE05, RE06, REP1, REP4 o REP6

## Unidad `ext::8.5.17.23` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.23. Operaciones de trasbordo (artículos 410 a 416 de la Ley 22.415).
- entidades de la unidad:
  - `e1` Operacion: Operaciones de trasbordo — Operaciones de trasbordo reguladas por los artículos 410 a 416 de la Ley 22.415, exceptuadas del seguimiento de negociaciones de divisas por exportaciones de bienes.
  - `e2` Excepcion: Excepción trasbordo — seguimiento de divisas — Las operaciones de trasbordo quedan exceptuadas del seguimiento de negociaciones de divisas por exportaciones de bienes.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 65** Excepcion `e2`: Excepción trasbordo — seguimiento de divisas | descripcion: Las operaciones de trasbordo quedan exceptuadas del seguimiento de negociaciones de divisas por exportaciones de bienes. | tramo: Operaciones de trasbordo (artículos 410 a 416 de la Ley 22.415)

## Unidad `cap::4.3.2` (punto_no_item)
- herencia: [intro 4.3] contraparte central.
Comprende a aquellas exposiciones de las entidades financieras con entidades de contrapar-
te central (CCP) que se originen en derivados OTC o negociados en mercados de valores y
en operaciones de financiación con títulos valores (“Securities Financing Transactions”, SFT)
y operaciones de liquidación diferida –definidas en el punto 4.2.–.
No están comprendidas las exposiciones originadas en operaciones al contado y que involu-
cren títulos valores, oro o moneda extranjera, c
- texto propio: 4.3.2. Alcance.
Cuando la entidad financiera realice operaciones con una QCCP deberá determinar
su exposición aplicando las disposiciones del punto 4.3.3., mientras que de tratarse
de una CCP que no califica serán de aplicación las previsiones del punto 4.3.4.
En los casos en que una CCP deje de calificar como QCCP, durante los tres meses
siguientes las operaciones podrán mantener el tratamiento del punto 4.3.3.; finalizado
ese plazo será de aplicación el punto 4.3.4.
Cuando se trate de una operación con derivados concertada en un mercado de
valores y la transacción entre el miembro compensador y la entidad financiera cliente
sea realizada y regida en el marco de un acuerdo bilateral, tanto la entidad financiera
cliente como el miembro compensador deberán dar a esa transacción el tratamiento
de un derivado OTC y aplicar lo previsto en el acápite ii) del punto 4.3.3.1. Este
tratamiento también se aplicará a las transacciones entre clientes de nivel inferior y
superior en una estructura multinivel.
- entidades de la unidad:
  - `e1` Operacion: Operaciones con QCCP — Operaciones que una entidad financiera realiza con una entidad de contraparte central calificada (QCCP), cuya exposición debe determinarse aplicando las disposiciones del punto 4.3.3.
  - `e2` Operacion: Operaciones con CCP no calificada — Operaciones que una entidad financiera realiza con una entidad de contraparte central que no califica como QCCP, cuya exigencia de capital se calcula conforme a lo previsto en el punto 4.3.4.
  - `e3` Condicion: CCP deja de calificar como QCCP — Supuesto en que una entidad de contraparte central pierde su calificación como QCCP.
  - `e4` Excepcion: Excepción tratamiento QCCP por tres meses — Las operaciones pueden mantener el tratamiento de QCCP durante tres meses después de que la CCP deje de calificar; finalizado ese plazo se aplica el punto 4.3.4.
  - `e5` Operacion: Derivados en mercado de valores con acuerdo bilateral — Operación con derivados concertada en un mercado de valores donde la transacción entre el miembro compensador y la entidad financiera cliente es realizada y regida en el marco de un acuerdo bilateral.
  - `e6` Obligacion: Tratamiento de derivado OTC para operaciones bilaterales — La entidad financiera cliente y el miembro compensador deben dar a la transacción el tratamiento de un derivado OTC y aplicar lo previsto en el acápite ii) del punto 4.3.3.1.
  - `e7` Obligacion: Tratamiento OTC en estructura multinivel — El tratamiento de derivado OTC también se aplica a las transacciones entre clientes de nivel inferior y superior en una estructura multinivel.
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 66** Excepcion `e4`: Excepción tratamiento QCCP por tres meses | descripcion: Las operaciones pueden mantener el tratamiento de QCCP durante tres meses después de que la CCP deje de calificar; finalizado ese plazo se aplica el punto 4.3.4. | tramo: durante los tres meses siguientes las operaciones podrán mantener el tratamiento del punto 4.3.3.

## Unidad `cla::2.2.1.3` (item)
- herencia: **[abre la lista]** [encabezado 2.2.1] 2.2.1. Los siguientes conceptos por intermediación financiera:
- texto propio: 2.2.1.3. Primas por opciones de compra y de venta tomadas.
- entidades de la unidad:
  - `e1` Operacion: Primas por opciones de compra y venta tomadas — Primas por opciones de compra y de venta tomadas en operaciones de intermediación financiera
  - `e2` Excepcion: Exclusión — Primas por opciones de compra y venta tomadas — Las primas por opciones de compra y de venta tomadas quedan excluidas de las financiaciones comprendidas
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 67** Excepcion `e2`: Exclusión — Primas por opciones de compra y venta tomadas | descripcion: Las primas por opciones de compra y de venta tomadas quedan excluidas de las financiaciones comprendidas | tramo: Primas por opciones de compra y de venta tomadas

## Unidad `ric::12.3` (punto_no_item)
- herencia: [encabezado S12] Sección 12. Disposiciones transitorias.
- texto propio: 12.3. Tratamiento de los defectos originados en el cómputo del 50 % –en lugar del 100 %– de los
resultados provenientes de los ajustes NIIF por primera vez dentro de la RPC (período enero
– marzo 2018).
Estos defectos se consideran admitidos (es decir que no constituirán incumplimientos) de
verificarse las siguientes condiciones:
a) surjan de la última conciliación de los estados contables trimestrales en el marco de la
convergencia a NIIF que cuente con informe de auditor externo;
b) dicha conciliación evidencia que de haberse considerado los resultados positivos al 100
% –en lugar del al 50 %– no se hubiera registrado tal defecto.
De reunir los requisitos citados, se consignará en la partida 60500000 la porción pertinente
para la neutralización del defecto generado.
A tal fin, se consignará como “número” y “fecha de Resolución” la de la Comunicación “A”
6456.
También se agregará una descripción detallada del cálculo del importe para el período in-
formado.
- entidades de la unidad:
  - `e1` Condicion: Defectos admitidos si surgen de última conciliación — El defecto se considera admitido si surge de la última conciliación de los estados contables trimestrales en el marco de la convergencia a NIIF que cuente con informe de auditor externo.
  - `e2` Condicion: Defectos admitidos si conciliación evidencia ausencia de defecto al 100 % — El defecto se considera admitido si la conciliación evidencia que de haberse considerado los resultados positivos al 100 % en lugar del 50 % no se hubiera registrado tal defecto.
  - `e3` Obligacion: Consignación en partida 60500000 de porción para neutralización — De reunir los requisitos citados, se consignará en la partida 60500000 la porción pertinente para la neutralización del defecto generado.
  - `e4` Obligacion: Consignación de número y fecha de Resolución A 6456 — Se consignará como número y fecha de Resolución la de la Comunicación A 6456.
  - `e5` Obligacion: Descripción detallada del cálculo del importe — Se agregará una descripción detallada del cálculo del importe para el período informado.
  - `e6` Comunicacion: Com. A 6456 — 
  - `e7` Excepcion: Defectos no constituyen incumplimientos si se verifican condiciones — Los defectos originados en el cómputo del 50 % en lugar del 100 % de los resultados provenientes de los ajustes NIIF no constituirán incumplimientos si se verifican las condiciones especificadas.
- relaciones del crudo (sin establecida_en ni de sujeto): e1 condicion_de e7; e2 condicion_de e7; to referencia e6
- NODOS A CLASIFICAR:
  - **caso 70** Excepcion `e7`: Defectos no constituyen incumplimientos si se verifican condiciones | descripcion: Los defectos originados en el cómputo del 50 % en lugar del 100 % de los resultados provenientes de los ajustes NIIF no constituirán incumplimientos si se verifican las condiciones especificadas. | tramo: Estos defectos se consideran admitidos (es decir que no constituirán incumplimientos) de verificarse las siguientes condiciones

## Unidad `ext::10.3.5::intro` (intro)
- herencia: [encabezado 10.3.5] 10.3.5. Pagos de importaciones de bienes ingresadas desde zonas francas con transferencia
- texto propio: aduanera de dominio del exportador al importador.
La entidad interviniente podrá dar acceso al mercado de cambios para el pago al
exterior de importaciones de bienes ingresadas desde zonas francas con
transferencia aduanera de dominio del exportador al importador en la medida que
verifique previamente que se cumplen la totalidad de requisitos detallados en el punto
10.3.2., reemplazando lo requerido en los incisos i), iii) y iv) del punto 10.3.2.1. por lo
siguiente:
- entidades de la unidad:
  - `e1` Operacion: Acceso al mercado de cambios para pago de importaciones desde zonas francas — Acceso al mercado de cambios para el pago al exterior de importaciones de bienes ingresadas desde zonas francas con transferencia aduanera de dominio del exportador al importador
  - `e2` Condicion: Verificación previa de requisitos del punto 10.3.2 — Se cumplen la totalidad de requisitos detallados en el punto 10.3.2, con la sustitución de lo requerido en los incisos i), iii) y iv) del punto 10.3.2.1 por lo siguiente
  - `e3` Excepcion: Sustitución de incisos i), iii) y iv) del punto 10.3.2.1 — Los incisos i), iii) y iv) del punto 10.3.2.1 quedan reemplazados por requisitos distintos para el acceso al mercado de cambios en importaciones desde zonas francas
  - `e4` Potestad: Facultad de dar acceso al mercado de cambios — La entidad interviniente tiene la facultad de dar acceso al mercado de cambios para el pago al exterior de importaciones de bienes ingresadas desde zonas francas con transferencia aduanera, sujeto a v
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 71** Excepcion `e3`: Sustitución de incisos i), iii) y iv) del punto 10.3.2.1 | descripcion: Los incisos i), iii) y iv) del punto 10.3.2.1 quedan reemplazados por requisitos distintos para el acceso al mercado de cambios en importaciones desde zonas francas | tramo: reemplazando lo requerido en los incisos i), iii) y iv) del punto 10.3.2.1. por lo siguiente:

## Unidad `cla::7.2.1` (punto_no_item)
- herencia: [encabezado 7.2] 7.2. Niveles de clasificación.
- texto propio: 7.2.1. Situación normal.
Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con
atrasos que no superan los 31 días.
Los adelantos transitorios en cuenta corriente se considerarán de cumplimiento normal
hasta los 61 días contados desde su otorgamiento.
A los fines de establecer los días de atraso, en el caso de las financiaciones instrumenta-
das mediante tarjetas de crédito, se considerarán los que resulten luego de imputar el
pago mínimo exigido en cada liquidación a cancelar la deuda en orden decreciente de an-
tigüedad.
Los deudores que hayan accedido a refinanciaciones de deudas encontrándose clasifica-
dos en niveles inferiores, sólo podrán incluirse en esta categoría en la medida en que se
hayan observado las pautas establecidas para cada uno de los correspondientes niveles
y, además, que el resto de sus deudas reúnan las condiciones para que el cliente pueda
ser recategorizado en este nivel.
Los deudores que hayan refinanciado sus deudas, aun no habiendo incurrido en atrasos
en el pago de sus servicios, podrán permanecer en esta categoría, cuando hayan accedi-
do, como máximo, a dos refinanciaciones, en el término de 12 meses, contados desde la
última refinanciación otorgada.
A esos efectos, no se considerará refinanciación la asistencia que se otorgue a los deu-
dores clasificados en esta categoría siempre que implique mayor deuda por capital –neto
de los intereses y accesorios que se capitalicen– respecto del importe adeudado con an-
terioridad por el mismo concepto y que se evalúe la capacidad de pago del deudor para
afrontar las obligaciones emergentes de esa ampliación del margen crediticio.
Los sobregiros en cuenta corriente bancaria por importes que excedan los márgenes de
utilización oportunamente acordados, o los que se ha
- entidades de la unidad:
  - `e1` Definicion: Situación normal — deudores — Categoría de clasificación que comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días.
  - `e2` Condicion: Atraso máximo 31 días — El cliente debe tener atrasos que no superen los 31 días para ser clasificado en situación normal.
  - `e3` Definicion: Adelantos transitorios — cumplimiento normal — Se considerarán de cumplimiento normal hasta los 61 días contados desde su otorgamiento.
  - `e4` Condicion: Plazo 61 días — adelantos transitorios — Los adelantos transitorios en cuenta corriente se consideran de cumplimiento normal dentro de este plazo.
  - `e5` Obligacion: Cálculo de atraso — tarjetas de crédito — Para financiaciones mediante tarjetas de crédito, los días de atraso se establecen considerando los que resulten luego de imputar el pago mínimo exigido en cada liquidación a cancelar la deuda en orde
  - `e6` Condicion: Refinanciación previa — recategorización — Para que deudores previamente clasificados en niveles inferiores puedan incluirse en situación normal tras refinanciación, deben haber observado las pautas de cada nivel y el resto de sus deudas debe 
  - `e7` Condicion: Máximo dos refinanciaciones en 12 meses — Deudores que refinanciaron sin incurrir en atrasos pueden permanecer en situación normal si accedieron a como máximo dos refinanciaciones en el término de 12 meses.
  - `e8` Excepcion: Excepción — ampliación de margen crediticio — No se considera refinanciación la asistencia a deudores en situación normal que implique mayor deuda por capital (neto de intereses y accesorios capitalizados) respecto del importe anterior, siempre q
  - `e9` Condicion: Condición — mayor deuda por capital — La asistencia debe implicar mayor deuda por capital (neto de intereses y accesorios capitalizados) respecto del importe anterior.
  - `e10` Condicion: Condición — evaluación de capacidad de pago — Debe evaluarse la capacidad de pago del deudor para afrontar las obligaciones emergentes de la ampliación del margen crediticio.
  - `e11` Excepcion: Excepción — sobregiros en cuenta corriente — Los sobregiros en cuenta corriente bancaria que excedan márgenes acordados o sin margen asignado no se consideran refinanciación si se cancelan dentro de 30 días.
  - `e12` Restriccion: Reclasificación — refinanciación en condiciones distintas — Si se verifican refinanciaciones en condiciones distintas a las excepciones señaladas, corresponderá la reclasificación del deudor como mínimo en el nivel inmediato inferior.
  - `e13` Operacion: Reclasificación de deudor — Cambio de categoría de clasificación del deudor a un nivel inmediato inferior cuando se verifican refinanciaciones en condiciones distintas a las permitidas.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1; e4 condicion_de e3; e6 condicion_de e1; e7 condicion_de e1; e9 condicion_de e8; e10 condicion_de e8; e12 limita e13
- NODOS A CLASIFICAR:
  - **caso 72** Excepcion `e11`: Excepción — sobregiros en cuenta corriente | descripcion: Los sobregiros en cuenta corriente bancaria que excedan márgenes acordados o sin margen asignado no se consideran refinanciación si se cancelan dentro de 30 días. | tramo: Los sobregiros en cuenta corriente bancaria por importes que excedan los márgenes de utilización oportunamente acordados, o los que se hayan efectivizado –cualquiera sea su importe– sin contar el cuentacorrentista con un margen previa y expresamente asignado, tampoco serán considerados refinanciación siempre que tales excesos se cancelen dentro de los 30 días.
  - **caso 86** Excepcion `e8`: Excepción — ampliación de margen crediticio | descripcion: No se considera refinanciación la asistencia a deudores en situación normal que implique mayor deuda por capital (neto de intereses y accesorios capitalizados) respecto del importe anterior, siempre que se evalúe la capacidad de pago del deudor. | tramo: A esos efectos, no se considerará refinanciación la asistencia que se otorgue a los deudores clasificados en esta categoría siempre que implique mayor deuda por capital –neto de los intereses y accesorios que se capitalicen– respecto del importe adeudado con anterioridad por el mismo concepto y que se evalúe la capacidad de pago del deudor para afrontar las obligaciones emergentes de esa ampliación del margen crediticio.

## Unidad `ctacte::1.5.2.9` (punto_no_item)
- herencia: [intro 1.5] En sus cláusulas se deberá prever, como mínimo: | [encabezado 1.5.2] 1.5.2. Obligaciones de la entidad.
- texto propio: 1.5.2.9. Constatar –tanto en los cheques librados en formato papel como en los certifica-
dos nominativos transferibles– la regularidad de la serie de endosos pero no la
autenticidad de la firma de los endosantes y verificar la firma del presentante,
que deberá insertarse con carácter de recibo.
Estas obligaciones recaen sobre la entidad girada cuando el cheque se presen-
te para el cobro en ella, en tanto que a la entidad en que se deposita el cheque
–cuando sea distinta de la girada– le corresponde controlar que la última firma
extendida en carácter de recibo contenga las especificaciones fijadas en el pun-
to 5.1.3., salvo que resulte aplicable el procedimiento de truncamiento, en cuyo
caso se estará a lo previsto en los respectivos convenios.
Cuando la presentación se efectúe a través de mandatario o beneficiario de una
cesión ordinaria, deberá verificarse además el instrumento por el cual se haya
otorgado el mandato o efectuado la cesión, excepto cuando la gestión de cobro
sea realizada por una entidad financiera no autorizada a captar depósitos en
cuenta corriente.
- entidades de la unidad:
  - `e1` Operacion: Constatar regularidad de serie de endosos — Constatar la regularidad de la serie de endosos en cheques librados en formato papel y en certificados nominativos transferibles
  - `e2` Restriccion: No verificar autenticidad de firma de endosantes — No verificar la autenticidad de la firma de los endosantes
  - `e3` Operacion: Verificar firma del presentante como recibo — Verificar la firma del presentante, que deberá insertarse con carácter de recibo
  - `e4` Obligacion: Obligación de constatar y verificar — entidad girada — La entidad girada debe constatar la regularidad de la serie de endosos y verificar la firma del presentante cuando el cheque se presente para el cobro en ella
  - `e5` Obligacion: Controlar última firma de recibo — entidad depositaria — La entidad en que se deposita el cheque, cuando sea distinta de la girada, debe controlar que la última firma extendida en carácter de recibo contenga las especificaciones fijadas en el punto 5.1.3.
  - `e6` Excepcion: Excepción — procedimiento de truncamiento — No aplica la obligación de controlar la última firma de recibo cuando resulte aplicable el procedimiento de truncamiento; en ese caso se estará a lo previsto en los respectivos convenios
  - `e7` Obligacion: Verificar instrumento de mandato o cesión — Cuando la presentación se efectúe a través de mandatario o beneficiario de una cesión ordinaria, debe verificarse el instrumento por el cual se haya otorgado el mandato o efectuado la cesión
  - `e8` Excepcion: Excepción — entidad financiera no autorizada a captar depósitos — No se requiere verificar el instrumento de mandato o cesión cuando la gestión de cobro sea realizada por una entidad financiera no autorizada a captar depósitos en cuenta corriente
  - `e9` Condicion: Condición — presentación a través de mandatario o cesionario — La obligación de verificar el instrumento de mandato o cesión se activa cuando la presentación se efectúe a través de mandatario o beneficiario de una cesión ordinaria
- relaciones del crudo (sin establecida_en ni de sujeto): e8 exceptua_obligacion e7; e9 condicion_de e7
- NODOS A CLASIFICAR:
  - **caso 73** Excepcion `e6`: Excepción — procedimiento de truncamiento | descripcion: No aplica la obligación de controlar la última firma de recibo cuando resulte aplicable el procedimiento de truncamiento; en ese caso se estará a lo previsto en los respectivos convenios | tramo: salvo que resulte aplicable el procedimiento de truncamiento, en cuyo caso se estará a lo previsto en los respectivos convenios

## Unidad `ext::3.16.3.5` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.16.3] operaciones con títulos valores y otros activos.
En el caso de que el cliente no sea una persona humana residente, la entidad deberá
contar con la conformidad previa del BCRA excepto que cuente con una declaración
jurada del cliente en la que deje constancia de que: | **[abre la lista]** [intersticial 3.16.3] En caso de que el cliente sea una persona jurídica, para que la operación no quede
comprendida por el requisito de conformidad previa, la entidad deberá contar
adicionalmente con una declaración jurada en la que conste:
- texto propio: 3.16.3.5. Lo previsto en los puntos 3.16.3.1. al 3.16.3.4. no resultará aplicable para
aquellas operaciones de egresos que correspondan a:
i) operaciones de clientes realizadas en el marco del punto 3.14.2.
ii) cancelaciones de financiaciones en moneda extranjera otorgadas por
entidades financieras locales, incluyendo los pagos por los consumos
en moneda extranjera efectuados mediante tarjetas de crédito o de
compra;
iii) operaciones comprendidas en el punto 3.13.1.4. en la medida que las
mismas sean cursadas en forma automática por la entidad en su
carácter de apoderada del beneficiario no residente.
iv) las repatriaciones de inversiones de portafolio de no residentes
cursadas en el marco de lo dispuesto en el punto 3.13.1.12.
Las entidades por sus operaciones propias en carácter de cliente deberán
dar cumplimiento sólo a lo previsto en los puntos 3.16.3.3. y 3.16.3.4.
- entidades de la unidad:
  - `e1` Excepcion: Excepción — operaciones punto 3.14.2 — No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para operaciones de clientes realizadas en el marco del punto 3.14.2
  - `e2` Excepcion: Excepción — cancelaciones de financiaciones en moneda extranjera — No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para cancelaciones de financiaciones en moneda extranjera otorgadas por entidades financieras locales, incluyendo pago
  - `e3` Excepcion: Excepción — operaciones punto 3.13.1.4 cursadas automáticamente — No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para operaciones del punto 3.13.1.4 cursadas automáticamente por la entidad como apoderada del beneficiario no residen
  - `e4` Excepcion: Excepción — repatriaciones de inversiones de portafolio — No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para repatriaciones de inversiones de portafolio de no residentes cursadas conforme al punto 3.13.1.12
  - `e5` Obligacion: Cumplimiento parcial — operaciones propias de entidades — Las entidades, por sus operaciones propias en carácter de cliente, deben cumplir solo con lo previsto en los puntos 3.16.3.3 y 3.16.3.4, quedando exceptuadas de los requisitos de los puntos 3.16.3.1 y
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 74** Excepcion `e1`: Excepción — operaciones punto 3.14.2 | descripcion: No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para operaciones de clientes realizadas en el marco del punto 3.14.2 | tramo: Lo previsto en los puntos 3.16.3.1. al 3.16.3.4. no resultará aplicable para aquellas operaciones de egresos que correspondan a: i) operaciones de clientes realizadas en el marco del punto 3.14.2.
  - **caso 75** Excepcion `e3`: Excepción — operaciones punto 3.13.1.4 cursadas automáticamente | descripcion: No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para operaciones del punto 3.13.1.4 cursadas automáticamente por la entidad como apoderada del beneficiario no residente | tramo: Lo previsto en los puntos 3.16.3.1. al 3.16.3.4. no resultará aplicable para aquellas operaciones de egresos que correspondan a: iii) operaciones comprendidas en el punto 3.13.1.4. en la medida que las mismas sean cursadas en forma automática por la entidad en su carácter de apoderada del beneficiario no residente.
  - **caso 76** Excepcion `e2`: Excepción — cancelaciones de financiaciones en moneda extranjera | descripcion: No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para cancelaciones de financiaciones en moneda extranjera otorgadas por entidades financieras locales, incluyendo pagos por consumos en moneda extranjera mediante tarjetas de crédito o de compra | tramo: Lo previsto en los puntos 3.16.3.1. al 3.16.3.4. no resultará aplicable para aquellas operaciones de egresos que correspondan a: ii) cancelaciones de financiaciones en moneda extranjera otorgadas por entidades financieras locales, incluyendo los pagos por los consumos en moneda extranjera efectuados mediante tarjetas de crédito o de compra;
  - **caso 77** Excepcion `e4`: Excepción — repatriaciones de inversiones de portafolio | descripcion: No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para repatriaciones de inversiones de portafolio de no residentes cursadas conforme al punto 3.13.1.12 | tramo: Lo previsto en los puntos 3.16.3.1. al 3.16.3.4. no resultará aplicable para aquellas operaciones de egresos que correspondan a: iv) las repatriaciones de inversiones de portafolio de no residentes cursadas en el marco de lo dispuesto en el punto 3.13.1.12.

## Unidad `ext::3.16.3.7` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.16.3] operaciones con títulos valores y otros activos.
En el caso de que el cliente no sea una persona humana residente, la entidad deberá
contar con la conformidad previa del BCRA excepto que cuente con una declaración
jurada del cliente en la que deje constancia de que: | **[abre la lista]** [intersticial 3.16.3] En caso de que el cliente sea una persona jurídica, para que la operación no quede
comprendida por el requisito de conformidad previa, la entidad deberá contar
adicionalmente con una declaración jurada en la que conste:
- texto propio: 3.16.3.7. La entidad también podrá considerar cumplimentado lo indicado en los
puntos 3.16.3.3. y 3.16.3.4. cuando:
i) el cliente haya presentado una declaración jurada dejando constancia
de que en el plazo previsto en el punto 3.16.3.4., salvo por aquellos
directamente asociados a operaciones habituales en el marco del
desarrollo de su actividad, no ha entregado en el país fondos en
moneda local ni otros activos locales líquidos -excepto fondos en
moneda extranjera depositados en entidades financieras locales- a
ninguna persona humana o jurídica,
ii) el cliente haya presentado una declaración jurada rubricada por cada
persona humana o jurídica detallada en el punto 3.16.3.3. a la cual el
cliente le haya entregado fondos en los términos previstos en el punto
3.16.3.4., dejando constancia de lo requerido en los puntos 3.16.3.1.,
3.16.3.2. y 3.16.3.4.
iii)el cliente haya presentado una declaración jurada rubricada por cada
persona humana o jurídica detallada en el punto 3.16.3.3., en la cual
deje constancia de que:
a)que cumple lo requerido en los puntos 3.16.3.1. y 3.16.3.2.; o
b) que en el plazo previsto en el punto 3.16.3.4., salvo por aquellos
directamente asociados a operaciones habituales entre residentes
de adquisición de bienes y/o servicios, no ha recibido en el país
fondos en moneda local ni otros activos locales líquidos -excepto
fondos en moneda extranjera depositados en entidades
financieras locales- que hayan provenido del cliente o de alguna
persona detallada en el punto 3.16.3.3. a la cual el cliente le haya
entregado fondos en los términos previstos en el punto 3.16.3.4.
En caso de que alguna de las personas detallada en el punto 3.16.3.3. sea
un ente perteneciente al sector público nacional, no será necesaria la
presentación por parte de ese ente de la d
- entidades de la unidad:
  - `e1` Operacion: Cumplimiento de requisitos 3.16.3.3 y 3.16.3.4 — Consideración de cumplimiento de los requisitos indicados en los puntos 3.16.3.3. y 3.16.3.4. cuando se verifican las condiciones enumeradas en los incisos i), ii) o iii).
  - `e2` Condicion: Declaración jurada cliente — fondos no entregados — El cliente ha presentado declaración jurada acreditando que, en el plazo del punto 3.16.3.4., salvo fondos asociados a operaciones habituales de su actividad, no ha entregado en el país fondos en mone
  - `e3` Condicion: Declaración jurada rubricada — personas receptoras de fondos — El cliente ha presentado declaración jurada rubricada por cada persona humana o jurídica (detallada en punto 3.16.3.3.) a la cual le entregó fondos, dejando constancia de lo requerido en los puntos 3.
  - `e4` Condicion: Declaración jurada rubricada — cumplimiento o no recepción de fondos — El cliente ha presentado declaración jurada rubricada por cada persona humana o jurídica (detallada en punto 3.16.3.3.) en la cual consta: (a) que cumple lo requerido en puntos 3.16.3.1. y 3.16.3.2.; 
  - `e5` Excepcion: Excepción — entes sector público nacional — No es necesaria la presentación de declaración jurada por parte de entes del sector público nacional detallados en punto 3.16.3.3. para considerar cumplimentado lo requerido en los incisos ii) o iii).
  - `e6` Excepcion: Excepción — entes sector público nacional (inciso iii) — No es necesaria la presentación de declaración jurada por parte de entes del sector público nacional detallados en punto 3.16.3.3. para considerar cumplimentado lo requerido en los incisos ii) o iii).
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 79** Excepcion `e5`: Excepción — entes sector público nacional | descripcion: No es necesaria la presentación de declaración jurada por parte de entes del sector público nacional detallados en punto 3.16.3.3. para considerar cumplimentado lo requerido en los incisos ii) o iii). | tramo: En caso de que alguna de las personas detallada en el punto 3.16.3.3. sea un ente perteneciente al sector público nacional, no será necesaria la presentación por parte de ese ente de la declaración jurada requerida en los puntos ii) o iii) precedentes para considerar cumplimentado lo requerido.
  - **caso 168** Condicion `e2`: Declaración jurada cliente — fondos no entregados | descripcion: El cliente ha presentado declaración jurada acreditando que, en el plazo del punto 3.16.3.4., salvo fondos asociados a operaciones habituales de su actividad, no ha entregado en el país fondos en moneda local ni otros activos locales líquidos (excepto fondos en moneda extranjera en entidades financieras locales) a ninguna persona. | tramo: el cliente haya presentado una declaración jurada dejando constancia de que en el plazo previsto en el punto 3.16.3.4., salvo por aquellos directamente asociados a operaciones habituales en el marco del desarrollo de su actividad, no ha entregado en el país fondos en moneda local ni otros activos locales líquidos -excepto fondos en moneda extranjera depositados en entidades financieras locales- a ninguna persona humana o jurídica
  - **caso 169** Condicion `e4`: Declaración jurada rubricada — cumplimiento o no recepción de fondos | descripcion: El cliente ha presentado declaración jurada rubricada por cada persona humana o jurídica (detallada en punto 3.16.3.3.) en la cual consta: (a) que cumple lo requerido en puntos 3.16.3.1. y 3.16.3.2.; o (b) que en el plazo del punto 3.16.3.4., salvo fondos asociados a operaciones habituales entre residentes de adquisición de bienes/servicios, no ha recibido en el país fondos en moneda local ni otros activos locales líquidos (excepto fondos en moneda extranjera en entidades financieras locales) provenientes del cliente o de personas a las cuales el cliente entregó fondos. | tramo: el cliente haya presentado una declaración jurada rubricada por cada persona humana o jurídica detallada en el punto 3.16.3.3., en la cual deje constancia de que: a)que cumple lo requerido en los puntos 3.16.3.1. y 3.16.3.2.; o b) que en el plazo previsto en el punto 3.16.3.4., salvo por aquellos directamente asociados a operaciones habituales entre residentes de adquisición de bienes y/o servicios, no ha recibido en el país fondos en moneda local ni otros activos locales líquidos -excepto fondos en moneda extranjera depositados en entidades financieras locales- que hayan provenido del cliente o de alguna persona detallada en el punto 3.16.3.3. a la cual el cliente le haya entregado fondos en los términos previstos en el punto 3.16.3.4.
  - **caso 170** Condicion `e3`: Declaración jurada rubricada — personas receptoras de fondos | descripcion: El cliente ha presentado declaración jurada rubricada por cada persona humana o jurídica (detallada en punto 3.16.3.3.) a la cual le entregó fondos, dejando constancia de lo requerido en los puntos 3.16.3.1., 3.16.3.2. y 3.16.3.4. | tramo: el cliente haya presentado una declaración jurada rubricada por cada persona humana o jurídica detallada en el punto 3.16.3.3. a la cual el cliente le haya entregado fondos en los términos previstos en el punto 3.16.3.4., dejando constancia de lo requerido en los puntos 3.16.3.1., 3.16.3.2. y 3.16.3.4.

## Unidad `cla::1.2.2` (punto_no_item)
- herencia: [encabezado 1.2] 1.2. Criterios especiales de imputación.
- texto propio: 1.2.2. Deudores en concurso preventivo.
En el caso de deudores que hayan solicitado su concurso preventivo, los créditos que les
sean otorgados con posterioridad a ese pedido, en la medida que cuenten con garantías
de terceros que permitan su cobro al vencimiento sin necesidad de la intervención del
cliente en concurso, a los fines de esta clasificación podrán imputarse -a opción de la
entidad- al tercero constituido en principal o directo pagador o avalista o codeudor que
haya renunciado al beneficio de excusión.
Igual temperamento podrá observarse cuando se trate de créditos respecto de documen-
tos o valores cedidos por el deudor en concurso que puedan considerarse garantías pre-
feridas “A” por ser cobrables directamente del tercero responsable del documento (por
ejemplo: facturas de crédito, facturas a consumidores emitidas por empresas de servicios
públicos proveedoras de electricidad, gas, etc., cupones de tarjetas de crédito, etc.). En
los casos de deudores por servicios públicos o por tarjetas de crédito, no será obligatoria
la apertura del legajo.
- entidades de la unidad:
  - `e1` Operacion: Otorgamiento de créditos a deudor en concurso preventivo — Créditos otorgados a deudores que hayan solicitado concurso preventivo, con posterioridad a ese pedido, que cuenten con garantías de terceros que permitan su cobro al vencimiento sin necesidad de la i
  - `e2` Potestad: Opción de imputación a tercero — créditos en concurso — La entidad tiene la opción de imputar los créditos otorgados a deudor en concurso preventivo al tercero constituido en principal o directo pagador o avalista o codeudor que haya renunciado al benefici
  - `e3` Condicion: Garantías de terceros que permitan cobro al vencimiento — Los créditos deben contar con garantías de terceros que permitan su cobro al vencimiento sin necesidad de la intervención del cliente en concurso.
  - `e4` Operacion: Créditos sobre documentos o valores cedidos por deudor en concurso — Créditos respecto de documentos o valores cedidos por el deudor en concurso que puedan considerarse garantías preferidas "A" por ser cobrables directamente del tercero responsable del documento (por e
  - `e5` Potestad: Opción de imputación a tercero — créditos sobre documentos cedidos — La entidad tiene la opción de observar igual temperamento (imputar al tercero responsable) cuando se trate de créditos respecto de documentos o valores cedidos por el deudor en concurso que puedan con
  - `e6` Excepcion: No obligatoriedad de apertura de legajo — deudores por servicios públicos o tarjetas — No es obligatoria la apertura del legajo en los casos de deudores por servicios públicos o por tarjetas de crédito.
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 81** Excepcion `e6`: No obligatoriedad de apertura de legajo — deudores por servicios públicos o tarjetas | descripcion: No es obligatoria la apertura del legajo en los casos de deudores por servicios públicos o por tarjetas de crédito. | tramo: En los casos de deudores por servicios públicos o por tarjetas de crédito, no será obligatoria la apertura del legajo.

## Unidad `cla::3.4.2` (punto_no_item)
- herencia: [encabezado 3.4] 3.4. Legajo del cliente.
- texto propio: 3.4.2. Contenido.
En el legajo se reunirán todos los elementos de juicio que se tengan en cuenta para rea-
lizar las evaluaciones y clasificaciones y se dejará constancia de las revisiones efectua-
das y de la clasificación asignada.
Cuando no corresponda evaluar la capacidad de repago del deudor por encontrarse la
deuda cubierta con garantías preferidas “A”, según lo previsto en el punto 4.4., no será
obligatorio incorporar al legajo del cliente el flujo de fondos, los estados contables ni toda
otra información necesaria para efectuar ese análisis.
A los fines de la actualización del legajo del cliente, se admitirá que la clasificación asig-
nada se mantenga en planillas separadas, siempre que el procedimiento adoptado –que
deberá estar descripto en el “Manual de procedimientos de clasificación y previsión”–
permita la identificación precisa de la clasificación asignada a cada cliente desde la plani-
lla al legajo y viceversa.
Dicho legajo deberá contar con información acerca de los márgenes crediticios, discrimi-
nado –de corresponder– por tipo o línea, conforme al punto 1.1.3.2., acápite ii) del TO
sobre Gestión Crediticia.
Las entidades financieras deberán comunicar a los deudores los cambios negativos en la
clasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al
monto establecido en el punto 2. “Deudores Comprendidos” de la Sección 3. “Deudores
del sistema financiero” –Normas de Procedimiento– del Régimen Informativo Contable
Mensual.
Deberán informarse los cambios negativos en la clasificación a los deudores que sean
clasificados en las situaciones 3, 4 o 5 y de los deudores en gestión judicial o extrajudi-
cial de cobro (estos últimos, en la medida que cuenten con notificaciones postales o
fehacientes respecto al inicio de las ge
- entidades de la unidad:
  - `e1` Obligacion: Reunir elementos de juicio en legajo — Reunir en el legajo todos los elementos de juicio para evaluaciones y clasificaciones, dejando constancia de revisiones y clasificación asignada.
  - `e2` Excepcion: Excepción — información no obligatoria con garantías preferidas A — No es obligatorio incorporar flujo de fondos, estados contables ni información para análisis de capacidad de repago cuando la deuda está cubierta con garantías preferidas A.
  - `e3` Obligacion: Permitir clasificación en planillas separadas con procedimiento descrito — Se admite mantener la clasificación en planillas separadas si el procedimiento (descrito en Manual de procedimientos) permite identificar precisamente la clasificación de cada cliente entre planilla y
  - `e4` Obligacion: Incluir información de márgenes crediticios en legajo — El legajo debe incluir información sobre márgenes crediticios, discriminados por tipo o línea según corresponda, conforme a normas de Gestión Crediticia.
  - `e5` Obligacion: Comunicar cambios negativos en clasificación a deudores — Comunicar a los deudores los cambios negativos en su clasificación; es optativo cuando el saldo de deuda sea inferior al monto establecido en el Régimen Informativo Contable Mensual.
  - `e6` Obligacion: Informar cambios negativos a deudores en situaciones 3, 4, 5 o en gestión de cobro — Informar cambios negativos en clasificación a deudores en situaciones 3, 4 o 5, y a deudores en gestión judicial o extrajudicial de cobro (si cuentan con notificaciones postales o fehacientes del inic
  - `e7` Obligacion: Remitir información de cambios dentro de 45 días por medios especificados — Remitir información de cambios negativos a deudores dentro de 45 días de la reclasificación, mediante: resumen impreso de movimientos, resumen de cuenta de tarjetas, recibo de pago, o correspondencia 
  - `e8` Obligacion: Informar a clientes por home banking en igual plazo — Las entidades financieras que ofrecen home banking deben informar a cada cliente por ese medio la información de cambios negativos en clasificación en igual plazo (45 días).
  - `e9` Obligacion: Mantener disponible saldo actualizado de financiaciones — Mantener disponible el saldo actualizado de todas las financiaciones otorgadas (incluyendo filiales y unidades operativas), discriminado por concepto, en el lugar del legajo o casa central según corre
  - `e10` Obligacion: Mantener declaración jurada sobre vinculación para clientes sector privado no financiero — Mantener en el legajo declaración jurada sobre vinculación e influencia controlante de clientes del sector privado no financiero cuya deuda total exceda del 2,5% de responsabilidad patrimonial computa
  - `e11` Obligacion: Incluir información de corresponsales en legajo — El legajo de corresponsales debe contener información sobre identificación, calificación, márgenes de crédito y datos vinculados a esa relación, conforme a normas de Cuentas de corresponsalía.
  - `e12` Obligacion: Constar análisis de graduación del crédito en legajos — Los legajos deben incluir los análisis realizados por aplicación de normas sobre graduación del crédito.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 82** Excepcion `e2`: Excepción — información no obligatoria con garantías preferidas A | descripcion: No es obligatorio incorporar flujo de fondos, estados contables ni información para análisis de capacidad de repago cuando la deuda está cubierta con garantías preferidas A. | tramo: Cuando no corresponda evaluar la capacidad de repago del deudor por encontrarse la deuda cubierta con garantías preferidas "A", según lo previsto en el punto 4.4., no será obligatorio incorporar al legajo del cliente el flujo de fondos, los estados contables ni toda otra información necesaria para efectuar ese análisis.

## Unidad `cap::10.2.2.6` (item)
- herencia: **[abre la lista]** [intro 10.2.2] Las ECAI deberán cumplir cada uno de los siguientes seis criterios:
- texto propio: 10.2.2.6. Credibilidad.
Las evaluaciones de crédito de las ECAI deben ser confiables para terceros
independientes. Además, la existencia de procedimientos internos destina-
dos a prevenir el uso indebido de información confidencial contribuye a la
credibilidad de una ECAI. Para ser reconocida, no es requisito que una ECAI
evalúe empresas en más de un país.
- entidades de la unidad:
  - `e1` Obligacion: Confiabilidad de evaluaciones de crédito — Las evaluaciones de crédito de las ECAI deben ser confiables para terceros independientes
  - `e2` Obligacion: Procedimientos internos para prevenir uso indebido de información — Existencia de procedimientos internos destinados a prevenir el uso indebido de información confidencial para contribuir a la credibilidad de una ECAI
  - `e3` Excepcion: No requisito de evaluación en múltiples países — No es requisito que una ECAI evalúe empresas en más de un país para ser reconocida
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 83** Excepcion `e3`: No requisito de evaluación en múltiples países | descripcion: No es requisito que una ECAI evalúe empresas en más de un país para ser reconocida | tramo: Para ser reconocida, no es requisito que una ECAI evalúe empresas en más de un país

## Unidad `ext::4.3.2::cierre` (cierre)
- herencia: [encabezado 4.3.2] 4.3.2. Las operaciones de compraventa de títulos valores con liquidación en moneda
- texto propio: En ningún caso se permite la liquidación de estas operaciones mediante el pago en
billetes en moneda extranjera o mediante su depósito en cuentas custodia o en
cuentas de terceros, excepto que se trate de operaciones contra cable que utilicen
cuentas de terceros en el marco de lo contemplado en el punto 4.3.2.3.
Los requisitos previstos en los puntos 4.3.2.1. y 4.3.2.2. no resultarán aplicables en las
compras de títulos valores que:
i) sean concretadas por los clientes con fondos en moneda extranjera recibidos en
los 15 (quince) días hábiles previos a partir del cobro de capital y/o intereses de
títulos de deuda emitidos por residentes; y
ii) la reinversión de los fondos por parte del beneficiario resulte neutra en materia
impositiva respecto de la operatoria de acreditación de los fondos en una cuenta
a la vista del beneficiario en una entidad financiera y su posterior débito para la
compra de valores.
- entidades de la unidad:
  - `e1` Restriccion: Prohibición liquidación en billetes o depósito custodia — Se prohíbe la liquidación de operaciones de compraventa de títulos valores con liquidación en moneda mediante el pago en billetes en moneda extranjera o mediante su depósito en cuentas custodia o en c
  - `e2` Excepcion: Excepción operaciones contra cable con cuentas de terceros — Quedan exceptuadas de la prohibición de liquidación mediante depósito en cuentas de terceros las operaciones contra cable que utilicen cuentas de terceros conforme a lo previsto en el punto 4.3.2.3.
  - `e3` Excepcion: Excepción compras con fondos recibidos por cobro de títulos — No resultan aplicables los requisitos de los puntos 4.3.2.1 y 4.3.2.2 en las compras de títulos valores concretadas por los clientes con fondos en moneda extranjera recibidos en los 15 días hábiles pr
  - `e4` Condicion: Condición reinversión neutra en materia impositiva — La reinversión de los fondos por parte del beneficiario debe resultar neutra en materia impositiva respecto de la operatoria de acreditación de los fondos en una cuenta a la vista del beneficiario en 
- relaciones del crudo (sin establecida_en ni de sujeto): e2 exceptua e1; e4 condicion_de e3
- NODOS A CLASIFICAR:
  - **caso 84** Excepcion `e3`: Excepción compras con fondos recibidos por cobro de títulos | descripcion: No resultan aplicables los requisitos de los puntos 4.3.2.1 y 4.3.2.2 en las compras de títulos valores concretadas por los clientes con fondos en moneda extranjera recibidos en los 15 días hábiles previos al cobro de capital y/o intereses de títulos de deuda emitidos por residentes. | tramo: Los requisitos previstos en los puntos 4.3.2.1. y 4.3.2.2. no resultarán aplicables en las compras de títulos valores que: i) sean concretadas por los clientes con fondos en moneda extranjera recibidos en los 15 (quince) días hábiles previos a partir del cobro de capital y/o intereses de títulos de deuda emitidos por residentes

## Unidad `ext::3.16.2.1` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | **[abre la lista]** [intro 3.16.2] y/o certificados de depósitos argentinos representativos de acciones extranjeras.
La entidad deberá contar con la conformidad previa del BCRA excepto que cuente al
momento de acceso al mercado de cambios con una declaración jurada del cliente en
la que deje constancia de que: | [cierre 3.16.2] Este requisito no resultará a aplicación para aquellas operaciones de egresos que
correspondan a: | [cierre 3.16.2] i) operaciones de clientes realizadas en el marco de los puntos 3.8., 3.9., 3.13., | [cierre 3.16.2] 3.14.1. y 3.14.2.; | [cierre 3.16.2] ii) operaciones propias de una entidad en carácter de cliente;
iii) cancelaciones de financiaciones en moneda extranjera otorgadas por entidades | [cierre 3.16.2] financieras locales por los consumos en moneda extranjera efectuados
mediante tarjetas de crédito o de compra; o | [cierre 3.16.2] iv) pagos al exterior de las empresas no financieras emisoras de tarjetas por el uso | [cierre 3.16.2] de tarjetas de crédito, de compra, de débito o prepagas emitidas en el país.
- texto propio: 3.16.2.1. La totalidad de sus tenencias de moneda extranjera en el país se
encuentran depositadas en cuentas en entidades financieras y que no
poseía, al inicio del día en que solicita el acceso al mercado, certificados de
depósitos argentinos representativos de acciones extranjeras (CEDEARs)
y/o activos externos líquidos disponibles que conjuntamente tengan un
valor superior al equivalente de USD 100.000 (dólares estadounidenses
cien mil).
Serán considerados activos externos líquidos, entre otros: las tenencias de
billetes y monedas en moneda extranjera, disponibilidades en oro
amonedado o en barras de buena entrega, depósitos a la vista en
entidades financieras del exterior y otras inversiones que permitan obtener
disponibilidad inmediata de moneda extranjera (por ejemplo, inversiones en
títulos públicos externos con custodia en el país o en el exterior, fondos en
cuentas de inversión en administradores de inversiones radicados en el
exterior, criptoactivos, fondos en cuentas de proveedores de servicios de
pago, etc.).
No deben considerarse activos externos líquidos disponibles a aquellos
fondos depositados en el exterior que no pudiesen ser utilizados por el
cliente por tratarse de fondos de reserva o de garantía constituidos en
virtud de las exigencias previstas en contratos de endeudamiento con el
exterior, prefinanciaciones de exportaciones comprendidas en el punto
7.8.5. o de fondos constituidos como garantía de operaciones con
derivados concertadas en el exterior.
En el caso de que el cliente tuviera activos externos líquidos disponibles y/o
CEDEARs por un monto superior al establecido en el primer párrafo, la
entidad también podrá aceptar una declaración jurada del cliente en la que
deje constancia que no se excede tal monto al considerar que, parcial o
totalme
- entidades de la unidad:
  - `c1` Condicion: Tenencias de moneda extranjera depositadas en entidades financieras — La totalidad de las tenencias de moneda extranjera en el país están depositadas en cuentas en entidades financieras
  - `c2` Condicion: Ausencia de CEDEARs y activos externos líquidos superiores a USD 100.000 — No posee, al inicio del día en que solicita acceso al mercado, CEDEARs y/o activos externos líquidos disponibles que conjuntamente superen USD 100.000
  - `d1` Definicion: Activos externos líquidos — Tenencias de billetes y monedas en moneda extranjera, disponibilidades en oro amonedado o en barras de buena entrega, depósitos a la vista en entidades financieras del exterior e inversiones que permi
  - `e0` Excepcion: Exclusión de fondos de reserva o garantía en el exterior — No se consideran activos externos líquidos disponibles los fondos depositados en el exterior que no puedan ser utilizados por el cliente por ser fondos de reserva o garantía constituidos en virtud de 
  - `p1` Potestad: Facultad de aceptar declaración jurada cuando activos externos líquidos superan USD 100.000 — Cuando el cliente tiene activos externos líquidos disponibles y/o CEDEARs por monto superior a USD 100.000, la entidad podrá aceptar una declaración jurada del cliente en la que conste que no se exced
  - `c3` Condicion: Activos utilizados durante la jornada para pagos en mercado local — Los activos externos líquidos fueron utilizados durante esa jornada para realizar pagos que hubieran tenido acceso al mercado local de cambios
  - `c4` Condicion: Activos transferidos a cuenta de corresponsalía — Los activos externos líquidos fueron transferidos a favor del cliente a una cuenta de corresponsalía de una entidad local autorizada a operar en cambios
  - `c5` Condicion: Fondos de cobros de exportaciones o enajenación de activos no financieros — Los fondos están depositados en cuentas bancarias en el exterior a nombre del cliente y se originan en cobros de exportaciones de bienes y/o servicios, anticipos, prefinanciaciones o posfinanciaciones
  - `c6` Condicion: Fondos de endeudamientos financieros punto 3.5 — Los fondos están depositados en cuentas bancarias en el exterior a nombre del cliente, se originan en endeudamientos financieros del punto 3.5. y su monto no supera el equivalente a pagar por capital 
  - `c7` Condicion: Fondos de desembolsos de endeudamientos últimos 180 días — Los fondos están depositados en cuentas bancarias en el exterior a nombre del cliente, se originan en desembolsos en el exterior recibidos a partir del 29/11/24 de endeudamientos financieros del punto
  - `c8` Condicion: Fondos de ventas de títulos valores con liquidación en moneda extranjera — Los fondos están depositados en cuentas bancarias en el exterior a nombre del cliente y se originan en ventas de títulos valores con liquidación en moneda extranjera del punto 3.16.3.6.iii)
  - `c9` Condicion: Fondos de emisiones de títulos de deuda últimos 120 días — Los fondos están depositados en cuentas bancarias en el exterior a nombre del cliente y se originan en emisiones de títulos de deuda concretadas en los 120 días corridos previos, susceptibles de ser e
  - `o1` Obligacion: Constar en declaración jurada valor de activos externos líquidos y montos asignados — En la declaración jurada del cliente deberá constar expresamente el valor de sus activos externos líquidos disponibles al inicio del día y los montos que asigna a cada una de las situaciones descripta
- relaciones del crudo (sin establecida_en ni de sujeto): c3 condicion_de p1; c4 condicion_de p1; c5 condicion_de p1; c6 condicion_de p1; c7 condicion_de p1; c8 condicion_de p1; c9 condicion_de p1; p1 requiere o1
- NODOS A CLASIFICAR:
  - **caso 87** Excepcion `e0`: Exclusión de fondos de reserva o garantía en el exterior | descripcion: No se consideran activos externos líquidos disponibles los fondos depositados en el exterior que no puedan ser utilizados por el cliente por ser fondos de reserva o garantía constituidos en virtud de exigencias de contratos de endeudamiento con el exterior, prefinanciaciones de exportaciones del punto 7.8.5. o fondos constituidos como garantía de operaciones con derivados en el exterior | tramo: No deben considerarse activos externos líquidos disponibles a aquellos fondos depositados en el exterior que no pudiesen ser utilizados por el cliente por tratarse de fondos de reserva o de garantía constituidos en virtud de las exigencias previstas en contratos de endeudamiento con el exterior, prefinanciaciones de exportaciones comprendidas en el punto 7.8.5. o de fondos constituidos como garantía de operaciones con derivados concertadas en el exterior
  - **caso 144** Condicion `c2`: Ausencia de CEDEARs y activos externos líquidos superiores a USD 100.000 | descripcion: No posee, al inicio del día en que solicita acceso al mercado, CEDEARs y/o activos externos líquidos disponibles que conjuntamente superen USD 100.000 | tramo: que no poseía, al inicio del día en que solicita el acceso al mercado, certificados de depósitos argentinos representativos de acciones extranjeras (CEDEARs) y/o activos externos líquidos disponibles que conjuntamente tengan un valor superior al equivalente de USD 100.000 (dólares estadounidenses cien mil)
  - **caso 248** Condicion `c1`: Tenencias de moneda extranjera depositadas en entidades financieras | descripcion: La totalidad de las tenencias de moneda extranjera en el país están depositadas en cuentas en entidades financieras | tramo: La totalidad de sus tenencias de moneda extranjera en el país se encuentran depositadas en cuentas en entidades financieras

## Unidad `ext::3.18.2.1` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | **[abre la lista]** [intro 3.18.2] exportador deberá nominar una única entidad financiera local que será la
responsable de emitir las correspondientes certificaciones y remitirlas a las entidades
por las cuales el cliente desee acceder al mercado.
La entidad nominada podrá emitir una “Certificación de aumento de las exportaciones
de bienes en el año t” cuando se verifiquen la totalidad de los siguientes requisitos:
- texto propio: 3.18.2.1. El valor FOB de las exportaciones de bienes comprendidos en los puntos
7.1.1.2. a 7.1.1.5. embarcados en el año t y que cuenten con una
certificación de cumplido en el marco del SECOEXPO, es superior al valor
FOB de sus exportaciones para ese mismo conjunto de bienes
embarcadas en todo el año t-1.
A los efectos de este cómputo no deberán considerarse los bienes
exportados a través de operaciones exceptuadas del seguimiento en virtud
de lo dispuesto en el punto 8.5.17., las exportaciones a consumo con
despacho de importación temporaria (DIT) o aquellos que cuenten con las
ventajas aduaneras “EXPONOTITONEROSO” o “PROMOEXPO”.
- entidades de la unidad:
  - `e1` Operacion: Exportación de bienes con certificación SECOEXPO — Exportación de bienes comprendidos en los puntos 7.1.1.2. a 7.1.1.5., embarcados en el año t, con certificación de cumplido en el marco del SECOEXPO
  - `e2` Condicion: Aumento FOB año t respecto a año t-1 — El valor FOB de las exportaciones en el año t es superior al valor FOB de las exportaciones del mismo conjunto de bienes en el año t-1
  - `e3` Excepcion: Exclusión operaciones exceptuadas punto 8.5.17 — No se consideran en el cómputo los bienes exportados a través de operaciones exceptuadas del seguimiento conforme al punto 8.5.17
  - `e4` Excepcion: Exclusión exportaciones DIT — No se consideran en el cómputo las exportaciones a consumo con despacho de importación temporaria (DIT)
  - `e5` Excepcion: Exclusión bienes con ventajas aduaneras EXPONOTITONEROSO o PROMOEXPO — No se consideran en el cómputo los bienes que cuenten con las ventajas aduaneras EXPONOTITONEROSO o PROMOEXPO
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 88** Excepcion `e4`: Exclusión exportaciones DIT | descripcion: No se consideran en el cómputo las exportaciones a consumo con despacho de importación temporaria (DIT) | tramo: las exportaciones a consumo con despacho de importación temporaria (DIT)
  - **caso 89** Excepcion `e3`: Exclusión operaciones exceptuadas punto 8.5.17 | descripcion: No se consideran en el cómputo los bienes exportados a través de operaciones exceptuadas del seguimiento conforme al punto 8.5.17 | tramo: no deberán considerarse los bienes exportados a través de operaciones exceptuadas del seguimiento en virtud de lo dispuesto en el punto 8.5.17.
  - **caso 90** Excepcion `e5`: Exclusión bienes con ventajas aduaneras EXPONOTITONEROSO o PROMOEXPO | descripcion: No se consideran en el cómputo los bienes que cuenten con las ventajas aduaneras EXPONOTITONEROSO o PROMOEXPO | tramo: aquellos que cuenten con las ventajas aduaneras "EXPONOTITONEROSO" o "PROMOEXPO"

## Unidad `ext::14.2.1.2` (item)
- herencia: [chapeau_seccion S14] En esta sección se detallan las disposiciones complementarias en materia cambiaria que, en la
medida que las disposiciones generales no resulten más favorables, resultan aplicables a un
Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo los referidas al “Régimen de
Incentivo para Grandes Inversiones” (RIGI) establecido en el Título VII de la Ley 27.742 y
reglamentado por el Decreto 749/24 y concordantes. | [intro 14.2] Adicionalmente lo previsto en la normativa general en materia de egresos por el mercado de
cambios, en la medida que se cumplan los restantes requisitos aplicables a cada operación,
por aquellas financiaciones o aportes de inversión directa recibidos por el VPU adherido a
partir de la vigencia de la Ley 27.742, las entidades podrán también dar acceso en las
siguientes situaciones: | **[abre la lista]** [intro 14.2.1] corresponda, sin necesidad de contar con la conformidad previa del BCRA si tal
requisito estuviese vigente, las entidades podrán darle acceso al cliente para pagar,
incluso antes de la fecha de vencimiento, los intereses devengados hasta la fecha
de acceso que se encuentren impagos y/o el capital pendiente de: | [cierre 14.2.1] En el caso de que la totalidad de los fondos obtenidos por la financiación no pudiese
ser computada como ingresada y liquidada en el mercado de cambios, las
entidades también podrán dar acceso al VPU adherido, sin necesidad de contar con
la conformidad previa del BCRA si tal requisito estuviese vigente, para realizar: | [cierre 14.2.1] i) pagos de intereses devengados hasta la fecha de acceso que se encuentren | [cierre 14.2.1] impagos y que correspondan a la porción del capital equivalente a la proporción
de los fondos recibidos por el VPU por la financiación que puede computarse
como ingresada y liquidada por el mercado de cambios. | [cierre 14.2.1] ii) pagos por capital adeudado que corresponda a la porción del capital | [cierre 14.2.1] equivalente a la proporción de los fondos recibidos por el VPU por la
financiación que puede computarse como ingresada y liquidada por el mercado
de cambios.
- texto propio: 14.2.1.2. emisiones de títulos de deuda con registro en el país suscriptos
íntegramente en el exterior y que fueron ingresados y liquidados en el
mercado de cambios.
- entidades de la unidad:
  - `e1` Operacion: Pago de intereses y capital — emisiones de títulos de deuda — Pago de intereses devengados hasta la fecha de acceso que se encuentren impagos y/o el capital pendiente de emisiones de títulos de deuda con registro en el país suscriptos íntegramente en el exterior
  - `e2` Potestad: Facultad de dar acceso al cliente para pagar — títulos de deuda — Las entidades quedan facultadas para dar acceso al cliente para pagar, incluso antes de la fecha de vencimiento, los intereses devengados hasta la fecha de acceso que se encuentren impagos y/o el capi
  - `e3` Excepcion: Excepción — conformidad previa del BCRA no requerida — No se requiere la conformidad previa del BCRA si tal requisito estuviese vigente para dar acceso al cliente para pagar intereses y capital de emisiones de títulos de deuda
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 92** Excepcion `e3`: Excepción — conformidad previa del BCRA no requerida | descripcion: No se requiere la conformidad previa del BCRA si tal requisito estuviese vigente para dar acceso al cliente para pagar intereses y capital de emisiones de títulos de deuda | tramo: sin necesidad de contar con la conformidad previa del BCRA si tal requisito estuviese vigente

## Unidad `cap::8.6.3` (item)
- herencia: **[abre la lista]** [intro 8.6] A los fines de todas las reglamentaciones vinculadas al capital, su integración y aumento, in-
clusive los referidos a planes de regularización y saneamiento y sin perjuicio de lo previsto en
los puntos 5.1. a 5.3. de las normas sobre “Autorización y composición del capital de entidades
financieras” en materia de negociación de acciones o de aportes irrevocables para futuros au-
mentos de capital, los aportes deben ser efectuados en efectivo.
Excepcionalmente, mediando autorización previa de la  | [cierre 8.6] En los casos comprendidos en los puntos 8.6.1. y 8.6.2., los aportes deberán registrarse a su
valor de mercado. Se entenderá que los instrumentos cuentan con valor de mercado cuando
tengan cotización habitual en las bolsas y mercados regulados del país o del exterior en los
que se negocien, con transacciones relevantes en cuyo monto, la eventual liquidación de las
tenencias no pueda distorsionar significativamente su cotización.
En los casos del punto 8.6.3., los aportes deberán registrarse a su | [cierre 8.6] n1 | [cierre 8.6] punto 8.3.4.
En ningún caso la capitalización de deuda podrá implicar una limitación o suspensión al dere-
cho de preferencia establecido en el artículo 194 de la Ley General de Sociedades, por lo que
no será aplicable lo dispuesto en el artículo 197 de dicha ley.
La decisión de capitalización de los conceptos indicados en los puntos 8.6.1. a 8.6.3. por parte
de la Asamblea (o autoridad equivalente) será “ad referéndum” de su aprobación por parte de
la SEFyC o, en su caso, del BCRA –puntos 5.1. 
- texto propio: 8.6.3. depósitos y otras obligaciones por intermediación financiera de la entidad.
- entidades de la unidad:
  - `e1` Operacion: Aporte de depósitos y obligaciones por intermediación financiera — Aporte de depósitos y otras obligaciones por intermediación financiera de la entidad como forma de capitalización
  - `e2` Obligacion: Registrar aportes a valor contable — depósitos sin negociación en mercados secundarios — Cuando se trate de depósitos y otras obligaciones por intermediación financiera que no cuenten con autorización para ser negociados en mercados secundarios regulados del país o del exterior, los aport
  - `e3` Condicion: Depósitos sin autorización para negociación en mercados secundarios — Supuesto en que los depósitos y obligaciones por intermediación financiera no cuentan con autorización para ser negociados en mercados secundarios regulados del país o del exterior
  - `e4` Obligacion: Considerar disposiciones sobre instrumentos de deuda computables — capitalización — Cuando se trate de instrumentos de deuda computables como CA o PNc, al admitir los aportes se deberá tener en cuenta lo dispuesto en el punto 8.3.4
  - `e5` Restriccion: Prohibición — capitalización de deuda limitando derecho de preferencia — La capitalización de deuda no podrá implicar una limitación o suspensión al derecho de preferencia establecido en el artículo 194 de la Ley General de Sociedades
  - `e6` Excepcion: Inaplicabilidad artículo 197 LGS — capitalización de deuda — No será aplicable lo dispuesto en el artículo 197 de la Ley General de Sociedades en materia de capitalización de deuda
  - `e7` Obligacion: Decisión de capitalización ad referéndum de aprobación — SEFyC o BCRA — La decisión de capitalización de los conceptos indicados en los puntos 8.6.1. a 8.6.3. por parte de la Asamblea (o autoridad equivalente) será ad referéndum de su aprobación por parte de la SEFyC o, e
  - `e8` Obligacion: Exposición en nota a estados contables — capitalización ad referéndum — La circunstancia de que la decisión de capitalización sea ad referéndum de aprobación deberá ser expuesta en nota a los estados contables de los períodos siguientes (trimestral o anual, según correspo
  - `e9` Obligacion: Deducción de aportes no notificados de RPC — hasta notificación de aprobación — Hasta tanto se le haya notificado la aprobación de los aportes y en la medida en que éstos hayan sido contabilizados, se deducirán del respectivo componente de la RPC de la entidad financiera
  - `e10` Obligacion: Mantenimiento de tratamiento de deuda subordinada capitalizada — como pasivo — Cuando los aportes contabilizados provengan de la capitalización de deuda subordinada o de instrumentos representativos de deuda que puedan ser considerados (total o parcialmente) como parte integrant
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 93** Excepcion `e6`: Inaplicabilidad artículo 197 LGS — capitalización de deuda | descripcion: No será aplicable lo dispuesto en el artículo 197 de la Ley General de Sociedades en materia de capitalización de deuda | tramo: no será aplicable lo dispuesto en el artículo 197 de dicha ley

## Unidad `ext::8.5.17.10` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.10. Régimen de corredores de comercio (Resolución 122/93 de la
Administración Nacional de Aduanas).
- entidades de la unidad:
  - `e1` Operacion: Operación aduanera — régimen de corredores de comercio — Operación aduanera exceptuada del seguimiento de divisas por exportaciones de bienes, conforme al régimen de corredores de comercio establecido por la Resolución 122/93 de la Administración Nacional d
  - `e2` Excepcion: Excepción — régimen de corredores de comercio — Operación aduanera exceptuada del seguimiento de divisas por exportaciones de bienes conforme al régimen de corredores de comercio
  - `e3` Comunicacion: Resolución 122/93 — 
- relaciones del crudo (sin establecida_en ni de sujeto): to referencia e3
- NODOS A CLASIFICAR:
  - **caso 94** Excepcion `e2`: Excepción — régimen de corredores de comercio | descripcion: Operación aduanera exceptuada del seguimiento de divisas por exportaciones de bienes conforme al régimen de corredores de comercio | tramo: Régimen de corredores de comercio (Resolución 122/93 de la Administración Nacional de Aduanas)

## Unidad `ext::8.5.17.27` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.27. Exportaciones de valores (billetes, monedas, etc.) mediante el régimen
EC51.
- entidades de la unidad:
  - `e1` Operacion: Exportación de valores mediante régimen EC51 — Exportación de valores (billetes, monedas, etc.) mediante el régimen EC51, operación aduanera exceptuada del seguimiento de permiso de embarque
  - `e2` Excepcion: Excepción seguimiento — exportaciones valores EC51 — Operación aduanera exceptuada del seguimiento de permiso de embarque por el valor que corresponda a ventajas aduaneras u otras situaciones previstas
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 95** Excepcion `e2`: Excepción seguimiento — exportaciones valores EC51 | descripcion: Operación aduanera exceptuada del seguimiento de permiso de embarque por el valor que corresponda a ventajas aduaneras u otras situaciones previstas | tramo: Exportaciones de valores (billetes, monedas, etc.) mediante el régimen EC51

## Unidad `ext::8.5.17.6` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.6. Régimen de material promocional (Resolución General 2.345/07 de la
Administración Federal de Ingresos Públicos).
- entidades de la unidad:
  - `e1` Operacion: Régimen de material promocional — Operación aduanera exceptuada del seguimiento conforme a la Resolución General 2.345/07 de la Administración Federal de Ingresos Públicos
  - `e2` Excepcion: Excepción seguimiento — material promocional — Operación aduanera exceptuada del seguimiento de permisos de embarque por el régimen de material promocional regulado por la Resolución General 2.345/07 de la Administración Federal de Ingresos Públic
  - `e3` Comunicacion: Resolución General 2.345/07 — 
- relaciones del crudo (sin establecida_en ni de sujeto): to referencia e3
- NODOS A CLASIFICAR:
  - **caso 96** Excepcion `e2`: Excepción seguimiento — material promocional | descripcion: Operación aduanera exceptuada del seguimiento de permisos de embarque por el régimen de material promocional regulado por la Resolución General 2.345/07 de la Administración Federal de Ingresos Públicos | tramo: Régimen de material promocional (Resolución General 2.345/07 de la Administración Federal de Ingresos Públicos)

## Unidad `ext::8.5.17.17` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.17. Exportación a consumo con Destinación de Importación Temporaria, sin
transformación (subregímenes EC02, EG02 o PER1). Se refiere a la
exportación a consumo de bienes que retorna en cumplimiento de una
obligación asumida en el régimen de importación temporaria, egresando
al exterior en el mismo estado en que se importó.
- entidades de la unidad:
  - `e1` Operacion: Exportación a consumo con Destinación de Importación Temporaria — Exportación a consumo de bienes que retorna en cumplimiento de una obligación asumida en el régimen de importación temporaria, egresando al exterior en el mismo estado en que se importó. Subregímenes:
  - `e2` Excepcion: Excepción seguimiento — Exportación a consumo con Destinación de Importación Temporaria — Operación exceptuada del seguimiento de divisas por exportaciones de bienes, por corresponder a ventajas aduaneras u otras situaciones previstas en el régimen de importación temporaria.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 97** Excepcion `e2`: Excepción seguimiento — Exportación a consumo con Destinación de Importación Temporaria | descripcion: Operación exceptuada del seguimiento de divisas por exportaciones de bienes, por corresponder a ventajas aduaneras u otras situaciones previstas en el régimen de importación temporaria. | tramo: Exportación a consumo con Destinación de Importación Temporaria, sin transformación (subregímenes EC02, EG02 o PER1)

## Unidad `ext::8.5.17.21` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.21. Destinaciones suspensivas de exportaciones temporarias (artículos 349 a
373 del Código Aduanero).
- entidades de la unidad:
  - `e1` Operacion: Destinaciones suspensivas exportaciones temporarias — Destinaciones suspensivas de exportaciones temporarias conforme a los artículos 349 a 373 del Código Aduanero
  - `e2` Excepcion: Excepción seguimiento — destinaciones suspensivas — Operación exceptuada del seguimiento de permisos de embarque por el valor que corresponda a ventajas aduaneras u otras situaciones previstas
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 98** Excepcion `e2`: Excepción seguimiento — destinaciones suspensivas | descripcion: Operación exceptuada del seguimiento de permisos de embarque por el valor que corresponda a ventajas aduaneras u otras situaciones previstas | tramo: Destinaciones suspensivas de exportaciones temporarias (artículos 349 a 373 del Código Aduanero)

## Unidad `ext::8.5.17.11` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.11. Régimen de donación de órganos y sangre humana (Resolución 384/97
de la Administración Nacional de Aduanas).
- entidades de la unidad:
  - `e1` Operacion: Donación de órganos y sangre humana — Operación aduanera correspondiente al régimen de donación de órganos y sangre humana, exceptuada del seguimiento de permisos de embarque conforme a la Resolución 384/97 de la Administración Nacional d
  - `e2` Excepcion: Excepción seguimiento — donación órganos y sangre — Operación exceptuada del seguimiento de permisos de embarque por el valor que corresponda al régimen de donación de órganos y sangre humana, conforme a la Resolución 384/97 de la Administración Nacion
  - `e3` Comunicacion: Res. 384/97 — 
- relaciones del crudo (sin establecida_en ni de sujeto): to referencia e3
- NODOS A CLASIFICAR:
  - **caso 99** Excepcion `e2`: Excepción seguimiento — donación órganos y sangre | descripcion: Operación exceptuada del seguimiento de permisos de embarque por el valor que corresponda al régimen de donación de órganos y sangre humana, conforme a la Resolución 384/97 de la Administración Nacional de Aduanas. | tramo: Régimen de donación de órganos y sangre humana (Resolución 384/97 de la Administración Nacional de Aduanas)

## Unidad `ext::8.5.17.9` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.9. Régimen de envíos de asistencia y salvamento (artículos 581 al 584 de la
Ley 22.415).
- entidades de la unidad:
  - `e1` Operacion: Régimen de envíos de asistencia y salvamento — Envíos de asistencia y salvamento regulados por los artículos 581 al 584 de la Ley 22.415, exceptuados del seguimiento de divisas por exportaciones de bienes
  - `e2` Excepcion: Excepción operaciones aduaneras — seguimiento — Operaciones de envíos de asistencia y salvamento quedan exceptuadas del seguimiento de divisas por exportaciones de bienes
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 100** Excepcion `e2`: Excepción operaciones aduaneras — seguimiento | descripcion: Operaciones de envíos de asistencia y salvamento quedan exceptuadas del seguimiento de divisas por exportaciones de bienes | tramo: Régimen de envíos de asistencia y salvamento (artículos 581 al 584 de la Ley 22.415)

## Unidad `ctacte::6.4.6.5` (item)
- herencia: **[abre la lista]** [encabezado 6.4.6] 6.4.6. No corresponderá la comunicación al BCRA de los rechazos motivados por:
- texto propio: 6.4.6.5. Haberse declarado judicialmente el concurso preventivo del librador y siempre
que se trate de cheques de pago diferido emitidos hasta el día anterior a la fecha
de presentación de la solicitud de apertura de ese proceso y su fecha de pago
sea posterior a ella.
Además, en los casos de los puntos 6.4.6.2. a 6.4.6.4. los rechazos no se comunicarán única-
mente en los casos en que hubiera sido posible atenderlos con el saldo existente en la cuenta
de no haberse efectivizado el pago, incurrido en el error o dispuesta la medida cautelar.
- entidades de la unidad:
  - `e1` Operacion: Comunicación al BCRA de rechazos de cheques — Comunicación al BCRA de los rechazos de cheques
  - `e2` Excepcion: Excepción — concurso preventivo del librador — No corresponde comunicar al BCRA los rechazos cuando se ha declarado judicialmente el concurso preventivo del librador, siempre que se trate de cheques de pago diferido emitidos hasta el día anterior 
  - `e3` Condicion: Condición — cheques de pago diferido — La excepción aplica únicamente cuando se trata de cheques de pago diferido
  - `e4` Excepcion: Excepción — saldo insuficiente en puntos 6.4.6.2 a 6.4.6.4 — Para los rechazos de los puntos 6.4.6.2 a 6.4.6.4, no se comunican al BCRA únicamente cuando hubiera sido posible atenderlos con el saldo existente en la cuenta de no haberse efectivizado el pago, inc
- relaciones del crudo (sin establecida_en ni de sujeto): e2 exceptua e1; e3 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 102** Excepcion `e4`: Excepción — saldo insuficiente en puntos 6.4.6.2 a 6.4.6.4 | descripcion: Para los rechazos de los puntos 6.4.6.2 a 6.4.6.4, no se comunican al BCRA únicamente cuando hubiera sido posible atenderlos con el saldo existente en la cuenta de no haberse efectivizado el pago, incurrido en el error o dispuesta la medida cautelar | tramo: en los casos de los puntos 6.4.6.2. a 6.4.6.4. los rechazos no se comunicarán únicamente en los casos en que hubiera sido posible atenderlos con el saldo existente en la cuenta de no haberse efectivizado el pago, incurrido en el error o dispuesta la medida cautelar

## Unidad `ext::13.6` (punto_no_item)
- herencia: [encabezado S13] Sección 13. Pagos de servicios prestados por no residentes.
- texto propio: 13.6. Líneas de crédito de entidades financieras aplicadas a la financiación de importaciones de
servicios.
La entidad financiera tendrá acceso al mercado de cambios, en las condiciones previstas en
el punto 3.15.1., para la cancelación de líneas de crédito del exterior aplicadas a la
financiación de importaciones argentinas de servicios en la medida que la misma califique
como deuda comercial según lo dispuesto en el segundo párrafo del punto 13.1.2. y la
entidad cuente la documentación que demuestre que, al momento del otorgamiento de la
financiación al importador, se cumplían las condiciones que resultaban aplicables en ese
momento al tipo de operación financiada por la entidad.
En el caso de las financiaciones otorgadas a partir del 13/12/23, la entidad deberá contar con
la documentación que demuestre que:
i) la operación financiada correspondía a una importación de servicios prestada o
devengada a partir del 13/12/23.
ii) la fecha de vencimiento de la financiación otorgada era compatible con los plazos
previstos en el punto 13.2.:
a) si el otorgamiento de la financiación es anterior de la fecha de prestación o
devengamiento del servicio, los plazos previstos en el punto 13.2. se computarán a
partir de la fecha estimada de prestación o devengamiento del servicio más 15
(quince) días corridos.
En caso de tratarse una operación del concepto “S30. Servicios de fletes por
operaciones de importaciones de bienes” que encuadra en lo previsto en el punto
10.10.2.1., deberá financiarse hasta la fecha estimada de embarque de los bienes
en origen más un plazo adicional de 15 (quince) días corridos.
b) si el otorgamiento de la financiación es posterior a la fecha de prestación o
devengamiento del servicio, los plazos previstos en el punto 13.2. se computarán
desde la última fec
- entidades de la unidad:
  - `e1` Operacion: Acceso al mercado de cambios para cancelación de líneas de crédito — Acceso al mercado de cambios para la cancelación de líneas de crédito del exterior aplicadas a la financiación de importaciones argentinas de servicios, en las condiciones previstas en el punto 3.15.1
  - `e2` Condicion: Calificación como deuda comercial según punto 13.1.2. — La línea de crédito debe calificar como deuda comercial según lo dispuesto en el segundo párrafo del punto 13.1.2.
  - `e3` Condicion: Documentación de cumplimiento de condiciones al otorgamiento — La entidad debe contar con documentación que demuestre que al momento del otorgamiento de la financiación al importador se cumplían las condiciones aplicables en ese momento al tipo de operación finan
  - `e4` Obligacion: Documentación de importación de servicios a partir de 13/12/23 — Para financiaciones otorgadas a partir del 13/12/23, la entidad deberá contar con documentación que demuestre que la operación financiada correspondía a una importación de servicios prestada o devenga
  - `e5` Obligacion: Compatibilidad de vencimiento con plazos punto 13.2. — La fecha de vencimiento de la financiación otorgada debe ser compatible con los plazos previstos en el punto 13.2.
  - `e6` Condicion: Otorgamiento anterior a prestación o devengamiento del servicio — Cuando el otorgamiento de la financiación es anterior a la fecha de prestación o devengamiento del servicio, los plazos previstos en el punto 13.2. se computarán a partir de la fecha estimada de prest
  - `e7` Excepcion: Excepción servicios de fletes importaciones de bienes — Para operaciones del concepto S30 (Servicios de fletes por operaciones de importaciones de bienes) que encuadran en el punto 10.10.2.1., la financiación debe extenderse hasta la fecha estimada de emba
  - `e8` Condicion: Otorgamiento posterior a prestación o devengamiento del servicio — Cuando el otorgamiento de la financiación es posterior a la fecha de prestación o devengamiento del servicio, los plazos previstos en el punto 13.2. se computarán desde la última fecha mencionada.
  - `e9` Restriccion: Sujeción a conformidad previa del BCRA por incumplimiento — Los casos que no cumplan las condiciones requeridas quedan sujetos a la conformidad previa del BCRA para acceder al mercado de cambios.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1; e3 condicion_de e1; e6 condicion_de e5; e8 condicion_de e5
- NODOS A CLASIFICAR:
  - **caso 104** Excepcion `e7`: Excepción servicios de fletes importaciones de bienes | descripcion: Para operaciones del concepto S30 (Servicios de fletes por operaciones de importaciones de bienes) que encuadran en el punto 10.10.2.1., la financiación debe extenderse hasta la fecha estimada de embarque de los bienes en origen más 15 días corridos. | tramo: En caso de tratarse una operación del concepto "S30. Servicios de fletes por operaciones de importaciones de bienes" que encuadra en lo previsto en el punto 10.10.2.1., deberá financiarse hasta la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos.

## Unidad `ext::7.1.1.3` (item)
- herencia: **[abre la lista]** [intro 7.1.1] El contravalor en divisas de la exportación hasta alcanzar el valor facturado según la
condición de venta pactada deberá ingresarse al país y liquidarse en el mercado de
cambios.
En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al
Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad
de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198
de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicio | [cierre 7.1.1] Independientemente de los plazos máximos precedentes, los cobros de exportaciones
deberán ser ingresados y liquidados en el mercado de cambios dentro de los 20
(veinte) días hábiles de la fecha de cobro. La posibilidad de utilizar este plazo quedará
supeditada en todos los casos al cumplimiento de los plazos previstos en los puntos
7.1.1.1. a 7.1.1.5.
Los montos en moneda extranjera originados en cobros de siniestros por coberturas
contratadas, en la medida que los mismos cubran el valor de los 
- texto propio: 7.1.1.3. 60 (sesenta) días corridos para las operaciones con contrapartes vinculadas
que no correspondan a los bienes indicados en los puntos 7.1.1.1. y 7.1.1.2.
y las exportaciones correspondientes a los capítulos 26 (excepto las
posiciones 2601.11.00, 2603.00.90, 2607.00.00, 2608.00.10, 2613.90.90,
2616.10.00, 2616.90.00 y 2621.10.00) y 71 (excepto las posiciones
7106.91.00, 7108.12.10 y 7112.99.00).
Los exportadores que realizaron operaciones con contrapartes vinculadas
que correspondan a bienes comprendidos en el punto 7.1.1.4., en las cuales
el importador sea una sociedad controlada por el exportador argentino,
podrán solicitar a la entidad encargada del seguimiento de la destinación que
extienda el plazo hasta:
i) el plazo previsto en dicho punto cuando el exportador no haya registrado
exportaciones por un valor total superior al equivalente a USD
50.000.000 (dólares estadounidenses cincuenta millones) en el año
calendario inmediato anterior a la oficialización de la destinación;
ii) un plazo de 120 (ciento veinte) días corridos cuando el exportador haya
superado el monto indicado en el punto precedente y los bienes
exportados correspondan a las posiciones que se detallan a
continuación:
0202.30.00.111D, 0202.30.00.115M, 0202.30.00.117R;
0202.30.00.118U, 0202.30.00.121G, 0202.30.00.124N,
0202.30.00.126T, 0202.30.00.131K, 0202.30.00.133P,
0202.30.00.136W, 0202.30.00.137Y, 0202.30.00.141N,
0202.30.00.142Q, 0202.30.00.146Z, 0202.30.00.147B,
0202.30.00.151R, 0202.30.00.943L, 0202.30.00.991Y,
0202.30.00.992A, 0202.30.00.995G, 0203.21.00.000J,
0206.29.90.300P, 0207.14.00.100K, 1901.90.20 (en envases inmediatos
de contenido neto inferior o igual a 1 kg) y 2204.21.00.
- entidades de la unidad:
  - `e1` Operacion: Ingreso y liquidación de divisas — exportaciones — Ingreso al país y liquidación en el mercado de cambios del contravalor en divisas de la exportación hasta alcanzar el valor facturado según la condición de venta pactada.
  - `e2` Obligacion: Plazo 60 días — operaciones contrapartes vinculadas — Ingreso y liquidación de divisas en plazo de 60 (sesenta) días corridos para operaciones con contrapartes vinculadas que no correspondan a los bienes de los puntos 7.1.1.1. y 7.1.1.2., y para exportac
  - `e3` Excepcion: Exclusión posiciones arancelarias — capítulo 26 — Quedan exceptuadas del plazo de 60 días las exportaciones de las posiciones arancelarias del capítulo 26 especificadas.
  - `e4` Excepcion: Exclusión posiciones arancelarias — capítulo 71 — Quedan exceptuadas del plazo de 60 días las exportaciones de las posiciones arancelarias del capítulo 71 especificadas.
  - `e5` Potestad: Solicitud extensión plazo — contrapartes vinculadas controladas — Facultad de los exportadores que realizaron operaciones con contrapartes vinculadas (bienes del punto 7.1.1.4., importador sociedad controlada por el exportador argentino) de solicitar a la entidad en
  - `e6` Condicion: Condición — exportaciones no superiores USD 50.000.000 — Supuesto en que el exportador no ha registrado exportaciones por valor total superior a USD 50.000.000 en el año calendario inmediato anterior a la oficialización de la destinación.
  - `e7` Obligacion: Plazo según punto 7.1.1.4. — extensión condicionada — Extensión del plazo hasta el previsto en el punto 7.1.1.4. cuando el exportador no haya registrado exportaciones por valor total superior a USD 50.000.000 en el año calendario inmediato anterior a la 
  - `e8` Condicion: Condición — exportaciones superiores USD 50.000.000 — Supuesto en que el exportador ha superado USD 50.000.000 en exportaciones y los bienes corresponden a las posiciones arancelarias especificadas.
  - `e9` Obligacion: Plazo 120 días — extensión condicionada — Extensión del plazo hasta 120 (ciento veinte) días corridos cuando el exportador ha superado USD 50.000.000 en exportaciones y los bienes corresponden a las posiciones arancelarias especificadas.
- relaciones del crudo (sin establecida_en ni de sujeto): e6 condicion_de e7; e8 condicion_de e9
- NODOS A CLASIFICAR:
  - **caso 106** Excepcion `e3`: Exclusión posiciones arancelarias — capítulo 26 | descripcion: Quedan exceptuadas del plazo de 60 días las exportaciones de las posiciones arancelarias del capítulo 26 especificadas. | tramo: excepto las posiciones 2601.11.00, 2603.00.90, 2607.00.00, 2608.00.10, 2613.90.90, 2616.10.00, 2616.90.00 y 2621.10.00
  - **caso 107** Excepcion `e4`: Exclusión posiciones arancelarias — capítulo 71 | descripcion: Quedan exceptuadas del plazo de 60 días las exportaciones de las posiciones arancelarias del capítulo 71 especificadas. | tramo: excepto las posiciones 7106.91.00, 7108.12.10 y 7112.99.00

## Unidad `ext::8.5.17.18` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.18. Exportación a consumo de bienes que se encuentran excluidos del
Régimen de Equipaje –art. 59 inc. B) del Decreto 1.001/82–: son aquellos
bienes (por ejemplo: automotores, motocicletas, motores dentro o fuera
de borda, aeronaves, embarcaciones, etc.) que un residente del país
exporta con motivo de su radicación en el exterior.
- entidades de la unidad:
  - `e1` Definicion: Exportación a consumo — bienes excluidos Equipaje — Bienes tales como automotores, motocicletas, motores dentro o fuera de borda, aeronaves, embarcaciones, etc., que un residente del país exporta con motivo de su radicación en el exterior, excluidos de
  - `e2` Operacion: Exportación a consumo — bienes excluidos Equipaje — Exportación de bienes excluidos del Régimen de Equipaje (automotores, motocicletas, motores, aeronaves, embarcaciones, etc.) realizada por un residente del país con motivo de su radicación en el exter
  - `e3` Excepcion: Excepción — operaciones aduaneras exceptuadas seguimiento — Quedan exceptuadas del seguimiento las exportaciones a consumo de bienes excluidos del Régimen de Equipaje, por el valor que corresponda a ventajas aduaneras u otras situaciones previstas.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 108** Excepcion `e3`: Excepción — operaciones aduaneras exceptuadas seguimiento | descripcion: Quedan exceptuadas del seguimiento las exportaciones a consumo de bienes excluidos del Régimen de Equipaje, por el valor que corresponda a ventajas aduaneras u otras situaciones previstas. | tramo: Exportación a consumo de bienes que se encuentran excluidos del Régimen de Equipaje

## Unidad `cla::6.5.3.2` (item)
- herencia: [intro 6.5] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudor | **[abre la lista]** [intro 6.5.3] El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender
normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos,
esos problemas pueden resultar en una pérdida para la entidad financiera.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- texto propio: 6.5.3.2. Incurra en atrasos de hasta 180 días, con exclusión de los deudores comprendi-
dos en el punto 6.5.2.2. A este fin, el cómputo de los plazos no se interrumpirá
por el otorgamiento de renovaciones cuando previamente no se haya producido
la cancelación efectiva de las obligaciones vencidas, es decir sin recurrir a finan-
ciación directa o indirecta de la entidad.
- entidades de la unidad:
  - `e1` Condicion: Atrasos hasta 180 días — El cliente incurre en atrasos de hasta 180 días como indicador de problemas para atender normalmente sus compromisos financieros.
  - `e2` Excepcion: Exclusión deudores punto 6.5.2.2 — Quedan exceptuados de esta condición los deudores comprendidos en el punto 6.5.2.2.
  - `e3` Obligacion: Cómputo de plazos sin interrupción por renovaciones — El cómputo de los plazos de atrasos no se interrumpirá por el otorgamiento de renovaciones cuando previamente no se haya producido la cancelación efectiva de las obligaciones vencidas, es decir sin re
  - `e4` Condicion: Cancelación sin financiación directa o indirecta — La cancelación efectiva de las obligaciones vencidas debe realizarse sin recurrir a financiación directa o indirecta de la entidad.
- relaciones del crudo (sin establecida_en ni de sujeto): e4 condicion_de e3
- NODOS A CLASIFICAR:
  - **caso 109** Excepcion `e2`: Exclusión deudores punto 6.5.2.2 | descripcion: Quedan exceptuados de esta condición los deudores comprendidos en el punto 6.5.2.2. | tramo: con exclusión de los deudores comprendidos en el punto 6.5.2.2
  - **caso 142** Condicion `e1`: Atrasos hasta 180 días | descripcion: El cliente incurre en atrasos de hasta 180 días como indicador de problemas para atender normalmente sus compromisos financieros. | tramo: Incurra en atrasos de hasta 180 días

## Unidad `ext::2.2.2.3` (item)
- herencia: **[abre la lista]** [intro 2.2.2] servicios que ingresen en los plazos normativos previstos y encuadren en las
siguientes situaciones:
- texto propio: 2.2.2.3. Se trata de cobros de exportaciones de servicios que correspondan a las
siguientes operaciones asociadas al turismo internacional en el país:
i) los cobros por consumos en el país efectuados por no residentes
mediante tarjetas de débito, crédito, compra o prepagas emitidas en el
exterior.
ii) los cobros por consumos en el país efectuados por no residentes
mediante billeteras electrónicas o cualquier otra modalidad de pago que
implique un débito inmediato en una cuenta en una entidad financiera en
el exterior o en una cuenta virtual en una empresa en el exterior.
En el caso de que la modalidad por la cual se canaliza el consumo
contemple la posibilidad de utilizar cuentas virtuales, quien ingresa los
fondos deberá demostrar que el mecanismo de pago utilizado prevé que
tales cuentas se encuentren abiertas en instituciones cuya operatoria
esté autorizada por la autoridad monetaria o equivalente de su país de
radicación y que la tenencia de una clave fiscal de ese país es condición
para la apertura de la cuenta.
iii) los cobros por cualquier tipo de servicio turístico en el país contratado
por no residentes, incluyendo aquellos servicios contratados a través de
agencias mayoristas y/o minoristas de viajes y turismo del país.
iv)los cobros por servicios de transporte de pasajeros no residentes con
destino en el país por vía terrestre, aérea o acuática.
A los efectos del registro de estas operaciones se deberán confeccionar dos
boletos sin movimiento de pesos, el boleto de compra se realizará por el
concepto de servicios al que corresponda el ingreso y el boleto de venta bajo
el concepto “A10. Débito/crédito de moneda extranjera en cuentas locales
por transferencias con el exterior”.
- entidades de la unidad:
  - `e1` Operacion: Cobros exportaciones servicios turismo internacional — Cobros de exportaciones de servicios que correspondan a operaciones asociadas al turismo internacional en el país, incluyendo: consumos en el país efectuados por no residentes mediante tarjetas de déb
  - `e2` Operacion: Cobros consumos tarjetas no residentes — Cobros por consumos en el país efectuados por no residentes mediante tarjetas de débito, crédito, compra o prepagas emitidas en el exterior.
  - `e3` Operacion: Cobros consumos billeteras electrónicas no residentes — Cobros por consumos en el país efectuados por no residentes mediante billeteras electrónicas o cualquier otra modalidad de pago que implique un débito inmediato en una cuenta en una entidad financiera
  - `e4` Condicion: Cuentas virtuales autorizadas por autoridad monetaria — Cuando la modalidad de pago contemple la posibilidad de utilizar cuentas virtuales, estas deben estar abiertas en instituciones cuya operatoria esté autorizada por la autoridad monetaria o equivalente
  - `e5` Obligacion: Demostración requisitos cuentas virtuales — Quien ingresa los fondos deberá demostrar que el mecanismo de pago utilizado prevé que las cuentas virtuales se encuentren abiertas en instituciones cuya operatoria esté autorizada por la autoridad mo
  - `e6` Operacion: Cobros servicios turísticos no residentes — Cobros por cualquier tipo de servicio turístico en el país contratado por no residentes, incluyendo aquellos servicios contratados a través de agencias mayoristas y/o minoristas de viajes y turismo de
  - `e7` Operacion: Cobros transporte pasajeros no residentes — Cobros por servicios de transporte de pasajeros no residentes con destino en el país por vía terrestre, aérea o acuática.
  - `e8` Obligacion: Confección boletos sin movimiento de pesos — A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin movimiento de pesos: el boleto de compra se realizará por el concepto de servicios al que corresponda el ingreso
  - `e9` Excepcion: Excepción obligación liquidación cobros exportaciones servicios — Quedan exceptuados de la obligación de liquidación los cobros de exportaciones de servicios que ingresen en los plazos normativos previstos y encuadren en las situaciones descritas en este punto.
- relaciones del crudo (sin establecida_en ni de sujeto): e4 condicion_de e5; e8 regula e1
- NODOS A CLASIFICAR:
  - **caso 110** Excepcion `e9`: Excepción obligación liquidación cobros exportaciones servicios | descripcion: Quedan exceptuados de la obligación de liquidación los cobros de exportaciones de servicios que ingresen en los plazos normativos previstos y encuadren en las situaciones descritas en este punto. | tramo: Quedarán exceptuados de la obligación de liquidación los cobros de exportaciones de servicios que ingresen en los plazos normativos previstos y encuadren en las siguientes situaciones

## Unidad `ext::2.2.2.2` (item)
- herencia: **[abre la lista]** [intro 2.2.2] servicios que ingresen en los plazos normativos previstos y encuadren en las
siguientes situaciones:
- texto propio: 2.2.2.2. Se trata de cobros de exportaciones de servicios prestados por personas
jurídicas que sean beneficiarias del Régimen de fomento para las
exportaciones de la economía del conocimiento (Capítulo II del Decreto
679/22) y se cumplen la totalidad de las siguientes condiciones:
i) las operaciones corresponden a los códigos de concepto enunciados en
el punto 2.2.2.1.i).
La entidad interviniente deberá adicionalmente contar con una
declaración jurada del cliente en la que conste que los cobros que dejan
de liquidarse corresponden a exportaciones de servicios que están
relacionadas con actividades vinculadas a la economía del
conocimiento.
ii) el cliente cuente por el equivalente del monto que se pretende no
liquidar con una “Certificación de incremento de exportaciones
asociadas a la economía del conocimiento (Decreto 679/22)” emitida en
los términos previstos en el punto 2.6.2.
iii) los fondos en moneda extranjera deberán ser acreditados en una
“Cuenta especial para el régimen de fomento de la economía del
conocimiento. Decreto 679/22” de titularidad del cliente hasta que sean
destinados al pago en moneda extranjera de las remuneraciones de
personal en relación de dependencia, debidamente registrado, afectado
a las actividades de la economía del conocimiento, conforme los
criterios establecidos en el Decreto 679/22 y la Resolución 234/22 del
Ministerio de Economía.
A los efectos del registro de estas operaciones se deberán confeccionar dos
boletos sin movimiento de pesos, el boleto de compra se realizará por el
concepto de servicios que corresponda y el boleto de venta deberá
registrarse bajo el código de concepto “A22. Acreditación de cobros de
exportaciones de bienes y servicios”.
- entidades de la unidad:
  - `e1` Excepcion: Excepción liquidación — cobros servicios economía conocimiento — Quedan exceptuados de la obligación de liquidación los cobros de exportaciones de servicios prestados por personas jurídicas beneficiarias del Régimen de fomento para las exportaciones de la economía 
  - `c1` Condicion: Códigos de concepto — punto 2.2.2.1.i) — Las operaciones deben corresponder a los códigos de concepto enunciados en el punto 2.2.2.1.i).
  - `o1` Obligacion: Declaración jurada cliente — cobros servicios economía conocimiento — La entidad interviniente debe contar con una declaración jurada del cliente en la que conste que los cobros que dejan de liquidarse corresponden a exportaciones de servicios relacionadas con actividad
  - `c2` Condicion: Certificación incremento exportaciones — Decreto 679/22 — El cliente debe contar, por el equivalente del monto que se pretende no liquidar, con una Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22) emitida
  - `c3` Condicion: Acreditación fondos — Cuenta especial economía conocimiento — Los fondos en moneda extranjera deben ser acreditados en una Cuenta especial para el régimen de fomento de la economía del conocimiento (Decreto 679/22) de titularidad del cliente, hasta que sean dest
  - `o2` Obligacion: Confección boletos — registro operaciones servicios economía conocimiento — Para el registro de estas operaciones se deben confeccionar dos boletos sin movimiento de pesos: el boleto de compra por el concepto de servicios que corresponda y el boleto de venta registrado bajo e
  - `com1` Comunicacion: Decreto 679/22 — 
  - `com2` Comunicacion: Resolución 234/22 Ministerio de Economía — 
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1; c2 condicion_de e1; c3 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 111** Excepcion `e1`: Excepción liquidación — cobros servicios economía conocimiento | descripcion: Quedan exceptuados de la obligación de liquidación los cobros de exportaciones de servicios prestados por personas jurídicas beneficiarias del Régimen de fomento para las exportaciones de la economía del conocimiento, cuando se cumplen la totalidad de las condiciones especificadas. | tramo: Quedarán exceptuados de la obligación de liquidación los cobros de exportaciones de servicios que ingresen en los plazos normativos previstos y encuadren en las siguientes situaciones: Se trata de cobros de exportaciones de servicios prestados por personas jurídicas que sean beneficiarias del Régimen de fomento para las exportaciones de la economía del conocimiento (Capítulo II del Decreto 679/22) y se cumplen la totalidad de las siguientes condiciones

## Unidad `ctacte::5.1.1::cierre` (cierre)
- herencia: [encabezado 5.1.1] 5.1.1. Límite.
- texto propio: Se exceptúan de las limitaciones establecidas en este punto a los endosos que las enti-
dades financieras realicen para la obtención de financiación, a favor de una entidad fi-
nanciera o de un fiduciario de un fideicomiso financiero, en ambos casos comprendidos
en la Ley de Entidades Financieras y las sucesivas transmisiones a favor de otros sujetos
de la misma naturaleza, así como cuando los cheques se depositen en la Caja de Valo-
res S.A. para ser negociados en las bolsas de comercio y mercados de valores autoriza-
dos por la Comisión Nacional de Valores de la República Argentina, en cuyo caso los en-
dosos deberán ser extendidos con la cláusula “... para su negociación en mercados de
valores”. También se exceptuarán de la citada limitación los endosos a favor del BCRA y
aquellos efectuados en los ECHEQ.
- entidades de la unidad:
  - `e1` Excepcion: Excepción endosos para financiación — Quedan exceptuados de los límites de endosos los que las entidades financieras realicen para obtener financiación a favor de otra entidad financiera o de un fiduciario de fideicomiso financiero compre
  - `e2` Excepcion: Excepción endosos para negociación en mercados de valores — Quedan exceptuados los endosos cuando los cheques se depositen en la Caja de Valores S.A. para negociación en bolsas de comercio y mercados de valores autorizados por la CNV, debiendo extenderse los e
  - `e3` Excepcion: Excepción endosos a favor del BCRA — Quedan exceptuados los endosos a favor del BCRA de las limitaciones establecidas en el punto.
  - `e4` Excepcion: Excepción endosos en ECHEQ — Quedan exceptuados los endosos efectuados en los ECHEQ de las limitaciones establecidas en el punto.
  - `e5` Obligacion: Cláusula obligatoria en endosos para mercados de valores — Los endosos de cheques depositados en la Caja de Valores S.A. para negociación en mercados de valores deben extenderse con la cláusula "... para su negociación en mercados de valores".
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 112** Excepcion `e1`: Excepción endosos para financiación | descripcion: Quedan exceptuados de los límites de endosos los que las entidades financieras realicen para obtener financiación a favor de otra entidad financiera o de un fiduciario de fideicomiso financiero comprendidos en la LEF, y las sucesivas transmisiones a favor de otros sujetos de la misma naturaleza. | tramo: Se exceptúan de las limitaciones establecidas en este punto a los endosos que las entidades financieras realicen para la obtención de financiación, a favor de una entidad financiera o de un fiduciario de un fideicomiso financiero, en ambos casos comprendidos en la Ley de Entidades Financieras y las sucesivas transmisiones a favor de otros sujetos de la misma naturaleza
  - **caso 113** Excepcion `e3`: Excepción endosos a favor del BCRA | descripcion: Quedan exceptuados los endosos a favor del BCRA de las limitaciones establecidas en el punto. | tramo: También se exceptuarán de la citada limitación los endosos a favor del BCRA
  - **caso 114** Excepcion `e2`: Excepción endosos para negociación en mercados de valores | descripcion: Quedan exceptuados los endosos cuando los cheques se depositen en la Caja de Valores S.A. para negociación en bolsas de comercio y mercados de valores autorizados por la CNV, debiendo extenderse los endosos con la cláusula "... para su negociación en mercados de valores". | tramo: cuando los cheques se depositen en la Caja de Valores S.A. para ser negociados en las bolsas de comercio y mercados de valores autorizados por la Comisión Nacional de Valores de la República Argentina, en cuyo caso los endosos deberán ser extendidos con la cláusula "... para su negociación en mercados de valores"
  - **caso 115** Excepcion `e4`: Excepción endosos en ECHEQ | descripcion: Quedan exceptuados los endosos efectuados en los ECHEQ de las limitaciones establecidas en el punto. | tramo: aquellos efectuados en los ECHEQ

## Unidad `cap::2.8.1` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca | [encabezado 2.8] 2.8. Exposiciones minoristas.
- texto propio: 2.8.1. Exposiciones comprendidas.
i) Personas humanas.
ii) Micro, pequeñas y medianas empresas (Mipyme), conforme al TO sobre Determina-
ción de la Condición de Micro, Pequeña y Mediana Empresa, que se ajusten a los cri-
terios para las exposiciones minoristas normativas previstos en el punto 2.8.3.
El resto de las exposiciones a Mipyme recibirán el tratamiento aplicable a las exposi-
ciones a empresas previsto en el punto 2.7.
Se excluyen a las exposiciones con garantía hipotecaria sobre vivienda residencial, las
participaciones en el capital de Mipyme y la tenencia de instrumentos de deuda emitidos
por esas empresas.
- entidades de la unidad:
  - `e1` Definicion: Exposiciones minoristas comprendidas — Comprenden personas humanas y Micro, pequeñas y medianas empresas (Mipyme) conforme al TO sobre Determinación de la Condición de Micro, Pequeña y Mediana Empresa, que se ajusten a los criterios para l
  - `e2` Excepcion: Exclusión exposiciones hipotecarias, participaciones y deuda de Mipyme — Quedan excluidas de las exposiciones minoristas las exposiciones con garantía hipotecaria sobre vivienda residencial, las participaciones en el capital de Mipyme y la tenencia de instrumentos de deuda
  - `e3` Obligacion: Tratamiento aplicable a Mipyme no normativas — Las exposiciones a Mipyme que no se ajusten a los criterios para las exposiciones minoristas normativas recibirán el tratamiento aplicable a las exposiciones a empresas previsto en el punto 2.7.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 116** Excepcion `e2`: Exclusión exposiciones hipotecarias, participaciones y deuda de Mipyme | descripcion: Quedan excluidas de las exposiciones minoristas las exposiciones con garantía hipotecaria sobre vivienda residencial, las participaciones en el capital de Mipyme y la tenencia de instrumentos de deuda emitidos por esas empresas. | tramo: Se excluyen a las exposiciones con garantía hipotecaria sobre vivienda residencial, las participaciones en el capital de Mipyme y la tenencia de instrumentos de deuda emitidos por esas empresas.

## Unidad `ric::11.1::intro` (intro)
- herencia: [encabezado 11.1] 11.1. Normas de procedimiento.
- texto propio: Conceptos comprendidos.
Se incluirán los flujos de fondos nocionales futuros sujetos a reapreciación de activos, pasi-
vos y partidas fuera de balance sensibles a variaciones en la tasa de interés.
Conceptos excluidos.
- Activos que se deducen del capital ordinario del nivel 1 (COn1);
- Activos fijos;
- Posiciones en acciones en la cartera de inversión.
Frecuencia y consolidación.
Los datos se informarán con frecuencia trimestral y se integrarán con los datos correspon-
dientes al último mes de cada trimestre (marzo, junio, septiembre y diciembre), sobre base
individual y consolidada mensual. Serán aplicables los siguientes códigos de consolidación
definidos en la Sección 2.:
Base individual (código de consolidación 0 o 1);
Base consolidada (código de consolidación 2).
Se regirá por los plazos de presentación previstos para el régimen informativo contable men-
sual correspondiente al mes siguiente al del cierre de cada trimestre.
- entidades de la unidad:
  - `e1` Definicion: Conceptos comprendidos — flujos nocionales — Flujos de fondos nocionales futuros sujetos a reapreciación de activos, pasivos y partidas fuera de balance sensibles a variaciones en la tasa de interés.
  - `e2` Excepcion: Exclusión — activos deducidos del capital ordinario nivel 1 — Quedan excluidos de los conceptos comprendidos los activos que se deducen del capital ordinario del nivel 1 (COn1).
  - `e3` Excepcion: Exclusión — activos fijos — Quedan excluidos de los conceptos comprendidos los activos fijos.
  - `e4` Excepcion: Exclusión — posiciones en acciones cartera inversión — Quedan excluidas de los conceptos comprendidos las posiciones en acciones en la cartera de inversión.
  - `e5` Obligacion: Presentación trimestral — datos con consolidación — Los datos se informarán con frecuencia trimestral, integrándose con los datos correspondientes al último mes de cada trimestre (marzo, junio, septiembre y diciembre), sobre base individual y consolida
  - `e6` Definicion: Base individual — código consolidación 0 o 1 — Base individual se identifica con código de consolidación 0 o 1.
  - `e7` Definicion: Base consolidada — código consolidación 2 — Base consolidada se identifica con código de consolidación 2.
  - `e8` Obligacion: Cumplimiento plazos — régimen informativo contable mensual — La presentación se regirá por los plazos de presentación previstos para el régimen informativo contable mensual correspondiente al mes siguiente al del cierre de cada trimestre.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 117** Excepcion `e4`: Exclusión — posiciones en acciones cartera inversión | descripcion: Quedan excluidas de los conceptos comprendidos las posiciones en acciones en la cartera de inversión. | tramo: Posiciones en acciones en la cartera de inversión
  - **caso 120** Excepcion `e3`: Exclusión — activos fijos | descripcion: Quedan excluidos de los conceptos comprendidos los activos fijos. | tramo: Activos fijos
  - **caso 121** Excepcion `e2`: Exclusión — activos deducidos del capital ordinario nivel 1 | descripcion: Quedan excluidos de los conceptos comprendidos los activos que se deducen del capital ordinario del nivel 1 (COn1). | tramo: Activos que se deducen del capital ordinario del nivel 1 (COn1)

## Unidad `cap::2.6.1` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca | [encabezado 2.6] 2.6. Exposiciones a entidades financieras.
- texto propio: 2.6.1. Exposiciones comprendidas.
Comprende a las exposiciones a entidades financieras del país y del exterior (estas últi-
mas, sujetas a regulación y supervisión prudencial equiparables a los mínimos que se
establecen en los estándares internacionales o al cumplimiento del requisito de capitales
mínimos cuando se trate de bancos que no sean internacionalmente activos conforme a
la regulación de su jurisdicción). Se excluyen las exposiciones previstas en el punto
2.11.
Las exposiciones de corto plazo comprenden a aquellas denominadas en pesos cuya
fuente de fondos sea en esa moneda y su plazo contractual original sea de hasta 3 me-
ses, y a las exposiciones vinculadas con el comercio exterior cuyo plazo contractual ori-
ginal sea de hasta 6 meses.
- entidades de la unidad:
  - `e1` Operacion: Exposiciones a entidades financieras del país — Exposiciones a entidades financieras del país, comprendidas en el alcance de este punto.
  - `e2` Operacion: Exposiciones a entidades financieras del exterior — Exposiciones a entidades financieras del exterior, sujetas a regulación y supervisión prudencial equiparables a los mínimos de estándares internacionales o al cumplimiento del requisito de capitales m
  - `e3` Excepcion: Exclusión exposiciones punto 2.11 — Quedan excluidas del alcance de este punto las exposiciones previstas en el punto 2.11.
  - `e4` Definicion: Exposiciones de corto plazo — definición — Aquellas denominadas en pesos cuya fuente de fondos sea en esa moneda y su plazo contractual original sea de hasta 3 meses, y las exposiciones vinculadas con el comercio exterior cuyo plazo contractua
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 118** Excepcion `e3`: Exclusión exposiciones punto 2.11 | descripcion: Quedan excluidas del alcance de este punto las exposiciones previstas en el punto 2.11. | tramo: Se excluyen las exposiciones previstas en el punto 2.11

## Unidad `cap::4.1::intro` (intro)
- herencia: [encabezado 4.1] 4.1. Exigencia de capital por riesgo de crédito de contraparte para operaciones DvP fallidas y no
- texto propio: DvP.
En las operaciones con títulos valores, oro o moneda extranjera pendientes de liquidación
(como ocurre en las operaciones contado a liquidar), la exposición al riesgo de crédito de
contraparte se produce desde la fecha de la operación, con independencia de cuando se
registre o contabilice. Las entidades deberán desarrollar, implementar y mejorar sistemas para
realizar un seguimiento adecuado de la exposición al riesgo de crédito de contraparte
procedente de esas operaciones y obtener información que permita intervenir en el momento
oportuno.
Las operaciones concertadas bajo la modalidad de entrega contra pago (DvP) –que implica el
intercambio simultáneo de valores por efectivo– exponen a las entidades al riesgo de pérdida
por la exposición actual positiva –definida como la diferencia positiva entre el valor de la ope-
ración al precio de liquidación convenido y su valor al precio actual de mercado–.
Las operaciones en las que se entrega efectivo sin recibir la correspondiente contrapartida (tí-
tulos valores, oro o moneda extranjera) o, al contrario, en las que se entregan los efectos
acordados sin el correspondiente pago de efectivo –es decir, operaciones no DvP– exponen a
las entidades al riesgo de pérdida por el valor total del efectivo abonado o de los efectos en-
tregados.
En el presente punto se detalla el cómputo de la exigencia de capital para cubrir ambos tipos
de riesgo. Esto incluye operaciones sujetas a valuación diaria a precios de mercado y a repo-
sición diaria de márgenes realizadas a través de cámaras de compensación y de CCP sujetas
a regulación. No se incluyen las operaciones de pase que no hayan podido liquidarse.
- entidades de la unidad:
  - `e1` Operacion: Operaciones DvP con títulos, oro o moneda extranjera — Operaciones con títulos valores, oro o moneda extranjera pendientes de liquidación (como operaciones contado a liquidar) que implican intercambio simultáneo de valores por efectivo. La exposición al r
  - `e2` Operacion: Operaciones no DvP con títulos, oro o moneda extranjera — Operaciones en las que se entrega efectivo sin recibir la correspondiente contrapartida (títulos valores, oro o moneda extranjera) o se entregan los efectos acordados sin el correspondiente pago de ef
  - `e3` Obligacion: Desarrollar, implementar y mejorar sistemas de seguimiento — Las entidades deberán desarrollar, implementar y mejorar sistemas para realizar un seguimiento adecuado de la exposición al riesgo de crédito de contraparte procedente de operaciones con títulos valor
  - `e4` Excepcion: Exclusión de operaciones de pase no liquidadas — Quedan excluidas del cómputo de la exigencia de capital las operaciones de pase que no hayan podido liquidarse.
  - `e5` Condicion: Operaciones sujetas a valuación diaria y reposición de márgenes — El cómputo de la exigencia de capital incluye operaciones sujetas a valuación diaria a precios de mercado y a reposición diaria de márgenes realizadas a través de cámaras de compensación y de CCP suje
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 119** Excepcion `e4`: Exclusión de operaciones de pase no liquidadas | descripcion: Quedan excluidas del cómputo de la exigencia de capital las operaciones de pase que no hayan podido liquidarse. | tramo: No se incluyen las operaciones de pase que no hayan podido liquidarse
  - **caso 211** Condicion `e5`: Operaciones sujetas a valuación diaria y reposición de márgenes | descripcion: El cómputo de la exigencia de capital incluye operaciones sujetas a valuación diaria a precios de mercado y a reposición diaria de márgenes realizadas a través de cámaras de compensación y de CCP sujetas a regulación. | tramo: operaciones sujetas a valuación diaria a precios de mercado y a reposición diaria de márgenes realizadas a través de cámaras de compensación y de CCP sujetas a regulación

## Unidad `polcre::5.1` (punto_no_item)
- herencia: [encabezado S5] Sección 5. Financiamiento a residentes en el exterior.
- texto propio: 5.1. Criterio general.
El otorgamiento de asistencia financiera a residentes en el exterior sólo procederá en tanto se
ajuste al criterio general sobre política de crédito indicado en la Sección 1.
Conforme a ello, se podrán conceder líneas de crédito a bancos del exterior, corresponsales o
no, y a otros residentes en el exterior destinadas a facilitar las exportaciones locales.
También se admite la existencia de créditos a residentes en el exterior correspondientes a des-
fases de liquidación de operaciones con títulos valores o monedas extranjeras con cotización y
las operaciones previstas en los siguientes puntos.
- entidades de la unidad:
  - `e1` Condicion: Ajuste a criterio general de política de crédito — El otorgamiento de asistencia financiera a residentes en el exterior debe ajustarse al criterio general sobre política de crédito indicado en la Sección 1.
  - `e2` Operacion: Concesión de líneas de crédito a bancos del exterior — Concesión de líneas de crédito a bancos del exterior, corresponsales o no, destinadas a facilitar las exportaciones locales.
  - `e3` Operacion: Concesión de líneas de crédito a otros residentes en el exterior — Concesión de líneas de crédito a otros residentes en el exterior destinadas a facilitar las exportaciones locales.
  - `e4` Potestad: Facultad de conceder líneas de crédito a residentes en el exterior — Las entidades financieras quedan facultadas a conceder líneas de crédito a bancos del exterior, corresponsales o no, y a otros residentes en el exterior destinadas a facilitar las exportaciones locale
  - `e5` Operacion: Créditos por desfases de liquidación de operaciones con títulos valores — Créditos a residentes en el exterior correspondientes a desfases de liquidación de operaciones con títulos valores o monedas extranjeras con cotización.
  - `e6` Excepcion: Admisión de créditos por desfases de liquidación — Se admite la existencia de créditos a residentes en el exterior correspondientes a desfases de liquidación de operaciones con títulos valores o monedas extranjeras con cotización, como excepción a las
- relaciones del crudo (sin establecida_en ni de sujeto): e1 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 122** Excepcion `e6`: Admisión de créditos por desfases de liquidación | descripcion: Se admite la existencia de créditos a residentes en el exterior correspondientes a desfases de liquidación de operaciones con títulos valores o monedas extranjeras con cotización, como excepción a las restricciones generales. | tramo: También se admite la existencia de créditos a residentes en el exterior correspondientes a desfases de liquidación de operaciones con títulos valores o monedas extranjeras con cotización

## Unidad `cap::4.2.2` (punto_no_item)
- herencia: [intro 4.2] –OTC o negociados en mercados regulados– y con liquidación diferida.
La exigencia computada en este punto –basada en el Enfoque Estándar para la medición de
la exigencia por capital por riesgo de crédito de contraparte (“Standardised Approach for
measuring Counterparty Credit Risk”, SA-CCR)– se aplicará a operaciones con derivados
–OTC o negociados en mercados regulados– y con liquidación diferida, ya que las operacio-
nes de financiación con títulos valores (“Securities Financing Transactions”,
- texto propio: 4.2.2. Ajuste de valuación del crédito (CVA).
Además de la exposición al riesgo de incumplimiento determinada en el punto 4.2.1.,
las entidades financieras deberán observar una exigencia de capital por el riesgo de
pérdidas derivadas de valuar a precios de mercado el riesgo de contraparte esperado
–pérdidas conocidas como “ajustes de valuación del crédito”, CVA–.
Las entidades no observarán esta exigencia de capital cuando se trate de operaciones
de financiación con títulos valores –tales como las operaciones de pase– y en las ope-
raciones celebradas con una entidad de contraparte central (CCP).
La exigencia de capital por CVA correspondiente a la totalidad de contrapartes se de-
terminará según la siguiente expresión para un horizonte de riesgo de un año:
2
   
0,5 EADTotal Mcobertura w
w M B M B  
x x x x x x
i i i i i ind ind ind
 
K(CVA)2,33 i ind
x
 2
0,75 w2 EADTotal Mcobertura
M B
x x x x
i i i i i
i
donde:
- w: ponderador aplicable a la contraparte i, que se establece en 0 % para el sector
i
público no financiero y Banco Central, y en 3 % para el resto de las contrapar-
tes –excepto que se trate de entidades del exterior que no cumplan con lo pre-
visto en el punto 3.1. o 3.2., según corresponda, de las normas sobre “Evalua-
ciones crediticias”, en cuyo caso se les aplicará un ponderador del 10 %–. A los
efectos del cumplimiento de los citados puntos de las normas sobre “Evalua-
ciones crediticias” se deberá contar con calificación internacional de riesgo “in-
vestment grade”.
- EADTotal: exposición al incumplimiento de la contraparte i –agregada para todos los
i
conjuntos de neteo, de corresponder, e incluido el efecto del activo en ga-
rantía–, a cuyo valor se le aplica el factor de descuento (1-exp (-0,05 x
M:))/(0,05 x M:).
i i
- B: valor 
- entidades de la unidad:
  - `e1` Obligacion: Exigencia de capital por CVA — Las entidades financieras deben observar una exigencia de capital por el riesgo de pérdidas derivadas de valuar a precios de mercado el riesgo de contraparte esperado (CVA).
  - `e2` Excepcion: Excepción CVA — operaciones de financiación con títulos valores — Las entidades no observarán la exigencia de capital por CVA cuando se trate de operaciones de financiación con títulos valores, tales como operaciones de pase.
  - `e3` Excepcion: Excepción CVA — operaciones con CCP — Las entidades no observarán la exigencia de capital por CVA en operaciones celebradas con una entidad de contraparte central (CCP).
  - `e4` Obligacion: Determinación de exigencia de capital por CVA según fórmula — La exigencia de capital por CVA correspondiente a la totalidad de contrapartes se determinará según una expresión matemática para un horizonte de riesgo de un año. La fórmula incluye ponderadores apli
  - `e5` Restriccion: Ponderador 0% — sector público no financiero y Banco Central — El ponderador aplicable a la contraparte i se establece en 0% para el sector público no financiero y Banco Central.
  - `e6` Restriccion: Ponderador 3% — resto de contrapartes — El ponderador aplicable a la contraparte i se establece en 3% para el resto de las contrapartes, excepto entidades del exterior que no cumplan con lo previsto en puntos 3.1 o 3.2 de normas sobre Evalu
  - `e7` Excepcion: Excepción ponderador — entidades del exterior sin calificación investment grade — Se aplicará un ponderador del 10% a entidades del exterior que no cumplan con lo previsto en puntos 3.1 o 3.2 de normas sobre Evaluaciones crediticias (requieren calificación internacional de riesgo i
  - `e8` Obligacion: Calificación investment grade para cumplimiento de normas — Para cumplir con los puntos 3.1 o 3.2 de las normas sobre Evaluaciones crediticias, se debe contar con calificación internacional de riesgo investment grade.
  - `e9` Restriccion: Elegibilidad de coberturas — solo para mitigación de CVA — Solo las coberturas utilizadas con el propósito de mitigar el riesgo de CVA y gestionadas como tales son elegibles para ser consideradas en el cómputo de la exigencia de capital.
  - `e10` Definicion: Coberturas admisibles para CVA — Son coberturas admisibles: swaps de incumplimiento crediticio de referencia única (single-name CDS), swaps de incumplimiento crediticio contingentes de referencia única, otros instrumentos de cobertur
  - `e11` Restriccion: Exclusión de otros tipos de cobertura del cálculo de K(CVA) — No deben considerarse en el cálculo del K(CVA) otros tipos de cobertura del riesgo de contraparte, debiendo recibir el mismo tratamiento que cualquier otro instrumento de la cartera de la entidad fina
  - `e12` Restriccion: Exclusión de CDS por tramos o enésimo incumplimiento — Los swaps de incumplimiento crediticio por tramos o de enésimo incumplimiento no constituyen coberturas de CVA admisibles.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 exceptua_obligacion e1; e3 exceptua_obligacion e1
- NODOS A CLASIFICAR:
  - **caso 123** Excepcion `e7`: Excepción ponderador — entidades del exterior sin calificación investment grade | descripcion: Se aplicará un ponderador del 10% a entidades del exterior que no cumplan con lo previsto en puntos 3.1 o 3.2 de normas sobre Evaluaciones crediticias (requieren calificación internacional de riesgo investment grade). | tramo: excepto que se trate de entidades del exterior que no cumplan con lo previsto en el punto 3.1. o 3.2., según corresponda, de las normas sobre "Evaluaciones crediticias", en cuyo caso se les aplicará un ponderador del 10 %

## Unidad `ext::10.10.2.10` (item)
- herencia: [intro 10.10] de ingreso aduanero a partir del 13/12/23. | **[abre la lista]** [intro 10.10.2] Las entidades podrán dar acceso al mercado de cambios para cursar pagos con
registro de ingreso aduanero pendiente por operaciones no comprendidas en el
punto 10.6.6. cuando, en adición a los restantes requisitos aplicables, se verifique
alguna de las siguientes situaciones: | [cierre 10.10.2] Se podrá considerar como importación de bienes de capital a: i) aquellas que
correspondan a bienes cuyas posiciones arancelarias se encuentren clasificadas
como BK en la Nomenclatura Común del MERCOSUR (Decreto 690/02 y
complementarias) y ii) aquellas que incluyan otros bienes en la medida que los
bienes clasificados como BK representen como mínimo el 90% (noventa por
ciento) del valor FOB total de la operación y la entidad cuente con una declaración
jurada del cliente en la cual deje constancia
- texto propio: 10.10.2.10. El pago corresponda a la cancelación de deudas por operaciones
financiadas o garantizadas con anterioridad al 13/12/23 por
organismos internacionales y/o agencias oficiales de crédito.
Las entidades podrán considerar también como operación
garantizada por una agencia oficial de crédito a aquella que se
encuentre cubierta por una garantía emitida por una aseguradora
privada por cuenta y orden de un gobierno nacional de otro país. En
todos los casos, la entidad interviniente deberá contar con
documentación en la que conste explícitamente tal situación.
- entidades de la unidad:
  - `c1` Condicion: Pago cancelación deudas operaciones financiadas/garantizadas — El pago debe corresponder a la cancelación de deudas por operaciones que fueron financiadas o garantizadas antes del 13/12/23 por organismos internacionales y/o agencias oficiales de crédito
  - `e1` Excepcion: Garantía aseguradora privada por cuenta de gobierno extranjero — Se considera como operación garantizada por agencia oficial de crédito aquella cubierta por garantía de aseguradora privada emitida por cuenta y orden de un gobierno nacional extranjero
  - `o1` Obligacion: Documentación de garantía aseguradora privada — La entidad interviniente debe contar con documentación que conste explícitamente la situación de cobertura por garantía de aseguradora privada por cuenta y orden de gobierno extranjero
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 124** Excepcion `e1`: Garantía aseguradora privada por cuenta de gobierno extranjero | descripcion: Se considera como operación garantizada por agencia oficial de crédito aquella cubierta por garantía de aseguradora privada emitida por cuenta y orden de un gobierno nacional extranjero | tramo: Las entidades podrán considerar también como operación garantizada por una agencia oficial de crédito a aquella que se encuentre cubierta por una garantía emitida por una aseguradora privada por cuenta y orden de un gobierno nacional de otro país
  - **caso 215** Condicion `c1`: Pago cancelación deudas operaciones financiadas/garantizadas | descripcion: El pago debe corresponder a la cancelación de deudas por operaciones que fueron financiadas o garantizadas antes del 13/12/23 por organismos internacionales y/o agencias oficiales de crédito | tramo: El pago corresponda a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito

## Unidad `ext::3.5.3.2` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.5] exterior.
Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o
intereses de títulos de deuda con registro público en el exterior, otros endeudamientos
financieros con el exterior y títulos de deuda con registro público en el país denominados en
moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las
siguientes condiciones: | [intro 3.5.3] (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar.
En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir
del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado
de cambios deberá adicionalmente producirse una vez transcurridos, como mínimo,
desde la fecha de emisión: | [intro 3.5.3] i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25.
ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25.
iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25. | **[abre la lista]** [intro 3.5.3] El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa
del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y
se cumplan la totalidad de las condiciones estipuladas en cada caso:
- texto propio: 3.5.3.2. Precancelación de capital e intereses con la liquidación simultánea de otros
endeudamientos financieros comprendidos en este punto 3.5.
i) la precancelación de capital e intereses sea efectuada en manera
simultánea con los fondos liquidados de un nuevo endeudamiento
financiero comprendido en este punto 3.5.;
ii) la vida promedio del nuevo endeudamiento sea mayor a la vida
promedio remanente de la deuda que se precancela; y
iii) el monto acumulado de los vencimientos de capital del nuevo
endeudamiento en ningún momento podrá superar, hasta la fecha de
vencimiento de la deuda que se cancela, el monto que hubieran
acumulado los vencimientos de capital de la deuda que se cancela.
- entidades de la unidad:
  - `e1` Excepcion: Excepción precancelación con liquidación simultánea — Se exceptúa la exigencia de conformidad previa del BCRA para acceso al mercado de cambios antes del plazo establecido cuando se trata de precancelación de capital e intereses realizada simultáneamente
  - `c1` Condicion: Precancelación simultánea con nuevo endeudamiento — La precancelación de capital e intereses debe efectuarse de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero comprendido en el punto 3.5.
  - `c2` Condicion: Vida promedio del nuevo endeudamiento mayor — La vida promedio del nuevo endeudamiento debe ser mayor a la vida promedio remanente de la deuda que se precancela.
  - `r1` Restriccion: Límite monto acumulado vencimientos capital nuevo endeudamiento — El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos d
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1; c2 condicion_de e1; r1 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 125** Excepcion `e1`: Excepción precancelación con liquidación simultánea | descripcion: Se exceptúa la exigencia de conformidad previa del BCRA para acceso al mercado de cambios antes del plazo establecido cuando se trata de precancelación de capital e intereses realizada simultáneamente con fondos de nuevo endeudamiento financiero, siempre que se cumplan todas las condiciones especificadas. | tramo: El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso: i) la precancelación de capital e intereses sea efectuada en manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero comprendido en este punto 3.5.; ii) la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente de la deuda que se precancela; y iii) el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela.

## Unidad `cla::6.5.4.6` (item)
- herencia: [intro 6.5] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudor | **[abre la lista]** [intro 6.5.4] El análisis del flujo de fondos del cliente demuestra que es altamente improbable que
pueda atender la totalidad de sus compromisos financieros.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- texto propio: 6.5.4.6. Haya sido demandado judicialmente por la entidad para el cobro de su acreencia
cuando ello se encuentre vinculado a la falta de pago y registre mora en el pago
de hasta un año. Se excluyen los casos en que las acciones se refieren a la dis-
cusión sobre otros aspectos contractuales.
En caso de verificarse atrasos mayores a 540 días, corresponderá la reclasifica-
ción inmediata del deudor en el nivel siguiente inferior.
- entidades de la unidad:
  - `e1` Condicion: Demanda judicial por cobro vinculada a falta de pago — El cliente ha sido demandado judicialmente por la entidad para el cobro de su acreencia cuando ello se encuentra vinculado a la falta de pago
  - `e2` Condicion: Mora en pago hasta un año — El cliente registra mora en el pago de hasta un año
  - `e3` Excepcion: Excepción acciones sobre aspectos contractuales — Se excluyen de la clasificación en alto riesgo de insolvencia los casos en que las acciones judiciales se refieren a la discusión sobre otros aspectos contractuales, no al cobro de acreencia por falta
  - `e4` Obligacion: Reclasificación inmediata por atrasos mayores a 540 días — Cuando se verifiquen atrasos mayores a 540 días, corresponde la reclasificación inmediata del deudor al nivel siguiente inferior
- relaciones del crudo (sin establecida_en ni de sujeto): e1 condicion_de e4; e2 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 126** Excepcion `e3`: Excepción acciones sobre aspectos contractuales | descripcion: Se excluyen de la clasificación en alto riesgo de insolvencia los casos en que las acciones judiciales se refieren a la discusión sobre otros aspectos contractuales, no al cobro de acreencia por falta de pago | tramo: Se excluyen los casos en que las acciones se refieren a la discusión sobre otros aspectos contractuales

## Unidad `cap::5.2.3.3` (punto_no_item)
- herencia: [chapeau_seccion S5] A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o
parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera
de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las
técnicas previstas en el punto 5.1.
La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia-
ción con títulos valores (securities financing transactions, SFT) –co | [intro 5.2.3] rantías) personales y derivados de crédito.
- texto propio: 5.2.3.3. Requisitos operativos específicos para los derivados de crédito.
i) Los eventos de crédito especificados por las partes contratantes deberán
incluir, como mínimo: a) falta de pago de los importes vencidos según los
términos de la obligación subyacente que se encuentren vigentes al mo-
mento de producirse dicha falta de pago –pudiendo prever un período de
gracia cuando la obligación subyacente así lo contemple, en cuyo caso am-
bos períodos deberán estar en consonancia–; b) apertura de concurso pre-
ventivo, acuerdo preventivo extrajudicial, quiebra, insolvencia o incapacidad
del deudor para hacer frente a sus deudas, o su impago o la aceptación por
escrito de su incapacidad generalizada para satisfacerlas a su vencimiento
–así como eventos similares–; y c) reestructuración de la obligación subya-
cente que involucre la condonación o el aplazamiento del pago del capital,
los intereses y/o las comisiones, y que implique una pérdida.
ii) Se admitirá que el derivado de crédito cubra obligaciones que no incluyen la
obligación subyacente, es decir que exista un descalce entre esta última y la
obligación de referencia del derivado de crédito –obligación utilizada a efec-
tos de determinar el monto del efectivo a liquidar o la obligación a entregar–
siempre que: a) la obligación de referencia sea de categoría similar o inferior
a la obligación subyacente; b) ambas estén emitidas por el mismo deudor; y
c) existan cláusulas recíprocas en caso de incumplimiento o cláusulas recí-
procas de aceleración legalmente exigibles.
iii) El período de vigencia del derivado de crédito no podrá ser inferior a cual-
quier período de gracia necesario para poder determinar que efectivamente
se ha producido el incumplimiento de la obligación subyacente debido a su
impago.
iv) Los derivado
- entidades de la unidad:
  - `e1` Obligacion: Especificación de eventos de crédito en derivados — Las partes contratantes de derivados de crédito deben especificar eventos de crédito que incluyan como mínimo: falta de pago de importes vencidos (con posibilidad de período de gracia en consonancia c
  - `e2` Condicion: Descalce entre obligación subyacente y de referencia — El derivado de crédito puede cubrir obligaciones distintas de la subyacente (descalce) cuando: la obligación de referencia sea de categoría similar o inferior a la subyacente, ambas sean emitidas por 
  - `e3` Restriccion: Período de vigencia mínimo del derivado de crédito — El período de vigencia del derivado de crédito debe ser suficiente para determinar si se ha producido el incumplimiento de la obligación subyacente por impago, considerando cualquier período de gracia
  - `e4` Obligacion: Proceso de valuación para derivados con liquidación en efectivo — Para derivados de crédito con liquidación en efectivo, debe existir un sólido proceso de valuación que permita estimar la pérdida fehacientemente, y debe establecerse con exactitud el período durante 
  - `e5` Condicion: Aplicación de requisitos cuando obligación de referencia difiere de subyacente — Cuando la obligación de referencia para liquidación en efectivo sea distinta de la obligación subyacente, aplican los requisitos del acápite ii) (descalce entre obligaciones).
  - `e6` Obligacion: Transferencia de obligación subyacente al proveedor de protección — Cuando la liquidación de la protección crediticia requiera transferencia de la obligación subyacente, los términos de esa obligación deben permitir que el consentimiento para la transferencia no pueda
  - `e7` Obligacion: Identificación de responsables de determinar evento de crédito — Debe identificarse claramente a las partes responsables de determinar si ocurrió un evento de crédito. La responsabilidad no recae solo en el vendedor de protección; el comprador puede informar al ven
  - `e8` Condicion: Descalce en obligación para determinar evento de crédito — Se permite descalce entre la obligación subyacente y la utilizada para determinar evento de crédito cuando: la obligación sea de categoría similar o inferior a la subyacente, ambas sean emitidas por e
  - `e9` Excepcion: Reconocimiento parcial cuando reestructuración no está contemplada — Se permite reconocimiento parcial del derivado de crédito cuando la reestructuración de la obligación subyacente no esté contemplada pero se cumplan los demás requisitos de los acápites i) a vii).
  - `e10` Restriccion: Límite de reconocimiento cuando derivado es inferior a obligación — Cuando el importe del derivado de crédito es inferior o igual al de la obligación subyacente, puede computarse como máximo el 60% del valor de la cobertura.
  - `e11` Restriccion: Límite de reconocimiento cuando derivado es superior a obligación — Cuando el importe del derivado de crédito es superior al de la obligación subyacente, puede computarse como cobertura como máximo el 60% del valor de la obligación subyacente.
  - `e12` Restriccion: Reconocimiento de swaps de incumplimiento crediticio y rendimiento total — Solo se reconocen swaps de incumplimiento crediticio y de rendimiento total que brinden protección crediticia equivalente a garantías.
  - `e13` Excepcion: Excepción a reconocimiento de swaps de retorno total — No se reconoce la protección crediticia cuando una entidad financiera compra protección mediante swap de retorno total, contabiliza como renta neta los pagos netos recibidos, pero no contabiliza el de
  - `e14` Restriccion: Prohibición de reconocimiento de otros derivados de crédito — No se reconocen como cobertura del riesgo de crédito otros tipos de derivados de crédito, incluyendo derivados de primer y/o enésimo incumplimiento (first-to-default o nth-to-default).
- relaciones del crudo (sin establecida_en ni de sujeto): e13 exceptua e12
- NODOS A CLASIFICAR:
  - **caso 127** Excepcion `e9`: Reconocimiento parcial cuando reestructuración no está contemplada | descripcion: Se permite reconocimiento parcial del derivado de crédito cuando la reestructuración de la obligación subyacente no esté contemplada pero se cumplan los demás requisitos de los acápites i) a vii). | tramo: Cuando la reestructuración de la obligación subyacente no esté contemplada por el derivado de crédito, pero se cumplan los requisitos incluidos en los acápites i) a vii) precedentes, se permitirá el reconocimiento parcial del derivado de crédito.
  - **caso 140** Condicion `e5`: Aplicación de requisitos cuando obligación de referencia difiere de subyacente | descripcion: Cuando la obligación de referencia para liquidación en efectivo sea distinta de la obligación subyacente, aplican los requisitos del acápite ii) (descalce entre obligaciones). | tramo: Si la obligación de referencia especificada en el derivado de crédito, a efectos de la liquidación de la cobertura en efectivo, fuera distinta de la obligación subyacente, será de aplicación lo establecido en el acápite ii).
  - **caso 173** Condicion `e8`: Descalce en obligación para determinar evento de crédito | descripcion: Se permite descalce entre la obligación subyacente y la utilizada para determinar evento de crédito cuando: la obligación sea de categoría similar o inferior a la subyacente, ambas sean emitidas por el mismo deudor, y existan cláusulas recíprocas legalmente exigibles de incumplimiento cruzado o aceleración cruzada. | tramo: Se permite un descalce entre la obligación subyacente y la obligación utilizada a efectos de determinar si ha ocurrido un evento de crédito siempre que: a) esta última sea de categoría similar o inferior a la obligación subyacente, b) ambas obligaciones estén emitidas por el mismo deudor, y c) existan cláusulas recíprocas legalmente exigibles de incumplimiento cruzado o de aceleración cruzada.
  - **caso 174** Condicion `e2`: Descalce entre obligación subyacente y de referencia | descripcion: El derivado de crédito puede cubrir obligaciones distintas de la subyacente (descalce) cuando: la obligación de referencia sea de categoría similar o inferior a la subyacente, ambas sean emitidas por el mismo deudor, y existan cláusulas recíprocas de incumplimiento o aceleración legalmente exigibles. | tramo: Se admitirá que el derivado de crédito cubra obligaciones que no incluyen la obligación subyacente, es decir que exista un descalce entre esta última y la obligación de referencia del derivado de crédito –obligación utilizada a efectos de determinar el monto del efectivo a liquidar o la obligación a entregar– siempre que: a) la obligación de referencia sea de categoría similar o inferior a la obligación subyacente; b) ambas estén emitidas por el mismo deudor; y c) existan cláusulas recíprocas en caso de incumplimiento o cláusulas recíprocas de aceleración legalmente exigibles.

## Unidad `cap::6.2.1.2` (punto_no_item)
- herencia: [intro 6.2] La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu-
los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio-
nes preferidas no convertibles.
Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo
de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de
la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera.
L | [intro 6.2.1] La exigencia de capital por riesgo específico tiene por objeto proteger a la entidad ante
movimientos adversos en el precio de un título causados por factores relacionados con
su emisor. Para su cálculo, sólo se permitirá netear las posiciones opuestas respecto de
una misma especie, incluidas las posiciones en derivados.
- texto propio: 6.2.1.2. Exigencia de capital por riesgo específico en posiciones de titulización.
i) La exigencia de capital por riesgo específico de las posiciones de tituliza-
ción mantenidas en la cartera de negociación será el 8 % del importe pon-
derado por riesgo de las posiciones de titulización netas imputadas a esa
cartera, aplicando a ese efecto el ponderador resultante de observar las
disposiciones relativas al enfoque estandarizado –punto 3.1.11.–, multipli-
cado por un ratio de concentración.
El ratio de concentración se obtendrá de la suma de los valores nominales
de todos los tramos dividida por la suma de los valores nominales de los
tramos subordinados o de igual prelación (“pari passu”) que el tramo en el
que se tiene la posición.
Cuando la entidad no pueda determinar la exigencia de capital por riesgo
específico conforme a la metodología establecida o el ratio de concentra-
ción sea igual o superior a 12,5, se deberá aplicar a la posición neta un
ponderador de riesgo del 1250 %.
ii) Se podrá excluir del cómputo de la exigencia de capital por riesgo general
de mercado aquellas posiciones que, conforme a lo previsto en este punto,
conlleven un ponderador de riesgo del 1250 %.
- entidades de la unidad:
  - `e1` Operacion: Posiciones de titulización en cartera de negociación — Posiciones de titulización mantenidas en la cartera de negociación, sujetas a cálculo de exigencia de capital por riesgo específico.
  - `e2` Obligacion: Calcular exigencia capital riesgo específico titulización — La exigencia de capital por riesgo específico de las posiciones de titulización mantenidas en la cartera de negociación será el 8 % del importe ponderado por riesgo de las posiciones de titulización n
  - `e3` Definicion: Ratio de concentración — La suma de los valores nominales de todos los tramos dividida por la suma de los valores nominales de los tramos subordinados o de igual prelación (pari passu) que el tramo en el que se tiene la posic
  - `e4` Restriccion: Ponderador 1250 % cuando no se puede determinar exigencia — Cuando la entidad no pueda determinar la exigencia de capital por riesgo específico conforme a la metodología establecida o el ratio de concentración sea igual o superior a 12,5, se deberá aplicar a l
  - `e5` Condicion: Condición: no poder determinar exigencia o ratio ≥ 12,5 — La entidad no puede determinar la exigencia de capital por riesgo específico conforme a la metodología establecida, o el ratio de concentración es igual o superior a 12,5.
  - `e6` Excepcion: Exclusión de exigencia capital riesgo general mercado — Se podrá excluir del cómputo de la exigencia de capital por riesgo general de mercado aquellas posiciones que conlleven un ponderador de riesgo del 1250 %.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 regula e1; e4 limita e1; e5 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 128** Excepcion `e6`: Exclusión de exigencia capital riesgo general mercado | descripcion: Se podrá excluir del cómputo de la exigencia de capital por riesgo general de mercado aquellas posiciones que conlleven un ponderador de riesgo del 1250 %. | tramo: Se podrá excluir del cómputo de la exigencia de capital por riesgo general de mercado aquellas posiciones que, conforme a lo previsto en este punto, conlleven un ponderador de riesgo del 1250 %.

## Unidad `cap::6.2.2.3` (punto_no_item)
- herencia: [intro 6.2] La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu-
los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio-
nes preferidas no convertibles.
Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo
de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de
la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera.
L | [encabezado 6.2.2] 6.2.2. Exigencia de capital por riesgo general de mercado: método de los plazos residuales.
- texto propio: 6.2.2.3. Las posiciones compradas y vendidas en títulos de deuda e instrumentos deri-
vados se imputarán a escalas de vencimientos divididas en 15 o 13 bandas
temporales, según que el cupón del instrumento sea, o no, menor a 3 %. Los
instrumentos a tasa fija se asignarán según su plazo residual y los instrumen-
tos a tasa variable según el plazo que resta hasta el siguiente ajuste del inte-
rés. El ponderador de riesgo de los instrumentos a tasa variable dependerá de
que el cupón de renta del período en curso –o, de no estar disponible aún, el
último que se hubiera pagado– represente o no un rendimiento menor a 3 %
anual. Se podrán excluir las posiciones opuestas por el mismo importe en una
misma especie, como así también los derivados (“swaps”, “forwards”, futuros y
“forward rate agreements” –FRAs–) estrechamente relacionados y que cum-
plan las condiciones establecidas en el acápite i) del punto 6.2.3.5.
- entidades de la unidad:
  - `e1` Operacion: Imputación posiciones títulos deuda — escalas vencimientos — Las posiciones compradas y vendidas en títulos de deuda e instrumentos derivados se imputarán a escalas de vencimientos divididas en 15 bandas temporales si el cupón es mayor o igual a 3 %, o en 13 ba
  - `e2` Operacion: Asignación instrumentos tasa fija — plazo residual — Los instrumentos a tasa fija se asignarán según su plazo residual
  - `e3` Operacion: Asignación instrumentos tasa variable — plazo ajuste — Los instrumentos a tasa variable se asignarán según el plazo que resta hasta el siguiente ajuste del interés
  - `e4` Operacion: Determinación ponderador riesgo — tasa variable — El ponderador de riesgo de los instrumentos a tasa variable dependerá de si el cupón de renta del período en curso (o el último pagado si no está disponible) representa un rendimiento menor a 3 % anua
  - `e5` Excepcion: Exclusión posiciones opuestas mismo importe — Se pueden excluir las posiciones opuestas por el mismo importe en una misma especie de la imputación a escalas de vencimientos
  - `e6` Excepcion: Exclusión derivados relacionados — condiciones punto 6.2.3.5 — Se pueden excluir los derivados (swaps, forwards, futuros y FRAs) estrechamente relacionados que cumplan las condiciones establecidas en el acápite i) del punto 6.2.3.5
  - `e7` Potestad: Facultad de excluir posiciones y derivados — Facultad de excluir posiciones opuestas por el mismo importe en una misma especie y derivados estrechamente relacionados que cumplan condiciones específicas
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 129** Excepcion `e5`: Exclusión posiciones opuestas mismo importe | descripcion: Se pueden excluir las posiciones opuestas por el mismo importe en una misma especie de la imputación a escalas de vencimientos | tramo: Se podrán excluir las posiciones opuestas por el mismo importe en una misma especie
  - **caso 130** Excepcion `e6`: Exclusión derivados relacionados — condiciones punto 6.2.3.5 | descripcion: Se pueden excluir los derivados (swaps, forwards, futuros y FRAs) estrechamente relacionados que cumplan las condiciones establecidas en el acápite i) del punto 6.2.3.5 | tramo: Se podrán excluir [...] los derivados ("swaps", "forwards", futuros y "forward rate agreements" –FRAs–) estrechamente relacionados y que cumplan las condiciones establecidas en el acápite i) del punto 6.2.3.5

## Unidad `ext::2.2.1` (punto_no_item)
- herencia: [encabezado 2.2] 2.2. Cobros de exportaciones de servicios.
- texto propio: 2.2.1. Los cobros por la prestación de servicios por parte de residentes a no residentes
deberán ser ingresados y liquidados en el mercado de cambios en un plazo no mayor
a los 20 (veinte) días hábiles a partir de la fecha de su percepción en el exterior o en el
país o de su acreditación en cuentas del exterior.
En el caso de que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al
Régimen de Incentivo para Grandes Inversiones (RIGI) que haya declarado ante la
Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el
artículo 198 de la Ley 27.742 será aplicable la excepción prevista en el punto 14.1.3.
En el caso de fondos percibidos o acreditados en el exterior, se podrá considerar
cumplimentado el ingreso y liquidación por el monto equivalente a los gastos
habituales debitados por las entidades financieras del exterior por la transferencia de
fondos al país.
- entidades de la unidad:
  - `e1` Operacion: Ingreso y liquidación de cobros por servicios — Cobros por la prestación de servicios por parte de residentes a no residentes que deben ser ingresados y liquidados en el mercado de cambios
  - `e2` Obligacion: Plazo máximo 20 días hábiles — ingreso y liquidación de cobros — Los cobros por la prestación de servicios por parte de residentes a no residentes deberán ser ingresados y liquidados en el mercado de cambios en un plazo no mayor a los 20 (veinte) días hábiles a par
  - `e3` Condicion: Cliente VPU adherido al RIGI con declaración de beneficios — El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que haya declarado ante la Autoridad de Aplicación que preveía hacer uso de los benef
  - `e4` Excepcion: Excepción para VPU RIGI — punto 14.1.3 — Será aplicable la excepción prevista en el punto 14.1.3 para clientes VPU adheridos al RIGI que hayan declarado ante la Autoridad de Aplicación que preveían hacer uso de los beneficios del artículo 19
  - `e5` Condicion: Fondos percibidos o acreditados en el exterior — Los fondos han sido percibidos o acreditados en el exterior
  - `e6` Potestad: Facultad de considerar cumplido ingreso por gastos de transferencia — Se podrá considerar cumplimentado el ingreso y liquidación por el monto equivalente a los gastos habituales debitados por las entidades financieras del exterior por la transferencia de fondos al país
  - `e7` Comunicacion: Ley 27.742 — 
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e4; e5 condicion_de e6; e2 regula e1
- NODOS A CLASIFICAR:
  - **caso 131** Excepcion `e4`: Excepción para VPU RIGI — punto 14.1.3 | descripcion: Será aplicable la excepción prevista en el punto 14.1.3 para clientes VPU adheridos al RIGI que hayan declarado ante la Autoridad de Aplicación que preveían hacer uso de los beneficios del artículo 198 de la Ley 27.742 | tramo: será aplicable la excepción prevista en el punto 14.1.3

## Unidad `docvig::2.2.3` (punto_no_item)
- herencia: [encabezado 2.2] 2.2. Mayores de 75 años al 31.12.14 y los incapaces declarados judicialmente.
- texto propio: 2.2.3. A partir del año de otorgada la residencia permanente o temporaria en el país.
Documento Nacional de Identidad, manual o digital (DNI-m o DNI-d).
De existir prueba en contrario del país de domicilio, aplicará el punto 2.2.2.
En todos los casos deberá acreditarse la categoría de residencia, su vigencia y el tiempo de
radicación a partir de documentación emitida por la DNM.
El DNI-d en formato credencial virtual para dispositivos móviles inteligentes podrá ser exhibido
en las casas operativas de las entidades financieras en la medida que se observen las disposi-
ciones contenidas en el punto 2.12. de las normas sobre “Medidas mínimas de seguridad en
entidades financieras”.
- entidades de la unidad:
  - `c1` Condicion: Residencia permanente o temporaria otorgada — La documentación de identidad requerida aplica a partir del año en que se otorgó la residencia permanente o temporaria en el país
  - `op1` Operacion: Presentación de DNI manual o digital — Presentación de Documento Nacional de Identidad en formato manual o digital (DNI-m o DNI-d) como documentación válida
  - `ob1` Obligacion: Acreditación de categoría de residencia y vigencia — Deberá acreditarse la categoría de residencia, su vigencia y el tiempo de radicación a partir de documentación emitida por la Dirección Nacional de Migraciones
  - `pot1` Potestad: Exhibición de DNI-d en formato credencial virtual — El DNI-d en formato credencial virtual para dispositivos móviles inteligentes podrá ser exhibido en las casas operativas de las entidades financieras, sujeto a observancia de disposiciones sobre medid
  - `c2` Condicion: Observancia de medidas mínimas de seguridad — La exhibición del DNI-d en formato credencial virtual está condicionada a la observancia de las disposiciones sobre medidas mínimas de seguridad en entidades financieras
  - `exc1` Excepcion: Excepción por prueba en contrario del país de domicilio — Si existe prueba en contrario del país de domicilio, se aplicarán las disposiciones del punto 2.2.2 en lugar de las del presente punto
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de op1; c2 condicion_de pot1
- NODOS A CLASIFICAR:
  - **caso 132** Excepcion `exc1`: Excepción por prueba en contrario del país de domicilio | descripcion: Si existe prueba en contrario del país de domicilio, se aplicarán las disposiciones del punto 2.2.2 en lugar de las del presente punto | tramo: De existir prueba en contrario del país de domicilio, aplicará el punto 2.2.2

## Unidad `ext::3.5.3::intro` (intro)
- herencia: [encabezado 3.5.3] 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3
- texto propio: (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar.
En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir
del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado
de cambios deberá adicionalmente producirse una vez transcurridos, como mínimo,
desde la fecha de emisión:
i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25.
ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25.
iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25.
El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa
del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y
se cumplan la totalidad de las condiciones estipuladas en cada caso:
- entidades de la unidad:
  - `c1` Condicion: Acceso al mercado — anterioridad máxima 3 días — El acceso al mercado de cambios debe producirse con una anterioridad no mayor a 3 días hábiles antes de la fecha de vencimiento del servicio de capital o interés a pagar.
  - `c2` Condicion: Pago de capital — títulos emitidos 08/11/24 a 20/04/25 — 12 meses mínimo — Para pagos de capital de títulos de deuda emitidos entre el 08/11/24 y el 20/04/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos
  - `c3` Condicion: Pago de capital — títulos emitidos 21/04/25 a 15/05/25 — 6 meses mínimo — Para pagos de capital de títulos de deuda emitidos entre el 21/04/25 y el 15/05/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos
  - `c4` Condicion: Pago de capital — títulos emitidos a partir 16/05/25 — 18 meses mínimo — Para pagos de capital de títulos de deuda emitidos a partir del 16/05/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos, como mín
  - `p1` Potestad: Autorización previa del BCRA — acceso anticipado al mercado — El BCRA puede otorgar conformidad previa para que el acceso al mercado de cambios se produzca antes de los plazos indicados.
  - `e1` Excepcion: Excepción — conformidad previa del BCRA — situaciones especiales — No se requiere conformidad previa del BCRA si el deudor encuadra en alguna de las situaciones especiales que siguen y se cumplen todas las condiciones estipuladas en cada caso.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 133** Condicion `c1`: Acceso al mercado — anterioridad máxima 3 días | descripcion: El acceso al mercado de cambios debe producirse con una anterioridad no mayor a 3 días hábiles antes de la fecha de vencimiento del servicio de capital o interés a pagar. | tramo: El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar
  - **caso 216** Condicion `c2`: Pago de capital — títulos emitidos 08/11/24 a 20/04/25 — 12 meses mínimo | descripcion: Para pagos de capital de títulos de deuda emitidos entre el 08/11/24 y el 20/04/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 12 meses desde la fecha de emisión. | tramo: si el título fue emitido entre el 08/11/24 y el 20/04/25
  - **caso 217** Condicion `c3`: Pago de capital — títulos emitidos 21/04/25 a 15/05/25 — 6 meses mínimo | descripcion: Para pagos de capital de títulos de deuda emitidos entre el 21/04/25 y el 15/05/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 6 meses desde la fecha de emisión. | tramo: si el título fue emitido entre 21/04/25 y el 15/05/25
  - **caso 218** Condicion `c4`: Pago de capital — títulos emitidos a partir 16/05/25 — 18 meses mínimo | descripcion: Para pagos de capital de títulos de deuda emitidos a partir del 16/05/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 18 meses desde la fecha de emisión. | tramo: si el título fue emitido a partir del 16/05/25

## Unidad `ctacte::7.3.3.2` (punto_no_item)
- herencia: [encabezado 7.3.3] 7.3.3. En caso de denuncia de extravío.
- texto propio: 7.3.3.2. Cuando el banco desconozca el juzgado interviniente.
i) Solicitar fehacientemente al cuentacorrentista, dentro de las 48 horas hábi-
les bancarias de producido cada rechazo, que en el término de 10 días co-
rridos contados desde dicha fecha acredite la formulación de la pertinente
denuncia ante el Juez competente, mediante presentación de copia auten-
ticada.
ii) Si el cuentacorrentista acredita dicha formulación, remitir el cheque o certifi-
cado nominativo transferible rechazado –retenido según lo previsto en el
punto 7.3.1.– al juzgado interviniente en la causa.
iii) Cuando el cuentacorrentista no acredite la formulación de la denuncia judi-
cial informar al BCRA, a los efectos de que cada rechazo sea incluido en la
“Central de cheques rechazados”.
A tal fin, corresponde que al momento en que la pertinente información
quede disponible en el aludido banco, la Superintendencia de Entidades
Financieras y Cambiarias –Gestión de la Información– cuente con el detalle
de las gestiones realizadas y de los comprobantes respectivos.
La formulación de la citada denuncia fuera del término establecido en el
punto 7.3.3.2. i) podrá dar lugar a las gestiones para lograr la eventual baja
de los rechazos de aquella central.
iv) Archivar las actuaciones vinculadas a la denuncia recibida y a los rechazos
efectuados por tal motivo.
- entidades de la unidad:
  - `e1` Obligacion: Solicitar acreditación de denuncia judicial — El banco debe solicitar fehacientemente al cuentacorrentista que acredite la formulación de denuncia ante el Juez competente mediante copia autenticada.
  - `e2` Obligacion: Remitir cheque al juzgado si se acredita denuncia — El banco debe remitir el cheque o certificado nominativo transferible rechazado al juzgado interviniente cuando el cuentacorrentista acredita la formulación de la denuncia.
  - `e3` Condicion: Acreditación de formulación de denuncia judicial — Que el cuentacorrentista acredite la formulación de la denuncia ante el Juez competente.
  - `e4` Obligacion: Informar al BCRA si no se acredita denuncia — El banco debe informar al BCRA cuando el cuentacorrentista no acredite la formulación de la denuncia judicial, a fin de que cada rechazo sea incluido en la Central de cheques rechazados.
  - `e5` Condicion: No acreditación de formulación de denuncia judicial — Que el cuentacorrentista no acredite la formulación de la denuncia judicial.
  - `e6` Obligacion: Proporcionar detalle de gestiones a la Superintendencia — El banco debe proporcionar a la Superintendencia de Entidades Financieras y Cambiarias el detalle de las gestiones realizadas y de los comprobantes respectivos cuando la información quede disponible.
  - `e7` Potestad: Gestiones para baja de rechazos por denuncia fuera de término — La Superintendencia o el BCRA puede realizar gestiones para lograr la eventual baja de los rechazos de la Central de cheques rechazados cuando la denuncia se formula fuera del término establecido.
  - `e8` Obligacion: Archivar actuaciones vinculadas a la denuncia — El banco debe archivar las actuaciones vinculadas a la denuncia recibida y a los rechazos efectuados por tal motivo.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 134** Condicion `e3`: Acreditación de formulación de denuncia judicial | descripcion: Que el cuentacorrentista acredite la formulación de la denuncia ante el Juez competente. | tramo: Si el cuentacorrentista acredita dicha formulación
  - **caso 206** Condicion `e5`: No acreditación de formulación de denuncia judicial | descripcion: Que el cuentacorrentista no acredite la formulación de la denuncia judicial. | tramo: Cuando el cuentacorrentista no acredite la formulación de la denuncia judicial

## Unidad `ext::7.10.2.2` (item)
- herencia: [intro 7.10] del régimen de fomento de inversión para las exportaciones (Decreto 234/21). | **[abre la lista]** [intro 7.10.2] que se verifiquen la totalidad de las siguientes condiciones:
- texto propio: 7.10.2.2. El monto aplicado en el año calendario no supere el equivalente al 25%
(veinticinco por ciento) del monto bruto de las inversiones ingresadas para
financiar el desarrollo del proyecto que genera las exportaciones aplicadas.
El monto bruto de las inversiones ingresadas a computar surgirá de la
suma de los montos acumulados por:
i) las liquidaciones efectuadas en el mercado de cambios a partir del
07/04/21 en concepto de endeudamientos financieros comprendidos
en el punto 3.5. y aportes de inversión extranjera directa.
ii) el valor FOB de las importaciones de bienes de capital incorporados al
proyecto de inversión cuyo registro de ingreso aduanero se haya
producido a partir del 07/04/21 y que hayan tenido una financiación de
un acreedor del exterior con una vida promedio no inferior a 1 (un) año
que no fue computada en el punto anterior o hayan constituido un
aporte de inversión directa en especie a la empresa residente.
Las inversiones podrán ser computadas una vez transcurrido un año
calendario desde su liquidación en el mercado de cambios y/o el registro de
ingreso aduanero de los bienes de capital, según corresponda.
En el caso de aportes de inversión directa, el cliente deberá presentar la
documentación que avale la capitalización definitiva del aporte. En caso de
no disponerla, deberá presentar constancia del inicio del trámite de
inscripción ante el Registro Público de Comercio de la decisión de
capitalización definitiva de los aportes de capital computados de acuerdo
con los requisitos legales correspondientes y comprometerse a presentar la
documentación de la capitalización definitiva del aporte dentro de los 365
(trescientos sesenta y cinco) días corridos desde el inicio del trámite.
- entidades de la unidad:
  - `c1` Condicion: Año calendario — monto aplicado — El monto aplicado en el año calendario no debe superar el equivalente al 25% del monto bruto de las inversiones ingresadas para financiar el desarrollo del proyecto que genera las exportaciones aplica
  - `d1` Definicion: Monto bruto de inversiones ingresadas — La suma de los montos acumulados por: (i) liquidaciones en el mercado de cambios a partir del 07/04/21 por endeudamientos financieros comprendidos en el punto 3.5 y aportes de inversión extranjera dir
  - `c2` Condicion: Plazo de un año desde liquidación o ingreso aduanero — Las inversiones pueden ser computadas solo después de transcurrido un año calendario desde su liquidación en el mercado de cambios y/o el registro de ingreso aduanero de los bienes de capital, según c
  - `o1` Obligacion: Presentar documentación de capitalización definitiva — En el caso de aportes de inversión directa, el cliente debe presentar la documentación que avale la capitalización definitiva del aporte.
  - `e1` Excepcion: Excepción — falta de documentación de capitalización — Cuando el cliente no dispone de la documentación que avala la capitalización definitiva del aporte.
  - `o2` Obligacion: Presentar constancia de inicio de trámite de inscripción — El cliente debe presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio de la decisión de capitalización definitiva de los aportes de capital computados de acue
  - `o3` Obligacion: Comprometerse a presentar documentación de capitalización — El cliente debe comprometerse a presentar la documentación de la capitalización definitiva del aporte dentro de los 365 días corridos desde el inicio del trámite.
- relaciones del crudo (sin establecida_en ni de sujeto): e1 exceptua_obligacion o1; e1 condicion_de o2; e1 condicion_de o3
- NODOS A CLASIFICAR:
  - **caso 136** Condicion `c1`: Año calendario — monto aplicado | descripcion: El monto aplicado en el año calendario no debe superar el equivalente al 25% del monto bruto de las inversiones ingresadas para financiar el desarrollo del proyecto que genera las exportaciones aplicadas. | tramo: El monto aplicado en el año calendario no supere el equivalente al 25% (veinticinco por ciento) del monto bruto de las inversiones ingresadas para financiar el desarrollo del proyecto que genera las exportaciones aplicadas
  - **caso 225** Condicion `c2`: Plazo de un año desde liquidación o ingreso aduanero | descripcion: Las inversiones pueden ser computadas solo después de transcurrido un año calendario desde su liquidación en el mercado de cambios y/o el registro de ingreso aduanero de los bienes de capital, según corresponda. | tramo: Las inversiones podrán ser computadas una vez transcurrido un año calendario desde su liquidación en el mercado de cambios y/o el registro de ingreso aduanero de los bienes de capital, según corresponda

## Unidad `ext::3.5.3.5` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.5] exterior.
Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o
intereses de títulos de deuda con registro público en el exterior, otros endeudamientos
financieros con el exterior y títulos de deuda con registro público en el país denominados en
moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las
siguientes condiciones: | [intro 3.5.3] (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar.
En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir
del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado
de cambios deberá adicionalmente producirse una vez transcurridos, como mínimo,
desde la fecha de emisión: | [intro 3.5.3] i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25.
ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25.
iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25. | **[abre la lista]** [intro 3.5.3] El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa
del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y
se cumplan la totalidad de las condiciones estipuladas en cada caso:
- texto propio: 3.5.3.5. Precancelación de capital e intereses por parte de un VPU adherido al RIGI.
El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de
Incentivo para Grandes Inversiones (RIGI) que precancela capital o intereses
devengados por endeudamientos financieros comprendidos en este punto
3.5. en el marco de lo previsto en el punto 14.2.1.
- entidades de la unidad:
  - `c1` Condicion: Anterioridad máxima 3 días hábiles — El acceso al mercado de cambios debe producirse con una anterioridad no mayor a 3 días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar
  - `c2` Condicion: Plazo mínimo desde emisión — títulos 08/11/24 a 20/04/25 — Para títulos de deuda emitidos entre el 08/11/24 y el 20/04/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 12 meses desde la fecha de emisión
  - `c3` Condicion: Plazo mínimo desde emisión — títulos 21/04/25 a 15/05/25 — Para títulos de deuda emitidos entre el 21/04/25 y el 15/05/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 6 meses desde la fecha de emisión
  - `c4` Condicion: Plazo mínimo desde emisión — títulos a partir de 16/05/25 — Para títulos de deuda emitidos a partir del 16/05/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 18 meses desde la fecha de emisión
  - `e1` Excepcion: Excepción VPU-RIGI — precancelación de capital e intereses — Quedan exceptuados de los requisitos de anterioridad y plazo mínimo desde emisión los VPU adheridos al RIGI que precancelen capital o intereses devengados por endeudamientos financieros comprendidos e
  - `op1` Operacion: Precancelación de capital e intereses — VPU-RIGI — Precancelación de capital o intereses devengados por endeudamientos financieros comprendidos en el punto 3.5, realizada por un VPU adherido al RIGI
- relaciones del crudo (sin establecida_en ni de sujeto): e1 exceptua c1; e1 exceptua c2; e1 exceptua c3; e1 exceptua c4; e1 condicion_de op1
- NODOS A CLASIFICAR:
  - **caso 137** Condicion `c1`: Anterioridad máxima 3 días hábiles | descripcion: El acceso al mercado de cambios debe producirse con una anterioridad no mayor a 3 días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar | tramo: El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar
  - **caso 228** Condicion `c2`: Plazo mínimo desde emisión — títulos 08/11/24 a 20/04/25 | descripcion: Para títulos de deuda emitidos entre el 08/11/24 y el 20/04/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 12 meses desde la fecha de emisión | tramo: 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25
  - **caso 229** Condicion `c3`: Plazo mínimo desde emisión — títulos 21/04/25 a 15/05/25 | descripcion: Para títulos de deuda emitidos entre el 21/04/25 y el 15/05/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 6 meses desde la fecha de emisión | tramo: 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25
  - **caso 230** Condicion `c4`: Plazo mínimo desde emisión — títulos a partir de 16/05/25 | descripcion: Para títulos de deuda emitidos a partir del 16/05/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 18 meses desde la fecha de emisión | tramo: 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25

## Unidad `cap::6.2::intro` (intro)
- herencia: [encabezado 6.2] 6.2. Exigencia de capital por riesgo de tasa de interés.
- texto propio: La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu-
los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio-
nes preferidas no convertibles.
Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo
de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de
la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera.
Las acciones preferidas convertibles a un precio predeterminado en acciones ordinarias de la
emisora se tratarán según cómo se negocien, como títulos de deuda o como acciones.
La exigencia se obtendrá como la suma de dos exigencias calculadas por separado: una por
el riesgo específico de cada instrumento, ya sea que se trate de una posición vendida o com-
prada, y otra por el riesgo general de mercado –vinculado al efecto de cambios en la tasa de
interés sobre la cartera–, en la que se podrán compensar las posiciones compradas y vendi-
das en diferentes instrumentos.
Para los instrumentos derivados, serán de aplicación las disposiciones establecidas en el pun-
to 6.2.3.
- entidades de la unidad:
  - `e1` Operacion: Cálculo de exigencia de capital por riesgo de tasa de interés — Cálculo de la exigencia de capital por riesgo de tasa de interés sobre títulos de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las acciones preferidas no convertibles.
  - `e2` Operacion: Tratamiento de títulos en operaciones de pase pasivo — Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo de operación de financiación con títulos valores se trata como si todavía fuese propiedad de la entidad ce
  - `e3` Operacion: Tratamiento de acciones preferidas convertibles — Las acciones preferidas convertibles a un precio predeterminado en acciones ordinarias de la emisora se tratan según cómo se negocien, como títulos de deuda o como acciones.
  - `e4` Obligacion: Cálculo de exigencia como suma de dos componentes — La exigencia se obtendrá como la suma de dos exigencias calculadas por separado: una por el riesgo específico de cada instrumento (posición vendida o comprada) y otra por el riesgo general de mercado 
  - `e5` Condicion: Aplicación a instrumentos derivados — Para los instrumentos derivados, se aplican las disposiciones establecidas en el punto 6.2.3.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 138** Condicion `e5`: Aplicación a instrumentos derivados | descripcion: Para los instrumentos derivados, se aplican las disposiciones establecidas en el punto 6.2.3. | tramo: Para los instrumentos derivados, serán de aplicación las disposiciones establecidas en el punto 6.2.3.

## Unidad `ctacte::10.2.4.1` (punto_no_item)
- herencia: [intro 10.2.4] pago de cheques.
- texto propio: 10.2.4.1. Motivo que origina el cierre (decisión del banco, inclusión en la “Central de
cuentacorrentistas inhabilitados”, etc.), como consecuencia de lo cual serán
de aplicación las normas insertas en la Sección 9.
- entidades de la unidad:
  - `e1` Obligacion: Aviso de motivo del cierre de cuenta — El banco debe informar el motivo que origina el cierre de la cuenta, ya sea por decisión del banco, inclusión en la Central de cuentacorrentistas inhabilitados u otra causa.
  - `e2` Condicion: Aplicación de normas de la Sección 9 — La aplicación de las normas de la Sección 9 se condiciona al cierre de la cuenta o suspensión previa del pago de cheques.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 139** Condicion `e2`: Aplicación de normas de la Sección 9 | descripcion: La aplicación de las normas de la Sección 9 se condiciona al cierre de la cuenta o suspensión previa del pago de cheques. | tramo: como consecuencia de lo cual serán de aplicación las normas insertas en la Sección 9

## Unidad `cap::6.6.3.2` (punto_no_item)
- herencia: [intro 6.6.3] El método delta-plus utiliza los parámetros de sensibilidad o “letras griegas” asociadas
a las opciones para determinar el equivalente delta de cada posición.
Al equivalente delta de la posición, se le aplicará la metodología estándar de los pun-
tos 6.2. a 6.4., al efecto de calcular la exigencia de capital por riesgo general de mer-
cado para las opciones, al que se agregan exigencias adicionales para la cobertura de
los riesgos gamma –que mide la tasa de cambio del coeficiente delta ante vari
- texto propio: 6.6.3.2. Las posiciones ponderadas por delta cuyo subyacente sean títulos de deuda o
tasas de interés se asignarán a las bandas temporales establecidas en el pun-
to 6.2. Se informarán dos partes de la operación: uno cuando el contrato sub-
yacente entra en vigor y otro cuando vence. Los “caps” o “floors” se deberán
registrar como una combinación de un bono a interés variable y un conjunto
de opciones europeas. Serán de aplicación las disposiciones sobre posiciones
compensadas del acápite i) del punto 6.2.3.5.
- entidades de la unidad:
  - `e1` Operacion: Asignación posiciones delta a bandas temporales — Las posiciones ponderadas por delta cuyo subyacente sean títulos de deuda o tasas de interés se asignan a las bandas temporales establecidas en el punto 6.2.
  - `e2` Obligacion: Información dos partes operación — opciones delta — Se informarán dos partes de la operación: uno cuando el contrato subyacente entra en vigor y otro cuando vence.
  - `e3` Obligacion: Registro caps/floors como combinación — opciones europeas — Los "caps" o "floors" se deberán registrar como una combinación de un bono a interés variable y un conjunto de opciones europeas.
  - `e4` Condicion: Aplicación disposiciones posiciones compensadas — Se aplican las disposiciones sobre posiciones compensadas del acápite i) del punto 6.2.3.5.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 141** Condicion `e4`: Aplicación disposiciones posiciones compensadas | descripcion: Se aplican las disposiciones sobre posiciones compensadas del acápite i) del punto 6.2.3.5. | tramo: Serán de aplicación las disposiciones sobre posiciones compensadas del acápite i) del punto 6.2.3.5.

## Unidad `cap::3.1.8.1` (punto_no_item)
- herencia: [intro 3.1] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi-
cional o sintética, o a una estructura con similares características.
La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con-
ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de
deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset-
Backed Securities”, ABS) y bonos de tit | [encabezado 3.1.8] 3.1.8. Tratamiento de las titulizaciones con cláusulas de amortización anticipada.
- texto propio: 3.1.8.1. A los efectos de estimar la exigencia de capital, la entidad financiera originante
no podrá excluir las exposiciones objeto de titulización –punto 3.1.2.2.– ni podrá
reconocer el empleo de técnicas de CRC para la cobertura de la posición sub-
yacente en las titulizaciones sintéticas –punto 3.1.7.– si:
i) la entidad origina o patrocina una operación de titulización que incluye una o
más facilidades de crédito rotativas; y
ii) la operación de titulización incluye una cláusula de amortización anticipada
u otra disposición similar que, una vez activada:
a) subordine la participación de la entidad, preferente o de igual prelación
(“pari passu”), a la participación de otros inversores en las facilidades de
crédito rotativas subyacentes;
b) subordine aún más la participación subordinada de la entidad con
respecto a la participación de terceros; o
c) de cualquier otra forma aumente la exposición de la entidad a las pérdi-
das asociadas a las facilidades rotativas subyacentes.
- entidades de la unidad:
  - `e1` Restriccion: Exclusión de exposiciones en titulizaciones con amortización anticipada — La entidad financiera originante no podrá excluir las exposiciones objeto de titulización cuando origina o patrocina una operación de titulización que incluye una o más facilidades de crédito rotativa
  - `e2` Restriccion: Reconocimiento de técnicas CRC en titulizaciones sintéticas con amortización anticipada — La entidad financiera originante no podrá reconocer el empleo de técnicas de CRC para la cobertura de la posición subyacente en las titulizaciones sintéticas cuando origina o patrocina una operación d
  - `e3` Condicion: Originar o patrocinar titulización con facilidades rotativas — La entidad origina o patrocina una operación de titulización que incluye una o más facilidades de crédito rotativas.
  - `e4` Condicion: Cláusula de amortización anticipada activada — La operación de titulización incluye una cláusula de amortización anticipada u otra disposición similar que, una vez activada.
  - `e5` Condicion: Subordinación de participación de la entidad — La cláusula de amortización anticipada subordina la participación de la entidad, preferente o de igual prelación (pari passu), a la participación de otros inversores en las facilidades de crédito rota
  - `e6` Condicion: Subordinación adicional de participación subordinada — La cláusula de amortización anticipada subordina aún más la participación subordinada de la entidad con respecto a la participación de terceros.
  - `e7` Condicion: Aumento de exposición a pérdidas en facilidades rotativas — La cláusula de amortización anticipada de cualquier otra forma aumenta la exposición de la entidad a las pérdidas asociadas a las facilidades rotativas subyacentes.
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e1; e3 condicion_de e2; e4 condicion_de e1; e4 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 143** Condicion `e7`: Aumento de exposición a pérdidas en facilidades rotativas | descripcion: La cláusula de amortización anticipada de cualquier otra forma aumenta la exposición de la entidad a las pérdidas asociadas a las facilidades rotativas subyacentes. | tramo: de cualquier otra forma aumente la exposición de la entidad a las pérdidas asociadas a las facilidades rotativas subyacentes
  - **caso 246** Condicion `e6`: Subordinación adicional de participación subordinada | descripcion: La cláusula de amortización anticipada subordina aún más la participación subordinada de la entidad con respecto a la participación de terceros. | tramo: subordine aún más la participación subordinada de la entidad con respecto a la participación de terceros
  - **caso 247** Condicion `e5`: Subordinación de participación de la entidad | descripcion: La cláusula de amortización anticipada subordina la participación de la entidad, preferente o de igual prelación (pari passu), a la participación de otros inversores en las facilidades de crédito rotativas subyacentes. | tramo: subordine la participación de la entidad, preferente o de igual prelación ("pari passu"), a la participación de otros inversores en las facilidades de crédito rotativas subyacentes

## Unidad `cap::2.1` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca
- texto propio: 2.1. Exigencia.
Se determinará aplicando la siguiente expresión:
C = (k x 0,08 x APR ) + INC
RC C
donde:
C : exigencia de capital por riesgo de crédito.
RC
k: factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por
la SEFYC, teniendo en cuenta la siguiente escala:
[TABLA cap::tabla001 | página 7 | e0_tablas | columnas]
Columnas: Calificación asignada | Valor de “k”
Fila 1: Calificación asignada = 1 | Valor de “k” = 1
Fila 2: Calificación asignada = 2 | Valor de “k” = 1,03
Fila 3: Calificación asignada = 3 | Valor de “k” = 1,08
Fila 4: Calificación asignada = 4 | Valor de “k” = 1,13
Fila 5: Calificación asignada = 5 | Valor de “k” = 1,19
[FIN TABLA cap::tabla001]
A este efecto, se considerará la última calificación informada para el cálculo de la
exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la
notificación. En tanto no se comunique, el valor de “k” será igual a 1,03.
APR : activos ponderados por riesgo de crédito, determinados mediante la suma de los valores
C
obtenidos luego de aplicar la siguiente expresión:
A x p + PFB x CCF x p + no DvP + (DVP + RCD + INC(inversiones empresas)) x 12,5
significativas en
donde:
A: activos computables/exposiciones.
PFB: partidas fuera de balance (conceptos computables no registrados en el balance
de saldos).
CCF: factor de conversión crediticia.
p: ponderador de riesgo, en tanto por uno.
no DvP: operaciones sin entrega contra pago. Importe determinado mediante la suma
de los valores obtenidos luego de aplicar a las operaciones comprendidas el
correspondiente ponderador de riesgo (p) conforme a lo dispuesto en el punto
4.1.
DvP: operaciones de entrega contra pago fallidas (a los efectos de estas normas,
incluyen las operaciones de pago contra pago –PvP– fallidas)
- entidades de la unidad:
  - `e1` Operacion: Cálculo de exigencia de capital por riesgo de crédito — Exigencia de capital por riesgo de crédito (C) determinada mediante la fórmula: C = (k x 0,08 x APR) + INC, donde k es factor vinculado a calificación asignada por SEFYC, APR son activos ponderados po
  - `e2` Definicion: Factor k según calificación SEFYC — Factor vinculado a la calificación asignada a la entidad según evaluación de SEFYC. Valores: calificación 1 = 1; calificación 2 = 1,03; calificación 3 = 1,08; calificación 4 = 1,13; calificación 5 = 1
  - `e3` Obligacion: Aplicación de última calificación informada para cálculo de k — Se considerará la última calificación informada para el cálculo de la exigencia de capital que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación.
  - `e4` Condicion: Ausencia de comunicación de calificación — Cuando no se comunique calificación de la entidad, el valor de k será igual a 1,03.
  - `e5` Definicion: Activos ponderados por riesgo de crédito (APR) — Activos ponderados por riesgo de crédito, determinados mediante suma de: A x p + PFB x CCF x p + no DvP + (DVP + RCD + INC(inversiones empresas)) x 12,5, donde A son activos computables/exposiciones, 
  - `e6` Definicion: Activos computables/exposiciones (A) — Activos computables/exposiciones.
  - `e7` Definicion: Partidas fuera de balance (PFB) — Partidas fuera de balance, conceptos computables no registrados en el balance de saldos.
  - `e8` Definicion: Factor de conversión crediticia (CCF) — Factor de conversión crediticia.
  - `e9` Definicion: Ponderador de riesgo (p) — Ponderador de riesgo, en tanto por uno.
  - `e10` Definicion: Operaciones sin entrega contra pago (no DvP) — Operaciones sin entrega contra pago. Importe determinado mediante suma de valores obtenidos luego de aplicar a las operaciones comprendidas el correspondiente ponderador de riesgo (p) conforme a lo di
  - `e11` Definicion: Operaciones de entrega contra pago fallidas (DvP) — Operaciones de entrega contra pago fallidas, que incluyen operaciones de pago contra pago (PvP) fallidas. Importe determinado mediante suma de valores obtenidos luego de multiplicar exposición actual 
  - `e12` Definicion: Exigencia por riesgo de crédito de contraparte en derivados OTC (RCD) — Exigencia por riesgo de crédito de contraparte en operaciones con derivados extrabursátiles (over-the-counter, OTC), determinada conforme a lo establecido en punto 4.2.
  - `e13` Restriccion: Límite participación en capital de cada empresa — Límite máximo de participación en el capital de cada empresa del 15% de la responsabilidad patrimonial computable (RPC) de la entidad financiera del último día anterior al que corresponda.
  - `e14` Restriccion: Límite total participaciones en capital de empresas — Límite máximo de total de participaciones en el capital de empresas del 60% de la responsabilidad patrimonial computable (RPC) de la entidad financiera del último día anterior al que corresponda.
  - `e15` Definicion: Incremento por excesos a límites de inversiones en empresas (INC) — Incremento por los excesos a los límites de participación en el capital de cada empresa (15%) y total de participaciones en el capital de empresas (60%), calculados sobre la responsabilidad patrimonia
  - `e16` Definicion: Incremento por excesos a límites diversos (INC) — Incremento por excesos a: relación de activos inmovilizados y otros conceptos (Sección 4 del TO), límites en Financiamiento al Sector Público no Financiero, límites en Grandes Exposiciones al Riesgo d
  - `e17` Obligacion: Aplicación de disposiciones sobre incumplimientos de capitales mínimos — Serán de aplicación las disposiciones contenidas en la Sección 2 del TO sobre Incumplimientos de Capitales Mínimos y Relaciones Técnicas. Criterios Aplicables, salvo que resulte aplicable lo previsto 
  - `e18` Obligacion: Cómputo de exposición crediticia de cupos crediticios ampliados — Se computará en la expresión de APR la exposición crediticia resultante de utilización de cupos crediticios ampliados (puntos 6.1.1.2 y 6.1.2.1 acápite d del TO sobre Financiamiento al Sector Público 
  - `e19` Obligacion: Cómputo de uso de cupo ampliado — 25% primer mes — Cómputo como INC del uso del cupo ampliado: 25% a partir del primer mes de utilización económica de las obras o generación de ingresos.
  - `e20` Obligacion: Cómputo de uso de cupo ampliado — 50% séptimo mes — Cómputo como INC del uso del cupo ampliado: 50% a partir del séptimo mes de utilización económica de las obras o generación de ingresos.
  - `e21` Obligacion: Cómputo de uso de cupo ampliado — 100% décimo tercer mes — Cómputo como INC del uso del cupo ampliado: 100% a partir del décimo tercer mes de utilización económica de las obras o generación de ingresos.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 145** Condicion `e4`: Ausencia de comunicación de calificación | descripcion: Cuando no se comunique calificación de la entidad, el valor de k será igual a 1,03. | tramo: En tanto no se comunique, el valor de "k" será igual a 1,03.

## Unidad `ctacte::4.4.2` (punto_no_item)
- herencia: [encabezado 4.4] 4.4. Aval.
- texto propio: 4.4.2. Cuando la entidad depositaria avale cheques de pago diferido presentados por su inter-
medio y registrados sin aval por la entidad girada, aquélla emitirá los pertinentes certifi-
cados nominativos transferibles. Los certificados de que se trata podrán extenderse –a
solicitud del depositante de los cheques– en forma individual por cada uno de ellos o por
un conjunto.
- entidades de la unidad:
  - `e1` Operacion: Aval de cheques de pago diferido — La entidad depositaria avala cheques de pago diferido presentados por su intermedio y registrados sin aval por la entidad girada.
  - `e2` Obligacion: Emisión de certificados nominativos transferibles — La entidad depositaria emitirá los pertinentes certificados nominativos transferibles cuando avale cheques de pago diferido presentados por su intermedio y registrados sin aval por la entidad girada.
  - `e3` Potestad: Extensión de certificados individual o conjunta — Los certificados podrán extenderse a solicitud del depositante de los cheques en forma individual por cada uno de ellos o por un conjunto.
  - `e4` Condicion: Aval de cheques sin aval previo de la entidad girada — Los cheques de pago diferido deben estar registrados sin aval por la entidad girada.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condiciona e1
- NODOS A CLASIFICAR:
  - **caso 146** Condicion `e4`: Aval de cheques sin aval previo de la entidad girada | descripcion: Los cheques de pago diferido deben estar registrados sin aval por la entidad girada. | tramo: registrados sin aval por la entidad girada

## Unidad `ext::3.17.2::cierre` (cierre)
- herencia: [encabezado 3.17.2] 3.17.2. Los beneficiarios del Régimen de acceso a divisas para la producción incremental de
- texto propio: Si fuese necesario modificar la entidad nominada responsable de lo indicado en los
puntos 3.17.2.1. y/o 3.17.2.2., la nueva entidad será considerada responsable una
vez que el cambio de entidad haya quedado registrado en el BCRA y la entidad
previa le haya remitido el detalle de las certificaciones emitidas a nombre del cliente
hasta ese momento.
- entidades de la unidad:
  - `c1` Condicion: Cambio de entidad nominada responsable — Supuesto en que es necesario modificar la entidad nominada responsable de lo indicado en los puntos 3.17.2.1. y/o 3.17.2.2.
  - `o1` Obligacion: Registro de cambio de entidad en BCRA — La nueva entidad será considerada responsable una vez que el cambio de entidad haya quedado registrado en el BCRA
  - `o2` Obligacion: Remisión de detalle de certificaciones por entidad previa — La entidad previa debe remitir a la nueva entidad el detalle de las certificaciones emitidas a nombre del cliente hasta el momento del cambio
  - `c2` Condicion: Registro en BCRA y remisión de certificaciones — Supuesto en que concurren dos hechos: el cambio de entidad está registrado en el BCRA y la entidad previa ha remitido el detalle de certificaciones
- relaciones del crudo (sin establecida_en ni de sujeto): c2 condicion_de o1
- NODOS A CLASIFICAR:
  - **caso 147** Condicion `c1`: Cambio de entidad nominada responsable | descripcion: Supuesto en que es necesario modificar la entidad nominada responsable de lo indicado en los puntos 3.17.2.1. y/o 3.17.2.2. | tramo: Si fuese necesario modificar la entidad nominada responsable de lo indicado en los puntos 3.17.2.1. y/o 3.17.2.2.

## Unidad `ext::3.15.1` (punto_no_item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.15] financiación de operaciones de comercio exterior y garantías financieras otorgadas.
- texto propio: 3.15.1. Cancelación de líneas de crédito del exterior aplicadas por las entidades a la
financiación de operaciones de comercio exterior.
Las entidades financieras tendrán acceso al mercado de cambios a partir del
vencimiento para la cancelación de líneas de crédito otorgadas por entidades
financieras del exterior y aplicadas a la financiación de operaciones de exportación o
importación de residentes.
La cancelación de las líneas destinadas a la financiación de operaciones de
importación de bienes y servicios quedará adicionalmente alcanzada por las
condiciones específicas previstas en los puntos 10.7. y 13.6., respectivamente.
También podrán acceder para precancelar dichas líneas de crédito en la medida que
la financiación otorgada por la entidad local haya sido precancelada por el deudor. El
acceso al mercado de cambios por parte de los clientes para la precancelación de
estas financiaciones requerirá la conformidad previa del BCRA.
La entidad deberá contar con la validación de la declaración del “Relevamiento de
activos y pasivos externos” de la entidad, en la medida que sea aplicable.
- entidades de la unidad:
  - `e1` Operacion: Cancelación líneas crédito exterior — exportación/importación — Cancelación de líneas de crédito otorgadas por entidades financieras del exterior y aplicadas a la financiación de operaciones de exportación o importación de residentes.
  - `e2` Obligacion: Acceso mercado cambios — cancelación líneas crédito — Las entidades financieras tendrán acceso al mercado de cambios a partir del vencimiento para la cancelación de líneas de crédito otorgadas por entidades financieras del exterior y aplicadas a la finan
  - `e3` Condicion: Cancelación líneas importación — condiciones puntos 10.7 y 13.6 — La cancelación de líneas destinadas a la financiación de operaciones de importación de bienes y servicios está sujeta a las condiciones específicas previstas en los puntos 10.7. y 13.6.
  - `e4` Potestad: Precancelación líneas crédito — facultad acceso mercado cambios — Las entidades financieras podrán acceder al mercado de cambios para precancelar líneas de crédito en la medida que la financiación otorgada por la entidad local haya sido precancelada por el deudor.
  - `e5` Condicion: Precancelación por clientes — condición conformidad BCRA — El acceso al mercado de cambios por parte de los clientes para la precancelación de financiaciones requiere conformidad previa del BCRA.
  - `e6` Obligacion: Validación declaración activos pasivos externos — La entidad deberá contar con la validación de la declaración del 'Relevamiento de activos y pasivos externos' de la entidad, en la medida que sea aplicable.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condiciona e1; e6 condiciona e1
- NODOS A CLASIFICAR:
  - **caso 148** Condicion `e3`: Cancelación líneas importación — condiciones puntos 10.7 y 13.6 | descripcion: La cancelación de líneas destinadas a la financiación de operaciones de importación de bienes y servicios está sujeta a las condiciones específicas previstas en los puntos 10.7. y 13.6. | tramo: La cancelación de las líneas destinadas a la financiación de operaciones de importación de bienes y servicios quedará adicionalmente alcanzada por las condiciones específicas previstas en los puntos 10.7. y 13.6., respectivamente
  - **caso 231** Condicion `e5`: Precancelación por clientes — condición conformidad BCRA | descripcion: El acceso al mercado de cambios por parte de los clientes para la precancelación de financiaciones requiere conformidad previa del BCRA. | tramo: El acceso al mercado de cambios por parte de los clientes para la precancelación de estas financiaciones requerirá la conformidad previa del BCRA

## Unidad `ric::11.1.3` (punto_no_item)
- herencia: [intro 11.1] Conceptos comprendidos.
Se incluirán los flujos de fondos nocionales futuros sujetos a reapreciación de activos, pasi-
vos y partidas fuera de balance sensibles a variaciones en la tasa de interés.
Conceptos excluidos.
- Activos que se deducen del capital ordinario del nivel 1 (COn1);
- Activos fijos;
- Posiciones en acciones en la cartera de inversión.
Frecuencia y consolidación.
Los datos se informarán con frecuencia trimestral y se integrarán con los datos correspon-
dientes al último mes de 
- texto propio: 11.1.3. Instrucciones particulares para los cuadros 11.2.2. a) y 11.2.2. b).
Se aplicarán los criterios especificados anteriormente, considerando la apertura con-
ceptual definida en estos cuadros.
Consecuentemente, el total de flujos de fondos asignados de cada banda debe coin-
cidir con los totales informados en los cuadros 11.2.1. a) y b).
- entidades de la unidad:
  - `e1` Obligacion: Aplicar criterios especificados — cuadros 11.2.2 — Aplicar los criterios especificados anteriormente, considerando la apertura conceptual definida en los cuadros 11.2.2. a) y 11.2.2. b).
  - `e2` Condicion: Coincidencia de totales — flujos de fondos por banda — El total de flujos de fondos asignados de cada banda debe coincidir con los totales informados en los cuadros 11.2.1. a) y b).
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 151** Condicion `e2`: Coincidencia de totales — flujos de fondos por banda | descripcion: El total de flujos de fondos asignados de cada banda debe coincidir con los totales informados en los cuadros 11.2.1. a) y b). | tramo: el total de flujos de fondos asignados de cada banda debe coincidir con los totales informados en los cuadros 11.2.1. a) y b).

## Unidad `ric::S2` (seccion_sin_puntos)
- herencia: 
- texto propio: Sección 2. Entidades comprendidas.
CONSOLIDACIÓN
COD CASOS
0 Entidad que no consolida, con filiales en el país y en el exterior.
1 Entidad que consolida, con filiales en el país y en el exterior.
Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país
y en el exterior) – (con el alcance definido en el punto 6.2. de las normas sobre “Su-
2
pervisión consolidada”)
Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país y
9 en el exterior -que no consolida con otras entidades financieras-) - (con el alcance defini-
do en el punto 6.2. de las normas sobre “Supervisión consolidada”)
Consolidado trimestral (entidad financiera con filiales, subsidiarias significativas y otros
3
entes en el país y en el exterior) – (código de consolidación suspendido desde
abril/24 según punto 6.1. de las normas sobre “Supervisión consolidada”, excepto
para Ratio de apalancamiento, -Sección 10.- que continuará presentado código 3
con el alcance definido en el punto 6.2. de las normas citadas).
Código 9
No se presentará la información consolidada mensual, debiendo consignar en su lugar una decla-
ración conteniendo los siguientes datos:
- Exigencia por riesgo de crédito (código 70100000).
- Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estan-
darizada (sólo para el último mes del trimestre) (código 70500000).
- Exigencia por riesgo de mercado para las posiciones del último día del mes (código
70800000).
- Exigencia por riesgo operacional (código 70300000).
- Responsabilidad patrimonial computable.
- En los casos que corresponda:
a) Defecto de integración por riesgos de crédito, de mercado y operacional.
b) Incremento de la exigencia de capitales mínimos por excesos en la relación
- entidades de la unidad:
  - `e1` Definicion: Consolidación — código 0 — Entidad que no consolida, con filiales en el país y en el exterior.
  - `e2` Definicion: Consolidación — código 1 — Entidad que consolida, con filiales en el país y en el exterior.
  - `e3` Definicion: Consolidación — código 2 — Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país y en el exterior) con el alcance definido en el punto 6.2. de las normas sobre Supervisión consolidada.
  - `e4` Definicion: Consolidación — código 9 — Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país y en el exterior -que no consolida con otras entidades financieras-) con el alcance definido en el punto 6
  - `e5` Obligacion: Declaración — código 9 — exigencia riesgo crédito — Entidades con código 9 deberán presentar declaración conteniendo exigencia por riesgo de crédito (código 70100000).
  - `e6` Obligacion: Declaración — código 9 — riesgo tasa interés EVE — Entidades con código 9 deberán presentar declaración conteniendo cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada, sólo para el último mes del trim
  - `e7` Obligacion: Declaración — código 9 — exigencia riesgo mercado — Entidades con código 9 deberán presentar declaración conteniendo exigencia por riesgo de mercado para las posiciones del último día del mes (código 70800000).
  - `e8` Obligacion: Declaración — código 9 — exigencia riesgo operacional — Entidades con código 9 deberán presentar declaración conteniendo exigencia por riesgo operacional (código 70300000).
  - `e9` Obligacion: Declaración — código 9 — responsabilidad patrimonial — Entidades con código 9 deberán presentar declaración conteniendo responsabilidad patrimonial computable.
  - `e10` Obligacion: Declaración — código 9 — defecto integración riesgos — Entidades con código 9 deberán incluir en la declaración, en los casos que corresponda, detalle del defecto de integración por riesgos de crédito, de mercado y operacional.
  - `e11` Obligacion: Declaración — código 9 — incremento exigencia capitales — Entidades con código 9 deberán incluir en la declaración, en los casos que corresponda, incremento de la exigencia de capitales mínimos por excesos en la relación de activos inmovilizados y otros conc
  - `e12` Obligacion: Declaración — código 9 — detalle franquicias — Entidades con código 9 deberán incluir en la declaración, en los casos que corresponda, detalle de las eventuales franquicias otorgadas y otras facilidades.
  - `e13` Obligacion: Declaración — código 9 — reducción exigencia riesgo operacional — Entidades con código 9 deberán incluir en la declaración, en los casos que corresponda, reducción de exigencia de riesgo operacional y los datos para su determinación.
  - `e14` Obligacion: Información — código 3 — frecuencia trimestral — Entidades con código 3 deberán presentar información con frecuencia trimestral, integrada con saldos al cierre del trimestre bajo informe.
  - `e15` Obligacion: Información — código 3 — datos códigos 0, 1, 2 — Entidades con código 3 deberán incluir los datos previstos para los códigos 0, 1 y 2, excepto en el caso de riesgo de mercado y riesgo operacional, donde se informarán únicamente las partidas 70800000
  - `e16` Excepcion: Excepción — código 3 — riesgo mercado y operacional — Para entidades con código 3, en el caso de riesgo de mercado y riesgo operacional se informarán únicamente las partidas 70800000 y 70300000 y, de corresponder, 3600000Y y 37000000, en lugar de los dat
  - `e17` Obligacion: Cómputo — código 3 — instrucciones mensuales — Para determinar las exigencias de código 3, se tendrán en cuenta las instrucciones establecidas para el cómputo mensual, en lo que resulte pertinente.
  - `e18` Condicion: Condición — código 3 — suspensión desde abril/24 — Código 3 de consolidación trimestral está suspendido desde abril/24 según punto 6.1. de las normas sobre Supervisión consolidada, excepto para Ratio de apalancamiento (Sección 10) que continuará prese
- relaciones del crudo (sin establecida_en ni de sujeto): e16 exceptua_obligacion e15
- NODOS A CLASIFICAR:
  - **caso 153** Condicion `e18`: Condición — código 3 — suspensión desde abril/24 | descripcion: Código 3 de consolidación trimestral está suspendido desde abril/24 según punto 6.1. de las normas sobre Supervisión consolidada, excepto para Ratio de apalancamiento (Sección 10) que continuará presentando código 3. | tramo: código de consolidación suspendido desde abril/24 según punto 6.1. de las normas sobre "Supervisión consolidada", excepto para Ratio de apalancamiento, -Sección 10.- que continuará presentado código 3

## Unidad `ext::2.7::cierre` (cierre)
- herencia: [encabezado 2.7] 2.7. Otras excepciones a la obligación de liquidación.
- texto propio: A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin
movimiento de pesos, por los conceptos de compra y venta que correspondan, computándose
el monto por el cual se utiliza este mecanismo a los efectos de los límites mensuales que
pudieran ser aplicables según el caso.
En todos los casos se deberá contar con una declaración jurada del cliente en la que deja
constancia de tener conocimiento de que los fondos que se aplican bajo esta modalidad serán
computados a los efectos del cálculo de los límites que normativamente correspondan al
concepto de venta de cambio que corresponda y que no los excede.
- entidades de la unidad:
  - `e1` Operacion: Confección de boletos sin movimiento de pesos — Confección de dos boletos sin movimiento de pesos, por los conceptos de compra y venta que correspondan, para el registro de operaciones bajo la modalidad de excepciones a la obligación de liquidación
  - `e2` Obligacion: Cómputo de monto en límites mensuales — El monto utilizado bajo esta modalidad debe computarse a los efectos de los límites mensuales que pudieran ser aplicables según el caso.
  - `e3` Obligacion: Declaración jurada del cliente — conocimiento de cómputo — Debe contarse con una declaración jurada del cliente en la que conste que tiene conocimiento de que los fondos aplicados bajo esta modalidad serán computados a los efectos del cálculo de los límites q
  - `e4` Restriccion: Límite — fondos no exceden límites aplicables — Los fondos que se aplican bajo esta modalidad no deben exceder los límites que normativamente correspondan al concepto de venta de cambio que corresponda.
  - `e5` Condicion: Condición — declaración jurada del cliente — La operación bajo esta modalidad requiere que el cliente otorgue una declaración jurada en la que conste su conocimiento del cómputo de los fondos en los límites y que esos fondos no exceden los límit
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condiciona e1; e4 limita e1
- NODOS A CLASIFICAR:
  - **caso 154** Condicion `e5`: Condición — declaración jurada del cliente | descripcion: La operación bajo esta modalidad requiere que el cliente otorgue una declaración jurada en la que conste su conocimiento del cómputo de los fondos en los límites y que esos fondos no exceden los límites aplicables. | tramo: En todos los casos se deberá contar con una declaración jurada del cliente

## Unidad `cap::4.3.1.1` (punto_no_item)
- herencia: [intro 4.3] contraparte central.
Comprende a aquellas exposiciones de las entidades financieras con entidades de contrapar-
te central (CCP) que se originen en derivados OTC o negociados en mercados de valores y
en operaciones de financiación con títulos valores (“Securities Financing Transactions”, SFT)
y operaciones de liquidación diferida –definidas en el punto 4.2.–.
No están comprendidas las exposiciones originadas en operaciones al contado y que involu-
cren títulos valores, oro o moneda extranjera, c | [encabezado 4.3.1] 4.3.1. Definiciones.
- texto propio: 4.3.1.1. Entidad de contraparte central calificada (“Qualifying Central Counterparty”,
QCCP): aquella entidad autorizada a operar como CCP por el regulador de
su jurisdicción –en el país, la Comisión Nacional de Valores (CNV)– en
relación a los productos que ofrece, que se encuentre radicada y sea
supervisada en una jurisdicción en la que el regulador ha establecido –y
hecho público que aplica a dicha CCP en forma permanente– regulaciones
compatibles con las normas sobre “Principios para las infraestructuras del
mercado financiero”.
En el caso de que la CCP esté localizada en una jurisdicción en la que no
le sean aplicables los citados Principios, el BCRA podrá determinar que de
todos modos encuadra en la categoría de QCCP.
Además, a efectos de que la CCP pueda ser considerada QCCP, deberá
estar disponible la información necesaria para el cómputo de la exigencia
de capital para la exposición a fondos de garantía constituidos para hacer
frente a incumplimientos, conforme a lo previsto en el acápite ii) del punto
4.3.3.2.
Las entidades financieras podrán considerar como QCCP a la CCP que,
de acuerdo con las normas de la CNV,:
i) cuente con un informe de su auditoría externa acerca de si cumple o
cumple en general con los principios y recomendaciones de la Organi-
zación Internacional de Comisiones de Valores ("International Organi-
zation of Securities Commissions", IOSCO) y del Comité de Pagos e
Infraestructuras del Mercado ("Committee on Payments and Market In-
frastructures", CPMI) y,
ii) brinde la información necesaria para el cómputo de la exigencia de ca-
pital por riesgo de crédito de contraparte por la exposición de las enti-
dades financieras a los fondos de garantía constituidos para hacer
frente a incumplimientos (punto 4.3.3.2.).
- entidades de la unidad:
  - `e1` Definicion: QCCP — Entidad de contraparte central calificada — Aquella entidad autorizada a operar como CCP por el regulador de su jurisdicción (en Argentina, la CNV) en relación a los productos que ofrece, que se encuentre radicada y sea supervisada en una juris
  - `e2` Condicion: Condición — CCP en jurisdicción sin Principios aplicables — La CCP está localizada en una jurisdicción en la que no le son aplicables los Principios para las infraestructuras del mercado financiero.
  - `e3` Potestad: BCRA — Determinar QCCP en jurisdicción sin Principios — El BCRA tiene la facultad de determinar que una CCP encuadra en la categoría de QCCP aun cuando esté localizada en una jurisdicción en la que no le sean aplicables los Principios para las infraestruct
  - `e5` Condicion: Condición — Disponibilidad de información para cómputo de capital — Debe estar disponible la información necesaria para el cómputo de la exigencia de capital para la exposición a fondos de garantía constituidos para hacer frente a incumplimientos, conforme a lo previs
  - `e6` Obligacion: Entidades financieras — Considerar QCCP según normas CNV — Las entidades financieras tienen la facultad de considerar como QCCP a una CCP que cumpla con los requisitos establecidos en las normas de la CNV.
  - `e7` Condicion: Condición — Informe de auditoría externa sobre cumplimiento IOSCO/CPMI — La CCP cuenta con un informe de su auditoría externa acerca de si cumple o cumple en general con los principios y recomendaciones de IOSCO y del CPMI.
  - `e8` Condicion: Condición — Información para cómputo de capital por riesgo de crédito — La CCP brinda la información necesaria para el cómputo de la exigencia de capital por riesgo de crédito de contraparte por la exposición de las entidades financieras a los fondos de garantía constitui
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e3; e7 condicion_de e6; e8 condicion_de e6
- NODOS A CLASIFICAR:
  - **caso 155** Condicion `e5`: Condición — Disponibilidad de información para cómputo de capital | descripcion: Debe estar disponible la información necesaria para el cómputo de la exigencia de capital para la exposición a fondos de garantía constituidos para hacer frente a incumplimientos, conforme a lo previsto en el acápite ii) del punto 4.3.3.2. | tramo: deberá estar disponible la información necesaria para el cómputo de la exigencia de capital para la exposición a fondos de garantía constituidos para hacer frente a incumplimientos, conforme a lo previsto en el acápite ii) del punto 4.3.3.2

## Unidad `cap::8.6::cierre` (cierre)
- herencia: [encabezado 8.6] 8.6. Aportes de capital.
- texto propio: En los casos comprendidos en los puntos 8.6.1. y 8.6.2., los aportes deberán registrarse a su
valor de mercado. Se entenderá que los instrumentos cuentan con valor de mercado cuando
tengan cotización habitual en las bolsas y mercados regulados del país o del exterior en los
que se negocien, con transacciones relevantes en cuyo monto, la eventual liquidación de las
tenencias no pueda distorsionar significativamente su cotización.
En los casos del punto 8.6.3., los aportes deberán registrarse a su valor de mercado –con el al-
cance definido en el párrafo anterior– o, cuando se trate de entidades financieras que realicen
oferta pública de sus acciones, al precio que fije la autoridad de contralor competente del co-
rrespondiente mercado. No se admitirán los aportes de esta clase de instrumentos cuando no
se verifique el cumplimiento de las condiciones mencionadas precedentemente.
Cuando se trate de depósitos y otras obligaciones por intermediación financiera de la entidad
financiera que no cuenten con autorización para ser negociados en mercados secundarios re-
gulados del país o del exterior, los aportes se admitirán a su valor contable –capital, intereses,
ajustes, diferencias de cotización por moneda extranjera y, de corresponder, descuentos de
emisión–, conforme a las normas del BCRA. En el caso de los instrumentos de deuda compu-
tables como CA o PNc, al admitir los aportes, se deberá tener en cuenta lo dispuesto en el
n1
punto 8.3.4.
En ningún caso la capitalización de deuda podrá implicar una limitación o suspensión al dere-
cho de preferencia establecido en el artículo 194 de la Ley General de Sociedades, por lo que
no será aplicable lo dispuesto en el artículo 197 de dicha ley.
La decisión de capitalización de los conceptos indicados en los puntos 8.6.1. a 8.6.3. 
- entidades de la unidad:
  - `e1` Operacion: Registro de aportes a valor de mercado — Registro de aportes a su valor de mercado en los casos comprendidos en los puntos 8.6.1. y 8.6.2., cuando los instrumentos tengan cotización habitual en bolsas y mercados regulados del país o del exte
  - `e2` Definicion: Valor de mercado — instrumentos cotizados — Los instrumentos cuentan con valor de mercado cuando tengan cotización habitual en las bolsas y mercados regulados del país o del exterior en los que se negocien, con transacciones relevantes en cuyo 
  - `e3` Operacion: Registro de aportes punto 8.6.3. a valor de mercado o precio de autoridad — En los casos del punto 8.6.3., registro de aportes a su valor de mercado o, cuando se trate de entidades financieras que realicen oferta pública de sus acciones, al precio que fije la autoridad de con
  - `e4` Restriccion: Prohibición de aportes sin cumplimiento de condiciones — No se admitirán los aportes de instrumentos del punto 8.6.3. cuando no se verifique el cumplimiento de las condiciones de valor de mercado o precio de autoridad mencionadas precedentemente.
  - `e5` Operacion: Registro de depósitos y obligaciones a valor contable — Cuando se trate de depósitos y otras obligaciones por intermediación financiera de la entidad financiera que no cuenten con autorización para ser negociados en mercados secundarios regulados del país 
  - `e6` Condicion: Condición — instrumentos de deuda CA o PNc — Cuando se trate de instrumentos de deuda computables como CA o PNc, al admitir los aportes se debe tener en cuenta lo dispuesto en el punto 8.3.4.
  - `e7` Restriccion: Prohibición — capitalización de deuda no limita derecho de preferencia — La capitalización de deuda no podrá implicar una limitación o suspensión al derecho de preferencia establecido en el artículo 194 de la Ley General de Sociedades; por lo tanto, no será aplicable lo di
  - `e8` Obligacion: Decisión de capitalización ad referéndum de aprobación — La decisión de capitalización de los conceptos indicados en los puntos 8.6.1. a 8.6.3. por parte de la Asamblea (o autoridad equivalente) será ad referéndum de su aprobación por parte de la SEFyC o, e
  - `e9` Obligacion: Exposición en nota a estados contables de capitalización — La circunstancia de que la capitalización está ad referéndum de aprobación deberá ser expuesta en nota a los estados contables de los períodos siguientes (trimestral o anual, según corresponda), en lo
  - `e10` Obligacion: Deducción de aportes de RPC hasta notificación de aprobación — Hasta tanto se le haya notificado la aprobación de los aportes y en la medida en que éstos hayan sido contabilizados, se deducirán del respectivo componente de la RPC de la entidad financiera.
  - `e11` Obligacion: Mantenimiento de tratamiento de deuda subordinada capitalizada — Cuando los aportes contabilizados provengan de la capitalización de deuda subordinada o de instrumentos representativos de deuda que puedan ser considerados (total o parcialmente) como parte integrant
  - `e12` Comunicacion: Com. Autorización y composición del capital — 
- relaciones del crudo (sin establecida_en ni de sujeto): to referencia e12
- NODOS A CLASIFICAR:
  - **caso 156** Condicion `e6`: Condición — instrumentos de deuda CA o PNc | descripcion: Cuando se trate de instrumentos de deuda computables como CA o PNc, al admitir los aportes se debe tener en cuenta lo dispuesto en el punto 8.3.4. | tramo: En el caso de los instrumentos de deuda computables como CA o PNc, al admitir los aportes, se deberá tener en cuenta lo dispuesto en el punto 8.3.4

## Unidad `cap::3.1.7` (punto_no_item)
- herencia: [intro 3.1] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi-
cional o sintética, o a una estructura con similares características.
La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con-
ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de
deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset-
Backed Securities”, ABS) y bonos de tit
- texto propio: 3.1.7. Tratamiento de las operaciones sintéticas.
El empleo de técnicas de coberturas del riesgo de crédito (CRC) –tales como activos
admitidos como garantía, garantías personales y derivados de crédito– para cubrir la po-
sición subyacente se podrá reconocer a efectos de determinar la exigencia de capital co-
rrespondiente a titulizaciones sintéticas sólo si se satisfacen las siguientes condiciones:
i) Las coberturas del riesgo de crédito cumplen los requisitos establecidos en la Sec-
ción 5.
ii) Los activos admitidos como garantía se limitan a los especificados en los puntos
5.3.1.2. y 5.3.2.2. Podrán reconocerse los activos admisibles dados en garantía por
“entes de propósito especial” (SPE).
iii) Los garantes admisibles se limitan a los estipulados en el punto 5.4.1. Los SPE no
son garantes admisibles.
iv) La entidad transfiere a terceros el riesgo de crédito asociado a las exposiciones
subyacentes.
v) Los instrumentos utilizados para transferir el riesgo de crédito no contienen cláusu-
las o condiciones que limiten la cantidad del riesgo de crédito transferido, tales como
las siguientes:
a) Cláusulas que limiten de forma considerable la protección crediticia o la transfe-
rencia del riesgo de crédito, tales como cláusulas de amortización anticipada en
una titulización de facilidades crediticias rotativas que produzcan el efecto de
subordinar los derechos de la entidad financiera, umbrales por debajo de los cua-
les no se active la protección crediticia –incluso si se produce un evento de crédi-
to– establecidos en niveles elevados, o cláusulas que permitan la extinción de la
protección debido al deterioro de la calidad crediticia de las posiciones subyacen-
tes.
b) Cláusulas que obliguen a la entidad originante a alterar las exposiciones subya-
centes para mejorar 
- entidades de la unidad:
  - `e1` Operacion: Cobertura de riesgo de crédito en titulizaciones sintéticas — Empleo de técnicas de coberturas del riesgo de crédito (CRC) tales como activos admitidos como garantía, garantías personales y derivados de crédito para cubrir la posición subyacente en titulizacione
  - `e2` Obligacion: Reconocimiento de coberturas — requisitos de Sección 5 — Las coberturas del riesgo de crédito deben cumplir los requisitos establecidos en la Sección 5 para ser reconocidas a efectos de determinar la exigencia de capital en titulizaciones sintéticas
  - `e3` Restriccion: Límite cualitativo — activos admitidos como garantía — Los activos admitidos como garantía se limitan a los especificados en los puntos 5.3.1.2. y 5.3.2.2.
  - `e4` Excepcion: Excepción — SPE como garantes de activos en garantía — Se permite el reconocimiento de activos admisibles dados en garantía por entes de propósito especial (SPE), como excepción a la limitación de activos admitidos como garantía
  - `e5` Restriccion: Límite cualitativo — garantes admisibles — Los garantes admisibles se limitan a los estipulados en el punto 5.4.1.
  - `e6` Restriccion: Prohibición — SPE como garantes — Los entes de propósito especial (SPE) no son garantes admisibles
  - `e7` Obligacion: Transferencia de riesgo de crédito a terceros — La entidad debe transferir a terceros el riesgo de crédito asociado a las exposiciones subyacentes
  - `e8` Restriccion: Prohibición — cláusulas limitantes de protección crediticia — Los instrumentos utilizados para transferir el riesgo de crédito no pueden contener cláusulas o condiciones que limiten la cantidad del riesgo de crédito transferido
  - `e9` Restriccion: Prohibición — cláusulas de amortización anticipada subordinante — Se prohíben cláusulas de amortización anticipada en una titulización de facilidades crediticias rotativas que produzcan el efecto de subordinar los derechos de la entidad financiera
  - `e10` Restriccion: Prohibición — umbrales elevados de activación de protección — Se prohíben umbrales por debajo de los cuales no se active la protección crediticia, incluso si se produce un evento de crédito, cuando están establecidos en niveles elevados
  - `e11` Restriccion: Prohibición — cláusulas de extinción por deterioro crediticio — Se prohíben cláusulas que permitan la extinción de la protección debido al deterioro de la calidad crediticia de las posiciones subyacentes
  - `e12` Restriccion: Prohibición — obligación de alterar exposiciones subyacentes — Se prohíben cláusulas que obliguen a la entidad originante a alterar las exposiciones subyacentes para mejorar la calidad crediticia promedio del conjunto de activos subyacente
  - `e13` Restriccion: Prohibición — incremento de costo de protección por deterioro crediticio — Se prohíben cláusulas que incrementen el costo de la protección crediticia para la entidad en respuesta al deterioro en la calidad crediticia del conjunto de activos subyacente
  - `e14` Restriccion: Prohibición — incremento de rendimiento a terceros por deterioro crediticio — Se prohíben cláusulas que incrementen el rendimiento pagadero a partes distintas de la entidad originante, tales como inversores y terceros proveedores de mejoras crediticias, en respuesta al deterior
  - `e15` Restriccion: Prohibición — aumento de posición a primera pérdida post-inicio — Se prohíben cláusulas que contemplen aumentos de la posición a primera pérdida retenida o de las mejoras crediticias provistas por la entidad originante después del inicio de la operación
  - `e16` Obligacion: Dictamen jurídico — exigibilidad del contrato — Debe contarse con dictamen jurídico competente que confirme la exigibilidad del contrato
  - `e17` Condicion: Opciones de exclusión — requisitos del punto 3.1.4 — Las opciones de exclusión deben satisfacer las condiciones estipuladas en el punto 3.1.4
  - `e18` Condicion: Condición — satisfacción de todas las condiciones enumeradas — El reconocimiento de coberturas del riesgo de crédito para determinar la exigencia de capital en titulizaciones sintéticas está condicionado a la satisfacción de todas las condiciones enumeradas (i a 
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1; e3 condicion_de e1; e5 condicion_de e1; e7 condicion_de e1; e8 condicion_de e1; e16 condicion_de e1; e17 condicion_de e1; e4 exceptua e3; e8 prohibe e1; e9 prohibe e1; e10 prohibe e1; e11 prohibe e1; e12 prohibe e1; e13 prohibe e1; e14 prohibe e1; e15 prohibe e1
- NODOS A CLASIFICAR:
  - **caso 157** Condicion `e18`: Condición — satisfacción de todas las condiciones enumeradas | descripcion: El reconocimiento de coberturas del riesgo de crédito para determinar la exigencia de capital en titulizaciones sintéticas está condicionado a la satisfacción de todas las condiciones enumeradas (i a vii) | tramo: se podrá reconocer a efectos de determinar la exigencia de capital correspondiente a titulizaciones sintéticas sólo si se satisfacen las siguientes condiciones

## Unidad `ext::7.7` (punto_no_item)
- herencia: [encabezado S7] Sección 7. Cobros de exportaciones de bienes.
- texto propio: 7.7. Cancelación de anticipos u otras financiaciones de exportación sin aplicación de divisas por
cobros de exportaciones de bienes.
Dadas las características que definen a los anticipos, prefinanciaciones de exportaciones -
locales o externas- y otras financiaciones de exportación, estas operaciones deberán ser
canceladas con fondos originados en el cobro de exportaciones de bienes, salvo que el cliente
pueda demostrar que no puede hacerlo de dicha forma por causas ajenas a su voluntad (por
ejemplo: desistimiento de la operación por parte del comprador externo, falta de pago por
parte del comprador externo, etc.).
El acceso al mercado local de cambios para cancelar anticipos u otras financiaciones de
exportaciones del exterior sin aplicación de divisas de cobros de exportaciones de bienes se
regirá por las normas para la cancelación de servicios de capital de préstamos financieros.
El acceso al mercado de cambios por parte de clientes para la precancelación de
financiaciones de exportación otorgadas por entidades financieras locales quedará sujeto a la
conformidad previa del BCRA. Este requisito se considerará cumplimentado en la medida que
el cliente registre, en la fecha de acceso al mercado, liquidaciones por cobros de
exportaciones de bienes por un monto igual o mayor al que se precancela a la entidad
financiera local.
En el caso de operaciones comprendidas en el “Seguimiento de anticipos y otras
financiaciones de exportación de bienes” (Sección 9.), la entidad para dar acceso al mercado
de cambios deberá contar con la correspondiente certificación por parte de la entidad
encargada del seguimiento de la financiación.
Los exportadores que registren anticipos u otras financiaciones de exportación comprendidas
en el “Seguimiento de anticipos y otras financiaciones de 
- entidades de la unidad:
  - `e1` Operacion: Cancelación de anticipos u otras financiaciones de exportación — Cancelación de anticipos, prefinanciaciones de exportaciones (locales o externas) y otras financiaciones de exportación sin aplicación de divisas por cobros de exportaciones de bienes
  - `e2` Obligacion: Cancelación con fondos de cobros de exportación — Las operaciones de anticipos, prefinanciaciones de exportaciones y otras financiaciones de exportación deberán ser canceladas con fondos originados en el cobro de exportaciones de bienes
  - `e3` Excepcion: Excepción por causas ajenas a la voluntad del cliente — No aplica la obligación de cancelación con fondos de cobros de exportación cuando el cliente demuestra que no puede hacerlo por causas ajenas a su voluntad
  - `e4` Obligacion: Acceso al mercado local de cambios — cancelación de anticipos — El acceso al mercado local de cambios para cancelar anticipos u otras financiaciones de exportaciones del exterior sin aplicación de divisas de cobros de exportaciones de bienes se regirá por las norm
  - `e5` Condicion: Conformidad previa del BCRA — precancelación de financiaciones — El acceso al mercado de cambios para precancelación de financiaciones de exportación otorgadas por entidades financieras locales requiere conformidad previa del BCRA
  - `e6` Excepcion: Cumplimiento de conformidad previa — liquidaciones de cobros — La conformidad previa del BCRA se considera cumplida cuando el cliente registra liquidaciones por cobros de exportaciones de bienes por monto igual o mayor al que se precancela
  - `e7` Condicion: Operaciones en Seguimiento de anticipos y financiaciones — Operaciones comprendidas en el Seguimiento de anticipos y otras financiaciones de exportación de bienes (Sección 9)
  - `e8` Obligacion: Certificación para acceso al mercado de cambios — La entidad debe contar con certificación de la entidad encargada del seguimiento de la financiación para dar acceso al mercado de cambios en operaciones comprendidas en el Seguimiento de anticipos y o
  - `e9` Obligacion: Notificación de disminución de capital adeudado — Los exportadores con anticipos u otras financiaciones de exportación por deudas directas no garantizadas por entidades financieras locales deben notificar a la entidad encargada del seguimiento cualqu
  - `e10` Definicion: Anticipos y prefinanciaciones de exportación — Operaciones que se caracterizan por ser anticipos, prefinanciaciones de exportaciones (locales o externas) y otras financiaciones de exportación
- relaciones del crudo (sin establecida_en ni de sujeto): e3 exceptua_obligacion e2; e6 exceptua_obligacion e5; e7 condicion_de e8
- NODOS A CLASIFICAR:
  - **caso 158** Condicion `e5`: Conformidad previa del BCRA — precancelación de financiaciones | descripcion: El acceso al mercado de cambios para precancelación de financiaciones de exportación otorgadas por entidades financieras locales requiere conformidad previa del BCRA | tramo: El acceso al mercado de cambios por parte de clientes para la precancelación de financiaciones de exportación otorgadas por entidades financieras locales quedará sujeto a la conformidad previa del BCRA

## Unidad `cla::7.2.2.1` (punto_no_item)
- herencia: [encabezado 7.2.2] 7.2.2. Riesgo bajo.
- texto propio: 7.2.2.1. En observación.
Comprende los clientes que registran incumplimientos ocasionales en la atención
de sus obligaciones, con atrasos de más de 31 hasta 90 días.
En cuanto a la situación jurídica del deudor, se considerará si mantiene conve-
nios de pago resultantes de concordatos judiciales o extrajudiciales homologados
(incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer
cuando se haya cancelado, al menos, el 10 % del importe involucrado en el cita-
do acuerdo.
Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de
pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inme-
diato superior, cuando hayan cumplido puntualmente o con atrasos que no su-
peren los 31 días, con el pago de 1 cuota o, cuando se trate de financiaciones de
pago único, periódico superior a bimestral o irregular, hayan cancelado al menos
el 5 % de sus obligaciones refinanciadas (por capital), con más la cantidad de
cuotas o el porcentaje acumulado que pudiera corresponder, respectivamente, si
la refinanciación se hubiera otorgado de encontrarse incluido el deudor en nive-
les inferiores.
El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su
deuda –aun cuando haya cancelado la cuota citada en el párrafo precedente– y
recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad”, y en la medida
en que dicha financiación adicional no hubiese sido cancelada, deberá permane-
cer en esta categoría por lo menos 180 días contados desde la fecha en que se
otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la
circunstancia más reciente.
En caso de verificarse atrasos mayores a 31 días en el pago de lo
- entidades de la unidad:
  - `e1` Definicion: En observación — deudores cartera consumo/vivienda — Categoría de clasificación que comprende los clientes que registran incumplimientos ocasionales en la atención de sus obligaciones, con atrasos de más de 31 hasta 90 días.
  - `e2` Condicion: Convenios de pago homologados — cancelación 10 % — Condición relativa a la situación jurídica del deudor: se considera si mantiene convenios de pago homologados a vencer cuando se haya cancelado al menos el 10 % del importe involucrado.
  - `e3` Operacion: Reclasificación a nivel inmediato superior — deudas refinanciadas — Reclasificación de clientes con deudas refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) al nivel inmediato superior, cuando hayan cumplido puntualmente o con atrasos no supe
  - `e4` Condicion: Cumplimiento puntual o atrasos ≤ 31 días — 1 cuota — Condición para reclasificación: cumplimiento puntual o atrasos que no superen los 31 días, con el pago de 1 cuota.
  - `e5` Condicion: Cancelación 5 % obligaciones refinanciadas — pago único/irregular — Condición para reclasificación en financiaciones de pago único, periódico superior a bimestral o irregular: cancelación de al menos el 5 % de las obligaciones refinanciadas (por capital).
  - `e6` Restriccion: Permanencia mínima 180 días — crédito adicional — El deudor clasificado en esta categoría que haya refinanciado su deuda y recibido crédito adicional en los términos del punto 2.2.5 de las normas sobre Previsiones mínimas por riesgo de incobrabilidad
  - `e7` Condicion: Atrasos mayores a 31 días — servicios deuda refinanciada — Condición que activa reclasificación inmediata: verificación de atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta cate
  - `e8` Operacion: Reclasificación inmediata — atrasos mayores a 31 días — Reclasificación inmediata del deudor en el nivel que resulte de considerar la cantidad total de días de atraso (días efectivamente registrados desde la primera cuota impaga de la refinanciación más lo
  - `e9` Condicion: Deudas refinanciadas — obligaciones pago periódico — Condición: deudas refinanciadas mediante obligaciones de pago periódico (mensual o bimestral).
- relaciones del crudo (sin establecida_en ni de sujeto): e4 condicion_de e3; e5 condicion_de e3; e9 condicion_de e3; e7 condicion_de e8
- NODOS A CLASIFICAR:
  - **caso 160** Condicion `e2`: Convenios de pago homologados — cancelación 10 % | descripcion: Condición relativa a la situación jurídica del deudor: se considera si mantiene convenios de pago homologados a vencer cuando se haya cancelado al menos el 10 % del importe involucrado. | tramo: se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer cuando se haya cancelado, al menos, el 10 % del importe involucrado en el citado acuerdo.

## Unidad `cla::7.2.3` (punto_no_item)
- herencia: [encabezado 7.2] 7.2. Niveles de clasificación.
- texto propio: 7.2.3. Riesgo medio.
Comprende los clientes que muestran alguna incapacidad para cancelar sus obligacio-
nes, con atrasos de más de 90 hasta 180 días.
En cuanto a la situación jurídica del deudor, se considerará si mantiene convenios de pa-
go resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los
acuerdos preventivos extrajudiciales homologados) a vencer cuando aún no se haya can-
celado el 10 % del importe involucrado en el citado acuerdo.
A fin de determinar el importe de la cancelación, se admitirá computar el 50 % de las ga-
rantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados
a la explotación del deudor –con excepción de las hipotecas sobre inmuebles rurales que,
por lo tanto, serán computables–, observando los márgenes de cobertura establecidos en
las normas sobre “Garantías”.
Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago pe-
riódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior,
cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el
pago de 2 cuotas consecutivas o, cuando se trate de financiaciones de pago único, perió-
dico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligacio-
nes refinanciadas (por capital), con más la cantidad de cuotas o el porcentaje acumulado
que pudiera corresponder, respectivamente, si la refinanciación se hubiera otorgado de
encontrarse incluido el deudor en el nivel inferior.
El deudor refinanciado que haya cumplido con lo dispuesto en los párrafos precedentes,
según corresponda, podrá ser reclasificado en el nivel inmediato superior si, además, el
resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel.
El deudor q
- entidades de la unidad:
  - `e1` Definicion: Riesgo medio — deudores — Categoría que comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días.
  - `e2` Condicion: Convenios de pago — situación jurídica — Se considera la situación jurídica del deudor respecto a convenios de pago de concordatos judiciales o extrajudiciales homologados, incluyendo acuerdos preventivos extrajudiciales homologados, cuando 
  - `e3` Obligacion: Computar garantías adicionales — determinación de cancelación — Para determinar el importe de la cancelación, se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deud
  - `e4` Condicion: Reclasificación — deudas refinanciadas con pago periódico — Condición para reclasificación de deudores cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral): cumplimiento puntual o con atrasos que no superen los 31
  - `e5` Condicion: Reclasificación — financiaciones de pago único o irregular — Condición para reclasificación cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular: cancelación de al menos el 5 % de las obligaciones refinanciadas (por capita
  - `e6` Potestad: Reclasificación en nivel inmediato superior — deudor refinanciado — Facultad de reclasificar en el nivel inmediato superior a clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral), cuando se cumplan las condicione
  - `e7` Condicion: Reclasificación — resto de deudas en nivel inmediato superior — Condición adicional para reclasificación del deudor refinanciado: el resto de sus deudas debe reunir, como mínimo, las condiciones previstas en el nivel inmediato superior.
  - `e8` Restriccion: Permanencia mínima — deudor refinanciado con crédito adicional — Deudor clasificado en riesgo medio que haya refinanciado su deuda y recibido crédito adicional (en los términos del punto 2.2.5 de normas sobre Previsiones mínimas por riesgo de incobrabilidad), mient
  - `e9` Obligacion: Reclasificación inmediata — atrasos mayores a 31 días — Cuando se verifiquen atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en riesgo medio, corresponde la reclasificación inmedia
- relaciones del crudo (sin establecida_en ni de sujeto): e4 condicion_de e6; e5 condicion_de e6; e7 condicion_de e6
- NODOS A CLASIFICAR:
  - **caso 161** Condicion `e2`: Convenios de pago — situación jurídica | descripcion: Se considera la situación jurídica del deudor respecto a convenios de pago de concordatos judiciales o extrajudiciales homologados, incluyendo acuerdos preventivos extrajudiciales homologados, cuando aún no se haya cancelado el 10 % del importe involucrado. | tramo: se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer cuando aún no se haya cancelado el 10 % del importe involucrado en el citado acuerdo.

## Unidad `ctacte::9.2.1.4` (punto_no_item)
- herencia: [intro 9.2] Al verificarse cualquiera de las causales previstas en el punto 9.1., se observará el siguiente
procedimiento. | [encabezado 9.2.1] 9.2.1. Por parte del cuentacorrentista.
- texto propio: 9.2.1.4. Depositar en una cuenta especial, en tiempo oportuno para hacer frente a ellos
en las correspondientes fechas indicadas para el pago, los importes de los che-
ques de pago diferido (registrados o no) a vencer con posterioridad a la fecha de
notificación de cierre de la cuenta, que hayan sido incluidos en la nómina a que
se refiere el punto 9.2.1.1.
Cuando el cuentacorrentista revista la condición de usuario de servicios financieros
y la cuenta corriente de que se trate no prevea el uso de cheques ni registre saldo deu-
dor, deberá ofrecerse la utilización de mecanismos electrónicos simples, eficaces e in-
mediatos que permitan el cierre de la cuenta en un solo acto (tales como correo electró-
nico, telefonía, banca por Internet –“home banking”–, cajeros automáticos y terminales
de autoservicio).
A tal efecto, se deberá admitir como mínimo la utilización de la banca por Internet
–“home banking”–.
Sin perjuicio de ello, las entidades financieras deberán permitir el cierre de la cuenta co-
rriente en cualquier sucursal –no necesariamente en la de radicación de la cuenta–.
En todos los casos, la entidad deberá proporcionar –en ese mismo acto– constancia del
respectivo trámite de cierre, no pudiéndose devengar ningún tipo de comisión y/o cargo
desde la fecha de presentación de la correspondiente solicitud.
En caso de que registre saldo deudor, el cierre deberá al menos poder ser realizado en
forma presencial –en cualquier sucursal de la entidad financiera a opción del usuario–
conforme a lo previsto precedentemente.
Cuando existan fondos remanentes, a opción del titular, se procederá al cierre de la
cuenta transfiriéndose dichos fondos a saldos inmovilizados de acuerdo con el procedi-
miento establecido con carácter general para el tratamiento de dichos saldos.
- entidades de la unidad:
  - `e1` Obligacion: Depositar importes de cheques diferidos en cuenta especial — El cuentacorrentista debe depositar en una cuenta especial, en tiempo oportuno para hacer frente a los cheques de pago diferido (registrados o no) a vencer con posterioridad a la fecha de notificación
  - `e2` Condicion: Cuentacorrentista usuario de servicios financieros sin cheques ni saldo deudor — El cuentacorrentista reviste la condición de usuario de servicios financieros y la cuenta corriente no prevé el uso de cheques ni registra saldo deudor.
  - `e3` Obligacion: Ofrecer mecanismos electrónicos simples para cierre de cuenta — Debe ofrecerse la utilización de mecanismos electrónicos simples, eficaces e inmediatos que permitan el cierre de la cuenta en un solo acto, tales como correo electrónico, telefonía, banca por Interne
  - `e4` Condicion: Condición para ofrecer mecanismos electrónicos — Esta obligación se aplica cuando el cuentacorrentista reviste la condición de usuario de servicios financieros y la cuenta corriente no prevé el uso de cheques ni registra saldo deudor.
  - `e5` Obligacion: Admitir como mínimo banca por Internet para cierre — Se debe admitir como mínimo la utilización de la banca por Internet (home banking).
  - `e6` Obligacion: Permitir cierre de cuenta en cualquier sucursal — Las entidades financieras deben permitir el cierre de la cuenta corriente en cualquier sucursal, no necesariamente en la de radicación de la cuenta.
  - `e7` Obligacion: Proporcionar constancia de cierre sin comisiones — La entidad debe proporcionar en el mismo acto constancia del trámite de cierre, sin poder devengar ningún tipo de comisión y/o cargo desde la fecha de presentación de la solicitud.
  - `e8` Restriccion: Prohibición de devengar comisiones desde presentación de solicitud — No se puede devengar ningún tipo de comisión y/o cargo desde la fecha de presentación de la solicitud de cierre.
  - `e9` Condicion: Cierre con saldo deudor — Cuando la cuenta registra saldo deudor.
  - `e10` Obligacion: Permitir cierre presencial en cualquier sucursal con saldo deudor — El cierre debe poder ser realizado al menos en forma presencial en cualquier sucursal de la entidad financiera a opción del usuario.
  - `e11` Condicion: Existencia de fondos remanentes — Cuando existen fondos remanentes en la cuenta.
  - `e12` Potestad: Opción del titular para transferencia de fondos remanentes — A opción del titular, se procede al cierre de la cuenta transfiriendo los fondos remanentes a saldos inmovilizados conforme al procedimiento general para el tratamiento de dichos saldos.
- relaciones del crudo (sin establecida_en ni de sujeto): e4 condicion_de e3; e9 condicion_de e10; e11 condicion_de e12
- NODOS A CLASIFICAR:
  - **caso 165** Condicion `e2`: Cuentacorrentista usuario de servicios financieros sin cheques ni saldo deudor | descripcion: El cuentacorrentista reviste la condición de usuario de servicios financieros y la cuenta corriente no prevé el uso de cheques ni registra saldo deudor. | tramo: Cuando el cuentacorrentista revista la condición de usuario de servicios financieros y la cuenta corriente de que se trate no prevea el uso de cheques ni registre saldo deudor

## Unidad `ext::4.4.3` (item)
- herencia: **[abre la lista]** [intro 4.4] registro de ingreso aduanero hasta el 12/12/23.
Los importadores de bienes podrán suscribir Bonos para la Reconstrucción de una Argentina
Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por sus importaciones de
bienes con registro de ingreso aduanero hasta el 12/12/23.
La entidad que concrete la oferta de suscripción en nombre del cliente deberá contar con las
respectivas certificaciones sobre el monto pendiente de pago emitidas por la/s entidad/es
encargada/s del seguimiento de | [cierre 4.4] En caso de que la importación de bienes encuadre en los puntos 10.3.3., 10.9.1., 10.9.2. y
10.9.3., la entidad que concrete la oferta de suscripción en nombre del cliente deberá verificar
en forma directa lo previsto en los puntos 4.4.1. a 4.4.5. y, adicionalmente, contar con una
declaración jurada del cliente en la que deja constancia de que no ha solicitado la utilización
de este mecanismo en otra entidad por esa deuda. La entidad también deberá realizar la
correspondiente intervención de la d
- texto propio: 4.4.3. se cumplen las condiciones previstas en el punto 10.3.2.1. para el acceso al mercado
de cambios excepto aquella prevista en el inciso viii).
- entidades de la unidad:
  - `c1` Condicion: Cumplimiento condiciones acceso mercado cambios — Se cumplen las condiciones previstas en el punto 10.3.2.1. para el acceso al mercado de cambios
  - `e1` Excepcion: Excepción inciso viii) acceso mercado cambios — Queda exceptuada la condición prevista en el inciso viii) del punto 10.3.2.1. para el acceso al mercado de cambios
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 166** Condicion `c1`: Cumplimiento condiciones acceso mercado cambios | descripcion: Se cumplen las condiciones previstas en el punto 10.3.2.1. para el acceso al mercado de cambios | tramo: se cumplen las condiciones previstas en el punto 10.3.2.1. para el acceso al mercado de cambios

## Unidad `ext::4.4.4` (item)
- herencia: **[abre la lista]** [intro 4.4] registro de ingreso aduanero hasta el 12/12/23.
Los importadores de bienes podrán suscribir Bonos para la Reconstrucción de una Argentina
Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por sus importaciones de
bienes con registro de ingreso aduanero hasta el 12/12/23.
La entidad que concrete la oferta de suscripción en nombre del cliente deberá contar con las
respectivas certificaciones sobre el monto pendiente de pago emitidas por la/s entidad/es
encargada/s del seguimiento de | [cierre 4.4] En caso de que la importación de bienes encuadre en los puntos 10.3.3., 10.9.1., 10.9.2. y
10.9.3., la entidad que concrete la oferta de suscripción en nombre del cliente deberá verificar
en forma directa lo previsto en los puntos 4.4.1. a 4.4.5. y, adicionalmente, contar con una
declaración jurada del cliente en la que deja constancia de que no ha solicitado la utilización
de este mecanismo en otra entidad por esa deuda. La entidad también deberá realizar la
correspondiente intervención de la d
- texto propio: 4.4.4. el cliente cumple los requisitos complementarios previstos en los puntos 3.16.1. a
3.16.4. El punto 3.16.3. sólo será aplicable para clientes que no sean personas
humanas residentes.
- entidades de la unidad:
  - `c1` Condicion: Cumplimiento requisitos complementarios 3.16.1 a 3.16.4 — El cliente debe cumplir los requisitos complementarios previstos en los puntos 3.16.1. a 3.16.4.
  - `e1` Excepcion: Excepción punto 3.16.3 para personas humanas residentes — El punto 3.16.3. no es aplicable para clientes que sean personas humanas residentes.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 167** Condicion `c1`: Cumplimiento requisitos complementarios 3.16.1 a 3.16.4 | descripcion: El cliente debe cumplir los requisitos complementarios previstos en los puntos 3.16.1. a 3.16.4. | tramo: el cliente cumple los requisitos complementarios previstos en los puntos 3.16.1. a 3.16.4.

## Unidad `ctacte::8.2.3.1` (punto_no_item)
- herencia: [encabezado 8.2.3] 8.2.3. En la “Central de cheques denunciados como extraviados, sustraídos o adulterados”.
- texto propio: 8.2.3.1. Haber denunciado el titular o tenedor desposeído a la entidad el extravío, la
sustracción o la adulteración de los documentos mencionados en el punto 7.1.,
excepto la fórmula especial para solicitar cuadernos de cheques.
- entidades de la unidad:
  - `e1` Condicion: Denuncia de extravío, sustracción o adulteración — El titular o tenedor desposeído debe haber denunciado a la entidad el extravío, la sustracción o la adulteración de los documentos mencionados en el punto 7.1.
  - `e2` Excepcion: Excepción fórmula especial cuadernos de cheques — La fórmula especial para solicitar cuadernos de cheques queda exceptuada de la exigencia de denuncia de extravío, sustracción o adulteración.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 171** Condicion `e1`: Denuncia de extravío, sustracción o adulteración | descripcion: El titular o tenedor desposeído debe haber denunciado a la entidad el extravío, la sustracción o la adulteración de los documentos mencionados en el punto 7.1. | tramo: Haber denunciado el titular o tenedor desposeído a la entidad el extravío, la sustracción o la adulteración de los documentos mencionados en el punto 7.1.

## Unidad `ctacte::8.2.3.2` (punto_no_item)
- herencia: [encabezado 8.2.3] 8.2.3. En la “Central de cheques denunciados como extraviados, sustraídos o adulterados”.
- texto propio: 8.2.3.2. Haber denunciado la entidad el extravío, sustracción o adulteración en algunas
de sus filiales de los documentos mencionados en el punto 7.1., excepto la fór-
mula especial para solicitar cuadernos de cheques.
- entidades de la unidad:
  - `e1` Condicion: Denuncia de extravío, sustracción o adulteración en filiales — La entidad ha denunciado el extravío, sustracción o adulteración de documentos en algunas de sus filiales, conforme a lo mencionado en el punto 7.1.
  - `e2` Excepcion: Excepción fórmula especial para cuadernos de cheques — No se incluye en la denuncia la fórmula especial para solicitar cuadernos de cheques
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 172** Condicion `e1`: Denuncia de extravío, sustracción o adulteración en filiales | descripcion: La entidad ha denunciado el extravío, sustracción o adulteración de documentos en algunas de sus filiales, conforme a lo mencionado en el punto 7.1. | tramo: Haber denunciado la entidad el extravío, sustracción o adulteración en algunas de sus filiales de los documentos mencionados en el punto 7.1.

## Unidad `cla::6.5.4.1` (item)
- herencia: [intro 6.5] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudor | **[abre la lista]** [intro 6.5.4] El análisis del flujo de fondos del cliente demuestra que es altamente improbable que
pueda atender la totalidad de sus compromisos financieros.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- texto propio: 6.5.4.1. Presente una situación financiera ilíquida y muy alto nivel de endeudamiento, con
resultados negativos en la explotación y obligación de vender activos de impor-
tancia para la actividad desarrollada y que materialmente sean de magnitud sig-
nificativa. El flujo de fondos es manifiestamente insuficiente, no alcanzando a cu-
brir el pago de intereses, y es factible presumir que también tendrá dificultades
para cumplir eventuales acuerdos de refinanciación.
En el análisis que se lleve a cabo deberá tenerse en cuenta, de corresponder, la
eventual incidencia que en su capacidad de pago pueda tener la situación en la
que se encuentran los demás integrantes del grupo de contrapartes conectadas
al cual pertenece.
- entidades de la unidad:
  - `e1` Operacion: Situación financiera ilíquida con alto endeudamiento — Situación financiera caracterizada por iliquidez, muy alto nivel de endeudamiento, resultados negativos en la explotación y obligación de vender activos de importancia para la actividad desarrollada q
  - `e2` Operacion: Flujo de fondos insuficiente para cobertura de intereses — Flujo de fondos manifiestamente insuficiente que no alcanza a cubrir el pago de intereses
  - `e3` Condicion: Dificultades presumibles para cumplir acuerdos de refinanciación — Presunción de dificultades para cumplir eventuales acuerdos de refinanciación
  - `e4` Condicion: Incidencia de situación de contrapartes conectadas — Debe tenerse en cuenta la eventual incidencia en la capacidad de pago del cliente derivada de la situación de los demás integrantes del grupo de contrapartes conectadas al cual pertenece
  - `e5` Obligacion: Análisis de incidencia de contrapartes conectadas — En el análisis de clasificación deberá tenerse en cuenta, de corresponder, la eventual incidencia en la capacidad de pago del cliente derivada de la situación de los demás integrantes del grupo de con
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 177** Condicion `e3`: Dificultades presumibles para cumplir acuerdos de refinanciación | descripcion: Presunción de dificultades para cumplir eventuales acuerdos de refinanciación | tramo: es factible presumir que también tendrá dificultades para cumplir eventuales acuerdos de refinanciación
  - **caso 194** Condicion `e4`: Incidencia de situación de contrapartes conectadas | descripcion: Debe tenerse en cuenta la eventual incidencia en la capacidad de pago del cliente derivada de la situación de los demás integrantes del grupo de contrapartes conectadas al cual pertenece | tramo: la eventual incidencia que en su capacidad de pago pueda tener la situación en la que se encuentran los demás integrantes del grupo de contrapartes conectadas al cual pertenece

## Unidad `ext::14.4.1` (item)
- herencia: [chapeau_seccion S14] En esta sección se detallan las disposiciones complementarias en materia cambiaria que, en la
medida que las disposiciones generales no resulten más favorables, resultan aplicables a un
Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo los referidas al “Régimen de
Incentivo para Grandes Inversiones” (RIGI) establecido en el Título VII de la Ley 27.742 y
reglamentado por el Decreto 749/24 y concordantes. | **[abre la lista]** [intro 14.4] en materia de cobros de exportaciones de bienes y servicios.
Para dar acceso al mercado de cambios por cualquier concepto de egreso a un VPU que
haya solicitado la inscripción al RIGI indicando ante la Autoridad de Aplicación que preveía
hacer uso de los beneficios establecidos en el régimen en materia de cobro de exportaciones
de bienes y servicios, adicionalmente a los restantes requisitos que le sean aplicables a la
operación, las entidades deberán: | [cierre 14.4] Este requisito complementario no resultará aplicable cuando el acceso al mercado de
cambios del VPU sea con el objeto de realizar alguna de las siguientes operaciones: | [cierre 14.4] i) pagos de intereses admitidos por las financiaciones contempladas en los puntos | [cierre 14.4] 14.2.1.1. al 14.2.1.11. | [cierre 14.4] ii) pagos de utilidades y dividendos a accionistas no residentes admitidos en el punto | [cierre 14.4] 14.2.2. | [cierre 14.4] iii) pagos de capital de las financiaciones locales contempladas en los puntos 14.2.1.3. | [cierre 14.4] al 14.2.1.5.
- texto propio: 14.4.1. contar con una declaración jurada del representante legal del VPU, o un apoderado
con facultades suficientes para asumir este compromiso en nombre del VPU, en la
que deje constancia de que el importe total de divisas ingresadas desde el exterior y
liquidadas en el mercado de cambios por cualquier concepto por parte del VPU ad-
herido es, al momento de cada acceso, igual o mayor al monto que surge de sumar
el monto de la operación que se pretende cursar al monto total de los accesos al
mercado de cambios del VPU para egresos por todo concepto excepto los pagos
admitidos de intereses y/o utilidades y dividendos y/o el capital de financiaciones lo-
cales contempladas en los puntos 14.2.1.3. al 14.2.1.5.
La liquidación en el mercado de cambios de financiaciones en moneda extranjera
otorgadas al VPU por una entidad financiera local a partir de una línea de crédito del
exterior también deberán ser computadas a favor del VPU como parte de las divisas
ingresadas desde el exterior.
- entidades de la unidad:
  - `e1` Obligacion: Declaración jurada de divisas ingresadas — VPU RIGI — El VPU debe contar con una declaración jurada del representante legal o apoderado con facultades suficientes en la que conste que el importe total de divisas ingresadas desde el exterior y liquidadas 
  - `e2` Condicion: Divisas ingresadas igual o mayor al monto de operación más accesos previos — El importe total de divisas ingresadas desde el exterior y liquidadas en el mercado de cambios debe ser, al momento de cada acceso, igual o mayor al monto que resulta de sumar el monto de la operación
  - `e3` Obligacion: Computar liquidación de financiaciones en moneda extranjera como divisas ingresadas — La liquidación en el mercado de cambios de financiaciones en moneda extranjera otorgadas al VPU por una entidad financiera local a partir de una línea de crédito del exterior debe ser computada a favo
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 178** Condicion `e2`: Divisas ingresadas igual o mayor al monto de operación más accesos previos | descripcion: El importe total de divisas ingresadas desde el exterior y liquidadas en el mercado de cambios debe ser, al momento de cada acceso, igual o mayor al monto que resulta de sumar el monto de la operación pretendida al monto total de accesos previos para egresos, excluyendo pagos de intereses, utilidades, dividendos y capital de financiaciones locales. | tramo: el importe total de divisas ingresadas desde el exterior y liquidadas en el mercado de cambios por cualquier concepto por parte del VPU adherido es, al momento de cada acceso, igual o mayor al monto que surge de sumar el monto de la operación que se pretende cursar al monto total de los accesos al mercado de cambios del VPU para egresos por todo concepto excepto los pagos admitidos de intereses y/o utilidades y dividendos y/o el capital de financiaciones locales contempladas en los puntos 14.2.1.3. al 14.2.1.5.

## Unidad `ext::3.5.1.1` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.5] exterior.
Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o
intereses de títulos de deuda con registro público en el exterior, otros endeudamientos
financieros con el exterior y títulos de deuda con registro público en el país denominados en
moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las
siguientes condiciones: | **[abre la lista]** [intro 3.5.1] un monto equivalente al valor nominal del endeudamiento financiero.
Este requisito se considerará cumplimentado en los siguientes casos:
- texto propio: 3.5.1.1. los endeudamientos desembolsados con anterioridad al 01/09/19.
- entidades de la unidad:
  - `e1` Condicion: Endeudamientos desembolsados antes 01/09/19 — El requisito de demostrar ingreso y liquidación de divisas se considera cumplimentado cuando los endeudamientos fueron desembolsados con anterioridad al 01/09/19
  - `e2` Excepcion: Excepción requisito liquidación divisas — endeudamientos anteriores 01/09/19 — Quedan exceptuados del requisito de demostrar ingreso y liquidación de divisas en el mercado de cambios los endeudamientos desembolsados con anterioridad al 01/09/19
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 179** Condicion `e1`: Endeudamientos desembolsados antes 01/09/19 | descripcion: El requisito de demostrar ingreso y liquidación de divisas se considera cumplimentado cuando los endeudamientos fueron desembolsados con anterioridad al 01/09/19 | tramo: los endeudamientos desembolsados con anterioridad al 01/09/19

## Unidad `ext::7.5.5.2` (item)
- herencia: [intro 7.5] La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de
ingreso y liquidación en las siguientes circunstancias: | **[abre la lista]** [intro 7.5.5] revisables o concentrados de minerales.
Cuando al vencimiento del plazo no haya sido posible, por causas ajenas a la voluntad
del exportador, determinar el precio definitivo de los bienes comprendidos en la opera-
ción, la entidad podrá extender el plazo hasta los 120 (ciento veinte) días corridos a
contar desde la fecha de cumplido de embarque que figura en el permiso de embarque
provisorio.
Para ello la entidad encargada del seguimiento deberá verificar el cumplimiento de las
siguientes condic
- texto propio: 7.5.5.2. el exportador ha entregado una declaración jurada en la que deja constancia
de los motivos ajenos a su voluntad por los cuales a la fecha no ha sido
posible determinar el precio definitivo de los bienes comprendidos en la
operación.
- entidades de la unidad:
  - `c1` Condicion: Entrega de declaración jurada sobre motivos — El exportador debe haber entregado una declaración jurada que constate los motivos ajenos a su voluntad que impidieron determinar el precio definitivo de los bienes en la operación.
  - `op1` Operacion: Entrega de declaración jurada por exportador — Entrega de una declaración jurada por parte del exportador.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 180** Condicion `c1`: Entrega de declaración jurada sobre motivos | descripcion: El exportador debe haber entregado una declaración jurada que constate los motivos ajenos a su voluntad que impidieron determinar el precio definitivo de los bienes en la operación. | tramo: el exportador ha entregado una declaración jurada en la que deja constancia de los motivos ajenos a su voluntad por los cuales a la fecha no ha sido posible determinar el precio definitivo de los bienes comprendidos en la operación

## Unidad `cap::2.4` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca
- texto propio: 2.4. Requisitos de debida diligencia.
Las entidades financieras del grupo 1 deberán llevar a cabo un proceso de debida diligencia –al
momento del otorgamiento del crédito y con frecuencia mínima anual– a fin de que puedan con-
tar con una adecuada comprensión del perfil de riesgo y las características de sus contrapartes.
El grado de sofisticación de las evaluaciones de debida diligencia deberá ser proporcional a la
dimensión e importancia económica de las entidades financieras y a la naturaleza y complejidad
de sus operaciones. Como resultado de esa evaluación, las entidades financieras deberán de-
mostrar a la SEFYC que los ponderadores de riesgo asignados son adecuados a los perfiles de
riesgo de sus contrapartes.
A tales efectos, las entidades financieras del grupo 1 deberán:
i) adoptar medidas adecuadas y razonables con el fin de evaluar el desempeño financiero y
operativo de cada contraparte a través del análisis crediticio;
ii) contar con acceso a información sobre sus contrapartes de manera regular para completar
su análisis;
iii) llevar a cabo los análisis de las exposiciones a contrapartes que pertenezcan a grupos
consolidados –siempre que sea posible– a nivel individual. Al momento de evaluar la capa-
cidad de pago de la contraparte individual, las entidades financieras deberán tener en
cuenta el respaldo del grupo económico, así como la posibilidad de que la contraparte se
vea perjudicada por los problemas generados en el grupo económico;
iv) contar con políticas, procesos, sistemas y controles internos eficaces; y
v) poder demostrar a la SEFYC que sus análisis de debida diligencia son adecuados y consis-
tentes con otros modelos y evaluaciones que deban ser llevados a cabo por las entidades
–tales como los procesos de estimación de previsiones por riesgo de
- entidades de la unidad:
  - `e1` Obligacion: Debida diligencia — evaluación anual de contrapartes — Las entidades financieras del grupo 1 deben llevar a cabo un proceso de debida diligencia al momento del otorgamiento del crédito y con frecuencia mínima anual para contar con una adecuada comprensión
  - `e2` Obligacion: Proporcionalidad sofisticación evaluaciones debida diligencia — El grado de sofisticación de las evaluaciones de debida diligencia debe ser proporcional a la dimensión e importancia económica de las entidades financieras y a la naturaleza y complejidad de sus oper
  - `e3` Obligacion: Demostración adecuación ponderadores riesgo a SEFYC — Las entidades financieras deben demostrar a la SEFYC que los ponderadores de riesgo asignados son adecuados a los perfiles de riesgo de sus contrapartes.
  - `e4` Obligacion: Medidas evaluación desempeño financiero operativo contraparte — Las entidades financieras del grupo 1 deben adoptar medidas adecuadas y razonables con el fin de evaluar el desempeño financiero y operativo de cada contraparte a través del análisis crediticio.
  - `e5` Obligacion: Acceso información regular contrapartes — Las entidades financieras del grupo 1 deben contar con acceso a información sobre sus contrapartes de manera regular para completar su análisis.
  - `e6` Obligacion: Análisis exposiciones contrapartes grupos consolidados nivel individual — Las entidades financieras del grupo 1 deben llevar a cabo los análisis de las exposiciones a contrapartes que pertenezcan a grupos consolidados a nivel individual, siempre que sea posible.
  - `e7` Condicion: Evaluación capacidad pago contraparte individual con respaldo grupo — Al momento de evaluar la capacidad de pago de la contraparte individual, las entidades financieras deben tener en cuenta el respaldo del grupo económico y la posibilidad de que la contraparte se vea p
  - `e8` Obligacion: Políticas procesos sistemas controles internos eficaces — Las entidades financieras del grupo 1 deben contar con políticas, procesos, sistemas y controles internos eficaces.
  - `e9` Obligacion: Demostración adecuación consistencia análisis debida diligencia a SEFYC — Las entidades financieras del grupo 1 deben demostrar a la SEFYC que sus análisis de debida diligencia son adecuados y consistentes con otros modelos y evaluaciones que deban ser llevados a cabo por l
  - `e10` Excepcion: Excepción exposiciones gobiernos bancos centrales punto 2.12.2 — El requerimiento de debida diligencia no aplica a exposiciones a gobiernos y bancos centrales previstas en el punto 2.12.2.
- relaciones del crudo (sin establecida_en ni de sujeto): e10 exceptua_obligacion e1
- NODOS A CLASIFICAR:
  - **caso 181** Condicion `e7`: Evaluación capacidad pago contraparte individual con respaldo grupo | descripcion: Al momento de evaluar la capacidad de pago de la contraparte individual, las entidades financieras deben tener en cuenta el respaldo del grupo económico y la posibilidad de que la contraparte se vea perjudicada por problemas del grupo económico. | tramo: Al momento de evaluar la capacidad de pago de la contraparte individual, las entidades financieras deberán tener en cuenta el respaldo del grupo económico, así como la posibilidad de que la contraparte se vea perjudicada por los problemas generados en el grupo económico

## Unidad `ext::3.18.2.2` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | **[abre la lista]** [intro 3.18.2] exportador deberá nominar una única entidad financiera local que será la
responsable de emitir las correspondientes certificaciones y remitirlas a las entidades
por las cuales el cliente desee acceder al mercado.
La entidad nominada podrá emitir una “Certificación de aumento de las exportaciones
de bienes en el año t” cuando se verifiquen la totalidad de los siguientes requisitos:
- texto propio: 3.18.2.2. El exportador no registra a la fecha de emisión permisos con plazo vencido
para el ingreso y liquidación de las divisas en situación de incumplimiento.
Los permisos que revistan la condición de “incumplido en gestión de cobro”
no serán considerados a estos efectos.
- entidades de la unidad:
  - `e1` Condicion: Exportador sin permisos vencidos a emisión — El exportador no registra a la fecha de emisión permisos con plazo vencido para el ingreso y liquidación de las divisas en situación de incumplimiento
  - `e2` Excepcion: Excepción permisos incumplidos en gestión de cobro — Los permisos que revistan la condición de 'incumplido en gestión de cobro' no serán considerados para la verificación del requisito de ausencia de permisos con plazo vencido
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 182** Condicion `e1`: Exportador sin permisos vencidos a emisión | descripcion: El exportador no registra a la fecha de emisión permisos con plazo vencido para el ingreso y liquidación de las divisas en situación de incumplimiento | tramo: El exportador no registra a la fecha de emisión permisos con plazo vencido para el ingreso y liquidación de las divisas en situación de incumplimiento

## Unidad `cap::2.5.5` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca | [encabezado 2.5] 2.5. Criterios para la determinación de los activos ponderados por riesgo.
- texto propio: 2.5.5. El término “exposición” abarca a todas las financiaciones otorgadas por la entidad –en
sus distintas modalidades, tales como préstamos, tenencias de títulos valores, fianzas,
avales y demás responsabilidades eventuales–, incluidas las que provengan de opera-
ciones realizadas en los mercados de títulos valores, de monedas y de derivados.
En el caso de exposiciones a entidades financieras, exposiciones a empresas, exposi-
ciones minoristas, exposiciones con garantía hipotecaria, exposiciones en situación de
incumplimiento y exposiciones a instrumentos, deberá tenerse en cuenta las disposicio-
nes específicas de los puntos 2.6., 2.7., 2.8., 2.9., 2.10. y 2.11., respectivamente.
A fin de determinar el importe de las financiaciones comprendidas en la exposición al
sector público no financiero, respecto de los títulos públicos nacionales que cuenten con
cotización normal y habitual por importes significativos en mercados del país que se
apliquen a operaciones de pase pasivo en pesos y que estén fondeados con depósitos
de esos títulos públicos, se observará el criterio de posición neta de títulos previsto en el
TO sobre Financiamiento al Sector Público no Financiero.
Las exposiciones incluirán los saldos de deuda y los compromisos eventuales multipli-
cados por el correspondiente factor de conversión crediticia (CCF).
- entidades de la unidad:
  - `e1` Definicion: Exposición — financiaciones otorgadas — Todas las financiaciones otorgadas por la entidad en sus distintas modalidades (préstamos, tenencias de títulos valores, fianzas, avales y demás responsabilidades eventuales), incluidas las que proven
  - `e2` Condicion: Exposiciones a entidades financieras — aplicación de disposiciones específicas — Cuando se trate de exposiciones a entidades financieras, deben aplicarse las disposiciones específicas del punto 2.6.
  - `e3` Condicion: Exposiciones a empresas — aplicación de disposiciones específicas — Cuando se trate de exposiciones a empresas, deben aplicarse las disposiciones específicas del punto 2.7.
  - `e4` Condicion: Exposiciones minoristas — aplicación de disposiciones específicas — Cuando se trate de exposiciones minoristas, deben aplicarse las disposiciones específicas del punto 2.8.
  - `e5` Condicion: Exposiciones con garantía hipotecaria — aplicación de disposiciones específicas — Cuando se trate de exposiciones con garantía hipotecaria, deben aplicarse las disposiciones específicas del punto 2.9.
  - `e6` Condicion: Exposiciones en situación de incumplimiento — aplicación de disposiciones específicas — Cuando se trate de exposiciones en situación de incumplimiento, deben aplicarse las disposiciones específicas del punto 2.10.
  - `e7` Condicion: Exposiciones a instrumentos — aplicación de disposiciones específicas — Cuando se trate de exposiciones a instrumentos, deben aplicarse las disposiciones específicas del punto 2.11.
  - `e8` Obligacion: Observar criterio de posición neta — títulos públicos nacionales — Observar el criterio de posición neta de títulos previsto en el TO sobre Financiamiento al Sector Público no Financiero para determinar el importe de las financiaciones comprendidas en la exposición a
  - `e9` Obligacion: Incluir saldos de deuda y compromisos eventuales — factor de conversión crediticia — Las exposiciones incluirán los saldos de deuda y los compromisos eventuales multiplicados por el correspondiente factor de conversión crediticia (CCF).
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 183** Condicion `e3`: Exposiciones a empresas — aplicación de disposiciones específicas | descripcion: Cuando se trate de exposiciones a empresas, deben aplicarse las disposiciones específicas del punto 2.7. | tramo: En el caso de exposiciones a empresas
  - **caso 184** Condicion `e2`: Exposiciones a entidades financieras — aplicación de disposiciones específicas | descripcion: Cuando se trate de exposiciones a entidades financieras, deben aplicarse las disposiciones específicas del punto 2.6. | tramo: En el caso de exposiciones a entidades financieras
  - **caso 185** Condicion `e7`: Exposiciones a instrumentos — aplicación de disposiciones específicas | descripcion: Cuando se trate de exposiciones a instrumentos, deben aplicarse las disposiciones específicas del punto 2.11. | tramo: En el caso de exposiciones a instrumentos
  - **caso 186** Condicion `e5`: Exposiciones con garantía hipotecaria — aplicación de disposiciones específicas | descripcion: Cuando se trate de exposiciones con garantía hipotecaria, deben aplicarse las disposiciones específicas del punto 2.9. | tramo: En el caso de exposiciones con garantía hipotecaria
  - **caso 187** Condicion `e6`: Exposiciones en situación de incumplimiento — aplicación de disposiciones específicas | descripcion: Cuando se trate de exposiciones en situación de incumplimiento, deben aplicarse las disposiciones específicas del punto 2.10. | tramo: En el caso de exposiciones en situación de incumplimiento
  - **caso 188** Condicion `e4`: Exposiciones minoristas — aplicación de disposiciones específicas | descripcion: Cuando se trate de exposiciones minoristas, deben aplicarse las disposiciones específicas del punto 2.8. | tramo: En el caso de exposiciones minoristas

## Unidad `cap::3.1.11.1` (punto_no_item)
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
- texto propio: 3.1.11.1. Conceptos.
La información necesaria para calcular las siguientes variables será provista
o estimada por cada entidad:
i) K : exigencia de capital que hubiera correspondido a las exposiciones
SA
subyacentes de no haber sido titulizadas.
ii) W: ratio de exposiciones subyacentes en situación de mora respecto del
total de exposiciones subyacentes.
iii) A: punto de unión del tramo (“tranche attachment point”). Representa el
umbral a partir del cual las pérdidas del conjunto de activos subyacente
comenzarán a asignarse a la posición de titulización mantenida por la
entidad. Es un porcentaje, entre cero y cien, que equivale al mayor entre
cero y el ratio entre (a) el saldo de todos los activos subyacentes menos el
saldo de todos los tramos con preferencia o de igual prelación (“pari
passu”) respecto del tramo al que está expuesta la entidad (incluido este
tramo) y (b) el saldo de todos los activos subyacentes de la titulización.
iv) D: punto de separación del tramo (“tranche detachment point”): constituye
el umbral a partir del cual las pérdidas del conjunto de activos subyacente
resultarán en una pérdida completa del principal del tramo o posición de la
entidad. Es un porcentaje, entre cero y cien, que equivale al mayor entre
cero y el ratio entre (a) el saldo de los activos subyacentes menos el saldo
de los tramos con preferencia respecto del tramo al que está expuesta la
entidad y (b) el saldo de todos los activos subyacentes de la titulización.
v) K : cargo de capital para las exposiciones subyacentes ajustado por mora.
A
vi) K : exigencia de capital por unidad de posición de titulización.
SSFA(KA)
Para el cálculo de las variables A y D, la sobrecolateralización y los fondos in-
tegrados en concepto de reserva (“reserve accounts”) deberán ser reconoci-
dos como t
- entidades de la unidad:
  - `e1` Definicion: K_SA: exigencia de capital exposiciones subyacentes — exigencia de capital que hubiera correspondido a las exposiciones subyacentes de no haber sido titulizadas
  - `e2` Definicion: W: ratio de exposiciones en mora — ratio de exposiciones subyacentes en situación de mora respecto del total de exposiciones subyacentes
  - `e3` Definicion: A: punto de unión del tramo (attachment point) — punto de unión del tramo (tranche attachment point); umbral a partir del cual las pérdidas del conjunto de activos subyacente comenzarán a asignarse a la posición de titulización mantenida por la enti
  - `e4` Definicion: D: punto de separación del tramo (detachment point) — punto de separación del tramo (tranche detachment point); umbral a partir del cual las pérdidas del conjunto de activos subyacente resultarán en una pérdida completa del principal del tramo o posición
  - `e5` Definicion: K_A: cargo de capital exposiciones subyacentes ajustado — cargo de capital para las exposiciones subyacentes ajustado por mora
  - `e6` Definicion: K_SSFA(KA): exigencia de capital por unidad posición — exigencia de capital por unidad de posición de titulización
  - `e7` Obligacion: Reconocimiento de sobrecolateralización y reservas en cálculo A y D — para el cálculo de las variables A y D, la sobrecolateralización y los fondos integrados en concepto de reserva deberán ser reconocidos como tramos y los activos que conforman estas reservas deberán s
  - `e8` Restriccion: Límite reconocimiento reservas — absorción pérdidas — solo la parte de las reservas que esté sujeta a la absorción de pérdidas y proporcione una mejora crediticia podrá ser reconocida como tramo y activo subyacente
  - `e9` Restriccion: Exclusión reservas ingresos futuros — cálculo A y D — las reservas a integrar con ingresos futuros provenientes de los activos subyacentes (tal como el margen financiero futuro no realizado) y los activos que no proporcionen mejoras crediticias (tales co
  - `e10` Obligacion: Consideración realidad económica en aplicación definiciones — las entidades deberán considerar la realidad o finalidad económica de la transacción y aplicar estas definiciones de manera prudente en función de las características de la estructura
  - `e11` Condicion: Identidad A y D cuando única diferencia es vencimiento — cuando la única diferencia entre dos posiciones es el vencimiento, A y D serán idénticos
  - `e12` Obligacion: Provisión o estimación de variables por entidades — la información necesaria para calcular las siguientes variables será provista o estimada por cada entidad
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 190** Condicion `e11`: Identidad A y D cuando única diferencia es vencimiento | descripcion: cuando la única diferencia entre dos posiciones es el vencimiento, A y D serán idénticos | tramo: Si la única diferencia entre dos posiciones fueran el vencimiento, A y D serán idénticos.

## Unidad `ext::7.11.2.3` (item)
- herencia: [intro 7.11] de exportaciones de bienes. | **[abre la lista]** [intro 7.11.2] que se verifiquen la totalidad de las siguientes condiciones: | [cierre 7.11.2] La entidad deberá verificar los requisitos habituales a los efectos de certificar la
aplicación de divisas a la cancelación de la financiación.
- texto propio: 7.11.2.3. El importador haya demostrado el registro de ingreso aduanero de los
bienes por un valor equivalente al monto total de la financiación que
pretende ser cancelada con este mecanismo. A los efectos del valor de los
bienes podrá tomarse en todo concepto que forme parte de la condición de
compra pactada registrada en la factura emitida por el proveedor del
exterior.
Si existiesen fondos destinados al pago de fletes de importaciones de
bienes no incluidos en la condición de compra y el importador demostró el
registro de ingreso aduanero de los bienes cuyos fletes se abonaron,
también se podrá computar el valor de los fletes que consten en la
documentación de transporte asociada al registro de ingreso aduanero de
los bienes.
En el caso de operaciones comprendidas en el punto 7.11.1.6. también se
admitirá la cancelación de intereses a partir de la fecha en que se complete
el ingreso de la financiación, sin necesidad de contar en ese momento con
el registro de ingreso aduanero de los bienes.
- entidades de la unidad:
  - `c1` Condicion: Importador demuestra registro ingreso aduanero — El importador debe haber demostrado el registro de ingreso aduanero de los bienes cuyo valor sea equivalente al monto total de la financiación que se pretende cancelar con este mecanismo.
  - `d1` Definicion: Valor de bienes para cálculo de equivalencia — Para determinar el valor de los bienes se puede considerar todo concepto que forme parte de la condición de compra pactada registrada en la factura emitida por el proveedor del exterior.
  - `e1` Excepcion: Excepción — fletes de importaciones no incluidos en condición de compra — Se admite computar el valor de los fletes no incluidos en la condición de compra cuando el importador ha demostrado el registro de ingreso aduanero de los bienes cuyos fletes se abonaron y constan en 
  - `e2` Excepcion: Excepción — cancelación de intereses sin registro aduanero previo — Para operaciones comprendidas en el punto 7.11.1.6, se admite la cancelación de intereses desde la fecha en que se complete el ingreso de la financiación, sin requerir en ese momento el registro de in
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 191** Condicion `c1`: Importador demuestra registro ingreso aduanero | descripcion: El importador debe haber demostrado el registro de ingreso aduanero de los bienes cuyo valor sea equivalente al monto total de la financiación que se pretende cancelar con este mecanismo. | tramo: El importador haya demostrado el registro de ingreso aduanero de los bienes por un valor equivalente al monto total de la financiación que pretende ser cancelada con este mecanismo

## Unidad `polcre::7.1.2` (item)
- herencia: **[abre la lista]** [intro 7.1] Se encuentran comprendidos en la categoría de “Grandes empresas exportadoras” los clientes
del sector privado no financiero que reúnan concurrentemente las siguientes condiciones: | [cierre 7.1] Cuando el cliente reúna la condición del punto 7.1.1. pero el importe total de sus financiaciones
en pesos en el sistema financiero no supere el importe de $ 30.000 millones y no haya mante-
nido pases y/o cauciones bursátiles tomadas –en pesos– durante los últimos 90 días corridos,
la entidad financiera podrá otorgarle nuevas financiaciones en la medida que con tales desem-
bolsos no se supere ese importe.
Cuando se trate de conjuntos económicos se los considerará como un solo cliente, a cuyo
e
- texto propio: 7.1.2. Mantengan un importe total de financiaciones alcanzadas en pesos en el conjunto del
sistema financiero que supere el monto de $ 30.000 millones, y/o pases y/o cauciones
bursátiles tomadas –en pesos– cualquiera sea su importe durante los últimos 90 días
corridos.
Las financiaciones alcanzadas serán aquellas que hayan implicado desembolsos de
fondos, así como el importe no utilizado del límite de crédito asignado para adelantos en
cuenta corriente. Se computará su saldo de capital a fin del mes anterior al que corres-
ponda su determinación.
Cuando un cliente manifieste por declaración jurada que no se encuadra en la categoría
de “Gran empresa exportadora” y, de la información disponible en la “Central de deudo-
res del sistema financiero”, surja que supera el importe de $ 30.000 millones, deberá
presentar una certificación extendida por Auditor Externo o Contador Público indepen-
diente (con firma debidamente certificada por el respectivo Consejo Profesional de
Ciencias Económicas) en la que se detallen las financiaciones en pesos y moneda ex-
tranjera en el conjunto de las entidades financieras, desagregando los datos correspon-
dientes a cada uno de esos intermediarios a la fecha a la cual se refiera, y los citados
pases y cauciones bursátiles tomados –en pesos– durante los últimos 90 días corridos.
Lo previsto en este párrafo no será de aplicación cuando el cliente reúna la condición de
MiPyME –de acuerdo con las normas sobre “Determinación de la condición de micro,
pequeña y mediana empresa”–.
Esa certificación mantendrá vigencia durante 90 días corridos desde la fecha a la cual
se refiera, sin perjuicio de la presentación de una nueva certificación en caso de corres-
ponder.
- entidades de la unidad:
  - `c1` Condicion: Importe total financiaciones pesos supera $ 30.000 millones — El cliente mantiene un importe total de financiaciones alcanzadas en pesos en el conjunto del sistema financiero que supera el monto de $ 30.000 millones
  - `c2` Condicion: Pases y/o cauciones bursátiles tomadas en pesos últimos 90 días — El cliente ha mantenido pases y/o cauciones bursátiles tomadas en pesos durante los últimos 90 días corridos, cualquiera sea su importe
  - `d1` Definicion: Financiaciones alcanzadas — Aquellas que hayan implicado desembolsos de fondos, así como el importe no utilizado del límite de crédito asignado para adelantos en cuenta corriente
  - `o1` Obligacion: Presentar certificación de Auditor Externo o Contador Público — El cliente debe presentar una certificación extendida por Auditor Externo o Contador Público independiente (con firma debidamente certificada por el respectivo Consejo Profesional de Ciencias Económic
  - `c3` Condicion: Cliente manifiesta por declaración jurada no encuadrarse en categoría — El cliente manifiesta por declaración jurada que no se encuadra en la categoría de Gran empresa exportadora y de la información disponible en la Central de deudores del sistema financiero surge que su
  - `e1` Excepcion: Excepción para clientes MiPyME — La obligación de presentar certificación no aplica cuando el cliente reúna la condición de MiPyME de acuerdo con las normas sobre Determinación de la condición de micro, pequeña y mediana empresa
  - `c4` Condicion: Vigencia de certificación 90 días corridos — La certificación mantiene vigencia durante 90 días corridos desde la fecha a la cual se refiera
- relaciones del crudo (sin establecida_en ni de sujeto): c3 condicion_de o1; e1 exceptua_obligacion o1
- NODOS A CLASIFICAR:
  - **caso 192** Condicion `c1`: Importe total financiaciones pesos supera $ 30.000 millones | descripcion: El cliente mantiene un importe total de financiaciones alcanzadas en pesos en el conjunto del sistema financiero que supera el monto de $ 30.000 millones | tramo: un importe total de financiaciones alcanzadas en pesos en el conjunto del sistema financiero que supere el monto de $ 30.000 millones
  - **caso 221** Condicion `c2`: Pases y/o cauciones bursátiles tomadas en pesos últimos 90 días | descripcion: El cliente ha mantenido pases y/o cauciones bursátiles tomadas en pesos durante los últimos 90 días corridos, cualquiera sea su importe | tramo: pases y/o cauciones bursátiles tomadas –en pesos– cualquiera sea su importe durante los últimos 90 días corridos
  - **caso 255** Condicion `c4`: Vigencia de certificación 90 días corridos | descripcion: La certificación mantiene vigencia durante 90 días corridos desde la fecha a la cual se refiera | tramo: Esa certificación mantendrá vigencia durante 90 días corridos desde la fecha a la cual se refiera

## Unidad `cap::6.2.2.4` (punto_no_item)
- herencia: [intro 6.2] La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu-
los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio-
nes preferidas no convertibles.
Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo
de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de
la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera.
L | [encabezado 6.2.2] 6.2.2. Exigencia de capital por riesgo general de mercado: método de los plazos residuales.
- texto propio: 6.2.2.4. Las posiciones imputadas a cada banda temporal deberán ponderarse por un
factor que refleje su sensibilidad a los cambios en las tasas de interés, confor-
me al siguiente cuadro:
[TABLA cap::tabla036 | página 124 | e0_tablas | posicional]
Fila 1: col1 = Zona | col2 = Cupón menor a 3 % | col3 = Cupón igual o mayor a 3 % | col4 = Ponderador de riesgo | col5 = Cambio supuesto en el rendimiento –a utilizar en el método delta-plus (punto 6.6.3.)–
Fila 2: col2 = Meses* ⟨abarca hasta col3⟩
Fila 3: col1 = 1 | col2 = 0-1 | col3 = 0-1 | col4 = 0,00 % | col5 = 1,00
Fila 4: col1 = 1 ⟨combinada con fila 3⟩ | col2 = 1-3 | col3 = 1-3 | col4 = 0,20 % | col5 = 1,00
Fila 5: col1 = 1 ⟨combinada con fila 3⟩ | col2 = 3-6 | col3 = 3-6 | col4 = 0,40 % | col5 = 1,00
Fila 6: col1 = 1 ⟨combinada con fila 3⟩ | col2 = 6-12 | col3 = 6-12 | col4 = 0,70 % | col5 = 1,00
Fila 7: col2 = Años* ⟨abarca hasta col3⟩
Fila 8: col1 = 2 | col2 = 1-1,9 | col3 = 1-2 | col4 = 1,25 % | col5 = 0,90
Fila 9: col1 = 2 ⟨combinada con fila 8⟩ | col2 = 1,9-2,8 | col3 = 2-3 | col4 = 1,75 % | col5 = 0,80
Fila 10: col1 = 2 ⟨combinada con fila 8⟩ | col2 = 2,8-3,6 | col3 = 3-4 | col4 = 2,25 % | col5 = 0,75
Fila 11: col2 = Años* ⟨abarca hasta col3⟩
Fila 12: col1 = 3 | col2 = 3,6-4,3 | col3 = 4-5 | col4 = 2,75 % | col5 = 0,75
Fila 13: col1 = 3 ⟨combinada con fila 12⟩ | col2 = 4,3-5,7 | col3 = 5-7 | col4 = 3,25 % | col5 = 0,70
Fila 14: col1 = 3 ⟨combinada con fila 12⟩ | col2 = 5,7-7,3 | col3 = 7-10 | col4 = 3,75 % | col5 = 0,65
Fila 15: col1 = 3 ⟨combinada con fila 12⟩ | col2 = 7,3-9,3 | col3 = 10-15 | col4 = 4,50 % | col5 = 0,60
Fila 16: col1 = 3 ⟨combinada con fila 12⟩ | col2 = 9,3-10,6 | col3 = 15-20 | col4 = 5,25 % | col5 = 0,60
Fila 17: col1 = 3 ⟨combinada con fila 12⟩ | col2 = 10,6-12 | col3 = Más de 20 | col4 = 6,
- entidades de la unidad:
  - `e1` Operacion: Ponderación de posiciones por sensibilidad a tasas — Aplicación de factores de ponderación a las posiciones según su sensibilidad a cambios en tasas de interés, conforme a la tabla de bandas temporales y cupones
  - `e2` Obligacion: Ponderar posiciones por factor de sensibilidad — Las entidades deberán ponderar las posiciones imputadas a cada banda temporal por un factor que refleje su sensibilidad a los cambios en las tasas de interés, según los ponderadores de riesgo establec
  - `e3` Condicion: Imputación a banda temporal según plazo residual — Cuando el plazo residual o el plazo hasta el siguiente ajuste del interés coincide con el límite entre dos bandas temporales, la posición se imputa a la banda temporal más próxima a la fecha de cálcul
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condiciona e1
- NODOS A CLASIFICAR:
  - **caso 193** Condicion `e3`: Imputación a banda temporal según plazo residual | descripcion: Cuando el plazo residual o el plazo hasta el siguiente ajuste del interés coincide con el límite entre dos bandas temporales, la posición se imputa a la banda temporal más próxima a la fecha de cálculo | tramo: Al efecto de imputar una posición a la escala de vencimientos cuando el plazo residual o el plazo que resta hasta el siguiente ajuste del interés, según el caso, es igual al límite entre dos bandas, corresponderá realizar la imputación a la banda temporal más próxima a la fecha de cálculo

## Unidad `ext::3.5.1::intro` (intro)
- herencia: [encabezado 3.5.1] 3.5.1. El deudor demuestre el ingreso y liquidación de divisas en el mercado de cambios por
- texto propio: un monto equivalente al valor nominal del endeudamiento financiero.
Este requisito se considerará cumplimentado en los siguientes casos:
- entidades de la unidad:
  - `e1` Condicion: Ingreso y liquidación de divisas en mercado de cambios — El deudor debe demostrar el ingreso y liquidación de divisas en el mercado de cambios por un monto equivalente al valor nominal del endeudamiento financiero
  - `e2` Obligacion: Cumplimiento de requisito de ingreso y liquidación de divisas — El requisito de ingreso y liquidación de divisas en el mercado de cambios se considerará cumplimentado en los siguientes casos
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 197** Condicion `e1`: Ingreso y liquidación de divisas en mercado de cambios | descripcion: El deudor debe demostrar el ingreso y liquidación de divisas en el mercado de cambios por un monto equivalente al valor nominal del endeudamiento financiero | tramo: El deudor demuestre el ingreso y liquidación de divisas en el mercado de cambios por un monto equivalente al valor nominal del endeudamiento financiero

## Unidad `ext::4.8.4.3` (item)
- herencia: [intro 4.8] Argentina Libre (BOPREAL). | **[abre la lista]** [intro 4.8.4] monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas
elegibles para los puntos 4.4. y 4.5., podrán acceder al mercado de cambios para
pagar capital de deudas elegibles por las cuales no se suscribió un título BOPREAL,
cuando se verifique alguna de las siguientes condiciones: | [cierre 4.8.4] Adicionalmente a los restantes requisitos normativos aplicables, la entidad deberá
contar con una declaración jurada del cliente en la que conste el monto suscripto del
BOPREAL Serie 1, los montos de las deudas comerciales de bienes y servicios por
operaciones anteriores al 13/12/23 elegibles y que el pago queda encuadrado en los
límites previstos.
- texto propio: 4.8.4.3. en forma simultánea concrete la liquidación por un monto equivalente al
pagado de cobros anticipados de exportaciones de bienes que serán
cancelados con embarques cuyos cobros hubiera correspondido ingresar a
partir del 01/03/25 a razón de un máximo mensual equivalente al 10% (diez
por ciento) del monto total de los anticipos que se encuadraron en este
mecanismo.
La entidad deberá contar con una declaración jurada del importador en la
cual deja constancia de que será necesaria la conformidad previa del BCRA
para la cancelación de estos cobros anticipados de exportaciones de bienes
antes de los plazos estipulados.
- entidades de la unidad:
  - `e1` Condicion: Liquidación simultánea de cobros anticipados — Condición de que la liquidación se concrete en forma simultánea por un monto equivalente al pagado de cobros anticipados de exportaciones de bienes que serán cancelados con embarques cuyos cobros hubi
  - `e2` Restriccion: Tope 10% mensual — cobros anticipados de exportaciones — El monto de liquidación de cobros anticipados de exportaciones no podrá exceder un máximo mensual equivalente al 10% (diez por ciento) del monto total de los anticipos que se encuadraron en este mecan
  - `e3` Obligacion: Declaración jurada del importador — conformidad previa BCRA — La entidad deberá contar con una declaración jurada del importador en la cual conste que será necesaria la conformidad previa del BCRA para la cancelación de cobros anticipados de exportaciones de bie
  - `e4` Potestad: Conformidad previa BCRA — cancelación de cobros anticipados — El BCRA tiene la potestad de otorgar o denegar la conformidad previa para la cancelación de cobros anticipados de exportaciones de bienes antes de los plazos estipulados
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 198** Condicion `e1`: Liquidación simultánea de cobros anticipados | descripcion: Condición de que la liquidación se concrete en forma simultánea por un monto equivalente al pagado de cobros anticipados de exportaciones de bienes que serán cancelados con embarques cuyos cobros hubiera correspondido ingresar a partir del 01/03/25 | tramo: en forma simultánea concrete la liquidación por un monto equivalente al pagado de cobros anticipados de exportaciones de bienes que serán cancelados con embarques cuyos cobros hubiera correspondido ingresar a partir del 01/03/25

## Unidad `cla::6.5.3.6` (item)
- herencia: [intro 6.5] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudor | **[abre la lista]** [intro 6.5.3] El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender
normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos,
esos problemas pueden resultar en una pérdida para la entidad financiera.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- texto propio: 6.5.3.6. Mantenga convenios de pago resultantes de concordatos judiciales o extrajudi-
ciales homologados (incluyendo los acuerdos preventivos extrajudiciales homo-
logados) a vencer o arreglos privados concertados en forma conjunta con enti-
dades financieras acreedoras cuando aún no se haya cancelado el 10 % del im-
porte involucrado en el citado acuerdo.
A fin de determinar el importe de la cancelación, se admitirá computar el 50 %
de las garantías adicionales a las ofrecidas originalmente, constituidas sobre
bienes no vinculados a la explotación del deudor –con excepción de las hipote-
cas sobre inmuebles rurales que, por lo tanto, serán computables–, observando
los márgenes de cobertura establecidos en las normas sobre “Garantías”.
- entidades de la unidad:
  - `e1` Condicion: Mantenimiento de convenios de concordatos o arreglos privados — El cliente mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo acuerdos preventivos extrajudiciales homologados) a vencer o arreglos privados con
  - `e2` Obligacion: Computar 50 % de garantías adicionales para determinar cancelación — A fin de determinar el importe de la cancelación, se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del 
  - `e3` Excepcion: Excepción hipotecas sobre inmuebles rurales — garantías adicionales — Las hipotecas sobre inmuebles rurales constituidas como garantías adicionales serán computables, a diferencia de otras garantías sobre bienes no vinculados a la explotación del deudor
- relaciones del crudo (sin establecida_en ni de sujeto): e3 exceptua_obligacion e2
- NODOS A CLASIFICAR:
  - **caso 199** Condicion `e1`: Mantenimiento de convenios de concordatos o arreglos privados | descripcion: El cliente mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo acuerdos preventivos extrajudiciales homologados) a vencer o arreglos privados concertados con entidades financieras acreedoras, siempre que aún no se haya cancelado el 10 % del importe involucrado en el acuerdo | tramo: Mantenga convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer o arreglos privados concertados en forma conjunta con entidades financieras acreedoras cuando aún no se haya cancelado el 10 % del importe involucrado en el citado acuerdo

## Unidad `cap::5.4.5` (item)
- herencia: [chapeau_seccion S5] A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o
parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera
de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las
técnicas previstas en el punto 5.1.
La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia-
ción con títulos valores (securities financing transactions, SFT) –co | **[abre la lista]** [intro 5.4] Se aplicará el método de sustitución de ponderadores. Con este método, el ponderador de
riesgo de la contraparte se sustituye por el ponderador de riesgo del garante –o contragarante–
o proveedor de protección crediticia –conforme a la tabla de ponderadores prevista en la Sec-
ción 2.–.
Se reconocerán sólo las garantías emitidas –o protección provista, en el caso de derivados de
crédito– por entidades listadas en el punto 5.4.1.
La parte de la exposición sin cobertura mantendrá el ponderador de 
- texto propio: 5.4.5. Descalce de plazos de vencimiento.
El descalce de plazos tiene lugar cuando el plazo de vencimiento residual de la CRC es
inferior al de la exposición subyacente; ambos plazos de vencimiento deberán medirse
en forma conservadora.
El plazo de vencimiento de la exposición subyacente se calculará como el mayor plazo
de vencimiento restante posible antes de que la contraparte deba cumplir su obligación,
teniendo en cuenta cualquier período de gracia aplicable. Con relación a la CRC, se de-
berá tener en cuenta las opciones incorporadas que puedan reducir el plazo de venci-
miento, a fin de utilizar el menor plazo de vencimiento posible. Cuando el proveedor de
protección pueda solicitar anticipadamente la liquidación de la operación, el plazo de
vencimiento será siempre el correspondiente a la primera fecha en la que pueda solicitar
su liquidación.
Si la solicitud de liquidación de la operación por anticipado está sujeta a la discrecionali-
dad de la entidad financiera compradora de la protección, pero los términos del acuerdo
contienen un incentivo positivo para que la entidad exija la liquidación de la operación
antes del plazo de vencimiento establecido en el contrato, se considerará que el plazo
de vencimiento es el tiempo restante hasta la primera fecha posible de liquidación.
De haber descalce de plazos de vencimiento, la CRC que tenga un plazo de vencimien-
to original inferior a un año o residual no mayor a tres meses no será reconocida. Cuan-
do en estos casos sea factible el cómputo de la CRC su reconocimiento será parcial,
aplicándose el siguiente ajuste:
P = P x (t – 0,25) / (T – 0,25)
a
donde:
P : valor de la CRC ajustado por descalce de plazos de vencimiento.
a
P: valor de la protección crediticia ajustada por cualquier aforo aplicable.
t: mín. (T; plazo
- entidades de la unidad:
  - `e1` Definicion: Descalce de plazos de vencimiento — Situación en la que el plazo de vencimiento residual de la cobertura del riesgo de crédito (CRC) es inferior al de la exposición subyacente.
  - `e2` Condicion: Medición conservadora de plazos de vencimiento — Los plazos de vencimiento de la CRC y de la exposición subyacente deben medirse en forma conservadora.
  - `e3` Operacion: Cálculo del plazo de vencimiento de la exposición subyacente — Cálculo del plazo de vencimiento de la exposición subyacente como el mayor plazo de vencimiento restante posible antes de que la contraparte deba cumplir su obligación, considerando períodos de gracia
  - `e4` Operacion: Cálculo del plazo de vencimiento de la CRC — Cálculo del plazo de vencimiento de la CRC considerando las opciones incorporadas que puedan reducir el plazo, utilizando el menor plazo de vencimiento posible.
  - `e5` Condicion: Plazo de vencimiento cuando hay liquidación anticipada — Cuando el proveedor de protección puede solicitar liquidación anticipada, el plazo de vencimiento es el de la primera fecha posible de liquidación.
  - `e6` Condicion: Plazo de vencimiento con incentivo positivo para liquidación anticipada — Cuando hay incentivo positivo en el acuerdo para liquidación anticipada, el plazo de vencimiento es el tiempo restante hasta la primera fecha posible de liquidación.
  - `e7` Restriccion: No reconocimiento de CRC con descalce de plazos — Cuando hay descalce de plazos de vencimiento, no se reconoce la CRC que tenga un plazo de vencimiento original inferior a un año o residual no mayor a tres meses.
  - `e8` Excepcion: Reconocimiento parcial de CRC con descalce de plazos — Cuando sea factible el cómputo de la CRC con descalce de plazos, se reconoce parcialmente aplicando un ajuste de descalce de plazos de vencimiento.
- relaciones del crudo (sin establecida_en ni de sujeto): e8 exceptua e7
- NODOS A CLASIFICAR:
  - **caso 200** Condicion `e2`: Medición conservadora de plazos de vencimiento | descripcion: Los plazos de vencimiento de la CRC y de la exposición subyacente deben medirse en forma conservadora. | tramo: ambos plazos de vencimiento deberán medirse en forma conservadora
  - **caso 226** Condicion `e6`: Plazo de vencimiento con incentivo positivo para liquidación anticipada | descripcion: Cuando hay incentivo positivo en el acuerdo para liquidación anticipada, el plazo de vencimiento es el tiempo restante hasta la primera fecha posible de liquidación. | tramo: Si la solicitud de liquidación de la operación por anticipado está sujeta a la discrecionalidad de la entidad financiera compradora de la protección, pero los términos del acuerdo contienen un incentivo positivo para que la entidad exija la liquidación de la operación antes del plazo de vencimiento establecido en el contrato, se considerará que el plazo de vencimiento es el tiempo restante hasta la primera fecha posible de liquidación
  - **caso 227** Condicion `e5`: Plazo de vencimiento cuando hay liquidación anticipada | descripcion: Cuando el proveedor de protección puede solicitar liquidación anticipada, el plazo de vencimiento es el de la primera fecha posible de liquidación. | tramo: Cuando el proveedor de protección pueda solicitar anticipadamente la liquidación de la operación, el plazo de vencimiento será siempre el correspondiente a la primera fecha en la que pueda solicitar su liquidación

## Unidad `ext::9.3.1.2` (item)
- herencia: [intro 9.3] A solicitud del exportador, la entidad encargada del seguimiento emitirá las certificaciones de
aplicación en la medida que se verifiquen las condiciones previstas en los puntos 9.3.1. al
9.3.13.
La entidad deberá dejar registradas las certificaciones de aplicación emitidas para cada una
de las operaciones bajo su seguimiento. | **[abre la lista]** [intro 9.3.1] partir del 02/09/19 y prefinanciaciones locales.
La entidad podrá emitir las certificaciones de aplicación de las divisas a la
cancelación del capital e intereses en la medida que se verifiquen las siguientes
condiciones: | [cierre 9.3.1] La entidad también podrá emitir certificaciones de aplicación con imputación a una
operación bajo su seguimiento, en la medida que el exportador demuestre
fehacientemente que las divisas del permiso se utilizaron para cancelar la deuda
original que fue cedida a otro acreedor externo por el acreedor originalmente
declarado, o una renovación de la operación original con el mismo acreedor.
- texto propio: 9.3.1.2. Que el monto a certificar por una aplicación a la cancelación del capital
sea menor o igual al saldo liquidado pendiente de aplicación que registra
la entidad para la operación en cuestión.
En caso de tratarse de una operación del exterior liquidada parcialmente
durante las respectivas vigencias de los Decretos 492/23, 549/23, 597/23
y 28/23, también se podrá emitir certificaciones por la porción no liquidada
en la medida que se verifique lo previsto en el punto 7.3.11.
- entidades de la unidad:
  - `e1` Condicion: Monto a certificar menor o igual al saldo liquidado — El monto a certificar por una aplicación a la cancelación del capital debe ser menor o igual al saldo liquidado pendiente de aplicación que registra la entidad para la operación en cuestión.
  - `e2` Excepcion: Excepción operaciones del exterior liquidadas parcialmente — Se permite emitir certificaciones por la porción no liquidada de operaciones del exterior liquidadas parcialmente durante las vigencias de los Decretos 492/23, 549/23, 597/23 y 28/23, siempre que se v
  - `e3` Condicion: Verificación de lo previsto en punto 7.3.11 — Condición de que se verifique lo previsto en el punto 7.3.11 para la emisión de certificaciones por la porción no liquidada.
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 201** Condicion `e1`: Monto a certificar menor o igual al saldo liquidado | descripcion: El monto a certificar por una aplicación a la cancelación del capital debe ser menor o igual al saldo liquidado pendiente de aplicación que registra la entidad para la operación en cuestión. | tramo: Que el monto a certificar por una aplicación a la cancelación del capital sea menor o igual al saldo liquidado pendiente de aplicación que registra la entidad para la operación en cuestión

## Unidad `ext::3.4.2` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | **[abre la lista]** [intro 3.4] Las entidades podrán dar acceso al mercado de cambios para girar divisas al exterior en
concepto de utilidades y dividendos a accionistas no residentes, en la medida que se cumpla
la totalidad de las siguientes condiciones: | [cierre 3.4] Los casos que no encuadren en lo expuesto precedentemente requerirán la conformidad
previa del BCRA para acceder al mercado de cambios.
Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre
(BOPREAL) por hasta el equivalente al monto en moneda local de las utilidades y dividendos
pendientes de pago a accionistas no residentes según la distribución determinada por la
asamblea de accionistas, en la medida que se encuentren sujetos a conformidad previa del
BCRA y se cump
- texto propio: 3.4.2. El monto total abonado por este concepto a accionistas no residentes, incluido el pago
cuyo curso se está solicitando, no supere el monto en moneda local que les
corresponda según la distribución determinada por la asamblea de accionistas.
La entidad deberá contar con una declaración jurada firmada por el representante legal
de la empresa residente o un apoderado con facultades suficientes para asumir este
compromiso en nombre de la empresa.
- entidades de la unidad:
  - `e1` Condicion: Monto total no supere distribución accionistas — El monto total abonado a accionistas no residentes, incluido el pago cuyo curso se solicita, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamb
  - `e2` Obligacion: Declaración jurada representante legal — pago utilidades — La entidad debe contar con una declaración jurada firmada por el representante legal de la empresa residente o un apoderado con facultades suficientes para asumir el compromiso en nombre de la empresa
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 202** Condicion `e1`: Monto total no supere distribución accionistas | descripcion: El monto total abonado a accionistas no residentes, incluido el pago cuyo curso se solicita, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas | tramo: El monto total abonado por este concepto a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no supere el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas

## Unidad `ext::9.3.12.2` (item)
- herencia: [intro 9.3] A solicitud del exportador, la entidad encargada del seguimiento emitirá las certificaciones de
aplicación en la medida que se verifiquen las condiciones previstas en los puntos 9.3.1. al
9.3.13.
La entidad deberá dejar registradas las certificaciones de aplicación emitidas para cada una
de las operaciones bajo su seguimiento. | **[abre la lista]** [intro 9.3.12] La entidad podrá emitir las certificaciones de aplicación de las divisas al pago de
utilidades y dividendos a accionistas no residentes, en la medida que se cumplan la
totalidad de las siguientes condiciones:
- texto propio: 9.3.12.2. El monto total abonado por este concepto a accionistas no residentes,
incluido el pago cuya aplicación se está solicitando, no supere el monto en
moneda local que les corresponda según la distribución determinada por la
asamblea de accionistas.
La entidad deberá contar con una declaración jurada firmada por el
representante legal de la empresa residente o un apoderado con facultades
suficientes para asumir este compromiso en nombre de la empresa.
- entidades de la unidad:
  - `c1` Condicion: Monto total no supere distribución asamblea — El monto total abonado a accionistas no residentes, incluido el pago cuya aplicación se solicita, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la 
  - `o1` Obligacion: Declaración jurada de representante legal — pago utilidades — La entidad debe contar con una declaración jurada firmada por el representante legal de la empresa residente o un apoderado con facultades suficientes para asumir el compromiso en nombre de la empresa
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 203** Condicion `c1`: Monto total no supere distribución asamblea | descripcion: El monto total abonado a accionistas no residentes, incluido el pago cuya aplicación se solicita, no debe superar el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas | tramo: El monto total abonado por este concepto a accionistas no residentes, incluido el pago cuya aplicación se está solicitando, no supere el monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas

## Unidad `cap::4.2.1.2::parte2` (punto_no_item)
- herencia: [intro 4.2] –OTC o negociados en mercados regulados– y con liquidación diferida.
La exigencia computada en este punto –basada en el Enfoque Estándar para la medición de
la exigencia por capital por riesgo de crédito de contraparte (“Standardised Approach for
measuring Counterparty Credit Risk”, SA-CCR)– se aplicará a operaciones con derivados
–OTC o negociados en mercados regulados– y con liquidación diferida, ya que las operacio-
nes de financiación con títulos valores (“Securities Financing Transactions”, | [intro 4.2.1] La exposición al riesgo de crédito de contraparte (EAD) se calculará por separado para
cada conjunto de neteo (“netting set”, NS) y se determinará del siguiente modo:
donde:
α = 1,40.
CR: costo de reposición calculado de acuerdo con el punto 4.2.1.1.
EPF: exposición potencial futura calculado de acuerdo con el punto 4.2.1.2.
El cálculo del CR y de la EPF diferirá según que los conjuntos de neteo estén sujetos o
no al intercambio de márgenes de variación:
− Operaciones sin margen de variación: el | [intro 4.2.1] ante el incumplimiento de la contraparte y la liquidación inmediata de sus opera-
ciones y la EPF adicionará el incremento probable de la exposición, calculado de
modo conservador, en el horizonte temporal de un año a partir de la fecha de
cálculo. | [intro 4.2.1] − Operaciones con margen de variación: el CR representa la pérdida que ocurriría | [intro 4.2.1] ante el incumplimiento de la contraparte –en el presente o en el futuro– si la liqui-
dación y reposición de las operaciones fueran instantáneas. Dado que puede ha-
ber un lapso –período de riesgo de margen (“MPOR”)– entre el último intercambio
de garantías antes del incumplimiento y la reposición, el adicional por la EPF re-
presenta el potencial cambio de valor de las operaciones durante ese período. | [intro 4.2.1] En ambos casos, y a los efectos de determinar el costo de reposición, el aforo de los
activos recibidos en garantía (excepto efectivo) representará el cambio potencial del
valor de dicha garantía durante el período relevante –un año, para las operaciones sin
márgenes, y el período de riesgo de margen, para las operaciones con márgenes–.
Además:
− La EAD para un conjunto de neteo con márgenes de variación tendrá como límite | [intro 4.2.1] superior la EAD que resultaría para el mismo conjunto si no los tuviera. | [intro 4.2.1] − La EAD de un conjunto de neteo que sólo comprende opciones vendidas podrá | [intro 4.2.1] ser cero cuando hayan sido cobradas todas las primas y en tanto dichas opciones
no estén comprendidas en acuerdos de neteo que incluyan otros productos o la
constitución de márgenes.
- texto propio: 4.2.1.2. Cálculo de la EPF.
Resultará del producto entre:
- la suma de los adicionales correspondientes a cada clase de activos; y
- un multiplicador que permite reconocer la garantía en exceso o el valor de
mercado negativo de las operaciones, conforme a la siguiente expresión:
EPF = multiplicador x AdicionalTotal
donde:
es la suma de los adicionales correspondientes a cada clase de activos
–no se reconocen beneficios por diversificación–, calculados de acuerdo con
la metodología expuesta en los acápites viii) a xii) de este punto, y el multi-
plicador se define como:
El multiplicador se reduce a medida que se incrementa la tenencia de garan-
tías en exceso –sujeto a un mínimo de 5 % de la EPF– y operará de la si-
guiente manera:
− Cuando el costo de reposición corriente sea positivo –esto es, cuando el
valor de los activos en garantía sea inferior al valor de mercado neto de los
contratos de derivados– el multiplicador será igual a uno –esto es, el com-
ponente EPF será igual al valor del AdicionalTotal–.
− Cuando el valor de los activos en garantía supere el valor de mercado neto
de los contratos de derivados –garantías en exceso–, el multiplicador será
inferior a la unidad –esto es, el componente EPF será menor que el valor
del AdicionalTotal –.
− El multiplicador se activará –es decir, tomará un valor inferior a la unidad–
también cuando el valor corriente de las operaciones con derivados sea
negativo.
Para determinar el cálculo de la EPF, las operaciones se ajustarán a lo si-
guiente:
− Cada derivado se asignará a una clase de activo sobre la base de su factor
de riesgo principal –que en la mayoría de los casos será el único, definido
por la referencia a un instrumento subyacente, tal como una curva de tasas
de interés en el caso de un “swap” de tasas de interés o
- entidades de la unidad:
  - `e1` Operacion: Operaciones derivados sin liquidación centralizada con márgenes diarios — Operaciones de derivados que no se liquidan en forma centralizada y están sujetas a acuerdos de márgenes diarios
  - `c1` Condicion: MPOR mínimo 10 días hábiles — derivados sin liquidación centralizada — El período de riesgo de margen (MPOR) mínimo será de al menos 10 días hábiles para operaciones de derivados que no se liquidan en forma centralizada y están sujetas a acuerdos de márgenes diarios
  - `e2` Operacion: Operaciones derivados con liquidación centralizada y márgenes diarios — Operaciones de derivados que se liquidan en forma centralizada y están sujetas a acuerdos de márgenes diarios entre miembro compensador y clientes
  - `c2` Condicion: MPOR mínimo 5 días hábiles — derivados con liquidación centralizada — El período de riesgo de margen (MPOR) mínimo será de 5 días hábiles para operaciones de derivados que se liquidan en forma centralizada y están sujetas a acuerdos de márgenes diarios entre miembro com
  - `c3` Condicion: MPOR mínimo 20 días hábiles — neteo con >5.000 operaciones — El período de riesgo de margen (MPOR) mínimo será de 20 días hábiles para conjuntos de neteo (excepto aquellos con contraparte central) cuyo número de operaciones supere 5.000 en cualquier momento del
  - `c4` Condicion: MPOR doble por disputas pendientes en neteo — El período de riesgo de margen será el doble para conjuntos de neteo con disputas pendientes
  - `o1` Obligacion: Reflejar antecedente de disputas mediante MPOR duplicado — La entidad deberá reflejar mediante un MPOR duplicado si ha experimentado más de dos disputas sobre margin calls durante dos trimestres anteriores que se hayan prolongado más que el MPOR correspondien
  - `d1` Definicion: MPOR — Período de riesgo de margen — Período de riesgo de margen correspondiente al acuerdo sobre márgenes aplicable a la operación
  - `o2` Obligacion: Incrementar MPOR cuando frecuencia de reposición no sea diaria — Los mínimos de MPOR se deberán incrementar cuando la frecuencia de reposición de márgenes no sea diaria, usando la fórmula MPOR = mínimo + N - 1, donde N es la cantidad de días entre reposiciones
  - `d2` Definicion: Parámetros de correlación regulatorios — Utilizados solo en el cálculo de la EPF de derivados sobre acciones, créditos y commodities (no aplican a derivados de tasa de interés o tipo de cambio) para ponderar componentes sistemáticos e idiosi
  - `d3` Definicion: Adicional para derivados de tasa de interés — Este adicional captura el riesgo que surge de la correlación imperfecta entre derivados con plazos diferentes. Los derivados se dividen en tres bandas temporales sobre la base de la fecha de finalizac
  - `e3` Operacion: Cálculo nocional efectivo derivados tasa de interés por banda temporal — Cálculo del nocional efectivo para derivados de tasa de interés por banda temporal, que es la suma de nocionales ajustados multiplicados por ajustes delta regulatorios y factor por plazo residual
  - `p1` Potestad: SEFyC puede requerir asignación a múltiples clases de activos — La SEFyC podrá requerir que operaciones complejas (como derivados híbridos) se asignen a más de una clase de activos, debiendo asignarse la posición a múltiples clases y determinarse para cada una el 
  - `d4` Definicion: Adicional para derivados de tipo de cambio — El nocional efectivo se computa como suma de nocionales ajustados multiplicados por deltas regulatorios. El adicional es producto del valor absoluto del nocional efectivo y factor regulatorio (idéntic
  - `d5` Definicion: Adicional para derivados de crédito — Las exposiciones están sujetas a dos niveles de compensación: compensación plena entre derivados de crédito que hacen referencia a misma entidad/índice, y compensación parcial entre entidades diferent
  - `d6` Definicion: Adicional para derivados sobre acciones — Utiliza modelo de factor único dividiendo riesgo de cada entidad en componentes sistemático e idiosincrásico. Permite compensación íntegra de operaciones de una entidad pero solo compensación del comp
  - `d7` Definicion: Adicional para derivados sobre commodities — Emplea modelo de factor único dentro de cada conjunto de cobertura. Permite compensación total entre derivados del mismo tipo de commodity, compensación parcial entre tipos dentro de conjunto, pero si
  - `p2` Potestad: SEFyC puede requerir definiciones precisas de commodities — La SEFyC podrá requerir definiciones más precisas de conjuntos de cobertura por tipo de commodity si alguna entidad tuviera exposición muy significativa al riesgo de base entre productos diferentes de
  - `p3` Potestad: Entidades pueden no reconocer compensaciones entre bandas temporales — Las entidades tienen la opción de no reconocer compensaciones entre bandas temporales en el cálculo del adicional para derivados de tasa de interés, reduciendo la fórmula correspondiente
  - `d8` Definicion: Factores regulatorios, correlaciones y adicionales por volatilidad de opciones — Tabla que especifica para cada clase de activo (tasa de interés, tipo de cambio, crédito, acciones, commodities) los factores SF, correlaciones y volatilidades aplicables, con tratamiento especial par
  - `o3` Obligacion: Aplicar SF multiplicado por 0,5 a operaciones sobre bases — El factor de sensibilidad (SF) a aplicar a operaciones sobre bases será el factor de la clase de activo correspondiente multiplicado por 0,5
  - `o4` Obligacion: Aplicar SF multiplicado por 5 a operaciones sobre volatilidades — El factor a aplicar a operaciones sobre volatilidades será el factor de la clase de activo correspondiente multiplicado por 5
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1; c2 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 204** Condicion `c4`: MPOR doble por disputas pendientes en neteo | descripcion: El período de riesgo de margen será el doble para conjuntos de neteo con disputas pendientes | tramo: El doble del período de riesgo de margen para los conjuntos de neteo con disputas pendientes
  - **caso 205** Condicion `c3`: MPOR mínimo 20 días hábiles — neteo con >5.000 operaciones | descripcion: El período de riesgo de margen (MPOR) mínimo será de 20 días hábiles para conjuntos de neteo (excepto aquellos con contraparte central) cuyo número de operaciones supere 5.000 en cualquier momento del trimestre calendario anterior | tramo: 20 días hábiles para los conjuntos de neteo –excepto aquellos con una contraparte central– cuyo número de operaciones supere las 5.000 en cualquier momento del trimestre calendario anterior

## Unidad `cap::3.1.13.3` (punto_no_item)
- herencia: [intro 3.1] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi-
cional o sintética, o a una estructura con similares características.
La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con-
ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de
deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset-
Backed Securities”, ABS) y bonos de tit | [intro 3.1.13] Al calcular la exigencia de capital, se podrá reconocer la protección crediticia recibida
respecto de una posición de titulización siempre que:
i) Se trate de alguno de los activos admitidos como garantía en los puntos 5.3.1.2. y | [intro 3.1.13] 5.3.2.2. o de garantías personales o de derivados de crédito que cumplan con los
requisitos operativos especificados en el punto 5.2.3.
Se podrán reconocer los activos dados en garantía por los SPE. | [intro 3.1.13] ii) La protección sea provista por alguna de las entidades detalladas en el punto 5.4.1. | [intro 3.1.13] No podrán reconocerse los SPE como garantes admisibles.
- texto propio: 3.1.13.3. Descalce de plazos de vencimiento.
La exigencia de capital para hacer frente a un descalce de plazos de venci-
miento se determinará conforme a lo previsto en el punto 5.4.5. En el caso de
que las exposiciones cubiertas tengan vencimientos diferentes, se usará el
plazo más largo.
Cuando la protección adquirida cubra a los activos titulizados, podrá surgir un
descalce de plazos de vencimiento en el contexto de una titulización sintética.
Cuando se celebra un nuevo contrato que compensa al derivado de crédito o
de cualquier otro modo se le pone fin a la protección original, los plazos efec-
tivos de todos los tramos de la titulización sintética podrían diferir del de las
exposiciones subyacentes.
Las entidades que titulicen sintéticamente las exposiciones que tienen en el
activo a través de la compra de protección por tramos no deberán tener en
cuenta los descalces de plazos de vencimiento de las posiciones de tituliza-
ción a las que se les asigne un ponderador de 1250%. Para cualquier otra
posición de titulización, deberán aplicar el tratamiento establecido en el punto
5.4.5.
- entidades de la unidad:
  - `e1` Operacion: Determinación exigencia capital descalce plazos — Determinación de la exigencia de capital para hacer frente a un descalce de plazos de vencimiento conforme a lo previsto en el punto 5.4.5.
  - `e2` Condicion: Exposiciones cubiertas con vencimientos diferentes — Cuando las exposiciones cubiertas tienen vencimientos diferentes, se usa el plazo más largo.
  - `e3` Obligacion: Usar plazo más largo en vencimientos diferentes — Cuando las exposiciones cubiertas tienen vencimientos diferentes, se usará el plazo más largo.
  - `e4` Condicion: Protección cubre activos titulizados — Cuando la protección adquirida cubre a los activos titulizados, puede surgir un descalce de plazos de vencimiento en el contexto de una titulización sintética.
  - `e5` Operacion: Descalce de plazos en titulización sintética — Surgimiento de un descalce de plazos de vencimiento en el contexto de una titulización sintética cuando la protección adquirida cubre a los activos titulizados.
  - `e6` Condicion: Nuevo contrato compensa derivado de crédito — Cuando se celebra un nuevo contrato que compensa al derivado de crédito o se pone fin a la protección original, los plazos efectivos de todos los tramos de la titulización sintética podrían diferir de
  - `e7` Restriccion: No tener en cuenta descalces ponderador 1250% — Las entidades que titulicen sintéticamente las exposiciones a través de la compra de protección por tramos no deberán tener en cuenta los descalces de plazos de vencimiento de las posiciones de tituli
  - `e8` Obligacion: Aplicar tratamiento punto 5.4.5 otras posiciones — Para cualquier otra posición de titulización que no tenga asignado un ponderador de 1250%, deberán aplicar el tratamiento establecido en el punto 5.4.5.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e3; e4 condicion_de e5
- NODOS A CLASIFICAR:
  - **caso 207** Condicion `e6`: Nuevo contrato compensa derivado de crédito | descripcion: Cuando se celebra un nuevo contrato que compensa al derivado de crédito o se pone fin a la protección original, los plazos efectivos de todos los tramos de la titulización sintética podrían diferir del de las exposiciones subyacentes. | tramo: Cuando se celebra un nuevo contrato que compensa al derivado de crédito o de cualquier otro modo se le pone fin a la protección original

## Unidad `ext::11.1::intro` (intro)
- herencia: [encabezado 11.1] 11.1. Seguimiento de oficializaciones de importación.
- texto propio: Quedarán comprendidas todas las oficializaciones de importación ocurridas a partir del
01/11/19 y aquellas que sean anteriores por las cuales se solicite realizar pagos a través del
mercado de cambios a partir de la mencionada fecha.
Por cada oficialización del despacho de importación, el importador deberá nominar una
entidad para que se haga responsable del seguimiento de la oficialización. Esta entidad será
la responsable de verificar el cumplimiento de las condiciones estipuladas en la presente
normativa que habilitarán el acceso al mercado de cambios y/o la afectación de una
oficialización a la regularización de un pago con registro aduanero pendiente.
La entidad será originalmente nominada por el importador ante la ARCA, pudiendo el
importador posteriormente modificarla en la medida que, a la fecha de la solicitud de cambio
de entidad, no existan certificaciones emitidas de acceso al mercado de cambios que estén
pendientes de uso.
En caso de que el importador no haya nominado a una entidad al momento de la oficialización
podrá posteriormente seleccionar una entidad que se haga cargo del seguimiento.
Serán elegibles para el importador, quedando obligadas a llevar a cabo las responsabilidades
asociadas al presente seguimiento, todas las entidades financieras y casas de cambio salvo
aquellas que hayan notificado al BCRA que han optado por no operar en comercio exterior.
- entidades de la unidad:
  - `e1` Condicion: Oficializaciones desde 01/11/19 — Alcance temporal: oficializaciones de importación ocurridas a partir del 01/11/19, y oficializaciones anteriores para las cuales se solicite realizar pagos a través del mercado de cambios a partir de 
  - `e2` Obligacion: Importador nomina entidad responsable seguimiento — El importador debe nominar una entidad para cada oficialización del despacho de importación, que será responsable del seguimiento de esa oficialización
  - `e3` Obligacion: Entidad nominada verifica cumplimiento condiciones — La entidad nominada es responsable de verificar el cumplimiento de las condiciones que habilitan el acceso al mercado de cambios y/o la afectación de una oficialización a la regularización de un pago 
  - `e4` Obligacion: Entidad nominada originalmente ante ARCA — La entidad es originalmente nominada por el importador ante la ARCA
  - `e5` Potestad: Importador puede modificar entidad nominada — El importador puede posteriormente modificar la entidad nominada, siempre que a la fecha de la solicitud de cambio no existan certificaciones emitidas de acceso al mercado de cambios pendientes de uso
  - `e6` Condicion: No existen certificaciones pendientes de uso — Condición para que el importador pueda modificar la entidad nominada: que no existan certificaciones emitidas de acceso al mercado de cambios pendientes de uso a la fecha de la solicitud
  - `e7` Potestad: Importador puede seleccionar entidad posteriormente — Si el importador no ha nominado una entidad al momento de la oficialización, puede posteriormente seleccionar una entidad que se haga cargo del seguimiento
  - `e8` Obligacion: Entidades financieras y casas de cambio obligadas a llevar responsabilidades — Las entidades financieras y casas de cambio son elegibles y quedan obligadas a llevar a cabo las responsabilidades asociadas al seguimiento, excepto aquellas que hayan notificado al BCRA que han optad
  - `e9` Excepcion: Excepción entidades que optaron no operar comercio exterior — Quedan exceptuadas las entidades financieras y casas de cambio que hayan notificado al BCRA que han optado por no operar en comercio exterior
- relaciones del crudo (sin establecida_en ni de sujeto): e6 condicion_de e5; e9 exceptua_obligacion e8
- NODOS A CLASIFICAR:
  - **caso 208** Condicion `e1`: Oficializaciones desde 01/11/19 | descripcion: Alcance temporal: oficializaciones de importación ocurridas a partir del 01/11/19, y oficializaciones anteriores para las cuales se solicite realizar pagos a través del mercado de cambios a partir de esa fecha | tramo: Quedarán comprendidas todas las oficializaciones de importación ocurridas a partir del 01/11/19 y aquellas que sean anteriores por las cuales se solicite realizar pagos a través del mercado de cambios a partir de la mencionada fecha

## Unidad `ext::10.3.2.3` (item)
- herencia: **[abre la lista]** [intro 10.3.2] en el SEPAIMPO.
La entidad interviniente podrá dar acceso al mercado de cambios para el pago al
exterior de importaciones de bienes que cuentan con registro de ingreso aduanero
que constan en el SEPAIMPO, en la medida que verifique previamente la totalidad de
los siguientes requisitos: | [cierre 10.3.2] Los casos que no encuadren en lo expuesto precedentemente quedan sujetos a la
conformidad previa del BCRA, debiendo los pedidos ser canalizados por una entidad
autorizada a realizar este tipo de pagos.
- texto propio: 10.3.2.3. El pago no se realiza con anterioridad a la fecha de vencimiento de la
obligación con el exterior.
Este requisito no resultará aplicable cuando el cliente sea un Vehículo de
Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes
Inversiones (RIGI) y se cancelen financiaciones comerciales en el marco de
lo previsto en el punto 14.2.1.
- entidades de la unidad:
  - `c1` Condicion: Pago anterior a vencimiento de obligación — El pago no debe realizarse antes de la fecha de vencimiento de la obligación con el exterior
  - `e1` Excepcion: Excepción VPU RIGI — cancelación de financiaciones comerciales — El requisito de no realizar el pago con anterioridad al vencimiento no aplica cuando el cliente es un VPU adherido al RIGI y se cancelan financiaciones comerciales conforme al punto 14.2.1
- relaciones del crudo (sin establecida_en ni de sujeto): e1 exceptua c1
- NODOS A CLASIFICAR:
  - **caso 212** Condicion `c1`: Pago anterior a vencimiento de obligación | descripcion: El pago no debe realizarse antes de la fecha de vencimiento de la obligación con el exterior | tramo: El pago no se realiza con anterioridad a la fecha de vencimiento de la obligación con el exterior

## Unidad `ext::10.11.2` (item)
- herencia: **[abre la lista]** [intro 10.11] aduanero hasta el 12/12/23.
Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para
realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el
12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad
verifique que:
- texto propio: 10.11.2. el pago corresponda a la cancelación de deudas por operaciones financiadas o
garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o
agencias oficiales de crédito; o
Las entidades podrán considerar también como operación garantizada por una
agencia oficial de crédito a aquella que se encuentre cubierta por una garantía
emitida por una aseguradora privada por cuenta y orden de un gobierno nacional
de otro país. En todos los casos, la entidad interviniente deberá contar con
documentación en la que conste explícitamente tal situación.
- entidades de la unidad:
  - `e1` Condicion: Pago cancelación deudas operaciones financiadas/garantizadas — El pago corresponde a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito
  - `e2` Potestad: Considerar operación garantizada por aseguradora privada — Las entidades podrán considerar como operación garantizada por una agencia oficial de crédito aquella que se encuentre cubierta por una garantía emitida por una aseguradora privada por cuenta y orden 
  - `e3` Obligacion: Contar con documentación de garantía de aseguradora privada — La entidad interviniente deberá contar con documentación en la que conste explícitamente que la operación se encuentra cubierta por una garantía emitida por una aseguradora privada por cuenta y orden 
  - `e4` Definicion: Operación garantizada por agencia oficial de crédito — Aquella que se encuentre cubierta por una garantía emitida por una aseguradora privada por cuenta y orden de un gobierno nacional de otro país
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 213** Condicion `e1`: Pago cancelación deudas operaciones financiadas/garantizadas | descripcion: El pago corresponde a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito | tramo: el pago corresponda a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito

## Unidad `ext::13.3.7` (item)
- herencia: **[abre la lista]** [intro 13.3] anterioridad a lo previsto en los puntos 13.2.3. a 13.2.7.
También será admisible el acceso para el pago de servicios que fueron o serán prestados o
devengados a partir del 13/12/23 con antelación a los plazos previstos en los puntos 13.2.3.
a 13.2.7., cuando adicionalmente a los restantes requisitos normativo, se verifique el
encuadre en alguna de las siguientes situaciones:
- texto propio: 13.3.7. el pago corresponda a la cancelación de deudas por operaciones
financiadas o garantizadas con anterioridad al 13/12/23 por organismos
internacionales y/o agencias oficiales de crédito.
Las entidades podrán considerar también como operación garantizada por
una agencia oficial de crédito a aquella que se encuentre cubierta por una
garantía emitida por una aseguradora privada por cuenta y orden de un
gobierno nacional de otro país. En todos los casos, la entidad interviniente
deberá contar con documentación en la que conste explícitamente tal
situación.
- entidades de la unidad:
  - `c1` Condicion: Pago por cancelación de deudas — operaciones financiadas/garantizadas — El pago corresponde a la cancelación de deudas por operaciones que fueron financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito.
  - `p1` Potestad: Considerar operación garantizada por aseguradora privada — Las entidades tienen la facultad de considerar como operación garantizada por una agencia oficial de crédito aquella que se encuentre cubierta por una garantía emitida por una aseguradora privada por 
  - `o1` Obligacion: Contar con documentación de garantía por aseguradora privada — En todos los casos en que se considere una operación garantizada por una aseguradora privada por cuenta y orden de un gobierno nacional de otro país, la entidad interviniente debe contar con documenta
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 219** Condicion `c1`: Pago por cancelación de deudas — operaciones financiadas/garantizadas | descripcion: El pago corresponde a la cancelación de deudas por operaciones que fueron financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito. | tramo: el pago corresponda a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito

## Unidad `ext::7.6.1.1` (item)
- herencia: [intro 7.6] Un permiso de embarque será registrado por la entidad de seguimiento en la condición de
“Incumplido en gestión de cobro” cuando se haya verificado que el incumplimiento se debe a
la falta de pago del importador, por haberse demostrado las situaciones previstas conforme a
los puntos 7.6.1. a 7.6.3.
En todos los casos la entidad deberá obtener la declaración jurada sobre el carácter genuino
de lo declarado, firmada por el exportador o quien ejerza su representación legal o un
apoderado con faculta | **[abre la lista]** [intro 7.6.1] Cuando la falta de pago del importador extranjero se deba a la existencia de al menos
una de las siguientes situaciones:
- texto propio: 7.6.1.1. El país de destino de la exportación haya implementado restricciones a los
giros de divisas al exterior para el pago de importaciones con posterioridad
al embarque de la mercadería, y mientras duren estas restricciones, lo cual
será acreditado mediante copia con legalización consular, de la normativa
que dispone dicho control cambiario.
- entidades de la unidad:
  - `e1` Condicion: País destino implementó restricciones giros divisas — El país de destino de la exportación ha implementado restricciones a los giros de divisas al exterior para el pago de importaciones después del embarque de la mercadería.
  - `e2` Condicion: Restricciones vigentes mientras duren — Las restricciones a los giros de divisas permanecen vigentes durante el período en que se mantienen en el país de destino.
  - `e3` Obligacion: Acreditar restricciones cambiarias con copia legalizada — Acreditar la existencia de restricciones cambiarias mediante copia con legalización consular de la normativa que dispone el control cambiario en el país de destino.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 220** Condicion `e1`: País destino implementó restricciones giros divisas | descripcion: El país de destino de la exportación ha implementado restricciones a los giros de divisas al exterior para el pago de importaciones después del embarque de la mercadería. | tramo: El país de destino de la exportación haya implementado restricciones a los giros de divisas al exterior para el pago de importaciones con posterioridad al embarque de la mercadería
  - **caso 242** Condicion `e2`: Restricciones vigentes mientras duren | descripcion: Las restricciones a los giros de divisas permanecen vigentes durante el período en que se mantienen en el país de destino. | tramo: mientras duren estas restricciones

## Unidad `cap::5.3.2.3` (punto_no_item)
- herencia: [chapeau_seccion S5] A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o
parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera
de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las
técnicas previstas en el punto 5.1.
La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia-
ción con títulos valores (securities financing transactions, SFT) –co | [intro 5.3] La aplicación de la técnica de cobertura mediante activos admitidos como garantía dependerá
del método elegido. | [intro 5.3.2] Con este método, las entidades financieras deberán ajustar los valores de la exposición
y del activo recibido en garantía, a fin de tener en cuenta posibles futuras variaciones de
su valor de mercado. El importe resultante luego de realizar este ajuste por volatilidad
será superior en el caso de la exposición –con la excepción de los préstamos otorgados
en efectivo– e inferior en el caso de la garantía –excepto cuando esté constituida por un
depósito en la misma moneda que la exposición–.
El act | [intro 5.3.2] e c fx | [intro 5.3.2] prevista en el punto 5.3.2.3.– multiplicada por el ponderador de riesgo de la contraparte
–conforme a la tabla de ponderadores de riesgo de la Sección 2.–.
- texto propio: 5.3.2.3. Aforos regulatorios.
Las entidades financieras que utilicen el método integral deberán emplear los
siguientes aforos –los cuales suponen una valuación diaria a precios de merca-
do, una liquidación/reposición diaria de márgenes, y un período de manteni-
miento de 10 días hábiles–:
[TABLA cap::tabla032 | página 108 | e0_tablas | posicional]
Fila 1: col1 = Tipo de activo ⟨abarca hasta col2⟩ | col3 = Plazo de vencimiento residual: ⟨abarca hasta col7⟩
Fila 2: col3 = ≤ 1 año | col4 = >1 año y ≤ 3 años | col5 = >3 años y ≤ 5 años | col6 = >5 años y ≤ 10 años | col7 = >10años
Fila 3: col1 = Títulos valores emiti- dos por el sector pú- blico no financiero y por otros soberanos, e instrumentos de regulación monetaria emitidos por el BCRA, según ponderador de riesgo del emisor | col2 = 0% | col3 = 0,5% | col4 = 2% ⟨abarca hasta col5⟩ | col6 = 4% ⟨abarca hasta col7⟩
Fila 4: col1 = Títulos valores emiti- dos por el sector pú- blico no financiero y por otros soberanos, e instrumentos de regulación monetaria emitidos por el BCRA, según ponderador de riesgo del emisor ⟨combinada con fila 3⟩ | col2 = 20% o 50% | col3 = 1% | col4 = 3% ⟨abarca hasta col5⟩ | col6 = 6% ⟨abarca hasta col7⟩
Fila 5: col1 = Títulos valores emiti- dos por el sector pú- blico no financiero y por otros soberanos, e instrumentos de regulación monetaria emitidos por el BCRA, según ponderador de riesgo del emisor ⟨combinada con fila 3⟩ | col2 = 100% | col3 = 15% ⟨abarca hasta col7⟩
Fila 6: col1 = Títulos de deuda emitidos por empresas con “grado de inver- sión” ⟨abarca hasta col2⟩ | col3 = 2% | col4 = 4% | col5 = 6% | col6 = 12% | col7 = 20%
Fila 7: col1 = Títulos de deuda emitidos por fideicomisos financieros ⟨abarca hasta col2⟩ | col3 = 4% | col4 = 12% ⟨abarca hasta col5⟩ | col6 = 24% ⟨abarca hasta col7⟩

- entidades de la unidad:
  - `op1` Operacion: Cálculo de activo ponderado por riesgo — método integral — Cálculo del activo ponderado por riesgo como diferencia entre exposición ajustada por volatilidad y valor de garantía con aforos aplicados, multiplicado por ponderador de riesgo de contraparte
  - `r1` Restriccion: Aforo 0% — títulos públicos ponderador 0%, plazo ≤1 año — Aforo del 0% para títulos valores emitidos por sector público no financiero, otros soberanos e instrumentos de regulación monetaria del BCRA con ponderador de riesgo 0%, plazo de vencimiento residual 
  - `r2` Restriccion: Aforo 0,5% — títulos públicos ponderador 0%, plazo >1 año y ≤3 años — Aforo del 0,5% para títulos valores emitidos por sector público no financiero, otros soberanos e instrumentos de regulación monetaria del BCRA con ponderador de riesgo 0%, plazo de vencimiento residua
  - `r3` Restriccion: Aforo 2% — títulos públicos ponderador 0%, plazo >3 años y ≤5 años — Aforo del 2% para títulos valores emitidos por sector público no financiero, otros soberanos e instrumentos de regulación monetaria del BCRA con ponderador de riesgo 0%, plazo de vencimiento residual 
  - `r4` Restriccion: Aforo 4% — títulos públicos ponderador 0%, plazo >5 años y ≤10 años — Aforo del 4% para títulos valores emitidos por sector público no financiero, otros soberanos e instrumentos de regulación monetaria del BCRA con ponderador de riesgo 0%, plazo de vencimiento residual 
  - `r5` Restriccion: Aforo 4% — títulos públicos ponderador 0%, plazo >10 años — Aforo del 4% para títulos valores emitidos por sector público no financiero, otros soberanos e instrumentos de regulación monetaria del BCRA con ponderador de riesgo 0%, plazo de vencimiento residual 
  - `r6` Restriccion: Aforo 20% o 50% — títulos públicos ponderador 20% o 50%, plazo ≤1 año — Aforo del 20% o 50% para títulos valores emitidos por sector público no financiero, otros soberanos e instrumentos de regulación monetaria del BCRA con ponderador de riesgo 20% o 50%, plazo de vencimi
  - `r7` Restriccion: Aforo 1% — títulos públicos ponderador 20% o 50%, plazo >1 año y ≤3 años — Aforo del 1% para títulos valores emitidos por sector público no financiero, otros soberanos e instrumentos de regulación monetaria del BCRA con ponderador de riesgo 20% o 50%, plazo de vencimiento re
  - `r8` Restriccion: Aforo 3% — títulos públicos ponderador 20% o 50%, plazo >3 años y ≤5 años — Aforo del 3% para títulos valores emitidos por sector público no financiero, otros soberanos e instrumentos de regulación monetaria del BCRA con ponderador de riesgo 20% o 50%, plazo de vencimiento re
  - `r9` Restriccion: Aforo 6% — títulos públicos ponderador 20% o 50%, plazo >5 años y ≤10 años — Aforo del 6% para títulos valores emitidos por sector público no financiero, otros soberanos e instrumentos de regulación monetaria del BCRA con ponderador de riesgo 20% o 50%, plazo de vencimiento re
  - `r10` Restriccion: Aforo 6% — títulos públicos ponderador 20% o 50%, plazo >10 años — Aforo del 6% para títulos valores emitidos por sector público no financiero, otros soberanos e instrumentos de regulación monetaria del BCRA con ponderador de riesgo 20% o 50%, plazo de vencimiento re
  - `r11` Restriccion: Aforo 15% — títulos públicos ponderador 100%, todos los plazos — Aforo del 15% para títulos valores emitidos por sector público no financiero, otros soberanos e instrumentos de regulación monetaria del BCRA con ponderador de riesgo 100%, todos los plazos de vencimi
  - `r12` Restriccion: Aforo 2% — títulos deuda grado inversión, plazo ≤1 año — Aforo del 2% para títulos de deuda emitidos por empresas con grado de inversión, plazo de vencimiento residual ≤ 1 año
  - `r13` Restriccion: Aforo 4% — títulos deuda grado inversión, plazo >1 año y ≤3 años — Aforo del 4% para títulos de deuda emitidos por empresas con grado de inversión, plazo de vencimiento residual >1 año y ≤3 años
  - `r14` Restriccion: Aforo 6% — títulos deuda grado inversión, plazo >3 años y ≤5 años — Aforo del 6% para títulos de deuda emitidos por empresas con grado de inversión, plazo de vencimiento residual >3 años y ≤5 años
  - `r15` Restriccion: Aforo 12% — títulos deuda grado inversión, plazo >5 años y ≤10 años — Aforo del 12% para títulos de deuda emitidos por empresas con grado de inversión, plazo de vencimiento residual >5 años y ≤10 años
  - `r16` Restriccion: Aforo 20% — títulos deuda grado inversión, plazo >10 años — Aforo del 20% para títulos de deuda emitidos por empresas con grado de inversión, plazo de vencimiento residual >10 años
  - `r17` Restriccion: Aforo 4% — títulos deuda fideicomisos financieros, plazo ≤1 año — Aforo del 4% para títulos de deuda emitidos por fideicomisos financieros, plazo de vencimiento residual ≤ 1 año
  - `r18` Restriccion: Aforo 12% — títulos deuda fideicomisos financieros, plazo >1 año y ≤5 años — Aforo del 12% para títulos de deuda emitidos por fideicomisos financieros, plazo de vencimiento residual >1 año y ≤5 años
  - `r19` Restriccion: Aforo 24% — títulos deuda fideicomisos financieros, plazo >5 años — Aforo del 24% para títulos de deuda emitidos por fideicomisos financieros, plazo de vencimiento residual >5 años
  - `r20` Restriccion: Aforo 0% — efectivo en depósito, todos los plazos — Aforo del 0% para efectivo en depósito, todos los plazos de vencimiento residual
  - `r21` Restriccion: Aforo 20% — acciones en índices principales y oro, todos los plazos — Aforo del 20% para acciones (y bonos convertibles en acciones) incluidas en índices bursátiles principales y oro, todos los plazos de vencimiento residual
  - `r22` Restriccion: Aforo 30% — otras acciones cotizadas, todos los plazos — Aforo del 30% para otras acciones (y bonos convertibles en acciones) que coticen en bolsas o mercados de valores regulados, todos los plazos de vencimiento residual
  - `r23` Restriccion: Aforo mayor o media ponderada — cuotapartes FCI, depository receipts, CEDEAR y CEVA — Aforo para cuotapartes emitidas por fondos comunes de inversión (FCI), depository receipts, CEDEAR y CEVA: el mayor aforo que corresponda a cualquier título valor que integre el instrumento
  - `exc1` Excepcion: Excepción look-through — FCI con enfoque de transparencia — Excepción a la aplicación del mayor aforo: cuando la entidad pueda aplicar el enfoque de transparencia (look-through approach) para inversiones en acciones a través de FCI, podrá utilizar una media po
  - `r24` Restriccion: Aforo 30% — otras exposiciones, todos los plazos — Aforo del 30% para otro tipo de exposiciones, todos los plazos de vencimiento residual
  - `r25` Restriccion: Aforo 8% — descalce de monedas — Aforo por descalce de monedas del 8%, aplicable cuando la exposición y el activo recibido en garantía se encuentren denominados en monedas diferentes, sobre la base de un período de mantenimiento de 1
  - `cond1` Condicion: Ajuste de aforo por período de mantenimiento diferente — Condición para ajustar los aforos: cuando el período de mantenimiento o el período transcurrido entre liquidaciones/reposiciones de márgenes o valuaciones a precios de mercado sean distintos de los es
  - `ob1` Obligacion: Ajuste de aforo — fórmula raíz cuadrada del tiempo — Los aforos se modificarán utilizando la fórmula de la raíz cuadrada del tiempo cuando el período de mantenimiento o el período transcurrido entre liquidaciones/reposiciones de márgenes o valuaciones a
  - `r26` Restriccion: Aforo 30% — SFT con instrumentos no admisibles prestados o entregados — Aforo del 30% para operaciones de financiación con títulos valores (SFT) en las que la entidad financiera preste o entregue como garantía instrumentos no admisibles
  - `r27` Restriccion: Prohibición cobertura — SFT con instrumentos no admisibles tomados prestados o recibidos — Prohibición de aplicar cobertura del riesgo de crédito en operaciones de financiación con títulos valores (SFT) en las que la entidad financiera tome prestados o reciba como garantía instrumentos no a
  - `cond2` Condicion: Período de mantenimiento mínimo — operaciones de pase — Para operaciones de pase con liquidación/reposición diaria de márgenes, el período de mantenimiento mínimo es de 5 días hábiles
  - `cond3` Condicion: Período de mantenimiento mínimo — otras operaciones mercado de capitales — Para otras operaciones realizadas en el mercado de capitales con liquidación/reposición diaria de márgenes, el período de mantenimiento mínimo es de 10 días hábiles
  - `cond4` Condicion: Período de mantenimiento mínimo — préstamos garantizados — Para préstamos garantizados con títulos valores u otros activos admitidos como garantía con revaluación diaria, el período de mantenimiento mínimo es de 20 días hábiles
  - `ob2` Obligacion: Empleo de aforos regulatorios — método integral — Las entidades financieras que utilicen el método integral deberán emplear los aforos regulatorios establecidos, que suponen valuación diaria a precios de mercado, liquidación/reposición diaria de márg
- relaciones del crudo (sin establecida_en ni de sujeto): exc1 exceptua r23; cond1 condiciona ob1
- NODOS A CLASIFICAR:
  - **caso 222** Condicion `cond2`: Período de mantenimiento mínimo — operaciones de pase | descripcion: Para operaciones de pase con liquidación/reposición diaria de márgenes, el período de mantenimiento mínimo es de 5 días hábiles | tramo: Operaciones de pase | col2 = Liquidación / reposición diaria de márgenes | col3 = 5 días hábiles
  - **caso 223** Condicion `cond3`: Período de mantenimiento mínimo — otras operaciones mercado de capitales | descripcion: Para otras operaciones realizadas en el mercado de capitales con liquidación/reposición diaria de márgenes, el período de mantenimiento mínimo es de 10 días hábiles | tramo: Otras operaciones realizadas en el mercado de capitales | col2 = Liquidación / reposición diaria de márgenes | col3 = 10 días hábiles
  - **caso 224** Condicion `cond4`: Período de mantenimiento mínimo — préstamos garantizados | descripcion: Para préstamos garantizados con títulos valores u otros activos admitidos como garantía con revaluación diaria, el período de mantenimiento mínimo es de 20 días hábiles | tramo: Préstamos garantizados con títulos valores u otros activos admitidos como garantía | col2 = Revaluación diaria | col3 = 20 días hábiles

## Unidad `ctacte::1.5.2.3` (punto_no_item)
- herencia: [intro 1.5] En sus cláusulas se deberá prever, como mínimo: | [encabezado 1.5.2] 1.5.2. Obligaciones de la entidad.
- texto propio: 1.5.2.3. Enviar al cuentacorrentista, como máximo 8 días corridos después de finalizado
cada mes y/o el período menor que se establezca y en las condiciones que se
convenga, un extracto con el detalle de cada uno de los movimientos que se
efectúen en la cuenta –débitos y créditos–, cualquiera sea su concepto, identifi-
cando los distintos tipos de transacción mediante un código específico que cada
entidad instrumente a tal efecto y los saldos registrados en el período que com-
prende, pidiéndole su conformidad por escrito. También se deberán identificar en
el correspondiente extracto las operaciones realizadas por cuenta propia o por
cuenta de terceros, en la medida que se trate de depósitos de cheques por im-
portes superiores a $ 1.000 y que así se encuentren identificados por el corres-
pondiente endoso, mediante el procedimiento único que cada entidad opte por
aplicar a tal fin.
Adicionalmente, en el resumen se hará constar la clave bancaria uniforme (CBU)
para que el cliente pueda formular su adhesión a servicios de débito automático,
el plazo de compensación vigente para la operatoria de depósito de cheques y
otros documentos compensables y el importe total debitado en el período en
concepto de “Impuesto a las transacciones financieras”.
En ese extracto o resumen de cuenta, adicionalmente las entidades informarán
los siguientes datos mínimos:
i) De producirse débitos correspondientes al servicio de débito automático:
- Denominación de la empresa prestadora de servicios, organismo recauda-
dor de impuestos, etc., al cual se destinaron los fondos debitados.
- Identificación del cliente en la empresa o ente (apellido y nombre o código
o cuenta, etc.).
- Concepto de la operación causante del débito (mes, bimestre, cuota, etc.).
- Importe debitado.
- Fecha de débito.
i
- entidades de la unidad:
  - `e1` Obligacion: Envío de extracto mensual al cuentacorrentista — Enviar al cuentacorrentista un extracto con detalle de movimientos (débitos y créditos), identificando tipos de transacción mediante código específico y saldos del período, solicitando conformidad por
  - `e2` Obligacion: Identificación de operaciones por cuenta propia o terceros en extracto — Identificar en el extracto las operaciones realizadas por cuenta propia o por cuenta de terceros, cuando se trate de depósitos de cheques por importes superiores a $ 1.000 identificados por endoso, me
  - `e3` Obligacion: Inclusión de CBU en resumen de cuenta — Incluir en el resumen la clave bancaria uniforme (CBU) para que el cliente pueda formular su adhesión a servicios de débito automático.
  - `e4` Obligacion: Información de plazo de compensación en resumen — Incluir en el resumen el plazo de compensación vigente para la operatoria de depósito de cheques y otros documentos compensables.
  - `e5` Obligacion: Información de impuesto a transacciones financieras en resumen — Incluir en el resumen el importe total debitado en el período en concepto de Impuesto a las transacciones financieras.
  - `e6` Obligacion: Información de débitos de débito automático en extracto — Informar en el extracto, cuando se produzcan débitos de débito automático: denominación de la empresa prestadora o ente recaudador, identificación del cliente, concepto de la operación, importe debita
  - `e7` Obligacion: Información de transferencias en extracto — Informar en el extracto, cuando se efectúen transferencias, la información prevista en el punto 3.2. de las normas sobre Sistema Nacional de Pagos – Transferencias, según corresponda.
  - `e8` Condicion: Presunción de conformidad con movimiento registrado — Se presume conformidad con el movimiento registrado en el banco si dentro de 60 días corridos de vencido el período no se ha presentado reclamo en la entidad financiera.
  - `e9` Obligacion: Información de tasas de interés en extracto — Informar en el extracto, cuando se reconozcan intereses sobre saldos acreedores, las tasas nominal y efectiva, ambas anuales, correspondientes al período informado.
  - `e10` Obligacion: Inclusión de leyenda de garantía de depósitos — Incluir en el extracto la leyenda que corresponda en materia de garantía de los depósitos, según lo previsto en el punto 6. de las normas sobre Aplicación del sistema de seguro de garantía de los depó
  - `e11` Obligacion: Inclusión de datos de identificación tributaria de titulares — Incluir en el extracto el número de clave de identificación tributaria (CUIT, CUIL o CDI) de los titulares de la cuenta según registros de la depositaria. Obligatorio consignar datos de hasta tres tit
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 232** Condicion `e8`: Presunción de conformidad con movimiento registrado | descripcion: Se presume conformidad con el movimiento registrado en el banco si dentro de 60 días corridos de vencido el período no se ha presentado reclamo en la entidad financiera. | tramo: Se presumirá conformidad con el movimiento registrado en el banco si dentro de los 60 días corridos de vencido el respectivo período no se ha presentado en la entidad financiera la formulación de un reclamo.

## Unidad `cla::6.5.3.1` (item)
- herencia: [intro 6.5] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudor | **[abre la lista]** [intro 6.5.3] El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender
normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos,
esos problemas pueden resultar en una pérdida para la entidad financiera.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- texto propio: 6.5.3.1. Presente una situación financiera ilíquida y un nivel de flujo de fondos que no le
permita atender el pago de la totalidad del capital y de los intereses de las deu-
das, pudiendo cubrir solamente estos últimos. Escasa capacidad de ganancias.
La proyección del flujo de fondos muestra un progresivo deterioro y una alta
sensibilidad a modificaciones menores y previsibles de variables propias o del
entorno, debilitando aún más sus posibilidades de pago.
En el análisis que se lleve a cabo deberá tenerse en cuenta, de corresponder, la
eventual incidencia que en su capacidad de pago pueda tener la situación en la
que se encuentran los demás integrantes del grupo de contrapartes conectadas
al cual pertenece.
- entidades de la unidad:
  - `e1` Definicion: Clasificación Con problemas — indicador iliquidez — Situación en la que el cliente presenta iliquidez financiera y un nivel de flujo de fondos insuficiente para atender el pago de la totalidad del capital y de los intereses de las deudas, pudiendo cubr
  - `e2` Definicion: Indicador Con problemas — escasa capacidad de ganancias — Indicador de clasificación que refleja escasa capacidad de ganancias del cliente.
  - `e3` Condicion: Proyección flujo fondos — deterioro progresivo y alta sensibilidad — Condición que caracteriza la situación de clasificación Con problemas: la proyección del flujo de fondos muestra deterioro progresivo y alta sensibilidad a cambios menores y previsibles de variables p
  - `e4` Obligacion: Considerar incidencia grupo contrapartes conectadas — análisis flujo fondos — Deber de considerar, en el análisis de clasificación, la eventual incidencia que la situación de los demás integrantes del grupo de contrapartes conectadas pueda tener en la capacidad de pago del clie
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 233** Condicion `e3`: Proyección flujo fondos — deterioro progresivo y alta sensibilidad | descripcion: Condición que caracteriza la situación de clasificación Con problemas: la proyección del flujo de fondos muestra deterioro progresivo y alta sensibilidad a cambios menores y previsibles de variables propias o del entorno. | tramo: La proyección del flujo de fondos muestra un progresivo deterioro y una alta sensibilidad a modificaciones menores y previsibles de variables propias o del entorno, debilitando aún más sus posibilidades de pago

## Unidad `cap::2.11.3.1` (item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca | **[abre la lista]** [intro 2.11.3] A los fines de determinar si una exposición debe ser tratada como una acción, las en-
tidades financieras del grupo 1 deberán tener en cuenta la realidad económica del ins-
trumento.
Quedan comprendidas:
- texto propio: 2.11.3.1. Participaciones directas e indirectas en el patrimonio y las utilidades de las
entidades financieras y las empresas, con o sin derecho a voto. Las partici-
paciones indirectas incluyen, entre otras, a la tenencia de instrumentos deri-
vados vinculados a acciones y a las acciones, cuotas o partes de interés en
sociedades comerciales cuya principal actividad sea la inversión en accio-
nes.
- entidades de la unidad:
  - `e1` Definicion: Participaciones directas e indirectas — acción — Incluyen la tenencia de instrumentos derivados vinculados a acciones y las acciones, cuotas o partes de interés en sociedades comerciales cuya principal actividad sea la inversión en acciones.
  - `e2` Operacion: Tenencia de instrumentos derivados vinculados a acciones — Tenencia de instrumentos derivados vinculados a acciones, comprendida como una participación indirecta en el patrimonio y las utilidades de entidades financieras y empresas.
  - `e3` Operacion: Tenencia de acciones, cuotas o partes en sociedades de inversión — Tenencia de acciones, cuotas o partes de interés en sociedades comerciales cuya principal actividad sea la inversión en acciones, comprendida como una participación indirecta en el patrimonio y las ut
  - `e4` Condicion: Realidad económica del instrumento — grupo 1 — Para que una exposición sea tratada como una acción, las entidades financieras del grupo 1 deben considerar la realidad económica del instrumento.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 234** Condicion `e4`: Realidad económica del instrumento — grupo 1 | descripcion: Para que una exposición sea tratada como una acción, las entidades financieras del grupo 1 deben considerar la realidad económica del instrumento. | tramo: A los fines de determinar si una exposición debe ser tratada como una acción, las entidades financieras del grupo 1 deberán tener en cuenta la realidad económica del instrumento

## Unidad `ctacte::6.4.7.3` (item)
- herencia: **[abre la lista]** [intro 6.4.7] a las presentes disposiciones, se observará el siguiente proceso: | [cierre 6.4.7] Igual procedimiento se empleará en los casos de inhabilitaciones de cuentacorrentistas
que sean improcedentes, por haberse omitido informar al Banco Central de la República
Argentina el pago de multas previstas en la legislación, abonadas por los clientes.
- texto propio: 6.4.7.3. Cuando el Banco Central de la República Argentina deba modificar un cómputo
-cualquiera sea su motivo- en la “Central de cheques rechazados” que adminis-
tra, deberá abonarse la suma de $90 por cada uno de ellos en concepto de com-
pensación de gastos operativos.
Corresponderá ese pago cualquiera sea el motivo que origine la rectificación,
excepto que se trate de los rechazos producidos entre la fecha de presentación
judicial del deudor solicitando su concurso preventivo y la fecha de notificación a
la entidad financiera girada de la declaración de apertura del concurso.
En el caso de que las modificaciones se originen en un error operativo que afec-
te en forma masiva a los cheques rechazados que se informen y la alteración
sea común a todos ellos, el importe total por ese concepto no excederá de
$90.000 para el conjunto de estos registros, por presentación, con independen-
cia de la aplicación de lo dispuesto en el párrafo anterior para el resto de las si-
tuaciones derivadas de otros motivos. A estos fines la detección del error y su in-
formación al Banco Central de la República Argentina, ajustada a las formalida-
des establecidas por separado, debe completarse en un período máximo de 60
días corridos.
Estos gastos no podrán ser trasladados al cuentacorrentista, salvo que el pedido
de modificación se origine en causas atribuibles al cliente.
- entidades de la unidad:
  - `e1` Operacion: Modificación de cómputo en Central de cheques rechazados — Modificación de un cómputo en la Central de cheques rechazados administrada por el BCRA, cualquiera sea su motivo
  - `e2` Obligacion: Abono de $90 por modificación de cheque rechazado — Deberá abonarse la suma de $90 por cada cheque rechazado cuyo cómputo sea modificado, en concepto de compensación de gastos operativos
  - `e3` Condicion: Rechazos entre presentación judicial de concurso preventivo y notificación de apertura — Supuesto en que se trata de rechazos producidos entre la fecha de presentación judicial del deudor solicitando su concurso preventivo y la fecha de notificación a la entidad financiera girada de la de
  - `e4` Excepcion: Excepción — rechazos en período de concurso preventivo — No corresponde el pago de $90 cuando los rechazos se produjeron entre la presentación judicial del concurso preventivo y la notificación de la apertura del concurso
  - `e5` Restriccion: Tope $90.000 — error operativo masivo en cheques rechazados — Cuando las modificaciones se originen en un error operativo que afecte en forma masiva a los cheques rechazados que se informen y la alteración sea común a todos ellos, el importe total no excederá de
  - `e6` Condicion: Error operativo masivo común a todos los cheques — Supuesto en que las modificaciones se originen en un error operativo que afecte en forma masiva a los cheques rechazados que se informen y la alteración sea común a todos ellos
  - `e7` Condicion: Detección e información del error dentro de 60 días corridos — La detección del error y su información al BCRA, ajustada a las formalidades establecidas, debe completarse en un período máximo de 60 días corridos
  - `e8` Restriccion: Prohibición de trasladar gastos al cuentacorrentista — Los gastos de compensación no podrán ser trasladados al cuentacorrentista
  - `e9` Excepcion: Excepción — traslado de gastos por causas atribuibles al cliente — Excepción: los gastos sí podrán ser trasladados al cuentacorrentista cuando el pedido de modificación se origine en causas atribuibles al cliente
- relaciones del crudo (sin establecida_en ni de sujeto): e4 exceptua_obligacion e2; e6 condicion_de e5; e7 condicion_de e5; e9 exceptua e8
- NODOS A CLASIFICAR:
  - **caso 235** Condicion `e3`: Rechazos entre presentación judicial de concurso preventivo y notificación de apertura | descripcion: Supuesto en que se trata de rechazos producidos entre la fecha de presentación judicial del deudor solicitando su concurso preventivo y la fecha de notificación a la entidad financiera girada de la declaración de apertura del concurso | tramo: excepto que se trate de los rechazos producidos entre la fecha de presentación judicial del deudor solicitando su concurso preventivo y la fecha de notificación a la entidad financiera girada de la declaración de apertura del concurso

## Unidad `ric::5.1.1` (punto_no_item)
- herencia: [encabezado 5.1] 5.1. Normas de procedimiento
- texto propio: 5.1.1. Exigencia por riesgo operacional para entidades del Grupo 1
Se determinará mensualmente por la siguiente expresión:
CRO = BIC x ILM
donde:
CRO: exigencia de capital por riesgo operacional.
ILM: multiplicador de pérdida interna igual a 1.
BIC: componente del indicador de negocio = ∑ BI x α
i i
donde; α coeficiente marginal, determinado en función del tramo del BI:
i:
[TABLA ric::tabla014 | página 21 | e0_tablas | columnas]
Columnas: Categoría | Tramo de BI (en miles de millones de euros*) | Coeficientes marginales de BI (αi)
Fila 1: Categoría = 1 | Tramo de BI (en miles de millones de euros*) = ≤ 1 | Coeficientes marginales de BI (αi) = 12 %
Fila 2: Categoría = 2 | Tramo de BI (en miles de millones de euros*) = 1 < BI ≤ 30 | Coeficientes marginales de BI (αi) = 15 %
Fila 3: Categoría = 3 | Tramo de BI (en miles de millones de euros*) = > 30 | Coeficientes marginales de BI (αi) = 18 %
[FIN TABLA ric::tabla014]
(*) Se calculará el importe equivalente en pesos al T.C. vendedor del BNA al cie-
rre de las operaciones del último día hábil del mes anterior del que se trate.
Es decir, para un BI = 35.000 m EUR, el BIC = (1 x 12%) + (30-1) x 15% + (35-30) x 18% = 5.370 m EUR.
BI: VA (ILDC + SC + FC + RM ).
Prom Prom Prom Prom
La partida correspondiente al BIC, se informará por el importe calculado en
función de los coeficientes marginales que corresponda.
VA: Valor absoluto.
ILDC : Componente de intereses, arrendamientos y dividendos.
Prom
SC : Componente de servicios.
Prom
FC : Componente financiero.
Prom
RM : Resultado monetario total.
Prom
En las partidas correspondientes a cada componente, se informarán los
importes que surjan de realizar los cálculos para su determinación.
Cada término dentro de los 3 componentes y el resultado monetario debe
ser informado, respecto d
- entidades de la unidad:
  - `e1` Operacion: Cálculo de exigencia de capital por riesgo operacional — Determinación mensual de la exigencia de capital por riesgo operacional (CRO) mediante la fórmula CRO = BIC x ILM, donde BIC es el componente del indicador de negocio e ILM es el multiplicador de pérd
  - `e2` Definicion: CRO — exigencia de capital por riesgo operacional — Exigencia de capital por riesgo operacional.
  - `e3` Definicion: ILM — multiplicador de pérdida interna — Multiplicador de pérdida interna igual a 1.
  - `e4` Definicion: BIC — componente del indicador de negocio — Componente del indicador de negocio calculado como la sumatoria de BI multiplicado por el coeficiente marginal α correspondiente al tramo.
  - `e5` Definicion: BI — indicador de negocio — Valor absoluto de la suma de los componentes: intereses, arrendamientos y dividendos (ILDC), servicios (SC), financiero (FC) y resultado monetario total (RM), todos en promedio.
  - `e6` Definicion: VA — valor absoluto — Valor absoluto.
  - `e7` Definicion: ILDC — componente de intereses, arrendamientos y dividendos — Componente de intereses, arrendamientos y dividendos.
  - `e8` Definicion: SC — componente de servicios — Componente de servicios.
  - `e9` Definicion: FC — componente financiero — Componente financiero.
  - `e10` Definicion: RM — resultado monetario total — Resultado monetario total.
  - `e11` Obligacion: Información de BIC por coeficientes marginales — Obligación de informar la partida correspondiente al BIC por el importe calculado en función de los coeficientes marginales que corresponda según el tramo del BI.
  - `e12` Obligacion: Información de componentes por período de 12 meses — Obligación de informar en las partidas correspondientes a cada componente (ILDC, SC, FC, RM) los importes que surjan de realizar los cálculos para su determinación.
  - `e13` Obligacion: Información de términos reexpresados por inflación — Obligación de informar cada término dentro de los 3 componentes y el resultado monetario respecto de cada uno de los 3 períodos de 12 meses, reexpresados por inflación.
  - `e14` Condicion: Reexpresión de resultados desde mes de origen — Cuando los términos se refieren a resultados, la reexpresión por inflación operará desde el mes de origen de cada concepto hasta el cierre del período de cálculo de los 36 meses.
  - `e15` Condicion: Reexpresión de activos que generan intereses — Para los activos que generan intereses, será el importe que surja de reexpresar los saldos al cierre de cada uno de los 3 períodos de 12 meses, desde esa fecha hasta el cierre del período de cálculo d
  - `e16` Obligacion: Determinación de partidas netas por período consecutivo — Obligación de determinar primero el valor de las partidas netas que correspondan (ingresos menos egresos) para cada período de 12 meses consecutivos y, después, calcular el promedio de los 3 períodos.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 236** Condicion `e15`: Reexpresión de activos que generan intereses | descripcion: Para los activos que generan intereses, será el importe que surja de reexpresar los saldos al cierre de cada uno de los 3 períodos de 12 meses, desde esa fecha hasta el cierre del período de cálculo de los 36 meses. | tramo: En cuanto a los activos que generan intereses, será el importe que surja de reexpresar los saldos al cierre de cada uno de los 3 períodos de 12 meses, desde esa fecha hasta el cierre del período de cálculo de los 36 meses (n-1).
  - **caso 237** Condicion `e14`: Reexpresión de resultados desde mes de origen | descripcion: Cuando los términos se refieren a resultados, la reexpresión por inflación operará desde el mes de origen de cada concepto hasta el cierre del período de cálculo de los 36 meses. | tramo: Cuando estos términos se refieren a resultados, la reexpresión operará desde el mes de origen de cada concepto hasta el cierre del período de cálculo de los 36 meses (es decir, n-1).

## Unidad `cla::6.5.3.5` (item)
- herencia: [intro 6.5] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudor | **[abre la lista]** [intro 6.5.3] El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender
normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos,
esos problemas pueden resultar en una pérdida para la entidad financiera.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- texto propio: 6.5.3.5. Cuente con refinanciaciones reiteradas y sistemáticas del capital adeudado vin-
culadas a una insuficiente capacidad para su pago aun cuando abone los intere-
ses y siempre que no haya quitas en el capital, que no se reduzcan las tasas de
interés pactadas –salvo que ello derive de las condiciones del mercado– o que
no sea necesario aceptar bienes en pago de parte de las obligaciones.
Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos
superiores a 31 días, del 5 % de las obligaciones refinanciadas y la totalidad de
los intereses devengados, con más el porcentaje acumulado que pudiera co-
rresponder si la refinanciación se hubiera otorgado de haberse encontrado el
deudor en categorías inferiores, podrá reclasificárselo en niveles superiores (“en
observación” o “en situación normal”) si, además, se observan las otras condi-
ciones previstas en la correspondiente categoría.
El deudor que, encontrándose clasificado en esta categoría, haya refinanciado
su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo
precedente– y recibido crédito adicional en los términos a que se refiere el punto
2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad”, y
en la medida en que dicha financiación adicional no hubiese sido cancelada, de-
berá permanecer en esta categoría por lo menos 180 días contados desde la fe-
cha en que se otorgó crédito adicional o desde que se celebró el acuerdo de re-
financiación, la circunstancia más reciente. Ello, salvo que por aplicación de
otras pautas corresponda categorizarlo en el nivel inferior.
- entidades de la unidad:
  - `e1` Condicion: Refinanciaciones reiteradas y sistemáticas del capital — El cliente cuenta con refinanciaciones reiteradas y sistemáticas del capital adeudado vinculadas a insuficiente capacidad para su pago, aun cuando abone los intereses, sin quitas en capital, sin reduc
  - `e2` Condicion: Pago del 5% de obligaciones refinanciadas sin atrasos superiores a 31 días — Se ha pagado sin atrasos superiores a 31 días al menos el 5% de las obligaciones refinanciadas y la totalidad de los intereses devengados, más el porcentaje acumulado que correspondería si la refinanc
  - `e3` Potestad: Reclasificación a niveles superiores si se cumplen condiciones — La entidad podrá reclasificar al deudor en niveles superiores (en observación o en situación normal) si se observan las otras condiciones previstas en la correspondiente categoría
  - `e4` Obligacion: Permanencia mínima 180 días en categoría con refinanciación y crédito adicional — El deudor clasificado en esta categoría que haya refinanciado su deuda y recibido crédito adicional, mientras dicha financiación adicional no haya sido cancelada, debe permanecer en esta categoría por
  - `e5` Excepcion: Excepción a permanencia mínima 180 días por categorización inferior — No aplica la permanencia mínima de 180 días si por aplicación de otras pautas corresponde categorizar al deudor en el nivel inferior
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e3; e5 exceptua_obligacion e4
- NODOS A CLASIFICAR:
  - **caso 238** Condicion `e1`: Refinanciaciones reiteradas y sistemáticas del capital | descripcion: El cliente cuenta con refinanciaciones reiteradas y sistemáticas del capital adeudado vinculadas a insuficiente capacidad para su pago, aun cuando abone los intereses, sin quitas en capital, sin reducción de tasas pactadas (salvo por condiciones de mercado) ni aceptación de bienes en pago | tramo: Cuente con refinanciaciones reiteradas y sistemáticas del capital adeudado vinculadas a una insuficiente capacidad para su pago aun cuando abone los intereses y siempre que no haya quitas en el capital, que no se reduzcan las tasas de interés pactadas –salvo que ello derive de las condiciones del mercado– o que no sea necesario aceptar bienes en pago de parte de las obligaciones

## Unidad `ric::9.1.3` (punto_no_item)
- herencia: [encabezado 9.1] 9.1. Normas de procedimiento
- texto propio: 9.1.3. Limitación al crecimiento de pasivos
Cuando se presenten ambas o alguna de las siguientes situaciones:
- Obligatoriedad de presentación del Plan de Regularización y Saneamiento en capitales
mínimos.
- La suma de incrementos de exigencia de capitales mínimos por riesgo de crédito resul-
tantes de los incumplimientos en las relaciones técnicas de activos inmovilizados y/o
crediticias, supere el 5 % de dicha exigencia (código 70100000).
No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el
incumplimiento, teniendo en cuenta el importe registrado en el código 310000 del Balan-
ce de Saldos.
Se admitirá únicamente el crecimiento originado por el devengamiento de intereses.
En los casos de regulaciones sobre base consolidada, se asimilarán las partidas a la
posición individual.
Dicho límite se observará mientras persista alguna de las situaciones previstas.
- entidades de la unidad:
  - `c1` Condicion: Obligatoriedad Plan Regularización Capitales Mínimos — Se verifica cuando existe obligatoriedad de presentación del Plan de Regularización y Saneamiento en capitales mínimos
  - `c2` Condicion: Incrementos exigencia capitales superen 5 % — La suma de incrementos de exigencia de capitales mínimos por riesgo de crédito resultantes de incumplimientos en relaciones técnicas de activos inmovilizados y/o crediticias supera el 5 % de dicha exi
  - `r1` Restriccion: Tope depósitos nivel mes incumplimiento — No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento, considerando el importe registrado en el código 310000 del Balance de Saldos
  - `e1` Excepcion: Excepción crecimiento por devengamiento intereses — Se exceptúa del límite de depósitos el crecimiento originado por el devengamiento de intereses
  - `c3` Condicion: Regulaciones base consolidada asimilación partidas — Cuando se aplican regulaciones sobre base consolidada, las partidas se asimilarán a la posición individual
  - `c4` Condicion: Persistencia situaciones incumplimiento — El límite de depósitos se observará mientras persista alguna de las situaciones previstas (obligatoriedad del Plan o incrementos de exigencia superiores al 5 %)
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de r1; c2 condicion_de r1; e1 exceptua r1; c4 condicion_de r1
- NODOS A CLASIFICAR:
  - **caso 239** Condicion `c3`: Regulaciones base consolidada asimilación partidas | descripcion: Cuando se aplican regulaciones sobre base consolidada, las partidas se asimilarán a la posición individual | tramo: En los casos de regulaciones sobre base consolidada, se asimilarán las partidas a la posición individual

## Unidad `cap::2.12.13` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca | [intro 2.12] Concepto Ponderador | [intro 2.12] –en %–
- texto propio: 2.12.13. Operaciones DvP fallidas y no DvP. Deberá tenerse en cuenta lo previsto
en el punto 4.1.
- entidades de la unidad:
  - `e1` Operacion: Operaciones DvP fallidas — Operaciones de entrega contra pago (DvP) que no se completan exitosamente
  - `e2` Operacion: Operaciones no DvP — Operaciones que no son de entrega contra pago
  - `e3` Condicion: Remisión a punto 4.1 — El tratamiento de estas operaciones se rige por lo establecido en el punto 4.1
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 240** Condicion `e3`: Remisión a punto 4.1 | descripcion: El tratamiento de estas operaciones se rige por lo establecido en el punto 4.1 | tramo: Deberá tenerse en cuenta lo previsto en el punto 4.1

## Unidad `cap::3.1.2.2` (punto_no_item)
- herencia: [intro 3.1] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi-
cional o sintética, o a una estructura con similares características.
La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con-
ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de
deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset-
Backed Securities”, ABS) y bonos de tit | [encabezado 3.1.2] 3.1.2. Entidad financiera originante.
- texto propio: 3.1.2.2. Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir
las exposiciones objeto de una titulización tradicional sólo si se satisface la
totalidad de los siguientes requisitos operativos –debiendo computar exigencia
de capital por las posiciones de titulización que conserve–:
i) Se ha transferido a uno o más terceros el riesgo de crédito asociado a las
exposiciones titulizadas.
ii) La entidad cedente no mantiene un control directo ni indirecto (como ser a
través de una sociedad controlada) sobre las exposiciones transferidas. Ellas
han sido aisladas de la cedente a los efectos jurídicos de forma tal que están
fuera de su alcance y del de sus acreedores, incluso en los casos de liquida-
ción o quiebra. Estas condiciones deberán estar avaladas por dictamen jurí-
dico.
Se considera que la cedente mantiene el control efectivo de las exposiciones
transferidas si:
a) puede recomprarlas con el objeto de realizar sus beneficios, o
b) está obligada a conservar su riesgo.
El mantenimiento por parte de la cedente de la administración de las exposi-
ciones subyacentes no implicará un control indirecto sobre ellas.
iii) Los títulos valores emitidos no son obligaciones de la cedente. En conse-
cuencia, los inversores que compren los títulos valores sólo deberán tener
derechos frente al conjunto subyacente de exposiciones.
iv)La cesión se ha efectuado a un “Ente de Propósito Especial” (SPE) y los in-
versores pueden gravar o enajenar sus títulos valores sin restricción.
v) Las opciones de exclusión satisfacen las condiciones estipuladas en el punto
3.1.4.
vi)La titulización no contiene cláusulas mediante las cuales:
a) se obligue a la originante a alterar las exposiciones subyacentes con el ob-
jeto de mejorar su calidad crediticia, a menos que esto 
- entidades de la unidad:
  - `e1` Operacion: Exclusión de exposiciones titulizadas tradicionales — La entidad originante puede excluir las exposiciones objeto de una titulización tradicional del cálculo de activos ponderados por riesgo, siempre que se satisfaga la totalidad de los requisitos operat
  - `e2` Condicion: Transferencia de riesgo de crédito a terceros — Se ha transferido a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas.
  - `e3` Condicion: Aislamiento de exposiciones transferidas — La entidad cedente no mantiene control directo ni indirecto sobre las exposiciones transferidas, y éstas han sido aisladas jurídicamente de forma tal que están fuera del alcance de la cedente y de sus
  - `e4` Excepcion: Excepción: administración de exposiciones no implica control — El mantenimiento por parte de la cedente de la administración de las exposiciones subyacentes no implicará un control indirecto sobre ellas, exceptuando así el requisito de ausencia de control indirec
  - `e5` Condicion: Títulos valores no son obligaciones de la cedente — Los títulos valores emitidos no son obligaciones de la cedente, de modo que los inversores que compren los títulos valores sólo tienen derechos frente al conjunto subyacente de exposiciones.
  - `e6` Condicion: Cesión a Ente de Propósito Especial — La cesión se ha efectuado a un Ente de Propósito Especial (SPE) y los inversores pueden gravar o enajenar sus títulos valores sin restricción.
  - `e7` Condicion: Opciones de exclusión conforme punto 3.1.4 — Las opciones de exclusión satisfacen las condiciones estipuladas en el punto 3.1.4.
  - `e8` Restriccion: Prohibición: alteración de exposiciones para mejorar calidad crediticia — La titulización no contiene cláusulas mediante las cuales se obligue a la originante a alterar las exposiciones subyacentes con el objeto de mejorar su calidad crediticia, salvo que esto se logre medi
  - `e9` Restriccion: Prohibición: incremento de posición a primera pérdida — La titulización no contiene cláusulas mediante las cuales la entidad financiera deba incrementar su posición a primera pérdida o aumentar las mejoras crediticias provistas con posterioridad al inicio 
  - `e10` Restriccion: Prohibición: aumento de rendimiento por deterioro crediticio — La titulización no contiene cláusulas mediante las cuales se aumente el rendimiento pagadero a las partes distintas de la originante (inversores o terceros proveedores de mejoras crediticias) en respu
  - `e11` Restriccion: Prohibición: opciones de rescisión y eventos desencadenantes — La titulización no incluye opciones de rescisión o eventos desencadenantes de la extinción del contrato, salvo opciones de exclusión admitidas (punto 3.1.4.) o extinción por cambios impositivos o regu
  - `e12` Condicion: Requisito: ausencia de cláusulas prohibidas — La titulización no contiene cláusulas que obliguen a alterar exposiciones para mejorar calidad crediticia (salvo venta a terceros), que obliguen a incrementar posición a primera pérdida o mejoras cred
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1; e3 condicion_de e1; e4 exceptua e3; e5 condicion_de e1; e6 condicion_de e1; e7 condicion_de e1; e8 condicion_de e1; e9 condicion_de e1; e10 condicion_de e1; e11 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 241** Condicion `e12`: Requisito: ausencia de cláusulas prohibidas | descripcion: La titulización no contiene cláusulas que obliguen a alterar exposiciones para mejorar calidad crediticia (salvo venta a terceros), que obliguen a incrementar posición a primera pérdida o mejoras crediticias post-inicio, o que aumenten rendimiento en respuesta a deterioro crediticio. | tramo: La titulización no contiene cláusulas mediante las cuales: a) se obligue a la originante a alterar las exposiciones subyacentes con el objeto de mejorar su calidad crediticia, a menos que esto se logre mediante su venta –a precios de mercado– a terceros no vinculados a ésta; b) la entidad financiera deba incrementar su posición a primera pérdida –es decir, su exposición al tramo que absorbe las pérdidas en primer término– o aumentar las mejoras crediticias provistas, con posterioridad al inicio de la operación; o c) se aumente el rendimiento pagadero a las partes distintas de la originante, como pueden ser los inversores o terceros proveedores de mejoras crediticias, en respuesta a un deterioro de la calidad crediticia de las exposiciones subyacentes

## Unidad `cap::3.1.14.4` (punto_no_item)
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
- texto propio: 3.1.14.4. Criterios adicionales.
i) Riesgo de crédito de las exposiciones subyacentes.
A la fecha de corte, teniendo en cuenta las técnicas de cobertura del ries-
go crediticio, las exposiciones subyacentes deberán cumplir con las con-
diciones para recibir un ponderador de riesgo igual o inferior a:
- 40 % para el promedio ponderado por el valor de las exposiciones de
la cartera, en el caso de préstamos garantizados con hipotecas sobre
inmuebles residenciales;
- 50 % para cada una de las exposiciones individuales garantizadas con
hipotecas sobre inmuebles comerciales;
- 75 % para cada una de las exposiciones individuales de la cartera mi-
norista; o
- 100 % para cada una de las exposiciones individuales de cualquier
otro tipo.
ii) Atomización de la cartera.
A la fecha de corte, el monto total de las exposiciones a un deudor en par-
ticular no deberá exceder el 1 % del valor agregado del saldo de todas las
exposiciones incluidas en la cartera.
- entidades de la unidad:
  - `c1` Condicion: Riesgo de crédito exposiciones subyacentes — Las exposiciones subyacentes, considerando técnicas de cobertura del riesgo crediticio, deben cumplir con condiciones para recibir un ponderador de riesgo igual o inferior a los umbrales especificados
  - `r1` Restriccion: Límite concentración deudor individual — El monto total de las exposiciones a un deudor en particular no podrá exceder el 1 % del valor agregado del saldo de todas las exposiciones incluidas en la cartera.
  - `c2` Condicion: Fecha de corte para verificación — Las verificaciones de cumplimiento de los criterios se realizan a la fecha de corte.
- relaciones del crudo (sin establecida_en ni de sujeto): c2 condicion_de c1; c2 condicion_de r1
- NODOS A CLASIFICAR:
  - **caso 243** Condicion `c1`: Riesgo de crédito exposiciones subyacentes | descripcion: Las exposiciones subyacentes, considerando técnicas de cobertura del riesgo crediticio, deben cumplir con condiciones para recibir un ponderador de riesgo igual o inferior a los umbrales especificados según el tipo de exposición. | tramo: teniendo en cuenta las técnicas de cobertura del riesgo crediticio, las exposiciones subyacentes deberán cumplir con las condiciones para recibir un ponderador de riesgo igual o inferior a

## Unidad `ext::7.6.3::intro` (intro)
- herencia: [encabezado 7.6.3] 7.6.3. Deudor moroso.
- texto propio: Cuando el exportador mantenga acciones judiciales contra el importador, u otro
obligado a efectuar el pago, acreditándolo con copia del escrito de iniciación de
demanda certificada por el juzgado interviniente en cuanto a su fecha de inicio y
radicación.
La documentación deberá estar legalizada por autoridad consular o conforme a lo
previsto por el Convenio de la Haya del 5 de octubre de 1961, cuando resultase
aplicable.
También se podrán incluir casos en esta categoría, sin necesidad de que el exportador
haya iniciado y mantenga acciones legales, cuando se verifique alguna de las
siguientes situaciones:
- entidades de la unidad:
  - `e1` Condicion: Exportador mantiene acciones judiciales — El exportador mantiene acciones judiciales contra el importador u otro obligado a efectuar el pago
  - `e2` Obligacion: Acreditar con copia de escrito de demanda — Acreditar con copia del escrito de iniciación de demanda certificada por el juzgado interviniente en cuanto a su fecha de inicio y radicación
  - `e3` Obligacion: Legalizar documentación por autoridad consular — La documentación deberá estar legalizada por autoridad consular o conforme a lo previsto por el Convenio de la Haya del 5 de octubre de 1961, cuando resultase aplicable
  - `e4` Definicion: Deudor moroso — acciones judiciales — Se entiende por deudor moroso el caso en que el exportador mantenga acciones judiciales contra el importador u otro obligado a efectuar el pago, acreditándolo con copia del escrito de iniciación de de
  - `e5` Condicion: Se verifique alguna de las siguientes situaciones — Cuando se verifique alguna de las siguientes situaciones, sin necesidad de que el exportador haya iniciado y mantenga acciones legales
- relaciones del crudo (sin establecida_en ni de sujeto): e1 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 244** Condicion `e5`: Se verifique alguna de las siguientes situaciones | descripcion: Cuando se verifique alguna de las siguientes situaciones, sin necesidad de que el exportador haya iniciado y mantenga acciones legales | tramo: cuando se verifique alguna de las siguientes situaciones

## Unidad `cap::7.1.2` (punto_no_item)
- herencia: [chapeau_seccion S7] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en grupo 1 y grupo 2, conforme a lo previsto en la Sección 2. | [intro 7.1] Se determinará mensualmente por la siguiente expresión: | [intro 7.1] C = BIC x ILM | [intro 7.1] RO | [intro 7.1] Donde:
C : exigencia de capital por riesgo operacional. | [intro 7.1] RO | [intro 7.1] BIC: componente del indicador de negocio, que es el producto del indicador de negocio (BI) | [intro 7.1] por una serie de coeficientes marginales (α), calculado según lo previsto en el punto | [intro 7.1] i | [intro 7.1] 7.1.2. | [intro 7.1] ILM: multiplicador de pérdida interna igual a 1.
Los activos ponderados por riesgo (APR) para el riesgo operacional son iguales a 12,5 veces el
C . | [intro 7.1] RO
- texto propio: 7.1.2. Componente del indicador de negocio (BIC).
Se determinará por la siguiente expresión:
BIC = ∑ BI x α
i i
donde los coeficientes marginales (α) se determinarán en función del tramo del BI:
i
[TABLA cap::tabla038 | página 150 | e0_tablas | columnas]
Columnas: Categoría | Tramo de BI (en miles de millones de euros*) | Coeficientes marginales de BI (α) i
Fila 1: Categoría = 1 | Tramo de BI (en miles de millones de euros*) = ≤ 1 | Coeficientes marginales de BI (α) i = 12%
Fila 2: Categoría = 2 | Tramo de BI (en miles de millones de euros*) = 1 < BI ≤ 30 | Coeficientes marginales de BI (α) i = 15%
Fila 3: Categoría = 3 | Tramo de BI (en miles de millones de euros*) = >30 | Coeficientes marginales de BI (α) i = 18%
[FIN TABLA cap::tabla038]
* En línea con los estándares internacionales. Deberá calcularse el importe equivalente
en pesos al tipo de cambio vendedor del Banco de la Nación Argentina al cierre de las
operaciones del último día hábil del mes anterior del que se trate.
Los coeficientes marginales aumentan conforme se incrementa el tamaño del BI. Para las
entidades incluidas en la categoría 1 (BI igual o inferior al equivalente en pesos de
€1.000 millones), el BIC equivale al BI x 12%. El incremento marginal del BIC derivado
del aumento de una unidad del BI es del 12% en la categoría 1, del 15% en la categoría 2
y del 18% en la categoría 3.
- entidades de la unidad:
  - `e1` Operacion: Cálculo de BIC por tramos de BI — Cálculo del componente del indicador de negocio (BIC) como suma del producto del indicador de negocio (BI) por coeficientes marginales (α) según el tramo de BI: categoría 1 (BI ≤ €1.000 millones equiv
  - `e2` Obligacion: Conversión de BI a pesos — tipo de cambio vendedor BNA — Deberá calcularse el importe equivalente en pesos al tipo de cambio vendedor del Banco de la Nación Argentina al cierre de las operaciones del último día hábil del mes anterior del que se trate, para 
  - `e3` Definicion: Coeficientes marginales (α) — categoría 1 — En la categoría 1 (BI igual o inferior al equivalente en pesos de €1.000 millones), el coeficiente marginal es 12%, de modo que BIC = BI x 12%.
  - `e4` Definicion: Incremento marginal de BIC — categoría 1 — El incremento marginal del BIC derivado del aumento de una unidad del BI es del 12% en la categoría 1.
  - `e5` Definicion: Incremento marginal de BIC — categoría 2 — El incremento marginal del BIC derivado del aumento de una unidad del BI es del 15% en la categoría 2.
  - `e6` Definicion: Incremento marginal de BIC — categoría 3 — El incremento marginal del BIC derivado del aumento de una unidad del BI es del 18% en la categoría 3.
  - `e7` Condicion: Tramo de BI ≤ €1.000 millones equivalente en pesos — El BI es igual o inferior al equivalente en pesos de €1.000 millones (categoría 1).
  - `e8` Condicion: Tramo de BI entre €1.000 y €30.000 millones equivalente en pesos — El BI es superior a €1.000 millones e igual o inferior a €30.000 millones equivalente en pesos (categoría 2).
  - `e9` Condicion: Tramo de BI > €30.000 millones equivalente en pesos — El BI es superior a €30.000 millones equivalente en pesos (categoría 3).
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 249** Condicion `e7`: Tramo de BI ≤ €1.000 millones equivalente en pesos | descripcion: El BI es igual o inferior al equivalente en pesos de €1.000 millones (categoría 1). | tramo: BI igual o inferior al equivalente en pesos de €1.000 millones
  - **caso 250** Condicion `e9`: Tramo de BI > €30.000 millones equivalente en pesos | descripcion: El BI es superior a €30.000 millones equivalente en pesos (categoría 3). | tramo: >30
  - **caso 251** Condicion `e8`: Tramo de BI entre €1.000 y €30.000 millones equivalente en pesos | descripcion: El BI es superior a €1.000 millones e igual o inferior a €30.000 millones equivalente en pesos (categoría 2). | tramo: 1 < BI ≤ 30

## Unidad `ext::8.4.2` (punto_no_item)
- herencia: [encabezado 8.4] 8.4. Responsabilidades de la entidad nominada para el seguimiento del permiso.
- texto propio: 8.4.2. Determinación del plazo para el ingreso y liquidación de las divisas.
La entidad deberá determinar el plazo aplicable a cada exportación a partir de lo
dispuesto en el punto 7.1.1.
En el caso de que una exportación esté compuesta por distintos productos, el plazo
aplicable será aquel que representa una mayor proporción del valor FOB total de la
exportación.
La fecha de vencimiento que le corresponde a una exportación será aquella resultante
de sumar el plazo aplicable a la fecha de cumplido de embarque otorgada por la
Aduana. Si la fecha resultante fuese un día no hábil, el vencimiento se trasladará al
primer día hábil siguiente.
En caso de que exista una ampliación del plazo para un producto, el nuevo plazo se
aplicará tanto a las exportaciones embarcadas a partir de la vigencia de la ampliación
como a las embarcadas previamente cuyo plazo para ingresar y liquidar no se
encontrase vencido a ese momento. En tanto en caso de existir una reducción del
plazo vigente, el plazo reducido sólo regirá para las operaciones que se oficialicen a
partir de la vigencia del nuevo plazo.
- entidades de la unidad:
  - `e1` Operacion: Determinación del plazo para ingreso y liquidación — Determinación del plazo aplicable a cada exportación a partir de lo dispuesto en el punto 7.1.1.
  - `e2` Operacion: Aplicación del plazo en exportaciones multiproducto — En exportaciones compuestas por distintos productos, el plazo aplicable es aquel que representa una mayor proporción del valor FOB total de la exportación.
  - `e3` Operacion: Cálculo de fecha de vencimiento — La fecha de vencimiento es la resultante de sumar el plazo aplicable a la fecha de cumplido de embarque otorgada por la Aduana.
  - `e4` Condicion: Traslado de vencimiento a día hábil siguiente — Si la fecha de vencimiento resultante es un día no hábil, el vencimiento se traslada al primer día hábil siguiente.
  - `e5` Operacion: Aplicación de ampliación de plazo a exportaciones — Cuando existe ampliación del plazo para un producto, el nuevo plazo se aplica a exportaciones embarcadas a partir de la vigencia de la ampliación y a las embarcadas previamente cuyo plazo no esté venc
  - `e6` Restriccion: Plazo reducido solo para operaciones posteriores — En caso de reducción del plazo vigente, el plazo reducido solo rige para las operaciones que se oficialicen a partir de la vigencia del nuevo plazo.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 252** Condicion `e4`: Traslado de vencimiento a día hábil siguiente | descripcion: Si la fecha de vencimiento resultante es un día no hábil, el vencimiento se traslada al primer día hábil siguiente. | tramo: Si la fecha resultante fuese un día no hábil, el vencimiento se trasladará al primer día hábil siguiente.

## Unidad `cap::6.2.3.1` (punto_no_item)
- herencia: [intro 6.2] La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu-
los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio-
nes preferidas no convertibles.
Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo
de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de
la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera.
L | [encabezado 6.2.3] 6.2.3. Tratamiento de los derivados de tasas de interés.
- texto propio: 6.2.3.1. El sistema de medición deberá abarcar a todos los derivados de tasas de inte-
rés e instrumentos fuera de balance de la cartera de negociación sensibles a
los cambios en las tasas –tales como los FRAs, futuros sobre bonos, “swaps”
de tasas de interés y de monedas “cross-currency swaps”– y las posiciones de
divisas a término.
Las opciones se tratarán conforme a lo previsto en el punto 6.6.
- entidades de la unidad:
  - `e1` Operacion: Medición de derivados de tasas de interés — Sistema de medición que abarca todos los derivados de tasas de interés e instrumentos fuera de balance de la cartera de negociación sensibles a cambios en tasas, incluyendo FRAs, futuros sobre bonos, 
  - `e2` Obligacion: Abarcar derivados de tasas en sistema de medición — El sistema de medición deberá abarcar a todos los derivados de tasas de interés e instrumentos fuera de balance de la cartera de negociación sensibles a los cambios en las tasas, incluyendo FRAs, futu
  - `e3` Condicion: Tratamiento de opciones conforme punto 6.6 — Las opciones se tratarán conforme a lo previsto en el punto 6.6, lo que implica que su tratamiento está regulado en otra disposición normativa.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 regula e1
- NODOS A CLASIFICAR:
  - **caso 253** Condicion `e3`: Tratamiento de opciones conforme punto 6.6 | descripcion: Las opciones se tratarán conforme a lo previsto en el punto 6.6, lo que implica que su tratamiento está regulado en otra disposición normativa. | tramo: Las opciones se tratarán conforme a lo previsto en el punto 6.6.

## Unidad `ext::10.4.2.5` (item)
- herencia: **[abre la lista]** [intro 10.4.2] La entidad podrá dar acceso al mercado de cambios para el pago al exterior en la
medida que verifique previamente que se cumplen la totalidad de los siguientes
requisitos:
- texto propio: 10.4.2.5. Cuenta con elementos que le permitan avalar la razonabilidad de los
montos a pagar considerando la actividad importadora del cliente en los
últimos años y/o los planes de negocios que le presente el importador.
Adicionalmente, en el caso de que el cliente no sea una persona humana y
se haya constituido hasta 365 (trescientos sesenta y cinco) días corridos
antes de la fecha de acceso al mercado de cambios, para dar curso a
nuevos pagos se requerirá la conformidad previa del BCRA cuando el
monto pendiente de regularización por pagos anticipados de importaciones
sea mayor al equivalente de USD 5 millones (dólares estadounidenses
cinco millones), incluido el monto por el cual se solicita el acceso al
mercado de cambios. En el caso de que el cliente sea una unión transitoria,
se tomará en cuenta la fecha de constitución de la sociedad más antigua
que la conforma.
Para los importadores comprendidos en el párrafo anterior, las entidades
deberán consultar en el apartado “Régimen Informativo SEPAIMPO” del
sitio www3.bcra.gob.ar, si el saldo pendiente de regularización por pagos
anticipados de importaciones del cliente se encuentra comprendido en el
límite previsto.
- entidades de la unidad:
  - `c1` Condicion: Verificación previa de requisitos — La entidad debe verificar previamente que se cumplen la totalidad de los requisitos enumerados, incluido el del punto 10.4.2.5
  - `o1` Obligacion: Contar con elementos para avalar razonabilidad de montos — La entidad debe contar con elementos que le permitan avalar la razonabilidad de los montos a pagar, considerando la actividad importadora del cliente en los últimos años y/o los planes de negocios que
  - `c2` Condicion: Cliente no persona humana constituido hasta 365 días antes — Supuesto en que el cliente no es persona humana y se ha constituido hasta 365 días corridos antes de la fecha de acceso al mercado de cambios
  - `r1` Restriccion: Conformidad previa BCRA para pagos cuando monto pendiente supera USD 5 millones — Se requiere conformidad previa del BCRA para dar curso a nuevos pagos cuando el monto pendiente de regularización por pagos anticipados de importaciones sea mayor al equivalente de USD 5 millones, inc
  - `c3` Condicion: Cliente es unión transitoria — Supuesto en que el cliente es una unión transitoria; en este caso se toma en cuenta la fecha de constitución de la sociedad más antigua que la conforma
  - `o2` Obligacion: Consultar Régimen Informativo SEPAIMPO para verificar saldo pendiente — Las entidades deberán consultar en el apartado 'Régimen Informativo SEPAIMPO' del sitio www3.bcra.gob.ar si el saldo pendiente de regularización por pagos anticipados de importaciones del cliente se e
- relaciones del crudo (sin establecida_en ni de sujeto): c2 condicion_de r1; c3 condicion_de r1
- NODOS A CLASIFICAR:
  - **caso 254** Condicion `c1`: Verificación previa de requisitos | descripcion: La entidad debe verificar previamente que se cumplen la totalidad de los requisitos enumerados, incluido el del punto 10.4.2.5 | tramo: en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos
