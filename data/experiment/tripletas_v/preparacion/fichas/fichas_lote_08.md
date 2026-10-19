# U-TRIP-V: fichas del lote 08 (10)

Acta del sorteo `acta_sorteo_V.json` (sha256 `5d6a237e510bcf086db717061dd146eaa9b3181006cb7b1d300164436c720c55`), sellada a las 2026-10-19T14:23:55-03:00; fichas generadas a las 2026-10-19T14:25:19-03:00. Grafo KG-Tanda0-Desarrollo-r2b-sincola-rs1 (`66e745f5…`). Las fichas van en el orden sellado. Criterio (§3.4 del pre-registro): la evidencia sostiene la relación entre esos dos nodos, con sus sujetos, valores, calificadores y modalidad.

Cada ficha trae los dos nodos (tipo, etiqueta, descripción y propiedades), el predicado y la evidencia de cada procedencia: el texto heredado y el propio de la unidad de E0, el tramo literal de cada extremo en esa unidad si lo hay, las páginas y la ruta del PDF con la página. «literal» dice si el tramo está tal cual en el texto (exacta), por tokens (tokens) o no (no).

## V081 · `aplica_a` · lote_08, 1 de 10

**Origen** — Operacion «Pago de gastos al exterior por operatoria habitual» (`Operacion_pago_de_gastos_al_exterior_por_operatoria_habitual__ext_13_2_2_b49844`)

- descripción: Pago de gastos que las entidades abonan al exterior por su operatoria habitual, comprendido en las situaciones de acceso al mercado de cambios para pagos de servicios de no residentes prestados a partir del 13/12/23
- tipo: pago de servicios

**Predicado** — `aplica_a`

- tramo del sujeto: «las entidades» (literal: exacta)

**Destino** — Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (`Sujeto_rol_entidad_autorizada_exterior`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `ext::13.2.2` · ext · punto 13.2.2 · punto_propio · págs. 169

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=169`

> *heredado (encabezado, S13, p. 168):* Sección 13. Pagos de servicios prestados por no residentes.
>
> *heredado (encabezado, 13.2, p. 169):* 13.2. Pagos de servicios que fueron o serán prestados o devengados a partir del 13/12/23.
>
> *heredado (intro, 13.2, p. 169):* Las entidades podrán dar acceso al mercado de cambios para cursar pagos de servicios de no residentes que fueron o serán prestados a partir del 13/12/23 cuando, adicionalmente a los restantes requisitos normativos aplicables, la operación queda comprendida en algunas de las situaciones que se detallan a continuación:
>
> *propio:* 13.2.2. los gastos que abonen las entidades al exterior por su operatoria habitual.

- tramo del origen: «los gastos que abonen las entidades al exterior por su operatoria habitual» (literal: exacta)
- tramo del destino: —

---

## V082 · `condicion_de` · lote_08, 2 de 10

**Origen** — Condicion «Cumplimiento de condiciones del punto 3.11.3.» (`Condicion_cumplimiento_de_condiciones_del_punto_3_11_3__se_requiere_el_cumplimiento_de_las_7d6a58`)

- descripción: Se requiere el cumplimiento de las condiciones previstas en el punto 3.11.3. para acceder al mercado.

**Predicado** — `condicion_de`

**Destino** — Potestad «Acceso al mercado para compra de moneda extranjera» (`Potestad_acceso_al_mercado_para_compra_de_moneda_extranjera__los_residentes_con_endeudami_275d27`)

- descripción: Los residentes con endeudamientos comprendidos en el punto 7.9.1. y originados a partir del 07/01/21 (únicamente a partir del 08/08/25 en el caso de aquellos comprendidos en el punto 7.9.1.4.) o los fideicomisos constituidos en el país para garantizar la atención de los servicios de capital e intereses de tales endeudamientos, quedan autorizados a acceder al mercado para la compra de moneda extranjera para la constitución de garantías.

**Evidencia 1 de 1** — `ext::7.9.6` · ext · punto 7.9.6 · punto_propio · págs. 99

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=99`

> *heredado (encabezado, S7, p. 80):* Sección 7. Cobros de exportaciones de bienes.
>
> *heredado (encabezado, 7.9, p. 94):* 7.9. Operaciones financieras habilitadas para aplicar cobros de exportaciones de bienes y
>
> *heredado (intro, 7.9, p. 94):* servicios.
>
> *propio:* 7.9.6. Los residentes con endeudamientos comprendidos en el punto 7.9.1. y originados a partir del 07/01/21 (únicamente a partir del 08/08/25 en el caso de aquellos comprendidos en el punto 7.9.1.4.) o los fideicomisos constituidos en el país para garantizar la atención de los servicios de capital e intereses de tales endeudamientos, podrán acceder al mercado, en la medida que se cumplan las condiciones previstas en el punto 3.11.3., para la compra de moneda extranjera para la constitución de las garantías en cuentas en moneda extranjera abiertas en entidades financieras locales o en el exterior -cuando se trate de un endeudamiento financiero comprendido en el punto 3.5.-, por los montos exigibles en los contratos de endeudamiento.

- tramo del origen: «en la medida que se cumplan las condiciones previstas en el punto 3.11.3.» (literal: exacta)
- tramo del destino: «podrán acceder al mercado, en la medida que se cumplan las condiciones previstas en el punto 3.11.3., para la compra de moneda extranjera» (literal: exacta)

---

## V083 · `prohibe` · lote_08, 3 de 10

**Origen** — Restriccion «Prohibición de crear expectativa de recompra/rescate/amortización» (`Restriccion_la_entidad_financiera_debe_abstenerse_de_crear_en_ocasion_de_la_emision_de_la_ac_c0dfe0`)

- descripción: La entidad financiera debe abstenerse de crear, en ocasión de la emisión de la acción, cualquier expectativa de que la acción será recomprada, rescatada o amortizada.
- tipo: prohibicion

**Predicado** — `prohibe`

**Destino** — Operacion «Inclusión de acción en CO» (`Operacion_inclusion_de_accion_en_co__cap_8_3_1_9f00e1`)

- descripción: Inclusión de una acción dentro del Capital ordinario de nivel uno (CO), sujeta a condiciones sobre expectativas de recompra, rescate o amortización.
- tipo: Clasificación de instrumento de capital

**Evidencia 1 de 1** — `cap::8.3.1` · cap · punto 8.3.1 · punto_propio · págs. 156

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=156`

> *heredado (encabezado, S8, p. 154):* Sección 8. Responsabilidad patrimonial computable.
>
> *heredado (encabezado, 8.3, p. 156):* 8.3. Criterios relacionados con los conceptos computables.
>
> *propio:* 8.3.1. Capital ordinario de nivel uno (CO ). n1 Para que una acción sea considerada dentro del CO la entidad financiera se debe n1, abstener de crear, en ocasión de su emisión, cualquier expectativa de que la acción se- rá recomprada, rescatada o amortizada, y los términos contractuales no deberán conte- ner cláusula alguna que pudiera originar tal expectativa.

- tramo del origen: «la entidad financiera se debe abstener de crear, en ocasión de su emisión, cualquier expectativa de que la acción será recomprada, rescatada o amortizada» (literal: no)
- tramo del destino: «una acción sea considerada dentro del CO» (literal: exacta)

---

## V084 · `condicion_de` · lote_08, 4 de 10

**Origen** — Condicion «Exportaciones comprendidas en Decretos 492/23, 549/23, 597/23 y 28/23» (`Condicion_exportaciones_comprendidas_en_decretos_492_23_549_23_597_23_y_28_23__condicion_e_79a748`)

- descripción: Condición: exportaciones de bienes comprendidas en los Decretos 492/23, 549/23, 597/23 y 28/23, donde el cliente demuestra que durante sus vigencias ingresó y liquidó divisas por un monto no menor al porcentaje mínimo requerido del anticipo, prefinanciación o posfinanciación, y la porción no liquidada concretó operaciones de compraventa de títulos valores con liquidación en moneda extranjera en la adquisición y moneda local en la venta.
- umbrales (1):
  - comparacion: minimo_inclusivo; base: porcentaje mínimo requerido del anticipo; tramo: por un monto no menor al porcentaje mínimo requerido del anticipo, prefinanciación o posfinanciación

**Predicado** — `condicion_de`

**Destino** — Potestad «Extensión del plazo para liquidación de divisas — exportaciones Decretos 492/23, 549/23, 597/23 y 28/23» (`Potestad_extension_del_plazo_para_liquidacion_de_divisas_exportaciones_decretos_492_23_54_0e9399`)

- descripción: La entidad encargada del seguimiento del permiso podrá otorgar extensión del plazo para la liquidación de divisas del embarque a exportaciones de bienes comprendidas en los Decretos 492/23, 549/23, 597/23 y 28/23, cuando se cumplan las condiciones de ingreso y liquidación de divisas y operaciones de compraventa de títulos valores.

**Evidencia 1 de 1** — `ext::7.5.2` · ext · punto 7.5.2 · punto_propio · págs. 86, 87

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=86` · `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=87`

> *heredado (encabezado, S7, p. 80):* Sección 7. Cobros de exportaciones de bienes.
>
> *heredado (encabezado, 7.5, p. 86):* 7.5. Ampliaciones del plazo para el ingreso y liquidación de divisas.
>
> *heredado (intro, 7.5, p. 86):* La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias:
>
> *propio:* 7.5.2. Exportaciones financiadas al comprador totalmente prefinanciadas y/o posfinanciadas localmente o desde el exterior. Cuando el monto pendiente de ingreso de las operaciones haya sido prefinanciado en su totalidad y los fondos liquidados en el mercado de cambios en concepto de prefinanciaciones de exportaciones locales y/o del exterior, se podrá extender el plazo para la liquidación de divisas del embarque hasta la fecha de vencimiento de la correspondiente financiación dada al comprador. En tanto si el exportador demuestra haber liquidado en el mercado de cambio, antes del vencimiento del plazo, posfinanciaciones de exportaciones que cubran la totalidad del monto pendiente de ingreso del permiso, sin que se verifiquen las condiciones previstas para los puntos 9.3.4. y 9.3.5. para la emisión de la correspondiente certificación de aplicación, se podrá extender el plazo para la liquidación de divisas del embarque hasta la fecha en que venza el crédito de mayor plazo descontado y/o cedido por el exportador. Esto último también será aplicable cuando el exportador haya prefinanciado parcialmente la operación y demuestre haber liquidado en el mercado de cambio, antes del vencimiento, posfinanciaciones de exportaciones que cubran el resto del monto pendiente de ingreso. Esta extensión del plazo también se podrá otorgar a exportaciones de bienes comprendidas en lo dispuesto por los Decretos 492/23, 549/23, 597/23 y 28/23, en la medida que el cliente demuestre que, durante sus respectivas vigencias y en las condiciones estipuladas en los mencionados decretos, ingresó y liquidó divisas en el mercado de cambios por un monto no menor al porcentaje mínimo requerido del anticipo, prefinanciación o posfinanciación y la porción no liquidada concretó operaciones de compraventa con títulos valores, en las cuales los títulos valores son adquiridos con liquidación en moneda extranjera y vendidos con liquidación en moneda local en el país. En el caso de que la adquisición de títulos valores se haya concretado con liquidación en el país de la moneda extranjera se deberá contar con la certificación de la entidad que cursó la operación de canje y/o arbitraje por el ingreso de las divisas a través del mercado de cambios.

- tramo del origen: «Esta extensión del plazo también se podrá otorgar a exportaciones de bienes comprendidas en lo dispuesto por los Decretos 492/23, 549/23, 597/23 y 28/23, en la medida que el cliente demuestre que, durante sus respectivas vigencias y en las condiciones estipuladas en los mencionados decretos, ingresó y liquidó divisas en el mercado de cambios por un monto no menor al porcentaje mínimo requerido del anticipo, prefinanciación o posfinanciación y la porción no liquidada concretó operaciones de compraventa con títulos valores, en las cuales los títulos valores son adquiridos con liquidación en moneda extranjera y vendidos con liquidación en moneda local en el país» (literal: exacta)
- tramo del destino: «Esta extensión del plazo también se podrá otorgar a exportaciones de bienes comprendidas en lo dispuesto por los Decretos 492/23, 549/23, 597/23 y 28/23» (literal: exacta)

---

## V085 · `condicion_de` · lote_08, 5 de 10

**Origen** — Condicion «Verificación de requisitos normativos en punto 10.3.2.1» (`Condicion_verificacion_de_requisitos_normativos_en_punto_10_3_2_1__a_la_fecha_de_emision_d_e78f56`)

- descripción: A la fecha de emisión de la certificación, deben verificarse todos los requisitos normativos previstos en el punto 10.3.2.1.

**Predicado** — `condicion_de`

**Destino** — Obligacion «Emitir certificación a solicitud del importador» (`Obligacion_la_entidad_debe_emitir_la_certificacion_que_habilita_el_acceso_del_importador_al_bbfca9`)

- descripción: La entidad debe emitir la certificación que habilita el acceso del importador al mercado de cambios para realizar un pago con imputación del despacho de importación bajo seguimiento de la entidad, por cualquier entidad que opere en comercio exterior, a solicitud del importador.
- tipo: asignacion

**Evidencia 1 de 1** — `ext::11.1.3::intro` · ext · punto 11.1.3 · bloque_intro · págs. 162

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=162`

> *heredado (encabezado, S11, p. 160):* Sección 11. Sistema de seguimiento de pagos de importaciones (SEPAIMPO).
>
> *heredado (encabezado, 11.1, p. 160):* 11.1. Seguimiento de oficializaciones de importación.
>
> *heredado (encabezado, 11.1.3, p. 162):* 11.1.3. Certificación para el acceso al mercado de cambios para el pago de importaciones de
>
> *propio:* bienes con registro de ingreso aduanero. A solicitud del importador, la entidad procederá a emitir la certificación que habilita el acceso del importador al mercado de cambios para realizar un pago con imputación del despacho de importación bajo seguimiento de la entidad, por cualquier entidad que opere en comercio exterior. La emisión de una certificación por parte de la entidad implica que, a la fecha de su emisión, se verifican todos los requisitos normativos previstos en el punto 10.3.2.1. En la certificación que emita la entidad para habilitar el acceso al mercado de cambios deberá constar al menos la siguiente información:

- tramo del origen: «a la fecha de su emisión, se verifican todos los requisitos normativos previstos en el punto 10.3.2.1» (literal: exacta)
- tramo del destino: «A solicitud del importador, la entidad procederá a emitir la certificación que habilita el acceso del importador al mercado de cambios para realizar un pago con imputación del despacho de importación bajo seguimiento de la entidad, por cualquier entidad que opere en comercio exterior.» (literal: exacta)

---

## V086 · `aplica_a` · lote_08, 6 de 10

**Origen** — Obligacion «Procedimientos internos para prevenir uso indebido de información» (`Obligacion_existencia_de_procedimientos_internos_destinados_a_prevenir_el_uso_indebido_de_i_8c57d6`)

- descripción: Existencia de procedimientos internos destinados a prevenir el uso indebido de información confidencial para contribuir a la credibilidad de una ECAI
- tipo: otra

**Predicado** — `aplica_a`

- tramo del sujeto: «una ECAI» (literal: exacta)

**Destino** — Sujeto «Agentes de calificación externa (ECAI)» (`Sujeto_ecai`)

- descripción: —
- nivel: clase
- alias: ["ECAI"]

**Evidencia 1 de 1** — `cap::10.2.2.6` · cap · punto 10.2.2.6 · punto_propio · págs. 173

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=173`

> *heredado (encabezado, S10, p. 172):* Sección 10. Agentes de calificación externa (ECAI).
>
> *heredado (encabezado, 10.2, p. 172):* 10.2. Criterios de elegibilidad.
>
> *heredado (encabezado, 10.2.2, p. 172):* 10.2.2. Condiciones.
>
> *heredado (intro, 10.2.2, p. 172):* Las ECAI deberán cumplir cada uno de los siguientes seis criterios:
>
> *propio:* 10.2.2.6. Credibilidad. Las evaluaciones de crédito de las ECAI deben ser confiables para terceros independientes. Además, la existencia de procedimientos internos destina- dos a prevenir el uso indebido de información confidencial contribuye a la credibilidad de una ECAI. Para ser reconocida, no es requisito que una ECAI evalúe empresas en más de un país.

- tramo del origen: «la existencia de procedimientos internos destinados a prevenir el uso indebido de información confidencial contribuye a la credibilidad de una ECAI» (literal: exacta)
- tramo del destino: —

---

## V087 · `aplica_a` · lote_08, 7 de 10

**Origen** — Obligacion «Aplicación de disposiciones de Sección 5 por incumplimiento» (`Obligacion_a_los_sujetos_obligados_les_resultaran_de_aplicacion_las_disposiciones_de_la_sec_0054f1`)

- descripción: A los sujetos obligados les resultarán de aplicación las disposiciones de la Sección 5 en caso de incumplimiento de estas normas.
- tipo: otra
- umbrales (1):
  - comparacion: no_determinada; tramo: en caso de incumplimiento de estas normas

**Predicado** — `aplica_a`

- tramo del sujeto: «los sujetos obligados» (literal: exacta)

**Destino** — Sujeto «Sujetos obligados (Protección de usuarios)» (`Sujeto_rol_sujeto_obligado_proteccion`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `pro::1.2` · pro · punto 1.2 · punto_propio · págs. 4

- PDF: `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=4`

> *heredado (encabezado, S1, p. 3):* Sección 1. Disposiciones generales.
>
> *propio:* 1.2. Criterio general y supervisión. Los sujetos obligados deberán considerar y resolver fundadamente, contemplando los dere- chos básicos enunciados en la Sección 2. y las normas aplicables a la operatoria involucrada, los reclamos que, relacionados con los servicios que ofrecen y/o prestan, les planteen los usua- rios de tales servicios. El Banco Central de la República Argentina (BCRA) supervisará la actuación de los sujetos obligados, a quienes les resultarán de aplicación las disposiciones de la Sección 5. en caso de incumplimiento de estas normas.

- tramo del origen: «a quienes les resultarán de aplicación las disposiciones de la Sección 5. en caso de incumplimiento de estas normas.» (literal: exacta)
- tramo del destino: —

---

## V088 · `aplica_a` · lote_08, 8 de 10

**Origen** — Potestad «Asistencia crediticia — no obsta evaluación de otras facilidades» (`Potestad_asistencia_crediticia_no_obsta_evaluacion_de_otras_facilidades__el_otorgamiento__03cf6d`)

- descripción: El otorgamiento de asistencia crediticia de monto reducido no obsta a que para otras facilidades crediticias al mismo prestatario deba observarse evaluación de capacidad de pago

**Predicado** — `aplica_a`

- tramo del sujeto: «los sujetos obligados» (literal: no)

**Destino** — Sujeto «Obligados a clasificar deudores (Clasificación)» (`Sujeto_rol_obligado_a_clasificar_clasificacion`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `cla::7.1` · cla · punto 7.1 · punto_propio · págs. 33, 34

- PDF: `data/experiment/subset/TO_clasificacion_deudores_actual.pdf#page=33` · `data/experiment/subset/TO_clasificacion_deudores_actual.pdf#page=34`

> *heredado (encabezado, S7, p. 33):* Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
>
> *propio:* 7.1. Criterio de clasificación. Sin perjuicio de que los análisis previos al otorgamiento de las financiaciones y refinanciaciones también deben guardar relación con la capacidad de pago de los deudores, evaluando la afec- tación de sus ingresos periódicos por la totalidad de los compromisos de crédito asumidos, la clasificación de estos clientes se efectuará considerando -al cabo de cada mes- exclusivamente pautas objetivas vinculadas al grado de cumplimiento de las correspondientes obligaciones o su situación jurídica, las informaciones que surjan de la “Central de deudores del sistema financie- ro” –cuando reflejen niveles de calidad inferiores al asignado por la entidad–, de la base de “Deudores en situación irregular de ex entidades financieras” y la situación que surja de la apli- cación de las pautas de refinanciación. En caso de discrepancias, se deberá considerar la pau- ta que indique el mayor nivel de riesgo de incobrabilidad. Se entiende que el cumplimiento de las obligaciones a que se refieren las citadas pautas tiene lugar cuando no se recurra a nuevas financiaciones o refinanciaciones destinadas a cancelar obligaciones preexistentes, cualquiera sea la modalidad (prórrogas, esperas, ampliaciones de plazo o márgenes -sean tales modalidades expresas o tácitas-, disminuciones en los importes de las cuotas o pagos, renovaciones, reestructuraciones, etc.). En el caso de refinanciaciones, a fin de determinar una mejora en la clasificación del deudor, corresponderá tener en cuenta las pautas específicas previstas en cada una de las categorías. A esos efectos, no se considerarán dentro de ese concepto las refinanciaciones otorgadas a productores cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emer- gencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta la mora en el atraso de sus obligaciones para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, pre- existente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella. A fin de determinar una mejora en la clasificación del deudor que, como consecuencia de haber incurrido en atraso en el pago de sus obligaciones refinanciadas, haya sido recategorizado en niveles inferiores, corresponderá tener en cuenta las pautas específicas previstas en cada una de las categorías, en función de la cancelación de las cuotas mínimas (financiaciones de pago periódico, mensual o bimestral) o del porcentaje de cancelación del saldo (por capital) de sus obligaciones refinanciadas (financiaciones de pago único, periódico superior a bimestral o irre- gular). A tal fin, no se podrán efectuar mejoras en las clasificaciones de los clientes, si los mismos re- gistran un atraso mayor a 31 días en el pago de sus obligaciones refinanciadas. Los cobros no aplicados y las quitas concedidas en forma previa a la refinanciación reducen el importe de la obligación sujeta a refinanciación, con lo cual no son computables para la mejora de la clasificación en función de los parámetros establecidos para cada modalidad de pago de la refinanciación. Por lo tanto, la forma en que se imputen tales conceptos a la cancelación de la deuda objeto de refinanciación dependerá del criterio que opte por emplear cada entidad, sin perjuicio de la observancia de las demás disposiciones de carácter general que sean aplicables en la materia. Los pagos por adelantado y/o anticipos que sean efectuados en oportunidad de la refinancia- ción para acceder a ella o con posterioridad a su estructuración, serán computados, en término de las cuotas o porcentaje de amortización de capital, según sea la modalidad de pago de la re- financiación, en relación al saldo de capital de la obligación refinanciada. A fin de verificar el cumplimiento de las obligaciones de naturaleza comercial comprendidas en esta cartera sin recurrir a nuevas financiaciones o a refinanciaciones, no se considerarán com- prendidas en esas definiciones: i) las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10% del cupo asignado en oportunidad de la última evaluación crediticia del cliente hasta que corresponda ser evaluado nuevamente; ii) las renovaciones periódicas de crédito para capital de trabajo ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las activi- dades. Ello, en la medida en que sean consistentes con el curso normal de los negocios y exista capa- cidad para atender el resto de las obligaciones financieras. Cuando se hayan asignado al deudor márgenes de crédito por líneas de préstamo específicas y éstos se excedan, tales situaciones no serán consideradas refinanciaciones siempre que no se supere el límite de la asistencia máxima que le haya sido acordada por todo concepto en fun- ción de su capacidad de pago, según el acápite ii) del punto 1.1.3.2. de las normas sobre “Ges- tión crediticia”. No será obligatoria la evaluación de la capacidad de pago en función de los ingresos del presta- tario, en la medida en que se utilicen métodos específicos de evaluación o se trate de deudores por préstamos de monto reducido en los términos del punto 1.1.3.3. de las normas sobre “Ges- tión crediticia”. El otorgamiento de ese tipo de asistencia no obsta a que, en el caso de que se concedan al mismo prestatario otras facilidades crediticias, deba observarse lo previsto en el primer párrafo de este punto en materia de evaluación de la capacidad de pago del deudor.

- tramo del origen: «El otorgamiento de ese tipo de asistencia no obsta a que, en el caso de que se concedan al mismo prestatario otras facilidades crediticias, deba observarse lo previsto en el primer párrafo de este punto en materia de evaluación de la capacidad de pago del deudor» (literal: exacta)
- tramo del destino: —

---

## V089 · `aplica_a` · lote_08, 9 de 10

**Origen** — Restriccion «Prohibición comisiones servicios no solicitados» (`Restriccion_no_pueden_aplicarse_comisiones_ni_cargos_por_servicios_financieros_que_no_hayan__beda04`)

- descripción: No pueden aplicarse comisiones ni cargos por servicios financieros que no hayan sido solicitados, pactados y/o autorizados por el usuario.
- tipo: prohibicion

**Predicado** — `aplica_a`

- tramo del sujeto: «el sujeto obligado» (literal: exacta)

**Destino** — Sujeto «Sujetos obligados (Protección de usuarios)» (`Sujeto_rol_sujeto_obligado_proteccion`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `pro::2.3.2.2` · pro · punto 2.3.2.2 · punto_propio · págs. 12, 13

- PDF: `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=12` · `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=13`

> *heredado (encabezado, S2, p. 5):* Sección 2. Derechos básicos de los usuarios de servicios financieros.
>
> *heredado (encabezado, 2.3, p. 7):* 2.3. Recaudos mínimos de la relación de consumo.
>
> *heredado (encabezado, 2.3.2, p. 11):* 2.3.2. Comisiones y cargos.
>
> *propio:* 2.3.2.2. No admitidos. i)Principio general. No corresponde el cobro a los usuarios de conceptos que no observen las condiciones enunciadas en el punto 2.3.2.1. y/o que deriven de la prestación de un servicio cuya comisión o cargo, según corresponda, ya se encuentre incluida en otros conceptos cobrados por el sujeto obligado. En ningún caso podrán aplicarse comisiones y/o cargos al usuario por servi- cios financieros que no hayan sido solicitados, pactados y/o autorizados por él y, aun cuando habiendo sido solicitados, pactados y/o autorizados por éste e informados por el sujeto obligado al usuario, no se hayan prestado de ma- nera efectiva. ii)Casos particulares. No podrán aplicarse comisiones ni cargos por los siguientes conceptos: a) Operaciones efectuadas por ventanilla por los usuarios de servicios fi- nancieros que sean personas humanas. Esta limitación también alcanza, en las casas operativas distintas a aque- lla en la cual esté abierta la cuenta, a los movimientos de fondos en efec- tivo en pesos (depósitos y/o extracciones) y a la recepción de depósitos de cheques efectuados por cuenta propia y/o de terceros. Ello, indepen- dientemente de las comisiones y/o cargos que correspondan por la ges- tión de cobro de dichos documentos y por los servicios que, por sus ca- racterísticas, sólo pueden ser prestados por ventanilla (certificación de cheques, transferencias internacionales, etc.). b) Depósitos de efectivo en pesos en cuentas cuyos titulares sean personas humanas o jurídicas que revistan el carácter de micro, pequeñas o me- dianas empresas (Mipyme), de acuerdo con las condiciones previstas en el TO sobre Determinación de la Condición de Micro, Pequeña o Mediana Empresa. c) Contratación y/o administración de seguros (teniendo en cuenta lo previs- to en el punto 2.3.12.). d) Generación de resúmenes de cuenta y envío de resúmenes de cuenta virtual (esos servicios deben estar incluidos en la comisión por manteni- miento de cuenta). e) Evaluación, otorgamiento y/o administración de financiaciones. f) Gastos de tasación, notariales o de escribanía que se originen en ocasión del otorgamiento o cancelación de financiaciones –tales como de constitución de prenda o hipoteca–.

- tramo del origen: «En ningún caso podrán aplicarse comisiones y/o cargos al usuario por servicios financieros que no hayan sido solicitados, pactados y/o autorizados por él» (literal: exacta)
- tramo del destino: —

---

## V090 · `requiere` · lote_08, 10 de 10

**Origen** — Operacion «Cálculo BIC» (`Operacion_calculo_bic__ric_5_2_1_aac5e1`)

- descripción: Cálculo del Indicador de Negocio (BIC), código 33000000
- tipo: cálculo

**Predicado** — `requiere`

**Destino** — Obligacion «Informar BIC calculado» (`Obligacion_deber_de_informar_el_indicador_de_negocio_bic_calculado__ric_5_2_1_f8e663`)

- descripción: Deber de informar el Indicador de Negocio (BIC) calculado
- tipo: presentacion_informativa

**Evidencia 1 de 1** — `ric::5.2.1` · ric · punto 5.2.1 · punto_propio · págs. 25

- PDF: `data/experiment/subset/TO_regimen_informativo_contable_mensual_actual.pdf#page=25`

> *heredado (encabezado, S5, p. 21):* Sección 5. Exigencia por riesgo operacional
>
> *heredado (encabezado, 5.2, p. 25):* 5.2. Modelo de información
>
> *propio:* 5.2.1. Indicador de negocio (BI) Código Concepto Observaciones 33000000 BIC Se informará el BIC calculado

- tramo del origen: «BIC calculado» (literal: exacta)
- tramo del destino: «Se informará el BIC calculado» (literal: exacta)

---

