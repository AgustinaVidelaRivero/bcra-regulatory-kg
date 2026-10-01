FIRMADO por la autora — 2026-10-01

MANDATO — U-R2-CODIGO: CORRECCIONES EN CÓDIGO DE LA RELEASE r2.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad en CINCO ETAPAS, R1 a R5, en este orden, con FRENO obligatorio al final de cada una:
  reporte corto (no más de 40 líneas) y espera de la revisión y del «seguí» escrito de la
  autora. Ninguna etapa arranca sin él.
- Costo de API: USD 0 en todas las etapas. Ninguna llamada a la API; Neo4j no se usa.
- La medición r2a (plan, B2.11, unidad 9) es una unidad aparte, posterior. Esta unidad
  construye y prueba el código; no produce el grafo r2a ni llena el tablero.

CONTEXTO. Plan, fila B2.11, unidad 8 (docs/plan_tesis.md:397), habilitada: U-PYD cerrada
(`57a8dd2`) y unidad 2 hecha.
- La fila lista los candidatos, todos asignados a esta unidad por decisión de la autora:
  - las tablas como primera prioridad (`BKL-0006`, RX-10 y la detección en E0);
  - `BKL-0037` y la persistencia del crudo del reintento de E3;
  - la conexión del perfil r2;
  - la fusión (T2, con H2 y `BKL-0031`), `BKL-0030`, la `cuarentena` booleana y las mutuales;
  - la suite y las shapes del perfil r2.
- Por decisión de la autora del 01/10/2026 entran además cuatro candidatos del §4 del laudo de
  r2, que corrige el ensamblado: H1 y H4 (remisiones desde Condicion, Potestad y Definicion), las
  remisiones resueltas sobre el texto de E0 y no sobre la paráfrasis, la procedencia de las
  remisiones y la `establecida_en` derivada de la procedencia.
- Las decisiones de esquema que aplica esta unidad están en L-ESQ-R2 (FIRMADA en `4ef7650`).
  Por la regla k de CLAUDE.md §4, se lee con `git show 4ef7650:<ruta>`, nunca del archivo
  actual. Lo que aplica: §1.3 y §1.4 (umbrales, par B en r2a), §3 (resolución de sujetos), §4
  (registro de no mapeados), §6.4 (relaciones de la matriz ampliada) y §12; con sus dos notas
  posteriores a la firma.
- Insumos ya hechos:
  - el validador, la política y las reglas de comparación del perfil r2 (U-PYD,
    data/experiment/pyd_r2/, `57a8dd2`);
  - el catálogo r2 (U-CAT-UNICO, data/experiment/catalogo_unico/, `bd2122d`; derivador
    corregido en `5084781`).

Leé completos, antes de escribir una línea:
- la fila de la unidad 8 del plan (:397) y la fila de la unidad 7 (:396), con la calibración y
  el límite declarado de los rangos con unidad repetida;
- docs/laudo_release_r2_pipeline.md:
  - §1.1 (`BKL-0030`), §1.2 (`BKL-0031`), §1.3 (`BKL-0006` y RX-10), §1.4 (`cuarentena`) y §1.5
    (mutuales), cada uno con su cambio, sus módulos y su prueba de aceptación;
  - §3.2 (la clave de caché);
  - §4: H2, «los tres tipos nuevos se funden por label», y T2, «la fusión por descripción junta
    reglas distintas con igual redacción», :339;
  - §4: H1 y H4 (:329, con la simulación de +3.687 aristas), remisiones falsas por paráfrasis
    (:330), nodos sin ninguna arista (:332), procedencia de las remisiones (:333 y :335) y el test
    del ejemplo `cla::5.1.1.1` (:334);
- reports/u_audit_tipos_v3/inventario_U-AUDIT-TIPOS-V3.md (H1, H4 y punto 3) y
  p2_referencias_sim.json; reports/u_cons_arco_ejemplo/informe_U-CONS-ARCO-EJEMPLO.md, parte A;
- L-ESQ-R2 en su versión firmada (`git show 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`),
  las secciones citadas arriba, y las notas posteriores a la firma del archivo actual;
- reports/u_umbral/u1_mediciones.json (`medicion_2`: los 4 chunks de ponderadores sin detectar y
  los 12 con tabla del parser sin marca de E0) y reporte_u_umbral.md;
- reports/u_pre_r2/d1_suite.md (propuestas para T4, T5 y E4-a8) y d2_ausencias.md (las pérdidas
  por tablas de `ric::7.2` y `ric::9.2`);
- reports/u_listas_nomap/diseno_listas_nomap.md, secciones c (P-c1 a P-c3), d (P-d1 a P-d4) y g
  (LN-1 a LN-8 y S24 a S29);
- data/experiment/pyd_r2/ (validador_r2.py `validar` :437, reglas_comparacion.py `analizar` y
  `elemento_umbral`, politica_campos_r2.json) y data/experiment/catalogo_unico/generados_r2/;
- el pipeline que se toca:
  - data/experiment/reextraccion_v2/e0_chunking/ (e0_lib.py, correr_e0.py y, sin editarlo,
    e0_tablas.py);
  - corpus_v2/runner_corpus.py (:280-288, :572-583, :593, :671);
  - e1_extractor/cliente_e1.py (:60, :154);
  - e2_reduce/e2_lib.py (`entity_slug_v3` :122, Sujeto_propuesto :382-407, cuarentena :388);
  - corpus_v2/r1_e4.py, corpus_v2/r1_e5_esqueleto.py, corpus_v2/ensamblar_corpus.py y
    data/experiment/tanda0/code/ensamblar_tanda0.py;
  - corpus_v2/r1_referencias.py (`TIPOS_ORIGEN` :51, filtro de origen :243);
- la suite (scripts/regression_kg.py, scripts/regression_kg_esperado.json,
  scripts/selftest_regression_kg.py) y las shapes (scripts/shapes_validator.py,
  scripts/selftest_shapes_congelado.py);
- el tablero de correcciones, filas «Afirmación falsa por tabla no detectada», «Pérdidas de
  contenido por tablas», «Colisiones de ids de chunk en E0», «Crudo del reintento de E3 sin
  persistir», «Relaciones de la matriz ampliada sin verificar por E3», «Aristas `referencia` por
  tipo de origen», «Condiciones aisladas», «Remisiones falsas por paráfrasis» y «Test del ejemplo
  `cla::5.1.1.1`».

DECISIONES YA TOMADAS. No se re-deciden.
1. El orden de las etapas es R1 → R5 y no se adelanta ninguna. Las cinco cuestan USD 0.
2. Los perfiles existentes (`produccion_dev` y `v3_b54`) y los prompts sellados no se editan. Todo
   cambio de comportamiento entra en el perfil r2 o detrás de una versión nueva, de modo que el
   pipeline viejo siga reproduciendo lo sellado.
3. Un cambio en el texto de un chunk de E0 obliga a pagar E1 y E3 de ese chunk (laudo de r2,
   §3.2). Esta unidad no re-extrae: cuenta los chunks afectados y estima su costo para
   U-REEXT-T0.
4. El formato en que E0 serializa las tablas es decisión de diseño de la unidad, con FRENO antes de
   implementarlo (laudo de r2, §1.3).
5. `BKL-0031`: en esta unidad solo el paso 1, el detector de solo lectura. La adjudicación por
   muestra es de la autora, y la regla de fusión depende de esa tasa (laudo de r2, §1.2).
6. Mutuales: la opción (c) del laudo de r2, §1.5. La cláusula pasa a ser un test que documenta la
   persistencia; el remedio de raíz, la regla de calificadores en E1, es de U-PROMPT-R2 (checklist
   X8).
7. `cuarentena`: el cambio recomendado del laudo de r2, §1.4. T7 la lee con el mismo criterio que
   `en_cuarentena`; E2 no cambia.
8. Las shapes del perfil r2 las escribe esta unidad (decisión 8 del mandato de U-PYD).
   `shapes_validator.py` sigue solo con stdlib, y el perfil congelado no cambia.
9. La entrada r2 de la fixture de la suite la propone esta unidad. La sella la autora antes de
   correr U-REEXT-T0 (plan, B2.11, unidad 11).
10. El catálogo r2 se lee con candado de sha256 (`c3ad1581…`), y la política del perfil r2 con el
    sha de `57a8dd2`.
11. Remisiones y procedencia, por decisión de la autora del 01/10/2026 (candidatos del §4 del laudo
    de r2):
    - el resolvedor de remisiones parte también de Condicion, Potestad y Definicion, y lee
      `termino` (H1 y H4);
    - las remisiones se detectan sobre el texto de E0 del punto de origen, por `chunk_id`, y no
      sobre la paráfrasis;
    - se resuelven desde cada procedencia del origen. La parte de la vista del agente es de A1.8;
    - el ensamblado deriva `establecida_en` de la procedencia para todo nodo de contenido que no
      la tenga.

CONTROL QUE RIGE EN TODA ETAPA QUE TOCA CÓDIGO DEL PIPELINE:
- con los perfiles existentes, el pipeline reproduce byte a byte lo sellado: la E0 de la tanda 0,
  y los ensamblados KG-Tanda0-Desarrollo-r1 (`eab2fdd0…`), KG-Tanda0-Diez-r1 (`dd42d6d9…`) y el
  de los cinco (`4097d4fd…`);
- si algún sellado no se puede reproducir con los artefactos guardados, FRENO con el motivo;
- la reproducción corre sobre una copia en el scratchpad, nunca escribiendo en el repo (regla k).

R1 — Tablas. USD 0.
a. Detección en E0:
   - conectar `e0_tablas` a las marcas de E0, para los 12 chunks en que el parser detecta tabla y E0
     no la marca: `ric::S2`, `4.2`, `8.2`, `9.2.1` y `10.2`; `cap::4.2.1.1`, `6.2.1.1`, `12.1` y
     `12.2`; `ext::12.1`; `ctacte::13.2`; `polcre::1.5`;
   - una detección propia para los 4 chunks de ponderadores que no detecta ninguno de los dos:
     `cap::2.12.2.5`, `2.12.2.6`, `2.12.2.8` y `2.12.3.2`. La regla se declara antes de aplicarla, y
     se cuentan sus falsos positivos en los diez TOs.
b. Propuesta del formato de serialización de las tablas en el texto del chunk (decisión 4). Se
   presenta con dos o tres chunks de ejemplo, entre ellos `cap::1.2`. **FRENO intermedio:** la
   autora aprueba el formato antes de implementarlo.
c. Serialización implementada detrás de una versión nueva de E0. Controles:
   - verificación por multiconjunto (regla R-VERIF de B5.8.3), sin pérdida en ninguna tabla;
   - los chunks sin tabla quedan byte a byte idénticos;
   - la E0 vieja se sigue reproduciendo.
d. Censo, USD 0: cuántos chunks de los diez TOs cambian de texto, por TO, y el costo estimado de
   su E1 y E3 con la tarifa de referencia del laudo de r2, §1.3 (USD 0,0166 por unidad). Es el
   insumo del tope de U-REEXT-T0.
e. Verificación en código de los umbrales contra `e0_tablas` (L-ESQ-R2 §1.4), como marca y sin
   corregir.
   - **Caso de control:** `cap::1.2`. El parser da Bancos 5.000 y Restantes entidades 2.500, y las
     dos Restricciones del grafo tienen los montos invertidos: las dos quedan marcadas.
   - La corrección del monto exige re-extraer. En r2a, el test C2 y el de `BKL-0006` siguen en
     «persiste», y se declara.
   - Casos adicionales: `ric::7.2` (tabla marcada por E0 sin extracción) y `ric::9.2` (cuadro de
     códigos que E0 no marca), las pérdidas reales de D2.
FRENO R1:
- la detección, con sus falsos positivos;
- el formato aprobado;
- la verificación por multiconjunto;
- el censo con su costo;
- las marcas de `cap::1.2`;
- el sha256 de lo escrito.

R2 — Identificadores y persistencia. USD 0.
a. `BKL-0037`:
   - ids de chunk únicos por TO en E0, con la regla de desambiguación declarada antes. Hoy hay 69
     ids repetidos en adfsp, ceninf, cirmo3 y ri_niif (reports/u_insumos_cap/estadisticas_corpus.md
     §6);
   - el runner se detiene con un error explícito ante un id repetido, en lugar de pisar registros
     (runner_corpus.py:280-288 y :572-583);
   - selftest con un par de chunks de igual id;
   - la E0 de la tanda 0 no tiene ids repetidos y no cambia.
b. Persistencia del crudo del reintento de E3 (tablero, fila del crudo del reintento; checklist
   R30). El crudo de cada reintento queda guardado junto a `finales.jsonl` (o en un archivo
   compañero, a declarar), con la ancla del módulo que lo escribe.
   - Para la tanda 0, el lector toma el crudo de `e1_reintentos.db` (solo con `immutable=1`).
   - Se explica la diferencia de r1: 431 entradas contra 406 reintentos
     (reports/u_listas_nomap/n1_inventario.json, `reintentos_db.r1`).
FRENO R2:
- la regla de desambiguación;
- el selftest del runner;
- el formato de persistencia;
- la reproducción de lo sellado;
- el sha256 de lo escrito.

R3 — Conexión del perfil r2 al runner, a E2 y al ensamblado. USD 0.
a. **Perfil r2 conectado:** el runner y el ensamblado usan, con el perfil r2, el validador, la
   política y el catálogo r2. Con los perfiles existentes, nada cambia.
b. **Resolución de sujetos por relación,** entre E3 y E2 (L-ESQ-R2 §3.3; diseño, P-c1 a P-c3):
   - la regla textual gana solo con coincidencia exacta de label o alias (R1);
   - con R2 y R3 gana la sugerencia del modelo;
   - siempre se registran los dos ids;
   - R3 usa la lista inicial cerrada de expresiones colectivas, tomada de `prompt_e1.py:110`;
   - las menciones que califican una clase existente se resuelven a la clase y guardan el
     calificador;
   - el método queda en la arista, y el detalle en `resolucion_sujetos.jsonl`.

   Qué hacer con el E4 posterior a la fusión (pasada residual o retiro) se propone con su
   evidencia.
c. **Registro de no mapeados** (L-ESQ-R2 §4; diseño, P-d1 a P-d3):
   - `no_mapeados_sujetos.jsonl` por TO y por ensamblado;
   - E2 crea los `Sujeto_propuesto` desde el registro;
   - re-resolución por programa cuando cambia el sha del catálogo, idempotente.
d. **Remisiones y procedencia** (decisión 11), en `r1_referencias.py` y en la redirección de
   `ensamblar_tanda0.py`:
   - `TIPOS_ORIGEN` (`r1_referencias.py:51`) suma Condicion, Potestad y Definicion, y el resolvedor
     lee `termino` (H1 y H4);
   - las remisiones se detectan sobre el texto de E0 del punto de origen, no sobre la paráfrasis;
   - se resuelven desde cada procedencia del origen; los seis puntos de la fila del laudo (:335)
     pasan a origen o quedan declarados;
   - **casos de control:**
     - re-ensamblar el desarrollo reproduce la simulación de U-AUDIT-TIPOS-V3: +3.687 aristas y 0
       perdidas;
     - `cla::5.1.1.1` llega a `cla::3.7`;
     - `cap::8.2.3.3` llega a `cla::6.5.1` y `cla::7.2.1`, sin la remisión interna falsa;
     - en diez, cuántas remisiones cambian de destino.
e. **`establecida_en` derivada** (decisión 11): cero nodos de contenido sin `establecida_en`, y el
   resto de los aislados declarado por causa. En desarrollo hay 35 Condicion aisladas: 33 por
   rechazos de la matriz congelada y 2 sin relaciones emitidas; con H1, 9 de las 35 reciben una
   remisión (laudo de r2, §4, :332).
f. **Llenado en código de las listas de umbrales,** el par B (L-ESQ-R2 §1.3 y §1.4):
   - desde la descripción guardada y los `campos_heredados_v3`, con las reglas de U-PYD;
   - verificación contra el texto de E0 y contra `e0_tablas`, con las tablas de R1;
   - lo que no verifica se marca, sin corregirlo;
   - la base de un umbral relacional se resuelve a su punto o definición por el mecanismo de
     remisiones de (d); si no resuelve, se marca (L-ESQ-R2 §1.3, orientación c);
   - el campo de frecuencia;
   - el conteo de rangos con la unidad repetida («entre 30 días y 90 días»), por el límite
     declarado en la fila 7 del plan.
g. **Relaciones de la matriz ampliada:** entran con la marca de no verificadas por E3, que E2
   conserva, y se cuentan aparte (L-ESQ-R2 §6.4).
h. **Cómo muestra el agente la lista de umbrales** (L-ESQ-R2 §1.4, NO VERIFICADO): se lee, sin
   editarlo, `ver_nodo` del harness (que está sellado), de `neo4j_index.py` y de `tools_v2.py`, y
   se prueba en memoria con un nodo r2. Si alguna no la muestra, se reporta; no se arregla acá.
i. **Corrida de prueba sobre un TO,** `cla` (el del ejemplo del préstamo), en el scratchpad. La
   corrida completa es la unidad 9.
   - **Casos de control:**
     - `cla::5.1.1.1` → las dos `condicion_de` Condicion → Operacion, marcadas como no verificadas
       por E3. El crudo guardado de E1 las trae y la matriz congelada las rechazaba (verificado por
       la mesa el 01/10/2026 en `corpus_tanda0/salida_dirigida/cla/extracciones_e1_compact.jsonl`);
     - `cla::5.1.1.1` → la remisión a `cla::3.7`;
     - `cla::5.1.1.1` → el elemento de umbral mínimo estricto, valor 2, unidad «veces», con la base
       resuelta a `cla::3.7`;
     - una relación de sujeto con su método de resolución y, si la hay, su fila en el registro.
FRENO R3:
- la conexión, con la reproducción de lo sellado;
- la regla sobre el E4 residual;
- el registro;
- las remisiones y la `establecida_en` derivada, con sus casos de control;
- el resultado de la corrida de prueba con los casos de control;
- la lectura de cómo se muestra la lista;
- el sha256 de lo escrito.

R4 — Demás candidatos. USD 0.
a. **Fusión, T2 con H2 y `BKL-0031`.** En el perfil r2:
   - la fusión no junta nodos de puntos distintos por igualdad de descripción (T2: las
     Restricciones del 125 % de `ext::7.5.3` y `ext::7.8.5.1`);
   - Condicion, Definicion y Potestad no se funden solo por label (H2; `entity_slug_v3`,
     `e2_lib.py:122`).

   T2 tiene que pasar a «resuelto» sobre la prueba de r2, y el ensamblado viejo se sigue
   reproduciendo. Además, el paso 1 de `BKL-0031`: el detector de casi-duplicados, de solo lectura
   (laudo de r2, §1.2), con su reporte sobre r1 y sobre los ensamblados de la tanda 0.
b. **`BKL-0030`** (laudo de r2, §1.1):
   - que el reintento llegue a la API: la constante a 16.384 o un timeout explícito
     (`cliente_e1.py:60` y `:154`);
   - que la unidad se parta cuando no alcanza.

   **El cambio entra solo con el perfil r2.** `max_tokens` forma parte del request y, por lo
   tanto, de la clave de caché (`data/experiment/evaluacion/llm_cache.py:111-126`,
   `canonical_request` y `compute_key`). Cambiarlo en los perfiles existentes cambiaría las claves y
   obligaría a pagar de nuevo lo ya extraído.

   Se prueba sin API:
   - se arma el request y se comprueba localmente contra la guarda del SDK, con los casos del laudo
     `cap::3.1.14.1`, `cap::4.2.1.2` y `cap::4.3.3.1`;
   - sobre el camino sin corte, los selftests del manifiesto quedan byte a byte idénticos;
   - **control nuevo:** con los perfiles `produccion_dev` y `v3_b54`, la clave de caché de una
     muestra fija de requests de E1 y de E3 es idéntica a la de hoy. La muestra se declara antes,
     con su semilla, e incluye primeros intentos y reintentos.
c. **`cuarentena`** (decisión 7): sobre KG-Refinado, T7 deja de marcar los 11 casos que eran solo de
   formato; sobre r1, su veredicto no cambia.
d. **Mutuales** (decisión 6): RT-C6 pasa de informativo a test. Da «persiste» en r1 y en la prueba
   de r2, y figura en el reporte del gate.
FRENO R4:
- T2 y H2 con la reproducción de lo sellado;
- el reporte del detector de `BKL-0031`;
- la prueba sin API de `BKL-0030`;
- los cambios de T7 y RT-C6;
- el sha256 de lo escrito.

R5 — Suite y shapes del perfil r2. USD 0.
a. **Suite** (scripts/regression_kg.py):
   - LN-1 a LN-8 (diseño, g);
   - T4, T5 y E4-a8 re-direccionados según las propuestas de D1;
   - la corrección del test de `BKL-0028`: que compare contra los tres ids del exterior esperados y
     no cuente `Sujeto_banco_central_del_exterior` (regression_kg.py:788);
   - los matchers de `BKL-0006` y `BKL-0023`, que lean la lista de umbrales (L-ESQ-R2 §1.5);
   - el censo de aristas entre dos nodos con la misma descripción, informativo y sin regla de
     retiro (L-ESQ-R2 §6.5; laudo de r2, §4, :337). En la muestra de la lectura de la matriz, una
     regla de retiro habría retirado M50, que es correcta. El censo corre sobre KG-Reextraído-r1,
     los ensamblados de la tanda 0 y la prueba de r2. Como control, aplicado a las 105 relaciones de
     esa lectura (reports/u_estudio_matriz/lectura/), marca las seis de igual descripción (C22, M50 y
     M56 a M59), con M50 como caso a revisar;
   - el test del ejemplo `cla::5.1.1.1` (laudo de r2, §4, :334; tablero, fila del test del
     ejemplo). Comprueba dos cosas:
     - (i) la Operacion del punto recibe los dos vínculos normativos de los nodos de su punto:
       `condicion_de` desde las dos Condicion o, en la estructura de r1, `limita` desde las dos
       Restriccion;
     - (ii) un nodo del punto remite a `cla::3.7`.

     Sobre el grafo r2 se comprueba además, como informativo, (iii) el elemento de umbral mínimo
     estricto, valor 2, unidad «veces», con la base resuelta a `cla::3.7`.

     Estados esperados:
     - **KG-Reextraído-r1:** «resuelto», con dos Restriccion con `limita` y la `referencia` al 3.7
       (laudo de r2, §4, :334);
     - **KG-Tanda0-Desarrollo-r1:** «persiste»: las dos Condicion están aisladas y no hay remisión;
     - **r2a:** «resuelto». (i) viene de la matriz ampliada sobre el crudo guardado, con las dos
       relaciones marcadas como no verificadas por E3; (ii) viene de las remisiones de R3.d; (iii)
       del par B con la base resuelta. El reporte declara que (i) todavía no pasó por E3;
     - **r2b:** «resuelto», con las relaciones verificadas por E3 y sin la marca. Es la meta de
       U-REEXT-T0 (tablero, fila del test del ejemplo).

     Si en la prueba de r2a no se cumple (ii) o (iii), FRENO con la causa. La entrada de la
     fixture la sella la autora (decisión 9).
b. **Shapes** (scripts/shapes_validator.py), un perfil r2 nuevo:
   - S3 con la matriz ampliada;
   - S18 reescrita: Restricción «limite_cuantitativo» ⇒ lista de umbrales no vacía o marca;
   - S24, enum de Restriccion.tipo, y S25, enum de Comunicacion.tipo con «externa», bloqueantes
     salvo la marca `fuera_de_lista`;
   - S26, claves cerradas por tipo;
   - S27, arista de sujeto con mención y método: informativa en r2a, bloqueante desde r2b;
   - S28, `Sujeto_propuesto` con fila en el registro;
   - S29, destino de `padre_sugerido` en el catálogo único.

   El perfil congelado no cambia.
c. **Selftests:** selftest_regression_kg.py y selftest_shapes_congelado.py siguen en verde, y se
   agregan los casos de los tests y las shapes nuevos.
d. **Entrada r2 de la fixture:** propuesta, con su sha, sin sellar (decisión 9).
e. **Sin regresiones:** sobre los grafos sellados, con sus perfiles, la suite y las shapes dan los
   mismos resultados que hoy, salvo los cambios declarados en R4 y en (a).
FRENO R5, final:
- la tabla de tests y shapes nuevos con su resultado sobre la prueba de r2;
- la ausencia de regresiones;
- la entrada propuesta de la fixture;
- el sha256 de lo escrito.

Commit de la autora.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–k), en todas las etapas.
- Escrituras, según la etapa:
  - en el pipeline, solo los archivos listados en «Leé completos» bajo «el pipeline que se toca»;
  - en scripts/, solo regression_kg.py, regression_kg_esperado.json (la entrada propuesta, sin
    sellar), selftest_regression_kg.py, shapes_validator.py y su selftest;
  - los reportes y scripts nuevos, en data/experiment/r2_codigo/ (se crea), y tu scratchpad.

  No se editan:
  - e0_tablas.py, data/experiment/pyd_r2/, data/experiment/catalogo_unico/ ni los perfiles y
    prompts sellados;
  - el plan, el checklist, el tablero, los laudos ni el backlog.

  Nada sellado se toca (CLAUDE.md §3). No commitees.
- Fuentes firmadas por commit y verificaciones sobre copia (regla k).
- Python:
  - PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B en todo Python.
  - Ningún __pycache__ ni .pyc nuevo: línea de base al inicio y control al cierre.
  - Las dbs de caché solo con `file:…?immutable=1`.
  - Doble corrida byte a byte idéntica de todo lo que la etapa escribe.
- Afirmaciones y citas:
  - Toda afirmación lleva path:línea o comando.
  - Los conteos se recomputan antes de escribirse (§4 i); fracción cruda sobre n chico.
  - Lo que no esté en un artefacto es NO ENCONTRADO.
  - La tesis no se cita por línea de docs/tesis/main.tex; la fuente es Overleaf.
  - Los mentores solo por rol; cero nombres propios.
- Si algo de este mandato contradice un archivo del repo, mandan los archivos y se reporta la
  contradicción.
- Revisión y checkpoint:
  - Paquete de revisión revision_UR2CODIGO_R<n>/ por etapa, con manifest.txt (sha256 y una línea
    por archivo) y nombres únicos.
  - Checkpoint checkpoint_UR2CODIGO.md en el scratchpad, actualizado al cierre de cada etapa y
    antes de cualquier compactación.
- Shell zsh: variables entre comillas o como arrays; ningún comentario con # dentro de los
  bloques de comandos para copiar.

CRITERIO DE ACEPTACIÓN por etapa:
- el reporte corto con las salidas pedidas y sus casos de control;
- git status --short con solo los archivos autorizados de la etapa;
- la reproducción byte a byte de lo sellado con los perfiles existentes;
- doble corrida byte a byte idéntica de lo que la etapa escribe;
- el grep de convenciones, pegado aunque dé vacío.

FRENO al final de cada etapa, y el intermedio de R1.b.
