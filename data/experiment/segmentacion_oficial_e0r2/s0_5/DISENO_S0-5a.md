# U-SEG-OFICIAL — S0-5a: diseño aplicado de las reglas de corte de E0 (09/10/2026)

Mandato: `docs/mandatos/USEG_OFICIAL_S0-5a_reglas_de_corte_E0.md`, leído en `b60e2fc9` (sha256 del texto en ese commit
`4f4ca6c9…`), con su nota al pie del 09/10/2026 (control de continuidad de la numeración). USD 0, sin API. El código de
E0 se cambió solo en una copia del repo; el parche (`parche/`) se aplica en S0-5b. Las cifras que siguen se reproducen
con los comandos de `REPORTE_S0-5a.md`, §9.

## 1. Dónde corre

- **Copia completa del repo, sin enlaces simbólicos** (CLAUDE.md §4.l), en el scratchpad de la sesión; las bases de
  caché de E1 y E3 y las salidas de la tanda 0 que leen los selftests, copiadas también.
- **Código de partida**: el de S0-4b, igual al del repo (`e0_lib.py` `65a8c3b8…`, `correr_e0.py` `94d35349…`,
  `selftest_e0.py` `ec186071…`).
- **Código final** (el del parche): `e0_lib.py` `4d0abc1a…`, `correr_e0.py` `ed276d43…`, `selftest_e0.py` `9f2fbf28…`.
- **Prototipo con interruptor** para el censo por regla: el código final más 15 renglones en `correr_e0.py`
  (`parche/interruptor_prototipo_S0-5a.diff`): la variable `S0_5_REGLAS` deja prendidas solo las reglas que nombra
  (`NINGUNA`, `TODAS`, o una). No va al repo.
- **Corridas**: los 152 con `s0_1/scripts/correr_152.py` (9 procesos, una raíz mínima por configuración) y la tanda 0
  con `s0_1/scripts/correr_tanda0.py` (secuencial), sobre la copia.

## 2. Las seis reglas, como quedaron

Cada una detrás de un parámetro de `e0_lib` apagado por default, y prendida en `correr_e0.py` solo con e0-r2, fuera de
los diez TOs de la tanda 0 (`TOS_TANDA0_SIN_S0_5`) y, las que van por lista, solo en su lista.

| regla | parámetro (e0_lib) | alcance en correr_e0 |
|---|---|---|
| R5-a cierre al margen | `aplicar_cierre_al_margen(cierre=True)` | las listas de `listas_116` en los 142 TOs fuera de la tanda 0 |
| R5-a′ título de bloque | `aplicar_cierre_al_margen(titulo_bloque=True)` | ri_oc (`TOS_TITULO_BLOQUE_S0_5`) |
| R5-b intersticial continuada | `construir_chunks(intersticial_continuado=True)` | snp_dd y snp_cheq |
| R5-c título de sección envuelto | `construir_chunks(titulo_seccion_envuelto=True)` | los 142 |
| R5-d número en referencia | `parsear_cuerpo(numero_en_referencia=True)` | los 142 |
| R5-e rótulo vertical | `juntar_rotulo_vertical(res)` | ri_ccna |

### R5-a

- **Listas**: `listas_116`, el detector del §2.6 sobre el árbol de E0 (unión del de S1-bis y su corrección (i)); lo
  reproduce `scripts/detector_116.py` sobre la salida (121 / 316 / 317 sobre S0-4b, las cifras del mandato).
- **Párrafos**: los del detector corregido (el renglón del rótulo es un párrafo propio; un renglón con mayúscula
  inicial abre párrafo después de uno que termina en «.» o «:», y el segundo renglón del ítem abre párrafo si empieza
  con mayúscula). Se evalúa cada párrafo desde el segundo.
- **Columnas** (de las `Linea` de E0, que vienen de `extraer_lineas`): la de los rótulos es la mediana del `label_x0` de
  los ítems de la lista; la del texto, la mediana del `text_col` de los ítems **anteriores al último**, porque el del
  último puede ser la del propio cierre (cajasc 11.4.4). Un párrafo pasa al cierre del padre si está a más de la
  tolerancia de la columna del texto y más cerca de la de los rótulos. Si ningún ítem anterior tiene texto, pasa el
  párrafo que no corre más adentro que los rótulos más la tolerancia (ri_oc B.2.4 y B.3.4).
- **Tolerancia de columna: `TOL_COL_R5A = TOL_X` = 3,0 pt**, la de las columnas de E0, fijada en el código antes de
  correr el censo, una sola para los 152, y no ajustada después.
- **Destino**: los renglones salen del ítem y entran a los segmentos del padre, ordenados por posición; como están
  después del rótulo del último hijo, su rol es `cierre` (`<padre>::cierre`, o `S<n>::cierre` si el padre es una
  sección). `construir_chunks` hereda el cierre de cada ancestro: **todos los descendientes del padre heredan lo que
  R5-a mueve** (por eso `gerc::2.4.2`, un encabezado de verdad de R5-d, cambia su herencia: hereda el cierre nuevo
  `gerc::2.4::cierre`; su texto y su título no cambian).

### R5-a′

- Por lista, ri_oc. Se evalúa antes que R5-a: lo que abre la sección nueva ya no pasa por R5-a.
- El primer párrafo del último ítem, desde el segundo, que empieza con un renglón con forma de título de bloque
  (`_es_titulo_bloque`: 60 caracteres o menos, mayúscula inicial, sin «.», «,», «;» ni «:» al final, sin número de
  punto, sin huecos de columna) y al que sigue más texto abre una **sección sintética nueva, después de la del padre**,
  con ese renglón como rótulo, el resto del ítem y el cierre que el padre tenía. Llega hasta el encabezado siguiente
  de igual o mayor nivel, porque es una sección de primer nivel.
- **Clave**: `<to>::Sbloque<k>` (k-ésimo bloque del TO): `ri_oc::Sbloque1`. Es la convención de las secciones de E0
  (`S<numero>`) con el número `bloque1`; **la propongo para la revisión**, porque el mandato no fija el número.

### R5-b, R5-c, R5-d, R5-e

- **R5-b**: dos intersticiales consecutivas del mismo hueco y de la misma página se unen con (i), (i′) o (ii) del
  mandato; las uniones se encadenan; la unidad unida conserva el número de la primera, y las siguientes no se
  renumeran.
- **R5-c**: el chapeau de un solo renglón de una sección cuyo título no termina en «.», «:» ni «;» se junta al título
  con (a) a (d) del mandato, en un renglón aparte del encabezado (como en el PDF), y la sección queda sin chapeau.
- **R5-d**: veto de encabezado. El renglón anterior termina en una palabra de referencia del mandato (sin «y» ni «o»);
  el renglón no tiene huecos de columna, empieza en la columna del renglón anterior (la del cuerpo del texto, con
  `TOL_X`) y no en la de los rótulos de sus hermanos (el `label_x0` del último hermano abierto; sin hermanos, la
  columna de los hijos del padre). Sigue como prosa.
- **R5-e**: los renglones de una sola letra mayúscula en la misma columna, uno debajo del otro (3 o más, a 15 pt o
  menos), se juntan en un renglón con la palabra, en el lugar de la última letra y en la unidad que la tiene; las otras
  letras salen de sus unidades y `lineas_contenido` baja en las que salen (la cobertura sigue exacta).

## 3. Lo que cambió respecto del mandato, y por qué

1. **R5-a no recorre las listas de secciones de la corrección (ii) del detector** (secciones sin puntos consecutivas
   cuyo texto empieza con «N.»): esas secciones no tienen un nodo padre común, y no hay un `<padre>::cierre` al que
   mover el párrafo. `listas_116` toma solo las listas de puntos; el detector de S1-ter (`scripts/detector_116.py`) sí
   las cuenta (20 de las 277 sobre la salida final).
2. **R5-a′ solo cuando el padre es una sección de primer nivel** (el caso de ri_oc). Con un padre punto, la regla no
   dice adónde va el bloque; los candidatos de ese tipo quedan listados para la decisión de la autora (§4 del FRENO).
3. **R5-d como veto en el momento de aceptar el encabezado.** La primera versión cambiaba el motivo de rechazo de
   renglones que E0 ya rechazaba por otro motivo, sin cambiar ninguna unidad: ruido en `estructura_<to>.json` sin
   efecto en los chunks (cuántos, NO VERIFICADO: la salida de esa versión se descartó al rehacer la regla). Ahora corre
   solo cuando el renglón iba a aceptarse, y también en la rama de la raíz implícita. Detuve el lote de
   configuraciones y lo volví a correr con esta versión.
4. **R5-e sobre el árbol, no antes del parseo.** La primera versión juntaba las letras antes de `parsear_cuerpo`: una
   letra suelta al principio de la página cambiaba la zona del encabezado y E0 descartaba el membrete del formulario
   siguiente. Sobre el árbol, la lectura de la página no cambia.
5. **Los cuatro casos medidos de `selftest_e0` que esperaban la salida de S0-4** (ri_spi 92 unidades, ri_ccna 159 y la
   lista B con 47, ri_oc 187 y la herencia de B.1.1) se actualizaron con la razón en cada caso: R5-c quita cinco
   chapeaux en ri_ccna, y R5-a abre el cierre de B.1 en ri_oc.
6. **El número de pares (ii) de R5-b.** El mandato dice 19 pares de rótulo y descripción, 15 en snp_dd; el censo de la
   mesa que cita (`S0-5_evidencia_r5b_pares_salida.txt`) lista 14 en snp_dd y 4 en snp_cheq, 18. Mi salida une
   exactamente los pares de ese censo, más 7+8 por (i′): 17 en snp_dd y 4 en snp_cheq.
7. **Los 27 candidatos de R5-a′** no se reproducen: la heurística de la mesa no está versionada. Con el criterio de la
   regla (`scripts/candidatos_r5a2_S0-5a.py`: el primer renglón con forma de título desde el segundo párrafo del último
   ítem de las listas del detector) son 24; con el renglón que abre un párrafo, 17 de ellos; con cualquier renglón
   después del primero, 26.

## 4. Lo que el diseño no resuelve (va al FRENO)

- **El alcance de R5-a.** El mandato lo fija en las listas del detector corregido, con la evidencia de la mesa en los
  35 candidatos de la tanda 1. En los 152, R5-a mueve 186 párrafos (997 renglones) en 57 listas de 38 TOs; los 9 casos
  del mecanismo 1 y los 27 correctos cumplen la aceptación, y de las otras 48 leo, a la vista del texto de la salida,
  29 con forma de cierre, 13 que no son cierre y 6 dudosas (`censos/lectura_r5a_S0-5a.md`). Las 13 son formularios y
  modelos de nota, el cuerpo de un ítem con una columna de texto atípica (cirmo3 1.2.11.3 y 1.2.23.3, gerc 2.4.3), y
  bloques con título propio u otra parte del documento: el mismo mecanismo que R5-a′, que fuera de ri_oc no se aplica y
  deja el bloque en manos de R5-a. Como lo que R5-a mueve lo heredan todos los descendientes del padre, un falso
  positivo se repite en cada hermano.
- **El detector de S1-ter no ve los falsos positivos de R5-a**: 42 de las 57 listas dejan de ser candidatas en la salida
  final (el último ítem ya no tiene el párrafo de más), y no entran a la población del 1.16 de S1-ter.
- **La tanda 0**, fuera por lista: sin la exclusión, solo R5-a la cambiaría (15 cierres nuevos en 7 TOs y 63 unidades
  cambiadas; `censos/limites_S0-5a.json`).
