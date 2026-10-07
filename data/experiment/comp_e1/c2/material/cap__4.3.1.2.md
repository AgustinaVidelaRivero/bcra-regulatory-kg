# `cap::4.3.1.2` — Miembro compensador ("clearing member"): es un miembro –participante

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 4. Capital mínimo por riesgo de crédito de contraparte.
> *heredado:* 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con entidades de
> *heredado:* contraparte central. Comprende a aquellas exposiciones de las entidades financieras con entidades de contraparte central (CCP) que se originen en derivados OTC o negociados en mercados de valores y en operaciones de financiación con títulos valores ("Securities Financing Transactions", SFT) y operaciones de liquidación diferida –definidas en el punto 4.2.–. No están comprendidas las exposiciones originadas en operaciones al contado y que involucren títulos valores, oro o moneda extranjera, cuya exigencia de capital se calculará conforme a lo previsto en el punto 4.1.
> *heredado:* 4.3.1. Definiciones.
> *propio:* 4.3.1.2. Miembro compensador ("clearing member"): es un miembro –participante directo– de la CCP habilitado para realizar transacciones con dicha CCP, ya sea por cuenta propia o como intermediario entre la CCP y otros participantes del mercado. A los efectos del cálculo de la exigencia de capital, cuando una CCP tenga vínculos con una segunda CCP ésta será considerada como miembro compensador respecto de la primera. Dependerá de los acuerdos entre ambas que las garantías aportadas por la segunda a la primera sean tratadas como margen inicial o contribución a un fondo de garantía constituido para hacer frente a incumplimientos ("default fund").

## Omisiones leídas en T4 (M2)

sin_marca:21 [normativa; propio] «A los efectos del cálculo de la exigencia de capital»

## Código A

- **d1 Definicion** «Miembro compensador (clearing member)» — Miembro –participante directo– de la CCP habilitado para realizar transacciones con dicha CCP, ya sea por cuenta propia o como intermediario entre la CCP y otros participantes del mercado. · props: `{"termino": "Miembro compensador"}` · tramo [exacta]: «Miembro compensador ("clearing member"): es un miembro –participante directo– de la CCP habilitado para realizar transacciones con dicha CCP, ya sea por cuenta propia o como intermediario entre la CCP y otros participantes del mercado.»
- **d2 Definicion** «CCP vinculada a otra CCP: miembro compensador» — A los efectos del cálculo de la exigencia de capital, cuando una CCP tenga vínculos con una segunda CCP, ésta es considerada miembro compensador respecto de la primera. · props: `{"termino": "Miembro compensador"}` · tramo [exacta]: «A los efectos del cálculo de la exigencia de capital, cuando una CCP tenga vínculos con una segunda CCP ésta será considerada como miembro compensador respecto de la primera.»
- Omisión `fuera_de_tipos` [exacta]: «Dependerá de los acuerdos entre ambas que las garantías aportadas por la segunda a la primera sean tratadas como margen inicial o contribución a un fondo de garantía constituido para hacer frente a incumplimientos ("default fund").» — Regla de tratamiento de garantías que depende de los acuerdos entre las CCP; no manda ni prohíbe ni habilita conducta del sujeto regulado. Habría sido una Definicion o Condicion, pero no encaja con pr…

### A — omisiones de T4 a clasificar

- sin_marca:21 → entidades: d2 Definicion [exacta] solap 1.0 contiene | omisiones: —

## Código H

- **d1 Definicion** «Miembro compensador (clearing member)» — Miembro –participante directo– de la CCP habilitado para realizar transacciones con dicha CCP, ya sea por cuenta propia o como intermediario entre la CCP y otros participantes del mercado. · props: `{"termino": "Miembro compensador"}` · tramo [exacta]: «Miembro compensador ("clearing member"): es un miembro –participante directo– de la CCP habilitado para realizar transacciones con dicha CCP, ya sea por cuenta propia o como intermediario entre la CCP y otros participantes del mercado.»
- **d2 Definicion** «CCP vinculada a otra CCP: miembro compensador» — A los efectos del cálculo de la exigencia de capital, cuando una CCP tenga vínculos con una segunda CCP, la segunda es considerada miembro compensador respecto de la primera. · props: `{"termino": "miembro compensador"}` · tramo [exacta]: «A los efectos del cálculo de la exigencia de capital, cuando una CCP tenga vínculos con una segunda CCP ésta será considerada como miembro compensador respecto de la primera.»
- Omisión `fuera_de_tipos` [exacta]: «Dependerá de los acuerdos entre ambas que las garantías aportadas por la segunda a la primera sean tratadas como margen inicial o contribución a un fondo de garantía constituido para hacer frente a incumplimientos ("default fund").» — Regla de clasificación de las garantías (margen inicial o contribución al default fund) según los acuerdos entre CCP; no es deber, prohibición, facultad ni definición. Habría sido Condicion o Definici…

### H — omisiones de T4 a clasificar

- sin_marca:21 → entidades: d2 Definicion [exacta] solap 1.0 contiene | omisiones: —

## Código K

- **e1 Definicion** «Miembro compensador (clearing member)» — Miembro (participante directo) de la CCP habilitado para realizar transacciones con dicha CCP, ya sea por cuenta propia o como intermediario entre la CCP y otros participantes del mercado. · props: `{"termino": "Miembro compensador"}` · tramo [exacta]: «Miembro compensador ("clearing member"): es un miembro –participante directo– de la CCP habilitado para realizar transacciones con dicha CCP, ya sea por cuenta propia o como intermediario entre la CCP y otros participantes del mercado.»
- **e2 Definicion** «Segunda CCP vinculada como miembro compensador» — A los efectos del cálculo de la exigencia de capital, cuando una CCP tenga vínculos con una segunda CCP, ésta será considerada miembro compensador respecto de la primera. · props: `{"termino": "miembro\ncompensador"}` · tramo [exacta]: «cuando una CCP tenga vínculos con una segunda CCP ésta será considerada como miembro compensador respecto de la primera»
- **e3 Condicion** «CCP con vínculos con segunda CCP» — Supuesto: una CCP tiene vínculos con una segunda CCP. · tramo [exacta]: «cuando una CCP tenga vínculos con una segunda CCP»
- **e4 Definicion** «Tratamiento de garantías entre CCP vinculadas» — Según los acuerdos entre ambas CCP, las garantías aportadas por la segunda a la primera se tratan como margen inicial o como contribución a un fondo de garantía constituido para hacer frente a incumplimientos (default fund). · props: `{"termino": "garantías aportadas por la segunda a la primera"}` · tramo [exacta]: «Dependerá de los acuerdos entre ambas que las garantías aportadas por la segunda a la primera sean tratadas como margen inicial o contribución a un fondo de garantía»
- Omisión `relacion_sin_predicado` [exacta]: «cuando una CCP tenga vínculos con una segunda CCP ésta será considerada como miembro compensador» — condicion_de no admite Definicion como rango

### K — omisiones de T4 a clasificar

- sin_marca:21 → entidades: — | omisiones: —

## Código W

- **d1 Definicion** «Miembro compensador (clearing member)» — Miembro (participante directo) de la CCP habilitado para realizar transacciones con dicha CCP, por cuenta propia o como intermediario entre la CCP y otros participantes del mercado. · props: `{"termino": "Miembro compensador"}` · tramo [exacta]: «Miembro compensador ("clearing member"): es un miembro –participante directo– de la CCP habilitado para realizar transacciones con dicha CCP, ya sea por cuenta propia o como intermediario entre la CCP y otros participantes del mercado.»
- **d2 Definicion** «CCP vinculada como miembro compensador» — A los efectos del cálculo de la exigencia de capital, cuando una CCP tenga vínculos con una segunda CCP, ésta es considerada miembro compensador respecto de la primera. · props: `{"termino": "Miembro compensador"}` · tramo [exacta]: «cuando una CCP tenga vínculos con una segunda CCP ésta será considerada como miembro compensador respecto de la primera»
- **c1 Condicion** «Acuerdos entre CCP definen tratamiento de garantías» — Según los acuerdos entre ambas CCP, las garantías aportadas por la segunda a la primera se tratan como margen inicial o como contribución a un fondo de garantía para incumplimientos (default fund). · tramo [exacta]: «Dependerá de los acuerdos entre ambas que las garantías aportadas por la segunda a la primera sean tratadas como margen inicial o contribución a un fondo de garantía»

### W — omisiones de T4 a clasificar

- sin_marca:21 → entidades: — | omisiones: —

