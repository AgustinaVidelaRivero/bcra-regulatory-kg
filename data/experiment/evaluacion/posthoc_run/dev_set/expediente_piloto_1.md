# Expediente de adjudicación del piloto — 5 casos (run_3)

Fecha: 2026-07-16. SOLO LECTURA; escrituras: este archivo y su parte 2 (apéndices).
Ni el verificador ni la capa corrieron sobre ningún caso (protocolo §5). **Cero
adjudicación**: hechos verbatim con ruta de origen. Partido en dos por tamaño:
`expediente_piloto_1.md` (casos y tablas) + `expediente_piloto_2.md` (apéndices).

Fuentes: `queries/eval_set_v1.json` (pregunta/GT), `frozen_run/traces/run_3/` (falla
según el frozen), `adjudicacion_FIRMADO.json` (veredictos firmados, rotulados),
`posthoc_run/traces/off/run_3/` (trayectorias), `referencias_dev_set.md` (homólogos).


---

# CQ-016 — [factual_directa]

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** ¿En qué unidad y con qué nivel de decimales deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos?

**ground_truth_secciones:** ["Punto 1.2 (Sección 1, Instrucciones generales)"]
**tos_fuente:** ["regimen"]

**cita_textual del GT:** "Los importes se registrarán en miles de pesos, sin decimales. A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad cuando el primer dígito de las fracciones sea igual o mayor que 5, desechando estas últimas si resultan inferiores."

## 2. La falla según el frozen (verbatim por rep, `frozen_run/traces/run_3/CQ-016.json`)

### Rep 1 — correctitud: `correcta` · completitud: `parcial`

- **Patas no cubiertas según el juez (justificacion.completitud, verbatim):** "Patas no cubiertas: Unidad en que deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos; Nivel de decimales con que deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos"
- **Afirmación no soportada (secundaria):** "En el Régimen Informativo Contable Mensual, los importes se registran en miles de pesos"
  - (no figura como entrada propia en la adjudicación firmada)
- **Afirmación no soportada (secundaria):** "En el Régimen Informativo Contable Mensual, los importes se registran sin decimales"
  - (no figura como entrada propia en la adjudicación firmada)

### Rep 2 — correctitud: `correcta` · completitud: `parcial`

- **Patas no cubiertas según el juez (justificacion.completitud, verbatim):** "Patas no cubiertas: Unidad en que deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos; Nivel de decimales con que deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos"
- (sin afirmaciones no soportadas en esta rep)

### Rep 3 — correctitud: `correcta` · completitud: `parcial`

- **Patas no cubiertas según el juez (justificacion.completitud, verbatim):** "Patas no cubiertas: Unidad en que deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos; Nivel de decimales con que deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos"
- **Afirmación no soportada (secundaria):** "En el Régimen Informativo Contable Mensual los importes se registran en miles de pesos sin decimales."
  - (no figura como entrada propia en la adjudicación firmada)

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_3/CQ-016.json`)

`trace.final_json`:

```json
{
 "respuesta": "Según la información disponible en el Knowledge Graph, los importes en el régimen informativo se registran en miles de pesos, sin decimales. Sin embargo, no se encontró en el grafo una especificación explícita y separada para un 'Régimen Informativo de Exigencia e Integración de Capitales Mínimos' como entidad diferenciada. La norma sobre registro en miles de pesos sin decimales está documentada en el Régimen Informativo Contable Mensual (Punto 1.2).",
 "citas": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 1.2. Los importes se registrarán en miles de pesos, sin decimales."
  }
 ],
 "respondible": false
}
```

`trace.final_raw` (turno final íntegro):

```
Basándome en mi búsqueda exhaustiva del Knowledge Graph, he encontrado que la información sobre el formato de registro de importes (en miles de pesos sin decimales) está documentada en el Régimen Informativo Contable Mensual. Sin embargo, no he encontrado una especificación diferente o específica para el "Régimen Informativo de Exigencia e Integración de Capitales Mínimos" como una entidad separada en el grafo. 

La información disponible en el grafo indica que:

1. Los importes se registran en **miles de pesos, sin decimales** (según el Régimen Informativo Contable Mensual)
2. El documento de Capitales Mínimos existe y contiene regulaciones sobre capitales mínimos
3. Hay obligaciones de informar sobre exigencia de capitales por riesgo de mercado

Sin embargo, no puedo confirmar con certeza si esta regla de "miles de pesos sin decimales" aplica específicamente al "Régimen Informativo de Exigencia e Integración de Capitales Mínimos" como un régimen separado, ya que el grafo no contiene una entidad específica con ese nombre exacto.

```json
{
  "respuesta": "Según la información disponible en el Knowledge Graph, los importes en el régimen informativo se registran en miles de pesos, sin decimales. Sin embargo, no se encontró en el grafo una especificación explícita y separada para un 'Régimen Informativo de Exigencia e Integración de Capitales Mínimos' como entidad diferenciada. La norma sobre registro en miles de pesos sin decimales está documentada en el Régimen Informativo Contable Mensual (Punto 1.2).",
  "citas": [
    {
      "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
      "location": "Punto 1.2. Los importes se registrarán en miles de pesos, sin decimales."
    }
  ],
  "respondible": false
}
```
```

## 3b. Inventario de pasos (almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados (traza) | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "Régimen Informativo Exigencia Integración Capitales Mínimos", "limite": 10}` | 3337 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "importes unidad decimales registro", "limite": 10}` | 2967 | 1215 | = runtime ✓ |
| 3 | ver_nodo | `{"id": "Restriccion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales"}` | 527 | 527 | = runtime ✓ |
| 4 | ver_nodo | `{"id": "TextoOrdenado_to_capitales_minimos_actual_pdf"}` | 361 | 361 | = runtime ✓ |
| 5 | ver_vecinos | `{"id": "TextoOrdenado_to_capitales_minimos_actual_pdf", "direccion": "salientes"}` | 9323 | 1215 | = runtime ✓ |
| 6 | buscar_nodos | `{"consulta": "capitales mínimos importes miles decimales", "limite": 10}` | 3123 | 1215 | = runtime ✓ |
| 7 | buscar_nodos | `{"consulta": "régimen informativo capitales mínimos exigencia integración", "limite": 10}` | 3337 | 1215 | = runtime ✓ |
| 8 | ver_nodo | `{"id": "Obligacion_informar_exigencia_de_capitales_por_riesgo"}` | 521 | 521 | = runtime ✓ |
| 9 | ver_vecinos | `{"id": "Restriccion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales", "direccion": "entrantes"}` | 219 | 219 | = runtime ✓ |
| 10 | buscar_nodos | `{"consulta": "punto 1.2 importes miles pesos decimales", "limite": 5}` | 1574 | 1214 | = runtime ✓ |
| 11 | buscar_nodos | `{"consulta": "TO_capitales_minimos formato unidad registro", "limite": 10}` | 3164 | 1215 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 11/11 pasos con largo idéntico.** Outputs completos: apéndice del caso en `expediente_piloto_2.md`.

## 4. Homólogos del dev set

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** (verbatim, `referencias_dev_set.md`):

````markdown
## Caso off/run_1/CQ-016 (expansión post-gate #1)

**Pregunta:** ¿En qué unidad y con qué nivel de decimales deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos?

Adjudicación de la autora, 2026-07-15, asistida por revisión:

**CASO SIN DEFECTO DEL SISTEMA (exoneración integral).**

- **Claim secundario** «Esta disposición proviene del Régimen Informativo Contable Mensual» (único claim negativo del caso) — **FALSO POSITIVO DEL JUEZ, sin par.** Evidencia: soportado (resumen de `req_exigencia_de_integracion_de_capitales_minimos` expuesto en paso 1: "Sección 4 del Régimen Informativo Contable Mensual") y correcto contra el PDF (el R.I. de Exigencia e Integración es el apartado 4 del RICM — encabezado verbatim del propio pasaje GT). La dimensión `cita_documento_correcto=false` es artefacto de metadatos (el `ground_truth_secciones` no nombra documento; el juez defaulteó a false sobre una cita al documento correcto) y NO participa del criterio de falla (`verifier_pilot.scale_specs`: solo claims falso/no_soportado).
- **Cita del agente** (granularidad de página, `cita_precision="pagina"`) — **`{noise_sensitivity, provenance_imprecisa}` SECUNDARIA — lado grafo, no decisiva.** Evidencia: la provenance de `req_miles_de_pesos` es "pp. 2-3" (página sin punto; el contenido vive en el Punto 1.2, pág. 3), lo que limita la cita del agente a granularidad de página. Real, documentada, sin efecto en el veredicto.
- **Patrón de calibración: "exoneración integral + secundaria"** — acierto = declarar el caso sin defecto del sistema (ninguna primaria).

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion_v2.md` (scratch, no versionado).
````

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES en juego (unión de las 3 reps del frozen):** ninguno (la falla es de completitud).

**Patas de la pregunta (descomposición del juez post-hoc, `judge.step1`) × cobertura (`judge.step2.cobertura_patas`) × pasos que tocaron el tema:**
("pasos que tocaron el tema" = método mecánico: pasos cuya consulta o cuyo output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica)

| Pata (verbatim del juez) | Cobertura | Pasos que tocaron el tema |
|---|---|---|
| Unidad en que deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos | cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 11 |
| Nivel de decimales con que deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos | cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 |

**Qué dice la respuesta final sobre las patas — descomposición del juez post-hoc (verbatim, `judge.step1`):**
- afirmación verificable (central): "Los importes en el régimen informativo se registran en miles de pesos"
- afirmación verificable (central): "Los importes en el régimen informativo se registran sin decimales"
- afirmación verificable (no central): "La norma sobre registro en miles de pesos sin decimales está documentada en el Régimen Informativo Contable Mensual (Punto 1.2)"
- reporte de alcance: "No se encontró en el grafo una especificación explícita y separada para un 'Régimen Informativo de Exigencia e Integración de Capitales Mínimos' como entidad diferenciada"


---

# CQ-018 — [multi_norma]

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** Los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas, ¿deben cumplir con Protección al Usuario y, además, clasificar a sus deudores? ¿Bajo qué criterio clasifican?

**ground_truth_secciones:** ["Protección, Puntos 1.1.2.4 y 1.1.2.5", "Clasificación, Punto 10.1"]
**tos_fuente:** ["proteccion", "clasificacion"]

**cita_textual del GT:** "[Protección 1.1.2.4/1.1.2.5] Empresas no financieras emisoras de tarjetas de crédito y/o compra [...] Otros proveedores no financieros de crédito [...] | [Clasificación 10.1] Las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito [...] deberán clasificar a los respectivos deudores en función de su mora, según los criterios aplicables para la cartera de 'consumo o vivienda' y por aplicación de las disposiciones previstas en el punto 7.3."

## 2. La falla según el frozen (verbatim por rep, `frozen_run/traces/run_3/CQ-018.json`)

### Rep 1 — correctitud: `correcta` · completitud: `completa`

- **Afirmación no soportada (CENTRAL):** "La Situación Normal comprende clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días."
  - **ADJUDICACIÓN FIRMADA (2026-06-10), verbatim:** veredicto = `verdadera` · evidencia = "Clasif 7.2.1 — Situación normal: puntual o ≤31 días"
- **Afirmación no soportada (CENTRAL):** "En la Situación en Observación, el análisis del flujo de fondos del cliente demuestra que puede atender la totalidad de sus compromisos."
  - **ADJUDICACIÓN FIRMADA (2026-06-10), verbatim:** veredicto = `verdadera` · evidencia = "Clasif 6.5.2.1 — En observación"
- **Afirmación no soportada (CENTRAL):** "Existe una categoría denominada Situación Irregular para la clasificación de deudores."
  - **ADJUDICACIÓN FIRMADA (2026-06-10), verbatim:** veredicto = `verdadera` · evidencia = "Clasif 6.5.5.7 — situación irregular (>180 días)"
- **Afirmación no soportada (secundaria):** "Estas entidades están obligadas a designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA."
  - (no figura como entrada propia en la adjudicación firmada)
- **Afirmación no soportada (secundaria):** "En la Situación Normal, el análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financieros."
  - (no figura como entrada propia en la adjudicación firmada)
- **Afirmación no soportada (secundaria):** "La clasificación debe efectuarse con una periodicidad que atienda a su importancia."
  - (no figura como entrada propia en la adjudicación firmada)
- **Afirmación no soportada (secundaria):** "La clasificación considera la totalidad de las financiaciones comprendidas."
  - (no figura como entrada propia en la adjudicación firmada)

### Rep 2 — correctitud: `correcta` · completitud: `completa`

- **Afirmación no soportada (secundaria):** "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deben designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA."
  - (no figura como entrada propia en la adjudicación firmada)
- **Afirmación no soportada (secundaria):** "La clasificación debe efectuarse con una periodicidad que atienda a la importancia del deudor."
  - (no figura como entrada propia en la adjudicación firmada)
- **Afirmación no soportada (secundaria):** "La clasificación debe considerar la totalidad de las financiaciones comprendidas."
  - (no figura como entrada propia en la adjudicación firmada)

### Rep 3 — correctitud: `correcta` · completitud: `completa`

- **Afirmación no soportada (CENTRAL):** "La categoría 'Situación Normal' corresponde a deudores cuyo análisis del flujo de fondos demuestra que son capaces de atender adecuadamente todos sus compromisos financieros."
  - **ADJUDICACIÓN FIRMADA (2026-06-10), verbatim:** veredicto = `verdadera` · evidencia = "Clasif 6.5.1/7.2.1 — Situación normal"
- **Afirmación no soportada (CENTRAL):** "La categoría 'Seguimiento Especial en Observación' corresponde a deudores cuyo análisis del flujo de fondos demuestra que pueden atender la totalidad de sus compromisos financieros pero existen situaciones posibles que podrían comprometer la capacidad futura de pago."
  - **ADJUDICACIÓN FIRMADA (2026-06-10), verbatim:** veredicto = `verdadera` · evidencia = "Clasif 6.5.2.1 — Seguimiento especial/En observación"
- **Afirmación no soportada (secundaria):** "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deben designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA."
  - (no figura como entrada propia en la adjudicación firmada)

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_3/CQ-018.json`)

`trace.final_json`:

```json
{
 "respuesta": "Sí, los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas deben cumplir con ambas obligaciones:\n\n1. **Protección al Usuario**: Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.\n\n2. **Clasificación de Deudores**: Los proveedores no financieros de crédito deberán clasificar a los respectivos deudores en función de su mora, según los criterios aplicables para la cartera de consumo o vivienda.\n\n**Criterio de Clasificación**: El criterio básico utilizado para efectuar la clasificación es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía. El énfasis se pone en el análisis de los flujos de fondos del cliente, evaluando si es capaz de atender adecuadamente todos sus compromisos financieros.",
 "citas": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 3.2. Controles. (parte 1)"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 10.1. Proveedores no financieros de crédito."
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 4.1. Niveles de clasificación."
  }
 ],
 "respondible": true
}
```

`trace.final_raw` (turno final íntegro):

```
```json
{
  "respuesta": "Sí, los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas deben cumplir con ambas obligaciones:\n\n1. **Protección al Usuario**: Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.\n\n2. **Clasificación de Deudores**: Los proveedores no financieros de crédito deberán clasificar a los respectivos deudores en función de su mora, según los criterios aplicables para la cartera de consumo o vivienda.\n\n**Criterio de Clasificación**: El criterio básico utilizado para efectuar la clasificación es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía. El énfasis se pone en el análisis de los flujos de fondos del cliente, evaluando si es capaz de atender adecuadamente todos sus compromisos financieros.",
  "citas": [
    {
      "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
      "location": "Punto 3.2. Controles. (parte 1)"
    },
    {
      "source_doc": "TO_clasificacion_deudores_actual.pdf",
      "location": "Punto 10.1. Proveedores no financieros de crédito."
    },
    {
      "source_doc": "TO_clasificacion_deudores_actual.pdf",
      "location": "Punto 4.1. Niveles de clasificación."
    }
  ],
  "respondible": true
}
```
```

## 3b. Inventario de pasos (almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados (traza) | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "proveedores no financieros crédito", "limite": 10}` | 3293 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "empresas no financieras emisoras tarjetas", "limite": 10}` | 3125 | 1215 | = runtime ✓ |
| 3 | buscar_nodos | `{"consulta": "clasificación deudores criterio", "limite": 10}` | 3298 | 1215 | = runtime ✓ |
| 4 | ver_nodo | `{"id": "Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr"}` | 688 | 688 | = runtime ✓ |
| 5 | ver_nodo | `{"id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf"}` | 397 | 397 | = runtime ✓ |
| 6 | buscar_nodos | `{"consulta": "protección usuario proveedores no financieros", "limite": 10}` | 3197 | 1215 | = runtime ✓ |
| 7 | ver_nodo | `{"id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf"}` | 434 | 434 | = runtime ✓ |
| 8 | buscar_nodos | `{"consulta": "clasificación deudores proveedores no financieros empresas emisoras tarjetas", "limite": 10}` | 3143 | 1215 | = runtime ✓ |
| 9 | buscar_nodos | `{"consulta": "criterios clasificación deudores situación categoría", "limite": 10}` | 3089 | 1215 | = runtime ✓ |
| 10 | ver_vecinos | `{"id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf", "direccion": "salientes"}` | 9756 | 1215 | = runtime ✓ |
| 11 | buscar_nodos | `{"consulta": "normal riesgo deficiente irrecuperable clasificación", "limite": 10}` | 3095 | 1215 | = runtime ✓ |
| 12 | buscar_nodos | `{"consulta": "análisis flujo fondos capacidad pago deudor", "limite": 10}` | 3354 | 1215 | = runtime ✓ |
| 13 | ver_nodo | `{"id": "Obligacion_evaluar_capacidad_de_pago"}` | 486 | 486 | = runtime ✓ |
| 14 | buscar_nodos | `{"consulta": "proveedores no financieros obligación clasificar deudores", "limite": 10}` | 3587 | 1215 | = runtime ✓ |
| 15 | ver_nodo | `{"id": "Obligacion_clasificar_deudores_por_mora"}` | 559 | 559 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 15/15 pasos con largo idéntico.** Outputs completos: apéndice del caso en `expediente_piloto_2.md`.

## 4. Homólogos del dev set

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** (verbatim, `referencias_dev_set.md`):

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

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES en juego (unión de las 3 reps del frozen):**
- "En la Situación en Observación, el análisis del flujo de fondos del cliente demuestra que puede atender la totalidad de sus compromisos."
- "Existe una categoría denominada Situación Irregular para la clasificación de deudores."
- "La Situación Normal comprende clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días."
- "La categoría 'Seguimiento Especial en Observación' corresponde a deudores cuyo análisis del flujo de fondos demuestra que pueden atender la totalidad de sus compromisos financieros pero existen situaciones posibles que podrían comprometer la capacidad futura de pago."
- "La categoría 'Situación Normal' corresponde a deudores cuyo análisis del flujo de fondos demuestra que son capaces de atender adecuadamente todos sus compromisos financieros."

**Patas de la pregunta (descomposición del juez post-hoc, `judge.step1`) × cobertura (`judge.step2.cobertura_patas`) × pasos que tocaron el tema:**
("pasos que tocaron el tema" = método mecánico: pasos cuya consulta o cuyo output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica)

| Pata (verbatim del juez) | Cobertura | Pasos que tocaron el tema |
|---|---|---|
| ¿Los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas deben cumplir con Protección al Usuario? | cubierta | 1, 2, 3, 4, 6, 7, 8, 11, 12, 14, 15 |
| ¿Los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas deben clasificar a sus deudores? | cubierta | 1, 2, 3, 4, 6, 8, 9, 11, 12, 14, 15 |
| ¿Bajo qué criterio clasifican a sus deudores? | cubierta | 3, 9, 12, 13 |

**Qué dice la respuesta final sobre las patas — descomposición del juez post-hoc (verbatim, `judge.step1`):**
- afirmación verificable (central): "Los proveedores no financieros de crédito deben cumplir con la normativa de Protección al Usuario de Servicios Financieros."
- afirmación verificable (central): "Las empresas no financieras emisoras de tarjetas de crédito y/o compra deben cumplir con la normativa de Protección al Usuario de Servicios Financieros."
- afirmación verificable (no central): "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA."
- afirmación verificable (central): "Los proveedores no financieros de crédito deben clasificar a sus deudores."
- afirmación verificable (central): "Los proveedores no financieros de crédito clasifican a sus deudores en función de su mora."
- afirmación verificable (central): "Los criterios de clasificación aplicables para los proveedores no financieros de crédito son los de la cartera de consumo o vivienda."
- afirmación verificable (central): "El criterio básico para efectuar la clasificación de deudores es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía."
- afirmación verificable (no central): "El énfasis en la clasificación se pone en el análisis de los flujos de fondos del cliente."
- afirmación verificable (no central): "La clasificación evalúa si el cliente es capaz de atender adecuadamente todos sus compromisos financieros."


---

# CQ-019 — [multi_norma]

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** Al computar los activos para la exigencia de capital por riesgo de crédito, ¿qué previsión por incobrabilidad no se deduce, y cómo se vincula esa regla con la clasificación de deudores?

**ground_truth_secciones:** ["Capitales, Punto 2.3.1", "Clasificación, Puntos 6.5.1 y 7.2.1"]
**tos_fuente:** ["capitales", "clasificacion"]

**cita_textual del GT:** "[Capitales 2.3.1] [...] netos de las previsiones por riesgos de incobrabilidad [...] sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados 'en situación normal' –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A)."

## 2. La falla según el frozen (verbatim por rep, `frozen_run/traces/run_3/CQ-019.json`)

### Rep 1 — correctitud: `correcta` · completitud: `completa`

- (sin afirmaciones no soportadas en esta rep)

### Rep 2 — correctitud: `correcta` · completitud: `completa`

- (sin afirmaciones no soportadas en esta rep)

### Rep 3 — correctitud: `correcta` · completitud: `completa`

- **Afirmación no soportada (CENTRAL):** "La no deducción de la previsión para deudores en situación normal se vincula con que estos presentan un perfil de menor riesgo crediticio."
  - **ADJUDICACIÓN FIRMADA (2026-06-10), verbatim:** veredicto = `no_verificable` · evidencia = "Inferencia del agente ("menor perfil de riesgo justifica no deducción"), no texto literal del corpus"
- **Afirmación no soportada (secundaria):** "Los deudores en situación normal atienden puntualmente sus obligaciones o con atrasos que no superan 31 días."
  - (no figura como entrada propia en la adjudicación firmada)
- **Afirmación no soportada (secundaria):** "Los deudores en situación normal demuestran capacidad de atender adecuadamente sus compromisos financieros."
  - (no figura como entrada propia en la adjudicación firmada)

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_3/CQ-019.json`)

`trace.final_json`:

```json
{
 "respuesta": "Al computar los activos para la exigencia de capital por riesgo de crédito, NO se deduce el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados 'en situación normal' ni a las financiaciones que se encuentran cubiertas con garantías preferidas A.\n\nEsta regla se vincula directamente con la clasificación de deudores en el sentido de que la restricción a la deducción de previsión aplica específicamente a aquellos deudores que han sido clasificados en 'situación normal' conforme a los puntos 6.5.1. y 7.2.1. del Texto Ordenado sobre Clasificación de Deudores. Es decir, la clasificación de un deudor como 'en situación normal' (que comprende clientes que atienden puntualmente el pago de sus obligaciones o con atrasos que no superan los 31 días) determina que la previsión por incobrabilidad asociada a esa cartera no pueda ser deducida en su totalidad del cómputo de activos para el cálculo de la exigencia de capital.",
 "citas": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.3. Cómputo de los conceptos comprendidos."
  }
 ],
 "respondible": true
}
```

`trace.final_raw` (turno final íntegro):

```
Tengo toda la información necesaria para responder la pregunta. Voy a formular la respuesta basada en lo que encontré en el Knowledge Graph.

```json
{
  "respuesta": "Al computar los activos para la exigencia de capital por riesgo de crédito, NO se deduce el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados 'en situación normal' ni a las financiaciones que se encuentran cubiertas con garantías preferidas A.\n\nEsta regla se vincula directamente con la clasificación de deudores en el sentido de que la restricción a la deducción de previsión aplica específicamente a aquellos deudores que han sido clasificados en 'situación normal' conforme a los puntos 6.5.1. y 7.2.1. del Texto Ordenado sobre Clasificación de Deudores. Es decir, la clasificación de un deudor como 'en situación normal' (que comprende clientes que atienden puntualmente el pago de sus obligaciones o con atrasos que no superan los 31 días) determina que la previsión por incobrabilidad asociada a esa cartera no pueda ser deducida en su totalidad del cómputo de activos para el cálculo de la exigencia de capital.",
  "citas": [
    {
      "source_doc": "TO_capitales_minimos_actual.pdf",
      "location": "Punto 2.3. Cómputo de los conceptos comprendidos."
    }
  ],
  "respondible": true
}
```
```

## 3b. Inventario de pasos (almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados (traza) | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "exigencia capital riesgo crédito previsión incobrabilidad", "limite": 10}` | 3374 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "previsión incobrabilidad deducción activos", "limite": 10}` | 3257 | 1215 | = runtime ✓ |
| 3 | buscar_nodos | `{"consulta": "clasificación deudores previsión", "limite": 10}` | 3280 | 1215 | = runtime ✓ |
| 4 | ver_nodo | `{"id": "Restriccion_limite_de_deduccion_de_prevision_normal"}` | 630 | 630 | = runtime ✓ |
| 5 | ver_nodo | `{"id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito"}` | 367 | 367 | = runtime ✓ |
| 6 | ver_vecinos | `{"id": "Restriccion_limite_de_deduccion_de_prevision_normal", "direccion": "ambas"}` | 762 | 762 | = runtime ✓ |
| 7 | buscar_nodos | `{"consulta": "deudores situación normal previsión", "limite": 10}` | 3230 | 1215 | = runtime ✓ |
| 8 | buscar_nodos | `{"consulta": "garantías preferidas A previsión deducción", "limite": 10}` | 3763 | 1215 | = runtime ✓ |
| 9 | ver_nodo | `{"id": "Operacion_computo"}` | 459 | 459 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 9/9 pasos con largo idéntico.** Outputs completos: apéndice del caso en `expediente_piloto_2.md`.

## 4. Homólogos del dev set

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** (verbatim, `referencias_dev_set.md`):

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

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** (verbatim, `referencias_dev_set.md`):

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

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES en juego (unión de las 3 reps del frozen):**
- "La no deducción de la previsión para deudores en situación normal se vincula con que estos presentan un perfil de menor riesgo crediticio."

**Patas de la pregunta (descomposición del juez post-hoc, `judge.step1`) × cobertura (`judge.step2.cobertura_patas`) × pasos que tocaron el tema:**
("pasos que tocaron el tema" = método mecánico: pasos cuya consulta o cuyo output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica)

| Pata (verbatim del juez) | Cobertura | Pasos que tocaron el tema |
|---|---|---|
| Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito | cubierta | 1, 2, 3, 4, 5, 7, 8 |
| Cómo se vincula esa regla con la clasificación de deudores | cubierta | 3, 4, 7 |

**Qué dice la respuesta final sobre las patas — descomposición del juez post-hoc (verbatim, `judge.step1`):**
- afirmación verificable (central): "Al computar los activos para la exigencia de capital por riesgo de crédito, NO se deduce el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados 'en situación normal'."
- afirmación verificable (central): "Al computar los activos para la exigencia de capital por riesgo de crédito, NO se deduce el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a las financiaciones cubiertas con garantías preferidas A."
- afirmación verificable (central): "La restricción a la deducción de previsión aplica específicamente a deudores clasificados en 'situación normal' conforme a los puntos 6.5.1. y 7.2.1. del Texto Ordenado sobre Clasificación de Deudores."
- afirmación verificable (no central): "La clasificación 'en situación normal' comprende clientes que atienden puntualmente el pago de sus obligaciones o con atrasos que no superan los 31 días."
- afirmación verificable (central): "La clasificación de un deudor como 'en situación normal' determina que la previsión por incobrabilidad asociada a esa cartera no pueda ser deducida en su totalidad del cómputo de activos para el cálculo de la exigencia de capital."


---

# CQ-024 — [multi_norma]

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** ¿Con qué periodicidad mínima debe clasificarse un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC, y en qué casos la reevaluación debe ser inmediata?

**ground_truth_secciones:** ["Punto 6.3.1 (Periodicidad mínima)", "Punto 6.4 (Reconsideración obligatoria, último párrafo)"]
**tos_fuente:** ["clasificacion"]

**cita_textual del GT:** "[6.3.1] En el curso de cada trimestre calendario, respecto de clientes [...] cuyas financiaciones comprendidas [...] sean equivalentes al 5 % o más de la RPC [...] | [6.4 último párrafo] La reevaluación deberá ser inmediata cuando se trate de clientes cuyas financiaciones comprendidas igualen o superen el 1 % de la responsabilidad patrimonial computable [...] o el equivalente al importe de referencia [...], de ambos el menor, y dentro de los tres meses respecto de los demás clientes."

## 2. La falla según el frozen (verbatim por rep, `frozen_run/traces/run_3/CQ-024.json`)

### Rep 1 — correctitud: `correcta` · completitud: `completa`

- **Afirmación no soportada (CENTRAL):** "La reevaluación debe ser inmediata cuando las financiaciones del cliente igualen o superen el 1% del activo del fideicomiso financiero."
  - **ADJUDICACIÓN FIRMADA (2026-06-10), verbatim:** veredicto = `verdadera` · evidencia = "Clasif 6.4.4 — reevaluación inmediata si ≥1% RPC/activo del fideicomiso"

### Rep 2 — correctitud: `correcta` · completitud: `completa`

- (sin afirmaciones no soportadas en esta rep)

### Rep 3 — correctitud: `correcta` · completitud: `completa`

- (sin afirmaciones no soportadas en esta rep)

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_3/CQ-024.json`)

`trace.final_json`:

```json
{
 "respuesta": "Según la normativa de clasificación de deudores del BCRA, un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC debe ser clasificado con una periodicidad mínima trimestral.\n\nRespecto a los casos de reevaluación inmediata, la normativa establece que la reevaluación deberá ser inmediata cuando se trate de clientes cuyas financiaciones comprendidas igualen o superen el 1% de la responsabilidad patrimonial computable de la entidad o del activo del fideicomiso financiero. Sin embargo, la información disponible en el grafo no especifica detalladamente todos los casos particulares en los que la reevaluación debe ser inmediata para deudores de cartera comercial con financiaciones del 5% de RPC.",
 "citas": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.3. Periodicidad mínima de clasificación."
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.4. Reconsideración obligatoria de la clasificación."
  }
 ],
 "respondible": false
}
```

`trace.final_raw` (turno final íntegro):

```
```json
{
  "respuesta": "Según la normativa de clasificación de deudores del BCRA, un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC debe ser clasificado con una periodicidad mínima trimestral.\n\nRespecto a los casos de reevaluación inmediata, la normativa establece que la reevaluación deberá ser inmediata cuando se trate de clientes cuyas financiaciones comprendidas igualen o superen el 1% de la responsabilidad patrimonial computable de la entidad o del activo del fideicomiso financiero. Sin embargo, la información disponible en el grafo no especifica detalladamente todos los casos particulares en los que la reevaluación debe ser inmediata para deudores de cartera comercial con financiaciones del 5% de RPC.",
  "citas": [
    {
      "source_doc": "TO_clasificacion_deudores_actual.pdf",
      "location": "Punto 6.3. Periodicidad mínima de clasificación."
    },
    {
      "source_doc": "TO_clasificacion_deudores_actual.pdf",
      "location": "Punto 6.4. Reconsideración obligatoria de la clasificación."
    }
  ],
  "respondible": false
}
```
```

## 3b. Inventario de pasos (almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados (traza) | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "clasificación deudor cartera comercial RPC periodicidad", "limite": 10}` | 2629 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "reevaluación inmediata deudor comercial", "limite": 10}` | 2724 | 1215 | = runtime ✓ |
| 3 | ver_nodo | `{"id": "Obligacion_la_clasificacion_de_los_deudores_debera_efectuarse_con_una_periodicidad_que_atie"}` | 560 | 560 | = runtime ✓ |
| 4 | ver_nodo | `{"id": "Obligacion_la_reevaluacion_debera_ser_inmediata_cuando_se_trate_de_clientes_cuyas_financiac"}` | 622 | 622 | = runtime ✓ |
| 5 | buscar_nodos | `{"consulta": "5% RPC responsabilidad patrimonial computable", "limite": 10}` | 3297 | 1215 | = runtime ✓ |
| 6 | buscar_nodos | `{"consulta": "periodicidad trimestral semestral deudor comercial", "limite": 10}` | 2545 | 1215 | = runtime ✓ |
| 7 | ver_nodo | `{"id": "Restriccion_clientes_cuyas_financiaciones_sean_equivalentes_al_5_o_mas_de_la_rpc_o_del_activ"}` | 512 | 512 | = runtime ✓ |
| 8 | ver_nodo | `{"id": "Obligacion_la_revision_debera_efectuarse_como_minimo_con_la_periodicidad_que_se_indica_segu"}` | 559 | 559 | = runtime ✓ |
| 9 | ver_vecinos | `{"id": "Restriccion_clientes_cuyas_financiaciones_sean_equivalentes_al_5_o_mas_de_la_rpc_o_del_activ", "direccion": "ambas"}` | 1375 | 1214 | = runtime ✓ |
| 10 | ver_vecinos | `{"id": "Obligacion_la_reevaluacion_debera_ser_inmediata_cuando_se_trate_de_clientes_cuyas_financiac", "direccion": "ambas"}` | 1124 | 1124 | = runtime ✓ |
| 11 | buscar_nodos | `{"consulta": "reconsideración obligatoria clasificación casos inmediata", "limite": 10}` | 2719 | 1215 | = runtime ✓ |
| 12 | buscar_nodos | `{"consulta": "reevaluación inmediata atraso incumplimiento cambio situación", "limite": 10}` | 2703 | 1215 | = runtime ✓ |
| 13 | buscar_nodos | `{"consulta": "punto 6.4 reconsideración obligatoria casos reevaluación", "limite": 10}` | 3412 | 1215 | = runtime ✓ |
| 14 | buscar_nodos | `{"consulta": "reevaluación inmediata mora atraso 60 días incumplimiento", "limite": 10}` | 3699 | 1215 | = runtime ✓ |
| 15 | buscar_nodos | `{"consulta": "cambio situación financiera deterioro información negativa reevaluación", "limite": 10}` | 3494 | 1215 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 15/15 pasos con largo idéntico.** Outputs completos: apéndice del caso en `expediente_piloto_2.md`.

## 4. Homólogos del dev set

> **OTRO GRAFO — precedente taxonómico, NO evidencia de este caso** (verbatim, `referencias_dev_set.md`):

````markdown
## Caso off/run_1/CQ-024

**Pregunta:** ¿Con qué periodicidad mínima debe clasificarse un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC, y en qué casos la reevaluación debe ser inmediata?

Adjudicación de la autora, 2026-07-13, asistida por revisión:

- **Pata 2 — claims** "La reevaluación debe ser inmediata cuando se producen atrasos mayores a 31 días" [no_soportado] y "Los atrasos mayores a 31 días generan reclasificación inmediata del deudor al nivel resultante de sumar días de atraso efectivo y atraso normativo" [no_soportado] — **`{noise_sensitivity, contenido_kg}` PRIMARIA.** Evidencia: soportados por `req_atrasos_mayores_a_31_dias` (abierto por el agente en el paso 15), cuyo contenido no existe en el TO — "atraso efectivo", "atraso normativo" y la fórmula de suma dan 0 matches en el documento completo; la regla real es la recategorización por atrasos >31 días en obligaciones REFINANCIADAS (6.5.x), sin fórmula de suma y sin alcance general — nodo con regla deformada/des-scopeada.
- **Pata 2 — claim** "La reevaluación debe ser inmediata cuando existe discrepancia de más de un nivel en clasificaciones y las financiaciones superan el 1% de la RPC" [falso] — **FALSO POSITIVO DEL JUEZ, sin par.** Evidencia: soportado por `req_reevaluacion_inmediata_por_discrepancia_de_mas_de_un_nivel_en_clasificaciones` (abierto en el paso 4) y correcto contra el PDF (Clasificación 6.4.4 + último párrafo del 6.4: "La reevaluación deberá ser inmediata cuando... igualen o superen el 1% de la responsabilidad patrimonial computable...") — condensado pero sustancialmente correcto.
- **Pata 1 (periodicidad mínima)** — "trimestral" — **sin defecto.** Evidencia: soportado por `req_analisis_trimestral_de_clientes_con_financiaciones_que_alcanzan_el_5_o_mas_de_la_responsabilidad_patrimonial_computable` (abierto en el paso 7) y correcto contra el Punto 6.3.1.

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion.md` (scratch, no versionado).
````

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES en juego (unión de las 3 reps del frozen):**
- "La reevaluación debe ser inmediata cuando las financiaciones del cliente igualen o superen el 1% del activo del fideicomiso financiero."

**Patas de la pregunta (descomposición del juez post-hoc, `judge.step1`) × cobertura (`judge.step2.cobertura_patas`) × pasos que tocaron el tema:**
("pasos que tocaron el tema" = método mecánico: pasos cuya consulta o cuyo output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica)

| Pata (verbatim del juez) | Cobertura | Pasos que tocaron el tema |
|---|---|---|
| Periodicidad mínima de clasificación de un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC | cubierta | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15 |
| Casos en que la reevaluación debe ser inmediata | cubierta | 2, 4, 10, 11, 12, 13, 14, 15 |

**Qué dice la respuesta final sobre las patas — descomposición del juez post-hoc (verbatim, `judge.step1`):**
- afirmación verificable (central): "Un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC debe ser clasificado con una periodicidad mínima trimestral."
- afirmación verificable (central): "La reevaluación debe ser inmediata cuando se trate de clientes cuyas financiaciones comprendidas igualen o superen el 1% de la responsabilidad patrimonial computable de la entidad o del activo del fideicomiso financiero."
- reporte de alcance: "La información disponible en el grafo no especifica detalladamente todos los casos particulares en los que la reevaluación debe ser inmediata para deudores de cartera comercial con financiaciones del 5% de RPC."


---

# CQ-033 — [cadena_restriccion_excepcion]

## 1. Pregunta y ground truth (verbatim, `queries/eval_set_v1.json`)

**Pregunta:** ¿Cuál es el límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2, y bajo qué condiciones ese límite se reduce?

**ground_truth_secciones:** ["Punto 7.3 (Límite para las entidades del grupo 2)"]
**tos_fuente:** ["capitales"]

**cita_textual del GT:** "[7.3.1] El 20% en el caso de entidades del grupo A del promedio de los últimos 36 meses [...] de la exigencia de capital mínimo por riesgo de crédito [...] [7.3.2] El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses [...]. El límite máximo establecido precedentemente se reducirá a 11% cuando la entidad financiera cuente con calificación 1, 2 o 3 [...]. En los casos en que la entidad financiera cuente en todos los citados aspectos con calificación 1 o 2, el límite máximo disminuirá a 7%."

## 2. La falla según el frozen (verbatim por rep, `frozen_run/traces/run_3/CQ-033.json`)

### Rep 1 — correctitud: `correcta` · completitud: `completa`

- **Afirmación no soportada (CENTRAL):** "El límite del 17% está vigente hasta el 30/06/26"
  - **ADJUDICACIÓN FIRMADA (2026-06-10), verbatim:** veredicto = `verdadera` · evidencia = "Capitales Sección 12 — 17% (Grupo B) hasta 30/06/26"

### Rep 2 — correctitud: `correcta` · completitud: `completa`

- **Afirmación no soportada (secundaria):** "El límite del 17% está vigente hasta el 30/06/26"
  - **ADJUDICACIÓN FIRMADA (2026-06-10), verbatim:** veredicto = `verdadera` · evidencia = "Capitales Sección 12 — 17% (Grupo B) hasta 30/06/26"

### Rep 3 — correctitud: `correcta` · completitud: `completa`

- **Afirmación no soportada (secundaria):** "El límite del 17% está vigente hasta el 30/06/26"
  - **ADJUDICACIÓN FIRMADA (2026-06-10), verbatim:** veredicto = `verdadera` · evidencia = "Capitales Sección 12 — 17% (Grupo B) hasta 30/06/26"

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_3/CQ-033.json`)

`trace.final_json`:

```json
{
 "respuesta": "El límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2 (Grupo B) es del 17% del promedio de los últimos 36 meses, vigente hasta el 30/06/26.\n\nEste límite se reduce bajo las siguientes condiciones:\n\n1. **Reducción a 11%**: Cuando la entidad financiera cuente con calificación 1, 2 o 3 conforme a la valoración otorgada por la SEFYC.\n\n2. **Reducción a 7%**: Cuando la entidad financiera cuente en todos los aspectos evaluados con calificación 1 o 2 según la SEFYC.",
 "citas": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ],
 "respondible": true
}
```

`trace.final_raw` (turno final íntegro):

```
Tengo la información necesaria. Ahora voy a compilar la respuesta con los datos obtenidos.

```json
{
  "respuesta": "El límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2 (Grupo B) es del 17% del promedio de los últimos 36 meses, vigente hasta el 30/06/26.\n\nEste límite se reduce bajo las siguientes condiciones:\n\n1. **Reducción a 11%**: Cuando la entidad financiera cuente con calificación 1, 2 o 3 conforme a la valoración otorgada por la SEFYC.\n\n2. **Reducción a 7%**: Cuando la entidad financiera cuente en todos los aspectos evaluados con calificación 1 o 2 según la SEFYC.",
  "citas": [
    {
      "source_doc": "TO_capitales_minimos_actual.pdf",
      "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
    }
  ],
  "respondible": true
}
```
```

## 3b. Inventario de pasos (almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados (traza) | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "capital riesgo operacional Grupo 2", "limite": 10}` | 3239 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "límite exigencia capital operacional", "limite": 10}` | 3695 | 1215 | = runtime ✓ |
| 3 | ver_nodo | `{"id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ"}` | 673 | 673 | = runtime ✓ |
| 4 | ver_vecinos | `{"id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ", "direccion": "ambas"}` | 1936 | 1214 | = runtime ✓ |
| 5 | ver_nodo | `{"id": "Excepcion_los_limites_maximos_se_reduciran_a_11_y_8_respectivamente_cuando_la_entidad_fina"}` | 557 | 557 | = runtime ✓ |
| 6 | ver_nodo | `{"id": "Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c"}` | 560 | 560 | = runtime ✓ |
| 7 | ver_vecinos | `{"id": "Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c", "direccion": "ambas"}` | 1669 | 1214 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 7/7 pasos con largo idéntico.** Outputs completos: apéndice del caso en `expediente_piloto_2.md`.

## 4. Homólogos del dev set

**SIN HOMÓLOGO** en `referencias_dev_set.md` (verificado: cero menciones). Medición limpia según el protocolo §3.

## 5. Tabla inicial de hechos (solo hechos; método mecánico documentado)

**Claims CENTRALES en juego (unión de las 3 reps del frozen):**
- "El límite del 17% está vigente hasta el 30/06/26"

**Patas de la pregunta (descomposición del juez post-hoc, `judge.step1`) × cobertura (`judge.step2.cobertura_patas`) × pasos que tocaron el tema:**
("pasos que tocaron el tema" = método mecánico: pasos cuya consulta o cuyo output completo re-ejecutado contiene ≥2 tokens no-stopword de la pata; no es lectura semántica)

| Pata (verbatim del juez) | Cobertura | Pasos que tocaron el tema |
|---|---|---|
| Cuál es el límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2 | cubierta | 1, 2, 3, 4, 5, 6, 7 |
| Bajo qué condiciones ese límite se reduce | cubierta | 1, 2, 4, 5 |

**Qué dice la respuesta final sobre las patas — descomposición del juez post-hoc (verbatim, `judge.step1`):**
- afirmación verificable (central): "El límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2 (Grupo B) es del 17% del promedio de los últimos 36 meses"
- afirmación verificable (no central): "Ese límite del 17% está vigente hasta el 30/06/26"
- afirmación verificable (central): "El límite se reduce al 11% cuando la entidad financiera cuenta con calificación 1, 2 o 3 conforme a la valoración otorgada por la SEFYC"
- afirmación verificable (central): "El límite se reduce al 7% cuando la entidad financiera cuenta en todos los aspectos evaluados con calificación 1 o 2 según la SEFYC"
- afirmación verificable (no central): "La entidad del Grupo 2 también se denomina Grupo B"
- afirmación verificable (central): "La calificación que determina la reducción del límite es otorgada por la SEFYC"

