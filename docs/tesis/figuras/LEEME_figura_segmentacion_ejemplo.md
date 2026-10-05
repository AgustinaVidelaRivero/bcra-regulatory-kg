# figura_segmentacion_ejemplo — registro de generación (versión 1)

Figura del ejemplo de la segmentación, para la sección 4.1 de la tesis. Muestra
qué unidades de extracción salen del punto 5.1.1 de Clasificación de deudores,
en dos partes, a 15 cm de ancho:

- **A la izquierda**, el fragmento del 5.1.1 como aparece en el documento, bajo
  «Clasificación de deudores, página 16»: el título del punto, su párrafo
  propio y sus dos subpuntos, cada uno con su número y su primera línea. La
  del 5.1.1.2 se corta con «…». Una llave marca cada parte que da una unidad.
- **A la derecha**, bajo «Unidades de extracción», una tarjeta por unidad,
  unida por una flecha a la llave de su parte. La tarjeta del 5.1.1.1 va
  abierta. Muestra su cadena estructural como tres bloques en gris, cada uno
  con su título («Sección 5. Categorías de carteras.», «5.1. Categorías.» y
  «5.1.1. Cartera comercial.»), su texto propio (las dos primeras líneas, la
  segunda cortada con «…»), sus páginas («Páginas: 16») y sus marcas
  («Marcas: ninguna»). Las otras dos van cerradas, solo con su nombre:
  «5.1.1, párrafo» y «5.1.1.2».

La figura no lleva identificadores internos, nombres de archivo ni nombres de
campos del código, y el generador lo controla. El gris de la cadena
(`#e6e6e6`) es el único color nuevo frente a la figura del proceso: separa el
contexto heredado del texto propio.

## 1. Comandos

Desde la raíz del repo:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_segmentacion_ejemplo.py
```

El generador escribe `figura_segmentacion_ejemplo.svg`, `.png` y `.pdf` junto
a sí mismo. Con `--salida <directorio>` los escribe en otro lugar, y así corrí
las pruebas de determinismo de §7. Con `--mutacion <nombre>` inyecta un
defecto y tiene que frenar sin escribir nada (§5). Lo corrí con el Python
3.10.13 del `.venv`. Usa la biblioteca estándar y `pdfplumber` (para leer las
líneas de la página del PDF), y `rsvg-convert` 2.62.3 (cairo 1.18.4) para el
PNG y el PDF, como las figuras hermanas. No importa otros módulos del repo:
lee la figura del proceso como texto. No usa red ni API.

## 2. Fuentes y sellos

Todas con candado de sha256: si una cambia, el generador frena antes de dibujar.

| Fuente | Qué toma la figura | sha256 | Ancla |
|---|---|---|---|
| `docs/tesis/figuras/generar_figura_proceso.py` | el estilo (§6) y la tabla AFM de Helvetica y Helvetica-Bold (`_CARS` :335, `_AFM` :336-349) | `8667c219fe5586466e3cad04bc81843a8b39025d59b443edbacf79740349cbbf` | commit `552e61f` |
| `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/chunks_cla.json` | las unidades del 5.1.1: tipo, texto, cadena, páginas y marcas | `98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1` | commit `9f6361e` (único commit del archivo) |
| `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/estructura_cla.json` | el árbol del 5.1.1: título, párrafo propio y subpuntos | `3cd26083fee7355ef3d8027ac353a744c2f1cfa35830535fe1be2b9505eaf917` | commit `9f6361e` |
| `data/experiment/subset/TO_clasificacion_deudores_actual.pdf` | las líneas de la página 16 (con `extract_text_lines`) | `6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2` | fuera de git (`.gitignore:35`) |

Los dos archivos de la segmentación son los de HEAD y los de `9f6361e`
(`git show 9f6361e:<ruta> | shasum -a 256` da los mismos sha). Tienen el mismo
sha256 que los de `salida_enm01/`, de los que salen las figuras de la unidad y
del árbol de la sección del capítulo 3. `salida_tanda0_r2/chunks_cla.json`
también tiene ese sha (`shasum -a 256` sobre las tres rutas). La segmentación
r2b de Clasificación de deudores es, byte a byte, la del capítulo 3.

Métrica de texto. Los anchos salen de la tabla AFM de la figura del proceso,
leída del árbol sintáctico de ese archivo sin ejecutarlo. A esa tabla le sumo
un carácter que no tiene: «…», de 1000 en Helvetica y en Helvetica-Bold
(«C 188 ; WX 1000 ; N ellipsis» en `Helvetica.afm`, sha256
`db772f2830fb6d000907791d8d26a12524d96943a9a739e520ee855c6b25c96f`, y
`Helvetica-Bold.afm`, sha256
`8b697881c8ee617a177f6f2e2bbc88570b9fd2b9f0e89ecfc0f5507878f988fc`, las dos
copias de matplotlib que cita el registro de la figura del proceso, fuera del
repo). Contra la Helvetica del sistema (`/System/Library/Fonts/Helvetica.ttc`,
medida con PIL en el scratchpad sobre los 19 textos del SVG), la mayor
diferencia en que la real es más ancha es de +0,04 unidades, en «Abarca todas
las financiaciones comprendidas,». La holgura mínima de un texto al borde de su
caja es 5,0.

## 3. Qué texto sale de qué fuente

Rutas cortas: `seg/` = `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/`.
Las líneas del PDF son las de `extract_text_lines` de la página 16, contadas
desde 1. La línea 1 es el encabezado «CLASIFICACIÓN DE DEUDORES».

### 3.1 Las unidades que salen del 5.1.1

En la estructura, el 5.1.1 (`seg/estructura_cla.json:1193`) tiene un solo
párrafo propio, de rol `intro` (`:1198-1207`), y dos subpuntos, el 5.1.1.1
(`:1211`) y el 5.1.1.2 (`:1230`), los dos sin subpuntos. La segmentación saca
de él tres unidades, en este orden (`seg/chunks_cla.json`):

| Unidad en la figura | Clase | Registro | Texto inicial | Páginas | Marcas |
|---|---|---|---|---|---|
| 5.1.1, párrafo | unidad del párrafo propio (`mini_chunk`, `rol_bloque` `intro`) | `:2628` | «Abarca todas las financiaciones comprendidas, con excepción de las siguientes:» (`:2638`, el texto entero) | 16 (`:2635`) | ninguna (`:2667-2669`) |
| 5.1.1.1 | unidad de punto terminal (`punto_terminal`) | `:2677` | «5.1.1.1. Los créditos para consumo o vivienda.» (`:2686`) | 16 (`:2683`) | ninguna (`:2731-2733`) |
| 5.1.1.2 | unidad de punto terminal (`punto_terminal`) | `:2741` | «5.1.1.2. A opción de la entidad, las financiaciones de naturaleza comercial de hasta el» (`:2750`) | 16 (`:2747`) | ninguna (`:2795-2797`) |

El generador comprueba que las unidades del 5.1.1 sean exactamente esas: el
párrafo y una por subpunto, en el orden de la estructura. Ninguna otra unidad
del archivo empieza con «5.1.1.».

El párrafo propio del 5.1.1, completo: «Abarca todas las financiaciones
comprendidas, con excepción de las siguientes:». Es el mismo texto en
`seg/estructura_cla.json:1205`, en `seg/chunks_cla.json:2638` y en la línea 7
de la página 16 del PDF.

### 3.2 La cadena estructural del 5.1.1.1

La herencia del 5.1.1.1 (`seg/chunks_cla.json:2689`) tiene cinco tramos, que
forman tres bloques, uno por ancestro:

| Bloque | Tramos | Título (lo que dibuja la figura) | Línea del PDF |
|---|---|---|--:|
| sección 5 | encabezado (`:2693`) | «Sección 5. Categorías de carteras.» | 3 |
| 5.1 | encabezado (`:2701`) + párrafo propio (`:2709`, «La cartera se agrupará en dos categorías básicas:») | «5.1. Categorías.» | 4 |
| 5.1.1 | encabezado (`:2717`) + párrafo propio (`:2725`, «Abarca todas las financiaciones comprendidas, con excepción de las siguientes:») | «5.1.1. Cartera comercial.» | 6 |

El generador comprueba que los bloques sean los ancestros del 5.1.1.1 en la
estructura, en orden, y que cada uno empiece con su título. Los bloques del
5.1 y del 5.1.1 llevan además su párrafo, y la figura no lo dibuja: la figura
de la unidad del capítulo 3 (`generar_figura_unidad_extraccion.py`, sha256
`fb13e6c5c1091e2519a9f228b7e1db8d89406119eb5b2897b5edef7ee2287510`) ya muestra
la cadena del 5.1.1.1 con su texto completo (su registro, §3).

Páginas del 5.1.1.1: 16. Marcas: ninguna. La segmentación marca una unidad
por contenido tabular o por fórmula (`contenido_tabular` y `formula`,
heurísticas de `data/experiment/reextraccion_v2/e0_chunking/e0_lib.py:1695-1730`),
y las dos están en falso.

### 3.3 Inventario de los textos dibujados

Diecinueve textos, en 17 entradas. Cada texto es de una entrada y cada entrada
se dibuja. El control (§4, punto 1) comprueba el modo de cada entrada contra
su fuente:

- «literal»: igual a la fuente;
- «cortado»: un prefijo de la fuente que termina en una palabra entera,
  seguido de «…»;
- «partido»: los renglones, unidos por un blanco, dan la fuente;
- «primeras»: las primeras líneas del texto, la última cortada con «…» si el
  texto sigue;
- «propio»: un rótulo de la figura, o un texto que se deriva de la fuente.

| Entrada | Modo | Dibujado | Fuente |
|---|---|---|---|
| encabezado del documento | propio | «Clasificación de deudores, página 16» | en mayúsculas, la línea 1 de la página; la página, la del 5.1.1 en la estructura y la de las tres unidades |
| encabezado de las unidades | propio | «Unidades de extracción» | rótulo de la figura |
| título del 5.1.1 | literal | «5.1.1. Cartera comercial.» | PDF, línea 6 (y título del nodo en la estructura) |
| párrafo del 5.1.1 | partido | «Abarca todas las financiaciones comprendidas,» / «con excepción de las siguientes:» | PDF, línea 7 |
| primera línea del 5.1.1.1 | literal | «5.1.1.1. Los créditos para consumo o vivienda.» | PDF, línea 8 |
| primera línea del 5.1.1.2 | cortado | «5.1.1.2. A opción de la entidad, las…» | PDF, línea 13 |
| nombres de las tarjetas | propio | «5.1.1, párrafo», «5.1.1.1», «5.1.1.2» | número del punto de cada unidad; «párrafo» para la unidad del párrafo propio |
| rótulos de la tarjeta abierta | propio | «Cadena estructural», «Texto propio» | rótulos de la figura |
| bloques de la cadena | literal | los tres títulos de §3.2 | PDF, líneas 3, 4 y 6 |
| texto propio | primeras | «5.1.1.1. Los créditos para consumo o vivienda.» / «Los créditos de esta clase que superen el…» | `seg/chunks_cla.json:2686`; PDF, líneas 8 y 9 |
| páginas | propio | «Páginas: 16» | las páginas de la unidad |
| marcas | propio | «Marcas: ninguna» | las marcas de la unidad |

Por modo: 5 literales, 1 cortada, 1 partida, 1 de primeras líneas y 9
propias (17).

El texto completo de cada unidad de punto, con sus saltos de línea, es una
sucesión de líneas consecutivas de la página 16: el 5.1.1.1, las líneas 8 a
12; el 5.1.1.2, las 13 a 25. Las partes del fragmento están en el orden del
documento (líneas 6, 7, 8 y 13). El generador lo comprueba.

## 4. Controles

Todos están en el script. El primero que falla FRENA y no se escribe nada.
Valores de la consola del generador (comando de §1):

1. contenido: 19 textos en 17 entradas del inventario, con el modo de cada
   una contra su fuente (§3.3). Ningún texto lleva identificadores internos,
   nombres de archivo ni nombres de campos del código (`PROHIBIDOS`: «::»,
   «_», barras, extensiones, «cla», «chunk», «mini», nombres de campos,
   hexadecimales). Cada una de las 8 cajas tiene su clase.
2. trazado: 3 flechas y 7 tramos, ningún tramo diagonal, nulo ni de vuelta.
   Cada flecha sale de la mitad del lomo de la llave de su parte, hacia
   afuera, y llega al borde izquierdo de la tarjeta de su unidad, a 12
   unidades o más de las esquinas. Hay una flecha por unidad.
3. cajas: 8 cajas. Las que no se contienen no se superponen: 24,9 unidades
   como mínimo entre bordes (exigidas 8) y 3,0 entre dos bloques hermanos
   (exigidas 2). Cada bloque queda dentro de su tarjeta, con 7,7 de aire como
   mínimo (exigidas 3). Ningún trazo, punta ni llave entra en una caja.
4. cruces: **0 cruces** y 0 contactos entre flechas. La distancia mínima entre
   dos flechas es 23,2 («5.1.1.1» / «5.1.1.2») y de una flecha a una llave
   ajena, 16,9, con 3,0 exigidas. Ninguna punta toca otra flecha.
5. textos: ninguno superpuesto. Las distancias mínimas son 4,0 entre textos,
   11,1 de texto a trazo, 17,5 de texto a marca y 5,0 de texto al borde de su
   caja. La letra es de 13 unidades (7,27 pt) y de 14 unidades (7,83 pt)
   impresas a 15 cm.
6. margen: 37 elementos, todos a 2 mm o más del borde (izquierdo, derecho e
   inferior 2,21 mm; superior 2,76 mm).
7. registro y colores: el SVG se relee. Sus 34 elementos están registrados, en
   orden, y cada bloque se emite después de la tarjeta que lo contiene. Se
   controla el color de las 8 cajas, las 4 marcas (el pliegue y las tres
   llaves), las 3 flechas y los 19 textos. Los colores del SVG son `#1f1f1f`,
   `#444444`, `#555555`, `#999999`, `#e6e6e6`, `#fafafa` y `white`, y el gris
   `#e6e6e6` está solo en los tres bloques de la cadena.

## 5. Pruebas negativas

Corren en cada ejecución, antes de escribir, y cada una tiene que frenar en su
control y con su motivo. Si alguna no frena, el generador frena en
`[pruebas]`. Las cuatro primeras actúan sobre las fuentes leídas; las once
restantes, sobre una copia del modelo de la figura. Esas once también se
corren solas con `--mutacion`: cada una sale con código 1 y no escribe nada (0
archivos en el directorio de salida).

```
candado_del_pdf          [fuentes] data/experiment/subset/TO_clasificacion_deudores_actual.pdf no es el verificado: sha256 c2bd4dc5a2c4… ≠ 6e7f528d3fea…
estilo_distinto          [estilo] FS_TITULO, FS_TEXTO: la figura usa (14, 12) y docs/tesis/figuras/generar_figura_proceso.py:171 declara (14, 13)
texto_de_la_unidad       [contenido] el texto de la unidad 5.1.1.1: 0 apariciones en la página, se esperaba una: '5.1.1.1. Los créditos para consumo y vivienda.\nLos créditos '
seis_subpuntos           [contenido] el 5.1.1 tiene 6 subpuntos (más de 5): la figura no prevé resumirlos
texto_alterado           [contenido] «cadena_1»: dibujado ['5.1. Categorías. La cartera'] ≠ inventario ['5.1. Categorías.']
corte_en_media_palabra   [contenido] «parte_2»: ['5.1.1.2. A opción de la enti…'] no es cortado de su fuente '5.1.1.2. A opción de la entidad, las financiaciones de naturaleza come'
identificador            [contenido] «cla::5.1.1.2» lleva '::'
tramo_diagonal           [trazado] tramo diagonal en «5.1.1.1»: (342.0, 124.5) → (426.0, 134.5)
tarjetas_superpuestas    [cajas] la caja «tarjeta_1» se superpone con «tarjeta_2» o queda a -1.6 (< 8.0)
cruce_entre_flechas      [cruces] 2 cruce(s) entre flechas: «5.1.1.1» × «5.1.1.2» en (372, 124.5); «5.1.1.1» × «5.1.1.2» en (398, 124.5)
letra_chica              [textos] «Marcas: ninguna»: letra de 6.15 pt (< 7.0)
texto_fuera_de_su_caja   [textos] «Marcas: ninguna» a 1.0 del borde de su caja «tarjeta_1»
margen                   [margen] texto «Unidades de extracción» a 9.0 unidades del borde superior (< 10.1)
color                    [registro] «cadena_0» con relleno #fafafa, borde #999999 y grosor 1, no los de «cadena»
bloque_tapado            [registro] el bloque «cadena_0» se emite antes que «tarjeta_1», que lo contiene y lo tapa
```

Hay al menos una por control: fuentes 1, estilo 1, contenido 5, trazado 1,
cajas 1, cruces 1, textos 2, margen 1 y registro 2 (15). La prueba
`seis_subpuntos` es el resguardo de la regla para resumir subpuntos: el 5.1.1
tiene dos, y la figura no prevé resumir más de cinco.

La prueba `bloque_tapado` y el control del orden de pintado salen de un error
de la primera corrida. La tarjeta abierta se registraba después de sus bloques
y los tapaba, y los controles de entonces pasaban igual, porque ninguno miraba
el orden de pintado. Lo vi en el PNG. Ahora la tarjeta se registra antes que
sus bloques, y el control de registro frena si un bloque se emite antes que la
caja que lo contiene.

## 6. Estilo y composición

El estilo es el de la figura del proceso. Cada valor que uso se coteja con la
línea de `generar_figura_proceso.py` que lo declara, y la consola imprime esa
línea:

- el lienzo `W` (:163), la tipografía (:164);
- la paleta `NEUTRO`, `TINTA` y `TINTA_SUB`, `FLECHA` (:167-169), y el blanco
  de la caja discontinua (:170);
- los cuerpos y las interlíneas (:171-172), los márgenes internos (:174);
- los grosores de caja, de la caja discontinua y de la línea principal
  (:175-176), el radio de los trazos (:177) y las esquinas (:178);
- el margen (:180), el grosor del marco de la leyenda (:181) y la esquina de
  sus muestras (:1123), el marcador de las puntas (:183-184) y el pliegue de
  la hoja (:395);
- el tamaño impreso, los mínimos y las holguras (:311-325), la caja del texto
  (:350) y `SOURCE_DATE_EPOCH` (:1187).

Las piezas son estas:

- la hoja: la del Texto Ordenado de la figura del proceso, con la esquina
  plegada, en `NEUTRO`. El párrafo y los subpuntos van 14 unidades a la
  derecha del título del punto, como en el documento (columnas 98,0 y 129,0
  pt en la página). Entre dos partes hay 8 unidades de aire, porque el
  documento separa sus párrafos (en las líneas 6 a 25 de la página, de 25,2 a
  25,4 pt entre las primeras líneas de dos párrafos y de 12,6 a 12,8 dentro
  de uno, por `top` de `extract_text_lines`);
- las tarjetas: cajas de datos, en `NEUTRO`, de 320 unidades de ancho;
- los bloques de la tarjeta abierta: grosor 1 y esquina 3, los del marco y las
  muestras de la leyenda del proceso. Los de la cadena van en gris
  `#e6e6e6`, el único color nuevo. El del texto propio va en blanco. Los dos
  tienen el borde de `NEUTRO`;
- las llaves: en `FLECHA`, con el grosor de la caja discontinua (1,3), a 10
  unidades del borde de la hoja;
- las flechas: las de la línea principal del proceso (`FLECHA`, 1,8, con su
  marcador). La del 5.1.1.1 es recta y llega a la altura del nombre de su
  tarjeta. La del párrafo dobla hacia arriba en x = 372 y la del 5.1.1.2,
  hacia abajo en x = 398. Las dos doblan en x distintas, para que no parezcan
  una sola línea cortada por la recta;
- los textos: los nombres y los encabezados, en negrita de 14 y `TINTA`; lo
  demás, en 13 y `TINTA_SUB`.

Para llegar al nombre de la tarjeta abierta, esa tarjeta empieza 26,5
unidades debajo de la del párrafo. Debajo de ella dejo el mismo aire, para
enmarcarla.

## 7. Tamaño, salidas y determinismo

Lienzo de 760 × 432 unidades, impreso a **15,00 × 8,53 cm**. El PNG mide 1772 ×
1008 px a 300 dpi y el PDF, 425,20 × 241,80 pt.

| Archivo | sha256 |
|---|---|
| `generar_figura_segmentacion_ejemplo.py` | `132beccd87b918c300c47395c1999694864fb57c58d05801f909a33a3db89aa8` |
| `figura_segmentacion_ejemplo.svg` | `a0bde1d970bc07199a7a403ea9bac74a630e71178269fc304cd5c21df192eb58` |
| `figura_segmentacion_ejemplo.png` | `6058e476ec3a0277630dd959deece9781efcb679daa2003f3ac483a26e36c35e` |
| `figura_segmentacion_ejemplo.pdf` | `4a4213d5fc9d2273d3b45dfa663d9118ef279ae5988fa554189fe9713d7daa9e` |

Determinismo. Corrí el generador tres veces con `--salida` en el scratchpad,
con `PYTHONHASHSEED` 0, 1 y 4242, y una cuarta en el repo. Los cuatro SVG, PNG
y PDF son idénticos (`cmp`) y las cuatro consolas también. El PDF es
reproducible porque `rsvg-convert` corre con `SOURCE_DATE_EPOCH=0`.

Entrada a git. El generador, el SVG, el PNG y el PDF entran por las excepciones
`.gitignore:208`, `:187`, `:186` y `:188`. Este LEEME cae bajo `.gitignore:180`
(`docs/tesis/figuras/*`), como los demás LEEME de figuras, y entra forzado con
`git add -f`. Lo comprobé con `git check-ignore -v --no-index`.

## 8. Epígrafe propuesto

> Segmentación del punto 5.1.1 de Clasificación de deudores, con el fragmento
> de la página 16 del documento a la izquierda y las unidades de extracción
> que produce a la derecha. El párrafo propio del punto forma una unidad y cada
> subpunto forma otra, y cada flecha parte del tramo del documento del que
> sale su unidad. La unidad del 5.1.1.1 se muestra abierta, con su texto propio
> precedido por la cadena estructural que hereda, en gris, de la sección 5, del
> 5.1 y del 5.1.1, y las otras dos se muestran cerradas.

Lo decide la autora.

## 9. Observaciones

1. **La página.** La figura dice «página 16» y «Páginas: 16». Es la página del
   PDF, que es la que registra la segmentación (el campo de páginas de las
   unidades y la página del 5.1.1 en la estructura, contadas desde 1). El pie
   impreso de esa página dice «Página 1»: cuenta las páginas dentro de la
   sección 5 (`seg/pies_cla.json:239-251`; el registro de la figura de la
   página del ejemplo, `LEEME_figura_pagina_to.md:118-122`, lo explica). La
   figura de cómo se forma un Texto Ordenado sigue la misma convención («pág.
   16», `generar_figura_formacion_to.py:675`). Si el texto de la sección cita
   la página, tiene que ser con esta convención. (El registro de esa figura
   lo anota en `LEEME_figura_formacion_to.md:106`.)
2. **El título del 5.1.1 en el fragmento.** El fragmento empieza con el título
   del punto, porque así aparece en el documento. No lleva llave, porque no da
   una unidad propia: entra en la cadena de las tres unidades, como último
   bloque de la del 5.1.1.1. La unidad del párrafo lo lleva solo como título
   (`seg/chunks_cla.json:2659-2661`).
3. **El párrafo, en dos renglones.** En el documento, el párrafo del 5.1.1 es
   una sola línea (línea 7), que no entra en el ancho de la hoja. La figura lo
   dibuja completo, partido en un blanco, y el control comprueba que los dos
   renglones unidos den el texto.
4. **El 5.1.1.1 en el fragmento.** Su primera línea es su título, que entra
   entera y va sin «…», aunque el subpunto sigue cuatro líneas más (9 a 12).
   La tarjeta abierta muestra que el texto sigue.
5. **Resumen de subpuntos.** No aplica: el 5.1.1 tiene dos subpuntos.
