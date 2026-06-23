# Smoke del pipeline de corrida congelada

2 preguntas del dev_pool (CQ-023 answerable+adjudicación, dev_unans_1 unanswerable) × run_3 × N=2. Valida repeticiones, agregación modal, checkpoint, política de errores, cola de adjudicación y ceguera del juez. **NO toca el eval_set.**

## Agregación modal (N=2)

| qid | categoria | dimensión | modal | unánime | distribución |
|-----|-----------|-----------|-------|:-------:|--------------|
| CQ-023 | multi_norma | correctitud | correcta | ✅ | {'"correcta"': 2} |
| CQ-023 | multi_norma | completitud | sin_consenso | ⚠ sin_consenso | {'"completa"': 1, '"parcial"': 1} |
| CQ-023 | multi_norma | cita_documento_correcto | True | ✅ | {'true': 2} |
| CQ-023 | multi_norma | cita_precision | punto | ✅ | {'"punto"': 2} |
| dev_unans_1 | unanswerable | cita_documento_correcto | False | ✅ | {'false': 2} |
| dev_unans_1 | unanswerable | cita_precision | ausente | ✅ | {'"ausente"': 2} |
| dev_unans_1 | unanswerable | abstencion | correcta | ✅ | {'"correcta"': 2} |
| dev_unans_1 | unanswerable | especulacion_en_prosa | sin_consenso | ⚠ sin_consenso | {'false': 1, 'true': 1} |

> Con N=2, cualquier desacuerdo entre las 2 reps marca la dimensión `sin_consenso` (empate modal 1-1). Es esperado en preguntas de frontera.

## Ceguera del juez — auditoría

Payloads del juez auditados: **8** (2 por traza: Paso 1 + Paso 2). Claves de top-level expuestas al juez: `campos_automaticos, categoria, citas_agente, descomposicion, pregunta, referente, respondible, respuesta_agente, respuesta_cruda`.

- ✅ **Sin fugas de identidad de run**: no aparece ningún run_key (run_1..5), nombre de grafo (cookbook/papers/ppf_core/schema_light/hybrid), path (kg.json/source_kg/data\_experiment/frozen) ni prefijo de id de nodo (Obligacion_/ope_/con_/…) en ningún payload.

Lo único que el juez ve y correlaciona con el grafo es **contenido legítimo bajo evaluación**: la prosa de la respuesta, y las citas (`source_doc` = nombre de PDF, COMPARTIDO por los 5 grafos; `location` con su granularidad, que el juez NECESITA para puntuar `cita_precision`). No hay etiqueta ni metadata que identifique el run.

## Cola de adjudicación

2 entrada(s) en `adjudicacion_pendiente_SMOKE.json`. Ejemplo:
- CQ-023 rep1: 6 afirmación(es) central(es) no soportada(s); citas=[{'source_doc': 'TO_regimen_informativo_contable_mensual_actual.pdf', 'location': 'Punto 6.3. Límites mínimos:'}, {'source_doc': 'TO_capitales_minimos_actual.pdf', 'location': 'Punto 1.3. Integración.'}]

## Política de errores (verificada)

- Retries de infraestructura logueados: 0 eventos (ver `retries.jsonl`). 0 = no hubo errores de infra en el smoke.
- parse_errors: 0 | cortes max_tokens: 0 (no se reintentan: comportamiento del sistema).

## Costo del smoke
- Total: **$0.2506** (4 repeticiones).
