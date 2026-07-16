# Casos del piloto v6.0-D — vara de adjudicación (marco POST-HOC)

Vara del **piloto del compuesto v6.0-D**, bajo `docs/protocolo_piloto_v6.md` **+ su Enmienda
v1.1** (los GTs se adjudican sobre el marco POST-HOC: los claims que el juez post-hoc reprobó
y lo que la respuesta post-hoc afirma — exactamente el input que el instrumento recibe).
Adjudicada **ANTES de cualquier corrida**: el sellado es **por inexistencia** — los
veredictos del compuesto sobre estos casos no existen al momento de escribir esto.

**Vocabulario:** taxonomía **v2.6.1** (pares `{sintoma_capa1, causa_capa2}`, ver
`taxonomia.md`). **Circuito de adjudicación:** el de la vara v3 — re-ejecuciones
determinísticas de las trazas (outputs COMPLETOS, nunca la traza truncada), barridos
programáticos sobre el kg congelado, verificación contra los PDF del corpus, y D1
(`test_alcanzabilidad`) como instrumento de adjudicación. **Evidencia:**
`docs/evidencia_piloto/` (expediente_piloto_1/2.md, verificaciones_piloto.md) y
`docs/evidencia_capa_d/verificacion_estructura_piloto.md`.

**Los 5 casos** (todos off/run_3): CQ-018 (síntoma central), CQ-019 y CQ-033 (síntoma
secundario), CQ-016 y CQ-024 (controles negativos — enmienda E4).

---

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

## CQ-033 — `cadena_restriccion_excepcion` · TO: capitales

- **Pregunta:** ¿Cuál es el límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2, y bajo qué condiciones ese límite se reduce?
- **Síntoma post-hoc (verbatim, 1 no_soportado — cero centrales reprobados):**
  - [no_soportado] "Ese límite del 17% está vigente hasta el 30/06/26"
- **GT: SIN PRIMARIA + UNA SECUNDARIA REAL — `{noise_sensitivity, contenido_kg}`** sobre el
  claim del "hasta el 30/06/26".
  - **Mecanismo (des-scoping, test v2.6):** el claim está **SOPORTADO** — es eco del nodo
    `Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ`,
    expuesto en los outputs completos de los **pasos 1, 2, 3, 4 y 7** — pero el nodo presenta
    la regla **TRANSITORIA del 12.3 amputada de su encabezado de alcance**: su `descripcion`
    dice "La exigencia de capital por riesgo operacional para entidades del grupo B ... hasta
    el 30/06/26 no podrá superar el 17% del promedio de los últimos 36 meses", mientras el
    PDF (12.3) la scopea "**Para aquellas entidades financieras que sean reclasificadas desde
    el 01/01/2026**..."; el alcance sobrevive **solo en la provenance** (metadato: "Punto
    12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026").
    El límite general del 17% (7.3.2 del PDF) es permanente, sin esa vigencia. El nodo,
    leído solo, NO declara alcance ajeno → **defecto de contenido del grafo**, no de
    aplicación del agente.
  - **Exclusión explícita de `aplicacion_erronea`** (test v2.6: el alcance NO está declarado
    en el contenido del nodo) **y de `alucinacion_agente`** (el claim está soportado y es eco
    fiel del nodo).
- **REGLA DE ACIERTO:** acierto = **sin primarias**; detectar la secundaria
  `{noise_sensitivity, contenido_kg}` **suma**; **CUALQUIER primaria = miss**; atribuir la
  secundaria a `aplicacion_erronea` o `alucinacion_agente` **no es acierto de secundaria**.
- **Evidencia:** `docs/evidencia_piloto/verificaciones_piloto.md` §3 (exposición del "30/06"
  en el paso 3 con fragmento; barrido kg con el nodo íntegro — properties y provenance por
  separado); `docs/evidencia_piloto/expediente_piloto_1.md` (caso CQ-033) y
  `expediente_piloto_2.md` (outputs completos);
  `docs/evidencia_capa_d/verificacion_estructura_piloto.md` §2.
- **NOTA DE BACKLOG:** familia de nodos con provenance 12.3 des-scopeados — el del grupo C
  ídem (límites 14%/8%/5%); verificar en la ronda de refinamiento si existen portadores de
  los límites permanentes 7.3.1/7.3.2.
- **Nota (disclosure):** **sin homólogo** en ninguna etapa — la medición más limpia del
  piloto (protocolo §3).

## CQ-016 — `factual_directa` · TO: regimen — CONTROL NEGATIVO (enmienda E4)

- **Pregunta:** ¿En qué unidad y con qué nivel de decimales deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos?
- **Síntoma post-hoc: VACÍO** (verbatim: correctitud "correcta", completitud "completa", cero
  claims reprobados, ambas patas "cubierta" —
  `docs/evidencia_capa_d/verificacion_estructura_piloto.md` §2).
- **GT: EXONERACIÓN TOTAL** — `sin_defecto`; ninguna atribución de defecto.
- **REGLA DE ACIERTO:** acierto = exoneración total; **cualquier atribución de defecto =
  miss**; el **triage por R1** del compuesto sobre la exoneración correcta es **enrutamiento
  esperado** de la política conservadora, **no error** (enmienda E4 — su costo se mide como
  métrica del tablero).
- **Evidencia:** `docs/evidencia_piloto/expediente_piloto_1.md` (caso CQ-016);
  `docs/evidencia_capa_d/verificacion_estructura_piloto.md` §2.
- **NOTA DE BACKLOG (fuera del scoring):** el hecho identitario "el R.I. de Exigencia e
  Integración de Capitales Mínimos ES la Sección 4 del R.I.C.M." (verificado contra el
  encabezado del PDF) **no tiene portador en el grafo** — barrido en
  `docs/evidencia_piloto/verificaciones_piloto.md` §4: 0 candidatos para "exigencia e
  integracion"/"apartado 4"/"r.i.-c.m.". Ese hueco motiva el hedging del agente ("no se
  encontró ... como entidad diferenciada") y la falla del frozen (completitud parcial 3/3)
  que NO se reprodujo en el marco post-hoc (enmienda E2).
- **Nota (disclosure):** homólogo dev `off/run_1/CQ-016` — otro grafo, precedente
  taxonómico, no evidencia de este caso.

## CQ-024 — `multi_norma` · TO: clasificacion — CONTROL NEGATIVO (enmienda E4)

- **Pregunta:** ¿Con qué periodicidad mínima debe clasificarse un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC, y en qué casos la reevaluación debe ser inmediata?
- **Síntoma post-hoc: VACÍO** (verbatim: correctitud "correcta", completitud "completa", cero
  claims reprobados, ambas patas "cubierta" —
  `docs/evidencia_capa_d/verificacion_estructura_piloto.md` §2).
- **GT: EXONERACIÓN TOTAL** — `sin_defecto`; ninguna atribución de defecto.
- **REGLA DE ACIERTO:** ídem CQ-016 — acierto = exoneración total; cualquier atribución de
  defecto = miss; triage por R1 = enrutamiento esperado, no error.
- **Evidencia:** `docs/evidencia_piloto/expediente_piloto_1.md` (caso CQ-024);
  `docs/evidencia_capa_d/verificacion_estructura_piloto.md` §2.
- **NOTA DE BACKLOG:** su falla del frozen (1 afirmación central no soportada en la rep 1)
  queda para investigar en la ronda de refinamiento, fuera de este piloto (enmienda E2:
  falla no reproducida en el marco post-hoc).
- **Nota (disclosure):** homólogo dev `off/run_1/CQ-024` — otro grafo, precedente
  taxonómico, no evidencia de este caso.

---

**Vara del piloto v1 — 2026-07-16.** Protocolo: `docs/protocolo_piloto_v6.md` + Enmienda
v1.1 (pre-ejecución). **Hallazgos laterales al backlog de refinamiento** (documentados acá,
fuera del scoring del piloto):

1. **Provenance corrida 4.1→4.2** de `Obligacion_evaluar_capacidad_de_pago` (CQ-018 — no
   participó de la falla: contrafáctico documentado en su entrada).
2. **Familia de nodos 12.3 des-scopeados** — regla transitoria sin su encabezado de alcance
   en el contenido (grupo B 17%/11%/7%; grupo C 14%/8%/5%); verificar portadores de los
   límites permanentes 7.3.1/7.3.2 (CQ-033).
3. **Hecho identitario ausente**: "el R.I. de Exigencia e Integración de Capitales Mínimos
   ES la Sección 4 del R.I.C.M." sin portador en el grafo (CQ-016).
