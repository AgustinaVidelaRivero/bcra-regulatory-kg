# Control de no-determinismo (off-vs-off2) — A/B de caching

Las 3 preguntas que divergieron en off-vs-on, corridas dos veces más ambas SIN cache. Si off-vs-off2 también diverge, la inestabilidad es de la pregunta (no-determinismo a temp 0), no del cache.

**n=3: control de cordura, no test estadístico.** El argumento estructural (cache_control es metadata, no cambia la salida del modelo) hace baja la carga de la prueba.

**Veredicto: ⚠ Alguna pregunta es estable off-vs-off2 pero divergió off-vs-on → investigar antes de congelar.**

## Comparación lado a lado

| qid | off-vs-on (A/B) | off-vs-off2 (control) | ¿inestable sin cache? |
|-----|-----------------|------------------------|:---------------------:|
| CQ-009 | citas≠; veredicto: correctitud, completitud, requiere_adjudicacion_humana | citas≠; veredicto: correctitud, completitud, requiere_adjudicacion_humana | ✅ sí |
| CQ-023 | veredicto: completitud | citas≠; veredicto: cita_documento_correcto | ✅ sí |
| CQ-029 | veredicto: correctitud | idéntico | ❌ no (estable) |

## Detalle de veredictos off-vs-off2

**CQ-009** — inestable=True
- correctitud: A=`correcta` vs B=`incorrecta`
- completitud: A=`completa` vs B=`parcial`
- requiere_adjudicacion_humana: A=`False` vs B=`True`
- citas A: [{'source_doc': 'TO_clasificacion_deudores_actual.pdf', 'location': 'Punto 4.1. Niveles de clasificación.'}]
- citas B: [{'source_doc': 'TO_clasificacion_deudores_actual.pdf', 'location': 'Punto 6.1. Información básica.'}]

**CQ-023** — inestable=True
- cita_documento_correcto: A=`False` vs B=`True`
- citas A: [{'source_doc': 'TO_regimen_informativo_contable_mensual_actual.pdf', 'location': 'Punto 6.3. Límites mínimos:'}]
- citas B: [{'source_doc': 'TO_capitales_minimos_actual.pdf', 'location': 'Punto 1.3. Integración.'}, {'source_doc': 'TO_regimen_informativo_contable_mensual_actual.pdf', 'location': 'Punto 6.3. Límites mínimos:'}]

**CQ-029** — inestable=False
