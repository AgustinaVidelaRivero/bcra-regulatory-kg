# U-SEG-OFICIAL — S0-4a-ter: ri_oc (régimen de la página 1 y apartados de letra) y ri_ccna (sub-documento de letra, herencia de su rótulo y A.3)

Etapa S0-4a-ter del mandato FIRMADO en `e543cb2` (las 239 líneas firmadas dan `44cf30ca0d82…`), con la nota al pie del
08/10/2026 que revisa el FRENO S0-4a-bis y asienta las decisiones de la autora (líneas 620 a 655 del mandato en
`ae76f08`; hay además una nota del 08/10/2026 por la tarde, sin commit, en el árbol de trabajo desde las 11:15, que leí:
confirma el alcance de esta vuelta y declara los límites de sub-documento de la tanda 1 salvo lo que corrija esta vuelta
en ri_oc), y con el despacho de S0-4a-ter, que fija el alcance: la guarda de ri_oc como regla (decisión a), la
corrección de ri_ccna en vez de su declaración (decisión b), la batería de controles duros con cada regla nueva prendida
y apagada, el parche final con sus anclas y, por un agregado de la autora, la evaluación del Apartado B de ri_oc. USD 0:
ninguna llamada a la API. No edité el repo: el código es un parche sobre `26c6502` (`parche/`), y este registro está
armado en el scratchpad con la estructura que tendría en `data/experiment/segmentacion_oficial_e0r2/s0_4/ter/`; se copia
al repo en S0-4b. Ningún commit.

## 0. Método

- Estado al empezar (08/10/2026, 10:51): HEAD `ae76f08`, sin cambios rastreados en el árbol de trabajo; ningún
  proceso mío vivo (hay un `tail` de otra sesión, del 05/10, sobre otra carpeta de scratchpad, que no toqué);
  `data/experiment/mantenimiento/selftest_clave_cache.json` en `923dd900…`. Entre `7788e52` y `ae76f08`, ningún cambio
  en `reextraccion_v2/`, `mantenimiento/`, `segmentacion_oficial_e0r2/`, `tanda0/` ni `escalado_prep/`; el código de E0
  del repo sigue siendo el de `26c6502`.
- Copia: la de S0-4a-bis, puesta al día con `ae76f08` por el sha1 de git de cada archivo rastreado de
  `data/experiment/` y `docs/mandatos/` (47 que faltaban y 4 distintos, escritos desde `git cat-file`; los tres de
  `e0_chunking/` llevan el código de esta etapa); 0 enlaces.
- Punto de partida: el código de S0-4a-bis (`7e56f857…`, `2559b6c2…`, `a776126d…`). Dos códigos, cada uno en una raíz
  mínima armada desde la copia (`../scripts/raiz_minima.sh`, 0 enlaces): `impl4ter`, el del parche final, y `proto4ter`,
  el mismo con la variable `S0_4_REGLAS` (`parche/parche_interruptores_prototipo_S0-4a-ter_sin_aplicar.diff`; no va al
  repo).
- Corridas: el lote `scripts/lote_ter.sh` (registro en `censos/registro_lote_S0-4a-ter.txt`), con `manual` aparte y
  las corridas juntadas por TO, más las corridas de prueba de los seis TOs de las reglas de sub-documento (`p_*`: cada
  regla nueva sola encima de S0-4a-bis, y todas). Referencias: la corrida final de S0-4a-bis (`bis/corridas/bis_final`)
  y la E0 de S1 (`corridas/base`, igual a `s1/manifest_salida.json`).

## 1. Las cinco reglas

Cada una con su interruptor en `REGLAS_S0_4` (`correr_e0.py:132`, con su comentario en :119-131) y por lista; con los
parámetros apagados, ninguna rama nueva corre.

- **sdr1 — el régimen de la página 1 es el del TO** (decisión a). `limites_subdocumento(…, sin_regimen_pagina_1=True)`
  (`e0_lib.py:637-638`, :686-690): el régimen de la página 1 y los rótulos del mismo régimen en las páginas siguientes
  (el encabezado corrido) no abren sub-documento ni prefijan ids. Lista `TOS_SUBDOCUMENTO_R1_S0_4 = {"ri_oc"}`
  (`correr_e0.py:134`): esos TOs se leen con sub-documento y con la guarda (`correr_e0.py:1340-1341`, :1353-1354).
  Así, ri_oc entra a la lectura con sub-documentos por la regla: con sdr1 apagada, ri_oc es el de S0-4a-bis. La
  guarda va sobre la página 1 literal: ri_cc abre su régimen 4 en la p. 49, su primera página de cuerpo.
- **apl — apartados de letra** (agregado de la autora, Apartado B). En los TOs de `TOS_APARTADO_LETRA_S0_4 = {"ri_oc"}`
  (`correr_e0.py:135`), si la etapa elegida es la sin raíz y hay al menos `MIN_APARTADOS_R4` (2) renglones «APARTADO
  X: …», se vuelve a leer con el marcador de letra de la regla 4 de S0 (`correr_e0.py:1409-1412`), el que ya lee
  ri_spi: «APARTADO X:» abre la raíz X y «X.n.», «X.n.m.» son sus puntos. No cambia la etapa. La regla 4 de ri_spi
  sigue igual (corre solo si la lectura sin raíz deja el TO en una unidad).
- **sdl — sub-documento de letra** (decisión b: el corte de B.1 y B.2). Forma nueva de `limites_subdocumento` con
  `letras=True` (`RE_LETRA_SD`, `e0_lib.py:433-436`; :681-685; prefijo `L<k>`, :769; el límite lleva su letra, :778): un
  renglón «<letra>. <TÍTULO EN MAYÚSCULAS>», en serie desde la A dentro del mismo contenedor y de al menos dos rótulos.
  Con `parsear_cuerpo(letra_corte=True)` (:1409, :1497) se abre como los demás sub-documentos: raíz «0» con el rótulo y
  la numeración de raíces desde cero. Lista `TOS_LETRA_S0_4 = {"ri_ccna"}` (`correr_e0.py:136`, :1342 y :1357-1358).
- **sdlh — herencia del rótulo de letra** (decisión b: las 47). Con sdl, el rótulo de un sub-documento de letra se
  hereda solo con `letra_herencia=True` (`e0_lib.py:1410`, :1581-1584, :2931-2932); sin sdl, cada raíz abierta después
  de un rótulo de letra de su contenedor hereda el último (`ResultadoParseo.rotulos_letra`, :1383, :2135; :2935-2942).
- **sdla — el rótulo «X.n.» con la letra vigente** (la pieza que pedía A.3). En el modo sin raíz, un renglón «X.n.
  Título» cuya letra es la del último rótulo de letra del contenedor, más afuera que la raíz numérica abierta, cierra
  esa raíz y abre la raíz «X.n» (`letra_numero=True`, :1411; la letra vigente, :1503-1505, :1581-1586 y :1692-1694; la
  regla, :1724-1741).

## 2. Efecto de cada regla sola (encima de S0-4a-bis) y de todas

Corridas de prueba de los seis TOs de las reglas de sub-documento (ri_oc, ri_ccna, ri_sef, nmcief, ri_icpipsp,
ri_cc), con el prototipo: cada regla nueva sola encima de las reglas de S0-4a-bis (`ter/corridas/p_<regla>`), contra
esas mismas reglas solas (`p_bis`, igual byte a byte a `bis_final` en los seis: 30 de 30 archivos), y todas
(`p_todas`, igual a la corrida final del lote en los seis). En los cuatro TOs de la lista que no son ri_ccna, ninguna
regla nueva cambia nada.

| regla | TO | unidades | nuevas | desaparecen | cambian |
|---|---|---|---|---|---|
| sdr1 | ri_oc | 128 → 133 | 8 | 3 | 1 (`3.51`) |
| apl | ri_oc | 128 → 179 | 51 | 0 | 2 (`S0`, `3.51`) |
| sdl | ri_ccna | 159 → 163 | 53 | 49 | 1 (`D1A3::S0`) |
| sdlh | ri_ccna | 159 → 159 | 0 | 0 | 49 (solo herencia) |
| sdla | ri_ccna | 159 → 160 | 1 | 0 | 1 (`D1A3::S2`) |
| todas | ri_oc / ri_ccna | 128 → 184 / 159 → 164 | 59 / 54 | 3 / 49 | 2 / 1 |

sdr1 sola da, byte a byte, la medición de S0-4a-bis (`bis/corridas/oc_med`: 5 de 5 archivos de ri_oc).

## 3. ri_oc

ri_oc se lee en el modo sin raíz (`estructura_ri_oc.json`, `modo_lectura`). Su cuerpo tiene tres apartados:
«APARTADO A: OPERACIONES DE CAMBIOS» (p. 3), con las raíces 1 a 3 y sus puntos hasta 3.51; «APARTADO B: POSICIÓN
GENERAL DE CAMBIOS» (p. 16), con B.1 a B.3 y sus ítems B.1.1… (pp. 16 y 17); y «APARTADO C: COMPOSICIÓN DE LA
POSICIÓN GENERAL DE CAMBIOS» (p. 18), con C.1 a C.11. Después vienen los «Criterios de validación» de los tres
apartados y las «Aclaraciones» (pp. 18 a 21), y los Anexos I y II (pp. 22 a 28). Es la forma de la regla 4 de S0
(«APARTADO X:» y «X.n.»), que hoy solo lee ri_spi, porque ahí corre cuando la lectura sin raíz deja el TO en una
unidad; en ri_oc deja 128.

- **sdr1** (decisión a): da lo que midió S0-4a-bis, byte a byte. Los anexos salen de `ri_oc::3.51`: `A1::S0` (338
  caracteres), `A2::S0` (30, solo el rótulo) y `A2::S1` a `S3` nuevas, y `S4` a `S6` → `A2::S4` a `S6` (renombres con el
  mismo texto). Sin apl, `3.51` queda en 12.206 caracteres.
- **apl** (agregado de la autora): la forma está acotada a ri_oc por lista, reusa el código de la regla 4, tiene su
  interruptor, su caso sintético y su caso medido, y no mueve ningún otro TO (§5), así que entra. Separa el Apartado B
  y, por la misma forma, el C:
  - `ri_oc::3.51` queda con su texto: 778 caracteres, p. 15;
  - Apartado B: 37 unidades nuevas, 4.262 caracteres (`B.1.1` a `B.1.28`, `B.2::intro`, `B.2.1` a `B.2.4`, `B.3.1` a
    `B.3.4`), cada una con la herencia de la raíz B y de su B.n;
  - Apartado C: 13 unidades nuevas, 6.697 caracteres (`SC::chapeau_seccion`, `C.1` a `C.11` y `SC::cierre`);
  - `ri_oc::SA`, nueva, de 34 caracteres: solo el rótulo «APARTADO A: OPERACIONES DE CAMBIOS», que sale de `ri_oc::S0`
    (de 5.269 a 5.234 caracteres; pp. 1 y 2).
- **Lo que queda, con su cifra** (§10): los «Criterios de validación» y las «Aclaraciones» no tienen numeración ni forma
  de apartado, así que quedan en el Apartado C: los dos renglones del título («Criterios de validación», «Validación del
  Apartado A – Operaciones de cambios») al final de `ri_oc::C.11`, y el texto, 5.313 caracteres de las pp. 19 a 21, como
  cierre de la raíz C (`ri_oc::SC::cierre`). Los once puntos C.1 a C.11 heredan ese cierre: 39 tramos y 5.484 caracteres
  de herencia cada uno. Heredar el cierre del padre es lo que E0 hace siempre: en S0-4a-bis, 826 unidades de 59 TOs
  heredan tramos de cierre, hasta 6.588 caracteres (`ri_ii_31_12_19::6.5`). Ninguna unidad de ri_oc pasa de 13.944
  caracteres.
- **Juntas**: ri_oc pasa de 128 a 184 unidades. Dentro de la configuración final (§6), sacar sdr1 cambia, además de
  sus 12 eventos, la herencia de C.1 a C.11: sin sdr1, los anexos quedan dentro del cierre de la raíz C.

## 4. ri_ccna

El Anexo III de la primera norma de ri_ccna (pp. 15 a 21) tiene dos listas bajo dos rótulos de letra: «A. GENERAL»
(x0 115; adentro, «A.1. PRUEBAS DE CUMPLIMIENTO…» y «A.2. ANALISIS DE VARIACIONES» en x0 149, los ítems 1 y 2 de A.2 en
x0 203, y «A.3. El relevamiento…» en x0 149, p. 16) y «B. PRUEBAS SUSTANTIVAS» (x0 115, p. 16; los ítems 1 a 40 en x0
150). En ri_ccna son los únicos rótulos «letra. TÍTULO EN MAYÚSCULAS» en serie desde la A: «I. DISPOSICIONES
GENERALES…» (p. 2) se lee primero como candidato a parte (número romano), no como letra, y no forma serie de partes.

- **sdl**: «A. GENERAL» y «B. PRUEBAS SUSTANTIVAS» abren `D1A3L1` y `D1A3L2`. `D1A3::S0` queda en 122 caracteres («ANEXO
  III», «PROCEDIMIENTOS MINIMOS DE AUDITORIA» y «I APLICABLES PARA EL EXAMEN…»); `D1A3L1::S0` (1.220) lleva «A.
  GENERAL», A.1 y A.2 hasta los ítems; los ítems de A.2 son `D1A3L1::S1` y `S2`; B.1 y B.2 son `D1A3L2::S1` (304) y `S2`
  (242), y B.3 a B.40 pasan a `D1A3L2::S3` a `S40` (con 26.1 a 26.6 y 29.1 a 29.3). Sola: 159 → 163 unidades, 103
  eventos (53 nuevos, 49 que desaparecen, 1 que cambia), lo que dio el prototipo de la mesa.
- **sdlh**: las 47 unidades de B.3 a B.40 heredan «B. PRUEBAS SUSTANTIVAS». Sola (sin sdl), además, `D1A3::S1` y `S2`
  heredan «A. GENERAL», por la misma forma: 49 unidades, solo herencia. Con sdl, las 49 unidades de `D1A3L2` (B.1 a
  B.40) heredan su rótulo, y las 3 de `D1A3L1` (los dos ítems de A.2 y A.3), «A. GENERAL».
- **sdla** (la pieza para A.3): «A.3.» lleva la letra del último rótulo de letra (A) y está más afuera que la raíz
  abierta (149 contra 203), así que cierra la raíz 2 y abre la raíz `A.3`. Sola (sin sdl): `D1A3::SA.3` nueva (782
  caracteres: A.3, el rótulo de B, B.1 y B.2, porque B.1 y B.2 siguen sin poder abrir raíz) y `D1A3::S2` queda en
  667. Con sdl: `D1A3L1::SA.3`, de 211 caracteres, solo A.3. La forma «A.3.» de la regla 4 (raíz de letra «A» con sus
  puntos) no sirve acá: la abriría solo un «APARTADO A:», y los ítems numéricos de A.2 cerrarían esa raíz antes de A.3.
- **Juntas**: ri_ccna pasa de 159 a 164 unidades, y `D1A3::S2` (1.450 caracteres) queda separado en A.2.2
  (`D1A3L1::S2`, 667), A.3 (`D1A3L1::SA.3`, 211), el rótulo de B (`D1A3L2::S0`, 22), B.1 (304) y B.2 (242): las
  posiciones 0, 668, 880, 903 y 1.208 del prototipo de la mesa.
- **`D1A3L2::S0`, de 22 caracteres, solo el rótulo**: lo declaro, no lo evito. Es como las raíces «0» de un renglón
  que sd ya produce: en S0-4a-bis hay 7 (de 21 a 73 caracteres: `nmcief::A1P2::S0` y `A1P4::S0`,
  `ri_ccna::D2A1P1::S0` y `D2A1P2::S0`, `ri_icpipsp::A1C1::S0` a `A1C3::S0`). Evitarlo pide sacar el renglón del
  rótulo de toda unidad (no cumple la cobertura) o pegarlo al texto de B.1, que ya lo hereda.
- **Las guardas** (`censos/censo_formas_ter_152.json`): la regla va por lista y con la guarda de mayúsculas. En los 152,
  con la guarda (`scripts/censo_formas_ter_152.py`, sobre la corrida final): la forma de letra abre en tres TOs, ri_ccna
  y dos fuera de la lista: manori (p. 85, «A. PRECIO DE COMPRA $» a «F. MONTO DEL PRESTAMO…», filas de un cuadro) y
  ri_dsf («A. DATOS IDENTIFICATORIOS DEL DEUDOR», p. 2, y «B. DATOS SOBRE LA ASISTENCIA AL DEUDOR», p. 6), los que
  señaló el prototipo de la mesa. Sin la guarda de mayúsculas, aparecen además rótulos «letra. Título» con mayúscula
  inicial en 14 TOs (de 1 a 26 renglones; entre ellos ri_cc, 26, nmaeef, 6, y ri2_ae, 6). Por eso va por lista y con la
  guarda.

## 5. Controles duros, con cada regla nueva prendida y apagada

Todos en `censos/controles_S0-4a-ter.txt` y `censos/tanda0_S0-4a-ter.txt`, byte a byte:
- **Tanda 0, 57 de 57**, en diez corridas: la final (`impl4ter`, dos veces, iguales entre sí), todo apagado, las reglas
  de S0-4a-bis (las cinco nuevas apagadas), cada regla nueva sola encima de S0-4a-bis, y las cinco nuevas solas. Las
  reglas van por lista y ninguno de los diez TOs de la tanda 0 está en sus listas.
- **Los 25 archivos de la tanda 0 dentro de los 152**, iguales en las dos corridas finales (agregados: 20 iguales y 15
  ausentes en los dos).
- **Las cinco nuevas apagadas** (`proto4ter` con las reglas de S0-4a-bis) = S0-4a-bis, **768 de 768**.
- **Todo apagado = S1**, **768 de 768**, contra `corridas/base` y contra los sha256 de `s1/manifest_salida.json`.
- **Prendidas**, contra S0-4a-bis: 8 de 768 archivos distintos, todos de ri_oc y ri_ccna (sus `chunks_` y
  `estructura_`, y en `conteos.json`, `divergencias_indice_cuerpo.json`, `correcciones.json` y
  `encabezados_conservados.json`, solo sus entradas): ningún otro TO se mueve.
- **Doble corrida** de los 152 con el código final: 768 y 768, 0 distintos.
- **Prototipo y código**: el prototipo con todas las reglas da, en los 64 TOs que cambian contra S1, los mismos 320
  archivos por TO que el código sin interruptores; y las corridas de prueba de los seis TOs (`p_todas`), los mismos 30.
- **Selftest de claves** sobre la copia con el código final: VEREDICTO OK (anclaje r2b de E1 y E3 OK, contraste con la
  tabla OK) y salida igual byte a byte al JSON vigente del repo, `923dd900…` (`censos/selftest_claves_S0-4a-ter.txt`):
  ninguna clave de la tanda 0 se mueve.
- **Selftests de E0** (§8): en verde.
- **Unidades de más de 13.944 caracteres propios en los 152**: 28 (S1 34, S0-4a 29, S0-4a-bis 29). La que sale es
  `ri_oc::3.51`; ni ri_oc ni ri_ccna tienen ya ninguna.

## 6. Conciliación por regla

- **Cada regla sola, contra S0-4a-bis** (`censos/atribucion_S0-4a-ter_contra_S0-4a-bis.json`, `atribuir.py` de S0-1 con
  las corridas `p_<regla>` y `bis_final` para los demás TOs): 2 TOs, 168 eventos.
  - ri_oc, 64: sdr1 12 (8 nuevos, 3 que desaparecen y `3.51`), apl 52 (51 nuevos y `S0`); `3.51` lo cambian sdr1 y apl,
    cada una sola.
  - ri_ccna, 104: sdl 103 (53 nuevos, 49 que desaparecen, 1 que cambia) y 1 interacción, `D1A3L1::SA.3`: el id solo
    existe con sdl (el prefijo) y sdla (la raíz) juntas. sdlh (49 cambios de herencia) y sdla (`D1A3::SA.3` y
    `D1A3::S2`) no tienen eventos propios en la combinada porque sdl renombra esos ids: su efecto llega como contenido
    de los ids de sdl.
- **Cada regla dentro de la configuración final** (`censos/marginal_por_regla_S0-4a-ter.json`,
  `scripts/marginal_ter.py`: la final contra la final sin esa regla, en los seis TOs): sdr1, en ri_oc, 8 nuevos, 3 que
  desaparecen, `3.51` y la herencia de C.1 a C.11 (sin sdr1, los anexos quedan en el cierre de la raíz C que esos puntos
  heredan); apl, 51 nuevos y 2 cambios; sdl, 54 nuevos y 50 que desaparecen (uno más de cada lado que sola: también
  renombra A.3) y 1 cambio; sdlh, 52 cambios de herencia (las 49 de `D1A3L2` y las 3 de `D1A3L1`); sdla, 1 nueva
  (`D1A3L1::SA.3`) y 1 cambio (`D1A3L1::S2`); sdg3 y sdmax, lo mismo que en S0-4a-bis. Así cada efecto tiene una sola
  regla.
- **Contra S1** (`censos/atribucion_S0-4a-ter_contra_S1.json`, con las corridas de cada regla sola de S0-4a, y sdg3,
  sdmax y las cinco nuevas por resta contra la final sin cada una): 64 TOs, 1.609 eventos, que son los 1.540 de
  S0-4a-bis más 64 de ri_oc y 5 de ri_ccna (los ids nuevos de ri_ccna contra S1 pasan de «sd» a «sdl», y los ítems 31 a
  40, a «sdmax+sdl»). Interacciones, 2: `nmcief::A4::S1`, la de S0-4a, y `ri_oc::3.51`, que no es una interacción sino
  el evento que producen sdr1 y apl cada una por su lado: sacar una sola no lo quita, así que la resta no lo atribuye.
- **Unidades** (`censos/censo_final_ter_contra_S0-4a-bis.json`, `censo_final_ter_contra_S1.json`): S0-4a-bis 9.564 →
  S0-4a-ter **9.625** (+113 −52, 3 que cambian, en ri_oc y ri_ccna); contra S1, 9.554 → 9.625 (+431 −360), en 64 TOs (65
  con ri_mmsef). De los 52 ids que desaparecen, 51 son renombres con el mismo texto (3 en ri_oc, 48 en ri_ccna).
- **Tabla de reprocesamiento** (`censos/filas_por_regla_S0-4a-ter.json`): sdr1, F19b (5 nuevas), F05 y F02 (3
  renombres) y F01 (`3.51`); apl, F19b (51) y F01 (`S0`, `3.51`); sdl, F19b, F05 y F02 (48 renombres con el mismo texto)
  y F01; sdlh, F02 (49); sdla, F19b (1) y F01 (1). Ninguna fila nueva.

## 7. El parche final y las anclas de F19b

- **Parche** (`parche/`, con su LEEME; verificado sobre los archivos de `git show 26c6502:…` por los dos caminos,
  directo y sobre el de S0-4a-bis):
  - `e0_lib.py` `65a8c3b8…` (+696 −48 sobre `26c6502`; +85 −10 sobre S0-4a-bis);
  - `correr_e0.py` `94d35349…` (+79 −10; +24 −6);
  - `selftest_e0.py` `ec186071…` (+598 −9; +137 −16).
  Reemplaza al de S0-4a-bis para S0-4b.
- **Anclas de F19b** (`censos/anclas_f19b_S0-4a-ter.txt`; sobre el código de S0-4a-bis, el script reproduce las de esa
  etapa): `correr_e0.py:95-100` no se mueve, `:327-339 → :360-372`, `:576-585 → :609-618`, `:1266 → :1302`;
  `e0_lib.py:352 → :360`, `:473 → :556`. La tabla no la edito: la pone al día S0-4b.

## 8. Selftests

Sobre la copia, con el código final (`censos/selftests_e0_S0-4a-ter.txt`): `selftest_e0` **151/151**, b52 39/39,
b581 34/34, b582 59/59 y b583 33/33. De los 151, 14 son nuevos y 4 de S0-4a-bis cambiaron con la etapa (2 en q y 2
en s):
- **q** (1 nuevo y 2 ampliados): `limites_subdocumento` con `letras` y `sin_regimen_pagina_1` apagados por default;
  los tres parámetros de letra de `parsear_cuerpo` apagados por default; las reglas y las tres listas nuevas.
- **r** (8 nuevos, sintéticos): sdr1 (sin la regla, «10 – OPERACIONES DE CAMBIOS» de la página 1 prefija el anexo,
  `R10A1`; con ella, `A1` sin padre); apl (raíces numéricas y apartados de letra en la misma lectura sin raíz: sin el
  marcador, el Apartado B queda en el punto 1.1; con él, B.1.1 y B.1.2 son puntos de B y la raíz 1 sigue igual); sdl,
  tres casos (la forma da `A1L1` y `A1L2` con su letra y su padre, y «C. Datos…», sin mayúsculas, no; una serie que no
  empieza en la A no abre; sin la regla, B.1 y B.2 se rechazan y quedan en el ítem 2 de A, con ella son raíces de
  `A1L2`, sin heredar su rótulo); sdlh (sin sdl, `A1::S1` hereda «A. GENERAL» y `A1::S3` «B. PRUEBAS SUSTANTIVAS», sin
  otro cambio; con sdl, las de `A1L2` heredan su rótulo); sdla (sin sdl, `A1::SA.3`; con sdl, `A1L1::SA.3`, que hereda
  «A. GENERAL», y la raíz 2 ya no lleva A.3); y la cobertura exacta con las tres reglas de letra.
- **s** (5 nuevos y 2 actualizados, medidos sobre ocho TOs, con ri_oc agregado): sdl, sdlh y sdla en ri_ccna, sdr1 y
  apl en ri_oc; el caso de sdmax lee ahora los ítems 31 a 40 en `D1A3L2`, y la cobertura es en ocho TOs.

## 9. Correcciones a S0-4a-bis y a S0-4a

- **Los 11.427 caracteres no son el Apartado B solo** (S0-4a-bis, diseño §4 y FRENO). Medí ahora el texto que la
  variante de ri_oc dejaba en `ri_oc::3.51` (12.206 caracteres, `bis/corridas/oc_med`): 779 son del punto 3.51; desde
  «APARTADO B: POSICIÓN GENERAL DE CAMBIOS» (p. 16) hasta «APARTADO C» (p. 18) hay 4.659, que son el Apartado B; y los
  6.768 restantes son el Apartado C (p. 18) y lo que lo sigue hasta el Anexo I: «Criterios de validación», con la
  validación de los Apartados A, B y C, y «Aclaraciones» (pp. 18 a 21). En S0-4a-bis atribuí los 11.427 al Apartado B y
  le puse las páginas 16 a 21; la cifra llegó a la nota al pie y a la decisión (a) de la autora («el Apartado B, que
  queda dentro de 3.51, 11.427 de sus 12.206 caracteres»). Lo corrijo aquí y va como error propio (§13). Con apl, que
  separa los Apartados B y C, la cifra deja de ser un límite (§3).
- **ri_mmsef, con la precisión de la mesa**: el campo de la estructura que cambia entre S1 y S0-4a es el `text_col` del
  nodo 2.2 (de null a 76,6), además de los 3 avisos. Va en la nota fechada de S0-4b sobre el diseño de S0-4a (decisión
  d), junto con ri_tsa `reconocido_pleno`.

## 10. Límites declarados que quedan, con su cifra

- **ri_oc, los criterios de validación dentro del Apartado C**: los dos renglones del título («Criterios de
  validación», «Validación del Apartado A – Operaciones de cambios») al final de `ri_oc::C.11`, y su texto con las
  «Aclaraciones» (5.313 caracteres, pp. 19 a 21) como `ri_oc::SC::cierre`, heredado por C.1 a C.11 (39 tramos y 5.484
  caracteres de herencia cada uno; §3). El Apartado B, que era el límite de la decisión (a), ya no lo es: apl lo separa.
- **Unidades de solo rótulo** que agregan las reglas nuevas: `ri_ccna::D1A3L2::S0` (22 caracteres, «B. PRUEBAS
  SUSTANTIVAS»; sdl), `ri_oc::A2::S0` (30, «ANEXO II: Códigos de conceptos»; sdr1, como ya medía S0-4a-bis) y
  `ri_oc::SA` (34, «APARTADO A: OPERACIONES DE CAMBIOS»; apl). Las siete que ya había en S0-4a-bis siguen (§4).
- **ri_ccna, A.1 y A.2**: los rótulos «A.1. PRUEBAS DE CUMPLIMIENTO…» y «A.2. ANALISIS DE VARIACIONES» no abren unidad
  (están antes de cualquier raíz numérica de `D1A3L1`): quedan en `D1A3L1::S0` (1.220 caracteres: 550 de «A. GENERAL»
  y A.1, 670 de A.2 hasta sus ítems), y los dos ítems de A.2 heredan «A. GENERAL» pero no «A.2. ANALISIS DE
  VARIACIONES». De lo que pedía la decisión (b), no queda nada sin corregir.

## 11. Decisiones de la autora (PENDIENTES)

1. **apl separa también el Apartado C**, por la misma forma (§3); la autora confirma que entra así, con los criterios de
   validación dentro de C como límite declarado (§10).
2. **Las unidades de solo rótulo** nuevas (§10), declaradas como las de S0-4a-bis.
3. **El límite de A.1 y A.2 en ri_ccna** (§10), que la decisión (b) no cubría.
4. **Las correcciones** (§9): la cifra del Apartado B, para la nota al pie; y la precisión de ri_mmsef, en la nota
   fechada que S0-4b agrega al diseño de S0-4a.

## 12. Comandos

Desde la raíz del scratchpad. `../bis/scripts/` son los scripts de S0-4a-bis y `../scripts/`, los de S0-4a; `herr/` es
mi carpeta de herramientas (sus scripts son iguales a los de S0-4a y al `correr_152.py` de S0-1, como dice el diseño
de S0-4a-bis, §11).

```
scripts/lote_ter.sh <scratchpad> <python>                  (el lote: corridas, selftests de E0 y selftest de claves)
herr/correr_152.py --codigo raices/proto4ter --salida <dir> --workers <n> --tos <tos>   (con S0_4_REGLAS=<reglas>)
scripts/controles_ter.sh <scratchpad> <python>             (tanda 0 y controles de configuración, byte a byte)
scripts/marginal_ter.py <final> <dir con ter_sin_<r>> <reglas> <tos> <salida.json>   (efecto de cada regla en la final)
scripts/censo_formas_ter_152.py --codigo raices/impl4ter --corrida <dir E0> --salida <json>
../bis/scripts/censo_s04bis.py <base> <nueva> <salida.json> [--tos a,b]
../bis/scripts/por_to_iguales.py <a> <b> <tos>
../bis/scripts/contra_manifiesto_s1.py <corrida> <s1/manifest_salida.json>
../bis/scripts/anclas_f19b.py <código de 26c6502> <código de S0-4a-bis> <código final>
copia/data/experiment/segmentacion_oficial_e0r2/s0_1/scripts/atribuir.py --base <dir> --todas <dir> --regla … --resta … --out <json>
copia/data/experiment/segmentacion_oficial_e0r2/s0_2/scripts/filas_por_regla.py <corridas> <ref> <tos> <salida.json> <r>=<dir>
data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b \
    data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b --out <json>          (desde la raíz de la copia)
data/experiment/reextraccion_v2/e0_chunking/selftest_{e0,b52,b581,b582,b583}.py   (desde e0_chunking/ de la copia)
../scripts/raiz_minima.sh copia raices/<raíz> <dir con el código>
../scripts/grep_convenciones.py <repo> <paquete>
```

## 13. Errores propios, con su causa

1. **Los 11.427 caracteres de `ri_oc::3.51` atribuidos al Apartado B, en S0-4a-bis** (§9). Causa: medí desde
   «APARTADO B» hasta el final de la unidad y no leí lo que venía después; el Apartado C y los criterios de validación
   (6.768 caracteres) quedaron contados como Apartado B, y la cifra llegó a la nota al pie y a la decisión (a).
2. **Anclas escritas antes de leer el archivo, otra vez**, en el borrador de este diseño (`e0_lib.py:432-436` por
   :433-436 y cuatro rangos más). Las corregí contra el código antes de entregar. Es el mismo error que el 3 de
   S0-4a-bis: la regla que sigo desde ahora es tomar cada ancla con `grep -n` o `awk 'NR>=…'` sobre el archivo final y
   pegarla, no escribirla de memoria.
3. **Dos afirmaciones de un borrador de este diseño**, corregidas antes de entregar: que «I. DISPOSICIONES
   GENERALES…» de ri_ccna «es parte» (es un candidato a parte que no forma serie; ningún sub-documento P en la p. 2), y
   la descripción del texto de `D1A3::S0`.
4. **Un script de edición del selftest con un error de sintaxis** (mezclé una lista y `append`); falló antes de
   escribir, comprobé con el sha256 que el archivo no había cambiado y lo rehíce desde un archivo.
