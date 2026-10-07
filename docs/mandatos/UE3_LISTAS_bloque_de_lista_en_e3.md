# Mandato U-E3-LISTAS — el bloque que abre la lista entra al verificador de E3

**FIRMADO por la autora el 06/10/2026** (firma por mensaje de la autora; versión para firmar en `9bca986`; decisiones al firmar en la
nota al pie del 06/10/2026). Redactado por la mesa sobre el FRENO de U-DIAG-E3-LISTAS
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
DECISIONES DE LA AUTORA AL FIRMAR: tomadas el 06/10/2026; están en la nota al pie.

NOTAS POSTERIORES A LA FIRMA. El texto firmado son las 81 líneas de arriba (commit de la firma: PENDIENTE de la autora; versión para
firmar en `9bca986`) y no cambia.

- **06/10/2026 — decisiones de la autora al firmar.** (1) El nombre es U-E3-LISTAS. (2) La NOTA del ítem se redacta sobre el texto
  propuesto en la pieza 2, con tres precisiones que O1 resuelve: (a) cada cláusula corresponde a una regla del prefijo de E1 y la cita,
  sin agregar ningún criterio que E1 no tenga; las reglas son R28, R29, R30 y R16 (`e1_extractor/prompt_r2b_reemplazos.json:12`,
  `:108`, `:114` —composición con el encabezado de una lista—, `:120`) y P3C-b1, P3C-b2, P3C-b3, P3C-c1, P3C-c2, P3C-d1 y P3C-d2
  (`e1_extractor/prompt_r2b_parche_p3c.json:48`, `:55`, `:62`, `:69`, `:76`, `:83`, `:90`); las de las listas de condiciones son
  P3C-c1 y P3C-c2 (una Condicion por supuesto) y P3C-b3 (la excepción cuando los ítems son sus condiciones); (b) cubre los tres tipos de
  lista: la de lo que queda afuera de una clase (b1), la de una norma con sus excepciones (b2, «se prohíbe…, excepto para:»), donde el
  ítem es el supuesto en que la norma no rige, y la de condiciones o requisitos; (c) no solo exime: controla. Con el bloque a la vista,
  E3 verifica que lo compuesto en el ítem (sujeto, modalidad, cuantificador) coincida con lo que fija el encabezado; si no coincide,
  sigue siendo un error. (3) El texto final de la NOTA lo aprueba la autora en el FRENO O1, que muestra el texto y una prueba en seco
  (sin API: el mensaje de E3 armado con la pieza 1 y la NOTA) sobre ítems de los tres tipos, incluidos `cla::5.1.1.1` y uno de `ext::3.6.1`.
- **06/10/2026 — revisión del FRENO O1 y decisiones de la autora (O1 sin commit al escribir esta nota; enmienda 1 a este mandato,
  autorizada por la autora).** La revisión independiente reprodujo O1 con los comandos del paquete sobre copias de `d9d8888` sin
  enlaces: las 8 salidas del diagnóstico iguales byte a byte; la medición antes y después igual al FRENO (los 1.054 ítems cambian; los
  1.386 no ítems, las 2.440 unidades sin la marca r2 (y 2.427 de v3_b54 y 1.762 de r1) y los 13 casos del candado, byte a byte iguales;
  2.396.141 caracteres agregados); la prueba en seco con los mismos reclamos antes y después (4 de 5 sin base; 1 sigue); los archivos del
  repo que O1 lee, iguales antes y después; 2.213 `.pyc`.
  - **D1, citas con el bloque: SÍ, variante A** (enmienda 1 a este mandato). Se autoriza una línea en `ratchet_e3.py:283`:
    `cita_en_fuente(cita, chunk)` pasa a `cita_en_fuente(cita, chunk, _forma_r2(validacion))`, el mismo patrón de `ampliacion_activa(validacion)`
    en esa función (`:238`). Razón: sin el bloque en la fuente de las citas, toda cita de E3 al encabezado queda sin verificar y los
    veredictos inutilizables aumentan; con A, sobre los veredictos de hoy, 37 citas pasan a verificadas y 19 unidades pasan de cola por
    veredicto inutilizable a reintento. `ratchet_e3.py` sigue PROHIBIDO salvo esa línea; el riesgo declarado (una cita a la norma del
    encabezado se vuelve feedback del reintento, contra P3C-d2) lo mide O3.
  - **D2, párrafos partidos: SÍ.** El bloque que abre la lista son los bloques contiguos del mismo tipo y la misma unidad de origen (23
    ítems, 6 bloques, 8.819 caracteres más). Un tercer ítem en la fixture del candado, `pro::2.3.6.1`, además de los dos firmados; los
    valores del candado se recomputan en O2 con el texto final y la autora los confirma en el FRENO O2.
  - **D3, la norma del encabezado vuelta a emitir en el ítem: SÍ, sin cláusula en la NOTA.** E3 no la reclama; O3 cuenta por código, en
    las unidades afectadas, los ítems que repiten la norma de su encabezado (label o descripción con la norma del bloque), como medida.
  - **D4, largo y costo: SÍ**, 1.991 o 2.098 caracteres; unos USD 1,76 por corrida del tamaño de la tanda 0 (estimación con la razón
    marginal de E1, 3,06 caracteres por token).
  - **D5, qué compara A3r después del cambio.** A3r (`selftest_clave_cache.py:498-499`, anclaje `:1841`) deja de exigir las 2.440
    claves de E3 presentes: con el código vigente recomputa las 2.440 y exige que las 1.386 de no ítems estén en la base y que las 1.054
    ausentes sean exactamente las de los ítems (`prompt_r2b.es_item`), contadas y listadas; cualquier otra ausencia o presencia es
    DISCREPANCIA. La fila nueva de la tabla («E3 de las afectadas», F23b: el bloque que abre la lista y la NOTA del ítem en el mensaje de
    E3) declara ese anclaje; el bloque M de `selftest_e3` pasa de 13 a 18 casos (17 con los dos ítems, más `pro::2.3.6.1` con y sin la
    marca, según lo que recompute O2); las anclas de F04, F10, F10b, F23 y F01 a F03 se actualizan por el corrimiento de líneas.
  - **La población de O3 son 20 unidades distintas, no 24**: 17 con reintento por los reclamos P, C, B y B2 y 7 en la cola, 4 en los dos
    grupos (`ext::3.18.1.1`, `ext::3.5.6.1`, `ext::3.6.1.1`, `ext::3.6.4.2`); lista sellada `cc6b0cd6…`.
  - `reports/u_diag_e3_listas/` (:4-5 de este mandato) no está en el repo: el comando de archivo del 06/10/2026 frenaba por una ruta
    absoluta en `UDIAG_E3_LISTAS_grep_convenciones.txt` y no llegó a commitear. Se archiva con el comando corregido (rutas reemplazadas
    en las copias), en el commit de O1.
- **07/10/2026 — la NOTA del ítem aprobada con tres correcciones de la autora (versión 2; sin commit al escribir esta nota).**
  - (a) La tercera viñeta de la propuesta de O1 mezclaba los dos subcasos de P3C-b1 (`prompt_r2b_parche_p3c.json:48`) y sus dos ejemplos
    entre comillas asignaban una forma a una lista entera. En la versión 2 la viñeta se parte en dos, calcadas del prefijo: «lo que queda
    afuera» (cada ítem nombra un miembro excluido: Excepcion que dice qué queda afuera y de qué norma, con la contra-excepción como norma que
    vuelve a regir y una Condicion por condición) y «las condiciones de una sola excepción» (cada ítem describe un supuesto de la única
    salvedad: Condicion de esa excepción con su cuantificador; en la variante de línea de título, con supuestos alternativos la excepción
    compuesta con su supuesto). Y, porque la frontera entre b1 y b2 la decide E1 leyendo («Mirá qué trae cada ítem»), la NOTA dice que, si no
    queda claro si los ítems son miembros o supuestos, cualquiera de las dos formas vale y no es faltante. Los ejemplos entre comillas salen.
  - (b) La oración de la variante de línea de título («si se exigen juntos o no queda claro, el ítem es solo una Condicion y esa norma no se
    extrae en ningún ítem») es la regla literal de E1: R30, `prompt_r2b_reemplazos.json:114` («si se exigen juntos («y», «la totalidad»,
    «concurrentemente») o no queda claro, el ítem es solo una Condicion, y la norma del encabezado no se extrae en ningún ítem: repetirla con
    una sola condición la daría por suficiente»). Medido en la tanda 0 (copia de `d9d8888` con el prototipo de O1; `comun_e3.indice_bloque_lista`
    sobre los 1.053 ítems de la E0 r2b y los tipos de entidad de `extracciones_finales_r2_<to>.jsonl`): 39 ítems de 10 puntos abren su lista
    desde la línea de título; en 9 de los 10 puntos algún ítem lleva una norma (Obligacion, Restriccion, Potestad o Excepcion); en 1,
    `cap::10.2.1` (2 ítems, solo Definicion), ningún ítem lleva una norma y la del encabezado, si la hay, no está en el grafo. Es un conteo por
    tipo de entidad, no una lectura de si la norma compuesta coincide con el encabezado: cota superior de 1 punto en 10. Queda declarado como
    límite del grafo en la tesis, con esa cifra; la NOTA lo dice y no lo calla.
  - (c) Los dos tipeos señalados («partede», «propia:con») no están en los artefactos de O1 (grep sobre el texto propuesto, el parche del
    prototipo, los 1.054 mensajes generados y la prueba en seco: 0 coincidencias); en la versión 2 las dos palabras van con su espacio.
  - El texto aprobado, la tabla cláusula → regla actualizada (filas C5a, C6, C5b, C5b′ y C7) y el «seguí» de O2 (versión 2: los valores del
    candado de O1 se recomputan con esta NOTA, D2 y el tercer ítem) están en el paquete de la mesa; O2 pone el texto en `prompt_e3.py`.
