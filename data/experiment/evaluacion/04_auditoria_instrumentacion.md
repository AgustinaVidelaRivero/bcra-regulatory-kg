# Auditoría de instrumentación — corrida congelada (Fase 2.3)

**Alcance:** qué se persistió exactamente para las **345 trazas** de la corrida congelada (5 grafos × 23 preguntas × N=3), del lado del **agente** y del **juez (2 pasos)**, incluido thinking/chain-of-thought, y qué preservó la caché. Solo lectura: no se modificó ni re-corrió nada.

**Método:** verificación directa contra el código (`harness.py`, `judge.py`, `run_frozen.py`) y contra un archivo de traza persistido real (`frozen_run/traces/run_1/CQ-010.json`). Todas las afirmaciones de abajo provienen de inspección, no de memoria.

---

## 0. Hallazgo de entrada: NO hay thinking/CoT generado por ningún modelo

**Ni el agente ni el juez se ejecutan con thinking habilitado.** El parámetro `thinking` NO se pasa en ninguna llamada:

- Agente (`harness.py`): `client.messages.create(model, max_tokens, temperature, system, messages, tools[, tool_choice])` — sin `thinking`.
- Juez (`judge.py` `_call`): `client.messages.create(model, max_tokens, temperature, system, messages)` — sin `thinking`.

En Haiku 4.5 y Sonnet 4.6 el thinking es opt-in; sin el parámetro, las respuestas son solo bloques `text` + `tool_use`. **Conclusión: no existe contenido de thinking/chain-of-thought en ninguna de las 345 trazas — no se está perdiendo CoT porque no se genera.** (Habilitarlo requeriría un cambio de configuración; fuera del alcance de esta auditoría.)

---

## 1. Agente — qué se persistió (frozen)

El `QuestionTrace` del harness captura en memoria bastante (`api_calls`, `steps`, `final_raw`, `seen_provenances`), pero el pipeline congelado (`run_frozen.evaluate_cell`) arma el rep dict con un **subconjunto**. Claves persistidas por repetición (verificadas en el archivo real):

```
rep, qid, run, categoria, respondible, citas, respuesta, tool_calls_used,
hit_tool_limit, parse_ok, truncated_max_tokens, error, failed_trace, verdict,
harness_cost, judge_cost, judge_error
```

- **¿Contenido crudo completo del response?** **No.** Solo se guardan **campos derivados/parseados**: `respuesta`, `citas`, `respondible` (los tres son campos del JSON final ya parseado, vía `final_json`).
- **El texto crudo final** (`final_raw`, el string JSON exacto que emitió el modelo) existe en el `QuestionTrace` pero **NO se copia al rep congelado**.
- **Los bloques de contenido del response** (`response.content`: bloques `text` y `tool_use` de cada turno) **no se guardan**. Se anexan a `messages` en memoria y se descartan al terminar la repetición.
- **Texto/comentario intermedio** que el modelo emite entre tool calls (los bloques `text` previos a cada `tool_use`): **no se persiste**.
- **Steps de tool calls** (`tr.steps`: por cada tool call, `input` + output del tool **truncado a 1200 chars**): existen en el `QuestionTrace` pero **NO en el rep congelado**.
- **Thinking del agente:** no existe (sección 0).

> Nota: las trazas del **loop manual** (`trazas/manual_run_*.json`) sí incluyen `steps`, `api_calls`, `final_raw` y `seen_provenances` — pero son del dev_pool, **no de las 345 trazas del eval_set congelado**.

---

## 2. Juez (2 pasos) — qué se persistió (frozen)

Cada repetición no fallida invoca `judge.judge_trace`, que internamente hace **2 llamadas** (Paso 1 descomposición ciega + Paso 2 verificación). `evaluate_cell` guarda **solo `jr["verdict"]`** (el veredicto computado), **no** `jr["step1"]` ni `jr["step2"]`. Claves reales del `verdict` persistido:

```
correctitud, completitud, cita_documento_correcto, cita_precision, abstencion,
especulacion_en_prosa, afirmaciones_no_soportadas {centrales, secundarias,
n_centrales, n_secundarias}, requiere_adjudicacion_humana,
justificacion {correctitud, completitud, citas}   (+ abstencion en unanswerable)
```

- **¿Output crudo completo de cada llamada del juez?** **No.** En `_call`, `raw = None if parsed else text`: el texto crudo se **descarta cuando el parseo tiene éxito** (que es el caso de todas las trazas válidas). Solo se conservaría el crudo si el JSON no parseaba.
- **¿Razonamiento por dimensión?** **Parcialmente, y derivado.** Se guarda `justificacion` con strings por dimensión. Pero `justificacion.correctitud` y `justificacion.completitud` las **construye `_compute` en Python** a partir de las verificaciones (no son free-text del LLM); `justificacion.citas` y `justificacion.abstencion` sí salen del LLM (campo del Paso 2).
- **Paso 1 (descomposición):** `afirmaciones_verificables`, `reportes_de_alcance`, `patas_de_la_pregunta` — **NO se guardan**.
- **Paso 2 (verificación):** la lista completa `verificaciones` (verdict verdadero/falso/no_soportado **por cada afirmación**) y `cobertura_patas` (cubierta/no_cubierta por pata) — **NO se guardan**. Solo sobrevive el **derivado**: `afirmaciones_no_soportadas` (las no_soportadas centrales/secundarias + conteos) y los strings de `justificacion`.
- **Thinking del juez:** no existe (sección 0).

---

## 3. Caché — qué preserva

El caching del agente (`cache_conversation=True`, `cache_control` en el último bloque de usuario) es **input-side**: cachea el procesamiento del **prefijo del prompt** (KV-cache), servido como `cache_read_input_tokens`. **NO cachea el output del modelo.**

- **Un cache hit NO devuelve contenido reducido.** El output (`response.content`) se **genera fresco en cada llamada**, idéntico en naturaleza a una llamada sin caché. La caché solo abarata el reprocesamiento del input; no toca lo generado.
- **No hay thinking en la caché**, por dos razones independientes: (a) los outputs no se cachean en absoluto, y (b) el thinking está deshabilitado.
- El **juez NO usa caching** (sus llamadas no llevan `cache_control`); igual, su output también se genera fresco.

**Conclusión:** la caché no preserva ni reduce nada del output. Es ortogonal a esta auditoría de persistencia — lo que se guarda o se pierde es lo mismo con o sin caché.

---

## 4. Inventario de lo que se pierde hoy (345 trazas congeladas)

`R` = recuperable de los datos actuales · `RR` = solo vía re-corrida (no determinista a temp 0) · `—` = no aplica.

### Agente
| Ítem | ¿Guardado? | Recuperabilidad |
|------|:----------:|-----------------|
| Respuesta final parseada (`respuesta`, `citas`, `respondible`) | **Sí** | — |
| Texto crudo final (`final_raw`, JSON string exacto) | No | **R parcial**: reconstruible re-serializando `final_json`; no byte-exacto |
| Bloques crudos del response (`content[]`) | No | **RR** |
| Texto/comentario intermedio entre tool calls | No | **RR** |
| Steps de tool calls (inputs + outputs truncados a 1200) | No | **RR** |
| `seen_provenances` (provenances que el agente vio) | No | **RR** (o reconstrucción parcial consultando el grafo) |
| Tokens por rep (in/out/cache_read/cache_write) | No (solo `harness_cost` en USD) | **No recuperable**: el costo es 1 ecuación con 4 incógnitas |
| `stop_reason` / `api_calls` por llamada | No | **RR** |
| Thinking / chain-of-thought del agente | — (deshabilitado) | — |

### Juez (2 pasos)
| Ítem | ¿Guardado? | Recuperabilidad |
|------|:----------:|-----------------|
| Veredicto estructurado (8 dimensiones + `requiere_adjudicacion_humana`) | **Sí** | — |
| `afirmaciones_no_soportadas` (centrales/secundarias + conteos) | **Sí** | — |
| `justificacion` por dimensión (correctitud, completitud, citas[, abstencion]) | **Sí** | — (correctitud/completitud son derivadas por código, no free-text del LLM) |
| Paso 1: descomposición (afirmaciones, reportes_de_alcance, patas) | No | **RR** |
| Paso 2: `verificaciones` (verdadero/falso/no_soportado por afirmación) | No (solo el subconjunto no_soportado) | **RR** para la lista completa; las no_soportadas sí están |
| Paso 2: `cobertura_patas` (cubierta/no_cubierta por pata) | No (solo las no_cubiertas en `justificacion.completitud`) | **RR** para la lista completa |
| Texto crudo de cada llamada del juez | No (descartado en parseo OK) | **RR** |
| Tokens del juez por llamada | No (solo `judge_cost` en USD) | **No recuperable** |
| Thinking / chain-of-thought del juez | — (deshabilitado) | — |

---

## 5. Síntesis

1. **Thinking/CoT:** no se está perdiendo porque **nunca se generó** — ambos modelos corren sin `thinking`.
2. **Agente:** se preserva la **respuesta final parseada** (respuesta + citas + respondible) y metadata; se descarta todo el **contenido crudo del response, los steps de tool calls, el texto intermedio y el detalle de tokens** (solo sobrevive el costo en USD).
3. **Juez:** se preserva el **veredicto estructurado + justificación por dimensión + afirmaciones no soportadas**; se descartan el **Paso 1 completo, las verificaciones por-afirmación y la cobertura por-pata completas, y el texto crudo** de ambas llamadas.
4. **Caché:** input-side; no cachea ni reduce outputs — irrelevante para lo que se preserva.
5. **No recuperable de los datos actuales** (ni siquiera re-derivable): el **desglose de tokens por repetición** (agente y juez). Todo lo demás marcado **RR** requeriría re-correr (no determinista a temperatura 0, por lo que no reproduce las trazas congeladas).
