# Verificación estructural para la adjudicación del piloto

Fecha: 2026-07-16. SOLO LECTURA; única escritura: este archivo. No se corrió el verificador
ni la capa. Sin commits. Sin adjudicación — hechos con código y datos verbatim.

## 1. Qué recibe el verificador como "la falla"

**Circuito (código verbatim):** cuando `verificador.py` se invoca con un id de falla
(`off/run_3/CQ-018`), el contexto lo arma `build_falla_context(label, run, qid)`
([verificador.py:547]) a partir de la **traza POST-HOC**, no del frozen:

```python
# verificador.py:561
    rep = load_rep(label, run, qid)

# verifier_pilot.py:78-80 (importado en verificador.py:49)
def load_rep(label, run, qid):
    p = EVAL_DIR / "posthoc_run" / "traces" / label / run / f"{qid}.json"
    return json.load(open(p))[0]
```

**(a) El veredicto del juez presentado es el POST-HOC**, con estos campos:

- `judge.step1` completo — patas, afirmaciones verificables con centralidad, reportes de
  alcance (verificador.py:567-581);
- `judge.step2.verificaciones` filtradas a `falso`/`no_soportado` como **SÍNTOMA**
  (verificador.py:583-591):

```python
    # Síntoma: las afirmaciones que el juez marcó incorrectas.
    verifs = ((rep.get("judge") or {}).get("step2") or {}).get("verificaciones") or []
    fallidos = [v for v in verifs if v.get("verdict") in ("falso", "no_soportado")]
```

- las aprobadas van en sección aparte "no re-litigar" (verificador.py:593-600).
- **`cobertura_patas` NO se presenta** — `build_falla_context` no la incluye en ningún
  bloque del contexto (verificado sobre el cuerpo completo de la función, líneas 547-672).
- Si el juez post-hoc no marcó nada, el síntoma queda literal:
  `"(el juez no expuso afirmaciones desagregadas; revisá la respuesta final completa)"`
  (verificador.py:590-591).

**(b) La respuesta del agente** = `trace.final_json` de la misma traza post-hoc
(verificador.py:564 y el bloque `--- RESPUESTA FINAL DEL AGENTE ---`, líneas 653-656).

**(c) La trayectoria** = `trace.steps` de la traza post-hoc, con los **outputs TRUNCADOS tal
como están almacenados** (`s.get("output_truncado")`, verificador.py:612-614) — los outputs
íntegros solo vía la tool `ver_paso_completo` —, más los **nodos vistos con contenido
ÍNTEGRO** recuperados de la caché del agente (`recover_seen`, verifier_pilot.py:97+, que lee
`cache/calls.db`, namespace `agent|gfp=...|think=...`; verificador.py:622-634).

**Evidencia de formato — fragmento del prompt ensamblado para un caso del gate YA corrido
(off/run_3/CQ-031), re-ensamblado desde los insumos (no de gate2_v57/):**

```
FALLA A INVESTIGAR — pregunta CQ-031 (categoría: cadena_restriccion_excepcion) sobre el grafo run_3.

PREGUNTA:
¿Qué deudores no deben ser objeto de clasificación y respecto de qué deudores no corresponde evaluar la capacidad de repago?

--- DESCOMPOSICIÓN DEL JUEZ (step1) ---
patas de la pregunta:
  - Qué deudores no deben ser objeto de clasificación
  - Respecto de qué deudores no corresponde evaluar la capacidad de repago
afirmaciones verificables extraídas de la respuesta:
  - [central] "Los deudores en operaciones de cesión sin responsabilidad para el cedente no deben ser objeto de clasificación."
  - [no central] "Esta exclusión de clasificación está regulada en el Punto 4.6 de la normativa del BCRA."
  - [central] "Respecto de los deudores cuyas financiaciones se encuentren respaldadas con garantías preferidas 'A', no corresponde evaluar la capacidad de repago."
  - [central] "La exclusión de evaluación de capacidad de repago aplica únicamente respecto de las financiaciones que se encuentren respaldadas con garantías preferidas 'A'."
  - [no central] "Esta exclusión de evaluación de capacidad de repago está regulada en el Punto 4.4 de la normativa del BCRA."

--- SÍNTOMA: afirmaciones que el juez marcó incorrectas ---
  - [no_soportado/central] "Los deudores en operaciones de cesión sin responsabilidad para el cedente no deben ser objeto de clasificación."
  - [falso] "Esta exclusión de clasificación está regulada en el Punto 4.6 de la normativa del BCRA."

--- AFIRMACIONES QUE EL JUEZ APROBÓ — no re-litigar ---
  - [OK/central] "Respecto de los deudores cuyas financiaciones se encuentren respaldadas con garantías preferidas 'A', no corresponde evaluar la capacidad de repago."
  - [OK/central] "La exclusión de evaluación de capacidad de repago aplica únicamente respecto de las financiaciones que se encuentren respaldadas con garantías preferidas 'A'."
  - [OK] "Esta exclusión de evaluación de capacidad de repago está regulada en el Punto 4.4 de la normativa del BCRA."

--- RESPUESTA FINAL DEL AGENTE ---
respuesta: [respuesta completa del agente — verbatim en el expediente]
citas: TO_clasificacion_deudores_actual.pdf :: Punto 4.5. ...; :: Punto 4.6. ...; :: Punto 4.4. ...
respondible (declarado por el agente): True

[... sigue: TRAYECTORIA (15 pasos, outputs TRUNCADOS de la traza; ver_paso_completo disponible
como tool), NODOS VISTOS (n_seen=68, contenido íntegro desde la caché del agente), ESQUEMA DEL
GRAFO, instrucción final]
```

**El hecho estructural central para la adjudicación del piloto:** el universo del piloto se
seleccionó por los síntomas del FROZEN (3 reps de otra corrida), pero el verificador
investiga el síntoma del juez POST-HOC (una re-corrida N=1 con otra respuesta). En los 5
casos del piloto esos dos veredictos NO coinciden (sección 2): en particular, **el juez
post-hoc no registró falla alguna en CQ-016 ni en CQ-024** (correcta/completa, cero claims
reprobados) — para esos casos el verificador recibiría el síntoma vacío con la leyenda
literal de la línea 591.

## 2. Juez POST-HOC — CQ-016
-- step2.verificaciones (verbatim) --
[
 {
  "enunciado": "Los importes en el régimen informativo se registran en miles de pesos",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Los importes en el régimen informativo se registran sin decimales",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La norma sobre registro en miles de pesos sin decimales está documentada en el Régimen Informativo Contable Mensual (Punto 1.2)",
  "central": false,
  "verdict": "verdadero"
 }
]
-- step2.cobertura_patas (verbatim) --
[
 {
  "pata": "Unidad en que deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos",
  "cobertura": "cubierta"
 },
 {
  "pata": "Nivel de decimales con que deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos",
  "cobertura": "cubierta"
 }
]
-- verdict post-hoc --
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
-- TABLA claim -> posthoc -> frozen -> firmada --
CLAIM [verdadero/central]: "Los importes en el régimen informativo se registran en miles de pesos"
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [verdadero/central]: "Los importes en el régimen informativo se registran sin decimales"
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [verdadero]: "La norma sobre registro en miles de pesos sin decimales está documentada en el Régimen Informativo Contable Mensual (Punto 1.2)"
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura

## 2. Juez POST-HOC — CQ-018
-- step2.verificaciones (verbatim) --
[
 {
  "enunciado": "Los proveedores no financieros de crédito deben cumplir con la normativa de Protección al Usuario de Servicios Financieros.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Las empresas no financieras emisoras de tarjetas de crédito y/o compra deben cumplir con la normativa de Protección al Usuario de Servicios Financieros.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "Los proveedores no financieros de crédito deben clasificar a sus deudores.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Los proveedores no financieros de crédito clasifican a sus deudores en función de su mora.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Los criterios de clasificación aplicables para los proveedores no financieros de crédito son los de la cartera de consumo o vivienda.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "El criterio básico para efectuar la clasificación de deudores es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía.",
  "central": true,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "El énfasis en la clasificación se pone en el análisis de los flujos de fondos del cliente.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "La clasificación evalúa si el cliente es capaz de atender adecuadamente todos sus compromisos financieros.",
  "central": false,
  "verdict": "no_soportado"
 }
]
-- step2.cobertura_patas (verbatim) --
[
 {
  "pata": "¿Los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas deben cumplir con Protección al Usuario?",
  "cobertura": "cubierta"
 },
 {
  "pata": "¿Los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas deben clasificar a sus deudores?",
  "cobertura": "cubierta"
 },
 {
  "pata": "¿Bajo qué criterio clasifican a sus deudores?",
  "cobertura": "cubierta"
 }
]
-- verdict post-hoc --
{
 "correctitud": "correcta",
 "completitud": "completa",
 "afirmaciones_no_soportadas": {
  "centrales": [
   "El criterio básico para efectuar la clasificación de deudores es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía."
  ],
  "secundarias": [
   "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.",
   "El énfasis en la clasificación se pone en el análisis de los flujos de fondos del cliente.",
   "La clasificación evalúa si el cliente es capaz de atender adecuadamente todos sus compromisos financieros."
  ],
  "n_centrales": 1,
  "n_secundarias": 3
 }
}
-- TABLA claim -> posthoc -> frozen -> firmada --
CLAIM [verdadero/central]: "Los proveedores no financieros de crédito deben cumplir con la normativa de Protección al Usuario de Servicios Financieros."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [verdadero/central]: "Las empresas no financieras emisoras de tarjetas de crédito y/o compra deben cumplir con la normativa de Protección al Usuario de Servicios Financieros."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [no_soportado]: "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [verdadero/central]: "Los proveedores no financieros de crédito deben clasificar a sus deudores."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [verdadero/central]: "Los proveedores no financieros de crédito clasifican a sus deudores en función de su mora."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [verdadero/central]: "Los criterios de clasificación aplicables para los proveedores no financieros de crédito son los de la cartera de consumo o vivienda."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [no_soportado/central]: "El criterio básico para efectuar la clasificación de deudores es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [no_soportado]: "El énfasis en la clasificación se pone en el análisis de los flujos de fondos del cliente."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [no_soportado]: "La clasificación evalúa si el cliente es capaz de atender adecuadamente todos sus compromisos financieros."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura

## 2. Juez POST-HOC — CQ-019
-- step2.verificaciones (verbatim) --
[
 {
  "enunciado": "Al computar los activos para la exigencia de capital por riesgo de crédito, NO se deduce el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados 'en situación normal'.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Al computar los activos para la exigencia de capital por riesgo de crédito, NO se deduce el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a las financiaciones cubiertas con garantías preferidas A.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La restricción a la deducción de previsión aplica específicamente a deudores clasificados en 'situación normal' conforme a los puntos 6.5.1. y 7.2.1. del Texto Ordenado sobre Clasificación de Deudores.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La clasificación 'en situación normal' comprende clientes que atienden puntualmente el pago de sus obligaciones o con atrasos que no superan los 31 días.",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "La clasificación de un deudor como 'en situación normal' determina que la previsión por incobrabilidad asociada a esa cartera no pueda ser deducida en su totalidad del cómputo de activos para el cálculo de la exigencia de capital.",
  "central": true,
  "verdict": "verdadero"
 }
]
-- step2.cobertura_patas (verbatim) --
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
-- verdict post-hoc --
{
 "correctitud": "correcta",
 "completitud": "completa",
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [
   "La clasificación 'en situación normal' comprende clientes que atienden puntualmente el pago de sus obligaciones o con atrasos que no superan los 31 días."
  ],
  "n_centrales": 0,
  "n_secundarias": 1
 }
}
-- TABLA claim -> posthoc -> frozen -> firmada --
CLAIM [verdadero/central]: "Al computar los activos para la exigencia de capital por riesgo de crédito, NO se deduce el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados 'en situación normal'."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [verdadero/central]: "Al computar los activos para la exigencia de capital por riesgo de crédito, NO se deduce el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a las financiaciones cubiertas con garantías preferidas A."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [verdadero/central]: "La restricción a la deducción de previsión aplica específicamente a deudores clasificados en 'situación normal' conforme a los puntos 6.5.1. y 7.2.1. del Texto Ordenado sobre Clasificación de Deudores."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [no_soportado]: "La clasificación 'en situación normal' comprende clientes que atienden puntualmente el pago de sus obligaciones o con atrasos que no superan los 31 días."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [verdadero/central]: "La clasificación de un deudor como 'en situación normal' determina que la previsión por incobrabilidad asociada a esa cartera no pueda ser deducida en su totalidad del cómputo de activos para el cálculo de la exigencia de capital."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura

## 2. Juez POST-HOC — CQ-024
-- step2.verificaciones (verbatim) --
[
 {
  "enunciado": "Un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC debe ser clasificado con una periodicidad mínima trimestral.",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La reevaluación debe ser inmediata cuando se trate de clientes cuyas financiaciones comprendidas igualen o superen el 1% de la responsabilidad patrimonial computable de la entidad o del activo del fideicomiso financiero.",
  "central": true,
  "verdict": "verdadero"
 }
]
-- step2.cobertura_patas (verbatim) --
[
 {
  "pata": "Periodicidad mínima de clasificación de un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC",
  "cobertura": "cubierta"
 },
 {
  "pata": "Casos en que la reevaluación debe ser inmediata",
  "cobertura": "cubierta"
 }
]
-- verdict post-hoc --
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
-- TABLA claim -> posthoc -> frozen -> firmada --
CLAIM [verdadero/central]: "Un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC debe ser clasificado con una periodicidad mínima trimestral."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [verdadero/central]: "La reevaluación debe ser inmediata cuando se trate de clientes cuyas financiaciones comprendidas igualen o superen el 1% de la responsabilidad patrimonial computable de la entidad o del activo del fideicomiso financiero."
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura

## 2. Juez POST-HOC — CQ-033
-- step2.verificaciones (verbatim) --
[
 {
  "enunciado": "El límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2 (Grupo B) es del 17% del promedio de los últimos 36 meses",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "Ese límite del 17% está vigente hasta el 30/06/26",
  "central": false,
  "verdict": "no_soportado"
 },
 {
  "enunciado": "El límite se reduce al 11% cuando la entidad financiera cuenta con calificación 1, 2 o 3 conforme a la valoración otorgada por la SEFYC",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "El límite se reduce al 7% cuando la entidad financiera cuenta en todos los aspectos evaluados con calificación 1 o 2 según la SEFYC",
  "central": true,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La entidad del Grupo 2 también se denomina Grupo B",
  "central": false,
  "verdict": "verdadero"
 },
 {
  "enunciado": "La calificación que determina la reducción del límite es otorgada por la SEFYC",
  "central": true,
  "verdict": "verdadero"
 }
]
-- step2.cobertura_patas (verbatim) --
[
 {
  "pata": "Cuál es el límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2",
  "cobertura": "cubierta"
 },
 {
  "pata": "Bajo qué condiciones ese límite se reduce",
  "cobertura": "cubierta"
 }
]
-- verdict post-hoc --
{
 "correctitud": "correcta",
 "completitud": "completa",
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [
   "Ese límite del 17% está vigente hasta el 30/06/26"
  ],
  "n_centrales": 0,
  "n_secundarias": 1
 }
}
-- TABLA claim -> posthoc -> frozen -> firmada --
CLAIM [verdadero/central]: "El límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2 (Grupo B) es del 17% del promedio de los últimos 36 meses"
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [no_soportado]: "Ese límite del 17% está vigente hasta el 30/06/26"
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [verdadero/central]: "El límite se reduce al 11% cuando la entidad financiera cuenta con calificación 1, 2 o 3 conforme a la valoración otorgada por la SEFYC"
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [verdadero/central]: "El límite se reduce al 7% cuando la entidad financiera cuenta en todos los aspectos evaluados con calificación 1 o 2 según la SEFYC"
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [verdadero]: "La entidad del Grupo 2 también se denomina Grupo B"
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura
CLAIM [verdadero/central]: "La calificación que determina la reducción del límite es otorgada por la SEFYC"
   frozen(no-soportadas): no figura
   adjudicacion firmada: no figura

## 3. CQ-018 — nodos abiertos en pasos 4, 13 y 15 (contenido completo re-ejecutado, con provenances)
-- paso 4: ver_nodo({"id": "Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr"}) --
{
 "id": "Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr",
 "type": "Obligacion",
 "label": "Designar Directivo Responsable de Protección",
 "properties": {
  "descripcion": "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.",
  "tipo": "asignacion"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 3.2. Controles. (parte 1)"
  }
 ]
}
-- paso 13: ver_nodo({"id": "Obligacion_evaluar_capacidad_de_pago"}) --
{
 "id": "Obligacion_evaluar_capacidad_de_pago",
 "type": "Obligacion",
 "label": "Evaluar capacidad de pago",
 "properties": {
  "tipo": "calculo",
  "description": "El criterio básico a ser utilizado para efectuar la clasificación es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía de la entidad financiera",
  "plazo": "futuro"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 4.1. Niveles de clasificación."
  }
 ]
}
-- paso 15: ver_nodo({"id": "Obligacion_clasificar_deudores_por_mora"}) --
{
 "id": "Obligacion_clasificar_deudores_por_mora",
 "type": "Obligacion",
 "label": "Clasificar deudores por mora",
 "properties": {
  "tipo": "calculo",
  "plazo": "aplicación de disposiciones en punto 7.3",
  "description": "Deberán clasificar a los respectivos deudores en función de su mora, según los criterios aplicables para la cartera de consumo o vivienda y por aplicación de las disposiciones previstas en el punto 7.3"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 10.1. Proveedores no financieros de crédito."
  }
 ]
}


**Nota del punto 3:** el paso 13 es exactamente `ver_nodo(Obligacion_evaluar_capacidad_de_pago)` —
properties íntegras arriba, con `description` = "El criterio básico a ser utilizado para
efectuar la clasificación es la capacidad de pago en el futuro de la deuda o de los
compromisos objeto de la garantía de la entidad financiera" y provenance exacta
`TO_clasificacion_deudores_actual.pdf :: "Punto 4.1. Niveles de clasificación."`. Contenidos
consistentes con el apéndice del expediente (`expediente_piloto_2.md`), re-verificados acá
por re-ejecución directa.

**Nota de los cruces de la sección 2 (hecho):** ningún claim del juez post-hoc de los 5
casos coincide textualmente con las afirmaciones no soportadas del frozen ni figura en la
adjudicación firmada — las respuestas post-hoc son OTRAS respuestas (re-corrida N=1), con
claims propios. Los cruces por caso quedan en las tablas de arriba con "no figura" explícito.

---

*Fin de la verificación estructural. Sin adjudicación. A la espera de revisión.*
