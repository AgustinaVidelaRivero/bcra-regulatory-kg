# ev2_reporte — reporte consolidado de EV2 + atribución determinística de fallas (U-A0)

Unidad U-A0 (plan de tesis §4, unidad 1): sub-tareas **A0.1** (reporte
consolidado) y **A0.2** (atribución de fallas por traza). USD 0, sin API,
determinística. Insumos: SOLO archivos commiteados de las unidades EV2
(`ev2_corrida`, `ev2_fidelidad_eval`, `ev2_encadenamiento`, `ev2_adjudicacion`,
`ev2_juez`, `exploracion/ev2_fidelidad`), leídos o importados, jamás editados.
Nomenclatura canónica de `docs/nomenclatura_grafos.md`: KG-Base (`12c226e2`,
`run_3`) / KG-Refinado (`26fac8b4`, `v3`) / KG-Reextraído (`8e2eadee`, `v2`).

## Archivos

- `reporte_ev2.md` — **A0.1**: tabla definitiva de fidelidad con vías,
  cobertura por criterios recomputada, navegabilidad con denominadores por
  grafo, censo y diagnóstico de ausencias, validación del juez, salvedades
  (a)–(d), desvíos del período, costos por archivo, propuesta de cierre del
  issue #10.
- `code/comun_reporte.py` — rutas de insumos, sha256 esperados (insumos ya
  sellados por otras unidades + cuarteto), cargadores.
- `code/recomputo_ev2.py` → `salida/recomputo_ev2.json` (todos los números
  del reporte, con la ruta del insumo por bloque) + `salida/tablas_ev2.md`
  (tablas largas: definitivo por par, perfil por pregunta, cobertura por par,
  diagnóstico de ausencias por ancla).
- `regla_atribucion.md` — **A0.2 Fase A**: definiciones operativas exactas de
  las cuatro clases (ausencia_kg / alcanzabilidad / vista_no_consultada /
  generacion), precedencia, campos de traza, ancla primaria, columna cruzada
  abstención/contenido, población base (120) y opcional §7 (198). RATIFICADA
  y sellada en el commit `40603a9`.
- `code/atribucion_fallas.py` — módulo que implementa la regla importando el
  replay/métrica de `ev2_corrida` y `exploracion/sinteticas` (sin copiar):
  `--selftest` (sintético, 24 checks → `selftest_out/`, gitignorado),
  `--verificar-estructura` (conteos de veredictos por respuesta, sin abrir
  trazas), `--correr [--incluir-enc] [--sensibilidad-descendientes]` (Fase B;
  **se niega a correr si `regla_atribucion.md` no tiene commit**) →
  `salida/atribucion_fallas.{json,md}` (clase × grafo × veredicto, cruces con
  auxiliar/respondible/criterios no cumplidos, pares definitivos con traza
  representativa, censo de las 40 anclas de fidelidad, sensibilidad
  informativa, hallazgos H1–H7) + `salida/atribucion_por_traza.md` (311 filas).
  `--sensibilidad-descendientes` es INFORMATIVO, fuera de la regla ratificada.
- `code/hallazgos_atribucion_texto.md` — texto fijo de los hallazgos que
  `render_md` incluye en `salida/atribucion_fallas.md` (§5).

## Reproducción (USD 0)

```
python3 -B data/experiment/ev2_reporte/code/recomputo_ev2.py
.venv/bin/python -B data/experiment/ev2_reporte/code/atribucion_fallas.py --selftest
.venv/bin/python -B data/experiment/ev2_reporte/code/atribucion_fallas.py --verificar-estructura
```

Fase B (corrida tras el commit del laudo `40603a9`; doble corrida byte-idéntica salvo `generado`):

```
.venv/bin/python -B data/experiment/ev2_reporte/code/atribucion_fallas.py --correr --incluir-enc --sensibilidad-descendientes
```
