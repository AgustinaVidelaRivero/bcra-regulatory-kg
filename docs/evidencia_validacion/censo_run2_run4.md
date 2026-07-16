# Censo de run_2 y run_4 — universo para la validación de v6.1-D

Fecha: 2026-07-16. SOLO LECTURA; única escritura: este archivo. No se corrió agente, juez ni
verificador. Sin commits. **Sin partición ni muestra propuesta** (decisión externa).

## 1. Criterio y fuentes

Criterio de capa 1 del protocolo del piloto (§2), aplicado a run_2 y run_4: **correctitud
FINAL modal ∈ {incorrecta, parcial}** (reporte ETAPA 2 con la adjudicación firmada propagada
— `frozen_run/reporte_final.md` §3 como override del agregado crudo, igual que en el censo
del piloto), **o completitud modal = parcial**, **o afirmaciones CENTRALES no soportadas > 0
en alguna rep** (trazas del frozen, `frozen_run/traces/run_2|run_4/`). Las unanswerable se
marcan aparte (dimensión del frozen: abstención). Conforme a la enmienda v1.1 del protocolo,
el criterio del frozen SELECCIONA el universo; el marco de adjudicación es el POST-HOC —
por eso el punto 3 releva el síntoma post-hoc de cada candidato.

**Resultado: run_2 = 11 candidatos · run_4 = 12 candidatos. Los 23 tienen traza post-hoc**
(off y on).

**Disclosure de homólogos (no exclusión):** las CQ ya usadas en alguna etapa (dev
run_1/run_5, gate run_3, piloto run_3) son {016, 017, 018, 019, 020, 024, 025, 031, 033,
034}. Candidatas SIN ningún homólogo previo: **run_2: CQ-015, CQ-021 · run_4: CQ-008,
CQ-014, CQ-021, CQ-028** — el resto comparte CQ (otro grafo, otra falla; disclosure per
protocolo §3).

## 2. Trazas post-hoc

Existen completas para ambos runs:

```
posthoc_run/traces/off/run_2: 23 archivos · on/run_2: 23
posthoc_run/traces/off/run_4: 23 archivos · on/run_4: 23
```

Todos los candidatos del punto 1 tienen traza (columna `traza_off=SI` en el barrido).
**No hace falta generar trazas** — la rama del costo de generación no aplica.

## 3. Barrido completo (comando + output)

Código: mismo mecanismo del censo del piloto (agregado del frozen + overrides FINAL del
reporte ETAPA 2 + conteos por rep de las trazas del frozen + síntoma post-hoc del juez de
`posthoc_run/traces/off/`). Output íntegro:

```

======================================================================
run_2
======================================================================
CANDIDATO CQ-015 [factual_directa] — correctitud FINAL incorrecta, centrales no sop. (max 1) | corr_agg='correcta' final='incorrecta' comp='completa' | traza_off=SI
    r1: corr='correcta' comp='completa' no_sop_c/s=1/0
    r2: corr='correcta' comp='completa' no_sop_c/s=0/0
    r3: corr='correcta' comp='completa' no_sop_c/s=1/0
CANDIDATO CQ-017 [multi_norma] — completitud parcial, centrales no sop. (max 2) · HOMÓLOGO usado en otra etapa | corr_agg='correcta' final='correcta' comp='parcial' | traza_off=SI
    r1: corr='correcta' comp='parcial' no_sop_c/s=0/4
    r2: corr='correcta' comp='parcial' no_sop_c/s=2/2
    r3: corr='correcta' comp='parcial' no_sop_c/s=0/4
CANDIDATO CQ-018 [multi_norma] — correctitud FINAL incorrecta, centrales no sop. (max 4) · HOMÓLOGO usado en otra etapa | corr_agg='incorrecta' final='incorrecta' comp='completa' | traza_off=SI
    r1: corr='incorrecta' comp='parcial' no_sop_c/s=4/0
    r2: corr='correcta' comp='completa' no_sop_c/s=4/4
    r3: corr='incorrecta' comp='completa' no_sop_c/s=3/4
CANDIDATO CQ-019 [multi_norma] — centrales no sop. (max 1) · HOMÓLOGO usado en otra etapa | corr_agg='correcta' final='correcta' comp='completa' | traza_off=SI
    r1: corr='correcta' comp='parcial' no_sop_c/s=0/0
    r2: corr='correcta' comp='completa' no_sop_c/s=1/1
    r3: corr='correcta' comp='completa' no_sop_c/s=1/0
CANDIDATO CQ-020 [multi_norma] — centrales no sop. (max 7) · HOMÓLOGO usado en otra etapa | corr_agg='correcta' final='correcta' comp='completa' | traza_off=SI
    r1: corr='correcta' comp='completa' no_sop_c/s=7/1
    r2: corr='correcta' comp='completa' no_sop_c/s=5/1
    r3: corr='correcta' comp='completa' no_sop_c/s=7/1
CANDIDATO CQ-021 [factual_directa] — completitud parcial | corr_agg='correcta' final='correcta' comp='parcial' | traza_off=SI
    r1: corr='correcta' comp='parcial' no_sop_c/s=0/0
    r2: corr='correcta' comp='parcial' no_sop_c/s=0/0
    r3: corr='correcta' comp='parcial' no_sop_c/s=0/0
CANDIDATO CQ-024 [multi_norma] — completitud parcial, centrales no sop. (max 2) · HOMÓLOGO usado en otra etapa | corr_agg='correcta' final='correcta' comp='parcial' | traza_off=SI
    r1: corr='incorrecta' comp='parcial' no_sop_c/s=0/0
    r2: corr='correcta' comp='parcial' no_sop_c/s=2/0
    r3: corr='correcta' comp='parcial' no_sop_c/s=1/0
CANDIDATO CQ-025 [factual_directa] — correctitud FINAL incorrecta · HOMÓLOGO usado en otra etapa | corr_agg='incorrecta' final='incorrecta' comp='completa' | traza_off=SI
    r1: corr='incorrecta' comp='completa' no_sop_c/s=0/1
    r2: corr='incorrecta' comp='completa' no_sop_c/s=0/1
    r3: corr='incorrecta' comp='completa' no_sop_c/s=0/1
CANDIDATO CQ-031 [cadena_restriccion_excepcion] — completitud parcial, centrales no sop. (max 6) · HOMÓLOGO usado en otra etapa | corr_agg='correcta' final='correcta' comp='parcial' | traza_off=SI
    r1: corr='correcta' comp='parcial' no_sop_c/s=3/0
    r2: corr='incorrecta' comp='parcial' no_sop_c/s=0/0
    r3: corr='correcta' comp='parcial' no_sop_c/s=6/0
CANDIDATO CQ-033 [cadena_restriccion_excepcion] — correctitud FINAL incorrecta, completitud parcial, centrales no sop. (max 3) · HOMÓLOGO usado en otra etapa | corr_agg='correcta' final='incorrecta' comp='parcial' | traza_off=SI
    r1: corr='correcta' comp='parcial' no_sop_c/s=3/1
    r2: corr='correcta' comp='parcial' no_sop_c/s=0/3
    r3: corr='incorrecta' comp='completa' no_sop_c/s=3/0
CANDIDATO CQ-034 [cadena_restriccion_excepcion] — completitud parcial · HOMÓLOGO usado en otra etapa | corr_agg='correcta' final='correcta' comp='parcial' | traza_off=SI
    r1: corr='correcta' comp='parcial' no_sop_c/s=0/0
    r2: corr='correcta' comp='parcial' no_sop_c/s=0/0
    r3: corr='correcta' comp='parcial' no_sop_c/s=0/0
[unanswerable] CQ-036: abstencion_modal='correcta' | centrales_max=0 | r1: corr=None comp=None no_sop_c/s=0/2 | r2: corr=None comp=None no_sop_c/s=0/2 | r3: corr=None comp=None no_sop_c/s=0/3
[unanswerable] CQ-037: abstencion_modal='correcta' | centrales_max=2 | r1: corr=None comp=None no_sop_c/s=2/1 | r2: corr=None comp=None no_sop_c/s=1/2 | r3: corr=None comp=None no_sop_c/s=1/2
[unanswerable] CQ-038: abstencion_modal='correcta' | centrales_max=2 | r1: corr=None comp=None no_sop_c/s=1/1 | r2: corr=None comp=None no_sop_c/s=2/2 | r3: corr=None comp=None no_sop_c/s=0/2
[unanswerable] CQ-039: abstencion_modal='correcta' | centrales_max=0 | r1: corr=None comp=None no_sop_c/s=0/0 | r2: corr=None comp=None no_sop_c/s=0/0 | r3: corr=None comp=None no_sop_c/s=0/0

run_2: 11 candidatos: ['CQ-015', 'CQ-017', 'CQ-018', 'CQ-019', 'CQ-020', 'CQ-021', 'CQ-024', 'CQ-025', 'CQ-031', 'CQ-033', 'CQ-034']

--- síntoma POST-HOC (off/run_2) de los candidatos ---
CQ-015: corr='correcta' comp='completa' no_sop_c/s=0/0 | claims_reprobados=0 (centrales=0) | patas_no_cubiertas=0
CQ-017: corr='correcta' comp='parcial' no_sop_c/s=0/2 | claims_reprobados=2 (centrales=0) | patas_no_cubiertas=1
    [no_soportado] "Las obligaciones de protección de usuarios incluyen considerar y resolver fundadamente reclamos de usuarios."
    [no_soportado] "Los operadores de cambio están bajo supervisión del BCRA en materia de protección de usuarios."
    [pata no_cubierta] "Si el operador de cambio debe intervenir como entidad autorizada en el mercado de cambios"
CQ-018: corr='incorrecta' comp='parcial' no_sop_c/s=5/2 | claims_reprobados=8 (centrales=6) | patas_no_cubiertas=1
    [no_soportado/central] "Los proveedores no financieros de crédito deben considerar y resolver fundadamente reclamos de usuarios."
    [no_soportado/central] "Las empresas no financieras emisoras de tarjetas de crédito deben resolver reclamos de usuarios."
    [no_soportado] "Las empresas no financieras emisoras de tarjetas de crédito deben entregar información sobre productos y servicios."
    [no_soportado] "Las empresas no financieras emisoras de tarjetas de crédito deben publicar contratos."
    [falso/central] "El criterio básico de clasificación de deudores es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía, medida a través del análisis de flujo de fondos."
    [no_soportado/central] "Los criterios objetivos de clasificación de deudores incluyen el término de morosidad."
    [no_soportado/central] "Los criterios objetivos de clasificación de deudores incluyen la situación jurídica del cliente o sus deudas."
    [no_soportado/central] "Los criterios objetivos de clasificación de deudores incluyen el cumplimiento de refinanciaciones."
    [pata no_cubierta] "Si las empresas no financieras emisoras de tarjetas deben clasificar a sus deudores"
CQ-019: corr='correcta' comp='parcial' no_sop_c/s=0/0 | claims_reprobados=0 (centrales=0) | patas_no_cubiertas=2
    [pata no_cubierta] "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito"
    [pata no_cubierta] "Cómo se vincula esa regla con la clasificación de deudores"
CQ-020: corr='correcta' comp='completa' no_sop_c/s=5/1 | claims_reprobados=6 (centrales=5) | patas_no_cubiertas=0
    [no_soportado/central] "El factor de calificación K varía de 1 a 1,19 según la calificación asignada a la entidad por la SEFYC."
    [no_soportado/central] "En ausencia de comunicación de calificación por parte de la SEFYC, el valor de K es 1,03."
    [no_soportado/central] "La fórmula de CRC utiliza un multiplicador de 12,5 en el cálculo de APRC."
    [no_soportado/central] "El reporte se realiza a través del Régimen Informativo Contable Mensual (R.I.-C.M.)."
    [no_soportado] "El R.I.-C.M. es el procedimiento de información mensual sobre exigencia e integración de capitales mínimos."
    [no_soportado/central] "La información se reporta al último día de cada período mensual."
CQ-021: corr='correcta' comp='parcial' no_sop_c/s=0/0 | claims_reprobados=0 (centrales=0) | patas_no_cubiertas=2
    [pata no_cubierta] "Casos en que es optativo para la entidad comunicar al deudor un cambio negativo en su clasificación"
    [pata no_cubierta] "Régimen del que depende el umbral para dicha opcionalidad"
CQ-024: corr='correcta' comp='parcial' no_sop_c/s=0/2 | claims_reprobados=2 (centrales=0) | patas_no_cubiertas=1
    [no_soportado] "Existen obligaciones de reclasificación inmediata en casos de atrasos mayores a 31 días en deuda refinanciada."
    [no_soportado] "Existen obligaciones de reclasificación inmediata en casos de atrasos mayores a 540 días en deudores en concurso."
    [pata no_cubierta] "Casos en que la reevaluación de dicho deudor debe ser inmediata"
CQ-025: corr='incorrecta' comp='completa' no_sop_c/s=0/1 | claims_reprobados=2 (centrales=1) | patas_no_cubiertas=0
    [falso/central] "En el Régimen Informativo de Capitales Mínimos, la exigencia por riesgo de mercado se informa con frecuencia mensual."
    [no_soportado] "La exigencia por riesgo de mercado corresponde a las posiciones del último día del mes."
CQ-031: corr='incorrecta' comp='parcial' no_sop_c/s=0/0 | claims_reprobados=3 (centrales=3) | patas_no_cubiertas=2
    [falso/central] "Los deudores que resulten de operaciones de cesión sin responsabilidad para el cedente no serán objeto de clasificación."
    [falso/central] "No será obligatoria la evaluación de capacidad de pago en función de ingresos cuando se utilicen métodos específicos de evaluación."
    [falso/central] "No será obligatoria la evaluación de capacidad de pago en función de ingresos cuando se trate de deudores por préstamos de monto reducido."
    [pata no_cubierta] "Qué deudores no deben ser objeto de clasificación"
    [pata no_cubierta] "Respecto de qué deudores no corresponde evaluar la capacidad de repago"
CQ-033: corr='correcta' comp='parcial' no_sop_c/s=0/3 | claims_reprobados=3 (centrales=0) | patas_no_cubiertas=2
    [no_soportado] "El límite de capital por riesgo operacional para entidades del Grupo C es 14%."
    [no_soportado] "El límite del Grupo C puede reducirse a 8% si la calificación SEFYC es 1, 2 o 3."
    [no_soportado] "El límite del Grupo C puede reducirse a 5% si la calificación SEFYC es 1 o 2 en todos los aspectos."
    [pata no_cubierta] "Límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2"
    [pata no_cubierta] "Condiciones bajo las cuales ese límite se reduce"
CQ-034: corr='incorrecta' comp='parcial' no_sop_c/s=0/1 | claims_reprobados=2 (centrales=1) | patas_no_cubiertas=2
    [falso/central] "Para una persona humana residente que compra moneda extranjera para atesorar con débito en cuenta de entidades financieras locales, el límite mensual es USD 200."
    [no_soportado] "El límite de USD 200 mensual aplica en el conjunto de las entidades y conceptos señalados para compra de divisas por personas humanas residentes."
    [pata no_cubierta] "Límite mensual para compra de moneda extranjera para atesorar con débito en cuenta"
    [pata no_cubierta] "Límite general para otras modalidades de formación de activos externos"

======================================================================
run_4
======================================================================
CANDIDATO CQ-008 [factual_directa] — completitud parcial | corr_agg='correcta' final='correcta' comp='parcial' | traza_off=SI
    r1: corr='correcta' comp='parcial' no_sop_c/s=0/0
    r2: corr='correcta' comp='parcial' no_sop_c/s=0/0
    r3: corr='correcta' comp='parcial' no_sop_c/s=0/0
CANDIDATO CQ-014 [factual_directa] — centrales no sop. (max 2) | corr_agg='correcta' final='correcta' comp='completa' | traza_off=SI
    r1: corr='incorrecta' comp='parcial' no_sop_c/s=2/0
    r2: corr='correcta' comp='completa' no_sop_c/s=0/0
    r3: corr='correcta' comp='completa' no_sop_c/s=0/0
CANDIDATO CQ-017 [multi_norma] — correctitud FINAL parcial, completitud parcial, centrales no sop. (max 2) · HOMÓLOGO usado en otra etapa | corr_agg='correcta' final='parcial' comp='parcial' | traza_off=SI
    r1: corr='correcta' comp='parcial' no_sop_c/s=1/4
    r2: corr='correcta' comp='parcial' no_sop_c/s=0/5
    r3: corr='correcta' comp='parcial' no_sop_c/s=2/2
CANDIDATO CQ-018 [multi_norma] — centrales no sop. (max 3) · HOMÓLOGO usado en otra etapa | corr_agg='correcta' final='correcta' comp='completa' | traza_off=SI
    r1: corr='incorrecta' comp='completa' no_sop_c/s=0/1
    r2: corr='correcta' comp='completa' no_sop_c/s=1/5
    r3: corr='correcta' comp='completa' no_sop_c/s=3/2
CANDIDATO CQ-019 [multi_norma] — correctitud FINAL incorrecta, completitud parcial, centrales no sop. (max 4) · HOMÓLOGO usado en otra etapa | corr_agg='incorrecta' final='incorrecta' comp='parcial' | traza_off=SI
    r1: corr='incorrecta' comp='completa' no_sop_c/s=4/1
    r2: corr='incorrecta' comp='parcial' no_sop_c/s=2/3
    r3: corr='incorrecta' comp='parcial' no_sop_c/s=2/1
CANDIDATO CQ-020 [multi_norma] — centrales no sop. (max 4) · HOMÓLOGO usado en otra etapa | corr_agg='correcta' final='correcta' comp='completa' | traza_off=SI
    r1: corr='correcta' comp='completa' no_sop_c/s=0/4
    r2: corr='correcta' comp='completa' no_sop_c/s=4/2
    r3: corr='correcta' comp='completa' no_sop_c/s=0/0
CANDIDATO CQ-021 [factual_directa] — completitud parcial | corr_agg='correcta' final='correcta' comp='parcial' | traza_off=SI
    r1: corr='correcta' comp='parcial' no_sop_c/s=0/1
    r2: corr='correcta' comp='parcial' no_sop_c/s=0/1
    r3: corr='correcta' comp='parcial' no_sop_c/s=0/1
CANDIDATO CQ-024 [multi_norma] — completitud parcial · HOMÓLOGO usado en otra etapa | corr_agg='correcta' final='correcta' comp='parcial' | traza_off=SI
    r1: corr='correcta' comp='parcial' no_sop_c/s=0/1
    r2: corr='incorrecta' comp='parcial' no_sop_c/s=0/1
    r3: corr='correcta' comp='parcial' no_sop_c/s=0/1
CANDIDATO CQ-028 [cadena_restriccion_excepcion] — correctitud FINAL incorrecta | corr_agg='incorrecta' final='incorrecta' comp='completa' | traza_off=SI
    r1: corr='incorrecta' comp='completa' no_sop_c/s=0/1
    r2: corr='incorrecta' comp='completa' no_sop_c/s=0/1
    r3: corr='incorrecta' comp='completa' no_sop_c/s=0/1
CANDIDATO CQ-031 [cadena_restriccion_excepcion] — completitud parcial · HOMÓLOGO usado en otra etapa | corr_agg='correcta' final='correcta' comp='parcial' | traza_off=SI
    r1: corr='correcta' comp='parcial' no_sop_c/s=0/2
    r2: corr='incorrecta' comp='parcial' no_sop_c/s=0/0
    r3: corr='correcta' comp='parcial' no_sop_c/s=0/1
CANDIDATO CQ-033 [cadena_restriccion_excepcion] — completitud parcial, centrales no sop. (max 3) · HOMÓLOGO usado en otra etapa | corr_agg='correcta' final='correcta' comp='parcial' | traza_off=SI
    r1: corr='correcta' comp='parcial' no_sop_c/s=0/0
    r2: corr='incorrecta' comp='parcial' no_sop_c/s=3/2
    r3: corr='correcta' comp='parcial' no_sop_c/s=2/3
CANDIDATO CQ-034 [cadena_restriccion_excepcion] — correctitud FINAL incorrecta, completitud parcial · HOMÓLOGO usado en otra etapa | corr_agg='incorrecta' final='incorrecta' comp='parcial' | traza_off=SI
    r1: corr='incorrecta' comp='parcial' no_sop_c/s=0/0
    r2: corr='incorrecta' comp='parcial' no_sop_c/s=0/0
    r3: corr='incorrecta' comp='parcial' no_sop_c/s=0/0
[unanswerable] CQ-036: abstencion_modal='correcta' | centrales_max=0 | r1: corr=None comp=None no_sop_c/s=0/0 | r2: corr=None comp=None no_sop_c/s=0/0 | r3: corr=None comp=None no_sop_c/s=0/0
[unanswerable] CQ-037: abstencion_modal='correcta' | centrales_max=0 | r1: corr=None comp=None no_sop_c/s=0/2 | r2: corr=None comp=None no_sop_c/s=0/2 | r3: corr=None comp=None no_sop_c/s=0/2
[unanswerable] CQ-038: abstencion_modal='correcta' | centrales_max=0 | r1: corr=None comp=None no_sop_c/s=0/1 | r2: corr=None comp=None no_sop_c/s=0/4 | r3: corr=None comp=None no_sop_c/s=0/3
[unanswerable] CQ-039: abstencion_modal='correcta' | centrales_max=0 | r1: corr=None comp=None no_sop_c/s=0/0 | r2: corr=None comp=None no_sop_c/s=0/0 | r3: corr=None comp=None no_sop_c/s=0/1

run_4: 12 candidatos: ['CQ-008', 'CQ-014', 'CQ-017', 'CQ-018', 'CQ-019', 'CQ-020', 'CQ-021', 'CQ-024', 'CQ-028', 'CQ-031', 'CQ-033', 'CQ-034']

--- síntoma POST-HOC (off/run_4) de los candidatos ---
CQ-008: corr='correcta' comp='parcial' no_sop_c/s=0/0 | claims_reprobados=0 (centrales=0) | patas_no_cubiertas=1
    [pata no_cubierta] "Plazo en que la entidad financiera debe comunicar al cliente la última clasificación que le asignó, cuando el cliente lo solicita"
CQ-014: corr='correcta' comp='completa' no_sop_c/s=0/0 | claims_reprobados=0 (centrales=0) | patas_no_cubiertas=0
CQ-017: corr='correcta' comp='parcial' no_sop_c/s=0/2 | claims_reprobados=2 (centrales=0) | patas_no_cubiertas=1
    [no_soportado] "El mercado libre de cambios está definido como aquel por el cual se cursan operaciones realizadas por entidades financieras y demás personas autorizadas por el BCRA para dedicarse al comercio de compra y venta de monedas extranjeras."
    [no_soportado] "Existe una categoría de 'personas jurídicas no autorizadas a operar en cambios' que requieren conformidad previa del BCRA para acceder al mercado de cambios."
    [pata no_cubierta] "¿Un operador de cambio debe intervenir como entidad autorizada en el mercado de cambios?"
CQ-018: corr='correcta' comp='completa' no_sop_c/s=3/3 | claims_reprobados=6 (centrales=3) | patas_no_cubiertas=0
    [no_soportado] "La clasificación debe efectuarse considerando la totalidad de las financiaciones comprendidas."
    [no_soportado] "La clasificación debe realizarse con una periodicidad que atienda a la importancia del deudor."
    [no_soportado] "La clasificación debe documentarse el análisis efectuado."
    [no_soportado/central] "La categoría 'Situación normal' corresponde a clientes que atienden puntualmente el pago de sus obligaciones o con atrasos que no superan los 31 días."
    [no_soportado/central] "La categoría 'Clasificación con alto riesgo de insolvencia' corresponde a deudores cuyo análisis de flujo de fondos demuestra que es altamente improbable que puedan atender la totalidad de sus compromisos financieros."
    [no_soportado/central] "La categoría 'Clasificación irrecuperable' corresponde a deudas consideradas incobrables, donde la incobrabilidad es evidente al momento del análisis."
CQ-019: corr='incorrecta' comp='completa' no_sop_c/s=1/3 | claims_reprobados=7 (centrales=4) | patas_no_cubiertas=0
    [falso/central] "La previsión específica es la que no se deduce al computar los activos para la exigencia de capital por riesgo de crédito."
    [falso/central] "El cálculo de la exigencia de capital por riesgo de crédito debe efectuarse sobre el monto bruto de la exposición."
    [no_soportado] "La clasificación de deudores debe efectuarse considerando la totalidad de las financiaciones comprendidas."
    [no_soportado] "La clasificación de deudores determina la categoría en que se incluye cada deudor, siendo cinco las categorías de riesgo."
    [no_soportado] "La categoría de clasificación es criterio objetivo para modificar aspectos como el término de morosidad, la situación jurídica del cliente y la refinanciación."
    [no_soportado/central] "Las previsiones mínimas por riesgo de incobrabilidad se determinan en función de la categoría de clasificación asignada a cada deudor."
    [falso/central] "La previsión específica contable no se deduce del cálculo de capital (KSA)."
CQ-020: corr='correcta' comp='parcial' no_sop_c/s=3/1 | claims_reprobados=4 (centrales=3) | patas_no_cubiertas=1
    [no_soportado/central] "k está vinculado a la calificación asignada por la SEFYC"
    [no_soportado/central] "k toma valores entre 1 y 1,19"
    [no_soportado/central] "Los APRC se determinan mediante la suma de valores obtenidos aplicando ponderadores de riesgo a activos computables"
    [no_soportado] "Las entidades deben reportar información de capital en el régimen informativo contable mensual del BCRA"
    [pata no_cubierta] "Con qué frecuencia se reporta la CRC al BCRA"
CQ-021: corr='correcta' comp='parcial' no_sop_c/s=0/1 | claims_reprobados=1 (centrales=0) | patas_no_cubiertas=2
    [no_soportado] "La comunicación del cambio negativo en la clasificación debe realizarse mediante medios especificados por la regulación del BCRA"
    [pata no_cubierta] "Casos en que es optativo para la entidad comunicar al deudor un cambio negativo en su clasificación"
    [pata no_cubierta] "Régimen del que depende el umbral para determinar esa opcionalidad"
CQ-024: corr='correcta' comp='parcial' no_sop_c/s=0/0 | claims_reprobados=0 (centrales=0) | patas_no_cubiertas=2
    [pata no_cubierta] "Periodicidad mínima de clasificación de un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC"
    [pata no_cubierta] "Casos en que la reevaluación de dicho deudor debe ser inmediata"
CQ-028: corr='incorrecta' comp='completa' no_sop_c/s=0/1 | claims_reprobados=2 (centrales=1) | patas_no_cubiertas=0
    [falso/central] "El criterio para no admitir la comisión por precancelación total es el que ocurra primero entre la cuarta parte del plazo original y los 180 días."
    [no_soportado] "La comisión por precancelación parcial se permite sin la restricción temporal mencionada."
CQ-031: corr='correcta' comp='parcial' no_sop_c/s=0/2 | claims_reprobados=2 (centrales=0) | patas_no_cubiertas=2
    [no_soportado] "La documentación disponible establece que los deudores deben ser objeto de análisis de situación económica y financiera."
    [no_soportado] "La documentación disponible establece que los deudores deben ser objeto de clasificación periódica."
    [pata no_cubierta] "Qué deudores no deben ser objeto de clasificación"
    [pata no_cubierta] "Respecto de qué deudores no corresponde evaluar la capacidad de repago"
CQ-033: corr='parcial' comp='parcial' no_sop_c/s=0/1 | claims_reprobados=2 (centrales=0) | patas_no_cubiertas=1
    [falso] "Las entidades del Grupo 2 Grupo B tienen un límite máximo del 17% hasta el 30/06/26."
    [no_soportado] "Las entidades del Grupo 2 Grupo C tienen un límite máximo del 14% hasta el 30/06/26."
    [pata no_cubierta] "Bajo qué condiciones ese límite se reduce"
CQ-034: corr='incorrecta' comp='parcial' no_sop_c/s=0/0 | claims_reprobados=1 (centrales=1) | patas_no_cubiertas=1
    [falso/central] "Para otras modalidades de formación de activos externos (incluyendo débito en cuenta), aplica un límite mensual de USD 200 por mes calendario."
    [pata no_cubierta] "Límite mensual aplicable cuando la compra de moneda extranjera para atesorar se cursa con débito en cuenta"
```

## 4. Presupuesto por escenario

Base: la consigna del protocolo usa **~1,2M de input por caso verificado con N=3**
(estimación conservadora); el **promedio medido del piloto** fue **836K por caso**
(4.179.672 / 5; rango 394K-1.439K). Se tabulan ambos. Generación de trazas: **no aplica**
(todas existen).

| Escenario | Casos | Input @1,2M/caso | Input @836K/caso (medido) |
|---|---|---|---|
| Todos los elegibles (ambos runs) | 23 | ~27,6M | ~19,2M |
| Solo run_2 | 11 | ~13,2M | ~9,2M |
| Solo run_4 | 12 | ~14,4M | ~10,0M |
| Mitad de run_2 | 5-6 | ~6,0-7,2M | ~4,2-5,0M |
| Mitad de run_4 | 6 | ~7,2M | ~5,0M |
| Mitad del total | 11-12 | ~13,2-14,4M | ~9,2-10,0M |

## 5. Tabla final

| Run | Candidatos (criterio frozen) | Con traza / sin traza | Síntoma post-hoc disponible | Detalle notable del síntoma post-hoc |
|---|---|---|---|---|
| run_2 | **11** — CQ-015, 017, 018, 019, 020, 021, 024, 025, 031, 033, 034 | 11 / 0 | sí (relevado arriba, §3) | CQ-015 post-hoc SANO (correcta/completa, 0 reprobados — falla del frozen no reproducida); CQ-018 con 6 centrales reprobados; CQ-031 y CQ-034 con centrales `falso`; CQ-019/021/024 solo patas no cubiertas |
| run_4 | **12** — CQ-008, 014, 017, 018, 019, 020, 021, 024, 028, 031, 033, 034 | 12 / 0 | sí (§3) | CQ-014 post-hoc SANO (falla no reproducida); CQ-019 con 4 centrales reprobados (2 `falso`); CQ-034 con central `falso`; CQ-008/024 solo patas no cubiertas |
| **Total** | **23** | **23 / 0** | — | 2 candidatos con síntoma post-hoc vacío (candidatos naturales a control negativo, si la partición externa lo decide) |

Unanswerables (aparte, ambas runs): abstención modal correcta 4/4 en run_2 y run_4; en
run_2 CQ-037/038 tienen centrales no soportadas en trazas (2 máx.) — mismas exclusiones
documentadas del protocolo (sin categoría taxonómica para irrespondibles).

Presupuesto por escenario: §4. **La partición/muestra es decisión externa** — este censo no
la propone.

---

*Fin del censo. A la espera de revisión.*
