# `ext::9.3.12::intro` — [bloque intro] Utilidades y dividendos en el marco de lo previsto en el punto 7.10.

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.
> *heredado:* 9.3. Certificaciones de aplicación de cobros de exportaciones.
> *heredado:* 9.3.12. Utilidades y dividendos en el marco de lo previsto en el punto 7.10.
> *propio:* La entidad podrá emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes, en la medida que se cumplan la totalidad de las siguientes condiciones:

## Omisiones leídas en T4 (M2)

sin_marca:30 [normativa; heredado] «en el marco de lo previsto en el punto 7.10»

## Código A

- **p1 Potestad** «Emitir certificaciones de aplicación de divisas a utilidades y dividendos» — La entidad podrá emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes, en la medida que se cumplan la totalidad de las condiciones enumeradas a continuación (punto 7.10). · tramo [exacta]: «La entidad podrá emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes»
- **op1 Operacion** «Certificación de aplicación de divisas al pago de utilidades y dividendos a no residentes» — Emisión de certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes, en el marco del punto 7.10. · props: `{"tipo": "certificacion"}` · tramo [exacta]: «emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ op1 Operacion

### A — omisiones de T4 a clasificar

- sin_marca:30 → entidades: — | omisiones: —

## Código H

- **p1 Potestad** «Emitir certificaciones de aplicación de divisas a utilidades y dividendos» — La entidad podrá emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes, en la medida que se cumplan la totalidad de las siguientes condiciones (enumeradas en los ítems del punto). · tramo [exacta]: «La entidad podrá emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes»
- **o1 Operacion** «Certificación de aplicación de divisas al pago de utilidades y dividendos a no residentes» — Emisión de certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes, en el marco del punto 7.10, solo si se cumple la totalidad de las condiciones enumeradas. · props: `{"tipo": "certificacion"}` · tramo [exacta]: «emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ o1 Operacion

### H — omisiones de T4 a clasificar

- sin_marca:30 → entidades: — | omisiones: —

## Código K

- **e1 Operacion** «Certificación de aplicación de divisas a utilidades» — Emisión por la entidad de certificaciones de aplicación de las divisas de cobros de exportaciones al pago de utilidades y dividendos a accionistas no residentes, en el marco del punto 7.10. · props: `{"tipo": "certificación de aplicación de cobros de exportaciones"}` · tramo [exacta]: «emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes»
- **e2 Potestad** «Facultad de certificar aplicación a utilidades y dividendos» — La entidad podrá emitir certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes, siempre que se cumplan la totalidad de las condiciones enumeradas en los ítems siguientes (exigidas en forma concurrente). · tramo [exacta]: «La entidad podrá emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes»
- R: e2 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ e1 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «La entidad podrá emitir las certificaciones» — Vínculo Potestad → Operacion habilitada; ningún predicado lo representa (habilita).

### K — omisiones de T4 a clasificar

- sin_marca:30 → entidades: — | omisiones: —

## Código W

- **e1 Potestad** «Certificación de aplicación a utilidades y dividendos» — La entidad podrá emitir las certificaciones de aplicación de las divisas (de cobros de exportaciones) al pago de utilidades y dividendos a accionistas no residentes, en la medida que se cumplan la totalidad de las condiciones que se enumeran a continuación. · tramo [exacta]: «La entidad podrá emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes»
- **e2 Operacion** «Emisión de certificación de aplicación de divisas a utilidades y dividendos» — Emisión de certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes · props: `{"tipo": "certificación de aplicación de cobros de exportaciones"}` · tramo [exacta]: «emitir las certificaciones de aplicación de las divisas al pago de utilidades y dividendos a accionistas no residentes»
- R: e1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «La entidad») —ejecuta→ e2 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «La entidad podrá emitir las certificaciones» — Vínculo Potestad → Operacion habilitada; ningún predicado lo representa (habilita).

### W — omisiones de T4 a clasificar

- sin_marca:30 → entidades: — | omisiones: —

