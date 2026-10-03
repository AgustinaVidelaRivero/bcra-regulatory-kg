BORRADOR — PENDIENTE DE FIRMA DE LA AUTORA (redactado el 03/10/2026 sobre HEAD `e1c9456`)

MANDATO — U-PROMPT-R2: EL PREFIJO NUEVO DE E1 PARA LA RELEASE r2 (lo marcado r2b).
Repo bcra-regulatory-kg. Leé CLAUDE.md y docs/decisiones_caching_extraccion.md antes de empezar:
las cinco decisiones de caching son vinculantes para todo call site de E1 y E3.
- Unidad en CUATRO ETAPAS, P1 a P4, en este orden, con FRENO obligatorio al final de cada una:
  reporte corto (no más de 40 líneas), paquete de revisión (CLAUDE.md §4 g) y espera de la
  revisión y del «seguí» escrito de la autora.
- Costo de API: USD 0 en P1, P2 y P3. P4 es la prueba pareada, con tope fijado por la autora a
  la firma (referencia: la pareada de B5.4 costó USD 0,2902, `d3f2214`). Fuera de P4, ninguna
  llamada a la API. Neo4j no se usa.
- Esta unidad construye y prueba el prefijo; no re-extrae la tanda 0 (U-REEXT-T0, unidad 11) ni
  llena el tablero (unidad 9).

CONTEXTO. Plan, fila B2.11, unidad 10 (docs/plan_tesis.md:399). Depende de las unidades 5 a 8,
cerradas: L-ESQ-R2 FIRMADA (`4ef7650`, con sus notas posteriores y su enmienda 2, `5f9a731`),
U-CAT-UNICO (`bd2122d`), U-PYD (`57a8dd2`) y U-R2-CODIGO (`e1c9456`). Absorbe checklist X2, X4,
X5, X8 y X9. La medición r2a (unidad 9) corre antes y entrega la decisión sobre la regla de
`frecuencia` (tablero :74) y los límites relativos de S18.
- Qué cambia con el prefijo nuevo (L-ESQ-R2 §9, columna r2b; plan :399): la lista de umbrales
  como tramos literales (par A) y el tramo de la frecuencia en Obligacion; la mención del sujeto
  y el sujeto del catálogo como sugerencia; las omisiones con cinco categorías y tramo en todo
  chunk; las tablas serializadas por e0-r2 como contenido confiable frente al residual; los
  límites relativos como tramo sin valor; «externa» en Comunicacion.tipo; la tabla de firmas con
  `condicion_de` → Operacion y → Potestad y la instrucción nueva de Condicion; la instrucción
  sobre el destino de `limita` con los ponderadores; el bloque de catálogo regenerado desde el
  JSON único; la regla de calificadores (mutuales, X8); las incorrectas `E1-prompt` de la
  observación (12) (X5: `BKL-0032`, `BKL-0033`, `BKL-0035`, `BKL-0036`); las correcciones
  sistemáticas de asignación de sujeto de B2.4 que el diseño de U-LISTAS-NOMAP resolvió por
  mención y resolución en código (X9).
- Qué no cambia: `remite_a` no entra al tool schema de E1 ni a sus listas, que siguen con trece
  predicados; `referencia` queda como TextoOrdenado → Comunicacion (enmienda 2, §4 y §10). Los
  nueve tipos de entidad. El prompt de E3 en su prefijo (candado `21a836c7de6d`; laudo de r2,
  §3.2); solo cambia la NOTA del mensaje de usuario de E3 sobre las tablas (`prompt_e3.py:241`),
  que está fuera del prefijo.
- Herencia de U-PYD: el tool schema r2 y los enums ya se generan desde `modelos_r2.py`
  (`pyd_r2/generados/tool_schema_r2.json`, `enums_r2.json`, `manifest_generados_r2.json`): el
  elemento de umbral de E1 (`UmbralE1`), `sujeto_mencion`, las omisiones con categoría, los
  enums con «externa». Esta unidad los conecta al prefijo; no rediseña el modelo.

Leé completos, antes de escribir una línea:
- la fila de la unidad 10 del plan (:399), con sus cinco notas del 02/10; las filas 7 (:396) y
  8 (:397); la fila de la unidad 11 (:400) por el gate que va a correr sobre lo que esta unidad
  produce;
- L-ESQ-R2 en su versión firmada (`git show 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`):
  §1.3 y §1.4 (umbrales; la instrucción nueva sobre el destino de `limita`), §2.3 y §2.4
  (listas; «externa»), §3.3 y §3.4 (mención y resolución), §4.4, §5.3 y §5.4 (omisiones, cinco
  categorías), §6.3 y §6.4 (matriz; instrucción de Condicion), §7.4 (bloque del catálogo), §8.3
  y §8.4 (`relacion_sin_predicado`), §9 y §12; y las tres notas posteriores a la firma del
  archivo actual, en especial la del 02/10/2026 a §1.5 (límites relativos);
- la enmienda 2 de L-ESQ-R2 (`git show 5f9a731:…`), §4 y §10;
- reports/u_listas_nomap/diseno_listas_nomap.md: b (P-b1 a P-b4, con la instrucción del punto 5
  de P-b4), e (P-e1 a P-e4), f (tabla de lo que exige el prompt nuevo);
- reports/u_umbral/reporte_u_umbral.md §4 (par A) y la lectura de `limita`
  (reports/u_umbral/lectura_limita/resultado_lectura_limita.md: los 7 «no» y su destino esperado);
- docs/laudo_release_r2_pipeline.md §1.5 (a) (regla de calificadores) y §3.2 (la clave de caché:
  qué paga un prefijo nuevo);
- data/backlog/backlog.jsonl: `BKL-0032`, `BKL-0033`, `BKL-0035`, `BKL-0036` (incorrectas
  `E1-prompt` de la observación 12) y las nueve entradas `triaged` de B2.4 sobre asignación de
  sujeto (checklist X9, plan :380);
- reports/u_pre_r2/d2_ausencias.md: las ausencias atribuidas a tablas (E-tabla) y a E1 (G), y
  las reglas R-CITA y R-PRES con las que se mide su presencia;
- el prefijo sellado y su cadena, sin editarlos: data/experiment/reextraccion_v2/e1_extractor/prompt_e1.py
  (PREFIJO_SISTEMA, secciones TIPOS, PREDICADOS, SUJETOS, REGLAS 1 a 9, CONTENIDO NO-PROSA :156-165,
  REGLA regula/prohibe/limita :177, FORMATO :193; el bloque FLAGS E0 y «evidencia:» del mensaje,
  :496-503), e1_extractor/perfil_e1.py (`PERFILES_CONOCIDOS`, candado, `perfil()`),
  reextraccion_v2/manifiesto_corpus.py (`perfil_e1`), corpus_v2/runner_corpus.py (la opción
  `--perfil-r2` que conectó U-R2-CODIGO), e3_verificador/prompt_e3.py (:217 el prefijo con
  candado, :241 la NOTA del mensaje);
- data/experiment/pyd_r2/code/generar_r2.py y modelos_r2.py (`UmbralE1`, `RelacionE1`,
  `OmisionE1`, `SalidaE1R2`), y pyd_r2/generados/;
- la salida e0-r2 de los diez TOs versionada por la unidad 9
  (data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2/): el bloque `[TABLA … FIN TABLA]`,
  `flags.tablas_e0`, `contenido_tabular_residual` y `evidencia_tabular`;
- los precedentes de prueba pareada: la pareada de B5.4 (`d3f2214`; plan :399) y el protocolo de
  fichas pareadas con cegado de ESQ-3b (plan :650-:677).

DECISIONES YA TOMADAS. No se re-deciden.
1. El prefijo sellado (`e69feaaa…`) y el perfil `v3_b54` no se editan: el prefijo nuevo vive en
   un módulo propio y se registra como perfil nuevo en `perfil_e1.py`, con candado de sha, y
   llega a las corridas por el campo `perfil_e1` del manifiesto. La opción `--perfil-r2` del
   runner y del ensamblado queda subsumida por el perfil del manifiesto, con el camino por
   defecto byte a byte igual al de hoy.
2. Un prefijo nuevo es un namespace nuevo de caché de E1: U-REEXT-T0 paga E1 de las 2.434
   unidades. E3 conserva su prefijo y su candado (`21a836c7de6d`): un cambio en la NOTA del
   mensaje de E3 no cambia el prefijo, pero sí la clave local de la caché de E3 de los chunks
   cuyo mensaje cambia (`llm_cache.py`; laudo de r2, §3.2). Esta unidad cuenta esos chunks y su
   costo estimado; no los paga.
3. Umbrales (L-ESQ-R2 §1.3 y §1.4, par A): E1 emite, por entidad de los cuatro tipos, la lista
   de tramos literales de las cuantías, y en Obligacion el tramo de la frecuencia; para un
   límite relativo, el tramo sin cuantía («no podrá exceder el nivel alcanzado…»). El valor, la
   unidad, la comparación y la base los arma el código de U-R2-CODIGO, re-aplicado sin cambios
   sobre los tramos. La regla contra copiar celdas rige solo para el contenido tabular residual.
4. Sujetos (§3.3 y §3.4): `sujeto_mencion` obligatoria en toda relación `aplica_a` y `ejecuta`,
   copiada tal cual (artículos y orden del texto), una por sujeto en una enumeración, tomada del
   contexto heredado si el sujeto está ahí; `sujeto_id` como sugerencia del modelo;
   `sujeto_propuesto` deja de ser campo del modelo (P-b2). La resolución la hace el código.
5. Omisiones (§5.3, §5.4, §8.3): campo `omisiones` con `{categoria, tramo, nota}` en todo chunk,
   con las cinco categorías (`meta_normativo`, `tabla`, `formula`, `fuera_de_tipos`,
   `relacion_sin_predicado`); la regla 9 registra en lugar de callar; la regla 4 registra lo no
   extraído como `fuera_de_tipos`; toda relación que el texto expresa y el esquema no representa
   va como `relacion_sin_predicado`.
6. Tablas (plan :399, decisiones del 02/10): el bloque serializado por e0-r2 es confiable y sus
   valores se copian; `contenido_tabular_residual` conserva el tratamiento actual; la clave
   ausente se lee como residual igual a `contenido_tabular`; las líneas de `evidencia_tabular`
   que el bloque reemplazó no se imprimen como «evidencia:». Los metadatos de complejidad por
   tabla, si existen en `flags.tablas_e0`, gradúan la instrucción; si no existen, se declara.
7. Matriz (§6.3 y §6.4): la tabla de firmas del prefijo admite `condicion_de` → Operacion y →
   Potestad, con el desvío declarado de → Potestad; la instrucción de Condicion deja de mandarla
   «a la Excepcion, Obligacion o Restriccion del mismo chunk». E3 verifica lo nuevo en r2b.
8. Listas (§2.3 y §2.4): `Comunicacion.tipo` incorpora «externa»; los demás valores no cambian;
   Obligacion.tipo con sus seis valores y el original guardado.
9. `limita` (§1.4): la instrucción nueva, con el texto de la enmienda: «el destino de `limita`
   es el acto o la magnitud que el tope acota o, si es un ponderador, la exposición que pondera;
   no su base, su finalidad, su consecuencia ni el supuesto que lo habilita».
10. Catálogo (§7.4): el bloque del prompt se regenera desde `catalogo_sujetos_r2.json`
    (`generados_r2/bloque_catalogo_r2.txt`) y entra al prefijo; LN-8 lo controla.
11. Calificadores (laudo de r2, §1.5 a; X8): la instrucción que distingue el sujeto alcanzado
    del calificador que lo acota (mutuales y cooperativas «por las financiaciones que otorguen»),
    con RT-C6-5 como test de aceptación en r2b.
12. `remite_a` fuera de E1 (enmienda 2, §4 y §10): control sobre el prefijo nuevo y su tool
    schema; `referencia` solo TextoOrdenado → Comunicacion.
13. Generados: `pyd_r2/generados/` se regenera con `generar_r2.py` desde el `modelos_r2.py`
    vigente; control: el tool schema y los enums no cambian salvo lo que un cambio del modelo
    posterior a `57a8dd2` haya alterado y esté declarado; el manifiesto registra el sha nuevo.
14. La prueba pareada (P4) compara el prefijo sellado y el nuevo sobre los mismos chunks, con
    fichas pareadas cegadas y lectura asistida revisada por la autora (protocolo de ESQ-3b, plan
    :650-:677; pareada de B5.4, `d3f2214`). No
    decide nada sola: su resultado es insumo del tope y del gate de U-REEXT-T0.

P1 — Diseño del prefijo y del mensaje. USD 0.
a. Documento de diseño en data/experiment/prompt_r2/diseno_prefijo_r2.md: sección por sección,
   el texto sellado al lado del texto nuevo, con la decisión que lo manda; el tool schema r2 que
   se conecta y qué campos cambian respecto del sellado; el mensaje de usuario nuevo (bloque de
   tablas serializadas, residual, flags) y la NOTA nueva de E3; la lista de las decisiones 3 a
   12 con el párrafo exacto que las implementa.
b. Las instrucciones para X5 y X9: por cada `BKL` de X5 y cada entrada `triaged` de X9, qué
   oración del prefijo nuevo la ataca, o la declaración de que queda para el validador o para
   otra unidad.
c. Censo, USD 0: chunks de los diez TOs cuyo mensaje de E3 cambia por la NOTA nueva (los que
   tienen `tablas_e0`), con el costo estimado a la tarifa de referencia; lo que paga E1 (las
   2.434 unidades) a esa misma tarifa. Insumo del tope de U-REEXT-T0.
FRENO P1 (intermedio, antes de escribir código): la autora aprueba el texto del prefijo y del
mensaje.

P2 — Implementación. USD 0.
a. Módulo nuevo del prefijo r2 y su perfil en `perfil_e1.py` (`PERFILES_CONOCIDOS` suma el
   nuevo; candado de sha del prefijo y del tool schema); `manifiesto_corpus.py` lo admite;
   manifiestos nuevos de los diez TOs y de desarrollo con `perfil_e1` nuevo, sin tocar los
   existentes; el runner y el ensamblado despachan por el perfil del manifiesto.
b. Control de reproducción (regla de U-R2-CODIGO): con los perfiles existentes, E0 legada
   34/34, los tres ensamblados sellados y el grafo r2a de la unidad 9 byte a byte; el prefijo
   sellado, su hash y el prefijo de E3 sin cambio de un byte; el tool schema de E1 del perfil
   `v3_b54` byte a byte.
c. Selftests: casos del perfil nuevo en `selftest_manifiesto` (P3 y P4 para el perfil nuevo:
   requests de E1 y E3 byte a byte en doble corrida sin API, con el cliente simulado) y en
   `selftest_pyd_r2` para los generados; `selftest_cablev3` y los de E0 siguen en verde.
d. Prueba en seco: el request de E1 de dos chunks con tabla (`cap::1.2`, `ric::9.2`), de uno con
   sujeto propuesto y de `cla::5.1.1.1`, impresos en el paquete, sin llamar a la API.
FRENO P2: hash del prefijo nuevo y sha del tool schema; los sellados reproducidos; selftests; los
cuatro requests.

P3 — Lectura del crudo nuevo en el pipeline. USD 0.
a. El validador r2 lee la salida del prefijo nuevo (forma «r2», `validador_r2.validar`): los
   tramos de umbral entran al llenado de la lista (par A) con la misma verificación de r2a; la
   mención entra a la resolución por relación (R1 a R4, con R3 y los desacuerdos); las omisiones
   con categoría entran al registro; `fuera_de_tipos` y `relacion_sin_predicado` se cuentan.
b. Prueba sobre un crudo sintético que cubra cada campo nuevo, y sobre el crudo guardado de la
   tanda 0 leído como «v3» (sin cambios: control de que el camino r2a no se mueve).
c. Shapes y suite del perfil r2 sobre un grafo sintético con los campos nuevos: S27 en fase
   r2b, LN-3 y LN-7 con los valores nuevos.
FRENO P3: lo que cambia en la cadena de lectura, con sus selftests; 0 cambios en el grafo r2a.

P4 — Prueba pareada. Tope fijado a la firma.
a. Muestra de chunks de los diez TOs, sorteada con semilla declarada y estratificada: con tabla
   serializada, con sujeto propuesto en el crudo guardado, con cuantía, con `omisiones_no_prosa`,
   y sin ninguna marca. Tamaño y estratos los fija la autora (decisión abierta 2).
b. E1 con el prefijo sellado (desde la caché, USD 0) y con el nuevo (API, dentro del tope) sobre
   los mismos chunks; validación r2 de las dos salidas; fichas pareadas cegadas (protocolo de
   ESQ-3b) con las dimensiones: umbral con tramo literal verificado, mención verificada, omisiones
   con categoría y tramo, valores copiados de la tabla de `cap::1.2`, firma nueva de
   `condicion_de`, destino de `limita`.
c. Lectura asistida de las fichas, revisada por la autora; conteos con Wilson al 95 %; costo real
   contra el tope.
FRENO P4, final: la tabla pareada, los contadores del validador en las dos salidas (vocabulario
retirado, fuera de lista, tramos no verificados), el costo, el hash del prefijo, y la
recomendación para el tope de U-REEXT-T0.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–l), en todas las etapas.
- Escrituras, y solo estas:
  - data/experiment/reextraccion_v2/e1_extractor/: el módulo nuevo del prefijo r2 y
    perfil_e1.py; cliente_e1.py solo si el tool schema lo exige, declarado;
  - data/experiment/reextraccion_v2/manifiesto_corpus.py, corpus_v2/runner_corpus.py (despacho
    por perfil) y data/experiment/tanda0/code/ensamblar_tanda0.py (ídem);
  - data/experiment/reextraccion_v2/e3_verificador/prompt_e3.py, solo la NOTA del mensaje
    (:241); el prefijo (:217) y su candado no se tocan;
  - manifiestos nuevos en data/experiment/reextraccion_v2/manifiestos/ (los existentes no);
  - data/experiment/pyd_r2/generados/ (regenerados) y pyd_r2/code/validador_r2.py y
    selftest_pyd_r2.py, solo para leer la forma «r2» completa;
  - selftest_manifiesto.py, selftest_cablev3.py y los selftests del perfil nuevo;
  - data/experiment/prompt_r2/ (se crea): diseño, censos, muestra y fichas de la pareada,
    reportes; y tu scratchpad.
  - No se editan: prompt_e1.py (PREFIJO_SISTEMA y la cadena sellada), el perfil `v3_b54`, el
    prefijo de E3, modelos_r2.py (salvo decisión expresa de la autora), E0, E2, el ensamblado
    fuera del despacho por perfil, la suite, las shapes, el plan, el checklist, el tablero, los
    laudos, el backlog ni nada sellado (CLAUDE.md §3). No commitees.
- Caching: docs/decisiones_caching_extraccion.md, cinco decisiones vinculantes; la clave de la
  caché local y el namespace se reportan antes y después.
- Python: PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; ningún .pyc nuevo.
- Afirmaciones y citas: path:línea o comando; conteos recomputados; firmados por commit (regla k);
  NO ENCONTRADO explícito; la tesis no se cita por línea de main.tex; cero nombres propios.
- Acciones de la autora como PENDIENTES hasta su confirmación (regla j).

CRITERIO DE ACEPTACIÓN. El prefijo nuevo registrado como perfil con candado y hash; el camino
sellado byte a byte intacto (prefijo `e69feaaa…`, E3 `21a836c7de6d`, los tres ensamblados, el
grafo r2a); el tool schema conectado desde los generados de U-PYD, sin `remite_a` y con trece
predicados; cada decisión 3 a 12 con su párrafo en el prefijo o en el mensaje; la cadena de
lectura probada sobre crudo sintético sin mover r2a; la pareada dentro del tope, con fichas
cegadas y lectura asistida revisada por la autora. Commit de la autora al cierre de cada etapa.

DECISIONES ABIERTAS PARA LA AUTORA, A LA FIRMA.
1. Tope de la prueba pareada (referencia: USD 0,2902 en B5.4).
2. Tamaño y estratos de la muestra pareada (propuesta: 40 chunks, 8 por estrato).
3. La regla de `frecuencia` (tablero :74), con la medición de la unidad 9: si los plazos sin
   cuantía temporal dejan de ir a `frecuencia`, el prefijo lo refleja en el tramo que pide.
4. Si la salida de E1 para los límites relativos lleva una marca propia o solo el tramo (nota a
   L-ESQ-R2 §1.5): hoy, solo el tramo, y el código arma el elemento sin valor.
5. Si `modelos_r2.py` necesita un ajuste para la forma final del campo de umbral o de omisiones;
   si lo necesita, se autoriza por enmienda a este mandato y se regeneran los generados.
