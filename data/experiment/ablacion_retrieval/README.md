# Ablación de retrieval sobre KG-Refinado — U-A1.3 (plan de tesis, carril A, A1.3; corrida en A1.4)

Pre-registro sellado de la ablación factorial 2×2 {booleano, BM25} × {tools v1,
tools v2} (issue #5, sub-pregunta (ii) "retrieval ≠ estructura") + generación del
material NUEVO (pares sintéticos, semilla `sinteticas-faseA-v3`) con el pipeline de
`data/experiment/exploracion/sinteticas/` importado sin editar. Documento rector:
**`preregistro_ablacion.md`** (decisiones y umbrales marcados para la autora).

Estado: **fase A hecha ($0)** — pre-registro con laudos sellados, 4 celdas selladas
por sha, muestreo en seco verificado; **fase B ejecutada** (autorizada; sin E-C por
laudo O1): 50 pares aptos de 80 samples en `pares/pares_v3.json`, gasto real
USD 1,6957 (tope 3,00), desvíos declarados en el pre-registro §3. Pendiente: commit
de la autora (sello) y A1.4 con mandato propio. Esta unidad NO usa el
contenedor Neo4j (todo corre sobre `kg.json`); A1.4 sí.

Principio 7: ningún material EV2 (preguntas, criterios, pares, trazas de
`ev2_corrida`) se abrió; solo agregados publicados (`resumen_ev2_base_*.json`,
`reporte_navegabilidad.md`).

## Comandos (desde la raíz del repo)

```bash
# 0. piezas selladas (cuarteto, kg 26fac8b4, neo4j, agente_v2, pipeline de sintéticas): exit 0
.venv/bin/python -B data/experiment/ablacion_retrieval/comun_ablacion.py
# 1. celdas: construir / verificar contra lo escrito
.venv/bin/python -B data/experiment/ablacion_retrieval/celdas.py
.venv/bin/python -B data/experiment/ablacion_retrieval/celdas.py --check
# 2. muestreo en seco v3 (doble corrida byte-idéntica, censo, huérfanos, selftest stub, estimación)
.venv/bin/python -B data/experiment/ablacion_retrieval/muestreo_v3.py
# 3. fase B — selftests sin API
.venv/bin/python -B data/experiment/ablacion_retrieval/generar_pares_v3.py --selftest
.venv/bin/python -B data/experiment/ablacion_retrieval/validar_pares_v3.py --selftest
# 3'. fase B — SOLO con autorización (precios + tope) y decisión sobre estratos (E-C, ver pre-registro §3)
.venv/bin/python -B data/experiment/ablacion_retrieval/generar_pares_v3.py --preparar --estratos E-A,E-B,E-D,E-E   # u omitir --estratos
export ABLACION_TOPE_USD=3.00
.venv/bin/python -B data/experiment/ablacion_retrieval/generar_pares_v3.py --todo --autorizado
.venv/bin/python -B data/experiment/ablacion_retrieval/validar_pares_v3.py
```

## Mapa

| archivo / directorio | qué es |
|---|---|
| `preregistro_ablacion.md` | pre-registro §1 diseño · §2 config congelada · §3 material · §4 métrica y corrida · §5 predicciones · §6 presupuesto · §7 reglas |
| `anexo_solapamiento_anclas.md` | pool de anclas elegibles por estrato (175) y solapamiento esperado entre muestreos (hipergeométrica vs simulación ponderada; 28/37 dentro del IC 95 %) |
| `comun_ablacion.py` | rutas, `PIEZAS_SELLADAS` (sha256), `verificar_piezas()` |
| `celdas.py` → `celdas/` | las 4 celdas: prompt del sistema + specs + backend por tool, con sha; `manifest_celdas.json` |
| `muestreo_v3.py` → `muestreo/` | `samples_v3.json` (98 samples), `resumen_muestreo_v3.json`, `estimacion_faseB_v3.json` |
| `generar_pares_v3.py` | fase B: `runner_faseB` + `cliente_faseB` reusados por inyección de atributos (db y tope propios) |
| `validar_pares_v3.py` → `pares/` | set a sellar (`pares_v3.json`, 50 pares), registro de intentos, censo en KG-Refinado, validación (+ huérfanos P6, gasto real desde la db), manifest |
| `.gitignore` | local: `cache/` (dbs de la fase B), `__pycache__/` |

Reuso sin edición: `harness.py`/`loader.py`/`llm_cache.py` (cuarteto), `sampler`/
`generador`/`validador`/`resolucion`/`metrica`/`estimacion`/`runner_faseB`/
`cliente_faseB` (sintéticas), `neo4j_index`/`indices`/`grafos` (A1.1),
`tools_v2`/`agente_v2` (A1.2). Los únicos "cambios" son la semilla y la inyección
de rutas/tope por atributo de módulo en runtime.
