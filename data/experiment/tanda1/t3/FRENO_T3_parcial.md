# FRENO T3 (parcial) — tanda 1 de B6.1: el gate no pasa (17/10/2026, USD 0, sin API, sin commit)

Rigen el §5.1, el §5.2, el §5.3, el §5.4, el §5.4 bis, el §5.5 y el §7 del pre-registro firmado (`docs/preregistro_tanda1.md`, firma
en `95b18217`, con su nota del 17/10/2026 en `ca5b39fd`). HEAD `0c927ebb`.

**Resultado:** hice los cuatro ensamblados y reproducen. El gate (punto 4) **no pasa**, por dos causas que se dan en los cuatro grafos:
1. **Shapes:** S31, que es bloqueante, falla con la E0 de cada grafo tal como está en el repo. Las aristas `remite_a` de las partes por
   corte de `ri_rml::Sbloque14`, que el runner creó en E1, no encuentran su chunk en esa E0. Con la E0 con las partes, como la arma el
   runner, shapes pasa en los cuatro (medida informativa).
2. **Suite:** dos regresiones no declaradas, E4-a1 y E4-a4, contra la entrada sellada del grafo anterior. Hay dos sujetos propuestos
   de la tanda 1 que tienen candidato en el catálogo, por la etiqueta exacta o la singularizada, y E4 no los resolvió.

En la tanda 1 sola se suman 15 regresiones más, de ítems anclados en TOs de la tanda 0 que ese grafo no tiene.

Como dice el punto 4 del «seguí», freno acá, sin los puntos 5 (el registro y Neo4j), 6 (lo que se cuenta sin leer) y 7 (la preparación
de T4). Lo que sigue lo decide la autora. Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan
PENDIENTES.

Toda cifra de este FRENO sale por script de sus archivos (decisión 1.5). Las tablas las genera
`scripts/freno_t3_tablas.py`, y su salida es `salidas/tablas_freno_t3.md`, que copio abajo tal cual. Los demás números del texto son los
de esas tablas o de las salidas que cito.

## 1. Paso 0 (17/10/2026, 22:40:37)

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git rev-parse --abbrev-ref HEAD
main
$ git log -1 --format='%h %s'
0c927ebb Mandato firmado: las filas de alcance de la tanda final en el mensaje del extractor, con su nota al laudo y a la enmienda
$ git status --porcelain --untracked-files=no
$ git ls-files --others --exclude-standard -- data/experiment/reextraccion_v2/corpus_tanda1 data/experiment/tanda1
$ git merge-base --is-ancestor ec5162b6 HEAD; echo $?
0
$ git merge-base --is-ancestor 222a0614 HEAD; echo $?
0
$ sha256 en HEAD (git show HEAD:<ruta> | shasum -a 256)
fda4e15ac72514589ff87dbc541a9d32c3a3e707150ca1ee3616a26c90ff79fb  data/experiment/reextraccion_v2/manifiestos/tanda1_ens_veinte_r2b.json
1d7b940cb5a725e1623829ed917ac25971fac8057bb47fab6a4c18a9544a7582  data/experiment/reextraccion_v2/manifiestos/tanda1_ens_veinte_r2b_sincola.json
818a62cfde403a453d0551916022f928f7cd9cb62d7947801eadb587f2385d9d  data/experiment/reextraccion_v2/manifiestos/tanda1_20tos_r2b.json
22f33a175697304da213453f9a8ab11dcbbd210b75adcddf3741f66a81be2f5a  data/experiment/segmentacion_oficial_e0r2/s2/lista_tanda1_S2.json
9a81ead83e7d7d9765916e2ee72f346b494554146de4f9c2445a3cf1db46a009  data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.json
$ git diff --stat ca5b39fd HEAD -- data/experiment/tanda0/code data/experiment/reextraccion_v2/corpus_v2 data/experiment/reextraccion_v2/e2_reduce data/experiment/reextraccion_v2/e1_extractor data/experiment/reextraccion_v2/e3_verificador scripts data/experiment/neo4j data/experiment/catalogo_unico
$ git diff --quiet 9d1cdd92 HEAD -- data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b; echo $?
0
$ git ls-files data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b | wc -l
     107
$ pgrep -fl "runner_corpus.py|lanzar_t2.py"
(rc=1)
```

- `git status`, `git ls-files --others`, `git diff --stat` y `pgrep` salieron vacíos.
- `df -k .`: 222.533.016 KB libres.
- **La foto antes** (`t2/foto_repo_tanda1_t2.py`, de 22:41:10 a 22:41:23): 51.781 entradas, 14 sin abrir y 342 enlaces. Va en el paquete
  de revisión (`foto_repo_antes_T3.json`, con la carpeta personal como `$HOME`), como en T1 y T2. Al paso 0 la había escrito en `t3/`, y
  la saqué del repo antes de la foto de después (sección 8, error propio 5).
- **Los `.pyc`:** 11.236 líneas (`pyc_antes_T3.txt`, en el paquete; estuvo en `t3/` hasta el mismo momento).

## 2. Los ensamblados (punto 3)

Usé el método del re-sellado (`resellado_t0/FRENO_resellado_T0.md:44-77`):
- **una copia del repo** con el `rsync` de la cláusula y `--exclude=/data/experiment/neo4j/volumen`: 0 `.env`/`NO_ABRIR_`, 0 enlaces y
  0 `.pyc` (`<scratchpad>/t3/copia_t3`; el control, repetido al cierre, en `controles_cierre_t3.txt` del paquete);
- **las cadenas** con `scripts/cadena_t3.sh` (el modelo es `cadena_rs1.sh`), en un lote de 14 de a 4 (`scripts/correr_lote_t3.py`;
  `corridas/lote_t3.txt` y `corridas/lote_t3_rc.json`: las 14 con salida 0);
- **lo que reescribe un archivo rastreado** (la fixture) corrió primero en la copia, y al repo pasaron los mismos bytes
  (`scripts/escribir_en_el_repo_t3.py`, sección 7).

**La tanda 1.**
- `ensamblar_tanda0.py` con los manifiestos del 94 (`tanda1_ens_veinte_r2b.json`, `fda4e15a…`, y `_sincola`, `1d7b940c…`), `--entrada
  corpus_tanda1/salida_r2b` y `--e0-r2` con la E0 de la tanda 1; el sin cola, con `--sin-cola`.
- Salidas: `corpus_tanda1/ens_veinte_r2b/` y `corpus_tanda1/ens_veinte_r2b_sincola/`.

**El acumulado de las tandas 0 y 1** (30 TOs), completo y sin cola, en `t3/acumulado/`:
- **`scripts/armar_acumulado_t3.py`** arma, por copia, tres cosas:
  - **el manifiesto de extracción** de los 30 (`manifiestos/acumulado_30tos_r2b.json`): los `tos` de los dos manifiestos de extracción
    firmados, tal cual, en el orden de la tanda 0 y después el de la tanda 1, con `rutas.e0_salida` en la E0 combinada. Tope y margen
    van en 0, porque no es el manifiesto de una extracción;
  - **la E0 combinada** (`e0_acumulado_r2b/`): los 150 archivos por TO de las dos E0. No lleva los agregados ni `version_e0.json`, que
    el ensamblado y shapes no leen;
  - **la entrada combinada**: las 30 carpetas por TO de las dos salidas, 557 archivos.
  Todo sale igual a su origen (`armado_acumulado_t3.json`).
- **Los manifiestos de ensamblado** salieron de `nombres_remision/derivar_manifiesto_ensamblado_mesa.py`, con el corpus «acumulado» del
  contraste: `acumulado_ens_treinta_r2b.json` y `_sincola`.
  - La variante con la raya da 8 distintas y no entra, como decidió la autora. Rige la regla v2.
  - La regla da `nombres_remision` a 10 de los 30 TOs: 4 de la tanda 0 y 6 de la tanda 1 (`scripts/nombres_acumulado_t3.py` →
    `salidas/nombres_acumulado_t3.json`). Los 20 de la tanda 1 quedan como en su manifiesto. Los 10 de la tanda 0 cambian contra los de
    su re-sellado, donde los 10 tenían `nombres_remision`.
  - Los tres manifiestos cargan con `manifiesto_corpus.cargar`.
- **El ensamblado del acumulado no pidió cambiar código.**

**La doble corrida** (tabla 1):
- los cuatro grafos dan el mismo `kg.json` en dos corridas en procesos distintos;
- la doble corrida interna del ensamblado da `true`;
- solo difiere `reporte_ensamblado_r2.json`, que guarda las rutas de su salida y es igual con ellas normalizadas, como en el re-sellado.

## 3. El gate (punto 4)

### 3.1 Shapes

- **Con la E0 de cada grafo, NO PASA en los cuatro:** S31 en FAIL, que es bloqueante (tabla 3).
- **La causa,** contada desde los `kg.json` (por id, sin texto):
  - las aristas con `chunk_no_encontrado` son todas de las partes por corte de `ri_rml::Sbloque14` (`::parte1`, `::parte2`, `::parte4` y
    `::parte5`; en el sin cola, `::parte2` y `::parte5`; en el acumulado, además, `::parte3`; tabla 3b);
  - el runner las creó en E1, con `chunks_con_partes` (`runner_corpus.py:562-579`), y por eso no están en `chunks_ri_rml.json` de la E0
    commiteada;
  - el grafo se ensambló con esas partes: el ensamblado lee la E0 con `chunks_con_partes` (`ensamblar_tanda0.py:1828`);
  - las partes de `cap::4.2.1.2` de la tanda 0 no tienen ninguna `remite_a`, y por eso S31 pasa en la tanda 0 re-sellada con su E0 sin
    partes.
- **Con la E0 con las partes** (`reext_t0/t3/e0_con_partes.py`, sin cambios, el script de U-REEXT-T0 para M10), **PASA en los cuatro:**
  - 22 PASS, 2 FAIL informativas (S7 y S12) y 4 WARN;
  - S31 queda en 0 violaciones;
  - es el mismo perfil que el grafo anterior.
  Es una medida informativa: qué E0 rige para S31 lo decide la autora (sección 6).
- **Dónde quedaron las salidas.** Las de shapes y de la suite con la E0 de cada grafo quedaron en la carpeta de su ensamblado, como en
  los re-sellados (`corpus_tanda0/ens_diez_r2b_rs1/`); sus consolas, en `t3/gate/consolas/`; las de shapes con las partes, en
  `t3/gate/shapes_con_e0_con_partes/`. El punto 4 pide el `--out` de shapes en `t3/`, y para los dos grafos de la tanda 1 no lo cumplí
  (sección 8, error propio 4).
- Las métricas intrínsecas llaman igual a esa E0. Con la E0 commiteada frenan solas («El E0 indicado no es el de este grafo; FRENO»,
  tabla 7).

### 3.2 La suite

- **Las entradas nuevas de la fixture** las agrega `scripts/editar_fixture_t3.py`. Son copias de la entrada sellada del grafo anterior
  (el de la tanda 0 re-sellado, diez completo o diez sin cola), con el `kg`, el `kg_sha256` y el `registro_dir` nuevos. Las selladas no
  cambian (el script lo controla con el texto canónico de cada una).
- **El resultado** (tablas 4 y 5), en los cuatro grafos:
  - **las tres declaradas de siempre:** RT-C5-3, RT-C6-1 y RT-C6-2 (laudo, `:70-72`);
  - **dos no declaradas, E4-a1 y E4-a4,** que pasan de «resuelto» a «persiste». La suite marca dos sujetos propuestos de la tanda 1 que
    E4 dejó sin resolver y que tienen candidato en el catálogo, por la etiqueta exacta (E4-a1) o la singularizada (E4-a4):
    - `Sujeto_propuesto_proveedores_de_servicios_de_pago` → `Sujeto_proveedor_de_servicios_de_pago`;
    - `Sujeto_propuesto_camaras_electronicas_de_compensacion` → `Sujeto_camara_electronica_de_compensacion`.
    En la tanda 0 no había ninguno: en `corpus_tanda0/ens_diez_r2b_rs1/suite_perfil_r2.json`, E4-a1 y E4-a4 dan `propuestos=95 …
    resolubles no resueltos=0` (en el sin cola, `propuestos=93`). Es un hallazgo de la tanda 1, no un efecto de cómo se armaron los
    grafos;
  - **en la tanda 1 sola, 15 más,** que en el acumulado se cumplen con las mismas expectativas y el mismo código. Su detalle nombra anclas
    de TOs de la tanda 0 que el grafo de la tanda 1 no tiene: cap 1.2, ext, ric 7.1, cla 5.1.1.1, pro 1.1.2.5 y lingob. Los ítems de la
    suite son de esos documentos. Contra la entrada sellada del grafo anterior, en un grafo sin esos TOs, salen como regresión.
- **`selftest_regression_kg`** dio 184 de 184 en las dos corridas (tabla 6).

### 3.3 Reproducibilidad, selftests, intrínsecas y contadores

- **Reproducibilidad** (tabla 2): las dos cadenas r2a y los cuatro re-sellados salen byte a byte, desde la misma copia.
- **Selftests de la cadena** (tabla 6): son los del gate final del laudo (`gate_final_laudo_r2_mesa.sh:60-72`), en un clon APFS de la
  copia. El del catálogo pide git (`no se pudo leer 4ef7650:… con git show`), así que lo corrí en un `git clone` local del repo, en el
  scratchpad: 60 de 60 PASS (sección 8, error propio 1).
- **Intrínsecas de generación 3, informativas** (tabla 7): con la E0 con las partes; con la E0 del grafo frenan, por lo dicho en 3.1.
- **Contadores de E1** (tabla 8).
- **Los indicadores de cita no los medí:** necesitan trazas del agente, y EV2 nunca se corre (laudo, §3, punto 6), como en U-REEXT-T0 T3.

## Las tablas (`scripts/freno_t3_tablas.py` → `salidas/tablas_freno_t3.md`, tal cual)

#### Tabla 0. El acumulado y el lote de cadenas (`acumulado/armado_acumulado_t3.json`, `acumulado/manifiestos/`, `corridas/lote_t3_rc.json`)

- Armado: {'tos': 30, 'tanda0': 10, 'tanda1': 20, 'archivos_e0': 150, 'archivos_entrada': 557, 'todos_iguales_al_origen': True}; manifiesto de extracción `f6086c25ef41537ea32bf9ebfa507699fabcfa918411fa7e5f7223f902458622`; orígenes: {'tanda0': '72d84607', 'tanda1': '818a62cf'}.
- `acumulado_ens_treinta_r2b.json`: 30 TOs, 10 con `nombres_remision`; la variante con la raya da 8 distintas en el contraste del acumulado; regla: v2, sin la raya.
- `acumulado_ens_treinta_r2b_sincola.json`: 30 TOs, 10 con `nombres_remision`; la variante con la raya da 8 distintas en el contraste del acumulado; regla: v2, sin la raya.
- Lote de cadenas: 14 corridas, códigos de salida [0].

#### Tabla 1. Los cuatro grafos y su doble corrida (`salidas/doble_corrida_t3.json`)

| grafo | carpeta | nodos | aristas | sha256 del kg.json (corrida 1 = corrida 2) | archivos | distintos | doble corrida interna |
|---|---|---:|---:|---|---:|---|---|
| KG-Tanda1-Veinte-r2b | `data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b` | 12731 | 31478 | `22e83a62cb88e5bbe31b64a0f2322194bc2ffd2622ea7adc2c07310d8a02c7c7` = | 56 / 56 | reporte_ensamblado_r2.json (igual con las rutas normalizadas: True) | [True, True] |
| KG-Tanda1-Veinte-r2b-sincola | `data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b_sincola` | 12452 | 28320 | `384a6d5bc139cd7b74d86840c68e7034b7a9bcb4bc26da7c61567f3f053e624e` = | 56 / 56 | reporte_ensamblado_r2.json (igual con las rutas normalizadas: True) | [True, True] |
| KG-Acumulado-Tandas0y1-r2b | `data/experiment/tanda1/t3/acumulado/ens_treinta_r2b` | 21409 | 60227 | `e63536d15bd8f575f1b7680921e3ca0d4956bdc5e38dc3f2fea27bb67bd71769` = | 76 / 76 | reporte_ensamblado_r2.json (igual con las rutas normalizadas: True) | [True, True] |
| KG-Acumulado-Tandas0y1-r2b-sincola | `data/experiment/tanda1/t3/acumulado/ens_treinta_r2b_sincola` | 20833 | 55358 | `0435d41f9c7b45ea10cc87e8121fcfb8b3d2b089af837fff377a3460ced9636c` = | 76 / 76 | reporte_ensamblado_r2.json (igual con las rutas normalizadas: True) | [True, True] |

#### Tabla 2. Reproducibilidad (`salidas/doble_corrida_t3.json`, `cadenas`)

| cadena | sha256 del kg.json | esperado | igual | doble corrida interna |
|---|---|---|---|---|
| r2a_diez | `70d51e429b0e2cc1aafa697e32bc83462d371dfdd5edafb34e92fe4f7be45bdd` | `70d51e42` | True | True |
| r2a_desarrollo | `fa4c1043d859081e49dce6cb940a9f5d4c09fc6d449efb85355f95312257178a` | `fa4c1043` | True | True |
| r2b_diez | `fda6c07dbb95602f5992f7e1ad9bf148ff1c2a72b9f69ff2ebbce891c15740ea` | `fda6c07dbb95602f5992f7e1ad9bf148ff1c2a72b9f69ff2ebbce891c15740ea` | True | True |
| r2b_desarrollo | `acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31` | `acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31` | True | True |
| r2b_sincola_diez | `61dd1b69ba03e40499845c40a6a8bec4c22d892ebe95823c7d5a569110f08738` | `61dd1b69ba03e40499845c40a6a8bec4c22d892ebe95823c7d5a569110f08738` | True | True |
| r2b_sincola_desarrollo | `66e745f57397ab754cde09eb641e9f0d9ef6259ea7e6445d086ecbf1c36dcc6c` | `66e745f57397ab754cde09eb641e9f0d9ef6259ea7e6445d086ecbf1c36dcc6c` | True | True |

Veredicto del control: OK.

#### Tabla 3. Shapes (perfil r2, fase r2b; `salidas/tablas_gate_t3.json`)

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

#### Tabla 3b. La causa de S31: `remite_a` con el chunk de procedencia fuera de la E0 del grafo (`salidas/causa_s31_t3.json`)

| grafo | remite_a | fuera de la E0 | todas de partes por corte | por chunk |
|---|---:|---:|---|---|
| veinte | 11581 | 3415 | True | `ri_rml::Sbloque14::parte1` 1198, `ri_rml::Sbloque14::parte2` 942, `ri_rml::Sbloque14::parte4` 1240, `ri_rml::Sbloque14::parte5` 35 |
| veinte_sincola | 8838 | 977 | True | `ri_rml::Sbloque14::parte2` 942, `ri_rml::Sbloque14::parte5` 35 |
| acumulado | 26258 | 3419 | True | `ri_rml::Sbloque14::parte1` 1198, `ri_rml::Sbloque14::parte2` 942, `ri_rml::Sbloque14::parte3` 4, `ri_rml::Sbloque14::parte4` 1240, `ri_rml::Sbloque14::parte5` 35 |
| acumulado_sincola | 22277 | 981 | True | `ri_rml::Sbloque14::parte2` 942, `ri_rml::Sbloque14::parte3` 4, `ri_rml::Sbloque14::parte5` 35 |
| tanda0_diez_rs1 | 13232 | 0 | True | — |
| tanda0_diez_sincola_rs1 | 12251 | 0 | True | — |

#### Tabla 4. La suite (perfil r2, generación 3; `salidas/tablas_gate_t3.json` y `salidas/clasificacion_regresiones_t3.json`)

| grafo | entrada | resuelto / persiste / no aplica | regresiones | declaradas | no declaradas, también en el acumulado | no declaradas, solo sin los TOs de la tanda 0 |
|---|---|---|---:|---:|---:|---:|
| veinte | KG-Tanda1-Veinte-r2b | 31 / 16 / 21 | 20 | 3 | 2 | 15 |
| veinte_sincola | KG-Tanda1-Veinte-r2b-sincola | 31 / 16 / 21 | 20 | 3 | 2 | 15 |
| acumulado | KG-Acumulado-Tandas0y1-r2b | 46 / 13 / 9 | 5 | 3 | 2 | 0 |
| acumulado_sincola | KG-Acumulado-Tandas0y1-r2b-sincola | 46 / 13 / 9 | 5 | 3 | 2 | 0 |

El grafo anterior (KG-Tanda0-Diez-r2b-rs1): 48 / 11 / 9.

#### Tabla 5. Las regresiones no declaradas (`salidas/clasificacion_regresiones_t3.json`)

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

#### Tabla 6. Selftests (`selftests/`)

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

#### Tabla 7. Intrínsecas de generación 3, informativas (`intrinsecas_gen3/`)

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

#### Tabla 8. Contadores de E1 (`salidas/contadores_e1_t3.json`)

Total de los 20 TOs: {'tipo_obligacion_requisito_de_estructura': 0, 'tipo_obligacion_normalizados': 1}. TOs con algún valor distinto de 0: ['lingeef'].

En la tabla 6, `fin` es la marca de fin del lote de selftests (`fin del lote 2026-10-17 23:21:14`), no un selftest.

## 4. Lo que no hice

- **Los puntos 5, 6 y 7.** No toqué `grafos.py`, no escribí el registro de la vista, no levanté Neo4j ni cargué nada. No medí las
  observaciones ni las vigilancias, la cola ni el catálogo al cierre. No armé las poblaciones, los umbrales, los sorteos, el material ni
  `unidades_a_la_vista_T4.json`.
- **No miré nada de E3:** los estados, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3` ni el gasto de los
  reintentos. No escribí `NO_ABRIR_conteos_t3.json`, que es de esos puntos.
- **Lo que leí de la salida de T2:** los ensamblados leen la entrada, y yo leí solo los dos contadores `tipo_obligacion_*` de cada
  `resumen_e1.json`.

## 5. Las salidas que no van al repo

- **La entrada combinada del acumulado** (557 archivos y 297.695.212 bytes, medidos en la copia: `controles_cierre_t3.txt`): son copias
  de las salidas selladas de las dos tandas. Se rearma con
  `scripts/armar_acumulado_t3.py`, y su sha256 por archivo está en `acumulado/armado_acumulado_t3.json`.
- **Las segundas corridas y las de reproducibilidad:** sus sha256 están en `salidas/cadenas_sha256_t3.tsv`.
- **Las dos E0 con las partes:** se rearman con `reext_t0/t3/e0_con_partes.py`. Su consola está en `e0_con_partes/`.
- **Las fotos del repo, las listas de `.pyc` y el grep de convenciones:** en el paquete de revisión, como en T1 y T2.

## 6. Para la autora

1. **Qué E0 rige para S31.**
   - La E0 del repo no tiene las partes que el runner crea en E1 y que entran al grafo. Con ella falla, y con las partes pasa.
   - El runner y el ensamblado usan la E0 con las partes; las intrínsecas, también.
2. **E4-a1 y E4-a4.** Es un hallazgo de la tanda 1, en la resolución de sujetos de E4, con dos sujetos. Corresponde clasificarlo (§5.6)
   y decidir si se corrige o se declara.
3. **La suite sobre la tanda 1 sola.** 15 de sus 20 regresiones son de ítems anclados en TOs de la tanda 0. Falta el criterio para el
   grafo de una tanda que no contiene los documentos de la suite.
4. **Los nombres de la regla en el acumulado.** Los 10 TOs de la tanda 0 llevan `nombres_remision` distintos de los de su re-sellado
   (sección 2). No medí qué remisiones mueve ese cambio.
5. **La fixture lleva las cuatro entradas nuevas,** que son la entrada de la suite de los cuatro grafos. Quedan en el repo sin commit,
   igual que los ensamblados. Si no deben quedar, se sacan antes del commit.

## 7. La foto del repo, los .pyc y el grep de convenciones

Lo genera `scripts/freno_t3_foto.py` desde las dos fotos crudas y las dos listas de `.pyc` (su salida, `seccion7_foto_t3.md`, y las fotos van en el paquete).

- **La foto** (`t2/foto_repo_tanda1_t2.py`). Antes: 22:41:10 a 22:41:23 del 2026-10-17, 51.781 entradas. Después: 23:46:23 a 23:46:34 del 2026-10-17, 52.304 entradas, 14 sin abrir y 342 enlaces.
  - **523 nuevos:** 60 en `corpus_tanda1/ens_veinte_r2b/`; 60 en `corpus_tanda1/ens_veinte_r2b_sincola/`; 73 en `tanda1/t3/, lo demás`; 314 en `tanda1/t3/acumulado/`; 16 en `tanda1/t3/scripts/`.
  - **0 borrados**.
  - **1 cambiado**:
    - `scripts/regression_kg_esperado.json`: `754396aab0318ffd…` → `574169f961c9cdd1…`, de 195.500 a 261.887 bytes;
  - Antes de esta foto saqué del repo `t3/foto_repo_antes_T3.json` y `t3/pyc_antes_T3.txt` (error propio 5); por eso no figuran.
  - Fuera de las rutas admitidas: 0 nuevos, 0 borrados y 0 cambiados además de la fixture. Algún `grafos.py` nuevo o cambiado: False.
- **Los `.pyc`:** 11.236 líneas antes y 11.236 después; listas iguales: True.

**El sha256 de los archivos clave, de la foto de después:**

| archivo | sha256 |
|---|---|
| `data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b/r2/kg.json` | `22e83a62cb88e5bbe31b64a0f2322194bc2ffd2622ea7adc2c07310d8a02c7c7` |
| `data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b_sincola/r2/kg.json` | `384a6d5bc139cd7b74d86840c68e7034b7a9bcb4bc26da7c61567f3f053e624e` |
| `data/experiment/tanda1/t3/acumulado/ens_treinta_r2b/r2/kg.json` | `e63536d15bd8f575f1b7680921e3ca0d4956bdc5e38dc3f2fea27bb67bd71769` |
| `data/experiment/tanda1/t3/acumulado/ens_treinta_r2b_sincola/r2/kg.json` | `0435d41f9c7b45ea10cc87e8121fcfb8b3d2b089af837fff377a3460ced9636c` |
| `data/experiment/tanda1/t3/acumulado/manifiestos/acumulado_30tos_r2b.json` | `f6086c25ef41537ea32bf9ebfa507699fabcfa918411fa7e5f7223f902458622` |
| `data/experiment/tanda1/t3/acumulado/manifiestos/acumulado_ens_treinta_r2b.json` | `141001a2955f64349bf249dbf7359a451419151823200120263161a8ca49b6fe` |
| `data/experiment/tanda1/t3/acumulado/manifiestos/acumulado_ens_treinta_r2b_sincola.json` | `d791d695781a130442f1ce0301ddf1ce6f039543abfcd771caca86a4a6d1ca3e` |
| `scripts/regression_kg_esperado.json` | `574169f961c9cdd1925b25ccf1feacd56068a117e38cad98c9b5ffd3db194bc7` |

La fixture en HEAD (foto de antes): `754396aab0318ffdf74edd7e4e5f96c11ae0c94d351dfd0968c20cafb3645439`.

**Los scripts de T3** (`t3/scripts/`, sha256 de la foto de después):

| script | sha256 |
|---|---|
| `armar_acumulado_t3.py` | `f766a28ecfd3798e294919aaf6edb64ccb9a083774eceea917c147d477204e17` |
| `cadena_t3.sh` | `65fc7b326f0a63d6d995723a65d87b3579d07b9a961b349d10275bb6daef4018` |
| `causa_s31_t3.py` | `a1beae1a9031a53444e31f0913af02eefa4306bf1805f0045ab020e44ed1c84d` |
| `clasificar_regresiones_t3.py` | `1903e59418685d3577a338e2d09187678c203a6e55f617f987a543c9c9fca3e7` |
| `contadores_e1_t3.py` | `3dd9f9eb1cd69c99b4775828ce5715b6a75a695b0246aed2a7537a8a09f3a027` |
| `correr_lote_t3.py` | `8fc6a1a1234ec212e09b13e1bfde1ccea5c3563de7a21beff7d3d87edd72c8e4` |
| `doble_corrida_t3.py` | `6a271d3f7a05978cfe5df1e576f912b185ad9c16e0f69a14d8576e29aef4707f` |
| `editar_fixture_t3.py` | `1285cb147ccf909a9bcb3a04db094fc39d37255b370896d78e770a64c3aeb69b` |
| `escribir_en_el_repo_t3.py` | `706cb2c20100193ca0713aa0d22540ebb9e3dfce6ab4001668f75fae75a371a7` |
| `freno_t3_foto.py` | `3a6a78a1f6d4d1b9c61e8a5caa576022f36f3b85fcd9516219c168f268d2852a` |
| `freno_t3_tablas.py` | `34abcd4565f877e7837f27b41dd55383ade08dcdfd8b4723761ae1075234e101` |
| `gate_t3.sh` | `d71ab18063cd236bb50b0f9d25d175abdfe9ed6ffefb665e78486154eb8e3453` |
| `intrinsecas_t3.sh` | `5a58d3a49c3d604ad5bb15b640e617d65490fa0f20eaa8719bf7ce768f1fc691` |
| `nombres_acumulado_t3.py` | `db3c61194f546092359502f89cb99cd060f077123f234860d32b37d1a26fb4d9` |
| `selftests_t3.sh` | `6036623be2c1f5ea74167af0ebc0ae064c5318645d96d7add7084cc45beb2c66` |
| `tablas_gate_t3.py` | `f64dee2c56272c59e6201848c448b44a6255134bb0da755655d6b7c37143386f` |

- **Escrito después de la foto:** solo este FRENO.
- **El grep de convenciones** (`grep_convenciones_t3.py` y su salida, en el paquete) busca las palabras del `user.name` de git y las de
  origen conversacional en los 524 archivos nuevos o cambiados de la foto. El control positivo da su línea 2.
  - **En lo que redacté** (los scripts de `t3/scripts/` y las tablas): 0 coincidencias.
  - **En las salidas de los generadores y en las copias de la E0 y de los grafos,** las coincidencias son texto de la norma (palabras como
    «correo electrónico» o «e-mail», y un nombre propio del texto de la norma) o rutas absolutas.
  - **Rutas absolutas:** 21 archivos. 20 son salidas de los generadores en las carpetas de los ensamblados (`reporte_ensamblado_r2.json`,
    shapes y suite), que guardan las rutas de la copia, como las selladas de la tanda 0. El otro es `escribir_en_el_repo_t3.py`, que las
    nombra en su control.
  - Sobre este FRENO el grep corre después de escribirlo; su resultado va en el mensaje del FRENO, como en T2.
- **Las carpetas vedadas:** no abrí, no listé ni copié ninguna. No abrí ningún `.env` ni `NO_ABRIR_`; los cuatro del clon de git los
  borré por nombre (error propio 1).

## 8. Errores propios, con su causa

1. **Un `git clone` con archivos `.env` o `NO_ABRIR_`.** Para el selftest del catálogo, que pide git, hice un `git clone` local del repo
   en el scratchpad. El clon trae los archivos rastreados, y el control por nombre dio 4: `run_2_papers/code/.env.example`, los dos
   `NO_ABRIR_` de `tanda1/t2/` y el de `med_umbrales/p/lote1/freno/` (`clon_git_borrados_por_nombre.txt`). Corrí el selftest en el mismo
   comando, sin cortar ante el control, cuando la cláusula pide frenar y borrarlos antes de correr nada.
   - La causa: armé el clon con `git clone` en lugar del `rsync` de la cláusula, y no condicioné la corrida al control.
   - Después los borré por nombre, sin abrirlos, y borré el clon entero. El código de `catalogo_unico/code/` no nombra esos archivos
     (grep, sin coincidencias). No los abrí.
2. **Una atribución que corregí en el momento.** Primero conjeturé que parte de las violaciones de S31 en el acumulado venía de las partes
   de `cap::4.2.1.2` de la tanda 0. El recuento por id dio 0 aristas `remite_a` de esas partes: son todas de `ri_rml`. No llegó a ningún
   archivo.
3. **Una doble cuenta en `causa_s31_t3.py`, corregida antes de usarla.** El campo informativo de las `remite_a` con alguna procedencia
   en una parte contaba dos veces la arista cuando `provenances` repite la `provenance`.
   - La causa: recorrí las dos listas sin unirlas.
   - Lo corregí con un conjunto y volví a correrlo antes de armar ninguna tabla. La tabla 3b no usa ese campo.
4. **El `--out` de shapes de los dos grafos de la tanda 1, fuera de `t3/`.** El punto 4 lo pide en `t3/`, y quedó en
   `corpus_tanda1/ens_veinte_r2b/` y `_sincola/`, junto con la suite.
   - La causa: le pasé a `gate_t3.sh` la carpeta del ensamblado como salida, porque así están las salidas selladas de los re-sellados
     (`corpus_tanda0/ens_diez_r2b_rs1/`), sin contrastarlo con el punto 4.
   - No los moví, porque el mandato no autoriza mover salidas ya escritas. Si deben ir a `t3/`, son cuatro archivos por grafo (shapes y
     suite, `.md` y `.json`), y lo decide la autora.
5. **La foto de antes y la lista de `.pyc`, escritas en `t3/`.** Al paso 0 las escribí en `t3/`. En T1 y T2 van solo al paquete, y la
   foto lista rutas rastreadas que el grep de convenciones marca.
   - La causa: no las contrasté con lo que hicieron T1 y T2.
   - Las saqué del repo antes de la foto de después: las moví al scratchpad, con su sha256 controlado (`f5322f2a…` y `f1f16581…`), y van
     en el paquete.

FRENO T3 (parcial). Espero la revisión de la autora.
