# figura_evaluacion — registro de generación

Figura del método de evaluación, para la entrada del capítulo 5. Es un mapa de
cajas y flechas: a la izquierda, los datos (los documentos, el grafo evaluado
y los fragmentos de los documentos); arriba, la banda de la evaluación
intrínseca (la precisión y la cobertura del contenido del grafo); abajo, la
banda de la evaluación extrínseca (las respuestas del agente con cada uno de
los dos servidores, su juez, las reglas de las citas, la fidelidad, la
atribución de las fallas y la comparación con los fragmentos). Cada caja lleva,
si la tiene, el número de la sección que la trata, en negrita y arriba a la
izquierda.

Es un diagrama del método, sin datos: el script no lee datos, registros ni
resultados de la evaluación. Todo lo que dibuja está escrito en el script
(tablas `CAJAS` y `FLECHAS`). Ninguna caja nombra un modelo ni lleva una
cantidad; las únicas cifras son los números de sección y el «2» de la segunda
línea del agente («Consulta uno de los 2 servidores»), que es texto de la
tesis.

## 1. Cómo se regenera

Desde la raíz del repositorio, con el script en `docs/tesis/figuras/`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B docs/tesis/figuras/fig_evaluacion.py
```

Escribe `figura_evaluacion.png` junto al script. Opciones: `--salida
<directorio>` (otro lugar para el PNG), `--svg <ruta>` (guarda también el SVG)
y `--formato <ruta>` (el `generar_figura_proceso.py` con el que se coteja el
formato; por omisión, el que está junto al script, si está).

Herramientas: Python 3, solo la biblioteca estándar (corrido con Python
3.12.13), y `rsvg-convert` 2.62.3 (cairo 1.18.4, pango 1.58.2) para el PNG,
como las figuras del capítulo 4. El script no importa ni ejecuta código del
repositorio, no usa red ni API y no lee ningún archivo, salvo, como texto,
`generar_figura_proceso.py` para el cotejo del formato. Las figuras hermanas se
corren con el `.venv/bin/python` del repositorio; este script no se corrió con
ese intérprete (NO VERIFICADO), aunque no usa nada fuera de la biblioteca
estándar.

## 2. Composición

- Los datos van en una columna a la izquierda, fuera de las bandas. Cada banda
  lleva su rótulo arriba a la izquierda y su marco.
- Banda de arriba, dos filas. La de arriba: la cadena de la precisión (muestra
  de tripletas → juez de las tripletas → precisión e importancia) y, a la
  derecha, el final de la cadena de la cobertura (juez de presencia →
  cobertura). La de abajo: el comienzo de la cadena de la cobertura (muestra
  de pasajes → extrae → comprueba → ordena), que sube al juez de presencia con
  una flecha vertical. La cadena de la cobertura tiene seis cajas y, con la
  columna de los datos a la izquierda, no entra en una fila a 15 cm. La flecha
  del grafo al juez de presencia corre entre las dos filas.
- Banda de abajo, tres niveles. Arriba: redacta → preguntas → juez de las
  respuestas → comparación. En el medio: servidor del grafo ↔ agente →
  respuesta → atribución, con el agente debajo de las preguntas. Abajo: el
  servidor de los fragmentos (↔ agente), las reglas de las citas (debajo de la
  respuesta) y la fidelidad. La flecha del juez a la fidelidad pasa a la
  derecha de la atribución.
- Ninguna flecha atraviesa una caja ni tiene un tramo hacia la izquierda. Todas
  las cajas de destino tienen el centro a la derecha del de su origen, salvo
  una: «Ordena las tripletas por importancia» → «Juez de presencia», la flecha
  vertical que sube de una fila a la otra (`A_LA_IZQUIERDA`).
- Hay dos cruces entre flechas, en ángulo recto (`CRUCES`): la flecha del grafo
  a su servidor cruza las dos que salen de los documentos (a la muestra de
  pasajes y a la redacción de las preguntas). Con los datos a la izquierda,
  los documentos y el grafo alimentan las dos bandas, y alguna flecha tiene que
  cruzar a otra.
- Las flechas que salen de los datos llevan el grosor de las entradas de la
  figura del proceso (`GROSOR_RAMA`); las demás, el de su línea principal
  (`GROSOR_FLUJO`). Las dos flechas entre el agente y sus servidores tienen
  punta en los dos extremos.

Lienzo de 760 × 656 unidades, impreso a 15,00 × 12,95 cm. El PNG mide
1772 × 1530 px a 300 dpi.

## 3. Formato: de dónde sale cada valor

`P` es `docs/tesis/figuras/generar_figura_proceso.py` en el commit
`a9636f37b73dc5c9fafc6a37372b6236e83b37fc` (sha256
`8667c219fe5586466e3cad04bc81843a8b39025d59b443edbacf79740349cbbf`). `X` es
`fig_extractor_funcion.py`, el script de la figura del extractor como función
(sha256 `3d0b2dc8d2f5573a104a234babf24de4c13b5ed1805370300ddec9d7d6eec992`),
que en ese commit todavía no está versionado; sus líneas son las de ese
archivo. Los valores de `P` están copiados en el script, cada uno con su línea
en un comentario, y la tabla `FORMATO` los coteja con `P` (§6).

| Valor | En esta figura | Fuente |
|---|---|---|
| Biblioteca estándar y `rsvg-convert` | todo el script; PNG con `rsvg-convert -w 1772 -f png` | P:82-96, P:1239-1246 |
| Densidad del PNG, 300 dpi (bloque pHYs después de IHDR) | `con_densidad` | P:1190-1211 |
| Métrica del texto: tablas AFM de Helvetica y Helvetica-Bold | `_AFM`, más «¿» y «?» (§7) | P:335-349 |
| `W = 760` (unidades para 15 cm) | lienzo | P:163 |
| `ANCHO_CM = 15.0`, `DPI = 300` | ancho impreso y del PNG (1772 px) | P:311, P:313, P:314 |
| `TIPOGRAFIA = "Helvetica,Arial,sans-serif"` | `font-family` del SVG | P:164, P:1134 |
| `MODELO` (#fbe3d3 / #e07b39) | cajas naranjas: lo que ejecuta un modelo de lenguaje | P:165 |
| `DETERMINISTICA` (#e1e7ee / #4a5a6a) | cajas azules: código y reglas fijas | P:166 |
| `NEUTRO` (#fafafa / #999999) | cajas grises: datos y resultados | P:167 |
| `TINTA, TINTA_SUB` (#1f1f1f, #444444) | primera línea y número de sección en `TINTA`; segunda línea en `TINTA_SUB` | P:168, P:370 |
| `FLECHA` (#555555) | trazos y puntas | P:169 |
| `FS_TITULO, FS_TEXTO = 14, 13` | primera línea 14 en negrita; segunda línea 13 normal; número de sección 13 en negrita; leyenda 13 | P:171, P:365-372 |
| `IL = {14: 18, 13: 17}` | interlíneas | P:172 |
| `SEP_TITULO = 5` | de la primera línea a la segunda | P:173 |
| `PAD_X, PAD_Y = 9, 11` | márgenes internos | P:174 |
| ancho y alto de caja: texto + 2 × `PAD_X` + 2, texto + 2 × `PAD_Y` | `ancho_caja`, `alto_caja` | P:383-388 |
| texto centrado en vertical en su caja; línea de base | `textos_de` | P:586-589 |
| `GROSOR_CAJA = 1.6` | borde de las cajas y de las muestras | P:175 |
| `GROSOR_FLUJO, GROSOR_RAMA = 1.8, 1.6` | flechas (§2) | P:176, P:298-300 |
| `RADIO = 9` y la poligonal redondeada | esquinas de los trazos | P:177, P:1060-1073 |
| `RX = 8` | esquinas de las cajas | P:178 |
| `LEJOS_ESQUINA = RX + 4` | los extremos de las flechas, lejos de las esquinas | P:325 |
| marcador de la punta (`MARCADOR_A`, `MARCADOR_B`) | punta de todas las flechas | P:183-185, P:1136 |
| `HUECO_PUNTA = 2.0` | del final del trazo al borde de la caja | P:324 |
| `MARGEN = 12`, `MARGEN_MM = 2.0` | márgenes del lienzo | P:180, P:316-317 |
| `PT_MINIMO = 7.0` | ninguna letra por debajo de 7 pt | P:315 |
| `HOLGURA_TEXTO = 1.5`, `DISTANCIA_MIN = 3.0`, `SEP_CAJAS = 8.0` | holguras de los controles | P:318-320 |
| `ASC, DESC = 0.78, 0.22` | caja de cada texto | P:350 |
| un decimal en las coordenadas | `f` | P:567-570 |
| fondo blanco y cabecera del SVG | `dibujar` | P:1132-1135 |
| leyenda: textos de las 3 clases | `LEYENDA` | P:278-280 |
| leyenda: marco `LEYENDA_MARCO`, muestras de 24 × 16 con `rx` 3, filas de 22, `GRUPO_LEYENDA = 10`, posición de muestras y textos | leyenda, abajo a la izquierda | P:181-182, P:420, P:552-556, P:599-614, P:1123 |
| texto alineado a la izquierda, en `x + PAD_X` | todas las cajas | X:563, X:572 |
| encabezado: `FS_TITULO`, negrita, `TINTA` | rótulo de cada banda | X:595-596 |

Agregados de esta figura, hechos con piezas de `P`:

- El marco de cada banda es el de la leyenda (`LEYENDA_MARCO`, P:181).
- La punta del arranque de una flecha doble es el marcador de `P` con el
  triángulo dado vuelta y `refX="1"` (`MARCADOR_INICIO`).
- El número de sección va en la primera línea, en `FS_TEXTO` y negrita, a la
  izquierda del título y separado por un espacio de la primera línea
  (`SEP_SECCION`).
- La clase «resultado» usa la paleta de los datos (`NEUTRO`); la leyenda tiene
  las tres clases de la figura del proceso.

Medidas propias (no salen de otra figura): `ANCHO_TEXTO`, el ancho del texto
de cada caja, que decide en cuántos renglones se parte; `X_TRONCO = 128`
(vertical de la flecha del grafo a su servidor); `X_BANDA = 138` y
`PAD_BANDA = 4` (borde izquierdo de las bandas y aire a los costados);
`ALTO_ROTULO = 28` (6 + interlínea de 18 + 4); `SEP_BANDAS = 8`;
`PIE_BANDA = 4`; `SEP_FLECHA = 20` (cajas unidas por una flecha horizontal);
`SEP_DOBLE = 32` (flecha doble); `SEP_VERTICAL = 20` (flecha vertical);
`SEP_SIN_FLECHA = 10` (`SEP_CAJAS` más el borde, redondeado); `CARRIL = 10`
(del carril del grafo a las cajas); `SEP_FILA_B = 22`; `SOBRE_LEYENDA = 10`;
`ALTO_MAX_CM = 13.0`.

## 4. Cómo se cambia el texto o la clase de una caja

Cada caja es una línea de la tabla `CAJAS`, al principio del script:

```python
"juez_tripletas":      ("modelo",    "5.2.1", "Juez de las tripletas / ¿Es correcta? ¿Cuánto importa?"),
```

- La clase es el primer valor: `"modelo"` (naranja), `"codigo"` (azul),
  `"datos"` (gris) o `"resultado"` (gris, con el texto en negrita). Cambiar la
  clase de una caja es cambiar ese valor.
- La sección es el segundo valor (`None` si la caja no lleva número).
- El texto es el tercero; « / » separa la primera línea (negrita) de la segunda
  (normal, más chica). El script lo parte solo en renglones al ancho
  `ANCHO_TEXTO` de la caja.

Después de un cambio, se regenera con el comando de §1. Si el texto nuevo no
entra (una palabra más ancha que su caja, un texto fuera de su caja, dos cajas
encimadas, una flecha que atraviesa una caja, la figura por encima de 13 cm),
el script se detiene sin escribir nada y dice qué control falló; entonces se
ajusta el `ANCHO_TEXTO` de esa caja. Las flechas están en `FLECHAS`; agregar o
quitar una flecha pide cambiar también la composición (`armar`).

## 5. Revisión de la imagen

Revisada a tamaño completo y en recortes: ningún texto queda cortado,
superpuesto ni fuera de su caja; ninguna flecha atraviesa una caja; están las
23 cajas y las 26 flechas de las tablas, y ninguna más; cada número de sección
se lee.

Textos partidos en más líneas que las del texto fijado (la barra « / » separa
dos líneas; aquí, « | » marca cada corte agregado):

- Los | documentos; El grafo | evaluado; Los | fragmentos | de los | documentos
- Muestra | de | tripletas | del grafo; Muestra de | pasajes
- Juez de | las tripletas / ¿Es correcta? | ¿Cuánto | importa?
- Precisión | e importancia
- Extrae la | tripleta más | importante de | cada pasaje
- Comprueba | que su tramo | esté en el pasaje
- Ordena las | tripletas por | importancia
- Juez de | presencia / ¿Está la | tripleta en el | grafo?
- Redacta las | preguntas; Preguntas con | sus criterios
- Agente / Consulta uno | de los 2 | servidores
- Servidor | del grafo; Servidor | de los | fragmentos
- Respuesta, | citas y traza
- Juez de las | respuestas / ¿Cumple cada | criterio?
- Atribución | de las fallas; Comparación | con los fragmentos

Van en una sola línea: «Cobertura», «Reglas de las citas» y «Fidelidad».

## 6. Controles

El script se detiene sin escribir nada si falla uno (`verificar`). Valores de
la consola del comando de §1:

1. contenido: 23 cajas, las de `CAJAS`, cada una con su clase; el texto
   dibujado de cada caja, unido, es el de `CAJAS` letra por letra; 83 textos;
   ninguno nombra un modelo.
2. trazado: 26 flechas (2 con punta en los dos extremos), 31 tramos, ninguno
   diagonal ni hacia la izquierda; cada flecha sale del borde de su caja (o de
   un tramo de su flecha madre) y llega al borde de la de destino, lejos de
   las esquinas; las flechas son exactamente las de `FLECHAS`.
3. cajas: 24 con la leyenda, sin superposiciones, con 8,4 unidades como mínimo
   entre bordes; cada caja dentro de su banda y los datos fuera de las bandas;
   ningún trazo ni punta entra en una caja.
4. cruces: 2, los de `CRUCES`; ningún contacto; la distancia mínima entre dos
   flechas que no se cruzan es 15,4 unidades.
5. textos: ninguno superpuesto; distancias mínimas de 3,9 entre textos, 10,1
   de texto a trazo y 9,0 de texto al borde de su caja. La letra es de 13
   unidades (7,27 pt) y de 14 unidades (7,83 pt) impresas a 15 cm: la más
   chica es la misma que la de la figura del proceso.
6. margen y tamaño: todo a 2,21 mm o más del borde; 12,95 cm de alto (máximo
   13).
7. registro: el SVG se relee; colores controlados en 23 cajas, 3 muestras y
   26 flechas.

Cotejo del formato (`--formato` con la copia de `P` del commit de §3): los 35
valores de `FORMATO` coinciden, cada uno en la línea citada.

## 7. Observaciones

- La figura del proceso centra el texto de sus cajas (P:590). Aquí va alineado
  a la izquierda, como en la figura del extractor como función, porque el
  número de sección ocupa el comienzo de la primera línea.
- Todas las cajas llevan la primera línea en negrita (P:365-372), así que las
  cajas de resultado se ven como las de datos: grises y en negrita.
- Las tablas AFM de `P` no traen «¿» ni «?». Se agregaron con los anchos de
  las métricas Core 14 de Adobe (611 y 556 en Helvetica; 611 y 611 en
  Helvetica-Bold), sin cotejarlos con un archivo AFM (NO VERIFICADO). En la
  imagen, los textos con esos signos quedan dentro de su caja.
- El epígrafe lo redacta la autora.

## 8. Archivos

| Archivo | sha256 |
|---|---|
| `fig_evaluacion.py` | `34b18970e3f282d0ba17e211e5bf0098c18d2c48b95dd5d60f694d14a63894cd` |
| `figura_evaluacion.png` (1772 × 1530 px) | `1b85be9d381358b7e45e7144db2b45a0d54433d928e05f5260bd599e3389c80d` |

Reproducibilidad: corrido dos veces con el comando de §1, el PNG dio el mismo
sha256 y la consola fue la misma (`cmp`). Con `--formato` y con `--svg`, el
PNG es el mismo byte a byte.
