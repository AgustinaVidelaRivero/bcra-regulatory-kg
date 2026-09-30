# figura_fragmentos_vs_grafo — registro de generación (Figura 1.2)

Figura «la misma pregunta con dos formas de consultar» para la Introducción, con
el ejemplo del préstamo: el punto 5.1.1.1 del Texto Ordenado de Clasificación de
deudores, que remite al punto 3.7 («importe de referencia»).

- Arriba, la pregunta común.
- Izquierda, «Recuperación por fragmentos», bajo el subtítulo «Los dos puntos
  del ejemplo»: el punto 5.1.1.1 con su texto completo, la frase de remisión
  resaltada y la marca «recuperado · puesto 2»; el punto 3.7 en gris, con su
  texto y la marca «fuera de lo recuperado · puesto 1.523»; y la línea «resto
  del top-5: 5.1.1.2 · 5.1.2.2 · 5.1.2.1 · 7.4». Debajo, la respuesta que se
  puede redactar solo con lo recuperado y la marca de lo que falta.
- Derecha, «Consulta del grafo»: «1 · Buscar» con la pregunta; «2 · Abrir el
  nodo encontrado», la Restriccion del monto (5.1.1.1); «3 · Seguir las
  aristas», `referencia` hasta la Obligacion del 3.7 y `limita` hasta la
  Operacion (5.1.1.1), que la otra Restriccion del 5.1.1.1 (repago) también
  limita. Debajo, la respuesta con las dos condiciones del punto 5.1.1.1; la
  fila del 3.7 va con sangría bajo la del monto, porque la precisa.

**El lado derecho muestra el camino que el grafo pone al alcance desde el nodo
encontrado; no es la traza de una corrida del agente.** Qué nodo se abre y qué
aristas se siguen es una decisión de la figura (`NODO_ENCONTRADO`,
`ARISTAS_CONSULTA`); lo que se lee del grafo es que esos nodos y esas aristas
existen.

Historia: generada el 2026-09-28 en U-FIG-EJEMPLO, que reemplazó la versión del
ejemplo de los dividendos (generador y PNG del commit `fb6ef69`); ajustada el
mismo día en U-FIG-EJEMPLO-AJUSTE (§5). La versión de U-FIG-EJEMPLO no llegó a
commitearse: al cierre del ajuste, `git status` mostraba el generador y el PNG
como modificados respecto de `fb6ef69`.

## 1. Comandos de generación

```bash
PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py
PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py --verificar-busqueda
```

El generador escribe solo el PNG (el SVG va por stdin a `rsvg-convert` 2.62.3;
`--svg RUTA` lo guarda aparte). Con `--verificar-busqueda` vuelve a correr la
búsqueda léxica sobre los fragmentos de E0 (sin Neo4j ni API) y se detiene si
el top-5 o los puestos de 5.1.1.1 y 3.7 no son los del JSON; en la última
corrida coincidieron.

## 2. Grafo, pregunta y fuentes

- Grafo: KG-Reextraído-r1,
  `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`, sha256
  `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a`.
- Pregunta: «Para una entidad financiera, ¿qué condiciones hacen que los
  créditos para consumo o vivienda deban clasificarse en la cartera comercial?»

| Dato de la figura | De dónde sale |
|---|---|
| Pregunta | `ejemplo_prestamo_datos.json` → `pregunta` |
| Textos de 5.1.1.1 y 3.7, frase resaltada | JSON → `textos` (campo `texto` de los fragmentos E0 de `chunks_cla.json`, cortes de línea quitados y «pro-ductiva» reunida) |
| Puestos 2 y 1.523, resto del top-5 | JSON → `busqueda_fragmentos` (BM25, variante A, calculada por el extractor con `busqueda_lexica_fragmentos.py`) |
| Nodos, etiquetas, puntos y aristas | JSON → `grafo`, comprobados contra `kg.json` al generar |

| Archivo | sha256 |
|---|---|
| `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` | `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a` |
| `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cap.json` | `1931138dac0a107a69a7ff6312400f00465b991d52135457735beeb3e442c825` |
| `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json` | `98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1` |
| `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_ext.json` | `cbcd1a86f55ea49110610587873881c68c13a9d7975d3fd5e465f26302be2d12` |
| `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_pro.json` | `d8717d1c7423bb5f4d80cc830ff97635ce4d9839f8490b73860ea272568620e2` |
| `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_ric.json` | `fafebb82e07b34191b60022c1c179ea7d2213fd1f5d5f3a408b518c836c94c0d` |
| `docs/tesis/figuras/busqueda_lexica_fragmentos.py` | `13caa596ad25b9aae3e19ab5e1c4cf30821cf853418320090e2b5ed4cdbcf9d3` |
| `docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py` | `4c3a441972d27304b6d58d0664dbc15b893bce7ad3e7d2d49afad947f51eeea7` |
| `docs/tesis/figuras/ejemplo_prestamo_datos.json` | `25ab7b4c0d76fd735244fe0fecc17ceaba1b0e8bfd2312e7aa3cbd5c849672a2` |
| `docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py` | `0e7c379d71e4cda0192e26320d4f24ad4a26dc35a3da047bcbac8309412d43ad` |
| `docs/tesis/figuras/generar_figura_norma_a_grafo.py` (importado) | `9b0e45a299a0a078d250ccc999d192cbb83038bd8c00baa6bd8972d021b73f3d` |

`busqueda_lexica_fragmentos.py` tiene `tok_bm25` y `bm25` copiadas sin cambios
de `reports/u_inv_ejemplo/uinvejemplo_bm25.py` (commit `24e0116`; líneas 22-54;
sha256 `de9056c80c9a8b1e828ec6fbb6c712f140015b634c962604408354a5869b7ebe`;
antes en `/tmp/u_inv_ejemplo/`), réplica de
`data/experiment/bakeoff_embeddings/code/e3_medicion.py:56-90`: tokenizador en
minúsculas sin diacríticos, Okapi BM25 con k1 = 1,2 y b = 0,75, sobre el texto
completo de cada fragmento (encabezados heredados + texto propio). La elección
del ejemplo está en `reports/u_inv_candidatos/` (commit `791166d`; antes en
`/tmp/u_inv_candidatos/`).

Salida:

| Archivo | sha256 |
|---|---|
| `figura_fragmentos_vs_grafo.png` (1506 × 1829 px, 300 dpi) | `b5306b2fbf146e20d005ce469d7de86c78c03ac3bcc95e645597760c85954533` |
| SVG intermedio (no se guarda en el repositorio; 860 × 1044) | `9b0574b7ecadcfac8675c03f64c704993238d2ec202671df2c9eab6ae5a0f706` |

Generación determinística verificada: mismo PNG y mismo SVG con
`PYTHONHASHSEED` 0, 1, 2 y 3.

## 3. Qué está escrito a mano

Solo los textos de las dos respuestas (`RESPUESTA_*` en el generador):

- Izquierda: «Pasan a la cartera comercial si superan dos veces el importe de
  referencia establecido en el punto 3.7 y su repago depende de la actividad
  productiva o comercial del cliente (punto 5.1.1.1).», y debajo la marca
  «✗ el importe de referencia (punto 3.7): no recuperado» (la cruz se dibuja con
  dos trazos).
- Derecha: «Pasan a la cartera comercial si se cumplen las dos condiciones del
  punto 5.1.1.1:», y tres filas: «5.1.1.1 · superan dos veces el importe de
  referencia»; con sangría debajo de ella, «3.7 · el importe de referencia es el
  nivel máximo de ventas anuales de la categoría Micro del sector Comercio (Ley
  24.467)»; «5.1.1.1 · su repago depende de la actividad productiva o comercial,
  no de ingresos fijos». El número de cada fila se lee del punto del nodo del que
  sale la condición (restricción del monto, obligación del 3.7, restricción del
  repago), y la franja de la fila lleva el color del tipo de ese nodo.

Son también decisiones de composición, no datos: el umbral de lo recuperado
(top-5), el nodo que se abre en el paso 2, las tres aristas del paso 3 y la
sangría de la fila del 3.7.

## 4. Búsquedas del ejemplo

- **Fragmentos, variante A** (la que dibuja la figura): 1.763 fragmentos, 1.741
  con puntaje positivo. Top-5: 5.1.1.2 (28,1501), 5.1.1.1 (26,1982), 5.1.2.2
  (23,0787), 5.1.2.1 (22,6035), 7.4 (21,7776); 3.7 en el puesto 1.523 (1,4976).
  El extractor la recalcula y comprueba que reproduce
  `reports/u_med_ejemplo/umed2_analista_paso1_resultado.json` (commit
  `200462f`; sha256 `a69c44b00a7f4920d1a4e5224167e6edacf4b7153d004d2185050cb2387f5408`,
  línea 11 de `reports/u_med_ejemplo/umed_manifest.txt`; antes en
  `/tmp/u_med_ejemplo/`): misma pregunta, mismos sha256 de los cinco
  `chunks_*.json`, mismos tokens, mismo top-10 con los mismos puntajes exactos,
  y los puestos 2 y 1.523.
- **Fragmentos, variante B** (palabras vacías y raíces de Snowball para español,
  nltk 3.10.3), copiada en el JSON desde el mismo archivo: top-5 7.4, 5.1.1.2,
  10.2.1, 10.1, 5.1.1.1; 5.1.1.1 en el puesto 5; 3.7 sin puntaje (ningún término
  en común con la pregunta). La lista de palabras vacías está en
  `reports/u_med_ejemplo/umed2_analista_nltk_data/corpora/stopwords/spanish`
  (sha256 `6125eadf28ba664a60bf4296147bcbd40b80be93670056fdb229960ac15e2310`,
  igual a la línea 30 de `reports/u_med_ejemplo/umed2_analista_nltk_data_listado.sha256`);
  los paquetes de la venv de esa medición, con su versión, figuran en
  `reports/u_med_ejemplo/umed2_analista_venv_listado.sha256` (líneas 11, 34, 43,
  59, 201, 717, 1566 y 1577).
- **Nodos** (índice de texto completo `nodos_fulltext_kg_reextraido_r1`, 2.346
  nodos con coincidencia), copiada en el JSON desde
  `reports/u_med_ejemplo/umed2_analista_paso3_resultado.json` (sha256
  `047e6f6e80b6b88e300cfb090bd2223ea967de8c9cbea9e10f9c04a9c168a3cd`, línea 18
  del manifiesto): los nodos de 5.1.1.1 aparecen en los puestos 2 (Operacion), 4
  (Restriccion del monto, el nodo que abre la figura) y 156 (Restriccion del
  repago); ningún nodo de 3.7 tiene coincidencia. En la figura, el 3.7 se
  alcanza siguiendo la arista `referencia` desde la restricción del monto (la
  Obligacion del 3.7 tiene 13 aristas `referencia` entrantes, de 13 orígenes
  distintos, en `kg['edges']` de `kg.json`; la figura dibuja la de este punto).

## 5. Composición

- Los fragmentos muestran el texto completo del punto, con el número de punto
  en negrita al comienzo, donde el texto lo trae; la marca de estado ocupa la
  primera línea del recuadro, con el puesto.
- **Ajuste U-FIG-EJEMPLO-AJUSTE.** La oración de entrada de «Respuesta con lo
  consultado» anuncia dos condiciones y debajo hay tres filas: la del 3.7 precisa
  la condición del monto, no es una tercera. Esa fila va con 24 px de sangría
  (`SANGRIA_FILA`) debajo de la del monto y conserva su franja de color. El
  número de líneas de cada fila no cambió y el alto del PNG tampoco (1829 px).
- Las filas de las respuestas se envuelven en varias líneas cuando hace falta.
- Los nodos alcanzados están en `X_NODO` 118 (ancho 264) y los troncos de las
  aristas en x = 34 y x = 20, para que el rótulo `referencia` en negrita entre en
  el tramo horizontal; el script se detiene si un rótulo no entra.
- La leyenda nombra solo los tipos dibujados (Restriccion, Obligacion,
  Operacion), escritos como en el código.
- Tope de alto del PNG: 1850 px (`ALTO_MAX_PNG_PX`); la figura mide 1829 px
  (15,49 cm impresa a 12,75 cm de ancho).
- Tamaños: texto corrido 17 px → 7,14 pt; rótulos y leyenda 15 px → 6,30 pt,
  impresos a 12,75 cm.
- Verificación geométrica con `docs/tesis/figuras/verificar_geometria_svg.py` (sha256
  `fd8d062df7b7529131f466df628298e02dd079517aa66624caeea6a8b722df19`; métricas reales de
  Helvetica) sobre el SVG intermedio: 72 textos, 4 nodos, 10 trazos con flecha;
  ningún texto se superpone con otro ni pisa un nodo, ningún trazo atraviesa un
  nodo. Comandos (el SVG se guarda fuera del repositorio):
  `PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py --svg "$TMPDIR/figura_fragmentos_vs_grafo.svg"`
  y `PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/verificar_geometria_svg.py "$TMPDIR/figura_fragmentos_vs_grafo.svg"`.
