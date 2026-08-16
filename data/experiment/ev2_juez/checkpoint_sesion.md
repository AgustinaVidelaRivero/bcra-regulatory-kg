# checkpoint_sesion — construcción y calibración del juez de fidelidad EV2

Estado al momento de la primera llamada a la API (etapa 3 autorizada).

## Hecho y aprobado
- Etapa 1 (inventario, FRENO 1): U6 = 25 preguntas (`exploracion/generacion/preguntas_u6.json`),
  25 respuestas (`evaluacion/posthoc_run/traces/u6_exploracion/reensamblado_v3/`),
  adjudicación humana 7/15/3 (`exploracion/adjudicacion/u6_adjudicacion_humana.jsonl`).
  Carencia de criterios resuelta por opción A: criterios sellados en commit `2ac2fab`
  (`exploracion/u6_fidelidad/criterios_u6.json`, sha256 `b8d65789…`, 25/92).
- Etapa 2 (FRENO 2/2b): juez v1 en `data/experiment/ev2_juez/` — prompt con prohibición
  (sha256 `fd446f8e61f4…`), `juez.py`, `mapping.py` (+20 tests PASS), `driver_calibracion.py`
  (ciego al veredicto humano, semilla `juez-calibracion-v1`), `selftest.py` 32/32 PASS,
  `verificar_citas.py` (90/92 lineal + 2/2 tabular por Laudo D = 92/92), estimación
  ~126.8k in / ~27.8k out.
- Autorización etapa 3: precios in 3.00 / out 15.00 USD/MTok; estimación ~0,80; TOPE 1,50
  con freno por proyección.

## En curso
- Corrida `correr_calibracion.py` (wrapper con freno por proyección) → `out/veredictos_r{1,2,3}.jsonl`
  + `out/veredictos_agregados.json`; dbs `cache/juez_calibracion_r{1,2,3}.db`.
- Después: `analisis_acuerdo.py` (acuerdo juez-humana + clasificación de desacuerdos) → FRENO 3.

## Reglas vivas
- Cero commits; nada fuera de `data/experiment/ev2_juez/`; cuarteto intocable;
  NUNCA ajustar el prompt; material EV2 no se abre.

## Etapa 3 — estado al FRENO 3 (2026-08-16)
- Pasada 1 corrida: 75/75 llamadas, USD 1,0262 (dbs `cache/juez_calibracion_r{1,2,3}.db`),
  0 cross-hits, 86/92 pares unánimes; salidas en `out/`.
- HALLAZGO: la pasada juzgó las trazas B2, no las respuestas adjudicadas (sesión app);
  4/25 idénticas. Ver `out/NOTA_fuente_respuestas_pasada1.md`. Comparación válida solo en
  U6-004 (correcto→incorrecto), U6-006 (acuerdo), U6-014 (acuerdo), U6-017 (correcto→parcial).
- Hallazgo del instrumento: U6-001 c3 — fragmento copiado del gold en 3/3 reps (fuga de evidencia).
- Preparado sin correr: `--fuente-respuestas app` (25/25 offline). Re-pasada requiere autorización
  nueva (excede tope 1,50 acumulado). NO se tocó el prompt.

## Etapa 3b — estado al FRENO 3b (2026-08-16)
- Pasada 2 (fuente app, prompt v1 intacto sha fd446f8e…): 75/75, USD 1,0101, 0 cross-hits,
  dbs `cache_app/juez_calibracion_app_r{1,2,3}.db`, salidas `out_app/`.
- Acuerdo 14/25, desacuerdo 6, requiere_adjudicacion 5 (`out_app/acuerdo_juez_humana.json`,
  `reporte_desacuerdos.md`, `clasificacion_desacuerdos_lectura.md`).
- Los 6 desacuerdos son de etiqueta (5/6 = criterios no preguntados / matiz de cierre; U6-009
  granularidad de c1). Fuga real de gold: 1/276 (U6-001 c3 r2). NO se tocó el prompt.
- Gasto acumulado de la unidad: 1,0262 + 1,0101 = USD 2,0363.

## Etapa 4 — laudos post-3b, estado al FRENO 4 (2026-08-16)
- `calibracion/registro_calibracion.md` redactado (brecha de vara declarada, no aplicable a EV2,
  limitación U6-010).
- v1.1 = v1 + calibrador 1 (`prompt_juez_v1_1.md`, sha 6c3f1cb38542e4da…; v1 intacto fd446f8e…).
  Re-corrida `out_app_v11/` + `cache_app_v11/`: 75/75, USD 1,1461, 0 cross-hits.
- Aceptación NO cumplida: fuga eliminada (U6-001 c3 nc×3/null×3) PERO 3/91 pares cambian modal
  (U6-004 c1 nc→c; U6-011 c2 dudoso→nc; U6-019 c2 dudoso→c borde de ruido). NADA congelado; laudo pendiente.
- Gasto acumulado unidad: 1,0262 + 1,0101 + 1,1461 = USD 3,1824.

## CIERRE — laudo final (2026-08-16)
- CONGELADO prompt v1 (sha fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455).
- v1.1 descartada (rotulada; sha de corrida 6c3f1cb3… en meta de out_app_v11).
- registro_calibracion.md cerrado (§8). Calibración CERRADA. EV2 = unidad nueva.
- Gasto total unidad: USD 3,1824 (pasadas: 1,0262 B2-no-válida / 1,0101 v1-app / 1,1461 v1.1-descartada).
