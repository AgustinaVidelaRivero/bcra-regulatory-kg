---
name: eval-pipeline
description: Produce trazas juzgadas a partir de (grafo, queries) con el pipeline KG-RAG del repo — agente Haiku sobre el grafo + juez Sonnet v2.1.1 de dos pasos — vía runners/run_posthoc.py (caché + captura de crudos incluidas). Usala SIEMPRE que haya que ejecutar una evaluación: "corré el eval sobre run_X", "evaluá el grafo con eval_set_v2", "generá trazas (juzgadas)", "corré estas preguntas contra el KG", "medí cuánto acierta", "cuántas preguntas falla run_3", "corré el harness/el juez", "probá estas queries nuevas", "re-corré el dataset sobre la copia refinada". Disparala aunque el pedido no diga "evaluación" — si hay que correr preguntas contra un grafo y obtener veredictos, es esto. NO cubre: interpretar/atribuir fallas (skill kg-refinement), auditar la corrida congelada de la Fase 2.3, ni ajustar el juez.
---

# Pipeline de evaluación — trazas juzgadas a partir de (grafo, queries)

Esta skill hace UNA cosa: dado un grafo cargable y un archivo de queries, produce
**trazas juzgadas** (respuesta del agente + veredicto del juez, con crudos y costos)
y reporta dónde quedaron. Todo lo interpretativo (por qué falló una pregunta, a
quién atribuir, qué cambiar) es de la skill `kg-refinement`, no de esta.

**La ruta default para corridas nuevas es `runners/run_posthoc.py`**, NUNCA `harness.py`
suelto ni `run_frozen.py`: run_posthoc corre agente+juez juntos, pasa por la caché
persistente (no re-paga lo ya corrido) y captura los crudos íntegros por turno
(`data/experiment/evaluacion/runners/run_posthoc.py:1-43`).

## El sistema que se ejecuta (fijo, no se toca)

- **Agente respondedor:** `claude-haiku-4-5-20251001`, temperature 0, máx. 15 tool
  calls, 3 tools de grafo (`data/experiment/evaluacion/harness.py:47-50`).
  Contrato de respuesta: JSON `{respuesta, citas, respondible}`
  (`data/experiment/evaluacion/harness.py:85-92`).
- **Juez:** `claude-sonnet-4-6`, temperature 0, arquitectura de dos pasos v2.1.1;
  correctitud y completitud se computan determinísticamente en Python, no las
  decide el LLM (`data/experiment/evaluacion/judge.py:87-88` y `:204-267`).
  **Su prompt no se ajusta sin decisión de la autora**
  (`data/experiment/evaluacion/judge.py:73`).

## Prerrequisitos

- Venv de la raíz del repo (`.venv/bin/python`, Python 3.10).
- `ANTHROPIC_API_KEY` en `data/experiment/evaluacion/.env` (los modos con API
  abortan si falta, `data/experiment/evaluacion/runners/run_posthoc.py:283-285`).
- Directorio de trabajo: `data/experiment/evaluacion/`.

## Insumos

**Grafo** — claves válidas: `run_1`…`run_5` o `all`
(`data/experiment/evaluacion/loader.py:57-64`). Una clave nueva (p. ej. la copia
de refinamiento) primero tiene que estar cableada — ver
`.claude/skills/kg-refinement/references/preparar-run3-refinamiento.md`.

**Queries** — archivo JSON: lista `[{...}]` o dict `{"preguntas": [...]}`
(ambos aceptados, `data/experiment/evaluacion/runners/run_posthoc.py:272-274`).
Sets existentes en `data/experiment/evaluacion/queries/`: **eval sets para
conclusiones** — `eval_set_v1.json` (23 preguntas, congelado de la Fase 2.3) y
`eval_set_v2.json` (31) — y **material de desarrollo** — `dev.json`,
`dev_pool.json`, `candidatas.json`, `eval_set_v2_nuevas.json`. Regla: smoke tests
con material de desarrollo; conclusiones SOLO con eval sets (clasificación
completa en `references/contratos.md`).
Campos que el juez consume por pregunta: `id`, `pregunta`, `categoria`,
`respuesta_esperada`, `cita_textual`, `ground_truth_secciones`
(`data/experiment/evaluacion/judge.py:270-297`). Detalle del schema y de las
categorías en `references/contratos.md`.

## La corrida (secuencia sana)

```bash
cd data/experiment/evaluacion

# 0. Validar el archivo de queries (offline): toda pregunta NO-unanswerable debe
#    tener el referente completo para que el veredicto sea interpretable.
#    Las unanswerable (p. ej. CQ-036..039) no tienen referente POR DISEÑO: se excluyen.
python3 -c "
import json,sys
d=json.load(open(sys.argv[1])); qs=d['preguntas'] if isinstance(d,dict) else d
req=('respuesta_esperada','cita_textual','ground_truth_secciones')
inc=[q.get('id','?') for q in qs
     if q.get('categoria')!='unanswerable' and not all(q.get(k) for k in req)]
print(f'{len(qs)} preguntas | sin referente (no-unanswerable): {len(inc)} {inc or \"\"}')" \
  queries/eval_set_v2.json
# Esperado en eval_set_v1/v2: 0 incompletas. Si da >0, frenar y reportar — no correr.

# 1. Offline, gratis — cableado y replay determinista (14 checks):
python runners/run_posthoc.py --selftest

# 2. Con API, ~centavos — 1 pregunta, criterios PASS/FAIL automáticos:
python runners/run_posthoc.py --preflight --run run_3 --label <etiqueta>

# 3. Corrida completa:
python runners/run_posthoc.py --run run_3 --queries queries/eval_set_v2.json \
                      --reps 1 --label <etiqueta>
```

Flags (`data/experiment/evaluacion/runners/run_posthoc.py:515-527`): `--run`, `--reps`
(default 3), `--thinking` (default OFF), `--queries` (default `eval_set_v1.json`),
`--label`, `--db`.

**Reglas al lanzar:**

- **`--label` SIEMPRE explícito y nuevo.** El label nombra la carpeta de salida
  `posthoc_run/traces/{label}/{run}/` (`data/experiment/evaluacion/runners/run_posthoc.py:229`);
  repetir un label sobreescribe los `{qid}.json` de esa carpeta. Los labels `off`
  y `on` están OCUPADOS: contienen el dataset cualitativo de 230 trazas de la
  Fase 2.3+ — no reutilizarlos. (Sin `--label`, el default es justamente `off`/`on`
  según `--thinking`, `data/experiment/evaluacion/runners/run_posthoc.py:532` — otra razón
  para pasarlo siempre.)
- **`--reps 1` con caché caliente.** Con temperature 0 y caché, repeticiones del
  mismo request devuelven el MISMO objeto cacheado: N=3 colapsa en copias
  (hallazgo documentado de la re-corrida post-hoc). Reps > 1 solo aporta variación
  real si los requests no están cacheados; N=3 sin caché para conclusiones ante
  mentores es una decisión de la autora, no un default de esta skill.
- **`--thinking` cambia el namespace de caché** (`think=0/1` nunca se cruzan) y
  los requests dejan de ser byte-idénticos al frozen. Para comparabilidad con lo
  existente, OFF; para exploración del razonamiento, ON (patrón completo en la
  skill `llm-capture`).
- Trazas fallidas (parse error, truncado por max_tokens, error de API) **no se
  reintentan** — son comportamiento del sistema bajo evaluación; quedan con
  `failed_trace: true` y sin juez (`data/experiment/evaluacion/runners/run_posthoc.py:193-199`).

## Outputs y cómo leerlos

- **Por pregunta:** `posthoc_run/traces/{label}/{run}/{qid}.json` — lista de reps,
  cada una con la traza del agente, los crudos por turno, el juez completo
  (step1 + step2 + verdict) y los costos
  (`data/experiment/evaluacion/runners/run_posthoc.py:201-217`).
- **Por corrida:** `posthoc_run/summary_{label}_{run}.json` — n_preguntas,
  n_failed, costo_usd, stats de caché, code_version y graph_fingerprint
  (`data/experiment/evaluacion/runners/run_posthoc.py:250-264`).

Las dimensiones del veredicto, el mapping determinístico y el flag
`requiere_adjudicacion_humana` están en `references/contratos.md`.

## Reporte al usuario (verificable)

Al terminar, reportar SIEMPRE parseando el summary y las trazas reales — nunca
estimaciones (regla del proyecto): rutas exactas, n_preguntas, n_failed,
costo_usd, hit_rate de caché, y el conteo de veredictos por dimensión si se pide.
Toda traza con `requiere_adjudicacion_humana: true` se lista explícitamente — la
adjudicación contra los PDFs es de la autora.

## Non-goals

- **NO re-corre la evaluación congelada.** `run_frozen.py --mode graph` exige
  orden explícita de la autora (`data/experiment/evaluacion/run_frozen.py:29-30`)
  y re-correrla generaría datos nuevos, no reproduciría los existentes.
- **NO interpreta ni atribuye fallas** — eso es el Paso 3 de `kg-refinement`.
- **NO ajusta el juez ni el harness** (congelados; el juez además lo prohíbe en
  su docstring). Overrides de parámetros solo vía la cadena de `llm-capture`.
- **NO genera ni edita datasets de queries** — los eval sets se generan a ciegas
  en un proceso aparte (regla dura del Paso 1 de `kg-refinement`).
- **NO decide N para conclusiones** ante mentores (dueña: la autora).
- **NO commits** — los maneja la autora.

## Self-check (ejecutable)

```bash
cd data/experiment/evaluacion
python runners/run_posthoc.py --selftest   # offline, 14 checks, exit 0 si PASS
```

Tras una corrida real: verificar que `posthoc_run/summary_{label}_{run}.json`
existe, que `n_reps_total == n_preguntas × reps`, y que la carpeta
`posthoc_run/traces/{label}/{run}/` tiene un `{qid}.json` por pregunta del set.
