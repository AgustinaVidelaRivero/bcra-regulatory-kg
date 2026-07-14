# Referencias de calibración del DEV SET — iteración del verificador v5

**Qué es.** Las adjudicaciones humanas de referencia del **dev set** para iterar el prompt del verificador v5 (el *loop chico*): **8 casos** de `run_1`/`run_5` con GT en taxonomía v2 (pares `{sintoma_capa1, causa_capa2}`) — **5 originales** (adjudicados 2026-07-13/14) **+ 3 de la expansión post-gate #1** (off/run_1/CQ-016, on/run_5/CQ-019, off/run_1/CQ-018; adjudicados 2026-07-15) — contra los cuales se compara el output del verificador en cada iteración del prompt.

**Disclosure de la expansión (2026-07-15).** La expansión se motivó en las familias no ejercitadas que el gate #1 expuso (`provenance_imprecisa`, `estructural_kg`, y la nueva `aplicacion_erronea`); la adjudicación ciega **DISOLVIÓ las tres hipótesis** (provenance quedó como secundaria; estructural refutada por portador textual expuesto; aplicación errónea resultó des-scoping del grafo = `contenido_kg`) — **el hueco de cobertura persiste y queda documentado**.

**Relación con `casos_control.md`.** Los 5 casos-control de `run_3` son el **GATE FINAL pre-registrado**: se corren una sola vez, al final, para validar la versión candidata. Este dev set de `run_1`/`run_5` es el **banco de iteración**: acá se prueba, se falla y se ajusta cuantas veces haga falta. Esa separación resuelve la tensión loop-chico vs anti-overfitting: iterar contra el dev set no contamina el gate, y el gate no se gasta iterando.

**Fecha y procedencia.** Los 5 casos originales: adjudicación de la autora, **2026-07-13, asistida por revisión**, sobre la evidencia cruda de `posthoc_run/dev_set/hoja_adjudicacion.md` — dossieres **ciegos a las etiquetas del pilot** (pregunta + patas del juez + claims negativos + trayectoria + nodos íntegros + pasajes GT del PDF). Los 3 casos de la expansión: adjudicación de la autora, **2026-07-15, asistida por revisión**, sobre `posthoc_run/dev_set/hoja_adjudicacion_v2.md` — dossieres ciegos con **outputs COMPLETOS re-ejecutados determinísticamente** (sección 3 y 4 nunca desde la traza almacenada) y sección 5b de provenances verbatim. Las verificaciones de PDF citadas provienen de la sesión de revisión (barridos programáticos sobre todos los campos de los kg.json congelados + re-ejecución determinística de las búsquedas del agente con `harness.GraphIndex` + `pdf_locate` sobre el subset).

---

## Reglas de uso (explícitas)

1. **Los ejemplos resueltos del prompt del verificador NUNCA salen de estos 8 casos** (fuga dev→prompt). Si un caso de acá aparece en el prompt, el dev set deja de medir.
2. **El verificador nunca ve estas referencias.** Se compara su output contra ellas **externamente** (el comparador es quien lee este archivo, no el agente verificador).
3. **Criterio de acierto: igual que `casos_control.md`** — todas las **primarias** correctas como par `{sintoma, causa}`; las secundarias y los falsos positivos del juez **suman pero no son obligatorios**, y se registran como señal secundaria.
4. **Los 5 casos-control de run_3 NO se corren durante la iteración.** Solo al final, como gate.

---

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

---

## Caso off/run_1/CQ-020

**Pregunta:** ¿Cómo se calcula la exigencia de capital por riesgo de crédito (CRC) y con qué frecuencia se reporta al BCRA?

Adjudicación de la autora, 2026-07-13, asistida por revisión:

- **Pata 1 (cálculo) — claim central** "INC es el Incremento de exigencia por riesgo de crédito por excesos en participaciones en capital de empresas" — **`{noise_sensitivity, contenido_kg}` PRIMARIA.** Evidencia (precisada 2026-07-14, sin cambio de par ni jerarquía): el claim reproduce casi verbatim el label del nodo `req_incremento_de_exigencia_por_riesgo_de_credito_por_excesos_en_participaciones_en_capital_de_empresas_inc`, que estaba en el **TRAMO TRUNCADO** del output del paso 1 (5º resultado — visible en runtime, no en la traza almacenada), junto con su resumen ("Exigencia de capital adicional por inversiones significativas en empresas que exceden límites regulados"); ese label conflata INC(inversiones significativas, límites 15%/60% dentro de APRC) con el INC de la fórmula CRC (excesos en activos inmovilizados etc., Capitales 2.1) — soporte infiel al PDF.
  - **Nota de re-adjudicación (autora, 2026-07-14):** precisión de evidencia fundada en la auditoría de truncamiento — la traza almacenada no es el contexto del agente (`harness.py` pasa outputs completos al agente y almacena truncados); verificación por re-ejecución determinística.
- **Los otros 7 claims negativos** (k escala 1-1,19; k asignado por SEFyC; APRC suma con ponderadores; reporte vía R.I.-C.M.; y las 3 secundarias del R.I.-C.M.) — **FALSOS POSITIVOS DEL JUEZ, sin par.** Evidencia: soportados por los nodos abiertos (`req_factor_k`, `con_activos_ponderados_por_riesgo_de_credito_aprc`, `ins_regimen_informativo_contable_mensual`, `rep_regimen_informativo_contable_mensual_sobre_capitales_minimos`) y correctos contra el PDF (Capitales 2.1: escala k 1/1,03/1,08/1,13/1,19, calificación SEFYC, expresión de APRC; Régimen 1.1: frecuencia mensual por defecto).
- **Pata 2 (frecuencia)** — "mensual vía R.I.-C.M." — **sin defecto.** Evidencia: soportado por `ins_regimen_informativo_contable_mensual` (abierto en el paso 9) y correcto contra Régimen 1.1 (la exigencia por riesgo de crédito no está en las excepciones trimestrales).

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion.md` (scratch, no versionado).

---

## Caso on/run_1/CQ-019

**Pregunta:** Al computar los activos para la exigencia de capital por riesgo de crédito, ¿qué previsión por incobrabilidad no se deduce, y cómo se vincula esa regla con la clasificación de deudores?

Adjudicación de la autora, 2026-07-13, asistida por revisión:

- **Claim** "La previsión por riesgo de incobrabilidad sí se deduce para activos cubiertos con garantías preferidas A" [falso] — **`{noise_sensitivity, contenido_kg}` PRIMARIA.** Evidencia: soportado por `req_prevision_por_riesgo_de_incobrabilidad` ("Deducción por deterioro de activos... situación normal o cubiertos con garantías preferidas A"), cuyo contenido invierte el PDF (Capitales 2.3.1: "sin deducir el 100%... 'en situación normal'... y a las financiaciones que se encuentran cubiertas con garantías preferidas A" — ambas categorías son no-deducibles). Nota: ningún claim central falló; la primaria del caso descansa en la única secundaria [falso], decisión de la autora.
- **Claim** "La categoría 'situación normal' corresponde a clientes que demuestran capacidad de atender adecuadamente todos sus compromisos financieros" [no_soportado] — **FALSO POSITIVO DEL JUEZ, sin par** (re-adjudicado 2026-07-14). Evidencia: el resumen de `cla_situacion_normal_clasificacion_de_deudores`, con el contenido del claim ("Categoría de clasificación de deudores donde el cliente demuestra capacidad de atender adecuadamente todos sus compromisos financieros…"), apareció en el output COMPLETO del paso 2 del agente (auditoría 2026-07-14) — el claim estuvo soportado en runtime y es correcto contra Clasificación 6.5.1.
  - **Nota de re-adjudicación (autora, 2026-07-14):** fundada en la auditoría de truncamiento — la traza almacenada no es el contexto del agente (`harness.py` pasa outputs completos al agente y almacena truncados); verificación por re-ejecución determinística. Reemplaza la secundaria `{faithfulness, alucinacion_agente}` (modo a) del 2026-07-13.
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

## Caso off/run_1/CQ-016 (expansión post-gate #1)

**Pregunta:** ¿En qué unidad y con qué nivel de decimales deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos?

Adjudicación de la autora, 2026-07-15, asistida por revisión:

**CASO SIN DEFECTO DEL SISTEMA (exoneración integral).**

- **Claim secundario** «Esta disposición proviene del Régimen Informativo Contable Mensual» (único claim negativo del caso) — **FALSO POSITIVO DEL JUEZ, sin par.** Evidencia: soportado (resumen de `req_exigencia_de_integracion_de_capitales_minimos` expuesto en paso 1: "Sección 4 del Régimen Informativo Contable Mensual") y correcto contra el PDF (el R.I. de Exigencia e Integración es el apartado 4 del RICM — encabezado verbatim del propio pasaje GT). La dimensión `cita_documento_correcto=false` es artefacto de metadatos (el `ground_truth_secciones` no nombra documento; el juez defaulteó a false sobre una cita al documento correcto) y NO participa del criterio de falla (`verifier_pilot.scale_specs`: solo claims falso/no_soportado).
- **Cita del agente** (granularidad de página, `cita_precision="pagina"`) — **`{noise_sensitivity, provenance_imprecisa}` SECUNDARIA — lado grafo, no decisiva.** Evidencia: la provenance de `req_miles_de_pesos` es "pp. 2-3" (página sin punto; el contenido vive en el Punto 1.2, pág. 3), lo que limita la cita del agente a granularidad de página. Real, documentada, sin efecto en el veredicto.
- **Patrón de calibración: "exoneración integral + secundaria"** — acierto = declarar el caso sin defecto del sistema (ninguna primaria).

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion_v2.md` (scratch, no versionado).

---

## Caso on/run_5/CQ-019 (expansión post-gate #1)

**Pregunta:** Al computar los activos para la exigencia de capital por riesgo de crédito, ¿qué previsión por incobrabilidad no se deduce, y cómo se vincula esa regla con la clasificación de deudores?

Adjudicación de la autora, 2026-07-15, asistida por revisión:

- **Claims centrales** «situación normal ≤31 días» y «se computa como patrimonio neto complementario» — **FALSOS POSITIVOS DEL JUEZ, sin par.** Evidencia: ambos EXPUESTOS en el paso 16 (resúmenes de `situacion_normal` y `prevision_por_cartera_en_situacion_normal`, re-ejecución determinística 2026-07-15) y correctos contra el PDF (Clasificación 7.2.1 verbatim; Capitales 8.2.3.3/8.4.1.1). Mecanismo del FP: el juez verifica contra `ground_truth_secciones` (2.3.1/6.5.1/7.2.1) y el PNc cae fuera de ese marco aunque sea corpus verdadero — mismo patrón que la fórmula 70100000 en run_3/CQ-020.
- **La racionalización** «responde a que esos deudores presentan menor riesgo de incumplimiento» — **`{faithfulness, alucinacion_agente}` (modo b) SECUNDARIA.** Evidencia: ni los nodos expuestos ni el PDF dan esa justificación (barrido 2026-07-15; el 2.3.1 establece la regla sin fundamentarla).
- **SIN PRIMARIA.** Nota: la hipótesis estructural del inventario (familia B) queda refutada para este caso — el dato-puente (la referencia cruzada a 6.5.1/7.2.1) existe como portador textual (`to_sobre_clasificacion_de_deudores`) y estuvo expuesto en la trayectoria; los extremos sin arista no impidieron el vínculo.
- **Patrón de calibración: "exoneración de centrales + secundaria lado agente"** — acierto = ninguna primaria emitida.

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion_v2.md` (scratch, no versionado).

---

## Caso off/run_1/CQ-018 (expansión post-gate #1)

**Pregunta:** Los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas, ¿deben cumplir con Protección al Usuario y, además, clasificar a sus deudores? ¿Bajo qué criterio clasifican?

Adjudicación de la autora, 2026-07-15, asistida por revisión:

- **Claims de "Situación normal" y "Riesgo bajo"** — **`{noise_sensitivity, contenido_kg}` PRIMARIA.** Evidencia: ambos ecos verbatim de nodos defectuosos. `cla_situacion_normal_clasificacion_de_deudores` porta la definición COMERCIAL (6.5.1, "flujo de fondos") sin marca de alcance bajo label genérico — la definición pertinente al criterio de los PNFC es la de consumo (7.2.1, "puntual ≤31 días"); nodo des-scopeado (precedente: CQ-024 dev). `cla_riesgo_bajo_...` define riesgo bajo como "puntual o ≤31 días en refinanciaciones periódicas", que contradice el 7.2.2 ("atrasos de más de 31 hasta 90 días") — definición errónea.
- **Riesgo medio / riesgo alto / irrecuperable + los dos claims del Directivo Responsable** — **FALSOS POSITIVOS DEL JUEZ, sin par (×5).** Evidencia: los 3 de categorías son ecos de nodos expuestos, correctos contra 7.2.3/7.2.4/7.2.5 verbatim; los 2 del Directivo Responsable están soportados por `rsj_directivo_...` expuesto y los edges `debe_designar` de los pasos 7-8, correctos contra Protección 3.2.1.1 ("las empresas no financieras emisoras... y los otros proveedores no financieros de crédito... deberán designar"). Mecanismo de los 3 de categorías: contenido verdadero del corpus fuera de `ground_truth_secciones` — tercer caso del patrón (con run_3/CQ-020 y on/run_5/CQ-019).
- **Observación sin par:** `cla_riesgo_alto` y `cla_irrecuperable` tienen provenances VACÍAS (`[]`) — imperfección real del grafo, sin efecto en este veredicto (las citas de la respuesta salieron de otros nodos).
- **Patrón de calibración: "primaria única + FPs masivos"** — acierto = la primaria `{noise_sensitivity, contenido_kg}`.

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion_v2.md` (scratch, no versionado).

---

## Cobertura y límites

- **Primarias (actualizado 2026-07-15):** `alcanzabilidad_kg` ×2 casos (CQ-031 —patas 1 y 2—; CQ-017 pata 2-a) · `contenido_kg` ×5 casos (CQ-017 pata 2-b, CQ-020, CQ-019-run1, CQ-024, CQ-018) · **DOS CASOS DE EXONERACIÓN sin primaria** (CQ-016: exoneración integral + secundaria provenance; CQ-019-run5: exoneración de centrales + secundaria modo b) — patrón nuevo que ejercita el modo de falla de sobre-diagnóstico del gate #1 (CQ-020). Patrones de acierto: CQ-017 pata 2 es **sobredeterminada con DOS primarias** (acierto exige AMBAS, patrón "varias primarias"); CQ-031 pata 1 es primaria + secundaria (acierto = la primaria).
- **Lado agente: solo 2 secundarias** (CQ-031 `navegación`, ítem 4.6; CQ-019-run5 `alucinacion_agente` modo b). Sin instancias vigentes de: `alucinacion_agente` modo (a), `aplicacion_erronea`, `provenance_imprecisa` como primaria, `estructural_kg` — familias cubiertas solo por árbol y criterios, no por casos; **rareza consignada para la reunión de mentores**.
- **Falsos positivos del juez: 24 en los dev sets** (16 v1: CQ-017 4 · CQ-020 7 · CQ-019-run1 2 · CQ-024 1 · CQ-031 2 — más 8 v2: CQ-016 1 · CQ-019-run5 2 · CQ-018 5) **+ 2 en el gate = 26 documentados.** **MECANISMO identificado (tres confirmaciones):** el juez verifica contra `ground_truth_secciones` y marca `no_soportado` contenido verdadero del corpus fuera de ese marco (fórmula 70100000 / PNc 8.2.3.3 / definiciones 7.2.x). Útiles para calibrar la disciplina de "sin par / no es defecto del sistema".
- **Nota metodológica (2026-07-14):** cinco correcciones de referencia de esta semana son trazables al **truncamiento de trazas** — la traza almacena outputs truncados pero el agente recibió los completos (`harness.py`). Regla operativa: toda afirmación "X no apareció en la trayectoria" exige **re-ejecución determinística de los outputs completos**, nunca lectura de la traza almacenada sola. La **exposición en runtime** incluye los `resumen_propiedades` de los resultados de `buscar_nodos` (no solo lo abierto con `ver_nodo`): un claim puede estar soportado por un resumen de búsqueda que el agente nunca abrió.
- **Nota metodológica (2026-07-15) — criterio des-scoping vs aplicación:** si el alcance está EN el nodo y el agente lo ignora → `aplicacion_erronea`; si el nodo omite el alcance → `contenido_kg` (precedentes: CQ-024, CQ-018).
