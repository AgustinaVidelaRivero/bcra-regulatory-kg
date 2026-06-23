# Reporte final (DRAFT — etapa 1) — corrida congelada Fase 2.3

eval_set_v1 (23 preguntas) × 5 grafos × N=3. Respondedor `claude-haiku-4-5-20251001` (caching ON), juez `claude-sonnet-4-6` v2.1.1, ambos congelados. Veredicto por celda = MODAL de 3 reps.

> ⚠️ **DRAFT de dos etapas.** REGLA: toda celda answerable con ≥1 afirmación CENTRAL no soportada (en la cola de adjudicación) tiene su **correctitud marcada `pendiente_adjudicacion`** — NO se emite veredicto final de correctitud sobre ella hasta que la autora adjudique contra los PDFs. Las demás dimensiones (completitud, citas, abstención) SÍ se reportan. La **etapa 2 (final)** se emite tras la adjudicación humana.

## 1. Resumen por grafo

| Grafo | Costo | Estabilidad (unánimes) | sin_consenso | hit_limit | Adj. (rep / preg.) | Celdas pendientes |
|-------|------:|-----------------------:|-------------:|----------:|-------------------:|------------------:|
| run_1 | $3.3158 | 76/92 (83%) | 0 | 33/69 (48%) | 25 / 10 | 8 |
| run_2 | $3.0084 | 78/92 (85%) | 0 | 26/69 (38%) | 22 / 10 | 8 |
| run_3 | $3.2106 | 86/92 (93%) | 0 | 26/69 (38%) | 18 / 9 | 7 |
| run_4 | $3.2664 | 79/92 (86%) | 1 | 34/69 (49%) | 11 / 6 | 6 |
| run_5 | $3.0119 | 79/92 (86%) | 0 | 34/69 (49%) | 14 / 7 | 6 |
| **TOTAL** | **$15.8132** | | | | 90 / — | |

## 2. Correctitud — grafo × categoría (answerable)

Conteo de celdas por veredicto modal. `pend` = correctitud retenida (pendiente de adjudicación). El veredicto de esas celdas NO es final.

| Grafo | Categoría | correcta | parcial | incorrecta | pend |
|-------|-----------|---------:|--------:|-----------:|-----:|
| run_1 | factual_directa | 7 | 0 | 1 | 2 |
| run_1 | multi_norma | 0 | 0 | 0 | 5 |
| run_1 | cadena_restriccion_excepcion | 0 | 0 | 3 | 1 |
| run_2 | factual_directa | 8 | 0 | 1 | 1 |
| run_2 | multi_norma | 0 | 0 | 0 | 5 |
| run_2 | cadena_restriccion_excepcion | 2 | 0 | 0 | 2 |
| run_3 | factual_directa | 9 | 0 | 1 | 0 |
| run_3 | multi_norma | 0 | 0 | 0 | 5 |
| run_3 | cadena_restriccion_excepcion | 2 | 0 | 0 | 2 |
| run_4 | factual_directa | 9 | 0 | 0 | 1 |
| run_4 | multi_norma | 1 | 0 | 0 | 4 |
| run_4 | cadena_restriccion_excepcion | 1 | 0 | 2 | 1 |
| run_5 | factual_directa | 7 | 0 | 2 | 1 |
| run_5 | multi_norma | 2 | 0 | 0 | 3 |
| run_5 | cadena_restriccion_excepcion | 2 | 0 | 0 | 2 |

## 3. Completitud — grafo × categoría (answerable)

| Grafo | Categoría | completa | parcial |
|-------|-----------|---------:|--------:|
| run_1 | factual_directa | 7 | 3 |
| run_1 | multi_norma | 5 | 0 |
| run_1 | cadena_restriccion_excepcion | 3 | 1 |
| run_2 | factual_directa | 9 | 1 |
| run_2 | multi_norma | 3 | 2 |
| run_2 | cadena_restriccion_excepcion | 1 | 3 |
| run_3 | factual_directa | 9 | 1 |
| run_3 | multi_norma | 4 | 1 |
| run_3 | cadena_restriccion_excepcion | 3 | 1 |
| run_4 | factual_directa | 8 | 2 |
| run_4 | multi_norma | 2 | 3 |
| run_4 | cadena_restriccion_excepcion | 1 | 3 |
| run_5 | factual_directa | 10 | 0 |
| run_5 | multi_norma | 4 | 1 |
| run_5 | cadena_restriccion_excepcion | 2 | 2 |

## 4. Unanswerable — abstención y especulación (4 preguntas × grafo)

| Grafo | abst. correcta | abst. incorrecta | espec. True | espec. False |
|-------|---------------:|-----------------:|------------:|-------------:|
| run_1 | 3 | 1 | 2 | 2 |
| run_2 | 4 | 0 | 2 | 2 |
| run_3 | 4 | 0 | 2 | 2 |
| run_4 | 4 | 0 | 1 | 3 |
| run_5 | 4 | 0 | 1 | 3 |

## 5. Citas — por grafo (todas las celdas)

| Grafo | doc_correcto True | doc_correcto False | prec: punto | pagina | ausente |
|-------|------------------:|-------------------:|------------:|-------:|--------:|
| run_1 | 16 | 7 | 0 | 20 | 3 |
| run_2 | 16 | 7 | 12 | 8 | 3 |
| run_3 | 17 | 6 | 20 | 1 | 2 |
| run_4 | 15 | 8 | 14 | 3 | 5 |
| run_5 | 17 | 6 | 19 | 1 | 3 |

## 6. Celdas pendientes de adjudicación (correctitud retenida)

**35 celdas answerable** con correctitud retenida (de 90 entradas de cola; ver `adjudicacion_pendiente.json`):
- run_1: CQ-010, CQ-015, CQ-017, CQ-018, CQ-019, CQ-020, CQ-024, CQ-033
- run_2: CQ-015, CQ-017, CQ-018, CQ-019, CQ-020, CQ-024, CQ-031, CQ-033
- run_3: CQ-017, CQ-018, CQ-019, CQ-020, CQ-024, CQ-031, CQ-033
- run_4: CQ-014, CQ-017, CQ-018, CQ-019, CQ-020, CQ-033
- run_5: CQ-015, CQ-017, CQ-019, CQ-020, CQ-033, CQ-034

Además, 7 celdas **unanswerable** tienen afirmaciones a adjudicar (su veredicto de abstención se reporta, pero las afirmaciones flageadas igual requieren chequeo contra PDFs): run_1/CQ-037; run_1/CQ-038; run_2/CQ-037; run_2/CQ-038; run_3/CQ-037; run_3/CQ-038; run_5/CQ-038

## 7. Notas metodológicas

**(a) Métrica comparativa de adjudicación.** La unidad PRINCIPAL es **preguntas distintas flageadas** por grafo: run_1=10, run_2=10, run_3=9, run_4=6, run_5=7. La métrica por REPETICIÓN (25/22/18/11/14) es SECUNDARIA: el conteo por-rep mezcla *cuántas preguntas* necesitan adjudicación con la *inestabilidad rep-level* del flag, sobre-ponderando la segunda.

**(b) `multi_norma` no-puntuable en correctitud sin adjudicación.** En los **5 grafos**, TODAS las celdas `multi_norma` quedaron `pendiente_adjudicacion` (tabla 2: correcta/parcial/incorrecta en cero, todo en `pend`). El gold resumido (respuesta_esperada + cita_textual + ground_truth_secciones) no puede soportar respuestas multi-hop granulares verdaderas: una respuesta que combina 2+ secciones produce afirmaciones más finas que el referente, que el juez marca `no_soportado` (no falso) → adjudicación humana. Es **hallazgo metodológico, no defecto**: el mecanismo de seguridad del juez (no validar contra conocimiento paramétrico) operando como se diseñó. La correctitud de `multi_norma` solo es comparable entre estrategias DESPUÉS de la etapa 2.

---
**Etapa 2 (final):** tras la adjudicación humana de las afirmaciones centrales contra los PDFs, las celdas `pendiente_adjudicacion` reciben su correctitud final (correcta si las afirmaciones se verifican, incorrecta/parcial si alguna central resulta falsa) y se re-emiten las tablas 1, 2 y 6. NADA del dataset congelado se re-corre: la adjudicación solo resuelve veredictos retenidos.