# `ext::3.9::intro` — [bloque intro] Compra de moneda extranjera por parte de personas humanas residentes para la formación

Grupos: omisiones. Estado final en la tanda 0: `cola_humana`.

## Texto

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* 3.9. Compra de moneda extranjera por parte de personas humanas residentes para la formación
> *propio:* de activos externos bajo otras modalidades, la remisión de ayuda familiar u operaciones con derivados. Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de concepto A05) en la medida que no encuadre en el punto 3.12.1., sin la conformidad previa del BCRA, en la medida que se cumplan la totalidad de los siguientes requisitos:

## Omisiones leídas en T4 (M2)

con_marca:18 [no normativa; propio] «de activos externos bajo otras modalidades, la remisión de ayuda familiar u operaciones con derivados.»

## Código A

- **op1 Operacion** «Acceso al mercado de cambios para formación de activos externos y otros conceptos» — Acceso al mercado de cambios de personas humanas residentes para la formación de activos externos (códigos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y la operatoria con derivados (código A05), en la medida que no encuadre en el punto 3.12.1. · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de concepto A05)»
- **p1 Potestad** «Dar acceso al mercado de cambios sin conformidad previa del BCRA» — Las entidades pueden dar acceso al mercado de cambios a personas humanas residentes para la formación de activos externos, la remisión de ayuda familiar y la operatoria con derivados (código A05), en la medida que no encuadre en el punto 3.12.1., sin la conformidad previa del BCRA. · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de concepto A05) en la medida que no encuadre en el punto…»
- **c1 Condicion** «Cumplimiento de la totalidad de los requisitos siguientes» — Se exige el cumplimiento conjunto de la totalidad de los requisitos enumerados en los ítems siguientes para dar acceso sin conformidad previa del BCRA. · tramo [exacta]: «en la medida que se cumplan la totalidad de los siguientes requisitos»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)
- Omisión `relacion_sin_predicado` [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos» — Potestad → Operacion: se habría usado un predicado de habilitación sobre el acto; no existe en los 13 predicados.

### A — omisiones de T4 a clasificar

- con_marca:18 → entidades: op1 Operacion [exacta] solap 0.6; p1 Potestad [exacta] solap 0.6 | omisiones: —

## Código H

- **op1 Operacion** «Acceso al mercado de cambios — personas humanas residentes» — Dar acceso al mercado de cambios a personas humanas residentes para la formación de activos externos (conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y la operatoria con derivados (concepto A05) en la medida que no encuadre en el punto 3.12.1. · props: `{"tipo": "compra de moneda extranjera / acceso al mercado de cambios"}` · tramo [no]: «dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de con-cepto A05)»
- **pot1 Potestad** «Acceso sin conformidad previa del BCRA» — Las entidades podrán dar acceso al mercado de cambios a personas humanas residentes para formación de activos externos, remisión de ayuda familiar y operatoria con derivados, sin la conformidad previa del BCRA, en la medida que se cumplan la totalidad de los requisitos siguientes y no encuadre en el punto 3.12.1. · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes»
- **cond1 Condicion** «Cumplimiento de la totalidad de los requisitos» — Se deben cumplir la totalidad de los requisitos enumerados a continuación para acceder al mercado de cambios sin conformidad previa del BCRA. · tramo [exacta]: «en la medida que se cumplan la totalidad de los siguientes requisitos»
- R: pot1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)
- R: cond1 Condicion —condicion_de→ pot1 Potestad

### H — omisiones de T4 a clasificar

- con_marca:18 → entidades: op1 Operacion [no] solap 0.6 | omisiones: —

## Código K

- **p1 Potestad** «Acceso sin conformidad previa BCRA — personas humanas residentes» — Las entidades podrán dar acceso al mercado de cambios, sin la conformidad previa del BCRA, a las personas humanas residentes para la formación de activos externos (códigos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y la operatoria con derivados (código A05) en la medida que no encuadre en el punto 3.12.1., siempre que se cumplan la totalidad de los requisitos enumerado… · no definidas: `{"cuantificador_requisitos": "la totalidad de los siguientes requisitos"}` · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes»
- **o1 Operacion** «Formación de activos externos — personas humanas residentes» — Acceso al mercado de cambios de personas humanas residentes para formación de activos externos, códigos A01, A02, A03, A04, A06, A08, A14 y A24 · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24)»
- **o2 Operacion** «Remisión de ayuda familiar — personas humanas residentes» — Acceso al mercado de cambios de personas humanas residentes para la remisión de ayuda familiar · props: `{"tipo": "transferencia al exterior"}` · tramo [exacta]: «la remisión de ayuda familiar»
- **o3 Operacion** «Operatoria con derivados A05 — personas humanas residentes» — Acceso al mercado de cambios de personas humanas residentes para operatoria con derivados (código A05) que no encuadre en el punto 3.12.1. · props: `{"tipo": "operación con derivados"}` · tramo [exacta]: «para la operatoria con derivados (código de concepto A05) en la medida que no encuadre en el punto 3.12.1.»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)
- R: Sujeto_persona_humana (mención «personas humanas residentes») —ejecuta→ o1 Operacion
- R: Sujeto_persona_humana (mención «personas humanas residentes») —ejecuta→ o2 Operacion
- R: Sujeto_persona_humana (mención «personas humanas residentes») —ejecuta→ o3 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes» — Potestad → Operacion (habilita el acceso para formación de activos externos, ayuda familiar y derivados: o1, o2, o3); no hay predicado Potestad→Operacion

### K — omisiones de T4 a clasificar

- con_marca:18 → entidades: o2 Operacion [exacta] solap 0.3 contenido_en | omisiones: —

## Código N

- **e1 Potestad** «Acceso al mercado de cambios — formación de activos externos» — Las entidades están facultadas a dar acceso al mercado de cambios a personas humanas residentes para la formación de activos externos bajo los códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24, la remisión de ayuda familiar y la operatoria con derivados (código A05), siempre que no encuadre en el punto 3.12.1 y se cumplan los requisitos que siguen. · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de concepto A05)»
- **e2 Condicion** «Cumplimiento de totalidad de requisitos» — La facultad de dar acceso al mercado de cambios se condiciona al cumplimiento de la totalidad de los requisitos que siguen. · tramo [exacta]: «en la medida que se cumplan la totalidad de los siguientes requisitos»
- **e3 Condicion** «No encuadre en punto 3.12.1» — La operatoria no debe encuadrar en lo dispuesto en el punto 3.12.1. · tramo [exacta]: «en la medida que no encuadre en el punto 3.12.1.»
- R: e2 Condicion —condicion_de→ e1 Potestad
- R: e3 Condicion —condicion_de→ e1 Potestad
- R: e1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)
- Omisión `meta_normativo` [exacta]: «de activos externos bajo otras modalidades, la remisión de ayuda familiar u operaciones con derivados.» — Enumeración introductoria que contextualiza pero no prescribe conducta normativa propia

### N — omisiones de T4 a clasificar

- con_marca:18 → entidades: e1 Potestad [exacta] solap 0.6 | omisiones: om#0 meta_normativo [exacta] solap 1.0 contiene

## Código W

- **p1 Potestad** «Acceso sin conformidad BCRA — personas humanas residentes» — Las entidades pueden dar acceso al mercado de cambios a personas humanas residentes para formación de activos externos (A01, A02, A03, A04, A06, A08, A14 y A24), remisión de ayuda familiar y operatoria con derivados (A05) que no encuadre en el punto 3.12.1., sin la conformidad previa del BCRA, en la medida que se cumplan la totalidad de los requisitos que se enumeran a continuación. · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes»
- **o1 Operacion** «Formación de activos externos — personas humanas residentes» — Acceso al mercado de cambios de personas humanas residentes para formación de activos externos, códigos A01, A02, A03, A04, A06, A08, A14 y A24 · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24)»
- **o2 Operacion** «Remisión de ayuda familiar — personas humanas residentes» — Acceso al mercado de cambios de personas humanas residentes para la remisión de ayuda familiar · props: `{"tipo": "compra de moneda extranjera"}` · tramo [exacta]: «la remisión de ayuda familiar»
- **o3 Operacion** «Operatoria con derivados A05 — personas humanas residentes» — Acceso al mercado de cambios de personas humanas residentes para operatoria con derivados, código A05 · props: `{"tipo": "operación con derivados"}` · tramo [exacta]: «para la operatoria con derivados (código de concepto A05)»
- **c1 Condicion** «Derivados no encuadrados en punto 3.12.1.» — La operatoria con derivados no debe encuadrar en el punto 3.12.1. para acceder sin conformidad previa. · tramo [exacta]: «en la medida que no encuadre en el punto 3.12.1.»
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)
- R: Sujeto_persona_humana (mención «las personas humanas residentes») —ejecuta→ o1 Operacion
- R: Sujeto_persona_humana (mención «las personas humanas residentes») —ejecuta→ o2 Operacion
- R: Sujeto_persona_humana (mención «las personas humanas residentes») —ejecuta→ o3 Operacion
- R: c1 Condicion —condicion_de→ p1 Potestad
- Omisión `relacion_sin_predicado` [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos» — Potestad→Operacion (habilita); sin predicado. Ídem hacia o2 y o3.

### W — omisiones de T4 a clasificar

- con_marca:18 → entidades: o2 Operacion [exacta] solap 0.3 contenido_en | omisiones: —

