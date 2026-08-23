# ev2_r1 — U-B1.8: fidelidad EV2 de KG-Reextraído-r1 (plan v7, issue #16)

Única medición de KG-Reextraído-r1
(`data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`, sha256
`0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a`) sobre el
eje de fidelidad de EV2 (40 preguntas / 164 criterios, set sellado `9c44516`),
con el instrumento sellado sin cambios y pre-registro propio sellado por
commit ANTES de la fase B. Rige el principio 7 (r1 se mide sobre EV2 una sola
vez) y el principio 9 (nada de lo que falle se corrige en r1: va a la release
r2). Vinculantes: `preregistro_ev2_r1.md` (esta unidad),
`docs/protocolo_corrida_ev2.md`, `docs/preregistro_evaluacion_fidelidad_ev2.md`,
`data/experiment/ev2_reporte/regla_atribucion.md`.

Nada fuera de este directorio se edita: los módulos sellados de EV2
(`ev2_corrida`, `ev2_fidelidad_eval`, `ev2_encadenamiento`, `ev2_juez`,
cuarteto de `evaluacion/`) se IMPORTAN; la extensión a r1 es un registro en
memoria (`code/comun_r1.py`), con sha verificados al inicio y al cierre de
cada etapa (`sellos/`).

## Archivos

- `preregistro_ev2_r1.md` — pre-registro de la unidad (P1–P5, semillas,
  labels, ids opacos, costos, formato de lectura). Sellado por commit de la
  autora antes de la fase B.
- `code/comun_r1.py` — registro en memoria de r1 + adaptador de provenance
  (el de la vista v2 de la corrida base), orden (`orden-ev2-r1`), sellos,
  ids opacos y labels.
- `code/censo_r1.py` — fase A: censo de las 40 anclas sobre r1 (regla sellada
  + columnas informativas H24) → `censo/`.
- `code/selftest_r1.py` — fase A: selftest offline del circuito ($0) →
  `selftest_out/` (gitignorado).
- `code/estimacion_r1.py` — fase A: estimación de fase B desde archivos
  sellados → `estimacion/`.
- `code/runner_r1.py` — fase B (gateada): agente N=1 sobre las 40 →
  `trazas/ev2_r1_base/`.
- Los módulos de juez N=3, encadenamiento §7, worksheet ciego y cierre
  (tabla final + atribución A0.2 + lectura P1–P5) se agregan en la fase B,
  envolviendo el pipeline sellado, cada uno con selftest previo al gasto.

## Reproducción (fase A, offline, USD 0)

```
.venv/bin/python -B data/experiment/ev2_r1/code/selftest_r1.py
.venv/bin/python -B data/experiment/ev2_r1/code/censo_r1.py
.venv/bin/python -B data/experiment/ev2_r1/code/estimacion_r1.py
```

Fase B solo tras el sello del pre-registro y con autorización explícita con
tope (ver gating en cada módulo).
