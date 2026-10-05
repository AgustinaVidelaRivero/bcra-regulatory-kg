# Fichas de P5 (sin grupo ni origen)

Orden: random.Random('U-PROMPT-R2:P5:2026-10-05:fichas').shuffle sobre los 27 ids ordenados. A y B = las dos corridas de E1 con temperatura 0 (prefijo `322c5a23e9b7`, el código de P5), validadas con el validador del perfil r2b. Si las dos salidas son iguales byte a byte, la ficha lo dice y muestra una.

## Ficha 1 — `ext::4.1.4.7`

**Texto propio:**

```
4.1.4.7. la adquisición de tarjetas de regalo o equivalentes de tiendas o locales
radicados en el exterior.
```
**Heredado:** Sección 4. Otras disposiciones específicas. / 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tarjetas de / crédito, compra y prepagas emitidas en el país. / 4.1.4. Pagos al exterior por el uso de tarjetas de crédito, compra, débito o prepagas emitidas / en el país o cualquier modalidad que implique un débito inmediato en una cuenta en una entidad financiera local. Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deberán contar con la conformidad previa del BCRA para acceder…

**A** — error: None; salida: 994 tokens

- Operacion «Adquisición de tarjetas de regalo exterior»: Adquisición de tarjetas de regalo o equivalentes de tiendas o locales radicados en el exterior, mediante débito en cuenta en entidad financiera local o tarjetas emitidas en el país ‖ tramo (exacta): «la adquisición de tarjetas de regalo o equivalentes de tiendas o locales radicados en el exterior»
- Restriccion «Conformidad previa BCRA — pagos exterior tarjetas»: Requisito de conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas de crédito, compra, débito o prepagas emitidas en el país o cualquier modalidad que implique débito inmediato en cuenta en entidad financiera local, cuando tales pagos s… ‖ tramo (exacta): «Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deberán contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterio…»
  - Operacion:Adquisición de tarjetas de regalo exterior --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Conformidad previa BCRA — pagos exterior tarjetas --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Conformidad previa BCRA — pagos exterior tarjetas --limita--> Operacion:Adquisición de tarjetas de regalo exterior
  - Restriccion:Conformidad previa BCRA — pagos exterior tarjetas --aplica_a--> Las entidades financieras
  - Restriccion:Conformidad previa BCRA — pagos exterior tarjetas --aplica_a--> las empresas no financieras emisoras de tarjetas locales
  - mención: aplica_a «Las entidades financieras» (verificada: exacta)
  - mención: aplica_a «las empresas no financieras emisoras de tarjetas locales» (verificada: exacta)
  - omisión meta_normativo (exacta): «cuando tales pagos se originen, en forma directa o indirecta a través del uso de redes de pagos internacionales» — nota: 
  - heredado_compuesto: 1

**B** — error: None; salida: 1051 tokens

- Operacion «Adquisición de tarjetas de regalo exterior»: Adquisición de tarjetas de regalo o equivalentes de tiendas o locales radicados en el exterior, mediante débito en cuenta en entidad financiera local o tarjetas emitidas en el país ‖ tramo (exacta): «la adquisición de tarjetas de regalo o equivalentes de tiendas o locales radicados en el exterior»
- Obligacion «Conformidad previa BCRA — pagos exterior tarjetas»: Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deberán contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas o cualquier modalidad que implique débito inmediato en cuenta en entidad fi… ‖ tramo (exacta): «Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deberán contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterio…»
  - Operacion:Adquisición de tarjetas de regalo exterior --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Conformidad previa BCRA — pagos exterior tarjetas --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Conformidad previa BCRA — pagos exterior tarjetas --aplica_a--> Las entidades financieras
  - Obligacion:Conformidad previa BCRA — pagos exterior tarjetas --aplica_a--> las empresas no financieras emisoras de tarjetas locales
  - Obligacion:Conformidad previa BCRA — pagos exterior tarjetas --condiciona--> Operacion:Adquisición de tarjetas de regalo exterior
  - Operacion:Adquisición de tarjetas de regalo exterior --requiere--> Obligacion:Conformidad previa BCRA — pagos exterior tarjetas
  - mención: aplica_a «Las entidades financieras» (verificada: exacta)
  - mención: aplica_a «las empresas no financieras emisoras de tarjetas locales» (verificada: exacta)
  - heredado_compuesto: 0

## Ficha 2 — `ctacte::3.2.5`

**Texto propio:**

```
3.2.5. Fecha de vencimiento de un cheque de pago diferido –no registrado– anterior o igual a
la fecha de libramiento.
```
**Heredado:** Sección 3. Cheques. / 3.2. Títulos que carecen de valor como cheques. / El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque: / Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones.

**A** — error: None; salida: 660 tokens

- Operacion «Cheque de pago diferido no registrado»: Cheque de pago diferido que no ha sido registrado ‖ tramo (exacta): «cheque de pago diferido –no registrado–»
- Restriccion «Fecha de vencimiento anterior o igual a libramiento»: El cheque de pago diferido no registrado no valdrá como cheque cuando su fecha de vencimiento sea anterior o igual a la fecha de libramiento ‖ tramo (exacta): «Fecha de vencimiento de un cheque de pago diferido –no registrado– anterior o igual a la fecha de libramiento»
  - Restriccion:Fecha de vencimiento anterior o igual a libramiento --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - Restriccion:Fecha de vencimiento anterior o igual a libramiento --limita--> Operacion:Cheque de pago diferido no registrado
  - Restriccion:Fecha de vencimiento anterior o igual a libramiento --aplica_a--> Los títulos
  - mención: aplica_a «Los títulos» (verificada: exacta)
  - omisión meta_normativo (exacta): «no valdrá como cheque» — nota: Cláusula interpretativa que declara el efecto jurídico de la situación descrita (que el título pierde su carácter de cheque), no una prescri…
  - heredado_compuesto: 0

**B** — error: None; salida: 875 tokens

- Operacion «Cheque de pago diferido no registrado»: Cheque de pago diferido que no ha sido registrado ‖ tramo (exacta): «cheque de pago diferido –no registrado–»
- Condicion «Fecha de vencimiento anterior o igual a fecha de libramiento»: El cheque de pago diferido no registrado tiene una fecha de vencimiento anterior o igual a la fecha de su libramiento ‖ tramo (exacta): «Fecha de vencimiento de un cheque de pago diferido –no registrado– anterior o igual a la fecha de libramiento» ‖ umbrales: ['anterior o igual a la fecha de libramiento']
- Restriccion «Cheque sin valor como cheque»: El título que presenta esta situación no tendrá valor como cheque ‖ tramo (exacta): «no valdrá como cheque»
  - Operacion:Cheque de pago diferido no registrado --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - Condicion:Fecha de vencimiento anterior o igual a fecha de libramiento --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - Restriccion:Cheque sin valor como cheque --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - Condicion:Fecha de vencimiento anterior o igual a fecha de libramiento --condicion_de--> Restriccion:Cheque sin valor como cheque
  - Restriccion:Cheque sin valor como cheque --prohibe--> Operacion:Cheque de pago diferido no registrado
  - omisión meta_normativo (exacta): «Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones» — nota: Contenido de cierre del punto 3.2 que predica sobre la consecuencia de los títulos sin valor; no es parte del contenido normativo específico…
  - heredado_compuesto: 1

## Ficha 3 — `ctacte::3.2::intro`

**Texto propio:**

```
El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas
taxativamente a continuación, no valdrá como cheque:
```
**Heredado:** Sección 3. Cheques. / 3.2. Títulos que carecen de valor como cheques.

**A** — error: None; salida: 395 tokens

- Restriccion «Título sin valor como cheque»: Un título que presente alguna de las situaciones enumeradas a continuación no tendrá valor como cheque ‖ tramo (exacta): «El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque»
  - Restriccion:Título sin valor como cheque --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - omisión meta_normativo (exacta): «enumeradas taxativamente a continuación» — nota: Cláusula que predica sobre la forma de enumeración (carácter taxativo) de las situaciones que siguen, no sobre conducta regulada
  - heredado_compuesto: 0

**B** — error: None; salida: 383 tokens

- Restriccion «Título sin valor como cheque»: Un título que presente alguna de las situaciones enumeradas a continuación no tendrá valor como cheque ‖ tramo (exacta): «El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque»
  - Restriccion:Título sin valor como cheque --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - omisión meta_normativo (exacta): «enumeradas taxativamente a continuación» — nota: Declaración sobre el carácter exhaustivo de la enumeración que sigue; no prescribe conducta
  - heredado_compuesto: 0

## Ficha 4 — `ext::10.3.6`

**Texto propio:**

```
10.3.6. Pagos de importaciones con cartas de crédito o letras avaladas emitidas u otorgadas
por entidades financieras locales.
La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o
letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones
de bienes que tengan el registro aduanero de los bienes, incluso cuando no se
cumplan los requisitos establecidos para el acceso del cliente, en la medida que
cuente con la documentación que demuestre que, al momento de la apertura o
emisión por parte de la entidad, se cumplían las condiciones que resultaban
aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada
y el tipo de operación garantizada por la entidad.
En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del
13/12/23, la entidad deberá contar con la documentación que demuestre que, al
momento de la apertura o emisión, la operación garantizada correspondía a una
importación de bienes con registro de ingreso aduanero a partir de dicha fecha y,
salvo que la operación quedase comprendida en la situación prevista en el punto
10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la
fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien
por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de
arribo de los bienes al país.
Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se
cumplan las restantes condiciones, también se admitirá que el pago garantizado
tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes
en origen más un plazo adicional de 15 (quince) días corridos cuando correspondía a
la porción de una operación por la cual el cliente hubiese podido realizar pagos a la
vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2.
Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u
otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del
Anexo de la Comunicación A 7914.
El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de
cliente por el concepto “B14. Cancelación de garantías comerciales de entidades
financieras por importaciones de bienes con registro de ingreso aduanero”.
```
**Heredado:** Sección 10. Pagos de importaciones y otras compras de bienes en el exterior. / 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero.

**A = B (iguales byte a byte)** — error: None; salida: 3047 tokens

- Operacion «Cancelación de cartas de crédito o letras avaladas»: Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan registro aduanero de los bienes ‖ tramo (exacta): «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro adua…»
- Condicion «Documentación de cumplimiento de condiciones al momento de emisión»: La entidad debe contar con documentación que demuestre que al momento de la apertura o emisión se cumplían las condiciones aplicables según la fecha de emisión y el tipo de operación garantizada ‖ tramo (exacta): «en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que…»
- Condicion «Cartas de crédito o letras avaladas emitidas a partir del 13/12/23»: Aplica a cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13 de diciembre de 2023 ‖ tramo (exacta): «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23» ‖ umbrales: ['a partir del 13/12/23']
- Obligacion «Documentación de importación con registro aduanero a partir del 13/12/23»: La entidad deberá contar con documentación que demuestre que la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir del 13/12/23 ‖ tramo (exacta): «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero…»
- Condicion «Operación no comprendida en punto 10.10.2.11»: Salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11 ‖ tramo (exacta): «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- Obligacion «Pago garantizado a partir de plazo de bien más 15 días»: El pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1 más otros 15 días corridos a la fecha estimada de arribo de los bienes al país ‖ tramo (exacta): «que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (qu…» ‖ umbrales: ['más otros 15 (quince) días corridos']
- Condicion «Cartas de crédito o letras avaladas emitidas a partir del 14/04/25»: Aplica a cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14 de abril de 2025 ‖ tramo (exacta): «Para aquellas emitidas u otorgadas a partir del 14/04/25» ‖ umbrales: ['a partir del 14/04/25']
- Excepcion «Pago a partir de fecha estimada de embarque más 15 días»: Se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 días corridos cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de l… ‖ tramo (exacta): «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos cuando corr…» ‖ umbrales: ['más un plazo adicional de 15 (quince) días corridos']
- Comunicacion «Com. A 7914»:  ‖ tramo (exacta): «Comunicación A 7914»
- Obligacion «Boleto de venta a nombre de la entidad»: El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto 'B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero' ‖ tramo (exacta): «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes…»
  - Operacion:Cancelación de cartas de crédito o letras avaladas --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Documentación de cumplimiento de condiciones al momento de emisión --condicion_de--> Operacion:Cancelación de cartas de crédito o letras avaladas
  - Condicion:Cartas de crédito o letras avaladas emitidas a partir del 13/12/23 --condicion_de--> Obligacion:Documentación de importación con registro aduanero a partir del 13/12/…
  - Obligacion:Documentación de importación con registro aduanero a partir del 13/12/… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Operación no comprendida en punto 10.10.2.11 --condicion_de--> Obligacion:Pago garantizado a partir de plazo de bien más 15 días
  - Obligacion:Pago garantizado a partir de plazo de bien más 15 días --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Cartas de crédito o letras avaladas emitidas a partir del 14/04/25 --condicion_de--> Excepcion:Pago a partir de fecha estimada de embarque más 15 días
  - Excepcion:Pago a partir de fecha estimada de embarque más 15 días --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - TextoOrdenado:Texto Ordenado Exterior Cambios --referencia--> Comunicacion:Com. A 7914
  - Obligacion:Boleto de venta a nombre de la entidad --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Operacion:Cancelación de cartas de crédito o letras avaladas --aplica_a--> La entidad
  - Obligacion:Documentación de importación con registro aduanero a partir del 13/12/… --aplica_a--> la entidad
  - Obligacion:Boleto de venta a nombre de la entidad --aplica_a--> la propia entidad
  - mención: aplica_a «La entidad» (verificada: exacta)
  - mención: aplica_a «la entidad» (verificada: exacta)
  - mención: aplica_a «la propia entidad» (verificada: exacta)
  - omisión meta_normativo (exacta): «Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.…» — nota: 
  - heredado_compuesto: 0

## Ficha 5 — `cap::10.2.2.4`

**Texto propio:**

```
10.2.2.4. Divulgación.
Las ECAI deberán divulgar la siguiente información: su código de conducta;
el carácter general de sus acuerdos de remuneración con las entidades eva-
luadas; sus métodos de evaluación, incluida la definición de incumplimiento,
el horizonte temporal y el significado de cada calificación; las tasas de in-
cumplimiento efectivamente registradas en cada categoría de evaluación y la
transición entre las calificaciones –es decir, la probabilidad de migrar entre
calificaciones–.
```
**Heredado:** Sección 10. Agentes de calificación externa (ECAI). / 10.2. Criterios de elegibilidad. / 10.2.2. Condiciones. / Las ECAI deberán cumplir cada uno de los siguientes seis criterios:

**A** — error: None; salida: 1750 tokens

- Obligacion «Divulgación código de conducta»: Las ECAI deberán divulgar su código de conducta como parte de la información requerida en materia de divulgación. ‖ tramo (exacta): «Las ECAI deberán divulgar la siguiente información: su código de conducta»
- Obligacion «Divulgación carácter general acuerdos remuneración»: Las ECAI deberán divulgar el carácter general de sus acuerdos de remuneración con las entidades evaluadas. ‖ tramo (exacta): «el carácter general de sus acuerdos de remuneración con las entidades evaluadas»
- Obligacion «Divulgación métodos de evaluación»: Las ECAI deberán divulgar sus métodos de evaluación, incluida la definición de incumplimiento, el horizonte temporal y el significado de cada calificación. ‖ tramo (exacta): «sus métodos de evaluación, incluida la definición de incumplimiento, el horizonte temporal y el significado de cada calificación»
- Obligacion «Divulgación tasas incumplimiento y transición calificaciones»: Las ECAI deberán divulgar las tasas de incumplimiento efectivamente registradas en cada categoría de evaluación y la transición entre las calificaciones, es decir, la probabilidad de migrar entre calificaciones. ‖ tramo (exacta): «las tasas de incumplimiento efectivamente registradas en cada categoría de evaluación y la transición entre las calificaciones –es decir, la probabilidad de migrar entre calificaciones–»
- Condicion «Cumplimiento de seis criterios de elegibilidad»: Las ECAI deben cumplir cada uno de los seis criterios de elegibilidad enumerados, de los cuales la divulgación es uno. ‖ tramo (exacta): «Las ECAI deberán cumplir cada uno de los siguientes seis criterios»
  - Obligacion:Divulgación código de conducta --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Divulgación carácter general acuerdos remuneración --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Divulgación métodos de evaluación --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Divulgación tasas incumplimiento y transición calificaciones --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Cumplimiento de seis criterios de elegibilidad --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Divulgación código de conducta --aplica_a--> Las ECAI
  - Obligacion:Divulgación carácter general acuerdos remuneración --aplica_a--> Las ECAI
  - Obligacion:Divulgación métodos de evaluación --aplica_a--> Las ECAI
  - Obligacion:Divulgación tasas incumplimiento y transición calificaciones --aplica_a--> Las ECAI
  - Condicion:Cumplimiento de seis criterios de elegibilidad --condicion_de--> Obligacion:Divulgación código de conducta
  - Condicion:Cumplimiento de seis criterios de elegibilidad --condicion_de--> Obligacion:Divulgación carácter general acuerdos remuneración
  - Condicion:Cumplimiento de seis criterios de elegibilidad --condicion_de--> Obligacion:Divulgación métodos de evaluación
  - Condicion:Cumplimiento de seis criterios de elegibilidad --condicion_de--> Obligacion:Divulgación tasas incumplimiento y transición calificaciones
  - mención: aplica_a «Las ECAI» (verificada: exacta)
  - mención: aplica_a «Las ECAI» (verificada: exacta)
  - mención: aplica_a «Las ECAI» (verificada: exacta)
  - mención: aplica_a «Las ECAI» (verificada: exacta)
  - rechazo: firma_invalida: relations[9]: Condicion --aplica_a--> Sujeto
  - heredado_compuesto: 0

**B** — error: None; salida: 1747 tokens

- Obligacion «Divulgación código de conducta»: Las ECAI deberán divulgar su código de conducta como parte de la información requerida en materia de divulgación. ‖ tramo (exacta): «Las ECAI deberán divulgar la siguiente información: su código de conducta»
- Obligacion «Divulgación carácter general acuerdos remuneración»: Las ECAI deberán divulgar el carácter general de sus acuerdos de remuneración con las entidades evaluadas. ‖ tramo (exacta): «el carácter general de sus acuerdos de remuneración con las entidades evaluadas»
- Obligacion «Divulgación métodos de evaluación»: Las ECAI deberán divulgar sus métodos de evaluación, incluida la definición de incumplimiento, el horizonte temporal y el significado de cada calificación. ‖ tramo (exacta): «sus métodos de evaluación, incluida la definición de incumplimiento, el horizonte temporal y el significado de cada calificación»
- Obligacion «Divulgación tasas incumplimiento y transición calificaciones»: Las ECAI deberán divulgar las tasas de incumplimiento efectivamente registradas en cada categoría de evaluación y la transición entre las calificaciones, es decir, la probabilidad de migrar entre calificaciones. ‖ tramo (exacta): «las tasas de incumplimiento efectivamente registradas en cada categoría de evaluación y la transición entre las calificaciones –es decir, la probabilidad de migrar entre calificaciones–»
- Condicion «Cumplimiento de seis criterios de elegibilidad»: Las ECAI deben cumplir cada uno de los seis criterios de elegibilidad enumerados, incluido el de divulgación. ‖ tramo (exacta): «Las ECAI deberán cumplir cada uno de los siguientes seis criterios»
  - Obligacion:Divulgación código de conducta --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Divulgación carácter general acuerdos remuneración --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Divulgación métodos de evaluación --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Divulgación tasas incumplimiento y transición calificaciones --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Cumplimiento de seis criterios de elegibilidad --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Divulgación código de conducta --aplica_a--> Las ECAI
  - Obligacion:Divulgación carácter general acuerdos remuneración --aplica_a--> Las ECAI
  - Obligacion:Divulgación métodos de evaluación --aplica_a--> Las ECAI
  - Obligacion:Divulgación tasas incumplimiento y transición calificaciones --aplica_a--> Las ECAI
  - Condicion:Cumplimiento de seis criterios de elegibilidad --condicion_de--> Obligacion:Divulgación código de conducta
  - Condicion:Cumplimiento de seis criterios de elegibilidad --condicion_de--> Obligacion:Divulgación carácter general acuerdos remuneración
  - Condicion:Cumplimiento de seis criterios de elegibilidad --condicion_de--> Obligacion:Divulgación métodos de evaluación
  - Condicion:Cumplimiento de seis criterios de elegibilidad --condicion_de--> Obligacion:Divulgación tasas incumplimiento y transición calificaciones
  - mención: aplica_a «Las ECAI» (verificada: exacta)
  - mención: aplica_a «Las ECAI» (verificada: exacta)
  - mención: aplica_a «Las ECAI» (verificada: exacta)
  - mención: aplica_a «Las ECAI» (verificada: exacta)
  - rechazo: firma_invalida: relations[9]: Condicion --aplica_a--> Sujeto
  - heredado_compuesto: 0

## Ficha 6 — `ext::3.5.3.5`

**Texto propio:**

```
3.5.3.5. Precancelación de capital e intereses por parte de un VPU adherido al RIGI.
El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de
Incentivo para Grandes Inversiones (RIGI) que precancela capital o intereses
devengados por endeudamientos financieros comprendidos en este punto
3.5. en el marco de lo previsto en el punto 14.2.1.
```
**Heredado:** Sección 3. Disposiciones específicas para los egresos por el mercado de cambios / Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas… / 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el / exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el p… / 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 / (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar. En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado… / i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25. ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25. iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25. / El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:

**A** — error: None; salida: 1040 tokens

- Condicion «Cliente es VPU adherido al RIGI»: El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) ‖ tramo (exacta): «El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI)»
- Operacion «Precancelación de capital o intereses — endeudamientos financieros»: Precancelación de capital o intereses devengados por endeudamientos financieros comprendidos en el punto 3.5, realizada por un VPU adherido al RIGI en el marco de lo previsto en el punto 14.2.1 ‖ tramo (exacta): «precancela capital o intereses devengados por endeudamientos financieros comprendidos en este punto 3.5.»
- Excepcion «Excepción — acceso al mercado de cambios sin conformidad previa del BCRA»: El acceso al mercado de cambios para precancelación de capital o intereses por parte de un VPU adherido al RIGI no requiere conformidad previa del BCRA cuando se cumplen las condiciones estipuladas ‖ tramo (exacta): «Precancelación de capital e intereses por parte de un VPU adherido al RIGI»
  - Condicion:Cliente es VPU adherido al RIGI --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Operacion:Precancelación de capital o intereses — endeudamientos financieros --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Excepcion:Excepción — acceso al mercado de cambios sin conformidad previa del BC… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Cliente es VPU adherido al RIGI --condicion_de--> Excepcion:Excepción — acceso al mercado de cambios sin conformidad previa del BC…
  - Excepcion:Excepción — acceso al mercado de cambios sin conformidad previa del BC… --aplica_a--> un VPU adherido al RIGI
  - mención: aplica_a «un VPU adherido al RIGI» (verificada: exacta)
  - omisión relacion_sin_predicado (exacta): «en el marco de lo previsto en el punto 14.2.1» — nota: remisión a otra norma (punto 14.2.1); no es una relación entre entidades del chunk
  - heredado_compuesto: 0

**B** — error: None; salida: 802 tokens

- Condicion «VPU adherido al RIGI precancela capital o intereses»: El cliente es un VPU adherido al RIGI que precancela capital o intereses devengados por endeudamientos financieros comprendidos en el punto 3.5. ‖ tramo (exacta): «El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que precancela capital o intereses devengados por endeudamientos financieros comprend…»
- Excepcion «Excepción — Precancelación VPU RIGI sin conformidad previa BCRA»: Excepción a la exigencia de conformidad previa del BCRA para acceso al mercado de cambios antes de lo indicado en 3.5.3, cuando el cliente es un VPU adherido al RIGI que precancela capital o intereses en el marco del punto 14.2.1. ‖ tramo (exacta): «El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que precancela capital o intereses devengados por endeudamientos financieros comprend…»
  - Condicion:VPU adherido al RIGI precancela capital o intereses --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Excepcion:Excepción — Precancelación VPU RIGI sin conformidad previa BCRA --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - omisión relacion_sin_predicado (exacta): «en el marco de lo previsto en el punto 14.2.1» — nota: remisión a otra norma (punto 14.2.1); no se emite como relación entre entidades del chunk
  - heredado_compuesto: 0

## Ficha 7 — `ctacte::3.2.2`

**Texto propio:**

```
3.2.2. Existencia de tachaduras o enmiendas no salvadas por el librador.
```
**Heredado:** Sección 3. Cheques. / 3.2. Títulos que carecen de valor como cheques. / El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque: / Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones.

**A** — error: None; salida: 640 tokens

- Restriccion «Prohibición — tachaduras o enmiendas no salvadas»: El título que presente tachaduras o enmiendas no salvadas por el librador no valdrá como cheque. ‖ tramo (exacta): «Existencia de tachaduras o enmiendas no salvadas por el librador»
  - Restriccion:Prohibición — tachaduras o enmiendas no salvadas --establecida_en--> TextoOrdenado:Texto Ordenado Cuentas de Corresponsalía
  - rechazo: ref_colgante: relations[1] (prohibe): source='e1' target='e2'
  - omisión fuera_de_tipos (exacta): «Existencia de tachaduras o enmiendas no salvadas por el librador» — nota: El punto enuncia una situación (la existencia de tachaduras o enmiendas no salvadas) que es el supuesto de la prohibición de que el título v…
  - heredado_compuesto: 0

**B** — error: None; salida: 633 tokens

- Restriccion «Prohibición — cheques con tachaduras o enmiendas no salvadas»: El título respecto del que exista tachaduras o enmiendas no salvadas por el librador no valdrá como cheque. ‖ tramo (exacta): «Existencia de tachaduras o enmiendas no salvadas por el librador»
- Operacion «Cheque con tachaduras o enmiendas no salvadas»: Cheque que presenta tachaduras o enmiendas no salvadas por el librador. ‖ tramo (exacta): «Existencia de tachaduras o enmiendas no salvadas por el librador»
  - Restriccion:Prohibición — cheques con tachaduras o enmiendas no salvadas --establecida_en--> TextoOrdenado:Texto Ordenado Cuentas de Corresponsalía
  - Restriccion:Prohibición — cheques con tachaduras o enmiendas no salvadas --prohibe--> Operacion:Cheque con tachaduras o enmiendas no salvadas
  - omisión meta_normativo (exacta): «no valdrá como cheque» — nota: Cláusula que predica sobre el significado o efecto jurídico de la operación (que no tiene validez como cheque), no sobre la conducta de un s…
  - heredado_compuesto: 0

## Ficha 8 — `cla::5.1.1.1`

**Texto propio:**

```
5.1.1.1. Los créditos para consumo o vivienda.
Los créditos de esta clase que superen el equivalente a dos veces el importe de
referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado
a ingresos fijos o periódicos del cliente sino a la evolución de su actividad pro-
ductiva o comercial se incluirán dentro de la cartera comercial.
```
**Heredado:** Sección 5. Categorías de carteras. / 5.1. Categorías. / La cartera se agrupará en dos categorías básicas: / 5.1.1. Cartera comercial. / Abarca todas las financiaciones comprendidas, con excepción de las siguientes:

**A** — error: None; salida: 1316 tokens

- Operacion «Créditos para consumo o vivienda»: Créditos destinados a consumo o vivienda ‖ tramo (exacta): «Los créditos para consumo o vivienda»
- Condicion «Crédito supera dos veces importe referencia punto 3.7»: El crédito supera el equivalente a dos veces el importe de referencia establecido en el punto 3.7 ‖ tramo (exacta): «que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7.» ‖ umbrales: ['superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7']
- Condicion «Repago no vinculado a ingresos fijos o periódicos»: El repago no se encuentra vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial ‖ tramo (exacta): «cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial»
- Operacion «Inclusión en cartera comercial»: Inclusión del crédito dentro de la cartera comercial ‖ tramo (exacta): «se incluirán dentro de la cartera comercial»
- Excepcion «Excepción créditos consumo/vivienda de cartera comercial»: Los créditos para consumo o vivienda quedan exceptuados de la cartera comercial, salvo aquellos que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7 y cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su acti… ‖ tramo (exacta): «Los créditos para consumo o vivienda. Los créditos de esta clase que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado a …»
  - Excepcion:Excepción créditos consumo/vivienda de cartera comercial --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Condicion:Crédito supera dos veces importe referencia punto 3.7 --condicion_de--> Operacion:Inclusión en cartera comercial
  - Condicion:Repago no vinculado a ingresos fijos o periódicos --condicion_de--> Operacion:Inclusión en cartera comercial
  - rechazo: firma_invalida: relations[3]: Excepcion --exceptua--> Operacion
  - omisión relacion_sin_predicado (exacta): «Abarca todas las financiaciones comprendidas, con excepción de las siguientes» — nota: Relación entre la cartera comercial (punto 5.1.1) y la excepción de créditos para consumo o vivienda; predicado sugerido: 'exceptua_de_categ…
  - heredado_compuesto: 0

**B** — error: None; salida: 1531 tokens

- Operacion «Créditos para consumo o vivienda»: Créditos destinados a consumo o vivienda ‖ tramo (exacta): «Los créditos para consumo o vivienda»
- Condicion «Monto superior a dos veces importe referencia»: El crédito supera el equivalente a dos veces el importe de referencia establecido en el punto 3.7 ‖ tramo (exacta): «superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7.» ‖ umbrales: ['superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7.']
- Condicion «Repago vinculado a actividad productiva o comercial»: El repago no está vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial ‖ tramo (exacta): «cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial»
- Operacion «Inclusión en cartera comercial»: Inclusión del crédito dentro de la cartera comercial ‖ tramo (exacta): «se incluirán dentro de la cartera comercial»
- Excepcion «Excepción créditos consumo/vivienda de cartera comercial»: Los créditos para consumo o vivienda quedan exceptuados de la cartera comercial, salvo cuando superen el equivalente a dos veces el importe de referencia y su repago esté vinculado a la evolución de la actividad productiva o comercial del cliente ‖ tramo (exacta): «Los créditos para consumo o vivienda»
  - Operacion:Créditos para consumo o vivienda --establecida_en--> TextoOrdenado:Texto Ordenado de Clasificación de Deudores
  - Condicion:Monto superior a dos veces importe referencia --establecida_en--> TextoOrdenado:Texto Ordenado de Clasificación de Deudores
  - Condicion:Repago vinculado a actividad productiva o comercial --establecida_en--> TextoOrdenado:Texto Ordenado de Clasificación de Deudores
  - Operacion:Inclusión en cartera comercial --establecida_en--> TextoOrdenado:Texto Ordenado de Clasificación de Deudores
  - Excepcion:Excepción créditos consumo/vivienda de cartera comercial --establecida_en--> TextoOrdenado:Texto Ordenado de Clasificación de Deudores
  - Condicion:Monto superior a dos veces importe referencia --condicion_de--> Operacion:Inclusión en cartera comercial
  - Condicion:Repago vinculado a actividad productiva o comercial --condicion_de--> Operacion:Inclusión en cartera comercial
  - rechazo: firma_invalida: relations[7]: Excepcion --exceptua--> Operacion
  - omisión relacion_sin_predicado (exacta): «Los créditos de esta clase que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado …» — nota: La relación entre la Operacion (créditos para consumo/vivienda) y la Operacion (inclusión en cartera comercial) podría ser 'condiciona' (Obl…
  - heredado_compuesto: 0

## Ficha 9 — `ext::6.1.1`

**Texto propio:**

```
6.1.1. Monedas y billetes en moneda extranjera.
Comprende monedas y billetes emitidos por un estado extranjero.
```
**Heredado:** Sección 6. Definiciones. / En el marco de estas disposiciones se definen los siguientes conceptos: / 6.1. Instrumentos operados en el mercado de cambios.

**A = B (iguales byte a byte)** — error: None; salida: 316 tokens

- Definicion «Monedas y billetes en moneda extranjera»: Monedas y billetes emitidos por un estado extranjero. ‖ tramo (exacta): «Comprende monedas y billetes emitidos por un estado extranjero.»
  - Definicion:Monedas y billetes en moneda extranjera --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - heredado_compuesto: 0

## Ficha 10 — `ext::13.1.4`

**Texto propio:**

```
13.1.4. Si se trata de pagos de deudas por servicios de no residentes que fueron prestados
y/o devengados hasta el 12/12/23, la entidad deberá verificar que la operación
encuadra en alguna de las situaciones previstas en el punto 13.4.
Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre
(BOPREAL) por hasta el monto de la deuda pendiente de pago por estas
operaciones en la medida que se cumplan los requisitos previstos en el punto 4.5.
```
**Heredado:** Sección 13. Pagos de servicios prestados por no residentes. / 13.1. Disposiciones generales. / Las entidades podrán dar acceso al mercado de cambios por pagos de servicios prestados por no residentes en la medida que se cumplan las siguientes condiciones: / Los casos que no encuadren en lo expuesto precedentemente quedan sujetos a la conformidad previa del BCRA, debiendo los pedidos ser canalizados por una entidad autorizada a realizar este tipo de pagos.

**A** — error: None; salida: 1543 tokens

- Condicion «Servicios prestados hasta 12/12/23»: La operación refiere a pagos de deudas por servicios de no residentes que fueron prestados y/o devengados hasta el 12 de diciembre de 2023 ‖ tramo (exacta): «Si se trata de pagos de deudas por servicios de no residentes que fueron prestados y/o devengados hasta el 12/12/23» ‖ umbrales: ['hasta el 12/12/23']
- Obligacion «Verificar encuadre en situaciones punto 13.4»: La entidad deberá verificar que la operación encuadra en alguna de las situaciones previstas en el punto 13.4 ‖ tramo (exacta): «la entidad deberá verificar que la operación encuadra en alguna de las situaciones previstas en el punto 13.4»
- Potestad «Suscripción BOPREAL hasta monto deuda pendiente»: Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por estas operaciones ‖ tramo (exacta): «Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por estas operaciones»
- Condicion «Cumplimiento requisitos punto 4.5»: Se cumplen los requisitos previstos en el punto 4.5 ‖ tramo (exacta): «en la medida que se cumplan los requisitos previstos en el punto 4.5»
- Operacion «Pago de deuda por servicios de no residentes»: Pago de deuda por servicios prestados por no residentes ‖ tramo (exacta): «pagos de deudas por servicios de no residentes»
  - Condicion:Servicios prestados hasta 12/12/23 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Verificar encuadre en situaciones punto 13.4 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Potestad:Suscripción BOPREAL hasta monto deuda pendiente --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Cumplimiento requisitos punto 4.5 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Operacion:Pago de deuda por servicios de no residentes --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Servicios prestados hasta 12/12/23 --condicion_de--> Obligacion:Verificar encuadre en situaciones punto 13.4
  - Condicion:Cumplimiento requisitos punto 4.5 --condicion_de--> Potestad:Suscripción BOPREAL hasta monto deuda pendiente
  - Obligacion:Verificar encuadre en situaciones punto 13.4 --aplica_a--> la entidad
  - Potestad:Suscripción BOPREAL hasta monto deuda pendiente --aplica_a--> Los clientes
  - mención: aplica_a «la entidad» (verificada: exacta)
  - mención: aplica_a «Los clientes» (verificada: exacta)
  - omisión relacion_sin_predicado (exacta): «la entidad deberá verificar que la operación encuadra en alguna de las situaciones previstas en el punto 13.4» — nota: relación entre Obligacion (e2) y Operacion (e5): el deber de verificar se refiere a la operación de pago, pero el vínculo no encaja en regul…
  - heredado_compuesto: 0

**B** — error: None; salida: 1796 tokens

- Condicion «Servicios prestados hasta 12/12/23»: La operación refiere a pagos de deudas por servicios de no residentes que fueron prestados y/o devengados hasta el 12 de diciembre de 2023. ‖ tramo (exacta): «Si se trata de pagos de deudas por servicios de no residentes que fueron prestados y/o devengados hasta el 12/12/23» ‖ umbrales: ['hasta el 12/12/23']
- Obligacion «Verificar encuadre en situaciones punto 13.4»: La entidad deberá verificar que la operación encuadra en alguna de las situaciones previstas en el punto 13.4. ‖ tramo (exacta): «la entidad deberá verificar que la operación encuadra en alguna de las situaciones previstas en el punto 13.4»
- Potestad «Suscripción BOPREAL hasta monto deuda pendiente»: Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por estas operaciones. ‖ tramo (exacta): «Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por estas operaciones»
- Condicion «Cumplimiento requisitos punto 4.5»: Se cumplan los requisitos previstos en el punto 4.5. ‖ tramo (exacta): «en la medida que se cumplan los requisitos previstos en el punto 4.5»
- Operacion «Pago de deuda por servicios de no residentes»: Pago de deuda por servicios prestados por no residentes. ‖ tramo (exacta): «pagos de deudas por servicios de no residentes»
- Operacion «Suscripción de BOPREAL»: Suscripción de Bonos para la Reconstrucción de una Argentina Libre (BOPREAL). ‖ tramo (exacta): «suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL)»
  - Condicion:Servicios prestados hasta 12/12/23 --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Obligacion:Verificar encuadre en situaciones punto 13.4 --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Potestad:Suscripción BOPREAL hasta monto deuda pendiente --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Condicion:Cumplimiento requisitos punto 4.5 --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Operacion:Pago de deuda por servicios de no residentes --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Operacion:Suscripción de BOPREAL --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Condicion:Servicios prestados hasta 12/12/23 --condicion_de--> Obligacion:Verificar encuadre en situaciones punto 13.4
  - Condicion:Cumplimiento requisitos punto 4.5 --condicion_de--> Potestad:Suscripción BOPREAL hasta monto deuda pendiente
  - Obligacion:Verificar encuadre en situaciones punto 13.4 --regula--> Operacion:Pago de deuda por servicios de no residentes
  - Obligacion:Verificar encuadre en situaciones punto 13.4 --aplica_a--> la entidad
  - Potestad:Suscripción BOPREAL hasta monto deuda pendiente --aplica_a--> Los clientes
  - mención: aplica_a «la entidad» (verificada: exacta)
  - mención: aplica_a «Los clientes» (verificada: exacta)
  - omisión meta_normativo (exacta): «Los casos que no encuadren en lo expuesto precedentemente quedan sujetos a la conformidad previa del BCRA, debiendo los pedidos ser canalizados por una entidad …» — nota: Párrafo de cierre del punto 13.1 (contexto heredado); no se extrae contenido normativo del contexto heredado salvo composición con encabezad…
  - heredado_compuesto: 0

## Ficha 11 — `cap::6.3.2.1`

**Texto propio:**

```
6.3.2.1. Cálculo de las posiciones.
Para el cálculo de las exigencias por riesgo específico y riesgo general de
mercado, las posiciones en derivados deberán convertirse en nocionales:
i) Los futuros y “forwards” sobre acciones individuales deberán declararse
al precio de mercado del subyacente.
ii) Los futuros sobre índices bursátiles deberán declararse al valor de mer-
cado del nocional de la cartera de acciones subyacente.
iii) Los “swaps” de acciones se considerarán como dos posiciones nociona-
les.
iv) Las opciones sobre acciones e índices bursátiles se excluirán junto con
sus subyacentes –si se utiliza el método simplificado– o bien se incorpo-
rarán a la medida de riesgo general de mercado –si se utiliza el método
delta-plus–.
```
**Heredado:** Sección 6. Capital mínimo por riesgo de mercado. / 6.3. Exigencia de capital por riesgo de posiciones en acciones. / La exigencia de capital por el riesgo de mantener posiciones en acciones en la cartera de ne- gociación alcanza a las posiciones compradas y vendidas en acciones ordinarias, títulos de deuda convertibles que se comporten como acciones y los compromisos para ad… / 6.3.2. Tratamiento de los derivados sobre acciones. / A excepción de las opciones sobre acciones e índices bursátiles, que se tratan en el punto 6.6., los restantes derivados sobre acciones y las posiciones fuera de balance sensibles a los cambios en los precios de mercado deberán incluirse en el cómputo de la ex…

**A** — error: None; salida: 1486 tokens

- Operacion «Conversión de derivados a posiciones nocionales»: Para el cálculo de las exigencias por riesgo específico y riesgo general de mercado, las posiciones en derivados deberán convertirse en nocionales ‖ tramo (exacta): «las posiciones en derivados deberán convertirse en nocionales»
- Obligacion «Declaración futuros/forwards acciones — precio de mercado»: Los futuros y forwards sobre acciones individuales deberán declararse al precio de mercado del subyacente ‖ tramo (exacta): «Los futuros y "forwards" sobre acciones individuales deberán declararse al precio de mercado del subyacente»
- Obligacion «Declaración futuros índices bursátiles — valor nocional»: Los futuros sobre índices bursátiles deberán declararse al valor de mercado del nocional de la cartera de acciones subyacente ‖ tramo (exacta): «Los futuros sobre índices bursátiles deberán declararse al valor de mercado del nocional de la cartera de acciones subyacente»
- Operacion «Tratamiento swaps de acciones — dos posiciones nocionales»: Los swaps de acciones se considerarán como dos posiciones nocionales ‖ tramo (exacta): «Los "swaps" de acciones se considerarán como dos posiciones nocionales»
- Excepcion «Exclusión opciones — método simplificado»: Las opciones sobre acciones e índices bursátiles se excluirán junto con sus subyacentes cuando se utiliza el método simplificado ‖ tramo (exacta): «Las opciones sobre acciones e índices bursátiles se excluirán junto con sus subyacentes –si se utiliza el método simplificado–»
- Obligacion «Incorporación opciones — método delta-plus»: Las opciones sobre acciones e índices bursátiles se incorporarán a la medida de riesgo general de mercado cuando se utiliza el método delta-plus ‖ tramo (no): «Las opciones sobre acciones e índices bursátiles se incorporarán a la medida de riesgo general de mercado –si se utiliza el método delta-plus–»
  - Operacion:Conversión de derivados a posiciones nocionales --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Declaración futuros/forwards acciones — precio de mercado --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Declaración futuros índices bursátiles — valor nocional --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Operacion:Tratamiento swaps de acciones — dos posiciones nocionales --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Excepcion:Exclusión opciones — método simplificado --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Incorporación opciones — método delta-plus --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - omisión fuera_de_tipos (exacta): «Para el cálculo de las exigencias por riesgo específico y riesgo general de mercado» — nota: Cláusula introductoria que enuncia el ámbito de aplicación de las obligaciones siguientes; no es una norma autónoma sino contexto de las obl…
  - heredado_compuesto: 0

**B** — error: None; salida: 2650 tokens

- Operacion «Conversión nocional futuros/forwards acciones individuales»: Los futuros y forwards sobre acciones individuales se convierten a posiciones nocionales declarándose al precio de mercado del subyacente. ‖ tramo (exacta): «Los futuros y "forwards" sobre acciones individuales deberán declararse al precio de mercado del subyacente.»
- Operacion «Conversión nocional futuros índices bursátiles»: Los futuros sobre índices bursátiles se convierten a posiciones nocionales declarándose al valor de mercado del nocional de la cartera de acciones subyacente. ‖ tramo (exacta): «Los futuros sobre índices bursátiles deberán declararse al valor de mercado del nocional de la cartera de acciones subyacente.»
- Operacion «Conversión nocional swaps acciones»: Los swaps de acciones se convierten en dos posiciones nocionales. ‖ tramo (exacta): «Los "swaps" de acciones se considerarán como dos posiciones nocionales.»
- Obligacion «Declaración nocional futuros/forwards acciones individuales»: Las entidades deberán declarar los futuros y forwards sobre acciones individuales al precio de mercado del subyacente para el cálculo de exigencias por riesgo específico y riesgo general de mercado. ‖ tramo (exacta): «Los futuros y "forwards" sobre acciones individuales deberán declararse al precio de mercado del subyacente.»
- Obligacion «Declaración nocional futuros índices bursátiles»: Las entidades deberán declarar los futuros sobre índices bursátiles al valor de mercado del nocional de la cartera de acciones subyacente para el cálculo de exigencias por riesgo específico y riesgo general de mercado. ‖ tramo (exacta): «Los futuros sobre índices bursátiles deberán declararse al valor de mercado del nocional de la cartera de acciones subyacente.»
- Obligacion «Consideración swaps acciones como dos posiciones»: Las entidades deberán considerar los swaps de acciones como dos posiciones nocionales para el cálculo de exigencias por riesgo específico y riesgo general de mercado. ‖ tramo (exacta): «Los "swaps" de acciones se considerarán como dos posiciones nocionales.»
- Excepcion «Exclusión opciones método simplificado»: Las opciones sobre acciones e índices bursátiles se excluyen del cálculo de exigencias junto con sus subyacentes cuando se utiliza el método simplificado. ‖ tramo (exacta): «Las opciones sobre acciones e índices bursátiles se excluirán junto con sus subyacentes –si se utiliza el método simplificado–»
- Excepcion «Incorporación opciones método delta-plus»: Las opciones sobre acciones e índices bursátiles se incorporan a la medida de riesgo general de mercado cuando se utiliza el método delta-plus. ‖ tramo (exacta): «o bien se incorporarán a la medida de riesgo general de mercado –si se utiliza el método delta-plus–.»
- Condicion «Condición método simplificado»: Cuando se utiliza el método simplificado para el cálculo de exigencias. ‖ tramo (exacta): «si se utiliza el método simplificado»
- Condicion «Condición método delta-plus»: Cuando se utiliza el método delta-plus para el cálculo de exigencias. ‖ tramo (exacta): «si se utiliza el método delta-plus»
  - Obligacion:Declaración nocional futuros/forwards acciones individuales --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Declaración nocional futuros índices bursátiles --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Consideración swaps acciones como dos posiciones --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Excepcion:Exclusión opciones método simplificado --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Excepcion:Incorporación opciones método delta-plus --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Condición método simplificado --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Condición método delta-plus --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Declaración nocional futuros/forwards acciones individuales --aplica_a--> las entidades
  - Obligacion:Declaración nocional futuros índices bursátiles --aplica_a--> las entidades
  - Obligacion:Consideración swaps acciones como dos posiciones --aplica_a--> las entidades
  - Excepcion:Exclusión opciones método simplificado --aplica_a--> las entidades
  - Excepcion:Incorporación opciones método delta-plus --aplica_a--> las entidades
  - Condicion:Condición método simplificado --condicion_de--> Excepcion:Exclusión opciones método simplificado
  - Condicion:Condición método delta-plus --condicion_de--> Excepcion:Incorporación opciones método delta-plus
  - mención: aplica_a «las entidades» (verificada: no)
  - mención: aplica_a «las entidades» (verificada: no)
  - mención: aplica_a «las entidades» (verificada: no)
  - mención: aplica_a «las entidades» (verificada: no)
  - mención: aplica_a «las entidades» (verificada: no)
  - omisión meta_normativo (exacta): «Para el cálculo de las exigencias por riesgo específico y riesgo general de mercado, las posiciones en derivados deberán convertirse en nocionales:» — nota: Enunciado introductorio que anuncia el contenido de los ítems sin prescribir conducta propia; el contenido normativo está en cada ítem.
  - heredado_compuesto: 0

## Ficha 12 — `cap::5.3.1.3`

**Texto propio:**

```
5.3.1.3. Excepciones a la aplicación del ponderador de riesgo mínimo.
El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior
al 20% en los siguientes casos:
i) Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0%
cuando la contraparte sea un “participante esencial del mercado” (punto
5.3.1.4.) y, además, se satisfaga la totalidad de las siguientes condiciones:
a) La exposición y el activo recibido en garantía consisten en efectivo o en
títulos valores emitidos por el sector público no financiero sujetos a un
ponderador de riesgo del 0%.
b) La exposición y el activo recibido en garantía estén denominados en la
misma moneda.
c) El plazo de vencimiento de la operación sea de un día hábil o bien la ex-
posición y el activo recibido en garantía se valúen diariamente a precios
de mercado y estén sujetos a liquidación/reposición diaria de márgenes.
d) Cuando una de las partes incumpla la liquidación/reposición de márge-
nes, el tiempo exigido entre la última valuación a precio de mercado pre-
via al incumplimiento y la liquidación del activo no supere los cuatro días
hábiles.
e) La operación se liquide a través de un sistema previamente comprobado
para este tipo de operaciones.
f) La documentación de la operación sea la documentación estándar para
las operaciones de pase con los títulos valores en cuestión.
g) La documentación de la operación contemple que, en el caso de que
una de las partes incumpla la obligación de entregar efectivo o títulos va-
lores o de reponer el margen o cualquier otra obligación, la operación se-
rá inmediatamente cancelable.
h) Ante cualquier evento de incumplimiento, la entidad financiera conserve
el derecho irrestricto y legalmente exigible de tomar inmediatamente po-
sesión del activo y liquidarlo para cobrar sus acreencias.
ii) Las operaciones de pase en las cuales la contraparte no sea un “participan-
te esencial del mercado” (punto 5.3.1.4.), pero que satisfagan las restantes
condiciones establecidas en el acápite i), estarán sujetas a un ponderador
de riesgo del 10%.
iii) Las operaciones en las que la exposición y el activo recibido en garantía es-
tén denominados en la misma moneda y el mencionado activo recibido sea
efectivo depositado en la entidad financiera, o títulos valores emitidos por el
sector público no financiero o instrumentos de regulación monetaria emitidos
por el BCRA a los que les corresponda un ponderador de riesgo del 0% y a
cuyo valor de mercado se le haya aplicado un aforo de al menos el 20%, es-
tarán sujetas a un ponderador de riesgo del 0%.
```
**Heredado:** Sección 5. Cobertura del riesgo de crédito. / A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera de inversión –tales como préstamos y responsabilidades eventu… / 5.3. Operaciones cubiertas con activos admitidos como garantía. / La aplicación de la técnica de cobertura mediante activos admitidos como garantía dependerá del método elegido. / 5.3.1. Método simple. / Con este método, el ponderador de riesgo de la contraparte se sustituye por el pondera- dor de riesgo del activo mediante el cual se cubre –parcial o totalmente– la exposición –conforme a la tabla de ponderadores prevista en la Sección 2.–.

**A** — error: None; salida: 5152 tokens

- Restriccion «Ponderador mínimo 20% — excepciones»: El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos: operaciones de pase con participante esencial del mercado (0%), operaciones de pase sin participante esencial (10%), operaciones con activo en efectivo o títulos públicos con aforo mínimo… ‖ tramo (exacta): «El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos:» ‖ umbrales: ['inferior al 20%']
- Operacion «Operación de pase con participante esencial»: Operación de pase en la cual la contraparte es un participante esencial del mercado, sujeta a ponderador de riesgo del 0%. ‖ tramo (exacta): «Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0% cuando la contraparte sea un "participante esencial del mercado"»
- Restriccion «Ponderador 0% — pase con participante esencial»: Operaciones de pase con participante esencial del mercado sujetas a ponderador de riesgo del 0%, siempre que se satisfagan todas las condiciones especificadas. ‖ tramo (exacta): «Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0% cuando la contraparte sea un "participante esencial del mercado"» ‖ umbrales: ['ponderador de riesgo del 0%']
- Condicion «Exposición y garantía en efectivo o títulos públicos 0%»: La exposición y el activo recibido en garantía deben consistir en efectivo o en títulos valores emitidos por el sector público no financiero sujetos a un ponderador de riesgo del 0%. ‖ tramo (exacta): «La exposición y el activo recibido en garantía consisten en efectivo o en títulos valores emitidos por el sector público no financiero sujetos a un ponderador de riesgo del 0%»
- Condicion «Exposición y garantía en misma moneda»: La exposición y el activo recibido en garantía deben estar denominados en la misma moneda. ‖ tramo (exacta): «La exposición y el activo recibido en garantía estén denominados en la misma moneda»
- Condicion «Plazo un día hábil o valuación diaria con reposición»: El plazo de vencimiento debe ser de un día hábil, o alternativamente, la exposición y el activo recibido en garantía deben valuarse diariamente a precios de mercado y estar sujetos a liquidación/reposición diaria de márgenes. ‖ tramo (exacta): «El plazo de vencimiento de la operación sea de un día hábil o bien la exposición y el activo recibido en garantía se valúen diariamente a precios de mercado y estén sujetos a liquidación/reposición di…»
- Condicion «Liquidación de activo en máximo cuatro días hábiles»: Cuando una de las partes incumpla la liquidación/reposición de márgenes, el tiempo entre la última valuación a precio de mercado previa al incumplimiento y la liquidación del activo no debe superar los cuatro días hábiles. ‖ tramo (exacta): «Cuando una de las partes incumpla la liquidación/reposición de márgenes, el tiempo exigido entre la última valuación a precio de mercado previa al incumplimiento y la liquidación del activo no supere …» ‖ umbrales: ['no supere los cuatro días hábiles']
- Condicion «Liquidación a través de sistema comprobado»: La operación debe liquidarse a través de un sistema previamente comprobado para este tipo de operaciones. ‖ tramo (exacta): «La operación se liquide a través de un sistema previamente comprobado para este tipo de operaciones»
- Condicion «Documentación estándar para operaciones de pase»: La documentación de la operación debe ser la documentación estándar para las operaciones de pase con los títulos valores en cuestión. ‖ tramo (exacta): «La documentación de la operación sea la documentación estándar para las operaciones de pase con los títulos valores en cuestión»
- Condicion «Cancelabilidad inmediata ante incumplimiento»: La documentación debe contemplar que ante incumplimiento de cualquier obligación (entrega de efectivo, títulos valores, reposición de margen u otra), la operación será inmediatamente cancelable. ‖ tramo (exacta): «La documentación de la operación contemple que, en el caso de que una de las partes incumpla la obligación de entregar efectivo o títulos valores o de reponer el margen o cualquier otra obligación, la…»
- Condicion «Derecho irrestricto a tomar posesión y liquidar activo»: Ante cualquier evento de incumplimiento, la entidad financiera debe conservar el derecho irrestricto y legalmente exigible de tomar inmediatamente posesión del activo y liquidarlo para cobrar sus acreencias. ‖ tramo (exacta): «Ante cualquier evento de incumplimiento, la entidad financiera conserve el derecho irrestricto y legalmente exigible de tomar inmediatamente posesión del activo y liquidarlo para cobrar sus acreencias»
- Operacion «Operación de pase sin participante esencial»: Operación de pase en la cual la contraparte no es un participante esencial del mercado, pero satisface las restantes condiciones del acápite i). ‖ tramo (exacta): «Las operaciones de pase en las cuales la contraparte no sea un "participante esencial del mercado"»
- Restriccion «Ponderador 10% — pase sin participante esencial»: Operaciones de pase sin participante esencial del mercado, que satisfagan las restantes condiciones del acápite i), sujetas a ponderador de riesgo del 10%. ‖ tramo (exacta): «Las operaciones de pase en las cuales la contraparte no sea un "participante esencial del mercado" [...] estarán sujetas a un ponderador de riesgo del 10%» ‖ umbrales: ['ponderador de riesgo del 10%']
- Operacion «Operación con garantía en efectivo o títulos públicos con aforo»: Operación en la que la exposición y el activo recibido en garantía están denominados en la misma moneda, y el activo recibido es efectivo depositado en la entidad financiera, o títulos valores emitidos por el sector público no financiero, o instrumentos de regulación monetaria emitidos por el BCRA, … ‖ tramo (exacta): «Las operaciones en las que la exposición y el activo recibido en garantía estén denominados en la misma moneda y el mencionado activo recibido sea efectivo depositado en la entidad financiera, o títul…»
- Restriccion «Ponderador 0% — garantía en efectivo/títulos públicos con aforo»: Operaciones con exposición y garantía en la misma moneda, donde el activo recibido es efectivo depositado en la entidad, o títulos públicos o instrumentos de regulación monetaria del BCRA con ponderador 0% y aforo mínimo 20%, sujetas a ponderador de riesgo del 0%. ‖ tramo (exacta): «Las operaciones en las que la exposición y el activo recibido en garantía estén denominados en la misma moneda y el mencionado activo recibido sea efectivo depositado en la entidad financiera, o títul…» ‖ umbrales: ['ponderador de riesgo del 0%', 'aforo de al menos el 20%']
- Condicion «Activo con ponderador 0% y aforo mínimo 20%»: El activo recibido debe tener un ponderador de riesgo del 0% y a su valor de mercado se le debe haber aplicado un aforo de al menos el 20%. ‖ tramo (exacta): «a los que les corresponda un ponderador de riesgo del 0% y a cuyo valor de mercado se le haya aplicado un aforo de al menos el 20%» ‖ umbrales: ['aforo de al menos el 20%']
  - Restriccion:Ponderador mínimo 20% — excepciones --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Ponderador 0% — pase con participante esencial --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Exposición y garantía en efectivo o títulos públicos 0% --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Exposición y garantía en misma moneda --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Plazo un día hábil o valuación diaria con reposición --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Liquidación de activo en máximo cuatro días hábiles --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Liquidación a través de sistema comprobado --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Documentación estándar para operaciones de pase --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Cancelabilidad inmediata ante incumplimiento --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Derecho irrestricto a tomar posesión y liquidar activo --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Ponderador 10% — pase sin participante esencial --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Ponderador 0% — garantía en efectivo/títulos públicos con aforo --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Ponderador 0% — pase con participante esencial --limita--> Operacion:Operación de pase con participante esencial
  - Condicion:Exposición y garantía en efectivo o títulos públicos 0% --condicion_de--> Restriccion:Ponderador 0% — pase con participante esencial
  - Condicion:Exposición y garantía en misma moneda --condicion_de--> Restriccion:Ponderador 0% — pase con participante esencial
  - Condicion:Plazo un día hábil o valuación diaria con reposición --condicion_de--> Restriccion:Ponderador 0% — pase con participante esencial
  - Condicion:Liquidación de activo en máximo cuatro días hábiles --condicion_de--> Restriccion:Ponderador 0% — pase con participante esencial
  - Condicion:Liquidación a través de sistema comprobado --condicion_de--> Restriccion:Ponderador 0% — pase con participante esencial
  - Condicion:Documentación estándar para operaciones de pase --condicion_de--> Restriccion:Ponderador 0% — pase con participante esencial
  - Condicion:Cancelabilidad inmediata ante incumplimiento --condicion_de--> Restriccion:Ponderador 0% — pase con participante esencial
  - Condicion:Derecho irrestricto a tomar posesión y liquidar activo --condicion_de--> Restriccion:Ponderador 0% — pase con participante esencial
  - Restriccion:Ponderador 10% — pase sin participante esencial --limita--> Operacion:Operación de pase sin participante esencial
  - Condicion:Exposición y garantía en misma moneda --condicion_de--> Restriccion:Ponderador 10% — pase sin participante esencial
  - Restriccion:Ponderador 0% — garantía en efectivo/títulos públicos con aforo --limita--> Operacion:Operación con garantía en efectivo o títulos públicos con aforo
  - Condicion:Activo con ponderador 0% y aforo mínimo 20% --condicion_de--> Restriccion:Ponderador 0% — garantía en efectivo/títulos públicos con aforo
  - Restriccion:Ponderador 0% — pase con participante esencial --aplica_a--> la entidad financiera
  - Restriccion:Ponderador 10% — pase sin participante esencial --aplica_a--> la entidad financiera
  - Restriccion:Ponderador 0% — garantía en efectivo/títulos públicos con aforo --aplica_a--> la entidad financiera
  - mención: aplica_a «la entidad financiera» (verificada: exacta)
  - mención: aplica_a «la entidad financiera» (verificada: exacta)
  - mención: aplica_a «la entidad financiera» (verificada: exacta)
  - omisión relacion_sin_predicado (exacta): «Las operaciones de pase en las cuales la contraparte no sea un "participante esencial del mercado" (punto 5.3.1.4.), pero que satisfagan las restantes condicion…» — nota: relación de herencia o referencia a condiciones del acápite i) que no tiene predicado específico
  - heredado_compuesto: 0

**B** — error: None; salida: 4880 tokens

- Restriccion «Ponderador mínimo 20% — excepciones»: El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos: operaciones de pase con participante esencial del mercado (0%), operaciones de pase sin participante esencial (10%), operaciones con exposición y activo en igual moneda y activo en efecti… ‖ tramo (exacta): «El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos:» ‖ umbrales: ['inferior al 20%']
- Operacion «Operaciones de pase con participante esencial»: Operaciones de pase con contraparte que sea participante esencial del mercado, sujetas a ponderador de riesgo del 0%. ‖ tramo (exacta): «Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0% cuando la contraparte sea un "participante esencial del mercado"»
- Condicion «Exposición y activo en efectivo o títulos públicos 0%»: La exposición y el activo recibido en garantía consisten en efectivo o en títulos valores emitidos por el sector público no financiero sujetos a un ponderador de riesgo del 0%. ‖ tramo (exacta): «La exposición y el activo recibido en garantía consisten en efectivo o en títulos valores emitidos por el sector público no financiero sujetos a un ponderador de riesgo del 0%.»
- Condicion «Exposición y activo en igual moneda»: La exposición y el activo recibido en garantía estén denominados en la misma moneda. ‖ tramo (exacta): «La exposición y el activo recibido en garantía estén denominados en la misma moneda.»
- Condicion «Plazo un día hábil o valuación diaria con reposición»: El plazo de vencimiento de la operación sea de un día hábil o bien la exposición y el activo recibido en garantía se valúen diariamente a precios de mercado y estén sujetos a liquidación/reposición diaria de márgenes. ‖ tramo (exacta): «El plazo de vencimiento de la operación sea de un día hábil o bien la exposición y el activo recibido en garantía se valúen diariamente a precios de mercado y estén sujetos a liquidación/reposición di…»
- Condicion «Liquidación activo dentro de cuatro días hábiles»: Cuando una de las partes incumpla la liquidación/reposición de márgenes, el tiempo exigido entre la última valuación a precio de mercado previa al incumplimiento y la liquidación del activo no supere los cuatro días hábiles. ‖ tramo (exacta): «Cuando una de las partes incumpla la liquidación/reposición de márgenes, el tiempo exigido entre la última valuación a precio de mercado previa al incumplimiento y la liquidación del activo no supere …» ‖ umbrales: ['no supere los cuatro días hábiles']
- Condicion «Liquidación a través de sistema comprobado»: La operación se liquide a través de un sistema previamente comprobado para este tipo de operaciones. ‖ tramo (exacta): «La operación se liquide a través de un sistema previamente comprobado para este tipo de operaciones.»
- Condicion «Documentación estándar para operaciones de pase»: La documentación de la operación sea la documentación estándar para las operaciones de pase con los títulos valores en cuestión. ‖ tramo (exacta): «La documentación de la operación sea la documentación estándar para las operaciones de pase con los títulos valores en cuestión.»
- Condicion «Cancelabilidad inmediata ante incumplimiento»: La documentación de la operación contemple que, en el caso de que una de las partes incumpla la obligación de entregar efectivo o títulos valores o de reponer el margen o cualquier otra obligación, la operación será inmediatamente cancelable. ‖ tramo (exacta): «La documentación de la operación contemple que, en el caso de que una de las partes incumpla la obligación de entregar efectivo o títulos valores o de reponer el margen o cualquier otra obligación, la…»
- Condicion «Derecho irrestricto a tomar posesión y liquidar activo»: Ante cualquier evento de incumplimiento, la entidad financiera conserve el derecho irrestricto y legalmente exigible de tomar inmediatamente posesión del activo y liquidarlo para cobrar sus acreencias. ‖ tramo (exacta): «Ante cualquier evento de incumplimiento, la entidad financiera conserve el derecho irrestricto y legalmente exigible de tomar inmediatamente posesión del activo y liquidarlo para cobrar sus acreencias…»
- Operacion «Operaciones de pase sin participante esencial»: Operaciones de pase con contraparte que no sea participante esencial del mercado, pero que satisfagan las restantes condiciones del acápite i), sujetas a ponderador de riesgo del 10%. ‖ tramo (exacta): «Las operaciones de pase en las cuales la contraparte no sea un "participante esencial del mercado" (punto 5.3.1.4.), pero que satisfagan las restantes condiciones establecidas en el acápite i), estará…»
- Operacion «Operaciones con exposición y activo en igual moneda con aforo»: Operaciones en las que la exposición y el activo recibido en garantía estén denominados en la misma moneda, el activo sea efectivo depositado en la entidad financiera, o títulos valores emitidos por el sector público no financiero o instrumentos de regulación monetaria emitidos por el BCRA con ponde… ‖ tramo (exacta): «Las operaciones en las que la exposición y el activo recibido en garantía estén denominados en la misma moneda y el mencionado activo recibido sea efectivo depositado en la entidad financiera, o títul…»
- Restriccion «Ponderador 0% — operaciones de pase con participante esencial»: Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0% cuando la contraparte sea un participante esencial del mercado y se satisfagan todas las condiciones especificadas (a-h). ‖ tramo (exacta): «Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0% cuando la contraparte sea un "participante esencial del mercado"» ‖ umbrales: ['ponderador de riesgo del 0%']
- Restriccion «Ponderador 10% — operaciones de pase sin participante esencial»: Las operaciones de pase en las cuales la contraparte no sea un participante esencial del mercado, pero que satisfagan las restantes condiciones del acápite i), estarán sujetas a un ponderador de riesgo del 10%. ‖ tramo (exacta): «Las operaciones de pase en las cuales la contraparte no sea un "participante esencial del mercado" (punto 5.3.1.4.), pero que satisfagan las restantes condiciones establecidas en el acápite i), estará…» ‖ umbrales: ['ponderador de riesgo del 10%']
- Restriccion «Ponderador 0% — operaciones con activo en igual moneda y aforo»: Las operaciones en las que la exposición y el activo recibido en garantía estén denominados en la misma moneda, el activo sea efectivo depositado en la entidad financiera, o títulos valores emitidos por el sector público no financiero o instrumentos de regulación monetaria emitidos por el BCRA con p… ‖ tramo (exacta): «Las operaciones en las que la exposición y el activo recibido en garantía estén denominados en la misma moneda y el mencionado activo recibido sea efectivo depositado en la entidad financiera, o títul…» ‖ umbrales: ['ponderador de riesgo del 0%', 'aforo de al menos el 20%']
  - Restriccion:Ponderador mínimo 20% — excepciones --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Ponderador 0% — operaciones de pase con participante esencial --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Ponderador 10% — operaciones de pase sin participante esencial --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Ponderador 0% — operaciones con activo en igual moneda y aforo --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Exposición y activo en efectivo o títulos públicos 0% --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Exposición y activo en igual moneda --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Plazo un día hábil o valuación diaria con reposición --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Liquidación activo dentro de cuatro días hábiles --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Liquidación a través de sistema comprobado --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Documentación estándar para operaciones de pase --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Cancelabilidad inmediata ante incumplimiento --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Derecho irrestricto a tomar posesión y liquidar activo --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Exposición y activo en efectivo o títulos públicos 0% --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Exposición y activo en igual moneda --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Plazo un día hábil o valuación diaria con reposición --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Liquidación activo dentro de cuatro días hábiles --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Liquidación a través de sistema comprobado --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Documentación estándar para operaciones de pase --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Cancelabilidad inmediata ante incumplimiento --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Derecho irrestricto a tomar posesión y liquidar activo --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Restriccion:Ponderador 0% — operaciones de pase con participante esencial --aplica_a--> la entidad financiera
  - Restriccion:Ponderador 10% — operaciones de pase sin participante esencial --aplica_a--> la entidad financiera
  - Restriccion:Ponderador 0% — operaciones con activo en igual moneda y aforo --aplica_a--> la entidad financiera
  - mención: aplica_a «la entidad financiera» (verificada: exacta)
  - mención: aplica_a «la entidad financiera» (verificada: exacta)
  - mención: aplica_a «la entidad financiera» (verificada: exacta)
  - omisión fuera_de_tipos (exacta): «punto 5.3.1.4.» — nota: Remisión a otro punto normativo; no es contenido normativo extraíble de esta unidad
  - heredado_compuesto: 0

## Ficha 13 — `ext::3.5.3.4`

**Texto propio:**

```
3.5.3.4. Precancelación de capital e intereses en forma simultánea con la liquidación
de un nuevo endeudamiento financiero otorgado por una entidad financiera
local a partir de una línea de crédito del exterior.
i) la precancelación de capital e intereses sea efectuada de manera
simultánea con los fondos liquidados de un nuevo endeudamiento
financiero otorgado por una entidad financiera local a partir de una línea
de crédito del exterior;
ii) la vida promedio del nuevo endeudamiento sea mayor a la vida
promedio remanente de la deuda que se precancela; y
iii) el monto acumulado de los vencimientos de capital del nuevo
endeudamiento en ningún momento, hasta la fecha de vencimiento de la
deuda que se cancela, podrá superar el monto que hubieran acumulado
los vencimientos de capital de la deuda que se cancela.
```
**Heredado:** Sección 3. Disposiciones específicas para los egresos por el mercado de cambios / Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas… / 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el / exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el p… / 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 / (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar. En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado… / i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25. ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25. iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25. / El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:

**A** — error: None; salida: 1809 tokens

- Operacion «Precancelación de capital e intereses con nuevo endeudamiento»: Precancelación de capital e intereses efectuada de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una línea de crédito del exterior ‖ tramo (exacta): «Precancelación de capital e intereses en forma simultánea con la liquidación de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una línea de crédito del exterio…»
- Condicion «Simultaneidad de precancelación y liquidación»: La precancelación debe efectuarse de manera simultánea con los fondos liquidados del nuevo endeudamiento ‖ tramo (exacta): «la precancelación de capital e intereses sea efectuada de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una lín…»
- Condicion «Vida promedio del nuevo endeudamiento mayor a remanente»: La vida promedio del nuevo endeudamiento debe ser mayor a la vida promedio remanente de la deuda que se precancela ‖ tramo (exacta): «la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente de la deuda que se precancela»
- Restriccion «Límite acumulado de vencimientos de capital del nuevo endeudamiento»: El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela ‖ tramo (exacta): «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los…» ‖ umbrales: ['en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela']
- Excepcion «Excepción a acceso anticipado al mercado de cambios»: Se exceptúa del requisito de conformidad previa del BCRA cuando el deudor encuadra en alguna de las situaciones especificadas y se cumplen todas las condiciones estipuladas ‖ tramo (exacta): «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las co…»
  - Operacion:Precancelación de capital e intereses con nuevo endeudamiento --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Simultaneidad de precancelación y liquidación --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Vida promedio del nuevo endeudamiento mayor a remanente --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Límite acumulado de vencimientos de capital del nuevo endeudamiento --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Excepcion:Excepción a acceso anticipado al mercado de cambios --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Simultaneidad de precancelación y liquidación --condicion_de--> Excepcion:Excepción a acceso anticipado al mercado de cambios
  - Condicion:Vida promedio del nuevo endeudamiento mayor a remanente --condicion_de--> Excepcion:Excepción a acceso anticipado al mercado de cambios
  - Excepcion:Excepción a acceso anticipado al mercado de cambios --aplica_a--> el deudor
  - mención: aplica_a «el deudor» (verificada: exacta)
  - rechazo: firma_invalida: relations[7]: Restriccion --condicion_de--> Excepcion
  - omisión meta_normativo (exacta): «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaci…» — nota: Contenido que predica sobre la estructura de la excepción (que se requiere conformidad previa salvo en ciertos casos), no una prescripción d…
  - heredado_compuesto: 1

**B** — error: None; salida: 1448 tokens

- Operacion «Precancelación de capital e intereses con nuevo endeudamiento»: Precancelación de capital e intereses efectuada de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una línea de crédito del exterior ‖ tramo (exacta): «Precancelación de capital e intereses en forma simultánea con la liquidación de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una línea de crédito del exterio…»
- Condicion «Simultaneidad con liquidación de nuevo endeudamiento»: La precancelación debe efectuarse de manera simultánea con los fondos liquidados del nuevo endeudamiento ‖ tramo (exacta): «la precancelación de capital e intereses sea efectuada de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una lín…»
- Condicion «Vida promedio del nuevo endeudamiento mayor a remanente»: La vida promedio del nuevo endeudamiento debe ser mayor a la vida promedio remanente de la deuda que se precancela ‖ tramo (exacta): «la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente de la deuda que se precancela»
- Restriccion «Límite monto acumulado vencimientos capital nuevo endeudamiento»: El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela ‖ tramo (exacta): «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los…» ‖ umbrales: ['en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela']
  - Operacion:Precancelación de capital e intereses con nuevo endeudamiento --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Simultaneidad con liquidación de nuevo endeudamiento --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Vida promedio del nuevo endeudamiento mayor a remanente --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Límite monto acumulado vencimientos capital nuevo endeudamiento --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Simultaneidad con liquidación de nuevo endeudamiento --condicion_de--> Operacion:Precancelación de capital e intereses con nuevo endeudamiento
  - Condicion:Vida promedio del nuevo endeudamiento mayor a remanente --condicion_de--> Operacion:Precancelación de capital e intereses con nuevo endeudamiento
  - Restriccion:Límite monto acumulado vencimientos capital nuevo endeudamiento --limita--> Operacion:Precancelación de capital e intereses con nuevo endeudamiento
  - omisión meta_normativo (exacta): «Precancelación de capital e intereses en forma simultánea con la liquidación de un nuevo endeudamiento financiero otorgado por una entidad financiera local a pa…» — nota: El título del punto enuncia la operación que se regula pero no prescribe conducta por sí solo; el contenido normativo está en los ítems que …
  - heredado_compuesto: 0

## Ficha 14 — `ext::10.4.3.6`

**Texto propio:**

```
10.4.3.6. Cuenta con la declaración jurada del cliente de que se compromete a
demostrar el registro de ingreso aduanero de los bienes dentro de los 90
(noventa) días corridos de la fecha de acceso al mercado de cambios, o en
su defecto, proceder dentro de ese plazo, al reingreso de las divisas desde
el exterior.
```
**Heredado:** Sección 10. Pagos de importaciones y otras compras de bienes en el exterior. / 10.4. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente. / 10.4.3. Requisitos de acceso para el pago de deudas comerciales o a la vista contra la / presentación de la documentación de embarque. La entidad interviniente podrá dar acceso al mercado de cambios para el pago al exterior en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos:

**A** — error: None; salida: 1065 tokens

- Operacion «Acceso al mercado de cambios para pago de importaciones»: Acceso al mercado de cambios para el pago al exterior de deudas comerciales o a la vista contra la presentación de documentación de embarque, cuando se cumplen los requisitos establecidos. ‖ tramo (exacta): «dar acceso al mercado de cambios para el pago al exterior»
- Obligacion «Declaración jurada de compromiso — registro aduanero o reingreso»: El cliente debe contar con una declaración jurada en la que se compromete a demostrar el registro de ingreso aduanero de los bienes dentro de los 90 días corridos de la fecha de acceso al mercado de cambios, o en su defecto, proceder dentro de ese plazo al reingreso de las divisas desde el exterior. ‖ tramo (exacta): «Cuenta con la declaración jurada del cliente de que se compromete a demostrar el registro de ingreso aduanero de los bienes dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de…» ‖ umbrales: ['dentro de los 90 (noventa) días corridos']
- Condicion «Verificación previa de cumplimiento de requisitos»: La entidad interviniente debe verificar previamente que se cumplen la totalidad de los requisitos enumerados, incluido el de la declaración jurada del cliente. ‖ tramo (exacta): «en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos»
  - Obligacion:Declaración jurada de compromiso — registro aduanero o reingreso --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Operacion:Acceso al mercado de cambios para pago de importaciones --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Verificación previa de cumplimiento de requisitos --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Operacion:Acceso al mercado de cambios para pago de importaciones --aplica_a--> La entidad interviniente
  - Condicion:Verificación previa de cumplimiento de requisitos --condicion_de--> Operacion:Acceso al mercado de cambios para pago de importaciones
  - Operacion:Acceso al mercado de cambios para pago de importaciones --requiere--> Obligacion:Declaración jurada de compromiso — registro aduanero o reingreso
  - mención: aplica_a «La entidad interviniente» (verificada: exacta)
  - heredado_compuesto: 0

**B** — error: None; salida: 976 tokens

- Operacion «Acceso al mercado de cambios para pago de importaciones»: Acceso al mercado de cambios para el pago al exterior de deudas comerciales o a la vista contra la presentación de documentación de embarque, en el contexto de importaciones de bienes con registro de ingreso aduanero pendiente. ‖ tramo (exacta): «dar acceso al mercado de cambios para el pago al exterior»
- Condicion «Declaración jurada de compromiso de demostración de ingreso aduanero»: El cliente debe contar con una declaración jurada en la que se compromete a demostrar el registro de ingreso aduanero de los bienes dentro de 90 días corridos de la fecha de acceso al mercado de cambios, o alternativamente proceder al reingreso de las divisas desde el exterior dentro de ese mismo pl… ‖ tramo (exacta): «Cuenta con la declaración jurada del cliente de que se compromete a demostrar el registro de ingreso aduanero de los bienes dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de…» ‖ umbrales: ['dentro de los 90 (noventa) días corridos']
  - Condicion:Declaración jurada de compromiso de demostración de ingreso aduanero --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Operacion:Acceso al mercado de cambios para pago de importaciones --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Declaración jurada de compromiso de demostración de ingreso aduanero --condicion_de--> Operacion:Acceso al mercado de cambios para pago de importaciones
  - Operacion:Acceso al mercado de cambios para pago de importaciones --aplica_a--> La entidad interviniente
  - mención: aplica_a «La entidad interviniente» (verificada: exacta)
  - omisión meta_normativo (exacta): «La entidad interviniente podrá dar acceso al mercado de cambios para el pago al exterior en la medida que verifique previamente que se cumplen la totalidad de l…» — nota: Enunciado introductorio que anuncia la lista de requisitos; el contenido normativo (la facultad de dar acceso condicionada a la verificación…
  - heredado_compuesto: 0

## Ficha 15 — `ext::3.5.3.1`

**Texto propio:**

```
3.5.3.1. Precancelación de capital e intereses con la liquidación de fondos
ingresados desde el exterior por la emisión de un nuevo título de deuda
comprendido en este punto 3.5.
i) la precancelación de capital sea efectuada en manera simultánea con la
liquidación de los fondos ingresados desde el exterior por la emisión de
un nuevo título de deuda comprendido en este punto 3.5. emitido en el
marco de una operación de refinanciación, recompra y/o rescate
anticipado de deuda.
a) el nuevo título de deuda contempla 1 (un) año de gracia para el
pago de capital y su vida promedio es al menos 2 (dos) años mayor
a la vida promedio remanente de la deuda que se precancela; y
b) el monto acumulado de los vencimientos de capital del nuevo
endeudamiento en ningún momento podrá superar, hasta la fecha
de vencimiento de la deuda que se cancela, el monto que hubieran
acumulado los vencimientos de capital de la deuda que se cancela.
ii) la precancelación de intereses corresponde a los intereses devengados
por la deuda refinanciada hasta la fecha de cierre de la operación de
recompra y/o rescate, sin necesidad de que exista una liquidación de
fondos por el monto equivalente;
Adicionalmente, la entidad podrá darle acceso al mercado de cambios al
cliente para:
iii) pagar en concepto de prima de recompra, de rescate anticipado o
similar hasta el equivalente del 5% (cinco por ciento) del monto del
capital de la deuda recomprada y/o rescatada, en la medida que el pago
se concrete de manera simultánea con una liquidación de fondos
ingresados desde el exterior por el nuevo título de deuda que exceda al
monto de capital que se precancela, como mínimo, por un monto
equivalente al monto de la prima abonada.
iv)pagar a la fecha de cierre de la operación de recompra y/o rescate, sin
necesidad de que exista una liquidación de fondos por el monto
equivalente, los gastos de emisión u otros servicios prestados por no
residentes en el marco de la emisión de los nuevos títulos de deuda
emitidos y/o la operación de recompra y/o rescate.
```
**Heredado:** Sección 3. Disposiciones específicas para los egresos por el mercado de cambios / Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas… / 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el / exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el p… / 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 / (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar. En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado… / i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25. ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25. iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25. / El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:

**A** — error: None; salida: 3603 tokens

- Operacion «Precancelación de capital con liquidación de fondos»: Precancelación de capital efectuada de manera simultánea con la liquidación de fondos ingresados desde el exterior por la emisión de un nuevo título de deuda en operación de refinanciación, recompra y/o rescate anticipado ‖ tramo (exacta): «la precancelación de capital sea efectuada en manera simultánea con la liquidación de los fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en este punto 3.5. …»
- Condicion «Nuevo título con 1 año de gracia y vida promedio mayor»: El nuevo título de deuda debe contemplar 1 año de gracia para el pago de capital y su vida promedio debe ser al menos 2 años mayor a la vida promedio remanente de la deuda que se precancela ‖ tramo (exacta): «el nuevo título de deuda contempla 1 (un) año de gracia para el pago de capital y su vida promedio es al menos 2 (dos) años mayor a la vida promedio remanente de la deuda que se precancela» ‖ umbrales: ['1 (un) año de gracia', 'al menos 2 (dos) años mayor']
- Restriccion «Límite monto acumulado vencimientos capital nuevo endeudamiento»: El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela ‖ tramo (exacta): «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los…» ‖ umbrales: ['en ningún momento podrá superar']
- Operacion «Precancelación de intereses devengados»: Precancelación de intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de liquidación de fondos por monto equivalente ‖ tramo (exacta): «la precancelación de intereses corresponde a los intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquid…»
- Potestad «Acceso mercado cambios para pago prima recompra/rescate»: La entidad podrá otorgar acceso al mercado de cambios al cliente para pagar prima de recompra, rescate anticipado o similar hasta el 5% del monto del capital de la deuda recomprada y/o rescatada ‖ tramo (no): «la entidad podrá darle acceso al mercado de cambios al cliente para pagar en concepto de prima de recompra, de rescate anticipado o similar hasta el equivalente del 5% (cinco por ciento) del monto del…»
- Condicion «Pago simultáneo con liquidación de fondos que exceda capital»: El pago debe concretarse de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como mínimo, por un monto equivalente al monto de la prima abonada ‖ tramo (exacta): «el pago se concrete de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como mínimo, por un m…» ‖ umbrales: ['como mínimo, por un monto equivalente al monto de la prima abonada']
- Potestad «Acceso mercado cambios para pago gastos emisión y servicios»: La entidad podrá otorgar acceso al mercado de cambios al cliente para pagar gastos de emisión u otros servicios prestados por no residentes en el marco de la emisión de nuevos títulos de deuda y/o la operación de recompra y/o rescate, a la fecha de cierre, sin necesidad de liquidación de fondos por … ‖ tramo (no): «la entidad podrá darle acceso al mercado de cambios al cliente para pagar a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el mon…»
- Condicion «Acceso mercado cambios con anterioridad no mayor a 3 días hábiles»: El acceso al mercado de cambios debe producirse con una anterioridad no mayor a 3 días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar ‖ tramo (exacta): «El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar» ‖ umbrales: ['no mayor a los 3 (tres) días hábiles']
- Condicion «Plazo mínimo desde emisión para títulos emitidos 08/11/24 a 20/04/25»: Para títulos de deuda emitidos entre el 08/11/24 y el 20/04/25, debe haber transcurrido como mínimo 12 meses desde la fecha de emisión ‖ tramo (exacta): «12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25» ‖ umbrales: ['12 (doce) meses']
- Condicion «Plazo mínimo desde emisión para títulos emitidos 21/04/25 a 15/05/25»: Para títulos de deuda emitidos entre el 21/04/25 y el 15/05/25, debe haber transcurrido como mínimo 6 meses desde la fecha de emisión ‖ tramo (exacta): «6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25» ‖ umbrales: ['6 (seis) meses']
- Condicion «Plazo mínimo desde emisión para títulos emitidos a partir del 16/05/25»: Para títulos de deuda emitidos a partir del 16/05/25, debe haber transcurrido como mínimo 18 meses desde la fecha de emisión ‖ tramo (exacta): «18 (dieciocho) meses si el título fue emitido a partir del 16/05/25» ‖ umbrales: ['18 (dieciocho) meses']
  - Operacion:Precancelación de capital con liquidación de fondos --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Nuevo título con 1 año de gracia y vida promedio mayor --condicion_de--> Operacion:Precancelación de capital con liquidación de fondos
  - Operacion:Precancelación de intereses devengados --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Potestad:Acceso mercado cambios para pago prima recompra/rescate --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Pago simultáneo con liquidación de fondos que exceda capital --condicion_de--> Potestad:Acceso mercado cambios para pago prima recompra/rescate
  - Potestad:Acceso mercado cambios para pago gastos emisión y servicios --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Acceso mercado cambios con anterioridad no mayor a 3 días hábiles --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Plazo mínimo desde emisión para títulos emitidos 08/11/24 a 20/04/25 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Plazo mínimo desde emisión para títulos emitidos 21/04/25 a 15/05/25 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Plazo mínimo desde emisión para títulos emitidos a partir del 16/05/25 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Operacion:Precancelación de capital con liquidación de fondos --aplica_a--> la entidad
  - Potestad:Acceso mercado cambios para pago prima recompra/rescate --aplica_a--> la entidad
  - Potestad:Acceso mercado cambios para pago gastos emisión y servicios --aplica_a--> la entidad
  - mención: aplica_a «la entidad» (verificada: exacta)
  - mención: aplica_a «la entidad» (verificada: exacta)
  - mención: aplica_a «la entidad» (verificada: exacta)
  - rechazo: firma_invalida: relations[2]: Restriccion --condicion_de--> Operacion
  - omisión meta_normativo (exacta): «Adicionalmente, la entidad podrá darle acceso al mercado de cambios al cliente para» — nota: Enunciado introductorio que anuncia las potestades siguientes; no prescribe conducta por sí solo
  - heredado_compuesto: 4

**B** — error: None; salida: 3134 tokens

- Operacion «Precancelación de capital con liquidación de fondos»: Precancelación de capital efectuada de manera simultánea con la liquidación de fondos ingresados desde el exterior por la emisión de un nuevo título de deuda en operación de refinanciación, recompra y/o rescate anticipado de deuda. ‖ tramo (exacta): «la precancelación de capital sea efectuada en manera simultánea con la liquidación de los fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en este punto 3.5. …»
- Condicion «Nuevo título con 1 año de gracia y vida promedio mayor»: El nuevo título de deuda debe contemplar 1 año de gracia para el pago de capital y su vida promedio debe ser al menos 2 años mayor a la vida promedio remanente de la deuda que se precancela. ‖ tramo (exacta): «el nuevo título de deuda contempla 1 (un) año de gracia para el pago de capital y su vida promedio es al menos 2 (dos) años mayor a la vida promedio remanente de la deuda que se precancela» ‖ umbrales: ['1 (un) año de gracia', 'al menos 2 (dos) años mayor']
- Restriccion «Límite monto acumulado vencimientos capital nuevo endeudamiento»: El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela. ‖ tramo (exacta): «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los…»
- Operacion «Precancelación de intereses devengados»: Precancelación de intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de liquidación de fondos por el monto equivalente. ‖ tramo (exacta): «la precancelación de intereses corresponde a los intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquid…»
- Potestad «Acceso mercado cambios para pago prima recompra/rescate»: La entidad podrá dar acceso al mercado de cambios al cliente para pagar prima de recompra, rescate anticipado o similar hasta el 5% del monto del capital de la deuda recomprada y/o rescatada, siempre que el pago se concrete de manera simultánea con una liquidación de fondos ingresados desde el exter… ‖ tramo (no): «la entidad podrá darle acceso al mercado de cambios al cliente para pagar en concepto de prima de recompra, de rescate anticipado o similar hasta el equivalente del 5% (cinco por ciento) del monto del…»
- Condicion «Pago prima simultáneo con liquidación fondos excedente»: El pago de la prima debe concretarse de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como mínimo, por un monto equivalente al monto de la prima abonada. ‖ tramo (exacta): «el pago se concrete de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como mínimo, por un m…»
- Potestad «Acceso mercado cambios para pago gastos emisión y servicios»: La entidad podrá dar acceso al mercado de cambios al cliente para pagar, a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de liquidación de fondos por el monto equivalente, los gastos de emisión u otros servicios prestados por no residentes en el marco de la emisión de los… ‖ tramo (no): «la entidad podrá darle acceso al mercado de cambios al cliente para pagar a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el mon…»
- Obligacion «Acceso mercado cambios para precancelación capital e intereses»: Las entidades podrán dar acceso al mercado de cambios para la precancelación de capital efectuada de manera simultánea con la liquidación de fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en el punto 3.5. ‖ tramo (exacta): «Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exteri…»
  - Operacion:Precancelación de capital con liquidación de fondos --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Nuevo título con 1 año de gracia y vida promedio mayor --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Límite monto acumulado vencimientos capital nuevo endeudamiento --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Operacion:Precancelación de intereses devengados --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Potestad:Acceso mercado cambios para pago prima recompra/rescate --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Pago prima simultáneo con liquidación fondos excedente --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Potestad:Acceso mercado cambios para pago gastos emisión y servicios --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Acceso mercado cambios para precancelación capital e intereses --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Nuevo título con 1 año de gracia y vida promedio mayor --condicion_de--> Operacion:Precancelación de capital con liquidación de fondos
  - Condicion:Pago prima simultáneo con liquidación fondos excedente --condicion_de--> Potestad:Acceso mercado cambios para pago prima recompra/rescate
  - Obligacion:Acceso mercado cambios para precancelación capital e intereses --aplica_a--> Las entidades
  - Potestad:Acceso mercado cambios para pago prima recompra/rescate --aplica_a--> la entidad
  - Potestad:Acceso mercado cambios para pago gastos emisión y servicios --aplica_a--> la entidad
  - mención: aplica_a «Las entidades» (verificada: exacta)
  - mención: aplica_a «la entidad» (verificada: exacta)
  - mención: aplica_a «la entidad» (verificada: exacta)
  - omisión meta_normativo (exacta): «Precancelación de capital e intereses con la liquidación de fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en este p…» — nota: Título/encabezado que anuncia el contenido de la unidad sin prescribir conducta normativa por sí solo.
  - heredado_compuesto: 0

## Ficha 16 — `cap::6.3.2::intro`

**Texto propio:**

```
A excepción de las opciones sobre acciones e índices bursátiles, que se tratan en el
punto 6.6., los restantes derivados sobre acciones y las posiciones fuera de balance
sensibles a los cambios en los precios de mercado deberán incluirse en el cómputo de
la exigencia. Esto comprende a los futuros, “forwards” y “swaps”, tanto de acciones in-
dividuales como de índices bursátiles. Los derivados se convertirán en posiciones en su
correspondiente subyacente.
```
**Heredado:** Sección 6. Capital mínimo por riesgo de mercado. / 6.3. Exigencia de capital por riesgo de posiciones en acciones. / 6.3.2. Tratamiento de los derivados sobre acciones.

**A** — error: None; salida: 1112 tokens

- Excepcion «Excepción opciones sobre acciones e índices»: Las opciones sobre acciones e índices bursátiles quedan exceptuadas de la exigencia de incluirse en el cómputo, siendo tratadas en el punto 6.6. ‖ tramo (exacta): «A excepción de las opciones sobre acciones e índices bursátiles, que se tratan en el punto 6.6.»
- Obligacion «Inclusión derivados acciones en cómputo exigencia»: Los restantes derivados sobre acciones (futuros, forwards, swaps de acciones individuales o índices bursátiles) y las posiciones fuera de balance sensibles a cambios en precios de mercado deberán incluirse en el cómputo de la exigencia de capital. ‖ tramo (exacta): «los restantes derivados sobre acciones y las posiciones fuera de balance sensibles a los cambios en los precios de mercado deberán incluirse en el cómputo de la exigencia»
- Operacion «Conversión derivados a posiciones subyacente»: Los derivados sobre acciones se convertirán en posiciones en su correspondiente subyacente para efectos del cómputo de la exigencia de capital. ‖ tramo (exacta): «Los derivados se convertirán en posiciones en su correspondiente subyacente.»
- Definicion «Derivados sobre acciones comprendidos»: Comprende los futuros, forwards y swaps, tanto de acciones individuales como de índices bursátiles. ‖ tramo (exacta): «Esto comprende a los futuros, "forwards" y "swaps", tanto de acciones individuales como de índices bursátiles.»
  - Excepcion:Excepción opciones sobre acciones e índices --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Obligacion:Inclusión derivados acciones en cómputo exigencia --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Operacion:Conversión derivados a posiciones subyacente --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Definicion:Derivados sobre acciones comprendidos --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Obligacion:Inclusión derivados acciones en cómputo exigencia --aplica_a--> las entidades
  - Excepcion:Excepción opciones sobre acciones e índices --exceptua_obligacion--> Obligacion:Inclusión derivados acciones en cómputo exigencia
  - mención: aplica_a «las entidades» (verificada: no)
  - heredado_compuesto: 0

**B** — error: None; salida: 1232 tokens

- Excepcion «Opciones sobre acciones e índices — derivados»: Las opciones sobre acciones e índices bursátiles quedan exceptuadas del cómputo de la exigencia de capital por riesgo de posiciones en acciones; se tratan en el punto 6.6. ‖ tramo (exacta): «A excepción de las opciones sobre acciones e índices bursátiles, que se tratan en el punto 6.6.»
- Obligacion «Inclusión en cómputo — derivados sobre acciones»: Los restantes derivados sobre acciones (futuros, forwards, swaps de acciones individuales o de índices bursátiles) y las posiciones fuera de balance sensibles a cambios en precios de mercado deberán incluirse en el cómputo de la exigencia de capital por riesgo de posiciones en acciones. ‖ tramo (exacta): «los restantes derivados sobre acciones y las posiciones fuera de balance sensibles a los cambios en los precios de mercado deberán incluirse en el cómputo de la exigencia»
- Operacion «Conversión de derivados a posiciones en subyacente»: Los derivados sobre acciones se convierten en posiciones en su correspondiente subyacente para efectos del cómputo de la exigencia de capital. ‖ tramo (exacta): «Los derivados se convertirán en posiciones en su correspondiente subyacente.»
- Definicion «Derivados sobre acciones — comprende»: Comprende los futuros, forwards y swaps, tanto de acciones individuales como de índices bursátiles. ‖ tramo (exacta): «Esto comprende a los futuros, "forwards" y "swaps", tanto de acciones individuales como de índices bursátiles.»
  - Excepcion:Opciones sobre acciones e índices — derivados --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Inclusión en cómputo — derivados sobre acciones --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Inclusión en cómputo — derivados sobre acciones --aplica_a--> los restantes derivados sobre acciones y las posiciones fuera de balance sensibles a los cambios en los precios de mercado
  - Operacion:Conversión de derivados a posiciones en subyacente --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Definicion:Derivados sobre acciones — comprende --establecida_en--> TextoOrdenado:Capitales Mínimos
  - mención: aplica_a «los restantes derivados sobre acciones y las posiciones fuera de balance sensibl…» (verificada: exacta)
  - omisión relacion_sin_predicado (exacta): «los restantes derivados sobre acciones y las posiciones fuera de balance sensibles a los cambios en los precios de mercado deberán incluirse en el cómputo de la…» — nota: regula
  - heredado_compuesto: 0

## Ficha 17 — `polcre::2.1.15`

**Texto propio:**

```
2.1.15. Financiaciones de proyectos de inversión destinados a la ganadería bovina, incluido su
capital de trabajo, sin superar el 5 % de los depósitos en moneda extranjera de la entidad.
```
**Heredado:** Sección 2. Aplicación de la capacidad de préstamo de depósitos en moneda extranjera. / 2.1. Destinos. / La capacidad de préstamo de los depósitos en moneda extranjera deberá aplicarse, en la co- rrespondiente moneda de captación, en forma indistinta, a los siguientes destinos: / La aplicación de la capacidad de préstamo de depósitos en moneda extranjera a los destinos vinculados a operaciones de importación (previstos en los puntos 2.1.6., 2.1.7. y la parte atri- buible a éstos por aplicación de los puntos 2.1.8. y 2.1.9.), no podrá s… / x / t base base / Siendo: C: capacidad de préstamo del mes al que corresponda. / t / F : financiación de importaciones comprendidas, correspondientes al trimestre agos- base / to/octubre de 2008. / C : capacidad de préstamo que corresponda al trimestre agosto/octubre de 2008. / base / Las financiaciones y capacidad de préstamo deberán ser computadas de acuerdo con lo esta- blecido en el punto 2.5.

**A** — error: None; salida: 691 tokens

- Operacion «Financiación de proyectos ganadería bovina»: Financiación de proyectos de inversión destinados a la ganadería bovina, incluido su capital de trabajo ‖ tramo (exacta): «Financiaciones de proyectos de inversión destinados a la ganadería bovina, incluido su capital de trabajo»
- Restriccion «Límite 5% depósitos moneda extranjera»: Las financiaciones de proyectos de inversión destinados a la ganadería bovina no podrán superar el 5 % de los depósitos en moneda extranjera de la entidad ‖ tramo (exacta): «sin superar el 5 % de los depósitos en moneda extranjera de la entidad» ‖ umbrales: ['sin superar el 5 %']
  - Operacion:Financiación de proyectos ganadería bovina --establecida_en--> TextoOrdenado:Política de Crédito
  - Restriccion:Límite 5% depósitos moneda extranjera --establecida_en--> TextoOrdenado:Política de Crédito
  - Restriccion:Límite 5% depósitos moneda extranjera --limita--> Operacion:Financiación de proyectos ganadería bovina
  - Restriccion:Límite 5% depósitos moneda extranjera --aplica_a--> la entidad
  - mención: aplica_a «la entidad» (verificada: exacta)
  - heredado_compuesto: 0

**B** — error: None; salida: 805 tokens

- Operacion «Financiación proyectos ganadería bovina»: Financiación de proyectos de inversión destinados a la ganadería bovina, incluido su capital de trabajo ‖ tramo (exacta): «Financiaciones de proyectos de inversión destinados a la ganadería bovina, incluido su capital de trabajo»
- Restriccion «Límite 5% depósitos moneda extranjera»: La financiación de proyectos de inversión destinados a la ganadería bovina no podrá superar el 5 % de los depósitos en moneda extranjera de la entidad ‖ tramo (exacta): «sin superar el 5 % de los depósitos en moneda extranjera de la entidad» ‖ umbrales: ['sin superar el 5 %']
  - Operacion:Financiación proyectos ganadería bovina --establecida_en--> TextoOrdenado:Política de Crédito
  - Restriccion:Límite 5% depósitos moneda extranjera --establecida_en--> TextoOrdenado:Política de Crédito
  - Restriccion:Límite 5% depósitos moneda extranjera --limita--> Operacion:Financiación proyectos ganadería bovina
  - Restriccion:Límite 5% depósitos moneda extranjera --aplica_a--> la entidad
  - mención: aplica_a «la entidad» (verificada: exacta)
  - omisión meta_normativo (exacta): «La capacidad de préstamo de los depósitos en moneda extranjera deberá aplicarse, en la correspondiente moneda de captación, en forma indistinta, a los siguiente…» — nota: Enunciado introductorio que anuncia la lista de destinos; el contenido normativo se compone en cada ítem con este encabezado
  - heredado_compuesto: 0

## Ficha 18 — `ext::3.5.3::intro`

**Texto propio:**

```
(tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar.
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
```
**Heredado:** Sección 3. Disposiciones específicas para los egresos por el mercado de cambios / 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el / 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3

**A = B (iguales byte a byte)** — error: None; salida: 2073 tokens

- Operacion «Acceso al mercado de cambios — pago de títulos»: Acceso al mercado de cambios para pago de servicios de capital o interés de títulos de deuda, con anterioridad no mayor a 3 días hábiles a la fecha de vencimiento ‖ tramo (no): «El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar»
- Restriccion «Plazo mínimo 12 meses — títulos emitidos 08/11/24 a 20/04/25»: Para pago de capital de títulos de deuda emitidos entre 08/11/24 y 20/04/25 mediante transferencia al exterior, el acceso al mercado de cambios debe producirse como mínimo 12 meses desde la fecha de emisión ‖ tramo (exacta): «12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25» ‖ umbrales: ['como mínimo, desde la fecha de emisión: 12 (doce) meses']
- Restriccion «Plazo mínimo 6 meses — títulos emitidos 21/04/25 a 15/05/25»: Para pago de capital de títulos de deuda emitidos entre 21/04/25 y 15/05/25 mediante transferencia al exterior, el acceso al mercado de cambios debe producirse como mínimo 6 meses desde la fecha de emisión ‖ tramo (exacta): «6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25» ‖ umbrales: ['como mínimo, desde la fecha de emisión: 6 (seis) meses']
- Restriccion «Plazo mínimo 18 meses — títulos emitidos a partir del 16/05/25»: Para pago de capital de títulos de deuda emitidos a partir del 16/05/25 mediante transferencia al exterior, el acceso al mercado de cambios debe producirse como mínimo 18 meses desde la fecha de emisión ‖ tramo (exacta): «18 (dieciocho) meses si el título fue emitido a partir del 16/05/25» ‖ umbrales: ['como mínimo, desde la fecha de emisión: 18 (dieciocho) meses']
- Potestad «Autorización previa del BCRA — acceso anticipado al mercado de cambios»: El BCRA puede autorizar el acceso al mercado de cambios antes de los plazos mínimos establecidos, mediante conformidad previa ‖ tramo (exacta): «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA»
- Excepcion «Excepción — acceso anticipado sin conformidad previa»: No se requiere conformidad previa del BCRA para acceso anticipado al mercado de cambios cuando el deudor encuadra en alguna de las situaciones siguientes y se cumplen todas las condiciones de cada caso ‖ tramo (exacta): «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las co…»
  - Operacion:Acceso al mercado de cambios — pago de títulos --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Plazo mínimo 12 meses — títulos emitidos 08/11/24 a 20/04/25 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Plazo mínimo 6 meses — títulos emitidos 21/04/25 a 15/05/25 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Plazo mínimo 18 meses — títulos emitidos a partir del 16/05/25 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Potestad:Autorización previa del BCRA — acceso anticipado al mercado de cambios --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Excepcion:Excepción — acceso anticipado sin conformidad previa --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Plazo mínimo 12 meses — títulos emitidos 08/11/24 a 20/04/25 --limita--> Operacion:Acceso al mercado de cambios — pago de títulos
  - Restriccion:Plazo mínimo 6 meses — títulos emitidos 21/04/25 a 15/05/25 --limita--> Operacion:Acceso al mercado de cambios — pago de títulos
  - Restriccion:Plazo mínimo 18 meses — títulos emitidos a partir del 16/05/25 --limita--> Operacion:Acceso al mercado de cambios — pago de títulos
  - rechazo: firma_invalida: relations[9]: Excepcion --exceptua--> Potestad
  - omisión relacion_sin_predicado (exacta): «el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso» — nota: La excepción (e6) condiciona su aplicabilidad a que el deudor encuadre en situaciones y condiciones que se enumeran después (en el texto que…
  - heredado_compuesto: 0

## Ficha 19 — `cla::5.1.1::intro`

**Texto propio:**

```
Abarca todas las financiaciones comprendidas, con excepción de las siguientes:
```
**Heredado:** Sección 5. Categorías de carteras. / 5.1. Categorías. / 5.1.1. Cartera comercial.

**A = B (iguales byte a byte)** — error: None; salida: 405 tokens

- Definicion «Cartera comercial — alcance»: Abarca todas las financiaciones comprendidas, con excepción de las siguientes ‖ tramo (exacta): «Abarca todas las financiaciones comprendidas, con excepción de las siguientes:»
  - Definicion:Cartera comercial — alcance --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - omisión fuera_de_tipos (exacta): «con excepción de las siguientes:» — nota: Anuncio de lista de excepciones cuyo contenido está en los ítems siguientes (no en esta unidad intro). La excepción se extrae en cada ítem d…
  - heredado_compuesto: 0

## Ficha 20 — `cap::10.3.3.1`

**Texto propio:**

```
10.3.3.1. Cuando una entidad financiera invierta en una emisión que cuente con una
calificación específica para esa emisión, el ponderador de riesgo estará ba-
sado en esa calificación. De lo contrario, será de aplicación lo siguiente:
i) En los casos en que el prestatario cuente con una calificación específica
para una de sus emisiones de deuda –pero la exposición crediticia de la
entidad financiera no sea en dicha emisión– la exposición crediticia de la
entidad sólo recibirá una evaluación de crédito de alta calidad –es decir,
la que corresponde a un ponderador de riesgo inferior a la evaluación
aplicable a un crédito no calificado– cuando sea en todos sus aspectos
igual o preferente (“senior”) respecto del crédito evaluado. De lo contrario,
no podrá usarse dicha calificación y la exposición crediticia no calificada
recibirá el ponderador de riesgo correspondiente a los créditos no califi-
cados.
ii) Cuando el prestatario haya sido evaluado como emisor, esa calificación
se podrá aplicar a los créditos quirografarios no subordinados que le ha-
yan sido concedidos y no hayan sido evaluados. Las otras exposiciones
crediticias no calificadas del emisor serán tratadas como no calificadas.
iii) Cuando el emisor o una emisión específica tengan una baja evaluación
crediticia –es decir, asociada a un ponderador de riesgo igual o mayor
que el aplicable a exposiciones no calificadas–, una exposición crediticia
no evaluada frente a dicha contraparte que sea equiparable, o que esté
subordinada, a la evaluación del emisor –correspondiente a sus pasivos
quirografarios no subordinados– o a la evaluación de la exposición, recibi-
rá el mismo ponderador de riesgo que corresponda a esa baja calificación
crediticia.
```
**Heredado:** Sección 10. Agentes de calificación externa (ECAI). / 10.3. Consideraciones para su implementación. / 10.3.3. Evaluaciones de emisores o de emisiones.

**A** — error: None; salida: 3133 tokens

- Operacion «Inversión en emisión con calificación específica»: Inversión de una entidad financiera en una emisión que cuenta con una calificación específica para esa emisión ‖ tramo (exacta): «una entidad financiera invierta en una emisión que cuente con una calificación específica para esa emisión»
- Obligacion «Ponderador basado en calificación específica de emisión»: El ponderador de riesgo estará basado en la calificación específica de la emisión ‖ tramo (exacta): «el ponderador de riesgo estará basado en esa calificación»
- Condicion «Exposición crediticia igual o preferente a crédito evaluado»: La exposición crediticia debe ser en todos sus aspectos igual o preferente (senior) respecto del crédito evaluado ‖ tramo (exacta): «cuando sea en todos sus aspectos igual o preferente ("senior") respecto del crédito evaluado»
- Obligacion «Evaluación de alta calidad para exposición crediticia senior»: La exposición crediticia de la entidad recibirá una evaluación de crédito de alta calidad (ponderador de riesgo inferior al de créditos no calificados) cuando sea igual o preferente respecto del crédito evaluado ‖ tramo (exacta): «la exposición crediticia de la entidad sólo recibirá una evaluación de crédito de alta calidad –es decir, la que corresponde a un ponderador de riesgo inferior a la evaluación aplicable a un crédito n…»
- Restriccion «Prohibición de usar calificación para exposición no senior»: No podrá usarse la calificación de la emisión cuando la exposición crediticia no sea igual o preferente respecto del crédito evaluado; la exposición crediticia no calificada recibirá el ponderador de riesgo correspondiente a los créditos no calificados ‖ tramo (exacta): «no podrá usarse dicha calificación y la exposición crediticia no calificada recibirá el ponderador de riesgo correspondiente a los créditos no calificados»
- Obligacion «Aplicación de calificación de emisor a créditos quirografarios no subordinados»: La calificación del emisor se podrá aplicar a los créditos quirografarios no subordinados que le hayan sido concedidos y no hayan sido evaluados ‖ tramo (exacta): «esa calificación se podrá aplicar a los créditos quirografarios no subordinados que le hayan sido concedidos y no hayan sido evaluados»
- Obligacion «Tratamiento como no calificadas de otras exposiciones crediticias»: Las otras exposiciones crediticias no calificadas del emisor serán tratadas como no calificadas ‖ tramo (exacta): «Las otras exposiciones crediticias no calificadas del emisor serán tratadas como no calificadas»
- Condicion «Emisor o emisión con baja evaluación crediticia»: El emisor o una emisión específica tienen una baja evaluación crediticia, asociada a un ponderador de riesgo igual o mayor que el aplicable a exposiciones no calificadas ‖ tramo (exacta): «Cuando el emisor o una emisión específica tengan una baja evaluación crediticia –es decir, asociada a un ponderador de riesgo igual o mayor que el aplicable a exposiciones no calificadas–»
- Condicion «Exposición crediticia equiparable o subordinada a evaluación del emisor»: Una exposición crediticia no evaluada frente a la contraparte es equiparable o está subordinada a la evaluación del emisor (correspondiente a sus pasivos quirografarios no subordinados) o a la evaluación de la exposición ‖ tramo (exacta): «una exposición crediticia no evaluada frente a dicha contraparte que sea equiparable, o que esté subordinada, a la evaluación del emisor –correspondiente a sus pasivos quirografarios no subordinados– …»
- Obligacion «Ponderador de riesgo igual a baja calificación crediticia»: La exposición crediticia no evaluada recibirá el mismo ponderador de riesgo que corresponda a la baja calificación crediticia del emisor o la emisión ‖ tramo (exacta): «recibirá el mismo ponderador de riesgo que corresponda a esa baja calificación crediticia»
- Condicion «Prestatario sin calificación específica para la exposición»: Cuando la entidad financiera invierta en una emisión que no cuente con una calificación específica para esa emisión ‖ tramo (exacta): «De lo contrario»
  - Operacion:Inversión en emisión con calificación específica --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Ponderador basado en calificación específica de emisión --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Exposición crediticia igual o preferente a crédito evaluado --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Evaluación de alta calidad para exposición crediticia senior --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Prohibición de usar calificación para exposición no senior --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Aplicación de calificación de emisor a créditos quirografarios no subo… --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Tratamiento como no calificadas de otras exposiciones crediticias --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Emisor o emisión con baja evaluación crediticia --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Exposición crediticia equiparable o subordinada a evaluación del emiso… --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Ponderador de riesgo igual a baja calificación crediticia --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Prestatario sin calificación específica para la exposición --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Exposición crediticia igual o preferente a crédito evaluado --condicion_de--> Obligacion:Evaluación de alta calidad para exposición crediticia senior
  - Condicion:Emisor o emisión con baja evaluación crediticia --condicion_de--> Obligacion:Ponderador de riesgo igual a baja calificación crediticia
  - Condicion:Exposición crediticia equiparable o subordinada a evaluación del emiso… --condicion_de--> Obligacion:Ponderador de riesgo igual a baja calificación crediticia
  - Obligacion:Ponderador basado en calificación específica de emisión --aplica_a--> una entidad financiera
  - Obligacion:Evaluación de alta calidad para exposición crediticia senior --aplica_a--> la entidad
  - Restriccion:Prohibición de usar calificación para exposición no senior --aplica_a--> la entidad financiera
  - Obligacion:Aplicación de calificación de emisor a créditos quirografarios no subo… --aplica_a--> la entidad
  - Obligacion:Tratamiento como no calificadas de otras exposiciones crediticias --aplica_a--> la entidad
  - mención: aplica_a «una entidad financiera» (verificada: exacta)
  - mención: aplica_a «la entidad» (verificada: exacta)
  - mención: aplica_a «la entidad financiera» (verificada: exacta)
  - mención: aplica_a «la entidad» (verificada: exacta)
  - mención: aplica_a «la entidad» (verificada: exacta)
  - omisión meta_normativo (exacta): «De lo contrario, será de aplicación lo siguiente:» — nota: Enunciado introductorio que anuncia la aplicación de reglas alternativas; no prescribe conducta por sí solo
  - heredado_compuesto: 0

**B** — error: None; salida: 3032 tokens

- Operacion «Inversión en emisión con calificación específica»: Inversión de una entidad financiera en una emisión que cuenta con una calificación específica para esa emisión ‖ tramo (exacta): «una entidad financiera invierta en una emisión que cuente con una calificación específica para esa emisión»
- Obligacion «Ponderador basado en calificación específica»: El ponderador de riesgo estará basado en la calificación específica de la emisión ‖ tramo (exacta): «el ponderador de riesgo estará basado en esa calificación»
- Operacion «Exposición crediticia en emisión no calificada del prestatario»: Exposición crediticia de la entidad financiera que no es en la emisión específicamente calificada del prestatario ‖ tramo (exacta): «la exposición crediticia de la entidad financiera no sea en dicha emisión»
- Restriccion «Evaluación de alta calidad solo si senior o igual»: La exposición crediticia solo recibe evaluación de alta calidad cuando es en todos sus aspectos igual o preferente (senior) respecto del crédito evaluado ‖ tramo (exacta): «la exposición crediticia de la entidad sólo recibirá una evaluación de crédito de alta calidad –es decir, la que corresponde a un ponderador de riesgo inferior a la evaluación aplicable a un crédito n…»
- Restriccion «Prohibición de usar calificación si no es senior»: No podrá usarse la calificación de la emisión si la exposición crediticia no es senior respecto del crédito evaluado; la exposición no calificada recibirá el ponderador de riesgo de créditos no calificados ‖ tramo (exacta): «no podrá usarse dicha calificación y la exposición crediticia no calificada recibirá el ponderador de riesgo correspondiente a los créditos no calificados»
- Operacion «Evaluación de prestatario como emisor»: Evaluación del prestatario en su calidad de emisor ‖ tramo (exacta): «el prestatario haya sido evaluado como emisor»
- Potestad «Aplicación de calificación de emisor a créditos quirografarios»: La calificación del emisor podrá aplicarse a los créditos quirografarios no subordinados no evaluados que le hayan sido concedidos ‖ tramo (exacta): «esa calificación se podrá aplicar a los créditos quirografarios no subordinados que le hayan sido concedidos y no hayan sido evaluados»
- Restriccion «Otras exposiciones no calificadas tratadas como no calificadas»: Las otras exposiciones crediticias no calificadas del emisor serán tratadas como no calificadas ‖ tramo (exacta): «Las otras exposiciones crediticias no calificadas del emisor serán tratadas como no calificadas»
- Condicion «Emisor o emisión con baja evaluación crediticia»: El emisor o una emisión específica tienen una baja evaluación crediticia, asociada a un ponderador de riesgo igual o mayor que el aplicable a exposiciones no calificadas ‖ tramo (exacta): «Cuando el emisor o una emisión específica tengan una baja evaluación crediticia –es decir, asociada a un ponderador de riesgo igual o mayor que el aplicable a exposiciones no calificadas–»
- Obligacion «Ponderador igual a baja calificación para exposición equiparable o subordinada»: Una exposición crediticia no evaluada frente a la contraparte que sea equiparable o subordinada a la evaluación del emisor o de la exposición recibirá el mismo ponderador de riesgo que corresponda a esa baja calificación crediticia ‖ tramo (exacta): «una exposición crediticia no evaluada frente a dicha contraparte que sea equiparable, o que esté subordinada, a la evaluación del emisor –correspondiente a sus pasivos quirografarios no subordinados– …»
  - Operacion:Inversión en emisión con calificación específica --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Ponderador basado en calificación específica --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Operacion:Exposición crediticia en emisión no calificada del prestatario --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Evaluación de alta calidad solo si senior o igual --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Prohibición de usar calificación si no es senior --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Operacion:Evaluación de prestatario como emisor --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Potestad:Aplicación de calificación de emisor a créditos quirografarios --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Otras exposiciones no calificadas tratadas como no calificadas --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Emisor o emisión con baja evaluación crediticia --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Ponderador igual a baja calificación para exposición equiparable o sub… --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Ponderador basado en calificación específica --aplica_a--> una entidad financiera
  - Restriccion:Evaluación de alta calidad solo si senior o igual --aplica_a--> la entidad financiera
  - Restriccion:Prohibición de usar calificación si no es senior --aplica_a--> la entidad financiera
  - Potestad:Aplicación de calificación de emisor a créditos quirografarios --aplica_a--> la entidad financiera
  - Restriccion:Otras exposiciones no calificadas tratadas como no calificadas --aplica_a--> la entidad financiera
  - Obligacion:Ponderador igual a baja calificación para exposición equiparable o sub… --aplica_a--> la entidad financiera
  - Condicion:Emisor o emisión con baja evaluación crediticia --condicion_de--> Obligacion:Ponderador igual a baja calificación para exposición equiparable o sub…
  - Restriccion:Evaluación de alta calidad solo si senior o igual --limita--> Operacion:Exposición crediticia en emisión no calificada del prestatario
  - Restriccion:Prohibición de usar calificación si no es senior --prohibe--> Operacion:Exposición crediticia en emisión no calificada del prestatario
  - mención: aplica_a «una entidad financiera» (verificada: exacta)
  - mención: aplica_a «la entidad financiera» (verificada: exacta)
  - mención: aplica_a «la entidad financiera» (verificada: exacta)
  - mención: aplica_a «la entidad financiera» (verificada: exacta)
  - mención: aplica_a «la entidad financiera» (verificada: exacta)
  - mención: aplica_a «la entidad financiera» (verificada: exacta)
  - omisión meta_normativo (exacta): «De lo contrario, será de aplicación lo siguiente:» — nota: Cláusula introductoria que anuncia la enumeración de supuestos alternativos; no prescribe conducta por sí sola
  - heredado_compuesto: 0

## Ficha 21 — `cap::3.2::intro`

**Texto propio:**

```
Las participaciones en fondos (carteras de activos) imputadas a la cartera de inversión
–incluidas las exposiciones fuera de balance, tales como los compromisos de suscripciones fu-
turas– se deberán tratar de acuerdo con uno o más de los siguientes enfoques: de transparen-
cia (“look-through approach”, LTA), reglamentario (“mandate-based approach”, MBA) y residual
(“fall-back approach”, FBA).
Quedan comprendidas las participaciones en fondos comunes regidos por la Ley 24.083 de
Fondos Comunes de Inversión y en fideicomisos –en este último caso, en la medida en que el
riesgo de la inversión no se estructure a través de instrumentos que se emitan con distinta pre-
lación para el cobro, tales como títulos de deuda y certificados de participación–, imputados a
la cartera de inversión.
```
**Heredado:** Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fon- dos. / 3.2. Tratamiento de las posiciones en fondos.

**A** — error: None; salida: 1292 tokens

- Operacion «Tratamiento de posiciones en fondos»: Tratamiento de participaciones en fondos (carteras de activos) imputadas a la cartera de inversión, incluidas exposiciones fuera de balance como compromisos de suscripciones futuras, según uno o más de los siguientes enfoques: de transparencia (LTA), reglamentario (MBA) o residual (FBA). ‖ tramo (exacta): «Las participaciones en fondos (carteras de activos) imputadas a la cartera de inversión –incluidas las exposiciones fuera de balance, tales como los compromisos de suscripciones futuras– se deberán tr…»
- Definicion «Participaciones en fondos comprendidas»: Participaciones en fondos comunes regidos por la Ley 24.083 de Fondos Comunes de Inversión y en fideicomisos (en este último caso, siempre que el riesgo de la inversión no se estructure a través de instrumentos que se emitan con distinta prelación para el cobro, tales como títulos de deuda y certifi… ‖ tramo (exacta): «Quedan comprendidas las participaciones en fondos comunes regidos por la Ley 24.083 de Fondos Comunes de Inversión y en fideicomisos –en este último caso, en la medida en que el riesgo de la inversión…»
- Condicion «Riesgo no estructurado con distinta prelación»: El riesgo de la inversión no se estructura a través de instrumentos que se emitan con distinta prelación para el cobro. ‖ tramo (exacta): «en la medida en que el riesgo de la inversión no se estructure a través de instrumentos que se emitan con distinta prelación para el cobro»
  - Operacion:Tratamiento de posiciones en fondos --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Definicion:Participaciones en fondos comprendidas --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Riesgo no estructurado con distinta prelación --establecida_en--> TextoOrdenado:Capitales Mínimos
  - rechazo: firma_invalida: relations[3]: Condicion --condicion_de--> Definicion
  - omisión relacion_sin_predicado (exacta): «Las participaciones en fondos (carteras de activos) imputadas a la cartera de inversión –incluidas las exposiciones fuera de balance, tales como los compromisos…» — nota: Relación entre la Operacion (tratamiento de posiciones en fondos) y los tres enfoques (LTA, MBA, FBA) que no encaja en los predicados dispon…
  - heredado_compuesto: 0

**B** — error: None; salida: 976 tokens

- Operacion «Tratamiento de posiciones en fondos»: Tratamiento de participaciones en fondos (carteras de activos) imputadas a la cartera de inversión, incluidas exposiciones fuera de balance como compromisos de suscripciones futuras, según uno o más de los siguientes enfoques: de transparencia (LTA), reglamentario (MBA) o residual (FBA). ‖ tramo (exacta): «Las participaciones en fondos (carteras de activos) imputadas a la cartera de inversión –incluidas las exposiciones fuera de balance, tales como los compromisos de suscripciones futuras– se deberán tr…»
- Definicion «Participaciones en fondos comprendidas»: Participaciones en fondos comunes regidos por la Ley 24.083 de Fondos Comunes de Inversión y en fideicomisos (en este último caso, cuando el riesgo de la inversión no se estructure a través de instrumentos que se emitan con distinta prelación para el cobro, tales como títulos de deuda y certificados… ‖ tramo (exacta): «Quedan comprendidas las participaciones en fondos comunes regidos por la Ley 24.083 de Fondos Comunes de Inversión y en fideicomisos –en este último caso, en la medida en que el riesgo de la inversión…»
  - Operacion:Tratamiento de posiciones en fondos --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Definicion:Participaciones en fondos comprendidas --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Tratamiento de posiciones en fondos --aplica_a--> Las participaciones en fondos
  - mención: aplica_a «Las participaciones en fondos» (verificada: exacta)
  - omisión meta_normativo (exacta): «se deberán tratar de acuerdo con uno o más de los siguientes enfoques» — nota: Enunciado de modalidad prescriptiva que se extrae como parte de la Operacion e1, no como omisión independiente.
  - heredado_compuesto: 0

## Ficha 22 — `ext::10.4.2.5`

**Texto propio:**

```
10.4.2.5. Cuenta con elementos que le permitan avalar la razonabilidad de los
montos a pagar considerando la actividad importadora del cliente en los
últimos años y/o los planes de negocios que le presente el importador.
Adicionalmente, en el caso de que el cliente no sea una persona humana y
se haya constituido hasta 365 (trescientos sesenta y cinco) días corridos
antes de la fecha de acceso al mercado de cambios, para dar curso a
nuevos pagos se requerirá la conformidad previa del BCRA cuando el
monto pendiente de regularización por pagos anticipados de importaciones
sea mayor al equivalente de USD 5 millones (dólares estadounidenses
cinco millones), incluido el monto por el cual se solicita el acceso al
mercado de cambios. En el caso de que el cliente sea una unión transitoria,
se tomará en cuenta la fecha de constitución de la sociedad más antigua
que la conforma.
Para los importadores comprendidos en el párrafo anterior, las entidades
deberán consultar en el apartado “Régimen Informativo SEPAIMPO” del
sitio www3.bcra.gob.ar, si el saldo pendiente de regularización por pagos
anticipados de importaciones del cliente se encuentra comprendido en el
límite previsto.
```
**Heredado:** Sección 10. Pagos de importaciones y otras compras de bienes en el exterior. / 10.4. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente. / 10.4.2. Requisitos de acceso para el pago anticipado de importaciones. / La entidad podrá dar acceso al mercado de cambios para el pago al exterior en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos:

**A = B (iguales byte a byte)** — error: None; salida: 1968 tokens

- Condicion «Verificación previa de requisitos»: La entidad debe verificar previamente que se cumplen la totalidad de los requisitos enumerados para dar acceso al mercado de cambios para el pago al exterior. ‖ tramo (exacta): «en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos»
- Obligacion «Avalar razonabilidad de montos a pagar»: La entidad debe contar con elementos que le permitan avalar la razonabilidad de los montos a pagar considerando la actividad importadora del cliente en los últimos años y/o los planes de negocios que le presente el importador. ‖ tramo (exacta): «Cuenta con elementos que le permitan avalar la razonabilidad de los montos a pagar considerando la actividad importadora del cliente en los últimos años y/o los planes de negocios que le presente el i…»
- Condicion «Cliente no persona humana constituido hasta 365 días»: Supuesto en que el cliente no es una persona humana y se ha constituido hasta 365 días corridos antes de la fecha de acceso al mercado de cambios. ‖ tramo (exacta): «en el caso de que el cliente no sea una persona humana y se haya constituido hasta 365 (trescientos sesenta y cinco) días corridos antes de la fecha de acceso al mercado de cambios»
- Obligacion «Requerir conformidad previa del BCRA para nuevos pagos»: Para dar curso a nuevos pagos, se requiere la conformidad previa del BCRA cuando el monto pendiente de regularización por pagos anticipados de importaciones sea mayor al equivalente de USD 5 millones, incluido el monto por el cual se solicita el acceso al mercado de cambios. ‖ tramo (exacta): «para dar curso a nuevos pagos se requerirá la conformidad previa del BCRA cuando el monto pendiente de regularización por pagos anticipados de importaciones sea mayor al equivalente de USD 5 millones …» ‖ umbrales: ['mayor al equivalente de USD 5 millones (dólares estadounidenses cinco millones)']
- Excepcion «Excepción para uniones transitorias — fecha de constitución»: Cuando el cliente es una unión transitoria, se toma en cuenta la fecha de constitución de la sociedad más antigua que la conforma, en lugar de la fecha de constitución de la unión transitoria. ‖ tramo (exacta): «En el caso de que el cliente sea una unión transitoria, se tomará en cuenta la fecha de constitución de la sociedad más antigua que la conforma»
- Obligacion «Consultar Régimen Informativo SEPAIMPO»: Las entidades deben consultar en el apartado 'Régimen Informativo SEPAIMPO' del sitio www3.bcra.gob.ar si el saldo pendiente de regularización por pagos anticipados de importaciones del cliente se encuentra comprendido en el límite previsto. ‖ tramo (exacta): «las entidades deberán consultar en el apartado "Régimen Informativo SEPAIMPO" del sitio www3.bcra.gob.ar, si el saldo pendiente de regularización por pagos anticipados de importaciones del cliente se …»
  - Obligacion:Avalar razonabilidad de montos a pagar --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Requerir conformidad previa del BCRA para nuevos pagos --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Excepcion:Excepción para uniones transitorias — fecha de constitución --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Consultar Régimen Informativo SEPAIMPO --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Cliente no persona humana constituido hasta 365 días --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Cliente no persona humana constituido hasta 365 días --condicion_de--> Obligacion:Requerir conformidad previa del BCRA para nuevos pagos
  - Obligacion:Avalar razonabilidad de montos a pagar --aplica_a--> la entidad
  - Obligacion:Requerir conformidad previa del BCRA para nuevos pagos --aplica_a--> la entidad
  - Obligacion:Consultar Régimen Informativo SEPAIMPO --aplica_a--> las entidades
  - mención: aplica_a «la entidad» (verificada: exacta)
  - mención: aplica_a «la entidad» (verificada: exacta)
  - mención: aplica_a «las entidades» (verificada: exacta)
  - omisión meta_normativo (exacta): «Para los importadores comprendidos en el párrafo anterior» — nota: Referencia anafórica que ancla la obligación de consultar a los importadores mencionados en el párrafo anterior; no es contenido normativo i…
  - heredado_compuesto: 0

## Ficha 23 — `ctacte::3.2.4`

**Texto propio:**

```
3.2.4. Que contengan inscripciones de propaganda.
```
**Heredado:** Sección 3. Cheques. / 3.2. Títulos que carecen de valor como cheques. / El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque: / Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones.

**A** — error: None; salida: 518 tokens

- Restriccion «Prohibición cheques con inscripciones de propaganda»: Los cheques no podrán contener inscripciones de propaganda ‖ tramo (exacta): «Que contengan inscripciones de propaganda»
- Operacion «Presentación de cheques»: Presentación de cheques para compensación ‖ tramo (exacta): «nuevas presentaciones»
  - Restriccion:Prohibición cheques con inscripciones de propaganda --establecida_en--> TextoOrdenado:Texto Ordenado Cuentas de Corresponsalía
  - Restriccion:Prohibición cheques con inscripciones de propaganda --prohibe--> Operacion:Presentación de cheques
  - omisión meta_normativo (exacta): «no valdrá como cheque» — nota: Cláusula interpretativa que declara el efecto jurídico de la situación enumerada, no una prescripción de conducta
  - heredado_compuesto: 0

**B** — error: None; salida: 524 tokens

- Restriccion «Prohibición cheques con inscripciones de propaganda»: Los cheques no podrán contener inscripciones de propaganda ‖ tramo (exacta): «Que contengan inscripciones de propaganda»
- Operacion «Presentación de cheques»: Presentación de títulos/cheques para compensación ‖ tramo (exacta): «nuevas presentaciones»
  - Restriccion:Prohibición cheques con inscripciones de propaganda --establecida_en--> TextoOrdenado:Texto Ordenado Cuentas de Corresponsalía
  - Restriccion:Prohibición cheques con inscripciones de propaganda --prohibe--> Operacion:Presentación de cheques
  - omisión meta_normativo (exacta): «no valdrá como cheque» — nota: Cláusula interpretativa que predica sobre el significado jurídico (que el título no tiene valor como cheque) y no sobre conducta prescrita
  - heredado_compuesto: 0

## Ficha 24 — `cap::6.2.2.6`

**Texto propio:**

```
6.2.2.6. Como resultado de lo previsto en el punto 6.2.2.5. se obtendrá un conjunto de
posiciones netas compradas, un conjunto de posiciones netas vendidas y las
desestimaciones verticales. Luego, las entidades podrán realizar dos series de
compensaciones horizontales: primero, entre las posiciones netas dentro de
cada una de las tres zonas en las que se agrupan las bandas temporales y,
luego, entre las posiciones netas de las tres zonas. Dichas compensaciones
estarán sujetas a la siguiente escala de desestimaciones horizontales
-exigencias adicionales- expresadas como porcentajes de las posiciones que
se compensan:
[TABLA cap::tabla037 | página 125 | e0_tablas | posicional]
Fila 1: col1 = Zona | col2 = Banda | col3 = Porcentaje de desestimación aplicable: ⟨abarca hasta col5⟩
Fila 2: col3 = dentro de zona | col4 = entre zonas adyacentes | col5 = entre zonas 1 y 3
Fila 3: col2 = Meses*
Fila 4: col1 = 1 | col2 = 0-1 | col3 = 40%
Fila 5: col1 = 1 ⟨combinada con fila 4⟩ | col2 = 1-3 | col3 = 40% ⟨combinada con fila 4⟩
Fila 6: col1 = 1 ⟨combinada con fila 4⟩ | col2 = 3-6 | col3 = 40% ⟨combinada con fila 4⟩
Fila 7: col1 = 1 ⟨combinada con fila 4⟩ | col2 = 6-12 | col3 = 40% ⟨combinada con fila 4⟩
Fila 8: col1 = Años* ⟨abarca hasta col3⟩ | col4 = 40%
Fila 9: col1 = 2 | col2 = 1-2 | col3 = 30%
Fila 10: col1 = 2 ⟨combinada con fila 9⟩ | col2 = 2-3 | col3 = 30% ⟨combinada con fila 9⟩ | col5 = 100%
Fila 11: col1 = 2 ⟨combinada con fila 9⟩ | col2 = 3-4 | col3 = 30% ⟨combinada con fila 9⟩
Fila 12: col1 = Años* ⟨abarca hasta col3⟩ | col4 = 40%
Fila 13: col1 = 3 | col2 = 4-5 | col3 = 30%
Fila 14: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 5-7 | col3 = 30% ⟨combinada con fila 13⟩
Fila 15: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 7-10 | col3 = 30% ⟨combinada con fila 13⟩
Fila 16: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 10-15 | col3 = 30% ⟨combinada con fila 13⟩
Fila 17: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 15-20 | col3 = 30% ⟨combinada con fila 13⟩
Fila 18: col2 = Más de 20
[FIN TABLA cap::tabla037]
ei se puede simplificar menciones a “meses” y “años”ese
*
Al efecto de imputar una posición a la escala de vencimientos cuando el plazo residual o el plazo que
resta hasta el siguiente ajuste del interés, según el caso, es igual al límite entre dos bandas, correspon-
derá realizar la imputación a la banda temporal más próxima a la fecha de cálculo.
```
**Heredado:** Sección 6. Capital mínimo por riesgo de mercado. / 6.2. Exigencia de capital por riesgo de tasa de interés. / La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu- los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio- nes preferidas no convertibles. Un título valor vendido y recomprado… / 6.2.2. Exigencia de capital por riesgo general de mercado: método de los plazos residuales.

**A** — error: None; salida: 1960 tokens

- Operacion «Compensaciones horizontales de posiciones netas»: Realización de dos series de compensaciones horizontales: primero entre posiciones netas dentro de cada una de las tres zonas de bandas temporales, y luego entre posiciones netas de las tres zonas ‖ tramo (exacta): «las entidades podrán realizar dos series de compensaciones horizontales: primero, entre las posiciones netas dentro de cada una de las tres zonas en las que se agrupan las bandas temporales y, luego, …»
- Restriccion «Desestimaciones horizontales en compensaciones»: Las compensaciones horizontales están sujetas a una escala de desestimaciones horizontales (exigencias adicionales) expresadas como porcentajes de las posiciones que se compensan, según zonas y bandas temporales ‖ tramo (exacta): «Dichas compensaciones estarán sujetas a la siguiente escala de desestimaciones horizontales -exigencias adicionales- expresadas como porcentajes de las posiciones que se compensan»
- Condicion «Imputación a banda temporal más próxima»: Cuando el plazo residual o el plazo hasta el siguiente ajuste del interés es igual al límite entre dos bandas, la imputación debe realizarse a la banda temporal más próxima a la fecha de cálculo ‖ tramo (exacta): «Al efecto de imputar una posición a la escala de vencimientos cuando el plazo residual o el plazo que resta hasta el siguiente ajuste del interés, según el caso, es igual al límite entre dos bandas, c…»
  - Operacion:Compensaciones horizontales de posiciones netas --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Desestimaciones horizontales en compensaciones --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Imputación a banda temporal más próxima --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Compensaciones horizontales de posiciones netas --aplica_a--> las entidades
  - Restriccion:Desestimaciones horizontales en compensaciones --limita--> Operacion:Compensaciones horizontales de posiciones netas
  - mención: aplica_a «las entidades» (verificada: exacta)
  - omisión tabla (exacta): «[TABLA cap::tabla037 | página 125 | e0_tablas | posicional] Fila 1: col1 = Zona | col2 = Banda | col3 = Porcentaje de desestimación aplicable: ⟨abarca hasta col…» — nota: Contenido tabular declarado NO-CONFIABLE por E0. Tabla con escala de desestimaciones horizontales por zona, banda temporal y porcentaje. No …
  - heredado_compuesto: 0

**B** — error: None; salida: 1975 tokens

- Operacion «Compensaciones horizontales de posiciones netas»: Realización de dos series de compensaciones horizontales: primero entre posiciones netas dentro de cada una de las tres zonas de bandas temporales, y luego entre posiciones netas de las tres zonas ‖ tramo (exacta): «las entidades podrán realizar dos series de compensaciones horizontales: primero, entre las posiciones netas dentro de cada una de las tres zonas en las que se agrupan las bandas temporales y, luego, …»
- Restriccion «Desestimaciones horizontales en compensaciones»: Las compensaciones horizontales están sujetas a una escala de desestimaciones horizontales (exigencias adicionales) expresadas como porcentajes de las posiciones que se compensan ‖ tramo (exacta): «Dichas compensaciones estarán sujetas a la siguiente escala de desestimaciones horizontales -exigencias adicionales- expresadas como porcentajes de las posiciones que se compensan»
- Condicion «Imputación a banda temporal por plazo residual»: Cuando el plazo residual o el plazo que resta hasta el siguiente ajuste del interés es igual al límite entre dos bandas, la imputación debe realizarse a la banda temporal más próxima a la fecha de cálculo ‖ tramo (exacta): «Al efecto de imputar una posición a la escala de vencimientos cuando el plazo residual o el plazo que resta hasta el siguiente ajuste del interés, según el caso, es igual al límite entre dos bandas, c…»
  - Operacion:Compensaciones horizontales de posiciones netas --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimaciones horizontales en compensaciones --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Imputación a banda temporal por plazo residual --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Operacion:Compensaciones horizontales de posiciones netas --aplica_a--> las entidades
  - Restriccion:Desestimaciones horizontales en compensaciones --limita--> Operacion:Compensaciones horizontales de posiciones netas
  - mención: aplica_a «las entidades» (verificada: exacta)
  - omisión tabla (exacta): «[TABLA cap::tabla037 | página 125 | e0_tablas | posicional] Fila 1: col1 = Zona | col2 = Banda | col3 = Porcentaje de desestimación aplicable: ⟨abarca hasta col…» — nota: Tabla serializada declarada NO-CONFIABLE por E0; contiene escala de desestimaciones horizontales con porcentajes por zona y banda temporal q…
  - heredado_compuesto: 0

## Ficha 25 — `cap::11.4`

**Texto propio:**

```
11.4. A los efectos de la determinación de la RPC, las entidades financieras podrán computar como
capital ordinario de nivel uno (COn1) la diferencia positiva entre la nueva previsión contable
computada según el punto 5.5 de la NIIF 9 –teniendo en cuenta, de corresponder, la metodo-
logía de prorrateo prevista en la Comunicación A 6847– y la previsión regulatoria calculada
según las normas sobre Previsiones Mínimas por Riesgo de Incobrabilidad o la contable co-
rrespondiente al balance de saldos del 30/11 del año anterior al de la aplicación por primera
vez del citado punto de la NIIF 9 –la mayor de ambas–.
```
**Heredado:** Sección 11. Otras disposiciones.

**A** — error: None; salida: 1051 tokens

- Operacion «Cómputo de diferencia positiva como COn1»: Cómputo como capital ordinario de nivel uno (COn1) de la diferencia positiva entre la nueva previsión contable según NIIF 9 punto 5.5 (con metodología de prorrateo de Com. A 6847 si corresponde) y la previsión regulatoria según normas de Previsiones Mínimas por Riesgo de Incobrabilidad o la contable… ‖ tramo (exacta): «computar como capital ordinario de nivel uno (COn1) la diferencia positiva entre la nueva previsión contable computada según el punto 5.5 de la NIIF 9 –teniendo en cuenta, de corresponder, la metodolo…»
- Potestad «Facultad de computar diferencia positiva como COn1»: Facultad de las entidades financieras de computar como capital ordinario de nivel uno la diferencia positiva entre previsiones contables y regulatorias en los términos especificados ‖ tramo (exacta): «las entidades financieras podrán computar como capital ordinario de nivel uno (COn1) la diferencia positiva»
- Comunicacion «Com. A 6847»:  ‖ tramo (exacta): «Comunicación A 6847»
  - Potestad:Facultad de computar diferencia positiva como COn1 --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Operacion:Cómputo de diferencia positiva como COn1 --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - TextoOrdenado:Texto Ordenado de Capitales Mínimos --referencia--> Comunicacion:Com. A 6847
  - Potestad:Facultad de computar diferencia positiva como COn1 --aplica_a--> las entidades financieras
  - mención: aplica_a «las entidades financieras» (verificada: exacta)
  - omisión meta_normativo (exacta): «A los efectos de la determinación de la RPC» — nota: Cláusula introductoria que fija el propósito o contexto de aplicación de la facultad, no una prescripción independiente
  - heredado_compuesto: 0

**B** — error: None; salida: 1048 tokens

- Operacion «Cómputo de diferencia positiva como COn1»: Cómputo como capital ordinario de nivel uno (COn1) de la diferencia positiva entre la nueva previsión contable según NIIF 9 punto 5.5 (con metodología de prorrateo de Com. A 6847 si corresponde) y la previsión regulatoria según normas de Previsiones Mínimas por Riesgo de Incobrabilidad o la contable… ‖ tramo (exacta): «las entidades financieras podrán computar como capital ordinario de nivel uno (COn1) la diferencia positiva entre la nueva previsión contable computada según el punto 5.5 de la NIIF 9 –teniendo en cue…»
- Potestad «Facultad de computar diferencia como COn1 para RPC»: Facultad de computar como capital ordinario de nivel uno la diferencia positiva entre previsiones, a efectos de la determinación de la RPC ‖ tramo (exacta): «las entidades financieras podrán computar como capital ordinario de nivel uno (COn1) la diferencia positiva»
- Comunicacion «Com. A 6847»:  ‖ tramo (exacta): «Comunicación A 6847»
  - Operacion:Cómputo de diferencia positiva como COn1 --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Potestad:Facultad de computar diferencia como COn1 para RPC --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - TextoOrdenado:Texto Ordenado Capitales Mínimos --referencia--> Comunicacion:Com. A 6847
  - Potestad:Facultad de computar diferencia como COn1 para RPC --aplica_a--> las entidades financieras
  - mención: aplica_a «las entidades financieras» (verificada: exacta)
  - omisión meta_normativo (exacta): «A los efectos de la determinación de la RPC» — nota: Cláusula de alcance/finalidad que contextualiza la operación pero no prescribe conducta propia
  - heredado_compuesto: 0

## Ficha 26 — `polcre::5.3`

**Texto propio:**

```
5.3. Tenencia de títulos valores del exterior.
No podrán registrarse tenencias de títulos valores públicos y privados del exterior, incluidos los
títulos de deuda o participaciones correspondientes a carteras de activos entre los que se cuen-
ten títulos valores del exterior, como tampoco de certificados de depósito argentinos
(CEDEAR), excepto que se trate inversiones en títulos públicos externos emitidos por países
miembros de la OCDE cuya deuda soberana cuente con una calificación internacional no infe-
rior a “AA”.
Además, se admite la tenencia de títulos de deuda o participaciones correspondientes a carte-
ras de activos constituidas en el exterior, siempre que estén integradas exclusivamente por títu-
los valores públicos nacionales y/o privados del país, así como de “depository receipts” que co-
rrespondan a dichos títulos valores.
```
**Heredado:** Sección 5. Financiamiento a residentes en el exterior.

**A** — error: None; salida: 1340 tokens

- Restriccion «Prohibición tenencia títulos valores exterior»: Prohibición de registrar tenencias de títulos valores públicos y privados del exterior, incluidos títulos de deuda o participaciones de carteras de activos que contengan títulos valores del exterior, y certificados de depósito argentinos (CEDEAR) ‖ tramo (exacta): «No podrán registrarse tenencias de títulos valores públicos y privados del exterior, incluidos los títulos de deuda o participaciones correspondientes a carteras de activos entre los que se cuenten tí…»
- Excepcion «Excepción títulos públicos OCDE calificación AA»: Se exceptúa la prohibición para inversiones en títulos públicos externos emitidos por países miembros de la OCDE con calificación de deuda soberana no inferior a AA ‖ tramo (exacta): «excepto que se trate inversiones en títulos públicos externos emitidos por países miembros de la OCDE cuya deuda soberana cuente con una calificación internacional no inferior a "AA"» ‖ umbrales: ['no inferior a "AA"']
- Obligacion «Admisión tenencia títulos deuda carteras exterior»: Se admite la tenencia de títulos de deuda o participaciones de carteras de activos constituidas en el exterior, siempre que estén integradas exclusivamente por títulos valores públicos nacionales y/o privados del país, así como depository receipts que correspondan a dichos títulos valores ‖ tramo (exacta): «se admite la tenencia de títulos de deuda o participaciones correspondientes a carteras de activos constituidas en el exterior, siempre que estén integradas exclusivamente por títulos valores públicos…»
- Condicion «Condición integración exclusiva títulos nacionales»: La tenencia se admite cuando las carteras estén integradas exclusivamente por títulos valores públicos nacionales y/o privados del país ‖ tramo (exacta): «siempre que estén integradas exclusivamente por títulos valores públicos nacionales y/o privados del país»
  - Restriccion:Prohibición tenencia títulos valores exterior --establecida_en--> TextoOrdenado:Política de Crédito
  - Excepcion:Excepción títulos públicos OCDE calificación AA --exceptua--> Restriccion:Prohibición tenencia títulos valores exterior
  - Excepcion:Excepción títulos públicos OCDE calificación AA --establecida_en--> TextoOrdenado:Política de Crédito
  - Obligacion:Admisión tenencia títulos deuda carteras exterior --establecida_en--> TextoOrdenado:Política de Crédito
  - Condicion:Condición integración exclusiva títulos nacionales --establecida_en--> TextoOrdenado:Política de Crédito
  - Condicion:Condición integración exclusiva títulos nacionales --condicion_de--> Obligacion:Admisión tenencia títulos deuda carteras exterior
  - Restriccion:Prohibición tenencia títulos valores exterior --aplica_a--> las entidades
  - Obligacion:Admisión tenencia títulos deuda carteras exterior --aplica_a--> las entidades
  - mención: aplica_a «las entidades» (verificada: no)
  - mención: aplica_a «las entidades» (verificada: no)
  - heredado_compuesto: 0

**B** — error: None; salida: 1500 tokens

- Restriccion «Prohibición tenencia títulos valores del exterior»: Se prohíbe registrar tenencias de títulos valores públicos y privados del exterior, incluidos títulos de deuda o participaciones de carteras de activos que contengan títulos valores del exterior, así como certificados de depósito argentinos (CEDEAR). ‖ tramo (exacta): «No podrán registrarse tenencias de títulos valores públicos y privados del exterior, incluidos los títulos de deuda o participaciones correspondientes a carteras de activos entre los que se cuenten tí…»
- Excepcion «Excepción títulos públicos OCDE calificación AA»: Se exceptúa la prohibición para inversiones en títulos públicos externos emitidos por países miembros de la OCDE cuya deuda soberana tenga calificación internacional no inferior a AA. ‖ tramo (exacta): «excepto que se trate inversiones en títulos públicos externos emitidos por países miembros de la OCDE cuya deuda soberana cuente con una calificación internacional no inferior a "AA"» ‖ umbrales: ['no inferior a "AA"']
- Potestad «Admisión tenencia títulos carteras constituidas exterior»: Se admite la tenencia de títulos de deuda o participaciones correspondientes a carteras de activos constituidas en el exterior. ‖ tramo (exacta): «se admite la tenencia de títulos de deuda o participaciones correspondientes a carteras de activos constituidas en el exterior»
- Condicion «Carteras integradas exclusivamente por títulos nacionales»: La tenencia se admite siempre que las carteras estén integradas exclusivamente por títulos valores públicos nacionales y/o privados del país. ‖ tramo (exacta): «siempre que estén integradas exclusivamente por títulos valores públicos nacionales y/o privados del país»
- Potestad «Admisión tenencia depository receipts títulos nacionales»: Se admite la tenencia de depository receipts que correspondan a títulos valores públicos nacionales y/o privados del país. ‖ tramo (no): «se admite la tenencia de "depository receipts" que correspondan a dichos títulos valores»
  - Restriccion:Prohibición tenencia títulos valores del exterior --establecida_en--> TextoOrdenado:Política de Crédito
  - Excepcion:Excepción títulos públicos OCDE calificación AA --establecida_en--> TextoOrdenado:Política de Crédito
  - Potestad:Admisión tenencia títulos carteras constituidas exterior --establecida_en--> TextoOrdenado:Política de Crédito
  - Condicion:Carteras integradas exclusivamente por títulos nacionales --establecida_en--> TextoOrdenado:Política de Crédito
  - Potestad:Admisión tenencia depository receipts títulos nacionales --establecida_en--> TextoOrdenado:Política de Crédito
  - Excepcion:Excepción títulos públicos OCDE calificación AA --exceptua--> Restriccion:Prohibición tenencia títulos valores del exterior
  - Condicion:Carteras integradas exclusivamente por títulos nacionales --condicion_de--> Potestad:Admisión tenencia títulos carteras constituidas exterior
  - Restriccion:Prohibición tenencia títulos valores del exterior --aplica_a--> las entidades
  - Potestad:Admisión tenencia títulos carteras constituidas exterior --aplica_a--> las entidades
  - Potestad:Admisión tenencia depository receipts títulos nacionales --aplica_a--> las entidades
  - mención: aplica_a «las entidades» (verificada: no)
  - mención: aplica_a «las entidades» (verificada: no)
  - mención: aplica_a «las entidades» (verificada: no)
  - heredado_compuesto: 0

## Ficha 27 — `cla::6.5.4.5`

**Texto propio:**

```
6.5.4.5. Cuente con refinanciaciones del capital adeudado y de los intereses devengados
vinculadas a una insuficiente capacidad para su pago, con otorgamiento de qui-
tas o con reducción en las tasas de interés pactadas –salvo que ello derive de
las condiciones del mercado– o cuando haya sido necesario recibir bienes en
pago de parte de las obligaciones. No obstante, el deudor cuyas deudas hayan
sido refinanciadas con otorgamiento de quitas de capital podrá ser recategoriza-
do directamente en niveles superiores (“con problemas”, “en observación”) por la
aplicación de la metodología establecida en el punto 2.2.6. de las normas sobre
“Previsiones mínimas por riesgo de incobrabilidad”, siempre que además se ob-
serven las otras condiciones previstas en las correspondientes categorías.
Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos
superiores a los 31 días del 10 % de las obligaciones refinanciadas y la totalidad
de los intereses devengados, con más el porcentaje acumulado que pudiera co-
rresponder si la refinanciación se hubiera otorgado de haberse encontrado el
deudor en la categoría inferior, podrá reclasificárselo en el nivel inmediato supe-
rior si, además, se observan las otras condiciones previstas en el citado nivel.
El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su
deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo pre-
cedente– y recibido crédito adicional en los términos a que se refiere el punto
2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad”, y
en la medida en que dicha financiación adicional no hubiese sido cancelada, de-
berá permanecer en esta categoría por lo menos 180 días contados desde la fe-
cha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refi-
nanciación, la circunstancia más reciente. Ello, salvo que por aplicación de otras
pautas corresponda categorizarlo en el nivel inferior.
```
**Heredado:** Sección 6. Clasificación de los deudores de la cartera comercial. / 6.5. Niveles de clasificación. / Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si- guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta- llan en cada caso. Los clientes que no registren asistencia crediticia … / 6.5.4. Con alto riesgo de insolvencia. / El análisis del flujo de fondos del cliente demuestra que es altamente improbable que pueda atender la totalidad de sus compromisos financieros. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:

**A = B (iguales byte a byte)** — error: None; salida: 3065 tokens

- Operacion «Refinanciación de capital e intereses»: Refinanciación del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad para su pago, con otorgamiento de quitas o con reducción en las tasas de interés pactadas, o cuando haya sido necesario recibir bienes en pago de parte de las obligaciones. ‖ tramo (exacta): «Cuente con refinanciaciones del capital adeudado y de los intereses devengados»
- Restriccion «Indicador de alto riesgo — refinanciaciones con quitas o reducción de tasas»: Indicador de clasificación en categoría de alto riesgo de insolvencia: refinanciaciones con otorgamiento de quitas o reducción de tasas (salvo por condiciones de mercado) o recepción de bienes en pago de obligaciones. ‖ tramo (exacta): «Cuente con refinanciaciones del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad para su pago, con otorgamiento de quitas o con reducción en las tasas de interés …»
- Excepcion «Excepción — reducción de tasas por condiciones de mercado»: No se considera indicador de alto riesgo la reducción en las tasas de interés pactadas cuando derive de las condiciones del mercado. ‖ tramo (exacta): «salvo que ello derive de las condiciones del mercado»
- Potestad «Recategorización directa a niveles superiores — aplicación de metodología»: Facultad de recategorizar directamente en niveles superiores (con problemas, en observación) al deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital, por aplicación de la metodología del punto 2.2.6 de normas sobre previsiones mínimas. ‖ tramo (exacta): «el deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital podrá ser recategorizado directamente en niveles superiores ("con problemas", "en observación") por la aplicación …»
- Condicion «Condición para recategorización — observancia de otras condiciones»: La recategorización requiere que además se observen las otras condiciones previstas en las correspondientes categorías. ‖ tramo (exacta): «siempre que además se observen las otras condiciones previstas en las correspondientes categorías»
- Obligacion «Reclasificación a nivel inmediato superior — pago del 10 % sin atrasos»: Facultad de reclasificar al deudor en el nivel inmediato superior cuando haya pagado sin atrasos superiores a 31 días el 10 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, más el porcentaje acumulado que correspondería si la refinanciación se hubiera otorgado en categ… ‖ tramo (exacta): «Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 10 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, con más el …» ‖ umbrales: ['sin haber incurrido en atrasos superiores a los 31 días', 'del 10 % de las obligaciones refinanciadas']
- Condicion «Condición para reclasificación — observancia de otras condiciones del nivel»: La reclasificación al nivel inmediato superior requiere que además se observen las otras condiciones previstas en ese nivel. ‖ tramo (exacta): «si, además, se observan las otras condiciones previstas en el citado nivel»
- Restriccion «Permanencia mínima en categoría — 180 días tras crédito adicional»: Obligación de permanecer en la categoría de alto riesgo por lo menos 180 días contados desde la fecha más reciente entre el otorgamiento de crédito adicional o la celebración del acuerdo de refinanciación, cuando el deudor haya refinanciado su deuda y recibido crédito adicional que no haya sido canc… ‖ tramo (exacta): «El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo precedente– y recibido crédito adicional en lo…» ‖ umbrales: ['por lo menos 180 días']
- Excepcion «Excepción a permanencia mínima — categorización en nivel inferior»: No aplica la permanencia mínima de 180 días si por aplicación de otras pautas corresponde categorizar al deudor en el nivel inferior. ‖ tramo (exacta): «Ello, salvo que por aplicación de otras pautas corresponda categorizarlo en el nivel inferior»
  - Operacion:Refinanciación de capital e intereses --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Restriccion:Indicador de alto riesgo — refinanciaciones con quitas o reducción de … --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Excepcion:Excepción — reducción de tasas por condiciones de mercado --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Potestad:Recategorización directa a niveles superiores — aplicación de metodolo… --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Condicion:Condición para recategorización — observancia de otras condiciones --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Obligacion:Reclasificación a nivel inmediato superior — pago del 10 % sin atrasos --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Condicion:Condición para reclasificación — observancia de otras condiciones del … --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Restriccion:Permanencia mínima en categoría — 180 días tras crédito adicional --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Excepcion:Excepción a permanencia mínima — categorización en nivel inferior --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Excepcion:Excepción — reducción de tasas por condiciones de mercado --exceptua--> Restriccion:Indicador de alto riesgo — refinanciaciones con quitas o reducción de …
  - Condicion:Condición para recategorización — observancia de otras condiciones --condicion_de--> Potestad:Recategorización directa a niveles superiores — aplicación de metodolo…
  - Condicion:Condición para reclasificación — observancia de otras condiciones del … --condicion_de--> Obligacion:Reclasificación a nivel inmediato superior — pago del 10 % sin atrasos
  - Excepcion:Excepción a permanencia mínima — categorización en nivel inferior --exceptua--> Restriccion:Permanencia mínima en categoría — 180 días tras crédito adicional
  - omisión relacion_sin_predicado (exacta): «el deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital podrá ser recategorizado directamente en niveles superiores» — nota: Relación entre Potestad (e4) y Operacion (e1): la potestad de recategorizar se habilita cuando se ha realizado la operación de refinanciació…
  - heredado_compuesto: 0

