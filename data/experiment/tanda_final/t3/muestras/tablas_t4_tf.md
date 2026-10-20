#### Tabla T1. La población de cada muestra, por celda (`muestras/poblaciones_t4_t3f_tf.json`, 2026-10-20T14:08:23-03:00; `muestras/poblaciones_t4t1_tf.json`, 2026-10-20T14:08:26-03:00)

Grafo de las poblaciones de elementos del grafo: `data/experiment/reextraccion_v2/corpus_tanda_final/ens_98_r2b_sincola/r2/kg.json`, sha256 `c050f3c90ce5d32be759d2e5d05bbe2e131d9abf7811de097c97f4a1fe410cf7` (el mismo en los dos archivos: True). TOs por celda: RI:sin_raiz 20, RI:resto 4, NG:sin_raiz 6, NG:resto 68.

| muestra | elemento | N | RI:sin_raiz | RI:resto | NG:sin_raiz | NG:resto | se lee entera, sin celdas | sha256 de los ids por celda |
|---|---|---:|---:|---:|---:|---:|---|---|
| cola | unidad | 80 | 6 | 2 | 5 | 67 | False | `4ac193764d1a244c…` |
| aceptadas:items | unidad | 1.291 | 62 | 3 | 45 | 1.181 | False | `5a8e3408f0ef7787…` |
| aceptadas:no_items | unidad | 3.579 | 322 | 48 | 107 | 3.102 | False | `26d4c308dfe7aa66…` |
| vigilancia:2 | unidad | 292 | 98 | 2 | 5 | 187 | False | `6e0f1219abc26fa3…` |
| vigilancia:7 | arista | 6 | 1 | 0 | 0 | 5 | True | `ad2bdaf66d74c992…` |
| vigilancia:1 | nodo Condicion | 2.192 | 105 | 17 | 59 | 2.011 | False | `04031cfaadc9153e…` |
| vigilancia:3 | grupo de nodos | 220 | 12 | 5 | 3 | 200 | False | `2d0bcce25e21c7a2…` |
| observacion:12 | arista | 24.949 | 1.657 | 481 | 766 | 22.045 | False | `bff8b9f8281fc5b5…` |

Unidades en `finales.jsonl`: 4.950; la cola, 80; las aceptadas (los tres estados juntos), 4.870. Partes por corte de E1: 0. La (12), contra las aristas de extracción de la (10) del mismo grafo: {'universo': 24949, 'obs10_extraccion': 24949, 'igual': True}. La (3): 446 nodos en grupos, por tamaño {'2': 215, '3': 4, '4': 1}.

#### Tabla T2. Cuántos se sortean por celda, y lo que se declara (`celdas_t4_t3f.asignar`, sin cambios)

| muestra | RI:sin_raiz | RI:resto | NG:sin_raiz | NG:resto | total | notas |
|---|---:|---:|---:|---:|---:|---|
| cola | 6 | 2 | 5 | 17 | 30 | la clase RI tiene 8 de su cuota de 15: entran todos; faltan 7, que salen de la otra clase: 2 a NG:sin_raiz y 5 a NG:resto; la celda NG:sin_raiz tiene 5 de su cuota de 7: entran todos; NG:resto sortea 2 más |
| aceptadas:items | 12 | 3 | 5 | 10 | 30 | la celda RI:resto tiene 3 de su cuota de 5: entran todos; RI:sin_raiz sortea 2 más |
| aceptadas:no_items | 10 | 5 | 5 | 10 | 30 | — |
| vigilancia:2 | 13 | 2 | 5 | 10 | 30 | la celda RI:resto tiene 2 de su cuota de 5: entran todos; RI:sin_raiz sortea 3 más |
| vigilancia:7 | 1 | 0 | 0 | 5 | 6 | 6 elementos: se lee entera, sin celdas |
| vigilancia:1 | 10 | 5 | 5 | 10 | 30 | — |
| vigilancia:3 | 10 | 5 | 3 | 12 | 30 | la celda NG:sin_raiz tiene 3 de su cuota de 5: entran todos; NG:resto sortea 2 más |
| observacion:12 | 10 | 5 | 5 | 10 | 30 | — |

#### Tabla T3. Los pesos reales por celda (w_c = N_c / N de la población de cada muestra)

| muestra | RI:sin_raiz | RI:resto | NG:sin_raiz | NG:resto |
|---|---:|---:|---:|---:|
| aceptadas:items | 0,0480 | 0,0023 | 0,0349 | 0,9148 |
| aceptadas:no_items | 0,0900 | 0,0134 | 0,0299 | 0,8667 |
| cola | 0,0750 | 0,0250 | 0,0625 | 0,8375 |
| vigilancia:1 | 0,0479 | 0,0078 | 0,0269 | 0,9174 |
| vigilancia:2 | 0,3356 | 0,0068 | 0,0171 | 0,6404 |
| vigilancia:3 | 0,0545 | 0,0227 | 0,0136 | 0,9091 |
| vigilancia:7 | 0,1667 | 0,0000 | 0,0000 | 0,8333 |
| observacion:12 | 0,0664 | 0,0193 | 0,0307 | 0,8836 |
| proyección de la E0 de la tanda 1 (script de la mesa) | 0,0903 | 0,0477 | 0,0286 | 0,8334 |

#### Tabla T4. Los umbrales, con los pesos reales (`muestras/umbrales_t4_tf.json`) y la proyección

| estrato | n efectivo | atención desde (p) | freno por intervalos desde | atención sobre las 60 desde | errores en una sola celda para la atención |
|---|---:|---|---:|---:|---|
| items (reales) | 11,888 | 0,390 (0,0493) | 0,648 | 0,340 | RI:sin_raiz no alcanza sola, RI:resto no alcanza sola, NG:sin_raiz no alcanza sola, NG:resto 5 de 10 |
| items (proyección) | 14,105 | 0,380 (0,0493) | 0,626 | 0,330 | RI:sin_raiz no alcanza sola, RI:resto no alcanza sola, NG:sin_raiz no alcanza sola, NG:resto 5 de 10 |
| no_items (reales) | 13,133 | 0,290 (0,0498) | 0,544 | 0,244 | RI:sin_raiz no alcanza sola, RI:resto no alcanza sola, NG:sin_raiz no alcanza sola, NG:resto 4 de 10 |
| no_items (proyección) | 14,105 | 0,286 (0,0497) | 0,535 | 0,242 | RI:sin_raiz no alcanza sola, RI:resto no alcanza sola, NG:sin_raiz no alcanza sola, NG:resto 4 de 10 |

- **La tasa bajo H0** de cada estrato es la del script de la mesa (la de la tanda 0): items 6 de 30; no_items 4 de 30. Los dos momentos del §6 se juntan en uno: la atención propia de RI y la atención y el freno de cada estrato se calculan acá, antes de leer nada, porque T2 siguió de corrido y nada se leyó al cerrar el tramo 1.
- **Tasa ponderada total:** n efectivo 21,260 (proyección 27,572); pesos de los estratos ítems 0,2651 y no ítems 0,7349.
- **Atención de RI** (435 unidades RI aceptadas): salta desde una tasa ponderada de RI de 0,292 (p 0,0494); bajo H0, 0,1433; n efectivo 16,967; potencia con la tasa de RI duplicada 0,4677. Proyección: 0,278, 0,1616, 29,301 y 0,6940.
- **La cola, regla del 25 %:** n efectivo 23,100; límite superior de Wilson con 0 errores 0,1426; con 1 error en cada celda sola: RI:sin_raiz 0,1632, RI:resto 0,1632, NG:sin_raiz 0,1632, NG:resto 0,2175. Bases: tanda 0, 12 de 30, Wilson [0,246; 0,577] (reext_t0/t4/salida/tasas_t4.json); tanda 1, 14 de 30 con las dudosas como error; ponderada 0,4386, Wilson de Kish [0,2751; 0,6166]; la regla del 25 % se dispara (valores_huecos_tanda_final_mesa.json, T4.cola).
- **Los controles:** la importación del script de la mesa reproduce su JSON byte a byte: True; las tres cuentas con los pesos proyectados dan sus cifras: True.
- **La línea de base informativa, el T4 de la tanda 1** (`preregistro/valores_huecos_tanda_final_mesa.json`; no decide nada): aceptadas_items: 9 de 30 con las dudosas como error; ponderada 0,2196, Wilson de Kish [0,0784; 0,4822]; atención: no; freno: no; aceptadas_no_items: 3 de 30 con las dudosas como error; ponderada 0,0968, Wilson de Kish [0,0214; 0,3446]; atención: no; freno: no; ponderada_total: 0,1397, Wilson de Kish [0,0532; 0,3196]; atencion_RI: 7 de 30; ponderada de RI 0,1747; la atención no salta; cola: 14 de 30 con las dudosas como error; ponderada 0,4386, Wilson de Kish [0,2751; 0,6166]; la regla del 25 % se dispara; vigilancias_y_12: (1) 3 sí de 30; (2) 15 vaciamientos de 30; (3) 9 duplicaciones de 30; (7) 2 sin apoyo de 4; (12) 27 correctas de 30, Wilson [0,7438; 0,9654].

#### Tabla T5. Los sorteos (base `0897d609…`; igual al sha256 de la versión para firmar, de `5289b02f`: True)

| muestra | archivo | elementos | sha256 | hora |
|---|---|---:|---|---|
| cola | `muestras/cola.json` | 30 | `4d447ca82b8355354c9e5a07b063fac57f0fa7716de167cc547abf479f0bcf93` | 2026-10-20T14:08:58-03:00 |
| aceptadas:items | `muestras/aceptadas_items.json` | 30 | `396f332812db8fd35d9878f2366eda529e1b535db4ecaf7d360d63622737799e` | 2026-10-20T14:08:58-03:00 |
| aceptadas:no_items | `muestras/aceptadas_no_items.json` | 30 | `51bb8fd036bf4043c31b33be64fdd49d0d659f2fac2c909a24d72693409aa52c` | 2026-10-20T14:08:58-03:00 |
| vigilancia:2 | `muestras/vigilancia_2.json` | 30 | `da9849b0e9bae17a31e438339c05175ee0b4c6df179b89ec2af48a96313e3836` | 2026-10-20T14:08:58-03:00 |
| vigilancia:7 | `muestras/vigilancia_7.json` | 6 | `deb59743ab54ef13a3fb46285176dd3822d3b222adedadc83569cd6a9d55fefc` | 2026-10-20T14:08:58-03:00 |
| vigilancia:1 | `muestras/vigilancia_1.json` | 30 | `1ec9d44f355998c0bc4016c33770797093cc19fbc5093f487ad74c310c1e5f02` | 2026-10-20T14:08:58-03:00 |
| vigilancia:3 | `muestras/vigilancia_3.json` | 30 | `2b0d361b36345a0b85c64cced7fa259ba1df2d121f188ad8dbb1b11f695fb988` | 2026-10-20T14:08:58-03:00 |
| observacion:12 | `muestras/observacion_12.json` | 30 | `646587039a469880e7180fd43ca1ecb58569198fce61af07154082583a60b79e` | 2026-10-20T14:08:58-03:00 |

#### Tabla T6. El material (`muestras/material/`; 2026-10-20T14:09:10-03:00 y 2026-10-20T14:09:15-03:00)

| muestra | fichas | fichas (.jsonl) | fichas (.md) | planilla (.csv) |
|---|---:|---|---|---|
| cola | 30 | `75d630203b133c42…` | `0162485750338baf…` | `82e0bfa6255e0205…` |
| aceptadas:items | 30 | `5f88b8873ee835bd…` | `49c851c82e8659be…` | `790ab0df18dfee36…` |
| aceptadas:no_items | 30 | `d02a69ada432d571…` | `214f1d0281e0bc5c…` | `4e287d230cda2871…` |
| vigilancia:2 | 30 | `8fd6edef58918df4…` | `19646b7604853de6…` | `7ca27022841b18e3…` |
| vigilancia:7 | 6 | `bf50365e5d580d4f…` | `78bda5be873efed0…` | `82025c4850a615b0…` |
| vigilancia:1 | 30 | `7d106d37a2287505…` | `40d80848c676c03d…` | `e6581ab4b6a88833…` |
| vigilancia:3 | 30 | `f10de8fe8bbefb27…` | `18e98b027ab0984a…` | `11bc3414c939be43…` |
| observacion:12 | 30 | `bc38f9dd7e89c6be…` | `fed5c7e75cfb67ca…` | `4d5b3fc5ff64097f…` |

El control del material de (1), (3) y (12): {"fichas": 90, "claves_vedadas": 0, "texto_de": {"e0": 90}, "sin_texto": 0, "estado_en_los_md": 0}.

#### Tabla T7. Las unidades a la vista (`muestras/unidades_a_la_vista_T4.json`, 2026-10-20T14:09:45-03:00)

| muestra | fichas | unidades a la vista | por versión | con la regla 1.1 de la tanda 1 (información) |
|---|---:|---:|---|---:|
| cola | 30 | 30 | {'primera': 30} | 30 |
| aceptadas:items | 30 | 1.949 | {'final': 1949} | 33 |
| aceptadas:no_items | 30 | 1.917 | {'final': 1917} | 33 |
| vigilancia:2 | 30 | 978 | {'final': 978} | 30 |
| vigilancia:7 | 6 | 237 | {'final': 237} | 6 |
| vigilancia:1 | 30 | 1.469 | {'final': 1469} | 43 |
| vigilancia:3 | 30 | 27 | {'final': 27} | 27 |
| observacion:12 | 30 | 1.695 | {'final': 1695} | 29 |
| todas | — | 3.695 | {'primera': 30, 'final': 3665} | 224 |
