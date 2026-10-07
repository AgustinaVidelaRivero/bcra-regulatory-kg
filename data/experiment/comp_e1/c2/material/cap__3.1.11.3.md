# `cap::3.1.11.3` — Determinación del ponderador de riesgo (RW).

Grupos: grupo_c. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos.
> *heredado:* 3.1. Tratamiento de las titulizaciones.
> *heredado:* Se denomina "posición de titulización" a la exposición a una titulización (o retitulización), tradicional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes conceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos ("AssetBacked Securities", ABS) y bonos de titulización hipotecaria ("Mortgage-Backed Securities", MBS)–, mejoras crediticias, facilidades de liquidez, "swaps" de tasa de interés o de monedas y derivados de crédito. Las reservas ("reserve accounts"), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo también el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad económica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una determinada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> *heredado:* 3.1.11. Enfoque estandarizado.
> *heredado:* Los ponderadores de riesgo a aplicar a las posiciones de una titulización y a las exposiciones subyacentes de una retitulización para la determinación de la exigencia de capital se establecerán empleando las disposiciones de este punto. Las posiciones de titulización a las que no se les pueda aplicar el enfoque estandarizado deberán ser ponderadas al 1250 %.
> *propio:* 3.1.11.3. Determinación del ponderador de riesgo (RW). El ponderador de riesgo RW a asignar a una posición de titulización se calculará con ajuste a lo siguiente: i) Si D es menor o igual a K , el ponderador será de 1250 %. A ii) Si A es mayor o igual a K , el ponderador será igual a K multiplicado A SSFA(KA) por 12,5. iii) Si K es mayor que A y menor que D, el ponderador será un promedio A ponderado entre 1250 % y 12,5 veces K conforme a la siguiente exSSFA(KA) presión: El ponderador para coberturas del riesgo de mercado, tales como "swaps" de moneda o de tasa de interés, se inferirá a partir de una posición de titulización de igual prelación ("pari passu") con los "swaps" o, si tal posición no existiera, a partir del tramo subordinado más próximo. El ponderador resultante estará sujeto a un mínimo de: a) 15 % para titulizaciones que no cumplan con los criterios STC –punto 3.1.14.–. b) 10 % para los tramos de máxima preferencia de titulizaciones que cumplan con los criterios STC –punto 3.1.14.– y 15 % para los tramos subordinados de esas titulizaciones. c) 100 % para retitulizaciones. Para posiciones de titulización de máxima preferencia se podrá aplicar el tratamiento de transparencia ("look-through") de conformidad con lo previsto en el punto 3.1.6. Si el ponderador que surge de la aplicación de ese tratamiento fuera menor que el ponderador mínimo que corresponda de acuerdo con los apartados a) a c) precedentes, se podrá aplicar el primero.

## Supuestos de la fase A de T4 (M1)

1. «i) a iii) según D, A y KA» (miembros i))
2. «i) a iii) según D, A y KA» (miembros ii))
3. «i) a iii) según D, A y KA» (miembros iii))
4. «si no existiera la posición pari passu»
5. «mínimos por STC»
6. «look-through menor que el mínimo»

## Código A

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

### A — supuestos a clasificar

- 1. «i) a iii) según D, A y KA» → candidatos: —
- 2. «i) a iii) según D, A y KA» → candidatos: —
- 3. «i) a iii) según D, A y KA» → candidatos: —
- 4. «si no existiera la posición pari passu» → candidatos: ob4 Obligacion (1.00), ob1 Obligacion (0.25), op1 Operacion (0.25)
- 5. «mínimos por STC» → candidatos: r1 Restriccion (0.50), r2 Restriccion (0.50), r3 Restriccion (0.50)
- 6. «look-through menor que el mínimo» → candidatos: p2 Potestad (1.00), p1 Potestad (0.50), ob1 Obligacion (0.25), ob3 Obligacion (0.25)

## Código H

- **op1 Operacion** «Determinación del ponderador de riesgo de posición de titulización» — Cálculo del ponderador de riesgo RW a asignar a una posición de titulización · props: `{"tipo": "calculo"}` · tramo [exacta]: «El ponderador de riesgo RW a asignar a una posición de titulización se calculará con ajuste a lo siguiente»
- **ob1 Obligacion** «RW 1250 % si D ≤ K_A» — Si D es menor o igual a K_A, el ponderador RW de la posición de titulización será de 1250 %. · props: `{"tipo": "calculo"}` · umbral: ['1250 %'] · tramo [exacta]: «Si D es menor o igual a K , el ponderador será de 1250 %.»
- **c1 Condicion** «D menor o igual a K_A» — Supuesto en que D es menor o igual a K_A · props: `{"umbrales": [{"tramo": "D es menor o igual a K", "comparacion": "maximo_inclusivo", "base": "K", "regla_comparacion": "limite_relativo:compuesta:menor_o_igual", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['D es menor o igual a K'] · tramo [exacta]: «Si D es menor o igual a K»
- **ob2 Obligacion** «RW = 12,5 × K_SSFA(KA) si A ≥ K_A» — Si A es mayor o igual a K_A, el ponderador será igual a K_SSFA(KA) multiplicado por 12,5. · props: `{"tipo": "calculo", "umbrales": [{"tramo": "multiplicado\nA SSFA(KA)\npor 12,5", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['multiplicado A SSFA(KA) por 12,5'] · tramo [exacta]: «Si A es mayor o igual a K , el ponderador será igual a K multiplicado A SSFA(KA) por 12,5.»
- **c2 Condicion** «A mayor o igual a K_A» — Supuesto en que A es mayor o igual a K_A · props: `{"umbrales": [{"tramo": "A es mayor o igual a K", "comparacion": "minimo_inclusivo", "base": "K", "regla_comparacion": "limite_relativo:compuesta:mayor_o_igual", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['A es mayor o igual a K'] · tramo [exacta]: «Si A es mayor o igual a K»
- **ob3 Obligacion** «RW promedio ponderado si K_A < A < D» — Si K_A es mayor que A y menor que D, el ponderador será un promedio ponderado entre 1250 % y 12,5 veces K_SSFA(KA) conforme a la expresión indicada. · props: `{"tipo": "calculo"}` · umbral: ['entre 1250 % y 12,5 veces K'] · tramo [tokens]: «el ponderador será un promedio A ponderado entre 1250 % y 12,5 veces K conforme a la siguiente exSSFA(KA) presión»
- **c3 Condicion** «A entre K_A y D» — Supuesto en que K_A es mayor que A y menor que D · props: `{"umbrales": [{"tramo": "mayor que A y menor que D", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['mayor que A y menor que D'] · tramo [exacta]: «Si K es mayor que A y menor que D»
- **ob4 Obligacion** «Inferir ponderador de coberturas de riesgo de mercado» — El ponderador para coberturas del riesgo de mercado (swaps de moneda o de tasa) se infiere de una posición de titulización pari passu o, si no existe, del tramo subordinado más próximo. · props: `{"tipo": "calculo"}` · tramo [exacta]: «El ponderador para coberturas del riesgo de mercado, tales como "swaps" de moneda o de tasa de interés, se inferirá a partir de una posición de titulización de igual prelación ("pari passu") con los "swaps" o, si tal posición no existiera, a partir del tramo subordinado más próximo.»
- **r1 Restriccion** «Mínimo 15 % titulizaciones no STC» — El ponderador resultante estará sujeto a un mínimo de 15 % para titulizaciones que no cumplan con los criterios STC. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['un mínimo de: a) 15 %'] · tramo [exacta]: «15 % para titulizaciones que no cumplan con los criterios STC –punto 3.1.14.–»
- **r2 Restriccion** «Mínimo 10 % tramos de máxima preferencia STC» — El ponderador resultante estará sujeto a un mínimo de 10 % para los tramos de máxima preferencia de titulizaciones que cumplan con los criterios STC. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['10 % para los tramos de máxima preferencia'] · tramo [exacta]: «10 % para los tramos de máxima preferencia de titulizaciones que cumplan con los criterios STC –punto 3.1.14.–»
- **r3 Restriccion** «Mínimo 15 % tramos subordinados STC» — El ponderador resultante estará sujeto a un mínimo de 15 % para los tramos subordinados de las titulizaciones que cumplan con los criterios STC. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['15 % para los tramos subordinados'] · tramo [exacta]: «15 % para los tramos subordinados de esas titulizaciones»
- **r4 Restriccion** «Mínimo 100 % retitulizaciones» — El ponderador resultante estará sujeto a un mínimo de 100 % para retitulizaciones. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['100 % para retitulizaciones'] · tramo [exacta]: «100 % para retitulizaciones»
- **p1 Potestad** «Look-through en posiciones de máxima preferencia» — Para posiciones de titulización de máxima preferencia se puede aplicar el tratamiento de transparencia (look-through) del punto 3.1.6. · tramo [exacta]: «Para posiciones de titulización de máxima preferencia se podrá aplicar el tratamiento de transparencia ("look-through") de conformidad con lo previsto en el punto 3.1.6.»
- **p2 Potestad** «Aplicar RW look-through menor al mínimo» — Si el ponderador que surge del look-through es menor que el mínimo de los apartados a) a c), se puede aplicar el ponderador del look-through. · tramo [exacta]: «Si el ponderador que surge de la aplicación de ese tratamiento fuera menor que el ponderador mínimo que corresponda de acuerdo con los apartados a) a c) precedentes, se podrá aplicar el primero.»
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
- Omisión `formula` [exacta]: «conforme a la siguiente exSSFA(KA) presión:» — La expresión del promedio ponderado es una fórmula no incluida en el texto extraído; no se reconstruye.

### H — supuestos a clasificar

- 1. «i) a iii) según D, A y KA» → candidatos: —
- 2. «i) a iii) según D, A y KA» → candidatos: —
- 3. «i) a iii) según D, A y KA» → candidatos: —
- 4. «si no existiera la posición pari passu» → candidatos: ob4 Obligacion (1.00), ob1 Obligacion (0.25), op1 Operacion (0.25)
- 5. «mínimos por STC» → candidatos: r1 Restriccion (0.50), r2 Restriccion (0.50), r3 Restriccion (0.50)
- 6. «look-through menor que el mínimo» → candidatos: p2 Potestad (1.00), p1 Potestad (0.50), c1 Condicion (0.25), c3 Condicion (0.25)

## Código K

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

### K — supuestos a clasificar

- 1. «i) a iii) según D, A y KA» → candidatos: —
- 2. «i) a iii) según D, A y KA» → candidatos: —
- 3. «i) a iii) según D, A y KA» → candidatos: —
- 4. «si no existiera la posición pari passu» → candidatos: ob4 Obligacion (1.00), ob1 Obligacion (0.25), op1 Operacion (0.25)
- 5. «mínimos por STC» → candidatos: ex1 Excepcion (0.50), r1 Restriccion (0.50), r2 Restriccion (0.50), r3 Restriccion (0.50)
- 6. «look-through menor que el mínimo» → candidatos: ex1 Excepcion (1.00), p1 Potestad (0.50), c1 Condicion (0.25), c3 Condicion (0.25)

## Código W

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

### W — supuestos a clasificar

- 1. «i) a iii) según D, A y KA» → candidatos: —
- 2. «i) a iii) según D, A y KA» → candidatos: —
- 3. «i) a iii) según D, A y KA» → candidatos: —
- 4. «si no existiera la posición pari passu» → candidatos: o4 Obligacion (1.00), o1 Obligacion (0.25), o2 Obligacion (0.25), o3 Obligacion (0.25)
- 5. «mínimos por STC» → candidatos: r1 Restriccion (0.50), r2 Restriccion (0.50), r3 Restriccion (0.50), x1 Excepcion (0.50)
- 6. «look-through menor que el mínimo» → candidatos: x1 Excepcion (1.00), p1 Potestad (0.50), c1 Condicion (0.25), c3 Condicion (0.25)

