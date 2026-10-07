# `ext::14.5.7` — Los aportes de inversión directa en especie instrumentados mediante la entrega al

Grupos: grupo_c. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 14. Disposiciones complementarias asociadas al Régimen de Incentivo para Grandes Inversiones (RIGI).
> *heredado:* En esta sección se detallan las disposiciones complementarias en materia cambiaria que, en la medida que las disposiciones generales no resulten más favorables, resultan aplicables a un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo los referidas al "Régimen de Incentivo para Grandes Inversiones" (RIGI) establecido en el Título VII de la Ley 27.742 y reglamentado por el Decreto 749/24 y concordantes.
> *heredado:* 14.5. Otras disposiciones.
> *propio:* 14.5.7. Los aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital podrán ser computados como ingresados y liquidados en el mercado de cambios en la medida que: i) El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte que será computado como ingresado y liquidado en el mercado de cambios. La operación podrá incluir bienes que no revistan la condición de bien de capital en la medida que aquellos que lo sean representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado y la entidad cuente con una declaración jurada del cliente en la cual deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios para el funcionamiento, construcción o instalación de los bienes de capital que se están adquiriendo. La entidad deberá contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO). ii) El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte. En caso de no disponerla, deberá presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio de la decisión de capitalización definitiva de los aportes de capital computados de acuerdo con los requisitos legales correspondientes y comprometerse a presentar la documentación de la capitalización definitiva del aporte dentro de los 365 (trescientos sesenta y cinco) días corridos desde el inicio del trámite. iii) Una entidad financiera haya registrado al aporte de capital en el régimen informático de operaciones de cambio (RIOC) mediante la confección de dos boletos de cambio sin movimiento de fondos con las siguientes características: a) Los boletos deberán ser registrados en la fecha en que se produjo el registro de ingreso aduanero de los bienes, independientemente de cuál sea el momento en que el cliente solicite su registro ante la entidad financiera. b) El boleto de compra se confeccionará con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo. En caso de que el VPU contemple la posibilidad de aplicar cobros de exportaciones de bienes para la repatriación del aporte, la entidad deberá asignar el correspondiente número de identificación (número APX) para el "Seguimiento de anticipos y otras financiaciones de exportación de bienes", el cual quedará a cargo de la propia entidad. c) El boleto de venta se confeccionará con el código de concepto de pago diferido de importaciones de bienes de capital, dejando constancia que el pago se enmarca en el presente mecanismo.

## Supuestos de la fase A de T4 (M1)

1. «i) a iii) en la medida que» (miembros i))
2. «i) a iii) en la medida que» (miembros ii))
3. «i) a iii) en la medida que» (miembros iii))
4. «al menos 90 % del FOB»
5. «en caso de no disponer la documentación»
6. «VPU con cobros de exportaciones»

## Código A

- **op1 Operacion** «Aporte de inversión directa en especie con bienes de capital» — Aporte de inversión directa en especie instrumentado mediante la entrega al VPU de bienes de capital, computable como ingresado y liquidado en el mercado de cambios. · props: `{"tipo": "aporte de inversión directa"}` · tramo [exacta]: «Los aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital»
- **p1 Potestad** «Computar aporte en especie como ingresado y liquidado» — Los aportes de inversión directa en especie mediante entrega al VPU de bienes de capital podrán computarse como ingresados y liquidados en el mercado de cambios si se cumplen las condiciones i) a iii). · tramo [exacta]: «podrán ser computados como ingresados y liquidados en el mercado de cambios en la medida que»
- **c1 Condicion** «Registro de ingreso aduanero consistente con el aporte» — El VPU demostró el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte a computar. · tramo [exacta]: «El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte que será computado como ingresado y liquidado en el mercado de cambios.»
- **c2 Condicion** «Documentación de capitalización definitiva o constancia de trámite» — El VPU presenta la documentación que avala la capitalización definitiva del aporte o, en su defecto, constancia del inicio del trámite de inscripción ante el Registro Público de Comercio y compromiso de presentar la documentación definitiva. · tramo [exacta]: «El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte.»
- **c3 Condicion** «Registro en RIOC con dos boletos sin movimiento de fondos» — Una entidad financiera registró el aporte de capital en el RIOC mediante dos boletos de cambio sin movimiento de fondos con las características de los puntos a), b) y c). · tramo [exacta]: «Una entidad financiera haya registrado al aporte de capital en el régimen informático de operaciones de cambio (RIOC) mediante la confección de dos boletos de cambio sin movimiento de fondos»
- **o1 Condicion** «Bienes no de capital hasta 10% del FOB — requisitos» — La operación puede incluir bienes que no son bienes de capital siempre que los que lo sean representen como mínimo el 90% del valor FOB total pagado. · umbral: ['representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado'] · tramo [exacta]: «La operación podrá incluir bienes que no revistan la condición de bien de capital en la medida que aquellos que lo sean representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado»
- **o2 Obligacion** «Contar con declaración jurada del cliente sobre bienes restantes» — La entidad debe contar con una declaración jurada del cliente que deje constancia de que los bienes restantes son repuestos, accesorios o materiales necesarios para los bienes de capital. · props: `{"tipo": "otra"}` · tramo [exacta]: «la entidad cuente con una declaración jurada del cliente en la cual deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios para el funcionamiento, construcción o instalación de los bienes de capital que se están adquiriendo»
- **o3 Obligacion** «Contar con certificación SEPAIMPO» — La entidad debe contar con la certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO). · props: `{"tipo": "otra"}` · tramo [exacta]: «La entidad deberá contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO).»
- **o4 Obligacion** «VPU presenta documentación de capitalización definitiva» — El VPU debe presentar la documentación que avale la capitalización definitiva del aporte. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte.»
- **o5 Obligacion** «VPU: constancia de trámite y compromiso en 365 días» — Si no dispone de la documentación de capitalización definitiva, el VPU debe presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio y comprometerse a presentar la documentación dentro de los 365 días corridos desde el inicio del trámite. · props: `{"tipo": "presentacion_informativa"}` · umbral: ['dentro de los 365 (trescientos sesenta y cinco) días corridos desde el inicio de…'] · tramo [exacta]: «En caso de no disponerla, deberá presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio de la decisión de capitalización definitiva de los aportes de capital computados de acuerdo con los requisitos legales correspondientes y comprometerse a presentar la documentación de la capi…»
- **o6 Obligacion** «Registrar boletos en fecha de ingreso aduanero» — Los dos boletos de cambio deben registrarse en la fecha del registro de ingreso aduanero de los bienes, sin importar cuándo el cliente solicite su registro. · props: `{"tipo": "otra"}` · tramo [exacta]: «Los boletos deberán ser registrados en la fecha en que se produjo el registro de ingreso aduanero de los bienes, independientemente de cuál sea el momento en que el cliente solicite su registro ante la entidad financiera.»
- **o7 Obligacion** «Boleto de compra con código de concepto del mecanismo» — El boleto de compra se confecciona con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo. · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de compra se confeccionará con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo.»
- **o8 Obligacion** «Asignar número APX a cargo de la entidad» — Si el VPU contempla aplicar cobros de exportaciones de bienes para la repatriación del aporte, la entidad debe asignar el número APX para el Seguimiento de anticipos y otras financiaciones de exportación de bienes, a cargo de la propia entidad. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «En caso de que el VPU contemple la posibilidad de aplicar cobros de exportaciones de bienes para la repatriación del aporte, la entidad deberá asignar el correspondiente número de identificación (número APX) para el "Seguimiento de anticipos y otras financiaciones de exportación de bienes", el cual quedará a cargo de l…»
- **o9 Obligacion** «Boleto de venta con código de pago diferido de bienes de capital» — El boleto de venta se confecciona con el código de concepto de pago diferido de importaciones de bienes de capital, dejando constancia de que el pago se enmarca en este mecanismo. · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta se confeccionará con el código de concepto de pago diferido de importaciones de bienes de capital, dejando constancia que el pago se enmarca en el presente mecanismo.»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: o1 Condicion —condicion_de→ op1 Operacion
- R: p1 Potestad —aplica_a→ Sujeto_vpu_rigi (mención «VPU»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o3 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: o4 Obligacion —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- R: o5 Obligacion —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- R: o8 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o6 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «entidad financiera»)
- R: o6 Obligacion —regula→ op1 Operacion
- R: o7 Obligacion —regula→ op1 Operacion
- R: o9 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —condiciona→ op1 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «El VPU haya demostrado el registro de ingreso aduanero del bien de capital» — El sujeto VPU no se vincula a la Condicion c1 con aplica_a (dominio no admite Condicion); se habría usado aplica_a.

### A — supuestos a clasificar

- 1. «i) a iii) en la medida que» → candidatos: o1 Condicion (1.00), p1 Potestad (1.00)
- 2. «i) a iii) en la medida que» → candidatos: o1 Condicion (1.00), p1 Potestad (1.00)
- 3. «i) a iii) en la medida que» → candidatos: o1 Condicion (1.00), p1 Potestad (1.00)
- 4. «al menos 90 % del FOB» → candidatos: o1 Condicion (0.67)
- 5. «en caso de no disponer la documentación» → candidatos: o5 Obligacion (0.67), c2 Condicion (0.33), o4 Obligacion (0.33), o8 Obligacion (0.33)
- 6. «VPU con cobros de exportaciones» → candidatos: o8 Obligacion (1.00), c1 Condicion (0.33), c2 Condicion (0.33), o4 Obligacion (0.33)

## Código H

- **op1 Operacion** «Cómputo de aporte en especie de bienes de capital como ingresado y liquidado» — Aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital, computados como ingresados y liquidados en el mercado de cambios · props: `{"tipo": "computo_aporte_inversion_directa"}` · tramo [exacta]: «Los aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital podrán ser computados como ingresados y liquidados en el mercado de cambios»
- **pot1 Potestad** «Cómputo como ingresado y liquidado de aportes en especie (bienes de capital)» — Los aportes de inversión directa en especie mediante entrega al VPU de bienes de capital pueden computarse como ingresados y liquidados en el mercado de cambios, en la medida que se cumplan los supuestos i), ii) y iii) · tramo [exacta]: «podrán ser computados como ingresados y liquidados en el mercado de cambios en la medida que»
- **c1 Condicion** «Registro de ingreso aduanero consistente con el monto del aporte» — El VPU debe haber demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte a computar · tramo [exacta]: «El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte que será computado como ingresado y liquidado en el mercado de cambios.»
- **c2 Condicion** «Capitalización definitiva del aporte documentada» — El VPU presenta la documentación que avala la capitalización definitiva del aporte; en su defecto, constancia del inicio del trámite de inscripción ante el Registro Público de Comercio y compromiso de presentarla dentro de 365 días corridos · tramo [exacta]: «El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte.»
- **c3 Condicion** «Registro del aporte en RIOC con dos boletos de cambio» — Una entidad financiera debe haber registrado el aporte de capital en el RIOC mediante dos boletos de cambio sin movimiento de fondos, con las características de los puntos a), b) y c) · tramo [exacta]: «Una entidad financiera haya registrado al aporte de capital en el régimen informático de operaciones de cambio (RIOC) mediante la confección de dos boletos de cambio sin movimiento de fondos»
- **r1 Restriccion** «Bienes de capital al menos 90% del valor FOB» — La operación puede incluir bienes que no sean bienes de capital en la medida que los que lo sean representen como mínimo el 90% del valor FOB total pagado · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['como mínimo el 90% (noventa por ciento) del valor FOB total pagado'] · tramo [exacta]: «La operación podrá incluir bienes que no revistan la condición de bien de capital en la medida que aquellos que lo sean representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado»
- **o1 Obligacion** «Contar con declaración jurada del cliente sobre bienes restantes» — Para incluir bienes que no sean bienes de capital, la entidad debe contar con declaración jurada del cliente que deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios para el funcionamiento, construcción o instalación de los bienes de capital · props: `{"tipo": "otra"}` · tramo [exacta]: «la entidad cuente con una declaración jurada del cliente en la cual deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios para el funcionamiento, construcción o instalación de los bienes de capital que se están adquiriendo»
- **o2 Obligacion** «Contar con certificación SEPAIMPO» — La entidad debe contar con la certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO) · props: `{"tipo": "otra"}` · tramo [exacta]: «La entidad deberá contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO).»
- **o3 Obligacion** «VPU presenta documentación de capitalización definitiva» — El VPU debe presentar la documentación que avale la capitalización definitiva del aporte · props: `{"tipo": "presentacion_informativa"}` · tramo [no]: «El VPU deberá presentar la documentación que avala la capitalización definitiva del aporte.»
- **o4 Obligacion** «VPU presenta constancia de trámite y compromiso en 365 días» — Si no dispone de la documentación de capitalización definitiva, el VPU debe presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio y comprometerse a presentar la documentación dentro de 365 días corridos desde el inicio del trámite · props: `{"tipo": "presentacion_informativa"}` · umbral: ['dentro de los 365 (trescientos sesenta y cinco) días corridos desde el inicio de…'] · tramo [exacta]: «En caso de no disponerla, deberá presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio de la decisión de capitalización definitiva de los aportes de capital computados de acuerdo con los requisitos legales correspondientes y comprometerse a presentar la documentación de la capi…»
- **o5 Obligacion** «Registrar boletos en la fecha del ingreso aduanero» — Los dos boletos de cambio deben registrarse en la fecha del registro de ingreso aduanero de los bienes, sin importar cuándo el cliente solicite su registro ante la entidad financiera · props: `{"tipo": "otra"}` · tramo [exacta]: «Los boletos deberán ser registrados en la fecha en que se produjo el registro de ingreso aduanero de los bienes, independientemente de cuál sea el momento en que el cliente solicite su registro ante la entidad financiera.»
- **o6 Obligacion** «Boleto de compra con código de concepto del mecanismo» — El boleto de compra se confecciona con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de compra se confeccionará con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo.»
- **o7 Obligacion** «Asignar número APX si se aplican cobros de exportaciones» — Si el VPU contempla aplicar cobros de exportaciones de bienes para la repatriación del aporte, la entidad debe asignar el número APX para el Seguimiento de anticipos y otras financiaciones de exportación de bienes, a cargo de la propia entidad · props: `{"tipo": "asignacion"}` · tramo [exacta]: «la entidad deberá asignar el correspondiente número de identificación (número APX) para el "Seguimiento de anticipos y otras financiaciones de exportación de bienes", el cual quedará a cargo de la propia entidad.»
- **c4 Condicion** «VPU contempla cobros de exportaciones para repatriar el aporte» — El VPU contempla la posibilidad de aplicar cobros de exportaciones de bienes para la repatriación del aporte · tramo [exacta]: «En caso de que el VPU contemple la posibilidad de aplicar cobros de exportaciones de bienes para la repatriación del aporte»
- **o8 Obligacion** «Boleto de venta con código de pago diferido de importaciones» — El boleto de venta se confecciona con el código de concepto de pago diferido de importaciones de bienes de capital, dejando constancia de que el pago se enmarca en este mecanismo · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta se confeccionará con el código de concepto de pago diferido de importaciones de bienes de capital, dejando constancia que el pago se enmarca en el presente mecanismo.»
- R: c1 Condicion —condicion_de→ pot1 Potestad
- R: c2 Condicion —condicion_de→ pot1 Potestad
- R: c3 Condicion —condicion_de→ pot1 Potestad
- R: c4 Condicion —condicion_de→ o7 Obligacion
- R: r1 Restriccion —limita→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o1 Obligacion —regula→ op1 Operacion
- R: o5 Obligacion —regula→ op1 Operacion
- R: o6 Obligacion —regula→ op1 Operacion
- R: o7 Obligacion —regula→ op1 Operacion
- R: o8 Obligacion —regula→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: o3 Obligacion —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- R: o4 Obligacion —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- R: o7 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o5 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «entidad financiera»)
- R: pot1 Potestad —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- Omisión `relacion_sin_predicado` [exacta]: «El VPU haya demostrado el registro de ingreso aduanero del bien de capital» — Los requisitos i), ii) y iii) deben cumplirse conjuntamente (condicion_de hacia la Potestad)
- Omisión `fuera_de_tipos` [exacta]: «El boleto de compra se confeccionará con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo.» — Es parte de las características del registro RIOC; ya extraído como Obligacion

### H — supuestos a clasificar

- 1. «i) a iii) en la medida que» → candidatos: pot1 Potestad (1.00), r1 Restriccion (1.00)
- 2. «i) a iii) en la medida que» → candidatos: pot1 Potestad (1.00), r1 Restriccion (1.00)
- 3. «i) a iii) en la medida que» → candidatos: pot1 Potestad (1.00), r1 Restriccion (1.00)
- 4. «al menos 90 % del FOB» → candidatos: r1 Restriccion (1.00)
- 5. «en caso de no disponer la documentación» → candidatos: o4 Obligacion (0.67), c2 Condicion (0.33), c4 Condicion (0.33), o3 Obligacion (0.33)
- 6. «VPU con cobros de exportaciones» → candidatos: c4 Condicion (1.00), o7 Obligacion (1.00), c1 Condicion (0.33), c2 Condicion (0.33)

## Código K

- **op1 Operacion** «Cómputo aporte en especie como liquidado» — Cómputo como ingresados y liquidados en el mercado de cambios de aportes de inversión directa en especie instrumentados mediante entrega al VPU de bienes de capital · props: `{"tipo": "aporte de inversión directa"}` · tramo [exacta]: «Los aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital podrán ser computados como ingresados y liquidados en el mercado de cambios»
- **p1 Potestad** «Computar aporte en especie de bienes de capital» — Los aportes de inversión directa en especie mediante entrega al VPU de bienes de capital pueden computarse como ingresados y liquidados en el mercado de cambios si se cumplen las condiciones i) a iii). · tramo [exacta]: «podrán ser computados como ingresados y liquidados en el mercado de cambios en la medida que:»
- **c1 Condicion** «Registro aduanero del bien consistente con aporte» — El VPU demostró el registro de ingreso aduanero del bien de capital por valor consistente con el monto del aporte computado. · tramo [exacta]: «El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte»
- **p2 Potestad** «Inclusión de bienes no de capital» — La operación puede incluir bienes que no sean bienes de capital, bajo condiciones. · tramo [exacta]: «La operación podrá incluir bienes que no revistan la condición de bien de capital»
- **c2 Condicion** «Bienes de capital mínimo 90% valor FOB» — Los bienes de capital representan como mínimo el 90% del valor FOB total pagado. · umbral: ['como mínimo el 90% (noventa por ciento) del valor FOB total pagado'] · tramo [exacta]: «en la medida que aquellos que lo sean representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado»
- **c3 Condicion** «DDJJ cliente: restantes bienes son repuestos/accesorios» — La entidad cuenta con DDJJ del cliente de que los restantes bienes son repuestos, accesorios o materiales necesarios para funcionamiento, construcción o instalación de los bienes de capital. · tramo [exacta]: «la entidad cuente con una declaración jurada del cliente en la cual deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios»
- **o1 Obligacion** «Certificación SEPAIMPO — aporte en especie» — La entidad debe contar con la certificación de la entidad encargada del SEPAIMPO. · props: `{"tipo": "otra"}` · tramo [exacta]: «La entidad deberá contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO).»
- **o2 Obligacion** «Documentación de capitalización definitiva del aporte» — El VPU debe presentar la documentación que avale la capitalización definitiva del aporte. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte.»
- **x1 Excepcion** «Sin documentación: constancia de inscripción en trámite» — Si no dispone de la documentación, el VPU presenta constancia de inicio del trámite de inscripción en el Registro Público de Comercio y se compromete a presentar la documentación de capitalización definitiva dentro de 365 días corridos. · umbral: ['dentro de los 365 (trescientos sesenta y cinco) días corridos desde el inicio de…'] · tramo [exacta]: «En caso de no disponerla, deberá presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio»
- **c4 Condicion** «Registro del aporte en RIOC con dos boletos» — Una entidad financiera registró el aporte en el RIOC con dos boletos sin movimiento de fondos con las características a) a c). · tramo [exacta]: «Una entidad financiera haya registrado al aporte de capital en el régimen informático de operaciones de cambio (RIOC) mediante la confección de dos boletos de cambio sin movimiento de fondos»
- **o3 Obligacion** «Fecha de registro de boletos: ingreso aduanero» — Los boletos deben registrarse en la fecha del registro de ingreso aduanero de los bienes, independientemente de cuándo el cliente solicite su registro. · props: `{"tipo": "otra"}` · tramo [exacta]: «Los boletos deberán ser registrados en la fecha en que se produjo el registro de ingreso aduanero de los bienes»
- **o4 Obligacion** «Código de concepto del boleto de compra» — El boleto de compra se confecciona con código de concepto que identifique el aporte comprendido en el mecanismo. · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de compra se confeccionará con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo.»
- **c5 Condicion** «VPU contempla repatriar con cobros de exportación» — El VPU contempla aplicar cobros de exportaciones de bienes para repatriar el aporte. · tramo [exacta]: «En caso de que el VPU contemple la posibilidad de aplicar cobros de exportaciones de bienes para la repatriación del aporte»
- **o5 Obligacion** «Asignar número APX — seguimiento de anticipos» — La entidad debe asignar el número APX para el Seguimiento de anticipos y otras financiaciones de exportación de bienes, quedando a su cargo. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «la entidad deberá asignar el correspondiente número de identificación (número APX)»
- **o6 Obligacion** «Código de concepto del boleto de venta» — El boleto de venta se confecciona con el código de pago diferido de importaciones de bienes de capital, dejando constancia de que se enmarca en el mecanismo. · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta se confeccionará con el código de concepto de pago diferido de importaciones de bienes de capital»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c4 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p2 Potestad
- R: c3 Condicion —condicion_de→ p2 Potestad
- R: c5 Condicion —condicion_de→ o5 Obligacion
- R: x1 Excepcion —exceptua_obligacion→ o2 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o2 Obligacion —condiciona→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o4 Obligacion —regula→ op1 Operacion
- R: o6 Obligacion —regula→ op1 Operacion
- R: p1 Potestad —aplica_a→ Sujeto_vpu_rigi (mención «VPU»)
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: o2 Obligacion —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- R: x1 Excepcion —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- R: o5 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o3 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Una entidad financiera»)
- R: o4 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Una entidad financiera»)
- R: o6 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Una entidad financiera»)

### K — supuestos a clasificar

- 1. «i) a iii) en la medida que» → candidatos: c2 Condicion (1.00), p1 Potestad (1.00)
- 2. «i) a iii) en la medida que» → candidatos: c2 Condicion (1.00), p1 Potestad (1.00)
- 3. «i) a iii) en la medida que» → candidatos: c2 Condicion (1.00), p1 Potestad (1.00)
- 4. «al menos 90 % del FOB» → candidatos: c2 Condicion (0.67)
- 5. «en caso de no disponer la documentación» → candidatos: x1 Excepcion (0.67), c5 Condicion (0.33), o2 Obligacion (0.33)
- 6. «VPU con cobros de exportaciones» → candidatos: c5 Condicion (1.00), c1 Condicion (0.33), o2 Obligacion (0.33), op1 Operacion (0.33)

## Código W

- **op1 Operacion** «Cómputo como ingresado y liquidado de aporte en especie» — Cómputo como ingresados y liquidados en el mercado de cambios de aportes de inversión directa en especie instrumentados mediante entrega al VPU de bienes de capital · props: `{"tipo": "cómputo de ingreso y liquidación"}` · tramo [exacta]: «Los aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital podrán ser computados como ingresados y liquidados en el mercado de cambios»
- **p1 Potestad** «Cómputo de aportes en especie con bienes de capital» — Los aportes de inversión directa en especie mediante entrega al VPU de bienes de capital pueden computarse como ingresados y liquidados en el mercado de cambios si se cumplen los requisitos i) a iii). · tramo [exacta]: «podrán ser computados como ingresados y liquidados en el mercado de cambios en la medida que:»
- **c1 Condicion** «Registro de ingreso aduanero consistente con aporte» — El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte a computar. · props: `{"umbrales": [{"tramo": "por\nun valor consistente con el monto del aporte", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por un valor consistente con el monto del aporte'] · tramo [exacta]: «El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte»
- **p2 Potestad** «Inclusión de bienes que no son de capital» — La operación puede incluir bienes que no sean bienes de capital, sujeto a las condiciones del 90% FOB y la declaración jurada. · tramo [exacta]: «La operación podrá incluir bienes que no revistan la condición de bien de capital»
- **c2 Condicion** «Bienes de capital mínimo 90% del FOB» — Los bienes de capital representen como mínimo el 90% del valor FOB total pagado. · umbral: ['como mínimo el 90% (noventa por ciento) del valor FOB total pagado'] · tramo [exacta]: «en la medida que aquellos que lo sean representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado»
- **c3 Condicion** «Declaración jurada del cliente sobre restantes bienes» — La entidad cuente con declaración jurada del cliente de que los restantes bienes son repuestos, accesorios o materiales necesarios para funcionamiento, construcción o instalación de los bienes de capital. · tramo [exacta]: «la entidad cuente con una declaración jurada del cliente en la cual deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios»
- **o1 Obligacion** «Certificación SEPAIMPO — aporte en especie» — La entidad debe contar con la certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO). · props: `{"tipo": "otra"}` · tramo [exacta]: «La entidad deberá contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO).»
- **o2 Obligacion** «Documentación de capitalización definitiva — VPU» — El VPU debe presentar la documentación que avale la capitalización definitiva del aporte. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte.»
- **o3 Obligacion** «Constancia inicio inscripción y compromiso 365 días» — Si no dispone de la documentación, el VPU debe presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio de la capitalización definitiva y comprometerse a presentar la documentación dentro de 365 días corridos desde el inicio del trámite. · props: `{"tipo": "presentacion_informativa"}` · umbral: ['dentro de los 365 (trescientos sesenta y cinco) días corridos desde el inicio de…'] · tramo [exacta]: «En caso de no disponerla, deberá presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio»
- **c4 Condicion** «Sin documentación de capitalización definitiva» — El VPU no dispone de la documentación de capitalización definitiva. · tramo [exacta]: «En caso de no disponerla»
- **c5 Condicion** «Registro del aporte en RIOC con dos boletos» — Una entidad financiera haya registrado el aporte en el RIOC mediante dos boletos de cambio sin movimiento de fondos con las características a) a c). · tramo [exacta]: «Una entidad financiera haya registrado al aporte de capital en el régimen informático de operaciones de cambio (RIOC) mediante la confección de dos boletos de cambio sin movimiento de fondos»
- **op2 Operacion** «Registro en RIOC de boletos sin movimiento de fondos» — Registro del aporte de capital en especie en el RIOC mediante dos boletos de cambio (compra y venta) sin movimiento de fondos · props: `{"tipo": "registro de operación de cambio"}` · tramo [exacta]: «registrado al aporte de capital en el régimen informático de operaciones de cambio (RIOC) mediante la confección de dos boletos de cambio sin movimiento de fondos»
- **o4 Obligacion** «Fecha de registro de boletos: ingreso aduanero» — Los boletos deben registrarse en la fecha del registro de ingreso aduanero de los bienes, independientemente de cuándo el cliente solicite su registro ante la entidad financiera. · props: `{"tipo": "otra"}` · tramo [exacta]: «Los boletos deberán ser registrados en la fecha en que se produjo el registro de ingreso aduanero de los bienes»
- **o5 Obligacion** «Código de concepto del boleto de compra» — El boleto de compra se confecciona con un código de concepto que identifique que es un aporte comprendido en este mecanismo. · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de compra se confeccionará con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo.»
- **o6 Obligacion** «Asignación número APX si repatriación con exportaciones» — Si el VPU contempla aplicar cobros de exportaciones de bienes a la repatriación del aporte, la entidad debe asignar el número APX para el Seguimiento de anticipos y otras financiaciones de exportación de bienes, que queda a cargo de la propia entidad. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «la entidad deberá asignar el correspondiente número de identificación (número APX)»
- **c6 Condicion** «VPU contempla repatriar con cobros de exportaciones» — El VPU contempla aplicar cobros de exportaciones de bienes para la repatriación del aporte. · tramo [exacta]: «En caso de que el VPU contemple la posibilidad de aplicar cobros de exportaciones de bienes para la repatriación del aporte»
- **o7 Obligacion** «Código de concepto del boleto de venta» — El boleto de venta se confecciona con el código de concepto de pago diferido de importaciones de bienes de capital, dejando constancia de que el pago se enmarca en este mecanismo. · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta se confeccionará con el código de concepto de pago diferido de importaciones de bienes de capital»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c5 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p2 Potestad
- R: c3 Condicion —condicion_de→ p2 Potestad
- R: c4 Condicion —condicion_de→ o3 Obligacion
- R: c6 Condicion —condicion_de→ o6 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o2 Obligacion —condiciona→ op1 Operacion
- R: o4 Obligacion —regula→ op2 Operacion
- R: o5 Obligacion —regula→ op2 Operacion
- R: o7 Obligacion —regula→ op2 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: o2 Obligacion —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- R: o3 Obligacion —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- R: o6 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o4 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Una entidad financiera»)
- R: o5 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Una entidad financiera»)
- R: o7 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Una entidad financiera»)
- R: Sujeto_entidad_financiera (mención «Una entidad financiera») —ejecuta→ op2 Operacion

### W — supuestos a clasificar

- 1. «i) a iii) en la medida que» → candidatos: c2 Condicion (1.00), p1 Potestad (1.00)
- 2. «i) a iii) en la medida que» → candidatos: c2 Condicion (1.00), p1 Potestad (1.00)
- 3. «i) a iii) en la medida que» → candidatos: c2 Condicion (1.00), p1 Potestad (1.00)
- 4. «al menos 90 % del FOB» → candidatos: c2 Condicion (0.67), p2 Potestad (0.67)
- 5. «en caso de no disponer la documentación» → candidatos: c4 Condicion (0.67), o3 Obligacion (0.67), c6 Condicion (0.33), o2 Obligacion (0.33)
- 6. «VPU con cobros de exportaciones» → candidatos: c6 Condicion (1.00), o6 Obligacion (1.00), c1 Condicion (0.33), c4 Condicion (0.33)

