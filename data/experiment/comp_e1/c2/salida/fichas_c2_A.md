# Fichas de C2 — código A

Lectura cegada (primera lectura de la instancia). El código no dice el brazo ni la corrida; la tabla sigue cerrada hasta la adjudicación. Clases de M1 y M2: `c0/reglas_lectura_c0.md`.

## `cap::10.3.1.1` — Se asignarán las calificaciones de las ECAI admisibles a los ponderadores de

Grupos: omisiones.

### Texto

> *heredado:* Sección 10. Agentes de calificación externa (ECAI).
> *heredado:* 10.3. Consideraciones para su implementación.
> *heredado:* 10.3.1. Proceso de asignación de calificaciones (mapping).
> *propio:* 10.3.1.1. Se asignarán las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4.; es decir, las entidades financieras deberán establecer qué calificaciones o categorías de evaluación corresponden a esos ponderadores de riesgo. El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en esas calificaciones. Además, deberá abarcar todos los ponderadores de riesgo previstos en esos puntos.

### Extracción (código A)

- **op1 Operacion** «Asignación (mapping) de calificaciones ECAI a ponderadores de riesgo» — Proceso de asignación (mapping) de las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «Se asignarán las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4.»
- **ob1 Obligacion** «Establecer calificaciones ECAI correspondientes a cada ponderador» — Las entidades financieras deben establecer qué calificaciones o categorías de evaluación de las ECAI admisibles corresponden a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «las entidades financieras deberán establecer qué calificaciones o categorías de evaluación corresponden a esos ponderadores de riesgo»
- **ob2 Obligacion** «Mapping objetivo y con distribución coherente» — El proceso de asignación (mapping) debe ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en las calificaciones. · props: `{"tipo": "otra"}` · tramo [exacta]: «El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en esas calificaciones.»
- **ob3 Obligacion** «Mapping debe abarcar todos los ponderadores de riesgo» — El proceso de asignación (mapping) debe abarcar todos los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "otra"}` · tramo [exacta]: «Además, deberá abarcar todos los ponderadores de riesgo previstos en esos puntos.»
- R: ob1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:10 | sí | «es decir, las entidades financieras deberán establecer qué calificaciones o categorías de evaluación corresponden a esos ponderadores de riesgo» | `extraida_tramo_verificado` |  | Obligacion (ob1/o1) con tramo [exacta] igual al tramo omitido |

## `cap::2.1` — Exigencia.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 2. Capital mínimo por riesgo de crédito.
> *heredado:* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
> *heredado:* (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de importancia sistémica global (G-SIB).
> *heredado:* ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
> *propio:* 2.1. Exigencia. Se determinará aplicando la siguiente expresión: C = (k x 0,08 x APR ) + INC RC C donde: C : exigencia de capital por riesgo de crédito. RC k: factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por la SEFYC, teniendo en cuenta la siguiente escala: [TABLA cap::tabla001 | página 7 | e0_tablas | columnas] Columnas: Calificación asignada | Valor de "k" Fila 1: Calificación asignada = 1 | Valor de "k" = 1 Fila 2: Calificación asignada = 2 | Valor de "k" = 1,03 Fila 3: Calificación asignada = 3 | Valor de "k" = 1,08 Fila 4: Calificación asignada = 4 | Valor de "k" = 1,13 Fila 5: Calificación asignada = 5 | Valor de "k" = 1,19 [FIN TABLA cap::tabla001] A este efecto, se considerará la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación. En tanto no se comunique, el valor de "k" será igual a 1,03. APR : activos ponderados por riesgo de crédito, determinados mediante la suma de los valores C obtenidos luego de aplicar la siguiente expresión: A x p + PFB x CCF x p + no DvP + (DVP + RCD + INC(inversiones empresas)) x 12,5 significativas en donde: A: activos computables/exposiciones. PFB: partidas fuera de balance (conceptos computables no registrados en el balance de saldos). CCF: factor de conversión crediticia. p: ponderador de riesgo, en tanto por uno. no DvP: operaciones sin entrega contra pago. Importe determinado mediante la suma de los valores obtenidos luego de aplicar a las operaciones comprendidas el correspondiente ponderador de riesgo (p) conforme a lo dispuesto en el punto 4.1. DvP: operaciones de entrega contra pago fallidas (a los efectos de estas normas, incluyen las operaciones de pago contra pago –PvP– fallidas). Importe determinado mediante la suma de los valores obtenidos luego de multiplicar la exposición actual positiva por la exigencia de capital aplicable establecida en el punto 4.1. RCD: exigencia por riesgo de crédito de contraparte en operaciones con derivados extrabursátiles (over-the-counter, OTC), determinada conforme a lo establecido en el punto 4.2. INC(inversiones empresas): incremento por los excesos a los siguientes límites: significativas en – participación en el capital de cada empresa: 15%; – total de participaciones en el capital de empresas: 60%. Los límites máximos establecidos se aplicarán sobre la responsabilidad patrimonial computable (RPC) de la entidad financiera del último día anterior al que corresponda. INC: incremento por los siguientes excesos: – en la relación de activos inmovilizados y otros conceptos (Sección 4. del respectivo TO), excluidos los computados para la determinación del INC(inversiones significativas en empresas); – a los límites establecidos en el TO sobre Financiamiento al Sector Público no Financiero, excluidos los computados para la determinación del INC(inversiones significativas en empresas); – a los límites establecidos en el TO sobre Grandes Exposiciones al Riesgo de Crédito –según lo previsto en el acápite ii), punto 2.1. del TO sobre Incumplimientos de Capitales Mínimos y Relaciones Técnicas. Criterios Aplicables–, excluidos los computados para la determinación del INC(inversiones empresas); significativas en – a los límites de graduación del crédito (Sección 3. del respectivo TO); y – al límite de derivados sobre materias primas o productos básicos –commodities– previsto en el punto 1.2. del TO sobre Operaciones al Contado a Liquidar y a Término, Pases, Cauciones, Otros Derivados y con Fondos Comunes de Inversión. En la materia, serán de aplicación las disposiciones contenidas en la Sección 2. del TO sobre Incumplimientos de Capitales Mínimos y Relaciones Técnicas. Criterios Aplicables, salvo que resulte aplicable lo previsto en la Sección 3. de esas normas. También se computará en esta expresión la exposición crediticia resultante de la utilización de los cupos crediticios ampliados a que se refieren los puntos 6.1.1.2. y 6.1.2.1. –acápite d)– del TO sobre Financiamiento al Sector Público no Financiero (considerando, en su caso, lo establecido en la Sección 9. de las citadas normas) respecto de la asistencia financiera otorgada y/o las tenencias de instrumentos de deuda de fideicomisos financieros o fondos fiduciarios a que se refiere el punto 5.1. del TO sobre Financiamiento al Sector Público no Financiero y el punto 3.2.4. del citado ordenamiento computadas conforme al siguiente cronograma, el cual operará a partir de que se hayan comenzado a utilizar económicamente las obras o el equipamiento genere ingresos al fideicomiso o fondo fiduciario a través de tarifas, tasas, aranceles u otros conceptos similares. Cómputo como INC del uso del cupo A partir del ampliado –en % de dicha utilización– 25 Primer mes 50 Séptimo mes 100 Décimo tercer mes El sector público no financiero citado en estas normas es aquel definido en la Sección 1. del TO sobre Financiamiento al Sector Público no Financiero.

### Extracción (código A)

- **op1 Operacion** «Determinación exigencia capital por riesgo de crédito» — Cálculo de la exigencia de capital por riesgo de crédito (C RC) mediante la expresión C = (k x 0,08 x APR C) + INC, con k según la calificación asignada por la SEFYC. · props: `{"tipo": "calculo"}` · tramo [exacta]: «Se determinará aplicando la siguiente expresión:»
- **ob1 Obligacion** «Cálculo exigencia capital riesgo de crédito» — La exigencia de capital por riesgo de crédito se determina con la expresión C = (k x 0,08 x APR) + INC; k es el factor vinculado a la calificación asignada por la SEFYC según la escala: 1→1; 2→1,03; 3→1,08; 4→1,13; 5→1,19. · props: `{"tipo": "calculo"}` · tramo [exacta]: «Se determinará aplicando la siguiente expresión:»
- **ob2 Obligacion** «Última calificación informada para el cálculo de k» — Se considera la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación. · props: `{"tipo": "calculo", "umbrales": [{"tramo": "al tercer mes siguiente a aquel en que tenga lugar la\nnotificación", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['al tercer mes siguiente a aquel en que tenga lugar la notificación'] · tramo [exacta]: «se considerará la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación»
- **ob3 Obligacion** «k igual a 1,03 sin calificación comunicada» — En tanto no se comunique la calificación, el valor de k es 1,03. · props: `{"tipo": "calculo", "umbrales": [{"tramo": "el valor de “k” será igual a 1,03", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['el valor de "k" será igual a 1,03'] · tramo [exacta]: «En tanto no se comunique, el valor de "k" será igual a 1,03.»
- **ob4 Obligacion** «Cálculo de APR por riesgo de crédito» — Los activos ponderados por riesgo de crédito se determinan sumando los valores obtenidos al aplicar la expresión de activos, partidas fuera de balance, operaciones no DvP, DvP, RCD e INC de inversiones significativas en empresas. · props: `{"tipo": "calculo"}` · tramo [exacta]: «APR : activos ponderados por riesgo de crédito, determinados mediante la suma de los valores C obtenidos luego de aplicar la siguiente expresión:»
- **ob5 Obligacion** «INC por excesos a límites de inversiones en empresas» — Se computa un incremento por los excesos a los límites de participación en el capital de empresas, aplicados sobre la RPC del último día anterior al que corresponda. · props: `{"tipo": "calculo"}` · umbral: ['participación en el capital de cada empresa: 15%', 'total de participaciones en el capital de empresas: 60%'] · tramo [exacta]: «INC(inversiones empresas): incremento por los excesos a los siguientes límites:»
- **ob6 Obligacion** «INC por excesos a otros límites» — Se computa un incremento por los excesos en la relación de activos inmovilizados, límites de Financiamiento al Sector Público no Financiero, Grandes Exposiciones, graduación del crédito y derivados sobre commodities, excluidos los computados en INC de inversiones significativas en empresas. · props: `{"tipo": "calculo"}` · tramo [exacta]: «INC: incremento por los siguientes excesos:»
- **ob7 Obligacion** «Cómputo del uso de cupos crediticios ampliados como INC» — Se computa como INC la exposición crediticia por el uso de cupos crediticios ampliados respecto de asistencia a fideicomisos financieros o fondos fiduciarios, según cronograma: 25% primer mes, 50% séptimo mes, 100% décimo tercer mes, a partir de la utilización económica de las obras o generación de ingresos. · props: `{"tipo": "calculo", "umbrales": [{"tramo": "25 Primer mes", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "50 Séptimo mes", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "100 Décimo tercer mes", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['25 Primer mes', '50 Séptimo mes', '100 Décimo tercer mes'] · tramo [exacta]: «También se computará en esta expresión la exposición crediticia resultante de la utilización de los cupos crediticios ampliados»
- **def1 Definicion** «Sector público no financiero» — Es el definido en la Sección 1 del TO sobre Financiamiento al Sector Público no Financiero. · props: `{"termino": "sector público no financiero"}` · tramo [exacta]: «El sector público no financiero citado en estas normas es aquel definido en la Sección 1. del TO sobre Financiamiento al Sector Público no Financiero.»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion
- R: ob4 Obligacion —regula→ op1 Operacion
- Omisión `formula` [exacta]: «C = (k x 0,08 x APR ) + INC» — Fórmula no confiable; no se reconstruye.
- Omisión `formula` [exacta]: «A x p + PFB x CCF x p + no DvP + (DVP + RCD + INC(inversiones empresas)) x 12,5» — Fórmula de APR no confiable; no se reconstruye.
- Omisión `fuera_de_tipos` [exacta]: «En la materia, serán de aplicación las disposiciones contenidas en la Sección 2. del TO sobre Incumplimientos de Capitales Mínimos y Relaciones Técnicas. Criterios Aplicables, salvo que resulte aplicable lo previsto en la Sección 3. de esas normas.» — Remisión a otras normas; no se emite.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «en tanto no se comunique la calificación» | `dentro_de_norma` |  | dentro de la Obligacion ob3 («k igual a 1,03 sin calificación comunicada», tramo «En tanto no se comunique…»); sin Condicion |
| 2 | «el cronograma opera desde que las obras se usan económicamente» | `dentro_de_norma` |  | dentro de la Obligacion ob7 (descripción «a partir de la utilización económica de las obras»); sin Condicion |

## `cap::2.8.3.4` — En el caso de exposiciones minoristas a personas humanas, el total de los

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Capital mínimo por riesgo de crédito.
> *heredado:* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
> *heredado:* (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de importancia sistémica global (G-SIB).
> *heredado:* ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
> *heredado:* 2.8. Exposiciones minoristas.
> *heredado:* 2.8.3. Exposiciones minoristas normativas. Criterios.
> *propio:* 2.8.3.4. En el caso de exposiciones minoristas a personas humanas, el total de los vencimientos por las cuotas de todas las financiaciones de la entidad financiera que cuenten con amortización periódica –sin considerar las cuotas de créditos de otras entidades– no deberá exceder, al momento de los acuerdos, el 30% de los ingresos del deudor y/o, en su caso, de los codeudores. En consecuencia, los márgenes acordados para los descubiertos en cuenta corriente y los límites de compra de las tarjetas de crédito –en ambos casos, tanto el utilizado como el disponible–, así como los préstamos personales preacordados –en la medida en que aún no hayan sido formalizados ni desembolsados al cliente–, no formarán parte del numerador de la relación cuota/ingreso por no contar con una amortización periódica. Deberá considerarse dentro del concepto "cuotas" aquellas que el cliente tenga por compras financiadas en el marco del sistema de tarjeta de crédito. A los efectos de considerar en las exposiciones minoristas normativas a los créditos incorporados a través de una compra de cartera, se deberá contar con la información necesaria para verificar el cumplimiento de los criterios y límites detallados precedentemente.

### Extracción (código A)

- **op1 Operacion** «Financiaciones minoristas a personas humanas con amortización periódica» — Exposiciones minoristas a personas humanas: financiaciones de la entidad con amortización periódica, sin considerar cuotas de créditos de otras entidades, al momento de los acuerdos. · props: `{"tipo": "financiacion"}` · tramo [exacta]: «exposiciones minoristas a personas humanas, el total de los vencimientos por las cuotas de todas las financiaciones de la entidad financiera que cuenten con amortización periódica»
- **r1 Restriccion** «Tope 30% cuota/ingreso — minoristas a personas humanas» — En exposiciones minoristas a personas humanas, el total de los vencimientos por las cuotas de todas las financiaciones de la entidad con amortización periódica (sin considerar cuotas de créditos de otras entidades) no deberá exceder, al momento de los acuerdos, el 30% de los ingresos del deudor y/o de los codeudores. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['no deberá exceder, al momento de los acuerdos, el 30% de los ingresos del deudor…'] · tramo [exacta]: «no deberá exceder, al momento de los acuerdos, el 30% de los ingresos del deudor y/o, en su caso, de los codeudores»
- **d1 Definicion** «Numerador de la relación cuota/ingreso: exclusiones» — No forman parte del numerador los márgenes acordados para descubiertos en cuenta corriente y los límites de compra de tarjetas de crédito (utilizado y disponible), ni los préstamos personales preacordados aún no formalizados ni desembolsados, por no contar con amortización periódica. · props: `{"termino": "numerador de la relación cuota/ingreso"}` · tramo [exacta]: «los márgenes acordados para los descubiertos en cuenta corriente y los límites de compra de las tarjetas de crédito –en ambos casos, tanto el utilizado como el disponible–, así como los préstamos personales preacordados –en la medida en que aún no hayan sido formalizados ni desembolsados al cliente–, no formarán parte …»
- **o1 Obligacion** «Incluir cuotas de compras financiadas con tarjeta en 'cuotas'» — Deben considerarse dentro del concepto «cuotas» las que el cliente tenga por compras financiadas en el marco del sistema de tarjeta de crédito. · props: `{"tipo": "calculo"}` · tramo [exacta]: «Deberá considerarse dentro del concepto "cuotas" aquellas que el cliente tenga por compras financiadas en el marco del sistema de tarjeta de crédito.»
- **op2 Operacion** «Incorporación de créditos por compra de cartera a exposiciones minoristas normativas» — Consideración en las exposiciones minoristas normativas de los créditos incorporados a través de una compra de cartera. · props: `{"tipo": "compra de cartera"}` · tramo [exacta]: «considerar en las exposiciones minoristas normativas a los créditos incorporados a través de una compra de cartera»
- **o2 Obligacion** «Contar con información para verificar criterios — compra de cartera» — Para considerar en las exposiciones minoristas normativas los créditos incorporados por compra de cartera, se debe contar con la información necesaria para verificar el cumplimiento de los criterios y límites detallados precedentemente. · props: `{"tipo": "otra"}` · tramo [exacta]: «se deberá contar con la información necesaria para verificar el cumplimiento de los criterios y límites detallados precedentemente»
- R: r1 Restriccion —limita→ op1 Operacion
- R: o2 Obligacion —regula→ op2 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financie-ra»)
- R: o2 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «entidad financie-ra»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:7 | no | «En consecuencia» | `ausente` |  | ningún tramo contiene «En consecuencia» ni omisión que lo registre |

## `cap::3.1.1.5` — Las exposiciones subyacentes a la titulización podrán incluir, entre otros con-

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos.
> *heredado:* 3.1. Tratamiento de las titulizaciones.
> *heredado:* Se denomina "posición de titulización" a la exposición a una titulización (o retitulización), tradicional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes conceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos ("AssetBacked Securities", ABS) y bonos de titulización hipotecaria ("Mortgage-Backed Securities", MBS)–, mejoras crediticias, facilidades de liquidez, "swaps" de tasa de interés o de monedas y derivados de crédito. Las reservas ("reserve accounts"), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo también el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad económica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una determinada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> *heredado:* 3.1.1. Conceptos.
> *propio:* 3.1.1.5. Las exposiciones subyacentes a la titulización podrán incluir, entre otros conceptos: préstamos, compromisos asumidos por la entidad, posiciones de titulización, obligaciones negociables y acciones. El conjunto subyacente podrá incluir una o varias exposiciones.

### Extracción (código A)

- **d1 Definicion** «Exposiciones subyacentes a la titulización» — Pueden incluir, entre otros conceptos: préstamos, compromisos asumidos por la entidad, posiciones de titulización, obligaciones negociables y acciones. · props: `{"termino": "exposiciones subyacentes a la titulización"}` · tramo [exacta]: «Las exposiciones subyacentes a la titulización podrán incluir, entre otros conceptos: préstamos, compromisos asumidos por la entidad, posiciones de titulización, obligaciones negociables y acciones.»
- **d2 Definicion** «Conjunto subyacente» — El conjunto subyacente puede incluir una o varias exposiciones. · props: `{"termino": "conjunto subyacente"}` · tramo [exacta]: «El conjunto subyacente podrá incluir una o varias exposiciones.»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:29 | sí | «Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuen…» | `ausente` |  | ninguna entidad ni omisión cubre la oración del heredado |

## `cap::3.1.11.2` — Cálculo de las variables.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos.
> *heredado:* 3.1. Tratamiento de las titulizaciones.
> *heredado:* Se denomina "posición de titulización" a la exposición a una titulización (o retitulización), tradicional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes conceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos ("AssetBacked Securities", ABS) y bonos de titulización hipotecaria ("Mortgage-Backed Securities", MBS)–, mejoras crediticias, facilidades de liquidez, "swaps" de tasa de interés o de monedas y derivados de crédito. Las reservas ("reserve accounts"), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo también el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad económica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una determinada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> *heredado:* 3.1.11. Enfoque estandarizado.
> *heredado:* Los ponderadores de riesgo a aplicar a las posiciones de una titulización y a las exposiciones subyacentes de una retitulización para la determinación de la exigencia de capital se establecerán empleando las disposiciones de este punto. Las posiciones de titulización a las que no se les pueda aplicar el enfoque estandarizado deberán ser ponderadas al 1250 %.
> *propio:* 3.1.11.2. Cálculo de las variables. i) K . SA Es la exigencia de capital promedio de las exposiciones subyacentes; es decir, el ratio entre la suma de las exposiciones subyacentes ponderadas por riesgo y la suma de las exposiciones subyacentes, todo multiplicado por 8 %. El cálculo deberá reflejar los efectos de cualquier cobertura del riesgo de crédito que corresponda aplicar a las exposiciones subyacentes (individualmente o al conjunto). K es un porcentaje entre cero y cien; es SA decir, si el ponderador de riesgo medio ponderado fuera 100 %, K será SA igual a 8 %. Cuando la estructura involucre a un SPE, se considerará que todas las exposiciones del SPE vinculadas a la titulización integran el conjunto de activos subyacentes. Esto incluye a los activos en los que ha invertido el SPE, las reservas ("reserve accounts"), las cuentas de efectivo en garantía y los derechos frente a las contrapartes por "swaps" de tasa de interés o de moneda. No obstante, a los fines del cálculo de la exigencia de capital, la entidad podrá excluir del conjunto de activos subyacentes a las exposiciones del SPE si puede demostrar que el riesgo no afecta a su posición de titulización o, en su defecto, que el riesgo es insignificante porque, por ejemplo, ha sido mitigado. En el caso de las titulizaciones sintéticas a las que se aporten fondos, se deberán computar para el cálculo del K los montos recibidos por los insSA trumentos con vinculación crediticia ("credit linked note") u otros pasivos suscriptos por el SPE, cuando dichos importes sirvan como garantía del repago de la exposición titulizada en cuestión y el riesgo de incumplimiento esté sujeto a la asignación de pérdidas por tramos. Ello a menos que la entidad pueda demostrar que el riesgo de incumplimiento es insignificante. En los casos en los que la entidad haya constituido una previsión específica o tenga un descuento no reembolsable en el precio de compra de su exposición al conjunto de activos subyacentes, el cálculo de K deberá SA efectuarse usando el monto bruto de la exposición –es decir, sin deducir la previsión específica y/o el descuento no reembolsable en el precio de compra–. ii) W. La variable W es el ratio entre el monto nominal de las exposiciones subyacentes en mora y el monto nominal de las exposiciones subyacentes. Se consideran en mora a las exposiciones subyacentes cuando se verifiquen atrasos en los pagos de 90 días o más, estén sujetas a procedimientos de quiebra o concurso o en proceso de ejecución o consistan en bienes inmuebles adquiridos en defensa del crédito o se trate de exposiciones que se encuentren en situación de incumplimiento en los términos definidos en los contratos de titulización. En el caso de retitulizaciones cuya cartera subyacente consista en tramos de titulización y en otros activos, W será cero para las posiciones de titulización y la que corresponda según lo previsto en los dos párrafos precedentes para los activos subyacentes que no son titulizaciones, si los hubiera. iii) K . A K se obtiene a partir de K y W conforme a la siguiente expresión: A SA En el caso de retitulizaciones cuya cartera subyacente consista en tramos de titulización y en otros activos, se deberá calcular por separado el K coA rrespondiente a cada subconjunto aplicando W por separado de conformidad con lo previsto en el acápite ii). Consecuentemente, K para la exposiA ción a una retitulización será equivalente al promedio, ponderado por la exposición nominal, de los K correspondientes a cada subconjunto. A En caso de que se desconozca la situación de cumplimiento correspondiente al 5 % o menos de las exposiciones subyacentes, se deberá ajustar el cálculo de K de la siguiente manera: A Si la entidad no conociera la situación de cumplimiento para más del 5 % de la posición de titulización, ésta deberá ponderarse al 1250 %. iv) K . SSFA(KA) La exigencia de capital por unidad de posición de titulización, K , se SSFA(KA) calculará conforme a lo siguiente: donde: p = 0,5 si la titulización cumple con los criterios STC del punto 3.1.14. p = 1 si la titulización no cumple con los criterios STC del punto 3.1.14. p = 1,5 si se trata de una retitulización.

### Extracción (código A)

- **op_calc_ksa Operacion** «Cálculo de K_SA (exigencia de capital promedio subyacentes)» — Cálculo de K_SA: ratio entre la suma de exposiciones subyacentes ponderadas por riesgo y la suma de exposiciones subyacentes, multiplicado por 8 %, en el enfoque estandarizado de titulizaciones. · props: `{"tipo": "calculo"}` · tramo [exacta]: «Es la exigencia de capital promedio de las exposiciones subyacentes; es decir, el ratio entre la suma de las exposiciones subyacentes ponderadas por riesgo y la suma de las exposiciones subyacentes, todo multiplicado por 8 %.»
- **ob_ksa_cobertura Obligacion** «K_SA refleja efectos de cobertura del riesgo de crédito» — El cálculo de K_SA debe reflejar los efectos de cualquier cobertura del riesgo de crédito aplicable a las exposiciones subyacentes, individualmente o al conjunto. · props: `{"tipo": "calculo"}` · tramo [exacta]: «El cálculo deberá reflejar los efectos de cualquier cobertura del riesgo de crédito que corresponda aplicar a las exposiciones subyacentes (individualmente o al conjunto).»
- **def_ksa_rango Definicion** «K_SA es porcentaje entre cero y cien» — K_SA es un porcentaje entre cero y cien; si el ponderador de riesgo medio ponderado fuera 100 %, K_SA será igual a 8 %. · props: `{"termino": "K"}` · tramo [exacta]: «es un porcentaje entre cero y cien»
- **def_spe_activos Definicion** «Activos subyacentes incluyen exposiciones del SPE» — Cuando la estructura involucre a un SPE, todas las exposiciones del SPE vinculadas a la titulización integran el conjunto de activos subyacentes, incluyendo activos invertidos, reservas, cuentas de efectivo en garantía y derechos frente a contrapartes por swaps de tasa de interés o de moneda. · props: `{"termino": "conjunto de activos subyacentes"}` · tramo [exacta]: «Cuando la estructura involucre a un SPE, se considerará que todas las exposiciones del SPE vinculadas a la titulización integran el conjunto de activos subyacentes.»
- **pot_excluir_spe Potestad** «Excluir exposiciones del SPE del conjunto subyacente» — A los fines del cálculo de la exigencia de capital, la entidad puede excluir del conjunto de activos subyacentes las exposiciones del SPE si demuestra que el riesgo no afecta a su posición de titulización o que es insignificante. · tramo [exacta]: «la entidad podrá excluir del conjunto de activos subyacentes a las exposiciones del SPE si puede demostrar que el riesgo no afecta a su posición de titulización o, en su defecto, que el riesgo es insignificante porque, por ejemplo, ha sido mitigado»
- **cond_excluir_demuestra Condicion** «Demostrar riesgo no afecta o insignificante» — La entidad puede demostrar que el riesgo del SPE no afecta a su posición de titulización o que es insignificante (por ejemplo, mitigado). · tramo [exacta]: «si puede demostrar que el riesgo no afecta a su posición de titulización o, en su defecto, que el riesgo es insignificante»
- **ob_sintetica_fondos Obligacion** «Computar montos de CLN en K_SA (sintéticas con fondos)» — En titulizaciones sintéticas a las que se aporten fondos, se computan para K_SA los montos recibidos por instrumentos con vinculación crediticia u otros pasivos suscriptos por el SPE, cuando sirvan como garantía del repago y el riesgo de incumplimiento esté sujeto a asignación de pérdidas por tramos, salvo que se demuestre que el riesgo es insignificante. · props: `{"tipo": "calculo"}` · tramo [no]: «se deberán computar para el cálculo del K los montos recibidos por los instrumentos con vinculación crediticia ("credit linked note") u otros pasivos suscriptos por el SPE»
- **cond_sintetica_garantia Condicion** «Importes sirven de garantía y pérdidas por tramos» — Los importes sirven como garantía del repago de la exposición titulizada y el riesgo de incumplimiento está sujeto a la asignación de pérdidas por tramos. · tramo [exacta]: «cuando dichos importes sirvan como garantía del repago de la exposición titulizada en cuestión y el riesgo de incumplimiento esté sujeto a la asignación de pérdidas por tramos»
- **exc_sintetica_insignificante Excepcion** «Excepción: riesgo de incumplimiento insignificante (CLN)» — No se computan los montos de instrumentos con vinculación crediticia si la entidad demuestra que el riesgo de incumplimiento es insignificante; exceptúa la obligación de computarlos en K_SA. · tramo [exacta]: «Ello a menos que la entidad pueda demostrar que el riesgo de incumplimiento es insignificante.»
- **ob_ksa_bruto Obligacion** «K_SA con monto bruto de la exposición» — Cuando la entidad haya constituido previsión específica o tenga descuento no reembolsable en el precio de compra, K_SA se calcula con el monto bruto de la exposición, sin deducirlos. · props: `{"tipo": "calculo"}` · tramo [no]: «el cálculo de K deberá efectuarse usando el monto bruto de la exposición –es decir, sin deducir la previsión específica y/o el descuento no reembolsable en el precio de compra–»
- **cond_prevision Condicion** «Previsión específica o descuento no reembolsable» — La entidad constituyó una previsión específica o tiene un descuento no reembolsable en el precio de compra de su exposición al conjunto de activos subyacentes. · tramo [exacta]: «En los casos en los que la entidad haya constituido una previsión específica o tenga un descuento no reembolsable en el precio de compra de su exposición al conjunto de activos subyacentes»
- **def_w Definicion** «W: ratio exposiciones subyacentes en mora» — Ratio entre el monto nominal de las exposiciones subyacentes en mora y el monto nominal de las exposiciones subyacentes. · props: `{"termino": "W"}` · tramo [exacta]: «La variable W es el ratio entre el monto nominal de las exposiciones subyacentes en mora y el monto nominal de las exposiciones subyacentes.»
- **def_mora Definicion** «Exposiciones subyacentes en mora» — Exposiciones subyacentes con atrasos de 90 días o más, sujetas a quiebra o concurso, en ejecución, que consistan en bienes inmuebles adquiridos en defensa del crédito, o en incumplimiento según los contratos de titulización. · props: `{"termino": "en mora"}` · tramo [exacta]: «Se consideran en mora a las exposiciones subyacentes cuando se verifiquen atrasos en los pagos de 90 días o más»
- **def_w_retit Definicion** «W en retitulizaciones mixtas» — En retitulizaciones cuya cartera subyacente consista en tramos de titulización y otros activos, W es cero para las posiciones de titulización y la que corresponda para los activos subyacentes que no son titulizaciones. · props: `{"termino": "W"}` · tramo [exacta]: «W será cero para las posiciones de titulización y la que corresponda según lo previsto en los dos párrafos precedentes para los activos subyacentes que no son titulizaciones»
- **ob_ka_subconjunto Obligacion** «Calcular K_A por subconjunto en retitulizaciones» — En retitulizaciones con tramos de titulización y otros activos, se calcula por separado K_A de cada subconjunto aplicando W por separado; K_A de la retitulización es el promedio, ponderado por la exposición nominal, de los K_A de cada subconjunto. · props: `{"tipo": "calculo"}` · tramo [exacta]: «se deberá calcular por separado el K coA rrespondiente a cada subconjunto aplicando W por separado»
- **ob_ka_ajuste_desconocido Obligacion** «Ajustar K_A si se desconoce cumplimiento (≤5 %)» — Si se desconoce la situación de cumplimiento del 5 % o menos de las exposiciones subyacentes, se debe ajustar el cálculo de K_A. · props: `{"tipo": "calculo"}` · umbral: ['el 5 % o menos de las exposiciones subyacentes'] · tramo [exacta]: «En caso de que se desconozca la situación de cumplimiento correspondiente al 5 % o menos de las exposiciones subyacentes, se deberá ajustar el cálculo de K de la siguiente manera:»
- **ob_pond_1250 Obligacion** «Ponderar al 1250 % si se desconoce cumplimiento >5 %» — Si la entidad no conoce la situación de cumplimiento para más del 5 % de la posición de titulización, ésta se pondera al 1250 %. · props: `{"tipo": "calculo"}` · umbral: ['más del 5 % de la posición de titulización', 'ponderarse al 1250 %'] · tramo [exacta]: «Si la entidad no conociera la situación de cumplimiento para más del 5 % de la posición de titulización, ésta deberá ponderarse al 1250 %.»
- **cond_desconoce_5 Condicion** «Se desconoce cumplimiento de más del 5 %» — La entidad no conoce la situación de cumplimiento para más del 5 % de la posición de titulización. · umbral: ['más del 5 % de la posición de titulización'] · tramo [exacta]: «Si la entidad no conociera la situación de cumplimiento para más del 5 % de la posición de titulización»
- **def_ksfa_p Definicion** «Parámetro p de K_SSFA(KA)» — p = 0,5 si la titulización cumple con los criterios STC del punto 3.1.14; p = 1 si no los cumple; p = 1,5 si se trata de una retitulización. · props: `{"termino": "p"}` · tramo [exacta]: «p = 0,5 si la titulización cumple con los criterios STC del punto 3.1.14.»
- R: ob_ksa_cobertura Obligacion —regula→ op_calc_ksa Operacion
- R: ob_sintetica_fondos Obligacion —regula→ op_calc_ksa Operacion
- R: ob_ksa_bruto Obligacion —regula→ op_calc_ksa Operacion
- R: cond_excluir_demuestra Condicion —condicion_de→ pot_excluir_spe Potestad
- R: cond_sintetica_garantia Condicion —condicion_de→ ob_sintetica_fondos Obligacion
- R: cond_prevision Condicion —condicion_de→ ob_ksa_bruto Obligacion
- R: cond_desconoce_5 Condicion —condicion_de→ ob_pond_1250 Obligacion
- R: exc_sintetica_insignificante Excepcion —exceptua_obligacion→ ob_sintetica_fondos Obligacion
- R: ob_ksa_cobertura Obligacion —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- R: pot_excluir_spe Potestad —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- R: ob_sintetica_fondos Obligacion —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- R: ob_ksa_bruto Obligacion —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- R: ob_ka_subconjunto Obligacion —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- R: ob_pond_1250 Obligacion —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- Omisión `formula` [exacta]: «K se obtiene a partir de K y W conforme a la siguiente expresión:» — Expresión de K_A en función de K_SA y W: fórmula no confiable, no se reconstruye.
- Omisión `formula` [tokens]: «se SSFA(KA) calculará conforme a lo siguiente» — Fórmula de K_SSFA(KA) destruida en la extracción del PDF; no se reconstruye.
- Omisión `formula` [exacta]: «donde:» — Variables de la fórmula K_SSFA(KA); solo el parámetro p está en prosa y fue extraído como definición.
- Omisión `formula` [exacta]: «se deberá ajustar el cálculo de K de la siguiente manera:» — La expresión del ajuste de K_A para el 5 % o menos de exposiciones con situación desconocida es una fórmula no confiable; solo se extrajo la obligación de ajustar.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «estructura con SPE» | `dentro_de_norma` |  | dentro de la Definicion def_spe_activos (tramo «Cuando la estructura involucre a un SPE…»); extraído como norma de otro tipo |
| 2 | «si puede demostrar» | `condicion_con_relacion` |  | cond_excluir_demuestra Condicion —condicion_de→ pot_excluir_spe Potestad |
| 3 | «sintéticas con fondos aportados» | `dentro_de_norma` |  | dentro de la Obligacion ob_sintetica_fondos (descripción «En titulizaciones sintéticas a las que se aporten fondos»); la Condicion cond_sintetica_garantia es otro supuesto (garantía y pérdidas por tramos) |
| 4 | «previsión específica» | `condicion_con_relacion` |  | cond_prevision Condicion —condicion_de→ ob_ksa_bruto Obligacion |
| 5 | «desconocida para 5 % o menos» | `dentro_de_norma` |  | dentro de la Obligacion ob_ka_ajuste_desconocido (umbral «el 5 % o menos de las exposiciones subyacentes»); sin Condicion |
| 6 | «para más del 5 %» | `condicion_con_relacion` |  | cond_desconoce_5 Condicion con el umbral —condicion_de→ ob_pond_1250 Obligacion |

## `cap::3.1.11.3` — Determinación del ponderador de riesgo (RW).

Grupos: grupo_c.

### Texto

> *heredado:* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos.
> *heredado:* 3.1. Tratamiento de las titulizaciones.
> *heredado:* Se denomina "posición de titulización" a la exposición a una titulización (o retitulización), tradicional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes conceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos ("AssetBacked Securities", ABS) y bonos de titulización hipotecaria ("Mortgage-Backed Securities", MBS)–, mejoras crediticias, facilidades de liquidez, "swaps" de tasa de interés o de monedas y derivados de crédito. Las reservas ("reserve accounts"), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo también el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad económica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una determinada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> *heredado:* 3.1.11. Enfoque estandarizado.
> *heredado:* Los ponderadores de riesgo a aplicar a las posiciones de una titulización y a las exposiciones subyacentes de una retitulización para la determinación de la exigencia de capital se establecerán empleando las disposiciones de este punto. Las posiciones de titulización a las que no se les pueda aplicar el enfoque estandarizado deberán ser ponderadas al 1250 %.
> *propio:* 3.1.11.3. Determinación del ponderador de riesgo (RW). El ponderador de riesgo RW a asignar a una posición de titulización se calculará con ajuste a lo siguiente: i) Si D es menor o igual a K , el ponderador será de 1250 %. A ii) Si A es mayor o igual a K , el ponderador será igual a K multiplicado A SSFA(KA) por 12,5. iii) Si K es mayor que A y menor que D, el ponderador será un promedio A ponderado entre 1250 % y 12,5 veces K conforme a la siguiente exSSFA(KA) presión: El ponderador para coberturas del riesgo de mercado, tales como "swaps" de moneda o de tasa de interés, se inferirá a partir de una posición de titulización de igual prelación ("pari passu") con los "swaps" o, si tal posición no existiera, a partir del tramo subordinado más próximo. El ponderador resultante estará sujeto a un mínimo de: a) 15 % para titulizaciones que no cumplan con los criterios STC –punto 3.1.14.–. b) 10 % para los tramos de máxima preferencia de titulizaciones que cumplan con los criterios STC –punto 3.1.14.– y 15 % para los tramos subordinados de esas titulizaciones. c) 100 % para retitulizaciones. Para posiciones de titulización de máxima preferencia se podrá aplicar el tratamiento de transparencia ("look-through") de conformidad con lo previsto en el punto 3.1.6. Si el ponderador que surge de la aplicación de ese tratamiento fuera menor que el ponderador mínimo que corresponda de acuerdo con los apartados a) a c) precedentes, se podrá aplicar el primero.

### Extracción (código A)

- **op1 Operacion** «Determinación del ponderador de riesgo (RW)» — Cálculo del ponderador de riesgo RW a asignar a una posición de titulización, enfoque estandarizado · props: `{"tipo": "calculo"}` · tramo [exacta]: «El ponderador de riesgo RW a asignar a una posición de titulización se calculará»
- **ob1 Obligacion** «RW 1250 % si D ≤ KA» — Si D es menor o igual a KA, el ponderador de riesgo RW de la posición de titulización será de 1250 %. · props: `{"tipo": "calculo"}` · umbral: ['Si D es menor o igual a K , el ponderador será de 1250 %.'] · tramo [exacta]: «Si D es menor o igual a K , el ponderador será de 1250 %.»
- **ob2 Obligacion** «RW = 12,5 × KSSFA(KA) si A ≥ KA» — Si A es mayor o igual a KA, el ponderador de riesgo RW será igual a KSSFA(KA) multiplicado por 12,5. · props: `{"tipo": "calculo"}` · tramo [exacta]: «Si A es mayor o igual a K , el ponderador será igual a K multiplicado A SSFA(KA) por 12,5.»
- **ob3 Obligacion** «RW promedio ponderado si KA entre A y D» — Si KA es mayor que A y menor que D, el ponderador de riesgo RW será un promedio ponderado entre 1250 % y 12,5 veces KSSFA(KA), conforme a la expresión indicada. · props: `{"tipo": "calculo"}` · umbral: ['un promedio A ponderado entre 1250 % y 12,5 veces K'] · tramo [exacta]: «Si K es mayor que A y menor que D, el ponderador será un promedio A ponderado entre 1250 % y 12,5 veces K conforme a la siguiente exSSFA(KA) presión:»
- **ob4 Obligacion** «Inferir ponderador de coberturas de riesgo de mercado» — El ponderador para coberturas del riesgo de mercado (swaps de moneda o de tasa de interés) se infiere de una posición de titulización pari passu con los swaps o, si no existe, del tramo subordinado más próximo. · props: `{"tipo": "calculo"}` · tramo [exacta]: «El ponderador para coberturas del riesgo de mercado, tales como "swaps" de moneda o de tasa de interés, se inferirá a partir de una posición de titulización de igual prelación ("pari passu") con los "swaps" o, si tal posición no existiera, a partir del tramo subordinado más próximo.»
- **r1 Restriccion** «Mínimo 15 % — titulizaciones no STC» — El ponderador resultante estará sujeto a un mínimo de 15 % para titulizaciones que no cumplan con los criterios STC. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['El ponderador resultante estará sujeto a un mínimo de: a) 15 %'] · tramo [exacta]: «15 % para titulizaciones que no cumplan con los criterios STC –punto 3.1.14.–»
- **r2 Restriccion** «Mínimo 10 % — tramos máxima preferencia STC» — El ponderador resultante estará sujeto a un mínimo de 10 % para los tramos de máxima preferencia de titulizaciones que cumplan con los criterios STC. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['10 % para los tramos de máxima preferencia'] · tramo [exacta]: «10 % para los tramos de máxima preferencia de titulizaciones que cumplan con los criterios STC –punto 3.1.14.–»
- **r3 Restriccion** «Mínimo 15 % — tramos subordinados STC» — El ponderador resultante estará sujeto a un mínimo de 15 % para los tramos subordinados de titulizaciones que cumplan con los criterios STC. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['15 % para los tramos subordinados'] · tramo [exacta]: «15 % para los tramos subordinados de esas titulizaciones»
- **r4 Restriccion** «Mínimo 100 % — retitulizaciones» — El ponderador resultante estará sujeto a un mínimo de 100 % para retitulizaciones. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['100 % para retitulizaciones.'] · tramo [exacta]: «100 % para retitulizaciones.»
- **p1 Potestad** «Look-through para titulizaciones de máxima preferencia» — Para posiciones de titulización de máxima preferencia se puede aplicar el tratamiento de transparencia (look-through) conforme al punto 3.1.6. · tramo [exacta]: «Para posiciones de titulización de máxima preferencia se podrá aplicar el tratamiento de transparencia ("look-through")»
- **p2 Potestad** «Aplicar RW look-through menor al mínimo» — Si el ponderador resultante del look-through es menor que el mínimo de los apartados a) a c), se puede aplicar el ponderador del look-through. · tramo [exacta]: «Si el ponderador que surge de la aplicación de ese tratamiento fuera menor que el ponderador mínimo que corresponda de acuerdo con los apartados a) a c) precedentes, se podrá aplicar el primero.»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion
- R: ob4 Obligacion —regula→ op1 Operacion
- R: r1 Restriccion —limita→ op1 Operacion
- R: r2 Restriccion —limita→ op1 Operacion
- R: r3 Restriccion —limita→ op1 Operacion
- R: r4 Restriccion —limita→ op1 Operacion
- Omisión `formula` [exacta]: «conforme a la siguiente exSSFA(KA) presión:» — La expresión del promedio ponderado del caso iii) es una fórmula no confiable: no se reconstruye.
- Omisión `formula` [exacta]: «Si A es mayor o igual a K , el ponderador será igual a K multiplicado A SSFA(KA) por 12,5.» — Los subíndices de K (KA, KSSFA(KA)) están alterados por la extracción del PDF; la descripción se limita a lo que la prosa sostiene.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «i) a iii) según D, A y KA» (i)) | `dentro_de_norma` |  | dentro de la Obligacion ob1 («RW 1250 % si D ≤ KA», tramo con el «Si D es menor o igual a K»); sin Condicion |
| 2 | «i) a iii) según D, A y KA» (ii)) | `dentro_de_norma` |  | dentro de la Obligacion ob2 (tramo «Si A es mayor o igual a K…»); sin Condicion |
| 3 | «i) a iii) según D, A y KA» (iii)) | `dentro_de_norma` |  | dentro de la Obligacion ob3 (tramo «Si K es mayor que A y menor que D…»); sin Condicion |
| 4 | «si no existiera la posición pari passu» | `dentro_de_norma` |  | dentro de la Obligacion ob4 (tramo «…o, si tal posición no existiera, a partir del tramo subordinado más próximo») |
| 5 | «mínimos por STC» | `dentro_de_norma` |  | dentro de las Restricciones r1 a r4 (cada mínimo con su supuesto STC / no STC / retitulización en el tramo); sin Condicion |
| 6 | «look-through menor que el mínimo» | `dentro_de_norma` |  | dentro de la Potestad p2 (tramo «Si el ponderador … fuera menor que el ponderador mínimo …, se podrá aplicar el primero»); extraído como norma, no como Condicion ni Excepcion |

## `cap::3.1.14.1` — Riesgo de los activos subyacentes.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos.
> *heredado:* 3.1. Tratamiento de las titulizaciones.
> *heredado:* Se denomina "posición de titulización" a la exposición a una titulización (o retitulización), tradicional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes conceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos ("AssetBacked Securities", ABS) y bonos de titulización hipotecaria ("Mortgage-Backed Securities", MBS)–, mejoras crediticias, facilidades de liquidez, "swaps" de tasa de interés o de monedas y derivados de crédito. Las reservas ("reserve accounts"), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo también el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad económica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una determinada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> *heredado:* 3.1.14. Criterios para la determinación de titulizaciones simples, transparentes y comparables.
> *heredado:* A los fines de establecer el ponderador de riesgo a aplicar de acuerdo con el enfoque estandarizado –punto 3.1.11.–, una titulización se considerará simple, transparente y comparable (STC) si: -se trata de una titulización tradicional que no constituye un programa ABCP; - involucra una transferencia real de activos –en los términos del acápite v) del punto
> *heredado:* 3.1.14.1.–; y
> *heredado:* - cumple con la totalidad de los criterios previstos en el presente punto (en adelante,
> *heredado:* "criterios STC").
> *heredado:* El originante/fiduciario deberá divulgar toda la información necesaria respecto de la transacción que permita a los inversores determinar si la titulización cumple con los criterios STC. En base a la información provista, el inversor deberá realizar sus propias evaluaciones respecto del cumplimiento de estos criterios previo a la aplicación del enfoque estandarizado. Para las posiciones retenidas en las que el originante haya transferido el riesgo de acuerdo con lo establecido en los puntos 3.1.2.2. y 3.1.8.2. la determinación respecto del cumplimiento de los criterios será efectuada únicamente por la entidad originante. Los criterios STC deberán cumplirse en todo momento. Algunos de los criterios se deberán verificar sólo al momento de la originación o cuando se genere la posición –si ésta es posterior–, tal como en el caso de las garantías y las facilidades de liquidez. No obstante, los inversores y tenedores de las posiciones de titulización deberán tener en cuenta las modificaciones que puedan invalidar las evaluaciones de cumplimiento previas, tales como las deficiencias en la frecuencia y en el contenido de los informes a los inversores o los cambios en la documentación contrarios a los criterios STC. En los casos en que los criterios hagan referencia a activos subyacentes –incluidos los criterios previstos en el punto 3.1.14.4.– y el conjunto de subyacentes admita la incorporación de nuevos activos, el cumplimiento estará sujeto a que se realicen verificaciones cada vez que se incorporen esos nuevos activos. Cuando la SEFyC detecte que una titulización no cumple con alguno de los criterios, podrá exigir la implementación de acciones correctivas y/o determinar que se suspenda el tratamiento STC para una o más posiciones de titulización.
> *propio:* 3.1.14.1. Riesgo de los activos subyacentes. i) Naturaleza de los activos. Los activos subyacentes deberán estar constituidos por documentos a cobrar o derechos de crédito de carácter homogéneo en cuanto a su tipo, jurisdicción, legislación aplicable y moneda y sus flujos de fondos deberán estar contractualmente identificados, ser periódicos y consistir exclusivamente en pagos del principal e intereses o de arrendamientos financieros. La homogeneidad de los activos subyacentes deberá evaluarse teniendo en consideración los siguientes principios: a) La naturaleza de los activos deberá ser tal que los inversores, al realizar el proceso de debida diligencia, no necesiten analizar ni evaluar perfiles o factores de riesgo, crediticios o legales, sustancialmente diferentes entre sí. b) La homogeneidad se deberá evaluar en función de factores y perfiles de riesgo comunes al conjunto de los activos. c) Los documentos y créditos incluidos en la titulización deberán constituir obligaciones estándares, en términos de derechos de cobro y/o rentas de los activos y generar un flujo de pago a los inversores periódico y claramente definido –tal como el flujo que generan las facilidades que proveen las tarjetas de crédito–. d) El reembolso a los inversores en la titulización deberá provenir principalmente del producido de los activos subyacentes y no deberá depender de modo sustancial de la refinanciación de los créditos. Se podrá contar con la refinanciación o venta de los subyacentes siempre que las operaciones a refinanciar estén suficientemente distribuidas en el conjunto de los activos titulizados y que sus valores residuales no sean significativos. Las tasas de interés o de descuento de referencia deberán ser tasas de interés de mercado y de fácil consulta –tales como tasas interbancarias o tasas establecidas por el BCRA y tasas sectoriales que reflejen el costo del fondeo de las entidades financieras–, evitándose referencias a fórmulas complejas o derivados exóticos. Los límites máximos y mínimos establecidos sobre las tasas de interés no serán considerados necesariamente como derivados exóticos. ii) Historia de desempeño de los activos. Se deberá contar con información verificable sobre pérdidas e incumplimientos respecto de activos con características de riesgo sustancialmente similares a los que integran la titulización y por un período de tiempo lo suficientemente prolongado. Ello a los efectos de proveer al inversor de información respecto de las distintas categorías de activos, así como de datos que le permitan realizar un cálculo preciso de las pérdidas esperadas bajo distintos escenarios de estrés, para que pueda llevar a cabo un adecuado proceso de debida diligencia. Las fuentes de información y el acceso a los datos, así como los fundamentos que permitan aducir la similitud con los activos titulizados, deberán estar disponibles para todos los participantes del mercado. El inversor, además, deberán poder evaluar –durante su proceso de debida diligencia– si el originante, fiduciario, administrador, agente de cobro u otros sujetos con responsabilidad fiduciaria en la titulización cuentan con probados antecedentes, reunidos a lo largo de un período suficientemente largo, respecto de activos sustancialmente similares a aquellos que son objeto de titulización. Esta consideración no será condición para dar cumplimiento con el presente criterio. El originante de la titulización, así como el acreedor inicial de los créditos titulizados, deberán contar con experiencia suficiente en el otorgamiento de financiaciones similares a las titulizadas. El inversor deberá determinar la experiencia y el historial de desempeño del originante y del acreedor inicial respecto de activos sustancialmente similares a los titulizados a través de un período convenientemente prolongado. El desempeño se deberá verificar durante un período mínimo de 5 años en el caso de las exposiciones minoristas que se ajusten a la definición prevista en el punto 2.8.1. –sin considerar las exclusiones allí previstas– y que cumplan con el criterio previsto en el punto 2.8.3.1. Para el resto de las exposiciones, el desempeño deberá verificarse durante 7 años. Ello para evitar, por ejemplo, que se originen carteras con el solo fin de transferirlas. iii) Estado de cumplimiento de los activos. A fin de asegurar que sólo se asignen a una titulización documentos a cobrar o derechos de crédito que no estén en mora, no se podrán transferir activos en situación de incumplimiento o mora u obligaciones respecto de las cuales el originante o el fiduciario o los demás participantes de la titulización con responsabilidad fiduciaria cuenten con evidencia de un incremento sustancial en las pérdidas esperadas o que se encuentran en gestión de cobranza. El originante o fiduciario deberá verificar que los activos cumplan con las siguientes condiciones: a) El obligado al pago no ha sido sometido a un proceso de quiebra o de reestructuración de deuda debido a dificultades financieras en los 3 años previos a la fecha de originación, salvo que resulte de aplicación el período de 2 años previsto en el art. 26, inciso 4, de la Ley 25.326. b) El obligado al pago no cuenta con un historial de crédito desfavorable en algún registro público de crédito. c) El obligado al pago no cuenta con una evaluación de una agencia de calificación de créditos o un credit scoring que anticipen un riesgo de incumplimiento significativo. d) El documento a cobrar o derecho de crédito transferido no es objeto de litigios entre el obligado y el acreedor original. El análisis de estas condiciones deberá ser llevado a cabo por el originante o fiduciario dentro de los 45 días previos a la fecha de la transferencia de los activos. Al momento de la evaluación, no deberá existir evidencia que indique la posibilidad de deterioro en el estado de cumplimiento de los activos. Adicionalmente, al momento de la inclusión del activo en la cartera de subyacentes, deberá haberse registrado al menos un pago, excepto en el caso de las estructuras sobre activos de tipo rotativos (como tarjetas de crédito, facturas y otras exposiciones cancelables en un solo pago). iv)Consistencia en la originación de los activos. El originante deberá demostrar al inversor que los activos transferidos han sido generados en el curso normal de su negocio bajo estándares de originación uniformes y consistentes. Cuando esos estándares se vean afectados por cambios, el originante deberá comunicar el momento y el propósito de las modificaciones. Los estándares no deberán ser menos rigurosos que aquellos aplicados a los activos retenidos por el originante. Los documentos a cobrar o derechos de crédito titulizados –incluso cuando formen parte de carteras atomizadas– deberán satisfacer criterios de originación sólidos y prudentes que incluyan una evaluación de la capacidad e intención de los obligados de cumplir puntualmente con sus obligaciones. Además, en el caso de carteras atomizadas, tales documentos o derechos deberán ser originados en el curso normal del negocio del originante y sus flujos de fondos esperados deberán permitir atender las obligaciones establecidas en la titulización aun en escenarios de estrés suficientemente conservadores respecto de las pérdidas crediticias. Cuando los activos hayan sido adquiridos a terceros, el originante/fiduciario de la titulización deberá revisar los estándares de originación de esos terceros –verificando su existencia y calidad– y constatar que el acreedor original ha examinado y evaluado la habilidad y voluntad de los obligados de hacer los respectivos pagos de manera puntual. v) Selección y transferencia de los activos. El desempeño de la titulización no deberá depender de una selección de los subyacentes a través de la gestión activa y discrecional de la cartera. Por el contrario, la selección de los activos deberá estar sujeta a criterios de elegibilidad claramente definidos, tales como el tamaño de la obligación, la edad del sujeto de crédito y los ratios "loan-to-value" (LTV), "debtto-income" (DTI) y/o "debt service coverage" (DSC). En la medida en que la selección no sea discrecional, la incorporación de créditos en los períodos de rotación o su sustitución o recompra debido al incumplimiento de cláusulas contractuales no se considerará una gestión activa de la cartera. Los documentos a cobrar y créditos transferidos luego de la fecha en que se concreta la titulización tampoco deberán ser seleccionados de manera discrecional ni gestionados de forma activa. Los inversores deberían poder evaluar el riesgo crediticio de la cartera de activos en forma previa a sus decisiones de inversión. A efectos de cumplir con el principio de transferencia real, deberá realizarse una cesión efectiva de derechos de forma tal que los documentos a cobrar y derechos de crédito: a) constituyan una deuda de los respectivos obligados y ello conste en las cláusulas de la titulización; b) estén fuera del alcance del cedente, sus acreedores o liquidadores y no estén sujetos a riesgos de modificación sustancial de los contratos o restitución de los activos; c) hayan sido objeto de una cesión de créditos; es decir, que la transferencia del riesgo de crédito no se haya efectuado mediante un CDS, derivado o garantía (titulización sintética); y d) proporcionen un efectivo derecho contra el último obligado y no constituyan una titulización de otras titulizaciones; es decir, que no se trate de retitulizaciones. El contrato de cesión de los créditos deberá contener cláusulas por las cuales el originante garantice que los documentos a cobrar o los créditos que están siendo transferidos para su titulización no están afectados en garantía ni sujetos a ninguna otra condición o gravamen que, hasta donde se pueda prever, afecten el cobro de las sumas pendientes. La documentación que instrumente la titulización deberá incluir una opinión legal independiente que respalde que la transferencia real y la cesión de derechos bajo la legislación aplicable se ajustan a lo indicado en los apartados a) a d) anteriores. En el caso de que la legislación aplicable a la titulización no se ajuste a lo previsto en los apartados a) a d) precedentes, se deberá demostrar la existencia de los obstáculos que así lo impiden y especificar el método del que disponen los inversores para ejercer sus derechos contra los obligados al pago. Además, de corresponder, deberá informarse toda condición o evento que pueda retrasar o impedir la transferencia de los activos subyacentes a la titulización así como cualquier factor que pueda afectar el perfeccionamiento oportuno de los reclamos. vi) Información inicial y periódica. A fin de asistir a los inversores en la realización de un apropiado proceso de debida diligencia en forma previa a la inversión en un nuevo instrumento, se deberá contar con suficiente información a nivel de cada préstamo o, en el caso de carteras atomizadas, con datos sobre las características de riesgo relevantes resumidas a nivel de cada tramo de activos subyacentes. Para asistir a los inversores en el seguimiento permanente del desempeño de sus inversiones y para que aquellos inversores que deseen adquirir una titulización en el mercado secundario tengan información suficiente para realizar una correcta evaluación de la inversión, se deberá suministrar al menos trimestralmente durante la vida de la titulización datos a nivel de préstamos en función de las regulaciones aplicables o, en el caso de las carteras atomizadas, datos resumidos a nivel de cada tramo de activos subyacentes, así como también informes estandarizados dirigidos al inversor. Las fechas de corte de los datos deberán estar en línea con las utilizadas para la emisión de los informes. A efectos de generar confianza respecto tanto de la exactitud de lo informado sobre los activos subyacentes como de que estos activos cumplen con los requisitos de elegibilidad –acápite v) precedente–, la cartera inicial deberá ser revisada por un contador público independiente.

### Extracción (código A)

- **op_tit Operacion** «Titulización STC (criterios activos subyacentes)» — Titulización simple, transparente y comparable (STC): criterios sobre el riesgo de los activos subyacentes · props: `{"tipo": "titulización"}` · tramo [exacta]: «Riesgo de los activos subyacentes.»
- **o1 Obligacion** «Activos subyacentes homogéneos con flujos identificados» — Los activos subyacentes deben ser documentos a cobrar o derechos de crédito homogéneos en tipo, jurisdicción, legislación aplicable y moneda, con flujos de fondos contractualmente identificados, periódicos y consistentes exclusivamente en pagos de principal e intereses o arrendamientos financieros. · props: `{"tipo": "otra"}` · tramo [exacta]: «Los activos subyacentes deberán estar constituidos por documentos a cobrar o derechos de crédito de carácter homogéneo en cuanto a su tipo, jurisdicción, legislación aplicable y moneda»
- **o2 Obligacion** «Evaluar homogeneidad según principios a)-d)» — La homogeneidad debe evaluarse: sin perfiles de riesgo sustancialmente diferentes para el inversor, según factores comunes de riesgo, con obligaciones estándares y flujo periódico claramente definido, y con reembolso proveniente principalmente del producido de los activos y no de la refinanciación sustancial. · props: `{"tipo": "otra"}` · tramo [exacta]: «La homogeneidad de los activos subyacentes deberá evaluarse teniendo en consideración los siguientes principios»
- **o3 Obligacion** «Tasas de referencia de mercado y fácil consulta» — Las tasas de interés o de descuento de referencia deben ser tasas de mercado y de fácil consulta, evitando fórmulas complejas o derivados exóticos; los límites máximos y mínimos sobre las tasas no se consideran necesariamente derivados exóticos. · props: `{"tipo": "otra"}` · tramo [exacta]: «Las tasas de interés o de descuento de referencia deberán ser tasas de interés de mercado y de fácil consulta»
- **o4 Obligacion** «Información verificable de pérdidas e incumplimientos» — Contar con información verificable sobre pérdidas e incumplimientos de activos similares durante un período suficientemente prolongado, para que el inversor calcule pérdidas esperadas bajo escenarios de estrés. · props: `{"tipo": "otra"}` · tramo [exacta]: «Se deberá contar con información verificable sobre pérdidas e incumplimientos respecto de activos con características de riesgo sustancialmente similares a los que integran la titulización y por un período de tiempo lo suficientemente prolongado.»
- **o5 Obligacion** «Fuentes de información disponibles para el mercado» — Las fuentes de información, el acceso a los datos y los fundamentos de similitud con los activos titulizados deben estar disponibles para todos los participantes del mercado. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Las fuentes de información y el acceso a los datos, así como los fundamentos que permitan aducir la similitud con los activos titulizados, deberán estar disponibles para todos los participantes del mercado.»
- **o6 Obligacion** «Inversor evalúa antecedentes de originante y otros» — El inversor debe poder evaluar durante su debida diligencia si el originante, fiduciario, administrador, agente de cobro u otros con responsabilidad fiduciaria tienen probados antecedentes en activos similares; esta consideración no es condición para dar cumplimiento al criterio. · props: `{"tipo": "otra"}` · tramo [exacta]: «El inversor, además, deberán poder evaluar –durante su proceso de debida diligencia– si el originante, fiduciario, administrador, agente de cobro u otros sujetos con responsabilidad fiduciaria en la titulización cuentan con probados antecedentes»
- **o7 Obligacion** «Experiencia suficiente de originante y acreedor inicial» — El originante y el acreedor inicial deben contar con experiencia suficiente en el otorgamiento de financiaciones similares a las titulizadas. · props: `{"tipo": "otra"}` · tramo [exacta]: «El originante de la titulización, así como el acreedor inicial de los créditos titulizados, deberán contar con experiencia suficiente en el otorgamiento de financiaciones similares a las titulizadas.»
- **o8 Obligacion** «Inversor determina experiencia: 5 años minoristas» — El inversor debe determinar la experiencia y el historial de desempeño del originante y del acreedor inicial; el desempeño se verifica durante un mínimo de 5 años para exposiciones minoristas que se ajusten a la definición del punto 2.8.1. (sin considerar las exclusiones) y cumplan el criterio del punto 2.8.3.1. · props: `{"tipo": "otra"}` · umbral: ['un período mínimo de 5 años'] · tramo [exacta]: «El desempeño se deberá verificar durante un período mínimo de 5 años en el caso de las exposiciones minoristas que se ajusten a la definición prevista en el punto 2.8.1.»
- **o9 Obligacion** «Inversor verifica desempeño 7 años resto de exposiciones» — Para las exposiciones distintas de las minoristas indicadas, el desempeño del originante y del acreedor inicial debe verificarse durante 7 años. · props: `{"tipo": "otra"}` · umbral: ['durante 7 años'] · tramo [exacta]: «Para el resto de las exposiciones, el desempeño deberá verificarse durante 7 años.»
- **r1 Restriccion** «No transferir activos en mora o incumplimiento» — No se pueden transferir a la titulización activos en incumplimiento o mora, ni obligaciones con evidencia de incremento sustancial de pérdidas esperadas o en gestión de cobranza. · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «no se podrán transferir activos en situación de incumplimiento o mora u obligaciones respecto de las cuales el originante o el fiduciario o los demás participantes de la titulización con responsabilidad fiduciaria cuenten con evidencia de un incremento sustancial en las pérdidas esperadas o que se encuentran en gestión…»
- **o10 Obligacion** «Verificar condiciones de cumplimiento de activos a)-d)» — El originante o fiduciario debe verificar que los activos cumplan: obligado sin quiebra o reestructuración por dificultades financieras en los 3 años previos a la originación (salvo el período de 2 años del art. 26 inc. 4 Ley 25.326), sin historial de crédito desfavorable, sin evaluación o scoring que anticipe riesgo significativo de incumplimiento, y sin litigios sobre el crédito. · props: `{"tipo": "otra"}` · umbral: ['en los 3 años previos a la fecha de originación', 'el período de 2 años'] · tramo [exacta]: «El originante o fiduciario deberá verificar que los activos cumplan con las siguientes condiciones»
- **o11 Obligacion** «Análisis dentro de 45 días previos a transferencia» — El análisis de las condiciones de cumplimiento debe realizarse dentro de los 45 días previos a la transferencia de los activos; al evaluar no debe existir evidencia de posible deterioro. · props: `{"tipo": "otra"}` · umbral: ['dentro de los 45 días previos a la fecha de la transferencia de los activos'] · tramo [exacta]: «El análisis de estas condiciones deberá ser llevado a cabo por el originante o fiduciario dentro de los 45 días previos a la fecha de la transferencia de los activos.»
- **o12 Obligacion** «Al menos un pago registrado al incluir el activo» — Al incluir el activo en la cartera de subyacentes debe haberse registrado al menos un pago. · props: `{"tipo": "otra"}` · tramo [exacta]: «al momento de la inclusión del activo en la cartera de subyacentes, deberá haberse registrado al menos un pago»
- **x1 Excepcion** «Excepción pago previo: activos rotativos» — Exceptúa la exigencia de al menos un pago registrado para estructuras sobre activos rotativos. · tramo [exacta]: «excepto en el caso de las estructuras sobre activos de tipo rotativos (como tarjetas de crédito, facturas y otras exposiciones cancelables en un solo pago)»
- **o13 Obligacion** «Demostrar originación uniforme y consistente» — El originante debe demostrar al inversor que los activos fueron generados en el curso normal del negocio bajo estándares de originación uniformes y consistentes. · props: `{"tipo": "otra"}` · tramo [exacta]: «El originante deberá demostrar al inversor que los activos transferidos han sido generados en el curso normal de su negocio bajo estándares de originación uniformes y consistentes.»
- **o14 Obligacion** «Comunicar cambios en estándares de originación» — Cuando los estándares de originación cambien, el originante debe comunicar el momento y el propósito de las modificaciones. · props: `{"tipo": "otra"}` · tramo [exacta]: «el originante deberá comunicar el momento y el propósito de las modificaciones.»
- **r2 Restriccion** «Estándares no menos rigurosos que activos retenidos» — Los estándares de originación no deben ser menos rigurosos que los aplicados a los activos retenidos por el originante. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «Los estándares no deberán ser menos rigurosos que aquellos aplicados a los activos retenidos por el originante.»
- **o15 Obligacion** «Criterios de originación sólidos y prudentes» — Los documentos a cobrar o derechos de crédito titulizados, incluso en carteras atomizadas, deben satisfacer criterios de originación sólidos y prudentes que evalúen capacidad e intención de pago; en carteras atomizadas, deben originarse en el curso normal del negocio y sus flujos esperados permitir atender las obligaciones aun en escenarios de estrés conservadores. · props: `{"tipo": "otra"}` · tramo [exacta]: «deberán satisfacer criterios de originación sólidos y prudentes que incluyan una evaluación de la capacidad e intención de los obligados de cumplir puntualmente con sus obligaciones»
- **o16 Obligacion** «Revisar estándares de originación de terceros» — Cuando los activos hayan sido adquiridos a terceros, el originante/fiduciario debe revisar los estándares de originación de los terceros y constatar que el acreedor original evaluó la habilidad y voluntad de pago de los obligados. · props: `{"tipo": "otra"}` · tramo [exacta]: «el originante/fiduciario de la titulización deberá revisar los estándares de originación de esos terceros –verificando su existencia y calidad– y constatar que el acreedor original ha examinado y evaluado la habilidad y voluntad de los obligados de hacer los respectivos pagos de manera puntual»
- **c16 Condicion** «Activos adquiridos a terceros» — Los activos fueron adquiridos a terceros. · tramo [exacta]: «Cuando los activos hayan sido adquiridos a terceros»
- **r3 Restriccion** «Sin selección por gestión activa y discrecional» — El desempeño de la titulización no debe depender de una selección de subyacentes mediante gestión activa y discrecional de la cartera. · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «El desempeño de la titulización no deberá depender de una selección de los subyacentes a través de la gestión activa y discrecional de la cartera.»
- **o17 Obligacion** «Selección por criterios de elegibilidad definidos» — La selección de activos debe estar sujeta a criterios de elegibilidad claramente definidos, tales como tamaño de la obligación, edad del sujeto de crédito y ratios LTV, DTI y/o DSC. · props: `{"tipo": "otra"}` · tramo [exacta]: «la selección de los activos deberá estar sujeta a criterios de elegibilidad claramente definidos»
- **x2 Excepcion** «Rotación, sustitución o recompra no es gestión activa» — Exceptúa de la prohibición de gestión activa de la cartera la incorporación de créditos en períodos de rotación, su sustitución o recompra por incumplimiento de cláusulas contractuales. · tramo [exacta]: «la incorporación de créditos en los períodos de rotación o su sustitución o recompra debido al incumplimiento de cláusulas contractuales no se considerará una gestión activa de la cartera»
- **c_x2 Condicion** «Selección no discrecional» — La selección de los créditos no es discrecional. · tramo [exacta]: «En la medida en que la selección no sea discrecional»
- **r4 Restriccion** «Activos transferidos posteriormente sin selección discrecional» — Los documentos y créditos transferidos luego de la fecha de la titulización no deben ser seleccionados discrecionalmente ni gestionados de forma activa. · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «Los documentos a cobrar y créditos transferidos luego de la fecha en que se concreta la titulización tampoco deberán ser seleccionados de manera discrecional ni gestionados de forma activa.»
- **p1 Obligacion** «Inversores evalúan riesgo crediticio previo (recomendación)» — Recomendación y no un deber: los inversores deberían poder evaluar el riesgo crediticio de la cartera antes de sus decisiones de inversión. · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "deberían po-\nder evaluar", "modalidad_clasificada": "no_clasificada"}` · tramo [exacta]: «Los inversores deberían poder evaluar el riesgo crediticio de la cartera de activos en forma previa a sus decisiones de inversión.»
- **o18 Obligacion** «Cesión efectiva de derechos (transferencia real)» — Para la transferencia real debe realizarse una cesión efectiva de derechos de modo que los documentos y derechos: a) constituyan deuda de los obligados y conste en las cláusulas; b) estén fuera del alcance del cedente, sus acreedores o liquidadores y sin riesgo de modificación sustancial de contratos o restitución; c) sean objeto de cesión de créditos y no transferencia de riesgo por CDS, derivado… · props: `{"tipo": "otra"}` · tramo [exacta]: «A efectos de cumplir con el principio de transferencia real, deberá realizarse una cesión efectiva de derechos de forma tal que los documentos a cobrar y derechos de crédito:»
- **o19 Obligacion** «Cláusulas de garantía del originante sobre libertad de gravámenes» — El contrato de cesión debe contener cláusulas por las que el originante garantice que los activos transferidos no están afectados en garantía ni sujetos a otra condición o gravamen que, hasta donde se pueda prever, afecte el cobro. · props: `{"tipo": "otra"}` · tramo [exacta]: «El contrato de cesión de los créditos deberá contener cláusulas por las cuales el originante garantice que los documentos a cobrar o los créditos que están siendo transferidos para su titulización no están afectados en garantía ni sujetos a ninguna otra condición o gravamen»
- **o20 Obligacion** «Opinión legal independiente sobre transferencia real» — La documentación de la titulización debe incluir una opinión legal independiente que respalde que la transferencia real y la cesión de derechos se ajustan a los apartados a) a d). · props: `{"tipo": "otra"}` · tramo [exacta]: «La documentación que instrumente la titulización deberá incluir una opinión legal independiente que respalde que la transferencia real y la cesión de derechos bajo la legislación aplicable se ajustan a lo indicado en los apartados a) a d) anteriores.»
- **o21 Obligacion** «Demostrar obstáculos legales e informar método de inversores» — Si la legislación aplicable no se ajusta a los apartados a) a d), se debe demostrar la existencia de los obstáculos y especificar el método de los inversores para ejercer sus derechos contra los obligados; de corresponder, informar toda condición o evento que pueda retrasar o impedir la transferencia de los activos o afectar el perfeccionamiento de los reclamos. · props: `{"tipo": "otra"}` · tramo [exacta]: «se deberá demostrar la existencia de los obstáculos que así lo impiden y especificar el método del que disponen los inversores para ejercer sus derechos contra los obligados al pago»
- **c21 Condicion** «Legislación no se ajusta a apartados a)-d)» — La legislación aplicable a la titulización no se ajusta a lo previsto en los apartados a) a d). · tramo [exacta]: «En el caso de que la legislación aplicable a la titulización no se ajuste a lo previsto en los apartados a) a d) precedentes»
- **o22 Obligacion** «Información suficiente a nivel de préstamo previa a inversión» — Antes de la inversión en un nuevo instrumento se debe contar con información suficiente a nivel de cada préstamo o, en carteras atomizadas, con datos de riesgo resumidos por tramo de activos subyacentes. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «se deberá contar con suficiente información a nivel de cada préstamo o, en el caso de carteras atomizadas, con datos sobre las características de riesgo relevantes resumidas a nivel de cada tramo de activos subyacentes»
- **o23 Obligacion** «Información trimestral durante la vida de la titulización» — Suministrar al menos trimestralmente durante la vida de la titulización datos a nivel de préstamos (o resumidos por tramo en carteras atomizadas) e informes estandarizados al inversor; las fechas de corte deben estar en línea con las de emisión de informes. · props: `{"tipo": "presentacion_informativa", "frecuencia": "trimestral"}` · tramo [exacta]: «se deberá suministrar al menos trimestralmente durante la vida de la titulización datos a nivel de préstamos en función de las regulaciones aplicables o, en el caso de las carteras atomizadas, datos resumidos a nivel de cada tramo de activos subyacentes, así como también informes estandarizados dirigidos al inversor»
- **o24 Obligacion** «Revisión de cartera inicial por contador público independiente» — La cartera inicial debe ser revisada por un contador público independiente, para generar confianza sobre la exactitud de lo informado y el cumplimiento de los requisitos de elegibilidad del acápite v). · props: `{"tipo": "otra"}` · tramo [exacta]: «la cartera inicial deberá ser revisada por un contador público independiente»
- R: x1 Excepcion —exceptua_obligacion→ o12 Obligacion
- R: x2 Excepcion —exceptua→ r3 Restriccion
- R: c16 Condicion —condicion_de→ o16 Obligacion
- R: c_x2 Condicion —condicion_de→ x2 Excepcion
- R: c21 Condicion —condicion_de→ o21 Obligacion
- R: o1 Obligacion —regula→ op_tit Operacion
- R: o18 Obligacion —regula→ op_tit Operacion
- R: r1 Restriccion —prohibe→ op_tit Operacion
- R: r3 Restriccion —prohibe→ op_tit Operacion
- R: r4 Restriccion —prohibe→ op_tit Operacion
- R: r2 Restriccion —limita→ op_tit Operacion
- R: o10 Obligacion —aplica_a→ Sujeto (mención «El originante o fiduciario»)
- R: o11 Obligacion —aplica_a→ Sujeto (mención «el originante o fiduciario»)
- R: o13 Obligacion —aplica_a→ Sujeto (mención «El originante»)
- R: o14 Obligacion —aplica_a→ Sujeto (mención «el originante»)
- R: o16 Obligacion —aplica_a→ Sujeto (mención «el originante/fiduciario de la titulización»)
- R: o7 Obligacion —aplica_a→ Sujeto (mención «El originante de la titulización»)
- Omisión `relacion_sin_predicado` [exacta]: «El originante o fiduciario deberá verificar que los activos cumplan con las siguientes condiciones» — Los sujetos 'originante', 'fiduciario' no están en el catálogo; sus aplica_a se emitieron sin sujeto_id.
- Omisión `fuera_de_tipos` [exacta]: «Ello para evitar, por ejemplo, que se originen carteras con el solo fin de transferirlas.» — Declaración de finalidad del criterio de experiencia; no cambia el alcance de la norma.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «refinanciación distribuida» | `omitido` |  | sin extraer: la cláusula «Se podrá contar con la refinanciación o venta… siempre que…» no está en ninguna entidad (o2 cubre solo el principio d) ni en una omisión |
| 2 | «valores residuales no significativos» | `omitido` |  | sin extraer (misma cláusula ausente) |
| 3 | «minoristas 5 años» | `dentro_de_norma` |  | dentro de la Obligacion o8 («5 años minoristas», umbral); sin Condicion |
| 4 | «resto 7» | `dentro_de_norma` |  | dentro de la Obligacion o9 (umbral «durante 7 años») |
| 5 | «salvo el período de 2 años» | `dentro_de_norma` |  | dentro de la Obligacion o10 (descripción y umbral «el período de 2 años»); sin Excepcion |
| 6 | «condiciones a) a d)» (a)) | `dentro_de_norma` |  | dentro de la Obligacion o10 «Verificar condiciones a)-d)» |
| 7 | «condiciones a) a d)» (b)) | `dentro_de_norma` |  | dentro de la Obligacion o10 |
| 8 | «condiciones a) a d)» (c)) | `dentro_de_norma` |  | dentro de la Obligacion o10 |
| 9 | «condiciones a) a d)» (d)) | `dentro_de_norma` |  | dentro de la Obligacion o10 |

## `cap::3.1.2.2` — Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos.
> *heredado:* 3.1. Tratamiento de las titulizaciones.
> *heredado:* Se denomina "posición de titulización" a la exposición a una titulización (o retitulización), tradicional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes conceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos ("AssetBacked Securities", ABS) y bonos de titulización hipotecaria ("Mortgage-Backed Securities", MBS)–, mejoras crediticias, facilidades de liquidez, "swaps" de tasa de interés o de monedas y derivados de crédito. Las reservas ("reserve accounts"), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo también el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad económica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una determinada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> *heredado:* 3.1.2. Entidad financiera originante.
> *propio:* 3.1.2.2. Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional sólo si se satisface la totalidad de los siguientes requisitos operativos –debiendo computar exigencia de capital por las posiciones de titulización que conserve–: i) Se ha transferido a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas. ii) La entidad cedente no mantiene un control directo ni indirecto (como ser a través de una sociedad controlada) sobre las exposiciones transferidas. Ellas han sido aisladas de la cedente a los efectos jurídicos de forma tal que están fuera de su alcance y del de sus acreedores, incluso en los casos de liquidación o quiebra. Estas condiciones deberán estar avaladas por dictamen jurídico. Se considera que la cedente mantiene el control efectivo de las exposiciones transferidas si: a) puede recomprarlas con el objeto de realizar sus beneficios, o b) está obligada a conservar su riesgo. El mantenimiento por parte de la cedente de la administración de las exposiciones subyacentes no implicará un control indirecto sobre ellas. iii) Los títulos valores emitidos no son obligaciones de la cedente. En consecuencia, los inversores que compren los títulos valores sólo deberán tener derechos frente al conjunto subyacente de exposiciones. iv)La cesión se ha efectuado a un "Ente de Propósito Especial" (SPE) y los inversores pueden gravar o enajenar sus títulos valores sin restricción. v) Las opciones de exclusión satisfacen las condiciones estipuladas en el punto 3.1.4. vi)La titulización no contiene cláusulas mediante las cuales: a) se obligue a la originante a alterar las exposiciones subyacentes con el objeto de mejorar su calidad crediticia, a menos que esto se logre mediante su venta –a precios de mercado– a terceros no vinculados a ésta; b) la entidad financiera deba incrementar su posición a primera pérdida –es decir, su exposición al tramo que absorbe las pérdidas en primer término– o aumentar las mejoras crediticias provistas, con posterioridad al inicio de la operación; o c) se aumente el rendimiento pagadero a las partes distintas de la originante, como pueden ser los inversores o terceros proveedores de mejoras crediticias, en respuesta a un deterioro de la calidad crediticia de las exposiciones subyacentes. vii) No se incluyen opciones de rescisión o eventos desencadenantes de la extinción del contrato –excepto que se trate de opciones de exclusión admitidas (punto 3.1.4.) o que la extinción se deba a cambios impositivos o regulatorios específicos–, ni se incluyen cláusulas de amortización anticipada que –de acuerdo con lo previsto en el punto 3.1.8.1.– impliquen que la titulización no cumple con los requerimientos operacionales del presente punto.

### Extracción (código A)

- Rechazos del validador r2: relacion:firma_invalida
- **op1 Operacion** «Exclusión de exposiciones titulizadas del cálculo de APR» — Exclusión, al calcular los activos ponderados por riesgo, de las exposiciones objeto de una titulización tradicional, por la entidad originante · props: `{"tipo": "otra"}` · tramo [exacta]: «podrá excluir las exposiciones objeto de una titulización tradicional»
- **pot1 Potestad** «Exclusión de exposiciones titulizadas de los APR» — La entidad originante puede excluir del cálculo de activos ponderados por riesgo las exposiciones objeto de una titulización tradicional, sólo si se satisface la totalidad de los requisitos operativos i) a vii) · tramo [exacta]: «Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional sólo si se satisface la totalidad de los siguientes requisitos operativos»
- **ob1 Obligacion** «Computar capital por posiciones de titulización conservadas» — La entidad originante que excluye las exposiciones debe computar exigencia de capital por las posiciones de titulización que conserve · props: `{"tipo": "calculo"}` · tramo [exacta]: «debiendo computar exigencia de capital por las posiciones de titulización que conserve»
- **c1 Condicion** «Transferencia a terceros del riesgo de crédito» — Requisito i): se transfirió a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas · tramo [exacta]: «Se ha transferido a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas.»
- **c2 Condicion** «Cedente sin control y exposiciones aisladas» — Requisito ii): la cedente no mantiene control directo ni indirecto sobre las exposiciones transferidas, que han sido aisladas de la cedente a efectos jurídicos, fuera de su alcance y del de sus acreedores, incluso en liquidación o quiebra; estas condiciones deberán estar avaladas por dictamen jurídico. La administración de las exposiciones subyacentes por la cedente no implica control indirecto · tramo [exacta]: «La entidad cedente no mantiene un control directo ni indirecto (como ser a través de una sociedad controlada) sobre las exposiciones transferidas.»
- **c3 Condicion** «Títulos no son obligaciones de la cedente» — Requisito iii): los títulos valores emitidos no son obligaciones de la cedente; los inversores sólo deben tener derechos frente al conjunto subyacente de exposiciones · tramo [exacta]: «Los títulos valores emitidos no son obligaciones de la cedente.»
- **c4 Condicion** «Cesión a SPE y títulos libremente gravables o enajenables» — Requisito iv): la cesión se efectuó a un Ente de Propósito Especial (SPE) y los inversores pueden gravar o enajenar sus títulos valores sin restricción · tramo [no]: «La cesión se ha efectuado a un "Ente de Propósito Especial" (SPE) y los in-»
- **c5 Condicion** «Opciones de exclusión conformes al punto 3.1.4» — Requisito v): las opciones de exclusión satisfacen las condiciones estipuladas en el punto 3.1.4 · tramo [exacta]: «Las opciones de exclusión satisfacen las condiciones estipuladas en el punto»
- **c6 Condicion** «Sin cláusulas de alteración, mejora o mayor rendimiento» — Requisito vi): la titulización no contiene cláusulas que obliguen a la originante a alterar las exposiciones subyacentes para mejorar su calidad crediticia (salvo venta a precios de mercado a terceros no vinculados), que obliguen a incrementar su posición a primera pérdida o las mejoras crediticias tras el inicio de la operación, ni que aumenten el rendimiento pagadero a partes distintas de la ori… · tramo [exacta]: «La titulización no contiene cláusulas mediante las cuales:»
- **c7 Condicion** «Sin opciones de rescisión ni amortización anticipada incumplidora» — Requisito vii): no se incluyen opciones de rescisión o eventos desencadenantes de la extinción del contrato (excepto opciones de exclusión admitidas del punto 3.1.4 o extinción por cambios impositivos o regulatorios específicos), ni cláusulas de amortización anticipada que, según el punto 3.1.8.1, impliquen que la titulización no cumple los requerimientos operacionales · tramo [no]: «No se incluyen opciones de rescisión o eventos desencadenantes de la ex-»
- **d1 Definicion** «Control efectivo de la cedente sobre exposiciones transferidas» — Se considera que la cedente mantiene el control efectivo de las exposiciones transferidas si puede recomprarlas con el objeto de realizar sus beneficios, o está obligada a conservar su riesgo · props: `{"termino": "control efectivo"}` · tramo [exacta]: «Se considera que la cedente mantiene el control efectivo de las exposiciones transferidas si:»
- R: pot1 Potestad —aplica_a→ Sujeto (mención «la entidad originante»)
- R: ob1 Obligacion —aplica_a→ Sujeto (mención «la entidad originante»)
- R: Sujeto (mención «la entidad originante») —ejecuta→ op1 Operacion
- R: c1 Condicion —condicion_de→ pot1 Potestad
- R: c2 Condicion —condicion_de→ pot1 Potestad
- R: c3 Condicion —condicion_de→ pot1 Potestad
- R: c4 Condicion —condicion_de→ pot1 Potestad
- R: c5 Condicion —condicion_de→ pot1 Potestad
- R: c6 Condicion —condicion_de→ pot1 Potestad
- R: c7 Condicion —condicion_de→ pot1 Potestad

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:15 | sí | «En los casos en que exista incertidumbre acerca de si una determinada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que e…» | `ausente` |  | ninguna entidad ni omisión cubre la oración del heredado (las omisiones de H y K refieren a otros tramos) |

## `cap::4.3.1.2` — Miembro compensador ("clearing member"): es un miembro –participante

Grupos: omisiones.

### Texto

> *heredado:* Sección 4. Capital mínimo por riesgo de crédito de contraparte.
> *heredado:* 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con entidades de
> *heredado:* contraparte central. Comprende a aquellas exposiciones de las entidades financieras con entidades de contraparte central (CCP) que se originen en derivados OTC o negociados en mercados de valores y en operaciones de financiación con títulos valores ("Securities Financing Transactions", SFT) y operaciones de liquidación diferida –definidas en el punto 4.2.–. No están comprendidas las exposiciones originadas en operaciones al contado y que involucren títulos valores, oro o moneda extranjera, cuya exigencia de capital se calculará conforme a lo previsto en el punto 4.1.
> *heredado:* 4.3.1. Definiciones.
> *propio:* 4.3.1.2. Miembro compensador ("clearing member"): es un miembro –participante directo– de la CCP habilitado para realizar transacciones con dicha CCP, ya sea por cuenta propia o como intermediario entre la CCP y otros participantes del mercado. A los efectos del cálculo de la exigencia de capital, cuando una CCP tenga vínculos con una segunda CCP ésta será considerada como miembro compensador respecto de la primera. Dependerá de los acuerdos entre ambas que las garantías aportadas por la segunda a la primera sean tratadas como margen inicial o contribución a un fondo de garantía constituido para hacer frente a incumplimientos ("default fund").

### Extracción (código A)

- **d1 Definicion** «Miembro compensador (clearing member)» — Miembro –participante directo– de la CCP habilitado para realizar transacciones con dicha CCP, ya sea por cuenta propia o como intermediario entre la CCP y otros participantes del mercado. · props: `{"termino": "Miembro compensador"}` · tramo [exacta]: «Miembro compensador ("clearing member"): es un miembro –participante directo– de la CCP habilitado para realizar transacciones con dicha CCP, ya sea por cuenta propia o como intermediario entre la CCP y otros participantes del mercado.»
- **d2 Definicion** «CCP vinculada a otra CCP: miembro compensador» — A los efectos del cálculo de la exigencia de capital, cuando una CCP tenga vínculos con una segunda CCP, ésta es considerada miembro compensador respecto de la primera. · props: `{"termino": "Miembro compensador"}` · tramo [exacta]: «A los efectos del cálculo de la exigencia de capital, cuando una CCP tenga vínculos con una segunda CCP ésta será considerada como miembro compensador respecto de la primera.»
- Omisión `fuera_de_tipos` [exacta]: «Dependerá de los acuerdos entre ambas que las garantías aportadas por la segunda a la primera sean tratadas como margen inicial o contribución a un fondo de garantía constituido para hacer frente a incumplimientos ("default fund").» — Regla de tratamiento de garantías que depende de los acuerdos entre las CCP; no manda ni prohíbe ni habilita conducta del sujeto regulado. Habría sido una Definicion o Condicion, pero no encaja con pr…

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:21 | sí | «A los efectos del cálculo de la exigencia de capital» | `extraida_tramo_verificado` |  | d2 Definicion [exacta], tramo que contiene «A los efectos del cálculo de la exigencia de capital, cuando una CCP…» |

## `cap::5.2.1.3` — No deberá existir una correlación positiva sustancial entre la calidad crediticia

Grupos: omisiones.

### Texto

> *heredado:* Sección 5. Cobertura del riesgo de crédito.
> *heredado:* A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las técnicas previstas en el punto 5.1. La presente sección contempla, además, el cálculo de la exposición a las operaciones de financiación con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sección 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.
> *heredado:* 5.2. Requisitos para la aplicación de técnicas de coberturas del riesgo de crédito.
> *heredado:* 5.2.1. Requisitos generales.
> *propio:* 5.2.1.3. No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía –por ejemplo, los títulos valores emitidos por la contraparte o un vinculado a ella, no son admisibles–.

### Extracción (código A)

- **op1 Operacion** «Cobertura del riesgo de crédito con garantías» — Aplicación de técnicas de cobertura del riesgo de crédito (CRC) mediante garantías, a los efectos del cómputo de la exigencia de capital por riesgo de crédito. · props: `{"tipo": "cobertura del riesgo de crédito"}` · tramo [exacta]: «No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía»
- **r1 Restriccion** «Sin correlación positiva sustancial calidad crediticia-garantía» — No debe existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía; por ejemplo, los títulos valores emitidos por la contraparte o un vinculado a ella no son admisibles. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía –por ejemplo, los títulos valores emitidos por la contraparte o un vinculado a ella, no son admisibles–»
- R: r1 Restriccion —limita→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:22 | no | «por ejemplo» | `extraida_tramo_verificado` |  | r1 Restriccion [exacta], tramo que contiene «–por ejemplo, los títulos valores…» |

## `cap::6.2.3.5` — Exigencia de capital por derivados.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 6. Capital mínimo por riesgo de mercado.
> *heredado:* 6.2. Exigencia de capital por riesgo de tasa de interés.
> *heredado:* La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títulos de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las acciones preferidas no convertibles. Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera. Las acciones preferidas convertibles a un precio predeterminado en acciones ordinarias de la emisora se tratarán según cómo se negocien, como títulos de deuda o como acciones. La exigencia se obtendrá como la suma de dos exigencias calculadas por separado: una por el riesgo específico de cada instrumento, ya sea que se trate de una posición vendida o comprada, y otra por el riesgo general de mercado –vinculado al efecto de cambios en la tasa de interés sobre la cartera–, en la que se podrán compensar las posiciones compradas y vendidas en diferentes instrumentos. Para los instrumentos derivados, serán de aplicación las disposiciones establecidas en el punto 6.2.3.
> *heredado:* 6.2.3. Tratamiento de los derivados de tasas de interés.
> *propio:* 6.2.3.5. Exigencia de capital por derivados. i) Compensación admitida entre posiciones compensadas. Las posiciones compradas y vendidas, reales o nocionales, en idénticos instrumentos se podrán excluir del cómputo del riesgo específico y del riesgo general de mercado. Se entiende que los instrumentos son idénticos si tienen igual emisor, cupón, moneda y vencimiento. Del mismo modo, si se corresponden exactamente, se podrán excluir los futuros o "forwards" y sus subyacentes, pero sin dejar de computar el lado de la operación que representa el plazo hasta el vencimiento de la operación a término. Cuando el futuro o "forward" permita entregar una gama de instrumentos, la exclusión sólo será posible en la medida que la entidad pueda identificar fácilmente el título subyacente cuya entrega es más conveniente para el intermediario con la posición vendida y demostrar que los cambios de los precios del título más barato ("cheapest-to-deliver") y del futuro o "forward" están estrechamente alineados. No se permitirá la exclusión o compensación de posiciones en diferentes monedas, por lo que los lados de los "swaps" de monedas y de los contratos a término sobre monedas se deberán tratar como posiciones nocionales en los instrumentos pertinentes e incluirse en el cálculo correspondiente a cada moneda. Asimismo, las entidades podrán excluir posiciones opuestas en la misma categoría de instrumentos si consideran que están compensadas, incluso en el caso de posiciones en el valor delta de una opción. Para que proceda la exclusión, las posiciones se deberán referir a los mismos subyacentes, tener el mismo valor nominal y estar denominadas en la misma moneda. Sujeto a las mismas condiciones, también se podrán compensar los lados de "swaps" diferentes. Además: a) cuando se trate de futuros, la exclusión sólo procederá si los nocionales e instrumentos subyacentes refieren a productos idénticos y sus vencimientos no difieren en más de 7 días corridos; b) cuando se trate de "swaps" y FRAs, la tasa de referencia de las posiciones a interés variable deberá ser idéntica y deberá haber una correspondencia cercana entre los cupones (dentro de un margen de 15 puntos básicos); c) en los casos de "swaps", FRAs y "forwards", la próxima fecha de reajuste del interés o el vencimiento -cuando se trate de posiciones con cupón fijo o "forwards"- se deberá producir: - a menos de un mes: en el mismo día; - entre un mes y un año: con una discrepancia máxima entre esas fechas de siete días corridos; - a un año: con una discrepancia máxima entre esas fechas de treinta días corridos. ii) Exigencia de capital por riesgo específico. Los "swaps" de monedas y tasas de interés, los FRAs, los "forwards" de moneda y los futuros de tasa de interés o sobre un índice de tasa de interés no estarán sujetos a exigencia por riesgo específico. No obstante, en el caso de futuros en los que el subyacente sea un título de deuda o un índice que represente una canasta de títulos de deuda, se aplicará la exigencia por riesgo específico acorde al riesgo de crédito del emisor, según se establece en el punto 6.2.1. iii) Exigencia de capital por riesgo general de mercado. La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las posiciones al contado-, con la sola excepción de las posiciones que estén compensadas con instrumentos idénticos, conforme a lo establecido en el acápite i) de este punto.

### Extracción (código A)

- **op_computo Operacion** «Cómputo de riesgo específico y general de mercado de derivados» — Cómputo de la exigencia de capital por riesgo específico y riesgo general de mercado de posiciones en derivados de tasa de interés · props: `{"tipo": "otra"}` · tramo [exacta]: «del cómputo del riesgo específico y del riesgo general de mercado»
- **p1 Potestad** «Exclusión de posiciones idénticas compradas y vendidas» — Las posiciones compradas y vendidas, reales o nocionales, en instrumentos idénticos (igual emisor, cupón, moneda y vencimiento) se pueden excluir del cómputo del riesgo específico y general de mercado. · tramo [exacta]: «Las posiciones compradas y vendidas, reales o nocionales, en idénticos instrumentos se podrán excluir del cómputo del riesgo específico y del riesgo general de mercado.»
- **d1 Definicion** «Instrumentos idénticos» — Instrumentos que tienen igual emisor, cupón, moneda y vencimiento. · props: `{"termino": "instrumentos idénticos"}` · tramo [exacta]: «Se entiende que los instrumentos son idénticos si tienen igual emisor, cupón, moneda y vencimiento.»
- **p2 Potestad** «Exclusión de futuros/forwards y subyacentes correspondientes» — Si se corresponden exactamente, se pueden excluir los futuros o forwards y sus subyacentes, sin dejar de computar el lado de la operación que representa el plazo hasta el vencimiento de la operación a término. · tramo [exacta]: «si se corresponden exactamente, se podrán excluir los futuros o "forwards" y sus subyacentes, pero sin dejar de computar el lado de la operación que representa el plazo hasta el vencimiento de la operación a término»
- **r1 Restriccion** «Exclusión con gama de instrumentos: título más barato identificable» — Cuando el futuro o forward permita entregar una gama de instrumentos, la exclusión solo es posible si la entidad identifica fácilmente el título subyacente cheapest-to-deliver y demuestra que sus precios y los del futuro o forward están estrechamente alineados. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «la exclusión sólo será posible en la medida que la entidad pueda identificar fácilmente el título subyacente cuya entrega es más conveniente para el intermediario con la posición vendida y demostrar que los cambios de los precios del título más barato ("cheapest-to-deliver") y del futuro o "forward" están estrechamente…»
- **r2 Restriccion** «Prohibición de excluir o compensar posiciones en distintas monedas» — No se permite la exclusión o compensación de posiciones en diferentes monedas. · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «No se permitirá la exclusión o compensación de posiciones en diferentes monedas»
- **o1 Obligacion** «Tratar lados de swaps y forwards de monedas como posiciones nocionales» — Los lados de los swaps de monedas y de los contratos a término sobre monedas se tratan como posiciones nocionales en los instrumentos pertinentes y se incluyen en el cálculo correspondiente a cada moneda. · props: `{"tipo": "calculo"}` · tramo [exacta]: «los lados de los "swaps" de monedas y de los contratos a término sobre monedas se deberán tratar como posiciones nocionales en los instrumentos pertinentes e incluirse en el cálculo correspondiente a cada moneda»
- **p3 Potestad** «Exclusión de posiciones opuestas en misma categoría» — Las entidades pueden excluir posiciones opuestas en la misma categoría de instrumentos si consideran que están compensadas, incluso posiciones en el valor delta de una opción. · tramo [exacta]: «las entidades podrán excluir posiciones opuestas en la misma categoría de instrumentos si consideran que están compensadas, incluso en el caso de posiciones en el valor delta de una opción»
- **c1 Condicion** «Mismos subyacentes, valor nominal y moneda» — Para que proceda la exclusión de posiciones opuestas, las posiciones deben referirse a los mismos subyacentes, tener el mismo valor nominal y estar denominadas en la misma moneda. · tramo [exacta]: «las posiciones se deberán referir a los mismos subyacentes, tener el mismo valor nominal y estar denominadas en la misma moneda»
- **p4 Potestad** «Compensación de lados de swaps diferentes» — Sujeto a las mismas condiciones (mismos subyacentes, valor nominal y moneda), se pueden compensar los lados de swaps diferentes. · tramo [exacta]: «también se podrán compensar los lados de "swaps" diferentes»
- **r3 Restriccion** «Futuros: exclusión solo con vencimientos hasta 7 días de diferencia» — En futuros, la exclusión solo procede si los nocionales e instrumentos subyacentes refieren a productos idénticos y los vencimientos no difieren en más de 7 días corridos. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['no difieren en más de 7 días corridos'] · tramo [exacta]: «cuando se trate de futuros, la exclusión sólo procederá si los nocionales e instrumentos subyacentes refieren a productos idénticos y sus vencimientos no difieren en más de 7 días corridos»
- **r4 Restriccion** «Swaps y FRAs: tasa idéntica y cupones dentro de 15 pb» — En swaps y FRAs, la exclusión exige tasa de referencia idéntica en posiciones a interés variable y correspondencia cercana entre cupones, dentro de un margen de 15 puntos básicos. · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "dentro de un margen de 15\npuntos básicos", "comparacion": "maximo_inclusivo", "base": "un margen de 15 puntos básicos", "regla_comparacion": "limite_relativo:compuesta:dentro_de", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['dentro de un margen de 15 puntos básicos'] · tramo [exacta]: «cuando se trate de "swaps" y FRAs, la tasa de referencia de las posiciones a interés variable deberá ser idéntica y deberá haber una correspondencia cercana entre los cupones (dentro de un margen de 15 puntos básicos)»
- **r5a Restriccion** «Swaps, FRAs y forwards: mismo día si menos de un mes» — En swaps, FRAs y forwards, la próxima fecha de reajuste del interés o el vencimiento, si es a menos de un mes, debe producirse el mismo día para excluir posiciones. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['a menos de un mes: en el mismo día'] · tramo [exacta]: «a menos de un mes: en el mismo día»
- **r5b Restriccion** «Swaps, FRAs y forwards: discrepancia máxima 7 días entre un mes y un año» — En swaps, FRAs y forwards, la próxima fecha de reajuste o el vencimiento entre un mes y un año debe tener una discrepancia máxima de siete días corridos. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['discrepancia máxima entre esas fechas de siete días corridos'] · tramo [exacta]: «entre un mes y un año: con una discrepancia máxima entre esas fechas de siete días corridos»
- **r5c Restriccion** «Swaps, FRAs y forwards: discrepancia máxima 30 días a un año» — En swaps, FRAs y forwards, la próxima fecha de reajuste o el vencimiento a un año debe tener una discrepancia máxima de treinta días corridos. · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "discrepancia máxima entre esas fechas de trein-\n  ta días corridos", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['discrepancia máxima entre esas fechas de treinta días corridos'] · tramo [exacta]: «a un año: con una discrepancia máxima entre esas fechas de treinta días corridos»
- **e1 Excepcion** «Sin exigencia por riesgo específico: swaps, FRAs, forwards de moneda, futuros de tasa» — Los swaps de monedas y tasas de interés, FRAs, forwards de moneda y futuros de tasa de interés o sobre un índice de tasa de interés no están sujetos a exigencia de capital por riesgo específico. · tramo [exacta]: «Los "swaps" de monedas y tasas de interés, los FRAs, los "forwards" de moneda y los futuros de tasa de interés o sobre un índice de tasa de interés no estarán sujetos a exigencia por riesgo específico.»
- **o2 Obligacion** «Exigencia por riesgo específico en futuros sobre títulos de deuda» — En futuros cuyo subyacente es un título de deuda o un índice que representa una canasta de títulos de deuda, se aplica la exigencia por riesgo específico acorde al riesgo de crédito del emisor, según el punto 6.2.1. · props: `{"tipo": "calculo"}` · tramo [exacta]: «en el caso de futuros en los que el subyacente sea un título de deuda o un índice que represente una canasta de títulos de deuda, se aplicará la exigencia por riesgo específico acorde al riesgo de crédito del emisor, según se establece en el punto 6.2.1»
- **o3 Obligacion** «Exigencia por riesgo general de mercado sobre todos los derivados» — La exigencia de capital por riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados, como a las posiciones al contado. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las posiciones al contado-»
- **e2 Excepcion** «Excepción: posiciones compensadas con instrumentos idénticos» — Quedan fuera de la exigencia por riesgo general de mercado las posiciones compensadas con instrumentos idénticos, conforme al acápite i). · tramo [exacta]: «con la sola excepción de las posiciones que estén compensadas con instrumentos idénticos, conforme a lo establecido en el acápite i) de este punto»
- R: r1 Restriccion —limita→ op_computo Operacion
- R: r2 Restriccion —prohibe→ op_computo Operacion
- R: r3 Restriccion —limita→ op_computo Operacion
- R: r4 Restriccion —limita→ op_computo Operacion
- R: r5a Restriccion —limita→ op_computo Operacion
- R: r5b Restriccion —limita→ op_computo Operacion
- R: r5c Restriccion —limita→ op_computo Operacion
- R: o1 Obligacion —regula→ op_computo Operacion
- R: o2 Obligacion —regula→ op_computo Operacion
- R: o3 Obligacion —regula→ op_computo Operacion
- R: c1 Condicion —condicion_de→ p3 Potestad
- R: c1 Condicion —condicion_de→ p4 Potestad
- R: e2 Excepcion —exceptua_obligacion→ o3 Obligacion
- R: p3 Potestad —aplica_a→ Sujeto_rol_alcance_capmin (mención «las entidades»)
- R: r1 Restriccion —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «instrumentos idénticos» | `dentro_de_norma` |  | dentro de la Potestad p1 (tramo «en idénticos instrumentos se podrán excluir») y como Definicion d1; sin Condicion |
| 2 | «futuro con gama de instrumentos» | `dentro_de_norma` |  | extraído como norma de otro tipo: r1 Restriccion —limita→ op_computo; sin Condicion |
| 3 | «a) futuros a 7 días» | `dentro_de_norma` |  | extraído como norma de otro tipo: r3 Restriccion con el umbral; sin Condicion |
| 4 | «b) swaps y FRAs» | `dentro_de_norma` |  | extraído como norma de otro tipo: r4 Restriccion con el umbral; sin Condicion |
| 5 | «c) tramos de fechas» | `dentro_de_norma` |  | extraído como normas de otro tipo: r5a, r5b y r5c Restriccion con los umbrales; sin Condicion |
| 6 | «futuros sobre títulos» | `dentro_de_norma` |  | extraído como norma de otro tipo: o2 Obligacion («en el caso de futuros en los que el subyacente sea un título de deuda…»); sin Excepcion ni Condicion |

## `cap::6.3.2.2` — Exigencia de capital por derivados sobre acciones.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 6. Capital mínimo por riesgo de mercado.
> *heredado:* 6.3. Exigencia de capital por riesgo de posiciones en acciones.
> *heredado:* La exigencia de capital por el riesgo de mantener posiciones en acciones en la cartera de negociación alcanza a las posiciones compradas y vendidas en acciones ordinarias, títulos de deuda convertibles que se comporten como acciones y los compromisos para adquirir o vender acciones, así como en todo otro instrumento que tenga un comportamiento en el mercado similar al de las acciones, excluyendo a las acciones preferidas no convertibles, a las que se aplicará la exigencia por riesgo de tasa de interés descripta en el punto 6.2. Las posiciones compradas y vendidas en la misma especie podrán computarse en términos netos.
> *heredado:* 6.3.2. Tratamiento de los derivados sobre acciones.
> *heredado:* A excepción de las opciones sobre acciones e índices bursátiles, que se tratan en el punto 6.6., los restantes derivados sobre acciones y las posiciones fuera de balance sensibles a los cambios en los precios de mercado deberán incluirse en el cómputo de la exigencia. Esto comprende a los futuros, "forwards" y "swaps", tanto de acciones individuales como de índices bursátiles. Los derivados se convertirán en posiciones en su correspondiente subyacente.
> *propio:* 6.3.2.2. Exigencia de capital por derivados sobre acciones. i) Exigencia de capital por riesgo específico y por riesgo general de mercado. Cada posición compensada con una acción o índice bursátil idéntico podrá ser neteada en su totalidad, dando lugar a una única posición neta, vendida o comprada, sobre la que se aplicarán las exigencias de capital por riesgo específico y riesgo general de mercado. El riesgo de tasa de interés del derivado se computará conforme a lo indicado en el punto 6.2. ii) Exigencia de capital por índices. Además de la exigencia por riesgo general de mercado, se aplicará una exigencia de capital adicional de 2% de la posición neta, comprada o vendida, en contratos sobre índices calculados sobre carteras diversificadas de acciones a los efectos de cubrir factores tales como los riesgos de ejecución. Será objeto de revisión por parte de la Superintendencia de Entidades Financieras y Cambiarias que el ponderador de 2% se aplique sólo a índices bien diversificados y no, por ejemplo, a índices sectoriales. iii) Arbitraje. a) En el caso de las siguientes estrategias de arbitraje relacionadas con futuros, la exigencia de capital adicional de 2% del acápite ii) precedente se podrá aplicar sólo a uno de los índices (quedando exenta la posición contraria): - cuando la entidad asuma la posición contraria en exactamente el mismo índice pero a distintos vencimientos o mercados; - cuando la entidad mantenga la posición opuesta en contratos a idéntica fecha pero en índices diferentes, aunque similares, a cuyo efecto deberá tener a disposición de la Superintendencia de Entidades Financieras y Cambiarias evidencia de que ambos índices contienen suficientes componentes comunes como para justificar tal compensación. b) Se aplicará una exigencia de capital de 4% a las posiciones que surjan de estrategias de arbitraje, en las que un futuro sobre un índice amplio se calce con una canasta de acciones y, además, se verifique que: - la estrategia haya sido adoptada en forma deliberada y se vigile y gestione en forma particularizada; - la composición de la canasta de acciones represente al menos el 90% del índice si se descompone en sus componentes nocionales; - la exigencia de capital de 4%, que refleja los riesgos de divergencia y ejecución, equivale a una exigencia de 2% del valor bruto de las posiciones en cada lado. La exigencia es aplicable incluso si todas las acciones se mantienen en proporciones idénticas a las del índice. Cualquier valor excedente de las acciones que componen la canasta por encima del valor del futuro o cualquier valor excedente del futuro sobre el valor de la canasta se considerará como una posición abierta, comprada o vendida. c) Se podrán compensar –es decir, no aplicar exigencias de capital– posiciones contrarias, incluso tratándose de posiciones en mercados diferentes o de certificados de depósito de acciones sólo si se tienen en cuenta todos los costos de conversión, cuando los hubiera. Todo riesgo de tipo de cambio que surja de estas posiciones deberá computarse según se establece en el punto 6.4.

### Extracción (código A)

- **op_neteo Operacion** «Neteo de posiciones en derivados sobre acciones» — Neteo total de cada posición compensada con una acción o índice bursátil idéntico, dando lugar a una única posición neta, vendida o comprada, sobre la que se aplican las exigencias por riesgo específico y general de mercado. · props: `{"tipo": "otra"}` · tramo [exacta]: «Cada posición compensada con una acción o índice bursátil idéntico podrá ser neteada en su totalidad, dando lugar a una única posición neta, vendida o comprada»
- **pot_neteo Potestad** «Neteo total de posición compensada idéntica» — Cada posición compensada con una acción o índice bursátil idéntico podrá ser neteada en su totalidad, dando lugar a una única posición neta sobre la que se aplican las exigencias de capital por riesgo específico y general de mercado. · tramo [exacta]: «Cada posición compensada con una acción o índice bursátil idéntico podrá ser neteada en su totalidad»
- **ob_tasa Obligacion** «Riesgo de tasa de interés del derivado: punto 6.2» — El riesgo de tasa de interés del derivado se computa conforme a lo indicado en el punto 6.2. · props: `{"tipo": "calculo"}` · tramo [exacta]: «El riesgo de tasa de interés del derivado se computará conforme a lo indicado en el punto 6.2.»
- **ob_indices Obligacion** «Exigencia adicional 2% sobre índices» — Además de la exigencia por riesgo general de mercado, se aplica una exigencia de capital adicional de 2% de la posición neta, comprada o vendida, en contratos sobre índices calculados sobre carteras diversificadas de acciones, para cubrir factores como los riesgos de ejecución. · props: `{"tipo": "calculo"}` · umbral: ['adicional de 2% de la posición neta'] · tramo [exacta]: «se aplicará una exigencia de capital adicional de 2% de la posición neta, comprada o vendida, en contratos sobre índices calculados sobre carteras diversificadas de acciones»
- **ob_revision Potestad** «Revisión SEFyC del ponderador 2% solo en índices diversificados» — La SEFyC revisa que el ponderador de 2% se aplique sólo a índices bien diversificados y no, por ejemplo, a índices sectoriales. · tramo [exacta]: «Será objeto de revisión por parte de la Superintendencia de Entidades Financieras y Cambiarias que el ponderador de 2% se aplique sólo a índices bien diversificados y no, por ejemplo, a índices sectoriales.»
- **ex_arb_a Excepcion** «Arbitraje con futuros: 2% sobre un solo índice» — En estrategias de arbitraje con futuros (misma posición contraria en el mismo índice a distintos vencimientos o mercados, o posición opuesta a idéntica fecha en índices similares), la exigencia adicional de 2% del acápite ii) se aplica sólo a uno de los índices, quedando exenta la posición contraria. · umbral: ['adicional de 2% del acápite ii)'] · tramo [exacta]: «la exigencia de capital adicional de 2% del acápite ii) precedente se podrá aplicar sólo a uno de los índices (quedando exenta la posición contraria)»
- **cond_a1 Condicion** «Posición contraria en mismo índice, distintos vencimientos o mercados» — La entidad asume la posición contraria en exactamente el mismo índice pero a distintos vencimientos o mercados. · tramo [exacta]: «cuando la entidad asuma la posición contraria en exactamente el mismo índice pero a distintos vencimientos o mercados»
- **cond_a2 Condicion** «Posición opuesta a idéntica fecha en índices similares» — La entidad mantiene la posición opuesta en contratos a idéntica fecha pero en índices diferentes, aunque similares. · tramo [exacta]: «cuando la entidad mantenga la posición opuesta en contratos a idéntica fecha pero en índices diferentes, aunque similares»
- **ob_evidencia Obligacion** «Evidencia de componentes comunes a disposición de SEFyC» — En el arbitraje con posición opuesta en índices diferentes, aunque similares, la entidad debe tener a disposición de la SEFyC evidencia de que ambos índices contienen suficientes componentes comunes como para justificar la compensación. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «deberá tener a disposición de la Superintendencia de Entidades Financieras y Cambiarias evidencia de que ambos índices contienen suficientes componentes comunes como para justificar tal compensación»
- **ob_arb4 Obligacion** «Exigencia 4% en arbitraje futuro de índice amplio y canasta» — Se aplica una exigencia de capital de 4% (equivalente a 2% del valor bruto de las posiciones en cada lado) a las posiciones de estrategias de arbitraje en que un futuro sobre un índice amplio se calce con una canasta de acciones, aplicable incluso si todas las acciones se mantienen en proporciones idénticas a las del índice; el valor excedente de la canasta sobre el futuro, o del futuro sobre la c… · props: `{"tipo": "calculo"}` · umbral: ['exigencia de capital de 4%', '2% del valor bruto de las posiciones en cada lado'] · tramo [exacta]: «Se aplicará una exigencia de capital de 4% a las posiciones que surjan de estrategias de arbitraje, en las que un futuro sobre un índice amplio se calce con una canasta de acciones»
- **cond_b1 Condicion** «Estrategia deliberada, vigilada y gestionada en forma particularizada» — La estrategia de arbitraje fue adoptada en forma deliberada y se vigila y gestiona en forma particularizada. · tramo [exacta]: «la estrategia haya sido adoptada en forma deliberada y se vigile y gestione en forma particularizada»
- **cond_b2 Condicion** «Canasta representa al menos 90% del índice» — La composición de la canasta de acciones representa al menos el 90% del índice si se descompone en sus componentes nocionales. · umbral: ['al menos el 90% del índice'] · tramo [exacta]: «la composición de la canasta de acciones represente al menos el 90% del índice si se descompone en sus componentes nocionales»
- **pot_comp Potestad** «Compensación de posiciones contrarias sin exigencia» — Se pueden compensar (no aplicar exigencias de capital) posiciones contrarias, incluso en mercados diferentes o de certificados de depósito de acciones. · tramo [exacta]: «Se podrán compensar –es decir, no aplicar exigencias de capital– posiciones contrarias, incluso tratándose de posiciones en mercados diferentes o de certificados de depósito de acciones»
- **cond_comp Condicion** «Considerar todos los costos de conversión» — La compensación de posiciones contrarias procede sólo si se tienen en cuenta todos los costos de conversión, cuando los hubiera. · tramo [exacta]: «sólo si se tienen en cuenta todos los costos de conversión, cuando los hubiera»
- **ob_tc Obligacion** «Riesgo de tipo de cambio según punto 6.4» — Todo riesgo de tipo de cambio que surja de las posiciones compensadas debe computarse según el punto 6.4. · props: `{"tipo": "calculo"}` · tramo [exacta]: «Todo riesgo de tipo de cambio que surja de estas posiciones deberá computarse según se establece en el punto 6.4.»
- R: ex_arb_a Excepcion —exceptua_obligacion→ ob_indices Obligacion
- R: cond_a1 Condicion —condicion_de→ ex_arb_a Excepcion
- R: cond_a2 Condicion —condicion_de→ ex_arb_a Excepcion
- R: cond_b1 Condicion —condicion_de→ ob_arb4 Obligacion
- R: cond_b2 Condicion —condicion_de→ ob_arb4 Obligacion
- R: cond_comp Condicion —condicion_de→ pot_comp Potestad
- R: ob_evidencia Obligacion —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- R: pot_neteo Potestad —aplica_a→ Sujeto (mención «Cada posición compensada»)
- R: ob_revision Potestad —aplica_a→ Sujeto_sefyc (mención «la Superintendencia de Entisdades Financieras y Cambiarias»)

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «arbitrajes del a) (dos guiones)» (primer guion) | `condicion_con_relacion` |  | cond_a1 Condicion «Posición contraria en mismo índice, distintos vencimientos o mercados» —condicion_de→ ex_arb_a Excepcion (el 2 % sobre un solo índice) |
| 2 | «arbitrajes del a) (dos guiones)» (segundo guion) | `condicion_con_relacion` |  | cond_a2 Condicion «Posición opuesta a idéntica fecha en índices similares» —condicion_de→ ex_arb_a Excepcion |
| 3 | «b) canasta de al menos 90 %» | `condicion_con_relacion` |  | cond_b2 Condicion con el umbral «al menos el 90% del índice» —condicion_de→ ob_arb4 Obligacion |
| 4 | «c) sólo si se tienen en cuenta los costos» | `condicion_con_relacion` |  | cond_comp Condicion —condicion_de→ pot_comp Potestad |

## `cap::7.1.3::intro` — [bloque intro] Divulgación.

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Capital mínimo por riesgo operacional.
> *heredado:* 7.1. Exigencia de capital por riesgo operacional para entidades del grupo 1.
> *heredado:* 7.1.3. Divulgación.
> *propio:* Las entidades financieras deben dar a conocer al público, de manera regular, a través de sus páginas de Internet o reportes –conforme a los requerimientos que al efecto se establezcan– lo siguiente:

### Extracción (código A)

(sin entidades ni omisiones)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:28 | sí (remisión pura) | «conforme a los requerimientos que al efecto se establezcan» | `ausente` |  | ninguna entidad ni omisión cubre la remisión «conforme a los requerimientos que al efecto se establezcan» |

## `cap::7.3.2` — El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Capital mínimo por riesgo operacional.
> *heredado:* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en grupo 1 y grupo 2, conforme a lo previsto en la Sección 2.
> *heredado:* 7.3. Límite para las entidades del grupo 2.
> *heredado:* La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar:
> *propio:* 7.3.2. El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses –anteriores al mes a que corresponda la determinación de la exigencia– de la exigencia de capital mínimo por riesgo de crédito calculada según lo previsto en la Sección 2., expresada en moneda homogénea del mes anterior al que se efectúa el cálculo. El límite máximo establecido precedentemente se reducirá a 11% cuando la entidad financiera cuente con calificación 1, 2 o 3 conforme a la valoración otorgada por la SEFYC, en oportunidad de la última inspección efectuada, respecto de todos los siguientes aspectos: la entidad en su conjunto, sus sistemas informáticos y la labor de los responsables de la evaluación de sus sistemas de control interno. En los casos en que la entidad financiera cuente en todos los citados aspectos con calificación 1 o 2, el límite máximo disminuirá a 7%. A este efecto, se considerará la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación.

### Extracción (código A)

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

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «grupo B (17 %)» | `dentro_de_norma` |  | dentro de la Restriccion r1 (tramo «El 17% en el caso de entidades del grupo B…»); sin Condicion |
| 2 | «calificación 1, 2 o 3 (11 %)» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ r2 Restriccion |
| 3 | «calificación 1 o 2 (7 %)» | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ r3 Restriccion |

## `cap::8.2.3::cierre` — [bloque cierre] Patrimonio neto complementario –capital de nivel dos– (PNc).

Grupos: omisiones.

### Texto

> *heredado:* Sección 8. Responsabilidad patrimonial computable.
> *heredado:* 8.2. Conceptos computables.
> *heredado:* 8.2.3. Patrimonio neto complementario –capital de nivel dos– (PNc).
> *propio:* A los conceptos citados en los puntos precedentes se les restarán, de corresponder, los conceptos deducibles previstos en el punto 8.4.2.

### Extracción (código A)

- **o1 Obligacion** «Restar conceptos deducibles del PNc» — A los conceptos computables citados en los puntos precedentes del PNc (capital de nivel dos) se les restan, de corresponder, los conceptos deducibles previstos en el punto 8.4.2. · props: `{"tipo": "calculo"}` · tramo [exacta]: «A los conceptos citados en los puntos precedentes se les restarán, de corresponder, los conceptos deducibles previstos en el punto 8.4.2.»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:26 | no | «de corresponder» | `extraida_tramo_verificado` |  | Obligacion (o1/e1) [exacta] cuyo tramo contiene «de corresponder» |

## `cla::2.1.6` — Obligaciones negociables –incluye las subordinadas– y títulos de deuda de fideicomisos

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Financiaciones comprendidas.
> *heredado:* 2.1. Conceptos incluidos.
> *propio:* 2.1.6. Obligaciones negociables –incluye las subordinadas– y títulos de deuda de fideicomisos financieros no alcanzados por las normas sobre "Fideicomisos financieros comprendidos en la Ley de Entidades Financieras", valuados a costo amortizado y/o a valor razonable con cambios en otros resultados integrales.

### Extracción (código A)

- **d1 Definicion** «Financiaciones comprendidas: obligaciones negociables y títulos de deuda» — Concepto incluido entre las financiaciones comprendidas: obligaciones negociables (incluidas las subordinadas) y títulos de deuda de fideicomisos financieros no alcanzados por las normas sobre "Fideicomisos financieros comprendidos en la Ley de Entidades Financieras", valuados a costo amortizado y/o a valor razonable con cambios en otros resultados integrales. · props: `{"termino": "Obligaciones negociables –incluye las subordinadas– y títulos de deuda de fideicomisos financieros"}` · tramo [exacta]: «Obligaciones negociables –incluye las subordinadas– y títulos de deuda de fideicomisos financieros no alcanzados por las normas sobre "Fideicomisos financieros comprendidos en la Ley de Entidades Financieras", valuados a costo amortizado y/o a valor razonable con cambios en otros resultados integrales.»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:9 | sí | «no alcanzados por las normas sobre "Fideicomisos financieros comprendidos en la Ley de Entidades Financieras"» | `extraida_tramo_verificado` |  | d1 Definicion [exacta], tramo que contiene «no alcanzados por las normas sobre…» |

## `cla::2.2.4.4` — En el caso de las garantías otorgadas localmente, deberán existir respecto de

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Financiaciones comprendidas.
> *heredado:* 2.2. Exclusiones.
> *heredado:* 2.2.4. Financiaciones y avales, fianzas y otras responsabilidades otorgados por sucursales y
> *heredado:* subsidiarias locales de entidades financieras del exterior, por cuenta y orden de su casa matriz o sus sucursales en otros países o de la entidad controlante, siempre que se observen los siguientes requisitos:
> *propio:* 2.2.4.4. En el caso de las garantías otorgadas localmente, deberán existir respecto de ellas contragarantías extendidas por la casa matriz o sus sucursales en otros países o por la entidad controlante del exterior, cuya efectivización opere en forma irrestricta a simple requerimiento de la filial o subsidiaria local y en modo inmediato a su eventual ejecución por parte del beneficiario.

### Extracción (código A)

- **c1 Condicion** «Contragarantías de casa matriz para garantías locales» — Requisito para la exclusión del punto 2.2.4 (financiaciones y avales, fianzas y otras responsabilidades otorgados por sucursales y subsidiarias locales de entidades financieras del exterior): en las garantías otorgadas localmente deben existir contragarantías extendidas por la casa matriz, sus sucursales en otros países o la entidad controlante del exterior, con efectivización irrestricta a simple… · tramo [exacta]: «En el caso de las garantías otorgadas localmente, deberán existir respecto de ellas contragarantías extendidas por la casa matriz o sus sucursales en otros países o por la entidad controlante del exterior, cuya efectivización opere en forma irrestricta a simple requerimiento de la filial o subsidiaria local y en modo i…»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:8 | sí | «siempre que se observen los siguientes requisitos» | `ausente` |  | ninguna entidad ni omisión cubre «siempre que se observen los siguientes requisitos» (heredado) |

## `cla::3.5::intro` — [bloque intro] Responsabilidad de la tarea de clasificación.

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Tarea de clasificación.
> *heredado:* 3.5. Responsabilidad de la tarea de clasificación.
> *propio:* La tarea de clasificación podrá ser encomendada:

### Extracción (código A)

(sin entidades ni omisiones)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:12 | sí | «La tarea de clasificación podrá ser encomendada» | `ausente` |  | salida sin entidades ni omisiones en la unidad (ninguna Potestad para «podrá ser encomendada») |

## `cla::6.5.1.1` — presente una situación financiera líquida, con bajo nivel y adecuada estructura

Grupos: omisiones.

### Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.1. En situación normal.
> *heredado:* El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financieros. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *propio:* 6.5.1.1. presente una situación financiera líquida, con bajo nivel y adecuada estructura de endeudamiento en relación con su capacidad de ganancia, y muestre una alta capacidad de pago de las deudas (capital e intereses) en las condiciones pactadas generando fondos -medido a través del análisis de su flujoen grado aceptable. El flujo de fondos no es susceptible de variaciones significativas ante modificaciones importantes en el comportamiento de las variables tanto propias como vinculadas a su sector de actividad. En el análisis que se lleve a cabo deberá tenerse en cuenta, de corresponder, la eventual incidencia que en su capacidad de pago pueda tener la situación en la que se encuentran los demás integrantes del grupo de contrapartes conectadas al cual pertenece.

### Extracción (código A)

- **d1 Definicion** «Indicador de situación normal: situación financiera líquida y alta capacidad de pago» — Indicador de la situación normal (cartera comercial): el cliente presenta una situación financiera líquida, con bajo nivel y adecuada estructura de endeudamiento en relación con su capacidad de ganancia, y muestra una alta capacidad de pago de las deudas (capital e intereses) en las condiciones pactadas, generando fondos en grado aceptable, medido a través del análisis de su flujo. El flujo de fon… · props: `{"termino": "situación normal"}` · no definidas: `{"modalidad": "Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:", "modalidad_clasificada": "no_clasificada"}` · tramo [exacta]: «Entre los indicadores que pueden reflejar esta situación se destacan que el cliente: […] presente una situación financiera líquida, con bajo nivel y adecuada estructura de endeudamiento en relación con su capacidad de ganancia, y muestre una alta capacidad de pago de las deudas (capital e intereses) en las condiciones …»
- **o1 Obligacion** «Considerar incidencia del grupo de contrapartes conectadas» — En el análisis de la capacidad de pago del cliente, de corresponder, se debe tener en cuenta la eventual incidencia de la situación de los demás integrantes del grupo de contrapartes conectadas al que pertenece. · props: `{"tipo": "calculo"}` · tramo [exacta]: «En el análisis que se lleve a cabo deberá tenerse en cuenta, de corresponder, la eventual incidencia que en su capacidad de pago pueda tener la situación en la que se encuentran los demás integrantes del grupo de contrapartes conectadas al cual pertenece.»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:7 | sí | «Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:» | `extraida_tramo_verificado` |  | d1 Definicion [exacta], tramo que contiene la frase del heredado |

## `cla::6.5.3.10` — Mantenga arreglos privados con la entidad financiera que cuenten con la opi-

Grupos: grupo_c.

### Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.3. Con problemas.
> *heredado:* El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos, esos problemas pueden resultar en una pérdida para la entidad financiera. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *propio:* 6.5.3.10. Mantenga arreglos privados con la entidad financiera que cuenten con la opinión del auditor externo de la entidad sobre la factibilidad del cumplimiento de la refinanciación, cuando aún no se haya cancelado el 15 % del importe involucrado en el citado acuerdo y siempre que dicho acuerdo se haya alcanzado cuando el deudor se encontraba categorizado en los niveles "con alto riesgo de insolvencia" o "irrecuperable". A fin de determinar el importe de la cancelación, se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deudor –con excepción de las hipotecas sobre inmuebles rurales que, por lo tanto, serán computables–, observando los márgenes de cobertura establecidos en las normas sobre "Garantías". Será requisito indispensable, además, contar con la opinión favorable sobre la calidad de las garantías, formulada por el auditor externo. En los casos de acuerdos superiores al equivalente a 2,5 veces el importe de referencia establecido en el punto 3.7., la reclasificación inicial del cliente a esta categoría podrá realizarse siempre que no medie objeción por parte de la SEFyC, a la cual, previamente, se deberá plantear cada situación en forma individual.

### Extracción (código A)

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

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «sin cancelar el 15 %» | `sin_relacion` | norma_presente | c1 Condicion con el umbral, sin relación; el indicador (la norma de clasificación) está en la unidad como Definicion d1, que además lleva el supuesto en su tramo |
| 2 | «acuerdo alcanzado en alto riesgo o irrecuperable» | `sin_relacion` | norma_presente | c2 Condicion sin relación; la norma (el indicador d1) está en la unidad |
| 3 | «acuerdos de más de 2,5 veces el importe de referencia» | `condicion_con_relacion` |  | c4 Condicion con el umbral —condicion_de→ p2 Potestad (la reclasificación inicial) |

## `cla::6.5.3.7` — Incurra en atrasos recurrentes, incumplimiento de hasta 180 días respecto de

Grupos: omisiones.

### Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.3. Con problemas.
> *heredado:* El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos, esos problemas pueden resultar en una pérdida para la entidad financiera. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *propio:* 6.5.3.7. Incurra en atrasos recurrentes, incumplimiento de hasta 180 días respecto de condiciones contractuales o nulo movimiento en las cuentas con la entidad.

### Extracción (código A)

- **c1 Condicion** «Atrasos recurrentes, incumplimiento hasta 180 días o nulo movimiento» — Indicador de la categoría 'Con problemas' (cartera comercial): que el cliente incurra en atrasos recurrentes, incumplimiento de hasta 180 días respecto de condiciones contractuales o nulo movimiento en las cuentas con la entidad. Supuestos alternativos; la norma de clasificación 'Con problemas' está en la unidad del encabezado 6.5.3. · umbral: ['incumplimiento de hasta 180 días'] · tramo [exacta]: «Incurra en atrasos recurrentes, incumplimiento de hasta 180 días respecto de condiciones contractuales o nulo movimiento en las cuentas con la entidad.»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:11 | sí | «El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender normalmente la totalidad de sus compromisos financieros y que, de no ser …» | `ausente` |  | ninguna entidad ni omisión cubre la oración del heredado |

## `cla::6.5.4.5` — Cuente con refinanciaciones del capital adeudado y de los intereses devengados

Grupos: grupo_c.

### Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.4. Con alto riesgo de insolvencia.
> *heredado:* El análisis del flujo de fondos del cliente demuestra que es altamente improbable que pueda atender la totalidad de sus compromisos financieros. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *propio:* 6.5.4.5. Cuente con refinanciaciones del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad para su pago, con otorgamiento de quitas o con reducción en las tasas de interés pactadas –salvo que ello derive de las condiciones del mercado– o cuando haya sido necesario recibir bienes en pago de parte de las obligaciones. No obstante, el deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital podrá ser recategorizado directamente en niveles superiores ("con problemas", "en observación") por la aplicación de la metodología establecida en el punto 2.2.6. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", siempre que además se observen las otras condiciones previstas en las correspondientes categorías. Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 10 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, con más el porcentaje acumulado que pudiera corresponder si la refinanciación se hubiera otorgado de haberse encontrado el deudor en la categoría inferior, podrá reclasificárselo en el nivel inmediato superior si, además, se observan las otras condiciones previstas en el citado nivel. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente. Ello, salvo que por aplicación de otras pautas corresponda categorizarlo en el nivel inferior.

### Extracción (código A)

- **op1 Operacion** «Clasificación en categoría con alto riesgo de insolvencia» — Inclusión del cliente de la cartera comercial en la categoría 'Con alto riesgo de insolvencia' · props: `{"tipo": "clasificacion_de_deudor"}` · tramo [exacta]: «Con alto riesgo de insolvencia.»
- **c1 Condicion** «Refinanciaciones con quitas, menor tasa o bienes en pago» — Indicador de alto riesgo de insolvencia: el cliente cuenta con refinanciaciones del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad de pago, con quitas o con reducción de tasas pactadas (salvo condiciones de mercado), o cuando fue necesario recibir bienes en pago de parte de las obligaciones. Es uno de los indicadores que pueden reflejar la situación de la ca… · tramo [exacta]: «Cuente con refinanciaciones del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad para su pago, con otorgamiento de quitas o con reducción en las tasas de interés pactadas –salvo que ello derive de las condiciones del mercado– o cuando haya sido necesario recibir bienes en pago de p…»
- **p1 Potestad** «Recategorización directa a niveles superiores tras quitas de capital» — El deudor cuyas deudas fueron refinanciadas con quitas de capital puede ser recategorizado directamente en niveles superiores ('con problemas', 'en observación') por aplicación de la metodología del punto 2.2.6. de las normas de Previsiones mínimas. · tramo [exacta]: «el deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital podrá ser recategorizado directamente en niveles superiores ("con problemas", "en observación") por la aplicación de la metodología establecida en el punto 2.2.6.»
- **c2 Condicion** «Observancia de otras condiciones de la categoría superior» — Se observan además las otras condiciones previstas en las categorías superiores correspondientes; condiciona la recategorización directa tras quitas de capital. · tramo [exacta]: «siempre que además se observen las otras condiciones previstas en las correspondientes categorías.»
- **p2 Potestad** «Reclasificación al nivel inmediato superior» — Cuando se haya cumplido con el pago del 10 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, sin atrasos superiores a 31 días, podrá reclasificarse al deudor en el nivel inmediato superior. · tramo [exacta]: «podrá reclasificárselo en el nivel inmediato superior si, además, se observan las otras condiciones previstas en el citado nivel.»
- **c3 Condicion** «Pago del 10 % refinanciado sin atrasos mayores a 31 días» — Se cumplió al menos con el pago, sin atrasos superiores a 31 días, del 10 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, más el porcentaje acumulado que pudiera corresponder si la refinanciación se hubiera otorgado estando el deudor en la categoría inferior. · umbral: ['atrasos superiores a los 31 días', '10 % de las obligaciones refinanciadas'] · tramo [exacta]: «Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 10 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, con más el porcentaje acumulado que pudiera corresponder si la refinanciación se hubiera otorgado de haberse encontrado el deudor e…»
- **c4 Condicion** «Observancia de otras condiciones del nivel superior» — Se observan además las otras condiciones previstas en el nivel inmediato superior; condiciona la reclasificación. · tramo [exacta]: «si, además, se observan las otras condiciones previstas en el citado nivel»
- **o1 Obligacion** «Permanencia mínima de 180 días en la categoría» — El deudor clasificado en esta categoría que haya refinanciado su deuda (aun habiendo cancelado el porcentaje del párrafo precedente) y recibido crédito adicional (punto 2.2.5. de Previsiones mínimas), no cancelado, debe permanecer en la categoría al menos 180 días desde el crédito adicional o el acuerdo de refinanciación, el más reciente. · props: `{"tipo": "otra"}` · umbral: ['por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional…'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente.»
- **c5 Condicion** «Refinanciación y crédito adicional no cancelado» — El deudor, clasificado en esta categoría, refinanció su deuda y recibió crédito adicional (punto 2.2.5.), y la financiación adicional no fue cancelada; supuesto de la permanencia mínima de 180 días. · tramo [exacta]: «encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en q…»
- **x1 Excepcion** «Salvo categorización en nivel inferior por otras pautas» — Exceptúa la permanencia mínima de 180 días en la categoría cuando por aplicación de otras pautas corresponda categorizar al deudor en el nivel inferior. · tramo [exacta]: «Ello, salvo que por aplicación de otras pautas corresponda categorizarlo en el nivel inferior.»
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p2 Potestad
- R: c4 Condicion —condicion_de→ p2 Potestad
- R: c5 Condicion —condicion_de→ o1 Obligacion
- R: x1 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: p1 Potestad —aplica_a→ Sujeto_deudor (mención «el deudor»)
- R: o1 Obligacion —aplica_a→ Sujeto_deudor (mención «El deudor»)

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «bienes en pago» | `fusionado` |  | c1 Condicion (el indicador) junta «bienes en pago» con los otros supuestos del indicador (refinanciaciones con quitas o con reducción de tasas) en un solo tramo; c1 —condicion_de→ op1 |
| 2 | «recategorización siempre que…» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ p1 Potestad |
| 3 | «pago del 10 %» | `condicion_con_relacion` |  | c3 Condicion con los umbrales —condicion_de→ p2 Potestad |
| 4 | «financiación adicional sin cancelar» | `condicion_con_relacion` |  | c5 Condicion —condicion_de→ o1 Obligacion |
| 5 | «salvo otras pautas» | `condicion_con_relacion` |  | x1 Excepcion —exceptua_obligacion→ o1 Obligacion |

## `cla::6.5.4.7` — Haya solicitado el concurso preventivo, celebrado un acuerdo preventivo extraju-

Grupos: omisiones.

### Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.4. Con alto riesgo de insolvencia.
> *heredado:* El análisis del flujo de fondos del cliente demuestra que es altamente improbable que pueda atender la totalidad de sus compromisos financieros. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *propio:* 6.5.4.7. Haya solicitado el concurso preventivo, celebrado un acuerdo preventivo extrajudicial aún no homologado o se le haya requerido su quiebra, en tanto no hubiere sido declarada, por obligaciones que sean iguales o superiores al 20 % del patrimonio del cliente o por obligaciones entre el 5 % y menos del 20 % del patrimonio cuando persista el pedido de quiebra luego de transcurridos 90 días desde que ésta haya sido requerida. En caso de levantarse el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores, según la situación previa, si se observan las condiciones allí previstas. En el caso de deudores que hayan solicitado el concurso preventivo o acuerdo preventivo extrajudicial aún no homologado, corresponderá la reclasificación inmediata en el nivel siguiente inferior cuando se verifiquen atrasos de más de 540 días.

### Extracción (código A)

- **c1 Condicion** «Obligaciones ≥20 % del patrimonio — concurso, APE o pedido de quiebra» — Indicador de alto riesgo de insolvencia (punto 6.5.4): el cliente solicitó concurso preventivo, celebró un acuerdo preventivo extrajudicial no homologado o se le requirió la quiebra (no declarada), por obligaciones iguales o superiores al 20 % del patrimonio del cliente. Condición de la norma del encabezado 6.5.4 (clasificación con alto riesgo de insolvencia). · umbral: ['iguales o superiores al 20 % del patrimonio del cliente'] · tramo [exacta]: «Haya solicitado el concurso preventivo, celebrado un acuerdo preventivo extrajudicial aún no homologado o se le haya requerido su quiebra, en tanto no hubiere sido declarada, por obligaciones que sean iguales o superiores al 20 % del patrimonio del cliente»
- **c2 Condicion** «Obligaciones 5 %–<20 % del patrimonio — quiebra persistente 90 días» — Indicador de alto riesgo de insolvencia (punto 6.5.4): se le requirió la quiebra al cliente, por obligaciones entre el 5 % y menos del 20 % del patrimonio, cuando persista el pedido de quiebra luego de transcurridos 90 días desde que fue requerida. Condición de la norma del encabezado 6.5.4. · umbral: ['entre el 5 % y menos del 20 % del patrimonio', 'luego de transcurridos 90 días desde que ésta haya sido requerida'] · tramo [exacta]: «por obligaciones entre el 5 % y menos del 20 % del patrimonio cuando persista el pedido de quiebra luego de transcurridos 90 días desde que ésta haya sido requerida»
- **p1 Potestad** «Reclasificación a niveles superiores si se levanta la quiebra» — En caso de levantarse el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores, según la situación previa. · tramo [exacta]: «En caso de levantarse el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores, según la situación previa»
- **c3 Condicion** «Se observan las condiciones previstas para el nivel superior» — Para la reclasificación en niveles superiores tras levantarse el pedido de quiebra, deben observarse las condiciones previstas en esos niveles. · tramo [exacta]: «si se observan las condiciones allí previstas»
- **o1 Operacion** «Reclasificación del deudor en nivel superior» — Reclasificación del deudor en niveles superiores, según la situación previa, tras levantarse el pedido de quiebra. · props: `{"tipo": "clasificacion_de_deudor"}` · tramo [exacta]: «el deudor podrá ser reclasificado en niveles superiores»
- **o2 Operacion** «Reclasificación inmediata al nivel inferior siguiente» — Reclasificación inmediata en el nivel siguiente inferior de deudores que hayan solicitado el concurso preventivo o acuerdo preventivo extrajudicial aún no homologado. · props: `{"tipo": "clasificacion_de_deudor"}` · tramo [no]: «corresponderá la reclasificación ininmediata en el nivel siguiente inferior»
- **ob1 Obligacion** «Reclasificar al nivel inferior ante atraso >540 días» — Corresponde la reclasificación inmediata en el nivel siguiente inferior de los deudores que hayan solicitado concurso preventivo o acuerdo preventivo extrajudicial aún no homologado, cuando se verifiquen atrasos de más de 540 días. · props: `{"tipo": "otra"}` · umbral: ['atrasos de más de 540 días'] · tramo [exacta]: «En el caso de deudores que hayan solicitado el concurso preventivo o acuerdo preventivo extrajudicial aún no homologado, corresponderá la reclasificación inmediata en el nivel siguiente inferior cuando se verifiquen atrasos de más de 540 días.»
- **c4 Condicion** «Atrasos de más de 540 días — concurso o APE no homologado» — Supuesto para la reclasificación inmediata en el nivel inferior: deudores que solicitaron concurso preventivo o APE no homologado con atrasos de más de 540 días. · umbral: ['atrasos de más de 540 días'] · tramo [exacta]: «cuando se verifiquen atrasos de más de 540 días»
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: c4 Condicion —condicion_de→ ob1 Obligacion
- R: ob1 Obligacion —regula→ o2 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:16 | sí | «según la situación previa, si se observan las condiciones allí previstas» | `extraida_tramo_verificado` |  | c3 Condicion [exacta] «si se observan las condiciones allí previstas» y p1 Potestad [exacta] «…según la situación previa»: entre las dos cubren el tramo |

## `cla::6.5.5.2` — Incurra en atrasos superiores a un año, cuente con refinanciación del capital y

Grupos: grupo_c.

### Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.5. Irrecuperable.
> *heredado:* Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de circunstancias futuras, su incobrabilidad es evidente al momento del análisis. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *heredado:* Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el motivo (entre ellos por no contar con legajo o por no haber proporcionado información confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente, con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, por un período de hasta 540 días contados a partir de la apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales de cobro, según corresponda, no hubiesen presentado la documentación que permita realizarla, siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos. Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad".
> *propio:* 6.5.5.2. Incurra en atrasos superiores a un año, cuente con refinanciación del capital y sus intereses y con financiación de pérdidas de explotación. A este fin, el cómputo de los plazos no se interrumpirá por el otorgamiento de renovaciones cuando previamente no se haya producido la cancelación efectiva de las obligaciones vencidas, es decir sin recurrir a financiación directa o indirecta de la entidad. Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, podrá reclasificarse al deudor en el nivel inmediato superior si, además, se observan las otras condiciones previstas en el citado nivel. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente.

### Extracción (código A)

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

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «sin cancelación efectiva previa» | `dentro_de_norma` |  | dentro de la Restriccion r1 («No interrupción del cómputo por renovaciones», tramo con el «cuando previamente no se haya producido la cancelación efectiva»); sin Condicion |
| 2 | «pago del 15 %» | `condicion_con_relacion` |  | c2 Condicion con los umbrales —condicion_de→ p1 Potestad |
| 3 | «financiación adicional sin cancelar» | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ ob1 Obligacion |

## `cla::6.5.5.9` — Clientes del sector privado no financiero, cuya deuda (por todo concepto) más el

Grupos: grupo_c, omisiones.

### Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.5. Irrecuperable.
> *heredado:* Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de circunstancias futuras, su incobrabilidad es evidente al momento del análisis. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *heredado:* Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el motivo (entre ellos por no contar con legajo o por no haber proporcionado información confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente, con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, por un período de hasta 540 días contados a partir de la apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales de cobro, según corresponda, no hubiesen presentado la documentación que permita realizarla, siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos. Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad".
> *propio:* 6.5.5.9. Clientes del sector privado no financiero, cuya deuda (por todo concepto) más el importe de la financiación solicitada, al momento del otorgamiento de ésta, exceda del 2,5 % de la responsabilidad patrimonial computable de la entidad del último día del mes anterior al que corresponda o el equivalente al importe de referencia establecido en el punto 3.7., de ambos el menor, y que no hayan presentado declaración jurada sobre si revisten o no el carácter de vinculados al respectivo intermediario financiero o si su relación con éste implica la existencia de influencia controlante, o no hayan actualizado la presentada con anterioridad, con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, por un período de hasta 540 días contados a partir de la apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales de cobro, según corresponda, no hubiesen presentado la documentación que permita realizarla, siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos. Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad". Este tratamiento se aplicará desde la fecha de otorgamiento de la asistencia, cuando se trate de la primera declaración, o a partir del 1.12, en los casos de las actualizaciones posteriores, y hasta el mes anterior a la fecha en que el cliente efectúe la pertinente presentación.

### Extracción (código A)

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

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «deuda de más del 2,5 % de la RPC o del importe de referencia» | `condicion_con_relacion` |  | c1 Condicion con el umbral —condicion_de→ op1 Operacion (la clasificación como Irrecuperable, que es lo que el supuesto condiciona) |
| 2 | «excepción de concurso hasta 540 días» | `sin_relacion` | norma_presente | ex1 Excepcion con el umbral, sin relación hacia la norma que exceptúa (op1 está en la unidad; la salida lo declara en una omisión relacion_sin_predicado) |
| 3 | «siempre que haya informe» | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ ex1 Excepcion |
| 4 | «primera declaración» | `fusionado` |  | c4 Condicion junta la primera declaración y las actualizaciones (y el fin de la vigencia) en un solo tramo; c4 —condicion_de→ op1 |
| 5 | «actualizaciones» | `fusionado` |  | ídem, c4 |

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:26 | sí | «Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre "Previsiones mínimas por ries…» | `ausente` |  | ninguna entidad con tramo que cubra «Ello, sin perjuicio de que se trate de deudas…» ni omisión que lo registre |

## `cla::7.2.2.1` — En observación.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
> *heredado:* 7.2. Niveles de clasificación.
> *heredado:* 7.2.2. Riesgo bajo.
> *propio:* 7.2.2.1. En observación. Comprende los clientes que registran incumplimientos ocasionales en la atención de sus obligaciones, con atrasos de más de 31 hasta 90 días. En cuanto a la situación jurídica del deudor, se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer cuando se haya cancelado, al menos, el 10 % del importe involucrado en el citado acuerdo. Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior, cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 1 cuota o, cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligaciones refinanciadas (por capital), con más la cantidad de cuotas o el porcentaje acumulado que pudiera corresponder, respectivamente, si la refinanciación se hubiera otorgado de encontrarse incluido el deudor en niveles inferiores. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado la cuota citada en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente. En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categoría, corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días resultante de sumar los días de atraso efectivamente registrados a partir de la primera cuota impaga de la refinanciación y los de atraso mínimo establecidos normativamente que correspondan a la categoría en la que se encuentre clasificado el deudor en el mes en que se verifica el nuevo atraso.

### Extracción (código A)

- **d1 Definicion** «Categoría En observación (atrasos 31 a 90 días)» — Comprende los clientes que registran incumplimientos ocasionales en la atención de sus obligaciones, con atrasos de más de 31 hasta 90 días. · props: `{"termino": "En observación"}` · tramo [exacta]: «Comprende los clientes que registran incumplimientos ocasionales en la atención de sus obligaciones, con atrasos de más de 31 hasta 90 días.»
- **o1 Obligacion** «Considerar convenios de pago homologados — situación jurídica» — En cuanto a la situación jurídica del deudor, se considerará (para esta categoría) si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados, incluyendo acuerdos preventivos extrajudiciales homologados, a vencer. · props: `{"tipo": "otra"}` · tramo [exacta]: «En cuanto a la situación jurídica del deudor, se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer»
- **c1 Condicion** «Cancelado al menos 10 % del acuerdo homologado» — Se haya cancelado al menos el 10 % del importe involucrado en el acuerdo homologado. · umbral: ['al menos, el 10 % del importe involucrado en el citado acuerdo'] · tramo [exacta]: «cuando se haya cancelado, al menos, el 10 % del importe involucrado en el citado acuerdo»
- **p1 Potestad** «Reclasificación al nivel inmediato superior de refinanciados» — Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior. · tramo [exacta]: «Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior»
- **c2 Condicion** «Pago puntual (atraso hasta 31 días) de 1 cuota» — Hayan cumplido puntualmente o con atrasos que no superen los 31 días con el pago de 1 cuota (refinanciaciones de pago periódico mensual o bimestral), con más la cantidad de cuotas que pudiera corresponder si la refinanciación se hubiera otorgado de encontrarse incluido el deudor en niveles inferiores. · props: `{"umbrales": [{"tramo": "el pago de 1 cuota", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['atrasos que no superen los 31 días', 'el pago de 1 cuota'] · tramo [exacta]: «cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 1 cuota»
- **c3 Condicion** «Cancelado al menos 5 % de obligaciones refinanciadas» — Tratándose de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligaciones refinanciadas (por capital), con más el porcentaje acumulado que pudiera corresponder si la refinanciación se hubiera otorgado de encontrarse incluido el deudor en niveles inferiores. · umbral: ['al menos el 5 % de sus obligaciones refinanciadas (por capital)'] · tramo [exacta]: «cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligaciones refinanciadas (por capital)»
- **o2 Obligacion** «Permanencia mínima 180 días en la categoría» — El deudor clasificado en esta categoría que haya refinanciado su deuda y recibido crédito adicional (punto 2.2.5. de las normas sobre Previsiones mínimas por riesgo de incobrabilidad) no cancelado deberá permanecer en esta categoría por lo menos 180 días desde el crédito adicional o el acuerdo de refinanciación, el más reciente. · props: `{"tipo": "otra"}` · umbral: ['por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicio…'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente»
- **c4 Condicion** «Crédito adicional no cancelado tras refinanciar» — Deudor clasificado en esta categoría que haya refinanciado su deuda y recibido crédito adicional según el punto 2.2.5. de las normas de Previsiones mínimas, en la medida en que la financiación adicional no hubiese sido cancelada. · tramo [exacta]: «haya refinanciado su deuda –aun cuando haya cancelado la cuota citada en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancela…»
- **o3 Obligacion** «Reclasificación inmediata por atraso mayor a 31 días» — Corresponde la reclasificación inmediata del deudor en el nivel que surja de sumar los días de atraso efectivamente registrados desde la primera cuota impaga de la refinanciación y los días de atraso mínimo de la categoría en que esté clasificado en el mes en que se verifica el nuevo atraso. · props: `{"tipo": "otra"}` · tramo [exacta]: «corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días resultante de sumar los días de atraso efectivamente registrados a partir de la primera cuota impaga de la refinanciación y los de atraso mínimo establecidos normativamente que correspondan a la categoría…»
- **c5 Condicion** «Atrasos mayores a 31 días en deuda refinanciada» — Se verifiquen atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados desde la inclusión del deudor en esta categoría. · umbral: ['atrasos mayores a 31 días'] · tramo [exacta]: «En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categoría»
- **op1 Operacion** «Reclasificación de deudor refinanciado» — Reclasificación del deudor de cartera para consumo o vivienda en nivel superior o por nuevo atraso tras refinanciación. · props: `{"tipo": "clasificacion_deudor"}` · tramo [exacta]: «reclasificación inmediata del deudor»
- R: c1 Condicion —condicion_de→ o1 Obligacion
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: o2 Obligacion —aplica_a→ Sujeto_deudor (mención «El deudor»)
- R: c4 Condicion —condicion_de→ o2 Obligacion
- R: c5 Condicion —condicion_de→ o3 Obligacion
- R: o3 Obligacion —regula→ op1 Operacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «cancelado el 10 %» | `condicion_con_relacion` |  | c1 Condicion con el umbral —condicion_de→ o1 Obligacion (la consideración de los convenios de pago) |
| 2 | «pago de 1 cuota» | `condicion_con_relacion` |  | c2 Condicion con los umbrales —condicion_de→ p1 Potestad |
| 3 | «pago único o irregular con 5 %» | `condicion_con_relacion` |  | c3 Condicion con el umbral —condicion_de→ p1 Potestad |
| 4 | «financiación adicional sin cancelar» | `condicion_con_relacion` |  | c4 Condicion —condicion_de→ o2 Obligacion |
| 5 | «atrasos de más de 31 días» | `condicion_con_relacion` |  | c5 Condicion con el umbral —condicion_de→ o3 Obligacion |

## `cla::7.2.3` — Riesgo medio.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
> *heredado:* 7.2. Niveles de clasificación.
> *propio:* 7.2.3. Riesgo medio. Comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días. En cuanto a la situación jurídica del deudor, se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer cuando aún no se haya cancelado el 10 % del importe involucrado en el citado acuerdo. A fin de determinar el importe de la cancelación, se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deudor –con excepción de las hipotecas sobre inmuebles rurales que, por lo tanto, serán computables–, observando los márgenes de cobertura establecidos en las normas sobre "Garantías". Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior, cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 2 cuotas consecutivas o, cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligaciones refinanciadas (por capital), con más la cantidad de cuotas o el porcentaje acumulado que pudiera corresponder, respectivamente, si la refinanciación se hubiera otorgado de encontrarse incluido el deudor en el nivel inferior. El deudor refinanciado que haya cumplido con lo dispuesto en los párrafos precedentes, según corresponda, podrá ser reclasificado en el nivel inmediato superior si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado las cuotas o el porcentaje establecidos precedentemente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente. En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categoría, corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días resultante de sumar los días de atraso efectivamente registrados a partir de la primera cuota impaga de la refinanciación y los de atraso mínimo establecidos normativamente que correspondan a la categoría en la que se encuentre clasificado el deudor en el mes en que se verifica el nuevo atraso.

### Extracción (código A)

- **d1 Definicion** «Riesgo medio — clientes con atraso de más de 90 hasta 180 días» — Comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días. · props: `{"termino": "Riesgo medio"}` · tramo [exacta]: «Comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días.»
- **d2 Definicion** «Situación jurídica — convenios de pago homologados con menos del 10 % cancelado» — Para la situación jurídica del deudor se considera si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluidos acuerdos preventivos extrajudiciales homologados) a vencer cuando aún no se haya cancelado el 10 % del importe involucrado en el acuerdo. · props: `{"termino": "situación jurídica del deudor"}` · tramo [exacta]: «se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer cuando aún no se haya cancelado el 10 % del importe involucrado en el citado acuerdo»
- **p1 Potestad** «Cómputo del 50 % de garantías adicionales» — A fin de determinar el importe de la cancelación, se admite computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deudor, observando los márgenes de cobertura de las normas sobre Garantías; las hipotecas sobre inmuebles rurales son computables. · tramo [exacta]: «se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deudor»
- **p2 Potestad** «Reclasificación al nivel superior — deuda refinanciada» — Los clientes con deudas refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) pueden ser reclasificados en el nivel inmediato superior. · tramo [exacta]: «Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior»
- **c1 Condicion** «Pago de 2 cuotas consecutivas puntual o con atraso hasta 31 días» — Haber cumplido puntualmente o con atrasos que no superen los 31 días con el pago de 2 cuotas consecutivas. · props: `{"umbrales": [{"tramo": "2 cuotas consecutivas", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['atrasos que no superen los 31 días', '2 cuotas consecutivas'] · tramo [exacta]: «cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 2 cuotas consecutivas»
- **c2 Condicion** «Cancelación de al menos 5 % de obligaciones refinanciadas» — En financiaciones de pago único, periódico superior a bimestral o irregular, haber cancelado al menos el 5 % de las obligaciones refinanciadas (por capital), más la cantidad de cuotas o porcentaje acumulado que correspondiera si la refinanciación se hubiera otorgado con el deudor en el nivel inferior. · umbral: ['al menos el 5 % de sus obligaciones refinanciadas (por capital)'] · tramo [exacta]: «cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligaciones refinanciadas (por capital)»
- **p3 Potestad** «Reclasificación al nivel superior — deudor refinanciado con resto de deudas en condiciones» — El deudor refinanciado que haya cumplido lo dispuesto en los párrafos precedentes puede ser reclasificado en el nivel inmediato superior si además el resto de sus deudas reúnen como mínimo las condiciones del nivel. · tramo [exacta]: «podrá ser reclasificado en el nivel inmediato superior si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel»
- **c3 Condicion** «Resto de deudas con condiciones mínimas del nivel superior» — El resto de las deudas del deudor refinanciado reúne, como mínimo, las condiciones previstas en el nivel inmediato superior. · tramo [exacta]: «si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel»
- **r1 Obligacion** «Permanencia mínima 180 días — refinanciado con crédito adicional» — El deudor clasificado en esta categoría que haya refinanciado su deuda y recibido crédito adicional (punto 2.2.5 de Previsiones mínimas), mientras la financiación adicional no se haya cancelado, debe permanecer en esta categoría al menos 180 días desde el crédito adicional o el acuerdo de refinanciación, lo más reciente. · props: `{"tipo": "otra"}` · umbral: ['por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicio…'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente»
- **o1 Operacion** «Reclasificación inmediata por atraso mayor a 31 días» — Reclasificación inmediata del deudor refinanciado en el nivel que surja de sumar los días de atraso registrados desde la primera cuota impaga de la refinanciación y los de atraso mínimo de la categoría en que se encuentre en el mes del nuevo atraso. · props: `{"tipo": "clasificacion_de_deudor"}` · tramo [exacta]: «corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días resultante de sumar los días de atraso efectivamente registrados a partir de la primera cuota impaga de la refinanciación y los de atraso mínimo establecidos normativamente»
- **c4 Condicion** «Atrasos mayores a 31 días en deuda refinanciada» — Se verifican atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada desde la inclusión del deudor en esta categoría. · umbral: ['atrasos mayores a 31 días'] · tramo [exacta]: «En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categoría»
- R: c1 Condicion —condicion_de→ p2 Potestad
- R: c2 Condicion —condicion_de→ p2 Potestad
- R: c3 Condicion —condicion_de→ p3 Potestad
- R: c4 Condicion —condicion_de→ o1 Operacion
- R: r1 Obligacion —aplica_a→ Sujeto_deudor (mención «El deudor»)
- R: p2 Potestad —aplica_a→ Sujeto_cliente (mención «Los clientes»)
- R: p3 Potestad —aplica_a→ Sujeto (mención «El deudor refinanciado»)

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «sin cancelar el 10 %» | `dentro_de_norma` |  | dentro de la Definicion d2 («Situación jurídica — convenios… con menos del 10 % cancelado»); extraído como norma de otro tipo, sin Condicion |
| 2 | «pago de 2 cuotas» | `condicion_con_relacion` |  | c1 Condicion con los umbrales —condicion_de→ p2 Potestad |
| 3 | «pago único o irregular con 5 %» | `condicion_con_relacion` |  | c2 Condicion con el umbral —condicion_de→ p2 Potestad |
| 4 | «financiación adicional sin cancelar» | `dentro_de_norma` |  | dentro de la Obligacion r1 (permanencia de 180 días, descripción); sin Condicion |
| 5 | «atrasos de más de 31 días» | `condicion_con_relacion` |  | c4 Condicion con el umbral —condicion_de→ o1 Operacion (la reclasificación inmediata) |

## `cla::7.2.4` — Riesgo alto.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
> *heredado:* 7.2. Niveles de clasificación.
> *propio:* 7.2.4. Riesgo alto. Comprende a los clientes con atrasos de más de 180 días hasta un año. También incluirá a los deudores que hayan solicitado el concurso preventivo, celebrado un acuerdo preventivo extrajudicial aún no homologado o se le haya requerido su quiebra, en tanto no hubiere sido declarada, por obligaciones que sean iguales o superiores al 20 % del patrimonio del cliente o por obligaciones entre el 5 % y menos del 20 % del patrimonio cuando persista el pedido de quiebra luego de transcurridos 90 días desde que ésta haya sido requerida. En caso de levantarse el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores, según la situación previa, si se observan las condiciones allí previstas. En el caso de deudores que hayan solicitado el concurso preventivo o acuerdo preventivo extrajudicial o se encuentren en gestión judicial, que verifiquen atrasos de hasta 540 días. Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior, cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 3 cuotas consecutivas o, cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 10 % de sus obligaciones refinanciadas (por capital), con más la cantidad de cuotas o el porcentaje acumulado que pudiera corresponder, respectivamente, si la refinanciación se hubiera otorgado de encontrarse incluido el deudor en el nivel inferior En el caso de deudores que hayan solicitado el concurso preventivo, corresponderá la reclasificación inmediata en el nivel siguiente inferior cuando se verifiquen atrasos de más de 540 días. El deudor refinanciado que haya cumplido con lo dispuesto en los párrafos precedentes, según corresponda, podrá ser reclasificado en el nivel inmediato superior si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado las cuotas o el porcentaje establecidos precedentemente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente. En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categoría, corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días resultante de sumar los días de atraso efectivamente registrados a partir de la primera cuota impaga de la refinanciación y los de atraso mínimo establecidos normativamente que correspondan a la categoría en la que se encuentre clasificado el deudor en el mes en que se verifica el nuevo atraso.

### Extracción (código A)

- **op1 Operacion** «Clasificación en riesgo alto» — Clasificación de los deudores de la cartera para consumo o vivienda en el nivel de riesgo alto · props: `{"tipo": "clasificacion_de_deudor"}` · tramo [exacta]: «Riesgo alto.»
- **d1 Definicion** «Riesgo alto: atrasos de más de 180 días hasta un año» — Comprende a los clientes con atrasos de más de 180 días hasta un año. · props: `{"termino": "Riesgo alto"}` · tramo [exacta]: «Comprende a los clientes con atrasos de más de 180 días hasta un año.»
- **d2 Definicion** «Riesgo alto: concursados o con quiebra requerida» — Incluye a deudores que hayan solicitado el concurso preventivo, celebrado acuerdo preventivo extrajudicial no homologado o con quiebra requerida y no declarada, por obligaciones iguales o superiores al 20 % del patrimonio, o entre el 5 % y menos del 20 % cuando persista el pedido de quiebra tras 90 días. · props: `{"termino": "Riesgo alto"}` · no definidas: `{"nota": "incluye umbrales patrimoniales y plazo de 90 días"}` · tramo [no]: «También incluirá a los deudores que hayan solicitado el concurso preventivo, celebrado un acuerdo preventivo extrajudicial aún no homologado o se le haya requerido su quiebra, en tanto no hubiere sido declarada»
- **c1 Condicion** «Obligaciones ≥ 20 % del patrimonio» — Supuesto de inclusión en riesgo alto: obligaciones iguales o superiores al 20 % del patrimonio del cliente · umbral: ['iguales o superiores al 20 % del patrimonio del cliente'] · tramo [exacta]: «por obligaciones que sean iguales o superiores al 20 % del patrimonio del cliente»
- **c2 Condicion** «Obligaciones 5 % a <20 % con quiebra persistente 90 días» — Supuesto de inclusión en riesgo alto: obligaciones entre el 5 % y menos del 20 % del patrimonio cuando persista el pedido de quiebra luego de 90 días desde que fue requerida · umbral: ['entre el 5 % y menos del 20 % del patrimonio', 'luego de transcurridos 90 días desde que ésta haya sido requerida'] · tramo [exacta]: «por obligaciones entre el 5 % y menos del 20 % del patrimonio cuando persista el pedido de quiebra luego de transcurridos 90 días desde que ésta haya sido requerida»
- **p1 Potestad** «Reclasificación a niveles superiores tras levantarse quiebra» — Si se levanta el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores según la situación previa · tramo [no]: «En caso de levantarse el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores, según la situación previa»
- **c3 Condicion** «Observancia de condiciones previstas» — Reclasificación en niveles superiores si se observan las condiciones previstas para esos niveles · tramo [exacta]: «si se observan las condiciones allí previstas»
- **d3 Definicion** «Riesgo alto: concursados o en gestión judicial con atrasos hasta 540 días» — Deudores que hayan solicitado concurso preventivo o acuerdo preventivo extrajudicial o en gestión judicial, con atrasos de hasta 540 días. · props: `{"termino": "Riesgo alto"}` · no definidas: `{"nota": "umbral 540 días"}` · tramo [no]: «En el caso de deudores que hayan solicitado el concurso preventivo o acuerdo preventivo extrajudicial o se encuentren en gestión judicial, que verifiquen atrasos de hasta 540 días.»
- **p2 Potestad** «Reclasificación refinanciados al nivel inmediato superior» — Clientes con deudas refinanciadas mediante pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior · tramo [exacta]: «Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior»
- **c4 Condicion** «Pago puntual o atraso ≤31 días de 3 cuotas consecutivas» — Supuesto para reclasificar refinanciados de pago mensual o bimestral: pago de 3 cuotas consecutivas puntualmente o con atrasos que no superen 31 días · props: `{"umbrales": [{"tramo": "3 cuotas consecutivas", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['atrasos que no superen los 31 días', '3 cuotas consecutivas'] · tramo [exacta]: «cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 3 cuotas consecutivas»
- **c5 Condicion** «Cancelación de al menos 10 % de obligaciones refinanciadas» — Supuesto para financiaciones de pago único, periódico superior a bimestral o irregular: cancelación de al menos el 10 % de las obligaciones refinanciadas (por capital), con más la cantidad de cuotas o porcentaje acumulado que correspondiera si la refinanciación se hubiera otorgado estando el deudor en el nivel inferior · umbral: ['al menos el 10 % de sus obligaciones refinanciadas (por capital)'] · tramo [exacta]: «cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 10 % de sus obligaciones refinanciadas (por capital)»
- **o1 Obligacion** «Reclasificación inmediata concursados con atrasos >540 días» — Reclasificación inmediata en el nivel siguiente inferior de deudores que hayan solicitado concurso preventivo cuando se verifiquen atrasos de más de 540 días · props: `{"tipo": "otra"}` · umbral: ['atrasos de más de 540 días'] · tramo [exacta]: «En el caso de deudores que hayan solicitado el concurso preventivo, corresponderá la reclasificación inmediata en el nivel siguiente inferior cuando se verifiquen atrasos de más de 540 días.»
- **p3 Potestad** «Reclasificación al nivel superior con resto de deudas en condiciones» — El deudor refinanciado que cumplió lo dispuesto podrá ser reclasificado en el nivel inmediato superior si el resto de sus deudas reúne como mínimo las condiciones del nivel · tramo [exacta]: «podrá ser reclasificado en el nivel inmediato superior si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel»
- **c6 Condicion** «Resto de deudas en condiciones del nivel superior» — El resto de las deudas del deudor reúne como mínimo las condiciones previstas en el nivel superior · tramo [exacta]: «si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel»
- **r1 Restriccion** «Permanencia mínima 180 días con crédito adicional» — El deudor clasificado en riesgo alto que refinanció su deuda y recibió crédito adicional (punto 2.2.5 de Previsiones mínimas) no cancelado debe permanecer en la categoría al menos 180 días desde el crédito adicional o el acuerdo de refinanciación, lo más reciente, aun si canceló las cuotas o porcentaje establecidos · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicio…'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente»
- **c7 Condicion** «Crédito adicional no cancelado tras refinanciación» — Deudor en riesgo alto que refinanció su deuda y recibió crédito adicional en los términos del punto 2.2.5, y la financiación adicional no fue cancelada · tramo [exacta]: «haya refinanciado su deuda –aun cuando haya cancelado las cuotas o el porcentaje establecidos precedentemente– y recibido crédito adicional»
- **o2 Obligacion** «Reclasificación inmediata por atrasos >31 días en refinanciada» — Reclasificación inmediata del deudor en el nivel que surja de sumar los días de atraso registrados desde la primera cuota impaga de la refinanciación y los de atraso mínimo de la categoría en que esté clasificado en el mes del nuevo atraso · props: `{"tipo": "otra"}` · umbral: ['atrasos mayores a 31 días'] · tramo [no]: «En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categoría, corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días resultante»
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: c4 Condicion —condicion_de→ p2 Potestad
- R: c5 Condicion —condicion_de→ p2 Potestad
- R: c6 Condicion —condicion_de→ p3 Potestad
- R: c7 Condicion —condicion_de→ r1 Restriccion
- R: r1 Restriccion —limita→ op1 Operacion
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «por obligaciones que sean iguales o superiores al 20 % del patrimonio del cliente» — Habría usado condicion_de hacia una Definicion, pero el rango de condicion_de no admite Definicion
- Omisión `relacion_sin_predicado` [exacta]: «por obligaciones entre el 5 % y menos del 20 % del patrimonio cuando persista el pedido de quiebra luego de transcurridos 90 días» — Habría usado condicion_de hacia una Definicion, pero el rango de condicion_de no admite Definicion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «concurso con 20 % o más» | `sin_relacion` | norma_presente | c1 Condicion con el umbral, sin relación (omisión relacion_sin_predicado); la norma (la inclusión en riesgo alto) está en la unidad como d2 Definicion y op1 |
| 2 | «entre 5 % y 20 % con 90 días» | `sin_relacion` | norma_presente | c2 Condicion con los umbrales, sin relación (ídem) |
| 3 | «levantamiento del pedido» | `dentro_de_norma` |  | dentro de la Potestad p1 (tramo «En caso de levantarse el pedido de quiebra…»); c3 es «si se observan las condiciones allí previstas», no el levantamiento |
| 4 | «refinanciados» | `dentro_de_norma` |  | dentro de la Potestad p2 (tramo «Los clientes cuyas deudas hayan sido refinanciadas…») |
| 5 | «más de 540 días» | `dentro_de_norma` |  | dentro de la Obligacion o1 (umbral «atrasos de más de 540 días»); sin Condicion |
| 6 | «atrasos de más de 31 días» | `dentro_de_norma` |  | dentro de la Obligacion o2 (umbral «atrasos mayores a 31 días»); sin Condicion |

## `ctacte::1.5.2.6` — Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo

Grupos: omisiones.

### Texto

> *heredado:* Sección 1. Funcionamiento.
> *heredado:* 1.5. Aspectos del funcionamiento a incluir en el contrato de cuenta corriente.
> *heredado:* En sus cláusulas se deberá prever, como mínimo:
> *heredado:* 1.5.2. Obligaciones de la entidad.
> *propio:* 1.5.2.6. Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo– los cheques librados por el cuentacorrentista, de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque, teniendo en cuenta en materia de plazos de presentación los establecidos en el artículo 25 de la Ley de Cheques. En el caso de cheques de pago diferido, ese plazo se computará a partir de la fecha de pago consignada en el cheque.

### Extracción (código A)

- **ley Comunicacion** «Ley de Cheques» —  · props: `{"codigo": "Ley de Cheques", "tipo": "externa"}` · tramo [exacta]: «artículo 25 de la Ley de Cheques»
- **op1 Operacion** «Pago a la vista de cheques del cuentacorrentista» — Pago a la vista de los cheques librados por el cuentacorrentista, de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque · props: `{"tipo": "pago de cheques"}` · tramo [exacta]: «Pagar a la vista»
- **ob1 Obligacion** «Pagar a la vista cheques librados por cuentacorrentista» — Obligación de la entidad, a prever como mínimo en el contrato de cuenta corriente, de pagar a la vista los cheques librados por el cuentacorrentista, conforme a las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque, teniendo en cuenta los plazos de presentación del artículo 25 de la Ley de Cheques · props: `{"tipo": "otra"}` · tramo [exacta]: «Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo– los cheques librados por el cuentacorrentista, de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque»
- **ex1 Excepcion** «Excepción casos del punto 1.5.2.8 segundo párrafo» — Quedan exceptuados del deber de pagar a la vista los cheques en los casos a que se refiere el punto 1.5.2.8., segundo párrafo · tramo [exacta]: «excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo»
- **ob2 Obligacion** «Cómputo del plazo en cheques de pago diferido» — En cheques de pago diferido, el plazo de presentación se computa a partir de la fecha de pago consignada en el cheque · props: `{"tipo": "calculo"}` · tramo [exacta]: «En el caso de cheques de pago diferido, ese plazo se computará a partir de la fecha de pago consignada en el cheque.»
- R: to TextoOrdenado —referencia→ ley Comunicacion
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ex1 Excepcion —exceptua_obligacion→ ob1 Obligacion
- R: ob1 Obligacion —aplica_a→ Sujeto_banco (mención «la entidad»)
- R: ob2 Obligacion —aplica_a→ Sujeto_banco (mención «la entidad»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:6 | sí | «de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque» | `extraida_tramo_verificado` |  | ob1 Obligacion [exacta], tramo que contiene «de acuerdo con las disposiciones legales…» |

## `ctacte::2.1.1.4` — Lugar y fecha.

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Movimiento de las cuentas.
> *heredado:* 2.1. Créditos.
> *heredado:* 2.1.1. Mediante depósitos por ventanilla o cajeros automáticos.
> *heredado:* Cuando se empleen boletas, éstas deberán contener, como mínimo, los siguientes datos:
> *heredado:* Respecto de la realización de operaciones mediante cajeros automáticos, las entidades deberán tener implementados mecanismos de seguridad informática que garanticen la genuinidad de las operaciones.
> *propio:* 2.1.1.4. Lugar y fecha.

### Extracción (código A)

- **o1 Obligacion** «Boleta de depósito: consignar lugar y fecha» — Cuando se empleen boletas en depósitos por ventanilla o cajeros automáticos, éstas deberán contener, como mínimo, el dato de lugar y fecha (uno de los datos mínimos enumerados; deben incluirse todos). · props: `{"tipo": "otra"}` · tramo [exacta]: «Cuando se empleen boletas, éstas deberán contener, como mínimo, los siguientes datos: […] Lugar y fecha.»
- **c1 Condicion** «Empleo de boletas en depósitos» — Supuesto de que se empleen boletas en los depósitos por ventanilla o cajeros automáticos, que activa el deber de que contengan los datos mínimos, entre ellos lugar y fecha. · tramo [exacta]: «Cuando se empleen boletas»
- R: c1 Condicion —condicion_de→ o1 Obligacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:25 | sí | «2.1.1.4. Lugar y fecha.» | `extraida_tramo_verificado` |  | Obligacion con tramo de dos segmentos [exacta] «Cuando se empleen boletas… […] Lugar y fecha.» |

## `ctacte::2.3.5::intro` — [bloque intro] Publicidad.

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Movimiento de las cuentas.
> *heredado:* 2.3. Intereses.
> *heredado:* 2.3.5. Publicidad.
> *propio:* Los bancos deberán exponer en pizarras colocadas en los locales de atención al público como en las publicidades realizadas a través de medios gráficos (periódicos, revistas, carteleras en la vía pública, etc.) información sobre las tasas de interés que abonen sobre los saldos acreedores de las cuentas corrientes –cuando se reconozcan–, en tanto por ciento con dos decimales, con el siguiente detalle:

### Extracción (código A)

- **o1 Operacion** «Exposición de tasas de interés sobre saldos acreedores» — Exposición, en pizarras de los locales de atención al público y en publicidades por medios gráficos (periódicos, revistas, carteleras en la vía pública, etc.), de información sobre las tasas de interés que se abonan sobre los saldos acreedores de las cuentas corrientes, cuando se reconozcan. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «exponer en pizarras colocadas en los locales de atención al público como en las publicidades realizadas a través de medios gráficos (periódicos, revistas, carteleras en la vía pública, etc.) información sobre las tasas de interés que abonen sobre los saldos acreedores de las cuentas corrientes –cuando se reconozcan–»
- **ob1 Obligacion** «Exponer tasas de interés en pizarras y publicidad gráfica» — Los bancos deben exponer en pizarras de los locales de atención al público y en las publicidades por medios gráficos información sobre las tasas de interés que abonen sobre los saldos acreedores de las cuentas corrientes (cuando se reconozcan), en tanto por ciento con dos decimales, con el detalle que siguen los ítems del punto. · props: `{"tipo": "otra"}` · tramo [exacta]: «Los bancos deberán exponer en pizarras colocadas en los locales de atención al público como en las publicidades realizadas a través de medios gráficos (periódicos, revistas, carteleras en la vía pública, etc.) información sobre las tasas de interés que abonen sobre los saldos acreedores de las cuentas corrientes –cuand…»
- R: ob1 Obligacion —regula→ o1 Operacion
- R: ob1 Obligacion —aplica_a→ Sujeto_banco (mención «Los bancos»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:17 | no | «con el siguiente detalle:» | `extraida_tramo_verificado` |  | ob1 Obligacion [exacta], tramo que contiene «con el siguiente detalle:» |

## `ctacte::3.2.1.2` — El número de orden, impreso en el cuerpo del cheque librado en formato papel

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Cheques.
> *heredado:* 3.2. Títulos que carecen de valor como cheques.
> *heredado:* El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque:
> *heredado:* Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones.
> *heredado:* 3.2.1. Falta de alguna de las especificaciones contenidas en los artículos 2°, incisos 1 a 6, 4°,
> *heredado:* 23 y 54, incisos 1 a 9, de la Ley de Cheques, a saber:
> *propio:* 3.2.1.2. El número de orden, impreso en el cuerpo del cheque librado en formato papel o incorporado a los datos del cheque librado por medios electrónicos.

### Extracción (código A)

- **c1 Condicion** «Falta del número de orden del cheque» — Supuesto de falta de una de las especificaciones de la Ley de Cheques: el número de orden, impreso en el cuerpo del cheque librado en formato papel o incorporado a los datos del cheque librado por medios electrónicos. Condiciona la norma del punto 3.2 según la cual el título no valdrá como cheque (alcanza si falta cualquiera de las especificaciones enumeradas). · tramo [exacta]: «Falta de alguna de las especificaciones contenidas en los artículos 2°, incisos 1 a 6, 4°, 23 y 54, incisos 1 a 9, de la Ley de Cheques, a saber: […] El número de orden, impreso en el cuerpo del cheque librado en formato papel o incorporado a los datos del cheque librado por medios electrónicos.»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:8 | sí | «no valdrá como cheque» | `ausente` |  | ningún tramo contiene «no valdrá como cheque» (el de c1 cubre la lista de especificaciones); solo en la descripción de c1 |

## `ctacte::3.5.3` — Presentación al cobro.

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Cheques.
> *heredado:* 3.5. Cheques librados por medios electrónicos (ECHEQ).
> *propio:* 3.5.3. Presentación al cobro. El tenedor legitimado podrá efectuar la presentación al cobro de cada ECHEQ a partir de la correspondiente fecha de pago a través de una orden electrónica de acreditación o cobrarlo por ventanilla. En su defecto, quedará pendiente hasta la fecha de vencimiento del plazo previsto en el artículo 25 de la Ley de Cheques.

### Extracción (código A)

- **op1 Operacion** «Presentación al cobro de ECHEQ» — Presentación al cobro de cada ECHEQ por el tenedor legitimado a partir de la fecha de pago, mediante orden electrónica de acreditación o por ventanilla. · props: `{"tipo": "presentacion_al_cobro"}` · tramo [exacta]: «efectuar la presentación al cobro de cada ECHEQ a partir de la correspondiente fecha de pago»
- **p1 Potestad** «Presentar ECHEQ al cobro desde fecha de pago» — El tenedor legitimado puede presentar al cobro cada ECHEQ a partir de la fecha de pago, a través de una orden electrónica de acreditación o cobrándolo por ventanilla. · tramo [exacta]: «El tenedor legitimado podrá efectuar la presentación al cobro de cada ECHEQ a partir de la correspondiente fecha de pago a través de una orden electrónica de acreditación o cobrarlo por ventanilla.»
- **c1 Comunicacion** «Ley de Cheques» —  · props: `{"codigo": "Ley de Cheques", "tipo": "externa"}` · tramo [exacta]: «artículo 25 de la Ley de Cheques»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: p1 Potestad —aplica_a→ Sujeto (mención «El tenedor legitimado»)
- Omisión `fuera_de_tipos` [exacta]: «En su defecto, quedará pendiente hasta la fecha de vencimiento del plazo previsto en el artículo 25 de la Ley de Cheques.» — Consecuencia de no presentar el ECHEQ al cobro; no nombra quien la aplica ni encaja en ningún tipo.

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:27 | sí | «En su defecto» | `omision_otra_vez` | fuera_de_tipos | om#0 fuera_de_tipos [exacta] «En su defecto, quedará pendiente…» |

## `ctacte::5.1.2.2` — A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de En-

Grupos: omisiones.

### Texto

> *heredado:* Sección 5. Endosos, modalidades especiales de emisión y aval.
> *heredado:* 5.1. Endoso.
> *heredado:* 5.1.2. El cheque extendido a favor de una persona determinada, que no posea la cláusula "no a
> *heredado:* la orden", será transmisible por endoso. También podrán ser transmitidos por endoso los cheques con la citada condición ("no a la orden"), en los casos de transferencias –primeras y sucesivas– cuando se extienda:
> *heredado:* En los casos de cheques librados al portador o a favor de una persona determinada –que posean o no la cláusula "no a la orden"– y que sean entregados por su beneficiario a un tercero para la gestión de cobro mediante su presentación en ventanilla o a través de su depósito en cuenta para su compensación electrónica, se deberá consignar al dorso la firma y aclaración –o en el correspondiente registro electrónico, la identificación– del mandante u ordenante de la gestión y su número de identificación personal –según las normas sobre "Documentos de identificación en vigencia"– en los casos de personas físicas, o CUIT o CDI en los casos de personas jurídicas, independientemente de la existencia o no del documento que instrumenta el mandato. Adicionalmente, se insertará alguna de las siguientes expresiones: "en procuración", "valor al cobro" o "para su gestión de cobro", como manifestación de los efectos de ese endoso. La obligación de consignar el número de identificación personal o CUIT o CDI, según corresponda y la leyenda mencionada anteriormente recae, indistintamente, en el mandante u ordenante y el mandatario o gestor.
> *propio:* 5.1.2.2. A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras, en la medida en que se trate de operaciones relativas al fideicomiso.

### Extracción (código A)

- **p1 Potestad** «Endoso de cheques "no a la orden" a fiduciarios financieros» — Podrán ser transmitidos por endoso los cheques con la cláusula "no a la orden", en los casos de transferencias (primeras y sucesivas), cuando se extiendan a favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras, en la medida en que se trate de operaciones relativas al fideicomiso. · tramo [exacta]: «También podrán ser transmitidos por endoso los cheques con la citada condición ("no a la orden"), en los casos de transferencias –primeras y sucesivas– cuando se extienda: […] A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras, en la medida en que se trate de operaciones …»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:28 | sí | «comprendidos en la Ley de Entidades Financieras» | `extraida_tramo_verificado` |  | p1 Potestad [exacta], tramo que contiene «comprendidos en la Ley de Entidades Financieras» |

## `ctacte::6.1.2.7` — Giro sobre el librador, salvo que se tratara de un cheque girado entre distintos

Grupos: omisiones.

### Texto

> *heredado:* Sección 6. Rechazo de cheques.
> *heredado:* 6.1. Causales.
> *heredado:* 6.1.2. Defectos formales.
> *heredado:* Se define como defecto formal todo aquel verificado en la creación del cheque que el beneficiario no pueda advertir por su mera apariencia. Quedan incluidos, entre otros, los siguientes casos:
> *propio:* 6.1.2.7. Giro sobre el librador, salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador.

### Extracción (código A)

- **d1 Definicion** «Defecto formal: giro sobre el librador» — Se incluye entre los defectos formales (verificados en la creación del cheque, que el beneficiario no puede advertir por su mera apariencia) el giro sobre el librador. · props: `{"termino": "defecto formal"}` · tramo [exacta]: «Quedan incluidos, entre otros, los siguientes casos: […] Giro sobre el librador»
- **x1 Excepcion** «Excepción: cheque entre establecimientos del mismo librador» — Queda fuera del defecto formal 'giro sobre el librador' el cheque girado entre distintos establecimientos de un mismo librador. · tramo [exacta]: «salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador»
- Omisión `relacion_sin_predicado` [exacta]: «salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador» — Se habría usado `exceptua`, pero su rango es Restriccion y el caso exceptuado es una Definicion.

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:11 | sí | «Se define como defecto formal todo aquel verificado en la creación del cheque que el beneficiario no pueda advertir por su mera apariencia» | `ausente` |  | ninguna entidad cubre la definición del heredado; la omisión refiere al «salvo…» |

## `ext::1.5` — Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Régimen

Grupos: omisiones.

### Texto

> *heredado:* Sección 1. Disposiciones generales.
> *propio:* 1.5. Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Régimen Penal Cambiario.

### Extracción (código A)

- **c1 Comunicacion** «Ley del Régimen Penal Cambiario» —  · props: `{"codigo": "Ley del Régimen Penal Cambiario", "tipo": "externa"}` · tramo [exacta]: «Ley del Régimen Penal Cambiario»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- Omisión `fuera_de_tipos` [exacta]: «Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Régimen Penal Cambiario.» — Consecuencia de un incumplimiento (sujeción al régimen penal cambiario) sin sujeto que la aplique nombrado; se habría usado Obligacion o Potestad con consecuencia = 'Los incumplimientos a esta normati…

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:17 | sí | «Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Régimen Penal Cambiario.» | `omision_otra_vez` | fuera_de_tipos | om#0 fuera_de_tipos [exacta] con la oración entera; c1 Comunicacion cubre solo el nombre de la ley |

## `ext::10.11.5` — el pago es concretado en el marco de lo dispuesto en el punto 4.8.4. por un cliente

Grupos: omisiones.

### Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.11. Disposiciones complementarias para importaciones de bienes con registro de ingreso
> *heredado:* aduanero hasta el 12/12/23. Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:
> *propio:* 10.11.5. el pago es concretado en el marco de lo dispuesto en el punto 4.8.4. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24; o

### Extracción (código A)

- **c1 Condicion** «Pago por cliente con BOPREAL Serie 1 ≥50% (punto 4.8.4)» — Supuesto alternativo (uno de los que la entidad debe verificar, unidos por «o») de la excepción al requisito de conformidad previa del BCRA para el acceso al mercado de cambios para pagos de importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23: el pago es concretado en el marco del punto 4.8.4. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% del… · umbral: ['por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por…'] · tramo [exacta]: «el pago es concretado en el marco de lo dispuesto en el punto 4.8.4. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:24 | sí | «excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:» | `ausente` |  | ninguna entidad ni omisión cubre la frase del heredado |

## `ext::10.3.2.1` — Certifica en carácter de entidad encargada del seguimiento de la

Grupos: omisiones.

### Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero.
> *heredado:* 10.3.2. Requisitos de acceso para el pago de oficializaciones de importación comprendidas
> *heredado:* en el SEPAIMPO. La entidad interviniente podrá dar acceso al mercado de cambios para el pago al exterior de importaciones de bienes que cuentan con registro de ingreso aduanero que constan en el SEPAIMPO, en la medida que verifique previamente la totalidad de los siguientes requisitos:
> *heredado:* Los casos que no encuadren en lo expuesto precedentemente quedan sujetos a la conformidad previa del BCRA, debiendo los pedidos ser canalizados por una entidad autorizada a realizar este tipo de pagos.
> *propio:* 10.3.2.1. Certifica en carácter de entidad encargada del seguimiento de la oficialización que se cumplen las condiciones que se enuncian a continuación o cuenta con una certificación para realizar el pago emitida por la entidad que tiene tal responsabilidad i) Cuenta con constancia del registro aduanero del ingreso al país de los bienes que originan el pago a cancelarse. ii) Cuenta con copia de factura comercial emitida en el exterior a nombre del cliente residente en el país, que efectúa la compra al exterior, donde conste nombre y dirección del emisor, nombre del importador argentino, la cantidad y descripción de la mercadería, condición de venta y valor de la factura. iii) Cuenta con copia del Documento de Transporte (Conocimiento de Embarque – Carta de Porte – Guía Aérea). iv) Que la información que surge de la factura comercial y del Documento de Transporte sea consistente con la que figura en los registros aduaneros, considerando las normas de declaración aduanera aplicables. v) Que la documentación presentada le permita establecer la fecha de vencimiento de la obligación con el exterior por parte del importador o, en su defecto, que la operación no tiene una fecha de vencimiento pactada. vi) Que, en caso de tratarse de operaciones financiadas, la documentación presentada le permite calificar a la misma como una deuda por importaciones de bienes según lo dispuesto en el punto 10.2.4. vii) Que el total de los pagos realizados con imputación a la oficialización de importación, incluyendo el pago cuyo curso se está solicitando, no supera el monto facturado en la condición de compra pactada. viii) Que el beneficiario del pago a realizar sea el proveedor del exterior o, en su caso, la entidad financiera del exterior o la agencia oficial de crédito que financió la compra al proveedor del exterior en la medida que las operaciones encuadren como deuda comercial por importaciones de bienes, o el no residente que compró el crédito al acreedor comercial del exterior y en la medida que no se modifiquen las condiciones en las que se otorgó el crédito. ix) Cuenta con constancia de que la operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos". x) En el caso de importaciones oficializadas con anterioridad al 01/11/19, cuenta con una declaración jurada consignando el saldo de deuda pendiente a la fecha, firmada por el importador o quien ejerza su representación legal o un apoderado con facultades suficientes para asumir este compromiso en nombre del importador.

### Extracción (código A)

- **op1 Operacion** «Acceso al mercado de cambios — pago de importaciones SEPAIMPO» — Dar acceso al mercado de cambios, por la entidad interviniente, para el pago al exterior de importaciones de bienes que cuentan con registro de ingreso aduanero y constan en el SEPAIMPO. · props: `{"tipo": "acceso al mercado de cambios"}` · tramo [exacta]: «dar acceso al mercado de cambios para el pago al exterior de importaciones de bienes que cuentan con registro de ingreso aduanero que constan en el SEPAIMPO»
- **p1 Potestad** «Facultad de dar acceso al MLC con requisitos verificados (certificación)» — La entidad interviniente podrá dar acceso al mercado de cambios para el pago al exterior de importaciones de bienes con registro de ingreso aduanero que constan en el SEPAIMPO, en la medida que verifique previamente la totalidad de los requisitos; este requisito: certifica en carácter de entidad encargada del seguimiento de la oficialización que se cumplen las condiciones enunciadas o cuenta con u… · tramo [exacta]: «La entidad interviniente podrá dar acceso al mercado de cambios para el pago al exterior de importaciones de bienes que cuentan con registro de ingreso aduanero que constan en el SEPAIMPO, en la medida que verifique previamente la totalidad de los siguientes requisitos: […] Certifica en carácter de entidad encargada de…»
- **c0 Condicion** «Certificación como entidad de seguimiento o certificación de tal entidad» — La entidad certifica, como encargada del seguimiento de la oficialización, que se cumplen las condiciones enunciadas, o cuenta con una certificación para realizar el pago emitida por la entidad responsable del seguimiento. · tramo [exacta]: «Certifica en carácter de entidad encargada del seguimiento de la oficialización que se cumplen las condiciones que se enuncian a continuación o cuenta con una certificación para realizar el pago emitida por la entidad que tiene tal responsabilidad»
- **c1 Condicion** «Constancia de registro aduanero de ingreso» — Cuenta con constancia del registro aduanero del ingreso al país de los bienes que originan el pago a cancelarse. · tramo [exacta]: «Cuenta con constancia del registro aduanero del ingreso al país de los bienes que originan el pago a cancelarse.»
- **c2 Condicion** «Copia de factura comercial del exterior» — Cuenta con copia de factura comercial emitida en el exterior a nombre del cliente residente que efectúa la compra, donde conste nombre y dirección del emisor, nombre del importador argentino, cantidad y descripción de la mercadería, condición de venta y valor de la factura. · tramo [exacta]: «Cuenta con copia de factura comercial emitida en el exterior a nombre del cliente residente en el país, que efectúa la compra al exterior, donde conste nombre y dirección del emisor, nombre del importador argentino, la cantidad y descripción de la mercadería, condición de venta y valor de la factura.»
- **c3 Condicion** «Copia del Documento de Transporte» — Cuenta con copia del Documento de Transporte (Conocimiento de Embarque, Carta de Porte o Guía Aérea). · tramo [exacta]: «Cuenta con copia del Documento de Transporte (Conocimiento de Embarque – Carta de Porte – Guía Aérea).»
- **c4 Condicion** «Consistencia de la documentación con registros aduaneros» — La información de la factura comercial y del Documento de Transporte debe ser consistente con la de los registros aduaneros, considerando las normas de declaración aduanera aplicables. · tramo [exacta]: «Que la información que surge de la factura comercial y del Documento de Transporte sea consistente con la que figura en los registros aduaneros, considerando las normas de declaración aduanera aplicables.»
- **c5 Condicion** «Documentación que permita establecer fecha de vencimiento» — La documentación presentada permite establecer la fecha de vencimiento de la obligación con el exterior del importador o, en su defecto, que la operación no tiene fecha de vencimiento pactada. · tramo [exacta]: «Que la documentación presentada le permita establecer la fecha de vencimiento de la obligación con el exterior por parte del importador o, en su defecto, que la operación no tiene una fecha de vencimiento pactada.»
- **c6 Condicion** «Operaciones financiadas calificables como deuda por importaciones» — En operaciones financiadas, la documentación presentada permite calificarla como deuda por importaciones de bienes según lo dispuesto en el punto 10.2.4. · tramo [exacta]: «Que, en caso de tratarse de operaciones financiadas, la documentación presentada le permite calificar a la misma como una deuda por importaciones de bienes según lo dispuesto en el punto 10.2.4.»
- **c7 Condicion** «Pagos totales no superan el monto facturado» — El total de los pagos con imputación a la oficialización de importación, incluido el pago solicitado, no supera el monto facturado en la condición de compra pactada. · props: `{"umbrales": [{"tramo": "no\nsupera el monto facturado en la condición de compra pactada", "comparacion": "maximo_inclusivo", "base": "monto facturado en la condición de compra pactada", "regla_comparacion": "limite_relativo:negacion:raiz_super", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['no supera el monto facturado en la condición de compra pactada'] · tramo [exacta]: «Que el total de los pagos realizados con imputación a la oficialización de importación, incluyendo el pago cuyo curso se está solicitando, no supera el monto facturado en la condición de compra pactada.»
- **c8 Condicion** «Beneficiario del pago: proveedor, financista o comprador del crédito» — El beneficiario del pago es el proveedor del exterior o, en su caso, la entidad financiera del exterior o agencia oficial de crédito que financió la compra (si encuadra como deuda comercial por importaciones de bienes), o el no residente que compró el crédito al acreedor comercial del exterior (si no se modifican las condiciones en que se otorgó el crédito). · tramo [exacta]: «Que el beneficiario del pago a realizar sea el proveedor del exterior o, en su caso, la entidad financiera del exterior o la agencia oficial de crédito que financió la compra al proveedor del exterior en la medida que las operaciones encuadren como deuda comercial por importaciones de bienes, o el no residente que comp…»
- **c9 Condicion** «Constancia de declaración en Relevamiento de activos y pasivos externos» — Cuenta con constancia de que la operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos". · tramo [exacta]: «Cuenta con constancia de que la operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos".»
- **c10 Condicion** «DDJJ de saldo pendiente — importaciones anteriores al 01/11/19» — En importaciones oficializadas con anterioridad al 01/11/19, cuenta con una declaración jurada consignando el saldo de deuda pendiente a la fecha, firmada por el importador, su representante legal o un apoderado con facultades suficientes. · tramo [exacta]: «En el caso de importaciones oficializadas con anterioridad al 01/11/19, cuenta con una declaración jurada consignando el saldo de deuda pendiente a la fecha, firmada por el importador o quien ejerza su representación legal o un apoderado con facultades suficientes para asumir este compromiso en nombre del importador.»
- R: p1 Potestad —aplica_a→ Sujeto (mención «La entidad interviniente»)
- R: Sujeto (mención «La entidad interviniente») —ejecuta→ op1 Operacion
- R: c0 Condicion —condicion_de→ p1 Potestad
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: c4 Condicion —condicion_de→ p1 Potestad
- R: c5 Condicion —condicion_de→ p1 Potestad
- R: c6 Condicion —condicion_de→ p1 Potestad
- R: c7 Condicion —condicion_de→ p1 Potestad
- R: c8 Condicion —condicion_de→ p1 Potestad
- R: c9 Condicion —condicion_de→ p1 Potestad
- R: c10 Condicion —condicion_de→ p1 Potestad

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:2 | sí | «o cuenta con una certificación para realizar el pago emitida por la entidad que tiene tal responsabilidad» | `extraida_tramo_verificado` |  | p1 Potestad y c0 Condicion [exacta], tramos que contienen «o cuenta con una certificación…» |

## `ext::10.3.6` — Pagos de importaciones con cartas de crédito o letras avaladas emitidas u otorgadas

Grupos: grupo_c.

### Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero.
> *propio:* 10.3.6. Pagos de importaciones con cartas de crédito o letras avaladas emitidas u otorgadas por entidades financieras locales. La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente, en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad. En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha y, salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país. Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2. Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914. El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero".

### Extracción (código A)

- **c7914 Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- **op1 Operacion** «Cancelación de cartas de crédito o letras avaladas de importaciones — acceso al mercado de cambios» — Cancelación por la entidad de cartas de crédito o letras avaladas emitidas u otorgadas por entidades financieras locales para garantizar importaciones de bienes con registro de ingreso aduanero, con acceso al mercado de cambios incluso sin cumplir los requisitos del cliente · props: `{"tipo": "compra de moneda extranjera para cancelar garantías"}` · tramo [exacta]: «cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes»
- **pot1 Potestad** «Acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas» — La entidad tiene acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de bienes con registro aduanero, incluso cuando no se cumplan los requisitos de acceso del cliente · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente»
- **cond1 Condicion** «Documentación que acredite condiciones aplicables a la emisión» — La entidad cuenta con documentación que demuestre que al momento de la apertura o emisión se cumplían las condiciones aplicables según la fecha de emisión u otorgamiento y el tipo de operación garantizada · tramo [exacta]: «en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad»
- **ob1 Obligacion** «Contar con documentación — emisiones desde 13/12/23» — Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad debe contar con documentación que demuestre que al momento de la apertura o emisión la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha y, salvo que la operación quedase comprendida en el punto 10.10.2.11., que el pago garantizado de… · props: `{"tipo": "otra"}` · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha»
- **exc1 Excepcion** «Excepción punto 10.10.2.11 — fecha de pago garantizado» — Exceptúa de la exigencia de documentación sobre la fecha desde la que el pago garantizado debía concretarse (plazo del punto 10.10.1. más 15 días corridos desde la fecha estimada de arribo) a las operaciones comprendidas en la situación del punto 10.10.2.11. · tramo [exacta]: «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- **cond2 Condicion** «Emisión u otorgamiento desde 14/04/25 y demás condiciones cumplidas» — Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones · tramo [exacta]: «Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones»
- **pot2 Potestad** «Admisión de pago garantizado desde fecha estimada de embarque más 15 días» — Para las emitidas u otorgadas a partir del 14/04/25 se admite que el pago garantizado debiera concretarse a partir de la fecha estimada de embarque en origen más 15 días corridos, cuando correspondía a la porción de una operación con pagos a la vista según los puntos 10.10.2.1. o 10.10.2.2. · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo p…»
- **ob2 Obligacion** «Boleto de venta a nombre de la entidad — concepto B14» — El boleto de venta debe efectuarse a nombre de la propia entidad en calidad de cliente por el concepto B14 Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero".»
- R: to TextoOrdenado —referencia→ c7914 Comunicacion
- R: pot1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: ob1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: pot2 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: ob2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la propia entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion
- R: cond1 Condicion —condicion_de→ pot1 Potestad
- R: cond2 Condicion —condicion_de→ pot2 Potestad
- R: exc1 Excepcion —exceptua_obligacion→ ob1 Obligacion
- R: ob2 Obligacion —regula→ op1 Operacion
- Omisión `meta_normativo` [exacta]: «Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914.» — Remisión informativa a una norma anterior: no prescribe conducta nueva.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «emitidas desde el 13/12/23 (más 15 días)» | `dentro_de_norma` |  | dentro de la Obligacion ob1 («Contar con documentación — emisiones desde 13/12/23», tramo); sin Condicion |
| 2 | «desde el 14/04/25» | `condicion_con_relacion` |  | cond2 Condicion «Emisión u otorgamiento desde 14/04/25…» —condicion_de→ pot2 Potestad |
| 3 | «con pagos a la vista» | `dentro_de_norma` |  | dentro de la Potestad pot2 (tramo «…cuando correspondía a la porción… pagos a la vista») |

## `ext::10.4.4` — Cancelación de garantías comerciales de importaciones de bienes otorgadas por

Grupos: grupo_c.

### Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.4. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente.
> *propio:* 10.4.4. Cancelación de garantías comerciales de importaciones de bienes otorgadas por entidades financieras locales. La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero pendiente, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente, en la medida que se verifique que se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad. En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha y, salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país. Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2. Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914. El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B11. Cancelación de garantías comerciales de entidades financieras de importaciones de bienes sin registro de ingreso aduanero". Por los pagos que se realicen, la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuado el pago. En la medida que la entidad no cuente con el registro de la oficialización del despacho de importación dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cambios, la entidad deberá efectuar la correspondiente denuncia.

### Extracción (código A)

- **c7914 Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- **op1 Operacion** «Cancelación de cartas de crédito o letras avaladas (importaciones)» — Acceso al mercado de cambios por la entidad para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de bienes con registro aduanero pendiente, incluso cuando no se cumplan los requisitos de acceso del cliente · props: `{"tipo": "compra de moneda extranjera para cancelar garantías comerciales"}` · tramo [exacta]: «cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero pendiente»
- **pot1 Potestad** «Acceso al mercado de cambios para cancelar garantías» — La entidad tiene acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas, incluso cuando no se cumplan los requisitos de acceso del cliente · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas»
- **cond1 Condicion** «Condiciones aplicables según fecha y tipo de operación» — Se verifica que se cumplían las condiciones aplicables según la fecha de emisión u otorgamiento y el tipo de operación garantizada · tramo [exacta]: «en la medida que se verifique que se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad»
- **ob1 Obligacion** «Contar con documentación de la operación garantizada (desde 13/12/23)» — Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, contar con documentación que demuestre que al momento de la apertura o emisión la operación garantizada era una importación con registro de ingreso aduanero a partir de dicha fecha y, salvo la situación del punto 10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la fecha resultan… · props: `{"tipo": "otra"}` · umbral: ['otros 15 (quince) días corridos'] · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha»
- **exc1 Excepcion** «Salvo situación del punto 10.10.2.11» — Exceptúa de demostrar que el pago garantizado debía concretarse a partir de la fecha de arribo más plazo, cuando la operación queda comprendida en el punto 10.10.2.11. · tramo [exacta]: «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- **pot2 Potestad** «Admisión de pago desde fecha estimada de embarque (desde 14/04/25)» — Para emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, se admite que el pago garantizado tuviera que concretarse desde la fecha estimada de embarque cuando correspondía a la porción de una operación con pagos a la vista según puntos 10.10.2.1. o 10.10.2.2. · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen»
- **cond2 Condicion** «Cumplimiento de las restantes condiciones» — Se cumplen las restantes condiciones; aplica a cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14/04/25 · tramo [exacta]: «en la medida que se cumplan las restantes condiciones»
- **ob2 Obligacion** «Boleto de venta a nombre de la entidad, concepto B11» — El boleto de venta se efectúa a nombre de la propia entidad en calidad de cliente por el concepto B11 · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B11. Cancelación de garantías comerciales de entidades financieras de importaciones de bienes sin registro de ingreso aduanero".»
- **ob3 Obligacion** «Informar CUIT del importador en SEPAIMPO en 5 días hábiles» — Por los pagos realizados, informar en el SEPAIMPO la CUIT del importador por el cual se efectuó el pago · props: `{"tipo": "reporte_al_supervisor"}` · umbral: ['dentro de los 5 (cinco) días hábiles'] · tramo [exacta]: «la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuado el pago»
- **cond3 Condicion** «Sin registro de oficialización a 90 días corridos» — La entidad no cuenta con el registro de la oficialización del despacho de importación dentro de los 90 días corridos de la fecha de acceso al mercado de cambios · umbral: ['dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cam…'] · tramo [exacta]: «En la medida que la entidad no cuente con el registro de la oficialización del despacho de importación dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cambios»
- **ob4 Obligacion** «Efectuar denuncia por falta de registro de despacho» — Efectuar la correspondiente denuncia cuando no se cuente con el registro de la oficialización del despacho de importación dentro de los 90 días corridos · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «la entidad deberá efectuar la correspondiente denuncia»
- R: to TextoOrdenado —referencia→ c7914 Comunicacion
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion
- R: pot1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: ob1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: ob2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la propia entidad»)
- R: ob3 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: ob4 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: cond1 Condicion —condicion_de→ pot1 Potestad
- R: cond2 Condicion —condicion_de→ pot2 Potestad
- R: cond3 Condicion —condicion_de→ ob4 Obligacion
- R: exc1 Excepcion —exceptua_obligacion→ ob1 Obligacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion
- Omisión `meta_normativo` [exacta]: «Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914.» — Declaración informativa/remisión sobre dónde se receptaron condiciones históricas; no prescribe conducta.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «emitidas desde el 13/12/23» | `dentro_de_norma` |  | dentro de la Obligacion ob1 («desde 13/12/23» en label, descripción y tramo); no hay Condicion para la fecha |
| 2 | «desde el 14/04/25» | `dentro_de_norma` |  | dentro de la Potestad pot2 (descripción «desde 14/04/25»); cond2 es «las restantes condiciones», no la fecha |
| 3 | «con pagos a la vista» | `dentro_de_norma` |  | dentro de la Potestad pot2 (descripción) |
| 4 | «sin oficialización a 90 días» | `condicion_con_relacion` |  | cond3 Condicion con el umbral —condicion_de→ ob4 Obligacion |

## `ext::10.5.5.2` — Operaciones en gestión de cobro por incumplimiento del proveedor.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.5. Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente.
> *heredado:* Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 estará sujeto a un seguimiento desde la fecha de acceso al mercado de cambios hasta la fecha en que se produzca su regularización. Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento de ese pago, y por hasta el monto girado, la existencia de:
> *heredado:* i) el registro de ingreso aduanero a su nombre o a nombre de un tercero en la medida
> *heredado:* que se cumplan las condiciones establecidas en la presente normativa; y/o
> *heredado:* ii) la liquidación en el mercado de cambios de las divisas asociadas a la devolución del
> *heredado:* pago efectuado; y/o
> *heredado:* iii) otras formas de regularización previstas en la presente norma según las condiciones
> *heredado:* y límites establecidos en cada caso; y/o
> *heredado:* iv) la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la
> *heredado:* operación. El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago y deberá estar debidamente justificado por ésta.
> *heredado:* 10.5.5. Prórrogas de plazos para la demostración del registro de ingreso aduanero.
> *heredado:* Las prórrogas del plazo para la demostración del registro de ingreso aduanero de importación serán concedidas por la entidad a cargo del seguimiento del pago realizado sin registro de ingreso aduanero, dentro de las condiciones que establece la presente normativa o con la previa conformidad del BCRA. Estas prórrogas deberán ser registradas por la entidad encargada del seguimiento del pago en el sistema SEPAIMPO.
> *propio:* 10.5.5.2. Operaciones en gestión de cobro por incumplimiento del proveedor. La entidad a cargo del seguimiento del pago realizado, podrá imputarlo en el SEPAIMPO como en "gestión de cobro" cuando se dé alguna de las siguientes condiciones: i) Control de cambios en el país del exportador. El importador puede demostrar su gestión de cobro y que la falta de ingreso obedece a que, en el país del proveedor del exterior, existen demoras por restricciones a los giros de divisas. Lo cual será acreditado mediante copia con legalización consular, de la normativa que dispone dicho control cambiario. ii) Insolvencia posterior del proveedor del exterior, no contándose con garantías de devolución de los fondos. En la medida que el importador argentino aporte la siguiente documentación: a) constancia de las publicaciones que hagan saber el inicio del trámite falencial conforme a lo exigido por la legislación vigente en el país en que tramite; y b) constancia de la presentación efectuada para obtener el reconocimiento y pago de su acreencia, certificada por la autoridad interviniente en el proceso, conforme al procedimiento aplicable en país donde haya debido efectuarla. La documentación deberá estar legalizada por autoridad consular o conforme a lo previsto por el Convenio de la Haya del 5 de octubre de 1961, cuando corresponda. iii) Deudor moroso. En la medida que se verifique alguna de las siguientes situaciones: a) El importador demuestre en forma fehaciente su gestión de cobro a través de los reclamos efectuados al obligado de pago por compañías de seguro de crédito a la exportación o de entidades constituidas como agencias de recupero nacionales o del exterior contratadas por el importador a tal efecto. Esta alternativa solo será válida en la medida que el valor adeudado al importador por el no residente no supere el equivalente de USD 100.000 (dólares estadounidenses cien mil); y/o b) El importador argentino haya iniciado y mantenga acciones judiciales contra el proveedor del exterior o contra quien corresponda, acreditándolo con copia del escrito de iniciación de demanda certificada por el juzgado interviniente en cuanto a su fecha de inicio y radicación. La documentación deberá estar legalizada por autoridad consular o conforme a lo previsto por el Convenio de la Haya del 5 de octubre de 1961, cuando resultase aplicable. En todos los casos, la entidad deberá exigir, además de la documentación señalada, una declaración jurada sobre el carácter genuino de lo declarado, firmada por el importador o quien ejerza su representación legal o un apoderado con facultades suficientes para asumir este compromiso en nombre del importador. Si el importador percibiera un monto en moneda extranjera, el mismo deberá ser ingresado y liquidado en el mercado de cambios dentro de los 20 (veinte) días hábiles siguientes a la fecha de efectiva percepción. En todos estos casos, la operación podrá permanecer en "gestión de cobro" mientras se demuestre la vigencia del reclamo y de las condiciones que explican la demora en la ejecución de la transferencia. A estos fines, la entidad otorgará hasta cinco prórrogas sucesivas de hasta 180 (ciento ochenta) días corridos. Utilizados los plazos máximos con sus sucesivas renovaciones, la entidad registrará la condición de no recupero total o parcial de los fondos en el SEPAIMPO, dando por finalizado su seguimiento del pago. Esto es independiente de la obligación del importador de ingresar por el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro, todo recupero en moneda extranjera que registre con relación a dicho pago.

### Extracción (código A)

- Rechazos del validador r2: relacion:firma_invalida, relacion:firma_invalida
- **op1 Operacion** «Imputación en gestión de cobro (SEPAIMPO)» — Imputar en el SEPAIMPO como en gestión de cobro el pago realizado sin registro de ingreso aduanero, por incumplimiento del proveedor, realizada por la entidad a cargo del seguimiento del pago · props: `{"tipo": "otra"}` · tramo [exacta]: «podrá imputarlo en el SEPAIMPO como en "gestión de cobro"»
- **p1 Potestad** «Facultad de imputar pago en gestión de cobro» — La entidad a cargo del seguimiento del pago puede imputarlo en el SEPAIMPO como en gestión de cobro cuando se dé alguna de las condiciones i), ii) o iii) · tramo [exacta]: «La entidad a cargo del seguimiento del pago realizado, podrá imputarlo en el SEPAIMPO como en "gestión de cobro" cuando se dé alguna de las siguientes condiciones»
- **c1 Condicion** «Control de cambios en país del exportador» — El importador demuestra su gestión de cobro y que la falta de ingreso obedece a demoras por restricciones a los giros de divisas en el país del proveedor; se acredita con copia con legalización consular de la normativa que dispone el control cambiario · tramo [exacta]: «El importador puede demostrar su gestión de cobro y que la falta de ingreso obedece a que, en el país del proveedor del exterior, existen demoras por restricciones a los giros de divisas.»
- **c2 Condicion** «Insolvencia posterior del proveedor sin garantías» — Insolvencia posterior del proveedor del exterior, sin garantías de devolución de los fondos, en la medida que el importador aporte la documentación de los puntos a) y b) legalizada · tramo [exacta]: «Insolvencia posterior del proveedor del exterior, no contándose con garantías de devolución de los fondos.»
- **c2a Condicion** «Constancia de publicaciones del trámite falencial» — El importador aporta constancia de las publicaciones del inicio del trámite falencial según la legislación del país donde tramite (se exige junto con la constancia b); condiciona la insolvencia posterior del proveedor) · tramo [exacta]: «constancia de las publicaciones que hagan saber el inicio del trámite falencial conforme a lo exigido por la legislación vigente en el país en que tramite»
- **c2b Condicion** «Constancia de presentación de acreencia certificada» — El importador aporta constancia de la presentación para obtener reconocimiento y pago de su acreencia, certificada por la autoridad interviniente, según el procedimiento del país (se exige junto con la constancia a)) · tramo [exacta]: «constancia de la presentación efectuada para obtener el reconocimiento y pago de su acreencia, certificada por la autoridad interviniente en el proceso»
- **c3a Condicion** «Deudor moroso: reclamos por seguro o recupero, hasta USD 100.000» — Deudor moroso: el importador demuestra su gestión de cobro mediante reclamos de compañías de seguro de crédito a la exportación o agencias de recupero contratadas; válida solo si el valor adeudado por el no residente no supera USD 100.000 (alternativa con b) · umbral: ['solo será válida en la medida que el valor adeudado al importador por el no resi…'] · tramo [exacta]: «El importador demuestre en forma fehaciente su gestión de cobro a través de los reclamos efectuados al obligado de pago por compañías de seguro de crédito a la exportación o de entidades constituidas como agencias de recupero nacionales o del exterior contratadas por el importador a tal efecto.»
- **c3b Condicion** «Deudor moroso: acciones judiciales iniciadas y mantenidas» — Deudor moroso: el importador inició y mantiene acciones judiciales contra el proveedor o quien corresponda, acreditado con copia del escrito de demanda certificada por el juzgado; documentación legalizada por autoridad consular o Convenio de la Haya del 5/10/1961 cuando resulte aplicable (alternativa con a)) · tramo [exacta]: «El importador argentino haya iniciado y mantenga acciones judiciales contra el proveedor del exterior o contra quien corresponda, acreditándolo con copia del escrito de iniciación de demanda certificada por el juzgado interviniente en cuanto a su fecha de inicio y radicación.»
- **o1 Obligacion** «Exigir declaración jurada de carácter genuino» — En todos los casos, la entidad debe exigir, además de la documentación, una declaración jurada sobre el carácter genuino de lo declarado, firmada por el importador, su representante legal o un apoderado con facultades suficientes · props: `{"tipo": "otra"}` · tramo [exacta]: «la entidad deberá exigir, además de la documentación señalada, una declaración jurada sobre el carácter genuino de lo declarado, firmada por el importador o quien ejerza su representación legal o un apoderado con facultades suficientes»
- **o2 Obligacion** «Ingreso y liquidación en 20 días hábiles de lo percibido» — Si el importador percibe un monto en moneda extranjera, debe ingresarlo y liquidarlo en el mercado de cambios dentro de los 20 días hábiles siguientes a la efectiva percepción · props: `{"tipo": "otra"}` · umbral: ['dentro de los 20 (veinte) días hábiles siguientes a la fecha de efectiva percepc…'] · tramo [exacta]: «Si el importador percibiera un monto en moneda extranjera, el mismo deberá ser ingresado y liquidado en el mercado de cambios dentro de los 20 (veinte) días hábiles siguientes a la fecha de efectiva percepción.»
- **op2 Operacion** «Ingreso y liquidación en el mercado de cambios de lo percibido» — Ingreso y liquidación en el mercado de cambios del monto en moneda extranjera percibido por el importador · props: `{"tipo": "otra"}` · tramo [exacta]: «ingresado y liquidado en el mercado de cambios»
- **o3 Obligacion** «Hasta cinco prórrogas sucesivas de 180 días» — Mientras se demuestre la vigencia del reclamo y de las condiciones que explican la demora, la entidad otorga hasta cinco prórrogas sucesivas de hasta 180 días corridos para mantener la operación en gestión de cobro · props: `{"tipo": "otra", "umbrales": [{"tramo": "hasta cinco prórrogas sucesivas", "comparacion": "maximo_inclusivo", "base": "cinco prórrogas sucesivas", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['hasta cinco prórrogas sucesivas', 'hasta 180 (ciento ochenta) días corridos'] · tramo [exacta]: «la entidad otorgará hasta cinco prórrogas sucesivas de hasta 180 (ciento ochenta) días corridos.»
- **c4 Condicion** «Vigencia del reclamo y de condiciones de la demora» — Permanencia en gestión de cobro mientras se demuestre la vigencia del reclamo y de las condiciones que explican la demora en la transferencia · tramo [exacta]: «mientras se demuestre la vigencia del reclamo y de las condiciones que explican la demora en la ejecución de la transferencia»
- **o4 Obligacion** «Registrar no recupero en SEPAIMPO y finalizar seguimiento» — Utilizados los plazos máximos con sus renovaciones, la entidad registra en el SEPAIMPO la condición de no recupero total o parcial de los fondos y finaliza su seguimiento del pago · props: `{"tipo": "otra"}` · tramo [exacta]: «la entidad registrará la condición de no recupero total o parcial de los fondos en el SEPAIMPO, dando por finalizado su seguimiento del pago.»
- **o5 Obligacion** «Ingreso por mercado de cambios de todo recupero en 20 días hábiles» — Independientemente del registro de no recupero, el importador debe ingresar por el mercado de cambios dentro de 20 días hábiles de la fecha de cobro todo recupero en moneda extranjera relativo al pago · props: `{"tipo": "otra"}` · umbral: ['dentro de los 20 (veinte) días hábiles de la fecha de cobro'] · tramo [exacta]: «la obligación del importador de ingresar por el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro, todo recupero en moneda extranjera que registre con relación a dicho pago.»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3a Condicion —condicion_de→ p1 Potestad
- R: c3b Condicion —condicion_de→ p1 Potestad
- R: c4 Condicion —condicion_de→ o3 Obligacion
- R: p1 Potestad —aplica_a→ Sujeto (mención «La entidad a cargo del seguimiento del pago realizado»)
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o2 Obligacion —aplica_a→ Sujeto_importador (mención «el importador»)
- R: o3 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o4 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o5 Obligacion —aplica_a→ Sujeto_importador (mención «el importador»)
- R: Sujeto (mención «La entidad a cargo del seguimiento del pago realizado») —ejecuta→ op1 Operacion
- R: Sujeto_importador (mención «el importador») —ejecuta→ op2 Operacion
- R: o2 Obligacion —regula→ op2 Operacion
- Omisión `fuera_de_tipos` [exacta]: «La documentación deberá estar legalizada por autoridad consular o conforme a lo previsto por el Convenio de la Haya del 5 de octubre de 1961, cuando corresponda.» — Requisito de legalización de la documentación del punto ii); habría sido Obligacion del importador/condición adicional; se registró solo en la descripción de la Condicion c2, sin sujeto explícito.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «i) control de cambios» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ p1 Potestad |
| 2 | «ii) insolvencia (con a y b)» | `condicion_con_relacion` |  | c2 Condicion (con c2a y c2b sin relación) —condicion_de→ p1 Potestad |
| 3 | «a hasta USD 100.000» | `condicion_con_relacion` |  | c3a Condicion con el umbral —condicion_de→ p1 Potestad |
| 4 | «b acciones judiciales» | `condicion_con_relacion` |  | c3b Condicion —condicion_de→ p1 Potestad |
| 5 | «percepción en moneda extranjera» | `dentro_de_norma` |  | dentro de la Obligacion o2 (tramo «Si el importador percibiera…»); sin Condicion |

## `ext::10.5::intro` — [bloque intro] Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente.

Grupos: omisiones.

### Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.5. Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente.
> *propio:* Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 estará sujeto a un seguimiento desde la fecha de acceso al mercado de cambios hasta la fecha en que se produzca su regularización. Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento de ese pago, y por hasta el monto girado, la existencia de: i) el registro de ingreso aduanero a su nombre o a nombre de un tercero en la medida que se cumplan las condiciones establecidas en la presente normativa; y/o ii) la liquidación en el mercado de cambios de las divisas asociadas a la devolución del pago efectuado; y/o iii) otras formas de regularización previstas en la presente norma según las condiciones y límites establecidos en cada caso; y/o iv) la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la operación. El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago y deberá estar debidamente justificado por ésta.

### Extracción (código A)

- **op1 Operacion** «Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente» — Seguimiento de todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19, desde la fecha de acceso al mercado de cambios hasta la fecha de su regularización. · props: `{"tipo": "seguimiento de pagos"}` · tramo [exacta]: «Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 estará sujeto a un seguimiento desde la fecha de acceso al mercado de cambios hasta la fecha en que se produzca su regularización.»
- **def1 Definicion** «Pago regularizado a efectos cambiarios» — La situación de estos pagos se considera regularizada a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento, por hasta el monto girado, la existencia de: i) registro de ingreso aduanero a su nombre o a nombre de un tercero en la medida que se cumplan las condiciones de la normativa; y/o ii) liquidación en el mercado de cambios de las divisas asociadas a la devoluci… · props: `{"termino": "regularizada"}` · tramo [exacta]: «Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento de ese pago, y por hasta el monto girado, la existencia de:»
- **op2 Operacion** «Pedido de conformidad del BCRA para regularizar pago» — Pedido de conformidad al BCRA para dar por regularizada parte o el total de la operación de pago de importaciones con registro de ingreso aduanero pendiente. · props: `{"tipo": "otra"}` · tramo [exacta]: «la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la operación. El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago»
- **r1 Restriccion** «Solo la entidad encargada del seguimiento tramita el pedido» — El pedido de conformidad del BCRA solo podrá ser tramitado por la entidad encargada del seguimiento del pago. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago»
- **o1 Obligacion** «Justificar debidamente el pedido de conformidad» — El pedido de conformidad del BCRA debe estar debidamente justificado por la entidad encargada del seguimiento del pago. · props: `{"tipo": "otra"}` · tramo [exacta]: «deberá estar debidamente justificado por ésta»
- R: r1 Restriccion —limita→ op2 Operacion
- R: o1 Obligacion —regula→ op2 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto (mención «la entidad encargada del seguimiento del pago»)
- R: o1 Obligacion —aplica_a→ Sujeto (mención «la entidad encargada del seguimiento del pago»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:4 | sí | «a los efectos cambiarios» | `extraida_tramo_verificado` |  | def1 Definicion [exacta], tramo que contiene «a los efectos cambiarios» |

## `ext::13.3.9` — el pago sea a una contraparte no vinculada al cliente y se concrete

Grupos: omisiones.

### Texto

> *heredado:* Sección 13. Pagos de servicios prestados por no residentes.
> *heredado:* 13.3. Pagos de servicios que fueron o serán prestados o devengados a partir del 13/12/23 con
> *heredado:* anterioridad a lo previsto en los puntos 13.2.3. a 13.2.7. También será admisible el acceso para el pago de servicios que fueron o serán prestados o devengados a partir del 13/12/23 con antelación a los plazos previstos en los puntos 13.2.3. a 13.2.7., cuando adicionalmente a los restantes requisitos normativo, se verifique el encuadre en alguna de las siguientes situaciones:
> *propio:* 13.3.9. el pago sea a una contraparte no vinculada al cliente y se concrete mediante la realización de un canje y/o arbitraje con los fondos depositados en una cuenta en moneda extranjera en una entidad financiera local.

### Extracción (código A)

- **c1 Condicion** «Pago a contraparte no vinculada mediante canje/arbitraje» — Supuesto alternativo (basta alguna de las situaciones del punto 13.3) para que sea admisible el acceso al pago de servicios prestados o devengados a partir del 13/12/23 con antelación a los plazos de los puntos 13.2.3. a 13.2.7.: el pago es a una contraparte no vinculada al cliente y se concreta mediante canje y/o arbitraje con fondos depositados en una cuenta en moneda extranjera en una entidad f… · tramo [exacta]: «el pago sea a una contraparte no vinculada al cliente y se concrete mediante la realización de un canje y/o arbitraje con los fondos depositados en una cuenta en moneda extranjera en una entidad financiera local»
- Omisión `fuera_de_tipos` [exacta]: «También será admisible el acceso para el pago de servicios que fueron o serán prestados o devengados a partir del 13/12/23 con antelación a los plazos previstos en los puntos 13.2.3. a 13.2.7.» — La norma del encabezado (admisibilidad del acceso al mercado de cambios para el pago de servicios con antelación a los plazos) no se compone en el ítem porque no está claro que sea una Potestad ni una…

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:1 | sí | «También será admisible el acceso para el pago de servicios que fueron o serán prestados o devengados a partir del 13/12/23 con antelación a los plazos previstos…» | `omision_otra_vez` | fuera_de_tipos | om#0 fuera_de_tipos [exacta] con la primera parte de la oración del heredado («También será admisible… 13.2.7.») |

## `ext::13.5` — Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas por entidades

Grupos: omisiones.

### Texto

> *heredado:* Sección 13. Pagos de servicios prestados por no residentes.
> *propio:* 13.5. Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas por entidades financieras para garantizar importaciones de servicios. Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios, en la medida que se verifique que cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada. En particular, en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23 y el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le corresponde al servicio por el punto 13.2. más otros 15 (quince) días corridos a la fecha estimada de prestación o devengamiento del servicio. En caso de tratarse una operación del concepto "S30. Servicios de fletes por operaciones de importaciones de bienes" que encuadra en lo previsto en el punto 10.10.2.1., debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar 15 (quince) días corridos a la fecha estimada de embarque de los bienes en origen.

### Extracción (código A)

- **op1 Operacion** «Pago propio por cartas de crédito o letras avaladas — importación de servicios» — Pagos propios de entidades financieras, con acceso al mercado de cambios, por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios. · props: `{"tipo": "pago al exterior"}` · tramo [exacta]: «cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios»
- **pot1 Potestad** «Acceso al mercado de cambios para pagos propios por cartas de crédito o letras avaladas» — Las entidades financieras tienen acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de servicios. · tramo [exacta]: «Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios»
- **c1 Condicion** «Cumplimiento de condiciones aplicables a la fecha de emisión» — Se verifique que cumplían las condiciones aplicables según la fecha de emisión u otorgamiento de la carta de crédito o letra avalada. · tramo [exacta]: «en la medida que se verifique que cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada»
- **ob1 Obligacion** «Contar con documentación del servicio y pago garantizado (desde 13/12/23)» — Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad debe contar con documentación que demuestre que al emitirse la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23 y que el pago debía concretarse desde la fecha resultante de adicionar el plazo del punto 13.2 más 15 días corridos a la fecha estimada de prestación… · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos a la fecha estimada de prestación o devengam…'] · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23 y el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días …»
- **ob2 Obligacion** «Pago S30 fletes importación: 15 días desde embarque estimado» — Para operaciones del concepto S30 (fletes por importaciones de bienes) que encuadran en el punto 10.10.2.1., el pago garantizado debía ser concretado por el cliente a partir de la fecha resultante de adicionar 15 días corridos a la fecha estimada de embarque de los bienes en origen; la entidad debe contar con la documentación que lo demuestre. · props: `{"tipo": "otra"}` · umbral: ['adicionar 15 (quince) días corridos a la fecha estimada de embarque de los biene…'] · tramo [exacta]: «En caso de tratarse una operación del concepto "S30. Servicios de fletes por operaciones de importaciones de bienes" que encuadra en lo previsto en el punto 10.10.2.1., debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar 15 (quince) días corridos a la fecha estimada de embarque de los bi…»
- R: pot1 Potestad —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- R: ob1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad»)
- R: ob2 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- R: Sujeto_entidad_financiera (mención «Las entidades financieras») —ejecuta→ op1 Operacion
- R: c1 Condicion —condicion_de→ pot1 Potestad
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:24 | sí | «En particular, en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23» | `ausente` |  | ningún tramo contiene «En particular, en el caso de cartas…»: el de ob1 empieza en «la entidad deberá contar…»; solo en la descripción de ob1 |

## `ext::14.5.7` — Los aportes de inversión directa en especie instrumentados mediante la entrega al

Grupos: grupo_c.

### Texto

> *heredado:* Sección 14. Disposiciones complementarias asociadas al Régimen de Incentivo para Grandes Inversiones (RIGI).
> *heredado:* En esta sección se detallan las disposiciones complementarias en materia cambiaria que, en la medida que las disposiciones generales no resulten más favorables, resultan aplicables a un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo los referidas al "Régimen de Incentivo para Grandes Inversiones" (RIGI) establecido en el Título VII de la Ley 27.742 y reglamentado por el Decreto 749/24 y concordantes.
> *heredado:* 14.5. Otras disposiciones.
> *propio:* 14.5.7. Los aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital podrán ser computados como ingresados y liquidados en el mercado de cambios en la medida que: i) El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte que será computado como ingresado y liquidado en el mercado de cambios. La operación podrá incluir bienes que no revistan la condición de bien de capital en la medida que aquellos que lo sean representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado y la entidad cuente con una declaración jurada del cliente en la cual deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios para el funcionamiento, construcción o instalación de los bienes de capital que se están adquiriendo. La entidad deberá contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO). ii) El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte. En caso de no disponerla, deberá presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio de la decisión de capitalización definitiva de los aportes de capital computados de acuerdo con los requisitos legales correspondientes y comprometerse a presentar la documentación de la capitalización definitiva del aporte dentro de los 365 (trescientos sesenta y cinco) días corridos desde el inicio del trámite. iii) Una entidad financiera haya registrado al aporte de capital en el régimen informático de operaciones de cambio (RIOC) mediante la confección de dos boletos de cambio sin movimiento de fondos con las siguientes características: a) Los boletos deberán ser registrados en la fecha en que se produjo el registro de ingreso aduanero de los bienes, independientemente de cuál sea el momento en que el cliente solicite su registro ante la entidad financiera. b) El boleto de compra se confeccionará con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo. En caso de que el VPU contemple la posibilidad de aplicar cobros de exportaciones de bienes para la repatriación del aporte, la entidad deberá asignar el correspondiente número de identificación (número APX) para el "Seguimiento de anticipos y otras financiaciones de exportación de bienes", el cual quedará a cargo de la propia entidad. c) El boleto de venta se confeccionará con el código de concepto de pago diferido de importaciones de bienes de capital, dejando constancia que el pago se enmarca en el presente mecanismo.

### Extracción (código A)

- **op1 Operacion** «Aporte de inversión directa en especie con bienes de capital» — Aporte de inversión directa en especie instrumentado mediante la entrega al VPU de bienes de capital, computable como ingresado y liquidado en el mercado de cambios. · props: `{"tipo": "aporte de inversión directa"}` · tramo [exacta]: «Los aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital»
- **p1 Potestad** «Computar aporte en especie como ingresado y liquidado» — Los aportes de inversión directa en especie mediante entrega al VPU de bienes de capital podrán computarse como ingresados y liquidados en el mercado de cambios si se cumplen las condiciones i) a iii). · tramo [exacta]: «podrán ser computados como ingresados y liquidados en el mercado de cambios en la medida que»
- **c1 Condicion** «Registro de ingreso aduanero consistente con el aporte» — El VPU demostró el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte a computar. · tramo [exacta]: «El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte que será computado como ingresado y liquidado en el mercado de cambios.»
- **c2 Condicion** «Documentación de capitalización definitiva o constancia de trámite» — El VPU presenta la documentación que avala la capitalización definitiva del aporte o, en su defecto, constancia del inicio del trámite de inscripción ante el Registro Público de Comercio y compromiso de presentar la documentación definitiva. · tramo [exacta]: «El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte.»
- **c3 Condicion** «Registro en RIOC con dos boletos sin movimiento de fondos» — Una entidad financiera registró el aporte de capital en el RIOC mediante dos boletos de cambio sin movimiento de fondos con las características de los puntos a), b) y c). · tramo [exacta]: «Una entidad financiera haya registrado al aporte de capital en el régimen informático de operaciones de cambio (RIOC) mediante la confección de dos boletos de cambio sin movimiento de fondos»
- **o1 Condicion** «Bienes no de capital hasta 10% del FOB — requisitos» — La operación puede incluir bienes que no son bienes de capital siempre que los que lo sean representen como mínimo el 90% del valor FOB total pagado. · umbral: ['representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado'] · tramo [exacta]: «La operación podrá incluir bienes que no revistan la condición de bien de capital en la medida que aquellos que lo sean representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado»
- **o2 Obligacion** «Contar con declaración jurada del cliente sobre bienes restantes» — La entidad debe contar con una declaración jurada del cliente que deje constancia de que los bienes restantes son repuestos, accesorios o materiales necesarios para los bienes de capital. · props: `{"tipo": "otra"}` · tramo [exacta]: «la entidad cuente con una declaración jurada del cliente en la cual deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios para el funcionamiento, construcción o instalación de los bienes de capital que se están adquiriendo»
- **o3 Obligacion** «Contar con certificación SEPAIMPO» — La entidad debe contar con la certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO). · props: `{"tipo": "otra"}` · tramo [exacta]: «La entidad deberá contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO).»
- **o4 Obligacion** «VPU presenta documentación de capitalización definitiva» — El VPU debe presentar la documentación que avale la capitalización definitiva del aporte. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte.»
- **o5 Obligacion** «VPU: constancia de trámite y compromiso en 365 días» — Si no dispone de la documentación de capitalización definitiva, el VPU debe presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio y comprometerse a presentar la documentación dentro de los 365 días corridos desde el inicio del trámite. · props: `{"tipo": "presentacion_informativa"}` · umbral: ['dentro de los 365 (trescientos sesenta y cinco) días corridos desde el inicio de…'] · tramo [exacta]: «En caso de no disponerla, deberá presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio de la decisión de capitalización definitiva de los aportes de capital computados de acuerdo con los requisitos legales correspondientes y comprometerse a presentar la documentación de la capi…»
- **o6 Obligacion** «Registrar boletos en fecha de ingreso aduanero» — Los dos boletos de cambio deben registrarse en la fecha del registro de ingreso aduanero de los bienes, sin importar cuándo el cliente solicite su registro. · props: `{"tipo": "otra"}` · tramo [exacta]: «Los boletos deberán ser registrados en la fecha en que se produjo el registro de ingreso aduanero de los bienes, independientemente de cuál sea el momento en que el cliente solicite su registro ante la entidad financiera.»
- **o7 Obligacion** «Boleto de compra con código de concepto del mecanismo» — El boleto de compra se confecciona con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo. · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de compra se confeccionará con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo.»
- **o8 Obligacion** «Asignar número APX a cargo de la entidad» — Si el VPU contempla aplicar cobros de exportaciones de bienes para la repatriación del aporte, la entidad debe asignar el número APX para el Seguimiento de anticipos y otras financiaciones de exportación de bienes, a cargo de la propia entidad. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «En caso de que el VPU contemple la posibilidad de aplicar cobros de exportaciones de bienes para la repatriación del aporte, la entidad deberá asignar el correspondiente número de identificación (número APX) para el "Seguimiento de anticipos y otras financiaciones de exportación de bienes", el cual quedará a cargo de l…»
- **o9 Obligacion** «Boleto de venta con código de pago diferido de bienes de capital» — El boleto de venta se confecciona con el código de concepto de pago diferido de importaciones de bienes de capital, dejando constancia de que el pago se enmarca en este mecanismo. · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta se confeccionará con el código de concepto de pago diferido de importaciones de bienes de capital, dejando constancia que el pago se enmarca en el presente mecanismo.»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: o1 Condicion —condicion_de→ op1 Operacion
- R: p1 Potestad —aplica_a→ Sujeto_vpu_rigi (mención «VPU»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o3 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: o4 Obligacion —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- R: o5 Obligacion —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- R: o8 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o6 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «entidad financiera»)
- R: o6 Obligacion —regula→ op1 Operacion
- R: o7 Obligacion —regula→ op1 Operacion
- R: o9 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —condiciona→ op1 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «El VPU haya demostrado el registro de ingreso aduanero del bien de capital» — El sujeto VPU no se vincula a la Condicion c1 con aplica_a (dominio no admite Condicion); se habría usado aplica_a.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «i) a iii) en la medida que» (i)) | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ p1 Potestad |
| 2 | «i) a iii) en la medida que» (ii)) | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ p1 Potestad |
| 3 | «i) a iii) en la medida que» (iii)) | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ p1 Potestad |
| 4 | «al menos 90 % del FOB» | `condicion_con_relacion` |  | o1 Condicion con el umbral —condicion_de→ op1 Operacion |
| 5 | «en caso de no disponer la documentación» | `dentro_de_norma` |  | dentro de la Obligacion o5 (tramo «En caso de no disponerla…»); sin Condicion |
| 6 | «VPU con cobros de exportaciones» | `dentro_de_norma` |  | dentro de la Obligacion o8 (tramo «En caso de que el VPU contemple…»); sin Condicion |

## `ext::2.1` — Cobros de exportaciones de bienes.

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
> *propio:* 2.1. Cobros de exportaciones de bienes. En las Secciones 7., 8. y 9. se detallan las normas asociadas a la operatoria de exportaciones de bienes, las disposiciones relacionadas al seguimiento de las negociaciones de divisas por exportaciones de bienes (SECOEXPO) y del seguimiento de anticipos y otras financiaciones de exportación de bienes, respectivamente.

### Extracción (código A)

(sin entidades ni omisiones)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:18 | no | «En las Secciones 7., 8. y 9. se detallan las normas asociadas a la operatoria de exportaciones de bienes, las disposiciones relacionadas al seguimiento de las n…» | `ausente` |  | ninguna entidad ni omisión cubre la oración |

## `ext::3.11.2::intro` — [bloque intro] Las entidades podrán dar acceso al mercado de cambios a los residentes que deban

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* 3.11. Otras compras de moneda extranjera por parte de residentes con aplicación específica.
> *heredado:* 3.11.2. Las entidades podrán dar acceso al mercado de cambios a los residentes que deban
> *propio:* realizar pagos de servicios de deudas financieras comprendidas en el punto 3.5. o de títulos valores con acceso al mercado de cambios en función de lo dispuesto en los puntos 3.6.1.3. a 3.6.1.5., para la compra de moneda extranjera con anterioridad al plazo admitido por la normativa para cada caso, en las siguientes condiciones:

### Extracción (código A)

- **p1 Potestad** «Acceso anticipado al mercado de cambios para pago de deudas» — Las entidades pueden dar acceso al mercado de cambios a residentes que deban pagar servicios de deudas financieras (punto 3.5.) o de títulos valores (puntos 3.6.1.3. a 3.6.1.5.), para comprar moneda extranjera con anterioridad al plazo admitido por la normativa en cada caso, en las condiciones que siguen. · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a los residentes que deban realizar pagos de servicios de deudas financieras comprendidas en el punto 3.5. o de títulos valores con acceso al mercado de cambios en función de lo dispuesto en los puntos 3.6.1.3. a 3.6.1.5., para la compra de moneda extranjera con ant…»
- **o1 Operacion** «Compra anticipada de moneda extranjera para pago de deudas» — Compra de moneda extranjera por residentes, con anterioridad al plazo admitido por la normativa para cada caso, para pagar servicios de deudas financieras comprendidas en el punto 3.5. o de títulos valores con acceso al mercado de cambios según los puntos 3.6.1.3. a 3.6.1.5. · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «para la compra de moneda extranjera con anterioridad al plazo admitido por la normativa para cada caso»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:20 | sí | «en las siguientes condiciones:» | `extraida_tramo_verificado` |  | p1 Potestad [exacta], tramo que contiene «en las siguientes condiciones:» |

## `ext::3.16.3.6` — En las declaraciones juradas elaboradas para dar cumplimiento a los

Grupos: grupo_c.

### Texto

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.16. Requisitos complementarios para los egresos por el mercado de cambios.
> *heredado:* 3.16.3. Declaración jurada de clientes que no sean personas humanas residentes respecto a
> *heredado:* operaciones con títulos valores y otros activos. En el caso de que el cliente no sea una persona humana residente, la entidad deberá contar con la conformidad previa del BCRA excepto que cuente con una declaración jurada del cliente en la que deje constancia de que:
> *heredado:* En caso de que el cliente sea una persona jurídica, para que la operación no quede comprendida por el requisito de conformidad previa, la entidad deberá contar adicionalmente con una declaración jurada en la que conste:
> *propio:* 3.16.3.6. En las declaraciones juradas elaboradas para dar cumplimiento a los puntos 3.16.3.1. y 3.16.3.2. no deberán tenerse en cuenta: i) las transferencias de títulos valores a entidades depositarias del exterior realizadas o a realizar por el cliente con el objeto de participar de un canje o una operación de recompra de títulos de deuda emitidos por el Gobierno Nacional, gobiernos locales u otros emisores residentes del sector privado. El cliente deberá comprometerse a presentar la correspondiente certificación por los títulos de deuda canjeados. ii) la entrega de activos locales con el objeto de cancelar una deuda con una agencia oficial de crédito o una entidad financiera del exterior, en la medida que se produzca a partir del vencimiento como consecuencia de una cláusula de garantía prevista en el contrato de endeudamiento. iii) las ventas de títulos valores con liquidación en moneda extranjera en el país o en el exterior cuando la totalidad de los fondos obtenidos de tales liquidaciones se haya utilizado o será utilizada dentro de los 10 (diez) días corridos a las siguientes operaciones: a) Pagos a partir del vencimiento de capital o intereses de nuevos endeudamientos financieros comprendidos en el punto 3.5., desembolsados a partir del 02/10/23 y que contemplen como mínimo 1 (un) año de gracia para el pago de capital. b) Repatriaciones del capital y rentas asociadas a las inversiones directas de no residentes recibidas a partir del 02/10/23, en la medida que la repatriación se produzca como mínimo 1 (un) año después de la concreción del aporte de capital y se haya dado cumplimiento a los mecanismos legales previstos en tales casos. c) Pagos a partir del vencimiento de capital o intereses de títulos de deuda emitidos a partir del 02/10/23 con registro público en el país no comprendidos en el punto 3.5., denominados y suscriptos en moneda extranjera, con servicios pagaderos en moneda extranjera y que contemplen como mínimo 2 (dos) años de gracia para el pago de capital. d) Pagos a partir del vencimiento de capital o intereses de endeudamientos financieros comprendidos en el punto 3.5. que no generen desembolsos por ser refinanciaciones de capital y/o intereses de operaciones contempladas en los incisos a) y c) precedentes, en la medida que las refinanciaciones no anticipen el vencimiento de la deuda original. e) Pagos a partir del vencimiento de capital o intereses de títulos de emitidos con registro público en el país no comprendidos en el punto 3.5., denominados en moneda extranjera, con servicios pagaderos en moneda extranjera y que no generen desembolsos por ser refinanciaciones de capital y/o intereses de operaciones contempladas en el inciso c) precedente en la medida que las refinanciaciones no anticipen el vencimiento de la deuda original. En todos los casos el cliente deberá presentar una declaración jurada dejando constancia de que los fondos oportunamente recibidos por las operaciones detalladas en los incisos a) a c) precedentes se utilizaron en su totalidad para concretar pagos en el país relacionados con la concreción de inversiones en la República Argentina. iv) las ventas con liquidación en moneda extranjera en el país o en el exterior de los Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) o las transferencias de estos bonos a depositarios en el exterior, cuando sean realizados por hasta el monto adquirido en la suscripción primaria por aquellos que participaron en dicha instancia. v) las ventas con liquidación en moneda extranjera en el exterior o las transferencias a depositarios del exterior que concreten los importadores de bienes y servicios que hayan adquirido en una suscripción primaria Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por deudas de importaciones de bienes y servicios elegibles en los puntos 4.4. y 4.5., cuando el valor de mercado de estas operaciones no supere a la diferencia entre el valor obtenido por la venta con liquidación en moneda extranjera en el exterior de bonos BOPREAL adquiridos en las suscripciones primarias citadas y su valor nominal, si el primero resultase menor.

### Extracción (código A)

- **x1 Excepcion** «Exclusión transferencias para canje o recompra de títulos de deuda» — En las declaraciones juradas de los puntos 3.16.3.1 y 3.16.3.2 no se tienen en cuenta las transferencias de títulos valores a entidades depositarias del exterior realizadas o a realizar por el cliente para participar de un canje o recompra de títulos de deuda emitidos por el Gobierno Nacional, gobiernos locales u otros emisores residentes del sector privado. Exceptúa la norma de las declaraciones … · tramo [exacta]: «no deberán tenerse en cuenta: i) las transferencias de títulos valores a entidades depositarias del exterior realizadas o a realizar por el cliente con el objeto de participar de un canje o una operación de recompra de títulos de deuda emitidos por el Gobierno Nacional, gobiernos locales u otros emisores residentes del…»
- **o1 Obligacion** «Compromiso de presentar certificación de títulos canjeados» — El cliente debe comprometerse a presentar la certificación correspondiente por los títulos de deuda canjeados (en el supuesto del inciso i). · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «El cliente deberá comprometerse a presentar la correspondiente certificación por los títulos de deuda canjeados.»
- **x2 Excepcion** «Exclusión entrega de activos locales por cláusula de garantía» — En las declaraciones juradas de los puntos 3.16.3.1 y 3.16.3.2 no se tiene en cuenta la entrega de activos locales para cancelar una deuda con una agencia oficial de crédito o una entidad financiera del exterior, en la medida que se produzca a partir del vencimiento como consecuencia de una cláusula de garantía prevista en el contrato de endeudamiento. Exceptúa la norma de las declaraciones jurada… · tramo [exacta]: «ii) la entrega de activos locales con el objeto de cancelar una deuda con una agencia oficial de crédito o una entidad financiera del exterior, en la medida que se produzca a partir del vencimiento como consecuencia de una cláusula de garantía prevista en el contrato de endeudamiento.»
- **x3 Excepcion** «Exclusión ventas de títulos con fondos aplicados a pagos de deuda o repatriaciones» — En las declaraciones juradas de los puntos 3.16.3.1 y 3.16.3.2 no se tienen en cuenta las ventas de títulos valores con liquidación en moneda extranjera en el país o en el exterior cuando la totalidad de los fondos se haya utilizado o será utilizada dentro de los 10 días corridos a las operaciones de los incisos a) a e). Exceptúa la norma de las declaraciones juradas de los puntos 3.16.3.1 y 3.16.… · umbral: ['dentro de los 10 (diez) días corridos'] · tramo [exacta]: «iii) las ventas de títulos valores con liquidación en moneda extranjera en el país o en el exterior cuando la totalidad de los fondos obtenidos de tales liquidaciones se haya utilizado o será utilizada dentro de los 10 (diez) días corridos a las siguientes operaciones:»
- **c0 Condicion** «Totalidad de fondos usados dentro de 10 días corridos» — La totalidad de los fondos obtenidos de la liquidación se utilizó o se utilizará dentro de los 10 días corridos en alguna de las operaciones de los incisos a) a e). · umbral: ['dentro de los 10 (diez) días corridos'] · tramo [exacta]: «cuando la totalidad de los fondos obtenidos de tales liquidaciones se haya utilizado o será utilizada dentro de los 10 (diez) días corridos a las siguientes operaciones»
- **ca Condicion** «Pagos de endeudamientos financieros nuevos con 1 año de gracia (inc. a)» — Destino de los fondos: pagos a partir del vencimiento de capital o intereses de nuevos endeudamientos financieros del punto 3.5., desembolsados desde el 02/10/23, con al menos 1 año de gracia para el capital. · umbral: ['como mínimo 1 (un) año de gracia para el pago de capital'] · tramo [exacta]: «a) Pagos a partir del vencimiento de capital o intereses de nuevos endeudamientos financieros comprendidos en el punto 3.5., desembolsados a partir del 02/10/23 y que contemplen como mínimo 1 (un) año de gracia para el pago de capital.»
- **cb Condicion** «Repatriaciones de inversiones directas con 1 año mínimo (inc. b)» — Destino de los fondos: repatriaciones del capital y rentas de inversiones directas de no residentes recibidas desde el 02/10/23, siempre que se produzcan al menos 1 año después del aporte y se hayan cumplido los mecanismos legales. · umbral: ['como mínimo 1 (un) año después de la concreción del aporte de capital'] · tramo [exacta]: «b) Repatriaciones del capital y rentas asociadas a las inversiones directas de no residentes recibidas a partir del 02/10/23, en la medida que la repatriación se produzca como mínimo 1 (un) año después de la concreción del aporte de capital y se haya dado cumplimiento a los mecanismos legales previstos en tales casos.»
- **cc Condicion** «Pagos de títulos de deuda con 2 años de gracia (inc. c)» — Destino de los fondos: pagos a partir del vencimiento de capital o intereses de títulos de deuda emitidos desde el 02/10/23 con registro público en el país no comprendidos en el punto 3.5., en moneda extranjera, con servicios pagaderos en moneda extranjera y al menos 2 años de gracia para el capital. · umbral: ['como mínimo 2 (dos) años de gracia para el pago de capital'] · tramo [exacta]: «c) Pagos a partir del vencimiento de capital o intereses de títulos de deuda emitidos a partir del 02/10/23 con registro público en el país no comprendidos en el punto 3.5., denominados y suscriptos en moneda extranjera, con servicios pagaderos en moneda extranjera y que contemplen como mínimo 2 (dos) años de gracia pa…»
- **cd Condicion** «Pagos de refinanciaciones de endeudamientos (inc. d)» — Destino de los fondos: pagos de endeudamientos financieros del punto 3.5. que no generan desembolsos por ser refinanciaciones de operaciones de los incisos a) y c), siempre que no anticipen el vencimiento de la deuda original. · tramo [exacta]: «d) Pagos a partir del vencimiento de capital o intereses de endeudamientos financieros comprendidos en el punto 3.5. que no generen desembolsos por ser refinanciaciones de capital y/o intereses de operaciones contempladas en los incisos a) y c) precedentes, en la medida que las refinanciaciones no anticipen el vencimie…»
- **ce Condicion** «Pagos de refinanciaciones de títulos de deuda (inc. e)» — Destino de los fondos: pagos de títulos emitidos con registro público en el país no comprendidos en el punto 3.5., en moneda extranjera con servicios pagaderos en moneda extranjera, que no generan desembolsos por ser refinanciaciones de operaciones del inciso c), siempre que no anticipen el vencimiento de la deuda original. · tramo [exacta]: «e) Pagos a partir del vencimiento de capital o intereses de títulos de emitidos con registro público en el país no comprendidos en el punto 3.5., denominados en moneda extranjera, con servicios pagaderos en moneda extranjera y que no generen desembolsos por ser refinanciaciones de capital y/o intereses de operaciones c…»
- **o2 Obligacion** «DDJJ sobre uso de fondos en inversiones en Argentina» — En los casos del inciso iii), el cliente debe presentar una declaración jurada que deje constancia de que los fondos recibidos por las operaciones de los incisos a) a c) se utilizaron en su totalidad para pagos en el país relacionados con inversiones en la República Argentina. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «En todos los casos el cliente deberá presentar una declaración jurada dejando constancia de que los fondos oportunamente recibidos por las operaciones detalladas en los incisos a) a c) precedentes se utilizaron en su totalidad para concretar pagos en el país relacionados con la concreción de inversiones en la República…»
- **x4 Excepcion** «Exclusión ventas o transferencias de BOPREAL hasta monto de suscripción primaria» — En las declaraciones juradas de los puntos 3.16.3.1 y 3.16.3.2 no se tienen en cuenta las ventas con liquidación en moneda extranjera de BOPREAL o sus transferencias a depositarios del exterior, hasta el monto adquirido en la suscripción primaria por quienes participaron en ella. Exceptúa la norma de las declaraciones juradas de los puntos 3.16.3.1 y 3.16.3.2 (otra unidad). · tramo [exacta]: «iv) las ventas con liquidación en moneda extranjera en el país o en el exterior de los Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) o las transferencias de estos bonos a depositarios en el exterior, cuando sean realizados por hasta el monto adquirido en la suscripción primaria por aquellos que particip…»
- **c4 Condicion** «Operación hasta monto adquirido en suscripción primaria BOPREAL» — Las ventas o transferencias de BOPREAL se realizan por hasta el monto adquirido en la suscripción primaria por quienes participaron en ella. · props: `{"umbrales": [{"tramo": "por hasta el monto adquirido en la suscripción primaria", "comparacion": "maximo_inclusivo", "base": "monto adquirido en la suscripción primaria", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto adquirido en la suscripción primaria'] · tramo [exacta]: «cuando sean realizados por hasta el monto adquirido en la suscripción primaria por aquellos que participaron en dicha instancia»
- **x5 Excepcion** «Exclusión ventas o transferencias de importadores con BOPREAL» — En las declaraciones juradas de los puntos 3.16.3.1 y 3.16.3.2 no se tienen en cuenta las ventas con liquidación en moneda extranjera en el exterior o las transferencias a depositarios del exterior de los importadores de bienes y servicios que adquirieron BOPREAL en suscripción primaria por deudas de importaciones elegibles en los puntos 4.4 y 4.5. Exceptúa la norma de las declaraciones juradas de… · tramo [exacta]: «v) las ventas con liquidación en moneda extranjera en el exterior o las transferencias a depositarios del exterior que concreten los importadores de bienes y servicios que hayan adquirido en una suscripción primaria Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por deudas de importaciones de bienes y se…»
- **c5 Condicion** «Valor de mercado no supera diferencia con valor nominal» — El valor de mercado de las operaciones no supera la diferencia entre el valor obtenido por la venta en el exterior de los BOPREAL adquiridos en suscripción primaria y su valor nominal, si el primero resultase menor. · props: `{"umbrales": [{"tramo": "no supere a la diferencia entre el valor obtenido por la venta con liquidación en moneda extranjera en el exterior de bonos BOPREAL adquiridos en las suscripciones primarias citadas y su valor nominal", "comparacion": "maximo_inclusivo", "base": "diferencia entre el valor obtenido por la venta con liquidación en moneda extranjera en el exterior de bonos BOPREAL adquiridos", "regla_comparacion": "limite_relativo:negacion:raiz_super", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['no supere a la diferencia entre el valor obtenido por la venta con liquidación e…'] · tramo [exacta]: «cuando el valor de mercado de estas operaciones no supere a la diferencia entre el valor obtenido por la venta con liquidación en moneda extranjera en el exterior de bonos BOPREAL adquiridos en las suscripciones primarias citadas y su valor nominal, si el primero resultase menor»
- R: c0 Condicion —condicion_de→ x3 Excepcion
- R: ca Condicion —condicion_de→ x3 Excepcion
- R: cb Condicion —condicion_de→ x3 Excepcion
- R: cc Condicion —condicion_de→ x3 Excepcion
- R: cd Condicion —condicion_de→ x3 Excepcion
- R: ce Condicion —condicion_de→ x3 Excepcion
- R: c4 Condicion —condicion_de→ x4 Excepcion
- R: c5 Condicion —condicion_de→ x5 Excepcion
- R: o1 Obligacion —aplica_a→ Sujeto_cliente (mención «El cliente»)
- R: o2 Obligacion —aplica_a→ Sujeto_cliente (mención «el cliente»)

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «garantía desde el vencimiento» | `dentro_de_norma` |  | dentro de la Excepcion x2 (tramo «en la medida que se produzca a partir del vencimiento…»); sin Condicion propia |
| 2 | «fondos usados en 10 días» | `condicion_con_relacion` |  | c0 Condicion con el umbral —condicion_de→ x3 Excepcion (la exclusión iii) |
| 3 | «repatriación a 1 año» | `condicion_con_relacion` |  | cb Condicion con el umbral —condicion_de→ x3 Excepcion |
| 4 | «BOPREAL hasta el monto suscripto» | `condicion_con_relacion` |  | c4 Condicion con el umbral —condicion_de→ x4 Excepcion |
| 5 | «valor de mercado que no supere la diferencia» | `condicion_con_relacion` |  | c5 Condicion con el umbral —condicion_de→ x5 Excepcion |

## `ext::3.9::intro` — [bloque intro] Compra de moneda extranjera por parte de personas humanas residentes para la formación

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* 3.9. Compra de moneda extranjera por parte de personas humanas residentes para la formación
> *propio:* de activos externos bajo otras modalidades, la remisión de ayuda familiar u operaciones con derivados. Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de concepto A05) en la medida que no encuadre en el punto 3.12.1., sin la conformidad previa del BCRA, en la medida que se cumplan la totalidad de los siguientes requisitos:

### Extracción (código A)

- **op1 Operacion** «Acceso al mercado de cambios para formación de activos externos y otros conceptos» — Acceso al mercado de cambios de personas humanas residentes para la formación de activos externos (códigos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y la operatoria con derivados (código A05), en la medida que no encuadre en el punto 3.12.1. · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de concepto A05)»
- **p1 Potestad** «Dar acceso al mercado de cambios sin conformidad previa del BCRA» — Las entidades pueden dar acceso al mercado de cambios a personas humanas residentes para la formación de activos externos, la remisión de ayuda familiar y la operatoria con derivados (código A05), en la medida que no encuadre en el punto 3.12.1., sin la conformidad previa del BCRA. · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de concepto A05) en la medida que no encuadre en el punto…»
- **c1 Condicion** «Cumplimiento de la totalidad de los requisitos siguientes» — Se exige el cumplimiento conjunto de la totalidad de los requisitos enumerados en los ítems siguientes para dar acceso sin conformidad previa del BCRA. · tramo [exacta]: «en la medida que se cumplan la totalidad de los siguientes requisitos»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)
- Omisión `relacion_sin_predicado` [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos» — Potestad → Operacion: se habría usado un predicado de habilitación sobre el acto; no existe en los 13 predicados.

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:18 | no | «de activos externos bajo otras modalidades, la remisión de ayuda familiar u operaciones con derivados.» | `ausente` |  | ningún tramo cubre el fragmento del título; op1 y p1 cubren la oración del cuerpo (coincidencia de palabras) |

## `ext::4.1.3.1` — Cuando el emisor de la tarjeta sea una entidad financiera, el titular podrá

Grupos: grupo_c.

### Texto

> *heredado:* Sección 4. Otras disposiciones específicas.
> *heredado:* 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tarjetas de
> *heredado:* crédito, compra y prepagas emitidas en el país.
> *heredado:* 4.1.3. Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o
> *heredado:* de compra.
> *propio:* 4.1.3.1. Cuando el emisor de la tarjeta sea una entidad financiera, el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos, debiendo aplicar como máximo en este caso el tipo de cambio vendedor (aplicable para operaciones efectuadas por ventanilla o a través de medios electrónicos, según corresponda) de la entidad emisora de la tarjeta del momento de cancelación –o día hábil inmediato anterior cuando el pago se efectúe un día inhábil–. En los casos donde los clientes hayan pactado el débito automático del resumen de la tarjeta en cuentas de la propia entidad emisora, aplicará el tipo de cambio vendedor para operaciones efectuadas a través de medios electrónicos de pago del cierre del mismo día hábil del pago.

### Extracción (código A)

- **op1 Operacion** «Cancelación de consumos en moneda extranjera con tarjeta» — Cancelación por el titular de consumos en moneda extranjera realizados con tarjeta de crédito y/o compra emitida por una entidad financiera, en moneda extranjera o en pesos. · props: `{"tipo": "cancelacion_de_consumos"}` · tramo [exacta]: «cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- **pot1 Potestad** «Cancelar consumos en moneda extranjera o en pesos» — El titular de la tarjeta puede cancelar los consumos realizados en moneda extranjera en esa moneda o en pesos, cuando el emisor es una entidad financiera. · tramo [exacta]: «el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- **cond1 Condicion** «Emisor de la tarjeta es entidad financiera» — Supuesto: el emisor de la tarjeta es una entidad financiera. · tramo [exacta]: «Cuando el emisor de la tarjeta sea una entidad financiera»
- **res1 Restriccion** «Tope tipo de cambio vendedor — cancelación en pesos» — En la cancelación en pesos de consumos en moneda extranjera se aplica como máximo el tipo de cambio vendedor (ventanilla o medios electrónicos, según corresponda) de la entidad emisora del momento de cancelación, o del día hábil inmediato anterior si el pago se efectúa un día inhábil. · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "aplicar como máximo en este caso el tipo de cambio vendedor", "comparacion": "maximo_inclusivo", "base": "en este caso el tipo de cambio vendedor", "regla_comparacion": "limite_relativo:compuesta:como_maximo", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['aplicar como máximo en este caso el tipo de cambio vendedor'] · tramo [exacta]: «debiendo aplicar como máximo en este caso el tipo de cambio vendedor (aplicable para operaciones efectuadas por ventanilla o a través de medios electrónicos, según corresponda) de la entidad emisora de la tarjeta del momento de cancelación –o día hábil inmediato anterior cuando el pago se efectúe un día inhábil–»
- **res2 Restriccion** «Tipo de cambio vendedor medios electrónicos — débito automático» — Cuando los clientes pactaron el débito automático del resumen en cuentas de la propia entidad emisora, se aplica el tipo de cambio vendedor para operaciones por medios electrónicos de pago del cierre del mismo día hábil del pago. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «En los casos donde los clientes hayan pactado el débito automático del resumen de la tarjeta en cuentas de la propia entidad emisora, aplicará el tipo de cambio vendedor para operaciones efectuadas a través de medios electrónicos de pago del cierre del mismo día hábil del pago.»
- **cond2 Condicion** «Débito automático pactado en cuenta de la entidad emisora» — Supuesto: los clientes pactaron el débito automático del resumen de la tarjeta en cuentas de la propia entidad emisora. · tramo [exacta]: «En los casos donde los clientes hayan pactado el débito automático del resumen de la tarjeta en cuentas de la propia entidad emisora»
- R: pot1 Potestad —aplica_a→ Sujeto (mención «el titular»)
- R: cond1 Condicion —condicion_de→ pot1 Potestad
- R: cond1 Condicion —condicion_de→ op1 Operacion
- R: res1 Restriccion —limita→ op1 Operacion
- R: res2 Restriccion —limita→ op1 Operacion
- R: cond2 Condicion —condicion_de→ res2 Restriccion
- R: res2 Restriccion —aplica_a→ Sujeto_cliente (mención «los clientes»)

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «emisor entidad financiera» | `condicion_con_relacion` |  | cond1 Condicion —condicion_de→ pot1 Potestad (y → op1) |
| 2 | «pago en día inhábil» | `dentro_de_norma` |  | dentro de la Restriccion res1 (tramo «o día hábil inmediato anterior cuando el pago se efectúe un día inhábil»); sin Condicion |
| 3 | «débito automático pactado» | `condicion_con_relacion` |  | cond2 Condicion —condicion_de→ res2 Restriccion |

## `ext::4.1.3.2` — Cuando se trate de empresas no financieras emisoras de tarjetas de crédito

Grupos: grupo_c.

### Texto

> *heredado:* Sección 4. Otras disposiciones específicas.
> *heredado:* 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tarjetas de
> *heredado:* crédito, compra y prepagas emitidas en el país.
> *heredado:* 4.1.3. Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o
> *heredado:* de compra.
> *propio:* 4.1.3.2. Cuando se trate de empresas no financieras emisoras de tarjetas de crédito y/o compra, el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos –siendo aplicable el tipo de cambio vendedor por canales electrónicos publicado por el Banco de la Nación Argentina el mismo día hábil de la fecha de pago o hábil inmediato anterior cuando el pago se efectúe un día inhábil–.

### Extracción (código A)

- **op1 Operacion** «Cancelación de consumos en moneda extranjera con tarjeta (empresas no financieras emisoras)» — Cancelación por el titular de los consumos realizados en moneda extranjera con tarjetas de crédito y/o compra emitidas por empresas no financieras, en moneda extranjera o en pesos; en pesos se aplica el tipo de cambio vendedor por canales electrónicos publicado por el Banco de la Nación Argentina el mismo día hábil de la fecha de pago, o el hábil inmediato anterior cuando el pago se efectúe un día… · props: `{"tipo": "cancelacion_consumos_tarjeta"}` · tramo [exacta]: «cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- **p1 Potestad** «Titular puede cancelar en moneda extranjera o en pesos» — Cuando se trate de empresas no financieras emisoras de tarjetas de crédito y/o compra, el titular puede cancelar los consumos en moneda extranjera en esa moneda o en pesos, aplicándose en este caso el tipo de cambio vendedor por canales electrónicos del Banco de la Nación Argentina del día hábil de la fecha de pago (o hábil inmediato anterior si el pago es en día inhábil). · tramo [exacta]: «Cuando se trate de empresas no financieras emisoras de tarjetas de crédito y/o compra, el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- R: p1 Potestad —aplica_a→ Sujeto (mención «el titular»)
- R: Sujeto (mención «el titular») —ejecuta→ op1 Operacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «emisoras no financieras» | `dentro_de_norma` |  | dentro de la Potestad p1 (tramo «Cuando se trate de empresas no financieras emisoras…»); sin Condicion |
| 2 | «pago en día inhábil» | `dentro_de_norma` |  | dentro de la Potestad p1 y de la Operacion op1 (descripción); sin Condicion |

## `ext::5.8.2.2` — Las transferencias tengan como ordenante la empresa del exterior firmante

Grupos: omisiones.

### Texto

> *heredado:* Sección 5. Pautas operativas.
> *heredado:* 5.8. Boletos globales diarios.
> *heredado:* Las entidades podrán elaborar un boleto global diario para las situaciones que se detallan a continuación, en la medida que se verifiquen todas las condiciones indicadas en cada caso. En todos los casos, se deberá requerir una lista detallada de los beneficiarios/ordenantes de los pagos comprendidos en dicho boleto, debiendo como mínimo informar respecto de ellos: nombres y apellidos completos o denominación social (según corresponda), CUIT, CUIL o CDI y el monto que le corresponde.
> *heredado:* 5.8.2. Ingresos de divisas a través de empresas procesadores de pagos.
> *heredado:* A nombre de la empresa local que actúa como representante en el país de la empresa procesadora de pagos en la medida que se cumplan las siguientes condiciones:
> *heredado:* Por los ingresos cursados que correspondan al cobro de exportaciones de bienes y servicios, la entidad receptora de la transferencia emitirá, a pedido del exportador, una certificación de ingreso y liquidación de divisas por los fondos recibidos en moneda local.
> *propio:* 5.8.2.2. Las transferencias tengan como ordenante la empresa del exterior firmante del acuerdo y se canalicen a través de una entidad financiera del exterior cuya casa matriz o controlante se encuentre radicada en un país miembro del Comité de Supervisión Bancaria de Basilea.

### Extracción (código A)

- **c1 Condicion** «Ordenante empresa del exterior vía entidad de país Basilea» — Supuesto para el boleto global diario de ingresos de divisas a través de empresas procesadoras de pagos (punto 5.8.2): las transferencias tienen como ordenante la empresa del exterior firmante del acuerdo y se canalizan a través de una entidad financiera del exterior cuya casa matriz o controlante está radicada en un país miembro del Comité de Supervisión Bancaria de Basilea. · tramo [exacta]: «Las transferencias tengan como ordenante la empresa del exterior firmante del acuerdo y se canalicen a través de una entidad financiera del exterior cuya casa matriz o controlante se encuentre radicada en un país miembro del Comité de Supervisión Bancaria de Basilea.»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:6 | sí | «5.8.2.2. Las transferencias tengan como ordenante la empresa del exterior firmante del acuerdo y se canalicen a través de una entidad financiera del exterior cu…» | `extraida_tramo_verificado` |  | c1 Condicion [exacta], tramo que cubre la oración (0,88, sin el número de punto) |

## `ext::7.1.1.5` — 365 (trescientos sesenta y cinco) días corridos para las operaciones que se

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.1. Obligación de ingreso y liquidación en los plazos establecidos.
> *heredado:* 7.1.1. Exportaciones oficializadas a partir del 02/09/19.
> *heredado:* El contravalor en divisas de la exportación hasta alcanzar el valor facturado según la condición de venta pactada deberá ingresarse al país y liquidarse en el mercado de cambios. En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicios resultará aplicable lo dispuesto en los puntos 14.1.1. y 14.1.2., según corresponda. El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse en los siguientes plazos a computar desde la fecha del cumplido de embarque otorgado por la Aduana:
> *heredado:* Independientemente de los plazos máximos precedentes, los cobros de exportaciones deberán ser ingresados y liquidados en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro. La posibilidad de utilizar este plazo quedará supeditada en todos los casos al cumplimiento de los plazos previstos en los puntos 7.1.1.1. a 7.1.1.5. Los montos en moneda extranjera originados en cobros de siniestros por coberturas contratadas, en la medida que los mismos cubran el valor de los bienes exportados, están alcanzados por esta obligación. El exportador deberá seleccionar una entidad para que realice el "Seguimiento de las negociaciones de divisas por exportaciones de bienes". La obligación de ingreso y liquidación de divisas de un permiso de embarque se considerará cumplida cuando la entidad haya certificado tal situación por los mecanismos establecidos a tal efecto.
> *propio:* 7.1.1.5. 365 (trescientos sesenta y cinco) días corridos para las operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE", independientemente del tipo de bien exportado.

### Extracción (código A)

- **op1 Operacion** «Ingreso y liquidación de divisas — EXPORTA SIMPLE» — Ingreso al país y liquidación en el mercado de cambios del contravalor en divisas de exportaciones de bienes concretadas en el marco del régimen EXPORTA SIMPLE, independientemente del tipo de bien exportado · props: `{"tipo": "otra"}` · tramo [exacta]: «El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse»
- **ob1 Obligacion** «Plazo 365 días corridos — EXPORTA SIMPLE» — El ingreso y liquidación de las divisas por el mercado de cambios debe concretarse dentro de 365 días corridos, a computar desde la fecha del cumplido de embarque otorgado por la Aduana, para las operaciones concretadas en el marco del régimen EXPORTA SIMPLE, independientemente del tipo de bien exportado · props: `{"tipo": "otra"}` · umbral: ['365 (trescientos sesenta y cinco) días corridos'] · tramo [exacta]: «El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse en los siguientes plazos a computar desde la fecha del cumplido de embarque otorgado por la Aduana: […] 365 (trescientos sesenta y cinco) días corridos para las operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE", ind…»
- R: ob1 Obligacion —regula→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:10 | sí | «independientemente del tipo de bien exportado» | `extraida_tramo_verificado` |  | Obligacion (ob1/e1) [exacta], tramo que contiene «independientemente del tipo de bien exportado» |

## `ext::7.1.3` — Anticipos, prefinanciaciones y posfinanciaciones del exterior.

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.1. Obligación de ingreso y liquidación en los plazos establecidos.
> *propio:* 7.1.3. Anticipos, prefinanciaciones y posfinanciaciones del exterior. Los anticipos, prefinanciaciones y posfinanciaciones del exterior deberán ser ingresadas y liquidadas en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el exterior. En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicios, resultará aplicable lo dispuesto en el punto 14.1.4.

### Extracción (código A)

- **op1 Operacion** «Ingreso y liquidación de anticipos, prefinanciaciones y posfinanciaciones del exterior» — Ingreso y liquidación en el mercado de cambios de anticipos, prefinanciaciones y posfinanciaciones del exterior, contada desde la fecha de cobro o desembolso en el exterior. · props: `{"tipo": "ingreso y liquidación de divisas"}` · tramo [exacta]: «Los anticipos, prefinanciaciones y posfinanciaciones del exterior deberán ser ingresadas y liquidadas en el mercado de cambios»
- **ob1 Obligacion** «Ingreso y liquidación en 20 días hábiles» — Los anticipos, prefinanciaciones y posfinanciaciones del exterior deben ser ingresados y liquidados en el mercado de cambios dentro de los 20 días hábiles de la fecha de cobro o desembolso en el exterior. · props: `{"tipo": "otra"}` · umbral: ['dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el e…'] · tramo [exacta]: «deberán ser ingresadas y liquidadas en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el exterior»
- **cond1 Condicion** «Cliente VPU adherido al RIGI con declaración de uso de beneficios» — Supuesto en que el cliente es un VPU adherido al RIGI que declaró ante la Autoridad de Aplicación que preveía usar los beneficios del art. 198 de la Ley 27.742 en materia de cobro de exportaciones; en ese caso resulta aplicable lo dispuesto en el punto 14.1.4 en lugar del plazo general del punto 7.1.3. · tramo [exacta]: «En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servici…»
- **ley1 Comunicacion** «Ley 27.742» —  · props: `{"codigo": "Ley 27.742", "tipo": "externa"}` · tramo [exacta]: «Ley 27.742»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: to TextoOrdenado —referencia→ ley1 Comunicacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:9 | sí (remisión pura) | «resultará aplicable lo dispuesto en el punto 14.1.4» | `ausente` |  | ninguna entidad ni omisión cubre «resultará aplicable lo dispuesto en el punto 14.1.4» |

## `ext::7.2.2` — Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación.

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.2. Liquidaciones y otros ingresos imputables al cumplimiento de un permiso de embarque.
> *propio:* 7.2.2. Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación. Cuando los exportadores anticipen fondos desde sus cuentas en el exterior a los fines de dar cumplimiento a la obligación de liquidación de exportaciones realizadas y pendientes de cobro.

### Extracción (código A)

- **op1 Operacion** «Ingreso de fondos propios de exportadores desde cuentas en el exterior» — Anticipo de fondos propios por los exportadores desde sus cuentas en el exterior, a los fines de dar cumplimiento a la obligación de liquidación de exportaciones realizadas y pendientes de cobro; ingreso imputable al cumplimiento de un permiso de embarque. · props: `{"tipo": "ingreso de fondos"}` · tramo [exacta]: «Cuando los exportadores anticipen fondos desde sus cuentas en el exterior a los fines de dar cumplimiento a la obligación de liquidación de exportaciones realizadas y pendientes de cobro.»
- R: Sujeto_exportador (mención «los exportadores») —ejecuta→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:15 | no | «7.2.2. Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación.» | `ausente` |  | ningún tramo cubre el título «Ingresos de fondos propios…»; op1 tiene como tramo la oración siguiente |

## `ext::7.5.3` — Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.5. Ampliaciones del plazo para el ingreso y liquidación de divisas.
> *heredado:* La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias:
> *propio:* 7.5.3. Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los endeudamientos financieros referidas en los puntos 7.3.5., 7.9. y 7.11. y las prefinanciaciones de exportaciones comprendidas en el punto 7.8.5. En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento del plazo para la liquidación de divisas del permiso, el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha. Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario.

### Extracción (código A)

- **op1 Operacion** «Ampliación plazo liquidación de divisas — fondos retenidos» — Ampliación del plazo para la liquidación de divisas de permisos cuyos fondos están retenidos en cuentas asociadas a endeudamientos financieros (puntos 7.3.5., 7.9. y 7.11.) y prefinanciaciones de exportaciones (punto 7.8.5.), hasta el quinto día hábil posterior a la fecha hasta la cual los cobros deben permanecer depositados según el contrato de financiamiento. · props: `{"tipo": "ampliacion_plazo_liquidacion"}` · tramo [exacta]: «el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha»
- **pot1 Potestad** «Exportador puede solicitar ampliación hasta 5.º día hábil» — El exportador puede solicitar que el plazo para la liquidación de divisas del permiso sea ampliado hasta el quinto día hábil posterior a la fecha hasta la cual los cobros deben permanecer depositados en virtud del contrato de financiamiento. · tramo [exacta]: «el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha»
- **pot2 Potestad** «Entidad concede extensión — fondos retenidos en cuentas asociadas» — La entidad encargada del seguimiento del permiso puede conceder extensiones en el plazo de ingreso y liquidación para permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los endeudamientos financieros referidos en los puntos 7.3.5., 7.9. y 7.11. y a las prefinanciaciones de exportaciones comprendidas en el punto 7.8.5. · tramo [exacta]: «La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias: [...] Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los»
- **cond1 Condicion** «Fecha de depósito exigida posterior al vencimiento del plazo» — La fecha hasta la cual los cobros del permiso deben permanecer depositados según el contrato de financiamiento es posterior al vencimiento del plazo para la liquidación de divisas del permiso. · tramo [exacta]: «En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento del plazo para la liquidación de divisas del permiso»
- **res1 Restriccion** «Tope 125% de servicios de capital e intereses» — La opción de ampliación del plazo está disponible hasta alcanzar el 125% de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 meses calendario. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capi…', 'el mes corriente y los siguientes 6 (seis) meses calendario'] · tramo [exacta]: «Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario.»
- R: pot1 Potestad —aplica_a→ Sujeto_exportador (mención «el exportador»)
- R: pot2 Potestad —aplica_a→ Sujeto (mención «La entidad encargada del seguimiento del permiso»)
- R: cond1 Condicion —condicion_de→ pot1 Potestad
- R: res1 Restriccion —limita→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:23 | sí | «La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias:» | `extraida_tramo_verificado` |  | Potestad [exacta] cuyo tramo contiene «La entidad encargada del seguimiento del permiso podrá conceder extensiones…» |

## `ext::7.9.4` — Por aquellas operaciones para las cuales los exportadores hagan ejercicio de la opción

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.9. Operaciones financieras habilitadas para aplicar cobros de exportaciones de bienes y
> *heredado:* servicios.
> *propio:* 7.9.4. Por aquellas operaciones para las cuales los exportadores hagan ejercicio de la opción prevista en el presente punto, la entidad financiera designada deberá remitir, por nota dirigida a la Gerencia Principal de Exterior y Cambios dentro de los 90 (noventa) días corridos posteriores al primer ingreso de fondos, la correspondiente certificación de que se cumplen las condiciones que permiten encuadrar la operación. La certificación que se presente en el BCRA deberá contener como mínimo, el detalle del punto normativo en que encuadra la operación, su número de identificación en el marco del "Seguimiento de anticipos y otras financiaciones de exportación de bienes" y, si existen endeudamientos que contemplen el mantenimiento de cuentas de garantías o cuentas específicas sin estar en garantía, identificación del tipo de cuenta y entidad financiera local o del exterior. El número de identificación a consignar será el número APX para las operaciones con liquidación en el mercado o el número ECO (Entidad-CUIT-N° Operación) para aquellas operaciones sin liquidaciones por ser refinanciaciones de deudas preexistentes. En el caso de que se trate de operaciones destinadas a la financiación de proyectos comprendidos en el punto 7.9.2., la entidad deberá adicionalmente remitir la certificación del cumplimiento de las condiciones para la elegibilidad del proyecto, la cual deberá contener, como mínimo, la descripción de éste, el monto proyectado a invertir y la composición del financiamiento. La certificación que emita la entidad financiera deberá basarse en las proyecciones sobre el aumento anual esperado en la producción de bienes exportables o que permiten sustituir importaciones, ventas externas en base al análisis de posibilidades de colocación o en su caso importaciones a sustituir, proporción de futuras ventas externas o sustitución de importaciones a cubrir con la producción del nuevo proyecto, flujos de divisas esperados y flujos de divisas con afectación a la atención de los servicios del financiamiento. La entidad solicitará los dictámenes profesionales que estime necesarios para asegurar la razonabilidad y genuinidad de la operación en los aspectos económicos y financieros, que deberán ser complementados con dictámenes sobre los aspectos técnicos del proyecto, cuando el mismo no cuente con la aprobación en los términos de la Ley 26.360. La documentación utilizada por la entidad financiera y hojas de trabajo que avalan la emisión de la certificación deberá quedar archivada en la entidad a disposición del BCRA.

### Extracción (código A)

- **o1 Operacion** «Certificación de encuadre de operación de financiación de exportaciones» — Operaciones para las cuales los exportadores ejercen la opción prevista en el punto; la entidad financiera designada certifica que se cumplen las condiciones que permiten encuadrar la operación. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «la entidad financiera designada deberá remitir, por nota dirigida a la Gerencia Principal de Exterior y Cambios dentro de los 90 (noventa) días corridos posteriores al primer ingreso de fondos, la correspondiente certificación»
- **ob1 Obligacion** «Remitir certificación al BCRA en 90 días corridos» — Por las operaciones para las cuales los exportadores ejercen la opción, la entidad financiera designada remite por nota a la Gerencia Principal de Exterior y Cambios la certificación de que se cumplen las condiciones de encuadre, dentro de los 90 días corridos posteriores al primer ingreso de fondos. · props: `{"tipo": "reporte_al_supervisor"}` · umbral: ['dentro de los 90 (noventa) días corridos posteriores al primer ingreso de fondos'] · tramo [exacta]: «la entidad financiera designada deberá remitir, por nota dirigida a la Gerencia Principal de Exterior y Cambios dentro de los 90 (noventa) días corridos posteriores al primer ingreso de fondos, la correspondiente certificación de que se cumplen las condiciones que permiten encuadrar la operación»
- **ob2 Obligacion** «Contenido mínimo de la certificación» — La certificación presentada en el BCRA debe contener como mínimo el detalle del punto normativo de encuadre, el número de identificación en el Seguimiento de anticipos y otras financiaciones de exportación de bienes y, si existen endeudamientos con cuentas de garantías o cuentas específicas sin estar en garantía, el tipo de cuenta y la entidad financiera local o del exterior. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «La certificación que se presente en el BCRA deberá contener como mínimo, el detalle del punto normativo en que encuadra la operación, su número de identificación en el marco del "Seguimiento de anticipos y otras financiaciones de exportación de bienes" y, si existen endeudamientos que contemplen el mantenimiento de cue…»
- **ob3 Obligacion** «Número de identificación APX o ECO» — El número de identificación a consignar es el APX para operaciones con liquidación en el mercado, o el ECO (Entidad-CUIT-N° Operación) para operaciones sin liquidaciones por ser refinanciaciones de deudas preexistentes. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «El número de identificación a consignar será el número APX para las operaciones con liquidación en el mercado o el número ECO (Entidad-CUIT-N° Operación) para aquellas operaciones sin liquidaciones por ser refinanciaciones de deudas preexistentes»
- **c1 Condicion** «Financiación de proyectos del punto 7.9.2» — Que se trate de operaciones destinadas a la financiación de proyectos comprendidos en el punto 7.9.2. · tramo [exacta]: «En el caso de que se trate de operaciones destinadas a la financiación de proyectos comprendidos en el punto 7.9.2.»
- **ob4 Obligacion** «Certificación adicional de elegibilidad del proyecto» — Para operaciones de financiación de proyectos comprendidos en el punto 7.9.2, la entidad remite adicionalmente la certificación de cumplimiento de las condiciones de elegibilidad del proyecto, con descripción del proyecto, monto proyectado a invertir y composición del financiamiento como mínimo. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «la entidad deberá adicionalmente remitir la certificación del cumplimiento de las condiciones para la elegibilidad del proyecto, la cual deberá contener, como mínimo, la descripción de éste, el monto proyectado a invertir y la composición del financiamiento»
- **ob5 Obligacion** «Base de proyecciones de la certificación» — La certificación emitida por la entidad financiera debe basarse en proyecciones sobre el aumento anual esperado de la producción de bienes exportables o sustitutivos de importaciones, ventas externas, proporción de futuras ventas externas o sustitución de importaciones a cubrir con el nuevo proyecto, flujos de divisas esperados y flujos de divisas afectados a la atención de los servicios del finan… · props: `{"tipo": "otra"}` · tramo [exacta]: «La certificación que emita la entidad financiera deberá basarse en las proyecciones sobre el aumento anual esperado en la producción de bienes exportables o que permiten sustituir importaciones, ventas externas en base al análisis de posibilidades de colocación o en su caso importaciones a sustituir, proporción de futu…»
- **ob6 Obligacion** «Solicitar dictámenes profesionales» — La entidad solicita los dictámenes profesionales que estime necesarios para asegurar la razonabilidad y genuinidad de la operación en los aspectos económicos y financieros, complementados con dictámenes sobre los aspectos técnicos del proyecto cuando éste no cuente con la aprobación en los términos de la Ley 26.360. · props: `{"tipo": "otra"}` · tramo [exacta]: «La entidad solicitará los dictámenes profesionales que estime necesarios para asegurar la razonabilidad y genuinidad de la operación en los aspectos económicos y financieros, que deberán ser complementados con dictámenes sobre los aspectos técnicos del proyecto, cuando el mismo no cuente con la aprobación en los términ…»
- **c2 Condicion** «Proyecto sin aprobación Ley 26.360» — Que el proyecto no cuente con la aprobación en los términos de la Ley 26.360, supuesto en que se exigen dictámenes sobre los aspectos técnicos. · tramo [exacta]: «cuando el mismo no cuente con la aprobación en los términos de la Ley 26.360»
- **ob7 Obligacion** «Archivar documentación de la certificación» — La documentación utilizada y las hojas de trabajo que avalan la emisión de la certificación deben quedar archivadas en la entidad a disposición del BCRA. · props: `{"tipo": "otra"}` · tramo [exacta]: «La documentación utilizada por la entidad financiera y hojas de trabajo que avalan la emisión de la certificación deberá quedar archivada en la entidad a disposición del BCRA»
- **l1 Comunicacion** «Ley 26.360» —  · props: `{"codigo": "Ley 26.360", "tipo": "externa"}` · tramo [exacta]: «Ley 26.360»
- R: to TextoOrdenado —referencia→ l1 Comunicacion
- R: ob1 Obligacion —regula→ o1 Operacion
- R: ob2 Obligacion —regula→ o1 Operacion
- R: ob3 Obligacion —regula→ o1 Operacion
- R: ob4 Obligacion —regula→ o1 Operacion
- R: c1 Condicion —condicion_de→ ob4 Obligacion
- R: c2 Condicion —condicion_de→ ob6 Obligacion
- R: ob1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera designada»)
- R: ob4 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: ob5 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: ob6 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: ob7 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «endeudamientos con cuentas de garantía» | `dentro_de_norma` |  | dentro de la Obligacion ob2 (descripción «si existen endeudamientos con cuentas de garantías…»); sin Condicion |
| 2 | «proyectos del 7.9.2» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ ob4 Obligacion |
| 3 | «proyecto sin aprobación de la Ley 26.360» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ ob6 Obligacion |

## `ext::8.4.2` — Determinación del plazo para el ingreso y liquidación de las divisas.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
> *heredado:* 8.4. Responsabilidades de la entidad nominada para el seguimiento del permiso.
> *propio:* 8.4.2. Determinación del plazo para el ingreso y liquidación de las divisas. La entidad deberá determinar el plazo aplicable a cada exportación a partir de lo dispuesto en el punto 7.1.1. En el caso de que una exportación esté compuesta por distintos productos, el plazo aplicable será aquel que representa una mayor proporción del valor FOB total de la exportación. La fecha de vencimiento que le corresponde a una exportación será aquella resultante de sumar el plazo aplicable a la fecha de cumplido de embarque otorgada por la Aduana. Si la fecha resultante fuese un día no hábil, el vencimiento se trasladará al primer día hábil siguiente. En caso de que exista una ampliación del plazo para un producto, el nuevo plazo se aplicará tanto a las exportaciones embarcadas a partir de la vigencia de la ampliación como a las embarcadas previamente cuyo plazo para ingresar y liquidar no se encontrase vencido a ese momento. En tanto en caso de existir una reducción del plazo vigente, el plazo reducido sólo regirá para las operaciones que se oficialicen a partir de la vigencia del nuevo plazo.

### Extracción (código A)

- **op1 Operacion** «Determinación del plazo de ingreso y liquidación de divisas» — Determinación, por la entidad nominada, del plazo aplicable a cada exportación para el ingreso y liquidación de las divisas, a partir de lo dispuesto en el punto 7.1.1. · props: `{"tipo": "determinacion_de_plazo"}` · tramo [exacta]: «Determinación del plazo para el ingreso y liquidación de las divisas.»
- **ob1 Obligacion** «Determinar plazo aplicable a cada exportación» — La entidad debe determinar el plazo aplicable a cada exportación a partir de lo dispuesto en el punto 7.1.1. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La entidad deberá determinar el plazo aplicable a cada exportación a partir de lo dispuesto en el punto 7.1.1.»
- **c1 Condicion** «Exportación compuesta por distintos productos» — Que la exportación esté compuesta por distintos productos. · tramo [exacta]: «En el caso de que una exportación esté compuesta por distintos productos»
- **ob2 Obligacion** «Plazo de mayor proporción del valor FOB» — En una exportación compuesta por distintos productos, el plazo aplicable es el que representa una mayor proporción del valor FOB total de la exportación. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el plazo aplicable será aquel que representa una mayor proporción del valor FOB total de la exportación.»
- **ob3 Obligacion** «Vencimiento: plazo más cumplido de embarque» — La fecha de vencimiento de una exportación es la resultante de sumar el plazo aplicable a la fecha de cumplido de embarque otorgada por la Aduana. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La fecha de vencimiento que le corresponde a una exportación será aquella resultante de sumar el plazo aplicable a la fecha de cumplido de embarque otorgada por la Aduana.»
- **c2 Condicion** «Fecha resultante en día no hábil» — Que la fecha de vencimiento resultante sea un día no hábil. · tramo [exacta]: «Si la fecha resultante fuese un día no hábil»
- **ob4 Obligacion** «Traslado del vencimiento al primer día hábil» — Si la fecha de vencimiento resultante fuese un día no hábil, el vencimiento se traslada al primer día hábil siguiente. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el vencimiento se trasladará al primer día hábil siguiente.»
- **c3 Condicion** «Ampliación del plazo para un producto» — Que exista una ampliación del plazo para un producto. · tramo [exacta]: «En caso de que exista una ampliación del plazo para un producto»
- **ob5 Obligacion** «Plazo ampliado: embarques desde vigencia y previos no vencidos» — Ante una ampliación del plazo para un producto, el nuevo plazo se aplica a las exportaciones embarcadas desde la vigencia de la ampliación y a las embarcadas previamente cuyo plazo para ingresar y liquidar no estuviese vencido a ese momento. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el nuevo plazo se aplicará tanto a las exportaciones embarcadas a partir de la vigencia de la ampliación como a las embarcadas previamente cuyo plazo para ingresar y liquidar no se encontrase vencido a ese momento.»
- **c4 Condicion** «Reducción del plazo vigente» — Que exista una reducción del plazo vigente. · tramo [exacta]: «en caso de existir una reducción del plazo vigente»
- **ob6 Obligacion** «Plazo reducido solo para oficializaciones posteriores» — Ante una reducción del plazo vigente, el plazo reducido rige solo para las operaciones que se oficialicen a partir de la vigencia del nuevo plazo. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el plazo reducido sólo regirá para las operaciones que se oficialicen a partir de la vigencia del nuevo plazo.»
- R: ob1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion
- R: ob4 Obligacion —regula→ op1 Operacion
- R: ob5 Obligacion —regula→ op1 Operacion
- R: ob6 Obligacion —regula→ op1 Operacion
- R: c1 Condicion —condicion_de→ ob2 Obligacion
- R: c2 Condicion —condicion_de→ ob4 Obligacion
- R: c3 Condicion —condicion_de→ ob5 Obligacion
- R: c4 Condicion —condicion_de→ ob6 Obligacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «exportación de varios productos» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ ob2 Obligacion |
| 2 | «fecha no hábil» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ ob4 Obligacion |
| 3 | «ampliación del plazo» | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ ob5 Obligacion |
| 4 | «reducción del plazo» | `condicion_con_relacion` |  | c4 Condicion —condicion_de→ ob6 Obligacion |

## `ext::8.5.18.1` — La documentación permite constatar que la entrega de la mercadería

Grupos: omisiones.

### Texto

> *heredado:* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
> *heredado:* 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
> *heredado:* La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque cuando cuente con los elementos que le permitan considerar que la operación se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las condiciones previstas en cada caso. La documentación utilizada para certificar el concepto y monto de las divisas imputado en cada caso deberá quedar archivada en la entidad a disposición del BCRA.
> *heredado:* 8.5.18. Cobros locales por exportaciones del régimen de ranchos a medios de transporte de
> *heredado:* bandera extranjera. La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque por el valor equivalente a los montos abonados localmente en pesos y/o en moneda extranjera al exportador por un agente local de la empresa propietaria de los medios de transporte de bandera extranjera, en la medida que se verifiquen las siguientes condiciones:
> *propio:* 8.5.18.1. La documentación permite constatar que la entrega de la mercadería exportada se ha producido en el país, que el agente local de la empresa propietaria de los medios de transporte de bandera extranjera ha realizado localmente el pago al exportador y la moneda en la que dicho pago se efectuó.

### Extracción (código A)

- **c1 Condicion** «Documentación que constata entrega, pago local y moneda» — Supuesto para que la entidad pueda considerar cumplimentado el seguimiento del permiso de embarque (cobros locales por exportaciones del régimen de ranchos a medios de transporte de bandera extranjera): la documentación permite constatar que la entrega de la mercadería exportada se produjo en el país, que el agente local de la empresa propietaria de los medios de transporte de bandera extranjera p… · tramo [exacta]: «La documentación permite constatar que la entrega de la mercadería exportada se ha producido en el país, que el agente local de la empresa propietaria de los medios de transporte de bandera extranjera ha realizado localmente el pago al exportador y la moneda en la que dicho pago se efectuó.»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:30 | sí | «La documentación utilizada para certificar el concepto y monto de las divisas imputado en cada caso deberá quedar archivada en la entidad a disposición del BCRA» | `ausente` |  | ninguna entidad ni omisión cubre la oración del heredado |

## `ext::8.5.22` — Exportación alcanzada por los beneficios cambiarios del Régimen de Promoción de

Grupos: omisiones.

### Texto

> *heredado:* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
> *heredado:* 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
> *heredado:* La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque cuando cuente con los elementos que le permitan considerar que la operación se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las condiciones previstas en cada caso. La documentación utilizada para certificar el concepto y monto de las divisas imputado en cada caso deberá quedar archivada en la entidad a disposición del BCRA.
> *propio:* 8.5.22. Exportación alcanzada por los beneficios cambiarios del Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13). A pedido de un cliente que posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos establecido por el Decreto 929/13, la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso que se encuentre amparado por un "Certificado DECRETO 929/13" emitido a partir de lo dispuesto por la Resolución 26/23 de la Secretaría de Energía.

### Extracción (código A)

- **p1 Potestad** «Considerar cumplimentado seguimiento — certificado Decreto 929/13» — La entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso amparada por un "Certificado DECRETO 929/13" emitido a partir de la Resolución 26/23 de la Secretaría de Energía, a pedido de un cliente con proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13). · tramo [exacta]: «la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso que se encuentre amparado por un "Certificado DECRETO 929/13" emitido a partir de lo dispuesto por la Resolución 26/23 de la Secretaría de Energía»
- **c1 Condicion** «Pedido de cliente con proyecto en régimen Decreto 929/13» — Que el cliente pida la imputación y posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13). · tramo [exacta]: «A pedido de un cliente que posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos establecido por el Decreto 929/13»
- **d929 Comunicacion** «Decreto 929/13» —  · props: `{"codigo": "Decreto 929/13", "tipo": "externa"}` · tramo [exacta]: «Decreto 929/13»
- **r26 Comunicacion** «Resolución 26/23 Secretaría de Energía» —  · props: `{"codigo": "Resolución 26/23 de la Secretaría de Energía", "tipo": "externa"}` · tramo [exacta]: «Resolución 26/23 de la Secretaría de Energía»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: to TextoOrdenado —referencia→ d929 Comunicacion
- R: to TextoOrdenado —referencia→ r26 Comunicacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:27 | sí | «La documentación utilizada para certificar el concepto y monto de las divisas imputado en cada caso deberá quedar archivada en la entidad a disposición del BCRA» | `ausente` |  | ninguna entidad ni omisión cubre la oración del heredado (la omisión de K refiere a otro tramo) |

## `ext::9.1.5` — Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean

Grupos: omisiones.

### Texto

> *heredado:* Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.
> *heredado:* 9.1. Operaciones comprendidas.
> *propio:* 9.1.5. Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones y para los cuales el exportador solicite su aplicación a permisos de embarque oficializados a partir del 02/09/19.

### Extracción (código A)

- **op1 Operacion** «Préstamos financieros con contratos vigentes al 31/08/19, servicios atendidos con flujo de exportaciones en el exterior» — Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones, y para los cuales el exportador solicite su aplicación a permisos de embarque oficializados a partir del 02/09/19. Operación comprendida en el seguimiento de anticipos y otras financiaciones de exportación de bie… · props: `{"tipo": "prestamo_financiero_de_exportacion_comprendido"}` · tramo [exacta]: «Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones y para los cuales el exportador solicite su aplicación a permisos de embarque oficializados a partir del 02/09/19.»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:3 | no | «9.1. Operaciones comprendidas.» | `ausente` |  | ninguna entidad ni omisión cubre el título «9.1. Operaciones comprendidas.» |

## `ext::9.3.10.4` — el pasivo en pesos con el exterior generado a partir de la fecha de la no

Grupos: omisiones.

### Texto

> *heredado:* Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.
> *heredado:* 9.3. Certificaciones de aplicación de cobros de exportaciones.
> *heredado:* A solicitud del exportador, la entidad encargada del seguimiento emitirá las certificaciones de aplicación en la medida que se verifiquen las condiciones previstas en los puntos 9.3.1. al 9.3.13. La entidad deberá dejar registradas las certificaciones de aplicación emitidas para cada una de las operaciones bajo su seguimiento.
> *heredado:* 9.3.10. Repatriaciones de aportes de inversión directa de no residentes en empresas que no
> *heredado:* controlantes de entidades financieras locales admitidas en los puntos 7.9. o 7.10. La entidad podrá emitir la certificación de aplicación en la medida que la entidad cuenta con la documentación que le permita verificar:
> *propio:* 9.3.10.4. el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda. Se encuentra declarado en la última presentación vencida del "Relevamiento de activos y pasivos externos", en caso de corresponder;

### Extracción (código A)

- **c1 Condicion** «Pasivo en pesos con el exterior declarado» — Supuesto que la entidad debe poder verificar con documentación para emitir la certificación de aplicación (repatriaciones de aportes de inversión directa de no residentes, punto 9.3.10): el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda, declarado en la última presentación vencida del "Relevami… · tramo [exacta]: «el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda. Se encuentra declarado en la última presentación vencida del "Relevamiento de activos y pasivos externos", en caso de corresponder»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:13 | no | «en caso de corresponder» | `extraida_tramo_verificado` |  | c1 Condicion [exacta], tramo que contiene «en caso de corresponder» |

## `ext::9.3.12::intro` — [bloque intro] Utilidades y dividendos en el marco de lo previsto en el punto 7.10.

Grupos: omisiones.

### Texto

> *heredado:* Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.
> *heredado:* 9.3. Certificaciones de aplicación de cobros de exportaciones.
> *heredado:* 9.3.12. Utilidades y dividendos en el marco de lo previsto en el punto 7.10.
> *propio:* La entidad podrá emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes, en la medida que se cumplan la totalidad de las siguientes condiciones:

### Extracción (código A)

- **p1 Potestad** «Emitir certificaciones de aplicación de divisas a utilidades y dividendos» — La entidad podrá emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes, en la medida que se cumplan la totalidad de las condiciones enumeradas a continuación (punto 7.10). · tramo [exacta]: «La entidad podrá emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes»
- **op1 Operacion** «Certificación de aplicación de divisas al pago de utilidades y dividendos a no residentes» — Emisión de certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes, en el marco del punto 7.10. · props: `{"tipo": "certificacion"}` · tramo [exacta]: «emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:30 | sí | «en el marco de lo previsto en el punto 7.10» | `ausente` |  | ninguna entidad ni omisión cubre «en el marco de lo previsto en el punto 7.10» (las omisiones de K y W refieren a «podrá emitir») |

## `ext::9.3.9` — Títulos de deuda con registro público en el país denominados en moneda extranjera

Grupos: omisiones.

### Texto

> *heredado:* Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.
> *heredado:* 9.3. Certificaciones de aplicación de cobros de exportaciones.
> *heredado:* A solicitud del exportador, la entidad encargada del seguimiento emitirá las certificaciones de aplicación en la medida que se verifiquen las condiciones previstas en los puntos 9.3.1. al 9.3.13. La entidad deberá dejar registradas las certificaciones de aplicación emitidas para cada una de las operaciones bajo su seguimiento.
> *propio:* 9.3.9. Títulos de deuda con registro público en el país denominados en moneda extranjera admitidos en el punto 7.9. La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación a partir del vencimiento del capital, intereses y otros conceptos admitidos, en la medida que verifique las condiciones indicadas en el punto 9.3.1., constate que la cancelación tuvo lugar a partir de la fecha de vencimiento y cuente con la documentación que verifican el cumplimiento de los requisitos establecidos en el punto 7.9.

### Extracción (código A)

- **p1 Potestad** «Emitir certificaciones de aplicación — títulos de deuda en ME» — La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación, a partir del vencimiento del capital, intereses y otros conceptos admitidos, de títulos de deuda con registro público en el país denominados en moneda extranjera admitidos en el punto 7.9. · tramo [exacta]: «La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación a partir del vencimiento del capital, intereses y otros conceptos admitidos»
- **op1 Operacion** «Certificación de aplicación — títulos de deuda con registro público en ME» — Emisión de certificaciones de aplicación de las divisas a la cancelación de capital, intereses y otros conceptos admitidos de títulos de deuda con registro público en el país denominados en moneda extranjera admitidos en el punto 7.9, a partir del vencimiento. · props: `{"tipo": "certificacion_de_aplicacion"}` · tramo [exacta]: «emitir las certificaciones de aplicación de las divisas a la cancelación»
- **c1 Condicion** «Condiciones del punto 9.3.1 verificadas» — La entidad verifica las condiciones indicadas en el punto 9.3.1. · tramo [exacta]: «en la medida que verifique las condiciones indicadas en el punto 9.3.1.»
- **c2 Condicion** «Cancelación constatada desde fecha de vencimiento» — La entidad constata que la cancelación tuvo lugar a partir de la fecha de vencimiento. · tramo [exacta]: «constate que la cancelación tuvo lugar a partir de la fecha de vencimiento»
- **c3 Condicion** «Documentación del cumplimiento del punto 7.9» — La entidad cuenta con la documentación que verifica el cumplimiento de los requisitos establecidos en el punto 7.9. · tramo [exacta]: «cuente con la documentación que verifican el cumplimiento de los requisitos establecidos en el punto 7.9»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:19 | sí | «admitidos en el punto 7.9» | `ausente` |  | ningún tramo contiene «admitidos en el punto 7.9» (c3 y c1 cubren otras menciones de los puntos 7.9 y 9.3.1) |

## `lingob::2.3.2.1` — Conflictos de intereses entre la entidad financiera, el Directorio, la Alta Gerencia

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Directorio.
> *heredado:* Los miembros del Directorio deberán contar con los conocimientos y competencias necesarias para comprender claramente sus responsabilidades y funciones dentro del gobierno societario y obrar con lealtad y con la diligencia de un buen hombre de negocios en los asuntos de la entidad financiera. Se considera una buena práctica que el Directorio se conforme observando el criterio de paridad de género, a efectos de potenciar la discusión y enriquecer la toma de decisiones con respecto a estrategias, políticas y asunción de riesgos. En los casos en que la presidencia del Directorio sea ejercida por un miembro que desempeña también funciones ejecutivas, se adoptarán las medidas necesarias a los efectos de que las decisiones se mantengan en línea con los objetivos societarios.
> *heredado:* 2.3. Objetivos estratégicos y valores organizacionales.
> *heredado:* Con ajuste al objeto social establecido por la Asamblea de accionistas, se considera como buena práctica que el Directorio apruebe y supervise los objetivos estratégicos y los valores societarios, comunicándolos a toda la organización. A esos efectos, el Directorio:
> *heredado:* 2.3.2. Se asegurará de que la Alta Gerencia implemente procedimientos para promover con-
> *heredado:* ductas profesionales y que prevengan y/o limiten la existencia de actividades o situaciones que puedan afectar negativamente la calidad del gobierno societario, tales como:
> *propio:* 2.3.2.1. Conflictos de intereses entre la entidad financiera, el Directorio, la Alta Gerencia y el grupo económico al que pertenece la entidad.

### Extracción (código A)

- **o1 Obligacion** «Asegurar procedimientos contra conflictos de intereses» — Recomendación (buena práctica), no un deber: el Directorio se asegura de que la Alta Gerencia implemente procedimientos para promover conductas profesionales y que prevengan y/o limiten la existencia de actividades o situaciones que puedan afectar negativamente la calidad del gobierno societario, tales como los conflictos de intereses entre la entidad financiera, el Directorio, la Alta Gerencia y … · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "se considera como bue-\nna práctica", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «se considera como buena práctica que el Directorio apruebe y supervise los objetivos estratégicos y los valores societarios, comunicándolos a toda la organización. A esos efectos, el Directorio: […] Conflictos de intereses entre la entidad financiera, el Directorio, la Alta Gerencia y el grupo económico al que pertenec…»
- R: o1 Obligacion —aplica_a→ Sujeto_directorio (mención «el Directorio»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:2 | sí | «Se considera una buena práctica que el Directorio se conforme observando el criterio de paridad de género, a efectos de potenciar la discusión y enriquecer la t…» | `ausente` |  | ninguna entidad ni omisión cubre la oración del heredado |

## `lingob::3.1.6` — Utilizar efectivamente el trabajo llevado a cabo por las auditorías interna y externa y las

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Alta Gerencia.
> *heredado:* Los integrantes de la Alta Gerencia deberán tener la idoneidad y experiencia necesarias en la actividad financiera para gestionar el negocio bajo su supervisión así como el control apropiado del personal de esas áreas.
> *heredado:* 3.1. Responsabilidades.
> *heredado:* La Alta Gerencia, como una buena práctica, será responsable de:
> *propio:* 3.1.6. Utilizar efectivamente el trabajo llevado a cabo por las auditorías interna y externa y las funciones relacionadas con el sistema de control interno, conforme a lo establecido en la Sección 5.

### Extracción (código A)

- **o1 Obligacion** «Utilizar efectivamente trabajo de auditorías y control interno» — Recomendación (buena práctica), no un deber: la Alta Gerencia es responsable de utilizar efectivamente el trabajo llevado a cabo por las auditorías interna y externa y las funciones relacionadas con el sistema de control interno, conforme a lo establecido en la Sección 5. · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "como una buena práctica", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «La Alta Gerencia, como una buena práctica, será responsable de: […] Utilizar efectivamente el trabajo llevado a cabo por las auditorías interna y externa y las funciones relacionadas con el sistema de control interno, conforme a lo establecido en la Sección 5.»
- R: o1 Obligacion —aplica_a→ Sujeto_alta_gerencia (mención «La Alta Gerencia»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:29 | sí (remisión pura) | «conforme a lo establecido en la Sección 5» | `extraida_tramo_verificado` |  | o1 Obligacion [exacta], tramo que contiene «conforme a lo establecido en la Sección 5» |

## `lingob::3.2::intro` — [bloque intro] Decisiones gerenciales.

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Alta Gerencia.
> *heredado:* 3.2. Decisiones gerenciales.
> *propio:* Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona. Es recomendable que la Alta Gerencia:

### Extracción (código A)

- **o1 Obligacion** «Decisiones gerenciales por más de una persona» — Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona. · props: `{"tipo": "otra"}` · tramo [exacta]: «Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona.»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:14 | sí | «en orden a las buenas prácticas» | `extraida_tramo_verificado` |  | o1 Obligacion [exacta], tramo que contiene «en orden a las buenas prácticas» |

## `lingob::4.2.1` — Comité de gestión de riesgos, que realizará un seguimiento de las actividades de la Alta

Grupos: omisiones.

### Texto

> *heredado:* Sección 4. Comités.
> *heredado:* 4.2. Otros comités.
> *heredado:* De acuerdo con las dimensiones, complejidad, importancia económica y perfil de riesgo que presente la entidad financiera y el grupo económico de que se trate, se recomienda el establecimiento de otros comités especializados, con una clara definición y divulgación de sus mandatos, composición (incluidos los miembros considerados independientes) y procedimientos de trabajo. Entre otros comités, se pueden mencionar los siguientes:
> *heredado:* Tanto los directores independientes como aquellos que no reúnan esa condición, pero posean conocimientos y aptitudes relevantes, deberían tener un rol clave en tales comités. A los efectos de maximizar la objetividad, es conveniente que la mayoría de los miembros revistan la condición de independiente, contemplando en su caso las situaciones previstas en el primer párrafo de este punto y la naturaleza específica de la entidad. Los citados comités no son excluyentes de otros que se puedan exigir de manera específica por normas del Banco Central de la República Argentina.
> *propio:* 4.2.1. Comité de gestión de riesgos, que realizará un seguimiento de las actividades de la Alta Gerencia relacionadas con la gestión de los riesgos de crédito, de mercado, de liquidez y/o de activos y pasivos, operacional, de cumplimiento y de reputación, entre otros. Asimismo, asesorará al Directorio sobre los riesgos de la entidad.

### Extracción (código A)

- **o1 Operacion** «Establecimiento de comité de gestión de riesgos» — Establecimiento del comité de gestión de riesgos, que realiza un seguimiento de las actividades de la Alta Gerencia relacionadas con la gestión de los riesgos de crédito, de mercado, de liquidez y/o de activos y pasivos, operacional, de cumplimiento y de reputación, entre otros, y asesora al Directorio sobre los riesgos de la entidad. · props: `{"tipo": "otra"}` · tramo [exacta]: «se recomienda el establecimiento de otros comités especializados […] Comité de gestión de riesgos, que realizará un seguimiento de las actividades de la Alta Gerencia relacionadas con la gestión de los riesgos de crédito, de mercado, de liquidez y/o de activos y pasivos, operacional, de cumplimiento y de reputación, en…»
- **ob1 Obligacion** «Recomendación: establecer comité de gestión de riesgos» — Recomendación (no un deber) de que la entidad financiera establezca, según sus dimensiones, complejidad, importancia económica y perfil de riesgo, un comité de gestión de riesgos, con definición y divulgación de sus mandatos, composición y procedimientos de trabajo, que realice un seguimiento de las actividades de la Alta Gerencia relacionadas con la gestión de los riesgos de crédito, de mercado, … · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "se recomienda el establecimiento de otros comités especializados", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «se recomienda el establecimiento de otros comités especializados […] Comité de gestión de riesgos, que realizará un seguimiento de las actividades de la Alta Gerencia relacionadas con la gestión de los riesgos de crédito, de mercado, de liquidez y/o de activos y pasivos, operacional, de cumplimiento y de reputación, en…»
- R: ob1 Obligacion —regula→ o1 Operacion
- R: ob1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:4 | sí | «Tanto los directores independientes como aquellos que no reúnan esa condición, pero posean conocimientos y aptitudes relevantes, deberían tener un rol clave en …» | `ausente` |  | ninguna entidad ni omisión cubre la oración del heredado |
| con_marca:19 | sí | «A los efectos de maximizar la objetividad, es conveniente que la mayoría de los miembros revistan la condición de independiente» | `ausente` |  | ninguna entidad ni omisión cubre la oración del heredado |

## `lingob::4.2.2` — Comité de incentivos al personal, encargado de vigilar que el sistema de incentivos eco-

Grupos: omisiones.

### Texto

> *heredado:* Sección 4. Comités.
> *heredado:* 4.2. Otros comités.
> *heredado:* De acuerdo con las dimensiones, complejidad, importancia económica y perfil de riesgo que presente la entidad financiera y el grupo económico de que se trate, se recomienda el establecimiento de otros comités especializados, con una clara definición y divulgación de sus mandatos, composición (incluidos los miembros considerados independientes) y procedimientos de trabajo. Entre otros comités, se pueden mencionar los siguientes:
> *heredado:* Tanto los directores independientes como aquellos que no reúnan esa condición, pero posean conocimientos y aptitudes relevantes, deberían tener un rol clave en tales comités. A los efectos de maximizar la objetividad, es conveniente que la mayoría de los miembros revistan la condición de independiente, contemplando en su caso las situaciones previstas en el primer párrafo de este punto y la naturaleza específica de la entidad. Los citados comités no son excluyentes de otros que se puedan exigir de manera específica por normas del Banco Central de la República Argentina.
> *propio:* 4.2.2. Comité de incentivos al personal, encargado de vigilar que el sistema de incentivos económicos al personal sea consistente con la cultura, los objetivos, los negocios a largo plazo, la estrategia y el entorno de control de la entidad, según se formule en la pertinente política.

### Extracción (código A)

- **o1 Obligacion** «Recomendación comité de incentivos al personal» — Recomendación (no un deber) de establecer, según las dimensiones, complejidad, importancia económica y perfil de riesgo de la entidad y su grupo económico, un comité de incentivos al personal, encargado de vigilar que el sistema de incentivos económicos al personal sea consistente con la cultura, los objetivos, los negocios a largo plazo, la estrategia y el entorno de control de la entidad, según … · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "se recomienda el establecimiento de otros comités especializados", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «se recomienda el establecimiento de otros comités especializados […] Comité de incentivos al personal, encargado de vigilar que el sistema de incentivos económicos al personal sea consistente con la cultura, los objetivos, los negocios a largo plazo, la estrategia y el entorno de control de la entidad, según se formule…»
- **op1 Operacion** «Establecimiento de comité de incentivos al personal» — Establecimiento de un comité especializado de incentivos al personal, que vigila que el sistema de incentivos económicos al personal sea consistente con la cultura, los objetivos, los negocios a largo plazo, la estrategia y el entorno de control de la entidad, según la pertinente política. · props: `{"tipo": "otra"}` · tramo [exacta]: «Comité de incentivos al personal, encargado de vigilar que el sistema de incentivos económicos al personal sea consistente con la cultura»
- R: o1 Obligacion —regula→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:21 | sí | «se recomienda el establecimiento de otros comités especializados» | `extraida_tramo_verificado` |  | o1 Obligacion [exacta], tramo que contiene «se recomienda el establecimiento de otros comités especializados» |

## `lingob::7.1.1` — Estructura del Directorio (conformación según el estatuto, tamaño, miembros, proceso

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Otras políticas organizacionales.
> *heredado:* 7.1. Política de transparencia.
> *heredado:* A los fines de que la entidad financiera sea dirigida con transparencia, es recomendable una apropiada divulgación de la información hacia el depositante, inversor, accionista y público en general que promueva la disciplina de mercado y, por ende, un buen gobierno societario. El objetivo de la política de transparencia en el gobierno societario es proveer a las citadas partes de la información necesaria para que evalúen la efectividad en la gestión del Directorio y de la Alta Gerencia. La publicación de informes sobre los aspectos del gobierno societario puede asistir a los participantes del mercado y a otras partes interesadas en el monitoreo de la fortaleza y solvencia de la entidad. Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la siguiente información, en función del tamaño, complejidad y estructura propietaria, importancia económica y perfil de riesgo de la entidad, dependiendo también de si la entidad cotiza o no en bolsas:
> *propio:* 7.1.1. Estructura del Directorio (conformación según el estatuto, tamaño, miembros, proceso de selección, calificaciones, criterios de independencia y paridad de género, intereses particulares en transacciones o asuntos que afecten a la entidad financiera) y de la Alta Gerencia (responsabilidades, líneas de reportes, calificaciones y experiencia) y miembros de los comités (misión, objetivos y responsabilidades).

### Extracción (código A)

- **o1 Obligacion** «Divulgar estructura del Directorio, Alta Gerencia y comités» — Recomendación (no un deber) de incluir en los sitios públicos de las entidades financieras y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la estructura del Directorio (conformación según el estatuto, tamaño, miembros, proceso de selección, calificaciones, criterios de independencia y paridad de género, intereses particulares en transacciones o asuntos… · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "Es deseable incluir", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la siguiente información, en función del tamaño, complejidad y estructura propietaria, importancia económica y perfil de riesgo de l…»
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:25 | sí | «A los fines de que la entidad financiera sea dirigida con transparencia, es recomendable una apropiada divulgación de la información hacia el depositante, inver…» | `ausente` |  | ninguna entidad ni omisión cubre la oración del heredado |

## `lingob::7.1.7` — En las entidades financieras públicas, la definición de la política en función de su natura-

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Otras políticas organizacionales.
> *heredado:* 7.1. Política de transparencia.
> *heredado:* A los fines de que la entidad financiera sea dirigida con transparencia, es recomendable una apropiada divulgación de la información hacia el depositante, inversor, accionista y público en general que promueva la disciplina de mercado y, por ende, un buen gobierno societario. El objetivo de la política de transparencia en el gobierno societario es proveer a las citadas partes de la información necesaria para que evalúen la efectividad en la gestión del Directorio y de la Alta Gerencia. La publicación de informes sobre los aspectos del gobierno societario puede asistir a los participantes del mercado y a otras partes interesadas en el monitoreo de la fortaleza y solvencia de la entidad. Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la siguiente información, en función del tamaño, complejidad y estructura propietaria, importancia económica y perfil de riesgo de la entidad, dependiendo también de si la entidad cotiza o no en bolsas:
> *propio:* 7.1.7. En las entidades financieras públicas, la definición de la política en función de su naturaleza jurídica conforme su carta orgánica y/o estatutos.

### Extracción (código A)

- **o1 Obligacion** «Divulgar política según naturaleza jurídica (entidades públicas)» — Recomendación (no un deber): en las entidades financieras públicas, incluir en los sitios públicos (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la definición de la política en función de su naturaleza jurídica conforme su carta orgánica y/o estatutos, en función del tamaño, complejidad y estructura propietaria, importancia econ… · props: `{"tipo": "presentacion_informativa"}` · no definidas: `{"modalidad": "Es deseable incluir", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la siguiente información, en función del tamaño, complejidad y estructura propietaria, importancia económica y perfil de riesgo de l…»
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:22 | sí | «Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información pe…» | `extraida_tramo_verificado` |  | o1 Obligacion [exacta], tramo de dos segmentos que contiene la oración del heredado entera |

## `pagjub::2.2` — Modelo de nota de presentación de la rendición de cuentas.

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Rendición de cuentas por parte de las entidades financieras.
> *propio:* 2.2. Modelo de nota de presentación de la rendición de cuentas. Fecha: De: (1) A: BANCO CENTRAL DE LA REPÚBLICA ARGENTINA. Remitimos a Uds. para su procesamiento, en los términos de las normas sobre "Pago de beneficios de la seguridad social por cuenta de la Administración Nacional de la Seguridad Social (ANSES)" los archivos contenidos en los soportes de información que se acompañan, en los cuales se detalla el estado de la totalidad de las órdenes de pago que la ANSES nos encomendara pagar, correspondientes al período .....(2)......de la liquidación ….(3)... Emisión de ANSES: …...................(4) ............ casos por $................(5) ................, Órdenes de Pago pagadas: .............(6) …........ casos por $................(7) .................. Órdenes de Pago impagas: .............(8) ............ casos por $................(9) .................. Certificamos que los datos señalados precedentemente son ciertos y resumen la información detallada en los archivos contenidos en los soportes que se acompañan. Identificación de los archivos Responsables: Firma Firma Nombres y apellidos Nombres y apellidos Tipo y N° doc. de identidad (10) Tipo y N° doc. de identidad (10) Tel. Tel. ................. RECIBIDO ------------------------------------------------------------------------------------------------------------------ Referencias: (1)Código de la entidad financiera. (2)Consignar período de pago mensual o aguinaldo, en su caso. (3)Consignar tipo de liquidación ("ANSES", cuando la rendición es de prestaciones de la Administración Nacional de la Seguridad Social y "MTESS" cuando la rendición es de prestaciones por cuenta y orden del Ministerio de Trabajo, Empleo y Seguridad Social). (4) Cantidad de órdenes de pago que se encomendó pagar a la entidad financiera durante el período de pago correspondiente. (5)Importe en pesos del total puesto al pago. (6)Cantidad de órdenes de pago pagadas. (7)Importe en pesos del total pagado. (8)Cantidad de órdenes de pago impagas. (9)Importe en pesos del total impago. (10)Conforme a lo previsto en las normas sobre "Documentos de identificación en vigencia".

### Extracción (código A)

- **op1 Operacion** «Presentación de rendición de cuentas al BCRA» — Remisión al BCRA, mediante nota modelo, de los archivos en soportes de información con el estado de la totalidad de las órdenes de pago encomendadas por la ANSES, correspondientes al período y liquidación consignados. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Remitimos a Uds. para su procesamiento, en los términos de las normas sobre "Pago de beneficios de la seguridad social por cuenta de la Administración Nacional de la Seguridad Social (ANSES)" los archivos contenidos en los soportes de información que se acompañan»
- **ob1 Obligacion** «Certificar datos de la rendición de cuentas» — La nota de presentación certifica que los datos consignados (casos e importes emitidos, pagados e impagos) son ciertos y resumen la información detallada en los archivos de los soportes acompañados. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «Certificamos que los datos señalados precedentemente son ciertos y resumen la información detallada en los archivos contenidos en los soportes que se acompañan.»
- R: op1 Operacion —requiere→ ob1 Obligacion
- Omisión `fuera_de_tipos` [exacta]: «Responsables: Firma Firma Nombres y apellidos Nombres y apellidos Tipo y N° doc. de identidad (10) Tipo y N° doc. de identidad (10) Tel. Tel.» — Campos del formulario de firma de los responsables; es contenido de modelo, sin norma extraíble.
- Omisión `fuera_de_tipos` [exacta]: «(3)Consignar tipo de liquidación ("ANSES", cuando la rendición es de prestaciones de la Administración Nacional de la Seguridad Social y "MTESS" cuando la rendición es de prestaciones por cuenta y orden del Ministerio de Trabajo, Empleo y Seguridad Social).» — Instrucciones de llenado del formulario (referencias 1 a 10); se habría usado Obligacion o Definicion pero describen campos de un modelo. Sin sujeto nombrado en la unidad, no se emite aplica_a.

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:16 | no | «Órdenes de Pago pagadas: .............(6) …........ casos por $................(7) ..................» | `ausente` |  | ninguna entidad; las omisiones fuera_de_tipos refieren a otros campos del modelo (firmas, nota 3) |

## `pagjub::2.8.4.3` — Debitar de la cuenta corriente de la entidad participante el importe de las órdenes

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Rendición de cuentas por parte de las entidades financieras.
> *heredado:* 2.8. Liquidación de la rendición de cuentas.
> *heredado:* El procesamiento de la información de la rendición de cuentas dará lugar a diferentes movimientos de fondos los que, según los casos correspondientes, se describen a continuación:
> *heredado:* 2.8.4. Presentación aceptada durante el período de presentación tardía con inconsistencias.
> *heredado:* El BCRA, en el mismo día de la aceptación, procederá a:
> *propio:* 2.8.4.3. Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditando el mismo en una cuenta transitoria del BCRA, hasta la fecha límite.

### Extracción (código A)

- **op1 Operacion** «Débito en cuenta corriente de órdenes de pago abonadas e impagas con inconsistencias» — Débito, de la cuenta corriente de la entidad participante, del importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditándolo en una cuenta transitoria del BCRA, hasta la fecha límite; en presentación aceptada durante el período de presentación tardía con inconsistencias. · props: `{"tipo": "debito en cuenta corriente"}` · tramo [exacta]: «Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditando el mismo en una cuenta transitoria del BCRA, hasta la fecha límite.»
- **ob1 Obligacion** «BCRA debita órdenes de pago impagas con inconsistencias el día de la aceptación» — El BCRA, en el mismo día de la aceptación de la presentación tardía con inconsistencias, debe debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditándolo en una cuenta transitoria del BCRA, hasta la fecha límite. · props: `{"tipo": "otra"}` · tramo [exacta]: «El BCRA, en el mismo día de la aceptación, procederá a: […] Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditando el mismo en una cuenta transitoria del BCRA, hasta la fecha límite.»
- R: ob1 Obligacion —aplica_a→ Sujeto_bcra (mención «El BCRA»)
- R: ob1 Obligacion —regula→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:14 | no | «El procesamiento de la información de la rendición de cuentas dará lugar a diferentes movimientos de fondos los que, según los casos correspondientes, se descri…» | `ausente` |  | ninguna entidad ni omisión cubre la oración del heredado |

## `polcre::6.2.1.5` — Al momento del otorgamiento de financiaciones a personas humanas, se deberá

Grupos: omisiones.

### Texto

> *heredado:* Sección 6. Préstamos de Unidades de Valor Adquisitivo y de Unidades de Vivienda.
> *heredado:* 6.2. Préstamos de Unidades de Vivienda actualizables por el "ICC" - Ley 27.271 ("UVI").
> *heredado:* 6.2.1. Las operaciones de financiación de Unidades de Vivienda actualizables por el índice del
> *heredado:* costo de construcción ("ICC") - Ley 27.271 ("UVI") estarán sujetas a las siguientes condiciones:
> *propio:* 6.2.1.5. Al momento del otorgamiento de financiaciones a personas humanas, se deberá tener especial atención a la relación cuota/ingreso de manera de que el deudor pueda afrontar posibles incrementos en el importe de las cuotas sin afectar su capacidad de pago, teniendo en cuenta que sus ingresos pueden no seguir la evolución de la Unidad de Vivienda actualizable por "ICC" ("UVI") ni la del "CVS".

### Extracción (código A)

- **op1 Operacion** «Otorgamiento de financiaciones UVI a personas humanas» — Otorgamiento de financiaciones en Unidades de Vivienda actualizables por ICC (UVI) a personas humanas. · props: `{"tipo": "financiacion"}` · tramo [exacta]: «Al momento del otorgamiento de financiaciones a personas humanas»
- **ob1 Obligacion** «Atención especial a relación cuota/ingreso en UVI» — Al otorgar financiaciones UVI a personas humanas, se debe tener especial atención a la relación cuota/ingreso, de modo que el deudor pueda afrontar posibles incrementos de las cuotas sin afectar su capacidad de pago, considerando que sus ingresos pueden no seguir la evolución de la UVI ni la del CVS. · props: `{"tipo": "otra"}` · tramo [no]: «estarán sujetas a las siguientes condiciones: [â€¦] se deberá tener especial atención a la relación cuota/ingreso de manera de que el deudor pueda afrontar posibles incrementos en el importe de las cuotas sin afectar su capacidad de pago»
- R: ob1 Obligacion —regula→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:5 | sí | «Las operaciones de financiación de Unidades de Vivienda actualizables por el índice del costo de construcción ("ICC") - Ley 27.271 ("UVI") estarán sujetas a las…» | `ausente` |  | ninguna entidad ni omisión cubre la oración del heredado |

## `polcre::7.1.2` — Mantengan un importe total de financiaciones alcanzadas en pesos en el conjunto del

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Financiaciones a "Grandes empresas exportadoras".
> *heredado:* 7.1. Clientes comprendidos.
> *heredado:* Se encuentran comprendidos en la categoría de "Grandes empresas exportadoras" los clientes del sector privado no financiero que reúnan concurrentemente las siguientes condiciones:
> *heredado:* Cuando el cliente reúna la condición del punto 7.1.1. pero el importe total de sus financiaciones en pesos en el sistema financiero no supere el importe de $ 30.000 millones y no haya mantenido pases y/o cauciones bursátiles tomadas –en pesos– durante los últimos 90 días corridos, la entidad financiera podrá otorgarle nuevas financiaciones en la medida que con tales desembolsos no se supere ese importe. Cuando se trate de conjuntos económicos se los considerará como un solo cliente, a cuyo efecto será de aplicación el punto 1.2.2. de las normas sobre "Grandes exposiciones al riesgo de crédito". A los fines de la imputación de las financiaciones, será de aplicación lo previsto en las normas sobre "Grandes exposiciones al riesgo de crédito".
> *propio:* 7.1.2. Mantengan un importe total de financiaciones alcanzadas en pesos en el conjunto del sistema financiero que supere el monto de $ 30.000 millones, y/o pases y/o cauciones bursátiles tomadas –en pesos– cualquiera sea su importe durante los últimos 90 días corridos. Las financiaciones alcanzadas serán aquellas que hayan implicado desembolsos de fondos, así como el importe no utilizado del límite de crédito asignado para adelantos en cuenta corriente. Se computará su saldo de capital a fin del mes anterior al que corresponda su determinación. Cuando un cliente manifieste por declaración jurada que no se encuadra en la categoría de "Gran empresa exportadora" y, de la información disponible en la "Central de deudores del sistema financiero", surja que supera el importe de $ 30.000 millones, deberá presentar una certificación extendida por Auditor Externo o Contador Público independiente (con firma debidamente certificada por el respectivo Consejo Profesional de Ciencias Económicas) en la que se detallen las financiaciones en pesos y moneda extranjera en el conjunto de las entidades financieras, desagregando los datos correspondientes a cada uno de esos intermediarios a la fecha a la cual se refiera, y los citados pases y cauciones bursátiles tomados –en pesos– durante los últimos 90 días corridos. Lo previsto en este párrafo no será de aplicación cuando el cliente reúna la condición de MiPyME –de acuerdo con las normas sobre "Determinación de la condición de micro, pequeña y mediana empresa"–. Esa certificación mantendrá vigencia durante 90 días corridos desde la fecha a la cual se refiera, sin perjuicio de la presentación de una nueva certificación en caso de corresponder.

### Extracción (código A)

- **c1 Condicion** «Importe en pesos > $ 30.000 millones o pases/cauciones» — Condición de la categoría 'Grandes empresas exportadoras' (norma del encabezado del punto 7.1, que se exige concurrentemente con las demás): que el cliente mantenga un importe total de financiaciones alcanzadas en pesos en el conjunto del sistema financiero superior a $ 30.000 millones, y/o pases y/o cauciones bursátiles tomadas en pesos, cualquiera sea su importe, durante los últimos 90 días corr… · umbral: ['que supere el monto de $ 30.000 millones', 'cualquiera sea su importe durante los últimos 90 días corridos'] · tramo [exacta]: «Mantengan un importe total de financiaciones alcanzadas en pesos en el conjunto del sistema financiero que supere el monto de $ 30.000 millones, y/o pases y/o cauciones bursátiles tomadas –en pesos– cualquiera sea su importe durante los últimos 90 días corridos.»
- **d1 Definicion** «Financiaciones alcanzadas» — Son las que hayan implicado desembolsos de fondos, así como el importe no utilizado del límite de crédito asignado para adelantos en cuenta corriente; se computa su saldo de capital a fin del mes anterior al que corresponda su determinación. · props: `{"termino": "financiaciones alcanzadas"}` · tramo [exacta]: «Las financiaciones alcanzadas serán aquellas que hayan implicado desembolsos de fondos, así como el importe no utilizado del límite de crédito asignado para adelantos en cuenta corriente.»
- **o1 Obligacion** «Presentar certificación de Auditor Externo o Contador Público» — El cliente que manifestó por declaración jurada no ser 'Gran empresa exportadora' y supera $ 30.000 millones según la Central de deudores debe presentar certificación de Auditor Externo o Contador Público independiente (firma certificada por el Consejo Profesional) detallando financiaciones en pesos y moneda extranjera en el conjunto de las entidades, desagregadas por intermediario, y los pases y … · props: `{"tipo": "presentacion_informativa"}` · umbral: ['durante los últimos 90 días corridos'] · tramo [exacta]: «deberá presentar una certificación extendida por Auditor Externo o Contador Público independiente (con firma debidamente certificada por el respectivo Consejo Profesional de Ciencias Económicas) en la que se detallen las financiaciones en pesos y moneda extranjera en el conjunto de las entidades financieras, desagregan…»
- **c2 Condicion** «Declaración jurada de no encuadre y superación de $ 30.000 millones» — Supuesto de la obligación de presentar certificación: que el cliente declare por declaración jurada que no se encuadra como 'Gran empresa exportadora' y que la Central de deudores del sistema financiero muestre que supera $ 30.000 millones. · umbral: ['surja que supera el importe de $ 30.000 millones'] · tramo [exacta]: «Cuando un cliente manifieste por declaración jurada que no se encuadra en la categoría de "Gran empresa exportadora" y, de la información disponible en la "Central de deudores del sistema financiero", surja que supera el importe de $ 30.000 millones»
- **x1 Excepcion** «Excepción MiPyME — certificación» — La obligación de presentar certificación de Auditor Externo o Contador Público no se aplica cuando el cliente reúna la condición de MiPyME según las normas sobre 'Determinación de la condición de micro, pequeña y mediana empresa'. · tramo [exacta]: «Lo previsto en este párrafo no será de aplicación cuando el cliente reúna la condición de MiPyME –de acuerdo con las normas sobre "Determinación de la condición de micro, pequeña y mediana empresa"–.»
- R: c2 Condicion —condicion_de→ o1 Obligacion
- R: x1 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: o1 Obligacion —aplica_a→ Sujeto_cliente (mención «un cliente»)
- Omisión `fuera_de_tipos` [no]: «Esa certificación mantendrá vigencia durante 90 días corridos desde la fecha a la cual se refiera, sin perjuicio de la presentación de una nueva certificación en caso de correspondiente.» — Vigencia de la certificación (90 días corridos): atributo de la certificación, no es deber, prohibición ni facultad; se recogió en la descripción de la Obligacion o1. Habría sido un atributo de Obliga…

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «financiaciones de más de $ 30.000 millones» | `sin_relacion` | norma_en_heredado | c1 Condicion con el umbral, sin relación; la norma («Se encuentran comprendidos… que reúnan concurrentemente las siguientes condiciones») está en el texto heredado |
| 2 | «pases o cauciones en 90 días» | `sin_relacion` | norma_en_heredado | la misma c1 Condicion (segundo umbral «durante los últimos 90 días corridos»), sin relación; norma en el heredado |
| 3 | «declaración jurada contra la Central de deudores» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ o1 Obligacion |
| 4 | «MiPyME» | `condicion_con_relacion` |  | x1 Excepcion —exceptua_obligacion→ o1 Obligacion (cláusula de excepción) |

## `polcre::7.1::cierre` — [bloque cierre] Clientes comprendidos.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Financiaciones a "Grandes empresas exportadoras".
> *heredado:* 7.1. Clientes comprendidos.
> *propio:* Cuando el cliente reúna la condición del punto 7.1.1. pero el importe total de sus financiaciones en pesos en el sistema financiero no supere el importe de $ 30.000 millones y no haya mantenido pases y/o cauciones bursátiles tomadas –en pesos– durante los últimos 90 días corridos, la entidad financiera podrá otorgarle nuevas financiaciones en la medida que con tales desembolsos no se supere ese importe. Cuando se trate de conjuntos económicos se los considerará como un solo cliente, a cuyo efecto será de aplicación el punto 1.2.2. de las normas sobre "Grandes exposiciones al riesgo de crédito". A los fines de la imputación de las financiaciones, será de aplicación lo previsto en las normas sobre "Grandes exposiciones al riesgo de crédito".

### Extracción (código A)

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

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «reúne 7.1.1» | `dentro_de_norma` |  | dentro de la Potestad p1 y de la Operacion op1 (descripción «cliente que reúne la condición del punto 7.1.1.»); sin Condicion |
| 2 | «no supera $ 30.000 millones» | `condicion_con_relacion` |  | c1 Condicion con el umbral —condicion_de→ p1 Potestad |
| 3 | «sin pases» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ p1 Potestad |
| 4 | «desembolsos que no superen el importe» | `dentro_de_norma` |  | extraído como norma de otro tipo: r1 Restriccion con el umbral —limita→ op1; también dentro de p1; sin Condicion |
| 5 | «conjuntos económicos» | `dentro_de_norma` |  | extraído como Definicion d1; sin Condicion |

## `pro::2.3.5.1` — Todo importe cobrado o adeudado de cualquier forma al usuario de servicios fi-

Grupos: grupo_c.

### Texto

> *heredado:* Sección 2. Derechos básicos de los usuarios de servicios financieros.
> *heredado:* 2.3. Recaudos mínimos de la relación de consumo.
> *heredado:* 2.3.5. Reintegro de importes.
> *propio:* 2.3.5.1. Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: i) tasas de interés, comisiones y/o cargos sin el cumplimiento de lo previsto en los puntos 2.3.2. a 2.3.4.; ii) cargos en exceso de los costos de los servicios que terceros les cobraron a los sujetos obligados en relación con servicios prestados a los usuarios y/o de los precios que el tercero prestador perciba de particulares en general; iii) comisiones en exceso de las máximas fijadas por el BCRA que sean de aplicación; iv) en incumplimiento al nivel de la tasa de interés máxima aplicable a financiaciones vinculadas a tarjetas de crédito previstas en el texto ordenado sobre Tasas de Interés en las Operaciones de Crédito; v) en exceso de lo oportunamente pactado entre el usuario y el sujeto obligado; vi) otros generados en forma impropia por su naturaleza, tales como intereses compensatorios por saldos deudores generados en cuentas de depósito distintas de la cuenta corriente bancaria; vii) así como los importes adeudados al usuario por haber liquidado en forma incorrecta promociones, descuentos u otro tipo de beneficios –es decir, que no se ajustan a los términos, condiciones y/o modalidades que hubieran sido ofrecidos, publicitados o convenidos–; deberá serle reintegrado dentro de: - los diez (10) días hábiles siguientes al momento de la presentación del reclamo ante el sujeto obligado, de conformidad con las previsiones del punto 3.1.6.; o - los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por el sujeto obligado o por la fiscalización que realice la SEFYC. Ello, sin perjuicio de las sanciones que pudieran corresponder. En tales situaciones, corresponderá reconocer el importe de los gastos que resulten razonables realizados para la obtención del reintegro y, en todos los casos, los intereses compensatorios pertinentes, computados desde la fecha del cobro indebido hasta la de su efectiva devolución. A ese efecto, el sujeto obligado deberá aplicar 1,5 veces la tasa promedio correspondiente al período comprendido entre el momento en que la citada diferencia hubiera sido exigible –fecha en la que se cobraron los importes objeto del reclamo– y el de su efectiva cancelación, computado a partir de la encuesta diaria de tasas de interés de depósitos a plazo fijo de 30 a 59 días –de pesos o dólares estadounidenses, según la moneda de la operación– informada por el BCRA sobre la base de la información provista por la totalidad de bancos públicos y privados. Cuando la tasa correspondiente a tal encuesta no estuviera disponible, se deberá tomar la última informada. Cuando el usuario posea en la entidad financiera obligada una cuenta a la vista que se halle abierta a su nombre, ésta deberá acreditar ese importe en dicha cuenta en forma automática sin necesidad de requerimiento expreso. Si ello no fuera posible o no se tratare de una entidad financiera, el importe del reintegro deberá ser acreditado en una tarjeta de crédito de su titularidad o detraído del saldo vigente de la financiación que lo generó. Deberá notificarse la acreditación del reintegro o, en su caso, su puesta a disposición mediante aviso efectuado a través de medios electrónicos –cajeros automáticos, banca por Internet (home banking), etc.– y/o servicios telefónicos –tales como mensajes de texto y/o voz– y: a) documento escrito dirigido a su domicilio –en forma separada de cualquier otra información que se le remita (resúmenes de cuenta, boletines informativos, etc.), aun cuando forme parte de la misma remesa–; o b) a su correo electrónico –en aquellos casos en que hubiere expresamente aceptado esa forma de notificación–. Estas disposiciones serán de aplicación a los efectos de dar cumplimiento a acuerdos extrajudiciales homologados, acuerdos homologados por acciones colectivas (artículo 54 de la Ley 24.240) o sentencias judiciales, en la medida en que no se opongan a lo previsto en esos acuerdos o a lo dispuesto por los poderes públicos de las distintas jurisdicciones. Adicionalmente, el sujeto obligado deberá verificar si este tipo de situaciones que generan la obligación de reintegros ha ocurrido respecto de los usuarios que se encuentren en la misma situación y, de corresponder, proceder a su reintegro según el procedimiento previsto en este punto, notificando de tal circunstancia y resultados a su Responsable de Atención al Usuario de Servicios Financieros.

### Extracción (código A)

- **op1 Operacion** «Reintegro de importes cobrados indebidamente al usuario» — Reintegro al usuario de importes cobrados o adeudados indebidamente por tasas, comisiones o cargos sin cumplir los puntos 2.3.2. a 2.3.4., cargos en exceso de costos de terceros, comisiones por encima de las máximas del BCRA, incumplimiento de la tasa máxima en tarjetas de crédito, excesos sobre lo pactado, cargos impropios por su naturaleza e importes adeudados por promociones, descuentos o benef… · props: `{"tipo": "reintegro"}` · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos»
- **ob1 Obligacion** «Reintegro en 10 días hábiles del reclamo o 5 de constatado» — Reintegrar al usuario el importe indebido dentro de los diez días hábiles de presentado el reclamo ante el sujeto obligado, o dentro de los cinco días hábiles de constatada la circunstancia por el sujeto obligado o por la SEFYC; sin perjuicio de las sanciones que pudieran corresponder · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «deberá serle reintegrado dentro de: - los diez (10) días hábiles siguientes al momento de la presentación del reclamo ante el sujeto obligado, de conformidad con las previsiones del punto 3.1.6.; o - los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por el sujeto obligado o por la fiscal…»
- **ob2 Obligacion** «Reconocer gastos razonables e intereses compensatorios» — Reconocer al usuario los gastos razonables realizados para obtener el reintegro y, en todos los casos, los intereses compensatorios desde la fecha del cobro indebido hasta la efectiva devolución · props: `{"tipo": "calculo"}` · tramo [exacta]: «corresponderá reconocer el importe de los gastos que resulten razonables realizados para la obtención del reintegro y, en todos los casos, los intereses compensatorios pertinentes, computados desde la fecha del cobro indebido hasta la de su efectiva devolución»
- **ob3 Obligacion** «Intereses a 1,5 veces la tasa promedio plazo fijo» — Aplicar 1,5 veces la tasa promedio del período entre la exigibilidad de la diferencia y su efectiva cancelación, computada a partir de la encuesta diaria de tasas de depósitos a plazo fijo de 30 a 59 días (pesos o dólares según la moneda de la operación) informada por el BCRA con información de la totalidad de bancos públicos y privados · props: `{"tipo": "calculo"}` · umbral: ['1,5 veces la tasa promedio correspondiente al período comprendido entre el momen…'] · tramo [exacta]: «el sujeto obligado deberá aplicar 1,5 veces la tasa promedio correspondiente al período comprendido entre el momento en que la citada diferencia hubiera sido exigible»
- **ob4 Obligacion** «Tomar la última tasa informada si no hay encuesta» — Tomar la última tasa informada cuando la tasa de la encuesta del BCRA no estuviera disponible · props: `{"tipo": "calculo"}` · tramo [exacta]: «Cuando la tasa correspondiente a tal encuesta no estuviera disponible, se deberá tomar la última informada.»
- **c4 Condicion** «Tasa de la encuesta no disponible» — La tasa de la encuesta diaria de depósitos a plazo fijo no está disponible · tramo [exacta]: «Cuando la tasa correspondiente a tal encuesta no estuviera disponible»
- **ob5 Obligacion** «Acreditar automáticamente en cuenta a la vista» — Acreditar el importe del reintegro en forma automática, sin requerimiento expreso, en la cuenta a la vista abierta a nombre del usuario en la entidad financiera obligada · props: `{"tipo": "asignacion"}` · tramo [exacta]: «ésta deberá acreditar ese importe en dicha cuenta en forma automática sin necesidad de requerimiento expreso»
- **c5 Condicion** «Usuario con cuenta a la vista en la entidad» — El usuario posee en la entidad financiera obligada una cuenta a la vista abierta a su nombre · tramo [exacta]: «Cuando el usuario posea en la entidad financiera obligada una cuenta a la vista que se halle abierta a su nombre»
- **ob6 Obligacion** «Reintegro en tarjeta o detracción del saldo financiado» — Acreditar el reintegro en una tarjeta de crédito del usuario o detraerlo del saldo vigente de la financiación que lo generó · props: `{"tipo": "asignacion"}` · tramo [exacta]: «el importe del reintegro deberá ser acreditado en una tarjeta de crédito de su titularidad o detraído del saldo vigente de la financiación que lo generó»
- **c6 Condicion** «Acreditación en cuenta imposible o no es entidad financiera» — No es posible acreditar en cuenta a la vista o el sujeto obligado no es una entidad financiera · tramo [exacta]: «Si ello no fuera posible o no se tratare de una entidad financiera»
- **ob7 Obligacion** «Notificar acreditación del reintegro» — Notificar al usuario la acreditación del reintegro o su puesta a disposición mediante aviso por medios electrónicos y/o servicios telefónicos y, además, por documento escrito al domicilio (separado de otra información) o por correo electrónico si lo aceptó expresamente · props: `{"tipo": "comunicacion_a_cliente"}` · tramo [exacta]: «Deberá notificarse la acreditación del reintegro o, en su caso, su puesta a disposición mediante aviso efectuado a través de medios electrónicos –cajeros automáticos, banca por Internet (home banking), etc.– y/o servicios telefónicos –tales como mensajes de texto y/o voz– y:»
- **ob8 Obligacion** «Verificar casos análogos y reintegrar a otros usuarios» — Verificar si las situaciones que generan reintegros ocurrieron respecto de usuarios en la misma situación, reintegrar si corresponde según el procedimiento del punto y notificar circunstancia y resultados al Responsable de Atención al Usuario de Servicios Financieros · props: `{"tipo": "otra"}` · tramo [exacta]: «el sujeto obligado deberá verificar si este tipo de situaciones que generan la obligación de reintegros ha ocurrido respecto de los usuarios que se encuentren en la misma situación y, de corresponder, proceder a su reintegro según el procedimiento previsto en este punto, notificando de tal circunstancia y resultados a …»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion
- R: ob5 Obligacion —regula→ op1 Operacion
- R: ob6 Obligacion —regula→ op1 Operacion
- R: ob7 Obligacion —regula→ op1 Operacion
- R: ob8 Obligacion —regula→ op1 Operacion
- R: c4 Condicion —condicion_de→ ob4 Obligacion
- R: c5 Condicion —condicion_de→ ob5 Obligacion
- R: c6 Condicion —condicion_de→ ob6 Obligacion
- R: ob1 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- R: ob2 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «sujeto obligado»)
- R: ob3 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- R: ob5 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera obligada»)
- R: ob6 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «sujeto obligado»)
- R: ob7 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «sujeto obligado»)
- R: ob8 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- Omisión `fuera_de_tipos` [exacta]: «Ello, sin perjuicio de las sanciones que pudieran corresponder.» — Salvedad sobre consecuencias de un incumplimiento: no nombra al sujeto que las aplica; se habría usado Potestad. No altera el deber de reintegro.
- Omisión `fuera_de_tipos` [exacta]: «Estas disposiciones serán de aplicación a los efectos de dar cumplimiento a acuerdos extrajudiciales homologados, acuerdos homologados por acciones colectivas (artículo 54 de la Ley 24.240) o sentencias judiciales, en la medida en que no se opongan a lo previsto en esos acuerdos o a lo dispuesto por los poderes público…» — Cláusula de alcance/aplicación supletoria a acuerdos y sentencias; no encaja en ningún tipo sin sujeto nombrado (habría sido Condicion o alcance de la norma).

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «conceptos i) a vii)» (i)) | `dentro_de_norma` |  | dentro de la Operacion op1 (descripción: los conceptos enumerados) y de la Obligacion ob1; sin Condicion por concepto |
| 2 | «conceptos i) a vii)» (ii)) | `dentro_de_norma` |  | dentro de la Operacion op1 (descripción: los conceptos enumerados) y de la Obligacion ob1; sin Condicion por concepto |
| 3 | «conceptos i) a vii)» (iii)) | `dentro_de_norma` |  | dentro de la Operacion op1 (descripción: los conceptos enumerados) y de la Obligacion ob1; sin Condicion por concepto |
| 4 | «conceptos i) a vii)» (iv)) | `dentro_de_norma` |  | dentro de la Operacion op1 (descripción: los conceptos enumerados) y de la Obligacion ob1; sin Condicion por concepto |
| 5 | «conceptos i) a vii)» (v)) | `dentro_de_norma` |  | dentro de la Operacion op1 (descripción: los conceptos enumerados) y de la Obligacion ob1; sin Condicion por concepto |
| 6 | «conceptos i) a vii)» (vi)) | `dentro_de_norma` |  | dentro de la Operacion op1 (descripción: los conceptos enumerados) y de la Obligacion ob1; sin Condicion por concepto |
| 7 | «conceptos i) a vii)» (vii)) | `dentro_de_norma` |  | dentro de la Operacion op1 (descripción: los conceptos enumerados) y de la Obligacion ob1; sin Condicion por concepto |
| 8 | «plazo por reclamo» | `dentro_de_norma` |  | dentro de la Obligacion ob1 (umbral «los diez (10) días hábiles…»); sin Condicion |
| 9 | «por constatación» | `dentro_de_norma` |  | dentro de la Obligacion ob1 (umbral «los cinco (5) días hábiles…»); sin Condicion |
| 10 | «tasa no disponible» | `condicion_con_relacion` |  | c4 Condicion «Tasa de la encuesta no disponible» —condicion_de→ ob4 Obligacion |
| 11 | «cuenta a la vista» | `condicion_con_relacion` |  | c5 Condicion —condicion_de→ ob5 Obligacion |
| 12 | «si no fuera posible» | `condicion_con_relacion` |  | c6 Condicion —condicion_de→ ob6 Obligacion |

## `pro::2.7::intro` — [bloque intro] Revocación de la aceptación y rescisión de relaciones contractuales.

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Derechos básicos de los usuarios de servicios financieros.
> *heredado:* 2.7. Revocación de la aceptación y rescisión de relaciones contractuales.
> *propio:* Los sujetos obligados deberán contar con sendos hipervínculos que permitan al usuario:

### Extracción (código A)

(sin entidades ni omisiones)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:3 | sí | «que permitan al usuario» | `ausente` |  | salida sin entidades ni omisiones en la unidad |

## `pro::3.1.3` — Registro Centralizado de Consultas y Reclamos (RCCR).

Grupos: grupo_c.

### Texto

> *heredado:* Sección 3. Servicio de atención al usuario de servicios financieros.
> *heredado:* Los sujetos obligados deberán establecer este servicio para dar tratamiento y resolver las consultas y reclamos que presenten los usuarios de servicios financieros, observando las normas legales, reglamentarias y disposiciones vigentes en materia de protección al usuario de servicios financieros, adoptando acciones que reduzcan su reiteración.
> *heredado:* 3.1. Requisitos mínimos.
> *propio:* 3.1.3. Registro Centralizado de Consultas y Reclamos (RCCR). Se deberán asentar en una base de datos única y centralizada todas las presentaciones (consultas o reclamos) recibidas de los usuarios de servicios financieros, independientemente del medio a través del cual fueron canalizadas y de la casa receptora. Las consultas y/o reclamos que deben ser asentados en el RCCR son aquellos que, para su respuesta al cliente, requieren del análisis de la documentación obrante en el sujeto obligado y/o del pedido de información y/o documentación a otros sujetos u organismos, de manera tal que no se puede dar la respuesta en forma inmediata. También deben ser asentados en el mencionado registro aquellos reclamos que representan una queja por presunto incumplimiento, prestación defectuosa o falta de prestación de un producto o servicio ofrecido por el sujeto obligado, aun cuando pueda dárseles respuesta en forma inmediata. Deberán consignarse como mínimo los siguientes datos: número de consulta o reclamo; fecha, canal y motivo de la presentación; tipo y número de documento de identificación del presentante; casa receptora y afectada/s; otra/s entidad/es involucrada/s y el estado del trámite, el cual deberá mantenerse actualizado (pendiente de respuesta, con respuesta provisoria o definitiva al presentante, junto con la respuesta brindada, etc.). Los números asignados a las presentaciones deberán ser correlativos y la base de datos sólo podrá ser modificada para la incorporación de nuevas consultas o reclamos, o para el agregado de nueva información sobre el estado actualizado de los trámites. Cuando la consulta o el reclamo sea iniciada/o llamando a una línea o central telefónica o ingresando datos en una página de Internet, habilitadas para ese fin, el número de consulta o reclamo deberá ser provisto en el acto al presentante, respetando la correlatividad citada. Para los casos en que el presentante no reciba automáticamente el número de su consulta o reclamo, se deberá establecer un procedimiento que prevea la notificación del número o código que le sea asignado dentro de los tres (3) días hábiles de iniciada la presentación ante el sujeto obligado. La información incorporada a esta base de datos deberá conservarse por el término de diez (10) años.

### Extracción (código A)

- **op1 Operacion** «Asentamiento en el RCCR de consultas y reclamos» — Asentar en una base de datos única y centralizada (RCCR) las presentaciones (consultas o reclamos) recibidas de los usuarios de servicios financieros, independientemente del medio de canalización y de la casa receptora. · props: `{"tipo": "otra"}` · tramo [exacta]: «Se deberán asentar en una base de datos única y centralizada todas las presentaciones (consultas o reclamos) recibidas de los usuarios de servicios financieros»
- **ob1 Obligacion** «Asentar presentaciones en base única y centralizada (RCCR)» — Asentar en una base de datos única y centralizada todas las presentaciones (consultas o reclamos) recibidas de los usuarios, independientemente del medio y de la casa receptora. · props: `{"tipo": "otra"}` · tramo [exacta]: «Se deberán asentar en una base de datos única y centralizada todas las presentaciones (consultas o reclamos) recibidas de los usuarios de servicios financieros, independientemente del medio a través del cual fueron canalizadas y de la casa receptora.»
- **ob2 Obligacion** «Asentar consultas y reclamos sin respuesta inmediata» — Deben asentarse en el RCCR las consultas y/o reclamos que requieren análisis de documentación del sujeto obligado y/o pedido de información a otros sujetos u organismos, de modo que no pueden responderse de inmediato. · props: `{"tipo": "otra"}` · tramo [exacta]: «Las consultas y/o reclamos que deben ser asentados en el RCCR son aquellos que, para su respuesta al cliente, requieren del análisis de la documentación obrante en el sujeto obligado y/o del pedido de información y/o documentación a otros sujetos u organismos, de manera tal que no se puede dar la respuesta en forma inm…»
- **ob3 Obligacion** «Asentar reclamos por queja aunque haya respuesta inmediata» — Deben asentarse en el RCCR los reclamos que representan una queja por presunto incumplimiento, prestación defectuosa o falta de prestación de un producto o servicio, aun cuando pueda darse respuesta inmediata. · props: `{"tipo": "otra"}` · tramo [exacta]: «También deben ser asentados en el mencionado registro aquellos reclamos que representan una queja por presunto incumplimiento, prestación defectuosa o falta de prestación de un producto o servicio ofrecido por el sujeto obligado, aun cuando pueda dárseles respuesta en forma inmediata.»
- **ob4 Obligacion** «Consignar datos mínimos de cada presentación» — Consignar como mínimo: número de consulta o reclamo; fecha, canal y motivo; tipo y número de documento del presentante; casa receptora y afectada/s; otra/s entidad/es involucrada/s y estado del trámite. · props: `{"tipo": "otra"}` · tramo [exacta]: «Deberán consignarse como mínimo los siguientes datos: número de consulta o reclamo; fecha, canal y motivo de la presentación; tipo y número de documento de identificación del presentante; casa receptora y afectada/s; otra/s entidad/es involucrada/s y el estado del trámite»
- **ob5 Obligacion** «Mantener actualizado el estado del trámite» — El estado del trámite debe mantenerse actualizado (pendiente de respuesta, con respuesta provisoria o definitiva, junto con la respuesta brindada, etc.). · props: `{"tipo": "otra"}` · tramo [exacta]: «el cual deberá mantenerse actualizado (pendiente de respuesta, con respuesta provisoria o definitiva al presentante, junto con la respuesta brindada, etc.)»
- **ob6 Obligacion** «Numeración correlativa de presentaciones» — Los números asignados a las presentaciones deben ser correlativos. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «Los números asignados a las presentaciones deberán ser correlativos»
- **r1 Restriccion** «Base RCCR modificable solo para incorporar consultas o estado» — La base de datos solo puede modificarse para incorporar nuevas consultas o reclamos o agregar información sobre el estado actualizado de los trámites. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «la base de datos sólo podrá ser modificada para la incorporación de nuevas consultas o reclamos, o para el agregado de nueva información sobre el estado actualizado de los trámites»
- **c1 Condicion** «Inicio por línea telefónica o página de Internet» — La consulta o reclamo se inicia llamando a una línea o central telefónica o ingresando datos en una página de Internet habilitadas para ese fin. · tramo [exacta]: «Cuando la consulta o el reclamo sea iniciada/o llamando a una línea o central telefónica o ingresando datos en una página de Internet, habilitadas para ese fin»
- **ob7 Obligacion** «Proveer número en el acto al presentante» — Proveer en el acto al presentante el número de consulta o reclamo, respetando la correlatividad. · props: `{"tipo": "comunicacion_a_cliente"}` · tramo [exacta]: «el número de consulta o reclamo deberá ser provisto en el acto al presentante, respetando la correlatividad citada»
- **c2 Condicion** «Presentante sin número automático» — El presentante no recibe automáticamente el número de su consulta o reclamo. · tramo [exacta]: «Para los casos en que el presentante no reciba automáticamente el número de su consulta o reclamo»
- **ob8 Obligacion** «Notificar número en 3 días hábiles» — Establecer un procedimiento que prevea la notificación del número o código asignado dentro de los tres días hábiles de iniciada la presentación. · props: `{"tipo": "comunicacion_a_cliente"}` · umbral: ['dentro de los tres (3) días hábiles de iniciada la presentación'] · tramo [exacta]: «se deberá establecer un procedimiento que prevea la notificación del número o código que le sea asignado dentro de los tres (3) días hábiles de iniciada la presentación ante el sujeto obligado»
- **ob9 Obligacion** «Conservar la información 10 años» — Conservar la información incorporada a la base de datos por diez años. · props: `{"tipo": "otra"}` · umbral: ['por el término de diez (10) años'] · tramo [exacta]: «La información incorporada a esta base de datos deberá conservarse por el término de diez (10) años.»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion
- R: ob4 Obligacion —regula→ op1 Operacion
- R: r1 Restriccion —limita→ op1 Operacion
- R: c1 Condicion —condicion_de→ ob7 Obligacion
- R: c2 Condicion —condicion_de→ ob8 Obligacion
- R: ob1 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «sujeto obligado»)
- R: ob2 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «sujeto obligado»)
- R: ob3 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «sujeto obligado»)
- R: ob8 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «sujeto obligado»)
- R: Sujeto_rol_sujeto_obligado_proteccion (mención «sujeto obligado») —ejecuta→ op1 Operacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «presentación por teléfono o Internet» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ ob7 Obligacion |
| 2 | «presentante que no recibe el número automáticamente» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ ob8 Obligacion |

## `pro::3.2.3.5` — Los reportes del Directivo Responsable de Protección de los Usuarios de Ser-

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Servicio de atención al usuario de servicios financieros.
> *heredado:* Los sujetos obligados deberán establecer este servicio para dar tratamiento y resolver las consultas y reclamos que presenten los usuarios de servicios financieros, observando las normas legales, reglamentarias y disposiciones vigentes en materia de protección al usuario de servicios financieros, adoptando acciones que reduzcan su reiteración.
> *heredado:* 3.2. Controles.
> *heredado:* 3.2.3. Del Banco Central de la República Argentina.
> *heredado:* En la sede en la cual desempeñe sus funciones el responsable de atención al usuario de servicios financieros (titular o suplente a cargo) deberán encontrarse a disposición del BCRA:
> *propio:* 3.2.3.5. Los reportes del Directivo Responsable de Protección de los Usuarios de Servicios Financieros o del Comité de Protección de los Usuarios de Servicios Financieros, según corresponda.

### Extracción (código A)

- **o1 Obligacion** «Reportes Directivo/Comité Protección a disposición del BCRA» — Deben encontrarse a disposición del BCRA, en la sede en que el responsable de atención al usuario (titular o suplente a cargo) desempeña sus funciones, los reportes del Directivo Responsable de Protección de los Usuarios de Servicios Financieros o del Comité de Protección de los Usuarios de Servicios Financieros, según corresponda. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «En la sede en la cual desempeñe sus funciones el responsable de atención al usuario de servicios financieros (titular o suplente a cargo) deberán encontrarse a disposición del BCRA: […] Los reportes del Directivo Responsable de Protección de los Usuarios de Servicios Financieros o del Comité de Protección de los Usuari…»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:5 | no | «según corresponda» | `extraida_tramo_verificado` |  | o1 Obligacion [exacta], tramo que contiene «según corresponda» |

## `ric::12.4` — Suspensión de la observancia de las regulaciones técnicas sobre base consolidada

Grupos: omisiones.

### Texto

> *heredado:* Sección 12. Disposiciones transitorias.
> *propio:* 12.4. Suspensión de la observancia de las regulaciones técnicas sobre base consolidada trimestral (punto 6.1. de las normas sobre "Supervisión consolidada"). A partir del período de información abril/24: - Se suspende el envío de informaciones con código de consolidación 3 -con la excepción prevista para Ratio de apalancamiento-, siendo marzo/24 el último período trimestral que corresponde informar con este nivel de consolidación; - En la información sobre base consolidada mensual (códigos de consolidación 2 ó 9) se incluirán -de corresponderlas operaciones de los entes a que refieren los incisos i), ii) y iii) del primer párrafo del punto 6.2. de las normas sobre "Supervisión consolidada. - Las entidades financieras que hasta el 31/03/24 informaban únicamente códigos de consolidación 1 y 3, de mantenerse esta situación de consolidación, pasarán a informar: a) códigos 1 y 9 sólo si consolidan con alguno de los entes a que refieren los incisos i), ii) y iii) del punto 6.2. de las normas citadas; b) en caso contrario, código 0. - Ratio de apalancamiento (Sección 10.) a) Conforme a lo dispuesto en el punto 6.2. último párrafo de las normas sobre "Supervisión consolidada", mantendrá su frecuencia trimestral (datos del mes de cierre de trimestre) y su vencimiento según punto 1.1. del Régimen Informativo para Supervisión; b) Se continuará informando código de consolidación 3; no obstante, las operaciones a incluir serán las que correspondan al perímetro de consolidación mensual, considerando de corresponder, los sujetos previstos en el punto 6.2. de las normas citadas. - Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5.) y Riesgo de tasa de interés en la cartera de inversión (Sección 11.) De corresponder, la consolidación mensual (código 2) considerará las operaciones de los entes a que refieren los incisos i), ii) y iii) del primer párrafo del punto 6.2. de las normas sobre "Supervisión consolidada".

### Extracción (código A)

- **op1 Operacion** «Envío de informaciones con código de consolidación 3» — Envío de informaciones sobre base consolidada trimestral con código de consolidación 3, con la excepción prevista para Ratio de apalancamiento · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «el envío de informaciones con código de consolidación 3»
- **ex1 Excepcion** «Suspensión envío código 3 desde abril/24» — A partir del período abril/24 se suspende el envío de informaciones con código de consolidación 3 (base consolidada trimestral, punto 6.1. de Supervisión consolidada); marzo/24 es el último período trimestral a informar con ese nivel. Exceptúa el deber de informar con código 3, salvo Ratio de apalancamiento. · tramo [exacta]: «Se suspende el envío de informaciones con código de consolidación 3 -con la excepción prevista para Ratio de apalancamiento-, siendo marzo/24 el último período trimestral que corresponde informar con este nivel de consolidación»
- **ob1 Obligacion** «Incluir operaciones de entes incisos i), ii) y iii) en consolidación mensual» — A partir del período abril/24, en la información sobre base consolidada mensual (códigos 2 ó 9) se incluyen, de corresponder, las operaciones de los entes de los incisos i), ii) y iii) del primer párrafo del punto 6.2. de Supervisión consolidada · props: `{"tipo": "presentacion_informativa", "frecuencia": "mensual"}` · tramo [exacta]: «En la información sobre base consolidada mensual (códigos de consolidación 2 ó 9) se incluirán -de corresponderlas operaciones de los entes a que refieren los incisos i), ii) y iii) del primer párrafo del punto 6.2. de las normas sobre "Supervisión consolidada.»
- **ob2 Obligacion** «Informar códigos 1 y 9 si consolidan con entes i), ii), iii)» — Las entidades financieras que hasta el 31/03/24 informaban únicamente códigos de consolidación 1 y 3, de mantenerse esa situación, pasan a informar códigos 1 y 9 sólo si consolidan con alguno de los entes de los incisos i), ii) y iii) del punto 6.2. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Las entidades financieras que hasta el 31/03/24 informaban únicamente códigos de consolidación 1 y 3, de mantenerse esta situación de consolidación, pasarán a informar: a) códigos 1 y 9 sólo si consolidan con alguno de los entes a que refieren los incisos i), ii) y iii) del punto 6.2. de las normas citadas»
- **c2 Condicion** «Consolida con alguno de los entes i), ii), iii)» — La entidad consolida con alguno de los entes a que refieren los incisos i), ii) y iii) del punto 6.2. de Supervisión consolidada · tramo [exacta]: «sólo si consolidan con alguno de los entes a que refieren los incisos i), ii) y iii) del punto 6.2. de las normas citadas»
- **ob3 Obligacion** «Informar código 0 si no consolidan con esos entes» — Las entidades financieras que hasta el 31/03/24 informaban únicamente códigos 1 y 3, de mantenerse esa situación, pasan a informar código 0 si no consolidan con los entes de los incisos i), ii) y iii) del punto 6.2. · props: `{"tipo": "presentacion_informativa"}` · tramo [no]: «Las entidades financieras que hasta el 31/03/24 informaban únicamente códigos de consolidación 1 y 3, de mantenerse esta situación de consolidación, pasarán a informar: b) en caso contrario, código 0.»
- **c3 Condicion** «No consolida con los entes i), ii), iii)» — La entidad no consolida con ninguno de los entes a que refieren los incisos i), ii) y iii) del punto 6.2. · tramo [exacta]: «en caso contrario»
- **ob4 Obligacion** «Ratio de apalancamiento: frecuencia trimestral y vencimiento» — El Ratio de apalancamiento (Sección 10.) mantiene su frecuencia trimestral (datos del mes de cierre de trimestre) y su vencimiento según punto 1.1. del Régimen Informativo para Supervisión, conforme al punto 6.2. último párrafo de Supervisión consolidada · props: `{"tipo": "presentacion_informativa", "frecuencia": "trimestral"}` · tramo [exacta]: «mantendrá su frecuencia trimestral (datos del mes de cierre de trimestre) y su vencimiento según punto 1.1. del Régimen Informativo para Supervisión»
- **ob5 Obligacion** «Ratio de apalancamiento: seguir informando código 3 con perímetro mensual» — Ratio de apalancamiento: se continúa informando código de consolidación 3, pero las operaciones a incluir son las del perímetro de consolidación mensual, considerando de corresponder los sujetos previstos en el punto 6.2. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se continuará informando código de consolidación 3; no obstante, las operaciones a incluir serán las que correspondan al perímetro de consolidación mensual, considerando de corresponder, los sujetos previstos en el punto 6.2. de las normas citadas.»
- **ob6 Obligacion** «Datos complementarios: consolidación mensual código 2 con entes» — En los datos complementarios del cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5.) y Riesgo de tasa de interés en la cartera de inversión (Sección 11.), la consolidación mensual (código 2) considera, de corresponder, las operaciones de los entes de los incisos i), ii) y iii) del primer párrafo del punto 6.2. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «De corresponder, la consolidación mensual (código 2) considerará las operaciones de los entes a que refieren los incisos i), ii) y iii) del primer párrafo del punto 6.2. de las normas sobre "Supervisión consolidada".»
- R: c2 Condicion —condicion_de→ ob2 Obligacion
- R: c3 Condicion —condicion_de→ ob3 Obligacion
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- R: ob3 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- Omisión `fuera_de_tipos` [exacta]: «Se suspende el envío de informaciones con código de consolidación 3» — La excepción no se conecta con exceptua_obligacion porque la obligación de informar con código 3 está en otra unidad (punto 6.1. de Supervisión consolidada / otras secciones del TO), no en este chunk.

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:20 | no | «A partir del período de información abril/24» | `ausente` |  | ningún tramo contiene «A partir del período de información abril/24»; ex1 lo lleva en la descripción |

## `ric::3.1.7` — Exigencia de capital por riesgo de crédito de contraparte en operaciones con en-

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Exigencia por riesgo de crédito
> *heredado:* 3.1. Normas de procedimiento.
> *propio:* 3.1.7. Exigencia de capital por riesgo de crédito de contraparte en operaciones con entidades de contraparte central Las exposiciones de las entidades financieras con entidades de contraparte central con el alcance establecido en el punto 4.3. de las normas sobre "Capitales mínimos de las entidades financieras" –determinadas conforme a dichas normas-, se consignarán en la partida 12500000 por cada ponderador que corresponda aplicar, siguiendo el modelo de información inserto en el punto 3.1.4..

### Extracción (código A)

- **e1 Obligacion** «Consignación exposiciones con ECC en partida 12500000» — Las exposiciones de las entidades financieras con entidades de contraparte central, con el alcance del punto 4.3. de las normas de Capitales mínimos y determinadas conforme a ellas, se consignan en la partida 12500000 por cada ponderador aplicable, siguiendo el modelo de información del punto 3.1.4. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Las exposiciones de las entidades financieras con entidades de contraparte central con el alcance establecido en el punto 4.3. de las normas sobre "Capitales mínimos de las entidades financieras" –determinadas conforme a dichas normas-, se consignarán en la partida 12500000 por cada ponderador que corresponda aplicar, …»
- **e2 Operacion** «Exigencia de capital por riesgo de crédito de contraparte con ECC» — Exposiciones de entidades financieras con entidades de contraparte central, determinadas conforme a las normas de Capitales mínimos (punto 4.3.), consignadas por ponderador · props: `{"tipo": "otra"}` · tramo [exacta]: «Exigencia de capital por riesgo de crédito de contraparte en operaciones con entidades de contraparte central»
- R: e1 Obligacion —regula→ e2 Operacion
- R: e1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:13 | sí (remisión pura) | «siguiendo el modelo de información inserto en el punto 3.1.4.» | `extraida_tramo_verificado` |  | e1 Obligacion [exacta], tramo que contiene «siguiendo el modelo de información inserto en el punto 3.1.4.» |

## `ric::4.1.1.5` — Código 312200/xx

Grupos: omisiones.

### Texto

> *heredado:* Sección 4. Exigencia e integración por riesgo de mercado
> *heredado:* 4.1. Normas de procedimiento
> *heredado:* 4.1.1. Exigencia
> *propio:* 4.1.1.5. Código 312200/xx Se consignará el valor de la exigencia por riesgo general de acciones para el último día del período (n) determinada conforme a las disposiciones del punto 6.3. de las normas sobre "Capitales mínimos de las entidades financieras". Este riesgo se discriminará por mercado, entendido a estos efectos como el país en que se negocien posiciones -compradas o vendidasen acciones. A estos efectos, el país se identificará de acuerdo con la codificación del Country Codes del SWIFT.

### Extracción (código A)

- **op1 Operacion** «Exigencia por riesgo general de acciones» — Exigencia por riesgo general de acciones, determinada conforme al punto 6.3. de las normas sobre Capitales mínimos de las entidades financieras, al último día del período (n) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «el valor de la exigencia por riesgo general de acciones para el último día del período (n)»
- **ob1 Obligacion** «Consignar exigencia riesgo general de acciones (312200/xx)» — Se consigna en el código 312200/xx el valor de la exigencia por riesgo general de acciones para el último día del período (n), determinada conforme al punto 6.3. de las normas sobre Capitales mínimos de las entidades financieras. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se consignará el valor de la exigencia por riesgo general de acciones para el último día del período (n) determinada conforme a las disposiciones del punto 6.3. de las normas sobre "Capitales mínimos de las entidades financieras".»
- **ob2 Obligacion** «Discriminar riesgo de acciones por mercado (país)» — El riesgo general de acciones se discrimina por mercado, entendido como el país en que se negocien posiciones, compradas o vendidas, en acciones. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Este riesgo se discriminará por mercado»
- **def1 Definicion** «Mercado (país de negociación de acciones)» — A estos efectos, el país en que se negocien posiciones, compradas o vendidas, en acciones. · props: `{"termino": "mercado"}` · tramo [exacta]: «mercado, entendido a estos efectos como el país en que se negocien posiciones -compradas o vendidasen acciones»
- **ob3 Obligacion** «Identificar país según Country Codes SWIFT» — El país se identifica de acuerdo con la codificación del Country Codes del SWIFT. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «el país se identificará de acuerdo con la codificación del Country Codes del SWIFT»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:1 | no | «Código 312200/xx» | `ausente` |  | ninguna entidad ni omisión cubre «Código 312200/xx» |

## `ric::4.5.2` — Futuros y Contratos a Término, incluidos los FRA

Grupos: grupo_c.

### Texto

> *heredado:* Sección 4. Exigencia e integración por riesgo de mercado
> *heredado:* 4.5. Información sobre instrumentos derivados
> *propio:* 4.5.2. Futuros y Contratos a Término, incluidos los FRA [TABLA ric::tabla012 | página 19 | e0_tablas | posicional] Fila 1: col1 = Descripción del activo subyacente(1) | col2 = Fecha correspondiente al plazo residual del subyacente (cuando corresponda)(2) | col3 = Vencimiento del derivado | col4 = Contraparte/Ámb ito de negociación | col5 = Valor nocional(3) | col6 = Tasa de cupón del activo subyacente (cuando corresponda)(4) | col7 = Precio pactado del subyacente (5) | col8 = Precio de mercado del activo subyacente | col9 = Compra / venta a término (6) [FIN TABLA ric::tabla012] (1) Describir el activo comprado o vendido a futuro. Por ejemplo: Tasa de interés Badlar Privada para depósitos de más de 1 millón de pesos por un plazo de 30 a 35 días, dólar estadounidense, Bono de la Nación Arg. en dólar link con vencimiento al 2017 - AJ17D, etc. (2) Por ejemplo, en un futuro sobre un título público es el plazo residual del título público subyacente. (3) Especificar el valor nocional incluyendo la moneda o unidad de medida. Por ejemplo, USD 25.000.000, $ 100.000, etc. (4) Por ejemplo, en un futuro sobre un título público, es la tasa del cupón corriente de dicho título (5) Valor del subyacente pactado. Por ejemplo, valor de la tasa fija pactada, valor pactado del dólar, valor pactado del bono, etc. (6) Consignar "C" si el contrato en cuestión es una compra a término, o "V" si es una venta a término.

### Extracción (código A)

- **op1 Operacion** «Información de futuros y contratos a término, incluidos FRA» — Presentación informativa sobre instrumentos derivados: futuros y contratos a término, incluidos los FRA, con los datos de la tabla (activo subyacente, plazo residual, vencimiento, contraparte/ámbito, valor nocional, tasa de cupón, precio pactado, precio de mercado, compra/venta). · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Futuros y Contratos a Término, incluidos los FRA»
- **ob1 Obligacion** «Informar datos del futuro o contrato a término» — Informar, por cada futuro o contrato a término (incluidos FRA): descripción del activo subyacente, fecha del plazo residual del subyacente (cuando corresponda), vencimiento del derivado, contraparte/ámbito de negociación y valor nocional (con moneda o unidad de medida). · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Descripción del activo subyacente(1) | col2 = Fecha correspondiente al plazo residual del subyacente (cuando corresponda)(2) | col3 = Vencimiento del derivado | col4 = Contraparte/Ámb ito de negociación | col5 = Valor nocional(3)»
- **ob2 Obligacion** «Informar precios, tasa de cupón y sentido C/V» — Informar, por cada futuro o contrato a término (incluidos FRA): tasa de cupón del activo subyacente (cuando corresponda), precio pactado del subyacente, precio de mercado del activo subyacente y si es compra ("C") o venta ("V") a término. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Tasa de cupón del activo subyacente (cuando corresponda)(4) | col7 = Precio pactado del subyacente (5) | col8 = Precio de mercado del activo subyacente | col9 = Compra / venta a término (6)»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- Omisión `fuera_de_tipos` [exacta]: «(1) Describir el activo comprado o vendido a futuro.» — Instrucción de cómo completar la columna (notas explicativas 1 a 6 con ejemplos); su contenido sustantivo está recogido en las obligaciones de informar. Tipo que se habría usado: Definicion o descripc…
- Omisión `fuera_de_tipos` [exacta]: «(6) Consignar "C" si el contrato en cuestión es una compra a término, o "V" si es una venta a término.» — Instrucción de codificación del campo; se recoge en la descripción de la obligación. Tipo que se habría usado: Obligacion de tipo otra.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | ««C» si es compra a término» | `dentro_de_norma` |  | dentro de la Obligacion ob2 (tramo «Consignar "C" si el contrato… es una compra a término»); sin Condicion |
| 2 | ««V» si es venta» | `dentro_de_norma` |  | dentro de la Obligacion ob2 (tramo «o "V" si es una venta a término»); sin Condicion |

## `ric::5.1.3.4` — Se informará una sola partida 3600000Y, reflejando la situación de la entidad

Grupos: omisiones.

### Texto

> *heredado:* Sección 5. Exigencia por riesgo operacional
> *heredado:* 5.1. Normas de procedimiento
> *heredado:* 5.1.3. Reducción de la exigencia para entidades financieras del Grupo 2 que pertenezcan a
> *heredado:* los Grupos "A", "B" y "C".
> *propio:* 5.1.3.4. Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación; el promedio de las exigencias por riesgo de crédito se calculará en esta Institución en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos.

### Extracción (código A)

- **op1 Operacion** «Informar partida 3600000Y» — Informar una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación (reducción de la exigencia por riesgo operacional para entidades del Grupo 2 que pertenezcan a los Grupos A, B y C). · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informará una sola partida 3600000Y»
- **ob1 Obligacion** «Informar una sola partida 3600000Y» — Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación»
- **ob2 Obligacion** «Cálculo del promedio de exigencias por riesgo de crédito» — El promedio de las exigencias por riesgo de crédito se calculará en esta Institución en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el promedio de las exigencias por riesgo de crédito se calculará en esta Institución en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob1 Obligacion —aplica_a→ Sujeto_rol_entidad_comprendida_reginf (mención «la entidad»)
- R: ob2 Obligacion —aplica_a→ Sujeto_bcra (mención «esta Institución»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:12 | sí | «reflejando la situación de la entidad respecto de su calificación» | `extraida_tramo_verificado` |  | ob1 Obligacion [exacta], tramo que contiene «reflejando la situación de la entidad respecto de su calificación» |

## `ric::6.1.2` — Conceptos deducibles del capital ordinario de nivel uno (CDCOn1) -Partida 70220000-

Grupos: grupo_c, omisiones.

### Texto

> *heredado:* Sección 6. Responsabilidad Patrimonial Computable
> *heredado:* 6.1. Normas de procedimiento
> *heredado:* La responsabilidad patrimonial computable se determinará en función de los saldos de las partidas admitidas, registrados al último día del mes bajo informe.
> *propio:* 6.1.2. Conceptos deducibles del capital ordinario de nivel uno (CDCOn1) -Partida 70220000Código 20800000. Se informarán las existencias de títulos valores, certificados de depósitos a plazo fijo, otros títulos de crédito, etc., que no se encuentren físicamente en poder de la entidad, de acuerdo con el punto 8.4.1.3. -Sección 8del texto ordenado de las normas sobre "Capitales mínimos de las entidades financieras". Código 20900000. Se incluirá el mayor saldo registrado durante el mes a que corresponde la determinación de la responsabilidad patrimonial computable, de la tenencia de títulos valores y otros instrumentos de deuda, contractualmente subordinados a los demás pasivos, emitidos por otras entidades financieras. Código 21000000. Se consignará el mayor saldo registrado durante el mes a que corresponde la determinación de la responsabilidad patrimonial computable, de las cuentas de corresponsalía con entidades financieras del exterior que no cuenten con calificación "investment grade" otorgada por alguna de las calificadoras admitidas por las normas sobre "Evaluación de entidades financieras". Código 21100000. Se incluirá el mayor saldo registrado durante el mes a que corresponde la determinación del capital ordinario de nivel 1 (COn1), de los títulos emitidos por gobiernos de países extranjeros, cuya calificación internacional sea inferior a la asignada a títulos públicos nacionales de la República Argentina, y que no cuenten con mercados donde se transen en forma habitual por valores relevantes; de acuerdo con el punto 8.4.1.4. de las normas sobre "Capitales mínimos de las entidades financieras". Código 21500000 Se detallará el 100 % del valor -neto de la depreciación acumuladade los bienes inmuebles para uso propio y diversos (incluidos en los rubros 180000 y 190000 del balance de saldos), cuya registración contable no se encuentre respaldada con la pertinente escritura traslativa de dominio debidamente inscripta en el Registro de la Propiedad Inmueble (concepto "CDCOn1"). Código 21600000 Se incluirán los activos intangibles netos de sus respectivas amortizaciones acumuladas. Comprende la llave de negocio que cumpla los requisitos establecidos en el punto 8.4.1.8. de las normas sobre "Capitales mínimos de las entidades financieras". Código 21800000. Comprende las diferencias por insuficiencia de constitución de las previsiones mínimas por riesgo de incobrabilidad determinada por la Superintendencia de Entidades Financieras y Cambiarias, en la medida en que no hayan sido contabilizadas, con efecto al cierre del mes siguiente a aquel en que la entidad reciba la notificación a que se refiere el primer párrafo del punto 2.7. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", según el punto 8.4.1.12. de las normas sobre "Capitales mínimos de las entidades financieras". Código 22000000 Comprende el valor -neto de desafectacionesde la llave negativa registrada en adquisiciones de participaciones por un costo inferior a su valor patrimonial proporcional. Esta partida se computará únicamente en la información consolidada de la adquirente o en la información individual del ente combinado (en caso de fusión entre adquirente y adquirida). Este concepto deberá considerarse con signo negativo dentro del término "CDCOn1". Código 22100000 Comprende el saldo a favor por aplicación del impuesto a la ganancia mínima presunta - neto de las previsionesque exceda el 10% del patrimonio neto básico correspondiente al mes anterior. Además, se incluirá el saldo a favor proveniente de activos por impuestos diferidos. Código 22300000 Se informarán los aportes registrados contablemente como tales cuya capitalización aún no haya sido autorizada por la SEFyC. Códigos 22510000 a 22530000 Se consignarán los excesos a los límites para la afectación de activos en garantía, según lo dispuesto en la Sección 3. de las normas sobre "Afectación de activos en garantía". Código 22600000 Se incluirán las ganancias por ventas resultantes de operaciones de titulización (deberán computarse cuando no se cumpla con los requisitos vinculados con opciones de exclusión, cuando exista respaldo implícito de titulizaciones o cuando corresponda calcular exigencia por titulizaciones con cláusulas de cancelación anticipada). También se incluirán las ganancias por operaciones de venta o cesión de cartera con responsabilidad para el cedente, computadas de acuerdo con lo establecido en el punto 8.4.1.16. de las normas sobre "Capitales mínimos de las entidades financieras". Código 22700000 Se informará el mayor saldo de la asistencia crediticia otorgada en el mes, cuando los adelantos previstos en el punto 3.2.5. de la Sección 3. de las normas sobre "Financiamiento al sector público no financiero" superen el límite autorizado y/o no sean cancelados en los plazos allí previstos. Código 26300000 Se informarán las previsiones por riesgo de incobrabilidad correspondientes a financiaciones en situación normal o cubiertas con garantías preferidas "A" que no superen el 1,25 % de los APRs. En los casos que corresponda, se computará la absorción prevista en la partida 21300000. Códigos 23400000, 23500000, 25300000, 25400000, 27300000 y 27400000 Reflejarán la deducción -para cada nivel de capital consideradode las inversiones en instrumentos computables como capital regulatorio de empresas de servicios complementarios -no sujetas a supervisión consolidaday compañías de seguro, y sus importes se informarán netos de las deducciones previstas en el cronograma del punto 11.5. de las normas sobre "Capitales mínimos de las entidades financieras". Código 21200000 Se informarán los conceptos deducibles del COn1, no incluidos en otros códigos.

### Extracción (código A)

- **c1 Comunicacion** «Capitales mínimos de las entidades financieras» —  · props: `{"codigo": "Capitales mínimos de las entidades financieras"}` · tramo [exacta]: «"Capitales mínimos de las entidades financieras"»
- **o1 Obligacion** «Informar títulos valores no en poder de la entidad (20800000)» — Código 20800000: se informarán las existencias de títulos valores, certificados de depósitos a plazo fijo, otros títulos de crédito, etc., que no se encuentren físicamente en poder de la entidad, de acuerdo con el punto 8.4.1.3. -Sección 8de Capitales mínimos. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informarán las existencias de títulos valores, certificados de depósitos a plazo fijo, otros títulos de crédito, etc., que no se encuentren físicamente en poder de la entidad»
- **o2 Obligacion** «Mayor saldo de deuda subordinada de otras entidades (20900000)» — Código 20900000: se incluirá el mayor saldo registrado durante el mes de la tenencia de títulos valores y otros instrumentos de deuda subordinados emitidos por otras entidades financieras. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se incluirá el mayor saldo registrado durante el mes a que corresponde la determinación de la responsabilidad patrimonial computable, de la tenencia de títulos valores y otros instrumentos de deuda, contractualmente subordinados a los demás pasivos, emitidos por otras entidades financieras.»
- **o3 Obligacion** «Mayor saldo corresponsalía sin investment grade (21000000)» — Código 21000000: se consignará el mayor saldo del mes de las cuentas de corresponsalía con entidades financieras del exterior sin calificación investment grade otorgada por calificadoras admitidas. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se consignará el mayor saldo registrado durante el mes a que corresponde la determinación de la responsabilidad patrimonial computable, de las cuentas de corresponsalía con entidades financieras del exterior que no cuenten con calificación "investment grade"»
- **o4 Obligacion** «Mayor saldo títulos de gobiernos extranjeros (21100000)» — Código 21100000: se incluirá el mayor saldo del mes de los títulos emitidos por gobiernos extranjeros con calificación inferior a la de los títulos públicos nacionales y sin mercados donde se transen habitualmente por valores relevantes, según punto 8.4.1.4. de Capitales mínimos. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se incluirá el mayor saldo registrado durante el mes a que corresponde la determinación del capital ordinario de nivel 1 (COn1), de los títulos emitidos por gobiernos de países extranjeros»
- **o5 Obligacion** «100 % inmuebles sin escritura inscripta (21500000)» — Código 21500000: se detallará el 100 % del valor neto de depreciación acumulada de los bienes inmuebles para uso propio y diversos (rubros 180000 y 190000) cuya registración contable no esté respaldada con escritura traslativa de dominio inscripta (concepto CDCOn1). · props: `{"tipo": "presentacion_informativa"}` · umbral: ['el 100 % del valor -neto de la depreciación acumulada-'] · tramo [exacta]: «Se detallará el 100 % del valor -neto de la depreciación acumuladade los bienes inmuebles para uso propio y diversos»
- **o6 Obligacion** «Activos intangibles netos (21600000)» — Código 21600000: se incluirán los activos intangibles netos de amortizaciones acumuladas; comprende la llave de negocio que cumpla los requisitos del punto 8.4.1.8. de Capitales mínimos. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se incluirán los activos intangibles netos de sus respectivas amortizaciones acumuladas.»
- **o7 Obligacion** «Insuficiencia de previsiones mínimas no contabilizada (21800000)» — Código 21800000: comprende las diferencias por insuficiencia de constitución de previsiones mínimas determinada por la SEFyC, en la medida en que no hayan sido contabilizadas, con efecto al cierre del mes siguiente a la notificación (punto 2.7. de Previsiones mínimas; punto 8.4.1.12. de Capitales mínimos). · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Comprende las diferencias por insuficiencia de constitución de las previsiones mínimas por riesgo de incobrabilidad determinada por la Superintendencia de Entidades Financieras y Cambiarias, en la medida en que no hayan sido contabilizadas»
- **o8 Obligacion** «Llave negativa neta de desafectaciones (22000000)» — Código 22000000: comprende el valor neto de desafectaciones de la llave negativa registrada en adquisiciones de participaciones por un costo inferior a su valor patrimonial proporcional. Se computa únicamente en la información consolidada de la adquirente o en la individual del ente combinado, con signo negativo dentro de CDCOn1. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Comprende el valor -neto de desafectacionesde la llave negativa registrada en adquisiciones de participaciones por un costo inferior a su valor patrimonial proporcional.»
- **o9 Obligacion** «Saldo a favor ganancia mínima presunta y diferidos (22100000)» — Código 22100000: saldo a favor por impuesto a la ganancia mínima presunta, neto de previsiones, que exceda el 10% del patrimonio neto básico del mes anterior; además, el saldo a favor de activos por impuestos diferidos. · props: `{"tipo": "presentacion_informativa"}` · umbral: ['que exceda el 10% del patrimonio neto básico correspondiente al mes anterior'] · tramo [exacta]: «Comprende el saldo a favor por aplicación del impuesto a la ganancia mínima presunta - neto de las previsionesque exceda el 10% del patrimonio neto básico correspondiente al mes anterior. Además, se incluirá el saldo a favor proveniente de activos por impuestos diferidos.»
- **o10 Obligacion** «Aportes no capitalizados sin autorización (22300000)» — Código 22300000: se informarán los aportes registrados contablemente cuya capitalización aún no haya sido autorizada por la SEFyC. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informarán los aportes registrados contablemente como tales cuya capitalización aún no haya sido autorizada por la SEFyC.»
- **o11 Obligacion** «Excesos límites afectación de activos en garantía (22510000-22530000)» — Códigos 22510000 a 22530000: se consignarán los excesos a los límites para la afectación de activos en garantía, según la Sección 3. de Afectación de activos en garantía. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se consignarán los excesos a los límites para la afectación de activos en garantía»
- **o12 Obligacion** «Ganancias por titulización y cesión con responsabilidad (22600000)» — Código 22600000: se incluirán las ganancias por ventas resultantes de operaciones de titulización (a computar cuando no se cumpla con requisitos de opciones de exclusión, exista respaldo implícito o corresponda calcular exigencia por cláusulas de cancelación anticipada); también las ganancias por venta o cesión de cartera con responsabilidad para el cedente, según punto 8.4.1.16. de Capitales míni… · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se incluirán las ganancias por ventas resultantes de operaciones de titulización»
- **o13 Obligacion** «Mayor saldo asistencia crediticia al sector público (22700000)» — Código 22700000: se informará el mayor saldo de la asistencia crediticia otorgada en el mes, cuando los adelantos del punto 3.2.5. de Financiamiento al sector público no financiero superen el límite autorizado y/o no sean cancelados en los plazos previstos. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informará el mayor saldo de la asistencia crediticia otorgada en el mes, cuando los adelantos previstos en el punto 3.2.5. de la Sección 3. de las normas sobre "Financiamiento al sector público no financiero" superen el límite autorizado y/o no sean cancelados en los plazos allí previstos.»
- **cd13 Condicion** «Adelantos exceden límite o no se cancelan en plazo» — Supuesto del código 22700000: los adelantos superan el límite autorizado y/o no son cancelados en los plazos previstos. · tramo [exacta]: «cuando los adelantos previstos en el punto 3.2.5. de la Sección 3. de las normas sobre "Financiamiento al sector público no financiero" superen el límite autorizado y/o no sean cancelados en los plazos allí previstos»
- **o14 Obligacion** «Previsiones financiaciones normales hasta 1,25 % APRs (26300000)» — Código 26300000: se informarán las previsiones por riesgo de incobrabilidad de financiaciones en situación normal o cubiertas con garantías preferidas A que no superen el 1,25 % de los APRs. Se computará la absorción prevista en la partida 21300000 en los casos que corresponda. · props: `{"tipo": "presentacion_informativa"}` · umbral: ['que no superen el 1,25 % de los APRs'] · tramo [exacta]: «Se informarán las previsiones por riesgo de incobrabilidad correspondientes a financiaciones en situación normal o cubiertas con garantías preferidas "A" que no superen el 1,25 % de los APRs.»
- **o15 Obligacion** «Deducción inversiones en empresas complementarias y seguros» — Códigos 23400000, 23500000, 25300000, 25400000, 27300000 y 27400000: reflejarán la deducción, para cada nivel de capital, de inversiones en instrumentos computables como capital regulatorio de empresas de servicios complementarios no sujetas a supervisión consolidada y compañías de seguro; importes netos de las deducciones del cronograma del punto 11.5. de Capitales mínimos. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Reflejarán la deducción -para cada nivel de capital consideradode las inversiones en instrumentos computables como capital regulatorio de empresas de servicios complementarios -no sujetas a supervisión consolidaday compañías de seguro»
- **o16 Obligacion** «Otros conceptos deducibles del COn1 (21200000)» — Código 21200000: se informarán los conceptos deducibles del COn1 no incluidos en otros códigos. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informarán los conceptos deducibles del COn1, no incluidos en otros códigos.»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: cd13 Condicion —condicion_de→ o13 Obligacion
- Omisión `fuera_de_tipos` [exacta]: «Esta partida se computará únicamente en la información consolidada de la adquirente o en la información individual del ente combinado (en caso de fusión entre adquirente y adquirida).» — Alcance de la partida 22000000, incorporado en la descripción de o8; no hay sujeto nombrado con catálogo.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «código 22600000 (tres «cuando»)» (opciones de exclusión) | `dentro_de_norma` |  | dentro de la Obligacion o12 (descripción: «a computar cuando no se cumpla con requisitos de opciones de exclusión…»); sin Condicion |
| 2 | «código 22600000 (tres «cuando»)» (respaldo implícito) | `dentro_de_norma` |  | dentro de la Obligacion o12 (descripción); sin Condicion |
| 3 | «código 22600000 (tres «cuando»)» (cancelación anticipada) | `dentro_de_norma` |  | dentro de la Obligacion o12 (descripción); sin Condicion |
| 4 | «código 22700000» | `condicion_con_relacion` |  | cd13 Condicion «Adelantos exceden límite o no se cancelan en plazo» —condicion_de→ o13 Obligacion |
| 5 | «código 21800000» | `dentro_de_norma` |  | dentro de la Obligacion o7 (tramo «en la medida en que no hayan sido contabilizadas»); sin Condicion |

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:23 | sí (remisión pura) | «de acuerdo con el punto 8.4.1.3. -Sección 8del texto ordenado de las normas sobre "Capitales mínimos de las entidades financieras"» | `ausente` |  | ningún tramo contiene la remisión: el de o1 termina en «…en poder de la entidad»; c1 Comunicacion cubre solo el nombre del TO; remisión en la descripción de o1 |

## `ric::9.1.3` — Limitación al crecimiento de pasivos

Grupos: grupo_c.

### Texto

> *heredado:* Sección 9. Incrementos de exigencia por riesgo de crédito
> *heredado:* 9.1. Normas de procedimiento
> *propio:* 9.1.3. Limitación al crecimiento de pasivos Cuando se presenten ambas o alguna de las siguientes situaciones: - Obligatoriedad de presentación del Plan de Regularización y Saneamiento en capitales mínimos. - La suma de incrementos de exigencia de capitales mínimos por riesgo de crédito resultantes de los incumplimientos en las relaciones técnicas de activos inmovilizados y/o crediticias, supere el 5 % de dicha exigencia (código 70100000). No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento, teniendo en cuenta el importe registrado en el código 310000 del Balance de Saldos. Se admitirá únicamente el crecimiento originado por el devengamiento de intereses. En los casos de regulaciones sobre base consolidada, se asimilarán las partidas a la posición individual. Dicho límite se observará mientras persista alguna de las situaciones previstas.

### Extracción (código A)

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

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «obligación del plan de regularización» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ r1 Restriccion |
| 2 | «incrementos de más del 5 %» | `condicion_con_relacion` |  | c2 Condicion con el umbral —condicion_de→ r1 Restriccion |
| 3 | «base consolidada» | `dentro_de_norma` |  | extraído como norma de otro tipo: o1 Obligacion «Asimilación de partidas en base consolidada» (el supuesto en su tramo); sin Condicion |
| 4 | «mientras persista» | `dentro_de_norma` |  | dentro de la Restriccion r1 (descripción «mientras persista alguna de las situaciones previstas»); sin Condicion |

