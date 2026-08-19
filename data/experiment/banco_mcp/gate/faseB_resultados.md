# FASE B — Resultados (corridas reales con `claude -p`)

Autorizada por `docs/laudo_gate_trazabilidad.md` §3. Todo lo que sigue se corrió **después** de
escribir `faseB_predeclaracion.md`, que fijó modelo, tope de tool calls, precios y reglas de freno.

## 0. Resumen en una línea

**La maquinaria sobrevive a las sesiones reales: 9/9.** Replay estándar, replay fuerte y
determinismo en verde en las nueve sesiones; el adaptador no rechazó ni perdió un solo step.
Ocho de nueve clases coincidieron con la predicción; la novena difiere por **navegación del
agente**, no por falla de maquinaria, y estaba declarada como predicción frágil antes de correr.

## 1. Lo que se declaró antes y lo que efectivamente pasó

| declarado antes de correr | qué pasó |
|---|---|
| modelo `claude-sonnet-5` | se honró en todos los turnos del agente. **Pero la sesión no es de un solo modelo**: el harness usa además `claude-haiku-4-5-20251001` para trabajo interno (507–1.027 tokens de entrada por sesión). Ver §5, hallazgo B1 |
| tope de 8 tool calls por sesión | **nunca se alcanzó**: el máximo fue 7 (GATE-01). `hit_tool_limit` no disparó en ninguna traza |
| tope por sesión `--max-budget-usd 0.15` | **disparó una vez**, en GATE-03 (`is_error: true`, `subtype: error_max_budget_usd`). El corte es duro y se reporta: la traza quedó completa (6 steps) y atribuible; **no se re-corrió** |
| freno por proyección si la proyección supera USD 1,20 | proyección tras la sesión descartable: **USD ~1,04** → no disparó |
| freno acumulado en USD 1,50 | gasto real **USD 1,2983** → no disparó |
| GATE-10 una sola vez | corrió una sola vez |
| GATE-07 best effort | **borde NO obtenido** (ver §3) |
| GATE-11 condicional | **no corrido** (ver §3) |

## 2. Demostración por clase — misma tabla que la fase A

Salidas: `corrida_faseB/demostracion_faseB.{json,md}`. Comando que la reproduce sin API:

```
python3 -B data/experiment/banco_mcp/gate/code/adaptador_cc.py adaptar \
  --rebanada data/experiment/banco_mcp/gate/sesiones_faseB/rebanada_cruda.jsonl \
  --out data/experiment/banco_mcp/gate/corrida_faseB/trazas \
  --casos data/experiment/banco_mcp/gate/casos_gate_faseB.json
python3 -B data/experiment/banco_mcp/gate/code/demostracion_gate.py \
  --out data/experiment/banco_mcp/gate/corrida_faseB \
  --casos data/experiment/banco_mcp/gate/casos_gate_faseB.json \
  --trazas data/experiment/banco_mcp/gate/corrida_faseB/trazas \
  --rebanada data/experiment/banco_mcp/gate/sesiones_faseB/rebanada_cruda.jsonl \
  --nombre demostracion_faseB
```

| caso | ancla | clase esperada | clase obtenida | replay | replay fuerte | determinismo | maquinaria | clase |
|---|---|---|---|---|---|---|---|---|
| GATE-01 | ext:9.9 | ausencia_kg | ausencia_kg | ok | ok | ok | **PASS** | coincide |
| GATE-02 | ext:3.3 | ausencia_kg | ausencia_kg | ok | ok | ok | **PASS** | coincide |
| GATE-03 | ext:7.4 | alcanzabilidad | **generacion** | ok | ok | ok | **PASS** | **difiere** |
| GATE-04 | ext:8.2 | vista_no_consultada | vista_no_consultada | ok | ok | ok | **PASS** | coincide |
| GATE-05 | ext:6.11 | generacion | generacion | ok | ok | ok | **PASS** | coincide |
| GATE-06 | ext:6.11 | generacion | generacion | ok | ok | ok | **PASS** | coincide |
| GATE-07 | ext:6.11 | alcanzabilidad | alcanzabilidad | ok | ok | ok | **PASS** | coincide (borde no obtenido, §3) |
| GATE-08 | ext:6.11 | alcanzabilidad | alcanzabilidad | ok | ok | ok | **PASS** | coincide |
| GATE-10 | ext:10.1 | generacion | generacion | ok | ok | ok | **PASS** | coincide |

Dos lecturas, declaradas por separado antes de correr:

- **Maquinaria (el criterio de la fase B): 9/9.** Replay estándar + replay fuerte + determinismo
  de la atribución + re-adaptación byte-idéntica desde la rebanada cruda. Esto es lo que el gate
  mide, y no falló en ningún caso.
- **Clase: 8/9 coincidieron con la predicción.** El script marca `FAIL` en GATE-03 porque su
  criterio es el de la fase A (coincidencia de clase); por el criterio declarado de la fase B ese
  caso es PASS. La discrepancia se deja visible en vez de retocar el script.

**Por qué GATE-03 difiere.** La predicción era `alcanzabilidad`: la pregunta usa vocabulario
disjunto del label del ancla, así que el ancla no debía aparecer en ninguna búsqueda. El agente
real navegó así:

```
buscar_nodos("operacion epsilon") → ver_nodo(Operacion_puente_epsilon) → ver_vecinos(idem)
→ ver_nodo(Obligacion_ancla_alfa) → ver_vecinos(Obligacion_ancla_alfa) → ver_nodo(Restriccion_ancla_beta)
```

El ancla nunca fue **vista** (`vista: false`, no apareció en ningún `buscar_nodos`) pero sí
**consultada** en el step 5 vía `ver_vecinos`, así que la precedencia sellada (consultada antes
que vista, regla §4) da `generacion`. **Es la clase correcta para lo que el agente hizo.** La
predicción era frágil y estaba declarada como tal en `casos_gate_faseB.json`. Lo que este caso
demuestra de paso es el valor del caso (V,F,V) con un agente real: sin la precedencia, esta traza
se habría clasificado como `alcanzabilidad` y habría dicho que el agente nunca tuvo el contenido,
cuando lo tuvo.

**Lo que la fase B agrega sobre la fase A.** En la fase A la navegación estaba puesta en escena.
Acá `vista_no_consultada` (GATE-04) la produjo un agente real sin que nadie se lo pidiera: buscó
`acreditacion complementaria`, el ancla salió primera, y abrió el señuelo léxico que salió
segundo. Es la brecha vista-sin-consultar del proyecto, reproducida en el banco nuevo.

## 3. Bordes: qué se obtuvo y qué no

| borde | estado | detalle |
|---|---|---|
| output por encima del cap del transporte (GATE-10) | **OBTENIDO** | el agente abrió el nodo grande; Claude Code derramó el output íntegro a disco y el adaptador lo siguió: **replay fuerte en verde sobre una sesión real**. Confirma en producción el hallazgo H1 de la fase A y la motivación de R1 |
| tools que devuelven vacío (GATE-08) | **OBTENIDO** | tres búsquedas seguidas sin resultados; el agente abandonó y marcó la respuesta como no respondible |
| sesión sin tool calls (GATE-07) | **NO OBTENIDO** | la pregunta era contestable sin consultar el grafo, pero el agente igual hizo **5 llamadas**. Se reporta como no obtenido; **la sesión no se editó**. El manejo de trazas de cero steps queda demostrado solo por la fase A |
| corte de sesión (GATE-09) | **NO CORRIDO** | el corte es una propiedad del archivo en disco, no del agente: no se puede producir con una corrida real sin escenificarlo. La demostración de la fase A se mantiene |
| contrato v2 (GATE-11) | **NO CORRIDO** | el laudo resolvió R2 por la opción B (el banco expone la firma v1). El hallazgo de la fase A ya está sellado y correrlo no decide nada; se omitió para no gastar presupuesto en confirmar lo laudado |

## 4. P0 — el número que el laudo pedía

Medido con dos sesiones descartables idénticas salvo la configuración, con `--tools Bash` (la
misma configuración de tools de las corridas reales). `P0` = tokens de entrada de la primera
llamada, que en la fórmula del entregable 7 es `P0 + Q_s`.

| configuración | P0 (tokens) | costo de la primera llamada (CLI) |
|---|---|---|
| `--safe-mode` (harness desnudo: sin CLAUDE.md, sin skills, sin plugins, sin MCP) | **9.412** | USD 0,0949 |
| por defecto, en cwd limpio fuera del repo | **19.074** | USD 0,1916 |
| **diferencia = costo de la configuración local** | **9.662** | USD 0,0967 |

**La configuración local del usuario duplica el prompt de sistema del harness.** Para A2.0-banco
esto es una decisión de diseño, no un detalle: el banco tiene que declarar en qué configuración
corre, porque `P0` aparece una vez por turno y multiplica todo lo demás. Las corridas de esta
fase usaron `--safe-mode`.

Con `P0 = 9.412` la fórmula del entregable 7 queda cerrada. Medición contra la corrida real: las
nueve sesiones sumaron 470.639 tokens de lectura de caché y 38.686 de escritura — es decir, el
prefijo se escribió una vez por sesión y se leyó ~12 veces, exactamente el comportamiento que la
fórmula asumía.

## 5. Hallazgos nuevos de la fase B

**B1 — Una sesión de Claude Code no es de un solo modelo.** Además del `claude-sonnet-5`
declarado, cada sesión usó `claude-haiku-4-5-20251001` para trabajo interno del harness. El
modelo declarado se honró para los turnos del agente, pero **la metadata por traza que pide
A2.0-banco (punto v de su diseño: «model id exacto devuelto por la API») no puede ser un solo
string**: tiene que ser el inventario de modelos de la sesión con su uso, o el número no
describe lo que se corrió.

**B2 — La contabilidad del CLI no coincide con los precios oficiales.** Recomputando el gasto
desde los conteos de tokens de la misma salida, por los precios verificados el día de la corrida:

| lectura | total |
|---|---|
| `total_cost_usd` que reporta `claude -p` (la fuente declarada) | **USD 1,2983** |
| recómputo desde `modelUsage` × precios oficiales | **USD 0,4191** |
| razón | **3,1×** |

La parte de Haiku coincide al centavo con los precios oficiales; la de Sonnet 5 está
sobre-facturada ~3×. Presenté el número del CLI como gasto de la unidad porque es el que declaré
como fuente y porque es **el conservador** (si me equivoco, me equivoco gastando de menos). Para
A2.0-banco el requisito que se deriva es concreto: **la contabilidad del banco se computa desde
los conteos de tokens, no desde el costo que reporta el harness**, y el precio se sella con la
corrida. El comando que reproduce las dos lecturas:

```
python3 -B data/experiment/banco_mcp/gate/code/contabilidad_faseB.py \
  --runs <dir de runs> --out data/experiment/banco_mcp/gate/corrida_faseB/contabilidad_faseB.json
```

**B3 — El aislamiento por capacidad funciona y el adaptador quedó sin trabajo sucio.**
Con `--tools Bash --allowedTools "Bash(python3 *)"`: 35 tool calls en 9 sesiones,
**0 rechazos** del adaptador y **0 `permission_denials`**. En la fase A, donde el agente tenía
todas las tools, el adaptador tuvo que rechazar 3 comandos. Es la confirmación empírica de R6:
con aislamiento, el adaptador no filtra nada y no hay superficie donde perder un step.

**B4 — El agente real respetó el contrato de salida (R4).** Las nueve sesiones terminaron con el
bloque JSON pedido (`respuesta` / `citas` / `respondible`). El hueco `final_json` de la fase A se
cierra fijándolo en el prompt, como el laudo aceptó.

**B5 — El slug de proyecto también reemplaza `_` por `-`.** El directorio de sesiones de un cwd
`…/faseB_cwd` es `…-faseB-cwd`. La regla completa es `pwd | tr '/ _' '---'`, no solo `/` y
espacio. Corregido en `inventario_campos.md`.

## 6. Gasto real

**USD 1,2983** según la fuente de contabilidad declarada (`total_cost_usd` de `claude -p`,
sumado sobre 12 sesiones: 9 casos + 2 descartables de P0 + 1 sesión de calibración de GATE-05).
Tope autorizado USD 2,00; freno declarado USD 1,50. Ninguno se alcanzó.

Desvío declarado: GATE-05 se corrió **dos veces** (USD 0,0839 de más). La primera fue la sesión
de calibración con la que medí el reuso de caché para poder proyectar; el runner que corrió
después no la vio porque miraba otro directorio. Se reporta como gasto de la unidad y las dos
salidas quedan en el paquete; la traza adaptada es la de la corrida del runner.

## 7. Nota de confidencialidad sobre los artefactos crudos

En todo campo **generado por el código de esta unidad** las rutas absolutas van enmascaradas.
No se enmascaran: `sesiones_faseB/rebanada_cruda.jsonl` (líneas verbatim de las sesiones),
`corrida_faseB/salidas_claude/run_*.json` (salida literal de `claude -p`, que es la fuente de
contabilidad) ni `corrida_faseB/salidas_claude/prompt_*.txt` (el prompt literal que recibió el
agente). Editarlos los invalidaría como evidencia: el gasto dejaría de ser verificable y el
prompt dejaría de ser el que se corrió. Contienen rutas de la máquina y ningún dato de terceros.
