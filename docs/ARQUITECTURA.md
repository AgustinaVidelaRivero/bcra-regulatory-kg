# Arquitectura del repo — bcra-regulatory-kg

**Generado:** 2026-07-09, sobre el working tree en HEAD `7db9020` (limpio).
**Método:** cada ruta y afirmación de este documento sale de `ls`/`find`/`grep`/lectura
real de los archivos en la sesión que lo generó — no de memoria. Donde el propósito de
un archivo no fue evidente leyéndolo, dice `[propósito no evidente — confirmar con
Agustina]`. La numeración de fases es la canónica de `CLAUDE.md`: **2.3** = evaluación
congelada · **2.3+** = instrumentación post-hoc · **2.4** = verificador · **2.5** =
refinamiento.

---

## 1. Árbol de directorios (profundidad 2, anotado)

```
.
├── .claude/                      Config local de Claude Code (settings.local.json)
│   └── skills/                   4 skills del pipeline: eval-pipeline, frozen-eval-audit,
│                                 kg-refinement, llm-capture (cada una: SKILL.md + references/)
├── _archive_riesgo_crediticio/   Pivote anterior del proyecto, archivado (no se usa)
│   ├── data/                     kg/, processed/, raw/ del pivote viejo
│   ├── docs/                     schema/ del pivote viejo
│   └── scripts/                  download_bcra.py (versión vieja, duplica nombre con scripts/)
├── data/
│   ├── experiment/               El experimento de la tesis (ver §2): run_1..run_5, subset, evaluacion
│   ├── kg/                       VACÍO (solo .gitkeep) — placeholder
│   ├── processed/                VACÍO (solo .gitkeep) — placeholder
│   └── raw/                      Corpus BCRA descargado: 00_marco_legal, 01_textos_ordenados,
│                                 02_comunicaciones_A, 03_comunicaciones_B, 06_tachado_negrita,
│                                 _backups + manifiesto.csv, manifiesto_descartados.csv,
│                                 checkpoint.json, log.txt (los PDF/HTML están gitignoreados)
├── docs/
│   ├── defensa/                  guion_presentacion.md, preguntas_jurado.md
│   ├── literatura/               bibliography.bib, comparativa.md, gaps.md, papers/, resumenes/,
│   │                             papers_a_buscar.md
│   ├── ppf/                      PPF_Prel_VidelaRivero_Agustina.pdf, main.tex (LaTeX del PPF)
│   ├── schema/                   experiment_protocol.md, experiment_instance_template.md,
│   │                             corpus_analysis_for_schema.md, legacy/ (v0.1 del schema)
│   └── hallazgos_tesis.md        Hallazgos H1–H13 para Resultados/Discusión y ronda de feedback
├── notebooks/                    01_turtle_basics.ipynb (intro rdflib, etapa temprana; nada lo usa)
├── scripts/                      shapes_validator.py (shapes S1-S12 sobre los kg.json)
│   └── adhoc/                    b5_minirun_ext.py (mini-run de validación del scraper)
├── src/                          scraper/: download_bcra.py (subcomandos B1..B9),
│   │                             report_b4_b5.py, retry_persistent_fails.py;
│   │                             extraction/ y kg/ placeholders (solo __init__.py)
├── tests/                        VACÍO (solo .gitkeep) — el test real vive en evaluacion/
├── CLAUDE.md                     Memoria del proyecto (fases, reglas, lecciones) — fuente de verdad
├── README.md                     Presentación del proyecto (autora, mentores)
└── requirements.txt              Python 3.11 (.python-version); anthropic==0.100.0, pypdf, rdflib, etc.
```

Dentro de `data/experiment/` (profundidad 3, es el corazón del repo):

```
data/experiment/
├── subset/                       Los 5 TOs del experimento (PDFs) — READ-ONLY y gitignoreados
├── run_1_cookbook/               ┐
├── run_2_papers/                 │ Fase 2.2: una carpeta por estrategia de schema.
├── run_3_ppf_core/               │ Cada una: kg.json, schema.md, report.md, kg_visual.html, code/
├── run_4_schema_light/           │ run_3 = GANADOR de la Fase 2.3
├── run_5_hybrid/                 ┘
└── evaluacion/                   Fases 2.3 → 2.5: scripts, datos frozen, post-hoc, verificador (§3, §4)
```

---

## 2. Estado por zona

| Zona | Estado | Detalle |
|---|---|---|
| `data/experiment/subset/` | [CONGELADO] | Los 5 PDFs fuente, read-only. Además **gitignoreados** (`.gitignore:34` `data/experiment/**/*.pdf`) — un clone fresco NO los tiene. |
| `data/experiment/run_1..run_5/` | [CONGELADO] | Los 5 `kg.json` de la Fase 2.2. La congelación de `run_3` se levanta SOLO bajo el pipeline de refinamiento, sobre una **copia** (`run_3_refinamiento/` — al 2026-07-09 **no existe todavía**); el original queda como baseline. |
| `evaluacion/loader.py`, `harness.py`, `judge.py`, `run_frozen.py` | [CONGELADO] | Código congelado de la Fase 2.3 (juez v2.1.1). No se editan. |
| `evaluacion/frozen_run/`, `frozen_smoke/` | [CONGELADO] | Datos de la corrida congelada que seleccionó a run_3 (agg, checkpoints, reporte_final.md, 115 trazas tracked) y su smoke previo. |
| `evaluacion/queries/eval_set_v1.json` | [CONGELADO] | 23 CQs, diseño ciego, frozen pre-corrida. |
| `evaluacion/adjudicacion_FIRMADO.json` | [CONGELADO] | Adjudicación humana firmada de la Fase 2.3. |
| `evaluacion/` (raíz: verificador.py, pdf_locate.py, verifier_pilot.py, runners/run_posthoc.py, llm_cache.py, runners/reporte_verificador_html.py) | [ACTIVO] | Instrumentación 2.3+ y verificador 2.4. Acá se trabaja ahora. |
| `evaluacion/queries/eval_set_v2*.json` | [ACTIVO] | v1 + 8 CQs nuevas (CQ-040–047); dataset del refinamiento 2.5. |
| `evaluacion/posthoc_run/revision_prompt_v4/` | [ACTIVO] | Paquete de revisión del prompt v4 armado para la ronda de feedback — lo ÚNICO tracked de `posthoc_run/`. |
| `.claude/skills/` | [ACTIVO] | Las 4 skills operativas del pipeline. |
| `docs/` (hallazgos, defensa, ppf) | [ACTIVO] | Documentación de tesis en curso. |
| `evaluacion/cache/` | [SCRATCH] | Gitignoreado por `.gitignore:56` (`data/experiment/evaluacion/cache/`). Crudos completos de la API: calls.db, verificador.db, verifier_pilot.db, calls.db.verif_backup. |
| `evaluacion/posthoc_run/` (todo salvo revision_prompt_v4) | [SCRATCH] | Gitignoreado por `.gitignore:57-58` (`posthoc_run/*` + excepción `!.../revision_prompt_v4/`). Incluye: traces/{off,on}, calibracion_verificador{,_v2,_v3,_v4}, auditoria_gt, pilot_verificador, reportes_html, esquema_slides, summary_{off,on}_run_X.json. |
| `evaluacion/logs/` | [SCRATCH] | Gitignoreado — pero por la regla **genérica** `logs/` (`.gitignore:47`), no por una decisión explícita. Ver Inconsistencia #2. |
| `evaluacion/.env` | [SCRATCH] | Gitignoreado por `*.env` (`.gitignore:43`). API key. |
| `data/raw/**/*.pdf|html` | [SCRATCH] | Gitignoreados (`.gitignore:32-34`); la metadata (manifiesto.csv, checkpoint.json, log.txt) SÍ está versionada. |

---

## 3. Scripts de `data/experiment/evaluacion/` (19 .py)

"Quién lo usa" = imports reales (`grep "from X import\|import X"` sobre los .py de la carpeta;
ninguno se importa desde fuera de `evaluacion/`). "API" = hace llamadas a la API Anthropic.

| Script | Qué hace | Quién lo importa | API |
|---|---|---|---|
| `loader.py` [CONGELADO] | Adaptador uniforme de los 5 kg.json: normaliza desviaciones de schema en memoria, mergea duplicados de run_5 | 14 scripts (todos menos gen_demo_html, llm_cache, pdf_locate, test_llm_cache) | No |
| `harness.py` [CONGELADO] | Agente respondedor KG-RAG: Haiku 4.5 fijo, temp 0, 3 tools de grafo (buscar_nodos / ver_nodo / ver_vecinos) | judge, run_frozen, run_manual, run_posthoc, run_etapa2, ab_caching, ab_control, ab_investigate_cq029, adjudicacion_worksheet, verificador | Sí |
| `judge.py` [CONGELADO] | LLM-as-judge v2.1.1: Sonnet, dos pasos, ciego al grafo; changelog v1→v2.1.1 en el docstring | run_frozen, run_posthoc, ab_caching, ab_control, ab_investigate_cq029 | Sí |
| `run_frozen.py` [CONGELADO] | Pipeline de la corrida congelada: eval_set_v1 × 5 grafos × N reps, veredicto modal, checkpoints | nadie (entry point) | Sí |
| `analisis/run_manual.py` | Corre UNA pregunta del pool contra un grafo (loop manual 2.3), anexa traza idempotente | nadie (entry point) | Sí |
| `runners/validate_loader.py` | Valida loader sobre los 5 grafos: reabre cada kg.json por su cuenta y cruza conteos (checks C1..) → `01_validacion_loader.md` | nadie (entry point) | No |
| `analisis/ab_caching.py` | A/B de prompt caching multi-turn (6 preguntas dev_pool, run_3, sin/con cache) → `03_ab_caching.md` | nadie (entry point) | Sí |
| `analisis/ab_control.py` | Control de no-determinismo del A/B: las 3 divergentes, off vs off2 → `03b_ab_control.md` | nadie (entry point) | Sí |
| `analisis/ab_investigate_cq029.py` | Investigación puntual de CQ-029 (K corridas sin/con cache) → `03c_cq029_investigacion.md` | nadie (entry point) | Sí |
| `analisis/adjudicacion_worksheet.py` | Reorganiza la cola de adjudicación humana en worksheet (propagación solo por identidad estricta) | nadie (entry point) | No |
| `runners/run_etapa2.py` | Reporte ETAPA 2: aplica veredictos del worksheet FIRMADO y re-emite reporte_final.md | nadie (entry point) | No |
| `analisis/gen_demo_html.py` | Genera `demo_evaluacion.html` (trazas + juez, datos reales de frozen_run/) para mostrar en reunión | nadie (entry point) | No |
| `llm_cache.py` (2.3+) | Caché SQLite + captura del crudo íntegro; wrapper drop-in del cliente Anthropic, key determinística, namespace versionado | run_posthoc, verifier_pilot, verificador, test_llm_cache | Envuelve al cliente (paga API solo en cache-miss del que lo usa) |
| `tests/test_llm_cache.py` | Test aislado de la caché con cliente FALSO (Message real por model_validate); PASS/FAIL exit 0/1 | nadie (entry point) | No (explícitamente sin API) |
| `runners/run_posthoc.py` (2.3+) | Runner instrumentado: re-corrida rica con thinking ON/OFF vía ParamOverrideClient, sin tocar lo congelado; `--preflight`/`--verify-replay` | nadie (entry point) | Sí (cacheada) |
| `verifier_pilot.py` (2.4, piloto) | Piloto del verificador claim-level (¿defecto de KG o de agente?): mapeo claim→nodo con Haiku, verificación con Opus, evaluador A ciego con Sonnet | verificador (usa load_rep, recover_seen, _extract_json) | Sí (cacheada en cache/verifier_pilot.db) |
| `pdf_locate.py` (2.4) | Localización de pasajes en los PDFs del subset (por punto con prose_score anti-índice, o por página). Autocontenido, solo pypdf | verificador, verifier_pilot | No |
| `verificador.py` (2.4) | Verificador agéntico v4: por cada falla investiga por qué falló y atribuye (grafo vs agente) con taxonomía cerrada, arrancando del síntoma (anti-sesgo) | reporte_verificador_html | Sí (cacheada en cache/verificador.db) |
| `runners/reporte_verificador_html.py` (2.4) | Reporte HTML por corrida del verificador (`--input --run --label [--ground-truth]`); estampa commit y namespace en meta.json e index acumulado | nadie (entry point) | No |

Documentos `.md` numerados en la misma carpeta (reportes de cada etapa 2.3/2.3+):
`00_inventario.md` (inventario y desviaciones de schema de los 5 kg.json),
`01_validacion_loader.md`, `02_calibracion_juez.md`, `03_ab_caching.md`,
`03b_ab_control.md`, `03c_cq029_investigacion.md`, `04_auditoria_instrumentacion.md`.

---

## 4. Dónde vive cada artefacto, por fase

**Corpus (Fase 1 / B.x)**
- Descarga: `src/scraper/download_bcra.py` (subcomandos B1..B9) + `report_b4_b5.py`, `retry_persistent_fails.py`.
- Datos: `data/raw/` (PDF/HTML gitignoreados; manifiesto.csv y logs versionados).

**Fase 2.2 — construcción de los 5 grafos**
- `data/experiment/run_X_*/`: kg.json + schema.md + report.md + kg_visual.html + code/ por estrategia.
- Solo run_3 conserva `kg_visual.html` commiteado; las visualizaciones de los demás runs se regeneran con `cd data/experiment/run_X_*/code && python visualize.py` (en run_1: `python 07_visualize.py`; requiere `pyvis` instalado).
- Protocolo: `docs/schema/experiment_protocol.md`, `experiment_instance_template.md`.

**Fase 2.3 — evaluación congelada**
- Eval sets: `evaluacion/queries/` — `eval_set_v1.json` (23 CQs, congelado), `candidatas.json`
  (pool ciego original), `dev.json` / `dev_pool.json` (desarrollo, descartables).
- Código: `loader.py`, `harness.py`, `judge.py`, `run_frozen.py` (congelados).
- Corrida: `evaluacion/frozen_run/` (agg_run_X.json, checkpoint_run_X.md, reporte_final.md,
  retries_run_X.jsonl, traces/ con 115 archivos tracked). Smoke previo: `frozen_smoke/`.
- Trazas manuales: `evaluacion/trazas/` (manual_run_1.json, manual_run_3.json, 20260609_155542_run_3_dev.json).
- Calibración del juez: `02_calibracion_juez.md` (changelog v1→v2.1.1 también en judge.py).
- Adjudicación humana: `adjudicacion_pendiente.json` → `adjudicacion_worksheet.{json,md}` →
  `adjudicacion_FIRMADO.json` (firmado) → `runners/run_etapa2.py` re-emite reporte_final.md.
- Demo de reunión: `demo_evaluacion.html` (generado por analisis/gen_demo_html.py).

**Fase 2.3+ — instrumentación post-hoc**
- Código: `llm_cache.py` (+ `tests/test_llm_cache.py`), `runners/run_posthoc.py`.
- Caché de crudos: `evaluacion/cache/*.db` [SCRATCH].
- Trazas ricas: `posthoc_run/traces/{off,on}/` y `posthoc_run/summary_{off,on}_run_X.json` [SCRATCH].
- Auditoría de qué se persistió: `04_auditoria_instrumentacion.md`.

**Fase 2.4 — verificador**
- Código: `verifier_pilot.py` (piloto), `verificador.py` (agéntico v4), `pdf_locate.py`,
  `runners/reporte_verificador_html.py`.
- Piloto y mapa de defectos: `posthoc_run/pilot_verificador/` (mapa_agregado.json,
  mapa_depurado.json, verificador_scale_full.json, evaluador_a.json, ...) [SCRATCH].
- Calibraciones del verificador v1–v4: `posthoc_run/calibracion_verificador{,_v2,_v3,_v4}/` [SCRATCH].
- Auditoría de ground truth: `posthoc_run/auditoria_gt/` (CQ-017/020/025/031/034.md + _barrido.py) [SCRATCH].
- Reportes HTML: `posthoc_run/reportes_html/` (index.html + un dir por corrida con reporte.html
  y meta.json) [SCRATCH].
- Paquete de revisión del prompt v4: `posthoc_run/revision_prompt_v4/` (prompt_v4.md, caso_CQ-020.md,
  caso_CQ-034.md, tabla_v1_v4.md) — **tracked** (excepción en .gitignore).
- Hallazgos: `docs/hallazgos_tesis.md` (H1–H13).
- Datos para slides: `posthoc_run/esquema_slides/datos.md` [SCRATCH].

**Fase 2.5 — refinamiento (en preparación)**
- Skill: `.claude/skills/kg-refinement/` (SKILL.md + references/: casos_control.md,
  taxonomia.md, formato_propuesta.md, preparar-run3-refinamiento.md).
- Dataset: `queries/eval_set_v2.json` (31 CQs) + `eval_set_v2_nuevas.json` (las 8 nuevas).
- Copia de trabajo `run_3_refinamiento/`: **NO existe todavía** (verificado con find, 2026-07-09).

**Skills del pipeline (transversales):** `.claude/skills/eval-pipeline/` (correr evaluaciones),
`frozen-eval-audit/` (auditar/reproducir el frozen sin API), `llm-capture/` (patrón de caché
obligatorio), `kg-refinement/` (pipeline 2.5).

---

## 5. Inconsistencias detectadas

1. **Numeración de fases:** NO se encontró ningún archivo con la numeración vieja
   ("2.4" = refinamiento). Todas las menciones a "Fase 2.4" del repo (verificador.py,
   pdf_locate.py, verifier_pilot.py:175, runners/reporte_verificador_html.py, hallazgos_tesis.md,
   llm-capture/SKILL.md:22) refieren al **verificador** — consistente con la canónica.
   Las únicas menciones del error histórico son auto-aclaratorias (CLAUDE.md:109,
   kg-refinement/SKILL.md).
2. **`evaluacion/logs/run5_merges.json` está gitignoreado por accidente de la regla genérica
   `logs/` (`.gitignore:47`)**, no por decisión explícita: CLAUDE.md lo describe como el log
   de auditoría de los merges de run_5, pero no está versionado (`git check-ignore -v` lo
   confirma). No se corrigió — solo se señala.
3. **Los 5 PDFs de `data/experiment/subset/` están gitignoreados** (`.gitignore:34`):
   un clone fresco no tiene el corpus del experimento. Coherente con la política de no
   versionar PDFs, pero conviene saberlo antes de clonar en otra máquina.
4. **Historia del paquete de entrega:** el paquete de entrega original vivió fuera del
   repo y no se conserva; su contenido quedó absorbido por los documentos de `docs/`
   listados en `INDICE.md`. (La carpeta de revisión que sí quedó en el repo es
   `posthoc_run/revision_prompt_v4/`, tracked.)
5. **`scripts/adhoc/b5_minirun_ext.py`** dice en su docstring "Uso: python /tmp/b5_minirun_ext.py"
   — no coincide con su ubicación real en el repo.
6. **Placeholders vacíos:** `src/extraction` y `src/kg` contienen solo
   `__init__.py`; `tests/`, `data/kg/`, `data/processed/` solo `.gitkeep`. El único test real
   (`tests/test_llm_cache.py`) vive en `data/experiment/evaluacion/`, no en `tests/`.
7. **Nombre duplicado:** `src/scraper/download_bcra.py` (vigente) y
   `_archive_riesgo_crediticio/scripts/download_bcra.py` (pivote archivado).
8. **`evaluacion/cache/calls.db.verif_backup`** — backup ad-hoc junto a calls.db
   [propósito/momento del backup no evidente — confirmar con Agustina].
9. **Dos convenciones para trazas:** `evaluacion/trazas/` (castellano, loop manual 2.3) vs
   `frozen_run/traces/` y `posthoc_run/traces/` (inglés). Mismo concepto, dos nombres.
10. **`frozen_run/reporte_final_draft.md`** convive con `reporte_final.md` (el draft quedó
    superseded por la versión post-adjudicación).
11. **Huérfano:** `notebooks/01_turtle_basics.ipynb` (intro a rdflib de la etapa temprana);
    nada en el repo lo referencia.
