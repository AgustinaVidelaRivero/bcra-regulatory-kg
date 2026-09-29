# Reporte CIEGO — fidelidad EV2, celda C2 de la tanda 0 (ev2_c2_r1_neo4j) (40 respuestas × juez v1, N=3)

Veredictos por id OPACO. La tabla id_opaco → (pregunta, grafo) vive en
`desanonimizacion/tabla_id_opaco.json` y NO se cruza acá: el cruce
veredicto × grafo lo computa la revisión (pre-registro §3, ceguera de grafo).

## Instrumento y sellos


- modelo(s) observado(s): ['claude-sonnet-4-6']
- prompt sha256 observado en las respuestas del juez: ['fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455']
- stop_reasons: {'end_turn': 120}
- semilla de orden: `juez-ev2-v1`; N=3

## Carga

- respuestas: 40 — por grafo {'KG_Reextraido_r1': 40}; 40 preguntas × {1: 40} respuestas; criterios gold 164
- flag `respondible` del agente (metadato de trazas, no viaja al juez): {'True': 33, 'False': 7}

## Corrida

- llamadas: 120 / 120
- freno por proyección: None
- gasto real (desde dbs, filas de `cache`): 120 filas, 197286 in / 57688 out → USD 1.4572
- por repetición: {1: {'filas': 40, 'in': 65762, 'out': 19288, 'usd': 0.4866}, 2: {'filas': 40, 'in': 65762, 'out': 19147, 'usd': 0.4845}, 3: {'filas': 40, 'in': 65762, 'out': 19253, 'usd': 0.4861}}
- precios (USD/MTok): {'in': 3.0, 'out': 15.0}; tope: 2.16
- cross-hits entre repeticiones: **0** (keys por db {'ev2_c2_r1_neo4j_juez_r1.db': 40, 'ev2_c2_r1_neo4j_juez_r2.db': 40, 'ev2_c2_r1_neo4j_juez_r3.db': 40}; intersecciones {'ev2_c2_r1_neo4j_juez_r1.db∩ev2_c2_r1_neo4j_juez_r2.db': 0, 'ev2_c2_r1_neo4j_juez_r1.db∩ev2_c2_r1_neo4j_juez_r3.db': 0, 'ev2_c2_r1_neo4j_juez_r2.db∩ev2_c2_r1_neo4j_juez_r3.db': 0})
- hits por label dentro de cada db: {'ev2_c2_r1_neo4j_juez_r1.db': {'ev2_c2_r1_neo4j_juez_r1': 0}, 'ev2_c2_r1_neo4j_juez_r2.db': {'ev2_c2_r1_neo4j_juez_r2': 0}, 'ev2_c2_r1_neo4j_juez_r3.db': {'ev2_c2_r1_neo4j_juez_r3': 0}} (total 0); accesos por db {'ev2_c2_r1_neo4j_juez_r1.db': 40, 'ev2_c2_r1_neo4j_juez_r2.db': 40, 'ev2_c2_r1_neo4j_juez_r3.db': 40}
- errores del juez (no parseable/truncado): {1: 0, 2: 0, 3: 0}; respuestas incompletas (fuera de agregados): 0 

## Distribución (ciega, sobre los agregados)

- veredicto por pregunta (mapping §2): **{'parcial': 23, 'correcto': 8, 'incorrecto': 4, 'requiere_adjudicacion': 5}** sobre 40
- pares (respuesta, criterio): 164 — modales {'cumplido': 80, 'no_cumplido': 76, 'dudoso': 8}; todas las reps {'cumplido': 239, 'no_cumplido': 227, 'dudoso': 26}
- no-determinismo: unánimes 158/164; no unánimes con dudoso 6; sin_consenso 0
- clasificación auxiliar (modal): {'contenido': 36, 'abstencion': 4}; todas las reps {'contenido': 108, 'abstencion': 12}; no unánime en 0 respuestas
- veredicto × clasificación auxiliar: {'contenido→parcial': 23, 'contenido→correcto': 8, 'abstencion→incorrecto': 3, 'contenido→requiere_adjudicacion': 4, 'contenido→incorrecto': 1, 'abstencion→requiere_adjudicacion': 1}
- auditoría de fragmentos (492): {'null': 195, 'verbatim': 295, 'fuga_gold': 0, 'no_verbatim': 2}

### Fragmentos no_verbatim / fuga_gold (2)

- T0C2B-28b6769231 c2 r1 [dudoso] no_verbatim: «Debe informar **previamente** al BCRA antes de implementar el aumento. La notificación debe realizarse por la vía consignada en la normativa.»
- T0C2B-28b6769231 c2 r2 [dudoso] no_verbatim: «Debe informar **previamente** al BCRA antes de implementar el aumento. La notificación debe realizarse por la vía consignada en la normativa.»

## Veredictos por id opaco

| id_opaco | K | modales por criterio | veredicto (mapping) | clasif. aux. (3 reps) | fragmentos null/verb/fuga/no_verb |
|---|---|---|---|---|---|
| T0C2B-15f80bc4a1 | 3 | cump no_c no_c | parcial | cont/cont/cont | 6/3/0/0 |
| T0C2B-1cce275862 | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 12/0/0/0 |
| T0C2B-28b6769231 | 4 | dudo dudo no_c cump | requiere_adjudicacion | cont/cont/cont | 3/7/0/2 |
| T0C2B-308c5fbced | 4 | cump cump cump no_c | parcial | cont/cont/cont | 3/9/0/0 |
| T0C2B-315a8f1c05 | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 12/0/0/0 |
| T0C2B-3476e65db1 | 4 | cump cump cump no_c | parcial | cont/cont/cont | 3/9/0/0 |
| T0C2B-383f8bcd90 | 4 | cump no_c cump no_c | parcial | cont/cont/cont | 3/9/0/0 |
| T0C2B-393cb53389 | 5 | cump cump no_c no_c cump | parcial | cont/cont/cont | 6/9/0/0 |
| T0C2B-3a126a1a5a | 5 | no_c no_c no_c no_c no_c | incorrecto | abst/abst/abst | 15/0/0/0 |
| T0C2B-4b8594e669 | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |
| T0C2B-4e6eb698bd | 5 | no_c dudo no_c dudo no_c | requiere_adjudicacion | abst/abst/abst | 9/6/0/0 |
| T0C2B-6299b0c9be | 4 | cump cump cump cump | correcto | cont/cont/cont | 0/12/0/0 |
| T0C2B-6c7beee699 | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |
| T0C2B-755b650416 | 5 | no_c cump cump no_c no_c | parcial | cont/cont/cont | 9/6/0/0 |
| T0C2B-7bd5777bc8 | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 9/3/0/0 |
| T0C2B-7defd8abcf | 4 | cump cump cump no_c | parcial | cont/cont/cont | 0/12/0/0 |
| T0C2B-837dfeed16 | 5 | cump cump cump cump no_c | parcial | cont/cont/cont | 0/15/0/0 |
| T0C2B-8386fba9b7 | 5 | dudo no_c dudo no_c no_c | requiere_adjudicacion | cont/cont/cont | 9/6/0/0 |
| T0C2B-8926cf03c2 | 4 | cump cump no_c cump | parcial | cont/cont/cont | 0/12/0/0 |
| T0C2B-9bf24133ba | 4 | cump no_c cump cump | parcial | cont/cont/cont | 3/9/0/0 |
| T0C2B-a643e60fe2 | 4 | cump cump no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| T0C2B-a8ef753431 | 5 | no_c cump no_c no_c no_c | parcial | cont/cont/cont | 9/6/0/0 |
| T0C2B-ab881d97cd | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 9/3/0/0 |
| T0C2B-b405625923 | 4 | dudo cump no_c cump | requiere_adjudicacion | cont/cont/cont | 3/9/0/0 |
| T0C2B-b7dd2b99d4 | 5 | cump no_c no_c no_c no_c | parcial | cont/cont/cont | 9/6/0/0 |
| T0C2B-c3bd1ee927 | 3 | cump cump cump | correcto | cont/cont/cont | 0/9/0/0 |
| T0C2B-c464f96b88 | 4 | cump cump no_c cump | parcial | cont/cont/cont | 0/12/0/0 |
| T0C2B-c5bfa1a47c | 4 | no_c cump no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| T0C2B-c6209b2953 | 5 | cump cump cump cump cump | correcto | cont/cont/cont | 0/15/0/0 |
| T0C2B-c923924761 | 5 | no_c no_c no_c no_c no_c | incorrecto | cont/cont/cont | 15/0/0/0 |
| T0C2B-ce714abb79 | 5 | cump cump cump cump cump | correcto | cont/cont/cont | 0/15/0/0 |
| T0C2B-d12ce9a408 | 5 | cump cump no_c no_c cump | parcial | cont/cont/cont | 6/9/0/0 |
| T0C2B-d17afef9ae | 5 | dudo cump cump cump cump | requiere_adjudicacion | cont/cont/cont | 0/15/0/0 |
| T0C2B-d4efd8a98e | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| T0C2B-dfa56336d2 | 4 | no_c no_c no_c cump | parcial | cont/cont/cont | 9/3/0/0 |
| T0C2B-e21ebda5eb | 4 | cump cump cump cump | correcto | cont/cont/cont | 0/12/0/0 |
| T0C2B-f23187467d | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 9/3/0/0 |
| T0C2B-f56bdf9cc9 | 4 | no_c cump no_c no_c | parcial | cont/cont/cont | 3/9/0/0 |
| T0C2B-f8be153fd5 | 3 | cump no_c cump | parcial | cont/cont/cont | 3/6/0/0 |
| T0C2B-f97dcf700f | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |

Abreviaturas: cump=cumplido, no_c=no_cumplido, dudo=dudoso, S/C=sin_consenso; abst=abstencion, cont=contenido.
