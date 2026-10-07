# `ext::10.4.4` — Cancelación de garantías comerciales de importaciones de bienes otorgadas por

Grupos: grupo_c. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.4. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente.
> *propio:* 10.4.4. Cancelación de garantías comerciales de importaciones de bienes otorgadas por entidades financieras locales. La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero pendiente, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente, en la medida que se verifique que se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad. En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha y, salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país. Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2. Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914. El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B11. Cancelación de garantías comerciales de entidades financieras de importaciones de bienes sin registro de ingreso aduanero". Por los pagos que se realicen, la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuado el pago. En la medida que la entidad no cuente con el registro de la oficialización del despacho de importación dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cambios, la entidad deberá efectuar la correspondiente denuncia.

## Supuestos de la fase A de T4 (M1)

1. «emitidas desde el 13/12/23»
2. «desde el 14/04/25»
3. «con pagos a la vista»
4. «sin oficialización a 90 días»

## Código A

- **c7914 Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- **op1 Operacion** «Cancelación de cartas de crédito o letras avaladas (importaciones)» — Acceso al mercado de cambios por la entidad para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de bienes con registro aduanero pendiente, incluso cuando no se cumplan los requisitos de acceso del cliente · props: `{"tipo": "compra de moneda extranjera para cancelar garantías comerciales"}` · tramo [exacta]: «cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero pendiente»
- **pot1 Potestad** «Acceso al mercado de cambios para cancelar garantías» — La entidad tiene acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas, incluso cuando no se cumplan los requisitos de acceso del cliente · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas»
- **cond1 Condicion** «Condiciones aplicables según fecha y tipo de operación» — Se verifica que se cumplían las condiciones aplicables según la fecha de emisión u otorgamiento y el tipo de operación garantizada · tramo [exacta]: «en la medida que se verifique que se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad»
- **ob1 Obligacion** «Contar con documentación de la operación garantizada (desde 13/12/23)» — Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, contar con documentación que demuestre que al momento de la apertura o emisión la operación garantizada era una importación con registro de ingreso aduanero a partir de dicha fecha y, salvo la situación del punto 10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la fecha resultan… · props: `{"tipo": "otra"}` · umbral: ['otros 15 (quince) días corridos'] · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha»
- **exc1 Excepcion** «Salvo situación del punto 10.10.2.11» — Exceptúa de demostrar que el pago garantizado debía concretarse a partir de la fecha de arribo más plazo, cuando la operación queda comprendida en el punto 10.10.2.11. · tramo [exacta]: «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- **pot2 Potestad** «Admisión de pago desde fecha estimada de embarque (desde 14/04/25)» — Para emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, se admite que el pago garantizado tuviera que concretarse desde la fecha estimada de embarque cuando correspondía a la porción de una operación con pagos a la vista según puntos 10.10.2.1. o 10.10.2.2. · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen»
- **cond2 Condicion** «Cumplimiento de las restantes condiciones» — Se cumplen las restantes condiciones; aplica a cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14/04/25 · tramo [exacta]: «en la medida que se cumplan las restantes condiciones»
- **ob2 Obligacion** «Boleto de venta a nombre de la entidad, concepto B11» — El boleto de venta se efectúa a nombre de la propia entidad en calidad de cliente por el concepto B11 · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B11. Cancelación de garantías comerciales de entidades financieras de importaciones de bienes sin registro de ingreso aduanero".»
- **ob3 Obligacion** «Informar CUIT del importador en SEPAIMPO en 5 días hábiles» — Por los pagos realizados, informar en el SEPAIMPO la CUIT del importador por el cual se efectuó el pago · props: `{"tipo": "reporte_al_supervisor"}` · umbral: ['dentro de los 5 (cinco) días hábiles'] · tramo [exacta]: «la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuado el pago»
- **cond3 Condicion** «Sin registro de oficialización a 90 días corridos» — La entidad no cuenta con el registro de la oficialización del despacho de importación dentro de los 90 días corridos de la fecha de acceso al mercado de cambios · umbral: ['dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cam…'] · tramo [exacta]: «En la medida que la entidad no cuente con el registro de la oficialización del despacho de importación dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cambios»
- **ob4 Obligacion** «Efectuar denuncia por falta de registro de despacho» — Efectuar la correspondiente denuncia cuando no se cuente con el registro de la oficialización del despacho de importación dentro de los 90 días corridos · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «la entidad deberá efectuar la correspondiente denuncia»
- R: to TextoOrdenado —referencia→ c7914 Comunicacion
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion
- R: pot1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: ob1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: ob2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la propia entidad»)
- R: ob3 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: ob4 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: cond1 Condicion —condicion_de→ pot1 Potestad
- R: cond2 Condicion —condicion_de→ pot2 Potestad
- R: cond3 Condicion —condicion_de→ ob4 Obligacion
- R: exc1 Excepcion —exceptua_obligacion→ ob1 Obligacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion
- Omisión `meta_normativo` [exacta]: «Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914.» — Declaración informativa/remisión sobre dónde se receptaron condiciones históricas; no prescribe conducta.

### A — supuestos a clasificar

- 1. «emitidas desde el 13/12/23» → candidatos: ob1 Obligacion (1.00), cond2 Condicion (0.25), op1 Operacion (0.25), pot2 Potestad (0.25)
- 2. «desde el 14/04/25» → candidatos: cond2 Condicion (1.00), pot2 Potestad (1.00)
- 3. «con pagos a la vista» → candidatos: pot2 Potestad (1.00), ob3 Obligacion (0.50)
- 4. «sin oficialización a 90 días» → candidatos: cond3 Condicion (1.00), ob4 Obligacion (1.00), ob1 Obligacion (0.33), ob3 Obligacion (0.33)

## Código H

- **com1 Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- **op1 Operacion** «Acceso al mercado de cambios para cancelar garantías comerciales de importaciones con registro aduanero pendiente» — Acceso al mercado de cambios por la entidad para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de bienes con registro aduanero pendiente, incluso cuando no se cumplan los requisitos de acceso del cliente · props: `{"tipo": "compra de moneda extranjera / acceso al mercado de cambios"}` · tramo [exacta]: «tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero pendiente»
- **pot1 Potestad** «Acceso al mercado de cambios para cancelar garantías» — La entidad tiene acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas que garantizan importaciones de bienes con registro aduanero pendiente, incluso cuando no se cumplan los requisitos de acceso del cliente · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas»
- **cond1 Condicion** «Verificar condiciones vigentes a la fecha de emisión» — Se verifica que se cumplían las condiciones aplicables según la fecha de emisión u otorgamiento de la carta de crédito o letra avalada y el tipo de operación garantizada · tramo [exacta]: «en la medida que se verifique que se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad»
- **ob1 Obligacion** «Contar con documentación de la operación garantizada (desde 13/12/23)» — Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, contar con documentación que demuestre que al momento de la apertura o emisión la operación garantizada correspondía a una importación con registro de ingreso aduanero a partir de dicha fecha y, salvo que quedase comprendida en el punto 10.10.2.11., que el pago garantizado debía ser concretado por el cliente a par… · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes …'] · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha»
- **pot2 Potestad** «Admisión de pago desde fecha estimada de embarque (desde 14/04/25)» — Para emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, se admite que el pago garantizado debiera concretarse a partir de la fecha estimada de embarque cuando correspondía a la porción de una operación por la cual el cliente pudo realizar pagos a la vista según los puntos 10.10.2.1. o 10.10.2.2. · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen»
- **ob2 Obligacion** «Boleto de venta a nombre de la entidad, concepto B11» — El boleto de venta debe efectuarse a nombre de la propia entidad en calidad de cliente por el concepto B11. Cancelación de garantías comerciales de entidades financieras de importaciones de bienes sin registro de ingreso aduanero · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B11. Cancelación de garantías comerciales de entidades financieras de importaciones de bienes sin registro de ingreso aduanero".»
- **ob3 Obligacion** «Informar CUIT del importador en SEPAIMPO en 5 días hábiles» — Por los pagos realizados, informar en el SEPAIMPO la CUIT del importador por el cual se efectuó el pago · props: `{"tipo": "reporte_al_supervisor"}` · umbral: ['dentro de los 5 (cinco) días hábiles'] · tramo [exacta]: «la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuado el pago»
- **cond2 Condicion** «Sin registro de oficialización del despacho a 90 días» — La entidad no cuenta con el registro de la oficialización del despacho de importación dentro de los 90 días corridos de la fecha de acceso al mercado de cambios · umbral: ['dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cam…'] · tramo [exacta]: «En la medida que la entidad no cuente con el registro de la oficialización del despacho de importación dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cambios»
- **ob4 Obligacion** «Efectuar denuncia por falta de registro de despacho» — Efectuar la correspondiente denuncia cuando la entidad no cuente con el registro de la oficialización del despacho de importación dentro de los 90 días corridos de la fecha de acceso al mercado de cambios · props: `{"tipo": "otra"}` · tramo [exacta]: «la entidad deberá efectuar la correspondiente denuncia»
- R: to TextoOrdenado —referencia→ com1 Comunicacion
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion
- R: pot1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: ob1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: ob2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la propia entidad»)
- R: ob3 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: ob4 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: cond1 Condicion —condicion_de→ pot1 Potestad
- R: cond2 Condicion —condicion_de→ ob4 Obligacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: op1 Operacion —requiere→ ob3 Obligacion
- Omisión `meta_normativo` [exacta]: «Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914.» — Enunciado informativo/remisión histórica sobre dónde se receptaron las condiciones; no prescribe conducta.

### H — supuestos a clasificar

- 1. «emitidas desde el 13/12/23» → candidatos: ob1 Obligacion (1.00), op1 Operacion (0.25), pot2 Potestad (0.25)
- 2. «desde el 14/04/25» → candidatos: pot2 Potestad (1.00)
- 3. «con pagos a la vista» → candidatos: pot2 Potestad (1.00), ob3 Obligacion (0.50)
- 4. «sin oficialización a 90 días» → candidatos: cond2 Condicion (1.00), ob4 Obligacion (1.00), ob1 Obligacion (0.33), ob3 Obligacion (0.33)

## Código K

- **c1 Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- **op1 Operacion** «Acceso al MLC para cancelar garantías comerciales de importación» — Acceso de la entidad al mercado de cambios para cancelar cartas de crédito o letras avaladas que emitió u otorgó para garantizar importaciones de bienes con registro aduanero pendiente, incluso cuando no se cumplan los requisitos de acceso del cliente · props: `{"tipo": "acceso al mercado de cambios"}` · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero pendiente»
- **p1 Potestad** «Acceso propio aun sin requisitos del cliente» — La entidad puede acceder al mercado de cambios para cancelar las garantías comerciales que otorgó para importaciones de bienes con registro aduanero pendiente, incluso si no se cumplen los requisitos de acceso del cliente · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero pendiente, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente»
- **cd1 Condicion** «Condiciones vigentes a la fecha de emisión» — Que se verifique que se cumplían las condiciones aplicables según la fecha de emisión u otorgamiento de la garantía y el tipo de operación garantizada · tramo [exacta]: «en la medida que se verifique que se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada»
- **cd2 Condicion** «Garantías emitidas desde el 13/12/23» — Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23 · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»
- **o1 Obligacion** «Documentación de registro de ingreso desde 13/12/23» — La entidad debe contar con documentación que demuestre que, al abrirse o emitirse la garantía, la operación garantizada era una importación de bienes con registro de ingreso aduanero a partir del 13/12/23 · props: `{"tipo": "otra"}` · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha»
- **o2 Obligacion** «Documentación de plazo de pago garantizado» — Para garantías desde el 13/12/23, la entidad debe contar con documentación que demuestre que el pago garantizado debía concretarse a partir de la fecha estimada de arribo más el plazo del punto 10.10.1 más 15 días corridos · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes …'] · tramo [exacta]: «que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país»
- **x1 Excepcion** «Situación del punto 10.10.2.11 — plazo de pago» — No se exige documentar el plazo de pago garantizado si la operación está comprendida en el punto 10.10.2.11 · tramo [exacta]: «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- **p2 Potestad** «Pago desde embarque admitido desde 14/04/25» — Para garantías emitidas desde el 14/04/25, se admite que el pago garantizado debiera concretarse desde la fecha estimada de embarque cuando correspondía a la porción por la que el cliente podía pagar a la vista según 10.10.2.1 o 10.10.2.2, cumpliéndose las restantes condiciones · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen»
- **cd3 Condicion** «Garantías emitidas desde el 14/04/25» — Garantías emitidas u otorgadas a partir del 14/04/25 · tramo [exacta]: «Para aquellas emitidas u otorgadas a partir del 14/04/25»
- **cd4 Condicion** «Porción con pago a la vista admitido» — Que el pago corresponda a la porción por la que el cliente podía pagar a la vista según 10.10.2.1 o 10.10.2.2 · tramo [exacta]: «cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2.»
- **cd5 Condicion** «Cumplimiento de restantes condiciones» — Que se cumplan las restantes condiciones · tramo [exacta]: «en la medida que se cumplan las restantes condiciones»
- **o3 Obligacion** «Boleto a nombre de la entidad concepto B11» — El boleto de venta debe hacerse a nombre de la propia entidad como cliente, concepto B11 · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B11. Cancelación de garantías comerciales de entidades financieras de importaciones de bienes sin registro de ingreso aduanero"»
- **o4 Obligacion** «Informar CUIT del importador en SEPAIMPO» — Por los pagos realizados, la entidad debe informar en el SEPAIMPO la CUIT del importador dentro de 5 días hábiles · props: `{"tipo": "reporte_al_supervisor"}` · umbral: ['dentro de los 5 (cinco) días hábiles'] · tramo [exacta]: «Por los pagos que se realicen, la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuado el pago»
- **o5 Obligacion** «Denuncia por falta de oficialización del despacho» — La entidad debe efectuar la denuncia si no cuenta con el registro de oficialización del despacho dentro de 90 días corridos del acceso · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «la entidad deberá efectuar la correspondiente denuncia»
- **cd6 Condicion** «Sin oficialización del despacho en 90 días» — Que la entidad no cuente con el registro de oficialización del despacho dentro de 90 días corridos del acceso · umbral: ['dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cam…'] · tramo [exacta]: «En la medida que la entidad no cuente con el registro de la oficialización del despacho de importación dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cambios»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: cd1 Condicion —condicion_de→ p1 Potestad
- R: cd2 Condicion —condicion_de→ o1 Obligacion
- R: cd2 Condicion —condicion_de→ o2 Obligacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o2 Obligacion —condiciona→ op1 Operacion
- R: x1 Excepcion —exceptua_obligacion→ o2 Obligacion
- R: cd3 Condicion —condicion_de→ p2 Potestad
- R: cd4 Condicion —condicion_de→ p2 Potestad
- R: cd5 Condicion —condicion_de→ p2 Potestad
- R: o3 Obligacion —regula→ op1 Operacion
- R: op1 Operacion —requiere→ o4 Obligacion
- R: o4 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: op1 Operacion —requiere→ o5 Obligacion
- R: o5 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: cd6 Condicion —condicion_de→ o5 Obligacion
- Omisión `meta_normativo` [exacta]: «Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914.» — Nota histórica sobre dónde se recogieron condiciones previas; la Comunicación se extrajo como entidad.

### K — supuestos a clasificar

- 1. «emitidas desde el 13/12/23» → candidatos: cd2 Condicion (1.00), o1 Obligacion (0.75), o2 Obligacion (0.75), cd3 Condicion (0.25)
- 2. «desde el 14/04/25» → candidatos: cd3 Condicion (1.00), p2 Potestad (1.00)
- 3. «con pagos a la vista» → candidatos: cd4 Condicion (1.00), o4 Obligacion (0.50), p2 Potestad (0.50)
- 4. «sin oficialización a 90 días» → candidatos: cd6 Condicion (1.00), o5 Obligacion (1.00), o2 Obligacion (0.33), o4 Obligacion (0.33)

## Código W

- **op1 Operacion** «Acceso al MLC para cancelar garantías comerciales de importación» — Acceso de la entidad financiera local al mercado de cambios para cancelar cartas de crédito o letras avaladas que garantizan importaciones de bienes con registro aduanero pendiente, incluso sin cumplirse los requisitos para el acceso del cliente · props: `{"tipo": "acceso al mercado de cambios"}` · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero pendiente»
- **p1 Potestad** «Acceso propio de la entidad sin requisitos del cliente» — La entidad puede acceder al mercado de cambios para cancelar las garantías, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas»
- **c1 Condicion** «Cumplimiento de condiciones vigentes a la emisión» — Que se verifique que se cumplían las condiciones aplicables según la fecha de emisión de la garantía y el tipo de operación garantizada · tramo [exacta]: «en la medida que se verifique que se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada»
- **c2 Condicion** «Garantías emitidas desde 13/12/23» — Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23 · props: `{"umbrales": [{"tramo": "a partir del\n13/12/23", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['a partir del 13/12/23'] · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»
- **o1 Obligacion** «Documentación de importación con registro desde 13/12/23 y plazo de pago» — La entidad debe contar con documentación que demuestre que la operación garantizada era una importación con registro de ingreso a partir del 13/12/23 y que el pago garantizado debía concretarse a partir de la fecha estimada de arribo más el plazo del punto 10.10.1 más 15 días corridos · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes …'] · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha»
- **x1 Excepcion** «Situación del punto 10.10.2.11 — requisito de plazo de pago» — No se exige demostrar el plazo de pago diferido cuando la operación queda comprendida en el punto 10.10.2.11 · tramo [exacta]: «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- **x2 Excepcion** «Pago desde embarque para porción a la vista» — Para garantías emitidas desde 14/04/25, cumpliéndose las restantes condiciones, se admite que el pago garantizado se concrete desde la fecha estimada de embarque cuando corresponde a la porción por la que el cliente pudo pagar a la vista según 10.10.2.1 o 10.10.2.2 · props: `{"umbrales": [{"tramo": "a partir del 14/04/25", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['a partir del 14/04/25'] · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen»
- **c3 Condicion** «Porción con pagos a la vista admitidos» — Que el pago corresponda a la porción por la que el cliente pudo pagar a la vista según 10.10.2.1 o 10.10.2.2 · tramo [exacta]: «cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista»
- **o2 Obligacion** «Boleto a nombre propio concepto B11» — El boleto de venta se efectúa a nombre de la propia entidad como cliente por el concepto B11 · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente»
- **o3 Obligacion** «Informar CUIT del importador en SEPAIMPO» — Por los pagos realizados, informar en SEPAIMPO la CUIT del importador dentro de 5 días hábiles · props: `{"tipo": "reporte_al_supervisor"}` · umbral: ['dentro de los 5 (cinco) días hábiles'] · tramo [exacta]: «la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador»
- **o4 Obligacion** «Denuncia por falta de oficialización del despacho» — Si no cuenta con registro de oficialización del despacho dentro de 90 días corridos del acceso, la entidad debe efectuar la denuncia · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «la entidad deberá efectuar la correspondiente denuncia»
- **c4 Condicion** «Sin oficialización del despacho en 90 días» — Falta de registro de oficialización del despacho dentro de 90 días corridos del acceso · umbral: ['dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cam…'] · tramo [exacta]: «En la medida que la entidad no cuente con el registro de la oficialización del despacho de importación dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cambios»
- **cm Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- R: to TextoOrdenado —referencia→ cm Comunicacion
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ o1 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: x1 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: x2 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: c3 Condicion —condicion_de→ x2 Excepcion
- R: o2 Obligacion —regula→ op1 Operacion
- R: op1 Operacion —requiere→ o3 Obligacion
- R: o3 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: op1 Operacion —requiere→ o4 Obligacion
- R: o4 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: c4 Condicion —condicion_de→ o4 Obligacion

### W — supuestos a clasificar

- 1. «emitidas desde el 13/12/23» → candidatos: c2 Condicion (1.00), o1 Obligacion (0.75), op1 Operacion (0.25), x2 Excepcion (0.25)
- 2. «desde el 14/04/25» → candidatos: x2 Excepcion (1.00)
- 3. «con pagos a la vista» → candidatos: c3 Condicion (1.00), o3 Obligacion (0.50), x2 Excepcion (0.50)
- 4. «sin oficialización a 90 días» → candidatos: c4 Condicion (1.00), o4 Obligacion (1.00), o1 Obligacion (0.33), o3 Obligacion (0.33)

