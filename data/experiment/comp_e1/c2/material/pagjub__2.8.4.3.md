# `pagjub::2.8.4.3` — Debitar de la cuenta corriente de la entidad participante el importe de las órdenes

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 2. Rendición de cuentas por parte de las entidades financieras.
> *heredado:* 2.8. Liquidación de la rendición de cuentas.
> *heredado:* El procesamiento de la información de la rendición de cuentas dará lugar a diferentes movimientos de fondos los que, según los casos correspondientes, se describen a continuación:
> *heredado:* 2.8.4. Presentación aceptada durante el período de presentación tardía con inconsistencias.
> *heredado:* El BCRA, en el mismo día de la aceptación, procederá a:
> *propio:* 2.8.4.3. Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditando el mismo en una cuenta transitoria del BCRA, hasta la fecha límite.

## Omisiones leídas en T4 (M2)

sin_marca:14 [no normativa; heredado] «El procesamiento de la información de la rendición de cuentas dará lugar a diferentes movimientos de fondos los que, según los casos correspondientes, se describen a continuación»

## Código A

- **op1 Operacion** «Débito en cuenta corriente de órdenes de pago abonadas e impagas con inconsistencias» — Débito, de la cuenta corriente de la entidad participante, del importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditándolo en una cuenta transitoria del BCRA, hasta la fecha límite; en presentación aceptada durante el período de presentación tardía con inconsistencias. · props: `{"tipo": "debito en cuenta corriente"}` · tramo [exacta]: «Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditando el mismo en una cuenta transitoria del BCRA, hasta la fecha límite.»
- **ob1 Obligacion** «BCRA debita órdenes de pago impagas con inconsistencias el día de la aceptación» — El BCRA, en el mismo día de la aceptación de la presentación tardía con inconsistencias, debe debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditándolo en una cuenta transitoria del BCRA, hasta la fecha límite. · props: `{"tipo": "otra"}` · tramo [exacta]: «El BCRA, en el mismo día de la aceptación, procederá a: […] Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditando el mismo en una cuenta transitoria del BCRA, hasta la fecha límite.»
- R: ob1 Obligacion —aplica_a→ Sujeto_bcra (mención «El BCRA»)
- R: ob1 Obligacion —regula→ op1 Operacion

### A — omisiones de T4 a clasificar

- sin_marca:14 → entidades: — | omisiones: —

## Código H

- **o1 Operacion** «Débito en cuenta corriente de órdenes de pago impagas con inconsistencias» — Débito de la cuenta corriente de la entidad participante del importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditándolo en una cuenta transitoria del BCRA hasta la fecha límite · props: `{"tipo": "debito en cuenta corriente"}` · tramo [exacta]: «Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias»
- **ob1 Obligacion** «BCRA debita órdenes con inconsistencias el mismo día» — El BCRA, en el mismo día de la aceptación de la presentación tardía con inconsistencias, debe debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditándolo en una cuenta transitoria del BCRA, hasta la fecha límite · props: `{"tipo": "otra"}` · tramo [exacta]: «El BCRA, en el mismo día de la aceptación, procederá a: […] Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditando el mismo en una cuenta transitoria del BCRA, hasta la fecha límite.»
- R: ob1 Obligacion —aplica_a→ Sujeto_bcra (mención «El BCRA»)
- R: Sujeto_bcra (mención «El BCRA») —ejecuta→ o1 Operacion
- R: ob1 Obligacion —regula→ o1 Operacion

### H — omisiones de T4 a clasificar

- sin_marca:14 → entidades: — | omisiones: —

## Código K

- **e1 Obligacion** «Débito órdenes con inconsistencias — presentación tardía» — Ante una presentación aceptada durante el período de presentación tardía con inconsistencias, el BCRA, en el mismo día de la aceptación, debe debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditándolo en una cuenta transitoria del BCRA hasta la fecha límite. · props: `{"tipo": "otra"}` · tramo [exacta]: «El BCRA, en el mismo día de la aceptación, procederá a: […] Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditando el mismo en una cuenta transitoria del BCRA, hasta la fecha límite.»
- **e2 Operacion** «Débito en cuenta corriente de entidad participante» — Débito por el BCRA en la cuenta corriente de la entidad participante del importe de órdenes de pago abonadas e impagas con inconsistencias, con acreditación en cuenta transitoria del BCRA hasta la fecha límite. · props: `{"tipo": "débito en cuenta corriente"}` · tramo [exacta]: «Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias»
- R: e1 Obligacion —regula→ e2 Operacion
- R: e1 Obligacion —aplica_a→ Sujeto_bcra (mención «El BCRA»)
- R: Sujeto_bcra (mención «El BCRA») —ejecuta→ e2 Operacion
- R: e2 Operacion —aplica_a→ Sujeto_rol_alcance_pagjub (mención «la entidad participante»)

### K — omisiones de T4 a clasificar

- sin_marca:14 → entidades: — | omisiones: —

## Código W

- **e1 Obligacion** «Débito de órdenes con inconsistencias a transitoria» — En presentación aceptada durante el período de presentación tardía con inconsistencias, el BCRA, en el mismo día de la aceptación, debe debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditándolo en una cuenta transitoria del BCRA hasta la fecha límite. · props: `{"tipo": "otra"}` · tramo [exacta]: «El BCRA, en el mismo día de la aceptación, procederá a: […] Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias, acreditando el mismo en una cuenta transitoria del BCRA, hasta la fecha límite.»
- **e2 Operacion** «Débito en cuenta corriente de entidad participante» — Débito del importe de órdenes de pago abonadas e impagas con inconsistencias en la cuenta corriente de la entidad participante y acreditación en cuenta transitoria del BCRA hasta la fecha límite · props: `{"tipo": "debito en cuenta corriente"}` · tramo [exacta]: «Debitar de la cuenta corriente de la entidad participante el importe de las órdenes de pago abonadas e impagas que presenten inconsistencias»
- R: e1 Obligacion —aplica_a→ Sujeto_bcra (mención «El BCRA»)
- R: e1 Obligacion —regula→ e2 Operacion
- R: Sujeto_bcra (mención «El BCRA») —ejecuta→ e2 Operacion

### W — omisiones de T4 a clasificar

- sin_marca:14 → entidades: — | omisiones: —

