# U-SEG-OFICIAL, S1, punto 8 — regla de comparación del censo de renglones

Escrita el 06/10/2026, antes de correr el censo (su sha256 y su hora quedan en `censo_renglones_S1.json`, clave
`regla`). La aplica `scripts/censo_renglones_S1.py` sobre la salida de la corrida de S1 (`e0/`). Si un resultado no
cierra, se corrige la cifra o se declara, no la regla. Fuentes: tercera nota al pie del mandato (`2faff14`), su
corrección en la nota de `d59921f`, la nota del hallazgo 1.16 (`0a3ac81`) y la de S0-2 (`26c6502`).

Versión 2. La versión 1 (sha256 `636cf3ffdcca360c…`, 18:34) se reemplazó a las 18:37, antes de correr el censo: recorría
los renglones en una sola pasada y un renglón del índice podía consumir, como «otra página», la entrada del renglón de
cuerpo con el mismo texto, que quedaba después en la lista sin serlo. La versión 2 empareja primero en la misma página
y solo después en otra, y solo para renglones de páginas de cuerpo.

## Qué es un renglón del PDF

Un renglón es una `Linea` de `e0_lib.extraer_lineas(pdf)`: las palabras que extrae pdfplumber, agrupadas por altura y
unidas por un espacio. Es el texto sobre el que E0 define su cobertura. Lo que pdfplumber no extrae (imágenes, texto
dibujado) queda fuera de este censo; la lectura de cortes del punto 7, contra la página renderizada, lo cubre en su
muestra.

## Entradas de las unidades

Texto normalizado: espacios colapsados, sin espacios en los extremos. Por TO, tres multiconjuntos, cada entrada con
sus páginas:
- (U) los renglones del `texto` de cada chunk de `chunks_<to>.json`, con las páginas del chunk, salvo los de un bloque
  de tabla serializada (`[TABLA …` a `[FIN TABLA …`);
- (H) los renglones de los tramos `encabezado` de la herencia (títulos de sección y de punto), una vez por (unidad de
  origen, texto), con las páginas del tramo;
- (T) los renglones de `lineas_e0` (página y texto) de los segmentos de `tablas_<to>.json` de una tabla con chunk
  dueño.

## Clases de cada renglón

1. **Primera pasada, misma página**, para los renglones de todas las páginas, en orden de página y de arriba abajo:
   consume una entrada de U, si no de H, si no de T, con el mismo texto y cuyas páginas incluyan la del renglón. Es
   **en una unidad** (texto propio, encabezado heredado o tabla serializada).
2. **Segunda pasada, otra página**, solo para los renglones de páginas con rol `cuerpo` que quedaron sin entrada:
   consume una entrada de U o de H con el mismo texto en otra página. Es en una unidad, y se cuenta aparte
   (`en_unidad_otra_pagina`).
3. **Rol de página.** La página no tiene rol `cuerpo` (rol de `pies_<to>.json`, `paginas_detalle`, el de la escalera
   de e0-r2). Excepción: toda página con rol `portada` o `indice` que no sea la primera del documento va a la **lista
   de páginas de portada o de índice**, con todos sus renglones, cuántos son de texto corrido y cuántos están en una
   unidad.
4. **Rol de encabezado o de pie.** El renglón está entre los quitados por la zona de encabezado o de pie
   (`estructura_<to>.json`, `accounting.detalle_descartes`, página y texto) y su forma (minúsculas, cada número
   reemplazado por `#`, espacios colapsados) aparece entre los quitados de otra página del mismo documento. Si no se
   repite, va a la **lista**, como `encabezado_o_pie_no_repetido`.
5. **Sin unidad ni rol.** Todo lo demás va a la **lista**, como `sin_unidad_ni_rol`.

Texto corrido: renglón sin huecos de columna (`ngaps == 0`) y de 55 caracteres o más (el criterio de prosa de
`s0_1/scripts/censo_r3b.py:35`).

## Qué se reporta

- Por TO: renglones del PDF; en unidad (U, H y T), con `en_unidad_otra_pagina` aparte; por rol de página; por
  encabezado o pie repetido; y la cifra del censo: los `encabezado_o_pie_no_repetido` más los `sin_unidad_ni_rol`,
  con su lista de páginas y renglones. Aparte, las páginas de portada o de índice que no son la primera, con sus
  renglones, cuántos son de texto corrido y cuántos están en una unidad.
- Control: las 7 páginas que pasaron a índice en S0-2 y no son la primera de su documento (adfsp 3, ceninf 2, cirmo3
  3 y 4, nmaeef 2 y 14, ri2_ae 13) tienen que estar en la lista de páginas de portada o de índice.
- Aparte, como información: los renglones de U que no encontraron renglón del PDF.

## Hallazgo 1.16: cierre de una lista dentro del último ítem

Una línea aparte del censo, con su regla:
- Se recorre el árbol de `estructura_<to>.json`. Un nodo padre con dos o más hijos de tipo punto, todos sin hijos
  propios, es una lista; su último hijo es el último ítem.
- Corte de párrafo dentro del texto de una unidad: un renglón que empieza con mayúscula (A–Z, Á, É, Í, Ó, Ú, Ñ) y
  sigue a un renglón que termina en punto o en dos puntos.
- Caso: el último ítem tiene al menos un corte de párrafo y ninguno de los ítems anteriores de la lista lo tiene. Se
  lista con el id, la página y el primer renglón después del corte (el cierre candidato).
- Calibración: la regla se corre también sobre `pro` (`e0_chunking/salida_tanda0_r2b/`), que no es de los 152, y
  tiene que encontrar `pro::1.1.2.7` (PDF p. 3). No tiene piso: la revisión lee los casos.
