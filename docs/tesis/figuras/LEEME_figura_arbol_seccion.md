# figura_arbol_seccion — registro de generación (versión 2)

Figura «la sección 5 de Clasificación de deudores como árbol» para el análisis
del documento (capítulo 3). La sección 5 («Sección 5. Categorías de carteras.»)
y sus nueve puntos como árbol con sangría, cada punto en una caja con su número
y su título tal como figuran en E0, el título cortado en una palabra entera y
con «…» cuando se corta (sección 3). Dos estilos de caja, con leyenda: punto
contenedor (relleno gris azulado, borde oscuro) y punto terminal (blanco, borde
gris). Los contenedores con párrafos sin numerar llevan una marca «¶» dentro de
su caja. Los puntos 5.1.1 y 5.1.1.1, los del ejemplo del préstamo, llevan un
contorno naranja. Debajo, la leyenda. La imagen no lleva nombres de archivo,
rutas ni identificadores internos, y ningún texto ni trazo queda a menos de 2
mm de un borde.

«Punto contenedor» (un punto con subpuntos), «punto terminal» (uno sin
subpuntos) y «párrafo sin numerar» (el que un contenedor tiene antes o después
de sus subpuntos) son nombres de este trabajo, no del BCRA, los mismos de la
figura de la página del ejemplo.

**Tamaño efectivo a 15 cm de ancho** (todo el texto es propio de la figura):

| Qué | Lienzo | Impreso |
|---|--:|--:|
| encabezado de la sección, números y títulos de los puntos | 14 unidades | **8,27 pt** |
| marca «¶» y leyenda | 13 unidades | **7,68 pt** |

Mínimo del repo para texto propio: 7 pt; los 27 textos lo cumplen. **Alto: 8,66
cm** (lienzo 720 × 415,5 unidades; el PDF 425,2 × 245,5 pt; el PNG 1772 × 1024
px a 300 dpi). **Margen mínimo a los bordes: 2,29 mm** en los cuatro; exigido 2
mm.

Historia (las dos el 30/09/2026 en U-CAP3-FIGS; ninguna commiteada al escribir
esto):

- Versión 1: el título de E0 entero, con los cortes de línea del documento
  («… para la ad-», «… del im-»), una nota en la leyenda que lo explicaba, y el
  encabezado de la sección y la leyenda pegados al borde izquierdo. sha256:
  generador `25be7291118c3a726c95bbfdf21f58d1f9d90bc9ab7880f5cdb45e1215f9a64a`,
  PNG `366f78d4b150d0011d59d6c5e21271b1780e7e162cf949065b65fdb0f0464095`, PDF
  `975fc8f2d5e0e2dcb91ada654c390aaab50e7fb4a9095d063091309c27e4b125`, LEEME
  `690572ca782802a9857ceab3f7928bda2314ea27c7e02ba664098a58d92bd151`.
- Versión 2 (esta), con los cambios de la revisión: títulos cortados en
  palabra entera con «…», sin la nota de la leyenda, y margen de 2 mm a los
  cuatro bordes, controlado por el script.

## 1. Cómo regenerar

Desde la raíz del repo:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_arbol_seccion.py
```

Escribe `figura_arbol_seccion.png` y `figura_arbol_seccion.pdf`. El SVG es
intermedio y solo se escribe con `--svg <ruta>`. Los controles de geometría
corren siempre.

Herramientas de la corrida registrada (30/09/2026): `rsvg-convert` 2.62.3
(cairo 1.18.4), y en el `.venv` del repo (Python 3.10.13) pdfplumber 0.11.10,
Pillow 12.3.0 y pypdf 6.10.2. Reutiliza por importación
`generar_figura_norma_a_grafo.py` (sha256
`9b0e45a299a0a078d250ccc999d192cbb83038bd8c00baa6bd8972d021b73f3d`) y
`generar_figura_proceso_extraccion.py` (sha256
`6a91931abeb9927842f76fa50471497e926c69fc56617c62ef7f05ddf6c010d6`), los dos
del commit `fbe69d4`.

## 2. Fuentes

| Fuente | sha256 | Ancla |
|---|---|---|
| E0, `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/estructura_cla.json` | `3cd26083fee7355ef3d8027ac353a744c2f1cfa35830535fe1be2b9505eaf917` | commit `d082812`; la sección 5 empieza en `:1166` |
| E0, `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json` | `98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1` | commit `d082812` |
| PDF del corpus, `data/experiment/subset/TO_clasificacion_deudores_actual.pdf` | `6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2` | fuera de git (`.gitignore:35`); solo contraste |

## 3. Qué dato sale de qué fuente

| Elemento de la figura | Fuente |
|---|---|
| «Sección 5. Categorías de carteras.» | `estructura_cla.json`: `numero` y `titulo` de la sección (`:1166-1167`), con el prefijo «Sección»; comprobado como línea de la página 16 del PDF |
| Los nueve puntos, su orden y su anidamiento | `estructura_cla.json`: campo `hijos`, en orden de documento |
| Número y título de cada punto | `estructura_cla.json`: `numero` (sin el punto final que lleva en el PDF) y `titulo`, cortado por la regla de abajo |
| Contenedor o terminal | `estructura_cla.json`: contenedor si `hijos` no está vacío; contrastado con `chunks_cla.json` (un chunk `punto_terminal` por terminal, ninguno por contenedor) |
| Marca «¶» | `chunks_cla.json`, por la regla de abajo; contrastada con los segmentos `intro`/`cierre` de `estructura_cla.json` |
| Resaltado de 5.1.1 y 5.1.1.1 | los puntos del ejemplo (decisión 1 del mandato); el script comprueba que sean puntos de la sección |
| Leyenda | texto fijo del script |

**Regla de la marca** (declarada en el script como `REGLA_MARCA`, antes de la
función que la aplica): un punto contenedor lleva la marca si E0 tiene para él
al menos un bloque de párrafo sin numerar, es decir, un chunk de tipo
`mini_chunk` cuya `unidad` es el número del punto, con `rol_bloque` `intro`
(antes de sus subpuntos) o `cierre` (después). En la sección 5 la cumplen los
tres contenedores, los tres con `intro`: `cla::5.1::intro` («La cartera se
agrupará en dos categorías básicas:», `chunks_cla.json:2587`),
`cla::5.1.1::intro` («Abarca todas las financiaciones comprendidas, con
excepción de las siguientes:», `:2628`) y `cla::5.1.2::intro` («Comprende:»,
`:2805`). Ninguno tiene `cierre`.

Resultado: 9 puntos, 3 contenedores (5.1, 5.1.1, 5.1.2; los 3 con marca) y 6
terminales (5.1.1.1, 5.1.1.2, 5.1.2.1 a 5.1.2.4), según la salida del script.

**Títulos** (regla de `titulo_mostrado`, declarada en el script). El título de
E0 de cada punto es el resto de su primera línea en el PDF, así que el de los
puntos sin título propio termina donde termina la línea. El título mostrado se
corta en una palabra entera: se quita la palabra final si termina en guion (la
que el documento divide al final de la línea) y, si no entra en una línea de la
caja hasta el margen derecho, las palabras finales que sobran. Lleva «…» si se
quitó alguna palabra o si no termina en punto, es decir, si la oración que abre
el punto sigue en el documento. Resultado, según la salida del script:

| Punto | Título mostrado | «…» |
|---|---|---|
| 5.1, 5.1.1, 5.1.1.1, 5.1.2, 5.1.2.2 | el título de E0 entero (termina en punto) | no |
| 5.1.1.2 | «A opción de la entidad, las financiaciones de naturaleza comercial de hasta el…» | la oración sigue en el documento |
| 5.1.2.1 | «Créditos para consumo (personales y familiares, para profesionales, para la…» | palabra dividida con guion («ad-») |
| 5.1.2.3 | «Préstamos a Instituciones de Microcrédito –hasta el equivalente al 40 % del…» | palabra dividida con guion («im-») |
| 5.1.2.4 | «Las financiaciones de naturaleza comercial de hasta el equivalente a dos veces…» | la oración sigue en el documento |

Ningún título se corta por ancho: los nueve entran en una línea. El script
comprueba, para cada punto, que el texto mostrado sin «…» sea un prefijo de la
primera línea del punto en su página del PDF (la línea que abre con su número),
que termine en una palabra entera (el carácter que sigue en la línea es un
blanco, o la línea termina ahí) y que no termine en guion; y, cuando el «…» se
debe solo a que no termina en punto, que el punto sea terminal y que su chunk
de E0 tenga más de una línea.

**Colapso.** La regla del mandato (más de 25 puntos: el 5.1 completo y los
demás de primer nivel colapsados con la cantidad de puntos que contienen) está
implementada (`UMBRAL_COLAPSO`, función `filas`) pero no se ejercita: la sección
5 tiene 9 puntos y se muestra completa. La probé fuera del repo sobre la
sección 6 (58 puntos): muestra el 6.1 y colapsa 6.3 (3 puntos), 6.4 (4) y 6.5
(45); los terminales de primer nivel (6.2, 6.6) quedan como están.

## 4. NO ENCONTRADO

Nada: todo lo que la figura dibuja está en E0 y en el PDF.

## 5. Candados y controles

El script frena (`SystemExit`) si:

- el sha256 del PDF, de `estructura_cla.json` o de `chunks_cla.json` no es el
  fijado, o la sección 5 no aparece exactamente una vez;
- para algún punto, la estructura y los chunks no coinciden en si es terminal,
  la marca de los chunks no coincide con los segmentos `intro`/`cierre` de la
  estructura, o un terminal tiene párrafo sin numerar;
- el encabezado de la sección no es una línea de su página, o la página de
  algún punto no es de la sección;
- un punto resaltado no es de la sección;
- un título mostrado no pasa las comprobaciones de la sección 3, o no entra en
  una línea ni con una sola palabra;
- **geometría** (métricas reales de Helvetica; 27 textos, 18 cajas, 25 marcas,
  0 fallas): un texto por debajo de 7 pt impresos, fuera del lienzo,
  superpuesto a otro, fuera de su caja, cortado por el borde de otra caja o
  tocado por una marca (conectores del árbol, contornos naranja); o dos cajas de
  puntos que se tocan;
- **margen** (61 elementos: los 27 textos, medidos con las métricas reales, y
  34 dibujados leídos del SVG, 21 rectángulos y 13 trazos, con medio grosor de
  trazo): un elemento a menos de 2 mm (`MARGEN_MM`; 9,6 unidades de lienzo) de
  uno de los cuatro bordes. Mínimos de la corrida registrada: 11,0 unidades
  (2,29 mm) en los cuatro. Prueba negativa, fuera del repo: con el borde
  izquierdo de la versión 1 (x = 4) el control da 3 fallas (el encabezado de la
  sección y los dos tramos del conector de la raíz).

Verificación adicional con `docs/tesis/figuras/verificar_geometria_svg.py` sobre
el SVG guardado con `--svg`: 27 textos, 0 nodos, 0 trazos con flecha, 0 fallas.

## 6. Composición

Lienzo de 720 unidades para 15 cm, con 11 unidades (2,29 mm) de margen a los
cuatro bordes. Encabezado de la sección arriba, sin caja.
Una fila por punto cada 32 unidades, cajas de 24 de alto y ancho ajustado al
texto (medido con la tabla de métricas del script; el control usa las métricas
reales); sangría de 26 unidades por nivel. Conectores en ángulo recto, en gris
(`#8a8a8a`), de cada padre a sus hijos por la izquierda de las cajas; el
conector llega al contorno naranja cuando el hijo está resaltado. Contenedor:
relleno `#e1e7ee`, borde `#4a5a6a` (la paleta de las figuras hermanas); terminal:
blanco, borde `#999999`; marca: casilla blanca con «¶» en `#4a5a6a`, dentro del
borde derecho del contenedor; resaltado: contorno `#e07b39` a 3,5 unidades de la
caja. Leyenda en un recuadro gris claro, dentro del margen, en dos columnas.

## 7. Salidas y reproducibilidad

| Archivo | sha256 |
|---|---|
| `generar_figura_arbol_seccion.py` | `9848e106987fe3c22d31b5876ef6efb3d28fac92a2e814126e729bffb6ee3736` |
| `figura_arbol_seccion.png` (1772 × 1024 px, 300 dpi) | `6c4ec705d93b76dc01942d8e16210010567ac0cba67ce5722cd7e6889d553e13` |
| `figura_arbol_seccion.pdf` (425,2 × 245,5 pt) | `773016308c50af55af3df30a8fe672573ce046e05ee34331367739abd5670514` |
| SVG intermedio (no se versiona) | `b880ed64e85c7d3bd5ed6293575906d9ae677e3637c1b7ffca9ec48cdceff063` |

Dos corridas con `PYTHONHASHSEED` 0 y 1, separadas por cinco segundos: el SVG,
el PNG y el PDF salieron idénticos byte a byte, y la salida de consola también
(salvo la ruta del SVG). PDF reproducible con `SOURCE_DATE_EPOCH=0`
(`/CreationDate` 01/01/1970). Stream de contenido de la página del PDF, sha256
`f797cf9ca7f90d74babea8cb8ef0c305bba902336331ae2fc17dff52ad47bbee`.
