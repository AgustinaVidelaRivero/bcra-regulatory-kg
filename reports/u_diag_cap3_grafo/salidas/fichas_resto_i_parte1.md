# Grupo (i) por código, resto sin leer, parte 1

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
  - **caso R1** Excepcion `e1`: Excepción punto 3.16.3 para personas humanas residentes | descripcion: El punto 3.16.3. no es aplicable para clientes que sean personas humanas residentes. | tramo: El punto 3.16.3. sólo será aplicable para clientes que no sean personas humanas residentes.

## Unidad `ext::3.5.4.3` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.5] exterior.
Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o
intereses de títulos de deuda con registro público en el exterior, otros endeudamientos
financieros con el exterior y títulos de deuda con registro público en el país denominados en
moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las
siguientes condiciones: | **[abre la lista]** [intro 3.5.4] para el acceso al mercado de cambios para la cancelación al vencimiento de capital e
intereses de los endeudamientos financieros comprendidos en este punto 3.5., este
requisito no resultará aplicable cuando se cumpla la totalidad de las siguientes
condiciones:
- texto propio: 3.5.4.3. el endeudamiento tenga una vida promedio no inferior a los 2 (dos) años.
- entidades de la unidad:
  - `c1` Condicion: Vigencia requisito conformidad previa BCRA — La condición de que el requisito de conformidad previa del BCRA para el acceso al mercado de cambios para la cancelación al vencimiento de capital e intereses de los endeudamientos financieros se encu
  - `e1` Excepcion: Excepción conformidad previa — condiciones cumplidas — El requisito de conformidad previa del BCRA no resultará aplicable cuando se cumplan todas las condiciones enumeradas en el punto 3.5.4
  - `c2` Condicion: Vida promedio endeudamiento mínimo 2 años — Que el endeudamiento tenga una vida promedio no inferior a los 2 (dos) años
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1; c2 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso R2** Excepcion `e1`: Excepción conformidad previa — condiciones cumplidas | descripcion: El requisito de conformidad previa del BCRA no resultará aplicable cuando se cumplan todas las condiciones enumeradas en el punto 3.5.4 | tramo: este requisito no resultará aplicable cuando se cumpla la totalidad de las siguientes condiciones

## Unidad `ext::3.5.4::intro` (intro)
- herencia: [encabezado 3.5.4] 3.5.4. En la medida que se encuentre vigente el requisito de conformidad previa del BCRA
- texto propio: para el acceso al mercado de cambios para la cancelación al vencimiento de capital e
intereses de los endeudamientos financieros comprendidos en este punto 3.5., este
requisito no resultará aplicable cuando se cumpla la totalidad de las siguientes
condiciones:
- entidades de la unidad:
  - `e1` Condicion: Vigencia requisito conformidad previa BCRA — Condición de vigencia del requisito de conformidad previa del BCRA para acceso al mercado de cambios en cancelación de endeudamientos financieros
  - `e2` Excepcion: Excepción requisito conformidad previa — endeudamientos financieros — El requisito de conformidad previa del BCRA para acceso al mercado de cambios no resultará aplicable cuando se cumpla la totalidad de las condiciones que siguen, en relación con la cancelación al venc
- relaciones del crudo (sin establecida_en ni de sujeto): e1 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso R3** Excepcion `e2`: Excepción requisito conformidad previa — endeudamientos financieros | descripcion: El requisito de conformidad previa del BCRA para acceso al mercado de cambios no resultará aplicable cuando se cumpla la totalidad de las condiciones que siguen, en relación con la cancelación al vencimiento de capital e intereses de endeudamientos financieros comprendidos en el punto 3.5. | tramo: este requisito no resultará aplicable cuando se cumpla la totalidad de las siguientes condiciones

## Unidad `ext::13.4.7` (item)
- herencia: **[abre la lista]** [intro 13.4] Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para
realizar pagos de servicios de no residentes prestados o devengados hasta el 12/12/23,
excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique
que:
- texto propio: 13.4.7. el pago se concreta en el marco de lo dispuesto en el punto 4.8.5. por un cliente que
suscribió BOPREAL Serie 1 por un monto igual o mayor al 25% (veinticinco por
ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con
anterioridad al 31/01/24; o
- entidades de la unidad:
  - `c1` Condicion: Pago en marco punto 4.8.5 — El pago se concreta en el marco de lo dispuesto en el punto 4.8.5
  - `c2` Condicion: Cliente suscribió BOPREAL Serie 1 monto ≥ 25% — Cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 25% del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24
  - `e1` Excepcion: Excepción conformidad previa BCRA — pagos servicios no residentes — Excepción a la exigencia de conformidad previa del BCRA para acceso al mercado de cambios para pagos de servicios de no residentes prestados o devengados hasta el 12/12/23, cuando se cumplen las condi
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1; c2 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso R4** Excepcion `e1`: Excepción conformidad previa BCRA — pagos servicios no residentes | descripcion: Excepción a la exigencia de conformidad previa del BCRA para acceso al mercado de cambios para pagos de servicios de no residentes prestados o devengados hasta el 12/12/23, cuando se cumplen las condiciones del punto 4.8.5 y el cliente suscribió BOPREAL Serie 1 por monto ≥ 25% de deudas elegibles antes del 31/01/24 | tramo: Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de servicios de no residentes prestados o devengados hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que: […] el pago se concreta en el marco de lo dispuesto en el punto 4.8.5. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 25% (veinticinco por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24

## Unidad `ext::13.4.4` (item)
- herencia: **[abre la lista]** [intro 13.4] Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para
realizar pagos de servicios de no residentes prestados o devengados hasta el 12/12/23,
excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique
que:
- texto propio: 13.4.4. el cliente cuenta por el equivalente al monto a pagar con una “Certificación por los
regímenes de acceso a divisas para la producción incremental de petróleo y/o gas
natural (Decreto 277/22)” emitida en el marco de lo dispuesto en el punto 3.17.; o
- entidades de la unidad:
  - `c1` Condicion: Cliente cuenta con Certificación Decreto 277/22 — El cliente cuenta con una Certificación emitida conforme al Decreto 277/22 sobre regímenes de acceso a divisas para producción incremental de petróleo y/o gas natural, por el equivalente al monto a pa
  - `e1` Excepcion: Excepción conformidad previa BCRA — servicios no residentes — Excepción a la exigencia de conformidad previa del BCRA para pagos de servicios de no residentes prestados o devengados hasta el 12/12/23, cuando el cliente cuenta con Certificación conforme al Decret
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso R5** Excepcion `e1`: Excepción conformidad previa BCRA — servicios no residentes | descripcion: Excepción a la exigencia de conformidad previa del BCRA para pagos de servicios de no residentes prestados o devengados hasta el 12/12/23, cuando el cliente cuenta con Certificación conforme al Decreto 277/22. | tramo: Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de servicios de no residentes prestados o devengados hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que: […] el cliente cuenta por el equivalente al monto a pagar con una "Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)" emitida en el marco de lo dispuesto en el punto 3.17.; o

## Unidad `ext::3.5.6.1` (item)
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
- texto propio: 3.5.6.1. se trate de operaciones propias de las entidades financieras locales.
- entidades de la unidad:
  - `e1` Excepcion: Excepción operaciones propias entidades financieras locales — Excepción al requisito de conformidad previa del BCRA para cancelación de capital e intereses de endeudamientos financieros cuando el acreedor sea contraparte vinculada, cuando se trate de operaciones
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R6** Excepcion `e1`: Excepción operaciones propias entidades financieras locales | descripcion: Excepción al requisito de conformidad previa del BCRA para cancelación de capital e intereses de endeudamientos financieros cuando el acreedor sea contraparte vinculada, cuando se trate de operaciones propias de las entidades financieras locales. | tramo: se trate de operaciones propias de las entidades financieras locales

## Unidad `ext::2.6::intro` (intro)
- herencia: [encabezado 2.6] 2.6. Excepción de liquidación de cobros de exportaciones de bienes y servicios para los
- texto propio: beneficiarios del “Régimen de fomento para las exportaciones de la economía
del conocimiento”.
- entidades de la unidad:
  - `e1` Excepcion: Excepción liquidación cobros exportaciones economía conocimiento — Excepción de liquidación de cobros de exportaciones de bienes y servicios para los beneficiarios del Régimen de fomento para las exportaciones de la economía del conocimiento
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R7** Excepcion `e1`: Excepción liquidación cobros exportaciones economía conocimiento | descripcion: Excepción de liquidación de cobros de exportaciones de bienes y servicios para los beneficiarios del Régimen de fomento para las exportaciones de la economía del conocimiento | tramo: Excepción de liquidación de cobros de exportaciones de bienes y servicios para los beneficiarios del "Régimen de fomento para las exportaciones de la economía del conocimiento"

## Unidad `ext::3.5.6.10` (item)
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
- texto propio: 3.5.6.10. se trate de un endeudamiento financiero comprendido en este punto 3.5. con
una vida promedio no inferior a los 2 (dos) años liquidado entre el 27/08/21 y
el 12/12/23 y que fue utilizado para pagar deudas comerciales por la
importación de bienes y servicios a partir de la emisión de una “Certificación
de ingreso de nuevo endeudamiento financiero con el exterior” en el marco
del punto 1. de la Comunicación A 7348 y concordantes (disposiciones
receptadas oportunamente en el punto 3.19. del Anexo de la Comunicación
A 7914).
- entidades de la unidad:
  - `c1` Condicion: Endeudamiento financiero comprendido en 3.5. — El endeudamiento debe estar comprendido en el punto 3.5. (Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el exterior)
  - `c2` Condicion: Vida promedio no inferior a 2 años — El endeudamiento debe tener una vida promedio mínima de 2 años
  - `c3` Condicion: Liquidación entre 27/08/21 y 12/12/23 — El endeudamiento debe haber sido liquidado en el período comprendido entre el 27 de agosto de 2021 y el 12 de diciembre de 2023
  - `c4` Condicion: Utilización para pagar deudas comerciales por importación — El endeudamiento debe haber sido utilizado para pagar deudas comerciales derivadas de la importación de bienes y servicios
  - `c5` Condicion: Emisión de Certificación conforme Com. A 7348 — Debe haberse emitido una Certificación de ingreso de nuevo endeudamiento financiero con el exterior conforme al punto 1 de la Comunicación A 7348 y normas concordantes
  - `e1` Excepcion: Excepción — conformidad previa BCRA no requerida — Exceptúa el requisito de conformidad previa del BCRA para el acceso al mercado de cambios para la cancelación de capital e intereses de endeudamientos financieros cuando se cumplen todas las condicion
  - `com1` Comunicacion: Com. A 7348 — 
  - `com2` Comunicacion: Com. A 7914 — 
- relaciones del crudo (sin establecida_en ni de sujeto): to referencia com1; to referencia com2; c1 condicion_de e1; c2 condicion_de e1; c3 condicion_de e1; c4 condicion_de e1; c5 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso R8** Excepcion `e1`: Excepción — conformidad previa BCRA no requerida | descripcion: Exceptúa el requisito de conformidad previa del BCRA para el acceso al mercado de cambios para la cancelación de capital e intereses de endeudamientos financieros cuando se cumplen todas las condiciones enumeradas: endeudamiento comprendido en punto 3.5., vida promedio no inferior a 2 años, liquidado entre 27/08/21 y 12/12/23, utilizado para pagar deudas comerciales por importación de bienes y servicios, y emitida Certificación conforme Com. A 7348 | tramo: se trate de un endeudamiento financiero comprendido en este punto 3.5. con una vida promedio no inferior a los 2 (dos) años liquidado entre el 27/08/21 y el 12/12/23 y que fue utilizado para pagar deudas comerciales por la importación de bienes y servicios a partir de la emisión de una "Certificación de ingreso de nuevo endeudamiento financiero con el exterior" en el marco del punto 1. de la Comunicación A 7348 y concordantes

## Unidad `ext::3.16.2::cierre` (cierre)
- herencia: [encabezado 3.16.2] 3.16.2. Declaración jurada del cliente respecto a sus tenencias de activos externos líquidos
- texto propio: Este requisito no resultará a aplicación para aquellas operaciones de egresos que
correspondan a:
i) operaciones de clientes realizadas en el marco de los puntos 3.8., 3.9., 3.13.,
3.14.1. y 3.14.2.;
ii) operaciones propias de una entidad en carácter de cliente;
iii) cancelaciones de financiaciones en moneda extranjera otorgadas por entidades
financieras locales por los consumos en moneda extranjera efectuados
mediante tarjetas de crédito o de compra; o
iv) pagos al exterior de las empresas no financieras emisoras de tarjetas por el uso
de tarjetas de crédito, de compra, de débito o prepagas emitidas en el país.
- entidades de la unidad:
  - `e1` Excepcion: Excepción — declaración jurada tenencias activos externos — La declaración jurada del cliente respecto a sus tenencias de activos externos líquidos no resultará de aplicación para operaciones de egresos que correspondan a operaciones de clientes en el marco de
  - `e2` Condicion: Operaciones de clientes — puntos 3.8., 3.9., 3.13., 3.14.1. y 3.14.2. — Operaciones de clientes realizadas en el marco de los puntos 3.8., 3.9., 3.13., 3.14.1. y 3.14.2.
  - `e3` Condicion: Operaciones propias de entidad en carácter de cliente — Operaciones propias de una entidad en carácter de cliente.
  - `e4` Condicion: Cancelaciones de financiaciones en moneda extranjera — tarjetas — Cancelaciones de financiaciones en moneda extranjera otorgadas por entidades financieras locales por consumos en moneda extranjera efectuados mediante tarjetas de crédito o de compra.
  - `e5` Condicion: Pagos al exterior — empresas emisoras de tarjetas — Pagos al exterior de empresas no financieras emisoras de tarjetas por el uso de tarjetas de crédito, de compra, de débito o prepagas emitidas en el país.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1; e3 condicion_de e1; e4 condicion_de e1; e5 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso R9** Excepcion `e1`: Excepción — declaración jurada tenencias activos externos | descripcion: La declaración jurada del cliente respecto a sus tenencias de activos externos líquidos no resultará de aplicación para operaciones de egresos que correspondan a operaciones de clientes en el marco de los puntos 3.8., 3.9., 3.13., 3.14.1. y 3.14.2.; operaciones propias de una entidad en carácter de cliente; cancelaciones de financiaciones en moneda extranjera otorgadas por entidades financieras locales por consumos en moneda extranjera efectuados mediante tarjetas de crédito o de compra; o pagos al exterior de empresas no financieras emisoras de tarjetas por el uso de tarjetas de crédito, de compra, de débito o prepagas emitidas en el país. | tramo: Este requisito no resultará a aplicación para aquellas operaciones de egresos que correspondan a:

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
  - **caso R10** Excepcion `e2`: Excepción fórmula especial cuadernos de cheques | descripcion: La fórmula especial para solicitar cuadernos de cheques queda exceptuada de la exigencia de denuncia de extravío, sustracción o adulteración. | tramo: excepto la fórmula especial para solicitar cuadernos de cheques

## Unidad `ext::6.9` (item)
- herencia: **[abre la lista]** [chapeau_seccion S6] En el marco de estas disposiciones se definen los siguientes conceptos:
- texto propio: 6.9. Rentas (ingreso primario).
Comprende la remuneración de empleados y la renta de la inversión. En el primer caso, se
incluyen los pagos de sueldos y otras remuneraciones de trabajadores temporales que se
perciben por el trabajo personal realizado por el residente de una economía, para el residente
de otra economía. En rentas de la inversión, se incluyen las transacciones por ingresos de
residentes de una economía por la tenencia de activos financieros emitidos o adeudados por
residentes de otra economía. Comprende los pagos de intereses y de utilidades y dividendos.
También se incluye en este concepto, la renta obtenida por las inversiones directas en
inmuebles. En cambio, la renta obtenida por el alquiler a no residentes de inmuebles ubicados
en el país, constituyen un ingreso del residente por servicios de alquileres.
- entidades de la unidad:
  - `e1` Definicion: Rentas (ingreso primario) — Comprende la remuneración de empleados y la renta de la inversión. En el primer caso, se incluyen los pagos de sueldos y otras remuneraciones de trabajadores temporales que se perciben por el trabajo 
  - `e2` Definicion: Remuneración de empleados — Pagos de sueldos y otras remuneraciones de trabajadores temporales que se perciben por el trabajo personal realizado por el residente de una economía, para el residente de otra economía.
  - `e3` Definicion: Renta de la inversión — Transacciones por ingresos de residentes de una economía por la tenencia de activos financieros emitidos o adeudados por residentes de otra economía. Comprende los pagos de intereses y de utilidades y
  - `e4` Definicion: Renta por inversiones directas en inmuebles — Renta obtenida por las inversiones directas en inmuebles, incluida en el concepto de rentas (ingreso primario).
  - `e5` Excepcion: Exclusión — renta por alquiler de inmuebles a no residentes — La renta obtenida por el alquiler a no residentes de inmuebles ubicados en el país no se incluye en rentas (ingreso primario), sino que constituye un ingreso del residente por servicios de alquileres.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R11** Excepcion `e5`: Exclusión — renta por alquiler de inmuebles a no residentes | descripcion: La renta obtenida por el alquiler a no residentes de inmuebles ubicados en el país no se incluye en rentas (ingreso primario), sino que constituye un ingreso del residente por servicios de alquileres. | tramo: la renta obtenida por el alquiler a no residentes de inmuebles ubicados en el país, constituyen un ingreso del residente por servicios de alquileres

## Unidad `cap::2.7.1` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca | [encabezado 2.7] 2.7. Exposiciones a empresas.
- texto propio: 2.7.1. Exposiciones comprendidas.
i) Empresas y otras personas jurídicas del país y del exterior –tales como entidades
cambiarias, aseguradoras, bursátiles y empresas del país a las que se les otorga el
tratamiento del sector privado no financiero en función de lo establecido en la Sección
1.del TO sobre Financiamiento al Sector Público no Financiero–.
ii) Demás entes con características similares que no cumplan los criterios para ser ad-
mitidas en otras categorías.
No se incluyen las exposiciones a instrumentos previstas en el punto 2.11.
- entidades de la unidad:
  - `e1` Definicion: Exposiciones a empresas — comprendidas — Comprende empresas y otras personas jurídicas del país y del exterior, tales como entidades cambiarias, aseguradoras, bursátiles y empresas del país a las que se les otorga el tratamiento del sector p
  - `e2` Definicion: Exposiciones a empresas — demás entes similares — Comprende demás entes con características similares que no cumplan los criterios para ser admitidas en otras categorías.
  - `e3` Excepcion: Exclusión — exposiciones a instrumentos — Las exposiciones a instrumentos previstas en el punto 2.11 quedan excluidas de las exposiciones a empresas.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R12** Excepcion `e3`: Exclusión — exposiciones a instrumentos | descripcion: Las exposiciones a instrumentos previstas en el punto 2.11 quedan excluidas de las exposiciones a empresas. | tramo: No se incluyen las exposiciones a instrumentos previstas en el punto 2.11

## Unidad `cap::2.2.1` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca | [encabezado 2.2] 2.2. Exclusiones.
- texto propio: 2.2.1. Garantías otorgadas a favor del BCRA y por obligaciones directas.
- entidades de la unidad:
  - `e1` Excepcion: Exclusión garantías BCRA y obligaciones directas — Las garantías otorgadas a favor del BCRA y por obligaciones directas quedan excluidas del cómputo de capital mínimo por riesgo de crédito
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R13** Excepcion `e1`: Exclusión garantías BCRA y obligaciones directas | descripcion: Las garantías otorgadas a favor del BCRA y por obligaciones directas quedan excluidas del cómputo de capital mínimo por riesgo de crédito | tramo: Garantías otorgadas a favor del BCRA y por obligaciones directas

## Unidad `ext::2.6.1::intro` (intro)
- herencia: [encabezado 2.6.1] 2.6.1. Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen
- texto propio: de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo
dispuesto en el Capítulo II del Decreto 679/22 quedarán exceptuados de la obligación
de liquidación de los cobros de exportaciones de bienes y servicios que correspondan
a actividades de la economía del conocimiento, en la medida que se cumpla la
totalidad de las siguientes condiciones:
- entidades de la unidad:
  - `e1` Excepcion: Excepción liquidación cobros exportaciones economía conocimiento — Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y beneficiarios del Capítulo II del Decreto 679/22 quedan exceptuada
  - `c1` Condicion: Cumplimiento totalidad condiciones siguientes — La excepción se aplica cuando se cumpla la totalidad de las condiciones que siguen.
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso R14** Excepcion `e1`: Excepción liquidación cobros exportaciones economía conocimiento | descripcion: Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y beneficiarios del Capítulo II del Decreto 679/22 quedan exceptuadas de la obligación de liquidación de cobros de exportaciones de bienes y servicios correspondientes a actividades de la economía del conocimiento. | tramo: quedarán exceptuados de la obligación de liquidación de los cobros de exportaciones de bienes y servicios que correspondan a actividades de la economía del conocimiento

## Unidad `ext::6.7` (item)
- herencia: **[abre la lista]** [chapeau_seccion S6] En el marco de estas disposiciones se definen los siguientes conceptos:
- texto propio: 6.7. Posición general de cambios (PGC).
Comprenderá la totalidad de los activos externos líquidos de la entidad, netos de los saldos
deudores de corresponsalía originados en la operatoria del mercado de cambios. También
quedarán comprendidas las compras y ventas concertadas en el mercado de cambios y que
se encuentran pendientes de liquidación.
Serán considerados activos externos líquidos de la entidad, entre otros: monedas y billetes en
moneda extranjera, disponibilidades en oro amonedado o en barras de buena entrega, saldos
acreedores de corresponsalía (incluyendo las transferencias a favor de terceros sin liquidación
concertada), otros depósitos a la vista en entidades financieras del exterior, inversiones en
títulos públicos externos y certificados de depósito a plazo.
No formarán parte de la PGC: inversiones directas en el exterior, activos externos de terceros
en custodia, ventas y compras a término de divisas o valores externos, depósitos en el BCRA
en moneda extranjera en cuentas a nombre de la entidad y demás activos locales en moneda
extranjera.
- entidades de la unidad:
  - `e1` Definicion: PGC — activos externos líquidos netos — La totalidad de los activos externos líquidos de la entidad, netos de los saldos deudores de corresponsalía originados en la operatoria del mercado de cambios.
  - `e2` Definicion: PGC — compras y ventas concertadas pendientes — Incluye las compras y ventas concertadas en el mercado de cambios que se encuentran pendientes de liquidación.
  - `e3` Definicion: Activos externos líquidos — componentes — Monedas y billetes en moneda extranjera, disponibilidades en oro amonedado o en barras de buena entrega, saldos acreedores de corresponsalía (incluyendo las transferencias a favor de terceros sin liqu
  - `e4` Excepcion: Exclusiones de PGC — inversiones directas — Las inversiones directas en el exterior no forman parte de la Posición general de cambios.
  - `e5` Excepcion: Exclusiones de PGC — activos en custodia — Los activos externos de terceros en custodia no forman parte de la Posición general de cambios.
  - `e6` Excepcion: Exclusiones de PGC — ventas y compras a término — Las ventas y compras a término de divisas o valores externos no forman parte de la Posición general de cambios.
  - `e7` Excepcion: Exclusiones de PGC — depósitos BCRA moneda extranjera — Los depósitos en el BCRA en moneda extranjera en cuentas a nombre de la entidad no forman parte de la Posición general de cambios.
  - `e8` Excepcion: Exclusiones de PGC — activos locales moneda extranjera — Los demás activos locales en moneda extranjera no forman parte de la Posición general de cambios.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R15** Excepcion `e6`: Exclusiones de PGC — ventas y compras a término | descripcion: Las ventas y compras a término de divisas o valores externos no forman parte de la Posición general de cambios. | tramo: No formarán parte de la PGC: ventas y compras a término de divisas o valores externos

## Unidad `ext::6.7` (item)
- herencia: **[abre la lista]** [chapeau_seccion S6] En el marco de estas disposiciones se definen los siguientes conceptos:
- texto propio: 6.7. Posición general de cambios (PGC).
Comprenderá la totalidad de los activos externos líquidos de la entidad, netos de los saldos
deudores de corresponsalía originados en la operatoria del mercado de cambios. También
quedarán comprendidas las compras y ventas concertadas en el mercado de cambios y que
se encuentran pendientes de liquidación.
Serán considerados activos externos líquidos de la entidad, entre otros: monedas y billetes en
moneda extranjera, disponibilidades en oro amonedado o en barras de buena entrega, saldos
acreedores de corresponsalía (incluyendo las transferencias a favor de terceros sin liquidación
concertada), otros depósitos a la vista en entidades financieras del exterior, inversiones en
títulos públicos externos y certificados de depósito a plazo.
No formarán parte de la PGC: inversiones directas en el exterior, activos externos de terceros
en custodia, ventas y compras a término de divisas o valores externos, depósitos en el BCRA
en moneda extranjera en cuentas a nombre de la entidad y demás activos locales en moneda
extranjera.
- entidades de la unidad:
  - `e1` Definicion: PGC — activos externos líquidos netos — La totalidad de los activos externos líquidos de la entidad, netos de los saldos deudores de corresponsalía originados en la operatoria del mercado de cambios.
  - `e2` Definicion: PGC — compras y ventas concertadas pendientes — Incluye las compras y ventas concertadas en el mercado de cambios que se encuentran pendientes de liquidación.
  - `e3` Definicion: Activos externos líquidos — componentes — Monedas y billetes en moneda extranjera, disponibilidades en oro amonedado o en barras de buena entrega, saldos acreedores de corresponsalía (incluyendo las transferencias a favor de terceros sin liqu
  - `e4` Excepcion: Exclusiones de PGC — inversiones directas — Las inversiones directas en el exterior no forman parte de la Posición general de cambios.
  - `e5` Excepcion: Exclusiones de PGC — activos en custodia — Los activos externos de terceros en custodia no forman parte de la Posición general de cambios.
  - `e6` Excepcion: Exclusiones de PGC — ventas y compras a término — Las ventas y compras a término de divisas o valores externos no forman parte de la Posición general de cambios.
  - `e7` Excepcion: Exclusiones de PGC — depósitos BCRA moneda extranjera — Los depósitos en el BCRA en moneda extranjera en cuentas a nombre de la entidad no forman parte de la Posición general de cambios.
  - `e8` Excepcion: Exclusiones de PGC — activos locales moneda extranjera — Los demás activos locales en moneda extranjera no forman parte de la Posición general de cambios.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R16** Excepcion `e5`: Exclusiones de PGC — activos en custodia | descripcion: Los activos externos de terceros en custodia no forman parte de la Posición general de cambios. | tramo: No formarán parte de la PGC: activos externos de terceros en custodia

## Unidad `ext::6.7` (item)
- herencia: **[abre la lista]** [chapeau_seccion S6] En el marco de estas disposiciones se definen los siguientes conceptos:
- texto propio: 6.7. Posición general de cambios (PGC).
Comprenderá la totalidad de los activos externos líquidos de la entidad, netos de los saldos
deudores de corresponsalía originados en la operatoria del mercado de cambios. También
quedarán comprendidas las compras y ventas concertadas en el mercado de cambios y que
se encuentran pendientes de liquidación.
Serán considerados activos externos líquidos de la entidad, entre otros: monedas y billetes en
moneda extranjera, disponibilidades en oro amonedado o en barras de buena entrega, saldos
acreedores de corresponsalía (incluyendo las transferencias a favor de terceros sin liquidación
concertada), otros depósitos a la vista en entidades financieras del exterior, inversiones en
títulos públicos externos y certificados de depósito a plazo.
No formarán parte de la PGC: inversiones directas en el exterior, activos externos de terceros
en custodia, ventas y compras a término de divisas o valores externos, depósitos en el BCRA
en moneda extranjera en cuentas a nombre de la entidad y demás activos locales en moneda
extranjera.
- entidades de la unidad:
  - `e1` Definicion: PGC — activos externos líquidos netos — La totalidad de los activos externos líquidos de la entidad, netos de los saldos deudores de corresponsalía originados en la operatoria del mercado de cambios.
  - `e2` Definicion: PGC — compras y ventas concertadas pendientes — Incluye las compras y ventas concertadas en el mercado de cambios que se encuentran pendientes de liquidación.
  - `e3` Definicion: Activos externos líquidos — componentes — Monedas y billetes en moneda extranjera, disponibilidades en oro amonedado o en barras de buena entrega, saldos acreedores de corresponsalía (incluyendo las transferencias a favor de terceros sin liqu
  - `e4` Excepcion: Exclusiones de PGC — inversiones directas — Las inversiones directas en el exterior no forman parte de la Posición general de cambios.
  - `e5` Excepcion: Exclusiones de PGC — activos en custodia — Los activos externos de terceros en custodia no forman parte de la Posición general de cambios.
  - `e6` Excepcion: Exclusiones de PGC — ventas y compras a término — Las ventas y compras a término de divisas o valores externos no forman parte de la Posición general de cambios.
  - `e7` Excepcion: Exclusiones de PGC — depósitos BCRA moneda extranjera — Los depósitos en el BCRA en moneda extranjera en cuentas a nombre de la entidad no forman parte de la Posición general de cambios.
  - `e8` Excepcion: Exclusiones de PGC — activos locales moneda extranjera — Los demás activos locales en moneda extranjera no forman parte de la Posición general de cambios.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R17** Excepcion `e7`: Exclusiones de PGC — depósitos BCRA moneda extranjera | descripcion: Los depósitos en el BCRA en moneda extranjera en cuentas a nombre de la entidad no forman parte de la Posición general de cambios. | tramo: No formarán parte de la PGC: depósitos en el BCRA en moneda extranjera en cuentas a nombre de la entidad

## Unidad `ctacte::6.4.6.2` (item)
- herencia: **[abre la lista]** [encabezado 6.4.6] 6.4.6. No corresponderá la comunicación al BCRA de los rechazos motivados por:
- texto propio: 6.4.6.2. El pago de cheques falsificados o adulterados.
- entidades de la unidad:
  - `e1` Excepcion: Excepción — cheques falsificados o adulterados — No corresponderá la comunicación al BCRA de los rechazos motivados por el pago de cheques falsificados o adulterados
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R18** Excepcion `e1`: Excepción — cheques falsificados o adulterados | descripcion: No corresponderá la comunicación al BCRA de los rechazos motivados por el pago de cheques falsificados o adulterados | tramo: El pago de cheques falsificados o adulterados

## Unidad `ext::10.2.2` (punto_no_item)
- herencia: [encabezado 10.2] 10.2. Definiciones.
- texto propio: 10.2.2. Registro de ingreso aduanero.
A los efectos de esta norma se considera que una importación de bienes cuenta con
el registro de ingreso aduanero cuando el importador realizó la oficialización del
despacho de importación para su posterior despacho a plaza de los bienes.
También se da cumplimiento a dicho registro cuando los bienes son ingresados al
país con despacho a plaza a través de Solicitud Particular o Courier o se
cumplimentó el trámite aduanero por el ingreso de bienes del exterior a zonas francas
nacionales y dicho ingreso se corresponde con una venta de bienes de un no
residente a un residente.
No se incluyen los registros aduaneros por importaciones suspensivas de depósitos
de almacenamiento ni los ingresos de importaciones temporarias sin giro de divisas.
- entidades de la unidad:
  - `e1` Definicion: Registro de ingreso aduanero — importación — Una importación de bienes cuenta con el registro de ingreso aduanero cuando el importador realizó la oficialización del despacho de importación para su posterior despacho a plaza de los bienes.
  - `e2` Definicion: Registro de ingreso aduanero — despacho a plaza — Se da cumplimiento al registro de ingreso aduanero cuando los bienes son ingresados al país con despacho a plaza a través de Solicitud Particular o Courier.
  - `e3` Definicion: Registro de ingreso aduanero — zonas francas — Se da cumplimiento al registro de ingreso aduanero cuando se cumplimentó el trámite aduanero por el ingreso de bienes del exterior a zonas francas nacionales y dicho ingreso se corresponde con una ven
  - `e4` Excepcion: Exclusión — importaciones suspensivas de depósitos — No se incluyen los registros aduaneros por importaciones suspensivas de depósitos de almacenamiento en la definición de registro de ingreso aduanero.
  - `e5` Excepcion: Exclusión — importaciones temporarias sin giro — No se incluyen los ingresos de importaciones temporarias sin giro de divisas en la definición de registro de ingreso aduanero.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R19** Excepcion `e4`: Exclusión — importaciones suspensivas de depósitos | descripcion: No se incluyen los registros aduaneros por importaciones suspensivas de depósitos de almacenamiento en la definición de registro de ingreso aduanero. | tramo: No se incluyen los registros aduaneros por importaciones suspensivas de depósitos de almacenamiento

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
  - **caso R20** Excepcion `e1`: Excepción — conformidad previa del BCRA — situaciones especiales | descripcion: No se requiere conformidad previa del BCRA si el deudor encuadra en alguna de las situaciones especiales que siguen y se cumplen todas las condiciones estipuladas en cada caso. | tramo: excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso

## Unidad `ext::2.7::intro` (intro)
- herencia: [encabezado 2.7] 2.7. Otras excepciones a la obligación de liquidación.
- texto propio: En adición a las excepciones enunciadas precedentemente, tampoco resultará exigible la
liquidación en el mercado de cambios de los fondos en moneda extranjera que reciban los
residentes por las operaciones previstas en los puntos 2.1. a 2.5., en la medida que se cumpla
la totalidad de las siguientes condiciones:
- entidades de la unidad:
  - `e1` Excepcion: Excepción liquidación fondos moneda extranjera — No será exigible la liquidación en el mercado de cambios de fondos en moneda extranjera recibidos por residentes de operaciones previstas en puntos 2.1 a 2.5, cuando se cumplan todas las condiciones s
  - `c1` Condicion: Cumplimiento totalidad condiciones siguientes — Se requiere el cumplimiento de la totalidad de las condiciones que se enuncian a continuación
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso R21** Excepcion `e1`: Excepción liquidación fondos moneda extranjera | descripcion: No será exigible la liquidación en el mercado de cambios de fondos en moneda extranjera recibidos por residentes de operaciones previstas en puntos 2.1 a 2.5, cuando se cumplan todas las condiciones siguientes | tramo: tampoco resultará exigible la liquidación en el mercado de cambios de los fondos en moneda extranjera que reciban los residentes por las operaciones previstas en los puntos 2.1. a 2.5., en la medida que se cumpla la totalidad de las siguientes condiciones

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
  - **caso R22** Excepcion `e1`: Excepción inciso viii) acceso mercado cambios | descripcion: Queda exceptuada la condición prevista en el inciso viii) del punto 10.3.2.1. para el acceso al mercado de cambios | tramo: excepto aquella prevista en el inciso viii)

## Unidad `cla::2.2.2.2` (item)
- herencia: **[abre la lista]** [encabezado 2.2.2] 2.2.2. Las siguientes garantías otorgadas:
- texto propio: 2.2.2.2. A favor del Banco Central de la República Argentina.
- entidades de la unidad:
  - `e1` Excepcion: Exclusión garantías a favor del BCRA — Quedan exceptuadas de la clasificación las garantías otorgadas a favor del Banco Central de la República Argentina
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R23** Excepcion `e1`: Exclusión garantías a favor del BCRA | descripcion: Quedan exceptuadas de la clasificación las garantías otorgadas a favor del Banco Central de la República Argentina | tramo: A favor del Banco Central de la República Argentina

## Unidad `ext::3.13.1.2` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.13] residentes | **[abre la lista]** [intro 3.13.1] residentes y otras compras de moneda extranjera por parte de clientes no residentes
requerirá la conformidad previa del BCRA, excepto para las operaciones de: | [cierre 3.13.1] Si una repatriación de una inversión directa de no residentes consiste en una
reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa
local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar
con la documentación que demuestre que se han cumplimentado los mecanismos
legales previstos y haber verificado que se encuentra declarada, en caso de
corresponder, en la última presentación vencida del “Relevamiento de activos y
pasivos externos” 
- texto propio: 3.13.1.2. Representaciones diplomáticas y consulares y personal diplomático
acreditado en el país por transferencias que efectúen en ejercicio de sus
funciones.
- entidades de la unidad:
  - `e1` Excepcion: Excepción repatriación — representaciones diplomáticas — Quedan exceptuadas de la exigencia de conformidad previa del BCRA las operaciones de repatriación de inversiones de no residentes y otras compras de moneda extranjera realizadas por representaciones d
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R24** Excepcion `e1`: Excepción repatriación — representaciones diplomáticas | descripcion: Quedan exceptuadas de la exigencia de conformidad previa del BCRA las operaciones de repatriación de inversiones de no residentes y otras compras de moneda extranjera realizadas por representaciones diplomáticas y consulares y personal diplomático acreditado en el país, cuando las transferencias se efectúen en ejercicio de sus funciones. | tramo: Representaciones diplomáticas y consulares y personal diplomático acreditado en el país por transferencias que efectúen en ejercicio de sus funciones

## Unidad `cla::2.2.2.1` (item)
- herencia: **[abre la lista]** [encabezado 2.2.2] 2.2.2. Las siguientes garantías otorgadas:
- texto propio: 2.2.2.1. Por obligaciones directas.
- entidades de la unidad:
  - `e1` Excepcion: Exclusión garantías por obligaciones directas — Quedan exceptuadas del alcance de las garantías comprendidas las garantías otorgadas por obligaciones directas
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R25** Excepcion `e1`: Exclusión garantías por obligaciones directas | descripcion: Quedan exceptuadas del alcance de las garantías comprendidas las garantías otorgadas por obligaciones directas | tramo: Por obligaciones directas

## Unidad `pro::1.1.2.5` (punto_no_item)
- herencia: [encabezado 1.1.2] 1.1.2. Sujetos obligados.
- texto propio: 1.1.2.5. Otros proveedores no financieros de crédito alcanzados por las normas sobre
“Proveedores no financieros de crédito”, excepto que se trate de asociaciones
mutuales o cooperativas, por las financiaciones que otorguen.
- entidades de la unidad:
  - `e1` Definicion: Otros proveedores no financieros de crédito alcanzados — Proveedores no financieros de crédito que están alcanzados por las normas sobre protección de usuarios, con excepción de asociaciones mutuales o cooperativas, en lo que respecta a las financiaciones q
  - `e2` Excepcion: Excepción asociaciones mutuales y cooperativas — Quedan exceptuadas del alcance de las normas sobre proveedores no financieros de crédito las asociaciones mutuales y cooperativas, en lo que respecta a las financiaciones que otorguen.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R26** Excepcion `e2`: Excepción asociaciones mutuales y cooperativas | descripcion: Quedan exceptuadas del alcance de las normas sobre proveedores no financieros de crédito las asociaciones mutuales y cooperativas, en lo que respecta a las financiaciones que otorguen. | tramo: excepto que se trate de asociaciones mutuales o cooperativas

## Unidad `ext::8.5.17.19` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.19. Exportación a consumo de bienes que conforman el equipaje no
acompañado del viajero pero que se exportan fuera de los plazos
establecidos en el inciso c) apartado 3 del artículo 60 del Decreto
1.001/82.
- entidades de la unidad:
  - `e1` Excepcion: Excepción equipaje no acompañado fuera de plazo — Quedan exceptuadas del seguimiento las exportaciones a consumo de bienes que conforman el equipaje no acompañado del viajero cuando se exportan fuera de los plazos establecidos en el inciso c) apartad
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R27** Excepcion `e1`: Excepción equipaje no acompañado fuera de plazo | descripcion: Quedan exceptuadas del seguimiento las exportaciones a consumo de bienes que conforman el equipaje no acompañado del viajero cuando se exportan fuera de los plazos establecidos en el inciso c) apartado 3 del artículo 60 del Decreto 1.001/82 | tramo: Exportación a consumo de bienes que conforman el equipaje no acompañado del viajero pero que se exportan fuera de los plazos establecidos en el inciso c) apartado 3 del artículo 60 del Decreto 1.001/82

## Unidad `ext::8.5.17.2` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.2. Régimen de rancho (artículos 506 al 516 de la Ley 22.415) en la medida
que correspondan a medios de transporte de bandera nacional.
- entidades de la unidad:
  - `e1` Excepcion: Excepción rancho — seguimiento operaciones aduaneras — Quedan exceptuadas del seguimiento las operaciones aduaneras correspondientes al régimen de rancho regulado en los artículos 506 al 516 de la Ley 22.415, en la medida que correspondan a medios de tran
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R28** Excepcion `e1`: Excepción rancho — seguimiento operaciones aduaneras | descripcion: Quedan exceptuadas del seguimiento las operaciones aduaneras correspondientes al régimen de rancho regulado en los artículos 506 al 516 de la Ley 22.415, en la medida que correspondan a medios de transporte de bandera nacional. | tramo: Régimen de rancho (artículos 506 al 516 de la Ley 22.415) en la medida que correspondan a medios de transporte de bandera nacional

## Unidad `ext::8.5.17.28` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.28. Operaciones aduaneras de los subregímenes “BARA” y “VMI1” en el
marco de la operatoria de proveedores de combustibles de medios de
transporte.
- entidades de la unidad:
  - `e1` Excepcion: Excepción operaciones aduaneras BARA y VMI1 — Quedan exceptuadas del seguimiento las operaciones aduaneras de los subregímenes BARA y VMI1 en el marco de la operatoria de proveedores de combustibles de medios de transporte
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R29** Excepcion `e1`: Excepción operaciones aduaneras BARA y VMI1 | descripcion: Quedan exceptuadas del seguimiento las operaciones aduaneras de los subregímenes BARA y VMI1 en el marco de la operatoria de proveedores de combustibles de medios de transporte | tramo: Operaciones aduaneras de los subregímenes "BARA" y "VMI1" en el marco de la operatoria de proveedores de combustibles de medios de transporte

## Unidad `cla::2.2.1.5` (item)
- herencia: **[abre la lista]** [encabezado 2.2.1] 2.2.1. Los siguientes conceptos por intermediación financiera:
- texto propio: 2.2.1.5. Anticipos y préstamos al Fondo de Garantía de los Depósitos.
- entidades de la unidad:
  - `e1` Excepcion: Exclusión — Anticipos y préstamos al Fondo de Garantía — Quedan exceptuados de la clasificación de deudores los anticipos y préstamos al Fondo de Garantía de los Depósitos, en el contexto de financiaciones por intermediación financiera.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R30** Excepcion `e1`: Exclusión — Anticipos y préstamos al Fondo de Garantía | descripcion: Quedan exceptuados de la clasificación de deudores los anticipos y préstamos al Fondo de Garantía de los Depósitos, en el contexto de financiaciones por intermediación financiera. | tramo: Anticipos y préstamos al Fondo de Garantía de los Depósitos

## Unidad `cla::2.2.1.1` (item)
- herencia: **[abre la lista]** [encabezado 2.2.1] 2.2.1. Los siguientes conceptos por intermediación financiera:
- texto propio: 2.2.1.1. Deudores por pases activos, ventas a término y ventas al contado a liquidar.
- entidades de la unidad:
  - `e1` Excepcion: Exclusión — deudores por pases activos, ventas a término y ventas al contado — Quedan exceptuados de la clasificación de deudores los deudores por pases activos, ventas a término y ventas al contado a liquidar
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R31** Excepcion `e1`: Exclusión — deudores por pases activos, ventas a término y ventas al contado | descripcion: Quedan exceptuados de la clasificación de deudores los deudores por pases activos, ventas a término y ventas al contado a liquidar | tramo: Deudores por pases activos, ventas a término y ventas al contado a liquidar

## Unidad `ext::7.8.4::intro` (intro)
- herencia: [encabezado 7.8.4] 7.8.4. Excepción de liquidación para cobros de exportaciones de bienes de beneficiarios del
- texto propio: régimen de fomento para las exportaciones de la economía del conocimiento.
Quedarán exceptuados de la obligación de liquidación, en la medida que ingresen
dentro de los plazos normativos establecidos, los cobros de exportaciones de bienes
de personas jurídicas que sean beneficiarias del régimen de fomento para las
exportaciones de la economía del conocimiento (Capítulo II del Decreto 679/22) y se
cumplan la totalidad de las siguientes condiciones:
- entidades de la unidad:
  - `e1` Excepcion: Excepción liquidación — cobros exportaciones beneficiarios economía conocimiento — Quedan exceptuados de la obligación de liquidación los cobros de exportaciones de bienes de personas jurídicas beneficiarias del régimen de fomento para las exportaciones de la economía del conocimien
  - `e2` Condicion: Cumplimiento totalidad condiciones — excepción liquidación — Se deben cumplir la totalidad de las condiciones que siguen para que la excepción de liquidación sea aplicable.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso R32** Excepcion `e1`: Excepción liquidación — cobros exportaciones beneficiarios economía conocimiento | descripcion: Quedan exceptuados de la obligación de liquidación los cobros de exportaciones de bienes de personas jurídicas beneficiarias del régimen de fomento para las exportaciones de la economía del conocimiento, siempre que ingresen dentro de los plazos normativos establecidos. | tramo: Quedarán exceptuados de la obligación de liquidación, en la medida que ingresen dentro de los plazos normativos establecidos, los cobros de exportaciones de bienes de personas jurídicas que sean beneficiarias del régimen de fomento para las exportaciones de la economía del conocimiento (Capítulo II del Decreto 679/22)

## Unidad `ext::2.2.2::intro` (intro)
- herencia: [encabezado 2.2.2] 2.2.2. Quedarán exceptuados de la obligación de liquidación los cobros de exportaciones de
- texto propio: servicios que ingresen en los plazos normativos previstos y encuadren en las
siguientes situaciones:
- entidades de la unidad:
  - `e1` Excepcion: Excepción — cobros de exportaciones de servicios — Quedan exceptuados de la obligación de liquidación los cobros de exportaciones de servicios que ingresen en los plazos normativos previstos y encuadren en las situaciones que siguen.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R33** Excepcion `e1`: Excepción — cobros de exportaciones de servicios | descripcion: Quedan exceptuados de la obligación de liquidación los cobros de exportaciones de servicios que ingresen en los plazos normativos previstos y encuadren en las situaciones que siguen. | tramo: Quedarán exceptuados de la obligación de liquidación los cobros de exportaciones de servicios que ingresen en los plazos normativos previstos y encuadren en las siguientes situaciones

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
  - **caso R34** Excepcion `e2`: Excepción requisito liquidación divisas — endeudamientos anteriores 01/09/19 | descripcion: Quedan exceptuados del requisito de demostrar ingreso y liquidación de divisas en el mercado de cambios los endeudamientos desembolsados con anterioridad al 01/09/19 | tramo: los endeudamientos desembolsados con anterioridad al 01/09/19

## Unidad `ext::6.1.2` (punto_no_item)
- herencia: [chapeau_seccion S6] En el marco de estas disposiciones se definen los siguientes conceptos: | [encabezado 6.1] 6.1. Instrumentos operados en el mercado de cambios.
- texto propio: 6.1.2. Divisas en moneda extranjera.
Son instrumentos de pago expresados en una moneda emitida por un estado
extranjero y generalmente aceptados en transacciones transnacionales: transferencia
bancaria internacional, orden de pago, giro, cheque de viajero, cheque sobre cuentas
en el exterior, etc.
Quedan excluidos de esta definición las monedas y billetes en moneda extranjera, el
oro amonedado y el oro en barras de buena entrega.
- entidades de la unidad:
  - `e1` Definicion: Divisas en moneda extranjera — Instrumentos de pago expresados en una moneda emitida por un estado extranjero y generalmente aceptados en transacciones transnacionales, incluyendo transferencia bancaria internacional, orden de pago
  - `e2` Excepcion: Exclusión de monedas, billetes, oro amonedado y oro en barras — Quedan excluidos de la definición de divisas en moneda extranjera las monedas y billetes en moneda extranjera, el oro amonedado y el oro en barras de buena entrega.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R35** Excepcion `e2`: Exclusión de monedas, billetes, oro amonedado y oro en barras | descripcion: Quedan excluidos de la definición de divisas en moneda extranjera las monedas y billetes en moneda extranjera, el oro amonedado y el oro en barras de buena entrega. | tramo: Quedan excluidos de esta definición las monedas y billetes en moneda extranjera, el oro amonedado y el oro en barras de buena entrega.

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
  - **caso R36** Excepcion `e1`: Excepción — fletes de importaciones no incluidos en condición de compra | descripcion: Se admite computar el valor de los fletes no incluidos en la condición de compra cuando el importador ha demostrado el registro de ingreso aduanero de los bienes cuyos fletes se abonaron y constan en la documentación de transporte asociada. | tramo: Si existiesen fondos destinados al pago de fletes de importaciones de bienes no incluidos en la condición de compra y el importador demostró el registro de ingreso aduanero de los bienes cuyos fletes se abonaron, también se podrá computar el valor de los fletes que consten en la documentación de transporte asociada al registro de ingreso aduanero de los bienes

## Unidad `ext::3.5.1.2` (item)
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
- texto propio: 3.5.1.2. los endeudamientos originados a partir del 01/09/19 que no generen
desembolsos por ser refinanciaciones de capital y/o intereses de deudas
financieras con el exterior que hubieran tenido acceso en virtud de la
normativa aplicable, en la medida que las refinanciaciones no anticipen el
vencimiento de la deuda original.
- entidades de la unidad:
  - `c1` Condicion: Endeudamientos originados desde 01/09/19 — El endeudamiento debe haber sido originado a partir del 01/09/19
  - `c2` Condicion: Refinanciaciones sin desembolsos — El endeudamiento no debe generar desembolsos por tratarse de refinanciaciones de capital y/o intereses de deudas financieras con el exterior
  - `c3` Condicion: Deuda original con acceso previo — Las deudas financieras originales con el exterior deben haber tenido acceso al mercado de cambios conforme a la normativa aplicable
  - `c4` Condicion: Refinanciación sin anticipación de vencimiento — Las refinanciaciones no deben anticipar el vencimiento de la deuda original
  - `e1` Excepcion: Excepción requisito ingreso liquidación divisas — refinanciaciones — Se exceptúa del requisito de demostrar ingreso y liquidación de divisas en el mercado de cambios a los endeudamientos que sean refinanciaciones de capital y/o intereses de deudas financieras con el ex
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1; c2 condicion_de e1; c3 condicion_de e1; c4 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso R37** Excepcion `e1`: Excepción requisito ingreso liquidación divisas — refinanciaciones | descripcion: Se exceptúa del requisito de demostrar ingreso y liquidación de divisas en el mercado de cambios a los endeudamientos que sean refinanciaciones de capital y/o intereses de deudas financieras con el exterior que hubieran tenido acceso previo, siempre que no anticipen el vencimiento original | tramo: los endeudamientos originados a partir del 01/09/19 que no generen desembolsos por ser refinanciaciones de capital y/o intereses de deudas financieras con el exterior que hubieran tenido acceso en virtud de la normativa aplicable, en la medida que las refinanciaciones no anticipen el vencimiento de la deuda original

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
  - **caso R38** Excepcion `e2`: Excepción operaciones del exterior liquidadas parcialmente | descripcion: Se permite emitir certificaciones por la porción no liquidada de operaciones del exterior liquidadas parcialmente durante las vigencias de los Decretos 492/23, 549/23, 597/23 y 28/23, siempre que se verifique lo previsto en el punto 7.3.11. | tramo: En caso de tratarse de una operación del exterior liquidada parcialmente durante las respectivas vigencias de los Decretos 492/23, 549/23, 597/23 y 28/23, también se podrá emitir certificaciones por la porción no liquidada en la medida que se verifique lo previsto en el punto 7.3.11

## Unidad `ric::5.1.3::intro` (intro)
- herencia: [encabezado 5.1.3] 5.1.3. Reducción de la exigencia para entidades financieras del Grupo 2 que pertenezcan a
- texto propio: los Grupos “A”, “B” y “C”.
- entidades de la unidad:
  - `e1` Excepcion: Reducción exigencia — Grupo 2 en Grupos A, B, C — Se reduce la exigencia para entidades financieras del Grupo 2 que pertenezcan a los Grupos "A", "B" y "C".
  - `e2` Condicion: Pertenencia a Grupos A, B o C — La entidad financiera del Grupo 2 pertenece a los Grupos "A", "B" o "C".
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso R39** Excepcion `e1`: Reducción exigencia — Grupo 2 en Grupos A, B, C | descripcion: Se reduce la exigencia para entidades financieras del Grupo 2 que pertenezcan a los Grupos "A", "B" y "C". | tramo: Reducción de la exigencia para entidades financieras del Grupo 2 que pertenezcan a los Grupos "A", "B" y "C".

## Unidad `ext::6.3` (item)
- herencia: **[abre la lista]** [chapeau_seccion S6] En el marco de estas disposiciones se definen los siguientes conceptos:
- texto propio: 6.3. Operaciones al contado.
Comprende las operaciones en las cuales la liquidación por parte de ambas partes está
pactada dentro de un plazo de hasta 2 (dos) días hábiles desde la fecha de su concertación.
Estas operaciones se consideran como accesos al mercado de cambios según su fecha de
concertación.
- entidades de la unidad:
  - `e1` Definicion: Operaciones al contado — Operaciones en las cuales la liquidación por parte de ambas partes está pactada dentro de un plazo de hasta 2 (dos) días hábiles desde la fecha de su concertación.
  - `e2` Condicion: Acceso al mercado de cambios por fecha de concertación — Las operaciones al contado se consideran accesos al mercado de cambios según su fecha de concertación.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R40** Condicion `e2`: Acceso al mercado de cambios por fecha de concertación | descripcion: Las operaciones al contado se consideran accesos al mercado de cambios según su fecha de concertación. | tramo: Estas operaciones se consideran como accesos al mercado de cambios según su fecha de concertación.

## Unidad `ext::7.6.1.2` (item)
- herencia: [intro 7.6] Un permiso de embarque será registrado por la entidad de seguimiento en la condición de
“Incumplido en gestión de cobro” cuando se haya verificado que el incumplimiento se debe a
la falta de pago del importador, por haberse demostrado las situaciones previstas conforme a
los puntos 7.6.1. a 7.6.3.
En todos los casos la entidad deberá obtener la declaración jurada sobre el carácter genuino
de lo declarado, firmada por el exportador o quien ejerza su representación legal o un
apoderado con faculta | **[abre la lista]** [intro 7.6.1] Cuando la falta de pago del importador extranjero se deba a la existencia de al menos
una de las siguientes situaciones:
- texto propio: 7.6.1.2. En el país de destino, el acceso al mercado de cambios para el pago de
importaciones de bienes está sujeto al requisito de una autorización previa,
existiendo documentación que permite a la entidad interviniente considerar
que existe una demora en el otorgamiento de estas autorizaciones, que no
es atribuible a las partes intervinientes en la operación comercial ni a las
entidades financieras participantes.
- entidades de la unidad:
  - `c1` Condicion: Acceso al mercado de cambios sujeto a autorización previa — El acceso al mercado de cambios para el pago de importaciones de bienes en el país de destino está sujeto al requisito de una autorización previa.
  - `c2` Condicion: Demora en otorgamiento de autorizaciones de cambios — Existe documentación que permite a la entidad interviniente considerar que hay una demora en el otorgamiento de las autorizaciones de cambios, no atribuible a las partes intervinientes en la operación
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R41** Condicion `c1`: Acceso al mercado de cambios sujeto a autorización previa | descripcion: El acceso al mercado de cambios para el pago de importaciones de bienes en el país de destino está sujeto al requisito de una autorización previa. | tramo: En el país de destino, el acceso al mercado de cambios para el pago de importaciones de bienes está sujeto al requisito de una autorización previa

## Unidad `ext::7.6.2::intro` (intro)
- herencia: [encabezado 7.6.2] 7.6.2. Insolvencia posterior del importador extranjero.
- texto propio: Cuando el importador extranjero haya caído en estado de insolvencia con posterioridad
al embarque de la mercadería y el exportador aporte la siguiente documentación:
- entidades de la unidad:
  - `c1` Condicion: Insolvencia posterior del importador extranjero — El importador extranjero ha caído en estado de insolvencia después del embarque de la mercadería
  - `c2` Condicion: Aporte de documentación por exportador — El exportador aporta la documentación requerida
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R42** Condicion `c2`: Aporte de documentación por exportador | descripcion: El exportador aporta la documentación requerida | tramo: el exportador aporte la siguiente documentación

## Unidad `cap::2.10` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca
- texto propio: 2.10. Exposiciones en situación de incumplimiento.
Comprende a todas aquellas exposiciones a un deudor respecto del que se verifique alguna
de las siguientes situaciones:
i) El deudor posee un crédito en mora de más de 90 días. Se considera que un descubierto
en cuenta corriente se encuentra en mora a partir del momento en que el deudor excede
el límite autorizado o se le comunica un nuevo límite y éste es inferior a su saldo deudor.
ii) El deudor cuenta con cualquier obligación significativa respecto de la cual se haya sus-
pendido el devengamiento de intereses, o los intereses se encuentren totalmente previ-
sionados.
iii) Se ha dado de baja contablemente una obligación o se ha constituido una previsión es-
pecífica frente a una desmejora significativa en la calidad crediticia del deudor con poste-
rioridad al otorgamiento del crédito.
iv) Se ha vendido un crédito con una pérdida significativa con motivo de su situación crediti-
cia.
v) Se ha acordado una reestructuración de una obligación crediticia que puede resultar en
una reducción de la deuda como consecuencia de quitas, diferimientos del pago del capi-
tal o de los intereses o una disminución de las comisiones aplicables.
vi) Se ha solicitado la quiebra del deudor u otra medida similar que produzca el diferimiento
o impida el recupero del crédito por parte de la entidad.
vii) El deudor ha solicitado su concurso preventivo o quiebra u otra medida similar que pro-
duzca el diferimiento o impida el recupero del crédito por parte de la entidad.
viii) La entidad financiera considera que es improbable que pueda recuperar el total de las
acreencias del deudor sin recurrir a la ejecución de las garantías u otras medidas en de-
fensa de su crédito.
- entidades de la unidad:
  - `e1` Definicion: Exposiciones en situación de incumplimiento — Todas aquellas exposiciones a un deudor respecto del que se verifique alguna de las siguientes situaciones: (i) El deudor posee un crédito en mora de más de 90 días; (ii) El deudor cuenta con cualquie
  - `e2` Condicion: Crédito en mora de más de 90 días — Situación en que el deudor posee un crédito en mora de más de 90 días. Se considera que un descubierto en cuenta corriente se encuentra en mora a partir del momento en que el deudor excede el límite a
  - `e3` Condicion: Obligación significativa con intereses suspendidos o provisionados — Situación en que el deudor cuenta con cualquier obligación significativa respecto de la cual se haya suspendido el devengamiento de intereses, o los intereses se encuentren totalmente provisionados.
  - `e4` Condicion: Baja contable o previsión por desmejora crediticia — Situación en que se ha dado de baja contablemente una obligación o se ha constituido una previsión específica frente a una desmejora significativa en la calidad crediticia del deudor con posterioridad
  - `e5` Condicion: Venta de crédito con pérdida significativa — Situación en que se ha vendido un crédito con una pérdida significativa con motivo de su situación crediticia.
  - `e6` Condicion: Reestructuración de obligación crediticia — Situación en que se ha acordado una reestructuración de una obligación crediticia que puede resultar en una reducción de la deuda como consecuencia de quitas, diferimientos del pago del capital o de l
  - `e7` Condicion: Solicitud de quiebra del deudor — Situación en que se ha solicitado la quiebra del deudor u otra medida similar que produzca el diferimiento o impida el recupero del crédito por parte de la entidad.
  - `e8` Condicion: Solicitud de concurso preventivo o quiebra por el deudor — Situación en que el deudor ha solicitado su concurso preventivo o quiebra u otra medida similar que produzca el diferimiento o impida el recupero del crédito por parte de la entidad.
  - `e9` Condicion: Recupero improbable sin ejecución de garantías — Situación en que la entidad financiera considera que es improbable que pueda recuperar el total de las acreencias del deudor sin recurrir a la ejecución de las garantías u otras medidas en defensa de 
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R43** Condicion `e4`: Baja contable o previsión por desmejora crediticia | descripcion: Situación en que se ha dado de baja contablemente una obligación o se ha constituido una previsión específica frente a una desmejora significativa en la calidad crediticia del deudor con posterioridad al otorgamiento del crédito. | tramo: Se ha dado de baja contablemente una obligación o se ha constituido una previsión específica frente a una desmejora significativa en la calidad crediticia del deudor con posterioridad al otorgamiento del crédito

## Unidad `ext::3.15.2.4` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.15] financiación de operaciones de comercio exterior y garantías financieras otorgadas. | **[abre la lista]** [intro 3.15.2] Las entidades financieras locales podrán acceder al mercado de cambios para hacer
frente a sus obligaciones con no residentes por garantías financieras otorgadas a
partir del 01/10/21, en la medida que se reúnan la totalidad de las siguientes
condiciones:
- texto propio: 3.15.2.4. El beneficiario del pago es la contraparte no residente o una entidad
financiera del exterior que haya otorgado garantías por el fiel cumplimiento
de contratos de obras o provisión de bienes y/o servicios por parte del
exportador o una empresa no residente que controla.
- entidades de la unidad:
  - `c1` Condicion: Beneficiario es contraparte no residente — El beneficiario del pago es la contraparte no residente
  - `c2` Condicion: Beneficiario es entidad financiera del exterior — El beneficiario es una entidad financiera del exterior que haya otorgado garantías por el fiel cumplimiento de contratos de obras o provisión de bienes y/o servicios por parte del exportador o una emp
  - `d1` Definicion: Beneficiario del pago — garantías financieras — La contraparte no residente o una entidad financiera del exterior que haya otorgado garantías por el fiel cumplimiento de contratos de obras o provisión de bienes y/o servicios por parte del exportado
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R44** Condicion `c1`: Beneficiario es contraparte no residente | descripcion: El beneficiario del pago es la contraparte no residente | tramo: El beneficiario del pago es la contraparte no residente

## Unidad `ext::3.15.2.4` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.15] financiación de operaciones de comercio exterior y garantías financieras otorgadas. | **[abre la lista]** [intro 3.15.2] Las entidades financieras locales podrán acceder al mercado de cambios para hacer
frente a sus obligaciones con no residentes por garantías financieras otorgadas a
partir del 01/10/21, en la medida que se reúnan la totalidad de las siguientes
condiciones:
- texto propio: 3.15.2.4. El beneficiario del pago es la contraparte no residente o una entidad
financiera del exterior que haya otorgado garantías por el fiel cumplimiento
de contratos de obras o provisión de bienes y/o servicios por parte del
exportador o una empresa no residente que controla.
- entidades de la unidad:
  - `c1` Condicion: Beneficiario es contraparte no residente — El beneficiario del pago es la contraparte no residente
  - `c2` Condicion: Beneficiario es entidad financiera del exterior — El beneficiario es una entidad financiera del exterior que haya otorgado garantías por el fiel cumplimiento de contratos de obras o provisión de bienes y/o servicios por parte del exportador o una emp
  - `d1` Definicion: Beneficiario del pago — garantías financieras — La contraparte no residente o una entidad financiera del exterior que haya otorgado garantías por el fiel cumplimiento de contratos de obras o provisión de bienes y/o servicios por parte del exportado
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R45** Condicion `c2`: Beneficiario es entidad financiera del exterior | descripcion: El beneficiario es una entidad financiera del exterior que haya otorgado garantías por el fiel cumplimiento de contratos de obras o provisión de bienes y/o servicios por parte del exportador o una empresa no residente que controla | tramo: una entidad financiera del exterior que haya otorgado garantías por el fiel cumplimiento de contratos de obras o provisión de bienes y/o servicios por parte del exportador o una empresa no residente que controla

## Unidad `ext::4.7.2` (item)
- herencia: [intro 4.7] contrapartes vinculadas sujetos a la conformidad previa del BCRA prevista en los puntos
3.3.3. y 3.5.6.
Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre
(BOPREAL) por hasta la suma adeudada a la fecha de la suscripción por: | [intro 4.7] i) Intereses compensatorios vencidos hasta el 04/07/24 por deudas comerciales por | [intro 4.7] importaciones de bienes y servicios con contrapartes vinculadas. | [intro 4.7] ii) Intereses compensatorios vencidos hasta el 31/12/24 por deudas financieras con | [intro 4.7] contrapartes vinculadas. | [intro 4.7] iii) Capital vencido por deudas financieras con contrapartes vinculadas. | **[abre la lista]** [intro 4.7] La entidad que concrete la oferta de suscripción en nombre del cliente deberá contar con la
documentación que permite avalar la existencia de la deuda, el monto adeudado a la fecha de
suscripción y verificar que: | [cierre 4.7] La mencionada entidad deberá realizar un boleto de venta de cambio a nombre del cliente por
el código de concepto que identifique el tipo de operación (“I12. Registro de intereses
compensatorios por deudas comerciales con contrapartes vinculadas por adjudicación de
bonos BOPREAL”, “I13. Registro de intereses compensatorios por deudas financieras con
contrapartes vinculadas por adjudicación de bonos BOPREAL” o “P28. Registro de deudas
con contrapartes vinculadas por adjudicación de bonos BOPREAL”
- texto propio: 4.7.2. el cliente cumple los requisitos complementarios previstos en los puntos 3.16.1. a
3.16.4.
- entidades de la unidad:
  - `e1` Condicion: Cliente cumple requisitos complementarios — El cliente debe cumplir los requisitos complementarios establecidos en los puntos 3.16.1 a 3.16.4
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R46** Condicion `e1`: Cliente cumple requisitos complementarios | descripcion: El cliente debe cumplir los requisitos complementarios establecidos en los puntos 3.16.1 a 3.16.4 | tramo: el cliente cumple los requisitos complementarios previstos en los puntos 3.16.1. a 3.16.4.

## Unidad `cap::2.7.2.1` (item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca | **[abre la lista]** [intro 2.7.2] des financieras deberán considerar las siguientes definiciones:
- texto propio: 2.7.2.1. Empresas con “grado de inversión”.
Las empresas con “grado de inversión” son aquellas con capacidad suficiente
para atender puntualmente sus compromisos financieros aun ante cambios ad-
versos en la coyuntura económica y en las condiciones de los negocios.
A tales efectos, se deberá tener en cuenta la complejidad del modelo de nego-
cios de la empresa, el desempeño en relación con su industria y empresas simi-
lares y los riesgos de su entorno operativo. La empresa con “grado de inver-
sión” (o su controlante) deberá haber emitido títulos valores que coticen en bol-
sas o mercados de valores reconocidos.
- entidades de la unidad:
  - `e1` Definicion: Empresas con grado de inversión — Aquellas con capacidad suficiente para atender puntualmente sus compromisos financieros aun ante cambios adversos en la coyuntura económica y en las condiciones de los negocios.
  - `e2` Condicion: Complejidad del modelo de negocios y desempeño relativo — Para determinar si una empresa tiene grado de inversión, se debe considerar la complejidad del modelo de negocios, el desempeño relativo a su industria y empresas similares, y los riesgos de su entorn
  - `e3` Condicion: Emisión de títulos valores en bolsas reconocidas — La empresa con grado de inversión, o su controlante, debe haber emitido títulos valores que coticen en bolsas o mercados de valores reconocidos.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R47** Condicion `e2`: Complejidad del modelo de negocios y desempeño relativo | descripcion: Para determinar si una empresa tiene grado de inversión, se debe considerar la complejidad del modelo de negocios, el desempeño relativo a su industria y empresas similares, y los riesgos de su entorno operativo. | tramo: se deberá tener en cuenta la complejidad del modelo de negocios de la empresa, el desempeño en relación con su industria y empresas similares y los riesgos de su entorno operativo

## Unidad `cap::2.10` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca
- texto propio: 2.10. Exposiciones en situación de incumplimiento.
Comprende a todas aquellas exposiciones a un deudor respecto del que se verifique alguna
de las siguientes situaciones:
i) El deudor posee un crédito en mora de más de 90 días. Se considera que un descubierto
en cuenta corriente se encuentra en mora a partir del momento en que el deudor excede
el límite autorizado o se le comunica un nuevo límite y éste es inferior a su saldo deudor.
ii) El deudor cuenta con cualquier obligación significativa respecto de la cual se haya sus-
pendido el devengamiento de intereses, o los intereses se encuentren totalmente previ-
sionados.
iii) Se ha dado de baja contablemente una obligación o se ha constituido una previsión es-
pecífica frente a una desmejora significativa en la calidad crediticia del deudor con poste-
rioridad al otorgamiento del crédito.
iv) Se ha vendido un crédito con una pérdida significativa con motivo de su situación crediti-
cia.
v) Se ha acordado una reestructuración de una obligación crediticia que puede resultar en
una reducción de la deuda como consecuencia de quitas, diferimientos del pago del capi-
tal o de los intereses o una disminución de las comisiones aplicables.
vi) Se ha solicitado la quiebra del deudor u otra medida similar que produzca el diferimiento
o impida el recupero del crédito por parte de la entidad.
vii) El deudor ha solicitado su concurso preventivo o quiebra u otra medida similar que pro-
duzca el diferimiento o impida el recupero del crédito por parte de la entidad.
viii) La entidad financiera considera que es improbable que pueda recuperar el total de las
acreencias del deudor sin recurrir a la ejecución de las garantías u otras medidas en de-
fensa de su crédito.
- entidades de la unidad:
  - `e1` Definicion: Exposiciones en situación de incumplimiento — Todas aquellas exposiciones a un deudor respecto del que se verifique alguna de las siguientes situaciones: (i) El deudor posee un crédito en mora de más de 90 días; (ii) El deudor cuenta con cualquie
  - `e2` Condicion: Crédito en mora de más de 90 días — Situación en que el deudor posee un crédito en mora de más de 90 días. Se considera que un descubierto en cuenta corriente se encuentra en mora a partir del momento en que el deudor excede el límite a
  - `e3` Condicion: Obligación significativa con intereses suspendidos o provisionados — Situación en que el deudor cuenta con cualquier obligación significativa respecto de la cual se haya suspendido el devengamiento de intereses, o los intereses se encuentren totalmente provisionados.
  - `e4` Condicion: Baja contable o previsión por desmejora crediticia — Situación en que se ha dado de baja contablemente una obligación o se ha constituido una previsión específica frente a una desmejora significativa en la calidad crediticia del deudor con posterioridad
  - `e5` Condicion: Venta de crédito con pérdida significativa — Situación en que se ha vendido un crédito con una pérdida significativa con motivo de su situación crediticia.
  - `e6` Condicion: Reestructuración de obligación crediticia — Situación en que se ha acordado una reestructuración de una obligación crediticia que puede resultar en una reducción de la deuda como consecuencia de quitas, diferimientos del pago del capital o de l
  - `e7` Condicion: Solicitud de quiebra del deudor — Situación en que se ha solicitado la quiebra del deudor u otra medida similar que produzca el diferimiento o impida el recupero del crédito por parte de la entidad.
  - `e8` Condicion: Solicitud de concurso preventivo o quiebra por el deudor — Situación en que el deudor ha solicitado su concurso preventivo o quiebra u otra medida similar que produzca el diferimiento o impida el recupero del crédito por parte de la entidad.
  - `e9` Condicion: Recupero improbable sin ejecución de garantías — Situación en que la entidad financiera considera que es improbable que pueda recuperar el total de las acreencias del deudor sin recurrir a la ejecución de las garantías u otras medidas en defensa de 
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R48** Condicion `e2`: Crédito en mora de más de 90 días | descripcion: Situación en que el deudor posee un crédito en mora de más de 90 días. Se considera que un descubierto en cuenta corriente se encuentra en mora a partir del momento en que el deudor excede el límite autorizado o se le comunica un nuevo límite y éste es inferior a su saldo deudor. | tramo: El deudor posee un crédito en mora de más de 90 días

## Unidad `ext::4.6.2.2` (item)
- herencia: [intro 4.6] pendientes de pago o ya percibidas en el país. | **[abre la lista]** [intro 4.6.2] dividendos cobrados desde el 01/09/19.
Los clientes no residentes podrán suscribir Bonos para la Reconstrucción de una
Argentina Libre (BOPREAL) por hasta el equivalente al monto en moneda local de las
utilidades y dividendos cobrados desde el 01/09/19 a partir de la distribución
determinada por la asamblea de accionistas, ajustado por el último Índice de Precios al
Consumidor (IPC) disponible a la fecha de suscripción.
La entidad que concrete la oferta de suscripción en nombre del cliente deber | [cierre 4.6.2] Adicionalmente, la entidad deberá realizar un boleto de venta de cambio a nombre de
la empresa que hubiera abonado las utilidades y dividendos bajo el código "P21.
Registro de fondos abonados en el país por utilidades y dividendos por adjudicación de
bonos BOPREAL"; consignando el valor nominal en moneda extranjera de los bonos
BOPREAL adjudicado al cliente.
- texto propio: 4.6.2.2. El residente que abonó las utilidades y dividendos cumple los requisitos
complementarios previstos en los puntos 3.16.1. a 3.16.4.
- entidades de la unidad:
  - `e1` Condicion: Cumplimiento de requisitos complementarios — El residente que abonó las utilidades y dividendos debe cumplir los requisitos complementarios previstos en los puntos 3.16.1. a 3.16.4.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R49** Condicion `e1`: Cumplimiento de requisitos complementarios | descripcion: El residente que abonó las utilidades y dividendos debe cumplir los requisitos complementarios previstos en los puntos 3.16.1. a 3.16.4. | tramo: El residente que abonó las utilidades y dividendos cumple los requisitos complementarios previstos en los puntos 3.16.1. a 3.16.4.

## Unidad `ext::2.6.1.3` (item)
- herencia: [intro 2.6] beneficiarios del “Régimen de fomento para las exportaciones de la economía
del conocimiento”. | **[abre la lista]** [intro 2.6.1] de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo
dispuesto en el Capítulo II del Decreto 679/22 quedarán exceptuados de la obligación
de liquidación de los cobros de exportaciones de bienes y servicios que correspondan
a actividades de la economía del conocimiento, en la medida que se cumpla la
totalidad de las siguientes condiciones: | [cierre 2.6.1] Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el Capítulo II
del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento
cambiario diferencial que no sea aquel previsto en dicho capítulo.
- texto propio: 2.6.1.3. se den cumplimiento a los restantes requisitos establecidos en los puntos
2.2.2.2. o 7.8.4., según corresponda.
- entidades de la unidad:
  - `c1` Condicion: Cumplimiento requisitos puntos 2.2.2.2 o 7.8.4 — Se debe dar cumplimiento a los restantes requisitos establecidos en los puntos 2.2.2.2 o 7.8.4, según corresponda, como condición para la excepción de liquidación de cobros de exportaciones de bienes 
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R50** Condicion `c1`: Cumplimiento requisitos puntos 2.2.2.2 o 7.8.4 | descripcion: Se debe dar cumplimiento a los restantes requisitos establecidos en los puntos 2.2.2.2 o 7.8.4, según corresponda, como condición para la excepción de liquidación de cobros de exportaciones de bienes y servicios para beneficiarios del Régimen de Promoción de la Economía del Conocimiento. | tramo: se den cumplimiento a los restantes requisitos establecidos en los puntos 2.2.2.2. o 7.8.4., según corresponda

## Unidad `ext::9.3.10.1` (item)
- herencia: [intro 9.3] A solicitud del exportador, la entidad encargada del seguimiento emitirá las certificaciones de
aplicación en la medida que se verifiquen las condiciones previstas en los puntos 9.3.1. al
9.3.13.
La entidad deberá dejar registradas las certificaciones de aplicación emitidas para cada una
de las operaciones bajo su seguimiento. | **[abre la lista]** [intro 9.3.10] controlantes de entidades financieras locales admitidas en los puntos 7.9. o 7.10.
La entidad podrá emitir la certificación de aplicación en la medida que la entidad
cuenta con la documentación que le permita verificar:
- texto propio: 9.3.10.1. el cumplimiento de los requisitos establecidos en los puntos 7.9. o 7.10.;
- entidades de la unidad:
  - `e1` Condicion: Cumplimiento requisitos puntos 7.9 o 7.10 — Verificación del cumplimiento de los requisitos establecidos en los puntos 7.9 o 7.10 para repatriaciones de aportes de inversión directa de no residentes en empresas no controlantes de entidades fina
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R51** Condicion `e1`: Cumplimiento requisitos puntos 7.9 o 7.10 | descripcion: Verificación del cumplimiento de los requisitos establecidos en los puntos 7.9 o 7.10 para repatriaciones de aportes de inversión directa de no residentes en empresas no controlantes de entidades financieras locales | tramo: el cumplimiento de los requisitos establecidos en los puntos 7.9. o 7.10.

## Unidad `ext::9.3.10.4` (item)
- herencia: [intro 9.3] A solicitud del exportador, la entidad encargada del seguimiento emitirá las certificaciones de
aplicación en la medida que se verifiquen las condiciones previstas en los puntos 9.3.1. al
9.3.13.
La entidad deberá dejar registradas las certificaciones de aplicación emitidas para cada una
de las operaciones bajo su seguimiento. | **[abre la lista]** [intro 9.3.10] controlantes de entidades financieras locales admitidas en los puntos 7.9. o 7.10.
La entidad podrá emitir la certificación de aplicación en la medida que la entidad
cuenta con la documentación que le permita verificar:
- texto propio: 9.3.10.4. el pasivo en pesos con el exterior generado a partir de la fecha de la no
aceptación del aporte irrevocable o de la reducción de capital según
corresponda. Se encuentra declarado en la última presentación vencida del
“Relevamiento de activos y pasivos externos”, en caso de corresponder;
- entidades de la unidad:
  - `c1` Condicion: Pasivo en pesos con exterior desde no aceptación o reducción — El pasivo en pesos con el exterior debe haber sido generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital, según corresponda.
  - `c2` Condicion: Declaración en Relevamiento de activos y pasivos externos — El pasivo debe encontrarse declarado en la última presentación vencida del Relevamiento de activos y pasivos externos, en caso de corresponder.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R52** Condicion `c2`: Declaración en Relevamiento de activos y pasivos externos | descripcion: El pasivo debe encontrarse declarado en la última presentación vencida del Relevamiento de activos y pasivos externos, en caso de corresponder. | tramo: Se encuentra declarado en la última presentación vencida del "Relevamiento de activos y pasivos externos", en caso de corresponder

## Unidad `ext::4.6.1.2` (item)
- herencia: [intro 4.6] pendientes de pago o ya percibidas en el país. | **[abre la lista]** [intro 4.6.1] residentes a partir de la distribución determinada por la asamblea de accionistas.
Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre
(BOPREAL) por hasta el equivalente al monto en moneda local de las utilidades y
dividendos pendientes de pago a accionistas no residentes a partir de la distribución
determinada por la asamblea de accionistas.
La entidad que concrete la oferta de suscripción en nombre del cliente deberá verificar
el cumplimiento de los siguientes req | [cierre 4.6.1] Adicionalmente, la mencionada entidad deberá realizar un boleto de venta de cambio a
nombre del cliente por el código de concepto "I09. Registro de utilidades y dividendos
por adjudicación de bonos BOPREAL"; consignando el valor nominal en moneda
extranjera de los bonos BOPREAL adjudicado al cliente.
- texto propio: 4.6.1.2. La operación se encuentra declarada, en caso de corresponder, en la última
presentación vencida del "Relevamiento de activos y pasivos externos".
- entidades de la unidad:
  - `c1` Condicion: Declaración en Relevamiento de activos y pasivos externos — La operación debe encontrarse declarada, en caso de corresponder, en la última presentación vencida del Relevamiento de activos y pasivos externos
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R53** Condicion `c1`: Declaración en Relevamiento de activos y pasivos externos | descripcion: La operación debe encontrarse declarada, en caso de corresponder, en la última presentación vencida del Relevamiento de activos y pasivos externos | tramo: La operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos"

## Unidad `ext::10.11.7.5` (punto_no_item)
- herencia: [intro 10.11] aduanero hasta el 12/12/23.
Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para
realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el
12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad
verifique que: | [intro 10.11.7] clasifique como MiPyMe según lo dispuesto en las normas de “Determinación de la
condición de micro, pequeña y mediana empresa” y se cumple la totalidad de las
siguientes condiciones:.
- texto propio: 10.11.7.5. La entidad cuente con una declaración jurada del cliente en la que
conste que:
i) la totalidad de sus deudas por importaciones de bienes y servicios
previas al 13/12/23 han sido declaradas en el “Padrón de Deuda
Comercial por Importaciones con Proveedores del Exterior” y el
monto total adeudado a la fecha de cierre del mencionado registro
no superaba el equivalente a USD 500.000 (dólares
estadounidenses quinientos mil).
ii) los montos abonados por este mecanismo en el conjunto de las
entidades y por el conjunto de los conceptos no superan los límites
previstos en el punto 10.11.7.3.
- entidades de la unidad:
  - `c1` Condicion: Declaración jurada cliente deuda comercial — La entidad debe contar con una declaración jurada del cliente que acredite el cumplimiento de los requisitos sobre deuda comercial previa y límites de pago.
  - `c2` Condicion: Deuda comercial previa declarada — tope USD 500.000 — La totalidad de las deudas por importaciones de bienes y servicios previas al 13/12/23 deben haber sido declaradas en el Padrón de Deuda Comercial por Importaciones con Proveedores del Exterior, y el 
  - `c3` Condicion: Montos abonados respetan límites punto 10.11.7.3 — Los montos abonados por este mecanismo en el conjunto de las entidades y por el conjunto de los conceptos no deben superar los límites previstos en el punto 10.11.7.3.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso R54** Condicion `c1`: Declaración jurada cliente deuda comercial | descripcion: La entidad debe contar con una declaración jurada del cliente que acredite el cumplimiento de los requisitos sobre deuda comercial previa y límites de pago. | tramo: La entidad cuente con una declaración jurada del cliente en la que conste que:
