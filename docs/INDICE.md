# Índice de lectura — documentos formales de la tesis

Este es mi mapa de lectura del repo. Ordena los documentos formales en capas: qué leer
para entender el proyecto, cuál es la cadena de validación del instrumento (en orden
cronológico, con el commit que selló cada pieza — extraídos de `git log`), qué es
evidencia de respaldo, y dónde viven el corpus y los datos. Las rutas son exactas.

---

## (i) Para entender el proyecto

- `docs/ARQUITECTURA.md` — mapa completo del repo: zonas congeladas/activas/scratch,
  hallazgos de higiene y punteros. Snapshot del 2026-07-09 (commit `9eb5ef7`).
- `docs/hallazgos_tesis.md` — los hallazgos H1–H13 que alimentan Resultados/Discusión
  (commit `7db9020`, 2026-07-09).
- `docs/ppf/main.tex` — fuente LaTeX de mi PPF preliminar (commit `c0bb059`, 2026-06-03);
  el PDF compilado vive en el mismo directorio `docs/ppf/`.

Contexto adicional: `docs/schema/experiment_protocol.md` y
`docs/schema/experiment_instance_template.md` (protocolo de la Fase 2.2, con `docs/schema/legacy/`
como historia del scope viejo), `docs/literatura/` (papers con resúmenes críticos y
comparativa), y `docs/defensa/` (guion de presentación y preguntas de jurado).

## (ii) La cadena de validación del instrumento (orden cronológico)

El instrumento final del proyecto es el compuesto **v7–v0.4b** (verificador v5.7 + capa
determinística + S1). Cada etapa siguió el mismo patrón: protocolo o vara sellada ANTES
de toda corrida, corrida única, lectura contra la vara. Los commits salen de `git log`.

1. `docs/especificacion_verificador_v57.md` — especificación final del verificador de
   atribución: historia v1→v5.7 con fuentes por cifra (commit `32f819e`, 2026-07-14).
2. `docs/protocolo_gate2.md` — protocolo pre-registrado del gate #2, la segunda y ÚLTIMA
   calibración de v5.7 (commit `c0b96a4`, 2026-07-14).
3. `docs/lectura_gate2_AB.md` — doble lectura del gate #2 (vara A / vara v3), commiteada
   junto con `docs/especificacion_capa_deterministica.md` (la capa D del compuesto)
   (commit `150d67b`, 2026-07-15).
4. `docs/protocolo_piloto_v6.md` — protocolo pre-registrado del piloto v6.0-D (commit
   `fb8d888`, 2026-07-16); su vara vive en
   `.claude/skills/kg-refinement/references/casos_piloto.md` (sellada por inexistencia).
5. `docs/lectura_piloto_v6.md` — lectura del piloto: corrida única, 5 casos frescos
   (commit `c29720b`, 2026-07-16).
6. `docs/protocolo_validacion_v61.md` — protocolo pre-registrado de la validación de
   v6.1-D (commit `4109d44`, 2026-07-16); vara:
   `.claude/skills/kg-refinement/references/casos_validacion.md`.
7. `docs/lectura_validacion_v61.md` — lectura de la validación: 8 casos run_2/run_4
   (commit `ea793b5`, 2026-07-16).
8. `docs/diseno_v7_s1.md` — diseño de v7 = v6.1-D + S1, la segunda pasada con fuentes
   forzadas (commit `fbdb8db`, 2026-07-16).
9. `docs/lectura_b4_s1.md` — lectura de B4, el desarrollo de S1 contra el dev iterable
   (commit `f08c3ac`, 2026-07-17).
10. `docs/casos_gate_cqn.md` — vara del gate CQN: adjudicación de los 10 casos, sellada
    por inexistencia (commit `1d4e7a8`, 2026-07-18).
11. `docs/lectura_gate_cqn.md` — lectura head-to-head del gate CQN, v6.1-D vs v7/S1
    (commit `7cef0ba`, 2026-07-19).
12. `docs/diseno_ciclo2.md` — diseño pre-registrado del ciclo 2: D7/v6.2-D, guarda de
    dominio, portador robusto (commit `b84668e`, 2026-07-19); **enmienda §4bis**
    (requisito de fundamento del pasaje, `fuente_no_funda`) en commit `56bc5aa`
    (2026-07-19).
13. `docs/casos_gate_cqn2.md` — vara del gate CQN2: adjudicación de los 11 casos,
    sellada antes de toda corrida (commit `65bea99`, 2026-07-19).
14. `docs/lectura_ciclo2.md` — lectura final del ciclo 2: head-to-head a tres columnas
    sobre el gate CQN2; deja fijado el instrumento del proyecto = v7-v0.4b (commit
    `7cc3bd2`, 2026-07-20).

## (iii) Evidencia y auditoría

Material de auditoría de las adjudicaciones — no es lectura, es respaldo. Cada lectura
de la capa (ii) cita aquí sus verbatims, expedientes y verificaciones determinísticas.

- `docs/evidencia_capa_d/` — unidades D1–D6 de la capa determinística.
- `docs/evidencia_vara_v3/` — re-adjudicación de la vara v3 y auditoría de truncamiento.
- `docs/evidencia_piloto/` — expedientes y verificaciones del piloto v6.0-D.
- `docs/evidencia_validacion/` — expedientes y verificaciones de la validación v6.1-D
  (incluye el censo run_2/run_4).
- `docs/evidencia_dev_v7/` — expedientes del dev de v7/S1.
- `docs/evidencia_v7/` — arquitectura v7 y resultados de S1 v0.1→v0.3.1.
- `docs/evidencia_gate_cqn/` — barrido de KG y censo del gate CQN.
- `docs/evidencia_gate_cqn2/` — barrido, censo y custodia del gate CQN2.
- `data/experiment/evaluacion/posthoc_run/` — los artefactos crudos citados por todo lo
  anterior (trazas off/on, JSONs congelados de gates y calibraciones, summaries),
  incorporados a git en las tandas 1 y 1b (commits `fb685a7` y `7942ead`, 2026-07-20).
- `data/experiment/evaluacion/frozen_run/` y `frozen_smoke/` — la corrida congelada de
  la Fase 2.3 que seleccionó al grafo ganador (trazas, checkpoints, reporte final).

## (iv) Corpus y datos

- `data/experiment/subset/` — los 5 Textos Ordenados del experimento, sellados y
  READ-ONLY (PDFs gitignoreados por política; un clone fresco no los trae).
- `data/experiment/evaluacion/queries/` — los eval sets sellados:
  `eval_set_v1.json` (23 CQs, commit `7d118ee`, 2026-06-09), `eval_set_v2.json`
  (+8 CQs difíciles, commit `7cfe143`, 2026-07-06), `eval_set_cqn.json` (15 preguntas,
  commit `2b8d449`, 2026-07-17) y `eval_set_cqn2.json` (15 preguntas, commit `df29525`,
  2026-07-19), con sus variantes `_runtime` y el log `run5_merges.json`.
- `data/experiment/run_1_cookbook/ … run_5_hybrid/` — las 5 estrategias de la Fase 2.2:
  `kg.json` (grafo congelado; run_3 es el ganador y baseline), `schema.md`, `report.md`
  y `code/` con su cache de reproducibilidad. Solo run_3 conserva `kg_visual.html`
  commiteado; las demás visualizaciones se regeneran (ver `docs/ARQUITECTURA.md`).
- `data/raw/` — el corpus regulatorio BCRA descargado (PDFs/HTML gitignoreados por
  política; `manifiesto.csv`, checkpoint y logs sí versionados;
  descargador: `scripts/download_bcra.py`).
- `data/experiment/evaluacion/cache/` — crudos completos de todas las llamadas a la API
  (SQLite, gitignoreados; el patrón de captura está en la skill `llm-capture`).
- `docs/tesis/` — mis borradores de escritura de la tesis (fuera de version control por
  decisión mía; solo el `.gitkeep` está tracked).
