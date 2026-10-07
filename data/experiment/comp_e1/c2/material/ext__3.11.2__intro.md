# `ext::3.11.2::intro` — [bloque intro] Las entidades podrán dar acceso al mercado de cambios a los residentes que deban

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* 3.11. Otras compras de moneda extranjera por parte de residentes con aplicación específica.
> *heredado:* 3.11.2. Las entidades podrán dar acceso al mercado de cambios a los residentes que deban
> *propio:* realizar pagos de servicios de deudas financieras comprendidas en el punto 3.5. o de títulos valores con acceso al mercado de cambios en función de lo dispuesto en los puntos 3.6.1.3. a 3.6.1.5., para la compra de moneda extranjera con anterioridad al plazo admitido por la normativa para cada caso, en las siguientes condiciones:

## Omisiones leídas en T4 (M2)

con_marca:20 [normativa; propio] «en las siguientes condiciones:»

## Código A

- **p1 Potestad** «Acceso anticipado al mercado de cambios para pago de deudas» — Las entidades pueden dar acceso al mercado de cambios a residentes que deban pagar servicios de deudas financieras (punto 3.5.) o de títulos valores (puntos 3.6.1.3. a 3.6.1.5.), para comprar moneda extranjera con anterioridad al plazo admitido por la normativa en cada caso, en las condiciones que siguen. · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a los residentes que deban realizar pagos de servicios de deudas financieras comprendidas en el punto 3.5. o de títulos valores con acceso al mercado de cambios en función de lo dispuesto en los puntos 3.6.1.3. a 3.6.1.5., para la compra de moneda extranjera con ant…»
- **o1 Operacion** «Compra anticipada de moneda extranjera para pago de deudas» — Compra de moneda extranjera por residentes, con anterioridad al plazo admitido por la normativa para cada caso, para pagar servicios de deudas financieras comprendidas en el punto 3.5. o de títulos valores con acceso al mercado de cambios según los puntos 3.6.1.3. a 3.6.1.5. · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «para la compra de moneda extranjera con anterioridad al plazo admitido por la normativa para cada caso»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)

### A — omisiones de T4 a clasificar

- con_marca:20 → entidades: p1 Potestad [exacta] solap 1.0 contiene | omisiones: —

## Código H

- **p1 Potestad** «Dar acceso anticipado al mercado de cambios» — Las entidades pueden dar acceso al mercado de cambios a residentes que deban pagar servicios de deudas financieras (punto 3.5.) o de títulos valores con acceso al mercado de cambios (puntos 3.6.1.3. a 3.6.1.5.), para comprar moneda extranjera antes del plazo admitido por la normativa en cada caso, en las condiciones que enumeran los ítems siguientes. · no definidas: `{"condiciones": "en las siguientes condiciones: (enumeradas en los ítems siguientes)"}` · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a los residentes que deban realizar pagos de servicios de deudas financieras comprendidas en el punto 3.5. o de títulos valores con acceso al mercado de cambios en función de lo dispuesto en los puntos 3.6.1.3. a 3.6.1.5., para la compra de moneda extranjera con ant…»
- **o1 Operacion** «Compra anticipada de moneda extranjera para pago de deudas» — Compra de moneda extranjera por residentes, con acceso al mercado de cambios, con anterioridad al plazo admitido por la normativa para cada caso, para pagar servicios de deudas financieras comprendidas en el punto 3.5. o de títulos valores con acceso según los puntos 3.6.1.3. a 3.6.1.5. · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «para la compra de moneda extranjera con anterioridad al plazo admitido por la normativa para cada caso»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)
- R: o1 Operacion —aplica_a→ Sujeto_sector_privado_no_financiero (mención «los residentes»)

### H — omisiones de T4 a clasificar

- con_marca:20 → entidades: — | omisiones: —

## Código K

- **e1 Potestad** «Acceso anticipado al MLC para servicios de deuda» — Las entidades podrán dar acceso al mercado de cambios a los residentes que deban realizar pagos de servicios de deudas financieras comprendidas en el punto 3.5. o de títulos valores con acceso al mercado de cambios según los puntos 3.6.1.3. a 3.6.1.5., para comprar moneda extranjera antes del plazo admitido por la normativa para cada caso, en las condiciones que se enumeran a continuación. · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a los residentes que deban»
- **e2 Operacion** «Compra anticipada de moneda extranjera para servicios de deuda» — Compra de moneda extranjera por residentes, con anterioridad al plazo admitido por la normativa, para pagar servicios de deudas financieras del punto 3.5. o de títulos valores con acceso según puntos 3.6.1.3. a 3.6.1.5. · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «para la compra de moneda extranjera con anterioridad al plazo admitido por la normativa para cada caso»
- R: e1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)
- R: Sujeto (mención «los residentes») —ejecuta→ e2 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «Las entidades podrán dar acceso al mercado de cambios a los residentes que deban» — Vínculo Potestad → Operacion (habilita); no hay predicado

### K — omisiones de T4 a clasificar

- con_marca:20 → entidades: — | omisiones: —

## Código W

- **e1 Potestad** «Acceso anticipado para pago de deudas — entidades» — Las entidades podrán dar acceso al mercado de cambios a los residentes que deban realizar pagos de servicios de deudas financieras comprendidas en el punto 3.5. o de títulos valores con acceso según los puntos 3.6.1.3. a 3.6.1.5., para la compra de moneda extranjera con anterioridad al plazo admitido por la normativa para cada caso, en las condiciones que se enumeran a continuación. · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a los residentes que deban»
- **e2 Operacion** «Compra anticipada de moneda extranjera para servicios de deuda» — Compra de moneda extranjera por residentes en el mercado de cambios, con anterioridad al plazo admitido por la normativa, para pagos de servicios de deudas financieras del punto 3.5. o de títulos valores con acceso según puntos 3.6.1.3. a 3.6.1.5. · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «para la compra de moneda extranjera con anterioridad al plazo admitido por la normativa para cada caso»
- R: e1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)
- R: e2 Operacion —aplica_a→ Sujeto (mención «los residentes»)
- R: Sujeto (mención «los residentes») —ejecuta→ e2 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «Las entidades podrán dar acceso al mercado de cambios a los residentes» — Vínculo Potestad → Operacion (habilita); no hay predicado para él

### W — omisiones de T4 a clasificar

- con_marca:20 → entidades: — | omisiones: —

