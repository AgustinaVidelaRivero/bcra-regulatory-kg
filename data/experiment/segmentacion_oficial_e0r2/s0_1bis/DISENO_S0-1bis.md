# U-SEG-OFICIAL — S0-1 bis: regla 6 en E1, lista de puntos leída como cuerpo y filas del catálogo de rdbcra

Etapa S0-1 bis de la nota fechada del 05/10/2026 al pie del mandato de U-SEG-OFICIAL (`d59921f`; el texto firmado
sigue dando `44cf30ca0d82…` con `git show e543cb2:docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md | shasum -a 256`).
Parte del prototipo final de S0-1 (`../s0_1/parche/`, en `3920323`) y toma como dadas las decisiones de esa nota:
la regla 5 por lista, el acompañamiento T, la regla 6 en E0 como se propuso, la regla 6 en E1 sin cambiar la
partición por corte de la tanda 0, y ri_cc y ri_tsa sin cambio en E0. USD 0: ninguna llamada a la API. No implementé
nada en el repo: el prototipo vive en una copia del scratchpad y va como parche sin aplicar en `parche/`. Los censos
están en `censos/`; los scripts nuevos, en `scripts/`; los de S0-1 que reuso, en `../s0_1/scripts/` (§9).

## 0. Método

- Copia: la del prototipo de S0-1 (`e0_lib.py` `2405862332cfed73…`, `correr_e0.py` `d0b4bcd453e89b30…`), armada
  copiando, sin enlaces simbólicos, sin bases `.db`, sin `corpus_tanda0/` y sin `logs/` (control en el freno).
- Base de comparación: la corrida final de S0-1 de los 152 TOs (el prototipo de S0-1 con todas sus reglas), con los
  scripts de S0-1 (`correr_152.py`, `correr_tanda0.py`, `comparar_e0.py`). En este documento, «antes» es esa corrida
  y «después», la corrida final de S0-1 bis (todas las reglas, más la 8 y la 9). En los JSON de `censos/` esas
  corridas se llaman por su directorio del scratchpad: `final_c` (antes), `bis_final2` (después), `inter_r8` (con el
  código final, sin la regla 9), `solo9b` (la regla 9 sin la parte 9a) y `t0_bis_final` (la tanda 0).
- Interruptores del prototipo: `S0_REGLAS` suma `r8` y `r9`; `S0_RAZON_E1` fija la razón de tokens por carácter
  del tercer escalón (1,175 por omisión).
- Con las reglas de S0-1 y sin la 8 ni la 9, el prototipo nuevo reproduce byte a byte la corrida final de S0-1 en
  los 152 (`censos/condiciones_S0-1bis.txt`): el código nuevo no corre si su regla está apagada.

## 1. Resultado de conjunto

- Tanda 0: 57 de 57 archivos iguales byte a byte a `salida_tanda0_r2b/`.
- `particionar_por_corte` sobre las 2.439 unidades de la tanda 0: igual a la de `9f6361e` con la razón 1,175 y con
  1,498 (sha256 `435af2fe…` en los tres casos). El prototipo de S0-1 la cambiaba en `cap::4.2.1.2` (15.056 y
  11.669 → 2.906, 12.149 y 11.669) y en `ric::11.2::intro` (sin partición → 11.327 y 3.723).
- En los 152 cambian 7 TOs: la regla 8, adfsp, ceninf, cirmo3, manori, nmaeef y ri_niif; la regla 9, rdbcra. Los
  otros 145, iguales byte a byte en sus cinco archivos por TO y en sus entradas de los agregados
  (`censos/condicion_tos_no_tocados.json`). Cobertura exacta en los 152.
- Unidades: 9.533 → 9.555. En los 7 TOs, 179 ids nuevos y 157 que desaparecen, y 133 chunks comunes con otro
  texto (`sha256_completo`), por TO y por regla en `censos/ids_que_cambian_S0-1bis.json`.

## 2. A — Regla 6 en E1

**Diseño.** La partición por ítems de `particionar_por_corte` es la de `9f6361e`. La partición por renglones entra
solo donde hoy no hay salida: (i) en una unidad sin ítems cuyo texto propio pasa la capacidad del tercer escalón,
y (ii) en el ítem, o el chapeau, que deja una parte por ítems sobre esa capacidad; las demás partes quedan como en
la partición por ítems (`_particionar_texto` recibe el umbral desde el que parte por renglones). La capacidad es
40.960 tokens (`MAX_TOKENS_ESCALON_3_R2`, `cliente_e1.py:86`) sobre la razón de la cota de P4: 34.859 caracteres
con la mediana (1,175) y 27.343 con el máximo (1,498). Queda como parámetro (`capacidad_escalon_3_r6`); en S0-2,
como constante que fija T2, junto con el objetivo de las partes (13.091 hoy).

**Clases** (las de S0-1: A no se parte y pasa el reintento con la mediana; B se parte y su parte mayor lo pasa; C en
el borde; D entra con la razón máxima), sobre la misma salida final de E0 y con tres particiones por corte
(`censos/clases_*.json`; 87 unidades sobre 10.937 caracteres):

| Partición por corte | Razón | A | B | C | D | Al tercer escalón | Sin salida |
|---|---|---|---|---|---|---|---|
| `9f6361e` | 1,175 | 15 | 9 | 58 | 5 | 21 | 3 |
| `9f6361e` | 1,498 | 15 | 9 | 58 | 5 | 20 | 4 |
| prototipo de S0-1 | — | 0 | 0 | 80 | 7 | 0 | 0 |
| S0-1 bis | 1,175 | 14 | 8 | 60 | 5 | 22 | 0 |
| S0-1 bis | 1,498 | 14 | 7 | 61 | 5 | 21 | 0 |

- Sin salida con `9f6361e`: `cateloc::S2` (130.099, sin ítems), `ri_niif::S4` (partes de 20.216 y 62.305) y
  `ri_niif::S7` (7.080 y 43.362); con 1,498, también `ri2_cs::S3` (3.128, 28.915 y 2.668). S0-1 bis las parte por
  renglones: `cateloc::S2` en 14 partes (mayor 13.085); de `ri_niif::S4` solo el ítem de 62.305, en 5 (la parte de
  20.216 llega al tercer escalón); de `ri_niif::S7` el de 43.362, en 4; y, con 1,498, de `ri2_cs::S3` el de 28.915,
  en 3. Ninguna unidad queda sin salida con ninguna de las dos razones.
- **Cambia de clase con el parámetro una sola:** `ri2_cs::S3`, B con 1,175 (su parte de 28.915 entra en el tercer
  escalón) y C con 1,498 (`censos/cmp_clases_razon_1.175_vs_1.498.json`). En el borde queda `ri_cc::S3`, cuya parte
  mayor (27.274) cambia con una razón de 1,502 o más.
- Contra el prototipo de S0-1 cambian 25 unidades (`censos/cmp_clases_S0-1_vs_S0-1bis_1.175.json`): 12 de C a A,
  2 de D a A y 8 de C a B, que S0-1 partía por renglones y que ahora llegan al tercer escalón enteras o con su
  partición por ítems (las 22 de A y B, con 1,175), y 3 que siguen en C con la partición por ítems
  (`ri_con::S0`, `ri_dsf::S8::chapeau_seccion` y `snp_tr::1.6::intro`).

## 3. B — Regla 8: lista de puntos leída como cuerpo

**El caso.** Una corrida de rótulos que es una lista y no la estructura: la de una sección («La sección se encuentra
organizada en cinco puntos:» y 1.1 a 1.5, manori p. 3), o una página de índice que E0 lee como cuerpo. E0 abre
nodos con esos rótulos; los rótulos reales de más adelante quedan rechazados, sin padre, o con `::rep2`.

**Diseño.** Antes del parseo, en cada etapa de la escalera y con los roles de esa etapa, `lineas_de_listas_r8` marca
los renglones de las listas; en el parseo son un veto, como la regla 2: un renglón marcado no abre raíz (explícita
ni implícita) ni se acepta como punto, y queda como texto del nodo abierto; un renglón que ya se rechazaba conserva
su motivo. Una lista es una corrida de rótulos de una página con al menos 3 de dos niveles o más, entre los que solo
hay líneas «Sección N.», renglones más a la derecha que el rótulo, de menos de 70 caracteres, que no empiezan en
minúscula (ítems y títulos de la lista) y, a lo sumo, un renglón en minúscula por rótulo (el comentario del prototipo
describe esos renglones como ítems que empiezan en mayúscula o en un número romano: es más estrecho que el código y se
corrige en S0-2); cada número tiene que reaparecer como rótulo en una página posterior, con
el mismo título en al menos el 80 % de los rótulos, a lo sumo el 25 % puede llevar un renglón en minúscula, y entre
las reapariciones tiene que haber, en mediana, más de 3 renglones.

**Censo** (`censos/censo_regla8.json`, 152 TOs y los diez PDFs de la tanda 0): 781 corridas candidatas; 105
descartadas por tener menos de 3 rótulos de dos niveles, 661 porque algún número no reaparece, una por títulos
distintos (ri_pnp p. 6, una enumeración de requisitos), y dos en ri_ccna p. 32, una por renglones en minúscula y una
porque sus números reaparecen en forma de lista (la declaración jurada, repetida como formulario en p. 41). Quedan 12
listas con 150 rótulos en 7 TOs: manori pp. 3 y 57 (listas de sección) y páginas de índice en adfsp p. 3, ceninf
p. 2, cirmo3 pp. 3 y 4, nmaeef pp. 2 (dos corridas), 14 y 36, ri2_ae p. 13 y ri_niif p. 1. Ninguna en la tanda 0. La
regla veta 108 renglones (cirmo3 52, nmaeef 24, manori 10, adfsp 9, ceninf 9, ri_niif 4); los otros 42 ya se
rechazaban y conservan su motivo (nmaeef pp. 14 y 36, 20; ri2_ae, 12; cirmo3, 10), así que ri2_ae no cambia.

**Efecto** (`censos/ids_que_cambian_S0-1bis.json`):

| TO | Chunks | Ids nuevos | Desaparecen | Cambian | Qué pasa |
|---|---|---|---|---|---|
| adfsp | 101 → 93 | 1 | 9 | 0 | los `6.x::rep2` del índice, en `adfsp::S6` |
| ceninf | 47 → 38 | 0 | 9 | 9 | el índice de p. 2 queda en `ceninf::S1::chapeau_seccion` |
| cirmo3 | 308 → 257 | 1 | 52 | 0 | los 52 `7.x::rep2` del índice, en `cirmo3::S7` |
| manori | 66 → 144 | 132 | 54 | 6 | los subpuntos 1.1.x a 3.4.x encuentran padre |
| nmaeef | 47 → 56 | 17 | 8 | 26 | las secciones 1 a 10 del Anexo I salen de `S11::chapeau_seccion` |
| ri_niif | 11 → 7 | 0 | 4 | 1 | los `2.x::rep2` y `3.x::rep2` del índice, en `ri_niif::S1` |

En manori, los formularios de 1.5 y 3.5 quedan dentro de `1.5.1`, `3.5.1` y `3.5.2` con sus tablas serializadas
(467 → 468 tablas serializadas en los 152; manori 15 → 16 de 18). Los rótulos sin padre del censo del punto 7 pasan
de 70 a 12 (manori 58 → 0; `censos/censo_p7_resto_*.json`).

**dmrd p. 6.** Ya lo resuelve la regla 1 de S0-1: «Sección 1 – Ámbito de aplicación» abre la sección y los ítems 1 a
6 quedan en `dmrd::S1` (1.948 caracteres); en `9f6361e` abrían las raíces S1 a S6. No es una lista de puntos (son
de un nivel) y la regla 8 no la toca.

**Límite.** En cinco TOs la lista es una página de índice que los roles leen como cuerpo; la regla la deja como
texto de una unidad: `adfsp::S6` (596 caracteres), `ceninf::S1::chapeau_seccion` (692), `cirmo3::S7` (4.415),
`nmaeef::S0` (1.300) y `ri_niif::S1` (9.500, pp. 1 a 4, texto que antes estaba en `ri_niif::3.2::rep2`). Antes eran
unidades propias, con ids duplicados en adfsp, ceninf, cirmo3 y ri_niif; lo correcto sería el rol de índice
(decisión 2, §7).

## 4. C — Regla 9: filas del catálogo 11.x de rdbcra

**El caso** (`censos/censo_filas_catalogo_*.json`, `find_tables()` sobre el PDF). El catálogo ocupa pp. 36 a 48:
119 filas cuya primera celda es solo un número de punto, con la descripción, la gravedad y las dos multas en las otras
celdas. La descripción está centrada en la fila: empieza renglones antes del renglón del número, que además puede
seguir en minúscula. Antes: 91 filas con unidad y 28 cuyo número E0 rechaza por resto en minúscula; las 97 unidades
terminales 11.x son esas 91 más 6 encabezados de grupo que quedaron terminales porque se rechazaron todas sus filas
(11.4, 11.7, 11.11, 11.18, 11.20 y 11.21; `censos/unidades_11x_antes_y_despues.json`).

**Diseño.** Fila de catálogo: fila de un segmento de tabla de e0_tablas con al menos 3 filas cuya primera celda es
solo un número de punto (primer componente hasta `MAX_RAIZ`). La banda de cada fila es la de `find_tables()`, con
los ajustes de e0_tablas; las tablas se detectan una vez, antes del parseo, y el PDF se vuelve a abrir solo en los
TOs con filas de catálogo. Dos partes:
- **9a, en el parseo:** el renglón que empieza con el número de una fila es rótulo aunque su resto siga en minúscula
  (la celda es la evidencia). Solo levanta los rechazos por resto en minúscula; los vetos de las reglas 2 y 8 siguen
  después. Acepta los 28 números (14 con el aviso `aceptado_fila_de_catalogo_r9`, por columna; los otros 14 pasan por
  la secuencia, una vez aceptada la primera fila del grupo).
- **9b, después del parseo y de las correcciones de continuidad y de fronteras, antes de armar los chunks y del
  acompañamiento T:** cada renglón de la banda que quedó en otra unidad pasa al punto de la fila; los anteriores al
  renglón del número, como `lineas_previas` del nodo, que el texto lleva antes del label. El texto sigue el orden
  del PDF. Mueve 223 renglones, todos anteriores al número, en 117 de las 119 filas.

**Prueba.** Control automático de las 119 filas (`censos/control_filas_catalogo_*.json`: renglones de la banda contra
los del texto de la unidad): antes, 10 limpias, 81 con renglones de otra fila y 28 sin unidad; solo con 9b, 91 limpias
y 28 sin unidad (su texto sigue en los encabezados y en las intros de grupo); con 9a y 9b, 119 limpias. Lectura de
10 filas contra el PDF, con semilla 20261005 (`censos/lectura_filas_r9.json`; recortes en el paquete): 11.1.3,
11.2.8, 11.2.9, 11.5.2, 11.8.3, 11.9.1, 11.12.6, 11.15.8, 11.16.1 y 11.16.2. Las 10 llevan su descripción entera, su
gravedad y sus dos multas, y nada de otra fila. Sale limpio: no hace falta marcar las 97 unidades.

**Efecto.** rdbcra 254 → 261 chunks: 28 ids nuevos (las 28 filas), 21 que desaparecen (los 6 encabezados que eran
terminales y 15 intros de grupo, `11.x::intro`, que eran el comienzo de la descripción de su primera fila) y 91 con
otro texto. Las 97 unidades terminales 11.x pasan a ser las 119 filas. Las tablas del catálogo siguen sin serializar
(cada fila es una unidad); su texto es el de los renglones.

**Otros TOs.** La forma de catálogo aparece en 5 TOs más (`censos/censo_regla9.json`; 191 filas): cedin pp. 19-20,
consyr p. 9 y seggar pp. 17-18, en páginas de tabla de norma de origen (`tabla_norma_origen`), y ri_dsf pp. 26-27 y
snp_tr_nc p. 26, en cuerpo, con sus renglones rechazados por motivos que 9a no levanta (fuera de sección, veto de la
regla 2, padre no abierto). Ninguna parte actúa en ellos y salen byte a byte iguales: el aviso de la regla se escribe
solo si alguna fila queda anclada. En la tanda 0 no hay filas de catálogo: la tabla de códigos NCM de ext p. 167
(«8802.11.00») queda fuera por `MAX_RAIZ`; sin esa guarda, el aviso de una tabla sin filas ancladas cambiaba
`estructura_ext.json` y `conteos.json`.

## 5. Cruces de las reglas 8 y 9 con las reglas 2, 6, 7 y T, y orden

Medidos apagando cada regla, con y sin la regla nueva, sobre los TOs que la regla nueva toca
(`censos/cruces_r8.json`, `censos/cruces_r9.json`):

| | Regla 2 | Regla 6 | Regla 7 | T |
|---|---|---|---|---|
| Regla 8 | actúa en ri_niif (21.526) con y sin la 8; la 8 veta los mismos renglones | parte unidades grandes de manori y nmaeef con y sin la 8 | sin la 8, re-ancla los subpuntos de manori; con la 8, solo `manori::1.5.2` | sin la 8 funde tablas de manori; con la 8 no actúa |
| Regla 9 | actúa en rdbcra (2.3.1) con y sin la 9; la 9 hace lo mismo con y sin la 2 | no actúa en rdbcra | no actúa en rdbcra | no actúa en rdbcra |

Los 108 renglones que veta la regla 8 son los mismos con y sin cada una de las cuatro, y el informe de la regla 9
(119 filas, 223 renglones) también. Orden: la marca de la regla 8 antes del parseo, en cada etapa de la escalera;
en el parseo, 9a levanta el rechazo por resto en minúscula, después vetan la regla 2 y la 8, y después reabre la 7;
tras las correcciones de continuidad y de fronteras, la detección de tablas y su asignación a renglones, 9b ancla
las filas; después T funde y se serializan las tablas; la regla 6 parte al final, sobre los chunks.

## 6. Condiciones de aceptación (salidas en `censos/condiciones_S0-1bis.txt`)

- Tanda 0: 57 de 57 iguales byte a byte a `salida_tanda0_r2b/`.
- TOs que las reglas nuevas no tocan: 145, iguales byte a byte a la corrida final de S0-1 (archivos por TO y
  entradas de los agregados; `version_e0.json` igual).
- `particionar_por_corte`: igual a `9f6361e` en las 2.439 unidades de la tanda 0, con 1,175 y con 1,498.
- Ninguna regla quedó como límite por no cumplirlas. Límites medidos que quedan: las páginas de índice de la regla 8
  (§3) y el borde de `ri_cc::S3` con el parámetro (§2).

## 7. Decisiones de la autora

1. **Regla 9:** 9a y 9b (propuesta: 119 filas limpias; cambia 49 ids de rdbcra) o solo 9b (texto de 91 filas, sin
   ids nuevos; 28 filas siguen sin unidad). El diseño de S0-1 preveía el anclaje sin cambio de ids: limpio no sale.
2. **Páginas de índice leídas como cuerpo** (regla 8 en adfsp, ceninf, cirmo3, nmaeef y ri_niif): dejar su texto en
   una unidad (propuesta para esta release) o darles rol de índice, con su censo, como ampliación de la regla 3.
3. **Regla 6 en E1:** en S0-2 la razón del tercer escalón y el objetivo de las partes salen de T2; con la cota de P4
   cambia `ri2_cs::S3` y está en el borde `ri_cc::S3`.

## 8. Para S0-2

- Las reglas 8 y 9 y la regla 6 en E1 quedan como constantes de e0-r2, sin interruptores; la razón y el objetivo,
  de T2. La detección de tablas pasa a correr antes del parseo (una sola vez, como en el prototipo).
- Tabla de reprocesamiento: las unidades que aparecen o desaparecen por las reglas 8 y 9 se suman a las de S0-1 (si
  F01 las cubre o hace falta una fila nueva se propone en el freno de S0-2). En la tanda 0 no se dispara ninguna.

## 9. Comandos

Desde el scratchpad, con `PYTHONDONTWRITEBYTECODE=1` y el python de `.venv` con `-B`; `<copia>` es la copia con el
prototipo y `S0_REGLAS=r1,r2,r3,r4,r5,r6,r7,r1r7t,r8,r9` (sin `r9`, o sin `r8` ni `r9`, para las intermedias).
```
../s0_1/scripts/lineas_152.py <copia> <caché de líneas>
../s0_1/scripts/correr_152.py --codigo <copia> --salida <dir> [--workers 7] [--tos a,b]
../s0_1/scripts/correr_tanda0.py --codigo <copia> --salida <dir>
../s0_1/scripts/comparar_e0.py <antes> <después> <salida.json> [--tos a,b]
../s0_1/scripts/censo_p7_resto.py <dir> <salida>
scripts/condicion_tos_no_tocados.py <antes> <después> <tos declarados> <salida>
scripts/particion_corte_unidades.py <copia> <dir de la tanda 0> <salida>      (S0_RAZON_E1=1.175 | 1.498)
scripts/censo_clases_tercer_escalon.py --e0 <después> --codigo <copia> --razon-e3 <r> --out <json>
scripts/comparar_clases.py <censo 1> <censo 2> <salida>
scripts/censo_regla8.py <copia> <caché de líneas> <salida>
scripts/censo_regla9.py <copia> <salida> [--workers 7]
scripts/censo_filas_catalogo.py <pdf de rdbcra> <dir> <salida>
scripts/control_filas_catalogo.py <pdf de rdbcra> <caché de rdbcra> <dir> <salida>
scripts/unidades_11x.py <censo de filas> <antes> <después> <salida>
scripts/muestra_filas_r9.py <pdf de rdbcra> <después> <dir de salida>
scripts/cruces_regla_nueva.py <runs> <con todas> <sin la nueva> <prefijo sin X> <prefijo sin X ni la nueva> <tos> <salida>
scripts/ids_que_cambian_bis.py <antes> <intermedia sin r9> <después> <tos> <salida>
scripts/tablas_serializadas.py <dir> [tos]
```
