# figura_formacion_to — registro de generación (versión 3)

Figura «cómo se forma un Texto Ordenado» para el análisis del documento
(capítulo 3). A la izquierda, una línea de tiempo con las comunicaciones «A»
del punto 5.1.1.1 de Clasificación de deudores según su fila de la tabla de
correlaciones: la norma de origen («A» 2216) y las ocho que lo modificaron.
Debajo, separada por una línea de puntos y fuera del eje, la «A» 8378, que no
está en esa fila, con el rótulo «última comunicación incorporada al Texto
Ordenado (portada)». A la derecha, el Texto Ordenado como un manual en cinco
bloques rotulados con sus páginas: portada, índice, cuerpo, tabla de
correlaciones e historial. En el cuerpo, una casilla por sección, con la de la
sección 5 y el punto 5.1.1.1 resaltados; en la tabla, la fila del 5.1.1.1
resaltada. Entre las dos, una flecha con el
rótulo «cada comunicación reemplaza las hojas que modifica». La imagen no lleva
nombres de archivo, rutas ni identificadores internos, y ningún texto ni trazo
queda a menos de 2 mm de un borde.

El eje de la línea de tiempo ordena por número de comunicación, sin escala de
tiempo: el documento no da las fechas de las comunicaciones del punto, y la
nota del eje lo dice (sección 4).

Comillas (criterio aprobado en la revisión de la versión 2): los rótulos
propios de la figura escriben «A» con comillas latinas (en el título de la
columna y en los números del eje, «A» 2216); todo lo transcripto del PDF
conserva “A” como en el documento: la fila de la tabla, la portada y el
historial.

**Tamaño efectivo a 15 cm de ancho** (todo el texto es propio de la figura; no
hay facsímil):

| Qué | Lienzo | Impreso |
|---|--:|--:|
| títulos, números de comunicación, rótulos de bloque | 14 unidades | **8,27 pt** |
| subtítulos, rótulos de rol, contenido de los bloques, nota, rótulo de la flecha | 13 unidades | **7,68 pt** |

Mínimo del repo para texto propio: 7 pt; los 64 textos lo cumplen. **Alto: 10,08
cm** (lienzo 720 × 483,8 unidades; el PDF 425,2 × 285,7 pt; el PNG 1772 × 1191
px a 300 dpi). **Margen mínimo a los bordes: 2,19 mm** (derecho; izquierdo,
superior e inferior 2,29 mm); exigido 2 mm.

Historia (versiones 1 y 2 el 30/09/2026 y versión 3 el 01/10/2026, en
U-CAP3-FIGS; ninguna commiteada al escribir esto):

- Versión 1: la «A» 8378 al final del mismo eje, 14 unidades más abajo, con el
  rótulo «última comunicación incorporada (portada)»; “A” en todos los
  rótulos; el contenido pegado a los bordes izquierdo y superior. sha256:
  generador `c852620fcb1055b0948d0bcd0dceb2971fe187d5670aa78020240e9cff9cbc4c`,
  PNG `61f7bf80949a6a2385c9f40d43910a3e70da149525feb2ac06991f5289b55817`, PDF
  `b8c131a996db700d33ce01a7ee92753fa7ff14965ed7e97086681a07c2dff3fd`, LEEME
  `00a29911479165615dae3f5dcf783e1f648b1bec3fafc483e5c64a368fe5deaa`.
- Versión 2, con los cambios de la revisión de la versión 1: la «A» 8378 fuera
  del eje, tras una línea de puntos, con el rótulo nuevo; comillas latinas en
  los rótulos propios; margen de 2 mm a los cuatro bordes, controlado por el
  script; la columna «Punto» de la tabla pasa de 62 a 56 unidades para que las
  observaciones sigan en tres líneas con la columna derecha más angosta. La
  nota del eje decía «El documento solo da la fecha de la última.», lo que es
  incorrecto: el historial fecha otras comunicaciones (sección 4); lo que vale
  es que no fecha ninguna del punto. sha256: generador
  `e05940d634beb930bba6f98c56d33ae24662b80f4e21d6de47a77847f9f9ef1b`, PNG
  `93c2fb8b55b3ce04c7a052a64ecd3b539f559eefe8915a23b24619eb62d4166c`, PDF
  `db3ea6760f77365d57be0db9727716e959bbdb54de92f3efff6ccf9e2c065635`, LEEME
  `64c7462c12c6c46abc12470e9de1d3f458aedefc60d48f636e4905bf4ab00089`.
- Versión 3 (esta), con los cambios de la revisión de la versión 2: la nota
  del eje termina en «El documento no da las fechas de las comunicaciones del
  punto.», y el script frena si el historial diera fecha a alguna comunicación
  de la fila; el bloque de las secciones se rotula «Cuerpo», el nombre que usa
  la tesis. Nada más cambia en la figura.

## 1. Cómo regenerar

Desde la raíz del repo:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_formacion_to.py
```

Escribe `figura_formacion_to.png` y `figura_formacion_to.pdf`. El SVG es
intermedio: va a `rsvg-convert` por la entrada estándar y solo se escribe con
`--svg <ruta>`. Los controles de geometría corren siempre (no hay
`--verificar`: el script frena si alguno falla).

Herramientas de la corrida registrada (01/10/2026): `rsvg-convert` 2.62.3
(cairo 1.18.4), y en el `.venv` del repo (Python 3.10.13) pdfplumber 0.11.10,
Pillow 12.3.0 y pypdf 6.10.2. Reutiliza por importación
`generar_figura_norma_a_grafo.py` (sha256
`9b0e45a299a0a078d250ccc999d192cbb83038bd8c00baa6bd8972d021b73f3d`) y
`generar_figura_proceso_extraccion.py` (sha256
`6a91931abeb9927842f76fa50471497e926c69fc56617c62ef7f05ddf6c010d6`), los dos
del commit `fbe69d4`, como la figura de la página del ejemplo.

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
| PDF del corpus, `data/experiment/subset/TO_clasificacion_deudores_actual.pdf` (60 páginas) | `6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2` | fuera de git (`.gitignore:35`); el mismo sha declara el inventario del conjunto de desarrollo, `data/experiment/reextraccion_v2/manifiestos/desarrollo_5tos.json` (`tos[cla].sha256_pdf`, commit `bcb936a`) |
| E0, `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/estructura_cla.json` | `3cd26083fee7355ef3d8027ac353a744c2f1cfa35830535fe1be2b9505eaf917` | commit `d082812` |
| Estadística del corpus, `reports/u_insumos_cap/estadisticas_corpus.json` | `1630d1de9f5c065eec00a237f2ba21ff43e4ee11e9332409c56593b12ccbe6ab` | commit `ded3494` (solo contraste) |

## 3. Qué dato sale de qué fuente

| Elemento de la figura | Fuente | Ancla |
|---|---|---|
| Portada: «CLASIFICACIÓN DE DEUDORES», «Última comunicación incorporada: “A” 8378», «Texto ordenado al 19/12/2025» | sus tres líneas, tal como están; la segunda viene entre guiones («-Última … 8378-») y se dibuja sin ellos | PDF, página 1 |
| Bloques y sus páginas: portada 1, índice 2–3, cuerpo 4–43, tabla de correlaciones 44–49, historial 50–60 | reglas de `clasificar_paginas` (abajo) sobre el texto de cada página | PDF, páginas 1–60 |
| Casillas 1 a 10 | secciones leídas de los encabezados «Sección N.» de las páginas 4–43 | PDF; la primera página de cada sección coincide con el campo `pagina` de cada sección de `estructura_cla.json` |
| «Sección 5. Categorías de carteras. · pág. 16» y «5.1.1.1. Los créditos para consumo o vivienda.» | `estructura_cla.json`: `numero` y `titulo` de la sección 5 (`:1166-1168`) y del punto; página, `pagina` del punto | comprobados como texto de la página 16 del PDF |
| Fila de la tabla: «5.1.1.1.», tres veces «“A” 2216», «Según Com. “A” 2410, 4310 (punto 1.), 4975, 5311, 5637, 5998, 6558 y 6938.» | palabras de las columnas «Com.» y «OBSERVACIONES» entre «5.1.1.1.» y «5.1.1.2.», con las columnas tomadas de los bordes verticales que atraviesan la fila de encabezados; el texto de observaciones se reenvuelve al ancho del bloque | PDF, página 46 |
| Eje: «A» 2216 (norma de origen); 2410, 4310, 4975, 5311, 5637, 5998, 6558, 6938 (lo modificaron) | la columna «Com.» da el origen; las observaciones «Según Com. “A” …» dan las modificaciones, quitados los paréntesis («(punto 1.)») | PDF, página 46 |
| «A» 8378, aparte y fuera del eje, «última comunicación incorporada al Texto Ordenado (portada)» | la portada; el script comprueba que no esté en la fila del punto | PDF, página 1 |
| Fecha «19/12/25» de la “A” 8378 | la línea «19/12/25: “A” 8378» del historial | PDF, página 50 |
| Bloque del historial: «Comunicaciones que componen el historial de la norma» y «Últimas modificaciones: […] 19/12/25: “A” 8378» | su título, su primera línea y la última de sus modificaciones; «[…]» marca las cuatro omitidas | PDF, página 50 |
| Títulos, rótulos de bloque, encabezados de la tabla, rótulos de rol, nota del eje, rótulo de la flecha | texto fijo del script; el rótulo de la flecha es el del mandato de la unidad; el de la «A» 8378, el rótulo «Cuerpo» y la nota del eje, los de las revisiones | el script comprueba los números que contienen (punto 5.1.1.1), los rótulos fijados, el texto de la nota y que la nota valga (sección 5) |

Las reglas que asignan cada página a un bloque (`clasificar_paginas`), en este
orden: portada, la página 1 si dice «Última comunicación incorporada»; índice,
la página que dice «-Índice-»; cuerpo, la que tiene pie de hoja («Versión: …
COMUNICACIÓN») y una línea «Sección N.» entre sus cuatro primeras; tabla, la que
tiene los encabezados «NORMA DE ORIGEN» y «OBSERVACIONES»; historial, la que
dice «Comunicaciones que componen el historial de la norma» y todas las que la
siguen. Una página sin regla frena el script, y los bloques tienen que ser
contiguos y estar en ese orden. Contrastes: las 40 páginas del cuerpo son las
que E0 declara como cuerpo (`estructura_cla.json:4`, `paginas_cuerpo`); las 6 de
la tabla y las 60 del documento son las de la estadística del corpus para cla
(`estadisticas_corpus.json:6290` y `:6303`).

El bloque «Historial» abarca las páginas 50 a 60 por esa regla: después de las
últimas modificaciones (página 50) siguen, sin pie ni tabla, las disposiciones
transitorias, el texto base y las comunicaciones que dieron origen a la norma o
la actualizaron (páginas 51–57), las comunicaciones vinculadas (58–59) y la
legislación externa relacionada (60). La figura las rotula juntas como
historial.

## 4. NO ENCONTRADO

**La fecha de las nueve comunicaciones de la fila del punto:** “A” 2216, 2410,
4310, 4975, 5311, 5637, 5998, 6558 y 6938. El historial (páginas 50–60) da
fechas de comunicaciones en dos formas: la lista «Últimas modificaciones» de la
página 50 («dd/mm/aa: “A” nnnn»), que fecha cinco, la 7687, 7928, 7937, 8215 y
8378; y, en dos entradas de la página 58, la fecha de publicación en el Boletín
Oficial: «(B.O. del 7.7.99)» en la “A” 2935 y «(B.O. del 7.7.99 rectificada en el
B.O. del 13.7.99)» en la “A” 2936. El «31.3.04» de la entrada de la “B” 8493
(página 57) es parte de su título («Tratamiento del saldo al 31.3.04»). Ninguna
de las nueve del punto tiene fecha en ninguna de las dos formas; la “A” 8378 sí,
en la lista. Por eso el eje ordena por número, sin escala de tiempo, y la nota
dice que el documento no da las fechas de las comunicaciones del punto. La
consola del generador lo imprime (líneas «fechas que el historial da a las
comunicaciones del eje» y «comunicaciones del historial con alguna fecha») y el
script frena si dejara de valer (sección 5).

**Corrección de las versiones 1 y 2 de este LEEME:** decían que el PDF da la
fecha de una comunicación «en un solo lugar», la lista de la página 50. Las
entradas de la página 58 con fecha del Boletín Oficial lo desmienten. Causa:
busqué fechas solo con la forma «dd/mm/aa» de esa lista. La figura no cambia
por esto: ninguna de esas comunicaciones es del punto.

No uso como fecha de una comunicación la vigencia que traen los pies de hoja
(«Vigencia: … COMUNICACIÓN “A” nnnn»): es la vigencia de cada hoja, no la fecha
de la comunicación. La misma comunicación aparece con vigencias distintas: la
“A” 7443 con 01/01/2020 (páginas 10, 14, 19, 31, 33 y 39; «1/1/2020» en la
30), 27/5/2020 (29), 15/01/2022 (32) y 03/01/2022 (43); la “A” 8378, fechada el
19/12/25 en el historial, figura en los pies de las páginas 3 y 11 con
vigencia 20/12/2025. Dos comunicaciones del eje tienen hojas con pie: la “A”
5998 (páginas 12 y 22, 25/06/2016) y la “A” 6558 (páginas 2 y 15, 5/9/2018);
esas vigencias quedan fuera de la figura por la misma razón. Comando que lista
la comunicación y la vigencia del pie de cada hoja:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c "import pdfplumber,re; d=pdfplumber.open('data/experiment/subset/TO_clasificacion_deudores_actual.pdf'); print([(p.page_number, m) for p in d.pages for m in re.findall(r'COMUNICACI.N .A. (\d+) P.gina \d+\s+(\S+)', p.extract_text() or '')])"
```

## 5. Candados y controles

El script frena (`SystemExit`) si:

- el sha256 del PDF, de `estructura_cla.json` o de `estadisticas_corpus.json`
  no es el fijado, o el inventario del conjunto de desarrollo no declara ese
  PDF para cla;
- la portada no dice «“A” 8378» y «19/12/2025» o no tiene tres líneas;
- una página no cae en ninguna regla, los bloques no son contiguos o no van en
  orden, o las secciones no van en orden;
- las páginas del cuerpo no son las 40 de E0, la primera página de alguna
  sección no es la de E0, o las páginas de la tabla o del documento no son las
  de la estadística del corpus;
- el punto o el encabezado de su sección no están en la página que declara E0,
  o esa página no es una página de su sección;
- no se reconoce la fila de encabezados o las columnas de una página de la
  tabla, la fila del 5.1.1.1 no aparece exactamente una vez, su columna «Com.»
  no son comunicaciones «A» o sus observaciones no son «Según Com. “A” …»;
- la fila tiene más de una norma de origen, la última comunicación incorporada
  está en la fila, o las comunicaciones no van en orden creciente de número;
- **la nota del eje no vale:** el historial da fecha a alguna comunicación de la
  fila del punto, en cualquiera de sus dos formas (`fechas_del_historial`: la
  lista «dd/mm/aa: “A” nnnn» y las entradas «“A” nnnn: título» con sus líneas de
  continuación, fechas «d/m/aa» o «d.m.aa», más toda línea del historial con el
  número y una fecha); o el texto de la nota no es el fijado. Prueba negativa,
  fuera del repo: con una fecha simulada para la «A» 2410 («7.7.99») o para la
  «A» 6938 («01/02/20») el script frena;
- la «A» 8378 no tiene fecha en la lista del historial (o la tiene otra
  comunicación del eje), su fecha no es la de la portada, o la última
  modificación del historial no es la última incorporada;
- el título de la línea de tiempo no nombra el punto, el rótulo de la flecha
  no es «cada comunicación reemplaza las hojas que modifica», o el de la «A»
  8378 no es «última comunicación incorporada al Texto Ordenado (portada)»;
- la última comunicación incorporada no cierra el eje;
- la flecha no llega al bloque del cuerpo;
- **geometría** (métricas reales de Helvetica; 64 textos, 19 cajas, 18 marcas,
  0 fallas): un texto por debajo de 7 pt impresos, fuera del lienzo,
  superpuesto a otro, fuera de la caja que lo contiene, cortado por el borde de
  otra caja, o tocado por una marca (eje, marcadores, corchete, flecha, línea
  de puntos, unión entre la casilla y el punto, regla de la tabla);
- **margen** (97 elementos: los 64 textos, medidos con las métricas reales, y
  33 dibujados leídos del SVG, 17 rectángulos, 9 círculos y 7 trazos, con medio
  grosor de trazo y la punta de la flecha): un elemento a menos de 2 mm (`MARGEN_MM`; 9,6
  unidades de lienzo) de uno de los cuatro bordes. Mínimos de la corrida
  registrada: izquierdo 11,0 unidades (2,29 mm), superior 11,0 (2,29 mm),
  derecho 10,5 (2,19 mm, el borde de los bloques de la derecha con medio
  grosor de trazo) e inferior 11,0 (2,29 mm). Prueba negativa, fuera del repo:
  con la geometría de la versión 1 (columna izquierda en x = 0, contenido desde
  y = 4) el control da 21 fallas.

Verificación adicional con `docs/tesis/figuras/verificar_geometria_svg.py` sobre
el SVG guardado con `--svg`: 64 textos, 0 nodos, 1 trazo con flecha, 0 fallas.

## 6. Composición

Lienzo de 720 unidades para 15 cm, con 11 unidades (2,29 mm) de margen a los
cuatro bordes. Columna izquierda de la unidad 11 a la 231 (220 unidades, 4,58
cm), columna derecha de la 356 a la 709 (353 unidades, 7,35 cm), calle de 125
unidades entre las dos con el rótulo de la flecha centrado. Eje vertical con un
marcador por comunicación de la fila, cada 27 unidades: círculo lleno para la
norma de origen, círculo vacío para las que lo modificaron. Veinte unidades
debajo del último, una línea de puntos a lo ancho de la columna (el mismo
trazo que el corte de la figura de la página del ejemplo); 22 unidades más
abajo, fuera del eje, un rombo con la «A» 8378, su fecha y su rótulo en dos
líneas. Corchete a la derecha de las ocho modificaciones, con el rótulo «lo
modificaron»; la flecha sale de ese rótulo, horizontal, y llega al bloque del
cuerpo. Nota del eje en cuatro líneas. En la tabla, columnas de 56, 104 y el
resto de las unidades. Resaltado en el naranja que las figuras hermanas usan
para el ejemplo (`#e07b39`, fondo `#fbe3d3`); bloques en gris claro con borde
gris.

## 7. Salidas y reproducibilidad

| Archivo | sha256 |
|---|---|
| `generar_figura_formacion_to.py` | `de31ceb9fb82b489571b965288553e65432d072aa69d947505c9deffd3fe638f` (hasta el 08/10/2026, `e0910b594c647833e3984edf8198a855faad017ef307823a43004fb2d61b211f`; §9) |
| `figura_formacion_to.png` (1772 × 1191 px, 300 dpi) | `6af84adad220b071524a3ba7fdae5ef376c3aa6aa8290c04c50987641491ff1e` |
| `figura_formacion_to.pdf` (425,2 × 285,7 pt) | `1d0dbce1e90380d1a2d3dcb4bbe2c9b993cf50a2ae84bd4e3b7d43a7c29912e1` |
| SVG intermedio (no se versiona) | `7ff0008c7ac1e7bf49955113bab6b8d06bbbc9aee62ec7e3e3b086f4eda5dff0` |

Dos corridas con `PYTHONHASHSEED` 0 y 1, separadas por cuatro segundos: el SVG,
el PNG y el PDF salieron idénticos byte a byte, y la salida de consola también
(salvo la ruta del SVG, que era distinta a propósito). El PDF es reproducible
porque el script fija `SOURCE_DATE_EPOCH=0` al llamar a `rsvg-convert`, como la
figura de la página del ejemplo (su LEEME, sección 5): `/CreationDate`
01/01/1970. Stream de contenido de la página del PDF, sha256
`05ce75d390c2f0551d89b93648688443375be5664024603deb1714e86c96163e`.

## 8. Observación para el texto del capítulo

La “A” 7024 figura en el pie de 15 hojas, entre ellas la página 16, la del
punto 5.1.1.1 («Versión: 10a. COMUNICACIÓN “A” 7024», vigencia 20/03/2020), y en
el historial (página 55), pero no aparece en ninguna fila de la tabla de
correlaciones: el texto de las 60 páginas dice «7024» solo en las páginas 9,
16, 18, 21, 23–28, 35–38 y 40 (pies) y 55 (historial). Comando:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c "import pdfplumber; d=pdfplumber.open('data/experiment/subset/TO_clasificacion_deudores_actual.pdf'); print([p.page_number for p in d.pages if '7024' in (p.extract_text() or '')])"
```

La tabla, por lo tanto, no registra todas las comunicaciones que reemplazaron
una hoja: la hoja de la página 16 la reemplazó una comunicación que la tabla no
atribuye a ningún punto. La figura no lo muestra; queda anotado por si el texto
del capítulo afirma lo contrario.

## 9. Nota del 08/10/2026: el medidor, `DPI` y la densidad, de `generar_figura_norma_a_grafo.py`

Un cambio en el generador, ninguno en la figura:

- **Qué fallaba.** Desde `88bfe89`, `generar_figura_proceso_extraccion.py` ya no
  tiene `DPI`, `grabar_densidad` ni `medidor`. El generador fallaba al
  importarse, con `AttributeError` en `DPI = proc.DPI` (:106), antes de llegar a
  la llamada `proc.medidor()` (:770): no corría en HEAD.
- **Qué cambió.** Los tres salen ahora de `generar_figura_norma_a_grafo.py`
  (sha256 `618789ae…`), que el generador ya importaba como `base`: `base.DPI`
  (:106; vale 300, como antes), `base.grabar_densidad` (:870; la función de
  :1049 de ese archivo, igual a la que tenía
  `generar_figura_proceso_extraccion.py` en `fbe69d4`) y `base.medidor()` (:770;
  la función de :806). El docstring (:46-51) dice de dónde sale cada cosa. De
  `generar_figura_proceso_extraccion.py` (sha256 `f4842a6a…`) sigue tomando `W`,
  `ANCHO_TEXTO_CM`, `PT_POR_CM` y `FLECHA`, con los mismos valores que en
  `fbe69d4`.
- **El medidor.** `base.medidor()` difiere del de `fbe69d4` en dos cosas: si
  faltan PIL o la fuente del sistema, frena en lugar de devolver `None`, así que
  la reserva con la tabla de métricas del script (:771-773) ya no se alcanza; y
  carga la fuente a `int(round(fs * 10))` en lugar de `fs * 10`. Ninguna de las
  dos cambia esta figura.

El script tiene las mismas líneas (948) y su sha256 pasó de `e0910b59…` a
`de31ceb9…` (§7). Sobre una copia del repo, con `PYTHONHASHSEED` 0, 1 y 4242, el
PNG y el PDF salen idénticos byte a byte a los commiteados, y el SVG intermedio
da el sha256 de §7; registros en el paquete de revisión de FIX-MEDIDOR-8.
