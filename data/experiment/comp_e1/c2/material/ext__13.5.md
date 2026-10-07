# `ext::13.5` — Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas por entidades

Grupos: omisiones. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 13. Pagos de servicios prestados por no residentes.
> *propio:* 13.5. Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas por entidades financieras para garantizar importaciones de servicios. Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios, en la medida que se verifique que cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada. En particular, en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23 y el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le corresponde al servicio por el punto 13.2. más otros 15 (quince) días corridos a la fecha estimada de prestación o devengamiento del servicio. En caso de tratarse una operación del concepto "S30. Servicios de fletes por operaciones de importaciones de bienes" que encuadra en lo previsto en el punto 10.10.2.1., debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar 15 (quince) días corridos a la fecha estimada de embarque de los bienes en origen.

## Omisiones leídas en T4 (M2)

sin_marca:24 [normativa; propio] «En particular, en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»

## Código A

- **op1 Operacion** «Pago propio por cartas de crédito o letras avaladas — importación de servicios» — Pagos propios de entidades financieras, con acceso al mercado de cambios, por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios. · props: `{"tipo": "pago al exterior"}` · tramo [exacta]: «cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios»
- **pot1 Potestad** «Acceso al mercado de cambios para pagos propios por cartas de crédito o letras avaladas» — Las entidades financieras tienen acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de servicios. · tramo [exacta]: «Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios»
- **c1 Condicion** «Cumplimiento de condiciones aplicables a la fecha de emisión» — Se verifique que cumplían las condiciones aplicables según la fecha de emisión u otorgamiento de la carta de crédito o letra avalada. · tramo [exacta]: «en la medida que se verifique que cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada»
- **ob1 Obligacion** «Contar con documentación del servicio y pago garantizado (desde 13/12/23)» — Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad debe contar con documentación que demuestre que al emitirse la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23 y que el pago debía concretarse desde la fecha resultante de adicionar el plazo del punto 13.2 más 15 días corridos a la fecha estimada de prestación… · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos a la fecha estimada de prestación o devengam…'] · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23 y el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días …»
- **ob2 Obligacion** «Pago S30 fletes importación: 15 días desde embarque estimado» — Para operaciones del concepto S30 (fletes por importaciones de bienes) que encuadran en el punto 10.10.2.1., el pago garantizado debía ser concretado por el cliente a partir de la fecha resultante de adicionar 15 días corridos a la fecha estimada de embarque de los bienes en origen; la entidad debe contar con la documentación que lo demuestre. · props: `{"tipo": "otra"}` · umbral: ['adicionar 15 (quince) días corridos a la fecha estimada de embarque de los biene…'] · tramo [exacta]: «En caso de tratarse una operación del concepto "S30. Servicios de fletes por operaciones de importaciones de bienes" que encuadra en lo previsto en el punto 10.10.2.1., debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar 15 (quince) días corridos a la fecha estimada de embarque de los bi…»
- R: pot1 Potestad —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- R: ob1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad»)
- R: ob2 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- R: Sujeto_entidad_financiera (mención «Las entidades financieras») —ejecuta→ op1 Operacion
- R: c1 Condicion —condicion_de→ pot1 Potestad
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion

### A — omisiones de T4 a clasificar

- sin_marca:24 → entidades: op1 Operacion [exacta] solap 0.5; pot1 Potestad [exacta] solap 0.5; ob1 Obligacion [exacta] solap 0.33 | omisiones: —

## Código H

- **op1 Operacion** «Pago propio por cartas de crédito o letras avaladas — importación de servicios» — Pagos propios de las entidades financieras por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios, cursados con acceso al mercado de cambios · props: `{"tipo": "pago al exterior"}` · tramo [exacta]: «cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios»
- **pot1 Potestad** «Acceso al mercado de cambios — pagos propios por cartas de crédito» — Las entidades financieras tienen acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de servicios · tramo [exacta]: «Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios»
- **c1 Condicion** «Cumplimiento de condiciones vigentes a la fecha de emisión» — Que se verifique que se cumplían las condiciones aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada · tramo [exacta]: «en la medida que se verifique que cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada»
- **ob1 Obligacion** «Contar con documentación — cartas de crédito desde 13/12/23» — Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad debe contar con documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23 y que el pago garantizado debía ser concretado por el cliente a partir de la fecha resultante de adicionar el plazo en días… · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos a la fecha estimada de prestación o devengam…'] · tramo [exacta]: «En particular, en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23»
- **ob2 Obligacion** «Documentación — fletes S30 de importación de bienes» — Para operaciones del concepto S30 (fletes por importaciones de bienes) que encuadran en el punto 10.10.2.1., el pago debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar 15 días corridos a la fecha estimada de embarque de los bienes en origen; la entidad debe contar con la documentación que lo demuestre · props: `{"tipo": "otra"}` · umbral: ['adicionar 15 (quince) días corridos a la fecha estimada de embarque de los biene…'] · tramo [exacta]: «En caso de tratarse una operación del concepto "S30. Servicios de fletes por operaciones de importaciones de bienes" que encuadra en lo previsto en el punto 10.10.2.1., debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar 15 (quince) días corridos a la fecha estimada de embarque de los bi…»
- R: pot1 Potestad —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- R: ob1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad»)
- R: ob2 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- R: Sujeto_entidad_financiera (mención «Las entidades financieras») —ejecuta→ op1 Operacion
- R: c1 Condicion —condicion_de→ pot1 Potestad
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion

### H — omisiones de T4 a clasificar

- sin_marca:24 → entidades: ob1 Obligacion [exacta] solap 1.0 contiene; op1 Operacion [exacta] solap 0.5 | omisiones: —

## Código K

- **op1 Operacion** «Acceso MLC: pago propio cartas de crédito/letras avaladas» — Acceso de las entidades financieras al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de servicios · props: `{"tipo": "acceso al mercado de cambios"}` · tramo [exacta]: «Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios»
- **p1 Potestad** «Acceso MLC entidades por pagos propios de garantías» — Las entidades financieras pueden acceder al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas que garantizan importaciones de servicios. · tramo [exacta]: «Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios»
- **c1 Condicion** «Cumplimiento de condiciones vigentes a la emisión» — Que se verifique que las cartas de crédito o letras avaladas cumplían las condiciones aplicables según su fecha de emisión u otorgamiento. · tramo [exacta]: «en la medida que se verifique que cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada»
- **o1 Obligacion** «Documentación servicio y plazo — garantías desde 13/12/23» — Para cartas de crédito o letras avaladas emitidas desde el 13/12/23, la entidad debe contar con documentación que demuestre que, al momento de apertura o emisión, el servicio garantizado era prestado o devengado desde el 13/12/23 y el pago debía concretarse por el cliente a partir del plazo del punto 13.2 más 15 días corridos desde la fecha estimada de prestación o devengamiento (para fletes S30 e… · props: `{"tipo": "otra"}` · umbral: ['el plazo en días corridos que le corresponde al servicio por el punto 13.2. más …', 'adicionar 15 (quince) días corridos a la fecha estimada de embarque de los biene…'] · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23»
- **c2 Condicion** «Garantías emitidas desde el 13/12/23» — Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23. · tramo [exacta]: «en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»
- **c3 Condicion** «Fletes S30 encuadrados en punto 10.10.2.1.» — Operación del concepto S30 fletes por importaciones de bienes encuadrada en 10.10.2.1.; aplica el plazo de 15 días desde el embarque. · tramo [exacta]: «En caso de tratarse una operación del concepto "S30. Servicios de fletes por operaciones de importaciones de bienes" que encuadra en lo previsto en el punto 10.10.2.1.»
- R: p1 Potestad —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- R: Sujeto_entidad_financiera (mención «Las entidades financieras») —ejecuta→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ o1 Obligacion
- R: c3 Condicion —condicion_de→ o1 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion

### K — omisiones de T4 a clasificar

- sin_marca:24 → entidades: c2 Condicion [exacta] solap 0.92 contenido_en; op1 Operacion [exacta] solap 0.5; o1 Obligacion [exacta] solap 0.33 | omisiones: —

## Código W

- **op1 Operacion** «Pagos propios por cartas de crédito/letras avaladas de importación de servicios» — Acceso al mercado de cambios de entidades financieras para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de servicios · props: `{"tipo": "acceso al mercado de cambios"}` · tramo [exacta]: «tendrán acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios»
- **p1 Potestad** «Acceso al MLC — pagos propios por cartas de crédito» — Las entidades financieras pueden acceder al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas que garantizan importaciones de servicios · tramo [exacta]: «Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios»
- **c1 Condicion** «Cumplimiento de condiciones vigentes a la emisión» — Se verifique que las operaciones cumplían las condiciones aplicables según la fecha de emisión u otorgamiento de la carta de crédito o letra avalada · tramo [exacta]: «en la medida que se verifique que cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada»
- **c2 Condicion** «Carta de crédito emitida desde 13/12/23» — Supuesto de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23 · tramo [exacta]: «en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»
- **o1 Obligacion** «Documentación de servicio y plazo de pago garantizado» — La entidad debe contar con documentación que demuestre que, al apertura/emisión, el servicio garantizado fue prestado o devengado desde el 13/12/23 y que el pago garantizado debía concretarse a partir de la fecha estimada de prestación o devengamiento más el plazo del punto 13.2 más 15 días corridos · props: `{"tipo": "otra", "umbrales": [{"tramo": "el plazo en días corridos que le corresponde al servicio por el punto 13.2.", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['el plazo en días corridos que le corresponde al servicio por el punto 13.2.', 'más otros 15 (quince) días corridos a la fecha estimada de prestación o devengam…'] · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23 y el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días …»
- **c3 Condicion** «Fletes S30 encuadrados en punto 10.10.2.1.» — Operación del concepto S30 fletes por importaciones de bienes encuadrada en el punto 10.10.2.1. · tramo [exacta]: «En caso de tratarse una operación del concepto "S30. Servicios de fletes por operaciones de importaciones de bienes" que encuadra en lo previsto en el punto 10.10.2.1.»
- **o2 Obligacion** «Fletes S30: pago desde embarque más 15 días» — Para fletes S30 del punto 10.10.2.1., la entidad debe contar con documentación que demuestre que el pago garantizado debía concretarse a partir de la fecha estimada de embarque más 15 días corridos · props: `{"tipo": "otra"}` · umbral: ['adicionar 15 (quince) días corridos a la fecha estimada de embarque de los biene…'] · tramo [exacta]: «debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar 15 (quince) días corridos a la fecha estimada de embarque de los bienes en origen»
- R: p1 Potestad —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- R: Sujeto_entidad_financiera (mención «Las entidades financieras») —ejecuta→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ o1 Obligacion
- R: c3 Condicion —condicion_de→ o2 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o2 Obligacion —condiciona→ op1 Operacion

### W — omisiones de T4 a clasificar

- sin_marca:24 → entidades: c2 Condicion [exacta] solap 0.92 contenido_en; op1 Operacion [exacta] solap 0.5; o1 Obligacion [exacta] solap 0.33 | omisiones: —

