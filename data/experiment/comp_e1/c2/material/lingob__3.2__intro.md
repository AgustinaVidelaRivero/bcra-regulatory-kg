# `lingob::3.2::intro` — [bloque intro] Decisiones gerenciales.

Grupos: omisiones. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 3. Alta Gerencia.
> *heredado:* 3.2. Decisiones gerenciales.
> *propio:* Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona. Es recomendable que la Alta Gerencia:

## Omisiones leídas en T4 (M2)

con_marca:14 [normativa; propio] «en orden a las buenas prácticas»

## Código A

- **o1 Obligacion** «Decisiones gerenciales por más de una persona» — Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona. · props: `{"tipo": "otra"}` · tramo [exacta]: «Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona.»

### A — omisiones de T4 a clasificar

- con_marca:14 → entidades: o1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código H

- **o1 Obligacion** «Decisiones gerenciales adoptadas por más de una persona» — Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona. · props: `{"tipo": "otra"}` · tramo [exacta]: «Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona.»

### H — omisiones de T4 a clasificar

- con_marca:14 → entidades: o1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código K

- **op1 Operacion** «Adopción de principales decisiones gerenciales» — Adopción de las principales decisiones gerenciales de la entidad · props: `{"tipo": "decision gerencial"}` · tramo [exacta]: «Las principales decisiones gerenciales»
- **ob1 Obligacion** «Decisiones colegiadas — principales decisiones gerenciales» — Recomendación (buena práctica, no deber): las principales decisiones gerenciales serán adoptadas por más de una persona. · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "en orden a las buenas prácticas", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona.»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob1 Obligacion —aplica_a→ Sujeto_alta_gerencia (mención «Alta Gerencia»)

### K — omisiones de T4 a clasificar

- con_marca:14 → entidades: ob1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código W

- **e1 Operacion** «Adopción de principales decisiones gerenciales» — Adopción de las principales decisiones gerenciales de la entidad · props: `{"tipo": "decisión gerencial"}` · tramo [exacta]: «Las principales decisiones gerenciales»
- **e2 Obligacion** «Más de una persona — decisiones gerenciales principales» — Recomendación de buena práctica, no un deber: las principales decisiones gerenciales serán adoptadas por más de una persona. · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "en orden a las buenas prácticas", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona.»
- R: e2 Obligacion —regula→ e1 Operacion
- R: e2 Obligacion —aplica_a→ Sujeto_alta_gerencia (mención «Alta Gerencia»)

### W — omisiones de T4 a clasificar

- con_marca:14 → entidades: e2 Obligacion [exacta] solap 1.0 contiene | omisiones: —

