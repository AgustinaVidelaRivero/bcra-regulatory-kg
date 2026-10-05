FIRMADO por la autora el 03/10/2026 (redactado el 03/10/2026 sobre HEAD `e1c9456`; borrador en `e91f864`,
decisiones 15 a 21 en `a304b89` y `43dc44f`; firma por mensaje de la autora, commit PENDIENTE)

MANDATO — U-PROMPT-R2: EL PREFIJO NUEVO DE E1 PARA LA RELEASE r2 (lo marcado r2b).
Repo bcra-regulatory-kg. Leé CLAUDE.md y docs/decisiones_caching_extraccion.md antes de empezar:
las cinco decisiones de caching son vinculantes para todo call site de E1 y E3.
- Unidad en CUATRO ETAPAS, P1 a P4, en este orden, con FRENO obligatorio al final de cada una:
  reporte corto (no más de 40 líneas), paquete de revisión (CLAUDE.md §4 g) y espera de la
  revisión y del «seguí» escrito de la autora.
- Costo de API: USD 0 en P1, P2 y P3. P4 es la prueba pareada, con tope de USD 2 (decisión 18),
  revisable en el FRENO P1 con la estimación de P1.c y P1.d (referencia: la pareada de B5.4 costó
  USD 0,2902, `d3f2214`). Fuera de P4, ninguna llamada a la API. Neo4j no se usa.
- Esta unidad construye y prueba el prefijo; no re-extrae la tanda 0 (U-REEXT-T0, unidad 11) ni
  llena el tablero (unidad 9).

CONTEXTO. Plan, fila B2.11, unidad 10 (docs/plan_tesis.md:399). Depende de las unidades 5 a 8,
cerradas: L-ESQ-R2 FIRMADA (`4ef7650`, con sus notas posteriores y su enmienda 2, `5f9a731`),
U-CAT-UNICO (`bd2122d`), U-PYD (`57a8dd2`) y U-R2-CODIGO (`e1c9456`). Absorbe checklist X2, X4,
X5, X8 y X9. **Arranca después de que la unidad 9 (U-MED-R2A) cierre M1:** P1 lee la salida e0-r2 de
los diez TOs que esa etapa versiona (`data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2/`)
y su grafo r2a. La regla de `frecuencia` (tablero :74) se decide en el FRENO P1 con la medición de la
unidad 9 (decisión 20); los límites relativos van como tramo sin valor (decisión 21).
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
  mención y resolución en código (X9); y, por las decisiones D6 a D8 del protocolo entre tandas
  (`docs/protocolo_entre_tandas.md`, §8 a §10, FIRMADO por la autora el 03/10/2026 (borrador en `9eabab0`, firma en `a304b89`)): el tramo literal de evidencia por entidad, `Comunicacion.tipo` y `numero` y el
  TextoOrdenado derivados en código con `Definicion.termino` literal, y las válvulas nuevas
  (`otras_propiedades` en relaciones; `source` y `destino` en `relacion_sin_predicado`).
- Qué no cambia: `remite_a` no entra al tool schema de E1 ni a sus listas, que siguen con trece
  predicados; `referencia` queda como TextoOrdenado → Comunicacion (enmienda 2, §4 y §10). Los
  nueve tipos de entidad. El prompt de E3 en su prefijo (candado `21a836c7de6d`; laudo de r2,
  §3.2); solo cambia la NOTA del mensaje de usuario de E3 sobre las tablas (`prompt_e3.py:241`),
  que está fuera del prefijo.
- Herencia de U-PYD: el tool schema r2 y los enums ya se generan desde `modelos_r2.py`
  (`pyd_r2/generados/tool_schema_r2.json`, `enums_r2.json`, `manifest_generados_r2.json`): el
  elemento de umbral de E1 (`UmbralE1`), `sujeto_mencion`, las omisiones con categoría, los
  enums con «externa». Esta unidad los conecta al prefijo; los únicos cambios al modelo son los de
  las decisiones 15 a 17, con sus generados regenerados.

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
15. Tramo literal de evidencia por entidad (decisión D6 de la autora, `docs/protocolo_entre_tandas.md`, §8 a §10, FIRMADO por la autora el 03/10/2026 (borrador en `9eabab0`, firma en `a304b89`)): cada
    entidad de los nueve tipos lleva un campo `tramo` con el tramo del texto propio o heredado del
    chunk que la funda, copiado tal cual; el código lo verifica como subcadena normalizada del
    texto de E0 (la regla de la mención, P-b3 y P-b4: exacta, por tokens o no verificada, con marca)
    y lo guarda en el nodo. Hace verificable la descripción y deja la evidencia de una entidad de
    tipo dudoso. El campo entra a `modelos_r2.py` (`_EntidadE1` y el nodo del grafo) y a los
    generados; la etapa de diseño estima su costo en tokens de salida (P1.d).
16. Campos que salen del prompt y se derivan en código (decisión D7): `Comunicacion.tipo` y
    `numero` se derivan de `codigo` (L-ESQ-R2 §2.4 ya deriva el tipo en r2a) y `materia`,
    `archivo` y `version` del TextoOrdenado se derivan de E0 y del inventario, como ya hace la
    canonización de E4 (`r2_codigo/r3_freno.md`, §3): los cinco campos salen del tool schema de E1
    y el prompt pide solo `codigo`. `Definicion.termino` se pide literal («copiado tal cual») y el
    código lo verifica como el tramo de la decisión 15.
17. Válvulas de escape (decisión D8): `otras_propiedades` también en `relations[]`, con la misma
    descripción que en las entidades; la omisión `relacion_sin_predicado` admite `source` y
    `destino` opcionales (los `local_id` de la relación que el esquema no representa); la
    instrucción de las omisiones `fuera_de_tipos` y `relacion_sin_predicado` pide anotar en `nota`
    el tipo o el predicado que el modelo habría usado. Los tres cambios entran a `modelos_r2.py`,
    al validador (las `otras_propiedades` de la relación van a la arista como no definidas, como
    `properties_no_definidas` en el nodo) y a los generados.
18. Tope de la prueba pareada: USD 2 (decisión de la autora del 03/10/2026), revisable en el FRENO
    P1 con la estimación de costo de P1.c y P1.d.
19. Muestra de la pareada (decisión de la autora del 03/10/2026): 40 chunks sorteados, 8 por
    estrato, más los casos de control fijos fuera del sorteo (`cap::1.2`, `ric::9.2`,
    `cla::5.1.1.1` y el chunk de la cláusula de mutuales de RT-C6-5, `pro::1.1.2.5`) y un estrato
    fuera de muestra con chunks de TOs ya excluidos de B6.3 (a) (el estrato «ESQ ya excluidos» del
    protocolo entre tandas, §7), cuya E0 se produce con e0-r2 en el scratchpad y no se versiona:
    mide si el prefijo generaliza sin contaminar el conjunto de evaluación.
20. La regla de `frecuencia` (tablero :74) se decide en el FRENO P1, con la medición de la unidad 9
    (decisión de la autora del 03/10/2026); el prefijo refleja lo decidido en el tramo que pide.
21. Límites relativos: E1 emite solo el tramo, sin marca propia, y el código arma el elemento sin
    valor (nota del 02/10/2026 a L-ESQ-R2 §1.5; decisión de la autora del 03/10/2026).

P1 — Diseño del prefijo y del mensaje. USD 0.
a. Documento de diseño en data/experiment/prompt_r2/diseno_prefijo_r2.md: sección por sección,
   el texto sellado al lado del texto nuevo, con la decisión que lo manda; el tool schema r2 que
   se conecta y qué campos cambian respecto del sellado; el mensaje de usuario nuevo (bloque de
   tablas serializadas, residual, flags) y la NOTA nueva de E3; la lista de las decisiones 3 a
   12 y 15 a 17 con el párrafo exacto que las implementa, y los campos del tool schema que entran
   (tramo de evidencia, `otras_propiedades` en relaciones, `source` y `destino` en la omisión) y
   que salen (`Comunicacion.tipo` y `numero`, `materia`, `archivo` y `version`). La regla
   `regula`/`prohibe`/`limita` del prefijo (`prompt_e1.py:177`) se alinea con el control de
   coherencia tipo–predicado de `BKL-0038` (plan :396; marca del modelo r2): una Restricción
   «prohibicion» usa `prohibe` y las de límite usan `limita`, y el documento muestra el texto
   sellado y el nuevo lado a lado.
b. Las instrucciones para X5 y X9: por cada `BKL` de X5 y cada entrada `triaged` de X9, qué
   oración del prefijo nuevo la ataca, o la declaración de que queda para el validador o para
   otra unidad.
c. Censo de costo, USD 0, del prefijo nuevo por unidad y en total, sobre el crudo guardado de la
   tanda 0: los tokens de entrada del prefijo nuevo (system y tool schema, con la fórmula de caching
   de la decisión 2 de `docs/decisiones_caching_extraccion.md`: escritura de caché en la primera
   unidad de cada corrida secuencial y lectura en las demás) más el mensaje de cada unidad; los
   tokens de salida de todos los campos nuevos (tramos de umbral, mención del sujeto, omisiones con
   tramo, tramo de evidencia por entidad, `otras_propiedades`), estimados por unidad desde el crudo
   guardado (largo de los tramos que fundarían cada entidad, relación y omisión); los chunks cuyo
   mensaje de E3 cambia por la NOTA nueva (los que tienen `tablas_e0`), a la tarifa de E3. Con ese
   costo por unidad se recalculan el tope de U-REEXT-T0 (2.434 unidades) y el costo de referencia de
   las tandas 1, 2 y 3 del protocolo entre tandas (§5: 3.292 unidades del ejemplo de la tanda 1,
   5.669 de los digeribles restantes más 2.008 de los no-RI, 976 de los RI), que hoy están a la tarifa
   de la tanda 0 (USD 0,0166 por unidad). Las cifras van al FRENO P1 y, si la autora las aprueba,
   al protocolo como nota fechada.
d. Costo y riesgo del tramo de evidencia por entidad (decisión 15), USD 0: sobre el crudo guardado
   de la tanda 0, el largo en tokens de salida del tramo mínimo que fundaría cada entidad (una
   aproximación por tipo, con la regla de la mención sobre la descripción guardada), el total por
   chunk y por corrida, y su costo a la tarifa de salida del modelo; y la verificación en código:
   la regla (subcadena normalizada del texto propio o heredado del chunk; exacta, por tokens o no
   verificada), su marca en el nodo, el contador y el selftest que la cubre. Lo mismo, en breve,
   para `Definicion.termino` literal (decisión 16). Riesgo de corte (`BKL-0030`): con la salida más
   larga estimada (todos los campos nuevos), cuántas unidades de la tanda 0 quedarían cerca del
   techo de `max_tokens` del primer intento del perfil r2 (`runner_corpus.py`, R4.b de U-R2-CODIGO,
   `26d274d`), con qué margen, y si el reintento a 16.384 las cubre; las que no, listadas, con la
   propuesta (partir la unidad, R4.b) para el FRENO P1.
FRENO P1 (intermedio, antes de escribir código): la autora aprueba el texto del prefijo y del
mensaje, con las estimaciones de P1.c y P1.d, y decide el tope de P4 (decisión 18) y la regla de
`frecuencia` (decisión 20).

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
   con categoría entran al registro; `fuera_de_tipos` y `relacion_sin_predicado` se cuentan, con
   sus `source` y `destino` cuando vienen; el tramo de evidencia de cada entidad y el `termino`
   literal se verifican con su marca (decisiones 15 y 16); `Comunicacion.tipo` y `numero` y el
   TextoOrdenado se derivan en código (decisión 16); las `otras_propiedades` de la relación van a
   la arista como no definidas (decisión 17).
b. Prueba sobre un crudo sintético que cubra cada campo nuevo, y sobre el crudo guardado de la
   tanda 0 leído como «v3» (sin cambios: control de que el camino r2a no se mueve).
c. Shapes y suite del perfil r2 sobre un grafo sintético con los campos nuevos: S27 en fase
   r2b, LN-3 y LN-7 con los valores nuevos.
FRENO P3: lo que cambia en la cadena de lectura, con sus selftests; 0 cambios en el grafo r2a.

P4 — Prueba pareada. Tope USD 2 (decisión 18), revisado en el FRENO P1.
a. Muestra de chunks de los diez TOs, sorteada con semilla declarada y estratificada (decisión 19):
   40 chunks, 8 por estrato, en cinco estratos: con tabla serializada, con sujeto propuesto en el
   crudo guardado, con cuantía, con `omisiones_no_prosa`, y sin ninguna marca. Fuera del sorteo, los
   casos de control fijos: `cap::1.2` (la tabla invertida), `ric::9.2` (el cuadro de códigos),
   `cla::5.1.1.1` (el ejemplo de la tesis) y `pro::1.1.2.5` (la cláusula de mutuales de RT-C6-5).
   Y un estrato fuera de muestra: 8 chunks sorteados de los TOs ya excluidos de B6.3 (a) del estrato
   «ESQ ya excluidos» del protocolo (§7: ayccef, expaef, opefci, adrei), dos por TO, cuya E0 se
   produce con e0-r2 en el scratchpad y no se versiona; mide si el prefijo generaliza a TOs que no
   vio, sin tocar el conjunto de evaluación. Las fichas de los casos fijos y del estrato fuera de
   muestra se cuentan aparte de la tasa de los 40.
b. E1 con el prefijo sellado y con el nuevo sobre los mismos chunks. Para los 40 sorteados y los
   casos fijos, el brazo sellado sale de la caché (USD 0) y el brazo nuevo paga la API dentro del
   tope. Para los 8 chunks del estrato fuera de muestra (ayccef, expaef, opefci, adrei) no hay salida
   del prefijo sellado en la caché: el brazo sellado también corre por la API, dentro del tope de
   USD 2, sobre su E0 legada (`correr_e0.py` sin `--version-e0`, en el scratchpad), y el brazo nuevo
   sobre su E0 e0-r2. Validación r2 de las dos salidas; fichas pareadas cegadas (protocolo de
   ESQ-3b) con las dimensiones: umbral con tramo literal verificado, mención verificada, omisiones
   con categoría y tramo, valores copiados de la tabla de `cap::1.2`, firma nueva de
   `condicion_de`, destino de `limita`.
   Declaración: la pareada compara release contra release, el prefijo sellado con la E0 legada
   frente al prefijo nuevo con e0-r2, no el prefijo solo. Las diferencias no se atribuyen al prompt
   o a E0 por separado, salvo donde la ficha lo permita (por ejemplo, la tabla de `cap::1.2`, que
   solo existe serializada en e0-r2). El reporte lo dice así en su primera línea.
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
  - data/experiment/pyd_r2/code/modelos_r2.py y selftest_pyd_r2.py, solo para los campos de las
    decisiones 15 a 17 (tramo de evidencia por entidad, `otras_propiedades` en relaciones, `source`
    y `destino` en la omisión, retiro de `Comunicacion.tipo` y `numero` y de `materia`, `archivo` y
    `version` del tool schema de E1); data/experiment/pyd_r2/generados/ (regenerados) y
    pyd_r2/code/validador_r2.py, para leer la forma «r2» completa;
  - selftest_manifiesto.py, selftest_cablev3.py y los selftests del perfil nuevo;
  - data/experiment/prompt_r2/ (se crea): diseño, censos, muestra y fichas de la pareada,
    reportes; y tu scratchpad.
  - No se editan: prompt_e1.py (PREFIJO_SISTEMA y la cadena sellada), el perfil `v3_b54`, el
    prefijo de E3, modelos_r2.py fuera de los campos de las decisiones 15 a 17, E0, E2, el ensamblado
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
predicados; cada decisión 3 a 12 y 15 a 21 con su párrafo en el prefijo o en el mensaje, y el
tool schema con los campos que entran y sin los que salen; el costo por unidad del prefijo nuevo
estimado y el tope de U-REEXT-T0 recalculado; la cadena de
lectura probada sobre crudo sintético sin mover r2a; la pareada dentro del tope, con fichas
cegadas y lectura asistida revisada por la autora. Commit de la autora al cierre de cada etapa.

DECISIONES ABIERTAS A LA FIRMA: ninguna. Las cuatro del borrador quedaron decididas el 03/10/2026
(decisiones 18 a 21); el tope de P4 y la regla de `frecuencia` se revisan en el FRENO P1 con las
estimaciones de P1.c y P1.d y la medición de la unidad 9.

FIRMA. FIRMADO por la autora el 03/10/2026, con el ajuste de P4.b (el brazo sellado del estrato fuera de
muestra corre por la API con su E0 legada) y la declaración de que la pareada compara release contra
release. Sin decisiones abiertas.

NOTAS POSTERIORES A LA FIRMA. El texto firmado no se edita; estas notas se leen junto con él.
- **03/10/2026 — firma y dependencia (decisión de la autora).** La firma está commiteada en `b901f6d`; el
  «commit PENDIENTE» del encabezado queda superado. La dependencia del CONTEXTO («arranca después de que
  la unidad 9 cierre M1») se precisa así: U-PROMPT-R2 adelanta de P1 lo que no depende de la unidad 9
  (P1.a sin el mensaje de tablas, P1.b, y la parte de P1.c y P1.d que sale del crudo guardado de la tanda
  0); completa lo que depende de la E0 e0-r2 versionada (el mensaje de tablas, el censo de E3 con
  `tablas_e0`) tras el FRENO M1 de U-MED-R2A; y el FRENO P1 se hace tras el FRENO M2 de U-MED-R2A. La
  decisión 20 (regla de `frecuencia`) se toma en el FRENO P1 con el conteo de M2.c de U-MED-R2A y, si M3
  cerró, con la lectura de M3.d; si M3 no cerró, la autora la elige antes de que arranque P2, porque P2
  congela el prefijo. Motivo: la medición de los plazos mandados a `frecuencia` no sale de M1 sino de
  M2.c y M3.d (`UMED_R2A_medicion_r2a.md:138-139`, `:169`), hallazgo de la instancia de esta unidad al
  verificar la precondición sobre `b901f6d`.
- **03/10/2026 — casos de control fijos de la pareada (decisión de la autora).** En la decisión 19, y en
  la lista de P4.a que la ejecuta (`:249`), el caso `ric::9.2` pasa a ser `ric::9.2.1`. `ric:9.2` es una
  de las nueve anclas de las ausencias de D2 de U-PRE-R2-DIAG (`reports/u_pre_r2/d2_ausencias.md:42`),
  no un chunk: ninguna de las dos E0 de la tanda 0 tiene un chunk con ese id
  (`data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_ric.json` y
  `salida_tanda0_r2/chunks_ric.json`, `f8dedd4`), y la unidad portadora del cuadro de códigos es
  `ric::9.2.1` (`d2_ausencias.md:138`), que en e0-r2 trae dos tablas serializadas (`ric::tabla022` y
  `ric::tabla023`). El id equivocado vino de la redacción del mandato, que tomó el ancla como id de
  chunk sin controlarla contra la E0. Se suma `cap::6.2.2.6` como caso fijo: su tabla (`cap::tabla037`,
  posicional; `salida_tanda0_r2/chunks_cap.json`) tiene 20 celdas combinadas que E0 no pudo asignar a
  sus filas, y el bloque deja el 100 % de la columna «entre zonas 1 y 3» en la fila de la banda 2-3 y
  el 40 % de «entre zonas adyacentes» en las dos filas de subtítulo «Años*», sin marca de a qué filas
  se aplican. Los casos fijos quedan en cinco: `cap::1.2`, `ric::9.2.1`, `cla::5.1.1.1`, `pro::1.1.2.5`
  y `cap::6.2.2.6`. Si la pareada muestra en `cap::6.2.2.6` la asociación mal hecha (por ejemplo, el
  100 % de «entre zonas 1 y 3» atado a la banda 2-3 por la fila donde quedó), esa tabla sale al
  tratamiento residual por una lista en código. La prueba en seco de P2.d (`:225`) usa `ric::9.2.1`.
- **03/10/2026 — regla del encabezado de lista (F1) y escrituras (decisión de la autora).** La regla del
  encabezado entra en P1 así: cada inciso extrae la norma compuesta con su encabezado (sujeto, modalidad
  y cuantificador), y la unidad del encabezado no emite nodo por el solo anuncio (regla 1 del borrador
  del prefijo, `data/experiment/prompt_r2/diseno_prefijo_r2.md`, R16, sin commit al 03/10/2026;
  `BKL-0035`, `data/backlog/backlog.jsonl`). La regla dice qué `tramo` lleva la entidad compuesta. Es la
  primera mitad de la opción F1-A de U-DIAG-PROCESO (`reports/u_diag_proceso/reporte_u_diag_proceso.md`,
  sin commit al 03/10/2026); la segunda mitad, que hacía emitir el deber a la unidad del encabezado, no
  se adopta: contradice la condición de cierre de `BKL-0035`. Declaración de la autora: F1 entra en el
  ciclo de la ventana aunque la destapó ESQ-2 y no la tanda 0, como el desvío del §2.4 de la enmienda
  de uso de la ventana (`git show 30f106c:data/experiment/esq/enmienda_uso_ventana_2026-09-30.md`,
  `:61-64`); sus fichas son de TOs ya excluidos de B6.3 (a) (ayccef, expaef y adrei,
  `data/experiment/esq/documentos_excluidos_esq.json`), así que no reduce el conjunto de evaluación. En
  P4, los chunks de esas cinco fichas (`ayccef::4.2.7.2`, `expaef::6.6.2`, `ayccef::3.4.1`,
  `expaef::1.1.2.5` y `adrei::4.3.1::intro`) entran fuera del sorteo y miden la corrección; la
  generalización se lee en el sorteo. La quinta es la unidad de un encabezado: con la regla no emite
  nodo y se mide por sus incisos. Se suman a las escrituras de la unidad
  `data/experiment/reextraccion_v2/e1_extractor/validador_e1.py` y su selftest (`selftest_e1.py`), solo
  para la traducción de la forma de salida «r2» (punto 4 del §10 del diseño), con la condición de que
  los perfiles existentes den el resultado byte a byte igual.
- **03/10/2026 — fe de erratas de la nota anterior (decisión de la autora).** La nota anterior dice que el
  reporte de U-DIAG-PROCESO (`reports/u_diag_proceso/reporte_u_diag_proceso.md`) está «sin commit al
  03/10/2026». Está commiteado en `93ce4b7`, anterior al commit de esa nota (`a807136`): la nota se
  redactó antes de los dos commits y entró desactualizada en ese punto. El resto de la nota no cambia.
- **03/10/2026 — E3 y la unidad del encabezado de lista, encabezados en línea de título y pata de E3 en
  P4 (decisión de la autora).** Se suman a las escrituras de la unidad
  `data/experiment/reextraccion_v2/e3_verificador/prompt_e3.py`, para la NOTA de los encabezados de lista
  además de la de tablas (el prefijo de E3 y su candado no se tocan), y `e3_verificador/ratchet_e3.py`
  con su selftest (`selftest_e3.py`), para la guarda ampliada con la salvaguarda. La regla de la guarda
  la fija la enmienda a LAUDO B (`docs/enmienda_laudo_B_guarda_ratchet_2026-10-03.md`): cubre cualquier
  faltante cuya cita verificada sea la cláusula ordenadora, solo si la unidad quedó sin Obligacion,
  Restriccion ni Potestad, y solo con la forma de salida «r2», de modo que los perfiles existentes den
  el resultado byte a byte igual. Queda autorizado de forma expresa, además del despacho por perfil, el
  cambio en `corpus_v2/runner_corpus.py:862` que la guarda ampliada requiere (diseño, §4.5).
  Condición: el reporte de U-REEXT-T0 lista cada unidad eximida. El punto 18 del §10.1 del diseño queda
  aprobado por tipo. (i) El inciso compone con su encabezado y, si el último encabezado no trae la
  modalidad o el sujeto, los toma del bloque heredado más cercano que los trae. (ii) El plazo, el
  ámbito o la condición que vale para cada inciso se compone en el inciso, tanto si el encabezado está
  en la línea de título como si tiene unidad; lo que es otra norma del encabezado queda en su unidad.
  (iii) Si los incisos son supuestos alternativos, la norma principal se compone en cada uno con su
  cuantificador; si son condiciones conjuntas no se compone, los incisos son Condicion y, cuando el
  encabezado está en la línea de título, la norma principal queda como límite declarado; ante la duda
  se tratan como conjuntas. La NOTA de E3, la regla 1 y la sección de composición del prefijo se
  alinean con el tipo (ii). P4 suma una pata de E3, con la NOTA y la guarda, sobre cuatro encabezados de
  lista (`ctacte::8.3::intro`, `ctacte::8.4::intro`, `ctacte::6.4.7::intro` y `adrei::4.3.1::intro`),
  reportada aparte y dentro del tope de USD 2 de la decisión 18. Fuentes: diseño de la unidad
  (`data/experiment/prompt_r2/diseno_prefijo_r2.md`, §4.5 y §10.1, puntos 18 y 20); plan, `:400`;
  `BKL-0035` y `BKL-0039` (`data/backlog/backlog.jsonl`).
- **03/10/2026 — FRENO P1 aprobado, aclaración sobre los supuestos alternativos y dos ajustes de texto
  (decisión de la autora).** P1 está commiteada en `fca019d`. Aclaración al tipo (iii) de la nota
  anterior: los supuestos alternativos se componen en cada ítem solo si el encabezado está en la línea
  de título; si el encabezado tiene unidad propia, los ítems son Condicion y la norma queda en esa
  unidad. Es lo que dicen el diseño y el borrador del prefijo (`git show
  fca019d:data/experiment/prompt_r2/diseno_prefijo_r2.md`, R30); la nota anterior lo escribió sin esa
  distinción. Decisiones del FRENO P1 (`git show fca019d:data/experiment/prompt_r2/freno_p1.md`): se
  aprueban el texto del prefijo y el del mensaje, con la variante B de `frecuencia` (el campo recibe
  solo la periodicidad; el momento sin cuantía queda en la descripción y en el `tramo`). El tope de la
  pareada queda en USD 2 (decisión 18) y el de U-REEXT-T0 en USD 69, para E1 a E3 de las 2.434
  unidades. Los puntos 1, 2, 3, 5, 8 y 10 del §10.1 del diseño quedan confirmados como los recomienda el
  freno: el TextoOrdenado no lleva `tramo`; los patrones de las decisiones 11 y 21 se describen sin
  citar los casos de prueba; «externa» se deriva de `codigo` en el código; el elemento sin valor del
  límite relativo va en `validador_r2.py`; queda la aclaración de R15 sobre «sujeto_propuesto»; y la
  guarda de `ejecuta` se extiende a los cinco TOs de desarrollo. No se agrega la marca
  `guarda_ampliada`: el reporte de U-REEXT-T0 separa las exenciones por tipo, porque LAUDO B exime solo
  `enumeracion_incompleta` y todo faltante eximido de otro tipo viene de la ampliación. Dos ajustes de
  texto entran antes de congelar el prefijo: en R8, la Condicion de un ítem cuya norma está en otra
  unidad va sin `condicion_de`; en R14, la Comunicacion citada sigue siendo entidad, con su `referencia`
  desde el TextoOrdenado.
- **04/10/2026 — P2 cerrada, y agregado a P3: todo lo que extrae el modelo pasa por E3 (decisión de
  la autora).** P2 está commiteada en `20b7f60`. `selftest_manifiesto` da 44/49 sobre una copia: los 5
  fallos de P5 vienen de la ruta absoluta que guarda el reporte sellado de E2, y pasan solo desde la
  raíz del repo. Los selftests corren sobre una copia (CLAUDE.md §4, regla l).
  Hallazgo que motiva el agregado. `validador_r2` valida el crudo del intento que E3 aceptó
  (`corpus_v2/runner_corpus.py`, `entrada_r2`), no la salida que aceptó `validador_e1` y que E3 vio. Por
  eso acepta elementos que el primer validador rechazó y que E3 nunca vio:
  - primer intento de los diez TOs de la tanda 0: 667. Son 655 relaciones de la matriz ampliada, con
    `no_verificada_e3`, y 12 sin marca: 2 entidades «Restriction» corregidas por alias, sus 6
    relaciones, 2 predicados corregidos por forma y 2 relaciones de sujeto
    (`data/experiment/pyd_r2/resultados/prueba_crudo_t0.md`, control C3, `b706d37`; recontado por la
    revisión sobre el crudo, con los dos validadores);
  - población final que lee la cadena r2: en los diez TOs, 701, 697 con marca y 4 sin marca; en
    desarrollo, 630, 627 y 3. Las 8 que faltan de las 12 eran de dos unidades que E3 mandó a reintento;
  - la marca se calcula hoy por la firma (`pyd_r2/code/modelos_r2.py`, invariante de
    `no_verificada_e3`), no por lo que pasó por E3. Con el perfil r2b marcaría relaciones que E3 sí vio:
    su esquema ya admite la matriz ampliada (`e1_extractor/perfil_e1.py`, `firma_valida=M.firma_r2`).
  Agregado a P3. Rige solo con la forma «r2»; los perfiles existentes y los grafos r2a no cambian.
  a. Todas las correcciones que hoy aplica `validador_r2` (alias de tipo, forma del predicado y las de
     las relaciones de sujeto) pasan a aplicarse en `validador_e1`, antes de E3, para que los elementos
     lleguen corregidos al verificador.
  b. Con el perfil r2b, el ensamblado toma solo lo que pasó por E3: `validador_r2` deja de leer la
     salida cruda para decidir qué entra.
  c. `no_verificada_e3` queda como red de seguridad, calculada por lo que pasó por E3 y no por el tipo
     de combinación. Un control de suite o de shape exige cero elementos de extracción sin verificar.
  d. Las relaciones derivadas en código (`remite_a`, `establecida_en`) y los valores de umbral
     calculados en código no llevan `no_verificada_e3`: su procedencia las declara derivadas, con su
     control propio. Estado verificado: `remite_a` ya lo cumple en el modelo (propiedades `alcance`,
     `destino` y `evidencia`, sin marcas de E1); los umbrales llevan origen, regla y tramo verificado;
     la `establecida_en` derivada lleva `rol_fuente: derivada_de_procedencia` (536 aristas en
     KG-Tanda0-Diez-r2a), pero el modelo no la declara derivada. P3 lo fija.
  e. Las unidades que E3 no terminó (ratchet agotado y cola humana). P3 presenta las dos opciones, fuera
     del grafo hasta resolverse o adentro y marcadas, y la autora decide en el FRENO P3. Hoy entran
     marcadas: en la tanda 0 son 71 unidades en los diez TOs (291 nodos y 466 aristas con `cola_humana`)
     y 44 en desarrollo (216 y 343).
  f. P3 reporta, con la tanda 0 como referencia, cuántos elementos cambian de estado con cada cambio, y
     si alguno se pierde.
  g. Los grafos r2a sellados no se tocan.
  Escrituras que se suman a las de P3: `e1_extractor/validador_e1.py` y `selftest_e1.py` (ya
  autorizados por la nota del 03/10/2026); `corpus_v2/runner_corpus.py`, solo `entrada_r2` y lo que
  alimenta, detrás de la forma «r2»; `pyd_r2/code/modelos_r2.py`, solo la invariante de
  `no_verificada_e3` y la declaración de la `establecida_en` derivada; y sus selftests. El tool schema
  (`0c391f2b…`) y el prefijo (`14d6b63b508e`) no cambian. P3 no edita la suite ni las shapes: deja el
  conteo en el reporte del ensamblado, y el control de (c) entra con los pedidos de suite ya asignados
  antes del gate de r2b (`docs/plan_tesis.md:400`), ampliado de las relaciones a todo elemento de
  extracción.
  Orden con U-R2-CODIGO-2: P3 y C2 comparten `runner_corpus.py` y no corren a la vez. La segunda
  arranca sobre el commit de la primera.
- **04/10/2026 — orden y control de (c) (decisiones de la autora).** P3 va primero; C2 de U-R2-CODIGO-2
  arranca sobre el commit de P3. El control de (c) queda como lo dice la nota anterior: P3 deja en su
  reporte el conteo de elementos de extracción sin verificar, y el control de suite o de shape entra con
  los pedidos de suite ya asignados antes del gate de r2b (`docs/plan_tesis.md:400`). La pareada de P4
  usa la E0 versionada en `f8dedd4`; los manifiestos r2b los actualiza U-REEXT-T0 como su primer paso.
- **04/10/2026 — etapa nueva P3b: parche del prefijo, del mensaje y del lazo de E3, antes de P4 (decisión
  de la autora).** Sale de la revisión independiente (`reports/u_revision_libre/reporte.md` y
  `freno_b1.md`; commit PENDIENTE) y de U-DIAG-VINCULO (`b0ee084`). Va después del commit de P3 y antes
  de P4, y re-congela el prefijo.
  Criterio general. Para todo hallazgo que dependa de cómo interpreta el modelo una frase, E1 copia
  literalmente el marcador y la clasificación la hace el código: una forma nueva que aparezca en las
  tandas se agrega al código y se re-aplica sobre lo extraído, sin cambiar el prefijo. Los patrones se
  describen con palabras propias, sin ventanas de cinco palabras de los chunks de prueba
  (`data/experiment/prompt_r2/p1/nofiltracion.py`). Las propuestas que cambian el esquema no se adoptan:
  el contenido entra por las válvulas existentes o se declara.
  En el prefijo:
  a. Recomendación (1.3): se extrae como Obligacion. E1 copia literalmente el marcador de la modalidad en
     `otras_propiedades`, la descripción dice que es una recomendación y el código clasifica la modalidad.
  b. Consecuencia de un incumplimiento (1.4): Obligacion o Potestad del sujeto que la aplica, si el texto
     lo nombra; si no, omisión con su tramo; nunca Restriccion. E1 copia el marcador en
     `otras_propiedades`.
  c. Excepcion (2.8): se conecta con la norma que exceptúa cuando esa norma está en su unidad.
  d. Predicados (3.2): se definen `regula`, `requiere` y `condiciona`, y se resuelve en el texto la
     contradicción de `regula` desde Restriccion, sin tocar la matriz.
  e. Lista dentro de una unidad (1.18): la composición vale también ahí.
  f. Listas de excepciones (U-DIAG-VINCULO): regla en la composición con el encabezado. Cada ítem es una
     Excepcion compuesta con la norma del encabezado, sin `exceptua` cuando esa norma está en otra unidad.
  En el mensaje de E1:
  g. `es_item` (1.2) busca el encabezado terminado en «:» entre los bloques heredados, no solo en el
     último, de modo que funcione con o sin el recorte de herencia del punto (h) de C2 de U-R2-CODIGO-2.
  h. Mini-chunks que empiezan a mitad de oración (2.16), con su par en la verificación del tramo: un
     tramo que va del título al cuerpo tiene que verificar.
  En E3:
  i. La NOTA de las categorías nuevas de omisión (3.4; FRENO A1, punto 8).
  En `ratchet_e3.py`:
  j. Los veredictos con `faltantes` como texto que se pueden leer, se leen (2.2).
  k. El reintento que reemplaza sin comparar (2.14): la etapa presenta las opciones con sus números y la
     autora decide. No se implementa antes.
  En `validador_r2.py`:
  l. `derivar_comunicacion` no da por Comunicación una ley escrita como «A-39» (1.12).
  Para cada punto, el diseño dice si admite la forma «el modelo copia, el código decide» o si necesita
  que el modelo decida, y por qué.
  Dos frenos:
  - FRENO P3b-1, de diseño: el texto del parche lado a lado con el congelado, el control de
    no-filtración, el diseño de g a l y las opciones de k. Sin congelar ni implementar. La autora aprueba
    el texto.
  - FRENO P3b-2: el prefijo re-congelado con su hash y sus candados, el tool schema sin cambio, los
    selftests sobre una copia, los sellados reproducidos, y la estimación de costo de la pareada y de
    U-REEXT-T0 con el prefijo nuevo.
  Rige solo con la forma «r2». No cambia el esquema ni el tool schema. Escrituras: las ya autorizadas de
  esta unidad (`prompt_r2b.py` y sus reemplazos, `perfil_e1.py`, `prompt_e3.py` solo en la NOTA,
  `ratchet_e3.py`, `validador_r2.py`, sus selftests y `data/experiment/prompt_r2/`). No edita
  `runner_corpus.py`. Comparte `pyd_r2/code/selftest_pyd_r2.py` con C2 de U-R2-CODIGO-2: las dos
  implementaciones no corren a la vez.
  P4 cambia así: `cla::5.1.1::intro` se suma a los casos fijos y, con `cla::5.1.1.1`, mide la corrección;
  y se suma un estrato de listas de excepciones que no se leyeron al escribir la regla, elegidas por
  lectura y no por el tipo léxico del censo de U-DIAG-VINCULO, para medir si generaliza. P4 no se
  autoriza hasta el FRENO P3b-2.
  Fuera de esta etapa: el alcance en títulos que no terminan en «:» (2.7) va por código, no por prompt;
  el plazo asumido máximo (1.8) es regla de L-ESQ-R2 §1.3 (`4ef7650`) y cambiarla pide una enmienda
  firmada; el linaje (2.6) y las cuantías en tipos sin `umbrales` (2.10) se declaran como límite.
- **04/10/2026 — agregados a P3b y decisión sobre la cola humana (decisión de la autora).** Salen de la
  verificación de la sección 4.4 de la tesis. Se suman a la etapa P3b; lo demás de esa etapa no cambia.
  1. Punto j (2.2): veredictos de E3 que llegan como texto dentro de `faltantes`. Recuento sobre
     `corpus_tanda0/salida/*/finales.jsonl` y `veredictos.jsonl`: de las 71 unidades en cola humana de
     la tanda 0, 25 son esta falla de formato, 21 de las 36 con el veredicto inutilizable y 4 de las 35
     que fueron a la cola tras el reintento. En las 21, el texto trae el veredicto entero: 5 dicen
     `completo_ok` y 16 `faltantes_detectados`. De las 16, 7 traen algún faltante de severidad alta y 9
     no; de esas 9, 8 se leen como JSON y 1 (`cap::5.3.2.5`) no es JSON válido.
     El punto j deja de ser «se leen»: el FRENO P3b-1 presenta dos opciones con sus números y la autora
     decide. Opción 1: leer esa forma en código, sin API. Opción 2: volver a pedir el veredicto a E3,
     con su costo estimado. Para cada una: cuántas de las 25 salen de la cola y a qué estado van con la
     política vigente del ratchet, cuántas quedan, y qué pasa con el texto que no es JSON válido. No se
     implementa antes de la decisión.
  2. Punto k (2.14): descripción que copia la nota del verificador. Caso: en la re-extracción de
     `cla::6.3.3`, aceptada tras el reintento, la descripción de una Condicion repite palabras de la
     nota de E3 que no están en el texto de la unidad. P3b-1 suma:
     - una medida, sin API: en cuántas de las 220 unidades aceptadas tras el reintento
       (`corpus_tanda0/salida_dirigida/*/finales.jsonl`; 219 en `salida/`) alguna descripción contiene
       texto de la nota de E3 que no está en la unidad. La regla de la medida (ventana de palabras y
       normalización) se declara antes de contar, y los casos se listan;
     - dos defensas, como propuesta: el mensaje del reintento marca la nota de E3 como contenido que
       no se copia, y un control en código marca las descripciones con texto de la nota ausente de la
       unidad. El control marca: no rechaza ni corrige sin decisión de la autora.
  3. Cola humana. Decisión de la autora del 04/10/2026: las unidades de la cola humana entran al grafo
     marcadas, y en cada tanda se revisa una muestra, con la tasa de error medida y reportada con la
     tanda (nota del 04/10/2026 al pie de `docs/protocolo_entre_tandas.md`; `docs/plan_tesis.md:363`).
     En esta unidad:
     - P3 ya no presenta las dos opciones del punto e del agregado a P3 del 04/10/2026: quedó decidida
       la segunda, adentro y marcadas;
     - el texto de `e3_verificador/ratchet_e3.py` (`:351-355` en HEAD: «el chunk NO ingresa al grafo
       hasta resolución») se alinea con la decisión en la implementación de P3b. No es un comentario:
       es el campo `todo` que el ratchet escribe en cada registro de `cola_humana.jsonl`. Por eso el
       cambio rige solo con la forma «r2», y las salidas selladas se siguen reproduciendo byte a byte.
       No cambia qué unidades entran al grafo.
- **04/10/2026 — P3b: las `otras_propiedades` de la relación llegan a la arista (decisión de la autora, tras
  el FRENO P3, §5.2).** E2 copia a la arista solo `MARCAS_ARISTA_R2` (`e2_reduce/e2_lib.py:801-803`), y las
  `otras_propiedades` de la relación, que el validador deja en `properties_no_definidas`, no llegan. P3b lo
  corrige. Se suma `e2_reduce/e2_lib.py` a las escrituras de P3b, solo para ese cambio y solo en el camino del
  perfil r2 (`:793-797`), con una condición: los perfiles existentes dan byte a byte lo mismo, con los cinco
  ensamblados sellados reproducidos. Levanta, solo para ese cambio, la prohibición de editar E2 del texto
  firmado (`:292-295`).
  Verificado sobre una copia: las `otras_propiedades` de una entidad sí llegan al nodo, como
  `properties_no_definidas`, en el grafo del E2 r2 y en el ensamblado (variante de `cadena_sintetica_p3.py`
  con una entidad con `otras_propiedades`). Los marcadores de modalidad de los puntos a y b van en la entidad:
  no dependen de este cambio.
  A tratar en el diseño (FRENO P3b-1): `properties_no_definidas` es una clave del nodo fuera de `properties`,
  y la vista que lee el agente lleva solo `properties` (`data/experiment/tanda0/code/comun_tanda0.py:78-94`).
  El diseño dice dónde queda la modalidad que clasifica el código para que el agente la vea, o declara que
  su exportación va con U-NAV-DISENO.
- **04/10/2026 — reparto de lo que P3 dejó para decidir (decisiones de la autora; FRENO P3, §5).** El punto 2
  va a P3b (nota anterior). Los puntos 1, 3, 4 y 6 van a C2 de U-R2-CODIGO-2, como sus puntos (n), (o), (p) y
  (q) (`docs/mandatos/UR2CODIGO2_correcciones_previas_a_reext.md`, nota del 04/10/2026). El punto 5 queda como
  está: se cuenta según dónde se ancla la entidad.
- **04/10/2026 — P3b: las operaciones se unen solo dentro de su punto (decisión de la autora, tras la
  verificación de la sección 4.5 de la tesis; `reports/verif_union_ops/`, commit PENDIENTE).** Con el perfil
  r2 y la fase r2b, la clave de fusión de la Operacion lleva el punto de la procedencia, como la de los demás
  nodos de contenido (`e2_reduce/e2_lib.py:839-860`, `entity_slug_r2`). Hoy la Operacion se funde por
  etiqueta (`:118-121`) y el nodo conserva la etiqueta y las propiedades de la primera unidad (`:993`). La
  regla nueva elimina las uniones entre puntos distintos; las uniones dentro de un mismo punto no cambian. Es
  un cambio de código sobre lo guardado, USD 0.
  Medida de referencia sobre los dos grafos r2a:
  - en KG-Tanda0-Desarrollo-r2a, 37 de 1.555 operaciones juntan más de un punto (ext 29, cap 5 y cla 3) y
    pasan a ser 89;
  - en KG-Tanda0-Diez-r2a, 59 de 2.047 (ext 29, ctacte 16, cap 5, pagjub 5, cla 3 y polcre 1) pasan a ser 148;
  - en cada grafo, 5 nodos juntan unidades de un mismo punto y quedan como están.
  La lectura de las 37 de desarrollo es de esa verificación: 18 correctas, 8 incorrectas y 11 dudosas.
  Va a P3b porque P3b ya edita `e2_lib.py`. Condiciones:
  - los dos grafos r2a sellados y los tres ensamblados r1 se siguen reproduciendo byte a byte: la regla nueva
    rige solo con la fase r2b;
  - `ensamblar_r2` no conoce la fase (`e2_lib.py:863-865`), y la llaman `tanda0/code/ensamblar_tanda0.py:825`
    y `corpus_v2/runner_corpus.py:1061`. P3b dice, antes de implementar, cómo le llega la fase a E2. Si hace
    falta tocar esos dos sitios de llamada, es una línea en cada uno, como despacho por perfil, declarada: se
    levanta para esa línea la restricción de no editar `runner_corpus.py` de la nota de la etapa P3b. Los dos
    archivos los edita también C2 de U-R2-CODIGO-2: las dos implementaciones no corren a la vez;
  - se suma a las escrituras de P3b, solo para el caso nuevo: `e2_reduce/selftest_e2.py`. El control de
    `data/experiment/r2_codigo/selftest_r4.py:239-241` («Operacion y Sujeto siguen como v3») sigue valiendo
    para la fase r2a y no se edita.
  Control: la lista de las operaciones que se separan en los dos grafos r2a, con sus puntos; ninguna unión
  dentro de un mismo punto cambia; y lo que cambia aguas abajo, contado: las aristas que tocan esos nodos (589
  en desarrollo y 711 en diez; 439 y 481 de ellas son `remite_a`), la adjudicación de colisiones entre TOs y
  los conflictos de propiedades.
  La alternativa que propone la verificación (unir por etiqueta plegada dentro del mismo encabezado de E0)
  queda como mejora a medir después de U-REEXT-T0 (`docs/plan_tesis.md:400`).
- **04/10/2026 — FRENO P3b-1 aprobado, y decisiones para P3b-2 (decisiones de la autora).** El diseño quedó
  commiteado en `023f9a0` (`data/experiment/prompt_r2/freno_p3b1.md` y `p3b/`). La revisión reprodujo sus 11
  salidas byte a byte sobre una copia. El «seguí» de P3b-2 lo mandó la autora (declaración de la autora del
  04/10/2026), con estas decisiones:
  1. El texto queda aprobado: el prefijo con sus 12 reemplazos, el mensaje de E1, la NOTA de E3 y el aviso
     del reintento.
  2. j: opción 1. Los veredictos de E3 que llegan como texto se leen en código, con reparo y con la marca de
     cómo se leyeron.
  3. k: k4. El reintento con menos elementos se acepta con la marca `reintento_con_menos_elementos` y se
     cuenta por tanda. No se lee por muestra: no agrega una obligación al protocolo. La recuperación por
     tramo de lo que el reintento dejó se mide después de U-REEXT-T0 (`docs/plan_tesis.md:400`).
  4. Copia de la nota de E3: las dos defensas. El control marca en el nodo, no solo en los registros de la
     corrida, y P3b lee los 45 casos de la tanda 0.
  5. l: como se diseñó.
  6. El mensaje de E1 suma una frase para las unidades con la herencia recortada por C2 de U-R2-CODIGO-2,
     que explica el marcador «[recorte de E0: …]».
  7. Las claves nuevas de `properties_no_definidas` (`modalidad`, `consecuencia` y `modalidad_clasificada`)
     se cuentan aparte de las demás.
  8. La unión de las operaciones por punto (nota anterior): P3b toca una línea en cada sitio de llamada de
     `ensamblar_r2` para pasarle la fase, declarada, y suma `e2_reduce/selftest_e2.py` solo para el caso
     nuevo.
  Orden: P3b-2 va primero, y la implementación de C2 de U-R2-CODIGO-2 arranca sobre su commit.
- **04/10/2026 — FRENO P3b-2 revisado, y decisiones de la autora (commit de P3b-2 PENDIENTE).** El freno está
  en `data/experiment/prompt_r2/freno_p3b2.md`. La revisión reprodujo sobre copias: los dos grafos r2a
  sellados y los tres ensamblados r1; el prefijo re-congelado (hash `3817de475c93`, 55.105 caracteres, tool
  schema sin cambio); la unión de las operaciones por punto (37 pasan a ser 89 en desarrollo y 59 a 148 en
  diez); los selftests (`selftest_prompt_r2b` 34/34, `selftest_e3` 95/95, `selftest_pyd_r2` 343/343 y
  `selftest_e2` 41/41); la cadena sintética de P3b-2, 20/20; y las salidas de `p3b2/salida/`, byte a byte.
  Decisiones:
  1. Tope de U-REEXT-T0: sube de USD 69 a USD 72. La estimación central con el parche es USD 50,74, con la
     NOTA de E3 como cota alta, y por el factor 1,4 da 71,04 (`p3b2/salida/costo_p3b2.json`). Reemplaza el
     tope de USD 69 de la nota del 03/10/2026 sobre el FRENO P1. El tope de la pareada sigue en USD 2.
  2. Marca de la copia de la nota de E3. La lectura de los 45 casos dio 11 copias reales, en 11 unidades, y 34
     coincidencias legítimas (`p3b2/lectura_copia_nota.md`). `properties_no_definidas.copia_nota_e3` marca
     una posible copia: no afirma que lo sea. Se vuelve a medir sobre el crudo de U-REEXT-T0, con la regla de
     `p3b2/regla_lectura_copia_nota.md`; si la precisión sigue baja, la regla se ajusta en código entre
     tandas. Las 11 copias reales de los grafos r2a quedan declaradas: `cla::6.3.3`, `ctacte::3.2.1.2`,
     `ctacte::3.2.1.7`, `ctacte::6.4.1.1`, `ctacte::10.2.4.2`, `ext::3.5.4.2`, `ext::3.18.3::intro`,
     `ext::7.1.1::intro`, `ext::7.11::intro`, `ext::14.2.1.10` y `pagjub::2.8.2::intro`.
  3. `derivar_comunicacion`: con la forma r2, el paso `derivar_de_codigo_o_label` lee el tramo verificado.
     La nota a la política está en `data/experiment/pyd_r2/politica_campos_r2_notas.md`.
  4. `MODALIDAD_FORMAS` (`pyd_r2/code/validador_r2.py`) no está medida. P4 reporta cuántas recomendaciones y
     consecuencias detecta la clasificación del código, contra una lectura de muestra. La lista se ajusta en
     código entre tandas si hace falta.
  5. Las marcas de j y de k4 llegan al reporte por `vistos_por_e3`: va a C2 de U-R2-CODIGO-2, como punto (t).
  6. h cubre solo el tramo simple: es un límite declarado. U-REEXT-T0 cuenta los mini-chunks a mitad de
     oración con un tramo de dos segmentos.
  7. Cadena sintética de P3 (`p3/cadena_sintetica_p3.py`): con el código nuevo da 26 de 27. Falla su caso
     «LÍMITE» de la arista, que esperaba que la arista no llevara `properties_no_definidas`. P3b-2 actualiza
     ese caso esperado y su resumen antes de su commit. El otro caso «LÍMITE» de esa cadena, el de las
     omisiones, lo actualiza C2 de U-R2-CODIGO-2 cuando implemente su punto (p).
- **04/10/2026 — P3b-2 commiteada, y enmienda 4 a L-ESQ-R2 (decisiones de la autora).** P3b-2 quedó en
  `c8c3970`, y la nota anterior, en `226ef7b`.
  - El punto l queda respaldado por la enmienda 4 a L-ESQ-R2
    (`data/experiment/esq/enmienda4_L-ESQ-R2_comunicacion_tramo_2026-10-04.md`, FIRMADA por la autora el
    04/10/2026; commit de la firma PENDIENTE): con la forma r2, el tipo de la Comunicación se deriva del tramo
    verificado, y el número se toma del `codigo` y se controla contra el tramo. Precisa la decisión 16 de este
    mandato para la forma r2.
  - La marca `copia_nota_e3` no se le muestra al agente: sirve para la evaluación y para las muestras, no
    para la navegación (borrador de U-NAV-DISENO).
  - Cadena sintética de P3: el caso de la arista ya está actualizado en el árbol de trabajo (dos archivos de
    `data/experiment/prompt_r2/p3/`), y la cadena da 27 de 27 sobre una copia. Su commit está PENDIENTE: no
    entró en `c8c3970`.
- **04/10/2026 — la cadena sintética de P3b-2 después del punto (t) de C2 (decisión de la autora, tras el
  FRENO C2 de U-R2-CODIGO-2).** Con el código de C2, la cadena da 18 de 20: los casos de
  `data/experiment/prompt_r2/p3b2/cadena_sintetica_p3b2.py:260` y `:289` afirman que `vistos_por_e3` lleva
  solo la marca de la copia, y el punto (t) suma las otras dos. Esos dos casos y el resumen
  (`p3b2/salida/resumen_cadena_sintetica_p3b2.json`) los actualiza C2, antes de su commit: los dos archivos
  se suman a las escrituras de C2, solo para eso. P4 parte de la cadena en 20 de 20.
  Otra herencia de C2, para U-REEXT-T0: `e1_extractor/selftest_prompt_r2b.py` lee `salida_tanda0_r2/` y
  exige que ninguna unidad lleve `herencia_recortada` (`:118` y `:148-149`). Hoy pasa, 34 de 34. Sobre
  `salida_tanda0_r2b/` ese caso cambia, por `ric::11.2.3`: quedó en el borrador del mandato de U-REEXT-T0.
- **04/10/2026 — «seguí» de P4 preparado, con agregados de la autora (despacho PENDIENTE, sobre el commit de
  C2 de U-R2-CODIGO-2).** Agregados a P4 por decisión de la autora del 04/10/2026:
  - `cap::8.5.1`, `cap::8.5.2` y `cap::8.5.3` entran como casos fijos: son ítems que el punto g del parche
    reconoce (`data/experiment/prompt_r2/freno_p3b1.md:28-29`);
  - P4 cuenta las Condicion de ítems sin `condicion_de` en el brazo nuevo, y en cuántas la norma está en
    otra unidad;
  - en la pata de E3, cada caso que quede con la marca `copia_nota_e3` se relee con la regla de
    `data/experiment/prompt_r2/p3b2/regla_lectura_copia_nota.md`.
  Dos cosas las puse yo en el texto del «seguí», y la autora las confirma o las saca al despachar: el tamaño
  del estrato de listas de excepciones, 8 unidades, y el reporte de los tokens de salida por carácter de
  texto propio en el brazo nuevo.
  Lo demás de P4 queda como en el mandato y sus notas: los cinco casos fijos, `cla::5.1.1::intro`, los
  chunks de las fichas de F1, el estrato fuera de muestra, la pata de E3, la medición de `MODALIDAD_FORMAS`
  contra una lectura de muestra y el tope de USD 2. La estimación de P3b-2 cuenta 64 llamadas y no incluye
  `cla::5.1.1::intro`, los tres de `cap::8.5` ni el estrato de listas de excepciones: P4 proyecta el costo
  antes de correr y frena si pasa el tope.
- **04/10/2026 — FRENO P4 revisado; etapas nuevas P3c y P4b, antes de U-REEXT-T0 (decisión de la autora).**
  P4 corrió sobre `9f6361e` y costó USD 1,1086, de un tope de 2 (`data/experiment/prompt_r2/freno_p4.md` y
  `p4/`, sin commit al 04/10/2026). Corrí sus ocho scripts de USD 0 dos veces sobre una copia: las diez
  salidas son iguales a las de `p4/salida/`. El prefijo de P3b-2 no emite la Excepcion de `cla::5.1.1.1`.
  La autora revisó la lectura asistida y la corrigió en cuatro puntos. Los verifiqué contra el crudo
  (`p4/salida/resultados_p4.jsonl`), y la unidad los asentó en `p4/lectura_p4.md`, sección «Revisión de la
  autora»:
  - `cap::5.4.4`: el `limita` del brazo nuevo va de Restriccion a Definicion, el validador lo rechaza por la
    firma y no llega al grafo. La marca pasa a «no emite». La tabla pareada no cambia: el destino de
    `limita` sigue en 3 y 5 de 6 fichas, porque el brazo sellado no emitía la relación en esa ficha.
  - `cla::5.1.1.1`: el brazo nuevo funde dos condiciones en un nodo. La etiqueta y el umbral son del monto;
    la descripción y el tramo, del repago. El brazo sellado emitía dos Condicion.
  - `cla::5.1.1::intro`: el brazo nuevo pierde la Definicion de alcance que emitía el sellado y declara la
    frase como `meta_normativo`. La exclusión de los créditos para consumo o vivienda no queda en ninguna
    entidad.
  - De las 24 omisiones `meta_normativo` del brazo nuevo, una por ficha, 9 son contenido normativo: 8 de las
    16 que copian texto propio, y la conformidad previa del encabezado en `ext::13.4.8`.
  Decisión de la autora: el prompt se ajusta antes de U-REEXT-T0, en tres pasos de esta unidad, cada uno con
  su FRENO.
  - **P3c-1, diseño**, sin implementar: el texto lado a lado y el control de no-filtración, como en P3b-1.
  - **P3c-2, implementación**, con el prefijo re-congelado.
  - **P4b, prueba corta**: casos que no se hayan leído al escribir el ajuste, elegidos por lectura y
    sellados antes de correr, con los dos tipos de lista del punto 2; más `cla::5.1.1::intro` y
    `cla::5.1.1.1`, que miden la corrección del ejemplo. Con su proyección de costo antes de correr.
  Los cinco puntos del ajuste:
  1. `meta_normativo`, más estricta: nunca una frase con un deber, una prohibición, una facultad, una
     condición, una excepción, un alcance o una modalidad.
  2. Las listas que exceptúan, en sus dos tipos. Cuando los ítems son las cosas exceptuadas
     (`cla::5.1.1.1`), cada ítem es una Excepcion, incluida la excepción con contra-excepción. Cuando los
     ítems son las condiciones de una sola excepción (`ext::13.4`), cada ítem es una Condicion de esa
     excepción. En los dos tipos, la descripción de la entidad del ítem nombra la norma que se exceptúa. No
     lleva `exceptua` cuando esa norma está en otra unidad.
  3. Un nodo por condición, con la etiqueta coherente con su descripción, su tramo y su umbral.
  4. La norma del encabezado no se repite como entidad propia dentro del ítem: se compone en la descripción
     de la entidad del ítem (`ext::13.4.4`).
  5. Sin mención cuando el texto no nombra al sujeto: de las 15 menciones que no verifican en las 76 fichas
     del brazo nuevo, 14 son «las entidades».
  Agregados, en la misma etapa:
  - `cap::tabla037` pasa a la lista de tablas forzadas a residual (`prompt_r2b.TABLAS_RESIDUALES_FORZADAS`),
    como preveía la nota del 03/10/2026 sobre los casos fijos de la pareada.
  - El validador verifica el tramo de las omisiones contra el texto propio y el heredado. Hoy lo verifica
    solo contra el propio (`pyd_r2/code/validador_r2.py:1316`): de las 22 omisiones que no verifican, 7
    copian texto heredado.
  - Los candados de los insumos que no entran al hash del prefijo: la lista de tablas forzadas (F04b), las
    líneas fijas del mensaje de E1 (F22 y F22b) y las NOTAS de E3 (F23). Solo comparan: no entran al pedido
    ni cambian ninguna clave. Se sellan después del ajuste del texto. Para esto la autora autorizó
    `e3_verificador/prompt_e3.py` más allá de la NOTA y, en `data/experiment/mantenimiento/`, las cuatro
    filas de la tabla de reprocesamiento y las variaciones R29, R29b, R30 y R32 del selftest de claves, que
    pasan de «cambia» a «frena». T1 de U-REEXT-T0 solo los verifica.
  Fuera de la unidad: la condición 10 de la tanda 1 queda pendiente hasta P4b
  (`docs/checklist_pre_escalado.md:81`); el tope de U-REEXT-T0 sigue en USD 72; y la base de caché de P4 no
  se reutiliza en U-REEXT-T0. Fe de erratas de la nota del 04/10/2026 sobre la enmienda 4 a L-ESQ-R2: el
  arreglo de la cadena sintética de P3 está commiteado en `f3922d8`.
- **04/10/2026 — agregado a P3c-1 (decisión de la autora, tras la revisión del FRENO P4).** La nota anterior
  quedó en `bd77541`, y P4, en `2ed47a0`. El diseño de P3c-1 suma cuatro cosas.
  - **El encabezado puro de lista** no se extrae ni se declara como omisión. Precisa el punto 1: una frase
    que solo anuncia los ítems puede llevar un verbo de deber («Las entidades financieras deben:»,
    `adrei::4.3.1::intro`) y no es `meta_normativo`.
  - **Casos.** `ayccef::2.4.8.1` y `ayccef::4.2.7.2` entran como casos de control. `cap::3.1.14::intro` y
    `ric::3.1.8` quedan para analizar en el diseño. Los cuatro son omisiones `meta_normativo` con texto
    propio del brazo nuevo de P4 que no estaban entre las nueve de la revisión de la lectura.
  - **El criterio de `cap::5.4.4`** (una relación que el validador de su brazo rechaza no llega al grafo) se
    aplica a las seis `condicion_de` del brazo sellado que su validador rechaza por la firma: `cap::2.5.7`,
    `cla::5.1.1.1`, `ctacte::5.1.2.2`, `ext::10.2.5`, `ext::3.3.3.3` y `ext::3.5.6.9`
    (`data/experiment/prompt_r2/p3c/insumos_p4_p3c.py`, sin commit al 04/10/2026).
  - **Tercer escalón del reintento de E1, con transmisión por partes.** Se diseña en P3c-1 y se implementa en
    P3c-2. Es para las unidades que cortan también en el reintento de 16.384 tokens y no se pueden partir, y
    para las partes que cortan. La autora autorizó para esto `e1_extractor/cliente_e1.py` y
    `corpus_v2/runner_corpus.py`.
    - No hace falta tocar `data/experiment/evaluacion/llm_cache.py`, que está sellado. Alcanza un adaptador
      del cliente real (`cliente_e1.py:167`) cuyo `messages.create` use `messages.stream` y devuelva el
      mensaje final. La caché guarda y reconstruye ese mensaje igual (`llm_cache.py:310-311` y `:205-211`),
      y la clave cambia solo por `max_tokens`, en ese intento.
    - El SDK 0.100.0 rechaza un pedido sin transmisión de más de 21.333 tokens de salida cuando no hay
      `timeout` explícito en la llamada ni en el cliente (`resources/messages/messages.py:984-987` y
      `_base_client.py:731-740`). El máximo de salida de `claude-haiku-4-5` es de 64.000 tokens
      (documentación de modelos de la API, consultada el 04/10/2026).
    - Con la salida que midió P4, en la tanda 0 lo necesitarían `ric::11.2::intro` y la parte mayor de
      `cap::4.2.1.2`.
    - Quedan abiertos para el diseño: el techo; la fila de la tabla de reprocesamiento, que la autorización
      de las cuatro filas no cubre; y una prueba con una llamada real, que tiene costo.
- **04/10/2026 — FRENO P3c-1 revisado; decisiones de la autora para P3c-2 y P4b.** Las dos notas anteriores
  quedaron en `bd77541` y en `28ec100`. El freno está en `data/experiment/prompt_r2/freno_p3c1.md` y el
  diseño, en `p3c/diseno_p3c.md` (sin commit al 04/10/2026). Corrí sus siete scripts dos veces sobre una
  copia: las 13 salidas son iguales a las de `p3c/salida/`. Las marcas y la tabla de P4, regeneradas con el
  criterio de `cap::5.4.4` en los dos brazos, son iguales a las de `p4/salida/`: cambian seis marcas del
  brazo sellado, y `condicion_de` con firma nueva queda sin pares en los tres grupos.
  Decisiones de la autora:
  1. **El texto, aprobado:** los 15 reemplazos del prefijo (borrador `322c5a23e9b7`, de 55.105 a 59.909
     caracteres, con el tool schema sin cambio), la línea de alcance del mensaje de E1 y las dos NOTAS de E3.
     Para `cap::3.1.14::intro` y `ric::3.1.8` vale la lectura del diseño: sus frases son alcance y van en la
     descripción de su norma.
  2. **Contador de omisiones `meta_normativo`** cuyo tramo trae una marca de deber, de facultad, de
     condición o de excepción: en `validador_r2`, contando sin rechazar, para vigilarlo en U-REEXT-T0.
  3. **La vigencia (P3C-a2):** de una frase de vigencia, solo la fecha es `meta_normativo`. Un régimen de
     transición con condiciones es contenido normativo.
  4. **P4b,** con los grupos del diseño (29 unidades en dos brazos, más E3 en 6) y tope de USD 1,5. Para
     las listas de lo que queda afuera (b1), la elección busca por lectura otras formas de enunciar la
     exclusión, no solo la léxica de `cla::5.1.1`. Si no aparece ninguna, b1 se mide solo con el ejemplo y
     se declara así.
  5. **Los candados,** como los recomienda el diseño: el de E3, entero al importar `prompt_e3.py` (opción
     i); las dos fixtures nuevas, `e1_extractor/candado_mensaje_r2b.json` y
     `e3_verificador/candado_mensaje_e3.json`, con su chunk y su validación sintéticos; y la regeneración
     de `data/experiment/mantenimiento/selftest_clave_cache.json`.
  6. **El tercer escalón del reintento de E1:**
     - techo de 40.960 tokens;
     - el reintento del ratchet de esas unidades, con el mismo techo;
     - la fila F08d de la tabla de reprocesamiento y la variación R13c del selftest de claves, autorizadas;
     - una llamada real de confirmación, con tope de USD 0,20;
     - la actualización de `reextraccion_v2/selftest_ub53.py`;
     - las unidades que usen el escalón no van a la muestra de la cola humana, que sería una obligación
       nueva del protocolo: llevan una marca propia y U-REEXT-T0 las lee todas en T4. Con ese número se
       decide si hace falta algo para el escalado.
  7. **Antes de habilitar el tercer escalón,** P3c-2 verifica en la documentación oficial que el contexto
     del modelo de E3 admite un pedido de unos 50.000 tokens, y lo cita.
  Costo. La llamada de P3c-2 (tope USD 0,20) y P4b (tope USD 1,5) son las únicas llamadas a la API
  autorizadas fuera de P4. El texto firmado decía «Fuera de P4, ninguna llamada a la API» (`:12`).
  De la revisión, PENDIENTE de decisión de la autora:
  - **La regla 9.** El laudo de esquema congelado la aceptó «sin tocar más la regla» (R4,
    `data/experiment/esq/laudo_esquema_congelado.md:50-51`, `2593d4d`), y L-ESQ-R2 describe lo
    meta-normativo como «finalidad, vigencia, interpretación y alcance de una norma» (`4ef7650:687`). Los
    puntos 1 y 3 sacan el alcance y dejan de la vigencia solo la fecha: cambian una regla de un texto
    firmado.
  - **Las normas con sujeto.** En el crudo de P4, las normas (Obligacion, Restriccion y Potestad) con
    `aplica_a` son 129 de 143 con el prefijo sellado y 111 de 157 con el de P3b-2; con el punto e de P3c
    quedarían 96 de 157. El alcance del TO no está en ningún nodo del grafo.
- **04/10/2026 — decisiones de la autora sobre los dos pendientes de la nota anterior y sobre el «seguí» de
  P3c-2.** P3c-1 quedó en `438bbd5` y la nota anterior, en `6633dc7`.
  - **La regla 9** va por enmienda: `data/experiment/esq/enmienda7_L-ESQ-R2_regla9_meta_normativo_2026-10-04.md`,
    BORRADOR — PENDIENTE DE FIRMA. La autora la firma antes del commit de P3c-2; P3c-2 implementa mientras
    tanto.
  - **El punto e queda aprobado como está.** P4b cuenta, por brazo, las normas (Obligacion, Restriccion y
    Potestad) con relación de sujeto.
  - **Mejora condicionada, a medir después de U-REEXT-T0** (fuera de esta unidad): en un documento con
    alcance, una norma sin mención recibe `aplica_a` hacia el rol de alcance de su documento, como relación
    derivada y marcada como tal. Entra solo si supera el piso de precisión: 30 relaciones leídas, con el
    límite inferior de Wilson en 0,75 o más. Está registrada en `docs/plan_tesis.md:400` y en el borrador del
    mandato de U-REEXT-T0.
  - **P4b,** además: uno de los cuatro casos del grupo a es un régimen de transición con condiciones, elegido
    por lectura; y su base de caché, como la de P4, no se reutiliza en U-REEXT-T0.
  - **Autorizaciones confirmadas por la autora:** el gasto de API de P4b (tope USD 1,5) y de la llamada real
    del tercer escalón (tope USD 0,20), los archivos de código de la nota anterior, y la fila F08d con la
    variación R13c.
  El «seguí» de P3c-2 está preparado, con estas decisiones; su despacho está PENDIENTE.
- **04/10/2026 — FRENO P3c-2 revisado; correcciones, enmienda 7 FIRMADA y «seguí» de P4b (decisiones de la
  autora).** La nota anterior quedó en `1873962`. El freno está en `data/experiment/prompt_r2/freno_p3c2.md`
  (sin commit al 04/10/2026). Corrí sus controles sobre una copia: los cinco scripts de USD 0 dan las salidas
  de `p3c2/salida/`, las dos fixtures y `selftest_clave_cache.json` salen iguales a los del repo, y los
  selftests dan lo que dice el freno (51, 80, 392, 101, 41, 52 y 109 casos, sin fallos; el del manifiesto,
  44 de 49, como corresponde sobre una copia). La cadena r2a con el código nuevo da los ocho sha256 de C2,
  con `70d51e42…` y `fa4c1043…`. El prefijo implementado es el borrador aprobado, byte a byte: 59.909
  caracteres, hash `322c5a23e9b7`.
  - **Enmienda 7 a L-ESQ-R2, FIRMADA por la autora el 04/10/2026** (commit de la firma PENDIENTE): el texto
    implementado coincide con su §1. «Régimen de transición con condiciones» no aparece con esas palabras y
    lo cubre la prueba de P3C-a3; quedó dicho en la nota de la verificación de la enmienda.
  - **El contador de omisiones `meta_normativo`** pasa a las siete clases de la enmienda 7: deber,
    prohibición, facultad, condición, excepción, alcance y modalidad. Con las cuatro de hoy detecta 5 de las
    9 normativas de P4; las otras 4 son de alcance o de modalidad. Sigue contando sin rechazar. La unidad
    declara la lista de marcas, suma casos al selftest y re-valida la salida guardada de P4.
  - **Tabla de reprocesamiento:** autorizado el texto del §10 del freno, en tres lugares fuera de las filas ya
    autorizadas: el §1 («Sin candado»), la nota de F22, F22b y F23, y la lista «Solo r2b», con F08d.
  - **Desvío aceptado:** la llamada real del tercer escalón transmitió con 24.576 tokens de techo y no con
    40.960, porque con 40.960 el peor caso proyectado pasaba el tope de USD 0,20. Como 24.576 supera el
    límite sin transmisión, el despacho y la transmisión son los del escalón. El techo completo lo ejercita
    `selftest_ub53.py` con un SDK falso. La llamada costó USD 0,042 y no se repite.
  - **P4b** va con lo ya decidido, más el contador de `meta_normativo` por brazo y la condición 10 de la
    tanda 1 decidida con el resultado del ejemplo. Se despacha después del commit de P3c-2.
  El mensaje de correcciones y el «seguí» de P4b están preparados; sus despachos están PENDIENTES.
