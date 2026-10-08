# U-SEG-OFICIAL — S0-4a-bis: raíz mayor que MAX_RAIZ dentro de un sub-documento, medición de ri_oc y herencia de 4a en la tanda 0

Etapa S0-4a-bis del mandato FIRMADO en `e543cb2` (las 239 líneas firmadas dan `44cf30ca0d82…`), con la nota al pie del
07/10/2026 (noche) que revisa el FRENO S0-4a y asienta las decisiones de la autora (`7788e52`, líneas 562 a 619 del
mandato), y con el «seguí» de S0-4a-bis, que fija el alcance: la regla de ri_ccna (ítems 31 a 40), la medición de ri_oc
sin aplicar, los controles duros con la regla prendida y apagada, el parche final con sus anclas, y el control de la
herencia de los 53 puntos 4a de la tanda 0. USD 0: ninguna llamada a la API. No edité el repo: el código es un parche
sobre `26c6502` (`parche/`), y este registro está armado en el scratchpad con la estructura que tendría en
`data/experiment/segmentacion_oficial_e0r2/s0_4/bis/`; se copia al repo en S0-4b. Ningún commit.

## 0. Método

- Estado al empezar (08/10/2026, 07:44): HEAD `7788e52`, sin cambios rastreados en el árbol de trabajo (solo
  `s1/e0/` y carpetas de `reports/` sin seguimiento, de otras unidades); ningún proceso de corridas vivo;
  `data/experiment/mantenimiento/selftest_clave_cache.json` del repo en `923dd900…`, el JSON vigente después de revertir
  O5 (nota al pie, (e)). El código de E0 del repo sigue siendo el de `26c6502` (`git diff --stat 26c6502 HEAD` de
  `e0_chunking/`, vacío).
- Copia: la de S0-4a (`HEAD f96ab49`, 0 enlaces), puesta al día con `7788e52`. Comparé cada archivo rastreado de
  `data/experiment/` y `docs/mandatos/` de HEAD con la copia por el sha1 de git: faltaban 82 y eran distintos 9, más
  los tres de `e0_chunking/` que llevan el código de S0-4a. Escribí en la copia los 91 desde `git cat-file` (sin
  tocar los tres de E0), y la copia sigue con 0 enlaces. Las salidas de r2b de la tanda 0 y las cachés de E1 y E3 de
  la copia tienen los mismos archivos, tamaños y fechas que las del repo (no abrí las del repo).
- Tres códigos, cada uno en una raíz mínima armada desde la copia (`../scripts/raiz_minima.sh`, 0 enlaces):
  `impl4bis`, el del parche final; `proto4bis`, el mismo con la variable `S0_4_REGLAS` que elige las reglas
  (`parche/parche_interruptores_prototipo_S0-4a-bis_sin_aplicar.diff`, como en S0-4a; no va al repo); y `oc4bis`, el
  prototipo con la variante de medición de ri_oc (`parche/parche_medicion_ri_oc_S0-4a-bis_sin_aplicar.diff`, §4; no se
  aplica).
- Corridas: el lote `scripts/lote_bis.sh` (registro en `censos/registro_lote_S0-4a-bis.txt`), con `manual` aparte y
  las corridas juntadas por TO (`../scripts/juntar_por_to.py`, el de S0-4a), y dos corridas chicas de los cinco TOs de
  la lista (sd solo y sd con sdmax). Las referencias de S0-4a son sus corridas de la sesión anterior: `final` (S0-4a con
  todas las reglas), `base` (S1, igual a `s1/e0/`) y `r_sd` (sd solo).

## 1. La regla sdmax

- **Qué hace.** Dentro de un sub-documento, en el modo sin raíz, una raíz explícita mayor que `MAX_RAIZ` (30) no se
  rechaza si sucede exactamente a la anterior; las guardas G0 a G3 de siempre rigen igual. Fuera de un sub-documento, o
  si no es la sucesora exacta, el rechazo `raiz_mayor_a_max` no cambia. Cada raíz que abre lleva el aviso
  `raiz_mayor_a_max_subdocumento_sdmax`.
- **Dónde.** `e0_lib.py`: el parámetro `raiz_max_subdoc` de `parsear_cuerpo` (:1387, apagado por default, con su
  docstring en :1438), la condición (:1738-1742), el aviso (:1785) y el rechazo de siempre (:1866-1867; en S0-4a,
  :1853). `correr_e0.py`: `"sdmax"` en `REGLAS_S0_4` (:128, con su comentario en :119-127) y el parámetro, que se pasa
  junto con la regla de sub-documento (:1340-1344). Corre solo donde corre sd: en los cinco TOs de
  `TOS_SUBDOCUMENTO_S0_4`, y solo con sd prendida.
- **Interruptor propio**: `"sdmax"` en `REGLAS_S0_4`; en el prototipo, `S0_4_REGLAS` la elige como a las demás.

## 2. Efecto y censo

- **En los 152** (`censos/controles_S0-4a-bis.txt`): contra S0-4a, la corrida final cambia solo en ri_ccna: 4 de 768
  archivos (`chunks_ri_ccna.json`, `estructura_ri_ccna.json` y, en `conteos.json` y `divergencias_indice_cuerpo.json`,
  solo la entrada de ri_ccna). Unidades: S0-4a 9.554 → S0-4a-bis 9.564.
- **ri_ccna** (`censos/censo_sdmax_sobre_S0-4a_S0-4a-bis.json`, `censos/censo_sdmax_sobre_sd_S0-4a-bis.json`): 149 →
  159 unidades, 11 eventos: `ri_ccna::D1A3::S30` pasa de 2.285 a 350 caracteres (queda solo el ítem 30, p. 20) y
  `ri_ccna::D1A3::S31` a `S40` son nuevas (pp. 20 y 21; de 71 a 308 caracteres); 10 rótulos nuevos y 10 avisos
  `raiz_mayor_a_max_subdocumento_sdmax`; los 10 rechazos `raiz_mayor_a_max` de ri_ccna desaparecen. Coincide con lo
  esperado por la mesa.
- **Los otros cuatro TOs de la lista** (ri_sef, nmcief, ri_icpipsp, ri_cc): sin cambios (archivos por TO iguales a los de
  S0-4a). En ri_sef, los códigos del Anexo II (`ri_sef::A2`, p. 7: 101 a 126, salvo 110 y 122, 24 renglones) siguen
  rechazados por `raiz_mayor_a_max`: no suceden a la raíz anterior.
- **Censo sobre los 152**: la regla no puede actuar fuera de un sub-documento, y los sub-documentos solo se abren en
  los cinco TOs de la lista; en ellos abre 10 raíces, todas en ri_ccna.
- **Límite declarado que queda en el Anexo III de ri_ccna** (decisión de la autora: la 5 del §8 de S0-4a como límite
  declarado, salvo ri_ccna 31 a 40). La lista A («A. GENERAL») y la B («B. PRUEBAS SUSTANTIVAS») comparten el espacio de
  ids de las raíces del anexo. Los ítems 1 y 2 de A.2 abren `D1A3::S1` y `S2`; A.3 (un párrafo, 212 caracteres), el
  rótulo «B. PRUEBAS SUSTANTIVAS» y los ítems B.1 y B.2 (547 caracteres) quedan dentro de `ri_ccna::D1A3::S2` (1.450
  caracteres; el ítem A.2.2 propio son 668), porque 1 y 2 no suceden a la raíz 2. Desde B.3, cada ítem abre su raíz
  (`S3` a `S40`), y ninguna de sus 47 unidades (con los sub-ítems 26.1 a 26.6 y 29.1 a 29.3) hereda «B. PRUEBAS
  SUSTANTIVAS»: su herencia es «ANEXO III», y en 26 y 29 también el ítem y su chapeau. En S0-4a eran 2 unidades
  (`S2` y `S30`) con 12 de los 40 ítems de la lista B bajo el id de otro ítem (B.1, B.2 y B.31 a B.40), la cifra de la
  mesa. Con sdmax queda 1 unidad (`S2`), con 2 de los 40 (B.1 y B.2) y con A.3.

## 3. Controles duros, con la regla prendida y apagada

Todos en `censos/controles_S0-4a-bis.txt` y `censos/tanda0_S0-4a-bis.txt`, byte a byte (`../scripts/cmp_dirs.py`):
- **Tanda 0, 57 de 57**, en seis corridas: la final (`impl4bis`, dos veces, iguales entre sí), todo apagado, todas menos
  sdmax, sdmax sola y sd con sdmax. La regla va por lista (solo en sub-documentos de los cinco TOs de la lista, ninguno
  de la tanda 0), así que no puede tocarla.
- **Los 25 archivos de la tanda 0 dentro de los 152**, iguales en las dos corridas finales (agregados: 20 iguales y 15
  ausentes en los dos; `../scripts/control_tanda0_en_152.py`).
- **Regla apagada**: todas las reglas menos sdmax (`proto4bis`) da la corrida final de S0-4a, 768 de 768.
- **Regla prendida**: contra S0-4a cambian solo los archivos de ri_ccna (§2).
- **Todo apagado = S1**: 768 de 768 contra la E0 de S1 de S0-4a (`corridas/base`) y contra los sha256 de los 768
  archivos `e0/` de `s1/manifest_salida.json` (`ee7c07c`; `scripts/contra_manifiesto_s1.py`).
- **Doble corrida** de los 152 con el código final: 768 y 768, 0 distintos.
- **Prototipo y código**: el prototipo con todas las reglas da, en los 64 TOs que cambian contra S1, los mismos 320
  archivos por TO que el código sin interruptores.
- **Selftest de claves** (`data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b`, desde la raíz de la
  copia, con el código final instalado en su `e0_chunking/`): VEREDICTO OK; anclaje r2b de E1 y de E3 OK; contraste con
  la tabla OK; su salida es igual byte a byte al JSON vigente del repo (`923dd900…`, el de después de revertir O5):
  ninguna clave de la tanda 0 se mueve (`censos/selftest_claves_S0-4a-bis.txt`).
- **Selftests de E0** sobre la copia (§8): en verde.

## 4. ri_oc: medición, sin aplicar

- **Qué medí** (`parche/parche_medicion_ri_oc_S0-4a-bis_sin_aplicar.diff`, raíz `oc4bis`): ri_oc sumado a la lista de
  sub-documento por la variable `S0_4_SD_MEDICION`, con una guarda: un régimen en la página 1 es el del propio TO y no
  abre sub-documento ni prefija ids. Sin la guarda, el detector toma «B.C.R.A. 10 – OPERACIONES DE CAMBIOS» (el
  encabezado corrido de cada página, p. 1) como régimen `R10`, y todos los ids de ri_oc llevarían `R10::`. La guarda va
  sobre la página 1 literal, no sobre la primera página de cuerpo: ri_cc abre su régimen 4 en la p. 49, que es su primera
  página de cuerpo. En los cinco TOs de la lista no hay ningún régimen en la página 1, así que la guarda no los tocaría.
  Corrí ri_oc con todas las reglas, con la variante (`oc_med`) y sin ella (`oc_ref`, igual byte a byte a ri_oc en la
  corrida final: 5 de 5 archivos).
- **Resultado** (`censos/medicion_ri_oc_S0-4a-bis.json`, `scripts/medicion_ri_oc.py`): ri_oc pasa de 128 a 133
  unidades, con 12 eventos. Se abren dos sub-documentos, `A1` (Anexo I, p. 22) y `A2` (Anexo II, p. 23), sin prefijo
  de régimen.
  - `ri_oc::3.51` cambia: de 19.239 caracteres en las pp. 15 a 25 pasa a 12.206 en las pp. 15 a 21 (F01). Lo que sale
    son 7.032 caracteres de los dos anexos.
  - 5 unidades nuevas (F19b): `ri_oc::A1::S0` (338, la lista de códigos de instrumentos), `A2::S0` (30, el rótulo) y
    `A2::S1` a `S3` (3.502, 2.197 y 961: los capítulos 1 a 3 del Anexo II, que hoy van dentro de 3.51).
  - 3 renombres con el mismo texto (F05 y F02): `ri_oc::S4`, `S5` y `S6` (los capítulos 4 a 6 del Anexo II, que hoy ya
    se abren como raíces) pasan a `ri_oc::A2::S4` a `S6`, y heredan «ANEXO II: Códigos de conceptos».
- **El Apartado B no se separa.** «APARTADO B: POSICIÓN GENERAL DE CAMBIOS» (pp. 16 a 21) es texto de otro apartado,
  pero ninguna forma de sub-documento lo reconoce: queda dentro de `ri_oc::3.51`, que con la variante tiene 779
  caracteres del punto 3.51 y 11.427 del Apartado B (con sus ítems B.1, B.1.1…), y hereda solo «3.».
- **Para la condición 12 de la tanda 1**: con la variante, `ri_oc::3.51` baja de 19.239 a 12.206 caracteres, bajo el
  umbral de 13.944, y las unidades de más de 13.944 caracteres propios en los 152 pasarían de 29 a 28 (son 34 en S1,
  29 en S0-4a y 29 en S0-4a-bis). Sin la variante, `ri_oc::3.51` queda como está (19.239) y entra a la lista de la
  condición 12, como dice la nota al pie.
- **No la apliqué**: ni la variante ni ri_oc están en el parche final; la autora decide con la cifra (§10).

## 5. Tanda 0: la herencia de los 53 puntos de la clase 4a

- **Pregunta de la autora**: para los 53 puntos de la clase 4a de la tanda 0 (`../censos/censo_4ab_sobre_S0-3.json`,
  clave `tanda0_limite_declarado`), ¿la oración que E0 tomó como título está en el texto heredado de las unidades hijas,
  o sea, la veía E1?
- **Método** (`scripts/herencia_4a_tanda0.py`): la oración es el título del punto, como lo leyó E0 en
  `salida_tanda0_r2b/estructura_<to>.json`, más los renglones de su intro hasta el primero que termina en punto o en
  dos puntos (el criterio de `e0_lib.clase_titulo_4ab`). En cada unidad descendiente del punto (`chunks_<to>.json`,
  ids que empiezan con «<to>::<punto>.»), busco el título y la continuación en sus tramos de herencia, con los espacios
  y los saltos de renglón normalizados. Lo heredado es lo que E1 ve: el mensaje de E1 r2b escribe cada tramo de la
  herencia tal cual (`reextraccion_v2/e1_extractor/prompt_r2b.py:423-425` en `7788e52`).
- **Resultado** (`censos/herencia_4a_tanda0_S0-4a-bis.json`): **53 de 53 sí**, 0 no. Las 249 unidades descendientes
  (de 2 a 13 por punto) heredan las dos partes: el título partido como tramo `encabezado` del punto y la continuación
  como su tramo `intro`. Por TO: ext 37, ctacte 8, cap 3, polcre 2, cla 1, lingob 1 y pro 1.
- **Control negativo**: en una copia de la salida, saqué de una unidad hija (`cap::2.7.2.2`) el tramo `intro` de
  2.7.2; el script da 52 sí y 1 no, con la continuación como faltante.
- **Lo que esto no dice**: E1 ve la oración entera, pero partida en dos tramos, y el primero rotulado como encabezado del
  punto (en `cap::2.7.2`, «… las entida-» en el encabezado y «des financieras deberán considerar…» en la intro). El
  contenido llega; lo que queda es el rótulo.
- **Cifra a declarar** (decisión (a) de la autora; `../censos/censo_4ab_sobre_S0-3.json`): 123 puntos de la familia del
  mecanismo 4 en la tanda 0, de los que 4a y 4b tocarían 114 (53 por 4a y 61 por 4b, 22 de ellos retirando la intro)
  y 9 no tienen regla; en los 53 de 4a, E1 veía la oración entera en la herencia de las unidades hijas.

## 6. Conciliación por regla

- **Contra S0-4a** (`censos/atribucion_S0-4a-bis_contra_S0-4a.json`, `atribuir.py` de S0-1 con sdmax por resta contra
  la corrida sin ella): 1 TO, 11 eventos, todos de sdmax sola (`cambia` 1, `nuevo` 10); interacción, 0.
- **Los mismos 11 eventos sobre sd sola** (`censos/eventos_sdmax_S0-4a-bis.json`, `scripts/eventos_sdmax.py`): sd sola
  con el código nuevo es igual, byte a byte, a sd sola de S0-4a (25 de 25 archivos por TO), y sdmax sobre sd sola
  produce los mismos 11 eventos con el mismo contenido (texto, herencia, páginas, marcas y tipo) que sobre S0-4a.
- **Contra S1** (`censos/atribucion_S0-4a-bis_contra_S1.json`, con las mismas corridas de cada regla sola de S0-4a, sdg3
  por resta contra la corrida final sin sdg3 en los cinco TOs de la lista y sdmax por resta contra la final sin sdmax):
  64 TOs, 1.540 eventos, que son los 1.530 de S0-4a más 10 `nuevo|sdmax` (`D1A3::S31` a `S40`). `D1A3::S30` ya era un
  id nuevo contra S1 (por sd): la atribución identifica cada evento por su tipo y su id, así que su cambio de texto por
  sdmax no suma un evento contra S1 (sí contra S0-4a). La única interacción sigue siendo `nmcief::A4::S1`. Antes de
  usarla, reproduje con el mismo script la atribución de S0-4a contra S1: da los mismos datos que
  `../censos/atribucion_S0-4_contra_S1.json` (cambia solo el orden de las claves de `tos_por_regla`, que sigue el de los
  argumentos).
- **Unidades contra S1** (`censos/censo_final_bis_contra_S1.json`): 9.554 → 9.564 (+367 −357), en 64 TOs (65 con
  ri_mmsef, que cambia solo su estructura; §9).
- **Tabla de reprocesamiento** (`censos/filas_por_regla_S0-4a-bis.json`, `filas_por_regla.py` de S0-2): sdmax toca F19b
  (10 unidades nuevas) y F01 (`D1A3::S30`, texto propio). La variante de ri_oc tocaría F19b (las 5 unidades nuevas),
  F05 y F02 (los 3 renombres) y F01 (`ri_oc::3.51`; `censos/filas_medicion_ri_oc_S0-4a-bis.json`). Ninguna fila nueva.

## 7. El parche final y las anclas de F19b

- **Parche** (`parche/`, con su LEEME; verificado aplicándolo sobre los archivos de `git show 26c6502:…` por los dos
  caminos, directo y sobre el de S0-4a):
  - `e0_lib.py` `7e56f857…` (+621 −48 sobre `26c6502`; +19 −6 sobre S0-4a);
  - `correr_e0.py` `2559b6c2…` (+61 −10; +12 −9);
  - `selftest_e0.py` `a776126d…` (+477 −9; +39 −6).
  Reemplaza al de S0-4a para S0-4b.
- **Anclas de F19b** (`scripts/anclas_f19b.py`: mapea cada renglón ancla de `26c6502` al renglón con el mismo
  contenido; todas contiguas). La fila cita `correr_e0.py:95-100`, `:327-339`, `:576-585` y `:1266`, y `e0_lib.py:352`
  y `:473`.
  - Con el parche de S0-4a, el script reproduce la referencia de la mesa: `correr_e0.py:327 → :352`, `:576 → :601`,
    `:1266 → :1294`; `e0_lib.py:352 → :359`, `:473 → :551`; `:95-100` no se mueve.
  - Con el parche final, que es el que vale para S0-4b: `correr_e0.py:95-100` (no se mueve), `:327-339 → :353-365`,
    `:576-585 → :602-611`, `:1266 → :1295`; `e0_lib.py:352 → :360`, `:473 → :552`.
  - La tabla no la edito: S0-4b pone las anclas al día al aplicar el parche.

## 8. Selftests

Sobre la copia, con el código final (`censos/selftests_e0_S0-4a-bis.txt`): `selftest_e0` **137/137**: los 134 de
S0-4a, dos de ellos ampliados en q (el parámetro de sdmax, apagado por default; `"sdmax"` en `REGLAS_S0_4`), más tres
nuevos, el caso sintético (r) y dos medidos (s). b52 39/39, b581 34/34, b582 59/59 y b583 33/33.
- **Caso sintético** (r): una parte con las raíces 1 a 31 y la 33, y otra con el código 101. Sin la regla, la última
  raíz es la 30 (la 31 se rechaza por `MAX_RAIZ`); con ella, se abre la 31, que sucede a la 30. La 33 y el 101 siguen
  rechazados, hay un solo aviso sdmax (el de la 31), y fuera de un sub-documento la regla no corre.
- **Casos medidos** (s): en ri_ccna, `D1A3::S31` a `S40` existen, `S30` tiene 350 caracteres y no lleva el 31, y el TO
  tiene 159 unidades; en ri_sef, los 24 rechazos `raiz_mayor_a_max` del Anexo II siguen y no hay aviso sdmax.

## 9. Correcciones al registro de S0-4a

Dos afirmaciones del diseño de S0-4a que la revisión de la mesa marcó, verificadas ahora contra los archivos:
- **ri_tsa no es `parcial_declarado`.** El diseño de S0-4a (§1.1 y §7) dice que ri_tsa y ri2_pm «siguen
  `parcial_declarado`». En `s1/controles_S1.json`, `por_to.ri_tsa.clase` es `reconocido_pleno`; solo ri2_pm es
  `parcial_declarado`.
- **ri_mmsef cambia 3 avisos y un campo, no un aviso.** El diseño de S0-4a (§5) dice que ri_mmsef «cambia solo un
  aviso de la estructura». Contra S1 (`corridas/base` → `corridas/final` de S0-4a), sus chunks, índice, pies y tablas
  son iguales; en la estructura cambian el campo `secciones` y 3 avisos, todos de la p. 3: sale `padre_reabierto_r2`
  de 2.2 y entran `cuerpo_al_rotulo_m1` (forma a del mecanismo 1 de S0-3, en 2.2) y `aceptado_con_columna_derivada`
  (2.2.1).
Las dos van como errores propios (§12). El diseño de S0-4a no lo edité: S0-4b, al copiarlo al repo, le agrega una nota
fechada con estas dos correcciones (PENDIENTE).

## 10. Decisiones de la autora (PENDIENTES)

1. **ri_oc** (§4): sumarlo a la lista de sub-documento con la guarda del régimen de la página 1, o dejarlo como límite
   declarado y en la lista de la condición 12 de la tanda 1. Con la variante, `ri_oc::3.51` baja de 19.239 a 12.206
   caracteres (bajo 13.944) y los anexos quedan aparte (5 unidades nuevas y 3 renombres); el Apartado B (11.427
   caracteres) sigue dentro de 3.51 en los dos casos. Si se aplica, la guarda es código nuevo: necesita su interruptor,
   su caso en el selftest y los controles duros otra vez antes de S0-4b, porque el código de E0 se cambia una sola vez.
2. **El límite de ri_ccna que queda** (§2): A.3, B.1 y B.2 dentro de `ri_ccna::D1A3::S2` (1.450 caracteres), y las 47
   unidades de los ítems B.3 a B.40 sin «B. PRUEBAS SUSTANTIVAS» en su herencia. Lo dejo declarado con esa cifra,
   según la decisión 5; la autora confirma la redacción.
3. **Las dos correcciones al diseño de S0-4a** (§9): S0-4b las agrega como nota fechada al copiarlo al repo.

## 11. Comandos

Desde la raíz del scratchpad. Las rutas `../` son las de S0-4a. `herr/` es mi carpeta de herramientas: su
`correr_152.py` es igual a `../../s0_1/scripts/correr_152.py`, y sus `correr_tanda0_par.py`, `juntar_por_to.py`,
`cmp_dirs.py`, `control_tanda0_en_152.py` y `raiz_minima.sh` son iguales a los de `../scripts/` (comprobado con `cmp`).
`scripts/comparar_e0.py` es una copia de `../../s0_1/scripts/comparar_e0.py`, que `censo_s04bis.py` importa.

```
scripts/lote_bis.sh <scratchpad> <python>                  (el lote: corridas, selftests de E0 y selftest de claves)
herr/correr_152.py --codigo raices/proto4bis --salida <dir> --workers <n> --tos <tos>   (con S0_4_REGLAS=<reglas>)
scripts/controles_bis.sh <scratchpad> <python>             (tanda 0 y controles de configuración, byte a byte)
scripts/por_to_iguales.py <a> <b> <tos>                    (los cinco archivos por TO, byte a byte)
scripts/censo_s04bis.py <base> <nueva> <salida.json> [--tos a,b]   (el censo de S0-4 con el aviso de sdmax)
scripts/eventos_sdmax.py <antes_1> <después_1> <antes_2> <después_2> <tos> <salida.json>
scripts/medicion_ri_oc.py <referencia> <medición> <salida.json>
scripts/herencia_4a_tanda0.py ../censos/censo_4ab_sobre_S0-3.json <salida_tanda0_r2b> <salida.json>
scripts/anclas_f19b.py <código de 26c6502> <código nuevo> […]
copia/data/experiment/segmentacion_oficial_e0r2/s0_1/scripts/atribuir.py --base corridas/base \
    --todas bis/corridas/bis_final --regla <r>=corridas/r_<r>,corridas/base … \
    --resta sdg3=bis/corridas/bis_sin_sdg3,bis/corridas/bis_final --resta sdmax=bis/corridas/bis_sinmax --out <json>
data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b \
    data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b --out <json>          (desde la raíz de la copia)
data/experiment/reextraccion_v2/e0_chunking/selftest_{e0,b52,b581,b582,b583}.py   (desde e0_chunking/ de la copia)
../scripts/raiz_minima.sh copia raices/<raíz> <dir con el código>
../scripts/grep_convenciones.py <repo> <paquete>             (el de S0-4a)
```

## 12. Errores propios, con su causa

1. **ri_tsa como `parcial_declarado`, en el diseño de S0-4a** (§9). Causa: le atribuí a ri_tsa la clase de ri2_pm
   porque las dos quedan fuera de la lista por la misma razón, sin leer su clase en `s1/controles_S1.json`. Lo marcó la
   revisión de la mesa.
2. **«ri_mmsef cambia solo un aviso», en el diseño de S0-4a** (§9). Causa: repetí la descripción del FRENO S0-3
   («como en S0-3») sin recontar la diferencia de S0-4 contra S1, que son 3 avisos y el campo `secciones`. Lo marcó la
   revisión de la mesa.
3. **Dos anclas y un nombre de aviso mal escritos en un borrador de este diseño**, corregidos antes de entregar,
   contra el código: el comentario de `REGLAS_S0_4` en `correr_e0.py:119-127` (había escrito :117-125) y los avisos de
   ri_mmsef con su tipo exacto. Causa: los escribí de memoria antes de leer el archivo.
4. **Un renglón de más de 120 caracteres** en el comentario de `REGLAS_S0_4` de la primera versión del código de
   sdmax; lo reacomodé antes de la primera corrida, así que todas las corridas usan el código final (sha en el
   registro del lote).
5. **Un control comparaba contra una carpeta que la copia no tiene.** La primera versión de `scripts/controles_bis.sh`
   comparaba la corrida con todo apagado contra `s1/e0/` de la copia, y dio 768 «distintos». Causa: la copia de S0-4a se
   armó sin `s1/e0/` (lo dice su §0) y no lo comprobé antes de escribir la línea. La reemplacé por la comparación contra
   los sha256 de `s1/manifest_salida.json` (768 de 768) y volví a correr el script entero.

## Nota posterior (08/10/2026, S0-4b)

Nota fechada; el texto de arriba es el revisado, sin cambios (sha256 del texto sin esta nota: `644be88671276f9f…`).
Corrección: los 11.427 caracteres de `ri_oc::3.51` que no eran del punto (§4, y §10, decisión 1) no son el Apartado B
solo. Son 4.659 del Apartado B (pp. 16 y 17) y 6.768 del Apartado C con los criterios de validación y las aclaraciones
(1.380 del Apartado C, p. 18, y 5.388 de los criterios y las aclaraciones, pp. 19 a 21); el «11.427» los sumaba como
Apartado B. La medición está en el diseño de S0-4a-ter (`../ter/DISENO_S0-4a-ter.md`, §9). Con la regla apl de
S0-4a-ter, `ri_oc::3.51` queda con su texto (778 caracteres) y los Apartados B y C son unidades propias.

Además, el código que S0-4b aplicó al repo es el de S0-4a-ter (`../ter/parche/`), que incluye este; las anclas de
este diseño son las del parche de S0-4a-bis.
