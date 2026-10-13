# U-SEG-OFICIAL, S1-quater: la lectura de la etapa 1, controlada (mesa, 13/10/2026)

USD 0, sin API. Nota de la mesa revisora para el registro de la etapa 1 (hoja de ruta de la mesa, §89).
- **Qué no lleva:** marcas, texto de las fichas, ids de unidades ni ids de fichas.
- **Dónde queda la planilla de la lectora:** fuera del repo, en su carpeta, hasta que termine la adjudicación de la autora. En el
  repo quedan su sha256 y su hora (`sello_etapa_1_S1quater.txt`).
- **Cómo controlé:** solo por script, sobre copias de las transcripciones y de la carpeta. No vi marcas, texto de las fichas ni el
  contenido de `trabajo_marcar.py`.

## 1. La lectura

- **Dónde y con qué:** en `fuera_del_repo/lecturas_ciegas/lectura_segmentacion_s1quater/etapa_1/`, con el despacho sellado
  `despacho_lectora_S1quater_etapa_1.md` (`dc1ebcfe…`) y `claude-opus-5-5`, el modelo de S1-ter.
- **El sello:** la lectora selló la planilla a las 14:04:27 del 13/10/2026: `planilla_etapa_1.tsv`
  `5414ddf1d7365f9e00231e52811b248b6590d622f59c2d27ecee90597e6838dc`.
- **Su FRENO:** `FRENO_lectora_etapa_1_S1quater.md`, con la carpeta personal reemplazada por `$HOME` y las cuentas del paso 1 en lugar
  de su salida entera. No trae cifras ni resúmenes de lo leído.
- **Las sesiones en esa carpeta:** dos.
  - **La primera** (`6dc89c01…`) recibió el despacho y, 3 segundos después, quedó interrumpida por la autora («[Request interrupted
    by user]»), sin ninguna respuesta del modelo ni llamadas a herramientas.
  - **La lectura es la segunda** (`925d760b…`), que recibió el despacho entero.

## 2. La regla de la autora, fijada antes del control, tal cual

Recibida y sellada por la mesa a las 14:08:30 del 13/10/2026, antes de mirar la sesión (sha256 `1be7654a…`):
- «vale si la lectora abrió las imágenes de cada ficha antes de decidir su marca, y si las marcas salen de su lectura. Si un script solo
  escribió en la planilla lo que ella decidió, vale igual y se declara;
- no vale si alguna ficha se marcó sin abrir sus imágenes, o si las marcas las calculó un script. En ese caso la planilla queda sellada y
  conservada, se declara, y la etapa 1 se lee de nuevo en una sesión nueva, con el mismo despacho y una carpeta reinstalada desde el tar
  sellado;
- ni vos ni yo vemos marcas, texto de fichas ni el contenido de trabajo_marcar.py.»

## 3. El control de la sesión

- **La carpeta:**
  - las 200 llamadas (96 Read, 103 Bash, 1 Write) quedan dentro de `etapa_1/`, sin `git`, sin tocar el scratchpad ni la memoria. Las
    rutas que marca el control son texto entre comillas de los argumentos;
  - en `etapa_1/` hay, además de lo instalado, solo `trabajo_marcar.py` y `sello_etapa_1.txt`;
  - los 96 archivos de su `manifest.txt` siguen iguales, y la etapa 2 no se tocó.
- **Las imágenes:**
  - las 95 se abrieron, una vez cada una;
  - en las 90 fichas, todas las imágenes se abrieron antes de la primera escritura de su fila;
  - 89 de 89 filas se escribieron antes de abrir la primera imagen de la ficha siguiente.
- **El texto de las fichas:**
  - la lectora leyó los primeros 120 renglones del archivo con Read y el resto por tramos, con `sed -n`, sin cortes en las salidas;
  - las 90 fichas se le mostraron enteras antes de su marca. Solo falta el renglón vacío del final del archivo.
- **Cómo se escribieron las filas:** de a una, con 91 llamadas a `trabajo_marcar.py`.
  - Cada llamada lleva 7 argumentos: el id de la ficha y los campos de la fila, que la lectora escribió en cada llamada.
  - 89 fichas se escribieron una vez, y una, dos: la lectora corrigió su fila 145 segundos después, sin volver a abrir sus imágenes, que
    había abierto antes de la primera escritura.
  - Una nota nombra otra ficha.
- **`trabajo_marcar.py`** (48 renglones, `0322375d…`, el mismo que escribió la sesión):
  - **qué usa y qué abre:** solo `sys`, y abre solo `planilla_etapa_1.tsv`, para leerla y reescribirla con la fila nueva;
  - **de dónde salen los valores:** de los argumentos (`sys.argv`). Los valida contra conjuntos fijos de valores permitidos de marca y
    de clase, y controla que no traigan tabuladores ni saltos de renglón;
  - **lo que no hace:** no trae ids de ficha ni marcas como datos, no lee las fichas ni las imágenes, y no deriva ninguna marca.
- **La planilla:** 90 filas, todas con marca. Los ids y las páginas son iguales a los de la vacía, y en el mismo orden.
- **La duración, del paso 0 al sello:** 11 min 1 s, con 95 imágenes. La lectora de la etapa 1 de S1-ter tardó 10 min 45 s, con 138
  imágenes, con el mismo modelo.

## 4. La regla, aplicada: la etapa 1 vale

- **Las imágenes:** la lectora abrió las imágenes de cada ficha antes de escribir su marca. Es lo que se puede observar de cuándo la
  decidió.
- **De dónde salen las marcas:** de su lectura. Las pasó ella, ficha por ficha, como argumentos.
- **El script:** solo escribió en la planilla lo que ella decidió. Vale igual, y se declara.
- **Se declaran también:**
  - la fila corregida una vez, sin volver a abrir sus imágenes;
  - la primera sesión, interrumpida antes de empezar.
- **Un límite:** lo que se observa es el orden de las llamadas. La decisión misma no deja rastro aparte de ellas.
