# `cla::6.5.3.10` — Mantenga arreglos privados con la entidad financiera que cuenten con la opi-

Grupos: grupo_c. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.3. Con problemas.
> *heredado:* El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos, esos problemas pueden resultar en una pérdida para la entidad financiera. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *propio:* 6.5.3.10. Mantenga arreglos privados con la entidad financiera que cuenten con la opinión del auditor externo de la entidad sobre la factibilidad del cumplimiento de la refinanciación, cuando aún no se haya cancelado el 15 % del importe involucrado en el citado acuerdo y siempre que dicho acuerdo se haya alcanzado cuando el deudor se encontraba categorizado en los niveles "con alto riesgo de insolvencia" o "irrecuperable". A fin de determinar el importe de la cancelación, se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deudor –con excepción de las hipotecas sobre inmuebles rurales que, por lo tanto, serán computables–, observando los márgenes de cobertura establecidos en las normas sobre "Garantías". Será requisito indispensable, además, contar con la opinión favorable sobre la calidad de las garantías, formulada por el auditor externo. En los casos de acuerdos superiores al equivalente a 2,5 veces el importe de referencia establecido en el punto 3.7., la reclasificación inicial del cliente a esta categoría podrá realizarse siempre que no medie objeción por parte de la SEFyC, a la cual, previamente, se deberá plantear cada situación en forma individual.

## Supuestos de la fase A de T4 (M1)

1. «sin cancelar el 15 %»
2. «acuerdo alcanzado en alto riesgo o irrecuperable»
3. «acuerdos de más de 2,5 veces el importe de referencia»

## Código A

- **d1 Definicion** «Indicador: arreglos privados con opinión del auditor» — Indicador de la categoría 'Con problemas': el cliente mantiene arreglos privados con la entidad financiera que cuentan con la opinión del auditor externo de la entidad sobre la factibilidad del cumplimiento de la refinanciación, cuando aún no se haya cancelado el 15 % del importe involucrado y siempre que el acuerdo se haya alcanzado cuando el deudor estaba categorizado 'con alto riesgo de insolve… · props: `{"termino": "arreglos privados con opinión del auditor externo"}` · tramo [exacta]: «Entre los indicadores que pueden reflejar esta situación se destacan que el cliente: […] Mantenga arreglos privados con la entidad financiera que cuenten con la opinión del auditor externo de la entidad sobre la factibilidad del cumplimiento de la refinanciación»
- **c1 Condicion** «Cancelación inferior al 15 % del importe del acuerdo» — Aún no se ha cancelado el 15 % del importe involucrado en el acuerdo de refinanciación. · umbral: ['cuando aún no se haya cancelado el 15 % del importe involucrado'] · tramo [exacta]: «cuando aún no se haya cancelado el 15 % del importe involucrado en el citado acuerdo»
- **c2 Condicion** «Acuerdo alcanzado con deudor en alto riesgo o irrecuperable» — El acuerdo se alcanzó cuando el deudor se encontraba categorizado como 'con alto riesgo de insolvencia' o 'irrecuperable'. · tramo [exacta]: «siempre que dicho acuerdo se haya alcanzado cuando el deudor se encontraba categorizado en los niveles "con alto riesgo de insolvencia" o "irrecuperable"»
- **p1 Potestad** «Computar 50 % de garantías adicionales» — A fin de determinar el importe de la cancelación, se admite computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deudor (las hipotecas sobre inmuebles rurales son computables), observando los márgenes de cobertura de las normas sobre 'Garantías'. · tramo [exacta]: «se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deudor»
- **c3 Condicion** «Opinión favorable del auditor sobre garantías» — Requisito indispensable para computar las garantías adicionales: contar con la opinión favorable del auditor externo sobre la calidad de las garantías. · tramo [exacta]: «Será requisito indispensable, además, contar con la opinión favorable sobre la calidad de las garantías, formulada por el auditor externo.»
- **p2 Potestad** «Reclasificación inicial sin objeción de la SEFyC» — En acuerdos superiores a 2,5 veces el importe de referencia del punto 3.7., la reclasificación inicial del cliente a esta categoría podrá realizarse siempre que no medie objeción de la SEFyC. · tramo [no]: «la reclasificación inicial del cliente a estta categoría podrá realizarse siempre que no medie objeción por parte de la SEFyC»
- **c4 Condicion** «Acuerdo superior a 2,5 veces el importe de referencia» — El acuerdo es superior al equivalente a 2,5 veces el importe de referencia establecido en el punto 3.7. · umbral: ['acuerdos superiores al equivalente a 2,5 veces el importe de referencia establec…'] · tramo [exacta]: «En los casos de acuerdos superiores al equivalente a 2,5 veces el importe de referencia establecido en el punto 3.7.»
- **c5 Condicion** «Sin objeción de la SEFyC» — No media objeción de la SEFyC a la reclasificación inicial del cliente. · tramo [exacta]: «siempre que no medie objeción por parte de la SEFyC»
- **o1 Obligacion** «Plantear cada situación individual a la SEFyC» — En los acuerdos superiores a 2,5 veces el importe de referencia, previamente a la reclasificación se deberá plantear cada situación en forma individual a la SEFyC. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «a la cual, previamente, se deberá plantear cada situación en forma individual»
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: c4 Condicion —condicion_de→ p2 Potestad
- R: c5 Condicion —condicion_de→ p2 Potestad

### A — supuestos a clasificar

- 1. «sin cancelar el 15 %» → candidatos: c1 Condicion (0.50), d1 Definicion (0.50)
- 2. «acuerdo alcanzado en alto riesgo o irrecuperable» → candidatos: c2 Condicion (1.00), d1 Definicion (1.00), c1 Condicion (0.20), c4 Condicion (0.20)
- 3. «acuerdos de más de 2,5 veces el importe de referencia» → candidatos: c4 Condicion (1.00), o1 Obligacion (1.00), p2 Potestad (1.00), c1 Condicion (0.17)

## Código H

- **c1 Condicion** «Indicador: arreglo privado con opinión de auditor, cancelado <15 %» — Indicador de la categoría 'Con problemas' (norma del encabezado 6.5.3): el cliente mantiene arreglos privados con la entidad financiera que cuentan con la opinión del auditor externo sobre la factibilidad del cumplimiento de la refinanciación, cuando aún no se ha cancelado el 15 % del importe involucrado en el acuerdo. · umbral: ['cuando aún no se haya cancelado el 15 % del importe involucrado en el citado acu…'] · tramo [exacta]: «Mantenga arreglos privados con la entidad financiera que cuenten con la opinión del auditor externo de la entidad sobre la factibilidad del cumplimiento de la refinanciación, cuando aún no se haya cancelado el 15 % del importe involucrado en el citado acuerdo»
- **c2 Condicion** «Acuerdo alcanzado en categoría alto riesgo o irrecuperable» — Supuesto adicional del indicador de arreglos privados: el acuerdo se alcanzó cuando el deudor estaba categorizado como 'con alto riesgo de insolvencia' o 'irrecuperable'. · tramo [exacta]: «siempre que dicho acuerdo se haya alcanzado cuando el deudor se encontraba categorizado en los niveles "con alto riesgo de insolvencia" o "irrecuperable"»
- **p1 Potestad** «Cómputo del 50 % de garantías adicionales» — A fin de determinar el importe de la cancelación, se admite computar el 50 % de las garantías adicionales a las originalmente ofrecidas, constituidas sobre bienes no vinculados a la explotación del deudor (las hipotecas sobre inmuebles rurales son computables), observando los márgenes de cobertura de las normas sobre 'Garantías'. · tramo [exacta]: «se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deudor»
- **o1 Condicion** «Opinión favorable del auditor sobre calidad de garantías» — Requisito indispensable para computar las garantías adicionales: contar con la opinión favorable del auditor externo sobre la calidad de las garantías. · tramo [exacta]: «Será requisito indispensable, además, contar con la opinión favorable sobre la calidad de las garantías, formulada por el auditor externo.»
- **p2 Potestad** «Reclasificación inicial sin objeción de SEFyC» — En acuerdos superiores a 2,5 veces el importe de referencia del punto 3.7., la reclasificación inicial del cliente a la categoría 'Con problemas' podrá realizarse siempre que no medie objeción de la SEFyC. · tramo [exacta]: «la reclasificación inicial del cliente a esta categoría podrá realizarse siempre que no medie objeción por parte de la SEFyC»
- **c3 Condicion** «Acuerdo superior a 2,5 veces importe de referencia» — Supuesto: el acuerdo supera el equivalente a 2,5 veces el importe de referencia del punto 3.7. · umbral: ['superiores al equivalente a 2,5 veces el importe de referencia establecido en el…'] · tramo [exacta]: «En los casos de acuerdos superiores al equivalente a 2,5 veces el importe de referencia establecido en el punto 3.7.»
- **c4 Condicion** «No media objeción de la SEFyC» — Supuesto: no media objeción de la SEFyC a la reclasificación inicial del cliente. · tramo [exacta]: «siempre que no medie objeción por parte de la SEFyC»
- **ob1 Obligacion** «Plantear previamente cada situación a la SEFyC» — En los acuerdos superiores a 2,5 veces el importe de referencia, se deberá plantear previamente a la SEFyC cada situación en forma individual. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «a la cual, previamente, se deberá plantear cada situación en forma individual»
- R: c3 Condicion —condicion_de→ p2 Potestad
- R: c4 Condicion —condicion_de→ p2 Potestad
- R: o1 Condicion —condicion_de→ p1 Potestad
- R: p2 Potestad —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: ob1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: p1 Potestad —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)

### H — supuestos a clasificar

- 1. «sin cancelar el 15 %» → candidatos: c1 Condicion (0.50)
- 2. «acuerdo alcanzado en alto riesgo o irrecuperable» → candidatos: c2 Condicion (1.00), c1 Condicion (0.20), c3 Condicion (0.20)
- 3. «acuerdos de más de 2,5 veces el importe de referencia» → candidatos: c3 Condicion (1.00), ob1 Obligacion (1.00), p2 Potestad (1.00), c1 Condicion (0.33)

## Código K

- **c1 Condicion** «Arreglos privados con opinión del auditor — indicador con problemas» — Indicador de la categoría 'con problemas' (cartera comercial): el cliente mantiene arreglos privados con la entidad financiera que cuentan con la opinión del auditor externo de la entidad sobre la factibilidad del cumplimiento de la refinanciación. · tramo [exacta]: «Mantenga arreglos privados con la entidad financiera que cuenten con la opinión del auditor externo de la entidad sobre la factibilidad del cumplimiento de la refinanciación»
- **c2 Condicion** «No cancelado 15 % del acuerdo — indicador con problemas» — Supuesto del indicador de la categoría 'con problemas': aún no se canceló el 15 % del importe involucrado en el arreglo privado. · umbral: ['aún no se haya cancelado el 15 % del importe involucrado en el citado acuerdo'] · tramo [exacta]: «cuando aún no se haya cancelado el 15 % del importe involucrado en el citado acuerdo»
- **c3 Condicion** «Acuerdo alcanzado en alto riesgo o irrecuperable» — Supuesto del indicador de la categoría 'con problemas': el acuerdo se alcanzó cuando el deudor estaba categorizado 'con alto riesgo de insolvencia' o 'irrecuperable'. · tramo [exacta]: «siempre que dicho acuerdo se haya alcanzado cuando el deudor se encontraba categorizado en los niveles "con alto riesgo de insolvencia" o "irrecuperable"»
- **p1 Potestad** «Cómputo 50 % garantías adicionales — importe de cancelación» — Para determinar el importe cancelado del acuerdo se admite computar el 50 % de las garantías adicionales a las originalmente ofrecidas, constituidas sobre bienes no vinculados a la explotación del deudor, observando los márgenes de cobertura de las normas sobre 'Garantías'. · tramo [exacta]: «A fin de determinar el importe de la cancelación, se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deudor»
- **x1 Excepcion** «Hipotecas sobre inmuebles rurales computables» — Exceptúa del requisito de que las garantías computables recaigan sobre bienes no vinculados a la explotación del deudor a las hipotecas sobre inmuebles rurales, que son computables. · tramo [exacta]: «con excepción de las hipotecas sobre inmuebles rurales que, por lo tanto, serán computables»
- **c4 Condicion** «Opinión favorable del auditor sobre garantías» — Requisito indispensable para computar las garantías: opinión favorable del auditor externo sobre su calidad. · tramo [exacta]: «Será requisito indispensable, además, contar con la opinión favorable sobre la calidad de las garantías, formulada por el auditor externo.»
- **op1 Operacion** «Reclasificación inicial a categoría con problemas» — Reclasificación inicial del cliente a la categoría 'con problemas' por acuerdos superiores a 2,5 veces el importe de referencia. · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «la reclasificación inicial del cliente a esta categoría podrá realizarse»
- **c5 Condicion** «Acuerdos superiores a 2,5 veces importe referencia» — Acuerdos superiores al equivalente a 2,5 veces el importe de referencia del punto 3.7. · umbral: ['superiores al equivalente a 2,5 veces el importe de referencia establecido en el…'] · tramo [exacta]: «En los casos de acuerdos superiores al equivalente a 2,5 veces el importe de referencia establecido en el punto 3.7.»
- **c6 Condicion** «No objeción de la SEFyC» — La reclasificación inicial puede realizarse siempre que no medie objeción de la SEFyC. · tramo [exacta]: «siempre que no medie objeción por parte de la SEFyC»
- **o1 Obligacion** «Planteo previo individual a SEFyC — reclasificación» — En acuerdos superiores a 2,5 veces el importe de referencia, se debe plantear previamente a la SEFyC cada situación en forma individual antes de la reclasificación inicial. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «a la cual, previamente, se deberá plantear cada situación en forma individual»
- R: c4 Condicion —condicion_de→ p1 Potestad
- R: c5 Condicion —condicion_de→ op1 Operacion
- R: c6 Condicion —condicion_de→ op1 Operacion
- R: c5 Condicion —condicion_de→ o1 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: p1 Potestad —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: Sujeto_entidad_financiera (mención «la entidad financiera») —ejecuta→ op1 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «con excepción de las hipotecas sobre inmuebles rurales» — La excepción relaja el alcance de una Potestad; exceptua solo admite Restriccion/Obligacion.

### K — supuestos a clasificar

- 1. «sin cancelar el 15 %» → candidatos: c2 Condicion (0.50)
- 2. «acuerdo alcanzado en alto riesgo o irrecuperable» → candidatos: c3 Condicion (1.00), c2 Condicion (0.20), p1 Potestad (0.20)
- 3. «acuerdos de más de 2,5 veces el importe de referencia» → candidatos: c5 Condicion (1.00), o1 Obligacion (1.00), op1 Operacion (1.00), c2 Condicion (0.17)

## Código W

- **e1 Condicion** «Arreglos privados con opinión del auditor externo — indicador con problemas» — Indicador de la situación 'con problemas' (cartera comercial): el cliente mantiene arreglos privados con la entidad financiera que cuentan con la opinión del auditor externo de la entidad sobre la factibilidad del cumplimiento de la refinanciación. Es uno de los indicadores que pueden reflejar la situación (no se exigen todos). · tramo [exacta]: «Entre los indicadores que pueden reflejar esta situación se destacan que el cliente: […] Mantenga arreglos privados con la entidad financiera que cuenten con la opinión del auditor externo de la entidad sobre la factibilidad del cumplimiento de la refinanciación»
- **e2 Condicion** «Cancelación menor al 15 % del acuerdo» — Que aún no se haya cancelado el 15 % del importe involucrado en el acuerdo privado. · umbral: ['aún no se haya cancelado el 15 % del importe involucrado en el citado acuerdo'] · tramo [exacta]: «cuando aún no se haya cancelado el 15 % del importe involucrado en el citado acuerdo»
- **e3 Condicion** «Acuerdo alcanzado con deudor en alto riesgo o irrecuperable» — Que el acuerdo se haya alcanzado cuando el deudor estaba categorizado 'con alto riesgo de insolvencia' o 'irrecuperable'. · tramo [exacta]: «siempre que dicho acuerdo se haya alcanzado cuando el deudor se encontraba categorizado en los niveles "con alto riesgo de insolvencia" o "irrecuperable"»
- **e4 Potestad** «Cómputo 50 % garantías adicionales — importe de cancelación» — Para determinar el importe de la cancelación se admite computar el 50 % de las garantías adicionales a las originales, constituidas sobre bienes no vinculados a la explotación del deudor (las hipotecas sobre inmuebles rurales sí son computables), observando los márgenes de cobertura de las normas sobre Garantías. · tramo [exacta]: «se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente»
- **e5 Condicion** «Opinión favorable del auditor externo sobre garantías» — Requisito indispensable para computar las garantías adicionales: opinión favorable del auditor externo sobre la calidad de las garantías. · tramo [exacta]: «Será requisito indispensable, además, contar con la opinión favorable sobre la calidad de las garantías, formulada por el auditor externo.»
- **e6 Operacion** «Reclasificación inicial a 'con problemas' por acuerdos» — Reclasificación inicial del cliente a la categoría 'con problemas' por acuerdos superiores a 2,5 veces el importe de referencia del punto 3.7. · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «la reclasificación inicial del cliente a esta categoría»
- **e7 Condicion** «Acuerdos superiores a 2,5 veces importe de referencia» — Acuerdos superiores al equivalente a 2,5 veces el importe de referencia del punto 3.7. · umbral: ['superiores al equivalente a 2,5 veces el importe de referencia establecido en el…'] · tramo [exacta]: «En los casos de acuerdos superiores al equivalente a 2,5 veces el importe de referencia establecido en el punto 3.7.»
- **e8 Condicion** «Sin objeción de la SEFyC» — Que no medie objeción de la SEFyC para la reclasificación inicial. · tramo [exacta]: «siempre que no medie objeción por parte de la SEFyC»
- **e9 Obligacion** «Planteo individual previo a la SEFyC — reclasificación» — En acuerdos superiores a 2,5 veces el importe de referencia, plantear previamente a la SEFyC cada situación en forma individual antes de la reclasificación inicial. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «a la cual, previamente, se deberá plantear cada situación en forma individual»
- R: e5 Condicion —condicion_de→ e4 Potestad
- R: e7 Condicion —condicion_de→ e6 Operacion
- R: e8 Condicion —condicion_de→ e6 Operacion
- R: e7 Condicion —condicion_de→ e9 Obligacion
- R: e9 Obligacion —condiciona→ e6 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «cuando aún no se haya cancelado el 15 % del importe involucrado en el citado acuerdo» — Condición que acota otra Condicion (el indicador); condicion_de no admite Condicion como rango.
- Omisión `relacion_sin_predicado` [exacta]: «siempre que dicho acuerdo se haya alcanzado» — Condición que acota otra Condicion; condicion_de no admite Condicion como rango.

### W — supuestos a clasificar

- 1. «sin cancelar el 15 %» → candidatos: e2 Condicion (0.50)
- 2. «acuerdo alcanzado en alto riesgo o irrecuperable» → candidatos: e3 Condicion (1.00), e2 Condicion (0.20)
- 3. «acuerdos de más de 2,5 veces el importe de referencia» → candidatos: e6 Operacion (1.00), e7 Condicion (1.00), e9 Obligacion (1.00), e2 Condicion (0.17)

