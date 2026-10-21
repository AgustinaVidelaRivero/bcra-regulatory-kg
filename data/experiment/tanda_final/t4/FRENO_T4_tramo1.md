# FRENO T4 de la tanda final, primer tramo (B6.1): la lectura asistida, las planillas, el LEEME y el convertidor

20/10/2026. Pre-registro firmado (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`), §6: «Quién lee: lectura asistida con revisión
de la autora (D2), como en el T4 de la tanda 1». USD 0, sin API. Nada commiteado y ningún mensaje de commit preparado. Todo lo nuevo está
en `data/experiment/tanda_final/t4/`.

## 1. Paso 0

La salida, con la carpeta personal reemplazada por `$HOME` (`t4/paso0/paso0_T4_salida.txt`, de `t4/scripts/paso0_t4.sh`):

```
== pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
== git log --format=%s -3
Registro de decisiones, tripletas y mandatos: la reaplicacion unica, la herramienta de puntos, el reintento por forma, las remisiones a un punto padre y la tercera enmienda de tripletas, firmados
Tanda final: el sello de sus dos grafos, segundo commit
Tanda final: los ocho ensamblados, el gate, el registro de sus dos grafos, lo contado sin leer y la preparacion de sus lecturas
== git log --format='%h %H' -3
7cbf3525 7cbf35256ad6497500a11508415d986ca876ad89
5aae4fe0 5aae4fe087b9ecf736c8e492ec158f2107995d47
71cb9305 71cb9305ee0be585643cf3f8e473bd96f00853bb
== git status --porcelain --untracked-files=no (entre las dos rayas)
--
--
== commit_sellado de la tanda final en grafos.py
280:    "KG_TandaFinal_r2b": {
282:        "label": "KG_TandaFinal_r2b",
285-        "commit_sellado": "71cb930",
294:    "KG_TandaFinal_r2b_sincola": {
296:        "label": "KG_TandaFinal_r2b_sincola",
299-        "commit_sellado": "71cb930",
== sha256 de las muestras, del material y de la derivada
muestra cola 4d447ca82b8355354c9e5a07b063fac57f0fa7716de167cc547abf479f0bcf93 True
muestra aceptadas:items 396f332812db8fd35d9878f2366eda529e1b535db4ecaf7d360d63622737799e True
muestra aceptadas:no_items 51bb8fd036bf4043c31b33be64fdd49d0d659f2fac2c909a24d72693409aa52c True
muestra vigilancia:2 da9849b0e9bae17a31e438339c05175ee0b4c6df179b89ec2af48a96313e3836 True
muestra vigilancia:7 deb59743ab54ef13a3fb46285176dd3822d3b222adedadc83569cd6a9d55fefc True
muestra vigilancia:1 1ec9d44f355998c0bc4016c33770797093cc19fbc5093f487ad74c310c1e5f02 True
muestra vigilancia:3 2b0d361b36345a0b85c64cced7fa259ba1df2d121f188ad8dbb1b11f695fb988 True
muestra observacion:12 646587039a469880e7180fd43ca1ecb58569198fce61af07154082583a60b79e True
material cola jsonl 75d630203b133c427268c021784ac542520daa02b920bdcfb5b13db97182c65c True
material cola md 0162485750338baf38a4db59d0e697f9e47d532505dd3e3ce6dc06c87eeb7a64 True
material aceptadas:items jsonl 5f88b8873ee835bdd1ab996347f48883eda53915c9a34b589bbcd8a4ba073dd2 True
material aceptadas:items md 49c851c82e8659beca806832adf1dc85a4535ddb01b2137424286308ff5de9b1 True
material aceptadas:no_items jsonl d02a69ada432d571e850449fdb1e0dc02f502efcd38f5ea7be0d35c1f3857b01 True
material aceptadas:no_items md 214f1d0281e0bc5c2372300eacef3eeb9a54a955f287570cacd866f3b552af78 True
material vigilancia:2 jsonl 8fd6edef58918df416037a11e3941a8c26f75881633d4fd3a3692efe8534b170 True
material vigilancia:2 md 19646b7604853de6e905e34400eff52c44c5a9ca094b0088a61c7717b710528c True
material vigilancia:7 jsonl bf50365e5d580d4f33085dff67f2264aa4cd66c149eccf57ba16bc9283a20ef3 True
material vigilancia:7 md 78bda5be873efed0c9ea79d57f889e5677dcffa4f821dee7639522ffb3f4d4e5 True
material vigilancia:1 jsonl 7d106d37a228750564e0b029d9008d8563ceeb1a93b816207a45a10c203ea217 True
material vigilancia:1 md 40d80848c676c03d316d7e7ab0854642bbc1f65f57ac67c8c5145f1a7d7a4a93 True
material vigilancia:3 jsonl f10de8fe8bbefb27ca8e38c9344a589af2588d567624f610d02e2f552f124862 True
material vigilancia:3 md 18e98b027ab0984a774936cb39283cc491b6a8e1a6b7536dfbf01c8138f36984 True
material observacion:12 jsonl bc38f9dd7e89c6be97e4f811bce6f164dc26ac7a64da9f4d647cec8e7c367cfb True
material observacion:12 md fed5c7e75cfb67ca77891468ef930391ff1f9a9d28c8692a9f7e8949e200cb3a True
derivada 26c29d9424ffaf634a02735a972ad29e7df8b06463b8ad430654d50d4d442fc2 True
ok True
rc=0
== la foto nueva contra la de después de T3 y los tres commits
{
 "rutas_en_los_commits": 2687,
 "por_estado_en_los_commits": {
  "A": 2683,
  "M": 4
 "nuevos": 8,
 "borrados": 0,
 "cambiados": 3,
 "nuevos_borrados_o_cambiados_fuera_de_los_commits": [],
 "rutas_de_los_commits_distintas_de_HEAD": [],
 "ok": true
}
rc=0
== .pyc: líneas y diff contra el cierre de T3
   11236
iguales
== pgrep -fl "runner_corpus.py|lanzar_t|correr_tanda"
rc=1
== pgrep -fl ensamblar_tanda0.py
rc=1
== hora
2026-10-20 16:35:12
```

El bloque de la foto sale filtrado: sin los sha256 de las dos fotos y sin las llaves que cierran. El JSON entero está en
`t4/paso0/foto_contra_commits_T4.json`.

Todo da lo esperado:
- el log tiene los tres commits en el orden pedido, y el `status` (sin los no rastreados) está vacío;
- los dos `commit_sellado` de la tanda final en `grafos.py` son `71cb930`, el hash corto del primero de los tres commits;
- las ocho muestras, los ocho `fichas_*.jsonl` y los ocho `fichas_*.md` tienen el sha256 de las tablas T5 y T6 del FRENO T3, y la
  versión derivada de la lectura, `26c29d9424ffaf634a02735a972ad29e7df8b06463b8ad430654d50d4d442fc2`;
- la foto nueva tiene 8 archivos nuevos, 0 borrados y 3 cambiados contra la de después de T3. Los
  11 son rutas de los tres commits (eb5ad14b..7cbf3525, 2.687 rutas), con el sha256 de su
  blob en HEAD (`paso0_foto_contra_commits_t4.py`);
- no corre ninguna extracción, y `pgrep -fl ensamblar_tanda0.py` no muestra procesos.

## 2. Lo decidido sobre el FRENO T3 final

Lo aplico como lo recibí: las cinco decisiones cierran; las 3.695 unidades a la vista son todas de TOs de la tanda final; los dos momentos
de lectura juntos quedan como desvío declarado del §6, sin firma nueva (FRENO T3, sección 7.7). Va a la §68 del registro de decisiones,
que no escribo.

## 3. La lectura asistida (punto 3)

- **Quién lee:** Claude Opus 5.5 (`claude-opus-5-5`), la ejecutora de esta sesión de Claude Code. Leí ficha por ficha y
  escribí cada propuesta, sin API ni otro modelo. La lectura va de las 16:40:09 a las 16:59:28
  del 2026-10-20 (el `st_birthtime` y el `st_mtime` de los borradores).
- **Cómo leí:** cada ficha en su `.jsonl` del material de T3, con `t4/scripts/ver_fichas_t4.py`, que solo la compacta (el mismo contenido
  que el `.md` de la autora, sin el estado de E3 ni sus marcas). Juzgué contra el texto que muestra la ficha. Las propuestas las fui
  escribiendo en borradores, una por ficha, con `t4/scripts/anotar_t4.py`, que controla las respuestas válidas del LEEME. Los borradores
  quedan en `t4/lectura_asistida/borradores/`.
- **Lo que queda:**
  - `t4/lectura_asistida/lectura_asistida_t4_tramo1.json`: el modelo, la hora, los criterios (`criterios_de_la_propuesta`), las reglas
    usadas y las 216 propuestas, cada una con su regla y una justificación que cita el texto;
  - `t4/lectura_asistida/omisiones_y_observaciones_t4_tramo1.md`: lo que va aparte. No cambia ninguna propuesta.
  - Los dos los arma `t4/scripts/armar_lectura_t4.py`, que controla los ids, las celdas y el orden contra las planillas en blanco de T3,
    la muestra y el material (sección 7).
- Sin tasas, sin umbrales, sin atención, sin freno y sin ampliación: son del segundo tramo.

Cuántas propuestas hay de cada respuesta, por muestra, y las reglas que usé (`t4/tablas_freno_t4.md`, de `t4/scripts/tablas_freno_t4.py`):

#### Tabla 1. Las propuestas, por muestra y por respuesta (`lectura_asistida/lectura_asistida_t4_tramo1.json`; modelo Claude Opus 5.5, `claude-opus-5-5`; de 16:40:09 a 16:59:28 del 2026-10-20)

| muestra | fichas | propuestas por respuesta | suma |
|---|---:|---|---:|
| cola | 30 | sin error 20; con error 5; dudosa 5 | 30 |
| aceptadas_items | 30 | sin error 26; con error 4; dudosa 0 | 30 |
| aceptadas_no_items | 30 | sin error 25; con error 5; dudosa 0 | 30 |
| vigilancia_2 | 30 | vaciamiento 5; no vaciamiento 25; no decidible 0 | 30 |
| vigilancia_7 | 6 | con apoyo 4; sin apoyo 2; no decidible 0 | 6 |
| vigilancia_1 | 30 | sí 6; no 24; no decidible 0 | 30 |
| vigilancia_3 | 30 | duplicación 3; distintos 27 | 30 |
| observacion_12 | 30 | correcta 29; no decidible 0; incorrecta (catálogo) 1 | 30 |
| total | 216 | — | 216 |

#### Tabla 2. Las reglas de la propuesta usadas, por muestra (`reglas_usadas`; definidas en `criterios_de_la_propuesta`)

| muestra | reglas |
|---|---|
| cola | `U-sostenida` 20; `U-tipo` 3; `U-fuera-del-texto` 3; `U-no-sostenida` 2; `U-dudosa` 2 |
| aceptadas_items | `U-sostenida` 26; `U-no-sostenida` 4 |
| aceptadas_no_items | `U-sostenida` 25; `U-tipo` 3; `U-no-sostenida` 2 |
| vigilancia_2 | `V2-sin-contenido` 14; `V2-marco-de-lista` 10; `V2-con-contenido` 3; `V2-dato-a-informar` 2; `V2-cubierto` 1 |
| vigilancia_7 | `V7-ejecutor-alcanzado` 4; `V7-otro-ejecutor` 2 |
| vigilancia_1 | `V1-condicion` 24; `V1-deber` 6 |
| vigilancia_3 | `V3-par-deber-acto` 21; `V3-contenido-distinto` 3; `V3-repite` 3; `V3-par-modalidad-acto` 3 |
| observacion_12 | `O12-correcta` 29; `O12-sujeto-de-otro-TO` 1 |

## 4. Las planillas, el LEEME y el convertidor (puntos 4 a 6)

- **Las planillas** (`t4/lectura_autora/<muestra>.csv`): UTF-8 sin BOM, «;» y «\n», con las columnas `id`, `celda`, `ficha`,
  `propuesta`, `justificacion`, `veredicto_autora` y `nota_autora`, las dos últimas vacías. Los ids y las celdas son los de las planillas
  en blanco de T3, en su orden. La columna `ficha` da la ruta del `.md` desde la raíz del repo y, tras «#», el número de su encabezado.
  Ninguna celda empieza con «=», «+», «-» ni «@».
- **El LEEME:** lo copié de la copia permanente de la mesa (solo ese archivo) a `t4/lectura_autora/LEEME_lectura_T4.md`. Su sha256 es
  el del «seguí». Sus rutas y nombres coinciden con lo armado: las ocho planillas `<muestra>.csv`, el material
  `t3/muestras/material/<m>/fichas_<m>.md`, las 216 fichas, los nombres de muestra del convertidor y los 24.949 elementos del universo de
  la (12) (la N de `poblaciones_t4t1_tf.json`). No lo cambié.
- **El convertidor** (`t4/lectura_autora/convertir_lectura_T4.py`) es el de la tanda 1 con el nombre de la tanda y los sha256 de las
  planillas nuevas. Este es todo el diff:

```diff
--- tanda1/t4/lectura_autora/convertir_lectura_T4.py
+++ tanda_final/t4/lectura_autora/convertir_lectura_T4.py
@@ -1 +1 @@
-"""Convierte la exportación de Numbers de una planilla de la lectura de T4 (tanda 1, primer tramo) en la planilla marcada que se sella.
+"""Convierte la exportación de Numbers de una planilla de la lectura de T4 (tanda final, primer tramo) en la planilla marcada que se sella.
@@ -26,8 +26,8 @@
-    "cola": "5f1fefe1887fd999a989a7414790018b6dc3390f3f4c256423cb84cd358f799a",
-    "aceptadas_items": "4932f4a80c8ae43d9667d280647e13bbc9f8f174f1d16da356961864d92fe439",
-    "aceptadas_no_items": "cc830b718cb13ccb595f95d1b0d0cc229f79802c1600c6f2665255d6ffec1e8a",
-    "vigilancia_2": "580e4b047d839b5f6a4528544645fe66b87037b5daee2505fbb2e8d311b55045",
-    "vigilancia_7": "b047d9ed7992ebc315eea8e55fe16a85233e8fa38d47cda5a85419649e17d7a1",
-    "vigilancia_1": "609577900a2522faf14fe0ba1fc6808ab89e58a352bb49028b2170bbcd52a52b",
-    "vigilancia_3": "099ab7e227a93d5ca0075f4e9286ef82139018c9bc74f86edd6e29462e50a3ae",
-    "observacion_12": "f4ba30e1831c1221d9f7b40214f01c437590182792ec85e096983853aeaf04a5"
+    "cola": "cf9c8d72e0f740eede87427225b318ad1ff636c9f85e18b7adebab42d8ec7954",
+    "aceptadas_items": "2811a5c78c6a06dfd4e90727e1331ebe9e2b66ce4b90c2dc68eac926d94679f5",
+    "aceptadas_no_items": "3ca4affa48b172dc0ad0dfa91201923184c708c9cfabb2797381515cd0844b69",
+    "vigilancia_2": "e41e1db8c64f4802c996d848ea5e827cf271d6fddbeafad91907558e1429d156",
+    "vigilancia_7": "1ecfa46039573186d74a121d8d11399b3e134589257feb16310720e53d4dbd4b",
+    "vigilancia_1": "5884316305ba70f4298cca7aed1ec9be9456e00cd93db5286164a50e9aa029b3",
+    "vigilancia_3": "13e70d15a0a0698f24bce68b9f88ef3c0671f202477054fa76a66d9ac5a2b917",
+    "observacion_12": "86186ed69c51fe768fd8881f241c8b5dfeb74598416712f22130e7ef18cd568f"
```

#### Tabla 3. Las planillas en blanco de la autora, el LEEME y el convertidor (sha256 recalculado aquí)

| archivo | sha256 | igual al del JSON de la lectura | igual al de SHA_PLANILLAS del convertidor |
|---|---|---|---|
| `t4/lectura_autora/cola.csv` | `cf9c8d72e0f740eede87427225b318ad1ff636c9f85e18b7adebab42d8ec7954` | True | True |
| `t4/lectura_autora/aceptadas_items.csv` | `2811a5c78c6a06dfd4e90727e1331ebe9e2b66ce4b90c2dc68eac926d94679f5` | True | True |
| `t4/lectura_autora/aceptadas_no_items.csv` | `3ca4affa48b172dc0ad0dfa91201923184c708c9cfabb2797381515cd0844b69` | True | True |
| `t4/lectura_autora/vigilancia_2.csv` | `e41e1db8c64f4802c996d848ea5e827cf271d6fddbeafad91907558e1429d156` | True | True |
| `t4/lectura_autora/vigilancia_7.csv` | `1ecfa46039573186d74a121d8d11399b3e134589257feb16310720e53d4dbd4b` | True | True |
| `t4/lectura_autora/vigilancia_1.csv` | `5884316305ba70f4298cca7aed1ec9be9456e00cd93db5286164a50e9aa029b3` | True | True |
| `t4/lectura_autora/vigilancia_3.csv` | `13e70d15a0a0698f24bce68b9f88ef3c0671f202477054fa76a66d9ac5a2b917` | True | True |
| `t4/lectura_autora/observacion_12.csv` | `86186ed69c51fe768fd8881f241c8b5dfeb74598416712f22130e7ef18cd568f` | True | True |
| `t4/lectura_autora/LEEME_lectura_T4.md` | `9e224f09213b0ca821bcbbf0af0c923c09251cb5bfd1f81d5b716697ea627525` | igual al del «seguí»: True | — |
| `t4/lectura_autora/convertir_lectura_T4.py` | `8be2e02d13f865c72ec8a9b38b297a81f4b81ebf54f74dce7458cb002db3a9c7` | — | muestras en SHA_PLANILLAS: 8 |

El convertidor de la tanda 1 (`data/experiment/tanda1/t4/lectura_autora/convertir_lectura_T4.py`, `e3e1150a92c5b712…`) y el de la tanda final difieren solo en la primera línea del docstring («tanda 1» → «tanda final») y en los ocho valores de SHA_PLANILLAS (`diff`, sección 4 del FRENO).

#### Tabla 4. La prueba del convertidor (`prueba_convertidor/prueba_convertidor_t4.json`; Python 3.12.13; fuera del repo)

| caso | código de salida (esperado) | lo que controla | ok |
|---|---|---|---|
| 1. válida (cola, BOM, «;», 3 cambios con nota) | 0 (0) | «OK: cola_marcada.csv» en la salida | True |
| 2. otra vez la misma: no pisa la marcada | 1 (1) | «ya existe: no la piso» en la salida | True |
| 3. válida (aceptadas_items, «,», CRLF y fila vacía al final) | 0 (0) | «saqué una fila vacía al final» en la salida | True |
| 4. respuesta mal escrita, vacía y cambio sin nota | 1 (1) | «3 PROBLEMA(S)» en la salida | True |
| 5. dos filas en otro orden | 1 (1) | «no son los de la planilla» en la salida | True |
| 6. columna de más con texto | 1 (1) | «columnas de más» en la salida | True |
| 7. una fila de menos | 1 (1) | «filas de datos» en la salida | True |
| 8a. (12): «incorrecta» sin capa | 1 (1) | «no es una de» en la salida | True |
| 8b. (12): «incorrecta (E1-prompt)» con nota | 0 (0) | «OK: observacion_12_marcada.csv» en la salida | True |
| 9. muestra que no existe | 1 (1) | «no es una de» en la salida | True |
| 10. la exportación es la planilla | 1 (1) | «no puede ser la planilla» en la salida | True |
| 11. planilla alterada (sha256 distinto) | 1 (1) | «sha256 distinto» en la salida | True |

El repo, antes y después de la prueba: `t4/lectura_autora/` con los mismos sha256 (True); la copia, igual al repo antes de probar (True) y sin enlaces (0); todos los casos como se esperaba: True.

- **Cómo controla los ids:** como el de la tanda 1, controla que el id y la celda de cada fila de la exportación sean los de la planilla,
  y que la planilla tenga su sha256. Los ids de cada planilla son los de su muestra: `armar_lectura_t4.py` lo controla contra
  `t3/muestras/<m>.json` antes de escribirla.
- **La prueba** (`t4/scripts/prueba_convertidor_t4.py`) corre sobre una copia sin enlaces armada en el scratchpad, con exportaciones de
  juguete. Los veredictos de juguete son las propuestas, salvo los cambios de cada caso; no son una lectura. La salida está en
  `t4/prueba_convertidor/`, y la copia con las exportaciones va en el paquete.
- **El sello** lo hace la autora, con las ocho marcadas (LEEME).

## 5. El cegamiento

- El material no trae el estado de E3 ni sus marcas: el control de T3 (`t3/muestras/control_material_tf.json`) da 0 claves vedadas.
- No abrí `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3` ni el gasto de los reintentos.
- Ninguna cifra de esta unidad los usa, así que no escribí `t4/NO_ABRIR_conteos_t4.json`: no hay nada que poner. Si la mesa lo quiere
  igual, vacío, lo agrego.
- **De la tanda 1** abrí solo dos cosas:
  - el convertidor (`tanda1/t4/lectura_autora/convertir_lectura_T4.py`; listé solo los `.py` de esa carpeta);
  - la sección 6 de `tanda1/t3/FRENO_T3.md`, por las definiciones de (1) y (3), que son «las que propuso la ejecutora en el FRENO T3, §6»
    (registro, §29).
  - No abrí sus muestras, su material, sus planillas ni su lectura asistida.
- No abrí ninguna carpeta vedada ni ningún `NO_ABRIR_`. No hice copias del repo: la prueba copia solo `t4/lectura_autora/`, sin `.env`, `NO_ABRIR_` ni `_SOLO_MESA` y sin enlaces (el control
  está en `control_final_T4.json` del paquete).

## 6. La foto del repo, los .pyc y el grep de convenciones

La foto del paso 0 y la de después (`t1/foto_repo_tanda_final_t1.py`, corrido desde su copia del scratchpad, con el mismo sha256,
`3220cf3c…`) quedan fuera del repo y del paquete, porque nombran todas las rutas del repo; su sha256 y su resumen están en `t4/resumen_fotos_T4.json` (de `t4/scripts/foto_t4.py`).

- **La foto.**
  - Paso 0: 16:32:09 a 16:32:24, 58.013 entradas.
  - Después: 17:04:00 a 17:04:16, 58.050 entradas,
    45 sin abrir y 342 enlaces.
  - **37 nuevos, todos en `tanda_final/t4/`:** 11 en `lectura_asistida/`; 10 en `lectura_autora/`; 3 en `paso0/`; 2 en `prueba_convertidor/`; 9 en `scripts/`; 2 en `t4/ (raíz)`.
  - **Nuevos fuera de `t4/`:** 0. **Borrados:** 0. **Cambiados:** 0.
  - Este FRENO, `t4/resumen_fotos_T4.json` y el script que los arma (`t4/scripts/freno_t4_armar.py`) se escriben después de la foto;
    el control final del paquete (`control_final_T4.json`) confirma que son los únicos nuevos desde ella.
- **Los `.pyc`:** 11.236 líneas en el paso 0 y 11.236 después; listas iguales: True. Todo
  corrió con `-B`.
- **El grep de convenciones** sobre los 37 archivos nuevos de `t4/`, sin los `NO_ABRIR_`:
  - 0 coincidencias de los tokens del nombre y de los términos, y 0 archivos con rutas absolutas;
  - control positivo, 2; tokens dentro de rutas absolutas, 0;
  - el script es `t3/scripts/grep_convenciones_tf.py`, sin cambios, con `LC_ALL=en_US.UTF-8`.
  - El grep del FRENO va en el control final del paquete.

## 7. El script de cada cifra

| cifra | script | salida |
|---|---|---|
| el paso 0 (log, status, `commit_sellado`, sha256, foto contra los commits, procesos) | `t4/scripts/paso0_t4.sh`, `paso0_sha_muestras_t4.py`, `paso0_foto_contra_commits_t4.py` | `t4/paso0/` |
| las propuestas por respuesta y las reglas (tablas 1 y 2) | `t4/scripts/tablas_freno_t4.py` (desde la lectura asistida) | `t4/tablas_freno_t4.md`, `t4/consola_tablas_freno_t4.txt` |
| la lectura asistida, las omisiones y las planillas, con sus controles | `t4/scripts/armar_lectura_t4.py` | `t4/lectura_asistida/`, `t4/lectura_autora/*.csv`, `t4/lectura_asistida/consola_armar_lectura_t4.txt` |
| los sha256 de las planillas, del LEEME y del convertidor (tabla 3) | `t4/scripts/tablas_freno_t4.py` | `t4/tablas_freno_t4.md` |
| la prueba del convertidor (tabla 4) | `t4/scripts/prueba_convertidor_t4.py` | `t4/prueba_convertidor/` |
| la foto y los `.pyc` | `t1/foto_repo_tanda_final_t1.py`, `t4/scripts/foto_t4.py` | `t4/resumen_fotos_T4.json` |
| el grep de convenciones | `t3/scripts/grep_convenciones_tf.py` | `t4/resumen_fotos_T4.json` («grep») |
| este FRENO | `t4/scripts/freno_t4_armar.py` | `t4/FRENO_T4_tramo1.md` |

## 8. Para la autora

- **Las planillas están listas para leer.** Cada fila trae mi propuesta, su justificación y la ruta de la ficha. Los criterios están en
  `criterios_de_la_propuesta`; los que más pueden pesar en la adjudicación son interpretaciones mías, fijadas antes de tu lectura:
  1. **U-tipo:** cuento como error de la unidad un tipo que contradice la modalidad del texto. Por ejemplo, un deber tipado Condicion o
     Excepcion, un permiso tipado Obligacion o un deber tipado Potestad, y el futuro normativo lo leo como deber. Son 3 de la cola
     y 3 de las aceptadas no ítems. Es la misma lectura que la «sí» de la (1).
  2. **U-fuera-del-texto:** un nodo sin pasaje en el texto que muestra la ficha lo propongo como dudosa. Vendría de la herencia que E1 ve y
     E3 no (§31). Son 3 de la cola.
  3. **La (2):**
     - el bloque que abre una lista lo propongo como «no vaciamiento», porque su deber y su sujeto pasan a cada ítem
       (`V2-marco-de-lista`, 10);
     - un dato que el régimen pide informar, sin nodo, como «vaciamiento» (`V2-dato-a-informar`,
       2).
  4. **La (3):** el par de una facultad o de un límite y el acto lo trato como el par del deber y el acto (`V3-par-modalidad-acto`,
     3).
  5. **La (12):** la única incorrecta va a «catálogo»: un sujeto resuelto al rol de alcance de otro TO.
- **La marca de cada fila es tuya:** el convertidor exige la razón en `nota_autora` cuando el veredicto cambia la propuesta.

## 9. Errores propios, con su causa

1. **El paso 0 dio un código de salida que no era el del script.** En la primera corrida de `paso0_t4.sh`, el `rc` del bloque de la foto
   era el del `grep` que filtraba la salida, no el del script, porque faltaba `pipefail`. Lo agregué y volví a correr el paso 0 entero
   antes de escribir nada; la salida de la sección 1 es la segunda.
2. **Dos justificaciones de la (3) no citaban el texto.** La 10 citaba el deber con otras palabras («se deberá considerar» por «se deberá
   tener en cuenta»), y la 26, la descripción del nodo («no podrá ser inferior al 25%») en lugar del texto. La causa: escribí esas
   justificaciones mirando solo las líneas de los nodos del grupo, sin el texto. Las encontré al releer contra el texto completo los
   grupos que propongo como duplicación, y las corregí en el borrador antes de armar las planillas.
3. **La regla de la ficha 12 de la cola no era la de los casos iguales.** Primero la anoté con la regla `U-dudosa`. Al ver que las fichas
   14 y 18 tenían el mismo caso (nodos sin pasaje en el texto que muestra la ficha), la pasé a `U-fuera-del-texto`. La propuesta, «dudosa»,
   no cambió.
4. **Un control de forma de las planillas dio un falso positivo.** El control de que ninguna celda empiece con «=», «+», «-» o «@» marcó
   las celdas vacías, por cómo tomaba el primer carácter. Lo corregí y lo volví a correr: 0 celdas.
5. **El control final falló la primera vez.** Corrí el grep con un entorno sin `HOME`, y git no encontró el nombre del usuario. Le pasé
   el entorno completo y volví a correr el control entero.

## 10. Lo que no hice

- **Las cifras del segundo tramo:** no calculé tasas, umbrales ni atención, y no sorteé ninguna ampliación.
- **Commits y escrituras ajenas:**
  - no commiteé ni preparé mensajes de commit;
  - no escribí en la memoria, en `.claude/` ni en `.gitignore`.
- **Lo que no toqué:** los grafos, los manifiestos, la E0, el código del pipeline, la fixture, `grafos.py`, Neo4j ni nada de `t3/`. De
  `t3/` solo leí, y corrí sin cambios su grep de convenciones.
- **El scratchpad:** nada que se necesite después queda solo en él. El paquete y su copia permanente llevan los borradores de origen,
  la copia de la prueba y las salidas.

FRENO T4, primer tramo: espero la revisión de la mesa y la lectura de la autora.
