# A/B de prompt caching (multi-turn) — harness KG-RAG

6 preguntas del dev_pool sobre Run 3, SIN cache vs CON cache (cache_control móvil en el último bloque de usuario; ámbito INTRA-pregunta). Respondedor `claude-haiku-4-5-20251001`, temp 0. Juez de equivalencia: v2.1.1 CONGELADO.

**Equivalencia: ❌ NO pasa** (parse + respondible + citas post-norm + veredictos del juez idénticos).

## Equivalencia por pregunta

| qid | parse | respondible | citas (post-norm) | juez idéntico | diffs |
|-----|:-----:|:-----------:|:-----------------:|:-------------:|-------|
| CQ-001 | ✅ | ✅ | ✅ | ✅ | — |
| CQ-009 | ✅ | ✅ | ❌ | ❌ | correctitud, completitud, requiere_adjudicacion_humana |
| CQ-023 | ✅ | ✅ | ✅ | ❌ | completitud |
| CQ-029 | ✅ | ✅ | ✅ | ❌ | correctitud |
| CQ-032 | ✅ | ✅ | ✅ | ✅ | — |
| dev_unans_1 | ✅ | ✅ | ✅ | ✅ | — |

## Economía del cache (medida, no asumida)

La escritura de cache cuesta 1,25× y la lectura 0,1×. El costo `on` ya incluye el premium de escritura. Las preguntas cortas (pocas tools) pueden no ahorrar; la ganancia está en las largas.

| qid | tools | tok_in off | tok_in on | cache_creation | cache_read | costo off | costo on | Δ% |
|-----|------:|-----------:|----------:|---------------:|-----------:|----------:|---------:|----:|
| CQ-001 | 3 | 10179 | 1481 | 4531 | 4167 | $0.01274 | $0.01007 | +21.0% |
| CQ-009 | 15 | 94423 | 10175 | 11372 | 65242 | $0.10253 | $0.03916 | +61.8% |
| CQ-023 | 15 | 57964 | 5511 | 15083 | 52731 | $0.06679 | $0.03874 | +42.0% |
| CQ-029 | 9 | 56791 | 5486 | 10973 | 40485 | $0.06341 | $0.02979 | +53.0% |
| CQ-032 | 5 | 11920 | 1503 | 5511 | 4906 | $0.01521 | $0.01217 | +20.0% |
| dev_unans_1 | 15 | 91885 | 5458 | 18543 | 87984 | $0.10100 | $0.04639 | +54.1% |
| **TOTAL** | | 323162 | 29614 | 66013 | 255515 | **$0.36169** | **$0.17633** | **+51.2%** |

**Factor de ahorro neto: 2.05×** (costo sin cache / costo con cache, sobre las 6 preguntas).

**Ámbito declarado:** el ahorro es INTRA-pregunta. El prefijo compartido entre preguntas distintas (system+tools, ~1.433 tok) está por debajo del mínimo cacheable de Haiku 4.5 (4.096 tok), por lo que el cache NO se comparte entre preguntas: cada pregunta arranca conversación nueva y solo reutiliza el cache dentro de su propio loop de tools.
