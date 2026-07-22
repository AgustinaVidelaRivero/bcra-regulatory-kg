# Mapa de artefactos del frozen + walkthrough de auditoría de un veredicto

> **Estado verificado:** estructuras parseadas de los archivos reales y citas
> `archivo:línea` verificadas contra el repo el 2026-07-06 (HEAD `454bd9d`,
> 2026-06-28, más working tree sin commitear).

Todo vive en `data/experiment/evaluacion/` salvo indicación.

## Los artefactos, eslabón por eslabón

### 1. Trazas congeladas — `frozen_run/traces/run_X/CQ-YYY.json`

Lista de N=3 reps. Campos por rep (parseados de `run_3/CQ-002.json`): `qid`,
`run`, `rep`, `categoria`, `respuesta`, `citas`, `respondible`, `verdict` (el
veredicto completo del juez para ESA rep), `parse_ok`, `failed_trace`,
`truncated_max_tokens`, `hit_tool_limit`, `tool_calls_used`, `error`,
`judge_error`, `harness_cost`, `judge_cost`. **Sin `steps`** (limitación
registrada, `data/experiment/evaluacion/run_frozen.py:46-58`).

### 2. Agregados — `frozen_run/agg_run_X.json`

23 celdas (una por pregunta). Estructura por celda (parseada):
`qid`, `categoria`, `reps_meta` (resumen liviano por rep), y `agg` =
`{n_reps, n_validas, dimensiones}` donde cada dimensión trae
`{modal, unanime, distribucion, n}` — p. ej.
`{"modal": "correcta", "unanime": true, "distribucion": {"\"correcta\"": 3}, "n": 3}`.
Empate modal → `sin_consenso` (no se inventa desempate,
`data/experiment/evaluacion/run_frozen.py:9-12`).

### 3. Checkpoints — `frozen_run/checkpoint_run_X.md`

Revisión operador por grafo. Regenerable desde el agg con
`--mode regen --graph run_X` (`data/experiment/evaluacion/run_frozen.py:833-847`;
incorpora la cola de adjudicación y el summary del selftest si existen).

### 4. Reporte etapa 1 — `frozen_run/reporte_final_draft.md`

Generado por `--mode report` → `build_report()`
(`data/experiment/evaluacion/run_frozen.py:646-808`). Regla clave: toda celda
answerable con ≥1 afirmación central no_soportada queda
`pendiente_adjudicacion` — en particular, **TODAS las celdas `multi_norma` de los
5 grafos** quedaron retenidas (hallazgo metodológico registrado en el propio
reporte, `data/experiment/evaluacion/run_frozen.py:787-797`).

### 5. Adjudicación humana — `adjudicacion_pendiente.json` → `adjudicacion_FIRMADO.json`

La cola la llena la corrida (`data/experiment/evaluacion/run_frozen.py:26-27`);
el FIRMADO es el worksheet resuelto y firmado por la autora. **Ninguno de los dos
se edita desde una skill.**

### 6. Reporte etapa 2 (final) — `frozen_run/reporte_final.md`

Lo re-emite `python runners/run_etapa2.py` (`data/experiment/evaluacion/runners/run_etapa2.py:41`):
aplica los veredictos del FIRMADO vía el log de propagación, recomputa la
correctitud retenida con el mapping congelado v2.1.1 (verdadera no penaliza /
falsa → incorrecta / parcial → parcial / no_verificable → indeterminable;
precedencia incorrecta > parcial > indeterminable > correcta) y re-agrega modal
(`data/experiment/evaluacion/runners/run_etapa2.py:10-27`). No toca trazas, juez ni
eval_set.

### Artefactos de soporte

- `frozen_run/retries_run_X.jsonl` — log de retries de infraestructura por grafo
  (`data/experiment/evaluacion/run_frozen.py:884-885`). Los errores de infra se
  reintentan; parse errors y cortes por max_tokens NO (comportamiento del sistema,
  `data/experiment/evaluacion/run_frozen.py:19-22`).
- `frozen_run/selftest_retry.json` — resultado del selftest del RetryingClient
  (`data/experiment/evaluacion/run_frozen.py:853-862`; ojo: `--mode selftest` lo
  REESCRIBE).
- `01_validacion_loader.md` — reporte de integridad C1–C8 (lo reescribe
  `runners/validate_loader.py`).
- `adjudicacion_worksheet.md` / `.json` — worksheet con el que se firmó.

## Walkthrough: auditar el veredicto de (qid, run, dimensión)

1. **Reps crudas:** abrir `frozen_run/traces/{run}/{qid}.json` y leer
   `verdict.{dimensión}` de cada una de las 3 reps. Anotar también `parse_ok` /
   `failed_trace` (una rep fallida no vota).
2. **Agregado:** en `frozen_run/agg_{run}.json`, buscar la celda con ese `qid` y
   verificar que `agg.dimensiones.{dimensión}.distribucion` coincide con lo
   contado a mano en el paso 1, y que `modal` es la moda (o `sin_consenso` si hay
   empate).
3. **¿Estuvo retenida?** Si la dimensión es `correctitud` y la celda aparece en
   `adjudicacion_pendiente.json` (filtrar por `run` + `qid`): el draft la reporta
   `pendiente_adjudicacion`; el veredicto FINAL sale de `reporte_final.md`, y su
   justificación de la(s) entrada(s) correspondiente(s) en
   `adjudicacion_FIRMADO.json`.
4. **Reporte:** confirmar que la fila correspondiente de
   `reporte_final_draft.md` (etapa 1) y/o `reporte_final.md` (etapa 2) refleja lo
   anterior. Si algo no cuadra, ANTES de concluir error: regenerar el reporte
   (`--mode report` / `runners/run_etapa2.py`) y comparar con `git diff` — distingue
   "reporte desactualizado" (diff no vacío) de "inconsistencia real en los datos"
   (diff vacío y sigue sin cuadrar → reportar a la autora, no tocar).

## Recordatorio de capas (ruling 2026-06-10)

Reporting (eslabones 3, 4, 6 y los reportes de soporte) se regenera/corrige con
registro. Sistema bajo evaluación (eslabones 1, 2, 5 y los `kg.json`) no se toca
jamás (`data/experiment/evaluacion/run_frozen.py:33-45`).
