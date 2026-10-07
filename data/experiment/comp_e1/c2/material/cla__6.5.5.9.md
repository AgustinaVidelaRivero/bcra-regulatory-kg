# `cla::6.5.5.9` — Clientes del sector privado no financiero, cuya deuda (por todo concepto) más el

Grupos: grupo_c, omisiones. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.5. Irrecuperable.
> *heredado:* Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de circunstancias futuras, su incobrabilidad es evidente al momento del análisis. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *heredado:* Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el motivo (entre ellos por no contar con legajo o por no haber proporcionado información confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente, con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, por un período de hasta 540 días contados a partir de la apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales de cobro, según corresponda, no hubiesen presentado la documentación que permita realizarla, siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos. Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad".
> *propio:* 6.5.5.9. Clientes del sector privado no financiero, cuya deuda (por todo concepto) más el importe de la financiación solicitada, al momento del otorgamiento de ésta, exceda del 2,5 % de la responsabilidad patrimonial computable de la entidad del último día del mes anterior al que corresponda o el equivalente al importe de referencia establecido en el punto 3.7., de ambos el menor, y que no hayan presentado declaración jurada sobre si revisten o no el carácter de vinculados al respectivo intermediario financiero o si su relación con éste implica la existencia de influencia controlante, o no hayan actualizado la presentada con anterioridad, con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, por un período de hasta 540 días contados a partir de la apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales de cobro, según corresponda, no hubiesen presentado la documentación que permita realizarla, siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos. Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad". Este tratamiento se aplicará desde la fecha de otorgamiento de la asistencia, cuando se trate de la primera declaración, o a partir del 1.12, en los casos de las actualizaciones posteriores, y hasta el mes anterior a la fecha en que el cliente efectúe la pertinente presentación.

## Supuestos de la fase A de T4 (M1)

1. «deuda de más del 2,5 % de la RPC o del importe de referencia»
2. «excepción de concurso hasta 540 días»
3. «siempre que haya informe»
4. «primera declaración»
5. «actualizaciones»

## Omisiones leídas en T4 (M2)

con_marca:26 [normativa; propio] «Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad"»

## Código A

- **op1 Operacion** «Clasificación como Irrecuperable por falta de declaración jurada de vinculación» — Clasificación en la categoría Irrecuperable de clientes del sector privado no financiero cuya deuda más la financiación solicitada excede el 2,5 % de la RPC (o el importe de referencia del punto 3.7., el menor) y que no presentaron o no actualizaron la declaración jurada sobre vinculación; indicador de irrecuperabilidad que el encabezado enuncia como 'entre los indicadores que pueden reflejar esta… · props: `{"tipo": "clasificacion de deudor"}` · tramo [no]: «Clientes del sector privado no financiero, cuya deuda (por todo concepto) más el importe de la financiación solicitada, al momento del otorgamiento de ésta, exceda del 2,5 % de la responsabilidad patrimonial computable»
- **c1 Condicion** «Deuda más financiación excede 2,5 % RPC o importe de referencia» — La deuda del cliente por todo concepto más la financiación solicitada, al otorgarse, excede el menor entre el 2,5 % de la responsabilidad patrimonial computable de la entidad del último día del mes anterior y el importe de referencia del punto 3.7. · umbral: ['exceda del 2,5 % de la responsabilidad patrimonial computable de la entidad del …'] · tramo [no]: «cuya deuda (por todo concepto) más el importe de la financiación solicitada, al momento del otorgamiento de ésta, exceda del 2,5 % de la responsabilidad patrimonial computable de la entidad del último día del mes anterior al que corresponda o el equivalente al importe de referencia establecido en el punto 3.7., de ambo…»
- **c2 Condicion** «Sin declaración jurada de vinculación presentada o actualizada» — El cliente no presentó la declaración jurada sobre si es vinculado al intermediario financiero o si su relación implica influencia controlante, o no actualizó la presentada con anterioridad. · tramo [no]: «que no hayan presentado declaración jurada sobre si revisten o no el carácter de vinculados al respectivo intermediario financiero o si su relación con éste implica la existencia de influencia controlante, o no hayan actualizado la presentada con anterioridad»
- **ex1 Excepcion** «Excepción deudores en concurso hasta 540 días» — Quedan fuera de la clasificación como Irrecuperable por falta de declaración jurada los deudores en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, por hasta 540 días desde la apertura del concurso, solicitud del acuerdo o inicio de gestiones judiciales de cobro, no hubiesen presentado la documentación que permita realizarla (la declaración jurada); exceptúa l… · umbral: ['por un período de hasta 540 días contados a partir de la apertura del concurso'] · tramo [no]: «con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, por un período de hasta 540 días contados a partir de la apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales de cobro, según corresponda, no hubiesen presentado…»
- **c3 Condicion** «Informe de abogado sobre razonabilidad del recupero» — Se cuenta con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos; condiciona la excepción de los deudores en concurso. · tramo [no]: «siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos»
- **c4 Condicion** «Vigencia del tratamiento desde otorgamiento o 1.12 hasta presentación» — El tratamiento (clasificación en Irrecuperable) se aplica desde la fecha de otorgamiento de la asistencia, si se trata de la primera declaración, o a partir del 1.12 en actualizaciones posteriores, y hasta el mes anterior a la fecha en que el cliente efectúe la presentación. · tramo [exacta]: «Este tratamiento se aplicará desde la fecha de otorgamiento de la asistencia, cuando se trate de la primera declaración, o a partir del 1.12, en los casos de las actualizaciones posteriores, y hasta el mes anterior a la fecha en que el cliente efectúe la pertinente presentación.»
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: c2 Condicion —condicion_de→ op1 Operacion
- R: c4 Condicion —condicion_de→ op1 Operacion
- R: c3 Condicion —condicion_de→ ex1 Excepcion
- R: op1 Operacion —aplica_a→ Sujeto_sector_privado_no_financiero (mención «Clientes del sector privado no financiero»)
- Omisión `relacion_sin_predicado` [exacta]: «con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial» — Se habría usado un predicado de excepción hacia una Operacion (exceptua), pero exceptua solo admite Restriccion u Obligacion como rango; la Excepcion exceptúa la clasificación de la Operacion.

### A — supuestos a clasificar

- 1. «deuda de más del 2,5 % de la RPC o del importe de referencia» → candidatos: c1 Condicion (1.00), op1 Operacion (1.00), ex1 Excepcion (0.17)
- 2. «excepción de concurso hasta 540 días» → candidatos: ex1 Excepcion (1.00), c3 Condicion (0.50)
- 3. «siempre que haya informe» → candidatos: c3 Condicion (0.67)
- 4. «primera declaración» → candidatos: c4 Condicion (1.00), c2 Condicion (0.50), ex1 Excepcion (0.50), op1 Operacion (0.50)
- 5. «actualizaciones» → candidatos: c4 Condicion (1.00)

### A — omisiones de T4 a clasificar

- con_marca:26 → entidades: — | omisiones: —

## Código H

- **op1 Operacion** «Clasificación como irrecuperable — cliente sin declaración jurada de vinculación» — Clasificación en la categoría Irrecuperable (6.5.5) de clientes del sector privado no financiero cuya deuda más la financiación solicitada excede del 2,5 % de la RPC o del importe de referencia del punto 3.7. (el menor) y que no presentaron o no actualizaron la declaración jurada sobre vinculación o influencia controlante. Se aplica desde la fecha de otorgamiento (primera declaración) o desde el 1… · props: `{"tipo": "clasificacion de deudor"}` · tramo [exacta]: «Entre los indicadores que pueden reflejar esta situación se destacan que el cliente: […] Clientes del sector privado no financiero, cuya deuda (por todo concepto) más el importe de la financiación solicitada, al momento del otorgamiento de ésta, exceda del 2,5 % de la responsabilidad patrimonial computable»
- **ob1 Obligacion** «Indicador irrecuperable: sin declaración jurada de vinculación» — Recomendación (indicador, no deber): entre los indicadores de situación irrecuperable se destaca que el cliente del sector privado no financiero con deuda más financiación solicitada superior al 2,5 % de la RPC (o importe del punto 3.7., el menor) no haya presentado o actualizado la declaración jurada de vinculación o influencia controlante. Se cumple con cualquiera de los dos supuestos (no presen… · props: `{"tipo": "otra", "umbrales": [{"tramo": "el equivalente al importe de refe-\nrencia establecido en el punto 3.7., de ambos el menor", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · no definidas: `{"modalidad": "Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:", "modalidad_clasificada": "no_clasificada"}` · umbral: ['exceda del 2,5 % de la responsabilidad patrimonial computable de la entidad del …', 'el equivalente al importe de referencia establecido en el punto 3.7., de ambos e…'] · tramo [exacta]: «Entre los indicadores que pueden reflejar esta situación se destacan que el cliente: […] que no hayan presentado declaración jurada sobre si revisten o no el carácter de vinculados al respectivo intermediario financiero o si su relación con éste implica la existencia de influencia controlante, o no hayan actualizado la…»
- **ex1 Excepcion** «Excepción deudores en concurso o acuerdo preventivo» — Quedan fuera del indicador de falta de declaración jurada (no se los considera en esta categoría por ese motivo) los deudores en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, por hasta 540 días desde la apertura del concurso, solicitud del acuerdo o inicio de gestiones de cobro, no hubiesen presentado la documentación. · umbral: ['por un período de hasta 540 días contados a partir de la apertura del concurso'] · tramo [exacta]: «con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, por un período de hasta 540 días contados a partir de la apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales de cobro, según corresponda, no hubiesen presentado…»
- **c1 Condicion** «Informe de abogado sobre razonabilidad del recupero» — Que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos; condición de la excepción para deudores en concurso o acuerdo preventivo. · tramo [exacta]: «siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ex1 Excepcion —exceptua_obligacion→ ob1 Obligacion
- R: c1 Condicion —condicion_de→ ex1 Excepcion
- R: ob1 Obligacion —aplica_a→ Sujeto_rol_obligado_a_clasificar_clasificacion (mención «de la entidad»)
- R: Sujeto_rol_obligado_a_clasificar_clasificacion (mención «de la entidad») —ejecuta→ op1 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad".» — Salvedad que remite a otro punto/norma; la remisión la registra el código. Se refleja en la descripción de la Operacion.

### H — supuestos a clasificar

- 1. «deuda de más del 2,5 % de la RPC o del importe de referencia» → candidatos: ob1 Obligacion (1.00), op1 Operacion (1.00)
- 2. «excepción de concurso hasta 540 días» → candidatos: ex1 Excepcion (1.00), c1 Condicion (0.50)
- 3. «siempre que haya informe» → candidatos: c1 Condicion (0.67), ob1 Obligacion (0.33)
- 4. «primera declaración» → candidatos: op1 Operacion (1.00), ex1 Excepcion (0.50), ob1 Obligacion (0.50)
- 5. «actualizaciones» → candidatos: op1 Operacion (1.00)

### H — omisiones de T4 a clasificar

- con_marca:26 → entidades: — | omisiones: om#0 relacion_sin_predicado [exacta] solap 1.0 contiene

## Código K

- **op1 Operacion** «Clasificación Irrecuperable por falta de DDJJ de vinculación» — Clasificación en la categoría Irrecuperable (indicador del punto 6.5.5) de clientes del sector privado no financiero cuya deuda más la financiación solicitada supere el umbral y que no hayan presentado o actualizado la declaración jurada sobre vinculación o influencia controlante. Se aplica desde la fecha de otorgamiento de la asistencia (primera declaración) o desde el 1.12 (actualizaciones poste… · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «Clientes del sector privado no financiero, cuya deuda (por todo concepto) más el importe de la financiación solicitada»
- **c1 Condicion** «Deuda más financiación excede 2,5 % RPC o referencia» — La deuda total más la financiación solicitada, al otorgamiento, excede el 2,5 % de la RPC de la entidad del último día del mes anterior o el importe de referencia del punto 3.7., el menor de ambos. · props: `{"umbrales": [{"tramo": "el equivalente al importe de refe-\nrencia establecido en el punto 3.7., de ambos el menor", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['exceda del 2,5 % de la responsabilidad patrimonial computable de la entidad', 'el equivalente al importe de referencia establecido en el punto 3.7., de ambos e…'] · tramo [exacta]: «cuya deuda (por todo concepto) más el importe de la financiación solicitada, al momento del otorgamiento de ésta, exceda del 2,5 % de la responsabilidad patrimonial computable»
- **c2 Condicion** «Sin DDJJ de vinculación presentada o actualizada» — El cliente no presentó declaración jurada sobre si es vinculado al intermediario o si su relación implica influencia controlante, o no actualizó la presentada. · tramo [exacta]: «que no hayan presentado declaración jurada sobre si revisten o no el carácter de vinculados»
- **x1 Excepcion** «Deudores en concurso o gestión judicial hasta 540 días» — Quedan fuera de la clasificación en Irrecuperable por falta de DDJJ los deudores en concurso, con APE solicitado o en gestión judicial que no presentaron la documentación por hasta 540 días desde la apertura, solicitud o inicio de gestiones. · umbral: ['por un período de hasta 540 días contados a partir de la apertura del concurso'] · tramo [exacta]: «con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial»
- **c3 Condicion** «Informe de abogado sobre razonabilidad del recupero» — Que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos. · tramo [exacta]: «siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero»
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: c2 Condicion —condicion_de→ op1 Operacion
- R: c3 Condicion —condicion_de→ x1 Excepcion
- R: op1 Operacion —aplica_a→ Sujeto_sector_privado_no_financiero (mención «Clientes del sector privado no financiero»)
- R: x1 Excepcion —aplica_a→ Sujeto_deudor (mención «los deudores»)
- Omisión `relacion_sin_predicado` [exacta]: «con excepción de los deudores en concurso» — La excepción recae sobre la Operacion de clasificación; exceptua solo admite Restriccion.
- Omisión `fuera_de_tipos` [exacta]: «Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2.» — Salvedad de compatibilidad con el régimen de previsiones; sin tipo adecuado.

### K — supuestos a clasificar

- 1. «deuda de más del 2,5 % de la RPC o del importe de referencia» → candidatos: c1 Condicion (1.00), op1 Operacion (0.50)
- 2. «excepción de concurso hasta 540 días» → candidatos: x1 Excepcion (1.00)
- 3. «siempre que haya informe» → candidatos: c3 Condicion (0.67)
- 4. «primera declaración» → candidatos: op1 Operacion (1.00), c2 Condicion (0.50)
- 5. «actualizaciones» → candidatos: op1 Operacion (1.00)

### K — omisiones de T4 a clasificar

- con_marca:26 → entidades: — | omisiones: om#1 fuera_de_tipos [exacta] solap 0.69

## Código W

- **c1 Condicion** «Deuda superior al 2,5 % RPC — indicador Irrecuperable» — Indicador (alternativo) para clasificar en categoría Irrecuperable: clientes del sector privado no financiero cuya deuda por todo concepto más la financiación solicitada, al momento de su otorgamiento, exceda el 2,5 % de la RPC de la entidad del último día del mes anterior o el importe de referencia del punto 3.7., el menor de ambos. · props: `{"umbrales": [{"tramo": "el equivalente al importe de referencia establecido en el punto 3.7., de ambos el menor", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['exceda del 2,5 % de la responsabilidad patrimonial computable', 'el equivalente al importe de referencia establecido en el punto 3.7., de ambos e…'] · tramo [exacta]: «Clientes del sector privado no financiero, cuya deuda (por todo concepto) más el»
- **c2 Condicion** «Falta de DDJJ de vinculación — indicador Irrecuperable» — Supuesto concurrente del indicador para categoría Irrecuperable: que el cliente no haya presentado declaración jurada sobre si es vinculado al intermediario financiero o si su relación implica influencia controlante, o no la haya actualizado. El tratamiento rige desde el otorgamiento (primera declaración) o desde el 1.12 (actualizaciones) hasta el mes anterior a la presentación. · tramo [exacta]: «que no hayan presentado declaración jurada sobre si revisten o no el carácter de vinculados»
- **x1 Excepcion** «Deudores en concurso o gestión judicial — exclusión» — Quedan exceptuados de la clasificación en Irrecuperable por este indicador los deudores en concurso, con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, por hasta 540 días desde la apertura/solicitud/inicio, no hubiesen presentado la documentación. · umbral: ['por un período de hasta 540 días'] · tramo [exacta]: «con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial»
- **c3 Condicion** «Informe de abogado sobre recupero — condición excepción» — La excepción rige siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos. · tramo [no]: «siempre que se cuente con informe de abo-gado de la entidad financiera acreedora»
- R: c3 Condicion —condicion_de→ x1 Excepcion
- R: x1 Excepcion —aplica_a→ Sujeto_deudor (mención «los deudores»)
- Omisión `fuera_de_tipos` [exacta]: «Este tratamiento se aplicará desde la fecha de otorgamiento de la asistencia,» — Ámbito temporal del tratamiento; recogido en la descripción de c2, sin tipo propio.

### W — supuestos a clasificar

- 1. «deuda de más del 2,5 % de la RPC o del importe de referencia» → candidatos: c1 Condicion (1.00)
- 2. «excepción de concurso hasta 540 días» → candidatos: x1 Excepcion (1.00), c3 Condicion (0.25)
- 3. «siempre que haya informe» → candidatos: c3 Condicion (0.67), c2 Condicion (0.33)
- 4. «primera declaración» → candidatos: c2 Condicion (1.00)
- 5. «actualizaciones» → candidatos: c2 Condicion (1.00)

### W — omisiones de T4 a clasificar

- con_marca:26 → entidades: — | omisiones: —

