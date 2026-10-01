# figura_unidad_extraccion — registro de generación (versión 5)

Figura «las unidades del ejemplo» para el análisis del documento (capítulo 3,
sección 3.2): dos unidades de Clasificación de deudores, una debajo de la otra,
tal como las arma el artefacto de unidades con el que se construyó el grafo r1.

- Arriba, **«Unidad de extracción del punto 5.1.1.1»**: en gris, la herencia
  del punto terminal en tres bloques (el título de la sección; el título y el
  párrafo sin numerar del 5.1; el título y el párrafo sin numerar del 5.1.1); en
  negro, el texto completo del 5.1.1.1. Al margen, un rótulo por bloque y una
  llave que agrupa los tres bloques grises bajo «cadena estructural».
- Abajo, **«Unidad de extracción del párrafo del 5.1.1»**: en gris, los títulos
  de la sección 5, del 5.1 y del 5.1.1; en negro, solo el párrafo «Abarca todas
  las financiaciones comprendidas, con excepción de las siguientes:». Al
  margen, un rótulo por bloque y una llave que agrupa los tres títulos grises
  bajo «títulos que ubican el párrafo».
- Debajo de cada unidad, su lugar: «Lugar: Clasificación de deudores, punto
  5.1.1.1» y «Lugar: Clasificación de deudores, punto 5.1.1».

Regla de la figura: **gris es la herencia y negro es el texto**, tal como el
modelo recibe cada unidad (sección 8). La figura no muestra nada de la salida de
la extracción, ningún tipo de entidad o de relación ni nombres de nodos, y no
lleva nombres de archivo, rutas ni identificadores internos.

| Unidad | Bloque | Color | Rótulo al margen |
|---|---|---|---|
| 5.1.1.1 | «Sección 5. Categorías de carteras.» | gris | título de la sección |
| 5.1.1.1 | «5.1. Categorías.» + «La cartera se agrupará en dos categorías básicas:» | gris | texto del 5.1 |
| 5.1.1.1 | «5.1.1. Cartera comercial.» + «Abarca todas las financiaciones …» | gris | texto del 5.1.1 |
| 5.1.1.1 | los tres bloques grises | — | llave: cadena estructural |
| 5.1.1.1 | el punto 5.1.1.1 completo, en sus 5 líneas | negro | texto del 5.1.1.1 |
| 5.1.1 | «Sección 5. Categorías de carteras.» | gris | título de la sección |
| 5.1.1 | «5.1. Categorías.» | gris | título del 5.1 |
| 5.1.1 | «5.1.1. Cartera comercial.» | gris | título del 5.1.1 |
| 5.1.1 | los tres títulos grises | — | llave: títulos que ubican el párrafo |
| 5.1.1 | «Abarca todas las financiaciones comprendidas, con excepción de las siguientes:» | negro | párrafo sin numerar del 5.1.1 |

**Tamaño efectivo a 15 cm de ancho** (todo el texto, también el transcripto, se
controla contra el mínimo de 7 pt):

| Qué | Lienzo | Impreso |
|---|--:|--:|
| títulos de las dos unidades (negrita) | 14 unidades | **8,27 pt** |
| texto transcripto, rótulos, rótulos de las llaves y lugar | 13 unidades | **7,68 pt** |

Los 31 textos lo cumplen (2 a 14 unidades y 29 a 13). **Alto: 9,12 cm** (lienzo
720 × 438,0 unidades; el PDF 425,2 × 258,5 pt; el PNG 1772 × 1078 px a 300
dpi). **Margen mínimo a los bordes: 2,16 mm** (izquierdo: el borde de 1,3 de
grosor de los bloques negros); superior e inferior 2,29 mm, derecho 4,94 mm;
exigido 2 mm.

Historia (las cinco versiones el 01/10/2026, en la unidad F4; ninguna
commiteada al escribir esto). Antes de dibujar, la unidad frenó porque el
artefacto no arma la unidad estructural del 5.1.1 como la definición del
contexto: pone el título del 5.1.1 en la herencia y no en el texto (sección
8). La disposición quedó fijada en la revisión de ese freno: la figura sigue
al artefacto en las dos unidades.

- Versión 1: la unidad estructural sin llave; el lugar sin rótulo
  («Clasificación de deudores, punto 5.1.1.1»). sha256: generador
  `f626142c4cf20139567f21f17565a85bcf22d6fa6be58dac9fc900777a63abb7`, PNG
  `a97b62062045df2afb23fd886a0ad734d687974d432354d5e2a918523ae58460`, PDF
  `a940cfba60c32a5191a268a71badcc74f178a95ba5bdaf8749034391c2d85660`, LEEME
  `450adc430ea05590c8eb9ad80cc075ade7068893a6ae475af57f953dc0ccce18`.
- Versión 2, con los dos ajustes de la revisión de la versión 1: el
  rótulo «Lugar:» delante de cada lugar, y en la unidad estructural una llave
  como la de la unidad del 5.1.1.1 que agrupa los tres títulos grises bajo
  «títulos que ubican el párrafo». Nada más cambia en la figura. sha256:
  generador `f213f24ce6266dcbdeb7b2bcac4ea19810bff8cf90f23880734d6db8ff6778b4`,
  PNG `602c3d92dcedc52e7fa38908fe850c065372b4e890d4754a25788cbd4d0b63fb`, PDF
  `40cda9a533902c107b46aaac2a4a1062eae2f50fc1c4c65e0227058f4d68fe54`, LEEME
  `dd816c72d776e8bd5ca6923a0b828208ec0cf7cb40dd463be51d3f993564a44e`.
- Versión 3: el título de la unidad de arriba pasa de «Unidad de
  extracción del 5.1.1.1» a «Unidad de punto del 5.1.1.1», en el generador
  (`UNIDADES`, el control `comprobar_textos_fijos` y la descripción inicial).
  La razón es terminológica: «unidad de extracción» nombra a las dos clases de
  unidad, y «unidad de punto» a la de un punto terminal. Nada más cambia en la
  figura: el SVG difiere del de la versión 2 solo en la línea de ese título, y
  los controles dan las mismas cifras de geometría, de margen y de alto. Esa
  terminología de la tesis está NO VERIFICADA contra su fuente en Overleaf. La
  copia del repo, `docs/tesis/main.tex`, sección «La unidad de extracción y la
  segmentación», dice «Unas y otras son las unidades de extracción» y no
  contiene «unidad de punto». sha256: generador
  `c109a83775d671b8e93f1c03612cbe811639494cbe167f5d1422ddbb7a4b4d9e`, PNG
  `7e1eb42ab440cf4ffd0316bc9b39db4b4ef93c0c95c31ec7323f654e65d3890e`, PDF
  `8e20fa4c466c023772228f7ee9cbba50d6fde0232f8bd38300bbc1f1a3f1b700`, LEEME
  `246b2b2c096edb40e274b48b8481957525fac3e73bc386b7036ea546daa954cf`.
- Versión 4: los dos títulos pasan a una forma paralela. Arriba,
  «Unidad de punto del 5.1.1.1» pasa a «Unidad de extracción del punto
  5.1.1.1»; abajo, «Unidad estructural del párrafo del 5.1.1» pasa a «Unidad
  de extracción del párrafo del 5.1.1 (unidad estructural)». El cambio está en
  el generador (`UNIDADES`, el control `comprobar_textos_fijos` y la
  descripción inicial). Nada más cambia en la figura: el SVG difiere del de la
  versión 3 solo en las dos líneas de los títulos, y los controles dan las
  mismas cifras de geometría, de margen y de alto. El título de abajo, el más
  largo, mide 412,3 unidades en negrita a 14 (métricas reales de Helvetica) y
  termina en la unidad 423,3, antes del borde derecho de los bloques (491).
  La copia del repo de la tesis, `docs/tesis/main.tex:620`, usa los dos
  términos («la unidad estructural» y «las unidades de extracción»); contra la
  fuente en Overleaf, NO VERIFICADA. sha256: generador
  `48b012f4bd0837ec4065356d8cc9fb3e208c0d4c06162e7e0cfe5669488bf87b`, PNG
  `b0b1ec74881caac8d2d8ae7a29010361c29959e7540c6915e26860c255ab1789`, PDF
  `bf38e2498110a462bdf89b150aa45b78fad7d348d7be3f5a3f471a3b0a6dcfe5`, LEEME
  `e69d4991f4f351f26ff0ab30abd023c37a72908bd030f125f7a6e1881aec4b19`.
- Versión 5 (esta): el título de abajo pasa a «Unidad de extracción del
  párrafo del 5.1.1», sin el paréntesis «(unidad estructural)», porque la
  tesis deja de usar ese nombre; el de arriba queda como en la versión 4. Que
  la tesis ya no lo use está NO VERIFICADO contra su fuente en Overleaf; la
  copia del repo, `docs/tesis/main.tex:620`, todavía dice «la unidad
  estructural». El cambio está en el generador (`UNIDADES`, el control
  `comprobar_textos_fijos` y la descripción inicial). Nada más cambia en la
  figura: el SVG difiere del de la versión 4 solo en la línea de ese título,
  y los controles dan las mismas cifras de geometría, de margen y de alto. El
  título mide 277,0 unidades en negrita a 14 y termina en la unidad 288,0. En
  este LEEME, «unidad estructural» sigue nombrando la clase de unidad (el tipo
  `mini_chunk` del artefacto) fuera del texto de la figura.

## 1. Cómo regenerar

Desde la raíz del repo (el script también corre desde otro directorio: sus
rutas salen de su propia ubicación):

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_unidad_extraccion.py
```

Escribe `figura_unidad_extraccion.png` y `figura_unidad_extraccion.pdf`. El SVG
es intermedio: va a `rsvg-convert` por la entrada estándar y solo se escribe con
`--svg <ruta>`. Los controles corren siempre (no hay `--verificar`: el script
frena si alguno falla).

Herramientas de la corrida registrada (01/10/2026): `rsvg-convert` 2.62.3
(cairo 1.18.4), y en el `.venv` del repo (Python 3.10.13) pdfplumber 0.11.10,
Pillow 12.3.0 y pypdf 6.10.2. Reutiliza por importación
`generar_figura_norma_a_grafo.py` (sha256
`9b0e45a299a0a078d250ccc999d192cbb83038bd8c00baa6bd8972d021b73f3d`) y
`generar_figura_proceso_extraccion.py` (sha256
`6a91931abeb9927842f76fa50471497e926c69fc56617c62ef7f05ddf6c010d6`), los dos
del commit `fbe69d4`, como las figuras de la página del ejemplo y de cómo se
forma un Texto Ordenado.

## 2. Fuentes

| Fuente | sha256 | Ancla |
|---|---|---|
| PDF del corpus, `data/experiment/subset/TO_clasificacion_deudores_actual.pdf` | `6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2` | fuera de git (`.gitignore:35`); el mismo sha declara el inventario del conjunto de desarrollo, `data/experiment/reextraccion_v2/manifiestos/desarrollo_5tos.json:18-21` (commit `bcb936a`); portada «“A” 8378» y «19/12/2025», comprobada |
| Artefacto de unidades, `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json` (143 unidades) | `98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1` | commit `d082812` (único commit del archivo) |
| E1 de cla del corpus sobre el que se ensambló r1, `data/experiment/reextraccion_v2/corpus_v2/salida/cla/extracciones_e1.jsonl` | `3346f7fbd6fff7869fb07baafa2497af90b4047a597169337b547f6f6d825f45` | commit `5273c0c`; solo para la comprobación de procedencia |

**Por qué este artefacto es el de r1.** r1 es
`data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`
(`docs/tablero.md:38-41`). Su ensamblado lee la salida sellada
`corpus_v2/salida` (`corpus_v2/r1_comun.py:27`) y las unidades de este artefacto
(`r1_comun.py:29` y `:110-111`; `ensamblar_r1.py:56`); la E1 de esa salida cargó
el mismo directorio (`corpus_v2/runner_corpus.py:110` y `:452`, con
`e1_extractor/comun_e1.py:26` y `:40-49`). El script comprueba que los 144
registros de la E1 de cla cubren exactamente las 143 unidades del artefacto y
que las dos del ejemplo están entre ellas con su tipo. El grafo r1 cita además
las dos unidades en su provenance (9 menciones de `cla::5.1.1::intro` y 19 de
`cla::5.1.1.1`):

```bash
grep -o '"chunk_id": "cla::5.1.1.1"' data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json | wc -l
```

`salida_tanda0/chunks_cla.json` y `escalado_prep/e0_dry_subset_ref/cla/chunks_cla.json`
tienen el mismo sha256; `e0_chunking/salida/chunks_cla.json` (sha
`9b82f00a…`, 127 unidades, todas `punto_terminal`) es la calibración previa a
la enmienda 01, sin unidades estructurales.

## 3. Qué texto sale de qué fuente

Todo el texto de los bloques es el del artefacto, transcripto tal cual y con sus
saltos de línea. Las líneas del PDF se cuentan desde 1 en `extract_text_lines`
de la página 16 (las líneas 1 y 2 son el encabezado «CLASIFICACIÓN DE DEUDORES»
y «B.C.R.A.»).

| Unidad | Tramo del artefacto (`tipo` de `unidad_origen`) | Línea del artefacto | Líneas de la página 16 |
|---|---|--:|--:|
| 5.1.1.1 | herencia 1: encabezado de S5 | 2693 | 3 |
| 5.1.1.1 | herencia 2: encabezado de 5.1 | 2701 | 4 |
| 5.1.1.1 | herencia 3: intro de 5.1 | 2709 | 5 |
| 5.1.1.1 | herencia 4: encabezado de 5.1.1 | 2717 | 6 |
| 5.1.1.1 | herencia 5: intro de 5.1.1 | 2725 | 7 |
| 5.1.1.1 | texto | 2686 | 8–12 |
| 5.1.1 | herencia 1: encabezado de S5 | 2645 | 3 |
| 5.1.1 | herencia 2: encabezado de 5.1 | 2653 | 4 |
| 5.1.1 | herencia 3: encabezado de 5.1.1 | 2661 | 6 |
| 5.1.1 | texto | 2638 | 7 |

El registro de la unidad del 5.1.1.1 empieza en `chunks_cla.json:2677`
(`"id": "cla::5.1.1.1"`) y el de la unidad del 5.1.1 en `:2628`
(`"id": "cla::5.1.1::intro"`). El script imprime la línea de cada tramo en cada
corrida y comprueba que esa línea, decodificada, dé el texto de la unidad.

Texto propio de la figura (fijo en `UNIDADES`): los títulos de las unidades, los
rótulos, los rótulos de las llaves y el lugar. El script deriva de cada unidad el
texto esperado y frena si no coincide: «título de la sección» para el
encabezado de la sección; «título del N» para un bloque que solo es el
encabezado de N; «texto del N» para encabezado y párrafo de N; «texto del
5.1.1.1» y «párrafo sin numerar del 5.1.1» para el texto de cada unidad; el
título de cada unidad con su número («Unidad de extracción del punto 5.1.1.1»
y «Unidad de extracción del párrafo del 5.1.1»); la llave
de la unidad terminal, «cadena estructural», y la de la unidad estructural,
«títulos que ubican el párrafo» (`TEXTO_LLAVE`; en la figura, partidos en dos y
en tres líneas); el lugar, «Lugar: » seguido del nombre del Texto Ordenado, que
en mayúsculas tiene que ser la primera línea de la portada («CLASIFICACIÓN DE
DEUDORES»), y del punto.
Ningún rótulo propio lleva comillas.

## 4. Artefacto frente al PDF

Sin diferencias: los diez tramos (seis de la unidad del 5.1.1.1 y cuatro de la
del 5.1.1) están en el texto de la página 16 exactamente como en el artefacto, y
cada línea de cada tramo es una línea del PDF. El corte «pro-» / «ductiva» del
5.1.1.1 está igual en los dos (líneas 11 y 12 de la página) y se dibuja así. La
consola lo imprime («diferencias artefacto / PDF: 0»). Si un tramo solo
apareciera en la página después de quitar guiones de fin de línea y colapsar
blancos, el script lo informaría como diferencia y dibujaría lo que dice el
artefacto; si no apareciera ni así, frenaría.

## 5. Candados y controles

El script frena (`SystemExit`) si:

- el sha256 del PDF, del artefacto o de la E1 de cla no es el fijado, o el
  inventario del conjunto de desarrollo no declara ese PDF para cla;
- la portada no dice «“A” 8378» y «19/12/2025»;
- el artefacto repite ids, o la E1 de cla del corpus de r1 no procesó
  exactamente sus unidades, o no procesó las dos del ejemplo con su tipo
  (`punto_terminal`, `mini_chunk`);
- **la composición de una unidad no es la fijada**: la herencia de
  `cla::5.1.1.1` tiene que ser, en este orden, encabezado de S5, encabezado e
  intro de 5.1, encabezado e intro de 5.1.1; la de `cla::5.1.1::intro`,
  encabezado de S5, de 5.1 y de 5.1.1. Prueba negativa, fuera del repo: con la
  división que pedía la versión inicial del mandato (título del 5.1.1 en el
  texto) el script frena con «el artefacto arma la herencia de otra manera»;
- una unidad o un tramo no está entero en la página 16 según el artefacto; el
  texto del punto terminal no empieza con su número y su título; el texto de la
  unidad estructural no es un único párrafo sin numerar de rol `intro`; o los
  títulos que heredan las dos unidades no coinciden;
- un texto propio no es el que se deriva de la unidad (sección 3), o el nombre
  del Texto Ordenado no es el de la portada. Prueba negativa, fuera del repo: con
  el rótulo de la llave de la unidad estructural partido como «títulos que» /
  «ubican» el script frena. Prueba negativa de los títulos, fuera del repo
  (los títulos se alteran en memoria y se llama a la resolución, sin
  exportar): frena en los siete casos. Abajo, el título como en la versión 4
  («Unidad de extracción del párrafo del 5.1.1 (unidad estructural)») o como
  en las versiones 2 y 3 («Unidad estructural del párrafo del 5.1.1»), sin
  «del párrafo», sin el número o con un blanco al final; arriba, el título
  como en la versión 3 («Unidad de punto del 5.1.1.1») o como en la 2
  («Unidad de extracción del 5.1.1.1»);
- una línea del artefacto no da el texto de la unidad, o un tramo no está en la
  página 16 ni siquiera normalizado (sección 4);
- **transcripción**: lo dibujado, reconstruido por unidad y por tramo, no es el
  texto del artefacto; un tramo de la herencia queda fuera de un bloque gris o
  en otro color que el gris, o el texto fuera del bloque negro o en otro color
  que el negro; o algún texto dibujado contiene «extractor», «::», «/», una
  extensión de archivo, «cla» como palabra o «chunk». Prueba negativa, fuera del
  repo: un texto «cla::5.1.1.1» agregado a la figura la hace frenar;
- **geometría** (métricas reales de Helvetica; 31 textos, 8 cajas, 2 marcas, 0
  fallas): un texto por debajo de 7 pt impresos, fuera del lienzo, superpuesto
  a otro, fuera de la caja que lo contiene, cortado por el borde de otra caja o
  tocado por una de las dos llaves. Holgura mínima de una línea transcripta al borde derecho
  de su bloque: 10,5 unidades (la del párrafo del 5.1.1, 462,5 unidades de
  ancho);
- **margen** (41 elementos: los 31 textos, medidos con las métricas reales, y 10
  dibujados leídos del SVG, 8 rectángulos y 2 trazos, con medio grosor de trazo;
  en las llaves, la caja incluye los puntos de control de sus curvas): un
  elemento a menos de 2 mm (`MARGEN_MM`; 9,6 unidades de lienzo) de uno de los
  cuatro bordes. Es el control de `generar_figura_formacion_to.py:109-113` y
  `:840-852`; `generar_figura_pagina_to.py` no tiene control de margen. Mínimos
  de la corrida registrada: izquierdo 10,3 unidades (2,16 mm), superior 11,0
  (2,29 mm), derecho 23,7 (4,94 mm, la línea «que ubican» del rótulo de la
  segunda llave) e inferior 11,0 (2,29 mm). Prueba negativa, fuera del repo:
  con el contenido a 5 unidades de los bordes, 14 fallas.

Verificación adicional con `docs/tesis/figuras/verificar_geometria_svg.py` sobre
el SVG guardado con `--svg`: 31 textos, 0 nodos, 0 trazos con flecha, 0 fallas.

## 6. Composición

Lienzo de 720 unidades para 15 cm, con 11 unidades (2,29 mm) de margen. Bloques
de la unidad 11 a la 491 (480 unidades, 10,00 cm), con 7 unidades de aire a los
lados y 5 arriba y abajo; interlínea de 16 unidades. Entre bloques grises, 4
unidades; entre la herencia y el texto, 9; entre las dos unidades, 24. Rótulos
en la columna que empieza en la unidad 501, centrados en la altura de su bloque.
En cada unidad, una llave a la derecha de los rótulos de la herencia, de la
unidad 616,7 a la 626,7, que abarca los tres bloques grises: en la unidad del
5.1.1.1, de y = 31,0 a 140,0, con el rótulo en dos líneas («cadena» /
«estructural»); en la unidad estructural, de y = 299,0 a 376,0, con el rótulo
en tres líneas («títulos» / «que ubican» / «el párrafo»). Los rótulos empiezan
en la unidad 632,7 y van centrados en la punta de su llave. Entre la llave y el
margen derecho quedan 76,3 unidades: «títulos que ubican el párrafo» (160,4) no
entra en una línea y ninguna partición en dos líneas entra («títulos que
ubican», 101,9; «ubican el párrafo», 96,8).

Colores de la paleta compartida con las figuras de la página del ejemplo y de
cómo se forma un Texto Ordenado: bloques grises con fondo `#f4f6f8`, borde
`#999999` y texto `#555555`; bloques negros con fondo blanco, borde `#4a5a6a`
(1,3) y texto `#1f1f1f`; rótulos y lugar en `#555555`; títulos en `#1f1f1f`,
negrita; llaves en `#4a5a6a`. El naranja de las figuras hermanas no se usa: la
figura no resalta nada.

## 7. Salidas y reproducibilidad

| Archivo | sha256 |
|---|---|
| `generar_figura_unidad_extraccion.py` | `fb13e6c5c1091e2519a9f228b7e1db8d89406119eb5b2897b5edef7ee2287510` |
| `figura_unidad_extraccion.png` (1772 × 1078 px, 300 dpi) | `fd63395655c041a8a28569f902ca39a5addb90a13aebb20fd29315062e099481` |
| `figura_unidad_extraccion.pdf` (425,2 × 258,5 pt) | `8ddef99029cd4eafc55e3c5a255b39e07893f36dd7621c0b6326b0bceaefacab` |
| SVG intermedio (no se versiona) | `e82a2e48c7a8324ad6c704ec0a7e0b82b3f425e82b6792bf5fbb032503115779` |

Dos corridas con `PYTHONHASHSEED` 0 y 1, que empezaron con un segundo de
diferencia, y una tercera con `PYTHONHASHSEED` 0, 81 segundos después de la
primera: el SVG, el PNG y el PDF salieron idénticos byte a byte en las tres, y
la salida de consola también (salvo la ruta del SVG, que era distinta a
propósito). El PDF es reproducible
porque el script fija `SOURCE_DATE_EPOCH=0` al llamar a `rsvg-convert`, como las
figuras hermanas: `/CreationDate` 01/01/1970. Stream de contenido de la página
del PDF, sha256
`12df8d743e691c7368fae101a5fbc4fa53103240642f8007d4fa7f043a51d7a5`.

Este LEEME cae bajo `.gitignore:180` (`docs/tesis/figuras/*`), sin excepción
que lo libere (`git check-ignore -v --no-index` lo atribuye a esa línea), así
que entra a git forzado, con `git add -f`. Al escribir esto está en el índice
con el contenido de la versión 2 (blob `13f48aa`), sin commit. El generador,
el PNG y el PDF entran por las excepciones `.gitignore:208`, `:186` y `:188`.

## 8. Observación para el texto de la sección 3.2

La definición de la unidad estructural de un punto contenedor («su título y sus
párrafos sin numerar, precedido solo por los títulos de su sección y de los
puntos que lo contienen») no es la que arma el artefacto, en dos puntos:

- **el título propio va en la herencia, no en el texto.** La herencia de una
  unidad estructural es la cadena de títulos «desde la sección hasta el propio
  nodo inclusive» (`data/experiment/reextraccion_v2/e0_chunking/e0_lib.py:1566-1580`),
  y su texto es solo la prosa del bloque (`e0_lib.py:1582-1612`). El modelo
  recibe el título bajo «Cadena de títulos (ubica el bloque; NO es contenido a
  extraer):» y el párrafo solo como su unidad
  (`data/experiment/reextraccion_v2/e1_extractor/prompt_e1.py:476` y `:508-509`);
- **hay una unidad por bloque, no una por punto contenedor.** El párrafo
  anterior a los subpuntos, cada párrafo entre subpuntos y el párrafo posterior
  son unidades distintas (`e0_lib.py:1679-1688`). El 5.1.1 tiene un solo
  párrafo, así que el ejemplo no lo muestra.

La figura sigue al artefacto; el título de la unidad («Unidad de extracción
del párrafo del 5.1.1») ya nombra el bloque. Queda anotado
por si el texto de la sección conserva la definición actual.
