# Fase B — corrida 2 (2026-08-23, Claude Code 2.1.241 re-sellado): reporte

Corrida por la autora con `correr_smoke.py` (tope 3 / freno 2 / proyección 2,4; vía `api`).
12 sesiones: 2 P0 + 4 preguntas × 2 brazos + 2 E2E. Gasto R9 **USD 0,4410** (CLI 0,4410; razón 1,0 — §5).
Acumulado de la unidad con la corrida 1 declarada: 0,093 + 0,441 = **USD 0,534** de tope 3.
Ningún freno disparó (proyección tras P0: 0,1654).

## 1. Checklist del criterio de aceptación laudado

| criterio | resultado | evidencia |
|---|---|---|
| tools no vacías en init + servidores `connected` | **12/12** (8/8 SMK) — kg: 3 tools, vector: 1; `coincide=true` en todas | `meta_*.json → inventario_tools_R6`, `servidores_mcp.en_init` |
| ≥ 1 llamada en cada log R1 (SMK) con correlación al stream | **8/8** — kg: 7/10/8/13; vector: 1/1/1/2; mapa R7 completo: `coincide_tool_input=true` en los 43 steps y `n_llamadas(log) == tool_use(stream)` en todas | `meta_*.json → mapa_R7`, `log_r1_*.jsonl` |
| JSON del contrato presente | **12/12** (también P0 y E2E) | `meta_*.json → final_json_R4` |
| línea `fin` en los dos servidores (C2) | **12/12**, incluido el vectorial (en la corrida 1: 0/6) | `log_r1_*.jsonl`, última línea |
| versión del CLI == sellada | 12/12 `2.1.241`, `coincide_con_sellada=true` | `meta → harness_R10` |

## 2. Circuito completo por sesión (traza → adaptador → atribución → replay)

Adaptación con `adaptador_banco.py` (log R1 = fuente de verdad); atribución del brazo KG con el
código de A0.2 importado y replay contra `Neo4jIndex(KG_Refinado, fulltext)`; al no haber
veredicto de juez (el banco no evalúa), la atribución se ejercitó con los tres veredictos
posibles — con `correcto` la clase es `null` por regla (no se atribuye falla), como corresponde.

| sesión | steps | atribuible | completa R3 | clase (incorrecto/parcial) | replay | replay fuerte | determinismo | max chars step |
|---|---|---|---|---|---|---|---|---|
| SMK-01-kg | 7 | ✓ | ✓ | generacion / generacion | ✓ | ✓ | ✓ | 3.582 |
| SMK-01-vector | 1 | ✓ | ✓ | n/a (brazo sin clases A0.2) | — | — | — | 10.718 |
| SMK-02-kg | 10 | ✓ | ✓ | generacion / generacion | ✓ | ✓ | ✓ | 3.808 |
| SMK-02-vector | 1 | ✓ | ✓ | n/a | — | — | — | 16.631 |
| SMK-03-kg | 8 | ✓ | ✓ | generacion / generacion | ✓ | ✓ | ✓ | 3.836 |
| SMK-03-vector | 1 | ✓ | ✓ | n/a | — | — | — | 17.884 |
| SMK-04-kg | 13 | ✓ | ✓ | generacion / generacion | ✓ | ✓ | ✓ | 3.992 |
| SMK-04-vector | 2 | ✓ | ✓ | n/a | — | — | — | 11.540 |

Nada de lo que pasó en fase A falló acá: replay estándar y fuerte 4/4 sesiones KG con los tres
veredictos, determinismo 4/4, adaptador sin rechazos ni descartes (43/43 steps, 0 `rechazos`).
Las cuatro clases del gate no se re-ejercitan acá (las preguntas propias tienen ancla presente y
consultada ⇒ `generacion`); la demostración por clase completa quedó hecha sobre MCP en fase A
(19 casos) y la corrida real la confirma en la clase que las sesiones producen.

**Hallazgo H-B2 (se declara, no se ajusta): `--max-turns 12` no disparó con `num_turns=14`.**
SMK-04-kg terminó `subtype=success` con `num_turns=14` (13 tool calls). O bien `num_turns` del
`result` no cuenta lo mismo que los «agentic turns» del flag (p. ej. incluye llamadas internas),
o el límite no se aplicó. Con lo persistido no se puede decidir; queda como caracterización
pendiente del corte R5 antes del pre-registro de A2.1 (el corte operativo del banco siguió
siendo el tope del prompt + `--max-budget-usd`). Relacionado: el tope de 10 tool calls del
prompt fue excedido por el agente en SMK-04-kg (13) — comportamiento ya declarado como posible
en `config_agentes.json` (el tope del prompt es instructivo; se registra el valor real).

## 3. Aislamiento end-to-end sobre sesiones reales

| | resultado | evidencia |
|---|---|---|
| (a) inventario | 12/12 sesiones con exactamente las tools de su brazo (las del KG nunca en el vectorial ni viceversa; ninguna built-in) | `meta_* → inventario_tools_R6` |
| (b) artefactos del grafo | E2E-kg: se le pidió leer `kg.json`; el agente respondió que no tiene acceso a archivos, `respondible:false`, **0 tool calls, 0 denials** (no hay tool que denegar: aislamiento por ausencia de capacidad, no por rechazo) | `meta_E2E-kg.json` |
| (c) puerto Neo4j | E2E-vector: se le pidió conectarse al 7687; respondió que solo tiene `buscar_pasajes`, `respondible:false`; hizo 1 llamada legítima a su propia tool (consulta sobre el pedido, 1.447 chars) | `meta_E2E-vector.json`, `log_r1_E2E-vector.jsonl` |
| (d) positivo | los dos brazos alcanzaron su fuente con el agente real: 38 llamadas KG (Neo4j fulltext, kg_sha 26fac8b4…) y 5+1 vectoriales (matriz 12d284d5…) con resultados no vacíos | logs R1, `trazas/` |

`permission_denials = []` en las 12 sesiones: coherente con el diseño (sin capacidad no hay
intento que denegar).

## 4. Cap de resultados MCP: qué llegó al modelo

La sonda `limite=50` (81.275 chars) **no se ejercitó**: el agente usó siempre `limite` 3-10.
Máximo observado: **17.884 chars** (SMK-03-vector, `buscar_pasajes` limite 10). En los **43/43**
steps el texto del `tool_result` de la sesión es **byte-idéntico** al `output_str` íntegro del
log R1 (`sesion_igual_al_log=true`, `sesion_truncada_por_transporte=false`, 0 derrames a
archivo): por debajo del umbral documentado de 25.000 tokens nada se truncó ni se derivó a
disco. El cap de Claude Code por encima del umbral sigue **no medido con sesión real** (ningún
resultado natural lo alcanzó); el número del transporte del banco (sin tope hasta 50,5 M chars)
y el comportamiento documentado del CLI quedan como cota, y el log R1 sigue siendo la fuente de
verdad en cualquier caso.

## 5. Costos: R9 vs CLI por sesión

| sesión | R9 (tokens × precios sellados) | `total_cost_usd` CLI | razón |
|---|---|---|---|
| P0-kg | 0,009681 | 0,009681 | 1,000 |
| P0-vector | 0,008588 | 0,008588 | 1,000 |
| SMK-01-kg | 0,036337 | 0,036337 | 1,000 |
| SMK-01-vector | 0,024779 | 0,024779 | 1,000 |
| SMK-02-kg | 0,062019 | 0,062019 | 1,000 |
| SMK-02-vector | 0,030177 | 0,030177 | 1,000 |
| SMK-03-kg | 0,051522 | 0,051522 | 1,000 |
| SMK-03-vector | 0,033988 | 0,033988 | 1,000 |
| SMK-04-kg | 0,078474 | 0,078474 | 1,000 |
| SMK-04-vector | 0,078726 | 0,078726 | 1,000 |
| E2E-kg | 0,011626 | 0,011626 | 1,000 |
| E2E-vector | 0,015080 | 0,015080 | 1,000 |
| **total** | **0,4410** | **0,4410** | **1,0** |

**Registro de cambio de comportamiento del CLI**: en 2.1.196 la razón CLI/R9 fue 2,3× en la
corrida 1 y ~3,1× en la fase B del gate (b08095a, R9); en **≥ 2.1.221 el `total_cost_usd`
coincide con el recómputo desde tokens a precios oficiales** (12/12 sesiones al décimo de
centavo). El banco sigue computando desde tokens (R9) — la coincidencia se declara como
**validación cruzada nueva**, no como cambio de fuente.

## 6. P0 definitivo de `--bare` (con tools conectadas)

| brazo | P0 (cache_creation de la 1.ª llamada, `--max-turns 1`) | componentes |
|---|---|---|
| kg | **3.134 tokens** | 2.162 (harness desnudo, cota de la corrida 1) + ~972 de las 3 defs v1 |
| vector | **2.728 tokens** | 2.070 + ~658 de `buscar_pasajes` |

Referencia histórica (otra versión y otra configuración, sin contraste directo — alcance del
re-sellado laudado): 9.412 tokens en `--safe-mode` bajo 2.1.196 (gate, b08095a). El prompt entra
como cacheable: las sesiones SMK leen el prefijo de caché escrito por P0.
