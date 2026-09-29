# Reporte CIEGO — fidelidad EV2, celda C3 de la tanda 0 (ev2_c3_dev_mem) (40 respuestas × juez v1, N=3)

Veredictos por id OPACO. La tabla id_opaco → (pregunta, grafo) vive en
`desanonimizacion/tabla_id_opaco.json` y NO se cruza acá: el cruce
veredicto × grafo lo computa la revisión (pre-registro §3, ceguera de grafo).

## Instrumento y sellos


- modelo(s) observado(s): ['claude-sonnet-4-6']
- prompt sha256 observado en las respuestas del juez: ['fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455']
- stop_reasons: {'end_turn': 120}
- semilla de orden: `juez-ev2-v1`; N=3

## Carga

- respuestas: 40 — por grafo {'tanda0_ens_desarrollo': 40}; 40 preguntas × {1: 40} respuestas; criterios gold 164
- flag `respondible` del agente (metadato de trazas, no viaja al juez): {'False': 8, 'True': 32}

## Corrida

- llamadas: 120 / 120
- freno por proyección: None
- gasto real (desde dbs, filas de `cache`): 120 filas, 197400 in / 58362 out → USD 1.4676
- por repetición: {1: {'filas': 40, 'in': 65800, 'out': 19381, 'usd': 0.4881}, 2: {'filas': 40, 'in': 65800, 'out': 19498, 'usd': 0.4899}, 3: {'filas': 40, 'in': 65800, 'out': 19483, 'usd': 0.4896}}
- precios (USD/MTok): {'in': 3.0, 'out': 15.0}; tope: 2.16
- cross-hits entre repeticiones: **0** (keys por db {'ev2_c3_dev_mem_juez_r1.db': 40, 'ev2_c3_dev_mem_juez_r2.db': 40, 'ev2_c3_dev_mem_juez_r3.db': 40}; intersecciones {'ev2_c3_dev_mem_juez_r1.db∩ev2_c3_dev_mem_juez_r2.db': 0, 'ev2_c3_dev_mem_juez_r1.db∩ev2_c3_dev_mem_juez_r3.db': 0, 'ev2_c3_dev_mem_juez_r2.db∩ev2_c3_dev_mem_juez_r3.db': 0})
- hits por label dentro de cada db: {'ev2_c3_dev_mem_juez_r1.db': {'ev2_c3_dev_mem_juez_r1': 0}, 'ev2_c3_dev_mem_juez_r2.db': {'ev2_c3_dev_mem_juez_r2': 0}, 'ev2_c3_dev_mem_juez_r3.db': {'ev2_c3_dev_mem_juez_r3': 0}} (total 0); accesos por db {'ev2_c3_dev_mem_juez_r1.db': 40, 'ev2_c3_dev_mem_juez_r2.db': 40, 'ev2_c3_dev_mem_juez_r3.db': 40}
- errores del juez (no parseable/truncado): {1: 0, 2: 0, 3: 0}; respuestas incompletas (fuera de agregados): 0 

## Distribución (ciega, sobre los agregados)

- veredicto por pregunta (mapping §2): **{'parcial': 19, 'correcto': 9, 'requiere_adjudicacion': 7, 'incorrecto': 5}** sobre 40
- pares (respuesta, criterio): 164 — modales {'no_cumplido': 79, 'cumplido': 78, 'dudoso': 7}; todas las reps {'no_cumplido': 236, 'cumplido': 235, 'dudoso': 21}
- no-determinismo: unánimes 160/164; no unánimes con dudoso 4; sin_consenso 0
- clasificación auxiliar (modal): {'contenido': 37, 'abstencion': 3}; todas las reps {'contenido': 111, 'abstencion': 9}; no unánime en 0 respuestas
- veredicto × clasificación auxiliar: {'contenido→parcial': 19, 'contenido→correcto': 9, 'contenido→requiere_adjudicacion': 7, 'abstencion→incorrecto': 3, 'contenido→incorrecto': 2}
- auditoría de fragmentos (492): {'null': 210, 'verbatim': 276, 'fuga_gold': 0, 'no_verbatim': 6}

### Fragmentos no_verbatim / fuga_gold (6)

- T0C3B-9cae67fe4e c1 r1 [cumplido] no_verbatim: «exigencia por riesgo específico de tasa de interés, (4) exigencia por riesgo general de tasa de interés... El riesgo de tasa se informa con apertura en tres modalidades: Total (código 311000/xx), Espe»
- T0C3B-9cae67fe4e c1 r2 [cumplido] no_verbatim: «exigencia por riesgo específico de tasa de interés, (4) exigencia por riesgo general de tasa de interés... El riesgo de tasa se informa con apertura en tres modalidades: Total (código 311000/xx), Espe»
- T0C3B-9cae67fe4e c1 r3 [cumplido] no_verbatim: «exigencia por riesgo específico de tasa de interés, (4) exigencia por riesgo general de tasa de interés... El riesgo de tasa se informa con apertura en tres modalidades: Total (código 311000/xx), Espe»
- T0C3B-06991c55dc c3 r1 [cumplido] no_verbatim: «En operaciones con margen de variación, el CR refleja la pérdida presente o futura ante incumplimiento. [...] En operaciones sin margen, la EPF adicionaría el incremento probable de la exposición en u»
- T0C3B-06991c55dc c3 r2 [cumplido] no_verbatim: «En operaciones con margen de variación, el CR refleja la pérdida presente o futura ante incumplimiento. [...] En operaciones sin margen, la EPF adicionaría el incremento probable de la exposición en u»
- T0C3B-06991c55dc c3 r3 [cumplido] no_verbatim: «En operaciones con margen de variación, el CR refleja la pérdida presente o futura ante incumplimiento. [...] En operaciones sin margen, la EPF adicionaría el incremento probable de la exposición en u»

## Veredictos por id opaco

| id_opaco | K | modales por criterio | veredicto (mapping) | clasif. aux. (3 reps) | fragmentos null/verb/fuga/no_verb |
|---|---|---|---|---|---|
| T0C3B-0117fc3358 | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 9/3/0/0 |
| T0C3B-046600af6e | 4 | cump cump no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| T0C3B-04dfda673f | 4 | no_c no_c no_c no_c | incorrecto | cont/cont/cont | 12/0/0/0 |
| T0C3B-06991c55dc | 4 | no_c cump cump cump | parcial | cont/cont/cont | 3/6/0/3 |
| T0C3B-087e910ed9 | 4 | no_c cump no_c no_c | parcial | cont/cont/cont | 3/9/0/0 |
| T0C3B-0f4b319a55 | 5 | cump cump no_c dudo no_c | requiere_adjudicacion | cont/cont/cont | 3/12/0/0 |
| T0C3B-12bbd38a79 | 5 | no_c no_c no_c no_c no_c | incorrecto | abst/abst/abst | 15/0/0/0 |
| T0C3B-179fb67665 | 4 | no_c no_c cump no_c | parcial | cont/cont/cont | 9/3/0/0 |
| T0C3B-1833a96ec7 | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |
| T0C3B-1848b62cac | 4 | cump no_c no_c cump | parcial | cont/cont/cont | 6/6/0/0 |
| T0C3B-1d5f6e774d | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |
| T0C3B-21f0d58cd6 | 4 | no_c cump cump no_c | parcial | cont/cont/cont | 6/6/0/0 |
| T0C3B-2cc0760313 | 5 | no_c no_c no_c no_c no_c | incorrecto | cont/cont/cont | 15/0/0/0 |
| T0C3B-3395cc0562 | 4 | cump cump cump cump | correcto | cont/cont/cont | 0/12/0/0 |
| T0C3B-39c6a66112 | 4 | dudo no_c no_c no_c | requiere_adjudicacion | cont/cont/cont | 9/3/0/0 |
| T0C3B-400fd53abc | 3 | dudo no_c no_c | requiere_adjudicacion | cont/cont/cont | 3/6/0/0 |
| T0C3B-431539448e | 4 | no_c cump no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| T0C3B-44d5a70645 | 3 | cump no_c no_c | parcial | cont/cont/cont | 6/3/0/0 |
| T0C3B-4687afd834 | 5 | no_c no_c dudo cump cump | requiere_adjudicacion | cont/cont/cont | 3/12/0/0 |
| T0C3B-496f793f5d | 4 | cump cump cump cump | correcto | cont/cont/cont | 0/12/0/0 |
| T0C3B-608c3bff62 | 4 | cump cump no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| T0C3B-6628454617 | 5 | cump cump cump cump cump | correcto | cont/cont/cont | 0/15/0/0 |
| T0C3B-6c0a99d083 | 5 | cump cump cump cump no_c | parcial | cont/cont/cont | 0/15/0/0 |
| T0C3B-762ae1099b | 4 | cump cump cump cump | correcto | cont/cont/cont | 0/12/0/0 |
| T0C3B-8324384fd9 | 5 | cump no_c no_c no_c no_c | parcial | cont/cont/cont | 12/3/0/0 |
| T0C3B-8cec0da9d9 | 4 | cump dudo cump cump | requiere_adjudicacion | cont/cont/cont | 1/11/0/0 |
| T0C3B-953c218876 | 4 | no_c no_c no_c cump | parcial | cont/cont/cont | 5/7/0/0 |
| T0C3B-9cae67fe4e | 5 | cump no_c cump cump no_c | parcial | cont/cont/cont | 3/9/0/3 |
| T0C3B-a3c5c3966b | 5 | no_c no_c no_c no_c no_c | incorrecto | abst/abst/abst | 15/0/0/0 |
| T0C3B-ac7e399a95 | 5 | no_c cump no_c no_c no_c | parcial | cont/cont/cont | 12/3/0/0 |
| T0C3B-b05183cfe8 | 4 | cump cump cump cump | correcto | cont/cont/cont | 0/12/0/0 |
| T0C3B-b0e988932f | 5 | no_c dudo no_c no_c cump | requiere_adjudicacion | cont/cont/cont | 9/6/0/0 |
| T0C3B-b59af92aab | 5 | no_c cump cump cump cump | parcial | cont/cont/cont | 3/12/0/0 |
| T0C3B-c3916086fa | 4 | cump cump dudo cump | requiere_adjudicacion | cont/cont/cont | 0/12/0/0 |
| T0C3B-cdf37c295d | 5 | cump cump no_c no_c cump | parcial | cont/cont/cont | 6/9/0/0 |
| T0C3B-d95d2d510c | 4 | no_c no_c no_c cump | parcial | cont/cont/cont | 9/3/0/0 |
| T0C3B-e4cc5c8d05 | 4 | no_c cump cump cump | parcial | cont/cont/cont | 3/9/0/0 |
| T0C3B-e92f30f66e | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |
| T0C3B-ef99480621 | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 12/0/0/0 |
| T0C3B-f4aaf5bea4 | 3 | cump cump cump | correcto | cont/cont/cont | 0/9/0/0 |

Abreviaturas: cump=cumplido, no_c=no_cumplido, dudo=dudoso, S/C=sin_consenso; abst=abstencion, cont=contenido.
