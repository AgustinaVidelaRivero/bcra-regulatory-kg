# figura_comparacion — registro de generación

## Versión del 05/11/2026

Esta sección reemplaza lo que el resto del LEEME diga distinto, incluida la versión del 29/10/2026 (textos y sha256). Parte de esa versión: script `1b75dd15c61dc769524f6c2ec508b4a0061f697d897b35a8f44f07cec9247511`, PNG `c02cfeba81270ecd6266bc69d94ffe4b3a1a4ae8735e33d7bcfeda7e9215d174`.

Cambio en lo dibujado: «principal» pasa a «combinada» en 3 cajas: «Configuración combinada» (`:89`), «Fidelidad de cada pregunta, con la combinada» (`:93`) y «Grafo contra la combinada» (`:95`). Las claves internas (`agente_principal`, `fidelidad_principal`, `contra_principal` y `CONFIGURACIONES`) no cambian, y por eso el SVG las sigue llevando en `data-caja` y `data-flecha`.

El título de la caja de la fidelidad ocupa ahora 4 renglones en vez de 3: la caja pasa de 76 a 94 unidades de alto, centrada en su fila. Ninguna otra caja ni flecha cambia. El SVG tiene 60 textos en vez de 59.

Comando sin cambios, con el `generar_figura_proceso.py` que dice «Reglas fijas» junto al script. Con el del commit `73f4bc4e`, que dice «Pieza de código» en su renglón 279, se detiene con `ALTO [formato]` y no escribe nada.

Resultado: lienzo 760 × 446 (sin cambios), PNG 1772 × 1040 px, sha256 `2e0154bfb5cf215eb925fab193d98fcc432324c2fbd846fb6441a9a9e5eaa3a7`; SVG, sha256 `c25dfa387e856d95ab1ebb8f6db078ca3f75393c94afd35ef7944495e643d04f`; dos corridas iguales. Script: sha256 `b7f1c93d904e003ea4d1c8adcd05e757ef11497afa08ed2008344f3ab266693c`.

## Versión del 29/10/2026

Esta sección reemplaza lo que el resto del LEEME diga distinto (textos, tamaño, sha256).

Cambio en lo dibujado: la leyenda de «codigo» pasa de «Pieza de código» a «Reglas fijas» (`:157`). La leyenda de «codigo» dice «Reglas fijas» en `generar_figura_proceso.py:279`; la figura la coteja con esa línea. Nada más.

Comando sin cambios, con el `generar_figura_proceso.py` nuevo junto al script.

Resultado: lienzo 760 × 446 (sin cambios), PNG 1772 × 1040 px, sha256 `c02cfeba81270ecd6266bc69d94ffe4b3a1a4ae8735e33d7bcfeda7e9215d174`; dos corridas iguales. Script: sha256 `1b75dd15c61dc769524f6c2ec508b4a0061f697d897b35a8f44f07cec9247511`.

Figura del diseño de la comparación del capítulo 5: cómo se comparan las
respuestas del agente que consulta el grafo con las del mismo agente cuando
consulta los fragmentos de los documentos, en sus 2 configuraciones. Es un
diagrama de cajas y flechas que se lee de izquierda a derecha: las preguntas
con sus criterios, las mismas para los 3; el agente con el grafo y el agente
con los fragmentos en la configuración combinada y en la densa, uno debajo del
otro; el juez de las respuestas, el mismo para los 3, que abarca las 3 filas;
la fidelidad de cada pregunta con cada uno; el grafo contra la combinada y
contra la densa; la corrección de Holm y, debajo de ella, la decisión.

Es un diagrama del método, sin datos: el script no lee datos, registros ni
resultados de la evaluación. Todo lo que dibuja está escrito en el script
(tablas `CAJAS` y `FLECHAS`). Ninguna caja lleva número de sección ni nombra
un modelo. Las cifras que aparecen («3», «0,025», «0,05» y «2») son texto de
la tesis.

## 1. Cómo se regenera

Desde la raíz del repositorio, con el script en `docs/tesis/figuras/`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B docs/tesis/figuras/fig_comparacion.py
```

Escribe `figura_comparacion.png` junto al script. Opciones: `--salida
<directorio>` (otro lugar para el PNG), `--svg <ruta>` (guarda también el SVG)
y `--formato <ruta>` (el `generar_figura_proceso.py` con el que se coteja el
formato; por omisión, el que está junto al script, si está).

Herramientas: Python 3, solo la biblioteca estándar (corrido con Python
3.12.13), y `rsvg-convert` 2.62.3 (cairo 1.18.4, pango 1.58.2) para el PNG,
las mismas versiones que registra el mapa de la evaluación. El script no
importa ni ejecuta código del repositorio, no usa red ni API y no lee ningún
archivo, salvo, como texto, `generar_figura_proceso.py` para el cotejo del
formato. Escribe el PNG en la carpeta del script, sea cual sea la carpeta
desde la que se lo corre.

En la carpeta de trabajo, fuera del repositorio, se corrió con la ruta del
script en esa carpeta (`python3 -B fig_comparacion.py`, con
`PYTHONDONTWRITEBYTECODE=1`). La corrida desde la raíz del repositorio, con la
ruta de arriba, está NO VERIFICADA, y también la corrida con el
`.venv/bin/python` del repositorio. El script no usa nada fuera de la
biblioteca estándar.

## 2. Composición

- Seis columnas, de izquierda a derecha: las preguntas; los 3 agentes; el
  juez; las 3 fidelidades; las 2 comparaciones; la corrección de Holm con la
  decisión debajo.
- La decisión va debajo de la corrección de Holm, con una flecha vertical,
  porque las 7 columnas no entran en una fila a 15 cm con la letra del mapa.
  Con cada caja al ancho de su palabra más larga, las 7 cajas suman 651
  unidades y, con las 6 separaciones de 20, 771; el lienzo tiene 736 entre
  márgenes.
- Las configuraciones van de arriba abajo en el orden combinada, grafo, densa
  (`CONFIGURACIONES`). Con el grafo en el medio, cada comparación queda entre
  sus 2 filas, las 4 flechas que llegan a las comparaciones son horizontales y
  ninguna flecha cruza a otra. Con el grafo arriba, la flecha de la fidelidad
  del grafo a la comparación con la densa cruzaría a la de la combinada.
- El juez abarca el alto de las 3 filas. La flecha de cada agente entra al
  juez en la fila del agente, y la de cada fidelidad sale en la misma fila.
- Las preguntas van a la altura del agente con el grafo. Su flecha a ese
  agente es recta, y las otras dos salen por arriba y por abajo de la caja.
- Las flechas que salen de las preguntas, los datos de entrada, llevan el
  grosor de las entradas del mapa (`GROSOR_RAMA`). Las demás llevan el de su
  línea principal (`GROSOR_FLUJO`).
- Ninguna flecha atraviesa una caja ni cruza a otra, ningún tramo va hacia la
  izquierda y ninguna caja de destino empieza a la izquierda de su origen.
- La leyenda va abajo a la izquierda, debajo de las cajas que tiene encima,
  con las 3 clases del mapa y, después de «Datos», la de resultado. La
  decisión baja, a la derecha, hasta la altura de la leyenda.

Lienzo de 760 × 446 unidades, impreso a 15,00 × 8,80 cm. El PNG mide
1772 × 1040 px a 300 dpi.

## 3. Formato: de dónde sale cada valor

`E` es `fig_evaluacion.py`, el script del mapa de la evaluación (sha256
`34b18970e3f282d0ba17e211e5bf0098c18d2c48b95dd5d60f694d14a63894cd`); sus
líneas son las de ese archivo. `P` es
`docs/tesis/figuras/generar_figura_proceso.py` en el commit
`02f61cb050e43d752d89578574a6a1298d081e13` (sha256
`8667c219fe5586466e3cad04bc81843a8b39025d59b443edbacf79740349cbbf`, el mismo
del que `E` toma los valores). Cada valor está copiado en el script con sus dos
líneas en un comentario, y la tabla `FORMATO` coteja con `P` los 35 que vienen
de ahí (§6).

| Valor | En esta figura | Fuente |
|---|---|---|
| Biblioteca estándar y `rsvg-convert`; PNG con `rsvg-convert -w 1772 -f png` | todo el script; `exportar` | E:64-76, E:1154-1162 |
| Densidad del PNG, 300 dpi (bloque pHYs después de IHDR) | `con_densidad` | E:1134-1151 (P:1190-1211) |
| Métrica del texto: tablas AFM de Helvetica y Helvetica-Bold | `_AFM` | E:290-304 (P:335-349) |
| `W = 760` (unidades para 15 cm) | lienzo | E:172 (P:163) |
| `ANCHO_CM = 15.0`, `DPI = 300`, 1772 px | ancho impreso y del PNG | E:195-196, E:215 (P:311, P:313) |
| `TIPOGRAFIA = "Helvetica,Arial,sans-serif"` | `font-family` del SVG | E:173 (P:164) |
| `MODELO` (#fbe3d3 / #e07b39) | cajas naranjas: lo que ejecuta un modelo de lenguaje | E:174 (P:165) |
| `DETERMINISTICA` (#e1e7ee / #4a5a6a) | cajas azules: código y reglas fijas | E:175 (P:166) |
| `NEUTRO` (#fafafa / #999999) | cajas grises: datos y resultado | E:176, E:212 (P:167) |
| `TINTA, TINTA_SUB` (#1f1f1f, #444444) | primera línea en `TINTA`; segunda en `TINTA_SUB`; leyenda en `TINTA` | E:177 (P:168) |
| `FLECHA` (#555555) | trazos y puntas | E:178 (P:169) |
| `FS_TITULO, FS_TEXTO = 14, 13` | primera línea 14 en negrita; segunda línea 13 normal; leyenda 13 | E:179 (P:171) |
| `IL = {14: 18, 13: 17}` | interlíneas | E:180 (P:172) |
| `SEP_TITULO = 5` | de la primera línea a la segunda | E:181 (P:173) |
| `PAD_X, PAD_Y = 9, 11` | márgenes internos | E:182 (P:174) |
| ancho y alto de caja: texto + 2 × `PAD_X` + 2, texto + 2 × `PAD_Y` | `ancho_caja`, `alto_caja` | E:389-396 |
| texto alineado a la izquierda en `x + PAD_X`, centrado en vertical en su caja | `textos_de` | E:601-614 |
| renglones: se llena cada línea hasta el ancho de su caja | `partir` | E:345-359 |
| `GROSOR_CAJA = 1.6` | borde de las cajas, salvo la de resultado | E:183 (P:175) |
| `GROSOR_FLUJO, GROSOR_RAMA = 1.8, 1.6` | flechas (§2) | E:184 (P:176) |
| `RADIO = 9` y la poligonal redondeada | esquinas de los trazos | E:185, E:1046-1060 (P:177) |
| `RX = 8` | esquinas de las cajas | E:186 (P:178) |
| `LEJOS_ESQUINA = RX + 4` | los extremos de las flechas, lejos de las esquinas | E:206 (P:325) |
| marcador de la punta (`MARCADOR_A`, `MARCADOR_B`) | punta de todas las flechas | E:190-191, E:207 (P:183-184) |
| `HUECO_PUNTA = 2.0` | del final del trazo al borde de la caja | E:202 (P:324) |
| `MARGEN = 12`, `MARGEN_MM = 2.0` | márgenes del lienzo | E:187, E:198 (P:180, P:316) |
| `PT_MINIMO = 7.0` | ninguna letra por debajo de 7 pt | E:197 (P:315) |
| `HOLGURA_TEXTO = 1.5`, `DISTANCIA_MIN = 3.0`, `SEP_CAJAS = 8.0` | holguras de los controles | E:199-201 (P:318-320) |
| `ASC, DESC = 0.78, 0.22` | caja de cada texto | E:203 (P:350) |
| un decimal en las coordenadas | `f` | E:321-323 |
| fondo blanco y cabecera del SVG | `dibujar` | E:1063-1072 |
| leyenda: textos de las 3 clases | `LEYENDA` | E:192-194 (P:278-280) |
| leyenda: marco `LEYENDA_MARCO`, muestras de 24 × 16 con `rx` 3, filas de 22, `GRUPO_LEYENDA = 10`, ancho y posición de muestras y textos | leyenda | E:188-189, E:204-205, E:585-588, E:620-636 (P:181-182, P:420, P:1123) |
| `SEP_FLECHA = 20`, `SEP_VERTICAL = 20`, `SOBRE_LEYENDA = 10`, `SEP_SIN_FLECHA` | separaciones entre cajas | E:409, E:411, E:414, E:416 |
| controles (contenido, trazado, cajas, cruces, textos, margen, registro) | `verificar` | E:790-1036, E:1101-1128 |

Agregados de esta figura:

- `GROSOR_DESTACADO = 1.5 × GROSOR_CAJA = 2.4`: el borde de la caja de
  resultado, para que se distinga de los datos, que comparten el gris.
- La entrada «Resultado» de la leyenda, después de «Datos» (`LEYENDA`), con
  la muestra gris (`NEUTRO`) y el borde de 2,4 de la clase.
- `ALTO_MAX_CM = 9.0`: el alto máximo de la figura.
- `FS_MINIMO = FS_TEXTO`: ninguna letra por debajo de 13 unidades (7,27 pt),
  la más chica del mapa.
- La leyenda va debajo de las cajas que tiene encima, no debajo de todo el
  dibujo (`armar`, en `encima`).

Medidas propias (no salen de otra figura): `ANCHO_TEXTO`, el ancho del texto
de cada caja, que decide en cuántos renglones se parte; `CONFIGURACIONES` y
`COLUMNAS`, el orden de las filas y de las columnas.

## 4. Cómo se cambia una caja o una flecha

Cada caja es una línea de la tabla `CAJAS`, al principio del script:

```python
"holm":                ("codigo",    "Corrección de Holm / El valor p menor contra 0,025 y el otro contra 0,05"),
```

- La clase es el primer valor: `"modelo"` (naranja), `"codigo"` (azul),
  `"datos"` (gris) o `"resultado"` (gris, con el borde más grueso). Cambiar la
  clase de una caja es cambiar ese valor.
- El texto es el segundo; « / » separa la primera línea (negrita) de la
  segunda (normal, más chica). El script lo parte solo en renglones al ancho
  `ANCHO_TEXTO` de la caja.

Cada flecha es una línea de la tabla `FLECHAS`, `(origen, destino)`. Dónde va
cada caja y por dónde pasa cada flecha está en `armar`: agregar o quitar una
caja o una flecha pide cambiar también `armar`, y el control de trazado
(§6) falla si las flechas dibujadas no son las de la tabla.

Después de un cambio, se regenera con el comando de §1. Si un texto nuevo no
entra (una palabra más ancha que su caja, un texto fuera de su caja, dos cajas
encimadas, una flecha que atraviesa una caja, la figura por encima de 9 cm),
el script se detiene sin escribir nada y dice qué control falló; entonces se
ajusta el `ANCHO_TEXTO` de esa caja.

## 5. Revisión de la imagen

Revisada a tamaño completo y en dos recortes ampliados: ningún texto queda
cortado, superpuesto ni fuera de su caja; ninguna flecha atraviesa una caja;
están las 12 cajas y las 16 flechas de las tablas, y ninguna más. La caja de
resultado se distingue de las de datos por el borde, y lo mismo su muestra en
la leyenda.

Textos partidos en más líneas que las del texto fijado (la barra « / » separa
dos líneas; aquí, « | » marca cada corte agregado):

- Preguntas | con sus | criterios / Las mismas | para los 3
- Agente con | el grafo
- Agente con | los | fragmentos / Configuración | combinada
- Agente con | los | fragmentos / Configuración | densa
- Juez de las | respuestas / El mismo | para los 3
- Fidelidad de | cada pregunta, | con el grafo (y lo mismo con «con la densa»);
  con la combinada, Fidelidad de | cada pregunta, | con la | combinada
- Grafo contra | la combinada / Diferencia por | pregunta y | prueba de |
  permutación de | signos (y lo mismo con «la densa»)
- Corrección | de Holm / El valor p | menor contra | 0,025 y el otro |
  contra 0,05
- El grafo | supera a los | fragmentos | si supera a | las 2

Ninguna caja va en una sola línea.

## 6. Controles

El script se detiene sin escribir nada si falla uno (`verificar`). Valores de
la consola:

1. contenido: 12 cajas, las de `CAJAS`, cada una con su clase; el texto
   dibujado de cada caja, unido, es el de `CAJAS` letra por letra; 59 textos;
   ninguno nombra un modelo.
2. trazado: 16 flechas, 18 tramos, ninguno diagonal ni hacia la izquierda;
   ninguna caja de destino empieza a la izquierda de su origen; cada flecha
   sale del borde de su caja y llega al borde de la de destino, lejos de las
   esquinas; las flechas son exactamente las de `FLECHAS`.
3. cajas: 13 con la leyenda, sin superposiciones, con 8,4 unidades como
   mínimo entre bordes; ningún trazo ni punta entra en una caja.
4. cruces: ninguno y ningún contacto; la distancia mínima entre dos flechas
   es 41,2 unidades (las dos que salen de la fidelidad del grafo).
5. textos: ninguno superpuesto; distancias mínimas de 4,0 entre textos, 10,1
   de texto a trazo y 9,0 de texto al borde de su caja. La letra es de 13
   unidades (7,27 pt) y de 14 unidades (7,83 pt) impresas a 15 cm: la más
   chica es la misma que la del mapa.
6. margen y tamaño: todo a 2,21 mm o más del borde; 8,80 cm de alto (máximo
   9).
7. registro: el SVG se relee; color y grosor controlados en 12 cajas, 4
   muestras y 16 flechas.

Cotejo del formato (`--formato` con la copia de `P` del commit de §3): los 35
valores de `FORMATO` coinciden, cada uno en la línea citada, y el PNG es el
mismo byte a byte que sin cotejo.

## 7. Observaciones

- El mapa exige que el centro de cada caja de destino quede a la derecha del
  de su origen. Aquí se exige que ningún tramo vaya hacia la izquierda y que
  ninguna caja de destino empiece a la izquierda de su origen; la flecha
  vertical de la corrección de Holm a la decisión cumple las dos.
- La caja de resultado tiene su entrada en la leyenda, «Resultado»; el mapa
  no la tiene.
- Los textos usan solo caracteres de las tablas AFM del mapa; si uno nuevo no
  está, el script se detiene y lo dice.
- El epígrafe lo redacta la autora.

## 8. Archivos

| Archivo | sha256 |
|---|---|
| `fig_comparacion.py` | `b7f1c93d904e003ea4d1c8adcd05e757ef11497afa08ed2008344f3ab266693c` |
| `figura_comparacion.png` (1772 × 1040 px) | `2e0154bfb5cf215eb925fab193d98fcc432324c2fbd846fb6441a9a9e5eaa3a7` |
| `figura_comparacion.svg` | `c25dfa387e856d95ab1ebb8f6db078ca3f75393c94afd35ef7944495e643d04f` |

Reproducibilidad: corrido dos veces con `--salida` y `--svg`, el PNG y el SVG dieron el mismo sha256. Con `--formato`, contra una copia de `generar_figura_proceso.py` con «Reglas fijas», el PNG es el mismo byte a byte.
