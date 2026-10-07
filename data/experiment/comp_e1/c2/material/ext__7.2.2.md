# `ext::7.2.2` — Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación.

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.2. Liquidaciones y otros ingresos imputables al cumplimiento de un permiso de embarque.
> *propio:* 7.2.2. Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación. Cuando los exportadores anticipen fondos desde sus cuentas en el exterior a los fines de dar cumplimiento a la obligación de liquidación de exportaciones realizadas y pendientes de cobro.

## Omisiones leídas en T4 (M2)

sin_marca:15 [no normativa; propio] «7.2.2. Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación.»

## Código A

- **op1 Operacion** «Ingreso de fondos propios de exportadores desde cuentas en el exterior» — Anticipo de fondos propios por los exportadores desde sus cuentas en el exterior, a los fines de dar cumplimiento a la obligación de liquidación de exportaciones realizadas y pendientes de cobro; ingreso imputable al cumplimiento de un permiso de embarque. · props: `{"tipo": "ingreso de fondos"}` · tramo [exacta]: «Cuando los exportadores anticipen fondos desde sus cuentas en el exterior a los fines de dar cumplimiento a la obligación de liquidación de exportaciones realizadas y pendientes de cobro.»
- R: Sujeto_exportador (mención «los exportadores») —ejecuta→ op1 Operacion

### A — omisiones de T4 a clasificar

- sin_marca:15 → entidades: op1 Operacion [exacta] solap 0.5 | omisiones: —

## Código H

- **c1 Condicion** «Exportadores anticipan fondos desde cuentas en el exterior» — Supuesto en que los exportadores anticipan fondos propios desde sus cuentas en el exterior para cumplir la obligación de liquidación de exportaciones realizadas y pendientes de cobro; esos ingresos son imputables al cumplimiento del permiso de embarque (norma del punto 7.2, que esta unidad no extrae). · tramo [exacta]: «Cuando los exportadores anticipen fondos desde sus cuentas en el exterior a los fines de dar cumplimiento a la obligación de liquidación de exportaciones realizadas y pendientes de cobro»

### H — omisiones de T4 a clasificar

- sin_marca:15 → entidades: c1 Condicion [exacta] solap 0.5 | omisiones: —

## Código K

- **op1 Operacion** «Ingreso de fondos propios imputable a permiso de embarque» — Ingreso de fondos propios de los exportadores, desde sus cuentas en el exterior, imputable al cumplimiento de la obligación de liquidación de un permiso de embarque · props: `{"tipo": "ingreso de fondos del exterior imputable al cumplimiento de la obligación de liquidación"}` · tramo [exacta]: «Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación.»
- **c1 Condicion** «Anticipo desde cuentas propias en el exterior» — Que los exportadores anticipen fondos desde sus cuentas en el exterior para cumplir la obligación de liquidación de exportaciones ya realizadas y pendientes de cobro · tramo [exacta]: «Cuando los exportadores anticipen fondos desde sus cuentas en el exterior a los fines de dar cumplimiento a la obligación de liquidación de exportaciones realizadas y pendientes de cobro.»
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: Sujeto_exportador (mención «los exportadores») —ejecuta→ op1 Operacion

### K — omisiones de T4 a clasificar

- sin_marca:15 → entidades: op1 Operacion [exacta] solap 0.75 contenido_en; c1 Condicion [exacta] solap 0.5 | omisiones: —

## Código W

- **e1 Operacion** «Ingreso de fondos propios de exportadores imputable» — Ingreso de fondos propios de los exportadores, desde sus cuentas en el exterior, imputable al cumplimiento de la obligación de liquidación de exportaciones de bienes realizadas y pendientes de cobro (permiso de embarque). · props: `{"tipo": "ingreso de fondos del exterior"}` · tramo [exacta]: «Ingresos de fondos propios de los exportadores para el cumplimiento de la obligación.»
- **e2 Condicion** «Anticipo desde cuentas propias en el exterior» — Supuesto: que los exportadores anticipen fondos desde sus cuentas en el exterior con el fin de cumplir la obligación de liquidación de exportaciones ya realizadas y pendientes de cobro. · tramo [exacta]: «Cuando los exportadores anticipen fondos desde sus cuentas en el exterior a los fines de dar cumplimiento a la obligación de liquidación de exportaciones realizadas y pendientes de cobro.»
- R: e2 Condicion —condicion_de→ e1 Operacion
- R: Sujeto_exportador (mención «los exportadores») —ejecuta→ e1 Operacion

### W — omisiones de T4 a clasificar

- sin_marca:15 → entidades: e1 Operacion [exacta] solap 0.75 contenido_en; e2 Condicion [exacta] solap 0.5 | omisiones: —

