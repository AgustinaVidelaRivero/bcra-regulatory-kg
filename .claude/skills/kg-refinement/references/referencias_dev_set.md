# Referencias de calibración del DEV SET — iteración del verificador v5

**Qué es.** Las adjudicaciones humanas de referencia del **dev set** para iterar el prompt del verificador v5 (el *loop chico*): 5 fallas de `run_1`/`run_5` con GT en taxonomía v2 (pares `{sintoma_capa1, causa_capa2}`), contra las cuales se compara el output del verificador en cada iteración del prompt.

**Relación con `casos_control.md`.** Los 5 casos-control de `run_3` son el **GATE FINAL pre-registrado**: se corren una sola vez, al final, para validar la versión candidata. Este dev set de `run_1`/`run_5` es el **banco de iteración**: acá se prueba, se falla y se ajusta cuantas veces haga falta. Esa separación resuelve la tensión loop-chico vs anti-overfitting: iterar contra el dev set no contamina el gate, y el gate no se gasta iterando.

**Fecha y procedencia.** Adjudicación de la autora, **2026-07-13, asistida por revisión**, sobre la evidencia cruda de `posthoc_run/dev_set/hoja_adjudicacion.md` — dossieres **ciegos a las etiquetas del pilot** (pregunta + patas del juez + claims negativos + trayectoria + nodos íntegros + pasajes GT del PDF). Las verificaciones de PDF citadas provienen de la sesión de revisión (barridos programáticos sobre todos los campos de los kg.json congelados + re-ejecución determinística de las búsquedas del agente con `harness.GraphIndex` + `pdf_locate` sobre el subset).

---

## Reglas de uso (explícitas)

1. **Los ejemplos resueltos del prompt del verificador NUNCA salen de estos 5 casos** (fuga dev→prompt). Si un caso de acá aparece en el prompt, el dev set deja de medir.
2. **El verificador nunca ve estas referencias.** Se compara su output contra ellas **externamente** (el comparador es quien lee este archivo, no el agente verificador).
3. **Criterio de acierto: igual que `casos_control.md`** — todas las **primarias** correctas como par `{sintoma, causa}`; las secundarias y los falsos positivos del juez **suman pero no son obligatorios**, y se registran como señal secundaria.
4. **Los 5 casos-control de run_3 NO se corren durante la iteración.** Solo al final, como gate.

---

## Caso off/run_5/CQ-017

**Pregunta:** Un operador de cambio, ¿está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros y debe intervenir como entidad autorizada en el mercado de cambios?

Adjudicación de la autora, 2026-07-13, asistida por revisión:

- **Pata 2** ("debe intervenir como entidad autorizada") — **`{context_recall, alcanzabilidad_kg}` PRIMARIA.** Evidencia: los portadores de la regla de Exterior 1.1 existen (`intervencion_de_entidades_autorizadas_en_operaciones_de_camb`, `entidades_financieras_o_cambiarias_autorizadas__agencia_cambio`, `entidades_autorizadas_a_operar_en_cambios__otra`) pero ninguno apareció en las búsquedas del agente (pasos 3/12/15, re-ejecutados determinísticamente); por la regla de precedencia, el nodo entidad_operadora usado para rellenar no cuenta como contexto de la pata.
- **Pata 2 — claim central** "Los operadores de cambio son entidades financieras autorizadas a operar en el mercado de cambios" — **`{faithfulness, alucinacion_agente}` (modo b) SECUNDARIA.** Evidencia: ningún nodo consultado ni el PDF lo afirman (Exterior 1.1: "financieras **o cambiarias**"). Atenuante documentado: el grafo aportó ingredientes (type EntidadFinanciera del nodo operador_de_cambio__agencia_cambio; nodo entidad_operadora defectuoso).
- **Pata 2 — claim** "Existen entidades denominadas 'entidades operadoras en mercado de cambios' que son entidades financieras autorizadas..." — **`{noise_sensitivity, contenido_kg}` SECUNDARIA.** Evidencia: soportado por `entidad_operadora_en_mercado_de_cambios__otra`, cuyo contenido omite "o cambiarias" (contra Exterior 1.1) y cuya provenance (Punto 3.16) no funda el contenido (verificado: el 3.16 es requisitos de egresos/ARCA).
- **Pata 1 — claim de la enumeración de sujetos obligados** — **FALSO POSITIVO DEL JUEZ, sin par** (la pata 1 no tiene defecto en su núcleo). Evidencia: soportado por el nodo `sujeto_obligado` (abierto en el paso 13) y correcto contra Protección 1.1.2.x.
- **Pata 1 — las 4 glosas de obligaciones** (información clara, trato equitativo, acceso igualitario, resolución de reclamos) — **`{faithfulness, alucinacion_agente}` (modo a) SECUNDARIA.** Evidencia: sin soporte en los nodos abiertos por el agente; el grafo las porta en nodos alcanzables por label (`trato_equitativo_y_digno`, `derecho_a_informacion_clara_y_suficiente`, `acceso_igualitario_a_servicios_financieros`, `consideracion_y_resolucion_fundada_de_reclamos`) que el agente no consultó — exhibibles.

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion.md` (scratch, no versionado).

---

## Caso off/run_1/CQ-020

**Pregunta:** ¿Cómo se calcula la exigencia de capital por riesgo de crédito (CRC) y con qué frecuencia se reporta al BCRA?

Adjudicación de la autora, 2026-07-13, asistida por revisión:

- **Pata 1 (cálculo) — claim central** "INC es el Incremento de exigencia por riesgo de crédito por excesos en participaciones en capital de empresas" — **`{noise_sensitivity, contenido_kg}` PRIMARIA.** Evidencia: el claim reproduce casi verbatim el label del nodo `req_incremento_de_exigencia_por_riesgo_de_credito_por_excesos_en_participaciones_en_capital_de_empresas_inc`, visible en los resultados del paso 1 (re-ejecutado determinísticamente: 5º resultado); ese label conflata INC(inversiones significativas, límites 15%/60% dentro de APRC) con el INC de la fórmula CRC (excesos en activos inmovilizados etc., Capitales 2.1) — soporte infiel al PDF.
- **Los otros 7 claims negativos** (k escala 1-1,19; k asignado por SEFyC; APRC suma con ponderadores; reporte vía R.I.-C.M.; y las 3 secundarias del R.I.-C.M.) — **FALSOS POSITIVOS DEL JUEZ, sin par.** Evidencia: soportados por los nodos abiertos (`req_factor_k`, `con_activos_ponderados_por_riesgo_de_credito_aprc`, `ins_regimen_informativo_contable_mensual`, `rep_regimen_informativo_contable_mensual_sobre_capitales_minimos`) y correctos contra el PDF (Capitales 2.1: escala k 1/1,03/1,08/1,13/1,19, calificación SEFYC, expresión de APRC; Régimen 1.1: frecuencia mensual por defecto).
- **Pata 2 (frecuencia)** — "mensual vía R.I.-C.M." — **sin defecto.** Evidencia: soportado por `ins_regimen_informativo_contable_mensual` (abierto en el paso 9) y correcto contra Régimen 1.1 (la exigencia por riesgo de crédito no está en las excepciones trimestrales).

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion.md` (scratch, no versionado).

---

## Caso on/run_1/CQ-019

**Pregunta:** Al computar los activos para la exigencia de capital por riesgo de crédito, ¿qué previsión por incobrabilidad no se deduce, y cómo se vincula esa regla con la clasificación de deudores?

Adjudicación de la autora, 2026-07-13, asistida por revisión:

- **Claim** "La previsión por riesgo de incobrabilidad sí se deduce para activos cubiertos con garantías preferidas A" [falso] — **`{noise_sensitivity, contenido_kg}` PRIMARIA.** Evidencia: soportado por `req_prevision_por_riesgo_de_incobrabilidad` ("Deducción por deterioro de activos... situación normal o cubiertos con garantías preferidas A"), cuyo contenido invierte el PDF (Capitales 2.3.1: "sin deducir el 100%... 'en situación normal'... y a las financiaciones que se encuentran cubiertas con garantías preferidas A" — ambas categorías son no-deducibles). Nota: ningún claim central falló; la primaria del caso descansa en la única secundaria [falso], decisión de la autora.
- **Claim** "La categoría 'situación normal' corresponde a clientes que demuestran capacidad de atender adecuadamente todos sus compromisos financieros" [no_soportado] — **`{faithfulness, alucinacion_agente}` (modo a) SECUNDARIA.** Evidencia: sin soporte en los nodos abiertos por el agente; el grafo SÍ porta la definición en un nodo exhibible y alcanzable por label — `cla_situacion_normal_clasificacion_de_deudores` ("Categoría de clasificación de deudores donde el cliente demuestra capacidad de atender adecuadamente todos sus compromisos financieros a través del análisis de flujo de fondos") — que el agente no consultó (barrido del 2026-07-13 como constancia).
- **Claim** "La provisión específica para cartera clasificada como situación normal debe absorberse antes de la deducción de otros conceptos deducibles del capital" [no_soportado] — **FALSO POSITIVO DEL JUEZ, sin par.** Evidencia: soportado casi verbatim por `req_prevision_por_riesgo_de_incobrabilidad_en_cartera_en_situacion_normal` (abierto por el agente en el paso 10) y correcto contra el PDF (Capitales, punto 8.4.1.1 —conceptos deducibles del COn1—: "Previo a su deducción deberá absorberse el importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera en 'situación normal' computado como patrimonio neto complementario (punto 8.2.3.3.).").

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion.md` (scratch, no versionado).

---

## Caso off/run_1/CQ-024

**Pregunta:** ¿Con qué periodicidad mínima debe clasificarse un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC, y en qué casos la reevaluación debe ser inmediata?

Adjudicación de la autora, 2026-07-13, asistida por revisión:

- **Pata 2 — claims** "La reevaluación debe ser inmediata cuando se producen atrasos mayores a 31 días" [no_soportado] y "Los atrasos mayores a 31 días generan reclasificación inmediata del deudor al nivel resultante de sumar días de atraso efectivo y atraso normativo" [no_soportado] — **`{noise_sensitivity, contenido_kg}` PRIMARIA.** Evidencia: soportados por `req_atrasos_mayores_a_31_dias` (abierto por el agente en el paso 15), cuyo contenido no existe en el TO — "atraso efectivo", "atraso normativo" y la fórmula de suma dan 0 matches en el documento completo; la regla real es la recategorización por atrasos >31 días en obligaciones REFINANCIADAS (6.5.x), sin fórmula de suma y sin alcance general — nodo con regla deformada/des-scopeada.
- **Pata 2 — claim** "La reevaluación debe ser inmediata cuando existe discrepancia de más de un nivel en clasificaciones y las financiaciones superan el 1% de la RPC" [falso] — **FALSO POSITIVO DEL JUEZ, sin par.** Evidencia: soportado por `req_reevaluacion_inmediata_por_discrepancia_de_mas_de_un_nivel_en_clasificaciones` (abierto en el paso 4) y correcto contra el PDF (Clasificación 6.4.4 + último párrafo del 6.4: "La reevaluación deberá ser inmediata cuando... igualen o superen el 1% de la responsabilidad patrimonial computable...") — condensado pero sustancialmente correcto.
- **Pata 1 (periodicidad mínima)** — "trimestral" — **sin defecto.** Evidencia: soportado por `req_analisis_trimestral_de_clientes_con_financiaciones_que_alcanzan_el_5_o_mas_de_la_responsabilidad_patrimonial_computable` (abierto en el paso 7) y correcto contra el Punto 6.3.1.

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion.md` (scratch, no versionado).

---

## Caso off/run_1/CQ-031

**Pregunta:** ¿Qué deudores no deben ser objeto de clasificación y respecto de qué deudores no corresponde evaluar la capacidad de repago?

Adjudicación de la autora, 2026-07-13, asistida por revisión:

- **Pata 1** ("qué deudores no deben ser objeto de clasificación") — **UNA PRIMARIA + UNA SECUNDARIA** (re-adjudicada por la autora, 2026-07-14):
  - **`{context_recall, alcanzabilidad_kg}` PRIMARIA — ítem 4.5:** el portador `rsj_deudor_con_garantias_preferidas_a` existe, fiel, pero es inalcanzable **ex ante**: label sin vocabulario de la pregunta; no apareció en las 8 buscar_nodos de la traza (outputs completos, re-ejecutados) y "garantías" no fue expuesto al agente por ningún output de los pasos 1–14. Aplica la prueba de alcanzabilidad ex ante de `taxonomia.md` v2.1.
  - **`{context_recall, navegación}` SECUNDARIA — ítem 4.6:** el edge `ope_clasificacion_de_deudores --no_está_sujeta_a--> ope_creditos_cedidos_sin_responsabilidad_para_el_cedente` (prov. p.15) fue **visible en runtime** en el output completo del paso 15 (`harness.py` pasa outputs completos al agente y almacena truncados en la traza) y no fue explotado.
  - **Nota de re-adjudicación (autora, 2026-07-14):** la jerarquía del ítem 4.6 se corrige (primaria → secundaria) por el **contrafáctico empírico de run_3/CQ-031** — el agente de run_3 respondió la pata 1 únicamente con la cesión del 4.6 y el juez la reprobó igual (claim central `no_soportado`; cita al 4.6 marcada `falso`), demostrando que el 4.6 solo NO mueve el veredicto: lo decisivo es el 4.5 (la `cita_textual` del GT). El desacuerdo surgió en la iteración 2 del verificador v5.1; la corrección se funda en el contrafáctico, no en el output del instrumento. (Historia del GT: 2026-07-13 primaria única `alcanzabilidad_kg`; 2026-07-14 AM mixta con dos primarias, motivada por la iteración 1 y el micro-hecho del paso 15 — los `ver_vecinos` completos de los pasos 5 y 6 no exponen ningún portador; 2026-07-14 esta corrección de jerarquía.)
- **Pata 2** ("respecto de qué deudores no corresponde evaluar la capacidad de repago") — **`{context_recall, alcanzabilidad_kg}` PRIMARIA.** Evidencia: el dato GT (4.4) nunca apareció en la trayectoria; los portadores `cla_garantias_preferidas_a` y `cla_financiaciones_con_garantias_preferidas_a` son alcanzables solo por vocabulario propio ("garantías preferidas"), no por los términos de la pregunta.
- **Los 2 claims de "monto reducido" marcados falso por el juez** — **FALSOS POSITIVOS DEL JUEZ, sin par** (no es defecto del sistema). Evidencia: claim 1 soportado por `cla_deudores_por_prestamos_de_monto_reducido` y correcto contra el PDF (TO Clasificación, Sección 7: "No será obligatoria la evaluación de la capacidad de pago en función de los ingresos [...] préstamos de monto reducido"); claim 2 ídem con salvedad (generaliza sin el calificador "por ingresos").

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion.md` (scratch, no versionado).

---

## Cobertura y límites

- **Todas las primarias son lado grafo (re-confirmado 2026-07-14, tras la corrección de jerarquía de CQ-031):** `alcanzabilidad_kg` ×2 casos (CQ-031 —patas 1 y 2—, CQ-017) y `contenido_kg` ×3 casos (CQ-020, CQ-019, CQ-024). CQ-031 pata 1 es primaria + secundaria: el acierto exige la primaria (patrón "primaria + secundaria" de `casos_control.md`).
- **Causas lado agente presentes solo como secundarias:** CQ-031 (`navegación`, ítem 4.6), CQ-017 (`alucinacion_agente` en sus dos modos: b —glosa de cosecha propia— y a —portador exhibible no consultado—) y CQ-019 (modo a). Ninguna mueve el acierto.
- **Falsos positivos del juez documentados dentro del set: 12 claims en 5 entradas** (CQ-017: 1 · CQ-020: 7 · CQ-019: 1 · CQ-024: 1 · CQ-031: 2) — CQ-020 concentra 7. Útiles para calibrar la disciplina de "sin par / no es defecto del sistema".
- **Sin primaria lado agente — límite conocido:** el dev set no ejercita el caso donde lo que rompe la respuesta es del agente (`navegación` está presente solo como secundaria, CQ-031 ítem 4.6). Consistente con el gate (`casos_control.md`, cuya cobertura de lados declara lo mismo) y **consignado para la reunión de mentores** (queda abierta la incorporación futura de un caso con primaria lado agente).
