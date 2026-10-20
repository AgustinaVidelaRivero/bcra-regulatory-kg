# FRENO T3 (parcial) — tanda final de B6.1: los ocho ensamblados reproducen; el gate no pasa por el selftest de claves (20/10/2026, USD 0, sin API, sin commit)

Rigen el pre-registro de la tanda final FIRMADO (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`, con sus notas posteriores en
`27bfaeb5` y `86541475`), sus §2, §5, §6, §7 y §8 y la precisión de la firma, lo del pre-registro de la tanda 1 que este no reemplaza y el
«seguí» de T3, con sus tres correcciones. HEAD `eb5ad14b`. Toda cifra de este FRENO sale de un script de `t3/scripts/` y de su salida; la
sección 9 los lista.

**Resultado:**
- **Los ocho ensamblados** (punto 3) salen con rc 0 en las 28 corridas del lote, la doble corrida de cada uno da el mismo `kg.json`, los
  diez grafos sellados de las tandas 0 y 1 se reproducen byte a byte y el acumulado con el tramo 1 da las cifras de la prueba de la mesa
  (tablas E1 a E5). Los cuatro `kg.json` de los acumulados pasan de 100 MB y van con su `.gz`, que se restaura byte a byte.
- **El gate** (punto 4) **no pasa**, por una sola causa: el selftest de claves (`selftest_clave_cache`) da rc distinto de 0. La causa, por
  código y por datos, sin abrir sus salidas: su variación R23 supone que la unidad `snp_psp::1.3.1.1` no está en la caché de E1, y
  `snp_psp` es un TO de la tanda final que T2 extrajo con el mismo chunk (sección 3.4). Lo demás del gate da lo esperado: con la E0
  con las partes, que rige para S31, shapes pasa en los ocho; la suite da 0 regresiones no declaradas que cuenten; los
  selftests de la cadena dan rc 0; la fixture solo suma las ocho entradas.
- Como dice el punto 4 del «seguí», **freno acá, sin los puntos 5 (el registro y Neo4j), 6 (lo que se cuenta sin leer) y 7 (la
  preparación de T4)**. Lo que sigue lo decide la autora. Dejé preparados sus scripts, sin correr sobre el repo (sección 5). Nada commiteado
  y ningún mensaje de commit preparado.

## 1. Paso 0 (20/10/2026, desde las 10:02:13)

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
checkpoint. La foto entera queda fuera del repo y del paquete porque nombra todas las rutas del repo; su resumen va en la sección 7. La
salida de las entradas en HEAD termina con la cuenta de los renglones OK de `t1/sha256_para_T2.txt`.

## 2. Los ocho ensamblados (punto 3)

El mecanismo es el del T3 de la tanda 1, copiado y adaptado en `t3/scripts/`: `armar_acumulados_tf.py` arma por copia la E0 y la entrada
de los dos acumulados en una copia del repo (la del `rsync` del «seguí», con 0 nombres vedados y 0 enlaces); `cadena_t3_tf.sh` corre
`ensamblar_tanda0.py` con los argumentos de las corridas del T3 de la tanda 1; `correr_lote_t3_tf.py` corre las 28 cadenas de a
tres; `doble_corrida_tf.py` compara. La tanda y el tramo 1 van con los cuatro manifiestos de T1, `--entrada
data/experiment/reextraccion_v2/corpus_tanda_final/salida_r2b` y la E0 de los 98. La unidad con error de T2
(`ri_transpa::Sbloque1::chapeau_seccion`) falta en los grafos, como decidió la autora (registro, §44): no la toqué.

#### Tabla E1. Los ocho ensamblados (`salidas/doble_corrida_tf.json`, `salidas/comprimir_kg_tf.json`; el lote, `corridas/lote_t3_tf_rc.json`: 28 corridas, rc distinto de 0 en 0, de 10:10:59 a 11:13:06)

| grafo | carpeta | TOs | nodos | aristas | `kg.json` (bytes) | sha256 del `kg.json` | dos corridas iguales | doble corrida interna | minutos (corrida 1, 2) |
|---|---|---:|---:|---:|---:|---|---|---|---|
| KG-Acumulado-Tandas0y1yFinal-r2b | `data/experiment/tanda_final/t3/acumulado/ens_128_r2b` | 128 | 38.324 | 114.925 | 220.599.822 | `c43d66e503c2b27477cd17a5ffc2c64b6334d9525f0524d82ff248f04e7d96ac` | True | True | 25,8, 24,4 |
| KG-Acumulado-Tandas0y1yFinal-r2b-sincola | `data/experiment/tanda_final/t3/acumulado/ens_128_r2b_sincola` | 128 | 37.321 | 104.279 | 197.955.473 | `398459a853590c584398243b543548d5634124d5577b3cfffe4332f0a61ac0fd` | True | True | 23,4, 22,1 |
| KG-TandaFinal-r2b | `data/experiment/reextraccion_v2/corpus_tanda_final/ens_98_r2b` | 98 | 17.025 | 46.273 | 86.155.155 | `db2df7b7e707ef191d1df6fdb3638fd920cf4486afce13a7e889b9755155bc97` | True | True | 5,3, 5,2 |
| KG-TandaFinal-r2b-sincola | `data/experiment/reextraccion_v2/corpus_tanda_final/ens_98_r2b_sincola` | 98 | 16.598 | 43.392 | 80.314.222 | `c050f3c90ce5d32be759d2e5d05bbe2e131d9abf7811de097c97f4a1fe410cf7` | True | True | 5,1, 5,1 |
| KG-Acumulado-Tandas0y1yTramo1-r2b | `data/experiment/tanda_final/t3/acumulado/ens_60_tramo1_r2b` | 60 | 23.671 | 67.006 | 132.598.843 | `87ea32c503cd79bcf537a5d259527f4a50ccf00dc40a682ea9abc200b8d6ce50` | True | True | 11,2, 10,7 |
| KG-Acumulado-Tandas0y1yTramo1-r2b-sincola | `data/experiment/tanda_final/t3/acumulado/ens_60_tramo1_r2b_sincola` | 60 | 22.930 | 59.354 | 115.837.346 | `4ec19d46f23b80866866e132d6d367b88f9f83c12856abba36536ad06dd9d32d` | True | True | 10,2, 9,2 |
| KG-TandaFinal-Tramo1-r2b | `data/experiment/reextraccion_v2/corpus_tanda_final/ens_tramo1_r2b` | 30 | 2.372 | 4.066 | 8.233.790 | `f064d4e00b41246525d3c30a88f33b3ba9672c5e02cc10a36a4fa18dc88b940c` | True | True | 0,4, 0,4 |
| KG-TandaFinal-Tramo1-r2b-sincola | `data/experiment/reextraccion_v2/corpus_tanda_final/ens_tramo1_r2b_sincola` | 30 | 2.207 | 3.822 | 7.595.198 | `bbda74cda7e071e27782b41b06d7557e2c153e8afff7ea3f6540bdd520c3615f` | True | True | 0,4, 0,5 |

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

#### Tabla E4. La prueba de la raya en el tramo 1 y el acumulado de 60 contra la prueba de la mesa

- **tf_tramo1_raya** contra KG-TandaFinal-Tramo1-r2b: `kg.json` igual: True (`f064d4e00b412465…`); archivos distintos: reporte_ensamblado_r2.json; TOs con `nombres_remision` distintos entre los dos manifiestos: 23.
- **tf_tramo1_raya_sincola** contra KG-TandaFinal-Tramo1-r2b-sincola: `kg.json` igual: True (`bbda74cda7e071e2…`); archivos distintos: reporte_ensamblado_r2.json; TOs con `nombres_remision` distintos entre los dos manifiestos: 23.
- **KG-Acumulado-Tandas0y1yTramo1-r2b**: 23.671 nodos y 67.006 aristas; la mesa (registro, §43), 23.671 y 67.006: igual True.
- **KG-Acumulado-Tandas0y1yTramo1-r2b-sincola**: 22.930 nodos y 59.354 aristas; la mesa (registro, §43), 22.930 y 59.354: igual True.
- Los `nombres_remision` del manifiesto de T3 contra los de los manifiestos que usó la mesa (`data/experiment/tanda1/t3/acumulado/manifiestos/acumulado_ens_treinta_r2b.json`, `data/experiment/tanda_final/t1/ensamblado/manifiestos/tanda_final_ens_tramo1_r2b.json`): 60 TOs, 60 en los de la mesa, 0 distintos.

#### Tabla E5. El armado de los acumulados (`acumulado/armado_acumulado_<n>_tf.json`)

| acumulado | TOs (0 / 1 / final) | archivos de la E0 | archivos de la entrada | bytes de la entrada | todos iguales al origen | manifiesto de extracción |
|---|---|---:|---:|---:|---|---|
| 128 | 128 (10 / 20 / 98) | 640 | 2.295 | 530.323.665 | True | `7a17222c1579cd02…` |
| 60 | 60 (10 / 20 / 30) | 300 | 1.073 | 327.469.149 | True | `a2ef5e64478bdad2…` |

La entrada combinada se registra solo por su total de archivos, sus bytes y el sha256 de su lista (cegamiento, punto 8): no va al repo, porque es la salida de la extracción por copia.

### 2.1 Los `nombres_remision` de los ensamblados nuevos, medidos (§7; registro, §19; enmienda 9, punto 8)

`medir_nombres_t3_tf.py` es la medición de la mesa (`nombres_remision/medir_nombres_remision_mesa.py`) con los cuatro corpus nuevos; el
contraste y el resumen son los de la mesa, sin cambios (`contrastar_con_inventario_completo_mesa.py` y `resumir_medicion_mesa.py`). Todo
corrió sobre la copia. `tabla_nombres_t3_tf.py` pone las cifras de la mesa al lado (las del 16/10/2026 del repo, y las de la enmienda 9,
punto 8, `756a0394:81-84`, para el tramo 1 y el acumulado de 60):

| ensamblado | TOs | menciones | resueltas, regla | resueltas, raya | distintas, regla | distintas, raya | la raya entra (§19) | en el manifiesto | la mesa (menciones / regla / raya / distintas con la raya) | igual |
|---|---:|---:|---:|---:|---:|---:|---|---|---|---|
| KG-TandaFinal-r2b (y su sin cola) | 98 | 804 | 389 | 413 | 0 | 3 | no | regla, 31 TOs con nombres | 804 / 389 / 413 / 3 (data/experiment/nombres_remision/medicion/ (16/10/2026)) | sí |
| KG-TandaFinal-Tramo1-r2b (y su sin cola) | 30 | 309 | 1 | 1 | 0 | 0 | sí | regla, 25 TOs con nombres | 309 / 1 / 1 / 0 (756a0394, enmienda 9, punto 8, líneas 81 a 84 (17/10/2026)) | sí |
| KG-Acumulado-Tandas0y1yFinal-r2b (y su sin cola) | 128 | 1608 | 1279 | 1319 | 0 | 0 | sí | regla con la raya, 50 TOs con nombres | 1608 / 1279 / 1319 / 0 (data/experiment/nombres_remision/medicion/ (16/10/2026)) | sí |
| KG-Acumulado-Tandas0y1yTramo1-r2b (y su sin cola) | 60 | 1113 | 429 | 455 | 0 | 23 | no | regla, 35 TOs con nombres | 1113 / 429 / 455 / 23 (756a0394, enmienda 9, punto 8, líneas 81 a 84 (17/10/2026)) | sí |

Iguales a la mesa en los cuatro: True.

- **Los manifiestos de los acumulados.** El de 128 lo derivó `derivar_manifiesto_ensamblado_mesa.py` con el contraste de la mesa (corpus
  `acumulado_final`: 0 distintas, la raya entra; 50 TOs con nombres). Para el de 60, ese
  derivador frena, porque la medición del repo no tiene un corpus con esos TOs (la de la enmienda 9, punto 8, está en el paquete de la mesa).
  Lo derivé con `derivar_manifiesto_ensamblado_tf.py`, que hace lo mismo con la variante decidida por la fuente que se le pasa
  (`756a0394:83-84`: 23 distintas, la raya no entra; 35 TOs con nombres), y escribe esa fuente en la
  `descripcion`. La medición de arriba la confirma.

## 3. El gate (punto 4)

Sobre la copia del repo, con las decisiones del gate de la tanda 1 (registro, §29): para S31 rige la E0 con las partes por corte, y se
informan las dos corridas; la suite se juzga sobre el acumulado, y en la tanda y en el tramo 1 lo «fuera del grafo» se informa aparte y no
cuenta; E4-a1 y E4-a4 siguen declaradas. Los `--out` van a `t3/gate/` (el «seguí» lo pide así; en la tanda 1 fueron a las carpetas de los
ensamblados).

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
  - **La causa del de claves** (`gate_decisiones/diagnostico_clave_cache_tf.json`, sin abrir sus salidas): los 16 campos que difieren de A3 sin cuentas son de la variación del TO nuevo (`variacion_to_nuevo`, R23 en el perfil r2b) o derivan de ella: True. Supone que `snp_psp::1.3.1.1` no está en la caché de E1; `snp_psp` es de la tanda final (82.º de `orden_corrida`, tramo 2) y su chunk es el mismo en la E0 de la tanda final y en b584: True. R23 supone que la unidad de un TO fuera de la tanda 0 no está en la caché de E1. T2 extrajo ese TO con el perfil r2b y el mismo chunk, así que la clave está y R23 deja de dar miss: el selftest falla por su supuesto, no por el código de la clave.
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
- **Los `nombres_remision` medidos** (`nombres_remision/tabla_nombres_t3_tf.json`): iguales a la medición de la mesa en los cuatro ensamblados: True; la variante en cada manifiesto sigue la §19: KG-TandaFinal-r2b True; KG-TandaFinal-Tramo1-r2b False; KG-Acumulado-Tandas0y1yFinal-r2b True; KG-Acumulado-Tandas0y1yTramo1-r2b True.

**Veredicto del gate, con las decisiones de la §29: NO PASA.**

### 3.1 Shapes

- Con la E0 con las partes (`e0_partes_tf.py`, que corre `reext_t0/t3/e0_con_partes.py` sin cambios, dos veces por E0): pasa en los ocho.
  La tanda final no tuvo unidades partidas (su E0 con las partes es la E0 del repo: True); en los acumulados entran
  las partes de las tandas 0 y 1 (cap::4.2.1.2 en 2 partes, ri_rml::Sbloque14 en 5 partes).
- Con la E0 de cada grafo: S31 falla en 4 grafos (KG-Acumulado-Tandas0y1yFinal-r2b, KG-Acumulado-Tandas0y1yFinal-r2b-sincola, KG-Acumulado-Tandas0y1yTramo1-r2b, KG-Acumulado-Tandas0y1yTramo1-r2b-sincola), por las `remite_a` de las partes por corte
  de `ri_rml::Sbloque14`, de la tanda 1 (tabla V2, `causa_s31_tf.json`). En los cuatro de la tanda final, S31 pasa también con la E0 del
  repo.
- Los FAIL y WARN que no bloquean son los mismos en los ocho y en los grafos de la tanda 1 (`tablas_gate_tf.json`, `no_pass`).

### 3.2 La suite y la fixture

- **La fixture** (`editar_fixture_tf.py`, sobre la copia): ocho entradas nuevas al final de `estado_esperado`, copias de la entrada sellada
  del grafo anterior del mismo tipo de la tanda 1 (KG-Tanda1-Veinte-r2b para la tanda y el tramo 1; KG-Acumulado-Tandas0y1-r2b para los
  acumulados, completo o sin cola), con el `kg`, el `kg_sha256` y el `registro_dir` nuevos. El script controla que las expectativas de esas
  cuatro y de las dos de diez de la tanda 0 re-sellada son las mismas, así que elegir una u otra solo cambia el rótulo.
- **El control de la precisión de la firma, punto 3** (`control_fixture_tf.py`, contra `git show HEAD:`): 4.094 claves de HEAD,
  0 quitadas y 0 cambiadas; 2.272 claves nuevas, todas de las ocho entradas: True; el orden de las selladas,
  igual: True. Veredicto: OK.
- **El resultado:** en los acumulados, 5 regresiones en cada uno, las tres del laudo y E4-a1 y E4-a4, declaradas; en la tanda y en el
  tramo 1, 18 en cada uno, todas fuera del grafo (`fuera_del_grafo_tf.py`, con las anclas de cada ítem sacadas de su definición en
  `scripts/regression_kg.py`). El cruce: en los cuatro, las no declaradas fuera del grafo son las no declaradas que su acumulado no da (15 y
  15 ítems, iguales: True).

### 3.3 La reproducibilidad, los selftests de la cadena, las intrínsecas y los contadores

Las tablas E3 y V3. Los selftests de la cadena corrieron sobre un clon APFS de la copia (`selftests_tf.sh`, con 0 nombres vedados y 0
enlaces). El del catálogo pide `git show 4ef7650:<ruta>` (`derivar_catalogo_r2.py:103`): corrió con `GIT_DIR` en el `.git` del repo y
`GIT_OPTIONAL_LOCKS=0`, en lugar del `git clone` del T3 de la tanda 1, que trajo archivos `.env` y `NO_ABRIR_` al clon. El sha256 de
`.git/index` y de `.git/HEAD` antes de los selftests y al cerrar T3 (2026-10-20 13:03:22), por sus primeros 16 caracteres: iguales,
True.

### 3.4 El selftest de claves: la causa por la que el gate no pasa

- **Cómo corrió:** `selftest_clave_cache --salida-r2b data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b`, como en A3 y en T1, sobre el
  clon, con su JSON y su consola a archivos que no abrí; `selftest_claves_sin_cuentas_tf.py` (el de T1 con los nombres de T3) les sacó
  las cuentas con `alcance_e1/a3/scripts/clave_cache_sin_cuentas_a3.py` y las comparó con las de A3 sin cuentas. Los sha256 de las dos
  originales:

```
a6272d3df1aaeea8de3f3a8a6dce958424fb242dd19a774e85b157328434e6a6  selftest_clave_cache_t3.json (original, con las cuentas; no se abre)
2d502351f8e2087299540519eeb505685c41961b7df0dda3eda2cdff3332db07  consola_selftest_clave_cache_t3.txt (original, con las cuentas; no se abre)
```

- **Lo que dio:** el selftest terminó con rc 1. Las dos salidas sin cuentas no son las de A3 (JSON igual: False; consola igual:
  False), así que el script las renombró a `NO_ABRIR_` y no las abrí. Doy solo las rutas de los
  16 campos del JSON que difieren, sin valores:
  `/contraste_tabla/discrepancias[0]/fila`, `/contraste_tabla/discrepancias[0]/selftest[0]`, `/contraste_tabla/discrepancias[0]/selftest[1]`, `/contraste_tabla/discrepancias[0]/tabla[0]`, `/contraste_tabla/discrepancias[0]/tabla[1]`, `/contraste_tabla/discrepancias[0]/variacion`, `/contraste_tabla/estado`, `/contraste_tabla/filas[32]/observado[0]/coincide`, `/contraste_tabla/filas[32]/observado[0]/e1`, `/perfil_r2b/variaciones[30]/detalle/clave_en_cache_e1`, `/perfil_r2b/variaciones[30]/e1/observadas_que_cambian[0]`, `/perfil_r2b/variaciones[30]/e1/ok`, `/perfil_r2b/variaciones[30]/e1/token`, `/perfil_r2b/variaciones[30]/ok`, `/variaciones_con_discrepancia[0]`, `/veredicto`.
- **La causa** (`diagnostico_clave_cache_tf.py`, que lee solo esas rutas, el código del selftest, el manifiesto de la tanda final y las dos
  E0; ni las salidas del selftest ni las bases de la caché):
  - todos esos campos son de la variación del TO nuevo o derivan de ella: True. Es `variacion_to_nuevo`, la única
    función del selftest con el campo `clave_en_cache_e1`: V23 en el perfil sellado y R23 en el r2b;
  - supone que una unidad de un TO de fuera de la tanda 0, `snp_psp::1.3.1.1` (de la partición b584), no está en la caché de E1 (miss);
  - `snp_psp` es de la tanda final (82.º de `orden_corrida`, tramo 2), y su chunk es el mismo en la E0 de la tanda final y en
    b584: True. T2 lo extrajo con el perfil r2b, así que la clave de R23 está en la caché y R23 deja de dar miss.
  - En T1 el selftest dio OK (FRENO T1, §4.1) porque T2 todavía no había extraído ese TO. El código de la clave (`llm_cache.py`,
    `cliente_e1.py` y `cliente_e3.py`) está entre las 78 rutas, que el paso 0 dio iguales; el selftest no está entre ellas y es el de HEAD.
    Falla por un supuesto que T2 dejó de cumplir, no por el código de la clave.
- **El cegamiento:** saber si una clave de E1 está en la base es un dato de la caché de E1; no di cuentas de claves ni nada de E3. Las
  dos salidas sin cuentas quedan como `NO_ABRIR_` en `t3/selftests/clave_cache/`, sin abrir; las dos originales, con las cuentas, quedan
  en el scratchpad, sin abrir, y van solo por su sha256.

## 4. Para la autora

1. **El selftest de claves** (sección 3.4): decide cómo sigue el gate. Las opciones que veo, sin tocar código: declarar la R23 (y la V23
   del perfil sellado, que no cambió) como no aplicable después de T2, porque su TO ya se extrajo, y juzgar el selftest sin ella; o pedir a
   la mesa que cambie el TO de la variación por uno que no esté en ninguna tanda (`TO_NUEVO` y `UNIDAD_TO_NUEVO`,
   `selftest_clave_cache.py:132-133`), que es tocar el código del selftest (no está entre las 78 rutas). Lo demás del gate da lo esperado
   (tabla V1).
2. **Los manifiestos del tramo 1.** El «seguí» pide los cuatro manifiestos de T1, que no llevan la raya, y la §19 con la enmienda 9, punto 8,
   dice que en el tramo 1 solo «la raya entra, sin cambiar ninguna resolución». Corrí las dos: el `kg.json` es el mismo, completo y sin cola,
   aunque los `nombres_remision` cambian en 23 de los 30 TOs (tabla E4). Mandan los archivos: la regla de la §19 da la raya;
   el grafo no cambia con ninguna.
3. **El derivador del acumulado de 60** (sección 2.1): el de la mesa no corre sin la medición en el repo, y usé una copia adaptada.
4. **Para el punto 7, cuando se decida seguir** (preparado, sin correr sobre el repo):
   - los umbrales: el script de la mesa, importado sin cambios como en el T3 de la tanda 1, mide la atención y el freno contra la tasa de
     la tanda 0 (su `BASE`), y el pre-registro de la tanda final da como línea de base la de la tanda 1. Las dejo las dos al lado;
   - `unidades_a_la_vista_T4.json`: la regla del «seguí» (de un nodo, todas las unidades de su procedencia) es la del T3 de la tanda 1; el T4
     de la tanda 1 usó una más chica (decisión del 18/10/2026, punto 1.1: sin el TextoOrdenado ni el Sujeto fusionado). Sigo la del «seguí» y
     doy la otra como información;
   - los dos momentos de lectura del §6 se juntan en uno, como lo pide el «seguí».

## 5. Lo que no hice: los puntos 5, 6 y 7

Por el freno del punto 4 no toqué `grafos.py` ni Neo4j, no conté nada sin leer y no armé poblaciones, umbrales, sorteos ni material. Están
listos en `t3/scripts/` y no corrieron: `editar_grafos_tf.py`, `dry_registro_tf.py`, `cargar_neo4j_tf.py`, `control_cola_neo4j_tf.py`,
`contado_sin_leer_tf.py`, `tablas_contado_tf.py`, `poblaciones_t4_t3f_tf.py`, `poblaciones_t4t1_tf.py`, `umbrales_t4_tf.py`, `sorteos_t4_t3f_tf.py`,
`sorteos_t4t1_tf.py`, `material_t4_t3f_tf.py`, `material_t4t1_tf.py`, `unidades_a_la_vista_tf.py` y `tablas_t4_tf.py`. La base de los
sorteos la controlé: `git show 5289b02f:docs/preregistro_tanda_final.md` da `0897d609…`.

La versión derivada de la lectura (7.7) no lee ningún grafo: la armé en el scratchpad con el completador sobre el pre-registro de
`4de7f2a7` y `--momento lectura_tramo1`, y queda sin ningún `⟦T4.` (solo espera el hueco de T5). No la pasé al repo, porque es del punto 7;
va en el paquete.

## 6. El cegamiento (punto 8)

- No miré ni di el desglose de las aceptadas por estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3`
  ni el gasto de los reintentos.
- De la salida de la extracción, ninguna cuenta por tipo de archivo. La entrada de los acumulados se registra solo por su total de archivos,
  sus bytes y el sha256 de su lista (tabla E5). La E0 con las partes informa las unidades partidas por corte, que son de E1.
- No escribí `NO_ABRIR_conteos_t3.json`: lo escribe lo contado sin leer (punto 6), que no corrí. Los `NO_ABRIR_` de esta parte son los dos del
  selftest de claves (sección 3.4).
- No abrí ningún `.env` ni ningún `NO_ABRIR_`, ni ninguna carpeta vedada.

## 7. La foto del repo, los .pyc, lo escrito en el repo y el grep de convenciones

Lo genera `scripts/freno_tf_foto.py` desde la foto del paso 0 y la de después (`tanda_final/t1/foto_repo_tanda_final_t1.py`; las dos, fuera del repo y del paquete, porque nombran todas las rutas del repo; en el paquete van su sha256 y este resumen).

- **La foto.** Paso 0: 10:03:25 a 10:03:40 del 2026-10-20, 55.309 entradas. Después: 13:04:06 a 13:04:20 del 2026-10-20, 57.888 entradas, 44 sin abrir y 342 enlaces.
  - **2.579 nuevos:** 212 en `corpus_tanda_final/ens_98_r2b/`; 212 en `corpus_tanda_final/ens_98_r2b_sincola/`; 76 en `corpus_tanda_final/ens_tramo1_r2b/`; 76 en `corpus_tanda_final/ens_tramo1_r2b_sincola/`; 1.772 en `tanda_final/t3/acumulado/`; 31 en `tanda_final/t3/corridas/`; 6 en `tanda_final/t3/e0_con_partes/`; 73 en `tanda_final/t3/gate/`; 14 en `tanda_final/t3/gate_decisiones/`; 28 en `tanda_final/t3/intrinsecas_gen3/`; 12 en `tanda_final/t3/nombres_remision/`; 2 en `tanda_final/t3/prueba_raya_tramo1/`; 8 en `tanda_final/t3/salidas/`; 43 en `tanda_final/t3/scripts/`; 14 en `tanda_final/t3/selftests/`.
  - **0 borrados:** ninguno.
  - **1 cambiados:** 1 la fixture.
  - **Fuera de lo admitido:** 0.
  - `scripts/regression_kg_esperado.json`: `574169f961c9cdd1…` (HEAD) → `496a03c9a6d959f0…`, de 261.887 a 399.453 bytes.
- **Los `.pyc`:** 11.236 líneas en el paso 0 y 11.236 después; listas iguales: True.

**El sha256 de los archivos clave, de la foto de después:**

| archivo | sha256 |
|---|---|
| `scripts/regression_kg_esperado.json` | `496a03c9a6d959f0d8d0b1ba961adae2e83d64df6431d1739025e7f494964aac` |
| `data/experiment/neo4j/grafos.py` | `cec1ec717451f6775c7ef1b98f4a1cf80d628ff444e0ed58a8f8d5b1a42b31ff` |
| `data/experiment/tanda_final/t3/registro_vista_r2b_tanda_final.py` | no está: es de los puntos 5 o 7, que no corrí |
| `data/experiment/tanda_final/preregistro/preregistro_tanda_final_derivada_T4.md` | no está: es de los puntos 5 o 7, que no corrí |
| `data/experiment/tanda_final/preregistro/preregistro_tanda_final_derivada_T4.huecos.json` | no está: es de los puntos 5 o 7, que no corrí |

**Lo que se escribió en el repo** (`escribir_en_el_repo_tf.py`, en 2 etapas, los ensamblados y el gate, desde un staging armado en el
scratchpad; antes, cada ruta nueva no existía y la fixture era la de HEAD; después, cada archivo es byte a byte el del staging):
2.536 archivos nuevos y 1 que cambia, la fixture; escritos iguales al staging: 2.537 de
2.537. Escritos después de la foto de después: este FRENO y `t3/resumen_fotos_T3.json`.

**El grep de convenciones** (`grep_convenciones_tf.py`, con `LC_ALL=en_US.UTF-8`; los tokens del nombre salen de `git config user.name`
en memoria y no quedan escritos; los términos, los del FRENO T1, §11), en dos grupos, sin los `NO_ABRIR_`:
- **Lo que redacté** (`t3/scripts/`, `t3/salidas/`, `t3/gate_decisiones/`, la tabla de los nombres y la fixture): 67 archivos;
  5 renglones con coincidencias, en `freno_t3_parcial_armar_tf.py` (1) y `grep_convenciones_tf.py` (4): los
  dos escriben los términos del grep, uno para buscarlos y el otro para describirlos; tokens del nombre fuera de rutas, 0.
  Rutas absolutas en `escribir_en_el_repo_tf.py` y `grep_convenciones_tf.py`, que las nombran en sus controles. El renglón de
  control (el primer token y «slack») da 2 coincidencias, una por término.
- **Lo que escribieron los generadores** (los ensamblados, la E0 combinada, shapes, la suite, las intrínsecas, los selftests y las consolas):
  2.508 archivos de texto, con coincidencias en 219. Los términos son texto de las normas
  («correo» 5.577, «e-mail» 490, «pedido por» 147, «email» 60, «reunión con» 4). Los tokens del nombre: 72 dentro de
  rutas absolutas de la copia (las que guardan 8 `reporte_ensamblado_r2.json`, como los sellados de la tanda 1) y
  36 fuera de ellas, en 16 archivos que copian texto de las normas
  (`chunks_*`, `estructura_*`, `kg.json`, `omisiones.jsonl`, `tablas_*`: las copias de la E0 y los registros
  de omisiones del ensamblado). Nada de eso lo escribí yo.
- Sobre este FRENO el grep corre después de escribirlo; su resultado va en el mensaje del FRENO.

## 8. Errores propios, con su causa

1. **La primera corrida de `doble_corrida_tf.py` usó una copia vieja del script.** Corrí los scripts desde la copia del repo y copié
   `t3/scripts/` antes de agregarle la cuenta de la raya; la salida salió sin esa cuenta. Sincronicé los scripts (control por `cmp`) y la volví
   a correr; la tabla E4 es la de la segunda.
2. **Dos carpetas vacías en el repo.** Llamé a `intrinsecas_tf.sh` con la carpeta de salida relativa, y el script hace `mkdir -p` antes de
   entrar en la copia: creó `t3/intrinsecas_gen3/e0_del_grafo/` y `con_partes/` en el repo, vacías, y ninguna métrica corrió (la consola
   apuntaba a una carpeta que no existía en la copia). Las borré con `rmdir`, que solo borra carpetas vacías, y las intrínsecas corrieron
   de nuevo con la salida absoluta, dentro de la copia, como en la tanda 1.

## 9. Los scripts y sus salidas

Los scripts, en `t3/scripts/` (copias adaptadas de los de la tanda 1, con el modelo nombrado en cada docstring); las salidas, en `t3/`:
`salidas/` (doble corrida, compresión, contadores de E1, tablas de los ensamblados), `corridas/` (el lote, su registro y las consolas, con las
rutas reemplazadas), `gate/` (shapes y suite de cada grafo, con las dos E0), `gate_decisiones/` (E0 con las partes, tablas, fuera del grafo,
S31, fixture, diagnóstico del selftest de claves y veredicto), `nombres_remision/`, `intrinsecas_gen3/`, `selftests/` y las consolas de
`e0_con_partes/`. Los ensamblados, en `corpus_tanda_final/ens_*` y en `t3/acumulado/`, con los manifiestos, la E0 combinada y los registros
del armado; la prueba de la raya, solo con sus manifiestos (`t3/prueba_raya_tramo1/manifiestos/`).

El paquete `revision_tanda_final_FRENO_T3/` va en el scratchpad, con su `manifest.txt`, y su copia con `ditto` en
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/afadde2e-6298-47fb-9777-7fcb43152d50/scratchpad/revision_tanda_final_FRENO_T3/`; la
verificación va en el mensaje del FRENO.

FRENO T3 (parcial). Espero la revisión de la mesa y la decisión de la autora.
