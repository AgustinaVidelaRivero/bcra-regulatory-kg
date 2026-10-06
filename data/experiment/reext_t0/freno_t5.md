# FRENO T5 de U-REEXT-T0, final: el reporte (06/10/2026; USD 0, sin API; sin commit)

**Precondiciones** (salida completa en `UREEXT_T0_T5_precondiciones_abc.txt`, en el paquete):
- a. `git log --oneline -1 -- data/experiment/reext_t0` → `889b2f9 U-REEXT-T0 T4, segundo tramo (…`. `git status --short -- data/experiment scripts docs/mandatos` → vacío.
- b. `shasum -a 256` de los dos kg.json → `a9631a64b422…` y `6e7560433148…`. `scripts/regression_kg_esperado.json` tiene `KG-Tanda0-Diez-r2b a9631a64…` y `KG-Tanda0-Desarrollo-r2b 6e756043…`. `grafos.py` tiene `"commit_sellado": "bbc38dc"` en las dos entradas.
- c. `shasum -a 256` → `tasas_t4.json` `f9a459a7d192…` y `adjudicacion_autora.json` `707863628565…`.

**Reporte**: `data/experiment/reext_t0/reporte_u_reext_t0.md`. Anexos: `t5/comandos_t5.sh <repo> <copia> <salida>` corre los comandos sobre una copia sin enlaces, y `t5/cifras_t5.py` recomputa cada cifra y escribe `t5/salida/anexo_cifras_t5.{json,md}`. Corrí `comandos_t5.sh` dos veces, a dos salidas distintas, y el anexo sale igual byte a byte.

**1. Costos, gate, tablero y controles de T3**: **Costos.** T2 49,6598 = E1 24,7195 + E3 24,9403 (verificación 21,9706 + reintentos 2,9697). T2-bis 0,49291, T2-ter 0,249002; el resto, USD 0. **Total: 50,401698 de 80**, igual a `presupuesto_compartido.json`. **Gate re-corrido sobre la copia.** Shapes con `--e0` PASA en los dos grafos, 18/18 bloqueantes, con la consola idéntica a la de T3-bis. Suite con la fixture `f72518b3…`: 68 ítems, 9 NO VERIFICADAS, 56 coinciden y 3 regresiones declaradas (RT-C5-3, RT-C6-1, RT-C6-2). **Tablero.** La columna r2b del repo es la derivación exacta de la medición y los controles de T3-bis (`cmp`): 22 celdas escritas y 4 «No medible en r2b». **Controles a–r.** Iguales byte a byte a `controles_t3bis.json`. **Reparación** (`cifra_reparacion.py`). 12 salidas mal formadas en 8 unidades: 6 resueltas con un reintento, 2 reparadas y 0 agotadas.

**2. Lo que P4b dejó sin mejorar** (de cada uno, lo corregible en código y el límite, en el reporte; decide la autora): Listas: b1 1/3 y 9/21; b2 5/7 y 0/32. Con la forma de b2 de `ext::3.13.1` y `ext::3.6.1`: b1 1/1 y b2 7/9. Condicion por supuesto: 1/30 por unidad. Por supuesto, 43/77/7/2/8 de 137, con la adjudicación de `c9d4c40`; 77/137 en [0,478; 0,642]. En 26 de 30 unidades hay al menos un supuesto dentro de una norma. Omisiones, sin marca: 19/30 normativas (14/30 sin remisiones). Con el tramo propio, 390,9 [264,9; 511,4] y 268,8 [160,3; 399,4] de 733: lo que se le escapa al contador. Omisiones, con marca: 27/30, y con el tramo propio 134,7 de 404. El heredado va aparte: 97,7 y 242,4.

**3. Variación del modelo**: E1: P5 dio 6/27 iguales; en T4 5.b, 4 idénticas, 23 distintas, y la marca cambia en 3 y en 5. E3, P5: el mismo veredicto en 10/10, la misma evaluación en 9/10 e iguales byte a byte en 6/10. E3, esta corrida: 2.685 pedidos, todos distintos (0 repetidos, 0 aciertos, sin temperatura). Ninguna unidad tuvo dos veredictos para el mismo pedido, así que la variación no se puede medir sobre `veredictos.jsonl`.

**4. Lo que sigue**, sin hacerlo: Los cinco del mandato. U-SINCOLA-T0. P20, con sus ocho puntos. El experimento de comparación de modelos, con los dos hallazgos de T4 como línea de base.

**5. Claves**: `selftest_clave_cache.py --salida-r2b`, sobre la copia y dos veces igual: **A1r OK** (2.449 claves; 8 en `-rforma1`, 2 en `-rforma2`) y **A3r OK** (2.440 pares); VEREDICTO OK. La constante de la E0 no cambia. Tabla: `git diff` toca solo las filas F05, F10 y F14, que pasan a citar la enmienda 3 (`0cb0c70`, §1, puntos 1 a 3), y el §5. §5: la tarifa observada, E1 0,010135, E3 0,010226 y 0,020361 por unidad, con su comando.

**6. Cola**: 12/30 con error [0,246; 0,577]; la regla se dispara. La salida elegida es la forma (a), en U-SINCOLA-T0. Salen 313 de 8.816 nodos y 1.503 de 27.632 aristas: 411 con la marca de la cola y 1.092 derivadas (`remite_a` 1.004, `establecida_en` 86, `padre_sugerido` 2). Quedan 21 nodos compartidos. La parte 1 sale entera, con sus 53 entidades. La simulación sobre la copia queda en 8.503 nodos y 26.129 aristas. Las 15 preguntas no cambian, ninguna cae bajo el ancla de una unidad de la cola, y el ejemplo de la tesis no está en la cola. En la suite cambia solo LN-5.

**Contradicciones** (mandan los archivos; no las corrijo): La fila de la suite en el tablero (:55) dice que el `kg_sha256` está en null en el repo. El §4 y las notas de la tabla dicen «A1r y A3r: NO_VERIFICABLE» y «enmienda en curso». `insumos_escritura.md`, §7, ítem 2, dice 25 de 30 (son 26) y lleva cifras provisorias. P20 (3) dice que `selftest_clave_cache` falla.

**Errores propios**, corregidos y con su causa en el reporte: Las shapes sin `--e0` la primera vez. Un enlace `.venv` momentáneo en la copia, contra la regla l; nada se escribió por él. El bloque 5 del anexo leía el selftest viejo de la copia. Dos recuentos del borrador: 5 «No medible» y 10 `TextoOrdenado`.

**Controles**: sha256 del repo antes y después: solo cambian `tabla_reprocesamiento.md` y `selftest_clave_cache.json`, y se agregan `t5/` (4 archivos), el reporte y este freno; cambia además `data/experiment/neo4j/volumen/logs/debug.log`, que git ignora: es el contenedor de Neo4j, que está corriendo (checkpoints programados), y ningún comando de T5 usa Neo4j. Hay 2.213 `.pyc`. El grep de convenciones da vacío (en el paquete). **Paquete:** `revision_UREEXT_T0_FRENO_T5/`.

**Commit PENDIENTE de la autora; la unidad cierra con su commit. Espero la revisión.**
