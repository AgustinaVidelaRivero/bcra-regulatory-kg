# `ext::8.4.2` — Determinación del plazo para el ingreso y liquidación de las divisas.

Grupos: grupo_c. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
> *heredado:* 8.4. Responsabilidades de la entidad nominada para el seguimiento del permiso.
> *propio:* 8.4.2. Determinación del plazo para el ingreso y liquidación de las divisas. La entidad deberá determinar el plazo aplicable a cada exportación a partir de lo dispuesto en el punto 7.1.1. En el caso de que una exportación esté compuesta por distintos productos, el plazo aplicable será aquel que representa una mayor proporción del valor FOB total de la exportación. La fecha de vencimiento que le corresponde a una exportación será aquella resultante de sumar el plazo aplicable a la fecha de cumplido de embarque otorgada por la Aduana. Si la fecha resultante fuese un día no hábil, el vencimiento se trasladará al primer día hábil siguiente. En caso de que exista una ampliación del plazo para un producto, el nuevo plazo se aplicará tanto a las exportaciones embarcadas a partir de la vigencia de la ampliación como a las embarcadas previamente cuyo plazo para ingresar y liquidar no se encontrase vencido a ese momento. En tanto en caso de existir una reducción del plazo vigente, el plazo reducido sólo regirá para las operaciones que se oficialicen a partir de la vigencia del nuevo plazo.

## Supuestos de la fase A de T4 (M1)

1. «exportación de varios productos»
2. «fecha no hábil»
3. «ampliación del plazo»
4. «reducción del plazo»

## Código A

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

### A — supuestos a clasificar

- 1. «exportación de varios productos» → candidatos: c1 Condicion (0.67), ob2 Obligacion (0.67), ob1 Obligacion (0.33), ob3 Obligacion (0.33)
- 2. «fecha no hábil» → candidatos: c2 Condicion (1.00), ob4 Obligacion (1.00), ob3 Obligacion (0.50)
- 3. «ampliación del plazo» → candidatos: c3 Condicion (1.00), ob5 Obligacion (1.00), c4 Condicion (0.50), ob1 Obligacion (0.50)
- 4. «reducción del plazo» → candidatos: c4 Condicion (1.00), ob6 Obligacion (1.00), c3 Condicion (0.50), ob1 Obligacion (0.50)

## Código H

- **op1 Operacion** «Determinación del plazo de ingreso y liquidación de divisas» — Determinación, por la entidad nominada, del plazo aplicable a cada exportación para el ingreso y liquidación de las divisas, a partir de lo dispuesto en el punto 7.1.1. · props: `{"tipo": "determinacion_de_plazo"}` · tramo [exacta]: «Determinación del plazo para el ingreso y liquidación de las divisas.»
- **ob1 Obligacion** «Determinar plazo aplicable a cada exportación» — La entidad debe determinar el plazo aplicable a cada exportación a partir de lo dispuesto en el punto 7.1.1; si la exportación está compuesta por distintos productos, el plazo aplicable es el que representa una mayor proporción del valor FOB total de la exportación. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La entidad deberá determinar el plazo aplicable a cada exportación a partir de lo dispuesto en el punto 7.1.1.»
- **c1 Condicion** «Exportación compuesta por distintos productos» — Supuesto en que la exportación está compuesta por distintos productos; el plazo aplicable es el que representa una mayor proporción del valor FOB total. · tramo [exacta]: «En el caso de que una exportación esté compuesta por distintos productos»
- **ob2 Obligacion** «Plazo del producto de mayor proporción FOB» — En una exportación compuesta por distintos productos, el plazo aplicable es el que representa una mayor proporción del valor FOB total de la exportación. · props: `{"tipo": "calculo", "umbrales": [{"tramo": "una mayor proporción del valor FOB total de la\nexportación", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['una mayor proporción del valor FOB total de la exportación'] · tramo [exacta]: «el plazo aplicable será aquel que representa una mayor proporción del valor FOB total de la exportación.»
- **ob3 Obligacion** «Calcular fecha de vencimiento de la exportación» — La fecha de vencimiento de una exportación resulta de sumar el plazo aplicable a la fecha de cumplido de embarque otorgada por la Aduana. · props: `{"tipo": "calculo"}` · tramo [exacta]: «La fecha de vencimiento que le corresponde a una exportación será aquella resultante de sumar el plazo aplicable a la fecha de cumplido de embarque otorgada por la Aduana.»
- **c2 Condicion** «Fecha resultante en día no hábil» — Supuesto en que la fecha de vencimiento resultante sea un día no hábil. · tramo [exacta]: «Si la fecha resultante fuese un día no hábil»
- **ob4 Obligacion** «Trasladar vencimiento al primer día hábil siguiente» — Si la fecha de vencimiento resultante fuese un día no hábil, el vencimiento se traslada al primer día hábil siguiente. · props: `{"tipo": "calculo"}` · tramo [exacta]: «el vencimiento se trasladará al primer día hábil siguiente.»
- **ob5 Obligacion** «Ampliación de plazo: aplica a embarcadas previas no vencidas» — Ante una ampliación del plazo para un producto, el nuevo plazo se aplica a las exportaciones embarcadas desde la vigencia de la ampliación y a las embarcadas previamente cuyo plazo para ingresar y liquidar no estuviese vencido a ese momento. · props: `{"tipo": "calculo"}` · tramo [exacta]: «En caso de que exista una ampliación del plazo para un producto, el nuevo plazo se aplicará tanto a las exportaciones embarcadas a partir de la vigencia de la ampliación como a las embarcadas previamente cuyo plazo para ingresar y liquidar no se encontrase vencido a ese momento.»
- **c3 Condicion** «Ampliación del plazo para un producto» — Supuesto en que existe una ampliación del plazo para un producto. · tramo [exacta]: «En caso de que exista una ampliación del plazo para un producto»
- **ob6 Obligacion** «Reducción de plazo: solo operaciones oficializadas después» — Ante una reducción del plazo vigente, el plazo reducido rige solo para las operaciones que se oficialicen a partir de la vigencia del nuevo plazo. · props: `{"tipo": "calculo"}` · tramo [exacta]: «en caso de existir una reducción del plazo vigente, el plazo reducido sólo regirá para las operaciones que se oficialicen a partir de la vigencia del nuevo plazo.»
- **c4 Condicion** «Reducción del plazo vigente» — Supuesto en que existe una reducción del plazo vigente. · tramo [exacta]: «en caso de existir una reducción del plazo vigente»
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
- R: ob1 Obligacion —aplica_a→ Sujeto (mención «La entidad»)
- R: ob2 Obligacion —aplica_a→ Sujeto (mención «La entidad»)
- R: ob3 Obligacion —aplica_a→ Sujeto (mención «La entidad»)
- R: ob4 Obligacion —aplica_a→ Sujeto (mención «La entidad»)
- R: ob5 Obligacion —aplica_a→ Sujeto (mención «La entidad»)
- R: ob6 Obligacion —aplica_a→ Sujeto (mención «La entidad»)

### H — supuestos a clasificar

- 1. «exportación de varios productos» → candidatos: c1 Condicion (0.67), ob1 Obligacion (0.67), ob2 Obligacion (0.67), ob3 Obligacion (0.33)
- 2. «fecha no hábil» → candidatos: c2 Condicion (1.00), ob4 Obligacion (1.00), ob3 Obligacion (0.50)
- 3. «ampliación del plazo» → candidatos: c3 Condicion (1.00), ob5 Obligacion (1.00), c1 Condicion (0.50), c4 Condicion (0.50)
- 4. «reducción del plazo» → candidatos: c4 Condicion (1.00), ob6 Obligacion (1.00), c1 Condicion (0.50), c3 Condicion (0.50)

## Código K

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

### K — supuestos a clasificar

- 1. «exportación de varios productos» → candidatos: c1 Condicion (0.67), o2 Obligacion (0.67), o1 Obligacion (0.33), o3 Obligacion (0.33)
- 2. «fecha no hábil» → candidatos: c2 Condicion (1.00), o4 Obligacion (1.00), o3 Obligacion (0.50)
- 3. «ampliación del plazo» → candidatos: c3 Condicion (1.00), o5 Obligacion (1.00), c4 Condicion (0.50), o1 Obligacion (0.50)
- 4. «reducción del plazo» → candidatos: c4 Condicion (1.00), o6 Obligacion (1.00), c3 Condicion (0.50), o1 Obligacion (0.50)

## Código W

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

### W — supuestos a clasificar

- 1. «exportación de varios productos» → candidatos: c1 Condicion (0.67), e2 Obligacion (0.67), e1 Obligacion (0.33), e3 Obligacion (0.33)
- 2. «fecha no hábil» → candidatos: c2 Condicion (1.00), e4 Obligacion (1.00), e3 Obligacion (0.50)
- 3. «ampliación del plazo» → candidatos: c3 Condicion (1.00), e5 Obligacion (1.00), c4 Condicion (0.50), e1 Obligacion (0.50)
- 4. «reducción del plazo» → candidatos: c4 Condicion (1.00), e6 Obligacion (1.00), c3 Condicion (0.50), e1 Obligacion (0.50)

