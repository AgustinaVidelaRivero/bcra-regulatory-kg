# Fichas de C2 — código W

Lectura cegada (primera lectura de la instancia). El código no dice el brazo ni la corrida; la tabla sigue cerrada hasta la adjudicación. Clases de M1 y M2: `c0/reglas_lectura_c0.md`.

## `cap::10.3.1.1` — Se asignarán las calificaciones de las ECAI admisibles a los ponderadores de

Grupos: omisiones.

### Texto

> *heredado:* Sección 10. Agentes de calificación externa (ECAI).
> *heredado:* 10.3. Consideraciones para su implementación.
> *heredado:* 10.3.1. Proceso de asignación de calificaciones (mapping).
> *propio:* 10.3.1.1. Se asignarán las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4.; es decir, las entidades financieras deberán establecer qué calificaciones o categorías de evaluación corresponden a esos ponderadores de riesgo. El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en esas calificaciones. Además, deberá abarcar todos los ponderadores de riesgo previstos en esos puntos.

### Extracción (código W)

- **op1 Operacion** «Asignación de calificaciones ECAI a ponderadores (mapping)» — Asignación de las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "asignación de calificaciones"}` · tramo [exacta]: «Proceso de asignación de calificaciones (mapping).»
- **o1 Obligacion** «Establecer correspondencia calificaciones-ponderadores de riesgo» — Las entidades financieras deberán asignar las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4., estableciendo qué calificaciones o categorías de evaluación corresponden a cada ponderador. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «las entidades financieras deberán establecer qué calificaciones o categorías de evaluación corresponden a esos ponderadores de riesgo»
- **o2 Obligacion** «Objetividad y coherencia del mapping» — El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en esas calificaciones. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en esas calificaciones»
- **o3 Obligacion** «Cobertura de todos los ponderadores en mapping» — El proceso de asignación (mapping) deberá abarcar todos los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «deberá abarcar todos los ponderadores de riesgo previstos en esos puntos»
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: Sujeto_entidad_financiera (mención «las entidades financieras») —ejecuta→ op1 Operacion

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

### Extracción (código W)

- **e1 Operacion** «Cálculo exigencia capital por riesgo de crédito» — Determinación de la exigencia de capital mínimo por riesgo de crédito mediante una expresión que combina factor k, 8% de los APR e incrementos INC · props: `{"tipo": "cálculo de exigencia"}` · tramo [exacta]: «C : exigencia de capital por riesgo de crédito.»
- **e2 Obligacion** «Factor k según calificación SEFYC — exigencia crédito» — El factor k de la exigencia se fija según la calificación asignada por la SEFYC: calificación 1 → k=1; 2 → 1,03; 3 → 1,08; 4 → 1,13; 5 → 1,19. · props: `{"tipo": "calculo"}` · tramo [exacta]: «k: factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por la SEFYC, teniendo en cuenta la siguiente escala:»
- **e3 Obligacion** «Última calificación informada — cómputo al tercer mes» — Se considera la última calificación informada para el cálculo de la exigencia a integrar al tercer mes siguiente al de la notificación. · props: `{"tipo": "calculo", "umbrales": [{"tramo": "al tercer mes siguiente a aquel en que tenga lugar la\nnotificación", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['al tercer mes siguiente a aquel en que tenga lugar la notificación'] · tramo [exacta]: «se considerará la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación»
- **e4 Obligacion** «k igual a 1,03 sin calificación comunicada» — Mientras no se comunique la calificación, k vale 1,03. · props: `{"tipo": "calculo"}` · tramo [exacta]: «En tanto no se comunique, el valor de "k" será igual a 1,03.»
- **e5 Condicion** «Calificación aún no comunicada» — Mientras la SEFYC no comunique la calificación. · tramo [exacta]: «En tanto no se comunique»
- **e6 Restriccion** «Límite 15% participación por empresa» — Participación en el capital de cada empresa: límite 15% de la RPC del último día anterior; los excesos incrementan la exigencia (INC inversiones significativas). · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['participación en el capital de cada empresa: 15%'] · tramo [exacta]: «– participación en el capital de cada empresa: 15%;»
- **e7 Restriccion** «Límite 60% total participaciones en empresas» — Total de participaciones en el capital de empresas: límite 60% de la RPC del último día anterior; los excesos incrementan la exigencia. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['total de participaciones en el capital de empresas: 60%'] · tramo [exacta]: «– total de participaciones en el capital de empresas: 60%.»
- **e8 Operacion** «Participación en capital de empresas» — Participaciones de la entidad en el capital de empresas · props: `{"tipo": "inversión"}` · tramo [exacta]: «participación en el capital de cada empresa»
- **e9 Obligacion** «Base RPC del día anterior para límites» — Los límites de participaciones se aplican sobre la RPC de la entidad financiera del último día anterior. · props: `{"tipo": "calculo"}` · tramo [exacta]: «Los límites máximos establecidos se aplicarán sobre la responsabilidad patrimonial computable (RPC) de la entidad financiera del último día anterior al que corresponda.»
- **e10 Obligacion** «INC por excesos en relaciones técnicas» — La exigencia se incrementa por excesos en: activos inmovilizados; límites de Financiamiento al SPNF; Grandes Exposiciones; graduación del crédito; límite de derivados sobre commodities; excluidos los computados en INC por inversiones significativas. · props: `{"tipo": "calculo"}` · tramo [exacta]: «INC: incremento por los siguientes excesos:»
- **e11 Obligacion** «Aplicar Sección 2 TO Incumplimientos» — Se aplican las disposiciones de la Sección 2 del TO Incumplimientos de Capitales Mínimos y Relaciones Técnicas. · props: `{"tipo": "otra"}` · tramo [exacta]: «En la materia, serán de aplicación las disposiciones contenidas en la Sección 2. del TO sobre Incumplimientos de Capitales Mínimos y Relaciones Técnicas. Criterios Aplicables»
- **e12 Excepcion** «Aplicación de Sección 3 TO Incumplimientos» — Salvo que resulte aplicable la Sección 3 de esas normas. · tramo [exacta]: «salvo que resulte aplicable lo previsto en la Sección 3. de esas normas»
- **e13 Obligacion** «Cómputo como INC de cupos crediticios ampliados» — Se computa como INC la exposición por uso de cupos ampliados (puntos 6.1.1.2 y 6.1.2.1 d) TO SPNF) por asistencia o tenencias de fideicomisos/fondos fiduciarios, según cronograma: 25% desde el primer mes, 50% desde el séptimo, 100% desde el décimo tercero, contado desde que las obras se usen económicamente o generen ingresos. · props: `{"tipo": "calculo", "umbrales": [{"tramo": "25 Primer mes", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "50 Séptimo mes", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "100 Décimo tercer mes", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['25 Primer mes', '50 Séptimo mes', '100 Décimo tercer mes'] · tramo [exacta]: «También se computará en esta expresión la exposición crediticia resultante de la utilización de los cupos crediticios ampliados»
- **e14 Condicion** «Inicio de uso económico o ingresos» — El cronograma opera desde que las obras se usen económicamente o el equipamiento genere ingresos. · tramo [exacta]: «a partir de que se hayan comenzado a utilizar económicamente las obras o el equipamiento genere ingresos al fideicomiso o fondo fiduciario»
- **e15 Definicion** «Sector público no financiero» — El definido en la Sección 1 del TO sobre Financiamiento al SPNF. · props: `{"termino": "sector público no financiero"}` · tramo [exacta]: «El sector público no financiero citado en estas normas es aquel definido en la Sección 1. del TO sobre Financiamiento al Sector Público no Financiero.»
- **e16 Definicion** «DvP fallidas incluyen PvP fallidas» — Operaciones de entrega contra pago fallidas, incluidas las de pago contra pago fallidas. · props: `{"termino": "DvP"}` · tramo [exacta]: «DvP: operaciones de entrega contra pago fallidas (a los efectos de estas normas, incluyen las operaciones de pago contra pago –PvP– fallidas)»
- R: e2 Obligacion —regula→ e1 Operacion
- R: e3 Obligacion —regula→ e1 Operacion
- R: e4 Obligacion —regula→ e1 Operacion
- R: e5 Condicion —condicion_de→ e4 Obligacion
- R: e6 Restriccion —limita→ e8 Operacion
- R: e7 Restriccion —limita→ e8 Operacion
- R: e10 Obligacion —regula→ e1 Operacion
- R: e13 Obligacion —regula→ e1 Operacion
- R: e14 Condicion —condicion_de→ e13 Obligacion
- R: e12 Excepcion —exceptua_obligacion→ e11 Obligacion
- R: e9 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «entidad financiera»)
- Omisión `formula` [exacta]: «C = (k x 0,08 x APR ) + INC» — Fórmula declarada no confiable; no se reconstruye.
- Omisión `formula` [exacta]: «A x p + PFB x CCF x p + no DvP + (DVP + RCD + INC(inversiones empresas)) x 12,5» — Fórmula de APR no confiable; términos definidos solo descriptivamente.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «en tanto no se comunique la calificación» | `condicion_con_relacion` |  | e5 Condicion «Calificación aún no comunicada» —condicion_de→ e4 Obligacion |
| 2 | «el cronograma opera desde que las obras se usan económicamente» | `condicion_con_relacion` |  | e14 Condicion «Inicio de uso económico o ingresos» —condicion_de→ e13 Obligacion |

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

### Extracción (código W)

- **op1 Operacion** «Exposición minorista normativa a personas humanas» — Inclusión de exposiciones minoristas a personas humanas en las exposiciones minoristas normativas · props: `{"tipo": "clasificación de exposición"}` · tramo [exacta]: «En el caso de exposiciones minoristas a personas humanas»
- **r1 Restriccion** «Relación cuota/ingreso máx. 30% — minoristas personas humanas» — En exposiciones minoristas a personas humanas, el total de vencimientos por cuotas de todas las financiaciones de la entidad con amortización periódica (sin considerar cuotas de créditos de otras entidades) no deberá exceder, al momento de los acuerdos, el 30% de los ingresos del deudor y/o codeudores. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['no deberá exceder, al momento de los acuerdos, el 30% de los ingresos del deudor'] · tramo [exacta]: «el total de los vencimientos por las cuotas de todas las financiaciones de la entidad financiera que cuenten con amortización periódica –sin considerar las cuotas de créditos de otras entidades– no deberá exceder, al momento de los acuerdos, el 30% de los ingresos del deudor y/o, en su caso, de los codeudores.»
- **d1 Definicion** «Numerador cuota/ingreso: conceptos excluidos» — No forman parte del numerador: márgenes de descubiertos en cuenta corriente y límites de compra de tarjetas (utilizado y disponible) y préstamos personales preacordados no formalizados ni desembolsados, por no contar con amortización periódica. · props: `{"termino": "numerador de la relación cuo-\nta/ingreso"}` · tramo [exacta]: «los márgenes acordados para los descubiertos en cuenta corriente y los límites de compra de las tarjetas de crédito –en ambos casos, tanto el utilizado como el disponible–, así como los préstamos personales preacordados –en la medida en que aún no hayan sido formalizados ni desembolsados al cliente–, no formarán parte …»
- **d2 Definicion** «Cuotas: incluye compras financiadas con tarjeta» — El concepto cuotas incluye las que el cliente tenga por compras financiadas en el sistema de tarjeta de crédito. · props: `{"termino": "cuotas"}` · tramo [exacta]: «Deberá considerarse dentro del concepto "cuotas" aquellas que el cliente tenga por compras financiadas en el marco del sistema de tarjeta de crédito.»
- **o1 Obligacion** «Información para verificar criterios — compra de cartera» — Para considerar en exposiciones minoristas normativas créditos incorporados por compra de cartera, se deberá contar con la información necesaria para verificar el cumplimiento de los criterios y límites precedentes. · props: `{"tipo": "otra"}` · tramo [exacta]: «se deberá contar con la información necesaria para verificar el cumplimiento de los criterios y límites detallados precedentemente.»
- **op2 Operacion** «Inclusión de créditos de compra de cartera en minoristas normativas» — Considerar como exposiciones minoristas normativas créditos incorporados mediante compra de cartera · props: `{"tipo": "clasificación de exposición"}` · tramo [exacta]: «considerar en las exposiciones minoristas normativas a los créditos incorporados a través de una compra de cartera»
- R: r1 Restriccion —limita→ op1 Operacion
- R: o1 Obligacion —condiciona→ op2 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)

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

### Extracción (código W)

- **d1 Definicion** «Exposiciones subyacentes a la titulización: conceptos incluidos» — Las exposiciones subyacentes a la titulización pueden incluir, entre otros conceptos (enumeración no taxativa), préstamos, compromisos asumidos por la entidad, posiciones de titulización, obligaciones negociables y acciones. · props: `{"termino": "exposiciones subyacentes a la titulización"}` · tramo [exacta]: «Las exposiciones subyacentes a la titulización podrán incluir, entre otros conceptos: préstamos, compromisos asumidos por la entidad, posiciones de titulización, obligaciones negociables y acciones.»
- **d2 Definicion** «Conjunto subyacente: una o varias exposiciones» — El conjunto subyacente de una titulización puede estar compuesto por una o varias exposiciones. · props: `{"termino": "conjunto subyacente"}` · tramo [exacta]: «El conjunto subyacente podrá incluir una o varias exposiciones.»

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

### Extracción (código W)

- **d1 Definicion** «KSA — exigencia de capital promedio subyacentes» — KSA: exigencia de capital promedio de las exposiciones subyacentes; ratio entre la suma de las exposiciones subyacentes ponderadas por riesgo y la suma de las exposiciones subyacentes, multiplicado por 8 %; porcentaje entre cero y cien. · props: `{"termino": "K"}` · tramo [exacta]: «Es la exigencia de capital promedio de las exposiciones subyacentes»
- **o1 Operacion** «Cálculo de KSA en titulizaciones» — Cálculo de la exigencia de capital promedio de las exposiciones subyacentes (KSA) bajo enfoque estandarizado de titulización · props: `{"tipo": "calculo"}` · tramo [exacta]: «El cálculo deberá reflejar los efectos de cualquier cobertura del riesgo de crédito»
- **ob1 Obligacion** «Reflejar coberturas de riesgo — cálculo KSA» — El cálculo de KSA deberá reflejar los efectos de cualquier cobertura del riesgo de crédito aplicable a las exposiciones subyacentes, individualmente o al conjunto. · props: `{"tipo": "calculo"}` · tramo [exacta]: «El cálculo deberá reflejar los efectos de cualquier cobertura del riesgo de crédito que corresponda aplicar a las exposiciones subyacentes»
- **d2 Definicion** «Activos subyacentes con SPE» — Cuando la estructura involucre a un SPE, integran el conjunto todas las exposiciones del SPE vinculadas a la titulización: activos en que invirtió el SPE, reservas, cuentas de efectivo en garantía y derechos frente a contrapartes por swaps de tasa o moneda. · props: `{"termino": "conjunto de activos subyacentes"}` · tramo [exacta]: «Cuando la estructura involucre a un SPE, se considerará que todas las exposiciones del SPE vinculadas a la titulización integran el conjunto de activos subyacentes.»
- **p1 Potestad** «Excluir exposiciones del SPE de subyacentes» — A los fines del cálculo de la exigencia de capital, la entidad podrá excluir del conjunto de activos subyacentes las exposiciones del SPE. · tramo [exacta]: «la entidad podrá excluir del conjunto de activos subyacentes a las exposiciones del SPE»
- **c1 Condicion** «Demostrar riesgo no afecta o insignificante» — La entidad demuestra que el riesgo no afecta a su posición de titulización o que es insignificante (p. ej., mitigado). · tramo [exacta]: «si puede demostrar que el riesgo no afecta a su posición de titulización o, en su defecto, que el riesgo es insignificante»
- **ob2 Obligacion** «Computar CLN en KSA — titulizaciones sintéticas» — En titulizaciones sintéticas con aporte de fondos, computar en KSA los montos recibidos por credit linked notes u otros pasivos suscriptos por el SPE. · props: `{"tipo": "calculo"}` · tramo [exacta]: «se deberán computar para el cálculo del K los montos recibidos por los insSA trumentos con vinculación crediticia ("credit linked note") u otros pasivos suscriptos por el SPE»
- **c2 Condicion** «Importes sirven como garantía del repago» — Los importes sirven como garantía del repago de la exposición titulizada. · tramo [exacta]: «cuando dichos importes sirvan como garantía del repago de la exposición titulizada en cuestión»
- **c3 Condicion** «Riesgo sujeto a asignación por tramos» — El riesgo de incumplimiento está sujeto a la asignación de pérdidas por tramos. · tramo [exacta]: «el riesgo de incumplimiento esté sujeto a la asignación de pérdidas por tramos»
- **x1 Excepcion** «Riesgo de incumplimiento insignificante — cómputo CLN» — No rige el cómputo de los montos de CLN si la entidad demuestra que el riesgo de incumplimiento es insignificante. · tramo [exacta]: «Ello a menos que la entidad pueda demostrar que el riesgo de incumplimiento es insignificante.»
- **ob3 Obligacion** «Monto bruto con previsión o descuento — KSA» — Si la entidad constituyó previsión específica o tiene descuento no reembolsable en el precio de compra, KSA se calcula con el monto bruto, sin deducirlos. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el cálculo de K deberá SA efectuarse usando el monto bruto de la exposición»
- **c4 Condicion** «Previsión específica o descuento no reembolsable» — La entidad constituyó previsión específica o tiene descuento no reembolsable en el precio de compra de su exposición. · tramo [exacta]: «En los casos en los que la entidad haya constituido una previsión específica o tenga un descuento no reembolsable en el precio de compra»
- **d3 Definicion** «W — ratio de subyacentes en mora» — Ratio entre el monto nominal de las exposiciones subyacentes en mora y el monto nominal de las exposiciones subyacentes. · props: `{"termino": "W"}` · tramo [exacta]: «La variable W es el ratio entre el monto nominal de las exposiciones subyacentes en mora y el monto nominal de las exposiciones subyacentes.»
- **d4 Definicion** «Exposiciones subyacentes en mora» — Atrasos de 90 días o más, quiebra/concurso o ejecución, inmuebles adquiridos en defensa del crédito, o incumplimiento según los contratos de titulización. · props: `{"termino": "en mora"}` · tramo [exacta]: «Se consideran en mora a las exposiciones subyacentes cuando se verifiquen atrasos en los pagos de 90 días o más»
- **d5 Definicion** «W en retitulizaciones mixtas» — En retitulizaciones con tramos de titulización y otros activos, W es cero para las posiciones de titulización y la que corresponda para los demás activos subyacentes. · props: `{"termino": "W"}` · tramo [exacta]: «W será cero para las posiciones de titulización»
- **ob4 Obligacion** «KA separado por subconjunto — retitulizaciones mixtas» — En retitulizaciones con tramos de titulización y otros activos, calcular KA por subconjunto con W separado; KA de la retitulización = promedio ponderado por exposición nominal. · props: `{"tipo": "calculo"}` · tramo [exacta]: «se deberá calcular por separado el K coA rrespondiente a cada subconjunto aplicando W por separado»
- **ob5 Obligacion** «Ajustar KA por cumplimiento desconocido ≤5 %» — Ajustar el cálculo de KA cuando se desconozca la situación de cumplimiento del 5 % o menos de las exposiciones subyacentes (fórmula no extraída). · props: `{"tipo": "calculo"}` · tramo [exacta]: «se deberá ajustar el cálculo de K de la siguiente manera:»
- **c5 Condicion** «Cumplimiento desconocido 5 % o menos» — Se desconoce la situación de cumplimiento del 5 % o menos de las exposiciones subyacentes. · umbral: ['5 % o menos de las exposiciones subyacentes'] · tramo [exacta]: «En caso de que se desconozca la situación de cumplimiento correspondiente al 5 % o menos de las exposiciones subyacentes»
- **r1 Restriccion** «Ponderador 1250 % por cumplimiento desconocido >5 %» — La posición de titulización se pondera al 1250 % si la entidad desconoce la situación de cumplimiento para más del 5 %. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['ponderarse al 1250 %'] · tramo [exacta]: «ésta deberá ponderarse al 1250 %»
- **c6 Condicion** «Cumplimiento desconocido más del 5 %» — La entidad no conoce la situación de cumplimiento para más del 5 % de la posición. · umbral: ['más del 5 %'] · tramo [exacta]: «Si la entidad no conociera la situación de cumplimiento para más del 5 % de la posición de titulización»
- **o2 Operacion** «Ponderación de posición de titulización» — Ponderación por riesgo de la posición de titulización · props: `{"tipo": "ponderacion"}` · tramo [exacta]: «posición de titulización»
- **ob6 Obligacion** «Calcular KSSFA(KA) por unidad de posición» — Calcular KSSFA(KA) conforme a fórmula, con p = 0,5 si cumple criterios STC del 3.1.14, p = 1 si no los cumple, p = 1,5 para retitulización. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La exigencia de capital por unidad de posición de titulización, K , se SSFA(KA) calculará conforme a lo siguiente:»
- R: ob1 Obligacion —regula→ o1 Operacion
- R: p1 Potestad —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: ob2 Obligacion —regula→ o1 Operacion
- R: c2 Condicion —condicion_de→ ob2 Obligacion
- R: c3 Condicion —condicion_de→ ob2 Obligacion
- R: x1 Excepcion —exceptua_obligacion→ ob2 Obligacion
- R: x1 Excepcion —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- R: ob3 Obligacion —regula→ o1 Operacion
- R: c4 Condicion —condicion_de→ ob3 Obligacion
- R: c5 Condicion —condicion_de→ ob5 Obligacion
- R: r1 Restriccion —limita→ o2 Operacion
- R: c6 Condicion —condicion_de→ r1 Restriccion
- Omisión `formula` [exacta]: «K se obtiene a partir de K y W conforme a la siguiente expresión:» — Fórmula de KA no confiable; no se reconstruye.
- Omisión `formula` [exacta]: «se deberá ajustar el cálculo de K de la siguiente manera:» — Fórmula de ajuste de KA no confiable.
- Omisión `formula` [exacta]: «calculará conforme a lo siguiente: donde:» — Fórmula de KSSFA(KA) no confiable; solo se describen los valores de p en la descripción.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «estructura con SPE» | `dentro_de_norma` |  | dentro de la Definicion d2 («Activos subyacentes con SPE») |
| 2 | «si puede demostrar» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ p1 Potestad |
| 3 | «sintéticas con fondos aportados» | `dentro_de_norma` |  | dentro de la Obligacion ob2 (descripción «En titulizaciones sintéticas con aporte de fondos»); c2 y c3 son otros supuestos |
| 4 | «previsión específica» | `condicion_con_relacion` |  | c4 Condicion —condicion_de→ ob3 Obligacion |
| 5 | «desconocida para 5 % o menos» | `condicion_con_relacion` |  | c5 Condicion con el umbral —condicion_de→ ob5 Obligacion |
| 6 | «para más del 5 %» | `condicion_con_relacion` |  | c6 Condicion con el umbral —condicion_de→ r1 Restriccion (la ponderación al 1250 %, extraída como Restriccion) |

## `cap::3.1.11.3` — Determinación del ponderador de riesgo (RW).

Grupos: grupo_c.

### Texto

> *heredado:* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos.
> *heredado:* 3.1. Tratamiento de las titulizaciones.
> *heredado:* Se denomina "posición de titulización" a la exposición a una titulización (o retitulización), tradicional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes conceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos ("AssetBacked Securities", ABS) y bonos de titulización hipotecaria ("Mortgage-Backed Securities", MBS)–, mejoras crediticias, facilidades de liquidez, "swaps" de tasa de interés o de monedas y derivados de crédito. Las reservas ("reserve accounts"), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo también el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad económica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una determinada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> *heredado:* 3.1.11. Enfoque estandarizado.
> *heredado:* Los ponderadores de riesgo a aplicar a las posiciones de una titulización y a las exposiciones subyacentes de una retitulización para la determinación de la exigencia de capital se establecerán empleando las disposiciones de este punto. Las posiciones de titulización a las que no se les pueda aplicar el enfoque estandarizado deberán ser ponderadas al 1250 %.
> *propio:* 3.1.11.3. Determinación del ponderador de riesgo (RW). El ponderador de riesgo RW a asignar a una posición de titulización se calculará con ajuste a lo siguiente: i) Si D es menor o igual a K , el ponderador será de 1250 %. A ii) Si A es mayor o igual a K , el ponderador será igual a K multiplicado A SSFA(KA) por 12,5. iii) Si K es mayor que A y menor que D, el ponderador será un promedio A ponderado entre 1250 % y 12,5 veces K conforme a la siguiente exSSFA(KA) presión: El ponderador para coberturas del riesgo de mercado, tales como "swaps" de moneda o de tasa de interés, se inferirá a partir de una posición de titulización de igual prelación ("pari passu") con los "swaps" o, si tal posición no existiera, a partir del tramo subordinado más próximo. El ponderador resultante estará sujeto a un mínimo de: a) 15 % para titulizaciones que no cumplan con los criterios STC –punto 3.1.14.–. b) 10 % para los tramos de máxima preferencia de titulizaciones que cumplan con los criterios STC –punto 3.1.14.– y 15 % para los tramos subordinados de esas titulizaciones. c) 100 % para retitulizaciones. Para posiciones de titulización de máxima preferencia se podrá aplicar el tratamiento de transparencia ("look-through") de conformidad con lo previsto en el punto 3.1.6. Si el ponderador que surge de la aplicación de ese tratamiento fuera menor que el ponderador mínimo que corresponda de acuerdo con los apartados a) a c) precedentes, se podrá aplicar el primero.

### Extracción (código W)

- **op1 Operacion** «Asignación de RW a posición de titulización» — Asignación del ponderador de riesgo RW a una posición de titulización bajo el enfoque estandarizado (SSFA) · props: `{"tipo": "ponderación por riesgo"}` · tramo [exacta]: «El ponderador de riesgo RW a asignar a una posición de titulización»
- **o1 Obligacion** «RW 1250 % si D ≤ KA» — El RW de la posición de titulización será de 1250 % si D es menor o igual a KA · props: `{"tipo": "calculo"}` · umbral: ['el ponderador será de 1250 %'] · tramo [exacta]: «El ponderador de riesgo RW a asignar a una posición de titulización se calculará con ajuste a lo siguiente: […] Si D es menor o igual a K , el ponderador será de 1250 %.»
- **c1 Condicion** «D menor o igual a KA» — El punto de desprendimiento D es menor o igual a KA · tramo [exacta]: «Si D es menor o igual a K»
- **o2 Obligacion** «RW = KSSFA × 12,5 si A ≥ KA» — Si A es mayor o igual a KA, el RW será igual a KSSFA(KA) multiplicado por 12,5 · props: `{"tipo": "calculo"}` · tramo [exacta]: «El ponderador de riesgo RW a asignar a una posición de titulización se calculará con ajuste a lo siguiente: […] Si A es mayor o igual a K , el ponderador será igual a K multiplicado»
- **c2 Condicion** «A mayor o igual a KA» — El punto de enganche A es mayor o igual a KA · tramo [exacta]: «Si A es mayor o igual a K»
- **o3 Obligacion** «RW promedio ponderado si A < KA < D» — Si KA es mayor que A y menor que D, el RW será un promedio ponderado entre 1250 % y 12,5 veces KSSFA(KA) conforme a una expresión (fórmula no reproducida) · props: `{"tipo": "calculo"}` · tramo [no]: «El ponderador de riesgo RW a asignar a una posición de titulización se calculará con ajuste a lo siguiente: […] el ponderador será un promedio A ponderado entre 1250 % y 12,5 veces K conforme a la siguiente ex-»
- **c3 Condicion** «KA mayor que A y menor que D» — KA es mayor que A y menor que D · tramo [exacta]: «Si K es mayor que A y menor que D»
- **o4 Obligacion** «RW coberturas de mercado inferido pari passu» — El RW para coberturas de riesgo de mercado (swaps de moneda o tasa) se infiere de una posición de titulización pari passu con los swaps o, si no existiera, del tramo subordinado más próximo · props: `{"tipo": "calculo"}` · tramo [exacta]: «El ponderador para coberturas del riesgo de mercado, tales como "swaps" de moneda o de tasa de interés, se inferirá a partir de una posición de titulización de igual prelación ("pari passu") con los "swaps"»
- **r1 Restriccion** «Mínimo 15 % — titulizaciones no STC» — El RW tiene un mínimo de 15 % para titulizaciones que no cumplan los criterios STC · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['sujeto a un mínimo de: […] 15 % para titulizaciones que no cumplan con los crite…'] · tramo [exacta]: «El ponderador resultante estará sujeto a un mínimo de: […] 15 % para titulizaciones que no cumplan con los criterios STC»
- **r2 Restriccion** «Mínimo 10 % — tramos preferentes STC» — El RW tiene un mínimo de 10 % para tramos de máxima preferencia de titulizaciones STC · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['10 % para los tramos de máxima preferencia'] · tramo [exacta]: «El ponderador resultante estará sujeto a un mínimo de: […] 10 % para los tramos de máxima preferencia de titulizaciones que cumplan con los criterios STC»
- **r3 Restriccion** «Mínimo 15 % — tramos subordinados STC» — El RW tiene un mínimo de 15 % para tramos subordinados de titulizaciones STC · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['15 % para los tramos subordinados'] · tramo [exacta]: «El ponderador resultante estará sujeto a un mínimo de: […] 15 % para los tramos subordinados de esas titulizaciones»
- **r4 Restriccion** «Mínimo 100 % — retitulizaciones» — El RW tiene un mínimo de 100 % para retitulizaciones · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['100 % para retitulizaciones'] · tramo [exacta]: «El ponderador resultante estará sujeto a un mínimo de: […] 100 % para retitulizaciones.»
- **p1 Potestad** «Look-through para posiciones de máxima preferencia» — Para posiciones de máxima preferencia se puede aplicar el tratamiento look-through del punto 3.1.6 · tramo [exacta]: «Para posiciones de titulización de máxima preferencia se podrá aplicar el tratamiento de transparencia ("look-through")»
- **x1 Excepcion** «RW look-through menor que mínimo aplicable» — Si el RW por look-through es menor que el mínimo de los apartados a) a c), se puede aplicar el primero, sin sujeción a esos mínimos · tramo [exacta]: «Si el ponderador que surge de la aplicación de ese tratamiento fuera menor que el ponderador mínimo que corresponda de acuerdo con los apartados a) a c) precedentes, se podrá aplicar el primero.»
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o4 Obligacion —regula→ op1 Operacion
- R: c1 Condicion —condicion_de→ o1 Obligacion
- R: c2 Condicion —condicion_de→ o2 Obligacion
- R: c3 Condicion —condicion_de→ o3 Obligacion
- R: r1 Restriccion —limita→ op1 Operacion
- R: r2 Restriccion —limita→ op1 Operacion
- R: r3 Restriccion —limita→ op1 Operacion
- R: r4 Restriccion —limita→ op1 Operacion
- R: x1 Excepcion —exceptua→ r1 Restriccion
- R: x1 Excepcion —exceptua→ r2 Restriccion
- R: x1 Excepcion —exceptua→ r3 Restriccion
- R: x1 Excepcion —exceptua→ r4 Restriccion
- Omisión `formula` [exacta]: «conforme a la siguiente exSSFA(KA) presión:» — La expresión del promedio ponderado no se pudo extraer de forma confiable; no se reconstruye
- Omisión `formula` [exacta]: «ii) Si A es mayor o igual a K , el ponderador será igual a K multiplicado A SSFA(KA) por 12,5.» — Los subíndices de KA y KSSFA(KA) quedaron dañados en la extracción; 12,5 es un factor del cálculo, no un umbral

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «i) a iii) según D, A y KA» (i)) | `condicion_con_relacion` |  | c1 Condicion «D menor o igual a KA» —condicion_de→ o1 Obligacion |
| 2 | «i) a iii) según D, A y KA» (ii)) | `condicion_con_relacion` |  | c2 Condicion «A mayor o igual a KA» —condicion_de→ o2 Obligacion |
| 3 | «i) a iii) según D, A y KA» (iii)) | `condicion_con_relacion` |  | c3 Condicion «KA mayor que A y menor que D» —condicion_de→ o3 Obligacion |
| 4 | «si no existiera la posición pari passu» | `dentro_de_norma` |  | dentro de la Obligacion o4 (descripción) |
| 5 | «mínimos por STC» | `dentro_de_norma` |  | dentro de las Restricciones r1 a r4; sin Condicion |
| 6 | «look-through menor que el mínimo» | `condicion_con_relacion` |  | x1 Excepcion «RW look-through menor que mínimo aplicable» (cláusula de excepción a los mínimos) —exceptua→ r1 a r4 Restriccion |

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

### Extracción (código W)

- **op1 Operacion** «Titulización STC» — Titulización simple, transparente y comparable (STC) a los fines del ponderador del enfoque estandarizado · props: `{"tipo": "titulizacion"}` · tramo [exacta]: «Criterios para la determinación de titulizaciones simples, transparentes y comparables.»
- **o1 Obligacion** «Homogeneidad y flujos — activos subyacentes STC» — Los subyacentes deben ser documentos a cobrar o derechos de crédito homogéneos (tipo, jurisdicción, legislación, moneda), con flujos contractualmente identificados, periódicos y exclusivamente de principal e intereses o arrendamientos financieros. · props: `{"tipo": "otra"}` · tramo [exacta]: «Los activos subyacentes deberán estar constituidos por documentos a cobrar o derechos de crédito de carácter homogéneo en cuanto a su tipo, jurisdicción, legislación aplicable y moneda»
- **o2 Obligacion** «Evaluación de homogeneidad por principios a)-d)» — La homogeneidad debe evaluarse según: a) sin perfiles de riesgo sustancialmente diferentes; b) factores de riesgo comunes; c) obligaciones estándares con flujo periódico y definido; d) reembolso principalmente del producido de los activos, no dependiente sustancialmente de refinanciación. · props: `{"tipo": "otra"}` · tramo [exacta]: «La homogeneidad de los activos subyacentes deberá evaluarse teniendo en consideración los siguientes principios:»
- **p1 Potestad** «Refinanciación o venta de subyacentes admitida» — Se puede contar con la refinanciación o venta de los subyacentes bajo condiciones. · tramo [exacta]: «Se podrá contar con la refinanciación o venta de los subyacentes»
- **c1 Condicion** «Refinanciaciones suficientemente distribuidas» — Operaciones a refinanciar suficientemente distribuidas en la cartera · tramo [exacta]: «siempre que las operaciones a refinanciar estén suficientemente distribuidas en el conjunto de los activos titulizados»
- **c2 Condicion** «Valores residuales no significativos» — Valores residuales no significativos · tramo [exacta]: «que sus valores residuales no sean significativos»
- **o3 Obligacion** «Tasas de referencia de mercado y fácil consulta» — Tasas de referencia de mercado y fácil consulta, evitando fórmulas complejas o derivados exóticos; topes y pisos de tasas no se consideran necesariamente derivados exóticos. · props: `{"tipo": "otra"}` · tramo [exacta]: «Las tasas de interés o de descuento de referencia deberán ser tasas de interés de mercado y de fácil consulta»
- **o4 Obligacion** «Información verificable de pérdidas e incumplimientos» — Contar con información verificable de pérdidas e incumplimientos de activos similares por período suficientemente prolongado. · props: `{"tipo": "otra"}` · tramo [exacta]: «Se deberá contar con información verificable sobre pérdidas e incumplimientos»
- **o5 Obligacion** «Fuentes de información disponibles al mercado» — Fuentes, acceso a datos y fundamentos de similitud disponibles para todos los participantes del mercado. · props: `{"tipo": "otra"}` · tramo [exacta]: «deberán estar disponibles para todos los participantes del mercado»
- **o6 Obligacion** «Experiencia suficiente del originante y acreedor inicial» — Originante y acreedor inicial con experiencia suficiente en financiaciones similares. · props: `{"tipo": "otra"}` · tramo [exacta]: «El originante de la titulización, así como el acreedor inicial de los créditos titulizados, deberán contar con experiencia suficiente»
- **o7 Obligacion** «Inversor determina historial de desempeño» — El inversor debe determinar experiencia e historial de desempeño del originante y acreedor inicial. · props: `{"tipo": "otra"}` · tramo [exacta]: «El inversor deberá determinar la experiencia y el historial de desempeño del originante y del acreedor inicial»
- **o8 Obligacion** «Desempeño 5 años — exposiciones minoristas» — Desempeño verificado mínimo 5 años para exposiciones minoristas del punto 2.8.1 (sin exclusiones) que cumplan 2.8.3.1. · props: `{"tipo": "otra"}` · umbral: ['período mínimo de 5 años'] · tramo [exacta]: «El desempeño se deberá verificar durante un período mínimo de 5 años en el caso de las exposiciones minoristas»
- **o9 Obligacion** «Desempeño 7 años — resto de exposiciones» — Para el resto de exposiciones, desempeño verificado durante 7 años. · props: `{"tipo": "otra"}` · umbral: ['durante 7 años'] · tramo [exacta]: «Para el resto de las exposiciones, el desempeño deberá verificarse durante 7 años.»
- **r1 Restriccion** «Prohibido transferir activos en mora» — No se pueden transferir activos en incumplimiento o mora, con evidencia de incremento sustancial de pérdidas esperadas o en gestión de cobranza. · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «no se podrán transferir activos en situación de incumplimiento o mora»
- **op2 Operacion** «Transferencia de activos a la titulización» — Transferencia de activos subyacentes a la titulización · props: `{"tipo": "transferencia de activos"}` · tramo [exacta]: «transferir activos»
- **o10 Obligacion** «Sin quiebra o reestructuración del obligado 3 años» — Originante o fiduciario debe verificar que el obligado no tuvo quiebra o reestructuración en los 3 años previos. · props: `{"tipo": "otra"}` · umbral: ['en los 3 años previos a la fecha de originación'] · tramo [exacta]: «El originante o fiduciario deberá verificar que los activos cumplan con las siguientes condiciones: […] El obligado al pago no ha sido sometido a un proceso de quiebra o de reestructuración de deuda debido a dificultades financieras en los 3 años previos a la fecha de originación»
- **x1 Excepcion** «Período de 2 años Ley 25.326» — Se aplica el período de 2 años de la Ley 25.326 en lugar de 3. · umbral: ['el período de 2 años'] · tramo [exacta]: «salvo que resulte de aplicación el período de 2 años previsto en el art. 26, inciso 4, de la Ley 25.326»
- **o11 Obligacion** «Sin historial de crédito desfavorable del obligado» — Verificar que el obligado no tenga historial desfavorable en registro público de crédito. · props: `{"tipo": "otra"}` · tramo [exacta]: «El originante o fiduciario deberá verificar que los activos cumplan con las siguientes condiciones: […] El obligado al pago no cuenta con un historial de crédito desfavorable en algún registro público de crédito.»
- **o12 Obligacion** «Sin calificación o scoring de riesgo significativo» — Verificar ausencia de calificación o scoring que anticipe riesgo significativo. · props: `{"tipo": "otra"}` · tramo [exacta]: «El originante o fiduciario deberá verificar que los activos cumplan con las siguientes condiciones: […] El obligado al pago no cuenta con una evaluación de una agencia de calificación de créditos o un credit scoring que anticipen un riesgo de incumplimiento significativo.»
- **o13 Obligacion** «Crédito transferido sin litigios» — Verificar que el crédito no sea objeto de litigio entre obligado y acreedor original. · props: `{"tipo": "otra"}` · tramo [exacta]: «El originante o fiduciario deberá verificar que los activos cumplan con las siguientes condiciones: […] El documento a cobrar o derecho de crédito transferido no es objeto de litigios entre el obligado y el acreedor original.»
- **o14 Obligacion** «Análisis dentro de 45 días previos a transferencia» — Análisis dentro de los 45 días previos a la transferencia; sin evidencia de deterioro al evaluar. · props: `{"tipo": "otra"}` · umbral: ['dentro de los 45 días previos a la fecha de la transferencia'] · tramo [exacta]: «El análisis de estas condiciones deberá ser llevado a cabo por el originante o fiduciario dentro de los 45 días previos a la fecha de la transferencia»
- **o15 Obligacion** «Al menos un pago registrado al incluir activo» — Al incluir el activo en la cartera debe haberse registrado al menos un pago. · props: `{"tipo": "otra", "umbrales": [{"tramo": "al menos un pago", "comparacion": "minimo_inclusivo", "base": "un pago", "regla_comparacion": "limite_relativo:compuesta:al_menos", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['al menos un pago'] · tramo [exacta]: «deberá haberse registrado al menos un pago»
- **x2 Excepcion** «Activos rotativos — sin pago previo» — Estructuras sobre activos rotativos (tarjetas, facturas, cancelables en un pago) exceptuadas del pago previo. · tramo [exacta]: «excepto en el caso de las estructuras sobre activos de tipo rotativos»
- **o16 Obligacion** «Demostrar originación uniforme al inversor» — Originante demuestra originación en curso normal con estándares uniformes y consistentes. · props: `{"tipo": "otra"}` · tramo [exacta]: «El originante deberá demostrar al inversor que los activos transferidos han sido generados en el curso normal de su negocio»
- **o17 Obligacion** «Comunicar cambios en estándares de originación» — Ante cambios de estándares, comunicar momento y propósito. · props: `{"tipo": "otra"}` · tramo [exacta]: «el originante deberá comunicar el momento y el propósito de las modificaciones»
- **r2 Restriccion** «Estándares no menos rigurosos que retenidos» — Estándares no menos rigurosos que los de activos retenidos. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «Los estándares no deberán ser menos rigurosos que aquellos aplicados a los activos retenidos por el originante.»
- **o18 Obligacion** «Criterios de originación sólidos y prudentes» — Créditos titulizados con criterios de originación sólidos, con evaluación de capacidad e intención de pago; carteras atomizadas originadas en curso normal y con flujos suficientes en estrés. · props: `{"tipo": "otra"}` · tramo [exacta]: «deberán satisfacer criterios de originación sólidos y prudentes»
- **o19 Obligacion** «Revisar estándares de terceros cedentes» — Si activos adquiridos a terceros, revisar sus estándares y constatar evaluación del acreedor original. · props: `{"tipo": "otra"}` · tramo [exacta]: «el originante/fiduciario de la titulización deberá revisar los estándares de originación de esos terceros»
- **c3 Condicion** «Activos adquiridos a terceros» — Activos adquiridos a terceros · tramo [exacta]: «Cuando los activos hayan sido adquiridos a terceros»
- **r3 Restriccion** «Sin gestión activa y discrecional de cartera» — Prohibida la selección por gestión activa y discrecional, incluso para activos transferidos luego; selección por criterios de elegibilidad definidos. Rotación, sustitución o recompra no discrecional no es gestión activa. · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «El desempeño de la titulización no deberá depender de una selección de los subyacentes a través de la gestión activa y discrecional de la cartera.»
- **op3 Operacion** «Selección discrecional de subyacentes» —  · props: `{"tipo": "seleccion de activos"}` · tramo [exacta]: «selección de los subyacentes a través de la gestión activa y discrecional»
- **o20 Obligacion** «Cesión efectiva de derechos — transferencia real» — Cesión efectiva tal que los créditos: a) sean deuda del obligado; b) fuera del alcance del cedente; c) cedidos sin CDS/derivado/garantía; d) no retitulizaciones. · props: `{"tipo": "otra"}` · tramo [exacta]: «deberá realizarse una cesión efectiva de derechos»
- **o21 Obligacion** «Cláusula de garantía de libre gravamen» — El contrato debe incluir garantía del originante de que los créditos no están gravados. · props: `{"tipo": "otra"}` · tramo [exacta]: «El contrato de cesión de los créditos deberá contener cláusulas»
- **o22 Obligacion** «Opinión legal independiente de transferencia real» — Documentación con opinión legal independiente sobre transferencia real conforme a)-d). · props: `{"tipo": "otra"}` · tramo [exacta]: «deberá incluir una opinión legal independiente»
- **o23 Obligacion** «Demostrar obstáculos legales y método de reclamo» — Si la legislación no se ajusta, demostrar obstáculos, especificar método de reclamo e informar eventos que retrasen la transferencia. · props: `{"tipo": "otra"}` · tramo [exacta]: «se deberá demostrar la existencia de los obstáculos que así lo impiden»
- **c4 Condicion** «Legislación no ajustada a a)-d)» — Legislación aplicable no se ajusta a a)-d) · tramo [exacta]: «En el caso de que la legislación aplicable a la titulización no se ajuste a lo previsto en los apartados a) a d) precedentes»
- **o24 Obligacion** «Información inicial por préstamo o tramo» — Información suficiente por préstamo o, en carteras atomizadas, por tramo, previa a la inversión. · props: `{"tipo": "otra"}` · tramo [exacta]: «se deberá contar con suficiente información a nivel de cada préstamo»
- **o25 Obligacion** «Suministro trimestral de datos al inversor» — Suministrar al menos trimestralmente datos por préstamo o tramo e informes estandarizados; fechas de corte alineadas. · props: `{"tipo": "otra", "frecuencia": "trimestral"}` · tramo [exacta]: «se deberá suministrar al menos trimestralmente durante la vida de la titulización datos»
- **o26 Obligacion** «Revisión de cartera inicial por contador independiente» — Cartera inicial revisada por contador público independiente. · props: `{"tipo": "otra"}` · tramo [exacta]: «la cartera inicial deberá ser revisada por un contador público independiente»
- R: o1 Obligacion —regula→ op1 Operacion
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: r1 Restriccion —prohibe→ op2 Operacion
- R: x1 Excepcion —exceptua_obligacion→ o10 Obligacion
- R: x2 Excepcion —exceptua_obligacion→ o15 Obligacion
- R: o14 Obligacion —condiciona→ op2 Operacion
- R: c3 Condicion —condicion_de→ o19 Obligacion
- R: c4 Condicion —condicion_de→ o23 Obligacion
- R: r3 Restriccion —prohibe→ op3 Operacion
- R: o20 Obligacion —regula→ op2 Operacion
- Omisión `meta_normativo` [exacta]: «Ello para evitar, por ejemplo, que se originen carteras con el solo fin de transferirlas.» — Finalidad
- Omisión `fuera_de_tipos` [exacta]: «Esta consideración no será condición para dar cumplimiento con el presente criterio.» — Evaluación de antecedentes del originante por el inversor no condiciona el criterio; Potestad/expectativa no deóntica
- Omisión `fuera_de_tipos` [exacta]: «Los inversores deberían poder evaluar el riesgo crediticio de la cartera de activos en forma previa a sus decisiones de inversión.» — Expectativa sin sujeto obligado claro; Obligacion recomendada

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «refinanciación distribuida» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ p1 Potestad |
| 2 | «valores residuales no significativos» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ p1 Potestad |
| 3 | «minoristas 5 años» | `dentro_de_norma` |  | dentro de la Obligacion o8 |
| 4 | «resto 7» | `dentro_de_norma` |  | dentro de la Obligacion o9 |
| 5 | «salvo el período de 2 años» | `condicion_con_relacion` |  | x1 Excepcion «Período de 2 años Ley 25.326» —exceptua_obligacion→ o10 Obligacion |
| 6 | «condiciones a) a d)» (a)) | `dentro_de_norma` |  | extraída como norma de otro tipo: o10 Obligacion «Sin quiebra o reestructuración del obligado 3 años» |
| 7 | «condiciones a) a d)» (b)) | `dentro_de_norma` |  | o11 Obligacion |
| 8 | «condiciones a) a d)» (c)) | `dentro_de_norma` |  | o12 Obligacion |
| 9 | «condiciones a) a d)» (d)) | `dentro_de_norma` |  | o13 Obligacion |

## `cap::3.1.2.2` — Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos.
> *heredado:* 3.1. Tratamiento de las titulizaciones.
> *heredado:* Se denomina "posición de titulización" a la exposición a una titulización (o retitulización), tradicional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes conceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos ("AssetBacked Securities", ABS) y bonos de titulización hipotecaria ("Mortgage-Backed Securities", MBS)–, mejoras crediticias, facilidades de liquidez, "swaps" de tasa de interés o de monedas y derivados de crédito. Las reservas ("reserve accounts"), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo también el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad económica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una determinada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> *heredado:* 3.1.2. Entidad financiera originante.
> *propio:* 3.1.2.2. Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional sólo si se satisface la totalidad de los siguientes requisitos operativos –debiendo computar exigencia de capital por las posiciones de titulización que conserve–: i) Se ha transferido a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas. ii) La entidad cedente no mantiene un control directo ni indirecto (como ser a través de una sociedad controlada) sobre las exposiciones transferidas. Ellas han sido aisladas de la cedente a los efectos jurídicos de forma tal que están fuera de su alcance y del de sus acreedores, incluso en los casos de liquidación o quiebra. Estas condiciones deberán estar avaladas por dictamen jurídico. Se considera que la cedente mantiene el control efectivo de las exposiciones transferidas si: a) puede recomprarlas con el objeto de realizar sus beneficios, o b) está obligada a conservar su riesgo. El mantenimiento por parte de la cedente de la administración de las exposiciones subyacentes no implicará un control indirecto sobre ellas. iii) Los títulos valores emitidos no son obligaciones de la cedente. En consecuencia, los inversores que compren los títulos valores sólo deberán tener derechos frente al conjunto subyacente de exposiciones. iv)La cesión se ha efectuado a un "Ente de Propósito Especial" (SPE) y los inversores pueden gravar o enajenar sus títulos valores sin restricción. v) Las opciones de exclusión satisfacen las condiciones estipuladas en el punto 3.1.4. vi)La titulización no contiene cláusulas mediante las cuales: a) se obligue a la originante a alterar las exposiciones subyacentes con el objeto de mejorar su calidad crediticia, a menos que esto se logre mediante su venta –a precios de mercado– a terceros no vinculados a ésta; b) la entidad financiera deba incrementar su posición a primera pérdida –es decir, su exposición al tramo que absorbe las pérdidas en primer término– o aumentar las mejoras crediticias provistas, con posterioridad al inicio de la operación; o c) se aumente el rendimiento pagadero a las partes distintas de la originante, como pueden ser los inversores o terceros proveedores de mejoras crediticias, en respuesta a un deterioro de la calidad crediticia de las exposiciones subyacentes. vii) No se incluyen opciones de rescisión o eventos desencadenantes de la extinción del contrato –excepto que se trate de opciones de exclusión admitidas (punto 3.1.4.) o que la extinción se deba a cambios impositivos o regulatorios específicos–, ni se incluyen cláusulas de amortización anticipada que –de acuerdo con lo previsto en el punto 3.1.8.1.– impliquen que la titulización no cumple con los requerimientos operacionales del presente punto.

### Extracción (código W)

- **op1 Operacion** «Exclusión de exposiciones titulizadas de APR» — Exclusión, por la entidad originante, de las exposiciones objeto de una titulización tradicional al calcular los activos ponderados por riesgo · props: `{"tipo": "calculo"}` · tramo [exacta]: «Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional»
- **p1 Potestad** «Facultad de excluir exposiciones de titulización tradicional» — Al calcular los APR, la entidad originante puede excluir las exposiciones objeto de una titulización tradicional solo si se cumplen todos los requisitos operativos i) a vii) · tramo [exacta]: «la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional sólo si se satisface la totalidad de los siguientes requisitos operativos»
- **o1 Obligacion** «Exigencia de capital por posiciones conservadas» — La entidad originante que excluya las exposiciones debe computar exigencia de capital por las posiciones de titulización que conserve · props: `{"tipo": "calculo"}` · tramo [exacta]: «debiendo computar exigencia de capital por las posiciones de titulización que conserve»
- **c1 Condicion** «Transferencia del riesgo de crédito a terceros» — Requisito i): riesgo de crédito de las exposiciones titulizadas transferido a uno o más terceros · tramo [exacta]: «Se ha transferido a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas.»
- **c2 Condicion** «Ausencia de control directo o indirecto de cedente» — Requisito ii): la cedente no mantiene control directo ni indirecto sobre las exposiciones transferidas · tramo [exacta]: «La entidad cedente no mantiene un control directo ni indirecto (como ser a través de una sociedad controlada) sobre las exposiciones transferidas.»
- **c3 Condicion** «Aislamiento jurídico de exposiciones de la cedente» — Requisito ii): exposiciones aisladas jurídicamente de la cedente y sus acreedores, incluso en liquidación o quiebra · tramo [exacta]: «Ellas han sido aisladas de la cedente a los efectos jurídicos de forma tal que están fuera de su alcance y del de sus acreedores, incluso en los casos de liquidación o quiebra.»
- **o2 Obligacion** «Dictamen jurídico que avale control y aislamiento» — Las condiciones de ausencia de control y aislamiento jurídico deben estar avaladas por dictamen jurídico · props: `{"tipo": "otra"}` · tramo [exacta]: «Estas condiciones deberán estar avaladas por dictamen jurídico.»
- **d1 Definicion** «Control efectivo de la cedente» — La cedente mantiene control efectivo si: a) puede recomprar las exposiciones para realizar sus beneficios, o b) está obligada a conservar su riesgo. Mantener la administración de las exposiciones subyacentes no implica control indirecto · props: `{"termino": "control efectivo"}` · tramo [exacta]: «Se considera que la cedente mantiene el control efectivo de las exposiciones transferidas si:»
- **c4 Condicion** «Títulos no son obligaciones de la cedente» — Requisito iii): títulos emitidos no son obligaciones de la cedente; inversores solo con derechos frente al conjunto subyacente · tramo [exacta]: «Los títulos valores emitidos no son obligaciones de la cedente.»
- **c5 Condicion** «Cesión a Ente de Propósito Especial» — Requisito iv): cesión efectuada a un SPE · tramo [exacta]: «La cesión se ha efectuado a un "Ente de Propósito Especial" (SPE)»
- **c6 Condicion** «Libre gravamen o enajenación por inversores» — Requisito iv): inversores pueden gravar o enajenar sus títulos sin restricción · tramo [exacta]: «los inversores pueden gravar o enajenar sus títulos valores sin restricción»
- **c7 Condicion** «Opciones de exclusión según punto 3.1.4» — Requisito v): opciones de exclusión cumplen condiciones del punto 3.1.4 · tramo [exacta]: «Las opciones de exclusión satisfacen las condiciones estipuladas en el punto 3.1.4.»
- **c8 Condicion** «Sin cláusula de alterar exposiciones subyacentes» — Requisito vi.a): sin cláusulas que obliguen a la originante a alterar las exposiciones para mejorar su calidad, salvo venta a precios de mercado a terceros no vinculados · tramo [exacta]: «se obligue a la originante a alterar las exposiciones subyacentes con el objeto de mejorar su calidad crediticia, a menos que esto se logre mediante su venta –a precios de mercado– a terceros no vinculados a ésta»
- **c9 Condicion** «Sin cláusula de incrementar primera pérdida» — Requisito vi.b): sin cláusulas que obliguen a incrementar la posición a primera pérdida o las mejoras crediticias tras el inicio de la operación · tramo [exacta]: «la entidad financiera deba incrementar su posición a primera pérdida»
- **c10 Condicion** «Sin aumento de rendimiento por deterioro crediticio» — Requisito vi.c): sin cláusulas que aumenten el rendimiento a partes distintas de la originante ante deterioro de la calidad crediticia de las exposiciones · tramo [exacta]: «se aumente el rendimiento pagadero a las partes distintas de la originante»
- **c11 Condicion** «Sin opciones de rescisión ni eventos de extinción» — Requisito vii): sin opciones de rescisión ni eventos de extinción, excepto opciones de exclusión admitidas (3.1.4) o extinción por cambios impositivos o regulatorios específicos · tramo [exacta]: «No se incluyen opciones de rescisión o eventos desencadenantes de la extinción del contrato»
- **c12 Condicion** «Sin amortización anticipada incumplidora (3.1.8.1)» — Requisito vii): sin cláusulas de amortización anticipada que, según 3.1.8.1, impliquen incumplimiento de los requisitos operacionales · tramo [exacta]: «ni se incluyen cláusulas de amortización anticipada que –de acuerdo con lo previsto en el punto 3.1.8.1.– impliquen que la titulización no cumple con los requerimientos operacionales del presente punto»
- R: p1 Potestad —aplica_a→ Sujeto (mención «la entidad originante»)
- R: o1 Obligacion —aplica_a→ Sujeto (mención «la entidad originante»)
- R: Sujeto (mención «la entidad originante») —ejecuta→ op1 Operacion
- R: op1 Operacion —requiere→ o1 Obligacion
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
- R: c11 Condicion —condicion_de→ p1 Potestad
- R: c12 Condicion —condicion_de→ p1 Potestad

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

### Extracción (código W)

- **d1 Definicion** «Miembro compensador (clearing member)» — Miembro (participante directo) de la CCP habilitado para realizar transacciones con dicha CCP, por cuenta propia o como intermediario entre la CCP y otros participantes del mercado. · props: `{"termino": "Miembro compensador"}` · tramo [exacta]: «Miembro compensador ("clearing member"): es un miembro –participante directo– de la CCP habilitado para realizar transacciones con dicha CCP, ya sea por cuenta propia o como intermediario entre la CCP y otros participantes del mercado.»
- **d2 Definicion** «CCP vinculada como miembro compensador» — A los efectos del cálculo de la exigencia de capital, cuando una CCP tenga vínculos con una segunda CCP, ésta es considerada miembro compensador respecto de la primera. · props: `{"termino": "Miembro compensador"}` · tramo [exacta]: «cuando una CCP tenga vínculos con una segunda CCP ésta será considerada como miembro compensador respecto de la primera»
- **c1 Condicion** «Acuerdos entre CCP definen tratamiento de garantías» — Según los acuerdos entre ambas CCP, las garantías aportadas por la segunda a la primera se tratan como margen inicial o como contribución a un fondo de garantía para incumplimientos (default fund). · tramo [exacta]: «Dependerá de los acuerdos entre ambas que las garantías aportadas por la segunda a la primera sean tratadas como margen inicial o contribución a un fondo de garantía»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:21 | sí | «A los efectos del cálculo de la exigencia de capital» | `ausente` |  | ningún tramo ni omisión lo cubre |

## `cap::5.2.1.3` — No deberá existir una correlación positiva sustancial entre la calidad crediticia

Grupos: omisiones.

### Texto

> *heredado:* Sección 5. Cobertura del riesgo de crédito.
> *heredado:* A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las técnicas previstas en el punto 5.1. La presente sección contempla, además, el cálculo de la exposición a las operaciones de financiación con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sección 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.
> *heredado:* 5.2. Requisitos para la aplicación de técnicas de coberturas del riesgo de crédito.
> *heredado:* 5.2.1. Requisitos generales.
> *propio:* 5.2.1.3. No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía –por ejemplo, los títulos valores emitidos por la contraparte o un vinculado a ella, no son admisibles–.

### Extracción (código W)

- **e1 Operacion** «Aplicación de técnicas de cobertura del riesgo de crédito» — Aplicación de técnicas de cobertura del riesgo de crédito (CRC) a efectos del cómputo de la exigencia de capital por riesgo de crédito · props: `{"tipo": "cobertura del riesgo de crédito"}` · tramo [exacta]: «Requisitos para la aplicación de técnicas de coberturas del riesgo de crédito»
- **e2 Restriccion** «Sin correlación positiva sustancial contraparte-garantía — CRC» — Requisito general para aplicar técnicas de CRC: no deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía»
- **e3 Restriccion** «Inadmisibles títulos de contraparte o vinculado — garantía CRC» — Por ejemplo, los títulos valores emitidos por la contraparte o un vinculado a ella no son admisibles como garantía para la cobertura del riesgo de crédito. · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «los títulos valores emitidos por la contraparte o un vinculado a ella, no son admisibles»
- R: e2 Restriccion —limita→ e1 Operacion
- R: e3 Restriccion —prohibe→ e1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:22 | no | «por ejemplo» | `ausente` |  | ningún tramo contiene «por ejemplo» ni omisión que lo registre |

## `cap::6.2.3.5` — Exigencia de capital por derivados.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 6. Capital mínimo por riesgo de mercado.
> *heredado:* 6.2. Exigencia de capital por riesgo de tasa de interés.
> *heredado:* La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títulos de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las acciones preferidas no convertibles. Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera. Las acciones preferidas convertibles a un precio predeterminado en acciones ordinarias de la emisora se tratarán según cómo se negocien, como títulos de deuda o como acciones. La exigencia se obtendrá como la suma de dos exigencias calculadas por separado: una por el riesgo específico de cada instrumento, ya sea que se trate de una posición vendida o comprada, y otra por el riesgo general de mercado –vinculado al efecto de cambios en la tasa de interés sobre la cartera–, en la que se podrán compensar las posiciones compradas y vendidas en diferentes instrumentos. Para los instrumentos derivados, serán de aplicación las disposiciones establecidas en el punto 6.2.3.
> *heredado:* 6.2.3. Tratamiento de los derivados de tasas de interés.
> *propio:* 6.2.3.5. Exigencia de capital por derivados. i) Compensación admitida entre posiciones compensadas. Las posiciones compradas y vendidas, reales o nocionales, en idénticos instrumentos se podrán excluir del cómputo del riesgo específico y del riesgo general de mercado. Se entiende que los instrumentos son idénticos si tienen igual emisor, cupón, moneda y vencimiento. Del mismo modo, si se corresponden exactamente, se podrán excluir los futuros o "forwards" y sus subyacentes, pero sin dejar de computar el lado de la operación que representa el plazo hasta el vencimiento de la operación a término. Cuando el futuro o "forward" permita entregar una gama de instrumentos, la exclusión sólo será posible en la medida que la entidad pueda identificar fácilmente el título subyacente cuya entrega es más conveniente para el intermediario con la posición vendida y demostrar que los cambios de los precios del título más barato ("cheapest-to-deliver") y del futuro o "forward" están estrechamente alineados. No se permitirá la exclusión o compensación de posiciones en diferentes monedas, por lo que los lados de los "swaps" de monedas y de los contratos a término sobre monedas se deberán tratar como posiciones nocionales en los instrumentos pertinentes e incluirse en el cálculo correspondiente a cada moneda. Asimismo, las entidades podrán excluir posiciones opuestas en la misma categoría de instrumentos si consideran que están compensadas, incluso en el caso de posiciones en el valor delta de una opción. Para que proceda la exclusión, las posiciones se deberán referir a los mismos subyacentes, tener el mismo valor nominal y estar denominadas en la misma moneda. Sujeto a las mismas condiciones, también se podrán compensar los lados de "swaps" diferentes. Además: a) cuando se trate de futuros, la exclusión sólo procederá si los nocionales e instrumentos subyacentes refieren a productos idénticos y sus vencimientos no difieren en más de 7 días corridos; b) cuando se trate de "swaps" y FRAs, la tasa de referencia de las posiciones a interés variable deberá ser idéntica y deberá haber una correspondencia cercana entre los cupones (dentro de un margen de 15 puntos básicos); c) en los casos de "swaps", FRAs y "forwards", la próxima fecha de reajuste del interés o el vencimiento -cuando se trate de posiciones con cupón fijo o "forwards"- se deberá producir: - a menos de un mes: en el mismo día; - entre un mes y un año: con una discrepancia máxima entre esas fechas de siete días corridos; - a un año: con una discrepancia máxima entre esas fechas de treinta días corridos. ii) Exigencia de capital por riesgo específico. Los "swaps" de monedas y tasas de interés, los FRAs, los "forwards" de moneda y los futuros de tasa de interés o sobre un índice de tasa de interés no estarán sujetos a exigencia por riesgo específico. No obstante, en el caso de futuros en los que el subyacente sea un título de deuda o un índice que represente una canasta de títulos de deuda, se aplicará la exigencia por riesgo específico acorde al riesgo de crédito del emisor, según se establece en el punto 6.2.1. iii) Exigencia de capital por riesgo general de mercado. La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las posiciones al contado-, con la sola excepción de las posiciones que estén compensadas con instrumentos idénticos, conforme a lo establecido en el acápite i) de este punto.

### Extracción (código W)

- **op1 Operacion** «Cálculo exigencia riesgo tasa por derivados» — Cálculo de la exigencia de capital por riesgo específico y general de mercado de tasa de interés para posiciones en instrumentos derivados · props: `{"tipo": "calculo"}` · tramo [exacta]: «Exigencia de capital por derivados.»
- **p1 Potestad** «Exclusión posiciones en idénticos instrumentos» — Las posiciones compradas y vendidas, reales o nocionales, en idénticos instrumentos pueden excluirse del cómputo del riesgo específico y general de mercado. · tramo [exacta]: «Las posiciones compradas y vendidas, reales o nocionales, en idénticos instrumentos se podrán excluir del cómputo del riesgo específico y del riesgo general de mercado.»
- **d1 Definicion** «Instrumentos idénticos» — Instrumentos con igual emisor, cupón, moneda y vencimiento. · props: `{"termino": "idénticos"}` · tramo [exacta]: «Se entiende que los instrumentos son idénticos si tienen igual emisor, cupón, moneda y vencimiento.»
- **p2 Potestad** «Exclusión futuros/forwards y sus subyacentes» — Si se corresponden exactamente, pueden excluirse los futuros o forwards y sus subyacentes, sin dejar de computar el lado que representa el plazo hasta el vencimiento de la operación a término. · tramo [exacta]: «si se corresponden exactamente, se podrán excluir los futuros o "forwards" y sus subyacentes»
- **c1 Condicion** «Correspondencia exacta futuro-subyacente» — Que el futuro o forward y su subyacente se correspondan exactamente. · tramo [exacta]: «si se corresponden exactamente»
- **o1 Obligacion** «Computar lado plazo de operación a término» — Al excluir futuros/forwards y subyacentes, debe seguir computándose el lado que representa el plazo hasta el vencimiento de la operación a término. · props: `{"tipo": "calculo"}` · tramo [exacta]: «pero sin dejar de computar el lado de la operación que representa el plazo hasta el vencimiento de la operación a término»
- **c2 Condicion** «Identificar fácilmente subyacente más conveniente» — Cuando el futuro o forward permita entregar una gama de instrumentos, la entidad debe poder identificar fácilmente el subyacente de entrega más conveniente para el vendedor. · tramo [exacta]: «la exclusión sólo será posible en la medida que la entidad pueda identificar fácilmente el título subyacente cuya entrega es más conveniente para el intermediario con la posición vendida»
- **c3 Condicion** «Precios cheapest-to-deliver y futuro alineados» — Demostrar que los cambios de precios del título más barato y del futuro o forward están estrechamente alineados (futuros con gama de entregables). · tramo [exacta]: «demostrar que los cambios de los precios del título más barato ("cheapest-to-deliver") y del futuro o "forward" están estrechamente alineados»
- **r1 Restriccion** «Prohibida compensación entre distintas monedas» — No se permite la exclusión o compensación de posiciones en diferentes monedas. · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «No se permitirá la exclusión o compensación de posiciones en diferentes monedas»
- **o2 Obligacion** «Swaps y término de monedas como nocionales» — Los lados de swaps de monedas y contratos a término sobre monedas deben tratarse como posiciones nocionales e incluirse en el cálculo de cada moneda. · props: `{"tipo": "calculo"}` · tramo [exacta]: «los lados de los "swaps" de monedas y de los contratos a término sobre monedas se deberán tratar como posiciones nocionales en los instrumentos pertinentes e incluirse en el cálculo correspondiente a cada moneda»
- **p3 Potestad** «Exclusión posiciones opuestas misma categoría» — Las entidades pueden excluir posiciones opuestas en la misma categoría de instrumentos si consideran que están compensadas, incluso posiciones en el valor delta de una opción. · tramo [exacta]: «las entidades podrán excluir posiciones opuestas en la misma categoría de instrumentos si consideran que están compensadas»
- **c4 Condicion** «Mismos subyacentes» — Las posiciones deben referirse a los mismos subyacentes. · tramo [exacta]: «las posiciones se deberán referir a los mismos subyacentes»
- **c5 Condicion** «Mismo valor nominal» — Las posiciones deben tener el mismo valor nominal. · tramo [exacta]: «tener el mismo valor nominal»
- **c6 Condicion** «Misma moneda de denominación» — Las posiciones deben estar denominadas en la misma moneda. · tramo [exacta]: «estar denominadas en la misma moneda»
- **p4 Potestad** «Compensación lados de swaps diferentes» — Sujeto a las mismas condiciones (mismos subyacentes, valor nominal y moneda), pueden compensarse lados de swaps diferentes. · tramo [exacta]: «Sujeto a las mismas condiciones, también se podrán compensar los lados de "swaps" diferentes.»
- **c7 Condicion** «Futuros: productos idénticos» — En futuros, la exclusión procede solo si nocionales y subyacentes refieren a productos idénticos. · tramo [exacta]: «cuando se trate de futuros, la exclusión sólo procederá si los nocionales e instrumentos subyacentes refieren a productos idénticos»
- **c8 Condicion** «Futuros: vencimientos difieren ≤7 días» — En futuros, los vencimientos no difieren en más de 7 días corridos. · umbral: ['no difieren en más de 7 días corridos'] · tramo [exacta]: «sus vencimientos no difieren en más de 7 días corridos»
- **c9 Condicion** «Swaps/FRAs: tasa de referencia idéntica» — En swaps y FRAs, la tasa de referencia de posiciones a interés variable debe ser idéntica. · tramo [exacta]: «la tasa de referencia de las posiciones a interés variable deberá ser idéntica»
- **c10 Condicion** «Swaps/FRAs: cupones dentro de 15 pb» — En swaps y FRAs, correspondencia cercana entre cupones dentro de 15 puntos básicos. · props: `{"umbrales": [{"tramo": "dentro de un margen de 15\npuntos básicos", "comparacion": "maximo_inclusivo", "base": "un margen de 15 puntos básicos", "regla_comparacion": "limite_relativo:compuesta:dentro_de", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['dentro de un margen de 15 puntos básicos'] · tramo [exacta]: «deberá haber una correspondencia cercana entre los cupones (dentro de un margen de 15 puntos básicos)»
- **c11 Condicion** «Reajuste a menos de un mes: mismo día» — Swaps, FRAs y forwards: si la próxima fecha de reajuste o vencimiento es a menos de un mes, debe coincidir el mismo día. · umbral: ['a menos de un mes'] · tramo [exacta]: «c) en los casos de "swaps", FRAs y "forwards", la próxima fecha de reajuste del interés o el vencimiento -cuando se trate de posiciones con cupón fijo o "forwards"- se deberá producir: […] - a menos de un mes: en el mismo día;»
- **c12 Condicion** «Reajuste entre 1 mes y 1 año: ≤7 días» — Swaps, FRAs y forwards: con reajuste/vencimiento entre un mes y un año, discrepancia máxima de siete días corridos. · umbral: ['entre un mes y un año', 'discrepancia máxima entre esas fechas de siete días corridos'] · tramo [exacta]: «entre un mes y un año: con una discrepancia máxima entre esas fechas de siete días corridos»
- **c13 Condicion** «Reajuste a un año: ≤30 días» — Swaps, FRAs y forwards: con reajuste/vencimiento a un año, discrepancia máxima de treinta días corridos. · props: `{"umbrales": [{"tramo": "discrepancia máxima entre esas fechas de trein-\nta días corridos", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['a un año', 'discrepancia máxima entre esas fechas de treinta días corridos'] · tramo [exacta]: «a un año: con una discrepancia máxima entre esas fechas de treinta días corridos»
- **x1 Excepcion** «Swaps, FRAs, forwards y futuros tasa: sin riesgo específico» — Swaps de monedas y tasas, FRAs, forwards de moneda y futuros de tasa o índice de tasa quedan fuera de la exigencia por riesgo específico. · tramo [exacta]: «Los "swaps" de monedas y tasas de interés, los FRAs, los "forwards" de moneda y los futuros de tasa de interés o sobre un índice de tasa de interés no estarán sujetos a exigencia por riesgo específico.»
- **o3 Obligacion** «Riesgo específico en futuros sobre títulos de deuda» — Para futuros cuyo subyacente sea un título de deuda o índice de canasta de títulos de deuda, se aplica exigencia por riesgo específico según el riesgo de crédito del emisor (punto 6.2.1). · props: `{"tipo": "calculo"}` · tramo [exacta]: «en el caso de futuros en los que el subyacente sea un título de deuda o un índice que represente una canasta de títulos de deuda, se aplicará la exigencia por riesgo específico acorde al riesgo de crédito del emisor»
- **o4 Obligacion** «Riesgo general alcanza todas las posiciones derivadas» — La exigencia por riesgo general de mercado alcanza a todas las posiciones en derivados, como a las de contado. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados»
- **x2 Excepcion** «Posiciones compensadas idénticas: sin riesgo general» — Quedan fuera de la exigencia por riesgo general de mercado las posiciones compensadas con instrumentos idénticos (acápite i). · tramo [exacta]: «con la sola excepción de las posiciones que estén compensadas con instrumentos idénticos»
- R: c1 Condicion —condicion_de→ p2 Potestad
- R: c2 Condicion —condicion_de→ p2 Potestad
- R: c3 Condicion —condicion_de→ p2 Potestad
- R: c4 Condicion —condicion_de→ p3 Potestad
- R: c5 Condicion —condicion_de→ p3 Potestad
- R: c6 Condicion —condicion_de→ p3 Potestad
- R: c4 Condicion —condicion_de→ p4 Potestad
- R: c5 Condicion —condicion_de→ p4 Potestad
- R: c6 Condicion —condicion_de→ p4 Potestad
- R: c7 Condicion —condicion_de→ p3 Potestad
- R: c8 Condicion —condicion_de→ p3 Potestad
- R: c9 Condicion —condicion_de→ p3 Potestad
- R: c10 Condicion —condicion_de→ p3 Potestad
- R: c11 Condicion —condicion_de→ p3 Potestad
- R: c12 Condicion —condicion_de→ p3 Potestad
- R: c13 Condicion —condicion_de→ p3 Potestad
- R: p3 Potestad —aplica_a→ Sujeto_rol_alcance_capmin (mención «las entidades»)
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o4 Obligacion —regula→ op1 Operacion
- R: r1 Restriccion —limita→ op1 Operacion
- R: x2 Excepcion —exceptua_obligacion→ o4 Obligacion
- Omisión `relacion_sin_predicado` [exacta]: «No obstante, en el caso de futuros» — o3 es una contra-excepción a x1; ningún predicado une Obligacion con Excepcion. La exigencia general por riesgo específico (6.2.1) no está en la unidad, así que x1 va sin exceptua_obligacion.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «instrumentos idénticos» | `dentro_de_norma` |  | dentro de la Potestad p1 y como Definicion d1; sin Condicion |
| 2 | «futuro con gama de instrumentos» | `condicion_con_relacion` |  | c2 y c3 Condicion —condicion_de→ p2 Potestad |
| 3 | «a) futuros a 7 días» | `condicion_con_relacion` |  | c8 Condicion con el umbral (y c7) —condicion_de→ p3 Potestad |
| 4 | «b) swaps y FRAs» | `condicion_con_relacion` |  | c9 y c10 Condicion (con el umbral de 15 pb) —condicion_de→ p3 Potestad |
| 5 | «c) tramos de fechas» | `condicion_con_relacion` |  | c11, c12 y c13 Condicion con los umbrales —condicion_de→ p3 Potestad |
| 6 | «futuros sobre títulos» | `dentro_de_norma` |  | extraído como norma de otro tipo: o3 Obligacion; sin Excepcion ni Condicion (la omisión declara la contra-excepción sin predicado) |

## `cap::6.3.2.2` — Exigencia de capital por derivados sobre acciones.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 6. Capital mínimo por riesgo de mercado.
> *heredado:* 6.3. Exigencia de capital por riesgo de posiciones en acciones.
> *heredado:* La exigencia de capital por el riesgo de mantener posiciones en acciones en la cartera de negociación alcanza a las posiciones compradas y vendidas en acciones ordinarias, títulos de deuda convertibles que se comporten como acciones y los compromisos para adquirir o vender acciones, así como en todo otro instrumento que tenga un comportamiento en el mercado similar al de las acciones, excluyendo a las acciones preferidas no convertibles, a las que se aplicará la exigencia por riesgo de tasa de interés descripta en el punto 6.2. Las posiciones compradas y vendidas en la misma especie podrán computarse en términos netos.
> *heredado:* 6.3.2. Tratamiento de los derivados sobre acciones.
> *heredado:* A excepción de las opciones sobre acciones e índices bursátiles, que se tratan en el punto 6.6., los restantes derivados sobre acciones y las posiciones fuera de balance sensibles a los cambios en los precios de mercado deberán incluirse en el cómputo de la exigencia. Esto comprende a los futuros, "forwards" y "swaps", tanto de acciones individuales como de índices bursátiles. Los derivados se convertirán en posiciones en su correspondiente subyacente.
> *propio:* 6.3.2.2. Exigencia de capital por derivados sobre acciones. i) Exigencia de capital por riesgo específico y por riesgo general de mercado. Cada posición compensada con una acción o índice bursátil idéntico podrá ser neteada en su totalidad, dando lugar a una única posición neta, vendida o comprada, sobre la que se aplicarán las exigencias de capital por riesgo específico y riesgo general de mercado. El riesgo de tasa de interés del derivado se computará conforme a lo indicado en el punto 6.2. ii) Exigencia de capital por índices. Además de la exigencia por riesgo general de mercado, se aplicará una exigencia de capital adicional de 2% de la posición neta, comprada o vendida, en contratos sobre índices calculados sobre carteras diversificadas de acciones a los efectos de cubrir factores tales como los riesgos de ejecución. Será objeto de revisión por parte de la Superintendencia de Entidades Financieras y Cambiarias que el ponderador de 2% se aplique sólo a índices bien diversificados y no, por ejemplo, a índices sectoriales. iii) Arbitraje. a) En el caso de las siguientes estrategias de arbitraje relacionadas con futuros, la exigencia de capital adicional de 2% del acápite ii) precedente se podrá aplicar sólo a uno de los índices (quedando exenta la posición contraria): - cuando la entidad asuma la posición contraria en exactamente el mismo índice pero a distintos vencimientos o mercados; - cuando la entidad mantenga la posición opuesta en contratos a idéntica fecha pero en índices diferentes, aunque similares, a cuyo efecto deberá tener a disposición de la Superintendencia de Entidades Financieras y Cambiarias evidencia de que ambos índices contienen suficientes componentes comunes como para justificar tal compensación. b) Se aplicará una exigencia de capital de 4% a las posiciones que surjan de estrategias de arbitraje, en las que un futuro sobre un índice amplio se calce con una canasta de acciones y, además, se verifique que: - la estrategia haya sido adoptada en forma deliberada y se vigile y gestione en forma particularizada; - la composición de la canasta de acciones represente al menos el 90% del índice si se descompone en sus componentes nocionales; - la exigencia de capital de 4%, que refleja los riesgos de divergencia y ejecución, equivale a una exigencia de 2% del valor bruto de las posiciones en cada lado. La exigencia es aplicable incluso si todas las acciones se mantienen en proporciones idénticas a las del índice. Cualquier valor excedente de las acciones que componen la canasta por encima del valor del futuro o cualquier valor excedente del futuro sobre el valor de la canasta se considerará como una posición abierta, comprada o vendida. c) Se podrán compensar –es decir, no aplicar exigencias de capital– posiciones contrarias, incluso tratándose de posiciones en mercados diferentes o de certificados de depósito de acciones sólo si se tienen en cuenta todos los costos de conversión, cuando los hubiera. Todo riesgo de tipo de cambio que surja de estas posiciones deberá computarse según se establece en el punto 6.4.

### Extracción (código W)

- **op1 Operacion** «Exigencia de capital por derivados sobre acciones» — Cómputo de la exigencia de capital por riesgo de posiciones en derivados sobre acciones e índices bursátiles · props: `{"tipo": "cálculo de exigencia de capital"}` · tramo [exacta]: «Exigencia de capital por derivados sobre acciones.»
- **p1 Potestad** «Neteo de posiciones compensadas idénticas» — Cada posición compensada con una acción o índice bursátil idéntico podrá netearse en su totalidad, dando una única posición neta sobre la que se aplican las exigencias por riesgo específico y general de mercado · tramo [exacta]: «Cada posición compensada con una acción o índice bursátil idéntico podrá ser neteada en su totalidad»
- **o1 Obligacion** «Riesgo de tasa del derivado según 6.2» — El riesgo de tasa de interés del derivado se computa conforme al punto 6.2 · props: `{"tipo": "calculo"}` · tramo [exacta]: «El riesgo de tasa de interés del derivado se computará conforme a lo indicado en el punto 6.2.»
- **r1 Restriccion** «Adicional 2% — contratos sobre índices diversificados» — Además de la exigencia por riesgo general de mercado, exigencia adicional de 2% de la posición neta, comprada o vendida, en contratos sobre índices calculados sobre carteras diversificadas de acciones, para cubrir riesgos de ejecución · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['exigencia de capital adicional de 2% de la posición neta'] · tramo [exacta]: «se aplicará una exigencia de capital adicional de 2% de la posición neta»
- **pt1 Potestad** «Revisión SEFyC del ponderador 2%» — La SEFyC revisa que el ponderador de 2% se aplique sólo a índices bien diversificados y no a índices sectoriales · tramo [exacta]: «Será objeto de revisión por parte de la Superintendencia de Entidades Financieras y Cambiarias que el ponderador de 2% se aplique sólo a índices bien diversificados»
- **x1 Excepcion** «Arbitraje con futuros: 2% sólo a un índice» — En las estrategias de arbitraje con futuros enumeradas, el adicional de 2% se aplica sólo a uno de los índices, quedando exenta la posición contraria (alcanza cualquiera de los supuestos) · umbral: ['exigencia de capital adicional de 2%'] · tramo [exacta]: «la exigencia de capital adicional de 2% del acápite ii) precedente se podrá aplicar sólo a uno de los índices (quedando exenta la posición contraria)»
- **c1 Condicion** «Mismo índice, distintos vencimientos o mercados» — La entidad asume la posición contraria en el mismo índice a distintos vencimientos o mercados (supuesto alternativo) · tramo [exacta]: «cuando la entidad asuma la posición contraria en exactamente el mismo índice pero a distintos vencimientos o mercados»
- **c2 Condicion** «Misma fecha, índices diferentes similares» — La entidad mantiene posición opuesta en contratos a idéntica fecha en índices diferentes aunque similares (supuesto alternativo) · tramo [exacta]: «cuando la entidad mantenga la posición opuesta en contratos a idéntica fecha pero en índices diferentes, aunque similares»
- **o2 Obligacion** «Evidencia de componentes comunes a disposición SEFyC» — Para compensar índices diferentes similares, la entidad debe tener a disposición de la SEFyC evidencia de que ambos índices contienen suficientes componentes comunes · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «deberá tener a disposición de la Superintendencia de Entidades Financieras y Cambiarias evidencia de que ambos índices contienen suficientes componentes comunes»
- **r2 Restriccion** «Exigencia 4% — arbitraje futuro índice vs canasta» — Exigencia de 4% a posiciones de arbitraje en que un futuro sobre índice amplio se calza con una canasta de acciones, equivalente a 2% del valor bruto de cada lado; aplicable aun con proporciones idénticas al índice; los excedentes de valor entre canasta y futuro se consideran posición abierta · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['exigencia de capital de 4%', 'equivale a una exigencia de 2% del valor bruto de las posiciones en cada lado'] · tramo [exacta]: «Se aplicará una exigencia de capital de 4% a las posiciones que surjan de estrategias de arbitraje»
- **c3 Condicion** «Futuro sobre índice amplio calzado con canasta» — Un futuro sobre índice amplio se calza con una canasta de acciones · tramo [exacta]: «en las que un futuro sobre un índice amplio se calce con una canasta de acciones»
- **c4 Condicion** «Estrategia deliberada, vigilada y gestionada» — La estrategia fue adoptada deliberadamente y se vigila y gestiona en forma particularizada · tramo [exacta]: «la estrategia haya sido adoptada en forma deliberada y se vigile y gestione en forma particularizada»
- **c5 Condicion** «Canasta representa al menos 90% del índice» — La canasta representa al menos el 90% del índice descompuesto en componentes nocionales · umbral: ['represente al menos el 90% del índice'] · tramo [exacta]: «la composición de la canasta de acciones represente al menos el 90% del índice»
- **p2 Potestad** «Compensación de posiciones contrarias sin exigencia» — Se pueden compensar posiciones contrarias, incluso en mercados diferentes o certificados de depósito de acciones, sin aplicar exigencia · tramo [exacta]: «Se podrán compensar –es decir, no aplicar exigencias de capital– posiciones contrarias»
- **c6 Condicion** «Considerar todos los costos de conversión» — Se tienen en cuenta todos los costos de conversión, cuando los hubiera · tramo [exacta]: «sólo si se tienen en cuenta todos los costos de conversión, cuando los hubiera»
- **o3 Obligacion** «Riesgo cambiario de compensaciones según 6.4» — El riesgo de tipo de cambio de estas posiciones se computa según el punto 6.4 · props: `{"tipo": "calculo"}` · tramo [exacta]: «Todo riesgo de tipo de cambio que surja de estas posiciones deberá computarse según se establece en el punto 6.4.»
- R: o1 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: r1 Restriccion —limita→ op1 Operacion
- R: r2 Restriccion —limita→ op1 Operacion
- R: x1 Excepcion —exceptua→ r1 Restriccion
- R: c1 Condicion —condicion_de→ x1 Excepcion
- R: c2 Condicion —condicion_de→ x1 Excepcion
- R: c3 Condicion —condicion_de→ r2 Restriccion
- R: c4 Condicion —condicion_de→ r2 Restriccion
- R: c5 Condicion —condicion_de→ r2 Restriccion
- R: c6 Condicion —condicion_de→ p2 Potestad
- R: pt1 Potestad —aplica_a→ Sujeto_sefyc (mención «Superintendencia de Entidades Financieras y Cambiarias»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- R: x1 Excepcion —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- Omisión `relacion_sin_predicado` [exacta]: «a cuyo efecto deberá tener a disposición» — La obligación de evidencia es requisito del supuesto c2; no hay predicado Obligacion→Condicion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «arbitrajes del a) (dos guiones)» (primer guion) | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ x1 Excepcion |
| 2 | «arbitrajes del a) (dos guiones)» (segundo guion) | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ x1 Excepcion |
| 3 | «b) canasta de al menos 90 %» | `condicion_con_relacion` |  | c5 Condicion con el umbral —condicion_de→ r2 Restriccion (la exigencia del 4 %, extraída como Restriccion) |
| 4 | «c) sólo si se tienen en cuenta los costos» | `condicion_con_relacion` |  | c6 Condicion —condicion_de→ p2 Potestad |

## `cap::7.1.3::intro` — [bloque intro] Divulgación.

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Capital mínimo por riesgo operacional.
> *heredado:* 7.1. Exigencia de capital por riesgo operacional para entidades del grupo 1.
> *heredado:* 7.1.3. Divulgación.
> *propio:* Las entidades financieras deben dar a conocer al público, de manera regular, a través de sus páginas de Internet o reportes –conforme a los requerimientos que al efecto se establezcan– lo siguiente:

### Extracción (código W)

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

### Extracción (código W)

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

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «grupo B (17 %)» | `dentro_de_norma` |  | dentro de la Restriccion r1; sin Condicion |
| 2 | «calificación 1, 2 o 3 (11 %)» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ r2 Restriccion |
| 3 | «calificación 1 o 2 (7 %)» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ r3 Restriccion |

## `cap::8.2.3::cierre` — [bloque cierre] Patrimonio neto complementario –capital de nivel dos– (PNc).

Grupos: omisiones.

### Texto

> *heredado:* Sección 8. Responsabilidad patrimonial computable.
> *heredado:* 8.2. Conceptos computables.
> *heredado:* 8.2.3. Patrimonio neto complementario –capital de nivel dos– (PNc).
> *propio:* A los conceptos citados en los puntos precedentes se les restarán, de corresponder, los conceptos deducibles previstos en el punto 8.4.2.

### Extracción (código W)

- **e1 Obligacion** «Restar conceptos deducibles 8.4.2 — PNc» — En el cómputo del patrimonio neto complementario (capital de nivel dos), a los conceptos citados en los puntos precedentes se les restarán, de corresponder, los conceptos deducibles previstos en el punto 8.4.2. · props: `{"tipo": "calculo"}` · tramo [exacta]: «A los conceptos citados en los puntos precedentes se les restarán, de corresponder, los conceptos deducibles previstos en el punto 8.4.2.»
- **e2 Operacion** «Cómputo del patrimonio neto complementario (PNc)» — Determinación del patrimonio neto complementario –capital de nivel dos– (PNc) de la responsabilidad patrimonial computable · props: `{"tipo": "calculo"}` · tramo [exacta]: «Patrimonio neto complementario –capital de nivel dos– (PNc).»
- R: e1 Obligacion —regula→ e2 Operacion

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

### Extracción (código W)

- **d1 Definicion** «ON y títulos de deuda de FF — financiaciones comprendidas» — Las financiaciones comprendidas incluyen las obligaciones negociables (incluidas las subordinadas) y los títulos de deuda de fideicomisos financieros no alcanzados por las normas sobre "Fideicomisos financieros comprendidos en la Ley de Entidades Financieras", valuados a costo amortizado y/o a valor razonable con cambios en otros resultados integrales. · props: `{"termino": "Financiaciones comprendidas"}` · tramo [exacta]: «Obligaciones negociables –incluye las subordinadas– y títulos de deuda de fideicomisos financieros no alcanzados por las normas sobre "Fideicomisos financieros comprendidos en la Ley de Entidades Financieras", valuados a costo amortizado y/o a valor razonable con cambios en otros resultados integrales.»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:9 | sí | «no alcanzados por las normas sobre "Fideicomisos financieros comprendidos en la Ley de Entidades Financieras"» | `extraida_tramo_verificado` |  | d1 Definicion [exacta], tramo que contiene el fragmento |

## `cla::2.2.4.4` — En el caso de las garantías otorgadas localmente, deberán existir respecto de

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Financiaciones comprendidas.
> *heredado:* 2.2. Exclusiones.
> *heredado:* 2.2.4. Financiaciones y avales, fianzas y otras responsabilidades otorgados por sucursales y
> *heredado:* subsidiarias locales de entidades financieras del exterior, por cuenta y orden de su casa matriz o sus sucursales en otros países o de la entidad controlante, siempre que se observen los siguientes requisitos:
> *propio:* 2.2.4.4. En el caso de las garantías otorgadas localmente, deberán existir respecto de ellas contragarantías extendidas por la casa matriz o sus sucursales en otros países o por la entidad controlante del exterior, cuya efectivización opere en forma irrestricta a simple requerimiento de la filial o subsidiaria local y en modo inmediato a su eventual ejecución por parte del beneficiario.

### Extracción (código W)

- **c1 Condicion** «Contragarantías del exterior para garantías locales» — Requisito (exigido junto con los demás del punto 2.2.4) para la exclusión de las normas de clasificación de las financiaciones, avales, fianzas y otras responsabilidades otorgados por sucursales y subsidiarias locales de entidades financieras del exterior por cuenta y orden de su casa matriz, sus sucursales en otros países o la entidad controlante: en el caso de garantías otorgadas localmente, deb… · tramo [exacta]: «En el caso de las garantías otorgadas localmente, deberán existir respecto de ellas contragarantías extendidas por la casa matriz o sus sucursales en otros países o por la entidad controlante del exterior, cuya efectivización opere en forma irrestricta a simple requerimiento de la filial o subsidiaria local y en modo i…»

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

### Extracción (código W)

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

### Extracción (código W)

- **d1 Definicion** «Indicador situación normal: liquidez y alta capacidad de pago» — Es uno de los indicadores (no excluyentes) que pueden reflejar la situación normal en la cartera comercial: el cliente presenta una situación financiera líquida, con bajo nivel y adecuada estructura de endeudamiento en relación con su capacidad de ganancia, y muestra una alta capacidad de pago de las deudas (capital e intereses) en las condiciones pactadas generando fondos —medido a través del aná… · props: `{"termino": "En situación normal"}` · tramo [exacta]: «Entre los indicadores que pueden reflejar esta situación se destacan que el cliente: […] presente una situación financiera líquida, con bajo nivel y adecuada estructura»
- **op1 Operacion** «Análisis para clasificación de deudor cartera comercial» — Análisis de la capacidad de pago del cliente para su clasificación en la cartera comercial · props: `{"tipo": "clasificación de deudores"}` · tramo [exacta]: «En el análisis que se lleve a cabo»
- **o1 Obligacion** «Considerar incidencia del grupo de contrapartes conectadas» — En el análisis de clasificación deberá tenerse en cuenta, de corresponder, la eventual incidencia en la capacidad de pago del cliente de la situación de los demás integrantes del grupo de contrapartes conectadas al que pertenece. · props: `{"tipo": "otra"}` · tramo [exacta]: «En el análisis que se lleve a cabo deberá tenerse en cuenta, de corresponder, la eventual incidencia que en su capacidad de pago pueda tener la situación en la que se encuentran los demás integrantes del grupo de contrapartes conectadas al cual pertenece.»
- R: o1 Obligacion —regula→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_obligado_a_clasificar_clasificacion (mención «la entidad»)

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

### Extracción (código W)

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

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «sin cancelar el 15 %» | `sin_relacion` | norma_presente | e2 Condicion con el umbral, sin relación (la salida lo declara en una omisión relacion_sin_predicado); el indicador está en la unidad como e1 Condicion |
| 2 | «acuerdo alcanzado en alto riesgo o irrecuperable» | `sin_relacion` | norma_presente | e3 Condicion sin relación (ídem, omisión relacion_sin_predicado) |
| 3 | «acuerdos de más de 2,5 veces el importe de referencia» | `condicion_con_relacion` |  | e7 Condicion con el umbral —condicion_de→ e9 Obligacion y → e6 Operacion |

## `cla::6.5.3.7` — Incurra en atrasos recurrentes, incumplimiento de hasta 180 días respecto de

Grupos: omisiones.

### Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.3. Con problemas.
> *heredado:* El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos, esos problemas pueden resultar en una pérdida para la entidad financiera. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *propio:* 6.5.3.7. Incurra en atrasos recurrentes, incumplimiento de hasta 180 días respecto de condiciones contractuales o nulo movimiento en las cuentas con la entidad.

### Extracción (código W)

- **c1 Condicion** «Atrasos recurrentes — indicador situación Con problemas» — Indicador (alternativo) de que el cliente de cartera comercial está en la categoría 'Con problemas' (6.5.3): que incurra en atrasos recurrentes. · tramo [exacta]: «Incurra en atrasos recurrentes»
- **c2 Condicion** «Incumplimiento hasta 180 días — indicador Con problemas» — Indicador (alternativo) de clasificación 'Con problemas' (6.5.3): incumplimiento de hasta 180 días respecto de condiciones contractuales. · umbral: ['hasta 180 días'] · tramo [exacta]: «incumplimiento de hasta 180 días respecto de condiciones contractuales»
- **c3 Condicion** «Nulo movimiento en cuentas — indicador Con problemas» — Indicador (alternativo) de clasificación 'Con problemas' (6.5.3): nulo movimiento en las cuentas del cliente con la entidad. · tramo [exacta]: «nulo movimiento en las cuentas con la entidad»

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

### Extracción (código W)

- **c1 Condicion** «Refinanciaciones por insuficiente capacidad de pago — indicador alto riesgo» — Indicador de la categoría 'con alto riesgo de insolvencia' (6.5.4): el cliente cuenta con refinanciaciones del capital e intereses vinculadas a una insuficiente capacidad de pago, con quitas o con reducción de tasas pactadas, o cuando haya sido necesario recibir bienes en pago de parte de las obligaciones. Es uno de varios indicadores no taxativos. · tramo [exacta]: «Entre los indicadores que pueden reflejar esta situación se destacan que el cliente: […] Cuente con refinanciaciones del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad para su pago, con otorgamiento de quitas o con reducción en las tasas de interés pactadas»
- **x1 Excepcion** «Reducción de tasas por condiciones de mercado — no indicador» — La reducción de tasas pactadas no cuenta como indicador de alto riesgo de insolvencia cuando deriva de las condiciones del mercado. · tramo [exacta]: «salvo que ello derive de las condiciones del mercado»
- **p1 Potestad** «Recategorización directa a niveles superiores tras quitas» — El deudor refinanciado con quitas de capital podrá ser recategorizado directamente en 'con problemas' o 'en observación' por aplicación de la metodología del punto 2.2.6 de Previsiones mínimas por riesgo de incobrabilidad. · tramo [exacta]: «el deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital podrá ser recategorizado directamente en niveles superiores ("con problemas", "en observación")»
- **c2 Condicion** «Otras condiciones de la categoría observadas — recategorización directa» — Que se observen además las otras condiciones previstas en las categorías superiores correspondientes. · tramo [exacta]: «siempre que además se observen las otras condiciones previstas en las correspondientes categorías»
- **p2 Potestad** «Reclasificación al nivel inmediato superior tras pagos» — El deudor refinanciado podrá ser reclasificado en el nivel inmediato superior. · tramo [exacta]: «podrá reclasificárselo en el nivel inmediato superior»
- **c3 Condicion** «Pago del 10 % de refinanciación sin atrasos» — Haber pagado al menos el 10 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, más el porcentaje acumulado que correspondería de haber estado el deudor en la categoría inferior, sin atrasos superiores a 31 días. · umbral: ['sin haber incurrido en atrasos superiores a los 31 días', 'al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores…'] · tramo [exacta]: «Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 10 % de las obligaciones refinanciadas y la totalidad de los intereses devengados»
- **c4 Condicion** «Otras condiciones del nivel superior observadas — reclasificación» — Que se observen además las otras condiciones del nivel inmediato superior. · tramo [exacta]: «si, además, se observan las otras condiciones previstas en el citado nivel»
- **o1 Obligacion** «Permanencia mínima 180 días en alto riesgo» — El deudor clasificado en alto riesgo de insolvencia que haya refinanciado (aun habiendo cancelado el porcentaje del párrafo precedente) y recibido crédito adicional según el punto 2.2.5 de Previsiones mínimas, no cancelado, debe permanecer en esta categoría al menos 180 días desde el crédito adicional o el acuerdo de refinanciación, lo más reciente. · props: `{"tipo": "asignacion"}` · umbral: ['por lo menos 180 días'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente»
- **c5 Condicion** «Refinanciación con crédito adicional no cancelado» — Que el deudor haya refinanciado y recibido crédito adicional (punto 2.2.5 de Previsiones mínimas) aún no cancelado. · tramo [exacta]: «y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada»
- **x2 Excepcion** «Otras pautas exigen nivel inferior — permanencia 180 días» — La permanencia mínima no impide categorizarlo en el nivel inferior si otras pautas lo exigen. · tramo [exacta]: «salvo que por aplicación de otras pautas corresponda categorizarlo en el nivel inferior»
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p2 Potestad
- R: c4 Condicion —condicion_de→ p2 Potestad
- R: c5 Condicion —condicion_de→ o1 Obligacion
- R: x2 Excepcion —exceptua_obligacion→ o1 Obligacion
- Omisión `relacion_sin_predicado` [exacta]: «salvo que ello derive de las condiciones del mercado» — La excepción acota una Condicion (indicador); exceptua solo admite Restriccion/Obligacion.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «bienes en pago» | `fusionado` |  | c1 Condicion (el indicador, sin relación) junta «bienes en pago» con los otros supuestos del indicador (descripción) |
| 2 | «recategorización siempre que…» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ p1 Potestad |
| 3 | «pago del 10 %» | `condicion_con_relacion` |  | c3 Condicion con los umbrales —condicion_de→ p2 Potestad |
| 4 | «financiación adicional sin cancelar» | `condicion_con_relacion` |  | c5 Condicion —condicion_de→ o1 Obligacion |
| 5 | «salvo otras pautas» | `condicion_con_relacion` |  | x2 Excepcion —exceptua_obligacion→ o1 Obligacion |

## `cla::6.5.4.7` — Haya solicitado el concurso preventivo, celebrado un acuerdo preventivo extraju-

Grupos: omisiones.

### Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.4. Con alto riesgo de insolvencia.
> *heredado:* El análisis del flujo de fondos del cliente demuestra que es altamente improbable que pueda atender la totalidad de sus compromisos financieros. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *propio:* 6.5.4.7. Haya solicitado el concurso preventivo, celebrado un acuerdo preventivo extrajudicial aún no homologado o se le haya requerido su quiebra, en tanto no hubiere sido declarada, por obligaciones que sean iguales o superiores al 20 % del patrimonio del cliente o por obligaciones entre el 5 % y menos del 20 % del patrimonio cuando persista el pedido de quiebra luego de transcurridos 90 días desde que ésta haya sido requerida. En caso de levantarse el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores, según la situación previa, si se observan las condiciones allí previstas. En el caso de deudores que hayan solicitado el concurso preventivo o acuerdo preventivo extrajudicial aún no homologado, corresponderá la reclasificación inmediata en el nivel siguiente inferior cuando se verifiquen atrasos de más de 540 días.

### Extracción (código W)

- **c1 Condicion** «Concurso o quiebra por obligaciones ≥20% patrimonio» — Indicador de la categoría 'Con alto riesgo de insolvencia' (6.5.4): el cliente solicitó concurso preventivo, celebró acuerdo preventivo extrajudicial no homologado o se le requirió la quiebra (no declarada), por obligaciones iguales o superiores al 20 % de su patrimonio. · umbral: ['iguales o superiores al 20 % del patrimonio del cliente'] · tramo [exacta]: «Haya solicitado el concurso preventivo, celebrado un acuerdo preventivo extrajudicial aún no homologado o se le haya requerido su quiebra, en tanto no hubiere sido declarada, por obligaciones que sean iguales o superiores al 20 % del patrimonio del cliente»
- **c2 Condicion** «Pedido de quiebra 5%-20% persistente 90 días» — Indicador de la categoría 'Con alto riesgo de insolvencia' (6.5.4): obligaciones entre el 5 % y menos del 20 % del patrimonio cuando el pedido de quiebra persiste luego de 90 días desde que fue requerida. · umbral: ['entre el 5 % y menos del 20 % del patrimonio', 'luego de transcurridos 90 días desde que ésta haya sido requerida'] · tramo [exacta]: «por obligaciones entre el 5 % y menos del 20 % del patrimonio cuando persista el pedido de quiebra luego de transcurridos 90 días desde que ésta haya sido requerida»
- **op1 Operacion** «Reclasificación en niveles superiores tras levantar quiebra» — Reclasificación del deudor en niveles superiores, según la situación previa, al levantarse el pedido de quiebra. · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «el deudor podrá ser reclasificado en niveles superiores, según la situación previa»
- **p1 Potestad** «Reclasificar en niveles superiores al levantarse quiebra» — Levantado el pedido de quiebra, el deudor puede ser reclasificado en niveles superiores según la situación previa, si se observan las condiciones allí previstas. · tramo [exacta]: «En caso de levantarse el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores, según la situación previa, si se observan las condiciones allí previstas.»
- **c3 Condicion** «Levantamiento del pedido de quiebra» — Que se levante el pedido de quiebra. · tramo [exacta]: «En caso de levantarse el pedido de quiebra»
- **c4 Condicion** «Condiciones del nivel superior observadas» — Que se observen las condiciones previstas para el nivel superior según la situación previa. · tramo [exacta]: «si se observan las condiciones allí previstas»
- **o1 Obligacion** «Reclasificación inmediata nivel inferior por atrasos >540 días» — Para deudores con concurso preventivo o acuerdo preventivo extrajudicial no homologado, corresponde reclasificarlos inmediatamente en el nivel siguiente inferior cuando registren atrasos de más de 540 días. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «corresponderá la reclasificación inmediata en el nivel siguiente inferior cuando se verifiquen atrasos de más de 540 días»
- **c5 Condicion** «Concurso o APE no homologado solicitado» — Deudores que solicitaron concurso preventivo o acuerdo preventivo extrajudicial aún no homologado. · tramo [exacta]: «En el caso de deudores que hayan solicitado el concurso preventivo o acuerdo preventivo extrajudicial aún no homologado»
- **c6 Condicion** «Atrasos de más de 540 días» — Que se verifiquen atrasos de más de 540 días. · umbral: ['atrasos de más de 540 días'] · tramo [exacta]: «cuando se verifiquen atrasos de más de 540 días»
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: c4 Condicion —condicion_de→ p1 Potestad
- R: c5 Condicion —condicion_de→ o1 Obligacion
- R: c6 Condicion —condicion_de→ o1 Obligacion
- R: op1 Operacion —aplica_a→ Sujeto_deudor (mención «deudor»)
- Omisión `relacion_sin_predicado` [exacta]: «el deudor podrá ser reclasificado» — Potestad → Operacion habilitada; no hay predicado
- Omisión `relacion_sin_predicado` [exacta]: «corresponderá la reclasificación inmediata en el nivel siguiente inferior» — La obligación de reclasificar regula el acto de clasificación; no se emitió Operacion separada

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:16 | sí | «según la situación previa, si se observan las condiciones allí previstas» | `extraida_tramo_verificado` |  | p1 Potestad [exacta] (y c4 Condicion) con tramo que contiene el fragmento |

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

### Extracción (código W)

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

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «sin cancelación efectiva previa» | `dentro_de_norma` |  | dentro de la Restriccion r1 («Cómputo de plazos no interrumpido por renovaciones», tramo); sin Condicion |
| 2 | «pago del 15 %» | `condicion_con_relacion` |  | c4 Condicion con los umbrales —condicion_de→ p1 Potestad |
| 3 | «financiación adicional sin cancelar» | `condicion_con_relacion` |  | c8 Condicion «Financiación adicional no cancelada» —condicion_de→ o1 Obligacion |

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

### Extracción (código W)

- **c1 Condicion** «Deuda superior al 2,5 % RPC — indicador Irrecuperable» — Indicador (alternativo) para clasificar en categoría Irrecuperable: clientes del sector privado no financiero cuya deuda por todo concepto más la financiación solicitada, al momento de su otorgamiento, exceda el 2,5 % de la RPC de la entidad del último día del mes anterior o el importe de referencia del punto 3.7., el menor de ambos. · props: `{"umbrales": [{"tramo": "el equivalente al importe de referencia establecido en el punto 3.7., de ambos el menor", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['exceda del 2,5 % de la responsabilidad patrimonial computable', 'el equivalente al importe de referencia establecido en el punto 3.7., de ambos e…'] · tramo [exacta]: «Clientes del sector privado no financiero, cuya deuda (por todo concepto) más el»
- **c2 Condicion** «Falta de DDJJ de vinculación — indicador Irrecuperable» — Supuesto concurrente del indicador para categoría Irrecuperable: que el cliente no haya presentado declaración jurada sobre si es vinculado al intermediario financiero o si su relación implica influencia controlante, o no la haya actualizado. El tratamiento rige desde el otorgamiento (primera declaración) o desde el 1.12 (actualizaciones) hasta el mes anterior a la presentación. · tramo [exacta]: «que no hayan presentado declaración jurada sobre si revisten o no el carácter de vinculados»
- **x1 Excepcion** «Deudores en concurso o gestión judicial — exclusión» — Quedan exceptuados de la clasificación en Irrecuperable por este indicador los deudores en concurso, con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, por hasta 540 días desde la apertura/solicitud/inicio, no hubiesen presentado la documentación. · umbral: ['por un período de hasta 540 días'] · tramo [exacta]: «con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial»
- **c3 Condicion** «Informe de abogado sobre recupero — condición excepción» — La excepción rige siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos. · tramo [no]: «siempre que se cuente con informe de abo-gado de la entidad financiera acreedora»
- R: c3 Condicion —condicion_de→ x1 Excepcion
- R: x1 Excepcion —aplica_a→ Sujeto_deudor (mención «los deudores»)
- Omisión `fuera_de_tipos` [exacta]: «Este tratamiento se aplicará desde la fecha de otorgamiento de la asistencia,» — Ámbito temporal del tratamiento; recogido en la descripción de c2, sin tipo propio.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «deuda de más del 2,5 % de la RPC o del importe de referencia» | `sin_relacion` | norma_en_heredado | c1 Condicion con los umbrales, sin relación; la norma que condiciona (la inclusión en Irrecuperable) está en el texto heredado y no se emitió como entidad |
| 2 | «excepción de concurso hasta 540 días» | `sin_relacion` | norma_en_heredado | x1 Excepcion con el umbral, sin relación hacia la norma que exceptúa (solo aplica_a); la clasificación no está como entidad |
| 3 | «siempre que haya informe» | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ x1 Excepcion |
| 4 | «primera declaración» | `dentro_de_norma` |  | en la descripción de c2 (el tramo temporal) y en una omisión fuera_de_tipos; sin Condicion propia |
| 5 | «actualizaciones» | `dentro_de_norma` |  | ídem, descripción de c2 y omisión fuera_de_tipos |

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:26 | sí | «Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre "Previsiones mínimas por ries…» | `ausente` |  | ninguna entidad ni omisión lo cubre |

## `cla::7.2.2.1` — En observación.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
> *heredado:* 7.2. Niveles de clasificación.
> *heredado:* 7.2.2. Riesgo bajo.
> *propio:* 7.2.2.1. En observación. Comprende los clientes que registran incumplimientos ocasionales en la atención de sus obligaciones, con atrasos de más de 31 hasta 90 días. En cuanto a la situación jurídica del deudor, se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer cuando se haya cancelado, al menos, el 10 % del importe involucrado en el citado acuerdo. Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior, cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 1 cuota o, cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligaciones refinanciadas (por capital), con más la cantidad de cuotas o el porcentaje acumulado que pudiera corresponder, respectivamente, si la refinanciación se hubiera otorgado de encontrarse incluido el deudor en niveles inferiores. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado la cuota citada en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente. En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categoría, corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días resultante de sumar los días de atraso efectivamente registrados a partir de la primera cuota impaga de la refinanciación y los de atraso mínimo establecidos normativamente que correspondan a la categoría en la que se encuentre clasificado el deudor en el mes en que se verifica el nuevo atraso.

### Extracción (código W)

- **d1 Definicion** «En observación — cartera consumo o vivienda» — Nivel de riesgo bajo de la cartera para consumo o vivienda que comprende los clientes con incumplimientos ocasionales, con atrasos de más de 31 hasta 90 días. · props: `{"termino": "En observación"}` · tramo [exacta]: «Comprende los clientes que registran incumplimientos ocasionales en la atención de sus obligaciones, con atrasos de más de 31 hasta 90 días.»
- **o1 Operacion** «Clasificación en situación En observación» — Clasificación de deudores de la cartera para consumo o vivienda en el nivel En observación (riesgo bajo). · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «Comprende los clientes que registran incumplimientos ocasionales»
- **c1 Condicion** «Convenios concordatarios con 10 % cancelado» — Situación jurídica: se considera si el deudor mantiene convenios de pago de concordatos judiciales o extrajudiciales homologados (incl. acuerdos preventivos extrajudiciales) a vencer, cuando se haya cancelado al menos el 10 % del importe involucrado. · umbral: ['al menos, el 10 % del importe involucrado'] · tramo [exacta]: «se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados»
- **p1 Potestad** «Reclasificación al nivel superior — deudas refinanciadas» — Los clientes con deudas refinanciadas pueden ser reclasificados en el nivel inmediato superior si cumplen las condiciones de pago (1 cuota o 5 % del capital refinanciado, más cuotas o porcentaje acumulado que corresponda por niveles inferiores). · tramo [exacta]: «podrán ser reclasificados en el nivel inmediato superior»
- **o2 Operacion** «Reclasificación al nivel inmediato superior» — Reclasificación en el nivel inmediato superior de clientes cuyas deudas fueron refinanciadas. · props: `{"tipo": "reclasificación de deudor"}` · tramo [exacta]: «podrán ser reclasificados en el nivel inmediato superior»
- **c2 Condicion** «Pago periódico: 1 cuota sin atraso >31 días» — Refinanciación mediante obligaciones de pago periódico (mensual o bimestral): haber pagado 1 cuota puntualmente o con atrasos que no superen 31 días. · props: `{"umbrales": [{"tramo": "el pago de 1 cuota", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['atrasos que no superen los 31 días', 'el pago de 1 cuota'] · tramo [exacta]: «cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 1 cuota»
- **c3 Condicion** «Pago único/irregular: 5 % capital cancelado» — Financiaciones de pago único, periódico superior a bimestral o irregular: haber cancelado al menos el 5 % de las obligaciones refinanciadas (por capital). · umbral: ['al menos el 5 % de sus obligaciones refinanciadas (por capital)'] · tramo [exacta]: «cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligaciones refinanciadas (por capital)»
- **c4 Condicion** «Cuotas adicionales según nivel inferior previo» — Adicionalmente, la cantidad de cuotas o porcentaje acumulado que correspondería si la refinanciación se hubiera otorgado estando el deudor en niveles inferiores. · props: `{"umbrales": [{"tramo": "la cantidad de\ncuotas o el porcentaje acumulado que pudiera corresponder", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['la cantidad de cuotas o el porcentaje acumulado que pudiera corresponder'] · tramo [exacta]: «con más la cantidad de cuotas o el porcentaje acumulado que pudiera corresponder, respectivamente, si la refinanciación se hubiera otorgado de encontrarse incluido el deudor en niveles inferiores»
- **r1 Restriccion** «Permanencia mínima 180 días — refinanciado con crédito adicional» — El deudor en esta categoría que refinanció y recibió crédito adicional (punto 2.2.5 de Previsiones mínimas), no cancelado, debe permanecer en ella al menos 180 días desde el otorgamiento del crédito adicional o del acuerdo de refinanciación, la más reciente, aun si canceló la cuota. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por lo menos 180 días'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días»
- **o3 Operacion** «Reclasificación de deudor refinanciado con crédito adicional» — Cambio de categoría del deudor En observación que refinanció y recibió crédito adicional. · props: `{"tipo": "reclasificación de deudor"}` · tramo [exacta]: «haya refinanciado su deuda»
- **c5 Condicion** «Refinanciación con crédito adicional recibido» — Que el deudor haya refinanciado su deuda y recibido crédito adicional en términos del punto 2.2.5 de Previsiones mínimas. · tramo [exacta]: «haya refinanciado su deuda –aun cuando haya cancelado la cuota citada en el párrafo precedente– y recibido crédito adicional»
- **c6 Condicion** «Financiación adicional no cancelada» — Que la financiación adicional no haya sido cancelada. · tramo [exacta]: «en la medida en que dicha financiación adicional no hubiese sido cancelada»
- **ob1 Obligacion** «Reclasificación inmediata por atraso >31 días en refinanciación» — Reclasificar inmediatamente al deudor en el nivel que surja de sumar los días de atraso efectivos desde la primera cuota impaga de la refinanciación y los de atraso mínimo de la categoría en que esté clasificado en el mes del nuevo atraso. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días»
- **o4 Operacion** «Reclasificación inmediata del deudor refinanciado» — Reclasificación inmediata del deudor con atrasos en la deuda refinanciada. · props: `{"tipo": "reclasificación de deudor"}` · tramo [exacta]: «la reclasificación inmediata del deudor»
- **c7 Condicion** «Atrasos mayores a 31 días en refinanciación» — Atrasos mayores a 31 días en el pago de servicios de la deuda refinanciada, contados desde la inclusión del deudor en esta categoría. · umbral: ['atrasos mayores a 31 días'] · tramo [exacta]: «En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada»
- R: c1 Condicion —condicion_de→ o1 Operacion
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: c4 Condicion —condicion_de→ p1 Potestad
- R: p1 Potestad —aplica_a→ Sujeto_cliente (mención «Los clientes»)
- R: r1 Restriccion —limita→ o3 Operacion
- R: c5 Condicion —condicion_de→ r1 Restriccion
- R: c6 Condicion —condicion_de→ r1 Restriccion
- R: ob1 Obligacion —regula→ o4 Operacion
- R: c7 Condicion —condicion_de→ ob1 Obligacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «cancelado el 10 %» | `condicion_con_relacion` |  | c1 Condicion con el umbral —condicion_de→ o1 Operacion (la clasificación en observación) |
| 2 | «pago de 1 cuota» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ p1 Potestad |
| 3 | «pago único o irregular con 5 %» | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ p1 Potestad |
| 4 | «financiación adicional sin cancelar» | `condicion_con_relacion` |  | c6 Condicion «Financiación adicional no cancelada» —condicion_de→ r1 Restriccion |
| 5 | «atrasos de más de 31 días» | `condicion_con_relacion` |  | c7 Condicion con el umbral —condicion_de→ ob1 Obligacion |

## `cla::7.2.3` — Riesgo medio.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
> *heredado:* 7.2. Niveles de clasificación.
> *propio:* 7.2.3. Riesgo medio. Comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días. En cuanto a la situación jurídica del deudor, se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer cuando aún no se haya cancelado el 10 % del importe involucrado en el citado acuerdo. A fin de determinar el importe de la cancelación, se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deudor –con excepción de las hipotecas sobre inmuebles rurales que, por lo tanto, serán computables–, observando los márgenes de cobertura establecidos en las normas sobre "Garantías". Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior, cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 2 cuotas consecutivas o, cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligaciones refinanciadas (por capital), con más la cantidad de cuotas o el porcentaje acumulado que pudiera corresponder, respectivamente, si la refinanciación se hubiera otorgado de encontrarse incluido el deudor en el nivel inferior. El deudor refinanciado que haya cumplido con lo dispuesto en los párrafos precedentes, según corresponda, podrá ser reclasificado en el nivel inmediato superior si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado las cuotas o el porcentaje establecidos precedentemente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente. En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categoría, corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días resultante de sumar los días de atraso efectivamente registrados a partir de la primera cuota impaga de la refinanciación y los de atraso mínimo establecidos normativamente que correspondan a la categoría en la que se encuentre clasificado el deudor en el mes en que se verifica el nuevo atraso.

### Extracción (código W)

- **d1 Definicion** «Riesgo medio — nivel cartera consumo/vivienda» — Comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días. · props: `{"termino": "Riesgo medio"}` · tramo [exacta]: «Comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días.»
- **c1 Condicion** «Convenios concordatarios con menos del 10 % cancelado» — Situación jurídica: se considera si el deudor mantiene convenios de pago de concordatos judiciales o extrajudiciales homologados (incluidos acuerdos preventivos extrajudiciales) a vencer cuando aún no se canceló el 10 % del importe del acuerdo. · umbral: ['cuando aún no se haya cancelado el 10 % del importe involucrado'] · tramo [exacta]: «se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados»
- **p1 Potestad** «Cómputo 50 % garantías adicionales — importe cancelado» — Para determinar el importe de la cancelación se admite computar el 50 % de las garantías adicionales a las originales, constituidas sobre bienes no vinculados a la explotación del deudor (salvo hipotecas sobre inmuebles rurales, que son computables), observando márgenes de cobertura de normas sobre Garantías. · tramo [exacta]: «se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente»
- **ex1 Excepcion** «Hipotecas sobre inmuebles rurales computables» — Las hipotecas sobre inmuebles rurales quedan fuera de la exigencia de bienes no vinculados a la explotación del deudor y son computables. · tramo [exacta]: «con excepción de las hipotecas sobre inmuebles rurales que, por lo tanto, serán computables»
- **op1 Operacion** «Reclasificación al nivel superior — deudor refinanciado» — Reclasificación en el nivel inmediato superior de clientes en riesgo medio cuyas deudas fueron refinanciadas · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «podrán ser reclasificados en el nivel inmediato superior»
- **p2 Potestad** «Reclasificación ascendente de refinanciados — riesgo medio» — Los clientes con deudas refinanciadas pueden ser reclasificados en el nivel inmediato superior si cumplen las condiciones de pago y el resto de sus deudas reúne las condiciones de ese nivel. · tramo [exacta]: «Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior»
- **c2 Condicion** «Pago puntual de 2 cuotas consecutivas» — Refinanciaciones de pago periódico mensual o bimestral: pago de 2 cuotas consecutivas puntualmente o con atrasos no mayores a 31 días, más las cuotas que correspondieran si hubiera estado en el nivel inferior. · props: `{"umbrales": [{"tramo": "pago de 2 cuotas consecutivas", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['con atrasos que no superen los 31 días', 'pago de 2 cuotas consecutivas'] · tramo [exacta]: «cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 2 cuotas consecutivas»
- **c3 Condicion** «Cancelación de al menos 5 % refinanciado» — Financiaciones de pago único, periódico superior a bimestral o irregular: cancelación de al menos el 5 % del capital refinanciado, más el porcentaje acumulado que correspondiera si hubiera estado en el nivel inferior. · umbral: ['al menos el 5 % de sus obligaciones refinanciadas (por capital)'] · tramo [exacta]: «hayan cancelado al menos el 5 % de sus obligaciones refinanciadas (por capital)»
- **c4 Condicion** «Resto de deudas cumple condiciones del nivel» — El resto de las deudas del deudor refinanciado reúne como mínimo las condiciones del nivel inmediato superior. · tramo [exacta]: «si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel»
- **r1 Restriccion** «Permanencia mínima 180 días — refinanciado con crédito adicional» — El deudor en riesgo medio que refinanció y recibió crédito adicional (punto 2.2.5 de Previsiones mínimas), no cancelado, debe permanecer en la categoría al menos 180 días desde el crédito adicional o el acuerdo, lo más reciente, aunque haya cancelado las cuotas o porcentaje. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por lo menos 180 días'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días»
- **c5 Condicion** «Crédito adicional recibido y no cancelado» — El deudor refinanciado recibió crédito adicional en términos del punto 2.2.5 de Previsiones mínimas y esa financiación no fue cancelada. · tramo [exacta]: «en la medida en que dicha financiación adicional no hubiese sido cancelada»
- **o1 Obligacion** «Reclasificación inmediata por atraso >31 días» — Ante atrasos mayores a 31 días en la deuda refinanciada desde la inclusión en esta categoría, reclasificar de inmediato al deudor en el nivel que surja de sumar los días de atraso desde la primera cuota impaga de la refinanciación y los de atraso mínimo de la categoría en que esté clasificado en el mes del nuevo atraso. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «corresponderá la reclasificación inmediata del deudor»
- **c6 Condicion** «Atrasos mayores a 31 días en refinanciación» — Atrasos mayores a 31 días en servicios de la deuda refinanciada desde la inclusión en esta categoría. · umbral: ['atrasos mayores a 31 días'] · tramo [exacta]: «En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada»
- **op2 Operacion** «Reclasificación inmediata — deudor refinanciado con atraso» — Reclasificación inmediata según días acumulados de atraso · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días»
- R: c2 Condicion —condicion_de→ p2 Potestad
- R: c3 Condicion —condicion_de→ p2 Potestad
- R: c4 Condicion —condicion_de→ p2 Potestad
- R: c5 Condicion —condicion_de→ r1 Restriccion
- R: c6 Condicion —condicion_de→ o1 Obligacion
- R: r1 Restriccion —limita→ op1 Operacion
- R: o1 Obligacion —regula→ op2 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «con excepción de las hipotecas sobre inmuebles rurales que, por lo tanto, serán computables» — Excepción a una Potestad; exceptua solo admite Restriccion/Obligacion.
- Omisión `relacion_sin_predicado` [exacta]: «se considerará si mantiene convenios de pago» — Criterio de inclusión en la clase; condicion_de no admite Definicion.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «sin cancelar el 10 %» | `sin_relacion` | norma_presente | c1 Condicion con el umbral, sin relación (omisión relacion_sin_predicado: condicion_de no admite Definicion); la norma está en la unidad como d1 |
| 2 | «pago de 2 cuotas» | `condicion_con_relacion` |  | c2 Condicion con los umbrales —condicion_de→ p2 Potestad |
| 3 | «pago único o irregular con 5 %» | `condicion_con_relacion` |  | c3 Condicion con el umbral —condicion_de→ p2 Potestad |
| 4 | «financiación adicional sin cancelar» | `condicion_con_relacion` |  | c5 Condicion «Crédito adicional recibido y no cancelado» —condicion_de→ r1 Restriccion |
| 5 | «atrasos de más de 31 días» | `condicion_con_relacion` |  | c6 Condicion con el umbral —condicion_de→ o1 Obligacion |

## `cla::7.2.4` — Riesgo alto.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
> *heredado:* 7.2. Niveles de clasificación.
> *propio:* 7.2.4. Riesgo alto. Comprende a los clientes con atrasos de más de 180 días hasta un año. También incluirá a los deudores que hayan solicitado el concurso preventivo, celebrado un acuerdo preventivo extrajudicial aún no homologado o se le haya requerido su quiebra, en tanto no hubiere sido declarada, por obligaciones que sean iguales o superiores al 20 % del patrimonio del cliente o por obligaciones entre el 5 % y menos del 20 % del patrimonio cuando persista el pedido de quiebra luego de transcurridos 90 días desde que ésta haya sido requerida. En caso de levantarse el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores, según la situación previa, si se observan las condiciones allí previstas. En el caso de deudores que hayan solicitado el concurso preventivo o acuerdo preventivo extrajudicial o se encuentren en gestión judicial, que verifiquen atrasos de hasta 540 días. Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior, cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 3 cuotas consecutivas o, cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 10 % de sus obligaciones refinanciadas (por capital), con más la cantidad de cuotas o el porcentaje acumulado que pudiera corresponder, respectivamente, si la refinanciación se hubiera otorgado de encontrarse incluido el deudor en el nivel inferior En el caso de deudores que hayan solicitado el concurso preventivo, corresponderá la reclasificación inmediata en el nivel siguiente inferior cuando se verifiquen atrasos de más de 540 días. El deudor refinanciado que haya cumplido con lo dispuesto en los párrafos precedentes, según corresponda, podrá ser reclasificado en el nivel inmediato superior si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado las cuotas o el porcentaje establecidos precedentemente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente. En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categoría, corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días resultante de sumar los días de atraso efectivamente registrados a partir de la primera cuota impaga de la refinanciación y los de atraso mínimo establecidos normativamente que correspondan a la categoría en la que se encuentre clasificado el deudor en el mes en que se verifica el nuevo atraso.

### Extracción (código W)

- **d1 Definicion** «Riesgo alto — nivel cartera consumo/vivienda» — Nivel de clasificación de la cartera para consumo o vivienda que comprende a los clientes con atrasos de más de 180 días hasta un año; también a deudores con concurso preventivo, APE no homologado o pedido de quiebra no declarada, según los supuestos de obligaciones respecto del patrimonio, y a deudores concursados, con APE o en gestión judicial con atrasos de hasta 540 días. · props: `{"termino": "Riesgo alto"}` · tramo [exacta]: «Comprende a los clientes con atrasos de más de 180 días hasta un año.»
- **op1 Operacion** «Clasificación en Riesgo alto — deudores consumo/vivienda» — Inclusión de deudores de la cartera para consumo o vivienda en el nivel Riesgo alto. · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «También incluirá a los deudores que hayan solicitado el concurso preventivo, celebrado un acuerdo preventivo extrajudicial aún no homologado o se le haya requerido su quiebra, en tanto no hubiere sido declarada»
- **c1 Condicion** «Atrasos de más de 180 días hasta un año» — Atrasos de más de 180 días hasta un año. · umbral: ['atrasos de más de 180 días', 'hasta un año'] · tramo [exacta]: «clientes con atrasos de más de 180 días hasta un año»
- **c2 Condicion** «Concurso, APE o pedido de quiebra no declarada» — Deudor que solicitó concurso preventivo, celebró APE no homologado o se le requirió la quiebra no declarada. · tramo [exacta]: «deudores que hayan solicitado el concurso preventivo, celebrado un acuerdo preventivo extrajudicial aún no homologado o se le haya requerido su quiebra, en tanto no hubiere sido declarada»
- **c3 Condicion** «Obligaciones ≥ 20 % del patrimonio» — Obligaciones iguales o superiores al 20 % del patrimonio del cliente (alternativa a c4). · umbral: ['iguales o superiores al 20 % del patrimonio del cliente'] · tramo [exacta]: «por obligaciones que sean iguales o superiores al 20 % del patrimonio del cliente»
- **c4 Condicion** «Obligaciones 5–20 % y quiebra persistente 90 días» — Obligaciones entre 5 % y menos del 20 % del patrimonio, con pedido de quiebra persistente luego de 90 días (alternativa a c3). · umbral: ['entre el 5 % y menos del 20 % del patrimonio', 'luego de transcurridos 90 días'] · tramo [exacta]: «por obligaciones entre el 5 % y menos del 20 % del patrimonio cuando persista el pedido de quiebra luego de transcurridos 90 días desde que ésta haya sido requerida»
- **c5 Condicion** «Concursados/APE/gestión judicial con atraso hasta 540 días» — Deudores con concurso preventivo, APE o en gestión judicial con atrasos de hasta 540 días. · umbral: ['atrasos de hasta 540 días'] · tramo [exacta]: «En el caso de deudores que hayan solicitado el concurso preventivo o acuerdo preventivo extrajudicial o se encuentren en gestión judicial, que verifiquen atrasos de hasta 540 días.»
- **p1 Potestad** «Reclasificación al levantarse pedido de quiebra» — Levantado el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores según la situación previa, si se observan las condiciones de esos niveles. · tramo [exacta]: «En caso de levantarse el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores, según la situación previa, si se observan las condiciones allí previstas.»
- **op2 Operacion** «Reclasificación al nivel superior — deudor refinanciado» — Reclasificación al nivel inmediato superior de clientes en Riesgo alto con deudas refinanciadas. · props: `{"tipo": "reclasificación de deudor"}` · tramo [exacta]: «podrán ser reclasificados en el nivel inmediato superior»
- **p2 Potestad** «Reclasificación superior de refinanciados con pago periódico» — Los clientes con deudas refinanciadas con pago periódico mensual o bimestral, o de pago único/periódico superior a bimestral/irregular, podrán ser reclasificados en el nivel inmediato superior si cumplen las condiciones de pago. · tramo [exacta]: «Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior»
- **c6 Condicion** «Pago puntual de 3 cuotas consecutivas» — Refinanciación de pago periódico mensual o bimestral: pago puntual o con atrasos no superiores a 31 días de 3 cuotas consecutivas. · props: `{"umbrales": [{"tramo": "pago de 3 cuotas consecutivas", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['atrasos que no superen los 31 días', 'pago de 3 cuotas consecutivas'] · tramo [exacta]: «cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 3 cuotas consecutivas»
- **c7 Condicion** «Cancelación 10 % — pago único o irregular» — Financiaciones de pago único, periódico superior a bimestral o irregular: cancelación de al menos el 10 % del capital refinanciado, más las cuotas o porcentaje acumulado que correspondiera si la refinanciación se hubiera otorgado estando en el nivel inferior. · props: `{"umbrales": [{"tramo": "con más la cantidad de cuotas o el porcentaje acumu-\nlado que pudiera corresponder", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['al menos el 10 % de sus obligaciones refinanciadas (por capital)', 'con más la cantidad de cuotas o el porcentaje acumulado que pudiera corresponder'] · tramo [exacta]: «cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 10 % de sus obligaciones refinanciadas (por capital)»
- **o1 Obligacion** «Reclasificación inmediata inferior — concursados atraso >540 días» — Deudores con concurso preventivo deben reclasificarse inmediatamente en el nivel siguiente inferior cuando verifiquen atrasos de más de 540 días. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «En el caso de deudores que hayan solicitado el concurso preventivo, corresponderá la reclasificación inmediata en el nivel siguiente inferior cuando se verifiquen atrasos de más de 540 días.»
- **c8 Condicion** «Concursado con atrasos de más de 540 días» — Deudor concursado con atrasos de más de 540 días. · umbral: ['atrasos de más de 540 días'] · tramo [exacta]: «cuando se verifiquen atrasos de más de 540 días»
- **p3 Potestad** «Reclasificación superior si resto de deudas cumple» — El deudor refinanciado que cumplió lo previsto podrá ser reclasificado en el nivel inmediato superior si además el resto de sus deudas reúne como mínimo las condiciones del nivel. · tramo [exacta]: «El deudor refinanciado que haya cumplido con lo dispuesto en los párrafos precedentes, según corresponda, podrá ser reclasificado en el nivel inmediato superior»
- **c9 Condicion** «Resto de deudas reúne condiciones del nivel» — El resto de las deudas reúne como mínimo las condiciones del nivel inmediato superior. · tramo [exacta]: «si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel»
- **r1 Restriccion** «Permanencia mínima 180 días — refinanciado con crédito adicional» — El deudor en Riesgo alto que refinanció y recibió crédito adicional (punto 2.2.5 de Previsiones mínimas) no cancelado debe permanecer en la categoría al menos 180 días desde el crédito adicional o la refinanciación, lo más reciente, aun cancelando cuotas o porcentaje. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por lo menos 180 días'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente»
- **c10 Condicion** «Refinanciación con crédito adicional no cancelado» — Deudor que refinanció y recibió crédito adicional en términos del punto 2.2.5 de Previsiones mínimas. · tramo [exacta]: «haya refinanciado su deuda –aun cuando haya cancelado las cuotas o el porcentaje establecidos precedentemente– y recibido crédito adicional»
- **c11 Condicion** «Financiación adicional no cancelada» — La financiación adicional no fue cancelada. · tramo [exacta]: «en la medida en que dicha financiación adicional no hubiese sido cancelada»
- **o2 Obligacion** «Reclasificación inmediata por atraso >31 días en refinanciación» — Ante atrasos mayores a 31 días en la deuda refinanciada desde la inclusión en Riesgo alto, reclasificar inmediatamente al deudor en el nivel que surja de sumar los días de atraso desde la primera cuota impaga de la refinanciación y los de atraso mínimo de la categoría en que esté en el mes del nuevo atraso. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días»
- **c12 Condicion** «Atrasos mayores a 31 días en deuda refinanciada» — Atrasos mayores a 31 días en servicios de la deuda refinanciada desde la inclusión en esta categoría. · umbral: ['atrasos mayores a 31 días'] · tramo [exacta]: «En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada»
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: c2 Condicion —condicion_de→ op1 Operacion
- R: c3 Condicion —condicion_de→ op1 Operacion
- R: c4 Condicion —condicion_de→ op1 Operacion
- R: c5 Condicion —condicion_de→ op1 Operacion
- R: c6 Condicion —condicion_de→ p2 Potestad
- R: c7 Condicion —condicion_de→ p2 Potestad
- R: c8 Condicion —condicion_de→ o1 Obligacion
- R: c9 Condicion —condicion_de→ p3 Potestad
- R: c10 Condicion —condicion_de→ r1 Restriccion
- R: c11 Condicion —condicion_de→ r1 Restriccion
- R: c12 Condicion —condicion_de→ o2 Obligacion
- R: p2 Potestad —aplica_a→ Sujeto_cliente (mención «Los clientes»)
- R: r1 Restriccion —aplica_a→ Sujeto_deudor (mención «El deudor»)
- R: p1 Potestad —aplica_a→ Sujeto_deudor (mención «el deudor»)
- R: p3 Potestad —aplica_a→ Sujeto_deudor (mención «El deudor refinanciado»)
- Omisión `relacion_sin_predicado` [exacta]: «podrán ser reclasificados en el nivel inmediato superior» — Potestad → Operacion habilitada; sin predicado.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «concurso con 20 % o más» | `condicion_con_relacion` |  | c3 Condicion con el umbral (con c2, el concurso) —condicion_de→ op1 Operacion |
| 2 | «entre 5 % y 20 % con 90 días» | `condicion_con_relacion` |  | c4 Condicion con los umbrales —condicion_de→ op1 Operacion |
| 3 | «levantamiento del pedido» | `dentro_de_norma` |  | dentro de la Potestad p1 (tramo); sin Condicion |
| 4 | «refinanciados» | `dentro_de_norma` |  | dentro de la Potestad p2 (tramo) |
| 5 | «más de 540 días» | `condicion_con_relacion` |  | c8 Condicion con el umbral —condicion_de→ o1 Obligacion |
| 6 | «atrasos de más de 31 días» | `condicion_con_relacion` |  | c12 Condicion con el umbral —condicion_de→ o2 Obligacion |

## `ctacte::1.5.2.6` — Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo

Grupos: omisiones.

### Texto

> *heredado:* Sección 1. Funcionamiento.
> *heredado:* 1.5. Aspectos del funcionamiento a incluir en el contrato de cuenta corriente.
> *heredado:* En sus cláusulas se deberá prever, como mínimo:
> *heredado:* 1.5.2. Obligaciones de la entidad.
> *propio:* 1.5.2.6. Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo– los cheques librados por el cuentacorrentista, de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque, teniendo en cuenta en materia de plazos de presentación los establecidos en el artículo 25 de la Ley de Cheques. En el caso de cheques de pago diferido, ese plazo se computará a partir de la fecha de pago consignada en el cheque.

### Extracción (código W)

- **c1 Comunicacion** «Ley de Cheques» —  · props: `{"codigo": "Ley de Cheques", "tipo": "externa"}` · tramo [exacta]: «artículo 25 de la Ley de Cheques»
- **op1 Operacion** «Pago a la vista de cheques» — Pago a la vista por la entidad de los cheques librados por el cuentacorrentista · props: `{"tipo": "pago de cheques"}` · tramo [exacta]: «Pagar a la vista»
- **o1 Obligacion** «Cláusula contractual: pagar a la vista cheques» — El contrato de cuenta corriente debe prever, como mínimo, la obligación de la entidad de pagar a la vista los cheques librados por el cuentacorrentista, conforme a las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque y considerando los plazos de presentación del art. 25 de la Ley de Cheques. · props: `{"tipo": "otra"}` · tramo [exacta]: «En sus cláusulas se deberá prever, como mínimo: […] Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo– los cheques librados por el cuentacorrentista»
- **x1 Excepcion** «Casos del punto 1.5.2.8 segundo párrafo» — La obligación de pagar a la vista no rige en los casos del punto 1.5.2.8., segundo párrafo. · tramo [exacta]: «excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo»
- **o2 Obligacion** «Plazo pago diferido desde fecha de pago» — En cheques de pago diferido, el plazo de presentación se computa desde la fecha de pago consignada en el cheque. · props: `{"tipo": "calculo"}` · tramo [exacta]: «En el caso de cheques de pago diferido, ese plazo se computará a partir de la fecha de pago consignada en el cheque.»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: x1 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: o1 Obligacion —aplica_a→ Sujeto_banco (mención «la entidad»)
- R: Sujeto_banco (mención «la entidad») —ejecuta→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:6 | sí | «de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque» | `ausente` |  | ningún tramo lo contiene: el de o1 termina en «…librados por el cuentacorrentista»; solo en la descripción de o1 |

## `ctacte::2.1.1.4` — Lugar y fecha.

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Movimiento de las cuentas.
> *heredado:* 2.1. Créditos.
> *heredado:* 2.1.1. Mediante depósitos por ventanilla o cajeros automáticos.
> *heredado:* Cuando se empleen boletas, éstas deberán contener, como mínimo, los siguientes datos:
> *heredado:* Respecto de la realización de operaciones mediante cajeros automáticos, las entidades deberán tener implementados mecanismos de seguridad informática que garanticen la genuinidad de las operaciones.
> *propio:* 2.1.1.4. Lugar y fecha.

### Extracción (código W)

- **e1 Obligacion** «Lugar y fecha — contenido mínimo boleta de depósito» — Cuando se empleen boletas para depósitos en cuenta corriente por ventanilla o cajeros automáticos, éstas deberán contener, como mínimo, el lugar y la fecha (junto con los demás datos de la lista, todos exigidos). · props: `{"tipo": "otra"}` · tramo [exacta]: «Cuando se empleen boletas, éstas deberán contener, como mínimo, los siguientes datos: […] Lugar y fecha.»
- **e2 Operacion** «Depósito en cuenta corriente por ventanilla o cajero» — Crédito en cuenta corriente mediante depósitos por ventanilla o cajeros automáticos · props: `{"tipo": "deposito"}` · tramo [exacta]: «Mediante depósitos por ventanilla o cajeros automáticos.»
- **e3 Condicion** «Empleo de boletas en el depósito» — Que en el depósito se empleen boletas. · tramo [exacta]: «Cuando se empleen boletas»
- R: e1 Obligacion —regula→ e2 Operacion
- R: e3 Condicion —condicion_de→ e1 Obligacion

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

### Extracción (código W)

(sin entidades ni omisiones)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:17 | no | «con el siguiente detalle:» | `ausente` |  | ningún tramo contiene «con el siguiente detalle:» ni omisión que lo registre |

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

### Extracción (código W)

- **c1 Condicion** «Falta del número de orden del cheque» — Supuesto (alternativo: basta la falta de alguna de las especificaciones) por el cual el título no vale como cheque: falta del número de orden, impreso en el cuerpo del cheque librado en formato papel o incorporado a los datos del cheque librado por medios electrónicos. · tramo [exacta]: «El número de orden, impreso en el cuerpo del cheque librado en formato papel o incorporado a los datos del cheque librado por medios electrónicos.»

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

### Extracción (código W)

- **op1 Operacion** «Presentación al cobro de ECHEQ» — Presentación al cobro de un cheque librado por medios electrónicos (ECHEQ) por el tenedor legitimado, a través de una orden electrónica de acreditación o por ventanilla · props: `{"tipo": "presentacion_al_cobro"}` · tramo [exacta]: «presentación al cobro de cada ECHEQ»
- **p1 Potestad** «Cobro de ECHEQ desde fecha de pago» — El tenedor legitimado puede presentar al cobro cada ECHEQ a partir de su fecha de pago, mediante una orden electrónica de acreditación, o cobrarlo por ventanilla · tramo [exacta]: «El tenedor legitimado podrá efectuar la presentación al cobro de cada ECHEQ a partir de la correspondiente fecha de pago a través de una orden electrónica de acreditación o cobrarlo por ventanilla»
- R: p1 Potestad —aplica_a→ Sujeto (mención «El tenedor legitimado»)
- R: Sujeto (mención «El tenedor legitimado») —ejecuta→ op1 Operacion
- Omisión `fuera_de_tipos` [exacta]: «En su defecto, quedará pendiente hasta la fecha de vencimiento del plazo previsto en el artículo 25 de la Ley de Cheques.» — Efecto sobre el estado del ECHEQ no presentado (queda pendiente hasta el vencimiento del plazo legal); no es un deber, una prohibición ni una facultad de ningún sujeto. Habría sido una Condicion o un …

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:27 | sí | «En su defecto» | `omision_otra_vez` | fuera_de_tipos | om#0 fuera_de_tipos [exacta], mismo tramo |

## `ctacte::5.1.2.2` — A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de En-

Grupos: omisiones.

### Texto

> *heredado:* Sección 5. Endosos, modalidades especiales de emisión y aval.
> *heredado:* 5.1. Endoso.
> *heredado:* 5.1.2. El cheque extendido a favor de una persona determinada, que no posea la cláusula "no a
> *heredado:* la orden", será transmisible por endoso. También podrán ser transmitidos por endoso los cheques con la citada condición ("no a la orden"), en los casos de transferencias –primeras y sucesivas– cuando se extienda:
> *heredado:* En los casos de cheques librados al portador o a favor de una persona determinada –que posean o no la cláusula "no a la orden"– y que sean entregados por su beneficiario a un tercero para la gestión de cobro mediante su presentación en ventanilla o a través de su depósito en cuenta para su compensación electrónica, se deberá consignar al dorso la firma y aclaración –o en el correspondiente registro electrónico, la identificación– del mandante u ordenante de la gestión y su número de identificación personal –según las normas sobre "Documentos de identificación en vigencia"– en los casos de personas físicas, o CUIT o CDI en los casos de personas jurídicas, independientemente de la existencia o no del documento que instrumenta el mandato. Adicionalmente, se insertará alguna de las siguientes expresiones: "en procuración", "valor al cobro" o "para su gestión de cobro", como manifestación de los efectos de ese endoso. La obligación de consignar el número de identificación personal o CUIT o CDI, según corresponda y la leyenda mencionada anteriormente recae, indistintamente, en el mandante u ordenante y el mandatario o gestor.
> *propio:* 5.1.2.2. A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras, en la medida en que se trate de operaciones relativas al fideicomiso.

### Extracción (código W)

- **op1 Operacion** «Endoso de cheque «no a la orden» a fiduciario» — Transmisión por endoso (primeras y sucesivas transferencias) de cheques con cláusula «no a la orden» extendidos a favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras · props: `{"tipo": "transmisión por endoso"}` · tramo [exacta]: «A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras»
- **p1 Potestad** «Endoso admitido: cheque «no a la orden» a fiduciario» — Los cheques con cláusula «no a la orden» podrán ser transmitidos por endoso, en transferencias primeras y sucesivas, cuando se extiendan a favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras (uno de los supuestos alternativos de la lista). · tramo [exacta]: «También podrán ser transmitidos por endoso los cheques con la citada condición ("no a la orden"), en los casos de transferencias –primeras y sucesivas– cuando se extienda: […] A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras»
- **c1 Condicion** «Operaciones relativas al fideicomiso» — El endoso del cheque «no a la orden» al fiduciario procede en la medida en que se trate de operaciones relativas al fideicomiso. · tramo [exacta]: «en la medida en que se trate de operaciones relativas al fideicomiso»
- **ley Comunicacion** «Ley de Entidades Financieras» —  · props: `{"codigo": "Ley de Entidades Financieras", "tipo": "externa"}` · tramo [exacta]: «Ley de Entidades Financieras»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: to TextoOrdenado —referencia→ ley Comunicacion
- Omisión `relacion_sin_predicado` [exacta]: «También podrán ser transmitidos por endoso» — Potestad que habilita la Operacion; no hay predicado Potestad→Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:28 | sí | «comprendidos en la Ley de Entidades Financieras» | `extraida_tramo_verificado` |  | op1 Operacion y p1 Potestad [exacta], tramos que contienen el fragmento |

## `ctacte::6.1.2.7` — Giro sobre el librador, salvo que se tratara de un cheque girado entre distintos

Grupos: omisiones.

### Texto

> *heredado:* Sección 6. Rechazo de cheques.
> *heredado:* 6.1. Causales.
> *heredado:* 6.1.2. Defectos formales.
> *heredado:* Se define como defecto formal todo aquel verificado en la creación del cheque que el beneficiario no pueda advertir por su mera apariencia. Quedan incluidos, entre otros, los siguientes casos:
> *propio:* 6.1.2.7. Giro sobre el librador, salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador.

### Extracción (código W)

- **d1 Definicion** «Giro sobre el librador — defecto formal de cheque» — Entre los defectos formales (verificados en la creación del cheque y no advertibles por el beneficiario por su mera apariencia) queda incluido, entre otros, el giro sobre el librador, salvo que se trate de un cheque girado entre distintos establecimientos de un mismo librador. · props: `{"termino": "defecto formal"}` · tramo [exacta]: «Se define como defecto formal todo aquel verificado en la creación del cheque que el beneficiario no pueda advertir por su mera apariencia. Quedan incluidos, entre otros, los siguientes casos: […] Giro sobre el librador»
- **x1 Excepcion** «Cheque entre establecimientos del mismo librador — no defecto» — El giro sobre el librador no constituye defecto formal (causal de rechazo del cheque) cuando se trata de un cheque girado entre distintos establecimientos de un mismo librador. · tramo [exacta]: «salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador»
- Omisión `relacion_sin_predicado` [exacta]: «salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador» — La excepción recorta el alcance de una Definicion; exceptua solo admite Restriccion como rango.

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:11 | sí | «Se define como defecto formal todo aquel verificado en la creación del cheque que el beneficiario no pueda advertir por su mera apariencia» | `extraida_tramo_verificado` |  | d1 Definicion [exacta], tramo que contiene «Se define como defecto formal…» |

## `ext::1.5` — Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Régimen

Grupos: omisiones.

### Texto

> *heredado:* Sección 1. Disposiciones generales.
> *propio:* 1.5. Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Régimen Penal Cambiario.

### Extracción (código W)

- **c1 Comunicacion** «Ley del Régimen Penal Cambiario» —  · props: `{"codigo": "Ley del Régimen Penal Cambiario", "tipo": "externa"}` · tramo [exacta]: «Ley del Régimen Penal Cambiario»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- Omisión `fuera_de_tipos` [exacta]: «Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Régimen Penal Cambiario.» — Consecuencia de un incumplimiento (sometimiento al Régimen Penal Cambiario) sin sujeto que la aplique nombrado; no es Restriccion. Tramo que la ata a la falta: 'Los incumplimientos a esta normativa se…

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

### Extracción (código W)

- **c1 Condicion** «Pago en el marco del punto 4.8.4» — Supuesto (alternativo a los demás ítems) de la excepción a la conformidad previa del BCRA para acceder al mercado de cambios a pagar importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23: que la entidad verifique que el pago se concreta en el marco del punto 4.8.4. · tramo [exacta]: «el pago es concretado en el marco de lo dispuesto en el punto 4.8.4.»
- **c2 Condicion** «Cliente suscribió BOPREAL Serie 1 ≥50% deudas elegibles» — Supuesto de la misma excepción a la conformidad previa del BCRA: que el pago lo concrete un cliente que, con anterioridad al 31/01/24, suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% del total pendiente de sus deudas elegibles para los puntos 4.4. y 4.5. · umbral: ['por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por…'] · tramo [exacta]: «por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24»

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

### Extracción (código W)

- **c0 Condicion** «Certificación de entidad de seguimiento — acceso pago importaciones SEPAIMPO» — Requisito (uno de los que se exigen todos juntos) para que la entidad interviniente pueda dar acceso al mercado de cambios para pagar importaciones de bienes con registro de ingreso aduanero que constan en el SEPAIMPO: la entidad certifica, como encargada del seguimiento de la oficialización, que se cumplen las condiciones i) a x), o cuenta con una certificación para el pago emitida por la entidad… · tramo [exacta]: «Certifica en carácter de entidad encargada del seguimiento de la oficialización que se cumplen las condiciones que se enuncian a continuación o cuenta con una certificación para realizar el pago emitida por la entidad que tiene tal responsabilidad»
- **c1 Condicion** «Constancia de registro aduanero de ingreso» — Condición a certificar: contar con constancia del registro aduanero del ingreso al país de los bienes que originan el pago. · tramo [exacta]: «Cuenta con constancia del registro aduanero del ingreso al país de los bienes que originan el pago a cancelarse.»
- **c2 Condicion** «Copia de factura comercial del exterior» — Condición a certificar: copia de factura comercial emitida en el exterior a nombre del cliente residente, con nombre y dirección del emisor, nombre del importador, cantidad y descripción de la mercadería, condición de venta y valor. · tramo [exacta]: «Cuenta con copia de factura comercial emitida en el exterior a nombre del cliente residente en el país»
- **c3 Condicion** «Copia del Documento de Transporte» — Condición a certificar: copia del Documento de Transporte. · tramo [exacta]: «Cuenta con copia del Documento de Transporte (Conocimiento de Embarque – Carta de Porte – Guía Aérea).»
- **c4 Condicion** «Consistencia factura y transporte con registros aduaneros» — Condición a certificar: la información de la factura y del Documento de Transporte es consistente con los registros aduaneros, según las normas de declaración aduanera aplicables. · tramo [exacta]: «Que la información que surge de la factura comercial y del Documento de Transporte sea consistente con la que figura en los registros aduaneros»
- **c5 Condicion** «Fecha de vencimiento determinable de la obligación» — Condición a certificar: la documentación permite establecer la fecha de vencimiento de la obligación con el exterior o que no tiene vencimiento pactado. · tramo [exacta]: «Que la documentación presentada le permita establecer la fecha de vencimiento de la obligación con el exterior por parte del importador o, en su defecto, que la operación no tiene una fecha de vencimiento pactada.»
- **c6 Condicion** «Operaciones financiadas calificables como deuda por importaciones» — Condición a certificar: si es financiada, la documentación permite calificarla como deuda por importaciones de bienes según el punto 10.2.4. · tramo [exacta]: «Que, en caso de tratarse de operaciones financiadas, la documentación presentada le permite calificar a la misma como una deuda por importaciones de bienes»
- **c7 Condicion** «Pagos acumulados no superan monto facturado» — Condición a certificar: el total de pagos imputados a la oficialización, incluido el solicitado, no supera el monto facturado en la condición de compra pactada. · props: `{"umbrales": [{"tramo": "no\nsupera el monto facturado en la condición de compra pactada", "comparacion": "maximo_inclusivo", "base": "monto facturado en la condición de compra pactada", "regla_comparacion": "limite_relativo:negacion:raiz_super", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['no supera el monto facturado en la condición de compra pactada'] · tramo [exacta]: «Que el total de los pagos realizados con imputación a la oficialización de importación, incluyendo el pago cuyo curso se está solicitando, no supera el monto facturado en la condición de compra pactada.»
- **c8 Condicion** «Beneficiario admitido del pago» — Condición a certificar: el beneficiario es el proveedor del exterior, o la entidad financiera del exterior o agencia oficial de crédito que financió la compra (si encuadra como deuda comercial por importaciones de bienes), o el no residente que compró el crédito al acreedor comercial sin modificar las condiciones del crédito. · tramo [exacta]: «Que el beneficiario del pago a realizar sea el proveedor del exterior o, en su caso, la entidad financiera del exterior o la agencia oficial de crédito que financió la compra al proveedor del exterior»
- **c9 Condicion** «Declaración en Relevamiento de activos y pasivos externos» — Condición a certificar: constancia de declaración de la operación, de corresponder, en la última presentación vencida del Relevamiento de activos y pasivos externos. · tramo [exacta]: «Cuenta con constancia de que la operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos".»
- **c10 Condicion** «DDJJ de saldo — importaciones oficializadas antes 01/11/19» — Condición a certificar: para importaciones oficializadas antes del 01/11/19, declaración jurada del saldo de deuda pendiente firmada por el importador, su representante legal o apoderado con facultades suficientes. · tramo [exacta]: «En el caso de importaciones oficializadas con anterioridad al 01/11/19, cuenta con una declaración jurada consignando el saldo de deuda pendiente a la fecha»
- Omisión `relacion_sin_predicado` [exacta]: «que se cumplen las condiciones que se enuncian a continuación» — Las condiciones i) a x) son el contenido de la certificación c0; condicion_de no admite una Condicion como destino.

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:2 | sí | «o cuenta con una certificación para realizar el pago emitida por la entidad que tiene tal responsabilidad» | `extraida_tramo_verificado` |  | c0 Condicion [exacta], tramo que contiene el fragmento |

## `ext::10.3.6` — Pagos de importaciones con cartas de crédito o letras avaladas emitidas u otorgadas

Grupos: grupo_c.

### Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero.
> *propio:* 10.3.6. Pagos de importaciones con cartas de crédito o letras avaladas emitidas u otorgadas por entidades financieras locales. La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente, en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad. En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha y, salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país. Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2. Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914. El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero".

### Extracción (código W)

- **op1 Operacion** «Cancelación de cartas de crédito o letras avaladas de importación» — Acceso de la entidad financiera local al mercado de cambios para cancelar cartas de crédito o letras avaladas que emitió u otorgó en garantía de importaciones de bienes con registro aduanero · props: `{"tipo": "acceso al mercado de cambios"}` · tramo [exacta]: «cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes»
- **p1 Potestad** «Acceso de la entidad para cancelar garantías de importación» — La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas que emitió u otorgó en garantía de importaciones de bienes con registro aduanero · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas»
- **x1 Excepcion** «Sin requisitos de acceso del cliente» — El acceso de la entidad corresponde aunque no se cumplan los requisitos fijados para el acceso del cliente · tramo [exacta]: «incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente»
- **c1 Condicion** «Documentación de condiciones vigentes al emitir» — La entidad debe contar con documentación que demuestre que, al abrir o emitir la garantía, se cumplían las condiciones aplicables según la fecha de emisión y el tipo de operación garantizada · tramo [exacta]: «en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad»
- **o1 Obligacion** «Documentar importación con registro desde 13/12/23» — Para garantías emitidas desde el 13/12/23, la entidad debe contar con documentación que demuestre que, al abrir o emitir la garantía, la operación garantizada era una importación de bienes con registro de ingreso aduanero desde esa fecha · props: `{"tipo": "otra"}` · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha»
- **c2 Condicion** «Garantías emitidas desde 13/12/23» — Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23 · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»
- **o2 Obligacion** «Documentar plazo de pago garantizado (10.10.1 + 15 días)» — Para garantías emitidas desde el 13/12/23, la entidad debe documentar que el cliente debía concretar el pago garantizado desde la fecha estimada de arribo más el plazo que fija el punto 10.10.1 para el bien más 15 días corridos · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes …'] · tramo [exacta]: «que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país»
- **x2 Excepcion** «Situación del punto 10.10.2.11» — La documentación del plazo de pago no se exige si la operación está comprendida en la situación del punto 10.10.2.11 · tramo [exacta]: «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- **x3 Excepcion** «Pago desde embarque + 15 días (desde 14/04/25)» — En las garantías emitidas desde el 14/04/25, en lugar del plazo desde el arribo se admite que el pago garantizado debiera hacerse desde la fecha estimada de embarque más 15 días corridos, para la porción que pudo pagarse a la vista por los puntos 10.10.2.1 o 10.10.2.2 · umbral: ['más un plazo adicional de 15 (quince) días corridos'] · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos»
- **c3 Condicion** «Garantías emitidas desde 14/04/25» — Garantías emitidas u otorgadas a partir del 14/04/25 · tramo [exacta]: «Para aquellas emitidas u otorgadas a partir del 14/04/25»
- **c4 Condicion** «Cumplimiento de las restantes condiciones» — Que se cumplan las restantes condiciones · tramo [exacta]: «en la medida que se cumplan las restantes condiciones»
- **c5 Condicion** «Porción pagable a la vista (10.10.2.1/2)» — Que el pago corresponda a la porción por la que el cliente pudo pagar a la vista según los puntos 10.10.2.1 o 10.10.2.2 · tramo [exacta]: «cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2.»
- **o3 Obligacion** «Boleto a nombre de la entidad, concepto B14» — El boleto de venta se hace a nombre de la propia entidad, como cliente, por el concepto B14 · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero"»
- **com1 Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- R: to TextoOrdenado —referencia→ com1 Comunicacion
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_entidad_financiera (mención «entidades financieras locales») —ejecuta→ op1 Operacion
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: c2 Condicion —condicion_de→ o1 Obligacion
- R: c2 Condicion —condicion_de→ o2 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o2 Obligacion —condiciona→ op1 Operacion
- R: x2 Excepcion —exceptua_obligacion→ o2 Obligacion
- R: x3 Excepcion —exceptua_obligacion→ o2 Obligacion
- R: c3 Condicion —condicion_de→ x3 Excepcion
- R: c4 Condicion —condicion_de→ x3 Excepcion
- R: c5 Condicion —condicion_de→ x3 Excepcion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la propia entidad»)
- Omisión `relacion_sin_predicado` [exacta]: «incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente» — La excepción releva de los requisitos de acceso del cliente, que no están en esta unidad; no hay exceptua hacia una Potestad

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «emitidas desde el 13/12/23 (más 15 días)» | `condicion_con_relacion` |  | c2 Condicion «Garantías emitidas desde 13/12/23» —condicion_de→ o1 y o2 Obligacion |
| 2 | «desde el 14/04/25» | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ x3 Excepcion |
| 3 | «con pagos a la vista» | `condicion_con_relacion` |  | c5 Condicion «Porción pagable a la vista» —condicion_de→ x3 Excepcion |

## `ext::10.4.4` — Cancelación de garantías comerciales de importaciones de bienes otorgadas por

Grupos: grupo_c.

### Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.4. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente.
> *propio:* 10.4.4. Cancelación de garantías comerciales de importaciones de bienes otorgadas por entidades financieras locales. La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero pendiente, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente, en la medida que se verifique que se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad. En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha y, salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país. Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2. Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914. El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B11. Cancelación de garantías comerciales de entidades financieras de importaciones de bienes sin registro de ingreso aduanero". Por los pagos que se realicen, la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuado el pago. En la medida que la entidad no cuente con el registro de la oficialización del despacho de importación dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cambios, la entidad deberá efectuar la correspondiente denuncia.

### Extracción (código W)

- **op1 Operacion** «Acceso al MLC para cancelar garantías comerciales de importación» — Acceso de la entidad financiera local al mercado de cambios para cancelar cartas de crédito o letras avaladas que garantizan importaciones de bienes con registro aduanero pendiente, incluso sin cumplirse los requisitos para el acceso del cliente · props: `{"tipo": "acceso al mercado de cambios"}` · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero pendiente»
- **p1 Potestad** «Acceso propio de la entidad sin requisitos del cliente» — La entidad puede acceder al mercado de cambios para cancelar las garantías, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas»
- **c1 Condicion** «Cumplimiento de condiciones vigentes a la emisión» — Que se verifique que se cumplían las condiciones aplicables según la fecha de emisión de la garantía y el tipo de operación garantizada · tramo [exacta]: «en la medida que se verifique que se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada»
- **c2 Condicion** «Garantías emitidas desde 13/12/23» — Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23 · props: `{"umbrales": [{"tramo": "a partir del\n13/12/23", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['a partir del 13/12/23'] · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»
- **o1 Obligacion** «Documentación de importación con registro desde 13/12/23 y plazo de pago» — La entidad debe contar con documentación que demuestre que la operación garantizada era una importación con registro de ingreso a partir del 13/12/23 y que el pago garantizado debía concretarse a partir de la fecha estimada de arribo más el plazo del punto 10.10.1 más 15 días corridos · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes …'] · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha»
- **x1 Excepcion** «Situación del punto 10.10.2.11 — requisito de plazo de pago» — No se exige demostrar el plazo de pago diferido cuando la operación queda comprendida en el punto 10.10.2.11 · tramo [exacta]: «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- **x2 Excepcion** «Pago desde embarque para porción a la vista» — Para garantías emitidas desde 14/04/25, cumpliéndose las restantes condiciones, se admite que el pago garantizado se concrete desde la fecha estimada de embarque cuando corresponde a la porción por la que el cliente pudo pagar a la vista según 10.10.2.1 o 10.10.2.2 · props: `{"umbrales": [{"tramo": "a partir del 14/04/25", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['a partir del 14/04/25'] · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen»
- **c3 Condicion** «Porción con pagos a la vista admitidos» — Que el pago corresponda a la porción por la que el cliente pudo pagar a la vista según 10.10.2.1 o 10.10.2.2 · tramo [exacta]: «cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista»
- **o2 Obligacion** «Boleto a nombre propio concepto B11» — El boleto de venta se efectúa a nombre de la propia entidad como cliente por el concepto B11 · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente»
- **o3 Obligacion** «Informar CUIT del importador en SEPAIMPO» — Por los pagos realizados, informar en SEPAIMPO la CUIT del importador dentro de 5 días hábiles · props: `{"tipo": "reporte_al_supervisor"}` · umbral: ['dentro de los 5 (cinco) días hábiles'] · tramo [exacta]: «la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador»
- **o4 Obligacion** «Denuncia por falta de oficialización del despacho» — Si no cuenta con registro de oficialización del despacho dentro de 90 días corridos del acceso, la entidad debe efectuar la denuncia · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «la entidad deberá efectuar la correspondiente denuncia»
- **c4 Condicion** «Sin oficialización del despacho en 90 días» — Falta de registro de oficialización del despacho dentro de 90 días corridos del acceso · umbral: ['dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cam…'] · tramo [exacta]: «En la medida que la entidad no cuente con el registro de la oficialización del despacho de importación dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cambios»
- **cm Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- R: to TextoOrdenado —referencia→ cm Comunicacion
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ o1 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: x1 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: x2 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: c3 Condicion —condicion_de→ x2 Excepcion
- R: o2 Obligacion —regula→ op1 Operacion
- R: op1 Operacion —requiere→ o3 Obligacion
- R: o3 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: op1 Operacion —requiere→ o4 Obligacion
- R: o4 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: c4 Condicion —condicion_de→ o4 Obligacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «emitidas desde el 13/12/23» | `condicion_con_relacion` |  | c2 Condicion con el umbral «a partir del 13/12/23» —condicion_de→ o1 Obligacion |
| 2 | «desde el 14/04/25» | `dentro_de_norma` |  | umbral «a partir del 14/04/25» dentro de la Excepcion x2 (la norma que admite el pago desde el embarque); la fecha no es una Condicion propia |
| 3 | «con pagos a la vista» | `condicion_con_relacion` |  | c3 Condicion «Porción con pagos a la vista admitidos» —condicion_de→ x2 Excepcion (la norma de la admisión) |
| 4 | «sin oficialización a 90 días» | `condicion_con_relacion` |  | c4 Condicion con el umbral —condicion_de→ o4 Obligacion |

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

### Extracción (código W)

- **op1 Operacion** «Imputación en gestión de cobro en SEPAIMPO» — Imputación en el SEPAIMPO, como en «gestión de cobro», del pago de importaciones con registro de ingreso aduanero pendiente, por incumplimiento del proveedor · props: `{"tipo": "imputación de pago de importación"}` · tramo [exacta]: «podrá imputarlo en el SEPAIMPO como en "gestión de cobro"»
- **p1 Potestad** «Facultad de imputar en gestión de cobro» — La entidad a cargo del seguimiento puede imputar el pago en el SEPAIMPO como en gestión de cobro cuando se da alguna de las condiciones (alternativas) i), ii) o iii) · tramo [exacta]: «La entidad a cargo del seguimiento del pago realizado, podrá imputarlo en el SEPAIMPO como en "gestión de cobro" cuando se dé alguna de las siguientes condiciones:»
- **c1 Condicion** «Control de cambios en país del exportador» — Supuesto i): el importador demuestra su gestión de cobro y que la falta de ingreso obedece a demoras por restricciones a los giros de divisas en el país del proveedor, acreditado con copia con legalización consular de la normativa de control cambiario · tramo [exacta]: «El importador puede demostrar su gestión de cobro y que la falta de ingreso obedece a que, en el país del proveedor del exterior, existen demoras por restricciones a los giros de divisas.»
- **c2 Condicion** «Insolvencia posterior del proveedor sin garantías» — Supuesto ii): insolvencia posterior del proveedor del exterior sin garantías de devolución, con aporte por el importador de la documentación a) y b), legalizada consularmente o según el Convenio de La Haya cuando corresponda · tramo [exacta]: «Insolvencia posterior del proveedor del exterior, no contándose con garantías de devolución de los fondos.»
- **c2a Condicion** «Constancia de publicaciones del trámite falencial» — Para el supuesto ii), el importador aporta constancia de las publicaciones del inicio del trámite falencial conforme la legislación del país en que tramite · tramo [exacta]: «constancia de las publicaciones que hagan saber el inicio del trámite falencial»
- **c2b Condicion** «Constancia de presentación para reconocimiento de acreencia» — Para el supuesto ii), el importador aporta constancia de la presentación para el reconocimiento y pago de su acreencia, certificada por la autoridad interviniente · tramo [exacta]: «constancia de la presentación efectuada para obtener el reconocimiento y pago de su acreencia, certificada por la autoridad interviniente en el proceso»
- **c3a Condicion** «Deudor moroso: reclamos por aseguradoras o agencias» — Supuesto iii) a): el importador demuestra fehacientemente su gestión de cobro mediante reclamos de compañías de seguro de crédito a la exportación o agencias de recupero contratadas; válido solo si lo adeudado no supera USD 100.000 · tramo [exacta]: «El importador demuestre en forma fehaciente su gestión de cobro a través de los reclamos efectuados al obligado de pago por compañías de seguro de crédito a la exportación o de entidades constituidas como agencias de recupero»
- **c3a2 Condicion** «Adeudado no superior a USD 100.000» — La alternativa iii) a) solo vale si el valor adeudado por el no residente no supera el equivalente de USD 100.000 · umbral: ['no supere el equivalente de USD 100.000'] · tramo [exacta]: «Esta alternativa solo será válida en la medida que el valor adeudado al importador por el no residente no supere el equivalente de USD 100.000»
- **c3b Condicion** «Deudor moroso: acciones judiciales iniciadas» — Supuesto iii) b): el importador inició y mantiene acciones judiciales, acreditadas con copia certificada del escrito de demanda, legalizada consularmente o según Convenio de La Haya · tramo [exacta]: «El importador argentino haya iniciado y mantenga acciones judiciales contra el proveedor del exterior o contra quien corresponda»
- **o1 Obligacion** «Declaración jurada del importador — exigencia de entidad» — La entidad debe exigir una declaración jurada sobre el carácter genuino de lo declarado, firmada por el importador, su representante legal o apoderado con facultades suficientes · props: `{"tipo": "otra"}` · tramo [exacta]: «En todos los casos, la entidad deberá exigir, además de la documentación señalada, una declaración jurada sobre el carácter genuino de lo declarado»
- **o2 Obligacion** «Ingreso y liquidación de lo percibido en 20 días» — El monto en moneda extranjera percibido por el importador debe ingresarse y liquidarse en el mercado de cambios dentro de 20 días hábiles de su percepción · props: `{"tipo": "otra"}` · umbral: ['dentro de los 20 (veinte) días hábiles siguientes a la fecha de efectiva percepc…'] · tramo [exacta]: «Si el importador percibiera un monto en moneda extranjera, el mismo deberá ser ingresado y liquidado en el mercado de cambios dentro de los 20 (veinte) días hábiles siguientes a la fecha de efectiva percepción.»
- **c4 Condicion** «Percepción de monto en moneda extranjera» — Supuesto de que el importador perciba un monto en moneda extranjera · tramo [exacta]: «Si el importador percibiera un monto en moneda extranjera»
- **op2 Operacion** «Permanencia en gestión de cobro» — Permanencia de la operación en estado de gestión de cobro en SEPAIMPO · props: `{"tipo": "permanencia en estado de gestión de cobro"}` · tramo [exacta]: «la operación podrá permanecer en "gestión de cobro" mientras se demuestre la vigencia del reclamo»
- **c5 Condicion** «Vigencia del reclamo y de condiciones de demora» — La operación permanece en gestión de cobro mientras se demuestre la vigencia del reclamo y de las condiciones de la demora · tramo [exacta]: «mientras se demuestre la vigencia del reclamo y de las condiciones que explican la demora en la ejecución de la transferencia»
- **r1 Restriccion** «Hasta cinco prórrogas de hasta 180 días» — Para la permanencia en gestión de cobro la entidad otorgará hasta cinco prórrogas sucesivas de hasta 180 días corridos cada una · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "hasta cinco prórrogas sucesivas", "comparacion": "maximo_inclusivo", "base": "cinco prórrogas sucesivas", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['hasta cinco prórrogas sucesivas', 'de hasta 180 (ciento ochenta) días corridos'] · tramo [exacta]: «la entidad otorgará hasta cinco prórrogas sucesivas de hasta 180 (ciento ochenta) días corridos»
- **o3 Obligacion** «Registro de no recupero y fin del seguimiento» — Agotados los plazos máximos y renovaciones, la entidad registra en el SEPAIMPO el no recupero total o parcial de los fondos, finalizando su seguimiento del pago · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «Utilizados los plazos máximos con sus sucesivas renovaciones, la entidad registrará la condición de no recupero total o parcial de los fondos en el SEPAIMPO»
- **c6 Condicion** «Agotamiento de plazos máximos y renovaciones» — Uso de los plazos máximos con sus sucesivas renovaciones · tramo [exacta]: «Utilizados los plazos máximos con sus sucesivas renovaciones»
- **o4 Obligacion** «Ingreso de todo recupero en 20 días hábiles» — Independientemente del cierre del seguimiento, el importador debe ingresar por el mercado de cambios todo recupero en moneda extranjera relativo al pago dentro de 20 días hábiles del cobro · props: `{"tipo": "otra"}` · umbral: ['dentro de los 20 (veinte) días hábiles de la fecha de cobro'] · tramo [exacta]: «la obligación del importador de ingresar por el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro, todo recupero en moneda extranjera»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad a cargo del seguimiento del pago realizado»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad a cargo del seguimiento del pago realizado») —ejecuta→ op1 Operacion
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c2a Condicion —condicion_de→ p1 Potestad
- R: c2b Condicion —condicion_de→ p1 Potestad
- R: c3a Condicion —condicion_de→ p1 Potestad
- R: c3a2 Condicion —condicion_de→ p1 Potestad
- R: c3b Condicion —condicion_de→ p1 Potestad
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o2 Obligacion —aplica_a→ Sujeto_importador (mención «el importador»)
- R: c4 Condicion —condicion_de→ o2 Obligacion
- R: c5 Condicion —condicion_de→ op2 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: r1 Restriccion —limita→ op2 Operacion
- R: o3 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: c6 Condicion —condicion_de→ o3 Obligacion
- R: o4 Obligacion —aplica_a→ Sujeto_importador (mención «importador»)

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «i) control de cambios» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ p1 Potestad |
| 2 | «ii) insolvencia (con a y b)» | `condicion_con_relacion` |  | c2 Condicion (y c2a, c2b) —condicion_de→ p1 Potestad |
| 3 | «a hasta USD 100.000» | `condicion_con_relacion` |  | c3a Condicion y c3a2 Condicion (el umbral) —condicion_de→ p1 Potestad |
| 4 | «b acciones judiciales» | `condicion_con_relacion` |  | c3b Condicion —condicion_de→ p1 Potestad |
| 5 | «percepción en moneda extranjera» | `condicion_con_relacion` |  | c4 Condicion «Percepción de monto en moneda extranjera» —condicion_de→ o2 Obligacion |

## `ext::10.5::intro` — [bloque intro] Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente.

Grupos: omisiones.

### Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.5. Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente.
> *propio:* Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 estará sujeto a un seguimiento desde la fecha de acceso al mercado de cambios hasta la fecha en que se produzca su regularización. Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento de ese pago, y por hasta el monto girado, la existencia de: i) el registro de ingreso aduanero a su nombre o a nombre de un tercero en la medida que se cumplan las condiciones establecidas en la presente normativa; y/o ii) la liquidación en el mercado de cambios de las divisas asociadas a la devolución del pago efectuado; y/o iii) otras formas de regularización previstas en la presente norma según las condiciones y límites establecidos en cada caso; y/o iv) la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la operación. El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago y deberá estar debidamente justificado por ésta.

### Extracción (código W)

- **op1 Operacion** «Pago de importaciones con ingreso aduanero pendiente» — Pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 con acceso al mercado de cambios · props: `{"tipo": "pago de importaciones"}` · tramo [exacta]: «Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19»
- **o1 Obligacion** «Seguimiento hasta regularización — pago de importaciones pendiente» — Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 queda sujeto a seguimiento desde la fecha de acceso al mercado de cambios hasta su regularización, a cargo de la entidad encargada del seguimiento. · props: `{"tipo": "otra"}` · tramo [exacta]: «estará sujeto a un seguimiento desde la fecha de acceso al mercado de cambios hasta la fecha en que se produzca su regularización»
- **d1 Definicion** «Situación regularizada de pagos de importaciones» — La situación de estos pagos se considera regularizada a efectos cambiarios cuando se demuestra ante la entidad encargada del seguimiento, por hasta el monto girado, la existencia de alguno o varios de: registro de ingreso aduanero (propio o de tercero, cumpliendo condiciones); liquidación de divisas por devolución del pago; otras formas de regularización previstas; conformidad del BCRA. · props: `{"termino": "regularizada"}` · tramo [exacta]: «Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento de ese pago, y por hasta el monto girado, la existencia de:»
- **c1 Condicion** «Registro de ingreso aduanero — regularización» — Existencia del registro de ingreso aduanero a nombre del importador o de un tercero, cumpliendo las condiciones de la normativa (supuesto alternativo, y/o). · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «el registro de ingreso aduanero a su nombre o a nombre de un tercero en la medida que se cumplan las condiciones establecidas en la presente normativa»
- **c2 Condicion** «Liquidación de divisas por devolución — regularización» — Liquidación en el mercado de cambios de las divisas asociadas a la devolución del pago (supuesto alternativo, y/o). · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «la liquidación en el mercado de cambios de las divisas asociadas a la devolución del pago efectuado»
- **c3 Condicion** «Otras formas previstas — regularización» — Otras formas de regularización previstas en la norma, según sus condiciones y límites (supuesto alternativo, y/o). · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «otras formas de regularización previstas en la presente norma según las condiciones y límites establecidos en cada caso»
- **c4 Condicion** «Conformidad del BCRA — regularización» — Conformidad del BCRA para dar por regularizada parte o el total de la operación (supuesto alternativo, y/o). · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la operación»
- **r1 Restriccion** «Pedido de conformidad solo por entidad de seguimiento» — El pedido de conformidad al BCRA solo puede ser tramitado por la entidad encargada del seguimiento del pago. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago»
- **op2 Operacion** «Pedido de conformidad de regularización al BCRA» — Tramitación ante el BCRA del pedido de conformidad para dar por regularizada parte o el total de la operación · props: `{"tipo": "solicitud"}` · tramo [exacta]: «El pedido solo podrá ser tramitado»
- **o2 Obligacion** «Justificación debida del pedido de conformidad» — La entidad encargada del seguimiento debe justificar debidamente el pedido de conformidad ante el BCRA. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «deberá estar debidamente justificado por ésta»
- **p1 Potestad** «Conformidad BCRA para regularizar operación» — El BCRA puede otorgar conformidad para dar por regularizada parte o el total de la operación. · tramo [exacta]: «la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la operación»
- R: op1 Operacion —requiere→ o1 Obligacion
- R: r1 Restriccion —limita→ op2 Operacion
- R: o2 Obligacion —regula→ op2 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad encargada del seguimiento del pago»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad encargada del seguimiento del pago»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «la entidad encargada del seguimiento del pago») —ejecuta→ op2 Operacion
- R: p1 Potestad —aplica_a→ Sujeto_bcra (mención «BCRA»)
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad encargada del seguimiento de ese pago»)
- Omisión `relacion_sin_predicado` [exacta]: «Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre» — Las condiciones i)-iv) son supuestos de la regularización (Definicion); condicion_de no admite Definicion como rango. Se habría usado condicion_de.
- Omisión `relacion_sin_predicado` [exacta]: «Se considerará regularizada la situación de estos pagos» — La regularización pone fin al seguimiento (Obligacion); no hay predicado para el término de una obligación.

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:4 | sí | «a los efectos cambiarios» | `extraida_tramo_verificado` |  | d1 Definicion [exacta], tramo que contiene el fragmento (además om#0 relacion_sin_predicado sobre la misma oración) |

## `ext::13.3.9` — el pago sea a una contraparte no vinculada al cliente y se concrete

Grupos: omisiones.

### Texto

> *heredado:* Sección 13. Pagos de servicios prestados por no residentes.
> *heredado:* 13.3. Pagos de servicios que fueron o serán prestados o devengados a partir del 13/12/23 con
> *heredado:* anterioridad a lo previsto en los puntos 13.2.3. a 13.2.7. También será admisible el acceso para el pago de servicios que fueron o serán prestados o devengados a partir del 13/12/23 con antelación a los plazos previstos en los puntos 13.2.3. a 13.2.7., cuando adicionalmente a los restantes requisitos normativo, se verifique el encuadre en alguna de las siguientes situaciones:
> *propio:* 13.3.9. el pago sea a una contraparte no vinculada al cliente y se concrete mediante la realización de un canje y/o arbitraje con los fondos depositados en una cuenta en moneda extranjera en una entidad financiera local.

### Extracción (código W)

- **c1 Condicion** «Contraparte no vinculada — pago anticipado de servicios» — Supuesto (junto con el de canje/arbitraje) de la situación 13.3.9 que habilita el acceso al mercado de cambios para el pago de servicios prestados o devengados a partir del 13/12/23 con antelación a los plazos de los puntos 13.2.3. a 13.2.7.: que el pago sea a una contraparte no vinculada al cliente. · tramo [exacta]: «el pago sea a una contraparte no vinculada al cliente»
- **c2 Condicion** «Canje/arbitraje con fondos en cuenta local — pago anticipado» — Supuesto (junto con el de contraparte no vinculada) de la situación 13.3.9 que habilita el acceso anticipado para el pago de servicios: que el pago se concrete mediante un canje y/o arbitraje con fondos depositados en una cuenta en moneda extranjera en una entidad financiera local. · tramo [exacta]: «se concrete mediante la realización de un canje y/o arbitraje con los fondos depositados en una cuenta en moneda extranjera en una entidad financiera local»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:1 | sí | «También será admisible el acceso para el pago de servicios que fueron o serán prestados o devengados a partir del 13/12/23 con antelación a los plazos previstos…» | `ausente` |  | ninguna entidad ni omisión cubre la oración del heredado |

## `ext::13.5` — Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas por entidades

Grupos: omisiones.

### Texto

> *heredado:* Sección 13. Pagos de servicios prestados por no residentes.
> *propio:* 13.5. Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas por entidades financieras para garantizar importaciones de servicios. Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios, en la medida que se verifique que cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada. En particular, en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23 y el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le corresponde al servicio por el punto 13.2. más otros 15 (quince) días corridos a la fecha estimada de prestación o devengamiento del servicio. En caso de tratarse una operación del concepto "S30. Servicios de fletes por operaciones de importaciones de bienes" que encuadra en lo previsto en el punto 10.10.2.1., debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar 15 (quince) días corridos a la fecha estimada de embarque de los bienes en origen.

### Extracción (código W)

- **op1 Operacion** «Pagos propios por cartas de crédito/letras avaladas de importación de servicios» — Acceso al mercado de cambios de entidades financieras para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de servicios · props: `{"tipo": "acceso al mercado de cambios"}` · tramo [exacta]: «tendrán acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios»
- **p1 Potestad** «Acceso al MLC — pagos propios por cartas de crédito» — Las entidades financieras pueden acceder al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas que garantizan importaciones de servicios · tramo [exacta]: «Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios»
- **c1 Condicion** «Cumplimiento de condiciones vigentes a la emisión» — Se verifique que las operaciones cumplían las condiciones aplicables según la fecha de emisión u otorgamiento de la carta de crédito o letra avalada · tramo [exacta]: «en la medida que se verifique que cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada»
- **c2 Condicion** «Carta de crédito emitida desde 13/12/23» — Supuesto de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23 · tramo [exacta]: «en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»
- **o1 Obligacion** «Documentación de servicio y plazo de pago garantizado» — La entidad debe contar con documentación que demuestre que, al apertura/emisión, el servicio garantizado fue prestado o devengado desde el 13/12/23 y que el pago garantizado debía concretarse a partir de la fecha estimada de prestación o devengamiento más el plazo del punto 13.2 más 15 días corridos · props: `{"tipo": "otra", "umbrales": [{"tramo": "el plazo en días corridos que le corresponde al servicio por el punto 13.2.", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['el plazo en días corridos que le corresponde al servicio por el punto 13.2.', 'más otros 15 (quince) días corridos a la fecha estimada de prestación o devengam…'] · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23 y el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días …»
- **c3 Condicion** «Fletes S30 encuadrados en punto 10.10.2.1.» — Operación del concepto S30 fletes por importaciones de bienes encuadrada en el punto 10.10.2.1. · tramo [exacta]: «En caso de tratarse una operación del concepto "S30. Servicios de fletes por operaciones de importaciones de bienes" que encuadra en lo previsto en el punto 10.10.2.1.»
- **o2 Obligacion** «Fletes S30: pago desde embarque más 15 días» — Para fletes S30 del punto 10.10.2.1., la entidad debe contar con documentación que demuestre que el pago garantizado debía concretarse a partir de la fecha estimada de embarque más 15 días corridos · props: `{"tipo": "otra"}` · umbral: ['adicionar 15 (quince) días corridos a la fecha estimada de embarque de los biene…'] · tramo [exacta]: «debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar 15 (quince) días corridos a la fecha estimada de embarque de los bienes en origen»
- R: p1 Potestad —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- R: Sujeto_entidad_financiera (mención «Las entidades financieras») —ejecuta→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ o1 Obligacion
- R: c3 Condicion —condicion_de→ o2 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o2 Obligacion —condiciona→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:24 | sí | «En particular, en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23» | `extraida_tramo_verificado` |  | c2 Condicion [exacta] con el mismo tramo (sin «En particular») |

## `ext::14.5.7` — Los aportes de inversión directa en especie instrumentados mediante la entrega al

Grupos: grupo_c.

### Texto

> *heredado:* Sección 14. Disposiciones complementarias asociadas al Régimen de Incentivo para Grandes Inversiones (RIGI).
> *heredado:* En esta sección se detallan las disposiciones complementarias en materia cambiaria que, en la medida que las disposiciones generales no resulten más favorables, resultan aplicables a un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo los referidas al "Régimen de Incentivo para Grandes Inversiones" (RIGI) establecido en el Título VII de la Ley 27.742 y reglamentado por el Decreto 749/24 y concordantes.
> *heredado:* 14.5. Otras disposiciones.
> *propio:* 14.5.7. Los aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital podrán ser computados como ingresados y liquidados en el mercado de cambios en la medida que: i) El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte que será computado como ingresado y liquidado en el mercado de cambios. La operación podrá incluir bienes que no revistan la condición de bien de capital en la medida que aquellos que lo sean representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado y la entidad cuente con una declaración jurada del cliente en la cual deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios para el funcionamiento, construcción o instalación de los bienes de capital que se están adquiriendo. La entidad deberá contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO). ii) El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte. En caso de no disponerla, deberá presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio de la decisión de capitalización definitiva de los aportes de capital computados de acuerdo con los requisitos legales correspondientes y comprometerse a presentar la documentación de la capitalización definitiva del aporte dentro de los 365 (trescientos sesenta y cinco) días corridos desde el inicio del trámite. iii) Una entidad financiera haya registrado al aporte de capital en el régimen informático de operaciones de cambio (RIOC) mediante la confección de dos boletos de cambio sin movimiento de fondos con las siguientes características: a) Los boletos deberán ser registrados en la fecha en que se produjo el registro de ingreso aduanero de los bienes, independientemente de cuál sea el momento en que el cliente solicite su registro ante la entidad financiera. b) El boleto de compra se confeccionará con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo. En caso de que el VPU contemple la posibilidad de aplicar cobros de exportaciones de bienes para la repatriación del aporte, la entidad deberá asignar el correspondiente número de identificación (número APX) para el "Seguimiento de anticipos y otras financiaciones de exportación de bienes", el cual quedará a cargo de la propia entidad. c) El boleto de venta se confeccionará con el código de concepto de pago diferido de importaciones de bienes de capital, dejando constancia que el pago se enmarca en el presente mecanismo.

### Extracción (código W)

- **op1 Operacion** «Cómputo como ingresado y liquidado de aporte en especie» — Cómputo como ingresados y liquidados en el mercado de cambios de aportes de inversión directa en especie instrumentados mediante entrega al VPU de bienes de capital · props: `{"tipo": "cómputo de ingreso y liquidación"}` · tramo [exacta]: «Los aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital podrán ser computados como ingresados y liquidados en el mercado de cambios»
- **p1 Potestad** «Cómputo de aportes en especie con bienes de capital» — Los aportes de inversión directa en especie mediante entrega al VPU de bienes de capital pueden computarse como ingresados y liquidados en el mercado de cambios si se cumplen los requisitos i) a iii). · tramo [exacta]: «podrán ser computados como ingresados y liquidados en el mercado de cambios en la medida que:»
- **c1 Condicion** «Registro de ingreso aduanero consistente con aporte» — El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte a computar. · props: `{"umbrales": [{"tramo": "por\nun valor consistente con el monto del aporte", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por un valor consistente con el monto del aporte'] · tramo [exacta]: «El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte»
- **p2 Potestad** «Inclusión de bienes que no son de capital» — La operación puede incluir bienes que no sean bienes de capital, sujeto a las condiciones del 90% FOB y la declaración jurada. · tramo [exacta]: «La operación podrá incluir bienes que no revistan la condición de bien de capital»
- **c2 Condicion** «Bienes de capital mínimo 90% del FOB» — Los bienes de capital representen como mínimo el 90% del valor FOB total pagado. · umbral: ['como mínimo el 90% (noventa por ciento) del valor FOB total pagado'] · tramo [exacta]: «en la medida que aquellos que lo sean representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado»
- **c3 Condicion** «Declaración jurada del cliente sobre restantes bienes» — La entidad cuente con declaración jurada del cliente de que los restantes bienes son repuestos, accesorios o materiales necesarios para funcionamiento, construcción o instalación de los bienes de capital. · tramo [exacta]: «la entidad cuente con una declaración jurada del cliente en la cual deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios»
- **o1 Obligacion** «Certificación SEPAIMPO — aporte en especie» — La entidad debe contar con la certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO). · props: `{"tipo": "otra"}` · tramo [exacta]: «La entidad deberá contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO).»
- **o2 Obligacion** «Documentación de capitalización definitiva — VPU» — El VPU debe presentar la documentación que avale la capitalización definitiva del aporte. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte.»
- **o3 Obligacion** «Constancia inicio inscripción y compromiso 365 días» — Si no dispone de la documentación, el VPU debe presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio de la capitalización definitiva y comprometerse a presentar la documentación dentro de 365 días corridos desde el inicio del trámite. · props: `{"tipo": "presentacion_informativa"}` · umbral: ['dentro de los 365 (trescientos sesenta y cinco) días corridos desde el inicio de…'] · tramo [exacta]: «En caso de no disponerla, deberá presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio»
- **c4 Condicion** «Sin documentación de capitalización definitiva» — El VPU no dispone de la documentación de capitalización definitiva. · tramo [exacta]: «En caso de no disponerla»
- **c5 Condicion** «Registro del aporte en RIOC con dos boletos» — Una entidad financiera haya registrado el aporte en el RIOC mediante dos boletos de cambio sin movimiento de fondos con las características a) a c). · tramo [exacta]: «Una entidad financiera haya registrado al aporte de capital en el régimen informático de operaciones de cambio (RIOC) mediante la confección de dos boletos de cambio sin movimiento de fondos»
- **op2 Operacion** «Registro en RIOC de boletos sin movimiento de fondos» — Registro del aporte de capital en especie en el RIOC mediante dos boletos de cambio (compra y venta) sin movimiento de fondos · props: `{"tipo": "registro de operación de cambio"}` · tramo [exacta]: «registrado al aporte de capital en el régimen informático de operaciones de cambio (RIOC) mediante la confección de dos boletos de cambio sin movimiento de fondos»
- **o4 Obligacion** «Fecha de registro de boletos: ingreso aduanero» — Los boletos deben registrarse en la fecha del registro de ingreso aduanero de los bienes, independientemente de cuándo el cliente solicite su registro ante la entidad financiera. · props: `{"tipo": "otra"}` · tramo [exacta]: «Los boletos deberán ser registrados en la fecha en que se produjo el registro de ingreso aduanero de los bienes»
- **o5 Obligacion** «Código de concepto del boleto de compra» — El boleto de compra se confecciona con un código de concepto que identifique que es un aporte comprendido en este mecanismo. · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de compra se confeccionará con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo.»
- **o6 Obligacion** «Asignación número APX si repatriación con exportaciones» — Si el VPU contempla aplicar cobros de exportaciones de bienes a la repatriación del aporte, la entidad debe asignar el número APX para el Seguimiento de anticipos y otras financiaciones de exportación de bienes, que queda a cargo de la propia entidad. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «la entidad deberá asignar el correspondiente número de identificación (número APX)»
- **c6 Condicion** «VPU contempla repatriar con cobros de exportaciones» — El VPU contempla aplicar cobros de exportaciones de bienes para la repatriación del aporte. · tramo [exacta]: «En caso de que el VPU contemple la posibilidad de aplicar cobros de exportaciones de bienes para la repatriación del aporte»
- **o7 Obligacion** «Código de concepto del boleto de venta» — El boleto de venta se confecciona con el código de concepto de pago diferido de importaciones de bienes de capital, dejando constancia de que el pago se enmarca en este mecanismo. · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta se confeccionará con el código de concepto de pago diferido de importaciones de bienes de capital»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c5 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p2 Potestad
- R: c3 Condicion —condicion_de→ p2 Potestad
- R: c4 Condicion —condicion_de→ o3 Obligacion
- R: c6 Condicion —condicion_de→ o6 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o2 Obligacion —condiciona→ op1 Operacion
- R: o4 Obligacion —regula→ op2 Operacion
- R: o5 Obligacion —regula→ op2 Operacion
- R: o7 Obligacion —regula→ op2 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: o2 Obligacion —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- R: o3 Obligacion —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- R: o6 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o4 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Una entidad financiera»)
- R: o5 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Una entidad financiera»)
- R: o7 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Una entidad financiera»)
- R: Sujeto_entidad_financiera (mención «Una entidad financiera») —ejecuta→ op2 Operacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «i) a iii) en la medida que» (i)) | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ p1 Potestad |
| 2 | «i) a iii) en la medida que» (ii)) | `dentro_de_norma` |  | extraído como norma de otro tipo: o2 Obligacion —condiciona→ op1; sin Condicion para ii) |
| 3 | «i) a iii) en la medida que» (iii)) | `condicion_con_relacion` |  | c5 Condicion —condicion_de→ p1 Potestad |
| 4 | «al menos 90 % del FOB» | `condicion_con_relacion` |  | c2 Condicion con el umbral —condicion_de→ p2 Potestad |
| 5 | «en caso de no disponer la documentación» | `condicion_con_relacion` |  | c4 Condicion «Sin documentación de capitalización definitiva» —condicion_de→ o3 Obligacion |
| 6 | «VPU con cobros de exportaciones» | `condicion_con_relacion` |  | c6 Condicion —condicion_de→ o6 Obligacion |

## `ext::2.1` — Cobros de exportaciones de bienes.

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
> *propio:* 2.1. Cobros de exportaciones de bienes. En las Secciones 7., 8. y 9. se detallan las normas asociadas a la operatoria de exportaciones de bienes, las disposiciones relacionadas al seguimiento de las negociaciones de divisas por exportaciones de bienes (SECOEXPO) y del seguimiento de anticipos y otras financiaciones de exportación de bienes, respectivamente.

### Extracción (código W)

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

### Extracción (código W)

- **e1 Potestad** «Acceso anticipado para pago de deudas — entidades» — Las entidades podrán dar acceso al mercado de cambios a los residentes que deban realizar pagos de servicios de deudas financieras comprendidas en el punto 3.5. o de títulos valores con acceso según los puntos 3.6.1.3. a 3.6.1.5., para la compra de moneda extranjera con anterioridad al plazo admitido por la normativa para cada caso, en las condiciones que se enumeran a continuación. · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a los residentes que deban»
- **e2 Operacion** «Compra anticipada de moneda extranjera para servicios de deuda» — Compra de moneda extranjera por residentes en el mercado de cambios, con anterioridad al plazo admitido por la normativa, para pagos de servicios de deudas financieras del punto 3.5. o de títulos valores con acceso según puntos 3.6.1.3. a 3.6.1.5. · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «para la compra de moneda extranjera con anterioridad al plazo admitido por la normativa para cada caso»
- R: e1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)
- R: e2 Operacion —aplica_a→ Sujeto (mención «los residentes»)
- R: Sujeto (mención «los residentes») —ejecuta→ e2 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «Las entidades podrán dar acceso al mercado de cambios a los residentes» — Vínculo Potestad → Operacion (habilita); no hay predicado para él

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:20 | sí | «en las siguientes condiciones:» | `ausente` |  | ningún tramo contiene «en las siguientes condiciones:» (las omisiones de K y W refieren a «podrán dar acceso») |

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

### Extracción (código W)

- **x1 Excepcion** «Transferencias para canje o recompra de deuda — DJ 3.16.3.1/2» — En las declaraciones juradas de los puntos 3.16.3.1 y 3.16.3.2 (requisito de conformidad previa del BCRA) no se computan las transferencias de títulos a depositarias del exterior para participar de un canje o recompra de títulos de deuda del Gobierno Nacional, gobiernos locales u otros emisores residentes del sector privado. · tramo [no]: «no deberán tenerse en cuenta: […] las transferencias de títulos valores a entidades depositarias del exterior realizadas o a realizar por el cliente con el objeto de participar de un canje o una operación de recompra de títulos de deuda emitidos por el Gobierno Nacional, gobiernos locales u otros emisores residentes de…»
- **o1 Obligacion** «Compromiso de certificación de títulos canjeados» — Para la exclusión del inciso i), el cliente debe comprometerse a presentar la certificación por los títulos de deuda canjeados. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «El cliente deberá comprometerse a presentar la correspondiente certificación por los títulos de deuda canjeados.»
- **x2 Excepcion** «Entrega de activos locales por garantía de deuda» — En las DJ de los puntos 3.16.3.1 y 3.16.3.2 no se computa la entrega de activos locales para cancelar deuda con agencia oficial de crédito o entidad financiera del exterior, si se produce desde el vencimiento por cláusula de garantía del contrato. · tramo [no]: «no deberán tenerse en cuenta: […] la entrega de activos locales con el objeto de cancelar una deuda con una agencia oficial de crédito o una entidad financiera del exterior»
- **c2 Condicion** «A partir del vencimiento por cláusula de garantía» — La entrega se produce a partir del vencimiento como consecuencia de una cláusula de garantía del contrato de endeudamiento. · tramo [exacta]: «en la medida que se produzca a partir del vencimiento como consecuencia de una cláusula de garantía prevista en el contrato de endeudamiento»
- **x3 Excepcion** «Ventas de títulos con liquidación en ME aplicadas a pagos» — En las DJ de los puntos 3.16.3.1 y 3.16.3.2 no se computan las ventas de títulos con liquidación en moneda extranjera cuando la totalidad de los fondos se usó o usará dentro de 10 días corridos a alguna de las operaciones a) a e). · tramo [no]: «no deberán tenerse en cuenta: […] las ventas de títulos valores con liquidación en moneda extranjera en el país o en el exterior»
- **c3 Condicion** «Totalidad de fondos aplicada en 10 días» — La totalidad de los fondos se utiliza dentro de 10 días corridos en alguna de las operaciones a) a e). · umbral: ['dentro de los 10 (diez) días corridos'] · tramo [exacta]: «cuando la totalidad de los fondos obtenidos de tales liquidaciones se haya utilizado o será utilizada dentro de los 10 (diez) días corridos a las siguientes operaciones»
- **c3a Condicion** «a) Pagos de nuevos endeudamientos con 1 año de gracia» — Destino alternativo: pagos de nuevos endeudamientos financieros (punto 3.5) desembolsados desde 02/10/23 con al menos 1 año de gracia. · umbral: ['como mínimo 1 (un) año de gracia'] · tramo [exacta]: «Pagos a partir del vencimiento de capital o intereses de nuevos endeudamientos financieros comprendidos en el punto 3.5., desembolsados a partir del 02/10/23 y que contemplen como mínimo 1 (un) año de gracia para el pago de capital.»
- **c3b Condicion** «b) Repatriación de inversiones directas tras 1 año» — Destino alternativo: repatriaciones de inversiones directas de no residentes recibidas desde 02/10/23, al menos 1 año después del aporte y cumpliendo los mecanismos legales. · umbral: ['como mínimo 1 (un) año después de la concreción del aporte de capital'] · tramo [exacta]: «Repatriaciones del capital y rentas asociadas a las inversiones directas de no residentes recibidas a partir del 02/10/23, en la medida que la repatriación se produzca como mínimo 1 (un) año después de la concreción del aporte de capital y se haya dado cumplimiento a los mecanismos legales previstos en tales casos.»
- **c3c Condicion** «c) Pagos de títulos locales con 2 años de gracia» — Destino alternativo: pagos de títulos de deuda con registro público local emitidos desde 02/10/23, en ME, con al menos 2 años de gracia. · umbral: ['como mínimo 2 (dos) años de gracia'] · tramo [exacta]: «Pagos a partir del vencimiento de capital o intereses de títulos de deuda emitidos a partir del 02/10/23 con registro público en el país no comprendidos en el punto 3.5., denominados y suscriptos en moneda extranjera, con servicios pagaderos en moneda extranjera y que contemplen como mínimo 2 (dos) años de gracia para …»
- **c3d Condicion** «d) Pagos de refinanciaciones de a) y c)» — Destino alternativo: pagos de endeudamientos (3.5) que refinancian sin desembolso operaciones de a) y c), sin anticipar el vencimiento original. · tramo [exacta]: «Pagos a partir del vencimiento de capital o intereses de endeudamientos financieros comprendidos en el punto 3.5. que no generen desembolsos por ser refinanciaciones de capital y/o intereses de operaciones contempladas en los incisos a) y c) precedentes, en la medida que las refinanciaciones no anticipen el vencimiento…»
- **c3e Condicion** «e) Pagos de refinanciaciones de títulos de c)» — Destino alternativo: pagos de títulos con registro público local en ME que refinancian sin desembolso operaciones de c), sin anticipar el vencimiento original. · tramo [exacta]: «Pagos a partir del vencimiento de capital o intereses de títulos de emitidos con registro público en el país no comprendidos en el punto 3.5., denominados en moneda extranjera, con servicios pagaderos en moneda extranjera y que no generen desembolsos por ser refinanciaciones de capital y/o intereses de operaciones cont…»
- **o2 Obligacion** «DJ del cliente sobre uso de fondos en inversiones» — Para la exclusión del inciso iii), el cliente debe presentar DJ de que los fondos recibidos por las operaciones a) a c) se usaron totalmente en pagos en el país vinculados a inversiones en Argentina. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «En todos los casos el cliente deberá presentar una declaración jurada dejando constancia de que los fondos oportunamente recibidos por las operaciones detalladas en los incisos a) a c) precedentes se utilizaron en su totalidad para concretar pagos en el país relacionados con la concreción de inversiones en la República…»
- **x4 Excepcion** «Ventas o transferencias de BOPREAL de suscriptores primarios» — En las DJ de los puntos 3.16.3.1 y 3.16.3.2 no se computan ventas con liquidación en ME o transferencias al exterior de BOPREAL realizadas por quienes participaron de la suscripción primaria, hasta el monto adquirido en ella. · tramo [no]: «no deberán tenerse en cuenta: […] las ventas con liquidación en moneda extranjera en el país o en el exterior de los Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) o las transferencias de estos bonos a depositarios en el exterior»
- **c4 Condicion** «Hasta monto suscripto en forma primaria» — Realizadas por quienes participaron de la suscripción primaria y hasta el monto adquirido en ella. · props: `{"umbrales": [{"tramo": "por hasta el monto adquirido en la suscripción primaria", "comparacion": "maximo_inclusivo", "base": "monto adquirido en la suscripción primaria", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto adquirido en la suscripción primaria'] · tramo [exacta]: «cuando sean realizados por hasta el monto adquirido en la suscripción primaria por aquellos que participaron en dicha instancia»
- **x5 Excepcion** «Importadores con BOPREAL: ventas o transferencias al exterior» — En las DJ de los puntos 3.16.3.1 y 3.16.3.2 no se computan ventas con liquidación en ME en el exterior o transferencias al exterior de importadores que suscribieron BOPREAL por deudas de importaciones elegibles (4.4 y 4.5), con tope de valor de mercado. · tramo [no]: «no deberán tenerse en cuenta: […] las ventas con liquidación en moneda extranjera en el exterior o las transferencias a depositarios del exterior que concreten los importadores de bienes y servicios que hayan adquirido en una suscripción primaria Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por deudas …»
- **c5 Condicion** «Valor de mercado no supera diferencia vs. nominal» — El valor de mercado de las operaciones no supera la diferencia entre lo obtenido por la venta de BOPREAL en el exterior y su valor nominal, si aquel es menor. · props: `{"umbrales": [{"tramo": "no supere a la diferencia entre el valor obtenido por la venta con liquidación en moneda extranjera en el exterior de bonos BOPREAL adquiridos en las suscripciones primarias citadas y su valor nominal", "comparacion": "maximo_inclusivo", "base": "diferencia entre el valor obtenido por la venta con liquidación en moneda extranjera en el exterior de bonos BOPREAL adquiridos", "regla_comparacion": "limite_relativo:negacion:raiz_super", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['no supere a la diferencia entre el valor obtenido por la venta con liquidación e…'] · tramo [exacta]: «cuando el valor de mercado de estas operaciones no supere a la diferencia entre el valor obtenido por la venta con liquidación en moneda extranjera en el exterior de bonos BOPREAL adquiridos en las suscripciones primarias citadas y su valor nominal, si el primero resultase menor»
- R: c2 Condicion —condicion_de→ x2 Excepcion
- R: c3 Condicion —condicion_de→ x3 Excepcion
- R: c3a Condicion —condicion_de→ x3 Excepcion
- R: c3b Condicion —condicion_de→ x3 Excepcion
- R: c3c Condicion —condicion_de→ x3 Excepcion
- R: c3d Condicion —condicion_de→ x3 Excepcion
- R: c3e Condicion —condicion_de→ x3 Excepcion
- R: c4 Condicion —condicion_de→ x4 Excepcion
- R: c5 Condicion —condicion_de→ x5 Excepcion
- R: o1 Obligacion —aplica_a→ Sujeto_cliente (mención «El cliente»)
- R: o2 Obligacion —aplica_a→ Sujeto_cliente (mención «el cliente»)
- R: x5 Excepcion —aplica_a→ Sujeto_importador (mención «los importadores de bienes y servicios»)

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «garantía desde el vencimiento» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ x2 Excepcion |
| 2 | «fondos usados en 10 días» | `condicion_con_relacion` |  | c3 Condicion con el umbral —condicion_de→ x3 Excepcion |
| 3 | «repatriación a 1 año» | `condicion_con_relacion` |  | c3b Condicion con el umbral —condicion_de→ x3 Excepcion |
| 4 | «BOPREAL hasta el monto suscripto» | `condicion_con_relacion` |  | c4 Condicion con el umbral —condicion_de→ x4 Excepcion |
| 5 | «valor de mercado que no supere la diferencia» | `condicion_con_relacion` |  | c5 Condicion con el umbral —condicion_de→ x5 Excepcion |

## `ext::3.9::intro` — [bloque intro] Compra de moneda extranjera por parte de personas humanas residentes para la formación

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* 3.9. Compra de moneda extranjera por parte de personas humanas residentes para la formación
> *propio:* de activos externos bajo otras modalidades, la remisión de ayuda familiar u operaciones con derivados. Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de concepto A05) en la medida que no encuadre en el punto 3.12.1., sin la conformidad previa del BCRA, en la medida que se cumplan la totalidad de los siguientes requisitos:

### Extracción (código W)

- **p1 Potestad** «Acceso sin conformidad BCRA — personas humanas residentes» — Las entidades pueden dar acceso al mercado de cambios a personas humanas residentes para formación de activos externos (A01, A02, A03, A04, A06, A08, A14 y A24), remisión de ayuda familiar y operatoria con derivados (A05) que no encuadre en el punto 3.12.1., sin la conformidad previa del BCRA, en la medida que se cumplan la totalidad de los requisitos que se enumeran a continuación. · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes»
- **o1 Operacion** «Formación de activos externos — personas humanas residentes» — Acceso al mercado de cambios de personas humanas residentes para formación de activos externos, códigos A01, A02, A03, A04, A06, A08, A14 y A24 · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24)»
- **o2 Operacion** «Remisión de ayuda familiar — personas humanas residentes» — Acceso al mercado de cambios de personas humanas residentes para la remisión de ayuda familiar · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «la remisión de ayuda familiar»
- **o3 Operacion** «Operatoria con derivados A05 — personas humanas residentes» — Acceso al mercado de cambios de personas humanas residentes para operatoria con derivados, código A05 · props: `{"tipo": "operación con derivados"}` · tramo [exacta]: «para la operatoria con derivados (código de concepto A05)»
- **c1 Condicion** «Derivados no encuadrados en punto 3.12.1.» — La operatoria con derivados no debe encuadrar en el punto 3.12.1. para acceder sin conformidad previa. · tramo [exacta]: «en la medida que no encuadre en el punto 3.12.1.»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)
- R: Sujeto_persona_humana (mención «las personas humanas residentes») —ejecuta→ o1 Operacion
- R: Sujeto_persona_humana (mención «las personas humanas residentes») —ejecuta→ o2 Operacion
- R: Sujeto_persona_humana (mención «las personas humanas residentes») —ejecuta→ o3 Operacion
- R: c1 Condicion —condicion_de→ p1 Potestad
- Omisión `relacion_sin_predicado` [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos» — Potestad→Operacion (habilita); sin predicado. Ídem hacia o2 y o3.

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:18 | no | «de activos externos bajo otras modalidades, la remisión de ayuda familiar u operaciones con derivados.» | `ausente` |  | o2 Operacion tiene como tramo «la remisión de ayuda familiar», frase que también está en el cuerpo; nada cubre el fragmento del título |

## `ext::4.1.3.1` — Cuando el emisor de la tarjeta sea una entidad financiera, el titular podrá

Grupos: grupo_c.

### Texto

> *heredado:* Sección 4. Otras disposiciones específicas.
> *heredado:* 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tarjetas de
> *heredado:* crédito, compra y prepagas emitidas en el país.
> *heredado:* 4.1.3. Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o
> *heredado:* de compra.
> *propio:* 4.1.3.1. Cuando el emisor de la tarjeta sea una entidad financiera, el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos, debiendo aplicar como máximo en este caso el tipo de cambio vendedor (aplicable para operaciones efectuadas por ventanilla o a través de medios electrónicos, según corresponda) de la entidad emisora de la tarjeta del momento de cancelación –o día hábil inmediato anterior cuando el pago se efectúe un día inhábil–. En los casos donde los clientes hayan pactado el débito automático del resumen de la tarjeta en cuentas de la propia entidad emisora, aplicará el tipo de cambio vendedor para operaciones efectuadas a través de medios electrónicos de pago del cierre del mismo día hábil del pago.

### Extracción (código W)

- **op1 Operacion** «Cancelación de consumos en moneda extranjera con tarjeta» — Cancelación por el titular de consumos en moneda extranjera efectuados con tarjeta de crédito y/o compra emitida por una entidad financiera, en moneda extranjera o en pesos · props: `{"tipo": "cancelacion de consumos con tarjeta"}` · tramo [exacta]: «cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- **c1 Condicion** «Emisor de la tarjeta es entidad financiera» — Que el emisor de la tarjeta sea una entidad financiera · tramo [exacta]: «Cuando el emisor de la tarjeta sea una entidad financiera»
- **p1 Potestad** «Cancelar consumos en moneda extranjera o pesos» — El titular de la tarjeta emitida por entidad financiera puede cancelar los consumos en moneda extranjera en esa moneda o en pesos · tramo [exacta]: «el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- **r1 Restriccion** «Tope tipo de cambio vendedor — cancelación en pesos» — En la cancelación en pesos se aplica como máximo el tipo de cambio vendedor (ventanilla o medios electrónicos según corresponda) de la entidad emisora del momento de cancelación, o del día hábil inmediato anterior si el pago es en día inhábil · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "como máximo en este caso el tipo de cambio vendedor (aplicable para operaciones efectuadas por ventanilla o a través de medios electrónicos, según corresponda) de la entidad emisora de la tarjeta del momento de cancelación", "comparacion": "maximo_inclusivo", "base": "en este caso el tipo de cambio vendedor (aplicable para operaciones efectuadas por ventanilla o a través de medios electrónicos", "regla_comparacion": "limite_relativo:compuesta:como_maximo", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['como máximo en este caso el tipo de cambio vendedor (aplicable para operaciones …'] · tramo [exacta]: «debiendo aplicar como máximo en este caso el tipo de cambio vendedor (aplicable para operaciones efectuadas por ventanilla o a través de medios electrónicos, según corresponda) de la entidad emisora de la tarjeta del momento de cancelación –o día hábil inmediato anterior cuando el pago se efectúe un día inhábil–»
- **c2 Condicion** «Débito automático en cuenta de la emisora» — Que los clientes hayan pactado el débito automático del resumen en cuentas de la propia entidad emisora · tramo [exacta]: «En los casos donde los clientes hayan pactado el débito automático del resumen de la tarjeta en cuentas de la propia entidad emisora»
- **o1 Obligacion** «Tipo de cambio electrónico cierre — débito automático» — Con débito automático pactado en cuentas de la emisora, se aplica el tipo de cambio vendedor para operaciones por medios electrónicos de pago del cierre del mismo día hábil del pago · props: `{"tipo": "calculo"}` · tramo [exacta]: «aplicará el tipo de cambio vendedor para operaciones efectuadas a través de medios electrónicos de pago del cierre del mismo día hábil del pago»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ o1 Obligacion
- R: p1 Potestad —aplica_a→ Sujeto (mención «el titular»)
- R: r1 Restriccion —limita→ op1 Operacion
- R: o1 Obligacion —regula→ op1 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto (mención «la entidad emisora de la tarjeta»)
- R: Sujeto (mención «el titular») —ejecuta→ op1 Operacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «emisor entidad financiera» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ p1 Potestad |
| 2 | «pago en día inhábil» | `dentro_de_norma` |  | dentro de la Restriccion r1 (tramo y umbral); sin Condicion |
| 3 | «débito automático pactado» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ o1 Obligacion |

## `ext::4.1.3.2` — Cuando se trate de empresas no financieras emisoras de tarjetas de crédito

Grupos: grupo_c.

### Texto

> *heredado:* Sección 4. Otras disposiciones específicas.
> *heredado:* 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tarjetas de
> *heredado:* crédito, compra y prepagas emitidas en el país.
> *heredado:* 4.1.3. Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o
> *heredado:* de compra.
> *propio:* 4.1.3.2. Cuando se trate de empresas no financieras emisoras de tarjetas de crédito y/o compra, el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos –siendo aplicable el tipo de cambio vendedor por canales electrónicos publicado por el Banco de la Nación Argentina el mismo día hábil de la fecha de pago o hábil inmediato anterior cuando el pago se efectúe un día inhábil–.

### Extracción (código W)

- **e1 Operacion** «Cancelación de consumos en moneda extranjera con tarjeta» — Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o de compra · props: `{"tipo": "cancelación de consumos con tarjeta"}` · tramo [exacta]: «Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o»
- **e2 Potestad** «Cancelación en moneda extranjera o pesos — tarjetas de emisoras no financieras» — Cuando la tarjeta es de una empresa no financiera emisora de tarjetas de crédito y/o compra, el titular puede cancelar los consumos en moneda extranjera en esa moneda o en pesos; en pesos rige el tipo de cambio vendedor por canales electrónicos publicado por el Banco de la Nación Argentina el mismo día hábil de la fecha de pago, o el hábil inmediato anterior si el pago se hace un día inhábil. · no definidas: `{"tipo_de_cambio_aplicable": "tipo de cambio vendedor por canales electrónicos publicado por el Banco de la Nación Argentina el mismo día hábil de la fecha de pago o hábil inmediato anterior cuando el` · tramo [exacta]: «el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- **e3 Condicion** «Tarjeta emitida por empresa no financiera» — Supuesto: la emisora de la tarjeta es una empresa no financiera emisora de tarjetas de crédito y/o compra. · tramo [exacta]: «Cuando se trate de empresas no financieras emisoras de tarjetas de crédito y/o compra»
- R: e3 Condicion —condicion_de→ e2 Potestad
- R: e2 Potestad —aplica_a→ Sujeto (mención «el titular»)
- R: Sujeto (mención «el titular») —ejecuta→ e1 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «el titular podrá cancelar los consumos realizados en moneda extranjera» — Potestad que habilita la operación de cancelación; no hay predicado Potestad→Operacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «emisoras no financieras» | `condicion_con_relacion` |  | e3 Condicion «Tarjeta emitida por empresa no financiera» —condicion_de→ e2 Potestad |
| 2 | «pago en día inhábil» | `dentro_de_norma` |  | dentro de la Potestad e2 (descripción y propiedad no definida tipo_de_cambio_aplicable); sin Condicion |

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

### Extracción (código W)

- **c1 Condicion** «Ordenante empresa exterior firmante — boleto global procesadoras» — Condición (exigida junto con las demás) para elaborar el boleto global diario a nombre de la empresa local representante de la procesadora de pagos por ingresos de divisas: que las transferencias tengan como ordenante a la empresa del exterior firmante del acuerdo. · tramo [exacta]: «Las transferencias tengan como ordenante la empresa del exterior firmante del acuerdo»
- **c2 Condicion** «Canal entidad exterior con matriz Basilea — boleto global» — Condición (exigida junto con las demás) para elaborar el boleto global diario por ingresos de divisas a través de procesadoras de pagos: que las transferencias se canalicen por una entidad financiera del exterior cuya casa matriz o controlante esté radicada en un país miembro del Comité de Supervisión Bancaria de Basilea. · tramo [exacta]: «se canalicen a través de una entidad financiera del exterior cuya casa matriz o controlante se encuentre radicada en un país miembro del Comité de Supervisión Bancaria de Basilea»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:6 | sí | «5.8.2.2. Las transferencias tengan como ordenante la empresa del exterior firmante del acuerdo y se canalicen a través de una entidad financiera del exterior cu…» | `extraida_tramo_verificado` |  | c1 y c2 Condicion [exacta]: entre las dos cubren la oración |

## `ext::7.1.1.5` — 365 (trescientos sesenta y cinco) días corridos para las operaciones que se

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.1. Obligación de ingreso y liquidación en los plazos establecidos.
> *heredado:* 7.1.1. Exportaciones oficializadas a partir del 02/09/19.
> *heredado:* El contravalor en divisas de la exportación hasta alcanzar el valor facturado según la condición de venta pactada deberá ingresarse al país y liquidarse en el mercado de cambios. En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicios resultará aplicable lo dispuesto en los puntos 14.1.1. y 14.1.2., según corresponda. El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse en los siguientes plazos a computar desde la fecha del cumplido de embarque otorgado por la Aduana:
> *heredado:* Independientemente de los plazos máximos precedentes, los cobros de exportaciones deberán ser ingresados y liquidados en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro. La posibilidad de utilizar este plazo quedará supeditada en todos los casos al cumplimiento de los plazos previstos en los puntos 7.1.1.1. a 7.1.1.5. Los montos en moneda extranjera originados en cobros de siniestros por coberturas contratadas, en la medida que los mismos cubran el valor de los bienes exportados, están alcanzados por esta obligación. El exportador deberá seleccionar una entidad para que realice el "Seguimiento de las negociaciones de divisas por exportaciones de bienes". La obligación de ingreso y liquidación de divisas de un permiso de embarque se considerará cumplida cuando la entidad haya certificado tal situación por los mecanismos establecidos a tal efecto.
> *propio:* 7.1.1.5. 365 (trescientos sesenta y cinco) días corridos para las operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE", independientemente del tipo de bien exportado.

### Extracción (código W)

- **e1 Obligacion** «Plazo 365 días EXPORTA SIMPLE — ingreso y liquidación» — El ingreso y liquidación por el mercado de cambios de las divisas de exportaciones de bienes oficializadas a partir del 02/09/19 debe concretarse dentro de 365 días corridos desde el cumplido de embarque otorgado por la Aduana, para las operaciones concretadas en el marco del régimen "EXPORTA SIMPLE", sin importar el tipo de bien exportado. · props: `{"tipo": "otra"}` · umbral: ['365 (trescientos sesenta y cinco) días corridos'] · tramo [exacta]: «El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse en los siguientes plazos a computar desde la fecha del cumplido de embarque otorgado por la Aduana: […] 365 (trescientos sesenta y cinco) días corridos para las operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE", ind…»
- **e2 Operacion** «Ingreso y liquidación de divisas — exportación EXPORTA SIMPLE» — Ingreso y liquidación en el mercado de cambios del contravalor de exportaciones de bienes concretadas en el régimen "EXPORTA SIMPLE", cualquiera sea el bien exportado. · props: `{"tipo": "ingreso y liquidación de divisas de exportación"}` · tramo [exacta]: «operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE"»
- R: e1 Obligacion —regula→ e2 Operacion

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

### Extracción (código W)

- **op1 Operacion** «Ingreso y liquidación de anticipos y financiaciones del exterior» — Ingreso y liquidación en el mercado de cambios de anticipos, prefinanciaciones y posfinanciaciones del exterior de exportaciones de bienes · props: `{"tipo": "ingreso y liquidación de divisas"}` · tramo [exacta]: «Los anticipos, prefinanciaciones y posfinanciaciones del exterior deberán ser ingresadas y liquidadas en el mercado de cambios»
- **ob1 Obligacion** «Plazo 20 días hábiles — ingreso y liquidación de anticipos» — Los anticipos, prefinanciaciones y posfinanciaciones del exterior deben ingresarse y liquidarse en el mercado de cambios dentro de los 20 días hábiles de la fecha de cobro o desembolso en el exterior. · props: `{"tipo": "otra"}` · umbral: ['dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el e…'] · tramo [exacta]: «Los anticipos, prefinanciaciones y posfinanciaciones del exterior deberán ser ingresadas y liquidadas en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el exterior.»
- **ex1 Excepcion** «VPU RIGI con beneficios art. 198 — régimen 14.1.4» — Si el cliente es un VPU adherido al RIGI que declaró prever usar los beneficios del art. 198 de la Ley 27.742 en cobro de exportaciones, en lugar del plazo de 20 días hábiles rige lo dispuesto en el punto 14.1.4. · tramo [exacta]: «En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servici…»
- **c1 Condicion** «Declaración ante Autoridad de Aplicación de uso art. 198» — Que el VPU haya declarado ante la Autoridad de Aplicación que preveía usar los beneficios del art. 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicios. · tramo [exacta]: «que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742»
- **com1 Comunicacion** «Ley 27.742» —  · props: `{"codigo": "Ley 27.742", "tipo": "externa"}` · tramo [exacta]: «Ley 27.742»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ex1 Excepcion —exceptua_obligacion→ ob1 Obligacion
- R: c1 Condicion —condicion_de→ ex1 Excepcion
- R: ex1 Excepcion —aplica_a→ Sujeto_vpu_rigi (mención «Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI)»)
- R: to TextoOrdenado —referencia→ com1 Comunicacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:9 | sí (remisión pura) | «resultará aplicable lo dispuesto en el punto 14.1.4» | `extraida_tramo_verificado` |  | ex1 Excepcion [exacta], tramo que contiene la remisión |

## `ext::7.2.2` — Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación.

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.2. Liquidaciones y otros ingresos imputables al cumplimiento de un permiso de embarque.
> *propio:* 7.2.2. Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación. Cuando los exportadores anticipen fondos desde sus cuentas en el exterior a los fines de dar cumplimiento a la obligación de liquidación de exportaciones realizadas y pendientes de cobro.

### Extracción (código W)

- **e1 Operacion** «Ingreso de fondos propios de exportadores imputable» — Ingreso de fondos propios de los exportadores, desde sus cuentas en el exterior, imputable al cumplimiento de la obligación de liquidación de exportaciones de bienes realizadas y pendientes de cobro (permiso de embarque). · props: `{"tipo": "ingreso de fondos del exterior"}` · tramo [exacta]: «Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación.»
- **e2 Condicion** «Anticipo desde cuentas propias en el exterior» — Supuesto: que los exportadores anticipen fondos desde sus cuentas en el exterior con el fin de cumplir la obligación de liquidación de exportaciones ya realizadas y pendientes de cobro. · tramo [exacta]: «Cuando los exportadores anticipen fondos desde sus cuentas en el exterior a los fines de dar cumplimiento a la obligación de liquidación de exportaciones realizadas y pendientes de cobro.»
- R: e2 Condicion —condicion_de→ e1 Operacion
- R: Sujeto_exportador (mención «los exportadores») —ejecuta→ e1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:15 | no | «7.2.2. Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación.» | `extraida_tramo_verificado` |  | e1 Operacion [exacta] con el mismo tramo del título |

## `ext::7.5.3` — Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.5. Ampliaciones del plazo para el ingreso y liquidación de divisas.
> *heredado:* La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias:
> *propio:* 7.5.3. Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los endeudamientos financieros referidas en los puntos 7.3.5., 7.9. y 7.11. y las prefinanciaciones de exportaciones comprendidas en el punto 7.8.5. En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento del plazo para la liquidación de divisas del permiso, el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha. Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario.

### Extracción (código W)

- **e1 Potestad** «Ampliación de plazo por fondos retenidos en cuentas» — La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación de divisas para permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a endeudamientos financieros (puntos 7.3.5., 7.9. y 7.11.) y prefinanciaciones de exportaciones (punto 7.8.5.). · tramo [exacta]: «La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias: […] Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los endeudamientos financieros referidas en los puntos 7.3.5., 7.9. y 7.11. y las prefinanciacio…»
- **e2 Potestad** «Solicitud del exportador de ampliar plazo de liquidación» — El exportador podrá solicitar que el plazo para la liquidación de divisas del permiso sea ampliado hasta el quinto día hábil posterior a la fecha hasta la cual los cobros deben permanecer depositados según el contrato del financiamiento. · tramo [exacta]: «el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha.»
- **e3 Condicion** «Fecha de depósito contractual posterior al vencimiento» — Que la fecha hasta la cual los cobros deben permanecer depositados según el contrato del financiamiento sea posterior al vencimiento del plazo de liquidación del permiso. · tramo [exacta]: «En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento del plazo para la liquidación de divisas del permiso»
- **e4 Restriccion** «Tope 125% servicios de capital e intereses — ampliación» — La ampliación está disponible hasta alcanzar el 125% de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 meses calendario. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capi…', 'el mes corriente y los siguientes 6 (seis) meses calendario'] · tramo [exacta]: «Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario.»
- **e5 Operacion** «Ampliación del plazo de liquidación por fondos retenidos» — Ampliación del plazo de ingreso y liquidación de divisas de un permiso con cobros retenidos en cuentas asociadas a financiamientos. · props: `{"tipo": "ampliación de plazo"}` · tramo [exacta]: «solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha»
- R: e1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad encargada del seguimiento del permiso»)
- R: e2 Potestad —aplica_a→ Sujeto_exportador (mención «el exportador»)
- R: e3 Condicion —condicion_de→ e2 Potestad
- R: e4 Restriccion —limita→ e5 Operacion

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

### Extracción (código W)

- **c1 Comunicacion** «Ley 26.360» —  · props: `{"codigo": "Ley 26.360", "tipo": "externa"}` · tramo [exacta]: «Ley 26.360»
- **op1 Operacion** «Opción de aplicación de cobros de exportaciones a operaciones financieras» — Ejercicio por los exportadores de la opción prevista en el punto 7.9 de aplicar cobros de exportaciones de bienes a operaciones financieras habilitadas · props: `{"tipo": "aplicación de cobros de exportaciones"}` · tramo [exacta]: «operaciones para las cuales los exportadores hagan ejercicio de la opción prevista en el presente punto»
- **o1 Obligacion** «Remitir certificación de encuadre a Exterior y Cambios» — La entidad financiera designada debe remitir por nota a la Gerencia Principal de Exterior y Cambios, dentro de los 90 días corridos posteriores al primer ingreso de fondos, la certificación de que se cumplen las condiciones que permiten encuadrar la operación. · props: `{"tipo": "reporte_al_supervisor"}` · umbral: ['dentro de los 90 (noventa) días corridos posteriores al primer ingreso de fondos'] · tramo [exacta]: «la entidad financiera designada deberá remitir, por nota dirigida a la Gerencia Principal de Exterior y Cambios dentro de los 90 (noventa) días corridos posteriores al primer ingreso de fondos, la correspondiente certificación de que se cumplen las condiciones que permiten encuadrar la operación»
- **o2 Obligacion** «Contenido mínimo de la certificación de encuadre» — La certificación presentada al BCRA debe contener como mínimo el punto normativo de encuadre, el número de identificación en el Seguimiento de anticipos y otras financiaciones de exportación de bienes (APX si hubo liquidación en el mercado; ECO si son refinanciaciones sin liquidación) y, si hay cuentas de garantía o específicas, tipo de cuenta y entidad financiera local o del exterior. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «La certificación que se presente en el BCRA deberá contener como mínimo, el detalle del punto normativo en que encuadra la operación»
- **cd1 Condicion** «Existencia de cuentas de garantía o específicas» — Si existen endeudamientos que contemplen cuentas de garantía o cuentas específicas sin estar en garantía, se debe identificar el tipo de cuenta y la entidad. · tramo [exacta]: «si existen endeudamientos que contemplen el mantenimiento de cuentas de garantías o cuentas específicas sin estar en garantía»
- **o3 Obligacion** «Certificación de elegibilidad del proyecto 7.9.2» — Para operaciones de financiación de proyectos del punto 7.9.2, la entidad debe remitir además la certificación de cumplimiento de condiciones de elegibilidad, con como mínimo descripción del proyecto, monto proyectado a invertir y composición del financiamiento. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «la entidad deberá adicionalmente remitir la certificación del cumplimiento de las condiciones para la elegibilidad del proyecto»
- **cd2 Condicion** «Operaciones de financiación de proyectos 7.9.2» — Operaciones destinadas a la financiación de proyectos comprendidos en el punto 7.9.2. · tramo [exacta]: «En el caso de que se trate de operaciones destinadas a la financiación de proyectos comprendidos en el punto 7.9.2.»
- **o4 Obligacion** «Basar certificación en proyecciones productivas y de divisas» — La certificación de la entidad financiera debe basarse en proyecciones de aumento anual de producción exportable o sustitutiva de importaciones, ventas externas, proporción a cubrir con el nuevo proyecto, flujos de divisas esperados y afectados al servicio del financiamiento. · props: `{"tipo": "otra"}` · tramo [exacta]: «La certificación que emita la entidad financiera deberá basarse en las proyecciones»
- **o5 Obligacion** «Solicitar dictámenes profesionales económico-financieros» — La entidad solicitará los dictámenes profesionales que estime necesarios para asegurar la razonabilidad y genuinidad económica y financiera de la operación. · props: `{"tipo": "otra"}` · tramo [exacta]: «La entidad solicitará los dictámenes profesionales que estime necesarios para asegurar la razonabilidad y genuinidad de la operación»
- **o6 Obligacion** «Complementar con dictámenes técnicos del proyecto» — Los dictámenes deben complementarse con dictámenes sobre aspectos técnicos del proyecto cuando éste no cuente con aprobación en términos de la Ley 26.360. · props: `{"tipo": "otra"}` · tramo [exacta]: «deberán ser complementados con dictámenes sobre los aspectos técnicos del proyecto»
- **cd3 Condicion** «Proyecto sin aprobación Ley 26.360» — El proyecto no cuenta con la aprobación en los términos de la Ley 26.360. · tramo [exacta]: «cuando el mismo no cuente con la aprobación en los términos de la Ley 26.360»
- **o7 Obligacion** «Archivar documentación de respaldo a disposición BCRA» — La documentación y hojas de trabajo que avalan la emisión de la certificación deben quedar archivadas en la entidad a disposición del BCRA. · props: `{"tipo": "otra"}` · tramo [exacta]: «deberá quedar archivada en la entidad a disposición del BCRA»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: Sujeto_exportador (mención «los exportadores») —ejecuta→ op1 Operacion
- R: op1 Operacion —requiere→ o1 Obligacion
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera designada»)
- R: cd1 Condicion —condicion_de→ o2 Obligacion
- R: o3 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: cd2 Condicion —condicion_de→ o3 Obligacion
- R: o4 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: o5 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: o6 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: cd3 Condicion —condicion_de→ o6 Obligacion
- R: o7 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «endeudamientos con cuentas de garantía» | `condicion_con_relacion` |  | cd1 Condicion «Existencia de cuentas de garantía o específicas» —condicion_de→ o2 Obligacion |
| 2 | «proyectos del 7.9.2» | `condicion_con_relacion` |  | cd2 Condicion —condicion_de→ o3 Obligacion |
| 3 | «proyecto sin aprobación de la Ley 26.360» | `condicion_con_relacion` |  | cd3 Condicion —condicion_de→ o6 Obligacion |

## `ext::8.4.2` — Determinación del plazo para el ingreso y liquidación de las divisas.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
> *heredado:* 8.4. Responsabilidades de la entidad nominada para el seguimiento del permiso.
> *propio:* 8.4.2. Determinación del plazo para el ingreso y liquidación de las divisas. La entidad deberá determinar el plazo aplicable a cada exportación a partir de lo dispuesto en el punto 7.1.1. En el caso de que una exportación esté compuesta por distintos productos, el plazo aplicable será aquel que representa una mayor proporción del valor FOB total de la exportación. La fecha de vencimiento que le corresponde a una exportación será aquella resultante de sumar el plazo aplicable a la fecha de cumplido de embarque otorgada por la Aduana. Si la fecha resultante fuese un día no hábil, el vencimiento se trasladará al primer día hábil siguiente. En caso de que exista una ampliación del plazo para un producto, el nuevo plazo se aplicará tanto a las exportaciones embarcadas a partir de la vigencia de la ampliación como a las embarcadas previamente cuyo plazo para ingresar y liquidar no se encontrase vencido a ese momento. En tanto en caso de existir una reducción del plazo vigente, el plazo reducido sólo regirá para las operaciones que se oficialicen a partir de la vigencia del nuevo plazo.

### Extracción (código W)

- **op1 Operacion** «Ingreso y liquidación de divisas por exportación» — Ingreso y liquidación en el mercado de cambios de las divisas de exportaciones de bienes, objeto de seguimiento por la entidad nominada · props: `{"tipo": "ingreso y liquidación de divisas"}` · tramo [exacta]: «Determinación del plazo para el ingreso y liquidación de las divisas.»
- **e1 Obligacion** «Determinar plazo aplicable a cada exportación» — La entidad nominada para el seguimiento del permiso deberá determinar el plazo aplicable a cada exportación según lo dispuesto en el punto 7.1.1. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La entidad deberá determinar el plazo aplicable a cada exportación a partir de lo dispuesto en el punto 7.1.1.»
- **e2 Obligacion** «Plazo por producto de mayor proporción FOB» — Si la exportación está compuesta por distintos productos, el plazo aplicable es el del producto que representa la mayor proporción del valor FOB total de la exportación. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el plazo aplicable será aquel que representa una mayor proporción del valor FOB total de la exportación»
- **c1 Condicion** «Exportación compuesta por distintos productos» — Que la exportación esté compuesta por distintos productos. · tramo [exacta]: «En el caso de que una exportación esté compuesta por distintos productos»
- **e3 Obligacion** «Fecha de vencimiento: embarque más plazo» — La fecha de vencimiento de una exportación resulta de sumar el plazo aplicable a la fecha de cumplido de embarque otorgada por la Aduana. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La fecha de vencimiento que le corresponde a una exportación será aquella resultante de sumar el plazo aplicable a la fecha de cumplido de embarque otorgada por la Aduana.»
- **e4 Obligacion** «Traslado del vencimiento al día hábil siguiente» — Si la fecha de vencimiento resultante es un día no hábil, el vencimiento se traslada al primer día hábil siguiente. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el vencimiento se trasladará al primer día hábil siguiente»
- **c2 Condicion** «Fecha resultante en día no hábil» — Que la fecha de vencimiento resultante sea un día no hábil. · tramo [exacta]: «Si la fecha resultante fuese un día no hábil»
- **e5 Obligacion** «Ampliación de plazo: aplica a embarques no vencidos» — Ante una ampliación del plazo para un producto, el nuevo plazo se aplica a las exportaciones embarcadas desde la vigencia de la ampliación y a las embarcadas previamente cuyo plazo para ingresar y liquidar no estuviera vencido a ese momento. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el nuevo plazo se aplicará tanto a las exportaciones embarcadas a partir de la vigencia de la ampliación como a las embarcadas previamente cuyo plazo para ingresar y liquidar no se encontrase vencido a ese momento»
- **c3 Condicion** «Ampliación del plazo para un producto» — Que exista una ampliación del plazo para un producto. · tramo [exacta]: «En caso de que exista una ampliación del plazo para un producto»
- **e6 Obligacion** «Reducción de plazo: solo operaciones posteriores» — Ante una reducción del plazo vigente, el plazo reducido sólo rige para las operaciones que se oficialicen a partir de la vigencia del nuevo plazo. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el plazo reducido sólo regirá para las operaciones que se oficialicen a partir de la vigencia del nuevo plazo»
- **c4 Condicion** «Reducción del plazo vigente» — Que exista una reducción del plazo vigente. · tramo [exacta]: «en caso de existir una reducción del plazo vigente»
- R: e1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: e1 Obligacion —regula→ op1 Operacion
- R: e2 Obligacion —regula→ op1 Operacion
- R: e3 Obligacion —regula→ op1 Operacion
- R: e4 Obligacion —regula→ op1 Operacion
- R: e5 Obligacion —regula→ op1 Operacion
- R: e6 Obligacion —regula→ op1 Operacion
- R: c1 Condicion —condicion_de→ e2 Obligacion
- R: c2 Condicion —condicion_de→ e4 Obligacion
- R: c3 Condicion —condicion_de→ e5 Obligacion
- R: c4 Condicion —condicion_de→ e6 Obligacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «exportación de varios productos» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ e2 Obligacion |
| 2 | «fecha no hábil» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ e4 Obligacion |
| 3 | «ampliación del plazo» | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ e5 Obligacion |
| 4 | «reducción del plazo» | `condicion_con_relacion` |  | c4 Condicion —condicion_de→ e6 Obligacion |

## `ext::8.5.18.1` — La documentación permite constatar que la entrega de la mercadería

Grupos: omisiones.

### Texto

> *heredado:* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
> *heredado:* 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
> *heredado:* La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque cuando cuente con los elementos que le permitan considerar que la operación se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las condiciones previstas en cada caso. La documentación utilizada para certificar el concepto y monto de las divisas imputado en cada caso deberá quedar archivada en la entidad a disposición del BCRA.
> *heredado:* 8.5.18. Cobros locales por exportaciones del régimen de ranchos a medios de transporte de
> *heredado:* bandera extranjera. La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque por el valor equivalente a los montos abonados localmente en pesos y/o en moneda extranjera al exportador por un agente local de la empresa propietaria de los medios de transporte de bandera extranjera, en la medida que se verifiquen las siguientes condiciones:
> *propio:* 8.5.18.1. La documentación permite constatar que la entrega de la mercadería exportada se ha producido en el país, que el agente local de la empresa propietaria de los medios de transporte de bandera extranjera ha realizado localmente el pago al exportador y la moneda en la que dicho pago se efectuó.

### Extracción (código W)

- **c1 Condicion** «Entrega en el país documentada — ranchos» — Condición para dar por cumplido el seguimiento del permiso de embarque por cobros locales de exportaciones del régimen de ranchos a medios de transporte de bandera extranjera: la documentación tiene que permitir constatar que la mercadería exportada se entregó en el país. · tramo [exacta]: «La documentación permite constatar que la entrega de la mercadería exportada se ha producido en el país»
- **c2 Condicion** «Pago local del agente documentado — ranchos» — Condición para dar por cumplido el seguimiento del permiso de embarque (régimen de ranchos): la documentación tiene que permitir constatar que el agente local de la empresa propietaria de los medios de transporte de bandera extranjera le pagó localmente al exportador. · tramo [exacta]: «que el agente local de la empresa propietaria de los medios de transporte de bandera extranjera ha realizado localmente el pago al exportador»
- **c3 Condicion** «Moneda del pago documentada — ranchos» — Condición para dar por cumplido el seguimiento del permiso de embarque (régimen de ranchos): la documentación tiene que permitir constatar en qué moneda se hizo el pago local al exportador. · tramo [exacta]: «la moneda en la que dicho pago se efectuó»

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

### Extracción (código W)

- **c1 Comunicacion** «Decreto 929/13» —  · props: `{"codigo": "Decreto 929/13", "tipo": "externa"}` · tramo [exacta]: «Decreto 929/13»
- **c2 Comunicacion** «Resolución 26/23 Secretaría de Energía» —  · props: `{"codigo": "Resolución 26/23 de la Secretaría de Energía", "tipo": "externa"}` · tramo [exacta]: «Resolución 26/23 de la Secretaría de Energía»
- **p1 Potestad** «Cumplido seguimiento por Certificado Decreto 929/13» — A pedido del cliente, la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte amparada por un "Certificado DECRETO 929/13" emitido a partir de la Resolución 26/23 de la Secretaría de Energía. · tramo [exacta]: «la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso que se encuentre amparado por un "Certificado DECRETO 929/13"»
- **k1 Condicion** «Pedido de cliente con proyecto Decreto 929/13» — Que lo pida un cliente con proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13). · tramo [exacta]: «A pedido de un cliente que posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos establecido por el Decreto 929/13»
- **k2 Condicion** «Certificado emitido según Resolución 26/23» — Solo por la parte del permiso amparada por un Certificado DECRETO 929/13 emitido conforme la Resolución 26/23 de la Secretaría de Energía. · tramo [exacta]: «amparado por un "Certificado DECRETO 929/13" emitido a partir de lo dispuesto por la Resolución 26/23 de la Secretaría de Energía»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: to TextoOrdenado —referencia→ c2 Comunicacion
- R: k1 Condicion —condicion_de→ p1 Potestad
- R: k2 Condicion —condicion_de→ p1 Potestad
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)

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

### Extracción (código W)

- **e1 Operacion** «Préstamos financieros atendidos con exportaciones — seguimiento» — Operación comprendida en el seguimiento de anticipos y otras financiaciones de exportación de bienes: préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones, y para los cuales el exportador solicite su aplicación a permisos de embarque oficializados a partir del 02/09… · props: `{"tipo": "préstamo financiero de exportación"}` · tramo [exacta]: «Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones»
- **c1 Condicion** «Contrato vigente al 31/08/19 con atención por exportaciones» — El préstamo tiene contrato vigente al 31/08/19 y sus condiciones prevén atender los servicios aplicando en el exterior el flujo de fondos de exportaciones. · tramo [exacta]: «con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones»
- **c2 Condicion** «Solicitud de aplicación a permisos desde 02/09/19» — El exportador solicita aplicar el préstamo a permisos de embarque oficializados a partir del 02/09/19. · tramo [exacta]: «el exportador solicite su aplicación a permisos de embarque oficializados a partir del 02/09/19»
- R: c1 Condicion —condicion_de→ e1 Operacion
- R: c2 Condicion —condicion_de→ e1 Operacion
- R: Sujeto_exportador (mención «el exportador») —ejecuta→ e1 Operacion

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

### Extracción (código W)

- **c1 Condicion** «Pasivo en pesos con el exterior verificado» — Supuesto de la potestad de la entidad de emitir la certificación de aplicación por repatriaciones de aportes de inversión directa de no residentes (punto 9.3.10): debe contar con documentación que permita verificar el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital, según corresponda. · tramo [exacta]: «el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda»
- **c2 Condicion** «Pasivo declarado en Relevamiento de activos y pasivos externos» — Supuesto de la potestad de emitir la certificación de aplicación del punto 9.3.10: el pasivo se encuentra declarado en la última presentación vencida del "Relevamiento de activos y pasivos externos", en caso de corresponder. · tramo [exacta]: «Se encuentra declarado en la última presentación vencida del "Relevamiento de activos y pasivos externos", en caso de corresponder»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:13 | no | «en caso de corresponder» | `extraida_tramo_verificado` |  | c2 Condicion [exacta], tramo que contiene «en caso de corresponder» |

## `ext::9.3.12::intro` — [bloque intro] Utilidades y dividendos en el marco de lo previsto en el punto 7.10.

Grupos: omisiones.

### Texto

> *heredado:* Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.
> *heredado:* 9.3. Certificaciones de aplicación de cobros de exportaciones.
> *heredado:* 9.3.12. Utilidades y dividendos en el marco de lo previsto en el punto 7.10.
> *propio:* La entidad podrá emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes, en la medida que se cumplan la totalidad de las siguientes condiciones:

### Extracción (código W)

- **e1 Potestad** «Certificación de aplicación a utilidades y dividendos» — La entidad podrá emitir las certificaciones de aplicación de las divisas (de cobros de exportaciones) al pago de utilidades y dividendos a accionistas no residentes, en la medida que se cumplan la totalidad de las condiciones que se enumeran a continuación. · tramo [exacta]: «La entidad podrá emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes»
- **e2 Operacion** «Emisión de certificación de aplicación de divisas a utilidades y dividendos» — Emisión de certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes · props: `{"tipo": "certificación de aplicación de cobros de exportaciones"}` · tramo [exacta]: «emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes»
- R: e1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ e2 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «La entidad podrá emitir las certificaciones» — Vínculo Potestad → Operacion habilitada; ningún predicado lo representa (habilita).

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

### Extracción (código W)

- **op1 Operacion** «Certificación de aplicación — títulos de deuda en moneda extranjera» — Emisión de certificaciones de aplicación de divisas de exportación a la cancelación de títulos de deuda con registro público en el país denominados en moneda extranjera admitidos en el punto 7.9, a partir del vencimiento del capital, intereses y otros conceptos admitidos · props: `{"tipo": "certificación de aplicación de cobros de exportaciones"}` · tramo [exacta]: «La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación a partir del vencimiento del capital, intereses y otros conceptos admitidos»
- **p1 Potestad** «Facultad de certificar aplicación a títulos de deuda» — La entidad podrá emitir certificaciones de aplicación de las divisas a la cancelación de títulos de deuda con registro público en el país en moneda extranjera (punto 7.9) a partir del vencimiento del capital, intereses y otros conceptos admitidos · tramo [exacta]: «La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación a partir del vencimiento del capital, intereses y otros conceptos admitidos»
- **c1 Condicion** «Condiciones del punto 9.3.1 verificadas» — Que la entidad verifique las condiciones indicadas en el punto 9.3.1. · tramo [exacta]: «en la medida que verifique las condiciones indicadas en el punto 9.3.1.»
- **c2 Condicion** «Cancelación a partir del vencimiento constatada» — Que la entidad constate que la cancelación tuvo lugar a partir de la fecha de vencimiento · tramo [exacta]: «constate que la cancelación tuvo lugar a partir de la fecha de vencimiento»
- **c3 Condicion** «Documentación de requisitos del punto 7.9» — Que la entidad cuente con la documentación que verifica el cumplimiento de los requisitos del punto 7.9 · tramo [exacta]: «cuente con la documentación que verifican el cumplimiento de los requisitos establecidos en el punto 7.9.»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion
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

### Extracción (código W)

- **e1 Obligacion** «Prevención de conflictos de intereses — Directorio» — Recomendación (buena práctica, no deber): el Directorio se asegurará de que la Alta Gerencia implemente procedimientos que prevengan y/o limiten conflictos de intereses entre la entidad financiera, el Directorio, la Alta Gerencia y el grupo económico al que pertenece la entidad, por afectar negativamente la calidad del gobierno societario. · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "se considera como bue-\nna práctica", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «Se asegurará de que la Alta Gerencia implemente procedimientos […] Conflictos de intereses entre la entidad financiera, el Directorio, la Alta Gerencia»
- R: e1 Obligacion —aplica_a→ Sujeto_directorio (mención «el Directorio»)

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

### Extracción (código W)

- **e1 Obligacion** «Uso efectivo del trabajo de auditorías — Alta Gerencia» — Recomendación (buena práctica, no deber): la Alta Gerencia es responsable de utilizar efectivamente el trabajo llevado a cabo por las auditorías interna y externa y las funciones relacionadas con el sistema de control interno, conforme a lo establecido en la Sección 5. · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "como una buena práctica", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «La Alta Gerencia, como una buena práctica, será responsable de: […] Utilizar efectivamente el trabajo llevado a cabo por las auditorías interna y externa y las funciones relacionadas con el sistema de control interno, conforme a lo establecido en la Sección 5.»
- R: e1 Obligacion —aplica_a→ Sujeto_alta_gerencia (mención «La Alta Gerencia»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:29 | sí (remisión pura) | «conforme a lo establecido en la Sección 5» | `extraida_tramo_verificado` |  | e1 Obligacion [exacta], tramo que contiene la remisión |

## `lingob::3.2::intro` — [bloque intro] Decisiones gerenciales.

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Alta Gerencia.
> *heredado:* 3.2. Decisiones gerenciales.
> *propio:* Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona. Es recomendable que la Alta Gerencia:

### Extracción (código W)

- **e1 Operacion** «Adopción de principales decisiones gerenciales» — Adopción de las principales decisiones gerenciales de la entidad · props: `{"tipo": "decisión gerencial"}` · tramo [exacta]: «Las principales decisiones gerenciales»
- **e2 Obligacion** «Más de una persona — decisiones gerenciales principales» — Recomendación de buena práctica, no un deber: las principales decisiones gerenciales serán adoptadas por más de una persona. · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "en orden a las buenas prácticas", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona.»
- R: e2 Obligacion —regula→ e1 Operacion
- R: e2 Obligacion —aplica_a→ Sujeto_alta_gerencia (mención «Alta Gerencia»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:14 | sí | «en orden a las buenas prácticas» | `extraida_tramo_verificado` |  | e2 Obligacion [exacta], tramo que contiene «en orden a las buenas prácticas» |

## `lingob::4.2.1` — Comité de gestión de riesgos, que realizará un seguimiento de las actividades de la Alta

Grupos: omisiones.

### Texto

> *heredado:* Sección 4. Comités.
> *heredado:* 4.2. Otros comités.
> *heredado:* De acuerdo con las dimensiones, complejidad, importancia económica y perfil de riesgo que presente la entidad financiera y el grupo económico de que se trate, se recomienda el establecimiento de otros comités especializados, con una clara definición y divulgación de sus mandatos, composición (incluidos los miembros considerados independientes) y procedimientos de trabajo. Entre otros comités, se pueden mencionar los siguientes:
> *heredado:* Tanto los directores independientes como aquellos que no reúnan esa condición, pero posean conocimientos y aptitudes relevantes, deberían tener un rol clave en tales comités. A los efectos de maximizar la objetividad, es conveniente que la mayoría de los miembros revistan la condición de independiente, contemplando en su caso las situaciones previstas en el primer párrafo de este punto y la naturaleza específica de la entidad. Los citados comités no son excluyentes de otros que se puedan exigir de manera específica por normas del Banco Central de la República Argentina.
> *propio:* 4.2.1. Comité de gestión de riesgos, que realizará un seguimiento de las actividades de la Alta Gerencia relacionadas con la gestión de los riesgos de crédito, de mercado, de liquidez y/o de activos y pasivos, operacional, de cumplimiento y de reputación, entre otros. Asimismo, asesorará al Directorio sobre los riesgos de la entidad.

### Extracción (código W)

- **e1 Obligacion** «Comité de gestión de riesgos — establecimiento recomendado» — Recomendación (no deber): según dimensiones, complejidad, importancia económica y perfil de riesgo de la entidad financiera y su grupo económico, se recomienda establecer, entre otros comités especializados, un Comité de gestión de riesgos, con clara definición y divulgación de mandato, composición y procedimientos, que realice el seguimiento de las actividades de la Alta Gerencia relacionadas con… · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "se recomienda", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «se recomienda el establecimiento de otros comités especializados, con una clara definición y divulgación de sus mandatos, composición (incluidos los miembros considerados independientes) y procedimientos de trabajo. Entre otros comités, se pueden mencionar los siguientes: […] Comité de gestión de riesgos, que realizará…»
- **c1 Condicion** «Según dimensiones, complejidad y perfil de riesgo» — El establecimiento del comité se recomienda de acuerdo con las dimensiones, complejidad, importancia económica y perfil de riesgo de la entidad financiera y su grupo económico. · tramo [exacta]: «De acuerdo con las dimensiones, complejidad, importancia económica y perfil de riesgo que presente la entidad financiera y el grupo económico de que se trate»
- R: c1 Condicion —condicion_de→ e1 Obligacion
- R: e1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)

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

### Extracción (código W)

- **e1 Obligacion** «Comité de incentivos al personal — recomendación» — Recomendación (no deber): según dimensiones, complejidad, importancia económica y perfil de riesgo de la entidad financiera y su grupo económico, se recomienda establecer, entre otros comités especializados, un Comité de incentivos al personal, con clara definición y divulgación de mandato, composición y procedimientos, encargado de vigilar que el sistema de incentivos económicos al personal sea c… · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "se recomienda", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «se recomienda el establecimiento de otros comités especializados […] Comité de incentivos al personal, encargado de vigilar que el sistema de incentivos económicos al personal sea consistente con la cultura, los objetivos, los negocios a largo plazo, la estrategia y el entorno de control de la entidad»
- R: e1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:21 | sí | «se recomienda el establecimiento de otros comités especializados» | `extraida_tramo_verificado` |  | e1 Obligacion [exacta], tramo que contiene la frase |

## `lingob::7.1.1` — Estructura del Directorio (conformación según el estatuto, tamaño, miembros, proceso

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Otras políticas organizacionales.
> *heredado:* 7.1. Política de transparencia.
> *heredado:* A los fines de que la entidad financiera sea dirigida con transparencia, es recomendable una apropiada divulgación de la información hacia el depositante, inversor, accionista y público en general que promueva la disciplina de mercado y, por ende, un buen gobierno societario. El objetivo de la política de transparencia en el gobierno societario es proveer a las citadas partes de la información necesaria para que evalúen la efectividad en la gestión del Directorio y de la Alta Gerencia. La publicación de informes sobre los aspectos del gobierno societario puede asistir a los participantes del mercado y a otras partes interesadas en el monitoreo de la fortaleza y solvencia de la entidad. Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la siguiente información, en función del tamaño, complejidad y estructura propietaria, importancia económica y perfil de riesgo de la entidad, dependiendo también de si la entidad cotiza o no en bolsas:
> *propio:* 7.1.1. Estructura del Directorio (conformación según el estatuto, tamaño, miembros, proceso de selección, calificaciones, criterios de independencia y paridad de género, intereses particulares en transacciones o asuntos que afecten a la entidad financiera) y de la Alta Gerencia (responsabilidades, líneas de reportes, calificaciones y experiencia) y miembros de los comités (misión, objetivos y responsabilidades).

### Extracción (código W)

- **e1 Obligacion** «Divulgar estructura del Directorio, Alta Gerencia y comités» — Recomendación (no deber): es deseable que las entidades financieras incluyan en sus sitios públicos (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda y en función de su tamaño, complejidad, estructura propietaria, importancia económica, perfil de riesgo y cotización en bolsas, la estructura del Directorio (conformación según el estat… · props: `{"tipo": "presentacion_informativa"}` · no definidas: `{"modalidad": "Es deseable", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la siguiente información […] Estructura del Directorio (conformación según el estatuto, tamaño, miembros, proceso de selección, cali…»
- R: e1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)

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

### Extracción (código W)

- **e1 Obligacion** «Política según naturaleza jurídica — divulgación entidades públicas» — Recomendación (no deber): es deseable que las entidades financieras públicas incluyan en sus sitios públicos (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la definición de la política en función de su naturaleza jurídica conforme su carta orgánica y/o estatutos, en función del tamaño, complejidad, estructura propietaria, importa… · props: `{"tipo": "presentacion_informativa"}` · no definidas: `{"modalidad": "Es deseable", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la siguiente información […] En las entidades financieras públicas, la definición de la política en función de su naturaleza jurídic…»
- R: e1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras públicas»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:22 | sí | «Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información pe…» | `extraida_tramo_verificado` |  | e1 Obligacion [exacta], tramo de dos segmentos que cubre el comienzo de la oración del heredado, no el calificador final; cobertura parcial 0,58 |

## `pagjub::2.2` — Modelo de nota de presentación de la rendición de cuentas.

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Rendición de cuentas por parte de las entidades financieras.
> *propio:* 2.2. Modelo de nota de presentación de la rendición de cuentas. Fecha: De: (1) A: BANCO CENTRAL DE LA REPÚBLICA ARGENTINA. Remitimos a Uds. para su procesamiento, en los términos de las normas sobre "Pago de beneficios de la seguridad social por cuenta de la Administración Nacional de la Seguridad Social (ANSES)" los archivos contenidos en los soportes de información que se acompañan, en los cuales se detalla el estado de la totalidad de las órdenes de pago que la ANSES nos encomendara pagar, correspondientes al período .....(2)......de la liquidación ….(3)... Emisión de ANSES: …...................(4) ............ casos por $................(5) ................, Órdenes de Pago pagadas: .............(6) …........ casos por $................(7) .................. Órdenes de Pago impagas: .............(8) ............ casos por $................(9) .................. Certificamos que los datos señalados precedentemente son ciertos y resumen la información detallada en los archivos contenidos en los soportes que se acompañan. Identificación de los archivos Responsables: Firma Firma Nombres y apellidos Nombres y apellidos Tipo y N° doc. de identidad (10) Tipo y N° doc. de identidad (10) Tel. Tel. ................. RECIBIDO ------------------------------------------------------------------------------------------------------------------ Referencias: (1)Código de la entidad financiera. (2)Consignar período de pago mensual o aguinaldo, en su caso. (3)Consignar tipo de liquidación ("ANSES", cuando la rendición es de prestaciones de la Administración Nacional de la Seguridad Social y "MTESS" cuando la rendición es de prestaciones por cuenta y orden del Ministerio de Trabajo, Empleo y Seguridad Social). (4) Cantidad de órdenes de pago que se encomendó pagar a la entidad financiera durante el período de pago correspondiente. (5)Importe en pesos del total puesto al pago. (6)Cantidad de órdenes de pago pagadas. (7)Importe en pesos del total pagado. (8)Cantidad de órdenes de pago impagas. (9)Importe en pesos del total impago. (10)Conforme a lo previsto en las normas sobre "Documentos de identificación en vigencia".

### Extracción (código W)

- **op1 Operacion** «Presentación nota de rendición de cuentas al BCRA» — Remisión al BCRA de la nota de presentación de la rendición de cuentas con los soportes de información que detallan el estado de la totalidad de las órdenes de pago encomendadas por la ANSES para un período y liquidación · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Modelo de nota de presentación de la rendición de cuentas.»
- **o1 Obligacion** «Detalle de órdenes emitidas, pagadas e impagas — nota» — Consignar en la nota el código de la entidad, el período de pago (mensual o aguinaldo), el tipo de liquidación (ANSES o MTESS) y la cantidad e importe en pesos de las órdenes de pago emitidas, pagadas e impagas · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «Emisión de ANSES: …...................(4) ............ casos por $................(5) ................,»
- **o2 Obligacion** «Certificación de veracidad de datos — nota» — Certificar, con firma de responsables identificados, que los datos de la nota son ciertos y resumen la información de los archivos acompañados · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «Certificamos que los datos señalados precedentemente son ciertos y resumen la información detallada en los archivos contenidos en los soportes que se acompañan.»
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: o2 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: Sujeto_entidad_financiera (mención «las entidades financieras») —ejecuta→ op1 Operacion
- Omisión `tabla` [exacta]: «Responsables: Firma Firma» — Campos del formulario modelo (firmas, identificación, recibido) con disposición tabular; no se reconstruye su estructura.

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:16 | no | «Órdenes de Pago pagadas: .............(6) …........ casos por $................(7) ..................» | `ausente` |  | ninguna entidad; om#0 tabla refiere a los campos de firmas |

## `pagjub::2.8.4.3` — Debitar de la cuenta corriente de la entidad participante el importe de las órdenes

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Rendición de cuentas por parte de las entidades financieras.
> *heredado:* 2.8. Liquidación de la rendición de cuentas.
> *heredado:* El procesamiento de la información de la rendición de cuentas dará lugar a diferentes movimientos de fondos los que, según los casos correspondientes, se describen a continuación:
> *heredado:* 2.8.4. Presentación aceptada durante el período de presentación tardía con inconsistencias.
> *heredado:* El BCRA, en el mismo día de la aceptación, procederá a:
> *propio:* 2.8.4.3. Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditando el mismo en una cuenta transitoria del BCRA, hasta la fecha límite.

### Extracción (código W)

- **e1 Obligacion** «Débito de órdenes con inconsistencias a transitoria» — En presentación aceptada durante el período de presentación tardía con inconsistencias, el BCRA, en el mismo día de la aceptación, debe debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditándolo en una cuenta transitoria del BCRA hasta la fecha límite. · props: `{"tipo": "otra"}` · tramo [exacta]: «El BCRA, en el mismo día de la aceptación, procederá a: […] Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditando el mismo en una cuenta transitoria del BCRA, hasta la fecha límite.»
- **e2 Operacion** «Débito en cuenta corriente de entidad participante» — Débito del importe de órdenes de pago abonadas e impagas con inconsistencias en la cuenta corriente de la entidad participante y acreditación en cuenta transitoria del BCRA hasta la fecha límite · props: `{"tipo": "debito en cuenta corriente"}` · tramo [exacta]: «Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias»
- R: e1 Obligacion —aplica_a→ Sujeto_bcra (mención «El BCRA»)
- R: e1 Obligacion —regula→ e2 Operacion
- R: Sujeto_bcra (mención «El BCRA») —ejecuta→ e2 Operacion

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

### Extracción (código W)

- **e1 Operacion** «Otorgamiento de financiaciones UVI a personas humanas» — Otorgamiento de financiaciones de Unidades de Vivienda actualizables por ICC - Ley 27.271 (UVI) a personas humanas · props: `{"tipo": "financiación"}` · tramo [exacta]: «Al momento del otorgamiento de financiaciones a personas humanas»
- **e2 Obligacion** «Atención relación cuota/ingreso — financiaciones UVI» — Las operaciones de financiación UVI están sujetas a la condición de que, al otorgar financiaciones a personas humanas, se tenga especial atención a la relación cuota/ingreso, de manera que el deudor pueda afrontar posibles incrementos en el importe de las cuotas sin afectar su capacidad de pago, teniendo en cuenta que sus ingresos pueden no seguir la evolución de la UVI ni la del CVS. · props: `{"tipo": "otra"}` · tramo [exacta]: «estarán sujetas a las siguientes condiciones […] Al momento del otorgamiento de financiaciones a personas humanas, se deberá tener especial atención a la relación cuota/ingreso»
- R: e2 Obligacion —regula→ e1 Operacion

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

### Extracción (código W)

- **c1 Condicion** «Financiaciones en pesos > $30.000 millones — Gran empresa exportadora» — Condición (concurrente con las demás del punto 7.1) para que un cliente del sector privado no financiero quede comprendido en la categoría "Grandes empresas exportadoras": mantener un total de financiaciones alcanzadas en pesos en el conjunto del sistema financiero superior a $ 30.000 millones (alternativa y/o con pases o cauciones tomadas en pesos en los últimos 90 días). · umbral: ['que supere el monto de $ 30.000 millones'] · tramo [exacta]: «Mantengan un importe total de financiaciones alcanzadas en pesos en el conjunto del sistema financiero que supere el monto de $ 30.000 millones»
- **c2 Condicion** «Pases/cauciones tomadas en pesos últimos 90 días — Gran empresa exportadora» — Condición alternativa (y/o) a la anterior para integrar la categoría "Grandes empresas exportadoras": haber mantenido pases y/o cauciones bursátiles tomadas en pesos, cualquiera sea su importe, durante los últimos 90 días corridos. · umbral: ['durante los últimos 90 días corridos'] · tramo [exacta]: «y/o pases y/o cauciones bursátiles tomadas –en pesos– cualquiera sea su importe durante los últimos 90 días corridos»
- **d1 Definicion** «Financiaciones alcanzadas» — Aquellas que hayan implicado desembolsos de fondos, así como el importe no utilizado del límite de crédito asignado para adelantos en cuenta corriente; se computa su saldo de capital a fin del mes anterior al de su determinación. · props: `{"termino": "financiaciones alcanzadas"}` · tramo [exacta]: «Las financiaciones alcanzadas serán aquellas que hayan implicado desembolsos de fondos, así como el importe no utilizado del límite de crédito asignado para adelantos en cuenta corriente.»
- **o1 Obligacion** «Certificación de auditor/contador — cliente que niega encuadre» — El cliente que declare no encuadrarse como "Gran empresa exportadora" pese a que la Central de deudores muestre que supera $ 30.000 millones debe presentar certificación de Auditor Externo o Contador Público independiente (firma certificada por el Consejo Profesional) detallando sus financiaciones en pesos y moneda extranjera en el conjunto de las entidades financieras, desagregadas por entidad a … · props: `{"tipo": "presentacion_informativa"}` · umbral: ['durante los últimos 90 días corridos'] · tramo [exacta]: «deberá presentar una certificación extendida por Auditor Externo o Contador Público independiente»
- **c3 Condicion** «Declaración jurada de no encuadre — certificación» — Que el cliente manifieste por declaración jurada no encuadrarse en la categoría "Gran empresa exportadora". · tramo [exacta]: «Cuando un cliente manifieste por declaración jurada que no se encuadra en la categoría de "Gran empresa exportadora"»
- **c4 Condicion** «Central de deudores muestra > $30.000 millones» — Que de la Central de deudores del sistema financiero surja que el cliente supera $ 30.000 millones. · umbral: ['supera el importe de $ 30.000 millones'] · tramo [exacta]: «de la información disponible en la "Central de deudores del sistema financiero", surja que supera el importe de $ 30.000 millones»
- **x1 Excepcion** «Clientes MiPyME — sin certificación» — La obligación de presentar la certificación no aplica cuando el cliente reúna la condición de MiPyME según las normas respectivas. · tramo [exacta]: «Lo previsto en este párrafo no será de aplicación cuando el cliente reúna la condición de MiPyME»
- R: o1 Obligacion —aplica_a→ Sujeto_cliente (mención «un cliente»)
- R: x1 Excepcion —aplica_a→ Sujeto_cliente (mención «el cliente»)
- R: c3 Condicion —condicion_de→ o1 Obligacion
- R: c4 Condicion —condicion_de→ o1 Obligacion
- R: x1 Excepcion —exceptua_obligacion→ o1 Obligacion
- Omisión `fuera_de_tipos` [exacta]: «Esa certificación mantendrá vigencia durante 90 días corridos desde la fecha a la cual se refiera» — Plazo de vigencia de la certificación; no es deber, límite ni definición (posible propiedad de la Obligacion o3/Definicion).

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «financiaciones de más de $ 30.000 millones» | `sin_relacion` | norma_en_heredado | c1 Condicion con el umbral, sin relación; norma en el texto heredado |
| 2 | «pases o cauciones en 90 días» | `sin_relacion` | norma_en_heredado | c2 Condicion con el umbral, sin relación; norma en el texto heredado |
| 3 | «declaración jurada contra la Central de deudores» | `condicion_con_relacion` |  | c3 y c4 Condicion (la DDJJ y la Central de deudores, partidas) —condicion_de→ o1 Obligacion |
| 4 | «MiPyME» | `condicion_con_relacion` |  | x1 Excepcion —exceptua_obligacion→ o1 Obligacion |

## `polcre::7.1::cierre` — [bloque cierre] Clientes comprendidos.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Financiaciones a "Grandes empresas exportadoras".
> *heredado:* 7.1. Clientes comprendidos.
> *propio:* Cuando el cliente reúna la condición del punto 7.1.1. pero el importe total de sus financiaciones en pesos en el sistema financiero no supere el importe de $ 30.000 millones y no haya mantenido pases y/o cauciones bursátiles tomadas –en pesos– durante los últimos 90 días corridos, la entidad financiera podrá otorgarle nuevas financiaciones en la medida que con tales desembolsos no se supere ese importe. Cuando se trate de conjuntos económicos se los considerará como un solo cliente, a cuyo efecto será de aplicación el punto 1.2.2. de las normas sobre "Grandes exposiciones al riesgo de crédito". A los fines de la imputación de las financiaciones, será de aplicación lo previsto en las normas sobre "Grandes exposiciones al riesgo de crédito".

### Extracción (código W)

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

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «reúne 7.1.1» | `condicion_con_relacion` |  | c0 Condicion —condicion_de→ p1 Potestad |
| 2 | «no supera $ 30.000 millones» | `condicion_con_relacion` |  | c1 Condicion con el umbral —condicion_de→ p1 Potestad |
| 3 | «sin pases» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ p1 Potestad |
| 4 | «desembolsos que no superen el importe» | `condicion_con_relacion` |  | c3 Condicion con el umbral —condicion_de→ p1 Potestad |
| 5 | «conjuntos económicos» | `dentro_de_norma` |  | extraído como Definicion d1; sin Condicion |

## `pro::2.3.5.1` — Todo importe cobrado o adeudado de cualquier forma al usuario de servicios fi-

Grupos: grupo_c.

### Texto

> *heredado:* Sección 2. Derechos básicos de los usuarios de servicios financieros.
> *heredado:* 2.3. Recaudos mínimos de la relación de consumo.
> *heredado:* 2.3.5. Reintegro de importes.
> *propio:* 2.3.5.1. Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: i) tasas de interés, comisiones y/o cargos sin el cumplimiento de lo previsto en los puntos 2.3.2. a 2.3.4.; ii) cargos en exceso de los costos de los servicios que terceros les cobraron a los sujetos obligados en relación con servicios prestados a los usuarios y/o de los precios que el tercero prestador perciba de particulares en general; iii) comisiones en exceso de las máximas fijadas por el BCRA que sean de aplicación; iv) en incumplimiento al nivel de la tasa de interés máxima aplicable a financiaciones vinculadas a tarjetas de crédito previstas en el texto ordenado sobre Tasas de Interés en las Operaciones de Crédito; v) en exceso de lo oportunamente pactado entre el usuario y el sujeto obligado; vi) otros generados en forma impropia por su naturaleza, tales como intereses compensatorios por saldos deudores generados en cuentas de depósito distintas de la cuenta corriente bancaria; vii) así como los importes adeudados al usuario por haber liquidado en forma incorrecta promociones, descuentos u otro tipo de beneficios –es decir, que no se ajustan a los términos, condiciones y/o modalidades que hubieran sido ofrecidos, publicitados o convenidos–; deberá serle reintegrado dentro de: - los diez (10) días hábiles siguientes al momento de la presentación del reclamo ante el sujeto obligado, de conformidad con las previsiones del punto 3.1.6.; o - los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por el sujeto obligado o por la fiscalización que realice la SEFYC. Ello, sin perjuicio de las sanciones que pudieran corresponder. En tales situaciones, corresponderá reconocer el importe de los gastos que resulten razonables realizados para la obtención del reintegro y, en todos los casos, los intereses compensatorios pertinentes, computados desde la fecha del cobro indebido hasta la de su efectiva devolución. A ese efecto, el sujeto obligado deberá aplicar 1,5 veces la tasa promedio correspondiente al período comprendido entre el momento en que la citada diferencia hubiera sido exigible –fecha en la que se cobraron los importes objeto del reclamo– y el de su efectiva cancelación, computado a partir de la encuesta diaria de tasas de interés de depósitos a plazo fijo de 30 a 59 días –de pesos o dólares estadounidenses, según la moneda de la operación– informada por el BCRA sobre la base de la información provista por la totalidad de bancos públicos y privados. Cuando la tasa correspondiente a tal encuesta no estuviera disponible, se deberá tomar la última informada. Cuando el usuario posea en la entidad financiera obligada una cuenta a la vista que se halle abierta a su nombre, ésta deberá acreditar ese importe en dicha cuenta en forma automática sin necesidad de requerimiento expreso. Si ello no fuera posible o no se tratare de una entidad financiera, el importe del reintegro deberá ser acreditado en una tarjeta de crédito de su titularidad o detraído del saldo vigente de la financiación que lo generó. Deberá notificarse la acreditación del reintegro o, en su caso, su puesta a disposición mediante aviso efectuado a través de medios electrónicos –cajeros automáticos, banca por Internet (home banking), etc.– y/o servicios telefónicos –tales como mensajes de texto y/o voz– y: a) documento escrito dirigido a su domicilio –en forma separada de cualquier otra información que se le remita (resúmenes de cuenta, boletines informativos, etc.), aun cuando forme parte de la misma remesa–; o b) a su correo electrónico –en aquellos casos en que hubiere expresamente aceptado esa forma de notificación–. Estas disposiciones serán de aplicación a los efectos de dar cumplimiento a acuerdos extrajudiciales homologados, acuerdos homologados por acciones colectivas (artículo 54 de la Ley 24.240) o sentencias judiciales, en la medida en que no se opongan a lo previsto en esos acuerdos o a lo dispuesto por los poderes públicos de las distintas jurisdicciones. Adicionalmente, el sujeto obligado deberá verificar si este tipo de situaciones que generan la obligación de reintegros ha ocurrido respecto de los usuarios que se encuentren en la misma situación y, de corresponder, proceder a su reintegro según el procedimiento previsto en este punto, notificando de tal circunstancia y resultados a su Responsable de Atención al Usuario de Servicios Financieros.

### Extracción (código W)

- **op1 Operacion** «Reintegro de importes cobrados indebidamente al usuario» — Reintegro al usuario de servicios financieros de importes cobrados o adeudados por los conceptos enumerados en i) a vii) · props: `{"tipo": "reintegro"}` · tramo [exacta]: «deberá serle reintegrado dentro de:»
- **o1 Obligacion** «Reintegro tasas/comisiones/cargos sin cumplir 2.3.2–2.3.4» — Deber de reintegrar al usuario todo importe cobrado o adeudado por tasas de interés, comisiones y/o cargos sin cumplir los puntos 2.3.2 a 2.3.4, en los plazos de 10 días hábiles desde el reclamo o 5 días hábiles desde la constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: […] i) tasas de interés, comisiones y/o cargos sin el cumplimiento de lo previsto en los puntos 2.3.2. a 2.3.4.;»
- **o2 Obligacion** «Reintegro cargos en exceso de costos de terceros» — Deber de reintegrar cargos en exceso de los costos de servicios que terceros cobraron a los sujetos obligados por servicios a usuarios y/o de los precios que el tercero perciba de particulares en general, en 10 días hábiles desde el reclamo o 5 desde la constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: […] ii) cargos en exceso de los costos de los servicios que terceros les cobraron a los sujetos obligados»
- **o3 Obligacion** «Reintegro comisiones en exceso de máximas BCRA» — Deber de reintegrar comisiones en exceso de las máximas fijadas por el BCRA aplicables, en 10 días hábiles desde el reclamo o 5 desde la constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: […] iii) comisiones en exceso de las máximas fijadas por el BCRA»
- **o4 Obligacion** «Reintegro por exceder tasa máxima de tarjetas» — Deber de reintegrar importes cobrados en incumplimiento de la tasa máxima de financiaciones con tarjetas de crédito (TO Tasas de Interés en las Operaciones de Crédito), en 10 días hábiles desde el reclamo o 5 desde la constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: […] iv) en incumplimiento al nivel de la tasa de interés máxima aplicable a financiaciones vinculadas a tarjetas de crédito»
- **o5 Obligacion** «Reintegro por exceso sobre lo pactado» — Deber de reintegrar importes cobrados en exceso de lo pactado entre usuario y sujeto obligado, en 10 días hábiles desde el reclamo o 5 desde la constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: […] v) en exceso de lo oportunamente pactado entre el usuario y el sujeto obligado;»
- **o6 Obligacion** «Reintegro de conceptos impropios por su naturaleza» — Deber de reintegrar otros importes generados en forma impropia por su naturaleza, como intereses compensatorios por saldos deudores en cuentas de depósito distintas de la cuenta corriente, en 10 días hábiles desde el reclamo o 5 desde la constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: […] vi) otros generados en forma impropia por su naturaleza»
- **o7 Obligacion** «Reintegro por promociones o beneficios mal liquidados» — Deber de reintegrar importes adeudados por liquidar incorrectamente promociones, descuentos u otros beneficios (no ajustados a lo ofrecido, publicitado o convenido), en 10 días hábiles desde el reclamo o 5 desde la constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: […] vii) así como los importes adeudados al usuario por haber liquidado en forma incorrecta promociones, descuentos u otro tipo de beneficios»
- **o8 Obligacion** «Reconocimiento de gastos razonables e intereses compensatorios» — Reconocer gastos razonables para obtener el reintegro e intereses compensatorios desde el cobro indebido hasta la efectiva devolución · props: `{"tipo": "calculo"}` · tramo [exacta]: «corresponderá reconocer el importe de los gastos que resulten razonables realizados para la obtención del reintegro y, en todos los casos, los intereses compensatorios pertinentes»
- **o9 Obligacion** «Tasa 1,5 veces promedio plazo fijo 30-59 días» — Aplicar 1,5 veces la tasa promedio de la encuesta diaria de plazo fijo de 30 a 59 días (pesos o dólares según la operación) informada por el BCRA, entre la exigibilidad y la cancelación; si no está disponible, la última informada · props: `{"tipo": "calculo"}` · umbral: ['1,5 veces la tasa promedio'] · tramo [exacta]: «el sujeto obligado deberá aplicar 1,5 veces la tasa promedio»
- **o10 Obligacion** «Acreditación automática en cuenta a la vista» — La entidad financiera debe acreditar automáticamente el reintegro en la cuenta a la vista del usuario · props: `{"tipo": "otra"}` · tramo [exacta]: «ésta deberá acreditar ese importe en dicha cuenta en forma automática sin necesidad de requerimiento expreso»
- **c1 Condicion** «Usuario con cuenta a la vista en la entidad» — El usuario posee cuenta a la vista abierta a su nombre en la entidad financiera obligada · tramo [exacta]: «Cuando el usuario posea en la entidad financiera obligada una cuenta a la vista que se halle abierta a su nombre»
- **o11 Obligacion** «Acreditación alternativa en tarjeta o financiación» — Acreditar el reintegro en tarjeta de crédito del titular o detraerlo del saldo de la financiación que lo generó · props: `{"tipo": "otra"}` · tramo [exacta]: «el importe del reintegro deberá ser acreditado en una tarjeta de crédito de su titularidad o detraído del saldo vigente de la financiación que lo generó»
- **c2 Condicion** «Imposibilidad de acreditar en cuenta o no ser entidad financiera» — No es posible acreditar en cuenta a la vista o el sujeto no es entidad financiera · tramo [exacta]: «Si ello no fuera posible o no se tratare de una entidad financiera»
- **o12 Obligacion** «Notificación del reintegro por medio electrónico y documento» — Notificar la acreditación o puesta a disposición mediante medios electrónicos y/o telefónicos y, además, documento escrito separado al domicilio o correo electrónico si fue aceptado expresamente · props: `{"tipo": "comunicacion_a_cliente"}` · tramo [exacta]: «Deberá notificarse la acreditación del reintegro o, en su caso, su puesta a disposición mediante aviso efectuado a través de medios electrónicos»
- **o13 Obligacion** «Verificación de usuarios en igual situación» — Verificar si la situación ocurrió con otros usuarios en igual situación, reintegrarles según este punto y notificar circunstancias y resultados al Responsable de Atención al Usuario · props: `{"tipo": "otra"}` · tramo [exacta]: «el sujeto obligado deberá verificar si este tipo de situaciones que generan la obligación de reintegros ha ocurrido respecto de los usuarios que se encuentren en la misma situación»
- **o14 Obligacion** «Aplicación a acuerdos homologados y sentencias» — El procedimiento de reintegro aplica para cumplir acuerdos extrajudiciales u homologados por acciones colectivas (art. 54 Ley 24.240) o sentencias, en la medida que no se opongan a ellos · props: `{"tipo": "otra"}` · tramo [exacta]: «Estas disposiciones serán de aplicación a los efectos de dar cumplimiento a acuerdos extrajudiciales homologados»
- **cm1 Comunicacion** «Ley 24.240» —  · props: `{"codigo": "Ley 24.240", "tipo": "externa"}` · tramo [exacta]: «artículo 54 de la Ley 24.240»
- R: to TextoOrdenado —referencia→ cm1 Comunicacion
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o4 Obligacion —regula→ op1 Operacion
- R: o5 Obligacion —regula→ op1 Operacion
- R: o6 Obligacion —regula→ op1 Operacion
- R: o7 Obligacion —regula→ op1 Operacion
- R: o8 Obligacion —regula→ op1 Operacion
- R: o9 Obligacion —regula→ op1 Operacion
- R: o10 Obligacion —regula→ op1 Operacion
- R: o11 Obligacion —regula→ op1 Operacion
- R: op1 Operacion —requiere→ o12 Obligacion
- R: c1 Condicion —condicion_de→ o10 Obligacion
- R: c2 Condicion —condicion_de→ o11 Obligacion
- R: o9 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- R: o10 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera obligada»)
- R: o13 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- Omisión `fuera_de_tipos` [exacta]: «Ello, sin perjuicio de las sanciones que pudieran corresponder.» — Consecuencia de un incumplimiento (sanciones) sin quien la aplica nombrado

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «conceptos i) a vii)» (i)) | `dentro_de_norma` |  | extraído como norma de otro tipo: o1 Obligacion (un deber de reintegro por concepto) —regula→ op1; sin Condicion |
| 2 | «conceptos i) a vii)» (ii)) | `dentro_de_norma` |  | extraído como norma de otro tipo: o2 Obligacion (un deber de reintegro por concepto) —regula→ op1; sin Condicion |
| 3 | «conceptos i) a vii)» (iii)) | `dentro_de_norma` |  | extraído como norma de otro tipo: o3 Obligacion (un deber de reintegro por concepto) —regula→ op1; sin Condicion |
| 4 | «conceptos i) a vii)» (iv)) | `dentro_de_norma` |  | extraído como norma de otro tipo: o4 Obligacion (un deber de reintegro por concepto) —regula→ op1; sin Condicion |
| 5 | «conceptos i) a vii)» (v)) | `dentro_de_norma` |  | extraído como norma de otro tipo: o5 Obligacion (un deber de reintegro por concepto) —regula→ op1; sin Condicion |
| 6 | «conceptos i) a vii)» (vi)) | `dentro_de_norma` |  | extraído como norma de otro tipo: o6 Obligacion (un deber de reintegro por concepto) —regula→ op1; sin Condicion |
| 7 | «conceptos i) a vii)» (vii)) | `dentro_de_norma` |  | extraído como norma de otro tipo: o7 Obligacion (un deber de reintegro por concepto) —regula→ op1; sin Condicion |
| 8 | «plazo por reclamo» | `dentro_de_norma` |  | dentro de las Obligaciones o1 a o7 (umbral «los diez (10) días hábiles…»); sin Condicion |
| 9 | «por constatación» | `dentro_de_norma` |  | dentro de las Obligaciones o1 a o7 (umbral «los cinco (5) días hábiles…»); sin Condicion |
| 10 | «tasa no disponible» | `dentro_de_norma` |  | dentro de la Obligacion o9 (descripción «si no está disponible, la última informada»); sin Condicion |
| 11 | «cuenta a la vista» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ o10 Obligacion |
| 12 | «si no fuera posible» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ o11 Obligacion |

## `pro::2.7::intro` — [bloque intro] Revocación de la aceptación y rescisión de relaciones contractuales.

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Derechos básicos de los usuarios de servicios financieros.
> *heredado:* 2.7. Revocación de la aceptación y rescisión de relaciones contractuales.
> *propio:* Los sujetos obligados deberán contar con sendos hipervínculos que permitan al usuario:

### Extracción (código W)

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

### Extracción (código W)

- **op1 Operacion** «Registro de consultas y reclamos en RCCR» — Asiento de las consultas y reclamos de usuarios de servicios financieros en una base de datos única y centralizada (RCCR) · props: `{"tipo": "registro"}` · tramo [exacta]: «Registro Centralizado de Consultas y Reclamos (RCCR).»
- **o1 Obligacion** «Asentar todas las presentaciones en base única centralizada» — Asentar en una base de datos única y centralizada todas las consultas o reclamos recibidos de usuarios, independientemente del medio de canalización y de la casa receptora. · props: `{"tipo": "otra"}` · tramo [exacta]: «Se deberán asentar en una base de datos única y centralizada todas las presentaciones (consultas o reclamos) recibidas de los usuarios de servicios financieros»
- **o2 Obligacion** «Asentar consultas que requieren análisis o información» — Deben asentarse en el RCCR las consultas y/o reclamos que para su respuesta requieren análisis de documentación del sujeto obligado o pedido de información a otros sujetos u organismos, de modo que no puede responderse en forma inmediata. · props: `{"tipo": "otra"}` · tramo [exacta]: «Las consultas y/o reclamos que deben ser asentados en el RCCR son aquellos que, para su respuesta al cliente, requieren del análisis de la documentación obrante en el sujeto obligado y/o del pedido de información y/o documentación a otros sujetos u organismos»
- **o3 Obligacion** «Asentar quejas por incumplimiento aun con respuesta inmediata» — Deben asentarse en el RCCR los reclamos que representan una queja por presunto incumplimiento, prestación defectuosa o falta de prestación de un producto o servicio ofrecido por el sujeto obligado, aun cuando pueda dárseles respuesta inmediata. · props: `{"tipo": "otra"}` · tramo [exacta]: «También deben ser asentados en el mencionado registro aquellos reclamos que representan una queja por presunto incumplimiento, prestación defectuosa o falta de prestación»
- **o4 Obligacion** «Datos mínimos a consignar en el RCCR» — Consignar como mínimo: número de consulta o reclamo; fecha, canal y motivo; tipo y número de documento del presentante; casa receptora y afectada/s; otra/s entidad/es involucrada/s y estado del trámite. · props: `{"tipo": "otra"}` · tramo [exacta]: «Deberán consignarse como mínimo los siguientes datos»
- **o5 Obligacion** «Estado del trámite actualizado» — Mantener actualizado el estado del trámite (pendiente de respuesta, con respuesta provisoria o definitiva, junto con la respuesta brindada, etc.). · props: `{"tipo": "otra"}` · tramo [exacta]: «el estado del trámite, el cual deberá mantenerse actualizado»
- **o6 Obligacion** «Numeración correlativa de presentaciones» — Los números asignados a las presentaciones deben ser correlativos. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «Los números asignados a las presentaciones deberán ser correlativos»
- **r1 Restriccion** «Modificación de base solo para altas y actualizaciones» — La base de datos solo puede modificarse para incorporar nuevas consultas o reclamos o agregar información sobre el estado actualizado de los trámites. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «la base de datos sólo podrá ser modificada para la incorporación de nuevas consultas o reclamos, o para el agregado de nueva información sobre el estado actualizado de los trámites»
- **op2 Operacion** «Modificación de la base de datos del RCCR» — Modificación de la base de datos del RCCR · props: `{"tipo": "modificacion de registro"}` · tramo [exacta]: «la base de datos sólo podrá ser modificada»
- **c1 Condicion** «Presentación por teléfono o página de Internet» — Consulta o reclamo iniciado por línea o central telefónica o página de Internet habilitadas para ese fin. · tramo [exacta]: «Cuando la consulta o el reclamo sea iniciada/o llamando a una línea o central telefónica o ingresando datos en una página de Internet, habilitadas para ese fin»
- **o7 Obligacion** «Número provisto en el acto al presentante» — Proveer en el acto al presentante el número de consulta o reclamo, respetando la correlatividad. · props: `{"tipo": "comunicacion_a_cliente"}` · tramo [exacta]: «el número de consulta o reclamo deberá ser provisto en el acto al presentante, respetando la correlatividad citada»
- **c2 Condicion** «Presentante sin número automático» — El presentante no recibe automáticamente el número de su consulta o reclamo. · tramo [exacta]: «Para los casos en que el presentante no reciba automáticamente el número de su consulta o reclamo»
- **o8 Obligacion** «Procedimiento de notificación del número en 3 días» — Establecer un procedimiento que prevea notificar al presentante el número o código asignado dentro de los 3 días hábiles de iniciada la presentación. · props: `{"tipo": "comunicacion_a_cliente"}` · umbral: ['dentro de los tres (3) días hábiles de iniciada la presentación'] · tramo [exacta]: «se deberá establecer un procedimiento que prevea la notificación del número o código que le sea asignado dentro de los tres (3) días hábiles de iniciada la presentación ante el sujeto obligado»
- **o9 Obligacion** «Conservación de la información por 10 años» — Conservar la información incorporada a la base de datos por 10 años. · props: `{"tipo": "otra"}` · umbral: ['por el término de diez (10) años'] · tramo [exacta]: «La información incorporada a esta base de datos deberá conservarse por el término de diez (10) años»
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o4 Obligacion —regula→ op1 Operacion
- R: o6 Obligacion —regula→ op1 Operacion
- R: r1 Restriccion —limita→ op2 Operacion
- R: c1 Condicion —condicion_de→ o7 Obligacion
- R: c2 Condicion —condicion_de→ o8 Obligacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «Los sujetos obligados»)

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «presentación por teléfono o Internet» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ o7 Obligacion |
| 2 | «presentante que no recibe el número automáticamente» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ o8 Obligacion |

## `pro::3.2.3.5` — Los reportes del Directivo Responsable de Protección de los Usuarios de Ser-

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Servicio de atención al usuario de servicios financieros.
> *heredado:* Los sujetos obligados deberán establecer este servicio para dar tratamiento y resolver las consultas y reclamos que presenten los usuarios de servicios financieros, observando las normas legales, reglamentarias y disposiciones vigentes en materia de protección al usuario de servicios financieros, adoptando acciones que reduzcan su reiteración.
> *heredado:* 3.2. Controles.
> *heredado:* 3.2.3. Del Banco Central de la República Argentina.
> *heredado:* En la sede en la cual desempeñe sus funciones el responsable de atención al usuario de servicios financieros (titular o suplente a cargo) deberán encontrarse a disposición del BCRA:
> *propio:* 3.2.3.5. Los reportes del Directivo Responsable de Protección de los Usuarios de Servicios Financieros o del Comité de Protección de los Usuarios de Servicios Financieros, según corresponda.

### Extracción (código W)

- **e1 Obligacion** «Reportes del Directivo/Comité de Protección a disposición BCRA» — Los sujetos obligados deben mantener a disposición del BCRA, en la sede en la cual desempeñe sus funciones el responsable de atención al usuario de servicios financieros (titular o suplente a cargo), los reportes del Directivo Responsable de Protección de los Usuarios de Servicios Financieros o del Comité de Protección de los Usuarios de Servicios Financieros, según corresponda. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «deberán encontrarse a disposición del BCRA: […] Los reportes del Directivo Responsable de Protección de los Usuarios de Servicios Financieros o del Comité de Protección de los Usuarios de Servicios Financieros, según corresponda.»
- R: e1 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «Los sujetos obligados»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:5 | no | «según corresponda» | `extraida_tramo_verificado` |  | e1 Obligacion [exacta], tramo que contiene el fragmento |

## `ric::12.4` — Suspensión de la observancia de las regulaciones técnicas sobre base consolidada

Grupos: omisiones.

### Texto

> *heredado:* Sección 12. Disposiciones transitorias.
> *propio:* 12.4. Suspensión de la observancia de las regulaciones técnicas sobre base consolidada trimestral (punto 6.1. de las normas sobre "Supervisión consolidada"). A partir del período de información abril/24: - Se suspende el envío de informaciones con código de consolidación 3 -con la excepción prevista para Ratio de apalancamiento-, siendo marzo/24 el último período trimestral que corresponde informar con este nivel de consolidación; - En la información sobre base consolidada mensual (códigos de consolidación 2 ó 9) se incluirán -de corresponderlas operaciones de los entes a que refieren los incisos i), ii) y iii) del primer párrafo del punto 6.2. de las normas sobre "Supervisión consolidada. - Las entidades financieras que hasta el 31/03/24 informaban únicamente códigos de consolidación 1 y 3, de mantenerse esta situación de consolidación, pasarán a informar: a) códigos 1 y 9 sólo si consolidan con alguno de los entes a que refieren los incisos i), ii) y iii) del punto 6.2. de las normas citadas; b) en caso contrario, código 0. - Ratio de apalancamiento (Sección 10.) a) Conforme a lo dispuesto en el punto 6.2. último párrafo de las normas sobre "Supervisión consolidada", mantendrá su frecuencia trimestral (datos del mes de cierre de trimestre) y su vencimiento según punto 1.1. del Régimen Informativo para Supervisión; b) Se continuará informando código de consolidación 3; no obstante, las operaciones a incluir serán las que correspondan al perímetro de consolidación mensual, considerando de corresponder, los sujetos previstos en el punto 6.2. de las normas citadas. - Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5.) y Riesgo de tasa de interés en la cartera de inversión (Sección 11.) De corresponder, la consolidación mensual (código 2) considerará las operaciones de los entes a que refieren los incisos i), ii) y iii) del primer párrafo del punto 6.2. de las normas sobre "Supervisión consolidada".

### Extracción (código W)

- **op1 Operacion** «Envío de información código consolidación 3» — Envío de informaciones con código de consolidación 3 (base consolidada trimestral) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «envío de informaciones con código de consolidación 3»
- **r1 Restriccion** «Suspensión envío código consolidación 3» — A partir del período abril/24 se suspende el envío de informaciones con código de consolidación 3, siendo marzo/24 el último período trimestral a informar con ese nivel · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «Se suspende el envío de informaciones con código de consolidación 3»
- **x1 Excepcion** «Ratio de apalancamiento — exceptuado de suspensión código 3» — La suspensión del envío con código de consolidación 3 no alcanza al Ratio de apalancamiento, que continúa informándose con código 3 · tramo [exacta]: «-con la excepción prevista para Ratio de apalancamiento-»
- **o1 Obligacion** «Inclusión entes 6.2 en consolidación mensual» — Desde abril/24, en la información consolidada mensual (códigos 2 ó 9) se incluirán, de corresponder, las operaciones de los entes de los incisos i), ii) y iii) del primer párrafo del punto 6.2. de Supervisión consolidada · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «En la información sobre base consolidada mensual (códigos de consolidación 2 ó 9) se incluirán -de corresponderlas operaciones de los entes»
- **o2 Obligacion** «Informar códigos 1 y 9 si consolidan» — Las entidades financieras que hasta el 31/03/24 informaban solo códigos 1 y 3, de mantenerse esa situación, informarán códigos 1 y 9 sólo si consolidan con alguno de los entes de los incisos i), ii) y iii) del punto 6.2. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «pasarán a informar: a) códigos 1 y 9 sólo si consolidan con alguno de los entes»
- **c1 Condicion** «Informaban solo códigos 1 y 3 hasta 31/03/24» — Entidades que hasta el 31/03/24 informaban únicamente códigos 1 y 3 y mantienen esa situación · tramo [exacta]: «que hasta el 31/03/24 informaban únicamente códigos de consolidación 1 y 3, de mantenerse esta situación de consolidación»
- **c2 Condicion** «Consolida con entes incisos i-iii punto 6.2» — La entidad consolida con alguno de los entes de los incisos i), ii) y iii) del punto 6.2. · tramo [exacta]: «sólo si consolidan con alguno de los entes a que refieren los incisos i), ii) y iii) del punto 6.2.»
- **o3 Obligacion** «Informar código 0 si no consolidan» — Las entidades financieras que hasta el 31/03/24 informaban solo códigos 1 y 3, de mantenerse esa situación y no consolidar con los entes del punto 6.2., informarán código 0 · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «b) en caso contrario, código 0.»
- **o4 Obligacion** «Ratio apalancamiento: frecuencia trimestral y vencimiento» — El Ratio de apalancamiento mantiene frecuencia trimestral (datos del mes de cierre de trimestre) y vencimiento según punto 1.1. del Régimen Informativo para Supervisión · props: `{"tipo": "presentacion_informativa", "frecuencia": "trimestral"}` · tramo [exacta]: «mantendrá su frecuencia trimestral (datos del mes de cierre de trimestre) y su vencimiento según punto 1.1. del Régimen Informativo para Supervisión»
- **o5 Obligacion** «Ratio apalancamiento: código 3 con perímetro mensual» — Para Ratio de apalancamiento se continúa informando código 3, incluyendo las operaciones del perímetro de consolidación mensual, considerando de corresponder los sujetos del punto 6.2. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se continuará informando código de consolidación 3; no obstante, las operaciones a incluir serán las que correspondan al perímetro de consolidación mensual»
- **o6 Obligacion** «Riesgo mercado y tasa: consolidación mensual con entes» — En datos complementarios de riesgo de mercado (puntos 4.3. a 4.5.) y riesgo de tasa de interés (Sección 11.), la consolidación mensual (código 2) considerará, de corresponder, las operaciones de los entes de los incisos i), ii) y iii) del punto 6.2. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «De corresponder, la consolidación mensual (código 2) considerará las operaciones de los entes a que refieren los incisos i), ii) y iii)»
- R: r1 Restriccion —prohibe→ op1 Operacion
- R: x1 Excepcion —exceptua→ r1 Restriccion
- R: c1 Condicion —condicion_de→ o2 Obligacion
- R: c2 Condicion —condicion_de→ o2 Obligacion
- R: c1 Condicion —condicion_de→ o3 Obligacion
- R: o2 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- R: o3 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- Omisión `meta_normativo` [exacta]: «A partir del período de información abril/24:» — Fecha de vigencia de las disposiciones transitorias

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:20 | no | «A partir del período de información abril/24» | `omision_otra_vez` | meta_normativo | om#0 meta_normativo [exacta], mismo tramo |

## `ric::3.1.7` — Exigencia de capital por riesgo de crédito de contraparte en operaciones con en-

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Exigencia por riesgo de crédito
> *heredado:* 3.1. Normas de procedimiento.
> *propio:* 3.1.7. Exigencia de capital por riesgo de crédito de contraparte en operaciones con entidades de contraparte central Las exposiciones de las entidades financieras con entidades de contraparte central con el alcance establecido en el punto 4.3. de las normas sobre "Capitales mínimos de las entidades financieras" –determinadas conforme a dichas normas-, se consignarán en la partida 12500000 por cada ponderador que corresponda aplicar, siguiendo el modelo de información inserto en el punto 3.1.4..

### Extracción (código W)

- **e1 Obligacion** «Consignar exposiciones con CCP en partida 12500000» — Las exposiciones de las entidades financieras con entidades de contraparte central, con el alcance del punto 4.3. de Capitales mínimos y determinadas conforme a dichas normas, se consignan en la partida 12500000 por cada ponderador que corresponda aplicar, siguiendo el modelo del punto 3.1.4. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «se consignarán en la partida 12500000 por cada ponderador que corresponda aplicar, siguiendo el modelo de información inserto en el punto 3.1.4.»
- **e2 Operacion** «Exposiciones con entidades de contraparte central» — Exposiciones de entidades financieras con entidades de contraparte central, con el alcance del punto 4.3. de las normas sobre Capitales mínimos, determinadas conforme a dichas normas · props: `{"tipo": "exposición por riesgo de crédito de contraparte"}` · tramo [exacta]: «Las exposiciones de las entidades financieras con entidades de contraparte central»
- **e3 Comunicacion** «Capitales mínimos de las entidades financieras» —  · props: `{"codigo": "Capitales mínimos de las entidades financieras"}` · tramo [exacta]: «normas sobre "Capitales mínimos de las entidades financieras"»
- R: e1 Obligacion —regula→ e2 Operacion
- R: e1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: to TextoOrdenado —referencia→ e3 Comunicacion

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

### Extracción (código W)

- **e1 Obligacion** «Consignar exigencia riesgo general de acciones (312200/xx)» — En el código 312200/xx se consignará el valor de la exigencia por riesgo general de acciones para el último día del período (n), determinada conforme al punto 6.3. de las normas sobre Capitales mínimos de las entidades financieras. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se consignará el valor de la exigencia por riesgo general de acciones para el último día del período (n) determinada conforme a las disposiciones del punto 6.3. de las normas sobre "Capitales mínimos de las entidades financieras".»
- **e2 Obligacion** «Discriminación por mercado (país) — riesgo de acciones» — La exigencia por riesgo general de acciones se informará discriminada por mercado, identificando el país según la codificación Country Codes del SWIFT. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Este riesgo se discriminará por mercado, entendido a estos efectos como el país en que se negocien posiciones -compradas o vendidasen acciones.»
- **e3 Definicion** «Mercado: país de negociación de acciones» — El país en que se negocien posiciones -compradas o vendidasen acciones; identificado según Country Codes del SWIFT. · props: `{"termino": "mercado"}` · tramo [exacta]: «mercado, entendido a estos efectos como el país en que se negocien posiciones -compradas o vendidasen acciones»

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

### Extracción (código W)

- **op1 Operacion** «Información de futuros y contratos a término (FRA)» — Presentación de información sobre futuros y contratos a término, incluidos los FRA, en el marco de la información sobre instrumentos derivados por riesgo de mercado · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Futuros y Contratos a Término, incluidos los FRA»
- **o1 Obligacion** «Campos del cuadro — futuros y contratos a término» — Informar por cada futuro o contrato a término: descripción del activo subyacente, fecha del plazo residual del subyacente (cuando corresponda), vencimiento del derivado, contraparte/ámbito de negociación, valor nocional, tasa de cupón del subyacente (cuando corresponda), precio pactado del subyacente, precio de mercado del subyacente y compra/venta a término · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Fila 1: col1 = Descripción del activo subyacente(1) | col2 = Fecha correspondiente al plazo residual del subyacente (cuando corresponda)(2) | col3 = Vencimiento del derivado | col4 = Contraparte/Ámb ito de negociación | col5 = Valor nocional(3) | col6 = Tasa de cupón del activo subyacente (cuando corresponda)(4) | col7…»
- **o2 Obligacion** «Describir activo subyacente comprado o vendido» — Describir el activo comprado o vendido a futuro (p. ej. tasa Badlar Privada, dólar estadounidense, bono AJ17D) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Describir el activo comprado o vendido a futuro.»
- **o3 Obligacion** «Valor nocional con moneda o unidad» — Especificar el valor nocional incluyendo la moneda o unidad de medida (p. ej. USD 25.000.000, $ 100.000) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Especificar el valor nocional incluyendo la moneda o unidad de medida.»
- **o4 Obligacion** «Consignar C o V — compra/venta a término» — Consignar "C" si el contrato es una compra a término o "V" si es una venta a término · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Consignar "C" si el contrato en cuestión es una compra a término, o "V" si es una venta a término.»
- **d1 Definicion** «Fecha de plazo residual del subyacente» — Por ejemplo, en un futuro sobre un título público es el plazo residual del título público subyacente · props: `{"termino": "Fecha correspondiente al plazo residual del subyacente"}` · tramo [exacta]: «en un futuro sobre un título público es el plazo residual del título público subyacente»
- **d2 Definicion** «Tasa de cupón del activo subyacente» — Por ejemplo, en un futuro sobre un título público, es la tasa del cupón corriente de dicho título · props: `{"termino": "Tasa de cupón del activo subyacente"}` · tramo [exacta]: «en un futuro sobre un título público, es la tasa del cupón corriente de dicho título»
- **d3 Definicion** «Precio pactado del subyacente» — Valor del subyacente pactado, p. ej. tasa fija pactada, valor pactado del dólar o del bono · props: `{"termino": "Precio pactado del subyacente"}` · tramo [exacta]: «Valor del subyacente pactado.»
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o4 Obligacion —regula→ op1 Operacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | ««C» si es compra a término» | `dentro_de_norma` |  | dentro de la Obligacion o4 (tramo «Consignar "C" si el contrato… es una compra a término»); sin Condicion |
| 2 | ««V» si es venta» | `dentro_de_norma` |  | dentro de la Obligacion o4 (tramo «o "V" si es una venta a término»); sin Condicion |

## `ric::5.1.3.4` — Se informará una sola partida 3600000Y, reflejando la situación de la entidad

Grupos: omisiones.

### Texto

> *heredado:* Sección 5. Exigencia por riesgo operacional
> *heredado:* 5.1. Normas de procedimiento
> *heredado:* 5.1.3. Reducción de la exigencia para entidades financieras del Grupo 2 que pertenezcan a
> *heredado:* los Grupos "A", "B" y "C".
> *propio:* 5.1.3.4. Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación; el promedio de las exigencias por riesgo de crédito se calculará en esta Institución en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos.

### Extracción (código W)

- **e1 Obligacion** «Partida única 3600000Y — calificación de la entidad» — En el marco de la reducción de la exigencia por riesgo operacional para entidades financieras del Grupo 2 de los Grupos A, B y C, se informará una sola partida 3600000Y que refleje la situación de la entidad respecto de su calificación. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación»
- **e2 Operacion** «Cálculo por el BCRA del promedio de exigencias por riesgo de crédito» — El promedio de las exigencias por riesgo de crédito lo calcula esta Institución (BCRA) con los datos de exigencia por riesgo de crédito informada en los períodos previos. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el promedio de las exigencias por riesgo de crédito se calculará en esta Institución en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos»
- R: Sujeto_bcra (mención «esta Institución») —ejecuta→ e2 Operacion
- R: e1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «entidades financieras»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:12 | sí | «reflejando la situación de la entidad respecto de su calificación» | `extraida_tramo_verificado` |  | e1 Obligacion [exacta], tramo que contiene el fragmento |

## `ric::6.1.2` — Conceptos deducibles del capital ordinario de nivel uno (CDCOn1) -Partida 70220000-

Grupos: grupo_c, omisiones.

### Texto

> *heredado:* Sección 6. Responsabilidad Patrimonial Computable
> *heredado:* 6.1. Normas de procedimiento
> *heredado:* La responsabilidad patrimonial computable se determinará en función de los saldos de las partidas admitidas, registrados al último día del mes bajo informe.
> *propio:* 6.1.2. Conceptos deducibles del capital ordinario de nivel uno (CDCOn1) -Partida 70220000Código 20800000. Se informarán las existencias de títulos valores, certificados de depósitos a plazo fijo, otros títulos de crédito, etc., que no se encuentren físicamente en poder de la entidad, de acuerdo con el punto 8.4.1.3. -Sección 8del texto ordenado de las normas sobre "Capitales mínimos de las entidades financieras". Código 20900000. Se incluirá el mayor saldo registrado durante el mes a que corresponde la determinación de la responsabilidad patrimonial computable, de la tenencia de títulos valores y otros instrumentos de deuda, contractualmente subordinados a los demás pasivos, emitidos por otras entidades financieras. Código 21000000. Se consignará el mayor saldo registrado durante el mes a que corresponde la determinación de la responsabilidad patrimonial computable, de las cuentas de corresponsalía con entidades financieras del exterior que no cuenten con calificación "investment grade" otorgada por alguna de las calificadoras admitidas por las normas sobre "Evaluación de entidades financieras". Código 21100000. Se incluirá el mayor saldo registrado durante el mes a que corresponde la determinación del capital ordinario de nivel 1 (COn1), de los títulos emitidos por gobiernos de países extranjeros, cuya calificación internacional sea inferior a la asignada a títulos públicos nacionales de la República Argentina, y que no cuenten con mercados donde se transen en forma habitual por valores relevantes; de acuerdo con el punto 8.4.1.4. de las normas sobre "Capitales mínimos de las entidades financieras". Código 21500000 Se detallará el 100 % del valor -neto de la depreciación acumuladade los bienes inmuebles para uso propio y diversos (incluidos en los rubros 180000 y 190000 del balance de saldos), cuya registración contable no se encuentre respaldada con la pertinente escritura traslativa de dominio debidamente inscripta en el Registro de la Propiedad Inmueble (concepto "CDCOn1"). Código 21600000 Se incluirán los activos intangibles netos de sus respectivas amortizaciones acumuladas. Comprende la llave de negocio que cumpla los requisitos establecidos en el punto 8.4.1.8. de las normas sobre "Capitales mínimos de las entidades financieras". Código 21800000. Comprende las diferencias por insuficiencia de constitución de las previsiones mínimas por riesgo de incobrabilidad determinada por la Superintendencia de Entidades Financieras y Cambiarias, en la medida en que no hayan sido contabilizadas, con efecto al cierre del mes siguiente a aquel en que la entidad reciba la notificación a que se refiere el primer párrafo del punto 2.7. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", según el punto 8.4.1.12. de las normas sobre "Capitales mínimos de las entidades financieras". Código 22000000 Comprende el valor -neto de desafectacionesde la llave negativa registrada en adquisiciones de participaciones por un costo inferior a su valor patrimonial proporcional. Esta partida se computará únicamente en la información consolidada de la adquirente o en la información individual del ente combinado (en caso de fusión entre adquirente y adquirida). Este concepto deberá considerarse con signo negativo dentro del término "CDCOn1". Código 22100000 Comprende el saldo a favor por aplicación del impuesto a la ganancia mínima presunta - neto de las previsionesque exceda el 10% del patrimonio neto básico correspondiente al mes anterior. Además, se incluirá el saldo a favor proveniente de activos por impuestos diferidos. Código 22300000 Se informarán los aportes registrados contablemente como tales cuya capitalización aún no haya sido autorizada por la SEFyC. Códigos 22510000 a 22530000 Se consignarán los excesos a los límites para la afectación de activos en garantía, según lo dispuesto en la Sección 3. de las normas sobre "Afectación de activos en garantía". Código 22600000 Se incluirán las ganancias por ventas resultantes de operaciones de titulización (deberán computarse cuando no se cumpla con los requisitos vinculados con opciones de exclusión, cuando exista respaldo implícito de titulizaciones o cuando corresponda calcular exigencia por titulizaciones con cláusulas de cancelación anticipada). También se incluirán las ganancias por operaciones de venta o cesión de cartera con responsabilidad para el cedente, computadas de acuerdo con lo establecido en el punto 8.4.1.16. de las normas sobre "Capitales mínimos de las entidades financieras". Código 22700000 Se informará el mayor saldo de la asistencia crediticia otorgada en el mes, cuando los adelantos previstos en el punto 3.2.5. de la Sección 3. de las normas sobre "Financiamiento al sector público no financiero" superen el límite autorizado y/o no sean cancelados en los plazos allí previstos. Código 26300000 Se informarán las previsiones por riesgo de incobrabilidad correspondientes a financiaciones en situación normal o cubiertas con garantías preferidas "A" que no superen el 1,25 % de los APRs. En los casos que corresponda, se computará la absorción prevista en la partida 21300000. Códigos 23400000, 23500000, 25300000, 25400000, 27300000 y 27400000 Reflejarán la deducción -para cada nivel de capital consideradode las inversiones en instrumentos computables como capital regulatorio de empresas de servicios complementarios -no sujetas a supervisión consolidaday compañías de seguro, y sus importes se informarán netos de las deducciones previstas en el cronograma del punto 11.5. de las normas sobre "Capitales mínimos de las entidades financieras". Código 21200000 Se informarán los conceptos deducibles del COn1, no incluidos en otros códigos.

### Extracción (código W)

- **op Operacion** «Informe partida CDCOn1 70220000» — Información de los conceptos deducibles del capital ordinario de nivel uno en la partida 70220000 del régimen de Responsabilidad Patrimonial Computable · props: `{"tipo": "presentacion_informativa"}` · tramo [no]: «Conceptos deducibles del capital ordinario de nivel uno (CDCOn1) -Partida 70220000-»
- **o1 Obligacion** «Código 20800000: títulos no en poder» — Informar existencias de títulos valores, certificados de plazo fijo y otros títulos de crédito que no estén físicamente en poder de la entidad, según punto 8.4.1.3. de Capitales mínimos · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informarán las existencias de títulos valores, certificados de depósitos a plazo fijo, otros títulos de crédito, etc., que no se encuentren físicamente en poder de la entidad»
- **o2 Obligacion** «Código 20900000: títulos subordinados otras EF» — Incluir el mayor saldo del mes de tenencia de títulos e instrumentos de deuda subordinados emitidos por otras entidades financieras · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se incluirá el mayor saldo registrado durante el mes a que corresponde la determinación de la responsabilidad patrimonial computable, de la tenencia de títulos valores y otros instrumentos de deuda, contractualmente subordinados a los demás pasivos, emitidos por otras entidades financieras.»
- **o3 Obligacion** «Código 21000000: corresponsalía exterior sin investment grade» — Consignar el mayor saldo del mes de cuentas de corresponsalía con entidades financieras del exterior sin calificación investment grade otorgada por calificadoras admitidas por Evaluación de entidades financieras · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se consignará el mayor saldo registrado durante el mes a que corresponde la determinación de la responsabilidad patrimonial computable, de las cuentas de corresponsalía con entidades financieras del exterior que no cuenten con calificación "investment grade"»
- **o4 Obligacion** «Código 21100000: títulos gobiernos extranjeros baja calificación» — Incluir el mayor saldo del mes de títulos de gobiernos extranjeros con calificación inferior a la de títulos públicos nacionales y sin mercados de negociación habitual por valores relevantes (punto 8.4.1.4. Capitales mínimos) · props: `{"tipo": "presentacion_informativa", "umbrales": [{"tramo": "cuya calificación internacional sea inferior a la\nasignada a títulos públicos nacionales de la República Argentina", "comparacion": "maximo_estricto", "base": "asignada a títulos públicos nacionales de la República Argentina", "regla_comparacion": "limite_relativo:simple:inferior", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['cuya calificación internacional sea inferior a la asignada a títulos públicos na…'] · tramo [exacta]: «Se incluirá el mayor saldo registrado durante el mes a que corresponde la determinación del capital ordinario de nivel 1 (COn1), de los títulos emitidos por gobiernos de países extranjeros»
- **o5 Obligacion** «Código 21500000: inmuebles sin escritura inscripta» — Detallar el 100% del valor neto de depreciación de inmuebles de uso propio y diversos (rubros 180000 y 190000) cuya registración no esté respaldada con escritura inscripta en el Registro de la Propiedad Inmueble · props: `{"tipo": "presentacion_informativa"}` · umbral: ['el 100 % del valor -neto de la depreciación acumulada-'] · tramo [exacta]: «Se detallará el 100 % del valor -neto de la depreciación acumuladade los bienes inmuebles para uso propio y diversos»
- **o6 Obligacion** «Código 21600000: activos intangibles netos» — Incluir activos intangibles netos de amortizaciones, comprendida la llave de negocio que cumpla el punto 8.4.1.8. de Capitales mínimos · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se incluirán los activos intangibles netos de sus respectivas amortizaciones acumuladas. Comprende la llave de negocio»
- **o7 Obligacion** «Código 21800000: insuficiencia de previsiones mínimas» — Informar diferencias por insuficiencia de previsiones mínimas determinadas por la SEFyC no contabilizadas, con efecto al cierre del mes siguiente a la notificación del punto 2.7. de Previsiones mínimas · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Comprende las diferencias por insuficiencia de constitución de las previsiones mínimas por riesgo de incobrabilidad determinada por la Superintendencia»
- **o8 Obligacion** «Código 22000000: llave negativa con signo negativo» — Informar la llave negativa neta de desafectaciones, considerada con signo negativo dentro de CDCOn1 · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Comprende el valor -neto de desafectacionesde la llave negativa registrada en adquisiciones de participaciones por un costo inferior a su valor patrimonial proporcional.»
- **r1 Restriccion** «Llave negativa solo en consolidada/ente combinado» — La partida 22000000 se computa únicamente en la información consolidada de la adquirente o individual del ente combinado en caso de fusión · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «Esta partida se computará únicamente en la información consolidada de la adquirente o en la información individual del ente combinado»
- **o9 Obligacion** «Código 22100000: ganancia mínima presunta e impuestos diferidos» — Informar saldo a favor por impuesto a la ganancia mínima presunta neto de previsiones que exceda el 10% del PN básico del mes anterior, y el saldo a favor por activos por impuestos diferidos · props: `{"tipo": "presentacion_informativa"}` · umbral: ['que exceda el 10% del patrimonio neto básico correspondiente al mes anterior'] · tramo [exacta]: «Comprende el saldo a favor por aplicación del impuesto a la ganancia mínima presunta - neto de las previsionesque exceda el 10% del patrimonio neto básico»
- **o10 Obligacion** «Código 22300000: aportes no autorizados SEFyC» — Informar aportes registrados cuya capitalización no fue autorizada por la SEFyC · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informarán los aportes registrados contablemente como tales cuya capitalización aún no haya sido autorizada por la SEFyC.»
- **o11 Obligacion** «Códigos 22510000-22530000: excesos activos en garantía» — Consignar los excesos a los límites de afectación de activos en garantía (Sección 3 de esas normas) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se consignarán los excesos a los límites para la afectación de activos en garantía»
- **o12 Obligacion** «Código 22600000: ganancias por titulización» — Incluir ganancias por ventas de operaciones de titulización cuando se verifiquen los supuestos indicados · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se incluirán las ganancias por ventas resultantes de operaciones de titulización»
- **c1 Condicion** «Incumplimiento opciones de exclusión» — No se cumplen requisitos de opciones de exclusión · tramo [exacta]: «cuando no se cumpla con los requisitos vinculados con opciones de exclusión»
- **c2 Condicion** «Respaldo implícito de titulizaciones» — Existe respaldo implícito · tramo [exacta]: «cuando exista respaldo implícito de titulizaciones»
- **c3 Condicion** «Exigencia por cancelación anticipada» — Corresponde exigencia por cláusulas de cancelación anticipada · tramo [exacta]: «cuando corresponda calcular exigencia por titulizaciones con cláusulas de cancelación anticipada»
- **o13 Obligacion** «Código 22600000: ganancias cesión con responsabilidad» — Incluir ganancias por venta o cesión de cartera con responsabilidad para el cedente, según punto 8.4.1.16. Capitales mínimos · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «También se incluirán las ganancias por operaciones de venta o cesión de cartera con responsabilidad para el cedente»
- **o14 Obligacion** «Código 22700000: asistencia sector público excedida» — Informar el mayor saldo de asistencia crediticia del mes cuando los adelantos del punto 3.2.5. de Financiamiento al SPNF superen el límite o no se cancelen en plazo · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informará el mayor saldo de la asistencia crediticia otorgada en el mes»
- **c4 Condicion** «Adelantos SPNF exceden límite o plazo» — Adelantos superan límite autorizado y/o no se cancelan en plazo · props: `{"umbrales": [{"tramo": "superen el límite autorizado", "comparacion": "minimo_estricto", "base": "límite autorizado", "regla_comparacion": "limite_relativo:simple:raiz_super", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['superen el límite autorizado'] · tramo [exacta]: «cuando los adelantos previstos en el punto 3.2.5. de la Sección 3. de las normas sobre "Financiamiento al sector público no financiero" superen el límite autorizado y/o no sean cancelados en los plazos allí previstos»
- **o15 Obligacion** «Código 26300000: previsiones situación normal» — Informar previsiones de financiaciones en situación normal o con garantías preferidas A que no superen el 1,25% de los APRs; computar absorción de partida 21300000 cuando corresponda · props: `{"tipo": "presentacion_informativa"}` · umbral: ['que no superen el 1,25 % de los APRs'] · tramo [exacta]: «Se informarán las previsiones por riesgo de incobrabilidad correspondientes a financiaciones en situación normal o cubiertas con garantías preferidas "A"»
- **o16 Obligacion** «Inversiones en servicios complementarios y seguros» — Códigos 23400000 a 27400000: reflejar por nivel de capital la deducción de inversiones en capital regulatorio de empresas de servicios complementarios no sujetas a supervisión consolidada y compañías de seguro, netas del cronograma del punto 11.5. Capitales mínimos · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Reflejarán la deducción -para cada nivel de capital consideradode las inversiones en instrumentos computables como capital regulatorio de empresas de servicios complementarios»
- **o17 Obligacion** «Código 21200000: otros deducibles COn1» — Informar conceptos deducibles del COn1 no incluidos en otros códigos · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informarán los conceptos deducibles del COn1, no incluidos en otros códigos.»
- R: o1 Obligacion —regula→ op Operacion
- R: o2 Obligacion —regula→ op Operacion
- R: o3 Obligacion —regula→ op Operacion
- R: o4 Obligacion —regula→ op Operacion
- R: o5 Obligacion —regula→ op Operacion
- R: o6 Obligacion —regula→ op Operacion
- R: o7 Obligacion —regula→ op Operacion
- R: o8 Obligacion —regula→ op Operacion
- R: o9 Obligacion —regula→ op Operacion
- R: o10 Obligacion —regula→ op Operacion
- R: o11 Obligacion —regula→ op Operacion
- R: o12 Obligacion —regula→ op Operacion
- R: o13 Obligacion —regula→ op Operacion
- R: o14 Obligacion —regula→ op Operacion
- R: o15 Obligacion —regula→ op Operacion
- R: o16 Obligacion —regula→ op Operacion
- R: o17 Obligacion —regula→ op Operacion
- R: r1 Restriccion —limita→ op Operacion
- R: c1 Condicion —condicion_de→ o12 Obligacion
- R: c2 Condicion —condicion_de→ o12 Obligacion
- R: c3 Condicion —condicion_de→ o12 Obligacion
- R: c4 Condicion —condicion_de→ o14 Obligacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «código 22600000 (tres «cuando»)» (opciones de exclusión) | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ o12 Obligacion |
| 2 | «código 22600000 (tres «cuando»)» (respaldo implícito) | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ o12 Obligacion |
| 3 | «código 22600000 (tres «cuando»)» (cancelación anticipada) | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ o12 Obligacion |
| 4 | «código 22700000» | `condicion_con_relacion` |  | c4 Condicion con el umbral —condicion_de→ o14 Obligacion |
| 5 | «código 21800000» | `dentro_de_norma` |  | dentro de la Obligacion o7 (tramo «en la medida en que no hayan sido contabilizadas»); sin Condicion |

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:23 | sí (remisión pura) | «de acuerdo con el punto 8.4.1.3. -Sección 8del texto ordenado de las normas sobre "Capitales mínimos de las entidades financieras"» | `ausente` |  | ningún tramo contiene la remisión; en la descripción de o1 |

## `ric::9.1.3` — Limitación al crecimiento de pasivos

Grupos: grupo_c.

### Texto

> *heredado:* Sección 9. Incrementos de exigencia por riesgo de crédito
> *heredado:* 9.1. Normas de procedimiento
> *propio:* 9.1.3. Limitación al crecimiento de pasivos Cuando se presenten ambas o alguna de las siguientes situaciones: - Obligatoriedad de presentación del Plan de Regularización y Saneamiento en capitales mínimos. - La suma de incrementos de exigencia de capitales mínimos por riesgo de crédito resultantes de los incumplimientos en las relaciones técnicas de activos inmovilizados y/o crediticias, supere el 5 % de dicha exigencia (código 70100000). No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento, teniendo en cuenta el importe registrado en el código 310000 del Balance de Saldos. Se admitirá únicamente el crecimiento originado por el devengamiento de intereses. En los casos de regulaciones sobre base consolidada, se asimilarán las partidas a la posición individual. Dicho límite se observará mientras persista alguna de las situaciones previstas.

### Extracción (código W)

- **op1 Operacion** «Captación de depósitos» — Crecimiento del nivel de depósitos (código 310000 del Balance de Saldos) · props: `{"tipo": "captación de depósitos"}` · tramo [exacta]: «el nivel de depósitos alcanzados»
- **c1 Condicion** «Obligatoriedad de Plan de Regularización y Saneamiento» — Supuesto alternativo (basta uno): obligatoriedad de presentar el Plan de Regularización y Saneamiento en capitales mínimos · tramo [exacta]: «Obligatoriedad de presentación del Plan de Regularización y Saneamiento en capitales mínimos.»
- **c2 Condicion** «Incrementos de exigencia superiores al 5 %» — Supuesto alternativo (basta uno): la suma de incrementos de exigencia por riesgo de crédito por incumplimientos en relaciones técnicas de activos inmovilizados y/o crediticias supera el 5 % de dicha exigencia (código 70100000) · umbral: ['supere el 5 % de dicha exigencia'] · tramo [exacta]: «La suma de incrementos de exigencia de capitales mínimos por riesgo de crédito resultantes de los incumplimientos en las relaciones técnicas de activos inmovilizados y/o crediticias, supere el 5 % de dicha exigencia (código 70100000).»
- **r1 Restriccion** «Tope de depósitos al nivel del mes de incumplimiento» — No podrá excederse el nivel de depósitos alcanzado en el mes en que se origine el incumplimiento (código 310000 del Balance de Saldos), mientras persista alguna de las situaciones; en regulaciones sobre base consolidada las partidas se asimilan a la posición individual · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el\nincumplimiento", "comparacion": "maximo_inclusivo", "base": "nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento", "regla_comparacion": "limite_relativo:negacion:raiz_exced", "origen": "e1", "tramo_verificado": "exacta"}]}` · no definidas: `{"vigencia": "Dicho límite se observará mientras persista alguna de las situaciones previstas.", "base_consolidada": "En los casos de regulaciones sobre base consolidada, se asimilarán las partidas a ` · umbral: ['No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origi…'] · tramo [exacta]: «No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento»
- **x1 Excepcion** «Crecimiento por devengamiento de intereses» — Del tope de depósitos se admite únicamente el crecimiento originado por devengamiento de intereses · tramo [exacta]: «Se admitirá únicamente el crecimiento originado por el devengamiento de intereses.»
- R: c1 Condicion —condicion_de→ r1 Restriccion
- R: c2 Condicion —condicion_de→ r1 Restriccion
- R: r1 Restriccion —limita→ op1 Operacion
- R: x1 Excepcion —exceptua→ r1 Restriccion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «obligación del plan de regularización» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ r1 Restriccion |
| 2 | «incrementos de más del 5 %» | `condicion_con_relacion` |  | c2 Condicion con el umbral —condicion_de→ r1 Restriccion |
| 3 | «base consolidada» | `dentro_de_norma` |  | dentro de la Restriccion r1 (descripción «En regulaciones sobre base consolidada se asimilan las partidas…»); sin Condicion |
| 4 | «mientras persista» | `dentro_de_norma` |  | dentro de la Restriccion r1 (descripción «mientras persista alguna de las situaciones previstas»); sin Condicion |

