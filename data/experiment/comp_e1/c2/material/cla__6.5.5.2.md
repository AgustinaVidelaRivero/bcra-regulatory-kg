# `cla::6.5.5.2` — Incurra en atrasos superiores a un año, cuente con refinanciación del capital y

Grupos: grupo_c. Estado final en la tanda 0: `aceptado_tras_reintento`.

## Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.5. Irrecuperable.
> *heredado:* Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de circunstancias futuras, su incobrabilidad es evidente al momento del análisis. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *heredado:* Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el motivo (entre ellos por no contar con legajo o por no haber proporcionado información confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente, con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, por un período de hasta 540 días contados a partir de la apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales de cobro, según corresponda, no hubiesen presentado la documentación que permita realizarla, siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos. Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad".
> *propio:* 6.5.5.2. Incurra en atrasos superiores a un año, cuente con refinanciación del capital y sus intereses y con financiación de pérdidas de explotación. A este fin, el cómputo de los plazos no se interrumpirá por el otorgamiento de renovaciones cuando previamente no se haya producido la cancelación efectiva de las obligaciones vencidas, es decir sin recurrir a financiación directa o indirecta de la entidad. Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, podrá reclasificarse al deudor en el nivel inmediato superior si, además, se observan las otras condiciones previstas en el citado nivel. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente.

## Supuestos de la fase A de T4 (M1)

1. «sin cancelación efectiva previa»
2. «pago del 15 %»
3. «financiación adicional sin cancelar»

## Código A

- Rechazos del validador r2: relacion:firma_invalida
- **c1 Condicion** «Indicador: atrasos >1 año con refinanciación y financiación de pérdidas» — Indicador de la categoría Irrecuperable (norma del encabezado de 6.5.5): el cliente incurre en atrasos superiores a un año, cuenta con refinanciación del capital y sus intereses y con financiación de pérdidas de explotación. · umbral: ['atrasos superiores a un año'] · tramo [exacta]: «Incurra en atrasos superiores a un año, cuente con refinanciación del capital y sus intereses y con financiación de pérdidas de explotación»
- **o1 Operacion** «Cómputo de plazos de atraso con renovaciones» — Cómputo de los plazos de atraso a los fines del indicador, en caso de renovaciones sin cancelación efectiva previa de las obligaciones vencidas. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el cómputo de los plazos no se interrumpirá por el otorgamiento de renovaciones»
- **r1 Restriccion** «No interrupción del cómputo por renovaciones» — El cómputo de los plazos de atraso no se interrumpe por renovaciones cuando previamente no hubo cancelación efectiva de las obligaciones vencidas, es decir sin recurrir a financiación directa o indirecta de la entidad. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «el cómputo de los plazos no se interrumpirá por el otorgamiento de renovaciones cuando previamente no se haya producido la cancelación efectiva de las obligaciones vencidas, es decir sin recurrir a financiación directa o indirecta de la entidad»
- **p1 Potestad** «Reclasificar al nivel inmediato superior» — Facultad de reclasificar al deudor en el nivel inmediato superior cuando se cumplió el pago del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, y se observan las otras condiciones del nivel. · tramo [exacta]: «podrá reclasificarse al deudor en el nivel inmediato superior si, además, se observan las otras condiciones previstas en el citado nivel»
- **c2 Condicion** «Pago 15% refinanciado sin atrasos >31 días» — Se cumplió el pago, sin atrasos superiores a 31 días, del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados. · umbral: ['sin haber incurrido en atrasos superiores a los 31 días', 'del 15 % de las obligaciones refinanciadas'] · tramo [exacta]: «Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados»
- **ob1 Obligacion** «Permanencia mínima 180 días en Irrecuperable» — El deudor clasificado en esta categoría que haya refinanciado su deuda (aun habiendo cancelado el porcentaje del párrafo precedente) y recibido crédito adicional en los términos del punto 2.2.5. de las normas de Previsiones mínimas, sin que esa financiación adicional se hubiese cancelado, debe permanecer en la categoría al menos 180 días desde el crédito adicional o el acuerdo de refinanciación, l… · props: `{"tipo": "otra"}` · umbral: ['por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional…'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente»
- **c3 Condicion** «Refinanció y recibió crédito adicional no cancelado» — Supuesto de la permanencia mínima: el deudor refinanció su deuda y recibió crédito adicional (punto 2.2.5. de Previsiones mínimas) que no fue cancelado. · tramo [exacta]: «haya refinanciado su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese si…»
- R: r1 Restriccion —limita→ o1 Operacion
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ ob1 Obligacion
- R: ob1 Obligacion —aplica_a→ Sujeto_deudor (mención «El deudor»)

### A — supuestos a clasificar

- 1. «sin cancelación efectiva previa» → candidatos: o1 Operacion (1.00), r1 Restriccion (0.67)
- 2. «pago del 15 %» → candidatos: c2 Condicion (1.00), p1 Potestad (1.00)
- 3. «financiación adicional sin cancelar» → candidatos: c3 Condicion (0.67), ob1 Obligacion (0.67), c1 Condicion (0.33), r1 Restriccion (0.33)

## Código H

- **op1 Operacion** «Clasificación en categoría Irrecuperable» — Clasificación del cliente en la categoría Irrecuperable (6.5.5) cuando se verifica el indicador de atrasos superiores a un año con refinanciación y financiación de pérdidas de explotación · props: `{"tipo": "clasificacion_de_deudor"}` · tramo [exacta]: «Incurra en atrasos superiores a un año, cuente con refinanciación del capital y sus intereses y con financiación de pérdidas de explotación»
- **c1 Condicion** «Atrasos > 1 año con refinanciación y financiación de pérdidas» — Indicador de irrecuperabilidad: el cliente incurre en atrasos superiores a un año, cuenta con refinanciación del capital y sus intereses y con financiación de pérdidas de explotación · umbral: ['atrasos superiores a un año'] · tramo [exacta]: «Incurra en atrasos superiores a un año, cuente con refinanciación del capital y sus intereses y con financiación de pérdidas de explotación»
- **d1 Definicion** «Cómputo de plazos no interrumpido por renovaciones» — A los fines del indicador, el cómputo de los plazos de atraso no se interrumpe por renovaciones cuando previamente no hubo cancelación efectiva de las obligaciones vencidas, es decir sin recurrir a financiación directa o indirecta de la entidad · props: `{"termino": "cómputo de los plazos"}` · tramo [exacta]: «el cómputo de los plazos no se interrumpirá por el otorgamiento de renovaciones cuando previamente no se haya producido la cancelación efectiva de las obligaciones vencidas, es decir sin recurrir a financiación directa o indirecta de la entidad»
- **p1 Potestad** «Reclasificación al nivel inmediato superior» — Podrá reclasificarse al deudor en el nivel inmediato superior si se cumplió con el pago del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, y se observan las otras condiciones del nivel · tramo [exacta]: «podrá reclasificarse al deudor en el nivel inmediato superior si, además, se observan las otras condiciones previstas en el citado nivel»
- **c2 Condicion** «Pago del 15 % refinanciado e intereses sin atrasos > 31 días» — Se haya pagado al menos el 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, sin atrasos superiores a 31 días · umbral: ['atrasos superiores a los 31 días', '15 % de las obligaciones refinanciadas'] · tramo [exacta]: «Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados»
- **r1 Restriccion** «Permanencia mínima 180 días en Irrecuperable» — El deudor clasificado en esta categoría que refinanció su deuda y recibió crédito adicional (punto 2.2.5. de Previsiones mínimas) no cancelado, aun habiendo cancelado el porcentaje referido, debe permanecer en la categoría al menos 180 días desde el crédito adicional o el acuerdo de refinanciación, el más reciente · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional…'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente»
- **c3 Condicion** «Refinanció y recibió crédito adicional no cancelado» — El deudor clasificado en Irrecuperable refinanció su deuda y recibió crédito adicional en los términos del punto 2.2.5. y esa financiación adicional no fue cancelada · tramo [exacta]: «haya refinanciado su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese si…»
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ r1 Restriccion
- R: p1 Potestad —aplica_a→ Sujeto_deudor (mención «al deudor»)
- R: r1 Restriccion —aplica_a→ Sujeto_deudor (mención «El deudor»)
- R: r1 Restriccion —limita→ op1 Operacion

### H — supuestos a clasificar

- 1. «sin cancelación efectiva previa» → candidatos: d1 Definicion (0.67)
- 2. «pago del 15 %» → candidatos: c2 Condicion (1.00), p1 Potestad (1.00)
- 3. «financiación adicional sin cancelar» → candidatos: c3 Condicion (0.67), c1 Condicion (0.33), d1 Definicion (0.33), op1 Operacion (0.33)

## Código K

- **op1 Operacion** «Clasificación en Irrecuperable — cartera comercial» — Clasificación de clientes de la cartera comercial en la categoría Irrecuperable · props: `{"tipo": "clasificacion de deudor"}` · tramo [exacta]: «6.5.5. Irrecuperable.»
- **c1 Condicion** «Atrasos superiores a un año — indicador Irrecuperable» — Indicador de la categoría Irrecuperable: el cliente incurre en atrasos superiores a un año (concurrente con los demás supuestos del ítem) · umbral: ['atrasos superiores a un año'] · tramo [exacta]: «Entre los indicadores que pueden reflejar esta situación se destacan que el cliente: […] Incurra en atrasos superiores a un año»
- **c2 Condicion** «Refinanciación de capital e intereses — indicador Irrecuperable» — Indicador de la categoría Irrecuperable: el cliente cuenta con refinanciación del capital y sus intereses · tramo [exacta]: «cuente con refinanciación del capital y sus intereses»
- **c3 Condicion** «Financiación de pérdidas de explotación — indicador Irrecuperable» — Indicador de la categoría Irrecuperable: el cliente cuenta con financiación de pérdidas de explotación · tramo [exacta]: «con financiación de pérdidas de explotación»
- **o1 Obligacion** «Cómputo de plazos no interrumpido por renovaciones» — El cómputo de los plazos de atraso no se interrumpe por renovaciones si antes no hubo cancelación efectiva de las obligaciones vencidas, es decir sin recurrir a financiación directa o indirecta de la entidad · props: `{"tipo": "calculo"}` · tramo [exacta]: «el cómputo de los plazos no se interrumpirá por el otorgamiento de renovaciones cuando previamente no se haya producido la cancelación efectiva de las obligaciones vencidas»
- **op2 Operacion** «Reclasificación al nivel inmediato superior desde Irrecuperable» — Reclasificación del deudor refinanciado desde Irrecuperable al nivel inmediato superior · props: `{"tipo": "reclasificacion de deudor"}` · tramo [exacta]: «podrá reclasificarse al deudor en el nivel inmediato superior»
- **p1 Potestad** «Reclasificación ascendente de deudor refinanciado» — Puede reclasificarse al deudor en el nivel inmediato superior cuando haya pagado el 15 % de lo refinanciado y la totalidad de intereses devengados sin atrasos superiores a 31 días y se observen las demás condiciones de ese nivel · tramo [exacta]: «podrá reclasificarse al deudor en el nivel inmediato superior»
- **c4 Condicion** «Pago del 15 % de obligaciones refinanciadas» — Haber pagado al menos el 15 % de las obligaciones refinanciadas sin atrasos superiores a 31 días · props: `{"umbrales": [{"tramo": "al menos se haya cumplido con el pago", "comparacion": "minimo_inclusivo", "base": "se haya cumplido con el pago", "regla_comparacion": "limite_relativo:compuesta:al_menos", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['al menos se haya cumplido con el pago', 'sin haber incurrido en atrasos superiores a los 31 días', 'del 15 % de las obligaciones refinanciadas'] · tramo [exacta]: «Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 15 % de las obligaciones refinanciadas»
- **c5 Condicion** «Pago de la totalidad de intereses devengados» — Haber pagado la totalidad de los intereses devengados · tramo [exacta]: «la totalidad de los intereses devengados»
- **c6 Condicion** «Otras condiciones del nivel superior observadas» — Que se observen las otras condiciones previstas para el nivel inmediato superior · tramo [exacta]: «si, además, se observan las otras condiciones previstas en el citado nivel»
- **r1 Restriccion** «Permanencia mínima 180 días en Irrecuperable» — El deudor irrecuperable que refinanció y recibió crédito adicional (punto 2.2.5 de Previsiones mínimas) no cancelado debe permanecer en la categoría al menos 180 días desde el crédito adicional o el acuerdo de refinanciación, lo más reciente, aun habiendo cancelado el 15 % · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional…'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días»
- **c7 Condicion** «Deuda refinanciada y crédito adicional recibido» — El deudor clasificado en Irrecuperable refinanció su deuda · tramo [exacta]: «haya refinanciado su deuda»
- **c8 Condicion** «Crédito adicional recibido según punto 2.2.5» — Recibió crédito adicional en los términos del punto 2.2.5 de Previsiones mínimas · tramo [exacta]: «recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad"»
- **c9 Condicion** «Financiación adicional no cancelada» — La financiación adicional no fue cancelada · tramo [exacta]: «en la medida en que dicha financiación adicional no hubiese sido cancelada»
- **com1 Comunicacion** «Previsiones mínimas por riesgo de incobrabilidad» —  · props: `{"codigo": "Previsiones mínimas por riesgo de incobrabilidad"}` · tramo [exacta]: «"Previsiones mínimas por riesgo de incobrabilidad"»
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: c2 Condicion —condicion_de→ op1 Operacion
- R: c3 Condicion —condicion_de→ op1 Operacion
- R: c4 Condicion —condicion_de→ p1 Potestad
- R: c5 Condicion —condicion_de→ p1 Potestad
- R: c6 Condicion —condicion_de→ p1 Potestad
- R: c7 Condicion —condicion_de→ r1 Restriccion
- R: c8 Condicion —condicion_de→ r1 Restriccion
- R: c9 Condicion —condicion_de→ r1 Restriccion
- R: r1 Restriccion —limita→ op2 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto_deudor (mención «El deudor»)
- R: to TextoOrdenado —referencia→ com1 Comunicacion
- Omisión `relacion_sin_predicado` [exacta]: «podrá reclasificarse al deudor en el nivel inmediato superior» — Potestad → Operacion habilitada; no hay predicado

### K — supuestos a clasificar

- 1. «sin cancelación efectiva previa» → candidatos: o1 Obligacion (0.67)
- 2. «pago del 15 %» → candidatos: c4 Condicion (1.00), c5 Condicion (0.50), p1 Potestad (0.50), r1 Restriccion (0.50)
- 3. «financiación adicional sin cancelar» → candidatos: c9 Condicion (0.67), c3 Condicion (0.33), c7 Condicion (0.33), c8 Condicion (0.33)

## Código N

- **e1 Operacion** «Incurrir en atrasos superiores a un año» — El cliente incurre en atrasos superiores a un año en el pago de sus obligaciones · props: `{"tipo": "incumplimiento de obligación"}` · tramo [exacta]: «Incurra en atrasos superiores a un año»
- **e2 Operacion** «Refinanciación del capital e intereses» — El cliente cuenta con refinanciación del capital y sus intereses · props: `{"tipo": "refinanciación"}` · tramo [exacta]: «cuente con refinanciación del capital y sus intereses»
- **e3 Operacion** «Financiación de pérdidas de explotación» — El cliente cuenta con financiación de pérdidas de explotación · props: `{"tipo": "financiación"}` · tramo [exacta]: «financiación de pérdidas de explotación»
- **e4 Condicion** «Cómputo de plazos sin interrupción por renovaciones» — El cómputo de los plazos de atraso no se interrumpe por renovaciones si no ha habido cancelación efectiva de obligaciones vencidas sin financiación directa o indirecta · tramo [exacta]: «el cómputo de los plazos no se interrumpirá por el otorgamiento de renovaciones cuando previamente no se haya producido la cancelación efectiva de las obligaciones vencidas»
- **e5 Excepcion** «Reclasificación por pago del 15% de obligaciones refinanciadas» — Excepción a la clasificación en categoría Irrecuperable: el deudor puede reclasificarse al nivel superior si ha pagado sin atrasos mayores a 31 días el 15% de obligaciones refinanciadas y la totalidad de intereses · umbral: ['atrasos superiores a los 31 días', '15 % de las obligaciones refinanciadas'] · tramo [exacta]: «Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, podrá reclasificarse al deudor en el nivel inmediato superior»
- **e6 Condicion** «Observancia de otras condiciones del nivel superior» — Para la reclasificación, además del pago del 15%, deben observarse las otras condiciones previstas en el nivel inmediato superior · tramo [exacta]: «si, además, se observan las otras condiciones previstas en el citado nivel»
- **e7 Restriccion** «Permanencia mínima 180 días con crédito adicional» — El deudor que ha refinanciado su deuda y recibido crédito adicional debe permanecer en la categoría Irrecuperable por lo menos 180 días desde la fecha más reciente entre otorgamiento de crédito adicional o celebración del acuerdo de refinanciación · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por lo menos 180 días'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente»
- **e8 Condicion** «Crédito adicional no cancelado» — La restricción de permanencia aplica en la medida en que el crédito adicional no haya sido cancelado · tramo [exacta]: «en la medida en que dicha financiación adicional no hubiese sido cancelada»
- R: e4 Condicion —condicion_de→ e1 Operacion
- R: e6 Condicion —condicion_de→ e5 Excepcion
- R: e8 Condicion —condicion_de→ e7 Restriccion
- Omisión `meta_normativo` [exacta]: «A este fin, el cómputo de los plazos no se interrumpirá por el otorgamiento de renovaciones cuando previamente no se haya producido la cancelación efectiva de las obligaciones vencidas, es decir sin recurrir a financiación directa o indirecta de la entidad» — Aclaración interpretativa sobre cómo se computa el plazo de atraso; el contenido normativo (la condición sobre la no interrupción) se extrajo como Condicion e4

### N — supuestos a clasificar

- 1. «sin cancelación efectiva previa» → candidatos: e4 Condicion (0.67)
- 2. «pago del 15 %» → candidatos: e5 Excepcion (1.00), e6 Condicion (1.00), e1 Operacion (0.50)
- 3. «financiación adicional sin cancelar» → candidatos: e8 Condicion (0.67), e3 Operacion (0.33), e4 Condicion (0.33), e7 Restriccion (0.33)

## Código W

- **c1 Condicion** «Atrasos superiores a un año — indicador Irrecuperable» — Indicador de la categoría Irrecuperable (cartera comercial): el cliente incurre en atrasos superiores a un año, junto con refinanciación de capital e intereses y financiación de pérdidas de explotación. · umbral: ['atrasos superiores a un año'] · tramo [exacta]: «Entre los indicadores que pueden reflejar esta situación se destacan que el cliente: […] Incurra en atrasos superiores a un año»
- **c2 Condicion** «Refinanciación de capital e intereses — indicador Irrecuperable» — Indicador de la categoría Irrecuperable: el cliente cuenta con refinanciación del capital y sus intereses. · tramo [exacta]: «cuente con refinanciación del capital y sus intereses»
- **c3 Condicion** «Financiación de pérdidas de explotación — indicador Irrecuperable» — Indicador de la categoría Irrecuperable: el cliente cuenta con financiación de pérdidas de explotación. · tramo [exacta]: «con financiación de pérdidas de explotación»
- **r1 Restriccion** «Cómputo de plazos no interrumpido por renovaciones» — El cómputo de los plazos de atraso no se interrumpe por renovaciones si antes no hubo cancelación efectiva de las obligaciones vencidas, es decir sin recurrir a financiación directa o indirecta de la entidad. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «el cómputo de los plazos no se interrumpirá por el otorgamiento de renovaciones cuando previamente no se haya producido la cancelación efectiva de las obligaciones vencidas»
- **op1 Operacion** «Cómputo de plazos de atraso del deudor» — Cómputo de los plazos de atraso a los fines de la clasificación en Irrecuperable. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el cómputo de los plazos»
- **p1 Potestad** «Reclasificación al nivel inmediato superior» — Puede reclasificarse al deudor Irrecuperable en el nivel inmediato superior si pagó sin atrasos superiores a 31 días el 15 % de las obligaciones refinanciadas y la totalidad de intereses devengados, y se observan las otras condiciones de ese nivel. · tramo [exacta]: «podrá reclasificarse al deudor en el nivel inmediato superior»
- **c4 Condicion** «Pago 15 % refinanciado sin atrasos >31 días» — Haber pagado al menos el 15 % de las obligaciones refinanciadas sin atrasos superiores a 31 días. · umbral: ['sin haber incurrido en atrasos superiores a los 31 días', 'al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores…'] · tramo [exacta]: «al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 15 % de las obligaciones refinanciadas»
- **c5 Condicion** «Pago de la totalidad de intereses devengados» — Haber pagado la totalidad de los intereses devengados. · tramo [exacta]: «la totalidad de los intereses devengados»
- **c6 Condicion** «Otras condiciones del nivel superior observadas» — Que se observen las otras condiciones previstas en el nivel inmediato superior. · tramo [exacta]: «si, además, se observan las otras condiciones previstas en el citado nivel»
- **o1 Obligacion** «Permanencia mínima 180 días en Irrecuperable» — El deudor Irrecuperable que refinanció y recibió crédito adicional (punto 2.2.5 de Previsiones mínimas) no cancelado debe permanecer en esta categoría al menos 180 días desde el otorgamiento del crédito adicional o del acuerdo de refinanciación, la circunstancia más reciente. · props: `{"tipo": "asignacion"}` · umbral: ['por lo menos 180 días'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días»
- **c7 Condicion** «Refinanciación y crédito adicional no cancelado» — Deudor clasificado en Irrecuperable que refinanció su deuda (aun habiendo cancelado el 15 %) y recibió crédito adicional según punto 2.2.5 de Previsiones mínimas. · tramo [exacta]: «haya refinanciado su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo precedente– y recibido crédito adicional»
- **c8 Condicion** «Financiación adicional no cancelada» — Que la financiación adicional no haya sido cancelada. · tramo [exacta]: «en la medida en que dicha financiación adicional no hubiese sido cancelada»
- R: r1 Restriccion —limita→ op1 Operacion
- R: c4 Condicion —condicion_de→ p1 Potestad
- R: c5 Condicion —condicion_de→ p1 Potestad
- R: c6 Condicion —condicion_de→ p1 Potestad
- R: c7 Condicion —condicion_de→ o1 Obligacion
- R: c8 Condicion —condicion_de→ o1 Obligacion

### W — supuestos a clasificar

- 1. «sin cancelación efectiva previa» → candidatos: r1 Restriccion (0.67)
- 2. «pago del 15 %» → candidatos: c4 Condicion (1.00), p1 Potestad (1.00), c5 Condicion (0.50), c7 Condicion (0.50)
- 3. «financiación adicional sin cancelar» → candidatos: c8 Condicion (0.67), c1 Condicion (0.33), c3 Condicion (0.33), c7 Condicion (0.33)

