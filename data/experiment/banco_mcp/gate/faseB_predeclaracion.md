# FASE B — PRE-DECLARACIÓN (escrita ANTES de correr nada)

Unidad **U-A2.0-gate**, fase B. Autorizada por `docs/laudo_gate_trazabilidad.md` §3:
tope **USD 2**, precios verificados contra documentación oficial antes de correr, freno por
proyección.

Este documento se escribe **antes** de la primera llamada. Todo lo que fija queda fijado: si la
corrida real se desvía de acá, el desvío se reporta, no se ajusta la declaración.

## 1. Modelo exacto (string)

```
claude-sonnet-5
```

Se declara el string tal cual se pasa a `claude -p --model`. La corrida verifica el **model id
efectivamente devuelto** por la sesión (`message.model` en el jsonl y `modelUsage` en la salida
`--output-format json`) y lo persiste por traza; si difiere del declarado, es hallazgo y se
reporta — no se corrige el declarado a posteriori.

Por qué Sonnet 5 y no otro: es un modelo de sesión soportado por el harness (alias `sonnet`),
el más barato de los soportados con adaptive thinking, y el gate no mide calidad del agente
sino supervivencia del adaptador y del replay. Haiku 4.5 sería más barato ($1/$5) pero no está
declarado como modelo de sesión del harness; probarlo gastaría presupuesto en averiguar eso.

## 2. Tope de tool calls por sesión

```
MAX_TOOL_CALLS_GATE = 8
```

- Se declara **en el prompt** del agente y se registra por traza.
- Es el reemplazo del `hit_tool_limit` del harness congelado (requisito **R5** del laudo), y
  se reporta como métrica propia del banco: **no** se compara numéricamente con el tope de 15
  del harness.
- **El corte es duro y se declara.** Si el agente real navega más que la puesta en escena de la
  fase A, la traza se marca `hit_tool_limit: true` y el caso se reporta como es. **No se
  re-corre para "mejorar" el caso.**
- Justificación del número: las secuencias de la fase A usaron 1–3 steps; 8 deja margen para
  búsquedas fallidas sin que el costo (que crece con el cuadrado de las tool calls) se dispare.

## 3. Precios verificados (documentación oficial, consultada hoy)

Fuente: `https://platform.claude.com/docs/en/about-claude/pricing.md` y
`https://platform.claude.com/docs/en/about-claude/models/overview.md`.

| modelo | input | escritura de caché 5 min | lectura de caché | output |
|---|---|---|---|---|
| **claude-sonnet-5** | **$2 / MTok** | **$2,50 / MTok** | **$0,20 / MTok** | **$10 / MTok** |
| claude-haiku-4-5 (referencia) | $1 / MTok | $1,25 / MTok | $0,10 / MTok | $5 / MTok |
| claude-opus-5 (referencia) | $5 / MTok | $6,25 / MTok | $0,50 / MTok | $25 / MTok |

Nota verificada en la fuente: el precio $2/$10 de Sonnet 5, anunciado como introductorio hasta
2026-08-31, **pasó a ser el precio estándar**; el aumento a $3/$15 no va a ocurrir. Es decir:
no hay riesgo de que el precio cambie durante esta corrida.

Costo adicional de tools: el harness usa la tool `Bash`, que es cliente y **no** tiene cargo
por uso — solo tokens. No se habilita ninguna server tool (sin web search, sin code execution),
así que no hay cargos por búsqueda ni por hora de contenedor.

## 4. Tope y regla de freno

- **Tope duro de la unidad: USD 2** (laudo §3).
- **Tope por sesión, aplicado por el propio harness**: `--max-budget-usd 0.15`. Es un corte del
  lado del CLI, no una promesa: una sesión que se desmadre se corta sola.
- **Freno por proyección, en dos puntos:**
  1. tras la sesión descartable (paso 5), se proyecta el costo de las 11 sesiones. Si la
     proyección supera **USD 1,20** (60 % del tope), **FRENO** y reporto sin correr el resto.
  2. durante la corrida, gasto acumulado real. Si supera **USD 1,50** (75 % del tope),
     **FRENO** y reporto lo obtenido.
- La contabilidad es el campo `total_cost_usd` que devuelve `claude -p --output-format json`
  por sesión, sumado. Se persiste crudo por sesión.

## 5. Aislamiento y configuración de las sesiones

| decisión | valor | por qué |
|---|---|---|
| directorio de trabajo | un directorio limpio del scratchpad, **fuera del repo** | evita que el agente de juguete herede el `CLAUDE.md` del proyecto (contaminaría el prompt y el número de P0) |
| tools disponibles | `--tools Bash` | **aislamiento por capacidad** (requisito R6): el agente no tiene Read, Edit ni ninguna otra tool |
| permisos | `--allowedTools "Bash(python3 *)"` | solo puede invocar las tools de juguete |
| persistencia | por defecto (la sesión escribe su jsonl) | el jsonl es el insumo del adaptador |
| formato de salida | `--output-format json` | trae `session_id`, `usage` y `total_cost_usd`: es la fuente de contabilidad |

## 6. Medición de P0 (el número que el laudo pide)

Primer paso, sesión **descartable**, sin tools y sin tarea real, en dos configuraciones, para
separar el prompt de sistema del harness del contexto que agrega la configuración local:

- **(a) `--safe-mode`**: harness desnudo (sin `CLAUDE.md`, sin skills, sin plugins, sin MCP).
- **(b) por defecto en cwd limpio**: harness + configuración de usuario.

`P0` es el total de tokens de entrada de la primera llamada (`input_tokens +
cache_creation_input_tokens + cache_read_input_tokens`), que es lo que la fórmula del entregable
7 llama `P0 + Q_s`. La diferencia (b) − (a) es el costo de la configuración local, número que
A2.0-banco necesita para decidir en qué configuración corre el banco.

## 7. Qué se reporta igual que en la fase A

La demostración por clase se reporta con la **misma tabla**: una fila por caso con clase
esperada / obtenida / replay / replay fuerte / PASS-FAIL. **Si una clase que pasó en fase A
ahora falla, es hallazgo y FRENO** — no se ajusta el adaptador para que pase.

## 8. Recortes declarados

- **GATE-10** (output que excede el cap del transporte) corre **una sola vez**, no dos: su
  valor probatorio ya está obtenido offline en la fase A.
- **GATE-07** (sesión sin tool calls) es **best effort declarado**: si el modelo llama a una
  tool igual, se reporta como **no obtenido**. La sesión **no se edita**.
- **GATE-11** (contrato v2) se corre solo si la proyección de costo lo permite con holgura. El
  laudo ya resolvió R2 por la opción B (el banco expone la firma v1), así que su hallazgo está
  sellado offline y no es condición de nada; si entra, entra como confirmación.
