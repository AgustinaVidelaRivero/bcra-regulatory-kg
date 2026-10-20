# Mandato U-REMISIONES-SUBPUNTOS: la remisión a un punto padre o a una sección, como quinto paso de la re-aplicación (firmado el 20/10/2026)

**FIRMADO por la autora el 20/10/2026** (por mensaje recibido a las 12:42:26; hoja de ruta de la mesa, §197), sobre el borrador de la §195
con la cuenta de hubs de la §196 (sha256 `09bbcf57…`, en el paquete de la mesa, `decisiones_195_mesa/remisiones/`), con D-1, D-2 (la opción
B, no la E), D-3, D-4 y D-5 como dice la sección «Firma», que manda sobre su texto. El texto firmado es el del borrador, con este
encabezado y esa sección. USD 0, sin API. Las cifras salen de los scripts de `remisiones_sin_resolver_por_causa_mesa.md` y de
`decisiones_196_mesa/remisiones_hubs/`, en el paquete de la mesa.

## 1. De dónde sale

- **El registro, §41:** las remisiones sin resolver del acumulado, por clase de causa; si una clase se corrige por código, su mandato, con
  su medición, para que entre antes del corte del sábado 24/10/2026 a las 12:00 (R5).
- **La precisión 2 de la firma de la re-aplicación única** (20/10/2026, recibida a las 10:01:39), tal cual: «Las remisiones: si su mandato
  se firma antes de la corrida, entran como quinto paso (+ las remisiones), después de C1, con su regla de aislamiento como las otras
  piezas. Solo cambian aristas remite_a, cada una con su causa, y las que D ya cambió en el paso 2 se informan aparte. Si una arista cambia
  por las dos piezas, frena y decido yo.»
- **El hallazgo de la frontera de ancla y chunk** (`data/experiment/bakeoff_embeddings/hallazgo_frontera_ancla_chunk.md`): un punto de la
  norma puede existir solo repartido entre sus subpuntos.

## 2. Lo que pasa hoy

- `resolver` (`r1_referencias.py:1139-1190` en HEAD) busca nodos anclados en el punto exacto que se cita. Si el punto existe en la E0 y no
  tiene nodos, la cita queda irresoluble con causa `punto_sin_nodos` (`:1190`), aunque sus subpuntos tengan nodos.
- **En el acumulado de las tandas 0 y 1:** 368 citas con cola y 366 sin cola son de ese caso, a un punto padre (265 / 264) o a una sección
  (103 / 102). Son la única clase de las remisiones sin resolver (906 / 889) que se corrige por código. Las demás van al grafo corregido,
  declaradas, y las que citan un TO de la tanda final se resuelven solas cuando entra (251 / 246, NO VERIFICADO hasta el acumulado de las
  tres tandas).

## 3. El cambio (la opción E, que la mesa recomienda)

- **Una opción nueva del resolvedor, apagada por defecto,** y su bandera en la cadena (`--remisiones-a-subpuntos`, en `correr_cadena_r2`
  de `ensamblar_tanda0.py`). Sin la bandera, la salida es la de siempre, byte a byte.
- **Con la bandera, en la rama de `punto_sin_nodos`:** si el punto o la sección citada tiene subpuntos con nodos, los destinos son los nodos
  de la frontera de cada rama: en cada rama del subárbol, el primer subpunto con nodos (D-2). Si no tiene, la cita sigue como hoy.
- **La arista no cambia de forma:** `destino` es la unidad citada, `alcance` el de `alcance_remision` (interna o externa), y `evidencia` el
  tramo. Las propiedades siguen siendo las tres de `PROPIEDADES_REMISION` (`modelos_r2.py:175`), así que S30 y S31 de las shapes no
  cambian.
- **La causa va en el registro de remisiones:** la cita lleva las unidades de su frontera, para que cada arista nueva se pueda contar con su
  causa.
- **El código parte de los blobs de D** (`ensamblar_tanda0.py` `58e736db` y `r1_referencias.py` `84e8831f`, del paquete de la segunda pasada
  de U-PROC-HERENCIA), porque D toca los mismos dos archivos y entra antes.

## 4. El selftest y la medición

1. **El selftest de la opción,** con grafos de juguete: un punto padre con hijos con nodos; una sección; una rama cuyo primer punto con
   nodos está más abajo que el de otra rama (la frontera); un punto sin subpuntos con nodos (sigue `punto_sin_nodos`); el origen dentro del
   subárbol citado (D-3); y la opción apagada, igual a hoy.
2. **Sin la bandera, sobre el acumulado de las tandas 0 y 1** (los dos grafos): el `kg.json` y el registro de remisiones, con el sha256 del
   sello.
3. **Con la bandera, sobre el mismo acumulado:**
   - las citas que se resuelven y las `remite_a` nuevas, una por una por código, con su causa. Tienen que dar las cuentas de la mesa (368 y
     25.763 con cola; 366 y 25.524 sin cola, con E y sin D-3), o explicar la diferencia;
   - solo se agregan `remite_a`: ninguna sale, ningún otro predicado cambia, ningún nodo cambia, y toda cita nueva era `punto_sin_nodos`
     sin la bandera;
   - las shapes y la suite, regla por regla, con las regresiones declaradas;
   - **los hubs,** con la regla de la familia 5 (`familias_nav.py` del 142, `:33-34` y `:62`: grado en el 1 % más alto del grafo
     servido): el umbral y cuántos nodos son hub sin la bandera y con ella, cuántos entran a la lista y cuántos salen, por tipo de nodo,
     en los dos grafos. Las nuevas `remite_a` suben el grado de sus orígenes y de sus destinos, y N6 se mide sin ellas;
   - la validación de los modelos r2 y R19 («solo código», como en D).
4. **En la re-aplicación, como quinto paso** (después de C1), sobre el acumulado de las tres tandas, con la regla de la precisión 2. Las
   `remite_a` que D cambió en el paso 2 se informan aparte, y si una arista cambia por las dos piezas, frena.

## 5. Dónde y cuándo

- **La sesión abre desde** `~/INGENIERIA IA/TESIS/fuera_del_repo/remisiones_subpuntos/` (D-4). Trabaja sobre una copia del repo (rsync sin
  `.git`, `.venv`, `.env`, `NO_ABRIR_`, `*_SOLO_MESA*` ni enlaces; nunca un `git clone`). **No usa Neo4j ni Docker.** No escribe en el repo.
- **Cuándo:** se despacha apenas se firme, el miércoles 21. Su FRENO y su revisión van antes de la corrida de la re-aplicación del jueves 22.
  Si no está lista para entonces, rige la precisión 1 de la firma de la re-aplicación: se avisa antes de la corrida y decide la autora.
- **Su commit** va después del sello de la tanda final y después del de D, porque `ensamblar_tanda0.py` y `r1_referencias.py` son dos de
  las 78 rutas. Lo prepara la mesa, con una fila nueva en la tabla de reprocesamiento.

## 6. El cegamiento

- Rige el §7 bis de U-PROC-HERENCIA: códigos, unidades y conteos, nada de contenido de nodos de la tanda 1 ni de la tanda final, y ninguna
  cifra ni lista por estado de E3.
- La consola muestra solo cuentas y sha256. Las listas de aristas van por código de id.

## 7. El FRENO y el paquete

- El paso 0 (con `pwd`), el diff contra los blobs de D, el selftest, las mediciones del §4 con su script y su salida, la foto del repo (sin
  cambios), los `.pyc` y el grep de convenciones con `LC_ALL=en_US.UTF-8`.
- El paquete `revision_UREMISIONES_SUBPUNTOS/`, con su `manifest.txt` y su copia con `ditto` en la copia permanente, verificada.
- Nada commiteado y nada escrito en la memoria.

## 8. Las decisiones para la firma

1. **D-1, corregir o declarar:** corregir esta clase, como quinto paso (recomendado), o declararla y que vaya al grafo corregido.
2. **D-2, los destinos** (con cola; sin cola entre paréntesis):
   - **E, la frontera de cada rama** (recomendada): 368 citas (366), 25.763 `remite_a` nuevas (25.524), con una mediana de 23 nodos por cita;
   - B, el primer nivel con nodos de todo el subárbol: las mismas citas y 14.049 (13.856). Deja afuera las ramas cuyo primer punto con
     nodos está más abajo;
   - C, los hijos inmediatos: 364 (362) y 14.004 (13.811);
   - A, el subárbol entero: 368 (366) y 53.819 (52.350).
   Hoy el grafo tiene 26.258 `remite_a` con cola y 22.277 sin cola: E casi las duplica.
3. **D-3, el origen dentro del contenedor:** si el origen está dentro del subárbol que cita (8 de 404 citas con cola), los nodos de su propia
   unidad no son destino, como en la autorreferencia (recomendado).
4. **D-4, el nombre y la carpeta:** U-REMISIONES-SUBPUNTOS, en `fuera_del_repo/remisiones_subpuntos/`.
5. **D-5, la declaración en N7 y en el pre-registro de B6.3:** N6 se midió sin estas `remite_a` y sin los hubs que agregan (las cifras
   del §4, punto 3, y del quinto paso), como se declara para C1 (registro, §47) (recomendado).

## Firma

**FIRMADO por la autora el 20/10/2026,** por mensaje recibido a las 12:42:26 (hoja de ruta de la mesa, §197), tal cual: «Firmo el mandato
de las remisiones (decisiones_195_mesa/remisiones/MANDATO_UREMISIONES_SUBPUNTOS_BORRADOR_mesa.md, sha256
09bbcf5792724180a99c09c39de47fb4cf4661c3f60174bfd8175ce9f354aad1) con D-1, corregir esta clase como quinto paso de la re-aplicación; D-2,
la opción B y no la E, porque ver_remisiones agrupa las remite_a por el punto citado, así que en esa herramienta el agente ve lo mismo con B
que con E, y B lo hace con la mitad de las aristas y menos hubs nuevos (89 contra 142 en el sin cola); y D-3, D-4 y D-5 como los proponés.
Las cuentas que controla la medición pasan a ser las de B (368 y 14.049 con cola; 366 y 13.856 sin cola, sin D-3), o la diferencia
explicada.»
