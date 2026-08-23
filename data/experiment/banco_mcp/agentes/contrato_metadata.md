# Contrato de metadata por traza — banco MCP (v1)

Unidad U-A2.0-banco, entregable 5. Implementado en `agentes/lanzar_agente.py::armar_meta`; un
`meta_<id>.json` por sesión. Toda clave es obligatoria (puede valer `null` si la sesión no llegó a
producirla, y entonces `completitud_R3.completa` es `false`).

| clave | requisito | contenido | de dónde sale |
|---|---|---|---|
| `contrato` | — | `"agentes/contrato_metadata.md v1"` | constante |
| `pregunta_id`, `brazo`, `modo` | — | id de la corrida; `kg`/`vector`; `real`/`init` | argumentos del lanzador |
| `sesion` | R1/R7 | `session_id` (fijado con `--session-id`), `copia_jsonl` (índice, no fuente de verdad), `cwd` aislado, `claude_code_version` | `claude --version`, `system/init` |
| `modelos_R8` | R8 | `declarado` (`--model`), `inventario_observado` (todos los modelos vistos: init + `modelUsage` + `message.model` de cada mensaje), `uso_por_modelo` | stream-json |
| `credenciales` | 6 | `via_declarada` (`api`/`bedrock`), `apiKeySource_en_init` | lanzador + `system/init` |
| `servidores_mcp` | R1 | estado en init, `servidor`, `version_servidor`, `config` íntegra + `config_sha256`, `fuente` (sha del kg.json o de la matriz, backend, n), `entorno_servidor` (versiones) | línea `inicio` del log R1 |
| `sha_fuentes` | 5 | `kg_sha256` / `sha256_matriz_vectorial` (el que corresponda al brazo) | log R1 |
| `harness_R10` | R10 | `modo` (`--bare`), `permission_mode`, `claude_code_version` (salida de `claude --version`), `claude_code_version_sellada` (de `config_agentes.json`) y `coincide_con_sellada` (si es `false`, la traza se declara como corrida con CLI no sellado y el smoke se re-valida), `flags_estructurales`, `tools_denegadas`, `tools_builtin`, `config_agentes_sha256`, `sha_identidad_pipeline` | config sellada + init |
| `inventario_tools_R6` | R6 | `tools_en_init`, `esperadas`, `coincide` | `system/init` |
| `corte_R5` | R5 | `max_turns`, `tope_tool_calls_prompt`, `max_budget_usd` (declarados) y `num_turns_observado`, `n_tool_calls_observado`, `corte_disparado` (subtype del result si no fue `success`) | config + result |
| `completitud_R3` | R3 | `completa` (bool) y `motivos_incompleta` | regla abajo |
| `mapa_R7` | R7 | por step: `n`, `tool_use_id`, `tool`, `input`, `call_id_log`, `coincide_tool_input` | tool_use de la sesión × orden del log R1 |
| `tokens_R9` | R9 | `por_llamada_api` (uso por mensaje del asistente: input/output/cache_creation/cache_read y modelo), `costo_recomputado` (Σ tokens × `precios_sellados.json`), `total_cost_usd_cli_solo_para_contraste`, `precios_sellados_sha256` | stream-json + precios sellados |
| `final_json_R4` | R4 | el JSON final parseado (`respuesta`, `citas`, `respondible`) | texto de `result.result` |
| `permission_denials` | R6 | lista del CLI | result |
| `log_r1` | R1 | `existe`, `ruta`, `sha256`, `n_llamadas` | archivo del log |

## Regla de completitud (R3)

`completa = true` si y solo si: hay evento `result` con `subtype == "success"` y `is_error == false`;
el último mensaje contiene un JSON con las tres claves del contrato de salida; el log R1 tiene la
línea `fin`; `n_llamadas` del log == cantidad de `tool_use` MCP de la sesión; y todo `tool_use` MCP
tiene su `tool_result`. Cualquier otra cosa ⇒ `completa = false` con los motivos enumerados; la
traza se excluye de la métrica y se declara, nunca se atribuye.

## Mapa R7

`n` es el orden de aparición del `tool_use` MCP en la sesión; `call_id_log` es la `n`-ésima llamada
del log R1 del servidor de esa sesión (un proceso por sesión). `coincide_tool_input` verifica que
tool e input coinciden; el adaptador (entregable 7) además verifica `output_sha256` del log contra
el texto del `tool_result` de la sesión cuando este no fue truncado por el transporte.

## Costo (R9)

`costo = Σ_modelo (inputTokens·p_in + cacheCreationInputTokens·p_cw5m + cacheReadInputTokens·p_cr + outputTokens·p_out)/1e6`
con `precios_sellados.json`. `total_cost_usd` del CLI se guarda solo para contraste (sobrefactura
~3× medida en b08095a).
