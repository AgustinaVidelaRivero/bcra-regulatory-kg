# U-SEG-OFICIAL, S1-ter: registro de la adjudicación, la pasada 1 de la autora y la selección de la pasada 2 (mesa, 11/10/2026)

USD 0, sin API. Los archivos de las dos pasadas están fuera del repo, en `~/INGENIERIA IA/TESIS/fuera_del_repo/adjudicacion_s1ter/`, y
acá se citan por su sha256. No se corrió `armar` ni `aplicar_adjudicacion_S1ter.py`, ni se calcularon el piso ni el acuerdo: esperan a
que la autora selle la pasada 2.

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
