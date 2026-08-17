# checkpoint — ev2_adjudicacion (worksheet ciego §6 + resolución de pendientes §7)

## Estado: worksheet CONSTRUIDO, adjudicación humana PENDIENTE (frenado para revisión)

Fecha: 2026-08-16. Gasto: USD 0 (offline). Sin commits (los hace la autora).

## Hecho

- `code/construir_worksheet.py`: población A (30 pares: 21 heredados + 9 pendientes §7)
  y muestra B (12) derivadas de los archivos commiteados; tabla final por grafo
  verificada contra la esperada (v2 3/20/7/10, v3 4/17/7/12, run_3 2/13/17/8);
  48 fichas ciegas en `adjudicacion/worksheet_adjudicacion.{json,md}`; tabla
  ficha → par en `adjudicacion_SOLO_MESA/`.
- `code/cerrar_adjudicacion.py`: cierre (mapping §2 + agregar_par) con tests
  sintéticos 31/31 (`code/tests_cerrar.py`); corrida en seco sobre el worksheet
  vacío reproduce la tabla pre-adjudicación (salidas en scratchpad, no en repo).
- `code/selftest_nofuga.py`: 40/40 checks (0 marcadores, integridad, orden,
  población).

## Desvíos respecto del mandato (reportados)

- Votos `requiere_adjudicacion` dentro de los 9 pendientes §7: 17, no 24. Los 24
  del mandato son el total de respuestas §7 con ese veredicto (17 en pendientes
  + 7 en pares decididos por invariancia, que no requieren adjudicación).
- Textos idénticos entre re-corridas de un mismo par comparten ficha (2 casos:
  17 votos → 15 fichas). Decisión de esta unidad, sujeta a ratificación.

## Decisiones de mesa a ratificar

1. Muestra B: generador nuevo por (grafo, estrato) sobre ids de pregunta ordenados.
2. Respuesta de la ficha para pares re-corridos muestreados: menor rep cuyo
   veredicto coincide con el final (incluye pares de auditoría §7).
3. Fichas compartidas por textos idénticos (arriba).
4. La muestra §6 no reemplaza el veredicto del juez en esos pares.
5. Un heredado adjudicado como `parcial` NO dispara re-corridas §3 desde esta
   unidad (el disparador §3 se aplicó sobre la corrida base; extenderlo requiere laudo).

## Próximo paso

La autora completa `worksheet_adjudicacion.json` (campo `veredicto` de cada
criterio) → `code/cerrar_adjudicacion.py --worksheet <completado>` → revisión.
