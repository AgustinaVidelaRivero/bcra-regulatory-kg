# `polcre::7.1::cierre` — [bloque cierre] Clientes comprendidos.

Grupos: grupo_c. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 7. Financiaciones a "Grandes empresas exportadoras".
> *heredado:* 7.1. Clientes comprendidos.
> *propio:* Cuando el cliente reúna la condición del punto 7.1.1. pero el importe total de sus financiaciones en pesos en el sistema financiero no supere el importe de $ 30.000 millones y no haya mantenido pases y/o cauciones bursátiles tomadas –en pesos– durante los últimos 90 días corridos, la entidad financiera podrá otorgarle nuevas financiaciones en la medida que con tales desembolsos no se supere ese importe. Cuando se trate de conjuntos económicos se los considerará como un solo cliente, a cuyo efecto será de aplicación el punto 1.2.2. de las normas sobre "Grandes exposiciones al riesgo de crédito". A los fines de la imputación de las financiaciones, será de aplicación lo previsto en las normas sobre "Grandes exposiciones al riesgo de crédito".

## Supuestos de la fase A de T4 (M1)

1. «reúne 7.1.1»
2. «no supera $ 30.000 millones»
3. «sin pases»
4. «desembolsos que no superen el importe»
5. «conjuntos económicos»

## Código A

- **op1 Operacion** «Nuevas financiaciones a grandes empresas exportadoras» — Otorgamiento de nuevas financiaciones en pesos al cliente que reúne la condición del punto 7.1.1. y cuyo importe total de financiaciones en pesos en el sistema financiero no supera $ 30.000 millones · props: `{"tipo": "financiacion"}` · tramo [exacta]: «podrá otorgarle nuevas financiaciones»
- **p1 Potestad** «Otorgar nuevas financiaciones hasta $ 30.000 millones» — La entidad financiera puede otorgar nuevas financiaciones al cliente que reúne la condición del punto 7.1.1. pero cuyas financiaciones totales en pesos en el sistema financiero no superan $ 30.000 millones, en la medida que con los desembolsos no se supere ese importe · tramo [no]: «la entidad financiera podrá otorgarle nuevas financiaciones en la medida que con tales desembolsos no se supere ese importe»
- **c1 Condicion** «Financiaciones en pesos no superan $ 30.000 millones» — El importe total de las financiaciones en pesos del cliente en el sistema financiero no supera $ 30.000 millones · umbral: ['no supere el importe de $ 30.000 millones'] · tramo [exacta]: «el importe total de sus financiaciones en pesos en el sistema financiero no supere el importe de $ 30.000 millones»
- **c2 Condicion** «Sin pases ni cauciones bursátiles tomadas últimos 90 días» — El cliente no ha mantenido pases y/o cauciones bursátiles tomadas en pesos durante los últimos 90 días corridos · umbral: ['durante los últimos 90 días corridos'] · tramo [no]: «no haya mantenido pases y/o cauciones bursátiles tomadas –en pesos– durante los últimos 90 días corridos»
- **r1 Restriccion** «Tope $ 30.000 millones con los nuevos desembolsos» — Los nuevos desembolsos no pueden hacer superar el importe de $ 30.000 millones de financiaciones totales del cliente · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "no se supere ese importe", "comparacion": "maximo_inclusivo", "base": "ese importe", "regla_comparacion": "limite_relativo:negacion:raiz_super", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['no se supere ese importe'] · tramo [no]: «en la medida que con tales desembolsos no se supere ese importe»
- **d1 Definicion** «Conjunto económico como un solo cliente» — Los conjuntos económicos se consideran como un solo cliente, de acuerdo con el punto 1.2.2. de las normas sobre Grandes exposiciones al riesgo de crédito · props: `{"termino": "conjuntos económicos"}` · tramo [exacta]: «Cuando se trate de conjuntos económicos se los considerará como un solo cliente»
- R: p1 Potestad —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: r1 Restriccion —limita→ op1 Operacion
- Omisión `fuera_de_tipos` [exacta]: «A los fines de la imputación de las financiaciones, será de aplicación lo previsto en las normas sobre "Grandes exposiciones al riesgo de crédito".» — Remisión a otras normas sobre la imputación de las financiaciones; el contenido lo fija la norma remitida, no hay deber ni definición propia que extraer.

### A — supuestos a clasificar

- 1. «reúne 7.1.1» → candidatos: op1 Operacion (1.00), p1 Potestad (1.00), d1 Definicion (0.33)
- 2. «no supera $ 30.000 millones» → candidatos: c1 Condicion (1.00), op1 Operacion (1.00), p1 Potestad (0.75), r1 Restriccion (0.75)
- 3. «sin pases» → candidatos: c2 Condicion (1.00)
- 4. «desembolsos que no superen el importe» → candidatos: p1 Potestad (0.67), r1 Restriccion (0.67), c1 Condicion (0.33), op1 Operacion (0.33)
- 5. «conjuntos económicos» → candidatos: d1 Definicion (1.00)

## Código H

- **op1 Operacion** «Otorgamiento de nuevas financiaciones en pesos» — Otorgamiento de nuevas financiaciones a clientes que reúnen la condición del punto 7.1.1. y cuyas financiaciones totales en pesos en el sistema financiero no superan $ 30.000 millones. · props: `{"tipo": "financiacion"}` · tramo [exacta]: «la entidad financiera podrá otorgarle nuevas financiaciones»
- **p1 Potestad** «Podrá otorgar nuevas financiaciones hasta $ 30.000 millones» — La entidad financiera puede otorgar nuevas financiaciones al cliente que reúna la condición del punto 7.1.1. y no supere el importe total de financiaciones en pesos de $ 30.000 millones, sin que los desembolsos superen ese importe. · tramo [no]: «la entidad financiera podrá otorgarle nuevas financiaciones en la medida que con tales desembolsos no se supere ese importe»
- **r1 Restriccion** «Tope $ 30.000 millones — nuevas financiaciones» — Los nuevos desembolsos no pueden hacer superar el importe total de financiaciones en pesos en el sistema financiero de $ 30.000 millones. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['no supere el importe de $ 30.000 millones'] · tramo [no]: «en la medida que con tales desembolsos no se supere ese importe»
- **c1 Condicion** «Cliente reúne condición del punto 7.1.1» — El cliente reúne la condición del punto 7.1.1. · tramo [exacta]: «Cuando el cliente reúna la condición del punto 7.1.1.»
- **c2 Condicion** «Financiaciones en pesos hasta $ 30.000 millones» — El importe total de las financiaciones del cliente en pesos en el sistema financiero no supera $ 30.000 millones. · umbral: ['no supere el importe de $ 30.000 millones'] · tramo [exacta]: «el importe total de sus financiaciones en pesos en el sistema financiero no supere el importe de $ 30.000 millones»
- **c3 Condicion** «Sin pases/cauciones bursátiles tomadas en 90 días» — El cliente no mantuvo pases y/o cauciones bursátiles tomadas en pesos durante los últimos 90 días corridos. · umbral: ['durante los últimos 90 días corridos'] · tramo [no]: «no haya mantenido pases y/o cauciones bursátiles tomadas –en pesos– durante los últimos 90 días corridos»
- **d1 Definicion** «Conjunto económico como un solo cliente» — Los conjuntos económicos se consideran un solo cliente, conforme al punto 1.2.2. de las normas sobre Grandes exposiciones al riesgo de crédito. · props: `{"termino": "conjuntos económicos"}` · tramo [exacta]: «Cuando se trate de conjuntos económicos se los considerará como un solo cliente, a cuyo efecto será de aplicación el punto 1.2.2. de las normas sobre "Grandes exposiciones al riesgo de crédito".»
- R: p1 Potestad —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: r1 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: r1 Restriccion —limita→ op1 Operacion
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad
- Omisión `meta_normativo` [exacta]: «A los fines de la imputación de las financiaciones, será de aplicación lo previsto en las normas sobre "Grandes exposiciones al riesgo de crédito".» — Remisión a otras normas para la imputación de las financiaciones; la remisión la registra el código y no hay contenido propio extraíble.

### H — supuestos a clasificar

- 1. «reúne 7.1.1» → candidatos: c1 Condicion (1.00), op1 Operacion (0.67), p1 Potestad (0.67), d1 Definicion (0.33)
- 2. «no supera $ 30.000 millones» → candidatos: c2 Condicion (1.00), op1 Operacion (0.75), p1 Potestad (0.75), r1 Restriccion (0.75)
- 3. «sin pases» → candidatos: c3 Condicion (1.00)
- 4. «desembolsos que no superen el importe» → candidatos: p1 Potestad (1.00), r1 Restriccion (0.67), c2 Condicion (0.33)
- 5. «conjuntos económicos» → candidatos: d1 Definicion (1.00)

## Código K

- **op1 Operacion** «Nuevas financiaciones a cliente del 7.1.1» — Otorgamiento de nuevas financiaciones por la entidad financiera a un cliente que reúne la condición del punto 7.1.1 (gran empresa exportadora) · props: `{"tipo": "financiacion"}` · tramo [exacta]: «la entidad financiera podrá otorgarle nuevas financiaciones»
- **p1 Potestad** «Facultad de otorgar nuevas financiaciones hasta $30.000 millones» — La entidad financiera podrá otorgar nuevas financiaciones al cliente que reúna la condición del punto 7.1.1, siempre que con tales desembolsos no se supere el importe de $ 30.000 millones de financiaciones totales en pesos en el sistema financiero. · tramo [exacta]: «la entidad financiera podrá otorgarle nuevas financiaciones en la medida que con tales desembolsos no se supere ese importe»
- **c1 Condicion** «Financiaciones en pesos no superan $30.000 millones» — Que el importe total de financiaciones en pesos del cliente en el sistema financiero no supere $ 30.000 millones · umbral: ['no supere el importe de $ 30.000 millones'] · tramo [exacta]: «el importe total de sus financiaciones en pesos en el sistema financiero no supere el importe de $ 30.000 millones»
- **c2 Condicion** «Sin pases/cauciones tomadas en pesos últimos 90 días» — Que el cliente no haya mantenido pases y/o cauciones bursátiles tomadas en pesos durante los últimos 90 días corridos · umbral: ['durante los últimos 90 días corridos'] · tramo [exacta]: «no haya mantenido pases y/o cauciones bursátiles tomadas –en pesos– durante los últimos 90 días corridos»
- **c3 Condicion** «Cliente reúne condición del punto 7.1.1» — Que el cliente reúna la condición del punto 7.1.1 · tramo [exacta]: «Cuando el cliente reúna la condición del punto 7.1.1.»
- **r1 Restriccion** «Tope desembolsos: no superar $30.000 millones» — Las nuevas financiaciones no pueden hacer que se supere el importe de $ 30.000 millones · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "no se supere ese importe", "comparacion": "maximo_inclusivo", "base": "ese importe", "regla_comparacion": "limite_relativo:negacion:raiz_super", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['no se supere ese importe'] · tramo [exacta]: «en la medida que con tales desembolsos no se supere ese importe»
- **d1 Definicion** «Conjuntos económicos como un solo cliente» — Se los considera como un solo cliente, aplicando el punto 1.2.2 de las normas sobre Grandes exposiciones al riesgo de crédito · props: `{"termino": "conjuntos económicos"}` · tramo [exacta]: «Cuando se trate de conjuntos económicos se los considerará como un solo cliente»
- **ob1 Obligacion** «Imputación de financiaciones según Grandes exposiciones» — La imputación de las financiaciones se realiza según lo previsto en las normas sobre Grandes exposiciones al riesgo de crédito · props: `{"tipo": "calculo"}` · tramo [exacta]: «A los fines de la imputación de las financiaciones, será de aplicación lo previsto en las normas sobre "Grandes exposiciones al riesgo de crédito"»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: r1 Restriccion —limita→ op1 Operacion
- R: p1 Potestad —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: r1 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: Sujeto_entidad_financiera (mención «la entidad financiera») —ejecuta→ op1 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «la entidad financiera podrá otorgarle nuevas financiaciones» — Potestad → Operacion habilitada; no hay predicado

### K — supuestos a clasificar

- 1. «reúne 7.1.1» → candidatos: c3 Condicion (1.00), op1 Operacion (1.00), p1 Potestad (0.67), d1 Definicion (0.33)
- 2. «no supera $ 30.000 millones» → candidatos: c1 Condicion (0.75), p1 Potestad (0.75), r1 Restriccion (0.75)
- 3. «sin pases» → candidatos: c2 Condicion (1.00)
- 4. «desembolsos que no superen el importe» → candidatos: p1 Potestad (0.67), r1 Restriccion (0.67), c1 Condicion (0.33)
- 5. «conjuntos económicos» → candidatos: d1 Definicion (1.00)

## Código W

- **op1 Operacion** «Nuevas financiaciones a gran empresa exportadora» — Otorgamiento de nuevas financiaciones por la entidad financiera a un cliente que reúne la condición del punto 7.1.1. · props: `{"tipo": "financiación"}` · tramo [exacta]: «la entidad financiera podrá otorgarle nuevas financiaciones»
- **p1 Potestad** «Facultad de otorgar nuevas financiaciones hasta $30.000 millones» — La entidad financiera podrá otorgar nuevas financiaciones al cliente que reúna la condición del punto 7.1.1., en la medida que con tales desembolsos no se supere el importe de $ 30.000 millones. · tramo [exacta]: «la entidad financiera podrá otorgarle nuevas financiaciones en la medida que con tales desembolsos no se supere ese importe.»
- **c0 Condicion** «Cliente reúne condición del punto 7.1.1.» — Que el cliente reúna la condición del punto 7.1.1. · tramo [exacta]: «Cuando el cliente reúna la condición del punto 7.1.1.»
- **c1 Condicion** «Financiaciones en pesos del cliente ≤ $30.000 millones» — Que el importe total de financiaciones en pesos del cliente en el sistema financiero no supere $ 30.000 millones. · umbral: ['no supere el importe de $ 30.000 millones'] · tramo [exacta]: «el importe total de sus financiaciones en pesos en el sistema financiero no supere el importe de $ 30.000 millones»
- **c2 Condicion** «Sin pases/cauciones tomadas en pesos 90 días» — Que el cliente no haya mantenido pases y/o cauciones bursátiles tomadas en pesos durante los últimos 90 días corridos. · umbral: ['durante los últimos 90 días corridos'] · tramo [exacta]: «no haya mantenido pases y/o cauciones bursátiles tomadas –en pesos– durante los últimos 90 días corridos»
- **c3 Condicion** «Nuevos desembolsos no superan $30.000 millones» — Que con los nuevos desembolsos no se supere el importe de $ 30.000 millones. · props: `{"umbrales": [{"tramo": "no se supere ese importe", "comparacion": "maximo_inclusivo", "base": "ese importe", "regla_comparacion": "limite_relativo:negacion:raiz_super", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['no se supere ese importe'] · tramo [exacta]: «en la medida que con tales desembolsos no se supere ese importe»
- **d1 Definicion** «Conjunto económico como un solo cliente» — Los conjuntos económicos se consideran como un solo cliente, aplicando el punto 1.2.2. de las normas sobre Grandes exposiciones al riesgo de crédito. · props: `{"termino": "conjuntos económicos"}` · tramo [exacta]: «Cuando se trate de conjuntos económicos se los considerará como un solo cliente»
- **o1 Obligacion** «Imputación de financiaciones según Grandes exposiciones» — La imputación de las financiaciones se realiza según lo previsto en las normas sobre Grandes exposiciones al riesgo de crédito. · props: `{"tipo": "calculo"}` · tramo [exacta]: «A los fines de la imputación de las financiaciones, será de aplicación lo previsto en las normas sobre "Grandes exposiciones al riesgo de crédito".»
- R: c0 Condicion —condicion_de→ p1 Potestad
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: p1 Potestad —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: Sujeto_entidad_financiera (mención «la entidad financiera») —ejecuta→ op1 Operacion
- R: o1 Obligacion —regula→ op1 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «la entidad financiera podrá otorgarle nuevas financiaciones» — Potestad → Operacion habilitada; no hay predicado

### W — supuestos a clasificar

- 1. «reúne 7.1.1» → candidatos: c0 Condicion (1.00), op1 Operacion (1.00), p1 Potestad (0.67), d1 Definicion (0.33)
- 2. «no supera $ 30.000 millones» → candidatos: c1 Condicion (0.75), c3 Condicion (0.75), p1 Potestad (0.75)
- 3. «sin pases» → candidatos: c2 Condicion (1.00)
- 4. «desembolsos que no superen el importe» → candidatos: c3 Condicion (0.67), p1 Potestad (0.67), c1 Condicion (0.33)
- 5. «conjuntos económicos» → candidatos: d1 Definicion (1.00)

