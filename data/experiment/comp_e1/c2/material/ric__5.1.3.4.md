# `ric::5.1.3.4` — Se informará una sola partida 3600000Y, reflejando la situación de la entidad

Grupos: omisiones. Estado final en la tanda 0: `cola_humana`.

## Texto

> *heredado:* Sección 5. Exigencia por riesgo operacional
> *heredado:* 5.1. Normas de procedimiento
> *heredado:* 5.1.3. Reducción de la exigencia para entidades financieras del Grupo 2 que pertenezcan a
> *heredado:* los Grupos "A", "B" y "C".
> *propio:* 5.1.3.4. Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación; el promedio de las exigencias por riesgo de crédito se calculará en esta Institución en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos.

## Omisiones leídas en T4 (M2)

sin_marca:12 [normativa; propio] «reflejando la situación de la entidad respecto de su calificación»

## Código A

- **op1 Operacion** «Informar partida 3600000Y» — Informar una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación (reducción de la exigencia por riesgo operacional para entidades del Grupo 2 que pertenezcan a los Grupos A, B y C). · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informará una sola partida 3600000Y»
- **ob1 Obligacion** «Informar una sola partida 3600000Y» — Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación»
- **ob2 Obligacion** «Cálculo del promedio de exigencias por riesgo de crédito» — El promedio de las exigencias por riesgo de crédito se calculará en esta Institución en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el promedio de las exigencias por riesgo de crédito se calculará en esta Institución en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob1 Obligacion —aplica_a→ Sujeto_rol_entidad_comprendida_reginf (mención «la entidad»)
- R: ob2 Obligacion —aplica_a→ Sujeto_bcra (mención «esta Institución»)

### A — omisiones de T4 a clasificar

- sin_marca:12 → entidades: ob1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código H

- **op1 Operacion** «Informar partida 3600000Y única» — Informar una sola partida 3600000Y que refleja la situación de la entidad respecto de su calificación (reducción de la exigencia por riesgo operacional, entidades del Grupo 2 pertenecientes a los Grupos A, B y C). · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación»
- **ob1 Obligacion** «Informar una sola partida 3600000Y» — Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación»
- **ob2 Obligacion** «Cálculo en el BCRA del promedio de exigencias por riesgo de crédito» — El promedio de las exigencias por riesgo de crédito se calcula en el BCRA (esta Institución) en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el promedio de las exigencias por riesgo de crédito se calculará en esta Institución en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob1 Obligacion —aplica_a→ Sujeto_rol_entidad_comprendida_reginf (mención «la entidad»)
- R: ob2 Obligacion —aplica_a→ Sujeto_bcra (mención «esta Institución»)

### H — omisiones de T4 a clasificar

- sin_marca:12 → entidades: op1 Operacion [exacta] solap 1.0 contiene; ob1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código K

- **e1 Obligacion** «Partida única 3600000Y — reducción exigencia riesgo operacional» — En el marco de la reducción de la exigencia por riesgo operacional para entidades del Grupo 2 de los Grupos A, B y C, se informará una sola partida 3600000Y que refleje la situación de la entidad respecto de su calificación. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación»
- **e2 Operacion** «Cálculo por el BCRA del promedio de exigencias por riesgo de crédito» — El BCRA calcula el promedio de las exigencias por riesgo de crédito en base a los datos de exigencia por riesgo de crédito informada en los períodos previos. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el promedio de las exigencias por riesgo de crédito se calculará en esta Institución»
- R: e1 Obligacion —aplica_a→ Sujeto_rol_entidad_comprendida_reginf (mención «la entidad»)
- R: Sujeto_bcra (mención «esta Institución») —ejecuta→ e2 Operacion

### K — omisiones de T4 a clasificar

- sin_marca:12 → entidades: e1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código N

- **e1 Operacion** «Informe partida 3600000Y» — Informe de una sola partida 3600000Y que refleja la situación de la entidad respecto de su calificación · props: `{"tipo": "presentación informativa"}` · tramo [exacta]: «Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación»
- **e2 Operacion** «Cálculo promedio exigencias riesgo crédito» — Cálculo del promedio de las exigencias por riesgo de crédito en la Institución sobre la base de los datos de exigencia por riesgo de crédito informados en períodos previos · props: `{"tipo": "cálculo"}` · tramo [exacta]: «el promedio de las exigencias por riesgo de crédito se calculará en esta Institución en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos»
- **e3 Obligacion** «Informar partida 3600000Y» — Deber de informar una sola partida 3600000Y · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informará una sola partida 3600000Y»
- **e4 Obligacion** «Calcular promedio exigencias riesgo crédito» — Deber de calcular en la Institución el promedio de las exigencias por riesgo de crédito · props: `{"tipo": "calculo"}` · tramo [exacta]: «el promedio de las exigencias por riesgo de crédito se calculará en esta Institución»
- R: e3 Obligacion —aplica_a→ Sujeto_rol_entidad_comprendida_reginf (mención «la entidad»)
- R: e4 Obligacion —aplica_a→ Sujeto (mención «esta Institución»)
- Omisión `meta_normativo` [exacta]: «reflejando la situación de la entidad respecto de su calificación» — Cláusula que describe el propósito o el contenido informativo de la partida, no una prescripción de conducta separada
- Omisión `meta_normativo` [exacta]: «en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos» — Cláusula que especifica la base de cálculo, no una prescripción de conducta separada

### N — omisiones de T4 a clasificar

- sin_marca:12 → entidades: e1 Operacion [exacta] solap 1.0 contiene | omisiones: om#0 meta_normativo [exacta] solap 1.0 contiene

## Código W

- **e1 Obligacion** «Partida única 3600000Y — calificación de la entidad» — En el marco de la reducción de la exigencia por riesgo operacional para entidades financieras del Grupo 2 de los Grupos A, B y C, se informará una sola partida 3600000Y que refleje la situación de la entidad respecto de su calificación. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación»
- **e2 Operacion** «Cálculo por el BCRA del promedio de exigencias por riesgo de crédito» — El promedio de las exigencias por riesgo de crédito lo calcula esta Institución (BCRA) con los datos de exigencia por riesgo de crédito informada en los períodos previos. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el promedio de las exigencias por riesgo de crédito se calculará en esta Institución en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos»
- R: Sujeto_bcra (mención «esta Institución») —ejecuta→ e2 Operacion
- R: e1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «entidades financieras»)

### W — omisiones de T4 a clasificar

- sin_marca:12 → entidades: e1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

