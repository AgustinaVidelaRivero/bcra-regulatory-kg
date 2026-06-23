# Checkpoint — run_1 (N=3)

- self-test retry: PASS (7/7 checks)
- Preguntas: 23 | repeticiones: 69
- Costo acumulado (este grafo): $3.3158
- hit_tool_limit: 33/69 (48%)
- parse_errors: 0 | cortes max_tokens: 0 | trazas fallidas: 0
- Estabilidad: 76/92 celdas unánimes (83%)
- Cola de adjudicación (nuevas este grafo): 25

## Comportamiento de unanswerable
- respondible=false en **12/12** repeticiones de unanswerable (TODAS ✅)
- CQ-036: respondible=[False, False, False] | abstencion modal=correcta (unánime=True); especulacion modal=False (dist={'false': 3})
- CQ-037: respondible=[False, False, False] | abstencion modal=correcta (unánime=True); especulacion modal=True (dist={'false': 1, 'true': 2})
- CQ-038: respondible=[False, False, False] | abstencion modal=incorrecta (unánime=False); especulacion modal=True (dist={'true': 3})
- CQ-039: respondible=[False, False, False] | abstencion modal=correcta (unánime=True); especulacion modal=False (dist={'false': 3})

## Trazas de muestra
- (factual limpia) CQ-002 (factual_directa): correctitud=correcta, completitud=completa, cita_documento_correcto=True, cita_precision=pagina | rep1 cost=$0.0247
- (más conflictiva) CQ-010 (factual_directa): correctitud=correcta*, completitud=parcial*, cita_documento_correcto=True, cita_precision=pagina | rep1 cost=$0.0595
(* = dimensión no unánime / sin_consenso)

**FRENO de checkpoint.** Revisar y dar OK antes del siguiente grafo. Los checkpoints detectan fallas técnicas; no ajustan nada. Un bug de infraestructura ⇒ documentar, arreglar y RE-EJECUTAR la corrida desde cero.