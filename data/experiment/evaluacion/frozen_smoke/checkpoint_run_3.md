# Checkpoint — run_3 (N=2)

- Preguntas: 2 | repeticiones: 4
- Costo acumulado (este grafo): $0.2506
- hit_tool_limit: 3/4 (75%)
- parse_errors: 0 | cortes max_tokens: 0 | trazas fallidas: 0
- Estabilidad: 6/8 celdas unánimes (75%)
- Cola de adjudicación (nuevas este grafo): 2

## Comportamiento de unanswerable
- dev_unans_1: abstencion modal=correcta (unánime=True); especulacion modal=sin_consenso (dist={'false': 1, 'true': 1})

## Trazas de muestra (1-2)
- CQ-023 (multi_norma): correctitud=correcta, completitud=sin_consenso, cita_documento_correcto=True, cita_precision=punto | rep1 cost=$0.0717
- dev_unans_1 (unanswerable): cita_documento_correcto=False, cita_precision=ausente, abstencion=correcta, especulacion_en_prosa=sin_consenso | rep1 cost=$0.0563

**FRENO de checkpoint.** Revisar y dar OK antes del siguiente grafo. Los checkpoints detectan fallas técnicas; no ajustan nada. Un bug de infraestructura ⇒ documentar, arreglar y RE-EJECUTAR la corrida desde cero.