### Tabla 0. El acumulado y el lote de cadenas (`acumulado/armado_acumulado_t3.json`, `acumulado/manifiestos/`, `corridas/lote_t3_rc.json`)

- Armado: {'tos': 30, 'tanda0': 10, 'tanda1': 20, 'archivos_e0': 150, 'archivos_entrada': 557, 'todos_iguales_al_origen': True}; manifiesto de extracción `f6086c25ef41537ea32bf9ebfa507699fabcfa918411fa7e5f7223f902458622`; orígenes: {'tanda0': '72d84607', 'tanda1': '818a62cf'}.
- `acumulado_ens_treinta_r2b.json`: 30 TOs, 10 con `nombres_remision`; la variante con la raya da 8 distintas en el contraste del acumulado; regla: v2, sin la raya.
- `acumulado_ens_treinta_r2b_sincola.json`: 30 TOs, 10 con `nombres_remision`; la variante con la raya da 8 distintas en el contraste del acumulado; regla: v2, sin la raya.
- Lote de cadenas: 14 corridas, códigos de salida [0].

### Tabla 1. Los cuatro grafos y su doble corrida (`salidas/doble_corrida_t3.json`)

| grafo | carpeta | nodos | aristas | sha256 del kg.json (corrida 1 = corrida 2) | archivos | distintos | doble corrida interna |
|---|---|---:|---:|---|---:|---|---|
| KG-Tanda1-Veinte-r2b | `data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b` | 12731 | 31478 | `22e83a62cb88e5bbe31b64a0f2322194bc2ffd2622ea7adc2c07310d8a02c7c7` = | 56 / 56 | reporte_ensamblado_r2.json (igual con las rutas normalizadas: True) | [True, True] |
| KG-Tanda1-Veinte-r2b-sincola | `data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b_sincola` | 12452 | 28320 | `384a6d5bc139cd7b74d86840c68e7034b7a9bcb4bc26da7c61567f3f053e624e` = | 56 / 56 | reporte_ensamblado_r2.json (igual con las rutas normalizadas: True) | [True, True] |
| KG-Acumulado-Tandas0y1-r2b | `data/experiment/tanda1/t3/acumulado/ens_treinta_r2b` | 21409 | 60227 | `e63536d15bd8f575f1b7680921e3ca0d4956bdc5e38dc3f2fea27bb67bd71769` = | 76 / 76 | reporte_ensamblado_r2.json (igual con las rutas normalizadas: True) | [True, True] |
| KG-Acumulado-Tandas0y1-r2b-sincola | `data/experiment/tanda1/t3/acumulado/ens_treinta_r2b_sincola` | 20833 | 55358 | `0435d41f9c7b45ea10cc87e8121fcfb8b3d2b089af837fff377a3460ced9636c` = | 76 / 76 | reporte_ensamblado_r2.json (igual con las rutas normalizadas: True) | [True, True] |

### Tabla 2. Reproducibilidad (`salidas/doble_corrida_t3.json`, `cadenas`)

| cadena | sha256 del kg.json | esperado | igual | doble corrida interna |
|---|---|---|---|---|
| r2a_diez | `70d51e429b0e2cc1aafa697e32bc83462d371dfdd5edafb34e92fe4f7be45bdd` | `70d51e42` | True | True |
| r2a_desarrollo | `fa4c1043d859081e49dce6cb940a9f5d4c09fc6d449efb85355f95312257178a` | `fa4c1043` | True | True |
| r2b_diez | `fda6c07dbb95602f5992f7e1ad9bf148ff1c2a72b9f69ff2ebbce891c15740ea` | `fda6c07dbb95602f5992f7e1ad9bf148ff1c2a72b9f69ff2ebbce891c15740ea` | True | True |
| r2b_desarrollo | `acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31` | `acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31` | True | True |
| r2b_sincola_diez | `61dd1b69ba03e40499845c40a6a8bec4c22d892ebe95823c7d5a569110f08738` | `61dd1b69ba03e40499845c40a6a8bec4c22d892ebe95823c7d5a569110f08738` | True | True |
| r2b_sincola_desarrollo | `66e745f57397ab754cde09eb641e9f0d9ef6259ea7e6445d086ecbf1c36dcc6c` | `66e745f57397ab754cde09eb641e9f0d9ef6259ea7e6445d086ecbf1c36dcc6c` | True | True |

Veredicto del control: OK.

### Tabla 3. Shapes (perfil r2, fase r2b; `salidas/tablas_gate_t3.json`)

| grafo | E0 | veredicto | PASS / FAIL / WARN | bloqueantes en FAIL | no PASS | S31 |
|---|---|---|---|---|---|---|
| veinte | la del grafo | NO PASA | 21 / 3 / 4 | S31 | S31 FAIL, S7 FAIL, S8 WARN, S11 WARN, S12 FAIL, S21 WARN, S23 WARN | 11581 aristas remite_a: {'chunk_no_encontrado': 3415, 'en_un_tramo_del_chunk_de_la_arista': 8166}; 3415 violaciones. |
| veinte | con las partes (informativa) | PASA | 22 / 2 / 4 | — | S7 FAIL, S8 WARN, S11 WARN, S12 FAIL, S21 WARN, S23 WARN | 11581 aristas remite_a: {'en_un_tramo_del_chunk_de_la_arista': 11581}; 0 violaciones. |
| veinte_sincola | la del grafo | NO PASA | 21 / 3 / 4 | S31 | S31 FAIL, S7 FAIL, S8 WARN, S11 WARN, S12 FAIL, S21 WARN, S23 WARN | 8838 aristas remite_a: {'chunk_no_encontrado': 977, 'en_un_tramo_del_chunk_de_la_arista': 7861}; 977 violaciones. |
| veinte_sincola | con las partes (informativa) | PASA | 22 / 2 / 4 | — | S7 FAIL, S8 WARN, S11 WARN, S12 FAIL, S21 WARN, S23 WARN | 8838 aristas remite_a: {'en_un_tramo_del_chunk_de_la_arista': 8838}; 0 violaciones. |
| acumulado | la del grafo | NO PASA | 21 / 3 / 4 | S31 | S31 FAIL, S7 FAIL, S8 WARN, S11 WARN, S12 FAIL, S21 WARN, S23 WARN | 26258 aristas remite_a: {'chunk_no_encontrado': 3419, 'en_un_tramo_del_chunk_de_la_arista': 22839}; 3419 violaciones. |
| acumulado | con las partes (informativa) | PASA | 22 / 2 / 4 | — | S7 FAIL, S8 WARN, S11 WARN, S12 FAIL, S21 WARN, S23 WARN | 26258 aristas remite_a: {'en_un_tramo_del_chunk_de_la_arista': 26258}; 0 violaciones. |
| acumulado_sincola | la del grafo | NO PASA | 21 / 3 / 4 | S31 | S31 FAIL, S7 FAIL, S8 WARN, S11 WARN, S12 FAIL, S21 WARN, S23 WARN | 22277 aristas remite_a: {'chunk_no_encontrado': 981, 'en_un_tramo_del_chunk_de_la_arista': 21296}; 981 violaciones. |
| acumulado_sincola | con las partes (informativa) | PASA | 22 / 2 / 4 | — | S7 FAIL, S8 WARN, S11 WARN, S12 FAIL, S21 WARN, S23 WARN | 22277 aristas remite_a: {'en_un_tramo_del_chunk_de_la_arista': 22277}; 0 violaciones. |

El grafo anterior (KG-Tanda0-Diez-r2b-rs1): PASA, {'PASS': 22, 'FAIL': 2, 'WARN': 4}, no PASS S7 FAIL, S8 WARN, S11 WARN, S12 FAIL, S21 WARN, S23 WARN; S31: 13232 aristas remite_a: {'en_un_tramo_del_chunk_de_la_arista': 13232}; 0 violaciones..

### Tabla 3b. La causa de S31: `remite_a` con el chunk de procedencia fuera de la E0 del grafo (`salidas/causa_s31_t3.json`)

| grafo | remite_a | fuera de la E0 | todas de partes por corte | por chunk |
|---|---:|---:|---|---|
| veinte | 11581 | 3415 | True | `ri_rml::Sbloque14::parte1` 1198, `ri_rml::Sbloque14::parte2` 942, `ri_rml::Sbloque14::parte4` 1240, `ri_rml::Sbloque14::parte5` 35 |
| veinte_sincola | 8838 | 977 | True | `ri_rml::Sbloque14::parte2` 942, `ri_rml::Sbloque14::parte5` 35 |
| acumulado | 26258 | 3419 | True | `ri_rml::Sbloque14::parte1` 1198, `ri_rml::Sbloque14::parte2` 942, `ri_rml::Sbloque14::parte3` 4, `ri_rml::Sbloque14::parte4` 1240, `ri_rml::Sbloque14::parte5` 35 |
| acumulado_sincola | 22277 | 981 | True | `ri_rml::Sbloque14::parte2` 942, `ri_rml::Sbloque14::parte3` 4, `ri_rml::Sbloque14::parte5` 35 |
| tanda0_diez_rs1 | 13232 | 0 | True | — |
| tanda0_diez_sincola_rs1 | 12251 | 0 | True | — |

### Tabla 4. La suite (perfil r2, generación 3; `salidas/tablas_gate_t3.json` y `salidas/clasificacion_regresiones_t3.json`)

| grafo | entrada | resuelto / persiste / no aplica | regresiones | declaradas | no declaradas, también en el acumulado | no declaradas, solo sin los TOs de la tanda 0 |
|---|---|---|---:|---:|---:|---:|
| veinte | KG-Tanda1-Veinte-r2b | 31 / 16 / 21 | 20 | 3 | 2 | 15 |
| veinte_sincola | KG-Tanda1-Veinte-r2b-sincola | 31 / 16 / 21 | 20 | 3 | 2 | 15 |
| acumulado | KG-Acumulado-Tandas0y1-r2b | 46 / 13 / 9 | 5 | 3 | 2 | 0 |
| acumulado_sincola | KG-Acumulado-Tandas0y1-r2b-sincola | 46 / 13 / 9 | 5 | 3 | 2 | 0 |

El grafo anterior (KG-Tanda0-Diez-r2b-rs1): 48 / 11 / 9.

### Tabla 5. Las regresiones no declaradas (`salidas/clasificacion_regresiones_t3.json`)

| ítem | esperado → medido | clase | en los acumulados | detalle (de la tanda 1 sola) |
|---|---|---|---|---|
| BKL-0001 | resuelto → no_aplicable | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | el grafo no tiene nodos anclados en Capitales Mínimos |
| BKL-0002 | resuelto → no_aplicable | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | el grafo no tiene nodos anclados en Exterior y Cambios |
| BKL-0005 | resuelto → no_aplicable | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | sin portador: ninguna Obligacion anclada en ric 7.1 con «para el cálculo del importe correspondiente al mes n» |
| BKL-0006 | resuelto → no_aplicable | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | sin Restriccion anclada en cap 1.2 con un monto de la tabla del 1.2 en la lista de umbrales |
| BKL-0023 | resuelto → no_aplicable | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | sin Restriccion anclada en cap 1.2 con un monto de la tabla del 1.2 en la lista de umbrales, ni de compañías financieras ni de bancos |
| EJ-cla-5.1.1.1 | resuelto → no_aplicable | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | sin nodos de contenido anclados en cla 5.1.1.1 |
| ID-alta_gerencia | resuelto → no_aplicable | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | BKL-0034: el grafo no tiene nodos del TO de las anclas de la lectura (['lingob']); la entrada se lee contra esos chunks |
| ID-comite_de_auditoria | resuelto → no_aplicable | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | BKL-0034: el grafo no tiene nodos del TO de las anclas de la lectura (['lingob']); la entrada se lee contra esos chunks |
| ID-directorio | resuelto → no_aplicable | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | BKL-0034: el grafo no tiene nodos del TO de las anclas de la lectura (['lingob']); la entrada se lee contra esos chunks |
| RT-C7-1 | resuelto → no_aplicable | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | RT-C7-1: sin portador del 7.1 (Obligacion con «para el cálculo del importe correspondiente al mes n») |
| RT-C7-2 | resuelto → no_aplicable | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | RT-C7-2: sin portador del 7.1 (Obligacion con «para el cálculo del importe correspondiente al mes n») |
| RT-C7-3 | resuelto → no_aplicable | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | RT-C7-3: sin portador del 7.1 (Obligacion con «para el cálculo del importe correspondiente al mes n») |
| T1 | resuelto → persiste | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | anclados_3_9=0 puntos=[] con_usd_200=0 |
| T2 | resuelto → persiste | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | nodos_separados_ext=0 puntos_distintos=[] |
| T3 | resuelto → persiste | no declarada, solo sin los TOs de la tanda 0 | acumulado resuelto, acumulado_sincola resuelto | anclados_1_1_2_5=0 con_salvedad=0 de_los_cuales_excepcion=0 |
| E4-a1 | resuelto → persiste | no declarada, también en el acumulado | acumulado persiste, acumulado_sincola persiste | propuestos=284 con candidato label_exacto=1 resolubles no resueltos=1 [('Sujeto_propuesto_proveedores_de_servicios_de_pago', 'Sujeto_proveedor_de_servicios_de_p |
| E4-a4 | resuelto → persiste | no declarada, también en el acumulado | acumulado persiste, acumulado_sincola persiste | propuestos=284 con candidato label_singularizado=2 resolubles no resueltos=2 [('Sujeto_propuesto_camaras_electronicas_de_compensacion', 'Sujeto_camara_electroni |

### Tabla 6. Selftests (`selftests/`)

| selftest | rc | última línea |
|---|---|---|
| catalogo_unico | rc=1 | derivar_catalogo_r2.FrenoDerivacion: no se pudo leer 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30. |
| catalogo_unico_en_clon_git | rc=0 | selftest U-CAT-UNICO: 60/60 PASS |
| clave_cache | rc=0 | VEREDICTO: OK |
| e0 | rc=0 | SELFTEST: 251/251 PASS |
| ensamblado_omisiones | rc=0 | SELFTEST ENSAMBLADO U-OMISIONES-COD: 38/38 PASS |
| fin | sin rc |  |
| metrica_condiciones | rc=0 | SELFTEST METRICA I: 3/3 PASS |
| pyd_r2 | rc=0 | TOTAL: 409/409 |
| r3 | rc=0 | SELFTEST R3: 160/160 PASS |
| regression_kg_1 | rc=0 | selftest_regression_kg: 184/184 casos OK |
| regression_kg_2 | rc=0 | selftest_regression_kg: 184/184 casos OK |
| shapes_congelado | rc=0 | vocabulario: <SCRATCHPAD>/t3/clon_selftests/data/experiment/esq/code/prompt_congelado.py (sha256 prefijo e69fe |

`selftest_clave_cache_t3.json`: veredicto OK.

### Tabla 7. Intrínsecas de generación 3, informativas (`intrinsecas_gen3/`)

| grafo | E0 | rc | M4 grado medio | M9 nodos aislados | M10 chunks mudos |
|---|---|---|---:|---:|---|
| KG-Tanda1-Veinte-r2b | e0_del_grafo | rc=1 | — | — | — (RuntimeError: Atribución gen 3 inválida: 5 chunk_id de provenances no existen en E0 (primeros: ['ri_rml::Sbloque14::part) |
| KG-Tanda1-Veinte-r2b-sincola | e0_del_grafo | rc=1 | — | — | — (RuntimeError: Atribución gen 3 inválida: 3 chunk_id de provenances no existen en E0 (primeros: ['ri_rml::Sbloque14::part) |
| KG-Acumulado-Tandas0y1-r2b | e0_del_grafo | rc=1 | — | — | — (RuntimeError: Atribución gen 3 inválida: 7 chunk_id de provenances no existen en E0 (primeros: ['cap::4.2.1.2::parte1', ) |
| KG-Acumulado-Tandas0y1-r2b-sincola | e0_del_grafo | rc=1 | — | — | — (RuntimeError: Atribución gen 3 inválida: 4 chunk_id de provenances no existen en E0 (primeros: ['cap::4.2.1.2::parte2', ) |
| KG-Tanda1-Veinte-r2b | con_partes | rc=0 | 4.945095 | 16 | 0 / 3294 |
| KG-Tanda1-Veinte-r2b-sincola | con_partes | rc=0 | 4.548667 | 16 | 42 / 3294 |
| KG-Acumulado-Tandas0y1-r2b | con_partes | rc=0 | 5.626325 | 23 | 0 / 5734 |
| KG-Acumulado-Tandas0y1-r2b-sincola | con_partes | rc=0 | 5.314453 | 23 | 111 / 5734 |

### Tabla 8. Contadores de E1 (`salidas/contadores_e1_t3.json`)

Total de los 20 TOs: {'tipo_obligacion_requisito_de_estructura': 0, 'tipo_obligacion_normalizados': 1}. TOs con algún valor distinto de 0: ['lingeef'].
