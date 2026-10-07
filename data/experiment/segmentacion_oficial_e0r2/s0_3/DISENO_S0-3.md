# U-SEG-OFICIAL — S0-3: cinco mecanismos de E0 tras la lectura de cortes de S1 (diseño, prototipo y medición)

Etapa S0-3 del mandato FIRMADO en `e543cb2` (las 239 líneas firmadas dan `44cf30ca0d82…`), leído con sus notas al pie,
en particular las del 07/10/2026 (resultado de S1 y decisión de la autora: S0-3 acotada; `604640c`), y con el
despacho de S0-3, que fija el alcance (cinco mecanismos; nada más) y los controles duros. USD 0: ninguna llamada a la
API. No edité el código del repo: el prototipo es un parche sobre `26c6502` (`parche/`). Escribí solo esta carpeta
(`s0_3/`) y `../FRENO_S0-3.md`. Ningún commit.

## 0. Método

- Precondiciones, con su salida, en `censos/precondiciones_S0-3.txt`: el código de E0 del repo es el de `26c6502`
  (`git diff --stat 26c6502 HEAD` de `e0_chunking/`, vacío; sha256 de los tres archivos, iguales a los de S0-2); el
  texto firmado da `44cf30ca…`; la nota de la decisión S0-3 está en `604640c` y la del sorteo de cortes, en `2faff14`.
- Copia de trabajo: el árbol del repo (HEAD `ee7c07c` al empezar) copiado al scratchpad sin `.git`, `.venv`, `.venv-app`,
  el volumen de Neo4j, `data/raw/` ni `s1/e0/`; los 336 enlaces simbólicos absolutos que trae, borrados de la copia.
  Con las bases de caché, que el selftest de claves necesita. Durante la unidad entraron 5 commits de otras unidades
  (`ee7c07c..93bebd2`); ninguno toca el mandato de esta unidad, `e0_chunking/`, esta carpeta, la tabla de
  reprocesamiento, la partición ni los PDF (`git diff --stat ee7c07c HEAD` de esas rutas, vacío salvo el mandato de
  otra unidad).
- Base de comparación: la E0 de S1 (código de `26c6502`). La reproduje sobre la copia con `../s0_1/scripts/correr_152.py`:
  768 de 768 archivos iguales byte a byte a `s1/e0/`; y la tanda 0 con `../s0_1/scripts/correr_tanda0.py`: 57 de 57
  iguales a `salida_tanda0_r2b/`.
- Dos códigos en copias: `impl3`, sin interruptores (el que da el parche), y `proto3`, el mismo con dos variables de
  entorno que eligen las reglas (`S0_3_REGLAS`) y miden el mecanismo 4 también en la tanda 0 (`S0_3_M4_EN_TANDA0`),
  solo para medir cada regla sola. Con todas las reglas, los dos dan la misma E0 (§5).
- Cada forma es un parámetro apagado por default en `e0_lib.py` (la versión legada no las conoce, selftest n) y
  encendido en la escalera de e0-r2 de `correr_e0.py` (`REGLAS_S0_3`).

## 1. Los cinco mecanismos: reglas, formas y dónde están en el código

Anclas de línea sobre el código del parche (`impl3`).

### Mecanismo 1 — cuerpo de punto que queda como intersticial del padre, partido por renglón

Causa (S1, filas 29, 42, 43, 45, 49, 63 y 74 de las marcas): un punto cuyo rótulo y cuerpo están en la misma columna,
la columna de texto de su padre. La primera línea de prosa después del rótulo coincide con la columna de un ancestro y
el parser la re-ancla a él (`e0_lib.py`, «re-anclaje a un ancestro»); el punto queda en su rótulo y su cuerpo sale como
intersticiales del padre, uno por cambio de columna.

- **Forma a** (la regla del despacho; `parsear_cuerpo(formas_m1={"a"})`, `e0_lib.py:1729-1738`): si el punto abierto
  todavía es solo su rótulo (sin segmentos ni hijos, sin columna de texto) y la prosa que sigue está en la columna del
  rótulo, la prosa es cuerpo del punto. **Guarda** (`_sangria_colgante_m1`, `:1781`), agregada después del primer censo:
  no actúa si un hermano anterior del punto tiene su cuerpo más adentro que su rótulo (sangría colgante: la prosa a la
  altura del rótulo es del padre, como el cierre del 2.7 de ext) o es un renglón suelto, sin cuerpo ni hijos (una lista
  de ítems de un renglón: la prosa que sigue al último es el cierre del padre). Sin esta segunda condición la regla
  cambiaba tres unidades de la tanda 0 (cap 8.6.3, ctacte 5.1.1.2 y ext 11.1.3.12, las tres el último ítem de una lista
  de renglones sueltos seguido del cierre del padre); con ella, ninguna (§4).
- **Forma b** (agregada para snp_cheq, que el despacho nombra en este mecanismo pero la regla escrita no alcanza;
  `:1739-1746`): en snp_cheq 7.1.x el rótulo está centrado (x0 63,8) y el cuerpo corre a su izquierda (46 a 58); las
  descripciones de campo a x0 57,5 coinciden por azar con la columna de texto de 7.1 (56,8) y se re-anclan a 7.1. La
  forma b: un punto cuyo cuerpo corre a la izquierda de su rótulo no devuelve prosa a un ancestro. Es una extensión de
  la regla del despacho, declarada: decide la autora (§7).

### Mecanismo 2 — numeración o título no leído, pegado a la unidad anterior

Solo en el modo sin raíz, en la línea que abre una raíz (`parsear_cuerpo(formas_m2=…)`, `e0_lib.py:1404-1420` y
`:1494-1496`):
- **forma a**, número pegado al título: «4.Integración de los aportes.» (seggar p. 4; `RE_NUM_PEGADO_M2`, `:381`);
- **forma b**, número con guion y título en mayúsculas: «1- INTRODUCCIÓN» (ri2_pm pp. 1 y 3; `RE_NUM_GUION_M2`, `:382`);
- **forma c**, título en mayúsculas sin punto final en una columna más profunda que la de las raíces abiertas: la guarda
  de columna (G3) no la rechaza («2. CUADRO 1 – CANTIDAD DE TARJETAS EMITIDAS», ri_tar p. 2; G3 la rechazaba por estar
  14 pt más adentro que la raíz 1).
- **Guardas**, agregadas después del primer censo, cada una por un caso leído: la raíz sucede exactamente a la anterior
  (o es la 1) — sin ella, «26.ANTICIPO DE OPERACIONES» (el número del régimen en el título de ri_ao) abría la raíz 26 y
  absorbía el documento; en las formas a y b el renglón no se repite textualmente en la zona de título de 3 páginas o
  más (`detectar_banners_texto`) — sin ella, «3.Deudores del Sistema Financiero.», el título corrido de ri_dsf, abría
  una raíz; y las raíces de las formas a y b no fijan la columna de las raíces — sin ella, en ri_dsf «1.Instrucciones
  generales.» fijaba una columna más afuera que la del diseño de registro y G3 rechazaba las raíces 3 a 8. Una raíz que
  no pasa una guarda deja el renglón como estaba (sin rechazo nuevo en la estructura).
- Cada raíz que abre una forma nueva queda declarada en los avisos de la estructura (`raiz_m2`, con su forma).

### Mecanismo 3 — índice leído como cuerpo (cuarta forma de la regla 8)

`lineas_de_listas_r8(forma4_m3=True)` y `paginas_indice_r8(forma4_m3=True)` (`e0_lib.py:407-461` y `:509-513`): además
de las listas de rótulos de dos niveles, una lista de al menos 3 rótulos de un nivel, consecutivos (el índice del
Anexo I de ri2_ae p. 3: «1. Designación» a «9. Confidencialidad»), con las mismas guardas de la regla 8 (cada número
reaparece después como rótulo con el mismo título en el 80 % de los rótulos; a lo sumo un 25 % con un renglón en
minúscula; brecha mediana entre reapariciones mayor que 3). Si la página es entera esa lista, pasa a índice (ampliación
de la regla 3); si no, sus rótulos se vetan. Acotada por el censo de páginas de la regla 8 (decisión 8 de S0-2): toda
página que cambie de rol es hallazgo (§3).

### Mecanismo 4 — primer renglón tomado como título

`titulo_es_texto_m4` y `construir_chunks(titulo_texto_m4=True)` (`e0_lib.py:2466-2477` y `:2499-2511`): en un punto con
hijos, el renglón del rótulo no es su título sino el primero de su texto si termina en guion de corte o no termina en
punto, y el renglón siguiente (el primero de su intro) empieza en minúscula (seguef 2.1.6: «…deberán complementar su
seguri-» / «dad con dispositivos…»). Entonces el encabezado heredado del punto es solo su número («2.1.6.») y el renglón
del rótulo encabeza el bloque de la intro, en el mini-chunk y en el tramo heredado por sus hijos.

**Choca con el control duro de la tanda 0** (§4): la E0 de la tanda 0 tiene 123 puntos con esta forma en 9
de sus diez TOs; la regla cambia esas intros y la herencia de sus hijos, filas F01 a F03 de la tabla de reprocesamiento,
que cambian la clave de E1 y de E3 de esas unidades (`tabla_reprocesamiento.md:145-147`). En el
prototipo el mecanismo no corre en los diez TOs de la tanda 0 (`correr_e0.TOS_TANDA0_SIN_M4`, `:121`): es mi
propuesta, decisión de la autora (§7).

### Mecanismo 5 — la zona de encabezado

`separar_encabezado_pie(cierre_m5, cola_m5, zona6_m5)` (`e0_lib.py:804-806`, `:895-924`, `:955-956`, `:975`, `:989-1014`):
- **forma a** (fimipyme p. 4, ri_cc pp. 60 y 62): después de la primera línea de sección de la zona, una línea de
  sección de otro número o con «B.C.R.A.» cierra el encabezado, y una con «B.C.R.A.» se descarta como encabezado, solo
  si su texto se repite en la zona de título de otra página de cuerpo. Primer censo: con «una línea de sección que no
  se repite» a secas, el título de la misma sección repetido bajo el recuadro (dmrd pp. 6 a 60, 8 renglones) pasaba a
  ser texto; la refiné a «de otro número».
- **forma b** (ri2_ci p. 5; además snp_cheq p. 71): un renglón no es cola del título si empieza con un inciso («ii)»), ni
  si el título no quedó abierto (no termina en guion, coma ni palabra de enlace), el renglón no está en la columna de la
  línea de sección y el que le sigue está en su misma columna a interlineado de párrafo. Primer censo: sin la condición
  del título abierto, las colas reales de dos renglones de ctacte (pp. 44 a 48, tanda 0) y ctavis (pp. 30 a 33) dejaban
  de serlo; la condición viene de `continua_titulo` (`:1017`), sin la parte que mira el renglón siguiente.
- **forma c** (ri_ai p. 3): si los cinco primeros renglones son el recuadro (en mayúsculas o con «B.C.R.A.») y el sexto
  es la línea de sección, la zona es de seis renglones y la sección se abre.
- **Los apartados de `ri_ai::S4`** («1. Posición», «2. Franquicias», «3. Incumplimientos»), que el despacho nombra en esta
  forma, **no son un caso de la zona de encabezado**: la sección 4 se abre bien (p. 7, quinto renglón) y los apartados
  se rechazan por `fuera_de_seccion_4` (numeración propia dentro de una sección sin puntos). Leerlos como unidades es
  otro mecanismo; no lo implementé. Censo en §6.

## 2. Censo por regla en los 152 TOs

Cada regla sola contra la base (`censos/censo_v_<regla>.json`, `scripts/censo_s03.py`; corridas del prototipo con
`S0_3_REGLAS=<regla>`). «Renglones» son los que cambian de rol: de prosa a rótulo (mecanismo 2), de cuerpo a índice
(3), del rótulo a la intro (4) o entre encabezado y texto (5); en el mecanismo 1, los puntos que recuperan su cuerpo
(1a) y los renglones que ya no se re-anclan al padre (1b), según los avisos de la estructura. «Cambian»: unidades
comunes con otro texto, herencia, páginas o marcas. La tanda 0 da 57 de 57 archivos iguales con cada regla sola
(`censos/tanda0_por_regla.txt`).

| regla | TOs | renglones | rótulos +/− | ids +/− | unidades | cambian (F01 / F02 / F03) |
|---|---|---|---|---|---|---|
| 1a | nmcief, ri_dcpc (y ri_mmsef, solo el aviso) | 33 puntos con cuerpo | 0 / 0 | 0 / 69 | 9.554 → 9.485 | 32 (27 / – / 5) |
| 1b | snp_cheq | 31 renglones | 0 / 0 | 0 / 109 | → 9.445 | 55 (47 / – / 8) |
| 2a | manual, ri_ao, ri_dsf, ri_icpipsp, seggar, verac | 18 a rótulo | 18 / 11 | 11 / 3 | → 9.562 | 49 (11 / 34 / 6) |
| 2b | ri2_pm | 2 a rótulo | 2 / 2 | 0 / 0 | = | 14 (2 / 12 / –) |
| 2c | manual, ri_tar | 5 a rótulo | 20 / 0 | 42 / 25 | → 9.571 | 6 (2 / – / 4) |
| 3 | ri2_ae | 1 página a índice (12 renglones de contenido) | 18 / 10 | 15 / 9 | → 9.560 | 5 (5 / – / –) |
| 4 | 51 TOs (fuera de la tanda 0) | 150 rótulos a la intro | 0 / 0 | 0 / 0 | = | 762 (150 / 612 / 563) |
| 5a | fimipyme, ri_cc | 5 de encabezado a texto | 0 / 0 | 0 / 0 | = | 10 (3 / – / 7) |
| 5b | ri2_ci, snp_cheq | 3 de encabezado a texto | 0 / 0 | 0 / 0 | = | 2 (2 / – / –) |
| 5c | ri_ai | 2 de texto a encabezado | 3 / 0 | 2 / 0 | → 9.556 | 1 (1 / – / –) |
| **todas** | 65 (64 con unidades que cambian) | — | 61 / 23 | **70 / 215** | **9.554 → 9.409** | 920 (250 / 642 / 588) |

En el mecanismo 4, F02 y F03 se superponen (una unidad puede cambiar los dos tramos heredados); entre reglas, las
unidades que cambian no se suman (manual cambia con 2a y 2c; snp_cheq con 1b, 4 y 5b). La lista por TO, con las
unidades antes y después, los ids, los renglones y los rótulos, está en `censos/censo_v_final.json` (`por_to_resumen`
y `por_to`); los 51 TOs del mecanismo 4, en `censos/censo_v_m4.json`. Sin el mecanismo 4 (variante `sin_m4`) cambian
17 TOs y las unidades dan lo mismo (9.409): la regla 4 no agrega ni quita ids.

## 3. Censo de renglones que cambian de rol (configuración final)

Configuración final contra la base (`censos/censo_v_final.json`):
- de encabezado a texto, 8 renglones: fimipyme p. 4 (2, el comienzo del único párrafo de la sección 1), ri_cc p. 60 (2,
  el ítem de ponderación) y p. 62 (1, el rótulo «4. Facilidades Otorgadas por el B.C.R.A.»), ri2_ci p. 5 (2, de
  1.1.1.4) y snp_cheq p. 71 (1, «ii) Cabecera de lote»). Son los 7 renglones de texto de norma perdidos del censo de los
  28 de S1 (`s1/lectura_cortes/censo_28_renglones_sin_explicacion_S1_mesa.md`) y el título del ítem ii de snp_cheq;
- de texto a encabezado, 2 renglones: ri_ai p. 3, la cola del recuadro («CONCEPTOS. (R.I. – A.I.)») y la línea
  «Sección 2. Instrucciones generales», que pasa a abrir la sección;
- una página cambia de rol: ri2_ae p. 3, de cuerpo a índice (18 renglones, 6 de encabezado y pie y 12 de contenido);
  ninguna otra página cambia de rol en los 152 (acotada por el censo de páginas de la regla 8, decisión 8 de S0-2);
- de prosa a rótulo y al revés (rótulos de nodos de la estructura): 61 nuevos y 23 que desaparecen, en 10 TOs (las
  formas del mecanismo 2, el índice de ri2_ae y la sección 2 de ri_ai); los títulos de raíces implícitas («1.», sin
  título) reemplazados por el título leído cuentan en los dos lados.

## 4. Controles duros

- **Los 25 archivos de la tanda 0** (ctacte, lingob, polcre, pagjub y docvig: chunks, estructura, índice, tablas y pies)
  dentro de la corrida de los 152, con el código del parche: 25 de 25 iguales byte a byte a `salida_tanda0_r2b/`; sus
  entradas de los agregados, 20 iguales y 15 ausentes en los dos lados (sub_chunking, encabezados_conservados e
  ids_desambiguados), como en S1. Además, la tanda 0 entera (los diez TOs con `correr_tanda0.py`): 57 de 57 archivos
  iguales, en las dos corridas y con cada regla sola (`censos/doble_corrida_S0-3.txt`, `censos/tanda0_por_regla.txt`).
- **Selftest de claves** sobre la copia con el parche y las bases: VEREDICTO OK, contraste con la tabla OK, anclaje r2b OK;
  la salida, igual byte a byte a la de HEAD (`censos/selftests_S0-3.txt`). Ninguna clave de la tanda 0 se mueve.
- Los dos controles se cumplen **porque el mecanismo 4 no corre en la tanda 0**. Sin esa exclusión (variante
  `m4_t0m4`), la tanda 0 cambia en 10 de sus 57 archivos (los chunks de 9 TOs y `conteos.json`): 123 intros y 738 de sus
  2.439 unidades (`censos/censo_t0_m4_en_tanda0.json`).

## 5. Corrida de los 152, doble, y conciliación contra S1

- **Doble corrida** de los 152 con el código del parche (`../s0_1/scripts/correr_152.py --codigo <copia con el parche>`):
  768 y 768 archivos, **0 distintos**; y la primera, igual byte a byte a la del prototipo con todas las reglas (0 de 768
  distintos): el parche limpio y el prototipo dan la misma E0 (`censos/doble_corrida_S0-3.txt`).
- **Conciliación de unidades contra S1** (`censos/censo_v_final.json`, `censos/atribucion_S0-3.json`): 9.554 → **9.409**
  (+70 −215). Por regla, cada una sola contra la base, y la suma cierra con la combinada: 1a −69; 1b −109; 2a +11 −3;
  2c +42 −25; 3 +15 −9; 5c +2; 2b, 4, 5a y 5b, 0 (+70 −215).
- **Atribución** (el método de S0-1, `../s0_1/scripts/atribuir.py`): en los 64 TOs cuyas unidades cambian hay 1.206
  eventos (920 unidades que cambian, 215 ids que desaparecen, 70 nuevos y 1 cambio de orden, el de los intersticiales de
  snp_cheq 7.1 que quedan, por 1b), y cada uno lo produce una regla sola: 4, 746; 1b, 165; 1a, 96; 2c, 73; 2a, 63; 3, 29;
  2b, 14; 5a, 10; 1a y 4 a la vez, 5; 5c, 3; 5b, 2. «Interacción», 0. En ri_dcpc, 4 sola cambiaría la herencia de 11
  intersticiales de 4.2 que con 1a desaparecen. ri_mmsef cambia solo en un aviso de la estructura (1a hace lo que antes
  hacía la reapertura de la regla 7) y sus unidades son las mismas: con él, 65 TOs cambian algún archivo.
- **Unidades que cambian en los 17 errores de S1**: §6.

## 6. Lo que S0-3 no cubre

De los 17 errores de corte del primer grupo de la lectura de S1 (`s1/lectura_cortes/marcas_lectura_cortes_S1_mesa_136_filas.tsv`),
la configuración final cambia 12 en la dirección de la corrección y deja 5 sin cambio
(`censos/errores_S1_frente_a_S0-3.json`, `scripts/errores_s1_vs_s03.py`; no es una lectura: dice qué unidad cambia y
cómo empieza y termina, para leer en S1-bis):

| fila | unidad de S1 | qué hace S0-3 |
|---|---|---|
| 29 | `snp_cheq::7.1::intersticial::107` | desaparece: la descripción del campo 8 vuelve a `snp_cheq::7.1.6` (1b; 7.1.6 pasa a pp. 98 a 100) |
| 42 | `ri_dcpc::3.1.1` | 46 → 817 caracteres: lleva sus dos párrafos (1a) |
| 43, 45, 49 | `ri_dcpc::3.1::intersticial::4`, `3.2::intersticial::4`, `3.2::intersticial::1` | desaparecen: las viñetas vuelven al cuerpo de 3.1.3.3 y 3.2.1 (1a) |
| 47 | `seguef::2.1.6::intro` | empieza en «2.1.6. Cuando se decida…» (4) |
| 54 | `ri_tar::1.1` | 5.621 → 985: solo «Aclaraciones»; se abren los cuadros 2, 3 y 4 (2c; 2 → 17 unidades) |
| 63, 74 | `nmcief::3.2::intersticial::11` y `::20` | desaparecen: el cuerpo de 3.2.1 y 3.2.3 vuelve a su punto (1a) |
| 69 | `seggar::S3::cierre` | 624 → 112: se abre la sección 4 (2a) |
| 76, 86 | `ri2_ae::S1`, `ri2_ae::S4` | la p. 3 pasa a índice; S1 es la sección 1 del cuerpo (14 → 4.647); S4 del índice desaparece (3) |
| 58 | `ri_sef::S0` | sin cambio: partes I, II y III con números romanos y anexos |
| 59 | `nmaeef::2.9` | sin cambio: el cierre de la sección 2 sigue al último ítem en el mismo margen (el caso inverso del mecanismo 1) |
| 71 | `nmcief::S3::chapeau_seccion` | sin cambio: la sección 4 («4. Periodicidad…», 9,5 pt más adentro, sin mayúsculas), las partes III y IV del Anexo I (romanos) y el Anexo II con numeración propia |
| 82 | `ri_ccna::S8::cierre::parte7` | sin cambio: declaraciones juradas y anexos con numeración propia |
| 85 | `ri_icpipsp::S8` | sin cambio: la tabla del Anexo I con filas numeradas y el Anexo II |

Cuatro de los cinco que quedan son de la familia de sub-documento (anexos o partes con numeración propia que reinicia:
ri_sef, nmcief, ri_ccna, ri_icpipsp), la misma de ri_cc, ri_tsa y el Manual de Cuentas de ri2_pm, que el despacho deja
fuera de S0-3 (S0-4, antes de la tanda 3). El quinto (nmaeef 2.9) es el inverso del mecanismo 1: en un documento de
diseño plano, el párrafo que cierra la sección después del último ítem está en el margen del ítem.

**Proyección sobre el piso, NO es una lectura** (la lectura de S1-bis es la que cuenta): si la muestra de S1 se leyera
con el código de S0-3 y los 12 cambios resultaran correctos, quedarían al menos 5 errores en 90; con 5, la cota inferior
de Wilson es 0,8765, bajo el piso de 0,90 (admite 3: 0,9065). Con una tasa de error de 5 en 90 en la población del
primer grupo, la probabilidad de que una muestra nueva de 90 tenga 3 errores o menos es 0,257 (binomial).

Otros límites que dejo declarados:
- **ri2_ae, secciones 3 a 8** (efecto del mecanismo 3): con la p. 3 como índice se abren las secciones 1 y 2 del cuerpo,
  pero los rótulos «3. Exclusión…» a «8. Régimen aplicable…» están 3,5 a 7 pt más adentro que la raíz 1 (deriva de
  márgenes entre Comunicaciones) y la guarda de columna (G3) los rechaza: sus rótulos y su texto quedan dentro de
  otras unidades (el de la sección 3 en `ri2_ae::2.2`; los de 4 y 5 en `ri2_ae::3.3`; los de 6 a 8 en `ri2_ae::5.3`).
  Antes también quedaban fuera (en `ri2_ae::S9`, que se llevaba el Anexo I entero). Censo de raíces rechazadas por G3
  que suceden exactamente a la anterior: 26 en 9 TOs (`censos/g3_raices_sucesoras_rechazadas.json`); mezcla títulos reales (seggar «6. Instrumentación.», nmcief «4.
  Periodicidad…», ri2_ae, ri_laft «2. Periodicidad») con filas de tabla e ítems (manual «5. Irrecuperable 50% 100%»,
  nmaeef, ri2_cs, ri_ccna). Relajar G3 no está entre las tres formas del despacho; no lo hice.
- **Apartados de un nivel dentro de una sección sin puntos** (ri_ai S4, que el despacho nombra): en los 152 hay 38 listas
  de rótulos «1.», «2.»… consecutivos rechazados por `fuera_de_seccion_N` (por sección y página): 6 en 5 secciones sin
  puntos de 5 TOs (ri_ai S4, ri_cc S3, ri_psp III, ri_rml 6 y ri_tsa S3, esta en dos páginas; ri_cc y ri_tsa, dentro de
  sub-documentos ya declarados) y 32 en 5 secciones con puntos de 4 TOs (adfsp 6, cajasc 9, snp_cheq 7 y snp_dd 3 y 7:
  sobre todo descripciones de campos); en la tanda 0, 2 (cap S4 y ric S11)
  (`censos/apartados_un_nivel_en_seccion.json`). Es otro mecanismo (numeración propia dentro de una sección); no lo
  implementé.
- **Mecanismo 4 y los títulos partidos**: de las 150 intros del mecanismo 4 en los 152 (fuera de la tanda 0), 104
  terminan en dos puntos (la oración que abre una lista, el caso de seguef), 30 son de un renglón sin dos puntos (en la
  muestra que leí, títulos partidos en dos renglones: «10.7. Procedimientos especiales… tributaria» / «internacional.») y
  16 de varios renglones (clasificación por la forma de la intro, `censos/m4_formas_de_la_intro.json`). En los títulos
  partidos la intro pasa de un pedazo de título a ser el título entero: deja de empezar a mitad de frase, pero queda
  como una unidad sin texto normativo. La regla del despacho no los distingue.
- **nmaeef p. 63** (título del modelo de nota del Anexo V, «EXTERNO/A DE ENTIDADES SUJETAS AL CONTROL DEL B.C.R.A.…»):
  sigue fuera; nmaeef no tiene líneas de sección y la forma a del mecanismo 5 actúa solo después de una.
- ri_cc (sub-documento), ri_spi, ri_tar p. 1 r. 10 y las vías de ri2_pm y ri_spi: fuera de S0-3 por el despacho.

## 7. Decisiones de la autora (PENDIENTES)

1. **Mecanismo 4 y la tanda 0** (contradicción entre el despacho y los archivos: la regla escrita no puede cumplir el
   control duro). La E0 de la tanda 0 tiene 123 intros con esta forma en 9 de sus 10 TOs (cap 9, cla 1, ctacte 14, ext
   89, lingob 2, pagjub 3, polcre 2, pro 1, ric 2); con la regla, cambian 738 de sus 2.439 unidades (las intros y la
   herencia de sus hijos; `censos/censo_t0_m4_en_tanda0.json`, `censos/tanda0_por_regla.txt`, variante `m4_t0m4`).
   Opciones: (a) la regla no corre en los diez TOs de la tanda 0 (lo que hace el prototipo; la tanda 0 conserva el
   defecto, declarado, hasta una release que la re-extraiga); (b) la regla en todas partes, con re-extracción de esas
   unidades de la tanda 0 y re-sellado (rompe el control duro tal como está escrito); (c) sin mecanismo 4, límite
   declarado (150 intros en 51 TOs de los 152, fuera de la tanda 0, más las 21 de los cuatro TOs de la tanda 0 que son
   de la partición). Recomiendo (a).
2. **Forma 1b** (snp_cheq), extensión de la regla escrita del mecanismo 1: la regla del despacho no alcanza el caso de
   snp_cheq que nombra. Recomiendo incluirla: actúa solo en snp_cheq (31 renglones; 362 → 253 unidades) y no toca la
   tanda 0.
3. **Las guardas** que agregué a las reglas escritas por los casos leídos (1a: lista de renglones sueltos y sangría
   colgante; 2: sucesión exacta, título corrido, columna de raíz; 5a: «de otro número»; 5b: título abierto): sin ellas
   la regla rompía la tanda 0 (1a, 5b) o empeoraba TOs que no estaban en el despacho (2: ri_ao, ri_dsf; 5a: dmrd).
4. **Los apartados de ri_ai S4** quedan fuera (no son de la zona de encabezado; otro mecanismo).
5. **El piso de S1-bis**: con lo que dejo, la proyección sobre la muestra de S1 es de al menos 5 errores en 90 (§6),
   cuatro de ellos de sub-documento. Antes de S1-bis, la autora decide si sigue a S1-bis con S0-3 tal como está
   (probabilidad aproximada de llegar al piso: 0,26, si la tasa de error del primer grupo fuera 5 en 90) o si adelanta
   la regla de sub-documento (S0-4) a antes de S1-bis.
6. Las filas de la tabla de reprocesamiento por regla (§9): ninguna nueva; F19b, F01, F02 y F03, como en S0-2.

## 8. Selftests

Sobre la copia con el código del parche (`impl3`), desde `e0_chunking/`, con `PYTHONDONTWRITEBYTECODE=1` y `-B`
(`censos/selftests_S0-3.txt`):
- `selftest_e0.py`: **110/110**. Los 84 de S0-2 (con dos casos medidos movidos: el acompañamiento T pasa de ri_dcpc a
  snp_dd, porque con el mecanismo 1a las tablas de ri_dcpc quedan en el cuerpo de 2.4 y 2.5 y T ya no actúa ahí; la
  regla 7 pasa de ri_mmsef a manori 1.5, porque el mecanismo 1a no cierra ri_mmsef 2.2 y la reapertura ya no hace falta,
  con las mismas unidades) y 26 nuevos: n) 3, la versión legada; o) 13 casos sintéticos, uno o más por forma, cada uno
  con el resultado sin la regla al lado; p) 10 casos medidos sobre nueve TOs (ri_dcpc, nmcief, seggar, ri_tar, ri2_ae,
  seguef, fimipyme, ri2_ci, ri_ai) y la cobertura exacta. La primera corrida dio 109/110: el caso medido de la regla 7
  en ri_mmsef; lo moví y la segunda dio 110/110.
- `selftest_b52.py` 39/39, `selftest_b581.py` 34/34, `selftest_b582.py` 59/59, `selftest_b583.py` 33/33.
- Selftest de claves (`data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b
  data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b`, desde la raíz de `impl3`, con las bases): VEREDICTO OK,
  contraste con la tabla OK, anclaje r2b OK (2.449 claves de E1); la salida es igual byte a byte a
  `data/experiment/mantenimiento/selftest_clave_cache.json` de HEAD. Ninguna clave de la tanda 0 se mueve.

## 9. Tabla de reprocesamiento

Qué clase de cambio produce cada regla sobre las unidades (`censos/filas_por_regla_S0-3.json`, el script de S0-2,
`../s0_2/scripts/filas_por_regla.py`): unidades agregadas o retiradas por una regla de E0 (F19b) en 1a, 1b, 2a, 2c, 3 y
5c; texto propio (F01) en todas; herencia de encabezado (F02) en 2a, 2b y 4; herencia de prosa (F03) en 1a, 1b, 2a, 2c,
4 y 5a. Son filas que ya están en la tabla desde S0-2 (`data/experiment/mantenimiento/tabla_reprocesamiento.md`, F01 a
F03 y F19b); no hace falta una fila nueva. En la tanda 0 no se dispara ninguna: su E0 no cambia un byte, y el selftest
de claves da OK con la salida igual a la de HEAD (§8). No edité la tabla.

## 10. Comandos

Sobre una copia del repo sin enlaces, con `PYTHONDONTWRITEBYTECODE=1` y el python de `.venv` con `-B`. `<copia>` es una copia
con el parche aplicado; `<proto>`, la misma con el parche de interruptores.
```
../s0_1/scripts/correr_152.py --codigo <copia> --salida <dir> [--workers 8] [--tos a,b]
../s0_1/scripts/correr_tanda0.py --codigo <copia> --salida <dir>
S0_3_REGLAS=<reglas> S0_3_M4_EN_TANDA0=<0|1> ../s0_1/scripts/correr_152.py --codigo <proto> --salida <dir>
scripts/lote_reglas.sh <scratchpad> <python>          (cada regla sola, sobre los 152 y la tanda 0)
scripts/censo_s03.py <base> <nueva> <salida.json> [--tos a,b]
scripts/censos_complementarios.py <base> <final> <tanda 0 base> <dir censos>
scripts/errores_s1_vs_s03.py <tsv de marcas de S1> <base> <final> <salida.json>
../s0_1/scripts/atribuir.py --base <base> --todas <final> --regla m1a=<dir> … --out <json>
../s0_2/scripts/filas_por_regla.py <corridas> base <tos> <salida.json> m1a=v_m1a … final=v_final
../s0_1/scripts/comparar_e0.py <base> <nueva> <salida.json>
data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b --out <json>
data/experiment/reextraccion_v2/e0_chunking/selftest_{e0,b52,b581,b582,b583}.py   (desde e0_chunking/ de la copia)
```
