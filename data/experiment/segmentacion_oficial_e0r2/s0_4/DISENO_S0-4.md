# U-SEG-OFICIAL — S0-4a: sub-documento, oración tomada como título, título envuelto y apartados de ri_ai (diseño, prototipo y medición)

Etapa S0-4a del mandato FIRMADO en `e543cb2` (las 239 líneas firmadas dan `44cf30ca0d82…`), leído con sus notas al pie,
en particular las del 07/10/2026 (revisión del FRENO S0-3 y decisiones de la autora: S0-4 antes de S1-bis), y con el
despacho de S0-4, que fija el alcance y los controles duros. USD 0: ninguna llamada a la API. No edité el repo: el
código de S0-4 es un parche sobre `26c6502` (`parche/`), y este registro (diseño, censos, scripts y freno) está armado
en el scratchpad con la estructura que tendría en `data/experiment/segmentacion_oficial_e0r2/s0_4/`; lo copio al repo
con el «seguí» (§10). Ningún commit.

## 0. Método

- Precondiciones, con su salida, en `censos/precondiciones_S0-4.txt`: HEAD `f96ab49` al empezar; el código de E0 del
  repo es el de `26c6502` (`git diff --stat 26c6502 HEAD` de `e0_chunking/`, vacío; sha256 `c5e7106a…`, `4570a0c8…`,
  `af114a4d…`); el texto firmado da `44cf30ca…`; S0-3 está commiteada en `2185807`; su parche, aplicado con
  `patch -p1` sobre los archivos de `git show 26c6502:…`, da los sha del LEEME (`3ce0a2d8…`, `0002ed4e…`, `cd4b98db…`).
- Copia de trabajo: el árbol del repo copiado al scratchpad sin `.git`, `.venv`, `.venv-app`, `data/raw/`, el volumen de
  Neo4j ni `s1/e0/`; los 336 enlaces simbólicos absolutos que trae, borrados de la copia (0 enlaces). Con las bases de
  caché, que el selftest de claves necesita. Para las corridas de E0, raíces mínimas copiadas de esa copia (código de
  E0, `e0_tablas.py`, los PDF de `escalado_prep/pdfs/` y `subset/`, `conteos_b584.json` y el manifiesto de la tanda 0),
  cada una con 0 enlaces (`scripts/raiz_minima.sh`).
- Bases reproducidas sobre la copia: la E0 de S1 (código de `26c6502`, `../s0_1/scripts/correr_152.py`): 768 de 768
  archivos iguales a `s1/e0/` y a los sha256 de los 768 archivos `e0/` de `s1/manifest_salida.json` (`ee7c07c`); la
  tanda 0 (`../s0_1/scripts/correr_tanda0.py`): 57 de 57 iguales a `salida_tanda0_r2b/`; S0-3 sin el mecanismo 4 (el
  código de S0-3 con `REGLAS_S0_3` sin «m4»): 768 de 768 iguales a la corrida `v_sin_m4` de la sesión de S0-3, 9.409
  unidades, y su tanda 0, 57 de 57.
- Dos códigos: `impl4`, el del parche, sin interruptores, y `proto4`, el mismo con una variable de entorno que elige las
  reglas (`S0_4_REGLAS`; `parche/parche_interruptores_prototipo_S0-4_sin_aplicar.diff`, que no va al repo).
- Corrida de la tanda 0 en paralelo por TO (`scripts/correr_tanda0_par.py`), validada antes de usarla: con el código de
  `26c6502` da 57 de 57 archivos iguales a `salida_tanda0_r2b/`.
- El TO `manual` pide unos 5 GB por proceso; dos lecturas suyas a la vez hacen paginar la máquina (16 GB). Las corridas
  de configuración (todo apagado, solo S0-3, la segunda final y el prototipo) corrieron sin `manual` en paralelo y
  `manual` aparte, de a una, y se juntaron con `scripts/juntar_por_to.py`, que rehace los archivos por TO y los
  agregados con el criterio de `correr_152.py` (validado: sobre la corrida final, 768 de 768 iguales).
- Las reglas acotadas por lista en el código (sub-documento y sdg3 en cinco TOs, apartados en ri_ai) corrieron solas
  sobre sus TOs; en los demás no pueden actuar (la condición `to in TOS_…` está antes de la regla) y la referencia es la
  base. 4a y 4b solas corrieron sobre los 52 TOs con algún punto candidato (la condición común de las dos, §1.3, en la
  estructura de la base de S1 o de S0-3; `censos/tos_candidatos_4ab.txt`); en los otros 100 no hay punto donde actúen.
  Cada regla de S0-3 sola corrió sobre los TOs que lista su censo de S0-3 (`s0_3/censos/censo_v_<regla>.json`), y da en
  ellos los mismos archivos que la corrida de esa regla sola de la sesión de S0-3 (§4).
- La sesión se cortó a las 20:37, con tres corridas de configuración, la segunda tanda 0 final y los selftests de E0
  a medias. Al retomar verifiqué con `ps` que no quedara ningún proceso, revisé cada corrida por su salida (el «listo …
  0 con error» de su registro y sus archivos) y rehice enteras las que habían quedado a medias (`censos/estado_al_retomar_S0-4a.md`;
  lote `scripts/lote_s04f.sh`).

## 1. Las reglas: qué hacen y dónde están en el código

Anclas de línea sobre el código del parche (`e0_lib.py` y `correr_e0.py` de la copia con el parche). Cada regla es un
parámetro apagado por default en `e0_lib.py` (la versión legada no las conoce: selftest q) y encendido en la escalera
de e0-r2 de `correr_e0.py`, con su nombre en `REGLAS_S0_4` (`correr_e0.py:127`) y, si corresponde, su lista de TOs
(`:128-130`). Constantes y comentario de las formas: `e0_lib.py:396-440`.

### 1.0 El mecanismo 4 de S0-3, fuera

`titulo_es_texto_m4`, el parámetro `titulo_texto_m4` de `construir_chunks` y `TOS_TANDA0_SIN_M4` no están (el parche de
S0-4 sobre el de S0-3 los quita): `REGLAS_S0_3` queda con nueve reglas (`correr_e0.py:117`). Lo reemplazan 4a y 4b
(§1.3), que reusan la parte del mecanismo 4 que ponía el rótulo al frente de la intro (`_seg_intro`, `e0_lib.py:2823`).

### 1.1 Sub-documento («sd»)

`limites_subdocumento` (`e0_lib.py:632`) recorre las páginas de cuerpo y devuelve, en orden, los límites de
sub-documento; `parsear_cuerpo(subdocumentos=…)` abre en cada uno una raíz nueva (`abrir_subdocumento`, `:1527`). Corre
solo en los cinco TOs de la lista (`TOS_SUBDOCUMENTO_S0_4`: ri_sef, nmcief, ri_ccna, ri_icpipsp y ri_cc); ri_tsa y
ri2_pm quedan fuera por lista y siguen `parcial_declarado`.

Formas del rótulo:
- **anexo**: un renglón entero «ANEXO <n>», «Anexo <n>», «-ANEXO-», o «Anexo <n> – Título», entre los primeros 6
  renglones de una página de cuerpo (`RE_ANEXO_SD`). <n> en romanos o arábigos; el anexo tiene que suceder al anterior
  (o ser el I o el primero sin número). El encabezado corrido de cada página repite el número y no es un límite. Un
  anexo I después de otro anexo abre un documento nuevo: ri_ccna junta dos normas (auditorías externas, pp. 1 a 41, y
  controles internos, pp. 42 a 60), cada una con sus anexos I a IV (prefijos D1 y D2). Guarda por caso leído: una
  serie de letras («ANEXO A» a «ANEXO L», los modelos de publicación del R.I. – P. de ri_cc, pp. 93 a 105) no es de
  sub-documentos; «ANEXO I» después de «ANEXO H» es la letra I.
- **parte**: un renglón «I. Título», «I.- TÍTULO», «I - TÍTULO», «II- TÍTULO» o «I TÍTULO» (sin separador, solo en
  mayúsculas) (`RE_PARTE_SD`), dentro de una serie de al menos 2 partes consecutivas desde la I en el mismo anexo
  (`MIN_PARTES_SD`). Guarda por caso leído: un «I.» suelto no forma serie (los rubros «I. Bienes Diversos» e «I.
  Utilidades diversas» de los modelos de balance de ri_cc, pp. 84 y 87).
- **régimen**: un renglón «<n> - TÍTULO EN MAYÚSCULAS» o con la sigla «(R.I. – <sigla>)» entre los primeros 6 renglones
  (`RE_REGIMEN_SD`, `RE_SIGLA_REGIMEN_SD`): los regímenes 4 y 5 y el R.I. – P. de ri_cc. El despacho habla del «título
  de un régimen tras una página de índice»; la página de índice no es condición, porque la que precede al R.I. – P.
  (p. 76) no tiene la marca «-Índice-».
- **formulario** (forma que agregué; §8): una página de cuerpo con el membrete «BANCO CENTRAL DE LA REPÚBLICA ARGENTINA»
  entre sus primeros 3 renglones y sin rótulo de anexo (`RE_MEMBRETE_SD`); la página con «Cont. <n>» sigue el
  formulario anterior (`RE_CONT_SD`). Son las fórmulas de la primera norma de ri_ccna (pp. 31 a 41: antecedentes,
  declaraciones juradas, solicitud de inscripción). Sin esta forma, sus ítems «5.» a «8.» abrían las raíces 5 a 8 del
  Anexo IV (sucesoras exactas de su raíz 4; lo vi en una corrida de prueba del prototipo sobre los TOs de los casos,
  antes de agregar la forma, que no conservé).
- **circular** (forma que agregué; §8): un renglón «Circular <SIGLA> <n>. Título» (`RE_CIRCULAR_SD`), en una serie de al
  menos 2 en el mismo anexo: los bloques SINAP, CONAU y RUNOR de la tabla del Anexo I de ri_icpipsp, cuyas filas vuelven
  a numerarse desde 1. Es el caso de la fila 85 de S1, que sin esta forma seguía con el error.

Prefijo: la concatenación de R<n> (o RI<sigla>), D<k> (solo si el régimen junta más de un documento), A<n> (A, si el
anexo no tiene número) o F<k>, y P<n> o C<k>. Ejemplos de la corrida final: `ri_sef::P1::11.2`, `nmcief::A2::3.2.1`,
`nmcief::A1P2::S4`, `ri_ccna::D2A1P2::3.1`, `ri_ccna::D1F2::S1`, `ri_icpipsp::A1C2::S1`, `ri_cc::R5::2.1`,
`ri_cc::RIP::S0`.

Lectura: en cada límite se cierra la pila y se abre una raíz sintética «0» con el prefijo; su título es el renglón del
rótulo y, si el rótulo es un renglón de contenido (las partes, los anexos de ri_sef y de ri_icpipsp, los membretes que
no se repiten), es su renglón de label. Un rótulo que quedó en la zona de encabezado (los anexos corridos de nmcief y
ri_ccna, los regímenes de ri_cc) abre el sub-documento al empezar la página (`:1562`; el de un renglón de contenido,
en ese renglón, `:1640`). La numeración de raíces vuelve a empezar (`ultima_raiz_num` y `col_raiz` en cero) y las raíces
y secciones que se abren después llevan el prefijo. La raíz «0» que no lleva texto se retira al final, como el
preámbulo (`:2041`); el registro de sub-documentos queda en `ResultadoParseo.subdocumentos` y en la estructura
(`subdocumentos`). En `construir_chunks`, el id de cada unidad lleva el prefijo (`<to>::<prefijo>::<unidad>`, `_unidad`,
`:2837`) y su herencia empieza con un tramo `encabezado` por cada rótulo de la cadena de sub-documentos
(`_tramos_subdoc`, `:2842`; `unidad_origen` = el prefijo); la raíz «0» de un sub-documento hereda solo los que la
contienen. La regla no cambia el modo de lectura de un TO: la escalera elige la etapa sin ella y vuelve a leer esa
etapa con los sub-documentos (`correr_e0.py:1370`, `:1377`, `:1393`).

Decisión de diseño que declaro (§8): un rótulo abre su sub-documento aunque no lo siga una numeración que reinicie. La
parte II de ri_sef (A, B y C, sin números), la parte III del Anexo I de nmcief, los anexos de tabla o de formulario y el
R.I. – P. de ri_cc no tienen numeración propia; si no abrieran raíz, su texto seguiría pegado a la última unidad del
sub-documento anterior, que es el error que la regla corrige.

### 1.2 Guarda de columna dentro de un sub-documento («sdg3»)

Dentro de un sub-documento, la guarda de columna (G3) no rechaza una raíz con forma de título que sucede exactamente a
la anterior (`e0_lib.py:1746`); la raíz se declara (`raiz_g3_subdocumento_sd`, `:1772`). Es el caso de la fila 71 de
S1: «4. Periodicidad y documentación de las reuniones» de nmcief está 9,5 pt más adentro que la raíz 3 (las raíces 1 a 4
de la parte II del Anexo I están a 94,5, 86,0, 76,5 y 86,0 pt: páginas de Comunicaciones con márgenes distintos). Con
la regla de sub-documento sola, la sección 4 queda dentro de `nmcief::A1P2::S3`. No corre fuera de un sub-documento.

### 1.3 Oración tomada como título («4a») y título envuelto («4b»)

`clase_titulo_4ab` (`e0_lib.py:2753`) clasifica cada punto con hijos que cumple la condición común (la del mecanismo 4:
el título no termina en punto y la intro empieza en minúscula):
- **4b** si el primer renglón de la intro completa el título: termina en punto (o es toda la intro y no termina en
  dos puntos) y no lleva un verbo de `RE_VERBO_ORACION_4AB`. El renglón se junta al título, en un renglón aparte del
  encabezado, tal cual está en el PDF (`_titulo_linea`, `:2871`), y sale de la intro, que se emite solo si le queda
  texto (`:2906`, `:3054`).
- **4a** si no es 4b y la primera oración (el título con los renglones del primer segmento de la intro hasta el primero
  que termina en punto o en dos puntos) termina en dos puntos o lleva un verbo de esa lista. La intro empieza en el
  rótulo y el encabezado heredado es solo el número (`:2869`), como hacía el mecanismo 4.
- Si no es ninguna, el punto queda como en S0-3 (§7).

`RE_VERBO_ORACION_4AB` (`:439`): deberá(n), debe(n), podrá(n), puede(n), corresponde(n), corresponderá(n), será(n),
tendrá(n) y el futuro impersonal «se <verbo>rá(n)». Es la lista del despacho («deberá, deberán, podrá, no podrá,
corresponde, se informará…») más los presentes deónticos y «será», «tendrá» (caso leído: `ctavis::4.1.2`, «La letra de
cambio extendida a favor de una persona determinada, que no posea la» / «cláusula “no a la orden”, será transmisible
por endoso.»). La guarda de 4b («no juntar si el renglón siguiente es una oración completa con sujeto y verbo») es esa
misma lista sobre el renglón.

Las dos reglas no corren en los diez TOs de la tanda 0 (`TOS_TANDA0_SIN_4AB`, `correr_e0.py:130`; los parámetros se
arman en `procesar_tablas_r2`, `:1289`).

Validación del clasificador contra la lectura de la mesa de la revisión de S0-3 (los 15 puntos de la tanda 0 sorteados
con `S0-3:mecanismo4:muestra_mesa` y leídos): los 12 títulos partidos salen 4b y las 3 oraciones (`ext::3.17.3`,
`cap::6.9.2`, `ext::5.5.1`) salen 4a. Y los 30 títulos partidos de un renglón de los 152 (`s0_3/censos/m4_formas_de_la_intro.json`)
salen 4b, los 30.

### 1.4 Apartados de una sección sin puntos («ap»)

En una sección de la lectura vigente que no tiene puntos, un rótulo de un nivel «N. Título» con N = 1, 2, 3…
consecutivos abre el punto «<sección>.N», con el número impreso N y la marca `correccion_numeracion`
(«apartado_de_seccion: el PDF imprime 1. dentro de la Sección 4; E0 lo abre como el punto 4.1»), en lugar de
rechazarse por `fuera_de_seccion` (`e0_lib.py:1836`; `_flags_numeracion`, `:2738`). Solo en ri_ai (`TOS_APARTADOS_S0_4`):
«1. Posición», «2. Franquicias» y «3. Incumplimientos» de la Sección 4 (p. 7) pasan a `ri_ai::4.1` a `4.3`, y
`ri_ai::S4` desaparece.

## 2. Censo por regla en los 152 TOs

Cada regla sola contra la base de S1 (`censos/censo_v_<regla>.json`, `scripts/censo_s04.py`; corridas del prototipo con
`S0_4_REGLAS=<regla>`), salvo sdg3, que no actúa sin sub-documento y se mide como la corrida final contra la final sin
ella. «Cambian»: unidades comunes con otro texto, herencia, páginas o marcas, por fila de la tabla de reprocesamiento
(`censos/filas_por_regla_S0-4.json`, el script de S0-2). La tanda 0 da 57 de 57 archivos iguales con cada regla sola
(§4).

| regla | TOs | renglones | rótulos +/− | ids +/− | unidades | cambian (F01 / F02 / F03) |
|---|---|---|---|---|---|---|
| sd | ri_sef, nmcief, ri_ccna, ri_icpipsp, ri_cc | 41 rótulos de sub-documento | 188 / 2 | 308 / 139 | 142 → 311 | 2 (2 / – / –) |
| sdg3 (sobre sd) | nmcief | 1 a rótulo | 1 / 0 | 1 / 0 | 288 → 289 | 1 (1 / – / –) |
| 4a | 41 TOs | 96 rótulos a la intro | 0 / 0 | 0 / 0 | = | 490 (96 / 394 / 370) |
| 4b | 24 TOs | 40 renglones de la intro al título | 0 / 0 | 0 / 30 | 9.554 → 9.524 | 170 (10 / 160 / 145) |
| ap | ri_ai | 3 a rótulo | 3 / 0 | 3 / 1 | 11 → 13 | 0 |

Detalle:
- **sd**: de los 308 ids nuevos y 139 que desaparecen, 116 son la misma unidad con otro id (mismo texto propio, con el
  rótulo del sub-documento en la herencia: filas F05 y F02), 192 son unidades nuevas y 23 retiradas (F19b)
  (`censos/renombres_sd_contra_S1.json`, `scripts/renombres_sd.py`). Por TO: ri_sef 27 → 36 unidades, nmcief 40 → 65,
  ri_ccna 31 → 149, ri_icpipsp 9 → 25, ri_cc 35 → 36. Los 41 límites (`censos/censo_subdocumento_152.json`, clave
  `limites_por_forma_en_la_lista`): 20 anexos, 9 partes, 3 regímenes, 6 formularios y 3 circulares.
- **4a y 4b**: el clasificador del censo (`scripts/censo_4ab.py`, la misma condición sobre la estructura) y lo que hicieron
  las corridas coinciden punto por punto: 96 en 4a y 40 en 4b contra la base de S1; 97 y 40 contra la de S0-3
  (`censos/censo_4ab_sobre_S1.json` y `censos/censo_4ab_sobre_S0-3.json`, clave `control_contra_las_corridas`). Sobre la
  base de S0-3, de los 151 candidatos (las 150 intros del mecanismo 4 de S0-3 más `ri2_ae::2.1`, que aparece cuando el
  mecanismo 3 de S0-3 abre la sección 2 de ri2_ae), 97 son 4a, 40 son 4b y 14 ninguna; por la forma de la intro del
  censo de S0-3: de un renglón sin dos puntos, 30 de 30 en 4b; terminan en dos puntos, 94 en 4a, 8 en 4b (el primer renglón completa el título y la intro sigue) y 3 ninguna; de varios
  renglones, 3 en 4a, 2 en 4b y 11 ninguna. En 4b, 30 intros eran solo el renglón que completa el título y se retiran
  (F19b); las otras 10 pierden ese renglón (F01).
- **ap**: `ri_ai::4.1` a `4.3` nuevos, `ri_ai::S4` retirado.

## 3. Censo de renglones que cambian de rol (configuración final)

Contra S0-3 sin el mecanismo 4 (`censos/censo_final_contra_S0-3.json`): ninguna página cambia de rol y ningún renglón
pasa entre encabezado y texto (S0-4 no toca la zona de encabezado ni los roles de página). Cambian:
- de prosa a rótulo, 195 rótulos nuevos y 2 que desaparecen (los preámbulos de nmcief y ri_ccna, que pasan a ser raíces
  «0» de su primer sub-documento): las raíces «0» de 38 sub-documentos (de los 41, 3 se retiran por vacías: R4 y R5 de
  ri_cc y D2A1 de ri_ccna), las raíces y puntos que la numeración reiniciada ya no rechaza (nmcief 29 rótulos nuevos,
  ri_ccna 135, ri_icpipsp 18, ri_sef 9, ri_cc 1), la raíz 4 de la parte II del Anexo I de nmcief (sdg3) y los tres
  apartados de ri_ai;
- del título a la intro, el renglón del rótulo de los 97 puntos de 4a (en la estructura sigue como label; cambia en las
  unidades);
- de la intro al título, el primer renglón de la intro de los 40 puntos de 4b (ídem).
Contra S1 se suman los de S0-3 (8 renglones de encabezado a texto, 2 de texto a encabezado y la p. 3 de ri2_ae a índice;
`censos/censo_final_contra_S1.json`).

## 4. Controles duros

- **Tanda 0**, los diez TOs con `scripts/correr_tanda0_par.py`: con la configuración final (código sin interruptores),
  57 de 57 archivos iguales byte a byte a `salida_tanda0_r2b/`, en las dos corridas; con todos los interruptores
  apagados, 57 de 57; y con cada regla sola (sd, sd con sdg3, 4a, 4b, ap y las nueve de S0-3), 57 de 57 en cada una
  (`censos/tanda0_por_regla_S0-4.txt`).
- **Los 25 archivos de la tanda 0 dentro de los 152** (ctacte, lingob, polcre, pagjub y docvig: chunks, estructura,
  índice, tablas y pies), en la corrida final: 25 de 25 iguales a `salida_tanda0_r2b/`; sus entradas de los siete
  agregados, 20 iguales y 15 ausentes en los dos lados (`scripts/control_tanda0_en_152.py`).
- **Selftest de claves** (`data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b
  data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b`, desde la raíz de la copia, con las bases de caché y el
  código de S0-4): VEREDICTO OK, contraste con la tabla OK, anclaje r2b OK (2.449 claves de E1); la salida
  (`923dd900…`) es igual byte a byte a `data/experiment/mantenimiento/selftest_clave_cache.json` del repo. Ninguna
  clave de la tanda 0 se mueve (`censos/selftest_claves_S0-4.txt`).
- **Todo apagado**: el prototipo con `S0_4_REGLAS=""` (las nueve reglas de S0-3 y las cinco de S0-4 apagadas) da los
  768 archivos de los 152 iguales byte a byte a los de S1 (`s1/e0/` y los sha256 de `s1/manifest_salida.json`): lo que
  no está detrás de un interruptor es inerte (`censos/controles_configuracion_S0-4.txt`).
- **Solo S0-3**: el prototipo con las nueve reglas de S0-3 da los 768 archivos iguales a la corrida de S0-3 sin el
  mecanismo 4. Y cada regla de S0-3 sola, con el código de S0-4, da en sus TOs los mismos archivos que la corrida de esa
  regla sola de la sesión de S0-3 (95 de 95 archivos por TO, con manual).
- **Prototipo y código**: el prototipo con todas las reglas da, en los 64 TOs que cambian contra S1, los mismos 320
  archivos por TO que el código sin interruptores.

## 5. Corrida de los 152, doble, y conciliación

- **Doble corrida** de los 152 con el código del parche: 768 y 768 archivos, **0 distintos**; la tanda 0, dos veces, 57
  y 57, iguales entre sí y a `salida_tanda0_r2b/` (`censos/controles_configuracion_S0-4.txt`,
  `censos/tanda0_por_regla_S0-4.txt`).
- **Unidades**: S1 9.554 → S0-3 sin el mecanismo 4 9.409 → S0-4 **9.554** (que el total vuelva a 9.554 es una
  coincidencia: contra S1 hay 357 ids nuevos y 357 que desaparecen). Cobertura exacta en los 152.
- **Contra S0-3 sin el mecanismo 4** (`censos/atribucion_S0-4_contra_S0-3.json`, el método de S0-1,
  `../s0_1/scripts/atribuir.py`): cambian 54 TOs, con 1.095 eventos (666 unidades que cambian, 142 ids que desaparecen y
  287 nuevos); unidades 9.409 → 9.554 (+287 −142): sd +172 (+283 −111), sdg3 +1, 4b −30, ap +2 (+3 −1), 4a 0. Por regla,
  cada evento lo produce una regla sola: sd 396, 4a 494, 4b 198, ap 4, sdg3 1, y 2 que producen 4a y 4b cada una sola
  (`prevmi::5.1.2.1` y `5.1.2.2`, cuya herencia lleva el encabezado de 5.1, que cambia por 4a, y el de 5.1.2, que cambia
  por 4b). «Interacción», 0. Dos efectos de una regla sola no llegan a la combinada: 4a cambiaría
  `prevmi::5.1.2::intro`, que 4b retira, y `ri_ccna::2.1::intro` y `2.1.9`, que sd renombra.
- **Contra S1** (`censos/atribucion_S0-4_contra_S1.json`, con las nueve reglas de S0-3 solas y las cinco de S0-4):
  cambian 64 TOs en sus unidades (65 con ri_mmsef, que cambia solo un aviso de la estructura, como en S0-3), con 1.530
  eventos (815 unidades que cambian, 357 ids que desaparecen, 357 nuevos y 1 cambio de orden, el de snp_cheq 7.1 por
  1b); unidades 9.554 → 9.554 (+357 −357). Por regla: 1a 69, 1b 165, 2a 62, 2b 14, 2c 73, 3 29, 5a 1, 5b 2, 5c 3, sd
  394, sdg3 1, 4a 485, 4b 198, ap 4; los que producen dos reglas, cada una sola: 1a y sd 26 (intersticiales y cierres de
  nmcief que 1a devuelve a sus puntos y sd renombra), 4a y 4b 2 (`prevmi::5.1.2.1` y `5.1.2.2`), 2a y sd 1 (en ri_icpipsp).
  **Interacción, 1**, leída: `nmcief::A4::S1` («1.Documentación de la Auditoría.», p. 25) se abre solo con sd y la forma
  2a de S0-3 juntas: sd hace que la numeración del Anexo IV empiece en 1 y 2a lee el número pegado al título; con 2a sola
  el 1 no sucede a la raíz anterior, y con sd sola el renglón no es un rótulo. Es la raíz 1 del Anexo IV. Efectos de una
  regla sola que no llegan a la combinada: en ri_cc, los 9 cambios de 5a quedan en unidades que sd renombra; en nmcief,
  6 de 1a y 26 de sd; 1 de 4a en prevmi y 2 en ri_ccna; 2 de sd en ri_icpipsp.

## 6. Proyección sobre los 17 errores de S1

De los 17 errores de corte del primer grupo de la lectura de S1 (`s1/lectura_cortes/marcas_lectura_cortes_S1_mesa_136_filas.tsv`),
la configuración final cambia 16 en la dirección de la corrección y deja 1 sin cambio
(`censos/errores_S1_frente_a_S0-4.json`, `scripts/errores_s1_vs_s04.py`; no es una lectura: dice qué unidad cambia,
cómo empieza y termina y dónde quedan su primer y su último renglón).

| fila | unidad de S1 | después de S0-4 | regla |
|---|---|---|---|
| 29 | `snp_cheq::7.1::intersticial::107` | desaparece; su texto está en `snp_cheq::7.1.6` | 1b |
| 42 | `ri_dcpc::3.1.1` | 46 → 817 caracteres: lleva sus dos párrafos | 1a |
| 43, 45, 49 | `ri_dcpc::3.1::intersticial::4`, `3.2::intersticial::4`, `3.2::intersticial::1` | desaparecen; su texto está en `3.1.3.3` y `3.2.1` | 1a |
| 47 | `seguef::2.1.6::intro` | empieza en «2.1.6. Cuando se decida…» (73 → 165) | 4a |
| 54 | `ri_tar::1.1` | 5.621 → 985: solo «Aclaraciones» | 2c |
| 58 | `ri_sef::S0` | 2.765 → 2.613: termina con las instrucciones generales; «I. Información solicitada» y su párrafo abren `ri_sef::P1::S0` | sd |
| 63, 74 | `nmcief::3.2::intersticial::11` y `::20` | desaparecen; su texto está en `nmcief::A2::3.2.1` y `A2::3.2.3` | 1a (ids con prefijo, sd) |
| 69 | `seggar::S3::cierre` | 624 → 112: se abre la sección 4 | 2a |
| 71 | `nmcief::S3::chapeau_seccion` | desaparece: «3. Propuesta…» es `nmcief::A1P2::S3` (1.580), «4. Periodicidad…» es `A1P2::S4`, la parte III es `A1P3::S0`, la IV `A1P4`, el Anexo II `A2` con su numeración | sd, sdg3 |
| 76, 86 | `ri2_ae::S1`, `ri2_ae::S4` | la p. 3 pasa a índice; S1 es la sección 1 del cuerpo (14 → 4.647); S4 desaparece | 3 |
| 82 | `ri_ccna::S8::cierre::parte7` | desaparece; su texto está en `ri_ccna::D2A2::3.3` a `D2A2::S5` y empieza `D2A3::S0` | sd |
| 85 | `ri_icpipsp::S8` | desaparece: la fila 8 es `ri_icpipsp::A1C1::S8` (2.336, sin el bloque CONAU), CONAU es `A1C2`, RUNOR `A1C3` y el Anexo II `A2::S0` | sd (circular) |
| 59 | `nmaeef::2.9` | sin cambio: el cierre de la sección 2 sigue al último ítem en el mismo margen | límite declarado |

**Proyección, NO es una lectura** (la lectura de S1-bis es la que cuenta): si la muestra de S1 se leyera con el código
de S0-4 y los 16 cambios resultaran correctos, quedaría 1 error en 90; con 1, la cota inferior de Wilson es 0,9397
(piso 0,90, que admite 3: 0,9065). Con una tasa de error de 1 en 90 en la población del primer grupo, la probabilidad de
que una muestra nueva de 90 tenga 3 errores o menos es 0,9817 (binomial). Las dos dudosas del primer grupo
(`inspag::2.25.2`, `lingeef::5.4.5.1`) no cambian.

## 7. Lo que S0-4 no cubre

- **nmaeef 2.9** (fila 59): límite declarado por decisión de la autora (el inverso del mecanismo 1). La misma forma
  aparece en `ri_sef::P1::S14`: los párrafos que cierran la parte I siguen al ítem 14 en el mismo margen (1.185
  caracteres).
- **Dentro de los sub-documentos**, cuatro casos que la regla separa del resto pero no segmenta por dentro:
  - `ri_cc::RIP::S0`: el R.I. – P. de ri_cc (pp. 76 a 118, 57.922 caracteres) queda en una unidad, declarada sin partir
    por tabla serializada (`sub_chunking.json`). Es en su mayor parte modelos de estados contables; su numeración
    («1.», «1.1», luego otra vez «1.», «2.», «3.» y las notas «1-», «5-», «10-») no es una espina que la lectura vigente
    lea. Antes estaba pegado a la sección 3 del régimen 5 (`ri_cc::S3`, 59.118).
  - ri_cc, régimen 4, Sección 3 (Capitales mínimos, con su propio índice en la p. 57): numeración «1.» a «6.» que
    reinicia dentro de la sección; «1.» y «2.» quedan en el chapeau (`ri_cc::R4::S3::chapeau_seccion`, 5.182) y «3.1» a
    «3.3» se abren por coincidencia con el número de la sección. Es la familia de los apartados de un nivel dentro de una
    sección (§7 de S0-3), que solo corre en ri_ai.
  - ri_ccna, Anexo III de la primera norma: dos listas numeradas bajo las sub-partes con letra «A. GENERAL» y «B.
    PRUEBAS SUSTANTIVAS», y 40 ítems en la segunda. Los ítems 1 y 2 de la lista B quedan dentro de `D1A3::S2` (que es
    el 2 de la lista A), los 3 a 30 abren `D1A3::S3` a `S30`, y los 31 a 40 se rechazan por `MAX_RAIZ` (30) y quedan en
    `D1A3::S30` (2.285).
  - `nmcief::A6::S0` (el Anexo VI, pp. 28 a 36, 23.071 caracteres): un anexo sin numeración, una unidad bajo el umbral
    de la partición por tamaño.
- **4a y 4b, 14 puntos sin regla** en los 152 (fuera de la tanda 0; `censos/censo_4ab_sobre_S0-3.json`, clase
  `ninguna`): títulos envueltos en dos renglones o más (`efemin::1.3.2`, `1.3.7`, `ri_dcpc::4.2`…) y oraciones con un
  verbo fuera de la lista (`lingeef::1.4.4`, «es esencial»; `ri_ii_31_12_19::4.3`, «comprenden»). Quedan como en S0-3.
- **La tanda 0** no lleva 4a ni 4b. El despacho la declara con «22 títulos partidos y 3 oraciones tomadas como título»;
  con el clasificador sobre `salida_tanda0_r2b/` son 123 puntos (los 123 del mecanismo 4): 61 de 4b (los 22 de un
  renglón, 37 cuya intro termina en dos puntos y 2 de varios renglones), 53 de 4a y 9 sin regla, en 9 de los 10 TOs
  (`censos/censo_4ab_sobre_S0-3.json`, clave `tanda0_limite_declarado`). Las 3 oraciones eran las de la muestra de 15.
- **Limpieza** (no es de corte): el rótulo corrido de un anexo que no está en mayúsculas («Anexo I» en la p. 15 de nmcief,
  «Anexo II» en las pp. 16 a 21) sigue como texto pegado a la unidad abierta (`nmcief::A1P3::S0` termina en «Anexo I»;
  `A2::2.4` y `A2::3.2.1`, en «Anexo II»), y la cabecera de columnas de la tabla de ri_icpipsp se repite al principio de
  cada página (`A1C1::S3`, `A1C2::S1`). Estaban en S1.
- **ri_tsa y ri2_pm**, fuera por lista (siguen `parcial_declarado`).
- **El censo de la regla en los otros 147 TOs** (`censos/censo_subdocumento_152.json`; la regla no corre en ellos): el
  detector encuentra límites en 35 TOs más (18 anexos, 42 partes, 26 regímenes, 1 formulario). Hay candidatos con la
  forma de los cinco (anexos con numeración propia en nmaeef, ri2_ae, ri_iepsp, ri_iesinap, ri_oc y ri_spi; partes en
  ri_niif, ri_ii_31_12_19, ri_pnp, ri_tii, ri_acsf y ri_psp) y falsos positivos que una ampliación tendría que guardar
  (filas de tabla en cateloc, «I BUENOS AIRES…»; «2 - CUIL» en snp_tr; un membrete dentro de un párrafo en seggar; el
  número del régimen informativo en el encabezado de un solo régimen, que solo cambiaría los ids). De las 26 raíces
  rechazadas por G3 en 9 TOs (`s0_3/censos/g3_raices_sucesoras_rechazadas.json`), dos son de TOs de la lista: la de
  nmcief es la de sdg3, y la de ri_ccna («9. Arqueo sorpresivo…», p. 17) se abre como `ri_ccna::D1A3::S9` porque en el
  Anexo III la columna de las raíces vuelve a empezar. De las otras, nmaeef (3) y ri2_ae (4) tienen anexos que la regla
  separaría; en manual, ri2_cs, ri_laft, ri_saofe y seggar el detector no encuentra anexo ni parte. No agregué ningún TO
  a la lista.

## 8. Decisiones de la autora (PENDIENTES)

1. **Las formas formulario y circular** de la regla de sub-documento, que agregué a las tres del despacho (anexo, parte,
   régimen) por dos casos leídos de los TOs de la lista: los formularios de ri_ccna (sin ellos, sus ítems abrían las
   raíces 5 a 8 del Anexo IV) y los bloques de circular de ri_icpipsp (sin ellos, la fila 85 de S1 seguía con el error).
2. **sdg3**: la guarda de columna no rechaza, dentro de un sub-documento, la raíz que sucede exactamente a la anterior.
   Actúa una vez en los cinco TOs (nmcief, «4. Periodicidad…»); sin ella, la fila 71 de S1 queda con la sección 4 dentro
   de `A1P2::S3`.
3. **Rótulo sin numeración que reinicia**: abre su sub-documento igual (§1.1).
4. **La lista de verbos de 4a y 4b** (§1.3): la del despacho más debe(n), puede(n), será(n), tendrá(n).
5. **Los casos de §7** dentro de los sub-documentos (R.I. – P. y Sección 3 del régimen 4 de ri_cc, Anexo III de ri_ccna,
   Anexo VI de nmcief) quedan como límite declarado o van a otra regla.
6. **El registro de S0-4a** está en el scratchpad (§10): con el «seguí», S0-4b lo copia a
   `data/experiment/segmentacion_oficial_e0r2/s0_4/` junto con el código.

## 9. Selftests

Sobre la copia con el código del parche, desde `e0_chunking/`, con `PYTHONDONTWRITEBYTECODE=1` y `-B`
(`censos/selftests_e0_S0-4.txt`):
- `selftest_e0.py`: **134/134**. Los 110 de S0-3 menos el caso sintético del mecanismo 4 (109) y 25 nuevos: q) 3, la
  versión legada y las listas de TOs (sub-documento sin ri_tsa ni ri2_pm; 4a y 4b fuera de la tanda 0; «m4» fuera de
  las reglas); r) 13 casos sintéticos (detección de las cinco formas y sus guardas, lectura con sub-documentos y su
  herencia, sdg3, 4a, 4b con su guarda del verbo, apartados); s) 9 casos medidos sobre siete TOs (los cinco de
  sub-documento con las filas 58, 71, 82 y 85 de S1 y los tres regímenes de ri_cc, sdg3, ri_ai y efemin 1.3.1 para 4b) y
  la cobertura exacta. La primera corrida dio 132/134: dos casos medidos de etapas anteriores que S0-4 cambia (el de la
  regla 4 contaba 95 unidades de ri_spi, que 4b deja en 93 al retirar las intros de un renglón de B.1 y B.3; el de 1a
  leía `nmcief::3.2.1`, que pasa a `nmcief::A2::3.2.1`); los corregí, con la razón en el caso, y la segunda dio 134/134
  (`censos/selftests_e0_S0-4_primera_corrida.txt`).
- `selftest_b52.py` 39/39, `selftest_b581.py` 34/34, `selftest_b582.py` 59/59, `selftest_b583.py` 33/33.
- Selftest de claves: §4.

## 10. Tabla de reprocesamiento y escrituras

- Filas por regla (`censos/filas_por_regla_S0-4.json`): sd, unidades renombradas con el mismo texto (F05) y con el
  rótulo del sub-documento en la herencia (F02), unidades nuevas o retiradas (F19b) y 2 con otro texto (F01); sdg3,
  F19b y F01; 4a, F01 (las 96 intros), F02 y F03; 4b, F19b (30 intros retiradas), F01, F02 y F03; ap, F19b. Son filas
  que ya están en la tabla (F01 a F03, F05 y F19b); no hace falta una fila nueva. En la tanda 0 no se dispara ninguna
  (57 de 57 y selftest de claves igual al del repo). No edité la tabla. Hallazgo para S0-4b: las anclas de F19b al código
  de E0 (`correr_e0.py:95-100`, `:327-339`, `:576-585`, `:1266`; `e0_lib.py:352`, `:473`) son las de `26c6502` y se
  corren al aplicar el código de S0-4; el contraste del selftest de claves no las lee.
- Escrituras de S0-4a: nada en el repo (foto sha256 antes y después, §11). El registro (este diseño, `censos/`,
  `scripts/`, `parche/` y `../FRENO_S0-4a.md`) está en el scratchpad, en `s0_4/`, y en el paquete de revisión.

## 11. Comandos

Sobre una copia del repo sin enlaces, con `PYTHONDONTWRITEBYTECODE=1` y el python de `.venv` con `-B`. `<impl>` es una
raíz con el código del parche; `<proto>`, la misma con el parche de interruptores.
```
scripts/raiz_minima.sh <copia> <raíz> <dir con e0_lib.py, correr_e0.py y selftest_e0.py>
../s0_1/scripts/correr_152.py --codigo <impl> --salida <dir> [--workers N] [--tos a,b]
scripts/correr_tanda0_par.py --codigo <impl> --salida <dir> [--workers N]
S0_4_REGLAS=<reglas separadas por coma | "" | TODAS> ../s0_1/scripts/correr_152.py --codigo <proto> --salida <dir> …
scripts/juntar_por_to.py <destino> <corrida sin manual> <corrida de manual>
scripts/censo_s04.py <base> <nueva> <salida.json> [--tos a,b]
scripts/censo_sd_152.py --codigo <impl> --corrida <dir E0> --g3 <json> --salida <json>
scripts/censo_4ab.py --codigo <impl> --base <dir> --r4a <dir> --r4b <dir> --tanda0 <salida_tanda0_r2b> --salida <json>
scripts/renombres_sd.py <ref> <corrida> <tos> <salida.json>
scripts/errores_s1_vs_s04.py <tsv de marcas de S1> <base> <final> <salida.json>
scripts/control_tanda0_en_152.py <dir 152> <salida_tanda0_r2b>
../s0_1/scripts/atribuir.py --base <dir> --todas <final> --regla <r>=<dir>[,<base>] … --resta sdg3=<sin_sdg3>,<final> --out <json>
../s0_2/scripts/filas_por_regla.py <corridas> <ref> <tos> <salida.json> <r>=<dir>[:<ref>] …
data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b --out <json>
data/experiment/reextraccion_v2/e0_chunking/selftest_{e0,b52,b581,b582,b583}.py   (desde e0_chunking/ de la copia)
scripts/grep_convenciones.py <repo> <paquete>   (grep de convenciones; los nombres los toma de git config, no los escribe)
scripts/lote.sh, scripts/lote_s04b.sh, scripts/lote_s04c.sh, scripts/lote_s04e.sh, scripts/lote_s04f.sh
                                       (los lotes que corrí; su registro, en censos/registro_lotes_S0-4.txt)
```

## 12. Errores propios, con su causa

Ninguno llegó a una cifra de este registro: los detecté antes de escribirlas y las corridas o censos afectados se
rehicieron enteros.

1. **KeyError `'D1'` en `_tramos_subdoc`** (primera corrida del prototipo de sub-documento sobre ri_ccna): buscaba el
   rótulo de un documento D<k> entre los sub-documentos, y los documentos no lo son. Corregido: el padre de un anexo o
   formulario es el régimen o el documento; el de una parte o una circular, el anexo si está dentro de uno.
2. **Primera batería de corridas con un código que no era el final**: `e0_lib.py` tenía líneas de más de 120
   caracteres; al reformatearlas cambió su sha256, así que detuve el lote y relancé todo con el código final
   (`censos/registro_lotes_S0-4.txt`, `lote_s04_detenido.log`; corridas descartadas aparte, no se usan).
3. **`scripts/lote.sh` registraba el código de salida de `date`** y no el de la corrida (`rc=$?` después de otro
   comando). Corregido con `local rc=$?` inmediatamente después de la corrida. Cada corrida la juzgo por el «listo …» de su
   propio registro (0 con error en las 152; los diez TOs en la tanda 0) y por sus archivos, no por ese código.
4. **Detuve procesos por un patrón de la ruta del scratchpad** y el patrón alcanzó también al selftest de E0, que estaba
   corriendo; lo volví a correr entero.
5. **Dos lecturas de `manual` a la vez** (unos 5 GB cada una) hicieron paginar la máquina. Detuve los flujos y corrí
   `manual` sola; las corridas se juntan con `scripts/juntar_por_to.py`, validado contra la corrida final (768 de 768).
6. **`scripts/censo_s04.py` contaba como cambio los avisos presentes en las dos corridas**; lo cambié a diferencia de
   multiconjuntos y recalculé todos los censos por regla.
7. **Una línea del registro de `lote_s04b` nombra `lote_s04d`**, que escribí y no corrí; el lote que relanzó off,
   s03cfg y final2 fue `lote_s04e`. Nota de corrección en el propio registro (20:16:46).
8. **Comparé un diccionario contra una cadena** al contrastar con `s1/manifest_salida.json` y salieron «distintos»
   que no lo eran; rehecha la comparación, 768 de 768 iguales.
9. **`selftest_e0` dio 132/134 en su primera corrida**: dos casos medidos de etapas anteriores esperaban la salida de
   antes de S0-4 (ri_spi, 95 unidades; `nmcief::3.2.1`). Los actualicé con su razón (4b retira las intros de B.1 y B.3;
   sd renombra a `nmcief::A2::3.2.1`) y la segunda corrida dio 134/134 (`censos/selftests_e0_S0-4_primera_corrida.txt`).
10. **El corte de la sesión** (20:37) dejó corridas a medias; las rehice enteras (§0, `censos/estado_al_retomar_S0-4a.md`).
11. **Dos frases de un borrador de este diseño**, corregidas antes de entregar: «tres casos» dentro de los
    sub-documentos cuando la lista tiene cuatro (§7), y una referencia a una corrida de prueba como si estuviera en el
    paquete, que no conservé (§1).

## Nota posterior (08/10/2026, S0-4b)

Nota fechada; el texto de arriba es el revisado, sin cambios (sha256 del texto sin esta nota: `579f926dbbf1456a…`). Dos
correcciones que marcó la revisión de la mesa, verificadas contra los archivos:
- **ri_tsa no es `parcial_declarado`** (§1.1 y §7, «siguen `parcial_declarado`»): en `s1/controles_S1.json`,
  `por_to.ri_tsa.clase` es `reconocido_pleno`; solo ri2_pm es `parcial_declarado`.
- **ri_mmsef no cambia «un aviso»** (§5): contra S1 cambian 3 avisos, todos de la p. 3 (sale `padre_reabierto_r2` de
  2.2; entran `cuerpo_al_rotulo_m1` en 2.2 y `aceptado_con_columna_derivada` en 2.2.1) y el `text_col` del nodo 2.2
  (de null a 76,6); sus chunks, índice, pies y tablas son iguales.

Además, para leer este registro en el repo: el FRENO de S0-4a, que §10 cita como `../FRENO_S0-4a.md`, está en
`s0_4/FRENO_S0-4a.md` (S0-4b copia los registros solo dentro de `s0_4/`); y el código que S0-4b aplicó al repo no es
el de este parche sino el de S0-4a-ter (`ter/parche/`), que lo incluye con la regla sdmax (`bis/`) y cinco reglas más
(`ter/`), así que las anclas de este diseño son las del parche de S0-4a.
