# Expediente de adjudicación — validación v6.1-D (8 casos, run_2/run_4) — parte 1

Fecha: 2026-07-16. SOLO LECTURA; escrituras: los 3 archivos del expediente. Marco
POST-HOC (off). Ni verificador ni capa corrieron sobre estos casos (protocolo §5).
**Cero adjudicación**: hechos verbatim con ruta de origen.

Partes: 1 = secciones 1-2-4-5 de los 8 casos; 2 = trayectorias run_2 (sección 3);
3 = trayectorias run_4 (sección 3).

Fuentes: `queries/eval_set_v1.json`, `posthoc_run/traces/off/run_2|run_4/`,
`frozen_run/traces/run_2|run_4/` (solo CONTEXTO FROZEN de los controles),
`referencias_dev_set.md`, `casos_control.md`, `casos_piloto.md` (homólogos, rotulados).


---

# run_2/CQ-015 — [factual_directa] · control negativo

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** A los fines cambiarios, ¿cómo se define a una persona humana como 'residente' del país?

**ground_truth_secciones:** ["Punto 6.5.1 (Residente - Persona humana)"]
**tos_fuente:** ["exterior"]

**cita_textual del GT:** "Se considerará que una persona humana es residente del país dentro de cuya frontera tiene su centro de interés económico o actividad principal. En tal sentido, deberá presumirse que una persona humana es residente de un país si permanece o tiene intención de permanecer en él por al menos un año."

## 2. Síntoma POST-HOC (verbatim, `posthoc_run/traces/off/run_2/CQ-015.json` → judge)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "A los fines cambiarios, una persona humana es 'residente' cuando tiene su centro de interés económico dentro del país.",
   "central": true
  },
  {
   "enunciado": "A los fines cambiarios, una persona humana es 'residente' cuando tiene su actividad principal dentro del país.",
   "central": true
  },
  {
   "enunciado": "A los fines cambiarios, una persona humana es 'residente' cuando tiene la intención de permanecer en el país por al menos un año.",
   "central": true
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "Definición de 'residente' del país para una persona humana a los fines cambiarios"
 ]
}
```

`judge.step2.verificaciones` (por claim, con veredicto y centralidad):

```json
[
 {
  "enunciado": "A los fines cambiarios, una persona humana es 'residente' cuando tiene su centro de interés económico dentro del país.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "A los fines cambiarios, una persona humana es 'residente' cuando tiene su actividad principal dentro del país.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "A los fines cambiarios, una persona humana es 'residente' cuando tiene la intención de permanecer en el país por al menos un año.",
  "central": true,
  "verdict": "verdadero"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Definición de 'residente' del país para una persona humana a los fines cambiarios",
  "cobertura": "cubierta"
 }
]
```

`judge.verdict` (correctitud/completitud/no-soportadas):

```json
{
 "correctitud": "correcta",
 "completitud": "completa",
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [],
  "n_centrales": 0,
  "n_secundarias": 0
 }
}
```

**SÍNTOMA VACÍO (explícito):** 0 claims reprobados · 0 patas no cubiertas — correctitud `correcta`, completitud `completa`.

**CONTEXTO FROZEN (rotulado: NO es el marco de adjudicación — es la falla que metió el caso al censo; `frozen_run/traces/run_2/CQ-015.json` + reporte ETAPA 2):**

- rep 1: correctitud `correcta` · completitud `completa` · no_sop c/s = 1/0
    - no soportada (CENTRAL): "La definición de residente a los fines cambiarios para personas humanas requiere cumplir con al menos uno de los tres criterios mencionados (no todos simultáneamente)."
- rep 2: correctitud `correcta` · completitud `completa` · no_sop c/s = 0/0
- rep 3: correctitud `correcta` · completitud `completa` · no_sop c/s = 1/0
    - no soportada (CENTRAL): "Los tres criterios mencionados son alternativos (basta cumplir uno de ellos)."
- correctitud FINAL modal del frozen: **incorrecta (reporte ETAPA 2 §3: {'incorrecta': 2, 'correcta': 1})**

## 3. Trayectoria post-hoc

En la parte 2 del expediente (`expediente_validacion_2.md`, sección "run_2/CQ-015"): respuesta final íntegra, inventario con fidelidad 4/4 y apéndice de outputs completos.

## 4. Homólogos de etapas previas

**SIN HOMÓLOGO en ninguna etapa previa** (ni dev, ni gate, ni piloto).

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES reprobados en juego (post-hoc):** ninguno.

**Patas (step1) × cobertura (step2) × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Definición de 'residente' del país para una persona humana a los fines cambiarios | cubierta | 1, 2, 3, 4 |

**Qué dice la respuesta por pata — descomposición del juez (verbatim, step1):**
- afirmación verificable (central): "A los fines cambiarios, una persona humana es 'residente' cuando tiene su centro de interés económico dentro del país."
- afirmación verificable (central): "A los fines cambiarios, una persona humana es 'residente' cuando tiene su actividad principal dentro del país."
- afirmación verificable (central): "A los fines cambiarios, una persona humana es 'residente' cuando tiene la intención de permanecer en el país por al menos un año."


---

# run_2/CQ-018 — [multi_norma] · deliberado (severidad)

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** Los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas, ¿deben cumplir con Protección al Usuario y, además, clasificar a sus deudores? ¿Bajo qué criterio clasifican?

**ground_truth_secciones:** ["Protección, Puntos 1.1.2.4 y 1.1.2.5", "Clasificación, Punto 10.1"]
**tos_fuente:** ["proteccion", "clasificacion"]

**cita_textual del GT:** "[Protección 1.1.2.4/1.1.2.5] Empresas no financieras emisoras de tarjetas de crédito y/o compra [...] Otros proveedores no financieros de crédito [...] | [Clasificación 10.1] Las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito [...] deberán clasificar a los respectivos deudores en función de su mora, según los criterios aplicables para la cartera de 'consumo o vivienda' y por aplicación de las disposiciones previstas en el punto 7.3."

## 2. Síntoma POST-HOC (verbatim, `posthoc_run/traces/off/run_2/CQ-018.json` → judge)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Los proveedores no financieros de crédito deben cumplir con normas de protección de usuarios.",
   "central": true
  },
  {
   "enunciado": "Los proveedores no financieros de crédito deben considerar y resolver fundadamente reclamos de usuarios.",
   "central": true
  },
  {
   "enunciado": "Los proveedores no financieros de crédito deben clasificar deudores según mora en cartera de consumo/vivienda.",
   "central": true
  },
  {
   "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito deben cumplir con normas de protección de usuarios.",
   "central": true
  },
  {
   "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito deben resolver reclamos de usuarios.",
   "central": true
  },
  {
   "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito deben entregar información sobre productos y servicios.",
   "central": false
  },
  {
   "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito deben publicar contratos.",
   "central": false
  },
  {
   "enunciado": "El criterio básico de clasificación de deudores es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía, medida a través del análisis de flujo de fondos.",
   "central": true
  },
  {
   "enunciado": "Los criterios objetivos de clasificación de deudores incluyen el término de morosidad.",
   "central": true
  },
  {
   "enunciado": "Los criterios objetivos de clasificación de deudores incluyen la situación jurídica del cliente o sus deudas.",
   "central": true
  },
  {
   "enunciado": "Los criterios objetivos de clasificación de deudores incluyen el cumplimiento de refinanciaciones.",
   "central": true
  }
 ],
 "reportes_de_alcance": [
  "En la información disponible en el grafo no se encontró una obligación explícita de clasificación de deudores para las empresas no financieras emisoras de tarjetas de crédito."
 ],
 "patas_de_la_pregunta": [
  "Si los proveedores no financieros de crédito deben cumplir con Protección al Usuario",
  "Si los proveedores no financieros de crédito deben clasificar a sus deudores",
  "Si las empresas no financieras emisoras de tarjetas deben cumplir con Protección al Usuario",
  "Si las empresas no financieras emisoras de tarjetas deben clasificar a sus deudores",
  "Bajo qué criterio clasifican sus deudores"
 ]
}
```

`judge.step2.verificaciones` (por claim, con veredicto y centralidad):

```json
[
 {
  "enunciado": "Los proveedores no financieros de crédito deben cumplir con normas de protección de usuarios.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Los proveedores no financieros de crédito deben considerar y resolver fundadamente reclamos de usuarios.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Los proveedores no financieros de crédito deben clasificar deudores según mora en cartera de consumo/vivienda.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito deben cumplir con normas de protección de usuarios.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito deben resolver reclamos de usuarios.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito deben entregar información sobre productos y servicios.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito deben publicar contratos.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "El criterio básico de clasificación de deudores es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía, medida a través del análisis de flujo de fondos.",
  "central": true,
  "verdict": "falso"
 },
 {
  "enunciado": "Los criterios objetivos de clasificación de deudores incluyen el término de morosidad.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Los criterios objetivos de clasificación de deudores incluyen la situación jurídica del cliente o sus deudas.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Los criterios objetivos de clasificación de deudores incluyen el cumplimiento de refinanciaciones.",
  "central": true,
  "verdict": "no_soportado"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Si los proveedores no financieros de crédito deben cumplir con Protección al Usuario",
  "cobertura": "cubierta"
 },
 {
  "pata": "Si los proveedores no financieros de crédito deben clasificar a sus deudores",
  "cobertura": "cubierta"
 },
 {
  "pata": "Si las empresas no financieras emisoras de tarjetas deben cumplir con Protección al Usuario",
  "cobertura": "cubierta"
 },
 {
  "pata": "Si las empresas no financieras emisoras de tarjetas deben clasificar a sus deudores",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "Bajo qué criterio clasifican sus deudores",
  "cobertura": "cubierta"
 }
]
```

`judge.verdict` (correctitud/completitud/no-soportadas):

```json
{
 "correctitud": "incorrecta",
 "completitud": "parcial",
 "afirmaciones_no_soportadas": {
  "centrales": [
   "Los proveedores no financieros de crédito deben considerar y resolver fundadamente reclamos de usuarios.",
   "Las empresas no financieras emisoras de tarjetas de crédito deben resolver reclamos de usuarios.",
   "Los criterios objetivos de clasificación de deudores incluyen el término de morosidad.",
   "Los criterios objetivos de clasificación de deudores incluyen la situación jurídica del cliente o sus deudas.",
   "Los criterios objetivos de clasificación de deudores incluyen el cumplimiento de refinanciaciones."
  ],
  "secundarias": [
   "Las empresas no financieras emisoras de tarjetas de crédito deben entregar información sobre productos y servicios.",
   "Las empresas no financieras emisoras de tarjetas de crédito deben publicar contratos."
  ],
  "n_centrales": 5,
  "n_secundarias": 2
 }
}
```

## 3. Trayectoria post-hoc

En la parte 2 del expediente (`expediente_validacion_2.md`, sección "run_2/CQ-018"): respuesta final íntegra, inventario con fidelidad 15/15 y apéndice de outputs completos.

## 4. Homólogos de etapas previas

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** — dev set (run_1) (verbatim, `referencias_dev_set.md`):

````markdown
## Caso off/run_1/CQ-018 (expansión post-gate #1)

**Pregunta:** Los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas, ¿deben cumplir con Protección al Usuario y, además, clasificar a sus deudores? ¿Bajo qué criterio clasifican?

Adjudicación de la autora, 2026-07-15, asistida por revisión:

- **Claims de "Situación normal" y "Riesgo bajo"** — **`{noise_sensitivity, contenido_kg}` PRIMARIA.** Evidencia: ambos ecos verbatim de nodos defectuosos. `cla_situacion_normal_clasificacion_de_deudores` porta la definición COMERCIAL (6.5.1, "flujo de fondos") sin marca de alcance bajo label genérico — la definición pertinente al criterio de los PNFC es la de consumo (7.2.1, "puntual ≤31 días"); nodo des-scopeado (precedente: CQ-024 dev). `cla_riesgo_bajo_...` define riesgo bajo como "puntual o ≤31 días en refinanciaciones periódicas", que contradice el 7.2.2 ("atrasos de más de 31 hasta 90 días") — definición errónea.
- **Riesgo medio / riesgo alto / irrecuperable + los dos claims del Directivo Responsable** — **FALSOS POSITIVOS DEL JUEZ, sin par (×5).** Evidencia: los 3 de categorías son ecos de nodos expuestos, correctos contra 7.2.3/7.2.4/7.2.5 verbatim; los 2 del Directivo Responsable están soportados por `rsj_directivo_...` expuesto y los edges `debe_designar` de los pasos 7-8, correctos contra Protección 3.2.1.1 ("las empresas no financieras emisoras... y los otros proveedores no financieros de crédito... deberán designar"). Mecanismo de los 3 de categorías: contenido verdadero del corpus fuera de `ground_truth_secciones` — tercer caso del patrón (con run_3/CQ-020 y on/run_5/CQ-019).
- **Observación sin par:** `cla_riesgo_alto` y `cla_irrecuperable` tienen provenances VACÍAS (`[]`) — imperfección real del grafo, sin efecto en este veredicto (las citas de la respuesta salieron de otros nodos).
- **Patrón de calibración: "primaria única + FPs masivos"** — acierto = la primaria `{noise_sensitivity, contenido_kg}`.

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion_v2.md` (scratch, no versionado).
````

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** — vara del piloto (run_3) (verbatim, `casos_piloto.md`):

````markdown
## CQ-018 — `multi_norma` · TOs: proteccion, clasificacion

- **Pregunta:** Los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas, ¿deben cumplir con Protección al Usuario y, además, clasificar a sus deudores? ¿Bajo qué criterio clasifican?
- **Síntoma post-hoc (verbatim, 4 no_soportados — 1 central):**
  - [no_soportado/central] "El criterio básico para efectuar la clasificación de deudores es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía."
  - [no_soportado] "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA."
  - [no_soportado] "El énfasis en la clasificación se pone en el análisis de los flujos de fondos del cliente."
  - [no_soportado] "La clasificación evalúa si el cliente es capaz de atender adecuadamente todos sus compromisos financieros."
- **GT: SIN PRIMARIA** (regla de jerarquía FP-centrales, v2.6: el único central reprobado es
  falso positivo del juez → el caso no tiene primaria). **Los 4 no_soportados son FALSOS
  POSITIVOS DEL JUEZ, sin par:**
  - **(a) el central del "criterio básico... capacidad de pago":** eco casi verbatim del nodo
    `Obligacion_evaluar_capacidad_de_pago`, **abierto por el agente en el paso 13**
    (contenido íntegro y provenance en
    `docs/evidencia_capa_d/verificacion_estructura_piloto.md` §3) — claim SOPORTADO; y
    correcto contra el PDF: Clasificación **4.2**, verificado contra la página ("El criterio
    básico a ser utilizado para efectuar tal clasificación es la capacidad de pago en el
    futuro..."). **Contrafáctico de provenance:** la provenance del nodo dice "Punto 4.1.
    Niveles de clasificación." y el contenido es del 4.2; corregirla NO cambia el veredicto
    del juez — el `ground_truth_secciones` del caso es Protección 1.1.2.4/1.1.2.5 +
    Clasificación 10.1, y una cita al 4.2 sigue fuera de ese marco → la provenance corrida
    NO participó de esta falla. **HALLAZGO LATERAL al backlog** (no secundaria de este GT).
  - **(b) el del Directivo Responsable:** eco del nodo abierto en el **paso 4**
    (`Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr`,
    provenance Protección "Punto 3.2. Controles."; contenido íntegro en
    `verificacion_estructura_piloto.md` §3) — soportado; oración verificada contra el corpus.
  - **(c) el del "énfasis... análisis de los flujos de fondos":** EXPUESTO en el output
    completo del **paso 12** (`docs/evidencia_piloto/verificaciones_piloto.md` §1a) —
    soportado; correcto contra Clasificación **4.3.1**.
  - **(d) el del "atender adecuadamente todos sus compromisos":** EXPUESTO en los outputs
    completos de los **pasos 11 y 12** (`verificaciones_piloto.md` §1b); el portador
    `Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien`
    es fiel al 6.5.1 y declara su alcance en su propio contenido — soportado y correcto.
- **REGLA DE ACIERTO:** acierto = emitir el caso **sin primarias** (el central como
  `sin_defecto`/sin par); las secundarias no se exigen; **CUALQUIER primaria = miss**.
- **Evidencia:** `docs/evidencia_piloto/expediente_piloto_1.md` (caso CQ-018: síntoma,
  respuesta, inventario) y `expediente_piloto_2.md` (outputs completos);
  `docs/evidencia_piloto/verificaciones_piloto.md` §1;
  `docs/evidencia_capa_d/verificacion_estructura_piloto.md` §2-§3.
- **Nota (disclosure):** homólogo dev `off/run_1/CQ-018` — otro grafo, precedente
  taxonómico, no evidencia de este caso.
````

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES reprobados en juego (post-hoc):**
- "Los proveedores no financieros de crédito deben considerar y resolver fundadamente reclamos de usuarios."
- "Las empresas no financieras emisoras de tarjetas de crédito deben resolver reclamos de usuarios."
- "El criterio básico de clasificación de deudores es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía, medida a través del análisis de flujo de fondos."
- "Los criterios objetivos de clasificación de deudores incluyen el término de morosidad."
- "Los criterios objetivos de clasificación de deudores incluyen la situación jurídica del cliente o sus deudas."
- "Los criterios objetivos de clasificación de deudores incluyen el cumplimiento de refinanciaciones."

**Patas (step1) × cobertura (step2) × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Si los proveedores no financieros de crédito deben cumplir con Protección al Usuario | cubierta | 1, 2, 4, 5, 7, 8, 9, 10, 13, 14, 15 |
| Si los proveedores no financieros de crédito deben clasificar a sus deudores | cubierta | 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15 |
| Si las empresas no financieras emisoras de tarjetas deben cumplir con Protección al Usuario | cubierta | 1, 2, 4, 5, 7, 8, 9, 13, 14, 15 |
| Si las empresas no financieras emisoras de tarjetas deben clasificar a sus deudores | no_cubierta | 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15 |
| Bajo qué criterio clasifican sus deudores | cubierta | 3, 10, 11, 12 |

**Qué dice la respuesta por pata — descomposición del juez (verbatim, step1):**
- afirmación verificable (central): "Los proveedores no financieros de crédito deben cumplir con normas de protección de usuarios."
- afirmación verificable (central): "Los proveedores no financieros de crédito deben considerar y resolver fundadamente reclamos de usuarios."
- afirmación verificable (central): "Los proveedores no financieros de crédito deben clasificar deudores según mora en cartera de consumo/vivienda."
- afirmación verificable (central): "Las empresas no financieras emisoras de tarjetas de crédito deben cumplir con normas de protección de usuarios."
- afirmación verificable (central): "Las empresas no financieras emisoras de tarjetas de crédito deben resolver reclamos de usuarios."
- afirmación verificable (no central): "Las empresas no financieras emisoras de tarjetas de crédito deben entregar información sobre productos y servicios."
- afirmación verificable (no central): "Las empresas no financieras emisoras de tarjetas de crédito deben publicar contratos."
- afirmación verificable (central): "El criterio básico de clasificación de deudores es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía, medida a través del análisis de flujo de fondos."
- afirmación verificable (central): "Los criterios objetivos de clasificación de deudores incluyen el término de morosidad."
- afirmación verificable (central): "Los criterios objetivos de clasificación de deudores incluyen la situación jurídica del cliente o sus deudas."
- afirmación verificable (central): "Los criterios objetivos de clasificación de deudores incluyen el cumplimiento de refinanciaciones."
- reporte de alcance: "En la información disponible en el grafo no se encontró una obligación explícita de clasificación de deudores para las empresas no financieras emisoras de tarjetas de crédito."


---

# run_2/CQ-019 — [multi_norma] · sorteo

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** Al computar los activos para la exigencia de capital por riesgo de crédito, ¿qué previsión por incobrabilidad no se deduce, y cómo se vincula esa regla con la clasificación de deudores?

**ground_truth_secciones:** ["Capitales, Punto 2.3.1", "Clasificación, Puntos 6.5.1 y 7.2.1"]
**tos_fuente:** ["capitales", "clasificacion"]

**cita_textual del GT:** "[Capitales 2.3.1] [...] netos de las previsiones por riesgos de incobrabilidad [...] sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados 'en situación normal' –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A)."

## 2. Síntoma POST-HOC (verbatim, `posthoc_run/traces/off/run_2/CQ-019.json` → judge)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [],
 "reportes_de_alcance": [
  "No se encontró en el Knowledge Graph información específica sobre qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito.",
  "No se encontró en el Knowledge Graph información sobre cómo se vincula esa regla con la clasificación de deudores.",
  "El grafo contiene referencias a previsión contable, previsión regulatoria y previsión por riesgo de incobrabilidad, pero no especifica cuál se excluye del cálculo de activos ni su relación con la clasificación de deudores."
 ],
 "patas_de_la_pregunta": [
  "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito",
  "Cómo se vincula esa regla con la clasificación de deudores"
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
  "pata": "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito",
  "cobertura": "no_cubierta"
 },
 {
  "pata": "Cómo se vincula esa regla con la clasificación de deudores",
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

## 3. Trayectoria post-hoc

En la parte 2 del expediente (`expediente_validacion_2.md`, sección "run_2/CQ-019"): respuesta final íntegra, inventario con fidelidad 15/15 y apéndice de outputs completos.

## 4. Homólogos de etapas previas

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** — dev set (run_1) (verbatim, `referencias_dev_set.md`):

````markdown
## Caso on/run_1/CQ-019

**Pregunta:** Al computar los activos para la exigencia de capital por riesgo de crédito, ¿qué previsión por incobrabilidad no se deduce, y cómo se vincula esa regla con la clasificación de deudores?

Adjudicación de la autora, 2026-07-13, asistida por revisión:

- **Claim** "La previsión por riesgo de incobrabilidad sí se deduce para activos cubiertos con garantías preferidas A" [falso] — **`{noise_sensitivity, contenido_kg}` PRIMARIA.** Evidencia: soportado por `req_prevision_por_riesgo_de_incobrabilidad` ("Deducción por deterioro de activos... situación normal o cubiertos con garantías preferidas A"), cuyo contenido invierte el PDF (Capitales 2.3.1: "sin deducir el 100%... 'en situación normal'... y a las financiaciones que se encuentran cubiertas con garantías preferidas A" — ambas categorías son no-deducibles). Nota: ningún claim central falló; la primaria del caso descansa en la única secundaria [falso], decisión de la autora.
- **Claim** "La categoría 'situación normal' corresponde a clientes que demuestran capacidad de atender adecuadamente todos sus compromisos financieros" [no_soportado] — **FALSO POSITIVO DEL JUEZ, sin par** (re-adjudicado 2026-07-14). Evidencia: el resumen de `cla_situacion_normal_clasificacion_de_deudores`, con el contenido del claim ("Categoría de clasificación de deudores donde el cliente demuestra capacidad de atender adecuadamente todos sus compromisos financieros…"), apareció en el output COMPLETO del paso 2 del agente (auditoría 2026-07-14) — el claim estuvo soportado en runtime y es correcto contra Clasificación 6.5.1.
  - **Nota de re-adjudicación (autora, 2026-07-14):** fundada en la auditoría de truncamiento — la traza almacenada no es el contexto del agente (`harness.py` pasa outputs completos al agente y almacena truncados); verificación por re-ejecución determinística. Reemplaza la secundaria `{faithfulness, alucinacion_agente}` (modo a) del 2026-07-13.
- **Claim** "La provisión específica para cartera clasificada como situación normal debe absorberse antes de la deducción de otros conceptos deducibles del capital" [no_soportado] — **FALSO POSITIVO DEL JUEZ, sin par.** Evidencia: soportado casi verbatim por `req_prevision_por_riesgo_de_incobrabilidad_en_cartera_en_situacion_normal` (abierto por el agente en el paso 10) y correcto contra el PDF (Capitales, punto 8.4.1.1 —conceptos deducibles del COn1—: "Previo a su deducción deberá absorberse el importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera en 'situación normal' computado como patrimonio neto complementario (punto 8.2.3.3.).").

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion.md` (scratch, no versionado).
````

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** — dev set (run_5) (verbatim, `referencias_dev_set.md`):

````markdown
## Caso on/run_5/CQ-019 (expansión post-gate #1)

**Pregunta:** Al computar los activos para la exigencia de capital por riesgo de crédito, ¿qué previsión por incobrabilidad no se deduce, y cómo se vincula esa regla con la clasificación de deudores?

Adjudicación de la autora, 2026-07-15, asistida por revisión:

- **Claims centrales** «situación normal ≤31 días» y «se computa como patrimonio neto complementario» — **FALSOS POSITIVOS DEL JUEZ, sin par.** Evidencia: ambos EXPUESTOS en el paso 16 (resúmenes de `situacion_normal` y `prevision_por_cartera_en_situacion_normal`, re-ejecución determinística 2026-07-15) y correctos contra el PDF (Clasificación 7.2.1 verbatim; Capitales 8.2.3.3/8.4.1.1). Mecanismo del FP: el juez verifica contra `ground_truth_secciones` (2.3.1/6.5.1/7.2.1) y el PNc cae fuera de ese marco aunque sea corpus verdadero — mismo patrón que la fórmula 70100000 en run_3/CQ-020.
- **La racionalización** «responde a que esos deudores presentan menor riesgo de incumplimiento» — **`{faithfulness, alucinacion_agente}` (modo b) SECUNDARIA.** Evidencia: ni los nodos expuestos ni el PDF dan esa justificación (barrido 2026-07-15; el 2.3.1 establece la regla sin fundamentarla).
- **SIN PRIMARIA.** Nota: la hipótesis estructural del inventario (familia B) queda refutada para este caso — el dato-puente (la referencia cruzada a 6.5.1/7.2.1) existe como portador textual (`to_sobre_clasificacion_de_deudores`) y estuvo expuesto en la trayectoria; los extremos sin arista no impidieron el vínculo.
- **Patrón de calibración: "exoneración de centrales + secundaria lado agente"** — acierto = ninguna primaria emitida.

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion_v2.md` (scratch, no versionado).
````

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** — vara del piloto (run_3) (verbatim, `casos_piloto.md`):

````markdown
## CQ-019 — `multi_norma` · TOs: capitales, clasificacion

- **Pregunta:** Al computar los activos para la exigencia de capital por riesgo de crédito, ¿qué previsión por incobrabilidad no se deduce, y cómo se vincula esa regla con la clasificación de deudores?
- **Síntoma post-hoc (verbatim, 1 no_soportado — cero centrales reprobados):**
  - [no_soportado] "La clasificación 'en situación normal' comprende clientes que atienden puntualmente el pago de sus obligaciones o con atrasos que no superan los 31 días."
- **GT: SIN PRIMARIA** (cero centrales reprobados). **El único reprobado (secundario) es
  FALSO POSITIVO DEL JUEZ, sin par:** está SOPORTADO por
  `Restriccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones`,
  **expuesto en el output completo del paso 7**
  (`docs/evidencia_piloto/verificaciones_piloto.md` §2a-§2b, contenido íntegro pegado) —
  descripción verbatim de la 7.2.1, provenance "Punto 7.2" —, y es correcto contra el corpus:
  la **adjudicación firmada** de la misma oración la marcó **verdadera** con evidencia
  "Clasif 7.2.1 — Situación normal: puntual o ≤31 días"
  (`docs/evidencia_piloto/expediente_piloto_1.md`, caso CQ-018 §2, rotulada).
- **REGLA DE ACIERTO:** ídem CQ-018 — acierto = sin primarias; **CUALQUIER primaria = miss**.
- **Evidencia:** `docs/evidencia_piloto/expediente_piloto_1.md` (caso CQ-019) y
  `expediente_piloto_2.md`; `verificaciones_piloto.md` §2;
  `docs/evidencia_capa_d/verificacion_estructura_piloto.md` §2.
- **Nota (disclosure):** dos homólogos dev (`on/run_1/CQ-019`, `on/run_5/CQ-019`) — otros
  grafos, precedente taxonómico, no evidencia de este caso.
````

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES reprobados en juego (post-hoc):** ninguno.

**Patas (step1) × cobertura (step2) × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito | no_cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 |
| Cómo se vincula esa regla con la clasificación de deudores | no_cubierta | 2, 3, 5, 11 |

**Qué dice la respuesta por pata — descomposición del juez (verbatim, step1):**
- reporte de alcance: "No se encontró en el Knowledge Graph información específica sobre qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito."
- reporte de alcance: "No se encontró en el Knowledge Graph información sobre cómo se vincula esa regla con la clasificación de deudores."
- reporte de alcance: "El grafo contiene referencias a previsión contable, previsión regulatoria y previsión por riesgo de incobrabilidad, pero no especifica cuál se excluye del cálculo de activos ni su relación con la clasificación de deudores."


---

# run_2/CQ-025 — [factual_directa] · sorteo

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** En el Régimen Informativo de Capitales Mínimos, ¿con qué frecuencia se informa la exigencia por riesgo de mercado y la información sobre ratio de apalancamiento?

**ground_truth_secciones:** ["Régimen Informativo, Punto 1.1 (Instrucciones generales); Sección 4 puntos 4.3-4.5; Sección 10 (Ratio de apalancamiento)"]
**tos_fuente:** ["regimen"]

**cita_textual del GT:** "La información tendrá frecuencia mensual y se integrará con datos referidos al mes bajo análisis, excepto las siguientes informaciones que tendrán frecuencia trimestral [...] Con los datos correspondientes al último mes de cada trimestre (marzo, junio, septiembre y diciembre): - Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5. de la Sección 4.) [...] - La información sobre Ratio de apalancamiento (Sección 10.) en base individual [...]"

## 2. Síntoma POST-HOC (verbatim, `posthoc_run/traces/off/run_2/CQ-025.json` → judge)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "En el Régimen Informativo de Capitales Mínimos, la exigencia por riesgo de mercado se informa con frecuencia mensual.",
   "central": true
  },
  {
   "enunciado": "La exigencia por riesgo de mercado corresponde a las posiciones del último día del mes.",
   "central": false
  },
  {
   "enunciado": "En el Régimen Informativo de Capitales Mínimos, la información sobre el ratio de apalancamiento se informa con frecuencia trimestral.",
   "central": true
  },
  {
   "enunciado": "La información sobre el ratio de apalancamiento corresponde a datos del mes de cierre de trimestre.",
   "central": false
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "Frecuencia con que se informa la exigencia por riesgo de mercado en el Régimen Informativo de Capitales Mínimos",
  "Frecuencia con que se informa la información sobre ratio de apalancamiento en el Régimen Informativo de Capitales Mínimos"
 ]
}
```

`judge.step2.verificaciones` (por claim, con veredicto y centralidad):

```json
[
 {
  "enunciado": "En el Régimen Informativo de Capitales Mínimos, la exigencia por riesgo de mercado se informa con frecuencia mensual.",
  "central": true,
  "verdict": "falso"
 },
 {
  "enunciado": "La exigencia por riesgo de mercado corresponde a las posiciones del último día del mes.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "En el Régimen Informativo de Capitales Mínimos, la información sobre el ratio de apalancamiento se informa con frecuencia trimestral.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La información sobre el ratio de apalancamiento corresponde a datos del mes de cierre de trimestre.",
  "central": false,
  "verdict": "verdadero"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Frecuencia con que se informa la exigencia por riesgo de mercado en el Régimen Informativo de Capitales Mínimos",
  "cobertura": "cubierta"
 },
 {
  "pata": "Frecuencia con que se informa la información sobre ratio de apalancamiento en el Régimen Informativo de Capitales Mínimos",
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
   "La exigencia por riesgo de mercado corresponde a las posiciones del último día del mes."
  ],
  "n_centrales": 0,
  "n_secundarias": 1
 }
}
```

## 3. Trayectoria post-hoc

En la parte 2 del expediente (`expediente_validacion_2.md`, sección "run_2/CQ-025"): respuesta final íntegra, inventario con fidelidad 7/7 y apéndice de outputs completos.

## 4. Homólogos de etapas previas

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** — vara del gate (run_3) (verbatim, `casos_control.md`):

````markdown
### CQ-025 — `multi_norma` (frecuencia de reporte) · TO: regimen
- **Pregunta:** ¿Con qué frecuencia se informa la exigencia por riesgo de mercado y el ratio de apalancamiento?
- **Atribución humana (confirmada — verificada contra el PDF real — MIXTA: una pata de sistema PRIMARIA + una pata que es falso positivo del juez):** caso de [atribución múltiple](taxonomia.md), estructuralmente como CQ-017 (dos patas independientes), pero con causas de **distinto tipo**.
  - **Pata 1 (riesgo de mercado) — `{noise_sensitivity, contenido_kg}`, PRIMARIA (defecto de grafo):** el PDF (Punto 1.1 del TO de Régimen Informativo) ubica los datos de riesgo de mercado (puntos 4.3-4.5) en la lista de excepciones **trimestrales**. Pero el nodo `Operacion_calculo_de_riesgo_de_mercado` del grafo dice "mensual" — claim soportado por el nodo consultado pero incorrecto contra el PDF. El extractor confundió: en el pasaje, "mensual" califica al **código de consolidación** ("consolidado mensual"), no a la frecuencia de reporte, que es **trimestral** según el encabezado del bloque. El nodo afirma un contenido que contradice el PDF → `contenido_kg`.
  - **Exclusión de `aplicacion_erronea` (test v2.6):** la rama "nodo fiel" no se alcanza — el nodo contradice al PDF (afirma "mensual" donde el Punto 1.1 ubica los puntos 4.3 a 4.5 en las excepciones trimestrales), de modo que el defecto es de contenido, no de aplicación. El nodo, leído solo, no declara alcance ajeno: afirma una frecuencia errónea como propia.
  - **Pata 2 (ratio de apalancamiento) — falso positivo del juez (NO defecto de grafo ni de agente; sin par v2 — no es defecto del sistema):** el agente respondió correctamente que el apalancamiento es **trimestral** y citó bien el Punto 10.1 (verificado contra el PDF: el Punto 10.1.1 contiene "los datos se informarán con frecuencia trimestral"). El juez marcó esa afirmación como falsa, pero era correcta → ruido del juez, no un defecto del sistema.
- **Disclosure (relación caso↔taxonomía):** este caso expuso en el gate #1 el hueco "nodo fiel mal aplicado" y motivó la creación de `aplicacion_erronea` (v2.5); se consigna para que la relación caso↔taxonomía quede a la vista.
- **Calibración (regla específica):** como la pata 1 es la causa primaria de **sistema** (defecto de grafo), el verificador **acierta si detecta la pata 1 como `contenido_kg` (defecto de grafo)**. Reconocer la pata 2 como **falso positivo del juez** suma pero es **secundario**. Detectar la pata 1 como "navegación" (defecto de agente) **NO** es acierto: el dato correcto (trimestral) **no existe en el grafo**, así que no es que el agente no lo encontró — es que el grafo lo tiene mal.
- **Palanca/riesgo esperados (Paso 4):** pata 1 → grafo/esquema (corregir el contenido del nodo: mensual→trimestral, contra el pasaje del PDF); pata 2 → ninguna acción sobre el sistema (ruido del juez, se reporta como falso positivo).
````

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES reprobados en juego (post-hoc):**
- "En el Régimen Informativo de Capitales Mínimos, la exigencia por riesgo de mercado se informa con frecuencia mensual."

**Patas (step1) × cobertura (step2) × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Frecuencia con que se informa la exigencia por riesgo de mercado en el Régimen Informativo de Capitales Mínimos | cubierta | 1, 2, 3, 4, 5, 6, 7 |
| Frecuencia con que se informa la información sobre ratio de apalancamiento en el Régimen Informativo de Capitales Mínimos | cubierta | 1, 2, 3, 4, 5, 6, 7 |

**Qué dice la respuesta por pata — descomposición del juez (verbatim, step1):**
- afirmación verificable (central): "En el Régimen Informativo de Capitales Mínimos, la exigencia por riesgo de mercado se informa con frecuencia mensual."
- afirmación verificable (no central): "La exigencia por riesgo de mercado corresponde a las posiciones del último día del mes."
- afirmación verificable (central): "En el Régimen Informativo de Capitales Mínimos, la información sobre el ratio de apalancamiento se informa con frecuencia trimestral."
- afirmación verificable (no central): "La información sobre el ratio de apalancamiento corresponde a datos del mes de cierre de trimestre."


---

# run_4/CQ-014 — [factual_directa] · control negativo

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** ¿En qué plazo deben ingresarse y liquidarse en el mercado de cambios los cobros de exportaciones de servicios?

**ground_truth_secciones:** ["Punto 2.2.1 (Cobros de exportaciones de servicios)"]
**tos_fuente:** ["exterior"]

**cita_textual del GT:** "Los cobros por la prestación de servicios por parte de residentes a no residentes deberán ser ingresados y liquidados en el mercado de cambios en un plazo no mayor a los 20 (veinte) días hábiles a partir de la fecha de su percepción en el exterior o en el país o de su acreditación en cuentas del exterior."

## 2. Síntoma POST-HOC (verbatim, `posthoc_run/traces/off/run_4/CQ-014.json` → judge)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Los cobros de exportaciones de servicios deben ingresarse y liquidarse en el mercado de cambios en un plazo no mayor a 20 días hábiles.",
   "central": true
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "plazo para ingresar y liquidar en el mercado de cambios los cobros de exportaciones de servicios"
 ]
}
```

`judge.step2.verificaciones` (por claim, con veredicto y centralidad):

```json
[
 {
  "enunciado": "Los cobros de exportaciones de servicios deben ingresarse y liquidarse en el mercado de cambios en un plazo no mayor a 20 días hábiles.",
  "central": true,
  "verdict": "verdadero"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "plazo para ingresar y liquidar en el mercado de cambios los cobros de exportaciones de servicios",
  "cobertura": "cubierta"
 }
]
```

`judge.verdict` (correctitud/completitud/no-soportadas):

```json
{
 "correctitud": "correcta",
 "completitud": "completa",
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [],
  "n_centrales": 0,
  "n_secundarias": 0
 }
}
```

**SÍNTOMA VACÍO (explícito):** 0 claims reprobados · 0 patas no cubiertas — correctitud `correcta`, completitud `completa`.

**CONTEXTO FROZEN (rotulado: NO es el marco de adjudicación — es la falla que metió el caso al censo; `frozen_run/traces/run_4/CQ-014.json` + reporte ETAPA 2):**

- rep 1: correctitud `incorrecta` · completitud `parcial` · no_sop c/s = 2/0
    - no soportada (CENTRAL): "Para operaciones de contraparte vinculada previas al 14/04/25, el plazo para ingresar y liquidar cobros de exportaciones de servicios es de 180 días corridos desde la fecha de prestación o devengamiento del servicio."
    - no soportada (CENTRAL): "A partir del 14/04/25, el plazo para operaciones de contraparte vinculada se redujo a 90 días corridos."
- rep 2: correctitud `correcta` · completitud `completa` · no_sop c/s = 0/0
- rep 3: correctitud `correcta` · completitud `completa` · no_sop c/s = 0/0
- correctitud FINAL modal del frozen: **correcta (reporte ETAPA 2 §3: {'incorrecta': 1, 'correcta': 2}); entró al censo por centrales no soportadas (2 en rep 1)**

## 3. Trayectoria post-hoc

En la parte 3 del expediente (`expediente_validacion_3.md`, sección "run_4/CQ-014"): respuesta final íntegra, inventario con fidelidad 9/9 y apéndice de outputs completos.

## 4. Homólogos de etapas previas

**SIN HOMÓLOGO en ninguna etapa previa** (ni dev, ni gate, ni piloto).

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES reprobados en juego (post-hoc):** ninguno.

**Patas (step1) × cobertura (step2) × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| plazo para ingresar y liquidar en el mercado de cambios los cobros de exportaciones de servicios | cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9 |

**Qué dice la respuesta por pata — descomposición del juez (verbatim, step1):**
- afirmación verificable (central): "Los cobros de exportaciones de servicios deben ingresarse y liquidarse en el mercado de cambios en un plazo no mayor a 20 días hábiles."


---

# run_4/CQ-019 — [multi_norma] · deliberado (severidad)

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** Al computar los activos para la exigencia de capital por riesgo de crédito, ¿qué previsión por incobrabilidad no se deduce, y cómo se vincula esa regla con la clasificación de deudores?

**ground_truth_secciones:** ["Capitales, Punto 2.3.1", "Clasificación, Puntos 6.5.1 y 7.2.1"]
**tos_fuente:** ["capitales", "clasificacion"]

**cita_textual del GT:** "[Capitales 2.3.1] [...] netos de las previsiones por riesgos de incobrabilidad [...] sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados 'en situación normal' –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A)."

## 2. Síntoma POST-HOC (verbatim, `posthoc_run/traces/off/run_4/CQ-019.json` → judge)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "La previsión específica es la que no se deduce al computar los activos para la exigencia de capital por riesgo de crédito.",
   "central": true
  },
  {
   "enunciado": "El cálculo de la exigencia de capital por riesgo de crédito debe efectuarse sobre el monto bruto de la exposición.",
   "central": true
  },
  {
   "enunciado": "La clasificación de deudores debe efectuarse considerando la totalidad de las financiaciones comprendidas.",
   "central": false
  },
  {
   "enunciado": "La clasificación de deudores determina la categoría en que se incluye cada deudor, siendo cinco las categorías de riesgo.",
   "central": false
  },
  {
   "enunciado": "La categoría de clasificación es criterio objetivo para modificar aspectos como el término de morosidad, la situación jurídica del cliente y la refinanciación.",
   "central": false
  },
  {
   "enunciado": "Las previsiones mínimas por riesgo de incobrabilidad se determinan en función de la categoría de clasificación asignada a cada deudor.",
   "central": true
  },
  {
   "enunciado": "La previsión específica contable no se deduce del cálculo de capital (KSA).",
   "central": true
  }
 ],
 "reportes_de_alcance": [],
 "patas_de_la_pregunta": [
  "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito",
  "Cómo se vincula esa regla con la clasificación de deudores"
 ]
}
```

`judge.step2.verificaciones` (por claim, con veredicto y centralidad):

```json
[
 {
  "enunciado": "La previsión específica es la que no se deduce al computar los activos para la exigencia de capital por riesgo de crédito.",
  "central": true,
  "verdict": "falso"
 },
 {
  "enunciado": "El cálculo de la exigencia de capital por riesgo de crédito debe efectuarse sobre el monto bruto de la exposición.",
  "central": true,
  "verdict": "falso"
 },
 {
  "enunciado": "La clasificación de deudores debe efectuarse considerando la totalidad de las financiaciones comprendidas.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "La clasificación de deudores determina la categoría en que se incluye cada deudor, siendo cinco las categorías de riesgo.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "La categoría de clasificación es criterio objetivo para modificar aspectos como el término de morosidad, la situación jurídica del cliente y la refinanciación.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Las previsiones mínimas por riesgo de incobrabilidad se determinan en función de la categoría de clasificación asignada a cada deudor.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "La previsión específica contable no se deduce del cálculo de capital (KSA).",
  "central": true,
  "verdict": "falso"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito",
  "cobertura": "cubierta"
 },
 {
  "pata": "Cómo se vincula esa regla con la clasificación de deudores",
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
  "centrales": [
   "Las previsiones mínimas por riesgo de incobrabilidad se determinan en función de la categoría de clasificación asignada a cada deudor."
  ],
  "secundarias": [
   "La clasificación de deudores debe efectuarse considerando la totalidad de las financiaciones comprendidas.",
   "La clasificación de deudores determina la categoría en que se incluye cada deudor, siendo cinco las categorías de riesgo.",
   "La categoría de clasificación es criterio objetivo para modificar aspectos como el término de morosidad, la situación jurídica del cliente y la refinanciación."
  ],
  "n_centrales": 1,
  "n_secundarias": 3
 }
}
```

## 3. Trayectoria post-hoc

En la parte 3 del expediente (`expediente_validacion_3.md`, sección "run_4/CQ-019"): respuesta final íntegra, inventario con fidelidad 15/15 y apéndice de outputs completos.

## 4. Homólogos de etapas previas

Misma CQ que **run_2/CQ-019** (arriba en este expediente): homólogos idénticos — verbatim pegados en esa entrada; valen rotulados igual para este caso.

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES reprobados en juego (post-hoc):**
- "La previsión específica es la que no se deduce al computar los activos para la exigencia de capital por riesgo de crédito."
- "El cálculo de la exigencia de capital por riesgo de crédito debe efectuarse sobre el monto bruto de la exposición."
- "Las previsiones mínimas por riesgo de incobrabilidad se determinan en función de la categoría de clasificación asignada a cada deudor."
- "La previsión específica contable no se deduce del cálculo de capital (KSA)."

**Patas (step1) × cobertura (step2) × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito | cubierta | 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15 |
| Cómo se vincula esa regla con la clasificación de deudores | cubierta | 3, 6, 9, 12, 13, 14 |

**Qué dice la respuesta por pata — descomposición del juez (verbatim, step1):**
- afirmación verificable (central): "La previsión específica es la que no se deduce al computar los activos para la exigencia de capital por riesgo de crédito."
- afirmación verificable (central): "El cálculo de la exigencia de capital por riesgo de crédito debe efectuarse sobre el monto bruto de la exposición."
- afirmación verificable (no central): "La clasificación de deudores debe efectuarse considerando la totalidad de las financiaciones comprendidas."
- afirmación verificable (no central): "La clasificación de deudores determina la categoría en que se incluye cada deudor, siendo cinco las categorías de riesgo."
- afirmación verificable (no central): "La categoría de clasificación es criterio objetivo para modificar aspectos como el término de morosidad, la situación jurídica del cliente y la refinanciación."
- afirmación verificable (central): "Las previsiones mínimas por riesgo de incobrabilidad se determinan en función de la categoría de clasificación asignada a cada deudor."
- afirmación verificable (central): "La previsión específica contable no se deduce del cálculo de capital (KSA)."


---

# run_4/CQ-017 — [multi_norma] · sorteo

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** Un operador de cambio, ¿está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros y debe intervenir como entidad autorizada en el mercado de cambios?

**ground_truth_secciones:** ["Protección, Punto 1.1.2.2", "Exterior y Cambios, Punto 1.1"]
**tos_fuente:** ["proteccion", "exterior"]

**cita_textual del GT:** "[Protección 1.1.2.2] Operadores de cambio, por las operaciones comprendidas en las normas sobre 'Exterior y cambios'. | [Exterior 1.1] En todas las operaciones de cambio, canje y/o arbitraje que se cursen por el mercado libre de cambios [...] deberán intervenir entidades financieras o cambiarias autorizadas a operar en cambios por el Banco Central [...]"

## 2. Síntoma POST-HOC (verbatim, `posthoc_run/traces/off/run_4/CQ-017.json` → judge)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Un operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros.",
   "central": true
  },
  {
   "enunciado": "El operador de cambio es clasificado como un 'sujeto obligado' conforme a la normativa de protección de usuarios.",
   "central": true
  },
  {
   "enunciado": "El mercado libre de cambios está definido como aquel por el cual se cursan operaciones realizadas por entidades financieras y demás personas autorizadas por el BCRA para dedicarse al comercio de compra y venta de monedas extranjeras.",
   "central": false
  },
  {
   "enunciado": "Existe una categoría de 'personas jurídicas no autorizadas a operar en cambios' que requieren conformidad previa del BCRA para acceder al mercado de cambios.",
   "central": false
  }
 ],
 "reportes_de_alcance": [
  "La información disponible en el grafo no es concluyente respecto a si el operador de cambio debe intervenir como entidad autorizada en el mercado de cambios.",
  "No hay información explícita en el grafo que determine si los operadores de cambio deben o no intervenir como entidades autorizadas en el mercado de cambios."
 ],
 "patas_de_la_pregunta": [
  "¿Un operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros?",
  "¿Un operador de cambio debe intervenir como entidad autorizada en el mercado de cambios?"
 ]
}
```

`judge.step2.verificaciones` (por claim, con veredicto y centralidad):

```json
[
 {
  "enunciado": "Un operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "El operador de cambio es clasificado como un 'sujeto obligado' conforme a la normativa de protección de usuarios.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "El mercado libre de cambios está definido como aquel por el cual se cursan operaciones realizadas por entidades financieras y demás personas autorizadas por el BCRA para dedicarse al comercio de compra y venta de monedas extranjeras.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Existe una categoría de 'personas jurídicas no autorizadas a operar en cambios' que requieren conformidad previa del BCRA para acceder al mercado de cambios.",
  "central": false,
  "verdict": "no_soportado"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "¿Un operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros?",
  "cobertura": "cubierta"
 },
 {
  "pata": "¿Un operador de cambio debe intervenir como entidad autorizada en el mercado de cambios?",
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
   "El mercado libre de cambios está definido como aquel por el cual se cursan operaciones realizadas por entidades financieras y demás personas autorizadas por el BCRA para dedicarse al comercio de compra y venta de monedas extranjeras.",
   "Existe una categoría de 'personas jurídicas no autorizadas a operar en cambios' que requieren conformidad previa del BCRA para acceder al mercado de cambios."
  ],
  "n_centrales": 0,
  "n_secundarias": 2
 }
}
```

## 3. Trayectoria post-hoc

En la parte 3 del expediente (`expediente_validacion_3.md`, sección "run_4/CQ-017"): respuesta final íntegra, inventario con fidelidad 16/16 y apéndice de outputs completos.

## 4. Homólogos de etapas previas

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** — dev set (run_5) (verbatim, `referencias_dev_set.md`):

````markdown
## Caso off/run_5/CQ-017

**Pregunta:** Un operador de cambio, ¿está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros y debe intervenir como entidad autorizada en el mercado de cambios?

Adjudicación de la autora, 2026-07-13, asistida por revisión:

- **Pata 2** ("debe intervenir como entidad autorizada") — **DOS PRIMARIAS, SOBREDETERMINADA** (re-adjudicada por la autora, 2026-07-14, por los micro-hechos de la iteración 4):
  - **`{context_recall, alcanzabilidad_kg}` PRIMARIA (a):** los portadores de la regla de Exterior 1.1 existen (`intervencion_de_entidades_autorizadas_en_operaciones_de_camb`, `entidades_financieras_o_cambiarias_autorizadas__agencia_cambio`, `entidades_autorizadas_a_operar_en_cambios__otra`) pero ninguno apareció en las búsquedas del agente (pasos 3/12/15, re-ejecutados determinísticamente); por la regla de precedencia, el nodo entidad_operadora usado para rellenar no cuenta como contexto de la pata.
  - **`{noise_sensitivity, contenido_kg}` PRIMARIA (b) — reemplaza a la secundaria `{faithfulness, alucinacion_agente}` (modo b) del 2026-07-13:** el claim central es eco casi verbatim del `resumen_propiedades` de `operador_de_cambios__otra` ("Entidad financiera autorizada a operar en el mercado de cambios"), expuesto al agente en runtime en los pasos 1 (pos. 7) y 12 (pos. 8), ambos en tramo truncado (re-ejecución determinística 2026-07-14); la description contradice el PDF (Exterior 1.1: "financieras **o cambiarias**" — categorías distintas) y su provenance (Punto 4.8, disposiciones BOPREAL) no funda el contenido — **agravante `provenance_imprecisa` documentada**.
  - **Nota de sobredeterminación:** cada primaria alcanza SOLA para romper la pata (contrafácticos: portadores del 1.1 alcanzables → el agente encuentra la regla correcta; description del nodo corregida → el eco del agente sale correcto). Patrón nuevo, **consignado para la reunión de mentores**.
  - **Regla de acierto del caso:** patrón "varias primarias" de `casos_control.md` — el acierto exige detectar AMBAS.
- **Pata 2 — claim** "Existen entidades denominadas 'entidades operadoras en mercado de cambios' que son entidades financieras autorizadas..." — **`{noise_sensitivity, contenido_kg}` SECUNDARIA.** Evidencia: soportado por `entidad_operadora_en_mercado_de_cambios__otra`, cuyo contenido omite "o cambiarias" (contra Exterior 1.1) y cuya provenance (Punto 3.16) no funda el contenido (verificado: el 3.16 es requisitos de egresos/ARCA).
- **Pata 1 — claim de la enumeración de sujetos obligados** — **`{noise_sensitivity, contenido_kg}` SECUNDARIA** (re-adjudicado 2026-07-14). Evidencia: soportado por el nodo `sujeto_obligado` (abierto en el paso 13), que enumera 5 categorías; el PDF Punto 1.1.2 enumera 7 (agrega 1.1.2.6 PSPCP y 1.1.2.7 PSI/billetera digital, verificado 2026-07-14) — claim soportado por nodo consultado e **incompleto contra el PDF**.
  - **Nota de re-adjudicación (autora, 2026-07-14):** reemplaza el FALSO POSITIVO DEL JUEZ del 2026-07-13, cuya verificación chequeó **presencia** de la enumeración pero no su **exhaustividad** contra el PDF.
- **Pata 1 — las 4 glosas de obligaciones** (información clara, trato equitativo, acceso igualitario, resolución de reclamos) — **FALSOS POSITIVOS DEL JUEZ, sin par** (re-adjudicado 2026-07-14). Evidencia: los 4 edges (`debe_garantizar → trato_equitativo_y_digno` y `→ derecho_a_informacion_clara_y_suficiente`; `debe_adoptar → acceso_igualitario_a_servicios_financieros`; `recae_sobre → consideracion_y_resolucion_fundada_de_reclamos`) existen en el output COMPLETO del paso 10 del agente (re-ejecución determinística, auditoría 2026-07-14); el agente los tuvo en runtime (el harness pasa outputs completos y almacena truncados) y son fieles al PDF (1.1.2, 1.2, 2.x).
  - **Nota de re-adjudicación (autora, 2026-07-14):** fundada en la auditoría de truncamiento — la traza almacenada no es el contexto del agente (`harness.py` pasa outputs completos al agente y almacena truncados); verificación por re-ejecución determinística.

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion.md` (scratch, no versionado).
````

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** — vara del gate (run_3) (verbatim, `casos_control.md`):

````markdown
### CQ-017 — `multi_norma` · TOs: proteccion, exterior
- **Pregunta:** Un operador de cambio, ¿está alcanzado por las normas de Protección de Usuarios y debe intervenir como entidad autorizada en el mercado de cambios?
- **Ground-truth secciones:** Protección, Punto 1.1.2.2 · Exterior y Cambios, Punto 1.1.
- **Atribución humana (confirmada — MIXTA con DOS causas, ambas PRIMARIAS; evidencia re-fundada 2026-07-15, vara v3):** es un caso de [atribución múltiple](taxonomia.md) con **dos defectos de grafo**, cada uno rompiendo una pata distinta de la pregunta. Como cada defecto mueve el veredicto de su pata, **ninguna es secundaria**.
  - **Causa primaria — `{context_recall, estructural_kg}` (pata 2):** falta la arista cross-documento que une Protección (Punto **1.1.2.2**, operador de cambio alcanzado) con Exterior y Cambios (Punto **1.1**, entidad autorizada en el mercado de cambios). Ausencia demostrada contra outputs COMPLETOS: "1.1.2.2", los portadores de la regla de Exterior 1.1 y el texto "entidad autorizada" están ausentes en los 15 pasos re-ejecutados (`docs/evidencia_vara_v3/auditoria_truncamiento_run3.md` §3). Y contra el grafo entero: el nodo `EntidadFinanciera_operador_de_cambio` tiene exactamente **2 edges, ambos internos a Protección**; los 3 nodos del grafo que mencionan "entidad autorizada"/"autorizadas a operar" no tienen ningún edge con él; **0 aristas** sobre los 6.634 edges conectan un nodo del operador con uno de entidad-autorizada/mercado-de-cambios (`verificaciones_vara_v3.md` §1). **Refuerzo:** el grafo SÍ expone 13 edges cross-documento desde `sujeto_obligado` hacia operaciones de Exterior (paso 10, output completo) y ninguno porta la regla del 1.1 — **la conexión específica es lo que falta**.
  - **Causa primaria — `{noise_sensitivity, provenance_imprecisa}` (pata 1):** el nodo del operador de cambio tiene provenance a nivel grueso — verbatim **"Punto 1.1. Partes."** (`verificaciones_vara_v3.md` §1a) — en vez del específico (**"1.1.2.2"**). El agente reportó fielmente lo que el nodo decía (citó 1.1) — claim soportado por el nodo pero incorrecto contra el GT —, y por eso el juez marcó la **pata 1** como incorrecta pese a que el contenido era correcto.
  - **Exclusión de `aplicacion_erronea` en la pata 1 (test v2.6):** el nodo es fiel y pertinente; su defecto es **la cita, no el alcance** — no hay contenido de otro alcance aplicado a esta pata.
  - Cada causa va con sus tres piezas de evidencia (afirmación / nodo / fuente).
- **Calibración:** como las dos causas son primarias, el verificador **acierta solo si detecta ambas** (`estructural_kg` Y `provenance_imprecisa`). Detectar una sola **no** es acierto — se perdió la mitad de la falla.
- **Palanca/riesgo esperados (Paso 4):** ambas → grafo/esquema · ambas **alto riesgo** — crear la arista cross-documento es estructura nueva, y corregir la provenance a nivel fino es decisión de modelado; las dos → revisión humana.
````

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES reprobados en juego (post-hoc):** ninguno.

**Patas (step1) × cobertura (step2) × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| ¿Un operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros? | cubierta | 1, 2, 4, 5, 6, 7, 8, 9, 14 |
| ¿Un operador de cambio debe intervenir como entidad autorizada en el mercado de cambios? | no_cubierta | 1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15 |

**Qué dice la respuesta por pata — descomposición del juez (verbatim, step1):**
- afirmación verificable (central): "Un operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros."
- afirmación verificable (central): "El operador de cambio es clasificado como un 'sujeto obligado' conforme a la normativa de protección de usuarios."
- afirmación verificable (no central): "El mercado libre de cambios está definido como aquel por el cual se cursan operaciones realizadas por entidades financieras y demás personas autorizadas por el BCRA para dedicarse al comercio de compra y venta de monedas extranjeras."
- afirmación verificable (no central): "Existe una categoría de 'personas jurídicas no autorizadas a operar en cambios' que requieren conformidad previa del BCRA para acceder al mercado de cambios."
- reporte de alcance: "La información disponible en el grafo no es concluyente respecto a si el operador de cambio debe intervenir como entidad autorizada en el mercado de cambios."
- reporte de alcance: "No hay información explícita en el grafo que determine si los operadores de cambio deben o no intervenir como entidades autorizadas en el mercado de cambios."


---

# run_4/CQ-020 — [multi_norma] · sorteo

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** ¿Cómo se calcula la exigencia de capital por riesgo de crédito (CRC) y con qué frecuencia se reporta al BCRA?

**ground_truth_secciones:** ["Capitales, Punto 2.1", "Régimen Informativo, Punto 3.1.2", "Régimen Informativo, Punto 1.1 (frecuencia)"]
**tos_fuente:** ["capitales", "regimen"]

**cita_textual del GT:** "[Capitales 2.1] Se determinará aplicando la siguiente expresión: CRC = (k x 0,08 x APRC) + INC | [Régimen 3.1.2] Se determinará de acuerdo con la siguiente expresión: CRC = (k x 0,08 x APRc) + INC | [Régimen 1.1] La información tendrá frecuencia mensual y se integrará con datos referidos al mes bajo análisis [...]"

## 2. Síntoma POST-HOC (verbatim, `posthoc_run/traces/off/run_4/CQ-020.json` → judge)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "La fórmula para calcular la CRC es: CRC = (k × 0,08 × APRC) + INC",
   "central": true
  },
  {
   "enunciado": "k es el factor de calificación de entidad",
   "central": true
  },
  {
   "enunciado": "k está vinculado a la calificación asignada por la SEFYC",
   "central": true
  },
  {
   "enunciado": "k toma valores entre 1 y 1,19",
   "central": true
  },
  {
   "enunciado": "0,08 es el factor de exigencia de capital en la fórmula de CRC",
   "central": true
  },
  {
   "enunciado": "APRC son los activos ponderados por riesgo de crédito",
   "central": true
  },
  {
   "enunciado": "Los APRC se determinan mediante la suma de valores obtenidos aplicando ponderadores de riesgo a activos computables",
   "central": true
  },
  {
   "enunciado": "INC representa los incrementos normativos en la fórmula de CRC",
   "central": true
  },
  {
   "enunciado": "Las entidades deben reportar información de capital en el régimen informativo contable mensual del BCRA",
   "central": false
  }
 ],
 "reportes_de_alcance": [
  "La información disponible en el grafo no especifica explícitamente si el reporte de la exigencia de CRC es mensual, trimestral u otra periodicidad.",
  "La respuesta fue marcada como no respondible (respondible: false) respecto a la frecuencia de reporte."
 ],
 "patas_de_la_pregunta": [
  "Cómo se calcula la exigencia de capital por riesgo de crédito (CRC)",
  "Con qué frecuencia se reporta la CRC al BCRA"
 ]
}
```

`judge.step2.verificaciones` (por claim, con veredicto y centralidad):

```json
[
 {
  "enunciado": "La fórmula para calcular la CRC es: CRC = (k × 0,08 × APRC) + INC",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "k es el factor de calificación de entidad",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "k está vinculado a la calificación asignada por la SEFYC",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "k toma valores entre 1 y 1,19",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "0,08 es el factor de exigencia de capital en la fórmula de CRC",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "APRC son los activos ponderados por riesgo de crédito",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Los APRC se determinan mediante la suma de valores obtenidos aplicando ponderadores de riesgo a activos computables",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "INC representa los incrementos normativos en la fórmula de CRC",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Las entidades deben reportar información de capital en el régimen informativo contable mensual del BCRA",
  "central": false,
  "verdict": "no_soportado"
 }
]
```

`judge.step2.cobertura_patas`:

```json
[
 {
  "pata": "Cómo se calcula la exigencia de capital por riesgo de crédito (CRC)",
  "cobertura": "cubierta"
 },
 {
  "pata": "Con qué frecuencia se reporta la CRC al BCRA",
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
  "centrales": [
   "k está vinculado a la calificación asignada por la SEFYC",
   "k toma valores entre 1 y 1,19",
   "Los APRC se determinan mediante la suma de valores obtenidos aplicando ponderadores de riesgo a activos computables"
  ],
  "secundarias": [
   "Las entidades deben reportar información de capital en el régimen informativo contable mensual del BCRA"
  ],
  "n_centrales": 3,
  "n_secundarias": 1
 }
}
```

## 3. Trayectoria post-hoc

En la parte 3 del expediente (`expediente_validacion_3.md`, sección "run_4/CQ-020"): respuesta final íntegra, inventario con fidelidad 15/15 y apéndice de outputs completos.

## 4. Homólogos de etapas previas

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** — dev set (run_1) (verbatim, `referencias_dev_set.md`):

````markdown
## Caso off/run_1/CQ-020

**Pregunta:** ¿Cómo se calcula la exigencia de capital por riesgo de crédito (CRC) y con qué frecuencia se reporta al BCRA?

Adjudicación de la autora, 2026-07-13, asistida por revisión:

- **Pata 1 (cálculo) — claim central** "INC es el Incremento de exigencia por riesgo de crédito por excesos en participaciones en capital de empresas" — **`{noise_sensitivity, contenido_kg}` PRIMARIA.** Evidencia (precisada 2026-07-14, sin cambio de par ni jerarquía): el claim reproduce casi verbatim el label del nodo `req_incremento_de_exigencia_por_riesgo_de_credito_por_excesos_en_participaciones_en_capital_de_empresas_inc`, que estaba en el **TRAMO TRUNCADO** del output del paso 1 (5º resultado — visible en runtime, no en la traza almacenada), junto con su resumen ("Exigencia de capital adicional por inversiones significativas en empresas que exceden límites regulados"); ese label conflata INC(inversiones significativas, límites 15%/60% dentro de APRC) con el INC de la fórmula CRC (excesos en activos inmovilizados etc., Capitales 2.1) — soporte infiel al PDF.
  - **Nota de re-adjudicación (autora, 2026-07-14):** precisión de evidencia fundada en la auditoría de truncamiento — la traza almacenada no es el contexto del agente (`harness.py` pasa outputs completos al agente y almacena truncados); verificación por re-ejecución determinística.
- **Los otros 7 claims negativos** (k escala 1-1,19; k asignado por SEFyC; APRC suma con ponderadores; reporte vía R.I.-C.M.; y las 3 secundarias del R.I.-C.M.) — **FALSOS POSITIVOS DEL JUEZ, sin par.** Evidencia: soportados por los nodos abiertos (`req_factor_k`, `con_activos_ponderados_por_riesgo_de_credito_aprc`, `ins_regimen_informativo_contable_mensual`, `rep_regimen_informativo_contable_mensual_sobre_capitales_minimos`) y correctos contra el PDF (Capitales 2.1: escala k 1/1,03/1,08/1,13/1,19, calificación SEFYC, expresión de APRC; Régimen 1.1: frecuencia mensual por defecto).
- **Pata 2 (frecuencia)** — "mensual vía R.I.-C.M." — **sin defecto.** Evidencia: soportado por `ins_regimen_informativo_contable_mensual` (abierto en el paso 9) y correcto contra Régimen 1.1 (la exigencia por riesgo de crédito no está en las excepciones trimestrales).

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion.md` (scratch, no versionado).
````

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** — vara del gate (run_3) (verbatim, `casos_control.md`):

````markdown
### CQ-020 — `multi_norma` · TOs: capitales, regimen
- **Pregunta:** ¿Cómo se calcula la exigencia de capital por riesgo de crédito (CRC) y con qué frecuencia se reporta al BCRA?
- **Ground-truth secciones:** Capitales, Punto 2.1 · Régimen Informativo, Punto 3.1.2 · Régimen Informativo, Punto 1.1 (frecuencia).
- **Atribución humana (primaria confirmada y re-fundada; secundaria disuelta 2026-07-15, vara v3):**
  - **Causa primaria — `{context_recall, completitud_kg}` (defecto del grafo):** falta el nodo de **frecuencia de reporte para riesgo de crédito**; por su ausencia el agente **mis-aplica el nodo de frecuencia de riesgo de mercado** (expuesto con label genérico en el paso 8, abierto en el paso 9 — `docs/evidencia_vara_v3/auditoria_truncamiento_run3.md` §4c). Por la [regla de precedencia](taxonomia.md) el síntoma es `context_recall`: el nodo de riesgo de mercado NO cuenta como contexto de la pata de crédito, así que el dato pertinente nunca apareció en la trayectoria. Evidencia re-fundada: **ningún output de los 11 pasos asocia frecuencia de reporte a riesgo de crédito** (los matches de frecuencia son riesgo operacional, riesgo de mercado, o el nombre del PDF en las provenances — `auditoria_truncamiento_run3.md` §4a); la frecuencia general del R.I.-C.M. ("la información tendrá frecuencia mensual", Punto 1.1) existe en el grafo **solo como location de provenance** del nodo TextoOrdenado, no en las properties de ningún nodo (`verificaciones_vara_v3.md` §3a). **Exclusión por test v2.2 de los 2 nodos marginales del barrido** — los únicos que combinan frecuencia con riesgo de crédito comparten tema pero no portan LA RESPUESTA (la frecuencia de reporte de la exigencia CRC): `Obligacion_se_informaran_los_incrementos_a_la_exigencia_segun_riesgo_de_credito_...` ("Se informarán los incrementos a la exigencia según riesgo de crédito generados por excesos verificados...", `plazo: mensual`) y `Obligacion_informacion_de_incumplimientos_de_grandes_exposiciones_...` ("Información de incumplimientos de Grandes Exposiciones al Riesgo de Crédito del mes bajo informe", `frecuencia: mensual`); además, **ninguno fue expuesto en la trayectoria** (`auditoria_truncamiento_run3.md` §4b). Es lo que mueve el veredicto, y lo que un refinamiento del grafo podría arreglar.
  - **La ex-secundaria `{faithfulness, alucinacion_agente}` SE DISUELVE → falso positivo del juez (sin par):** el claim **"0,08 es el coeficiente de capital mínimo"** está soportado por contenido EXPUESTO — los nodos abiertos con `ver_nodo` en los pasos 4 y 6 exponen el coeficiente 0,08 en las fórmulas de la exigencia por riesgo de crédito (paso 4, `Operacion_calculo_de_capital_minimo`: "C_RC = (k x 0,08 x APR_c) + INC"; paso 6, `Operacion_calculo_de_exigencia_por_riesgo`: "Código 70100000 (n) = k x 0,08 [ … ]") — y la fórmula es fiel al PDF (verificación contra el 8.1.1 registrada en la adjudicación anterior). Caminando el árbol: con soporte → `noise_sensitivity` → nodo fiel → pertinente → `sin_defecto`. **Corrección documentada:** el GT anterior nació de un barrido con variantes léxicas equivocadas — "APRc" sin guion bajo y "0.08" con punto dan ausente; "0,08" y "APR_c" dan presente (4 y 3 nodos) — `auditoria_truncamiento_run3.md` §4 + `verificaciones_vara_v3.md` §3b.
  - **El otro claim `no_soportado` del juez** —la fórmula alternativa "Código 70100000 (n) = …"— **se mantiene tal cual: falso positivo del juez** (sin par — no es defecto del sistema): está soportado por un nodo que el agente SÍ consultó (`Operacion_calculo_de_exigencia_por_riesgo`, `ver_nodo` en el paso 6 de su trayectoria) y es correcto contra el PDF (8.1.1); el juez es ciego al grafo y no podía verlo.
- **Calibración:** acierto = detectar la **causa primaria** (sin cambio: la ex-secundaria nunca fue exigida; hoy no hay secundaria — los claims del juez son falsos positivos, reconocerlos suma pero no es obligatorio).
- **Palanca/riesgo esperados (Paso 4):** la primaria → grafo/esquema (crear el nodo de frecuencia faltante) · **ALTO riesgo** → revisión humana.
- **Por qué la primaria es ALTO riesgo (confirmado):** el nodo de frecuencia para riesgo de crédito **no existe — hay que crearlo de cero**, y crear estructura nueva es decisión de modelado, no transcripción de un dato literal único. Por eso difiere de CQ-034, que es bajo riesgo (ahí el dato se transcribe sobre un patrón que el grafo ya tiene).
````

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES reprobados en juego (post-hoc):**
- "k está vinculado a la calificación asignada por la SEFYC"
- "k toma valores entre 1 y 1,19"
- "Los APRC se determinan mediante la suma de valores obtenidos aplicando ponderadores de riesgo a activos computables"

**Patas (step1) × cobertura (step2) × pasos que tocaron el tema** (método mecánico: pasos cuya consulta u output completo contiene ≥2 tokens no-stopword de la pata; no es lectura semántica):

| Pata (verbatim del juez) | Cobertura | Pasos |
|---|---|---|
| Cómo se calcula la exigencia de capital por riesgo de crédito (CRC) | cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14 |
| Con qué frecuencia se reporta la CRC al BCRA | no_cubierta | 1, 2, 3, 10, 13, 14 |

**Qué dice la respuesta por pata — descomposición del juez (verbatim, step1):**
- afirmación verificable (central): "La fórmula para calcular la CRC es: CRC = (k × 0,08 × APRC) + INC"
- afirmación verificable (central): "k es el factor de calificación de entidad"
- afirmación verificable (central): "k está vinculado a la calificación asignada por la SEFYC"
- afirmación verificable (central): "k toma valores entre 1 y 1,19"
- afirmación verificable (central): "0,08 es el factor de exigencia de capital en la fórmula de CRC"
- afirmación verificable (central): "APRC son los activos ponderados por riesgo de crédito"
- afirmación verificable (central): "Los APRC se determinan mediante la suma de valores obtenidos aplicando ponderadores de riesgo a activos computables"
- afirmación verificable (central): "INC representa los incrementos normativos en la fórmula de CRC"
- afirmación verificable (no central): "Las entidades deben reportar información de capital en el régimen informativo contable mensual del BCRA"
- reporte de alcance: "La información disponible en el grafo no especifica explícitamente si el reporte de la exigencia de CRC es mensual, trimestral u otra periodicidad."
- reporte de alcance: "La respuesta fue marcada como no respondible (respondible: false) respecto a la frecuencia de reporte."

