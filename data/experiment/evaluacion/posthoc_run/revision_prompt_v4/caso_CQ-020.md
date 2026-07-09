# Caso CQ-020 — calibración del verificador v4 (commit `e35fe21`)

## Pregunta

> ¿Cómo se calcula la exigencia de capital por riesgo de crédito (CRC) y con qué frecuencia se reporta al BCRA?

## Ground-truth (lectura pre-registrada)

`completitud_kg` primaria. (La secundaria `generación-de-más` suma pero no es requisito.)

## Atribución del verificador v4

Confianza declarada: **alta** · parse_ok: True · tool calls: 14 · tokens 264176 in / 8582 out

### Atribución 0 — `generación-de-más` / lado agente / primaria

Pata: Cómo se calcula la exigencia de capital por riesgo de crédito (CRC) — glosas de términos

Evidencia:
  - **afirmacion** — quote: «0,08 es el coeficiente de capital mínimo, [...] donde A representa activos, p los ponderadores de riesgo, PFB posiciones fuera de balance, y CCF factores de conversión de crédito.»
    ubicación: respuesta final
  - **nodo** — quote: «Cálculo de la exigencia por riesgo de crédito sin incluir el término INC mediante la fórmula: Código 70100000 (n) = k x 0,08 [ ∑(A x p) + ∑ (PFB x CCF x p) + ∑ (12300000 x p) + (∑ 13X00000 + 14000000 + 86300000) x 12,5 + 15000000 ]»
    ubicación: Operacion_calculo_de_exigencia_por_riesgo (nodo no contiene el 'donde:' que define A/p/PFB/CCF)
  - **fuente** — quote: «A = códigos de partida 11000000 a 12100000, 12400000 a 12600000. PFB = códigos de partida 1221000X y 1222000X; X = código de CCF aplicable según el punto 3.1.2. p = ponderador aplicable según el modelo de información del punto 3.1.4.»
    ubicación: TO_regimen_informativo_contable_mensual_actual.pdf, p.37 (Punto 8.1.1)

Búsquedas declaradas:
  - consulta: «APR_c factor ponderación riesgo»
    resultado: 255 matches, ninguno define 0,08 como coeficiente de capital mínimo
  - consulta: «INC incremento exigencia capital»
    resultado: 273 matches, ninguno define 0,08

### Atribución 1 — `generación-de-más` / lado agente / primaria

Pata: Con qué frecuencia se reporta al BCRA — el reporte traído es de riesgo de mercado, no de crédito

Evidencia:
  - **afirmacion** — quote: «Las entidades financieras deben presentar información sobre exigencia de capitales mínimos por riesgo de mercado con periodicidad mensual, desglosada por código de concepto y día del mes.»
    ubicación: respuesta final
  - **nodo** — quote: «Presentar información sobre exigencia de capitales mínimos por riesgo de mercado con periodicidad mensual, desglosada por código de concepto y día del mes»
    ubicación: Obligacion_informar_exigencia_de_capitales_por_riesgo
  - **fuente** — quote: «4.2. Modelos de información  Cuadro 4.2.1. Exigencia [...] 311000/xx Exigencia por riesgo de tasa - Total [...] 313000/xx Exigencia por riesgo de tipo de cambio [...] Sección 4. Exigencia e integración por riesgo de mercado»
    ubicación: TO_regimen_informativo_contable_mensual_actual.pdf, Punto 4.2 (pág 13)

Búsquedas declaradas:
  - consulta: «informar exigencia capital riesgo crédito mensual día del mes»
    resultado: 893 matches; nodos de riesgo operacional, incumplimientos de grandes exposiciones, incrementos por graduación de crédito; ninguno replica 'desglosada por código de concepto y día del mes' para riesgo de crédito

### Atribución 2 — `provenance_imprecisa` / lado grafo / secundaria

Pata: Cómo se calcula CRC — fórmula alternativa Código 70100000

Evidencia:
  - **afirmacion** — quote: «Alternativamente, sin incluir el término INC, se utiliza la fórmula: Código 70100000 (n) = k x 0,08 [ ∑(A x p) + ∑ (PFB x CCF x p) + ∑ (12300000 x p) + (∑ 13X00000 + 14000000 + 86300000) x 12,5 + 15000000 ]»
    ubicación: respuesta final
  - **nodo** — quote: «Cálculo de la exigencia por riesgo de crédito sin incluir el término INC mediante la fórmula: Código 70100000 (n) = k x 0,08 [ ∑(A x p) + ∑ (PFB x CCF x p) + ∑ (12300000 x p) + (∑ 13X00000 + 14000000 + 86300000) x 12,5 + 15000000 ]»
    ubicación: Operacion_calculo_de_exigencia_por_riesgo (provenance: Punto 8.1. Normas de procedimiento.)
  - **fuente** — quote: «8.1. Normas de procedimiento [pág 1: solo índice: '8.1. Normas de procedimiento / 8.2. Modelo de información / Sección 9. Incrementos...']»
    ubicación: TO_regimen_informativo_contable_mensual_actual.pdf, Punto 8.1 (ancla a un índice; el contenido real está en 8.1.1, p.37)

Búsquedas declaradas:
  (sin búsquedas declaradas en esta atribución)

## Razonamiento completo (verbatim)

> La pregunta tiene dos patas. PATA CÁLCULO: la fórmula central C_RC=(k x 0,08 x APR_c)+INC (aprobada) sale fiel del nodo Operacion_calculo_de_capital_minimo y del PDF 3.1.2. La fórmula alternativa (Código 70100000) también existe fielmente en el nodo Operacion_calculo_de_exigencia_por_riesgo y en el PDF (p.37, Punto 8.1.1); su cita apunta a 'Punto 8.1' que ancla a un índice, no al 8.1.1 donde vive el contenido (provenance imprecisa, secundaria). Lo que el juez marcó no_soportado son las GLOSAS que el agente agregó y que NINGÚN nodo visto contiene: (1) '0,08 es el coeficiente de capital mínimo' — ni el nodo de la fórmula ni las búsquedas de definición devuelven ese significado; (2) 'A representa activos', 'p ponderadores de riesgo', 'PFB posiciones fuera de balance', 'CCF factores de conversión de crédito' — el nodo NO contiene el bloque 'donde:' y el PDF (8.1.1) define A y PFB como CÓDIGOS DE PARTIDA, no como conceptos genéricos, por lo que además de no soportadas son inexactas. Esto es generación-de-más del agente (primaria de la pata cálculo). PATA REPORTE: el juez marcó FALSO 'corresponde a exigencia por riesgo de mercado' porque la pregunta pide la frecuencia de reporte del riesgo de CRÉDITO, pero el agente eligió el nodo Obligacion_informar_exigencia_de_capitales_por_riesgo, que dice fielmente 'riesgo de mercado' (Punto 4.2, Cuadro 4.2.1 de la Sección 4 'por riesgo de mercado'). El nodo es fiel al PDF; el error es del agente que trajo un reporte de la materia equivocada y lo presentó como respuesta a la pata de riesgo de crédito, arrastrando también la glosa 'desglosada por código de concepto y día del mes' (propia del cuadro de mercado). Es generación-de-más/uso indebido del agente (primaria de la pata reporte). El grafo tenía el dato correcto de la fórmula; el circuito se rompe en la construcción de la respuesta del agente, salvo la imprecisión de cita secundaria del grafo.

## Búsquedas en la trayectoria del verificador (tool calls `buscar_nodos`)

- paso 9: consulta «informar exigencia capital riesgo crédito mensual día del mes»
  → primeros resultados: ['Exigencia capital segundo a trigésimo sexto mes', 'Informar CRO mensualmente', 'Cálculo exigencia capital mínimo']
- paso 12: consulta «información exigencia riesgo crédito código concepto día del mes sección 3»
  → primeros resultados: ['Informar incumplimientos de Grandes Exposiciones', 'Informar incumplimientos de graduación de crédito', 'Incremento exigencia por exceso en graduación de crédito']

(La trayectoria completa —14 tool calls— está en `posthoc_run/calibracion_verificador_v4/CQ-020.json`, campo `_meta.trayectoria_verificador`.)
