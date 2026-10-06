# U-SEG-OFICIAL — S0-2: implementación de las reglas de S0 en e0-r2

Etapa S0-2 del mandato FIRMADO en `e543cb2` (las 239 líneas firmadas dan `44cf30ca0d82…`), leído con sus notas al
pie, en particular las del 05/10/2026 sobre los FRENOS S0-1 (`d59921f`) y S0-1 bis (`0b92a06`); y las decisiones del
despacho de S0-2, que no se vuelven a decidir. USD 0: ninguna llamada a la API. Escribí solo
`data/experiment/reextraccion_v2/e0_chunking/e0_lib.py`, `correr_e0.py` y `selftest_e0.py`, y esta carpeta
(`s0_2/`) con el freno. Ningún commit. Los censos y comparaciones están en `censos/`; los scripts nuevos, en
`scripts/`; los de S0-1 y S0-1 bis que reuso, en `../s0_1/scripts/` y `../s0_1bis/scripts/` (§8).

## 0. Método

- Precondiciones a–e del despacho, con su salida, en `censos/precondiciones_S0-2.txt`: el commit del FRENO T5 de
  U-REEXT-T0 es `0a3ac81`, ninguna extracción corre, `reextraccion_v2/` y `reext_t0/` están limpios, el código de E0
  es el de `9f6361e` y el parche completo de S0-1 bis da `81c3409851ba82a3…` y `f737028b1918cce0…`.
- Copia de trabajo: el árbol de HEAD copiado, sin `.git`, `.venv`, el volumen de Neo4j ni `__pycache__`. Traía 339
  enlaces simbólicos absolutos al repo (trazas de `ev2_corrida/navegabilidad/` y `.venv-app/`); los borré de la copia
  antes de usarla (borrar un enlace no toca su destino; lista en el paquete). Con las bases de caché, que el selftest
  de claves necesita para el anclaje (U-REEXT-T0 ya cerró).
- Dos códigos en copias: `impl`, el que va al repo, sin interruptores; y el prototipo con interruptores por regla
  (el de S0-1 bis con las decisiones de este despacho), que sirve solo para atribuir. Con todas las reglas, los dos
  dan los 768 archivos de los 152 TOs iguales byte a byte. El prototipo está en `prototipo/` como diff sobre el código
  de S0-2 (`patch -p1` en una copia; da `e0_lib.py` `0df55f1e76e1229c…` y `correr_e0.py` `076f662e03f7a442…`).
- Base de comparación: la E0 de `9f6361e` de los 152 TOs (la de S0-1) y `salida_tanda0_r2b/`.

## 1. El código

En e0-r2 las reglas son constantes; la versión legada no conoce ninguna (sus parámetros están apagados por default,
selftest j). No pasan al repo los interruptores del prototipo (`S0_REGLAS`, `S0_PARTIR_TABLAS`, `S0_RAZON_E1`) ni la
regla 5 general (`cola_estricta_si_prosa`), que la decisión 1 descarta.

- `e0_lib.py`: regla 1 (sección escrita de otra forma, `RE_SECCION_VARIANTE_R2`, `_match_seccion_r2`), regla 2
  (veto de rótulos que no lo son), regla 3 (continuación de índice con títulos, `continuacion_con_titulo`, y la
  ampliación `paginas_indice_r8`), regla 4 (`marcador_letra`), regla 7 (`reabrir_padre`), regla 8
  (`lineas_de_listas_r8` y su veto) y regla 9, parte 9a (`rotulos_fila`), con el campo `lineas_previas` del nodo.
- `correr_e0.py`: regla 5 (`COLA_TITULO_ESTRICTA_R5`), regla 6 (partición por renglones en la partición por tamaño de
  E0 y en `particionar_por_corte`, con `CAPACIDAD_ESCALON_3_R6` y `OBJETIVO_PARTES_RENGLONES_R6`), el acompañamiento T
  (`fundir_tabla_en_intersticiales`), regla 9 (`filas_de_catalogo_r9`, parte 9b `anclar_filas_de_catalogo_r9`) y la
  escalera con las reglas 3 y 8 en cada etapa.
- Orden: la regla 3 ampliada arma los roles de cada etapa; la marca de la regla 8 va antes del parseo de esa etapa;
  en el parseo, la regla 1 lee la sección antes que la cola de título (regla 5), la parte 9a levanta el rechazo por
  resto en minúscula, después vetan la 2 y la 8, y después reabre la 7; tras el parseo y sus correcciones, las tablas
  (detectadas antes del parseo, una sola vez) se asignan a los renglones, la parte 9b ancla las filas, T funde y se
  serializan las tablas; la regla 6 parte al final, sobre los chunks.
- sha256 del código: `e0_lib.py` `c5e7106a1b2d4cc6…`, `correr_e0.py` `4570a0c88d3e9fe9…`, `selftest_e0.py`
  `af114a4d793e20d6…` (completos en `censos/condiciones_S0-2.txt`).

## 2. Las decisiones del despacho

1. **Regla 5.** La lista de 9 páginas; la regla general no está en el código.
2. **T.** Adoptado.
3. **Regla 6 en E0.** La partición por renglones entra en la partición por tamaño (más de 26.182); el umbral no baja y
   las unidades con tabla serializada se declaran sin partir (9 en los 152).
4. **Regla 6 en E1.** La partición por corte de las 2.439 unidades de la tanda 0 no cambia (§3). Razón 1,5051
   (`data/experiment/reext_t0/freno_t2.md:12`; `docs/mandatos/UREEXT_T0_reextraccion_tanda0.md:485-487`); capacidad del
   tercer escalón 27.214. Clases (las definiciones de S0-1: el reintento, con 1,175 y 1,498) sobre las 78 unidades
   de la E0 final que pasan 10.937 caracteres
   (`censos/clases_S0-2_razon_1.5051.json`): A 14, B 7, C 49 y D 8; 21 llegan al tercer escalón (la mayor parte, 25.468,
   `ri_transpa::S14`), 5 se parten por renglones en E1 (`cateloc::S2`, `ri2_cs::S3`, `ri_cc::S3`, `ri_niif::S4` y
   `ri_niif::S7`) y ninguna queda sin salida. Solo por la razón (el mismo código con 1,175, sobre la misma E0) cambian
   dos: `ri2_cs::S3` pasa de B a D (su parte de 28.915 se parte en 9.905, 10.512 y 8.496) y `ri_cc::S3` cambia de
   partición (su parte de 27.274 se parte en 10.700, 10.503 y 6.069) pero sigue en B, porque le queda una parte de
   19.164 que llega al tercer escalón. Precisión al despacho: `ri_cc::S3` cambia de partición, no de clase.
5. **Objetivo de las partes por renglones: 10.886**, en E0 y en E1; el de la partición por ítems sigue en 13.091.
   Respecto de S0-1 bis, mueve a D `cateloc::S2` y `ri_niif::S7` (en E1 sus partes por renglones pasan a ser de
   10.886 o menos) y cambia las partes de E0 de cinco unidades: `manori::S2` y `snp_mep::S7` pasan de 4 a 5 partes, y
   `manual::S2::cierre`, `ri_ccna::S8::cierre` y `ri_dsf::S10` cambian el tamaño de sus partes (§4).
6. **ri_cc y ri_tsa.** E0 no cambia; no hay modo de sub-documento.
7. **Regla 8.** Veto, como en el prototipo; el comentario del bloque dice ahora lo que el código acepta entre rótulos
   (renglones más a la derecha que el rótulo anterior, de menos de 70 caracteres, que no empiezan en minúscula, y a lo
   sumo uno en minúscula por rótulo). Con los roles de S0-1 bis detecta las mismas 12 listas con 150 rótulos; con la
   ampliación de la regla 3, 8 de esas páginas son índice y la regla queda con 3 listas (manori pp. 3 y 57, nmaeef
   p. 36) y 10 renglones vetados, todos de manori (`censos/censo_regla8_*`).
8. **Páginas de índice leídas como cuerpo.** La regla tal como está escrita alcanza 4 de las 6 páginas (ceninf p. 2,
   cirmo3 pp. 3 y 4, ri_niif p. 1): en adfsp p. 3 el último ítem viene pegado a su título («6.10.Declaración…») y la
   regla 8 no lo toma como rótulo, y en nmaeef p. 2 hay, además de la lista, el título del anexo antes del primer
   rótulo y una palabra partida («Uni-» / «versitarios.») en la columna del rótulo. Para que las 6 reciban el rol, la
   lista admite esas tres formas (rótulo pegado, renglón en minúscula después de una palabra partida y a lo sumo un
   renglón sin número ni punto final antes del primer rótulo); solo pueden actuar en las 12 páginas con lista de la
   regla 8. Censo (`censos/censo_rol_indice.json`, 162 TOs): pasan a índice 8 páginas, las 6 de la decisión y, por la
   tercera forma, nmaeef p. 14 y ri2_ae p. 13 (los índices de anexo del censo); 178 renglones pasan de cuerpo a rol
   declarado, 152 en las 6 páginas (adfsp 12, ceninf 13, cirmo3 77, nmaeef p. 2 27 y ri_niif 23) y 13 en cada una de
   las otras dos. Desaparecen `adfsp::S6`, `cirmo3::S7`, `nmaeef::S0` y `ri_niif::S1`; aparece `ri_niif::S0`
   (preámbulo, pp. 2 a 4, 8.371 caracteres); `ceninf::S1::chapeau_seccion` queda con el chapeau de la p. 3 (109); la
   cobertura es exacta. Siguen en cuerpo las páginas con una lista parcial (manori pp. 3 y 57, nmaeef p. 36); ningún
   otro rol ni modo de lectura cambia; ceninf p. 1 sigue siendo cuerpo, no portada. Límite declarado: la línea
   «Sección 1. Formalidades…» de ri_niif está en mitad de la p. 2 (top 277) y E0 solo lee encabezados de sección en la
   zona de título, así que el cuerpo de la Sección 1 queda en `ri_niif::S0`.
9. **Regla 9.** Las dos partes, como en S0-1 bis: 119 filas ancladas, 223 renglones, 28 números aceptados por 9a. El
   orden por celda no se adopta. En las 119 filas el número, la gravedad y las multas están en un mismo renglón del
   PDF, y en 63 de ellas ese renglón lleva además un tramo de la descripción. Para ordenar por celda hay que partir ese
   renglón en todas las filas: el texto de la unidad deja de estar hecho con los renglones del PDF y el control
   automático (`control_filas_catalogo.py`, que compara renglones), que es criterio de aceptación, no puede dar limpia
   ninguna fila. La condición de no tocar nada fuera de rdbcra se cumpliría; el criterio del control, no.

## 3. Criterios de aceptación (comandos y salidas en `censos/condiciones_S0-2.txt`)

- Tanda 0: 57 de 57 archivos iguales byte a byte a `salida_tanda0_r2b/`.
- `particionar_por_corte` sobre las 2.439 unidades de `salida_tanda0_r2b/`: `435af2fe…`, igual a `9f6361e`; la única
  unidad con partición, `cap::4.2.1.2`, da 15.056 y 11.669 con los dos códigos.
- 152 TOs: cambian 26; los otros 126 salen iguales byte a byte a la base, en sus archivos por TO y en sus entradas de
  los agregados (`censos/condicion_tos_no_tocados_S0-2.json`). Cobertura exacta en los 152. Unidades: 9.554.
- Sobre el umbral de la partición por tamaño: 10 partidas y 9 declaradas por tabla serializada; ninguna salteada.
- Atribución y conciliación con S0-1 y S0-1 bis: §4.
- Las 119 filas del catálogo de rdbcra, limpias en el control automático (`censos/control_filas_catalogo_S0-2.json`).
- Rol de índice: §2, decisión 8.
- Tabla de reprocesamiento y selftest de claves: §5.
- Selftests de E0 sobre la copia: `selftest_e0` 84/84 (57 de antes y 27 casos nuevos, bloques j a m: uno o más por
  regla y la doble corrida de e0-r2), `b52` 39/39, `b581` 34/34, `b582` 59/59 y `b583` 33/33; los cuatro últimos con
  la misma salida que en HEAD. Doble corrida de los 152 y de la tanda 0: §3 bis.

### 3 bis. Doble corrida

Dos corridas completas con el código: la tanda 0 da 57 de 57 archivos iguales entre sí y a `salida_tanda0_r2b/`, y
los 152 TOs, 0 de 768 archivos distintos. La segunda corrida usó el código final (con el docstring de las reglas 8 y
9 en `parsear_cuerpo`); la primera, el anterior a ese cambio de docstring. Además, `selftest_e0` corre una doble
corrida de e0-r2 sobre garopt y ri_spi (bloque m).

## 4. Atribución de los ids que cambian y conciliación con S0-1 y S0-1 bis

**Atribución** (`censos/atribucion_S0-2.json`, `censos/ids_que_cambian_S0-2.json`; el método de S0-1: cada evento de
la corrida con todas las reglas se atribuye a las reglas cuya corrida sola produce el mismo evento, y a T si no está
en la corrida sin T). En los 26 TOs que cambian hay 1.430 eventos: 553 ids nuevos, 384 que desaparecen, 491 chunks
con otro texto y 2 cambios de orden. Por regla: 7, 317; T, 256; 1, 181; 9, 143; 8, 142; 3 ampliada y 8 (cada una
sola produce el evento), 115; 4, 95; 6, 58; 2, 33; 3, 31; 2 y 7, 21; 5, 19; 7 y 8, 9; 3 ampliada, 8. TOs por regla:
1, dmrd, garopt, inspag, opecam y snp_dd; 2, rdbcra, ri_dsf, ri_niif y ri_tsa; 3, fimipyme, snp_mep y venliq; 3
ampliada, adfsp, ceninf, cirmo3, nmaeef, ri2_ae y ri_niif; 4, ri_spi; 5, cirmo3, cryl, ri2_ci y snp_cheq; 6, manori,
manual, nmaeef, ri_ccna y snp_mep; 7, manori, rdbcra, ri_dcpc, ri_mmsef y snp_cheq; 8, adfsp, ceninf, cirmo3,
manori, nmaeef y ri_niif; 9, rdbcra; T, ri_dcpc y snp_cheq.
**«Otra», leída:** 2 eventos, `ri_dsf::S10::parte3` y `parte4`, una interacción de las reglas 2 y 6. La 2 deja
`ri_dsf::S10` como sección sin puntos de 27.767 caracteres; sin la 6, la partición por ítems de siempre la corta en 2
partes, y con la 6, el ítem de más de 13.091 se parte por renglones y salen 4. S0-1 la tenía igual.

**Conciliación** (`censos/conciliacion_S0-1_S0-1bis_S0-2.json`). Primero, las corridas de referencia reproducen los
dos censos commiteados: en los 25 TOs de `s0_1/censos/ids_que_cambian_S0-1.json` y
`s0_1bis/censos/ids_que_cambian_S0-1bis.json`, los ids de la base, menos los que desaparecen y más los nuevos de los
dos censos, son los de la corrida final de S0-1 bis. Después, S0-2 difiere de S0-1 bis en 11 TOs, con 41 eventos, todos
con su causa y ninguno «otra»:
- decisión 8 (rol de índice), 21 eventos en 6 TOs: adfsp 1, ceninf 9, cirmo3 1, nmaeef 7, ri2_ae 1 y ri_niif 2;
- decisión 5 (objetivo de las partes por renglones, 10.886), 20 eventos en 5 TOs: manori 5 (`manori::S2` pasa de 4 a
  5 partes), manual 6, ri_ccna 2, ri_dsf 2 y snp_mep 5 (`snp_mep::S7` pasa de 4 a 5 partes).
Las decisiones 4 (solo E1) y 9 (el orden por celda no se adoptó) no cambian E0, y sacar la regla 5 general no cambia
nada (no estaba encendida en S0-1 bis).

## 5. Tabla de reprocesamiento y selftest de claves

Qué cambia cada regla corrida sola, sobre los 26 TOs (`censos/filas_por_regla_S0-2.json`; el texto propio, F01; la
herencia de encabezado, F02, o de prosa, F03; las marcas, F04; páginas o metadatos sin cambio de texto, F05):

| Regla | Ids nuevos / que desaparecen | Unidades comunes | Filas |
|---|---|---|---|
| 1 | 201 / 1 | F01 12, F03 28, F05 18 | F19b, F01, F03, F05 |
| 2 | 8 / 41 | F01 2, F03 4 | F19b, F01, F03 |
| 3 | 15 / 1 | F03 11, F05 4 | F19b, F03, F05 |
| 3, ampliación | 18 / 80 | F01 17, F03 5, F05 4 | F19b, F01, F03, F05 |
| 4 | 94 / 0 | F01 1 | F19b, F01 |
| 5 | 0 / 0 | F01 8, F03 13, F05 2 | F01, F03, F05 |
| 6, E0 | 53 / 5 | F01 4 | F19b, F01 |
| 6, E1 | — | — | F20 (cambia el mecanismo de la partición por corte) |
| 7 | 175 / 96 | F01 13, F03 156 | F19b, F01, F03 |
| 8 | 154 / 91 | F01 22, F02 8, F03 11 | F19b, F01, F02, F03 |
| 9 | 28 / 21 | F01 94 (y las marcas de 7) | F19b, F01, F04 |
| T | 0 / 222 | F01 163, F03 28 (y las marcas de 97 en snp_cheq) | F19b, F01, F03, F04 |

(La regla 8 corrida sola, sin la ampliación de la regla 3, actúa en los 6 TOs de sus listas; con las dos, en
manori. T, medido con todas las reglas contra todas menos T, actúa en 3 TOs: en snp_dd funde tablas de chunks que la
regla 1 ya cambia, y la atribución por eventos de §4 los cuenta en la 1.) **Propuesta de fila nueva, que no escribí:** las unidades que una regla de segmentación de E0 agrega o
retira, sin cambio en el PDF. F19 es para un cambio de numeración del documento, y F01 para el texto de una unidad
que sigue existiendo; ninguna dice qué pasa con una unidad nueva por una release de E0. Propuesta: F19b, «una unidad
agregada o retirada por una regla de segmentación de E0 (release de e0-r2)»; dónde: E0 e0-r2 (texto, id y herencia);
qué se re-corre: E1 y E3 de las nuevas y de las que cambian texto o herencia (F01 a F03); una retirada no llama y
sale del ensamblado en código; clave de E1: cambia (las nuevas, sin clave previa); clave de E3: cambia (las nuevas);
re-procesamiento: E1 y E3 de las afectadas; clase 9; sin variación propia en el selftest de claves, porque en la
tanda 0 no ocurre. En la tanda 0 no se dispara ninguna fila: su E0 no cambia un byte.

**Selftest de claves** (`data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b …`, sobre la copia
con el código nuevo y las bases): veredicto OK, contraste con la tabla OK, anclaje r2b OK (2.449 claves de E1); la
salida es igual byte a byte a `data/experiment/mantenimiento/selftest_clave_cache.json` de `0a3ac81`. Ninguna clave
de la tanda 0 se mueve. El selftest leyó la tabla de `0a3ac81`, la de la copia: durante la unidad, otra unidad dejó
`tabla_reprocesamiento.md` modificada sin commit en el árbol de trabajo; no la toqué ni corrí el selftest contra esa
versión. La variación R26 (partición por corte de `cap::4.2.1.2`) corre con el `particionar_por_corte`
nuevo y da lo mismo.

## 6. Límites

- La línea «Sección 1. Formalidades…» de ri_niif está en mitad de la p. 2 y E0 solo lee encabezados de sección en la
  zona de título: el cuerpo de la Sección 1 queda en `ri_niif::S0`.
- Para la decisión 8 la lista admite tres formas que la regla escrita no nombra (§2); con ellas cambian también
  nmaeef p. 14 y ri2_ae p. 13.
- Las tablas del catálogo de rdbcra siguen sin serializar (cada fila es una unidad), y el texto de cada fila sigue el
  orden del PDF.
- ri_cc (pp. 2 a 47) y ri_tsa (pp. 3 a 61) siguen fuera de toda unidad, para la vía de página de la tanda 3.
- La razón 1,5051 es el p90 de 39 unidades de la tanda 0; con las partes incluidas, T2-bis la da en 1,4820
  (`data/experiment/reext_t0/freno_t2bis.md:27`). La decisión se tomó con 1,5051.

## 7. Para S1

- S1 corre con este código, sin interruptores.
- Por la corrección del 05/10/2026 al censo de renglones de S1 (punto 8), toda página de índice que no sea la primera
  de su documento va a la lista: 7 de las 8 páginas que pasaron a índice (ri_niif p. 1 es la primera de su
  documento).

## 8. Comandos

Sobre una copia del repo sin enlaces, con `PYTHONDONTWRITEBYTECODE=1` y el python de `.venv` con `-B`; `<copia>` es la
copia con el código nuevo y `<proto>`, la del prototipo con interruptores (`S0_REGLAS`).
```
../s0_1/scripts/correr_tanda0.py --codigo <copia> --salida <dir>
../s0_1/scripts/correr_152.py --codigo <copia> --salida <dir> [--workers 7] [--tos a,b]
../s0_1/scripts/comparar_e0.py <base> <nueva> <salida.json> [--tos a,b]
../s0_1/scripts/atribuir.py --base <base> --todas <proto, todas> --regla rX=<proto, solo rX> … --resta T=<proto, sin T> --out <json>
../s0_1/scripts/ids_que_cambian.py <comparación> <atribución> <salida>
../s0_1bis/scripts/condicion_tos_no_tocados.py <base> <nueva> <tos declarados> <salida>
../s0_1bis/scripts/particion_corte_unidades.py <copia> <salida_tanda0_r2b> <salida>
../s0_1bis/scripts/censo_clases_tercer_escalon.py --e0 <dir> --codigo <copia> --razon-e3 1.5051 --out <json>
../s0_1bis/scripts/comparar_clases.py <censo 1> <censo 2> <salida>
../s0_1bis/scripts/control_filas_catalogo.py <pdf de rdbcra> <caché de líneas de rdbcra> <dir> <salida>
../s0_1bis/scripts/censo_regla8.py <copia o proto> <caché de líneas> <salida>
scripts/censo_rol_indice.py <proto> <salida> [--workers 7]
scripts/conciliar_ids.py <base> <S0-1.json> <S0-1bis.json> <final S0-1 bis> <proto sin r3i> <S0-2> <salida>
scripts/filas_por_regla.py <runs> <base> <tos> <salida> rX=<solo rX> … T=<todas>:<sin T>
data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b <copia>/data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b --out <json>
data/experiment/reextraccion_v2/e0_chunking/selftest_{e0,b52,b581,b582,b583}.py   (desde e0_chunking/ de la copia)
```
