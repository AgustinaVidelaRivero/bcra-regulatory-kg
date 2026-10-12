# U-SEG-OFICIAL, S1-ter: registro de la adjudicación: la pasada 1 de la autora, la selección, la pasada 2 y el cierre (mesa, 11/10/2026)

USD 0, sin API. Los archivos de las dos pasadas están fuera del repo, en `~/INGENIERIA IA/TESIS/fuera_del_repo/adjudicacion_s1ter/`, y
acá se citan por su sha256. Hasta que la autora selló la pasada 2 no se corrió `armar` ni `aplicar_adjudicacion_S1ter.py`, ni se
calcularon el piso ni el acuerdo. Corrieron después, el 11/10/2026 (§7).

## 1. La pasada 1 de la autora, sellada

| etapa | archivo (en `pasada_1/etapa_N/`) | sha256 | sello |
|---|---|---|---|
| 1 | `adjudicacion_pasada_1_etapa_1.tsv` | `21815741534ac272deedd1899a44d64e218e2c86df08fb3c638aefda9949547d` | `sello_adjudicacion_pasada_1_etapa_1.txt` |
| 1 | `criterios_pasada_1_etapa_1.md` | `fec12170579282e1743315adba8eeaa699e37a23a5bda6769e0977edb1a190a1` | `sello_criterios_pasada_1_etapa_1.txt` |
| 2 | `adjudicacion_pasada_1_etapa_2.tsv` | `ebca1469b6383b9cc102e252b3c8169cbeac7d7d8471c571d3047d976a6f7465` | `sello_adjudicacion_pasada_1_etapa_2.txt` |
| 2 | `criterios_pasada_1_etapa_2.md` | `cdf8a9c25bd39aeeb17617f566fe33f6f56ab101d802e5953e754f078ba2b10c` | `sello_criterios_pasada_1_etapa_2.txt` |

- **Etapa 1.** El TSV y los criterios no cambian desde las 10:07:49 del 11/10/2026 (fecha de modificación). Los dos archivos de sello se
  crearon a las 10:09:06 y a las 10:09:12, y se reescribieron a las 10:14:42 con el mismo sha256: su renglón de fecha dice
  «2026-10-11 10:14:42 -0300». Datos de `stat` de la mesa.
- **Etapa 2.** El TSV no cambia desde las 16:06:28 y los criterios desde las 16:07:10. Los dos sellos son de las 16:08:52.
- **La verificación de la mesa** (11/10/2026, desde las 16:21:33) siguió el método (`metodo_adjudicacion_S1ter.md`):
  - tomó el sha256 de cada archivo de sello, sin calcularlo del TSV, y se lo pasó a `pasada_2_S1ter_v2.py`, que lo controla;
  - los cuatro archivos dan el sha256 de su sello;
  - con un sha256 equivocado el script frena sin escribir nada.

## 2. Lo que la autora vio antes de sellar sus pasadas 1

**Declaración de la autora del 11/10/2026:** «El 11/10/2026, mientras hacía la pasada 1 de la etapa 1, la autora llevó su propia cuenta
provisional de errores de corte y vio que superaba el límite del piso; con eso decidió el cambio del plan B del §62. No vio nada de la
lectora antes de sellar sus dos pasadas 1.»

- **Lo que la mesa puede anclar:**
  - la decisión del cambio del plan B le llegó a las 09:26:15 (hoja de ruta de la mesa, §62; nota al pie de
    `docs/mandatos/USEG_OFICIAL_S0-5a_reglas_de_corte_E0.md`, `e95413bb`), antes del primer sello de la etapa 1 (10:09:06);
  - el material con las marcas de la lectora (§3) lo armó la mesa a las 16:23:31 y lo instaló a las 16:25:55, después de los sellos de
    las dos etapas.
- Que no vio nada de la lectora antes es su declaración.

## 3. La selección de la pasada 2

- **Script:** `pasada_2_S1ter_v2.py seleccionar` (sha256 `ae0396d3…`, el del sello de los scripts de las 18:38:13 del 10/10/2026), a
  las 16:23:31, sobre copias.
- **Entradas,** con el sha256 tomado de sus archivos de sello:
  - la pasada 1 de las dos etapas (§1);
  - las planillas selladas de la lectora: `planilla_etapa_1.tsv` (`90b4e7aa…`) y `planilla_etapa_2.tsv` (`a06cdd0a…`), los registrados en
    `../lectura/incidentes_lectura_S1ter.md`.
- **Regla:** la a–d de la pasada 2 (decisión de la autora del 10/10/2026, hoja de ruta de la mesa, §56).
- **Salida:**

  | etapa | fichas en la pasada 2 | planilla de la pasada 2 (sha256) |
  |---|---|---|
  | 1 | 39 | `266be430d47ec2e1395825e5674d49d0eb26afdd3d807eafa1db9df3c32b3199` |
  | 2 | 68 | `2d09c49cc6fef25917e09d1db13770c19ad58544ed2bd54eba02bdab4ac586b4` |

  - Las cifras se leyeron como TSV, no por renglones.
  - Otra corrida da los mismos bytes.
- **El material** está en `fuera_del_repo/adjudicacion_s1ter/pasada_2/etapa_N/`. Por etapa lleva:
  - las fichas seleccionadas, con la condición que las trae, la fila de la pasada 1 y la de la lectora;
  - sus imágenes;
  - la planilla;
  - un LEEME;
  - un `manifest.txt`: `c223b9292c62827825419f83d497123b7b9d8391b619f54f3467fc9988594705` (etapa 1) y
    `c7f160401bc0fd480016184b8b41c6bad37532840a7cadf00c791dbd95d12d23` (etapa 2).
- **El script sellado no cambió.** `pasada_2_S1ter_v2.py` da `ae0396d3…` en el repo, en HEAD, en la copia que corrió y en su sello, y
  no tiene ningún control sobre «::».
- **Las notas de la autora no entran en la selección.** La regla a–d (`pasada_2_S1ter_v2.py:93-103`) lee la nota de la lectora, no la de
  la autora. Prueba de la mesa (11/10/2026, salida escrita a las 16:41:20, según `stat`; en un directorio temporal fuera del repo): la versión sellada, sobre copias de los dos
  TSV de la pasada 1 con la columna `nota` vaciada, selecciona los mismos ids, en el mismo orden, en las dos etapas. El sha256 de cada
  lista de ids (unidos por salto) es `a0c35839c64e247b14148ee785a423ad512bd364a60c222f66ea561f4701f31a` (etapa 1) y
  `b0d7ffdc06a30ca3f4c6a391e01ceb8e450aa95fb61875db079e5553c0338566` (etapa 2), igual con las notas y sin ellas.
- **El material lo armó un script de la mesa,** `armar_material_pasada_2_S1ter_mesa.py` (`12cf1af24ffa75c4c77bbf427f7a167aede2d2d85250718e3bfd2bcbc3392074`,
  en el paquete de la mesa), que no toca la selección.
  - Su control de «::» (`:114-115`) corre sobre la ficha y la fila de la lectora; la fila de la autora va tal cual.
  - Hubo dos versiones antes, que no se guardaron:
    - la primera frenaba por «::» en todo el texto, también en las notas de la autora, y no llegó a escribir el material;
    - la segunda tenía el control de ahora y difería de la final solo en una frase del LEEME. Su material se borró y se rearmó.
  - El material instalado es el de la versión final.
- **De dónde salen las fichas y las imágenes:** de una copia de las carpetas finales de la lectora reproducida por la mesa, cuyo
  `manifest.txt` da el de `../tramo_b2/fichas_numero_registro_S1ter.json` en las dos etapas.
- **Lo que no se corre todavía:** `armar` usa la planilla de la pasada 2 tal cual. No se corre, y tampoco `aplicar_adjudicacion_S1ter.py`
  ni el cálculo del piso y del acuerdo, hasta que la autora selle la pasada 2.

## 4. Qué leyó la mesa fuera del repo, y con qué comandos (11/10/2026, de 16:21:33 a 16:25:55)

Leer estaba permitido. En esas carpetas no se escribió nada.

- **`fuera_del_repo/adjudicacion_s1ter/pasada_1/`:**
  - `ls -la` de la carpeta, que muestra sus dos subcarpetas, `etapa_1/` y `etapa_2/`;
  - `cat` de los cuatro archivos de sello buscados primero en la raíz de la carpeta. No existen ahí: el comando falló sin leer nada;
  - en `etapa_1/` y `etapa_2/`: `cat` de los dos archivos de sello de cada etapa, y `ls -la` del TSV y de los criterios;
  - `stat` de los ocho archivos (fecha de creación y de modificación);
  - `cp -p` de esos ocho archivos a una carpeta de trabajo de la mesa, fuera del repo. La verificación, `seleccionar` y el material
    corrieron sobre esas copias.
  - No se listó el contenido de `etapa_1/` ni de `etapa_2/` ni se abrió ningún otro archivo.
- **Las dos carpetas de la lectora** (`fuera_del_repo/lecturas_ciegas/lectura_segmentacion_s1ter/etapa_1/` y `etapa_2/`): `cp -p` de
  `planilla_etapa_N.tsv` y `sello_etapa_N.txt` a la carpeta de trabajo. Ni listados ni otros archivos.
- **Las fichas y las imágenes del material** no salen de ninguna de esas carpetas, sino de la copia reproducida (§3).

## 5. La pasada 2 de la autora y sus cuatro notas de criterios, selladas

Las planillas están en `pasada_2/etapa_N/`, y las notas en `fuera_del_repo/adjudicacion_s1ter/`, cada una con su sello al lado.

| archivo | sha256 | sello (renglón de fecha) |
|---|---|---|
| `pasada_2/etapa_1/adjudicacion_pasada_2_etapa_1.tsv` | `f67e236023df9cfc78332aa89d00c0ffbf6b980831b2b7d7c2723f0dcaffa9a3` | `sello_adjudicacion_pasada_2_etapa_1.txt` (17:52:46) |
| `pasada_2/etapa_2/adjudicacion_pasada_2_etapa_2.tsv` | `a7068119e2e2335ee5882891a1cace80ffbb22455a115f59b3c523ced241285d` | `sello_adjudicacion_pasada_2_etapa_2.txt` (18:22:15) |
| `nota_criterios_antes_pasada_2.md` | `18fe56ba2d564d2b5f1f33d773610b2a7bbce646f4f5968e949490f47032c893` | `sello_nota_criterios_antes_pasada_2.txt` (17:12:05) |
| `nota_criterios_antes_pasada_2_adenda.md` | `c24fc62bee35a14ae8fe408d44349ab048fc5f24d5eaed680a9d3e4b2d7d960f` | `sello_nota_criterios_antes_pasada_2_adenda.txt` (17:21:23) |
| `nota_criterios_antes_pasada_2_adenda_2.md` | `98fb9c611a2e54a94cd9f1aa2e017039f751bf52c80a58bbdde754fd6ca3bddd` | `sello_nota_criterios_antes_pasada_2_adenda_2.txt` (17:40:38) |
| `nota_criterios_antes_pasada_2_adenda_3.md` | `b6adef6f7d5dd2a7ee3523c10003f09aa10f7c375270705c761e38bf1f2a4fe4` | `sello_nota_criterios_antes_pasada_2_adenda_3.txt` (18:19:27) |

Todas las horas son del 11/10/2026, -0300.

- **Datos de `stat` de la mesa:**
  - el TSV de la etapa 1 no cambia desde las 17:45:53, y su sello se creó a las 17:52:44;
  - el de la etapa 2 no cambia desde las 18:20:37, y su sello se creó a las 18:22:10;
  - las notas se crearon a las 17:12:05, 17:21:23, 17:40:38 y 18:18:23. Cada sello se creó a la misma hora que su nota. El de la
    adenda 3 se reescribió a las 18:19:27, la hora de su renglón de fecha.
- **La verificación de la mesa** (11/10/2026, desde las 18:30:09) siguió el método (`metodo_adjudicacion_S1ter.md`):
  - copió con `cp -p` solo esos doce archivos a una carpeta de trabajo fuera del repo. Las copias dan el sha256 de los originales;
  - tomó el sha256 de cada archivo de sello, sin calcularlo del archivo sellado. Los seis archivos dan el de su sello, que es además el
    que dio la autora;
  - a `armar` le pasó el sha256 de los sellos de las planillas, y el script lo controla. Con uno equivocado, frena sin escribir nada.
- **Qué leyó la mesa fuera del repo:**
  - ubicó los doce archivos con `[ -e … ]`, sin listar carpetas;
  - corrió `cat` de los seis sellos y `stat` de los doce archivos, y los copió con `cp -p`;
  - leyó las cuatro notas en la copia.
  - En esas carpetas no escribió nada. Solo creó en `fuera_del_repo/adjudicacion_s1ter/` la carpeta nueva `errores_confirmados/`,
    con el TSV de errores confirmados, que después reemplazó por su segunda versión (§7).

## 6. El control de forma, antes de `armar`

- **Decisión de la autora del 11/10/2026,** tomada antes de sellar la pasada 2: hoja de ruta de la mesa, §66, escrita a las 16:51:33.
  A las 16:51:17 ninguna etapa tenía sello de la pasada 2. Sobre cada planilla sellada de la pasada 2 se controla que:
  1. cada renglón tenga las columnas del encabezado;
  2. no haya comillas dobles;
  3. la columna `ficha` sea la de la selección: las mismas fichas, en el mismo orden, que la salida de `seleccionar` (`266be430…` y
     `2d09c49c…`).

  Si algo falla, la mesa frena sin correr nada, y la autora corrige y vuelve a sellar. Los scripts sellados no cambian.
- **Aclaración, decisión de la autora del 11/10/2026, posterior al sello** (recibida a las 18:28:05): el control de comillas dobles
  mira solo sus columnas, de `marca` a `nota`. Las columnas `lectora_…` vienen del material con comillas y son de solo lectura.
  - La salida de `seleccionar` ya trae comillas dobles en columnas de la lectora de la etapa 1, y en ninguna de la autora.
- **El control:** `control_forma_pasada_2_S1ter_mesa.py`
  (`72933ffe4a973c8c826934fe0c058405ca818b2fa82f9e4cc574daa49c812255`, en el paquete de la mesa).
  - Antes de leer cada planilla, controla su sha256 con el de su sello.
  - La lee por renglones y tabulaciones, sin el módulo `csv`, porque el error que busca está justo en cómo se parten los campos.
- **Resultado** (18:32:55): seis de seis ok, tres por etapa.
  - Sobre la salida de `seleccionar`, sin cambios, también da seis de seis.
  - Además, las columnas `lectora_…` de las dos planillas selladas son, byte a byte, las de esa salida.
- **Prueba en contra,** sobre copias de la planilla de la etapa 1 (`prueba_en_contra_control_forma_mesa.sh`,
  `ffcfc4be9c5bceb2de73f5785168f27c08e5f765cbedc2247150041d7202b41d`):
  - con una tabulación en una nota, una comilla doble en una nota o dos fichas cambiadas de orden, da MAL en el punto que corresponde;
  - con una comilla doble en una columna de la lectora, da ok;
  - con un sha256 equivocado, frena.

## 7. `armar`, `aplicar`, el piso y el acuerdo

- **Cuándo y con qué:** corrieron el 11/10/2026 a las 18:34:53, sobre copias. Los scripts sellados, sin cambios, se copiaron de HEAD
  (`13616dc8`):

  | script | sha256 | dónde está sellado |
  |---|---|---|
  | `adjudicacion/pasada_2_S1ter_v2.py armar` | `ae0396d3…` | `adjudicacion/sello_scripts_adjudicacion_v2_mesa.txt` |
  | `scripts/aplicar_adjudicacion_S1ter.py` | `c6316c8b…` | `tramo_b2/manifest_tramo_b2_S1ter.json` |
  | `scripts/cifras_lectura_S1ter.py` (el piso) | `65cd828b…` | `tramo_b/manifest_tramo_b_S1ter.json` |
  | `adjudicacion/acuerdo_etapa_1_S1ter.py` (el acuerdo) | `24bc1465…` | `adjudicacion/sello_acuerdo_etapa_1_mesa.txt` |

- **Entradas,** con el sha256 de su sello:
  - la pasada 1 (§1), las planillas de la lectora (§3) y la pasada 2 (§5);
  - `tramo_b/orden_lectura_S1ter.json` (`acd57e37…`) y `tramo_b/poblaciones_finales_S1ter.json` (`b47aee40…`), los de
    `tramo_b/sellos_S1ter_b.txt`;
  - `poblaciones_S1ter.json` (`a1313bd6…`, el de HEAD).
- **Resultado:** ningún script frenó, y dos corridas dan los mismos bytes. El comando es `correr_cierre_S1ter_mesa.sh`
  (`5ae30ede2f6c2e73d17863ef13a70f3abb435de44f5eda622579312f2dbe5053`, en el paquete de la mesa).
- **Salidas,** en el paquete de la mesa (`adjudicacion_S1ter_cierre_mesa/corrida/`):

  | script | salida (nombre en el paquete) | sha256 |
  |---|---|---|
  | `armar` | `adjudicacion_final_etapa_1_S1ter.tsv` (el TSV final; `armar` lo llama `adjudicacion_etapa_1.tsv`) | `6516e6c1dad7fa25174c5623dee17c5859120b1e2acf6d344429c0de9969680f` |
  | `armar` | `adjudicacion_final_etapa_2_S1ter.tsv` (ídem, `adjudicacion_etapa_2.tsv`) | `41235ad28424171db574858d14de4f1948fba78c93cf8f8a835d1d15483fca05` |
  | `armar` | `acuerdo_lectora_pasada_1_S1ter.json` | `76f41d0d3f9eb34651802a9701d588bb1301bc975774dab1b5f8267ea6a1d559` |
  | `aplicar` | `planilla_adjudicada_etapa_1_S1ter.tsv` | `1b1d35c0ab8be39c0e0d5a536ba749147edb049284e77e9d435c27895f26ab92` |
  | `aplicar` | `planilla_adjudicada_etapa_2_S1ter.tsv` | `7c9adf14381752255c9eb10e64583200e1793b8ba084267712d771fb55e85db5` |
  | `aplicar` | `registro_aplicar_adjudicacion_S1ter.json` | `e4dde326c90d34432b61f2bd6fd332f0d12543523000652ea0e7622ab308112d` |
  | el piso | `cifras_lectura_S1ter_adjudicada.json` | `74d6a9207473b3ccbc0d5fbfc9453b476c50a00a8fc8c8a3b604ca183422aa66` |
  | el acuerdo | `acuerdo_etapa_1_S1ter.json` | `2ad356ea339b9a322496e0c476c5cc97eee798c73eeb4de6e59b3fdd25fccca6` |

  Decide la versión del piso con las dudosas como error (`nota_piso_dudosas_S1ter.md`).
- **Decisión de la autora del 11/10/2026:** las salidas quedan fuera del repo, en el paquete de la mesa, hasta que se selle la lectura
  de S1-quater. Este registro lleva solo su sha256, sin las cifras.
- **Errores confirmados:** `fuera_del_repo/adjudicacion_s1ter/errores_confirmados/errores_confirmados_S1ter.tsv`
  (`5fe8a7ddda7c97dc6e37ec763778edb2f78df6fb340ad4238d195321abcb9def`), de solo lectura, con copia en el paquete de la mesa.
  - **Decisión de la autora del 11/10/2026:** sirve para agrupar los errores por mecanismo.
  - **Contenido:** un renglón por error de las dos etapas, sacado del TSV final de `armar`. Columnas: ficha, etapa, documento, id de la
    unidad en E0, pregunta (`la_unidad`, `la_que_sigue` o `la_herencia`), clase, subclase, subclase adicional, limpieza y la nota de
    la autora. No lleva columnas de la lectora.
  - **La columna `limpieza`** se sumó por decisión de la autora del 11/10/2026. Esta segunda versión reemplaza a la primera, que no la
    tenía (`578880e2…`, guardada en el paquete de la mesa); fuera de esa columna, las dos son iguales. La columna va solo en las filas
    de `la_unidad`. Una fila con `limpieza` y sin marca `error` haría frenar al script, y no hay ninguna.
  - **El id de la unidad:**
    - en `la_que_sigue`, es el de la unidad que le sigue en E0, calculada como `siguiente` de `scripts/fichas_S1ter.py`;
    - en `la_herencia`, es el de la unidad de la ficha, y van sin clase ni subclase, porque el TSV de adjudicación no las tiene.
  - **Lo arma** `lista_y_errores_S1ter_mesa.py` (`dda0946ac9f971e25de91efd8e05d68f49d78a09d841162ea7bbbc212d50a63f`, en el paquete
    de la mesa). Lee de E0 solo `e0/chunks_<documento>.json` de S1-ter: 77 archivos, cada uno controlado contra `manifest_salida.json`.

## 8. Fichas de la etapa 1 fuera de la pasada 2 que D3 o la adenda 3 podrían alcanzar

- **Decisión de la autora del 11/10/2026:** se declaran las fichas de la etapa 1 que reúnen tres condiciones:
  - no están en la pasada 2;
  - en la pasada 1 de la autora tienen marca `error`;
  - su unidad de E0 es un bloque declarado: id terminado en `::intro` o `::cierre`, `tipo` `mini_chunk` o título con `[bloque …]`.

  Quedan como en la pasada 1; solo se declaran.
- **Ninguna.** Todas las fichas de la etapa 1 con marca `error` en la pasada 1 de la autora están en la pasada 2.
- **Cómo lo controlé,** de dos maneras, sobre las copias de la pasada 1 (`21815741…`) y de la selección (`266be430…`):
  - con `lista_y_errores_S1ter_mesa.py`, que alcanza con una de las tres señales de la unidad;
  - con `awk`: los ids con marca `error` en la pasada 1, menos los de la selección, no dejan ninguno.
- **Con el control de la adenda 3** (unidad de `tipo` `seccion_sin_puntos`), ninguna ficha de la etapa 1 fuera de la pasada 2 lo
  tiene: las nueve de la etapa 1 están en la pasada 2 (`control_secciones_y_bloques_S1ter_mesa.py`, §9).

## 9. Declaración de la autora sobre la adjudicación

Texto de la autora, palabra por palabra:

> Declaración de la autora sobre la adjudicación de S1-ter.
> 1. La pasada 1, con asistencia de un modelo. Durante la pasada 1 de las dos etapas, la autora trabajó con un asistente de IA (Claude Opus 5.5, el mismo modelo que las lectoras). Los archivos de criterios sellados de la pasada 1 (fec12170… y cdf8a9c2…) registran que el asistente aplicó el criterio a fichas concretas, miró sus imágenes, marcó o recomendó marcas en varias de ellas y tomó una decisión de criterio delegada (D1). Eso se aparta de metodo_adjudicacion_S1ter.md, que fija que ningún modelo propone marcas. El acuerdo lectora–autora se calcula sobre la pasada 1 y es lo más afectado: no compara al modelo con un juicio humano independiente.
> 2. La pasada 2, hecha por un modelo con la autora. La pasada 2 de las dos etapas la hizo un asistente de IA (Claude Opus 5.5) junto con la autora. El asistente miró las imágenes, aplicó el criterio a cada ficha, propuso las marcas y las decisiones de criterio, y redactó la nota y las tres adendas; la autora participó y aprobó sus decisiones. Aparte, otro asistente de IA del mismo modelo vio solo las filas de la autora y de la lectora, sin imágenes ni texto de las unidades, y señaló qué regla del criterio estaba en juego en cada ficha. Esto también se aparta de metodo_adjudicacion_S1ter.md. Por eso la cifra de la E0 antes de la corrección no descansa en un juicio humano independiente. No alcanza a S1-quater.
> 3. Criterios fijados durante la pasada 2. Se fijaron en cuatro notas selladas: la nota (18fe56ba…, 17:12:05), escrita después de ver las fichas 1 a 15 de la etapa 1; la adenda 1 (c24fc62b…, 17:21:23); la adenda 2 (98fb9c61…, 17:40:38), que revoca C8 y extiende D3 a la etapa 1; y la adenda 3 (b6adef6f…, 18:19:27), que reescribe D11 y resuelve un hueco del criterio sobre los títulos sin número. Las adendas 2 y 3 se escribieron después de ver las marcas y notas de la lectora de las fichas que alcanzan. La adenda 2 se aplicó a todas las fichas de la pasada 2 de la etapa 1 en esa situación; una de ellas se decidió dos veces, la primera con C8. La adenda 3 se selló después que la pasada 2 de la etapa 1 y se aplicó solo a la etapa 2. Las nueve fichas de la etapa 1 cuya unidad es una sección sin puntos (E1-004, E1-006, E1-007, E1-018, E1-029, E1-047, E1-065, E1-071 y E1-089) no se revisaron con ella. Por decisión de la autora, la etapa 1 no se reabrió, porque ya estaba sellada y la cifra del piso ya se conoce. La adenda 3 nombra cinco fichas de la etapa 2 en esa situación y el control de la mesa encuentra seis: falta E2-056, que ya era error por la misma razón.
> 4. Una cuenta contra el piso durante la pasada 2. La adenda 2, sellada antes que las pasadas 2 (17:52:46 y 18:22:15), incluye una cuenta de los errores de corte de la etapa 1 comparada con el límite del piso. El método fijaba no hacer esa cuenta durante la adjudicación.
> 5. Notas de la pasada 1 sin fundamento. En dos fichas de la etapa 1, la nota de la pasada 1 se apoyaba en texto que se creía perdido y que está en una unidad vecina declarada; lo registra la adenda 2.
> 6. Límite de un control. El control de herencia por ancestros usado en la pasada 2 se apoya en las etiquetas de E0 y no detecta un bloque mal etiquetado; esos casos se detectaron midiendo la sangría.
> 7. Fichas fuera de la pasada 2. Las fichas de la etapa 1 que no entraron en la pasada 2 no se revisaron con D3 ni con la adenda 3, y quedan como en la pasada 1. El control de la mesa no encontró ninguna marcada error que sea un bloque declarado.

**Lo que dicen las notas sobre quién hizo la pasada 2** (párrafo de la mesa, por decisión de la autora del 11/10/2026). Las frases
van tal cual, con el sha256 de cada archivo y su renglón:

- **La nota,** `nota_criterios_antes_pasada_2.md` (`18fe56ba2d564d2b5f1f33d773610b2a7bbce646f4f5968e949490f47032c893`):
  - «La escribe el modelo, que es quien hace la pasada 2 por decisión de la autora del 11/10/2026 («tocás solo tus columnas, y solo
    donde decidas otra cosa»).» (`:7-8`)
  - «Las entradas 1 y 3 son decisiones que el modelo puede tomar porque los criterios son suyos» (`:9-10`)
  - sobre la confirmación de C2: «la confirma el modelo, no la autora.» (`:31`)
- **La adenda 1,** `nota_criterios_antes_pasada_2_adenda.md` (`c24fc62bee35a14ae8fe408d44349ab048fc5f24d5eaed680a9d3e4b2d7d960f`):
  - «Después de sellar la nota, la autora proveyó, en forma de tabla, qué dicen las tres etiquetas que la entrada 2 había dejado
    abiertas. La entrada 2 decía que el modelo no podía cerrarlas.» (`:8-9`)
  - sobre E1-049: «se decidió en la pasada 2 con C2 y contra la imagen de la p27» (`:18-19`)
- **La adenda 2,** `nota_criterios_antes_pasada_2_adenda_2.md`
  (`98fb9c611a2e54a94cd9f1aa2e017039f751bf52c80a58bbdde754fd6ca3bddd`). No dice quién la escribe. Dice: «El campo que decide apareció
  al consultar los datos de E0 durante la pasada 2.» (`:24`)
- **La adenda 3,** `nota_criterios_antes_pasada_2_adenda_3.md`
  (`b6adef6f7d5dd2a7ee3523c10003f09aa10f7c375270705c761e38bf1f2a4fe4`). No dice quién la escribe. Dice que se escribió «durante la
  pasada 2 de la etapa 2, después de ver las marcas y notas de la lectora de E2-033, E2-066, E2-094 y E2-099» (`:3-4`).

**Lo que la mesa puede anclar:**

- **Las horas** (§5):
  - la nota y las adendas 1 y 2 se sellaron antes que las dos pasadas 2;
  - la adenda 3 (18:19:27) se selló después del sello de la pasada 2 de la etapa 1 (17:52:46) y antes del de la etapa 2 (18:22:15).
- **Punto 1:** lo registran los criterios de la pasada 1.
  - Etapa 1: `criterios_pasada_1_etapa_1.md:62` y `:105`, y C9 (`:153-177`, «error del modelo»).
  - Etapa 2: `criterios_pasada_1_etapa_2.md:28` (D1, «decisión delegada al modelo»), y las decisiones tomadas «sobre la propuesta del
    modelo» o «sobre la recomendación del modelo» (`:117`, `:195`, `:237`, `:263`, `:281` y `:338`).
- **Punto 2:**
  - las frases del párrafo anterior;
  - que el método reserva la marca final a la autora y le da a la mesa de apoyo solo señalar la regla en juego:
    `metodo_adjudicacion_S1ter.md`, «Quién pone la marca»;
  - el material en texto que la mesa armó para la mesa de apoyo no lleva imágenes ni texto de las unidades. Son
    `para_mesa_de_apoyo_etapa_1.md` (`7684d03dc6fc019bcea9634baaa880888159e75ca789c4fd6d3bc173fbd4fc8c`) y
    `para_mesa_de_apoyo_etapa_2.md` (`a0acf67fb96b9e820b077e146498c1b9206f8f1a6fa5f98d0f72495cbd6fadc4`), en
    `fuera_del_repo/adjudicacion_s1ter/pasada_2/para_mesa_de_apoyo/`, controlados campo por campo contra el material.
- **Punto 3:**
  - las nueve fichas de la etapa 1 y las seis de la etapa 2 salen del control de la mesa `control_secciones_y_bloques_S1ter_mesa.py`
    (`31f621ab2f41bd76a9097df75ff9b1e314f1735b264c069aa4601d8491110488`, en el paquete de la mesa), sobre E0. Es el mismo control
    que usa la adenda 3: unidad de `tipo` `seccion_sin_puntos` y, en la etapa 2, también la unidad que le sigue. Su salida, sin
    marcas, es `secciones_sin_puntos_pasada_2_S1ter.json` (`9a5b5c88ba75fbc900e744b53974da7dcda6762e22e259d75801d7ef8b8893eb`);
  - la adenda 3 dice que se escribió durante la pasada 2 de la etapa 2 (párrafo anterior), y su sello es posterior al de la pasada 2 de
    la etapa 1;
  - la adenda 2 nombra su alcance, y la ficha decidida dos veces es E1-017;
  - que la adenda 2 se aplicó a todas las fichas de la etapa 1 en esa situación, y la decisión de no reabrir la etapa 1, son de la
    autora.
- **Punto 4,** que el método fijaba no hacer esa cuenta: el repo no lo dice con esas palabras. Lo más cercano es el motivo del diseño
  de la etapa 1 (`LEEME_adjudicacion_S1ter.md:13`), y que el piso y el acuerdo esperaban al sello de la pasada 2 (§3 de este
  registro).
- **Punto 5:** la adenda 2 declara las dos notas sin fundamento (E1-076 y E1-050).
- **Punto 6:** la adenda 3 usa la sangría en una ficha. Lo demás es declaración de la autora.
- **Punto 7:** el §8, con D3 y con el control de la adenda 3.
- **NO VERIFICADO por la mesa:** que la autora participó y aprobó las decisiones del asistente, y qué vio el otro asistente. Es
  declaración de la autora.

## 10. Unidades de documentos de la tanda 0 leídas en S1-ter (declaración, 12/10/2026)

- **Decisión de la autora del 12/10/2026:** si alguna de las 90 fichas de la etapa 1 es de un documento de la tanda 0, se declara en
  este registro. La cifra de S1-ter no se recalcula.
- **Con qué E0 se leyeron.** La tanda 0 quedó fuera de las reglas de S0-4 (4a y 4b) y de S0-5 por lista
  (`reextraccion_v2/e0_chunking/correr_e0.py:138` y `:156`).
  - Sus cinco documentos que están entre los 152 (ctacte, lingob, polcre, pagjub y docvig) se leyeron en S1-ter con la E0 de
    `salida_tanda0_r2b/`, sin esas reglas.
  - S0-5b controla esa E0 byte a byte: los 25 archivos de la tanda 0 dentro de los 152 dan 25 de 25.
- **Etapa 1:** 5 de las 90 fichas son de esos documentos, todas del estrato `vigente`:
  - E1-013, de docvig;
  - E1-021 y E1-048, de ctacte;
  - E1-038, de lingob;
  - E1-045, de polcre.
- **Etapa 2:** E2-025, de ctacte, y E2-055, de polcre. Las dos son de c116_a, y se leyeron con su unidad que sigue.
- **La cifra de S1-ter no se recalcula.** El cálculo ya informa aparte los errores de corte en documentos de la tanda 0
  (`scripts/cifras_lectura_S1ter.py:164-165`).
- **Lo que sigue** (decisiones de la autora del 12/10/2026, adenda 2 a su nota de decisiones de la corrección de E0,
  `1a25529306e6118bfa9696e1b6e7512e7190356c038f977f57c64770a119d9f1`):
  - la tanda 0 sigue fuera de la corrección de E0 de S0-6a;
  - sus unidades no entran en la población de S1-quater (adenda 1 al diseño de S1-quater).
- **Cómo lo controlé.** Usé el orden sellado de S1-ter (`tramo_b/orden_lectura_S1ter.json`, `acd57e37…`) y la E0 que leyó S1-ter,
  controlada contra `manifest_salida.json`.
  - Para las unidades de la etapa 2 usé `E0.partes` y `E0.siguiente` del diseño sellado de S1-quater.
  - El script es `fichas_tanda0_S1ter_mesa.py` (`ea88a1fc…`, en el paquete de la mesa).
  - Da 9 unidades, las mismas que `comun_S1quater.mostradas_S1ter` cuenta en esos documentos.
