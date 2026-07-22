# Expediente de adjudicación — GATE CQN2 — parte 1

Fecha: 2026-07-19. SOLO LECTURA; escrituras: los 2 archivos del expediente. **Ni el
verificador (ninguna versión), ni las capas, ni S1 corrieron sobre este material —
SELLADO POR INEXISTENCIA vigente hasta el commit de la vara.** Cero adjudicación: hechos
verbatim con ruta de origen.

Casos: las 11 fallas con síntoma no vacío del censo (censo_gate_cqn2.md). Fuentes:
`queries/eval_set_cqn2.json` (el SELLADO, df29525; el runtime solo duplica un campo),
`posthoc_run/traces/gate_cqn2/run_3/{id}.json`, barrido mecánico de territorio sobre las
5 varas previas (regex del numeral con guardas de dígito).

Índice de casos: CQN2-002 · CQN2-004 · CQN2-005 · CQN2-006 · CQN2-007 · CQN2-010 · CQN2-011 · CQN2-012 · CQN2-013 · CQN2-014 · CQN2-015

Partes: 1 = secciones 1-2-4-5; 2 = trayectorias completas (sección 3).


---

# CQN2-002 — [factual_directa] · estrato **primaria**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn2.json — el SELLADO)

**Pregunta:** Una entidad financiera controlante sujeta a supervisión consolidada, ¿sobre qué bases debe observar las normas sobre clasificación de deudores?

**ground_truth_secciones:** ["9.2."]
**tos_fuente:** ["TO_clasificacion_deudores_actual.pdf"]
**categoria:** factual_directa · **seccion_sorteada_origen:** "CLA-S9"
**estrato:** primaria · sin disclosure

**cita_textual del GT:** "Sin perjuicio del cumplimiento en forma individual, las entidades financieras controlantes suje-
tas a supervisión consolidada observarán las normas en materia de clasificación de deudores
sobre base consolidada mensual y, adicional e independientemente, trimestral."

**respuesta_breve del GT:** Además del cumplimiento en forma individual, debe observarlas sobre base consolidada mensual y, adicional e independientemente, trimestral.

## 2. Síntoma del juez (verbatim, traza gate_cqn2)

`judge.step1`:

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Una entidad financiera controlante sujeta a supervisión consolidada debe observar las normas sobre clasificación de deudores sobre base consolidada.",
   "central": true
  },
  {
   "enunciado": "Las normas del país donde esté situada la casa matriz o entidad controlante deben abarcar la supervisión sobre base consolidada de las filiales o subsidiarias locales.",
   "central": false
  },
  {
   "enunciado": "Los datos de clasificación de deudores se informan sobre base individual con código de consolidación 0 ó 1.",
   "central": false
  },
  {
   "enunciado": "Los datos de clasificación de deudores se informan sobre base consolidada trimestral con código de consolidación 3.",
   "central": false
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "Bases sobre las que una entidad financiera controlante sujeta a supervisión consolidada debe observar las normas sobre clasificación de deudores"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "Una entidad financiera controlante sujeta a supervisión consolidada debe observar las normas sobre clasificación de deudores sobre base consolidada.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Las normas del país donde esté situada la casa matriz o entidad controlante deben abarcar la supervisión sobre base consolidada de las filiales o subsidiarias locales.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Los datos de clasificación de deudores se informan sobre base individual con código de consolidación 0 ó 1.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Los datos de clasificación de deudores se informan sobre base consolidada trimestral con código de consolidación 3.",
  "central": false,
  "verdict": "no_soportado"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Bases sobre las que una entidad financiera controlante sujeta a supervisión consolidada debe observar las normas sobre clasificación de deudores",
  "cobertura": "cubierta"
 }
]
```

`judge.verdict`:

```json
{
 "correctitud": "correcta",
 "completitud": "completa",
 "cita_documento_correcto": true,
 "cita_precision": "punto",
 "abstencion": null,
 "especulacion_en_prosa": null,
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [
   "Las normas del país donde esté situada la casa matriz o entidad controlante deben abarcar la supervisión sobre base consolidada de las filiales o subsidiarias locales.",
   "Los datos de clasificación de deudores se informan sobre base individual con código de consolidación 0 ó 1.",
   "Los datos de clasificación de deudores se informan sobre base consolidada trimestral con código de consolidación 3."
  ],
  "n_centrales": 0,
  "n_secundarias": 3
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "El agente cita TO_clasificacion_deudores_actual.pdf, que corresponde al ground truth, con precisión a nivel punto (Punto 2.2), aunque el referente indica que la información relevante está en el punto 9.2."
 }
}
```

**Síntoma (resumen mecánico, filtro de build_falla_context): F = 3 (0 centrales) · P = 0 → NO VACÍO.**

## 3. Trayectoria

En `expediente_gate2_2.md`, sección "CQN2-002".

## 4. Homólogos / territorio

**Disclosure del sellado:** (sin disclosure — estrato primaria limpio)

**Territorio en varas previas** (barrido mecánico):

- GT `9.2.` (numeral 9.2) en **casos_gate_cqn.md** — 5 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L184): 9.2 de Exterior, con su antecedente "Por cada operación… deberá seleccionar una
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L185): entidad… Esta entidad será la única responsable…" (`cqn_010.md`, corpus 9.2).
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L195): - **Nota de conexión (K11):** los fragmentos del 9.2 SÍ existen en el grafo (incluido "el
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L197): clave porta LA MISMA provenance corrupta — el 9.2 fue extraído FRAGMENTADO con la
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L351): CQN-013 ×2 (1.5 por 1.6; 4.4 por Sección 5) — más los fragmentos del 9.2 de K11 con la

## 5. Tabla inicial de hechos (cero adjudicación)

**Claims reprobados:**
- secundario `no_soportado`: "Las normas del país donde esté situada la casa matriz o entidad controlante deben abarcar la supervisión sobre base consolidada de las filiales o subsidiarias locales."
- secundario `no_soportado`: "Los datos de clasificación de deudores se informan sobre base individual con código de consolidación 0 ó 1."
- secundario `no_soportado`: "Los datos de clasificación de deudores se informan sobre base consolidada trimestral con código de consolidación 3."

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Bases sobre las que una entidad financiera controlante sujeta a supervisión consolidada debe observar las normas sobre clasificación de deudores | cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 |

**Descomposición del juez (step1, verbatim):**
- afirmación (central): "Una entidad financiera controlante sujeta a supervisión consolidada debe observar las normas sobre clasificación de deudores sobre base consolidada."
- afirmación (no central): "Las normas del país donde esté situada la casa matriz o entidad controlante deben abarcar la supervisión sobre base consolidada de las filiales o subsidiarias locales."
- afirmación (no central): "Los datos de clasificación de deudores se informan sobre base individual con código de consolidación 0 ó 1."
- afirmación (no central): "Los datos de clasificación de deudores se informan sobre base consolidada trimestral con código de consolidación 3."


---

# CQN2-004 — [factual_directa] · estrato **primaria**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn2.json — el SELLADO)

**Pregunta:** ¿Cómo se determina la exigencia de capital mínimo por riesgo de mercado de una entidad financiera y qué método debe emplearse para su cálculo?

**ground_truth_secciones:** ["6.1."]
**tos_fuente:** ["TO_capitales_minimos_actual.pdf"]
**categoria:** factual_directa · **seccion_sorteada_origen:** "CAP-S6"
**estrato:** primaria · sin disclosure

**cita_textual del GT:** "La exigencia de capital por riesgo de mercado (RM) será la suma aritmética de la exigencia de
capital por los riesgos por tasa de interés (RT), acciones (RA), tipo de cambio (RTC), produc-
tos básicos (RPB) y opciones (ROP).
RM = RT + RA + RTC + RPB + ROP
Para su determinación, las entidades deberán emplear el Método de Medición Estándar pre-
visto en el punto 6.1.4."

**respuesta_breve del GT:** Es la suma aritmética de las exigencias de capital por los riesgos por tasa de interés (RT), acciones (RA), tipo de cambio (RTC), productos básicos (RPB) y opciones (ROP): RM = RT + RA + RTC + RPB + ROP. Para determinarla debe emplearse el Método de Medición Estándar.

## 2. Síntoma del juez (verbatim, traza gate_cqn2)

`judge.step1`:

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "La exigencia de capital mínimo por riesgo de mercado se determina mediante el Método de Medición Estándar.",
   "central": true
  },
  {
   "enunciado": "El Método de Medición Estándar está previsto en el punto 6.1.4 de la normativa de Capitales Mínimos del BCRA.",
   "central": true
  },
  {
   "enunciado": "Para el cálculo de la exigencia de capital por riesgo general de mercado se utiliza el método de plazos residuales.",
   "central": true
  },
  {
   "enunciado": "El método de plazos residuales obtiene la exigencia como la suma del valor absoluto de la posición ponderada neta, un porcentaje de desestimación vertical, porcentajes de desestimación horizontal y el cambio neto en opciones.",
   "central": true
  },
  {
   "enunciado": "La exigencia por riesgo de mercado se determina computando el mayor valor entre los códigos de cálculo 70810000 y 70820000.",
   "central": true
  },
  {
   "enunciado": "Para posiciones en opciones, las entidades pueden utilizar un método simplificado si cumplen ciertos límites.",
   "central": false
  },
  {
   "enunciado": "Las entidades pueden informar la exigencia por posiciones en opciones mediante cálculos de Gamma y Vega como alternativa al método simplificado.",
   "central": false
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "Cómo se determina la exigencia de capital mínimo por riesgo de mercado de una entidad financiera",
  "Qué método debe emplearse para su cálculo"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "La exigencia de capital mínimo por riesgo de mercado se determina mediante el Método de Medición Estándar.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "El Método de Medición Estándar está previsto en el punto 6.1.4 de la normativa de Capitales Mínimos del BCRA.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Para el cálculo de la exigencia de capital por riesgo general de mercado se utiliza el método de plazos residuales.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "El método de plazos residuales obtiene la exigencia como la suma del valor absoluto de la posición ponderada neta, un porcentaje de desestimación vertical, porcentajes de desestimación horizontal y el cambio neto en opciones.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "La exigencia por riesgo de mercado se determina computando el mayor valor entre los códigos de cálculo 70810000 y 70820000.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Para posiciones en opciones, las entidades pueden utilizar un método simplificado si cumplen ciertos límites.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Las entidades pueden informar la exigencia por posiciones en opciones mediante cálculos de Gamma y Vega como alternativa al método simplificado.",
  "central": false,
  "verdict": "no_soportado"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Cómo se determina la exigencia de capital mínimo por riesgo de mercado de una entidad financiera",
  "cobertura": "cubierta"
 },
 {
  "pata": "Qué método debe emplearse para su cálculo",
  "cobertura": "cubierta"
 }
]
```

`judge.verdict`:

```json
{
 "correctitud": "correcta",
 "completitud": "completa",
 "cita_documento_correcto": true,
 "cita_precision": "punto",
 "abstencion": null,
 "especulacion_en_prosa": null,
 "afirmaciones_no_soportadas": {
  "centrales": [
   "Para el cálculo de la exigencia de capital por riesgo general de mercado se utiliza el método de plazos residuales.",
   "El método de plazos residuales obtiene la exigencia como la suma del valor absoluto de la posición ponderada neta, un porcentaje de desestimación vertical, porcentajes de desestimación horizontal y el cambio neto en opciones.",
   "La exigencia por riesgo de mercado se determina computando el mayor valor entre los códigos de cálculo 70810000 y 70820000."
  ],
  "secundarias": [
   "Para posiciones en opciones, las entidades pueden utilizar un método simplificado si cumplen ciertos límites.",
   "Las entidades pueden informar la exigencia por posiciones en opciones mediante cálculos de Gamma y Vega como alternativa al método simplificado."
  ],
  "n_centrales": 3,
  "n_secundarias": 2
 },
 "requiere_adjudicacion_humana": true,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "La cita al Punto 6.1. de TO_capitales_minimos_actual.pdf coincide con el ground truth (sección 6.1.) y tiene precisión a nivel punto."
 }
}
```

**Síntoma (resumen mecánico, filtro de build_falla_context): F = 5 (3 centrales) · P = 0 → NO VACÍO.**

## 3. Trayectoria

En `expediente_gate2_2.md`, sección "CQN2-004".

## 4. Homólogos / territorio

**Disclosure del sellado:** (sin disclosure — estrato primaria limpio)

**Territorio en varas previas** (barrido mecánico):

- GT `6.1.` (numeral 6.1) en **casos_validacion.md** — 2 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L1): # Casos de la validación de v6.1-D — vara de adjudicación (marco POST-HOC)
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L3): Vara de la **validación empírica del compuesto v6.1-D**, bajo
- GT `6.1.` (numeral 6.1) en **casos_dev_v7.md** — 2 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L7): pre-registrado v6.1-D vs v7.
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L10): afirma — el input real del instrumento). **Adjudicada ANTES de correr v6.1-D o S1 sobre
- GT `6.1.` (numeral 6.1) en **casos_gate_cqn.md** — 2 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L373): ## (c) Reglas de acierto por caso — para el head-to-head v6.1-D vs v7
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L399): sobre estos 10 casos; el head-to-head pre-registrado (v6.1-D vs v7, mismo material,

## 5. Tabla inicial de hechos (cero adjudicación)

**Claims reprobados:**
- CENTRAL `no_soportado`: "Para el cálculo de la exigencia de capital por riesgo general de mercado se utiliza el método de plazos residuales."
- CENTRAL `no_soportado`: "El método de plazos residuales obtiene la exigencia como la suma del valor absoluto de la posición ponderada neta, un porcentaje de desestimación vertical, porcentajes de desestimación horizontal y el cambio neto en opciones."
- CENTRAL `no_soportado`: "La exigencia por riesgo de mercado se determina computando el mayor valor entre los códigos de cálculo 70810000 y 70820000."
- secundario `no_soportado`: "Para posiciones en opciones, las entidades pueden utilizar un método simplificado si cumplen ciertos límites."
- secundario `no_soportado`: "Las entidades pueden informar la exigencia por posiciones en opciones mediante cálculos de Gamma y Vega como alternativa al método simplificado."

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Cómo se determina la exigencia de capital mínimo por riesgo de mercado de una entidad financiera | cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 |
| Qué método debe emplearse para su cálculo | cubierta | 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15 |

**Descomposición del juez (step1, verbatim):**
- afirmación (central): "La exigencia de capital mínimo por riesgo de mercado se determina mediante el Método de Medición Estándar."
- afirmación (central): "El Método de Medición Estándar está previsto en el punto 6.1.4 de la normativa de Capitales Mínimos del BCRA."
- afirmación (central): "Para el cálculo de la exigencia de capital por riesgo general de mercado se utiliza el método de plazos residuales."
- afirmación (central): "El método de plazos residuales obtiene la exigencia como la suma del valor absoluto de la posición ponderada neta, un porcentaje de desestimación vertical, porcentajes de desestimación horizontal y el cambio neto en opciones."
- afirmación (central): "La exigencia por riesgo de mercado se determina computando el mayor valor entre los códigos de cálculo 70810000 y 70820000."
- afirmación (no central): "Para posiciones en opciones, las entidades pueden utilizar un método simplificado si cumplen ciertos límites."
- afirmación (no central): "Las entidades pueden informar la exigencia por posiciones en opciones mediante cálculos de Gamma y Vega como alternativa al método simplificado."


---

# CQN2-005 — [factual_directa] · estrato **primaria**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn2.json — el SELLADO)

**Pregunta:** En el sistema de seguimiento de pagos de importaciones (SEPAIMPO), ¿ante quién nomina originalmente el importador a la entidad responsable del seguimiento de la oficialización, y bajo qué condición puede cambiarla luego por otra entidad?

**ground_truth_secciones:** ["11.1."]
**tos_fuente:** ["TO_exterior_cambios_actual.pdf"]
**categoria:** factual_directa · **seccion_sorteada_origen:** "EXT-S11"
**estrato:** primaria · sin disclosure

**cita_textual del GT:** "La entidad será originalmente nominada por el importador ante la ARCA, pudiendo el
importador posteriormente modificarla en la medida que, a la fecha de la solicitud de cambio
de entidad, no existan certificaciones emitidas de acceso al mercado de cambios que estén
pendientes de uso."

**respuesta_breve del GT:** La entidad es originalmente nominada por el importador ante la ARCA. Puede modificarla posteriormente en la medida que, a la fecha de la solicitud de cambio de entidad, no existan certificaciones emitidas de acceso al mercado de cambios pendientes de uso.

## 2. Síntoma del juez (verbatim, traza gate_cqn2)

`judge.step1`:

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "En SEPAIMPO, por cada oficialización del despacho de importación, el importador nomina una entidad para que se haga responsable del seguimiento de la oficialización.",
   "central": true
  },
  {
   "enunciado": "La documentación consultada establece la obligación de nominación inicial.",
   "central": false
  }
 ],
 "reportes_de_alcance": [
  "En la información disponible en el Knowledge Graph no se especifican las condiciones bajo las cuales el importador puede cambiar posteriormente la entidad nominada.",
  "La documentación consultada no detalla los supuestos o requisitos para modificar la entidad nominada."
 ],
 "patas_de_la_pregunta": [
  "Ante quién nomina originalmente el importador a la entidad responsable del seguimiento de la oficialización en SEPAIMPO",
  "Bajo qué condición puede el importador cambiar luego esa entidad por otra"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "En SEPAIMPO, por cada oficialización del despacho de importación, el importador nomina una entidad para que se haga responsable del seguimiento de la oficialización.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La documentación consultada establece la obligación de nominación inicial.",
  "central": false,
  "verdict": "verdadero"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Ante quién nomina originalmente el importador a la entidad responsable del seguimiento de la oficialización en SEPAIMPO",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "Bajo qué condición puede el importador cambiar luego esa entidad por otra",
  "cobertura": "no_cubierta"
 }
]
```

`judge.verdict`:

```json
{
 "correctitud": "correcta",
 "completitud": "parcial",
 "cita_documento_correcto": true,
 "cita_precision": "punto",
 "abstencion": null,
 "especulacion_en_prosa": null,
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [],
  "n_centrales": 0,
  "n_secundarias": 0
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Ante quién nomina originalmente el importador a la entidad responsable del seguimiento de la oficialización en SEPAIMPO; Bajo qué condición puede el importador cambiar luego esa entidad por otra",
  "citas": "El agente cita correctamente el Punto 11.1 del TO_exterior_cambios_actual.pdf, que es el documento y sección del ground truth."
 }
}
```

**Síntoma (resumen mecánico, filtro de build_falla_context): F = 0 (0 centrales) · P = 2 → NO VACÍO.**

## 3. Trayectoria

En `expediente_gate2_2.md`, sección "CQN2-005".

## 4. Homólogos / territorio

**Disclosure del sellado:** (sin disclosure — estrato primaria limpio)

**Territorio en varas previas** (barrido mecánico):

- GT `11.1.` (numeral 11.1) en **casos_gate_cqn.md** — 1 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L232): código 3 figura suspendido), 11.1 en página 46 (`cqn_011.md`).

## 5. Tabla inicial de hechos (cero adjudicación)

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Ante quién nomina originalmente el importador a la entidad responsable del seguimiento de la oficialización en SEPAIMPO | no_cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 |
| Bajo qué condición puede el importador cambiar luego esa entidad por otra | no_cubierta | 1, 2, 3, 4, 6, 7, 9, 10, 12 |

**Descomposición del juez (step1, verbatim):**
- afirmación (central): "En SEPAIMPO, por cada oficialización del despacho de importación, el importador nomina una entidad para que se haga responsable del seguimiento de la oficialización."
- afirmación (no central): "La documentación consultada establece la obligación de nominación inicial."
- reporte de alcance: "En la información disponible en el Knowledge Graph no se especifican las condiciones bajo las cuales el importador puede cambiar posteriormente la entidad nominada."
- reporte de alcance: "La documentación consultada no detalla los supuestos o requisitos para modificar la entidad nominada."


---

# CQN2-006 — [factual_directa] · estrato **primaria**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn2.json — el SELLADO)

**Pregunta:** En el régimen informativo sobre exigencia e integración de capitales mínimos, ¿con qué frecuencia y mediante qué expresión se determina la exigencia de capital por riesgo operacional de las entidades del Grupo 1, y qué valor toma el multiplicador de pérdida interna?

**ground_truth_secciones:** ["5.1.1."]
**tos_fuente:** ["TO_regimen_informativo_contable_mensual_actual.pdf"]
**categoria:** factual_directa · **seccion_sorteada_origen:** "RIC-S5"
**estrato:** primaria · sin disclosure

**cita_textual del GT:** "Se determinará mensualmente por la siguiente expresión:
CRO = BIC x ILM
[...]
CRO: exigencia de capital por riesgo operacional.
ILM: multiplicador de pérdida interna igual a 1."

**respuesta_breve del GT:** Se determina mensualmente mediante la expresión CRO = BIC x ILM, donde CRO es la exigencia de capital por riesgo operacional, BIC el componente del indicador de negocio e ILM el multiplicador de pérdida interna, que es igual a 1.

## 2. Síntoma del juez (verbatim, traza gate_cqn2)

`judge.step1`:

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "La exigencia de capital por riesgo operacional de las entidades del Grupo 1 se determina con frecuencia mensual.",
   "central": true
  },
  {
   "enunciado": "La expresión utilizada para determinar la exigencia de capital por riesgo operacional de las entidades del Grupo 1 es CRO = BIC x ILM.",
   "central": true
  }
 ],
 "reportes_de_alcance": [
  "En la información disponible en el Knowledge Graph no se especifica el valor numérico que toma el multiplicador de pérdida interna (ILM)."
 ],
 "patas_de_la_pregunta": [
  "Frecuencia con que se determina la exigencia de capital por riesgo operacional de las entidades del Grupo 1",
  "Expresión mediante la cual se determina dicha exigencia",
  "Valor que toma el multiplicador de pérdida interna (ILM)"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "La exigencia de capital por riesgo operacional de las entidades del Grupo 1 se determina con frecuencia mensual.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La expresión utilizada para determinar la exigencia de capital por riesgo operacional de las entidades del Grupo 1 es CRO = BIC x ILM.",
  "central": true,
  "verdict": "verdadero"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Frecuencia con que se determina la exigencia de capital por riesgo operacional de las entidades del Grupo 1",
  "cobertura": "cubierta"
 },
 {
  "pata": "Expresión mediante la cual se determina dicha exigencia",
  "cobertura": "cubierta"
 },
 {
  "pata": "Valor que toma el multiplicador de pérdida interna (ILM)",
  "cobertura": "no_cubierta"
 }
]
```

`judge.verdict`:

```json
{
 "correctitud": "correcta",
 "completitud": "parcial",
 "cita_documento_correcto": false,
 "cita_precision": "punto",
 "abstencion": null,
 "especulacion_en_prosa": null,
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [],
  "n_centrales": 0,
  "n_secundarias": 0
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Valor que toma el multiplicador de pérdida interna (ILM)",
  "citas": "La cita apunta a 'TO_regimen_informativo_contable_mensual_actual.pdf' (Punto 5.1), pero el ground truth no incluye ese documento entre los referentes válidos, por lo que cita_documento_correcto es false; la precisión es a nivel punto."
 }
}
```

**Síntoma (resumen mecánico, filtro de build_falla_context): F = 0 (0 centrales) · P = 1 → NO VACÍO.**

## 3. Trayectoria

En `expediente_gate2_2.md`, sección "CQN2-006".

## 4. Homólogos / territorio

**Disclosure del sellado:** (sin disclosure — estrato primaria limpio)

**Territorio en varas previas:** el barrido mecánico de los numerales del GT sobre las 5 varas no devolvió líneas.

## 5. Tabla inicial de hechos (cero adjudicación)

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Frecuencia con que se determina la exigencia de capital por riesgo operacional de las entidades del Grupo 1 | cubierta | 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15 |
| Expresión mediante la cual se determina dicha exigencia | cubierta | 1, 2, 3, 4, 6, 9, 10, 12 |
| Valor que toma el multiplicador de pérdida interna (ILM) | no_cubierta | 3, 5, 7, 12, 13 |

**Descomposición del juez (step1, verbatim):**
- afirmación (central): "La exigencia de capital por riesgo operacional de las entidades del Grupo 1 se determina con frecuencia mensual."
- afirmación (central): "La expresión utilizada para determinar la exigencia de capital por riesgo operacional de las entidades del Grupo 1 es CRO = BIC x ILM."
- reporte de alcance: "En la información disponible en el Knowledge Graph no se especifica el valor numérico que toma el multiplicador de pérdida interna (ILM)."


---

# CQN2-007 — [factual_directa] · estrato **primaria**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn2.json — el SELLADO)

**Pregunta:** Para que la metodología de evaluación de un agente de calificación externa (ECAI) pueda ser reconocida a los fines de la determinación de ponderadores de riesgo, ¿qué antigüedad mínima de uso debe acreditar y a qué comprobación debe haber estado sujeta?

**ground_truth_secciones:** ["10.2.2.1."]
**tos_fuente:** ["TO_capitales_minimos_actual.pdf"]
**categoria:** factual_directa · **seccion_sorteada_origen:** "CAP-S10"
**estrato:** primaria · sin disclosure

**cita_textual del GT:** "Para poder ser reconocida, la metodología de evaluación de cada segmento
del mercado deberá previamente haber sido utilizada durante al menos un
año –preferiblemente tres años– y haber estado sujeta en ese lapso a la
comprobación rigurosa de su precisión mediante pruebas retrospectivas
(“backtesting”)."

**respuesta_breve del GT:** La metodología de evaluación de cada segmento del mercado debe haber sido utilizada previamente durante al menos un año –preferiblemente tres años– y haber estado sujeta en ese lapso a la comprobación rigurosa de su precisión mediante pruebas retrospectivas (backtesting).

## 2. Síntoma del juez (verbatim, traza gate_cqn2)

`judge.step1`:

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "La metodología de evaluación de un ECAI deberá haber sido utilizada durante al menos un año para ser reconocida a los fines de la determinación de ponderadores de riesgo.",
   "central": true
  },
  {
   "enunciado": "Es preferible que la metodología haya sido utilizada durante tres años.",
   "central": false
  },
  {
   "enunciado": "La metodología debe haber estado sujeta a la comprobación rigurosa de su precisión mediante pruebas retrospectivas (backtesting).",
   "central": true
  },
  {
   "enunciado": "La metodología debe ser rigurosa y sistemática.",
   "central": false
  },
  {
   "enunciado": "La metodología debe estar sujeta a algún tipo de validación basada en la experiencia histórica.",
   "central": false
  },
  {
   "enunciado": "Las evaluaciones deberán ser objeto de un control constante.",
   "central": false
  },
  {
   "enunciado": "Las evaluaciones deben responder a los cambios en la coyuntura financiera.",
   "central": false
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "Antigüedad mínima de uso que debe acreditar la metodología de evaluación de un ECAI para ser reconocida a los fines de la determinación de ponderadores de riesgo",
  "Comprobación a la que debe haber estado sujeta dicha metodología"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "La metodología de evaluación de un ECAI deberá haber sido utilizada durante al menos un año para ser reconocida a los fines de la determinación de ponderadores de riesgo.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Es preferible que la metodología haya sido utilizada durante tres años.",
  "central": false,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La metodología debe haber estado sujeta a la comprobación rigurosa de su precisión mediante pruebas retrospectivas (backtesting).",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La metodología debe ser rigurosa y sistemática.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "La metodología debe estar sujeta a algún tipo de validación basada en la experiencia histórica.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Las evaluaciones deberán ser objeto de un control constante.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Las evaluaciones deben responder a los cambios en la coyuntura financiera.",
  "central": false,
  "verdict": "no_soportado"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Antigüedad mínima de uso que debe acreditar la metodología de evaluación de un ECAI para ser reconocida a los fines de la determinación de ponderadores de riesgo",
  "cobertura": "cubierta"
 },
 {
  "pata": "Comprobación a la que debe haber estado sujeta dicha metodología",
  "cobertura": "cubierta"
 }
]
```

`judge.verdict`:

```json
{
 "correctitud": "correcta",
 "completitud": "completa",
 "cita_documento_correcto": true,
 "cita_precision": "pagina",
 "abstencion": null,
 "especulacion_en_prosa": null,
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [
   "La metodología debe ser rigurosa y sistemática.",
   "La metodología debe estar sujeta a algún tipo de validación basada en la experiencia histórica.",
   "Las evaluaciones deberán ser objeto de un control constante.",
   "Las evaluaciones deben responder a los cambios en la coyuntura financiera."
  ],
  "n_centrales": 0,
  "n_secundarias": 4
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "La cita apunta al documento correcto (TO_capitales_minimos_actual.pdf) pero solo a nivel de punto general (10.2) sin precisar la subsección 10.2.2.1., por lo que se clasifica como precisión de página."
 }
}
```

**Síntoma (resumen mecánico, filtro de build_falla_context): F = 4 (0 centrales) · P = 0 → NO VACÍO.**

## 3. Trayectoria

En `expediente_gate2_2.md`, sección "CQN2-007".

## 4. Homólogos / territorio

**Disclosure del sellado:** (sin disclosure — estrato primaria limpio)

**Territorio en varas previas:** el barrido mecánico de los numerales del GT sobre las 5 varas no devolvió líneas.

## 5. Tabla inicial de hechos (cero adjudicación)

**Claims reprobados:**
- secundario `no_soportado`: "La metodología debe ser rigurosa y sistemática."
- secundario `no_soportado`: "La metodología debe estar sujeta a algún tipo de validación basada en la experiencia histórica."
- secundario `no_soportado`: "Las evaluaciones deberán ser objeto de un control constante."
- secundario `no_soportado`: "Las evaluaciones deben responder a los cambios en la coyuntura financiera."

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Antigüedad mínima de uso que debe acreditar la metodología de evaluación de un ECAI para ser reconocida a los fines de la determinación de ponderadores de riesgo | cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| Comprobación a la que debe haber estado sujeta dicha metodología | cubierta | 1, 2, 3, 4, 6, 7, 8, 9, 10 |

**Descomposición del juez (step1, verbatim):**
- afirmación (central): "La metodología de evaluación de un ECAI deberá haber sido utilizada durante al menos un año para ser reconocida a los fines de la determinación de ponderadores de riesgo."
- afirmación (no central): "Es preferible que la metodología haya sido utilizada durante tres años."
- afirmación (central): "La metodología debe haber estado sujeta a la comprobación rigurosa de su precisión mediante pruebas retrospectivas (backtesting)."
- afirmación (no central): "La metodología debe ser rigurosa y sistemática."
- afirmación (no central): "La metodología debe estar sujeta a algún tipo de validación basada en la experiencia histórica."
- afirmación (no central): "Las evaluaciones deberán ser objeto de un control constante."
- afirmación (no central): "Las evaluaciones deben responder a los cambios en la coyuntura financiera."


---

# CQN2-010 — [multi_norma] · estrato **solapada**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn2.json — el SELLADO)

**Pregunta:** Un fideicomiso financiero es acreedor de créditos de cartera comercial cedidos por un banco. (a) En materia de protección de usuarios de servicios financieros, ¿el fiduciario es sujeto obligado, y los deudores cedidos revisten carácter de usuarios aunque no hayan sido notificados de la cesión? (b) Si un cliente registra financiaciones equivalentes al 5 % o más del activo del fideicomiso, ¿con qué periodicidad mínima debe revisarse su clasificación?

**ground_truth_secciones:** ["1.1.2.3.", "1.1.1.", "6.3.1."]
**tos_fuente:** ["TO_proteccion_usuarios_servicios_financieros_actual.pdf", "TO_clasificacion_deudores_actual.pdf"]
**categoria:** multi_norma · **seccion_sorteada_origen:** "CLA-S6 + PRO-S1"
**estrato:** solapada · **disclosure (verbatim):** Pata Clasificación 6.3.1: match exacto con CQ-024 (piloto, run_3). Pata Protección 1.1.x: hermanas directas quemadas en CQ-017 (1.1.2.2, ×2 grafos), CQ-018 (1.1.2.4/.5, ×2) y CQN-008 (1.1); el 1.1.2.3 puntual no fue GT previo. La combinación fideicomiso/deudores-cedidos es pregunta nueva.

**cita_textual del GT:** "1.1.2.3. Fiduciarios de fideicomisos acreedores de créditos cedidos por entidades finan-
cieras.
[...]
Forman también parte de esta categoría los deudores de créditos cedidos por las entida-
des financieras comprendidas en la Ley de Entidades Financieras, independientemente
de que hayan o no sido notificados fehacientemente de la transferencia de su obligación,
así como los deudores de créditos adquiridos por entidades financieras por cesión.
[...]
6.3.1. En el curso de cada trimestre calendario, respecto de clientes individualmente considera-
dos cuyas financiaciones comprendidas en algún momento sean equivalentes al 5 % o
más de la RPC o del activo del fideicomiso financiero del mes anterior a la finalización de
dicho período según se trate de entidades o fideicomisos financieros, respectivamente. A
estos fines, el grupo de contrapartes conectadas se tratará como un solo cliente."

**respuesta_breve del GT:** (a) Sí: los fiduciarios de fideicomisos acreedores de créditos cedidos por entidades financieras son sujetos obligados, y los deudores de créditos cedidos son usuarios de servicios financieros independientemente de que hayan sido o no notificados fehacientemente de la transferencia. (b) La clasificación debe revisarse en el curso de cada trimestre calendario, tratando al grupo de contrapartes conectadas como un solo cliente.

## 2. Síntoma del juez (verbatim, traza gate_cqn2)

`judge.step1`:

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Cuando un cliente registra financiaciones equivalentes al 5% o más del activo del fideicomiso financiero, su clasificación debe revisarse con una periodicidad mínima trimestral (en el curso de cada trimestre calendario).",
   "central": true
  }
 ],
 "reportes_de_alcance": [
  "No se encontró en el Knowledge Graph información explícita que confirme si el fiduciario de un fideicomiso financiero es sujeto obligado bajo la normativa de protección de usuarios de servicios financieros.",
  "No se encontró en el Knowledge Graph información explícita que confirme si los deudores cedidos revisten carácter de usuarios aunque no hayan sido notificados de la cesión."
 ],
 "patas_de_la_pregunta": [
  "Si el fiduciario de un fideicomiso financiero acreedor de créditos de cartera comercial cedidos por un banco es sujeto obligado en materia de protección de usuarios de servicios financieros",
  "Si los deudores cedidos revisten carácter de usuarios aunque no hayan sido notificados de la cesión",
  "Periodicidad mínima con la que debe revisarse la clasificación de un cliente que registra financiaciones equivalentes al 5% o más del activo del fideicomiso"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "Cuando un cliente registra financiaciones equivalentes al 5% o más del activo del fideicomiso financiero, su clasificación debe revisarse con una periodicidad mínima trimestral (en el curso de cada trimestre calendario).",
  "central": true,
  "verdict": "verdadero"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Si el fiduciario de un fideicomiso financiero acreedor de créditos de cartera comercial cedidos por un banco es sujeto obligado en materia de protección de usuarios de servicios financieros",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "Si los deudores cedidos revisten carácter de usuarios aunque no hayan sido notificados de la cesión",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "Periodicidad mínima con la que debe revisarse la clasificación de un cliente que registra financiaciones equivalentes al 5% o más del activo del fideicomiso",
  "cobertura": "cubierta"
 }
]
```

`judge.verdict`:

```json
{
 "correctitud": "correcta",
 "completitud": "parcial",
 "cita_documento_correcto": true,
 "cita_precision": "punto",
 "abstencion": null,
 "especulacion_en_prosa": null,
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [],
  "n_centrales": 0,
  "n_secundarias": 0
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Si el fiduciario de un fideicomiso financiero acreedor de créditos de cartera comercial cedidos por un banco es sujeto obligado en materia de protección de usuarios de servicios financieros; Si los deudores cedidos revisten carácter de usuarios aunque no hayan sido notificados de la cesión",
  "citas": "La cita apunta a 'TO_clasificacion_deudores_actual.pdf', Punto 6.3, que corresponde al ground truth (sección 6.3.1.), con precisión a nivel punto."
 }
}
```

**Síntoma (resumen mecánico, filtro de build_falla_context): F = 0 (0 centrales) · P = 2 → NO VACÍO.**

## 3. Trayectoria

En `expediente_gate2_2.md`, sección "CQN2-010".

## 4. Homólogos / territorio

**Disclosure del sellado:** Pata Clasificación 6.3.1: match exacto con CQ-024 (piloto, run_3). Pata Protección 1.1.x: hermanas directas quemadas en CQ-017 (1.1.2.2, ×2 grafos), CQ-018 (1.1.2.4/.5, ×2) y CQN-008 (1.1); el 1.1.2.3 puntual no fue GT previo. La combinación fideicomiso/deudores-cedidos es pregunta nueva.

**Territorio en varas previas:** el barrido mecánico de los numerales del GT sobre las 5 varas no devolvió líneas.

## 5. Tabla inicial de hechos (cero adjudicación)

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Si el fiduciario de un fideicomiso financiero acreedor de créditos de cartera comercial cedidos por un banco es sujeto obligado en materia de protección de usuarios de servicios financieros | no_cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 |
| Si los deudores cedidos revisten carácter de usuarios aunque no hayan sido notificados de la cesión | no_cubierta | 2, 3, 8, 9, 10, 11, 12, 14, 15, 16 |
| Periodicidad mínima con la que debe revisarse la clasificación de un cliente que registra financiaciones equivalentes al 5% o más del activo del fideicomiso | cubierta | 1, 3, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16 |

**Descomposición del juez (step1, verbatim):**
- afirmación (central): "Cuando un cliente registra financiaciones equivalentes al 5% o más del activo del fideicomiso financiero, su clasificación debe revisarse con una periodicidad mínima trimestral (en el curso de cada trimestre calendario)."
- reporte de alcance: "No se encontró en el Knowledge Graph información explícita que confirme si el fiduciario de un fideicomiso financiero es sujeto obligado bajo la normativa de protección de usuarios de servicios financieros."
- reporte de alcance: "No se encontró en el Knowledge Graph información explícita que confirme si los deudores cedidos revisten carácter de usuarios aunque no hayan sido notificados de la cesión."


---

# CQN2-011 — [multi_norma] · estrato **primaria**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn2.json — el SELLADO)

**Pregunta:** (a) Una entidad financiera en funcionamiento al 01/06/24 proyecta no alcanzar la integración de la exigencia básica de capital: ¿qué debe presentar, ante quién, en qué plazo y con qué duración máxima? (b) Una MiPyMe consulta si puede pagar a la vista, con registro de ingreso aduanero pendiente, la importación de una aeronave de la partida 8802 de la NCM embarcada en origen después del 14/04/25: ¿la posición arancelaria lo permite, y qué excepción subjetiva existe para ese tipo de bienes?

**ground_truth_secciones:** ["12.1. (Capitales Mínimos)", "12.1. (Exterior y Cambios)", "10.10.2.1. (Exterior y Cambios, referencia)"]
**tos_fuente:** ["TO_capitales_minimos_actual.pdf", "TO_exterior_cambios_actual.pdf"]
**categoria:** multi_norma · **seccion_sorteada_origen:** "CAP-S12 + EXT-S12"
**estrato:** primaria · **disclosure (verbatim):** GT 12.1 de Capitales: punto virgen, pero la Sección 12 (transitorias) es la familia del defecto adjudicado en CQN-014 (nodo del 12.3 con condicionamiento espurio); patrón de extracción documentado en la familia.

**cita_textual del GT:** "Las entidades financieras en funcionamiento al 01/06/24 que no cumplan con la integración
de la exigencia básica de capital conforme a lo previsto en el párrafo precedente y/o la exi-
gencia básica de capital desde el 01/01/25 según su Plan de negocios y proyecciones e in-
forme de autoevaluación del capital deberán presentar a la SEFYC un programa de encua-
dramiento dentro de los 20 días corridos siguientes a la registración o proyección de incum-
plimiento, respectivamente, el cual no deberá superar los 6 meses de plazo para cumplir con
la exigencia básica.
[...]
12.1.   Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2.
[...]
8802.11.00
[...]
Quedan exceptuadas las importaciones realizadas por empresas que presten
8802.20.10
servicios de aeronavegación.
[...]
10.10.2.1.   Pagos a la vista de importaciones de bienes cursados por personas
humanas o personas jurídicas que clasifiquen como MiPyMe según lo
dispuesto en las normas de "Determinación de la condición de micro,
pequeña y mediana empresa", en la medida que se trate de bienes
que hayan sido embarcados en origen a partir del 14/04/25 y las
posiciones arancelarias de los bienes no correspondan a aquellas
comprendidas en el punto 12.1."

**respuesta_breve del GT:** (a) Debe presentar a la SEFYC un programa de encuadramiento dentro de los 20 días corridos siguientes a la registración o proyección del incumplimiento, el cual no debe superar los 6 meses de plazo para cumplir con la exigencia básica. (b) No: la facilidad de pagos a la vista para MiPyMEs exige que las posiciones arancelarias no estén comprendidas en la lista con tratamiento específico, que incluye las posiciones de la partida 8802 (aeronaves); quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.

## 2. Síntoma del juez (verbatim, traza gate_cqn2)

`judge.step1`:

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Una entidad financiera que proyecta no alcanzar la integración de la exigencia básica de capital debe presentar un plan de regularización y saneamiento.",
   "central": true
  },
  {
   "enunciado": "El plazo para presentar el plan de regularización y saneamiento es dentro de los 30 días corridos siguientes al último día del mes al que corresponda el incumplimiento.",
   "central": true
  },
  {
   "enunciado": "La posición arancelaria NCM 8802 incluye las subpartidas 8802.11.00, 8802.12.10, 8802.12.90, 8802.20.10, 8802.20.21, 8802.20.22, 8802.20.90, 8802.30.10, 8802.30.21, 8802.30.29, 8802.30.31, 8802.30.39, 8802.30.90, 8802.40.10 y 8802.40.90.",
   "central": false
  },
  {
   "enunciado": "La posición arancelaria NCM 8802 está sujeta a arancel.",
   "central": true
  },
  {
   "enunciado": "Para operaciones embarcadas después del 14/04/25, existe una excepción que permite que el pago a la vista se concrete a partir de la fecha estimada de embarque más 15 días corridos cuando corresponde a porción de operación con pagos a la vista.",
   "central": true
  }
 ],
 "reportes_de_alcance": [
  "No se encontró en el Knowledge Graph información específica sobre qué debe presentar una entidad financiera que proyecta no alcanzar la integración de la exigencia básica de capital, ante quién, en qué plazo y con qué duración máxima (más allá del plazo de 30 días identificado).",
  "No se cuenta con detalles completos sobre la duración máxima del plan de regularización y saneamiento.",
  "No se cuenta con información sobre la autoridad específica ante la cual presentar el plan de regularización y saneamiento.",
  "No se encontró en el grafo información específica sobre si la excepción de pago a la vista (fecha de embarque más 15 días) aplica a MiPyMe.",
  "No se encontró en el grafo información específica sobre la posibilidad de pagar a la vista con registro de ingreso aduanero pendiente para bienes de la NCM 8802.",
  "No se encontró información sobre una excepción subjetiva específica para MiPyMe respecto de bienes de la partida 8802."
 ],
 "patas_de_la_pregunta": [
  "(a) Qué debe presentar la entidad financiera que proyecta no alcanzar la integración de la exigencia básica de capital",
  "(a) Ante quién debe presentarlo",
  "(a) En qué plazo debe presentarlo",
  "(a) Cuál es la duración máxima del instrumento a presentar",
  "(b) Si la posición arancelaria NCM 8802 permite el pago a la vista con registro de ingreso aduanero pendiente para importaciones embarcadas después del 14/04/25",
  "(b) Qué excepción subjetiva existe para ese tipo de bienes (aeronaves NCM 8802) en relación con MiPyMe"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "Una entidad financiera que proyecta no alcanzar la integración de la exigencia básica de capital debe presentar un plan de regularización y saneamiento.",
  "central": true,
  "verdict": "falso"
 },
 {
  "enunciado": "El plazo para presentar el plan de regularización y saneamiento es dentro de los 30 días corridos siguientes al último día del mes al que corresponda el incumplimiento.",
  "central": true,
  "verdict": "falso"
 },
 {
  "enunciado": "La posición arancelaria NCM 8802 incluye las subpartidas 8802.11.00, 8802.12.10, 8802.12.90, 8802.20.10, 8802.20.21, 8802.20.22, 8802.20.90, 8802.30.10, 8802.30.21, 8802.30.29, 8802.30.31, 8802.30.39, 8802.30.90, 8802.40.10 y 8802.40.90.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "La posición arancelaria NCM 8802 está sujeta a arancel.",
  "central": true,
  "verdict": "falso"
 },
 {
  "enunciado": "Para operaciones embarcadas después del 14/04/25, existe una excepción que permite que el pago a la vista se concrete a partir de la fecha estimada de embarque más 15 días corridos cuando corresponde a porción de operación con pagos a la vista.",
  "central": true,
  "verdict": "falso"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "(a) Qué debe presentar la entidad financiera que proyecta no alcanzar la integración de la exigencia básica de capital",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "(a) Ante quién debe presentarlo",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "(a) En qué plazo debe presentarlo",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "(a) Cuál es la duración máxima del instrumento a presentar",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "(b) Si la posición arancelaria NCM 8802 permite el pago a la vista con registro de ingreso aduanero pendiente para importaciones embarcadas después del 14/04/25",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "(b) Qué excepción subjetiva existe para ese tipo de bienes (aeronaves NCM 8802) en relación con MiPyMe",
  "cobertura": "no_cubierta"
 }
]
```

`judge.verdict`:

```json
{
 "correctitud": "incorrecta",
 "completitud": "parcial",
 "cita_documento_correcto": true,
 "cita_precision": "punto",
 "abstencion": null,
 "especulacion_en_prosa": null,
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [
   "La posición arancelaria NCM 8802 incluye las subpartidas 8802.11.00, 8802.12.10, 8802.12.90, 8802.20.10, 8802.20.21, 8802.20.22, 8802.20.90, 8802.30.10, 8802.30.21, 8802.30.29, 8802.30.31, 8802.30.39, 8802.30.90, 8802.40.10 y 8802.40.90."
  ],
  "n_centrales": 0,
  "n_secundarias": 1
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Afirmación central falsa: Una entidad financiera que proyecta no alcanzar la integración de la exigencia básica de capital debe presentar un plan de regularización y saneamiento.; El plazo para presentar el plan de regularización y saneamiento es dentro de los 30 días corridos siguientes al último día del mes al que corresponda el incumplimiento.; La posición arancelaria NCM 8802 está sujeta a arancel.; Para operaciones embarcadas después del 14/04/25, existe una excepción que permite que el pago a la vista se concrete a partir de la fecha estimada de embarque más 15 días corridos cuando corresponde a porción de operación con pagos a la vista.",
  "completitud": "Patas no cubiertas: (a) Qué debe presentar la entidad financiera que proyecta no alcanzar la integración de la exigencia básica de capital; (a) Ante quién debe presentarlo; (a) En qué plazo debe presentarlo; (a) Cuál es la duración máxima del instrumento a presentar; (b) Si la posición arancelaria NCM 8802 permite el pago a la vista con registro de ingreso aduanero pendiente para importaciones embarcadas después del 14/04/25; (b) Qué excepción subjetiva existe para ese tipo de bienes (aeronaves NCM 8802) en relación con MiPyMe",
  "citas": "El agente cita correctamente TO_capitales_minimos_actual.pdf (Punto 12.1) y TO_exterior_cambios_actual.pdf (Puntos 12.1 y 10.3), que corresponden a documentos del ground truth, con precisión a nivel punto."
 }
}
```

**Síntoma (resumen mecánico, filtro de build_falla_context): F = 5 (4 centrales) · P = 6 → NO VACÍO.**

## 3. Trayectoria

En `expediente_gate2_2.md`, sección "CQN2-011".

## 4. Homólogos / territorio

**Disclosure del sellado:** GT 12.1 de Capitales: punto virgen, pero la Sección 12 (transitorias) es la familia del defecto adjudicado en CQN-014 (nodo del 12.3 con condicionamiento espurio); patrón de extracción documentado en la familia.

**Territorio en varas previas:** el barrido mecánico de los numerales del GT sobre las 5 varas no devolvió líneas.

## 5. Tabla inicial de hechos (cero adjudicación)

**Claims reprobados:**
- CENTRAL `falso`: "Una entidad financiera que proyecta no alcanzar la integración de la exigencia básica de capital debe presentar un plan de regularización y saneamiento."
- CENTRAL `falso`: "El plazo para presentar el plan de regularización y saneamiento es dentro de los 30 días corridos siguientes al último día del mes al que corresponda el incumplimiento."
- secundario `no_soportado`: "La posición arancelaria NCM 8802 incluye las subpartidas 8802.11.00, 8802.12.10, 8802.12.90, 8802.20.10, 8802.20.21, 8802.20.22, 8802.20.90, 8802.30.10, 8802.30.21, 8802.30.29, 8802.30.31, 8802.30.39, 8802.30.90, 8802.40.10 y 8802.40.90."
- CENTRAL `falso`: "La posición arancelaria NCM 8802 está sujeta a arancel."
- CENTRAL `falso`: "Para operaciones embarcadas después del 14/04/25, existe una excepción que permite que el pago a la vista se concrete a partir de la fecha estimada de embarque más 15 días corridos cuando corresponde a porción de operación con pagos a la vista."

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| (a) Qué debe presentar la entidad financiera que proyecta no alcanzar la integración de la exigencia básica de capital | no_cubierta | 1, 2, 3, 4, 7, 9, 10, 11, 12, 13, 15 |
| (a) Ante quién debe presentarlo | no_cubierta | — |
| (a) En qué plazo debe presentarlo | no_cubierta | 2, 9, 10, 12 |
| (a) Cuál es la duración máxima del instrumento a presentar | no_cubierta | 1, 5, 9, 10, 12, 15 |
| (b) Si la posición arancelaria NCM 8802 permite el pago a la vista con registro de ingreso aduanero pendiente para importaciones embarcadas después del 14/04/25 | no_cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 |
| (b) Qué excepción subjetiva existe para ese tipo de bienes (aeronaves NCM 8802) en relación con MiPyMe | no_cubierta | 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15 |

**Descomposición del juez (step1, verbatim):**
- afirmación (central): "Una entidad financiera que proyecta no alcanzar la integración de la exigencia básica de capital debe presentar un plan de regularización y saneamiento."
- afirmación (central): "El plazo para presentar el plan de regularización y saneamiento es dentro de los 30 días corridos siguientes al último día del mes al que corresponda el incumplimiento."
- afirmación (no central): "La posición arancelaria NCM 8802 incluye las subpartidas 8802.11.00, 8802.12.10, 8802.12.90, 8802.20.10, 8802.20.21, 8802.20.22, 8802.20.90, 8802.30.10, 8802.30.21, 8802.30.29, 8802.30.31, 8802.30.39, 8802.30.90, 8802.40.10 y 8802.40.90."
- afirmación (central): "La posición arancelaria NCM 8802 está sujeta a arancel."
- afirmación (central): "Para operaciones embarcadas después del 14/04/25, existe una excepción que permite que el pago a la vista se concrete a partir de la fecha estimada de embarque más 15 días corridos cuando corresponde a porción de operación con pagos a la vista."
- reporte de alcance: "No se encontró en el Knowledge Graph información específica sobre qué debe presentar una entidad financiera que proyecta no alcanzar la integración de la exigencia básica de capital, ante quién, en qué plazo y con qué duración máxima (más allá del plazo de 30 días identificado)."
- reporte de alcance: "No se cuenta con detalles completos sobre la duración máxima del plan de regularización y saneamiento."
- reporte de alcance: "No se cuenta con información sobre la autoridad específica ante la cual presentar el plan de regularización y saneamiento."
- reporte de alcance: "No se encontró en el grafo información específica sobre si la excepción de pago a la vista (fecha de embarque más 15 días) aplica a MiPyMe."
- reporte de alcance: "No se encontró en el grafo información específica sobre la posibilidad de pagar a la vista con registro de ingreso aduanero pendiente para bienes de la NCM 8802."
- reporte de alcance: "No se encontró información sobre una excepción subjetiva específica para MiPyMe respecto de bienes de la partida 8802."


---

# CQN2-012 — [multi_norma] · estrato **solapada**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn2.json — el SELLADO)

**Pregunta:** Tras una fusión de entidades financieras: (a) ¿qué importe puede adicionarse a los efectos de la determinación de la responsabilidad patrimonial computable (RPC)? (b) ¿Cómo se calcula el total de integración (RPC) que la entidad informa como total de control en el régimen informativo sobre exigencia e integración de capitales mínimos?

**ground_truth_secciones:** ["11.2. (Capitales Mínimos)", "8.1.6. (R.I.-C.M.)"]
**tos_fuente:** ["TO_capitales_minimos_actual.pdf", "TO_regimen_informativo_contable_mensual_actual.pdf"]
**categoria:** multi_norma · **seccion_sorteada_origen:** "RIC-S8 + CAP-S11"
**estrato:** solapada · **disclosure (verbatim):** GT 8.1.6 ⊂ Sección 8 del RI, adjudicada dos veces en el gate CQN: CQN-007 (navegación; el nodo EVE del 8.1 existe sano) y CQN-009 (completitud_kg: el hermano 8.1.3/código 70700000 está AUSENTE de run_3). La cobertura del grafo sobre los códigos de la Sección 8 es conocida-parcial; el 8.1.6 puntual (fórmula RPC, 70200000) no fue adjudicado. Pata Capitales 11.2 (llave negativa): virgen.

**cita_textual del GT:** "11.2. Fusión de entidades financieras.
[...]
A los efectos de la determinación de la RPC, se podrá adicionar el importe correspondiente a
la llave de negocio negativa registrado en la partida específica en el rubro Previsiones del Pa-
sivo.
[...]
8.1.6. Código 70200000.
Responsabilidad patrimonial computable: (COn1-CDCOn1) + (CAn1-CDCAn1) + (PNc-CDPNc)"

**respuesta_breve del GT:** (a) Puede adicionarse el importe correspondiente a la llave de negocio negativa registrado en la partida específica del rubro Previsiones del Pasivo. (b) El total de control de responsabilidad patrimonial computable (código 70200000) se calcula como (COn1-CDCOn1) + (CAn1-CDCAn1) + (PNc-CDPNc).

## 2. Síntoma del juez (verbatim, traza gate_cqn2)

`judge.step1`:

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "La RPC se calcula en función de saldos de partidas admitidas al último día del mes.",
   "central": false
  },
  {
   "enunciado": "La integración diaria de capital se determina considerando la RPC del último día del mes anterior y cambios de valor del portafolio.",
   "central": false
  }
 ],
 "reportes_de_alcance": [
  "No se encontró información en el Knowledge Graph que responda específicamente a las preguntas formuladas.",
  "Se localizaron nodos relacionados con la responsabilidad patrimonial computable (RPC), la integración de capitales mínimos y operaciones de fusión de entidades financieras.",
  "No se identificaron disposiciones que especifiquen qué importe puede adicionarse a los efectos de la determinación de la RPC tras una fusión de entidades financieras.",
  "No se identificaron disposiciones que especifiquen cómo se calcula el total de integración (RPC) que la entidad informa como total de control en el régimen informativo sobre exigencia e integración de capitales mínimos.",
  "La información disponible no aborda específicamente los efectos de fusiones en estos cálculos."
 ],
 "patas_de_la_pregunta": [
  "Qué importe puede adicionarse a los efectos de la determinación de la RPC tras una fusión de entidades financieras",
  "Cómo se calcula el total de integración (RPC) que la entidad informa como total de control en el régimen informativo sobre exigencia e integración de capitales mínimos"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "La RPC se calcula en función de saldos de partidas admitidas al último día del mes.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "La integración diaria de capital se determina considerando la RPC del último día del mes anterior y cambios de valor del portafolio.",
  "central": false,
  "verdict": "no_soportado"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Qué importe puede adicionarse a los efectos de la determinación de la RPC tras una fusión de entidades financieras",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "Cómo se calcula el total de integración (RPC) que la entidad informa como total de control en el régimen informativo sobre exigencia e integración de capitales mínimos",
  "cobertura": "no_cubierta"
 }
]
```

`judge.verdict`:

```json
{
 "correctitud": "correcta",
 "completitud": "parcial",
 "cita_documento_correcto": false,
 "cita_precision": "ausente",
 "abstencion": null,
 "especulacion_en_prosa": null,
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [
   "La RPC se calcula en función de saldos de partidas admitidas al último día del mes.",
   "La integración diaria de capital se determina considerando la RPC del último día del mes anterior y cambios de valor del portafolio."
  ],
  "n_centrales": 0,
  "n_secundarias": 2
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Qué importe puede adicionarse a los efectos de la determinación de la RPC tras una fusión de entidades financieras; Cómo se calcula el total de integración (RPC) que la entidad informa como total de control en el régimen informativo sobre exigencia e integración de capitales mínimos",
  "citas": "El agente no presentó ninguna cita, por lo que no puede evaluarse si apunta a los documentos del ground truth."
 }
}
```

**Síntoma (resumen mecánico, filtro de build_falla_context): F = 2 (0 centrales) · P = 2 → NO VACÍO.**

## 3. Trayectoria

En `expediente_gate2_2.md`, sección "CQN2-012".

## 4. Homólogos / territorio

**Disclosure del sellado:** GT 8.1.6 ⊂ Sección 8 del RI, adjudicada dos veces en el gate CQN: CQN-007 (navegación; el nodo EVE del 8.1 existe sano) y CQN-009 (completitud_kg: el hermano 8.1.3/código 70700000 está AUSENTE de run_3). La cobertura del grafo sobre los códigos de la Sección 8 es conocida-parcial; el 8.1.6 puntual (fórmula RPC, 70200000) no fue adjudicado. Pata Capitales 11.2 (llave negativa): virgen.

**Territorio en varas previas:** el barrido mecánico de los numerales del GT sobre las 5 varas no devolvió líneas.

## 5. Tabla inicial de hechos (cero adjudicación)

**Claims reprobados:**
- secundario `no_soportado`: "La RPC se calcula en función de saldos de partidas admitidas al último día del mes."
- secundario `no_soportado`: "La integración diaria de capital se determina considerando la RPC del último día del mes anterior y cambios de valor del portafolio."

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Qué importe puede adicionarse a los efectos de la determinación de la RPC tras una fusión de entidades financieras | no_cubierta | 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14 |
| Cómo se calcula el total de integración (RPC) que la entidad informa como total de control en el régimen informativo sobre exigencia e integración de capitales mínimos | no_cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 |

**Descomposición del juez (step1, verbatim):**
- afirmación (no central): "La RPC se calcula en función de saldos de partidas admitidas al último día del mes."
- afirmación (no central): "La integración diaria de capital se determina considerando la RPC del último día del mes anterior y cambios de valor del portafolio."
- reporte de alcance: "No se encontró información en el Knowledge Graph que responda específicamente a las preguntas formuladas."
- reporte de alcance: "Se localizaron nodos relacionados con la responsabilidad patrimonial computable (RPC), la integración de capitales mínimos y operaciones de fusión de entidades financieras."
- reporte de alcance: "No se identificaron disposiciones que especifiquen qué importe puede adicionarse a los efectos de la determinación de la RPC tras una fusión de entidades financieras."
- reporte de alcance: "No se identificaron disposiciones que especifiquen cómo se calcula el total de integración (RPC) que la entidad informa como total de control en el régimen informativo sobre exigencia e integración de capitales mínimos."
- reporte de alcance: "La información disponible no aborda específicamente los efectos de fusiones en estos cálculos."


---

# CQN2-013 — [multi_norma] · estrato **solapada**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn2.json — el SELLADO)

**Pregunta:** (a) En el régimen informativo sobre exigencia e integración de capitales mínimos, ¿mediante qué expresión se calcula la exigencia de capital por riesgo de crédito? (b) Un residente debe pagar un servicio de asesoramiento (no comprendido en los conceptos con tratamiento especial) prestado a partir del 14/04/25 por una contraparte vinculada del exterior: ¿qué plazo debe transcurrir desde la prestación o devengamiento para poder acceder al mercado de cambios?

**ground_truth_secciones:** ["3.1.2. (R.I.-C.M.)", "13.2.7.1. (Exterior y Cambios)"]
**tos_fuente:** ["TO_regimen_informativo_contable_mensual_actual.pdf", "TO_exterior_cambios_actual.pdf"]
**categoria:** multi_norma · **seccion_sorteada_origen:** "RIC-S3 + EXT-S13"
**estrato:** solapada · **disclosure (verbatim):** Pata RI 3.1.2: match exacto con CQ-020, quemado en DOS varas y DOS grafos (control run_3, validación run_4); historia: su atribución secundaria se disolvió como FP del juez en la vara v3 (barrido léxico corregido). Pata Exterior 13.2.7.1 (90 días vinculadas): virgen. Pregunta nueva; solo una pata pisa territorio quemado.

**cita_textual del GT:** "Se determinará de acuerdo con la siguiente expresión:
CRC = (k x 0,08 x APRc) + INC
[...]
13.2.7. se trata de un servicio no comprendido en los puntos 13.2.1. a 13.2.5. que fue
provisto por una contraparte vinculada al residente y el pago se concreta:
13.2.7.1. una vez transcurrido un plazo de 90 (noventa) días corridos desde la
fecha de prestación o devengamiento del servicio si esa fecha tuvo lugar
a partir del 14/04/25."

**respuesta_breve del GT:** (a) La exigencia por riesgo de crédito se determina como CRC = (k x 0,08 x APRc) + INC. (b) Para servicios provistos por contrapartes vinculadas, prestados o devengados a partir del 14/04/25, el pago sólo puede concretarse una vez transcurridos 90 días corridos desde la fecha de prestación o devengamiento.

## 2. Síntoma del juez (verbatim, traza gate_cqn2)

`judge.step1`:

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "La exigencia de capital por riesgo de crédito se calcula mediante la expresión: C_RC = (k x 0,08 x APR_c) + INC",
   "central": true
  },
  {
   "enunciado": "Para servicios no comprendidos en los puntos 13.2.1 a 13.2.5, el plazo para acceder al mercado de cambios con contrapartes no vinculadas es de 90 días",
   "central": false
  },
  {
   "enunciado": "Para un servicio de asesoramiento prestado a partir del 14/04/25 por una contraparte vinculada del exterior, el plazo requerido desde la prestación o devengamiento para acceder al mercado de cambios es de 180 días corridos",
   "central": true
  },
  {
   "enunciado": "Los servicios de asesoramiento no comprendidos en los conceptos con tratamiento especial no están incluidos en los puntos 13.2.1 a 13.2.5",
   "central": false
  }
 ],
 "reportes_de_alcance": [
  "La respuesta fue marcada como no respondible (respondible: false), lo que indica que el sistema no pudo confirmar con certeza la información provista.",
  "El plazo de 180 días para contrapartes vinculadas se deduce por inferencia de la regulación, no de una norma explícita citada directamente para ese caso."
 ],
 "patas_de_la_pregunta": [
  "Expresión mediante la cual se calcula la exigencia de capital por riesgo de crédito en el régimen informativo sobre exigencia e integración de capitales mínimos",
  "Plazo que debe transcurrir desde la prestación o devengamiento de un servicio de asesoramiento (no comprendido en conceptos con tratamiento especial) prestado a partir del 14/04/25 por una contraparte vinculada del exterior para que un residente pueda acceder al mercado de cambios"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "La exigencia de capital por riesgo de crédito se calcula mediante la expresión: C_RC = (k x 0,08 x APR_c) + INC",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Para servicios no comprendidos en los puntos 13.2.1 a 13.2.5, el plazo para acceder al mercado de cambios con contrapartes no vinculadas es de 90 días",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Para un servicio de asesoramiento prestado a partir del 14/04/25 por una contraparte vinculada del exterior, el plazo requerido desde la prestación o devengamiento para acceder al mercado de cambios es de 180 días corridos",
  "central": true,
  "verdict": "falso"
 },
 {
  "enunciado": "Los servicios de asesoramiento no comprendidos en los conceptos con tratamiento especial no están incluidos en los puntos 13.2.1 a 13.2.5",
  "central": false,
  "verdict": "no_soportado"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Expresión mediante la cual se calcula la exigencia de capital por riesgo de crédito en el régimen informativo sobre exigencia e integración de capitales mínimos",
  "cobertura": "cubierta"
 },
 {
  "pata": "Plazo que debe transcurrir desde la prestación o devengamiento de un servicio de asesoramiento (no comprendido en conceptos con tratamiento especial) prestado a partir del 14/04/25 por una contraparte vinculada del exterior para que un residente pueda acceder al mercado de cambios",
  "cobertura": "cubierta"
 }
]
```

`judge.verdict`:

```json
{
 "correctitud": "incorrecta",
 "completitud": "completa",
 "cita_documento_correcto": true,
 "cita_precision": "punto",
 "abstencion": null,
 "especulacion_en_prosa": null,
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [
   "Para servicios no comprendidos en los puntos 13.2.1 a 13.2.5, el plazo para acceder al mercado de cambios con contrapartes no vinculadas es de 90 días",
   "Los servicios de asesoramiento no comprendidos en los conceptos con tratamiento especial no están incluidos en los puntos 13.2.1 a 13.2.5"
  ],
  "n_centrales": 0,
  "n_secundarias": 2
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Afirmación central falsa: Para un servicio de asesoramiento prestado a partir del 14/04/25 por una contraparte vinculada del exterior, el plazo requerido desde la prestación o devengamiento para acceder al mercado de cambios es de 180 días corridos",
  "completitud": "Todas las patas cubiertas.",
  "citas": "El agente cita TO_regimen_informativo_contable_mensual_actual.pdf (Punto 3.1) y TO_exterior_cambios_actual.pdf (Punto 13.2), ambos correspondientes a los ground truth sections, con precisión a nivel punto."
 }
}
```

**Síntoma (resumen mecánico, filtro de build_falla_context): F = 3 (1 centrales) · P = 0 → NO VACÍO.**

## 3. Trayectoria

En `expediente_gate2_2.md`, sección "CQN2-013".

## 4. Homólogos / territorio

**Disclosure del sellado:** Pata RI 3.1.2: match exacto con CQ-020, quemado en DOS varas y DOS grafos (control run_3, validación run_4); historia: su atribución secundaria se disolvió como FP del juez en la vara v3 (barrido léxico corregido). Pata Exterior 13.2.7.1 (90 días vinculadas): virgen. Pregunta nueva; solo una pata pisa territorio quemado.

**Territorio en varas previas** (barrido mecánico):

- GT `3.1.2. (R.I.-C.M.)` (numeral 3.1.2) en **casos_control.md** — 1 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L65): - **Ground-truth secciones:** Capitales, Punto 2.1 · Régimen Informativo, Punto 3.1.2 · Régimen Informativo, Punto 1.1 (frecuencia).

## 5. Tabla inicial de hechos (cero adjudicación)

**Claims reprobados:**
- secundario `no_soportado`: "Para servicios no comprendidos en los puntos 13.2.1 a 13.2.5, el plazo para acceder al mercado de cambios con contrapartes no vinculadas es de 90 días"
- CENTRAL `falso`: "Para un servicio de asesoramiento prestado a partir del 14/04/25 por una contraparte vinculada del exterior, el plazo requerido desde la prestación o devengamiento para acceder al mercado de cambios es de 180 días corridos"
- secundario `no_soportado`: "Los servicios de asesoramiento no comprendidos en los conceptos con tratamiento especial no están incluidos en los puntos 13.2.1 a 13.2.5"

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Expresión mediante la cual se calcula la exigencia de capital por riesgo de crédito en el régimen informativo sobre exigencia e integración de capitales mínimos | cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 |
| Plazo que debe transcurrir desde la prestación o devengamiento de un servicio de asesoramiento (no comprendido en conceptos con tratamiento especial) prestado a partir del 14/04/25 por una contraparte vinculada del exterior para que un residente pueda acceder al mercado de cambios | cubierta | 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 |

**Descomposición del juez (step1, verbatim):**
- afirmación (central): "La exigencia de capital por riesgo de crédito se calcula mediante la expresión: C_RC = (k x 0,08 x APR_c) + INC"
- afirmación (no central): "Para servicios no comprendidos en los puntos 13.2.1 a 13.2.5, el plazo para acceder al mercado de cambios con contrapartes no vinculadas es de 90 días"
- afirmación (central): "Para un servicio de asesoramiento prestado a partir del 14/04/25 por una contraparte vinculada del exterior, el plazo requerido desde la prestación o devengamiento para acceder al mercado de cambios es de 180 días corridos"
- afirmación (no central): "Los servicios de asesoramiento no comprendidos en los conceptos con tratamiento especial no están incluidos en los puntos 13.2.1 a 13.2.5"
- reporte de alcance: "La respuesta fue marcada como no respondible (respondible: false), lo que indica que el sistema no pudo confirmar con certeza la información provista."
- reporte de alcance: "El plazo de 180 días para contrapartes vinculadas se deduce por inferencia de la regulación, no de una norma explícita citada directamente para ese caso."


---

# CQN2-014 — [cadena_restriccion_excepcion] · estrato **primaria**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn2.json — el SELLADO)

**Pregunta:** En la clasificación de deudores de la cartera para consumo o vivienda, la regla es que no hay cumplimiento de las obligaciones cuando se recurre a nuevas financiaciones o refinanciaciones para cancelar obligaciones preexistentes. ¿Qué excepción rige para las refinanciaciones otorgadas a productores en el marco de la Ley de Emergencia Agropecuaria, y qué límites tiene ese tratamiento?

**ground_truth_secciones:** ["7.1."]
**tos_fuente:** ["TO_clasificacion_deudores_actual.pdf"]
**categoria:** cadena_restriccion_excepcion · **seccion_sorteada_origen:** "CLA-S7 (candidata 1 del stream de cadenas)"
**estrato:** primaria · **disclosure (verbatim):** Clas 7.1, hermana de 7.2.1 (CQ-019 ×3) y 10.1 (×3); punto propio virgen.

**cita_textual del GT:** "Se entiende que el cumplimiento de las obligaciones a que se refieren las citadas pautas tiene
lugar cuando no se recurra a nuevas financiaciones o refinanciaciones destinadas a cancelar
obligaciones preexistentes, cualquiera sea la modalidad (prórrogas, esperas, ampliaciones de
plazo o márgenes -sean tales modalidades expresas o tácitas-, disminuciones en los importes
de las cuotas o pagos, renovaciones, reestructuraciones, etc.). En el caso de refinanciaciones,
a fin de determinar una mejora en la clasificación del deudor, corresponderá tener en cuenta las
pautas específicas previstas en cada una de las categorías.
A esos efectos, no se considerarán dentro de ese concepto las refinanciaciones otorgadas a
productores cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emer-
gencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en
cuenta la mora en el atraso de sus obligaciones para el momento en que concluya la vigencia
de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar
mejoramiento de la clasificación asignada al cliente en función de su situación individual, pre-
existente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella."

**respuesta_breve del GT:** Esas refinanciaciones no se consideran dentro del concepto de refinanciación, pero a los fines de la clasificación debe tenerse en cuenta la mora en el atraso de las obligaciones al concluir la vigencia de la emergencia declarada. Además, el tratamiento no puede implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.

## 2. Síntoma del juez (verbatim, traza gate_cqn2)

`judge.step1`:

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Las refinanciaciones otorgadas a productores en el marco de la Ley de Emergencia Agropecuaria no se considerarán como refinanciación a los efectos de la clasificación de deudores.",
   "central": true
  },
  {
   "enunciado": "Esta excepción aplica cuando la refinanciación resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria.",
   "central": true
  },
  {
   "enunciado": "A los fines de la clasificación, deberá tenerse en cuenta la mora en el atraso de las obligaciones para el momento en que concluya la vigencia de la emergencia declarada en materia de Ley de Emergencia Agropecuaria.",
   "central": true
  },
  {
   "enunciado": "Una vez que concluya la emergencia, se evaluará la mora existente en ese momento para determinar la clasificación del deudor.",
   "central": true
  },
  {
   "enunciado": "La regla general establece que no hay cumplimiento de las obligaciones cuando se recurre a nuevas financiaciones o refinanciaciones para cancelar obligaciones preexistentes.",
   "central": false
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "Excepción que rige para las refinanciaciones otorgadas a productores en el marco de la Ley de Emergencia Agropecuaria",
  "Límites que tiene ese tratamiento excepcional"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "Las refinanciaciones otorgadas a productores en el marco de la Ley de Emergencia Agropecuaria no se considerarán como refinanciación a los efectos de la clasificación de deudores.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Esta excepción aplica cuando la refinanciación resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "A los fines de la clasificación, deberá tenerse en cuenta la mora en el atraso de las obligaciones para el momento en que concluya la vigencia de la emergencia declarada en materia de Ley de Emergencia Agropecuaria.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Una vez que concluya la emergencia, se evaluará la mora existente en ese momento para determinar la clasificación del deudor.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La regla general establece que no hay cumplimiento de las obligaciones cuando se recurre a nuevas financiaciones o refinanciaciones para cancelar obligaciones preexistentes.",
  "central": false,
  "verdict": "verdadero"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Excepción que rige para las refinanciaciones otorgadas a productores en el marco de la Ley de Emergencia Agropecuaria",
  "cobertura": "cubierta"
 },
 {
  "pata": "Límites que tiene ese tratamiento excepcional",
  "cobertura": "no_cubierta"
 }
]
```

`judge.verdict`:

```json
{
 "correctitud": "correcta",
 "completitud": "parcial",
 "cita_documento_correcto": true,
 "cita_precision": "punto",
 "abstencion": null,
 "especulacion_en_prosa": null,
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [],
  "n_centrales": 0,
  "n_secundarias": 0
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Límites que tiene ese tratamiento excepcional",
  "citas": "El agente cita correctamente el Punto 7.1 del TO de clasificación de deudores, que es el ground truth section indicado en el referente."
 }
}
```

**Síntoma (resumen mecánico, filtro de build_falla_context): F = 0 (0 centrales) · P = 1 → NO VACÍO.**

## 3. Trayectoria

En `expediente_gate2_2.md`, sección "CQN2-014".

## 4. Homólogos / territorio

**Disclosure del sellado:** Clas 7.1, hermana de 7.2.1 (CQ-019 ×3) y 10.1 (×3); punto propio virgen.

**Territorio en varas previas** (barrido mecánico):

- GT `7.1.` (numeral 7.1) en **casos_gate_cqn.md** — 2 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L253): - **Génesis del claim falso:** el agente estiró el nodo del RI 7.1
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L255): "Punto 7.1. Normas de procedimiento") a regla de determinación ("suma… junto con otras

## 5. Tabla inicial de hechos (cero adjudicación)

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Excepción que rige para las refinanciaciones otorgadas a productores en el marco de la Ley de Emergencia Agropecuaria | cubierta | 2, 3, 4, 5, 6, 7, 9 |
| Límites que tiene ese tratamiento excepcional | no_cubierta | — |

**Descomposición del juez (step1, verbatim):**
- afirmación (central): "Las refinanciaciones otorgadas a productores en el marco de la Ley de Emergencia Agropecuaria no se considerarán como refinanciación a los efectos de la clasificación de deudores."
- afirmación (central): "Esta excepción aplica cuando la refinanciación resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria."
- afirmación (central): "A los fines de la clasificación, deberá tenerse en cuenta la mora en el atraso de las obligaciones para el momento en que concluya la vigencia de la emergencia declarada en materia de Ley de Emergencia Agropecuaria."
- afirmación (central): "Una vez que concluya la emergencia, se evaluará la mora existente en ese momento para determinar la clasificación del deudor."
- afirmación (no central): "La regla general establece que no hay cumplimiento de las obligaciones cuando se recurre a nuevas financiaciones o refinanciaciones para cancelar obligaciones preexistentes."


---

# CQN2-015 — [cadena_restriccion_excepcion] · estrato **primaria**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn2.json — el SELLADO)

**Pregunta:** Al determinar el capital mínimo por riesgo de crédito, ¿qué piso rige para el ponderador de riesgo de una exposición con un deudor no calificado, y qué exposiciones están exceptuadas de ese piso?

**ground_truth_secciones:** ["2.5.4.", "2.12.2.2.", "2.12.2.3."]
**tos_fuente:** ["TO_capitales_minimos_actual.pdf"]
**categoria:** cadena_restriccion_excepcion · **seccion_sorteada_origen:** "CAP-S2 (candidata 2 del stream de cadenas)"
**estrato:** primaria · **disclosure (verbatim):** Cap 2.5.4/2.12.2.x, hermanas de 2.1 (CQ-020) y 2.3.1 (CQ-019 ×3); puntos propios vírgenes.

**cita_textual del GT:** "Ninguna exposición con deudores no calificados podrá recibir un ponderador de riesgo
menor que el que se aplica al país de constitución, excepto que se trate de las exposi-
ciones a que se refieren los puntos 2.12.2.2. y 2.12.2.3.
[...]
2.12.2.2. Al Gobierno Nacional y a los gobiernos provinciales y municipa-
les y de la Ciudad Autónoma de Buenos Aires (CABA) en pe-
sos, cuando su fuente de fondos sea en esa moneda.                       0
[...]
2.12.2.3. Al sector público no financiero por financiaciones otorgadas a
beneficiarios de la seguridad social o a empleados públicos –en
ambos casos, con código de descuento–, en la medida que di-
chas operaciones estén denominadas en pesos, la fuente de
fondos sea en esa moneda y las cuotas de todas las financia-
ciones de la entidad que cuenten con sistema de amortización
periódica no excedan, al momento de los acuerdos, del 30% de
los ingresos del deudor y/o, en su caso, de los codeudores.              0"

**respuesta_breve del GT:** Como regla, ninguna exposición con deudores no calificados puede recibir un ponderador de riesgo menor que el que se aplica al país de constitución. Quedan exceptuadas las exposiciones en pesos —con fuente de fondos en esa moneda— al Gobierno Nacional, a los gobiernos provinciales y municipales y a la CABA, y las financiaciones al sector público no financiero a beneficiarios de la seguridad social o empleados públicos con código de descuento, denominadas en pesos, con fuente de fondos en pesos y cuotas que no excedan al momento de los acuerdos el 30 % de los ingresos del deudor y/o codeudores.

## 2. Síntoma del juez (verbatim, traza gate_cqn2)

`judge.step1`:

```json
{
 "afirmaciones_verificables": [],
 "reportes_de_alcance": [
  "No se encontró en el Knowledge Graph información que especifique explícitamente cuál es el piso de ponderador de riesgo que rige para exposiciones con deudores no calificados.",
  "No se encontró en el Knowledge Graph información sobre qué exposiciones están exceptuadas de ese piso para deudores no calificados.",
  "Se identificaron múltiples restricciones sobre ponderadores de riesgo para diferentes tipos de exposiciones (MIPYME, personas humanas, entidades financieras, titulizaciones, etc.).",
  "No se localizó la regla general aplicable a deudores sin calificación crediticia."
 ],
 "patas_de_la_pregunta": [
  "Piso del ponderador de riesgo para exposiciones con deudores no calificados en el capital mínimo por riesgo de crédito",
  "Exposiciones exceptuadas de ese piso"
 ]
}
```

`judge.step2.verificaciones`:

```json
[]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Piso del ponderador de riesgo para exposiciones con deudores no calificados en el capital mínimo por riesgo de crédito",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "Exposiciones exceptuadas de ese piso",
  "cobertura": "no_cubierta"
 }
]
```

`judge.verdict`:

```json
{
 "correctitud": "correcta",
 "completitud": "parcial",
 "cita_documento_correcto": false,
 "cita_precision": "ausente",
 "abstencion": null,
 "especulacion_en_prosa": null,
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [],
  "n_centrales": 0,
  "n_secundarias": 0
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Piso del ponderador de riesgo para exposiciones con deudores no calificados en el capital mínimo por riesgo de crédito; Exposiciones exceptuadas de ese piso",
  "citas": "El agente no presentó ninguna cita."
 }
}
```

**Síntoma (resumen mecánico, filtro de build_falla_context): F = 0 (0 centrales) · P = 2 → NO VACÍO.**

## 3. Trayectoria

En `expediente_gate2_2.md`, sección "CQN2-015".

## 4. Homólogos / territorio

**Disclosure del sellado:** Cap 2.5.4/2.12.2.x, hermanas de 2.1 (CQ-020) y 2.3.1 (CQ-019 ×3); puntos propios vírgenes.

**Territorio en varas previas:** el barrido mecánico de los numerales del GT sobre las 5 varas no devolvió líneas.

## 5. Tabla inicial de hechos (cero adjudicación)

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Piso del ponderador de riesgo para exposiciones con deudores no calificados en el capital mínimo por riesgo de crédito | no_cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 |
| Exposiciones exceptuadas de ese piso | no_cubierta | 1, 2, 3, 5, 9, 10, 12 |

**Descomposición del juez (step1, verbatim):**
- reporte de alcance: "No se encontró en el Knowledge Graph información que especifique explícitamente cuál es el piso de ponderador de riesgo que rige para exposiciones con deudores no calificados."
- reporte de alcance: "No se encontró en el Knowledge Graph información sobre qué exposiciones están exceptuadas de ese piso para deudores no calificados."
- reporte de alcance: "Se identificaron múltiples restricciones sobre ponderadores de riesgo para diferentes tipos de exposiciones (MIPYME, personas humanas, entidades financieras, titulizaciones, etc.)."
- reporte de alcance: "No se localizó la regla general aplicable a deudores sin calificación crediticia."
