# `ric::4.5.2` — Futuros y Contratos a Término, incluidos los FRA

Grupos: grupo_c. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 4. Exigencia e integración por riesgo de mercado
> *heredado:* 4.5. Información sobre instrumentos derivados
> *propio:* 4.5.2. Futuros y Contratos a Término, incluidos los FRA [TABLA ric::tabla012 | página 19 | e0_tablas | posicional] Fila 1: col1 = Descripción del activo subyacente(1) | col2 = Fecha correspondiente al plazo residual del subyacente (cuando corresponda)(2) | col3 = Vencimiento del derivado | col4 = Contraparte/Ámb ito de negociación | col5 = Valor nocional(3) | col6 = Tasa de cupón del activo subyacente (cuando corresponda)(4) | col7 = Precio pactado del subyacente (5) | col8 = Precio de mercado del activo subyacente | col9 = Compra / venta a término (6) [FIN TABLA ric::tabla012] (1) Describir el activo comprado o vendido a futuro. Por ejemplo: Tasa de interés Badlar Privada para depósitos de más de 1 millón de pesos por un plazo de 30 a 35 días, dólar estadounidense, Bono de la Nación Arg. en dólar link con vencimiento al 2017 - AJ17D, etc. (2) Por ejemplo, en un futuro sobre un título público es el plazo residual del título público subyacente. (3) Especificar el valor nocional incluyendo la moneda o unidad de medida. Por ejemplo, USD 25.000.000, $ 100.000, etc. (4) Por ejemplo, en un futuro sobre un título público, es la tasa del cupón corriente de dicho título (5) Valor del subyacente pactado. Por ejemplo, valor de la tasa fija pactada, valor pactado del dólar, valor pactado del bono, etc. (6) Consignar "C" si el contrato en cuestión es una compra a término, o "V" si es una venta a término.

## Supuestos de la fase A de T4 (M1)

1. ««C» si es compra a término»
2. ««V» si es venta»

## Código A

- **op1 Operacion** «Información de futuros y contratos a término, incluidos FRA» — Presentación informativa sobre instrumentos derivados: futuros y contratos a término, incluidos los FRA, con los datos de la tabla (activo subyacente, plazo residual, vencimiento, contraparte/ámbito, valor nocional, tasa de cupón, precio pactado, precio de mercado, compra/venta). · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Futuros y Contratos a Término, incluidos los FRA»
- **ob1 Obligacion** «Informar datos del futuro o contrato a término» — Informar, por cada futuro o contrato a término (incluidos FRA): descripción del activo subyacente, fecha del plazo residual del subyacente (cuando corresponda), vencimiento del derivado, contraparte/ámbito de negociación y valor nocional (con moneda o unidad de medida). · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Descripción del activo subyacente(1) | col2 = Fecha correspondiente al plazo residual del subyacente (cuando corresponda)(2) | col3 = Vencimiento del derivado | col4 = Contraparte/Ámb ito de negociación | col5 = Valor nocional(3)»
- **ob2 Obligacion** «Informar precios, tasa de cupón y sentido C/V» — Informar, por cada futuro o contrato a término (incluidos FRA): tasa de cupón del activo subyacente (cuando corresponda), precio pactado del subyacente, precio de mercado del activo subyacente y si es compra ("C") o venta ("V") a término. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Tasa de cupón del activo subyacente (cuando corresponda)(4) | col7 = Precio pactado del subyacente (5) | col8 = Precio de mercado del activo subyacente | col9 = Compra / venta a término (6)»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- Omisión `fuera_de_tipos` [exacta]: «(1) Describir el activo comprado o vendido a futuro.» — Instrucción de cómo completar la columna (notas explicativas 1 a 6 con ejemplos); su contenido sustantivo está recogido en las obligaciones de informar. Tipo que se habría usado: Definicion o descripc…
- Omisión `fuera_de_tipos` [exacta]: «(6) Consignar "C" si el contrato en cuestión es una compra a término, o "V" si es una venta a término.» — Instrucción de codificación del campo; se recoge en la descripción de la obligación. Tipo que se habría usado: Obligacion de tipo otra.

### A — supuestos a clasificar

- 1. ««C» si es compra a término» → candidatos: ob2 Obligacion (1.00), op1 Operacion (1.00), ob1 Obligacion (0.50)
- 2. ««V» si es venta» → candidatos: ob2 Obligacion (1.00), op1 Operacion (1.00)

## Código H

- **op1 Operacion** «Información de futuros y contratos a término, incluidos FRA» — Presentación informativa sobre instrumentos derivados: futuros y contratos a término, incluidos los FRA, con los datos del activo subyacente, vencimiento, contraparte/ámbito, valor nocional, tasa de cupón, precios y compra/venta a término. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Futuros y Contratos a Término, incluidos los FRA»
- **ob1 Obligacion** «Describir el activo subyacente comprado o vendido a futuro» — Describir el activo comprado o vendido a futuro (columna Descripción del activo subyacente). · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Describir el activo comprado o vendido a futuro.»
- **ob2 Obligacion** «Especificar valor nocional con moneda o unidad» — Especificar el valor nocional incluyendo la moneda o unidad de medida (columna Valor nocional). · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Especificar el valor nocional incluyendo la moneda o unidad de medida.»
- **ob3 Obligacion** «Consignar C o V según compra o venta a término» — Consignar "C" si el contrato es una compra a término, o "V" si es una venta a término (columna Compra / venta a término). · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Consignar "C" si el contrato en cuestión es una compra a término, o "V" si es una venta a término.»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion
- Omisión `fuera_de_tipos` [exacta]: «(2) Por ejemplo, en un futuro sobre un título público es el plazo residual del título público subyacente.» — Nota explicativa de la columna 'Fecha correspondiente al plazo residual del subyacente'; ejemplo, sin deber autónomo. Se habría usado Definicion.
- Omisión `fuera_de_tipos` [exacta]: «(5) Valor del subyacente pactado. Por ejemplo, valor de la tasa fija pactada, valor pactado del dólar, valor pactado del bono, etc.» — Definición del campo 'Precio pactado del subyacente'; el rótulo de la tabla indica el campo sin mandar una conducta. Se habría usado Definicion.
- Omisión `fuera_de_tipos` [exacta]: «(4) Por ejemplo, en un futuro sobre un título público, es la tasa del cupón corriente de dicho título» — Nota explicativa de la columna 'Tasa de cupón del activo subyacente'; ejemplo, sin deber autónomo. Se habría usado Definicion.

### H — supuestos a clasificar

- 1. ««C» si es compra a término» → candidatos: ob3 Obligacion (1.00), op1 Operacion (1.00)
- 2. ««V» si es venta» → candidatos: ob3 Obligacion (1.00), op1 Operacion (1.00)

## Código K

- **e1 Operacion** «Información sobre futuros y contratos a término (FRA)» — Información sobre instrumentos derivados: futuros y contratos a término, incluidos los FRA, en el marco de la exigencia por riesgo de mercado · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Futuros y Contratos a Término, incluidos los FRA»
- **e2 Obligacion** «Columnas a informar — futuros y contratos a término» — Informar por cada futuro o contrato a término: descripción del activo subyacente, fecha del plazo residual del subyacente (cuando corresponda), vencimiento del derivado, contraparte/ámbito de negociación, valor nocional, tasa de cupón del subyacente (cuando corresponda), precio pactado, precio de mercado del subyacente y compra/venta a término · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Fila 1: col1 = Descripción del activo subyacente(1) | col2 = Fecha correspondiente al plazo residual del subyacente (cuando corresponda)(2) | col3 = Vencimiento del derivado | col4 = Contraparte/Ámb ito de negociación | col5 = Valor nocional(3) | col6 = Tasa de cupón del activo subyacente (cuando corresponda)(4) | col7…»
- **e3 Obligacion** «Describir activo subyacente comprado o vendido» — Describir el activo comprado o vendido a futuro (ej.: tasa Badlar Privada, dólar estadounidense, bono AJ17D) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Describir el activo comprado o vendido a futuro.»
- **e4 Obligacion** «Valor nocional con moneda o unidad» — Especificar el valor nocional incluyendo la moneda o unidad de medida (ej.: USD 25.000.000, $ 100.000) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Especificar el valor nocional incluyendo la moneda o unidad de medida.»
- **e5 Obligacion** «Consignar C o V según compra/venta» — Consignar "C" si el contrato es compra a término o "V" si es venta a término · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Consignar "C" si el contrato en cuestión es una compra a término, o "V" si es una venta a término.»
- **e6 Definicion** «Plazo residual del subyacente» — Ej.: en un futuro sobre un título público, el plazo residual del título público subyacente · props: `{"termino": "Fecha correspondiente al plazo residual del subyacente"}` · tramo [exacta]: «en un futuro sobre un título público es el plazo residual del título público subyacente»
- **e7 Definicion** «Tasa de cupón del activo subyacente» — Ej.: en un futuro sobre un título público, la tasa del cupón corriente de dicho título · props: `{"termino": "Tasa de cupón del activo subyacente"}` · tramo [exacta]: «en un futuro sobre un título público, es la tasa del cupón corriente de dicho título»
- **e8 Definicion** «Precio pactado del subyacente» — Valor del subyacente pactado: tasa fija pactada, valor pactado del dólar, del bono, etc. · props: `{"termino": "Precio pactado del subyacente"}` · tramo [exacta]: «Valor del subyacente pactado.»
- R: e2 Obligacion —regula→ e1 Operacion
- R: e3 Obligacion —regula→ e1 Operacion
- R: e4 Obligacion —regula→ e1 Operacion
- R: e5 Obligacion —regula→ e1 Operacion

### K — supuestos a clasificar

- 1. ««C» si es compra a término» → candidatos: e2 Obligacion (1.00), e5 Obligacion (1.00), e1 Operacion (0.50)
- 2. ««V» si es venta» → candidatos: e2 Obligacion (1.00), e5 Obligacion (1.00)

## Código W

- **op1 Operacion** «Información de futuros y contratos a término (FRA)» — Presentación de información sobre futuros y contratos a término, incluidos los FRA, en el marco de la información sobre instrumentos derivados por riesgo de mercado · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Futuros y Contratos a Término, incluidos los FRA»
- **o1 Obligacion** «Campos del cuadro — futuros y contratos a término» — Informar por cada futuro o contrato a término: descripción del activo subyacente, fecha del plazo residual del subyacente (cuando corresponda), vencimiento del derivado, contraparte/ámbito de negociación, valor nocional, tasa de cupón del subyacente (cuando corresponda), precio pactado del subyacente, precio de mercado del subyacente y compra/venta a término · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Fila 1: col1 = Descripción del activo subyacente(1) | col2 = Fecha correspondiente al plazo residual del subyacente (cuando corresponda)(2) | col3 = Vencimiento del derivado | col4 = Contraparte/Ámb ito de negociación | col5 = Valor nocional(3) | col6 = Tasa de cupón del activo subyacente (cuando corresponda)(4) | col7…»
- **o2 Obligacion** «Describir activo subyacente comprado o vendido» — Describir el activo comprado o vendido a futuro (p. ej. tasa Badlar Privada, dólar estadounidense, bono AJ17D) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Describir el activo comprado o vendido a futuro.»
- **o3 Obligacion** «Valor nocional con moneda o unidad» — Especificar el valor nocional incluyendo la moneda o unidad de medida (p. ej. USD 25.000.000, $ 100.000) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Especificar el valor nocional incluyendo la moneda o unidad de medida.»
- **o4 Obligacion** «Consignar C o V — compra/venta a término» — Consignar "C" si el contrato es una compra a término o "V" si es una venta a término · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Consignar "C" si el contrato en cuestión es una compra a término, o "V" si es una venta a término.»
- **d1 Definicion** «Fecha de plazo residual del subyacente» — Por ejemplo, en un futuro sobre un título público es el plazo residual del título público subyacente · props: `{"termino": "Fecha correspondiente al plazo residual del subyacente"}` · tramo [exacta]: «en un futuro sobre un título público es el plazo residual del título público subyacente»
- **d2 Definicion** «Tasa de cupón del activo subyacente» — Por ejemplo, en un futuro sobre un título público, es la tasa del cupón corriente de dicho título · props: `{"termino": "Tasa de cupón del activo subyacente"}` · tramo [exacta]: «en un futuro sobre un título público, es la tasa del cupón corriente de dicho título»
- **d3 Definicion** «Precio pactado del subyacente» — Valor del subyacente pactado, p. ej. tasa fija pactada, valor pactado del dólar o del bono · props: `{"termino": "Precio pactado del subyacente"}` · tramo [exacta]: «Valor del subyacente pactado.»
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o4 Obligacion —regula→ op1 Operacion

### W — supuestos a clasificar

- 1. ««C» si es compra a término» → candidatos: o1 Obligacion (1.00), o4 Obligacion (1.00), op1 Operacion (0.50)
- 2. ««V» si es venta» → candidatos: o1 Obligacion (1.00), o4 Obligacion (1.00)

