# U-SEG-OFICIAL, S1-quater: la lectura de la etapa 2, controlada (mesa, 13/10/2026)

USD 0, sin API. Nota de la mesa revisora para el registro de la etapa 2 (hoja de ruta de la mesa, §90).
- **Qué no lleva:** marcas, texto de las fichas, ids de unidades ni ids de fichas.
- **Dónde queda la planilla de la lectora:** fuera del repo, en su carpeta, hasta que termine la adjudicación de la autora. En el
  repo quedan su sha256 y su hora (`sello_etapa_2_S1quater.txt`).
- **Cómo controlé:** con el mismo método que la etapa 1 (`registro_lectura_etapa_1_S1quater_mesa.md`), solo por script. No vi
  marcas, texto de las fichas ni el contenido de `trabajo_marcar.py`.

## 1. La lectura

- **Dónde y con qué:** en `fuera_del_repo/lecturas_ciegas/lectura_segmentacion_s1quater/etapa_2/`, con el despacho sellado
  `despacho_lectora_S1quater_etapa_2.md` (`0cae1d21…`) y `claude-opus-5-5`.
- **La sesión:** una sola, `8ac1f8b2…`.
- **El sello:** `planilla_etapa_2.tsv` `bd11e4557a21218f4be2e7db8483adeb28ee2c382349caa0c4f9b974819456b0`, a las 14:36:05 del 13/10/2026.
- **Su FRENO:** `FRENO_lectora_etapa_2_S1quater.md`, con `$HOME` y las cuentas del paso 1. No trae cifras ni resúmenes de lo leído.

## 2. La regla, fijada antes del control

- **La decisión de la autora del §90:** «Para la etapa 2 rige la misma regla de validez que para la etapa 1 (§89), fijada antes de tu
  control». La regla es la de `registro_lectura_etapa_1_S1quater_mesa.md`, §2.
- **El sello:** la mesa la selló a las 14:38:02 del 13/10/2026, antes de mirar la sesión (sha256 `b858969d…`).

## 3. El control de la sesión

- **La carpeta:**
  - las 190 llamadas (119 Read, 70 Bash, 1 Write) quedan dentro de `etapa_2/`, sin `git`, sin tocar el scratchpad ni la memoria. Las
    rutas que marca el control son texto entre comillas de los argumentos;
  - además de lo instalado, en `etapa_2/` quedaron solo `trabajo_marcar.py` y `sello_etapa_2.txt`;
  - los 105 archivos de su `manifest.txt` siguen iguales, y la etapa 1 no se tocó.
- **Las imágenes:**
  - las 104 se abrieron, una vez cada una;
  - en las 60 fichas, todas las imágenes se abrieron antes de la primera escritura de su fila;
  - las fichas se abrieron en el orden de la planilla.
- **El texto de las fichas:** la lectora leyó el archivo por tramos (15 lecturas), sin cortes. Las 60 fichas se le mostraron enteras
  antes de su marca. A dos les falta solo un renglón vacío del final.
- **Cómo se escribieron las filas:** de a una, con 63 llamadas a `trabajo_marcar.py`, en 62 comandos (uno encadena dos).
  - Cada llamada lleva el id de la ficha y los campos de la fila, que la lectora escribió en cada llamada. En una, la nota va sin
    comillas, y el script une sus palabras.
  - 57 fichas se escribieron una vez y 3 dos veces: la lectora corrigió esas filas más tarde, sin volver a abrir sus imágenes, que había
    abierto antes de la primera escritura.
  - 58 de 59 filas se escribieron antes de abrir la primera imagen de la ficha siguiente. La de la ficha 29 del orden se escribió 8
    segundos después de abrir una de las dos imágenes de la 30, y antes de escribir la de la 30.
- **Un programa de Python en línea** (13 renglones, solo `csv`) leyó la planilla e imprimió para la lectora. No escribió nada.
- **`trabajo_marcar.py`** (36 renglones, `ffd14741…`, el mismo que escribió la sesión):
  - **qué usa y qué abre:** solo `sys`, y abre solo `planilla_etapa_2.tsv`, para leerla y reescribirla con la fila nueva;
  - **de dónde salen los valores:** de los argumentos (`sys.argv`). Los valida contra un diccionario de conjuntos fijos de valores
    permitidos, y controla que no traigan tabuladores ni saltos de renglón;
  - **lo que no hace:** no trae ids de ficha ni marcas como datos, no lee las fichas ni las imágenes, y no deriva ninguna marca.
  - Sus literales largos son su docstring y un mensaje de error.
- **La planilla:** 60 filas, todas con marca. Los ids y las páginas son iguales a los de la vacía, y en el mismo orden.
- **La duración, del paso 0 al sello:** 11 min 32 s, con 104 imágenes. La lectora de la etapa 2 de S1-ter tardó 11 min 57 s, con 164
  imágenes, con el mismo modelo.
- **Un error de la mesa, corregido antes de aplicar la regla:** la primera cuenta de escrituras no veía la llamada encadenada, y una
  segunda versión partía las notas entre comillas. La cuenta de arriba usa un tokenizador de shell. Con ese mismo tokenizador, la etapa 1
  da lo mismo que en su registro.

## 4. La regla, aplicada: la etapa 2 vale

- **Las imágenes:** la lectora abrió las imágenes de cada ficha antes de escribir su marca.
- **De dónde salen las marcas:** de su lectura. Las pasó ella, ficha por ficha, como argumentos.
- **El script:** solo escribió en la planilla lo que ella decidió. Vale igual, y se declara.
- **Se declaran también:** las tres filas corregidas sin volver a abrir sus imágenes, y la fila de la ficha 29, escrita después de
  abrir una imagen de la siguiente.
- **Un límite, como en la etapa 1:** lo que se observa es el orden de las llamadas.
