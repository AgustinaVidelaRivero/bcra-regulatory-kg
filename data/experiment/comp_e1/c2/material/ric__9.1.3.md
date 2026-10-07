# `ric::9.1.3` — Limitación al crecimiento de pasivos

Grupos: grupo_c. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 9. Incrementos de exigencia por riesgo de crédito
> *heredado:* 9.1. Normas de procedimiento
> *propio:* 9.1.3. Limitación al crecimiento de pasivos Cuando se presenten ambas o alguna de las siguientes situaciones: - Obligatoriedad de presentación del Plan de Regularización y Saneamiento en capitales mínimos. - La suma de incrementos de exigencia de capitales mínimos por riesgo de crédito resultantes de los incumplimientos en las relaciones técnicas de activos inmovilizados y/o crediticias, supere el 5 % de dicha exigencia (código 70100000). No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento, teniendo en cuenta el importe registrado en el código 310000 del Balance de Saldos. Se admitirá únicamente el crecimiento originado por el devengamiento de intereses. En los casos de regulaciones sobre base consolidada, se asimilarán las partidas a la posición individual. Dicho límite se observará mientras persista alguna de las situaciones previstas.

## Supuestos de la fase A de T4 (M1)

1. «obligación del plan de regularización»
2. «incrementos de más del 5 %»
3. «base consolidada»
4. «mientras persista»

## Código A

- **op1 Operacion** «Crecimiento de depósitos (pasivos)» — Crecimiento del nivel de depósitos (pasivos) respecto del alcanzado en el mes en que se origina el incumplimiento, según el importe del código 310000 del Balance de Saldos · props: `{"tipo": "crecimiento_de_pasivos"}` · tramo [exacta]: «No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento»
- **r1 Restriccion** «Tope: depósitos del mes del incumplimiento» — No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento, según el importe del código 310000 del Balance de Saldos. El límite se observa mientras persista alguna de las situaciones previstas. · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento", "comparacion": "maximo_inclusivo", "base": "nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento", "regla_comparacion": "limite_relativo:negacion:raiz_exced", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origi…'] · tramo [exacta]: «No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento, teniendo en cuenta el importe registrado en el código 310000 del Balance de Saldos.»
- **c1 Condicion** «Plan de Regularización y Saneamiento obligatorio» — Supuesto: obligatoriedad de presentación del Plan de Regularización y Saneamiento en capitales mínimos; basta con que se presente este supuesto o el otro (ambas o alguna). · tramo [exacta]: «Obligatoriedad de presentación del Plan de Regularización y Saneamiento en capitales mínimos.»
- **c2 Condicion** «Incrementos de exigencia superan 5 %» — Supuesto: la suma de incrementos de exigencia de capitales mínimos por riesgo de crédito resultantes de incumplimientos en las relaciones técnicas de activos inmovilizados y/o crediticias supera el 5 % de dicha exigencia (código 70100000); basta con este supuesto o el otro. · umbral: ['supere el 5 % de dicha exigencia'] · tramo [exacta]: «La suma de incrementos de exigencia de capitales mínimos por riesgo de crédito resultantes de los incumplimientos en las relaciones técnicas de activos inmovilizados y/o crediticias, supere el 5 % de dicha exigencia (código 70100000).»
- **x1 Excepcion** «Excepción: crecimiento por devengamiento de intereses» — Excepciona el tope al nivel de depósitos: se admite únicamente el crecimiento originado por el devengamiento de intereses. · tramo [exacta]: «Se admitirá únicamente el crecimiento originado por el devengamiento de intereses.»
- **o1 Obligacion** «Asimilación de partidas en base consolidada» — En los casos de regulaciones sobre base consolidada, se asimilarán las partidas a la posición individual a los fines del límite de depósitos. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «En los casos de regulaciones sobre base consolidada, se asimilarán las partidas a la posición individual.»
- R: r1 Restriccion —limita→ op1 Operacion
- R: c1 Condicion —condicion_de→ r1 Restriccion
- R: c2 Condicion —condicion_de→ r1 Restriccion
- R: x1 Excepcion —exceptua→ r1 Restriccion
- R: o1 Obligacion —regula→ op1 Operacion

### A — supuestos a clasificar

- 1. «obligación del plan de regularización» → candidatos: c1 Condicion (0.67)
- 2. «incrementos de más del 5 %» → candidatos: c2 Condicion (1.00)
- 3. «base consolidada» → candidatos: o1 Obligacion (1.00)
- 4. «mientras persista» → candidatos: r1 Restriccion (1.00)

## Código H

- **op1 Operacion** «Crecimiento de depósitos (pasivos)» — Crecimiento del nivel de depósitos (pasivos) respecto del alcanzado en el mes en que se origina el incumplimiento, según el importe registrado en el código 310000 del Balance de Saldos. · props: `{"tipo": "otra"}` · tramo [exacta]: «No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento»
- **r1 Restriccion** «Tope: nivel de depósitos del mes del incumplimiento» — No puede excederse el nivel de depósitos alcanzados en el mes en que se origine el incumplimiento, según el importe del código 310000 del Balance de Saldos. En regulaciones sobre base consolidada se asimilan las partidas a la posición individual. El límite se observa mientras persista alguna de las situaciones previstas. · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento", "comparacion": "maximo_inclusivo", "base": "nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento", "regla_comparacion": "limite_relativo:negacion:raiz_exced", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origi…'] · tramo [exacta]: «No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento, teniendo en cuenta el importe registrado en el código 310000 del Balance de Saldos.»
- **x1 Excepcion** «Excepción: crecimiento por devengamiento de intereses» — Exceptúa del límite al nivel de depósitos (no podrá excederse el nivel de depósitos del mes del incumplimiento) únicamente el crecimiento originado por el devengamiento de intereses. · tramo [exacta]: «Se admitirá únicamente el crecimiento originado por el devengamiento de intereses.»
- **c1 Condicion** «Obligatoriedad de Plan de Regularización y Saneamiento» — Supuesto alternativo (ambas o alguna de las situaciones): es obligatoria la presentación del Plan de Regularización y Saneamiento en capitales mínimos; activa el límite al crecimiento de depósitos. · tramo [exacta]: «Obligatoriedad de presentación del Plan de Regularización y Saneamiento en capitales mínimos.»
- **c2 Condicion** «Incrementos de exigencia por riesgo de crédito superan 5 %» — Supuesto alternativo (ambas o alguna de las situaciones): la suma de incrementos de exigencia de capitales mínimos por riesgo de crédito, por incumplimientos en relaciones técnicas de activos inmovilizados y/o crediticias, supera el 5 % de dicha exigencia (código 70100000); activa el límite al crecimiento de depósitos. · umbral: ['supere el 5 % de dicha exigencia (código 70100000)'] · tramo [exacta]: «La suma de incrementos de exigencia de capitales mínimos por riesgo de crédito resultantes de los incumplimientos en las relaciones técnicas de activos inmovilizados y/o crediticias, supere el 5 % de dicha exigencia (código 70100000).»
- R: r1 Restriccion —limita→ op1 Operacion
- R: x1 Excepcion —exceptua→ r1 Restriccion
- R: c1 Condicion —condicion_de→ r1 Restriccion
- R: c2 Condicion —condicion_de→ r1 Restriccion

### H — supuestos a clasificar

- 1. «obligación del plan de regularización» → candidatos: c1 Condicion (0.67)
- 2. «incrementos de más del 5 %» → candidatos: c2 Condicion (1.00)
- 3. «base consolidada» → candidatos: r1 Restriccion (1.00)
- 4. «mientras persista» → candidatos: r1 Restriccion (1.00)

## Código K

- **op1 Operacion** «Captación de depósitos» — Nivel de depósitos de la entidad, según importe registrado en el código 310000 del Balance de Saldos · props: `{"tipo": "captacion de depositos"}` · tramo [exacta]: «el nivel de depósitos»
- **r1 Restriccion** «Tope nivel de depósitos del mes de incumplimiento» — No podrá excederse el nivel de depósitos alcanzado en el mes en que se origine el incumplimiento, considerando el importe del código 310000 del Balance de Saldos; rige mientras persista alguna de las situaciones previstas. En regulaciones sobre base consolidada, las partidas se asimilan a la posición individual. · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento", "comparacion": "maximo_inclusivo", "base": "nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento", "regla_comparacion": "limite_relativo:negacion:raiz_exced", "origen": "e1", "tramo_verificado": "exacta"}]}` · no definidas: `{"vigencia": "Dicho límite se observará mientras persista alguna de las situaciones previstas.", "base_consolidada": "En los casos de regulaciones sobre base consolidada, se asimilarán las partidas a ` · umbral: ['No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origi…'] · tramo [exacta]: «No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento»
- **c1 Condicion** «Obligación de presentar Plan de Regularización» — Supuesto alternativo (basta alguno): obligatoriedad de presentar el Plan de Regularización y Saneamiento en capitales mínimos. · tramo [exacta]: «Obligatoriedad de presentación del Plan de Regularización y Saneamiento en capitales mínimos.»
- **c2 Condicion** «Incrementos de exigencia superan 5 %» — Supuesto alternativo: la suma de incrementos de exigencia por riesgo de crédito por incumplimientos en relaciones técnicas de activos inmovilizados y/o crediticias supera el 5 % de dicha exigencia (código 70100000). · umbral: ['supere el 5 % de dicha exigencia'] · tramo [exacta]: «La suma de incrementos de exigencia de capitales mínimos por riesgo de crédito resultantes de los incumplimientos en las relaciones técnicas de activos inmovilizados y/o crediticias, supere el 5 % de dicha exigencia (código 70100000).»
- **x1 Excepcion** «Crecimiento por devengamiento de intereses admitido» — Del tope de depósitos se admite únicamente el crecimiento originado por el devengamiento de intereses. · tramo [exacta]: «Se admitirá únicamente el crecimiento originado por el devengamiento de intereses.»
- R: r1 Restriccion —limita→ op1 Operacion
- R: c1 Condicion —condicion_de→ r1 Restriccion
- R: c2 Condicion —condicion_de→ r1 Restriccion
- R: x1 Excepcion —exceptua→ r1 Restriccion

### K — supuestos a clasificar

- 1. «obligación del plan de regularización» → candidatos: c1 Condicion (1.00)
- 2. «incrementos de más del 5 %» → candidatos: c2 Condicion (1.00)
- 3. «base consolidada» → candidatos: r1 Restriccion (1.00)
- 4. «mientras persista» → candidatos: r1 Restriccion (1.00)

## Código W

- **op1 Operacion** «Captación de depósitos» — Crecimiento del nivel de depósitos (código 310000 del Balance de Saldos) · props: `{"tipo": "captación de depósitos"}` · tramo [exacta]: «el nivel de depósitos alcanzados»
- **c1 Condicion** «Obligatoriedad de Plan de Regularización y Saneamiento» — Supuesto alternativo (basta uno): obligatoriedad de presentar el Plan de Regularización y Saneamiento en capitales mínimos · tramo [exacta]: «Obligatoriedad de presentación del Plan de Regularización y Saneamiento en capitales mínimos.»
- **c2 Condicion** «Incrementos de exigencia superiores al 5 %» — Supuesto alternativo (basta uno): la suma de incrementos de exigencia por riesgo de crédito por incumplimientos en relaciones técnicas de activos inmovilizados y/o crediticias supera el 5 % de dicha exigencia (código 70100000) · umbral: ['supere el 5 % de dicha exigencia'] · tramo [exacta]: «La suma de incrementos de exigencia de capitales mínimos por riesgo de crédito resultantes de los incumplimientos en las relaciones técnicas de activos inmovilizados y/o crediticias, supere el 5 % de dicha exigencia (código 70100000).»
- **r1 Restriccion** «Tope de depósitos al nivel del mes de incumplimiento» — No podrá excederse el nivel de depósitos alcanzado en el mes en que se origine el incumplimiento (código 310000 del Balance de Saldos), mientras persista alguna de las situaciones; en regulaciones sobre base consolidada las partidas se asimilan a la posición individual · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el\nincumplimiento", "comparacion": "maximo_inclusivo", "base": "nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento", "regla_comparacion": "limite_relativo:negacion:raiz_exced", "origen": "e1", "tramo_verificado": "exacta"}]}` · no definidas: `{"vigencia": "Dicho límite se observará mientras persista alguna de las situaciones previstas.", "base_consolidada": "En los casos de regulaciones sobre base consolidada, se asimilarán las partidas a ` · umbral: ['No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origi…'] · tramo [exacta]: «No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento»
- **x1 Excepcion** «Crecimiento por devengamiento de intereses» — Del tope de depósitos se admite únicamente el crecimiento originado por devengamiento de intereses · tramo [exacta]: «Se admitirá únicamente el crecimiento originado por el devengamiento de intereses.»
- R: c1 Condicion —condicion_de→ r1 Restriccion
- R: c2 Condicion —condicion_de→ r1 Restriccion
- R: r1 Restriccion —limita→ op1 Operacion
- R: x1 Excepcion —exceptua→ r1 Restriccion

### W — supuestos a clasificar

- 1. «obligación del plan de regularización» → candidatos: c1 Condicion (0.67)
- 2. «incrementos de más del 5 %» → candidatos: c2 Condicion (1.00)
- 3. «base consolidada» → candidatos: r1 Restriccion (1.00)
- 4. «mientras persista» → candidatos: r1 Restriccion (1.00)

