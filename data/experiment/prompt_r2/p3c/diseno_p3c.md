# U-PROMPT-R2 — diseño de la etapa P3c (FRENO P3c-1)

04/10/2026. HEAD `2a857db` al empezar y `bd77541` al cerrar: durante la etapa la autora commiteó P4 (`2ed47a0`, con
la revisión a a d de la lectura) y sus decisiones (`bd77541`, con la nota de la etapa P3c al mandato). USD 0: ninguna
llamada a la API. Sin commit. Nada congelado ni implementado: P3c-2 espera el «seguí» de este freno.

## 0. Fuentes

- **La etapa:** nota del 04/10/2026 al pie del mandato, «FRENO P4 revisado; etapas nuevas P3c y P4b»
  (`docs/mandatos/UPROMPT_R2_prefijo_nuevo.md:695-747`, commiteada en `bd77541`). Coincide con el pedido
  de la autora: cinco puntos de texto (a a e, que la nota numera 1 a 5) y tres agregados (f, g y h).
- **Agregado de la autora a P3c-1 (04/10/2026, de la revisión del FRENO P4),** en una nota al pie del mandato que
  está en el árbol sin commit al cerrar (`docs/mandatos/UPROMPT_R2_prefijo_nuevo.md:748-775`):
  - el encabezado puro de una lista con un deber o una condición (§1);
  - cuatro casos de control (§1);
  - el criterio de `cap::5.4.4` en los dos brazos de la lectura de P4 (aplicado en `p4/lectura_p4.md`);
  - el tercer escalón del reintento por corte (§5b).
- **Lo que motiva cada punto:** la lectura de P4 revisada por la autora (`p4/lectura_p4.md`, sección «Revisión de
  la autora») y el crudo de P4 (`p4/salida/resultados_p4.jsonl`). Las cifras de P4 que usa este diseño salen de
  `p3c/insumos_p4_p3c.py` (`salida/insumos_p4_p3c.json`).
- **La base del parche:** el prefijo de P3b-2, `3817de475c93` (sha `8d84364f…`, 55.105 caracteres; `c8c3970`).
- **h:** los hallazgos de U-TABLA-REPROC sobre las filas F04b, F22, F22b y F23
  (`data/experiment/mantenimiento/tabla_reprocesamiento.md`, `2a857db`, §1 y §3).
- **La E0 de los conteos:** la de C2, que lee U-REEXT-T0 (`e0_chunking/salida_tanda0_r2b`, `9f6361e`, 2.439
  unidades).
- **Corridas:** sobre una copia sin enlaces del repo, en el scratchpad (regla l). Las salidas están copiadas en
  `p3c/salida/`.

## 1. El parche del prefijo (a a e)

Son 15 reemplazos con ancla única sobre el prefijo congelado, como en P3b-1 (`p3c/borrador_parche_p3c.py`).
- **Archivos:**
  - los reemplazos: `salida/reemplazos_p3c_borrador.json`;
  - el prefijo con el parche: `salida/prefijo_r2b_p3c_borrador.txt`;
  - lado a lado: `salida/lado_a_lado_p3c.md`.
- **Anclas y reversibilidad:** cada ancla aparece una vez, y deshaciendo los reemplazos en orden inverso vuelve el
  congelado byte a byte.

| | Congelado | Borrador |
|---|---|---|
| Caracteres | 55.105 | 59.909 (+4.804) |
| Hash canónico (system + tools) | `3817de475c93` | `322c5a23e9b7` |
| Tool schema | `0c391f2b…` | sin cambio |

| Reemplazo | Punto | Qué cambia |
|---|---|---|
| P3C-a1 | a | Regla 9: lo meta-normativo predica sobre el significado, no sobre la conducta ni sobre a quién o a qué se aplica (sale «el alcance jurídico») |
| P3C-a2 | a | Regla 9: de la vigencia queda solo la fecha de entrada en vigencia (sale «aplicabilidad temporal») |
| P3C-a3 | a | Regla 9: la prueba antes de registrar un `meta_normativo`: la lista de lo que nunca lo es, adónde va (el alcance de una clase es Definicion; el de una norma, parte de esa norma; si no hay tipo, `fuera_de_tipos`), la prueba entre finalidad y alcance, y la única excepción: lo que un encabezado de lista fija para cada ítem se extrae en el ítem y no se registra |
| P3C-a4 | a | OMISIONES: la categoría `meta_normativo` remite a la prueba |
| P3C-a5 | a | Definicion: lo que una clase abarca o deja afuera sí la define (antes la regla decía que delimitar alcance no definía) |
| P3C-a6 | a | Unidad del encabezado: el encabezado puro de una lista no se registra como omisión: no es `meta_normativo` ni `fuera_de_tipos`, porque su sujeto, su deber o modalidad, su cuantificador y su condición se extraen en cada ítem |
| P3C-b1 | b | COMPOSICIÓN: la rama de EXCEPCIONES se parte en los dos tipos: lo que queda afuera (Excepcion, con la contra-excepción como manda POLARIDAD) y las condiciones de una sola excepción (Condicion); en los dos, la descripción nombra la norma exceptuada y no hay `exceptua` si la norma está en otra unidad |
| P3C-b2 | b | Unidad del encabezado: con los ítems como condiciones de una excepción, extrae la norma y la excepción unidas; con los ítems como lo que queda afuera, lo que el encabezado dice de la clase, como Definicion |
| P3C-b3 | b | Regla 1: suma la excepción cuyas condiciones son los ítems |
| P3C-c1 | c | Condicion: una por supuesto, todas con `condicion_de` a la misma norma; label, descripción, tramo y umbrales del mismo supuesto |
| P3C-c2 | c | LABELS: el label nombra lo mismo que la descripción, el tramo y los umbrales |
| P3C-d1 | d | Excepcion, CONEXIÓN: sin relación hacia un `local_id` que no se emitió, y sin volver a emitir la norma para tener a dónde conectarla |
| P3C-d2 | d | COMPOSICIÓN: la norma del encabezado no se emite como entidad aparte en el ítem; en las listas de supuestos, condiciones o excepciones va nombrada en la descripción |
| P3C-e1 | e | SUJETOS: sin mención si ni la unidad ni el heredado nombran al sujeto; entonces no hay relación |
| P3C-e2 | e | SUJETOS: el colectivo del TO solo cuando el texto lo nombra, con la expresión copiada del texto |

### Lo que motiva cada punto, y quién decide

- **a.** En el brazo nuevo de P4 hay 24 omisiones `meta_normativo`, una por ficha (`salida/insumos_p4_p3c.json`,
  `meta_normativo`). De ellas, 9 son contenido normativo según la revisión de la autora: 8 de las 16 con el tramo en
  el texto propio, y la de `ext::13.4.8`, con el tramo en el heredado.
  - **Decide el modelo:** es lectura de la frase.
  - **El código** puede contar las omisiones `meta_normativo` cuyo tramo trae una marca de deber, de facultad, de
    condición o de excepción. Es una propuesta (punto 2 de §10): cuenta, no rechaza.
- **b.** En el estrato de listas de P4, el nuevo emitió la Excepcion compuesta en 4 de 8 ítems, con una `exceptua`
  en las 4: en 3 queda colgante y en `ext::13.4.4` va a la norma del encabezado, repetida en el ítem
  (`p4/lectura_p4.md`). En ninguno de los otros 4, la descripción nombra la norma exceptuada.
  - **Decide el modelo** cuál de los dos tipos es la lista, por lectura del encabezado y del ítem.
  - **El código** verifica los tramos y rechaza el `exceptua` colgante (`ref_colgante`), como hoy.
  - **La contra-excepción** (`cla::5.1.1.1`) sigue la regla POLARIDAD que ya estaba en el prefijo: la norma que
    vuelve a regir en el supuesto, con una Condicion por condición. Si lo que vuelve a regir es la pertenencia a la
    clase, el texto la manda a una Operacion, el acto de clasificar. Así `condicion_de` no apunta a una Definicion,
    que su firma no admite. En el crudo del brazo sellado de P4, `cla::5.1.1.1` tiene esa forma: dos Condicion hacia
    la Operacion de clasificar. El validador v3 las rechaza por la firma.
- **c.** En `cla::5.1.1.1`, la Condicion e2 del brazo nuevo tiene la etiqueta y el umbral del monto, y la
  descripción y el tramo del repago (revisión de la autora, b).
  - **Decide el modelo.** El código no compara etiqueta y descripción: no hay una regla mecánica fiable.
- **d.** El caso es `ext::13.4.4`: el nuevo repite la Restriccion del encabezado dentro del ítem y la exceptúa.
  - **Decide el modelo.**
  - **El código ya lo cuenta:** una entidad de un ítem con el tramo simple solo en el heredado va al contador
    `tramo_entidad.solo_heredado:heredado_compuesto` (`validador_r2.py:294-297`). Propongo usarlo como medida de d en
    P4b y en U-REEXT-T0.
- **e.** De las 15 menciones que no verifican en las 76 fichas del brazo nuevo, 14 son «las entidades»
  (`salida/insumos_p4_p3c.json`, `menciones_no_verificadas`).
  - **Decide el modelo.**
  - **El código ya marca** la mención que no verifica (`mencion_verificada`).

### El encabezado puro de una lista (agregado, punto 1)

**El caso.** «Las entidades financieras deben:» (`adrei::4.3.1::intro`) y «que reúnan concurrentemente las siguientes
condiciones:» (`polcre::7.1::intro`) tienen un deber o una condición. Con la regla estricta, eso no puede ser
`meta_normativo`. Tampoco se extrae en su unidad, porque se compone en cada ítem.

**Cómo queda escrito para que no choque.** Dos piezas:
- **La prueba de la regla 9 (P3C-a3)** termina con la única excepción a «extraelo con el tipo que le toca»: el deber,
  la modalidad, el cuantificador o la condición que un encabezado de lista fija para cada ítem se extraen en cada
  ítem, y en la unidad del encabezado no se extraen ni se registran como omisión.
- **La unidad del encabezado (P3C-a6)** dice lo mismo desde la composición: el encabezado puro no se registra como
  omisión, no es `meta_normativo` ni `fuera_de_tipos`, porque todo lo que fija para los ítems se extrae en ellos.

Así la lista de lo que nunca es `meta_normativo` queda entera y el encabezado no cae en ninguna categoría de omisión.
- **Si el encabezado dice además algo aparte de la lista,** eso se extrae en su unidad, como ya decía el prefijo.
  Ejemplo: `polcre::7.1::intro`, donde la categoría de clientes es una Definicion.
- **E3 ya está alineada:** la NOTA del encabezado de lista dice que la falta del anuncio y de lo que se compone en
  los ítems no es faltante.

### Los cuatro casos de control del agregado (punto 2)

Los cuatro están entre las 76 unidades de P4, así que ya son casos de control de la no-filtración (§6). Con el texto
nuevo:
- **`ayccef::2.4.8.1`**, ítem de una lista de contenidos (lo que se presenta de cada accionista e integrante de los
  órganos). El nuevo emitió la Obligacion compuesta, con el tramo del ítem solo, y además declaró el ítem entero
  como `meta_normativo`.
  - Con P3C-a3, la omisión no puede ser `meta_normativo`, porque es un deber compuesto.
  - La regla vigente prohíbe registrar como omisión lo que se extrajo.
  - Lo esperado: la Obligacion compuesta, con el tramo de dos segmentos (R30) y sin omisión.
- **`ayccef::4.2.7.2`** («Los sistemas informáticos.»), ítem de «Tener calificación 1, 2 o 3 de la SEFyC, en todos
  los siguientes aspectos:», en la línea de título de 4.2.7, sin unidad propia. El nuevo emitió una Definicion y
  declaró el ítem `meta_normativo`.
  - El ítem es un aspecto en que la calificación se exige, junto con los demás: una condición.
  - Con P3C-a3 no puede ser `meta_normativo`, y con la composición es la Condicion compuesta, «calificación 1, 2 o 3
    en los sistemas informáticos», con su cuantificador (todos).
  - Ya lo marcaba así la lectura de P4 (F1).
- **`cap::3.1.14::intro`** (dudoso). La frase «A los fines de establecer el ponderador de riesgo a aplicar de acuerdo
  con el enfoque estandarizado» acota para qué se usa la definición STC.
  - Por la prueba entre finalidad y alcance de P3C-a3: sin la frase, la definición valdría para cualquier fin, así
    que es alcance.
  - Va en la descripción de la Definicion, que hoy no la tiene, y no es `meta_normativo`.
- **`ric::3.1.8`** (dudoso). «Para el cómputo de la exigencia adicional establecida en el punto 11.5.» de Capitales
  mínimos dice a qué cálculo se aplica la metodología que sigue.
  - Por la misma prueba, es alcance de las dos Obligacion de la metodología (a y b): sin la frase, la metodología no
    quedaría atada a esa exigencia.
  - Va en sus descripciones. La remisión al 11.5 la registra el código.
- **Mi lectura de los dos dudosos** es alcance; la decide la autora. Si la autora prefiere tratar las frases «a los
  fines de» y «para el cómputo de» como finalidad, la prueba se retira de P3C-a3 y los dos quedan como
  `meta_normativo`.

## 2. El mensaje de E1 (e) y las NOTAS de E3 (a y b)

`p3c/mensaje_p3c_borrador.py`, sobre la E0 de C2. Lado a lado en `salida/mensaje_p3c_lado_a_lado.md`; conteos en
`salida/mensaje_p3c.json`.

- **e, la línea «Alcance de este TO».** Hoy dice que, cuando la norma se dirija «genéricamente» al colectivo, se
  sugiera el rol, «con la expresión del texto». El borrador pide la expresión copiada del texto, y si el texto no
  nombra a ningún sujeto, que no haya relación: el alcance no reemplaza la mención.
  - Cambia el mensaje de 2.408 de las 2.439 unidades. Las 31 de docvig no tienen línea de alcance.
  - La línea crece 148 caracteres.
- **a, la NOTA de E3 de las omisiones de esquema** (`prompt_e3.NOTA_E3_OMISIONES`). Hoy describe `meta_normativo`
  como contenido «sobre el sentido, el alcance, el objetivo o la vigencia» de una norma. Con la regla 9 nueva, el
  alcance sale. La lista de lo que es faltante si se declara como meta-normativo pasa de «un deber o una
  prohibición» a la lista completa del punto a.
  - Va donde la extracción declare esas categorías: depende de la salida de E1.
- **b, la NOTA de E3 del encabezado de lista.** Su última oración suma, entre lo que el encabezado enuncia aparte de
  la lista y es faltante si no se extrajo, «la norma y su excepción cuando los ítems son las condiciones de esa
  excepción».
  - La llevan 212 unidades de la tanda 0.
- **Clase de reprocesamiento:**
  - la línea de alcance es F22b, por las unidades que la llevan (todas menos docvig);
  - las dos NOTAS son F23.
  - Con el prefijo nuevo, todas las claves de E1 cambian igual (F06).

## 3. f: `cap::tabla037` a residual

Un alta en `e1_extractor/tablas_residuales_forzadas_r2b.json`, con la tabla, el motivo y la fecha. Queda como en
`salida/tablas_residuales_forzadas_r2b_p3c.json`.
- **La trae una sola unidad,** `cap::6.2.2.6`, en la e0-r2 de `f8dedd4` y en la de C2.
- **Cambia** su bloque de tablas en el mensaje de E1: deja de ser tabla confiable y pasa a «no copies sus valores;
  registrá la omisión `tabla`».
- **Cambia** su NOTA de E3: la de siempre de los flags, en lugar de la de tablas confiables.
- **Clase:** F04b, E1 y E3 de esa unidad.

## 4. g: el tramo de las omisiones contra el texto propio y el heredado

**Hoy.** `validador_r2` verifica el tramo de la omisión solo contra el texto propio (`validador_r2.py:1316`). El de
la entidad, en cambio, contra el propio y el heredado, y en un mini-chunk a mitad de oración también en el orden de
lectura (`:272-298`).

**Propuesta.** El tramo de la omisión se verifica como el tramo simple de la entidad:
- primero contra el texto propio;
- si no verifica ahí, contra el texto completo;
- en un mini-chunk a mitad de oración, también en el orden de lectura.

El nivel conserva sus cuatro valores (`exacta`, `tokens`, `no` y `ausente`), así que `modelos_r2.py` no cambia. Lo
que verifica solo en el heredado va a un contador nuevo, `omisiones.tramo_solo_heredado`. El prefijo sigue pidiendo
el tramo del texto propio, y el contador hace visible la omisión que declara contenido de otra unidad.

**En P4** (`salida/insumos_p4_p3c.json`, `omisiones_verificacion_del_tramo`), sobre las 70 omisiones con tramo del
brazo nuevo:

| | Verifican | No verifican |
|---|---|---|
| Hoy (solo texto propio) | 48 | 22 |
| Con g | 56 (48 propio + 7 heredado + 1 orden de lectura) | 14 |

- **Las 14 que siguen sin verificar** son resúmenes de tablas y fórmulas, no copias.
- **No toca E3:** `validador_e1.proyectar_r2` pasa a E3 el tramo crudo, sin su nivel.
- **Clase:** F14b, solo código sobre lo guardado.
- **Selftest:** casos nuevos en `selftest_pyd_r2.py`: una omisión del heredado, una en el orden de lectura y una del
  propio, que conserva su nivel.

## 5. h: los candados de F04b, F22, F22b y F23

**Qué tienen en común.** Ninguno de los cuatro insumos entra al hash del prefijo ni al namespace: un cambio mueve
claves sin que nada frene (U-TABLA-REPROC, §1). Los candados solo comparan: no entran al pedido ni cambian ninguna
clave ni la salida de los perfiles existentes. Se sellan en P3c-2, después del ajuste del texto.

**F04b, la lista de tablas forzadas.** `prompt_r2b._cargar_tablas_forzadas` la lee con `_leer_con_candado` y un
`TABLAS_FORZADAS_SHA256_ESPERADO`, sellado con el alta de f. Hoy solo exige tabla, motivo y fecha (`:143-151`).

**F22 y F22b, las líneas del mensaje de E1.**
- **Qué cubre:** el sha256 del mensaje de un conjunto fijo de unidades que ejercita cada rama de
  `build_user_message_r2b` y de `bloque_flags`, con la lista de tablas forzadas de f.
- **Cuándo:** al importar `prompt_r2b.py`, al final del módulo.
- **El conjunto:** 12 unidades cubren las 29 ramas presentes en la tanda 0 (`p3c/candados_p3c.py`,
  `salida/candados_p3c.json`, por cobertura voraz y reproducible).
  - Las ramas: rótulos de la herencia, ítem con y sin cierres, mini-chunk a mitad de oración y normal, recorte,
    alcance y sin alcance, y cada variante de tablas y FLAGS E0.
  - Las unidades: `ric::11.1.1`, `ric::11.2::intro`, `ext::7.1.1.3`, `cap::5.3.2.3`, `docvig::S4`, `cap::1.4.1`,
    `cap::2.12.10::intro`, `cap::3.2.4`, `cap::4.2.1.2`, `cap::6.2.2.6`, `ric::11.2.3` y `ric::5.1.3.2`.
- **La fixture:** los 12 chunks se copian a un archivo fijo, junto a `prompt_r2b.py`, para que el candado no
  dependa de una E0 que puede cambiar (U-SEG-OFICIAL).
- **Refactor:** las líneas fijas que hoy están escritas dentro de la función (los rótulos de la herencia y el
  cierre, `:342-388`) pasan a constantes del módulo, sin cambiar un byte del mensaje, para que el selftest pueda
  variarlas.
- **Una rama no la ejercita ninguna unidad de la tanda 0:** la del alcance por clase sin `rol_id` (`linea_alcance`,
  `:334-336`). De las 71 entradas de `rol_por_to_r2.json`, 70 traen `rol_id`; la que no lo trae es `ri2_ci.pdf`,
  con dos clases, que no está en la tanda 0. Propongo sumar a la fixture una copia de un chunk de la tanda 0 con
  `archivo` = `ri2_ci.pdf`, marcada como sintética, para que el candado cubra esa rama.

**F23, las NOTAS de E3.**
- **Qué cubre:** el sha256 del mensaje de E3 de un conjunto fijo, con la marca r2 (las NOTAS de `notas_r2`) y sin
  ella (la NOTA de siempre).
- **Dónde:** al final de `prompt_e3.py`, junto al candado del prefijo (`:378-386`).
- **El conjunto:** 6 unidades cubren las 15 ramas: `ric::11.2::intro`, `cap::5.3.2.3`, `cap::2.13`,
  `cap::3.1.11.2`, `cap::1.4::intro` y `cap::3.2.4`.
- **La NOTA de las omisiones depende de la salida de E1,** así que se ejercita con una validación sintética mínima
  (una omisión `meta_normativo`, declarada en `candados_p3c.py`).
- **Acoplamiento a decidir:** `notas_r2` importa `prompt_r2b`. Hay dos maneras:
  - **(i)** el candado corre al importar `prompt_e3`, entero, y entonces el perfil sellado también importa
    `prompt_r2b` y sus candados, que solo comparan;
  - **(ii)** al importar corre la parte sin la marca r2, y la parte r2 corre una vez, en el primer mensaje r2.
  - Recomiendo (i), que es lo que pidió la autora («al final de `prompt_e3.py`»). El costo es ese acoplamiento,
    que declaro.

**El selftest de claves** (`mantenimiento/code/selftest_clave_cache.py`).
- **R32** (alta en la lista) ya corre en un proceso hijo con el JSON redirigido: con el candado, la importación
  frena, y pasa de «cambia» a «frena» como R21 y R22.
- **R29, R29b y R30** hoy varían una constante en memoria, después de importar. Para que frenen, pasan a procesos
  hijos que editan el literal en una copia del módulo antes de importarlo.
  - R29 edita la línea del ítem; R29b, la línea de cierre; R30, la NOTA de las omisiones.
  - Así se prueba lo que el candado protege: que alguien edite el archivo.
- **La tabla:** las filas F04b, F22, F22b y F23 pasan a «frena; re-sellado, la clase de la fila», con el ancla del
  candado. Se regenera `selftest_clave_cache.json`.

## 5b. El tercer escalón del reintento por corte (agregado, punto 4)

**Hoy, con el perfil r2** (`runner_corpus.py:526-629`):
- el primer intento es a 8.192 tokens y, si corta, hay un reintento a 16.384 (`cliente_e1.crear_con_reintento_corte`,
  `:324-348`);
- si el reintento también corta, la unidad se parte por ítems (`correr_e0.particionar_por_corte`) y las partes se
  extraen en el mismo pase.
- **Dos casos quedan como error definitivo:**
  - una unidad que no se puede partir (sin ítems, o con una tabla que quedaría partida);
  - una parte que corta.

El techo de 16.384 viene de la guarda del SDK: sin transmisión, el SDK rechaza el pedido cuyo `max_tokens` estima más
de 10 minutos (anthropic 0.100.0, `_base_client.py:731-740`: 3.600 s × `max_tokens` / 128.000). Eso deja
21.333 tokens como máximo sin transmitir.

**El diseño.** Solo con el perfil r2, y solo en esos dos casos.
- **El adaptador** (`cliente_e1.py`): una clase con la interfaz `messages.create(**kwargs)` que por dentro llama
  `messages.stream(**kwargs)` del cliente real y devuelve `get_final_message()`.
  - Normaliza el mensaje final a `anthropic.types.Message`. El SDK devuelve un `ParsedMessage`, subclase de
    `Message` (`types/parsed_message.py:45`); normalizarlo deja el crudo que guarda la caché con la forma del de
    `create`.
  - Pasa un `timeout` explícito al stream. Es una opción del pedido, no entra en la clave.
- **El cliente** (`ClienteE1Real`): con la opción de transmisión, que el runner activa solo con el perfil r2, abre un
  segundo `CachingClient` sobre el adaptador.
  - Usa la misma base y el mismo namespace de E1. `llm_cache.py` es del cuarteto sellado y no se toca: el adaptador
    queda debajo de él.
  - `create` despacha por ese cliente todo pedido cuyo `max_tokens` pase de 21.333; el resto, como hoy.
  - El chequeo de tope proyecta esa llamada con su techo, no con 8.192.
  - Su `usage` va al log con un componente propio (decisión 3 de caching).
- **El disparo** (`crear_con_reintento_corte`) recibe un parámetro nuevo, opcional, que solo pasa el runner r2: una
  función que dice si corresponde el tercer escalón. Corresponde si la unidad es una parte, o si
  `particionar_por_corte` no la parte.
  - Si el reintento de 16.384 corta y corresponde, hace una tercera llamada: el mismo pedido con `max_tokens` = 40.960.
  - Con el parámetro, devuelve los intentos cortados (uno o dos) para que el runner los persista. Sin él, el par de
    siempre: los perfiles existentes no cambian. Los otros cinco scripts que la llaman (los dos runners de fase B,
    la dirigida de la tanda 0, `cobertura_bloque_a/code/correr_a2.py` y `p4/correr_p4.py`) no pasan el parámetro.
- **El runner** (`runner_corpus.py`, solo r2):
  - registra el escalón en la unidad (`escalon_3`, con el resumen de los dos intentos cortados);
  - si el tercer intento también corta, deja el error definitivo nuevo `max_tokens_hit_tras_escalon_3`;
  - suma al resumen de E1 la lista de unidades que usaron el escalón.
- **El ratchet:** para esas unidades, el runner le pasa como techo del reintento el mismo 40.960, y el cliente del
  ratchet, también con la transmisión activa, lo despacha por el adaptador. `ratchet_e3.py` no cambia, porque llama
  `cliente.create(**kwargs)`. Sin esto, el reintento del ratchet de esas unidades cortaría a 16.384 y la unidad iría a
  la cola humana.

**El techo: 40.960 tokens.**
- Cubre el rango de 20.000 a 40.000 tokens del agregado, por debajo del máximo de salida de `claude-haiku-4-5`,
  64.000 tokens (nota del agregado al mandato, `:770-771`, que cita la documentación de modelos de la API).
- Con la razón más alta medida en P4 (1,498 tokens por carácter de texto propio), la salida más larga proyectada que
  llega al escalón en la tanda 0 es de 22.554 tokens (`cap::4.2.1.2::parte1`). El techo le deja un margen de 1,8.
- Ninguna salida proyectada lo pasa con ninguna de las tres razones (`salida/escalon3_p3c.json`).
- El costo de una llamada que llegue al techo es de USD 0,20 de salida.

**Qué llega al escalón en la tanda 0** (`p3c/escalon3_p3c.py`; la salida, como tokens por carácter por la razón de
cada fila):

| Razón | Casos | Salida máxima proyectada | Costo incremental: llamada y E3 | Con un reintento del ratchet al techo en cada caso |
|---|---|---|---|---|
| 0,86 (sellada, mediana) | 0 | — | USD 0 | USD 0 |
| 1,175 (nuevo, mediana de P4) | 2: `ric::11.2::intro` (no se parte) y `cap::4.2.1.2::parte1` | 17.691 | USD 0,36 | USD 0,79 |
| 1,498 (nuevo, máximo de P4) | 5: más `cap::3.1.14.1` y `cap::4.3.3.1` (no se parten) y `cap::4.2.1.2::parte2` | 22.554 | USD 0,97 | USD 2,03 |

- **Qué no cuenta el costo:** los dos intentos cortados (8.192 y 16.384) ya los paga el pipeline de hoy.
- **Las razones son medianas o máximos de 6 unidades:** con el prefijo sellado, la unidad más grande quedó muy por
  debajo de la mediana (`cap::4.2.1.2`, unos 0,46).
- **El tope de U-REEXT-T0** (USD 72) absorbe el peor caso.
- **Fuera de la tanda 0 el escalón pesa más.** El censo de U-SEG-OFICIAL (`docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md:75-84`,
  `bd77541`) cuenta, con la razón de 1,498, 14 unidades que no se pueden partir y pasan de 13.944 caracteres (clase
  A) y 15 cuya parte mayor pasa de ese tamaño (clase B).
  - Con 40.960 tokens, el escalón alcanza unos 34.860 caracteres de texto propio con la mediana de P4 y 27.343 con
    el máximo: las de las clases A y B que no pasen de ahí se recuperan, y las demás siguen con error declarado.
  - El techo puede subir hasta el máximo del modelo si el censo de ids de U-SEG-OFICIAL lo pide.
- **Sin transmisión,** el SDK acepta el pedido largo si la llamada trae un `timeout` explícito
  (`resources/messages/messages.py:984-987`). No lo propongo: la autora pidió transmisión, y una conexión que espera
  minutos sin recibir datos es más frágil que un flujo que los recibe de a partes.

**Su fila en la tabla de reprocesamiento** (propuesta; es una fila nueva, F08d):

| Fila | Cambio | Dónde entra | Qué obliga a recomputar | Clave E1 | Clave E3 | Clase | Principio | Variación |
|---|---|---|---|---|---|---|---|---|
| F08d | Tercer escalón del reintento por corte (perfil r2): transmisión por partes con techo 40.960, solo si el reintento de 16.384 corta y la unidad no se parte, o si corta una parte; y el reintento del ratchet de esas unidades al mismo techo | request del tercer intento y del reintento del ratchet, solo en esas unidades; mismo namespace | E1 de esas unidades y su E3 | cambia (solo esos requests) | no cambia (con la salida de E1 fija) | E1 y E3 de las afectadas | 9 | R13c, nueva: el techo del tercer escalón |

- **F08b** (techos del reintento) queda como está para el resto de las unidades.
- **La fila y R13c no están entre las escrituras autorizadas** de `data/experiment/mantenimiento/` (solo F04b, F22,
  F22b y F23, y R29 a R32): la autora decide si entran en P3c-2.

**Cómo se verifica con E3 una salida de 20.000 a 40.000 tokens.**
- **Entra.** E3 recibe el texto propio de la unidad y la extracción validada, renderizada (`comun_e3.py:111-192`),
  sin el JSON crudo. Con 40.000 tokens de salida de E1 y la unidad más larga de la tanda 0 (26.726 caracteres), el
  mensaje queda por debajo de unos 50.000 tokens, más el prefijo de E3 (en caché). Que entre en la ventana de contexto de `claude-sonnet-5` está NO
  VERIFICADO en el repo; lo confirma la llamada de P3c-2.
- **La salida de E3** es el veredicto, con techo de 4.096 tokens (`prompt_e3.py:37`). Está por debajo de la guarda
  del SDK, así que no necesita transmisión. Si corta, el veredicto no se lee y la unidad va a la cola humana
  marcada, como hoy.
- **Costo:** por unidad, unos USD 0,08 a 0,10 de E3 (`salida/escalon3_p3c.json`, `e3_usd`).
- **Lo que E3 no garantiza es la calidad** del veredicto sobre una lista tan larga: nunca se midió. Propongo que todas
  las unidades que usen el escalón entren a la muestra de la cola humana de la tanda, marcadas como tales. Son pocas:
  hasta 5 en la tanda 0 por la proyección. El ensamblado no cambia: la marca va en el registro de E1 y en su resumen.
- **No propongo partir el veredicto de E3:** cambiaría el mensaje de E3 de esas unidades y su clave, y no está
  autorizado.

**La confirmación en P3c-2: una llamada real de centavos.** Una unidad corta, ya leída (`cla::5.1.1::intro`), por el
adaptador con `max_tokens` = 40.960, en una base de caché propia de P3c-2.
- **Controla que** el mensaje final traiga el `tool_use`, el `usage` y el `stop_reason`, y que el crudo guardado
  tenga las mismas claves que el de una llamada sin transmisión de P4.
- **Repite** la misma llamada: tiene que salir de la caché, sin API.
- **Fuerza un corte:** la misma unidad con un `max_tokens` muy bajo, por el adaptador, para ver el `stop_reason`
  «max_tokens» en la transmisión.
- **Costo:** unos USD 0,05 (la escritura del prefijo y dos salidas cortas). Propongo un tope de USD 0,20.

## 6. No-filtración

`p3c/nofiltracion_p3c.py`: la regla de P1 y P3b-1, sin editar esos scripts.

- **Población:** 7.815 chunks: la E0 legada, la e0-r2 de `f8dedd4` y la de C2 de los diez TOs, y los cuatro TOs
  fuera de muestra.
- **Casos de control:** 93: los de P3b-1 y las 76 unidades de P4.
- **Base de comparación:** el prefijo congelado y la línea de alcance de hoy.
  - Las ventanas que ya estaban en la línea vieja no cuentan como agregadas. Es una diferencia con P3b-1, que solo
    comparaba contra el prefijo.

| Texto agregado | Ventanas de 5 palabras nuevas | Choques con un chunk | Bigramas o trigramas de control |
|---|---|---|---|
| Prefijo | 970 | 0 | 0 |
| Literales (línea de alcance y NOTAS de E3) | 192 | 0 | 0 |

`salida/nofiltracion_p3c.json`.

## 7. Costo

**De P3c-2:** USD 0.

**Sobre U-REEXT-T0, sin la salida** (`salida/proyeccion_p4b_p3c.json`, `u_reext_t0`):
- **El prefijo:** 26.309 tokens medidos en P4 pasan a unos 28.603 (+2.294), con los tokens por carácter de P4.
  - Lecturas de caché: +USD 0,56.
  - Escrituras: +USD 0,01.
- **La línea de alcance:** +USD 0,11.
- **Total sin la salida:** +USD 0,68.
- **El tercer escalón** (§5b): +USD 0,36 con la mediana de P4 y +0,97 con el máximo, sin reintentos del ratchet;
  0,79 y 2,03 con un reintento al techo en cada caso.
- **El efecto sobre la salida** de E1, y con ella sobre E3, no lo proyecto: lo mide P4b. Con la regla a pueden
  bajar las omisiones; con b y c, subir las Condicion. El borrador de U-REEXT-T0 ya prevé proyectar T1 con la salida
  de P4b.

## 8. P4b: la prueba corta

**Brazos.** Los dos prefijos, el vigente (`3817de475c93`) y el de P3c, con la misma e0-r2 (la de C2), sobre las mismas
unidades. Comparar contra el vigente separa el efecto del ajuste del de la muestra: las unidades son nuevas y P4 no
las corrió.

**Cómo se eligen los casos.** La elección es el primer paso de P4b, después de que P3c-2 congele el texto, para no
leer al escribir el ajuste ningún caso de la prueba.
- **Excluidas:** las 76 unidades de P4, los casos de control de P1 y P3b-1, las listas que P4 leyó (las cinco del
  estrato y las cinco descartadas) y las unidades que nombran este diseño y la lectura de P4.
- **Pool:** por grupo, definido en palabras. La elección es por lectura, con semilla, y la lista se sella (sha256 y
  hora) antes de correr, como el estrato de listas de P4.

| Grupo | Qué mide | Unidades | Población de donde se eligen |
|---|---|---|---|
| a | Ninguna omisión `meta_normativo` con deber, prohibición, facultad, condición, excepción, alcance o modalidad; ese contenido, extraído con su tipo | 4 | unidades con una cláusula de alcance, de modalidad o de anuncio con norma |
| b1 | Lo que queda afuera: Excepcion; descripción con la norma exceptuada; contra-excepción con una Condicion por condición; sin `exceptua` colgante | 3 ítems | listas cuyo encabezado anuncia los miembros excluidos de una clase |
| b2 | Las condiciones de una sola excepción: Condicion con su cuantificador; descripción con la norma exceptuada | 3 ítems | listas cuyo encabezado enuncia una salvedad y sus supuestos |
| b, encabezados | La unidad del encabezado: Definicion de la clase (b1); norma y excepción unidas (b2) | 4 | los encabezados de las listas de b1 y b2 |
| c | Una Condicion por supuesto, con label, descripción, tramo y umbral coherentes | 4 | normas con dos o más supuestos, uno con cuantía |
| d | La norma del encabezado no se repite en el ítem (contador `solo_heredado:heredado_compuesto`) | 4 | ítems de listas cuyo encabezado tiene unidad propia y enuncia una norma |
| e | Sin relación de sujeto cuando el texto no lo nombra; menciones que verifican | 4 | unidades de TOs con alcance cuyo texto propio y heredado no nombra al sujeto |
| Ejemplo | `cla::5.1.1::intro`: Definicion de alcance; `cla::5.1.1.1`: Excepcion, Operacion de clasificar y dos Condicion | 2 | fijos |
| f | `cap::6.2.2.6`: ningún valor de `cap::tabla037` copiado; omisión `tabla` declarada | 1 | fijo |

**El tipo b1 puede ser escaso.** Lo conté por forma léxica, sin leer
(`salida/proyeccion_p4b_p3c.json`, `pool_listas_b`):
- **En la tanda 0:** de los 210 contenedores de lista no leídos, 0 tienen la forma léxica de b1 y 10 alguna forma
  de excepción.
- **En la partición:** de 637 contenedores, 0 tienen la forma de b1 y 19 alguna forma de excepción, en 15 TOs.

Si la lectura no encuentra dos listas de b1 fuera de `cla::5.1.1`, b1 toma las que haya, incluidas las de la
partición, con su e0-r2 como el estrato fuera de muestra de P4, y lo declara. Es decisión de la autora (§10,
punto 4).

**Pata de E3.** Sobre 6 unidades del brazo P3c, para ver las NOTAS nuevas: los encabezados de b y dos de a.

**g y h, a USD 0.**
- **g:** re-validar la salida guardada de P4 con el validador nuevo; lo esperado es 56 de 70.
- **h:** los selftests, con R29, R29b, R30 y R32 en «frena» y los candados reproducidos.

**Salida.** Por brazo, los tokens de salida por unidad y por carácter de texto propio: alimentan la proyección de T1
de U-REEXT-T0.

**Costo** (`salida/proyeccion_p4b_p3c.json`, `p4b`). Son 29 unidades, 58 llamadas de E1 y 6 de E3, con las tarifas
de P4.
- Central: USD 0,83.
- Alto (salida y E3 por 1,5): USD 1,09.
- Propongo un tope de USD 1,5.

## 9. Lo que P3c-2 escribe

| Archivo | Para qué | Autorización |
|---|---|---|
| `e1_extractor/prompt_r2b.py` | parche de P3c sobre `3817de475c93` con su candado; línea de alcance; refactor de las líneas fijas; candado del mensaje (F22, F22b); lista forzada con sha (F04b) | escrituras de la unidad |
| `e1_extractor/prompt_r2b_parche_p3c.json` (nuevo) | los 15 reemplazos, con su sha | como el parche de P3b |
| `e1_extractor/tablas_residuales_forzadas_r2b.json` | el alta de f | punto f |
| `e1_extractor/candado_mensaje_r2b.json` (nuevo) | los 12 chunks de la fixture de F22 y F22b | **a autorizar** |
| `e1_extractor/perfil_e1.py`, `selftest_prompt_r2b.py`, `reextraccion_v2/selftest_manifiesto.py` | el hash nuevo del prefijo | como en P3b-2 |
| `e3_verificador/prompt_e3.py` | las NOTAS de a y b; el candado de F23 | punto h (más allá de la NOTA) |
| `e3_verificador/candado_mensaje_e3.json` (nuevo) | los 6 chunks y la validación sintética de F23 | **a autorizar** |
| `e3_verificador/selftest_e3.py` | casos de las NOTAS nuevas y del candado | escrituras de la unidad |
| `pyd_r2/code/validador_r2.py`, `selftest_pyd_r2.py` | g | escrituras de la unidad |
| `mantenimiento/tabla_reprocesamiento.md` (cuatro filas) y `code/selftest_clave_cache.py` (cuatro variaciones) | h | punto h |
| `mantenimiento/selftest_clave_cache.json` | la salida del selftest, regenerada | **a confirmar**: sale de las variaciones autorizadas |
| `e1_extractor/cliente_e1.py` | el tercer escalón: adaptador de transmisión, techo 40.960, despacho y proyección del tope | agregado, punto 4 |
| `corpus_v2/runner_corpus.py` | el disparo del tercer escalón y el techo del ratchet de esas unidades, solo r2 | agregado, punto 4 |
| `reextraccion_v2/selftest_ub53.py` (el que ejercita `crear_con_reintento_corte`) | el escalón con un cliente stub (corta, corta, no corta; parte que corta; sin el parámetro, el par de siempre) | **a confirmar**: es el selftest de la función autorizada |
| `mantenimiento/tabla_reprocesamiento.md` (fila F08d) y `code/selftest_clave_cache.py` (R13c) | la fila del tercer escalón | **a autorizar** |
| `data/experiment/prompt_r2/p3c2/` y `freno_p3c2.md` | scripts de control, la llamada real de centavos y el freno | escrituras de la unidad; la llamada con el tope que fije la autora |

**Rige solo con la forma r2.** Los cinco ensamblados sellados y los perfiles existentes, byte a byte. P3c-2 no corre
a la vez que otra unidad que edite `prompt_r2b.py`, `prompt_e3.py`, `validador_r2.py`, `cliente_e1.py` o
`runner_corpus.py`.

## 10. Para decidir

1. **El texto:** los 15 reemplazos, la línea de alcance y las dos NOTAS de E3, con la lectura de los dos dudosos
   (`cap::3.1.14::intro` y `ric::3.1.8`) como alcance.
2. **El contador de `meta_normativo` con marca** de deber, facultad, condición o excepción en el tramo (punto a): si
   va en `validador_r2` como F14b, contando sin rechazar.
3. **La vigencia (P3C-a2):** queda en `meta_normativo` solo la fecha de entrada en vigencia, y la «aplicabilidad
   temporal», que es un alcance, sale. Si la autora prefiere conservarla, el reemplazo se retira.
4. **P4b:**
   - los grupos y sus tamaños;
   - el tope de USD 1,5;
   - qué hacer si b1 no tiene dos listas en la tanda 0;
   - la pata de E3.
5. **h:**
   - el acoplamiento de E3, (i) o (ii);
   - las dos fixtures nuevas;
   - la regeneración de `selftest_clave_cache.json`.
6. **El tercer escalón:**
   - el techo de 40.960;
   - el techo del ratchet para esas unidades;
   - todas sus unidades a la muestra de la cola humana;
   - la fila F08d y R13c;
   - la llamada de centavos con tope de USD 0,20;
   - su selftest.
