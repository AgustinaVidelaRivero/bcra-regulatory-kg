# U-R2-CODIGO — FRENO R1: tablas (R1.a a R1.e)

Fecha: 02/10/2026. Mandato U-R2-CODIGO, firmado (`c60e89c`). Decisiones de la autora sobre el freno
intermedio (`r1_freno_intermedio.md`): A, formato aprobado; B, G-RECUADRO aprobada; C, R-TC2 aprobada;
D, herencia aprobada; E, celdas combinadas; F, semántica de la marca. USD 0: ninguna llamada a la API.

Toda cifra sale de un JSON de este directorio; cada script declara su comando en el encabezado. La E0
e0-r2 de la tanda 0 que leen no está en el repo: se genera con
`correr_e0.py --manifiesto <tanda0_10tos.json> --salida <dir> --version-e0 e0-r2`, sobre una copia del
código fuera del repo.

## 1. Código

- `e0_chunking/e0_lib.py`, que no menciona `e0_tablas`, de modo que A3 de `selftest_b583` sigue en verde.
  Dos cambios, inactivos en la versión legada:
  - el gancho opcional de `construir_chunks`;
  - con ese gancho activo, la herencia omite el tramo de un segmento absorbido entero por un bloque.
- `e0_chunking/correr_e0.py`, sección «tablas en E0, versión e0-r2». Contiene:
  - la detección (R-TC2, G-RECUADRO, asignación geométrica);
  - la serialización: formato §3 + E;
  - la geometría de celdas;
  - V1 a V3 y la contigüidad;
  - la marca F;
  - la guarda de sub-chunking.

  Todo detrás de `--version-e0 e0-r2`; la versión por defecto es `e0-v1`.

**Controles.**
- E0 legada de la tanda 0: 34 de 34 archivos idénticos a `salida_tanda0/`.
- e0-r2: doble corrida idéntica, 46 archivos.
- Selftests sobre la copia:
  - en verde: `selftest_e0` 57/57, `b52` 39/39, `b581` 34/34, `b582` 59/59, `b583` 33/33,
    `ub53` 40/40;
  - `selftest_manifiesto` 32/37: los 5 fallos P5 (ruta absoluta en `reporte_e2_<to>.json`) son los mismos
    con el código original (ver `r1_freno_intermedio.md` §1).

## 2. Detección (R1.a) — `r1a_deteccion_tablas.json`, `r1a_rtc2_*.json`

**Cifras.**
- 91 tablas: 86 de `e0_tablas` y 5 de R-TC2.
- 12 sin chunk: 9 en páginas de norma de origen y 3 banners.
- 25 recuadros y 54 tablas que marcan.
- 39 chunks con tabla: 14 nuevos y 25 que la versión legada ya marcaba.

**R-TC2.** 0 falsos positivos de 5 en los diez TOs, medidos sobre la misma muestra con la que se escribió
la regla. Fuera de muestra (145 TOs, sin `manual` ni `ri2_pm`): 2 detecciones, las 2 tablas reales.

**Contradicción con la lista del mandato (decisión B).** El mandato pide marcar 12 chunks; 3 no se marcan
porque todo lo que `e0_tablas` detecta en ellos es recuadro de prosa (`r1c_recuadros_evidencia.json`,
con las celdas completas). Fracción de caracteres en filas de una sola celda:
- `cap::4.2.1.1`: 6 tablas (`cap::tabla003` a `tabla008`), fracción 1,0 en las 6. Son párrafos y
  definiciones de fórmula dentro de marcos: «a) Operaciones sujetas a un acuerdo de n…», «donde: V: valor
  actual de mercado…».
- `ctacte::13.2`: `ctacte::tabla000`, fracción 0,8431. Es la oración del punto 13.2 partida en 7 filas,
  con una sola fila de 5 celdas: «–», «y de las disposiciones de la ARCA…», «–», «, deberán».
- `polcre::1.5`: `polcre::tabla000`, fracción 1,0. Es un párrafo en 3 filas: «…no deberán financiar en
  cuotas las compras de sus clientes…».

Las tablas reales asignadas llegan como mucho a 0,4262.

## 3. Serialización (R1.c) — `r1c_censo_serializacion.json`, `r1c_ejemplos.txt`

**Tablas.**
- Serializadas: 51 de 54 marcadas, 27 en modo columnas y 24 en modo posicional.
- Tamaño de las líneas de E0 reemplazadas → bloques: columnas 18.002 → 28.963 caracteres; posicional
  17.808 → 33.177.
- Sin serializar, marcadas y con el texto de E0 intacto:
  - por filas colapsadas: `ric::tabla000` (`ric::S2`) y `cap::tabla031` (`cap::4.2.1.2`);
  - declarada por `e0_tablas`: `ric::tabla001` (`ric::3.1.4`).
- Por geometría no determinada: 0 tablas.

**Verificaciones.**
- V1 a V3: 0 tablas con falla.
- V4:
  - 2.395 chunks sin tabla, idénticos a la versión legada;
  - los 39 chunks con tabla dan el texto, la herencia y los metadatos legados al reemplazar cada bloque
    por las líneas de E0 de su tabla;
  - los 2 chunks con tabla y sin bloque tienen el texto idéntico.
- Contigüidad: 0 tablas descartadas.

**A (encabezado del bloque).**
- `cap::2.12.2.6` queda en modo columnas, no posicional: su encabezado va en la línea «Columnas:» del
  bloque (ejemplo en `r1c_ejemplos.txt`).
- En modo posicional, 23 de 24 tablas tienen las filas de encabezado dentro del bloque.
- No cumple `ric::tabla023` (`ric::9.2.1`): es la continuación en la página 42 de `ric::tabla022`, sin
  encabezado repetido, y `e0_tablas` no la cosió. Su encabezado («Código | Concepto | Importe») está en el
  bloque de `ric::tabla022`, que la precede en el mismo chunk.

**D (herencia).** El único chunk con bloque heredado es `ric::11.2.3`, que hereda los 4 bloques de
`ric::11.2::intro`.

**E (celdas combinadas).**
- Celdas propagadas: 37, en 6 tablas:

  | tabla | celdas |
  |---|---|
  | `cap::tabla032` | 2 |
  | `cap::tabla035` | 2 |
  | `cap::tabla036` | 12 |
  | `cap::tabla037` | 18 |
  | `ric::tabla015` | 1 |
  | `ric::tabla016` | 2 |

- Celdas combinadas sin propagar: 42. En 22 el origen está en el encabezado (`ric::tabla025`, 028, 029,
  030 y 031); en 20, la celda de origen está vacía (`cap::tabla037`).
- Filas de subtítulo internas, no propagadas: 22, en 11 tablas.
  - En `cap::tabla036`, «Años*» cuenta 2 veces.
  - «Meses*» cae en la zona de encabezado de la tabla y no cuenta como subtítulo interno.
- El marcador «⟨…⟩» no aparece en ningún texto legado ni en ninguna celda de los diez TOs: 0 y 0.

**F (marca).** De los 39 chunks con tabla, 3 quedan con `contenido_tabular_residual` y 36 sin él. Los 3
son `cap::4.2.1.2`, `ric::S2` y `ric::3.1.4`, todos por una tabla marcada sin serializar. En ninguno lo
activa la heurística legada sobre líneas fuera de bloque. Interpretación declarada: el residual heurístico
es la regla legada de E0, con sus umbrales, aplicada a las líneas del chunk que no caen en un bloque.

**Hallazgo: sub-chunking.** Con la serialización, `cap::4.2.1.2` pasa de 26.182 caracteres (el umbral C8
exacto) a 26.626 (`sub_chunking.json` de la salida e0-r2).
- La guarda nueva no lo parte, para no cortar un bloque, y lo declara: `no_particionables`, motivo
  `tabla_serializada`.
- Es una de las tres unidades de `BKL-0030` (R4.b).

## 4. Censo de requests (R1.d) — `r1d_censo_requests.json`

Claves de E1 con el código del perfil `v3_b54`, el de la tanda 0, sin API. Se reutiliza `Armado` de
`mantenimiento/code/selftest_clave_cache.py`.

**Anclaje.** Las 2.434 claves legadas están en la caché de E1 (`immutable=1`). De las e0-r2 están 2.396:
faltan exactamente las 38 que cambian.

| TO | unidades | cambian | texto propio | flags | herencia | costo (USD 0,0166/unidad) |
|---|--:|--:|--:|--:|--:|--:|
| ric | 84 | 21 | 20 | 5 | 1 | 0,3486 |
| cap | 462 | 16 | 16 | 8 | 0 | 0,2656 |
| ext | 973 | 1 | 1 | 1 | 0 | 0,0166 |
| otros 7 TOs | 915 | 0 | 0 | 0 | 0 | 0 |
| **total** | 2.434 | **38** | 37 | 14 | 1 | **0,6308** |

Los motivos se superponen. Combinaciones: 23 solo texto, 13 texto y flags, 1 solo flags (`ric::S2`),
1 texto y herencia (`ric::11.2.3`).

**Declaración.** U-REEXT-T0 re-extrae la tanda 0 completa con el prefijo nuevo de E1 (plan, B2.11,
unidad 11). Este censo mide la parte atribuible a las tablas con el prefijo de la tanda 0, no el tope de
esa unidad.

## 5. Umbrales contra las tablas (R1.e) — `r1e_verificar_umbrales.json`, `verificacion_tablas.py`

Marca sin corregir.

**Control.** `cap::1.2`: las dos Restricciones quedan marcadas en KG-Tanda0-Desarrollo-r1, en
KG-Tanda0-Diez-r1 y en KG-Reextraído-r1.
- La de bancos nombra la columna «Bancos» y trae 2.500, que es de «Restantes entidades»; en su fila, la
  de bancos vale 5.000.
- La de restantes entidades trae 5.000, que es de «Bancos».

No hay otras marcas en ninguno de los tres grafos.

**Veredictos por valor.**

| grafo | nodos evaluados | valores (total) | verificado | en tabla sin veredicto | fuera de tabla | marca |
|---|--:|--:|--:|--:|--:|--:|
| desarrollo | 278 | 375 | 217 | 90 | 66 | 2 |
| diez | 278 | 375 | 217 | 90 | 66 | 2 |
| r1 | 233 | 156 | 66 | 36 | 52 | 2 |

**Declaración sobre la regla.** La regla tuvo cuatro versiones, corregidas después de ver la salida
sobre los mismos grafos. Las dos primeras marcaban 67 y 45 nodos, en su mayoría marcas falsas. La
historia está en el docstring del módulo. La versión vigente marca solo una inversión entre columnas
paralelas de la misma fila con valores de igual forma, y está calibrada sobre estos datos.

**Casos adicionales (pérdidas reales de D2).**
- `ric::7.2`: ningún nodo de contenido en ninguno de los tres grafos, así que no hay nada que verificar.
  Su tabla (`ric::tabla020`, códigos y conceptos) queda serializada en modo columnas.
- `ric::9.2`: ningún nodo marcado. En desarrollo y en diez son 5 Operacion; en r1, 7 Restriccion. Sus
  tablas quedan serializadas:
  - `ric::9.2.1`: `ric::tabla022` en modo columnas y `ric::tabla023` en modo posicional;
  - `ric::9.2.2`: `ric::tabla024` en modo columnas.

**Re-extracción.** La corrección del monto exige re-extraer. En r2a, el test C2 y el de `BKL-0006` siguen
en «persiste».

**Líneas de encabezado perdidas** (`r1e_lineas_perdidas.json`).
- El paso de la E0 legada que las pierde es `separar_encabezado_pie` (`e0_lib.py:502`). En la zona de
  encabezado de página (las primeras 5 líneas), descarta toda línea sin minúsculas (`_es_titulo_mayusculas`,
  `e0_lib.py:495`).
- `cap::2.12.2.6`: pierde «AAA A+ BBB+ BB+» (p. 24, top 116,4). **e0-r2 la recupera**: la tabla se
  serializa y el bloque lleva sus celdas.
- `ric::S2`: pierde «CONSOLIDACIÓN» y «COD CASOS» (p. 4, top 126,3 y 140,2). **e0-r2 no las recupera**:
  la tabla tiene filas colapsadas y no se serializa; quedan solo en `tablas_ric.json`.
- Hallazgo: la regla de encabezado puede perder cualquier línea en mayúsculas al tope de una página, no
  solo de tablas. No lo medí fuera de estos dos casos.
