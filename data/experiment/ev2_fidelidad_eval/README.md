# ev2_fidelidad_eval — evaluación de fidelidad de las 120 respuestas de EV2

Unidad que ejecuta el método pre-registrado en
`docs/preregistro_evaluacion_fidelidad_ev2.md` (commit `be8a84f`) con el juez
calibrado y CONGELADO de `data/experiment/ev2_juez/` (commit `1a0ac5c`:
`prompt_juez_v1.md` sha256 `fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455`,
`juez.py`, `mapping.py`) — se importan, jamás se editan. El cuarteto sellado de
`data/experiment/evaluacion/` tampoco se toca (sha 4/4 verificados al inicio y
al fin de cada corrida por `comun_fidelidad.verificar_sellos`).

Insumos (solo lectura): gold sellado
`data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json`
(commit `9c44516`; 40 preguntas / 164 criterios con cita) y las 120 trazas
`EV2F-*` de `data/experiment/ev2_corrida/trazas/ev2_base_{v2,v3,run3}/`
(commit `bb89a8e`); al juez viaja únicamente `trace.final_json.respuesta`.

## Diseño

- **Ceguera de grafo (§3).** El input del juez es exactamente prompt +
  (pregunta, respuesta, criterios con cita) — lo arma `juez.construir_kwargs`.
  Cada respuesta recibe un id opaco `EV2R-<10 hex>` =
  sha256(`juez-ev2-v1|id_pregunta|grafo|sha256(respuesta)`)[:10]. La tabla
  id_opaco → (id_pregunta, grafo, label, sha256 respuesta) vive en
  `desanonimizacion/tabla_id_opaco.json`, FUERA de `out/` y de todo input del
  juez. El pipeline recibe solo la vista ciega (id_opaco, pregunta, respuesta,
  criterios). El selftest verifica la no-fuga estructuralmente.
- **Orden (§3).** `orden/orden_ev2_fidelidad_ciego.json`: lista de 120 ids
  opacos = `random.Random("juez-ev2-v1").shuffle` sobre la lista ordenada por
  (id_pregunta, sha256 de la respuesta). Sin empates.
- **N=3 (§4).** Tres pasadas completas, una db de caché y un label por
  repetición (`cache/ev2_eval_r{1,2,3}.db`, labels `ev2_eval_r{1,2,3}`; patrón
  rt_c6_n3); 0 cross-hits verificados por keys disjuntas y access_log.
  Veredicto modal por par y mapping §2 en código (`mapping.py` del juez).
- **Salidas por respuesta (ciegas, en `out/`).** Veredictos por criterio de
  las 3 reps, fragmentos, justificaciones, clasificación auxiliar
  abstencion/contenido (3 reps + modal), veredicto de pregunta por mapping y
  auditoría mecánica de fragmentos (`auditoria_fragmentos.py`: null /
  verbatim / fuga_gold / no_verbatim — misma regla de
  `ev2_juez/analisis_acuerdo.py`, copiada verbatim y verificada por el selftest).
- **Reporte ciego.** `out/reporte_ciego.md` + `out/veredictos_agregados_ciego.json`
  por id opaco. El cruce veredicto × grafo NO se computa en la unidad: lo hace
  la revisión (`code/cruce_mesa.py`, probado solo sobre datos sintéticos).
- **Gasto.** Real desde las tablas `cache` de las dbs; freno por proyección
  antes de cada llamada; precios y tope solo por CLI.

## Archivos

- `code/comun_fidelidad.py` — sellos, carga (censo), ids opacos, orden, tabla, vista ciega.
- `code/preparar_carga.py` — fase A.a/b: `carga/censo_carga.json`, `orden/`,
  `desanonimizacion/`, `carga/mensajes_reales_medicion.json`.
- `code/pipeline_fidelidad.py` — fase B (gateada por `--autorizado-fase-b
  --precio-in --precio-out --tope`), agregación, cross-hits, reporte ciego;
  `--solo-agregados` recomputa sin API.
- `code/auditoria_fragmentos.py` — regla de auditoría de fragmentos.
- `code/selftest_fidelidad.py` — selftest offline (64 checks; escribe `selftest_out/`, gitignorado).
- `code/estimacion_fidelidad.py` — estimación sin precios → `estimacion/estimacion_fase_b.{json,md}`.
- `code/cruce_mesa.py` — herramienta de la revisión (no se corre sobre salidas reales en la unidad).
- `checkpoint_sesion.md` — estado de la unidad.

## Reproducción (offline, USD 0)

```
.venv/bin/python -B data/experiment/ev2_fidelidad_eval/code/preparar_carga.py
.venv/bin/python -B data/experiment/ev2_fidelidad_eval/code/selftest_fidelidad.py
.venv/bin/python -B data/experiment/ev2_fidelidad_eval/code/estimacion_fidelidad.py
```

Fase B (gasto real) solo con autorización explícita con precios y tope:

```
.venv/bin/python -B data/experiment/ev2_fidelidad_eval/code/pipeline_fidelidad.py \
    --autorizado-fase-b --precio-in <USD/MTok> --precio-out <USD/MTok> --tope <USD>
```
