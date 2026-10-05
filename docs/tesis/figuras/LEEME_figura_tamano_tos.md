# figura_tamano_tos — registro de generación (versión 2)

Figura «el tamaño de los Textos Ordenados» para el análisis del documento
(capítulo 3). Las páginas de cada uno de los 157 Textos Ordenados (los 152 del
corpus más los 5 del conjunto de desarrollo), una barra por documento,
ordenados de mayor a menor, en escala logarítmica, con un color por clase
(normativa general, régimen informativo) y leyenda con la cantidad de cada
una. Rotulados el más grande, como «Manual de cuentas (régimen informativo)»
con sus 2.037 páginas (su título completo en el inventario del corpus es «RI -
Manual de Cuentas vigente al 31/12/17.», `inventario_tos.csv:110`), y
Clasificación de deudores (60 páginas), por su título tal como figura en el
inventario. Debajo del eje, el total: «157 Textos Ordenados, de mayor a menor;
7.321 páginas en total». La imagen no lleva nombres de archivo, rutas ni
identificadores internos, y ningún texto ni trazo queda a menos de 2 mm de un
borde.

**Tamaño efectivo a 15 cm de ancho** (todo el texto es propio de la figura):

| Qué | Lienzo | Impreso |
|---|--:|--:|
| rótulos de los dos documentos y leyenda | 14 unidades | **8,27 pt** |
| marcas y títulos de los ejes | 13 unidades | **7,68 pt** |

Mínimo del repo para texto propio: 7 pt; los 12 textos lo cumplen. **Alto: 7,37
cm** (lienzo 720 × 353,9 unidades; el PDF 425,2 × 208,9 pt; el PNG 1772 × 871 px
a 300 dpi). Cada barra ocupa 4,20 unidades (0,87 mm). **Margen mínimo a los
bordes: 2,19 mm** (derecho; izquierdo e inferior 2,29 mm, superior 3,72 mm);
exigido 2 mm.

Historia (las dos el 30/09/2026 en U-CAP3-FIGS; ninguna commiteada al escribir
esto):

- Versión 1: el más grande rotulado con su título del inventario, «RI - Manual
  de Cuentas vigente al 31/12/17.»; el título del eje vertical a 8 unidades del
  borde izquierdo y la grilla y el eje a 3,5 unidades del derecho (con medio
  grosor de trazo). sha256: generador
  `c9efb3ccfdfa443cffcee0a66a344194fbbc71732b9e3634306baed3dc6c47d0`, PNG
  `9af78c7f8267d743a51c387d421921bc20455cc61216733a065fa7d18309ab1d`, PDF
  `f92729f8f5e1a542600895fff3479837524d0a1e47a944a9c2edd1f33de97fb4`, LEEME
  `6ad3854092ea1e5738409650058173ce4b36de2300d1eba83070ec72e4806395`.
- Versión 2 (esta), con los cambios de la revisión: el rótulo «Manual de
  cuentas (régimen informativo)» y margen de 2 mm a los cuatro bordes,
  controlado por el script.

## 1. Cómo regenerar

Desde la raíz del repo:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_tamano_tos.py
```

Escribe `figura_tamano_tos.png` y `figura_tamano_tos.pdf`. El SVG es intermedio
y solo se escribe con `--svg <ruta>`. Los controles de geometría corren
siempre.

Herramientas de la corrida registrada (30/09/2026): `rsvg-convert` 2.62.3
(cairo 1.18.4), y en el `.venv` del repo (Python 3.10.13) Pillow 12.3.0 y pypdf
6.10.2. Reutiliza por importación `generar_figura_norma_a_grafo.py` (sha256
`9b0e45a299a0a078d250ccc999d192cbb83038bd8c00baa6bd8972d021b73f3d`) y
`generar_figura_proceso_extraccion.py` (sha256
`6a91931abeb9927842f76fa50471497e926c69fc56617c62ef7f05ddf6c010d6`), los dos
del commit `fbe69d4`.

## 2. Fuentes

| Fuente | sha256 | Ancla |
|---|---|---|
| `reports/u_insumos_cap/estadisticas_corpus.json` | `1630d1de9f5c065eec00a237f2ba21ff43e4ee11e9332409c56593b12ccbe6ab` | commit `ded3494`; `por_to` de `corpus_152` en `:1593` y de `desarrollo_5` en `:6246` |
| `data/experiment/escalado_prep/inventario_tos.csv` (152 filas) | `a1db24fd2beaed2110349f295e7928bc0cd9d18333cce527773233a156a37e1f` | commit `111ed19`; el mismo sha declara `estadisticas_corpus.json` en `fuentes_principales` (`:7219`) |
| `data/experiment/escalado_prep/inventario_resumen.json` | `d60e65abda005433ac5d13c367b55fd40efa3124b1c698e1633f6fc1bd306f82` | commit `111ed19`; ídem |

## 3. Qué dato sale de qué fuente

| Elemento de la figura | Fuente |
|---|---|
| Una barra por documento, su altura | campo `paginas` de cada entrada de `por_to` de `corpus_152` (152) y de `desarrollo_5` (5) |
| Color de la barra | campo `categoria` de la misma entrada (`normativa_general`, `regimen_informativo`) |
| Orden | de mayor a menor por páginas; a igual cantidad de páginas, por identificador, para que el orden no dependa de la lectura (Clasificación de deudores queda en el puesto 23 de 157; hay otros dos documentos de 60 páginas) |
| «Manual de cuentas (régimen informativo)» y «2.037 páginas» | rótulo fijo del script (`ROTULO_MAYOR`), de la revisión de la versión 1, para el documento de más páginas (`estadisticas_corpus.json:3077`, 2.037); el script comprueba que su título en el inventario, «RI - Manual de Cuentas vigente al 31/12/17.» (`inventario_tos.csv:110`, campo `titulo_oficial`), diga «Manual de Cuentas» y que su clase sea régimen informativo, y lo imprime completo |
| «Clasificación de deudores» | `inventario_resumen.json:16-17`, `subset_excluido`: los cinco del conjunto de desarrollo no están en el CSV, y el resumen del mismo inventario da su título; páginas en `estadisticas_corpus.json:6290` (60) |
| Cantidades de la leyenda (103, 54) y total del eje (157; 7.321) | recomputados por el script (sección 4) |
| Nombres de las clases, títulos de los ejes | texto fijo del script |

La «clase» del mandato es el campo `categoria` de la estadística; el campo que
esa estadística llama `clase` es otra cosa (la clase de segmentación:
`reconocido_pleno`, `parcial_declarado` o `no_segmentable_declarado` en el
corpus de 152, vacía en el conjunto de desarrollo) y la figura no lo usa.

Las barras parten de 0,5 páginas, debajo de la marca 1 del eje, para que los
documentos de una página se vean; el eje llega a 3.000. Marcas en 1, 10, 100 y
1.000, con líneas de grilla finas.

## 4. Totales por clase, recomputados por el script

| Clase | Documentos | Páginas | Mínimo | Mediana | Máximo |
|---|--:|--:|--:|--:|--:|
| Normativa general | 103 | 3.827 | 5 | 25 | 204 |
| Régimen informativo | 54 | 3.494 | 1 | 9 | 2.037 |
| **Total** | **157** | **7.321** | 1 | 22 | 2.037 |

Dan 103 y 54 documentos y 7.321 páginas, lo que pide el mandato; si no, el
script frena. Contraste con la misma estadística: 99 + 4 = 103 y 53 + 1 = 54
(`R1_tos_por_categoria` de cada conjunto, `estadisticas_corpus.json:369-372` y
`:6047-6050`), y 6.757 + 564 = 7.321 páginas (`R2_paginas_total`, `:393` y
`:6065`). La mediana de régimen informativo es la de 54 valores (el promedio de
los dos centrales, los dos 9).

## 5. NO ENCONTRADO

Nada. Un apartamiento de la letra del mandato, que reporto: el título de
Clasificación de deudores no sale del CSV del inventario, que tiene solo los
152 del corpus, sino del resumen del mismo inventario (`subset_excluido`), que
es donde el inventario registra los cinco del conjunto de desarrollo.

## 6. Candados y controles

El script frena (`SystemExit`) si:

- el sha256 de la estadística, del CSV del inventario o de su resumen no es el
  fijado, o la estadística no declara esos dos archivos del inventario con ese
  sha en `fuentes_principales`;
- en algún conjunto, `por_to`, `ids` y `tos` no coinciden, o la suma de
  páginas no es su `R2_paginas_total`;
- para algún documento, `paginas` no es `sonda_paginas`, la clase no es una de
  las dos, no está en el inventario (o en su resumen), o su clase no es la del
  CSV;
- el inventario y el corpus de 152, o el resumen y el conjunto de desarrollo,
  no tienen los mismos documentos, o hay documentos repetidos;
- los totales no dan 103, 54 y 7.321 (**FRENO**);
- el más grande no es único, su título del inventario no dice «Manual de
  Cuentas» o su clase no es la del rótulo, o la línea guía no llega a la barra
  de Clasificación de deudores;
- **geometría** (métricas reales de Helvetica; 12 textos, 165 marcas, 0
  fallas): un texto por debajo de 7 pt impresos, fuera del lienzo, superpuesto
  a otro, o tocado por una barra, una línea de la grilla, el eje, una muestra
  de la leyenda o la línea guía;
- **margen** (177 elementos: los 12 textos, medidos con las métricas reales, y
  165 dibujados leídos del SVG, 159 rectángulos, que son las 157 barras y las 2
  muestras de la leyenda, y 6 trazos, que son las 4 líneas de la grilla, el eje
  y la línea guía, con medio grosor de trazo): un elemento a menos de 2 mm
  (`MARGEN_MM`; 9,6 unidades de lienzo) de uno de los cuatro bordes. Mínimos
  de la corrida registrada: izquierdo 11,0 unidades (2,29 mm), superior 17,9
  (3,72 mm), derecho 10,5 (2,19 mm, la grilla y el eje con medio grosor de
  trazo) e inferior 11,0 (2,29 mm). Prueba negativa, fuera del repo: con el
  borde derecho de la versión 1 (el área del gráfico hasta x = 716) el control
  da 7 fallas.

Verificación adicional con `docs/tesis/figuras/verificar_geometria_svg.py` sobre
el SVG guardado con `--svg`: 12 textos, 0 nodos, 0 trazos con flecha, 0 fallas.

## 7. Colores

Normativa general `#2a78d6` (azul) y régimen informativo `#1baf7a`
(aguamarina): los lugares 1 y 3 de la paleta categórica validada de la guía de
gráficos que usé para esta figura. El lugar 2, naranja, queda fuera porque las
figuras de la tesis reservan el naranja a las remisiones y al resaltado del
ejemplo. El par pasa el validador de paleta de esa guía (`validate_palette.js`,
externo al repo, corrido el 30/09/2026 con `--mode light`): banda de
luminosidad, croma, separación para daltonismo ΔE 23,1 (protan), visión normal
ΔE 24,0; el aguamarina tiene contraste 2,74:1 con el fondo (aviso, no falla),
compensado con la leyenda y los rótulos en tinta y con la tabla de la sección
4. La salida del validador va en el paquete de revisión. Grilla, eje y línea
guía en los grises de la misma guía (`#e1e0d9`, `#c3c2b7`, `#898781`).

## 8. Salidas y reproducibilidad

| Archivo | sha256 |
|---|---|
| `generar_figura_tamano_tos.py` | `1d4ae9fc2ed04390a66735224779aaf3406538eb41889acff081b1c57ac8e81b` |
| `figura_tamano_tos.png` (1772 × 871 px, 300 dpi) | `90a6f406e92c042e6c20479a4550b2d2b0cb22b9eb347533c5aebea77b30e385` |
| `figura_tamano_tos.pdf` (425,2 × 208,9 pt) | `a4a3c5f1468040277414e3a8cd3824297d2414d7e7513fbb27fa5a279abe4600` |
| SVG intermedio (no se versiona) | `c614a0ca7fcf8d54c3fc3cc2c48d25ce801ede82ecfeeb6be7fa640954696680` |

Dos corridas con `PYTHONHASHSEED` 0 y 1, separadas por cinco segundos: el SVG,
el PNG y el PDF salieron idénticos byte a byte, y la salida de consola también
(salvo la ruta del SVG). PDF reproducible con `SOURCE_DATE_EPOCH=0`
(`/CreationDate` 01/01/1970). Stream de contenido de la página del PDF, sha256
`ad3e9123214cb6573374230c45516ec9706ddcf58bec8ac5358973921554c164`.
