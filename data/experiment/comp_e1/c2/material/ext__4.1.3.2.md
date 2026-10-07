# `ext::4.1.3.2` — Cuando se trate de empresas no financieras emisoras de tarjetas de crédito

Grupos: grupo_c. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 4. Otras disposiciones específicas.
> *heredado:* 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tarjetas de
> *heredado:* crédito, compra y prepagas emitidas en el país.
> *heredado:* 4.1.3. Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o
> *heredado:* de compra.
> *propio:* 4.1.3.2. Cuando se trate de empresas no financieras emisoras de tarjetas de crédito y/o compra, el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos –siendo aplicable el tipo de cambio vendedor por canales electrónicos publicado por el Banco de la Nación Argentina el mismo día hábil de la fecha de pago o hábil inmediato anterior cuando el pago se efectúe un día inhábil–.

## Supuestos de la fase A de T4 (M1)

1. «emisoras no financieras»
2. «pago en día inhábil»

## Código A

- **op1 Operacion** «Cancelación de consumos en moneda extranjera con tarjeta (empresas no financieras emisoras)» — Cancelación por el titular de los consumos realizados en moneda extranjera con tarjetas de crédito y/o compra emitidas por empresas no financieras, en moneda extranjera o en pesos; en pesos se aplica el tipo de cambio vendedor por canales electrónicos publicado por el Banco de la Nación Argentina el mismo día hábil de la fecha de pago, o el hábil inmediato anterior cuando el pago se efectúe un día… · props: `{"tipo": "cancelacion_consumos_tarjeta"}` · tramo [exacta]: «cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- **p1 Potestad** «Titular puede cancelar en moneda extranjera o en pesos» — Cuando se trate de empresas no financieras emisoras de tarjetas de crédito y/o compra, el titular puede cancelar los consumos en moneda extranjera en esa moneda o en pesos, aplicándose en este caso el tipo de cambio vendedor por canales electrónicos del Banco de la Nación Argentina del día hábil de la fecha de pago (o hábil inmediato anterior si el pago es en día inhábil). · tramo [exacta]: «Cuando se trate de empresas no financieras emisoras de tarjetas de crédito y/o compra, el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- R: p1 Potestad —aplica_a→ Sujeto (mención «el titular»)
- R: Sujeto (mención «el titular») —ejecuta→ op1 Operacion

### A — supuestos a clasificar

- 1. «emisoras no financieras» → candidatos: op1 Operacion (1.00), p1 Potestad (1.00)
- 2. «pago en día inhábil» → candidatos: op1 Operacion (1.00), p1 Potestad (1.00)

## Código H

- **op1 Operacion** «Cancelación de consumos en moneda extranjera con tarjeta» — Cancelación por el titular de consumos en moneda extranjera realizados con tarjetas de crédito y/o compra de empresas no financieras emisoras, en moneda extranjera o en pesos; en pesos rige el tipo de cambio vendedor por canales electrónicos del BNA del día hábil de la fecha de pago (o hábil inmediato anterior si el pago es en día inhábil). · props: `{"tipo": "cancelacion_de_consumos"}` · tramo [exacta]: «cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- **p1 Potestad** «Titular puede cancelar en moneda extranjera o pesos» — Cuando se trate de empresas no financieras emisoras de tarjetas de crédito y/o compra, el titular puede cancelar los consumos realizados en moneda extranjera en esa moneda o en pesos, aplicándose en este caso el tipo de cambio vendedor por canales electrónicos publicado por el BNA el mismo día hábil de la fecha de pago o hábil inmediato anterior cuando el pago se efectúe un día inhábil. · tramo [exacta]: «el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- R: p1 Potestad —aplica_a→ Sujeto (mención «el titular»)
- R: op1 Operacion —aplica_a→ Sujeto_empresa_no_financiera_emisora_de_tarjetas (mención «empresas no financieras emisoras de tarjetas de crédito y/o compra»)

### H — supuestos a clasificar

- 1. «emisoras no financieras» → candidatos: op1 Operacion (1.00), p1 Potestad (1.00)
- 2. «pago en día inhábil» → candidatos: op1 Operacion (1.00), p1 Potestad (1.00)

## Código K

- **e1 Operacion** «Cancelación de consumos en moneda extranjera con tarjeta» — Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o de compra · props: `{"tipo": "cancelacion de consumos con tarjeta"}` · tramo [exacta]: «Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o»
- **e2 Potestad** «Cancelación en moneda extranjera o pesos — tarjetas de empresas no financieras» — Si la tarjeta de crédito y/o compra la emite una empresa no financiera, el titular puede cancelar los consumos en moneda extranjera en esa moneda o en pesos. En pesos se aplica el tipo de cambio vendedor por canales electrónicos que publica el Banco de la Nación Argentina el mismo día hábil de la fecha de pago, o el del día hábil inmediato anterior si el pago se hace un día inhábil. · tramo [exacta]: «el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- **e3 Condicion** «Emisor es empresa no financiera de tarjetas» — Supuesto: la emisora de la tarjeta de crédito y/o compra es una empresa no financiera. · tramo [exacta]: «Cuando se trate de empresas no financieras emisoras de tarjetas de crédito y/o compra»
- R: e3 Condicion —condicion_de→ e2 Potestad
- R: e2 Potestad —aplica_a→ Sujeto (mención «el titular»)
- Omisión `relacion_sin_predicado` [exacta]: «el titular podrá cancelar los consumos realizados en moneda extranjera» — Potestad → Operacion (habilita la operación); no hay predicado para unirlas.

### K — supuestos a clasificar

- 1. «emisoras no financieras» → candidatos: e3 Condicion (1.00), e2 Potestad (0.50)
- 2. «pago en día inhábil» → candidatos: e2 Potestad (1.00)

## Código W

- **e1 Operacion** «Cancelación de consumos en moneda extranjera con tarjeta» — Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o de compra · props: `{"tipo": "cancelación de consumos con tarjeta"}` · tramo [exacta]: «Cancelación de consumos en moneda extranjera efectuados con tarjeta de crédito y/o»
- **e2 Potestad** «Cancelación en moneda extranjera o pesos — tarjetas de emisoras no financieras» — Cuando la tarjeta es de una empresa no financiera emisora de tarjetas de crédito y/o compra, el titular puede cancelar los consumos en moneda extranjera en esa moneda o en pesos; en pesos rige el tipo de cambio vendedor por canales electrónicos publicado por el Banco de la Nación Argentina el mismo día hábil de la fecha de pago, o el hábil inmediato anterior si el pago se hace un día inhábil. · no definidas: `{"tipo_de_cambio_aplicable": "tipo de cambio vendedor por canales electrónicos publicado por el Banco de la Nación Argentina el mismo día hábil de la fecha de pago o hábil inmediato anterior cuando el` · tramo [exacta]: «el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pesos»
- **e3 Condicion** «Tarjeta emitida por empresa no financiera» — Supuesto: la emisora de la tarjeta es una empresa no financiera emisora de tarjetas de crédito y/o compra. · tramo [exacta]: «Cuando se trate de empresas no financieras emisoras de tarjetas de crédito y/o compra»
- R: e3 Condicion —condicion_de→ e2 Potestad
- R: e2 Potestad —aplica_a→ Sujeto (mención «el titular»)
- R: Sujeto (mención «el titular») —ejecuta→ e1 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «el titular podrá cancelar los consumos realizados en moneda extranjera» — Potestad que habilita la operación de cancelación; no hay predicado Potestad→Operacion

### W — supuestos a clasificar

- 1. «emisoras no financieras» → candidatos: e2 Potestad (1.00), e3 Condicion (1.00)
- 2. «pago en día inhábil» → candidatos: e2 Potestad (1.00)

