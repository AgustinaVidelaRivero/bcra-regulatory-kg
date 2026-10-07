# `ric::4.1.1.5` — Código 312200/xx

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 4. Exigencia e integración por riesgo de mercado
> *heredado:* 4.1. Normas de procedimiento
> *heredado:* 4.1.1. Exigencia
> *propio:* 4.1.1.5. Código 312200/xx Se consignará el valor de la exigencia por riesgo general de acciones para el último día del período (n) determinada conforme a las disposiciones del punto 6.3. de las normas sobre "Capitales mínimos de las entidades financieras". Este riesgo se discriminará por mercado, entendido a estos efectos como el país en que se negocien posiciones -compradas o vendidasen acciones. A estos efectos, el país se identificará de acuerdo con la codificación del Country Codes del SWIFT.

## Omisiones leídas en T4 (M2)

sin_marca:1 [no normativa; propio] «Código 312200/xx»

## Código A

- **op1 Operacion** «Exigencia por riesgo general de acciones» — Exigencia por riesgo general de acciones, determinada conforme al punto 6.3. de las normas sobre Capitales mínimos de las entidades financieras, al último día del período (n) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «el valor de la exigencia por riesgo general de acciones para el último día del período (n)»
- **ob1 Obligacion** «Consignar exigencia riesgo general de acciones (312200/xx)» — Se consigna en el código 312200/xx el valor de la exigencia por riesgo general de acciones para el último día del período (n), determinada conforme al punto 6.3. de las normas sobre Capitales mínimos de las entidades financieras. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se consignará el valor de la exigencia por riesgo general de acciones para el último día del período (n) determinada conforme a las disposiciones del punto 6.3. de las normas sobre "Capitales mínimos de las entidades financieras".»
- **ob2 Obligacion** «Discriminar riesgo de acciones por mercado (país)» — El riesgo general de acciones se discrimina por mercado, entendido como el país en que se negocien posiciones, compradas o vendidas, en acciones. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Este riesgo se discriminará por mercado»
- **def1 Definicion** «Mercado (país de negociación de acciones)» — A estos efectos, el país en que se negocien posiciones, compradas o vendidas, en acciones. · props: `{"termino": "mercado"}` · tramo [exacta]: «mercado, entendido a estos efectos como el país en que se negocien posiciones -compradas o vendidasen acciones»
- **ob3 Obligacion** «Identificar país según Country Codes SWIFT» — El país se identifica de acuerdo con la codificación del Country Codes del SWIFT. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «el país se identificará de acuerdo con la codificación del Country Codes del SWIFT»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion

### A — omisiones de T4 a clasificar

- sin_marca:1 → entidades: — | omisiones: —

## Código H

- **o1 Obligacion** «Consignar exigencia por riesgo general de acciones (312200/xx)» — Se consigna en el código 312200/xx el valor de la exigencia por riesgo general de acciones para el último día del período (n), determinada conforme al punto 6.3. de las normas sobre Capitales mínimos de las entidades financieras. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se consignará el valor de la exigencia por riesgo general de acciones para el último día del período (n)»
- **o2 Obligacion** «Discriminar riesgo general de acciones por mercado (país)» — El riesgo general de acciones se discrimina por mercado, entendido como el país en que se negocien posiciones, compradas o vendidas, en acciones. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Este riesgo se discriminará por mercado, entendido a estos efectos como el país en que se negocien posiciones -compradas o vendidasen acciones.»
- **o3 Obligacion** «Identificar el país según Country Codes del SWIFT» — El país en que se negocian las posiciones se identifica de acuerdo con la codificación del Country Codes del SWIFT. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «el país se identificará de acuerdo con la codificación del Country Codes del SWIFT.»
- **d1 Definicion** «Mercado (país de negociación de posiciones en acciones)» — A los efectos de la discriminación del riesgo general de acciones, el país en que se negocien posiciones, compradas o vendidas, en acciones. · props: `{"termino": "mercado"}` · tramo [exacta]: «mercado, entendido a estos efectos como el país en que se negocien posiciones -compradas o vendidasen acciones»

### H — omisiones de T4 a clasificar

- sin_marca:1 → entidades: — | omisiones: —

## Código K

- **e1 Obligacion** «Código 312200/xx — exigencia riesgo general acciones» — En el código 312200/xx se consignará el valor de la exigencia por riesgo general de acciones para el último día del período (n), determinada conforme al punto 6.3. de las normas sobre Capitales mínimos de las entidades financieras. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se consignará el valor de la exigencia por riesgo general de acciones para el último día del período (n) determinada conforme a las disposiciones del punto 6.3. de las normas sobre "Capitales mínimos de las entidades financieras".»
- **e2 Obligacion** «Discriminación por mercado — riesgo general de acciones» — El riesgo general de acciones informado en el código 312200/xx se discriminará por mercado, identificando el país según la codificación del Country Codes del SWIFT. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Este riesgo se discriminará por mercado»
- **e3 Definicion** «Mercado — país de negociación de acciones» — El país en que se negocien posiciones -compradas o vendidasen acciones. · props: `{"termino": "mercado"}` · tramo [exacta]: «entendido a estos efectos como el país en que se negocien posiciones -compradas o vendidasen acciones»
- **e4 Obligacion** «Identificación del país por Country Codes SWIFT» — A los fines de la discriminación por mercado del código 312200/xx, el país se identificará según la codificación del Country Codes del SWIFT. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «el país se identificará de acuerdo con la codificación del Country Codes del SWIFT»

### K — omisiones de T4 a clasificar

- sin_marca:1 → entidades: — | omisiones: —

## Código W

- **e1 Obligacion** «Consignar exigencia riesgo general de acciones (312200/xx)» — En el código 312200/xx se consignará el valor de la exigencia por riesgo general de acciones para el último día del período (n), determinada conforme al punto 6.3. de las normas sobre Capitales mínimos de las entidades financieras. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se consignará el valor de la exigencia por riesgo general de acciones para el último día del período (n) determinada conforme a las disposiciones del punto 6.3. de las normas sobre "Capitales mínimos de las entidades financieras".»
- **e2 Obligacion** «Discriminación por mercado (país) — riesgo de acciones» — La exigencia por riesgo general de acciones se informará discriminada por mercado, identificando el país según la codificación Country Codes del SWIFT. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Este riesgo se discriminará por mercado, entendido a estos efectos como el país en que se negocien posiciones -compradas o vendidasen acciones.»
- **e3 Definicion** «Mercado: país de negociación de acciones» — El país en que se negocien posiciones -compradas o vendidasen acciones; identificado según Country Codes del SWIFT. · props: `{"termino": "mercado"}` · tramo [exacta]: «mercado, entendido a estos efectos como el país en que se negocien posiciones -compradas o vendidasen acciones»

### W — omisiones de T4 a clasificar

- sin_marca:1 → entidades: — | omisiones: —

