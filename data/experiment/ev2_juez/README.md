# ev2_juez — Juez de fidelidad de EV2 (construcción y calibración)

Instrumento del eje de fidelidad de EV2, según el pre-registro VINCULANTE
`docs/preregistro_evaluacion_fidelidad_ev2.md` (sellado en commit `be8a84f`).
El `judge.py` del cuarteto sellado de `data/experiment/evaluacion/` es OTRO
instrumento (juez de la Fase 2.3): no se toca ni se reutiliza su prompt.

## Piezas

- `prompt_juez_v1.md` — prompt del juez, con la prohibición de modificación
  sin laudo escrita desde v1. Congelamiento por sha256 antes de tocar EV2.
- `juez.py` — request (pregunta + respuesta + criterios con cita, nada más),
  cliente `CachingClient` (una db por repetición, namespace por repetición),
  parseo estricto del veredicto. Modelo: `claude-sonnet-4-6`.
- `mapping.py` + `tests_mapping.py` — agregación modal (§4) y veredicto por
  pregunta (§2) EN CÓDIGO, con tests de respuesta conocida.
- `driver_calibracion.py` — corrida N=3 sobre los 25 casos de U6, orden
  aleatorizado semilla `juez-calibracion-v1`, persistencia write-through,
  verificación de 0 cross-hits. CIEGO al veredicto humano: no existe parámetro
  para la adjudicación.
- `conversor_criterios.py` — tabla de la autora (id | criterio | cita_textual)
  → `calibracion/criterios_u6.json` (esquema fijo) + verificación verbatim de
  cada cita contra el PDF del TO (pdfplumber, normalización solo-whitespace).
- `selftest.py` — selftest offline con cliente falso (persistencia, dbs
  separadas, mapping sobre veredictos scripteados, ceguera estructural).
- `estimacion.py` — costo parametrizado de una pasada (25×3); precios SOLO
  como variables de CLI, nunca hardcodeados.
- `calibracion/` — insumos y registro de la redacción de criterios (autora).
- `cache/`, `selftest_out/` — locales, gitignorados acá.

## Correr (offline, $0)

```
.venv/bin/python data/experiment/ev2_juez/tests_mapping.py
.venv/bin/python data/experiment/ev2_juez/selftest.py
.venv/bin/python data/experiment/ev2_juez/estimacion.py
```

La pasada real (`driver_calibracion.py --criterios …`) exige autorización
previa con precios y tope; el cómputo de acuerdo juez-humana vive en un paso
posterior separado del driver (el juez jamás ve la adjudicación).
