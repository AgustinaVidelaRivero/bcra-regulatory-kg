# Tablero de estado — bcra-regulatory-kg

Actualizado al cierre de la semana del 27 de julio al 2 de agosto de 2026 —
se actualiza por laudo al cierre de cada semana; entre cierres, el estado real
es `git log` + `data/backlog/backlog.jsonl`.

Generado sobre HEAD `8bcc461df4c8729892e169eaefc5a80531705b39` (working tree
limpio). Todo número de este documento sale de parseo real; la fuente se cita
junto a cada bloque.

---

## 1. Grafo vigente

- **Ruta:** `data/experiment/grafo_v2/reensamblado_v3/kg.json`.
- **Tamaño:** 4.459 nodos / 8.046 aristas
  (fuente: `python3 -c "import json; kg=json.load(open('data/experiment/grafo_v2/reensamblado_v3/kg.json')); print(len(kg['nodes']), len(kg['edges']))"`).
- **Registro como vigente:** entrada explícita `GRAFOS_EXPLICITOS` en
  `app/main.py:192` (promoción 2026-07-31, comentario en `app/main.py:187`).
- **Últimas correcciones aplicadas** (fuente: `data/backlog/backlog.jsonl`,
  eventos `aplicacion`/`cambio_estado` con ts 2026-07-31):
  - **BKL-0017** (C1) — restauración del criterio general 1.1 de Clasificación
    de Deudores; estado `verificado`; re-test 4/4 PASS
    (`data/backlog/retests/C1_retest_2026-07-31.md`).
  - **BKL-0006** (C2, opción A) — montos del punto 1.2 de Capitales Mínimos
    corregidos contra la tabla del PDF (bancos 5.000 / restantes 2.500);
    estado `verificado` (`data/backlog/retests/C2_retest_2026-07-31.md`).
  - **BKL-0007** — cerrada por referencia junto con C2; estado `verificado`.

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
- Nota de comparabilidad: la pasada 1 midió el v3 pre-C1/C2 (4.458 nodos /
  8.044 aristas, `pasada1_resumen.md` cabecera); el vigente ya incluye las
  correcciones (4.459 / 8.046).

## 3. Backlog de nodos

Fuente: `data/backlog/backlog.jsonl` (46 líneas, 22 ids únicos; estado
efectivo = último evento por id):

| Estado | Cantidad | Ids |
|---|---|---|
| `verificado` | 3 | BKL-0006, BKL-0007, BKL-0017 |
| `resuelta_por_v3` (retriage) | 2 | BKL-0001, BKL-0002 |
| `triaged` vigentes | 17 | BKL-0003..0005, 0008..0016, 0018..0022 |

Próximas candidatas, en orden:
1. **BKL-0019** — cuarentena: 9 aristas `subclase_de` según `padres_sugeridos`
   de `data/experiment/grafo_v2/reensamblado_v3/cuarentena.json`.
2. **BKL-0003 / BKL-0004 / BKL-0005** (E3/E4/E5 del
   `data/backlog/expediente_retriage_v3.md`) — defectos de contenido (especies
   en `backlog.jsonl`: `ausencia`, `ausencia`, `amputacion`).

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

1. **U5 — re-calibración del verificador (FIRME).** Expediente del juez en
   `docs/lectura_escalon1b.md` §5: (i) abstención-aprobada (EV1-029),
   (ii) varianza de tallado (EV1-035).
2. Resto del backlog de nodos (§3 de este tablero).
3. Matriz del `scripts/shapes_validator.py` a esquema v2.
4. Adaptador jsonl→traza (`docs/spec_backlog_refinamiento.md`, pendiente C4) +
   **U6 — exploración dirigida**, con lista de exclusión de territorio quemado
   (EV1/CQ/CQN/CQN2).
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
- **Experimento Graphiti post-U5:** timeboxeado, gitignoreado, nunca fuente de
  verdad ni artefacto de tesis
  (`docs/literatura/mapa_incorporacion_graph_eng.md`, fila d3).
- **Indexación de lecturas en `docs/INDICE.md`:** hay lecturas selladas sin
  indexar (verificado: `grep -n "lectura_escalon1b" docs/INDICE.md` = vacío;
  `lectura_ciclo2.md` sí figura, línea 61).

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