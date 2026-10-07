# `pagjub::2.2` — Modelo de nota de presentación de la rendición de cuentas.

Grupos: omisiones. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 2. Rendición de cuentas por parte de las entidades financieras.
> *propio:* 2.2. Modelo de nota de presentación de la rendición de cuentas. Fecha: De: (1) A: BANCO CENTRAL DE LA REPÚBLICA ARGENTINA. Remitimos a Uds. para su procesamiento, en los términos de las normas sobre "Pago de beneficios de la seguridad social por cuenta de la Administración Nacional de la Seguridad Social (ANSES)" los archivos contenidos en los soportes de información que se acompañan, en los cuales se detalla el estado de la totalidad de las órdenes de pago que la ANSES nos encomendara pagar, correspondientes al período .....(2)......de la liquidación ….(3)... Emisión de ANSES: …...................(4) ............ casos por $................(5) ................, Órdenes de Pago pagadas: .............(6) …........ casos por $................(7) .................. Órdenes de Pago impagas: .............(8) ............ casos por $................(9) .................. Certificamos que los datos señalados precedentemente son ciertos y resumen la información detallada en los archivos contenidos en los soportes que se acompañan. Identificación de los archivos Responsables: Firma Firma Nombres y apellidos Nombres y apellidos Tipo y N° doc. de identidad (10) Tipo y N° doc. de identidad (10) Tel. Tel. ................. RECIBIDO ------------------------------------------------------------------------------------------------------------------ Referencias: (1)Código de la entidad financiera. (2)Consignar período de pago mensual o aguinaldo, en su caso. (3)Consignar tipo de liquidación ("ANSES", cuando la rendición es de prestaciones de la Administración Nacional de la Seguridad Social y "MTESS" cuando la rendición es de prestaciones por cuenta y orden del Ministerio de Trabajo, Empleo y Seguridad Social). (4) Cantidad de órdenes de pago que se encomendó pagar a la entidad financiera durante el período de pago correspondiente. (5)Importe en pesos del total puesto al pago. (6)Cantidad de órdenes de pago pagadas. (7)Importe en pesos del total pagado. (8)Cantidad de órdenes de pago impagas. (9)Importe en pesos del total impago. (10)Conforme a lo previsto en las normas sobre "Documentos de identificación en vigencia".

## Omisiones leídas en T4 (M2)

sin_marca:16 [no normativa; propio] «Órdenes de Pago pagadas: .............(6) …........ casos por $................(7) ..................»

## Código A

- **op1 Operacion** «Presentación de rendición de cuentas al BCRA» — Remisión al BCRA, mediante nota modelo, de los archivos en soportes de información con el estado de la totalidad de las órdenes de pago encomendadas por la ANSES, correspondientes al período y liquidación consignados. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Remitimos a Uds. para su procesamiento, en los términos de las normas sobre "Pago de beneficios de la seguridad social por cuenta de la Administración Nacional de la Seguridad Social (ANSES)" los archivos contenidos en los soportes de información que se acompañan»
- **ob1 Obligacion** «Certificar datos de la rendición de cuentas» — La nota de presentación certifica que los datos consignados (casos e importes emitidos, pagados e impagos) son ciertos y resumen la información detallada en los archivos de los soportes acompañados. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «Certificamos que los datos señalados precedentemente son ciertos y resumen la información detallada en los archivos contenidos en los soportes que se acompañan.»
- R: op1 Operacion —requiere→ ob1 Obligacion
- Omisión `fuera_de_tipos` [exacta]: «Responsables: Firma Firma Nombres y apellidos Nombres y apellidos Tipo y N° doc. de identidad (10) Tipo y N° doc. de identidad (10) Tel. Tel.» — Campos del formulario de firma de los responsables; es contenido de modelo, sin norma extraíble.
- Omisión `fuera_de_tipos` [exacta]: «(3)Consignar tipo de liquidación ("ANSES", cuando la rendición es de prestaciones de la Administración Nacional de la Seguridad Social y "MTESS" cuando la rendición es de prestaciones por cuenta y orden del Ministerio de Trabajo, Empleo y Seguridad Social).» — Instrucciones de llenado del formulario (referencias 1 a 10); se habría usado Obligacion o Definicion pero describen campos de un modelo. Sin sujeto nombrado en la unidad, no se emite aplica_a.

### A — omisiones de T4 a clasificar

- sin_marca:16 → entidades: — | omisiones: —

## Código H

- **op1 Operacion** «Presentación de rendición de cuentas de órdenes de pago ANSES» — Remisión al BCRA, mediante nota de presentación y con archivos en soportes de información, del estado de la totalidad de las órdenes de pago que la ANSES encomendó pagar a la entidad, por período y tipo de liquidación (cantidad e importe de órdenes emitidas, pagadas e impagas). · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Remitimos a Uds. para su procesamiento, en los términos de las normas sobre "Pago de beneficios de la seguridad social por cuenta de la Administración Nacional de la Seguridad Social (ANSES)" los archivos contenidos en los soportes de información que se acompañan»
- **ob1 Obligacion** «Certificación de veracidad de los datos de la rendición» — La nota de presentación modelo incluye la certificación de que los datos consignados son ciertos y resumen la información detallada en los archivos de los soportes que se acompañan, firmada por los responsables de la entidad. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «Certificamos que los datos señalados precedentemente son ciertos y resumen la información detallada en los archivos contenidos en los soportes que se acompañan.»
- R: op1 Operacion —requiere→ ob1 Obligacion
- R: Sujeto_entidad_financiera (mención «la entidad financiera») —ejecuta→ op1 Operacion
- R: ob1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- Omisión `meta_normativo` [exacta]: «Fecha: De: (1) A: BANCO CENTRAL DE LA REPÚBLICA ARGENTINA.» — Campos de formato del modelo de nota (encabezado y destinatario); no hay contenido normativo.
- Omisión `meta_normativo` [exacta]: «(3)Consignar tipo de liquidación ("ANSES", cuando la rendición es de prestaciones de la Administración Nacional de la Seguridad Social y "MTESS" cuando la rendición es de prestaciones por cuenta y orden del Ministerio de Trabajo, Empleo y Seguridad Social).» — Instrucciones de llenado de los campos del formulario; no encajan en un tipo del esquema.

### H — omisiones de T4 a clasificar

- sin_marca:16 → entidades: — | omisiones: —

## Código K

- **e1 Operacion** «Nota de presentación de rendición de cuentas al BCRA» — Presentación al BCRA, mediante nota según modelo, de los archivos con el estado de la totalidad de las órdenes de pago que la ANSES encomendó pagar, por período y liquidación · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Modelo de nota de presentación de la rendición de cuentas.»
- **e2 Obligacion** «Consignar período de pago — nota de rendición» — En la nota de rendición se debe consignar el período de pago mensual o aguinaldo, en su caso · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Consignar período de pago mensual o aguinaldo, en su caso.»
- **e3 Obligacion** «Consignar tipo de liquidación ANSES/MTESS — nota de rendición» — Consignar "ANSES" si la rendición es de prestaciones de ANSES y "MTESS" si es de prestaciones por cuenta y orden del Ministerio de Trabajo, Empleo y Seguridad Social · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Consignar tipo de liquidación ("ANSES", cuando la rendición es de prestaciones de la Administración Nacional de la Seguridad Social y "MTESS" cuando la rendición es de prestaciones por cuenta y orden del Ministerio de Trabajo, Empleo y Seguridad Social).»
- **e4 Obligacion** «Certificación de veracidad de datos — nota de rendición» — La nota incluye la certificación, firmada por los responsables, de que los datos son ciertos y resumen la información de los archivos acompañados · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «Certificamos que los datos señalados precedentemente son ciertos y resumen la información detallada en los archivos contenidos en los soportes que se acompañan.»
- R: e2 Obligacion —regula→ e1 Operacion
- R: e3 Obligacion —regula→ e1 Operacion
- R: e4 Obligacion —regula→ e1 Operacion
- R: Sujeto_entidad_financiera (mención «las entidades financieras») —ejecuta→ e1 Operacion
- Omisión `tabla` [exacta]: «Emisión de ANSES: …...................(4) ............ casos por $................(5) ................,» — Campos del formulario modelo (cantidades e importes de órdenes emitidas, pagadas e impagas, firmas, identificación); estructura de plantilla no extraída como norma

### K — omisiones de T4 a clasificar

- sin_marca:16 → entidades: — | omisiones: —

## Código W

- **op1 Operacion** «Presentación nota de rendición de cuentas al BCRA» — Remisión al BCRA de la nota de presentación de la rendición de cuentas con los soportes de información que detallan el estado de la totalidad de las órdenes de pago encomendadas por la ANSES para un período y liquidación · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Modelo de nota de presentación de la rendición de cuentas.»
- **o1 Obligacion** «Detalle de órdenes emitidas, pagadas e impagas — nota» — Consignar en la nota el código de la entidad, el período de pago (mensual o aguinaldo), el tipo de liquidación (ANSES o MTESS) y la cantidad e importe en pesos de las órdenes de pago emitidas, pagadas e impagas · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «Emisión de ANSES: …...................(4) ............ casos por $................(5) ................,»
- **o2 Obligacion** «Certificación de veracidad de datos — nota» — Certificar, con firma de responsables identificados, que los datos de la nota son ciertos y resumen la información de los archivos acompañados · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «Certificamos que los datos señalados precedentemente son ciertos y resumen la información detallada en los archivos contenidos en los soportes que se acompañan.»
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: o2 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: Sujeto_entidad_financiera (mención «las entidades financieras») —ejecuta→ op1 Operacion
- Omisión `tabla` [exacta]: «Responsables: Firma Firma» — Campos del formulario modelo (firmas, identificación, recibido) con disposición tabular; no se reconstruye su estructura.

### W — omisiones de T4 a clasificar

- sin_marca:16 → entidades: — | omisiones: —

