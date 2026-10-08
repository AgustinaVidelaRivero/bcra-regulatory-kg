# figura_pagina_to — registro de generación (versión 3)

Figura «la página del ejemplo» para el análisis del documento (capítulo 3): la
página del Texto Ordenado de Clasificación de deudores que contiene los puntos
5.1.1 y 5.1.1.1 del ejemplo del préstamo, rasterizada desde el PDF del corpus a
10 cm de ancho dentro de una figura de 15 cm, con una columna de seis etiquetas
a la derecha unidas a cada parte por líneas guía; debajo, un recorte del punto
3.7, que está en otra página del mismo documento, a la misma escala que la
página. Se omite el tramo entre el encabezado de 5.1.2 y el pie; el corte se
marca con una línea de puntos. El logo, el encabezado y el pie quedan.

Las seis etiquetas, en este orden y con este texto fijo (título en negrita y una
línea debajo):

| Etiqueta | Línea debajo | Parte de la página |
|---|---|---|
| **Sección 5** | en el encabezado de la página | fila «Sección 5. Categorías de carteras.» de la tabla del encabezado |
| **Punto contenedor 5.1.1** | tiene subpuntos | recuadro sobre «5.1.1. Cartera comercial.»; corchete a la izquierda que abarca 5.1.1 hasta el final de 5.1.1.2 |
| **Párrafo sin numerar** | abre la excepción | recuadro sobre «Abarca todas las financiaciones comprendidas, con excepción de las siguientes:» |
| **Punto terminal 5.1.1.1** | no tiene subpuntos | recuadro sobre el punto 5.1.1.1 completo |
| **Remisión al punto 3.7** | el punto está en la sección 3 | recuadro naranja sobre «punto 3.7.» y flecha naranja hasta el recorte del 3.7 |
| **Pie de página** | versión, comunicación y vigencia | tabla del pie |

El script comprueba que los números de las etiquetas sean los leídos: sección 5
(encabezado de la página), 5.1.1 y 5.1.1.1 (E0 y PDF), 3.7 (la remisión dentro
del terminal) y sección 3 (encabezado de la página del punto remitido).
«Punto contenedor» (un punto con al menos un subpunto), «punto terminal» (uno
sin subpuntos) y «párrafo sin numerar» (el que un contenedor tiene antes o
después de sus subpuntos) son nombres de este trabajo, no del BCRA. La imagen no
lleva nombres de archivo ni rutas.

**Tamaño efectivo a 15 cm de ancho:**

| Qué | En el PDF | Impreso |
|---|--:|--:|
| texto de la página (todos sus caracteres visibles) | 11,04 pt | **6,07 pt** |
| texto del recorte del punto 3.7 | 11,0 pt | **6,04 pt** |
| etiquetas (título y línea, 14 unidades de lienzo) | — | **8,27 pt** |

Factor de la página: se muestran 515,9 pt de ancho en 10,00 cm (283,5 pt), 0,5495.
**Alto total de la figura: 12,51 cm** (425,2 × 354,6 pt el PDF; 1772 × 1478 px
el PNG a 300 dpi).

**Alcance del mínimo de 7 pt.** El mínimo de 7 pt impresos que el repo usa para
las figuras rige para el texto propio de la figura, que acá son las etiquetas
(8,27 pt, lo cumplen). No rige para la reproducción de la página: es un
facsímil del documento, que muestra su disposición (sección, puntos, párrafo,
remisión, pie), y la tesis cita aparte el texto de esos puntos. Por eso el
texto del facsímil (6,07 pt la página, 6,04 pt el recorte) no se controla
contra ese mínimo.

Dato de referencia: para que el facsímil llegara a 7 pt, la página necesitaría
11,5 cm (10 × 7 / 6,07); la columna quedaría en unas 143 unidades de lienzo y la
línea más ancha, «versión, comunicación y vigencia» (204,7 unidades a 14), solo
entraría en una línea a 5,8 pt, por debajo del mínimo que sí rige.

Historia (las tres el 30/09/2026, en U-CAP3-DOC C2; ninguna llegó a
commitearse):

- Versión 1: página a 5,95 cm dentro de 12,75 cm, anotaciones escritas en una
  columna, recorte al costado; texto de la página a 3,61 pt. sha256: generador
  `89de0c6977eed97585b02a7d8eaf51d8294dcd699b1b6fe7e5279c8db4c4daa8`, PNG
  `88db6054fd6965bee4b567af9df0bd5b9d7af61e1122ac09f0a7de13cb26d9c0`, PDF
  `6e51da70f61d7e99a99fc7595b0d0a7ef8f78c93711a05b111a56559f5ea30c2`, LEEME
  `6a874e7fb7999c4e22219797ce494270f95ed29adca2a5ebcbbe58b47df17a3a`.
- Versión 2: página a todo el ancho de 15 cm, marcadores numerados 1 a 6 con la
  leyenda en el epígrafe, recorte debajo, tramo 5.1.2–pie omitido; texto de la
  página a 9,07 pt. sha256: generador
  `d37be09ec125871ad1827a72c02b8cea610c5b96eff811c83ff28c4ce07f0a94`, PNG
  `f7a7abb1fc6e26a4e74bc4673c1270c2ef7a12e6f5c0117ddc5dfd3396faecde`, PDF
  `3feab24196b98293c43d21b0c47c41dd32bf0bdd9250a615940d83b1ae3e7f08`, LEEME
  `c66cb00dd48334d42e632a3cb4a5cfa853be8c7c8a9819aa28347483042dcd17`.
- Versión 3 (esta): combina las etiquetas con líneas guía y el corchete de la
  versión 1, que explican cada parte en la figura misma, con el tramo omitido de
  la versión 2, que deja más alto y más ancho para la página.

## 1. Cómo regenerar

Desde la raíz del repo (el script también corre desde otro directorio: sus
rutas salen de su propia ubicación):

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_pagina_to.py --verificar
```

Escribe `figura_pagina_to.png` y `figura_pagina_to.pdf`. El SVG es intermedio:
va a `rsvg-convert` por la entrada estándar y solo se escribe con
`--svg <ruta>`.

Herramientas de la corrida registrada: `rsvg-convert` 2.62.3 (cairo 1.18.4), y
en el `.venv` del repo pdfplumber 0.11.10 (capa de texto y coordenadas),
pypdfium2 5.12.1 (rasterizado), Pillow 12.3.0 y pypdf 6.10.2 (lectura del PDF
de salida). Reutiliza por importación `generar_figura_norma_a_grafo.py` (sha256
`9b0e45a299a0a078d250ccc999d192cbb83038bd8c00baa6bd8972d021b73f3d`) y
`generar_figura_proceso_extraccion.py` (sha256
`6a91931abeb9927842f76fa50471497e926c69fc56617c62ef7f05ddf6c010d6`), los dos
del commit `fbe69d4`. Del segundo toma el ancho de texto de 15 cm
(`ANCHO_TEXTO_CM`), no el 0,85 de las figuras hermanas.

Desde el 08/10/2026 (§6), el generador importa `generar_figura_norma_a_grafo.py`
en su versión de sha256
`618789ae333e17e0cb7ba1d9baf0d3d006e3f50745869de8bcffd5b487dde67c`, de la que
toma también el medidor, `DPI` y la densidad del PNG, y
`generar_figura_proceso_extraccion.py` en la de sha256
`f4842a6a45b624d7a123da0c423caea1fcc81c1073254d3b1fef63ab1edc5f8c`; la figura
sale idéntica.

## 2. Fuente y páginas

| Qué | Dato | Ancla |
|---|---|---|
| PDF del corpus | `data/experiment/subset/TO_clasificacion_deudores_actual.pdf`, 60 páginas | fuera de git: `.gitignore:35` (`data/experiment/**/*.pdf`) |
| sha256 del PDF | `6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2` | inventario del conjunto de desarrollo: `data/experiment/reextraccion_v2/manifiestos/desarrollo_5tos.json:18-21` (`tos[cla].sha256_pdf`), commit `bcb936a` |
| Versión | portada: «Última comunicación incorporada: “A” 8378», «Texto ordenado al 19/12/2025» | página 1 del PDF, comprobada por el script |
| E0, chunks | `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json`, sha256 `98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1` | commit `d082812` |
| E0, estructura | `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/estructura_cla.json`, sha256 `3cd26083fee7355ef3d8027ac353a744c2f1cfa35830535fe1be2b9505eaf917` | commit `d082812` |
| Página de 5.1.1 y 5.1.1.1 | **16** | `paginas` de `cla::5.1.1.1` = [16]; la misma página en la herencia de `S5`, de `5.1.1` y en `cla::5.1.1::intro` |
| Página de 3.7 | **14** | `paginas` de `cla::3.7` = [14] |

Las páginas no se suponen: salen de esos campos de E0, y el script comprueba que
el texto de cada chunk (`cla::5.1.1.1`, `cla::5.1.1::intro`, `cla::3.7`) esté en
la página que E0 declara, con los guiones de fin de línea quitados y los blancos
colapsados. Eso fija también la convención: el campo `paginas` de E0 cuenta
páginas del PDF desde 1.

El «Página 1» del pie de la página 16 no es la página del PDF: cuenta páginas
dentro de la sección. La Sección 5 empieza en la página 16 del PDF (herencia de
`S5` en E0) y su primera página dice «Página 1»; la página 14 del PDF es la sexta
de la Sección 3, que empieza en la página 9 (`paginas` de `cla::3.1` = [9]), y su
pie dice «Página 6».

El pie de la página 16 dice «Versión: 10a.», «COMUNICACIÓN “A” 7024» y
«Vigencia: 20/03/2020». Es la versión de esa página del documento, no la del
Texto Ordenado completo, cuya última comunicación incorporada es la «A» 8378
(portada).

## 3. Candados y controles

El script frena (`SystemExit`) si:

- el sha256 del PDF no es `PDF_SHA256`, o el inventario no declara ese sha y esa
  ruta para `cla`;
- la portada no dice «“A” 8378» y «19/12/2025»;
- el sha256 de `chunks_cla.json` o de `estructura_cla.json` no es el fijado;
- E0 no pone en una sola página el punto terminal, el punto remitido, el
  encabezado de la sección, el del contenedor y su párrafo sin numerar;
- `estructura_cla.json` no da a 5.1.1.1 como hijo de 5.1.1, da hijos a 5.1.1.1
  o no da a 5.1.1 un segmento `intro`;
- el texto de un chunk no está en su página, o el párrafo sin numerar y el
  recorte de 3.7 leídos del PDF no coinciden con el texto de E0;
- la página no es de la Sección 5, el punto remitido no es de la Sección 3,
  después de 5.1.1 no sigue 5.1.2, el párrafo sin numerar no contiene «con
  excepción de» o el terminal no remite al punto 3.7;
- «punto 3.7.» no aparece exactamente una vez dentro del punto terminal;
- el pie no tiene versión, comunicación y vigencia;
- un número de las etiquetas no es el leído, o una etiqueta no entra en una
  sola línea de la columna;
- el corte superior tocaría la línea que sigue a 5.1.2, o el tramo del pie
  empezaría sobre texto omitido;
- **geometría** (20 piezas contra los 1.989 caracteres con tinta y los 51
  bordes de tabla de la página): el tramo de cada línea guía sobre la página
  toca un carácter; un punto de origen, el corchete o la flecha tocan un
  carácter o un borde de tabla; o las líneas guía se cruzarían (sus orígenes y
  sus etiquetas no siguen el mismo orden vertical). Las líneas guía pueden
  cruzar un borde de tabla: la de la sección sale de su fila por el borde
  derecho del encabezado. Los espacios que el PDF trae como caracteres no
  cuentan (no tienen tinta). En la primera prueba de esta versión el control
  frenó el script porque el punto de origen de la línea guía del pie caía sobre
  el borde derecho de su tabla; quedó a un radio de distancia, afuera.

Con `--verificar`, además, mide los doce textos de las etiquetas con las
métricas reales de Helvetica: ninguno por debajo de 7 pt impresos, fuera de la
columna, superpuesto a otro o sobre la página o el recorte; 12 medidos, 0
fallas. Verificación geométrica adicional con
`docs/tesis/figuras/verificar_geometria_svg.py` sobre el SVG guardado con
`--svg`: 12 textos, 0 nodos, 1 trazo con flecha, 0 fallas.

## 4. Composición

Todas las posiciones salen de la capa de texto del PDF (pdfplumber), en puntos
PDF de la página 16:

- Ancho mostrado: de x = 60,0 a x = 575,8 (515,9 pt) en 480 de las 720
  unidades del lienzo (10,00 cm). A la izquierda del contenido quedan 12,9 pt,
  por donde baja la flecha (a 6 pt del contenido); a la derecha, 5 pt. Calle de
  20 unidades (0,42 cm), columna de etiquetas de 216 unidades (4,50 cm) y 4
  unidades de margen.
- Tramo superior: del logo (con 4 pt de aire) hasta 5 pt debajo del encabezado
  de 5.1.2 (y = 27,0 a 527,0). Se omiten las 10 líneas que siguen, de
  «Comprende:» a 5.1.2.4, y el blanco hasta el pie; el corte es una banda de 16
  unidades con una línea de puntos.
- Tramo del pie: de 8 pt sobre su tabla a 5 pt debajo (y = 765,2 a 804,5).
- Recorte del punto 3.7 (página 14): sus 4 líneas con 6 pt de aire (y = 389,8 a
  463,5), con el mismo ancho mostrado y la misma escala que la página, 14
  unidades debajo de ella, con borde naranja.
- Escala: 0,9304 unidades de lienzo por punto PDF; lienzo 720 × 600,4 unidades.
  Rasterizado a 4 píxeles por punto PDF (2063 px de ancho por recorte).
- Recuadros en el gris oscuro de la paleta compartida (`#4a5a6a`) sobre el
  encabezado de 5.1.1, el párrafo sin numerar y el punto 5.1.1.1 completo;
  recuadro naranja (`#e07b39`, el color que las figuras hermanas reservan a las
  remisiones) sobre «punto 3.7.». La sección y el pie no llevan recuadro: ya
  tienen los bordes de su tabla.
- Corchete del contenedor a la izquierda de 5.1.1 (x = 91,0), de su encabezado
  al final de 5.1.1.2 (y = 169,4 a 496,8; 20 líneas).
- Líneas guía: cada una sale, con un punto, del borde derecho de su parte a la
  altura de su primera línea, va en horizontal hasta salir de la página y sigue
  en diagonal hasta el título de su etiqueta. Orígenes: sección (313,6; 98,0),
  al final del texto de su fila; contenedor (221,5; 175,0); párrafo (524,0;
  200,3); terminal (568,1; 225,6); remisión (568,1; 263,5), en naranja, desde el
  borde del recuadro del terminal en la línea de «punto 3.7.»; pie (575,1;
  786,3), fuera del borde de su tabla (570,8). Cada etiqueta queda a la altura de su
  origen o, si no entra, debajo de la anterior.
- Flecha naranja de la remisión: sale del borde izquierdo del recuadro del
  terminal en la línea de «punto 3.7.» (126,5; 263,5), baja por la sangría
  entre el corchete y el bloque (x = 108,8) hasta el blanco que separa 5.1.1.2
  de 5.1.2 (y = 503,9), pasa bajo el extremo del corchete y baja por el margen
  izquierdo (x = 66,9) hasta el recorte del 3.7. No cruza texto, ni el corchete,
  ni las líneas guía de la derecha. Desde el recuadro de «punto 3.7.» en línea
  recta cruzaría el resto de la línea o las líneas de abajo.

Qué está escrito a mano: el texto fijo de las seis etiquetas (`ETIQUETAS`); sus
números se comprueban contra el PDF y E0.

## 5. Salidas y reproducibilidad

| Archivo | sha256 |
|---|---|
| `generar_figura_pagina_to.py` | `241b49814db8ebe7c78e035776bd2de80a652c75c8c33af99eec74cf58fd5c47` (hasta el 08/10/2026, `149e4bd9130d67b5440b6226c9b9f941327642e384a3f8572ea3481caafd9ce0`; §6) |
| `figura_pagina_to.png` (1772 × 1478 px, 300 dpi) | `abb991a5af5a2f83917b33e36b72628719100787c4790527a02beac5129fd115` |
| `figura_pagina_to.pdf` (425,2 × 354,6 pt) | `1568ca603aaa21923e199b7a2a1bf7e393e110cfb66fc6857e78580733575dff` |
| SVG intermedio (no se versiona) | `01d4560155cbb30332b9ac91b4478d251cd68e835ad6b54866abbba7dde165c6` |

Tres corridas con `PYTHONHASHSEED` 0, 1 y 2, separadas por más de un segundo:
el SVG, el PNG y el PDF salieron idénticos byte a byte, y la salida de consola
también.

El PDF es reproducible porque el script fija `SOURCE_DATE_EPOCH=0` al llamar a
`rsvg-convert`. Sin eso no lo es: cairo escribe `/Producer` y `/CreationDate`,
con segundos, en el diccionario `/Info`, que queda dentro de un `/ObjStm`
comprimido; un `grep` sobre los bytes del archivo no las encuentra, pero el
archivo cambia con el segundo de la corrida (en la prueba de la versión 1 sin la
variable, tres corridas dieron dos sha256 distintos, con el mismo largo en
bytes). Con la variable, la fecha es fija: 01/01/1970 (valor 0 de la época
Unix). Comando para verlo:

```bash
.venv/bin/python -B -c "from pypdf import PdfReader; print(PdfReader('docs/tesis/figuras/figura_pagina_to.pdf').metadata)"
```

Controles adicionales que imprime el script: sha256 del stream de contenido de
la página del PDF,
`295baeff42f94a33498bda1deac43a1543060a135adcfee79f34071cff70f1a4`, y de sus tres
XObjects (las tres imágenes),
`584b4479eb2714786ab0267802cd3c26d2b6fa716fcfe5bb7b574e1594bcca41`,
`68f65e8aa3e920780c3898526f1fb0b301ac384c2cf8feccec33229fe40dc8cc` y
`bf6d175d3a2301529593a7841d7158c2aa4434fba6fa4d0b5b54da68b58d9be7`.

## 6. Nota del 08/10/2026: el medidor, `DPI` y la densidad, de `generar_figura_norma_a_grafo.py`

Un cambio en el generador, ninguno en la figura:

- **Qué fallaba.** Desde `88bfe89`, `generar_figura_proceso_extraccion.py` ya no
  tiene `DPI`, `grabar_densidad` ni `medidor`. El generador fallaba al
  importarse, con `AttributeError` en `DPI = proc.DPI` (:123), antes de llegar a
  la llamada `proc.medidor()` (:708): no corría en HEAD.
- **Qué cambió.** Los tres salen ahora de `generar_figura_norma_a_grafo.py`
  (sha256 `618789ae…`), que el generador ya importaba como `base`: `base.DPI`
  (:123; vale 300, como antes), `base.grabar_densidad` (:677; la función de
  :1049 de ese archivo, igual a la que tenía
  `generar_figura_proceso_extraccion.py` en `fbe69d4`) y `base.medidor()` (:708;
  la función de :806). El docstring (:46-51) dice de dónde sale cada cosa. De
  `generar_figura_proceso_extraccion.py` (sha256 `f4842a6a…`) sigue tomando `W`,
  `ANCHO_TEXTO_CM` y `PT_POR_CM`, con los mismos valores que en `fbe69d4`.
- **El medidor.** `base.medidor()` difiere del de `fbe69d4` en dos cosas: si
  faltan PIL o la fuente del sistema, frena en lugar de devolver `None`, así que
  la reserva con la tabla de métricas del script (:709-712) ya no se alcanza; y
  carga la fuente a `int(round(fs * 10))` en lugar de `fs * 10`. Ninguna de las
  dos cambia esta figura.

El script tiene las mismas líneas (831) y su sha256 pasó de `149e4bd9…` a
`241b4981…` (§5). Sobre una copia del repo (con `--verificar`, como dice §1),
con `PYTHONHASHSEED` 0, 1 y 4242, el PNG y el PDF salen idénticos byte a byte a
los commiteados, y el SVG intermedio da el sha256 de §5; registros en el paquete
de revisión de FIX-MEDIDOR-8.
