# Mandato U-E3-LISTAS — el bloque que abre la lista entra al verificador de E3

**VERSIÓN PARA FIRMAR (06/10/2026) — PENDIENTE DE FIRMA DE LA AUTORA.** Redactado por la mesa sobre el FRENO de U-DIAG-E3-LISTAS
(reporte y propuesta archivados en `reports/u_diag_e3_listas/`) y las decisiones de la autora del 06/10/2026: la corrección rige desde
la tanda 1; la tanda 0 no se re-verifica, declara el límite (`docs/insumos_escritura.md` §7, ítem 4) y lo mide aparte con O3, que es
parte de esta unidad. Gasto de API: solo O3, con tope USD 1.

QUÉ CORRIGE. En la tanda 0, 1.054 de las 2.440 unidades verificadas son ítems de una lista; el fuente que recibe E3 lleva solo los
bloques heredados de tipo `encabezado` (`data/experiment/reextraccion_v2/e3_verificador/comun_e3.py:123-125`), así que en 1.015 ítems el
bloque que abre la lista (intro 982, intersticial 22, chapeau de sección 11) no llega ni al texto ni a la verificación de citas
(`:226-227`); la regla de composición (`NOTA_E3_ENCABEZADO_LISTA`, `prompt_e3.py:256-264`) va solo al mini-chunk del encabezado
(`:315-316`), nunca al ítem; y `prompt_e3.py:57` dice que E3 recibe «párrafos introductorios, intersticiales y de cierre». Efecto medido:
31 reclamos que piden en el ítem la norma del encabezado que el prefijo de E1 manda no emitir ahí (P3C-d1 y P3C-d2; 16 bloqueantes),
5 de polaridad sin fundamento, 9 de 15 falsas alarmas de contenido agregado en una muestra con semilla, 17 reintentos y 7 unidades de la
cola humana por esos reclamos (`reports/u_diag_e3_listas/reporte_u_diag_e3_listas.md`).

LAS CINCO PIEZAS (las dos primeras, solo con la forma r2: sin la marca `forma_salida = "r2"` de la validación el mensaje queda byte a byte
igual, como `notas_r2`, `prompt_e3.py:334-335`).
1. **El bloque que abre la lista entra al fuente del ítem y a sus citas.** En `comun_e3.py`, el texto fuente y `fuente_para_citas` de una
   unidad que es ítem (`prompt_r2b.bloque_lista(chunk)` distinto de `None`, no mini-chunk) suman ese bloque, y solo ese (no los cierres
   que lo siguen), con su rótulo (`[intro | punto X]`), con la misma regla que arma `LINEA_ITEM` en E1 (`prompt_r2b.py:306-320`): E1 y E3
   ven el mismo encabezado. Lo que E3 ya recibe no cambia.
2. **Una NOTA del ítem**, `NOTA_E3_ITEM_LISTA`, en espejo de `NOTA_E3_ENCABEZADO_LISTA`, agregada en `notas_r2` cuando la unidad es ítem:
   esta unidad es un ítem de la lista que abre el bloque [tipo | punto X]; en el ítem se componen el sujeto, la modalidad, el
   cuantificador y lo que el encabezado fija para cada ítem, y eso no es contenido agregado; la norma que el encabezado enuncia no se
   emite como entidad aparte en el ítem, y que falte no es faltante; si el encabezado anuncia lo que queda afuera de una clase, el ítem
   es una Excepcion, y una contra-excepción del ítem va como la norma que vuelve a regir, con sus Condicion. Texto final en O1 (decisión 2).
3. **La fixture del candado del mensaje de E3** (`candado_mensaje_e3.json`; hoy 6 unidades, ninguna ítem): se agregan dos ítems de
   `salida_tanda0_r2b/` con la forma r2, uno cuyo bloque es `intro` y otro cuyo bloque es `encabezado`, y se re-sellan
   `CANDADO_MENSAJE_E3_JSON_SHA256_ESPERADO` y `MENSAJE_E3_SHA256_ESPERADO` (`prompt_e3.py:405-406`). El re-sellado es un acto de la autora:
   la unidad propone los dos valores y el mensaje nuevo de los 8 casos en el FRENO O1; la autora los confirma en el «seguí» de O2.
4. **La tabla de reprocesamiento.** Fila nueva (la siguiente a F24): «Bloques heredados que entran al fuente y a las citas de E3 (regla
   de composición del fuente)»: clave de E1 no cambia; clave de E3 cambia en los ítems; clase «E3 de las afectadas» (los ítems), con E1
   de la caché y los reintentos donde cambie el feedback; con su variación en `selftest_clave_cache.py` (como R30 para F23). Nota a F23
   (la NOTA nueva) y a F24 (cambia qué reclamos tienen cita verificada y, con eso, qué unidades reintentan o van a la cola). La nota de
   `:61` («E3 no recibe los bloques de prosa heredados») pasa a decir qué recibe desde esta unidad.
5. **La contradicción de `prompt_e3.py:57`.** La frase está en `INSTRUCCIONES`, el prefijo de E3 (hash `21a836c7de6d`): no se edita,
   porque sería F10 (E3 de todas las unidades, namespace nuevo) y choca con E3 congelado (`ratchet_e3.py:32`). Con la pieza 1 el código
   cumple la frase para los bloques que abren una lista; para los cierres sigue sin cumplirla, y eso se declara en la nota de `:61` y en el
   reporte de la unidad.

ETAPAS.
O1. Diseño y medición en seco (USD 0, sobre una copia sin enlaces): el texto de la NOTA; los dos ítems de la fixture; el mensaje de E3
    antes y después para las 1.054 unidades de la tanda 0 (cuántas cambian, qué bloque entra, longitud agregada en caracteres y tokens
    estimados); la lista sellada de las 24 unidades afectadas de la tanda 0 (17 con reintento por esos reclamos y 7 en la cola, de
    `reports/u_diag_e3_listas/anexo/`); los valores nuevos del candado. FRENO O1.
O2. Implementación con selftest (`selftest_e3.py`: un ítem con intro, un ítem con encabezado, un mini-chunk, una unidad r1 sin cambio);
    re-sellado del candado con los valores confirmados por la autora; la fila nueva y las notas de la tabla; la variación en
    `selftest_clave_cache.py` y su JSON regenerado sobre copia; `selftest_clave_cache` y `selftest_e3` en verde; el mensaje de E3 de toda
    unidad que no es ítem, byte a byte igual al de hoy (control sobre las 1.386 de la tanda 0). FRENO O2.
O3. La medición aparte de la decisión de la autora sobre la tanda 0 (tope USD 1; ninguna llamada antes de O2): (a) E3 corregido, primera
    verificación sin ratchet, sobre las 24 unidades afectadas, con la extracción que vio E3 en la tanda 0, en una base propia
    (`data/experiment/e3_listas/cache/`): cuántos de los reclamos P, C, B y B2 desaparecen, cuántos persisten y cuántos nuevos aparecen,
    por unidad; (b) sin API: en las 17 unidades que reintentaron por esos reclamos, el intento 0 (`extracciones_e1.jsonl`) contra la
    extracción final (`extracciones_finales_r2_<to>.jsonl`): cuántas cambiaron, qué cambió (elementos que entran, salen o cambian),
    con ficha por unidad. Nada entra al grafo ni a las bases del pipeline (principio 9). Las cifras van a `docs/insumos_escritura.md` §7,
    ítem 4, como «PENDIENTE: las cifras de O3» resuelto. FRENO O3, final.

CRITERIOS DE ACEPTACIÓN. Cada uno con su comando y su salida: mensaje de E3 igual byte a byte fuera de los ítems y sin la forma r2; los
1.054 ítems con el bloque y la NOTA; candado re-sellado con los 8 casos y confirmado por la autora; selftests en verde; fila y notas de la
tabla con el contraste del selftest de claves en verde; `kg.json` de los grafos sellados sin cambios (la unidad no ensambla); O3 con sus
dos cifras y sus fichas, gasto ≤ USD 1; 2.213 `.pyc`; grep de convenciones.
ESCRITURAS: `data/experiment/reextraccion_v2/e3_verificador/{comun_e3.py, prompt_e3.py, candado_mensaje_e3.json, selftest_e3.py}`,
`data/experiment/mantenimiento/{tabla_reprocesamiento.md, code/selftest_clave_cache.py, selftest_clave_cache.json}`,
`docs/insumos_escritura.md` (solo las cifras de O3 en el ítem 4 de §7), `data/experiment/e3_listas/` (se crea) y el scratchpad.
PROHIBIDO: `INSTRUCCIONES`, los calibradores, el tool schema y el `PREFIJO_HASH` de E3; el prefijo y el mensaje de E1; `ratchet_e3.py`;
los grafos y las bases del pipeline (O3 usa una base propia); EV2; commitear; cualquier llamada a la API fuera de O3.
REQUISITOS: CLAUDE.md §4 (a a l), con `docs/decisiones_caching_extraccion.md` vinculante para O3.

CONVIVENCIA. Toca solo `e3_verificador/`, `mantenimiento/` e `insumos_escritura.md`. **Corre en paralelo** con S0-2 de U-SEG-OFICIAL (E0:
`e0_chunking/`, `segmentacion_oficial_e0r2/`), con SC1-bis y SC2 de U-SINCOLA-T0 (ensamblador, `corpus_tanda0/ens_*_sincola/`, fixture de la
suite, `grafos.py`; no importan `prompt_e3`), con C0 y C1 de U-COMP-E1 (`comp_e1/`; sin E3) y con R2-1 de U-RERESOL-CAT cuando arranque
(ensamblador, `r1_e4.py`, `regression_kg.py`). **Choca** con: (a) U-RUNNER-P20, que también edita `selftest_clave_cache.py` (punto 5) y la
tabla: uno después del otro, no a la vez; (b) U-OMISIONES-COD solo en la tabla (nota a F15 contra fila nueva y notas a F23/F24): filas
distintas, pero se commitea una antes que la otra; (c) cualquier unidad que importe `prompt_e3` entre el cambio y el re-sellado del
candado, porque el candado corre al importar y frena: por eso O2 trabaja sobre la copia y el repo recibe código y candado juntos;
quien importa `prompt_e3` hoy son los selftests de `r2_codigo/`, `selftest_clave_cache`, `selftest_dirigida_tanda0` y los scripts
cerrados de `prompt_r2/` y `reext_t0/` (ninguno corre en las unidades en paralelo, salvo `selftest_r3.py`, que SC1-bis corre sobre su
propia copia). `git status --short` completo al inicio, lo ajeno listado y sin tocar; 2.213 `.pyc` al inicio, declarados si difieren.
DECISIONES DE LA AUTORA AL FIRMAR: (1) el nombre de la unidad; (2) si la NOTA del ítem va con el texto propuesto o con uno suyo (se fija
en O1, con el texto final en el FRENO O1).
