# `ric::3.1.7` — Exigencia de capital por riesgo de crédito de contraparte en operaciones con en-

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 3. Exigencia por riesgo de crédito
> *heredado:* 3.1. Normas de procedimiento.
> *propio:* 3.1.7. Exigencia de capital por riesgo de crédito de contraparte en operaciones con entidades de contraparte central Las exposiciones de las entidades financieras con entidades de contraparte central con el alcance establecido en el punto 4.3. de las normas sobre "Capitales mínimos de las entidades financieras" –determinadas conforme a dichas normas-, se consignarán en la partida 12500000 por cada ponderador que corresponda aplicar, siguiendo el modelo de información inserto en el punto 3.1.4..

## Omisiones leídas en T4 (M2)

sin_marca:13 [normativa, remisión pura; propio] «siguiendo el modelo de información inserto en el punto 3.1.4.»

## Código A

- **e1 Obligacion** «Consignación exposiciones con ECC en partida 12500000» — Las exposiciones de las entidades financieras con entidades de contraparte central, con el alcance del punto 4.3. de las normas de Capitales mínimos y determinadas conforme a ellas, se consignan en la partida 12500000 por cada ponderador aplicable, siguiendo el modelo de información del punto 3.1.4. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Las exposiciones de las entidades financieras con entidades de contraparte central con el alcance establecido en el punto 4.3. de las normas sobre "Capitales mínimos de las entidades financieras" –determinadas conforme a dichas normas-, se consignarán en la partida 12500000 por cada ponderador que corresponda aplicar, …»
- **e2 Operacion** «Exigencia de capital por riesgo de crédito de contraparte con ECC» — Exposiciones de entidades financieras con entidades de contraparte central, determinadas conforme a las normas de Capitales mínimos (punto 4.3.), consignadas por ponderador · props: `{"tipo": "otra"}` · tramo [exacta]: «Exigencia de capital por riesgo de crédito de contraparte en operaciones con entidades de contraparte central»
- R: e1 Obligacion —regula→ e2 Operacion
- R: e1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)

### A — omisiones de T4 a clasificar

- sin_marca:13 → entidades: e1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código H

- **o1 Obligacion** «Consignar exposiciones con ECC en partida 12500000» — Las exposiciones de las entidades financieras con entidades de contraparte central, con el alcance del punto 4.3. de Capitales mínimos y determinadas conforme a dichas normas, se consignan en la partida 12500000 por cada ponderador aplicable, según el modelo de información del punto 3.1.4. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Las exposiciones de las entidades financieras con entidades de contraparte central con el alcance establecido en el punto 4.3. de las normas sobre "Capitales mínimos de las entidades financieras" –determinadas conforme a dichas normas-, se consignarán en la partida 12500000 por cada ponderador que corresponda aplicar, …»
- **op1 Operacion** «Informar exposiciones con entidades de contraparte central» — Consignación en la partida 12500000 de las exposiciones por riesgo de crédito de contraparte con entidades de contraparte central, por cada ponderador aplicable · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Las exposiciones de las entidades financieras con entidades de contraparte central»
- R: o1 Obligacion —regula→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)

### H — omisiones de T4 a clasificar

- sin_marca:13 → entidades: o1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código K

- **e1 Obligacion** «Consignar exposiciones con CCP en partida 12500000» — Las exposiciones de las entidades financieras con entidades de contraparte central, con el alcance del punto 4.3. de las normas sobre Capitales mínimos y determinadas conforme a dichas normas, se consignarán en la partida 12500000 por cada ponderador que corresponda aplicar, siguiendo el modelo del punto 3.1.4. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «se consignarán en la partida 12500000 por cada ponderador que corresponda aplicar, siguiendo el modelo de información inserto en el punto 3.1.4.»
- **e2 Operacion** «Exposiciones con entidades de contraparte central» — Exposiciones de las entidades financieras con entidades de contraparte central, con el alcance del punto 4.3. de las normas sobre Capitales mínimos, determinadas conforme a dichas normas · props: `{"tipo": "exposicion por riesgo de crédito de contraparte"}` · tramo [exacta]: «Las exposiciones de las entidades financieras con entidades de contraparte central»
- **c1 Comunicacion** «Normas Capitales mínimos» —  · props: `{"codigo": "Capitales mínimos de las entidades financieras"}` · tramo [exacta]: «normas sobre "Capitales mínimos de las entidades financieras"»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: e1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: e1 Obligacion —regula→ e2 Operacion

### K — omisiones de T4 a clasificar

- sin_marca:13 → entidades: e1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código W

- **e1 Obligacion** «Consignar exposiciones con CCP en partida 12500000» — Las exposiciones de las entidades financieras con entidades de contraparte central, con el alcance del punto 4.3. de Capitales mínimos y determinadas conforme a dichas normas, se consignan en la partida 12500000 por cada ponderador que corresponda aplicar, siguiendo el modelo del punto 3.1.4. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «se consignarán en la partida 12500000 por cada ponderador que corresponda aplicar, siguiendo el modelo de información inserto en el punto 3.1.4.»
- **e2 Operacion** «Exposiciones con entidades de contraparte central» — Exposiciones de entidades financieras con entidades de contraparte central, con el alcance del punto 4.3. de las normas sobre Capitales mínimos, determinadas conforme a dichas normas · props: `{"tipo": "exposición por riesgo de crédito de contraparte"}` · tramo [exacta]: «Las exposiciones de las entidades financieras con entidades de contraparte central»
- **e3 Comunicacion** «Capitales mínimos de las entidades financieras» —  · props: `{"codigo": "Capitales mínimos de las entidades financieras"}` · tramo [exacta]: «normas sobre "Capitales mínimos de las entidades financieras"»
- R: e1 Obligacion —regula→ e2 Operacion
- R: e1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: to TextoOrdenado —referencia→ e3 Comunicacion

### W — omisiones de T4 a clasificar

- sin_marca:13 → entidades: e1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

