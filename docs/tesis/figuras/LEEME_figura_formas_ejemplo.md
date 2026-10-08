# figura_formas_ejemplo — registro de generación (versión 2)

Figura «las formas del contenido en el ejemplo» para el análisis del documento
(capítulo 3, sección 3.3): el texto real del punto 5.1.1.1 de Clasificación de
deudores, con el párrafo del 5.1.1 que abre la excepción y el punto 3.7 al que
remite, y debajo del texto las formas del contenido marcadas. Sigue a las
figuras de la página, de la formación del Texto Ordenado, del árbol y de las
unidades de extracción.

- Arriba, **en gris, el párrafo del 5.1.1**: «5.1.1. Cartera comercial.» y
  «Abarca todas las financiaciones comprendidas, con excepción de las
  siguientes:».
- En el medio, **en negro, el texto completo del 5.1.1.1**, en sus cinco
  líneas, con los cortes de línea del documento (el corte «pro-» / «ductiva»
  incluido).
- Abajo, **en gris, el 3.7**: «3.7. Importe de referencia.» y su texto, en sus
  cuatro líneas, **sin marcas**: es solo el destino de la flecha.

Debajo del texto del 5.1.1 y del 5.1.1.1, un subrayado por tramo marcado, en el
color de su forma. Cada tramo tiene su rótulo en la columna del margen derecho,
en el mismo color, unido al subrayado por una línea guía fina. Una flecha
naranja sale de la remisión del 5.1.1.1, baja por la calle izquierda y entra al
bloque del 3.7 a la altura de su título. La figura no lleva títulos, leyenda,
nombres de archivo, rutas, identificadores internos ni nombres de tipo del
esquema.

| Tramo marcado (literal) | Bloque | Nivel | Rótulo | Color del trazo / del rótulo |
|---|---|:-:|---|---|
| «con excepción de las siguientes» | 5.1.1 | 1 | excepción (abierta en el 5.1.1) | `#6d597a` / `#6d597a` |
| «que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7.» | 5.1.1.1 | 1 | condición | `#2a6f97` / `#2a6f97` |
| «dos veces el importe de referencia» (dentro del anterior) | 5.1.1.1 | 2 | umbral | `#b23a48` / `#b23a48` |
| «establecido en el punto 3.7.» (dentro del anterior) | 5.1.1.1 | 2 | remisión | `#e07b39` / `#8a4513` |
| «cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial» | 5.1.1.1 | 1 | condición | `#2a6f97` / `#2a6f97` |
| «se incluirán dentro de la cartera comercial» | 5.1.1.1 | 1 | acto regulado | `#52796f` / `#52796f` |

El rótulo «excepción (abierta en el 5.1.1)» va partido en dos líneas
(«excepción» / «(abierta en el 5.1.1)»): en una línea mide 174,9 unidades a 13
(métricas reales de Helvetica) y la columna de los rótulos tiene 128,4 (de la
unidad 582 al borde derecho menos el margen exigido, 710,4).

**Tamaño efectivo a 15 cm de ancho** (todo el texto, también el transcripto, se
controla contra el mínimo de 7 pt):

| Qué | Lienzo | Impreso |
|---|--:|--:|
| texto transcripto de los tres bloques y rótulos | 13 unidades | **7,68 pt** |

Los 18 textos lo cumplen (11 líneas transcriptas y 7 líneas de rótulo).
**Alto: 7,80 cm** (lienzo 720 × 374,4 unidades; el PDF 425,2 × 221,1 pt; el PNG
1772 × 922 px a 300 dpi). **Margen mínimo a los bordes: 2,19 mm** (superior e
inferior: el borde de 1 de grosor de los bloques grises); izquierdo 2,96 mm (el
tramo vertical de la flecha), derecho 5,26 mm; exigido 2 mm.

Historia (las dos versiones el 01/10/2026, en la unidad F5; ninguna commiteada
al escribir esto):

- Versión 1: además de los seis tramos de esta versión, el 3.7 llevaba marcado
  «que determine la autoridad de aplicación de la Ley 24.467» con el rótulo
  «remisión fuera del BCRA», en dos líneas y en el naranja de la remisión; el
  §8 dejaba abierta una observación sobre «umbral». sha256: generador
  `ab1c3461795763cc9f1c7c94ae38ec700ef929b7b1f0f68f8f821a400363446c`, PNG
  `597750b07c5806e76f7ab3d7b69a16310973e14a9b2e30a8366aff59805947de`, PDF
  `559b63bfccc8e5311052fb04d324bad338a9601f62f133df3a6260c9d5ba3e03`, LEEME
  `32a3acd95a6713f34c8473df1614811c9a524cd8afdc9aa3e8209932a8052bc4`.
- Versión 2 (esta), con los cambios de la revisión de la versión 1: sale la
  marca del 3.7 y su rótulo, y el 3.7 queda en gris como destino de la flecha,
  sin ninguna marca; el script frena si el bloque al que llega la flecha lleva
  marcas (`generar_figura_formas_ejemplo.py:462-465`). La observación del §8
  queda resuelta. Nada más cambia en la figura: el SVG difiere del de la
  versión 1 solo en los cinco elementos quitados (los dos subrayados del 3.7,
  su guía y las dos líneas de su rótulo), y los controles dan las mismas cifras
  de margen, de alto y de distancia mínima entre trazos.

## 1. Cómo regenerar

Desde la raíz del repo (el script también corre desde otro directorio: sus
rutas salen de su propia ubicación):

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_formas_ejemplo.py
```

Escribe `figura_formas_ejemplo.png` y `figura_formas_ejemplo.pdf`. El SVG es
intermedio: va a `rsvg-convert` por la entrada estándar y solo se escribe con
`--svg <ruta>`. Los controles corren siempre (no hay `--verificar`: el script
frena si alguno falla).

Herramientas de la corrida registrada (01/10/2026): `rsvg-convert` 2.62.3
(cairo 1.18.4, pango 1.58.2, harfbuzz 14.3.1), y en el `.venv` del repo (Python
3.10.13) pdfplumber 0.11.10, Pillow 12.3.0 y pypdf 6.10.2. Reutiliza por
importación `generar_figura_norma_a_grafo.py` (sha256
`9b0e45a299a0a078d250ccc999d192cbb83038bd8c00baa6bd8972d021b73f3d`) y
`generar_figura_proceso_extraccion.py` (sha256
`6a91931abeb9927842f76fa50471497e926c69fc56617c62ef7f05ddf6c010d6`), los dos
del commit `fbe69d4`, como las figuras hermanas. Los controles de geometría y de
margen, la lectura de las anclas del artefacto y la exportación son copias de
las funciones de `generar_figura_formacion_to.py` (sin seguimiento en git al
escribir esto) y de `generar_figura_unidad_extraccion.py` (commit `eefaa58`),
como `generar_figura_unidad_extraccion.py` copia las de la primera: solo se
importan los dos módulos de `fbe69d4`.

Desde el 08/10/2026 (§9), el generador importa `generar_figura_norma_a_grafo.py`
en su versión de sha256
`618789ae333e17e0cb7ba1d9baf0d3d006e3f50745869de8bcffd5b487dde67c`, de la que
toma también el medidor, `DPI` y la densidad del PNG, y
`generar_figura_proceso_extraccion.py` en la de sha256
`f4842a6a45b624d7a123da0c423caea1fcc81c1073254d3b1fef63ab1edc5f8c`; la figura
sale idéntica.

## 2. Fuentes

| Fuente | sha256 | Ancla |
|---|---|---|
| PDF del corpus, `data/experiment/subset/TO_clasificacion_deudores_actual.pdf` | `6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2` | fuera de git (`.gitignore:35`); el mismo sha declara el inventario del conjunto de desarrollo, `data/experiment/reextraccion_v2/manifiestos/desarrollo_5tos.json:18-21` (commit `bcb936a`); portada «“A” 8378» y «19/12/2025», comprobada |
| Artefacto de unidades, `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json` (143 unidades) | `98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1` | commit `d082812` (único commit del archivo) |
| Nombres de tipo y de relación del esquema, solo para el control de los rótulos | — | tipos de nodo de r1 (comando abajo) y tipos y predicados del perfil r2, `data/experiment/pyd_r2/generados/enums_r2.json:9-17` y `:20-32` en `eb277ce` (sha256 `abd197ac…`); fijos en `NOMBRES_ESQUEMA` (`generar_figura_formas_ejemplo.py:166`) |

Tipos de nodo de r1 (Obligacion, Operacion, Restriccion, Excepcion, Sujeto,
Comunicacion, TextoOrdenado):

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c "import json,collections; k=json.load(open('data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json')); print(collections.Counter(n.get('type') for n in k['nodes']))"
```

## 3. Qué texto sale de qué fuente

Todo el texto de los bloques es el del artefacto, transcripto tal cual y con sus
saltos de línea (`BLOQUES`, `generar_figura_formas_ejemplo.py:108`). Las líneas
del PDF se cuentan desde 1 en `extract_text_lines` de cada página.

| Bloque | Unidad del artefacto (registro desde) | Pieza | Línea del artefacto | Página y líneas del PDF |
|---|---|---|--:|---|
| 5.1.1 (gris) | `cla::5.1.1.1` (`chunks_cla.json:2677`) | herencia 4: encabezado de 5.1.1 | 2717 | 16, línea 6 |
| 5.1.1 (gris) | `cla::5.1.1.1` | herencia 5: intro de 5.1.1 | 2725 | 16, línea 7 |
| 5.1.1.1 (negro) | `cla::5.1.1.1` | texto | 2686 | 16, líneas 8–12 |
| 3.7 (gris, sin marcas) | `cla::3.7` (`chunks_cla.json:2315`) | texto | 2324 | 14, líneas 21–24 |

El 3.7 sale de su propia unidad del artefacto, `cla::3.7` (`punto_terminal`,
página 14), que existe; no hizo falta tomarlo del PDF. Su herencia (el título de
la sección 3) no se dibuja. El bloque del 5.1.1 tiene que dar exactamente las
dos líneas fijadas en `LINEAS_5_1_1` (`:115`); el texto del 5.1.1.1 y el del 3.7
tienen que empezar con su número y su título.

**Artefacto frente al PDF: sin diferencias.** Cada pieza está tal cual en el
texto de su página (`extract_text`) y cada una de sus líneas es una línea de la
página. Si no fuera así, el script frenaría antes de dibujar, mostrando las
líneas del artefacto, las que no están en la página y las de la página (`freno`,
`:246`, llamado desde `resolver`, `:352`).

Texto propio de la figura: solo los rótulos (`TRAMOS`, `:122`). El script
comprueba que cada rótulo empiece con el nombre de su forma, en minúscula, que
su partición en líneas no cambie el texto y que ninguna de sus palabras sea un
nombre de tipo o de relación del esquema (`NOMBRES_ESQUEMA`, comparación exacta:
«excepción» no es «Excepcion»).

## 4. Tramos: comprobación literal

Regla de la comprobación (`mapa`, `:255`): el texto de cada bloque se lee con
los cortes de línea como espacios y el guion de corte como parte de la palabra
(un «-» al final de una línea que no es la última se quita y la línea se une a
la siguiente sin espacio). Es la normalización R7 de `norm` (`:235`), y el
script comprueba que las dos den lo mismo. Hay un solo corte con guion en los
tres bloques: «pro-» / «ductiva», en las líneas 4 y 5 del 5.1.1.1.

Cada tramo tiene que aparecer **exactamente una vez** en el texto normalizado
de su bloque y **al menos una vez** en el texto normalizado de su página del
PDF; si no, el script frena antes de dibujar. Resultado de la corrida
registrada (caracteres contados desde 0 en el texto normalizado del bloque):

| Rótulo | Bloque | Caracteres | En el bloque | En la página | Segmentos subrayados |
|---|---|--:|:-:|:-:|---|
| excepción (abierta en el 5.1.1) | 5.1.1 | 72–103 | 1 | 1 (pág. 16) | línea 2: «con excepción de las siguientes» |
| condición | 5.1.1.1 | 74–166 | 1 | 1 (pág. 16) | línea 2: «que superen el equivalente a dos veces el importe de»; línea 3: «referencia establecido en el punto 3.7.» |
| umbral | 5.1.1.1 | 103–137 | 1 | 3 (pág. 16) | línea 2: «dos veces el importe de»; línea 3: «referencia» |
| remisión | 5.1.1.1 | 138–166 | 1 | 4 (pág. 16) | línea 3: «establecido en el punto 3.7.» |
| condición | 5.1.1.1 | 169–307 | 1 | 1 (pág. 16) | línea 3: «cuyo repago no se encuentre vinculado»; línea 4 entera, con «pro-»; línea 5: «ductiva o comercial» |
| acto regulado | 5.1.1.1 | 308–351 | 1 | 1 (pág. 16) | línea 5: «se incluirán dentro de la cartera comercial» |

«dos veces el importe de referencia» y «establecido en el punto 3.7.» aparecen
más de una vez en la página 16 porque los repiten los puntos 5.1.1.2, 5.1.2.3 y
5.1.2.4; en el bloque del 5.1.1.1 aparecen una sola vez.

El guion de corte va subrayado con la parte de la palabra que queda en su línea
(«pro-»). Anidamiento: «umbral» y «remisión» caen dentro de la primera
«condición» (caracteres 103–137 y 138–166 dentro de 74–166); ningún otro par de
tramos de un mismo bloque se solapa. El bloque del 3.7, destino de la flecha,
no tiene tramos, y el script lo exige (`:462-465`).

## 5. Candados y controles

El script frena (`SystemExit`) si:

- el sha256 del PDF o del artefacto no es el fijado, o el inventario del
  conjunto de desarrollo no declara ese PDF para cla;
- la portada no dice «“A” 8378» y «19/12/2025»;
- el artefacto repite ids; una línea del artefacto no da el texto de la unidad;
  la herencia de `cla::5.1.1.1` no tiene el encabezado y la intro del 5.1.1
  consecutivos; una pieza no está, según el artefacto, en su página; o el texto
  del 5.1.1.1 o del 3.7 no empieza con su número y su título;
- **FRENO antes de dibujar**: una pieza del artefacto no está tal cual en su
  página del PDF; el bloque del 5.1.1 no son las dos líneas fijadas; un tramo
  no es literal y único en su bloque o no está en su página; un tramo anidado
  no cae dentro del suyo; dos tramos se solapan sin anidarse; o el bloque al
  que llega la flecha lleva marcas;
- un rótulo no empieza con su forma, su partición cambia el texto, su forma no
  tiene color o no está en minúscula, lleva un nombre del esquema, o dos formas
  comparten color;
- la flecha no sale de una remisión o el punto remitido («en el punto 3.7.») no
  es el de otro bloque; o la flecha no llega al bloque remitido o no llega en
  horizontal;
- **transcripción**: lo dibujado, reconstruido por bloque, no es el texto del
  artefacto, o una línea queda fuera de su caja o de su color (gris en el 5.1.1
  y el 3.7, negro en el 5.1.1.1); un rótulo no es el fijado o no va en el color
  de su forma; o algún texto dibujado contiene «extractor», «::», «/», una
  extensión de archivo, «cla» como palabra o «chunk»;
- **geometría** (métricas reales de Helvetica; 18 textos, 3 cajas, 30 marcas:
  los 29 segmentos de los trazos y la punta de la flecha; 0 fallas): un texto
  por debajo de 7 pt impresos, fuera del lienzo, superpuesto a otro, fuera de la
  caja que lo contiene, cortado por el borde de otra caja o tocado por una
  marca. Holgura mínima de una línea transcripta al borde derecho de su bloque:
  13,1 unidades (la segunda línea del 3.7, 502,9 de ancho);
- **trazos** (29 segmentos: 10 de subrayados, 15 de guías y 4 de la flecha):
  dos segmentos de tramos distintos a menos de 2,5 unidades entre sus ejes
  (`DISTANCIA_MIN`, `:212`; la flecha cuenta como trazo de la remisión).
  Mínimo de la corrida registrada: 3,60 unidades, entre el subrayado de
  «umbral» en la línea 3 y el tramo horizontal de la flecha que corre debajo;
- **margen** (38 elementos: los 18 textos y 20 dibujados leídos del SVG, 3
  rectángulos y 17 trazos, con medio grosor de trazo y la punta de la flecha):
  un elemento a menos de 2 mm (`MARGEN_MM`; 9,6 unidades de lienzo) de uno de
  los cuatro bordes. Es el control de `generar_figura_formacion_to.py:840-852`.
  Mínimos de la corrida registrada: izquierdo 14,2 unidades (2,96 mm),
  superior 10,5 (2,19 mm), derecho 25,3 (5,26 mm) e inferior 10,5 (2,19 mm).

**Pruebas negativas** de la versión 2, fuera del repo, sobre una copia espejo en
el scratchpad de la sesión, con la alteración hecha en memoria y sin exportar:
sin cambios, 0 fallas; con «dos veces el importe referencia» como tramo, FRENO
(0 apariciones); con «pro- ductiva» en lugar de «productiva», FRENO; con
«viviendas» en lugar de «vivienda» en el artefacto, FRENO con la diferencia
contra la página 16; con «umbral» declarado dentro de la otra condición, FRENO;
con «umbral» sin declarar anidado, FRENO por solape; con «Excepcion» en un
rótulo, frena; con el rótulo partido como «excepción» / «(abierta en el», frena;
con «cla::5.1.1.1» en un rótulo, frena por texto prohibido; **con la marca de
la versión 1 devuelta al 3.7, FRENO («el bloque 3.7, destino de la flecha,
lleva marcas»)**; con el segundo nivel de subrayado a 6,8 en lugar de 9,6, 11
fallas de trazos; con interlínea 18, 8 fallas de geometría; con la calle de la
flecha en x = 6, 1 falla de margen.

Verificación adicional con `docs/tesis/figuras/verificar_geometria_svg.py` sobre
el SVG guardado con `--svg`: 18 textos, 0 nodos, 1 trazo con flecha, 0 fallas.

## 6. Composición

Lienzo de 720 unidades para 15 cm, con 11 unidades (2,29 mm) de margen. Calle
izquierda para la flecha (su tramo vertical en x = 15). Bloques de la unidad 32
a la 555 (523 unidades, 10,90 cm), con 7 unidades de aire a los lados y 6
arriba; 19 unidades de la última línea de base al borde inferior, donde caben el
subrayado y el carril de la última línea. Interlínea de 27 unidades (`IL`,
`:202`), la misma en los tres bloques, que deja lugar, debajo de cada línea de
base, a dos niveles de subrayado (a 5,2 y 9,6 unidades, `DY_NIVEL`, `:207`) y a
un carril para guías (a 13,2, `DY_CARRIL`, `:208`). Entre el bloque del 5.1.1 y
el del 5.1.1.1, 9 unidades; antes del 3.7, 22.

- **Niveles**: el tramo que contiene a otros va en el nivel 1, pegado al texto;
  los anidados («umbral» y «remisión», dentro de la primera «condición»), en el
  nivel 2, más abajo. El nivel es la profundidad de anidamiento.
- **Guías**: cada guía sale del final del primer segmento del tramo que llega al
  final de su línea y sigue en horizontal, a la altura del subrayado (las dos
  «condición» y «umbral»); si ningún segmento llega al final de la línea, baja
  desde el final del tramo al carril de esa línea y sigue por él («excepción»,
  «remisión» y «acto regulado»). En x = 560 dobla hacia su rótulo. Subrayados de
  1,5 de grosor; guías de 0,8.
- **Rótulos**: en la columna que empieza en la unidad 582, en el orden de sus
  guías, cada uno lo más cerca posible de la altura de su guía; los que chocan
  se agrupan y el grupo se centra en el promedio de sus desplazamientos
  (`repartir`, `:516`). Corrida registrada: «condición» de 130,5 a 123,1,
  «umbral» de 134,9 a 139,1, la segunda «condición» de 157,5 a 155,1 y
  «remisión» de 165,5 a 171,1; «excepción» y «acto regulado» quedan a la altura
  de su guía.
- **Flecha** (1,6 de grosor, con punta): baja del comienzo del subrayado de la
  remisión (100,4; 161,9) al carril de la línea 3, corre a la izquierda hasta la
  calle, baja y entra en horizontal al bloque del 3.7, a la altura del centro de
  su primera línea (y = 259,8), con la punta sobre el borde del bloque.

Colores: bloques como en la figura de las unidades de extracción (grises con
fondo `#f4f6f8`, borde `#999999` y texto `#555555`; el negro con fondo blanco,
borde `#4a5a6a` de 1,3 y texto `#1f1f1f`). Formas, con tonos de la paleta
compartida (`generar_figura_norma_a_grafo.py:81-90`): excepción `#6d597a`,
condición `#2a6f97`, umbral `#b23a48`, acto regulado `#52796f` y remisión el
naranja `#e07b39` de las remisiones de las figuras del ejemplo
(`generar_figura_norma_a_grafo.py:89`), con el rótulo en el mismo tono
oscurecido, `#8a4513` (`:90`), porque el naranja sobre blanco se lee mal; la
flecha lleva el mismo naranja. La figura no depende solo del color: cada tramo
tiene su rótulo y su guía, y los anidados, su propio nivel.

## 7. Salidas y reproducibilidad

| Archivo | sha256 |
|---|---|
| `generar_figura_formas_ejemplo.py` | `ff0d85445baadc2f3b05c34825e3be39b1adce1dec740dcdc5d33561ec4c9fb8` (hasta el 08/10/2026, `93d30c363fb11afdbd5ac62433240abc0d1d231911ec474f9f7f899e6ebeb118`; §9) |
| `figura_formas_ejemplo.png` (1772 × 922 px, 300 dpi) | `ac29612bfa727f7f48b7d207c9b4826201eca4b875aa4476f7793b89e363a570` |
| `figura_formas_ejemplo.pdf` (425,2 × 221,1 pt) | `fa83fd3a15e2617f9a32e9adddb6f7a95358a021156d1bb2db5947bac664fabf` |
| SVG intermedio (no se versiona) | `186321be52f48d510b016bfe0cde198e37fdd4981181fc2ecb5565837a107f09` |

Tres corridas de la versión 2: la que escribió las salidas del repo, con
`PYTHONHASHSEED` 0, y dos de verificación sobre una copia idéntica del
generador en el scratchpad de la sesión (con el directorio de datos del repo
enlazado, solo para leer), con `PYTHONHASHSEED` 1 y 0, en el mismo segundo y un
segundo después. El SVG, el PNG y el PDF salieron idénticos byte a byte en las
tres, y la salida de consola también (salvo la ruta del SVG, distinta a
propósito). El PDF es reproducible porque el script fija `SOURCE_DATE_EPOCH=0`
al llamar a `rsvg-convert`, como las figuras hermanas: `/CreationDate`
01/01/1970. Stream de contenido de la página del PDF, sha256
`b9b3f5d24a945a0e708df003dce3b77a2b90cb17ddee3b917738996f8a1d8083`.

Este LEEME cae bajo `.gitignore:180` (`docs/tesis/figuras/*`), sin excepción que
lo libere (`git check-ignore -v --no-index` lo atribuye a esa línea), así que
entra a git solo forzado, con `git add -f`. El generador, el PNG y el PDF entran
por las excepciones `.gitignore:208`, `:186` y `:188`.

## 8. El umbral

Resuelto en la revisión de la versión 1: el umbral no es una forma de la tabla
de formas de la sección 3.3, sino una parte de la primera condición, y el
epígrafe de la figura en la tesis lo dice. La figura lo dibuja así: «dos veces
el importe de referencia» va subrayado en el segundo nivel, dentro de la
condición «que superen el equivalente a dos veces el importe de referencia
establecido en el punto 3.7.», con el rótulo «umbral». El texto del epígrafe,
contra su fuente en Overleaf, NO VERIFICADO.

## 9. Nota del 08/10/2026: el medidor, `DPI` y la densidad, de `generar_figura_norma_a_grafo.py`

Un cambio en el generador, ninguno en la figura:

- **Qué fallaba.** Desde `88bfe89`, `generar_figura_proceso_extraccion.py` ya no
  tiene `DPI`, `grabar_densidad` ni `medidor`. El generador fallaba al
  importarse, con `AttributeError` en `DPI = proc.DPI` (:178), antes de llegar a
  la llamada `proc.medidor()` (:870): no corría en HEAD.
- **Qué cambió.** Los tres salen ahora de `generar_figura_norma_a_grafo.py`
  (sha256 `618789ae…`), que el generador ya importaba como `base`: `base.DPI`
  (:178; vale 300, como antes), `base.grabar_densidad` (:824; la función de
  :1049 de ese archivo, igual a la que tenía
  `generar_figura_proceso_extraccion.py` en `fbe69d4`) y `base.medidor()` (:870;
  la función de :806). El docstring (:52-56) dice de dónde sale cada cosa, y el
  comentario de `MEDIR` (:477), `base.medidor`. De
  `generar_figura_proceso_extraccion.py` (sha256 `f4842a6a…`) sigue tomando `W`,
  `ANCHO_TEXTO_CM` y `PT_POR_CM`, con los mismos valores que en `fbe69d4`.
- **El medidor.** `base.medidor()` difiere del de `fbe69d4` en dos cosas: si
  faltan PIL o la fuente del sistema, frena en lugar de devolver `None`, así que
  el `SystemExit` propio de :871-872 ya no se alcanza; y carga la fuente a
  `int(round(fs * 10))` en lugar de `fs * 10`. Ninguna de las dos cambia esta
  figura.

El script tiene las mismas líneas (923) y su sha256 pasó de `93d30c36…` a
`ff0d8544…` (§7). Sobre una copia del repo, con `PYTHONHASHSEED` 0, 1 y 4242, el
PNG y el PDF salen idénticos byte a byte a los commiteados, y el SVG intermedio
da el sha256 de §7; registros en el paquete de revisión de FIX-MEDIDOR-8.
