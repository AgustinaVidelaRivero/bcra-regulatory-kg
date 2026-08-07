# Tablero de estado — bcra-regulatory-kg

Actualizado al 7 de agosto de 2026 (semana del 3 al 9 de agosto) —
se actualiza por laudo al cierre de cada semana; entre cierres, el estado real
es `git log` + `data/backlog/backlog.jsonl`.

Generado sobre HEAD `24432a45a0be7e2e4b42ea4fe2ffc48c53f59131` (working tree
limpio: `git status --porcelain` vacío al momento de generar, con la única
excepción de este archivo y de `docs/spec_backlog_refinamiento.md` durante su
edición). Todo número de este documento sale de parseo real; la fuente se cita
junto a cada bloque.

---

## 1. Grafo vigente

- **Ruta:** `data/experiment/grafo_v2/reensamblado_v3/kg.json`.
- **Tamaño:** 4.469 nodos / 8.073 aristas
  (fuente: `python3 -c "import json; kg=json.load(open('data/experiment/grafo_v2/reensamblado_v3/kg.json')); print(len(kg['nodes']), len(kg['edges']))"`).
- **sha256 (post-C7):**
  `26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571`
  (fuente: `shasum -a 256 data/experiment/grafo_v2/reensamblado_v3/kg.json`;
  coincide con el sha aplicado que cierra
  `data/backlog/retests/C7_retest_2026-08-03.md`).
- **Registro como vigente:** entrada explícita `GRAFOS_EXPLICITOS` en
  `app/main.py:192` (promoción 2026-07-31, comentario en `app/main.py:187`).
- **Últimas correcciones aplicadas** (fuente: `data/backlog/backlog.jsonl`,
  eventos `aplicacion`/`cambio_estado` con ts 2026-07-31 a 2026-08-03):
  - **BKL-0017** (C1) — restauración del criterio general 1.1 de Clasificación
    de Deudores; estado `verificado`; re-test 4/4 PASS
    (`data/backlog/retests/C1_retest_2026-07-31.md`).
  - **BKL-0006** (C2, opción A) — montos del punto 1.2 de Capitales Mínimos
    corregidos contra la tabla del PDF (bancos 5.000 / restantes 2.500);
    estado `verificado` (`data/backlog/retests/C2_retest_2026-07-31.md`).
  - **BKL-0007** — cerrada por referencia junto con C2; estado `verificado`.
  - **BKL-0023** (C3) — umbral propagado 2.500→5.000; estado `verificado`;
    re-test 4/4 (`data/backlog/retests/C3_retest_2026-08-02.md`); sha256
    posterior del kg `d673dd72…` (registrado en el commit `c51b96a`).
  - **BKL-0019** (C4) — aristas `subclase_de` promovidas desde cuarentena:
    de las 9 con padre sugerido en
    `data/experiment/grafo_v2/reensamblado_v3/cuarentena.json`, entraron
    **8** (bloque contiguo, `rol_fuente: cuarentena_laudada`); la novena
    (`Sujeto_propuesto_originante_acreedor_inicial`, DUDOSA: padre de nivel
    rol fuera del árbol de clases) quedó EXCLUIDA por laudo y DERIVADA a la
    decisión de modelado de BKL-0020 (evento `aplicacion` de BKL-0019 en
    `data/backlog/backlog.jsonl`); estado `verificado`; re-test 5/5
    (`data/backlog/retests/C4_retest_2026-08-02.md`); sha256 posterior del
    kg `0161be69…` (registrado en el commit `2c71e3f`).
  - **BKL-0004** (C5) — enumeración de niveles del 6.5 de Clasificación de
    Deudores restaurada: 9 nodos + 17 aristas (`rol_fuente:
    restauracion_manual`, cambio 100 % aditivo); estado `verificado`; re-test
    determinístico **32/32** (`data/backlog/retests/C5_retest_2026-08-02.md`);
    sha256 posterior `04a50081…`; corrida real RT-C5-1..RT-C5-5 con
    agente+juez: **5/5 correcta** (label `rt_c5_c6`, trazas juzgadas en
    `data/experiment/evaluacion/posthoc_run/traces/rt_c5_c6/`).
  - **BKL-0003** (C6) — salvedad mutuales/cooperativas del 1.1.2.5 de
    Protección de Usuarios: 1 nodo `Excepcion` + 2 aristas (`rol_fuente:
    restauracion_manual`, aditivo); estado `verificado` **en capa KG**;
    re-test determinístico **38/38**
    (`data/backlog/retests/C6_retest_2026-08-03.md`); sha256 posterior
    `fe5f6b69…`; corrida real RT-C6-1..RT-C6-4: **2/4** (incorrecta /
    correcta / parcial / correcta), con laudo de deslinde de capas: la capa
    KG cumplió (nodo presente, rank 1, `ver_nodo` byte-idéntico entre
    trazas); los residuos son de capa agente → altas BKL-0026 (generación) y
    BKL-0027 (navegación).
  - **BKL-0005** (C7) — calificadores del esquema del 7.1 de RegInf
    restaurados: edición de una sola `descripcion` de un solo nodo (cero
    nodos/aristas agregados); estado `verificado`; re-test determinístico
    **27/27** (`data/backlog/retests/C7_retest_2026-08-03.md`); sha256
    posterior `26fac8b4…` (= sha del vigente).
- **Hashes de referencia del `ver_nodo` de C6 (supersesión):** los vigentes,
  sellados en `data/backlog/retests/C6_retest_2026-08-03.md` (laudo de
  deslinde, commit `5b66d8b`), son
  `64bd825978953c4819dfa0850f1ff039d4b9bbbfa18fadfbc055822c6a6ab19e`
  (canónico: `json.dumps(obj, ensure_ascii=False, sort_keys=True)` sobre el
  output parseado) y
  `a5bb2d1fd7fc11eab4f6d23525efea0f3376c8c1981b1be50be268fba82e7667`
  (string crudo del output sin re-serializar), byte-idénticos entre RT-C6-1 y
  RT-C6-2. Cualquier hash de referencia previo citado para ese `ver_nodo` en
  material de sesión no versionado queda superseded: ningún otro hash de
  referencia figura en archivos del repo ni en la historia git (verificado en
  esta actualización por grep del prefijo previo y `git log -S`, ambos
  vacíos).

## 2. Baselines y mediciones selladas

Fuente: `data/experiment/evaluacion_escalon1/corridas/resultados_1b_FINALES_2026-07-31.json`
(clave `primaria`):

| Grafo | EV1 (36 preguntas) |
|---|---|
| `grafo_v2` | 27/36 |
| `reensamblado_v3` | 29/36 |
| `run_3` (referencia) | 31/36 |

- Lectura sellada del 1b: `docs/lectura_escalon1b.md`. EV1 quedó QUEMADO por
  completo (ídem, §5).
- **Pasada 1 intrínseca: HECHA** — descriptiva, sin umbrales, USD 0;
  **P-b (CRUX) CONFIRMADA** (v3 0.637730 > v2 0.600981 en M1)
  (fuente: `data/experiment/metricas_intrinsecas/pasada1_resumen.md`, tabla §1
  y fila P-b). **Umbrales de la pasada 2: PENDIENTES** (otra unidad y otro
  laudo, ídem y `docs/spec_evaluacion_intrinseca.md` §8).
- Nota de comparabilidad: la pasada 1 midió el v3 previo a las correcciones
  C1 a C7 (4.458 nodos / 8.044 aristas, `pasada1_resumen.md`
  cabecera); el vigente ya incluye las siete (4.469 / 8.073, §1).

## 3. Backlog de nodos

Fuente: `data/backlog/backlog.jsonl` (71 líneas, 27 ids únicos). Regla del
estado efectivo por id: se recorre el archivo en orden y (i) todo evento con
la clave `estado` no vacía fija el estado; (ii) la clave `estado_retriage`
— propia de los eventos `retriage_v3` y DISTINTA de `estado` — fija el
estado solo cuando vale `resuelta_por_v3`; su otro valor
(`vigente_sin_cambios`) no modifica nada; (iii) los eventos sin ninguna de
las dos claves (p. ej. `nota`) tampoco modifican. Comando que implementa la
regla tal cual y devuelve la tabla:
`python3 -c "import json,collections; est={}; [est.__setitem__(o['id'], o['estado'] if o.get('estado') else 'resuelta_por_v3') for o in map(json.loads, open('data/backlog/backlog.jsonl')) if o.get('estado') or o.get('estado_retriage')=='resuelta_por_v3']; print(len(est), dict(collections.Counter(est.values())))"`
→ `27 {'resuelta_por_v3': 2, 'verificado': 10, 'triaged': 15}`.

| Estado | Cantidad | Ids |
|---|---|---|
| `verificado` | 10 | BKL-0003..0007, 0017, 0019, 0023, 0026, 0027 |
| `resuelta_por_v3` (retriage) | 2 | BKL-0001, BKL-0002 |
| `triaged` vigentes | 15 | BKL-0008..0016, 0018, 0020..0022, 0024, 0025 |

Las tres candidatas del tablero anterior (BKL-0004, BKL-0003, BKL-0005) ya
fueron aplicadas y verificadas esta semana como C5, C6 y C7 (§1). La
priorización de las próximas queda pendiente de laudo.

Notas:
- **BKL-0026** (alta 2026-08-05, laudo commit `5b66d8b`) — defecto de capa
  generación, especie `alucinacion_agente` (casilla existente de la
  taxonomía v5.7): paráfrasis de verbatim sintácticamente ambiguo que
  invierte la norma con el nodo correcto presente en contexto (contraste
  RT-C6-1 vs RT-C6-2, `ver_nodo` byte-idéntico). La medición N=3 de RT-C6-1
  dio **incorrecta 3/3** (labels `rt_c6_n3_r{1,2,3}`, dbs separadas, 0 hits
  de caché): el flag "n=1 — sistematicidad NO confirmada" fue **retirado**
  (evento del 2026-08-07 en `backlog.jsonl`); el defecto es sistemático y
  reproducible con retrieval perfecto. Estado `verificado`, `aplicado_en`
  null (defecto de agente, no del grafo).
- **BKL-0027** (alta 2026-08-05, mismo laudo) — defecto de capa navegación,
  especie `navegación` (casilla existente de la taxonomía v5.7): asimetría
  direccional de `ver_vecinos` en roles alcanzables solo por aristas
  entrantes (RT-C6-3); pariente directo de BKL-0022. Estado `verificado`
  con flag n=1 (sin medición de sistematicidad programada), `aplicado_en`
  null.
- **BKL-0024 y BKL-0025** — altas de `app_feedback` (especie `ausencia`),
  `triaged` el 2026-08-02.
- **BKL-0022** queda `triaged`: su orfandad léxica está mitigada por
  navegación tras C4, pero esa navegabilidad es orden-dependiente bajo la
  ventana de 40 de `ver_vecinos` (fragilidad registrada en el evento `nota`
  del 2026-08-02); el fix durable queda diferido a la migración de backend
  (§5, unidad 7).
- **BKL-0020** acumuló la arista pendiente de C4 (la DUDOSA de
  `Sujeto_propuesto_originante_acreedor_inicial`), de modo que sus dos
  originantes son hoy una sola decisión de modelado.

## 4. Backlog RX (instrumento)

Fuente: `docs/backlog_reextraccion.md` (abierto, en acumulación; no ejecutar
hasta que yo lo cierre). Estado por entrada:

- **RX-01** — `chunk_id` ambiguo (81 ids / 183 chunks): mitigado en v3; fix de raíz pendiente.
- **RX-02** — location desplazada por coalescing (21 chunks / 26.308 chars): no mitigable en ensamblado.
- **RX-03** — falsos headers por referencias cruzadas (17 chunks / 47.813 chars): no mitigable; reproducibilidad DECLARADA.
- **RX-04** — 3 puntos sin articulado propio (clasificación 1.1 y 4.5, exterior 9.2): no mitigable.
- **RX-05** — 13 chunks con roles documentales mezclados: no mitigable; unidad de conteo DECLARADA.
- **RX-06** — 51 chunks partidos por `HARD_CAP_CHARS`: no mitigable; daño sin cuantificar (falta gold por chunk).
- **RX-07** — extracción del índice pagada (48 chunks): mitigada en v3; con precisión sellada del chunk mixto `clasificacion_deudores::10.4`.
- **RX-08** — 25 nodos cáscara heredados del índice: registro, no acción; se resuelve con RX-04.
- **RX-09** — preámbulos descartados (1.207 chars): impacto despreciable; listado para declarar cobertura 100%.
- **RX-10** — tablas linealizadas dentro del articulado: daño POR INSTANCIA, no sistemático; la instancia conocida (montos 1.2) ya corregida vía BKL-0006; toda tabla numérica requiere verificación individual.

## 5. Cola de unidades (orden vigente)

U5 (re-calibración del verificador) HECHA: gate U5 pasado y verificador
validado-en-familia v2/v3 (`docs/lectura_gate_u5.md`; Motor 3 habilitado
como diagnóstico automático con laudo humano). **Piloto sin-gold U6
(2026-08-07): Motor 3 NO validado como adjudicador sin humano** — acuerdo de
capa 4/13 (lectura estricta oficial; 6/13 en sensibilidad) contra umbral
pre-registrado ≥ 11/13; adjudicación manual permanente; régimen sin-gold
declarado no validado en este ciclo
(`docs/resultado_piloto_singold_u6.md` §1;
pre-registro `docs/preregistro_piloto_singold_u6.md` + enmienda 01).

1. Resto del backlog de nodos (§3 de este tablero). BKL-0023, hallazgo residual del gate U5, ya quedó cerrado por C3 (§1).
2. Matriz del `scripts/shapes_validator.py` a esquema v2.
3. **U6 — exploración dirigida: EJECUTADA Y ADJUDICADA** (corrida
   `u6_exploracion`, 25 casos; adjudicación humana sellada: **7 correctas /
   15 parciales / 3 incorrectas** —
   `data/experiment/exploracion/adjudicacion/u6_adjudicacion_humana.jsonl`,
   sellada con laudos №0-5 en el commit `b337152`). El adaptador jsonl→traza
   (`docs/spec_backlog_refinamiento.md`) ya está construido y
   el Motor 2 operativo (`scripts/adaptador_sesiones.py`, laudo D1, commit
   `0d5fd10`): cola de intake `data/backlog/intake/cola_intake.jsonl` con
   6 casos, 3 en `pendiente_de_triage`
   (fuente: `python3 -c "import json; xs=[json.loads(l) for l in open('data/backlog/intake/cola_intake.jsonl')]; print(len(xs), sum(1 for x in xs if x['estado']=='pendiente_de_triage'))"`).
4. **Canal de abstenciones-aprobadas (candidata):** screening de aprobadas /
   re-calibración del juez — fuera del universo de entrada del verificador
   (`docs/protocolo_gate_u5.md` §7, `docs/lectura_gate_u5.md` §5).
5. EV2 por generación ciega (`docs/lectura_escalon1b.md` §5).
6. Re-extracción única (cierra el backlog RX §4; insumos:
   `docs/literatura/mapa_incorporacion_graph_eng.md`).
7. Migración Neo4j (`docs/decision_backend_grafo.md`). **Backend
   experimental ejecutado y mergeado, NO inyectado** (commit `c26cb9b`;
   `data/experiment/neo4j/README.md`): carga verificada 4.469/8.073 exactos,
   índice full-text Lucene analyzer `spanish` sobre label+descripcion,
   adaptador `Neo4jIndex` con paridad exacta en `ver_nodo`/`ver_vecinos`
   (10/10 y 10/10) y divergencia esperada en `buscar_nodos`, benchmark de
   latencia (~2 ms de mediana full-text). El pipeline de evaluación sigue
   usando el `GraphIndex` in-memory; la inyección es decisión futura.
8. Escalado del corpus.
9. Comparación KG-RAG vs RAG tradicional (pregunta de investigación, `README.md`).

## 6. Laudos abiertos

- Cierre de la pasada 2 — laudo de M7 CERRADO (2026-08-02): `restauracion_manual` cuenta como rol normativo (fuera del numerador de M7); `esqueleto` también queda fuera del numerador (nodos sin chunk de origen); ambos integran el denominador. Declarado en la fila M7 de `docs/spec_evaluacion_intrinseca.md`. El bloqueante de la pasada 2 por este punto queda LEVANTADO. **M7 vigente: 577/4.469** — numerador = 577 nodos `tabla_norma_origen` (cero `indice`); los **11** nodos `restauracion_manual` del vigente (BKL-0017, los 9 de BKL-0004 y el de BKL-0003, según la fila M7 de la spec) quedan fuera del numerador, igual que los 70 `esqueleto`; ambos integran el denominador (recomputado: `python3 -c "import json,collections; kg=json.load(open('data/experiment/grafo_v2/reensamblado_v3/kg.json')); print(dict(collections.Counter(n.get('rol_fuente') for n in kg['nodes'])))"` → `{'esqueleto': 70, 'cuerpo': 3811, 'tabla_norma_origen': 577, 'restauracion_manual': 11}`).
- **Indexación de lecturas en `docs/INDICE.md`:** hay lecturas selladas sin
  indexar (verificado: `grep -n "lectura_escalon1b" docs/INDICE.md` = vacío;
  `lectura_ciclo2.md` sí figura, línea 61).
- **Experimento de memoria de sesiones** (candidatas: Graphiti — sinergia
  Neo4j —, TencentDB-Agent-Memory modo solo-artefactos, cognee; gbrain
  descartado): condición post-U5 CUMPLIDA; pendiente laudo de arranque y
  timebox.

## 7. Disciplinas activas

- **Pre-registro con válvula:** protocolo o vara sellada ANTES de toda corrida; desvíos por válvula documentada, nunca ajuste silencioso.
- **Material quemado:** EV1/CQ/CQN/CQN2 no se reutilizan como re-test ni objetivo.
- **Un commit por corrección:** cada arreglo del grafo con su evento en `backlog.jsonl` y su SHA.
- **Verificación contra archivos:** todo dato de estado sale de archivos del repo, nunca de memoria.
- **Blind eval generation para EV2:** las preguntas nuevas se generan a ciegas contra los PDFs, sin ver los grafos.

## 8. Hitos

- **Semana 27/07–02/08:** escalón 1b medido y adjudicado (v2 27/36 → v3 29/36;
  el defecto de ensamblado explicaba la mitad del gap contra run_3); inversión
  P-b confirmada (pasada 1 intrínseca); v3 promovido a vigente; circuito de
  refinamiento estrenado (C1 restauración 1.1, C2 montos 1.2; 3/22 entradas
  cerradas); biblioteca ampliada (playbook fichado, KARMA como 09, mapa de
  incorporación); CLAUDE.md + tablero. Commits 1–14 de la semana.
- **2026-08-02:** gate U5 pasado (cero silenciosos + 3/4, cuarto en rama de
  lectura), verificador validado-en-familia v2/v3, Motor 3 habilitado
  (diagnóstico automático, laudo humano), USD 23,22 (`docs/lectura_gate_u5.md`).
  Además: **C3 y C4 aplicadas y verificadas** (re-tests 4/4 y 5/5,
  `data/backlog/retests/C{3,4}_retest_2026-08-02.md`); **adaptador de
  sesiones (D1) construido** — Motor 2 operativo
  (`scripts/adaptador_sesiones.py`, commit `0d5fd10`); **INFRA-2** (reglas
  g/h del circuito de trabajo, commit `1ef98cf`). Commits de la semana
  27/07–02/08: **30**
  (fuente: `git rev-list --count --since=2026-07-27 HEAD`).
- **Semana 03/08–07/08:**
  - **C5, C6 y C7 aplicadas y verificadas** (re-tests determinísticos 32/32,
    38/38 y 27/27: `data/backlog/retests/C5_retest_2026-08-02.md`,
    `C6_retest_2026-08-03.md` y `C7_retest_2026-08-03.md`); grafo vigente en
    4.469/8.073, sha256 `26fac8b4…` (§1).
  - **Corrida real `rt_c5_c6`** (agente+juez, 9 preguntas, USD 0,40 —
    `summary_rt_c5_c6_reensamblado_v3.json`): **C5 5/5, C6 2/4**; laudo de
    deslinde de capas (capa KG cumplida; residuos de capa agente) → altas
    **BKL-0026** (generación) y **BKL-0027** (navegación), commit `5b66d8b`.
  - **U6 — exploración dirigida:** corrida `u6_exploracion` de 25 casos;
    adjudicación humana sellada **7 correctas / 15 parciales / 3
    incorrectas** (commit `b337152`).
  - **Piloto sin-gold U6** (pre-registrado, commits `3e507c1` + `e55388c`):
    **Motor 3 NO validado** — acuerdo de capa 4/13 (estricta) contra umbral
    ≥ 11/13; adjudicación manual permanente. Consumo USD 18,37
    (`docs/resultado_piloto_singold_u6.md`, commit `24432a4`).
  - **N=3 de RT-C6-1:** incorrecta **3/3** (labels `rt_c6_n3_r{1,2,3}`,
    0 hits de caché) — flag n=1 de BKL-0026 retirado (evento 2026-08-07 en
    `backlog.jsonl`).
  - **Backend Neo4j experimental completo y mergeado, no inyectado**
    (commit `c26cb9b`, `data/experiment/neo4j/README.md`).