# Reporte CIEGO — fidelidad EV2 de KG-Reextraído-r1 (U-B1.8) (40 respuestas × juez v1, N=3)

Veredictos por id OPACO. La tabla id_opaco → (pregunta, grafo) vive en
`desanonimizacion/tabla_id_opaco.json` y NO se cruza acá: el cruce
veredicto × grafo lo computa la revisión (pre-registro §3, ceguera de grafo).

## Instrumento y sellos

- `prompt_juez_v1.md`: `fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455`
- `juez.py`: `b4a74ba536dd5938aa0935ee088e8327bbad411229679887177653a698421236`
- `mapping.py`: `c905dd1a510925bad7a324722ff593ded09a95e77629e0a7e90fa13d5f3e6660`
- `loader.py`: `5aba8b7a0aa46e8d5c4c83b33884b8cae7d0a099884a7d3bc935de4d3097af8b`
- `harness.py`: `fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e`
- `judge.py`: `7169145aaeb3f2d90a7e3873964378aa6520c5688fed136cf5a79ea63b589eaa`
- `llm_cache.py`: `fc86b0e48df464d01d87aa1d8067168d2d522f66ead53f594092a16484c22752`
- `gold`: `1d58733699c325c90510e1ead5f18eac6c3cd970ee3b0ab7ff141da539162b40`
- `grafo_v2`: `8e2eadee57b48e00ccb51ade9a953ba1469001fe089c45d97c4307ccf2725581`
- `grafo_v3`: `26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571`
- `grafo_run_3`: `12c226e22b8fdc8f46999cae7f1eb808930e71f5dfe803f3a4f637a88348c410`
- `grafo_r1`: `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a`
- `comun_ev2.py`: `a397e94da899870e84fd50d788298dbd43c8e0e15eddf765466ec43e8222535a`
- `runner_ev2.py`: `c4b067f914cb080574fe16ba087f806e95351b4338ed8463092ad3ffae5ca931`
- `metrica_ev2.py`: `5c629c00e993bd3a0e7b1aafdf95ae5fcf1cd695dff1c8018f1b16a766b99c75`
- `comun_fidelidad.py`: `bb5c83cc1941a64b825b3c00e3160bd5171838aa429c54bbd4eb15c549d4fc49`
- `pipeline_fidelidad.py`: `86dabb4fb31543c1d63614a6361f04fb2b7eab129474e51d359c2bf5a1ead569`
- `agregacion_enc.py`: `b79fd7c67b5adb97010a749077693e01132fff2440eac9833cbc7710a7a6c7d0`
- `resolucion.py`: `afe66ee951cd847bc4e02486c8086b06e7a588c59a48b385b2245e6214b6c51b`
- `metrica.py`: `059f411b0f429dd371635bbcf9c382c1321342e6e88f89cd31bd51a154febb7e`

- modelo(s) observado(s): ['claude-sonnet-4-6']
- prompt sha256 observado en las respuestas del juez: ['fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455']
- stop_reasons: {'end_turn': 120}
- semilla de orden: `juez-ev2-v1`; N=3

## Carga

- respuestas: 40 — por grafo {'r1': 40}; 40 preguntas × {1: 40} respuestas; criterios gold 164
- flag `respondible` del agente (metadato de trazas, no viaja al juez): {'True': 31, 'False': 9}

## Corrida

- llamadas: 120 / 120
- freno por proyección: None
- gasto real (desde dbs, filas de `cache`): 120 filas, 196968 in / 56708 out → USD 1.4415
- por repetición: {1: {'filas': 40, 'in': 65656, 'out': 18938, 'usd': 0.481}, 2: {'filas': 40, 'in': 65656, 'out': 18934, 'usd': 0.481}, 3: {'filas': 40, 'in': 65656, 'out': 18836, 'usd': 0.4795}}
- precios (USD/MTok): {'in': 3.0, 'out': 15.0}; tope: 2.091
- cross-hits entre repeticiones: **0** (keys por db {'ev2_r1_eval_r1.db': 40, 'ev2_r1_eval_r2.db': 40, 'ev2_r1_eval_r3.db': 40}; intersecciones {'ev2_r1_eval_r1.db∩ev2_r1_eval_r2.db': 0, 'ev2_r1_eval_r1.db∩ev2_r1_eval_r3.db': 0, 'ev2_r1_eval_r2.db∩ev2_r1_eval_r3.db': 0})
- hits por label dentro de cada db: {'ev2_r1_eval_r1.db': {'ev2_r1_eval_r1': 0}, 'ev2_r1_eval_r2.db': {'ev2_r1_eval_r2': 0}, 'ev2_r1_eval_r3.db': {'ev2_r1_eval_r3': 0}} (total 0); accesos por db {'ev2_r1_eval_r1.db': 40, 'ev2_r1_eval_r2.db': 40, 'ev2_r1_eval_r3.db': 40}
- errores del juez (no parseable/truncado): {1: 0, 2: 0, 3: 0}; respuestas incompletas (fuera de agregados): 0 

## Distribución (ciega, sobre los agregados)

- veredicto por pregunta (mapping §2): **{'parcial': 23, 'requiere_adjudicacion': 5, 'incorrecto': 7, 'correcto': 5}** sobre 40
- pares (respuesta, criterio): 164 — modales {'cumplido': 69, 'no_cumplido': 90, 'dudoso': 5}; todas las reps {'cumplido': 207, 'no_cumplido': 270, 'dudoso': 15}
- no-determinismo: unánimes 164/164; no unánimes con dudoso 0; sin_consenso 0
- clasificación auxiliar (modal): {'contenido': 34, 'abstencion': 6}; todas las reps {'contenido': 102, 'abstencion': 18}; no unánime en 0 respuestas
- veredicto × clasificación auxiliar: {'contenido→parcial': 23, 'contenido→requiere_adjudicacion': 5, 'abstencion→incorrecto': 6, 'contenido→correcto': 5, 'contenido→incorrecto': 1}
- auditoría de fragmentos (492): {'null': 229, 'verbatim': 256, 'fuga_gold': 0, 'no_verbatim': 7}

### Fragmentos no_verbatim / fuga_gold (7)

- EV2R1-6bec148149 c4 r1 [no_cumplido] no_verbatim: «la información específica sobre [...] (2) la identificación específica para turistas extranjeros (como número de pasaporte u otro documento), no se encuentra disponible en los nodos consultados del Kn»
- EV2R1-6bec148149 c4 r2 [no_cumplido] no_verbatim: «la información específica sobre [...] la identificación específica para turistas extranjeros (como número de pasaporte u otro documento), no se encuentra disponible en los nodos consultados del Knowle»
- EV2R1-6bec148149 c4 r3 [no_cumplido] no_verbatim: «la información específica sobre [...] la identificación específica para turistas extranjeros (como número de pasaporte u otro documento), no se encuentra disponible en los nodos consultados del Knowle»
- EV2R1-d528ab4354 c2 r1 [no_cumplido] no_verbatim: «Se admiten excepciones a la regla de efectivo en los siguientes casos: - Punto 8.6.1 y 8.6.2... - Punto 8.6.3...»
- EV2R1-d528ab4354 c2 r2 [no_cumplido] no_verbatim: «Se admiten excepciones a la regla de efectivo en los siguientes casos: - Punto 8.6.1 y 8.6.2: Se permite aportar instrumentos de regulación monetaria y otros instrumentos...»
- EV2R1-d528ab4354 c2 r3 [no_cumplido] no_verbatim: «Se admiten excepciones a la regla de efectivo en los siguientes casos: - Punto 8.6.1 y 8.6.2: Se permite aportar instrumentos de regulación monetaria y otros instrumentos...»
- EV2R1-d528ab4354 c4 r2 [cumplido] no_verbatim: «los instrumentos de regulación monetaria y otros instrumentos, que deberán registrarse a su valor de mercado»

## Veredictos por id opaco

| id_opaco | K | modales por criterio | veredicto (mapping) | clasif. aux. (3 reps) | fragmentos null/verb/fuga/no_verb |
|---|---|---|---|---|---|
| EV2R1-00655f1ded | 4 | cump cump no_c cump | parcial | cont/cont/cont | 0/12/0/0 |
| EV2R1-04ce44f69b | 5 | cump no_c no_c no_c no_c | parcial | cont/cont/cont | 12/3/0/0 |
| EV2R1-0a65503bfe | 4 | dudo cump cump no_c | requiere_adjudicacion | cont/cont/cont | 3/9/0/0 |
| EV2R1-0ff66f88ae | 4 | cump no_c cump cump | parcial | cont/cont/cont | 3/9/0/0 |
| EV2R1-1848eadba5 | 4 | dudo no_c no_c cump | requiere_adjudicacion | cont/cont/cont | 3/9/0/0 |
| EV2R1-19347d39fc | 4 | no_c no_c dudo cump | requiere_adjudicacion | cont/cont/cont | 6/6/0/0 |
| EV2R1-1cbb0645b9 | 3 | cump no_c no_c | parcial | cont/cont/cont | 6/3/0/0 |
| EV2R1-252b750185 | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |
| EV2R1-25cd9bd7f0 | 5 | cump cump cump cump cump | correcto | cont/cont/cont | 0/15/0/0 |
| EV2R1-2f00f1f679 | 4 | no_c no_c no_c no_c | incorrecto | cont/cont/cont | 9/3/0/0 |
| EV2R1-3095cd8da3 | 5 | cump cump cump cump no_c | parcial | cont/cont/cont | 0/15/0/0 |
| EV2R1-3861519dff | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 9/3/0/0 |
| EV2R1-47d014aafe | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 7/5/0/0 |
| EV2R1-4d8d65c661 | 4 | cump no_c no_c cump | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R1-6bdfe6912b | 4 | cump cump no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R1-6bec148149 | 5 | no_c no_c no_c no_c cump | parcial | cont/cont/cont | 9/3/0/3 |
| EV2R1-6ca8ddd649 | 4 | cump cump cump cump | correcto | cont/cont/cont | 0/12/0/0 |
| EV2R1-6e4351da9b | 5 | no_c no_c no_c no_c no_c | incorrecto | abst/abst/abst | 15/0/0/0 |
| EV2R1-71c71d52ae | 4 | cump cump cump no_c | parcial | cont/cont/cont | 3/9/0/0 |
| EV2R1-8b1c2734d3 | 4 | no_c cump no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R1-93eea18bb9 | 5 | cump cump no_c no_c no_c | parcial | cont/cont/cont | 9/6/0/0 |
| EV2R1-9cbcc9852a | 5 | no_c dudo cump no_c no_c | requiere_adjudicacion | cont/cont/cont | 9/6/0/0 |
| EV2R1-ae5c1c005b | 4 | cump cump no_c no_c | parcial | cont/cont/cont | 4/8/0/0 |
| EV2R1-b38683643c | 3 | cump cump no_c | parcial | cont/cont/cont | 3/6/0/0 |
| EV2R1-b725a23200 | 3 | cump no_c cump | parcial | cont/cont/cont | 3/6/0/0 |
| EV2R1-b8e483a581 | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |
| EV2R1-bb984b7eb2 | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 12/0/0/0 |
| EV2R1-bf01984076 | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 12/0/0/0 |
| EV2R1-c3db008a4c | 2 | no_c cump | parcial | cont/cont/cont | 3/3/0/0 |
| EV2R1-c60347090b | 4 | cump cump dudo no_c | requiere_adjudicacion | cont/cont/cont | 3/9/0/0 |
| EV2R1-c721a2b153 | 5 | cump cump cump cump cump | correcto | cont/cont/cont | 0/15/0/0 |
| EV2R1-c98702a032 | 5 | no_c no_c no_c no_c no_c | incorrecto | abst/abst/abst | 12/3/0/0 |
| EV2R1-cde9363909 | 5 | no_c no_c no_c no_c cump | parcial | cont/cont/cont | 12/3/0/0 |
| EV2R1-d1688b43a8 | 4 | cump cump no_c cump | parcial | cont/cont/cont | 0/12/0/0 |
| EV2R1-d528ab4354 | 5 | cump no_c no_c cump cump | parcial | cont/cont/cont | 2/9/0/4 |
| EV2R1-d64e055766 | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 9/3/0/0 |
| EV2R1-d662c84c17 | 5 | cump cump no_c no_c cump | parcial | cont/cont/cont | 6/9/0/0 |
| EV2R1-ec5ef20075 | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 9/3/0/0 |
| EV2R1-f4b0955f4e | 5 | no_c no_c no_c no_c no_c | incorrecto | abst/abst/abst | 12/3/0/0 |
| EV2R1-fcd42c8725 | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |

Abreviaturas: cump=cumplido, no_c=no_cumplido, dudo=dudoso, S/C=sin_consenso; abst=abstencion, cont=contenido.
