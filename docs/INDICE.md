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
- `docs/nomenclatura_grafos.md` — nombres canónicos de los tres grafos medidos en EV2
  (KG-Base `12c226e2` / KG-Refinado `26fac8b4` / KG-Reextraído `8e2eadee`): alias
  históricos, paths, shas, commit de sellado y generación de pipeline de cada uno, la
  colisión del alias "v2" y la regla de uso para toda la prosa (commit `237fb8f`,
  2026-08-17). Leer antes de cualquier documento que nombre un grafo.

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
15. `docs/spec_evaluacion_intrinseca.md` — pre-registro del set de métricas de
    evaluación intrínseca del grafo (M1–M11): regla constitucional de pareo
    sub-fusión/sobre-fusión y denominador aguas arriba, predicciones selladas sobre
    el par defectuoso/re-ensamblado, régimen de dos pasadas sin umbrales (commit
    `cdf90e6`, 2026-07-30, anterior a `scripts/metricas_intrinsecas.py`; laudo M7 en la
    fila M7, commit `38ac8b1`, 2026-08-02).
16. `docs/protocolo_gate_u5.md` — protocolo pre-registrado del gate U5: el verificador
    sobre la familia v2/v3, 4 casos con vara sellada y reglas de acierto, criterio
    cero-silenciosos + ≥3/4, tope doble (commit `49721fd`, 2026-08-02); **Enmienda §8**
    (techo secundario renovado a USD 30 total, alcance exclusivo completar el gate) en
    commit `6150971` (2026-08-02).
17. `docs/lectura_gate_u5.md` — lectura del gate U5: EL GATE PASA (3 aciertos de 4,
    cuarto en rama de lectura B′, cero silenciosos); el verificador asciende a
    VALIDADO-EN-FAMILIA v2/v3 (Motor 3: diagnóstico automático, laudo humano) y deja
    el hallazgo residual BKL-0023 dentro de su propio gate (commit `f5bfb2c`, 2026-08-02).

**Evaluación de los grafos: escalón 1b, re-extracción y EV2** (misma disciplina —
protocolo o pre-registro sellado antes de la corrida, corrida única, lectura contra la
vara — aplicada ahora al grafo y no al verificador; nombres de grafos según
`docs/nomenclatura_grafos.md`).

18. `docs/lectura_escalon1b.md` — lectura sellada del escalón 1b (EV1, 36 preguntas,
    material QUEMADO): `grafo_v2` (`2c7487bb`) 27/36 → KG-Refinado pre-C1–C7 29/36,
    KG-Base 31/36 de referencia; el defecto de ensamblado explicaba la mitad del gap
    (commit `e77b11f`, 2026-07-31; protocolo `docs/protocolo_escalon1b.md`, `d235342`).
19. `docs/diseno_reextraccion_v2.md` — diseño de la re-extracción v2 (issue #8):
    pipeline E0–E5 (chunking estructural con herencia, extractor con prefijo cacheado,
    reduce determinístico, verificador de completitud en contexto fresco, E4/E5), con
    alternativas descartadas y el backlog RX como spec (commit `a8fa053`, 2026-08-10).
20. `docs/diseno_queries_sinteticas.md` — diseño del eje de navegabilidad de EV2:
    muestreo estratificado con control uniforme, gold por provenance invariante entre
    grafos, pares literal / anti-léxica, recall determinístico visto/consultado (commit
    `e40bbb9`, 2026-08-10).
21. `docs/diseno_ev2.md` — diseño de EV2 (issue #4): dos ejes (fidelidad ciega +
    navegabilidad sintética), cohortes núcleo-limpio/dirigida con veredicto solo del
    núcleo, gold anclas+criterios, protocolo de sellado en un commit (commit `7c21053`,
    2026-08-10).
22. `docs/enmienda_01_diseno_reextraccion_v2.md` — Enmienda 01 al diseño de la
    re-extracción: bloques estructurales como unidades de extracción de primera clase,
    motivada por la calibración E0→E3 sobre `pro` (60/117 faltantes solo-en-herencia,
    cola real 29,9 %), con predicciones refutables P1–P3 (commit `baf5608`, 2026-08-11;
    implementación y mini-recalibración: P1 confirmada, P2 refutada, P3 confirmada,
    commit `d082812`).
23. `docs/protocolo_corrida_ev2.md` — protocolo de corrida de EV2 sellado junto con el
    eje de fidelidad (40 preguntas ciegas, 164 criterios) y el manifest sha256: semillas
    `orden-ev2-v1` / `auditoria-ev2-v1`, repeticiones pre-declaradas, anti-cache
    (commit `9c44516`, 2026-08-13 — SELLO EV2, issues #3 y #4).
24. `docs/preregistro_evaluacion_fidelidad_ev2.md` — pre-registro del método de
    evaluación de fidelidad: juez Sonnet N=3 modal con ceguera de grafo, mapping en
    código, calibración solo-U6, adjudicación simétrica 10 %/10 % (commit `be8a84f`,
    2026-08-14; sellado después de la corrida del agente y antes de leer respuesta
    alguna).
25. `data/experiment/ev2_corrida/navegabilidad/reporte_navegabilidad.md` — lectura del
    eje de navegabilidad de EV2: replay determinístico 336/336, brecha literal vs
    anti-léxica confirmada en los tres grafos (recall consultada micro KG-Refinado
    0,958→0,620, KG-Base 0,716→0,493, KG-Reextraído 0,396→0,271 sobre 64/60/44 casos
    presentes), ausencias reportadas aparte (commit `5b02d22`, 2026-08-14).
26. `data/experiment/exploracion/u6_fidelidad/registro_criterios_u6.md` — registro de
    los criterios de calibración del juez (25 preguntas U6 / 92 criterios con cita
    verbatim): redacción por instancia ciega + revisión independiente + laudos A–D
    (commit `2ac2fab`, 2026-08-16).
27. `data/experiment/ev2_juez/calibracion/registro_calibracion.md` — registro de
    calibración del juez de fidelidad EV2: prompt v1 congelado (sha `fd446f8e`), 14/20
    acuerdos + 5 a adjudicación, 3/3 incorrectas detectadas, iteración v1.1 descartada
    por candado de ajuste, cuatro limitaciones documentadas (commit `1a0ac5c`,
    2026-08-16).
28. `data/experiment/ev2_reporte/reporte_ev2.md` — reporte consolidado de EV2 (U-A0 /
    A0.1): tabla definitiva de fidelidad KG-Base 3/20/17, KG-Refinado 5/26/9,
    KG-Reextraído 4/27/9 con vías y etapas, cobertura por criterios, navegabilidad,
    censo, validación del juez (11/12, 52/53), salvedades, desvíos del período y costos
    (USD 35,62), todo recomputable con un comando (commit `40603a9`, 2026-08-17; §12
    completado en `85d9fdb`).
29. `data/experiment/ev2_reporte/regla_atribucion.md` — regla de atribución
    determinística de fallas sellada ANTES del cómputo (A0.2 fase A): cuatro clases
    ausencia_kg / alcanzabilidad / vista_no_consultada / generacion con precedencia,
    veredicto por traza de esa misma respuesta, ancla primaria, abstención como columna
    cruzada (commit `40603a9`, 2026-08-17).
30. `data/experiment/ev2_reporte/salida/atribucion_fallas.md` — lectura de la
    atribución (A0.2 fase B): clase × grafo × veredicto sobre 120 trazas base + 191
    re-corridas, hallazgos H1–H7 (perfiles de falla distintos en el empate 9-9,
    generación clase modal 17/25/21, techo de retrieval 14/7/6, nodo-ancla cáscara),
    replay 120/120 + 191/191, doble corrida byte-idéntica (commit `85d9fdb`,
    2026-08-17).

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
  descargador: `src/scraper/download_bcra.py`).
- `data/experiment/evaluacion/cache/` — crudos completos de todas las llamadas a la API
  (SQLite, gitignoreados; el patrón de captura está en la skill `llm-capture`).
- `docs/tesis/` — mis borradores de escritura de la tesis (fuera de version control por
  decisión mía; solo el `.gitkeep` está tracked).
