# `cap::5.2.1.3` — No deberá existir una correlación positiva sustancial entre la calidad crediticia

Grupos: omisiones. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 5. Cobertura del riesgo de crédito.
> *heredado:* A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las técnicas previstas en el punto 5.1. La presente sección contempla, además, el cálculo de la exposición a las operaciones de financiación con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sección 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.
> *heredado:* 5.2. Requisitos para la aplicación de técnicas de coberturas del riesgo de crédito.
> *heredado:* 5.2.1. Requisitos generales.
> *propio:* 5.2.1.3. No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía –por ejemplo, los títulos valores emitidos por la contraparte o un vinculado a ella, no son admisibles–.

## Omisiones leídas en T4 (M2)

sin_marca:22 [no normativa; propio] «por ejemplo»

## Código A

- **op1 Operacion** «Cobertura del riesgo de crédito con garantías» — Aplicación de técnicas de cobertura del riesgo de crédito (CRC) mediante garantías, a los efectos del cómputo de la exigencia de capital por riesgo de crédito. · props: `{"tipo": "cobertura del riesgo de crédito"}` · tramo [exacta]: «No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía»
- **r1 Restriccion** «Sin correlación positiva sustancial calidad crediticia-garantía» — No debe existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía; por ejemplo, los títulos valores emitidos por la contraparte o un vinculado a ella no son admisibles. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía –por ejemplo, los títulos valores emitidos por la contraparte o un vinculado a ella, no son admisibles–»
- R: r1 Restriccion —limita→ op1 Operacion

### A — omisiones de T4 a clasificar

- sin_marca:22 → entidades: r1 Restriccion [exacta] solap 1.0 contiene | omisiones: —

## Código H

- **op1 Operacion** «Reconocimiento de garantía en cobertura del riesgo de crédito» — Reconocimiento de garantías como técnica de cobertura del riesgo de crédito (CRC) a efectos del cómputo de la exigencia de capital por riesgo de crédito. · props: `{"tipo": "cobertura_riesgo_credito"}` · tramo [exacta]: «No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía»
- **r1 Restriccion** «Sin correlación positiva sustancial calidad crediticia-garantía» — No debe existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía; por ejemplo, los títulos valores emitidos por la contraparte o un vinculado a ella no son admisibles. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía»
- R: r1 Restriccion —limita→ op1 Operacion

### H — omisiones de T4 a clasificar

- sin_marca:22 → entidades: — | omisiones: —

## Código K

- **e1 Operacion** «Aplicación de técnicas de cobertura del riesgo de crédito» — Reconocimiento de la cobertura del riesgo de crédito mediante técnicas CRC a los efectos del cómputo de la exigencia de capital · props: `{"tipo": "cobertura del riesgo de crédito"}` · tramo [exacta]: «Requisitos para la aplicación de técnicas de coberturas del riesgo de crédito»
- **e2 Restriccion** «Sin correlación positiva sustancial contraparte-garantía — CRC» — Requisito general para aplicar técnicas CRC: no deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía»
- **e3 Restriccion** «Inadmisibles títulos de la contraparte o vinculado — garantía CRC» — Como ejemplo de correlación positiva sustancial, los títulos valores emitidos por la contraparte o un vinculado a ella no son admisibles como garantía para la cobertura del riesgo de crédito. · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «los títulos valores emitidos por la contraparte o un vinculado a ella, no son admisibles»
- R: e2 Restriccion —limita→ e1 Operacion
- R: e3 Restriccion —prohibe→ e1 Operacion

### K — omisiones de T4 a clasificar

- sin_marca:22 → entidades: — | omisiones: —

## Código W

- **e1 Operacion** «Aplicación de técnicas de cobertura del riesgo de crédito» — Aplicación de técnicas de cobertura del riesgo de crédito (CRC) a efectos del cómputo de la exigencia de capital por riesgo de crédito · props: `{"tipo": "cobertura del riesgo de crédito"}` · tramo [exacta]: «Requisitos para la aplicación de técnicas de coberturas del riesgo de crédito»
- **e2 Restriccion** «Sin correlación positiva sustancial contraparte-garantía — CRC» — Requisito general para aplicar técnicas de CRC: no deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía»
- **e3 Restriccion** «Inadmisibles títulos de contraparte o vinculado — garantía CRC» — Por ejemplo, los títulos valores emitidos por la contraparte o un vinculado a ella no son admisibles como garantía para la cobertura del riesgo de crédito. · props: `{"tipo": "prohibicion"}` · tramo [exacta]: «los títulos valores emitidos por la contraparte o un vinculado a ella, no son admisibles»
- R: e2 Restriccion —limita→ e1 Operacion
- R: e3 Restriccion —prohibe→ e1 Operacion

### W — omisiones de T4 a clasificar

- sin_marca:22 → entidades: — | omisiones: —

