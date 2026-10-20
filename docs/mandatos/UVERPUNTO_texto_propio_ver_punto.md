# Mandato U-VERPUNTO: el texto propio entero en `ver_punto`, antes de N6 (firmado el 20/10/2026)

**FIRMADO por la autora el 20/10/2026** (por mensaje recibido a las 10:01:39; hoja de ruta de la mesa, §195), sobre el borrador de la §194
(sha256 `38f6812f…`, en el paquete de la mesa, `decisiones_194_mesa/ver_punto/`), con las decisiones del §7 que dice la sección «Firma»,
que mandan sobre su texto. El texto firmado es el del borrador, con este encabezado y esa sección. USD 0, sin API. Las cifras salen de
`largos_texto_propio_ver_punto_mesa.py` (en esa carpeta del paquete, con su salida).

## 1. La decisión de la autora, tal cual

«El punto 8 no va como límite: se arregla antes de N6. ver_punto no puede cortar el texto propio por debajo de lo que trae la herramienta de
fragmentos. Proponeme el arreglo más barato que no cambie nada más (subir el límite o paginar con desde), con la misma regresión que
U-NAV-DESDE, como mandato corto.» (20/10/2026, recibida a las 09:25:49.)

## 2. Lo que pasa hoy

- **`ver_punto`** (`familias_nav.py` del 142, `:526-528`) junta en una línea el texto propio de más de 1.500 caracteres y lo corta en 1.499
  más «…», con «cortado en 1.500» en su cabecera. La salida entera tiene un tope de 5.000 (`TOPES`, `:64`) y un corte final (`:578`). Su
  descripción dice «su texto (hasta 1.500 caracteres)» (`:99`).
- **La herramienta de fragmentos** devuelve el texto completo de cada pasaje, sin tope de caracteres (`servidor_mcp_vector.py:195`;
  descripciones, `:96` y `:111`).
- **Cuánto corta:**
  - en el grafo evaluado (E0 de los 128 TOs), 810 de los 10.321 puntos con texto, y 745 de las 8.474 unidades que pueden ser ancla;
  - en el acumulado de las tandas 0 y 1, el que mide N6, 497 de los 5.541 puntos con texto;
  - en la tanda 0 (`--contenido`), 150 de 2.361;
  - el más largo tiene 50.404 caracteres.

## 3. El cambio (la opción A, que la mesa recomienda)

- **El texto propio va entero.** Se saca el corte en 1.499 de `:528`, y la cabecera dice «Texto (N caracteres):» en todos los puntos.
- **El tope de la salida crece solo por el texto que antes se cortaba:** 5.000 más lo que el texto entero pasa del texto cortado de hoy.
  Así, a las secciones de nodos, relaciones e hijos les queda el mismo presupuesto que hoy, carácter por carácter, y sus líneas salen
  iguales.
- **La descripción** pasa de «su texto (hasta 1.500 caracteres)» a «su texto entero» (D-3). Es la única línea que cambia en la definición
  de las herramientas.
- **Por qué no la opción B (paginar con `desde`):**
  - suma un parámetro, un pie y casos nuevos;
  - para leer el punto más largo pide 34 llamadas de 1.500, y el tope de una sesión es 30 (registro, §50, R5);
  - con A, una llamada da lo mismo que fragmentos en una.

## 4. Lo que no cambia

- **Byte a byte:** toda salida de `ver_punto` de un punto con 1.500 caracteres o menos; las demás cinco herramientas de las familias y las
  tres de hoy; el índice por punto, el grafo, Neo4j, el denso y el brazo de fragmentos.
- **En los puntos largos,** todo menos la cabecera del texto y el texto.
- **El bloque de la familia 6** (`cccfcefd…`): ninguna de sus 7 salidas de `ver_punto` está cortada. Queda igual, y se controla.

## 5. Dónde y cómo corre

- **Una copia fuera del repo,** como U-NAV-DESDE, en `fuera_del_repo/unav_verpunto/` (D-4), con su Neo4j propio:
  - la copia, desde HEAD con la cláusula de copias, más los 27 archivos del 142 desde la copia permanente del paquete de la mesa
    (`decisiones_189_mesa/entrega_unav/para_el_repo/c142/`), cada uno con su sha256;
  - los dos índices por punto, desde `fuera_del_repo/indices_banco/`, verificados.
- **Cuándo:** nunca a la vez que otra unidad con Docker o con el denso; después de la carga en Neo4j del T3 de la tanda final; antes del
  rearmado del 142 (D-5).
- **No escribe en el repo.** Entra al repo con el 142: la mesa reemplaza en la entrega `familias_nav.py` y `selftest_familias_nav.py` por los
  de esta unidad, con su sha256, y lo rearma después del sello y de A2.2, antes de N6.

## 6. La regresión, como la de U-NAV-DESDE

1. **El selftest de las familias con Neo4j, en sus dos modos** (`--contenido` sobre la tanda 0 y `--cuentas` sobre el acumulado), con 0
   fallas:
   - T2 mide `ver_punto` contra su tope nuevo, que la función de la herramienta da por punto;
   - un caso nuevo (T12) controla, en cada punto, que la salida de hoy y la nueva difieran solo en la cabecera del texto y en el texto, y
     solo en los puntos largos, y que el texto nuevo sea el propio entero.
2. **Los sha256 de las salidas:**
   - con el texto de los puntos largos devuelto al corte de hoy, dan los de U-NAV-DESDE: `d8c276a8…` (9.302 salidas, tanda 0) y
     `3f98801f…` (22.081, acumulado);
   - con el pie de N5 restituido además, los de N5: `cb5bf051…` y `4ce4712b…`.
3. **Las salidas que cambian,** clasificadas: 150 más 42 con `max_nodos=25` en la tanda 0, y 497 más 125 en el acumulado (las cuentas de la
   mesa; las confirma la corrida). Ninguna en otra herramienta.
4. **El servidor por stdio (T10):** la salida más larga (unos 53.900 caracteres en el acumulado) llega entera al cliente. Si el cliente del
   banco la corta, frenás y decide la autora (D-6).
5. **El bloque de la familia 6:** sus 7 llamadas a `ver_punto` dan la misma salida, y el bloque, su sha256.
6. **F1 no corre:** el brazo de fragmentos no se toca. Lo controla el sha256 de sus archivos, antes y después.
- Todo USD 0. La consola de la parte del acumulado muestra solo cuentas y sha256 (cegamiento de U-MED-VERIF).

## 7. Las decisiones para la firma

1. **D-1, la opción:** A, el texto entero con el tope que crece solo por el texto (recomendada), o B, paginar con `desde`.
2. **D-2, el texto largo en una línea:** hoy, el texto de más de 1.500 caracteres se junta en una línea. La mesa propone dejarlo así, que
   cambia menos; la otra opción es mostrarlo con sus saltos, como el corto.
3. **D-3, la descripción nueva:** «su texto entero», en lugar de «su texto (hasta 1.500 caracteres)».
4. **D-4, el nombre y la carpeta:** U-VERPUNTO, en `fuera_del_repo/unav_verpunto/`.
5. **D-5, cuándo:** después de la carga en Neo4j de T3, sin otra unidad con Docker o con el denso, y antes del rearmado del 142.
6. **D-6, si el cliente del banco corta la salida más larga:** la mesa propone frenar y subir el límite de salida de MCP en los dos brazos
   por igual, declarado.

## 8. El FRENO y el paquete

- El FRENO lleva el paso 0, el diff, los seis puntos del §6 con su script y su salida, la foto del repo (sin cambios), los `.pyc` y el
  grep de convenciones con `LC_ALL=en_US.UTF-8`.
- El paquete `revision_UVERPUNTO/` va con su `manifest.txt` y su copia con `ditto` en la copia permanente, verificada.
- Nada commiteado y nada escrito en la memoria.

## Firma

**FIRMADO por la autora el 20/10/2026,** por mensaje recibido a las 10:01:39 (hoja de ruta de la mesa, §195), tal cual: «Firmo el mandato
corto de ver_punto (decisiones_194_mesa/ver_punto/MANDATO_UVERPUNTO_texto_propio_BORRADOR_mesa.md, sha256
38f6812fbd6935d4677d84988323062e5b699653217ba7f35dfe7436f5e3d369) con D-1, la opción A; D-2, el texto largo con sus saltos de línea, como
el corto, porque los puntos largos son listas y tablas y la herramienta de fragmentos los devuelve con sus saltos; D-3, «su texto entero»;
y D-4, D-5 y D-6 como los propone. Con la D-2, el control T12 sigue igual: solo cambian la cabecera y el texto de los puntos largos.»

En el mismo mensaje, tal cual: «Los ejemplos del brazo de fragmentos: armalos ya, a USD 0, en la misma copia de ver_punto, con los mismos 3
casos resueltos con su herramienta. Entran solo si la familia 6 entra en N7, como dice el mandato de U-NAV.»
