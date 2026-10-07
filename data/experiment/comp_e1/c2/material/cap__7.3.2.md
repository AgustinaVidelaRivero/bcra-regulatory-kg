# `cap::7.3.2` — El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses

Grupos: grupo_c. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 7. Capital mínimo por riesgo operacional.
> *heredado:* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en grupo 1 y grupo 2, conforme a lo previsto en la Sección 2.
> *heredado:* 7.3. Límite para las entidades del grupo 2.
> *heredado:* La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar:
> *propio:* 7.3.2. El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses –anteriores al mes a que corresponda la determinación de la exigencia– de la exigencia de capital mínimo por riesgo de crédito calculada según lo previsto en la Sección 2., expresada en moneda homogénea del mes anterior al que se efectúa el cálculo. El límite máximo establecido precedentemente se reducirá a 11% cuando la entidad financiera cuente con calificación 1, 2 o 3 conforme a la valoración otorgada por la SEFYC, en oportunidad de la última inspección efectuada, respecto de todos los siguientes aspectos: la entidad en su conjunto, sus sistemas informáticos y la labor de los responsables de la evaluación de sus sistemas de control interno. En los casos en que la entidad financiera cuente en todos los citados aspectos con calificación 1 o 2, el límite máximo disminuirá a 7%. A este efecto, se considerará la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación.

## Supuestos de la fase A de T4 (M1)

1. «grupo B (17 %)»
2. «calificación 1, 2 o 3 (11 %)»
3. «calificación 1 o 2 (7 %)»

## Código A

- **op1 Operacion** «Determinación exigencia capital mínimo por riesgo operacional» — Determinación de la exigencia de capital mínimo por riesgo operacional mediante la expresión del punto 7.2, para entidades del grupo 2. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2.»
- **r1 Restriccion** «Límite 17% grupo B — exigencia riesgo operacional» — La exigencia por riesgo operacional no podrá superar el 17% del promedio de los últimos 36 meses anteriores al mes de determinación de la exigencia de capital mínimo por riesgo de crédito (Sección 2), expresada en moneda homogénea del mes anterior al del cálculo, para entidades del grupo B. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses'] · tramo [exacta]: «no podrá superar: [...] El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses –anteriores al mes a que corresponda la determinación de la exigencia– de la exigencia de capital mínimo por riesgo de crédito calculada según lo previsto en la Sección 2.»
- **r2 Restriccion** «Límite 11% con calificación 1, 2 o 3 — exigencia riesgo operacional» — El límite máximo del 17% se reduce a 11% cuando la entidad financiera cuente con calificación 1, 2 o 3 otorgada por la SEFYC en la última inspección, respecto de todos los aspectos indicados. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['se reducirá a 11%'] · tramo [exacta]: «El límite máximo establecido precedentemente se reducirá a 11% cuando la entidad financiera cuente con calificación 1, 2 o 3»
- **c2 Condicion** «Calificación 1, 2 o 3 en todos los aspectos SEFYC» — Calificación 1, 2 o 3 según la SEFYC en la última inspección, respecto de todos los aspectos: la entidad en su conjunto, sus sistemas informáticos y la labor de los responsables de la evaluación de sus sistemas de control interno. Condiciona el límite del 11%. · tramo [exacta]: «cuente con calificación 1, 2 o 3 conforme a la valoración otorgada por la SEFYC, en oportunidad de la última inspección efectuada, respecto de todos los siguientes aspectos: la entidad en su conjunto, sus sistemas informáticos y la labor de los responsables de la evaluación de sus sistemas de control interno.»
- **r3 Restriccion** «Límite 7% con calificación 1 o 2 — exigencia riesgo operacional» — El límite máximo disminuye a 7% cuando la entidad financiera cuente en todos los aspectos citados con calificación 1 o 2. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['el límite máximo disminuirá a 7%'] · tramo [exacta]: «el límite máximo disminuirá a 7%»
- **c3 Condicion** «Calificación 1 o 2 en todos los aspectos» — La entidad financiera cuenta en todos los aspectos citados con calificación 1 o 2. Condiciona el límite del 7%. · tramo [exacta]: «En los casos en que la entidad financiera cuente en todos los citados aspectos con calificación 1 o 2»
- **o1 Obligacion** «Usar última calificación informada — tercer mes posterior a notificación» — Para aplicar los límites, se considera la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación. · props: `{"tipo": "calculo", "umbrales": [{"tramo": "al tercer mes siguiente a aquel en que tenga lugar la\nnotificación", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['al tercer mes siguiente a aquel en que tenga lugar la notificación'] · tramo [exacta]: «se considerará la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación»
- R: r1 Restriccion —limita→ op1 Operacion
- R: r2 Restriccion —limita→ op1 Operacion
- R: r3 Restriccion —limita→ op1 Operacion
- R: c2 Condicion —condicion_de→ r2 Restriccion
- R: c3 Condicion —condicion_de→ r3 Restriccion
- R: r1 Restriccion —aplica_a→ Sujeto (mención «entidades del grupo B»)
- R: r2 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: r3 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: o1 Obligacion —regula→ op1 Operacion

### A — supuestos a clasificar

- 1. «grupo B (17 %)» → candidatos: r1 Restriccion (1.00), op1 Operacion (0.50), r2 Restriccion (0.50)
- 2. «calificación 1, 2 o 3 (11 %)» → candidatos: c2 Condicion (1.00), r2 Restriccion (1.00), c3 Condicion (0.60), r3 Restriccion (0.60)
- 3. «calificación 1 o 2 (7 %)» → candidatos: c3 Condicion (1.00), r3 Restriccion (1.00), c2 Condicion (0.75), r2 Restriccion (0.75)

## Código H

- **op1 Operacion** «Exigencia de capital mínimo por riesgo operacional» — Determinación de la exigencia de capital mínimo por riesgo operacional mediante la expresión del punto 7.2, para entidades del grupo 2. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2.»
- **r1 Restriccion** «Tope 17% promedio 36 meses riesgo de crédito — grupo B» — La exigencia por riesgo operacional no podrá superar el 17% del promedio de los últimos 36 meses, anteriores al mes de la determinación, de la exigencia de capital mínimo por riesgo de crédito (Sección 2), en moneda homogénea del mes anterior al del cálculo, para entidades del grupo B. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses'] · tramo [exacta]: «no podrá superar: [...] El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses –anteriores al mes a que corresponda la determinación de la exigencia– de la exigencia de capital mínimo por riesgo de crédito calculada según lo previsto en la Sección 2., expresada en moneda homogénea del mes anter…»
- **r2 Restriccion** «Tope reducido 11% — calificación 1, 2 o 3» — El límite máximo del 17% se reduce a 11% cuando la entidad financiera cuente con calificación 1, 2 o 3 de la SEFYC en la última inspección, en todos los aspectos indicados. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['se reducirá a 11%'] · tramo [exacta]: «El límite máximo establecido precedentemente se reducirá a 11%»
- **c2 Condicion** «Calificación 1, 2 o 3 en todos los aspectos» — Calificación 1, 2 o 3 otorgada por la SEFYC en la última inspección en todos los aspectos: entidad en su conjunto, sistemas informáticos y labor de los responsables de evaluar el control interno. Se considera la última calificación informada para el cálculo de la exigencia a integrar al tercer mes siguiente a la notificación. · tramo [exacta]: «cuente con calificación 1, 2 o 3 conforme a la valoración otorgada por la SEFYC, en oportunidad de la última inspección efectuada, respecto de todos los siguientes aspectos: la entidad en su conjunto, sus sistemas informáticos y la labor de los responsables de la evaluación de sus sistemas de control interno»
- **r3 Restriccion** «Tope reducido 7% — calificación 1 o 2» — El límite máximo disminuye a 7% cuando la entidad financiera cuente en todos los aspectos citados con calificación 1 o 2. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['disminuirá a 7%'] · tramo [exacta]: «el límite máximo disminuirá a 7%»
- **c3 Condicion** «Calificación 1 o 2 en todos los aspectos» — Calificación 1 o 2 en todos los aspectos citados (entidad en su conjunto, sistemas informáticos, labor de los responsables del control interno). Se considera la última calificación informada para el cálculo de la exigencia a integrar al tercer mes siguiente a la notificación. · tramo [exacta]: «cuente en todos los citados aspectos con calificación 1 o 2»
- R: r1 Restriccion —limita→ op1 Operacion
- R: r2 Restriccion —limita→ op1 Operacion
- R: r3 Restriccion —limita→ op1 Operacion
- R: c2 Condicion —condicion_de→ r2 Restriccion
- R: c3 Condicion —condicion_de→ r3 Restriccion
- R: r1 Restriccion —aplica_a→ Sujeto (mención «entidades del grupo B»)
- R: r2 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: r3 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)

### H — supuestos a clasificar

- 1. «grupo B (17 %)» → candidatos: r1 Restriccion (1.00), op1 Operacion (0.50), r2 Restriccion (0.50)
- 2. «calificación 1, 2 o 3 (11 %)» → candidatos: r2 Restriccion (1.00), c2 Condicion (0.80), c3 Condicion (0.60), r3 Restriccion (0.60)
- 3. «calificación 1 o 2 (7 %)» → candidatos: r3 Restriccion (1.00), c2 Condicion (0.75), c3 Condicion (0.75), r2 Restriccion (0.75)

## Código K

- **op1 Operacion** «Exigencia de capital por riesgo operacional» — Determinación de la exigencia de capital mínimo por riesgo operacional según la expresión del punto 7.2. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2.»
- **r1 Restriccion** «Tope 17% grupo B — exigencia riesgo operacional» — Para entidades del grupo B, la exigencia por riesgo operacional no podrá superar el 17% del promedio de los últimos 36 meses (anteriores al mes de determinación) de la exigencia por riesgo de crédito calculada según la Sección 2, expresada en moneda homogénea del mes anterior al cálculo. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['no podrá superar: […] El 17%', 'promedio de los últimos 36 meses'] · tramo [exacta]: «La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar: […] El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses»
- **r2 Restriccion** «Tope reducido 11% — calificación 1, 2 o 3» — El límite del 17% se reduce a 11% cuando la entidad cuenta con calificación 1, 2 o 3 de la SEFyC en la última inspección en todos los aspectos señalados. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['se reducirá a 11%'] · tramo [exacta]: «El límite máximo establecido precedentemente se reducirá a 11%»
- **c1 Condicion** «Calificación SEFyC 1, 2 o 3 en todos los aspectos» — La entidad cuenta con calificación 1, 2 o 3 de la SEFyC en la última inspección respecto de la entidad en su conjunto, sus sistemas informáticos y la labor de los responsables de evaluar el control interno. · tramo [exacta]: «cuando la entidad financiera cuente con calificación 1, 2 o 3 conforme a la valoración otorgada por la SEFYC, en oportunidad de la última inspección efectuada, respecto de todos los siguientes aspectos: la entidad en su conjunto, sus sistemas informáticos y la labor de los responsables de la evaluación de sus sistemas …»
- **r3 Restriccion** «Tope reducido 7% — calificación 1 o 2» — El límite máximo disminuye a 7% cuando la entidad cuenta con calificación 1 o 2 en todos los aspectos citados. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['disminuirá a 7%'] · tramo [exacta]: «el límite máximo disminuirá a 7%»
- **c2 Condicion** «Calificación 1 o 2 en todos los aspectos» — La entidad cuenta con calificación 1 o 2 en todos los aspectos citados. · tramo [exacta]: «En los casos en que la entidad financiera cuente en todos los citados aspectos con calificación 1 o 2»
- **o1 Obligacion** «Última calificación aplicable al tercer mes siguiente» — Se considera la última calificación informada para el cálculo de la exigencia a integrar al tercer mes siguiente al de la notificación. · props: `{"tipo": "calculo", "umbrales": [{"tramo": "al tercer mes siguiente a aquel en que tenga lugar la\nnotificación", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['al tercer mes siguiente a aquel en que tenga lugar la notificación'] · tramo [exacta]: «se considerará la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación»
- R: r1 Restriccion —limita→ op1 Operacion
- R: r2 Restriccion —limita→ op1 Operacion
- R: r3 Restriccion —limita→ op1 Operacion
- R: c1 Condicion —condicion_de→ r2 Restriccion
- R: c2 Condicion —condicion_de→ r3 Restriccion
- R: o1 Obligacion —regula→ op1 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto (mención «entidades del grupo B»)
- R: r2 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: r3 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)

### K — supuestos a clasificar

- 1. «grupo B (17 %)» → candidatos: r1 Restriccion (1.00), r2 Restriccion (0.50)
- 2. «calificación 1, 2 o 3 (11 %)» → candidatos: r2 Restriccion (1.00), c1 Condicion (0.80), c2 Condicion (0.60), r3 Restriccion (0.60)
- 3. «calificación 1 o 2 (7 %)» → candidatos: r3 Restriccion (1.00), c1 Condicion (0.75), c2 Condicion (0.75), r2 Restriccion (0.75)

## Código W

- **op1 Operacion** «Exigencia por riesgo operacional — grupo B» — Exigencia de capital mínimo por riesgo operacional determinada según la expresión del punto 7.2, para entidades del grupo B · props: `{"tipo": "determinación de exigencia de capital mínimo"}` · tramo [exacta]: «La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2.»
- **r1 Restriccion** «Tope 17% — exigencia riesgo operacional grupo B» — La exigencia por riesgo operacional de las entidades del grupo B no podrá superar el 17% del promedio de los últimos 36 meses (anteriores al mes de determinación) de la exigencia por riesgo de crédito calculada según la Sección 2, expresada en moneda homogénea del mes anterior al cálculo. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['no podrá superar: […] El 17%', 'del promedio de los últimos 36 meses'] · tramo [exacta]: «La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar: […] El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses»
- **r2 Restriccion** «Tope 11% — calificación 1, 2 o 3» — El límite máximo del 17% se reduce a 11% cuando la entidad financiera cuenta con calificación 1, 2 o 3 de la SEFYC en todos los aspectos. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['se reducirá a 11%'] · tramo [exacta]: «El límite máximo establecido precedentemente se reducirá a 11%»
- **c1 Condicion** «Calificación SEFYC 1, 2 o 3 en todos aspectos» — La entidad cuenta con calificación 1, 2 o 3 de la SEFYC en la última inspección respecto de la entidad en su conjunto, sus sistemas informáticos y la labor de los responsables de la evaluación del control interno. · tramo [exacta]: «cuando la entidad financiera cuente con calificación 1, 2 o 3 conforme a la valoración otorgada por la SEFYC, en oportunidad de la última inspección efectuada, respecto de todos los siguientes aspectos»
- **r3 Restriccion** «Tope 7% — calificación 1 o 2» — El límite máximo disminuye a 7% cuando la entidad financiera cuenta en todos los aspectos citados con calificación 1 o 2. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['disminuirá a 7%'] · tramo [exacta]: «el límite máximo disminuirá a 7%»
- **c2 Condicion** «Calificación 1 o 2 en todos aspectos» — La entidad cuenta con calificación 1 o 2 en todos los aspectos citados. · tramo [exacta]: «En los casos en que la entidad financiera cuente en todos los citados aspectos con calificación 1 o 2»
- **o1 Obligacion** «Última calificación informada — aplicación al tercer mes» — Para aplicar los límites reducidos se considera la última calificación informada en el cálculo de la exigencia a integrar al tercer mes siguiente al de la notificación. · props: `{"tipo": "calculo", "umbrales": [{"tramo": "al tercer mes siguiente a aquel en que tenga lugar la\nnotificación", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['al tercer mes siguiente a aquel en que tenga lugar la notificación'] · tramo [exacta]: «se considerará la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación»
- R: r1 Restriccion —limita→ op1 Operacion
- R: r2 Restriccion —limita→ op1 Operacion
- R: r3 Restriccion —limita→ op1 Operacion
- R: c1 Condicion —condicion_de→ r2 Restriccion
- R: c2 Condicion —condicion_de→ r3 Restriccion
- R: r1 Restriccion —aplica_a→ Sujeto (mención «entidades del grupo B»)
- R: r2 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: r3 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: o1 Obligacion —regula→ op1 Operacion

### W — supuestos a clasificar

- 1. «grupo B (17 %)» → candidatos: r1 Restriccion (1.00), op1 Operacion (0.50), r2 Restriccion (0.50)
- 2. «calificación 1, 2 o 3 (11 %)» → candidatos: r2 Restriccion (1.00), c1 Condicion (0.80), c2 Condicion (0.60), r3 Restriccion (0.60)
- 3. «calificación 1 o 2 (7 %)» → candidatos: r3 Restriccion (1.00), c1 Condicion (0.75), c2 Condicion (0.75), r2 Restriccion (0.75)

