# FRENO B6.3-b2 bis — la excepción cerrada del testigo, sus pruebas y su reaplicación sobre la captura de la b2 (28/10/2026)

Unidad: B6.3, etapa b2 bis del runner. Costó USD 0. No hubo ninguna sesión nueva: no lancé ningún CLI ni ningún servidor MCP, y no hice
ninguna llamada a la API ni toqué ningún Neo4j.

En el repo escribí solo archivos nuevos: 2 en `data/experiment/banco_mcp/aislamiento/`, 2 en `b63/v2/b2bis/` (la reaplicación y su
lista de sha256) y este FRENO. No edité nada de HEAD, de la b1, de la b1 bis ni de la b2. Tampoco cambié las configs selladas, el
testigo de la b2 ni `leer_testigo`. No commiteé nada. Espero la revisión.

**El resultado.** Reaplicado sobre la captura de la b2, el testigo v2 da:
- `PASS_de_B63` true;
- `PASS_del_testigo_tal_cual` false, por 16 renglones: los 12 de la fecha y los 4 de la ventana de la nota de las configs de
  fragmentos en el `log_r1`;
- `excepcion_aplicada`: los 4 renglones, en las sesiones T2, T3, T5 y T6, en el renglón 0 del `log_r1` (`inicio`), campo `config.nota`.

Antes de aplicar la excepción, la reaplicación reproduce la b2 tal cual: cada campo de cada sesión, el FRENO, el PASS, los sha256 por
brazo y pedido, y las otras conexiones.

Los artefactos largos van en el paquete `revision_B63_FRENO_b2_bis/` (§8), por su nombre.

## 0. Los criterios

| # | criterio | dónde | resultado |
|---|---|---|---|
| 1 | el paso 0, con la captura | §1 | lo esperado; la captura, completa (95 de 95 del tar.gz, 12 de 12 pedidos con su sha256) |
| 2 | el diff del testigo v2 contra el de la b2: cambia solo en la excepción y en el resultado | §2 | +137 −24 en 10 bloques, todos de la excepción o del resultado |
| 3 | cada prueba, con su resultado, dos veces iguales | §3 | 12 de 12, dos veces, iguales byte a byte; el selftest de la b2, 3 de 3, igual al de la b2 |
| 4 | la reaplicación: los tres campos | §4 | `PASS_de_B63` true, `PASS_del_testigo_tal_cual` false con su causa, 4 renglones en `excepcion_aplicada` |
| 5 | el repo: solo archivos nuevos, con su lista y sus sha256; lo demás, igual; el grep, 0 | §5 y §8 | 5 nuevos; 60.292 entradas comparadas, 0 cambian; grep 0 en lo del repo |

Hubo errores propios (§6). El único que tocó el repo es un archivo intermedio que escribí ahí y borré antes de la foto después
(error 3). Uno es de la regla de las búsquedas: un `find` sin poda por nombre, sobre la captura, que no tiene nada vedado (error 5).

## 1. El paso 0

`paso0_b2bis.zsh` y `control_captura_b2bis.py`, en el scratchpad (`paso0_B63_b2bis.txt`). Tal cual, con la carpeta personal como `$HOME`:

```
paso 0 de B6.3-b2 bis, 28/10/2026 10:54:56 -0300
el scratchpad: <carpeta temporal>/d7b988e9-4130-42c4-b289-914468756f63/scratchpad
  revision_B63_FRENO_b2/ en la copia permanente: manifest.txt f847c42118bce856920e92202d196bfa8aaf6caabc4af67f5c2ccda347ce765b
    la copia permanente contra su manifest.txt: verificados 98 de 98; distintos o ausentes 0; sin entrada 0
  revision_B63_FRENO_b2/ en el scratchpad: manifest.txt f847c42118bce856920e92202d196bfa8aaf6caabc4af67f5c2ccda347ce765b; igual al de la copia permanente
    el scratchpad contra el mismo manifest.txt: verificados 98 de 98; distintos o ausentes 0; sin entrada 0
la captura de la b2 (el --tmp de medir_testigo_b63.py, <carpeta temporal>/…/scratchpad/b2/real/tmp):
  a. el tar.gz del paquete de la b2 (1aff74c2…): 95 archivos; iguales en la captura 95; distintos o ausentes 0; en la captura y no en el tar, fuera de la captura privada: 0
  b. la captura privada: 8 carpetas, las de las 8 sesiones del resultado: True; pedidos de las sesiones con su sha256 y sus bytes: 12 de 12; negativos con sus pedidos: 4; fallas []
  c. testigo_resultado.json de la captura, enmascarado, igual a testigo_resultado_B63b2.json del paquete: True
  d. de las 8 sesiones: stream y log_r1 en todas, y sesion_<id>.json y su carpeta de configuración en las 6 del testigo: True
  la captura de la b2: COMPLETA
  rc=0
pwd: $HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
HEAD: 1d1ff7f495f6cfb0ccd5df44bdb7eca62299673b
git status --porcelain --untracked-files=no, con las vedadas podadas por ruta y *_SOLO_MESA*/NO_ABRIR_* por nombre: []
sin rastrear en b63/: 65
  git status --porcelain --untracked-files=all -- data/experiment/banco_mcp/b63 | LC_ALL=C sort | shasum -a 256: 4e94a8d46a847163c557468d0647ee246f806965ec16dbd26acb2c1022a2e41c
  b63/v2/sha256_etapa_b1_b63.txt: OK (19 renglones)
  b63/v2/b1bis/sha256_etapa_b1bis_b63.txt: OK (18 renglones)
  b63/v2/b2/sha256_etapa_b2_b63.txt: OK (24 renglones)
aislamiento/:
  27c87f52e6e44118a580c924a9ca589a7de04b430f8c1b3fc288c4adde30dc7d  testigo_aislamiento_b63.py
  7e7395aaf78adbef513baf7f2b055d230cde10b15e52877fd616980a3c707592  selftest_testigo_aislamiento_b63.py
```

En el scratchpad no faltaba nada, así que no restauré nada. La foto antes del repo es de las 10:55:08 (`foto_antes_B63_b2bis.txt`): HEAD
`1d1ff7f4`, 60.292 entradas.

**Dos controles más, antes de escribir el testigo v2** (`control_config_sha_y_renglones_B63b2bis.txt`; imprime solo booleanos, sha256 y
números de renglón):
- en las 8 sesiones de la captura, el `config_sha256` del renglón de `inicio` del `log_r1` es el sha256 del archivo de la config de
  servidor del brazo (`a4acb5cf…` la híbrida, `09b2233d…` el denso y `9e9f0ee5…` el grafo);
- la ventana, por su sha256, está en los renglones 76 y 312 del pre-registro de HEAD, y una vez en la `.nota` de cada una de las dos
  configs de fragmentos.

## 2. El testigo v2

`aislamiento/testigo_aislamiento_b63_v2.py` es el testigo de la b2 (`27c87f52…`) con la excepción cerrada de la decisión 1, como una
lista de un solo elemento, fija en el código (`EXCEPCIONES`):
- **la ventana**, por su sha256 tal como la normaliza el testigo, es decir, sus 8 palabras de `trechos` unidas por un espacio, en UTF-8:
  `7018aeed5e917704ed87da793d5fade0c1bc28f00490c96b1e18733db0a5ea31`. El texto no está en el código;
- **el archivo**, el `log_r1` de la sesión; **el renglón**, el de `evento` `inicio`; **el campo**, `config.nota`;
- **la config de servidor de la sesión**, una de las dos de fragmentos, por su ruta y su sha256:
  `mcp_vector/config_fragmentos_hibrida_evaluado_r2b.json` (`a4acb5cff735…`) y `mcp_vector/config_fragmentos_denso_evaluado_r2b.json`
  (`09b2233d9016…`). Además, el renglón de `inicio` tiene que traer ese mismo `config_sha256`.

**Cómo decide.** `buscar_log_r1` hace la búsqueda del `log_r1` de la b2, tal cual (`buscar_en_archivos`), y además la hace con la
excepción.
- Para cada aparición de una ventana de un testigo sigue de qué cadena salen sus 8 palabras (renglón y ruta del campo).
- Una aparición pasa solo si es esa ventana, sus 8 palabras salen todas de `config.nota` del renglón de `inicio` y la config de servidor
  cumple las dos condiciones.
- Una ventana cuenta si tiene alguna aparición que no pasa. Los tokens de los plantados se cuentan como en la b2: la excepción no los
  toca.
- Antes de decidir, controla que las palabras con su origen den los mismos trechos que el testigo de la b2. Si no dan, frena.

Todo lo demás del testigo es el de la b2, también los renglones de la fecha.

**El resultado** (`cerrar_resultado`). Es el cierre de `fase_testigo` de la b2, movido a una función para que lo use también la
reaplicación:
- `FRENO` y `PASS`, tal cual los de la b2;
- `FRENO_con_la_excepcion`;
- `PASS_de_B63`: sin los renglones de la fecha (como `leer_testigo`) y con la excepción;
- `PASS_del_testigo_tal_cual`: el PASS de la b2;
- `excepcion_aplicada`: cuántos renglones de FRENO pasan, y en qué sesión, renglón del `log_r1`, campo y testigo.

**El diff contra el de la b2** (`diff_testigo_aislamiento_b63_v2_contra_b2_B63b2bis.diff`): +137 −24, en 10 bloques.
1. el docstring nuevo, antes del de la b2 tal cual;
2. `EXCEPCIONES`;
3. `cadenas_con_ruta`, `ventana_sha256`, `config_de_servidor`, `pasa_por_la_excepcion` y `buscar_log_r1`, y el parámetro `config` de
   `controlar_sesion`;
4. y 5. en `controlar_sesion`: el `log_r1` por `buscar_log_r1`, con sus campos nuevos y `testigos_que_llegan_con_la_excepcion`;
6. y 7. `fase_testigo`: la config de servidor de cada sesión y de cada negativo;
8. y 9. el cierre, movido a `cerrar_resultado`, con los campos nuevos;
10. el `main`, que imprime también `PASS_de_B63`.

En el cierre, el FRENO de la b2 queda partido en sus renglones sin la fecha y los de la fecha, en el mismo orden. La única diferencia de
la expresión es que `cap.claves_distintas` pasa a ser `res["claves_distintas_de_la_invalida"]`, el mismo valor. La reaplicación
comprueba que el FRENO y el PASS tal cual dan los de la b2 (§4).

## 3. Las pruebas

`aislamiento/selftest_testigo_aislamiento_b63_v2.py`. Cada prueba trabaja sobre una copia nueva de la captura de la b2, nunca sobre
la captura misma. La ventana se planta tomándola de la nota de la config de la híbrida por su sha256, y su texto no está en el archivo.
La otra ventana son las 8 primeras palabras del `CLAUDE.md` del repo en HEAD, un testigo.

| # | prueba | resultado |
|---|---|---|
| 1 | la excepción: un elemento; la ventana, una vez en la nota de cada config de fragmentos y 0 en la config del grafo; las dos configs dan su sha256 | PASS |
| 2 | la captura sin cambios: reproduce la b2; pasan los 4 renglones (T2, T3, T5 y T6; renglón 0, `inicio`, `config.nota`); `PASS_de_B63` true y `PASS_del_testigo_tal_cual` false; 12 de la fecha; `leer_testigo` coincide | PASS |
| 3a | la misma ventana en un pedido, en `system` | frena (T2) |
| 3b | la misma ventana en un pedido, en `messages` | frena (T2) |
| 4 | otra ventana en el `log_r1`, en el mismo renglón y el mismo campo | frena (T2) |
| 5a | la misma ventana en otro campo del renglón de `inicio` | frena (T2) |
| 5b | la misma ventana en otro renglón del `log_r1` (el de `fin`) | frena (T2) |
| 6a | la misma ventana en otro archivo: el stream | frena (T2) |
| 6b | la misma ventana en otro archivo: la carpeta de configuración | frena (T2) |
| 7 | la misma ventana en el `log_r1` de una sesión del grafo | frena (T1) |
| 8 | la misma ventana en su lugar, con otro `config_sha256` en el renglón de `inicio` | frena (T2) |
| 9 | la captura no cambió: el sha256 de sus 111 archivos, antes y después | PASS |

«Frena» quiere decir que `PASS_de_B63` da false y que esa sesión tiene su renglón «llega un testigo» en el FRENO con la excepción. En
cada prueba que frena, esa sesión es la única que lo tiene.

**Dos veces, en una copia** (`copia_y_selftest_b2bis.zsh`; copia c1, de 11:03:29 a 11:03:44; `copia_selftest_c1_B63b2bis.txt`):
- la copia: 2.842 archivos, sin `.env`, `NO_ABRIR_`, `*_SOLO_MESA*`, enlaces ni `.git`, igual al repo por sha256. Es la misma copia de
  la b2: `banco_mcp` sin `a2_2/adjudicacion`, `ev2_juez` y los `.py` del primer nivel de `evaluacion`;
- **el selftest v2**: 12 de 12 en PASS, dos veces, iguales byte a byte;
- **el selftest del testigo de la b2**: 3 de 3, dos veces, iguales, y byte a byte igual a su salida de la b2
  (`selftest_testigo_corrida1_B63b2.txt`);
- la captura (111 archivos) y lo copiado del repo, antes y después: iguales. `.pyc` en la copia: 0.

Fue el único intento: no hubo fallas.

## 4. La reaplicación

`b63/v2/b2bis/reaplicar_testigo_b63.py`, desde la raíz de la copia c1, sobre la captura de la b2 (solo lectura), dos veces, iguales
(`reaplicacion_B63b2bis.json`).

**Lo que reconstruye de la captura, sin ninguna sesión:**
- los pedidos, de la captura privada, con su ruta y su clave por presencia de `testigo_resultado.json`;
- los testigos, por `git show HEAD` y la cuenta;
- los tokens de los plantados, de la línea de comandos de cada negativo. El sha256 de cada renglón da el del plantado de la b2; los
  tokens no se imprimen;
- por sesión, `controlar_sesion` del testigo v2 sobre su stream, su `log_r1`, su carpeta de configuración y sus pedidos, con su
  marcador (`sesion_<id>.json`).

**Lo que toma de la b2, tal cual**, porque pediría la sesión o el servidor de captura y no toca la excepción: el rc de cada CLI, la
comparación con el init, el cwd vacío, los negativos, las tandas y sus otras conexiones, y los controles de después de la corrida.

**Los trechos permitidos van vacíos**, porque las descripciones de las herramientas pedirían un servidor. En la b2, ninguna sesión
excluyó ningún trecho (`trechos_excluidos_por_su_configuracion`, 0), así que los efectivos son los mismos. Lo comprueba el control.

**El control: reproduce la b2.** Dan lo de la b2:
- el plan;
- los 12 pedidos, con sus bytes y su sha256;
- los testigos, por sha256 y cantidad de trechos;
- los tokens de los plantados;
- cada campo de cada una de las 6 sesiones;
- el FRENO tal cual (16 renglones) y el PASS tal cual (false);
- los sha256 por brazo y pedido, las otras conexiones y `ningun_pedido_al_modelo_sale_de_la_maquina`.

**Los tres campos:**
- **`PASS_de_B63`: true.** El FRENO con la excepción tiene 12 renglones, los 12 de la fecha.
- **`PASS_del_testigo_tal_cual`: false.** La causa son sus 16 renglones: los 12 de la fecha y los 4 «llega un testigo» de T2, T3, T5 y
  T6, que son la ventana de la nota de las configs de fragmentos en el `log_r1`. Ningún otro.
- **`excepcion_aplicada`:** 4 renglones. En cada una de las 4 sesiones, uno: renglón 0 del `log_r1`, `inicio`, `config.nota`, testigo
  `repo:docs/preregistro_B6_3_evaluacion_final.md`, 1 ventana. No se aplicó en ninguna otra sesión.

**El control cruzado con `leer_testigo` de la b2** (sin cambiar):
- sobre el resultado tal cual da `PASS_de_B63` false, con los 4 renglones en `otros_FRENO`;
- sobre el FRENO con la excepción da `PASS_de_B63` true, el mismo del testigo v2.

## 5. El repo

- **Lo nuevo:**
  - en `aislamiento/`: `testigo_aislamiento_b63_v2.py` (`971626ee…`) y `selftest_testigo_aislamiento_b63_v2.py` (`5da99efc…`);
  - en `b63/v2/b2bis/`: `reaplicar_testigo_b63.py` (`610b0728…`) y su lista `sha256_etapa_b2bis_b63.txt`, que tiene los 3 renglones
    (`shasum -c` OK; `d4ac6324…`);
  - este FRENO.

  Los tres archivos son los mismos que corrieron en la copia c1: dan el sha256 de su lista de antes.
- **Las fotos** (`foto_despues_B63_b2bis.txt`). La foto antes es de las 10:55:08 y la foto después, de 11:04:35 a 11:04:54. Las dos
  tienen HEAD en `1d1ff7f4` y entre los dos HEAD no hay ningún commit.
  - 60.292 entradas comparadas, 0 cambian, 0 solo en la antes;
  - 2 solo en la después, los dos nuevos de `aislamiento/`;
  - las 13 podadas, iguales;
  - `.pyc` fuera de los venvs: 237 y 237.
- **Al cierre** (`repo_al_cierre_B63b2bis.txt`): status vacío, con las vedadas podadas; lo sin rastrear de `b63/` y de `aislamiento/`.

## 6. Errores propios, con su causa

1. **La primera versión de `buscar_log_r1` tenía una expresión confusa y un nombre que no existe (`_es_json`).** La vi al revisar el
   archivo, antes de correrlo, y la reescribí. La causa: armé el recorrido de los renglones de una vez, sin separar los renglones JSON de
   los de texto.
2. **Un script mío de edición no corrió por un error de sintaxis** en un `assert` con comillas escapadas dentro del heredoc. No aplicó
   ningún cambio. Lo repetí sin ese `assert`.
3. **Escribí un archivo intermedio en el repo**, `aislamiento/testigo_aislamiento_b63_v2.py.parcial`, y lo borré en el paso siguiente.
   - La causa: mi script de edición escribió su resultado parcial al lado del archivo, en lugar de en el scratchpad.
   - No corrió nunca, y no está en ninguna de las dos fotos: se creó y se borró entre las 10:55 y las 11:04.
   - El borrado fue un `rm` de ese único archivo, nuevo y mío.
4. **El primer control del `config_sha256` cortó con un `StopIteration`.** En `testigo/` hay una carpeta que no es de ninguna sesión, la
   del cliente que lee las descripciones. Lo rehíce salteándola, y la salida de esa corrida es la del paquete.
5. **Un `find` sin poda por nombre.** La función `captura()` de `copia_y_selftest_b2bis.zsh` toma el sha256 de cada archivo de la
   captura con un `find` que no poda `*_SOLO_MESA*` ni `NO_ABRIR_*`. En la captura no hay ninguno, ni ningún `.env`: lo controlé después
   por nombre, con un `find` que los poda, y dio 0 (`captura_por_nombre_B63b2bis.txt`). La causa: la escribí para una carpeta que sabía
   limpia, y no le puse la poda que el despacho pide en toda búsqueda. Los `find` que cuentan esos nombres en la copia son los del
   script de la b2, sin cambios, sobre una copia que el `rsync` arma sin ellos.

## 7. Declaraciones

- **La P de B6.3 es 1**, por la decisión 2 de la autora, y va en la entrada sellada que arma la mesa: esta etapa no la toca.
- **El pre-registro.** El testigo v2 y la reaplicación lo leen en el proceso, como el testigo de la b2, para sus trechos; no lo
  imprimen. Mis controles lo leyeron igual, e imprimieron solo números de renglón y sha256. No abrí ninguna pregunta, criterio ni cita.
- **Los negativos** también traen la ventana en su `log_r1` (el de la híbrida). El testigo de la b2 no busca testigos que lleguen en
  los negativos, y el v2 tampoco.
- **Las búsquedas:** los `git status` podaron las vedadas por ruta y las marcas por nombre. Los `find` y los `rsync` de la copia
  podaron `*_SOLO_MESA*` y `NO_ABRIR_*` por nombre, salvo el del error 5. No usé ningún `grep -r`.
- **Ningún `sed` ni `grep` sobre un archivo de conexión o de entorno.** No imprimí ninguna clave ni contraseña.
- **Lo que lancé:**
  - `paso0_b2bis.zsh` y `control_captura_b2bis.py`, el control del `config_sha256` y de los renglones, y `foto_repo_b1v2.py` con
    `comparar_fotos_b1.py`;
  - `copia_y_selftest_b2bis.zsh`, una vez (con `rsync`, `find`, `shasum` y `du`). En la copia corrió los dos selftests y la
    reaplicación, dos veces cada uno. Ninguno lanza un CLI ni un servidor;
  - el `grep_convenciones.py` de HEAD; `armar_manifest.py` y los scripts de enmascarado;
  - `git` (`status`, `log`, `rev-parse`, `show`), `ditto`, `diff`, `cmp` y `date`.
- **La carpeta temporal del sistema:** no escribí nada fuera del scratchpad.

## 8. El grep de convenciones y el paquete

**El grep de convenciones.** Corrí `segmentacion_oficial_e0r2/s0_4/scripts/grep_convenciones.py` de HEAD, con `LC_ALL=en_US.UTF-8`,
sobre copias de los 4 archivos del repo de antes de este FRENO y de los 3 scripts del scratchpad que había entonces
(`grep_convenciones_b2bis_y_scripts_B63b2bis.txt`):
- control positivo: 16 de 16 términos;
- archivos revisados: 7;
- en los 4 del repo, 0;
- 2 en `control_captura_b2bis.py`, en un mismo renglón: el patrón de la expresión regular que reemplaza la carpeta temporal por
  «<carpeta temporal>», el mismo de los scripts de enmascarado de la b2. Es el patrón que busca esa ruta para sacarla, no una ruta
  escrita en un artefacto.

Al cerrar lo corro otra vez, sobre este FRENO y el paquete. El resultado va en el reporte del cierre.

**El paquete:** `revision_B63_FRENO_b2_bis/`, en el scratchpad de esta sesión, con nombres únicos y su `manifest.txt`. Trae:
- lo que escribí en el repo, como `aislamiento__*` y `b2bis__*`, y este FRENO;
- los scripts, como `script__*`;
- el paso 0, los controles, el diff, las fotos enmascaradas, las salidas de los selftests y de las dos reaplicaciones, y el grep.

Lo copio con `ditto` a `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/d7b988e9-4130-42c4-b289-914468756f63/scratchpad/` y verifico
en la copia los sha256 de su manifiesto.
