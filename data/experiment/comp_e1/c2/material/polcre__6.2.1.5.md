# `polcre::6.2.1.5` — Al momento del otorgamiento de financiaciones a personas humanas, se deberá

Grupos: omisiones. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 6. Préstamos de Unidades de Valor Adquisitivo y de Unidades de Vivienda.
> *heredado:* 6.2. Préstamos de Unidades de Vivienda actualizables por el "ICC" - Ley 27.271 ("UVI").
> *heredado:* 6.2.1. Las operaciones de financiación de Unidades de Vivienda actualizables por el índice del
> *heredado:* costo de construcción ("ICC") - Ley 27.271 ("UVI") estarán sujetas a las siguientes condiciones:
> *propio:* 6.2.1.5. Al momento del otorgamiento de financiaciones a personas humanas, se deberá tener especial atención a la relación cuota/ingreso de manera de que el deudor pueda afrontar posibles incrementos en el importe de las cuotas sin afectar su capacidad de pago, teniendo en cuenta que sus ingresos pueden no seguir la evolución de la Unidad de Vivienda actualizable por "ICC" ("UVI") ni la del "CVS".

## Omisiones leídas en T4 (M2)

con_marca:5 [normativa; heredado] «Las operaciones de financiación de Unidades de Vivienda actualizables por el índice del costo de construcción ("ICC") - Ley 27.271 ("UVI") estarán sujetas a las siguientes condiciones»

## Código A

- **op1 Operacion** «Otorgamiento de financiaciones UVI a personas humanas» — Otorgamiento de financiaciones en Unidades de Vivienda actualizables por ICC (UVI) a personas humanas. · props: `{"tipo": "financiacion"}` · tramo [exacta]: «Al momento del otorgamiento de financiaciones a personas humanas»
- **ob1 Obligacion** «Atención especial a relación cuota/ingreso en UVI» — Al otorgar financiaciones UVI a personas humanas, se debe tener especial atención a la relación cuota/ingreso, de modo que el deudor pueda afrontar posibles incrementos de las cuotas sin afectar su capacidad de pago, considerando que sus ingresos pueden no seguir la evolución de la UVI ni la del CVS. · props: `{"tipo": "otra"}` · tramo [no]: «estarán sujetas a las siguientes condiciones: [â€¦] se deberá tener especial atención a la relación cuota/ingreso de manera de que el deudor pueda afrontar posibles incrementos en el importe de las cuotas sin afectar su capacidad de pago»
- R: ob1 Obligacion —regula→ op1 Operacion

### A — omisiones de T4 a clasificar

- con_marca:5 → entidades: — | omisiones: —

## Código H

- **op1 Operacion** «Otorgamiento de financiaciones UVI a personas humanas» — Otorgamiento de financiaciones de Unidades de Vivienda actualizables por ICC (UVI) a personas humanas · props: `{"tipo": "financiacion"}` · tramo [exacta]: «Al momento del otorgamiento de financiaciones a personas humanas»
- **ob1 Obligacion** «Atención especial a relación cuota/ingreso en UVI» — Al otorgar financiaciones UVI a personas humanas, se debe tener especial atención a la relación cuota/ingreso para que el deudor pueda afrontar posibles incrementos de las cuotas sin afectar su capacidad de pago, teniendo en cuenta que sus ingresos pueden no seguir la evolución de la UVI ni la del CVS · props: `{"tipo": "otra"}` · tramo [no]: «Las operaciones de financiación de Unidades de Vivienda actualizables por el índice del costo de construcción ("ICC") - Ley 27.271 ("UVI") estarán sujetas a las siguientes condiciones: […] se deberá tener especial atención a la relación cuota/ingreso de manera de que el deudor pueda afrontar posibles incrementos en el …»
- R: ob1 Obligacion —regula→ op1 Operacion

### H — omisiones de T4 a clasificar

- con_marca:5 → entidades: ob1 Obligacion [no] solap 1.0 contiene | omisiones: —

## Código K

- **e1 Operacion** «Financiación UVI a personas humanas» — Otorgamiento de financiaciones en Unidades de Vivienda actualizables por ICC (UVI) - Ley 27.271 a personas humanas · props: `{"tipo": "financiación"}` · tramo [exacta]: «Al momento del otorgamiento de financiaciones a personas humanas»
- **e2 Obligacion** «Atención relación cuota/ingreso — financiación UVI» — Condición a la que están sujetas las financiaciones UVI: al otorgarlas a personas humanas, se debe tener especial atención a la relación cuota/ingreso para que el deudor pueda afrontar posibles incrementos de las cuotas sin afectar su capacidad de pago, considerando que sus ingresos pueden no seguir la evolución de la UVI ni del CVS. · props: `{"tipo": "otra"}` · tramo [exacta]: «estarán sujetas a las siguientes condiciones […] se deberá tener especial atención a la relación cuota/ingreso de manera de que el deudor pueda afrontar posibles incrementos en el importe de las cuotas sin afectar su capacidad de pago»
- R: e2 Obligacion —regula→ e1 Operacion

### K — omisiones de T4 a clasificar

- con_marca:5 → entidades: — | omisiones: —

## Código W

- **e1 Operacion** «Otorgamiento de financiaciones UVI a personas humanas» — Otorgamiento de financiaciones de Unidades de Vivienda actualizables por ICC - Ley 27.271 (UVI) a personas humanas · props: `{"tipo": "financiación"}` · tramo [exacta]: «Al momento del otorgamiento de financiaciones a personas humanas»
- **e2 Obligacion** «Atención relación cuota/ingreso — financiaciones UVI» — Las operaciones de financiación UVI están sujetas a la condición de que, al otorgar financiaciones a personas humanas, se tenga especial atención a la relación cuota/ingreso, de manera que el deudor pueda afrontar posibles incrementos en el importe de las cuotas sin afectar su capacidad de pago, teniendo en cuenta que sus ingresos pueden no seguir la evolución de la UVI ni la del CVS. · props: `{"tipo": "otra"}` · tramo [exacta]: «estarán sujetas a las siguientes condiciones […] Al momento del otorgamiento de financiaciones a personas humanas, se deberá tener especial atención a la relación cuota/ingreso»
- R: e2 Obligacion —regula→ e1 Operacion

### W — omisiones de T4 a clasificar

- con_marca:5 → entidades: — | omisiones: —

