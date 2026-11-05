# figura_recorrido_respuesta — registro de generación

Figura del recorrido de una respuesta por la evaluación extrínseca, para el
capítulo 5. Sigue una sola pregunta, de punta a punta: la pregunta y sus
criterios; el agente, que consulta el grafo; la respuesta y la traza; el juez
de las respuestas, con su decisión sobre cada criterio; la regla fija que da
el veredicto; la lectura de la autora cuando un criterio queda en duda; los
indicadores de las citas, comprobados sobre la traza; y, si la respuesta
falla, la atribución de la falla y su clase.

Es un diagrama sin datos de la evaluación: el script no lee datos, registros ni
resultados. Todo lo que dibuja está escrito en el script (tablas `CAJAS` y
`FLECHAS`). Ninguna caja lleva el número de una sección de la tesis; los
números de punto que aparecen (5.1.1.1, 3.7) son parte del ejemplo.

## 1. El ejemplo es construido

La pregunta es la del ejemplo construido que la tesis usa en todos sus
capítulos (cuándo los créditos para consumo o vivienda pasan a la cartera
comercial), con sus tres criterios. La respuesta es una respuesta parcial que
cumple dos de los tres criterios. La respuesta, la traza y las decisiones del
juez son las del ejemplo, no las de una corrida; también lo es lo que de ellas
sale: el veredicto, el resultado de los indicadores de las citas y la clase de
la atribución.

Para poner las de una corrida real se cambian, en `CAJAS`, las líneas de
`respuesta`, `traza` y `juez` y, si cambia lo que de ellas sale, las de
`veredicto`, `fundada`, `atribucion` y `clase`; después se regenera con el
comando de §2 (ver §6).

## 2. Cómo se regenera

Desde la raíz del repositorio, con el script en `docs/tesis/figuras/`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B docs/tesis/figuras/fig_recorrido_respuesta.py
```

Escribe `figura_recorrido_respuesta.png` junto al script. Opciones: `--salida
<directorio>` (otro lugar para el PNG), `--svg <ruta>` (guarda también el SVG)
y `--formato <ruta>` (el `generar_figura_proceso.py` con el que se coteja el
formato; por omisión, el que está junto al script, si está).

La leyenda dice «Reglas fijas», así que el cotejo solo pasa contra un
`generar_figura_proceso.py` que diga lo mismo en su renglón 279. Contra el del
commit `73f4bc4e`, que dice «Pieza de código», se detiene con `ALTO [formato]` y
no escribe nada. Contra una copia con «Reglas fijas», da el mismo PNG.

Herramientas: Python 3, solo la biblioteca estándar (corrido con Python
3.12.13), y `rsvg-convert` 2.62.3 (cairo 1.18.4, pango 1.58.2) para el PNG,
como el mapa de la evaluación y las figuras del capítulo 4. El script no
importa ni ejecuta código del repositorio, no usa red ni API y no lee ningún
archivo, salvo, como texto, `generar_figura_proceso.py` para el cotejo del
formato. Se corrió desde la carpeta donde se escribió, fuera del repositorio,
con la misma línea y la ruta de esa carpeta; como el PNG se escribe junto al
script, el directorio de trabajo no cambia el resultado, pero la corrida desde
la raíz del repositorio queda NO VERIFICADA. Tampoco se corrió con el
`.venv/bin/python` del repositorio (NO VERIFICADO).

## 3. Composición

- Arriba, los dos datos de entrada: la pregunta y los criterios. La pregunta
  baja al agente y al juez; los criterios, al juez.
- En el medio, el camino principal en una fila (agente → respuesta → juez →
  regla del veredicto → veredicto), con sus cuatro flechas sobre una misma
  recta. Con la pregunta, que baja al agente con una flecha vertical, son las
  seis piezas del camino principal.
- Abajo, las ramas: la traza, debajo del agente, que alimenta los indicadores
  de las citas (debajo de la respuesta) y la atribución de la falla; los
  indicadores llevan a «Fundada»; el juez baja a la lectura de la autora
  («Si un criterio queda en duda»), que sube al veredicto; el veredicto baja a
  la atribución («Si falla»), y la atribución, a la clase. La leyenda va abajo
  a la izquierda, como en el mapa.
- Ninguna flecha atraviesa una caja, cruza o toca a otra flecha, ni tiene un
  tramo hacia la izquierda. Toda caja de destino tiene el centro a la derecha
  del de su origen o está debajo de él, unida por una flecha vertical: así
  bajan la pregunta al agente, los criterios al juez, el agente a la traza, la
  respuesta a los indicadores y el veredicto a la atribución.
- Las flechas del camino principal llevan el grosor de la línea principal de la
  figura del proceso (`GROSOR_FLUJO`); las demás, el de sus entradas y ramas
  (`GROSOR_RAMA`).
- Los dos rótulos van a la derecha del tramo vertical de su flecha, centrados
  en él, como en la figura del proceso.

Lienzo de 760 × 600 unidades, impreso a 15,00 × 11,84 cm. El PNG mide
1772 × 1399 px a 300 dpi.

## 4. Formato: de dónde sale cada valor

`M` es `fig_evaluacion.py`, el script del mapa de la evaluación (sha256
`34b18970e3f282d0ba17e211e5bf0098c18d2c48b95dd5d60f694d14a63894cd`); sus
líneas son las de ese archivo. `P` es
`docs/tesis/figuras/generar_figura_proceso.py` en el commit
`dbf2eef44510153a76181d010ebeb8c6a6b92aea` (sha256
`8667c219fe5586466e3cad04bc81843a8b39025d59b443edbacf79740349cbbf`, el mismo
archivo que cita el mapa; su último cambio es el commit `552e61f`). Los valores
están copiados en el script, cada uno con su línea de `M` y de `P` en un
comentario, y la tabla `FORMATO` coteja con `P` los que vienen de ahí (§8).

| Valor | En esta figura | Fuente |
|---|---|---|
| Biblioteca estándar y `rsvg-convert` | todo el script; PNG con `rsvg-convert -w 1772 -f png` | M:64-76, M:1154-1162 (P:82-96, P:1239-1246) |
| Densidad del PNG, 300 dpi (bloque pHYs después de IHDR) | `con_densidad` | M:1134-1151 (P:1190-1211) |
| Métrica del texto: tablas AFM de Helvetica y Helvetica-Bold, con «¿» y «?» | `_AFM` | M:290-306 (P:335-349) |
| `W = 760` (unidades para 15 cm) | lienzo | M:172 (P:163) |
| `ANCHO_CM = 15.0`, `DPI = 300`, 1772 px | ancho impreso y del PNG | M:195-196, M:215 (P:311, P:313) |
| `TIPOGRAFIA = "Helvetica,Arial,sans-serif"` | `font-family` del SVG | M:173, M:1067-1068 (P:164) |
| `MODELO` (#fbe3d3 / #e07b39) | cajas naranjas: lo que ejecuta un modelo de lenguaje | M:174 (P:165) |
| `DETERMINISTICA` (#e1e7ee / #4a5a6a) | cajas azules: código y reglas fijas | M:175 (P:166) |
| `NEUTRO` (#fafafa / #999999) | cajas grises: datos y resultados | M:176 (P:167) |
| `TINTA, TINTA_SUB` (#1f1f1f, #444444) | título y leyenda en `TINTA`; los demás renglones y los rótulos en `TINTA_SUB` | M:177 (P:168, P:594-597) |
| `FLECHA` (#555555) | trazos y puntas | M:178 (P:169) |
| `FS_TITULO, FS_TEXTO = 14, 13` | título 14 en negrita; demás renglones, leyenda y rótulos 13, normal | M:179 (P:171, P:594-597) |
| `IL = {14: 18, 13: 17}` | interlíneas | M:180 (P:172) |
| `SEP_TITULO = 5` | del título al primer renglón siguiente | M:181 (P:173) |
| `PAD_X, PAD_Y = 9, 11` | márgenes internos | M:182 (P:174) |
| ancho y alto de caja: texto + 2 × `PAD_X` + 2, texto + 2 × `PAD_Y` | `ancho_caja`, `alto_caja` | M:389-396 (P:383-388) |
| texto alineado a la izquierda en `x + PAD_X`, centrado en vertical; línea de base | `textos_de` | M:601-614 |
| partición del texto en renglones al ancho de la caja | `partir`, `lineas_caja` | M:345-382 |
| `GROSOR_CAJA = 1.6` | borde de las cajas y de las muestras, salvo los resultados y la lectura de la autora | M:183 (P:175) |
| borde de los resultados y de la lectura de la autora, 1,5 × `GROSOR_CAJA` = 2,4, en sus cajas y en sus muestras de la leyenda | `GROSOR_RESULTADO = round(1.5 * GROSOR_CAJA, 1)` (línea 181 de este script); la tabla `GROSOR` (líneas 190-191) se lo da a las clases «lectura» y «resultado» | M:183 (P:175), por 1,5 |
| `GROSOR_FLUJO, GROSOR_RAMA = 1.8, 1.6` | flechas (§3) | M:184 (P:176) |
| `RADIO = 9` y la poligonal redondeada | esquinas de los trazos | M:185, M:1046-1060 (P:177, P:1060-1073) |
| `RX = 8` | esquinas de las cajas | M:186 (P:178) |
| `LEJOS_ESQUINA = RX + 4` | los extremos de las flechas, lejos de las esquinas | M:206 (P:325) |
| marcador de la punta (`MARCADOR_A`, `MARCADOR_B`) | punta de todas las flechas | M:190-191, M:1070 (P:183-184) |
| `HUECO_PUNTA = 2.0` | del final del trazo al borde de la caja | M:202 (P:324) |
| `MARGEN = 12`, `MARGEN_MM = 2.0` | márgenes del lienzo | M:187, M:198, M:216 (P:180, P:316) |
| `PT_MINIMO = 7.0` | ninguna letra por debajo de 7 pt | M:197 (P:315) |
| `HOLGURA_TEXTO = 1.5`, `DISTANCIA_MIN = 3.0`, `SEP_CAJAS = 8.0` | holguras de los controles | M:199-201 (P:318-320) |
| `ASC, DESC = 0.78, 0.22` | caja de cada texto | M:203 (P:350) |
| un decimal en las coordenadas | `f` | M:321-323 (P:567-570) |
| fondo blanco y cabecera del SVG | `dibujar` | M:1063-1072 |
| leyenda: marco `LEYENDA_MARCO`, muestras de 24 × 16 con `rx` 3, filas de 22, `GRUPO_LEYENDA = 10`, posición de muestras y textos, abajo a la izquierda | `armar`, `muestras_leyenda`, `textos_de` | M:188-189, M:204-205, M:584-589, M:620-636 (P:181-182, P:420, P:1123) |
| leyenda: textos de las 3 primeras clases | `LEYENDA` | M:192-194 (P:278-280) |
| separaciones: `SEP_FLECHA = 20`, `SEP_VERTICAL = 20`, `CARRIL = 10`, `SOBRE_LEYENDA = 10`, `SEP_SIN_FLECHA = 10` | `armar` | M:409, M:411, M:412, M:414, M:416 |
| tramo común de dos cajas para una flecha recta | `comun` | M:446-454 |
| rótulo a la derecha de un tramo vertical, a `ROTULO_AIRE = 4.0`, centrado en el tramo | `armar` | P:323, P:541-549 |
| control de los rótulos: dentro del tramo recto, a no más de `JUNTO = 8.0`, `AJENA = 5.0` más lejos de otra flecha | `controlar_rotulos` | P:321-322, P:988-1015 |
| `ALTO_MAX_CM = 13.0` | alto máximo | M:217 |
| controles de contenido, trazado, cajas, cruces, textos, margen y registro | `verificar` | M:790-1036, M:1101-1128 |

Agregados de esta figura:

- Dos clases nuevas. «Lectura de la autora»: fondo blanco (`#ffffff`), borde
  `TINTA`, el color del título, con el grosor de los resultados, 2,4
  (`GROSOR_RESULTADO`). «Resultado»: la paleta de los datos (`NEUTRO`) con el
  borde de 2,4. Las dos van en la leyenda, con sus textos y con el mismo
  borde de 2,4 en su muestra, después de las tres del mapa.
- Varios renglones por caja: la barra « / » separa el título de cada renglón
  siguiente; cada renglón empieza en una línea nueva y se parte solo al ancho
  de la caja. El mapa tiene, como mucho, un renglón después del título.
- El control del trazado acepta, además de los destinos a la derecha del
  origen, los que están debajo de él, unidos por una sola flecha vertical hacia
  abajo (en el mapa, una lista de excepciones).
- Un texto no puede quedar a menos de `HOLGURA_TEXTO` de una caja que no es la
  suya (en el mapa, el control es solo de superposición); el control vale
  también para los rótulos.

Medidas propias (no salen de otra figura): `ANCHO_TEXTO`, el ancho del texto
de cada caja, que decide en cuántos renglones se parte; `SEP_ENTRADAS = 20`
(entre la pregunta y los criterios); de «Fundada» a la lectura de la autora,
`SEP_CAJAS` más la mitad de sus dos bordes de 2,4, redondeado hacia arriba
(11 unidades); la altura de la lectura de la autora,
calculada para que el rótulo de su flecha quede a `CARRIL` de la regla y a
`RADIO` del juez; la entrada de la flecha de la lectura al veredicto,
`LEJOS_ESQUINA + 5` desde el borde izquierdo del veredicto; y la vertical del
veredicto a la atribución, a la distancia del borde derecho que deja lugar a
su rótulo.

## 5. Cómo se cambia una caja o una flecha

Cada caja es una línea de la tabla `CAJAS`, al principio del script:

```python
"juez":         ("modelo",    "Juez de las respuestas / 1. Cumple / 2. No cumple / 3. Cumple"),
```

- La clase es el primer valor: `"modelo"` (naranja), `"codigo"` (azul),
  `"datos"` (gris), `"lectura"` (blanca, con el borde del color del texto y
  más grueso) o `"resultado"` (gris, con el borde más grueso).
- El texto es el segundo; « / » separa los renglones: el primero es el título,
  en negrita, y los demás van en letra normal más chica. El script los parte
  solo al ancho `ANCHO_TEXTO` de la caja.

Cada flecha es una línea de la tabla `FLECHAS` (origen, destino y rótulo, o
`None`). Cambiar un rótulo es cambiar el tercer valor. Agregar o quitar una
flecha pide cambiar también la composición (`armar`).

Después de un cambio, se regenera con el comando de §2. Si el texto nuevo no
entra (una palabra más ancha que su caja, un texto fuera de su caja, dos cajas
encimadas, una flecha que atraviesa una caja, la figura por encima de 13 cm),
el script se detiene sin escribir nada y dice qué control falló; entonces se
ajusta el `ANCHO_TEXTO` de esa caja.

## 6. Para una corrida real

Se cambian los textos de §1 y nada más. La decisión del juez va un renglón por
criterio (`1. Cumple / 2. No cumple / 3. Cumple`); la traza, en un renglón
después de «Traza». Si un texto nuevo es más largo, la caja crece hacia abajo
y la composición la acompaña; si no entra, el script lo dice (§5).

## 7. Revisión de la imagen

Revisada a tamaño completo y en dos recortes a resolución completa (los dos
rótulos; la traza y los indicadores): ningún texto queda cortado, superpuesto
ni fuera de su caja; ninguna flecha atraviesa una caja ni cruza a otra; están
las 13 cajas y las 16 flechas de las tablas, y ninguna más; los dos rótulos se
leen.

Textos partidos en más líneas que las del texto fijado (la barra « / » separa
renglones; aquí, « | » marca cada corte agregado; 23 cortes en 12 cajas):

- Pregunta / Para una entidad financiera, ¿qué condiciones hacen que los | créditos para consumo o vivienda deban clasificarse en la cartera | comercial?
- Criterios / … / 2. El importe es el máximo de ventas anuales de la | categoría Micro del sector Comercio / …
- Agente / Consulta el | grafo
- Respuesta / Esos créditos pasan a la cartera | comercial cuando superan dos | veces el importe de referencia y su | repago depende de la actividad del | cliente / Cita: Clasificación de deudores, | 5.1.1.1
- Traza / Abrió el | 5.1.1.1 y | no siguió la | remisión al | 3.7
- Juez de las | respuestas / …
- Regla del | veredicto / Todos cumplidos, | correcta / …
- Lectura de la autora / Pone el veredicto | contra el texto oficial
- Parcial / Cumple 2 de 3 | criterios
- Indicadores de las citas / … / Una cita es el punto que | responde
- Fundada / Cumple los 3 | indicadores
- Atribución de | la falla / Abrió uno de los | puntos que | responden

Va sin cortes: «Clase 4 / Lo consultó».

## 8. Controles

El script se detiene sin escribir nada si falla uno (`verificar`). Valores de
la consola del comando de §2:

1. contenido: 13 cajas, las de `CAJAS`, cada una con su clase; el texto
   dibujado de cada caja, unido, es el de `CAJAS` letra por letra; 2 rótulos,
   los de `FLECHAS`; 65 textos; ninguno nombra un modelo.
2. trazado: 16 flechas, 18 tramos, ninguno diagonal ni hacia la izquierda; cada
   flecha sale del borde de su caja y llega al borde de la de destino, lejos de
   las esquinas; las flechas son exactamente las de `FLECHAS`; 5 bajan a una
   caja que no está a la derecha de su origen, todas con una sola vertical.
3. cajas: 14 con la leyenda, sin superposiciones, con 8,6 unidades como mínimo
   entre bordes; ningún trazo ni punta entra en una caja.
4. cruces: ninguno, ningún contacto; la distancia mínima entre dos flechas es
   40,6 unidades.
5. textos: ninguno superpuesto; distancias mínimas de 4,0 entre textos, 4,0 de
   texto a trazo y 9,0 de texto al borde de su caja. La letra es de 13
   unidades (7,27 pt) y de 14 unidades (7,83 pt) impresas a 15 cm: la más
   chica es la misma que la del mapa.
6. rótulos: los dos a 4,0 de su flecha; la otra flecha más cercana, a 36,8
   («Si un criterio queda en duda») y a 46,2 («Si falla»).
7. margen y tamaño: todo a 2,13 mm o más del borde; 11,84 cm de alto
   (máximo 13).
8. registro: el SVG se relee; color y grosor controlados en 13 cajas, 5
   muestras y 16 flechas.

Cotejo del formato (`--formato` con `P` del commit de §4): los 38 valores de
`FORMATO` coinciden, cada uno en la línea citada.

## 9. Observaciones

- Las tablas AFM no traen «¿» ni «?»; el mapa los agregó con los anchos de las
  métricas Core 14 de Adobe, sin cotejarlos con un archivo AFM (NO
  VERIFICADO). En la imagen, la pregunta, el único texto con esos signos,
  queda dentro de su caja.
- La figura del proceso tiene una clase para la revisión humana, blanca, con
  borde gris y discontinuo (P:170, P:179, P:277, P:1097). Aquí la lectura de
  la autora va blanca con el borde continuo del color del texto, de 2,4.
- El epígrafe lo redacta la autora.

## 10. Archivos

| Archivo | sha256 |
|---|---|
| `fig_recorrido_respuesta.py` | `dad5b468a0a03c1633a4b4a5080098dc43471a5f1e3193db43dc9f37e43e1061` |
| `figura_recorrido_respuesta.png` (1772 × 1399 px) | `164d0241c130d279091a1c9321a98974a5720eebe7f5682e714aa3ed033dae09` |
| `figura_recorrido_respuesta.svg` | `c1b60d021184e8b061e3175c44d0c4bfcb2471e5840e102b98e88d910c56845b` |

Reproducibilidad: corrido dos veces con `--salida` y `--svg`, el PNG y el SVG
dieron el mismo sha256. Con el comando de §2 sin opciones y con `--formato`
(contra una copia con «Reglas fijas»), el PNG es el mismo byte a byte.

## 11. Cambio de texto de la leyenda

- `fig_recorrido_respuesta.py:183`: `("codigo", "Pieza de código")` pasa a
  `("codigo", "Reglas fijas")`. Es el único cambio del script. El ejemplo es el
  mismo: no cambian la respuesta, la traza ni las decisiones del juez.
- Antes: script `9ae4ee54e7430d20d8ef16204c4805c829e1d330f0536a382c6fbd8917e5aaee`,
  PNG `8bfe87c371592e3d9d7551955325a09e4ab8013e12c53a5534579c5e195cb177`.
- Por este cambio, ese texto de la leyenda ya no coincide con `M:193` ni con `P:279`
  en los archivos citados en §4; los demás valores de esa sección siguen iguales.
- La disposición no cambia: ningún renglón ni caja se mueve, y el PNG sigue en
  1772 × 1399 px.
