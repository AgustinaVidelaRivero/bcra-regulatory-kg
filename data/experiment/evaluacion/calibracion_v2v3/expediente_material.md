# Expediente del material — re-calibración del verificador sobre la familia v2/v3 (U5-PREP)

**Fecha:** 2026-08-02. **Unidad:** U5-PREP (preparación; la corrida es otra unidad; los
laudos son de la autora). **Alcance:** inventario completo del material de la familia
v2/v3 (grafo_v2 / reensamblado_v3) con veredicto causal humano, su mapeo a la taxonomía
v2.6.1 del verificador y su riqueza como calibrador.

**Fuentes (todo verbatim de archivos commiteados):**
- `data/experiment/evaluacion_escalon1/corridas/fichas_fallas_v2.json` (9 fichas, corrida 26/07).
- `data/experiment/evaluacion_escalon1/corridas/fichas_delta_1b.json` (4 fichas delta completas
  + 5 breves en la clave `cambios_de_patron_sin_cambio_de_mayoria`).
- `docs/lectura_escalon1b.md` §5 (expediente del juez: 2 casos).
- Catálogo v2.6.1: `.claude/skills/kg-refinement/references/taxonomia.md` (el rango que el
  prompt ensambla por referencia: Capa 1 con precedencia, tablas de Capa 2, árbol).
- Trazas íntegras (con `raw_turns_agent`, outputs completos re-ejecutables):
  `data/experiment/evaluacion/posthoc_run/traces/escalon1_r{1,2,3}/grafo_v2/EV1-*.json` (corrida 26/07)
  y `posthoc_run/traces/escalon1b_r{1,2,3}/{grafo_v2,reensamblado_v3}/EV1-*.json` (corrida 1b).

**CONTRADICCIÓN MANDATO↔ARCHIVOS (se reporta, regla d del circuito):** el mandato de la
unidad describe "las 9 de fichas_fallas_v2.json" como fichas "con veredicto causal humano
sellado". El archivo dice otra cosa: su `nota` declara "6 originales con falla ratificada
por adjudicación humana del 26/07 (**atribución causal pendiente**) + 3 adjudicadas con
causa (EV1-015, EV1-031, EV1-018)". Seis de las nueve tienen veredicto humano **de
síntoma** (la falla es real), no **de causa**. El expediente las inventaría igual, con esa
distinción explícita: sin causa sellada no pueden ser vara de atribución (ni calibrador ni
gate) hasta que la autora las adjudique.

---

## 1. Tabla de inventario

| # | Entrada | Origen | Veredicto causal | Mapeo v2.6.1 HOY | ¿Elegible como vara causal? |
|---|---|---|---|---|---|
| 1 | EV1-005 (v2) | fichas_fallas_v2 | síntoma ratificado; causa PENDIENTE | — (sin causa que mapear) | NO (hasta laudo) |
| 2 | EV1-011 (v2) | fichas_fallas_v2 | síntoma ratificado; causa PENDIENTE | — | NO (hasta laudo) |
| 3 | EV1-015 (v2) | fichas_fallas_v2 | SELLADO (26/07) | `{context_recall, completitud_kg}` (vía BKL-0017 `ausencia`) | SÍ |
| 4 | EV1-018 (v2) | fichas_fallas_v2 | SELLADO (26/07, corr. 27/07) | `{context_recall, alcanzabilidad_kg}` | SÍ |
| 5 | EV1-028 (v2) | fichas_fallas_v2 | síntoma ratificado; causa PENDIENTE | — | NO (hasta laudo) |
| 6 | EV1-029 (v2) | fichas_fallas_v2 | causa PENDIENTE en esta ficha (sellada después en la delta, fila 10) | — (ver fila 10) | vía fila 10 |
| 7 | EV1-031 (v2) | fichas_fallas_v2 | SELLADO (26/07) | `{context_recall, completitud_kg}` | SÍ |
| 8 | EV1-039 (v2) | fichas_fallas_v2 | síntoma ratificado; causa PENDIENTE | — (nota: territorio de BKL-0006 `quimera`) | NO (hasta laudo) |
| 9 | EV1-042 (v2) | fichas_fallas_v2 | causa PENDIENTE en esta ficha (sellada después en la delta, fila 12) | — (ver fila 12) | vía fila 12 |
| 10 | EV1-029 (delta) | fichas_delta_1b | SELLADO (laudo de válvula, 31/07) | **SIN CLASE limpia** (colapso alcanzabilidad_kg↔navegación; mecanismo B′) | SÍ, con la brecha declarada |
| 11 | EV1-031 (delta) | fichas_delta_1b | SELLADO (predicción sellada + verificación mecánica) | `{context_recall, completitud_kg}` (lado v2) | SÍ (refuerza fila 7) |
| 12 | EV1-042 (delta) | fichas_delta_1b | SELLADO (predicción sellada + verificación mecánica) | `{context_recall, completitud_kg}` (lado v2) | SÍ |
| 13 | EV1-035 (delta) | fichas_delta_1b | SELLADO (laudo de válvula, 31/07) | **SIN CLASE** (falla del instrumento juez, no del sistema; lo más cercano: exoneración `sin_defecto`) | SÍ, con la brecha declarada |
| 14 | Juez (i): abstención-aprobada | lectura_escalon1b §5 (ficha de origen: EV1-029 delta, r1 de ambos brazos) | SELLADO | **SIN CLASE** (falso negativo del juez; `sin_defecto` solo cubre falsos positivos) | material de juez, no de verificador (ver §4) |
| 15 | Juez (ii): varianza de tallado | lectura_escalon1b §5 (ficha de origen: EV1-035 delta) | SELLADO | **SIN CLASE** (ídem fila 13) | SÍ, como caso de exoneración |

Las 5 fichas breves de patrón se listan en §3: **ninguna califica como material** (motivo
por ficha).

---

## 2. Detalle por entrada

Convención: "causa sellada" se cita VERBATIM del campo `veredicto_causal` del JSON
correspondiente. "Riqueza" = qué trae la ficha + qué trae la traza persistida (la ficha
lleva `traza_tools` solo con inputs; los outputs completos viven en la traza de
`posthoc_run/traces/` y son re-ejecutables con `ver_paso_completo`).

### EV1-005 (v2) — enumerativa · RI · GT Punto 7.1

- **Causa sellada:** "falla ratificada por adjudicación humana (26/07); atribución causal
  pendiente de la autora".
- **Mapeo v2.6.1:** ninguno posible todavía (no hay causa que mapear).
- **Riqueza:** 3 réplicas casi idénticas (3 pasos cada una, sin tope de tools), respuesta
  con RPC + franquicia marcadas `falso` (2+1+2 claims), un solo `ver_nodo`
  (`Obligacion_para_el_calculo_del_importe_correspondiente_al_mes_n_procedera_tenerse_en_cuenta`).
  Traza completa en `posthoc_run/traces/escalon1_r{1,2,3}/grafo_v2/EV1-005.json`. Caso
  compacto y estable (3-0), bueno como vara futura SI la autora adjudica causa.

### EV1-011 (v2) — enumerativa · Clasificación · GT Puntos 6.5–6.5.5

- **Causa sellada:** "falla ratificada por adjudicación humana (26/07); atribución causal
  pendiente de la autora".
- **Mapeo v2.6.1:** pendiente. (Observación no vinculante para el laudo: las respuestas
  mezclan niveles de consumo con cartera comercial y citan "Punto 7.2" junto al 6.5 —
  patrón compatible con des-scoping, precedente off/run_1/CQ-018 del dev set; la
  clasificación es de la autora.)
- **Riqueza:** 3 réplicas de 15 pasos con `hit_tool_limit` ×3, 12 claims fallidos en
  total, múltiples nodos abiertos. Traza completa disponible. Caso rico pero SIN causa.

### EV1-015 (v2) — sujeto · Clasificación · GT Punto 1.1

- **Causa sellada:** "adjudicada (26/07): el 1.1 no alcanzado, capturado el vecino 7.1 —
  las réplicas niegan/eluden el dato que la key afirma; hit_tool_limit presente (ver
  réplicas)".
- **Mapeo v2.6.1:** `{context_recall, completitud_kg}`. Fundamento del casillero: el
  criterio general 1.1 estaba AUSENTE del grafo — BKL-0017 (especie `ausencia` en
  `data/backlog/backlog.jsonl`) lo restauró en el vigente vía C1
  (`data/backlog/retests/C1_retest_2026-07-31.md`); en el grafo congelado de la corrida el
  dato no existía, así que "no alcanzado" resuelve por el árbol a "No existe →
  completitud_kg". El mecanismo de producción del hueco (pérdida en el ensamblado) queda
  para `brechas_taxonomia.md` §1.
- **Riqueza:** ALTA. 3 réplicas (16/15/14 pasos, `hit_tool_limit` en 2), 25 claims
  fallidos, captura del vecino 7.1 documentada en respuestas y citas, y evidencia externa
  de la ausencia ya commiteada (expediente C1). Traza completa disponible.

### EV1-018 (v2) — enumerativa · Exterior · GT Punto 4.1.4

- **Causa sellada:** "adjudicada (26/07, corregida post-deslinde 27/07): no-respuesta —
  repiten la premisa sin listar operación alguna del 4.1.4; alcanzabilidad compartida (H1
  — dato nodificado en ambos brazos, no alcanzado por ningún agente)".
- **Mapeo v2.6.1:** `{context_recall, alcanzabilidad_kg}` — la clase existente cubre: el
  dato está nodificado (existe portador) y ningún agente de ningún brazo lo alcanzó.
- **Riqueza:** MEDIA. 3 réplicas cortas (3/4/4 pasos), 3 claims, respuestas casi
  idénticas que repiten la premisa. La evidencia de ranks del portador NO está en la
  ficha (la hipótesis H1 remite al deslinde del 27/07); para redactar la regla de acierto
  hay que exhibir el portador y sus ranks desde la traza/el índice, cosa que el propio
  verificador puede hacer con sus tools. Traza completa disponible.

### EV1-028 (v2) — sujeto · Protección · GT Punto 1.1.2.5

- **Causa sellada:** "falla ratificada por adjudicación humana (26/07); atribución causal
  pendiente de la autora".
- **Mapeo v2.6.1:** pendiente.
- **Riqueza:** 3 réplicas (10/9/9 pasos), 4 claims, nodos de PNFC y rol sujeto-obligado
  abiertos. Traza completa disponible. SIN causa.

### EV1-029 — sujeto · Protección · GT Puntos 1.1.1 y 3.1.1.1 (ficha v2 pendiente; delta SELLADA)

- **Causa sellada (delta, verbatim del laudo de válvula):** "Acierto real; caso de
  ALCANZABILIDAD, la tercera clase taxonómica del proyecto (existe pero inalcanzable): el
  nodo …997afd existía en v2 con descripción idéntica y provenance idéntica, pero bajo
  las 11 queries reales del agente v2 nunca entró al corte de 10 (mejores ranks 16 y 19).
  En v3 fue alcanzado; mecanismo verificado en la traza de r2: RAMA C — exposición por
  query directa en el paso 3 ('responsable consultas reclamos deudor cedido', rank 6 de
  10; ver_nodo directo del nodo en el paso 4); el 2×2 contrafáctico muestra que la misma
  query habría rendido rank 7 (≤10) sobre el índice de v2, y que la recomposición del
  índice deja los ranks del nodo esencialmente iguales entre brazos (16/19→16/21 en las
  queries de v2; 7→6 en la decisiva) — la query es nueva de la trayectoria de v3, no un
  desentierro del índice. La conversión no es atribuible al fix; se registra como
  varianza de trayectoria sobre material presente en ambos brazos. El mapeo la había
  clasificado no_recuperable_por_v3; la válvula atrapó el error de casillero (correspondía
  alcanzabilidad, cuya predicción era mejora_posible_no_garantizada). Caveat registrado:
  las réplicas r1 de AMBOS brazos son abstenciones aprobadas como correcta por el juez
  (patrón 'evasiva aprobada', precedente run_3/EV1-007), no flaggeadas y no re-abiertas
  por simetría; defecto del juez registrado para U5."
- **Mapeo v2.6.1:** **SIN CLASE limpia.** El laudo dice "alcanzabilidad" en el
  vocabulario del proyecto, pero la definición v2.6.1 de `alcanzabilidad_kg` exige que
  "ninguna búsqueda razonable desde los términos de la pregunta lo devuelve" y que "solo
  se alcanza con palabras del propio nodo" — y la evidencia de ranks muestra lo
  contrario: una query razonable del vocabulario de la pregunta ('responsable consultas
  reclamos deudor cedido') lo rankea 7 en el índice de v2. Tampoco es `navegación`
  limpia: las 11 queries reales del agente v2 eran razonables y dejaron el portador en
  ranks 16/19 (match positivo FUERA del corte de 10). Es el mecanismo B′
  (entierro-por-ranking), la laguna ya documentada del instrumento
  (`docs/casos_gate_cqn2.md`, caso CQN2-015: "D2 no distingue el entierro-por-ranking de
  la inalcanzabilidad léxica"). Análisis completo en `brechas_taxonomia.md` §3.
- **Riqueza:** MÁXIMA del expediente. Ficha delta con réplicas de ambos brazos
  (`replicas` v3 + `replicas_v2_referencia`), `cruce_trazas_v2_v3` con nodos consultados
  por brazo, evidencia de ranks del 2×2 contrafáctico citada en el laudo, y trazas
  completas en `posthoc_run/traces/escalon1b_r{1,2,3}/{grafo_v2,reensamblado_v3}/EV1-029.json`.
  Además porta el caso (i) del expediente del juez (fila 14).

### EV1-031 — puntual · Capitales · GT Punto 2.8.3.3 (v2 SELLADA + delta SELLADA)

- **Causa sellada (v2, 26/07):** "adjudicada (26/07): dato no alcanzado (evasivas: dato
  real ajeno + \"el KG no contiene\"); hit_tool_limit ×3".
- **Causa sellada (delta, 31/07):** "PREDICCIÓN SELLADA (mapeo 6c24009 §C):
  acierto_nuevo_esperado — 'dato de la clave nuevo en v3 desde chunk recuperado,
  alcanzable por 7/11 queries históricas'. VERIFICACIÓN MECÁNICA (esta unidad): el nodo
  predicho Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar_61edfb
  fue consultado vía ver_nodo en las 3 réplicas de v3 y aparece en las citas; ver
  evidencia_prediccion en esta ficha. Nada más se escribe: la lectura causal completa es
  de la discusión."
- **Mapeo v2.6.1:** `{context_recall, completitud_kg}` para el brazo v2 — el dato de la
  clave (75 SMVM, Punto 2.8.3.3) NO existía en el grafo v2 (es "nuevo en v3 desde chunk
  recuperado"); las evasivas del agente ("el KG no contiene") son la conducta esperada
  ante el hueco. El árbol resuelve: pata sin dato → context_recall → "No existe →
  completitud_kg". Mecanismo de producción (chunk perdido en el ensamblado):
  `brechas_taxonomia.md` §1.
- **Riqueza:** MÁXIMA. Doble sello independiente (adjudicación 26/07 + predicción
  pre-registrada del mapeo verificada mecánicamente), ficha delta con ambos brazos,
  `evidencia_prediccion` y `nodos_predichos_por_el_mapeo` en la ficha, contraste limpio
  v2 3-0 incorrecta → v3 3-0 correcta. Trazas completas de ambas corridas.

### EV1-035 (delta) — condicional · Capitales · GT Punto 2.9.2.2

- **Causa sellada (verbatim del laudo de válvula):** "Regresión NO atribuible al delta de
  ensamblado; el grafo queda exonerado por sus propias trazas: mismos nodos consultados
  en ambos brazos, alcanzabilidad intacta (la Excepcion consultada en v3 pese a rank 28),
  seis respuestas casi idénticas que comparten el mismo defecto de borde (condiciones de
  la excepción del 2.9.2.2 mal enunciadas). Mecanismo: varianza de descomposición del
  juez sobre un caso frontera — la misma familia de claims fue tallada como central-falsa
  (r1), no-central (r3) o no tallada, y el veredicto final dependió del tallado; canal
  explícitamente declarado fuera del alcance del screen en §E del mapeo. Nota: el laudo
  sellado run_3/EV1-035 ('excepción enunciada sin sus condiciones esenciales —
  sobre-ampliación') indica que las correctas de v2 en este caso eran suerte del tallado.
  Vocabulario del screen afinado: 'estable' declara alcanzabilidad estable, no veredicto
  estable. Caso completo registrado como insumo de calibración del juez (U5)."
- **Mapeo v2.6.1:** **SIN CLASE.** La causa del flip de veredicto es del instrumento juez
  (varianza de tallado entre réplicas), no del grafo ni del agente. Lo más cercano en el
  catálogo es la exoneración `sin_defecto` ("posible falso positivo del juez", lado
  ninguno) aplicada claim a claim — pero eso nombra el efecto por claim, no el mecanismo
  del instrumento; y el "defecto de borde" compartido de las seis respuestas (condiciones
  de la excepción mal enunciadas) quedó sin adjudicación fina de lado en esta familia.
  Análisis en `brechas_taxonomia.md` §2.
- **Riqueza:** ALTA como caso de exoneración/juez: seis respuestas casi idénticas con
  veredictos divergentes por tallado, ambos brazos en la ficha, rank 28 de la Excepcion
  documentado, antecedente run_3/EV1-035 sellado. Trazas completas de ambos brazos.

### EV1-039 (v2) — puntual · Capitales · GT Punto 1.2

- **Causa sellada:** "falla ratificada por adjudicación humana (26/07); atribución causal
  pendiente de la autora".
- **Mapeo v2.6.1:** pendiente. (Observación no vinculante: el GT es la tabla de montos
  del 1.2 — el territorio exacto de BKL-0006, especie `quimera`, RX-10 tabla linealizada,
  corregido en el vigente vía C2; las respuestas afirman "2.500 millones" para bancos
  donde la tabla del PDF dice 5.000. Si la autora adjudica, este caso agregaría al
  material la familia de contenido — hoy ausente. La clasificación es de la autora.)
- **Riqueza:** 3 réplicas (10/16/15 pasos, `hit_tool_limit` ×2), 10 claims, y expediente
  externo ya commiteado del defecto del nodo (C2, `data/backlog/retests/C2_retest_2026-07-31.md`).

### EV1-042 — puntual · Exterior · GT Punto 3.5.3 (ficha v2 pendiente; delta SELLADA)

- **Causa sellada (delta):** "PREDICCIÓN SELLADA (mapeo 6c24009 §C):
  acierto_nuevo_esperado — 'dato de la clave en 2 nodos nuevos de chunks recuperados,
  alcanzables por 3/7 queries históricas (cita imperfecta: locations RX-03)'.
  VERIFICACIÓN MECÁNICA (esta unidad): al menos uno de los 2 nodos predichos fue
  consultado vía ver_nodo en las 3 réplicas de v3; ver evidencia_prediccion. Nada más se
  escribe."
- **Mapeo v2.6.1:** `{context_recall, completitud_kg}` para el brazo v2 — mismo casillero
  y mismo fundamento que EV1-031 (dato ausente en v2, nuevo en v3 desde chunks
  recuperados). Con el matiz de calidad de cita (locations RX-03) ya declarado en el
  pre-registro.
- **Riqueza:** ALTA. Predicción sellada + verificación mecánica, ficha delta con ambos
  brazos y `evidencia_prediccion`, abstenciones honestas del agente v2 ("No se encontró
  en el Knowledge Graph…", `hit_tool_limit` ×3). Espejo estructural de EV1-031 con otro
  TO (Exterior) y otra familia de pregunta.

### Caso juez (i) — abstención-aprobada (ficha de origen: EV1-029 delta)

- **Veredicto sellado (`docs/lectura_escalon1b.md` §5):** "(i) abstención-aprobada —
  réplicas r1 de ambos brazos de EV1-029 aprobadas como correcta siendo abstenciones
  (patrón 'evasiva aprobada', precedente sellado run_3/EV1-007)". Precedente:
  `data/experiment/evaluacion_escalon1/acta_adjudicacion_EV1.md` ("EV1-007 | run_3 r3 →
  **incorrecta** (evasiva aprobada)").
- **Mapeo v2.6.1:** **SIN CLASE**, y además **estructuralmente fuera del universo de
  entrada del verificador**: es un falso NEGATIVO del juez (aprueba una no-respuesta);
  el verificador solo recibe fallas (respuestas que el juez marcó incorrectas), así que
  una abstención aprobada jamás llega a su bandeja. `sin_defecto` cubre el caso inverso
  (falso positivo). Análisis y consecuencias de diseño en `brechas_taxonomia.md` §2.
- **Riqueza:** las dos réplicas r1 (v2 y v3) están íntegras en la ficha delta de EV1-029
  y en `posthoc_run/traces/escalon1b_r1/{grafo_v2,reensamblado_v3}/EV1-029.json`, con la
  respuesta-abstención verbatim y el veredicto `correcta` del juez.

### Caso juez (ii) — varianza de tallado (ficha de origen: EV1-035 delta)

- **Veredicto sellado (`docs/lectura_escalon1b.md` §5):** "(ii) varianza de tallado —
  EV1-035, la misma familia de claims tallada distinto entre réplicas con el veredicto
  dependiendo del tallado".
- **Mapeo v2.6.1:** **SIN CLASE** (ver fila 13 y `brechas_taxonomia.md` §2). A diferencia
  del caso (i), este SÍ entra al universo del verificador: las réplicas talladas como
  central-falsa son fallas con síntoma, y el veredicto esperable del instrumento actual
  es la exoneración (`sin_defecto` sobre los claims tallados).
- **Riqueza:** la de EV1-035 (fila 13).

---

## 3. Las 5 fichas breves de patrón — listadas, con motivo de exclusión

Fuente: `fichas_delta_1b.json`, clave `cambios_de_patron_sin_cambio_de_mayoria`.
Registran solo `{id, patron_v2_v3, mayoria, replica_que_difiere}` — sin pregunta, sin
claims, sin trazas embebidas, sin veredicto causal.

| Id | Patrón v2→v3 | Réplica que difiere | ¿Sirve como material? |
|---|---|---|---|
| EV1-002 | 3-0 → 2-1 | r2 (correcta → incorrecta) | NO: mayoría correcta en ambos brazos — no hay falla de sistema que atribuir; el flip de réplica única no tiene veredicto causal humano. |
| EV1-010 | 2-1 → 3-0 | r2 (failed acarreada §8 en v2 → correcta) | NO: el delta es una traza fallida acarreada (`origen=sellado_escalon1_hueco_cache`, Enmienda §8 del protocolo 1b) — artefacto de corrida, no defecto de sistema ni de juez. |
| EV1-012 | 2-1 → 3-0 | r3 (incorrecta → correcta) | NO: mayoría correcta en ambos brazos; sin adjudicación causal de la réplica que difiere. |
| EV1-016 | 2-1 → 3-0 | r3 (failed acarreada §8 en v2 → correcta) | NO: mismo motivo que EV1-010. |
| EV1-036 | 3-0 → 2-1 | r3 (correcta → incorrecta por laudo humano 1b) | NO para U5 como vara del verificador (mayoría correcta; réplica única sin causa sellada). Anotación: al ser un flip producido POR laudo humano sobre veredicto del juez, es candidata natural a material de calibración DEL JUEZ si esa vía se abre — se deja registrada, sin dar por buena. |

Motivo común: el verificador atribuye causas de FALLAS de mayoría; ninguna de las cinco
es falla de mayoría en ningún brazo, y ninguna tiene causa humana sellada. Reutilizarlas
exigiría primero un laudo por réplica que hoy no existe.

---

## 4. Resumen de cobertura del material elegible

Con causa sellada hay **6 casos de sistema** (EV1-015, EV1-018, EV1-031, EV1-042,
EV1-029, EV1-035) **+ 2 casos de juez** montados sobre dos de ellos. Cobertura de clases
v2.6.1 que ese material ejerce:

- `completitud_kg` ×3 (EV1-015, EV1-031, EV1-042 — tres mecanismos de producción
  distintos: ausencia restaurada por C1, chunk perdido recuperado ×2).
- `alcanzabilidad_kg` ×1 limpia (EV1-018) + ×1 con brecha B′ (EV1-029).
- Exoneración (`sin_defecto`/sin primaria de sistema) ×1 (EV1-035), con el mecanismo juez
  SIN CLASE.
- **Sin ningún ejemplar en la familia v2/v3:** `contenido_kg` (candidato natural: EV1-039
  si se adjudica), `provenance_imprecisa`, `estructural_kg`, `navegación`,
  `alucinacion_agente`, `aplicacion_erronea`, `frontera_no_determinada`. Disclosure
  obligatorio para el split (`calibradores_v2v3.md` §1) y el gate
  (`docs/protocolo_gate_u5.md`).

Los 4 casos pendientes de causa (EV1-005, EV1-011, EV1-028, EV1-039) quedan como
**reserva adjudicable**: cada uno que la autora selle antes del gate puede ampliar la
cobertura de clases del gate sin tocar la calibración.
