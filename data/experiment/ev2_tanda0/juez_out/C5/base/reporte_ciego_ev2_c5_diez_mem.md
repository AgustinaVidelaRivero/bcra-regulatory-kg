# Reporte CIEGO — fidelidad EV2, celda C5 de la tanda 0 (ev2_c5_diez_mem) (20 respuestas × juez v1, N=3)

Veredictos por id OPACO. La tabla id_opaco → (pregunta, grafo) vive en
`desanonimizacion/tabla_id_opaco.json` y NO se cruza acá: el cruce
veredicto × grafo lo computa la revisión (pre-registro §3, ceguera de grafo).

## Instrumento y sellos


- modelo(s) observado(s): ['claude-sonnet-4-6']
- prompt sha256 observado en las respuestas del juez: ['fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455']
- stop_reasons: {'end_turn': 60}
- semilla de orden: `juez-ev2-v1`; N=3

## Carga

- respuestas: 20 — por grafo {'tanda0_ens_diez': 20}; 20 preguntas × {1: 20} respuestas; criterios gold 60
- flag `respondible` del agente (metadato de trazas, no viaja al juez): {'True': 18, 'False': 2}

## Corrida

- llamadas: 60 / 60
- freno por proyección: None
- gasto real (desde dbs, filas de `cache`): 60 filas, 95487 in / 25158 out → USD 0.6638
- por repetición: {1: {'filas': 20, 'in': 31829, 'out': 8472, 'usd': 0.2226}, 2: {'filas': 20, 'in': 31829, 'out': 8345, 'usd': 0.2207}, 3: {'filas': 20, 'in': 31829, 'out': 8341, 'usd': 0.2206}}
- precios (USD/MTok): {'in': 3.0, 'out': 15.0}; tope: 1.08
- cross-hits entre repeticiones: **0** (keys por db {'ev2_c5_diez_mem_juez_r1.db': 20, 'ev2_c5_diez_mem_juez_r2.db': 20, 'ev2_c5_diez_mem_juez_r3.db': 20}; intersecciones {'ev2_c5_diez_mem_juez_r1.db∩ev2_c5_diez_mem_juez_r2.db': 0, 'ev2_c5_diez_mem_juez_r1.db∩ev2_c5_diez_mem_juez_r3.db': 0, 'ev2_c5_diez_mem_juez_r2.db∩ev2_c5_diez_mem_juez_r3.db': 0})
- hits por label dentro de cada db: {'ev2_c5_diez_mem_juez_r1.db': {'ev2_c5_diez_mem_juez_r1': 0}, 'ev2_c5_diez_mem_juez_r2.db': {'ev2_c5_diez_mem_juez_r2': 0}, 'ev2_c5_diez_mem_juez_r3.db': {'ev2_c5_diez_mem_juez_r3': 0}} (total 0); accesos por db {'ev2_c5_diez_mem_juez_r1.db': 20, 'ev2_c5_diez_mem_juez_r2.db': 20, 'ev2_c5_diez_mem_juez_r3.db': 20}
- errores del juez (no parseable/truncado): {1: 0, 2: 0, 3: 0}; respuestas incompletas (fuera de agregados): 0 

## Distribución (ciega, sobre los agregados)

- veredicto por pregunta (mapping §2): **{'parcial': 7, 'correcto': 8, 'incorrecto': 1, 'requiere_adjudicacion': 4}** sobre 20
- pares (respuesta, criterio): 60 — modales {'cumplido': 38, 'no_cumplido': 18, 'dudoso': 4}; todas las reps {'cumplido': 114, 'no_cumplido': 54, 'dudoso': 12}
- no-determinismo: unánimes 60/60; no unánimes con dudoso 0; sin_consenso 0
- clasificación auxiliar (modal): {'contenido': 19, 'abstencion': 1}; todas las reps {'contenido': 57, 'abstencion': 3}; no unánime en 0 respuestas
- veredicto × clasificación auxiliar: {'contenido→parcial': 7, 'contenido→correcto': 8, 'contenido→incorrecto': 1, 'contenido→requiere_adjudicacion': 3, 'abstencion→requiere_adjudicacion': 1}
- auditoría de fragmentos (180): {'null': 29, 'verbatim': 148, 'fuga_gold': 0, 'no_verbatim': 3}

### Fragmentos no_verbatim / fuga_gold (3)

- T0C5B-3b98c9e00b c4 r1 [cumplido] no_verbatim: «los depósitos en monedas extranjeras distintas al dólar estadounidense realizados en dicha cuenta especial se consideran en su respectiva moneda para la aplicación de la capacidad de préstamo»
- T0C5B-3b98c9e00b c4 r2 [cumplido] no_verbatim: «los depósitos en monedas extranjeras distintas al dólar estadounidense realizados en dicha cuenta especial se consideran en su respectiva moneda para la aplicación de la capacidad de préstamo»
- T0C5B-3b98c9e00b c4 r3 [cumplido] no_verbatim: «los depósitos en monedas extranjeras distintas al dólar estadounidense realizados en dicha cuenta especial se consideran en su respectiva moneda para la aplicación de la capacidad de préstamo»

## Veredictos por id opaco

| id_opaco | K | modales por criterio | veredicto (mapping) | clasif. aux. (3 reps) | fragmentos null/verb/fuga/no_verb |
|---|---|---|---|---|---|
| T0C5B-09b80a0f68 | 3 | cump cump cump | correcto | cont/cont/cont | 0/9/0/0 |
| T0C5B-0d62fe774d | 3 | no_c no_c no_c | incorrecto | cont/cont/cont | 5/4/0/0 |
| T0C5B-31a66e14f3 | 3 | cump no_c cump | parcial | cont/cont/cont | 3/6/0/0 |
| T0C5B-3b98c9e00b | 4 | cump dudo no_c cump | requiere_adjudicacion | cont/cont/cont | 3/6/0/3 |
| T0C5B-48d0b52f37 | 3 | cump no_c no_c | parcial | cont/cont/cont | 0/9/0/0 |
| T0C5B-57d01b3ad5 | 3 | cump cump cump | correcto | cont/cont/cont | 0/9/0/0 |
| T0C5B-69bc15d16d | 3 | cump no_c cump | parcial | cont/cont/cont | 0/9/0/0 |
| T0C5B-700e268158 | 3 | cump cump cump | correcto | cont/cont/cont | 0/9/0/0 |
| T0C5B-7aec9b32aa | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 9/3/0/0 |
| T0C5B-8c6d9e24a1 | 3 | cump cump cump | correcto | cont/cont/cont | 0/9/0/0 |
| T0C5B-986680c5cc | 3 | cump cump cump | correcto | cont/cont/cont | 0/9/0/0 |
| T0C5B-9c1ee2ca2c | 3 | cump cump cump | correcto | cont/cont/cont | 0/9/0/0 |
| T0C5B-a3e3838cb3 | 4 | no_c no_c cump cump | parcial | cont/cont/cont | 6/6/0/0 |
| T0C5B-bcb8914d2d | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |
| T0C5B-c5ddad94ad | 3 | cump cump no_c | parcial | cont/cont/cont | 0/9/0/0 |
| T0C5B-d7845a3b19 | 3 | no_c no_c dudo | requiere_adjudicacion | abst/abst/abst | 0/9/0/0 |
| T0C5B-e1aaa8956b | 2 | cump no_c | parcial | cont/cont/cont | 0/6/0/0 |
| T0C5B-ee728cf77a | 3 | cump cump cump | correcto | cont/cont/cont | 0/9/0/0 |
| T0C5B-f68459f03a | 2 | dudo cump | requiere_adjudicacion | cont/cont/cont | 0/6/0/0 |
| T0C5B-fb7596a6df | 3 | cump dudo no_c | requiere_adjudicacion | cont/cont/cont | 3/6/0/0 |

Abreviaturas: cump=cumplido, no_c=no_cumplido, dudo=dudoso, S/C=sin_consenso; abst=abstencion, cont=contenido.
