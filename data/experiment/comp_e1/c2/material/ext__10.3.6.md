# `ext::10.3.6` — Pagos de importaciones con cartas de crédito o letras avaladas emitidas u otorgadas

Grupos: grupo_c. Estado final en la tanda 0: `aceptado_tras_reintento`.

## Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero.
> *propio:* 10.3.6. Pagos de importaciones con cartas de crédito o letras avaladas emitidas u otorgadas por entidades financieras locales. La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente, en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad. En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha y, salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país. Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2. Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914. El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero".

## Supuestos de la fase A de T4 (M1)

1. «emitidas desde el 13/12/23 (más 15 días)»
2. «desde el 14/04/25»
3. «con pagos a la vista»

## Código A

- **c7914 Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- **op1 Operacion** «Cancelación de cartas de crédito o letras avaladas de importaciones — acceso al mercado de cambios» — Cancelación por la entidad de cartas de crédito o letras avaladas emitidas u otorgadas por entidades financieras locales para garantizar importaciones de bienes con registro de ingreso aduanero, con acceso al mercado de cambios incluso sin cumplir los requisitos del cliente · props: `{"tipo": "compra de moneda extranjera para cancelar garantías"}` · tramo [exacta]: «cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes»
- **pot1 Potestad** «Acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas» — La entidad tiene acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de bienes con registro aduanero, incluso cuando no se cumplan los requisitos de acceso del cliente · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente»
- **cond1 Condicion** «Documentación que acredite condiciones aplicables a la emisión» — La entidad cuenta con documentación que demuestre que al momento de la apertura o emisión se cumplían las condiciones aplicables según la fecha de emisión u otorgamiento y el tipo de operación garantizada · tramo [exacta]: «en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad»
- **ob1 Obligacion** «Contar con documentación — emisiones desde 13/12/23» — Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad debe contar con documentación que demuestre que al momento de la apertura o emisión la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha y, salvo que la operación quedase comprendida en el punto 10.10.2.11., que el pago garantizado de… · props: `{"tipo": "otra"}` · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha»
- **exc1 Excepcion** «Excepción punto 10.10.2.11 — fecha de pago garantizado» — Exceptúa de la exigencia de documentación sobre la fecha desde la que el pago garantizado debía concretarse (plazo del punto 10.10.1. más 15 días corridos desde la fecha estimada de arribo) a las operaciones comprendidas en la situación del punto 10.10.2.11. · tramo [exacta]: «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- **cond2 Condicion** «Emisión u otorgamiento desde 14/04/25 y demás condiciones cumplidas» — Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones · tramo [exacta]: «Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones»
- **pot2 Potestad** «Admisión de pago garantizado desde fecha estimada de embarque más 15 días» — Para las emitidas u otorgadas a partir del 14/04/25 se admite que el pago garantizado debiera concretarse a partir de la fecha estimada de embarque en origen más 15 días corridos, cuando correspondía a la porción de una operación con pagos a la vista según los puntos 10.10.2.1. o 10.10.2.2. · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo p…»
- **ob2 Obligacion** «Boleto de venta a nombre de la entidad — concepto B14» — El boleto de venta debe efectuarse a nombre de la propia entidad en calidad de cliente por el concepto B14 Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero".»
- R: to TextoOrdenado —referencia→ c7914 Comunicacion
- R: pot1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: ob1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: pot2 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: ob2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la propia entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion
- R: cond1 Condicion —condicion_de→ pot1 Potestad
- R: cond2 Condicion —condicion_de→ pot2 Potestad
- R: exc1 Excepcion —exceptua_obligacion→ ob1 Obligacion
- R: ob2 Obligacion —regula→ op1 Operacion
- Omisión `meta_normativo` [exacta]: «Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914.» — Remisión informativa a una norma anterior: no prescribe conducta nueva.

### A — supuestos a clasificar

- 1. «emitidas desde el 13/12/23 (más 15 días)» → candidatos: ob1 Obligacion (1.00), pot2 Potestad (0.50), exc1 Excepcion (0.33), cond2 Condicion (0.17)
- 2. «desde el 14/04/25» → candidatos: cond2 Condicion (1.00), pot2 Potestad (1.00)
- 3. «con pagos a la vista» → candidatos: pot2 Potestad (1.00)

## Código H

- **c1 Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- **op1 Operacion** «Cancelación de cartas de crédito o letras avaladas» — Cancelación por la entidad de cartas de crédito o letras avaladas emitidas u otorgadas por entidades financieras locales para garantizar importaciones de bienes con registro de ingreso aduanero · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes»
- **p1 Potestad** «Acceso al mercado de cambios para cancelar garantías» — La entidad tiene acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de bienes con registro aduanero, incluso cuando no se cumplan los requisitos de acceso del cliente · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente»
- **cond1 Condicion** «Documentación de condiciones al momento de emisión» — Que la entidad cuente con la documentación que demuestre que, al momento de la apertura o emisión, se cumplían las condiciones aplicables según la fecha de emisión y el tipo de operación garantizada · tramo [exacta]: «en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad»
- **o1 Obligacion** «Contar con documentación (emitidas desde 13/12/23)» — Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad debe contar con documentación que demuestre que al momento de apertura o emisión la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha y, salvo que quedase comprendida en el punto 10.10.2.11., que el pago garantizado debía ser concreta… · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes …'] · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha»
- **p2 Potestad** «Admisión de pago desde embarque + 15 días (desde 14/04/25)» — Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14/04/25, también se admite que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque en origen más 15 días corridos, cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista según los puntos 10.10.2.1. o 10.10.2.2. · tramo [exacta]: «Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos»
- **cond2 Condicion** «Cumplimiento de las restantes condiciones» — Que se cumplan las restantes condiciones aplicables a las cartas de crédito o letras avaladas emitidas desde el 14/04/25 · tramo [exacta]: «en la medida que se cumplan las restantes condiciones»
- **o2 Obligacion** «Boleto de venta a nombre de la entidad, concepto B14» — El boleto de venta debe efectuarse a nombre de la propia entidad en calidad de cliente por el concepto B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero".»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: cond1 Condicion —condicion_de→ p1 Potestad
- R: cond2 Condicion —condicion_de→ p2 Potestad
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la propia entidad»)
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion
- Omisión `meta_normativo` [exacta]: «Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914.» — Remisión informativa a la norma anterior; no prescribe conducta.

### H — supuestos a clasificar

- 1. «emitidas desde el 13/12/23 (más 15 días)» → candidatos: o1 Obligacion (1.00), p2 Potestad (0.50), cond2 Condicion (0.17), op1 Operacion (0.17)
- 2. «desde el 14/04/25» → candidatos: cond2 Condicion (1.00), p2 Potestad (1.00)
- 3. «con pagos a la vista» → candidatos: p2 Potestad (1.00)

## Código K

- **op1 Operacion** «Cancelación por la entidad de cartas de crédito/letras avaladas de importación» — Acceso de la entidad financiera local al mercado de cambios para cancelar cartas de crédito o letras avaladas que emitió u otorgó para garantizar importaciones de bienes con registro aduanero · props: `{"tipo": "acceso al mercado de cambios"}` · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes»
- **p1 Potestad** «Acceso de la entidad para cancelar garantías de importación» — La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de bienes con registro aduanero, incluso cuando no se cumplan los requisitos para el acceso del cliente · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes»
- **c1 Condicion** «Documentación de cumplimiento de condiciones al emitir» — Que la entidad cuente con documentación que demuestre que al momento de apertura o emisión se cumplían las condiciones aplicables según la fecha de emisión y el tipo de operación garantizada · tramo [exacta]: «en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad»
- **o1 Obligacion** «Documentación post 13/12/23: registro aduanero y plazo de pago» — Para cartas de crédito o letras avaladas emitidas desde el 13/12/23, la entidad deberá contar con documentación que demuestre que la operación garantizada era una importación de bienes con registro de ingreso aduanero desde dicha fecha y que el pago garantizado debía concretarse a partir de la fecha estimada de arribo más el plazo del punto 10.10.1 más otros 15 días corridos · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes …'] · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que»
- **c2 Condicion** «Emisión a partir del 13/12/23» — Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23 · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»
- **x1 Excepcion** «Situación del punto 10.10.2.11 — requisito de plazo» — No se exige demostrar el plazo de pago (arribo + plazo 10.10.1 + 15 días) si la operación quedaba comprendida en el punto 10.10.2.11 · tramo [exacta]: «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- **x2 Excepcion** «Pago desde embarque + 15 días — emitidas desde 14/04/25» — Para emitidas desde el 14/04/25, se admite alternativamente que el pago garantizado debiera concretarse desde la fecha estimada de embarque más 15 días corridos, en vez del plazo desde arribo · umbral: ['más un plazo adicional de 15 (quince) días corridos'] · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos»
- **c3 Condicion** «Emisión a partir del 14/04/25» — Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14/04/25 · tramo [exacta]: «Para aquellas emitidas u otorgadas a partir del 14/04/25»
- **c4 Condicion** «Cumplimiento de restantes condiciones» — Que se cumplan las restantes condiciones · tramo [exacta]: «en la medida que se cumplan las restantes condiciones»
- **c5 Condicion** «Porción con pagos a la vista 10.10.2.1/10.10.2.2» — Que corresponda a la porción de la operación por la que el cliente hubiese podido pagar a la vista según 10.10.2.1 o 10.10.2.2 · tramo [exacta]: «cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2.»
- **o2 Obligacion** «Boleto a nombre de la entidad, concepto B14» — El boleto de venta debe efectuarse a nombre de la propia entidad en calidad de cliente por el concepto B14 · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero".»
- **com1 Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- R: to TextoOrdenado —referencia→ com1 Comunicacion
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: c2 Condicion —condicion_de→ o1 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: x1 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: x2 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: c3 Condicion —condicion_de→ x2 Excepcion
- R: c4 Condicion —condicion_de→ x2 Excepcion
- R: c5 Condicion —condicion_de→ x2 Excepcion
- R: o2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la propia entidad»)
- R: o2 Obligacion —regula→ op1 Operacion

### K — supuestos a clasificar

- 1. «emitidas desde el 13/12/23 (más 15 días)» → candidatos: o1 Obligacion (1.00), c2 Condicion (0.67), x2 Excepcion (0.50), x1 Excepcion (0.33)
- 2. «desde el 14/04/25» → candidatos: c3 Condicion (1.00), x2 Excepcion (1.00)
- 3. «con pagos a la vista» → candidatos: c5 Condicion (1.00)

## Código N

- **e1 Operacion** «Cancelación de cartas de crédito o letras avaladas» — Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes con registro aduanero · props: `{"tipo": "Acceso al mercado de cambios para cancelación de garantías comerciales"}` · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes»
- **e2 Condicion** «Documentación de cumplimiento de condiciones al momento de emisión» — La entidad debe contar con documentación que demuestre que al momento de la apertura o emisión se cumplían las condiciones aplicables según la fecha de emisión y el tipo de operación · tramo [exacta]: «en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad»
- **e3 Condicion** «Cartas de crédito o letras avaladas emitidas a partir del 13/12/23» — Aplica a cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13 de diciembre de 2023 · props: `{"umbrales": [{"tramo": "a partir del 13/12/23", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['a partir del 13/12/23'] · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»
- **e4 Obligacion** «Documentación de importación con registro aduanero a partir del 13/12/23» — La entidad deberá contar con documentación que demuestre que la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir del 13/12/23 · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha»
- **e5 Condicion** «Operación no comprendida en punto 10.10.2.11» — Salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11 · tramo [exacta]: «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- **e6 Obligacion** «Pago garantizado según plazo de bien más 15 días» — El pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1 más otros 15 días corridos a la fecha estimada de arribo de los bienes al país · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos'] · tramo [exacta]: «que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país»
- **e7 Condicion** «Cartas de crédito o letras avaladas emitidas a partir del 14/04/25» — Aplica a cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14 de abril de 2025 · props: `{"umbrales": [{"tramo": "a partir del 14/04/25", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['a partir del 14/04/25'] · tramo [exacta]: «Para aquellas emitidas u otorgadas a partir del 14/04/25»
- **e8 Excepcion** «Pago desde fecha estimada de embarque más 15 días» — Se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 días corridos cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista según los puntos 10.10.2.1 o 10.10.2.2 · umbral: ['más un plazo adicional de 15 (quince) días corridos'] · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo p…»
- **e9 Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- **e10 Obligacion** «Boleto de venta a nombre de la entidad» — El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto 'B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero' · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero".»
- R: e2 Condicion —condicion_de→ e1 Operacion
- R: e3 Condicion —condicion_de→ e4 Obligacion
- R: e5 Condicion —condicion_de→ e6 Obligacion
- R: e7 Condicion —condicion_de→ e8 Excepcion
- R: to TextoOrdenado —referencia→ e9 Comunicacion
- R: e1 Operacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: e4 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: e10 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la propia entidad»)
- Omisión `meta_normativo` [exacta]: «Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914.» — 

### N — supuestos a clasificar

- 1. «emitidas desde el 13/12/23 (más 15 días)» → candidatos: e3 Condicion (0.67), e4 Obligacion (0.50), e6 Obligacion (0.33), e8 Excepcion (0.33)
- 2. «desde el 14/04/25» → candidatos: e7 Condicion (1.00)
- 3. «con pagos a la vista» → candidatos: e8 Excepcion (1.00)

## Código W

- **op1 Operacion** «Cancelación de cartas de crédito o letras avaladas de importación» — Acceso de la entidad financiera local al mercado de cambios para cancelar cartas de crédito o letras avaladas que emitió u otorgó en garantía de importaciones de bienes con registro aduanero · props: `{"tipo": "acceso al mercado de cambios"}` · tramo [exacta]: «cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes»
- **p1 Potestad** «Acceso de la entidad para cancelar garantías de importación» — La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas que emitió u otorgó en garantía de importaciones de bienes con registro aduanero · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas»
- **x1 Excepcion** «Sin requisitos de acceso del cliente» — El acceso de la entidad corresponde aunque no se cumplan los requisitos fijados para el acceso del cliente · tramo [exacta]: «incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente»
- **c1 Condicion** «Documentación de condiciones vigentes al emitir» — La entidad debe contar con documentación que demuestre que, al abrir o emitir la garantía, se cumplían las condiciones aplicables según la fecha de emisión y el tipo de operación garantizada · tramo [exacta]: «en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad»
- **o1 Obligacion** «Documentar importación con registro desde 13/12/23» — Para garantías emitidas desde el 13/12/23, la entidad debe contar con documentación que demuestre que, al abrir o emitir la garantía, la operación garantizada era una importación de bienes con registro de ingreso aduanero desde esa fecha · props: `{"tipo": "otra"}` · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha»
- **c2 Condicion** «Garantías emitidas desde 13/12/23» — Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23 · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»
- **o2 Obligacion** «Documentar plazo de pago garantizado (10.10.1 + 15 días)» — Para garantías emitidas desde el 13/12/23, la entidad debe documentar que el cliente debía concretar el pago garantizado desde la fecha estimada de arribo más el plazo que fija el punto 10.10.1 para el bien más 15 días corridos · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes …'] · tramo [exacta]: «que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país»
- **x2 Excepcion** «Situación del punto 10.10.2.11» — La documentación del plazo de pago no se exige si la operación está comprendida en la situación del punto 10.10.2.11 · tramo [exacta]: «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- **x3 Excepcion** «Pago desde embarque + 15 días (desde 14/04/25)» — En las garantías emitidas desde el 14/04/25, en lugar del plazo desde el arribo se admite que el pago garantizado debiera hacerse desde la fecha estimada de embarque más 15 días corridos, para la porción que pudo pagarse a la vista por los puntos 10.10.2.1 o 10.10.2.2 · umbral: ['más un plazo adicional de 15 (quince) días corridos'] · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos»
- **c3 Condicion** «Garantías emitidas desde 14/04/25» — Garantías emitidas u otorgadas a partir del 14/04/25 · tramo [exacta]: «Para aquellas emitidas u otorgadas a partir del 14/04/25»
- **c4 Condicion** «Cumplimiento de las restantes condiciones» — Que se cumplan las restantes condiciones · tramo [exacta]: «en la medida que se cumplan las restantes condiciones»
- **c5 Condicion** «Porción pagable a la vista (10.10.2.1/2)» — Que el pago corresponda a la porción por la que el cliente pudo pagar a la vista según los puntos 10.10.2.1 o 10.10.2.2 · tramo [exacta]: «cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2.»
- **o3 Obligacion** «Boleto a nombre de la entidad, concepto B14» — El boleto de venta se hace a nombre de la propia entidad, como cliente, por el concepto B14 · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero"»
- **com1 Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- R: to TextoOrdenado —referencia→ com1 Comunicacion
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_entidad_financiera (mención «entidades financieras locales») —ejecuta→ op1 Operacion
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: c2 Condicion —condicion_de→ o1 Obligacion
- R: c2 Condicion —condicion_de→ o2 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o2 Obligacion —condiciona→ op1 Operacion
- R: x2 Excepcion —exceptua_obligacion→ o2 Obligacion
- R: x3 Excepcion —exceptua_obligacion→ o2 Obligacion
- R: c3 Condicion —condicion_de→ x3 Excepcion
- R: c4 Condicion —condicion_de→ x3 Excepcion
- R: c5 Condicion —condicion_de→ x3 Excepcion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la propia entidad»)
- Omisión `relacion_sin_predicado` [exacta]: «incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente» — La excepción releva de los requisitos de acceso del cliente, que no están en esta unidad; no hay exceptua hacia una Potestad

### W — supuestos a clasificar

- 1. «emitidas desde el 13/12/23 (más 15 días)» → candidatos: o2 Obligacion (1.00), c2 Condicion (0.67), o1 Obligacion (0.67), x3 Excepcion (0.50)
- 2. «desde el 14/04/25» → candidatos: c3 Condicion (1.00), x3 Excepcion (1.00)
- 3. «con pagos a la vista» → candidatos: c5 Condicion (1.00), x3 Excepcion (0.50)

