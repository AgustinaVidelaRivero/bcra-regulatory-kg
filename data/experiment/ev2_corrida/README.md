# ev2_corrida — corrida del agente EV2 sobre tres grafos (issue #10)

Protocolo vinculante: `docs/protocolo_corrida_ev2.md` (sellado en
`data/experiment/exploracion/ev2_sellado/manifest_ev2.txt`). El cuarteto de
`data/experiment/evaluacion/` (loader/harness/judge/llm_cache) se importa y
envuelve; jamás se edita. El set sellado es de solo lectura.

## Fase A (offline, USD 0) — contenido

- `code/comun_ev2.py` — rutas + sha256 de los 3 grafos (verificación
  obligatoria), vistas de censo y runtime por grafo (adaptadores de
  provenance documentados en el docstring: v2 `{to, archivo, punto}` →
  `{source_doc, location}`), set sellado, orden `orden-ev2-v1`.
- `code/censo_ev2.py` → `censo/censo_navegabilidad_{v2,v3,run_3}.json`,
  `censo/censo_resumen.json`, `censo/ausencias_diagnostico.json` — censo
  previo por grafo del eje sintético (regla sellada de `resolucion.py`:
  match exacto de punto, contenedores >10 anclas excluidos).
- `code/orden_ev2.py` → `orden/orden_ev2_resuelto.json` — 168 casos
  (40 fidelidad + 128 navegabilidad) ordenados por id y barajados con
  `random.Random("orden-ev2-v1")`; por grafo se saltean las ausencias del
  censo sin re-barajar.
- `code/runner_ev2.py` — runner de la corrida (fase B, gateado por
  `--autorizado-fase-b` + `EV2_TOPE_USD`): por caso persiste traza del
  harness + `steps_full` (outputs de tool íntegros) + `raw_turns_agent`
  (crudos API vía caché) + metadata. Una db por corrida-grafo
  (`cache/ev2_base_{v2,v3,run3}.db`, gitignoradas). Fidelidad se persiste
  SIN evaluar (ningún juez en esta unidad). Freno por proyección contra el
  tope global.
- `code/metrica_ev2.py` — métrica determinística de navegabilidad por
  replay (visto / consultado / brecha), envolviendo `metrica.py` de
  sintéticas + replay fuerte contra `steps_full`.
- `code/selftest_ev2.py` — selftest offline de punta a punta (cliente falso,
  2 casos por eje, 17 checks): persistencia completa, cero juez, replay
  100% hits, métrica auto-verificada. Escribe en `selftest_out/`
  (gitignorado).
- `code/estimacion_ev2.py` → `estimacion/estimacion_fase_b.{json,md}` —
  conteo de corridas con ausencias descontadas + tokens por corrida de
  corridas históricas citadas + fórmula con precios como variables
  (P_in, P_out, P_cache_write, P_cache_read). Sin precios.

## Reproducción

```
cd data/experiment/ev2_corrida/code
python3 -B censo_ev2.py
python3 -B orden_ev2.py
../../../../.venv/bin/python -B selftest_ev2.py
python3 -B estimacion_ev2.py
```

La fase B (gasto real) requiere autorización con precios y tope resueltos;
sin `--autorizado-fase-b` y `EV2_TOPE_USD` el runner aborta.
