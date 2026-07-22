# Expediente de adjudicación — RESERVA v7 (dev de S1) — 4 casos — parte 1

Fecha: 2026-07-16. SOLO LECTURA; escrituras: los 2 archivos del expediente. Marco
POST-HOC (off). **Ni verificador, ni capa determinística, ni S1 corrieron sobre estos
casos** — son la reserva pre-registrada, intocada hasta hoy.
**Cero adjudicación**: hechos verbatim con ruta de origen.

Partes: 1 = secciones 1-2-4-5 de los 4 casos; 2 = trayectorias completas (sección 3).

Fuentes: `queries/eval_set_v1.json`, `posthoc_run/traces/off/run_2|run_4/`,
barrido mecánico de homólogos sobre `referencias_dev_set.md`, `casos_control.md`,
`casos_piloto.md`, `casos_validacion.md`.


---

# run_2/CQ-021 — [factual_directa] · reserva v7

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** ¿En qué casos es optativo para la entidad comunicar al deudor un cambio negativo en su clasificación, y de qué régimen depende el umbral?

**ground_truth_secciones:** ["Clasificación, Punto 3.4.2 (Contenido del legajo)"]
**tos_fuente:** ["clasificacion"]

**cita_textual del GT:** "Las entidades financieras deberán comunicar a los deudores los cambios negativos en la clasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al monto establecido en el punto 2. 'Deudores Comprendidos' de la Sección 3. 'Deudores del sistema financiero' –Normas de Procedimiento– del Régimen Informativo Contable Mensual. Deberán informarse los cambios negativos en la clasificación a los deudores que sean clasificados en las situaciones 3, 4 o 5 y de los deudores en gestión judicial o extrajudicial de cobro (estos últimos, en la medida que cuenten con notificaciones postales o fehacientes respecto al inicio de las gestiones de cobro). Tal información deberá ser remitida a los deudores comprendidos dentro de los 45 días de realizada la reclasificación [...]"

## 2. Síntoma POST-HOC (verbatim, `posthoc_run/traces/off/run_2/CQ-021.json` → judge)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Existe una obligación general de comunicar cambios negativos en clasificación dentro de 45 días de realizada la reclasificación.",
   "central": false
  }
 ],
 "reportes_de_alcance": [
  "No se encontró información en el Knowledge Graph sobre casos específicos en que sea optativo para la entidad comunicar cambios negativos en la clasificación del deudor.",
  "No se encontró información sobre qué régimen determina el umbral para la comunicación optativa.",
  "Los detalles sobre excepciones optativas y los regímenes que establecen umbrales no están disponibles en la documentación consultada."
 ],
 "patas_de_la_pregunta": [
  "Casos en que es optativo para la entidad comunicar al deudor un cambio negativo en su clasificación",
  "Régimen del que depende el umbral para dicha opcionalidad"
 ]
}
```

`judge.step2.verificaciones` (por claim, con veredicto y centralidad):

```json
[
 {
  "enunciado": "Existe una obligación general de comunicar cambios negativos en clasificación dentro de 45 días de realizada la reclasificación.",
  "central": false,
  "verdict": "verdadero"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Casos en que es optativo para la entidad comunicar al deudor un cambio negativo en su clasificación",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "Régimen del que depende el umbral para dicha opcionalidad",
  "cobertura": "no_cubierta"
 }
]
```

`judge.verdict` (correctitud/completitud/no-soportadas):

```json
{
 "correctitud": "correcta",
 "completitud": "parcial",
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [],
  "n_centrales": 0,
  "n_secundarias": 0
 }
}
```

**Síntoma (resumen mecánico, mismo filtro que build_falla_context): F = 0 claims reprobados · P = 2 patas no cubiertas → síntoma NO VACÍO.**

## 3. Trayectoria post-hoc

En la parte 2 del expediente (`expediente_dev_v7_2.md`, sección "run_2/CQ-021"): respuesta final íntegra, inventario con fidelidad 15/15 y apéndice de outputs completos.

## 4. Homólogos de etapas previas

**SIN USO PREVIO EN NINGUNA ETAPA** — run_2/CQ-021 integra la reserva pre-registrada del protocolo de validación (`docs/protocolo_validacion_v61.md`): excluido del dev, del gate, del piloto y de la validación por diseño.

Barrido mecánico de la MISMA CQ sobre otros grafos (`grep -n "CQ-021"` en referencias_dev_set.md, casos_control.md, casos_piloto.md, casos_validacion.md): **cero apariciones** — esta CQ no fue adjudicada sobre NINGÚN grafo en ninguna etapa.

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES reprobados en juego (post-hoc):** ninguno.

**Patas (step1) × cobertura (step2) × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Casos en que es optativo para la entidad comunicar al deudor un cambio negativo en su clasificación | no_cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 |
| Régimen del que depende el umbral para dicha opcionalidad | no_cubierta | 7, 10 |

**Qué dice la respuesta por pata — descomposición del juez (verbatim, step1):**
- afirmación verificable (no central): "Existe una obligación general de comunicar cambios negativos en clasificación dentro de 45 días de realizada la reclasificación."
- reporte de alcance: "No se encontró información en el Knowledge Graph sobre casos específicos en que sea optativo para la entidad comunicar cambios negativos en la clasificación del deudor."
- reporte de alcance: "No se encontró información sobre qué régimen determina el umbral para la comunicación optativa."
- reporte de alcance: "Los detalles sobre excepciones optativas y los regímenes que establecen umbrales no están disponibles en la documentación consultada."


---

# run_4/CQ-008 — [factual_directa] · reserva v7

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** Cuando un cliente lo solicita, ¿en qué plazo debe la entidad financiera comunicarle la última clasificación que le asignó?

**ground_truth_secciones:** ["Punto 8.1 (Informaciones a suministrar)"]
**tos_fuente:** ["clasificacion"]

**cita_textual del GT:** "A solicitud de cada cliente, dentro de los 10 días corridos del pedido, la entidad financiera deberá comunicarle la última clasificación que le ha asignado, junto con los fundamentos que la justifican según la evaluación realizada por la entidad, el importe total de deudas con el sistema financiero y las clasificaciones asignadas que surjan de la última información disponible en la 'Central de deudores del sistema financiero'."

## 2. Síntoma POST-HOC (verbatim, `posthoc_run/traces/off/run_4/CQ-008.json` → judge)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [],
 "reportes_de_alcance": [
  "No se encontró en el Knowledge Graph información específica sobre el plazo en el cual la entidad financiera debe comunicar la última clasificación asignada a un cliente cuando este lo solicita.",
  "El grafo contiene normativa sobre clasificación de deudores y obligaciones de las entidades financieras.",
  "El grafo no incluye la disposición regulatoria que establece este plazo particular."
 ],
 "patas_de_la_pregunta": [
  "Plazo en que la entidad financiera debe comunicar al cliente la última clasificación que le asignó, cuando el cliente lo solicita"
 ]
}
```

`judge.step2.verificaciones` (por claim, con veredicto y centralidad):

```json
[]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Plazo en que la entidad financiera debe comunicar al cliente la última clasificación que le asignó, cuando el cliente lo solicita",
  "cobertura": "no_cubierta"
 }
]
```

`judge.verdict` (correctitud/completitud/no-soportadas):

```json
{
 "correctitud": "correcta",
 "completitud": "parcial",
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [],
  "n_centrales": 0,
  "n_secundarias": 0
 }
}
```

**Síntoma (resumen mecánico, mismo filtro que build_falla_context): F = 0 claims reprobados · P = 1 patas no cubiertas → síntoma NO VACÍO.**

## 3. Trayectoria post-hoc

En la parte 2 del expediente (`expediente_dev_v7_2.md`, sección "run_4/CQ-008"): respuesta final íntegra, inventario con fidelidad 15/15 y apéndice de outputs completos.

## 4. Homólogos de etapas previas

**SIN USO PREVIO EN NINGUNA ETAPA** — run_4/CQ-008 integra la reserva pre-registrada del protocolo de validación (`docs/protocolo_validacion_v61.md`): excluido del dev, del gate, del piloto y de la validación por diseño.

Barrido mecánico de la MISMA CQ sobre otros grafos (`grep -n "CQ-008"` en referencias_dev_set.md, casos_control.md, casos_piloto.md, casos_validacion.md): **cero apariciones** — esta CQ no fue adjudicada sobre NINGÚN grafo en ninguna etapa.

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES reprobados en juego (post-hoc):** ninguno.

**Patas (step1) × cobertura (step2) × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Plazo en que la entidad financiera debe comunicar al cliente la última clasificación que le asignó, cuando el cliente lo solicita | no_cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 |

**Qué dice la respuesta por pata — descomposición del juez (verbatim, step1):**
- reporte de alcance: "No se encontró en el Knowledge Graph información específica sobre el plazo en el cual la entidad financiera debe comunicar la última clasificación asignada a un cliente cuando este lo solicita."
- reporte de alcance: "El grafo contiene normativa sobre clasificación de deudores y obligaciones de las entidades financieras."
- reporte de alcance: "El grafo no incluye la disposición regulatoria que establece este plazo particular."


---

# run_4/CQ-021 — [factual_directa] · reserva v7

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** ¿En qué casos es optativo para la entidad comunicar al deudor un cambio negativo en su clasificación, y de qué régimen depende el umbral?

**ground_truth_secciones:** ["Clasificación, Punto 3.4.2 (Contenido del legajo)"]
**tos_fuente:** ["clasificacion"]

**cita_textual del GT:** "Las entidades financieras deberán comunicar a los deudores los cambios negativos en la clasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al monto establecido en el punto 2. 'Deudores Comprendidos' de la Sección 3. 'Deudores del sistema financiero' –Normas de Procedimiento– del Régimen Informativo Contable Mensual. Deberán informarse los cambios negativos en la clasificación a los deudores que sean clasificados en las situaciones 3, 4 o 5 y de los deudores en gestión judicial o extrajudicial de cobro (estos últimos, en la medida que cuenten con notificaciones postales o fehacientes respecto al inicio de las gestiones de cobro). Tal información deberá ser remitida a los deudores comprendidos dentro de los 45 días de realizada la reclasificación [...]"

## 2. Síntoma POST-HOC (verbatim, `posthoc_run/traces/off/run_4/CQ-021.json` → judge)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "La entidad financiera debe comunicar al deudor un cambio negativo en su clasificación dentro de 45 días",
   "central": false
  },
  {
   "enunciado": "La comunicación del cambio negativo en la clasificación debe realizarse mediante medios especificados por la regulación del BCRA",
   "central": false
  },
  {
   "enunciado": "Existen casos en que la comunicación del cambio negativo en la clasificación es optativa para la entidad",
   "central": true
  },
  {
   "enunciado": "El carácter optativo de la comunicación depende del saldo de deuda del deudor",
   "central": true
  },
  {
   "enunciado": "El umbral que determina cuándo la comunicación es optativa depende de un régimen específico",
   "central": true
  }
 ],
 "reportes_de_alcance": [
  "Los detalles concretos sobre cuáles son los casos optativos no están completamente desarrollados en los nodos consultados",
  "El régimen exacto del que depende el umbral no está completamente desarrollado en los nodos consultados"
 ],
 "patas_de_la_pregunta": [
  "Casos en que es optativo para la entidad comunicar al deudor un cambio negativo en su clasificación",
  "Régimen del que depende el umbral para determinar esa opcionalidad"
 ]
}
```

`judge.step2.verificaciones` (por claim, con veredicto y centralidad):

```json
[
 {
  "enunciado": "La entidad financiera debe comunicar al deudor un cambio negativo en su clasificación dentro de 45 días",
  "central": false,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La comunicación del cambio negativo en la clasificación debe realizarse mediante medios especificados por la regulación del BCRA",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Existen casos en que la comunicación del cambio negativo en la clasificación es optativa para la entidad",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "El carácter optativo de la comunicación depende del saldo de deuda del deudor",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "El umbral que determina cuándo la comunicación es optativa depende de un régimen específico",
  "central": true,
  "verdict": "verdadero"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Casos en que es optativo para la entidad comunicar al deudor un cambio negativo en su clasificación",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "Régimen del que depende el umbral para determinar esa opcionalidad",
  "cobertura": "no_cubierta"
 }
]
```

`judge.verdict` (correctitud/completitud/no-soportadas):

```json
{
 "correctitud": "correcta",
 "completitud": "parcial",
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [
   "La comunicación del cambio negativo en la clasificación debe realizarse mediante medios especificados por la regulación del BCRA"
  ],
  "n_centrales": 0,
  "n_secundarias": 1
 }
}
```

**Síntoma (resumen mecánico, mismo filtro que build_falla_context): F = 1 claims reprobados · P = 2 patas no cubiertas → síntoma NO VACÍO.**

## 3. Trayectoria post-hoc

En la parte 2 del expediente (`expediente_dev_v7_2.md`, sección "run_4/CQ-021"): respuesta final íntegra, inventario con fidelidad 16/16 y apéndice de outputs completos.

## 4. Homólogos de etapas previas

**SIN USO PREVIO EN NINGUNA ETAPA** — run_4/CQ-021 integra la reserva pre-registrada del protocolo de validación (`docs/protocolo_validacion_v61.md`): excluido del dev, del gate, del piloto y de la validación por diseño.

Barrido mecánico de la MISMA CQ sobre otros grafos (`grep -n "CQ-021"` en referencias_dev_set.md, casos_control.md, casos_piloto.md, casos_validacion.md): **cero apariciones** — esta CQ no fue adjudicada sobre NINGÚN grafo en ninguna etapa.

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES reprobados en juego (post-hoc):** ninguno.

**Claims secundarios reprobados:**
- "La comunicación del cambio negativo en la clasificación debe realizarse mediante medios especificados por la regulación del BCRA"

**Patas (step1) × cobertura (step2) × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Casos en que es optativo para la entidad comunicar al deudor un cambio negativo en su clasificación | no_cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16 |
| Régimen del que depende el umbral para determinar esa opcionalidad | no_cubierta | 5 |

**Qué dice la respuesta por pata — descomposición del juez (verbatim, step1):**
- afirmación verificable (no central): "La entidad financiera debe comunicar al deudor un cambio negativo en su clasificación dentro de 45 días"
- afirmación verificable (no central): "La comunicación del cambio negativo en la clasificación debe realizarse mediante medios especificados por la regulación del BCRA"
- afirmación verificable (central): "Existen casos en que la comunicación del cambio negativo en la clasificación es optativa para la entidad"
- afirmación verificable (central): "El carácter optativo de la comunicación depende del saldo de deuda del deudor"
- afirmación verificable (central): "El umbral que determina cuándo la comunicación es optativa depende de un régimen específico"
- reporte de alcance: "Los detalles concretos sobre cuáles son los casos optativos no están completamente desarrollados en los nodos consultados"
- reporte de alcance: "El régimen exacto del que depende el umbral no está completamente desarrollado en los nodos consultados"


---

# run_4/CQ-028 — [cadena_restriccion_excepcion] · reserva v7

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** ¿Puede un sujeto obligado cobrar una comisión por la precancelación total de una financiación? ¿Existe algún caso en que no se admita?

**ground_truth_secciones:** ["Punto 2.3.2.1 (Comisiones y cargos admitidos)"]
**tos_fuente:** ["proteccion"]

**cita_textual del GT:** "La precancelación total o parcial de financiaciones podrá dar lugar a la aplicación de comisiones. En el caso de precancelación total, no se admitirá la aplicación de comisiones cuando al momento de efectuarla haya transcurrido al menos la cuarta parte del plazo original de la financiación o 180 días corridos desde su otorgamiento, de ambos el mayor."

## 2. Síntoma POST-HOC (verbatim, `posthoc_run/traces/off/run_4/CQ-028.json` → judge)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Un sujeto obligado puede cobrar comisión por precancelación total de una financiación.",
   "central": true
  },
  {
   "enunciado": "No se admite comisión por precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original.",
   "central": true
  },
  {
   "enunciado": "No se admite comisión por precancelación total cuando hayan transcurrido al menos 180 días desde el inicio de la financiación.",
   "central": true
  },
  {
   "enunciado": "El criterio para no admitir la comisión por precancelación total es el que ocurra primero entre la cuarta parte del plazo original y los 180 días.",
   "central": true
  },
  {
   "enunciado": "La comisión por precancelación parcial se permite sin la restricción temporal mencionada.",
   "central": false
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "Si un sujeto obligado puede cobrar comisión por precancelación total de una financiación",
  "Si existe algún caso en que no se admita dicha comisión"
 ]
}
```

`judge.step2.verificaciones` (por claim, con veredicto y centralidad):

```json
[
 {
  "enunciado": "Un sujeto obligado puede cobrar comisión por precancelación total de una financiación.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "No se admite comisión por precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "No se admite comisión por precancelación total cuando hayan transcurrido al menos 180 días desde el inicio de la financiación.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "El criterio para no admitir la comisión por precancelación total es el que ocurra primero entre la cuarta parte del plazo original y los 180 días.",
  "central": true,
  "verdict": "falso"
 },
 {
  "enunciado": "La comisión por precancelación parcial se permite sin la restricción temporal mencionada.",
  "central": false,
  "verdict": "no_soportado"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Si un sujeto obligado puede cobrar comisión por precancelación total de una financiación",
  "cobertura": "cubierta"
 },
 {
  "pata": "Si existe algún caso en que no se admita dicha comisión",
  "cobertura": "cubierta"
 }
]
```

`judge.verdict` (correctitud/completitud/no-soportadas):

```json
{
 "correctitud": "incorrecta",
 "completitud": "completa",
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [
   "La comisión por precancelación parcial se permite sin la restricción temporal mencionada."
  ],
  "n_centrales": 0,
  "n_secundarias": 1
 }
}
```

**Síntoma (resumen mecánico, mismo filtro que build_falla_context): F = 2 claims reprobados · P = 0 patas no cubiertas → síntoma NO VACÍO.**

## 3. Trayectoria post-hoc

En la parte 2 del expediente (`expediente_dev_v7_2.md`, sección "run_4/CQ-028"): respuesta final íntegra, inventario con fidelidad 15/15 y apéndice de outputs completos.

## 4. Homólogos de etapas previas

**SIN USO PREVIO EN NINGUNA ETAPA** — run_4/CQ-028 integra la reserva pre-registrada del protocolo de validación (`docs/protocolo_validacion_v61.md`): excluido del dev, del gate, del piloto y de la validación por diseño.

Barrido mecánico de la MISMA CQ sobre otros grafos (`grep -n "CQ-028"` en referencias_dev_set.md, casos_control.md, casos_piloto.md, casos_validacion.md): **cero apariciones** — esta CQ no fue adjudicada sobre NINGÚN grafo en ninguna etapa.

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES reprobados en juego (post-hoc):**
- "El criterio para no admitir la comisión por precancelación total es el que ocurra primero entre la cuarta parte del plazo original y los 180 días."

**Claims secundarios reprobados:**
- "La comisión por precancelación parcial se permite sin la restricción temporal mencionada."

**Patas (step1) × cobertura (step2) × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Si un sujeto obligado puede cobrar comisión por precancelación total de una financiación | cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15 |
| Si existe algún caso en que no se admita dicha comisión | cubierta | 1, 6, 7, 9, 11, 12, 13, 14, 15 |

**Qué dice la respuesta por pata — descomposición del juez (verbatim, step1):**
- afirmación verificable (central): "Un sujeto obligado puede cobrar comisión por precancelación total de una financiación."
- afirmación verificable (central): "No se admite comisión por precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original."
- afirmación verificable (central): "No se admite comisión por precancelación total cuando hayan transcurrido al menos 180 días desde el inicio de la financiación."
- afirmación verificable (central): "El criterio para no admitir la comisión por precancelación total es el que ocurra primero entre la cuarta parte del plazo original y los 180 días."
- afirmación verificable (no central): "La comisión por precancelación parcial se permite sin la restricción temporal mencionada."

