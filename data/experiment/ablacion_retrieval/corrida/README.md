# Corrida factorial de la ablación de retrieval — U-A1.4 (plan de tesis, carril A, bloque A1)

Corrida de la ablación 2×2 {booleano, BM25} × {tools v1, tools v2} sobre
KG-Refinado (sha `26fac8b4…`) según el pre-registro SELLADO en `68c79dc`
(`../preregistro_ablacion.md`: diseño §1, config §2, material §3, métrica y
régimen §4, predicciones §5, presupuesto §6, reglas §7). NADA de lo sellado en
`..` (pre-registro, `celdas/`, `pares/`, `muestreo/`, anexo) se edita: este
directorio lo LEE, verifica cada pieza por sha256 y ejecuta.

Estado: **fase A hecha ($0)** — runner por celda, replay determinístico
(v1 + adaptador v2-aware con tests), pipeline de análisis completo, selftest
offline 75/75 con cliente falso, estimación. **Fase B EJECUTADA (2026-08-18,
autorizada con precios verificados Haiku 1/5 USD por MTok y tope USD 20):**
4 celdas × 100 casos = 400 trazas en `trazas/`, gasto real desde las dbs
USD 11,1948 (C00 2,8292 · C10 2,7669 · C01 2,8519 · C11 2,7468; cuota 5,00
por celda, sin frenos), `cache_stats.hits == 0` en las 4 dbs, 1 error técnico
persistido y declarado (C10 `EB-005::antilexica`, 400 permanente del harness,
precedente EA-013), replay estándar + fuerte 400/400 OK con doble corrida
byte-idéntica, análisis en `resultados/` (P1 cumplida · P2 no cumplida · P3
cumplida · P4 no cumplida · P5 cumplida · P6 no cumplida — lectura mecánica;
la interpretación es de la mesa y la autora). Pendiente: commit de la autora.

Prerrequisito: contenedor Neo4j de U-A1.1 con KG-Refinado cargado
(`../../neo4j/README.md`, `docker compose up -d` + `cargar_kg.py`); todo script
verifica `KG_Meta.kg_sha256 == 26fac8b4…` antes de tocar el grafo.

## Comandos (desde la raíz del repo)

```bash
# 0. piezas selladas + celdas contra sus sha (exit 0)
.venv/bin/python -B data/experiment/ablacion_retrieval/comun_ablacion.py
.venv/bin/python -B data/experiment/ablacion_retrieval/celdas.py --check
.venv/bin/python -B data/experiment/neo4j/cargar_kg.py --solo-verificar
# 1. fase A: selftest offline (cliente LLM falso, tools contra Neo4j real, $0) y tests del adaptador
.venv/bin/python -B data/experiment/ablacion_retrieval/corrida/selftest_ablacion.py
.venv/bin/python -B data/experiment/ablacion_retrieval/corrida/tests_replay_v2.py
# 2. estimación (tarifa Haiku = harness.PRICE_*, a re-verificar en la autorización)
.venv/bin/python -B data/experiment/ablacion_retrieval/corrida/estimacion_ablacion.py
# 3. fase B — SOLO con autorización explícita (precios verificados + tope), orden C00, C10, C01, C11
export ABLACION_A14_TOPE_USD=20
.venv/bin/python -B data/experiment/ablacion_retrieval/corrida/runner_ablacion.py --celda all --autorizado --precio-in <P_in> --precio-out <P_out>
# 4. replay determinístico de TODAS las trazas (doble corrida byte-idéntica) y análisis
.venv/bin/python -B data/experiment/ablacion_retrieval/corrida/replay_ablacion.py
.venv/bin/python -B data/experiment/ablacion_retrieval/corrida/analisis_ablacion.py
```

## Mapa

| archivo | qué es |
|---|---|
| `comun_corrida.py` | rutas, constantes pre-registradas por referencia (orden `C00,C10,C01,C11`, semillas `orden-ablacion-v1` / `bootstrap-ablacion-v1`, 10.000 remuestreos, umbrales P1–P6, n mínimo 8), carga verificada de celdas (sha archivo/prompt/specs vs `manifest_celdas.json`) y pares (sha vs `manifest_pares_v3.txt`), casos y orden, namespace por celda, `verificar_kg_meta`, índice de anclas |
| `agente_celda.py` | `BackendCelda` (despacho de las 3 tools contra Neo4j según los factores; mismos defaults que `harness._run_tool` / `ToolsV2.despachar`) y `AgenteCelda(GraphAgentV2)` (prompt/specs de la celda, `ask` copiado verificado, captura de outputs íntegros + latencia por tool; aserciones C00 == harness verbatim, C11 == A1.2 verbatim) |
| `runner_ablacion.py` | runner por celda: db fresca por celda `cache/ablacion_<celda>.db`, namespace `agent\|gfp=<sha KG>\|cv=<sha harness>+<sha celda>\|think=0`, write-through, retoma idempotente (traza existente ⇒ salteo sin accesos; reanudación intra-caso ⇒ hits declarados), freno por proyección (cuota = tope/4, ≥ 3 hechos), freno duro por contenedor, error API/harness persistido y declarado; gate `--autorizado` + `ABLACION_A14_TOPE_USD` + `--precio-in/--precio-out`; `gasto_desde_db` |
| `replay_ablacion.py` | replay estándar + fuerte de todas las trazas: v1 con `metrica_ev2.evaluar_caso(index=Neo4jIndex(modo))` sin cambios (+ cruce in-memory `GraphIndex` para el control); v2 con `reejecutar_step_celda` inyectado por atributo de módulo en `metrica`/`metrica_ev2`; doble corrida byte-idéntica → `resultados/replay_<celda>.json`, `replay_verificacion.json` |
| `tests_replay_v2.py` | tests del adaptador v2-aware (15): igualdad con `ToolsV2`, paridad v1, retrievers, inyección/restauración, replay fuerte falla con el re-ejecutor equivocado |
| `analisis_ablacion.py` | tabla central micro/macro (grupo todos, cohortes E-E / E-A..E-D separadas, estratos, sub-estratos), diferencias apareadas con IC bootstrap 95 %, P1–P6 mecánico con regla de lectura textual, tasas (hit_tool_limit, abstención, parse_ok, errores), latencias p50/p95 por pregunta y por tool → `resultados/analisis_ablacion.json` + `reporte_analisis.md`; operacionalizaciones declaradas |
| `estimacion_ablacion.py` | estimación §6 parametrizada (tokens medios del resumen publicado de EV2 base v3, fórmula del harness sin precios) → `resultados/estimacion_ablacion.json` |
| `selftest_ablacion.py` | selftest offline S0–S7 (75 checks) → `selftest_out/` (gitignorado) |
| `trazas/<celda>/` | (fase B) una traza JSON por caso + `resumen_ablacion_<celda>.json` |
| `resultados/` | `replay_<celda>.json`, `replay_verificacion.json`, `analisis_ablacion.json`, `reporte_analisis.md`, `gasto_real_faseB.json`, `estimacion_ablacion.json` |
| `.gitignore` | local: `cache/`, `selftest_out/`, `__pycache__/` |

Reuso sin edición: cuarteto (`harness`/`loader`/`llm_cache`), `neo4j_index`/`grafos`/
`conexion` (A1.1), `tools_v2`/`agente_v2` (A1.2), `metrica`/`resolucion`/`comun`
(sintéticas), `metrica_ev2`/`comun_ev2` (EV2, solo agregados publicados y
`cargar_runtime`), `run_posthoc._turns_since` (crudos vía access_log).
Principio 7: ningún material EV2 (preguntas, pares, trazas) se abre.
