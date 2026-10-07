# `ext::10.11.5` — el pago es concretado en el marco de lo dispuesto en el punto 4.8.4. por un cliente

Grupos: omisiones. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.11. Disposiciones complementarias para importaciones de bienes con registro de ingreso
> *heredado:* aduanero hasta el 12/12/23. Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:
> *propio:* 10.11.5. el pago es concretado en el marco de lo dispuesto en el punto 4.8.4. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24; o

## Omisiones leídas en T4 (M2)

con_marca:24 [normativa; heredado] «excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:»

## Código A

- **c1 Condicion** «Pago por cliente con BOPREAL Serie 1 ≥50% (punto 4.8.4)» — Supuesto alternativo (uno de los que la entidad debe verificar, unidos por «o») de la excepción al requisito de conformidad previa del BCRA para el acceso al mercado de cambios para pagos de importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23: el pago es concretado en el marco del punto 4.8.4. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% del… · umbral: ['por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por…'] · tramo [exacta]: «el pago es concretado en el marco de lo dispuesto en el punto 4.8.4. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24»

### A — omisiones de T4 a clasificar

- con_marca:24 → entidades: — | omisiones: —

## Código H

- **ex1 Excepcion** «Excepción conformidad previa — pago BOPREAL Serie 1 (4.8.4)» — Queda exceptuado de la conformidad previa del BCRA para el acceso al mercado de cambios para pagos de importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23 el caso en que la entidad verifique que el pago es concretado en el marco del punto 4.8.4. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% del total pendiente por sus deudas elegibles para los… · tramo [exacta]: «excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que: […] el pago es concretado en el marco de lo dispuesto en el punto 4.8.4. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas elegibles para…»
- **c1 Condicion** «Suscripción BOPREAL Serie 1 ≥50% de deudas elegibles» — El pago se concreta en el marco del punto 4.8.4. por un cliente que suscribió BOPREAL Serie 1, con anterioridad al 31/01/24, por un monto igual o mayor al 50% del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. · umbral: ['por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por…'] · tramo [exacta]: «el pago es concretado en el marco de lo dispuesto en el punto 4.8.4. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24»
- R: c1 Condicion —condicion_de→ ex1 Excepcion
- R: ex1 Excepcion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)

### H — omisiones de T4 a clasificar

- con_marca:24 → entidades: ex1 Excepcion [exacta] solap 1.0 contiene | omisiones: —

## Código K

- **c1 Condicion** «Pago en el marco del punto 4.8.4» — Supuesto de la excepción a la conformidad previa del BCRA para pagar importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23: la entidad verifica que el pago se concreta en el marco del punto 4.8.4. Es un supuesto alternativo («o») a los demás ítems de la lista. · tramo [exacta]: «el pago es concretado en el marco de lo dispuesto en el punto 4.8.4.»
- **c2 Condicion** «Cliente suscriptor BOPREAL Serie 1 ≥50% deudas elegibles» — Supuesto de la misma excepción a la conformidad previa del BCRA: el pago lo hace un cliente que suscribió BOPREAL Serie 1 antes del 31/01/24 por un monto igual o mayor al 50% del total pendiente de sus deudas elegibles para los puntos 4.4. y 4.5. · umbral: ['por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por…'] · tramo [exacta]: «por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24»

### K — omisiones de T4 a clasificar

- con_marca:24 → entidades: — | omisiones: —

## Código W

- **c1 Condicion** «Pago en el marco del punto 4.8.4» — Supuesto (alternativo a los demás ítems) de la excepción a la conformidad previa del BCRA para acceder al mercado de cambios a pagar importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23: que la entidad verifique que el pago se concreta en el marco del punto 4.8.4. · tramo [exacta]: «el pago es concretado en el marco de lo dispuesto en el punto 4.8.4.»
- **c2 Condicion** «Cliente suscribió BOPREAL Serie 1 ≥50% deudas elegibles» — Supuesto de la misma excepción a la conformidad previa del BCRA: que el pago lo concrete un cliente que, con anterioridad al 31/01/24, suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% del total pendiente de sus deudas elegibles para los puntos 4.4. y 4.5. · umbral: ['por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por…'] · tramo [exacta]: «por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24»

### W — omisiones de T4 a clasificar

- con_marca:24 → entidades: — | omisiones: —

