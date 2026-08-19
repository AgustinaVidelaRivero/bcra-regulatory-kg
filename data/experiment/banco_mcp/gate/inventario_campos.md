# Entregable 1 — Inventario de campos: qué necesita la atribución causal y de dónde sale

Unidad **U-A2.0-gate** (plan v3, carril A). Costo USD 0.
Regla vinculante: `data/experiment/ev2_reporte/regla_atribucion.md` (commit `40603a9`).
Implementación vinculante: `data/experiment/ev2_reporte/code/atribucion_fallas.py` (`85d9fdb`),
que se **importa** — no se edita ni se reimplementa.

Este documento es el **contrato que el adaptador debe satisfacer**: si un campo de la
columna «necesita» no se puede reconstruir desde una sesión de Claude Code, la clase que
depende de él no se puede atribuir, y eso es exactamente lo que el gate tiene que decidir.

---

## 1. La superficie exacta que consume la atribución

Punto de entrada único: `atribucion_fallas.atribuir_payload(payload, anclas, ancla_index,
index, veredicto, replay_fuerte=True)`. Todo lo que la atribución lee sale de cinco lugares:

| # | argumento | qué es | ¿viene de la sesión del agente? |
|---|---|---|---|
| 1 | `payload` | la traza persistida (formato `runner_ev2`) | **SÍ — es lo único que el adaptador produce** |
| 2 | `anclas` | `gold.ancla` de la pregunta (`to:punto`) | NO — set sellado |
| 3 | `ancla_index` | `resolucion.AnclaIndex` sobre el kg.json crudo | NO — grafo |
| 4 | `index` | `harness.GraphIndex` sobre la vista runtime del grafo | NO — grafo |
| 5 | `veredicto` | `parcial` / `incorrecto` / `correcto` de ESA respuesta | NO — juez / adjudicación |

**Consecuencia dura**: el gate solo puede fallar por el argumento 1. Los otros cuatro son
invariantes del instrumento y no dependen del harness que corra al agente.

La forma del `payload` (verificada contra `data/experiment/ev2_corrida/trazas/ev2_base_v3/EV2F-001.json`):

```
payload = {
  "meta":  {...},                                   # no lo lee atribuir_payload
  "trace": {"steps": [{n, tool, input, output_truncado, output_chars}, ...],
            "final_json": {"respuesta", "citas", "respondible"},
            "tool_calls_used": int, "hit_tool_limit": bool, ...},
  "steps_full": [{n, tool, input, output, output_chars}, ...],
}
```

## 2. Tabla campo por campo

Leyenda de «uso»: **D** = alimenta una DECISIÓN de clase; **V** = alimenta una VERIFICACIÓN
(replay); **M** = metadato que la salida reporta pero no decide nada.

| campo del payload | uso | qué decide | de dónde sale HOY (traza del repo) | de dónde sale en una sesión de Claude Code |
|---|---|---|---|---|
| `trace.steps[*].tool` | **D** | discrimina `buscar_nodos` (vista) de `ver_nodo`/`ver_vecinos` (consultada) | `harness.py:513` lo escribe por cada `tool_use` | `message.content[*].name` de la línea `type=assistant`. Bash: el nombre es `"Bash"` y la tool real hay que **parsearla del comando**. MCP: el nombre es `mcp__<server>__<tool>`, mapeo directo |
| `trace.steps[*].input` | **D** | argumentos con que se re-ejecuta el step: `{consulta,limite}`, `{id}`, `{id,direccion}` | ídem | `message.content[*].input` (dict). Bash: dentro de `input.command` como string → **hay que parsearlo**. MCP: es el dict estructurado, verbatim |
| `trace.steps[*].n` | **D** | orden del step; fija `vista_en_step` / `consultada_en_step` y por lo tanto la precedencia temporal reportada | contador `tool_calls_used` del harness | orden de aparición de los `tool_use` en el jsonl (cadena `parentUuid`/`uuid` + `timestamp`); **hay que renumerar 1..N filtrando las tools ajenas al grafo** |
| `trace.steps[*].output_truncado` | **V** | replay estándar (`metrica._check_replay`): prefijo de 1.200 chars | `harness._truncate(result_str)` | **NO existe con esa semántica.** Bash: `toolUseResult.stdout` (capeado a 30.000 chars, ver §3). MCP: `toolUseResult[*].text`. El adaptador debe **re-truncar a 1.200 con el formato del harness** |
| `trace.steps[*].output_chars` | **V** | replay estándar: longitud exacta del output completo | `len(result_str)` del output ÍNTEGRO | derivable **solo si el output llegó completo al jsonl**; si el transporte truncó, este número es irrecuperable desde la sesión |
| `steps_full[*].output` | **V** | replay FUERTE (`metrica_ev2.verificar_steps_full`): igualdad exacta del objeto | el runner captura el resultado antes de serializar | Bash: `json.loads(toolUseResult.stdout)` si no fue truncado. MCP: `json.loads(toolUseResult[*].text)` |
| `steps_full[*].n`, `.tool`, `.input` | **V** | espejo de `steps` | ídem | ídem que `steps` |
| `trace.final_json.respondible` | **M** | flag reportado como metadato (regla §5) | el agente lo escribe en su JSON final | último mensaje de texto del asistente, **solo si el prompt exige JSON estructurado** |
| `trace.tool_calls_used` | **M** | reportado | contador del harness | número de steps adaptados |
| `trace.hit_tool_limit` | **M** | reportado | `MAX_TOOL_CALLS` del harness | **no existe** en Claude Code: el corte lo pone otro mecanismo (límite de turnos / fin de sesión). Requiere convención propia |
| `trace.question`, `meta.*` | — | no los lee `atribuir_payload` | — | trazabilidad, no atribución |

## 3. Qué campo alimenta cada clase (la lectura que pide el mandato)

Precedencia sellada: `presente → consultada → vista` (regla §4).

| clase | condición | campos que la deciden | ¿depende de la sesión? |
|---|---|---|---|
| `ausencia_kg` | `ancla_presente == false` | **ninguno del payload**: sale de `AnclaIndex.resolver(to, punto)` sobre el kg.json | **NO.** Es inmune al harness: se decide con el gold y el grafo, aunque la sesión esté vacía |
| `generacion` | presente ∧ consultada | `steps[*].tool ∈ {ver_nodo, ver_vecinos}` + `steps[*].input.id` (+ `input.direccion` para vecinos) | SÍ |
| `vista_no_consultada` | presente ∧ ¬consultada ∧ vista | `steps[*].tool == buscar_nodos` + `input.consulta` + `input.limite` | SÍ |
| `alcanzabilidad` | presente ∧ ¬vista ∧ ¬consultada | **la ausencia de los anteriores en toda la traza** | SÍ, y es la más frágil: se afirma por NEGACIÓN. Un step perdido por el adaptador convierte falsamente cualquier clase en `alcanzabilidad` |

**Asimetría de riesgo declarada**: `ausencia_kg` no puede romperse por el transporte;
`generacion` y `vista_no_consultada` requieren recuperar tool+input correctamente;
`alcanzabilidad` es la única que un adaptador incompleto produce **por defecto**, en silencio.
De ahí que el gate exija cobertura de steps demostrable, no asumida: cualquier step que el
adaptador no entienda tiene que ser un **error ruidoso**, nunca un descarte.

## 4. Los outputs NO deciden la clase — decisión de diseño heredada, con consecuencia

`metrica.evaluar_traza` **re-ejecuta** cada step contra el `GraphIndex` y clasifica contra el
output re-ejecutado; el output persistido se usa **solo** para verificar el replay
(`metrica.py`, docstring y `_check_replay`). Consecuencia para el gate:

- para **atribuir** basta `(tool, input, orden)` — tres campos, todos presentes en el jsonl;
- para **verificar** hace falta el output íntegro; si el transporte lo truncó, la atribución
  sigue siendo computable pero **deja de ser auditable**, que es justamente el diferencial de
  la tesis (atribución por replay determinístico, no por confianza en el log).

## 5. Límites del transporte medidos (no supuestos)

Medición sobre el corpus de sesiones de Claude Code del proyecto (solo lectura; el corpus
vive fuera del repo y no se copia — se persisten longitudes, no contenido).

Comando que reproduce todos los números de esta sección:

```
python3 -B data/experiment/banco_mcp/gate/code/medicion_transporte.py \
  --proyecto "$HOME/.claude/projects/$(pwd | tr '/ _' '---')" \
  --out data/experiment/banco_mcp/gate/corrida/medicion_transporte.json
```

Salida persistida: `corrida/medicion_transporte.json` (135 archivos de sesión).

Ampliación medida en el entregable 5 y no supuesta acá: cuando el output supera el cap, Claude
Code **derrama el output íntegro a disco** y lo declara en `toolUseResult.persistedOutputPath` /
`persistedOutputSize`. Ese archivo vive en el directorio de la sesión, fuera del repo.

| transporte | campo del jsonl | evidencia | límite |
|---|---|---|---|
| Bash | `toolUseResult.stdout` | 5.829 resultados de Bash; máximo observado **exactamente 30.000 chars** (3 casos en el máximo), ninguno por encima | **cap duro de 30.000 chars** |
| Bash | bloque `tool_result.content` | en los 3 casos de 30.000 chars el bloque que ve el modelo mide 2.291 / 2.290 / 2.221 chars | el modelo recibe un **preview**, no el output |
| MCP | `toolUseResult[*].text` | 38 resultados de tool MCP; máximo **24.063 chars**, sin marca de truncado | cap **no alcanzado** en la evidencia disponible; **no se puede declarar que no exista** |
| ambos | marca de truncado | `"… [N characters truncated] …"`, 10 apariciones, entre 793 y 20.009 chars comidos | trunca **por el medio**: el prefijo *y* el sufijo sobreviven, el medio no |

Nota de reproducibilidad: los conteos crecen mientras la sesión que corre esta unidad sigue
escribiendo en su propio jsonl. Los **máximos** (30.000 / 24.063) y la existencia del cap son
estables; los `n` son un corte temporal y por eso van con el comando que los recomputa.

Comparación con el harness congelado: `harness.TRUNC_TOOL_OUTPUT = 1200` trunca el **log**,
pero el runner persiste `steps_full` con el output ÍNTEGRO capturado **antes** de serializar
(`runner_ev2.py`). Es decir: hoy el replay fuerte no depende del log. En Claude Code **no
existe** un equivalente de `steps_full` fuera del transporte.

## 6. Diferencia de contrato v1 vs v2 (afecta directamente a A2.0-banco)

El driver de replay congelado `metrica._reejecutar_step` despacha exactamente tres firmas:

```
buscar_nodos(consulta, limite) | ver_nodo(id) | ver_vecinos(id, direccion)
```

Las tools v2 (`data/experiment/agente_v2/tools_v2.py`, el laudo C11 de A1.4 que A2.0-banco
va a enchufar) cambian la tercera: `ver_vecinos_v2(id, relacion, pagina, por_pagina)`, con
payload propio (`salientes_total`, `salientes_paginas`, `salientes_pagina_siguiente`,
`salientes_por_relacion`, `filtro_relacion`, `pagina`, `por_pagina`). El driver congelado
**ignora** `relacion`/`pagina`/`por_pagina` y pasa un `direccion` que v2 no tiene.

Consecuencia, verificada empíricamente en el entregable 5: la **semántica** de la atribución
sobrevive (v2 sigue exponiendo `salientes[*].vecino_id` / `entrantes[*].vecino_id`, que es lo
único que lee `metrica.evaluar_traza`), pero el **replay** no: re-ejecutar un step v2 con el
driver v1 devuelve otro objeto y el replay diverge. Esto no es un defecto del adaptador: es
un requisito para A2.0-banco (ver entregable 6).

## 7. Campos que la sesión NO trae y hay que fabricar por convención

| campo | por qué no está | convención propuesta por esta unidad |
|---|---|---|
| `n` | Claude Code no numera tool calls por dominio | renumeración 1..N sobre los steps **del grafo**, en orden de aparición, saltando toda tool ajena (Read, Edit, …), con el mapa `n → uuid` persistido para trazabilidad |
| `output_truncado` / `output_chars` | el harness los deriva del output íntegro | derivarlos del output recuperado; si el transporte truncó, marcar `output_truncado = null` y `replay_*_ok = false` explícito, **nunca** rellenar con el truncado |
| `hit_tool_limit` | no hay `MAX_TOOL_CALLS` | `false` salvo evidencia de corte; el corte de sesión se marca aparte (`corte_sesion: true`) |
| `final_json` | depende del prompt | exigir al prompt del banco el mismo JSON de salida del harness; si falta, `final_json = null` y `respondible_flag = null` |
| veredicto | no lo produce el agente | fuera de alcance del adaptador: lo pone el juez del repo |
