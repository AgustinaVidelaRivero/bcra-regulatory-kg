# Tablero de estado — bcra-regulatory-kg

Actualizado al cierre de la semana del 27 de julio al 2 de agosto de 2026 —
se actualiza por laudo al cierre de cada semana; entre cierres, el estado real
es `git log` + `data/backlog/backlog.jsonl`.

Generado sobre HEAD `1ef98cf35173d8c405113024656cd7ae7ea67594` (working tree
limpio: `git status --porcelain` vacío al momento de generar, con la única
excepción de este mismo archivo durante su edición). Todo número de este documento sale de parseo real; la fuente se cita
junto a cada bloque.

---

## 1. Grafo vigente

- **Ruta:** `data/experiment/grafo_v2/reensamblado_v3/kg.json`.
- **Tamaño:** 4.459 nodos / 8.054 aristas
  (fuente: `python3 -c "import json; kg=json.load(open('data/experiment/grafo_v2/reensamblado_v3/kg.json')); print(len(kg['nodes']), len(kg['edges']))"`).
- **Registro como vigente:** entrada explícita `GRAFOS_EXPLICITOS` en
  `app/main.py:192` (promoción 2026-07-31, comentario en `app/main.py:187`).
- **Últimas correcciones aplicadas** (fuente: `data/backlog/backlog.jsonl`,
  eventos `aplicacion`/`cambio_estado` con ts 2026-07-31 y 2026-08-02):
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
  C1, C2, C3 y C4 (4.458 nodos / 8.044 aristas, `pasada1_resumen.md`
  cabecera); el vigente ya las incluye (4.459 / 8.054, §1).

## 3. Backlog de nodos

Fuente: `data/backlog/backlog.jsonl` (55 líneas, 23 ids únicos). Regla del
estado efectivo por id: se recorre el archivo en orden y (i) todo evento con
la clave `estado` no vacía fija el estado; (ii) la clave `estado_retriage`
— propia de los eventos `retriage_v3` y DISTINTA de `estado` — fija el
estado solo cuando vale `resuelta_por_v3`; su otro valor
(`vigente_sin_cambios`) no modifica nada; (iii) los eventos sin ninguna de
las dos claves (p. ej. `nota`) tampoco modifican. Comando que implementa la
regla tal cual y devuelve la tabla:
`python3 -c "import json,collections; est={}; [est.__setitem__(o['id'], o['estado'] if o.get('estado') else 'resuelta_por_v3') for o in map(json.loads, open('data/backlog/backlog.jsonl')) if o.get('estado') or o.get('estado_retriage')=='resuelta_por_v3']; print(len(est), dict(collections.Counter(est.values())))"`
→ `23 {'resuelta_por_v3': 2, 'triaged': 16, 'verificado': 5}`.

| Estado | Cantidad | Ids |
|---|---|---|
| `verificado` | 5 | BKL-0006, BKL-0007, BKL-0017, BKL-0019, BKL-0023 |
| `resuelta_por_v3` (retriage) | 2 | BKL-0001, BKL-0002 |
| `triaged` vigentes | 16 | BKL-0003..0005, 0008..0016, 0018, 0020..0022 |

Próximas candidatas, en orden:
1. **BKL-0004** (E4 del `data/backlog/expediente_retriage_v3.md`) — especie
   `ausencia`.
2. **BKL-0003** (E3, ídem) — especie `ausencia`.
3. **BKL-0005** (E5, ídem) — especie `amputacion`.

Notas:
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
validado-en-familia v2/v3 (`docs/lectura_gate_u5.md`; Motor 3 habilitado).

1. Resto del backlog de nodos (§3 de este tablero). BKL-0023, hallazgo residual del gate U5, ya quedó cerrado por C3 (§1).
2. Matriz del `scripts/shapes_validator.py` a esquema v2.
3. **U6 — exploración dirigida**, con lista de exclusión de territorio
   quemado (EV1/CQ/CQN/CQN2). El adaptador jsonl→traza
   (`docs/spec_backlog_refinamiento.md`) ya está construido y
   el Motor 2 operativo (`scripts/adaptador_sesiones.py`, laudo D1, commit
   `0d5fd10`): cola de intake `data/backlog/intake/cola_intake.jsonl` con
   3 casos, los 3 en `pendiente_de_triage`
   (fuente: `python3 -c "import json; xs=[json.loads(l) for l in open('data/backlog/intake/cola_intake.jsonl')]; print(len(xs), sum(1 for x in xs if x['estado']=='pendiente_de_triage'))"`).
4. **Canal de abstenciones-aprobadas (candidata):** screening de aprobadas /
   re-calibración del juez — fuera del universo de entrada del verificador
   (`docs/protocolo_gate_u5.md` §7, `docs/lectura_gate_u5.md` §5).
5. EV2 por generación ciega (`docs/lectura_escalon1b.md` §5).
6. Re-extracción única (cierra el backlog RX §4; insumos:
   `docs/literatura/mapa_incorporacion_graph_eng.md`).
7. Migración Neo4j (`docs/decision_backend_grafo.md`).
8. Escalado del corpus.
9. Comparación KG-RAG vs RAG tradicional (pregunta de investigación, `README.md`).

## 6. Laudos abiertos

- **Cierre de la pasada 2:** cómo cuentan las restauraciones manuales en M7 —
  el nodo de BKL-0017 lleva `rol_fuente: restauracion_manual`
  (`data/backlog/retests/C1_retest_2026-07-31.md`), valor fuera del
  vocabulario de roles que M7 usa como numerador
  (`docs/spec_evaluacion_intrinseca.md`, fila M7: numerador = {`indice`,
  `tabla_norma_origen`}; BLOQUEANTE en pasada 2).
  Verificado post-C3 (2026-08-02): el nodo corregido por C3 (`…_7bb7bb`)
  conserva `rol_fuente: cuerpo` y el único nodo con
  `rol_fuente: restauracion_manual` sigue siendo el de BKL-0017
  (`Obligacion_los_clientes_de_la_entidad_tanto_residentes_en_el_pais_de_los_sectores_publico_y_e1946e`)
  — C3 no amplía este bloqueante (fuente: `python3 -c "import json; kg=json.load(open('data/experiment/grafo_v2/reensamblado_v3/kg.json')); print([n['id'] for n in kg['nodes'] if n['rol_fuente']=='restauracion_manual'])"`).
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