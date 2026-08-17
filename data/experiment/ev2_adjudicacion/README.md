# ev2_adjudicacion — worksheet ciego de adjudicación humana de EV2 (§6)

Construye el worksheet con el que la autora adjudica, contra el PDF del TO y el
gold sellado, (a) los pares que la evaluación de fidelidad dejó en
`requiere_adjudicacion` y (b) la muestra simétrica del §6 del pre-registro
(`docs/preregistro_evaluacion_fidelidad_ev2.md`, commit be8a84f). Provee el
script que cierra la adjudicación (mapping §2 + `agregar_par`) y emite los
veredictos definitivos ciegos y la tasa de error del juez en ambas direcciones.

Todo OFFLINE (USD 0): ninguna llamada a API. Insumos solo lectura (sha
registrados en cada salida SOLO_MESA):

- base: `ev2_fidelidad_eval/out/veredictos_agregados_ciego.json` +
  `ev2_fidelidad_eval/desanonimizacion/tabla_id_opaco.json` (commit b624865);
- §7: `ev2_encadenamiento/reporte/veredictos_finales_ciego.json`,
  `ev2_encadenamiento/juez_out/veredictos_agregados_ciego.json`,
  `ev2_encadenamiento/desanonimizacion_SOLO_MESA/tabla_id_opaco_encadenamiento_SOLO_MESA.json`
  (commit 9044a04);
- respuestas: trazas `ev2_corrida/trazas/ev2_base_*/` y `ev2_encadenamiento/trazas/ev2_enc_*/`
  (solo `trace.final_json.respuesta`, sha256 verificado contra las tablas);
- gold: `exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json`;
- reglas importadas, jamás copiadas: `ev2_juez/mapping.py` (§2) y
  `ev2_encadenamiento/code/agregacion_enc.py` (`agregar_par`, protocolo §3).

## Veredicto final por par y población

Final pre-adjudicación por par (pregunta, grafo): si el par fue re-corrido en
el §7 (63 parciales + 3 auditoría), el agregado de las 3 re-corridas
(re-verificado con `agregar_par`); si no, el veredicto de la respuesta base.
Cruce por grafo (SOLO_MESA): v2 3/20/7/10, v3 4/17/7/12, run_3 2/13/17/8
(correcto/parcial/incorrecto/req.adj.) — coincide con la tabla de mesa del §7.

- **A. Pares con final `requiere_adjudicacion`: 30** = 21 heredados de la base
  (7/8/6 por grafo; la ficha lleva la respuesta base) + 9 pendientes del §7
  (3/4/2; una ficha por cada re-corrida con veredicto `requiere_adjudicacion`:
  17 votos → **15 fichas**, porque en 2 pares dos re-corridas tienen texto
  idéntico y comparten ficha; la adjudicación se aplica a ambas). Los 24 votos
  `requiere_adjudicacion` de las 198 respuestas del §7 se descomponen en 17
  dentro de los 9 pendientes + 7 dentro de pares ya decididos por invariancia,
  que no requieren adjudicación.
- **B. Muestra simétrica §6: 12** = ceil(10 %) de los `correcto` por grafo
  (3/4/2 → 1/1/1) + ceil(10 %) de los `parcial`+`incorrecto` (27/24/30 → 3/3/3),
  `random.Random("adjudicacion-ev2-v1").sample` sobre ids de pregunta ORDENADOS,
  generador nuevo por (grafo, estrato) (mismo patrón que la auditoría §7). Par
  re-corrido → la ficha lleva la re-corrida de menor rep cuyo veredicto coincide
  con el final; par no re-corrido → la respuesta base.

**48 fichas** (21 + 15 + 3 + 9), 200 criterios a marcar. Orden
`random.Random("worksheet-ev2-v1").shuffle` sobre (id_pregunta, sha256 respuesta)
ordenados; id de ficha `ADJ-` + sha256(`worksheet-ev2-v1|id_pregunta|sha256(respuesta)`)[:8].

## Ceguera

La ficha contiene: número, id opaco, TO y ancla del gold, pregunta, respuesta
COMPLETA, criterios con cita textual, y el espacio de marcas. NUNCA grafo,
label, rep, veredicto o fragmentos del juez, ids EV2R-/EV2E-/EV2F-. El selftest
verifica 0 marcadores (incluidos los 318 sufijos hex de todos los ids opacos y
los 40 ids de pregunta) y la integridad contra tabla y gold. La tabla ficha →
(par, respuesta, origen, veredictos del juez) vive en `adjudicacion_SOLO_MESA/`.

## Cierre

`code/cerrar_adjudicacion.py --worksheet <worksheet completado .json>`:
valida (ids, sha256 de cada respuesta, n de criterios, marcas ∈ {cumplido,
no_cumplido}), aplica el mapping §2 por ficha, resuelve los votos pendientes
de los pares §7 con `agregar_par` (tolera faltantes por invariancia), y emite
`adjudicacion/veredictos_definitivos_ciego.{json,md}`,
`adjudicacion/reporte_muestra_simetrica.{json,md}` (dirección A: juez
correcto / humana no; dirección B: juez parcial-incorrecto / humana correcto;
desacuerdo de grado; acuerdo por criterio) y
`adjudicacion_SOLO_MESA/cruce_definitivo_por_grafo_SOLO_MESA.{json,md}`.
La muestra §6 mide la tasa de error del juez y NO reemplaza su veredicto en
esos pares (cambiarlo requiere laudo). Tests: `code/tests_cerrar.py` (31
checks sintéticos).

## Archivos

- `code/comun_adj.py` — insumos, finales por par, población A, muestra B, fichas, render, marcadores.
- `code/construir_worksheet.py` → `adjudicacion/worksheet_adjudicacion.{json,md}`,
  `adjudicacion/censo_worksheet_ciego.md`, `adjudicacion_SOLO_MESA/{tabla_fichas,poblacion_adjudicacion}_SOLO_MESA.json`,
  `adjudicacion_SOLO_MESA/resumen_poblacion_SOLO_MESA.md`.
- `code/cerrar_adjudicacion.py` + `code/tests_cerrar.py`.
- `code/selftest_nofuga.py` → `selftest_out/` (gitignorado), 40 checks.
- `checkpoint_sesion.md` — estado de la unidad.

## Reproducción (offline, USD 0)

```
.venv/bin/python -B data/experiment/ev2_adjudicacion/code/construir_worksheet.py
.venv/bin/python -B data/experiment/ev2_adjudicacion/code/tests_cerrar.py
.venv/bin/python -B data/experiment/ev2_adjudicacion/code/selftest_nofuga.py
```
