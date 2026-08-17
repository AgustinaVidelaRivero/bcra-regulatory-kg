# Reporte FINAL CIEGO — encadenamiento §7 EV2 (re-corridas N=3 del agente × juez v1 N=3)

Veredictos por id OPACO. El id de par es el id opaco de la respuesta BASE
(`EV2R-…`, tabla de la corrida base); las respuestas nuevas llevan ids `EV2E-…`
(tabla en `desanonimizacion_SOLO_MESA/`). El cruce por grafo lo computa la mesa.

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
- `base_veredictos_agregados_ciego.json`: `9f1046c61372db44407d94cf3676d1a93db47f09f7c881e367517f8e01e8828c`
- `base_tabla_id_opaco.json`: `e219b2fb38eabc561f7118005c10408ce305a2ccc623e8d9915d9cda8cab6137`
- `runner_ev2.py`: `c4b067f914cb080574fe16ba087f806e95351b4338ed8463092ad3ffae5ca931`
- `comun_ev2.py`: `a397e94da899870e84fd50d788298dbd43c8e0e15eddf765466ec43e8222535a`
- `comun_fidelidad.py`: `bb5c83cc1941a64b825b3c00e3160bd5171838aa429c54bbd4eb15c549d4fc49`
- `pipeline_fidelidad.py`: `86dabb4fb31543c1d63614a6361f04fb2b7eab129474e51d359c2bf5a1ead569`

- modelo(s) del juez observado(s): ['claude-sonnet-4-6']; prompt sha256 observado: ['fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455']
- stop_reasons: {'end_turn': 594}

## Carga

- respuestas nuevas juzgadas: 198 (previstas 198); faltantes/incompletas del agente: 0 
- textos duplicados dentro de una misma pregunta (entre re-corridas): 16 → hits intra-db esperados por never-pay-twice: 60
- criterios gold: 164; flag `respondible` (metadato, no viaja al juez): {'False': 31, 'True': 167}

## Corrida del juez

- llamadas: 594 / 594; freno por proyección: None
- gasto real (desde dbs): 534 filas, 898515 in / 269901 out → USD 6.7441; por rep {1: {'filas': 178, 'in': 299505, 'out': 89925, 'usd': 2.2474}, 2: {'filas': 178, 'in': 299505, 'out': 90171, 'usd': 2.2511}, 3: {'filas': 178, 'in': 299505, 'out': 89805, 'usd': 2.2456}}
- precios (USD/MTok): {'in': 3.0, 'out': 15.0}; tope: 12.0
- cross-hits entre repeticiones del juez: **0** (keys por db {'ev2_enc_juez_r1.db': 178, 'ev2_enc_juez_r2.db': 178, 'ev2_enc_juez_r3.db': 178}; intersecciones {'ev2_enc_juez_r1.db∩ev2_enc_juez_r2.db': 0, 'ev2_enc_juez_r1.db∩ev2_enc_juez_r3.db': 0, 'ev2_enc_juez_r2.db∩ev2_enc_juez_r3.db': 0})
- hits por label dentro de cada db: {'ev2_enc_juez_r1.db': {'ev2_enc_juez_r1': 20}, 'ev2_enc_juez_r2.db': {'ev2_enc_juez_r2': 20}, 'ev2_enc_juez_r3.db': {'ev2_enc_juez_r3': 20}} (total 60; esperados por textos duplicados 60; accesos {'ev2_enc_juez_r1.db': 198, 'ev2_enc_juez_r2.db': 198, 'ev2_enc_juez_r3.db': 198})
- keys en común con las dbs del juez de la corrida base (informativo; dbs distintas): {'r1': 10, 'r2': 10, 'r3': 10}
- errores del juez: {1: 0, 2: 0, 3: 0}; respuestas incompletas: 0 

## Distribución por RESPUESTA nueva (mapping §2, ciega)

- veredicto por respuesta: **{'parcial': 148, 'correcto': 12, 'incorrecto': 14, 'requiere_adjudicacion': 24}** sobre 198
- pares (respuesta, criterio): 831 — modales {'cumplido': 403, 'no_cumplido': 402, 'dudoso': 26}; unánimes 820; sin_consenso 0
- clasificación auxiliar modal: {'contenido': 188, 'abstencion': 10}
- auditoría de fragmentos: {'null': 933, 'verbatim': 1516, 'fuga_gold': 0, 'no_verbatim': 44}

## Agregación por PAR (protocolo §3: mayoría de las 3 re-corridas; empate triple → parcial)

- pares agregados: 66 / 66; incompletos: 0 
- **disparados (base parcial) — final: {'parcial': 49, 'incorrecto': 4, 'requiere_adjudicacion': 9, 'correcto': 1}**; vías {'mayoria_2_de_3': 7, 'pendiente_de_adjudicacion': 9, 'unanime': 40, 'invariante_con_pendiente': 7}; unánimes 42
- disparados — veredictos individuales de las re-corridas: {'parcial': 145, 'correcto': 6, 'incorrecto': 14, 'requiere_adjudicacion': 24}
- **auditoría (base correcto) — final: {'correcto': 2, 'parcial': 1}**; vías {'unanime': 3}
- auditoría — flips descendentes: 1 / 3 (tasa 0.3333); sin flip 2; pendientes 0; re-corridas individuales no-correcto 3 / 9

## Veredictos finales por par (id opaco base)

| id_opaco_base | tipo | votos r1/r2/r3 | final | vía | flip |
|---|---|---|---|---|---|
| EV2R-03d3f8c3cc | parcial_disparado | parc/corr/parc | parcial | mayoria_2_de_3 | - |
| EV2R-06ecdefdcf | parcial_disparado | parc/inco/inco | incorrecto | mayoria_2_de_3 | - |
| EV2R-0860d0b8a5 | parcial_disparado | ADJ/ADJ/ADJ | requiere_adjudicacion | pendiente_de_adjudicacion | - |
| EV2R-0f4b9c4a38 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-19e7bd328b | parcial_disparado | inco/inco/inco | incorrecto | unanime | - |
| EV2R-1a818dddae | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-1c6a868ded | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-21c1a0b617 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-27b1161a7e | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-2a85163d83 | parcial_disparado | parc/parc/corr | parcial | mayoria_2_de_3 | - |
| EV2R-2e505e4272 | parcial_disparado | parc/inco/ADJ | requiere_adjudicacion | pendiente_de_adjudicacion | - |
| EV2R-3054a3d601 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-3e7ed08b34 | parcial_disparado | corr/corr/corr | correcto | unanime | - |
| EV2R-430cd763db | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-4847ade754 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-4b149f2b86 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-4e8b2a9f2a | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-4f697233b7 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-52ca117f6e | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-533f8ed556 | parcial_disparado | parc/parc/ADJ | parcial | invariante_con_pendiente | - |
| EV2R-534c224349 | parcial_disparado | corr/inco/ADJ | requiere_adjudicacion | pendiente_de_adjudicacion | - |
| EV2R-566d06d654 | parcial_disparado | ADJ/parc/ADJ | requiere_adjudicacion | pendiente_de_adjudicacion | - |
| EV2R-5744878e5b | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-58a7e9f2a1 | parcial_disparado | parc/inco/inco | incorrecto | mayoria_2_de_3 | - |
| EV2R-5a05f0ab37 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-5c2587d1f8 | parcial_disparado | parc/ADJ/parc | parcial | invariante_con_pendiente | - |
| EV2R-683b69a28b | parcial_disparado | ADJ/parc/parc | parcial | invariante_con_pendiente | - |
| EV2R-69881a8dc1 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-69c242f6e2 | parcial_disparado | ADJ/parc/parc | parcial | invariante_con_pendiente | - |
| EV2R-6ab1fd5859 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-6b605c05fc | parcial_disparado | parc/parc/inco | parcial | mayoria_2_de_3 | - |
| EV2R-6d8df11da2 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-6ef274ca11 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-757c889e2b | parcial_disparado | parc/parc/ADJ | parcial | invariante_con_pendiente | - |
| EV2R-76c070a6f7 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-788b326685 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-78c43e95b0 | auditoria_correcto | corr/corr/corr | correcto | unanime | sin_flip |
| EV2R-7ec4999f79 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-858b027be2 | parcial_disparado | inco/parc/inco | incorrecto | mayoria_2_de_3 | - |
| EV2R-86092f6789 | parcial_disparado | ADJ/ADJ/ADJ | requiere_adjudicacion | pendiente_de_adjudicacion | - |
| EV2R-87a4ca2cd5 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-893f855509 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-8cc2b9e117 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-9de0ed0463 | parcial_disparado | parc/parc/ADJ | parcial | invariante_con_pendiente | - |
| EV2R-aeb1d5a938 | parcial_disparado | ADJ/ADJ/parc | requiere_adjudicacion | pendiente_de_adjudicacion | - |
| EV2R-af7241e1b0 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-b018be139c | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-b9683442a7 | parcial_disparado | parc/parc/inco | parcial | mayoria_2_de_3 | - |
| EV2R-b9757343f9 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-bb1687163d | auditoria_correcto | corr/corr/corr | correcto | unanime | sin_flip |
| EV2R-bc430de596 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-bf64c7e08b | parcial_disparado | ADJ/parc/ADJ | requiere_adjudicacion | pendiente_de_adjudicacion | - |
| EV2R-c78b3683c5 | parcial_disparado | inco/parc/ADJ | requiere_adjudicacion | pendiente_de_adjudicacion | - |
| EV2R-cc098791f6 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-cc9fe3cb38 | parcial_disparado | ADJ/parc/parc | parcial | invariante_con_pendiente | - |
| EV2R-d25b8279f2 | parcial_disparado | parc/ADJ/ADJ | requiere_adjudicacion | pendiente_de_adjudicacion | - |
| EV2R-d4e1884cfe | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-d73c21b3c6 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-dacf6bf651 | auditoria_correcto | parc/parc/parc | parcial | unanime | flip |
| EV2R-de775a09d6 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-ea30d82507 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-eaad704270 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-ed1d57375f | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-f6fce759e0 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-f98cbe1614 | parcial_disparado | parc/parc/parc | parcial | unanime | - |
| EV2R-face86ba48 | parcial_disparado | parc/parc/parc | parcial | unanime | - |

Abreviaturas: corr=correcto, parc=parcial, inco=incorrecto, ADJ=requiere_adjudicacion.
