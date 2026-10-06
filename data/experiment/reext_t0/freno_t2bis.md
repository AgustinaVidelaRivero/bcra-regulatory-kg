# FRENO T2-bis de U-REEXT-T0 — corrección del runner y re-extracción de cap::4.2.1.2 (06/10/2026, USD 0,49291 de un tope de 3, sin commit)

**Precondiciones** (salidas):
- a. `git log --oneline -1 -- data/experiment/reext_t0` → `3d793aa U-REEXT-T0 T2 (mandato firmado en e2027dd; …`; el `git status --short` de `reext_t0` y `reextraccion_v2` sale vacío. b. `git diff --stat 9f6361e HEAD` sobre `e0_lib.py`, `correr_e0.py` y `e0_tablas.py` sale vacío. c. `pgrep -fl runner_corpus` no devuelve nada (rc 1).
- d. `estado_corpus.json`: `cap:e1` 5.660739 y `cap:e3` 4.724213; `presupuesto_compartido.json`: 49.659786. e. Sobre una copia, `particionar_por_corte` de `cap::4.2.1.2` (26.726 car.) da `::parte1` de 15.056 y `::parte2` de 11.669 (`precondicion_e.py`).

**Código**, primero sobre una copia y después en el repo (diffs en el paquete):
- a. `runner_corpus.py:67-68`: `e0_chunking` en el `sys.path`.
- b. `--reabrir-fase` (`:1313-1315`, `:1326-1327`, `:1362-1364` y `:1383-1385`) y `Estado.reabrir_fase` (`:383-396`): saca la fase cerrada y la deja como `fase_actual`, con su gasto como previo, y la registra en `reaperturas`. No hace nada si la fase no está cerrada o si hay otra en curso; sin el interruptor, nada cambia.
- c. `cliente_e1.SUFIJO_REINTENTO_FORMA_2` (`:77-80`, `:268-301`, `:453-467`) y el segundo disparo (`runner_corpus.py:529-539`, `:677-691`): una sola vez, cuando el primer reintento vuelve mal formado, y solo con el perfil r2b (lectura mía: la temperatura del reintento solo existe en r2b). El resumen de E1 suma `con_segundo_reintento`.
- **Corrección fuera de a–c** (decisión de la autora del 06/10/2026, con cinco condiciones; a confirmar): `cerrar_e2` (`:926-933`, `:958-962`). Antes, la unidad partida quedaba ausente del fan-in y la corrida terminaba con `FanInError`; ahora va con su último registro de E1 (`particionada_por_corte`) y el reporte la declara aparte, reemplazada por sus partes.
- Tabla, fila F20: el ancla pasa a ser `runner_corpus.py:67-68`, `:473-566`, `:710-719`; los dos últimos rangos son los anteriores renumerados.

**Sobre la copia**:
- Batería: los 15 selftests dan igual con el código de HEAD y con el nuevo (`selftest_manifiesto` 44/49, con los 5 fallos de P5). Selftest de claves: 0 claves se mueven; el JSON cambia solo en tres números de línea de constantes (87→89, 89→91, 92→94).
- Desde HEAD fallan dos selftests, por causas ajenas a T2-bis: `selftest_clave_cache` da FRENO en A1r (arma la clave del reintento por forma sin la temperatura 1 de r2b, `:465-466`, y encuentra 0 de 6), y `selftest_canal_abierto_e1` da 45/46.
- Pruebas sintéticas de las ramas nuevas: 10/10. E2 y E2 r2 de los diez TOs, regenerados con el código nuevo: 188/188 archivos iguales a T2.
- Corrida en seco (`seco_t2bis.py`: runner real, SDK falso, red bloqueada). Antes de corregir `cerrar_e2`: E1 y E3 corren y la corrida termina con `FanInError` (ausentes=1). Después: «corrida completa», y los nodos de las partes entran al E2 r2.

**Corrida real** (`lanzar_t2bis.py`, `--autorizado-tope 80.0`; de 07:51:51 a 08:00:23, −03): «corrida completa: gasto global=USD 50.1527». El tope de USD 3 se hizo cumplir por fuera del runner: el vigilante (`vigilante_t2bis.py`, en el paquete) leyó `presupuesto_compartido.json` y no actuó.
- **Gasto nuevo: 0,49291** = E1 0,427479 + E3 0,065431. `cap:e1` queda en 6,088218, `cap:e3` en 4,789644 y el presupuesto en 50,152696; la cuenta hecha con los tokens de las filas nuevas da lo mismo.
- **9 filas nuevas = 9 líneas de usage nuevas.** E1: 4 a temperatura 0, y 2 `-rforma1` y 2 `-rforma2` a temperatura 1. E3: 1, sin temperatura fijada. 4 aciertos de caché, todos donde se esperaban. El `-rforma2` de `cap::3.1.1.2` costó 0,038451, no 0,01: escribió el prefijo de 27.840 tokens en la caché de la API.
- **parte2**: corta en 8.192, en 16.384 sale mal formada y en `-rforma1` sale bien. En E3 queda `aceptado_con_residuales` y aporta 22 nodos al E2 r2 de cap (de 2.168 a 2.190), con procedencia `cap::4.2.1.2::parte2`, punto 4.2.1.2.
- **parte1**: corta en 8.192 y sale mal formada en 16.384, en `-rforma1` y en `-rforma2`: **queda sin validación**. `cap::3.1.1.2` también queda sin validación, declarada. En las cinco salidas mal formadas falta la clave `relations`: traen solo `entities`.
- **Criterios** (`criterios_t2bis.py`, sobre copias): C1 (los 460 registros y expedientes no cambian; los archivos solo crecen), C2 (los otros nueve TOs no cambian), C3, C4 y C6 OK. **C5 FALLA, solo por parte1**, que no tiene E1 válida ni está en la cola. `ModuleNotFoundError` no aparece en ninguna última versión de los registros.
- **Cuenta de las 2.439** (`t2_contadores.py`, con la hora de inicio de T2): 1.337 + 811 + 216 + 73 en cola + 1 sin validación + 1 particionada por corte, reemplazada por sus partes (parte2 `aceptado_con_residuales`, parte1 sin validación).
- El fan-in de `e2_lib`, que no toqué, la sigue contando entre los 11 rechazados del E2 del perfil de E1, con el motivo `error_api: particionada_por_corte`; `reporte_e2_cap.json` la declara aparte. La salida por carácter de las unidades de 3.000 car. o más pasa a incluir las partes: de 39 a 41 unidades, y el p90 de 1,5051 a 1,4820 (la decisión 4 se tomó con 1,5051).

**Para la autora**: 1. parte1 sin validación: C5 no se cumple, y no la volví a extraer. 2. Confirmar la corrección de `cerrar_e2` y cómo cuenta el fan-in. 3. Quedan 24 menciones con anclas desplazadas en otras filas de la tabla (lista en el paquete), y F08c no describe `-rforma2`: el despacho solo autorizaba F20. 4. Los dos selftests que fallan desde HEAD. 5. Cambiaron 3 archivos de `checkpoints/`: son salida de la corrida, pero el criterio no los nombra.

**SIGUSR1** (propuesta para antes de la tanda 1, sin implementar): el manejador solo prende una bandera, y Python reanuda la lectura en curso (PEP 475), así que la llamada termina y queda registrada. `fase_e1` y `fase_e3` miran la bandera antes de cada unidad y frenan con `Freno` (salida 3, estado persistido). El vigilante manda SIGUSR1 al llegar al umbral menos el costo máximo de una unidad, y SIGKILL tras una gracia. Prueba: un stub que se manda la señal a sí mismo a mitad de una unidad.

**Controles**: el sha256 del repo cambia solo en `runner_corpus.py`, `cliente_e1.py`, la tabla, `salida_r2b/cap/` (14 archivos y `particiones_por_corte.json` nuevo), el estado, el presupuesto, los 3 checkpoints, 2 bases y `logs/cache_usage.jsonl`. `.pyc`: 2.213. Grep de convenciones: vacío (en el paquete).

**Error propio**: al principio, el harness en seco importaba el runner sin la carpeta del modo script y pasaba la salida con ruta absoluta. Daba falsos negativos, y lo corregí antes de sacar conclusiones.

**Paquete:** `revision_UREEXT_T0_FRENO_T2bis/`, en el scratchpad. **Commit PENDIENTE de la autora. Espero el «seguí»; T3 no empezó.**
