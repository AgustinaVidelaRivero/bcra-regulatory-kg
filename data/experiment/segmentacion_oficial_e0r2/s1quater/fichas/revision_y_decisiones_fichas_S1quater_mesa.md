# U-SEG-OFICIAL, fichas de S1-quater: revisión de la mesa, el renglón del control a ciegas y las declaraciones de los dos tramos (13/10/2026)

USD 0, sin API.
- **Qué es:** una nota de la mesa revisora que entra con el registro de las fichas, por pedido de la autora (hoja de ruta de la mesa,
  §87 y §88).
- **Lo que no cambia:** ningún archivo de la ejecutora en `s1quater/fichas/`.
- **Lo que no lleva:** ids de unidades, el renglón ni el id de su ficha.
- **Los tramos:** las fichas corrieron en dos tramos de la misma sesión de la ejecutora (`912e1004…`). El primero frenó en el control a
  ciegas (`FRENO_S1quater_fichas.md`). El segundo siguió después del «seguí» de la mesa (`FRENO_S1quater_fichas_tramo_2.md` y la
  sección «Tramo 2, después del seguí» del REPORTE).

## 1. El renglón que marcó el control a ciegas

- **Lo que pasó:** en el primer tramo, el control a ciegas (`s1ter/scripts/control_ciego_fichas_S1ter.py`, sin cambios) marcó en la
  etapa 1 un renglón con un término de su lista, donde el despacho pedía 0. La ejecutora frenó sin mirarlo.
- **La regla de la autora,** fijada antes de que nadie supiera qué era el renglón (§87, recibida a las 11:04:39 y sellada por la mesa a
  las 11:04:53), tal cual:
  - «si el término está en el texto de la unidad o en su herencia, tal como los da la E0, es una falsa alarma del control: se declara y
    se sigue;
  - si está en algo que agrega la ficha (encabezados, rótulos, nombres de archivo o de imagen), es una filtración: se corrige el script
    de las fichas con una adenda al diseño y se rehacen las fichas;
  - nadie mira el renglón: ni vos, ni las ejecutoras, ni yo».
- **El diagnóstico de la mesa,** por script, sin mostrar el renglón:
  - **cómo:** el script encuentra el renglón como el control, reconstruye cada ficha con las funciones de formato de
    `fichas_S1quater.py` y la E0, y etiqueta cada renglón por su procedencia;
  - **cómo se probó antes:** sobre la carpeta de S1-ter reconstruye igual y no marca nada; con dos E0 modificadas a propósito, ubica
    bien un término puesto en el número de una unidad y otro puesto en su texto propio;
  - **el resultado:**
    - el renglón es el rótulo del número que la segmentación le asignó a la unidad;
    - el término que coincide es `1\.16`. Cae en el número, que viene de la E0, y no en la parte fija del rótulo;
    - según la E0, `1.16` está también en el texto propio de la unidad y en su herencia.
- **La decisión de la autora del 13/10/2026 (§88), tal cual:** «confirmo que el renglón es falsa alarma». La mesa la había propuesto
  como falsa alarma, señalando que el renglón es un rótulo. Por su pedido, se declara:
  - el renglón es un rótulo que agrega la ficha. Lo que coincidió es el número de la E0, que el diseño muestra a propósito (§5: «el
    número que le asignó la segmentación»);
  - aplicar la regla a un rótulo era un caso límite. La autora lo resolvió después de conocer el diagnóstico, con el criterio de qué
    agrega la ficha y qué viene de la E0;
  - la lista del control trae el nombre de una población de S1-ter, la de 1.16, que S1-quater no tiene.
- **Nadie miró el renglón.** Ni él ni su número aparecen en la transcripción de la ejecutora ni en la de la mesa.
- **Lo que no pudo verificar la ejecutora:** declara el diagnóstico como de la mesa, NO VERIFICADO en su sesión, porque verificarlo
  exigía leer el renglón.

## 2. La revisión de los dos tramos

- **El paquete de la ejecutora:** 43 de 43 contra su `manifest.txt` (`aef22b72…`). Sus copias de `s1quater/fichas/` son iguales a las
  del repo.
- **La reproducción, sobre copias:**
  - **las fichas,** desde el orden sellado y la E0 de `2374968a`: el registro da `5a469787…`, el sellado. La carpeta, las planillas y
    los dos `manifest.txt` (`110565d7…` y `37580fbc…`) son iguales;
  - **el control a ciegas:** su salida es igual byte a byte, con el mismo renglón marcado;
  - **`verificar_carpeta_lectora_S1ter.py`:** la salida es igual byte a byte (96 de 96 y 105 de 105);
  - **el paso 1 de la lectora:** 96 y 105 OK;
  - **el tar del tramo 2:** igual a la carpeta, con el mismo sha256 que el de resguardo (`86275bfd…`), porque ningún archivo cambió
    entre los dos.
- **El sello de los controles a ciegas** lleva 7 archivos, y los 7 dan su sha256. El «seguí» nombraba 5 salidas, y la ejecutora
  partió dos de ellas:
  - el paso 1 de la lectora, en dos archivos: las cuentas (`controles/paso1_lectora_S1quater_cuentas.txt`, en el repo) y la lista
    entera, que nombra cada archivo con su id opaco y sus páginas (`NO_ABRIR_paso1_lectora_S1quater_completo.txt`, en su paquete);
  - `verificar`, en dos archivos: sobre la carpeta y sobre el tar extraído (`controles/verificar_carpeta_lectora_S1quater.txt` y
    `_tar.txt`, con la misma salida);
  - las otras tres son la salida completa del control a ciegas, sus cuentas y el tar.
- **Las sesiones** (registros desde cada despacho):
  - sin carpetas vedadas;
  - nada del paquete de la mesa; del paquete del sorteo, solo el orden sellado, como argumento;
  - escrituras en el repo solo en `s1quater/fichas/`, y nada en `.claude/` ni en la memoria;
  - sin esperas programadas;
  - ningún `NO_ABRIR_` abierto;
  - ningún id de unidad impreso.
- **Unidades vistas, con el criterio de la adenda 4:** ninguna en ninguno de los dos tramos, ni en las herramientas ni en todo el texto
  de la sesión.

## 3. Declaraciones

- **a. La prueba del diseño necesitó tres scripts que el despacho no nombraba:** `sorteo_S1quater.py`, `poblaciones_S1quater.py` y
  `regresion_S1quater.py`.
  - La ejecutora los copió de HEAD, con los sha256 de `sello_diseno_S1quater.txt`.
  - La omisión es de la mesa: al probar el despacho copié la carpeta entera de scripts y no vi la dependencia.
- **b. El `python3` del sistema (3.12):** la ejecutora lo usó en el primer tramo para tareas auxiliares, sin tocar el repo (leer dos
  JSON, actualizar su checkpoint, armar el manifiesto de su paquete). Los scripts del diseño y los controles corrieron con el del
  `.venv` (3.10), y en el segundo tramo, todo.
- **c. El registro de las fichas y las planillas vacías** quedaron en el paquete de la ejecutora sin el prefijo `NO_ABRIR_`.
  - El registro trae el número que la segmentación le asignó a cada ficha.
  - Se tratan como `NO_ABRIR_`: no se abren y se controlan por sha256.
  - El registro no va a la carpeta de la lectora; las planillas, sí, como en S1-ter.
- **d. La unidad de más de la regresión** (la que entra solo por la doble cuenta de la ficha E2-033 de S1-ter) no estaba en la
  población de ningún estrato ni en la muestra. Ya salía por solapar una unidad leída en S1-ter.
- **e. El `sleep 60` del primer tramo no corrió:** la herramienta de la sesión lo bloqueó antes de correrlo, y no hubo espera.
  - La revisión de la mesa del §87 lo había descripto como una espera activa: el control de la mesa marcó la llamada sin mirar su
    resultado. Queda corregido.
  - El «seguí» repetía esa descripción.

## 4. La carpeta de la lectora, instalada

- **Cuándo:** la mesa la instaló el 13/10/2026 a las 13:24:04, como en S1-ter (§53), en
  `fuera_del_repo/lecturas_ciegas/lectura_segmentacion_s1quater/`.
- **Qué lleva:**
  - las fichas del tar sellado;
  - en cada etapa, la planilla vacía (`planilla_etapa_N.tsv`, la sellada) y su `manifest_planilla_etapa_N.txt` (`eb7c384f…` y
    `067bbcd3…`).
- **Los controles:**
  - los dos comandos del paso 1 de la lectora dan 96 OK más la planilla en la etapa 1, y 105 OK más la planilla en la etapa 2;
  - el control a ciegas de las planillas da 0 en todo, con los ids opacos iguales a los de las fichas y en orden;
  - 207 archivos, sin enlaces ni `.DS_Store`.
- **Lo que no se abrió:** nada.
