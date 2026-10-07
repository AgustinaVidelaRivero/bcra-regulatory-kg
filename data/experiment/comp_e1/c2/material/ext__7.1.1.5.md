# `ext::7.1.1.5` — 365 (trescientos sesenta y cinco) días corridos para las operaciones que se

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.1. Obligación de ingreso y liquidación en los plazos establecidos.
> *heredado:* 7.1.1. Exportaciones oficializadas a partir del 02/09/19.
> *heredado:* El contravalor en divisas de la exportación hasta alcanzar el valor facturado según la condición de venta pactada deberá ingresarse al país y liquidarse en el mercado de cambios. En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicios resultará aplicable lo dispuesto en los puntos 14.1.1. y 14.1.2., según corresponda. El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse en los siguientes plazos a computar desde la fecha del cumplido de embarque otorgado por la Aduana:
> *heredado:* Independientemente de los plazos máximos precedentes, los cobros de exportaciones deberán ser ingresados y liquidados en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro. La posibilidad de utilizar este plazo quedará supeditada en todos los casos al cumplimiento de los plazos previstos en los puntos 7.1.1.1. a 7.1.1.5. Los montos en moneda extranjera originados en cobros de siniestros por coberturas contratadas, en la medida que los mismos cubran el valor de los bienes exportados, están alcanzados por esta obligación. El exportador deberá seleccionar una entidad para que realice el "Seguimiento de las negociaciones de divisas por exportaciones de bienes". La obligación de ingreso y liquidación de divisas de un permiso de embarque se considerará cumplida cuando la entidad haya certificado tal situación por los mecanismos establecidos a tal efecto.
> *propio:* 7.1.1.5. 365 (trescientos sesenta y cinco) días corridos para las operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE", independientemente del tipo de bien exportado.

## Omisiones leídas en T4 (M2)

sin_marca:10 [normativa; propio] «independientemente del tipo de bien exportado»

## Código A

- **op1 Operacion** «Ingreso y liquidación de divisas — EXPORTA SIMPLE» — Ingreso al país y liquidación en el mercado de cambios del contravalor en divisas de exportaciones de bienes concretadas en el marco del régimen EXPORTA SIMPLE, independientemente del tipo de bien exportado · props: `{"tipo": "otra"}` · tramo [exacta]: «El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse»
- **ob1 Obligacion** «Plazo 365 días corridos — EXPORTA SIMPLE» — El ingreso y liquidación de las divisas por el mercado de cambios debe concretarse dentro de 365 días corridos, a computar desde la fecha del cumplido de embarque otorgado por la Aduana, para las operaciones concretadas en el marco del régimen EXPORTA SIMPLE, independientemente del tipo de bien exportado · props: `{"tipo": "otra"}` · umbral: ['365 (trescientos sesenta y cinco) días corridos'] · tramo [exacta]: «El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse en los siguientes plazos a computar desde la fecha del cumplido de embarque otorgado por la Aduana: […] 365 (trescientos sesenta y cinco) días corridos para las operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE", ind…»
- R: ob1 Obligacion —regula→ op1 Operacion

### A — omisiones de T4 a clasificar

- sin_marca:10 → entidades: ob1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código H

- **op1 Operacion** «Ingreso y liquidación de divisas de exportaciones EXPORTA SIMPLE» — Ingreso al país y liquidación en el mercado de cambios del contravalor en divisas de exportaciones de bienes oficializadas a partir del 02/09/19 concretadas en el marco del régimen EXPORTA SIMPLE, independientemente del tipo de bien exportado. · props: `{"tipo": "ingreso y liquidación de divisas de exportación"}` · tramo [exacta]: «El contravalor en divisas de la exportación hasta alcanzar el valor facturado según la condición de venta pactada deberá ingresarse al país y liquidarse en el mercado de cambios.»
- **ob1 Obligacion** «Plazo 365 días corridos — EXPORTA SIMPLE» — El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse dentro de 365 días corridos, a computar desde la fecha del cumplido de embarque otorgado por la Aduana, para las operaciones concretadas en el marco del régimen EXPORTA SIMPLE, independientemente del tipo de bien exportado. · props: `{"tipo": "otra"}` · umbral: ['365 (trescientos sesenta y cinco) días corridos'] · tramo [exacta]: «El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse en los siguientes plazos a computar desde la fecha del cumplido de embarque otorgado por la Aduana: […] 365 (trescientos sesenta y cinco) días corridos para las operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE", ind…»
- R: ob1 Obligacion —regula→ op1 Operacion

### H — omisiones de T4 a clasificar

- sin_marca:10 → entidades: ob1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código K

- **e1 Obligacion** «Plazo 365 días EXPORTA SIMPLE — ingreso y liquidación divisas» — El ingreso y la liquidación por el mercado de cambios de las divisas de exportaciones de bienes oficializadas a partir del 02/09/19 deberá concretarse dentro de 365 días corridos, contados desde la fecha del cumplido de embarque otorgado por la Aduana, en las operaciones concretadas en el marco del régimen "EXPORTA SIMPLE", sea cual sea el tipo de bien exportado. · props: `{"tipo": "otra"}` · umbral: ['365 (trescientos sesenta y cinco) días corridos'] · tramo [exacta]: «El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse en los siguientes plazos a computar desde la fecha del cumplido de embarque otorgado por la Aduana: […] 365 (trescientos sesenta y cinco) días corridos para las operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE", ind…»
- **e2 Operacion** «Ingreso y liquidación divisas exportación EXPORTA SIMPLE» — Ingreso y liquidación en el mercado de cambios del contravalor de exportaciones de bienes concretadas en el marco del régimen EXPORTA SIMPLE, sea cual sea el tipo de bien · props: `{"tipo": "ingreso y liquidación de divisas de exportación"}` · tramo [exacta]: «operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE"»
- R: e1 Obligacion —regula→ e2 Operacion

### K — omisiones de T4 a clasificar

- sin_marca:10 → entidades: e1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código W

- **e1 Obligacion** «Plazo 365 días EXPORTA SIMPLE — ingreso y liquidación» — El ingreso y liquidación por el mercado de cambios de las divisas de exportaciones de bienes oficializadas a partir del 02/09/19 debe concretarse dentro de 365 días corridos desde el cumplido de embarque otorgado por la Aduana, para las operaciones concretadas en el marco del régimen "EXPORTA SIMPLE", sin importar el tipo de bien exportado. · props: `{"tipo": "otra"}` · umbral: ['365 (trescientos sesenta y cinco) días corridos'] · tramo [exacta]: «El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse en los siguientes plazos a computar desde la fecha del cumplido de embarque otorgado por la Aduana: […] 365 (trescientos sesenta y cinco) días corridos para las operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE", ind…»
- **e2 Operacion** «Ingreso y liquidación de divisas — exportación EXPORTA SIMPLE» — Ingreso y liquidación en el mercado de cambios del contravalor de exportaciones de bienes concretadas en el régimen "EXPORTA SIMPLE", cualquiera sea el bien exportado. · props: `{"tipo": "ingreso y liquidación de divisas de exportación"}` · tramo [exacta]: «operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE"»
- R: e1 Obligacion —regula→ e2 Operacion

### W — omisiones de T4 a clasificar

- sin_marca:10 → entidades: e1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

