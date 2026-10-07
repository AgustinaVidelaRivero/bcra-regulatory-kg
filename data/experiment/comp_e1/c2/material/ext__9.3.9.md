# `ext::9.3.9` — Títulos de deuda con registro público en el país denominados en moneda extranjera

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.
> *heredado:* 9.3. Certificaciones de aplicación de cobros de exportaciones.
> *heredado:* A solicitud del exportador, la entidad encargada del seguimiento emitirá las certificaciones de aplicación en la medida que se verifiquen las condiciones previstas en los puntos 9.3.1. al 9.3.13. La entidad deberá dejar registradas las certificaciones de aplicación emitidas para cada una de las operaciones bajo su seguimiento.
> *propio:* 9.3.9. Títulos de deuda con registro público en el país denominados en moneda extranjera admitidos en el punto 7.9. La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación a partir del vencimiento del capital, intereses y otros conceptos admitidos, en la medida que verifique las condiciones indicadas en el punto 9.3.1., constate que la cancelación tuvo lugar a partir de la fecha de vencimiento y cuente con la documentación que verifican el cumplimiento de los requisitos establecidos en el punto 7.9.

## Omisiones leídas en T4 (M2)

sin_marca:19 [normativa; propio] «admitidos en el punto 7.9»

## Código A

- **p1 Potestad** «Emitir certificaciones de aplicación — títulos de deuda en ME» — La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación, a partir del vencimiento del capital, intereses y otros conceptos admitidos, de títulos de deuda con registro público en el país denominados en moneda extranjera admitidos en el punto 7.9. · tramo [exacta]: «La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación a partir del vencimiento del capital, intereses y otros conceptos admitidos»
- **op1 Operacion** «Certificación de aplicación — títulos de deuda con registro público en ME» — Emisión de certificaciones de aplicación de las divisas a la cancelación de capital, intereses y otros conceptos admitidos de títulos de deuda con registro público en el país denominados en moneda extranjera admitidos en el punto 7.9, a partir del vencimiento. · props: `{"tipo": "certificacion_de_aplicacion"}` · tramo [exacta]: «emitir las certificaciones de aplicación de las divisas a la cancelación»
- **c1 Condicion** «Condiciones del punto 9.3.1 verificadas» — La entidad verifica las condiciones indicadas en el punto 9.3.1. · tramo [exacta]: «en la medida que verifique las condiciones indicadas en el punto 9.3.1.»
- **c2 Condicion** «Cancelación constatada desde fecha de vencimiento» — La entidad constata que la cancelación tuvo lugar a partir de la fecha de vencimiento. · tramo [exacta]: «constate que la cancelación tuvo lugar a partir de la fecha de vencimiento»
- **c3 Condicion** «Documentación del cumplimiento del punto 7.9» — La entidad cuenta con la documentación que verifica el cumplimiento de los requisitos establecidos en el punto 7.9. · tramo [exacta]: «cuente con la documentación que verifican el cumplimiento de los requisitos establecidos en el punto 7.9»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad

### A — omisiones de T4 a clasificar

- sin_marca:19 → entidades: c3 Condicion [exacta] solap 0.75; c1 Condicion [exacta] solap 0.5 | omisiones: —

## Código H

- **p1 Potestad** «Emitir certificaciones de aplicación — títulos de deuda» — La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación de títulos de deuda con registro público en el país denominados en moneda extranjera admitidos en el punto 7.9, a partir del vencimiento del capital, intereses y otros conceptos admitidos. · tramo [exacta]: «La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación a partir del vencimiento del capital, intereses y otros conceptos admitidos»
- **o1 Operacion** «Emisión de certificaciones de aplicación — títulos de deuda en moneda extranjera» — Emisión de certificaciones de aplicación de las divisas a la cancelación (capital, intereses y otros conceptos admitidos) de títulos de deuda con registro público en el país denominados en moneda extranjera admitidos en el punto 7.9. · props: `{"tipo": "otra"}` · tramo [exacta]: «emitir las certificaciones de aplicación de las divisas a la cancelación a partir del vencimiento del capital, intereses y otros conceptos admitidos»
- **c1 Condicion** «Verificación condiciones del punto 9.3.1» — Que la entidad verifique las condiciones indicadas en el punto 9.3.1. · tramo [exacta]: «en la medida que verifique las condiciones indicadas en el punto 9.3.1.»
- **c2 Condicion** «Cancelación desde la fecha de vencimiento» — Que la entidad constate que la cancelación tuvo lugar a partir de la fecha de vencimiento. · tramo [exacta]: «constate que la cancelación tuvo lugar a partir de la fecha de vencimiento»
- **c3 Condicion** «Documentación de requisitos del punto 7.9» — Que la entidad cuente con la documentación que verifica el cumplimiento de los requisitos establecidos en el punto 7.9. · tramo [exacta]: «cuente con la documentación que verifican el cumplimiento de los requisitos establecidos en el punto 7.9.»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad

### H — omisiones de T4 a clasificar

- sin_marca:19 → entidades: c3 Condicion [exacta] solap 0.75; c1 Condicion [exacta] solap 0.5 | omisiones: —

## Código K

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

### K — omisiones de T4 a clasificar

- sin_marca:19 → entidades: c3 Condicion [exacta] solap 0.75; c1 Condicion [exacta] solap 0.5 | omisiones: —

## Código W

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

### W — omisiones de T4 a clasificar

- sin_marca:19 → entidades: c3 Condicion [exacta] solap 0.75; c1 Condicion [exacta] solap 0.5 | omisiones: —

