#### Tabla E1. Los ocho ensamblados (`salidas/doble_corrida_tf.json`, `salidas/comprimir_kg_tf.json`; el lote, `corridas/lote_t3_tf_rc.json`: 28 corridas, rc distinto de 0 en 0, de 10:10:59 a 11:13:06; el del tramo 1 con la raya, `corridas/lote_t3_tf_tramo1_raya_rc.json`: 2 corridas, rc distinto de 0 en 0, de 13:53:25 a 13:53:56)

| grafo | carpeta | TOs | nodos | aristas | `kg.json` (bytes) | sha256 del `kg.json` | dos corridas iguales | doble corrida interna | minutos (corrida 1, 2) |
|---|---|---:|---:|---:|---:|---|---|---|---|
| KG-Acumulado-Tandas0y1yFinal-r2b | `data/experiment/tanda_final/t3/acumulado/ens_128_r2b` | 128 | 38.324 | 114.925 | 220.599.822 | `c43d66e503c2b27477cd17a5ffc2c64b6334d9525f0524d82ff248f04e7d96ac` | True | True | 25,8, 24,4 |
| KG-Acumulado-Tandas0y1yFinal-r2b-sincola | `data/experiment/tanda_final/t3/acumulado/ens_128_r2b_sincola` | 128 | 37.321 | 104.279 | 197.955.473 | `398459a853590c584398243b543548d5634124d5577b3cfffe4332f0a61ac0fd` | True | True | 23,4, 22,1 |
| KG-TandaFinal-r2b | `data/experiment/reextraccion_v2/corpus_tanda_final/ens_98_r2b` | 98 | 17.025 | 46.273 | 86.155.155 | `db2df7b7e707ef191d1df6fdb3638fd920cf4486afce13a7e889b9755155bc97` | True | True | 5,3, 5,2 |
| KG-TandaFinal-r2b-sincola | `data/experiment/reextraccion_v2/corpus_tanda_final/ens_98_r2b_sincola` | 98 | 16.598 | 43.392 | 80.314.222 | `c050f3c90ce5d32be759d2e5d05bbe2e131d9abf7811de097c97f4a1fe410cf7` | True | True | 5,1, 5,1 |
| KG-Acumulado-Tandas0y1yTramo1-r2b | `data/experiment/tanda_final/t3/acumulado/ens_60_tramo1_r2b` | 60 | 23.671 | 67.006 | 132.598.843 | `87ea32c503cd79bcf537a5d259527f4a50ccf00dc40a682ea9abc200b8d6ce50` | True | True | 11,2, 10,7 |
| KG-Acumulado-Tandas0y1yTramo1-r2b-sincola | `data/experiment/tanda_final/t3/acumulado/ens_60_tramo1_r2b_sincola` | 60 | 22.930 | 59.354 | 115.837.346 | `4ec19d46f23b80866866e132d6d367b88f9f83c12856abba36536ad06dd9d32d` | True | True | 10,2, 9,2 |
| KG-TandaFinal-Tramo1-r2b | `data/experiment/reextraccion_v2/corpus_tanda_final/ens_tramo1_r2b` | 30 | 2.372 | 4.066 | 8.233.790 | `f064d4e00b41246525d3c30a88f33b3ba9672c5e02cc10a36a4fa18dc88b940c` | True | True | 0,5, 0,5 |
| KG-TandaFinal-Tramo1-r2b-sincola | `data/experiment/reextraccion_v2/corpus_tanda_final/ens_tramo1_r2b_sincola` | 30 | 2.207 | 3.822 | 7.595.198 | `bbda74cda7e071e27782b41b06d7557e2c153e8afff7ea3f6540bdd520c3615f` | True | True | 0,5, 0,4 |

En cada grafo, los archivos de las dos corridas son byte a byte iguales salvo `reporte_ensamblado_r2.json`, que guarda la ruta de su `--salida` y las de la raíz donde corrió; con esas rutas normalizadas, también es igual (KG-Acumulado-Tandas0y1yFinal-r2b True, KG-Acumulado-Tandas0y1yFinal-r2b-sincola True, KG-TandaFinal-r2b True, KG-TandaFinal-r2b-sincola True, KG-Acumulado-Tandas0y1yTramo1-r2b True, KG-Acumulado-Tandas0y1yTramo1-r2b-sincola True, KG-TandaFinal-Tramo1-r2b True, KG-TandaFinal-Tramo1-r2b-sincola True).

#### Tabla E2. Los `kg.json` de más de 100 MB (100.000.000 bytes), comprimidos con `scripts/kg_gz.py`

| grafo | `kg.json` (bytes) | `.gz` (bytes) | sha256 del `.gz` | zlib | restaurado byte a byte | `verificar --kg` |
|---|---:|---:|---|---|---|---|
| KG-Acumulado-Tandas0y1yFinal-r2b | 220.599.822 | 14.220.901 | `6ae1738d1cc42b2ae4493d7d04a5bc97f54c2de6d8462860feccd7f7b58b5e60` | 1.2.13 | True | rc 0 |
| KG-Acumulado-Tandas0y1yFinal-r2b-sincola | 197.955.473 | 13.311.612 | `72b20d83263d4d30e695d84ae71cf60a5273abf0f216859064ef9f4842e2320d` | 1.2.13 | True | rc 0 |
| KG-Acumulado-Tandas0y1yTramo1-r2b | 132.598.843 | 8.482.700 | `796662df0e29c02095e4240ffeae7d29c6c63295372ef2e8315de9cb10c50c2f` | 1.2.13 | True | rc 0 |
| KG-Acumulado-Tandas0y1yTramo1-r2b-sincola | 115.837.346 | 7.826.322 | `2bc477bc372c3c62de938d10c482fe192863bbe95ab31acca4d3e4fcd2a7f431` | 1.2.13 | True | rc 0 |

Los demás quedan sin comprimir: KG-TandaFinal-r2b (86.155.155 bytes), KG-TandaFinal-r2b-sincola (80.314.222 bytes), KG-TandaFinal-Tramo1-r2b (8.233.790 bytes), KG-TandaFinal-Tramo1-r2b-sincola (7.595.198 bytes). Ningún otro archivo de los ensamblados pasa de 50 MB. Manda el sha256 del `kg.json` sin comprimir (tabla E1); el sello de cada `.gz` lo repite.

#### Tabla E3. La reproducibilidad de los sellados (`salidas/doble_corrida_tf.json`, `cadenas`)

| cadena | sha256 del `kg.json` | sello | igual | doble corrida interna |
|---|---|---|---|---|
| r2a_diez | `70d51e429b0e2cc1aafa697e32bc83462d371dfdd5edafb34e92fe4f7be45bdd` | `70d51e42…` | True | True |
| r2a_desarrollo | `fa4c1043d859081e49dce6cb940a9f5d4c09fc6d449efb85355f95312257178a` | `fa4c1043…` | True | True |
| r2b_diez | `fda6c07dbb95602f5992f7e1ad9bf148ff1c2a72b9f69ff2ebbce891c15740ea` | `fda6c07dbb95602f…` | True | True |
| r2b_desarrollo | `acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31` | `acb26dca0885e9ea…` | True | True |
| r2b_sincola_diez | `61dd1b69ba03e40499845c40a6a8bec4c22d892ebe95823c7d5a569110f08738` | `61dd1b69ba03e404…` | True | True |
| r2b_sincola_desarrollo | `66e745f57397ab754cde09eb641e9f0d9ef6259ea7e6445d086ecbf1c36dcc6c` | `66e745f57397ab75…` | True | True |
| t1_veinte | `22e83a62cb88e5bbe31b64a0f2322194bc2ffd2622ea7adc2c07310d8a02c7c7` | `22e83a62cb88e5bb…` | True | True |
| t1_veinte_sincola | `384a6d5bc139cd7b74d86840c68e7034b7a9bcb4bc26da7c61567f3f053e624e` | `384a6d5bc139cd7b…` | True | True |
| acum_treinta | `e63536d15bd8f575f1b7680921e3ca0d4956bdc5e38dc3f2fea27bb67bd71769` | `e63536d15bd8f575…` | True | True |
| acum_treinta_sincola | `0435d41f9c7b45ea10cc87e8121fcfb8b3d2b089af837fff377a3460ced9636c` | `0435d41f9c7b45ea…` | True | True |

Los sellos: los seis de la tanda 0 de `resellado_t0/FRENO_resellado_T0.md:68-71` (las dos r2a, por su prefijo) y los cuatro de la tanda 1 de `tanda1/t3/FRENO_T3.md:32-35`.

#### Tabla E4. El tramo 1 con la raya contra la variante con los manifiestos de T1, y el acumulado de 60 contra la prueba de la mesa

- **KG-TandaFinal-Tramo1-r2b** (con la raya, la que rige) contra la variante con los manifiestos de T1 (la del FRENO parcial): `kg.json` igual: True (`f064d4e00b412465…`); archivos distintos: reporte_ensamblado_r2.json; TOs con `nombres_remision` distintos entre los dos manifiestos: 23. La variante de T1, en sus dos corridas: `kg.json` igual True, distintos reporte_ensamblado_r2.json.
- **KG-TandaFinal-Tramo1-r2b-sincola** (con la raya, la que rige) contra la variante con los manifiestos de T1 (la del FRENO parcial): `kg.json` igual: True (`bbda74cda7e071e2…`); archivos distintos: reporte_ensamblado_r2.json; TOs con `nombres_remision` distintos entre los dos manifiestos: 23. La variante de T1, en sus dos corridas: `kg.json` igual True, distintos reporte_ensamblado_r2.json.
- **KG-Acumulado-Tandas0y1yTramo1-r2b**: 23.671 nodos y 67.006 aristas; la mesa (registro, §43), 23.671 y 67.006: igual True.
- **KG-Acumulado-Tandas0y1yTramo1-r2b-sincola**: 22.930 nodos y 59.354 aristas; la mesa (registro, §43), 22.930 y 59.354: igual True.
- Los `nombres_remision` del manifiesto de T3 contra los de los manifiestos que usó la mesa (`data/experiment/tanda1/t3/acumulado/manifiestos/acumulado_ens_treinta_r2b.json`, `data/experiment/tanda_final/t1/ensamblado/manifiestos/tanda_final_ens_tramo1_r2b.json`): 60 TOs, 60 en los de la mesa, 0 distintos.

#### Tabla E5. El armado de los acumulados (`acumulado/armado_acumulado_<n>_tf.json`)

| acumulado | TOs (0 / 1 / final) | archivos de la E0 | archivos de la entrada | bytes de la entrada | todos iguales al origen | manifiesto de extracción |
|---|---|---:|---:|---:|---|---|
| 128 | 128 (10 / 20 / 98) | 640 | 2.295 | 530.323.665 | True | `7a17222c1579cd02…` |
| 60 | 60 (10 / 20 / 30) | 300 | 1.073 | 327.469.149 | True | `a2ef5e64478bdad2…` |

La entrada combinada se registra solo por su total de archivos, sus bytes y el sha256 de su lista (cegamiento, punto 8): no va al repo, porque es la salida de la extracción por copia.
