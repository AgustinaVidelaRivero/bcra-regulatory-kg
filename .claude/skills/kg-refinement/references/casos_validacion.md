# Casos de la validación de v6.1-D — vara de adjudicación (marco POST-HOC)

Vara de la **validación empírica del compuesto v6.1-D**, bajo
`docs/protocolo_validacion_v61.md`. **Marco POST-HOC** (los claims que el juez post-hoc
reprobó y lo que la respuesta post-hoc afirma — el input real del instrumento). Adjudicada
**ANTES de cualquier corrida** — **sellado por inexistencia**: los veredictos del compuesto
sobre estos 8 casos no existen al momento de escribir esto. **Vocabulario:** taxonomía
v2.6.1. **Circuito:** el de la vara — re-ejecuciones determinísticas de outputs completos,
barridos programáticos sobre el kg congelado de cada run, verificación contra los PDF del
corpus, y D1 como instrumento de adjudicación.

**Evidencia:** `docs/evidencia_validacion/` (censo, expediente_validacion_1/2/3.md,
verificaciones_validacion_1/2.md).

**Los 8 casos:** run_2/{CQ-015, CQ-018, CQ-019, CQ-025} · run_4/{CQ-014, CQ-019, CQ-017,
CQ-020} — composición del protocolo §3 (2 controles por diseño, 2 deliberados por severidad,
4 por sorteo con semilla fija).

---

## run_2/CQ-015 — `factual_directa` · CONTROL NEGATIVO (por diseño)

- **Pregunta:** ¿Qué criterios definen a una persona humana como "residente" a los fines cambiarios?
- **Rol:** control negativo — prueba **R6a POR DISEÑO** (falla del frozen no reproducida).
- **Síntoma post-hoc (verbatim):** VACÍO — correctitud `correcta`, completitud `completa`,
  cero claims reprobados, cero patas no cubiertas
  (`docs/evidencia_validacion/expediente_validacion_1.md`, caso run_2/CQ-015 §2).
- **GT: EXONERACIÓN TOTAL** — `sin_defecto`; ninguna atribución de defecto.
- **REGLA DE ACIERTO:** acierto = exoneración total; **cualquier atribución de defecto =
  miss**; el triage por **R1/R6a** sobre la exoneración correcta es **enrutamiento esperado**
  (regla E4 heredada), no error — su costo se mide.
- **Evidencia:** expediente_validacion_1.md (caso run_2/CQ-015: síntoma vacío explícito +
  contexto frozen rotulado); expediente_validacion_2.md (trayectoria, fidelidad 4/4).
- **NOTA DE BACKLOG:** la glosa del frozen ("los criterios son alternativos", adjudicada
  falsa en la firmada) **no se reprodujo** en el marco post-hoc — patrón de interpretación
  del agente, sin acción de grafo.

## run_4/CQ-014 — `factual_directa` · CONTROL NEGATIVO (por diseño)

- **Pregunta:** ¿En qué plazo deben ingresarse y liquidarse en el mercado de cambios los cobros de exportaciones de servicios?
- **Rol:** control negativo — ídem run_2/CQ-015.
- **Síntoma post-hoc (verbatim):** VACÍO — correctitud `correcta`, completitud `completa`,
  cero reprobados, cero patas no cubiertas (expediente_validacion_1.md §2, con el contexto
  frozen rotulado: centrales 2/0/0, FINAL correcta).
- **GT: EXONERACIÓN TOTAL** — `sin_defecto`.
- **REGLA DE ACIERTO:** ídem run_2/CQ-015 (acierto = exoneración; defecto = miss; R1/R6a =
  enrutamiento esperado).
- **Evidencia:** expediente_validacion_1.md (caso run_4/CQ-014);
  expediente_validacion_3.md (trayectoria, fidelidad 9/9).
- **NOTA DE BACKLOG:** los plazos de contraparte vinculada (180/90 días) del frozen **no se
  reprodujeron**; verificar en refinamiento si son prior del agente o contenido del corpus.

## run_2/CQ-025 — `factual_directa` · sorteo

- **Pregunta:** ¿Con qué frecuencia se informa la exigencia por riesgo de mercado y el ratio de apalancamiento?
- **Síntoma post-hoc (verbatim):** correctitud `incorrecta` · [falso/central] "En el Régimen
  Informativo de Capitales Mínimos, la exigencia por riesgo de mercado se informa con
  frecuencia mensual." · [no_soportado] "La exigencia por riesgo de mercado corresponde a
  las posiciones del último día del mes." (expediente_validacion_1.md §2).
- **GT:**
  - **`{noise_sensitivity, contenido_kg}` PRIMARIA:** el claim central falso es **eco del
    nodo `obligacion:envio_mensual_de_datos_sobre_riesgo_de_mercado`, EXPUESTO en el paso 2**
    (`docs/evidencia_validacion/verificaciones_validacion_1.md` §1), cuya descripcion afirma
    "envío mensual de datos" con provenance "Sección 4 > Punto 4.3" — **contradice al PDF**:
    el Punto 1.1 del TO de Régimen Informativo ubica los datos de los puntos 4.3-4.5 en las
    excepciones **TRIMESTRALES** (verificación de la vara del gate sobre el mismo pasaje,
    mismo corpus).
  - **`{context_recall, alcanzabilidad_kg}` SECUNDARIA, con nota de sobredeterminación
    parcial:** el portador correcto
    (`obligacion:presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado`,
    descripcion trimestral fiel) **existe, NO expuesto, D1 `alcanzable=false`,
    `mejor_rank=22`** (verificaciones_validacion_1.md §1c) — su contrafáctico rompe la pata
    por otra vía.
  - El secundario "posiciones del último día del mes" = **FALSO POSITIVO DEL JUEZ, sin par**
    (eco verbatim del nodo del paso 4, abierto).
- **REGLA DE ACIERTO:** acierto = **`contenido_kg` como primaria**; `navegación` o
  `alcanzabilidad_kg` como PRIMARIA **no son acierto**; la secundaria suma, no se exige.
- **Evidencia:** verificaciones_validacion_1.md §1 (exposición de "mensual" con nodo fuente;
  portador trimestral íntegro con D1); expediente_validacion_1.md (caso run_2/CQ-025) y
  expediente_validacion_2.md (trayectoria).
- **Nota (disclosure):** homólogo de gate run_3/CQ-025 — otro grafo, precedente taxonómico
  (con su asterisco heredado), no evidencia de este caso.

## run_2/CQ-019 — `multi_norma` · sorteo

- **Pregunta:** Al computar los activos para la exigencia de capital por riesgo de crédito, ¿qué previsión por incobrabilidad no se deduce, y cómo se vincula esa regla con la clasificación de deudores?
- **Síntoma post-hoc (verbatim):** correctitud `correcta`, completitud `parcial` — cero
  claims reprobados; **2 patas no cubiertas** ("qué previsión…", "cómo se vincula…")
  (expediente_validacion_1.md §2).
- **GT: `{context_recall, alcanzabilidad_kg}` PRIMARIA ÚNICA, PATA DOBLE:** el portador
  `concepto_definido:deudor_en_situacion_normal` **porta la regla Y el vínculo** — su
  descripcion: "Clasificación de deudor según normativa de clasificación de deudores del
  BCRA, **cuya cartera no será deducida al 100% de la previsión por riesgo de
  incobrabilidad**"; provenance Capitales "Sección 2 > Punto 2.3"; edge `definido_por` →
  `norma_referenciada:texto_ordenado_sobre_clasificacion_de_deudores` — **NO expuesto, D1
  `alcanzable=false`, `mejor_rank=null` (cero matches en 41 consultas)**
  (verificaciones_validacion_1.md §2).
  - **Mecanismo léxico documentado:** la pregunta dice "deudores", el portador "deudor" —
    **singular/plural sin stemming en el índice** (hermano del token truncado de CQ-031).
  - Conducta del agente: **abstención honesta** (3 reportes de alcance; sin claims).
  - "2.3.1": **0 en properties y 0 en provenances** de run_2 (verificaciones §2a-v).
- **REGLA DE ACIERTO:** acierto = **`alcanzabilidad_kg` como primaria**; `navegación` **NO**
  es acierto (excluida empíricamente por D1); `completitud_kg` **NO** es acierto (el
  portador existe).
- **Evidencia:** verificaciones_validacion_1.md §2 (candidatos íntegros con edges, D1);
  expediente_validacion_1.md (caso run_2/CQ-019) y expediente_validacion_2.md (fidelidad
  15/15).
- **Nota (disclosure):** homólogos dev on/run_1 y on/run_5, y piloto run_3 — otros grafos.

## run_2/CQ-018 — `multi_norma` · deliberado (severidad)

- **Pregunta:** Los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas, ¿deben cumplir con Protección al Usuario y, además, clasificar a sus deudores? ¿Bajo qué criterio clasifican?
- **Síntoma post-hoc (verbatim):** correctitud `incorrecta`, completitud `parcial`; **8
  claims reprobados (6 centrales, 1 falso)** y **1 pata no cubierta** ("¿las emisoras deben
  clasificar?") (expediente_validacion_1.md §2).
- **GT: SIN PRIMARIAS DE CLAIMS + PRIMARIA `{context_recall, completitud_kg}` EN LA PATA DE
  LAS EMISORAS.**
  - **Los 8 reprobados son FALSOS POSITIVOS DEL JUEZ, sin par — todos EXPUESTOS**
    (verificaciones_validacion_1.md §5a-5b):
    - **(a)** los 2 de reclamos: edges `obligado_a →
      obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios` en los **pasos 7 y
      8**;
    - **(b)** el **FALSO** del "criterio básico… medida a través del análisis de flujo de
      fondos": eco verbatim del nodo `concepto_definido:capacidad_de_pago`, **ABIERTO en el
      paso 12**, cuya descripcion fusiona los puntos 4.2 y 4.3.1 del TO de Clasificación —
      ambos verificados contra la página (4.2: "El criterio básico… capacidad de pago en el
      futuro…"; 4.3.1: "el énfasis deberá ponerse en el análisis de los flujos de fondos").
      **FP del juez sobre un veredicto "falso": variante grave del mecanismo, documentada.**
    - **(c)** los 3 de criterios objetivos: eco del nodo
      `concepto_definido:criterios_objetivos_de_clasificacion` (expuesto paso 10, abierto
      paso 11), correcto contra el punto 6.4.1 del TO, verificado contra la página ("término
      de morosidad, situación jurídica del cliente o de sus deudas, cumplimiento de
      refinanciaciones");
    - **(d)** los 2 secundarios: edges del paso 8 (información de productos; publicar
      contratos de adhesión).
  - **LA PRIMARIA:** la pata "¿las emisoras deben clasificar?" quedó no cubierta porque **el
    sujeto fue AMPUTADO del 10.1 en la extracción**: "10.1" da **0 portadores en properties**
    (29 solo en provenances, ninguno con la regla — verificaciones §5c); el único nodo
    emisoras∧clasificación (`sujeto_regulado:otras_entidades_acreedoras`) es la
    recategorización del 7.3, no la obligación, e inalcanzable (D1 false/null); los nodos de
    clasificar-por-mora existentes son de OTROS sujetos (seguros, MiPyMEs, PSCPP). **Gemelo
    por-sujeto del des-scoping** (el alcance subjetivo de la regla se perdió al extraer).
- **REGLA DE ACIERTO:** acierto = **`{context_recall, completitud_kg}` como primaria** (pata
  emisoras); **atribuir defecto a las 4 patas cubiertas invalida**; CUALQUIER otra primaria
  = miss; reconocer los FPs suma, no se exige.
- **Evidencia:** verificaciones_validacion_1.md §5; expediente_validacion_1.md (caso
  run_2/CQ-018) y expediente_validacion_2.md (fidelidad 15/15).
- **Nota (disclosure):** homólogos dev off/run_1 y piloto run_3 — otros grafos.

## run_4/CQ-017 — `multi_norma` · sorteo

- **Pregunta:** Un operador de cambio, ¿está alcanzado por las normas de Protección de Usuarios y debe intervenir como entidad autorizada en el mercado de cambios?
- **Síntoma post-hoc (verbatim):** correctitud `correcta`, completitud `parcial`; 2
  reprobados no centrales; **1 pata no cubierta** ("¿debe intervenir como entidad
  autorizada?") (expediente_validacion_1.md §2).
- **GT: PATA 2 — `{context_recall, completitud_kg}` PRIMARIA:** la regla del 1.1 de Exterior
  **no tiene portador en el kg de run_4** ("deberan intervenir": **0** en los 4 barridos —
  `docs/evidencia_validacion/verificaciones_validacion_2.md` §3a), pese a estar en el corpus
  (verificada contra el texto del TO: "… 'mercado de cambios', deberán intervenir…"); el
  único nodo operador (`operador_de_cambio`, provenance Protección 1.1.2.2) tiene **0
  salientes y 2 entrantes, ambos internos a Protección**; **0 aristas**
  operador↔entidad-autorizada sobre **3.434 edges** (§3b) — **hueco más profundo que el
  estructural de run_3: acá faltan las piezas, no solo el puente.**
  - **Pata 1 sana** (cubierta, centrales verdaderos) — **atribuirle defecto invalida**.
  - Los 2 secundarios = **FALSOS POSITIVOS DEL JUEZ, sin par**: ecos fieles de nodos
    expuestos y abiertos — `mercado_libre_de_cambios` (pasos 3/10/11/12; su descripcion es
    la definición del Artículo 1° del Decreto 260/02 anexado al TO, provenance
    p.183-185/Sección 15.1) y `personas_juridicas_no_autorizadas_a_operar_en_cambios`
    (pasos 13/15, provenance 3.10).
- **REGLA DE ACIERTO:** acierto = **`completitud_kg` como primaria de la pata 2**;
  `estructural_kg`/`alcanzabilidad_kg`/`navegación` como primaria **no son acierto**
  (exclusiones empíricas: 0 portadores).
- **Evidencia:** verificaciones_validacion_2.md §3; expediente_validacion_1.md (caso
  run_4/CQ-017) y expediente_validacion_3.md (fidelidad 16/16).
- **Nota (disclosure):** homólogos dev off/run_5 y gate run_3 — otros grafos.

## run_4/CQ-020 — `multi_norma` · sorteo

- **Pregunta:** ¿Cómo se calcula la exigencia de capital por riesgo de crédito (CRC) y con qué frecuencia se reporta al BCRA?
- **Síntoma post-hoc (verbatim):** correctitud `correcta`, completitud `parcial`; 4
  reprobados (3 centrales); **1 pata no cubierta** ("con qué frecuencia se reporta")
  (expediente_validacion_1.md §2).
- **GT: `{context_recall, completitud_kg}` PRIMARIA (pata frecuencia):** **0 nodos combinan
  frecuencia con riesgo de crédito en run_4** (verificaciones_validacion_2.md §4b) —
  **DEFECTO RECURRENTE con run_3/CQ-020: primer defecto inter-grafos del proyecto** (nota de
  backlog con ese rótulo). Conducta del agente: **abstención honesta** sobre esa pata
  (`respondible: false`).
  - **Los 3 centrales y el secundario reprobados = FALSOS POSITIVOS DEL JUEZ, sin par:**
    k↔SEFYC y "1 a 1,19" soportados por el nodo `factor_k` **EXPUESTO en el paso 14** (su
    descripcion trae la escala completa) y verificados contra el PDF (Capitales 2.1: "k:
    factor vinculado a la calificación… SEFYC", tabla 1→1 … 5→1,19, verificada contra el
    texto); APRC-ponderadores soportado (nodo `aprc` paso 14 +
    `activos_ponderados_por_riesgo_de_credito` pasos 7/8/11) y correcto contra el 2.1/3.1;
    el del R.I.C.M. soportado (paso 10). **Variante del mecanismo documentada:
    FP-por-cita-estrecha** — el contenido vive en la sección gold 2.1, pero fuera de la
    `cita_textual` del eval set.
- **REGLA DE ACIERTO:** acierto = **`completitud_kg` como primaria de la pata frecuencia**;
  **regla CQ-034 sobre la pata del cálculo** (atribuirle defecto invalida);
  `alcanzabilidad_kg`/`navegación` no son acierto.
- **Evidencia:** verificaciones_validacion_2.md §4; expediente_validacion_1.md (caso
  run_4/CQ-020) y expediente_validacion_3.md (fidelidad 15/15).
- **Nota (disclosure):** homólogos dev off/run_1 y gate run_3 — otros grafos.

## run_4/CQ-019 — `multi_norma` · deliberado (severidad)

- **Pregunta:** Al computar los activos para la exigencia de capital por riesgo de crédito, ¿qué previsión por incobrabilidad no se deduce, y cómo se vincula esa regla con la clasificación de deudores?
- **Síntoma post-hoc (verbatim):** correctitud `incorrecta`; **7 reprobados (4 centrales, de
  ellos 3 `falso`)** (expediente_validacion_1.md §2).
- **GT: `{noise_sensitivity, aplicacion_erronea}` PRIMARIA — PRIMER EJEMPLAR GENUINO DE LA
  CATEGORÍA.** Los 3 claims `falso` (previsión específica no se deduce; cálculo sobre monto
  bruto; no se deduce del KSA) son **ecos fieles del nodo `prevision_especifica`, EXPUESTO
  en los pasos 3/9 y ABIERTO en el paso 4**, cuya descripcion **DECLARA SU ALCANCE en el
  propio contenido**: "deducción contable que no se aplica al cálculo de **KSA**; el cálculo
  debe efectuarse sobre monto bruto de la exposición"
  (verificaciones_validacion_2.md §6a-6b) — y el nodo `ksa` también estuvo expuesto (edge
  `no_se_deduce_en_calculo_de → ksa`, paso 7). El contenido es **fiel al PDF** (Capitales
  3.1.11.x, titulizaciones, verificado contra el texto: "el cálculo de KSA deberá efectuarse
  usando el monto bruto de la exposición –es decir, sin deducir la previsión específica…") —
  **el agente aplicó a la exigencia CRC general una regla cuyo marco (KSA) estaba
  declarado**; la respuesta correcta es el 2.3.1 (netos, sin deducir la de situación
  normal). **Los `falso` del juez son CORRECTOS — se consigna.**
  - **SECUNDARIAS:**
    - `{faithfulness, alucinacion_agente}` sobre "las previsiones mínimas se determinan en
      función de la categoría" — claim central cuyo contenido fino **no está en lo expuesto
      ni en el corpus de 5 TOs** (pertenece al TO de Previsiones Mínimas, **EXTRA-CORPUS** —
      arruga documentada: primera aparición de la frontera verdad-extra-corpus). Jerarquía
      secundaria fundada: no rompe el caso (la correctitud incorrecta la producen los
      `falso`).
    - `{faithfulness, alucinacion_agente}` sobre "criterios objetivos…" — **AUSENTE de los
      15 outputs** (verificaciones §6a); modo (a)/(b) sin resolver, sin efecto en scoring.
  - "Totalidad de financiaciones" = **FP del juez** (eco fiel del nodo
    `clasificacion_de_deudores`, pasos 3/6/9).
  - "Cinco categorías" = **NEUTRAL con nota de backlog** (soportado por eco del nodo
    expuesto; el conteo vigente de niveles queda como chequeo de refinamiento; **sin efecto
    en scoring, en ninguna dirección**).
- **REGLA DE ACIERTO:** acierto = **`aplicacion_erronea` como primaria**; `contenido_kg`
  como primaria **NO** es acierto (el nodo es fiel y declara su marco); `alucinacion_agente`
  como primaria **NO** es acierto (los claims están soportados); las secundarias suman, no
  se exigen.
- **Evidencia:** verificaciones_validacion_2.md §6 (nodos fuente íntegros con la marca
  KSA/titulización properties-vs-provenance por nodo); expediente_validacion_1.md (caso
  run_4/CQ-019) y expediente_validacion_3.md (fidelidad 15/15).
- **Nota (disclosure):** homólogos dev on/run_1 y on/run_5, y piloto run_3 — otros grafos.

---

**Vara de la validación v1 — 2026-07-16.** Protocolo: `docs/protocolo_validacion_v61.md`.
**Hallazgos al backlog de refinamiento** (documentados acá, fuera del scoring):

1. **Nodo `obligacion:envio_mensual_de_datos_sobre_riesgo_de_mercado` contradictorio con el
   1.1** (run_2 — provenance 4.3, contenido "mensual" donde el régimen lo hace trimestral).
2. **Portador del 2.3 inalcanzable por singular/plural** (run_2 —
   `deudor_en_situacion_normal` vs "deudores"; el índice no tiene stemming).
3. **Sujeto "emisoras" amputado del 10.1 en la extracción** (run_2 — la obligación de
   clasificar perdió su sujeto; gemelo por-sujeto del des-scoping).
4. **Regla del 1.1 de Exterior sin portador** (run_4 — faltan las piezas, no solo el puente).
5. **Frecuencia de reporte CRC ausente — DEFECTO RECURRENTE run_3/run_4** (primer defecto
   inter-grafos del proyecto).
6. **Conteo de niveles del nodo de categorías de clasificación** (run_4 — chequeo pendiente
   del claim "cinco categorías").
7. **Provenances de run_2 con formato sospechoso** ("Sección 7 > Punto 8.1" y análogas) —
   revisar la convención de localización de ese grafo.
