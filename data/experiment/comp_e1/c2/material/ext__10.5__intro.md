# `ext::10.5::intro` — [bloque intro] Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente.

Grupos: omisiones. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.5. Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente.
> *propio:* Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 estará sujeto a un seguimiento desde la fecha de acceso al mercado de cambios hasta la fecha en que se produzca su regularización. Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento de ese pago, y por hasta el monto girado, la existencia de: i) el registro de ingreso aduanero a su nombre o a nombre de un tercero en la medida que se cumplan las condiciones establecidas en la presente normativa; y/o ii) la liquidación en el mercado de cambios de las divisas asociadas a la devolución del pago efectuado; y/o iii) otras formas de regularización previstas en la presente norma según las condiciones y límites establecidos en cada caso; y/o iv) la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la operación. El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago y deberá estar debidamente justificado por ésta.

## Omisiones leídas en T4 (M2)

sin_marca:4 [normativa; propio] «a los efectos cambiarios»

## Código A

- **op1 Operacion** «Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente» — Seguimiento de todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19, desde la fecha de acceso al mercado de cambios hasta la fecha de su regularización. · props: `{"tipo": "seguimiento de pagos"}` · tramo [exacta]: «Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 estará sujeto a un seguimiento desde la fecha de acceso al mercado de cambios hasta la fecha en que se produzca su regularización.»
- **def1 Definicion** «Pago regularizado a efectos cambiarios» — La situación de estos pagos se considera regularizada a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento, por hasta el monto girado, la existencia de: i) registro de ingreso aduanero a su nombre o a nombre de un tercero en la medida que se cumplan las condiciones de la normativa; y/o ii) liquidación en el mercado de cambios de las divisas asociadas a la devoluci… · props: `{"termino": "regularizada"}` · tramo [exacta]: «Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento de ese pago, y por hasta el monto girado, la existencia de:»
- **op2 Operacion** «Pedido de conformidad del BCRA para regularizar pago» — Pedido de conformidad al BCRA para dar por regularizada parte o el total de la operación de pago de importaciones con registro de ingreso aduanero pendiente. · props: `{"tipo": "otra"}` · tramo [exacta]: «la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la operación. El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago»
- **r1 Restriccion** «Solo la entidad encargada del seguimiento tramita el pedido» — El pedido de conformidad del BCRA solo podrá ser tramitado por la entidad encargada del seguimiento del pago. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago»
- **o1 Obligacion** «Justificar debidamente el pedido de conformidad» — El pedido de conformidad del BCRA debe estar debidamente justificado por la entidad encargada del seguimiento del pago. · props: `{"tipo": "otra"}` · tramo [exacta]: «deberá estar debidamente justificado por ésta»
- R: r1 Restriccion —limita→ op2 Operacion
- R: o1 Obligacion —regula→ op2 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto (mención «la entidad encargada del seguimiento del pago»)
- R: o1 Obligacion —aplica_a→ Sujeto (mención «la entidad encargada del seguimiento del pago»)

### A — omisiones de T4 a clasificar

- sin_marca:4 → entidades: def1 Definicion [exacta] solap 1.0 contiene | omisiones: —

## Código H

- **op1 Operacion** «Seguimiento de pagos de importaciones con registro aduanero pendiente» — Seguimiento de todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19, desde la fecha de acceso al mercado de cambios hasta la fecha de su regularización. · props: `{"tipo": "seguimiento de pagos"}` · tramo [exacta]: «Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 estará sujeto a un seguimiento desde la fecha de acceso al mercado de cambios hasta la fecha en que se produzca su regularización.»
- **def1 Definicion** «Regularización cambiaria de pagos con registro pendiente» — La situación de estos pagos se considera regularizada a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento, por hasta el monto girado, la existencia de: i) el registro de ingreso aduanero a su nombre o de un tercero, en la medida que se cumplan las condiciones de la normativa; y/o ii) la liquidación en el mercado de cambios de las divisas asociadas a la devolución… · props: `{"termino": "regularizada"}` · tramo [exacta]: «Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento de ese pago, y por hasta el monto girado, la existencia de:»
- **op2 Operacion** «Tramitación de pedido de conformidad BCRA» — Trámite ante el BCRA del pedido de conformidad para dar por regularizada parte o el total de la operación. · props: `{"tipo": "otra"}` · tramo [exacta]: «El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago»
- **r1 Restriccion** «Pedido de conformidad solo por entidad de seguimiento» — El pedido de conformidad del BCRA solo puede ser tramitado por la entidad encargada del seguimiento del pago. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago»
- **o1 Obligacion** «Justificación del pedido de conformidad» — El pedido de conformidad ante el BCRA debe estar debidamente justificado por la entidad encargada del seguimiento del pago. · props: `{"tipo": "otra"}` · tramo [exacta]: «deberá estar debidamente justificado por ésta»
- R: r1 Restriccion —limita→ op2 Operacion
- R: o1 Obligacion —regula→ op2 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto (mención «la entidad encargada del seguimiento del pago»)
- R: o1 Obligacion —aplica_a→ Sujeto (mención «la entidad encargada del seguimiento del pago»)

### H — omisiones de T4 a clasificar

- sin_marca:4 → entidades: def1 Definicion [exacta] solap 1.0 contiene | omisiones: —

## Código K

- **op1 Operacion** «Pago de importaciones con ingreso aduanero pendiente» — Pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 con acceso al mercado de cambios · props: `{"tipo": "pago de importaciones"}` · tramo [exacta]: «Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19»
- **ob1 Obligacion** «Seguimiento hasta regularización — pagos importaciones pendientes» — Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado desde el 02/09/19 está sujeto a seguimiento desde la fecha de acceso al mercado de cambios hasta su regularización · props: `{"tipo": "otra"}` · tramo [exacta]: «estará sujeto a un seguimiento desde la fecha de acceso al mercado de cambios hasta la fecha en que se produzca su regularización»
- **d1 Definicion** «Situación regularizada de pagos de importaciones» — La situación de los pagos se considera regularizada a efectos cambiarios cuando se demuestra ante la entidad encargada del seguimiento, por hasta el monto girado, alguno o varios de: (i) registro de ingreso aduanero a su nombre o de un tercero cumpliendo las condiciones normativas; (ii) liquidación en el mercado de cambios de divisas por devolución del pago; (iii) otras formas de regularización pr… · props: `{"termino": "regularizada"}` · tramo [exacta]: «Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento de ese pago, y por hasta el monto girado, la existencia de:»
- **c1 Condicion** «Registro de ingreso aduanero — regularización» — Supuesto alternativo (y/o) de regularización, por hasta el monto girado: registro de ingreso aduanero a nombre propio o de un tercero cumpliendo las condiciones normativas · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «el registro de ingreso aduanero a su nombre o a nombre de un tercero en la medida que se cumplan las condiciones establecidas en la presente normativa»
- **c2 Condicion** «Liquidación de divisas por devolución — regularización» — Supuesto alternativo (y/o) de regularización, por hasta el monto girado: liquidación en el mercado de cambios de las divisas asociadas a la devolución del pago · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «la liquidación en el mercado de cambios de las divisas asociadas a la devolución del pago efectuado»
- **c3 Condicion** «Otras formas previstas — regularización» — Supuesto alternativo (y/o) de regularización, por hasta el monto girado: otras formas previstas en la norma según sus condiciones y límites · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «otras formas de regularización previstas en la presente norma según las condiciones y límites establecidos en cada caso»
- **c4 Condicion** «Conformidad del BCRA — regularización» — Supuesto alternativo (y/o) de regularización, por hasta el monto girado: conformidad del BCRA para regularizar parte o el total de la operación · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la operación»
- **p1 Potestad** «Conformidad BCRA para regularizar operación» — El BCRA puede otorgar conformidad para dar por regularizada parte o el total de la operación · tramo [exacta]: «la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la operación»
- **op2 Operacion** «Pedido de conformidad al BCRA para regularizar» — Pedido de conformidad al BCRA para dar por regularizado un pago de importaciones con registro aduanero pendiente · props: `{"tipo": "solicitud de conformidad"}` · tramo [exacta]: «El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago»
- **r1 Restriccion** «Solo entidad de seguimiento tramita pedido» — El pedido de conformidad al BCRA solo puede ser tramitado por la entidad encargada del seguimiento del pago · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago»
- **ob2 Obligacion** «Justificación debida del pedido de conformidad» — El pedido de conformidad al BCRA debe estar debidamente justificado por la entidad encargada del seguimiento del pago · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «deberá estar debidamente justificado por ésta»
- R: op1 Operacion —requiere→ ob1 Obligacion
- R: p1 Potestad —aplica_a→ Sujeto_bcra (mención «BCRA»)
- R: r1 Restriccion —limita→ op2 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto (mención «la entidad encargada del seguimiento del pago»)
- R: Sujeto (mención «la entidad encargada del seguimiento del pago») —ejecuta→ op2 Operacion
- R: ob2 Obligacion —regula→ op2 Operacion
- R: ob2 Obligacion —aplica_a→ Sujeto (mención «la entidad encargada del seguimiento del pago»)
- Omisión `relacion_sin_predicado` [exacta]: «Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre» — Los supuestos de regularización ponen fin al seguimiento (Obligacion ob1); condicion_de sobre una Definicion (d1) no está admitido; se habría usado condicion_de hacia d1

### K — omisiones de T4 a clasificar

- sin_marca:4 → entidades: d1 Definicion [exacta] solap 1.0 contiene | omisiones: om#0 relacion_sin_predicado [exacta] solap 1.0 contiene

## Código W

- **op1 Operacion** «Pago de importaciones con ingreso aduanero pendiente» — Pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 con acceso al mercado de cambios · props: `{"tipo": "pago de importaciones"}` · tramo [exacta]: «Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19»
- **o1 Obligacion** «Seguimiento hasta regularización — pago de importaciones pendiente» — Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 queda sujeto a seguimiento desde la fecha de acceso al mercado de cambios hasta su regularización, a cargo de la entidad encargada del seguimiento. · props: `{"tipo": "otra"}` · tramo [exacta]: «estará sujeto a un seguimiento desde la fecha de acceso al mercado de cambios hasta la fecha en que se produzca su regularización»
- **d1 Definicion** «Situación regularizada de pagos de importaciones» — La situación de estos pagos se considera regularizada a efectos cambiarios cuando se demuestra ante la entidad encargada del seguimiento, por hasta el monto girado, la existencia de alguno o varios de: registro de ingreso aduanero (propio o de tercero, cumpliendo condiciones); liquidación de divisas por devolución del pago; otras formas de regularización previstas; conformidad del BCRA. · props: `{"termino": "regularizada"}` · tramo [exacta]: «Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento de ese pago, y por hasta el monto girado, la existencia de:»
- **c1 Condicion** «Registro de ingreso aduanero — regularización» — Existencia del registro de ingreso aduanero a nombre del importador o de un tercero, cumpliendo las condiciones de la normativa (supuesto alternativo, y/o). · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «el registro de ingreso aduanero a su nombre o a nombre de un tercero en la medida que se cumplan las condiciones establecidas en la presente normativa»
- **c2 Condicion** «Liquidación de divisas por devolución — regularización» — Liquidación en el mercado de cambios de las divisas asociadas a la devolución del pago (supuesto alternativo, y/o). · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «la liquidación en el mercado de cambios de las divisas asociadas a la devolución del pago efectuado»
- **c3 Condicion** «Otras formas previstas — regularización» — Otras formas de regularización previstas en la norma, según sus condiciones y límites (supuesto alternativo, y/o). · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «otras formas de regularización previstas en la presente norma según las condiciones y límites establecidos en cada caso»
- **c4 Condicion** «Conformidad del BCRA — regularización» — Conformidad del BCRA para dar por regularizada parte o el total de la operación (supuesto alternativo, y/o). · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la operación»
- **r1 Restriccion** «Pedido de conformidad solo por entidad de seguimiento» — El pedido de conformidad al BCRA solo puede ser tramitado por la entidad encargada del seguimiento del pago. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago»
- **op2 Operacion** «Pedido de conformidad de regularización al BCRA» — Tramitación ante el BCRA del pedido de conformidad para dar por regularizada parte o el total de la operación · props: `{"tipo": "solicitud"}` · tramo [exacta]: «El pedido solo podrá ser tramitado»
- **o2 Obligacion** «Justificación debida del pedido de conformidad» — La entidad encargada del seguimiento debe justificar debidamente el pedido de conformidad ante el BCRA. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «deberá estar debidamente justificado por ésta»
- **p1 Potestad** «Conformidad BCRA para regularizar operación» — El BCRA puede otorgar conformidad para dar por regularizada parte o el total de la operación. · tramo [exacta]: «la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la operación»
- R: op1 Operacion —requiere→ o1 Obligacion
- R: r1 Restriccion —limita→ op2 Operacion
- R: o2 Obligacion —regula→ op2 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad encargada del seguimiento del pago»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad encargada del seguimiento del pago»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «la entidad encargada del seguimiento del pago») —ejecuta→ op2 Operacion
- R: p1 Potestad —aplica_a→ Sujeto_bcra (mención «BCRA»)
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad encargada del seguimiento de ese pago»)
- Omisión `relacion_sin_predicado` [exacta]: «Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre» — Las condiciones i)-iv) son supuestos de la regularización (Definicion); condicion_de no admite Definicion como rango. Se habría usado condicion_de.
- Omisión `relacion_sin_predicado` [exacta]: «Se considerará regularizada la situación de estos pagos» — La regularización pone fin al seguimiento (Obligacion); no hay predicado para el término de una obligación.

### W — omisiones de T4 a clasificar

- sin_marca:4 → entidades: d1 Definicion [exacta] solap 1.0 contiene | omisiones: om#0 relacion_sin_predicado [exacta] solap 1.0 contiene

