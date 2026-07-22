# Contratos de datos del pipeline de evaluación

> **Estado verificado:** campos y valores verificados contra el repo el
> 2026-07-06 (HEAD `454bd9d`, 2026-06-28, más working tree sin commitear),
> incluyendo parseo real de `queries/eval_set_v2.json`.

## Sets disponibles y para qué sirve cada uno

**Regla: smoke tests con material de desarrollo; conclusiones SOLO con eval sets.**

| Archivo | Preguntas | Clase | Notas (verificadas por parseo) |
|---|---:|---|---|
| `queries/eval_set_v1.json` | 23 | **eval set** | congelado de la Fase 2.3 (el que seleccionó al ganador; default de `run_posthoc`, `data/experiment/evaluacion/runners/run_posthoc.py:63`) |
| `queries/eval_set_v2.json` | 31 | **eval set** | v1 + 8 nuevas difíciles (CQ-040–047); dataset del refinamiento (Paso 1 de `kg-refinement`) |
| `queries/dev.json` | 3 | desarrollo | sin `categoria` ni referente; default del CLI de `harness.py` |
| `queries/dev_pool.json` | 17 | desarrollo | con referente (salvo `dev_unans_1`); pool de calibración del juez (`data/experiment/evaluacion/judge.py:91`) y del smoke de `run_frozen` |
| `queries/candidatas.json` | 39 | desarrollo | candidatas de generación de las que salieron los eval sets |
| `queries/eval_set_v2_nuevas.json` | 8 | desarrollo | solo las 8 nuevas de v2, como material de trabajo — para correr v2 usar `eval_set_v2.json` completo |

## Input — archivo de queries

Raíz aceptada: lista `[{...}]` o dict `{"preguntas": [...]}`
(`data/experiment/evaluacion/runners/run_posthoc.py:272-274`).

Campos por pregunta (los de `eval_set_v2.json`, parseados):

| Campo | Quién lo consume |
|---|---|
| `id` | nombre del archivo de traza y logging (`data/experiment/evaluacion/runners/run_posthoc.py:188`) |
| `pregunta` | agente y juez |
| `categoria` | juez — `"unanswerable"` activa la evaluación de abstención/especulación; cualquier otra la anula (`data/experiment/evaluacion/judge.py:234-236`) |
| `respuesta_esperada`, `cita_textual`, `ground_truth_secciones` | el REFERENTE auditable del Paso 2 del juez (`data/experiment/evaluacion/judge.py:283-288`) |
| `dificultad`, `nota`, `tos_fuente` | metadata; el pipeline no los consume |

Categorías reales de `eval_set_v2.json` (31 preguntas): `factual_directa` 10,
`multi_norma` 9, `cadena_restriccion_excepcion` 8, `unanswerable` 4.

**Implicancia:** una query sin `respuesta_esperada`/`cita_textual`/
`ground_truth_secciones` se corre igual, pero el juez queda sin referente — el
veredicto no es interpretable. No correr sets incompletos sin señalarlo.

## Output — rep dict (uno por repetición, en `{qid}.json`)

Campos (`data/experiment/evaluacion/runners/run_posthoc.py:201-217`):

| Campo | Contenido |
|---|---|
| `rep`, `qid`, `run`, `categoria`, `thinking_enabled` | identificación |
| `failed_trace` | `true` si `not parse_ok`, truncado por max_tokens, o error (`data/experiment/evaluacion/runners/run_posthoc.py:193`) |
| `trace` | el `QuestionTrace` del harness: `steps` (tool calls), `api_calls`, `final_json`, `seen_provenances`, `citations_unseen_*`, tokens, `cost_usd` (`data/experiment/evaluacion/harness.py:292-315`) |
| `raw_turns_agent` / `raw_turns_judge` | crudo íntegro por turno recuperado de la caché (incl. thinking blocks si ON) |
| `judge` | `null` si `failed_trace`; si no: `{verdict, step1, step2, usage, errors}` (`data/experiment/evaluacion/judge.py:299-303`) |
| `harness_cost` / `judge_cost` | USD por rep (precios: Haiku 1.00/5.00, Sonnet 3.00/15.00 por MTok — `data/experiment/evaluacion/runners/run_posthoc.py:71-72`) |

## El veredicto del juez (`judge.verdict`)

Dimensiones (`data/experiment/evaluacion/run_frozen.py:113-114` las lista;
se computan en `data/experiment/evaluacion/judge.py:230-267`):

- `correctitud` ∈ {correcta, parcial, incorrecta} — **determinístico**: central
  falsa → incorrecta; secundaria falsa → parcial; `no_soportado` NUNCA baja
  correctitud (`data/experiment/evaluacion/judge.py:204-211`).
- `completitud` ∈ {completa, parcial} — todas las patas cubiertas o no.
- `cita_documento_correcto` (bool), `cita_precision` ∈ {punto, pagina, ausente}.
- `abstencion`, `especulacion_en_prosa` — SOLO para `categoria == "unanswerable"`;
  `null` en el resto.
- `afirmaciones_no_soportadas` — lista + conteos, centrales vs secundarias.
- `requiere_adjudicacion_humana` — `true` si hay ≥1 afirmación CENTRAL
  no_soportada (`data/experiment/evaluacion/judge.py:244`). Esas trazas van a
  adjudicación de la autora contra los PDFs; no se resuelven solas.

`correctitud`/`completitud` son `null` para unanswerable (ahí rigen
`abstencion`/`especulacion_en_prosa`).

## Output — summary (`posthoc_run/summary_{label}_{run}.json`)

Campos (`data/experiment/evaluacion/runners/run_posthoc.py:250-261`): `run_key`, `label`,
`thinking_enabled`, `timestamp`, `n_preguntas`, `reps_por_pregunta`,
`n_reps_total`, `n_failed`, `costo_usd`, `agent_cache_stats` / `judge_cache_stats`
(con `hit_rate`), `code_version`, `graph_fingerprint`.

Para el reporte verificable: `costo_usd` y `n_failed` salen de acá; el detalle
por pregunta, de los `{qid}.json`.
