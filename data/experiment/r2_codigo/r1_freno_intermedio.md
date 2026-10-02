# U-R2-CODIGO — R1, freno intermedio: detección de tablas (R1.a) y propuesta de formato (R1.b)

Fecha: 01/10/2026. Mandato U-R2-CODIGO, firmado (commit del mandato `c60e89c`). USD 0: ninguna
llamada a la API. Este documento sostiene el FRENO intermedio de R1: la serialización (R1.c) no está
implementada y no se implementa hasta que la autora apruebe el formato.

Salidas citadas (todas se reproducen con el comando del encabezado de cada script):
- `r1a_deteccion_tablas.json` (`r1a_deteccion_tablas.py`);
- `r1a_rtc2_candidatas_tanda0.json` (`r1a_rtc2_candidatas_tanda0.py`);
- `r1a_rtc2_fuera_de_muestra.json` (`r1a_rtc2_fuera_de_muestra.py`);
- `r1b_prototipo_formato.json` y `r1b_ejemplos_formato.txt` (`r1b_prototipo_formato.py`).

La salida de E0 versión e0-r2 de la tanda 0 que leen los tres no está en el repo: se genera con
`correr_e0.py --manifiesto <manifiesto tanda0_10tos> --salida <dir> --version-e0 e0-r2` sobre una copia
del código fuera del repo.

## 1. Código escrito en R1.a

- `e0_chunking/e0_lib.py`: `construir_chunks` recibe dos argumentos opcionales (`texto_lineas`,
  `lineas_por_chunk`). En `None`, el camino es el histórico.
- `e0_chunking/correr_e0.py`:
  - `--version-e0 {e0-v1,e0-r2}`, por defecto `e0-v1` (la legada). Con `e0-r2` escribe además
    `tablas_<to>.json` y `version_e0.json`;
  - sección nueva, «tablas en E0, versión e0-r2»: R-TC2, la guarda G-RECUADRO, la asignación
    geométrica y la marca. `e0_tablas` se importa dentro de las funciones y no se edita.
- La sección vive en el driver y no en `e0_lib.py` por `selftest_b583.py:76` (A3, «e0_lib no conoce a
  e0_tablas»), la garantía estructural de B5.8.3. Mi primera versión la tenía en `e0_lib.py` y rompía
  A3; la moví antes de cerrar.
- Control: con la versión legada, la E0 de la tanda 0 se reproduce byte a byte, 34 de 34 archivos contra
  `e0_chunking/salida_tanda0/` (`cmp` archivo por archivo, sobre una copia del código fuera del repo). La
  versión e0-r2 da doble corrida idéntica (45 archivos, `diff -rq`).
- Selftests sobre la copia:
  - `selftest_e0` 57/57, `selftest_b52` 39/39, `selftest_b581` 34/34, `selftest_b582` 59/59,
    `selftest_b583` 33/33 y `selftest_ub53` 40/40;
  - `selftest_manifiesto` da 32/37. Los 5 fallos son P5, paridad del reporte de E2: el
    `reporte_e2_<to>.json` sellado guarda la ruta absoluta de `extracciones`, y en la copia la ruta
    cambia; grafo y censo dan idénticos. Con el código original (`e0_lib.py` sha `ba297f65…`,
    `correr_e0.py` sha `04839ba6…`), sobre la misma copia, da los mismos 5 fallos. No los causa este
    cambio.

## 2. Detección (R1.a)

Reglas, declaradas en el comentario de la sección e0-r2 de `correr_e0.py`:
- **Fuente 1, `e0_tablas`.** `parsear_to` de B5.8.3, sin cambios.
- **Fuente 2, R-TC2 (detección propia).** Una tabla de `find_tables()` que R-TC descarta solo por
  `min_filas` y que cumple todo esto:
  - tiene exactamente 2 filas;
  - pasaría R-TC con 3 filas, es decir, ≥ 2 columnas y fuera de las zonas de banner y de pie;
  - su segunda fila tiene al menos 2 celdas numéricas.
- **Guarda G-RECUADRO.** Una tabla es recuadro de prosa si ≥ 0,75 de sus caracteres no blancos están en
  filas con una sola celda no vacía. Un recuadro no marca el chunk y no se serializa.
- **Asignación geométrica.** Una línea de E0 pertenece a un segmento si está en su página y su `top` cae
  en [y0 − 2, y1 − 2] del bbox.
- **Marca.** El chunk recibe `flags.contenido_tabular = True` y la clave nueva `flags.tablas_e0`.

**Declaración.** Las dos reglas nuevas (R-TC2 y el umbral de G-RECUADRO) las escribí después de mirar
`find_tables()` sobre los diez TOs. Los falsos positivos de abajo son en la muestra. El chequeo fuera de
muestra es informativo.

Resultados (`r1a_deteccion_tablas.json`):

| medida | valor |
|---|---|
| tablas lógicas | 91: 86 de `e0_tablas` y 5 de R-TC2 |
| sin chunk | 12, todas de `e0_tablas`: 9 en páginas `tabla_norma_origen` y 3 banners «B.C.R.A.» de 3 filas en páginas de cuerpo |
| recuadros (G-RECUADRO) | 25: 17 en `cap::4.2.1.2`, 6 en `cap::4.2.1.1`, 1 en `ctacte::13.2`, 1 en `polcre::1.5`; fracción mínima 0,8431 |
| tablas que marcan | 54: 48 parseadas y 1 declarada de `e0_tablas`, y 5 de R-TC2; fracción de recuadro máxima 0,4262 |
| chunks con tabla | 39: 14 que la legada no marcaba y 25 que ya marcaba |
| texto o herencia distintos de la legada | 0 chunks (en R1.a solo cambian las marcas) |

**Los 14 chunks nuevos marcados.**
- 10 por tablas de `e0_tablas`: `cap::1.2`, `cap::6.2.1.1`, `cap::12.1`, `cap::12.2`, `ext::12.1`,
  `ric::S2`, `ric::4.2`, `ric::8.2`, `ric::9.2.1` y `ric::10.2`.
- 4 por R-TC2: `cap::2.12.2.5`, `2.12.2.6`, `2.12.2.8` y `2.12.3.2`.

R-TC2 da 5 detecciones en los diez TOs. Las 5 son cuadros de ponderadores por calificación: los 4 del
mandato y `cap::2.12.2.4`, que E0 ya marcaba. **Falsos positivos: 0 de 5.**

Fuera de muestra (`r1a_rtc2_fuera_de_muestra.json`): R-TC2 corre sobre 145 TOs del corpus escalado, con
`manual` y `ri2_pm` omitidos por tamaño. Da 2 detecciones, las dos tablas reales: `ceninf` p. 4 y
`snp_spd` p. 20. **Falsos positivos: 0 de 2.**

Candidatas de dos filas en los diez TOs (`r1a_rtc2_candidatas_tanda0.json`): 284. Pasan la guarda
numérica 5, las de arriba. Quedan afuera 279:
- 272 banners «B.C.R.A.»;
- 7 más:
  - las tablas de códigos con una fila de datos de `ric` p. 25, 26 y 27 (puntos 5.2.1, 5.2.3 y 5.2.5);
  - las tablas de filas colapsadas de `cap` p. 9 (punto 2.1) y p. 63 (punto 4.1.1);
  - dos recuadros sin cifras de `cap` p. 74 y 80.

**Contradicción con el mandato (regla d de CLAUDE.md §4).** El mandato pide conectar `e0_tablas` a la
marca en 12 chunks. En 3 de ellos lo que `e0_tablas` toma por tabla es prosa dentro de un marco:
- `cap::4.2.1.1`: 6 tablas, todas con fracción 1,0;
- `ctacte::13.2`: fracción 0,8431;
- `polcre::1.5`: fracción 1,0.

Con G-RECUADRO, esos tres no se marcan. Con la versión actual del prompt, marcarlos haría que E1 trate la
prosa como tabla no confiable. Decide la autora (punto B de §4).

**Hallazgo.** La E0 legada perdió líneas de encabezado de tabla en dos chunks:
- `cap::2.12.2.6`: falta la línea «AAA A+ BBB+ BB+»; 0 apariciones en su texto de
  `salida_tanda0/chunks_cap.json`;
- `ric::S2`: faltan «CONSOLIDACIÓN» y «COD CASOS»; están en la página 4 dentro del bbox de la tabla y no
  en las líneas del chunk.

Las celdas del parser los tienen.

## 3. Propuesta de formato (R1.b)

**Bloque.** Cada tabla serializada reemplaza, en el texto del chunk, la corrida contigua de líneas de E0
que caen en su bbox. El bloque va delimitado:
`[TABLA <id> | página <p> | <e0_tablas o R-TC2> | <modo>]` … `[FIN TABLA <id>]`.

**Reglas comunes a los dos modos.**
- Una fila por línea: `Fila k: clave = valor | clave = valor`.
- Las celdas vacías o `None` se omiten. Las filas sin contenido no se escriben.
- Una celda multilínea se escribe en una línea, con los fragmentos unidos por un espacio. No se
  des-silabea.

**Modo «columnas»**, cuando el encabezado es simple:
- la zona de encabezado son las filas anteriores a la primera fila con una celda numérica o de código,
  y tiene de 1 a 4 filas;
- ninguna celda de la zona es `None` (en pdfplumber, `None` es celda combinada);
- ningún encabezado contiene « = ».

Una fila de la zona con la primera celda llena y todas las demás `None` es un rótulo de toda la tabla:
`Rótulo: …`. Las demás filas de la zona se unen por columna en `Columnas: …`. Cada valor lleva el texto
de su encabezado como clave, o `colk` si su columna no tiene encabezado.

**Modo «posicional»**, en cualquier otro caso: todas las filas, también las de encabezado, con clave
`colk`. No atribuye un encabezado combinado a una sola columna. Caso: `cap::6.2.1.1`, donde «Exigencia de
capital por riesgo específico» abarca dos columnas.

**Qué no se serializa.** La tabla queda marcada y el texto de E0 no se toca si se cumple alguna de estas
condiciones:
- `e0_tablas` la declaró;
- R-VERIF da pérdida en algún segmento;
- las líneas de E0 tienen caracteres que no están en las celdas (sería pérdida);
- tiene filas colapsadas, es decir, una celda multilínea toda numérica;
- alguna celda contiene «|»;
- la tabla cae en más de un chunk.

**Verificación prevista para R1.c, sin pérdida en ninguna tabla:**
- (V1) el bloque se relee y reproduce las filas del parser;
- (V2) R-VERIF sin caracteres perdidos;
- (V3) el multiconjunto de las líneas de E0 reemplazadas está contenido en el de las celdas;
- (V4) los chunks sin tabla serializada quedan byte a byte idénticos.

Además, R1.c chequea que las líneas reemplazadas sean contiguas.

**Prototipo** (`r1b_prototipo_formato.json`):

| medida | valor |
|---|---|
| tablas marcadas | 54 |
| serializadas | 51: 27 en modo «columnas» y 24 en modo «posicional» |
| no serializadas | 3: `ric::tabla000` de `ric::S2` y `cap::tabla031` por filas colapsadas; `ric::tabla001`, declarada por `e0_tablas` |
| tamaño | 35.810 caracteres de líneas de E0 pasan a 59.860 de bloques: columnas 18.002 → 28.824; posicional 17.808 → 31.036 |
| chunks con texto propio cambiado | 37 |

Ejemplos completos, antes y después, en `r1b_ejemplos_formato.txt`: `cap::1.2`, `cap::2.12.2.5`,
`ric::9.2.1` y `cap::6.2.1.1`, este último en modo posicional. `cap::1.2` queda así:

```
[TABLA cap::tabla000 | página 4 | e0_tablas | columnas]
Rótulo: -En millones de pesos-
Columnas: Bancos | Restantes entidades (salvo Cajas de Crédito Cooperativas)
Fila 1: Bancos = 5.000 | Restantes entidades (salvo Cajas de Crédito Cooperativas) = 2.500
[FIN TABLA cap::tabla000]
```

**Límites conocidos del formato.**
- En los cuadros con una columna de rótulos de fila (ponderadores, `cap::2.12.4.1`), la primera celda de
  datos se escribe con el encabezado de esa columna: «Calificación = Ponderador de riesgo». Es fiel a la
  grilla del parser, pero se lee raro.
- Un encabezado partido en dos filas que pdfplumber lee como celda combinada de toda la fila sale como
  rótulo. Caso: `ric::tabla009`, que queda con «Rótulo: Partida» y la columna «Código de».
- `ric::tabla023` es la continuación sin encabezado de `ric::tabla022`, que `e0_tablas` no cosió. Sale en
  modo posicional.

## 4. Decisiones que pido a la autora

- **A.** El formato de la §3, tal cual o con alguna de estas variantes:
  - (A1) clave por índice de columna en lugar del texto del encabezado, más compacto;
  - (A2) primera columna como rótulo de fila en los cuadros de ponderadores.
- **B.** G-RECUADRO, sí o no. Con la guarda, `cap::4.2.1.1`, `ctacte::13.2` y `polcre::1.5` no se marcan.
  Sin ella se marcan, como dice literalmente el mandato.
- **C.** R-TC2 tal como está declarada.
- **D.** La tabla serializada en un mini-chunk de introducción también viaja en la herencia de sus
  descendientes. En la tanda 0, el único caso es `ric::11.2::intro`, cuyo único heredero es
  `ric::11.2.3`.

El censo de requests que cambian y su costo (R1.d) se hace después de implementar, armando los requests
sin llamar a la API.
