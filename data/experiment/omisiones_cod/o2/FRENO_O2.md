# U-OMISIONES-COD — FRENO O2 (10/10/2026)

**Entrada.** HEAD `521e220a`. En el log están el registro de O1 (`f318de4`) y las dos notas del 10/10/2026 (`3c5f003` y `521e220`).
El texto firmado da `6c8914a0…` en `c90d3d9`, `3c5f003`, `521e220` y HEAD; leí el mandato en `521e220a`. Los 7 archivos del parche
de O1 eran los de HEAD (sha de `o1/parche/LEEME_parche.txt`), y los otros 5 que toca O2, sin cambios en el árbol. Foto al empezar:
49.173 archivos (salvo `.git`), de 07:56:39 a 07:56:50; 2.213 `.pyc` fuera de `.venv`.

**E0.** No toqué el código de E0 que aplicó S0-5b (`correr_e0.py` `68bd74b5…`, `e0_lib.py` `bd2190ad…`, `selftest_e0.py`
`789630b5…`). Mis copias salen del árbol de trabajo y lo traen, igual en todas. El ensamblado no corre E0: lee
`salida_tanda0_r2b/` (y `salida_tanda0_r2/` en r2a). Una corrida sí pasa por código de E0: `selftest_clave_cache` llama en memoria
a `e0_lib.recortar_herencia` y a `correr_e0.particionar_por_corte` (R26), en las dos baterías, sin escribir salida de E0. Control,
después de todas las corridas: `salida_tanda0_r2b/` (57 archivos) y `salida_tanda0_r2/` (47) de las copias son byte a byte las del
repo (`salidas/e0_tanda0_en_las_copias.txt`).

**Cómo trabajé.** Sobre copias del árbol de trabajo, con rsync, sin `.git`, sin `.venv` y sin enlaces: `c2_head` (el código de
HEAD), `c2_o2` (HEAD + el parche de O1 + O2), `c2_e` (`c2_o2` + la pieza (e)) y `c2_sinJ` (un clon de `c2_o2` con la procedencia
propia apagada, para aislar J). USD 0, sin API. Comandos: `comandos_O2.sh`.

**Línea de base.** HEAD da `40c54830` (diez) y `8d747e57` (sin cola), no `a9631a64` y `e22fae1a`: es R2-3 (`803623a`), sin
re-sellar (+1 propuesto de docvig, 4 `aplica_a` y 1 `padre_sugerido`; `o1/salidas/diff_a9631a64_vs_head_diez.json`). En
desarrollo, HEAD da los sellados (`6e756043`, `2922b72d`). Todos los diffs de abajo van de HEAD a O2, así que son solo de esta
unidad; donde la v7 da una cifra sobre `a9631a64`, la diferencia de R2-3 va aparte.

## El código en el repo

Aplicado a las 08:24:11, sin commit: los 14 archivos de las escrituras autorizadas (§5 y las dos notas del 10/10/2026), byte a
byte los de `c2_o2`. Parches en `parche/` (de HEAD a O2, y lo que O2 agrega sobre O1), con el sha de cada archivo en
`parche/LEEME_parche.txt`.

| archivo | qué |
|---|---|
| `pyd_r2/code/validador_r2.py` | f (la mención con contracciones); H (el tipo desde el código, con la marca) |
| `reextraccion_v2/corpus_v2/r1_e4.py` | f′ (`EXPRESIONES_COLECTIVAS_R3` y la rama del singular, opción ii) |
| `reextraccion_v2/corpus_v2/r1_referencias.py` | J (la procedencia de cada origen) y el agrupamiento sin el rol |
| `tanda0/code/ensamblar_tanda0.py` | A (a–d), C (g, g1, g2, g3), L, G-r, (h), K y la línea que activa J y el agrupamiento |
| `scripts/metricas_intrinsecas.py` | I, junto a M9 en `adaptador_gen3` |
| `med_umbrales/p/code/comun_P.py`, `armador_fichas_P.py` | L: la cuantía de las cuantías del tramo, por el valor |
| `selftest_pyd_r2.py`, `selftest_r3.py`, `selftest_comparador_P.py`; nuevos en `omisiones_cod/`: `selftest_ensamblado_omisiones.py`, `selftest_metrica_condiciones.py` | los selftests, abajo |
| `mantenimiento/tabla_reprocesamiento.md` | anclas de F14b, F15, F15b, F15c, F15d, F16 y F16b, y una nota; ninguna fila nueva |
| `docs/tablero_correcciones.md` | la fila de la observación 10: las tres cifras de (h) |

- **Lo que O2 agrega sobre O1:** `agrupar_sin_rol` en `r1_referencias.py` (los orígenes de una cita se agrupan por `(to, punto,
  chunk)`, sin el rol, también para la procedencia propia de J) y su activación en r2b (`ensamblar_tanda0.py:1729`). El resto son
  selftests, la tabla y el tablero (`parche/parche_O2_sobre_O1.diff`).
- **La tabla:** otra sesión la cambió a las 08:02:39, después de mi foto: corrigió las anclas de E0 que corrió el parche de
  S0-5a-bis y agregó una nota, sin commit. Combiné los dos cambios con `git merge-file`. Hubo un conflicto, en F16 y F16b, y lo
  resolví con mis anclas; en F16b solo cambio la de `ensamblar_tanda0.py`. Con la tabla final, `selftest_clave_cache` da OK y su
  JSON es igual al del repo.
- **H sobre P3b (l):** los dos casos de `selftest_pyd_r2.py` quedan reescritos, con la nota de que H los reemplaza.

## Un selftest por cambio, con positivos y negativos

| cambio | selftest | casos |
|---|---|---|
| A (a, b, c, d) | `selftest_ensamblado_omisiones`: S A (10), R (4) | a ±; b + (2) y − (2); c ±; d ±; casos reales de la v7 |
| e | `pieza_e/selftest_pieza_e.py` (6) | clase 3 y clase 1 +; tres −; la lista sellada, fila por fila |
| f | `selftest_pyd_r2` G17 (7) | contracciones +; mención ausente −; el span; una mención real; el tramo de una entidad no las usa − |
| f′ | `selftest_r3` T13a–d (13) | R3 con rol +; cinco − de forma; opción (ii) ±; la cadena con y sin rol |
| C (g a g3) | `selftest_ensamblado_omisiones`: S C (16), R (16) | los positivos y negativos de la v7, sintéticos y reales |
| L | S L (4), R (2); `selftest_comparador_P` (6 nuevos) | literal +; no verifica → conserva −; tramo compartido; las herramientas del piloto |
| G-r | S G-r (6), R (3) | a la unidad y al ancestro +; ya es la unidad, no se ubica, Comunicacion − |
| agrupamiento sin el rol | `selftest_r3` T13f (3) | la cita va solo al nodo que la nombra +; con el grupo partido por el rol, también al otro − |
| H | `selftest_pyd_r2` G17 (4) y los dos casos de P3b (l) | externas y «A-7000» +; la marca; la del modelo va a campos no definidos; el tramo manda − |
| I | `selftest_metrica_condiciones` (4) | `establecida_en` y `remite_a` no cuentan como contenido; `condicion_de` sí; M9 intacta; 331/1.952 |
| J | `selftest_r3` T13e (3), T13g (1) | dos orígenes, dos procedencias +; sin la opción, la de siempre −; mismas aristas; heredada sin tramo, con la marca |
| K y h | S K y h (2), R (1) | la cita a una unidad excluida + y la de un punto inexistente −; una arista de cada clase |

**La batería, HEAD → O2, sobre las copias** (`salidas/selftests_head/`, `selftests_nuevo/`): `selftest_pyd_r2` 398 → 409,
`selftest_r3` 140 → 160, `selftest_comparador_P` 23 → 29, `selftest_ensamblado_omisiones` 64/64, `selftest_metrica_condiciones`
4/4, todos en verde. Sin cambios: `selftest_e2` 41/41, `selftest_regression_kg` 184/184, `selftest_reresolver_catalogo` 66/66,
`selftest_prompt_r2b` 55/55, `pruebas_t3bis` 17/17 (JSON igual al del repo), `selftest_catalogo_unico` 60/60 (con el `.git` del repo
solo para lectura) y `gate6` (ii) 15 casos, 0 fallas. **Claves de caché:** VEREDICTO OK con los dos códigos, y el JSON es igual al
del repo; ninguna clave de E1 ni de E3 se mueve. **Fichas del lote 1:** byte a byte sobre `e22fae1a` y sobre el sin cola de O2.

## Las cadenas

| cadena | HEAD | O2, dos corridas |
|---|---|---|
| r2a diez / desarrollo | `70d51e42` / `fa4c1043` (`docs/laudo_release_r2_pipeline.md:73`) | los mismos |
| r2b diez | `40c54830` | `710664e9` |
| r2b diez sin cola | `8d747e57` | `a50210b4` |
| r2b desarrollo | `6e756043` | `18a2747d` |
| r2b desarrollo sin cola | `2922b72d` | `9f49d62d` |

Todas con rc=0 y la doble corrida interna byte a byte (`salidas/cadenas_sha256.tsv`). La segunda corrida de las cuatro r2b, en
otro proceso, da los mismos archivos; solo difiere `redirecciones` del reporte, que guarda las rutas de la copia
(`salidas/doble_corrida.json`). Suite y shapes (`salidas/suite_shapes/`): las shapes pasan en los cuatro r2b, sin bloqueantes en
FAIL, y ninguna cambia de resultado; en la suite, 0 ítems empeoran y LN-6 pasa de «persiste» a «resuelto» en los cuatro (como en
O1).

## El diff de los grafos r2b, declarado por campo

`salidas/diff_declarado_<grafo>.json` trae una fila por nodo, arista o elemento que cambia, con sus campos y su causa; 0 sin causa en
los cuatro. Diez (`40c54830` → `710664e9`; 8.817 → 8.813 nodos, 27.633 → 27.557 aristas):

| objeto | cambio | por causa |
|---|---|---|
| nodo | sale / entra | G-r 22 / 22 (el id nuevo, por el punto); salen f 1 y f′ 3 (propuestos) |
| nodo | cambia | G-r 204 (el punto o el rol de la procedencia); H 34; Sujeto: f 1, f′ 1, f y f′ 2 |
| arista | sale / entra | G-r 137 / 67; f′ 22 / 17; f 2 / 1 |
| arista | re-tecleada | G-r 50 (el mismo contenido con el id nuevo de un extremo) |
| arista | cambia | J 9.681; J y G-r 434; G-r 447; f 50; f′ 2 |
| elemento | cambia | C 158; L 620; C y L 2 |

- **Qué toca `kg.json`:** solo f, f′, C, L, G-r (con el agrupamiento sin el rol, que es su consecuencia), H y J. A, D, I y K dan
  0 filas, como pide el §4. C y L no tocan ningún campo fuera de los suyos.
- **J, aislado** (la misma cadena en `c2_sinJ`; `salidas/j_aislado_<grafo>.json`): mismos nodos, mismas aristas, y el mismo
  destino y la misma evidencia en las 13.310 `remite_a`. Cambia la procedencia de 10.139: 9.998 al tramo del propio origen, 97 con
  la marca sin tramo y 44 solo en `provenances`. El registro de remisiones queda igual.
- **La causa de las 10.530 `remite_a` que siguen y cambian de procedencia** entre HEAD y O2, separada con esa corrida
  (`salidas/j_descomposicion_<grafo>.json`): 9.681 solo por J, 434 por J y G-r, y 415 solo por G-r (la procedencia del primer nodo
  de un grupo que tiene un nodo de G-r); 0 sin explicar.
- **Los otros tres grafos**, en el mismo formato, con 0 sin causa: sin cola de diez, −4 nodos y −85 aristas; desarrollo, −3 y −7;
  desarrollo sin cola, −3 y −19.

## `remite_a`: el agrupamiento sin el rol, caso por caso

`salidas/remite_a_caso_por_caso_<grafo>.json` trae cada `remite_a` que cambia, con su clase y el control que la explica; 0 sin
explicar en los cuatro grafos.

- **De O1 a O2**, el agrupamiento solo (los nodos son iguales y fuera de `remite_a` no cambia nada del grafo;
  `salidas/o1_contra_o2.json`):
  - salen las 78 del reagrupamiento (70, 73 y 65 en los otros tres) y no entra ninguna. El control de cada una: en O1 la cita fue a
    todo el grupo partido por el rol («todos_los_nodos_del_punto»); en O2 la misma cita va, con «contiene_la_unidad», a otros nodos
    del mismo punto y chunk, y no a su origen;
  - 30 siguen y pierden una procedencia (26, 30 y 26 en los otros tres): la de una cita que cumple el mismo control. Es el mismo
    mecanismo, en aristas que otra cita sostiene.
- **De HEAD a O2, en diez:** 13.380 → 13.310, −137 y +67, ninguna re-tecleada:
  - 36 salen y 33 entran porque el destino es un nodo de G-r: está anclado en la unidad citada de un lado y no del otro (la regla de
    destinos del detector, `anclados` en `r1_referencias.py`);
  - 25 salen y 34 entran porque el origen es un nodo de G-r: su punto es el de la cita de un lado y no del otro;
  - 76 salen en `ctacte::1.5.3`: G-r pasa la Obligacion e1 de 1.5 a 1.5.3, que nombra la unidad citada, y la cita deja de ir a
    todo el punto y va a ella (4 nodos por 19 destinos).
  - Son las clases de la nota del 10/10/2026 (+145 y −137 con el código de O1), sin las 78: 67 = 145 − 78.
  - Los otros tres: sin cola de diez −133 y +54; desarrollo −39 y +37; desarrollo sin cola −38 y +24, con las mismas clases.
- La lectura de los 18 pares cita–origen queda para la revisión de la mesa, y no bloquea.

## Los registros (`salidas/registros_declarados_<grafo>.json`)

- `omisiones.jsonl`: las mismas filas, en el mismo orden; sin las tres claves de A, byte a byte las de HEAD.
- `remisiones_registro.json`, cita por cita, con 0 sin causa. En diez, 52 cambian por G-r (el grupo gana o pierde un nodo que
  cambia de punto, o G-r corrige el rol de sus nodos) y 57 son re-tecleadas.
- **K reescribe la causa, solo sin la cola.** En el sin cola de diez, 45 irresolubles pasan de `punto_sin_nodos` a
  `destino_en_unidad_excluida`, en 37 citas del registro; en la unidad del reporte (chunk, tramo y unidad citada) son 43 citas, y
  quedan 212 de 255. En desarrollo sin cola son 43, que en el reporte son 41 (quedan 174 de 215).
- `resolucion_sujetos.jsonl` (y por TO), en diez: cambian 486 filas. 51 son de f (la verificación de la mención) y 435 de f′: en
  401 cambia solo la regla del texto (R3), 15 pasan a desacuerdo y 19 cambian de método a R3.
- `no_mapeados_sujetos.jsonl`: 298 → 280; salen 19 (f′), y entra 1 y cambian 14 (f). `adjudicacion_cross_to.json`: sale
  `Sujeto_propuesto_la_entidad` (f′).
- `aristas_derivadas_cola_humana.json` (con la cola): en diez salen 4 y entran 13, todas aristas de G-r del grafo.
- Archivos nuevos: `supuestos_en_norma.jsonl` (A, d) y `procedencia_g_r.json` (G-r). El reporte tiene tres claves nuevas:
  `aristas_por_origen` (h), `procedencia_g_r` y `supuestos_en_norma`.

## Cifras de la v7

| Ítem | v7 (o nota) | O2 | |
|---|---|---|---|
| A, a / b / c / d | 390 / 404 / ≥ 2 / — | 390 (317, 50 y 23) / 404 / 179 / 1.567 en 877 unidades | como en O1 |
| A, e | — | pieza aparte, sin aplicar | la lectura no llegó al piso: límite declarado |
| B, f | 47 pasan | 257 → 210 sin verificar | 17 quedan, como límite |
| B, f′ | 19; 435/401 | R3 1 → 20; 435 filas, 401 solo por la regla del texto | desde HEAD, con f: desacuerdos 430 → 447; propuestos 99 → 95; no mapeados 298 → 280 (R2-3 suma 1 propuesto y 4 filas sobre `a9631a64`) |
| C | 11 / 177 / 76; cambian 160 | iguales; cambian 158 + 2 con L | `salidas/limites_C_O2_diez.json` |
| L | 759 + 2; los 6; 45 | 753 toman el tramo y 6 conservan la cuantía; 45 compartidos; cambian 622; «no» = 1, como en HEAD | fichas del lote 1, byte a byte |
| h | 13.301 / 13.380 / 746 | 13.296 / 13.310 / 746 | R2-3 +1 de extracción; f y f′ −6; G-r y el agrupamiento −70 `remite_a` |
| i | 49 y 20 (ventana real) | 49 y 20, los mismos nodos que en `a9631a64` | definición de la v6: 41 y 22 (43 y 22 en `a9631a64`) |
| G-r | 22 (9/8/4/1); 173 de rol; 0 fusiones | iguales; 194 entidades cambian solo el rol | |
| H | 8 / 26 / 0; desarrollo, 0 sin tratar | iguales; desarrollo 6 / 18 / 0 | |
| I | 331 de 1.952; 18 (8 + 10) | iguales | junto a M9 |
| J | hasta 13.380 | aislado: 10.139 de 13.310 | |
| K | 0; 43 de 255; 41 de 215 | iguales | |

## Las medidas sobre la tanda 0 (`salidas/medidas_tanda0_O2.json`, reportadas y sin sellar)

| | diez | diez sin cola | desarrollo | desarrollo sin cola |
|---|---|---|---|---|
| `kg.json` | `710664e9` | `a50210b4` | `18a2747d` | `9f49d62d` |
| nodos / aristas | 8.813 / 27.557 | 8.500 / 26.045 | 6.987 / 23.438 | 6.720 / 22.065 |
| A: a / b / c / d (entidades) | 390 / 404 / 179 / 1.567 | 337 / 357 / 177 / 1.494 | 287 / 289 / 133 / 1.274 | 242 / 247 / 131 / 1.212 |
| B: desacuerdos; R3 | 447; 20 | 445; 20 | 342; 19 | 340; 19 |
| C: resueltas / marcadas / sin base | 11 / 177 / 76 | 10 / 173 / 71 | 10 / 166 / 58 | 9 / 162 / 55 |
| L: toman el tramo / conservan; compartidos | 753 / 6; 45 | 728 / 6; 45 | 679 / 6; 45 | 657 / 6; 45 |
| G-r: cambia el punto / solo el rol | 22 / 194 | 19 / 182 | 14 / 155 | 13 / 143 |
| H: con la marca; sin tratar | 26; 0 | 25; 0 | 18; 0 | 18; 0 |
| I: Condicion sin arista de contenido | 331 de 1.952 | 322 de 1.868 | 300 de 1.668 | 292 de 1.588 |
| J: `remite_a`; con la marca sin tramo | 13.310; 97 | 12.297; 92 | 12.316; 88 | 11.360; 83 |
| K: citas a unidad excluida / punto sin nodos | 0 / 213 | 43 / 212 | 0 / 175 | 41 / 174 |
| h: extracción / `remite_a` / `establecida_en` derivadas | 13.296 / 13.310 / 746 | 12.884 / 12.297 / 660 | 10.349 / 12.316 / 593 | 10.009 / 11.360 / 516 |
| i: ventana con / sin `remite_a` | 49 / 20 | 44 / 20 | 41 / 12 | 36 / 12 |

K va en la unidad del reporte (citas: chunk, tramo y unidad citada). Ningún nodo ni arista queda fuera del modelo en los cuatro.

## Límites, caso por caso (`limites_O2.md`)

- L: 6 conservan la cuantía, con el mecanismo de la nota del 10/10/2026.
- f: 17 menciones siguen sin verificar (8 «las entidades» y 9 con «la», «los» o «el Directorio»).
- a: 8 omisiones en orden de lectura, sin la marca. d: 10 positivas de T4 sin detectar.
- e: la lectura a ciegas no llegó al piso. (e) queda como límite declarado, y la pieza sigue sin aplicar en `pieza_e/`. El
  resultado está en `omisiones_cod/lectura_e/`, de otra sesión y sin commit. No lo leí: sus cifras no van acá, y para mí ese
  resultado es NO VERIFICADO. En el diseño de T4 quedan 3 copias reales sin detectar y 4 detecciones que T4 no leyó como copia.
- H: 26 con `tipo_no_derivable` en diez (25 sin la cola; 18 en desarrollo, todas de la misma lista).
- C: 177 marcadas y 76 sin base, elemento por elemento. `ext::13.4.6` → `ext::4.4`, que O1 dejó sin leer, está leído: la base es el
  total de deudas elegibles «para los puntos 4.4. y 4.5.» (p. 172). Resuelve al primero de los dos puntos y la base es un monto, no
  la unidad citada: es correcto solo en parte. Ya estaba así en `a9631a64`; queda como límite medido, para el grupo 2.
- i: los 49 y 20 nodos, con sus aristas por dirección, como insumo de U-NAV-DISENO.

Calculados sobre el grafo de O2, `limites_O1.py` da lo mismo que en O1, campo por campo. Ninguno sale de los grupos de la v7, y no
propongo excepciones al §29.

## Errores propios, con su causa

1. **La fila F16b de la tabla.** Al re-anclarla en `c2_o2` tomé el texto de la fila del repo vivo, que ya traía el cambio de las
   08:02:39 de otra sesión, y no el de la copia de HEAD. La copia quedó con esas anclas de E0 sin su nota, y mi nota decía que «no se
   tocaron». Lo vi al aplicar, porque el archivo del repo ya no era el de mi foto: combiné los dos cambios y reescribí la frase.
2. **Dos controles de `remite_a`.** El primer control del destino usaba «la unidad o un descendiente», y no la regla de destinos
   del detector (el mismo `(to, punto)` en alguna procedencia). Dio 49 casos falsos sin explicar en diez. El de O1 → O2 no admitía
   que el mismo texto también fuera una cita heredada, y dio 4. Corregí los dos y quedan 0.
3. **La causa «J» del diff.** `diff_declarado.py` marcaba «J» en toda `remite_a` que sigue y cambia de procedencia. La corrida sin J
   mostró que 415 cambian por G-r, y la causa quedó separada (`diff_final.py`).
4. **Un `.pyc` en el repo.** Corrí `limites_C_O2.py` con `python3 -I`, sin `-B`. Al importar `medir_grupos_C_L` desde
   `o1/scripts/` del repo, escribió `o1/scripts/__pycache__/medir_grupos_C_L.cpython-312.pyc` a las 08:47:59 (2.214 `.pyc`). Lo
   vio el control de `.pyc` de la foto. Quité el archivo y la carpeta, que no estaban en la foto del principio, y el script ahora
   apaga la escritura de bytecode antes del import. `__pycache__/` está en `.gitignore`, y no entró nada al índice.

## Para la autora y la mesa

- (e): la lectura no llegó al piso. (e) queda como límite declarado, y su código, en `pieza_e/`, no se aplica.
  `pieza_e/LEEME_pieza_e.txt`, `limites_O2.md` y la nota de O2 en la tabla de reprocesamiento siguen diciendo la condición
  («entra solo si…»), que no se cumplió; no los toqué.
- La lectura de los 18 pares cita–origen, en la revisión de la mesa.
- `ext::13.4.6`, límite para el grupo 2.
- U3 de U-UNION-ESTRECHA toca `ensamblar_tanda0.py` después de esta unidad: el de O2 está en el árbol de trabajo, sin commit (sha
  `b720df24…`).
- Los cuatro grafos de O2 son lo que da la cadena con el código nuevo; no los sellé.
- No preparo mensaje de commit: lo arma la mesa.

## Cierre

- **Foto sha256 del repo, sin `.git`** (`scripts/foto_repo.py`):
  - antes, 49.173 archivos (07:56:39 a 07:56:50); después, 49.312 (08:58:12 a 08:58:22); ningún archivo quitado;
  - míos: 123 archivos nuevos en `omisiones_cod/o2/`, los dos selftests nuevos de `omisiones_cod/`, y cambian los 12 archivos de
    las escrituras autorizadas;
  - de otras sesiones, por ruta (no los toqué ni los abrí): nuevos, 13 en `omisiones_cod/lectura_e/` (la lectura a ciegas de (e))
    y `conf_matriz/.DS_Store`; cambia `conf_matriz/c2bis/registro_C2bis.md`; y `tabla_reprocesamiento.md`, que es una de mis
    escrituras, trae también el cambio de las 08:02:39;
  - tomé la foto antes de escribir esta sección: después cambia solo este archivo, dentro de `o2/`.
- **`.pyc`**: 2.213 antes y después, con la misma lista (después de quitar el que escribí; error 4).
- **Grep de convenciones**, sobre `o2/` y las 1.157 líneas que agrega el parche completo:
  - nombres de personas, con los tokens de `user.name` y una lista de nombres de pila: vacío;
  - fuentes conversacionales: vacío fuera de los datos; en los cuatro `salidas/diff_declarado_*.json` hay 188 coincidencias de
    «correo», todas en ids de nodos de la norma («correo electrónico» como canal de notificación);
  - rutas con el nombre de usuario: vacío;
  - control positivo: coincide la línea 2 del archivo de control.
- **Después de la C4** (hecha, confirmado por la autora el 10/10/2026): en este archivo cambian las tres menciones de (e) y
  esta línea. No cambia ningún otro archivo del repo.
- **Paquete** `revision_UOMISIONES_COD_O2/` en el scratchpad, con `manifest.txt`. La ruta de la copia permanente y la verificación
  de su manifiesto van en el reporte de cierre, porque este archivo entra al manifiesto.

**FRENO O2.**

---

**[10/10/2026] Nota de la mesa: tres aclaraciones de la revisión del FRENO O2.** El texto de arriba no cambia. La revisión de la mesa
reprodujo este FRENO sobre copias; su evidencia está en el paquete de la mesa (`hoja_de_ruta_tanda1_mesa/revision_O2/`, con
`revision_O2_analisis_remite_a_preguntas_3_4_5_r2b_diez.json`).

1. **Las 76 `remite_a` que salen en `ctacte::1.5.3` las saca G-r**, aunque la sección de `remite_a` las liste aparte de las clases «con
   id de G-r».
   - G-r corre sobre toda entidad cuyo punto no es su unidad (`ensamblar_tanda0.py:1421`, `:1650`). Pasa a 1.5.3 la Obligacion que nombra
     la unidad citada, que en HEAD estaba en `(1.5, herencia_encabezado)`.
   - Con eso, la regla D1 (`r1_referencias.py:1261-1280`) atribuye la cita a ella sola («contiene_la_unidad»). Antes la atribuía a los 4
     nodos de 1.5.3 («todos_los_nodos_del_punto»), cada uno hacia los 19 destinos anclados en la unidad citada: salen 4 × 19 = 76.
   - En `salidas/remite_a_caso_por_caso_r2b_diez.json` esas 76 tienen la clase «sin cambio de id en los extremos», porque ninguno de sus
     extremos cambia de id.
   - Las 19 que entran van de la Obligacion movida, con su id nuevo, a los mismos 19 destinos. Cuentan en la clase «origen con id de
     G-r» (34 entran).
   - Ninguna línea del parche nombra ese documento ni ese punto: es la regla general.
2. **La diferencia de 24 en J es 23 + 1.** J aislado cambia la procedencia de 10.139 `remite_a`, y el diff combinado le da 9.681 + 434
   = 10.115.
   - 23 son `remite_a` que entran en O2 (clase «destino con id de G-r») y cuya procedencia cambia J: no existen en HEAD, así que no
     están entre las que siguen.
   - 1 sigue y no aparece en el diff, porque G-r la cambia y J la deshace (la Operacion de polcre 2.1.7 hacia el TextoOrdenado de
     clasificación de deudores).
   - En los otros grafos: 20 = 19 + 1, 16 = 16 + 0 y 12 = 12 + 0 (`salidas/j_descomposicion_*.json`).
3. **El control del destino redefinido (error propio 2) controla coherencia, no corrección.** Usa la misma definición que el código
   (`anclados`, `r1_referencias.py:1069-1083`, usada en `:1178`): mide que el registro y el grafo digan lo mismo, no que la cita vaya
   al destino correcto. La corrección de G-r sobre `remite_a` la mide la lectura a ciegas de los 74 pares cita–origen (mandato
   U-PARES-REMITE-A, para firmar).
