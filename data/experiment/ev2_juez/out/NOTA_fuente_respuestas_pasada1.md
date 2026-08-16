# NOTA — pasada 1 de calibración (out/): fuente de respuestas INCORRECTA para comparar con la adjudicación

Esta pasada (75 llamadas, USD 1,0262, `resumen_corrida.json`) juzgó las
respuestas de las TRAZAS `posthoc_run/traces/u6_exploracion/reensamblado_v3/`
(corrida apareada B2 del agente sobre las 25 preguntas de U6).

La adjudicación humana sellada (`u6_adjudicacion_humana.jsonl`, commit b337152)
se hizo sobre las respuestas de la SESIÓN DE LA APP
`app/sessions/local/09beef6a-a147-4417-8a53-cea3da678930.jsonl` (laudo №0 de
`laudos_sellado_u6.md`: "las 25 preguntas corrieron en una única sesión de la
app local"; "el apareamiento con la corrida B2 queda preservado" — B2 es OTRA
corrida). Comparación texto a texto: **4/25 respuestas idénticas**
(U6-004, U6-006, U6-014, U6-017); **21/25 distintas**.

Consecuencias:
- `acuerdo_juez_humana.json` y `reporte_desacuerdos.md` de esta pasada NO son
  evidencia de calibración salvo para las 4 preguntas idénticas.
- Siguen siendo válidos como hechos sobre el instrumento: costo real,
  0 cross-hits, distribución de las 3 reps, no-determinismo por par (86/92
  unánimes), comportamiento de fragmentos (1 par de 92 con fragmento copiado
  del gold: U6-001 c3, 3/3 reps).
- El error es de la etapa 1 (inventario): identifiqué las trazas como "las
  respuestas adjudicadas" sin cotejarlas contra la fuente que la planilla
  declara. El mapeo confirmado en FRENO 1 heredó ese error.

Fuente correcta para calibrar: `driver_calibracion.py --fuente-respuestas app`
(carga verificada offline 25/25, apareamiento por texto exacto de la pregunta).
Ninguna llamada nueva a la API se hizo: excede el tope autorizado y requiere
autorización nueva.
