# `ctacte::2.3.5::intro` — [bloque intro] Publicidad.

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 2. Movimiento de las cuentas.
> *heredado:* 2.3. Intereses.
> *heredado:* 2.3.5. Publicidad.
> *propio:* Los bancos deberán exponer en pizarras colocadas en los locales de atención al público como en las publicidades realizadas a través de medios gráficos (periódicos, revistas, carteleras en la vía pública, etc.) información sobre las tasas de interés que abonen sobre los saldos acreedores de las cuentas corrientes –cuando se reconozcan–, en tanto por ciento con dos decimales, con el siguiente detalle:

## Omisiones leídas en T4 (M2)

sin_marca:17 [no normativa; propio] «con el siguiente detalle:»

## Código A

- **o1 Operacion** «Exposición de tasas de interés sobre saldos acreedores» — Exposición, en pizarras de los locales de atención al público y en publicidades por medios gráficos (periódicos, revistas, carteleras en la vía pública, etc.), de información sobre las tasas de interés que se abonan sobre los saldos acreedores de las cuentas corrientes, cuando se reconozcan. · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «exponer en pizarras colocadas en los locales de atención al público como en las publicidades realizadas a través de medios gráficos (periódicos, revistas, carteleras en la vía pública, etc.) información sobre las tasas de interés que abonen sobre los saldos acreedores de las cuentas corrientes –cuando se reconozcan–»
- **ob1 Obligacion** «Exponer tasas de interés en pizarras y publicidad gráfica» — Los bancos deben exponer en pizarras de los locales de atención al público y en las publicidades por medios gráficos información sobre las tasas de interés que abonen sobre los saldos acreedores de las cuentas corrientes (cuando se reconozcan), en tanto por ciento con dos decimales, con el detalle que siguen los ítems del punto. · props: `{"tipo": "otra"}` · tramo [exacta]: «Los bancos deberán exponer en pizarras colocadas en los locales de atención al público como en las publicidades realizadas a través de medios gráficos (periódicos, revistas, carteleras en la vía pública, etc.) información sobre las tasas de interés que abonen sobre los saldos acreedores de las cuentas corrientes –cuand…»
- R: ob1 Obligacion —regula→ o1 Operacion
- R: ob1 Obligacion —aplica_a→ Sujeto_banco (mención «Los bancos»)

### A — omisiones de T4 a clasificar

- sin_marca:17 → entidades: ob1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código H

- **o1 Obligacion** «Exponer tasas de interés sobre saldos acreedores» — Los bancos deben exponer, en pizarras en los locales de atención al público y en las publicidades realizadas en medios gráficos (periódicos, revistas, carteleras en la vía pública, etc.), información sobre las tasas de interés que abonen sobre los saldos acreedores de las cuentas corrientes (cuando se reconozcan), en tanto por ciento con dos decimales, con el detalle que sigue. · props: `{"tipo": "otra"}` · tramo [exacta]: «Los bancos deberán exponer en pizarras colocadas en los locales de atención al público como en las publicidades realizadas a través de medios gráficos (periódicos, revistas, carteleras en la vía pública, etc.) información sobre las tasas de interés que abonen sobre los saldos acreedores de las cuentas corrientes»
- **c1 Condicion** «Reconocimiento de intereses sobre saldos acreedores» — La exposición de tasas solo rige cuando se reconozcan intereses sobre los saldos acreedores de las cuentas corrientes. · tramo [exacta]: «–cuando se reconozcan–»
- R: c1 Condicion —condicion_de→ o1 Obligacion
- R: o1 Obligacion —aplica_a→ Sujeto_banco (mención «Los bancos»)

### H — omisiones de T4 a clasificar

- sin_marca:17 → entidades: — | omisiones: —

## Código K


### K — omisiones de T4 a clasificar

- sin_marca:17 → entidades: — | omisiones: —

## Código W


### W — omisiones de T4 a clasificar

- sin_marca:17 → entidades: — | omisiones: —

