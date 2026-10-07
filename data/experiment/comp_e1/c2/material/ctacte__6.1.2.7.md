# `ctacte::6.1.2.7` — Giro sobre el librador, salvo que se tratara de un cheque girado entre distintos

Grupos: omisiones. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 6. Rechazo de cheques.
> *heredado:* 6.1. Causales.
> *heredado:* 6.1.2. Defectos formales.
> *heredado:* Se define como defecto formal todo aquel verificado en la creación del cheque que el beneficiario no pueda advertir por su mera apariencia. Quedan incluidos, entre otros, los siguientes casos:
> *propio:* 6.1.2.7. Giro sobre el librador, salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador.

## Omisiones leídas en T4 (M2)

sin_marca:11 [normativa; heredado] «Se define como defecto formal todo aquel verificado en la creación del cheque que el beneficiario no pueda advertir por su mera apariencia»

## Código A

- **d1 Definicion** «Defecto formal: giro sobre el librador» — Se incluye entre los defectos formales (verificados en la creación del cheque, que el beneficiario no puede advertir por su mera apariencia) el giro sobre el librador. · props: `{"termino": "defecto formal"}` · tramo [exacta]: «Quedan incluidos, entre otros, los siguientes casos: […] Giro sobre el librador»
- **x1 Excepcion** «Excepción: cheque entre establecimientos del mismo librador» — Queda fuera del defecto formal 'giro sobre el librador' el cheque girado entre distintos establecimientos de un mismo librador. · tramo [exacta]: «salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador»
- Omisión `relacion_sin_predicado` [exacta]: «salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador» — Se habría usado `exceptua`, pero su rango es Restriccion y el caso exceptuado es una Definicion.

### A — omisiones de T4 a clasificar

- sin_marca:11 → entidades: — | omisiones: —

## Código H

- **d1 Definicion** «Defecto formal: giro sobre el librador» — El giro sobre el librador queda incluido entre los defectos formales del cheque (los verificados en su creación que el beneficiario no puede advertir por su mera apariencia), salvo que se trate de un cheque girado entre distintos establecimientos de un mismo librador. · props: `{"termino": "defecto formal"}` · tramo [exacta]: «Se define como defecto formal todo aquel verificado en la creación del cheque que el beneficiario no pueda advertir por su mera apariencia. […] Giro sobre el librador, salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador.»
- **x1 Excepcion** «Excepción cheque entre establecimientos del mismo librador» — Queda afuera del caso de defecto formal 'giro sobre el librador' (inclusión en la clase de defectos formales) el cheque girado entre distintos establecimientos de un mismo librador. · tramo [exacta]: «salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador»

### H — omisiones de T4 a clasificar

- sin_marca:11 → entidades: d1 Definicion [exacta] solap 1.0 contiene | omisiones: —

## Código K

- **d1 Definicion** «Giro sobre el librador — defecto formal» — Entre los casos incluidos como defecto formal (verificado en la creación del cheque y no advertible por el beneficiario por su mera apariencia) está el giro sobre el librador. · props: `{"termino": "defecto formal"}` · tramo [exacta]: «Quedan incluidos, entre otros, los siguientes casos: […] Giro sobre el librador»
- **x1 Excepcion** «Cheque entre establecimientos del mismo librador — no defecto» — El giro sobre el librador no se considera defecto formal (causal de rechazo) cuando se trata de un cheque girado entre distintos establecimientos de un mismo librador. · tramo [exacta]: «salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador»

### K — omisiones de T4 a clasificar

- sin_marca:11 → entidades: — | omisiones: —

## Código W

- **d1 Definicion** «Giro sobre el librador — defecto formal de cheque» — Entre los defectos formales (verificados en la creación del cheque y no advertibles por el beneficiario por su mera apariencia) queda incluido, entre otros, el giro sobre el librador, salvo que se trate de un cheque girado entre distintos establecimientos de un mismo librador. · props: `{"termino": "defecto formal"}` · tramo [exacta]: «Se define como defecto formal todo aquel verificado en la creación del cheque que el beneficiario no pueda advertir por su mera apariencia. Quedan incluidos, entre otros, los siguientes casos: […] Giro sobre el librador»
- **x1 Excepcion** «Cheque entre establecimientos del mismo librador — no defecto» — El giro sobre el librador no constituye defecto formal (causal de rechazo del cheque) cuando se trata de un cheque girado entre distintos establecimientos de un mismo librador. · tramo [exacta]: «salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador»
- Omisión `relacion_sin_predicado` [exacta]: «salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador» — La excepción recorta el alcance de una Definicion; exceptua solo admite Restriccion como rango.

### W — omisiones de T4 a clasificar

- sin_marca:11 → entidades: d1 Definicion [exacta] solap 1.0 contiene | omisiones: —

