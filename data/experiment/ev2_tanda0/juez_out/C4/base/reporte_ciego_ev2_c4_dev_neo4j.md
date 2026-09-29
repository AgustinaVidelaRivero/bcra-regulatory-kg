# Reporte CIEGO — fidelidad EV2, celda C4 de la tanda 0 (ev2_c4_dev_neo4j) (40 respuestas × juez v1, N=3)

Veredictos por id OPACO. La tabla id_opaco → (pregunta, grafo) vive en
`desanonimizacion/tabla_id_opaco.json` y NO se cruza acá: el cruce
veredicto × grafo lo computa la revisión (pre-registro §3, ceguera de grafo).

## Instrumento y sellos


- modelo(s) observado(s): ['claude-sonnet-4-6']
- prompt sha256 observado en las respuestas del juez: ['fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455']
- stop_reasons: {'end_turn': 120}
- semilla de orden: `juez-ev2-v1`; N=3

## Carga

- respuestas: 40 — por grafo {'KG_Tanda0_Desarrollo_r1': 40}; 40 preguntas × {1: 40} respuestas; criterios gold 164
- flag `respondible` del agente (metadato de trazas, no viaja al juez): {'True': 33, 'False': 7}

## Corrida

- llamadas: 120 / 120
- freno por proyección: None
- gasto real (desde dbs, filas de `cache`): 120 filas, 197031 in / 59418 out → USD 1.4824
- por repetición: {1: {'filas': 40, 'in': 65677, 'out': 19882, 'usd': 0.4953}, 2: {'filas': 40, 'in': 65677, 'out': 19796, 'usd': 0.494}, 3: {'filas': 40, 'in': 65677, 'out': 19740, 'usd': 0.4931}}
- precios (USD/MTok): {'in': 3.0, 'out': 15.0}; tope: 2.16
- cross-hits entre repeticiones: **0** (keys por db {'ev2_c4_dev_neo4j_juez_r1.db': 40, 'ev2_c4_dev_neo4j_juez_r2.db': 40, 'ev2_c4_dev_neo4j_juez_r3.db': 40}; intersecciones {'ev2_c4_dev_neo4j_juez_r1.db∩ev2_c4_dev_neo4j_juez_r2.db': 0, 'ev2_c4_dev_neo4j_juez_r1.db∩ev2_c4_dev_neo4j_juez_r3.db': 0, 'ev2_c4_dev_neo4j_juez_r2.db∩ev2_c4_dev_neo4j_juez_r3.db': 0})
- hits por label dentro de cada db: {'ev2_c4_dev_neo4j_juez_r1.db': {'ev2_c4_dev_neo4j_juez_r1': 0}, 'ev2_c4_dev_neo4j_juez_r2.db': {'ev2_c4_dev_neo4j_juez_r2': 0}, 'ev2_c4_dev_neo4j_juez_r3.db': {'ev2_c4_dev_neo4j_juez_r3': 0}} (total 0); accesos por db {'ev2_c4_dev_neo4j_juez_r1.db': 40, 'ev2_c4_dev_neo4j_juez_r2.db': 40, 'ev2_c4_dev_neo4j_juez_r3.db': 40}
- errores del juez (no parseable/truncado): {1: 0, 2: 0, 3: 0}; respuestas incompletas (fuera de agregados): 0 

## Distribución (ciega, sobre los agregados)

- veredicto por pregunta (mapping §2): **{'requiere_adjudicacion': 5, 'correcto': 9, 'parcial': 20, 'incorrecto': 6}** sobre 40
- pares (respuesta, criterio): 164 — modales {'dudoso': 5, 'no_cumplido': 73, 'cumplido': 86}; todas las reps {'dudoso': 15, 'no_cumplido': 219, 'cumplido': 258}
- no-determinismo: unánimes 162/164; no unánimes con dudoso 2; sin_consenso 0
- clasificación auxiliar (modal): {'contenido': 37, 'abstencion': 3}; todas las reps {'contenido': 111, 'abstencion': 9}; no unánime en 0 respuestas
- veredicto × clasificación auxiliar: {'contenido→requiere_adjudicacion': 5, 'contenido→correcto': 9, 'contenido→parcial': 20, 'abstencion→incorrecto': 3, 'contenido→incorrecto': 3}
- auditoría de fragmentos (492): {'null': 184, 'verbatim': 303, 'fuga_gold': 0, 'no_verbatim': 5}

### Fragmentos no_verbatim / fuga_gold (5)

- T0C4B-b953f6b6d0 c3 r1 [cumplido] no_verbatim: «En operaciones con margen de variación, el CR refleja la pérdida si la liquidación y reposición fueran instantáneas. En operaciones sin margen, representa la pérdida ante incumplimiento e inmediata li»
- T0C4B-b953f6b6d0 c3 r2 [cumplido] no_verbatim: «En operaciones con margen de variación, el CR refleja la pérdida si la liquidación y reposición fueran instantáneas. En operaciones sin margen, representa la pérdida ante incumplimiento e inmediata li»
- T0C4B-b953f6b6d0 c3 r3 [cumplido] no_verbatim: «En operaciones con margen de variación, el CR refleja la pérdida si la liquidación y reposición fueran instantáneas. En operaciones sin margen, representa la pérdida ante incumplimiento e inmediata li»
- T0C4B-e49e129ff4 c3 r2 [cumplido] no_verbatim: «Las operaciones que se incluyen en esta categoría comprenden: Transferencias personales [...] Donaciones, Jubilaciones y pensiones, Transferencias de ayuda familiar»
- T0C4B-e49e129ff4 c3 r3 [cumplido] no_verbatim: «Las operaciones que se incluyen en esta categoría comprenden: Transferencias personales [...] Donaciones, Jubilaciones y pensiones, Transferencias de ayuda familiar»

## Veredictos por id opaco

| id_opaco | K | modales por criterio | veredicto (mapping) | clasif. aux. (3 reps) | fragmentos null/verb/fuga/no_verb |
|---|---|---|---|---|---|
| T0C4B-0354d1e988 | 5 | no_c no_c no_c no_c no_c | incorrecto | abst/abst/abst | 15/0/0/0 |
| T0C4B-05947922a8 | 5 | cump cump cump cump no_c | parcial | cont/cont/cont | 0/15/0/0 |
| T0C4B-066c97e768 | 4 | no_c no_c no_c no_c | incorrecto | cont/cont/cont | 10/2/0/0 |
| T0C4B-06e979123d | 5 | no_c cump cump cump cump | parcial | cont/cont/cont | 3/12/0/0 |
| T0C4B-0e7c8d1861 | 4 | cump cump cump cump | correcto | cont/cont/cont | 0/12/0/0 |
| T0C4B-1d662c2b07 | 4 | cump cump cump cump | correcto | cont/cont/cont | 0/12/0/0 |
| T0C4B-25158426ed | 3 | dudo no_c no_c | requiere_adjudicacion | cont/cont/cont | 3/6/0/0 |
| T0C4B-273fab355c | 4 | dudo cump cump cump | requiere_adjudicacion | cont/cont/cont | 0/12/0/0 |
| T0C4B-2a9240fdcd | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |
| T0C4B-4ffa7837a0 | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 7/5/0/0 |
| T0C4B-5fce491d2f | 3 | dudo cump cump | requiere_adjudicacion | cont/cont/cont | 0/9/0/0 |
| T0C4B-6767342433 | 5 | cump cump cump no_c cump | parcial | cont/cont/cont | 3/12/0/0 |
| T0C4B-6d73f96abc | 5 | no_c no_c no_c no_c no_c | incorrecto | cont/cont/cont | 15/0/0/0 |
| T0C4B-715bdf9f7d | 5 | cump cump no_c no_c no_c | parcial | cont/cont/cont | 9/6/0/0 |
| T0C4B-7c92d3e727 | 4 | cump cump cump no_c | parcial | cont/cont/cont | 3/9/0/0 |
| T0C4B-7e4a734d19 | 4 | cump cump no_c cump | parcial | cont/cont/cont | 0/12/0/0 |
| T0C4B-83d8636b4d | 5 | cump cump no_c no_c no_c | parcial | cont/cont/cont | 3/12/0/0 |
| T0C4B-855b7042ef | 4 | cump cump cump cump | correcto | cont/cont/cont | 0/12/0/0 |
| T0C4B-8b28ae489c | 4 | cump cump no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| T0C4B-99c43a755e | 4 | no_c no_c no_c cump | parcial | cont/cont/cont | 9/3/0/0 |
| T0C4B-9e2a3da18c | 3 | cump no_c no_c | parcial | cont/cont/cont | 6/3/0/0 |
| T0C4B-a20f18c44e | 4 | cump no_c cump no_c | parcial | cont/cont/cont | 6/6/0/0 |
| T0C4B-a65e9ea436 | 4 | no_c cump no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| T0C4B-aa6cb4a706 | 4 | cump cump cump cump | correcto | cont/cont/cont | 0/12/0/0 |
| T0C4B-aab9e14ee0 | 4 | no_c no_c no_c cump | parcial | cont/cont/cont | 6/6/0/0 |
| T0C4B-b52a544894 | 5 | cump cump cump cump cump | correcto | cont/cont/cont | 0/15/0/0 |
| T0C4B-b953f6b6d0 | 4 | no_c cump cump cump | parcial | cont/cont/cont | 3/6/0/3 |
| T0C4B-c11e4ef72d | 4 | no_c cump no_c no_c | parcial | cont/cont/cont | 9/3/0/0 |
| T0C4B-c4e47c3479 | 4 | cump no_c cump cump | parcial | cont/cont/cont | 3/9/0/0 |
| T0C4B-d5c2f89978 | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |
| T0C4B-d6fa014a30 | 5 | cump cump no_c cump cump | parcial | cont/cont/cont | 3/12/0/0 |
| T0C4B-d8ea9cd689 | 5 | no_c cump no_c no_c no_c | parcial | cont/cont/cont | 11/4/0/0 |
| T0C4B-e0b9d32e5f | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 12/0/0/0 |
| T0C4B-e157b7795f | 5 | cump no_c cump dudo cump | requiere_adjudicacion | cont/cont/cont | 0/15/0/0 |
| T0C4B-e49e129ff4 | 4 | cump cump cump cump | correcto | cont/cont/cont | 0/10/0/2 |
| T0C4B-e640c80ce9 | 4 | dudo no_c no_c cump | requiere_adjudicacion | cont/cont/cont | 3/9/0/0 |
| T0C4B-e75fcc2bf9 | 5 | no_c cump cump no_c cump | parcial | cont/cont/cont | 6/9/0/0 |
| T0C4B-e8dc576b25 | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |
| T0C4B-efe38e40cc | 5 | no_c no_c no_c no_c no_c | incorrecto | abst/abst/abst | 15/0/0/0 |
| T0C4B-fc9d0e2941 | 4 | no_c no_c no_c no_c | incorrecto | cont/cont/cont | 9/3/0/0 |

Abreviaturas: cump=cumplido, no_c=no_cumplido, dudo=dudoso, S/C=sin_consenso; abst=abstencion, cont=contenido.
