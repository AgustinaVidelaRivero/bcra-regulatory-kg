# Casos del DEV de S1 — VARA DE DEV (marco POST-HOC)

**RÓTULO DISTINTIVO — VARA DE DEV.** A diferencia de las varas del gate, del piloto y de la
validación, estos GTs son **material de DESARROLLO de S1** (`docs/diseno_v7_s1.md` §4): el
prompt de S1 **puede iterarse contra ellos**. **NO son material de evaluación final** — el
juicio de v7 es el **gate de preguntas nuevas, sellado aparte**, con head-to-head
pre-registrado v6.1-D vs v7.

**Marco POST-HOC** (los claims que el juez post-hoc reprobó y lo que la respuesta post-hoc
afirma — el input real del instrumento). **Adjudicada ANTES de correr v6.1-D o S1 sobre
estos casos** — la reserva pre-registrada llega intocada: ni verificador, ni capa
determinística, ni S1 tienen veredicto alguno sobre estos 4 casos al momento de escribir
esto. **Vocabulario:** taxonomía v2.6.1. **Circuito:** el de la vara — re-ejecuciones
determinísticas de outputs completos, barridos programáticos sobre el kg congelado de cada
run, verificación contra los PDF del corpus, y D1 como instrumento de adjudicación.

**Evidencia:** `docs/evidencia_dev_v7/` (expediente_dev_v7_1/2.md,
verificaciones_dev_v7_1/2.md).

**Los 4 casos:** run_2/CQ-021 · run_4/{CQ-008, CQ-021, CQ-028} — la reserva pre-registrada
del protocolo de validación (`docs/protocolo_validacion_v61.md`), sin uso previo en ninguna
etapa (barrido mecánico: cero apariciones de estas CQs en las cuatro varas/referencias).

---

## run_2/CQ-021 — `factual_directa` · reserva v7

- **Pregunta:** ¿En qué casos es optativo para la entidad comunicar al deudor un cambio
  negativo en su clasificación, y de qué régimen depende el umbral?
- **Síntoma post-hoc:** F = 0 claims reprobados · P = **2 patas no cubiertas** (los casos
  optativos; el régimen del umbral) — correctitud `correcta`, completitud `parcial`
  (`docs/evidencia_dev_v7/expediente_dev_v7_1.md`, caso run_2/CQ-021 §2).
- **GT: {context_recall, completitud_kg} PRIMARIA — PATA DOBLE.** La cláusula optativa del
  3.4.2 y su remisión al RICM no tienen portador en el grafo:
  - `optativo|optativa`: **0 nodos en todo el kg run_2**
    (`docs/evidencia_dev_v7/verificaciones_dev_v7_1.md` §1);
  - `3.4.2`: **0 en properties y 0 en provenances** (run_2 cita "Sección N > Punto X");
  - los 7 nodos de `saldo de deuda` del kg: **ni expuestos ni alcanzables** (D1 false en
    todos, incluido `requisito:saldo_de_deuda_sin_deducir_previsiones_por_riesgo`).
- La extracción capturó solo la obligación y el plazo: el nodo
  `plazo:45_dias_de_realizada_la_reclasificacion` quedó expuesto **únicamente como vecino
  en el paso 6** (viajaron `vecino_label` + provenances; sus properties nunca se
  mostraron) — **observación de exposición, sin efecto en el GT**.
- **Conducta del agente: abstención parcial honesta** — afirmó la obligación general de los
  45 días (claim verdadero) y reportó explícitamente el alcance faltante en las dos patas.
- **REGLA DE ACIERTO:** acierto = **completitud_kg primaria**;
  **alcanzabilidad_kg/navegación NO son acierto** (no hay portador que alcanzar: 0
  candidatos en los barridos); **atribuir defecto al claim verdadero de los 45 días
  invalida** el caso.
- **Evidencia:** expediente_dev_v7_1.md (§1-2-5) + expediente_dev_v7_2.md (trayectoria,
  fidelidad 15/15) + verificaciones_dev_v7_1.md §1.

## run_4/CQ-008 — `factual_directa` · reserva v7

- **Pregunta:** Cuando un cliente lo solicita, ¿en qué plazo debe la entidad financiera
  comunicarle la última clasificación que le asignó?
- **Síntoma post-hoc:** F = 0 · P = **1 pata no cubierta** (el plazo a solicitud) —
  correctitud `correcta`, completitud `parcial` (expediente_dev_v7_1.md, caso
  run_4/CQ-008 §2).
- **GT: {context_recall, completitud_kg} PRIMARIA ÚNICA.** La regla del 8.1 (10 días
  corridos a solicitud del cliente) no tiene portador en el grafo:
  - `solicitud ∧ clasificacion`: **0 nodos en todo el kg run_4**
    (`docs/evidencia_dev_v7/verificaciones_dev_v7_1.md` §2);
  - los 17 nodos de `10 dias` son de OTROS TOs (exterior/capitales), ninguno de
    clasificación;
  - el único `comunicar ∧ clasificacion`
    (`deudor_en_gestion_judicial_o_extrajudicial_de_cobro`, provenance Punto 3.4.2) — **no
    expuesto, D1 false** (mejor rank 28).
- **Conducta del agente: abstención total honesta** — 15 pasos de búsqueda y un triple
  reporte de alcance, sin inventar el plazo.
- **REGLA DE ACIERTO:** ídem run_2/CQ-021 — acierto = **completitud_kg primaria**;
  alcanzabilidad/navegación NO son acierto; atribuir defecto a la conducta de abstención
  invalida.
- **Evidencia:** expediente_dev_v7_1.md (§1-2-5) + expediente_dev_v7_2.md (trayectoria,
  fidelidad 15/15) + verificaciones_dev_v7_1.md §2.

## run_4/CQ-021 — `factual_directa` · reserva v7

- **Pregunta:** la misma de run_2/CQ-021 (misma CQ sobre OTRO grafo).
- **Síntoma post-hoc:** F = 1 (secundario `no_soportado`: los "medios especificados por la
  regulación") · P = **2 patas no cubiertas** — correctitud `correcta`, completitud
  `parcial`; los 3 claims CENTRALES (optatividad existe / depende del saldo / hay un
  régimen del umbral) fueron aprobados `verdadero` (expediente_dev_v7_1.md, caso
  run_4/CQ-021 §2).
- **GT: {context_recall, completitud_kg} PRIMARIA — PATA DOBLE — variante de PORTADOR
  COMPRIMIDO.** El nodo `cambio_negativo_en_clasificacion` ("…con excepciones según el
  saldo de deuda", expuesto en 7 pasos) **sostuvo los 3 centrales verdaderos**, pero el
  detalle de los casos y la remisión al RICM no tienen portador:
  - `optativ`: **0 en el kg run_4 Y 0 en los 16 outputs**
    (`docs/evidencia_dev_v7/verificaciones_dev_v7_2.md` §3);
  - `regimen informativo ∧ deudores`: **0 nodos** — la única exposición de "regimen
    informativo" es el RIOC de operaciones de cambio, OTRO régimen.
  - **Distinción consignada:** el nodo **resume de menos, no afirma de más** — el defecto
    es de **completitud**, no de des-scoping (`contenido_kg`): el contenido que el portador
    tiene es fiel hasta donde llega.
- **SECUNDARIA: {faithfulness, alucinacion_agente}** sobre "medios especificados por la
  regulación" — ausente de outputs y del kg (exposición conjunta `medios ∧ comunicac`:
  AUSENTE); el modo (a)/(b) queda sin resolver, **sin efecto en el scoring**.
- **REGLA DE ACIERTO:** acierto = **completitud_kg primaria**; **contenido_kg NO es
  acierto** (el portador existente es fiel hasta donde llega); la secundaria **suma pero no
  se exige**.
- **Evidencia:** expediente_dev_v7_1.md (§1-2-5) + expediente_dev_v7_2.md (trayectoria,
  fidelidad 16/16) + verificaciones_dev_v7_2.md §3.

## run_4/CQ-028 — `cadena_restriccion_excepcion` · reserva v7

- **Pregunta:** ¿Puede un sujeto obligado cobrar una comisión por la precancelación total
  de una financiación? ¿Existe algún caso en que no se admita?
- **Síntoma post-hoc:** F = 2 (1 central `falso` + 1 secundario `no_soportado`) · P = 0 —
  correctitud `incorrecta`, completitud `completa` (expediente_dev_v7_1.md, caso
  run_4/CQ-028 §2).
- **GT: {noise_sensitivity, contenido_kg} PRIMARIA — NODO AMPUTADO DE SU CLÁUSULA
  DECISORIA.** El claim central falso ("el criterio es **el que ocurra primero**") nace del
  nodo `comision_por_precancelacion` (Punto 2.3.2.1, expuesto en los pasos 1, 3, 4, 6 y 7),
  cuya formulación termina: "…cuando haya transcurrido al menos la cuarta parte del plazo
  original **o 180 días**." El PDF dice (cita textual del GT del eval set, verbatim): "…la
  cuarta parte del plazo original de la financiación o 180 días corridos desde su
  otorgamiento, **de ambos el mayor**." La cláusula "de ambos el mayor" **no está en el
  nodo ni en ningún output** — "el mayor" solo aparece en un nodo de posiciones netas de
  moneda, otro tema (`docs/evidencia_dev_v7/verificaciones_dev_v7_2.md` §4).
  **Contrafáctico:** con el nodo completo, la glosa desaparece — la amputación empujó el
  error; la raíz es del grafo.
- **Conducta del agente (observación consignada, real y derivada de la amputación):** ante
  el "o" sin criterio de desempate, **rellenó la ambigüedad con un criterio inventado** ("el
  que ocurra primero") en vez de reportarla.
- **Los 3 centrales verdaderos** (puede cobrar / no se admite tras la cuarta parte / no se
  admite tras 180 días): **regla CQ-034** — atribuirles defecto **invalida** el caso.
- **El secundario** ("la parcial se permite sin la restricción") = **FALSO POSITIVO DEL
  JUEZ, sin par**: es una inferencia correcta del 2.3.2.1 — la restricción es solo para la
  precancelación total (cita del GT: "En el caso de precancelación total, no se admitirá…").
- **REGLA DE ACIERTO:** acierto = **contenido_kg primaria**; **alucinacion_agente como
  primaria NO es acierto** — la lectura alternativa queda documentada como **frontera
  genuina**: este caso es material de calibración de S1 **exactamente en esa frontera**
  (comparación de la formulación del nodo contra el alcance/criterio declarado en la
  fuente).
- **Evidencia:** expediente_dev_v7_1.md (§1-2-5) + expediente_dev_v7_2.md (trayectoria,
  fidelidad 15/15) + verificaciones_dev_v7_2.md §4.

---

## Cierre

**Versión:** vara de dev v1 — 2026-07-17. **Uso:** DEV de S1 conforme a
`docs/diseno_v7_s1.md` §4 (iteración del prompt de S1 permitida SOLO contra estos 4 casos,
con la regla de frenado de v5.7: lo que el dev motiva se valida sobre material que el dev
no tocó — el gate de preguntas nuevas, sellado aparte).

**HALLAZGO TRANSVERSAL (al backlog, con nombre): AMPUTACIÓN DE CLÁUSULAS como patrón de
extracción del pipeline.** Quinta y sexta apariciones: el **3.4.2 amputado de su cláusula
optativa** (en run_2 Y en run_4 — el mismo punto, dos pipelines distintos) y el **2.3.2.1
amputado de su criterio de desempate** ("de ambos el mayor", run_4) — sumándose a las
series previas (12.3/encabezado de alcance; 10.1/sujeto). El patrón: la extracción captura
la regla principal y pierde la cláusula que la condiciona (opción, alcance, desempate),
dejando nodos fieles-pero-incompletos que empujan al agente a rellenar o al lector a
generalizar.

**Ítems de backlog:**
- Cláusula optativa del 3.4.2 sin portador (run_2 y run_4).
- Regla del 8.1 (10 días corridos a solicitud del cliente) sin portador (run_4).
- Criterio "de ambos el mayor" del 2.3.2.1 amputado (run_4).
