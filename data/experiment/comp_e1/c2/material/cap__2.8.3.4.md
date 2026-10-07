# `cap::2.8.3.4` — En el caso de exposiciones minoristas a personas humanas, el total de los

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 2. Capital mínimo por riesgo de crédito.
> *heredado:* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
> *heredado:* (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de importancia sistémica global (G-SIB).
> *heredado:* ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
> *heredado:* 2.8. Exposiciones minoristas.
> *heredado:* 2.8.3. Exposiciones minoristas normativas. Criterios.
> *propio:* 2.8.3.4. En el caso de exposiciones minoristas a personas humanas, el total de los vencimientos por las cuotas de todas las financiaciones de la entidad financiera que cuenten con amortización periódica –sin considerar las cuotas de créditos de otras entidades– no deberá exceder, al momento de los acuerdos, el 30% de los ingresos del deudor y/o, en su caso, de los codeudores. En consecuencia, los márgenes acordados para los descubiertos en cuenta corriente y los límites de compra de las tarjetas de crédito –en ambos casos, tanto el utilizado como el disponible–, así como los préstamos personales preacordados –en la medida en que aún no hayan sido formalizados ni desembolsados al cliente–, no formarán parte del numerador de la relación cuota/ingreso por no contar con una amortización periódica. Deberá considerarse dentro del concepto "cuotas" aquellas que el cliente tenga por compras financiadas en el marco del sistema de tarjeta de crédito. A los efectos de considerar en las exposiciones minoristas normativas a los créditos incorporados a través de una compra de cartera, se deberá contar con la información necesaria para verificar el cumplimiento de los criterios y límites detallados precedentemente.

## Omisiones leídas en T4 (M2)

sin_marca:7 [no normativa; propio] «En consecuencia»

## Código A

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

### A — omisiones de T4 a clasificar

- sin_marca:7 → entidades: — | omisiones: —

## Código H

- **op1 Operacion** «Financiación minorista a personas humanas con amortización periódica» — Exposiciones minoristas a personas humanas: financiaciones de la entidad financiera con amortización periódica, sin considerar cuotas de créditos de otras entidades, al momento de los acuerdos. · props: `{"tipo": "financiacion"}` · tramo [exacta]: «exposiciones minoristas a personas humanas, el total de los vencimientos por las cuotas de todas las financiaciones de la entidad financiera que cuenten con amortización periódica»
- **r1 Restriccion** «Tope 30% cuota/ingreso del deudor» — El total de los vencimientos por las cuotas de todas las financiaciones de la entidad con amortización periódica no deberá exceder, al momento de los acuerdos, el 30% de los ingresos del deudor y/o codeudores. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['no deberá exceder, al momento de los acuerdos, el 30% de los ingresos del deudor…'] · tramo [exacta]: «no deberá exceder, al momento de los acuerdos, el 30% de los ingresos del deudor y/o, en su caso, de los codeudores»
- **d1 Definicion** «Exclusión del numerador cuota/ingreso: márgenes y límites sin amortización» — No forman parte del numerador de la relación cuota/ingreso, por no contar con amortización periódica: los márgenes acordados para descubiertos en cuenta corriente y los límites de compra de tarjetas de crédito (utilizado y disponible), y los préstamos personales preacordados aún no formalizados ni desembolsados. · props: `{"termino": "numerador de la relación cuota/ingreso"}` · tramo [exacta]: «los márgenes acordados para los descubiertos en cuenta corriente y los límites de compra de las tarjetas de crédito»
- **d2 Definicion** «Concepto cuotas incluye compras financiadas con tarjeta» — Dentro del concepto cuotas deben considerarse las que el cliente tenga por compras financiadas en el marco del sistema de tarjeta de crédito. · props: `{"termino": "cuotas"}` · tramo [exacta]: «Deberá considerarse dentro del concepto "cuotas" aquellas que el cliente tenga por compras financiadas en el marco del sistema de tarjeta de crédito.»
- **op2 Operacion** «Incorporación de créditos por compra de cartera a exposiciones minoristas normativas» — Consideración en las exposiciones minoristas normativas de los créditos incorporados a través de una compra de cartera. · props: `{"tipo": "compra_de_cartera"}` · tramo [exacta]: «considerar en las exposiciones minoristas normativas a los créditos incorporados a través de una compra de cartera»
- **o1 Obligacion** «Contar con información para verificar criterios y límites en compra de cartera» — Para considerar en las exposiciones minoristas normativas los créditos incorporados por compra de cartera, se deberá contar con la información necesaria para verificar el cumplimiento de los criterios y límites detallados precedentemente. · props: `{"tipo": "otra"}` · tramo [exacta]: «se deberá contar con la información necesaria para verificar el cumplimiento de los criterios y límites detallados precedentemente»
- R: r1 Restriccion —limita→ op1 Operacion
- R: o1 Obligacion —regula→ op2 Operacion
- R: r1 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera»)
- R: Sujeto_entidad_financiera (mención «la entidad financiera») —ejecuta→ op1 Operacion

### H — omisiones de T4 a clasificar

- sin_marca:7 → entidades: — | omisiones: —

## Código K

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

### K — omisiones de T4 a clasificar

- sin_marca:7 → entidades: — | omisiones: —

## Código W

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

### W — omisiones de T4 a clasificar

- sin_marca:7 → entidades: — | omisiones: —

