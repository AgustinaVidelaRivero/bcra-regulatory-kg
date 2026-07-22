# Expediente de adjudicación — GATE CQN (la última vara) — parte 1

Fecha: 2026-07-17. SOLO LECTURA; escrituras: los 2 archivos del expediente. **Ni el
verificador ni S1 corrieron sobre este material — SELLADO POR INEXISTENCIA: sus
veredictos no existen y no existirán hasta el commit de la vara.** Cero adjudicación:
hechos verbatim con ruta de origen.

Casos: las 10 fallas con síntoma no vacío del censo (censo_gate_cqn.md). Fuentes:
`queries/eval_set_cqn.json` (el SELLADO; el runtime solo duplica un campo),
`posthoc_run/traces/gate_cqn/run_3/{CQN}.json`, barrido mecánico de territorio sobre las
4 varas (regex del punto con guardas de dígito).

Partes: 1 = secciones 1-2-4-5; 2 = trayectorias completas (sección 3).


---

# CQN-001 — [factual_directa] · estrato **solapada**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn.json — el SELLADO)

**Pregunta:** ¿Qué monto mensual máximo puede comprar una persona humana residente, sin conformidad previa del BCRA, para la formación de activos externos, la remisión de ayuda familiar y la operatoria con derivados?

**pregunta_original (preservada):** ¿Qué monto mensual máximo puede comprar una persona humana residente, sin conformidad previa del BCRA, para la formación de activos externos bajo modalidades distintas de billetes y depósitos, la remisión de ayuda familiar o la operatoria con derivados?

**ground_truth_secciones:** ["TO_exterior_cambios_actual.pdf Punto 3.9"]
**tos_fuente:** ["TO_exterior_cambios_actual.pdf"]
**categoria_generacion:** factual_directa
**estrato:** solapada · **disclosure:** GT compartido con CQ-034 (gate) — estrato solapado. Redacción ajustada (la original queda en pregunta_original); la cita queda intacta. Respuesta esperada: USD 200 mensuales — el sub-tope de efectivo (USD 100) NO se exige.

**cita_textual del GT:** "para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de con- cepto A05) en la medida que no encuadre en el punto 3.12.1., sin la conformidad previa del BCRA, en la medida que se cumplan la totalidad de los siguientes requisitos: 3.9.1. El cliente no supere, en el mes calendario en el conjunto de las entidades y por el conjunto de los conceptos señalados, el equivalente a USD 200 (dólares estadounidenses doscientos)."

**respuesta_breve del GT:** El límite es el equivalente a USD 200 por mes calendario, computado en el conjunto de las entidades y por el conjunto de los conceptos señalados. Si la operación se hace con efectivo, el monto no puede superar el equivalente a USD 100 mensuales.

## 2. Síntoma del juez (verbatim, traza gate_cqn)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Existe un límite mensual de USD 100 para compra en efectivo en ciertos casos para personas humanas residentes",
   "central": false
  },
  {
   "enunciado": "Existe un límite anual de USD 36.000 para personas humanas en algunos mecanismos",
   "central": false
  }
 ],
 "reportes_de_alcance": [
  "No se encontró en el Knowledge Graph información específica que detalle un monto mensual máximo único para las tres operaciones mencionadas (formación de activos externos, remisión de ayuda familiar y operatoria con derivados) sin conformidad previa del BCRA",
  "Se identificaron referencias a estas operaciones en el grafo, pero los detalles de los límites mensuales específicos no fueron accesibles en las búsquedas realizadas",
  "No se pudo confirmar un monto mensual máximo único que aplique a las tres operaciones solicitadas sin conformidad previa del BCRA"
 ],
 "patas_de_la_pregunta": [
  "Monto mensual máximo que puede comprar una persona humana residente sin conformidad previa del BCRA para la formación de activos externos",
  "Monto mensual máximo que puede comprar una persona humana residente sin conformidad previa del BCRA para la remisión de ayuda familiar",
  "Monto mensual máximo que puede comprar una persona humana residente sin conformidad previa del BCRA para la operatoria con derivados",
  "Si existe un monto mensual máximo único que aplique conjuntamente a las tres operaciones"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "Existe un límite mensual de USD 100 para compra en efectivo en ciertos casos para personas humanas residentes",
  "central": false,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Existe un límite anual de USD 36.000 para personas humanas en algunos mecanismos",
  "central": false,
  "verdict": "no_soportado"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Monto mensual máximo que puede comprar una persona humana residente sin conformidad previa del BCRA para la formación de activos externos",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "Monto mensual máximo que puede comprar una persona humana residente sin conformidad previa del BCRA para la remisión de ayuda familiar",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "Monto mensual máximo que puede comprar una persona humana residente sin conformidad previa del BCRA para la operatoria con derivados",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "Si existe un monto mensual máximo único que aplique conjuntamente a las tres operaciones",
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
  "secundarias": [
   "Existe un límite anual de USD 36.000 para personas humanas en algunos mecanismos"
  ],
  "n_centrales": 0,
  "n_secundarias": 1
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Monto mensual máximo que puede comprar una persona humana residente sin conformidad previa del BCRA para la formación de activos externos; Monto mensual máximo que puede comprar una persona humana residente sin conformidad previa del BCRA para la remisión de ayuda familiar; Monto mensual máximo que puede comprar una persona humana residente sin conformidad previa del BCRA para la operatoria con derivados; Si existe un monto mensual máximo único que aplique conjuntamente a las tres operaciones",
  "citas": "El agente cita el documento correcto (TO_exterior_cambios_actual.pdf) pero apunta al Punto 3.10, mientras que el referente corresponde al Punto 3.9, por lo que la precisión es de nivel punto aunque erróneo."
 }
}
```

**Síntoma (resumen mecánico, mismo filtro que build_falla_context): F = 1 claims reprobados (0 centrales) · P = 4 patas no cubiertas → síntoma NO VACÍO.**

## 3. Trayectoria

En la parte 2 (`expediente_gate_2.md`, sección "CQN-001").

## 4. Homólogos / territorio

**Disclosure del eval set (verbatim):** GT compartido con CQ-034 (gate) — estrato solapado. Redacción ajustada (la original queda en pregunta_original); la cita queda intacta. Respuesta esperada: USD 200 mensuales — el sub-tope de efectivo (USD 100) NO se exige.

**Territorio en varas previas** (barrido mecánico; cada entrada rotulada):

- GT `TO_exterior_cambios_actual.pdf Punto 3.9` (punto 3.9) en **casos_control.md** — 2 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L43): - **Ground-truth secciones:** Punto 3.8 (billetes/depósitos, conceptos A07 y A09) · Punto 3.9 (otras modalidades, ayuda familiar, derivados).
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L44): - **Atribución humana (re-scopeada 2026-07-15, vara v3):** defecto del grafo → **`{context_recall, completitud_kg}`**, PRIMARIA, **re-scopeada a las DOS patas faltantes**: (i) lími

## 5. Tabla inicial de hechos (cero adjudicación)

**Claims reprobados en juego:**
- secundario `no_soportado`: "Existe un límite anual de USD 36.000 para personas humanas en algunos mecanismos"

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Monto mensual máximo que puede comprar una persona humana residente sin conformidad previa del BCRA para la formación de activos externos | no_cubierta | 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13 |
| Monto mensual máximo que puede comprar una persona humana residente sin conformidad previa del BCRA para la remisión de ayuda familiar | no_cubierta | 1, 2, 3, 4, 5, 6, 8, 9, 12, 13, 14, 15 |
| Monto mensual máximo que puede comprar una persona humana residente sin conformidad previa del BCRA para la operatoria con derivados | no_cubierta | 1, 2, 3, 4, 5, 6, 8, 9, 12, 13 |
| Si existe un monto mensual máximo único que aplique conjuntamente a las tres operaciones | no_cubierta | 1, 2, 3, 8, 12 |

**Descomposición del juez (qué dice la respuesta, verbatim step1):**
- afirmación (no central): "Existe un límite mensual de USD 100 para compra en efectivo en ciertos casos para personas humanas residentes"
- afirmación (no central): "Existe un límite anual de USD 36.000 para personas humanas en algunos mecanismos"
- reporte de alcance: "No se encontró en el Knowledge Graph información específica que detalle un monto mensual máximo único para las tres operaciones mencionadas (formación de activos externos, remisión de ayuda familiar y operatoria con derivados) sin conformidad previa del BCRA"
- reporte de alcance: "Se identificaron referencias a estas operaciones en el grafo, pero los detalles de los límites mensuales específicos no fueron accesibles en las búsquedas realizadas"
- reporte de alcance: "No se pudo confirmar un monto mensual máximo único que aplique a las tres operaciones solicitadas sin conformidad previa del BCRA"


---

# CQN-006 — [factual_directa] · estrato **primaria**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn.json — el SELLADO)

**Pregunta:** ¿En qué plazo debe un sujeto obligado reintegrar al usuario de servicios financieros los importes que le cobró indebidamente?

**ground_truth_secciones:** ["TO_proteccion_usuarios_servicios_financieros_actual.pdf Punto 2.3"]
**tos_fuente:** ["TO_proteccion_usuarios_servicios_financieros_actual.pdf"]
**categoria_generacion:** factual_directa
**estrato:** primaria · **disclosure:** respuesta de dos ramas (10 días tras reclamo / 5 tras constatación) — la vara exigirá ambas

**cita_textual del GT:** "deberá serle reintegrado dentro de: - los diez (10) días hábiles siguientes al momento de la presentación del re- clamo ante el sujeto obligado, de conformidad con las previsiones del punto 3.1.6.; o - los cinco (5) días hábiles siguientes al momento de constatarse tal circuns- tancia por el sujeto obligado o por la fiscalización que realice la SEFYC."

**respuesta_breve del GT:** El reintegro debe hacerse dentro de los diez (10) días hábiles siguientes a la presentación del reclamo ante el sujeto obligado, o dentro de los cinco (5) días hábiles siguientes al momento en que la circunstancia sea constatada por el propio sujeto obligado o por la fiscalización de la SEFyC.

## 2. Síntoma del juez (verbatim, traza gate_cqn)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "El sujeto obligado debe reintegrar los importes cobrados indebidamente dentro de los diez (10) días hábiles siguientes a la presentación del reclamo ante el sujeto obligado.",
   "central": true
  },
  {
   "enunciado": "El sujeto obligado debe reintegrar los importes cobrados indebidamente dentro de los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por el sujeto obligado.",
   "central": true
  },
  {
   "enunciado": "El sujeto obligado debe reintegrar los importes cobrados indebidamente dentro de los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por la fiscalización de la SEFYC.",
   "central": true
  },
  {
   "enunciado": "La obligación de reintegro aplica a importes cobrados o adeudados por conceptos como tasas de interés, comisiones y/o cargos sin cumplimiento de lo previsto.",
   "central": false
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "Plazo en que el sujeto obligado debe reintegrar al usuario de servicios financieros los importes cobrados indebidamente"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "El sujeto obligado debe reintegrar los importes cobrados indebidamente dentro de los diez (10) días hábiles siguientes a la presentación del reclamo ante el sujeto obligado.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "El sujeto obligado debe reintegrar los importes cobrados indebidamente dentro de los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por el sujeto obligado.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "El sujeto obligado debe reintegrar los importes cobrados indebidamente dentro de los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por la fiscalización de la SEFYC.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La obligación de reintegro aplica a importes cobrados o adeudados por conceptos como tasas de interés, comisiones y/o cargos sin cumplimiento de lo previsto.",
  "central": false,
  "verdict": "no_soportado"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Plazo en que el sujeto obligado debe reintegrar al usuario de servicios financieros los importes cobrados indebidamente",
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
   "La obligación de reintegro aplica a importes cobrados o adeudados por conceptos como tasas de interés, comisiones y/o cargos sin cumplimiento de lo previsto."
  ],
  "n_centrales": 0,
  "n_secundarias": 1
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "La cita apunta al documento correcto (TO_proteccion_usuarios_servicios_financieros_actual.pdf) con precisión a nivel punto (Punto 2.3), coincidiendo con el ground truth."
 }
}
```

**Síntoma (resumen mecánico, mismo filtro que build_falla_context): F = 1 claims reprobados (0 centrales) · P = 0 patas no cubiertas → síntoma NO VACÍO.**

## 3. Trayectoria

En la parte 2 (`expediente_gate_2.md`, sección "CQN-006").

## 4. Homólogos / territorio

**Disclosure del eval set (verbatim):** respuesta de dos ramas (10 días tras reclamo / 5 tras constatación) — la vara exigirá ambas

**Territorio en varas previas** (barrido mecánico; cada entrada rotulada):

- GT `TO_proteccion_usuarios_servicios_financieros_actual.pdf Punto 2.3` (punto 2.3) en **casos_validacion.md** — 4 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L94): incobrabilidad**"; provenance Capitales "Sección 2 > Punto 2.3"; edge `definido_por` →
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L101): - "2.3.1": **0 en properties y 0 en provenances** de run_2 (verificaciones §2a-v).
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L220): declarado**; la respuesta correcta es el 2.3.1 (netos, sin deducir la de situación
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L252): 2. **Portador del 2.3 inalcanzable por singular/plural** (run_2 —
- GT `TO_proteccion_usuarios_servicios_financieros_actual.pdf Punto 2.3` (punto 2.3) en **casos_dev_v7.md** — 4 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L114): nodo `comision_por_precancelacion` (Punto 2.3.2.1, expuesto en los pasos 1, 3, 4, 6 y 7),
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L129): JUEZ, sin par**: es una inferencia correcta del 2.3.2.1 — la restricción es solo para la
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L150): optativa** (en run_2 Y en run_4 — el mismo punto, dos pipelines distintos) y el **2.3.2.1
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L160): - Criterio "de ambos el mayor" del 2.3.2.1 amputado (run_4).

## 5. Tabla inicial de hechos (cero adjudicación)

**Claims reprobados en juego:**
- secundario `no_soportado`: "La obligación de reintegro aplica a importes cobrados o adeudados por conceptos como tasas de interés, comisiones y/o cargos sin cumplimiento de lo previsto."

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Plazo en que el sujeto obligado debe reintegrar al usuario de servicios financieros los importes cobrados indebidamente | cubierta | 1, 2, 3 |

**Descomposición del juez (qué dice la respuesta, verbatim step1):**
- afirmación (central): "El sujeto obligado debe reintegrar los importes cobrados indebidamente dentro de los diez (10) días hábiles siguientes a la presentación del reclamo ante el sujeto obligado."
- afirmación (central): "El sujeto obligado debe reintegrar los importes cobrados indebidamente dentro de los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por el sujeto obligado."
- afirmación (central): "El sujeto obligado debe reintegrar los importes cobrados indebidamente dentro de los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por la fiscalización de la SEFYC."
- afirmación (no central): "La obligación de reintegro aplica a importes cobrados o adeudados por conceptos como tasas de interés, comisiones y/o cargos sin cumplimiento de lo previsto."


---

# CQN-007 — [factual_directa] · estrato **primaria**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn.json — el SELLADO)

**Pregunta:** ¿En qué circunstancia se identifica a una entidad financiera como “entidad atípica” en relación con el riesgo de tasa de interés en la cartera de inversión?

**ground_truth_secciones:** ["TO_regimen_informativo_contable_mensual_actual.pdf Punto 8.1"]
**tos_fuente:** ["TO_regimen_informativo_contable_mensual_actual.pdf"]
**categoria_generacion:** factual_directa
**estrato:** primaria · **disclosure:** la cita usa 'esta medida' (EVE): se acepta la respuesta con o sin nombrar EVE, exigiendo umbral y base

**cita_textual del GT:** "Cuando esta medida supere el 15 % del nivel de capital 1, se identificará a la entidad como una “entidad atípica” y la SEFyC podrá exigirle la adopción de medidas específicas"

**respuesta_breve del GT:** Cuando la medida de riesgo EVE estandarizada (la máxima pérdida registrada entre los escenarios) supera el 15 % del nivel de capital 1, la entidad se identifica como “entidad atípica” y la SEFyC puede exigirle la adopción de medidas específicas.

## 2. Síntoma del juez (verbatim, traza gate_cqn)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [],
 "reportes_de_alcance": [
  "No se encontró información en el Knowledge Graph sobre las circunstancias específicas que identifican a una entidad financiera como 'entidad atípica' en relación con el riesgo de tasa de interés en la cartera de inversión.",
  "El grafo contiene regulaciones sobre el cálculo del riesgo de tasa de interés (EVE) y diversas obligaciones de las entidades financieras.",
  "El grafo no incluye la definición o criterios de identificación de entidades atípicas en este contexto."
 ],
 "patas_de_la_pregunta": [
  "Circunstancia en que se identifica a una entidad financiera como 'entidad atípica' en relación con el riesgo de tasa de interés en la cartera de inversión"
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
  "pata": "Circunstancia en que se identifica a una entidad financiera como 'entidad atípica' en relación con el riesgo de tasa de interés en la cartera de inversión",
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
  "completitud": "Patas no cubiertas: Circunstancia en que se identifica a una entidad financiera como 'entidad atípica' en relación con el riesgo de tasa de interés en la cartera de inversión",
  "citas": "El agente no presentó ninguna cita, por lo que no se puede verificar referencia al documento del ground truth."
 }
}
```

**Síntoma (resumen mecánico, mismo filtro que build_falla_context): F = 0 claims reprobados (0 centrales) · P = 1 patas no cubiertas → síntoma NO VACÍO.**

## 3. Trayectoria

En la parte 2 (`expediente_gate_2.md`, sección "CQN-007").

## 4. Homólogos / territorio

**Disclosure del eval set (verbatim):** la cita usa 'esta medida' (EVE): se acepta la respuesta con o sin nombrar EVE, exigiendo umbral y base

**Territorio en varas previas** (barrido mecánico; cada entrada rotulada):

- GT `TO_regimen_informativo_contable_mensual_actual.pdf Punto 8.1` (punto 8.1) en **casos_control.md** — 2 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L68): - **La ex-secundaria `{faithfulness, alucinacion_agente}` SE DISUELVE → falso positivo del juez (sin par):** el claim **"0,08 es el coeficiente de capital mínimo"** está soportado 
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L69): - **El otro claim `no_soportado` del juez** —la fórmula alternativa "Código 70100000 (n) = …"— **se mantiene tal cual: falso positivo del juez** (sin par — no es defecto del sistem
- GT `TO_regimen_informativo_contable_mensual_actual.pdf Punto 8.1` (punto 8.1) en **casos_validacion.md** — 1 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L261): 7. **Provenances de run_2 con formato sospechoso** ("Sección 7 > Punto 8.1" y análogas) —
- GT `TO_regimen_informativo_contable_mensual_actual.pdf Punto 8.1` (punto 8.1) en **casos_dev_v7.md** — 2 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L60): - **GT: {context_recall, completitud_kg} PRIMARIA ÚNICA.** La regla del 8.1 (10 días
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L159): - Regla del 8.1 (10 días corridos a solicitud del cliente) sin portador (run_4).

## 5. Tabla inicial de hechos (cero adjudicación)

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Circunstancia en que se identifica a una entidad financiera como 'entidad atípica' en relación con el riesgo de tasa de interés en la cartera de inversión | no_cubierta | 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 |

**Descomposición del juez (qué dice la respuesta, verbatim step1):**
- reporte de alcance: "No se encontró información en el Knowledge Graph sobre las circunstancias específicas que identifican a una entidad financiera como 'entidad atípica' en relación con el riesgo de tasa de interés en la cartera de inversión."
- reporte de alcance: "El grafo contiene regulaciones sobre el cálculo del riesgo de tasa de interés (EVE) y diversas obligaciones de las entidades financieras."
- reporte de alcance: "El grafo no incluye la definición o criterios de identificación de entidades atípicas en este contexto."


---

# CQN-008 — [multi_norma] · estrato **ilustrativa_no_puntuable**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn.json — el SELLADO)

**Pregunta:** ¿Las empresas no financieras emisoras de tarjetas de crédito están alcanzadas por las normas de protección de los usuarios de servicios financieros y, a la vez, con qué criterio deben clasificar a sus deudores según las normas sobre clasificación de deudores?

**ground_truth_secciones:** ["TO_proteccion_usuarios_servicios_financieros_actual.pdf Punto 1.1", "TO_clasificacion_deudores_actual.pdf Punto 10.1"]
**tos_fuente:** ["TO_proteccion_usuarios_servicios_financieros_actual.pdf", "TO_clasificacion_deudores_actual.pdf"]
**categoria_generacion:** multi_norma
**estrato:** ilustrativa_no_puntuable · **disclosure:** reformulación del territorio de CQ-017/CQ-018 (quemado en 3 grafos) — se corre y reporta aparte, no integra métricas

**cita_textual del GT:** "1.1.2. Sujetos obligados. 1.1.2.1. Entidades financieras. […] 1.1.2.4. Empresas no financieras emisoras de tarjetas de crédito y/o compra. […] Las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedo- res no financieros de crédito alcanzados por las normas sobre “Proveedores no financieros de crédito”, deberán clasificar a los respectivos deudores en función de su mora, según los crite- rios aplicables para la cartera de “consumo o vivienda” y por aplicación de las disposiciones previstas en el punto 7.3. (recategorización obligatoria)."

**respuesta_breve del GT:** Sí: son sujetos obligados de las normas de protección de usuarios de servicios financieros. Además, según las normas de clasificación de deudores deben clasificar a sus deudores en función de su mora, con los criterios aplicables a la cartera de consumo o vivienda y la recategorización obligatoria correspondiente.

## 2. Síntoma del juez (verbatim, traza gate_cqn)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito están alcanzadas por las normas de protección de los usuarios de servicios financieros.",
   "central": true
  },
  {
   "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito deben designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.",
   "central": false
  },
  {
   "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito están sujetas a todas las obligaciones de los sujetos obligados en materia de protección de usuarios.",
   "central": false
  },
  {
   "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito se consideran proveedores no financieros de crédito.",
   "central": true
  },
  {
   "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito están alcanzadas por las normas sobre clasificación de deudores.",
   "central": true
  },
  {
   "enunciado": "Los criterios objetivos de clasificación de deudores incluyen el término de morosidad.",
   "central": true
  },
  {
   "enunciado": "El criterio de morosidad contempla atrasos de hasta 180 días.",
   "central": true
  },
  {
   "enunciado": "El criterio de morosidad contempla atrasos superiores a 180 días hasta un año.",
   "central": true
  },
  {
   "enunciado": "El criterio de morosidad contempla atrasos superiores a 540 días.",
   "central": true
  },
  {
   "enunciado": "Los criterios objetivos de clasificación de deudores incluyen la situación jurídica del cliente o de sus deudas.",
   "central": true
  },
  {
   "enunciado": "La situación jurídica relevante para la clasificación incluye gestión judicial, concurso preventivo y acuerdo extrajudicial.",
   "central": true
  },
  {
   "enunciado": "Los criterios objetivos de clasificación de deudores incluyen el cumplimiento de refinanciaciones y pedidos de refinanciaciones de obligaciones.",
   "central": true
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "Si las empresas no financieras emisoras de tarjetas de crédito están alcanzadas por las normas de protección de los usuarios de servicios financieros",
  "Con qué criterio deben clasificar a sus deudores según las normas sobre clasificación de deudores"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito están alcanzadas por las normas de protección de los usuarios de servicios financieros.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito deben designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito están sujetas a todas las obligaciones de los sujetos obligados en materia de protección de usuarios.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito se consideran proveedores no financieros de crédito.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito están alcanzadas por las normas sobre clasificación de deudores.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Los criterios objetivos de clasificación de deudores incluyen el término de morosidad.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "El criterio de morosidad contempla atrasos de hasta 180 días.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "El criterio de morosidad contempla atrasos superiores a 180 días hasta un año.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "El criterio de morosidad contempla atrasos superiores a 540 días.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Los criterios objetivos de clasificación de deudores incluyen la situación jurídica del cliente o de sus deudas.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "La situación jurídica relevante para la clasificación incluye gestión judicial, concurso preventivo y acuerdo extrajudicial.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Los criterios objetivos de clasificación de deudores incluyen el cumplimiento de refinanciaciones y pedidos de refinanciaciones de obligaciones.",
  "central": true,
  "verdict": "no_soportado"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Si las empresas no financieras emisoras de tarjetas de crédito están alcanzadas por las normas de protección de los usuarios de servicios financieros",
  "cobertura": "cubierta"
 },
 {
  "pata": "Con qué criterio deben clasificar a sus deudores según las normas sobre clasificación de deudores",
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
   "Los criterios objetivos de clasificación de deudores incluyen el término de morosidad.",
   "El criterio de morosidad contempla atrasos de hasta 180 días.",
   "El criterio de morosidad contempla atrasos superiores a 180 días hasta un año.",
   "El criterio de morosidad contempla atrasos superiores a 540 días.",
   "Los criterios objetivos de clasificación de deudores incluyen la situación jurídica del cliente o de sus deudas.",
   "La situación jurídica relevante para la clasificación incluye gestión judicial, concurso preventivo y acuerdo extrajudicial.",
   "Los criterios objetivos de clasificación de deudores incluyen el cumplimiento de refinanciaciones y pedidos de refinanciaciones de obligaciones."
  ],
  "secundarias": [
   "Las empresas no financieras emisoras de tarjetas de crédito deben designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.",
   "Las empresas no financieras emisoras de tarjetas de crédito están sujetas a todas las obligaciones de los sujetos obligados en materia de protección de usuarios."
  ],
  "n_centrales": 7,
  "n_secundarias": 2
 },
 "requiere_adjudicacion_humana": true,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "El agente cita correctamente TO_proteccion_usuarios_servicios_financieros_actual.pdf y TO_clasificacion_deudores_actual.pdf Punto 10.1, que es uno de los documentos del ground truth, con precisión a nivel punto."
 }
}
```

**Síntoma (resumen mecánico, mismo filtro que build_falla_context): F = 9 claims reprobados (7 centrales) · P = 0 patas no cubiertas → síntoma NO VACÍO.**

## 3. Trayectoria

En la parte 2 (`expediente_gate_2.md`, sección "CQN-008").

## 4. Homólogos / territorio

**Disclosure del eval set (verbatim):** reformulación del territorio de CQ-017/CQ-018 (quemado en 3 grafos) — se corre y reporta aparte, no integra métricas

**Territorio en varas previas** (barrido mecánico; cada entrada rotulada):

- GT `TO_proteccion_usuarios_servicios_financieros_actual.pdf Punto 1.1` (punto 1.1) en **casos_control.md** — 7 línea(s), primeras 6:
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L54): - **Ground-truth secciones:** Protección, Punto 1.1.2.2 · Exterior y Cambios, Punto 1.1.
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L56): - **Causa primaria — `{context_recall, estructural_kg}` (pata 2):** falta la arista cross-documento que une Protección (Punto **1.1.2.2**, operador de cambio alcanzado) con Exterio
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L57): - **Causa primaria — `{noise_sensitivity, provenance_imprecisa}` (pata 1):** el nodo del operador de cambio tiene provenance a nivel grueso — verbatim **"Punto 1.1. Partes."** (`ve
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L65): - **Ground-truth secciones:** Capitales, Punto 2.1 · Régimen Informativo, Punto 3.1.2 · Régimen Informativo, Punto 1.1 (frecuencia).
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L67): - **Causa primaria — `{context_recall, completitud_kg}` (defecto del grafo):** falta el nodo de **frecuencia de reporte para riesgo de crédito**; por su ausencia el agente **mis-ap
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L77): - **Pata 1 (riesgo de mercado) — `{noise_sensitivity, contenido_kg}`, PRIMARIA (defecto de grafo):** el PDF (Punto 1.1 del TO de Régimen Informativo) ubica los datos de riesgo de m
- GT `TO_proteccion_usuarios_servicios_financieros_actual.pdf Punto 1.1` (punto 1.1) en **casos_piloto.md** — 3 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L4): v1.1** (los GTs se adjudican sobre el marco POST-HOC: los claims que el juez post-hoc reprobó
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L41): del juez — el `ground_truth_secciones` del caso es Protección 1.1.2.4/1.1.2.5 +
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L164): v1.1 (pre-ejecución). **Hallazgos laterales al backlog de refinamiento** (documentados acá,
- GT `TO_proteccion_usuarios_servicios_financieros_actual.pdf Punto 1.1` (punto 1.1) en **casos_validacion.md** — 5 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L65): el Punto 1.1 del TO de Régimen Informativo ubica los datos de los puntos 4.3-4.5 en las
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L156): - **GT: PATA 2 — `{context_recall, completitud_kg}` PRIMARIA:** la regla del 1.1 de Exterior
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L160): único nodo operador (`operador_de_cambio`, provenance Protección 1.1.2.2) tiene **0
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L251): 1.1** (run_2 — provenance 4.3, contenido "mensual" donde el régimen lo hace trimestral).
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L256): 4. **Regla del 1.1 de Exterior sin portador** (run_4 — faltan las piezas, no solo el puente).
- GT `TO_clasificacion_deudores_actual.pdf Punto 10.1` (punto 10.1) en **casos_control.md** — 1 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L79): - **Pata 2 (ratio de apalancamiento) — falso positivo del juez (NO defecto de grafo ni de agente; sin par v2 — no es defecto del sistema):** el agente respondió correctamente que e
- GT `TO_clasificacion_deudores_actual.pdf Punto 10.1` (punto 10.1) en **casos_piloto.md** — 1 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L42): Clasificación 10.1, y una cita al 4.2 sigue fuera de ese marco → la provenance corrida
- GT `TO_clasificacion_deudores_actual.pdf Punto 10.1` (punto 10.1) en **casos_validacion.md** — 2 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L137): sujeto fue AMPUTADO del 10.1 en la extracción**: "10.1" da **0 portadores en properties**
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L254): 3. **Sujeto "emisoras" amputado del 10.1 en la extracción** (run_2 — la obligación de
- GT `TO_clasificacion_deudores_actual.pdf Punto 10.1` (punto 10.1) en **casos_dev_v7.md** — 1 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L152): series previas (12.3/encabezado de alcance; 10.1/sujeto). El patrón: la extracción captura

## 5. Tabla inicial de hechos (cero adjudicación)

**Claims reprobados en juego:**
- secundario `no_soportado`: "Las empresas no financieras emisoras de tarjetas de crédito deben designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA."
- secundario `no_soportado`: "Las empresas no financieras emisoras de tarjetas de crédito están sujetas a todas las obligaciones de los sujetos obligados en materia de protección de usuarios."
- CENTRAL `no_soportado`: "Los criterios objetivos de clasificación de deudores incluyen el término de morosidad."
- CENTRAL `no_soportado`: "El criterio de morosidad contempla atrasos de hasta 180 días."
- CENTRAL `no_soportado`: "El criterio de morosidad contempla atrasos superiores a 180 días hasta un año."
- CENTRAL `no_soportado`: "El criterio de morosidad contempla atrasos superiores a 540 días."
- CENTRAL `no_soportado`: "Los criterios objetivos de clasificación de deudores incluyen la situación jurídica del cliente o de sus deudas."
- CENTRAL `no_soportado`: "La situación jurídica relevante para la clasificación incluye gestión judicial, concurso preventivo y acuerdo extrajudicial."
- CENTRAL `no_soportado`: "Los criterios objetivos de clasificación de deudores incluyen el cumplimiento de refinanciaciones y pedidos de refinanciaciones de obligaciones."

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Si las empresas no financieras emisoras de tarjetas de crédito están alcanzadas por las normas de protección de los usuarios de servicios financieros | cubierta | 1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16 |
| Con qué criterio deben clasificar a sus deudores según las normas sobre clasificación de deudores | cubierta | 3, 4, 6, 7, 9, 11, 12, 13, 14, 15, 16 |

**Descomposición del juez (qué dice la respuesta, verbatim step1):**
- afirmación (central): "Las empresas no financieras emisoras de tarjetas de crédito están alcanzadas por las normas de protección de los usuarios de servicios financieros."
- afirmación (no central): "Las empresas no financieras emisoras de tarjetas de crédito deben designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA."
- afirmación (no central): "Las empresas no financieras emisoras de tarjetas de crédito están sujetas a todas las obligaciones de los sujetos obligados en materia de protección de usuarios."
- afirmación (central): "Las empresas no financieras emisoras de tarjetas de crédito se consideran proveedores no financieros de crédito."
- afirmación (central): "Las empresas no financieras emisoras de tarjetas de crédito están alcanzadas por las normas sobre clasificación de deudores."
- afirmación (central): "Los criterios objetivos de clasificación de deudores incluyen el término de morosidad."
- afirmación (central): "El criterio de morosidad contempla atrasos de hasta 180 días."
- afirmación (central): "El criterio de morosidad contempla atrasos superiores a 180 días hasta un año."
- afirmación (central): "El criterio de morosidad contempla atrasos superiores a 540 días."
- afirmación (central): "Los criterios objetivos de clasificación de deudores incluyen la situación jurídica del cliente o de sus deudas."
- afirmación (central): "La situación jurídica relevante para la clasificación incluye gestión judicial, concurso preventivo y acuerdo extrajudicial."
- afirmación (central): "Los criterios objetivos de clasificación de deudores incluyen el cumplimiento de refinanciaciones y pedidos de refinanciaciones de obligaciones."


---

# CQN-009 — [multi_norma] · estrato **primaria**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn.json — el SELLADO)

**Pregunta:** ¿Qué importe debe consignar un banco —que no sea caja de crédito cooperativa— en el total de control correspondiente al capital mínimo básico del régimen informativo sobre exigencia e integración de capitales mínimos?

**ground_truth_secciones:** ["TO_regimen_informativo_contable_mensual_actual.pdf Punto 8.1", "TO_capitales_minimos_actual.pdf Punto 1.2"]
**tos_fuente:** ["TO_regimen_informativo_contable_mensual_actual.pdf", "TO_capitales_minimos_actual.pdf"]
**categoria_generacion:** multi_norma
**estrato:** primaria · **disclosure:** GT compartido con CQ-010 (nunca fue caso de falla) — disclosure leve

**cita_textual del GT:** "8.1.3. Código 70700000. Capital Mínimo Básico –punto 1.2. de las normas sobre “Capitales mínimos de las entidades financieras”–. […] Según la clase de entidad, serán las siguientes exigencias básicas: Restantes entidades Bancos (salvo Cajas de Crédito Cooperativas) -En millones de pesos- 5.000 2.500"

**respuesta_breve del GT:** Debe consignar $ 5.000 millones. El total de control del capital mínimo básico remite a la exigencia básica de las normas sobre capitales mínimos, que para los bancos es de $ 5.000 millones (y de $ 2.500 millones para las restantes entidades, salvo cajas de crédito cooperativas).

## 2. Síntoma del juez (verbatim, traza gate_cqn)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Los bancos (que no sean cajas de crédito cooperativa) deben mantener una exigencia básica de capital mínimo de 5.000 millones de pesos.",
   "central": true
  }
 ],
 "reportes_de_alcance": [
  "No se encontró en el Knowledge Graph información específica sobre qué importe debe consignarse en el 'total de control' correspondiente al capital mínimo básico del régimen informativo sobre exigencia e integración de capitales mínimos para bancos que no sean cajas de crédito cooperativa.",
  "La documentación disponible no especifica cómo debe reportarse este importe en un campo denominado 'total de control' en el régimen informativo."
 ],
 "patas_de_la_pregunta": [
  "Importe a consignar en el total de control correspondiente al capital mínimo básico del régimen informativo sobre exigencia e integración de capitales mínimos, para un banco que no sea caja de crédito cooperativa"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "Los bancos (que no sean cajas de crédito cooperativa) deben mantener una exigencia básica de capital mínimo de 5.000 millones de pesos.",
  "central": true,
  "verdict": "verdadero"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Importe a consignar en el total de control correspondiente al capital mínimo básico del régimen informativo sobre exigencia e integración de capitales mínimos, para un banco que no sea caja de crédito cooperativa",
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
  "completitud": "Patas no cubiertas: Importe a consignar en el total de control correspondiente al capital mínimo básico del régimen informativo sobre exigencia e integración de capitales mínimos, para un banco que no sea caja de crédito cooperativa",
  "citas": "El agente cita TO_capitales_minimos_actual.pdf Punto 1.2, que es uno de los documentos del ground truth."
 }
}
```

**Síntoma (resumen mecánico, mismo filtro que build_falla_context): F = 0 claims reprobados (0 centrales) · P = 1 patas no cubiertas → síntoma NO VACÍO.**

## 3. Trayectoria

En la parte 2 (`expediente_gate_2.md`, sección "CQN-009").

## 4. Homólogos / territorio

**Disclosure del eval set (verbatim):** GT compartido con CQ-010 (nunca fue caso de falla) — disclosure leve

**Territorio en varas previas** (barrido mecánico; cada entrada rotulada):

- GT `TO_regimen_informativo_contable_mensual_actual.pdf Punto 8.1` (punto 8.1) en **casos_control.md** — 2 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L68): - **La ex-secundaria `{faithfulness, alucinacion_agente}` SE DISUELVE → falso positivo del juez (sin par):** el claim **"0,08 es el coeficiente de capital mínimo"** está soportado 
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L69): - **El otro claim `no_soportado` del juez** —la fórmula alternativa "Código 70100000 (n) = …"— **se mantiene tal cual: falso positivo del juez** (sin par — no es defecto del sistem
- GT `TO_regimen_informativo_contable_mensual_actual.pdf Punto 8.1` (punto 8.1) en **casos_validacion.md** — 1 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L261): 7. **Provenances de run_2 con formato sospechoso** ("Sección 7 > Punto 8.1" y análogas) —
- GT `TO_regimen_informativo_contable_mensual_actual.pdf Punto 8.1` (punto 8.1) en **casos_dev_v7.md** — 2 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L60): - **GT: {context_recall, completitud_kg} PRIMARIA ÚNICA.** La regla del 8.1 (10 días
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L159): - Regla del 8.1 (10 días corridos a solicitud del cliente) sin portador (run_4).

## 5. Tabla inicial de hechos (cero adjudicación)

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Importe a consignar en el total de control correspondiente al capital mínimo básico del régimen informativo sobre exigencia e integración de capitales mínimos, para un banco que no sea caja de crédito cooperativa | no_cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 |

**Descomposición del juez (qué dice la respuesta, verbatim step1):**
- afirmación (central): "Los bancos (que no sean cajas de crédito cooperativa) deben mantener una exigencia básica de capital mínimo de 5.000 millones de pesos."
- reporte de alcance: "No se encontró en el Knowledge Graph información específica sobre qué importe debe consignarse en el 'total de control' correspondiente al capital mínimo básico del régimen informativo sobre exigencia e integración de capitales mínimos para bancos que no sean cajas de crédito cooperativa."
- reporte de alcance: "La documentación disponible no especifica cómo debe reportarse este importe en un campo denominado 'total de control' en el régimen informativo."


---

# CQN-010 — [multi_norma] · estrato **primaria**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn.json — el SELLADO)

**Pregunta:** Cuando las divisas del cobro de una exportación se aplican a cancelar una prefinanciación, ¿qué documento necesita la entidad encargada del seguimiento del permiso de embarque para registrar esa imputación y qué entidad es la única habilitada para emitirlo?

**ground_truth_secciones:** ["TO_exterior_cambios_actual.pdf Punto 8.4", "TO_exterior_cambios_actual.pdf Punto 9.2"]
**tos_fuente:** ["TO_exterior_cambios_actual.pdf"]
**categoria_generacion:** multi_norma
**estrato:** primaria · **disclosure:** limpia

**cita_textual del GT:** "8.4.3.2. Aplicación de las divisas provenientes del cobro de la exportación de bienes admitidos por esta normativa. La entidad deberá contar con una certificación de aplicación emitida por la encargada del seguimiento de la operación a cuya cancelación se aplicaron las divisas. […] Esta entidad será la única responsable de emitir los certificados de aplicación que habilitan que los cobros de exportaciones puedan ser imputados a los permisos correspondientes."

**respuesta_breve del GT:** Necesita una certificación de aplicación. La única habilitada para emitirla es la entidad nominada por el exportador para el seguimiento de la operación de financiación a cuya cancelación se aplicaron las divisas.

## 2. Síntoma del juez (verbatim, traza gate_cqn)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Cuando las divisas del cobro de una exportación se aplican a cancelar una prefinanciación, la entidad encargada del seguimiento del permiso de embarque necesita un certificado de aplicación para registrar esa imputación.",
   "central": true
  },
  {
   "enunciado": "La entidad financiera encargada del seguimiento del permiso de embarque es la única habilitada para emitir los certificados de aplicación.",
   "central": true
  },
  {
   "enunciado": "Los certificados de aplicación habilitan que los cobros de exportaciones puedan ser imputados a los permisos correspondientes.",
   "central": false
  },
  {
   "enunciado": "Esta regulación proviene del BCRA.",
   "central": false
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "Qué documento necesita la entidad encargada del seguimiento del permiso de embarque para registrar la imputación de divisas a una prefinanciación",
  "Qué entidad es la única habilitada para emitir ese documento"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "Cuando las divisas del cobro de una exportación se aplican a cancelar una prefinanciación, la entidad encargada del seguimiento del permiso de embarque necesita un certificado de aplicación para registrar esa imputación.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La entidad financiera encargada del seguimiento del permiso de embarque es la única habilitada para emitir los certificados de aplicación.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Los certificados de aplicación habilitan que los cobros de exportaciones puedan ser imputados a los permisos correspondientes.",
  "central": false,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Esta regulación proviene del BCRA.",
  "central": false,
  "verdict": "no_soportado"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Qué documento necesita la entidad encargada del seguimiento del permiso de embarque para registrar la imputación de divisas a una prefinanciación",
  "cobertura": "cubierta"
 },
 {
  "pata": "Qué entidad es la única habilitada para emitir ese documento",
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
   "Esta regulación proviene del BCRA."
  ],
  "n_centrales": 0,
  "n_secundarias": 1
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "La cita apunta al documento correcto (TO_exterior_cambios_actual.pdf) pero la ubicación indicada (Punto 7.10 / 9.1.7) no corresponde al punto 8.4 donde se encuentra la norma relevante, por lo que la precisión es de página y no de punto."
 }
}
```

**Síntoma (resumen mecánico, mismo filtro que build_falla_context): F = 1 claims reprobados (0 centrales) · P = 0 patas no cubiertas → síntoma NO VACÍO.**

## 3. Trayectoria

En la parte 2 (`expediente_gate_2.md`, sección "CQN-010").

## 4. Homólogos / territorio

**Disclosure del eval set (verbatim):** limpia

**Territorio en varas previas:** el barrido mecánico de los puntos del GT sobre las 4 varas no devolvió líneas.

## 5. Tabla inicial de hechos (cero adjudicación)

**Claims reprobados en juego:**
- secundario `no_soportado`: "Esta regulación proviene del BCRA."

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Qué documento necesita la entidad encargada del seguimiento del permiso de embarque para registrar la imputación de divisas a una prefinanciación | cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15 |
| Qué entidad es la única habilitada para emitir ese documento | cubierta | 1, 2, 3, 5, 7, 8, 10, 11, 12, 13, 14, 15 |

**Descomposición del juez (qué dice la respuesta, verbatim step1):**
- afirmación (central): "Cuando las divisas del cobro de una exportación se aplican a cancelar una prefinanciación, la entidad encargada del seguimiento del permiso de embarque necesita un certificado de aplicación para registrar esa imputación."
- afirmación (central): "La entidad financiera encargada del seguimiento del permiso de embarque es la única habilitada para emitir los certificados de aplicación."
- afirmación (no central): "Los certificados de aplicación habilitan que los cobros de exportaciones puedan ser imputados a los permisos correspondientes."
- afirmación (no central): "Esta regulación proviene del BCRA."


---

# CQN-011 — [multi_norma] · estrato **primaria**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn.json — el SELLADO)

**Pregunta:** ¿Con qué frecuencia se informa la información complementaria vinculada al riesgo de tasa de interés en la cartera de inversión y a qué caso de entidad corresponde el código de consolidación con el que se presenta en base consolidada?

**ground_truth_secciones:** ["TO_regimen_informativo_contable_mensual_actual.pdf Punto 11.1", "TO_regimen_informativo_contable_mensual_actual.pdf Sección 2"]
**tos_fuente:** ["TO_regimen_informativo_contable_mensual_actual.pdf"]
**categoria_generacion:** multi_norma
**estrato:** primaria · **disclosure:** familia de prefijo con territorio adjudicado, sin GT compartido

**cita_textual del GT:** "Los datos se informarán con frecuencia trimestral y se integrarán con los datos correspon- dientes al último mes de cada trimestre (marzo, junio, septiembre y diciembre), sobre base individual y consolidada mensual. Serán aplicables los siguientes códigos de consolidación definidos en la Sección 2.: Base individual (código de consolidación 0 o 1); Base consolidada (código de consolidación 2). […] Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país y en el exterior) – (con el alcance definido en el punto 6.2. de las normas sobre “Su- 2 pervisión consolidada”)"

**respuesta_breve del GT:** Se informa con frecuencia trimestral, con los datos del último mes de cada trimestre (marzo, junio, septiembre y diciembre). La base consolidada usa el código de consolidación 2, que corresponde al consolidado mensual de una entidad financiera con filiales y subsidiarias significativas en el país y en el exterior.

## 2. Síntoma del juez (verbatim, traza gate_cqn)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "La información complementaria vinculada al riesgo de tasa de interés en la cartera de inversión se informa con frecuencia trimestral.",
   "central": true
  },
  {
   "enunciado": "El código de consolidación 3 corresponde a la presentación en base consolidada trimestral.",
   "central": true
  },
  {
   "enunciado": "El código de consolidación 3 se aplica a entidades controlantes que deben presentar información consolidada de sus filiales o subsidiarias.",
   "central": true
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "Frecuencia con que se informa la información complementaria vinculada al riesgo de tasa de interés en la cartera de inversión",
  "A qué caso de entidad corresponde el código de consolidación con el que se presenta en base consolidada"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "La información complementaria vinculada al riesgo de tasa de interés en la cartera de inversión se informa con frecuencia trimestral.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "El código de consolidación 3 corresponde a la presentación en base consolidada trimestral.",
  "central": true,
  "verdict": "falso"
 },
 {
  "enunciado": "El código de consolidación 3 se aplica a entidades controlantes que deben presentar información consolidada de sus filiales o subsidiarias.",
  "central": true,
  "verdict": "falso"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Frecuencia con que se informa la información complementaria vinculada al riesgo de tasa de interés en la cartera de inversión",
  "cobertura": "cubierta"
 },
 {
  "pata": "A qué caso de entidad corresponde el código de consolidación con el que se presenta en base consolidada",
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
  "secundarias": [],
  "n_centrales": 0,
  "n_secundarias": 0
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Afirmación central falsa: El código de consolidación 3 corresponde a la presentación en base consolidada trimestral.; El código de consolidación 3 se aplica a entidades controlantes que deben presentar información consolidada de sus filiales o subsidiarias.",
  "completitud": "Patas no cubiertas: A qué caso de entidad corresponde el código de consolidación con el que se presenta en base consolidada",
  "citas": "El agente cita el documento correcto (TO_regimen_informativo_contable_mensual_actual.pdf) a nivel de punto, pero no apunta al Punto 11.1 ni a la Sección 2 que son las secciones relevantes del referente."
 }
}
```

**Síntoma (resumen mecánico, mismo filtro que build_falla_context): F = 2 claims reprobados (2 centrales) · P = 1 patas no cubiertas → síntoma NO VACÍO.**

## 3. Trayectoria

En la parte 2 (`expediente_gate_2.md`, sección "CQN-011").

## 4. Homólogos / territorio

**Disclosure del eval set (verbatim):** familia de prefijo con territorio adjudicado, sin GT compartido

**Territorio en varas previas** (barrido mecánico; cada entrada rotulada):

- GT `TO_regimen_informativo_contable_mensual_actual.pdf Sección 2` (punto 2) en **casos_control.md** — 19 línea(s), primeras 6:
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L12): 2. Se compara la atribución del agente con la **atribución humana** registrada acá.
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L24): > **Nota de procedencia (importante, leer).** Las preguntas y sus `ground_truth_secciones`/`cita_textual` salen verbatim de `data/experiment/evaluacion/queries/eval_set_v2.json` (p
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L30): - **El portador existe y es fiel:** el nodo `Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti` porta la regla del 4.5 verbatim en `prope
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L32): - **Prueba ex ante (v2.1), caminada con hechos:** "garantías" no está en la pregunta; fue expuesto al agente en outputs completos desde el paso 2; el agente lo incorporó y lo usó e
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L33): - **Exclusión EMPÍRICA de `navegación`:** el agente ejecutó las búsquedas razonables con el mejor vocabulario disponible y el índice no devolvió el portador — **0/10 apariciones en
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L34): - **Mecanismo confirmado:** el id truncado del portador indexa el token `garanti`, que el token de búsqueda `garantias` no matchea — score 0 en las consultas "garantías preferidas 
- GT `TO_regimen_informativo_contable_mensual_actual.pdf Sección 2` (punto 2) en **casos_piloto.md** — 22 línea(s), primeras 6:
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L9): **Vocabulario:** taxonomía **v2.6.1** (pares `{sintoma_capa1, causa_capa2}`, ver
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L14): `docs/evidencia_piloto/` (expediente_piloto_1/2.md, verificaciones_piloto.md) y
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L30): - **GT: SIN PRIMARIA** (regla de jerarquía FP-centrales, v2.6: el único central reprobado es
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L58): respuesta, inventario) y `expediente_piloto_2.md` (outputs completos);
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L60): `docs/evidencia_capa_d/verificacion_estructura_piloto.md` §2-§3.
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L73): (`docs/evidencia_piloto/verificaciones_piloto.md` §2a-§2b, contenido íntegro pegado) —
- GT `TO_regimen_informativo_contable_mensual_actual.pdf Sección 2` (punto 2) en **casos_validacion.md** — 53 línea(s), primeras 6:
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L8): v2.6.1. **Circuito:** el de la vara — re-ejecuciones determinísticas de outputs completos,
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L12): **Evidencia:** `docs/evidencia_validacion/` (censo, expediente_validacion_1/2/3.md,
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L13): verificaciones_validacion_1/2.md).
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L15): **Los 8 casos:** run_2/{CQ-015, CQ-018, CQ-019, CQ-025} · run_4/{CQ-014, CQ-019, CQ-017,
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L16): CQ-020} — composición del protocolo §3 (2 controles por diseño, 2 deliberados por severidad,
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L21): ## run_2/CQ-015 — `factual_directa` · CONTROL NEGATIVO (por diseño)
- GT `TO_regimen_informativo_contable_mensual_actual.pdf Sección 2` (punto 2) en **casos_dev_v7.md** — 31 línea(s), primeras 6:
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L13): esto. **Vocabulario:** taxonomía v2.6.1. **Circuito:** el de la vara — re-ejecuciones
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L17): **Evidencia:** `docs/evidencia_dev_v7/` (expediente_dev_v7_1/2.md,
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L18): verificaciones_dev_v7_1/2.md).
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L20): **Los 4 casos:** run_2/CQ-021 · run_4/{CQ-008, CQ-021, CQ-028} — la reserva pre-registrada
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L26): ## run_2/CQ-021 — `factual_directa` · reserva v7
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L30): - **Síntoma post-hoc:** F = 0 claims reprobados · P = **2 patas no cubiertas** (los casos

## 5. Tabla inicial de hechos (cero adjudicación)

**Claims reprobados en juego:**
- CENTRAL `falso`: "El código de consolidación 3 corresponde a la presentación en base consolidada trimestral."
- CENTRAL `falso`: "El código de consolidación 3 se aplica a entidades controlantes que deben presentar información consolidada de sus filiales o subsidiarias."

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Frecuencia con que se informa la información complementaria vinculada al riesgo de tasa de interés en la cartera de inversión | cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 10 |
| A qué caso de entidad corresponde el código de consolidación con el que se presenta en base consolidada | no_cubierta | 1, 2, 3, 4, 6, 7, 8, 9, 10 |

**Descomposición del juez (qué dice la respuesta, verbatim step1):**
- afirmación (central): "La información complementaria vinculada al riesgo de tasa de interés en la cartera de inversión se informa con frecuencia trimestral."
- afirmación (central): "El código de consolidación 3 corresponde a la presentación en base consolidada trimestral."
- afirmación (central): "El código de consolidación 3 se aplica a entidades controlantes que deben presentar información consolidada de sus filiales o subsidiarias."


---

# CQN-012 — [multi_norma] · estrato **solapada**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn.json — el SELLADO)

**Pregunta:** ¿Cómo se determina la exigencia de capital mínimo que debe integrar una entidad financiera y cómo se calcula, en su primer mes de funcionamiento, el componente de esa exigencia correspondiente al riesgo operacional?

**ground_truth_secciones:** ["TO_capitales_minimos_actual.pdf Punto 1.1", "TO_capitales_minimos_actual.pdf Punto 7.4"]
**tos_fuente:** ["TO_capitales_minimos_actual.pdf"]
**categoria_generacion:** multi_norma
**estrato:** solapada · **disclosure:** GT 1.1 compartido con CQ-020 (quemado ×2); pata 7.4 virgen

**cita_textual del GT:** "La exigencia de capital mínimo que las entidades financieras deberán tener integrada será equivalente al mayor valor que resulte de la comparación entre la exigencia básica y la suma de las determinadas por riesgos de crédito, de mercado –exigencia por las posiciones diarias de los activos comprendidos– y operacional. […] La exigencia mensual de capital mínimo por riesgo operacional de las entidades financieras de los grupos 1 y 2 correspondiente al primer mes será equivalente al 10% de la sumatoria de las exigencias determinadas por los riesgos de crédito y de mercado –en este caso, para las posi- ciones del último día– de ese mes."

**respuesta_breve del GT:** La exigencia es el mayor valor entre la exigencia básica y la suma de las exigencias por riesgos de crédito, de mercado y operacional. Para una entidad nueva, la exigencia por riesgo operacional del primer mes equivale al 10 % de la sumatoria de las exigencias por riesgos de crédito y de mercado —para las posiciones del último día— de ese mes.

## 2. Síntoma del juez (verbatim, traza gate_cqn)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "La exigencia de capital mínimo que debe integrar una entidad financiera se determina como la suma de los componentes por riesgo de crédito, riesgo de mercado y riesgo operacional, junto con otras exigencias regulatorias.",
   "central": true
  },
  {
   "enunciado": "Cada componente de la exigencia de capital mínimo se calcula conforme a metodologías específicas establecidas en la normativa.",
   "central": false
  },
  {
   "enunciado": "En el primer mes de funcionamiento de una nueva entidad, el componente de la exigencia correspondiente al riesgo operacional equivale al 10% de la sumatoria de las exigencias determinadas por los riesgos de crédito y de mercado de ese mes.",
   "central": true
  },
  {
   "enunciado": "Para el cálculo del primer mes de funcionamiento, el riesgo de mercado se considera tomando las posiciones del último día del mes.",
   "central": true
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "Cómo se determina la exigencia de capital mínimo que debe integrar una entidad financiera",
  "Cómo se calcula, en el primer mes de funcionamiento, el componente de la exigencia correspondiente al riesgo operacional"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "La exigencia de capital mínimo que debe integrar una entidad financiera se determina como la suma de los componentes por riesgo de crédito, riesgo de mercado y riesgo operacional, junto con otras exigencias regulatorias.",
  "central": true,
  "verdict": "falso"
 },
 {
  "enunciado": "Cada componente de la exigencia de capital mínimo se calcula conforme a metodologías específicas establecidas en la normativa.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "En el primer mes de funcionamiento de una nueva entidad, el componente de la exigencia correspondiente al riesgo operacional equivale al 10% de la sumatoria de las exigencias determinadas por los riesgos de crédito y de mercado de ese mes.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Para el cálculo del primer mes de funcionamiento, el riesgo de mercado se considera tomando las posiciones del último día del mes.",
  "central": true,
  "verdict": "verdadero"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Cómo se determina la exigencia de capital mínimo que debe integrar una entidad financiera",
  "cobertura": "cubierta"
 },
 {
  "pata": "Cómo se calcula, en el primer mes de funcionamiento, el componente de la exigencia correspondiente al riesgo operacional",
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
   "Cada componente de la exigencia de capital mínimo se calcula conforme a metodologías específicas establecidas en la normativa."
  ],
  "n_centrales": 0,
  "n_secundarias": 1
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Afirmación central falsa: La exigencia de capital mínimo que debe integrar una entidad financiera se determina como la suma de los componentes por riesgo de crédito, riesgo de mercado y riesgo operacional, junto con otras exigencias regulatorias.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "El agente cita correctamente TO_capitales_minimos_actual.pdf Punto 7.4, que es uno de los ground truth sections, con precisión a nivel punto."
 }
}
```

**Síntoma (resumen mecánico, mismo filtro que build_falla_context): F = 2 claims reprobados (1 centrales) · P = 0 patas no cubiertas → síntoma NO VACÍO.**

## 3. Trayectoria

En la parte 2 (`expediente_gate_2.md`, sección "CQN-012").

## 4. Homólogos / territorio

**Disclosure del eval set (verbatim):** GT 1.1 compartido con CQ-020 (quemado ×2); pata 7.4 virgen

**Territorio en varas previas** (barrido mecánico; cada entrada rotulada):

- GT `TO_capitales_minimos_actual.pdf Punto 1.1` (punto 1.1) en **casos_control.md** — 7 línea(s), primeras 6:
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L54): - **Ground-truth secciones:** Protección, Punto 1.1.2.2 · Exterior y Cambios, Punto 1.1.
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L56): - **Causa primaria — `{context_recall, estructural_kg}` (pata 2):** falta la arista cross-documento que une Protección (Punto **1.1.2.2**, operador de cambio alcanzado) con Exterio
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L57): - **Causa primaria — `{noise_sensitivity, provenance_imprecisa}` (pata 1):** el nodo del operador de cambio tiene provenance a nivel grueso — verbatim **"Punto 1.1. Partes."** (`ve
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L65): - **Ground-truth secciones:** Capitales, Punto 2.1 · Régimen Informativo, Punto 3.1.2 · Régimen Informativo, Punto 1.1 (frecuencia).
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L67): - **Causa primaria — `{context_recall, completitud_kg}` (defecto del grafo):** falta el nodo de **frecuencia de reporte para riesgo de crédito**; por su ausencia el agente **mis-ap
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L77): - **Pata 1 (riesgo de mercado) — `{noise_sensitivity, contenido_kg}`, PRIMARIA (defecto de grafo):** el PDF (Punto 1.1 del TO de Régimen Informativo) ubica los datos de riesgo de m
- GT `TO_capitales_minimos_actual.pdf Punto 1.1` (punto 1.1) en **casos_piloto.md** — 3 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L4): v1.1** (los GTs se adjudican sobre el marco POST-HOC: los claims que el juez post-hoc reprobó
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L41): del juez — el `ground_truth_secciones` del caso es Protección 1.1.2.4/1.1.2.5 +
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L164): v1.1 (pre-ejecución). **Hallazgos laterales al backlog de refinamiento** (documentados acá,
- GT `TO_capitales_minimos_actual.pdf Punto 1.1` (punto 1.1) en **casos_validacion.md** — 5 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L65): el Punto 1.1 del TO de Régimen Informativo ubica los datos de los puntos 4.3-4.5 en las
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L156): - **GT: PATA 2 — `{context_recall, completitud_kg}` PRIMARIA:** la regla del 1.1 de Exterior
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L160): único nodo operador (`operador_de_cambio`, provenance Protección 1.1.2.2) tiene **0
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L251): 1.1** (run_2 — provenance 4.3, contenido "mensual" donde el régimen lo hace trimestral).
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L256): 4. **Regla del 1.1 de Exterior sin portador** (run_4 — faltan las piezas, no solo el puente).

## 5. Tabla inicial de hechos (cero adjudicación)

**Claims reprobados en juego:**
- CENTRAL `falso`: "La exigencia de capital mínimo que debe integrar una entidad financiera se determina como la suma de los componentes por riesgo de crédito, riesgo de mercado y riesgo operacional, junto con otras exigencias regulatorias."
- secundario `no_soportado`: "Cada componente de la exigencia de capital mínimo se calcula conforme a metodologías específicas establecidas en la normativa."

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Cómo se determina la exigencia de capital mínimo que debe integrar una entidad financiera | cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15 |
| Cómo se calcula, en el primer mes de funcionamiento, el componente de la exigencia correspondiente al riesgo operacional | cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15 |

**Descomposición del juez (qué dice la respuesta, verbatim step1):**
- afirmación (central): "La exigencia de capital mínimo que debe integrar una entidad financiera se determina como la suma de los componentes por riesgo de crédito, riesgo de mercado y riesgo operacional, junto con otras exigencias regulatorias."
- afirmación (no central): "Cada componente de la exigencia de capital mínimo se calcula conforme a metodologías específicas establecidas en la normativa."
- afirmación (central): "En el primer mes de funcionamiento de una nueva entidad, el componente de la exigencia correspondiente al riesgo operacional equivale al 10% de la sumatoria de las exigencias determinadas por los riesgos de crédito y de mercado de ese mes."
- afirmación (central): "Para el cálculo del primer mes de funcionamiento, el riesgo de mercado se considera tomando las posiciones del último día del mes."


---

# CQN-013 — [cadena_restriccion_excepcion] · estrato **primaria**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn.json — el SELLADO)

**Pregunta:** ¿Qué consecuencias sancionatorias enfrenta un sujeto obligado que incumple las normas sobre protección de los usuarios de servicios financieros?

**ground_truth_secciones:** ["TO_proteccion_usuarios_servicios_financieros_actual.pdf Punto 1.2", "TO_proteccion_usuarios_servicios_financieros_actual.pdf Sección 5"]
**tos_fuente:** ["TO_proteccion_usuarios_servicios_financieros_actual.pdf"]
**categoria_generacion:** cadena_normativa
**estrato:** primaria · **disclosure:** familia de prefijo con territorio adjudicado, sin GT compartido

**cita_textual del GT:** "El Banco Central de la República Argentina (BCRA) supervisará la actuación de los sujetos obligados, a quienes les resultarán de aplicación las disposiciones de la Sección 5. en caso de incumplimiento de estas normas. […] El sujeto obligado y quienes resulten responsables serán pasibles de la aplicación de las sanciones previstas en las normas sobre “Régimen disciplinario a cargo del Banco Central de la República Argentina (Leyes 21.526 y 25.065) y tramitación de sumarios cambiarios (Ley 19.359)”, por los in- cumplimientos que se constaten respecto de estas normas"

**respuesta_breve del GT:** El criterio general remite, en caso de incumplimiento, a la sección de sanciones: el sujeto obligado y los responsables son pasibles de las sanciones previstas en las normas sobre “Régimen disciplinario a cargo del BCRA (Leyes 21.526 y 25.065) y tramitación de sumarios cambiarios (Ley 19.359)”, incluso por incumplimientos de los manuales de procedimiento interno.

## 2. Síntoma del juez (verbatim, traza gate_cqn)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "El sujeto obligado que incumple las normas sobre protección de los usuarios de servicios financieros es pasible de las sanciones previstas en las normas sobre 'Régimen disciplinario a cargo del Banco Central de la República Argentina'.",
   "central": true
  },
  {
   "enunciado": "Las sanciones del régimen disciplinario se aplican conforme a la Ley 21.526.",
   "central": true
  },
  {
   "enunciado": "Las sanciones del régimen disciplinario se aplican conforme a la Ley 25.065.",
   "central": true
  },
  {
   "enunciado": "Las sanciones incluyen la tramitación de sumarios cambiarios según la Ley 19.359.",
   "central": true
  },
  {
   "enunciado": "Los incumplimientos en el envío de información están sujetos a la aplicación del artículo 41 de la Ley de Entidades Financieras.",
   "central": true
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "Consecuencias sancionatorias que enfrenta un sujeto obligado que incumple las normas sobre protección de los usuarios de servicios financieros"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "El sujeto obligado que incumple las normas sobre protección de los usuarios de servicios financieros es pasible de las sanciones previstas en las normas sobre 'Régimen disciplinario a cargo del Banco Central de la República Argentina'.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Las sanciones del régimen disciplinario se aplican conforme a la Ley 21.526.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Las sanciones del régimen disciplinario se aplican conforme a la Ley 25.065.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Las sanciones incluyen la tramitación de sumarios cambiarios según la Ley 19.359.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Los incumplimientos en el envío de información están sujetos a la aplicación del artículo 41 de la Ley de Entidades Financieras.",
  "central": true,
  "verdict": "no_soportado"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Consecuencias sancionatorias que enfrenta un sujeto obligado que incumple las normas sobre protección de los usuarios de servicios financieros",
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
   "Los incumplimientos en el envío de información están sujetos a la aplicación del artículo 41 de la Ley de Entidades Financieras."
  ],
  "secundarias": [],
  "n_centrales": 1,
  "n_secundarias": 0
 },
 "requiere_adjudicacion_humana": true,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "La cita apunta al documento correcto (TO_proteccion_usuarios_servicios_financieros_actual.pdf) a nivel de punto, aunque el punto citado (4.4) difiere de los puntos del referente (1.2 y Sección 5)."
 }
}
```

**Síntoma (resumen mecánico, mismo filtro que build_falla_context): F = 1 claims reprobados (1 centrales) · P = 0 patas no cubiertas → síntoma NO VACÍO.**

## 3. Trayectoria

En la parte 2 (`expediente_gate_2.md`, sección "CQN-013").

## 4. Homólogos / territorio

**Disclosure del eval set (verbatim):** familia de prefijo con territorio adjudicado, sin GT compartido

**Territorio en varas previas** (barrido mecánico; cada entrada rotulada):

- GT `TO_proteccion_usuarios_servicios_financieros_actual.pdf Sección 5` (punto 5) en **casos_control.md** — 5 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L3): Referencia del **Paso 3, sub-fase A**. Antes de analizar todo el dataset, el agente corre su análisis sobre estas 5 preguntas, cuya atribución humana ya está documentada, y se comp
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L5): **Las 5 preguntas-control:** CQ-031, CQ-034, CQ-017, CQ-020, CQ-025. Son las 5 fallas de `run_3` sobre `eval_set_v1`, ya diagnosticadas a mano por la autora.
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L13): 3. **Umbral de calibración:** sugerido **≥4 de 5** coincidencias. **El umbral exacto lo decide la autora**; es un parámetro afinable, no un valor congelado.
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L24): > **Nota de procedencia (importante, leer).** Las preguntas y sus `ground_truth_secciones`/`cita_textual` salen verbatim de `data/experiment/evaluacion/queries/eval_set_v2.json` (p
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L86): ## Por qué estos 5 y no otros
- GT `TO_proteccion_usuarios_servicios_financieros_actual.pdf Sección 5` (punto 5) en **casos_piloto.md** — 5 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L17): **Los 5 casos** (todos off/run_3): CQ-018 (síntoma central), CQ-019 y CQ-033 (síntoma
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L82): - **Nota (disclosure):** dos homólogos dev (`on/run_1/CQ-019`, `on/run_5/CQ-019`) — otros
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L116): ídem (límites 14%/8%/5%); verificar en la ronda de refinamiento si existen portadores de
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L146): - **Pregunta:** ¿Con qué periodicidad mínima debe clasificarse un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC, y en qué casos la reevaluación de
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L170): en el contenido (grupo B 17%/11%/7%; grupo C 14%/8%/5%); verificar portadores de los
- GT `TO_proteccion_usuarios_servicios_financieros_actual.pdf Sección 5` (punto 5) en **casos_validacion.md** — 9 línea(s), primeras 6:
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L108): - **Nota (disclosure):** homólogos dev on/run_1 y on/run_5, y piloto run_3 — otros grafos.
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L119): (verificaciones_validacion_1.md §5a-5b):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L138): (29 solo en provenances, ninguno con la regla — verificaciones §5c); el único nodo
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L146): - **Evidencia:** verificaciones_validacion_1.md §5; expediente_validacion_1.md (caso
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L175): - **Nota (disclosure):** homólogos dev off/run_5 y gate run_3 — otros grafos.
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L191): factor vinculado a la calificación… SEFYC", tabla 1→1 … 5→1,19, verificada contra el
- GT `TO_proteccion_usuarios_servicios_financieros_actual.pdf Sección 5` (punto 5) en **casos_dev_v7.md** — 5 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L50): - **Evidencia:** expediente_dev_v7_1.md (§1-2-5) + expediente_dev_v7_2.md (trayectoria,
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L74): - **Evidencia:** expediente_dev_v7_1.md (§1-2-5) + expediente_dev_v7_2.md (trayectoria,
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L102): - **Evidencia:** expediente_dev_v7_1.md (§1-2-5) + expediente_dev_v7_2.md (trayectoria,
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L136): - **Evidencia:** expediente_dev_v7_1.md (§1-2-5) + expediente_dev_v7_2.md (trayectoria,
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L145): con la regla de frenado de v5.7: lo que el dev motiva se valida sobre material que el dev

## 5. Tabla inicial de hechos (cero adjudicación)

**Claims reprobados en juego:**
- CENTRAL `no_soportado`: "Los incumplimientos en el envío de información están sujetos a la aplicación del artículo 41 de la Ley de Entidades Financieras."

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Consecuencias sancionatorias que enfrenta un sujeto obligado que incumple las normas sobre protección de los usuarios de servicios financieros | cubierta | 1, 2, 3, 4, 5, 13, 14, 15 |

**Descomposición del juez (qué dice la respuesta, verbatim step1):**
- afirmación (central): "El sujeto obligado que incumple las normas sobre protección de los usuarios de servicios financieros es pasible de las sanciones previstas en las normas sobre 'Régimen disciplinario a cargo del Banco Central de la República Argentina'."
- afirmación (central): "Las sanciones del régimen disciplinario se aplican conforme a la Ley 21.526."
- afirmación (central): "Las sanciones del régimen disciplinario se aplican conforme a la Ley 25.065."
- afirmación (central): "Las sanciones incluyen la tramitación de sumarios cambiarios según la Ley 19.359."
- afirmación (central): "Los incumplimientos en el envío de información están sujetos a la aplicación del artículo 41 de la Ley de Entidades Financieras."


---

# CQN-014 — [cadena_restriccion_excepcion] · estrato **solapada**

## 1. Pregunta y ground truth (verbatim, queries/eval_set_cqn.json — el SELLADO)

**Pregunta:** Si una entidad financiera del grupo 2 no registró ingreso bruto positivo en ninguno de los períodos de 12 meses de los últimos 36 meses, ¿qué exigencia de capital por riesgo operacional debe observar?

**ground_truth_secciones:** ["TO_capitales_minimos_actual.pdf Punto 7.2", "TO_capitales_minimos_actual.pdf Punto 7.3"]
**tos_fuente:** ["TO_capitales_minimos_actual.pdf"]
**categoria_generacion:** cadena_normativa
**estrato:** solapada · **disclosure:** GT 7.3 compartido con CQ-033; en run_3 sus nodos de destino portan defectos adjudicados (familia 12.3)

**cita_textual del GT:** "Cuando n sea igual a cero (n=0), deberá observarse una exigencia equivalente al límite previsto en el punto 7.3. […] La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar: 7.3.1. El 20% en el caso de entidades del grupo A del promedio de los últimos 36 meses –anteriores al mes a que corresponda la determinación de la exigencia– de la exigencia de capital mínimo por riesgo de crédito calculada según lo previsto en la Sección 2., ex- presada en moneda homogénea del mes anterior al que se efectúa el cálculo. 7.3.2. El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses"

**respuesta_breve del GT:** Con n=0 debe observar una exigencia equivalente al límite fijado para el grupo 2: el 20 % (entidades del grupo A) o el 17 % (entidades del grupo B) del promedio de los últimos 36 meses de la exigencia de capital mínimo por riesgo de crédito, expresada en moneda homogénea del mes anterior al cálculo.

## 2. Síntoma del juez (verbatim, traza gate_cqn)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Si una entidad financiera del grupo 2 no registró ingreso bruto positivo en ninguno de los períodos de 12 meses de los últimos 36 meses, el valor de n es igual a 0.",
   "central": true
  },
  {
   "enunciado": "Cuando n=0, la entidad del grupo 2 debe observar una exigencia de capital por riesgo operacional equivalente al límite previsto en el punto 7.3 de las normas sobre Capitales mínimos de las entidades financieras.",
   "central": true
  },
  {
   "enunciado": "El punto 7.3 de las normas sobre Capitales mínimos de las entidades financieras establece un límite aplicable a la exigencia de capital por riesgo operacional.",
   "central": false
  }
 ],
 "reportes_de_alcance": [
  "La respuesta fue marcada como no respondible (respondible: false), lo que indica que el sistema no pudo determinar con certeza el valor concreto de la exigencia, remitiendo al punto 7.3 sin especificar su contenido."
 ],
 "patas_de_la_pregunta": [
  "Exigencia de capital por riesgo operacional que debe observar una entidad financiera del grupo 2 que no registró ingreso bruto positivo en ninguno de los períodos de 12 meses de los últimos 36 meses"
 ]
}
```

`judge.step2.verificaciones`:

```json
[
 {
  "enunciado": "Si una entidad financiera del grupo 2 no registró ingreso bruto positivo en ninguno de los períodos de 12 meses de los últimos 36 meses, el valor de n es igual a 0.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Cuando n=0, la entidad del grupo 2 debe observar una exigencia de capital por riesgo operacional equivalente al límite previsto en el punto 7.3 de las normas sobre Capitales mínimos de las entidades financieras.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "El punto 7.3 de las normas sobre Capitales mínimos de las entidades financieras establece un límite aplicable a la exigencia de capital por riesgo operacional.",
  "central": false,
  "verdict": "verdadero"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Exigencia de capital por riesgo operacional que debe observar una entidad financiera del grupo 2 que no registró ingreso bruto positivo en ninguno de los períodos de 12 meses de los últimos 36 meses",
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
  "completitud": "Patas no cubiertas: Exigencia de capital por riesgo operacional que debe observar una entidad financiera del grupo 2 que no registró ingreso bruto positivo en ninguno de los períodos de 12 meses de los últimos 36 meses",
  "citas": "El agente cita TO_capitales_minimos_actual.pdf Punto 7.2, que corresponde a uno de los ground truth secciones, con precisión a nivel punto."
 }
}
```

**Síntoma (resumen mecánico, mismo filtro que build_falla_context): F = 0 claims reprobados (0 centrales) · P = 1 patas no cubiertas → síntoma NO VACÍO.**

## 3. Trayectoria

En la parte 2 (`expediente_gate_2.md`, sección "CQN-014").

## 4. Homólogos / territorio

**Disclosure del eval set (verbatim):** GT 7.3 compartido con CQ-033; en run_3 sus nodos de destino portan defectos adjudicados (familia 12.3)

**Territorio en varas previas** (barrido mecánico; cada entrada rotulada):

- GT `TO_capitales_minimos_actual.pdf Punto 7.2` (punto 7.2) en **casos_piloto.md** — 2 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L74): descripción verbatim de la 7.2.1, provenance "Punto 7.2" —, y es correcto contra el corpus:
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L76): "Clasif 7.2.1 — Situación normal: puntual o ≤31 días"
- GT `TO_capitales_minimos_actual.pdf Punto 7.3` (punto 7.3) en **casos_piloto.md** — 3 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L101): El límite general del 17% (7.3.2 del PDF) es permanente, sin esa vigencia. El nodo,
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L117): los límites permanentes 7.3.1/7.3.2.
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L171): límites permanentes 7.3.1/7.3.2 (CQ-033).
- GT `TO_capitales_minimos_actual.pdf Punto 7.3` (punto 7.3) en **casos_validacion.md** — 1 línea(s):
  - **PRECEDENTE — otra pregunta u otro grafo, NO evidencia de este caso** (L140): recategorización del 7.3, no la obligación, e inalcanzable (D1 false/null); los nodos de

## 5. Tabla inicial de hechos (cero adjudicación)

**Patas × cobertura × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Exigencia de capital por riesgo operacional que debe observar una entidad financiera del grupo 2 que no registró ingreso bruto positivo en ninguno de los períodos de 12 meses de los últimos 36 meses | no_cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 |

**Descomposición del juez (qué dice la respuesta, verbatim step1):**
- afirmación (central): "Si una entidad financiera del grupo 2 no registró ingreso bruto positivo en ninguno de los períodos de 12 meses de los últimos 36 meses, el valor de n es igual a 0."
- afirmación (central): "Cuando n=0, la entidad del grupo 2 debe observar una exigencia de capital por riesgo operacional equivalente al límite previsto en el punto 7.3 de las normas sobre Capitales mínimos de las entidades financieras."
- afirmación (no central): "El punto 7.3 de las normas sobre Capitales mínimos de las entidades financieras establece un límite aplicable a la exigencia de capital por riesgo operacional."
- reporte de alcance: "La respuesta fue marcada como no respondible (respondible: false), lo que indica que el sistema no pudo determinar con certeza el valor concreto de la exigencia, remitiendo al punto 7.3 sin especificar su contenido."
