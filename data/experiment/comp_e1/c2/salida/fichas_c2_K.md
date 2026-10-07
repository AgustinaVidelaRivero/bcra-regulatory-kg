# Fichas de C2 — código K

Lectura cegada (primera lectura de la instancia). El código no dice el brazo ni la corrida; la tabla sigue cerrada hasta la adjudicación. Clases de M1 y M2: `c0/reglas_lectura_c0.md`.

## `cap::10.3.1.1` — Se asignarán las calificaciones de las ECAI admisibles a los ponderadores de

Grupos: omisiones.

### Texto

> *heredado:* Sección 10. Agentes de calificación externa (ECAI).
> *heredado:* 10.3. Consideraciones para su implementación.
> *heredado:* 10.3.1. Proceso de asignación de calificaciones (mapping).
> *propio:* 10.3.1.1. Se asignarán las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4.; es decir, las entidades financieras deberán establecer qué calificaciones o categorías de evaluación corresponden a esos ponderadores de riesgo. El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en esas calificaciones. Además, deberá abarcar todos los ponderadores de riesgo previstos en esos puntos.

### Extracción (código K)

- **op1 Operacion** «Mapping de calificaciones ECAI a ponderadores» — Asignación de las calificaciones de las ECAI admisibles a los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «Proceso de asignación de calificaciones (mapping).»
- **o1 Obligacion** «Establecer correspondencia calificaciones–ponderadores de riesgo» — Las entidades financieras deberán asignar las calificaciones de las ECAI admisibles a los ponderadores de riesgo del primer párrafo del punto 2.5.4., estableciendo qué calificaciones o categorías de evaluación corresponden a cada ponderador. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «las entidades financieras deberán establecer qué calificaciones o categorías de evaluación corresponden a esos ponderadores de riesgo»
- **o2 Obligacion** «Mapping objetivo y coherente con riesgo de crédito» — El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en las calificaciones. · props: `{"tipo": "otra"}` · tramo [exacta]: «El proceso de asignación (mapping) deberá ser objetivo y ofrecer una distribución de ponderadores coherente con la distribución de los niveles de riesgo de crédito recogidos en esas calificaciones»
- **o3 Obligacion** «Mapping debe abarcar todos los ponderadores» — El proceso de asignación deberá abarcar todos los ponderadores de riesgo previstos en los puntos referidos en el primer párrafo del punto 2.5.4. · props: `{"tipo": "otra"}` · tramo [exacta]: «deberá abarcar todos los ponderadores de riesgo previstos en esos puntos»
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

### Extracción (código K)

- **op1 Operacion** «Cálculo exigencia capital por riesgo de crédito» — Determinación de la exigencia de capital mínimo por riesgo de crédito (C RC) mediante la expresión que combina factor k, 8% de los APR e incrementos por excesos (INC) · props: `{"tipo": "calculo"}` · tramo [exacta]: «exigencia de capital por riesgo de crédito»
- **ob1 Obligacion** «Factor k según calificación SEFYC — exigencia» — Aplicar el factor k según la calificación asignada por la SEFYC: calificación 1 → k=1; 2 → 1,03; 3 → 1,08; 4 → 1,13; 5 → 1,19. · props: `{"tipo": "calculo", "umbrales": [{"tramo": "Fila 1: Calificación asignada = 1 | Valor de “k” = 1", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "Fila 2: Calificación asignada = 2 | Valor de “k” = 1,03", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "Fila 3: Calificación asignada = 3 | Valor de “k” = 1,08", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "Fila 4: Calificación asignada = 4 | Valor de “k” = 1,13", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "Fila 5: Calificación asignada = 5 | Valor de “k” = 1,19", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['Fila 1: Calificación asignada = 1 | Valor de "k" = 1', 'Fila 2: Calificación asignada = 2 | Valor de "k" = 1,03', 'Fila 3: Calificación asignada = 3 | Valor de "k" = 1,08', 'Fila 4: Calificación asignada = 4 | Valor de "k" = 1,13', 'Fila 5: Calificación asignada = 5 | Valor de "k" = 1,19'] · tramo [exacta]: «k: factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por la SEFYC, teniendo en cuenta la siguiente escala:»
- **ob2 Obligacion** «Última calificación al tercer mes siguiente — k» — Considerar la última calificación informada para la exigencia a integrar al tercer mes siguiente al de la notificación. · props: `{"tipo": "calculo", "umbrales": [{"tramo": "al tercer mes siguiente a aquel en que tenga lugar la\nnotificación", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['al tercer mes siguiente a aquel en que tenga lugar la notificación'] · tramo [exacta]: «se considerará la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación»
- **ob3 Obligacion** «k igual 1,03 sin calificación comunicada» — Mientras no se comunique la calificación, k será igual a 1,03. · props: `{"tipo": "calculo"}` · tramo [exacta]: «En tanto no se comunique, el valor de "k" será igual a 1,03.»
- **c3 Condicion** «Calificación no comunicada» — Mientras la calificación no haya sido comunicada · tramo [exacta]: «En tanto no se comunique»
- **d1 Definicion** «APR: activos ponderados por riesgo de crédito» — Activos ponderados por riesgo de crédito, suma de valores de la expresión con A, PFB, CCF, p, no DvP, DvP, RCD e INC(inversiones significativas en empresas) x 12,5. · props: `{"termino": "APR"}` · tramo [exacta]: «APR : activos ponderados por riesgo de crédito»
- **d2 Definicion** «A: activos computables/exposiciones» — activos computables/exposiciones · props: `{"termino": "A"}` · tramo [exacta]: «A: activos computables/exposiciones.»
- **d3 Definicion** «PFB: partidas fuera de balance» — partidas fuera de balance (conceptos computables no registrados en el balance de saldos) · props: `{"termino": "PFB"}` · tramo [exacta]: «PFB: partidas fuera de balance (conceptos computables no registrados en el balance de saldos).»
- **d4 Definicion** «CCF: factor de conversión crediticia» — factor de conversión crediticia · props: `{"termino": "CCF"}` · tramo [exacta]: «CCF: factor de conversión crediticia.»
- **d5 Definicion** «p: ponderador de riesgo» — ponderador de riesgo, en tanto por uno · props: `{"termino": "p"}` · tramo [exacta]: «p: ponderador de riesgo, en tanto por uno.»
- **d6 Definicion** «no DvP: operaciones sin entrega contra pago» — operaciones sin entrega contra pago; importe = suma de aplicar a las operaciones el ponderador p del punto 4.1 · props: `{"termino": "no DvP"}` · tramo [exacta]: «no DvP: operaciones sin entrega contra pago.»
- **d7 Definicion** «DvP: entrega contra pago fallidas» — operaciones de entrega contra pago fallidas, incluidas PvP fallidas; importe = exposición actual positiva por la exigencia del punto 4.1 · props: `{"termino": "DvP"}` · tramo [exacta]: «DvP: operaciones de entrega contra pago fallidas (a los efectos de estas normas, incluyen las operaciones de pago contra pago –PvP– fallidas).»
- **d8 Definicion** «RCD: riesgo contraparte derivados OTC» — exigencia por riesgo de crédito de contraparte en derivados OTC, según punto 4.2 · props: `{"termino": "RCD"}` · tramo [exacta]: «RCD: exigencia por riesgo de crédito de contraparte en operaciones con derivados extrabursátiles (over-the-counter, OTC)»
- **r1 Restriccion** «15% por empresa — participaciones en capital» — Límite de participación en el capital de cada empresa: 15% de la RPC del último día anterior; excesos incrementan la exigencia (INC inversiones significativas). · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['participación en el capital de cada empresa: 15%'] · tramo [exacta]: «– participación en el capital de cada empresa: 15%;»
- **r2 Restriccion** «60% total — participaciones en capital empresas» — Límite del total de participaciones en el capital de empresas: 60% de la RPC del último día anterior. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['total de participaciones en el capital de empresas: 60%'] · tramo [exacta]: «– total de participaciones en el capital de empresas: 60%.»
- **op2 Operacion** «Participación en capital de empresas» — Tenencia de participaciones en el capital de empresas por la entidad financiera · props: `{"tipo": "inversion"}` · tramo [exacta]: «participación en el capital de cada empresa»
- **ob4 Obligacion** «Incremento INC por excesos a relaciones técnicas» — Incrementar la exigencia por excesos en: activos inmovilizados; límites de financiamiento al SPNF; grandes exposiciones; graduación del crédito; derivados sobre commodities; excluidos los computados en INC(inversiones significativas en empresas). Aplican Sección 2 del TO de Incumplimientos salvo que rija su Sección 3. · props: `{"tipo": "calculo"}` · tramo [exacta]: «INC: incremento por los siguientes excesos:»
- **ob5 Obligacion** «Computar uso de cupos ampliados SPNF como INC» — Computar como INC la exposición por uso de cupos ampliados (puntos 6.1.1.2. y 6.1.2.1. d) del TO SPNF) respecto de asistencia a fideicomisos o fondos fiduciarios, según cronograma: 25% desde el primer mes, 50% desde el séptimo, 100% desde el décimo tercero. · props: `{"tipo": "calculo", "umbrales": [{"tramo": "25 Primer mes", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "50 Séptimo mes", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "100 Décimo tercer mes", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['25 Primer mes', '50 Séptimo mes', '100 Décimo tercer mes'] · tramo [exacta]: «También se computará en esta expresión la exposición crediticia resultante de la utilización de los cupos crediticios ampliados»
- **c5 Condicion** «Inicio de uso económico de obras» — El cronograma opera desde que las obras se usan económicamente o el equipamiento genera ingresos al fideicomiso o fondo · tramo [exacta]: «a partir de que se hayan comenzado a utilizar económicamente las obras o el equipamiento genere ingresos al fideicomiso o fondo fiduciario»
- **d9 Definicion** «Sector público no financiero — remisión TO SPNF» — el definido en la Sección 1. del TO sobre Financiamiento al Sector Público no Financiero · props: `{"termino": "sector público no financiero"}` · tramo [exacta]: «El sector público no financiero citado en estas normas es aquel definido en la Sección 1. del TO sobre Financiamiento al Sector Público no Financiero.»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion
- R: ob4 Obligacion —regula→ op1 Operacion
- R: ob5 Obligacion —regula→ op1 Operacion
- R: c3 Condicion —condicion_de→ ob3 Obligacion
- R: c5 Condicion —condicion_de→ ob5 Obligacion
- R: r1 Restriccion —limita→ op2 Operacion
- R: r2 Restriccion —limita→ op2 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: r2 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- Omisión `formula` [exacta]: «C = (k x 0,08 x APR ) + INC» — Fórmula declarada no confiable; no se reconstruye.
- Omisión `formula` [exacta]: «A x p + PFB x CCF x p + no DvP + (DVP + RCD + INC(inversiones empresas)) x 12,5» — Fórmula de APR no confiable; no se reconstruye.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «en tanto no se comunique la calificación» | `condicion_con_relacion` |  | c3 Condicion «Calificación no comunicada» —condicion_de→ ob3 Obligacion |
| 2 | «el cronograma opera desde que las obras se usan económicamente» | `condicion_con_relacion` |  | c5 Condicion «Inicio de uso económico de obras» —condicion_de→ ob5 Obligacion |

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

### Extracción (código K)

- **op1 Operacion** «Exposiciones minoristas normativas a personas humanas» — Inclusión de financiaciones a personas humanas como exposiciones minoristas normativas · props: `{"tipo": "clasificación de exposición"}` · tramo [exacta]: «En el caso de exposiciones minoristas a personas humanas»
- **r1 Restriccion** «Relación cuota/ingreso máx. 30% — minoristas personas humanas» — En exposiciones minoristas a personas humanas, el total de vencimientos por cuotas de todas las financiaciones de la entidad con amortización periódica (sin cuotas de créditos de otras entidades) no debe exceder, al momento de los acuerdos, el 30% de los ingresos del deudor y/o codeudores. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['no deberá exceder, al momento de los acuerdos, el 30% de los ingresos del deudor'] · tramo [exacta]: «el total de los vencimientos por las cuotas de todas las financiaciones de la entidad financiera que cuenten con amortización periódica –sin considerar las cuotas de créditos de otras entidades– no deberá exceder, al momento de los acuerdos, el 30% de los ingresos del deudor y/o, en su caso, de los codeudores.»
- **d1 Definicion** «Exclusiones del numerador de la relación cuota/ingreso» — No integran el numerador los márgenes acordados para descubiertos en cuenta corriente y los límites de compra de tarjetas de crédito (utilizado y disponible), ni los préstamos personales preacordados aún no formalizados ni desembolsados, por no contar con amortización periódica. · props: `{"termino": "numerador de la relación cuota/ingreso"}` · tramo [exacta]: «no formarán parte del numerador de la relación cuota/ingreso por no contar con una amortización periódica»
- **d2 Definicion** «Cuotas incluyen compras financiadas con tarjeta» — Comprende las cuotas que el cliente tenga por compras financiadas en el sistema de tarjeta de crédito. · props: `{"termino": "cuotas"}` · tramo [exacta]: «Deberá considerarse dentro del concepto "cuotas" aquellas que el cliente tenga por compras financiadas en el marco del sistema de tarjeta de crédito.»
- **o1 Obligacion** «Información de verificación — compra de cartera minorista» — Para considerar como exposiciones minoristas normativas créditos incorporados por compra de cartera, se debe contar con la información necesaria para verificar el cumplimiento de los criterios y límites precedentes. · props: `{"tipo": "otra"}` · tramo [exacta]: «se deberá contar con la información necesaria para verificar el cumplimiento de los criterios y límites detallados precedentemente.»
- **op2 Operacion** «Inclusión en minoristas normativas de cartera comprada» — Considerar como exposiciones minoristas normativas créditos incorporados por compra de cartera · props: `{"tipo": "clasificación de exposición"}` · tramo [exacta]: «A los efectos de considerar en las exposiciones minoristas normativas a los créditos incorporados a través de una compra de cartera»
- R: r1 Restriccion —limita→ op1 Operacion
- R: o1 Obligacion —condiciona→ op2 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «entidad financiera»)
- R: op1 Operacion —aplica_a→ Sujeto_persona_humana (mención «personas humanas»)

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

### Extracción (código K)

- **d1 Definicion** «Exposiciones subyacentes a la titulización: conceptos incluidos» — Las exposiciones subyacentes a la titulización pueden incluir, entre otros conceptos (lista no taxativa): préstamos, compromisos asumidos por la entidad, posiciones de titulización, obligaciones negociables y acciones. · props: `{"termino": "exposiciones subyacentes a la titulización"}` · tramo [exacta]: «Las exposiciones subyacentes a la titulización podrán incluir, entre otros conceptos: préstamos, compromisos asumidos por la entidad, posiciones de titulización, obligaciones negociables y acciones.»
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

### Extracción (código K)

- **d1 Definicion** «KSA — exigencia de capital promedio subyacentes» — KSA: ratio entre la suma de las exposiciones subyacentes ponderadas por riesgo y la suma de las exposiciones subyacentes, multiplicado por 8 %; porcentaje entre cero y cien. · props: `{"termino": "K"}` · tramo [exacta]: «Es la exigencia de capital promedio de las exposiciones subyacentes»
- **o1 Obligacion** «Reflejar coberturas — cálculo de KSA» — El cálculo de KSA debe reflejar los efectos de cualquier cobertura del riesgo de crédito aplicable a las exposiciones subyacentes (individualmente o al conjunto). · props: `{"tipo": "calculo"}` · tramo [exacta]: «El cálculo deberá reflejar los efectos de cualquier cobertura del riesgo de crédito que corresponda aplicar a las exposiciones subyacentes»
- **d2 Definicion** «Activos subyacentes con SPE — conjunto» — Cuando la estructura involucre a un SPE, integran el conjunto todas las exposiciones del SPE vinculadas a la titulización: activos invertidos, reservas, cuentas de efectivo en garantía y derechos frente a contrapartes por swaps. · props: `{"termino": "conjunto de activos subyacentes"}` · tramo [exacta]: «se considerará que todas las exposiciones del SPE vinculadas a la titulización integran el conjunto de activos subyacentes»
- **p1 Potestad** «Excluir exposiciones del SPE — subyacentes» — A los fines del cálculo de la exigencia de capital, la entidad puede excluir del conjunto de activos subyacentes las exposiciones del SPE. · tramo [exacta]: «la entidad podrá excluir del conjunto de activos subyacentes a las exposiciones del SPE»
- **c1 Condicion** «Demostrar riesgo no afecta o insignificante» — La entidad demuestra que el riesgo no afecta su posición de titulización o que es insignificante (p.ej., mitigado). · tramo [exacta]: «si puede demostrar que el riesgo no afecta a su posición de titulización o, en su defecto, que el riesgo es insignificante»
- **o2 Obligacion** «Computar CLN en KSA — titulizaciones sintéticas fondeadas» — En titulizaciones sintéticas a las que se aporten fondos, computar en KSA los montos recibidos por credit linked notes u otros pasivos suscriptos por el SPE. · props: `{"tipo": "calculo"}` · tramo [exacta]: «se deberán computar para el cálculo del K los montos recibidos por los insSA trumentos con vinculación crediticia»
- **c2 Condicion** «Importes sirven como garantía del repago» — Los importes sirven como garantía del repago de la exposición titulizada. · tramo [exacta]: «cuando dichos importes sirvan como garantía del repago de la exposición titulizada en cuestión»
- **c3 Condicion** «Riesgo sujeto a asignación por tramos» — El riesgo de incumplimiento está sujeto a la asignación de pérdidas por tramos. · tramo [exacta]: «el riesgo de incumplimiento esté sujeto a la asignación de pérdidas por tramos»
- **x1 Excepcion** «Riesgo insignificante demostrado — cómputo CLN» — No se computan los montos si la entidad demuestra que el riesgo de incumplimiento es insignificante. · tramo [exacta]: «Ello a menos que la entidad pueda demostrar que el riesgo de incumplimiento es insignificante.»
- **o3 Obligacion** «Monto bruto sin previsión — cálculo KSA» — Si la entidad constituyó previsión específica o tiene descuento no reembolsable en el precio de compra, KSA se calcula con el monto bruto, sin deducirlos. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el cálculo de K deberá SA efectuarse usando el monto bruto de la exposición»
- **c4 Condicion** «Previsión específica o descuento no reembolsable» — La entidad constituyó previsión específica o tiene descuento no reembolsable en el precio de compra de su exposición. · tramo [exacta]: «En los casos en los que la entidad haya constituido una previsión específica o tenga un descuento no reembolsable en el precio de compra»
- **d3 Definicion** «W — ratio de subyacentes en mora» — Ratio entre monto nominal de exposiciones subyacentes en mora y monto nominal de las exposiciones subyacentes. · props: `{"termino": "W"}` · tramo [exacta]: «La variable W es el ratio entre el monto nominal de las exposiciones subyacentes en mora y el monto nominal de las exposiciones subyacentes.»
- **d4 Definicion** «Exposiciones subyacentes en mora» — Atrasos de 90 días o más, quiebra o concurso, ejecución, inmuebles adquiridos en defensa del crédito o incumplimiento según los contratos de titulización. · props: `{"termino": "en mora"}` · tramo [exacta]: «Se consideran en mora a las exposiciones subyacentes cuando se verifiquen atrasos en los pagos de 90 días o más»
- **o4 Obligacion** «W cero para tramos — retitulizaciones mixtas» — En retitulizaciones con cartera de tramos de titulización y otros activos, W es cero para posiciones de titulización y la que corresponda para los demás activos. · props: `{"tipo": "calculo"}` · tramo [exacta]: «W será cero para las posiciones de titulización»
- **o5 Obligacion** «KA por subconjunto — retitulizaciones mixtas» — En retitulizaciones mixtas, calcular KA por separado por subconjunto aplicando W por separado; KA de la retitulización es el promedio ponderado por exposición nominal. · props: `{"tipo": "calculo"}` · tramo [exacta]: «se deberá calcular por separado el K coA rrespondiente a cada subconjunto»
- **o6 Obligacion** «Ajuste de KA — cumplimiento desconocido ≤5 %» — Ajustar el cálculo de KA cuando se desconoce la situación de cumplimiento del 5 % o menos de las subyacentes. · props: `{"tipo": "calculo"}` · tramo [exacta]: «se deberá ajustar el cálculo de K de la siguiente manera»
- **c5 Condicion** «Desconocido 5 % o menos de subyacentes» — Se desconoce la situación de cumplimiento de 5 % o menos de las subyacentes. · umbral: ['5 % o menos de las exposiciones subyacentes'] · tramo [exacta]: «En caso de que se desconozca la situación de cumplimiento correspondiente al 5 % o menos de las exposiciones subyacentes»
- **o7 Obligacion** «Ponderar 1250 % — cumplimiento desconocido >5 %» — La posición de titulización debe ponderarse al 1250 % si la entidad no conoce la situación de cumplimiento para más del 5 %. · props: `{"tipo": "calculo"}` · umbral: ['ponderarse al 1250 %'] · tramo [exacta]: «ésta deberá ponderarse al 1250 %»
- **c6 Condicion** «Desconocido más del 5 % de posición» — La entidad no conoce la situación de cumplimiento para más del 5 % de la posición. · umbral: ['más del 5 %'] · tramo [exacta]: «Si la entidad no conociera la situación de cumplimiento para más del 5 % de la posición de titulización»
- **d5 Definicion** «KSSFA(KA) — exigencia por unidad de posición» — Exigencia de capital por unidad de posición de titulización, KSSFA(KA), calculada por fórmula con parámetro p: 0,5 si cumple STC, 1 si no, 1,5 si retitulización. · props: `{"termino": "K"}` · tramo [exacta]: «La exigencia de capital por unidad de posición de titulización, K , se SSFA(KA) calculará conforme a lo siguiente»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ o2 Obligacion
- R: c3 Condicion —condicion_de→ o2 Obligacion
- R: x1 Excepcion —exceptua_obligacion→ o2 Obligacion
- R: c4 Condicion —condicion_de→ o3 Obligacion
- R: c5 Condicion —condicion_de→ o6 Obligacion
- R: c6 Condicion —condicion_de→ o7 Obligacion
- R: p1 Potestad —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- R: o3 Obligacion —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- R: o7 Obligacion —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- Omisión `formula` [exacta]: «K se obtiene a partir de K y W conforme a la siguiente expresión:» — Fórmula de KA no confiable en la extracción del PDF.
- Omisión `formula` [exacta]: «se deberá ajustar el cálculo de K de la siguiente manera:» — Fórmula de ajuste de KA no reproducida.
- Omisión `formula` [exacta]: «calculará conforme a lo siguiente: donde:» — Fórmula SSFA no confiable; solo se recogen los valores de p que enuncia la prosa en la definición.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «estructura con SPE» | `dentro_de_norma` |  | dentro de la Definicion d2 («Activos subyacentes con SPE») |
| 2 | «si puede demostrar» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ p1 Potestad |
| 3 | «sintéticas con fondos aportados» | `dentro_de_norma` |  | dentro de la Obligacion o2 (descripción «En titulizaciones sintéticas a las que se aporten fondos»); c2 y c3 son otros supuestos |
| 4 | «previsión específica» | `condicion_con_relacion` |  | c4 Condicion —condicion_de→ o3 Obligacion |
| 5 | «desconocida para 5 % o menos» | `condicion_con_relacion` |  | c5 Condicion con el umbral —condicion_de→ o6 Obligacion |
| 6 | «para más del 5 %» | `condicion_con_relacion` |  | c6 Condicion con el umbral —condicion_de→ o7 Obligacion |

## `cap::3.1.11.3` — Determinación del ponderador de riesgo (RW).

Grupos: grupo_c.

### Texto

> *heredado:* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos.
> *heredado:* 3.1. Tratamiento de las titulizaciones.
> *heredado:* Se denomina "posición de titulización" a la exposición a una titulización (o retitulización), tradicional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes conceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos ("AssetBacked Securities", ABS) y bonos de titulización hipotecaria ("Mortgage-Backed Securities", MBS)–, mejoras crediticias, facilidades de liquidez, "swaps" de tasa de interés o de monedas y derivados de crédito. Las reservas ("reserve accounts"), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo también el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad económica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una determinada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> *heredado:* 3.1.11. Enfoque estandarizado.
> *heredado:* Los ponderadores de riesgo a aplicar a las posiciones de una titulización y a las exposiciones subyacentes de una retitulización para la determinación de la exigencia de capital se establecerán empleando las disposiciones de este punto. Las posiciones de titulización a las que no se les pueda aplicar el enfoque estandarizado deberán ser ponderadas al 1250 %.
> *propio:* 3.1.11.3. Determinación del ponderador de riesgo (RW). El ponderador de riesgo RW a asignar a una posición de titulización se calculará con ajuste a lo siguiente: i) Si D es menor o igual a K , el ponderador será de 1250 %. A ii) Si A es mayor o igual a K , el ponderador será igual a K multiplicado A SSFA(KA) por 12,5. iii) Si K es mayor que A y menor que D, el ponderador será un promedio A ponderado entre 1250 % y 12,5 veces K conforme a la siguiente exSSFA(KA) presión: El ponderador para coberturas del riesgo de mercado, tales como "swaps" de moneda o de tasa de interés, se inferirá a partir de una posición de titulización de igual prelación ("pari passu") con los "swaps" o, si tal posición no existiera, a partir del tramo subordinado más próximo. El ponderador resultante estará sujeto a un mínimo de: a) 15 % para titulizaciones que no cumplan con los criterios STC –punto 3.1.14.–. b) 10 % para los tramos de máxima preferencia de titulizaciones que cumplan con los criterios STC –punto 3.1.14.– y 15 % para los tramos subordinados de esas titulizaciones. c) 100 % para retitulizaciones. Para posiciones de titulización de máxima preferencia se podrá aplicar el tratamiento de transparencia ("look-through") de conformidad con lo previsto en el punto 3.1.6. Si el ponderador que surge de la aplicación de ese tratamiento fuera menor que el ponderador mínimo que corresponda de acuerdo con los apartados a) a c) precedentes, se podrá aplicar el primero.

### Extracción (código K)

- **op1 Operacion** «Asignación de RW a posición de titulización» — Asignación del ponderador de riesgo RW a una posición de titulización bajo el enfoque estandarizado (SSFA) · props: `{"tipo": "ponderación por riesgo"}` · tramo [exacta]: «El ponderador de riesgo RW a asignar a una posición de titulización»
- **ob1 Obligacion** «RW 1250 % si D ≤ KA» — El RW de la posición de titulización se calculará en 1250 % cuando D sea menor o igual a KA. · props: `{"tipo": "calculo"}` · umbral: ['el ponderador será de 1250 %'] · tramo [exacta]: «Si D es menor o igual a K , el ponderador será de 1250 %.»
- **c1 Condicion** «D menor o igual a KA» — El punto de desprendimiento D es menor o igual a KA. · tramo [exacta]: «Si D es menor o igual a K»
- **ob2 Obligacion** «RW = KSSFA × 12,5 si A ≥ KA» — Cuando A es mayor o igual a KA, el RW será igual a KSSFA(KA) multiplicado por 12,5. · props: `{"tipo": "calculo"}` · tramo [exacta]: «Si A es mayor o igual a K , el ponderador será igual a K multiplicado»
- **c2 Condicion** «A mayor o igual a KA» — El punto de enganche A es mayor o igual a KA. · tramo [exacta]: «Si A es mayor o igual a K»
- **ob3 Obligacion** «RW promedio ponderado si A < KA < D» — Cuando KA es mayor que A y menor que D, el RW será un promedio ponderado entre 1250 % y 12,5 veces KSSFA(KA) conforme a una expresión. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el ponderador será un promedio»
- **c3 Condicion** «KA entre A y D» — KA es mayor que A y menor que D. · tramo [exacta]: «Si K es mayor que A y menor que D»
- **ob4 Obligacion** «RW de coberturas de riesgo de mercado inferido» — El RW para coberturas de riesgo de mercado (swaps de moneda o tasa) se inferirá de una posición de titulización pari passu con los swaps o, si no existiera, del tramo subordinado más próximo. · props: `{"tipo": "calculo"}` · tramo [exacta]: «El ponderador para coberturas del riesgo de mercado, tales como "swaps" de moneda o de tasa de interés, se inferirá a partir de una posición de titulización de igual prelación ("pari passu") con los "swaps"»
- **r1 Restriccion** «Piso 15 % RW — titulizaciones no STC» — El ponderador resultante tendrá un mínimo de 15 % para titulizaciones que no cumplan los criterios STC. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['sujeto a un mínimo de: a) 15 %'] · tramo [exacta]: «15 % para titulizaciones que no cumplan con los criterios STC»
- **r2 Restriccion** «Piso 10 % RW — tramos preferentes STC» — Mínimo de 10 % para tramos de máxima preferencia de titulizaciones que cumplan criterios STC. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['10 % para los tramos de máxima preferencia'] · tramo [exacta]: «10 % para los tramos de máxima preferencia de titulizaciones que cumplan con los criterios STC»
- **r3 Restriccion** «Piso 15 % RW — tramos subordinados STC» — Mínimo de 15 % para los tramos subordinados de titulizaciones que cumplan criterios STC. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['15 % para los tramos subordinados'] · tramo [exacta]: «15 % para los tramos subordinados de esas titulizaciones»
- **r4 Restriccion** «Piso 100 % RW — retitulizaciones» — Mínimo de 100 % para retitulizaciones. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['100 % para retitulizaciones'] · tramo [exacta]: «100 % para retitulizaciones»
- **p1 Potestad** «Look-through para posiciones de máxima preferencia» — Para posiciones de titulización de máxima preferencia se podrá aplicar el tratamiento de transparencia conforme al punto 3.1.6. · tramo [exacta]: «Para posiciones de titulización de máxima preferencia se podrá aplicar el tratamiento de transparencia ("look-through")»
- **ex1 Excepcion** «RW look-through inferior al mínimo aplicable» — Se podrá aplicar el RW del look-through aunque sea menor que los mínimos de los apartados a) a c). · tramo [exacta]: «Si el ponderador que surge de la aplicación de ese tratamiento fuera menor que el ponderador mínimo que corresponda de acuerdo con los apartados a) a c) precedentes, se podrá aplicar el primero.»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion
- R: ob4 Obligacion —regula→ op1 Operacion
- R: c1 Condicion —condicion_de→ ob1 Obligacion
- R: c2 Condicion —condicion_de→ ob2 Obligacion
- R: c3 Condicion —condicion_de→ ob3 Obligacion
- R: r1 Restriccion —limita→ op1 Operacion
- R: r2 Restriccion —limita→ op1 Operacion
- R: r3 Restriccion —limita→ op1 Operacion
- R: r4 Restriccion —limita→ op1 Operacion
- R: ex1 Excepcion —exceptua→ r1 Restriccion
- R: ex1 Excepcion —exceptua→ r2 Restriccion
- R: ex1 Excepcion —exceptua→ r3 Restriccion
- R: ex1 Excepcion —exceptua→ r4 Restriccion
- Omisión `formula` [exacta]: «conforme a la siguiente exSSFA(KA) presión:» — La expresión del promedio ponderado no se extrajo del PDF; no se reconstruye.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «i) a iii) según D, A y KA» (i)) | `condicion_con_relacion` |  | c1 Condicion «D menor o igual a KA» —condicion_de→ ob1 Obligacion |
| 2 | «i) a iii) según D, A y KA» (ii)) | `condicion_con_relacion` |  | c2 Condicion «A mayor o igual a KA» —condicion_de→ ob2 Obligacion |
| 3 | «i) a iii) según D, A y KA» (iii)) | `condicion_con_relacion` |  | c3 Condicion «KA entre A y D» —condicion_de→ ob3 Obligacion |
| 4 | «si no existiera la posición pari passu» | `dentro_de_norma` |  | dentro de la Obligacion ob4 (descripción «o, si no existiera, del tramo subordinado más próximo») |
| 5 | «mínimos por STC» | `dentro_de_norma` |  | dentro de las Restricciones r1 a r4; sin Condicion |
| 6 | «look-through menor que el mínimo» | `condicion_con_relacion` |  | ex1 Excepcion «RW look-through inferior al mínimo aplicable» (cláusula de excepción a los mínimos) —exceptua→ r1 a r4 Restriccion |

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

### Extracción (código K)

- **op1 Operacion** «Titulización STC» — Titulización calificada como simple, transparente y comparable (STC) a los fines del ponderador del enfoque estandarizado · props: `{"tipo": "titulizacion"}` · tramo [exacta]: «Criterios para la determinación de titulizaciones simples, transparentes y comparables.»
- **c1 Condicion** «Activos homogéneos con flujos identificados» — Criterio STC: subyacentes homogéneos en tipo, jurisdicción, legislación y moneda; flujos contractualmente identificados, periódicos y solo principal e intereses o arrendamientos financieros. Homogeneidad evaluada según principios a) a d): sin perfiles de riesgo sustancialmente diferentes, factores comunes, obligaciones estándares con flujo periódico, reembolso principalmente del producido y no de … · tramo [exacta]: «Los activos subyacentes deberán estar constituidos por documentos a cobrar o derechos de crédito de carácter homogéneo en cuanto a su tipo, jurisdicción, legislación aplicable y moneda»
- **c2 Condicion** «Tasas de referencia de mercado» — Criterio STC: tasas de referencia de mercado y de fácil consulta, evitando fórmulas complejas o derivados exóticos; topes y pisos de tasa no son necesariamente derivados exóticos. · tramo [exacta]: «Las tasas de interés o de descuento de referencia deberán ser tasas de interés de mercado y de fácil consulta»
- **p1 Potestad** «Refinanciación o venta de subyacentes admitida» — Se podrá contar con la refinanciación o venta de los subyacentes · tramo [exacta]: «Se podrá contar con la refinanciación o venta de los subyacentes»
- **c3 Condicion** «Refinanciaciones suficientemente distribuidas» — Operaciones a refinanciar suficientemente distribuidas en el conjunto de activos titulizados · tramo [exacta]: «siempre que las operaciones a refinanciar estén suficientemente distribuidas en el conjunto de los activos titulizados»
- **c4 Condicion** «Valores residuales no significativos» — Valores residuales no significativos · tramo [exacta]: «que sus valores residuales no sean significativos»
- **c5 Condicion** «Información verificable de pérdidas e incumplimientos» — Criterio STC: información verificable sobre pérdidas e incumplimientos de activos similares por período suficientemente prolongado; fuentes y datos disponibles para todos los participantes del mercado. · tramo [exacta]: «Se deberá contar con información verificable sobre pérdidas e incumplimientos»
- **o1 Obligacion** «Evaluación de antecedentes por el inversor» — El inversor deberá poder evaluar en su debida diligencia si originante, fiduciario, administrador u otros cuentan con antecedentes probados; no es condición para cumplir el criterio. · props: `{"tipo": "otra"}` · no definidas: `{"no_condicion": "Esta consideración no será condición para dar cum-\nplimiento con el presente criterio."}` · tramo [exacta]: «El inversor, además, deberán poder evaluar»
- **c6 Condicion** «Experiencia suficiente del originante y acreedor» — Criterio STC: originante y acreedor inicial con experiencia suficiente en financiaciones similares. · tramo [exacta]: «El originante de la titulización, así como el acreedor inicial de los créditos titulizados, deberán contar con experiencia suficiente»
- **o2 Obligacion** «Desempeño 5 años — exposiciones minoristas» — El inversor deberá determinar la experiencia e historial del originante y acreedor inicial; verificación mínima de 5 años para exposiciones minoristas del punto 2.8.1 que cumplan 2.8.3.1. · props: `{"tipo": "otra"}` · umbral: ['durante un período mínimo de 5 años'] · tramo [exacta]: «El desempeño se deberá verificar durante un período mínimo de 5 años en el caso de las exposiciones minoristas»
- **o3 Obligacion** «Desempeño 7 años — resto de exposiciones» — Para el resto de las exposiciones, el desempeño deberá verificarse durante 7 años. · props: `{"tipo": "otra"}` · umbral: ['durante 7 años'] · tramo [exacta]: «Para el resto de las exposiciones, el desempeño deberá verificarse durante 7 años.»
- **op2 Operacion** «Transferencia de activos a la titulización» — Transferencia de activos subyacentes a la titulización · props: `{"tipo": "transferencia de activos"}` · tramo [exacta]: «no se podrán transferir activos»
- **r1 Restriccion** «Prohibido transferir activos en mora o deteriorados» — No se podrán transferir activos en incumplimiento o mora, con evidencia de incremento sustancial de pérdidas esperadas o en gestión de cobranza. · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «no se podrán transferir activos en situación de incumplimiento o mora»
- **o4 Obligacion** «Verificar ausencia de quiebra en 3 años» — Originante o fiduciario deberá verificar que el obligado no tuvo quiebra o reestructuración en los 3 años previos a la originación. · props: `{"tipo": "otra"}` · umbral: ['en los 3 años previos a la fecha de originación'] · tramo [exacta]: «El originante o fiduciario deberá verificar que los activos cumplan con las siguientes condiciones: […] El obligado al pago no ha sido sometido a un proceso de quiebra o de reestructuración de deuda debido a dificultades financieras en los 3 años previos a la fecha de originación»
- **x1 Excepcion** «Período de 2 años Ley 25.326» — Se aplica el período de 2 años del art. 26 inc. 4 Ley 25.326 en lugar de 3 años. · umbral: ['el período de 2 años'] · tramo [exacta]: «salvo que resulte de aplicación el período de 2 años previsto en el art. 26, inciso 4, de la Ley 25.326»
- **o5 Obligacion** «Verificar historial de crédito no desfavorable» — Verificar que el obligado no tenga historial desfavorable en registro público de crédito. · props: `{"tipo": "otra"}` · tramo [exacta]: «El originante o fiduciario deberá verificar que los activos cumplan con las siguientes condiciones: […] El obligado al pago no cuenta con un historial de crédito desfavorable en algún registro público de crédito.»
- **o6 Obligacion** «Verificar calificación o scoring sin riesgo» — Verificar que no haya calificación o credit scoring que anticipe riesgo de incumplimiento significativo. · props: `{"tipo": "otra"}` · tramo [exacta]: «El originante o fiduciario deberá verificar que los activos cumplan con las siguientes condiciones: […] El obligado al pago no cuenta con una evaluación de una agencia de calificación de créditos o un credit scoring que anticipen un riesgo de incumplimiento significativo.»
- **o7 Obligacion** «Verificar ausencia de litigios» — Verificar que el crédito no sea objeto de litigio entre obligado y acreedor original. · props: `{"tipo": "otra"}` · tramo [exacta]: «El originante o fiduciario deberá verificar que los activos cumplan con las siguientes condiciones: […] El documento a cobrar o derecho de crédito transferido no es objeto de litigios entre el obligado y el acreedor original.»
- **o8 Obligacion** «Análisis dentro de 45 días previos» — Análisis dentro de los 45 días previos a la transferencia; sin evidencia de deterioro al evaluar. · props: `{"tipo": "otra"}` · umbral: ['dentro de los 45 días previos a la fecha de la transferencia'] · tramo [exacta]: «El análisis de estas condiciones deberá ser llevado a cabo por el originante o fiduciario dentro de los 45 días previos a la fecha de la transferencia»
- **c7 Condicion** «Al menos un pago registrado» — Criterio STC: al incluir el activo, al menos un pago registrado. · props: `{"umbrales": [{"tramo": "al menos un pago", "comparacion": "minimo_inclusivo", "base": "un pago", "regla_comparacion": "limite_relativo:compuesta:al_menos", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['al menos un pago'] · tramo [exacta]: «deberá haberse registrado al menos un pago»
- **x2 Excepcion** «Activos rotativos exentos del primer pago» — Estructuras sobre activos rotativos (tarjetas, facturas, cancelables en un pago) exceptuadas del requisito de un pago registrado. · tramo [exacta]: «excepto en el caso de las estructuras sobre activos de tipo rotativos»
- **o9 Obligacion** «Demostrar originación uniforme al inversor» — El originante deberá demostrar al inversor originación en curso normal bajo estándares uniformes y consistentes. · props: `{"tipo": "comunicacion_a_cliente"}` · tramo [exacta]: «El originante deberá demostrar al inversor que los activos transferidos han sido generados en el curso normal de su negocio»
- **o10 Obligacion** «Comunicar cambios en estándares de originación» — Ante cambios en los estándares, comunicar momento y propósito. · props: `{"tipo": "comunicacion_a_cliente"}` · tramo [exacta]: «el originante deberá comunicar el momento y el propósito de las modificaciones»
- **r2 Restriccion** «Estándares no menos rigurosos que retenidos» — Estándares de originación no menos rigurosos que los de activos retenidos. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «Los estándares no deberán ser menos rigurosos que aquellos aplicados a los activos retenidos por el originante.»
- **c8 Condicion** «Criterios de originación sólidos y prudentes» — Criterio STC: originación sólida con evaluación de capacidad de pago; en carteras atomizadas, curso normal del negocio y flujos que atiendan obligaciones en estrés. · tramo [exacta]: «deberán satisfacer criterios de originación sólidos y prudentes»
- **o11 Obligacion** «Revisar estándares de terceros cedentes» — Si los activos se adquirieron a terceros, revisar sus estándares y constatar evaluación de los obligados por el acreedor original. · props: `{"tipo": "otra"}` · tramo [exacta]: «el originante/fiduciario de la titulización deberá revisar los estándares de originación de esos terceros»
- **c9 Condicion** «Activos adquiridos a terceros» — Activos adquiridos a terceros · tramo [exacta]: «Cuando los activos hayan sido adquiridos a terceros»
- **r3 Restriccion** «Sin gestión activa discrecional de cartera» — Sin selección discrecional ni gestión activa, incluso para activos transferidos tras la titulización; selección con criterios de elegibilidad definidos. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «El desempeño de la titulización no deberá depender de una selección de los subyacentes a través de la gestión activa y discrecional de la cartera.»
- **c10 Condicion** «Cesión efectiva: deuda de los obligados» — Transferencia real: créditos constituyen deuda de los obligados y consta en cláusulas. · tramo [exacta]: «deberá realizarse una cesión efectiva de derechos de forma tal que los documentos a cobrar y derechos de crédito: […] constituyan una deuda de los respectivos obligados»
- **c11 Condicion** «Cesión efectiva: fuera del alcance del cedente» — Transferencia real: fuera del alcance del cedente y sin riesgo de modificación o restitución. · tramo [exacta]: «deberá realizarse una cesión efectiva de derechos de forma tal que los documentos a cobrar y derechos de crédito: […] estén fuera del alcance del cedente, sus acreedores o liquidadores»
- **c12 Condicion** «Cesión efectiva: no sintética» — Transferencia real: cesión de créditos, no mediante CDS, derivado o garantía. · tramo [exacta]: «deberá realizarse una cesión efectiva de derechos de forma tal que los documentos a cobrar y derechos de crédito: […] hayan sido objeto de una cesión de créditos»
- **c13 Condicion** «Cesión efectiva: no retitulización» — Transferencia real: derecho contra el último obligado y no retitulización. · tramo [exacta]: «deberá realizarse una cesión efectiva de derechos de forma tal que los documentos a cobrar y derechos de crédito: […] proporcionen un efectivo derecho contra el último obligado»
- **o12 Obligacion** «Cláusula de garantía de libre gravamen» — Contrato de cesión con cláusula del originante garantizando créditos libres de gravamen. · props: `{"tipo": "otra"}` · tramo [exacta]: «El contrato de cesión de los créditos deberá contener cláusulas por las cuales el originante garantice»
- **o13 Obligacion** «Opinión legal independiente sobre transferencia real» — Opinión legal independiente sobre transferencia real conforme a) a d). · props: `{"tipo": "otra"}` · tramo [exacta]: «La documentación que instrumente la titulización deberá incluir una opinión legal independiente»
- **o14 Obligacion** «Demostrar obstáculos legales e informar» — Si la legislación no se ajusta a a) a d), demostrar obstáculos, especificar método de los inversores e informar eventos que retrasen la transferencia. · props: `{"tipo": "otra"}` · tramo [exacta]: «se deberá demostrar la existencia de los obstáculos que así lo impiden»
- **c14 Condicion** «Legislación no ajustada a apartados a-d» — Legislación aplicable no ajustada a a) a d) · tramo [exacta]: «En el caso de que la legislación aplicable a la titulización no se ajuste a lo previsto en los apartados a) a d) precedentes»
- **o15 Obligacion** «Información inicial por préstamo» — Información suficiente por préstamo o resumida por tramo en carteras atomizadas, previo a la inversión. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «se deberá contar con suficiente información a nivel de cada préstamo»
- **o16 Obligacion** «Información trimestral a inversores» — Suministrar al menos trimestralmente datos por préstamo o por tramo e informes estandarizados; fechas de corte alineadas. · props: `{"tipo": "presentacion_informativa", "frecuencia": "trimestral"}` · tramo [exacta]: «se deberá suministrar al menos trimestralmente durante la vida de la titulización datos»
- **o17 Obligacion** «Revisión cartera inicial por contador independiente» — Cartera inicial revisada por contador público independiente. · props: `{"tipo": "otra"}` · tramo [exacta]: «la cartera inicial deberá ser revisada por un contador público independiente»
- **cm1 Comunicacion** «Ley 25.326» —  · props: `{"codigo": "Ley 25.326", "tipo": "externa"}` · tramo [exacta]: «Ley 25.326»
- R: to TextoOrdenado —referencia→ cm1 Comunicacion
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: c2 Condicion —condicion_de→ op1 Operacion
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: c4 Condicion —condicion_de→ p1 Potestad
- R: c5 Condicion —condicion_de→ op1 Operacion
- R: c6 Condicion —condicion_de→ op1 Operacion
- R: c7 Condicion —condicion_de→ op1 Operacion
- R: c8 Condicion —condicion_de→ op1 Operacion
- R: c9 Condicion —condicion_de→ o11 Obligacion
- R: c10 Condicion —condicion_de→ op1 Operacion
- R: c11 Condicion —condicion_de→ op1 Operacion
- R: c12 Condicion —condicion_de→ op1 Operacion
- R: c13 Condicion —condicion_de→ op1 Operacion
- R: c14 Condicion —condicion_de→ o14 Obligacion
- R: r1 Restriccion —prohibe→ op2 Operacion
- R: r2 Restriccion —limita→ op1 Operacion
- R: r3 Restriccion —limita→ op1 Operacion
- R: x1 Excepcion —exceptua_obligacion→ o4 Obligacion
- R: o8 Obligacion —condiciona→ op2 Operacion
- R: o12 Obligacion —regula→ op2 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto (mención «El inversor»)
- R: o2 Obligacion —aplica_a→ Sujeto (mención «El inversor»)
- R: o4 Obligacion —aplica_a→ Sujeto (mención «El originante o fiduciario»)
- R: o5 Obligacion —aplica_a→ Sujeto (mención «El originante o fiduciario»)
- R: o6 Obligacion —aplica_a→ Sujeto (mención «El originante o fiduciario»)
- R: o7 Obligacion —aplica_a→ Sujeto (mención «El originante o fiduciario»)
- R: o8 Obligacion —aplica_a→ Sujeto (mención «el originante o fiduciario»)
- R: o9 Obligacion —aplica_a→ Sujeto (mención «El originante»)
- R: o10 Obligacion —aplica_a→ Sujeto (mención «el originante»)
- R: o11 Obligacion —aplica_a→ Sujeto (mención «el originante/fiduciario de la titulización»)
- Omisión `meta_normativo` [exacta]: «Ello para evitar, por ejemplo, que se originen carteras con el solo fin de transferirlas.» — Finalidad
- Omisión `fuera_de_tipos` [exacta]: «En la medida en que la selección no sea discrecional, la incorporación de créditos en los períodos de rotación o su sustitución o recompra debido al incumplimiento de cláusulas contractuales no se considerará una gestión activa de la cartera.» — Delimitación de 'gestión activa'; habría sido Definicion/Excepcion de r3
- Omisión `fuera_de_tipos` [exacta]: «Los inversores deberían poder evaluar el riesgo crediticio de la cartera de activos en forma previa a sus decisiones de inversión.» — Expectativa sobre inversores; Obligacion recomendada

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «refinanciación distribuida» | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ p1 Potestad |
| 2 | «valores residuales no significativos» | `condicion_con_relacion` |  | c4 Condicion —condicion_de→ p1 Potestad |
| 3 | «minoristas 5 años» | `dentro_de_norma` |  | dentro de la Obligacion o2 («Desempeño 5 años — exposiciones minoristas») |
| 4 | «resto 7» | `dentro_de_norma` |  | dentro de la Obligacion o3 |
| 5 | «salvo el período de 2 años» | `condicion_con_relacion` |  | x1 Excepcion «Período de 2 años Ley 25.326» (cláusula de excepción) —exceptua_obligacion→ o4 Obligacion |
| 6 | «condiciones a) a d)» (a)) | `dentro_de_norma` |  | extraída como norma de otro tipo: o4 Obligacion «Verificar ausencia de quiebra en 3 años» |
| 7 | «condiciones a) a d)» (b)) | `dentro_de_norma` |  | o5 Obligacion «Verificar historial de crédito no desfavorable» |
| 8 | «condiciones a) a d)» (c)) | `dentro_de_norma` |  | o6 Obligacion «Verificar calificación o scoring sin riesgo» |
| 9 | «condiciones a) a d)» (d)) | `dentro_de_norma` |  | o7 Obligacion «Verificar ausencia de litigios» |

## `cap::3.1.2.2` — Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos.
> *heredado:* 3.1. Tratamiento de las titulizaciones.
> *heredado:* Se denomina "posición de titulización" a la exposición a una titulización (o retitulización), tradicional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes conceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos ("AssetBacked Securities", ABS) y bonos de titulización hipotecaria ("Mortgage-Backed Securities", MBS)–, mejoras crediticias, facilidades de liquidez, "swaps" de tasa de interés o de monedas y derivados de crédito. Las reservas ("reserve accounts"), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo también el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad económica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una determinada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> *heredado:* 3.1.2. Entidad financiera originante.
> *propio:* 3.1.2.2. Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional sólo si se satisface la totalidad de los siguientes requisitos operativos –debiendo computar exigencia de capital por las posiciones de titulización que conserve–: i) Se ha transferido a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas. ii) La entidad cedente no mantiene un control directo ni indirecto (como ser a través de una sociedad controlada) sobre las exposiciones transferidas. Ellas han sido aisladas de la cedente a los efectos jurídicos de forma tal que están fuera de su alcance y del de sus acreedores, incluso en los casos de liquidación o quiebra. Estas condiciones deberán estar avaladas por dictamen jurídico. Se considera que la cedente mantiene el control efectivo de las exposiciones transferidas si: a) puede recomprarlas con el objeto de realizar sus beneficios, o b) está obligada a conservar su riesgo. El mantenimiento por parte de la cedente de la administración de las exposiciones subyacentes no implicará un control indirecto sobre ellas. iii) Los títulos valores emitidos no son obligaciones de la cedente. En consecuencia, los inversores que compren los títulos valores sólo deberán tener derechos frente al conjunto subyacente de exposiciones. iv)La cesión se ha efectuado a un "Ente de Propósito Especial" (SPE) y los inversores pueden gravar o enajenar sus títulos valores sin restricción. v) Las opciones de exclusión satisfacen las condiciones estipuladas en el punto 3.1.4. vi)La titulización no contiene cláusulas mediante las cuales: a) se obligue a la originante a alterar las exposiciones subyacentes con el objeto de mejorar su calidad crediticia, a menos que esto se logre mediante su venta –a precios de mercado– a terceros no vinculados a ésta; b) la entidad financiera deba incrementar su posición a primera pérdida –es decir, su exposición al tramo que absorbe las pérdidas en primer término– o aumentar las mejoras crediticias provistas, con posterioridad al inicio de la operación; o c) se aumente el rendimiento pagadero a las partes distintas de la originante, como pueden ser los inversores o terceros proveedores de mejoras crediticias, en respuesta a un deterioro de la calidad crediticia de las exposiciones subyacentes. vii) No se incluyen opciones de rescisión o eventos desencadenantes de la extinción del contrato –excepto que se trate de opciones de exclusión admitidas (punto 3.1.4.) o que la extinción se deba a cambios impositivos o regulatorios específicos–, ni se incluyen cláusulas de amortización anticipada que –de acuerdo con lo previsto en el punto 3.1.8.1.– impliquen que la titulización no cumple con los requerimientos operacionales del presente punto.

### Extracción (código K)

- **op1 Operacion** «Exclusión de exposiciones titulizadas del cálculo APR» — Exclusión, por la entidad originante, de las exposiciones objeto de una titulización tradicional al calcular los activos ponderados por riesgo · props: `{"tipo": "cálculo de activos ponderados por riesgo"}` · tramo [exacta]: «Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional»
- **p1 Potestad** «Facultad de excluir exposiciones de titulización tradicional» — La entidad originante podrá excluir del cálculo de activos ponderados por riesgo las exposiciones objeto de una titulización tradicional sólo si se satisfacen todos los requisitos operativos i) a vii). · tramo [exacta]: «la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional sólo si se satisface la totalidad de los siguientes requisitos operativos»
- **o1 Obligacion** «Exigencia por posiciones de titulización conservadas» — La entidad originante que excluya las exposiciones debe computar exigencia de capital por las posiciones de titulización que conserve. · props: `{"tipo": "calculo"}` · tramo [exacta]: «debiendo computar exigencia de capital por las posiciones de titulización que conserve»
- **c1 Condicion** «Transferencia del riesgo de crédito a terceros» — Requisito i): el riesgo de crédito de las exposiciones titulizadas se transfirió a uno o más terceros. · tramo [exacta]: «Se ha transferido a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas.»
- **c2 Condicion** «Ausencia de control directo o indirecto de la cedente» — Requisito ii): la cedente no mantiene control directo ni indirecto sobre las exposiciones transferidas. · tramo [exacta]: «La entidad cedente no mantiene un control directo ni indirecto (como ser a través de una sociedad controlada) sobre las exposiciones transferidas.»
- **c3 Condicion** «Aislamiento jurídico de las exposiciones transferidas» — Requisito ii): exposiciones aisladas jurídicamente de la cedente y de sus acreedores, incluso en liquidación o quiebra. · tramo [exacta]: «Ellas han sido aisladas de la cedente a los efectos jurídicos de forma tal que están fuera de su alcance y del de sus acreedores, incluso en los casos de liquidación o quiebra.»
- **c4 Condicion** «Dictamen jurídico que avale las condiciones» — Requisito ii): la falta de control y el aislamiento deben estar avalados por dictamen jurídico. · tramo [exacta]: «Estas condiciones deberán estar avaladas por dictamen jurídico.»
- **d1 Definicion** «Control efectivo de la cedente» — La cedente mantiene el control efectivo de las exposiciones transferidas si a) puede recomprarlas para realizar sus beneficios, o b) está obligada a conservar su riesgo. Mantener la administración de las exposiciones subyacentes no implica control indirecto. · props: `{"termino": "control efectivo"}` · tramo [exacta]: «Se considera que la cedente mantiene el control efectivo de las exposiciones transferidas si:»
- **c5 Condicion** «Títulos no son obligaciones de la cedente» — Requisito iii): los títulos emitidos no son obligaciones de la cedente; los inversores sólo tienen derechos frente al conjunto subyacente de exposiciones. · tramo [exacta]: «Los títulos valores emitidos no son obligaciones de la cedente.»
- **c6 Condicion** «Cesión a un Ente de Propósito Especial» — Requisito iv): la cesión se efectuó a un SPE. · tramo [exacta]: «La cesión se ha efectuado a un "Ente de Propósito Especial" (SPE)»
- **c7 Condicion** «Libre gravamen o enajenación de títulos por inversores» — Requisito iv): los inversores pueden gravar o enajenar sus títulos sin restricción. · tramo [no]: «los inversores pueden gravar o enajenar sus títulos valores sin restricción»
- **c8 Condicion** «Opciones de exclusión conformes al punto 3.1.4» — Requisito v): las opciones de exclusión cumplen el punto 3.1.4. · tramo [exacta]: «Las opciones de exclusión satisfacen las condiciones estipuladas en el punto 3.1.4.»
- **c9 Condicion** «Sin cláusula de alterar exposiciones para mejorar calidad» — Requisito vi.a): la titulización no contiene cláusulas que obliguen a la originante a alterar las exposiciones subyacentes para mejorar su calidad crediticia, salvo mediante venta a precios de mercado a terceros no vinculados. · tramo [no]: «se obligue a la originante a alterar las exposiciones subyacentes con el objeto de mejorar su calidad crediticia, a menos que esto se logre mediante su venta –a precios de mercado– a terceros no vinculados a ésta»
- **c10 Condicion** «Sin cláusula de incrementar primera pérdida o mejoras» — Requisito vi.b): no hay cláusulas por las que la entidad deba incrementar su posición a primera pérdida o aumentar las mejoras crediticias provistas después del inicio de la operación. · tramo [exacta]: «la entidad financiera deba incrementar su posición a primera pérdida»
- **c11 Condicion** «Sin cláusula de aumentar rendimiento ante deterioro» — Requisito vi.c): no hay cláusulas que aumenten el rendimiento pagadero a partes distintas de la originante en respuesta a un deterioro de la calidad crediticia de las exposiciones subyacentes. · tramo [exacta]: «se aumente el rendimiento pagadero a las partes distintas de la originante»
- **c12 Condicion** «Sin opciones de rescisión ni eventos de extinción» — Requisito vii): no se incluyen opciones de rescisión ni eventos de extinción del contrato, excepto opciones de exclusión admitidas (punto 3.1.4.) o extinción por cambios impositivos o regulatorios específicos. · tramo [no]: «No se incluyen opciones de rescisión o eventos desencadenantes de la extinción del contrato»
- **c13 Condicion** «Sin amortización anticipada incumplidora (punto 3.1.8.1)» — Requisito vii): no se incluyen cláusulas de amortización anticipada que, según el punto 3.1.8.1., impliquen incumplir los requerimientos operacionales. · tramo [exacta]: «ni se incluyen cláusulas de amortización anticipada que –de acuerdo con lo previsto en el punto 3.1.8.1.– impliquen que la titulización no cumple con los requerimientos operacionales del presente punto»
- R: p1 Potestad —aplica_a→ Sujeto_entidad_originante_de_transferencia (mención «la entidad originante»)
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_originante_de_transferencia (mención «la entidad originante»)
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
- R: c13 Condicion —condicion_de→ p1 Potestad
- Omisión `relacion_sin_predicado` [exacta]: «podrá excluir las exposiciones objeto de una titulización tradicional» — Vínculo Potestad→Operacion (habilita); no hay predicado

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

### Extracción (código K)

- **e1 Definicion** «Miembro compensador (clearing member)» — Miembro (participante directo) de la CCP habilitado para realizar transacciones con dicha CCP, ya sea por cuenta propia o como intermediario entre la CCP y otros participantes del mercado. · props: `{"termino": "Miembro compensador"}` · tramo [exacta]: «Miembro compensador ("clearing member"): es un miembro –participante directo– de la CCP habilitado para realizar transacciones con dicha CCP, ya sea por cuenta propia o como intermediario entre la CCP y otros participantes del mercado.»
- **e2 Definicion** «Segunda CCP vinculada como miembro compensador» — A los efectos del cálculo de la exigencia de capital, cuando una CCP tenga vínculos con una segunda CCP, ésta será considerada miembro compensador respecto de la primera. · props: `{"termino": "miembro\ncompensador"}` · tramo [exacta]: «cuando una CCP tenga vínculos con una segunda CCP ésta será considerada como miembro compensador respecto de la primera»
- **e3 Condicion** «CCP con vínculos con segunda CCP» — Supuesto: una CCP tiene vínculos con una segunda CCP. · tramo [exacta]: «cuando una CCP tenga vínculos con una segunda CCP»
- **e4 Definicion** «Tratamiento de garantías entre CCP vinculadas» — Según los acuerdos entre ambas CCP, las garantías aportadas por la segunda a la primera se tratan como margen inicial o como contribución a un fondo de garantía constituido para hacer frente a incumplimientos (default fund). · props: `{"termino": "garantías aportadas por la segunda a la primera"}` · tramo [exacta]: «Dependerá de los acuerdos entre ambas que las garantías aportadas por la segunda a la primera sean tratadas como margen inicial o contribución a un fondo de garantía»
- Omisión `relacion_sin_predicado` [exacta]: «cuando una CCP tenga vínculos con una segunda CCP ésta será considerada como miembro compensador» — condicion_de no admite Definicion como rango

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:21 | sí | «A los efectos del cálculo de la exigencia de capital» | `ausente` |  | ningún tramo contiene «A los efectos del cálculo…»; la omisión relacion_sin_predicado refiere a «cuando una CCP tenga vínculos…» |

## `cap::5.2.1.3` — No deberá existir una correlación positiva sustancial entre la calidad crediticia

Grupos: omisiones.

### Texto

> *heredado:* Sección 5. Cobertura del riesgo de crédito.
> *heredado:* A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las técnicas previstas en el punto 5.1. La presente sección contempla, además, el cálculo de la exposición a las operaciones de financiación con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sección 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.
> *heredado:* 5.2. Requisitos para la aplicación de técnicas de coberturas del riesgo de crédito.
> *heredado:* 5.2.1. Requisitos generales.
> *propio:* 5.2.1.3. No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía –por ejemplo, los títulos valores emitidos por la contraparte o un vinculado a ella, no son admisibles–.

### Extracción (código K)

- **e1 Operacion** «Aplicación de técnicas de cobertura del riesgo de crédito» — Reconocimiento de la cobertura del riesgo de crédito mediante técnicas CRC a los efectos del cómputo de la exigencia de capital · props: `{"tipo": "cobertura del riesgo de crédito"}` · tramo [exacta]: «Requisitos para la aplicación de técnicas de coberturas del riesgo de crédito»
- **e2 Restriccion** «Sin correlación positiva sustancial contraparte-garantía — CRC» — Requisito general para aplicar técnicas CRC: no deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía»
- **e3 Restriccion** «Inadmisibles títulos de la contraparte o vinculado — garantía CRC» — Como ejemplo de correlación positiva sustancial, los títulos valores emitidos por la contraparte o un vinculado a ella no son admisibles como garantía para la cobertura del riesgo de crédito. · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «los títulos valores emitidos por la contraparte o un vinculado a ella, no son admisibles»
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

### Extracción (código K)

- **op1 Operacion** «Cómputo exigencia riesgo tasa — derivados» — Cálculo de la exigencia de capital por riesgo de tasa de interés (específico y general de mercado) para posiciones en instrumentos derivados · props: `{"tipo": "calculo"}` · tramo [exacta]: «Exigencia de capital por derivados.»
- **p1 Potestad** «Exclusión posiciones en idénticos instrumentos» — Las posiciones compradas y vendidas, reales o nocionales, en idénticos instrumentos se podrán excluir del cómputo del riesgo específico y general de mercado. · tramo [exacta]: «Las posiciones compradas y vendidas, reales o nocionales, en idénticos instrumentos se podrán excluir del cómputo del riesgo específico y del riesgo general de mercado.»
- **d1 Definicion** «Instrumentos idénticos» — Tienen igual emisor, cupón, moneda y vencimiento. · props: `{"termino": "instrumentos son idénticos"}` · tramo [exacta]: «Se entiende que los instrumentos son idénticos si tienen igual emisor, cupón, moneda y vencimiento.»
- **p2 Potestad** «Exclusión futuros/forwards y subyacentes correspondientes» — Se podrán excluir futuros o forwards y sus subyacentes si se corresponden exactamente, sin dejar de computar el lado que representa el plazo hasta el vencimiento de la operación a término. · tramo [exacta]: «si se corresponden exactamente, se podrán excluir los futuros o "forwards" y sus subyacentes, pero sin dejar de computar el lado de la operación que representa el plazo hasta el vencimiento de la operación a término.»
- **c1 Condicion** «Correspondencia exacta futuro-subyacente» — Que el futuro o forward y su subyacente se correspondan exactamente. · tramo [exacta]: «si se corresponden exactamente»
- **c2 Condicion** «Identificación del cheapest-to-deliver — gama entregable» — Cuando el futuro o forward permita entregar una gama de instrumentos, la exclusión solo procede si la entidad puede identificar fácilmente el título subyacente más conveniente de entregar. · tramo [exacta]: «la exclusión sólo será posible en la medida que la entidad pueda identificar fácilmente el título subyacente cuya entrega es más conveniente para el intermediario con la posición vendida»
- **c3 Condicion** «Precios cheapest-to-deliver y futuro alineados» — Demostrar que los cambios de precios del título más barato y del futuro o forward están estrechamente alineados. · tramo [exacta]: «demostrar que los cambios de los precios del título más barato ("cheapest-to-deliver") y del futuro o "forward" están estrechamente alineados»
- **r1 Restriccion** «Prohibida compensación entre distintas monedas» — No se permitirá la exclusión o compensación de posiciones en diferentes monedas. · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «No se permitirá la exclusión o compensación de posiciones en diferentes monedas»
- **o1 Obligacion** «Swaps y contratos de monedas como nocionales» — Los lados de swaps de monedas y contratos a término sobre monedas se tratarán como posiciones nocionales e incluirán en el cálculo de cada moneda. · props: `{"tipo": "calculo"}` · tramo [exacta]: «los lados de los "swaps" de monedas y de los contratos a término sobre monedas se deberán tratar como posiciones nocionales en los instrumentos pertinentes e incluirse en el cálculo correspondiente a cada moneda.»
- **p3 Potestad** «Exclusión posiciones opuestas misma categoría» — Las entidades podrán excluir posiciones opuestas en la misma categoría de instrumentos si consideran que están compensadas, incluso posiciones en el valor delta de una opción. · tramo [exacta]: «las entidades podrán excluir posiciones opuestas en la misma categoría de instrumentos si consideran que están compensadas»
- **p4 Potestad** «Compensación de lados de swaps diferentes» — Sujeto a las mismas condiciones, se podrán compensar los lados de swaps diferentes. · tramo [exacta]: «Sujeto a las mismas condiciones, también se podrán compensar los lados de "swaps" diferentes.»
- **c4 Condicion** «Mismos subyacentes» — Las posiciones deben referirse a los mismos subyacentes. · tramo [exacta]: «las posiciones se deberán referir a los mismos subyacentes»
- **c5 Condicion** «Mismo valor nominal» — Las posiciones deben tener el mismo valor nominal. · tramo [exacta]: «tener el mismo valor nominal»
- **c6 Condicion** «Misma moneda de denominación» — Las posiciones deben estar denominadas en la misma moneda. · tramo [exacta]: «estar denominadas en la misma moneda»
- **c7 Condicion** «Futuros: productos idénticos» — En futuros, la exclusión solo procede si nocionales y subyacentes refieren a productos idénticos. · tramo [exacta]: «cuando se trate de futuros, la exclusión sólo procederá si los nocionales e instrumentos subyacentes refieren a productos idénticos»
- **c8 Condicion** «Futuros: vencimientos difieren hasta 7 días» — En futuros, los vencimientos no difieren en más de 7 días corridos. · umbral: ['no difieren en más de 7 días corridos'] · tramo [exacta]: «sus vencimientos no difieren en más de 7 días corridos»
- **c9 Condicion** «Swaps/FRAs: tasa de referencia idéntica» — En swaps y FRAs, la tasa de referencia de posiciones a interés variable debe ser idéntica. · tramo [exacta]: «cuando se trate de "swaps" y FRAs, la tasa de referencia de las posiciones a interés variable deberá ser idéntica»
- **c10 Condicion** «Swaps/FRAs: cupones dentro de 15 pb» — En swaps y FRAs, correspondencia cercana entre cupones dentro de 15 puntos básicos. · props: `{"umbrales": [{"tramo": "dentro de un margen de 15\npuntos básicos", "comparacion": "maximo_inclusivo", "base": "un margen de 15 puntos básicos", "regla_comparacion": "limite_relativo:compuesta:dentro_de", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['dentro de un margen de 15 puntos básicos'] · tramo [exacta]: «deberá haber una correspondencia cercana entre los cupones (dentro de un margen de 15 puntos básicos)»
- **c11 Condicion** «Reajuste menos de un mes: mismo día» — En swaps, FRAs y forwards, si la próxima fecha de reajuste o vencimiento es a menos de un mes, debe producirse el mismo día. · umbral: ['a menos de un mes'] · tramo [exacta]: «c) en los casos de "swaps", FRAs y "forwards", la próxima fecha de reajuste del interés o el vencimiento -cuando se trate de posiciones con cupón fijo o "forwards"- se deberá producir: […] a menos de un mes: en el mismo día»
- **c12 Condicion** «Reajuste entre un mes y un año: 7 días» — Entre un mes y un año, discrepancia máxima de siete días corridos entre fechas. · umbral: ['entre un mes y un año', 'con una discrepancia máxima entre esas fechas de siete días corridos'] · tramo [exacta]: «c) en los casos de "swaps", FRAs y "forwards", la próxima fecha de reajuste del interés o el vencimiento -cuando se trate de posiciones con cupón fijo o "forwards"- se deberá producir: […] entre un mes y un año: con una discrepancia máxima entre esas fechas de siete días corridos»
- **c13 Condicion** «Reajuste a un año: 30 días» — A un año, discrepancia máxima de treinta días corridos entre fechas. · props: `{"umbrales": [{"tramo": "con una discrepancia máxima entre esas fechas de trein-\nta días corridos", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['a un año', 'con una discrepancia máxima entre esas fechas de treinta días corridos'] · tramo [exacta]: «c) en los casos de "swaps", FRAs y "forwards", la próxima fecha de reajuste del interés o el vencimiento -cuando se trate de posiciones con cupón fijo o "forwards"- se deberá producir: […] a un año: con una discrepancia máxima entre esas fechas de treinta días corridos»
- **x1 Excepcion** «Swaps, FRAs, forwards y futuros tasa: sin riesgo específico» — Exceptúa de la exigencia por riesgo específico a swaps de monedas y tasas, FRAs, forwards de moneda y futuros de tasa o índice de tasa. · tramo [exacta]: «Los "swaps" de monedas y tasas de interés, los FRAs, los "forwards" de moneda y los futuros de tasa de interés o sobre un índice de tasa de interés no estarán sujetos a exigencia por riesgo específico.»
- **o2 Obligacion** «Futuros sobre títulos de deuda: riesgo específico» — Para futuros con subyacente título de deuda o índice de canasta de títulos de deuda, se aplica exigencia por riesgo específico según riesgo de crédito del emisor (punto 6.2.1). · props: `{"tipo": "calculo"}` · tramo [exacta]: «en el caso de futuros en los que el subyacente sea un título de deuda o un índice que represente una canasta de títulos de deuda, se aplicará la exigencia por riesgo específico acorde al riesgo de crédito del emisor»
- **o3 Obligacion** «Riesgo general de mercado sobre todos los derivados» — La exigencia por riesgo general de mercado alcanza a todas las posiciones en derivados, igual que a las posiciones al contado. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados»
- **x2 Excepcion** «Posiciones compensadas con idénticos: sin riesgo general» — Quedan fuera de la exigencia por riesgo general de mercado las posiciones compensadas con instrumentos idénticos conforme al acápite i). · tramo [exacta]: «con la sola excepción de las posiciones que estén compensadas con instrumentos idénticos»
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
- R: r1 Restriccion —prohibe→ op1 Operacion
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: x2 Excepcion —exceptua_obligacion→ o3 Obligacion
- Omisión `relacion_sin_predicado` [exacta]: «no estarán sujetos a exigencia por riesgo específico. No obstante» — o2 es contra-excepción a x1; no hay predicado Obligacion→Excepcion
- Omisión `relacion_sin_predicado` [exacta]: «no estarán sujetos a exigencia por riesgo específico» — la regla general de exigencia por riesgo específico no está en la unidad; habría usado exceptua_obligacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «instrumentos idénticos» | `dentro_de_norma` |  | dentro de la Potestad p1 y como Definicion d1; sin Condicion (c7 «productos idénticos» es el supuesto a) de futuros, no este) |
| 2 | «futuro con gama de instrumentos» | `condicion_con_relacion` |  | c2 Condicion (identificar el cheapest-to-deliver) y c3 —condicion_de→ p2 Potestad |
| 3 | «a) futuros a 7 días» | `condicion_con_relacion` |  | c8 Condicion con el umbral (y c7) —condicion_de→ p3 Potestad |
| 4 | «b) swaps y FRAs» | `condicion_con_relacion` |  | c9 y c10 Condicion (con el umbral de 15 pb) —condicion_de→ p3 Potestad |
| 5 | «c) tramos de fechas» | `condicion_con_relacion` |  | c11, c12 y c13 Condicion con los umbrales —condicion_de→ p3 Potestad |
| 6 | «futuros sobre títulos» | `dentro_de_norma` |  | extraído como norma de otro tipo: o2 Obligacion; sin Excepcion ni Condicion (la omisión declara la contra-excepción sin predicado) |

## `cap::6.3.2.2` — Exigencia de capital por derivados sobre acciones.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 6. Capital mínimo por riesgo de mercado.
> *heredado:* 6.3. Exigencia de capital por riesgo de posiciones en acciones.
> *heredado:* La exigencia de capital por el riesgo de mantener posiciones en acciones en la cartera de negociación alcanza a las posiciones compradas y vendidas en acciones ordinarias, títulos de deuda convertibles que se comporten como acciones y los compromisos para adquirir o vender acciones, así como en todo otro instrumento que tenga un comportamiento en el mercado similar al de las acciones, excluyendo a las acciones preferidas no convertibles, a las que se aplicará la exigencia por riesgo de tasa de interés descripta en el punto 6.2. Las posiciones compradas y vendidas en la misma especie podrán computarse en términos netos.
> *heredado:* 6.3.2. Tratamiento de los derivados sobre acciones.
> *heredado:* A excepción de las opciones sobre acciones e índices bursátiles, que se tratan en el punto 6.6., los restantes derivados sobre acciones y las posiciones fuera de balance sensibles a los cambios en los precios de mercado deberán incluirse en el cómputo de la exigencia. Esto comprende a los futuros, "forwards" y "swaps", tanto de acciones individuales como de índices bursátiles. Los derivados se convertirán en posiciones en su correspondiente subyacente.
> *propio:* 6.3.2.2. Exigencia de capital por derivados sobre acciones. i) Exigencia de capital por riesgo específico y por riesgo general de mercado. Cada posición compensada con una acción o índice bursátil idéntico podrá ser neteada en su totalidad, dando lugar a una única posición neta, vendida o comprada, sobre la que se aplicarán las exigencias de capital por riesgo específico y riesgo general de mercado. El riesgo de tasa de interés del derivado se computará conforme a lo indicado en el punto 6.2. ii) Exigencia de capital por índices. Además de la exigencia por riesgo general de mercado, se aplicará una exigencia de capital adicional de 2% de la posición neta, comprada o vendida, en contratos sobre índices calculados sobre carteras diversificadas de acciones a los efectos de cubrir factores tales como los riesgos de ejecución. Será objeto de revisión por parte de la Superintendencia de Entidades Financieras y Cambiarias que el ponderador de 2% se aplique sólo a índices bien diversificados y no, por ejemplo, a índices sectoriales. iii) Arbitraje. a) En el caso de las siguientes estrategias de arbitraje relacionadas con futuros, la exigencia de capital adicional de 2% del acápite ii) precedente se podrá aplicar sólo a uno de los índices (quedando exenta la posición contraria): - cuando la entidad asuma la posición contraria en exactamente el mismo índice pero a distintos vencimientos o mercados; - cuando la entidad mantenga la posición opuesta en contratos a idéntica fecha pero en índices diferentes, aunque similares, a cuyo efecto deberá tener a disposición de la Superintendencia de Entidades Financieras y Cambiarias evidencia de que ambos índices contienen suficientes componentes comunes como para justificar tal compensación. b) Se aplicará una exigencia de capital de 4% a las posiciones que surjan de estrategias de arbitraje, en las que un futuro sobre un índice amplio se calce con una canasta de acciones y, además, se verifique que: - la estrategia haya sido adoptada en forma deliberada y se vigile y gestione en forma particularizada; - la composición de la canasta de acciones represente al menos el 90% del índice si se descompone en sus componentes nocionales; - la exigencia de capital de 4%, que refleja los riesgos de divergencia y ejecución, equivale a una exigencia de 2% del valor bruto de las posiciones en cada lado. La exigencia es aplicable incluso si todas las acciones se mantienen en proporciones idénticas a las del índice. Cualquier valor excedente de las acciones que componen la canasta por encima del valor del futuro o cualquier valor excedente del futuro sobre el valor de la canasta se considerará como una posición abierta, comprada o vendida. c) Se podrán compensar –es decir, no aplicar exigencias de capital– posiciones contrarias, incluso tratándose de posiciones en mercados diferentes o de certificados de depósito de acciones sólo si se tienen en cuenta todos los costos de conversión, cuando los hubiera. Todo riesgo de tipo de cambio que surja de estas posiciones deberá computarse según se establece en el punto 6.4.

### Extracción (código K)

- **op1 Operacion** «Derivados sobre acciones — exigencia de capital» — Cómputo de la exigencia de capital por riesgo de posiciones en derivados sobre acciones e índices bursátiles · props: `{"tipo": "calculo de exigencia de capital"}` · tramo [exacta]: «Tratamiento de los derivados sobre acciones.»
- **p1 Potestad** «Neteo de posiciones compensadas idénticas» — Cada posición compensada con una acción o índice bursátil idéntico podrá netearse en su totalidad, dando lugar a una única posición neta sobre la que se aplican las exigencias por riesgo específico y general de mercado. · tramo [exacta]: «Cada posición compensada con una acción o índice bursátil idéntico podrá ser neteada en su totalidad»
- **o1 Obligacion** «Riesgo de tasa del derivado según 6.2» — El riesgo de tasa de interés del derivado sobre acciones se computa conforme al punto 6.2. · props: `{"tipo": "calculo"}` · tramo [exacta]: «El riesgo de tasa de interés del derivado se computará conforme a lo indicado en el punto 6.2.»
- **o2 Obligacion** «Exigencia adicional 2% — contratos sobre índices diversificados» — Además de la exigencia por riesgo general de mercado, exigencia adicional de 2% de la posición neta en contratos sobre índices de carteras diversificadas, para cubrir riesgos de ejecución; solo a índices bien diversificados, no sectoriales. · props: `{"tipo": "calculo"}` · umbral: ['exigencia de capital adicional de 2% de la posición neta'] · tramo [exacta]: «se aplicará una exigencia de capital adicional de 2% de la posición neta, comprada o vendida, en contratos sobre índices calculados sobre carteras diversificadas de acciones»
- **pt2 Potestad** «Revisión SEFyC del ponderador 2%» — La SEFyC revisa que el ponderador de 2% se aplique sólo a índices bien diversificados y no a índices sectoriales. · tramo [exacta]: «Será objeto de revisión por parte de la Superintendencia de Entidades Financieras y Cambiarias que el ponderador de 2% se aplique sólo a índices bien diversificados»
- **x1 Excepcion** «Arbitraje con futuros — 2% a un solo índice» — En estrategias de arbitraje con futuros, la exigencia adicional de 2% se aplica sólo a uno de los índices, quedando exenta la posición contraria. · tramo [exacta]: «la exigencia de capital adicional de 2% del acápite ii) precedente se podrá aplicar sólo a uno de los índices (quedando exenta la posición contraria)»
- **c1 Condicion** «Posición contraria mismo índice, distinto vencimiento/mercado» — Supuesto alternativo: posición contraria en el mismo índice a distintos vencimientos o mercados. · tramo [exacta]: «cuando la entidad asuma la posición contraria en exactamente el mismo índice pero a distintos vencimientos o mercados»
- **c2 Condicion** «Posición opuesta misma fecha, índices similares» — Supuesto alternativo: posición opuesta en contratos a idéntica fecha en índices diferentes pero similares. · tramo [exacta]: «cuando la entidad mantenga la posición opuesta en contratos a idéntica fecha pero en índices diferentes, aunque similares»
- **o3 Obligacion** «Evidencia de componentes comunes a disposición SEFyC» — Para compensar índices diferentes pero similares, la entidad debe tener a disposición de la SEFyC evidencia de que ambos contienen suficientes componentes comunes. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «deberá tener a disposición de la Superintendencia de Entidades Financieras y Cambiarias evidencia de que ambos índices contienen suficientes componentes comunes»
- **o4 Obligacion** «Exigencia 4% — arbitraje futuro índice vs canasta» — Exigencia de 4% (equivalente a 2% del valor bruto de cada lado) a posiciones de arbitraje futuro sobre índice amplio calzado con canasta de acciones; aplicable aun con proporciones idénticas; el excedente entre canasta y futuro se considera posición abierta. · props: `{"tipo": "calculo"}` · umbral: ['exigencia de capital de 4%', 'equivale a una exigencia de 2% del valor bruto de las posiciones en cada lado'] · tramo [exacta]: «Se aplicará una exigencia de capital de 4% a las posiciones que surjan de estrategias de arbitraje, en las que un futuro sobre un índice amplio se calce con una canasta de acciones»
- **c3 Condicion** «Estrategia deliberada y gestionada particularizadamente» — La estrategia debe ser deliberada y vigilada y gestionada en forma particularizada. · tramo [exacta]: «la estrategia haya sido adoptada en forma deliberada y se vigile y gestione en forma particularizada»
- **c4 Condicion** «Canasta representa al menos 90% del índice» — La canasta representa al menos el 90% del índice descompuesto en componentes nocionales. · umbral: ['al menos el 90% del índice'] · tramo [exacta]: «la composición de la canasta de acciones represente al menos el 90% del índice»
- **p3 Potestad** «Compensación de posiciones contrarias» — Se pueden compensar posiciones contrarias, incluso en mercados diferentes o certificados de depósito de acciones. · tramo [exacta]: «Se podrán compensar –es decir, no aplicar exigencias de capital– posiciones contrarias»
- **c5 Condicion** «Considerar todos los costos de conversión» — La compensación procede sólo si se consideran todos los costos de conversión. · tramo [exacta]: «sólo si se tienen en cuenta todos los costos de conversión, cuando los hubiera»
- **o5 Obligacion** «Riesgo de tipo de cambio según 6.4» — El riesgo de tipo de cambio de estas posiciones se computa según el punto 6.4. · props: `{"tipo": "calculo"}` · tramo [exacta]: «Todo riesgo de tipo de cambio que surja de estas posiciones deberá computarse según se establece en el punto 6.4.»
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o4 Obligacion —regula→ op1 Operacion
- R: o5 Obligacion —regula→ op1 Operacion
- R: x1 Excepcion —exceptua_obligacion→ o2 Obligacion
- R: c1 Condicion —condicion_de→ x1 Excepcion
- R: c2 Condicion —condicion_de→ x1 Excepcion
- R: c3 Condicion —condicion_de→ o4 Obligacion
- R: c4 Condicion —condicion_de→ o4 Obligacion
- R: c5 Condicion —condicion_de→ p3 Potestad
- R: pt2 Potestad —aplica_a→ Sujeto_sefyc (mención «Superintendencia de Entidades Financieras y Cambiarias»)
- R: o3 Obligacion —aplica_a→ Sujeto_rol_alcance_capmin (mención «la entidad»)
- Omisión `meta_normativo` [exacta]: «a los efectos de cubrir factores tales como los riesgos de ejecución» — Finalidad de la exigencia adicional.
- Omisión `relacion_sin_predicado` [exacta]: «a cuyo efecto deberá tener a disposición» — La obligación de evidencia acompaña al supuesto c2; no hay predicado Obligacion→Condicion.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «arbitrajes del a) (dos guiones)» (primer guion) | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ x1 Excepcion |
| 2 | «arbitrajes del a) (dos guiones)» (segundo guion) | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ x1 Excepcion |
| 3 | «b) canasta de al menos 90 %» | `condicion_con_relacion` |  | c4 Condicion con el umbral —condicion_de→ o4 Obligacion |
| 4 | «c) sólo si se tienen en cuenta los costos» | `condicion_con_relacion` |  | c5 Condicion —condicion_de→ p3 Potestad |

## `cap::7.1.3::intro` — [bloque intro] Divulgación.

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Capital mínimo por riesgo operacional.
> *heredado:* 7.1. Exigencia de capital por riesgo operacional para entidades del grupo 1.
> *heredado:* 7.1.3. Divulgación.
> *propio:* Las entidades financieras deben dar a conocer al público, de manera regular, a través de sus páginas de Internet o reportes –conforme a los requerimientos que al efecto se establezcan– lo siguiente:

### Extracción (código K)

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

### Extracción (código K)

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

### Extracción (código K)

- **e1 Obligacion** «Deducción de conceptos del 8.4.2 — PNc» — En el cómputo del patrimonio neto complementario (capital de nivel dos), a los conceptos citados en los puntos precedentes se les restarán, de corresponder, los conceptos deducibles previstos en el punto 8.4.2. · props: `{"tipo": "calculo"}` · tramo [exacta]: «A los conceptos citados en los puntos precedentes se les restarán, de corresponder, los conceptos deducibles previstos en el punto 8.4.2.»
- **e2 Operacion** «Cómputo del patrimonio neto complementario (PNc)» — Determinación del patrimonio neto complementario –capital de nivel dos– a partir de los conceptos computables, neto de deducciones · props: `{"tipo": "calculo"}` · tramo [exacta]: «A los conceptos citados en los puntos precedentes se les restarán»
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

### Extracción (código K)

- **d1 Definicion** «ON y títulos de deuda de FF — financiaciones comprendidas» — Integran las financiaciones comprendidas (conceptos incluidos) las obligaciones negociables, incluidas las subordinadas, y los títulos de deuda de fideicomisos financieros no alcanzados por las normas sobre "Fideicomisos financieros comprendidos en la Ley de Entidades Financieras", valuados a costo amortizado y/o a valor razonable con cambios en otros resultados integrales. · props: `{"termino": "Financiaciones comprendidas"}` · tramo [exacta]: «Obligaciones negociables –incluye las subordinadas– y títulos de deuda de fideicomisos financieros no alcanzados por las normas sobre "Fideicomisos financieros comprendidos en la Ley de Entidades Financieras", valuados a costo amortizado y/o a valor razonable con cambios en otros resultados integrales.»

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

### Extracción (código K)

- **c1 Condicion** «Contragarantías del exterior para garantías locales — exclusión 2.2.4» — Requisito (exigido junto con los demás de la lista) para que queden excluidas de las normas de clasificación las financiaciones, avales, fianzas y otras responsabilidades otorgados por sucursales y subsidiarias locales de entidades financieras del exterior por cuenta y orden de su casa matriz, sus sucursales en otros países o la entidad controlante: para las garantías otorgadas localmente, deben e… · tramo [exacta]: «En el caso de las garantías otorgadas localmente, deberán existir respecto de ellas contragarantías extendidas por la casa matriz o sus sucursales en otros países o por la entidad controlante del exterior, cuya efectivización opere en forma irrestricta a simple requerimiento de la filial o subsidiaria local y en modo i…»

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

### Extracción (código K)

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

### Extracción (código K)

- **d1 Definicion** «Indicador situación financiera líquida — situación normal» — Entre los indicadores que pueden reflejar la situación normal de un deudor comercial se destaca que el cliente presente una situación financiera líquida, con bajo nivel y adecuada estructura de endeudamiento en relación con su capacidad de ganancia, y muestre alta capacidad de pago de capital e intereses en las condiciones pactadas, generando fondos en grado aceptable medido a través del análisis … · props: `{"termino": "En situación normal"}` · tramo [no]: «Entre los indicadores que pueden reflejar esta situación se destacan que el cliente: […] presente una situación financiera líquida, con bajo nivel y adecuada estructura de endeudamiento en relación con su capacidad de ganancia, y muestre una alta capacidad de pago de las deudas (capital e intereses) en las condiciones …»
- **d2 Definicion** «Indicador flujo estable — situación normal» — Indicador de situación normal: el flujo de fondos del cliente no es susceptible de variaciones significativas ante modificaciones importantes de variables propias o de su sector de actividad. · props: `{"termino": "En situación normal"}` · tramo [no]: «El flujo de fondos no es susceptible de variaciones significativas ante modificaciones importantes en el comportamiento de las variables tanto propias como vinculadas a su sector de actividad.»
- **o1 Obligacion** «Considerar grupo de contrapartes conectadas — análisis capacidad de pago» — En el análisis para clasificar al cliente en situación normal deberá tenerse en cuenta, de corresponder, la eventual incidencia en su capacidad de pago de la situación de los demás integrantes del grupo de contrapartes conectadas al que pertenece. · props: `{"tipo": "otra"}` · tramo [exacta]: «En el análisis que se lleve a cabo deberá tenerse en cuenta, de corresponder, la eventual incidencia que en su capacidad de pago pueda tener la situación en la que se encuentran los demás integrantes del grupo de contrapartes conectadas al cual pertenece.»
- **op1 Operacion** «Clasificación de deudores cartera comercial» — Clasificación de cada cliente de la cartera comercial y sus financiaciones en una de cinco categorías. · props: `{"tipo": "clasificación de deudor"}` · tramo [no]: «Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías»
- R: o1 Obligacion —regula→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:7 | sí | «Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:» | `extraida_tramo_no_verificable` |  | d1 Definicion con tramo de nivel [no] que contiene la frase |

## `cla::6.5.3.10` — Mantenga arreglos privados con la entidad financiera que cuenten con la opi-

Grupos: grupo_c.

### Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.3. Con problemas.
> *heredado:* El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos, esos problemas pueden resultar en una pérdida para la entidad financiera. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *propio:* 6.5.3.10. Mantenga arreglos privados con la entidad financiera que cuenten con la opinión del auditor externo de la entidad sobre la factibilidad del cumplimiento de la refinanciación, cuando aún no se haya cancelado el 15 % del importe involucrado en el citado acuerdo y siempre que dicho acuerdo se haya alcanzado cuando el deudor se encontraba categorizado en los niveles "con alto riesgo de insolvencia" o "irrecuperable". A fin de determinar el importe de la cancelación, se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deudor –con excepción de las hipotecas sobre inmuebles rurales que, por lo tanto, serán computables–, observando los márgenes de cobertura establecidos en las normas sobre "Garantías". Será requisito indispensable, además, contar con la opinión favorable sobre la calidad de las garantías, formulada por el auditor externo. En los casos de acuerdos superiores al equivalente a 2,5 veces el importe de referencia establecido en el punto 3.7., la reclasificación inicial del cliente a esta categoría podrá realizarse siempre que no medie objeción por parte de la SEFyC, a la cual, previamente, se deberá plantear cada situación en forma individual.

### Extracción (código K)

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

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «sin cancelar el 15 %» | `sin_relacion` | norma_presente | c2 Condicion con el umbral, sin relación; el indicador está en la unidad como c1 Condicion |
| 2 | «acuerdo alcanzado en alto riesgo o irrecuperable» | `sin_relacion` | norma_presente | c3 Condicion sin relación; ídem |
| 3 | «acuerdos de más de 2,5 veces el importe de referencia» | `condicion_con_relacion` |  | c5 Condicion con el umbral —condicion_de→ o1 Obligacion (el planteo previo a la SEFyC) y → op1 Operacion (la reclasificación inicial) |

## `cla::6.5.3.7` — Incurra en atrasos recurrentes, incumplimiento de hasta 180 días respecto de

Grupos: omisiones.

### Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.3. Con problemas.
> *heredado:* El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos, esos problemas pueden resultar en una pérdida para la entidad financiera. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *propio:* 6.5.3.7. Incurra en atrasos recurrentes, incumplimiento de hasta 180 días respecto de condiciones contractuales o nulo movimiento en las cuentas con la entidad.

### Extracción (código K)

- **c1 Condicion** «Atrasos recurrentes — indicador situación Con problemas» — Indicador (alternativo) que puede reflejar la situación 'Con problemas' (6.5.3) de un cliente de cartera comercial: que el cliente incurra en atrasos recurrentes. Supuesto para su clasificación en esa categoría. · tramo [exacta]: «Incurra en atrasos recurrentes»
- **c2 Condicion** «Incumplimiento hasta 180 días — indicador Con problemas» — Indicador (alternativo) que puede reflejar la situación 'Con problemas' (6.5.3): que el cliente incurra en incumplimiento de hasta 180 días respecto de condiciones contractuales. · umbral: ['incumplimiento de hasta 180 días'] · tramo [exacta]: «incumplimiento de hasta 180 días respecto de condiciones contractuales»
- **c3 Condicion** «Nulo movimiento en cuentas — indicador Con problemas» — Indicador (alternativo) que puede reflejar la situación 'Con problemas' (6.5.3): que el cliente registre nulo movimiento en las cuentas con la entidad. · tramo [exacta]: «nulo movimiento en las cuentas con la entidad»

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

### Extracción (código K)

- **c1 Condicion** «Indicador refinanciaciones por insuficiente capacidad de pago» — Indicador de la categoría 'con alto riesgo de insolvencia': el cliente cuenta con refinanciaciones de capital e intereses vinculadas a insuficiente capacidad de pago, con quitas o reducción de las tasas pactadas, o cuando haya sido necesario recibir bienes en pago de parte de las obligaciones. · tramo [exacta]: «Entre los indicadores que pueden reflejar esta situación se destacan que el cliente: […] Cuente con refinanciaciones del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad para su pago, con otorgamiento de quitas o con reducción en las tasas de interés pactadas»
- **x1 Excepcion** «Reducción de tasas por condiciones de mercado» — La reducción de tasas pactadas no constituye el indicador de alto riesgo de insolvencia si deriva de las condiciones del mercado. · tramo [exacta]: «salvo que ello derive de las condiciones del mercado»
- **o1 Operacion** «Recategorización directa por quitas a niveles superiores» — Recategorización directa en niveles superiores ('con problemas', 'en observación') del deudor refinanciado con quitas de capital, aplicando la metodología del punto 2.2.6. de Previsiones mínimas. · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «el deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital podrá ser recategorizado directamente en niveles superiores»
- **p1 Potestad** «Recategorizar directamente deudor refinanciado con quitas» — El deudor refinanciado con quitas de capital puede ser recategorizado directamente en 'con problemas' o 'en observación' por aplicación de la metodología del punto 2.2.6. de Previsiones mínimas. · tramo [exacta]: «podrá ser recategorizado directamente en niveles superiores ("con problemas", "en observación")»
- **c2 Condicion** «Otras condiciones de la categoría observadas» — Que se observen las otras condiciones previstas en las categorías correspondientes. · tramo [exacta]: «siempre que además se observen las otras condiciones previstas en las correspondientes categorías»
- **o2 Operacion** «Reclasificación al nivel inmediato superior» — Reclasificación del deudor refinanciado en el nivel inmediato superior. · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «podrá reclasificárselo en el nivel inmediato superior»
- **p2 Potestad** «Reclasificar al nivel inmediato superior tras pagos» — Puede reclasificarse al deudor refinanciado en el nivel inmediato superior cuando haya pagado el 10% de lo refinanciado e intereses sin atrasos superiores a 31 días y se observen las otras condiciones del nivel. · tramo [exacta]: «podrá reclasificárselo en el nivel inmediato superior»
- **c3 Condicion** «Pago del 10 % refinanciado e intereses» — Haber pagado al menos el 10% de las obligaciones refinanciadas y la totalidad de los intereses devengados, sin atrasos superiores a 31 días, más el porcentaje acumulado que correspondería si se hubiera estado en la categoría inferior. · props: `{"umbrales": [{"tramo": "al menos se haya cumplido con el pago", "comparacion": "minimo_inclusivo", "base": "se haya cumplido con el pago", "regla_comparacion": "limite_relativo:compuesta:al_menos", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['al menos se haya cumplido con el pago', 'sin haber incurrido en atrasos superiores a los 31 días', 'del 10 % de las obligaciones refinanciadas'] · tramo [exacta]: «Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 10 % de las obligaciones refinanciadas y la totalidad de los intereses devengados»
- **c4 Condicion** «Otras condiciones del nivel superior observadas» — Que se observen las otras condiciones previstas en el nivel inmediato superior. · tramo [exacta]: «si, además, se observan las otras condiciones previstas en el citado nivel»
- **r1 Restriccion** «Permanencia mínima 180 días con crédito adicional» — El deudor en esta categoría que refinanció y recibió crédito adicional (punto 2.2.5. de Previsiones mínimas) no cancelado debe permanecer en ella al menos 180 días desde el crédito adicional o la refinanciación, lo más reciente, aun habiendo cancelado el porcentaje del párrafo precedente. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional…'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días»
- **o3 Operacion** «Reclasificación de deudor refinanciado con crédito adicional» — Salida de la categoría 'con alto riesgo de insolvencia' de un deudor refinanciado que recibió crédito adicional. · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda»
- **c5 Condicion** «Crédito adicional no cancelado» — Que la financiación adicional recibida no haya sido cancelada. · tramo [exacta]: «en la medida en que dicha financiación adicional no hubiese sido cancelada»
- **x2 Excepcion** «Categorización en nivel inferior por otras pautas» — La permanencia mínima de 180 días no rige si por otras pautas corresponde categorizar al deudor en el nivel inferior. · tramo [exacta]: «salvo que por aplicación de otras pautas corresponda categorizarlo en el nivel inferior»
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p2 Potestad
- R: c4 Condicion —condicion_de→ p2 Potestad
- R: c5 Condicion —condicion_de→ r1 Restriccion
- R: r1 Restriccion —limita→ o3 Operacion
- R: x2 Excepcion —exceptua→ r1 Restriccion
- R: r1 Restriccion —aplica_a→ Sujeto_deudor (mención «El deudor»)
- R: p1 Potestad —aplica_a→ Sujeto_deudor (mención «el deudor»)
- Omisión `relacion_sin_predicado` [exacta]: «salvo que ello derive de las condiciones del mercado» — La excepción relaja una Condicion (indicador); exceptua solo admite Restriccion.
- Omisión `relacion_sin_predicado` [exacta]: «podrá ser recategorizado directamente en niveles superiores» — Potestad → Operacion sin predicado (habilita).

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «bienes en pago» | `fusionado` |  | c1 Condicion (el indicador, sin relación) junta «bienes en pago» con los otros supuestos del indicador |
| 2 | «recategorización siempre que…» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ p1 Potestad |
| 3 | «pago del 10 %» | `condicion_con_relacion` |  | c3 Condicion con los umbrales —condicion_de→ p2 Potestad |
| 4 | «financiación adicional sin cancelar» | `condicion_con_relacion` |  | c5 Condicion «Crédito adicional no cancelado» —condicion_de→ r1 Restriccion (la permanencia de 180 días) |
| 5 | «salvo otras pautas» | `condicion_con_relacion` |  | x2 Excepcion —exceptua→ r1 Restriccion |

## `cla::6.5.4.7` — Haya solicitado el concurso preventivo, celebrado un acuerdo preventivo extraju-

Grupos: omisiones.

### Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.4. Con alto riesgo de insolvencia.
> *heredado:* El análisis del flujo de fondos del cliente demuestra que es altamente improbable que pueda atender la totalidad de sus compromisos financieros. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *propio:* 6.5.4.7. Haya solicitado el concurso preventivo, celebrado un acuerdo preventivo extrajudicial aún no homologado o se le haya requerido su quiebra, en tanto no hubiere sido declarada, por obligaciones que sean iguales o superiores al 20 % del patrimonio del cliente o por obligaciones entre el 5 % y menos del 20 % del patrimonio cuando persista el pedido de quiebra luego de transcurridos 90 días desde que ésta haya sido requerida. En caso de levantarse el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores, según la situación previa, si se observan las condiciones allí previstas. En el caso de deudores que hayan solicitado el concurso preventivo o acuerdo preventivo extrajudicial aún no homologado, corresponderá la reclasificación inmediata en el nivel siguiente inferior cuando se verifiquen atrasos de más de 540 días.

### Extracción (código K)

- **c1 Condicion** «Concurso o APE por obligaciones ≥20% patrimonio» — Indicador de la situación 'Con alto riesgo de insolvencia' (6.5.4), alternativo a los demás indicadores: el cliente solicitó concurso preventivo, celebró acuerdo preventivo extrajudicial aún no homologado o se le requirió la quiebra (no declarada), por obligaciones iguales o superiores al 20 % de su patrimonio. · umbral: ['iguales o superiores al 20 % del patrimonio del cliente'] · tramo [exacta]: «Entre los indicadores que pueden reflejar esta situación se destacan que el cliente: […] Haya solicitado el concurso preventivo, celebrado un acuerdo preventivo extrajudicial aún no homologado o se le haya requerido su quiebra, en tanto no hubiere sido declarada, por obligaciones que sean iguales o superiores al 20 % d…»
- **c2 Condicion** «Pedido de quiebra 5%-20% patrimonio persistente 90 días» — Indicador de la situación 'Con alto riesgo de insolvencia' (6.5.4): obligaciones entre el 5 % y menos del 20 % del patrimonio cuando el pedido de quiebra persiste luego de 90 días desde su requerimiento. · umbral: ['entre el 5 % y menos del 20 % del patrimonio', 'luego de transcurridos 90 días desde que ésta haya sido requerida'] · tramo [exacta]: «por obligaciones entre el 5 % y menos del 20 % del patrimonio cuando persista el pedido de quiebra luego de transcurridos 90 días desde que ésta haya sido requerida»
- **p1 Potestad** «Reclasificación superior por levantamiento del pedido de quiebra» — En caso de levantarse el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores, según la situación previa, si se observan las condiciones allí previstas. · tramo [exacta]: «el deudor podrá ser reclasificado en niveles superiores, según la situación previa, si se observan las condiciones allí previstas»
- **c3 Condicion** «Levantamiento del pedido de quiebra» — Supuesto de levantamiento del pedido de quiebra. · tramo [exacta]: «En caso de levantarse el pedido de quiebra»
- **c4 Condicion** «Condiciones del nivel superior observadas» — Que se observen las condiciones previstas para el nivel superior según la situación previa. · tramo [exacta]: «si se observan las condiciones allí previstas»
- **o1 Obligacion** «Reclasificación inmediata inferior por atrasos >540 días» — Para deudores que hayan solicitado concurso preventivo o acuerdo preventivo extrajudicial aún no homologado, corresponde la reclasificación inmediata en el nivel siguiente inferior cuando se verifiquen atrasos de más de 540 días. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «corresponderá la reclasificación inmediata en el nivel siguiente inferior cuando se verifiquen atrasos de más de 540 días»
- **c5 Condicion** «Atrasos de más de 540 días en concursados» — Deudores con concurso preventivo o APE no homologado que registren atrasos de más de 540 días. · umbral: ['atrasos de más de 540 días'] · tramo [exacta]: «cuando se verifiquen atrasos de más de 540 días»
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: c4 Condicion —condicion_de→ p1 Potestad
- R: c5 Condicion —condicion_de→ o1 Obligacion

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

### Extracción (código K)

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

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «sin cancelación efectiva previa» | `dentro_de_norma` |  | dentro de la Obligacion o1 («Cómputo de plazos no interrumpido por renovaciones», tramo); sin Condicion |
| 2 | «pago del 15 %» | `condicion_con_relacion` |  | c4 Condicion con los umbrales —condicion_de→ p1 Potestad |
| 3 | «financiación adicional sin cancelar» | `condicion_con_relacion` |  | c9 Condicion «Financiación adicional no cancelada» —condicion_de→ r1 Restriccion |

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

### Extracción (código K)

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

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «deuda de más del 2,5 % de la RPC o del importe de referencia» | `condicion_con_relacion` |  | c1 Condicion con los umbrales —condicion_de→ op1 Operacion (la clasificación) |
| 2 | «excepción de concurso hasta 540 días» | `sin_relacion` | norma_presente | x1 Excepcion con el umbral, sin relación hacia la norma que exceptúa (op1 presente; omisión relacion_sin_predicado) |
| 3 | «siempre que haya informe» | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ x1 Excepcion |
| 4 | «primera declaración» | `dentro_de_norma` |  | dentro de la Operacion op1 (descripción); sin Condicion |
| 5 | «actualizaciones» | `dentro_de_norma` |  | ídem, op1 |

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:26 | sí | «Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre "Previsiones mínimas por ries…» | `omision_otra_vez` | fuera_de_tipos | om#1 fuera_de_tipos [exacta], el mismo tramo recortado antes de la cita de la norma |

## `cla::7.2.2.1` — En observación.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
> *heredado:* 7.2. Niveles de clasificación.
> *heredado:* 7.2.2. Riesgo bajo.
> *propio:* 7.2.2.1. En observación. Comprende los clientes que registran incumplimientos ocasionales en la atención de sus obligaciones, con atrasos de más de 31 hasta 90 días. En cuanto a la situación jurídica del deudor, se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer cuando se haya cancelado, al menos, el 10 % del importe involucrado en el citado acuerdo. Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior, cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 1 cuota o, cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligaciones refinanciadas (por capital), con más la cantidad de cuotas o el porcentaje acumulado que pudiera corresponder, respectivamente, si la refinanciación se hubiera otorgado de encontrarse incluido el deudor en niveles inferiores. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado la cuota citada en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente. En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categoría, corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días resultante de sumar los días de atraso efectivamente registrados a partir de la primera cuota impaga de la refinanciación y los de atraso mínimo establecidos normativamente que correspondan a la categoría en la que se encuentre clasificado el deudor en el mes en que se verifica el nuevo atraso.

### Extracción (código K)

- **d1 Definicion** «En observación (consumo/vivienda): atrasos 31-90 días» — Nivel de riesgo bajo de la cartera de consumo o vivienda que comprende los clientes con incumplimientos ocasionales y atrasos de más de 31 hasta 90 días; también se considera a quien mantenga convenios de pago de concordatos homologados a vencer con al menos 10 % cancelado. · props: `{"termino": "En observación"}` · tramo [exacta]: «Comprende los clientes que registran incumplimientos ocasionales en la atención de sus obligaciones, con atrasos de más de 31 hasta 90 días.»
- **c1 Condicion** «Concordato homologado con 10 % cancelado» — Situación jurídica: el deudor mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluidos acuerdos preventivos extrajudiciales homologados) a vencer, habiéndose cancelado al menos el 10 % del importe involucrado. · umbral: ['al menos, el 10 % del importe involucrado'] · tramo [exacta]: «se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados»
- **op1 Operacion** «Reclasificación de refinanciados al nivel superior» — Reclasificación en el nivel inmediato superior de clientes en observación cuyas deudas fueron refinanciadas. · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «podrán ser reclasificados en el nivel inmediato superior»
- **p1 Potestad** «Reclasificación ascendente de deudores refinanciados» — Los clientes con deudas refinanciadas pueden ser reclasificados en el nivel inmediato superior si cumplen las condiciones de pago. · tramo [exacta]: «Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior»
- **c2 Condicion** «Pago periódico: 1 cuota con atraso ≤31 días» — Refinanciación de pago periódico mensual o bimestral: pago de 1 cuota puntualmente o con atrasos no superiores a 31 días, más las cuotas que correspondieran si el deudor estuviera en niveles inferiores. · props: `{"umbrales": [{"tramo": "con el pago de 1 cuota", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['atrasos que no superen los 31 días', 'con el pago de 1 cuota'] · tramo [exacta]: «cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 1 cuota»
- **c3 Condicion** «Pago único/irregular: 5 % del capital cancelado» — Financiaciones de pago único, periódico superior a bimestral o irregular: cancelación de al menos el 5 % del capital refinanciado, más el porcentaje acumulado que correspondiera si el deudor estuviera en niveles inferiores. · umbral: ['al menos el 5 % de sus obligaciones refinanciadas (por capital)'] · tramo [exacta]: «cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligaciones refinanciadas (por capital)»
- **r1 Restriccion** «Permanencia mínima 180 días con crédito adicional» — El deudor en observación que refinanció y recibió crédito adicional (punto 2.2.5 de Previsiones mínimas) no cancelado debe permanecer en la categoría al menos 180 días desde el crédito adicional o la refinanciación, lo más reciente, aun habiendo pagado la cuota. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por lo menos 180 días'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días»
- **c4 Condicion** «Refinanciación con crédito adicional no cancelado» — Deudor que refinanció y recibió crédito adicional en los términos del punto 2.2.5 de Previsiones mínimas, no cancelado. · tramo [exacta]: «haya refinanciado su deuda –aun cuando haya cancelado la cuota citada en el párrafo precedente– y recibido crédito adicional»
- **op2 Operacion** «Reclasificación de deudor en observación» — Reclasificación del deudor en observación con deuda refinanciada. · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «reclasificación inmediata del deudor»
- **o1 Obligacion** «Reclasificación inmediata por atraso >31 días» — Ante atrasos mayores a 31 días en la deuda refinanciada, reclasificar inmediatamente al deudor en el nivel que surja de sumar los días de atraso efectivos desde la primera cuota impaga y los de atraso mínimo de la categoría en que esté clasificado en el mes del nuevo atraso. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días»
- **c5 Condicion** «Atrasos >31 días en deuda refinanciada» — Atrasos mayores a 31 días en servicios de la deuda refinanciada desde la inclusión en esta categoría. · umbral: ['atrasos mayores a 31 días'] · tramo [exacta]: «En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada»
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: c4 Condicion —condicion_de→ r1 Restriccion
- R: c5 Condicion —condicion_de→ o1 Obligacion
- R: r1 Restriccion —limita→ op1 Operacion
- R: o1 Obligacion —regula→ op2 Operacion
- R: p1 Potestad —aplica_a→ Sujeto_cliente (mención «Los clientes»)
- R: r1 Restriccion —aplica_a→ Sujeto_deudor (mención «El deudor»)
- Omisión `relacion_sin_predicado` [exacta]: «se considerará si mantiene convenios de pago» — Condición de inclusión en la clase definida; condicion_de no admite Definicion.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «cancelado el 10 %» | `sin_relacion` | norma_presente | c1 Condicion con el umbral, sin relación (omisión relacion_sin_predicado: condicion_de no admite Definicion); la norma está en la unidad como d1 Definicion |
| 2 | «pago de 1 cuota» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ p1 Potestad |
| 3 | «pago único o irregular con 5 %» | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ p1 Potestad |
| 4 | «financiación adicional sin cancelar» | `condicion_con_relacion` |  | c4 Condicion —condicion_de→ r1 Restriccion |
| 5 | «atrasos de más de 31 días» | `condicion_con_relacion` |  | c5 Condicion con el umbral —condicion_de→ o1 Obligacion |

## `cla::7.2.3` — Riesgo medio.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
> *heredado:* 7.2. Niveles de clasificación.
> *propio:* 7.2.3. Riesgo medio. Comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días. En cuanto a la situación jurídica del deudor, se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer cuando aún no se haya cancelado el 10 % del importe involucrado en el citado acuerdo. A fin de determinar el importe de la cancelación, se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deudor –con excepción de las hipotecas sobre inmuebles rurales que, por lo tanto, serán computables–, observando los márgenes de cobertura establecidos en las normas sobre "Garantías". Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior, cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 2 cuotas consecutivas o, cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligaciones refinanciadas (por capital), con más la cantidad de cuotas o el porcentaje acumulado que pudiera corresponder, respectivamente, si la refinanciación se hubiera otorgado de encontrarse incluido el deudor en el nivel inferior. El deudor refinanciado que haya cumplido con lo dispuesto en los párrafos precedentes, según corresponda, podrá ser reclasificado en el nivel inmediato superior si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado las cuotas o el porcentaje establecidos precedentemente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente. En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categoría, corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días resultante de sumar los días de atraso efectivamente registrados a partir de la primera cuota impaga de la refinanciación y los de atraso mínimo establecidos normativamente que correspondan a la categoría en la que se encuentre clasificado el deudor en el mes en que se verifica el nuevo atraso.

### Extracción (código K)

- **d1 Definicion** «Riesgo medio — nivel cartera consumo/vivienda» — Comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días. · props: `{"termino": "Riesgo medio"}` · tramo [exacta]: «Comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días.»
- **o1 Operacion** «Clasificación de deudor en riesgo medio» — Clasificación de deudores de la cartera para consumo o vivienda en el nivel riesgo medio · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «Riesgo medio»
- **c1 Condicion** «Convenios de pago con menos del 10 % cancelado» — Situación jurídica: el deudor mantiene convenios de pago de concordatos judiciales o extrajudiciales homologados a vencer sin haber cancelado aún el 10 % del importe del acuerdo. · umbral: ['cuando aún no se haya cancelado el 10 % del importe involucrado'] · tramo [exacta]: «se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer cuando aún no se haya cancelado el 10 % del importe involucrado en el citado acuerdo»
- **p1 Potestad** «Cómputo 50 % garantías adicionales — importe de cancelación» — Para determinar el importe cancelado se admite computar el 50 % de las garantías adicionales a las originales, constituidas sobre bienes no vinculados a la explotación del deudor, observando los márgenes de cobertura de las normas sobre Garantías. · tramo [exacta]: «se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deudor»
- **x1 Excepcion** «Hipotecas sobre inmuebles rurales computables» — Las hipotecas sobre inmuebles rurales, aunque vinculadas a la explotación, son computables como garantías adicionales (salvedad al requisito de bienes no vinculados de la potestad de cómputo). · tramo [exacta]: «con excepción de las hipotecas sobre inmuebles rurales que, por lo tanto, serán computables»
- **o2 Operacion** «Reclasificación de refinanciado al nivel superior» — Reclasificación en el nivel inmediato superior de clientes cuyas deudas fueron refinanciadas · props: `{"tipo": "reclasificación de deudor"}` · tramo [exacta]: «podrán ser reclasificados en el nivel inmediato superior»
- **p2 Potestad** «Reclasificación ascendente de deudores refinanciados» — Los clientes refinanciados pueden ser reclasificados en el nivel inmediato superior si cumplen las condiciones de pago y el resto de sus deudas reúne las condiciones del nivel. · tramo [exacta]: «Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior»
- **c2 Condicion** «Pago puntual de 2 cuotas consecutivas — periódico» — Refinanciación de pago periódico mensual o bimestral: pago de 2 cuotas consecutivas puntualmente o con atrasos no superiores a 31 días, más las cuotas que correspondieran si estuviera en el nivel inferior. · props: `{"umbrales": [{"tramo": "pago de 2 cuotas consecutivas", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['con atrasos que no superen los 31 días', 'pago de 2 cuotas consecutivas'] · tramo [exacta]: «cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 2 cuotas consecutivas»
- **c3 Condicion** «Cancelación 5 % — pago único o irregular» — Financiaciones de pago único, periódico superior a bimestral o irregular: cancelación de al menos el 5 % del capital refinanciado, más el porcentaje acumulado que correspondiera si estuviera en el nivel inferior. · umbral: ['al menos el 5 % de sus obligaciones refinanciadas (por capital)'] · tramo [exacta]: «cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligaciones refinanciadas (por capital)»
- **c4 Condicion** «Resto de deudas cumple condiciones del nivel» — Además, el resto de las deudas del deudor refinanciado debe reunir como mínimo las condiciones del nivel inmediato superior. · tramo [exacta]: «si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel»
- **r1 Restriccion** «Permanencia mínima 180 días — refinanciado con crédito adicional» — El deudor en riesgo medio que refinanció y recibió crédito adicional (punto 2.2.5 de Previsiones mínimas), no cancelado, debe permanecer en la categoría al menos 180 días desde el crédito adicional o la refinanciación, la más reciente, aun habiendo pagado las cuotas o el porcentaje. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por lo menos 180 días'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente»
- **c5 Condicion** «Crédito adicional recibido y no cancelado» — El deudor refinanciado recibió crédito adicional según punto 2.2.5 de Previsiones mínimas y éste no fue cancelado. · tramo [exacta]: «recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada»
- **ob1 Obligacion** «Reclasificación inmediata por atraso mayor a 31 días» — Reclasificar inmediatamente al deudor en el nivel que surja de sumar los días de atraso desde la primera cuota impaga de la refinanciación y los de atraso mínimo de la categoría en que se encuentre en el mes del nuevo atraso. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días»
- **c6 Condicion** «Atrasos mayores a 31 días en deuda refinanciada» — Atrasos mayores a 31 días en el pago de servicios de la deuda refinanciada desde la inclusión en riesgo medio. · umbral: ['atrasos mayores a 31 días'] · tramo [exacta]: «En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categoría»
- **co1 Comunicacion** «Normas sobre Garantías» —  · props: `{"codigo": "Garantías"}` · tramo [exacta]: «las normas sobre "Garantías"»
- **co2 Comunicacion** «Previsiones mínimas por riesgo de incobrabilidad» —  · props: `{"codigo": "Previsiones mínimas por riesgo de incobrabilidad"}` · tramo [exacta]: «normas sobre "Previsiones mínimas por riesgo de incobrabilidad"»
- R: c1 Condicion —condicion_de→ o1 Operacion
- R: c2 Condicion —condicion_de→ p2 Potestad
- R: c3 Condicion —condicion_de→ p2 Potestad
- R: c4 Condicion —condicion_de→ p2 Potestad
- R: r1 Restriccion —limita→ o2 Operacion
- R: c5 Condicion —condicion_de→ r1 Restriccion
- R: c6 Condicion —condicion_de→ ob1 Obligacion
- R: to TextoOrdenado —referencia→ co1 Comunicacion
- R: to TextoOrdenado —referencia→ co2 Comunicacion
- Omisión `relacion_sin_predicado` [exacta]: «con excepción de las hipotecas sobre inmuebles rurales que, por lo tanto, serán computables» — Excepción que relaja una Potestad; exceptua solo admite Restriccion u Obligacion.
- Omisión `relacion_sin_predicado` [exacta]: «corresponderá la reclasificación inmediata del deudor» — Vínculo con el acto de reclasificación (regula) no emitido por falta de Operacion específica de reclasificación descendente.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «sin cancelar el 10 %» | `condicion_con_relacion` |  | c1 Condicion con el umbral —condicion_de→ o1 Operacion (la clasificación en riesgo medio) |
| 2 | «pago de 2 cuotas» | `condicion_con_relacion` |  | c2 Condicion con los umbrales —condicion_de→ p2 Potestad |
| 3 | «pago único o irregular con 5 %» | `condicion_con_relacion` |  | c3 Condicion con el umbral —condicion_de→ p2 Potestad |
| 4 | «financiación adicional sin cancelar» | `condicion_con_relacion` |  | c5 Condicion «Crédito adicional recibido y no cancelado» —condicion_de→ r1 Restriccion |
| 5 | «atrasos de más de 31 días» | `condicion_con_relacion` |  | c6 Condicion con el umbral —condicion_de→ ob1 Obligacion |

## `cla::7.2.4` — Riesgo alto.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
> *heredado:* 7.2. Niveles de clasificación.
> *propio:* 7.2.4. Riesgo alto. Comprende a los clientes con atrasos de más de 180 días hasta un año. También incluirá a los deudores que hayan solicitado el concurso preventivo, celebrado un acuerdo preventivo extrajudicial aún no homologado o se le haya requerido su quiebra, en tanto no hubiere sido declarada, por obligaciones que sean iguales o superiores al 20 % del patrimonio del cliente o por obligaciones entre el 5 % y menos del 20 % del patrimonio cuando persista el pedido de quiebra luego de transcurridos 90 días desde que ésta haya sido requerida. En caso de levantarse el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores, según la situación previa, si se observan las condiciones allí previstas. En el caso de deudores que hayan solicitado el concurso preventivo o acuerdo preventivo extrajudicial o se encuentren en gestión judicial, que verifiquen atrasos de hasta 540 días. Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior, cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 3 cuotas consecutivas o, cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 10 % de sus obligaciones refinanciadas (por capital), con más la cantidad de cuotas o el porcentaje acumulado que pudiera corresponder, respectivamente, si la refinanciación se hubiera otorgado de encontrarse incluido el deudor en el nivel inferior En el caso de deudores que hayan solicitado el concurso preventivo, corresponderá la reclasificación inmediata en el nivel siguiente inferior cuando se verifiquen atrasos de más de 540 días. El deudor refinanciado que haya cumplido con lo dispuesto en los párrafos precedentes, según corresponda, podrá ser reclasificado en el nivel inmediato superior si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado las cuotas o el porcentaje establecidos precedentemente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente. En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categoría, corresponderá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total de días resultante de sumar los días de atraso efectivamente registrados a partir de la primera cuota impaga de la refinanciación y los de atraso mínimo establecidos normativamente que correspondan a la categoría en la que se encuentre clasificado el deudor en el mes en que se verifica el nuevo atraso.

### Extracción (código K)

- **d1 Definicion** «Riesgo alto — cartera consumo o vivienda» — Nivel que comprende a los clientes con atrasos de más de 180 días hasta un año; también incluye a deudores concursados, con APE no homologado o con pedido de quiebra no declarada, por obligaciones ≥ 20 % del patrimonio o entre 5 % y < 20 % si persiste el pedido de quiebra luego de 90 días; y a concursados, con APE o en gestión judicial con atrasos de hasta 540 días. · props: `{"termino": "Riesgo alto"}` · tramo [exacta]: «Comprende a los clientes con atrasos de más de 180 días hasta un año.»
- **o1 Operacion** «Clasificación en riesgo alto — consumo o vivienda» — Clasificación de clientes de la cartera para consumo o vivienda en el nivel riesgo alto · props: `{"tipo": "clasificación de deudor"}` · tramo [exacta]: «Comprende a los clientes con atrasos de más de 180 días hasta un año.»
- **c1 Condicion** «Atrasos más de 180 días hasta un año» — Atrasos de más de 180 días hasta un año · umbral: ['atrasos de más de 180 días hasta un año'] · tramo [exacta]: «clientes con atrasos de más de 180 días hasta un año»
- **c2 Condicion** «Concurso, APE o pedido de quiebra ≥20 % patrimonio» — Deudor con concurso preventivo solicitado, APE no homologado o pedido de quiebra no declarada, por obligaciones iguales o superiores al 20 % del patrimonio · umbral: ['iguales o superiores al 20 % del patrimonio del cliente'] · tramo [exacta]: «deudores que hayan solicitado el concurso preventivo, celebrado un acuerdo preventivo extrajudicial aún no homologado o se le haya requerido su quiebra, en tanto no hubiere sido declarada, por obligaciones que sean iguales o superiores al 20 % del patrimonio del cliente»
- **c3 Condicion** «Pedido de quiebra 5-20 % persistente 90 días» — Obligaciones entre 5 % y menos del 20 % del patrimonio cuando el pedido de quiebra persista luego de 90 días · umbral: ['entre el 5 % y menos del 20 % del patrimonio', 'luego de transcurridos 90 días'] · tramo [exacta]: «por obligaciones entre el 5 % y menos del 20 % del patrimonio cuando persista el pedido de quiebra luego de transcurridos 90 días desde que ésta haya sido requerida»
- **c4 Condicion** «Concursados/APE/gestión judicial atraso hasta 540 días» — Deudores con concurso preventivo, APE o en gestión judicial con atrasos de hasta 540 días · umbral: ['atrasos de hasta 540 días'] · tramo [exacta]: «En el caso de deudores que hayan solicitado el concurso preventivo o acuerdo preventivo extrajudicial o se encuentren en gestión judicial, que verifiquen atrasos de hasta 540 días.»
- **p1 Potestad** «Reclasificación por levantamiento pedido de quiebra» — Levantado el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores según la situación previa, si se observan las condiciones allí previstas · tramo [exacta]: «En caso de levantarse el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores, según la situación previa»
- **c5 Condicion** «Levantamiento del pedido de quiebra» — Que se levante el pedido de quiebra y se observen las condiciones del nivel superior · tramo [exacta]: «En caso de levantarse el pedido de quiebra»
- **p2 Potestad** «Reclasificación de refinanciados al nivel superior» — Clientes refinanciados podrán ser reclasificados en el nivel inmediato superior si cumplen pagos (periódicas: 3 cuotas consecutivas con atrasos ≤31 días; pago único/irregular: cancelación ≥10 % del capital refinanciado), más cuotas o porcentaje del nivel inferior si correspondiera · tramo [exacta]: «Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior»
- **c6 Condicion** «Pago de 3 cuotas con atraso ≤31 días» — Refinanciación de pago periódico mensual o bimestral: pago puntual o con atrasos no superiores a 31 días de 3 cuotas consecutivas · props: `{"umbrales": [{"tramo": "pago de 3 cuotas consecutivas", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['atrasos que no superen los 31 días', 'pago de 3 cuotas consecutivas'] · tramo [exacta]: «cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el pago de 3 cuotas consecutivas»
- **c7 Condicion** «Cancelación ≥10 % capital refinanciado (pago único/irregular)» — Financiaciones de pago único, periódico superior a bimestral o irregular: cancelación de al menos el 10 % del capital refinanciado · umbral: ['al menos el 10 % de sus obligaciones refinanciadas (por capital)'] · tramo [exacta]: «cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular, hayan cancelado al menos el 10 % de sus obligaciones refinanciadas (por capital)»
- **ob1 Obligacion** «Reclasificación inmediata de concursados con atraso >540 días» — Deudores con concurso preventivo solicitado deben reclasificarse inmediatamente en el nivel inferior cuando registren atrasos de más de 540 días · props: `{"tipo": "asignacion"}` · umbral: ['atrasos de más de 540 días'] · tramo [exacta]: «En el caso de deudores que hayan solicitado el concurso preventivo, corresponderá la reclasificación inmediata en el nivel siguiente inferior cuando se verifiquen atrasos de más de 540 días.»
- **p3 Potestad** «Reclasificación de refinanciado cumplidor al superior» — El deudor refinanciado que cumplió lo dispuesto podrá ser reclasificado en el nivel inmediato superior si el resto de sus deudas reúnen como mínimo las condiciones de ese nivel · tramo [exacta]: «podrá ser reclasificado en el nivel inmediato superior si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel»
- **c8 Condicion** «Resto de deudas cumplen condiciones del nivel superior» — El resto de las deudas reúnen como mínimo las condiciones del nivel superior · tramo [exacta]: «si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel»
- **r1 Restriccion** «Permanencia mínima 180 días con crédito adicional» — El deudor en riesgo alto que refinanció y recibió crédito adicional (punto 2.2.5 de Previsiones mínimas) no cancelado debe permanecer en esta categoría al menos 180 días desde el crédito adicional o la refinanciación, lo más reciente, aun habiendo cancelado cuotas o porcentaje · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por lo menos 180 días'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente»
- **c9 Condicion** «Crédito adicional no cancelado tras refinanciación» — Deudor refinanciado que recibió crédito adicional no cancelado · tramo [exacta]: «en la medida en que dicha financiación adicional no hubiese sido cancelada»
- **ob2 Obligacion** «Reclasificación inmediata por atrasos >31 días refinanciados» — Con atrasos mayores a 31 días en la deuda refinanciada, reclasificación inmediata en el nivel que surja de sumar los días de atraso desde la primera cuota impaga y los de atraso mínimo de la categoría vigente en el mes del nuevo atraso · props: `{"tipo": "asignacion"}` · umbral: ['atrasos mayores a 31 días'] · tramo [exacta]: «En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categoría, corresponderá la reclasificación inmediata del deudor»
- R: c1 Condicion —condicion_de→ o1 Operacion
- R: c2 Condicion —condicion_de→ o1 Operacion
- R: c3 Condicion —condicion_de→ o1 Operacion
- R: c4 Condicion —condicion_de→ o1 Operacion
- R: c5 Condicion —condicion_de→ p1 Potestad
- R: c6 Condicion —condicion_de→ p2 Potestad
- R: c7 Condicion —condicion_de→ p2 Potestad
- R: c8 Condicion —condicion_de→ p3 Potestad
- R: c9 Condicion —condicion_de→ r1 Restriccion
- R: r1 Restriccion —limita→ o1 Operacion
- R: ob2 Obligacion —regula→ o1 Operacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «concurso con 20 % o más» | `condicion_con_relacion` |  | c2 Condicion con el umbral —condicion_de→ o1 Operacion (la clasificación) |
| 2 | «entre 5 % y 20 % con 90 días» | `condicion_con_relacion` |  | c3 Condicion con los umbrales —condicion_de→ o1 Operacion |
| 3 | «levantamiento del pedido» | `condicion_con_relacion` |  | c5 Condicion —condicion_de→ p1 Potestad |
| 4 | «refinanciados» | `dentro_de_norma` |  | dentro de la Potestad p2 (tramo) |
| 5 | «más de 540 días» | `dentro_de_norma` |  | dentro de la Obligacion ob1 (umbral «atrasos de más de 540 días»); sin Condicion |
| 6 | «atrasos de más de 31 días» | `dentro_de_norma` |  | dentro de la Obligacion ob2 (umbral «atrasos mayores a 31 días»); la Condicion c6 es la de las 3 cuotas, no esta |

## `ctacte::1.5.2.6` — Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo

Grupos: omisiones.

### Texto

> *heredado:* Sección 1. Funcionamiento.
> *heredado:* 1.5. Aspectos del funcionamiento a incluir en el contrato de cuenta corriente.
> *heredado:* En sus cláusulas se deberá prever, como mínimo:
> *heredado:* 1.5.2. Obligaciones de la entidad.
> *propio:* 1.5.2.6. Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo– los cheques librados por el cuentacorrentista, de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque, teniendo en cuenta en materia de plazos de presentación los establecidos en el artículo 25 de la Ley de Cheques. En el caso de cheques de pago diferido, ese plazo se computará a partir de la fecha de pago consignada en el cheque.

### Extracción (código K)

- **op1 Operacion** «Pago a la vista de cheques» — Pago a la vista por la entidad de los cheques librados por el cuentacorrentista · props: `{"tipo": "pago de cheques"}` · tramo [exacta]: «Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo– los cheques librados por el cuentacorrentista»
- **o1 Obligacion** «Pagar a la vista cheques librados — cláusula contractual» — El contrato de cuenta corriente debe prever, como mínimo, la obligación de la entidad de pagar a la vista los cheques librados por el cuentacorrentista, conforme a las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque, considerando los plazos de presentación del art. 25 de la Ley de Cheques; salvo los casos del punto 1.5.2.8, segundo párrafo. · props: `{"tipo": "otra", "umbrales": [{"tramo": "teniendo en cuenta en materia de plazos de presentación los establecidos en el ar-\ntículo 25 de la Ley de Cheques", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['teniendo en cuenta en materia de plazos de presentación los establecidos en el a…'] · tramo [exacta]: «En sus cláusulas se deberá prever, como mínimo: […] Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo– los cheques librados por el cuentacorrentista, de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque»
- **o2 Obligacion** «Cómputo plazo desde fecha de pago — cheques de pago diferido» — En cheques de pago diferido, el plazo de presentación se computa a partir de la fecha de pago consignada en el cheque. · props: `{"tipo": "calculo"}` · tramo [exacta]: «En el caso de cheques de pago diferido, ese plazo se computará a partir de la fecha de pago consignada en el cheque.»
- **c1 Condicion** «Cheque de pago diferido» — Supuesto de cheques de pago diferido · tramo [exacta]: «En el caso de cheques de pago diferido»
- **x1 Excepcion** «Casos del punto 1.5.2.8 — pago a la vista» — Exceptúa de la obligación de pagar a la vista los cheques en los casos del punto 1.5.2.8, segundo párrafo · tramo [exacta]: «excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo»
- **cm1 Comunicacion** «Ley de Cheques» —  · props: `{"codigo": "Ley de Cheques", "tipo": "externa"}` · tramo [exacta]: «Ley de Cheques»
- R: to TextoOrdenado —referencia→ cm1 Comunicacion
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: c1 Condicion —condicion_de→ o2 Obligacion
- R: x1 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: o1 Obligacion —aplica_a→ Sujeto_banco (mención «la entidad»)
- R: Sujeto_banco (mención «la entidad») —ejecuta→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:6 | sí | «de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque» | `extraida_tramo_verificado` |  | o1 Obligacion [exacta], tramo que contiene el fragmento |

## `ctacte::2.1.1.4` — Lugar y fecha.

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Movimiento de las cuentas.
> *heredado:* 2.1. Créditos.
> *heredado:* 2.1.1. Mediante depósitos por ventanilla o cajeros automáticos.
> *heredado:* Cuando se empleen boletas, éstas deberán contener, como mínimo, los siguientes datos:
> *heredado:* Respecto de la realización de operaciones mediante cajeros automáticos, las entidades deberán tener implementados mecanismos de seguridad informática que garanticen la genuinidad de las operaciones.
> *propio:* 2.1.1.4. Lugar y fecha.

### Extracción (código K)

- **op1 Operacion** «Depósito por ventanilla o cajero automático» — Crédito en cuenta corriente mediante depósitos por ventanilla o cajeros automáticos · props: `{"tipo": "depósito"}` · tramo [exacta]: «Mediante depósitos por ventanilla o cajeros automáticos.»
- **ob1 Obligacion** «Lugar y fecha — dato mínimo de boletas de depósito» — Cuando se empleen boletas para depósitos por ventanilla o cajeros automáticos, éstas deberán contener, como mínimo y junto con los demás datos enumerados (todos exigidos), el lugar y la fecha. · props: `{"tipo": "otra"}` · tramo [exacta]: «Cuando se empleen boletas, éstas deberán contener, como mínimo, los siguientes datos: […] Lugar y fecha.»
- **c1 Condicion** «Empleo de boletas en el depósito» — Que se empleen boletas para el depósito. · tramo [exacta]: «Cuando se empleen boletas»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: c1 Condicion —condicion_de→ ob1 Obligacion
- R: ob1 Obligacion —aplica_a→ Sujeto_banco (mención «las entidades»)

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

### Extracción (código K)

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

### Extracción (código K)

- **c1 Condicion** «Falta del número de orden — título no vale como cheque» — Supuesto (alternativo: basta cualquiera de las especificaciones faltantes de la Ley de Cheques) por el cual el título no vale como cheque: la falta del número de orden, impreso en el cuerpo del cheque librado en formato papel o incorporado a los datos del cheque librado por medios electrónicos. · tramo [exacta]: «El número de orden, impreso en el cuerpo del cheque librado en formato papel»

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

### Extracción (código K)

- **op1 Operacion** «Presentación al cobro de ECHEQ» — Presentación al cobro de un cheque librado por medios electrónicos (ECHEQ) por el tenedor legitimado, mediante orden electrónica de acreditación o cobro por ventanilla · props: `{"tipo": "presentacion_al_cobro"}` · tramo [exacta]: «presentación al cobro de cada ECHEQ»
- **p1 Potestad** «Cobro de ECHEQ desde fecha de pago — tenedor legitimado» — El tenedor legitimado podrá presentar al cobro cada ECHEQ a partir de su fecha de pago, a través de una orden electrónica de acreditación o cobrándolo por ventanilla. · tramo [exacta]: «El tenedor legitimado podrá efectuar la presentación al cobro de cada ECHEQ a partir de la correspondiente fecha de pago a través de una orden electrónica de acreditación o cobrarlo por ventanilla»
- **c1 Condicion** «Desde la fecha de pago del ECHEQ» — La presentación al cobro puede efectuarse a partir de la correspondiente fecha de pago del ECHEQ. · tramo [exacta]: «a partir de la correspondiente fecha de pago»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: Sujeto (mención «El tenedor legitimado») —ejecuta→ op1 Operacion
- R: p1 Potestad —aplica_a→ Sujeto (mención «El tenedor legitimado»)
- Omisión `fuera_de_tipos` [exacta]: «En su defecto, quedará pendiente hasta la fecha de vencimiento del plazo previsto en el artículo 25 de la Ley de Cheques.» — Efecto/estado del ECHEQ no presentado (queda pendiente hasta el vencimiento del plazo legal); no es deber, prohibición ni facultad de un sujeto. Tipo que se habría usado: estado o efecto jurídico del …

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

### Extracción (código K)

- **c1 Condicion** «Cheque a favor de fiduciario de fideicomiso financiero» — Uno de los supuestos alternativos en que los cheques con cláusula "no a la orden" pueden transmitirse por endoso (transferencias primeras y sucesivas): que el cheque se extienda a favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras. · tramo [exacta]: «A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras»
- **c2 Condicion** «Operaciones relativas al fideicomiso» — Para el supuesto del fiduciario, el endoso de cheques "no a la orden" se admite solo si se trata de operaciones relativas al fideicomiso. · tramo [exacta]: «en la medida en que se trate de operaciones relativas al fideicomiso»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:28 | sí | «comprendidos en la Ley de Entidades Financieras» | `extraida_tramo_verificado` |  | c1 Condicion [exacta], tramo que contiene el fragmento |

## `ctacte::6.1.2.7` — Giro sobre el librador, salvo que se tratara de un cheque girado entre distintos

Grupos: omisiones.

### Texto

> *heredado:* Sección 6. Rechazo de cheques.
> *heredado:* 6.1. Causales.
> *heredado:* 6.1.2. Defectos formales.
> *heredado:* Se define como defecto formal todo aquel verificado en la creación del cheque que el beneficiario no pueda advertir por su mera apariencia. Quedan incluidos, entre otros, los siguientes casos:
> *propio:* 6.1.2.7. Giro sobre el librador, salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador.

### Extracción (código K)

- **d1 Definicion** «Giro sobre el librador — defecto formal» — Entre los casos incluidos como defecto formal (verificado en la creación del cheque y no advertible por el beneficiario por su mera apariencia) está el giro sobre el librador. · props: `{"termino": "defecto formal"}` · tramo [exacta]: «Quedan incluidos, entre otros, los siguientes casos: […] Giro sobre el librador»
- **x1 Excepcion** «Cheque entre establecimientos del mismo librador — no defecto» — El giro sobre el librador no se considera defecto formal (causal de rechazo) cuando se trata de un cheque girado entre distintos establecimientos de un mismo librador. · tramo [exacta]: «salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:11 | sí | «Se define como defecto formal todo aquel verificado en la creación del cheque que el beneficiario no pueda advertir por su mera apariencia» | `ausente` |  | ninguna entidad ni omisión cubre la definición del heredado |

## `ext::1.5` — Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Régimen

Grupos: omisiones.

### Texto

> *heredado:* Sección 1. Disposiciones generales.
> *propio:* 1.5. Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Régimen Penal Cambiario.

### Extracción (código K)

- **c1 Comunicacion** «Ley del Régimen Penal Cambiario» —  · props: `{"codigo": "Ley del Régimen Penal Cambiario", "tipo": "externa"}` · tramo [exacta]: «Ley del Régimen Penal Cambiario»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- Omisión `fuera_de_tipos` [exacta]: «Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Régimen Penal Cambiario.» — Es una consecuencia de un incumplimiento (sometimiento al Régimen Penal Cambiario) y el texto no nombra quién la aplica; habría sido Obligacion o Potestad de la autoridad. Consecuencia: 'se encontrará…

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

### Extracción (código K)

- **c1 Condicion** «Pago en el marco del punto 4.8.4» — Supuesto de la excepción a la conformidad previa del BCRA para pagar importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23: la entidad verifica que el pago se concreta en el marco del punto 4.8.4. Es un supuesto alternativo («o») a los demás ítems de la lista. · tramo [exacta]: «el pago es concretado en el marco de lo dispuesto en el punto 4.8.4.»
- **c2 Condicion** «Cliente suscriptor BOPREAL Serie 1 ≥50% deudas elegibles» — Supuesto de la misma excepción a la conformidad previa del BCRA: el pago lo hace un cliente que suscribió BOPREAL Serie 1 antes del 31/01/24 por un monto igual o mayor al 50% del total pendiente de sus deudas elegibles para los puntos 4.4. y 4.5. · umbral: ['por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por…'] · tramo [exacta]: «por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24»

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

### Extracción (código K)

- **c0 Condicion** «Certificación de la entidad de seguimiento — acceso para pago SEPAIMPO» — Uno de los requisitos que se exigen todos juntos para que la entidad interviniente pueda dar acceso al mercado de cambios para pagar importaciones de bienes registradas en el SEPAIMPO (punto 10.3.2): que la entidad, como encargada del seguimiento de la oficialización, certifique que se cumplen las condiciones i) a x), o que cuente con una certificación para realizar el pago emitida por la entidad … · tramo [exacta]: «Certifica en carácter de entidad encargada del seguimiento de la oficialización que se cumplen las condiciones que se enuncian a continuación o cuenta con una certificación para realizar el pago emitida por la entidad que tiene tal responsabilidad»
- **c1 Condicion** «Constancia de registro aduanero de ingreso» — Condición i) de la certificación: tener la constancia del registro aduanero del ingreso al país de los bienes que originan el pago. · tramo [exacta]: «Cuenta con constancia del registro aduanero del ingreso al país de los bienes que originan el pago a cancelarse.»
- **c2 Condicion** «Copia de factura comercial del exterior» — Condición ii): tener copia de la factura comercial emitida en el exterior a nombre del cliente residente que compra al exterior, con nombre y dirección del emisor, nombre del importador argentino, cantidad y descripción de la mercadería, condición de venta y valor de la factura. · tramo [exacta]: «Cuenta con copia de factura comercial emitida en el exterior a nombre del cliente residente en el país»
- **c3 Condicion** «Copia del Documento de Transporte» — Condición iii): tener copia del Documento de Transporte (conocimiento de embarque, carta de porte o guía aérea). · tramo [exacta]: «Cuenta con copia del Documento de Transporte (Conocimiento de Embarque – Carta de Porte – Guía Aérea).»
- **c4 Condicion** «Consistencia de factura y transporte con registros aduaneros» — Condición iv): que la información de la factura comercial y del Documento de Transporte sea consistente con la de los registros aduaneros, según las normas de declaración aduanera aplicables. · tramo [exacta]: «Que la información que surge de la factura comercial y del Documento de Transporte sea consistente con la que figura en los registros aduaneros»
- **c5 Condicion** «Fecha de vencimiento determinable de la obligación» — Condición v): que la documentación permita establecer la fecha de vencimiento de la obligación del importador con el exterior o, si no, que la operación no tiene fecha de vencimiento pactada. · tramo [exacta]: «Que la documentación presentada le permita establecer la fecha de vencimiento de la obligación con el exterior por parte del importador o, en su defecto, que la operación no tiene una fecha de vencimiento pactada.»
- **c6 Condicion** «Operaciones financiadas calificables como deuda por importaciones» — Condición vi): si la operación es financiada, que la documentación permita calificarla como deuda por importaciones de bienes según el punto 10.2.4. · tramo [exacta]: «Que, en caso de tratarse de operaciones financiadas, la documentación presentada le permite calificar a la misma como una deuda por importaciones de bienes según lo dispuesto en el punto 10.2.4.»
- **c7 Condicion** «Pagos acumulados no superan monto facturado» — Condición vii): que el total de pagos imputados a la oficialización, incluido el pago solicitado, no supere el monto facturado en la condición de compra pactada. · props: `{"umbrales": [{"tramo": "no\nsupera el monto facturado en la condición de compra pactada", "comparacion": "maximo_inclusivo", "base": "monto facturado en la condición de compra pactada", "regla_comparacion": "limite_relativo:negacion:raiz_super", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['no supera el monto facturado en la condición de compra pactada'] · tramo [exacta]: «Que el total de los pagos realizados con imputación a la oficialización de importación, incluyendo el pago cuyo curso se está solicitando, no supera el monto facturado en la condición de compra pactada.»
- **c8 Condicion** «Beneficiario admitido del pago» — Condición viii): que el beneficiario sea el proveedor del exterior; o la entidad financiera del exterior o la agencia oficial de crédito que financió la compra, si la operación encuadra como deuda comercial por importaciones de bienes; o el no residente que compró el crédito al acreedor comercial, siempre que no cambien las condiciones del crédito. · tramo [exacta]: «Que el beneficiario del pago a realizar sea el proveedor del exterior»
- **c9 Condicion** «Declaración en Relevamiento de activos y pasivos externos» — Condición ix): tener constancia de que la operación está declarada, si corresponde, en la última presentación vencida del Relevamiento de activos y pasivos externos. · tramo [exacta]: «Cuenta con constancia de que la operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos".»
- **c10 Condicion** «DDJJ de saldo para oficializaciones previas 01/11/19» — Condición x): para importaciones oficializadas antes del 01/11/19, tener una declaración jurada con el saldo de deuda pendiente a la fecha, firmada por el importador, su representante legal o un apoderado con facultades suficientes. · tramo [exacta]: «En el caso de importaciones oficializadas con anterioridad al 01/11/19, cuenta con una declaración jurada consignando el saldo de deuda pendiente a la fecha»
- Omisión `relacion_sin_predicado` [exacta]: «se cumplen las condiciones que se enuncian a continuación» — Las condiciones i) a x) son el contenido de la certificación c0; no hay un predicado Condicion→Condicion (se habría usado condicion_de). Lo mismo vale para c2 a c10.

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

### Extracción (código K)

- **op1 Operacion** «Cancelación por la entidad de cartas de crédito/letras avaladas de importación» — Acceso de la entidad financiera local al mercado de cambios para cancelar cartas de crédito o letras avaladas que emitió u otorgó para garantizar importaciones de bienes con registro aduanero · props: `{"tipo": "acceso al mercado de cambios"}` · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes»
- **p1 Potestad** «Acceso de la entidad para cancelar garantías de importación» — La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de bienes con registro aduanero, incluso cuando no se cumplan los requisitos para el acceso del cliente · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes»
- **c1 Condicion** «Documentación de cumplimiento de condiciones al emitir» — Que la entidad cuente con documentación que demuestre que al momento de apertura o emisión se cumplían las condiciones aplicables según la fecha de emisión y el tipo de operación garantizada · tramo [exacta]: «en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad»
- **o1 Obligacion** «Documentación post 13/12/23: registro aduanero y plazo de pago» — Para cartas de crédito o letras avaladas emitidas desde el 13/12/23, la entidad deberá contar con documentación que demuestre que la operación garantizada era una importación de bienes con registro de ingreso aduanero desde dicha fecha y que el pago garantizado debía concretarse a partir de la fecha estimada de arribo más el plazo del punto 10.10.1 más otros 15 días corridos · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes …'] · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que»
- **c2 Condicion** «Emisión a partir del 13/12/23» — Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23 · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»
- **x1 Excepcion** «Situación del punto 10.10.2.11 — requisito de plazo» — No se exige demostrar el plazo de pago (arribo + plazo 10.10.1 + 15 días) si la operación quedaba comprendida en el punto 10.10.2.11 · tramo [exacta]: «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- **x2 Excepcion** «Pago desde embarque + 15 días — emitidas desde 14/04/25» — Para emitidas desde el 14/04/25, se admite alternativamente que el pago garantizado debiera concretarse desde la fecha estimada de embarque más 15 días corridos, en vez del plazo desde arribo · umbral: ['más un plazo adicional de 15 (quince) días corridos'] · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos»
- **c3 Condicion** «Emisión a partir del 14/04/25» — Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14/04/25 · tramo [exacta]: «Para aquellas emitidas u otorgadas a partir del 14/04/25»
- **c4 Condicion** «Cumplimiento de restantes condiciones» — Que se cumplan las restantes condiciones · tramo [exacta]: «en la medida que se cumplan las restantes condiciones»
- **c5 Condicion** «Porción con pagos a la vista 10.10.2.1/10.10.2.2» — Que corresponda a la porción de la operación por la que el cliente hubiese podido pagar a la vista según 10.10.2.1 o 10.10.2.2 · tramo [exacta]: «cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2.»
- **o2 Obligacion** «Boleto a nombre de la entidad, concepto B14» — El boleto de venta debe efectuarse a nombre de la propia entidad en calidad de cliente por el concepto B14 · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero".»
- **com1 Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- R: to TextoOrdenado —referencia→ com1 Comunicacion
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: c2 Condicion —condicion_de→ o1 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: x1 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: x2 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: c3 Condicion —condicion_de→ x2 Excepcion
- R: c4 Condicion —condicion_de→ x2 Excepcion
- R: c5 Condicion —condicion_de→ x2 Excepcion
- R: o2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la propia entidad»)
- R: o2 Obligacion —regula→ op1 Operacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «emitidas desde el 13/12/23 (más 15 días)» | `condicion_con_relacion` |  | c2 Condicion «Emisión a partir del 13/12/23» —condicion_de→ o1 Obligacion |
| 2 | «desde el 14/04/25» | `condicion_con_relacion` |  | c3 Condicion «Emisión a partir del 14/04/25» —condicion_de→ x2 Excepcion (la admisión del pago desde el embarque) |
| 3 | «con pagos a la vista» | `condicion_con_relacion` |  | c5 Condicion «Porción con pagos a la vista» —condicion_de→ x2 Excepcion |

## `ext::10.4.4` — Cancelación de garantías comerciales de importaciones de bienes otorgadas por

Grupos: grupo_c.

### Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.4. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente.
> *propio:* 10.4.4. Cancelación de garantías comerciales de importaciones de bienes otorgadas por entidades financieras locales. La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero pendiente, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente, en la medida que se verifique que se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad. En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha y, salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país. Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2. Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914. El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B11. Cancelación de garantías comerciales de entidades financieras de importaciones de bienes sin registro de ingreso aduanero". Por los pagos que se realicen, la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuado el pago. En la medida que la entidad no cuente con el registro de la oficialización del despacho de importación dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cambios, la entidad deberá efectuar la correspondiente denuncia.

### Extracción (código K)

- **c1 Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- **op1 Operacion** «Acceso al MLC para cancelar garantías comerciales de importación» — Acceso de la entidad al mercado de cambios para cancelar cartas de crédito o letras avaladas que emitió u otorgó para garantizar importaciones de bienes con registro aduanero pendiente, incluso cuando no se cumplan los requisitos de acceso del cliente · props: `{"tipo": "acceso al mercado de cambios"}` · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero pendiente»
- **p1 Potestad** «Acceso propio aun sin requisitos del cliente» — La entidad puede acceder al mercado de cambios para cancelar las garantías comerciales que otorgó para importaciones de bienes con registro aduanero pendiente, incluso si no se cumplen los requisitos de acceso del cliente · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero pendiente, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente»
- **cd1 Condicion** «Condiciones vigentes a la fecha de emisión» — Que se verifique que se cumplían las condiciones aplicables según la fecha de emisión u otorgamiento de la garantía y el tipo de operación garantizada · tramo [exacta]: «en la medida que se verifique que se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada»
- **cd2 Condicion** «Garantías emitidas desde el 13/12/23» — Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23 · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»
- **o1 Obligacion** «Documentación de registro de ingreso desde 13/12/23» — La entidad debe contar con documentación que demuestre que, al abrirse o emitirse la garantía, la operación garantizada era una importación de bienes con registro de ingreso aduanero a partir del 13/12/23 · props: `{"tipo": "otra"}` · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha»
- **o2 Obligacion** «Documentación de plazo de pago garantizado» — Para garantías desde el 13/12/23, la entidad debe contar con documentación que demuestre que el pago garantizado debía concretarse a partir de la fecha estimada de arribo más el plazo del punto 10.10.1 más 15 días corridos · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes …'] · tramo [exacta]: «que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país»
- **x1 Excepcion** «Situación del punto 10.10.2.11 — plazo de pago» — No se exige documentar el plazo de pago garantizado si la operación está comprendida en el punto 10.10.2.11 · tramo [exacta]: «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- **p2 Potestad** «Pago desde embarque admitido desde 14/04/25» — Para garantías emitidas desde el 14/04/25, se admite que el pago garantizado debiera concretarse desde la fecha estimada de embarque cuando correspondía a la porción por la que el cliente podía pagar a la vista según 10.10.2.1 o 10.10.2.2, cumpliéndose las restantes condiciones · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen»
- **cd3 Condicion** «Garantías emitidas desde el 14/04/25» — Garantías emitidas u otorgadas a partir del 14/04/25 · tramo [exacta]: «Para aquellas emitidas u otorgadas a partir del 14/04/25»
- **cd4 Condicion** «Porción con pago a la vista admitido» — Que el pago corresponda a la porción por la que el cliente podía pagar a la vista según 10.10.2.1 o 10.10.2.2 · tramo [exacta]: «cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2.»
- **cd5 Condicion** «Cumplimiento de restantes condiciones» — Que se cumplan las restantes condiciones · tramo [exacta]: «en la medida que se cumplan las restantes condiciones»
- **o3 Obligacion** «Boleto a nombre de la entidad concepto B11» — El boleto de venta debe hacerse a nombre de la propia entidad como cliente, concepto B11 · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B11. Cancelación de garantías comerciales de entidades financieras de importaciones de bienes sin registro de ingreso aduanero"»
- **o4 Obligacion** «Informar CUIT del importador en SEPAIMPO» — Por los pagos realizados, la entidad debe informar en el SEPAIMPO la CUIT del importador dentro de 5 días hábiles · props: `{"tipo": "reporte_al_supervisor"}` · umbral: ['dentro de los 5 (cinco) días hábiles'] · tramo [exacta]: «Por los pagos que se realicen, la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuado el pago»
- **o5 Obligacion** «Denuncia por falta de oficialización del despacho» — La entidad debe efectuar la denuncia si no cuenta con el registro de oficialización del despacho dentro de 90 días corridos del acceso · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «la entidad deberá efectuar la correspondiente denuncia»
- **cd6 Condicion** «Sin oficialización del despacho en 90 días» — Que la entidad no cuente con el registro de oficialización del despacho dentro de 90 días corridos del acceso · umbral: ['dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cam…'] · tramo [exacta]: «En la medida que la entidad no cuente con el registro de la oficialización del despacho de importación dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cambios»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: cd1 Condicion —condicion_de→ p1 Potestad
- R: cd2 Condicion —condicion_de→ o1 Obligacion
- R: cd2 Condicion —condicion_de→ o2 Obligacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o2 Obligacion —condiciona→ op1 Operacion
- R: x1 Excepcion —exceptua_obligacion→ o2 Obligacion
- R: cd3 Condicion —condicion_de→ p2 Potestad
- R: cd4 Condicion —condicion_de→ p2 Potestad
- R: cd5 Condicion —condicion_de→ p2 Potestad
- R: o3 Obligacion —regula→ op1 Operacion
- R: op1 Operacion —requiere→ o4 Obligacion
- R: o4 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: op1 Operacion —requiere→ o5 Obligacion
- R: o5 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: cd6 Condicion —condicion_de→ o5 Obligacion
- Omisión `meta_normativo` [exacta]: «Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914.» — Nota histórica sobre dónde se recogieron condiciones previas; la Comunicación se extrajo como entidad.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «emitidas desde el 13/12/23» | `condicion_con_relacion` |  | cd2 Condicion «Garantías emitidas desde el 13/12/23» —condicion_de→ o1 y o2 Obligacion |
| 2 | «desde el 14/04/25» | `condicion_con_relacion` |  | cd3 Condicion «Garantías emitidas desde el 14/04/25» —condicion_de→ p2 Potestad |
| 3 | «con pagos a la vista» | `condicion_con_relacion` |  | cd4 Condicion «Porción con pago a la vista admitido» —condicion_de→ p2 Potestad |
| 4 | «sin oficialización a 90 días» | `condicion_con_relacion` |  | cd6 Condicion con el umbral —condicion_de→ o5 Obligacion |

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

### Extracción (código K)

- **op1 Operacion** «Imputación en gestión de cobro en SEPAIMPO» — Imputación del pago de importación con registro aduanero pendiente como en gestión de cobro en el SEPAIMPO, por incumplimiento del proveedor · props: `{"tipo": "registro"}` · tramo [exacta]: «podrá imputarlo en el SEPAIMPO como en "gestión de cobro"»
- **p1 Potestad** «Imputar en gestión de cobro — entidad seguimiento» — La entidad a cargo del seguimiento puede imputar el pago como en gestión de cobro en el SEPAIMPO cuando se dé alguna de las condiciones (alternativas) i) a iii) · tramo [exacta]: «La entidad a cargo del seguimiento del pago realizado, podrá imputarlo en el SEPAIMPO como en "gestión de cobro" cuando se dé alguna de las siguientes condiciones:»
- **c1 Condicion** «Control de cambios en país del exportador» — El importador demuestra gestión de cobro y que la falta de ingreso obedece a restricciones a giros de divisas en el país del proveedor, acreditado con copia con legalización consular de la normativa de control cambiario · tramo [exacta]: «El importador puede demostrar su gestión de cobro y que la falta de ingreso obedece a que, en el país del proveedor del exterior, existen demoras por restricciones a los giros de divisas.»
- **c2 Condicion** «Insolvencia posterior del proveedor sin garantías» — Insolvencia posterior del proveedor del exterior sin garantías de devolución, siempre que el importador aporte la documentación a) y b) · tramo [exacta]: «Insolvencia posterior del proveedor del exterior, no contándose con garantías de devolución de los fondos.»
- **c2a Condicion** «Constancia publicaciones inicio trámite falencial» — Para el supuesto ii), el importador aporta constancia de publicaciones del inicio del trámite falencial · tramo [exacta]: «constancia de las publicaciones que hagan saber el inicio del trámite falencial conforme a lo exigido por la legislación vigente en el país en que tramite»
- **c2b Condicion** «Constancia presentación reconocimiento de acreencia» — Para el supuesto ii), el importador aporta constancia certificada de la presentación para el reconocimiento y pago de su acreencia; documentación legalizada consularmente o según Convenio de La Haya de 1961 cuando corresponda · tramo [exacta]: «constancia de la presentación efectuada para obtener el reconocimiento y pago de su acreencia, certificada por la autoridad interviniente en el proceso»
- **c3 Condicion** «Deudor moroso — supuesto iii» — Deudor moroso, verificándose alguna de las situaciones a) o b) · tramo [exacta]: «Deudor moroso. En la medida que se verifique alguna de las siguientes situaciones:»
- **c3a Condicion** «Reclamos vía aseguradora o agencia de recupero» — El importador demuestra gestión de cobro por reclamos de aseguradoras de crédito a la exportación o agencias de recupero; válido solo si lo adeudado no supera USD 100.000 · umbral: ['no supere el equivalente de USD 100.000'] · tramo [exacta]: «El importador demuestre en forma fehaciente su gestión de cobro a través de los reclamos efectuados al obligado de pago por compañías de seguro de crédito a la exportación o de entidades constituidas como agencias de recupero nacionales o del exterior»
- **c3b Condicion** «Acciones judiciales iniciadas contra el proveedor» — El importador inició y mantiene acciones judiciales, acreditadas con copia certificada del escrito de demanda, legalizada consularmente o según Convenio de La Haya de 1961 · tramo [exacta]: «El importador argentino haya iniciado y mantenga acciones judiciales contra el proveedor del exterior o contra quien corresponda»
- **o1 Obligacion** «Exigir declaración jurada del importador» — En todos los casos la entidad debe exigir una declaración jurada sobre el carácter genuino de lo declarado, firmada por el importador, su representante legal o apoderado con facultades suficientes · props: `{"tipo": "otra"}` · tramo [exacta]: «la entidad deberá exigir, además de la documentación señalada, una declaración jurada sobre el carácter genuino de lo declarado»
- **o2 Obligacion** «Ingreso y liquidación de monto percibido» — Si el importador percibe un monto en moneda extranjera, debe ingresarlo y liquidarlo en el mercado de cambios dentro de 20 días hábiles de la percepción · props: `{"tipo": "otra"}` · umbral: ['dentro de los 20 (veinte) días hábiles siguientes a la fecha de efectiva percepc…'] · tramo [exacta]: «el mismo deberá ser ingresado y liquidado en el mercado de cambios dentro de los 20 (veinte) días hábiles siguientes a la fecha de efectiva percepción»
- **c4 Condicion** «Percepción de moneda extranjera por importador» — El importador percibe un monto en moneda extranjera · tramo [exacta]: «Si el importador percibiera un monto en moneda extranjera»
- **p2 Potestad** «Permanencia en gestión de cobro» — La operación puede permanecer en gestión de cobro mientras se demuestre la vigencia del reclamo y de las condiciones que explican la demora · tramo [exacta]: «la operación podrá permanecer en "gestión de cobro" mientras se demuestre la vigencia del reclamo»
- **c5 Condicion** «Vigencia del reclamo y condiciones de demora» — Se demuestra la vigencia del reclamo y de las condiciones que explican la demora · tramo [exacta]: «mientras se demuestre la vigencia del reclamo y de las condiciones que explican la demora en la ejecución de la transferencia»
- **o3 Obligacion** «Otorgar hasta cinco prórrogas de 180 días» — La entidad otorgará hasta cinco prórrogas sucesivas de hasta 180 días corridos para la permanencia en gestión de cobro · props: `{"tipo": "otra", "umbrales": [{"tramo": "hasta cinco prórrogas sucesivas", "comparacion": "maximo_inclusivo", "base": "cinco prórrogas sucesivas", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['hasta cinco prórrogas sucesivas', 'de hasta 180 (ciento ochenta) días corridos'] · tramo [exacta]: «la entidad otorgará hasta cinco prórrogas sucesivas de hasta 180 (ciento ochenta) días corridos»
- **o4 Obligacion** «Registrar no recupero y finalizar seguimiento» — Utilizados los plazos máximos con sus renovaciones, la entidad registra en SEPAIMPO el no recupero total o parcial y finaliza el seguimiento · props: `{"tipo": "otra"}` · tramo [exacta]: «la entidad registrará la condición de no recupero total o parcial de los fondos en el SEPAIMPO, dando por finalizado su seguimiento del pago»
- **c6 Condicion** «Agotamiento de plazos máximos y renovaciones» — Se utilizaron los plazos máximos con sus sucesivas renovaciones · tramo [exacta]: «Utilizados los plazos máximos con sus sucesivas renovaciones»
- **o5 Obligacion** «Ingresar recupero en 20 días hábiles» — Independientemente del fin del seguimiento, el importador debe ingresar por el mercado de cambios todo recupero en moneda extranjera dentro de 20 días hábiles del cobro · props: `{"tipo": "otra"}` · umbral: ['dentro de los 20 (veinte) días hábiles de la fecha de cobro'] · tramo [exacta]: «la obligación del importador de ingresar por el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro, todo recupero en moneda extranjera»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad a cargo del seguimiento del pago realizado»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad a cargo del seguimiento del pago realizado») —ejecuta→ op1 Operacion
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: c2a Condicion —condicion_de→ p1 Potestad
- R: c2b Condicion —condicion_de→ p1 Potestad
- R: c3a Condicion —condicion_de→ p1 Potestad
- R: c3b Condicion —condicion_de→ p1 Potestad
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o2 Obligacion —aplica_a→ Sujeto_importador (mención «el importador»)
- R: c4 Condicion —condicion_de→ o2 Obligacion
- R: c5 Condicion —condicion_de→ p2 Potestad
- R: o3 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o4 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: c6 Condicion —condicion_de→ o4 Obligacion
- R: o5 Obligacion —aplica_a→ Sujeto_importador (mención «importador»)
- Omisión `meta_normativo` [exacta]: «Esto es independiente de la obligación del importador» — Aclaración interpretativa sobre la independencia entre la finalización del seguimiento y la obligación del importador; la obligación se extrajo

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «i) control de cambios» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ p1 Potestad |
| 2 | «ii) insolvencia (con a y b)» | `condicion_con_relacion` |  | c2 Condicion (y c2a, c2b) —condicion_de→ p1 Potestad |
| 3 | «a hasta USD 100.000» | `condicion_con_relacion` |  | c3a Condicion con el umbral —condicion_de→ p1 Potestad |
| 4 | «b acciones judiciales» | `condicion_con_relacion` |  | c3b Condicion —condicion_de→ p1 Potestad |
| 5 | «percepción en moneda extranjera» | `condicion_con_relacion` |  | c4 Condicion «Percepción de moneda extranjera por importador» —condicion_de→ o2 Obligacion |

## `ext::10.5::intro` — [bloque intro] Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente.

Grupos: omisiones.

### Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.5. Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente.
> *propio:* Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 estará sujeto a un seguimiento desde la fecha de acceso al mercado de cambios hasta la fecha en que se produzca su regularización. Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento de ese pago, y por hasta el monto girado, la existencia de: i) el registro de ingreso aduanero a su nombre o a nombre de un tercero en la medida que se cumplan las condiciones establecidas en la presente normativa; y/o ii) la liquidación en el mercado de cambios de las divisas asociadas a la devolución del pago efectuado; y/o iii) otras formas de regularización previstas en la presente norma según las condiciones y límites establecidos en cada caso; y/o iv) la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la operación. El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago y deberá estar debidamente justificado por ésta.

### Extracción (código K)

- **op1 Operacion** «Pago de importaciones con ingreso aduanero pendiente» — Pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 con acceso al mercado de cambios · props: `{"tipo": "pago de importaciones"}` · tramo [exacta]: «Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19»
- **ob1 Obligacion** «Seguimiento hasta regularización — pagos importaciones pendientes» — Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado desde el 02/09/19 está sujeto a seguimiento desde la fecha de acceso al mercado de cambios hasta su regularización · props: `{"tipo": "otra"}` · tramo [exacta]: «estará sujeto a un seguimiento desde la fecha de acceso al mercado de cambios hasta la fecha en que se produzca su regularización»
- **d1 Definicion** «Situación regularizada de pagos de importaciones» — La situación de los pagos se considera regularizada a efectos cambiarios cuando se demuestra ante la entidad encargada del seguimiento, por hasta el monto girado, alguno o varios de: (i) registro de ingreso aduanero a su nombre o de un tercero cumpliendo las condiciones normativas; (ii) liquidación en el mercado de cambios de divisas por devolución del pago; (iii) otras formas de regularización pr… · props: `{"termino": "regularizada"}` · tramo [exacta]: «Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento de ese pago, y por hasta el monto girado, la existencia de:»
- **c1 Condicion** «Registro de ingreso aduanero — regularización» — Supuesto alternativo (y/o) de regularización, por hasta el monto girado: registro de ingreso aduanero a nombre propio o de un tercero cumpliendo las condiciones normativas · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «el registro de ingreso aduanero a su nombre o a nombre de un tercero en la medida que se cumplan las condiciones establecidas en la presente normativa»
- **c2 Condicion** «Liquidación de divisas por devolución — regularización» — Supuesto alternativo (y/o) de regularización, por hasta el monto girado: liquidación en el mercado de cambios de las divisas asociadas a la devolución del pago · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «la liquidación en el mercado de cambios de las divisas asociadas a la devolución del pago efectuado»
- **c3 Condicion** «Otras formas previstas — regularización» — Supuesto alternativo (y/o) de regularización, por hasta el monto girado: otras formas previstas en la norma según sus condiciones y límites · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «otras formas de regularización previstas en la presente norma según las condiciones y límites establecidos en cada caso»
- **c4 Condicion** «Conformidad del BCRA — regularización» — Supuesto alternativo (y/o) de regularización, por hasta el monto girado: conformidad del BCRA para regularizar parte o el total de la operación · props: `{"umbrales": [{"tramo": "por hasta el monto\ngirado", "comparacion": "maximo_inclusivo", "base": "monto girado", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto girado'] · tramo [exacta]: «la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la operación»
- **p1 Potestad** «Conformidad BCRA para regularizar operación» — El BCRA puede otorgar conformidad para dar por regularizada parte o el total de la operación · tramo [exacta]: «la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la operación»
- **op2 Operacion** «Pedido de conformidad al BCRA para regularizar» — Pedido de conformidad al BCRA para dar por regularizado un pago de importaciones con registro aduanero pendiente · props: `{"tipo": "solicitud de conformidad"}` · tramo [exacta]: «El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago»
- **r1 Restriccion** «Solo entidad de seguimiento tramita pedido» — El pedido de conformidad al BCRA solo puede ser tramitado por la entidad encargada del seguimiento del pago · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago»
- **ob2 Obligacion** «Justificación debida del pedido de conformidad» — El pedido de conformidad al BCRA debe estar debidamente justificado por la entidad encargada del seguimiento del pago · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «deberá estar debidamente justificado por ésta»
- R: op1 Operacion —requiere→ ob1 Obligacion
- R: p1 Potestad —aplica_a→ Sujeto_bcra (mención «BCRA»)
- R: r1 Restriccion —limita→ op2 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto (mención «la entidad encargada del seguimiento del pago»)
- R: Sujeto (mención «la entidad encargada del seguimiento del pago») —ejecuta→ op2 Operacion
- R: ob2 Obligacion —regula→ op2 Operacion
- R: ob2 Obligacion —aplica_a→ Sujeto (mención «la entidad encargada del seguimiento del pago»)
- Omisión `relacion_sin_predicado` [exacta]: «Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre» — Los supuestos de regularización ponen fin al seguimiento (Obligacion ob1); condicion_de sobre una Definicion (d1) no está admitido; se habría usado condicion_de hacia d1

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

### Extracción (código K)

- **c1 Condicion** «Contraparte no vinculada — pago anticipado de servicios» — Supuesto de la situación 13.3.9: el pago se hace a una contraparte no vinculada al cliente. Es una de las situaciones alternativas (basta alguna) que habilitan el acceso al mercado de cambios para pagar servicios prestados o devengados desde el 13/12/23 antes de los plazos de los puntos 13.2.3. a 13.2.7. Se exige junto con el supuesto del canje y/o arbitraje. · tramo [exacta]: «el pago sea a una contraparte no vinculada al cliente»
- **c2 Condicion** «Canje/arbitraje con fondos en cuenta local en moneda extranjera — pago anticipado» — Supuesto de la situación 13.3.9: el pago se hace mediante un canje y/o arbitraje con fondos depositados en una cuenta en moneda extranjera en una entidad financiera local. Se exige junto con el supuesto de la contraparte no vinculada, y habilita el acceso anticipado para pagar servicios antes de los plazos de los puntos 13.2.3. a 13.2.7. · tramo [exacta]: «se concrete mediante la realización de un canje y/o arbitraje con los fondos depositados en una cuenta en moneda extranjera en una entidad financiera local»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:1 | sí | «También será admisible el acceso para el pago de servicios que fueron o serán prestados o devengados a partir del 13/12/23 con antelación a los plazos previstos…» | `ausente` |  | ninguna entidad ni omisión cubre la oración del heredado |

## `ext::13.5` — Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas por entidades

Grupos: omisiones.

### Texto

> *heredado:* Sección 13. Pagos de servicios prestados por no residentes.
> *propio:* 13.5. Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas por entidades financieras para garantizar importaciones de servicios. Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios, en la medida que se verifique que cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada. En particular, en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23 y el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le corresponde al servicio por el punto 13.2. más otros 15 (quince) días corridos a la fecha estimada de prestación o devengamiento del servicio. En caso de tratarse una operación del concepto "S30. Servicios de fletes por operaciones de importaciones de bienes" que encuadra en lo previsto en el punto 10.10.2.1., debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar 15 (quince) días corridos a la fecha estimada de embarque de los bienes en origen.

### Extracción (código K)

- **op1 Operacion** «Acceso MLC: pago propio cartas de crédito/letras avaladas» — Acceso de las entidades financieras al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar importaciones de servicios · props: `{"tipo": "acceso al mercado de cambios"}` · tramo [exacta]: «Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de servicios»
- **p1 Potestad** «Acceso MLC entidades por pagos propios de garantías» — Las entidades financieras pueden acceder al mercado de cambios para cursar pagos propios por cartas de crédito o letras avaladas que garantizan importaciones de servicios. · tramo [exacta]: «Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios»
- **c1 Condicion** «Cumplimiento de condiciones vigentes a la emisión» — Que se verifique que las cartas de crédito o letras avaladas cumplían las condiciones aplicables según su fecha de emisión u otorgamiento. · tramo [exacta]: «en la medida que se verifique que cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada»
- **o1 Obligacion** «Documentación servicio y plazo — garantías desde 13/12/23» — Para cartas de crédito o letras avaladas emitidas desde el 13/12/23, la entidad debe contar con documentación que demuestre que, al momento de apertura o emisión, el servicio garantizado era prestado o devengado desde el 13/12/23 y el pago debía concretarse por el cliente a partir del plazo del punto 13.2 más 15 días corridos desde la fecha estimada de prestación o devengamiento (para fletes S30 e… · props: `{"tipo": "otra"}` · umbral: ['el plazo en días corridos que le corresponde al servicio por el punto 13.2. más …', 'adicionar 15 (quince) días corridos a la fecha estimada de embarque de los biene…'] · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a un servicio prestado o devengado a partir del 13/12/23»
- **c2 Condicion** «Garantías emitidas desde el 13/12/23» — Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23. · tramo [exacta]: «en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»
- **c3 Condicion** «Fletes S30 encuadrados en punto 10.10.2.1.» — Operación del concepto S30 fletes por importaciones de bienes encuadrada en 10.10.2.1.; aplica el plazo de 15 días desde el embarque. · tramo [exacta]: «En caso de tratarse una operación del concepto "S30. Servicios de fletes por operaciones de importaciones de bienes" que encuadra en lo previsto en el punto 10.10.2.1.»
- R: p1 Potestad —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- R: Sujeto_entidad_financiera (mención «Las entidades financieras») —ejecuta→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ o1 Obligacion
- R: c3 Condicion —condicion_de→ o1 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:24 | sí | «En particular, en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23» | `extraida_tramo_verificado` |  | c2 Condicion [exacta] con tramo «en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23» (sin «En particular») |

## `ext::14.5.7` — Los aportes de inversión directa en especie instrumentados mediante la entrega al

Grupos: grupo_c.

### Texto

> *heredado:* Sección 14. Disposiciones complementarias asociadas al Régimen de Incentivo para Grandes Inversiones (RIGI).
> *heredado:* En esta sección se detallan las disposiciones complementarias en materia cambiaria que, en la medida que las disposiciones generales no resulten más favorables, resultan aplicables a un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo los referidas al "Régimen de Incentivo para Grandes Inversiones" (RIGI) establecido en el Título VII de la Ley 27.742 y reglamentado por el Decreto 749/24 y concordantes.
> *heredado:* 14.5. Otras disposiciones.
> *propio:* 14.5.7. Los aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital podrán ser computados como ingresados y liquidados en el mercado de cambios en la medida que: i) El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte que será computado como ingresado y liquidado en el mercado de cambios. La operación podrá incluir bienes que no revistan la condición de bien de capital en la medida que aquellos que lo sean representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado y la entidad cuente con una declaración jurada del cliente en la cual deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios para el funcionamiento, construcción o instalación de los bienes de capital que se están adquiriendo. La entidad deberá contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO). ii) El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte. En caso de no disponerla, deberá presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio de la decisión de capitalización definitiva de los aportes de capital computados de acuerdo con los requisitos legales correspondientes y comprometerse a presentar la documentación de la capitalización definitiva del aporte dentro de los 365 (trescientos sesenta y cinco) días corridos desde el inicio del trámite. iii) Una entidad financiera haya registrado al aporte de capital en el régimen informático de operaciones de cambio (RIOC) mediante la confección de dos boletos de cambio sin movimiento de fondos con las siguientes características: a) Los boletos deberán ser registrados en la fecha en que se produjo el registro de ingreso aduanero de los bienes, independientemente de cuál sea el momento en que el cliente solicite su registro ante la entidad financiera. b) El boleto de compra se confeccionará con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo. En caso de que el VPU contemple la posibilidad de aplicar cobros de exportaciones de bienes para la repatriación del aporte, la entidad deberá asignar el correspondiente número de identificación (número APX) para el "Seguimiento de anticipos y otras financiaciones de exportación de bienes", el cual quedará a cargo de la propia entidad. c) El boleto de venta se confeccionará con el código de concepto de pago diferido de importaciones de bienes de capital, dejando constancia que el pago se enmarca en el presente mecanismo.

### Extracción (código K)

- **op1 Operacion** «Cómputo aporte en especie como liquidado» — Cómputo como ingresados y liquidados en el mercado de cambios de aportes de inversión directa en especie instrumentados mediante entrega al VPU de bienes de capital · props: `{"tipo": "aporte de inversión directa"}` · tramo [exacta]: «Los aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital podrán ser computados como ingresados y liquidados en el mercado de cambios»
- **p1 Potestad** «Computar aporte en especie de bienes de capital» — Los aportes de inversión directa en especie mediante entrega al VPU de bienes de capital pueden computarse como ingresados y liquidados en el mercado de cambios si se cumplen las condiciones i) a iii). · tramo [exacta]: «podrán ser computados como ingresados y liquidados en el mercado de cambios en la medida que:»
- **c1 Condicion** «Registro aduanero del bien consistente con aporte» — El VPU demostró el registro de ingreso aduanero del bien de capital por valor consistente con el monto del aporte computado. · tramo [exacta]: «El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte»
- **p2 Potestad** «Inclusión de bienes no de capital» — La operación puede incluir bienes que no sean bienes de capital, bajo condiciones. · tramo [exacta]: «La operación podrá incluir bienes que no revistan la condición de bien de capital»
- **c2 Condicion** «Bienes de capital mínimo 90% valor FOB» — Los bienes de capital representan como mínimo el 90% del valor FOB total pagado. · umbral: ['como mínimo el 90% (noventa por ciento) del valor FOB total pagado'] · tramo [exacta]: «en la medida que aquellos que lo sean representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado»
- **c3 Condicion** «DDJJ cliente: restantes bienes son repuestos/accesorios» — La entidad cuenta con DDJJ del cliente de que los restantes bienes son repuestos, accesorios o materiales necesarios para funcionamiento, construcción o instalación de los bienes de capital. · tramo [exacta]: «la entidad cuente con una declaración jurada del cliente en la cual deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios»
- **o1 Obligacion** «Certificación SEPAIMPO — aporte en especie» — La entidad debe contar con la certificación de la entidad encargada del SEPAIMPO. · props: `{"tipo": "otra"}` · tramo [exacta]: «La entidad deberá contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO).»
- **o2 Obligacion** «Documentación de capitalización definitiva del aporte» — El VPU debe presentar la documentación que avale la capitalización definitiva del aporte. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte.»
- **x1 Excepcion** «Sin documentación: constancia de inscripción en trámite» — Si no dispone de la documentación, el VPU presenta constancia de inicio del trámite de inscripción en el Registro Público de Comercio y se compromete a presentar la documentación de capitalización definitiva dentro de 365 días corridos. · umbral: ['dentro de los 365 (trescientos sesenta y cinco) días corridos desde el inicio de…'] · tramo [exacta]: «En caso de no disponerla, deberá presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio»
- **c4 Condicion** «Registro del aporte en RIOC con dos boletos» — Una entidad financiera registró el aporte en el RIOC con dos boletos sin movimiento de fondos con las características a) a c). · tramo [exacta]: «Una entidad financiera haya registrado al aporte de capital en el régimen informático de operaciones de cambio (RIOC) mediante la confección de dos boletos de cambio sin movimiento de fondos»
- **o3 Obligacion** «Fecha de registro de boletos: ingreso aduanero» — Los boletos deben registrarse en la fecha del registro de ingreso aduanero de los bienes, independientemente de cuándo el cliente solicite su registro. · props: `{"tipo": "otra"}` · tramo [exacta]: «Los boletos deberán ser registrados en la fecha en que se produjo el registro de ingreso aduanero de los bienes»
- **o4 Obligacion** «Código de concepto del boleto de compra» — El boleto de compra se confecciona con código de concepto que identifique el aporte comprendido en el mecanismo. · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de compra se confeccionará con un código de concepto que identifique que se trata de un aporte comprendido en este mecanismo.»
- **c5 Condicion** «VPU contempla repatriar con cobros de exportación» — El VPU contempla aplicar cobros de exportaciones de bienes para repatriar el aporte. · tramo [exacta]: «En caso de que el VPU contemple la posibilidad de aplicar cobros de exportaciones de bienes para la repatriación del aporte»
- **o5 Obligacion** «Asignar número APX — seguimiento de anticipos» — La entidad debe asignar el número APX para el Seguimiento de anticipos y otras financiaciones de exportación de bienes, quedando a su cargo. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «la entidad deberá asignar el correspondiente número de identificación (número APX)»
- **o6 Obligacion** «Código de concepto del boleto de venta» — El boleto de venta se confecciona con el código de pago diferido de importaciones de bienes de capital, dejando constancia de que se enmarca en el mecanismo. · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta se confeccionará con el código de concepto de pago diferido de importaciones de bienes de capital»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c4 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p2 Potestad
- R: c3 Condicion —condicion_de→ p2 Potestad
- R: c5 Condicion —condicion_de→ o5 Obligacion
- R: x1 Excepcion —exceptua_obligacion→ o2 Obligacion
- R: o1 Obligacion —condiciona→ op1 Operacion
- R: o2 Obligacion —condiciona→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o4 Obligacion —regula→ op1 Operacion
- R: o6 Obligacion —regula→ op1 Operacion
- R: p1 Potestad —aplica_a→ Sujeto_vpu_rigi (mención «VPU»)
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: o2 Obligacion —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- R: x1 Excepcion —aplica_a→ Sujeto_vpu_rigi (mención «El VPU»)
- R: o5 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: o3 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Una entidad financiera»)
- R: o4 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Una entidad financiera»)
- R: o6 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Una entidad financiera»)

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «i) a iii) en la medida que» (i)) | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ p1 Potestad |
| 2 | «i) a iii) en la medida que» (ii)) | `dentro_de_norma` |  | extraído como norma de otro tipo: o2 Obligacion —condiciona→ op1; sin Condicion para ii) |
| 3 | «i) a iii) en la medida que» (iii)) | `condicion_con_relacion` |  | c4 Condicion —condicion_de→ p1 Potestad |
| 4 | «al menos 90 % del FOB» | `condicion_con_relacion` |  | c2 Condicion con el umbral —condicion_de→ p2 Potestad (inclusión de bienes no de capital) |
| 5 | «en caso de no disponer la documentación» | `condicion_con_relacion` |  | x1 Excepcion «Sin documentación…» —exceptua_obligacion→ o2 Obligacion; leída como cláusula de excepción con obligación sustituta (caso límite, a adjudicar) |
| 6 | «VPU con cobros de exportaciones» | `condicion_con_relacion` |  | c5 Condicion —condicion_de→ o5 Obligacion |

## `ext::2.1` — Cobros de exportaciones de bienes.

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
> *propio:* 2.1. Cobros de exportaciones de bienes. En las Secciones 7., 8. y 9. se detallan las normas asociadas a la operatoria de exportaciones de bienes, las disposiciones relacionadas al seguimiento de las negociaciones de divisas por exportaciones de bienes (SECOEXPO) y del seguimiento de anticipos y otras financiaciones de exportación de bienes, respectivamente.

### Extracción (código K)

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

### Extracción (código K)

- **e1 Potestad** «Acceso anticipado al MLC para servicios de deuda» — Las entidades podrán dar acceso al mercado de cambios a los residentes que deban realizar pagos de servicios de deudas financieras comprendidas en el punto 3.5. o de títulos valores con acceso al mercado de cambios según los puntos 3.6.1.3. a 3.6.1.5., para comprar moneda extranjera antes del plazo admitido por la normativa para cada caso, en las condiciones que se enumeran a continuación. · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a los residentes que deban»
- **e2 Operacion** «Compra anticipada de moneda extranjera para servicios de deuda» — Compra de moneda extranjera por residentes, con anterioridad al plazo admitido por la normativa, para pagar servicios de deudas financieras del punto 3.5. o de títulos valores con acceso según puntos 3.6.1.3. a 3.6.1.5. · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «para la compra de moneda extranjera con anterioridad al plazo admitido por la normativa para cada caso»
- R: e1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)
- R: Sujeto (mención «los residentes») —ejecuta→ e2 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «Las entidades podrán dar acceso al mercado de cambios a los residentes que deban» — Vínculo Potestad → Operacion (habilita); no hay predicado

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

### Extracción (código K)

- **x1 Excepcion** «Transferencias para canje/recompra de deuda — DDJJ 3.16.3.1/2» — En las declaraciones juradas de los puntos 3.16.3.1 y 3.16.3.2 (requisito de conformidad previa del BCRA) no se computan las transferencias de títulos valores a depositarias del exterior para participar de un canje o recompra de títulos de deuda del Gobierno Nacional, gobiernos locales u otros emisores residentes del sector privado. · tramo [no]: «no deberán tenerse en cuenta: […] las transferencias de títulos valores a entidades depositarias del exterior realizadas o a realizar por el cliente con el objeto de participar de un canje o una operación de recompra de títulos de deuda emitidos por el Gobierno Nacional, gobiernos locales u otros emisores residentes de…»
- **o1 Obligacion** «Compromiso de certificación de títulos canjeados» — El cliente que invoque la exclusión del inciso i) debe comprometerse a presentar la certificación por los títulos de deuda canjeados. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «El cliente deberá comprometerse a presentar la correspondiente certificación por los títulos de deuda canjeados.»
- **x2 Excepcion** «Entrega de activos por garantía — DDJJ 3.16.3.1/2» — En las DDJJ de los puntos 3.16.3.1 y 3.16.3.2 no se computa la entrega de activos locales para cancelar deuda con una agencia oficial de crédito o entidad financiera del exterior. · tramo [no]: «no deberán tenerse en cuenta: […] la entrega de activos locales con el objeto de cancelar una deuda con una agencia oficial de crédito o una entidad financiera del exterior»
- **c2 Condicion** «Entrega desde vencimiento por cláusula de garantía» — La entrega debe producirse a partir del vencimiento como consecuencia de una cláusula de garantía del contrato de endeudamiento. · tramo [exacta]: «en la medida que se produzca a partir del vencimiento como consecuencia de una cláusula de garantía prevista en el contrato de endeudamiento.»
- **x3 Excepcion** «Ventas de títulos con fondos aplicados a pagos» — En las DDJJ de los puntos 3.16.3.1 y 3.16.3.2 no se computan las ventas de títulos con liquidación en moneda extranjera cuando la totalidad de los fondos se use dentro de 10 días corridos a alguna de las operaciones a) a e). · umbral: ['dentro de los 10 (diez) días corridos'] · tramo [no]: «no deberán tenerse en cuenta: […] las ventas de títulos valores con liquidación en moneda extranjera en el país o en el exterior cuando la totalidad de los fondos obtenidos de tales liquidaciones se haya utilizado o será utilizada dentro de los 10 (diez) días corridos a las siguientes operaciones:»
- **c3a Condicion** «a) Pagos de nuevos endeudamientos con 1 año gracia» — Destino alternativo: pagos de nuevos endeudamientos del 3.5 desembolsados desde 02/10/23 con al menos 1 año de gracia. · umbral: ['como mínimo 1 (un) año de gracia para el pago de capital'] · tramo [exacta]: «Pagos a partir del vencimiento de capital o intereses de nuevos endeudamientos financieros comprendidos en el punto 3.5., desembolsados a partir del 02/10/23 y que contemplen como mínimo 1 (un) año de gracia para el pago de capital.»
- **c3b Condicion** «b) Repatriación de inversiones directas tras 1 año» — Destino alternativo: repatriaciones de inversiones directas de no residentes recibidas desde 02/10/23, al menos 1 año después del aporte y cumpliendo los mecanismos legales. · umbral: ['como mínimo 1 (un) año después de la concreción del aporte de capital'] · tramo [exacta]: «Repatriaciones del capital y rentas asociadas a las inversiones directas de no residentes recibidas a partir del 02/10/23, en la medida que la repatriación se produzca como mínimo 1 (un) año después de la concreción del aporte de capital»
- **c3c Condicion** «c) Pagos de títulos locales con 2 años gracia» — Destino alternativo: pagos de títulos de deuda emitidos desde 02/10/23 con registro público en el país, no del 3.5, en moneda extranjera, con al menos 2 años de gracia. · umbral: ['como mínimo 2 (dos) años de gracia para el pago de capital'] · tramo [exacta]: «Pagos a partir del vencimiento de capital o intereses de títulos de deuda emitidos a partir del 02/10/23 con registro público en el país no comprendidos en el punto 3.5.»
- **c3d Condicion** «d) Pagos de refinanciaciones de incisos a) y c)» — Destino alternativo: pagos de refinanciaciones sin desembolso de operaciones de a) y c), siempre que no anticipen el vencimiento original. · tramo [exacta]: «Pagos a partir del vencimiento de capital o intereses de endeudamientos financieros comprendidos en el punto 3.5. que no generen desembolsos por ser refinanciaciones de capital y/o intereses de operaciones contempladas en los incisos a) y c) precedentes»
- **c3e Condicion** «e) Pagos de refinanciaciones de títulos inciso c)» — Destino alternativo: pagos de títulos con registro público local no del 3.5, en moneda extranjera, que refinancian operaciones del inciso c) sin anticipar vencimiento. · tramo [exacta]: «que no generen desembolsos por ser refinanciaciones de capital y/o intereses de operaciones contempladas en el inciso c) precedente en la medida que las refinanciaciones no anticipen el vencimiento de la deuda original.»
- **o2 Obligacion** «DDJJ de uso de fondos en inversiones» — Para la exclusión del inciso iii) el cliente debe presentar DDJJ de que los fondos de las operaciones a) a c) se usaron totalmente en pagos en el país vinculados a inversiones en Argentina. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «En todos los casos el cliente deberá presentar una declaración jurada dejando constancia de que los fondos oportunamente recibidos por las operaciones detalladas en los incisos a) a c) precedentes se utilizaron en su totalidad para concretar pagos en el país relacionados con la concreción de inversiones en la República…»
- **x4 Excepcion** «Ventas/transferencias BOPREAL suscriptores primarios» — En las DDJJ de 3.16.3.1 y 3.16.3.2 no se computan ventas con liquidación en ME o transferencias al exterior de BOPREAL realizadas por quienes participaron de la suscripción primaria, hasta el monto allí adquirido. · props: `{"umbrales": [{"tramo": "por hasta el monto adquirido en la suscripción primaria", "comparacion": "maximo_inclusivo", "base": "monto adquirido en la suscripción primaria", "regla_comparacion": "limite_relativo:compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['por hasta el monto adquirido en la suscripción primaria'] · tramo [no]: «no deberán tenerse en cuenta: […] las ventas con liquidación en moneda extranjera en el país o en el exterior de los Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) o las transferencias de estos bonos a depositarios en el exterior»
- **x5 Excepcion** «Ventas BOPREAL de importadores — DDJJ 3.16.3.1/2» — En las DDJJ de 3.16.3.1 y 3.16.3.2 no se computan ventas en el exterior o transferencias de importadores que suscribieron BOPREAL por deudas de importaciones elegibles (4.4 y 4.5), si su valor de mercado no supera la diferencia entre el valor de venta de los BOPREAL y su valor nominal, si el primero es menor. · props: `{"umbrales": [{"tramo": "cuando el valor de mercado de estas operaciones no supere a la diferencia entre el valor obtenido por la venta con liquidación en moneda extranjera en el exterior de bonos BOPREAL adquiridos en las suscripciones primarias citadas y su valor nominal", "comparacion": "maximo_inclusivo", "base": "diferencia entre el valor obtenido por la venta con liquidación en moneda extranjera en el exterior de bonos BOPREAL adquiridos", "regla_comparacion": "limite_relativo:negacion:raiz_super", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['cuando el valor de mercado de estas operaciones no supere a la diferencia entre …'] · tramo [no]: «no deberán tenerse en cuenta: […] las ventas con liquidación en moneda extranjera en el exterior o las transferencias a depositarios del exterior que concreten los importadores de bienes y servicios»
- R: c2 Condicion —condicion_de→ x2 Excepcion
- R: c3a Condicion —condicion_de→ x3 Excepcion
- R: c3b Condicion —condicion_de→ x3 Excepcion
- R: c3c Condicion —condicion_de→ x3 Excepcion
- R: c3d Condicion —condicion_de→ x3 Excepcion
- R: c3e Condicion —condicion_de→ x3 Excepcion
- R: o1 Obligacion —aplica_a→ Sujeto_cliente (mención «El cliente»)
- R: o2 Obligacion —aplica_a→ Sujeto_cliente (mención «el cliente»)
- R: x5 Excepcion —aplica_a→ Sujeto_importador (mención «los importadores de bienes y servicios»)

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «garantía desde el vencimiento» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ x2 Excepcion |
| 2 | «fondos usados en 10 días» | `dentro_de_norma` |  | dentro de la Excepcion x3 (tramo y umbral «dentro de los 10 (diez) días corridos»); sin Condicion propia (c3a–c3e son los destinos) |
| 3 | «repatriación a 1 año» | `condicion_con_relacion` |  | c3b Condicion con el umbral —condicion_de→ x3 Excepcion |
| 4 | «BOPREAL hasta el monto suscripto» | `dentro_de_norma` |  | dentro de la Excepcion x4 (umbral «por hasta el monto adquirido en la suscripción primaria»); sin Condicion |
| 5 | «valor de mercado que no supere la diferencia» | `dentro_de_norma` |  | dentro de la Excepcion x5 (umbral); sin Condicion |

## `ext::3.9::intro` — [bloque intro] Compra de moneda extranjera por parte de personas humanas residentes para la formación

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* 3.9. Compra de moneda extranjera por parte de personas humanas residentes para la formación
> *propio:* de activos externos bajo otras modalidades, la remisión de ayuda familiar u operaciones con derivados. Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de concepto A05) en la medida que no encuadre en el punto 3.12.1., sin la conformidad previa del BCRA, en la medida que se cumplan la totalidad de los siguientes requisitos:

### Extracción (código K)

- **p1 Potestad** «Acceso sin conformidad previa BCRA — personas humanas residentes» — Las entidades podrán dar acceso al mercado de cambios, sin la conformidad previa del BCRA, a las personas humanas residentes para la formación de activos externos (códigos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y la operatoria con derivados (código A05) en la medida que no encuadre en el punto 3.12.1., siempre que se cumplan la totalidad de los requisitos enumerado… · no definidas: `{"cuantificador_requisitos": "la totalidad de los siguientes requisitos"}` · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes»
- **o1 Operacion** «Formación de activos externos — personas humanas residentes» — Acceso al mercado de cambios de personas humanas residentes para formación de activos externos, códigos A01, A02, A03, A04, A06, A08, A14 y A24 · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24)»
- **o2 Operacion** «Remisión de ayuda familiar — personas humanas residentes» — Acceso al mercado de cambios de personas humanas residentes para la remisión de ayuda familiar · props: `{"tipo": "transferencia al exterior"}` · tramo [exacta]: «la remisión de ayuda familiar»
- **o3 Operacion** «Operatoria con derivados A05 — personas humanas residentes» — Acceso al mercado de cambios de personas humanas residentes para operatoria con derivados (código A05) que no encuadre en el punto 3.12.1. · props: `{"tipo": "operación con derivados"}` · tramo [exacta]: «para la operatoria con derivados (código de concepto A05) en la medida que no encuadre en el punto 3.12.1.»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)
- R: Sujeto_persona_humana (mención «personas humanas residentes») —ejecuta→ o1 Operacion
- R: Sujeto_persona_humana (mención «personas humanas residentes») —ejecuta→ o2 Operacion
- R: Sujeto_persona_humana (mención «personas humanas residentes») —ejecuta→ o3 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes» — Potestad → Operacion (habilita el acceso para formación de activos externos, ayuda familiar y derivados: o1, o2, o3); no hay predicado Potestad→Operacion

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

### Extracción (código K)

- **e1 Operacion** «Cancelación de consumos en moneda extranjera con tarjeta» — Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o de compra · props: `{"tipo": "cancelación de consumos con tarjeta"}` · tramo [exacta]: «Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o»
- **e2 Condicion** «Emisor de la tarjeta es entidad financiera» — Supuesto: el emisor de la tarjeta es una entidad financiera. · tramo [exacta]: «Cuando el emisor de la tarjeta sea una entidad financiera»
- **e3 Potestad** «Cancelación en moneda extranjera o pesos — titular» — El titular de la tarjeta emitida por una entidad financiera puede cancelar los consumos realizados en moneda extranjera en esa moneda o en pesos. · tramo [exacta]: «el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- **e4 Restriccion** «Tope tipo de cambio vendedor — cancelación en pesos» — Si se cancela en pesos, se aplica como máximo el tipo de cambio vendedor de la entidad emisora (ventanilla o medios electrónicos, según corresponda) del momento de cancelación, o del día hábil inmediato anterior si el pago se efectúa un día inhábil. · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "como máximo en este caso el tipo de\ncambio vendedor", "comparacion": "maximo_inclusivo", "base": "en este caso el tipo de cambio vendedor", "regla_comparacion": "limite_relativo:compuesta:como_maximo", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['como máximo en este caso el tipo de cambio vendedor'] · tramo [exacta]: «debiendo aplicar como máximo en este caso el tipo de cambio vendedor (aplicable para operaciones efectuadas por ventanilla o a través de medios electrónicos, según corresponda) de la entidad emisora de la tarjeta del momento de cancelación»
- **e5 Condicion** «Pago en día inhábil — tipo de cambio día hábil anterior» — Cuando el pago se efectúa un día inhábil, el tipo de cambio de referencia es el del día hábil inmediato anterior. · tramo [exacta]: «o día hábil inmediato anterior cuando el pago se efectúe un día inhábil»
- **e6 Condicion** «Débito automático en cuentas de la entidad emisora» — Supuesto: los clientes pactaron el débito automático del resumen en cuentas de la propia entidad emisora. · tramo [exacta]: «En los casos donde los clientes hayan pactado el débito automático del resumen de la tarjeta en cuentas de la propia entidad emisora»
- **e7 Obligacion** «Tipo de cambio electrónico cierre día de pago — débito automático» — En débito automático en cuentas de la entidad emisora, se aplica el tipo de cambio vendedor para operaciones por medios electrónicos de pago del cierre del mismo día hábil del pago. · props: `{"tipo": "calculo"}` · tramo [exacta]: «aplicará el tipo de cambio vendedor para operaciones efectuadas a través de medios electrónicos de pago del cierre del mismo día hábil del pago»
- R: e2 Condicion —condicion_de→ e3 Potestad
- R: e5 Condicion —condicion_de→ e4 Restriccion
- R: e6 Condicion —condicion_de→ e7 Obligacion
- R: e3 Potestad —aplica_a→ Sujeto (mención «el titular»)
- R: e4 Restriccion —aplica_a→ Sujeto (mención «la entidad emisora de la tarjeta»)
- R: e4 Restriccion —limita→ e1 Operacion
- R: e7 Obligacion —regula→ e1 Operacion
- R: Sujeto (mención «el titular») —ejecuta→ e1 Operacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «emisor entidad financiera» | `condicion_con_relacion` |  | e2 Condicion —condicion_de→ e3 Potestad |
| 2 | «pago en día inhábil» | `condicion_con_relacion` |  | e5 Condicion «Pago en día inhábil — tipo de cambio día hábil anterior» —condicion_de→ e4 Restriccion |
| 3 | «débito automático pactado» | `condicion_con_relacion` |  | e6 Condicion —condicion_de→ e7 Obligacion |

## `ext::4.1.3.2` — Cuando se trate de empresas no financieras emisoras de tarjetas de crédito

Grupos: grupo_c.

### Texto

> *heredado:* Sección 4. Otras disposiciones específicas.
> *heredado:* 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tarjetas de
> *heredado:* crédito, compra y prepagas emitidas en el país.
> *heredado:* 4.1.3. Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o
> *heredado:* de compra.
> *propio:* 4.1.3.2. Cuando se trate de empresas no financieras emisoras de tarjetas de crédito y/o compra, el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos –siendo aplicable el tipo de cambio vendedor por canales electrónicos publicado por el Banco de la Nación Argentina el mismo día hábil de la fecha de pago o hábil inmediato anterior cuando el pago se efectúe un día inhábil–.

### Extracción (código K)

- **e1 Operacion** «Cancelación de consumos en moneda extranjera con tarjeta» — Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o de compra · props: `{"tipo": "cancelacion de consumos con tarjeta"}` · tramo [exacta]: «Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o»
- **e2 Potestad** «Cancelación en moneda extranjera o pesos — tarjetas de empresas no financieras» — Si la tarjeta de crédito y/o compra la emite una empresa no financiera, el titular puede cancelar los consumos en moneda extranjera en esa moneda o en pesos. En pesos se aplica el tipo de cambio vendedor por canales electrónicos que publica el Banco de la Nación Argentina el mismo día hábil de la fecha de pago, o el del día hábil inmediato anterior si el pago se hace un día inhábil. · tramo [exacta]: «el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- **e3 Condicion** «Emisor es empresa no financiera de tarjetas» — Supuesto: la emisora de la tarjeta de crédito y/o compra es una empresa no financiera. · tramo [exacta]: «Cuando se trate de empresas no financieras emisoras de tarjetas de crédito y/o compra»
- R: e3 Condicion —condicion_de→ e2 Potestad
- R: e2 Potestad —aplica_a→ Sujeto (mención «el titular»)
- Omisión `relacion_sin_predicado` [exacta]: «el titular podrá cancelar los consumos realizados en moneda extranjera» — Potestad → Operacion (habilita la operación); no hay predicado para unirlas.

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «emisoras no financieras» | `condicion_con_relacion` |  | e3 Condicion «Emisor es empresa no financiera de tarjetas» —condicion_de→ e2 Potestad |
| 2 | «pago en día inhábil» | `dentro_de_norma` |  | dentro de la Potestad e2 (descripción); sin Condicion |

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

### Extracción (código K)

- **c1 Condicion** «Ordenante empresa del exterior firmante — boleto global procesadoras» — Una de las condiciones que deben cumplirse todas juntas para que el ingreso de divisas a través de una empresa procesadora de pagos pueda registrarse en un boleto global diario a nombre de su representante local: las transferencias deben tener como ordenante a la empresa del exterior que firmó el acuerdo. · tramo [exacta]: «Las transferencias tengan como ordenante la empresa del exterior firmante del acuerdo»
- **c2 Condicion** «Canalización vía entidad del exterior con matriz Basilea» — Una de las condiciones que deben cumplirse todas juntas para emitir el boleto global diario por ingresos a través de procesadoras de pagos: las transferencias deben canalizarse a través de una entidad financiera del exterior cuya casa matriz o controlante esté radicada en un país miembro del Comité de Supervisión Bancaria de Basilea. · tramo [exacta]: «se canalicen a través de una entidad financiera del exterior cuya casa matriz o controlante se encuentre radicada en un país miembro del Comité de Supervisión Bancaria de Basilea»

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:6 | sí | «5.8.2.2. Las transferencias tengan como ordenante la empresa del exterior firmante del acuerdo y se canalicen a través de una entidad financiera del exterior cu…» | `extraida_tramo_verificado` |  | c1 y c2 Condicion [exacta]: entre las dos cubren la oración (ordenante; canalización) |

## `ext::7.1.1.5` — 365 (trescientos sesenta y cinco) días corridos para las operaciones que se

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.1. Obligación de ingreso y liquidación en los plazos establecidos.
> *heredado:* 7.1.1. Exportaciones oficializadas a partir del 02/09/19.
> *heredado:* El contravalor en divisas de la exportación hasta alcanzar el valor facturado según la condición de venta pactada deberá ingresarse al país y liquidarse en el mercado de cambios. En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicios resultará aplicable lo dispuesto en los puntos 14.1.1. y 14.1.2., según corresponda. El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse en los siguientes plazos a computar desde la fecha del cumplido de embarque otorgado por la Aduana:
> *heredado:* Independientemente de los plazos máximos precedentes, los cobros de exportaciones deberán ser ingresados y liquidados en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro. La posibilidad de utilizar este plazo quedará supeditada en todos los casos al cumplimiento de los plazos previstos en los puntos 7.1.1.1. a 7.1.1.5. Los montos en moneda extranjera originados en cobros de siniestros por coberturas contratadas, en la medida que los mismos cubran el valor de los bienes exportados, están alcanzados por esta obligación. El exportador deberá seleccionar una entidad para que realice el "Seguimiento de las negociaciones de divisas por exportaciones de bienes". La obligación de ingreso y liquidación de divisas de un permiso de embarque se considerará cumplida cuando la entidad haya certificado tal situación por los mecanismos establecidos a tal efecto.
> *propio:* 7.1.1.5. 365 (trescientos sesenta y cinco) días corridos para las operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE", independientemente del tipo de bien exportado.

### Extracción (código K)

- **e1 Obligacion** «Plazo 365 días EXPORTA SIMPLE — ingreso y liquidación divisas» — El ingreso y la liquidación por el mercado de cambios de las divisas de exportaciones de bienes oficializadas a partir del 02/09/19 deberá concretarse dentro de 365 días corridos, contados desde la fecha del cumplido de embarque otorgado por la Aduana, en las operaciones concretadas en el marco del régimen "EXPORTA SIMPLE", sea cual sea el tipo de bien exportado. · props: `{"tipo": "otra"}` · umbral: ['365 (trescientos sesenta y cinco) días corridos'] · tramo [exacta]: «El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse en los siguientes plazos a computar desde la fecha del cumplido de embarque otorgado por la Aduana: […] 365 (trescientos sesenta y cinco) días corridos para las operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE", ind…»
- **e2 Operacion** «Ingreso y liquidación divisas exportación EXPORTA SIMPLE» — Ingreso y liquidación en el mercado de cambios del contravalor de exportaciones de bienes concretadas en el marco del régimen EXPORTA SIMPLE, sea cual sea el tipo de bien · props: `{"tipo": "ingreso y liquidación de divisas de exportación"}` · tramo [exacta]: «operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE"»
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

### Extracción (código K)

- **op1 Operacion** «Ingreso y liquidación de anticipos/prefinanciaciones del exterior» — Ingreso y liquidación en el mercado de cambios de anticipos, prefinanciaciones y posfinanciaciones del exterior de exportaciones de bienes · props: `{"tipo": "ingreso y liquidación de divisas"}` · tramo [exacta]: «Los anticipos, prefinanciaciones y posfinanciaciones del exterior deberán ser ingresadas y liquidadas en el mercado de cambios»
- **ob1 Obligacion** «Plazo 20 días hábiles — liquidar anticipos y financiaciones del exterior» — Los anticipos, prefinanciaciones y posfinanciaciones del exterior deben ingresarse y liquidarse en el mercado de cambios dentro de los 20 días hábiles de la fecha de cobro o desembolso en el exterior. · props: `{"tipo": "otra"}` · umbral: ['dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el e…'] · tramo [exacta]: «Los anticipos, prefinanciaciones y posfinanciaciones del exterior deberán ser ingresadas y liquidadas en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el exterior.»
- **ex1 Excepcion** «VPU RIGI con beneficios art. 198 — régimen 14.1.4» — Cuando el cliente es un VPU adherido al RIGI que declaró prever usar los beneficios del art. 198 de la Ley 27.742 en cobro de exportaciones, en lugar del plazo de 20 días hábiles rige lo dispuesto en el punto 14.1.4. · tramo [exacta]: «En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servici…»
- **c1 Condicion** «Cliente VPU RIGI que declaró usar art. 198» — El cliente es un VPU adherido al RIGI que declaró ante la Autoridad de Aplicación que preveía usar los beneficios del art. 198 de la Ley 27.742 en materia de cobro de exportaciones. · tramo [exacta]: «el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742»
- **l1 Comunicacion** «Ley 27.742» —  · props: `{"codigo": "Ley 27.742", "tipo": "externa"}` · tramo [exacta]: «Ley 27.742»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ex1 Excepcion —exceptua_obligacion→ ob1 Obligacion
- R: c1 Condicion —condicion_de→ ex1 Excepcion
- R: ex1 Excepcion —aplica_a→ Sujeto_vpu_rigi (mención «un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI)»)
- R: to TextoOrdenado —referencia→ l1 Comunicacion

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

### Extracción (código K)

- **op1 Operacion** «Ingreso de fondos propios imputable a permiso de embarque» — Ingreso de fondos propios de los exportadores, desde sus cuentas en el exterior, imputable al cumplimiento de la obligación de liquidación de un permiso de embarque · props: `{"tipo": "ingreso de fondos del exterior imputable al cumplimiento de la obligación de liquidación"}` · tramo [exacta]: «Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación.»
- **c1 Condicion** «Anticipo desde cuentas propias en el exterior» — Que los exportadores anticipen fondos desde sus cuentas en el exterior para cumplir la obligación de liquidación de exportaciones ya realizadas y pendientes de cobro · tramo [exacta]: «Cuando los exportadores anticipen fondos desde sus cuentas en el exterior a los fines de dar cumplimiento a la obligación de liquidación de exportaciones realizadas y pendientes de cobro.»
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: Sujeto_exportador (mención «los exportadores») —ejecuta→ op1 Operacion

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:15 | no | «7.2.2. Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación.» | `extraida_tramo_verificado` |  | op1 Operacion [exacta] con tramo «Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación.» |

## `ext::7.5.3` — Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.5. Ampliaciones del plazo para el ingreso y liquidación de divisas.
> *heredado:* La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias:
> *propio:* 7.5.3. Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los endeudamientos financieros referidas en los puntos 7.3.5., 7.9. y 7.11. y las prefinanciaciones de exportaciones comprendidas en el punto 7.8.5. En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento del plazo para la liquidación de divisas del permiso, el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha. Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario.

### Extracción (código K)

- **e1 Potestad** «Extensión de plazo por fondos retenidos en cuentas» — La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación para permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a endeudamientos financieros (puntos 7.3.5., 7.9. y 7.11.) y prefinanciaciones de exportaciones (punto 7.8.5.). · tramo [exacta]: «La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias: […] Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los endeudamientos financieros referidas en los puntos 7.3.5., 7.9. y 7.11. y las prefinanciacio…»
- **e2 Potestad** «Solicitud de ampliación hasta quinto día hábil» — El exportador podrá solicitar que el plazo de liquidación del permiso sea ampliado hasta el quinto día hábil posterior a la fecha hasta la cual los cobros deben permanecer depositados según el contrato de financiamiento. · tramo [exacta]: «el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha.»
- **e3 Condicion** «Fecha de depósito posterior al vencimiento del plazo» — Que la fecha hasta la cual los cobros deben permanecer depositados por el contrato de financiamiento sea posterior al vencimiento del plazo de liquidación del permiso. · tramo [exacta]: «En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento del plazo para la liquidación de divisas del permiso»
- **e4 Restriccion** «Tope 125% servicios de capital e intereses — ampliación» — La opción de ampliación está disponible hasta alcanzar el 125% de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 meses calendario. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capi…', 'el mes corriente y los siguientes 6 (seis) meses calendario'] · tramo [exacta]: «Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario.»
- **e5 Operacion** «Ampliación del plazo de liquidación de divisas» — Ampliación del plazo de ingreso y liquidación de divisas de un permiso de exportación con fondos retenidos en cuentas de financiamiento. · props: `{"tipo": "ampliación de plazo"}` · tramo [exacta]: «que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha»
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

### Extracción (código K)

- **e1 Operacion** «Aplicación de cobros de exportación a operaciones financieras habilitadas» — Operaciones para las que los exportadores ejercen la opción prevista en el punto 7.9 de aplicar cobros de exportaciones de bienes y servicios · props: `{"tipo": "aplicación de cobros de exportaciones"}` · tramo [exacta]: «aquellas operaciones para las cuales los exportadores hagan ejercicio de la opción prevista en el presente punto»
- **e2 Obligacion** «Remisión de certificación de encuadre al BCRA» — La entidad financiera designada debe remitir por nota a la Gerencia Principal de Exterior y Cambios la certificación de que se cumplen las condiciones de encuadre de la operación, dentro de los 90 días corridos posteriores al primer ingreso de fondos · props: `{"tipo": "reporte_al_supervisor"}` · umbral: ['dentro de los 90 (noventa) días corridos posteriores al primer ingreso de fondos'] · tramo [exacta]: «la entidad financiera designada deberá remitir, por nota dirigida a la Gerencia Principal de Exterior y Cambios dentro de los 90 (noventa) días corridos posteriores al primer ingreso de fondos, la correspondiente certificación de que se cumplen las condiciones que permiten encuadrar la operación»
- **e3 Obligacion** «Contenido mínimo de la certificación» — La certificación debe contener como mínimo el punto normativo de encuadre, el número de identificación en el Seguimiento de anticipos y otras financiaciones de exportación de bienes y, si hay endeudamientos con cuentas de garantía o específicas, el tipo de cuenta y la entidad financiera local o del exterior · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «La certificación que se presente en el BCRA deberá contener como mínimo, el detalle del punto normativo en que encuadra la operación, su número de identificación en el marco del "Seguimiento de anticipos y otras financiaciones de exportación de bienes" y, si existen endeudamientos que contemplen el mantenimiento de cue…»
- **e4 Condicion** «Endeudamientos con cuentas de garantía o específicas» — Existencia de endeudamientos que contemplen cuentas de garantía o cuentas específicas sin estar en garantía · tramo [exacta]: «si existen endeudamientos que contemplen el mantenimiento de cuentas de garantías o cuentas específicas sin estar en garantía»
- **e5 Obligacion** «Número APX o ECO como identificación» — Consignar número APX para operaciones con liquidación en el mercado, o número ECO para operaciones sin liquidación por ser refinanciaciones de deudas preexistentes · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «El número de identificación a consignar será el número APX para las operaciones con liquidación en el mercado o el número ECO (Entidad-CUIT-N° Operación) para aquellas operaciones sin liquidaciones por ser refinanciaciones de deudas preexistentes»
- **e6 Obligacion** «Certificación adicional de elegibilidad del proyecto» — Para financiación de proyectos del punto 7.9.2, la entidad debe remitir además certificación de elegibilidad del proyecto con descripción, monto proyectado a invertir y composición del financiamiento · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «la entidad deberá adicionalmente remitir la certificación del cumplimiento de las condiciones para la elegibilidad del proyecto, la cual deberá contener, como mínimo, la descripción de éste, el monto proyectado a invertir y la composición del financiamiento»
- **e7 Condicion** «Financiación de proyectos del punto 7.9.2» — Operaciones destinadas a financiar proyectos comprendidos en el punto 7.9.2 · tramo [exacta]: «En el caso de que se trate de operaciones destinadas a la financiación de proyectos comprendidos en el punto 7.9.2.»
- **e8 Obligacion** «Bases de proyección de la certificación» — La certificación debe basarse en proyecciones de aumento anual de producción exportable o sustitutiva de importaciones, ventas externas, proporción a cubrir con el nuevo proyecto, flujos de divisas esperados y afectados a servicios del financiamiento · props: `{"tipo": "otra"}` · tramo [exacta]: «La certificación que emita la entidad financiera deberá basarse en las proyecciones sobre el aumento anual esperado en la producción de bienes exportables»
- **e9 Obligacion** «Solicitud de dictámenes profesionales» — La entidad solicitará los dictámenes profesionales que estime necesarios sobre razonabilidad y genuinidad económica y financiera de la operación · props: `{"tipo": "otra"}` · tramo [exacta]: «La entidad solicitará los dictámenes profesionales que estime necesarios para asegurar la razonabilidad y genuinidad de la operación en los aspectos económicos y financieros»
- **e10 Obligacion** «Dictámenes técnicos complementarios del proyecto» — Los dictámenes deben complementarse con dictámenes técnicos del proyecto cuando éste no cuente con aprobación en términos de la Ley 26.360 · props: `{"tipo": "otra"}` · tramo [exacta]: «que deberán ser complementados con dictámenes sobre los aspectos técnicos del proyecto»
- **e11 Condicion** «Proyecto sin aprobación Ley 26.360» — El proyecto no cuenta con aprobación en los términos de la Ley 26.360 · tramo [exacta]: «cuando el mismo no cuente con la aprobación en los términos de la Ley 26.360»
- **e12 Obligacion** «Archivo de documentación a disposición del BCRA» — Documentación y hojas de trabajo que avalan la certificación deben quedar archivadas en la entidad a disposición del BCRA · props: `{"tipo": "otra"}` · tramo [exacta]: «La documentación utilizada por la entidad financiera y hojas de trabajo que avalan la emisión de la certificación deberá quedar archivada en la entidad a disposición del BCRA»
- **c1 Comunicacion** «Ley 26.360» —  · props: `{"codigo": "Ley 26.360", "tipo": "externa"}` · tramo [exacta]: «Ley 26.360»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: Sujeto_exportador (mención «los exportadores») —ejecuta→ e1 Operacion
- R: e1 Operacion —requiere→ e2 Obligacion
- R: e2 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera designada»)
- R: e4 Condicion —condicion_de→ e3 Obligacion
- R: e6 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: e7 Condicion —condicion_de→ e6 Obligacion
- R: e8 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: e9 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: e10 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: e11 Condicion —condicion_de→ e10 Obligacion
- R: e12 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «endeudamientos con cuentas de garantía» | `condicion_con_relacion` |  | e4 Condicion «Endeudamientos con cuentas de garantía o específicas» —condicion_de→ e3 Obligacion |
| 2 | «proyectos del 7.9.2» | `condicion_con_relacion` |  | e7 Condicion —condicion_de→ e6 Obligacion |
| 3 | «proyecto sin aprobación de la Ley 26.360» | `condicion_con_relacion` |  | e11 Condicion —condicion_de→ e10 Obligacion |

## `ext::8.4.2` — Determinación del plazo para el ingreso y liquidación de las divisas.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
> *heredado:* 8.4. Responsabilidades de la entidad nominada para el seguimiento del permiso.
> *propio:* 8.4.2. Determinación del plazo para el ingreso y liquidación de las divisas. La entidad deberá determinar el plazo aplicable a cada exportación a partir de lo dispuesto en el punto 7.1.1. En el caso de que una exportación esté compuesta por distintos productos, el plazo aplicable será aquel que representa una mayor proporción del valor FOB total de la exportación. La fecha de vencimiento que le corresponde a una exportación será aquella resultante de sumar el plazo aplicable a la fecha de cumplido de embarque otorgada por la Aduana. Si la fecha resultante fuese un día no hábil, el vencimiento se trasladará al primer día hábil siguiente. En caso de que exista una ampliación del plazo para un producto, el nuevo plazo se aplicará tanto a las exportaciones embarcadas a partir de la vigencia de la ampliación como a las embarcadas previamente cuyo plazo para ingresar y liquidar no se encontrase vencido a ese momento. En tanto en caso de existir una reducción del plazo vigente, el plazo reducido sólo regirá para las operaciones que se oficialicen a partir de la vigencia del nuevo plazo.

### Extracción (código K)

- **op1 Operacion** «Ingreso y liquidación de divisas de exportación» — Ingreso y liquidación en el mercado de cambios de las divisas por exportaciones de bienes, sujeto a seguimiento por la entidad nominada · props: `{"tipo": "ingreso y liquidación de divisas"}` · tramo [exacta]: «Determinación del plazo para el ingreso y liquidación de las divisas.»
- **o1 Obligacion** «Determinar plazo aplicable a cada exportación» — La entidad nominada para el seguimiento del permiso debe determinar el plazo aplicable a cada exportación según lo dispuesto en el punto 7.1.1. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La entidad deberá determinar el plazo aplicable a cada exportación a partir de lo dispuesto en el punto 7.1.1.»
- **o2 Obligacion** «Plazo de producto con mayor proporción FOB» — Si la exportación está compuesta por distintos productos, el plazo aplicable es el del producto que representa la mayor proporción del valor FOB total. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el plazo aplicable será aquel que representa una mayor proporción del valor FOB total de la exportación.»
- **c1 Condicion** «Exportación compuesta por distintos productos» — Supuesto de exportación compuesta por distintos productos. · tramo [exacta]: «En el caso de que una exportación esté compuesta por distintos productos»
- **o3 Obligacion** «Vencimiento: plazo más fecha de cumplido de embarque» — La fecha de vencimiento resulta de sumar el plazo aplicable a la fecha de cumplido de embarque otorgada por la Aduana. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La fecha de vencimiento que le corresponde a una exportación será aquella resultante de sumar el plazo aplicable a la fecha de cumplido de embarque otorgada por la Aduana.»
- **o4 Obligacion** «Traslado del vencimiento al primer día hábil» — Si la fecha resultante es día no hábil, el vencimiento se traslada al primer día hábil siguiente. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el vencimiento se trasladará al primer día hábil siguiente.»
- **c2 Condicion** «Fecha resultante en día no hábil» — Supuesto de que la fecha de vencimiento resultante sea día no hábil. · tramo [exacta]: «Si la fecha resultante fuese un día no hábil»
- **o5 Obligacion** «Ampliación de plazo: aplica a embarques previos no vencidos» — Ante una ampliación del plazo para un producto, el nuevo plazo se aplica a exportaciones embarcadas desde la vigencia de la ampliación y a las previas cuyo plazo no estuviera vencido. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el nuevo plazo se aplicará tanto a las exportaciones embarcadas a partir de la vigencia de la ampliación como a las embarcadas previamente cuyo plazo para ingresar y liquidar no se encontrase vencido a ese momento.»
- **c3 Condicion** «Ampliación del plazo para un producto» — Supuesto de ampliación del plazo para un producto. · tramo [exacta]: «En caso de que exista una ampliación del plazo para un producto»
- **o6 Obligacion** «Reducción de plazo: solo operaciones oficializadas posteriores» — Ante una reducción del plazo vigente, el plazo reducido rige solo para operaciones oficializadas a partir de la vigencia del nuevo plazo. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el plazo reducido sólo regirá para las operaciones que se oficialicen a partir de la vigencia del nuevo plazo.»
- **c4 Condicion** «Reducción del plazo vigente» — Supuesto de reducción del plazo vigente. · tramo [exacta]: «en caso de existir una reducción del plazo vigente»
- R: o1 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: o1 Obligacion —regula→ op1 Operacion
- R: c1 Condicion —condicion_de→ o2 Obligacion
- R: c2 Condicion —condicion_de→ o4 Obligacion
- R: c3 Condicion —condicion_de→ o5 Obligacion
- R: c4 Condicion —condicion_de→ o6 Obligacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «exportación de varios productos» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ o2 Obligacion |
| 2 | «fecha no hábil» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ o4 Obligacion |
| 3 | «ampliación del plazo» | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ o5 Obligacion |
| 4 | «reducción del plazo» | `condicion_con_relacion` |  | c4 Condicion —condicion_de→ o6 Obligacion |

## `ext::8.5.18.1` — La documentación permite constatar que la entrega de la mercadería

Grupos: omisiones.

### Texto

> *heredado:* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
> *heredado:* 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
> *heredado:* La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque cuando cuente con los elementos que le permitan considerar que la operación se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las condiciones previstas en cada caso. La documentación utilizada para certificar el concepto y monto de las divisas imputado en cada caso deberá quedar archivada en la entidad a disposición del BCRA.
> *heredado:* 8.5.18. Cobros locales por exportaciones del régimen de ranchos a medios de transporte de
> *heredado:* bandera extranjera. La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque por el valor equivalente a los montos abonados localmente en pesos y/o en moneda extranjera al exportador por un agente local de la empresa propietaria de los medios de transporte de bandera extranjera, en la medida que se verifiquen las siguientes condiciones:
> *propio:* 8.5.18.1. La documentación permite constatar que la entrega de la mercadería exportada se ha producido en el país, que el agente local de la empresa propietaria de los medios de transporte de bandera extranjera ha realizado localmente el pago al exportador y la moneda en la que dicho pago se efectuó.

### Extracción (código K)

- **c1 Condicion** «Documentación constata entrega local, pago y moneda» — Supuesto para que la entidad pueda considerar cumplido el seguimiento del permiso de embarque por cobros locales de exportaciones del régimen de ranchos: que la documentación permita constatar tres cosas: que la mercadería exportada se entregó en el país, que el agente local de la empresa propietaria de los medios de transporte de bandera extranjera pagó localmente al exportador, y en qué moneda s… · tramo [exacta]: «La documentación permite constatar que la entrega de la mercadería exportada se ha producido en el país, que el agente local de la empresa propietaria de los medios de transporte de bandera extranjera ha realizado localmente el pago al exportador y la moneda en la que dicho pago se efectuó.»

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

### Extracción (código K)

- **c1 Comunicacion** «Decreto 929/13» —  · props: `{"codigo": "Decreto 929/13", "tipo": "externa"}` · tramo [exacta]: «Decreto 929/13»
- **c2 Comunicacion** «Resolución 26/23 Secretaría de Energía» —  · props: `{"codigo": "Resolución 26/23 de la Secretaría de Energía", "tipo": "externa"}` · tramo [exacta]: «Resolución 26/23 de la Secretaría de Energía»
- **op1 Operacion** «Cumplimiento seguimiento permiso de embarque — Decreto 929/13» — Considerar cumplimentado el seguimiento de un permiso de embarque por la parte amparada por un Certificado DECRETO 929/13 · props: `{"tipo": "seguimiento de negociación de divisas por exportaciones"}` · tramo [exacta]: «considerar cumplimentado el seguimiento de un permiso de embarque»
- **p1 Potestad** «Imputación por Certificado Decreto 929/13 — seguimiento» — A pedido de un cliente con proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13), la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso amparada por un "Certificado DECRETO 929/13" emitido según la Resolución 26/23 de la Secretaría de Energía. · tramo [exacta]: «la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso que se encuentre amparado por un "Certificado DECRETO 929/13"»
- **k1 Condicion** «Pedido de cliente con proyecto Decreto 929/13» — Que lo pida un cliente que posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13). · tramo [exacta]: «A pedido de un cliente que posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos establecido por el Decreto 929/13»
- **k2 Condicion** «Certificado DECRETO 929/13 según Resolución 26/23» — Parte del permiso amparada por un Certificado DECRETO 929/13 emitido a partir de la Resolución 26/23 de la Secretaría de Energía. · tramo [exacta]: «amparado por un "Certificado DECRETO 929/13" emitido a partir de lo dispuesto por la Resolución 26/23 de la Secretaría de Energía»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: to TextoOrdenado —referencia→ c2 Comunicacion
- R: k1 Condicion —condicion_de→ p1 Potestad
- R: k2 Condicion —condicion_de→ p1 Potestad
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «la entidad») —ejecuta→ op1 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «la entidad podrá considerar cumplimentado el seguimiento» — Vínculo Potestad → Operacion habilitada; no hay predicado

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

### Extracción (código K)

- **e1 Operacion** «Préstamos financieros vigentes al 31/08/19 aplicados a exportaciones» — Operación comprendida en el seguimiento de financiaciones de exportación de bienes (Sección 9): préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones, y que el exportador pida aplicar a permisos de embarque oficializados a partir del 02/09/19. · props: `{"tipo": "financiación de exportación de bienes"}` · tramo [exacta]: «Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones»
- **e2 Condicion** «Contrato vigente al 31/08/19 con aplicación de exportaciones en el exterior» — El contrato del préstamo financiero estaba vigente al 31/08/19 y sus condiciones prevén atender los servicios aplicando en el exterior el flujo de fondos de exportaciones. · tramo [exacta]: «con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones»
- **e3 Condicion** «Solicitud del exportador: permisos oficializados desde 02/09/19» — El exportador pide que el préstamo se aplique a permisos de embarque oficializados a partir del 02/09/19. · tramo [exacta]: «para los cuales el exportador solicite su aplicación a permisos de embarque oficializados a partir del 02/09/19»
- R: e2 Condicion —condicion_de→ e1 Operacion
- R: e3 Condicion —condicion_de→ e1 Operacion
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

### Extracción (código K)

- **c1 Condicion** «Pasivo en pesos declarado en Relevamiento» — Supuesto de la facultad de la entidad de emitir la certificación de aplicación por repatriaciones de aportes de inversión directa de no residentes (punto 9.3.10): que la entidad cuente con documentación que le permita verificar que el pasivo en pesos con el exterior, generado desde la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda, se encuentra decl… · tramo [exacta]: «el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda. Se encuentra declarado en la última presentación vencida del "Relevamiento de activos y pasivos externos", en caso de corresponder»

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

### Extracción (código K)

- **e1 Operacion** «Certificación de aplicación de divisas a utilidades» — Emisión por la entidad de certificaciones de aplicación de las divisas de cobros de exportaciones al pago de utilidades y dividendos a accionistas no residentes, en el marco del punto 7.10. · props: `{"tipo": "certificación de aplicación de cobros de exportaciones"}` · tramo [exacta]: «emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes»
- **e2 Potestad** «Facultad de certificar aplicación a utilidades y dividendos» — La entidad podrá emitir certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes, siempre que se cumplan la totalidad de las condiciones enumeradas en los ítems siguientes (exigidas en forma concurrente). · tramo [exacta]: «La entidad podrá emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes»
- R: e2 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ e1 Operacion
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

### Extracción (código K)

- **e1 Operacion** «Certificación de aplicación — títulos de deuda en moneda extranjera» — Emisión de certificaciones de aplicación de divisas a la cancelación de títulos de deuda con registro público en el país denominados en moneda extranjera admitidos en el punto 7.9 · props: `{"tipo": "certificación de aplicación de cobros de exportaciones"}` · tramo [exacta]: «La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación»
- **e2 Potestad** «Facultad de certificar aplicación — títulos de deuda» — La entidad podrá emitir certificaciones de aplicación de divisas a la cancelación de títulos de deuda (punto 7.9) a partir del vencimiento del capital, intereses y otros conceptos admitidos · tramo [exacta]: «La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación a partir del vencimiento del capital, intereses y otros conceptos admitidos»
- **c1 Condicion** «Condiciones del punto 9.3.1 verificadas» — Que la entidad verifique las condiciones indicadas en el punto 9.3.1 · tramo [exacta]: «en la medida que verifique las condiciones indicadas en el punto 9.3.1.»
- **c2 Condicion** «Cancelación desde fecha de vencimiento constatada» — Que la entidad constate que la cancelación tuvo lugar a partir de la fecha de vencimiento · tramo [exacta]: «constate que la cancelación tuvo lugar a partir de la fecha de vencimiento»
- **c3 Condicion** «Documentación de requisitos del punto 7.9» — Que la entidad cuente con la documentación que verifica el cumplimiento de los requisitos del punto 7.9 · tramo [exacta]: «cuente con la documentación que verifican el cumplimiento de los requisitos establecidos en el punto 7.9.»
- R: e2 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ e1 Operacion
- R: c1 Condicion —condicion_de→ e2 Potestad
- R: c2 Condicion —condicion_de→ e2 Potestad
- R: c3 Condicion —condicion_de→ e2 Potestad
- Omisión `relacion_sin_predicado` [exacta]: «La entidad podrá emitir las certificaciones de aplicación» — Potestad → Operacion habilitada; no hay predicado Potestad→Operacion

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

### Extracción (código K)

- **e1 Obligacion** «Prevención de conflictos de intereses — procedimientos Alta Gerencia» — Recomendación (buena práctica, no deber): el Directorio se asegurará de que la Alta Gerencia implemente procedimientos que prevengan y/o limiten conflictos de intereses entre la entidad financiera, el Directorio, la Alta Gerencia y el grupo económico al que pertenece la entidad, por poder afectar negativamente la calidad del gobierno societario. · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "se considera como bue-\nna práctica", "modalidad_clasificada": "recomendacion"}` · tramo [no]: «se considera como buena práctica que el Directorio apruebe y supervise los objetivos estratégicos y los valores societarios, comunicándolos a toda la organización. A esos efectos, el Directorio: […] Se asegurará de que la Alta Gerencia implemente procedimientos para promover con- […] 2.3.2.1. Conflictos de intereses en…»
- R: e1 Obligacion —aplica_a→ Sujeto_directorio (mención «el Directorio»)
- R: e1 Obligacion —aplica_a→ Sujeto_alta_gerencia (mención «la Alta Gerencia»)

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

### Extracción (código K)

- **e1 Obligacion** «Uso efectivo de auditorías y control interno» — Recomendación (buena práctica), no un deber: la Alta Gerencia será responsable de utilizar efectivamente el trabajo llevado a cabo por las auditorías interna y externa y las funciones relacionadas con el sistema de control interno, conforme a lo establecido en la Sección 5. · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "como una buena práctica", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «La Alta Gerencia, como una buena práctica, será responsable de: […] Utilizar efectivamente el trabajo llevado a cabo por las auditorías interna y externa y las funciones relacionadas con el sistema de control interno, conforme a lo establecido en la Sección 5.»
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

### Extracción (código K)

- **op1 Operacion** «Adopción de principales decisiones gerenciales» — Adopción de las principales decisiones gerenciales de la entidad · props: `{"tipo": "decision gerencial"}` · tramo [exacta]: «Las principales decisiones gerenciales»
- **ob1 Obligacion** «Decisiones colegiadas — principales decisiones gerenciales» — Recomendación (buena práctica, no deber): las principales decisiones gerenciales serán adoptadas por más de una persona. · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "en orden a las buenas prácticas", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona.»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob1 Obligacion —aplica_a→ Sujeto_alta_gerencia (mención «Alta Gerencia»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:14 | sí | «en orden a las buenas prácticas» | `extraida_tramo_verificado` |  | ob1 Obligacion [exacta], tramo que contiene «en orden a las buenas prácticas» |

## `lingob::4.2.1` — Comité de gestión de riesgos, que realizará un seguimiento de las actividades de la Alta

Grupos: omisiones.

### Texto

> *heredado:* Sección 4. Comités.
> *heredado:* 4.2. Otros comités.
> *heredado:* De acuerdo con las dimensiones, complejidad, importancia económica y perfil de riesgo que presente la entidad financiera y el grupo económico de que se trate, se recomienda el establecimiento de otros comités especializados, con una clara definición y divulgación de sus mandatos, composición (incluidos los miembros considerados independientes) y procedimientos de trabajo. Entre otros comités, se pueden mencionar los siguientes:
> *heredado:* Tanto los directores independientes como aquellos que no reúnan esa condición, pero posean conocimientos y aptitudes relevantes, deberían tener un rol clave en tales comités. A los efectos de maximizar la objetividad, es conveniente que la mayoría de los miembros revistan la condición de independiente, contemplando en su caso las situaciones previstas en el primer párrafo de este punto y la naturaleza específica de la entidad. Los citados comités no son excluyentes de otros que se puedan exigir de manera específica por normas del Banco Central de la República Argentina.
> *propio:* 4.2.1. Comité de gestión de riesgos, que realizará un seguimiento de las actividades de la Alta Gerencia relacionadas con la gestión de los riesgos de crédito, de mercado, de liquidez y/o de activos y pasivos, operacional, de cumplimiento y de reputación, entre otros. Asimismo, asesorará al Directorio sobre los riesgos de la entidad.

### Extracción (código K)

- **e1 Obligacion** «Comité de gestión de riesgos — recomendación de establecerlo» — Recomendación (no deber): según dimensiones, complejidad, importancia económica y perfil de riesgo de la entidad financiera y su grupo económico, establecer un Comité de gestión de riesgos, con clara definición y divulgación de mandato, composición y procedimientos, que haga seguimiento de las actividades de la Alta Gerencia relacionadas con la gestión de los riesgos de crédito, mercado, liquidez … · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "se recomienda", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «se recomienda el establecimiento de otros comités especializados […] Comité de gestión de riesgos, que realizará un seguimiento de las actividades de la Alta Gerencia relacionadas con la gestión de los riesgos»
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

### Extracción (código K)

- **e1 Obligacion** «Comité de incentivos al personal — recomendación» — Recomendación (no deber): se recomienda que la entidad financiera, según sus dimensiones, complejidad, importancia económica y perfil de riesgo y el del grupo económico, establezca, entre otros comités especializados, un Comité de incentivos al personal, encargado de vigilar que el sistema de incentivos económicos al personal sea consistente con la cultura, los objetivos, los negocios a largo plaz… · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "se recomienda", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «se recomienda el establecimiento de otros comités especializados, con una clara definición y divulgación de sus mandatos, composición (incluidos los miembros considerados independientes) y procedimientos de trabajo. Entre otros comités, se pueden mencionar los siguientes: […] Comité de incentivos al personal, encargado…»
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

### Extracción (código K)

- **e1 Obligacion** «Divulgar estructura del Directorio, Alta Gerencia y comités» — Recomendación (no deber): es deseable que las entidades financieras incluyan en sus sitios públicos (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda y en función del tamaño, complejidad, estructura propietaria, importancia económica, perfil de riesgo y cotización en bolsa, la estructura del Directorio (conformación según el estatuto… · props: `{"tipo": "presentacion_informativa"}` · no definidas: `{"modalidad": "Es deseable", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la siguiente información […] Estructura del Directorio (conformación según el estatuto, tamaño, miembros, proceso de selección, cali…»
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

### Extracción (código K)

- **e1 Obligacion** «Divulgar política según naturaleza jurídica — entidades públicas» — Recomendación (no deber): es deseable que las entidades financieras públicas incluyan en sus sitios públicos (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la definición de la política en función de su naturaleza jurídica conforme su carta orgánica y/o estatutos, en función del tamaño, complejidad, estructura propietaria, importa… · props: `{"tipo": "presentacion_informativa"}` · no definidas: `{"modalidad": "Es deseable", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la siguiente información […] En las entidades financieras públicas, la definición de la política en función de su naturaleza jurídic…»
- R: e1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras públicas»)

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:22 | sí | «Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información pe…» | `extraida_tramo_verificado` |  | e1 Obligacion [exacta], tramo de dos segmentos que cubre el comienzo de la oración del heredado (hasta «la siguiente información»), no el calificador final («en función del tamaño… cotiza o no en bolsas»); cobertura parcial 0,58 |

## `pagjub::2.2` — Modelo de nota de presentación de la rendición de cuentas.

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Rendición de cuentas por parte de las entidades financieras.
> *propio:* 2.2. Modelo de nota de presentación de la rendición de cuentas. Fecha: De: (1) A: BANCO CENTRAL DE LA REPÚBLICA ARGENTINA. Remitimos a Uds. para su procesamiento, en los términos de las normas sobre "Pago de beneficios de la seguridad social por cuenta de la Administración Nacional de la Seguridad Social (ANSES)" los archivos contenidos en los soportes de información que se acompañan, en los cuales se detalla el estado de la totalidad de las órdenes de pago que la ANSES nos encomendara pagar, correspondientes al período .....(2)......de la liquidación ….(3)... Emisión de ANSES: …...................(4) ............ casos por $................(5) ................, Órdenes de Pago pagadas: .............(6) …........ casos por $................(7) .................. Órdenes de Pago impagas: .............(8) ............ casos por $................(9) .................. Certificamos que los datos señalados precedentemente son ciertos y resumen la información detallada en los archivos contenidos en los soportes que se acompañan. Identificación de los archivos Responsables: Firma Firma Nombres y apellidos Nombres y apellidos Tipo y N° doc. de identidad (10) Tipo y N° doc. de identidad (10) Tel. Tel. ................. RECIBIDO ------------------------------------------------------------------------------------------------------------------ Referencias: (1)Código de la entidad financiera. (2)Consignar período de pago mensual o aguinaldo, en su caso. (3)Consignar tipo de liquidación ("ANSES", cuando la rendición es de prestaciones de la Administración Nacional de la Seguridad Social y "MTESS" cuando la rendición es de prestaciones por cuenta y orden del Ministerio de Trabajo, Empleo y Seguridad Social). (4) Cantidad de órdenes de pago que se encomendó pagar a la entidad financiera durante el período de pago correspondiente. (5)Importe en pesos del total puesto al pago. (6)Cantidad de órdenes de pago pagadas. (7)Importe en pesos del total pagado. (8)Cantidad de órdenes de pago impagas. (9)Importe en pesos del total impago. (10)Conforme a lo previsto en las normas sobre "Documentos de identificación en vigencia".

### Extracción (código K)

- **e1 Operacion** «Nota de presentación de rendición de cuentas al BCRA» — Presentación al BCRA, mediante nota según modelo, de los archivos con el estado de la totalidad de las órdenes de pago que la ANSES encomendó pagar, por período y liquidación · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Modelo de nota de presentación de la rendición de cuentas.»
- **e2 Obligacion** «Consignar período de pago — nota de rendición» — En la nota de rendición se debe consignar el período de pago mensual o aguinaldo, en su caso · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Consignar período de pago mensual o aguinaldo, en su caso.»
- **e3 Obligacion** «Consignar tipo de liquidación ANSES/MTESS — nota de rendición» — Consignar "ANSES" si la rendición es de prestaciones de ANSES y "MTESS" si es de prestaciones por cuenta y orden del Ministerio de Trabajo, Empleo y Seguridad Social · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Consignar tipo de liquidación ("ANSES", cuando la rendición es de prestaciones de la Administración Nacional de la Seguridad Social y "MTESS" cuando la rendición es de prestaciones por cuenta y orden del Ministerio de Trabajo, Empleo y Seguridad Social).»
- **e4 Obligacion** «Certificación de veracidad de datos — nota de rendición» — La nota incluye la certificación, firmada por los responsables, de que los datos son ciertos y resumen la información de los archivos acompañados · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «Certificamos que los datos señalados precedentemente son ciertos y resumen la información detallada en los archivos contenidos en los soportes que se acompañan.»
- R: e2 Obligacion —regula→ e1 Operacion
- R: e3 Obligacion —regula→ e1 Operacion
- R: e4 Obligacion —regula→ e1 Operacion
- R: Sujeto_entidad_financiera (mención «las entidades financieras») —ejecuta→ e1 Operacion
- Omisión `tabla` [exacta]: «Emisión de ANSES: …...................(4) ............ casos por $................(5) ................,» — Campos del formulario modelo (cantidades e importes de órdenes emitidas, pagadas e impagas, firmas, identificación); estructura de plantilla no extraída como norma

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:16 | no | «Órdenes de Pago pagadas: .............(6) …........ casos por $................(7) ..................» | `ausente` |  | ninguna entidad; om#0 tabla cita la línea anterior («Emisión de ANSES…») y describe el bloque de cantidades e importes |

## `pagjub::2.8.4.3` — Debitar de la cuenta corriente de la entidad participante el importe de las órdenes

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Rendición de cuentas por parte de las entidades financieras.
> *heredado:* 2.8. Liquidación de la rendición de cuentas.
> *heredado:* El procesamiento de la información de la rendición de cuentas dará lugar a diferentes movimientos de fondos los que, según los casos correspondientes, se describen a continuación:
> *heredado:* 2.8.4. Presentación aceptada durante el período de presentación tardía con inconsistencias.
> *heredado:* El BCRA, en el mismo día de la aceptación, procederá a:
> *propio:* 2.8.4.3. Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditando el mismo en una cuenta transitoria del BCRA, hasta la fecha límite.

### Extracción (código K)

- **e1 Obligacion** «Débito órdenes con inconsistencias — presentación tardía» — Ante una presentación aceptada durante el período de presentación tardía con inconsistencias, el BCRA, en el mismo día de la aceptación, debe debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditándolo en una cuenta transitoria del BCRA hasta la fecha límite. · props: `{"tipo": "otra"}` · tramo [exacta]: «El BCRA, en el mismo día de la aceptación, procederá a: […] Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditando el mismo en una cuenta transitoria del BCRA, hasta la fecha límite.»
- **e2 Operacion** «Débito en cuenta corriente de entidad participante» — Débito por el BCRA en la cuenta corriente de la entidad participante del importe de órdenes de pago abonadas e impagas con inconsistencias, con acreditación en cuenta transitoria del BCRA hasta la fecha límite. · props: `{"tipo": "débito en cuenta corriente"}` · tramo [exacta]: «Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias»
- R: e1 Obligacion —regula→ e2 Operacion
- R: e1 Obligacion —aplica_a→ Sujeto_bcra (mención «El BCRA»)
- R: Sujeto_bcra (mención «El BCRA») —ejecuta→ e2 Operacion
- R: e2 Operacion —aplica_a→ Sujeto_rol_alcance_pagjub (mención «la entidad participante»)

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

### Extracción (código K)

- **e1 Operacion** «Financiación UVI a personas humanas» — Otorgamiento de financiaciones en Unidades de Vivienda actualizables por ICC (UVI) - Ley 27.271 a personas humanas · props: `{"tipo": "financiación"}` · tramo [exacta]: «Al momento del otorgamiento de financiaciones a personas humanas»
- **e2 Obligacion** «Atención relación cuota/ingreso — financiación UVI» — Condición a la que están sujetas las financiaciones UVI: al otorgarlas a personas humanas, se debe tener especial atención a la relación cuota/ingreso para que el deudor pueda afrontar posibles incrementos de las cuotas sin afectar su capacidad de pago, considerando que sus ingresos pueden no seguir la evolución de la UVI ni del CVS. · props: `{"tipo": "otra"}` · tramo [exacta]: «estarán sujetas a las siguientes condiciones […] se deberá tener especial atención a la relación cuota/ingreso de manera de que el deudor pueda afrontar posibles incrementos en el importe de las cuotas sin afectar su capacidad de pago»
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

### Extracción (código K)

- **c1 Condicion** «Financiaciones en pesos > $30.000 millones — Gran empresa exportadora» — Condición (concurrente con las demás del punto 7.1) para que un cliente del sector privado no financiero quede comprendido en la categoría "Grandes empresas exportadoras": mantener financiaciones alcanzadas en pesos en el sistema financiero por más de $ 30.000 millones (alternativa: y/o pases o cauciones bursátiles tomadas en pesos en los últimos 90 días). · umbral: ['que supere el monto de $ 30.000 millones'] · tramo [exacta]: «Mantengan un importe total de financiaciones alcanzadas en pesos en el conjunto del sistema financiero que supere el monto de $ 30.000 millones»
- **c2 Condicion** «Pases/cauciones tomadas en pesos últimos 90 días — Gran empresa exportadora» — Supuesto alternativo (y/o) del punto 7.1.2 para encuadrar en "Grandes empresas exportadoras": haber mantenido pases y/o cauciones bursátiles tomadas en pesos, cualquiera sea su importe, durante los últimos 90 días corridos. · umbral: ['durante los últimos 90 días corridos'] · tramo [exacta]: «y/o pases y/o cauciones bursátiles tomadas –en pesos– cualquiera sea su importe durante los últimos 90 días corridos»
- **d1 Definicion** «Financiaciones alcanzadas — Grandes empresas exportadoras» — Aquellas que hayan implicado desembolsos de fondos, así como el importe no utilizado del límite de crédito asignado para adelantos en cuenta corriente; se computa su saldo de capital a fin del mes anterior al de su determinación. · props: `{"termino": "financiaciones alcanzadas"}` · tramo [exacta]: «Las financiaciones alcanzadas serán aquellas que hayan implicado desembolsos de fondos, así como el importe no utilizado del límite de crédito asignado para adelantos en cuenta corriente.»
- **op1 Operacion** «Cómputo de financiaciones alcanzadas» — Cómputo del saldo de capital de las financiaciones alcanzadas a fin del mes anterior al de su determinación. · props: `{"tipo": "calculo"}` · tramo [exacta]: «Se computará su saldo de capital a fin del mes anterior al que corresponda su determinación.»
- **c3 Condicion** «DDJJ de no encuadre y CENDEU > $30.000 millones» — Cliente que declara bajo DDJJ no ser Gran empresa exportadora pero la Central de deudores muestra que supera $ 30.000 millones. · umbral: ['surja que supera el importe de $ 30.000 millones'] · tramo [exacta]: «Cuando un cliente manifieste por declaración jurada que no se encuadra en la categoría de "Gran empresa exportadora" y, de la información disponible en la "Central de deudores del sistema financiero", surja que supera el importe de $ 30.000 millones»
- **o1 Obligacion** «Certificación de auditor/contador — cliente con DDJJ contradicha» — El cliente debe presentar certificación de Auditor Externo o Contador Público independiente (firma certificada por el Consejo Profesional) detallando financiaciones en pesos y moneda extranjera en el conjunto de entidades financieras, desagregadas por entidad, y los pases y cauciones bursátiles tomados en pesos en los últimos 90 días corridos. · props: `{"tipo": "presentacion_informativa"}` · umbral: ['durante los últimos 90 días corridos'] · tramo [exacta]: «deberá presentar una certificación extendida por Auditor Externo o Contador Público independiente»
- **x1 Excepcion** «Cliente MiPyME — exento de certificación» — La obligación de presentar la certificación no aplica cuando el cliente reúna la condición de MiPyME según las normas respectivas. · tramo [exacta]: «Lo previsto en este párrafo no será de aplicación cuando el cliente reúna la condición de MiPyME»
- **r1 Restriccion** «Vigencia 90 días — certificación» — La certificación tiene vigencia de 90 días corridos desde su fecha de referencia, sin perjuicio de presentar una nueva si corresponde. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['mantendrá vigencia durante 90 días corridos'] · tramo [exacta]: «Esa certificación mantendrá vigencia durante 90 días corridos desde la fecha a la cual se refiera»
- **op2 Operacion** «Presentación de certificación de financiaciones» — Presentación de certificación de financiaciones y pases/cauciones por parte del cliente. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «presentar una certificación extendida por Auditor Externo o Contador Público independiente»
- R: c3 Condicion —condicion_de→ o1 Obligacion
- R: x1 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: o1 Obligacion —aplica_a→ Sujeto_cliente (mención «un cliente»)
- R: x1 Excepcion —aplica_a→ Sujeto_cliente (mención «el cliente»)
- R: o1 Obligacion —regula→ op2 Operacion
- R: r1 Restriccion —limita→ op2 Operacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «financiaciones de más de $ 30.000 millones» | `sin_relacion` | norma_en_heredado | c1 Condicion con el umbral, sin relación; norma en el texto heredado |
| 2 | «pases o cauciones en 90 días» | `sin_relacion` | norma_en_heredado | c2 Condicion con el umbral, sin relación; norma en el texto heredado |
| 3 | «declaración jurada contra la Central de deudores» | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ o1 Obligacion |
| 4 | «MiPyME» | `condicion_con_relacion` |  | x1 Excepcion —exceptua_obligacion→ o1 Obligacion |

## `polcre::7.1::cierre` — [bloque cierre] Clientes comprendidos.

Grupos: grupo_c.

### Texto

> *heredado:* Sección 7. Financiaciones a "Grandes empresas exportadoras".
> *heredado:* 7.1. Clientes comprendidos.
> *propio:* Cuando el cliente reúna la condición del punto 7.1.1. pero el importe total de sus financiaciones en pesos en el sistema financiero no supere el importe de $ 30.000 millones y no haya mantenido pases y/o cauciones bursátiles tomadas –en pesos– durante los últimos 90 días corridos, la entidad financiera podrá otorgarle nuevas financiaciones en la medida que con tales desembolsos no se supere ese importe. Cuando se trate de conjuntos económicos se los considerará como un solo cliente, a cuyo efecto será de aplicación el punto 1.2.2. de las normas sobre "Grandes exposiciones al riesgo de crédito". A los fines de la imputación de las financiaciones, será de aplicación lo previsto en las normas sobre "Grandes exposiciones al riesgo de crédito".

### Extracción (código K)

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

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «reúne 7.1.1» | `condicion_con_relacion` |  | c3 Condicion —condicion_de→ p1 Potestad |
| 2 | «no supera $ 30.000 millones» | `condicion_con_relacion` |  | c1 Condicion con el umbral —condicion_de→ p1 Potestad |
| 3 | «sin pases» | `condicion_con_relacion` |  | c2 Condicion —condicion_de→ p1 Potestad |
| 4 | «desembolsos que no superen el importe» | `dentro_de_norma` |  | extraído como norma de otro tipo: r1 Restriccion con el umbral; también dentro de p1; sin Condicion |
| 5 | «conjuntos económicos» | `dentro_de_norma` |  | extraído como Definicion d1; sin Condicion |

## `pro::2.3.5.1` — Todo importe cobrado o adeudado de cualquier forma al usuario de servicios fi-

Grupos: grupo_c.

### Texto

> *heredado:* Sección 2. Derechos básicos de los usuarios de servicios financieros.
> *heredado:* 2.3. Recaudos mínimos de la relación de consumo.
> *heredado:* 2.3.5. Reintegro de importes.
> *propio:* 2.3.5.1. Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: i) tasas de interés, comisiones y/o cargos sin el cumplimiento de lo previsto en los puntos 2.3.2. a 2.3.4.; ii) cargos en exceso de los costos de los servicios que terceros les cobraron a los sujetos obligados en relación con servicios prestados a los usuarios y/o de los precios que el tercero prestador perciba de particulares en general; iii) comisiones en exceso de las máximas fijadas por el BCRA que sean de aplicación; iv) en incumplimiento al nivel de la tasa de interés máxima aplicable a financiaciones vinculadas a tarjetas de crédito previstas en el texto ordenado sobre Tasas de Interés en las Operaciones de Crédito; v) en exceso de lo oportunamente pactado entre el usuario y el sujeto obligado; vi) otros generados en forma impropia por su naturaleza, tales como intereses compensatorios por saldos deudores generados en cuentas de depósito distintas de la cuenta corriente bancaria; vii) así como los importes adeudados al usuario por haber liquidado en forma incorrecta promociones, descuentos u otro tipo de beneficios –es decir, que no se ajustan a los términos, condiciones y/o modalidades que hubieran sido ofrecidos, publicitados o convenidos–; deberá serle reintegrado dentro de: - los diez (10) días hábiles siguientes al momento de la presentación del reclamo ante el sujeto obligado, de conformidad con las previsiones del punto 3.1.6.; o - los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por el sujeto obligado o por la fiscalización que realice la SEFYC. Ello, sin perjuicio de las sanciones que pudieran corresponder. En tales situaciones, corresponderá reconocer el importe de los gastos que resulten razonables realizados para la obtención del reintegro y, en todos los casos, los intereses compensatorios pertinentes, computados desde la fecha del cobro indebido hasta la de su efectiva devolución. A ese efecto, el sujeto obligado deberá aplicar 1,5 veces la tasa promedio correspondiente al período comprendido entre el momento en que la citada diferencia hubiera sido exigible –fecha en la que se cobraron los importes objeto del reclamo– y el de su efectiva cancelación, computado a partir de la encuesta diaria de tasas de interés de depósitos a plazo fijo de 30 a 59 días –de pesos o dólares estadounidenses, según la moneda de la operación– informada por el BCRA sobre la base de la información provista por la totalidad de bancos públicos y privados. Cuando la tasa correspondiente a tal encuesta no estuviera disponible, se deberá tomar la última informada. Cuando el usuario posea en la entidad financiera obligada una cuenta a la vista que se halle abierta a su nombre, ésta deberá acreditar ese importe en dicha cuenta en forma automática sin necesidad de requerimiento expreso. Si ello no fuera posible o no se tratare de una entidad financiera, el importe del reintegro deberá ser acreditado en una tarjeta de crédito de su titularidad o detraído del saldo vigente de la financiación que lo generó. Deberá notificarse la acreditación del reintegro o, en su caso, su puesta a disposición mediante aviso efectuado a través de medios electrónicos –cajeros automáticos, banca por Internet (home banking), etc.– y/o servicios telefónicos –tales como mensajes de texto y/o voz– y: a) documento escrito dirigido a su domicilio –en forma separada de cualquier otra información que se le remita (resúmenes de cuenta, boletines informativos, etc.), aun cuando forme parte de la misma remesa–; o b) a su correo electrónico –en aquellos casos en que hubiere expresamente aceptado esa forma de notificación–. Estas disposiciones serán de aplicación a los efectos de dar cumplimiento a acuerdos extrajudiciales homologados, acuerdos homologados por acciones colectivas (artículo 54 de la Ley 24.240) o sentencias judiciales, en la medida en que no se opongan a lo previsto en esos acuerdos o a lo dispuesto por los poderes públicos de las distintas jurisdicciones. Adicionalmente, el sujeto obligado deberá verificar si este tipo de situaciones que generan la obligación de reintegros ha ocurrido respecto de los usuarios que se encuentren en la misma situación y, de corresponder, proceder a su reintegro según el procedimiento previsto en este punto, notificando de tal circunstancia y resultados a su Responsable de Atención al Usuario de Servicios Financieros.

### Extracción (código K)

- **op1 Operacion** «Reintegro de importes cobrados indebidamente al usuario» — Reintegro al usuario de servicios financieros de importes cobrados o adeudados indebidamente · props: `{"tipo": "reintegro"}` · tramo [exacta]: «deberá serle reintegrado dentro de:»
- **o1 Obligacion** «Reintegro 10 días hábiles desde reclamo» — Reintegrar al usuario todo importe cobrado o adeudado por los conceptos i) a vii) dentro de los 10 días hábiles siguientes a la presentación del reclamo ante el sujeto obligado (conforme punto 3.1.6.); alternativa al plazo de 5 días desde constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo'] · tramo [exacta]: «deberá serle reintegrado dentro de: - los diez (10) días hábiles siguientes al momento de la presentación del reclamo ante el sujeto obligado»
- **o2 Obligacion** «Reintegro 5 días hábiles desde constatación» — Reintegrar al usuario los importes indebidos dentro de los 5 días hábiles siguientes a su constatación por el sujeto obligado o por la fiscalización de la SEFyC · props: `{"tipo": "otra"}` · umbral: ['los cinco (5) días hábiles siguientes al momento de constatarse'] · tramo [exacta]: «los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por el sujeto obligado o por la fiscalización que realice la SEFYC»
- **c1 Condicion** «Cobros sin cumplir puntos 2.3.2 a 2.3.4» — Importe cobrado por tasas, comisiones o cargos sin cumplir los puntos 2.3.2 a 2.3.4 · tramo [exacta]: «tasas de interés, comisiones y/o cargos sin el cumplimiento de lo previsto en los puntos 2.3.2. a 2.3.4.»
- **c2 Condicion** «Cargos en exceso de costos de terceros» — Cargos que exceden los costos cobrados por terceros o los precios que el tercero percibe de particulares · props: `{"umbrales": [{"tramo": "en exceso de los costos de los servicios que terceros les cobraron", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['en exceso de los costos de los servicios que terceros les cobraron'] · tramo [exacta]: «cargos en exceso de los costos de los servicios que terceros les cobraron a los sujetos obligados en relación con servicios prestados a los usuarios y/o de los precios que el tercero prestador perciba de particulares en general»
- **c3 Condicion** «Comisiones en exceso de máximas BCRA» — Comisiones que exceden las máximas fijadas por el BCRA · props: `{"umbrales": [{"tramo": "en exceso de las máximas fijadas por el BCRA", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['en exceso de las máximas fijadas por el BCRA'] · tramo [exacta]: «comisiones en exceso de las máximas fijadas por el BCRA que sean de aplicación»
- **c4 Condicion** «Incumplimiento de tasa máxima tarjetas de crédito» — Importes cobrados incumpliendo la tasa máxima de financiaciones con tarjeta de crédito (TO Tasas de Interés en las Operaciones de Crédito) · props: `{"umbrales": [{"tramo": "tasa de interés máxima aplicable a finan-\nciaciones vinculadas a tarjetas de crédito", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['tasa de interés máxima aplicable a financiaciones vinculadas a tarjetas de crédi…'] · tramo [exacta]: «en incumplimiento al nivel de la tasa de interés máxima aplicable a financiaciones vinculadas a tarjetas de crédito»
- **c5 Condicion** «Exceso sobre lo pactado» — Importes en exceso de lo pactado entre usuario y sujeto obligado · props: `{"umbrales": [{"tramo": "en exceso de lo oportunamente pactado", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['en exceso de lo oportunamente pactado'] · tramo [exacta]: «en exceso de lo oportunamente pactado entre el usuario y el sujeto obligado»
- **c6 Condicion** «Cobros impropios por su naturaleza» — Otros importes impropios por su naturaleza, p.ej. intereses compensatorios por saldos deudores en cuentas de depósito distintas de cuenta corriente · tramo [exacta]: «otros generados en forma impropia por su naturaleza»
- **c7 Condicion** «Promociones o beneficios mal liquidados» — Importes adeudados por liquidar incorrectamente promociones, descuentos o beneficios no ajustados a lo ofrecido, publicitado o convenido · tramo [exacta]: «importes adeudados al usuario por haber liquidado en forma incorrecta promociones, descuentos u otro tipo de beneficios»
- **o3 Obligacion** «Gastos razonables e intereses compensatorios — reintegro» — Reconocer gastos razonables para obtener el reintegro y siempre intereses compensatorios desde el cobro indebido hasta la devolución, aplicando 1,5 veces la tasa promedio de la encuesta diaria de plazo fijo de 30 a 59 días del BCRA (o la última informada si no está disponible) · props: `{"tipo": "calculo"}` · umbral: ['1,5 veces la tasa promedio'] · tramo [exacta]: «corresponderá reconocer el importe de los gastos que resulten razonables realizados para la obtención del reintegro y, en todos los casos, los intereses compensatorios pertinentes»
- **o4 Obligacion** «Acreditación automática en cuenta a la vista» — La entidad financiera debe acreditar automáticamente el reintegro en la cuenta a la vista del usuario · props: `{"tipo": "otra"}` · tramo [exacta]: «ésta deberá acreditar ese importe en dicha cuenta en forma automática sin necesidad de requerimiento expreso»
- **c8 Condicion** «Usuario con cuenta a la vista en la entidad» — El usuario posee cuenta a la vista a su nombre en la entidad financiera obligada · tramo [exacta]: «Cuando el usuario posea en la entidad financiera obligada una cuenta a la vista que se halle abierta a su nombre»
- **o5 Obligacion** «Acreditación en tarjeta o detracción de financiación» — Acreditar el reintegro en tarjeta de crédito del usuario o detraerlo del saldo de la financiación · props: `{"tipo": "otra"}` · tramo [exacta]: «el importe del reintegro deberá ser acreditado en una tarjeta de crédito de su titularidad o detraído del saldo vigente de la financiación que lo generó»
- **c9 Condicion** «Imposible acreditar en cuenta o no entidad financiera» — No es posible acreditar en cuenta a la vista o el obligado no es entidad financiera · tramo [exacta]: «Si ello no fuera posible o no se tratare de una entidad financiera»
- **o6 Obligacion** «Notificación del reintegro al usuario» — Notificar acreditación o puesta a disposición del reintegro por medios electrónicos y/o telefónicos y además por documento escrito separado a su domicilio o por correo electrónico si lo aceptó expresamente · props: `{"tipo": "comunicacion_a_cliente"}` · tramo [exacta]: «Deberá notificarse la acreditación del reintegro o, en su caso, su puesta a disposición mediante aviso efectuado a través de medios electrónicos»
- **o7 Obligacion** «Verificar usuarios en igual situación y reintegrar» — Verificar si otros usuarios en igual situación sufrieron cobros indebidos, reintegrarles según este punto y notificar circunstancias y resultados al Responsable de Atención al Usuario · props: `{"tipo": "otra"}` · tramo [exacta]: «el sujeto obligado deberá verificar si este tipo de situaciones que generan la obligación de reintegros ha ocurrido respecto de los usuarios que se encuentren en la misma situación»
- **c10 Condicion** «Cumplimiento de acuerdos homologados o sentencias» — Las disposiciones aplican para cumplir acuerdos extrajudiciales homologados, acuerdos por acciones colectivas (art. 54 Ley 24.240) o sentencias, en tanto no se opongan a ellos · tramo [exacta]: «en la medida en que no se opongan a lo previsto en esos acuerdos o a lo dispuesto por los poderes públicos»
- **cm1 Comunicacion** «Ley 24.240» —  · props: `{"codigo": "Ley 24.240", "tipo": "externa"}` · tramo [exacta]: «artículo 54 de la Ley 24.240»
- R: to TextoOrdenado —referencia→ cm1 Comunicacion
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o4 Obligacion —regula→ op1 Operacion
- R: o5 Obligacion —regula→ op1 Operacion
- R: op1 Operacion —requiere→ o6 Obligacion
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: c2 Condicion —condicion_de→ op1 Operacion
- R: c3 Condicion —condicion_de→ op1 Operacion
- R: c4 Condicion —condicion_de→ op1 Operacion
- R: c5 Condicion —condicion_de→ op1 Operacion
- R: c6 Condicion —condicion_de→ op1 Operacion
- R: c7 Condicion —condicion_de→ op1 Operacion
- R: c8 Condicion —condicion_de→ o4 Obligacion
- R: c9 Condicion —condicion_de→ o5 Obligacion
- R: c10 Condicion —condicion_de→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- R: o3 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- R: o4 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera obligada»)
- R: o7 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- Omisión `meta_normativo` [exacta]: «Ello, sin perjuicio de las sanciones que pudieran corresponder.» — Salvedad interpretativa sobre sanciones; no nombra quién las aplica

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «conceptos i) a vii)» (i)) | `condicion_con_relacion` |  | c1 Condicion (el concepto i)) —condicion_de→ op1 Operacion (el reintegro) |
| 2 | «conceptos i) a vii)» (ii)) | `condicion_con_relacion` |  | c2 Condicion (el concepto ii)) —condicion_de→ op1 Operacion (el reintegro) |
| 3 | «conceptos i) a vii)» (iii)) | `condicion_con_relacion` |  | c3 Condicion (el concepto iii)) —condicion_de→ op1 Operacion (el reintegro) |
| 4 | «conceptos i) a vii)» (iv)) | `condicion_con_relacion` |  | c4 Condicion (el concepto iv)) —condicion_de→ op1 Operacion (el reintegro) |
| 5 | «conceptos i) a vii)» (v)) | `condicion_con_relacion` |  | c5 Condicion (el concepto v)) —condicion_de→ op1 Operacion (el reintegro) |
| 6 | «conceptos i) a vii)» (vi)) | `condicion_con_relacion` |  | c6 Condicion (el concepto vi)) —condicion_de→ op1 Operacion (el reintegro) |
| 7 | «conceptos i) a vii)» (vii)) | `condicion_con_relacion` |  | c7 Condicion (el concepto vii)) —condicion_de→ op1 Operacion (el reintegro) |
| 8 | «plazo por reclamo» | `dentro_de_norma` |  | dentro de la Obligacion o1 (umbral «los diez (10) días hábiles…»); sin Condicion |
| 9 | «por constatación» | `dentro_de_norma` |  | extraído como norma de otro tipo: o2 Obligacion con el umbral «los cinco (5) días hábiles…»; sin Condicion |
| 10 | «tasa no disponible» | `dentro_de_norma` |  | dentro de la Obligacion o3 (descripción «o la última informada si no está disponible»); sin Condicion |
| 11 | «cuenta a la vista» | `condicion_con_relacion` |  | c8 Condicion —condicion_de→ o4 Obligacion |
| 12 | «si no fuera posible» | `condicion_con_relacion` |  | c9 Condicion —condicion_de→ o5 Obligacion |

## `pro::2.7::intro` — [bloque intro] Revocación de la aceptación y rescisión de relaciones contractuales.

Grupos: omisiones.

### Texto

> *heredado:* Sección 2. Derechos básicos de los usuarios de servicios financieros.
> *heredado:* 2.7. Revocación de la aceptación y rescisión de relaciones contractuales.
> *propio:* Los sujetos obligados deberán contar con sendos hipervínculos que permitan al usuario:

### Extracción (código K)

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

### Extracción (código K)

- **op1 Operacion** «Registro de consultas y reclamos en RCCR» — Asiento en base de datos única y centralizada de las presentaciones (consultas o reclamos) de usuarios de servicios financieros · props: `{"tipo": "registro"}` · tramo [exacta]: «Registro Centralizado de Consultas y Reclamos (RCCR).»
- **o1 Obligacion** «Asiento centralizado de todas las presentaciones — RCCR» — Asentar en una base de datos única y centralizada todas las consultas o reclamos recibidos de usuarios, independientemente del medio de canalización y de la casa receptora. · props: `{"tipo": "otra"}` · tramo [exacta]: «Se deberán asentar en una base de datos única y centralizada todas las presentaciones (consultas o reclamos) recibidas de los usuarios de servicios financieros»
- **o2 Obligacion** «Asiento de presentaciones sin respuesta inmediata — RCCR» — Deben asentarse en el RCCR las consultas y/o reclamos que requieren análisis de documentación del sujeto obligado y/o pedido de información a otros sujetos u organismos, de modo que no se puede responder en forma inmediata. · props: `{"tipo": "otra"}` · tramo [exacta]: «Las consultas y/o reclamos que deben ser asentados en el RCCR son aquellos que, para su respuesta al cliente, requieren del análisis de la documentación»
- **o3 Obligacion** «Asiento de quejas por incumplimiento aun con respuesta inmediata» — Deben asentarse los reclamos por presunto incumplimiento, prestación defectuosa o falta de prestación de un producto o servicio del sujeto obligado, aun cuando pueda dárseles respuesta inmediata. · props: `{"tipo": "otra"}` · tramo [exacta]: «También deben ser asentados en el mencionado registro aquellos reclamos que representan una queja por presunto incumplimiento, prestación defectuosa o falta de prestación»
- **o4 Obligacion** «Datos mínimos a consignar — RCCR» — Consignar como mínimo: número de consulta o reclamo; fecha, canal y motivo; tipo y número de documento del presentante; casa receptora y afectada/s; otra/s entidad/es involucrada/s; estado del trámite. · props: `{"tipo": "otra"}` · tramo [exacta]: «Deberán consignarse como mínimo los siguientes datos»
- **o5 Obligacion** «Estado del trámite actualizado — RCCR» — Mantener actualizado el estado del trámite (pendiente, respuesta provisoria o definitiva, junto con la respuesta brindada, etc.). · props: `{"tipo": "otra"}` · tramo [exacta]: «el estado del trámite, el cual deberá mantenerse actualizado»
- **o6 Obligacion** «Numeración correlativa de presentaciones — RCCR» — Los números asignados a las presentaciones deben ser correlativos. · props: `{"tipo": "asignacion"}` · tramo [exacta]: «Los números asignados a las presentaciones deberán ser correlativos»
- **r1 Restriccion** «Modificación de base solo para altas y actualizaciones» — La base sólo puede modificarse para incorporar nuevas consultas o reclamos o agregar información sobre el estado actualizado de los trámites. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «la base de datos sólo podrá ser modificada para la incorporación de nuevas consultas o reclamos, o para el agregado de nueva información sobre el estado actualizado de los trámites»
- **op2 Operacion** «Modificación de la base de datos RCCR» — Modificación de la base de datos del RCCR · props: `{"tipo": "modificacion de registro"}` · tramo [exacta]: «la base de datos sólo podrá ser modificada»
- **o7 Obligacion** «Número provisto en el acto — canal telefónico/Internet» — Proveer en el acto al presentante el número de consulta o reclamo, respetando la correlatividad. · props: `{"tipo": "comunicacion_a_cliente"}` · tramo [exacta]: «el número de consulta o reclamo deberá ser provisto en el acto al presentante, respetando la correlatividad citada»
- **c1 Condicion** «Presentación por teléfono o página de Internet» — Consulta o reclamo iniciado por línea/central telefónica o página de Internet habilitadas. · tramo [exacta]: «Cuando la consulta o el reclamo sea iniciada/o llamando a una línea o central telefónica o ingresando datos en una página de Internet, habilitadas para ese fin»
- **o8 Obligacion** «Procedimiento de notificación del número en 3 días» — Establecer un procedimiento que prevea notificar al presentante el número o código asignado dentro de los 3 días hábiles de iniciada la presentación. · props: `{"tipo": "comunicacion_a_cliente"}` · umbral: ['dentro de los tres (3) días hábiles de iniciada la presentación'] · tramo [exacta]: «se deberá establecer un procedimiento que prevea la notificación del número o código que le sea asignado dentro de los tres (3) días hábiles de iniciada la presentación»
- **c2 Condicion** «Presentante sin número automático» — El presentante no recibe automáticamente el número de su consulta o reclamo. · tramo [exacta]: «Para los casos en que el presentante no reciba automáticamente el número de su consulta o reclamo»
- **o9 Obligacion** «Conservación 10 años — base de datos RCCR» — Conservar la información de la base de datos por 10 años. · props: `{"tipo": "otra"}` · umbral: ['por el término de diez (10) años'] · tramo [exacta]: «La información incorporada a esta base de datos deberá conservarse por el término de diez (10) años.»
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

### Extracción (código K)

- **e1 Obligacion** «Reportes del Directivo/Comité de Protección a disposición BCRA» — En la sede en la que desempeñe sus funciones el responsable de atención al usuario de servicios financieros (titular o suplente a cargo) deberán estar a disposición del BCRA, junto con los demás elementos de la lista, los reportes del Directivo Responsable de Protección de los Usuarios de Servicios Financieros o del Comité de Protección de los Usuarios de Servicios Financieros, según corresponda. · props: `{"tipo": "reporte_al_supervisor"}` · tramo [exacta]: «En la sede en la cual desempeñe sus funciones el responsable de atención al usuario de servicios financieros (titular o suplente a cargo) deberán encontrarse a disposición del BCRA: […] Los reportes del Directivo Responsable de Protección de los Usuarios de Servicios Financieros o del Comité de Protección de los Usuari…»
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

### Extracción (código K)

- **c1 Comunicacion** «Normas Supervisión consolidada» —  · props: `{"codigo": "Supervisión consolidada"}` · tramo [exacta]: «normas sobre "Supervisión consolidada"»
- **op1 Operacion** «Envío información código de consolidación 3» — Envío de informaciones con nivel de consolidación trimestral (código 3) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «envío de informaciones con código de consolidación 3»
- **r1 Restriccion** «Suspensión envío código 3 desde abril/24» — A partir del período de información abril/24 se suspende el envío de informaciones con código de consolidación 3, siendo marzo/24 el último período trimestral a informar con ese nivel · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «Se suspende el envío de informaciones con código de consolidación 3»
- **x1 Excepcion** «Ratio de apalancamiento — excepción suspensión código 3» — La suspensión del envío con código 3 no alcanza al Ratio de apalancamiento · tramo [no]: «con la ex-cepción prevista para Ratio de apalancamiento»
- **o1 Obligacion** «Incluir entes 6.2 en consolidación mensual 2 ó 9» — En la información sobre base consolidada mensual (códigos 2 ó 9) se incluirán, de corresponder, las operaciones de los entes de los incisos i), ii) y iii) del primer párrafo del punto 6.2. de Supervisión consolidada · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «se incluirán -de corresponderlas operaciones de los entes a que refieren los incisos»
- **o2 Obligacion** «Informar códigos 1 y 9 — ex códigos 1 y 3» — Las entidades financieras que hasta el 31/03/24 informaban únicamente códigos 1 y 3, de mantenerse esa situación, pasarán a informar códigos 1 y 9 sólo si consolidan con alguno de los entes de los incisos i), ii) y iii) del punto 6.2. · props: `{"tipo": "presentacion_informativa"}` · tramo [no]: «pasarán a in-formar: […] a) códigos 1 y 9 sólo si consolidan con alguno de los entes»
- **k1 Condicion** «Consolida con entes incisos i-iii punto 6.2» — La entidad consolida con alguno de los entes de los incisos i), ii) y iii) del punto 6.2. · tramo [exacta]: «sólo si consolidan con alguno de los entes a que refieren los incisos»
- **k0 Condicion** «Informaba solo códigos 1 y 3 al 31/03/24» — Entidades que hasta el 31/03/24 informaban únicamente códigos 1 y 3 y mantienen esa situación · tramo [exacta]: «que hasta el 31/03/24 informaban únicamente códigos de consolidación 1 y 3, de mantenerse esta situación de consolidación»
- **o3 Obligacion** «Informar código 0 — no consolida con entes 6.2» — Las entidades financieras que informaban únicamente códigos 1 y 3, si no consolidan con los entes del punto 6.2., pasarán a informar código 0 · props: `{"tipo": "presentacion_informativa"}` · tramo [no]: «pasarán a in-formar: […] b) en caso contrario, código 0.»
- **o4 Obligacion** «Ratio de apalancamiento: frecuencia trimestral y vencimiento» — El Ratio de apalancamiento mantiene su frecuencia trimestral (datos del mes de cierre de trimestre) y su vencimiento según punto 1.1. del Régimen Informativo para Supervisión · props: `{"tipo": "presentacion_informativa", "frecuencia": "trimestral"}` · tramo [no]: «mantendrá su frecuencia trimestral (datos del mes de cierre de trimestre) y su vencimiento según punto 1.1. del Régimen Informa-tivo para Supervisión»
- **o5 Obligacion** «Ratio apalancamiento: código 3 con perímetro mensual» — Para Ratio de apalancamiento se continúa informando código 3, incluyendo las operaciones del perímetro de consolidación mensual, considerando de corresponder los sujetos del punto 6.2. · props: `{"tipo": "presentacion_informativa"}` · tramo [no]: «Se continuará informando código de consolidación 3; no obstante, las opera-ciones a incluir serán las que correspondan al perímetro de consolidación men-sual»
- **o6 Obligacion** «Riesgo mercado y tasa: código 2 incluye entes 6.2» — Para datos complementarios del cálculo de exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5.) y Riesgo de tasa de interés en la cartera de inversión (Sección 11.), la consolidación mensual (código 2) considerará, de corresponder, las operaciones de los entes de los incisos i), ii) y iii) del punto 6.2. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «De corresponder, la consolidación mensual (código 2) considerará las operaciones de los entes a que refieren los incisos»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: r1 Restriccion —prohibe→ op1 Operacion
- R: x1 Excepcion —exceptua→ r1 Restriccion
- R: k1 Condicion —condicion_de→ o2 Obligacion
- R: k0 Condicion —condicion_de→ o2 Obligacion
- R: k0 Condicion —condicion_de→ o3 Obligacion
- R: o2 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- R: o3 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «Las entidades financieras»)
- Omisión `meta_normativo` [exacta]: «A partir del período de información abril/24:» — Fecha de vigencia de las disposiciones transitorias

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:20 | no | «A partir del período de información abril/24» | `omision_otra_vez` | meta_normativo | om#0 meta_normativo [exacta] «A partir del período de información abril/24:» |

## `ric::3.1.7` — Exigencia de capital por riesgo de crédito de contraparte en operaciones con en-

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Exigencia por riesgo de crédito
> *heredado:* 3.1. Normas de procedimiento.
> *propio:* 3.1.7. Exigencia de capital por riesgo de crédito de contraparte en operaciones con entidades de contraparte central Las exposiciones de las entidades financieras con entidades de contraparte central con el alcance establecido en el punto 4.3. de las normas sobre "Capitales mínimos de las entidades financieras" –determinadas conforme a dichas normas-, se consignarán en la partida 12500000 por cada ponderador que corresponda aplicar, siguiendo el modelo de información inserto en el punto 3.1.4..

### Extracción (código K)

- **e1 Obligacion** «Consignar exposiciones con CCP en partida 12500000» — Las exposiciones de las entidades financieras con entidades de contraparte central, con el alcance del punto 4.3. de las normas sobre Capitales mínimos y determinadas conforme a dichas normas, se consignarán en la partida 12500000 por cada ponderador que corresponda aplicar, siguiendo el modelo del punto 3.1.4. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «se consignarán en la partida 12500000 por cada ponderador que corresponda aplicar, siguiendo el modelo de información inserto en el punto 3.1.4.»
- **e2 Operacion** «Exposiciones con entidades de contraparte central» — Exposiciones de las entidades financieras con entidades de contraparte central, con el alcance del punto 4.3. de las normas sobre Capitales mínimos, determinadas conforme a dichas normas · props: `{"tipo": "exposicion por riesgo de crédito de contraparte"}` · tramo [exacta]: «Las exposiciones de las entidades financieras con entidades de contraparte central»
- **c1 Comunicacion** «Normas Capitales mínimos» —  · props: `{"codigo": "Capitales mínimos de las entidades financieras"}` · tramo [exacta]: «normas sobre "Capitales mínimos de las entidades financieras"»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: e1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras»)
- R: e1 Obligacion —regula→ e2 Operacion

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

### Extracción (código K)

- **e1 Obligacion** «Código 312200/xx — exigencia riesgo general acciones» — En el código 312200/xx se consignará el valor de la exigencia por riesgo general de acciones para el último día del período (n), determinada conforme al punto 6.3. de las normas sobre Capitales mínimos de las entidades financieras. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se consignará el valor de la exigencia por riesgo general de acciones para el último día del período (n) determinada conforme a las disposiciones del punto 6.3. de las normas sobre "Capitales mínimos de las entidades financieras".»
- **e2 Obligacion** «Discriminación por mercado — riesgo general de acciones» — El riesgo general de acciones informado en el código 312200/xx se discriminará por mercado, identificando el país según la codificación del Country Codes del SWIFT. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Este riesgo se discriminará por mercado»
- **e3 Definicion** «Mercado — país de negociación de acciones» — El país en que se negocien posiciones -compradas o vendidasen acciones. · props: `{"termino": "mercado"}` · tramo [exacta]: «entendido a estos efectos como el país en que se negocien posiciones -compradas o vendidasen acciones»
- **e4 Obligacion** «Identificación del país por Country Codes SWIFT» — A los fines de la discriminación por mercado del código 312200/xx, el país se identificará según la codificación del Country Codes del SWIFT. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «el país se identificará de acuerdo con la codificación del Country Codes del SWIFT»

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

### Extracción (código K)

- **e1 Operacion** «Información sobre futuros y contratos a término (FRA)» — Información sobre instrumentos derivados: futuros y contratos a término, incluidos los FRA, en el marco de la exigencia por riesgo de mercado · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Futuros y Contratos a Término, incluidos los FRA»
- **e2 Obligacion** «Columnas a informar — futuros y contratos a término» — Informar por cada futuro o contrato a término: descripción del activo subyacente, fecha del plazo residual del subyacente (cuando corresponda), vencimiento del derivado, contraparte/ámbito de negociación, valor nocional, tasa de cupón del subyacente (cuando corresponda), precio pactado, precio de mercado del subyacente y compra/venta a término · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Fila 1: col1 = Descripción del activo subyacente(1) | col2 = Fecha correspondiente al plazo residual del subyacente (cuando corresponda)(2) | col3 = Vencimiento del derivado | col4 = Contraparte/Ámb ito de negociación | col5 = Valor nocional(3) | col6 = Tasa de cupón del activo subyacente (cuando corresponda)(4) | col7…»
- **e3 Obligacion** «Describir activo subyacente comprado o vendido» — Describir el activo comprado o vendido a futuro (ej.: tasa Badlar Privada, dólar estadounidense, bono AJ17D) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Describir el activo comprado o vendido a futuro.»
- **e4 Obligacion** «Valor nocional con moneda o unidad» — Especificar el valor nocional incluyendo la moneda o unidad de medida (ej.: USD 25.000.000, $ 100.000) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Especificar el valor nocional incluyendo la moneda o unidad de medida.»
- **e5 Obligacion** «Consignar C o V según compra/venta» — Consignar "C" si el contrato es compra a término o "V" si es venta a término · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Consignar "C" si el contrato en cuestión es una compra a término, o "V" si es una venta a término.»
- **e6 Definicion** «Plazo residual del subyacente» — Ej.: en un futuro sobre un título público, el plazo residual del título público subyacente · props: `{"termino": "Fecha correspondiente al plazo residual del subyacente"}` · tramo [exacta]: «en un futuro sobre un título público es el plazo residual del título público subyacente»
- **e7 Definicion** «Tasa de cupón del activo subyacente» — Ej.: en un futuro sobre un título público, la tasa del cupón corriente de dicho título · props: `{"termino": "Tasa de cupón del activo subyacente"}` · tramo [exacta]: «en un futuro sobre un título público, es la tasa del cupón corriente de dicho título»
- **e8 Definicion** «Precio pactado del subyacente» — Valor del subyacente pactado: tasa fija pactada, valor pactado del dólar, del bono, etc. · props: `{"termino": "Precio pactado del subyacente"}` · tramo [exacta]: «Valor del subyacente pactado.»
- R: e2 Obligacion —regula→ e1 Operacion
- R: e3 Obligacion —regula→ e1 Operacion
- R: e4 Obligacion —regula→ e1 Operacion
- R: e5 Obligacion —regula→ e1 Operacion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | ««C» si es compra a término» | `dentro_de_norma` |  | dentro de la Obligacion e5 (tramo «Consignar "C" si el contrato… es una compra a término»); sin Condicion |
| 2 | ««V» si es venta» | `dentro_de_norma` |  | dentro de la Obligacion e5 (tramo «o "V" si es una venta a término»); sin Condicion |

## `ric::5.1.3.4` — Se informará una sola partida 3600000Y, reflejando la situación de la entidad

Grupos: omisiones.

### Texto

> *heredado:* Sección 5. Exigencia por riesgo operacional
> *heredado:* 5.1. Normas de procedimiento
> *heredado:* 5.1.3. Reducción de la exigencia para entidades financieras del Grupo 2 que pertenezcan a
> *heredado:* los Grupos "A", "B" y "C".
> *propio:* 5.1.3.4. Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación; el promedio de las exigencias por riesgo de crédito se calculará en esta Institución en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos.

### Extracción (código K)

- **e1 Obligacion** «Partida única 3600000Y — reducción exigencia riesgo operacional» — En el marco de la reducción de la exigencia por riesgo operacional para entidades del Grupo 2 de los Grupos A, B y C, se informará una sola partida 3600000Y que refleje la situación de la entidad respecto de su calificación. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación»
- **e2 Operacion** «Cálculo por el BCRA del promedio de exigencias por riesgo de crédito» — El BCRA calcula el promedio de las exigencias por riesgo de crédito en base a los datos de exigencia por riesgo de crédito informada en los períodos previos. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el promedio de las exigencias por riesgo de crédito se calculará en esta Institución»
- R: e1 Obligacion —aplica_a→ Sujeto_rol_entidad_comprendida_reginf (mención «la entidad»)
- R: Sujeto_bcra (mención «esta Institución») —ejecuta→ e2 Operacion

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

### Extracción (código K)

- **op Operacion** «Informe CDCOn1 - Partida 70220000» — Información de los conceptos deducibles del capital ordinario de nivel uno en la determinación de la RPC · props: `{"tipo": "presentacion_informativa"}` · tramo [no]: «Conceptos deducibles del capital ordinario de nivel uno (CDCOn1) -Partida 70220000-»
- **o1 Obligacion** «Código 20800000: títulos no en poder» — Informar existencias de títulos valores, certificados de plazo fijo y otros títulos de crédito que no estén físicamente en poder de la entidad, según punto 8.4.1.3. de Capitales mínimos · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informarán las existencias de títulos valores, certificados de depósitos a plazo fijo, otros títulos de crédito, etc., que no se encuentren físicamente en poder de la entidad»
- **o2 Obligacion** «Código 20900000: deuda subordinada de otras EF» — Incluir el mayor saldo del mes de tenencia de títulos e instrumentos de deuda subordinados emitidos por otras entidades financieras · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se incluirá el mayor saldo registrado durante el mes a que corresponde la determinación de la responsabilidad patrimonial computable, de la tenencia de títulos valores y otros instrumentos de deuda, contractualmente subordinados a los demás pasivos, emitidos por otras entidades financieras.»
- **o3 Obligacion** «Código 21000000: corresponsalía sin investment grade» — Consignar el mayor saldo del mes de cuentas de corresponsalía con entidades financieras del exterior sin calificación investment grade de calificadoras admitidas por Evaluación de entidades financieras · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se consignará el mayor saldo registrado durante el mes a que corresponde la determinación de la responsabilidad patrimonial computable, de las cuentas de corresponsalía con entidades financieras del exterior que no cuenten con calificación "investment grade"»
- **o4 Obligacion** «Código 21100000: títulos de gobiernos extranjeros» — Incluir el mayor saldo del mes de títulos de gobiernos extranjeros con calificación inferior a la de títulos públicos argentinos y sin mercados de transacción habitual por valores relevantes (punto 8.4.1.4.) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se incluirá el mayor saldo registrado durante el mes a que corresponde la determinación del capital ordinario de nivel 1 (COn1), de los títulos emitidos por gobiernos de países extranjeros»
- **o5 Obligacion** «Código 21500000: inmuebles sin escritura inscripta» — Detallar el 100% del valor neto de inmuebles de uso propio y diversos (rubros 180000 y 190000) sin escritura traslativa de dominio inscripta en el Registro de la Propiedad Inmueble · props: `{"tipo": "presentacion_informativa"}` · umbral: ['el 100 % del valor -neto de la depreciación acumulada-'] · tramo [exacta]: «Se detallará el 100 % del valor -neto de la depreciación acumuladade los bienes inmuebles para uso propio y diversos»
- **o6 Obligacion** «Código 21600000: activos intangibles netos» — Incluir activos intangibles netos de amortizaciones, comprendida la llave de negocio que cumpla el punto 8.4.1.8. de Capitales mínimos · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se incluirán los activos intangibles netos de sus respectivas amortizaciones acumuladas.»
- **o7 Obligacion** «Código 21800000: insuficiencia de previsiones» — Informar las diferencias por insuficiencia de previsiones determinadas por la SEFyC no contabilizadas, con efecto al cierre del mes siguiente a la notificación (punto 2.7. Previsiones mínimas; 8.4.1.12. Capitales mínimos) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Comprende las diferencias por insuficiencia de constitución de las previsiones mínimas por riesgo de incobrabilidad determinada por la Superintendencia de Entidades Financieras y Cambiarias, en la medida en que no hayan sido contabilizadas»
- **o8 Obligacion** «Código 22000000: llave negativa con signo negativo» — Informar la llave negativa neta de desafectaciones; computarla con signo negativo dentro de CDCOn1 · props: `{"tipo": "calculo"}` · tramo [exacta]: «Comprende el valor -neto de desafectacionesde la llave negativa registrada en adquisiciones de participaciones por un costo inferior a su valor patrimonial proporcional.»
- **r1 Restriccion** «Llave negativa solo en información consolidada/combinada» — La partida 22000000 se computa únicamente en la información consolidada de la adquirente o individual del ente combinado en caso de fusión · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «Esta partida se computará únicamente en la información consolidada de la adquirente o en la información individual del ente combinado»
- **o9 Obligacion** «Código 22100000: ganancia mínima presunta e impuestos diferidos» — Informar el saldo a favor por impuesto a la ganancia mínima presunta neto de previsiones que exceda el 10% del PN básico del mes anterior, y el saldo a favor de activos por impuestos diferidos · props: `{"tipo": "presentacion_informativa"}` · umbral: ['que exceda el 10% del patrimonio neto básico correspondiente al mes anterior'] · tramo [exacta]: «Comprende el saldo a favor por aplicación del impuesto a la ganancia mínima presunta - neto de las previsionesque exceda el 10% del patrimonio neto básico»
- **o10 Obligacion** «Código 22300000: aportes no autorizados a capitalizar» — Informar aportes registrados cuya capitalización no fue autorizada por la SEFyC · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informarán los aportes registrados contablemente como tales cuya capitalización aún no haya sido autorizada por la SEFyC.»
- **o11 Obligacion** «Códigos 22510000-22530000: excesos afectación en garantía» — Consignar excesos a los límites de afectación de activos en garantía (Sección 3 de Afectación de activos en garantía) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se consignarán los excesos a los límites para la afectación de activos en garantía»
- **o12 Obligacion** «Código 22600000: ganancias por titulización» — Incluir ganancias por ventas de titulización cuando no se cumplan requisitos de opciones de exclusión, exista respaldo implícito o corresponda exigencia por cláusulas de cancelación anticipada · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se incluirán las ganancias por ventas resultantes de operaciones de titulización»
- **c1 Condicion** «Incumplimiento opciones de exclusión» — Cuando no se cumplan requisitos de opciones de exclusión · tramo [exacta]: «cuando no se cumpla con los requisitos vinculados con opciones de exclusión»
- **c2 Condicion** «Respaldo implícito de titulizaciones» — Cuando exista respaldo implícito de titulizaciones · tramo [exacta]: «cuando exista respaldo implícito de titulizaciones»
- **c3 Condicion** «Exigencia por cancelación anticipada» — Cuando corresponda exigencia por titulizaciones con cláusulas de cancelación anticipada · tramo [exacta]: «cuando corresponda calcular exigencia por titulizaciones con cláusulas de cancelación anticipada»
- **o13 Obligacion** «Código 22600000: ganancias cesión con responsabilidad» — Incluir ganancias por venta o cesión de cartera con responsabilidad para el cedente (punto 8.4.1.16.) · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «También se incluirán las ganancias por operaciones de venta o cesión de cartera con responsabilidad para el cedente»
- **o14 Obligacion** «Código 22700000: asistencia al SPNF excedida» — Informar el mayor saldo de asistencia crediticia del mes cuando los adelantos del punto 3.2.5. de Financiamiento al SPNF superen el límite o no se cancelen en plazo · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informará el mayor saldo de la asistencia crediticia otorgada en el mes»
- **c4 Condicion** «Adelantos SPNF exceden límite o plazo» — Adelantos que superen el límite autorizado y/o no se cancelen en plazo · tramo [exacta]: «cuando los adelantos previstos en el punto 3.2.5. de la Sección 3. de las normas sobre "Financiamiento al sector público no financiero" superen el límite autorizado y/o no sean cancelados en los plazos allí previstos»
- **o15 Obligacion** «Código 26300000: previsiones cartera normal» — Informar previsiones de financiaciones normales o con garantías preferidas A que no superen el 1,25% de los APRs; computar la absorción de la partida 21300000 cuando corresponda · props: `{"tipo": "presentacion_informativa"}` · umbral: ['que no superen el 1,25 % de los APRs'] · tramo [exacta]: «Se informarán las previsiones por riesgo de incobrabilidad correspondientes a financiaciones en situación normal o cubiertas con garantías preferidas "A" que no superen el 1,25 % de los APRs.»
- **o16 Obligacion** «Deducción inversiones en servicios complementarios y seguros» — Códigos 23400000 a 27400000: reflejar deducción por nivel de capital de inversiones en capital regulatorio de empresas de servicios complementarios no consolidadas y aseguradoras, netas del cronograma del punto 11.5. · props: `{"tipo": "calculo"}` · tramo [exacta]: «Reflejarán la deducción -para cada nivel de capital consideradode las inversiones en instrumentos computables como capital regulatorio de empresas de servicios complementarios -no sujetas a supervisión consolidaday compañías de seguro»
- **o17 Obligacion** «Código 21200000: otros conceptos deducibles COn1» — Informar conceptos deducibles del COn1 no incluidos en otros códigos · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informarán los conceptos deducibles del COn1, no incluidos en otros códigos.»
- R: o1 Obligacion —regula→ op Operacion
- R: o2 Obligacion —regula→ op Operacion
- R: o3 Obligacion —regula→ op Operacion
- R: o4 Obligacion —regula→ op Operacion
- R: o5 Obligacion —regula→ op Operacion
- R: o6 Obligacion —regula→ op Operacion
- R: o7 Obligacion —regula→ op Operacion
- R: o8 Obligacion —regula→ op Operacion
- R: r1 Restriccion —limita→ op Operacion
- R: o9 Obligacion —regula→ op Operacion
- R: o10 Obligacion —regula→ op Operacion
- R: o11 Obligacion —regula→ op Operacion
- R: o12 Obligacion —regula→ op Operacion
- R: o13 Obligacion —regula→ op Operacion
- R: o14 Obligacion —regula→ op Operacion
- R: o15 Obligacion —regula→ op Operacion
- R: o16 Obligacion —regula→ op Operacion
- R: o17 Obligacion —regula→ op Operacion
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
| 4 | «código 22700000» | `condicion_con_relacion` |  | c4 Condicion —condicion_de→ o14 Obligacion |
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

### Extracción (código K)

- **op1 Operacion** «Captación de depósitos» — Nivel de depósitos de la entidad, según importe registrado en el código 310000 del Balance de Saldos · props: `{"tipo": "captacion de depositos"}` · tramo [exacta]: «el nivel de depósitos»
- **r1 Restriccion** «Tope nivel de depósitos del mes de incumplimiento» — No podrá excederse el nivel de depósitos alcanzado en el mes en que se origine el incumplimiento, considerando el importe del código 310000 del Balance de Saldos; rige mientras persista alguna de las situaciones previstas. En regulaciones sobre base consolidada, las partidas se asimilan a la posición individual. · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento", "comparacion": "maximo_inclusivo", "base": "nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento", "regla_comparacion": "limite_relativo:negacion:raiz_exced", "origen": "e1", "tramo_verificado": "exacta"}]}` · no definidas: `{"vigencia": "Dicho límite se observará mientras persista alguna de las situaciones previstas.", "base_consolidada": "En los casos de regulaciones sobre base consolidada, se asimilarán las partidas a ` · umbral: ['No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origi…'] · tramo [exacta]: «No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incumplimiento»
- **c1 Condicion** «Obligación de presentar Plan de Regularización» — Supuesto alternativo (basta alguno): obligatoriedad de presentar el Plan de Regularización y Saneamiento en capitales mínimos. · tramo [exacta]: «Obligatoriedad de presentación del Plan de Regularización y Saneamiento en capitales mínimos.»
- **c2 Condicion** «Incrementos de exigencia superan 5 %» — Supuesto alternativo: la suma de incrementos de exigencia por riesgo de crédito por incumplimientos en relaciones técnicas de activos inmovilizados y/o crediticias supera el 5 % de dicha exigencia (código 70100000). · umbral: ['supere el 5 % de dicha exigencia'] · tramo [exacta]: «La suma de incrementos de exigencia de capitales mínimos por riesgo de crédito resultantes de los incumplimientos en las relaciones técnicas de activos inmovilizados y/o crediticias, supere el 5 % de dicha exigencia (código 70100000).»
- **x1 Excepcion** «Crecimiento por devengamiento de intereses admitido» — Del tope de depósitos se admite únicamente el crecimiento originado por el devengamiento de intereses. · tramo [exacta]: «Se admitirá únicamente el crecimiento originado por el devengamiento de intereses.»
- R: r1 Restriccion —limita→ op1 Operacion
- R: c1 Condicion —condicion_de→ r1 Restriccion
- R: c2 Condicion —condicion_de→ r1 Restriccion
- R: x1 Excepcion —exceptua→ r1 Restriccion

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «obligación del plan de regularización» | `condicion_con_relacion` |  | c1 Condicion —condicion_de→ r1 Restriccion |
| 2 | «incrementos de más del 5 %» | `condicion_con_relacion` |  | c2 Condicion con el umbral —condicion_de→ r1 Restriccion |
| 3 | «base consolidada» | `dentro_de_norma` |  | dentro de la Restriccion r1 (descripción «En regulaciones sobre base consolidada se asimilan las partidas…»); sin Condicion |
| 4 | «mientras persista» | `dentro_de_norma` |  | dentro de la Restriccion r1 (descripción «mientras persista alguna de las situaciones previstas»); sin Condicion |

