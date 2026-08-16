# checkpoint_sesion — evaluación de fidelidad EV2 (120 respuestas × juez v1)

## Fase A (offline, USD 0) — HECHA, esperando revisión (2026-08-16)

- Branch `main`; working tree limpio al inicio salvo este directorio (nuevo).
- Sellos verificados: prompt v1 `fd446f8e61f4…`; juez.py `b4a74ba536dd…`;
  mapping.py `c905dd1a5109…`; cuarteto 4/4 (loader `5aba8b7a…`, harness
  `fd267e83…`, judge `71691459…`, llm_cache `fc86b0e4…`); gold `1d587336…`.
- Carga: 120 respuestas = 40 × {v2, v3, run_3} = 3 por pregunta × 40; 164
  criterios; 0 marcadores de grafo en las 120 respuestas; flag respondible
  84 True / 36 False (metadato, no viaja al juez).
- Ids opacos 120 únicos; orden `juez-ev2-v1` persistido (`orden/`); tabla en
  `desanonimizacion/`; sin empates en la clave (id_pregunta, sha256).
- Selftest 64/64 PASS (`code/selftest_fidelidad.py`); tests_mapping del juez 20/20.
- Estimación (`estimacion/estimacion_fase_b.json`): 360 llamadas; entrada
  ~580.953 tokens [557.498–609.851]; salida ~207.903 (cota máx 258.480). Sin precios.
- Nada llamado a la API. `cache/` no existe. `out/` no existe.

## Fase B — PENDIENTE de autorización explícita (precios + tope)

Comando previsto:
`.venv/bin/python -B data/experiment/ev2_fidelidad_eval/code/pipeline_fidelidad.py --autorizado-fase-b --precio-in <in> --precio-out <out> --tope <tope>`
(retomable: write-through por id opaco; freno por proyección; luego
`--solo-agregados` recomputa reporte). Al terminar: gasto real desde dbs, 0
cross-hits, distribución ciega, reporte ciego + tabla aparte. NO cruzar
veredicto × grafo. FRENAR.

## Reglas vivas

Cero commits; nada fuera de `data/experiment/ev2_fidelidad_eval/`; juez y
cuarteto intocables; jamás editar prompt/juez.py/mapping.py; nombres jamás.

## Fase B — AUTORIZADA y LANZADA (2026-08-16 11:11 EDT)
- Precios in 3.00 / out 15.00 USD/MTok; TOPE 7.00 con freno por proyección.
- Comando: pipeline_fidelidad.py --autorizado-fase-b --precio-in 3.00 --precio-out 15.00 --tope 7.00
  (log en out/log_fase_b.txt). Retomable: si se corta, re-lanzar el mismo comando.
- Si errores/incompletas > 0: FRENAR para laudo antes de agregar.

## Fase B — TERMINADA (2026-08-16 11:51 EDT), esperando revisión de mesa
- 360/360 llamadas, 0 errores, 0 incompletas, sin freno; gasto real desde dbs USD 4,3405
  (585.801 in / 172.205 out; por rep 1,4411 / 1,4479 / 1,4515); 0 cross-hits; 0 hits.
- Distribución ciega (mapping §2): parcial 63 / incorrecto 27 / requiere_adjudicacion 21 / correcto 9.
- Pares 492: unánimes 483; sin_consenso 0; fragmentos null 673 / verbatim 792 / fuga_gold 0 / no_verbatim 11
  (los 11 = concatenaciones de piezas presentes en la respuesta).
- Salidas: out/veredictos_r{1,2,3}.jsonl, veredictos_agregados_ciego.json, reporte_ciego.md,
  resumen_corrida.json, log_fase_b.txt; sellos inicio==fin (carga/sellos_{inicio,fin}_faseB.txt).
- El cruce veredicto × grafo NO se computó: lo hace la mesa con desanonimizacion/tabla_id_opaco.json
  (code/cruce_mesa.py). Cero commits.
