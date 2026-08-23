# Banco de evaluación: Claude Code + servidores MCP (U-A2.0-banco)

Unidad A2.0-banco del plan (`docs/plan_tesis.md` v5, carril A, bloque A2). El brazo de
evaluación es una **variable declarada**: qué servidor MCP se enchufa al mismo agente
(`claude -p`, mismo modelo, mismo prompt). Este directorio construye el banco; **no diseña ni
corre la evaluación** (eso es A2.1/A2.2) y no abre material EV2.

Laudos vinculantes que implementa: `docs/laudo_gate_trazabilidad.md` (R1–R7), fase B del gate
(`gate/faseB_resultados.md`, R8–R10) y `docs/decision_modelo_embeddings.md` §7–§8.
El subdirectorio `gate/` está sellado (`c09663a`, `b08095a`): se importa, no se edita.

Estado: **UNIDAD COMPLETA (fases A y B)**. Fase B: corrida 1 (2.1.196) anómala y conservada como
evidencia (`smoke/resultados/faseB/`, diagnóstico y nota C3 incluidos); tras el laudo C1–C5
(actualización del CLI a 2.1.241, re-sellado de versión y prompt, C2–C4) la corrida 2 cumplió el
criterio de aceptación completo (`smoke/resultados/faseB_corrida2/reporte_faseB_corrida2.md`).
Gasto total de fase B: USD 0,534 (R9) de tope 3.

## Estructura

| ruta | qué es | versionado |
|---|---|---|
| `comun_banco.py` | log R1 (`LogR1`), sha de config, `serializar_payload` (= `json.dumps(obj, ensure_ascii=False)`, harness.py:512) | sí |
| `cliente_falso.py` | cliente MCP stdio síncrono para tests y selftest (sin modelo, USD 0) | sí |
| `requirements_kg.txt` / `requirements_vector.txt` | versiones pinneadas de cada servidor | sí |
| `mcp_kg/` | servidor MCP del KG (firma v1), configs selladas, test de paridad, resultados | sí |
| `mcp_vector/` | servidor MCP vectorial, constructor del índice, tests, resultados | sí (salvo `indice/`) |
| `mcp_vector/indice/` | matriz float32 1763×1024 + pasajes + manifiesto | **no** (gitignore local; regenerable, sha declarado) |
| `logs/` | logs R1 de los servidores (uno por proceso) | **no** (gitignore local) |
| `agentes/` | config sellada de los agentes (R10), plantilla + bloques de prompt, lanzador `claude -p`, precios sellados (R9), credenciales (6), contrato de metadata (5), selftest | sí (`resultados/` incluidos: son USD 0) |
| `aislamiento/` | test de aislamiento por capacidad (R6) y resultados | sí |
| `adaptador/` | adaptador del banco (importa el del gate), demostración por clase sobre MCP, medición del tope | sí |
| `smoke/` | selftest integrador offline, estimación de fase B, preguntas propias y runner del smoke (con guarda de autorización) | sí (`cwd_*/` no) |

## Entornos

- **KG**: `.venv` del repo (Python 3.10) + `requirements_kg.txt` (`neo4j==6.2.0`, `mcp==1.29.0`).
- **Vectorial**: Python 3.12 con `requirements_vector.txt` — exactamente el entorno de referencia
  del bake-off (`bakeoff_embeddings/resultados/e3_entorno.json`: torch 2.13.0, transformers
  5.15.1, sentence-transformers 6.0.0, tokenizers 0.22.2, numpy 2.5.2) + `mcp==1.29.0`. La caché
  de Hugging Face vive fuera del repo (`~/.cache/huggingface`); revisión del modelo pinneada.
- Prerrequisito del KG: contenedor `neo4j-bcra-kg-compose` (`data/experiment/neo4j/docker-compose.yml`)
  con KG-Refinado cargado. El servidor verifica `KG_Meta.kg_sha256` == sha del `kg.json` sellado ==
  sha esperado en su config **antes** de exponer una tool; si difiere, aborta.

## 1. Servidor MCP del KG (`mcp_kg/`)

`servidor_mcp_kg.py` expone `buscar_nodos(consulta, limite)` / `ver_nodo(id)` /
`ver_vecinos(id, direccion)` con la **firma v1** (laudo R2, opción B). Nada se reimplementa:

- nombre, descripción e `input_schema` se **importan** de `harness.TOOLS` (harness.py:242–284);
- el despacho replica `GraphAgent._run_tool` (mismos `args.get` y defaults);
- backend por config sellada: `neo4j` (`Neo4jIndex`, A1.1, modo `fulltext` = BM25/Lucene, base
  C10) para el head-to-head; `memoria` (`harness.GraphIndex` vía `tools_juguete.cargar_index`)
  para repetir la demostración por clase del gate sobre el mismo servidor y transporte;
- respuesta: UN bloque de texto = `json.dumps(result, ensure_ascii=False)`. Sin
  `structuredContent` ni campos extra (cambiarían `output_chars` y romperían el replay);
- `validate_input=False`: el harness no validaba (p. ej. `limite="7"` cae a 10).

Fuera del banco (R2): paginación, filtro por relación, `contexto_de`.

### Tabla harness v1 ↔ MCP, por tool

| tool | firma | descripción / schema | payload | backend de búsqueda | qué cambia |
|---|---|---|---|---|---|
| `buscar_nodos` | `(consulta, limite)` idéntica | verbatim de `harness.TOOLS` | byte-idéntico a `Neo4jIndex.buscar_nodos` serializado como el harness | **fulltext BM25 (Lucene) en vez del léxico in-memory** — divergencia deliberada y laudada (C10); `ver_nodo`/`ver_vecinos` no la tienen | transporte (stdio JSON-RPC), nombre visto por el agente `mcp__kg__buscar_nodos`, log R1 |
| `ver_nodo` | `(id)` idéntica | verbatim | byte-idéntico (paridad 10/10) | idéntico en ambos modos | solo transporte + log |
| `ver_vecinos` | `(id, direccion)` idéntica | verbatim | byte-idéntico (paridad 10/10, incl. `direccion` inválida → `ambas`) | idéntico | solo transporte + log |

### Test de paridad

```
.venv/bin/python -B data/experiment/banco_mcp/mcp_kg/test_paridad_mcp_kg.py
.venv/bin/python -B data/experiment/banco_mcp/mcp_kg/test_paridad_mcp_kg.py \
  --config data/experiment/banco_mcp/mcp_kg/config_mcp_kg_juguete.json \
  --out data/experiment/banco_mcp/mcp_kg/resultados/paridad_mcp_kg_juguete.json
```

10 llamadas por tool a través del transporte MCP (subproceso, cliente falso) contra `Neo4jIndex`
directo: **30/30 byte-idénticas**; definiciones de tools listadas == `harness.TOOLS`; log R1
con inicio + 30 llamadas + fin, `output_sha256` igual al texto recibido por el cliente
(`mcp_kg/resultados/paridad_mcp_kg.json`). Sobre el mini-grafo del gate: 30/30, y el nodo de
42.248 chars (GATE-10) llega íntegro por MCP al cliente falso
(`resultados/paridad_mcp_kg_juguete.json`).

## 2. Servidor MCP vectorial (`mcp_vector/`)

`construir_indice.py` reconstruye los 1.763 pasajes de E0 en composición **propio + herencia**
(la expresión de `bakeoff_embeddings/code/construir_gold_y_corpus.py`; ese script no se importa
porque corre a nivel de módulo y escribe en su directorio sellado — se replica la expresión y se
verifica por hash: cada pasaje contra `sha256_completo` y el corpus contra `sha256_corpus` del
bake-off) y los codifica con `microsoft/harrier-oss-v1-0.6b` @ `f9b9dc8d…`, float32, MPS,
`max_seq_length=32768`, **sin prompt en documentos**, con la misma agrupación por presupuesto de
tokens del bake-off (8448 / 32). Resultado (`mcp_vector/indice/manifiesto_indice.json`):

- `sha256_matriz = 12d284d5bce0d1d58f1e4437c47f2177b3145813586069ca72f9103309b28b65` ==
  `sha_docs` de harrier en el bake-off (`resultados/harrier.json`), con 32768 en lugar de 16384:
  0 truncados (pasaje más largo 8.233 tokens), 93 grupos; los embeddings son los mismos.

`servidor_mcp_vector.py` expone la tool única `buscar_pasajes(consulta, limite)`: prompt
`web_search_query` **solo en la consulta**, coseno, ranking score desc / id asc (desempate del
bake-off), `limite` acotado con la misma expresión que `GraphIndex._limite`. Cada pasaje cita
`to`, `archivo`, `unidad` (punto), `titulo`, `paginas`, `score` y el `texto` completo.

### Tests

```
<venv 3.12> python3 -B data/experiment/banco_mcp/mcp_vector/construir_indice.py
<venv 3.12> python3 -B data/experiment/banco_mcp/mcp_vector/test_mcp_vector.py            # con segunda construcción (b)
<venv 3.12> python3 -B data/experiment/banco_mcp/mcp_vector/test_mcp_vector.py --b-desde data/experiment/banco_mcp/mcp_vector/resultados/tests_mcp_vector_corrida1_con_reconstruccion.json   # cita (b) de la corrida 1
```

| test | criterio | resultado |
|---|---|---|
| (a) asimetría | consulta con/sin prompt: vectores distintos (coseno 0,804); filas del índice == codificación sin prompt (coseno ≥ 1−1e−5) y ≠ con prompt (0,92–0,95) | PASS |
| (b) determinismo | dos construcciones completas, sha256 de la matriz | PASS (`12d284d5…` las dos; en `tests_mcp_vector.json` citado explícitamente de `tests_mcp_vector_corrida1_con_reconstruccion.json`, porque la segunda construcción fue a un directorio temporal) |
| (c) bake-off | sha256 de la matriz == `sha_docs` de harrier (e3_entorno: mismas versiones, misma revisión, float32) | PASS |
| (d) transporte | 10 consultas por MCP byte-idénticas al cálculo directo; todo pasaje cita TO + punto; log R1 consistente | PASS (máx. 81.275 chars con `limite=50`) |

Nota medida sobre (a): re-codificar un pasaje **solo** (batch 1) difiere de la fila del índice en
1 ulp (coseno 1,0000001) por composición del batch en MPS; la identidad byte a byte exige la
misma agrupación, que es lo que (b) prueba. Por eso el criterio de (a) es numérico.

## Log R1 (los dos servidores)

JSONL, una línea por evento. `inicio` lleva config íntegra + sha, fuente (sha del kg.json /
de la matriz), entorno y `sesion_tag`; cada `llamada` lleva `call_id` (`<servidor>-<pid>-<n>`),
`n`, `rpc_request_id` (id JSON-RPC de la petición), timestamp, duración, `tool`, `input`
verbatim, `output_str` **íntegro** (la cadena exacta que viajó al cliente), `output_chars`,
`output_sha256` y `config_sha256`; `fin` cierra con el conteo. Ruta por `BANCO_LOG_R1`,
etiqueta por `BANCO_SESION_TAG`. Ninguna ruta absoluta de la máquina queda persistida.

R7: el mapa `n → tool_use_id` lo construye el adaptador (entregable 7) cruzando el orden de las
llamadas MCP de la sesión con `n` y verificando `output_sha256` contra el texto registrado.

## Tope de resultado por MCP (documentado; medición en fase B)

Según la documentación oficial (`docs/en/mcp`, "MCP output limits and warnings"): advertencia a
partir de 10.000 tokens, **límite por defecto 25.000 tokens** (`MAX_MCP_OUTPUT_TOKENS`); por
encima, "results that exceed the default threshold are persisted to disk and replaced with a file
reference in the conversation"; el servidor puede declarar `_meta["anthropic/maxResultSizeChars"]`
hasta 500.000 chars. El banco **no** usa esa anotación (cambiaría lo que ve el agente respecto
del harness) y deja el log R1 como fuente de verdad; el tope efectivo se mide con sesión real.

## 3. Agentes (`agentes/`)

Configuración sellada en `config_agentes.json` (sha en cada traza, R10): modelo `claude-sonnet-5`,
modo del harness **`--bare`**, `--tools ""` (ninguna built-in), `--strict-mcp-config --mcp-config
<brazo>.json`, `--permission-mode dontAsk`, `--allowedTools mcp__<server>__*`, `--disallowedTools`
redundante, cortes R5 (`--max-turns 12`, tope de 10 tool calls en el prompt, `--max-budget-usd 0.30`
por sesión), `--session-id` fijado por el lanzador. Cada flag lleva su cita de la doc oficial en el
JSON. **El log R1 del servidor sigue siendo la única fuente de verdad del contenido de cada tool
result**: el diseño no asume que el resultado llega íntegro al modelo (tope MCP de 25.000 tokens,
medición en fase B).

**Por qué `--bare` y no `--safe-mode`** (medido a USD 0, `aislamiento/resultados/init/`): bajo
`--safe-mode` el `--mcp-config` no carga (`mcp_servers=[]`, `tools=[]`), coherente con la doc del
flag («MCP servers … do not load»); bajo `--bare` carga y el servidor figura `connected`. La doc de
`--bare`: «skip auto-discovery of hooks, skills, custom commands, subagents, plugins, MCP servers,
auto memory, and CLAUDE.md»; «In bare mode, Claude Code never reads OAuth credentials». P0 de esta
configuración: no medido en fase A (cuesta); es el primer paso de fase B.

**Prompt** (`plantilla_prompt.txt` + `bloque_tools_<brazo>.txt`): se pasa como argumento de
`claude -p` (precedente del gate fase B; plan v6 (iii)); el prompt de sistema del harness no se
toca. Diff exacto entre brazos: `agentes/resultados/diff_prompt_brazos.txt` — solo el bloque de
tools. Contrato de salida R4 idéntico: `{"respuesta", "citas": ["documento | punto"], "respondible"}`.

**Hallazgo de versión**: Claude Code 2.1.196 no espera a servidores `pending` antes del primer
turno (doc `--mcp-config`: la espera requiere ≥ 2.1.221). El servidor vectorial carga el modelo de
forma perezosa (handshake inmediato) para figurar `connected` con su tool en `system/init`; el
`timeout` por servidor (600 s) cubre la primera llamada.

**Modo init (USD 0)**: `lanzar_agente.py --modo init` apunta `ANTHROPIC_BASE_URL` a un puerto
cerrado; ninguna petición llega a la API, el `system/init` (tools, servidores, modelo, permisos,
`apiKeySource`) se captura y el proceso se mata. Es la base del inventario R6 sin gastar.

## 4. Aislamiento por capacidad (`aislamiento/`)

```
BANCO_VENV_VECTOR=<venv 3.12> .venv/bin/python -B data/experiment/banco_mcp/aislamiento/test_aislamiento.py
```

| test | criterio | resultado |
|---|---|---|
| (a) inventario | tools en `system/init` por brazo: KG = `mcp__kg__{buscar_nodos,ver_nodo,ver_vecinos}`, vector = `mcp__vector__buscar_pasajes`; ninguna built-in; `dontAsk` | PASS |
| (b) artefactos del grafo | el agente vectorial no tiene tool de archivos ni shell; el servidor vectorial no importa módulos del grafo ni menciona sus rutas; `import neo4j` falla en su venv | PASS |
| (c) puerto Neo4j | sin tools de red/shell; el servidor vectorial no tiene driver bolt ni código de sockets | PASS |
| (d) positivo | cada servidor `connected` con sus tools en init + llamada real por el MISMO JSON de MCP devuelve datos de su fuente | PASS |

Las reglas `Read(./ruta)` no aplican a Bash (settings-reference), por eso el aislamiento es por
ausencia de capacidad y no por reglas de ruta. La denegación en runtime (el agente intenta) se
ejercita en fase B y queda en `permission_denials`. Inventario persistido por traza en
`meta_<id>.json` (`inventario_tools_R6`).

## 5. Metadata por traza (`agentes/contrato_metadata.md`)

Implementada en `lanzar_agente.py::armar_meta`. Traza de ejemplo que cumple el contrato
(`completa = true`, mapa R7 coincidente, costo R9 desde precios sellados, inventario R8 con dos
modelos): `agentes/resultados/selftest/meta_SELFTEST.json`, generada por `selftest_metadata.py`
con un `system/init` real, llamadas MCP reales (log R1 real) y un stream **sintético** sin modelo
— marcada `origen: selftest_sintetico`, no es una traza del banco.

## 6. Vía de credenciales (`agentes/config_credenciales.json`)

`--via api` (ANTHROPIC_API_KEY) o `--via bedrock` (CLAUDE_CODE_USE_BEDROCK=1); nada más cambia.
Identidad estructural: `sha_identidad_pipeline` (shas de prompt, plantilla, bloques, configs de
agentes/MCP/servidores, precios, modelo y flags) — verificado igual entre vías
(`6c04a944…` en el selftest). Umbral de switch declarado: 3 sesiones consecutivas con error de
cuota/capacidad, o proyección > 80 % del tope mensual del tier. Límites publicados: API Sonnet 5
Start tier 1.000 RPM / 2.000.000 ITPM / 400.000 OTPM, tope USD 500/mes (rate-limits); el tier
real de la cuenta y los límites de Bedrock **no se verificaron**. Suscripción: incompatible con
`--bare` (doc) ⇒ sería otra configuración R10; límites publicados (ventana rodante de 5 h +
semanal, caché de 1 h) y si el uso automatizado está permitido por los términos del plan: **no
verificado**.

## Nota de confidencialidad de los artefactos

Los `stream_*.jsonl` son salida literal de `claude -p` y contienen el `cwd` absoluto de la
máquina (no se editan: son evidencia). Todo campo generado por el código del banco va con rutas
relativas al repo o enmascaradas. Ningún dato de terceros.

## 7. Adaptador sobre MCP y demostración por clase (`adaptador/`)

`adaptador_banco.py` **importa** `gate/code/adaptador_cc.py` (truncado del harness, lector de
jsonl, constantes) y produce el payload del formato del repo usando el **log R1 como fuente de
verdad** (`output_str` íntegro) y la sesión como **índice** (orden, `tool_use_id`, JSON final).
Reconciliación R7: k-ésimo `tool_use` MCP ↔ k-ésima `llamada` del log; tool e input deben
coincidir y, si la sesión trae el texto, `sha256 == output_sha256`. Cualquier desajuste es un
`rechazo` con motivo (nunca un descarte); corte de sesión o log sin `fin` ⇒ `atribuible: false`.

**Demostración por clase sobre el transporte MCP** (`demo_clases_mcp.py`; condición de
aceptación): tools REALES del servidor (`config_mcp_kg_juguete.json`, backend memoria sobre el
mini-grafo del gate), navegaciones tomadas de las rebanadas selladas del gate (fase A
escenificada + fase B con agente real) vía `adaptador_cc.candidatos` importado, ejecutadas contra
el servidor por el cliente falso; sesión con la forma de Claude Code; atribución con A0.2
importado; replay estándar y fuerte; adaptación y atribución dobles.

```
.venv/bin/python -B data/experiment/banco_mcp/adaptador/demo_clases_mcp.py
```

Resultado (`adaptador/resultados/demo_clases/demo_clases_mcp.{json,md}`): **19 casos,
maquinaria 19/19, clase 18/19**; el único «difiere» es GATE-03@B (esperado `alcanzabilidad`,
obtenido `generacion`), **el mismo resultado que el gate obtuvo en fase B** con el agente real
(llegó al ancla por vecinos: caso (V,F,V) de la regla). Bordes: sesión sin tool calls (GATE-07@A),
tools vacías/id inexistente (GATE-08), corte (GATE-09@A → detectado, no atribuible), resultado de
42.248 chars íntegro (GATE-10). GATE-11 (v2) no corrido: fuera del banco por R2.

**Tope de tamaño de resultado** (`medir_tope_mcp.py` → `resultados/tope_mcp.json`): el
transporte del banco (servidor + SDK mcp 1.29 + stdio) devolvió byte-idénticos y con log R1
íntegro resultados de 101.188 / 1.010.188 / 5.050.188 / 20.200.188 / **50.500.188 chars**
(8,96 s): sin tope en el rango probado. El tope de **Claude Code** (lo que ve el modelo) es
25.000 tokens por defecto según la doc (`MAX_MCP_OUTPUT_TOKENS`; por encima «persisted to disk
and replaced with a file reference»); se mide con sesión real en fase B. Máximos naturales
medidos: 17.719 (KG Neo4j, `limite=50`), 42.248 (nodo grande del gate), 81.275 (vectorial,
`limite=50`).

## 8. Selftest integrador y estimación de fase B (`smoke/`)

`selftest_integrador.py` (USD 0): por brazo, init real → sesión con llamadas MCP reales sobre la
fuente real → log R1 → adaptador → metadata; en el brazo KG, atribución con A0.2 importado y
**replay estándar y fuerte contra `Neo4jIndex` en modo `fulltext`** (el mismo backend y modo del
servidor): PASS en los dos brazos (`smoke/resultados/selftest_integrador/`). Ancla y veredicto
propios y sintéticos (`cap:8.6`, `incorrecto`); EV2 no se abre.

`estimacion_faseB.json`: fórmula por sesión sin precios (cache write = P0+Q en el turno 1; cache
read = (T−1)(P0+Q); input sin caché = Σ tool results previos; output = 150·T), con P0 = 9.412 de
b08095a como cota (el P0 de `--bare` se mide primero en fase B), tamaños de resultado medidos y
navegación típica: 4 preguntas × 2 brazos + 2 sesiones de P0 = 10 sesiones ≈ 102k cache write,
246k cache read, 68k input, 5k output (Sonnet) ⇒ **≈ USD 0,50 a precios sellados**; contraste:
las 9 sesiones reales del gate costaron USD 0,42. Tope propuesto USD 3, freno interno 2, freno por
proyección 2,4. `preguntas_smoke.json` (4 preguntas propias con anclas propias que resuelven en
el KG, **territorio verificado** con `verificar_territorio.py`: 0 solapes por ancla y por prefijo de
punto contra el gold de fidelidad EV2, los pares sintéticos de EV2 —set y población— y los pares v3
de la ablación; chequeo obligatorio para toda pregunta futura del banco. **Desvío detectado en
revisión**: la versión inicial usaba `cap:8.6` y `pro:2.1`, anclas del gold de EV2; reemplazadas por
`cap:1.3` y `pro:2.7` antes de correr) y `correr_smoke.py` (exige `--autorizado-tope`; P0 → preguntas × brazos → aislamiento
end-to-end → adaptación + atribución → contabilidad R9 vs CLI) quedan escritos y sin correr.

## Consecuencias de diseño para el plan

- La versión del CLI es variable sellada (`config_agentes.json`: 2.1.196); si se actualiza, se
  declara y se re-valida el smoke.
- Fase B requiere `ANTHROPIC_API_KEY` (o Bedrock) en el entorno del runner: con la configuración
  sellada `--bare` el login OAuth de la suscripción no se usa (doc). Sin clave API en el entorno, el
  smoke no arranca (guarda del lanzador).
- `--bare` deja la **vía de suscripción fuera del banco**; las vías son API y Bedrock, con el
  umbral de switch declarado (3 sesiones consecutivas con error de cuota, o > 80 % del tope
  mensual del tier).

## Fase B (resumen; detalle en `smoke/resultados/faseB_corrida2/reporte_faseB_corrida2.md`)

- Corrida 2 bajo el re-sellado 2.1.241: 12/12 sesiones con tools en init y servidores
  `connected`; 8/8 SMK `completa=true` (R3 con C3); mapa R7 43/43; `fin` en ambos logs (C2);
  atribución + replay estándar y fuerte en verde con `Neo4jIndex` fulltext; aislamiento
  end-to-end (a)–(d) con 0 denials (por ausencia de capacidad); nada truncado por el transporte
  (máx. 17.884 chars, byte-igual al log R1); P0 de `--bare` con tools: kg 3.134 / vector 2.728
  (9.412 de safe-mode queda como referencia histórica de otra versión).
- Validación cruzada nueva: en ≥ 2.1.221 `total_cost_usd` del CLI == recómputo R9 (razón 1,0 en
  12/12; era 2,3–3,1× en 2.1.196). El banco sigue computando desde tokens (R9).
- Hallazgo H-B2 declarado: `--max-turns 12` no disparó con `num_turns=14` (SMK-04-kg); la
  semántica de `num_turns` vs «agentic turns» queda por caracterizar antes del pre-registro de
  A2.1. El tope de tool calls del prompt es instructivo (excedido una vez: 13).
- Registro para C0.3/C1.7 (encuadre laudado): la fabricación de respuestas de tool con formato
  verosímil en la corrida 1 (SMK-01-vector; 7/8 pseudo-llamadas) ocurrió bajo una contradicción
  de configuración — el prompt describía tools que el harness no había conectado —; es evidencia
  de que un agente sin fuente produce la forma de la evidencia sin la evidencia, NO una medida
  de propensión a fabricar en condiciones normales.
