# `ctacte::2.1.1.4` — Lugar y fecha.

Grupos: omisiones. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 2. Movimiento de las cuentas.
> *heredado:* 2.1. Créditos.
> *heredado:* 2.1.1. Mediante depósitos por ventanilla o cajeros automáticos.
> *heredado:* Cuando se empleen boletas, éstas deberán contener, como mínimo, los siguientes datos:
> *heredado:* Respecto de la realización de operaciones mediante cajeros automáticos, las entidades deberán tener implementados mecanismos de seguridad informática que garanticen la genuinidad de las operaciones.
> *propio:* 2.1.1.4. Lugar y fecha.

## Omisiones leídas en T4 (M2)

sin_marca:25 [normativa; propio] «2.1.1.4. Lugar y fecha.»

## Código A

- **o1 Obligacion** «Boleta de depósito: consignar lugar y fecha» — Cuando se empleen boletas en depósitos por ventanilla o cajeros automáticos, éstas deberán contener, como mínimo, el dato de lugar y fecha (uno de los datos mínimos enumerados; deben incluirse todos). · props: `{"tipo": "otra"}` · tramo [exacta]: «Cuando se empleen boletas, éstas deberán contener, como mínimo, los siguientes datos: […] Lugar y fecha.»
- **c1 Condicion** «Empleo de boletas en depósitos» — Supuesto de que se empleen boletas en los depósitos por ventanilla o cajeros automáticos, que activa el deber de que contengan los datos mínimos, entre ellos lugar y fecha. · tramo [exacta]: «Cuando se empleen boletas»
- R: c1 Condicion —condicion_de→ o1 Obligacion

### A — omisiones de T4 a clasificar

- sin_marca:25 → entidades: o1 Obligacion [exacta] solap 0.4 | omisiones: —

## Código H

- **o1 Obligacion** «Boletas de depósito: consignar lugar y fecha» — Cuando se empleen boletas para depósitos por ventanilla o cajeros automáticos, éstas deben contener, como mínimo, entre otros datos, el lugar y la fecha. · props: `{"tipo": "otra"}` · tramo [exacta]: «Cuando se empleen boletas, éstas deberán contener, como mínimo, los siguientes datos: […] Lugar y fecha.»

### H — omisiones de T4 a clasificar

- sin_marca:25 → entidades: o1 Obligacion [exacta] solap 0.4 | omisiones: —

## Código K

- **op1 Operacion** «Depósito por ventanilla o cajero automático» — Crédito en cuenta corriente mediante depósitos por ventanilla o cajeros automáticos · props: `{"tipo": "depósito"}` · tramo [exacta]: «Mediante depósitos por ventanilla o cajeros automáticos.»
- **ob1 Obligacion** «Lugar y fecha — dato mínimo de boletas de depósito» — Cuando se empleen boletas para depósitos por ventanilla o cajeros automáticos, éstas deberán contener, como mínimo y junto con los demás datos enumerados (todos exigidos), el lugar y la fecha. · props: `{"tipo": "otra"}` · tramo [exacta]: «Cuando se empleen boletas, éstas deberán contener, como mínimo, los siguientes datos: […] Lugar y fecha.»
- **c1 Condicion** «Empleo de boletas en el depósito» — Que se empleen boletas para el depósito. · tramo [exacta]: «Cuando se empleen boletas»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: c1 Condicion —condicion_de→ ob1 Obligacion
- R: ob1 Obligacion —aplica_a→ Sujeto_banco (mención «las entidades»)

### K — omisiones de T4 a clasificar

- sin_marca:25 → entidades: ob1 Obligacion [exacta] solap 0.4 | omisiones: —

## Código W

- **e1 Obligacion** «Lugar y fecha — contenido mínimo boleta de depósito» — Cuando se empleen boletas para depósitos en cuenta corriente por ventanilla o cajeros automáticos, éstas deberán contener, como mínimo, el lugar y la fecha (junto con los demás datos de la lista, todos exigidos). · props: `{"tipo": "otra"}` · tramo [exacta]: «Cuando se empleen boletas, éstas deberán contener, como mínimo, los siguientes datos: […] Lugar y fecha.»
- **e2 Operacion** «Depósito en cuenta corriente por ventanilla o cajero» — Crédito en cuenta corriente mediante depósitos por ventanilla o cajeros automáticos · props: `{"tipo": "deposito"}` · tramo [exacta]: «Mediante depósitos por ventanilla o cajeros automáticos.»
- **e3 Condicion** «Empleo de boletas en el depósito» — Que en el depósito se empleen boletas. · tramo [exacta]: «Cuando se empleen boletas»
- R: e1 Obligacion —regula→ e2 Operacion
- R: e3 Condicion —condicion_de→ e1 Obligacion

### W — omisiones de T4 a clasificar

- sin_marca:25 → entidades: e1 Obligacion [exacta] solap 0.4 | omisiones: —

