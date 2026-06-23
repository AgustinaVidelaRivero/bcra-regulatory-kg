# Checkpoint — run_3 (N=3)

- self-test retry: PASS (7/7 checks)
- Preguntas: 23 | repeticiones: 69
- Costo acumulado (este grafo): $3.2106
- hit_tool_limit: 26/69 (38%)
- parse_errors: 0 | cortes max_tokens: 0 | trazas fallidas: 0
- Estabilidad: 86/92 celdas unánimes (93%)
- Cola de adjudicación (nuevas este grafo): 18

## Comportamiento de unanswerable
- respondible=false en **12/12** repeticiones de unanswerable (TODAS ✅)
- CQ-036: respondible=[False, False, False] | abstencion modal=correcta (unánime=True); especulacion modal=True (dist={'false': 1, 'true': 2})
- CQ-037: respondible=[False, False, False] | abstencion modal=correcta (unánime=True); especulacion modal=False (dist={'false': 3})
- CQ-038: respondible=[False, False, False] | abstencion modal=correcta (unánime=True); especulacion modal=True (dist={'true': 3})
- CQ-039: respondible=[False, False, False] | abstencion modal=correcta (unánime=True); especulacion modal=False (dist={'false': 3})

## Trazas de muestra
- (factual limpia) CQ-002 (factual_directa): correctitud=correcta, completitud=completa, cita_documento_correcto=True, cita_precision=pagina | rep1 cost=$0.0270
- (más conflictiva) CQ-020 (multi_norma): correctitud=correcta*, completitud=completa, cita_documento_correcto=True*, cita_precision=punto | rep1 cost=$0.0806
(* = dimensión no unánime / sin_consenso)

**FRENO de checkpoint.** Revisar y dar OK antes del siguiente grafo. Los checkpoints detectan fallas técnicas; no ajustan nada. Un bug de infraestructura ⇒ documentar, arreglar y RE-EJECUTAR la corrida desde cero.