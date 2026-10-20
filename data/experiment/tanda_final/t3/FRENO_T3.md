# FRENO T3 — tanda final de B6.1: los ocho ensamblados, el gate (pasa con las decisiones de la autora), el registro y Neo4j, lo contado sin leer y la preparación de T4 (USD 0, sin API, sin commit)

Rigen el pre-registro de la tanda final FIRMADO (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`, con sus notas posteriores en
`27bfaeb5` y `86541475`), sus §2, §5, §6, §7 y §8 y la precisión de la firma, lo del pre-registro de la tanda 1 que este no reemplaza, el
«seguí» de T3 con sus tres correcciones y las cinco decisiones de la autora sobre el FRENO T3 parcial (sección 2), que mandan sobre el
«seguí». HEAD `eb5ad14b`. El FRENO parcial queda como `t3/FRENO_T3_parcial.md` (`f7abf9da…`), sin cambios. Toda cifra de este FRENO sale
de un script de `t3/scripts/` y de su salida; la sección 12 los lista.

**Resultado:**
- **Los ocho ensamblados** (punto 3) salen con rc 0 en las 30 corridas de los dos lotes, la doble corrida de cada uno da el mismo
  `kg.json`, los diez grafos sellados de las tandas 0 y 1 se reproducen byte a byte y el acumulado con el tramo 1 da las cifras de la prueba
  de la mesa (tablas E1 a E5). El tramo 1 va con la variante con la raya (decisión 2); su `kg.json` es el de la variante de T1.
- **El gate** (punto 4) **pasa**, con las decisiones de la §29 y la R23 y la V23 del selftest de claves declaradas no aplicables después de
  T2 (decisión 1): shapes pasa en los ocho con la E0 con las partes; la suite da 0 regresiones no declaradas que cuenten; los selftests de la
  cadena dan rc 0; sin la R23 y la V23, el de claves es igual a A3 en todo lo demás.
- **El registro y Neo4j** (punto 5): dos entradas nuevas en `grafos.py` y el registro de la vista; los dos grafos de la tanda, cargados con
  el envoltorio en memoria, con el gate 5 OK, la paridad 147 de 147 y 0 nodos con la marca de la cola en el sin cola. El cargador no cambió.
- **Lo contado sin leer** (punto 6): tablas C1 a C4, con la tanda 1 y la tanda 0 al lado, y la columna «Tanda final» del tablero.
- **La preparación de T4** (punto 7): las ocho muestras en dos corridas iguales; la cola, 30 = las 13 del tramo 1 enteras y 17 de
  NG resto; la versión derivada de la lectura, sin ningún `⟦T4.`.
- Nada commiteado y ningún mensaje de commit preparado.

## 1. Paso 0 (20/10/2026, desde las 10:02:13) y el control del comienzo de esta parte (13:51:19)

La salida, tal cual, con la carpeta personal como `$HOME` y el scratchpad como `<SCRATCHPAD>`.

```
2026-10-20 10:02:13 -0300
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
main
--- log -4
eb5ad14b Registro de decisiones y tripletas: un predicado con la definicion del prefijo, un caso resuelto de prohibicion fuera de la muestra, el piloto como sensibilidad y la herramienta de puntos sin recortar su texto
b17746be Tanda final: la extraccion de sus noventa y ocho documentos
257641e5 Registro de decisiones y tripletas: la ultima tanda extraida, lo pago de a uno, la cobertura de la validacion antes de la evaluacion final y un caso del pool corregido
98edf948 Tripletas: el juez de precision de la etapa de validacion antes de su primera corrida, con la calibracion fuera de muestra, y los lotes de esa etapa
--- show --stat HEAD
eb5ad14b Registro de decisiones y tripletas: un predicado con la definicion del prefijo, un caso resuelto de prohibicion fuera de la muestra, el piloto como sensibilidad y la herramienta de puntos sin recortar su texto

 docs/preregistro_evaluacion_tripletas.md           | 17 +++++++++++
 ...o_decisiones_calidad_y_evaluacion_2026-10-15.md | 33 ++++++++++++++++++++++
 2 files changed, 50 insertions(+)
--- status
--- untracked tanda_final/corpus
--- pgrep
pgrep_rc=1
--- 78 rutas
sello: data/experiment/tanda_final/preregistro/codigo_de_la_cadena_c66c7ecd_mesa.json (n declarado = 78, commit = c66c7ecdfae0d1b47cc5cbc4b4c43c18aede9fa9)
rutas leídas: 78
HEAD:  78 de 78
árbol: 78 de 78
rc=0
40de829cfd08b97192944c9e445da8003f6b22e34c6fd45a0ecd5d22dcf4958f  data/experiment/tanda_final/preregistro/codigo_de_la_cadena_c66c7ecd_mesa.json
```

La versión derivada de T1, regenerada con el completador sobre el pre-registro de `4de7f2a7` (`git show` al scratchpad), y las entradas
en HEAD (los cuatro manifiestos de ensamblado de T1 y la E0 de los 98):

```
b760edf7d341290ad910de993f8a868be426abcf2cfd14459240ad5a2b940cc2
completo hasta T1: 7 huecos; esperan 7; derivada_T1.md sha256 e6ee519a63e9004318bfa9718ca9e5db8e8b452fabbc477dae607dd3321f1f61
md igual
huecos igual
huecos JSON del árbol = HEAD
--- entradas en HEAD
igual 109985bba8bb830f78a92cf5a8f7f664581bee39098127c68e9ab184163df87b  data/experiment/tanda_final/t1/ensamblado/manifiestos/tanda_final_ens_98_r2b.json
igual 4a71bfe59ba98c3baf5394fb60f35e5ba190f71ab24ce1321445273a84ab15c0  data/experiment/tanda_final/t1/ensamblado/manifiestos/tanda_final_ens_98_r2b_sincola.json
igual 2a248f894053efe2fb3ce8fd7899387f3373562842c76d66e650a963f7e15fb0  data/experiment/tanda_final/t1/ensamblado/manifiestos/tanda_final_ens_tramo1_r2b.json
igual 08db5092025e61cfcfd3d35f1e78f4b77bc454f12d452e9ba1980463e91e5262  data/experiment/tanda_final/t1/ensamblado/manifiestos/tanda_final_ens_tramo1_r2b_sincola.json
E0 de los 98: 498 de 498 iguales en HEAD y en el árbol
499
```

Docker y el volumen de Neo4j del repo (por tamaño y fecha, contra la foto de después de T2), y la foto del repo antes, con la cuenta de los
`.pyc`:

```
29.3.1 Docker Desktop
foto de después de T2: 2026-10-20 00:12:30 | entradas del volumen: 229 | hoy: 229 | mismos tamaños: True | con fecha posterior a la foto: 0
2026-10-20 10:03:14 -0300
2026-10-20 10:03:25 2026-10-20 10:03:40 55309 entradas
   11236
cae4486fbd1f2a42bc9daa6641bf58d5ac690d6058b32e637a121b3b782b0187
eb5ad14b
ok
```

En la foto de antes: sus horas y sus entradas, la cuenta de los `.pyc`, el sha256 de la foto, el commit de HEAD y la escritura del
checkpoint. La salida de las entradas en HEAD termina con la cuenta de los renglones OK de `t1/sha256_para_T2.txt`.

Al empezar esta parte, después de las decisiones sobre el FRENO parcial: el estado del repo, los procesos, la foto contra la de después del
parcial y Docker (los dos renglones de `pgrep` son de un proceso que no lancé yo, que escribe fuera del repo; no lo toqué):

```
2026-10-20 13:51:19
eb5ad14b Registro de decisiones y tripletas: un predicado con la definicion del prefijo, u
b17746be Tanda final: la extraccion de sus noventa y ocho documentos
257641e5 Registro de decisiones y tripletas: la ultima tanda extraida, lo pago de a uno, l
 M scripts/regression_kg_esperado.json
86954: ensamblar_tanda0.py que no lancé yo, con --salida en ~/INGENIERIA IA/TESIS/fuera_del_repo/remisiones_subpuntos/… (renglón de pgrep, acortado)
86957: ensamblar_tanda0.py que no lancé yo, con --salida en ~/INGENIERIA IA/TESIS/fuera_del_repo/remisiones_subpuntos/… (renglón de pgrep, acortado)
pgrep rc=0
2026-10-20 13:51:19 2026-10-20 13:51:38 57890 entradas
desde la foto de después del parcial: nuevos 2 borrados 0 cambiados 0
nuevos: ['data/experiment/tanda_final/t3/FRENO_T3.md', 'data/experiment/tanda_final/t3/resumen_fotos_T3.json']
cambiados: []
29.3.1 Docker Desktop contenedores corriendo 3
```

## 2. Lo decidido sobre el FRENO parcial y cómo lo apliqué

1. **El selftest de claves.** La R23 del perfil r2b y la V23 del sellado quedan declaradas no aplicables después de T2: su TO ya se extrajo y
   su clave está en la caché, no por el código de la clave. El gate se juzga sin ellas, con todo lo demás igual a A3. Lo comprobé por script
   (`diagnostico_clave_cache_tf.py`, sección 4.4): los campos que difieren de A3 son de la R23 o derivan de ella, y la fila del contraste que
   difiere es la F17 (de R23). No toqué el selftest.
2. **Los manifiestos del tramo 1:** la variante con la raya, por la regla de la §19 y la enmienda 9, punto 8, que nombra el pre-registro
   (§7). **Se declara que el «seguí» decía los manifiestos de T1.** Los dos grafos del tramo 1 se ensamblaron de nuevo con los manifiestos de
   la raya (`t3/prueba_raya_tramo1/manifiestos/`, la carpeta de la prueba del parcial, que pasan a regir): la primera corrida, en la carpeta
   final; la segunda es la de la prueba de la raya del parcial. El `kg.json` es el mismo que con los de T1 (tabla E4). Rehíce lo que depende
   del manifiesto: el gate del tramo 1 (shapes, byte a byte igual; en la suite solo cambia la ruta del manifiesto que nombra T6), sus
   intrínsecas (las mismas métricas) y la medición de los nombres (los cuatro manifiestos siguen la §19).
3. **El derivador adaptado del acumulado de 60** queda, declarado, con mi medición al lado de las cifras de la mesa (sección 3.1).
4. **Los umbrales del punto 7.3:** los del script de la mesa, importado sin cambios, con su tasa base, la de la tanda 0, como dice el §6. Las
   cifras del T4 de la tanda 1 van al lado como línea de base informativa (tabla T4 y `umbrales_t4_tf.json`).
5. **`unidades_a_la_vista_T4.json`:** la regla del «seguí», con la del T4 de la tanda 1 al lado (tabla T7).

Las tres correcciones del «seguí» siguen: las poblaciones de los elementos del grafo, sobre `ens_98_r2b_sincola` (su ruta y su sha256, en la
tabla T1); el mecanismo de (1), (3) y la (12), el del T4 de la tanda 1 (`poblaciones_t4t1_tf.py` y `sorteos_t4t1_tf.py`); y la cola, en 30,
con las 13 del tramo 1 enteras y 17 de NG resto (tabla T2).

## 3. Los ocho ensamblados (punto 3)

El mecanismo es el del T3 de la tanda 1, copiado y adaptado en `t3/scripts/`: `armar_acumulados_tf.py` arma por copia la E0 y la entrada
de los dos acumulados en una copia del repo (la del `rsync` del «seguí», con 0 nombres vedados y 0 enlaces); `cadena_t3_tf.sh` corre
`ensamblar_tanda0.py` con los argumentos de las corridas del T3 de la tanda 1; `correr_lote_t3_tf.py` corre las cadenas; `doble_corrida_tf.py`
compara. La tanda va con los manifiestos de T1; el tramo 1, con los de la raya; los dos, con `--entrada
data/experiment/reextraccion_v2/corpus_tanda_final/salida_r2b` y la E0 de los 98. La unidad con error de T2
(`ri_transpa::Sbloque1::chapeau_seccion`) falta en los grafos, como decidió la autora (registro, §44): no la toqué.

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

### 3.1 Los `nombres_remision` de los ensamblados nuevos, medidos (§7; registro, §19; enmienda 9, punto 8)

`medir_nombres_t3_tf.py` es la medición de la mesa (`nombres_remision/medir_nombres_remision_mesa.py`) con los cuatro corpus nuevos; el
contraste y el resumen son los de la mesa, sin cambios. Todo corrió sobre la copia. `tabla_nombres_t3_tf.py` pone las cifras de la mesa al
lado (las del 16/10/2026 del repo, y las de la enmienda 9, punto 8, `756a0394:81-84`, para el tramo 1 y el acumulado de 60):

| ensamblado | TOs | menciones | resueltas, regla | resueltas, raya | distintas, regla | distintas, raya | la raya entra (§19) | en el manifiesto | la mesa (menciones / regla / raya / distintas con la raya) | igual |
|---|---:|---:|---:|---:|---:|---:|---|---|---|---|
| KG-TandaFinal-r2b (y su sin cola) | 98 | 804 | 389 | 413 | 0 | 3 | no | regla, 31 TOs con nombres | 804 / 389 / 413 / 3 (data/experiment/nombres_remision/medicion/ (16/10/2026)) | sí |
| KG-TandaFinal-Tramo1-r2b (y su sin cola) | 30 | 309 | 1 | 1 | 0 | 0 | sí | regla con la raya, 25 TOs con nombres | 309 / 1 / 1 / 0 (756a0394, enmienda 9, punto 8, líneas 81 a 84 (17/10/2026)) | sí |
| KG-Acumulado-Tandas0y1yFinal-r2b (y su sin cola) | 128 | 1608 | 1279 | 1319 | 0 | 0 | sí | regla con la raya, 50 TOs con nombres | 1608 / 1279 / 1319 / 0 (data/experiment/nombres_remision/medicion/ (16/10/2026)) | sí |
| KG-Acumulado-Tandas0y1yTramo1-r2b (y su sin cola) | 60 | 1113 | 429 | 455 | 0 | 23 | no | regla, 35 TOs con nombres | 1113 / 429 / 455 / 23 (756a0394, enmienda 9, punto 8, líneas 81 a 84 (17/10/2026)) | sí |

Iguales a la mesa en los cuatro: True; la variante de cada manifiesto sigue la §19 en los cuatro:
True. El manifiesto del acumulado de 128 lo derivó `derivar_manifiesto_ensamblado_mesa.py` con el
contraste de la mesa. Para el de 60, ese derivador frena porque la medición del repo no tiene un corpus con esos TOs: lo derivé con
`derivar_manifiesto_ensamblado_tf.py`, que hace lo mismo con la variante que da la fuente que se le pasa (`756a0394:83-84`: 23 distintas, la
raya no entra) y escribe esa fuente en la `descripcion` (decisión 3). La medición de arriba da la misma cifra.

## 4. El gate (punto 4)

Sobre la copia del repo, con las decisiones del gate de la tanda 1 (registro, §29) y la decisión 1. Los `--out` van a `t3/gate/` (el
«seguí» lo pide así; en la tanda 1 fueron a las carpetas de los ensamblados).

#### Tabla V0. La E0 con las partes por corte (`gate_decisiones/e0_partes_tf.json`)

| E0 | archivos | dos corridas iguales | unidades reemplazadas por sus partes | sha256 del conjunto |
|---|---:|---|---:|---|
| tanda_final | 498 | True | 0 | `fa6cc1c0dfc2517135ddf5fd693a04a3eb5cbd400f6e6304c443f80f945f6bb1` |
| acum128 | 640 | True | 2 | `8c2471dd2b486e4505646acb7898889006ebafb1ad9a45bd891352325a111567` |
| acum60 | 300 | True | 2 | `4b0831fc022799a4d3ddba4e4d492bbf0be238af46fb582e321daef74d9053d7` |

Controles: la de la tanda final es la E0 del repo: True; en los acumulados, los archivos de las tandas 0 y 1 son los de la E0 con las partes del acumulado de la tanda 1 y los de la tanda final, los de la suya: acum128 150 y 490 archivos, True; acum60 150 y 150 archivos, True.

#### Tabla V1. El veredicto del gate por grafo

| grafo | shapes, E0 con las partes (rige) | shapes, E0 del grafo (informada) | suite: resuelto / persiste / no aplica | regresiones | declaradas (laudo) | declaradas (§29) | fuera del grafo | no declaradas que cuentan |
|---|---|---|---|---:|---:|---:|---:|---|
| KG-TandaFinal-r2b | PASA (22 / 2 / 4) | PASA (22 / 2 / 4) | 33 / 14 / 21 | 18 | 3 | 0 | 18 | 0 |
| KG-TandaFinal-r2b-sincola | PASA (22 / 2 / 4) | PASA (22 / 2 / 4) | 33 / 14 / 21 | 18 | 3 | 0 | 18 | 0 |
| KG-TandaFinal-Tramo1-r2b | PASA (22 / 2 / 4) | PASA (22 / 2 / 4) | 33 / 14 / 21 | 18 | 3 | 0 | 18 | 0 |
| KG-TandaFinal-Tramo1-r2b-sincola | PASA (22 / 2 / 4) | PASA (22 / 2 / 4) | 33 / 14 / 21 | 18 | 3 | 0 | 18 | 0 |
| KG-Acumulado-Tandas0y1yFinal-r2b | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 46 / 13 / 9 | 5 | 3 | 2 | — (no se aplica) | 0 |
| KG-Acumulado-Tandas0y1yFinal-r2b-sincola | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 46 / 13 / 9 | 5 | 3 | 2 | — (no se aplica) | 0 |
| KG-Acumulado-Tandas0y1yTramo1-r2b | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 46 / 13 / 9 | 5 | 3 | 2 | — (no se aplica) | 0 |
| KG-Acumulado-Tandas0y1yTramo1-r2b-sincola | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 46 / 13 / 9 | 5 | 3 | 2 | — (no se aplica) | 0 |

Las columnas de shapes dan PASS / FAIL / WARN; los FAIL que no bloquean, por grafo, están en `tablas_gate_tf.json` (`no_pass`). «Fuera del grafo» cuenta las regresiones con todas sus anclas en TOs que el grafo no tiene; en los acumulados no se aplica (§29). La entrada de la fixture contra la que se mide cada grafo es la suya (las ocho nuevas heredan las expectativas de la tanda 1).
- **KG-TandaFinal-r2b, «fuera del grafo»:** 18 regresiones; de los 68 ítems, 29 fuera del grafo, 38 generales y 1 en el grafo. Cruce con acum128: 15 y 15 ítems, iguales: True.
- **KG-TandaFinal-r2b-sincola, «fuera del grafo»:** 18 regresiones; de los 68 ítems, 29 fuera del grafo, 38 generales y 1 en el grafo. Cruce con acum128_sincola: 15 y 15 ítems, iguales: True.
- **KG-TandaFinal-Tramo1-r2b, «fuera del grafo»:** 18 regresiones; de los 68 ítems, 30 fuera del grafo, 38 generales y 0 en el grafo. Cruce con acum60: 15 y 15 ítems, iguales: True.
- **KG-TandaFinal-Tramo1-r2b-sincola, «fuera del grafo»:** 18 regresiones; de los 68 ítems, 30 fuera del grafo, 38 generales y 0 en el grafo. Cruce con acum60_sincola: 15 y 15 ítems, iguales: True.

#### Tabla V2. S31 con la E0 de cada grafo: la causa, por id (`gate_decisiones/causa_s31_tf.json`)

| grafo | `remite_a` | con su chunk fuera de la E0 del grafo | todos son partes por corte |
|---|---:|---:|---|
| KG-TandaFinal-r2b | 19076 | 0 | True |
| KG-TandaFinal-r2b-sincola | 16889 | 0 | True |
| KG-TandaFinal-Tramo1-r2b | 750 | 0 | True |
| KG-TandaFinal-Tramo1-r2b-sincola | 737 | 0 | True |
| KG-Acumulado-Tandas0y1yFinal-r2b | 53885 | 3528 | True |
| KG-Acumulado-Tandas0y1yFinal-r2b-sincola | 44821 | 997 | True |
| KG-Acumulado-Tandas0y1yTramo1-r2b | 29847 | 3435 | True |
| KG-Acumulado-Tandas0y1yTramo1-r2b-sincola | 23314 | 997 | True |

#### Tabla V3. La doble corrida, la reproducibilidad, la fixture, los selftests y lo informativo

- **La doble corrida** de los ocho: True; **la reproducibilidad**: 10 cadenas, todas iguales a su sello: True; veredicto OK (`salidas/doble_corrida_tf.json`).
- **La fixture** (`gate_decisiones/control_fixture_tf.json`): 4094 claves de HEAD, 0 quitadas y 0 cambiadas; 2272 claves nuevas, todas de las ocho entradas nuevas: True; veredicto OK.
- **Los selftests:** catalogo_unico rc=0, e0 rc=0, ensamblado_omisiones rc=0, metrica_condiciones rc=0, pyd_r2 rc=0, r3 rc=0, regression_kg_1 rc=0, regression_kg_2 rc=0, shapes_congelado rc=0. **El de claves**, sin las cuentas: no se lee: el JSON va a un NO_ABRIR_; sus dos salidas sin cuentas, byte a byte las de A3: False y False.
  - **La causa del de claves** (`gate_decisiones/diagnostico_clave_cache_tf.json`, sin abrir sus salidas): los 16 campos que difieren de A3 sin cuentas son de la variación del TO nuevo (`variacion_to_nuevo`, R23 en el perfil r2b) o derivan de ella: True. Supone que `snp_psp::1.3.1.1` no está en la caché de E1; `snp_psp` es de la tanda final (82.º de `orden_corrida`, tramo 2) y su chunk es el mismo en la E0 de la tanda final y en b584: True. La fila del contraste que difiere, filas[32]/observado[0]: F17 (R23), es la de R23: True. R23 supone que la unidad de un TO fuera de la tanda 0 no está en la caché de E1. T2 extrajo ese TO con el perfil r2b y el mismo chunk, así que la clave está y R23 deja de dar miss: el selftest falla por su supuesto, no por el código de la clave.
  - **Declaradas no aplicables después de T2** (decisión de la autora sobre el FRENO T3 parcial): la R23 del perfil r2b y la V23 del sellado. Sin ellas, todo lo demás del selftest es igual a A3 sin cuentas: True. El selftest no se tocó; el cambio de su TO lo hace la mesa aparte.
- **Las intrínsecas de generación 3, con la E0 con las partes (informativas):**
  - KG-TandaFinal-r2b: M4 5.435888, M9 34 nodos aislados, M10 1 / 4951.
  - KG-TandaFinal-r2b-sincola: M4 5.228582, M9 31 nodos aislados, M10 81 / 4951.
  - KG-TandaFinal-Tramo1-r2b: M4 3.428331, M9 13 nodos aislados, M10 1 / 601.
  - KG-TandaFinal-Tramo1-r2b-sincola: M4 3.463525, M9 13 nodos aislados, M10 14 / 601.
  - KG-Acumulado-Tandas0y1yFinal-r2b: M4 5.997547, M9 51 nodos aislados, M10 1 / 10685.
  - KG-Acumulado-Tandas0y1yFinal-r2b-sincola: M4 5.588221, M9 48 nodos aislados, M10 192 / 10685.
  - KG-Acumulado-Tandas0y1yTramo1-r2b: M4 5.661442, M9 25 nodos aislados, M10 1 / 6335.
  - KG-Acumulado-Tandas0y1yTramo1-r2b-sincola: M4 5.176973, M9 25 nodos aislados, M10 125 / 6335.
- **Los contadores de E1 (informativos):** {'tipo_obligacion_requisito_de_estructura': 0, 'tipo_obligacion_normalizados': 0}.
- **Los `nombres_remision` medidos** (`nombres_remision/tabla_nombres_t3_tf.json`): iguales a la medición de la mesa en los cuatro ensamblados: True; la variante en cada manifiesto sigue la §19: KG-TandaFinal-r2b True; KG-TandaFinal-Tramo1-r2b True; KG-Acumulado-Tandas0y1yFinal-r2b True; KG-Acumulado-Tandas0y1yTramo1-r2b True.

**Veredicto del gate, con las decisiones de la §29 y la R23 y la V23 declaradas: PASA.**

### 4.1 Shapes

- Con la E0 con las partes (`e0_partes_tf.py`, que corre `reext_t0/t3/e0_con_partes.py` sin cambios, dos veces por E0): pasa en los ocho.
  La tanda final no tuvo unidades partidas (su E0 con las partes es la E0 del repo: True); en los acumulados entran
  las partes de las tandas 0 y 1 (cap::4.2.1.2 en 2 partes, ri_rml::Sbloque14 en 5 partes).
- Con la E0 de cada grafo: S31 falla en 4 grafos, los acumulados, por las `remite_a` de las partes por corte de `ri_rml::Sbloque14`,
  de la tanda 1 (tabla V2). En los cuatro de la tanda final, S31 pasa también con la E0 del repo.
- El tramo 1 con la raya contra la variante de T1 (`comparar_gate_tramo1_tf.py`): shapes, byte a byte igual con las dos E0 (4 de
  4 carpetas); en la suite cambian solo `consola_suite.txt`, `suite_perfil_r2.json`, `suite_perfil_r2.md`, por la ruta del manifiesto que nombra T6.

### 4.2 La suite y la fixture

- **La fixture** (`editar_fixture_tf.py`, sobre la copia): ocho entradas nuevas al final de `estado_esperado`, copias de la entrada sellada
  del grafo anterior del mismo tipo de la tanda 1 (KG-Tanda1-Veinte-r2b para la tanda y el tramo 1; KG-Acumulado-Tandas0y1-r2b para los
  acumulados, completo o sin cola). El script controla que las expectativas de esas cuatro y de las dos de diez de la tanda 0 re-sellada son
  las mismas. El tramo 1 con la raya tiene el mismo `kg.json`, así que la fixture no cambió.
- **El control de la precisión de la firma, punto 3** (`control_fixture_tf.py`, contra `git show HEAD:`): 4.094 claves de HEAD,
  0 quitadas y 0 cambiadas; 2.272 claves nuevas, todas de las ocho entradas: True. Veredicto: OK.
- **El resultado:** en los acumulados, 5 regresiones en cada uno, las tres del laudo y E4-a1 y E4-a4, declaradas; en la tanda y en el
  tramo 1, 18 en cada uno, todas fuera del grafo (`fuera_del_grafo_tf.py`). El cruce: en los cuatro, las no declaradas fuera del
  grafo son las no declaradas que su acumulado no da (15 y 15 ítems, iguales: True).

### 4.3 La reproducibilidad, los selftests de la cadena, las intrínsecas y los contadores

Las tablas E3 y V3. Los selftests de la cadena corrieron sobre un clon APFS de la copia (`selftests_tf.sh`, con 0 nombres vedados y 0
enlaces). El del catálogo pide `git show 4ef7650:<ruta>` (`derivar_catalogo_r2.py:103`): corrió con `GIT_DIR` en el `.git` del repo y
`GIT_OPTIONAL_LOCKS=0`, en lugar del `git clone` del T3 de la tanda 1, que trajo archivos `.env` y `NO_ABRIR_` al clon. El sha256 de
`.git/index` y de `.git/HEAD` antes de los selftests y al cerrar el parcial (2026-10-20 13:03:22), por sus primeros 16 caracteres:
iguales, True. Las intrínsecas con la E0 de cada grafo corren en los cuatro de la tanda final y frenan solas en los cuatro acumulados
(«Atribución gen 3 inválida»: las partes por corte no están en esa E0), como en la tanda 1.

### 4.4 El selftest de claves: la R23 y la V23, declaradas

- **Cómo corrió:** `selftest_clave_cache --salida-r2b data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b`, como en A3 y en T1, sobre el
  clon, con su JSON y su consola a archivos que no abrí; `selftest_claves_sin_cuentas_tf.py` (el de T1 con los nombres de T3) les sacó las
  cuentas con `alcance_e1/a3/scripts/clave_cache_sin_cuentas_a3.py` y las comparó con las de A3 sin cuentas. Los sha256 de las dos
  originales:

```
a6272d3df1aaeea8de3f3a8a6dce958424fb242dd19a774e85b157328434e6a6  selftest_clave_cache_t3.json (original, con las cuentas; no se abre)
2d502351f8e2087299540519eeb505685c41961b7df0dda3eda2cdff3332db07  consola_selftest_clave_cache_t3.txt (original, con las cuentas; no se abre)
```

- **Lo que dio:** rc 1. Las dos salidas sin cuentas no son las de A3 (JSON igual: False; consola igual:
  False), así que el script las renombró a `NO_ABRIR_` y no las abrí. Las rutas de los 16 campos del JSON
  que difieren, sin valores: `/contraste_tabla/discrepancias[0]/fila`, `/contraste_tabla/discrepancias[0]/selftest[0]`, `/contraste_tabla/discrepancias[0]/selftest[1]`, `/contraste_tabla/discrepancias[0]/tabla[0]`, `/contraste_tabla/discrepancias[0]/tabla[1]`, `/contraste_tabla/discrepancias[0]/variacion`, `/contraste_tabla/estado`, `/contraste_tabla/filas[32]/observado[0]/coincide`, `/contraste_tabla/filas[32]/observado[0]/e1`, `/perfil_r2b/variaciones[30]/detalle/clave_en_cache_e1`, `/perfil_r2b/variaciones[30]/e1/observadas_que_cambian[0]`, `/perfil_r2b/variaciones[30]/e1/ok`, `/perfil_r2b/variaciones[30]/e1/token`, `/perfil_r2b/variaciones[30]/ok`, `/variaciones_con_discrepancia[0]`, `/veredicto`.
- **La causa** (`diagnostico_clave_cache_tf.py`, que lee solo esas rutas, el código del selftest y su tabla, el manifiesto de la tanda final
  y las dos E0; ni las salidas del selftest ni las bases de la caché):
  - todos esos campos son de la variación del TO nuevo o derivan de ella: True. Es `variacion_to_nuevo`, la única
    función del selftest con el campo `clave_en_cache_e1`: V23 en el perfil sellado y R23 en el r2b; la fila del contraste que difiere es la
    F17, de R23 (leída con `leer_tabla` y `RE_IDS_TABLA` del propio selftest);
  - supone que `snp_psp::1.3.1.1` (de la partición b584) no está en la caché de E1 (miss); `snp_psp` es de la tanda final
    (82.º de `orden_corrida`, tramo 2), y su chunk es el mismo en la E0 de la tanda final y en b584: True. T2 lo extrajo con el
    perfil r2b, así que la clave de R23 está en la caché;
  - en T1 el selftest dio OK (FRENO T1, §4.1) porque T2 todavía no había extraído ese TO. El código de la clave (`llm_cache.py`,
    `cliente_e1.py` y `cliente_e3.py`) está entre las 78 rutas, que el paso 0 dio iguales; el selftest no está entre ellas y es el de HEAD.
- **Con la decisión 1:** sin la R23 y la V23, todo lo demás es igual a A3: True. El cambio del TO de la variación lo hace la mesa
  aparte.
- **El cegamiento:** saber si una clave de E1 está en la base es un dato de la caché de E1; no di cuentas de claves ni nada de E3. Las dos
  salidas sin cuentas quedan como `NO_ABRIR_` en `t3/selftests/clave_cache/`, sin abrir; las dos originales, con las cuentas, quedan en el
  scratchpad, sin abrir, y van solo por su sha256.

## 5. El registro y Neo4j (punto 5)

- **`grafos.py`** (`editar_grafos_tf.py`, sobre la copia): dos entradas nuevas al final, `KG_TandaFinal_r2b` y `KG_TandaFinal_r2b_sincola`, con
  label, índice y `ev2_key` propios y `commit_sellado` «PENDIENTE»; el sha256, los nodos y las aristas salen de la doble corrida. Las selladas
  no cambian: el script controla el texto antes y después del ancla, y la corrida en seco, cada entrada sellada (15, iguales:
  True; solo dos nuevas: True).
- **El registro de la vista** (`t3/registro_vista_r2b_tanda_final.py`, con el patrón del de la tanda 1), con el desglose de «punto sin nodos»
  del sin cola recomputado; la cola de la tanda final para ese desglose: 80 unidades.
- **La corrida en seco** (`dry_registro_tf.py`, por el camino de imports del cargador, sin Neo4j): OK; en los dos, sha256
  verificado y la vista con los conteos del registro (KG_TandaFinal_r2b: 17.025 / 46.273; KG_TandaFinal_r2b_sincola: 16.598 / 43.392); el desglose,
  igual a lo declarado: True.
- **El cargador** (`cargar_neo4j_tanda0.py`) acepta en `--grafo` solo las claves `KG_Tanda0_*`. Como en el T3 de la tanda 1 (pre-registro, §7),
  `cargar_neo4j_tf.py` lo importa sin editarlo, deja en memoria `CLAVES_TANDA0` con las dos claves de la tanda final y llama a su `main()`
  una vez por clave. Su sha256, antes y después de la carga, en el repo y en la copia: `e51a3a148e8d9f65…` y `e51a3a148e8d9f65…`; iguales: True.
  Las salidas heredan los rótulos de la tanda 0 (`carga_neo4j_tanda0.json`, «PARIDAD (tanda 0)»), que no se corrigen.
- **La carga** (`neo4j/<clave>/carga_neo4j_tanda0.json`), desde la copia:
  - KG_TandaFinal_r2b: sha256 verificado antes de cargar (True); 17.025 nodos y 46.273 aristas, 0 colgantes; dos cargas con la misma huella: True; `verificar_carga`: True; `KG_Meta.kg_sha256` igual al archivo: True, `commit_sellado` «PENDIENTE»; paridad 147/147; **gate 5: OK**.
  - KG_TandaFinal_r2b_sincola: sha256 verificado antes de cargar (True); 16.598 nodos y 43.392 aristas, 0 colgantes; dos cargas con la misma huella: True; `verificar_carga`: True; `KG_Meta.kg_sha256` igual al archivo: True, `commit_sellado` «PENDIENTE»; paridad 147/147; **gate 5: OK**.
- **El control de la cola** (`control_cola_neo4j_tf.py`, la copia del de la tanda 1 con las claves cambiadas): OK. En el sin cola,
  0 nodos con la marca en Neo4j y 0 en el `kg.json`; en el completo, llegan las 499 marcas de
  nodo del `kg.json` (499 en Neo4j).
- **Docker** (las consolas, en `neo4j/consolas/`). Al empezar respondía, con los contenedores de otro proyecto corriendo. Levanté el
  contenedor del repo con `docker compose up -d --wait` en `data/experiment/neo4j/` y, al terminar, lo detuve con `docker compose stop`. A
  diferencia de la tanda 1, no pedí el cierre de Docker: estaba corriendo antes y lo dejé como estaba. El contenedor del repo salió con el
  código 137 (`docker compose stop` lo terminó al pasar su espera), con la carga ya verificada. El arranque y el cierre:

```
# Arranque del contenedor del repo (2026-10-20 14:03:49)
$ docker compose up -d --wait   (en data/experiment/neo4j/)
 Container neo4j-bcra-kg-compose Starting 
 Container neo4j-bcra-kg-compose Started 
 Container neo4j-bcra-kg-compose Waiting 
 Container neo4j-bcra-kg-compose Healthy 
rc=0
fin 14:04:09
$ docker compose ps --format {{.Name}} {{.Status}}
neo4j-bcra-kg-compose Up 20 seconds (healthy)
```

```
# Cierre del contenedor del repo (2026-10-20 14:07:08)
$ docker compose stop   (en data/experiment/neo4j/)
 Container neo4j-bcra-kg-compose Stopping 
 Container neo4j-bcra-kg-compose Stopped 
rc=0
# Docker al cierre: queda como estaba antes de la carga (con los contenedores de otro proyecto)
$ docker compose ps -a --format {{.Name}} {{.Status}}
neo4j-bcra-kg-compose Exited (137) Less than a second ago
$ docker info --format {{.ServerVersion}} {{.ContainersRunning}}
29.3.1 3
$ docker ps --format {{.Names}} {{.Status}}
backend_notifications_db Up 28 hours
backend_users_db Up 28 hours
backend_friendships_app Restarting (1) 32 seconds ago
backend_friendships_db Up 28 hours
```

## 6. Lo que se cuenta sin leer (punto 6)

`contado_sin_leer_tf.py`, sobre la copia, es el del T3 de la tanda 1 con los grafos de la tanda final (la tanda y el acumulado de las tres,
completos y sin cola); importa sin editarlas las funciones de la tanda 0 y del re-sellado. La línea de base es la de la tanda 1 (su
`contado_sin_leer_t3f.json`, igual al de `eb0711a1`: True), con la de la tanda 0 al lado. Las cuentas bajo el cegamiento van a
`t3/NO_ABRIR_conteos_t3.json`, sin abrir: sha256 `9a830e053a13bdabbead5bbfe92b5fcc6351c7f2ee992aca0db1120cb1c93755`. La columna «Tanda final» del tablero está en
`t3/conteos_sin_leer/columna_tanda_final_tablero_tf.md`; el tablero del repo no se tocó.

#### Tabla C1. Observaciones (10) y (11) contra la tanda 1, con la tanda 0 re-sellada al lado

| grafo | unidades de E0 | (10) aristas de extracción | (10) por unidad | (11) `remite_a` entre documentos | menciones |
|---|---:|---:|---:|---:|---:|
| tanda final | 4.951 | 25.629 | 5,18 | 4.001 | 2.517 |
| tanda final sin cola | 4.951 | 24.949 | 5,04 | 2.520 | 2.408 |
| acumulado de las tres | 10.680 | 57.767 | 5,41 | 16.180 | 5.311 |
| acumulado de las tres sin cola | 10.680 | 56.297 | 5,27 | 10.236 | 5.117 |
| base de la tanda 1: tanda 1 | 3.290 | 18.887 | 5,74 | 1.541 | 1.272 |
| base de la tanda 1: tanda 1 sin cola | 3.290 | 18.483 | 5,62 | 299 | 1.224 |
| base de la tanda 1: acumulado de las tandas 0 y 1 | 5.729 | 32.138 | 5,61 | 3.628 | 2.783 |
| base de la tanda 1: acumulado de las tandas 0 y 1 sin cola | 5.729 | 31.348 | 5,47 | 2.061 | 2.698 |
| base re-sellada: diez | 2.439 | 13.251 | 5,43 | 642 | 1.510 |
| base re-sellada: desarrollo | 1.768 | 10.304 | 5,83 | 497 | 1.289 |

#### Tabla C2. Vigilancias (4), (5), (8) y (9) contra la tanda 1, con la tanda 0 re-sellada al lado

| grafo | (4) un TextoOrdenado por TO | (5) requisito_de_estructura / normalizados | (8) sujeto_propuesto / sujeto_id (tasa %) | (9) emisiones en E1 / aristas en el kg |
|---|---|---|---|---|
| tanda final | True | 0 / 0 | 579 / 5.365 (9,74) | 22 / 33 |
| tanda final sin cola | True | 0 / 0 | 579 / 5.365 (9,74) | 22 / 33 |
| acumulado de las tres | True | 0 / 1 | 1205 / 11.665 (9,36) | 29 / 59 |
| acumulado de las tres sin cola | True | 0 / 1 | 1205 / 11.665 (9,36) | 29 / 59 |
| base de la tanda 1: tanda 1 | True | 0 / 1 | 434 / 3.950 (9,90) | 7 / 20 |
| base de la tanda 1: tanda 1 sin cola | True | 0 / 1 | 434 / 3.950 (9,90) | 7 / 20 |
| base de la tanda 1: acumulado de las tandas 0 y 1 | True | 0 / 1 | 626 / 6.300 (9,04) | 7 / 27 |
| base de la tanda 1: acumulado de las tandas 0 y 1 sin cola | True | 0 / 1 | 626 / 6.300 (9,04) | 7 / 27 |
| base re-sellada: diez | True | 0 / 0 (los diez TOs) | 192 / 2.350 (7,55) | 0 (los diez TOs) / 8 |
| base re-sellada: desarrollo | True | 0 / 0 (los diez TOs) | 138 / 1.641 (7,76) | 0 (los diez TOs) / 8 |

#### Tabla C3. La cola, contra la de la tanda 1, con la tanda 0 re-sellada al lado

| grafo | cola | de unidades de E0 | % | por estado | aceptadas (los tres estados juntos) | en el grafo |
|---|---:|---:|---:|---|---:|---|
| tanda final | 80 | 4.951 | 1,6 | cola_humana 20, cola_humana_reextraccion_invalida 9, cola_humana_veredicto_inutilizable 51 | 4.870 | 499 nodos y 679 aristas con la marca |
| tanda final sin cola | 80 | 4.951 | 1,6 | cola_humana 20, cola_humana_reextraccion_invalida 9, cola_humana_veredicto_inutilizable 51 | 4.870 | 80 descartadas por el ensamblado |
| acumulado de las tres | 191 | 10.680 | 1,8 | cola_humana 63, cola_humana_reextraccion_invalida 13, cola_humana_veredicto_inutilizable 115 | 10.493 | 1123 nodos y 1472 aristas con la marca |
| acumulado de las tres sin cola | 191 | 10.680 | 1,8 | cola_humana 63, cola_humana_reextraccion_invalida 13, cola_humana_veredicto_inutilizable 115 | 10.493 | 191 descartadas por el ensamblado |
| base de la tanda 1: tanda 1 | 42 | 3.290 | 1,3 | cola_humana 18, cola_humana_reextraccion_invalida 2, cola_humana_veredicto_inutilizable 22 | 3.252 | — |
| base de la tanda 1: acumulado de las tandas 0 y 1 | 111 | 5.729 | 1,9 | cola_humana 43, cola_humana_reextraccion_invalida 4, cola_humana_veredicto_inutilizable 64 | 5.623 | — |
| base re-sellada (diez) | 69 | 2.439 | 2,8 | cola_humana 25, cola_humana_reextraccion_invalida 2, cola_humana_veredicto_inutilizable 42 | — | — |

El umbral de atención es 6 % (§5.4 b). Las unidades en `finales.jsonl` son tanda final 4.950, tanda final sin cola 4.950, acumulado de las tres 10.684, acumulado de las tres sin cola 10.684 (las partes por corte cuentan aparte); otros estados: tanda final ninguno, tanda final sin cola ninguno, acumulado de las tres ninguno, acumulado de las tres sin cola ninguno.

La cola por TO (tanda final): adfsp 1, afiltr 1, apnf 1, autenf 3, cateloc 3, cedin 1, cescar 2, consyr 2, cryl 1, ctavis 4, depinv 2, disres 3, evacre 1, fabcra 2, fimipyme 2, finsec 6, garopt 1, gescre 1, gracre 1, graloc 1, jafip 2, lavdin 1, pimf 1, prevmi 1, raapal 2, ratio 5, ratiofn 3, regpri 4, repefe 1, retype 1, ri_dsf 2, ri_iepsp 1, ri_ii_31_12_19 1, ri_msrl 2, ri_secoexpo 1, ri_tar 1, rmgcti 1, secfin 2, seggar 2, servco 1, snp_cec 3, snp_spd 1, tasint 1, traval 1.

#### Tabla C4. El catálogo al cierre (§5.5): claves con la mención verificada en cuarentena en 2 unidades o más

| registro | filas en cuarentena | verificadas | claves | claves con 2 unidades o más | en 2 TOs o más |
|---|---:|---:|---:|---:|---:|
| tanda final | 1088 | 956 | 303 | 45 | 19 |
| tanda final sin cola | 1055 | 924 | 297 | 43 | 19 |
| acumulado de las tres | 1939 | 1669 | 588 | 108 | 47 |
| acumulado de las tres sin cola | 1894 | 1626 | 577 | 105 | 47 |
| base de la tanda 1: tanda 1 | 703 | 570 | 237 | 38 | 8 |
| base de la tanda 1: tanda 1 sin cola | 693 | 561 | 233 | 37 | 8 |
| base de la tanda 1: acumulado de las tandas 0 y 1 | 851 | 713 | 320 | 56 | 13 |
| base de la tanda 1: acumulado de las tandas 0 y 1 sin cola | 839 | 702 | 315 | 54 | 12 |
| base de la tanda 0: diez (r2_1_medicion.json) | 164 | 145 | 87 | 14 | 1 |
| base de la tanda 0: diez_sincola (r2_1_medicion.json) | 162 | 143 | 85 | 14 | 1 |

Las claves y sus formas están en `contado_sin_leer_tf.json` (`catalogo_al_cierre`). Su lectura y aprobación es de la autora (enmienda 4, §1, punto 3); cuántas relaciones resuelve cada versión del catálogo se mide después de la re-resolución (punto 5).

Control de las funciones importadas: las del re-sellado sobre KG-Tanda0-Diez-r2b-rs1 contra su medición, True en las 11 filas controladas; las de este script sobre KG-Tanda1-Veinte-r2b-sincola contra la línea de base de la tanda 1, True en las 5 filas controladas. Los pozos de L-02 y L-04 no se miden: eran de la lectura de la tanda 1 (su pre-registro, §5.4 d).

## 7. La preparación de T4 (punto 7)

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

- **El control del material** (`control_material_tf.py`, con el de material_t4t1.py sobre las ocho muestras): claves del estado o de las marcas
  de E3, 0; fichas sin texto, 0; `.md` con «"estado», 0. No leí ninguna ficha.
- **La segunda corrida de los sorteos** (`muestras/segunda_corrida_de_los_sorteos/`) da las ocho muestras byte a byte iguales; los índices
  cambian solo en las horas.
- **La versión derivada de la lectura** (7.7), con el completador sobre el pre-registro de `4de7f2a7` y `--momento lectura_tramo1`: sin ningún
  `⟦T4.` (espera solo el hueco de T5), regenerada al final igual byte a byte. `preregistro/preregistro_tanda_final_derivada_T4.md`
  (`26c29d9424ffaf634a02735a972ad29e7df8b06463b8ad430654d50d4d442fc2`) y su `.huecos.json` (`4a17612bcf069beee9b00f513c6b69b7f4b0fa81b7ba590052f79d318b3862e4`).
- **Los dos momentos de lectura del §6 se juntan en uno**, porque T2 siguió de corrido y nada se leyó al cerrar el tramo 1: la atención propia
  de RI y la atención y el freno de cada estrato se calcularon acá, antes de leer nada. Va en lugar de la frase del §6 «se calculan después
  de leer las celdas del tramo 1».

## 8. El cegamiento (punto 8)

- No miré ni di el desglose de las aceptadas por estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3`
  ni el gasto de los reintentos. La cola y su composición por estado van en la tabla C3, como en la tanda 1.
- De la salida de la extracción, ninguna cuenta por tipo de archivo. La entrada de los acumulados se registra solo por su total de archivos,
  sus bytes y el sha256 de su lista (tabla E5). La E0 con las partes informa las unidades partidas por corte, que son de E1.
- Los `NO_ABRIR_` de esta unidad: `t3/NO_ABRIR_conteos_t3.json` y los dos del selftest de claves (sección 4.4). No abrí ninguno, ni ningún
  `.env`, ni ninguna carpeta vedada.

## 9. La foto del repo, los .pyc, lo escrito en el repo y el grep de convenciones

Lo genera `scripts/freno_tf_foto.py` desde la foto del paso 0 y la de después (`tanda_final/t1/foto_repo_tanda_final_t1.py`; las dos, fuera del repo y del paquete, porque nombran todas las rutas del repo; en el paquete van su sha256 y este resumen).

- **La foto.** Paso 0: 10:03:25 a 10:03:40 del 2026-10-20, 55.309 entradas. Después: 14:20:03 a 14:20:22 del 2026-10-20, 58.005 entradas, 45 sin abrir y 342 enlaces.
  - **2.712 nuevos:** 212 en `corpus_tanda_final/ens_98_r2b/`; 212 en `corpus_tanda_final/ens_98_r2b_sincola/`; 76 en `corpus_tanda_final/ens_tramo1_r2b/`; 76 en `corpus_tanda_final/ens_tramo1_r2b_sincola/`; 31 la base de Neo4j (neo4j/volumen/, fuera de git); 2 la versión derivada de la lectura; 3 en `tanda_final/t3/, lo demás`; 1.772 en `tanda_final/t3/acumulado/`; 5 en `tanda_final/t3/conteos_sin_leer/`; 36 en `tanda_final/t3/corridas/`; 6 en `tanda_final/t3/e0_con_partes/`; 74 en `tanda_final/t3/gate/`; 15 en `tanda_final/t3/gate_decisiones/`; 28 en `tanda_final/t3/intrinsecas_gen3/`; 66 en `tanda_final/t3/muestras/`; 16 en `tanda_final/t3/neo4j/`; 12 en `tanda_final/t3/nombres_remision/`; 2 en `tanda_final/t3/prueba_raya_tramo1/`; 8 en `tanda_final/t3/salidas/`; 46 en `tanda_final/t3/scripts/`; 14 en `tanda_final/t3/selftests/`.
  - **16 borrados:** 16 la base de Neo4j (neo4j/volumen/, fuera de git).
  - **71 cambiados:** 69 la base de Neo4j (neo4j/volumen/, fuera de git); 1 la fixture; 1 en `neo4j/grafos.py`.
  - **Fuera de lo admitido:** 0.
  - `scripts/regression_kg_esperado.json`: `574169f961c9cdd1…` (HEAD) → `496a03c9a6d959f0…`, de 261.887 a 399.453 bytes.
  - `data/experiment/neo4j/grafos.py`: `cec1ec717451f677…` (HEAD) → `c26fa5a78c5e88c7…`, de 19.048 a 21.395 bytes.
- **Los `.pyc`:** 11.236 líneas en el paso 0 y 11.236 después; listas iguales: True.

**El sha256 de los archivos clave, de la foto de después:**

| archivo | sha256 |
|---|---|
| `scripts/regression_kg_esperado.json` | `496a03c9a6d959f0d8d0b1ba961adae2e83d64df6431d1739025e7f494964aac` |
| `data/experiment/neo4j/grafos.py` | `c26fa5a78c5e88c75580c058b98889f0fdf7fa873abfc1a5f7574f29feb1e8c8` |
| `data/experiment/tanda_final/t3/registro_vista_r2b_tanda_final.py` | `4b83922e421177cc83b6cc3227b24a1126b90e9a4234ffd93cc0ee031f62cbc3` |
| `data/experiment/tanda_final/preregistro/preregistro_tanda_final_derivada_T4.md` | `26c29d9424ffaf634a02735a972ad29e7df8b06463b8ad430654d50d4d442fc2` |
| `data/experiment/tanda_final/preregistro/preregistro_tanda_final_derivada_T4.huecos.json` | `4a17612bcf069beee9b00f513c6b69b7f4b0fa81b7ba590052f79d318b3862e4` |

**Lo que se escribió en el repo** (`escribir_en_el_repo_tf.py`, desde un staging armado en el scratchpad; antes, cada ruta nueva no existía
y cada archivo que cambia era el de HEAD; después, cada archivo es byte a byte el del staging): ensamblados 2.350 nuevos, gate 186 nuevos y 1 que cambia, tramo1_raya 152 nuevos, gate2 193 nuevos, resto 91 nuevos y 1 que cambia, tablas_t4 2 nuevos;
escritos iguales al staging: 2.640 de 2.640. Lo del parcial que se reemplazó (el tramo 1 y las salidas del gate)
salió antes con `escribir_en_el_repo_tf.py apartar`, que controla que cada archivo sea el que se escribió y no esté en HEAD: tramo1_parcial 152 de 152, gate_parcial 186 de 186, tablas_t4 2 de 2; quedan en el
scratchpad. El FRENO parcial pasó a `t3/FRENO_T3_parcial.md`, con el mismo sha256. Escritos después de la foto de después: este FRENO y
`t3/resumen_fotos_T3.json`.

**El grep de convenciones** (`grep_convenciones_tf.py`, con `LC_ALL=en_US.UTF-8`; los tokens del nombre salen de `git config user.name`
en memoria y no quedan escritos; los términos, los del FRENO T1, §11), en dos grupos, sin los `NO_ABRIR_`:
- **Lo que redacté** (`t3/scripts/`, `t3/salidas/`, `t3/gate_decisiones/`, las tablas de lo contado y de T4, la tabla de los nombres, el
  registro de la vista, la fixture y `grafos.py`): 77 archivos; 8 renglones con coincidencias, en
  `freno_t3_armar_tf.py` (1) y `freno_t3_parcial_armar_tf.py` (1) y `grep_convenciones_tf.py` (4) y `FRENO_T3_parcial.md` (2), que escriben los términos del grep para buscarlos o
  describirlos; tokens del nombre fuera de rutas, 0. Rutas absolutas en `escribir_en_el_repo_tf.py` y `freno_t3_armar_tf.py` y `grep_convenciones_tf.py`,
  que las nombran en sus controles. El renglón de control (el primer token y «slack») da 2 coincidencias, una por término.
- **Lo que escribieron los generadores** (los ensamblados, la E0 combinada, shapes, la suite, las intrínsecas, los selftests, Neo4j, las
  muestras y su material y las consolas): 2.600 archivos de texto, con coincidencias en 224. Los términos son texto de las normas
  («correo» 5.670, «e-mail» 490, «pedido por» 147, «email» 60, «reunión con» 4). Los tokens del nombre: 72 dentro de rutas
  absolutas de la copia, que guardan los 8 `reporte_ensamblado_r2.json`, como los sellados de la tanda 1 (el otro archivo con
  `/private/tmp`, `preregistro_tanda_final_derivada_T4.md`, cita la frase del texto firmado que dice que nada queda ahí), y
  36 fuera de ellas, en 16 archivos que copian texto de las normas
  (`chunks_*`, `estructura_*`, `kg.json`, `omisiones.jsonl`, `tablas_*`). Nada de eso lo escribí yo.
- Sobre este FRENO el grep corre después de escribirlo; su resultado va en el mensaje del FRENO.

## 10. Para la autora

1. **`unidades_a_la_vista_T4.json` deja a la vista 3.695 de las 4.951 unidades** de la tanda final con la regla del «seguí»
   (decisión 5); con la del T4 de la tanda 1, 224. La diferencia es la de las dos reglas: la del «seguí» suma las unidades de los
   nodos TextoOrdenado y de los Sujeto con más de una unidad de procedencia que muestran las fichas, y la 1.1 no (tabla T7). Es la lista
   de exclusión de U-MED-VERIF.
2. **La lectura de T4** tiene sus muestras, su material y sus planillas en blanco en `t3/muestras/`, y la versión derivada de la lectura en
   `preregistro/`. No leí ninguna muestra ni marqué nada.
3. **Para el commit:** los cuatro `kg.json` de más de 100 MB de `t3/acumulado/ens_*/r2/` quedan en el árbol sin rastrear y no van al commit;
   van su `.gz` y su sello (registro, §30), como en la tanda 1. Las consolas de los lotes con extensión `.log` las ignora git.
4. **El contenedor de Neo4j del repo** salió con el código 137 al detenerlo (sección 5). La carga ya estaba verificada; la próxima carga lo
   arranca de nuevo.

## 11. Errores propios, con su causa

1. **La primera corrida de `doble_corrida_tf.py` usó una copia vieja del script** (parcial). Corrí los scripts desde la copia del repo y
   copié `t3/scripts/` antes de agregarle la cuenta de la raya. Sincronicé los scripts (control por `cmp`) y la volví a correr.
2. **Dos carpetas vacías en el repo** (parcial). Llamé a `intrinsecas_tf.sh` con la carpeta de salida relativa; el script hace `mkdir -p` antes
   de entrar en la copia y creó `t3/intrinsecas_gen3/e0_del_grafo/` y `con_partes/` en el repo, vacías, sin correr ninguna métrica. Las borré
   con `rmdir`; el script ahora frena si la salida no es absoluta.
3. **La doble corrida comparaba el `.gz` después de comprimir.** Al rehacerla en esta parte, los cuatro acumulados dieron «mismos nombres:
   False» porque su primera corrida ya tenía el `kg.json.gz` y su sello, que agregó `comprimir_kg_tf.py` después de la comparación del
   parcial. `doble_corrida_tf.py` ahora deja esos dos archivos fuera de la comparación, y lo dice su docstring.
4. **Un glob apartó de más.** Para rehacer las intrínsecas del tramo 1 aparté `*Tramo1*`, que también tomó las del acumulado de 60
   («…Tandas0y1yTramo1…»). Las devolví a su lugar sin cambios (las mismas que en el parcial) antes de seguir.

## 12. Los scripts y sus salidas

Los scripts, en `t3/scripts/` (copias adaptadas de los de la tanda 1, con el modelo nombrado en cada docstring); las salidas, en `t3/`:
`salidas/`, `corridas/` (los dos lotes, sus registros y las consolas, con las rutas reemplazadas), `gate/`, `gate_decisiones/`,
`nombres_remision/`, `intrinsecas_gen3/`, `selftests/`, las consolas de `e0_con_partes/`, `neo4j/`, `conteos_sin_leer/` y `muestras/`; y
`registro_vista_r2b_tanda_final.py`. Los ensamblados, en `corpus_tanda_final/ens_*` y en `t3/acumulado/`, con los manifiestos, la E0 combinada y
los registros del armado; los manifiestos del tramo 1 que rigen, en `t3/prueba_raya_tramo1/manifiestos/`. Lo que cambia fuera de `t3/`:
la fixture y `grafos.py`, y la versión derivada de la lectura en `preregistro/`.

El paquete `revision_tanda_final_FRENO_T3/` va en el scratchpad, con su `manifest.txt`, y su copia con `ditto` en
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/afadde2e-6298-47fb-9777-7fcb43152d50/scratchpad/revision_tanda_final_FRENO_T3/`; la
verificación va en el mensaje del FRENO.

FRENO T3. Espero la revisión de la mesa y la de la autora.
