# Protocolo pre-registrado — GATE U5: verificador sobre la familia v2/v3 (laudos incorporados, 2026-08-02)

> **Estado: laudos de la adjudicadora TOMADOS e incorporados (2026-08-02):** split
> ratificado con EV1-039 agregado como G-4; reglas de acierto ratificadas; criterio
> global laudado (§4); brechas por lectura externa (cero cambios a taxonomía, prompt,
> módulos o umbrales); esquema v2 NO se inyecta; tope doble laudado (§5); canal de
> abstenciones-aprobadas fuera de U5 (deuda en §7). Este protocolo se commitea ANTES de
> la corrida; la corrida no comienza hasta ese commit y es otra unidad. Esta unidad NO
> corre nada (USD 0).

## 1. Objeto

Los veredictos del verificador sobre la familia **v2/v3** (grafo_v2 / reensamblado_v3)
son hoy **exploratorios**: el instrumento fue validado contra cuatro varas humanas de la
familia run_3/run_1/run_5 (`docs/lectura_ciclo2.md` §6), nunca contra material v2/v3
(protocolo del escalón 1 §6: "el verificador no se corrió sobre v2"). **Si este gate
pasa, los veredictos del verificador sobre la familia v2/v3 ascienden de exploratorio a
validado**; si no pasa, siguen exploratorios y el resultado se reporta igual (ambos
gates de la historia del instrumento se reportan siempre juntos — precedente
`docs/protocolo_gate2.md` §1).

## 2. Configuración exacta a correr

**La columna ganadora del ciclo 2, sin tocar:** v7' = v6.2-D + S1 v0.4b
(`docs/lectura_ciclo2.md` §6: "v7' (v6.2-D + S1 v0.4b) queda como el instrumento del
proyecto").

- **Verificador v5.7 congelado** (`data/experiment/evaluacion/verificador.py`, hash
  sellado `084b2db8…` en `posthoc_run/dev_set/extraccion_h2h_ciclo2.md` §Sello), régimen
  `--n 3` con voto de mayoría, namespaces `cv=verificador-v5.7-rep{1,2,3}`.
- **Capa determinística v6.2-D** (`capa_deterministica_v62.py`, hash `d43f76b1…`) sobre
  las 3 reps.
- **S1 v0.4b** (`s1_fuentes_v04.py`, hash `ce423fab…`, `--n 3`, política conservadora)
  sobre la salida de la capa.
- **Todos los módulos del cluster congelado se IMPORTAN, jamás se editan** (zona sellada,
  CLAUDE.md §3). La guarda del paso 0 del ciclo 2 se replica: status limpio, vara =
  HEAD, hashes de los congelados idénticos al sello, cero diff.

**Config de familia v2/v3 (lo NUEVO — hallazgos de la arqueología, con sus decisiones de
diseño ya resueltas por la mecánica existente o derivadas a laudo):**

1. **Driver, no CLI:** la whitelist del CLI del verificador (`_parse_casos`,
   `verificador.py`) solo acepta labels `off|on` y rechaza `escalon1_r*`/`escalon1b_r*`.
   Igual que en los dos head-to-head del ciclo 2, la corrida usa un **driver que replica
   VERBATIM el loop del runner de `main()` en su rama `--n>1`** (`investigar_falla` +
   `agregar_voto`, namespaces intactos; nota de cableado de
   `extraccion_h2h_ciclo2.md`). El instrumento no se toca.
2. **Trazas de entrada:** compatibles con `load_rep` sin adaptación —
   `posthoc_run/traces/escalon1_r{1,2,3}/grafo_v2/EV1-*.json` (corrida 26/07) y
   `posthoc_run/traces/escalon1b_r{1,2,3}/{grafo_v2,reensamblado_v3}/EV1-*.json`
   (corrida 1b), con `raw_turns_agent`, `judge.step1/step2` y `trace.steps` verificados
   presentes.
3. **Territorio de S1 (guarda de dominio):** `tos_fuente` por pregunta leído de
   `data/experiment/evaluacion_escalon1/EV1_preguntas.json` (campo verificado presente
   en las 36 preguntas) — pasa por el parámetro `--eval-set`/equivalente del driver; el
   default del módulo (`eval_set_cqn.json`) NO aplica a esta familia.
4. **Esquema del grafo:** `build_falla_context` inyecta el esquema documentado SOLO para
   runs `run_3*`; para `grafo_v2`/`reensamblado_v3` el propio módulo declara
   explícitamente "No hay esquema documentado registrado para este grafo" y ordena
   inferir de las tools. **LAUDADO (2026-08-02): el esquema v2 NO se inyecta; rige la
   rama de esquema ausente.**
5. **Caché virgen verificable:** los namespaces de la corrida se computan sobre los
   graph_fingerprint de v2/v3, sobre los que no existe ninguna corrida previa del
   verificador (verificable pre-corrida en `cache/verificador.db`, consulta de
   namespaces por gfp — mismo chequeo que `protocolo_gate2.md` §2.d).
6. **Grafos congelados de la corrida:** los que produjeron las trazas (v2 y el v3
   pre-C1/C2 del 1b). El vigente (post-C1/C2) NO participa: el gate valida atribución
   sobre las fallas selladas, no el estado actual del grafo.

## 3. El gate: casos, vara sellada, reglas de acierto, ramas y válvula

**Casos (split RATIFICADO por laudo 2026-08-02, con EV1-039 agregado como G-4;
detalle en `data/experiment/evaluacion/calibracion_v2v3/calibradores_v2v3.md` §1):**
EV1-042, EV1-015, EV1-029, EV1-039. Traza exacta por caso (pre-registro del insumo):

| Caso | Traza (label/run/qid) | Clase esperada |
|---|---|---|
| G-1 · EV1-042 | `escalon1_r1/grafo_v2/EV1-042` | completitud_kg |
| G-2 · EV1-015 | `escalon1_r1/grafo_v2/EV1-015` | completitud_kg (sabor ausencia-restaurada) |
| G-3 · EV1-029 | `escalon1b_r3/reensamblado_v3/EV1-029` | alcanzabilidad_kg (mecanismo B′) |
| G-4 · EV1-039 | `escalon1_r1/grafo_v2/EV1-039` | contenido_kg (quimera de tabla, RX-10) |

**Distinción obligatoria (mandato de U5):** para cada caso, la **vara** es el veredicto
causal humano sellado VERBATIM (qué pasó de verdad); la **regla de acierto** es qué debe
EMITIR el instrumento para contar acierto — no son lo mismo, y la regla se escribe en el
vocabulario v2.6.1 que el instrumento puede emitir.

### G-1 · EV1-042

- **Vara sellada (verbatim, `fichas_delta_1b.json`):** "PREDICCIÓN SELLADA (mapeo
  6c24009 §C): acierto_nuevo_esperado — 'dato de la clave en 2 nodos nuevos de chunks
  recuperados, alcanzables por 3/7 queries históricas (cita imperfecta: locations
  RX-03)'. VERIFICACIÓN MECÁNICA (esta unidad): al menos uno de los 2 nodos predichos
  fue consultado vía ver_nodo en las 3 réplicas de v3; ver evidencia_prediccion. Nada
  más se escribe." (Lado v2: el dato no existía — por eso es "nuevo en v3".)
- **REGLA DE ACIERTO:** el voto emite **`{context_recall, completitud_kg}` como primaria
  única**, con campo `busquedas` no vacío.
- **Ramas pre-registradas:** (i) acierto (la regla); (ii) miss-nombrado:
  `alcanzabilidad_kg` o `navegación` (el portador no existe en v2 — miss); (iii) triage
  (voto dividido o flags de capa/S1) — se lee con su motivo; (iv) exoneración o
  `sin_defecto` — miss.
- **Válvula:** cualquier resultado fuera de (i)-(iv) — p. ej. `formato_invalido`
  persistente, primaria de una clase no contemplada — DETIENE la lectura del gate hasta
  discusión; no se improvisa casillero.

### G-2 · EV1-015

- **Vara sellada (verbatim, `fichas_fallas_v2.json`):** "adjudicada (26/07): el 1.1 no
  alcanzado, capturado el vecino 7.1 — las réplicas niegan/eluden el dato que la key
  afirma; hit_tool_limit presente (ver réplicas)". Ancla adicional commiteada: BKL-0017
  (especie `ausencia`; el criterio 1.1 no existía en el grafo congelado — restaurado
  después vía C1, `data/backlog/retests/C1_retest_2026-07-31.md`).
- **REGLA DE ACIERTO:** el voto emite **`{context_recall, completitud_kg}` como
  primaria**, y NO atribuye primaria por los claims del vecino 7.1 (relleno no
  pertinente de la pata; emitirlos como secundarias o notas no invalida).
- **Ramas pre-registradas:** (i) acierto; (ii) miss-nombrado: `alcanzabilidad_kg` /
  `navegación` (exigiría exhibir un portador del 1.1 que en ese grafo no existe);
  (iii) primaria montada sobre el 7.1 (p. ej. `aplicacion_erronea` como primaria) —
  miss; (iv) triage con motivo.
- **Válvula:** ídem G-1. Además, si el verificador EXHIBE un portador del criterio 1.1
  en el grafo congelado (contradiría la especie `ausencia` de BKL-0017), la lectura se
  detiene: eso es una discrepancia de archivo, no un miss.

### G-3 · EV1-029

- **Vara sellada (verbatim, `fichas_delta_1b.json`; extracto — el texto completo rige):**
  "caso de ALCANZABILIDAD […]: el nodo …997afd existía en v2 con descripción idéntica y
  provenance idéntica, pero bajo las 11 queries reales del agente v2 nunca entró al
  corte de 10 (mejores ranks 16 y 19). […] Caveat registrado: las réplicas r1 de AMBOS
  brazos son abstenciones aprobadas como correcta por el juez (patrón 'evasiva
  aprobada', precedente run_3/EV1-007), no flaggeadas y no re-abiertas por simetría;
  defecto del juez registrado para U5." La falla que se investiga es v3·r3 (réplica
  incorrecta: el agente atribuyó la atención al fiduciario; claim central `falso`).
- **REGLA DE ACIERTO (restringida a lo que el instrumento puede ver — la brecha B′ y el
  caso juez (i) son de lectura externa, `brechas_taxonomia.md` §2-§3):** el voto emite
  como primaria de la pata del responsable **`{context_recall, alcanzabilidad_kg}`**
  exhibiendo el portador `Obligacion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid_997afd`
  (quote de contenido) con constancia de búsqueda, **o** la clave equivalente con el
  portador exhibido y evidencia de ranks (la vara acepta la clave, no exige nombrar el
  mecanismo B′ — precedente CQN2-015: "acierto = la clave, no el mecanismo").
- **Ramas pre-registradas:** (i) acierto; (ii) **rama de lectura (ni acierto ni miss
  silencioso):** `{context_recall, navegación}` CON la simulación ex ante aportada —
  es la manifestación documentada de la laguna B′ y se deriva a revisión humana con ese
  rótulo; (iii) miss-nombrado: `completitud_kg` (el portador SÍ existe) o primaria por
  claims no centrales; (iv) triage con motivo.
- **Válvula:** ídem G-1; además, si alguna rep del verificador intenta adjudicar las
  réplicas r1 (abstenciones aprobadas — fuera de su bandeja), la lectura lo registra
  como hallazgo y sigue, sin contarlo en el score.

### G-4 · EV1-039

- **Vara sellada (verbatim, `fichas_fallas_v2.json`):** "falla ratificada por
  adjudicación humana (26/07); atribución causal pendiente de la autora". **El
  casillero causal queda LAUDADO por el destrabe del 2026-08-02** (contenido_kg), sobre
  la evidencia RX-10/BKL-0006 ya commiteada:
  - **El PDF como árbitro** (`data/backlog/propuestas/C2_montos_12.md`): tabla del
    punto 1.2 de `TO_capitales_minimos_actual.pdf`, página 4, extraída
    estructuralmente — **Bancos ↔ 5.000 · Restantes entidades (salvo Cajas de Crédito
    Cooperativas) ↔ 2.500** (en millones de pesos); y a continuación: "Las compañías
    financieras que realicen, en forma directa, operaciones de comercio exterior
    deberán observar las exigencias establecidas para los bancos."
  - **El chunk crudo que produjo la inversión** (mismo documento): el texto plano del
    chunk del caché (`TO_capitales_minimos_actual.pdf::1.2`, 343 chars) porta la
    linealización viciada «Restantes entidades / Bancos / (salvo Cajas de Crédito
    Cooperativas) / -En millones de pesos- / 5.000 2.500 / …» — encabezados en un
    orden, valores en otro (RX-10); el extractor emparejó según esa linealización.
  - **Los nodos invertidos:** en v3, `…_2d3063` (bancos, con monto de restantes) y
    `…_50658f` (`Restriccion_restantes_entidades_deberan_observar_exigencia_basica_de_5_000_millones_de_pesos_50658f`
    — el id mismo porta la inversión), corregidos después vía C2/BKL-0006
    (`data/backlog/retests/C2_retest_2026-07-31.md`). En el grafo v2 de la traza del
    gate, sus gemelos de contenido idéntico SIN sufijo (mismo chunk productor):
    `Restriccion_bancos_salvo_cajas_de_credito_cooperativas_deberan_observar_exigencia_basica_de_`
    y `Restriccion_restantes_entidades_deberan_observar_exigencia_basica_de_5_000_millones_de_pesos`.
- **Traza pre-registrada y por qué esa:** `escalon1_r1/grafo_v2/EV1-039` (réplica 1).
  Verificado contra `fichas_fallas_v2.json`: r1 es la réplica más limpia — 10 pasos,
  SIN tope de tools, abre con `ver_nodo` **los dos portadores invertidos** (pasos con
  ids citados arriba) y su respuesta hace eco de ambos valores cruzados ("Bancos …
  **2.500** millones" / "Restantes entidades … **5.000** millones") con cita al
  "Punto 1.2. Exigencia básica."; los 3 claims centrales salieron `falso`. (r2 también
  abre ambos pero con 16 pasos y tope; r3 abre solo el nodo de bancos.)
- **REGLA DE ACIERTO:** el voto emite **`{noise_sensitivity, contenido_kg}` como
  primaria**, y el señalamiento debe ser el correcto: la evidencia del par exhibe
  al menos uno de los dos nodos portadores de montos consultados por el agente (quote
  de contenido) **contradicho por el pasaje del 1.2 del PDF** (pieza `fuente` con la
  correspondencia real Bancos 5.000 / Restantes 2.500). Camino del árbol: claims
  soportados por nodos consultados → `noise_sensitivity`; nodo contradice el PDF →
  `contenido_kg`. No se exige nombrar el mecanismo (tabla linealizada / quimera):
  la sub-especie es de lectura externa.
- **Ramas pre-registradas:** (i) acierto (la regla); (ii) miss-nombrado:
  **`completitud_kg` o `alcanzabilidad_kg`** (el dato SÍ está nodificado y FUE
  consultado — atribuir hueco o entierro es errar el casillero; es además el error
  simétrico del EJEMPLO NEGATIVO del propio prompt del verificador, que usa esta
  misma pregunta de la exigencia básica sobre otro grafo); (iii) miss-nombrado:
  `alucinacion_agente` o `aplicacion_erronea` (los claims son eco de nodos consultados
  — hay soporte, descarta alucinación — y los nodos no declaran alcance ajeno que el
  agente haya ignorado — descarta aplicación errónea: el defecto vive EN el contenido
  de los nodos); (iv) triage con
  motivo (voto dividido / flags de capa o S1).
- **Válvula:** ídem G-1; además, si el verificador reporta que los nodos de la traza
  NO portan los montos invertidos (contradiría el contenido citado en la ficha y la
  cadena BKL-0006), la lectura se detiene: discrepancia de archivo, no miss.
- **DISCLOSURE (advertencia de lectura, precedente del asterisco de CQ-025 en
  `protocolo_gate2.md` §2.b):** los ejemplos resueltos hardcodeados del prompt sellado
  del verificador usan esta MISMA pregunta de la exigencia básica sobre OTROS grafos —
  el EJEMPLO 1 (run_5, valor de período vencido → `{noise_sensitivity, contenido_kg}`)
  y el EJEMPLO NEGATIVO (run_1, no confundir con `completitud_kg`). El prompt está
  congelado desde antes de que existiera este material (nunca se iteró contra EV1-039),
  pero un acierto en G-4 se lee con ese asterisco: la forma del caso está ejercitada en
  el propio prompt.

**Regla transversal (del ciclo 2, se replica):** un caso es "silencioso" solo si NINGUNA
etapa de su cadena (capa / S1 / triage) dejó flag (`docs/lectura_ciclo2.md` §5.b).
Confundir primaria con secundaria no es acierto (regla 4 de la vara de
`casos_control.md`).

## 4. Scoring y criterio de aprobación global — LAUDADO (2026-08-02)

**Scoring por caso (idéntico a `protocolo_gate2.md` §4):** ACIERTO / MISS / TRIAGE
(voto dividido = derivación con motivo, no miss silencioso); `formato_invalido` en una
rep = rep sin voto; mayoría estricta sobre reps válidas, <2 válidas o sin mayoría →
TRIAGE. G-3 agrega la rama de lectura (ii), que se reporta por separado.

**Precedente citado (ciclo 2, `docs/lectura_ciclo2.md` §2):** sobre 8 casos-primaria la
columna ganadora dio **6 aciertos / 1 miss-con-flag / 1 triage — CERO silenciosos**; las
3 solapadas aparte (2 aciertos / 1 miss-con-flag). La propiedad que el proyecto viene
exigiendo no es acierto perfecto sino **contención**: todo miss con flag, todo triage
con motivo.

**Criterio global LAUDADO:** el gate **PASA** si y solo si se cumplen las dos
condiciones:

1. **Cero errores silenciosos** — un miss-con-flag y un triage-con-motivo NO son
   silenciosos; silencioso = miss en el que ninguna etapa de la cadena (verificador /
   capa / S1 / triage) dejó flag. **Un solo miss silencioso = NO PASA**, sin excepción.
2. **≥3 aciertos de 4** — el cuarto caso puede ser a lo sumo miss-con-flag,
   triage-con-motivo, o la rama de lectura de G-3.

**Nota sobre N:** el gate queda en 4 casos por el laudo del 2026-08-02 (los 3 del split
original + EV1-039 con su casillero laudado sobre la evidencia BKL-0006/RX-10). La
reserva restante sin causa (EV1-005, EV1-011, EV1-028) NO entra. Después del commit de
este protocolo, el gate no se amplía.

## 5. Presupuesto estimado y tope

**Base de referencia medida (corridas previas del verificador, `--n 3`):**

- Gate CQN2 (11 casos × 3 reps): verificador **12.869.986 in / 300.112 out**; S1
  **186.531 in / 23.640 out** (≈1,4% del verificador); capas: cero LLM
  (`extraccion_h2h_ciclo2.md`, Costos totales). Promedio ≈ **390K in / 9,1K out por
  repetición** (12.869.986/33 y 300.112/33).
- Precedente de estimación del gate #2: "5 casos × 3 repeticiones × ~400K tokens de
  input ≈ 6M" (`protocolo_gate2.md` §5).

**Desglose estimado de este gate (4 casos × 3 reps = 12 llamadas de verificador):**

| Componente | Estimación | Base |
|---|---|---|
| Verificador (12 reps) | ≈ 4,8M in / ≈ 113K out | 12 × 400K in; 12 × 9,4K out (promedio CQN2 redondeado arriba) |
| Capa v6.2-D | 0 | determinística |
| S1 v0.4b | ≈ 72K in / 9K out | ≈1,5% del verificador (proporción CQN2) |
| **Total** | **≈ 4,9M in / ≈ 122K out** | |

Las corridas previas registraron costos del verificador en tokens, no en USD
(`extraccion_h2h_ciclo2.md` registra tokens; el USD 0,8146 del 1b/CQN2 es de
agente+juez, otra cosa).

**Tope LAUDADO (2026-08-02), doble y ambos cortan:**
- **Primario, por tokens: 6M de input / 200K de output** (≈1,2× y ≈1,6× la estimación —
  margen para reintentos de formato y casos largos tipo CQN2-012/015, que midieron
  hasta 2,75M in por caso).
- **Techo secundario, por gasto: USD 20** (tracker por filas nuevas de caché, el mismo
  mecanismo del 1b).

Alcanzado CUALQUIERA de los dos, la corrida se detiene y se reporta lo corrido.

## 6. Registro

- **Fecha de la propuesta:** 2026-08-02 (U5-PREP). **Laudos incorporados:** 2026-08-02
  (destrabe de la adjudicadora: split con G-4, reglas de acierto, criterio global §4,
  tope doble §5, brechas por lectura externa, esquema ausente, deuda del canal de
  abstenciones §7). Fecha del protocolo definitivo: la del commit de la autora.
- **Instrumento:** v7' congelado — hashes del sello del ciclo 2
  (`extraccion_h2h_ciclo2.md` §Sello), verificados en la guarda del paso 0.
- **Material:** `data/experiment/evaluacion/calibracion_v2v3/` (expediente, split,
  calibradores) + las fuentes selladas que el expediente cita.

## 7. Constancia de no-iteración y quemado

**El prompt del verificador, la taxonomía ensamblada, los módulos determinísticos, los
umbrales de S1 y los calibradores NO se iteran contra los casos del gate BAJO NINGUNA
CIRCUNSTANCIA** — ni antes de la corrida (los casos de gate no se corren en dev), ni
después (cualquiera sea el resultado, nada se ajusta contra ellos; un eventual ciclo 3
del instrumento se calibra contra material quemado o fresco NO-gate, nunca contra
estos). Los cuatro casos del gate quedan **QUEMADOS** al correrse; los tres calibradores
(EV1-031, EV1-018, EV1-035) **están QUEMADOS desde el laudo del 2026-08-02**
(`calibradores_v2v3.md` §3). La verificación de no-contaminación es mecánica y se
replica del gate #2 §2.d: pre-corrida, los namespaces del verificador sobre los gfp de
v2/v3 deben ser inexistentes en `cache/verificador.db`.

**Deuda explícita que este gate NO cubre (laudo 2026-08-02):** el canal de
**abstenciones-aprobadas** (falso negativo del juez — EV1-029 r1 de ambos brazos,
precedente sellado run_3/EV1-007) queda FUERA de U5: el verificador solo recibe fallas
y ninguna clase de salida lo alcanza (`calibracion_v2v3/brechas_taxonomia.md` §2).
Queda registrado como **candidata de cola: "screening de aprobadas / re-calibración del
juez"** — unidad propia, con su pre-registro y su laudo, a incorporar al tablero en el
próximo cierre.
