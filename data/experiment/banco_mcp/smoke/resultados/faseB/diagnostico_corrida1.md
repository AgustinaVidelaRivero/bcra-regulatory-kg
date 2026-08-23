# Diagnóstico de la corrida 1 de fase B (2026-08-23, 8 sesiones + 2 de P0 + 2 E2E)

Todo lo que sigue sale de los archivos persistidos en este directorio; nada se re-corrió.
Gasto erogado (R9, desde `modelUsage` × precios sellados): **USD 0,093** (CLI: 0,2137; razón 2,3×).
Queda declarado como gasto de la unidad.

## Tabla sesión por sesión

| sesión | `mcp_servers` en init | `tools` en init | turnos | tool calls | qué hizo el único turno | `completa` | motivo R3 |
|---|---|---|---|---|---|---|---|
| P0-kg | kg `pending` | [] | 1 | 0 | JSON del contrato (`respondible:false`), como se le pidió | true* | — |
| P0-vector | vector `pending` | [] | 1 | 0 | ídem | false | log R1 sin `fin` |
| SMK-01-kg | kg `pending` | [] | 1 | 0 | texto «Voy a buscar…» + pseudo-llamada `{"tool_call": "buscar_nodos", …}` | false | JSON final sin las claves del contrato |
| SMK-01-vector | vector `pending` | [] | 1 | 0 | **fabricó** una llamada `buscar_pasajes` y su *Response* con 5 resultados inventados (2.947 tokens de salida) | false | JSON final no parseable; log sin `fin` |
| SMK-02-kg | kg `pending` | [] | 1 | 0 | texto `buscar_nodos({...})` | false | sin claves del contrato |
| SMK-02-vector | vector `pending` | [] | 1 | 0 | pseudo-llamada `{"tool": "buscar_pasajes", …}` | false | sin claves; log sin `fin` |
| SMK-03-kg | kg `pending` | [] | 1 | 0 | pseudo-llamada `{"tool_call": "buscar_nodos", "parameters": …}` | false | sin claves del contrato |
| SMK-03-vector | vector `pending` | [] | 1 | 0 | JSON del contrato con `respondible:false` («las herramientas… no devolvieron pasajes») | false | log sin `fin` |
| SMK-04-kg | kg `pending` | [] | 1 | 0 | texto `buscar_nodos({...})` | false | sin claves del contrato |
| SMK-04-vector | vector `pending` | [] | 1 | 0 | pseudo-llamada `{"buscar_pasajes": {...}}` | false | sin claves; log sin `fin` |
| E2E-kg | kg `pending` | [] | 1 | 0 | declara que no puede leer archivos; JSON del contrato | true* | — |
| E2E-vector | vector `pending` | [] | 1 | 0 | declara que no puede conectarse a Neo4j ni leer archivos; JSON | false | log sin `fin` |

\* `completa=true` a pesar de `tools_en_init=[]`: la regla R3 implementada no exige que el inventario
R6 coincida con el esperado. Es un defecto de la regla (ver propuesta C3).

## 1. Init: servidores `pending`, tools ausentes — en las 12 sesiones

Fragmento (`stream_SMK-01-kg.jsonl`, línea 1):
```
"tools":[],"mcp_servers":[{"name":"kg","status":"pending"}],"model":"claude-sonnet-5","permissionMode":"dontAsk","apiKeySource":"ANTHROPIC_API_KEY"
```
Los servidores **sí arrancaron** y llegaron a servir: el log R1 tiene `inicio` en cada sesión
(p. ej. `log_r1_SMK-01-kg.jsonl`: `inicio` 19:00:02.246, `fin` 19:00:04.844, 0 llamadas). Es
decir, el handshake MCP terminó **después** de que el CLI tomó la foto del `system/init` y lanzó
el primer turno sin tools. Es el hallazgo de versión ya documentado (`config_agentes.json`,
`hallazgo_version`): Claude Code 2.1.196 no espera a los servidores `pending`; la doc sitúa la
espera en ≥ 2.1.221. La mitigación de fase A (carga perezosa del modelo en el servidor vectorial)
sirvió para el caso de 70 s, pero **no elimina la carrera**: con una sesión real el CLI arrancó
el turno antes del handshake incluso para el servidor del KG, que tarda ~1-2 s (Neo4j + sha del
kg.json). En los tests a USD 0 (`aislamiento/resultados/init/`, mismo comando salvo
`--no-session-persistence` y la URL cerrada) la foto dio `connected` 3/3 veces; la diferencia de
resultado entre ambos modos es consistente con una carrera que depende del orden de arranque, no
con una diferencia de configuración (el `argv` y el `env` declarados son idénticos salvo esos
dos ítems: `comando_SMK-01-kg.json` vs `aislamiento/resultados/init/comando_AISL-kg.json`).

## 2. Qué hizo el agente

Sin tools en contexto, el modelo **simuló** las llamadas como texto en 7 de 8 sesiones SMK (cuatro
formatos distintos de pseudo-llamada) y en SMK-01-vector además **fabricó la respuesta** de la
tool. Fragmento (`stream_SMK-01-vector.jsonl`, bloque `text` del asistente):
```
**buscar_pasajes**\n\n*Request*\n\n```json\n{\n  "consulta": "integración del capital mínimo riesgo de mercado", "limite": 5 }```\n\n*Response*\n\n```json\n{\n  "ok": true, … "cantidad": 5, "resultados": [ { "similitud": 0.6668, "to": "Capitales mínimos de las entidades financieras", …
```
(ese payload no existe: el servidor no recibió ninguna llamada — `log_r1_SMK-01-vector.jsonl`
tiene 0 líneas `llamada` — y la forma `ok/cantidad/similitud` no es la del servidor). SMK-03-vector
respondió el JSON del contrato con `respondible:false`. Ninguna sesión cortó por error:
`result.subtype=success`, `is_error=false`, `num_turns=1`, `permission_denials=[]`.

## 3. Por qué `completa=false`

Tres causas, todas derivadas de la 1:
- **R4**: en 7 sesiones el último mensaje no es el JSON del contrato (pseudo-llamadas o texto
  previo): «JSON final sin las tres claves del contrato» / «no parseable» (`meta_SMK-0*-*.json`,
  `completitud_R3.motivos_incompleta`).
- **R1/R3, brazo vectorial**: el log R1 del servidor vectorial no tiene línea `fin` en las 6
  sesiones (el del KG sí en las 6). El CLI termina el proceso del servidor al cerrar la sesión
  (doc stdio: cierre de stdin y luego terminación) y el servidor vectorial, con torch cargado,
  no alcanza a ejecutar su `finally: log.fin()` antes de ser terminado. Con 0 llamadas esto no
  perdió contenido, pero la regla de completitud lo cuenta como incompleto — correcto para R3,
  y a la vez señal de que el `fin` tiene que escribirse también ante SIGTERM.
- Los streams **no** quedaron truncos: todos terminan en `result`.

## 4. P0 y caché

P0 se midió con `--max-turns 1` y sin tools conectadas. `stream_P0-kg.jsonl` → `cache_creation
2162`, `cache_read 0`: es una primera llamada (escribe), no una lectura. En las sesiones SMK que
corrieron dentro de los 5 minutos siguientes, el uso muestra `cache_read 1283` + `cache_creation
~895`: el prefijo común del harness (1.283 tokens) **sí** se leyó de caché y lo propio de cada
sesión (prompt con pregunta + resto) se escribió. Conclusión: el prompt entra como cacheable.
Pero **P0 de `--bare` = 2.162 tokens está subestimado**: no incluye las definiciones de las tools
MCP (no estaban); se re-mide con servidores `connected`. Contraste con el gate: 9.412 en
`--safe-mode` (el harness desnudo de `--bare` es ~4× más chico, coherente con que no carga
CLAUDE.md/skills).

Defecto colateral del lanzador: `tokens_R9.por_llamada_api` lista dos eventos `assistant` por
mensaje (mismo `message.id`, uno con el bloque `thinking` y otro con el `text`) con el mismo
`usage` parcial (`input_tokens: 1`, `output_tokens: 2-3`): duplica y subreporta. El costo R9 NO
usa esa lista (usa `modelUsage` del `result`, que es correcto: Sonnet 2.947 tokens de salida en
SMK-01-vector), pero la lista por llamada hay que deduplicar por `message.id` y declarar que
`usage` en stream es parcial.

## Propuesta de corrección (NO implementada; se lauda antes de re-correr)

**C1 — Resolver la carrera del handshake (causa raíz).** Opciones, en orden de preferencia:
 a. **Actualizar Claude Code a ≥ 2.1.221** (doc `--mcp-config`: «When you pass this flag with
    `-p`, Claude Code waits for still-pending servers to connect before running the first turn, up
    to the `MCP_TIMEOUT` startup timeout»). Cambia la variable sellada `claude_code_version`
    (config + sha) → se declara, se re-validan a USD 0 los tests de aislamiento/init y el
    selftest, y recién después el smoke. Es la corrección documentada, no un parche.
 b. Si (a) no es viable: **gate de arranque del lado del banco** — el lanzador verifica en el
    `system/init` que `mcp_servers[*].status == "connected"` y `tools == esperadas` **antes** de
    que el modelo reciba el turno; como el CLI no lo permite en 2.1.196, el gate solo puede
    abortar la sesión (SIGINT tras el init, costo ≈ una llamada) y reintentar N veces. Es un
    parche: cuesta, no garantiza, y deja trazas abortadas que hay que declarar.
 c. Prompt: instrucción explícita «si no tenés ninguna tool disponible, no simules llamadas:
    respondé el JSON con `respondible:false` y motivo». No corrige la causa; evita que una
    sesión sin tools produzca pseudo-llamadas o respuestas fabricadas. Se propone **además** de
    (a), porque es una regla de honestidad del contrato R4, y es un cambio de prompt sellado
    (cambia el sha; idéntico en ambos brazos).

**C2 — `fin` del log R1 ante SIGTERM** (ambos servidores): manejador de señal que escribe la
línea `fin` antes de salir. No cambia payloads ni tools.

**C3 — Regla R3 más estricta**: `completa` exige además `inventario_tools_R6.coincide == true` y
`mcp_servers` todos `connected` en el init. Sin eso, E2E-kg y P0-kg no deberían contar como
completas.

**C4 — Lanzador**: deduplicar `por_llamada_api` por `message.id` y marcar `usage` de stream como
parcial; el costo R9 sigue saliendo de `modelUsage`.

**C5 — Repetir P0** con servidores `connected` (una sesión por brazo) y recién entonces
contrastar contra 9.412.

Gasto proyectado de la re-corrida completa: ≈ USD 0,10 (R9), dentro del tope 3 autorizado;
no arranca sin laudo de C1–C5.
