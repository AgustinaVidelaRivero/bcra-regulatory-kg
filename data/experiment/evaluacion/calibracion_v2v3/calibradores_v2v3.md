# Calibradores — familia v2/v3 (U5-PREP; split RATIFICADO por laudo 2026-08-02)

**Fecha:** 2026-08-02. **Formato:** el REAL del ciclo 2 — los calibradores del ciclo 2
son material QUEMADO con vara humana en **markdown por caso** (los 30 JSONs del gate CQN
+ su vara `docs/casos_gate_cqn.md`, iterados en las unidades 1/2/2b del ciclo; formato de
vara: `docs/casos_gate_cqn2.md` — secciones Perfil y síntoma / Ramas pre-registradas /
Exposición / VEREDICTO + tabla de reglas de acierto). **No existe ningún calibrador en
JSON en el ciclo 2** (verificado en la arqueología de la unidad: los únicos materiales de
calibración dentro del instrumento son los ejemplos resueltos hardcodeados de
`verificador.py` y los umbrales de `s1_fuentes_v04.py`, ambos sellados e intocables);
por eso este archivo es `.md`.

**Regla de fuga (idéntica al ciclo 2):** el verificador NUNCA ve este archivo (guard
`_assert_fuentes` de `verificador.py`; este archivo vive fuera de las fuentes del prompt
y así debe seguir). Se consume EXTERNAMENTE: quien compara la salida del instrumento
contra estas adjudicaciones es la lectura humana/externa, jamás el agente.

**Estado — LAUDADO (destrabe de la adjudicadora, 2026-08-02):** (a) split RATIFICADO,
con un agregado: **EV1-039 entra al gate como G-4** (casillero causal laudado
`contenido_kg` sobre la evidencia BKL-0006/RX-10 — vara y regla en
`docs/protocolo_gate_u5.md` §3); (b) reglas de acierto RATIFICADAS; (c) los tres
calibradores **QUEMADOS desde el laudo** (constancia en §3 de este archivo).

---

## 1. El split propuesto (justificación ficha por ficha)

**Material elegible** (única población con causa sellada — `expediente_material.md` §4):
EV1-015, EV1-018, EV1-029, EV1-031, EV1-035, EV1-042 (6 casos de sistema; 2 de ellos
portan además los casos del juez).

**Criterio (a) del mandato — máxima diversidad de clases con mínimo de fichas, y que el
gate conserve casos de cada clase si el material alcanza.** Las clases instanciadas son
tres: completitud_kg (×3), alcanzabilidad_kg (×2, una con brecha B′), exoneración/juez
(×2, subtipos distintos). Con 3 clases y ejemplares ≥2 por clase (salvo el subtipo (i)
del juez), el mínimo de calibración que cubre todo es **3 fichas — una por clase — y el
gate retiene al menos un ejemplar de cada clase**:

| Ficha | Lado propuesto | Justificación |
|---|---|---|
| **EV1-031** | **CALIBRACIÓN** | El ejemplar más rico de `completitud_kg` (doble sello: adjudicación 26/07 + predicción pre-registrada verificada mecánicamente; ambos brazos en la ficha; contraste 3-0→3-0 limpio). Calibrar con el ejemplar más rico y gatear con el espejo (EV1-042) maximiza lo que el calibrador enseña sin gastar la clase. |
| **EV1-018** | **CALIBRACIÓN** | La única `alcanzabilidad_kg` LIMPIA de la familia (dato nodificado, no alcanzado por ningún agente de ningún brazo, sin la complicación B′). Si fuera al gate, la clase quedaría calibrada solo con el caso B′ (EV1-029), que es justamente el ambiguo — calibrar con el caso limpio y gatear con el difícil es el orden correcto. |
| **EV1-035** | **CALIBRACIÓN** | El caso de exoneración (el instrumento debe emitir "ninguna primaria de sistema" ante un flip producido por tallado del juez). La disciplina de exoneración es el modo de falla más castigado en los gates previos (sobre-diagnóstico, gate #1) — se calibra, no se estrena en gate. Porta el caso juez (ii) `varianza_de_tallado`. |
| **EV1-042** | **GATE** | Espejo de EV1-031 (`completitud_kg` por chunk perdido) en OTRO TO (Exterior) y otra familia de pregunta (puntual con abstención): mide generalización del mecanismo calibrado, no memoria. |
| **EV1-015** | **GATE** | Segundo sabor de `completitud_kg` (criterio general ausente — BKL-0017 `ausencia` —, con captura del vecino 7.1): más difícil que el sabor chunk-perdido porque hay un vecino tentador que el instrumento debe descartar como no pertinente (test v2.2). Vara escueta: la regla de acierto de abajo la ancla en la evidencia commiteada de C1. |
| **EV1-029** | **GATE** | El caso B′ (la laguna documentada) + el caso juez (i) `abstencion_aprobada`. Va al gate por la pista del mandato evaluada así: los dos casos de juez son SUBTIPOS DISTINTOS — calibrar con uno NO enseña el otro (tallado ≠ abstención), así que "calibrar con uno y gatear con el otro" no da simetría real; lo que sí da es cobertura: el subtipo (ii) se calibra (EV1-035) y el subtipo (i) queda en gate montado sobre el caso B′, con su regla de acierto restringida a lo que el instrumento puede ver (la falla de r3). Asimetría declarada, no resuelta. |

**Agregado del laudo (2026-08-02): EV1-039 entra al GATE como G-4** — la mitigación que
esta propuesta dejaba disponible se ejerció: el casillero causal quedó laudado
(`contenido_kg`, quimera de tabla RX-10, evidencia BKL-0006) y el gate gana la familia
de contenido sin tocar la calibración. Vara, traza pre-registrada y regla de acierto:
`docs/protocolo_gate_u5.md` §3, G-4.

**Clases que quedan SIN representación en gate** (disclosure, actualizado al laudo):
la exoneración (`sin_defecto` / sin primaria) queda solo en calibración — el material
tiene UN solo ejemplar (EV1-035) y no se puede partir; y siguen sin ejemplar en toda la
familia `provenance_imprecisa`, `estructural_kg`, `navegación`, `alucinacion_agente`,
`aplicacion_erronea` y `frontera_no_determinada` (`expediente_material.md` §4; la
reserva restante sin causa — EV1-005, EV1-011, EV1-028 — no entra, laudo §4 del
protocolo).

**Criterio (c) del mandato — quemado:** todo lo que entre a calibración queda **QUEMADO**
(EV1-031, EV1-018, EV1-035, con sus trazas de ambos brazos): no sirve como re-test ni
objetivo de ninguna iteración futura de ningún componente. Los casos de gate quedan
quemados al correrse el gate (regla del ciclo 2). Registro formal del quemado: en el
protocolo (`docs/protocolo_gate_u5.md` §7) y, tras el laudo, en el tablero.

**Universo de casos-traza (pre-registro del insumo exacto):** el verificador consume UNA
traza por caso (`load_rep(label, run, qid)`). Propuesta de traza por caso (la lauda la
autora): para los casos v2 de la corrida 26/07, la réplica de menor índice cuya falla
porta el síntoma adjudicado (`escalon1_r1/grafo_v2/<qid>.json`, salvo indicación en el
caso); para EV1-029 la falla es `escalon1b_r3/reensamblado_v3/EV1-029.json` (la única
réplica incorrecta del brazo v3); para EV1-035 la falla es
`escalon1b_r1/reensamblado_v3/EV1-035.json` (la réplica tallada central-falsa).

---

## 2. Los calibradores (ejemplos resueltos completos, formato de vara del ciclo 2)

> Adjudicaciones transcriptas de los veredictos humanos sellados
> (`fichas_fallas_v2.json`, `fichas_delta_1b.json`, `docs/lectura_escalon1b.md` §5);
> ramas y reglas de acierto: PROPUESTAS de esta unidad, para laudo.

### CAL-1 · EV1-031 — `puntual` · TO: capitales · brazo grafo_v2 · clase: {context_recall, completitud_kg}

**1. Perfil y síntoma.** Pregunta: "En el marco de las exposiciones minoristas
normativas, ¿cuál es la exposición máxima admitida frente a una misma persona humana por
cartera para consumo al momento del acuerdo?" (GT: Punto 2.8.3.3). En v2: incorrecta
3-0, `hit_tool_limit` ×3 (15/15/16 pasos). Respuestas: dos evasivas que ofrecen límites
ajenos (0,2% / 1%) y declaran "el Knowledge Graph no contiene información específica";
una tercera que afirma el 0,2% como si fuera la respuesta (claims centrales `falso` ×2).
Traza del caso: `posthoc_run/traces/escalon1_r1/grafo_v2/EV1-031.json`.

**2. Ramas pre-registradas.** Por pata única: (A) completitud_kg — el dato (75 SMVM,
2.8.3.3) no existe en v2; (B) alcanzabilidad_kg — existe y no rankea; (C) navegación —
existe, alcanzable, no abierto; (D) el 0,2%/1% afirmado en r3: ¿contenido de otro alcance
aplicado (aplicacion_erronea) / FP del juez?

**3. Exposición (resuelta — qué debe encontrar el verificador).**
- **El dato de la clave NO existe en el grafo v2:** la predicción sellada del mapeo
  (`6c24009` §C) lo declara "dato de la clave **nuevo en v3** desde chunk recuperado", y
  la verificación mecánica de la ficha delta lo confirma: el portador
  `Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar_61edfb`
  existe en v3 (consultado vía `ver_nodo` en las 3 réplicas de v3, presente en las
  citas) y no tiene contraparte en v2. La constancia de búsqueda del propio verificador
  (campo `busquedas`, obligatorio para completitud) debe dar vacío sobre v2 para "75",
  "SMVM"/"Salario Mínimo Vital y Móvil" y el contenido del 2.8.3.3.
- **Los límites 0,2% y 1% que las respuestas ofrecen son datos reales de OTRO alcance**
  (nodos de exposiciones minoristas efectivamente consultados —
  `Restriccion_a_la_fecha_de_corte_el_monto_total_de_las_exposiciones_a_un_deudor_en_particular`,
  paso 5—): el relleno con material no pertinente NO cambia el síntoma de la pata
  (regla de precedencia C1a: pata sin dato pertinente → context_recall aunque haya
  relleno).
- **La conducta del agente fue honesta ante el hueco** en r1/r2 ("el KG no contiene…"):
  constatarlo es evidencia de lado grafo, no un campo vacío (FASE A, A3).

**4. VEREDICTO (vara sellada 26/07): {context_recall, completitud_kg}** — "dato no
alcanzado (evasivas: dato real ajeno + 'el KG no contiene'); hit_tool_limit ×3", con el
mecanismo de producción (chunk perdido en el ensamblado de v2) anotado como sub-especie
de lectura externa (`brechas_taxonomia.md` §1).

### CAL-2 · EV1-018 — `enumerativa` · TO: exterior · brazo grafo_v2 · clase: {context_recall, alcanzabilidad_kg}

**1. Perfil y síntoma.** Pregunta: "¿Para qué operaciones deben contar las entidades
financieras y las empresas no financieras emisoras de tarjetas locales con la conformidad
previa del BCRA…?" (GT: Punto 4.1.4). En v2: incorrecta 3-0, réplicas cortas (3/4/4
pasos, sin tope). Las tres respuestas REPITEN LA PREMISA de la pregunta ("deben contar
con la conformidad previa del BCRA para acceder al mercado de cambios… por el uso de
dichas tarjetas o cualquier modalidad que implique un débito inmediato…") sin listar
operación alguna del 4.1.4; claim central `no_soportado` en las tres. Traza:
`posthoc_run/traces/escalon1_r1/grafo_v2/EV1-018.json`.

**2. Ramas pre-registradas.** (A) completitud_kg — las operaciones del 4.1.4 no están
nodificadas; (B) alcanzabilidad_kg — están nodificadas y ninguna búsqueda razonable las
trae; (C) navegación — alcanzables y no abiertas (ojo: solo 3-4 pasos por réplica, hay
que probar si MÁS búsquedas razonables las traían); (D) sin_defecto — la respuesta era
correcta y el juez erró.

**3. Exposición (resuelta).**
- **El dato ESTÁ nodificado y ningún agente de ningún brazo lo alcanzó** (vara sellada:
  "alcanzabilidad compartida (H1 — dato nodificado en ambos brazos, no alcanzado por
  ningún agente)" — la hipótesis H1 del deslinde 27/07 abarca también a run_3, que
  falló igual). El verificador debe EXHIBIR el/los portador/es del 4.1.4 (quote de
  contenido, no de label) y aportar la constancia de búsqueda: con los términos de la
  pregunta ("conformidad previa", "tarjetas locales", "pagos al exterior") el portador
  no entra al corte; se alcanza con vocabulario propio del nodo.
- **El agente abrió solo el nodo de la premisa**
  (`Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc`,
  paso 3 de las tres réplicas) — fiel pero no pertinente a la enumeración pedida.
- **Cuidado pre-registrado:** con réplicas de 3-4 pasos, la frontera con `navegación`
  exige la prueba de alcanzabilidad ex ante completa (v2.1) hecha POR el verificador
  (simular las búsquedas razonables), no inferida de la brevedad de la traza.

**4. VEREDICTO (vara sellada 26/07, corregida 27/07): {context_recall,
alcanzabilidad_kg}** — no-respuesta por portador nodificado inalcanzado en ambos brazos.

### CAL-3 · EV1-035 — `condicional` · TO: capitales · brazo reensamblado_v3 (falla: r1) · clase: EXONERACIÓN (sin primaria de sistema)

**1. Perfil y síntoma.** Pregunta: "¿Puede considerarse normativa una exposición con
garantía hipotecaria cuando el inmueble que la garantiza todavía está en construcción?"
(GT: Punto 2.9.2.2). Seis respuestas casi idénticas entre ambos brazos (v2 2-1 correcta →
v3 2-1 incorrecta); la falla a investigar es v3·r1 (9 pasos): claims de la excepción del
2.9.2.2 — `falso`/central "La excepción aplica siempre que se trate de construcción de
hasta 4 unidades para vivienda", `falso`/no-central la extensión al ente con potestad
legal. Traza: `posthoc_run/traces/escalon1b_r1/reensamblado_v3/EV1-035.json`.

**2. Ramas pre-registradas.** Por claim reprobado: ¿contenido_kg (el nodo Excepcion
enuncia mal las condiciones) / alucinacion_agente (el agente recortó condiciones que el
nodo sí tiene) / sin_defecto (FP del juez)? Por pata: ¿alcanzabilidad de la Excepcion?

**3. Exposición (resuelta).**
- **El grafo queda exonerado por sus propias trazas** (vara sellada): mismos nodos
  consultados en ambos brazos (`cruce_trazas_v2_v3` de la ficha:
  `Excepcion_excepcion_para_inmuebles_en_construccion[_362c92]`,
  `Restriccion_exposicion_garantizada_por_inmueble_terminado[_e4a6e8]`), alcanzabilidad
  intacta (la Excepcion consultada en v3 pese a rank 28), y las seis respuestas comparten
  el mismo defecto de borde (condiciones de la excepción mal enunciadas) — es decir: el
  MISMO sistema produjo respuestas aprobadas y reprobadas; lo que cambió entre réplicas
  fue el TALLADO del juez (la misma familia de claims tallada central-falsa en r1,
  no-central en r3, no tallada en r2/v2).
- **Lo que el instrumento actual puede y debe emitir:** ninguna primaria de sistema. Los
  claims tallados resuelven por el árbol a la rama de exoneración o quedan por debajo del
  umbral de primaria (regla de jerarquía v2.6: si los centrales fallidos son ruido del
  juez, el caso no tiene primaria). La etiqueta `falla_de_juez/varianza_de_tallado` es de
  LECTURA EXTERNA (`brechas_taxonomia.md` §2), no del contrato del verificador.
- **Cuidado pre-registrado:** el "defecto de borde" compartido es real pero NO tiene
  adjudicación fina de lado en esta familia; emitirlo como SECUNDARIA documentada no
  invalida la exoneración; emitirlo como PRIMARIA sí la invalida.

**4. VEREDICTO (vara sellada 31/07): EXONERACIÓN — regresión no atribuible al sistema
(grafo exonerado por trazas; flip producido por varianza de tallado del juez).** Caso
juez (ii) del expediente §5 del 1b.

### Reglas de acierto de los calibradores (para el loop de comparación externa)

| Caso | Acierto = | Nota |
|---|---|---|
| CAL-1 (EV1-031) | `{context_recall, completitud_kg}` como primaria, con `busquedas` no vacías | `alcanzabilidad_kg` o `navegación` = miss (el portador NO existe en v2); atribuir defecto por el relleno 0,2%/1% como primaria = miss |
| CAL-2 (EV1-018) | `{context_recall, alcanzabilidad_kg}` como primaria, exhibiendo el portador (quote de contenido) + constancia de búsqueda | `completitud_kg` = miss (el dato está nodificado); `navegación` = miss solo si el verificador no aporta la simulación ex ante — si la aporta y da alcanzable, es hallazgo para revisión humana, no acierto |
| CAL-3 (EV1-035) | NINGUNA primaria de sistema (exoneración sostenida) | cualquier primaria confiada = miss (el modo de falla sobre-diagnóstico); secundaria documentada del borde no invalida |

---

## 3. Constancia de quemado (laudo 2026-08-02)

**EV1-031, EV1-018 y EV1-035 están QUEMADOS desde el laudo del 2026-08-02** como
material de calibración de la familia v2/v3 (con sus trazas de ambos brazos y sus
fichas): no sirven como re-test ni objetivo de ninguna iteración futura de ningún
componente, en la misma lista de territorio quemado que EV1/CQ/CQN/CQN2 ya integran a
nivel de eval sets. **EV1-042, EV1-015, EV1-029 y EV1-039 (G-4, agregado por el mismo
laudo) quedan reservados para el gate y se queman al correrse**
(`docs/protocolo_gate_u5.md` §7).
