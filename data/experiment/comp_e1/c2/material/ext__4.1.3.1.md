# `ext::4.1.3.1` — Cuando el emisor de la tarjeta sea una entidad financiera, el titular podrá

Grupos: grupo_c. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 4. Otras disposiciones específicas.
> *heredado:* 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tarjetas de
> *heredado:* crédito, compra y prepagas emitidas en el país.
> *heredado:* 4.1.3. Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o
> *heredado:* de compra.
> *propio:* 4.1.3.1. Cuando el emisor de la tarjeta sea una entidad financiera, el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos, debiendo aplicar como máximo en este caso el tipo de cambio vendedor (aplicable para operaciones efectuadas por ventanilla o a través de medios electrónicos, según corresponda) de la entidad emisora de la tarjeta del momento de cancelación –o día hábil inmediato anterior cuando el pago se efectúe un día inhábil–. En los casos donde los clientes hayan pactado el débito automático del resumen de la tarjeta en cuentas de la propia entidad emisora, aplicará el tipo de cambio vendedor para operaciones efectuadas a través de medios electrónicos de pago del cierre del mismo día hábil del pago.

## Supuestos de la fase A de T4 (M1)

1. «emisor entidad financiera»
2. «pago en día inhábil»
3. «débito automático pactado»

## Código A

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

### A — supuestos a clasificar

- 1. «emisor entidad financiera» → candidatos: cond1 Condicion (1.00), pot1 Potestad (1.00), op1 Operacion (0.67), cond2 Condicion (0.33)
- 2. «pago en día inhábil» → candidatos: res1 Restriccion (1.00), res2 Restriccion (0.67)
- 3. «débito automático pactado» → candidatos: cond2 Condicion (1.00), res2 Restriccion (1.00)

## Código H

- **op1 Operacion** «Cancelación de consumos en moneda extranjera con tarjeta» — Cancelación por el titular de consumos en moneda extranjera realizados con tarjeta cuyo emisor es una entidad financiera, en moneda extranjera o en pesos. · props: `{"tipo": "cancelacion_consumos_tarjeta"}` · tramo [exacta]: «cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- **p1 Potestad** «Titular puede cancelar en moneda extranjera o pesos» — Cuando el emisor de la tarjeta es una entidad financiera, el titular puede cancelar los consumos en moneda extranjera en esa moneda o en pesos. · tramo [exacta]: «el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- **c1 Condicion** «Emisor de la tarjeta es entidad financiera» — El emisor de la tarjeta es una entidad financiera; habilita la facultad del titular de cancelar los consumos en moneda extranjera o en pesos. · tramo [exacta]: «Cuando el emisor de la tarjeta sea una entidad financiera»
- **r1 Restriccion** «Tope tipo de cambio vendedor — cancelación en pesos» — En la cancelación en pesos se aplica como máximo el tipo de cambio vendedor (ventanilla o medios electrónicos, según corresponda) de la entidad emisora del momento de cancelación, o del día hábil inmediato anterior si el pago se efectúa un día inhábil. · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "como máximo en este caso el tipo de cambio vendedor (aplicable para operaciones efectuadas por ventanilla o a través de medios electrónicos, según corresponda) de la entidad emisora de la tarjeta del momento de cancelación", "comparacion": "maximo_inclusivo", "base": "en este caso el tipo de cambio vendedor (aplicable para operaciones efectuadas por ventanilla o a través de medios electrónicos", "regla_comparacion": "limite_relativo:compuesta:como_maximo", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['como máximo en este caso el tipo de cambio vendedor (aplicable para operaciones …'] · tramo [exacta]: «debiendo aplicar como máximo en este caso el tipo de cambio vendedor (aplicable para operaciones efectuadas por ventanilla o a través de medios electrónicos, según corresponda) de la entidad emisora de la tarjeta del momento de cancelación –o día hábil inmediato anterior cuando el pago se efectúe un día inhábil–»
- **r2 Restriccion** «Tipo de cambio débito automático — cierre del día del pago» — Si se pactó el débito automático del resumen en cuentas de la propia entidad emisora, se aplica el tipo de cambio vendedor para operaciones por medios electrónicos del cierre del mismo día hábil del pago. · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "aplicará el tipo de cambio vendedor para operaciones efectuadas a través de medios electrónicos de pago del cierre del mismo día hábil del pago", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['aplicará el tipo de cambio vendedor para operaciones efectuadas a través de medi…'] · tramo [exacta]: «En los casos donde los clientes hayan pactado el débito automático del resumen de la tarjeta en cuentas de la propia entidad emisora, aplicará el tipo de cambio vendedor para operaciones efectuadas a través de medios electrónicos de pago del cierre del mismo día hábil del pago.»
- **c2 Condicion** «Débito automático pactado en cuentas de la entidad emisora» — Los clientes pactaron el débito automático del resumen de la tarjeta en cuentas de la propia entidad emisora. · tramo [exacta]: «En los casos donde los clientes hayan pactado el débito automático del resumen de la tarjeta en cuentas de la propia entidad emisora»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ r2 Restriccion
- R: r1 Restriccion —limita→ op1 Operacion
- R: r2 Restriccion —limita→ op1 Operacion
- R: p1 Potestad —aplica_a→ Sujeto (mención «el titular»)
- R: r2 Restriccion —aplica_a→ Sujeto_entidad_financiera (mención «la propia entidad emisora»)
- R: Sujeto (mención «el titular») —ejecuta→ op1 Operacion

### H — supuestos a clasificar

- 1. «emisor entidad financiera» → candidatos: c1 Condicion (1.00), op1 Operacion (1.00), p1 Potestad (1.00), c2 Condicion (0.33)
- 2. «pago en día inhábil» → candidatos: r1 Restriccion (1.00), r2 Restriccion (0.67)
- 3. «débito automático pactado» → candidatos: c2 Condicion (1.00), r2 Restriccion (1.00)

## Código K

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

### K — supuestos a clasificar

- 1. «emisor entidad financiera» → candidatos: e2 Condicion (1.00), e3 Potestad (0.67), e4 Restriccion (0.33), e6 Condicion (0.33)
- 2. «pago en día inhábil» → candidatos: e4 Restriccion (1.00), e5 Condicion (1.00), e7 Obligacion (0.67)
- 3. «débito automático pactado» → candidatos: e6 Condicion (1.00), e7 Obligacion (0.67)

## Código W

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

### W — supuestos a clasificar

- 1. «emisor entidad financiera» → candidatos: c1 Condicion (1.00), op1 Operacion (0.67), p1 Potestad (0.67), c2 Condicion (0.33)
- 2. «pago en día inhábil» → candidatos: r1 Restriccion (1.00), o1 Obligacion (0.67)
- 3. «débito automático pactado» → candidatos: c2 Condicion (1.00), o1 Obligacion (1.00)

