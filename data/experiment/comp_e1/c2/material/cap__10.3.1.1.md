# `cap::10.3.1.1` — Se asignarán las calificaciones de las ECAI admisibles a los ponderadores de

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 10. Agentes de calificación externa (ECAI).
> *heredado:* 10.3. Consideraciones para su implementación.
> *heredado:* 10.3.1. Proceso de asignación de calificaciones (mapping).
> *propio:* 10.3.1.1. Se asignarán las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4.; es decir, las entidades financieras deberán establecer qué calificaciones o categorías de evaluación corresponden a esos ponderadores de riesgo. El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en esas calificaciones. Además, deberá abarcar todos los ponderadores de riesgo previstos en esos puntos.

## Omisiones leídas en T4 (M2)

con_marca:10 [normativa; propio] «es decir, las entidades financieras deberán establecer qué calificaciones o categorías de evaluación corresponden a esos ponderadores de riesgo»

## Código A

- **op1 Operacion** «Asignación (mapping) de calificaciones ECAI a ponderadores de riesgo» — Proceso de asignación (mapping) de las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «Se asignarán las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4.»
- **ob1 Obligacion** «Establecer calificaciones ECAI correspondientes a cada ponderador» — Las entidades financieras deben establecer qué calificaciones o categorías de evaluación de las ECAI admisibles corresponden a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «las entidades financieras deberán establecer qué calificaciones o categorías de evaluación corresponden a esos ponderadores de riesgo»
- **ob2 Obligacion** «Mapping objetivo y con distribución coherente» — El proceso de asignación (mapping) debe ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en las calificaciones. · props: `{"tipo": "otra"}` · tramo [exacta]: «El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en esas calificaciones.»
- **ob3 Obligacion** «Mapping debe abarcar todos los ponderadores de riesgo» — El proceso de asignación (mapping) debe abarcar todos los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "otra"}` · tramo [exacta]: «Además, deberá abarcar todos los ponderadores de riesgo previstos en esos puntos.»
- R: ob1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion

### A — omisiones de T4 a clasificar

- con_marca:10 → entidades: ob1 Obligacion [exacta] solap 0.92 contenido_en | omisiones: —

## Código H

- **op1 Operacion** «Asignación (mapping) de calificaciones ECAI a ponderadores de riesgo» — Proceso de asignación (mapping) de las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «Se asignarán las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4.»
- **ob1 Obligacion** «Establecer correspondencia calificaciones-ponderadores de riesgo» — Las entidades financieras deben establecer qué calificaciones o categorías de evaluación de las ECAI admisibles corresponden a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «las entidades financieras deberán establecer qué calificaciones o categorías de evaluación corresponden a esos ponderadores de riesgo»
- **ob2 Obligacion** «Mapping objetivo y con distribución coherente de ponderadores» — El proceso de asignación (mapping) debe ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en las calificaciones. · props: `{"tipo": "otra"}` · tramo [exacta]: «El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en esas calificaciones.»
- **ob3 Obligacion** «Mapping abarca todos los ponderadores de riesgo» — El proceso de asignación (mapping) debe abarcar todos los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "otra"}` · tramo [exacta]: «Además, deberá abarcar todos los ponderadores de riesgo previstos en esos puntos.»
- R: ob1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion
- R: Sujeto_entidad_financiera (mención «las entidades financieras») —ejecuta→ op1 Operacion

### H — omisiones de T4 a clasificar

- con_marca:10 → entidades: ob1 Obligacion [exacta] solap 0.92 contenido_en | omisiones: —

## Código K

- **op1 Operacion** «Mapping de calificaciones ECAI a ponderadores» — Asignación de las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «Proceso de asignación de calificaciones (mapping).»
- **o1 Obligacion** «Establecer correspondencia calificaciones–ponderadores de riesgo» — Las entidades financieras deberán asignar las calificaciones de las ECAI admisibles a los ponderadores de riesgo del primer párrafo del punto 2.5.4., estableciendo qué calificaciones o categorías de evaluación corresponden a cada ponderador. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «las entidades financieras deberán establecer qué calificaciones o categorías de evaluación corresponden a esos ponderadores de riesgo»
- **o2 Obligacion** «Mapping objetivo y coherente con riesgo de crédito» — El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en las calificaciones. · props: `{"tipo": "otra"}` · tramo [exacta]: «El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en esas calificaciones»
- **o3 Obligacion** «Mapping debe abarcar todos los ponderadores» — El proceso de asignación deberá abarcar todos los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "otra"}` · tramo [exacta]: «deberá abarcar todos los ponderadores de riesgo previstos en esos puntos»
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: Sujeto_entidad_financiera (mención «las entidades financieras») —ejecuta→ op1 Operacion

### K — omisiones de T4 a clasificar

- con_marca:10 → entidades: o1 Obligacion [exacta] solap 0.92 contenido_en | omisiones: —

## Código W

- **op1 Operacion** «Asignación de calificaciones ECAI a ponderadores (mapping)» — Asignación de las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "asignación de calificaciones"}` · tramo [exacta]: «Proceso de asignación de calificaciones (mapping).»
- **o1 Obligacion** «Establecer correspondencia calificaciones-ponderadores de riesgo» — Las entidades financieras deberán asignar las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4., estableciendo qué calificaciones o categorías de evaluación corresponden a cada ponderador. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «las entidades financieras deberán establecer qué calificaciones o categorías de evaluación corresponden a esos ponderadores de riesgo»
- **o2 Obligacion** «Objetividad y coherencia del mapping» — El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en esas calificaciones. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en esas calificaciones»
- **o3 Obligacion** «Cobertura de todos los ponderadores en mapping» — El proceso de asignación (mapping) deberá abarcar todos los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «deberá abarcar todos los ponderadores de riesgo previstos en esos puntos»
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: Sujeto_entidad_financiera (mención «las entidades financieras») —ejecuta→ op1 Operacion

### W — omisiones de T4 a clasificar

- con_marca:10 → entidades: o1 Obligacion [exacta] solap 0.92 contenido_en | omisiones: —

