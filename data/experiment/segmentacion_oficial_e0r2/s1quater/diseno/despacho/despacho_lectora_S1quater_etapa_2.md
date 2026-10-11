# Despacho de la lectura a ciegas de S1-quater, etapa 2 (mesa, 11/10/2026)

Sale del despacho v3 de S1-ter, etapa 2, con el mismo criterio, tal cual, y tres cambios por los incidentes de la lectura de
S1-ter (`s1ter/lectura/incidentes_lectura_S1ter.md`): las imágenes, ficha por ficha (paso 2); ningún archivo fuera de la carpeta,
tampoco en el scratchpad de la sesión; y la salida de los pasos 0 y 1, pegada tal cual (paso 7). Sellado con el diseño de
S1-quater, antes de que exista la E0 corregida. **No está despachado: se despacha después del sorteo, con la carpeta armada.**

## Para la autora (esta parte no se pega)

1. **La carpeta de la etapa:** `~/INGENIERIA IA/TESIS/fuera_del_repo/lecturas_ciegas/lectura_segmentacion_s1quater/etapa_2/`.
   - Lleva las fichas que arma `scripts/fichas_S1quater.py` desde el orden sellado, con su `manifest.txt`, sellado al armarla.
   - Lleva también `planilla_etapa_2.tsv` y `manifest_planilla_etapa_2.txt` (la opción 1 de S1-ter), que la mesa copia
     después de armar las fichas.
2. **Al crear la sesión en la app de escritorio, elegí como carpeta la de la etapa:** `etapa_2/`, no la carpeta de arriba, ni
   `fuera_del_repo/`, ni el repo. Si la sesión se abre en otra, el paso 0 la frena sin abrir nada; cerrala y abrí una nueva.
3. **La etapa 2 se abre solo cuando la etapa 1 esté sellada** (el FRENO de la etapa 1 trae el sello). Es una sesión nueva, distinta de la
   de la etapa 1.
4. **Pegá el texto de abajo tal cual.**

## Para pegar

Tu tarea es una lectura, USD 0 y sin API. Trabajás solo con los archivos de la carpeta desde la que se abrió esta sesión: no abras nada
fuera de ella, no busques otras fuentes, no uses git y no escribas fuera de esta carpeta: tampoco en el scratchpad de la sesión. Si
necesitás un archivo de trabajo, crealo en esta carpeta, con un nombre que empiece con `trabajo_`.

0. Controlá con `pwd` que la carpeta actual sea
   `/Users/agustinavidelarivero/INGENIERIA IA/TESIS/fuera_del_repo/lecturas_ciegas/lectura_segmentacion_s1quater/etapa_2`. Si no lo es,
   frená sin abrir nada: decí cuál es la carpeta actual y nada más.
1. Controlá la carpeta y mostrá la salida de los dos comandos. Si algún archivo no da OK, frená.
   - `awk 'NR>2 && NF{print $1"  "$3}' manifest.txt | shasum -a 256 -c -`
   - `shasum -a 256 -c manifest_planilla_etapa_2.txt`
2. **Qué se lee.** Todas las fichas de `fichas_etapa_2.md`, en su orden. La unidad que se califica es el texto que trae la ficha. Para
   saber si está bien cortada, comparala con la imagen de su página del PDF (los `.png` de la carpeta): la referencia es la imagen.
   Cada ficha dice qué número le asignó la segmentación a la unidad, o que no tiene número: es el número que se compara en el (5).
   Para cada ficha, abrí sus imágenes antes de marcarla, y escribí su fila en la planilla antes de pasar a la siguiente.
   - Cada ficha trae la unidad que se califica y, después, la unidad que le sigue en el documento. La que sigue está solo para ver
     dónde termina la primera y dónde empieza la segunda: **no se califica**. Una fila de la planilla por ficha, sobre la primera
     unidad. Si la unidad que se califica está partida por tamaño, la ficha trae todas sus partes y se califica entera.
   - Si la unidad que sigue no empieza o no termina donde corresponde según la imagen, decilo en nota, aunque la primera esté bien.
3. **El criterio** (mandato de la unidad, `docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md:284-292`, tal cual):
   - Una unidad es correcta si: (1) empieza donde empieza su punto; (2) termina donde termina; (3) no trae texto de otro punto ni
     restos de encabezados o pies de página; (4) no le falta texto propio; y (5) su número es el del punto.
   - Tres reglas para los casos dudosos. Una parte de una unidad partida por tamaño es correcta si corta en un límite de ítem y está
     declarada. Los guiones de silabeo no son error. Un párrafo sin numerar es correcto si cubre exactamente ese párrafo.
   - Dos clases de error; cada error lleva su clase y su subclase. De corte: empieza fuera de su punto, termina fuera de su punto, le
     falta texto propio, trae texto de otro punto, o su número no es el del punto. De limpieza: restos de encabezado o restos de pie de
     página.
4. **Dónde marcás:** en `planilla_etapa_2.tsv`, una fila por ficha, ya con `ficha` y `paginas`. No cambies esas dos columnas, ni el
   orden, ni el encabezado. Separador: tabulación. En ninguna celda va una tabulación ni un salto de renglón.
   - `marca`: `correcta`, `error` o `dudosa` (si no podés decidir; decí por qué en `nota`).
   - `clase`, solo si es `error`: `corte` o `limpieza`.
   - `subclase`, solo si es `error`. De corte: `empieza_fuera`, `termina_fuera`, `falta_texto_propio`, `trae_texto_de_otro_punto` o
     `numero_equivocado`. De limpieza: `restos_encabezado` o `restos_pie`.
   - `subclase_adicional`: una segunda subclase de las mismas listas, si hace falta.
   - `limpieza`: `restos_encabezado` o `restos_pie`, si además del corte hay restos. Si no, vacía.
   - `nota`: lo que quieras dejar dicho de la ficha, sea cual sea la marca. Si es `error` o `dudosa`, decí dónde está, con la página.
     Si el texto heredado (los títulos que la ficha muestra arriba de la unidad) no corresponde a la página, decilo en nota, aunque la
     marca sea correcta.
5. **Checkpoint:** si te acercás al límite de contexto, guardá la planilla con lo marcado hasta ahí, escribí en `estado_etapa_2.txt` la
   última ficha marcada y cuántas faltan, y frená sin sellar.
6. **Sello,** cuando todas las filas tengan `marca`:
   - `shasum -a 256 planilla_etapa_2.tsv > sello_etapa_2.txt`
   - `date '+%Y-%m-%d %H:%M:%S %z' >> sello_etapa_2.txt`

   Después del sello no cambies la planilla.
7. **FRENO**, con:
   - la salida de los pasos 0 y 1, pegada tal cual, sin resumir;
   - las rutas de la planilla y de su sello;
   - el modelo con que corrés esta sesión;
   - el contenido de `sello_etapa_2.txt`.

   Nada más: ni cifras, ni resúmenes de lo leído.
