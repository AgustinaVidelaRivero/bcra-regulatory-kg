# FRENO P5 de U-PROMPT-R2: la temperatura de E1

**La Excepcion de `cla::5.1.1.1` sale en las dos corridas con temperatura 0, con la Operacion de clasificar y una
Condicion por cada condición; `cla::5.1.1::intro` da la Definicion de alcance en las dos.**

05/10/2026. HEAD `fd81f2a`: la autora commiteó ahí la nota del mandato del 05/10/2026 («seguí» de P5 despachado) a
las 10:19, durante P5 y antes del sello y de la corrida (`git log`); el commit solo cambia tres documentos. La llamada
de control del punto 1 corrió desde una copia de `1297ff8`, el HEAD de ese momento. USD 0,9078 de un tope de 1,5. Sin
commit. El paquete de revisión está en el scratchpad de la sesión
(`revision_UPROMPT_R2_FRENO_P5/`, con `manifest.txt`).

## 0. Fuentes y diferencias

- Leí las notas fechadas del mandato (`docs/mandatos/UPROMPT_R2_prefijo_nuevo.md`) hasta la última, la del
  05/10/2026 que registra la decisión sobre E3 y el despacho del «seguí» (`:1050-1067`, en `fd81f2a`), y
  `docs/decisiones_caching_extraccion.md`.
- **El mensaje coincide con los archivos.** La nota anterior dejaba la temperatura de E3 PENDIENTE de decisión; la
  nota nueva y el mensaje la resuelven igual: E3 queda sin temperatura fijada, declarado como límite, y P5 mide la
  variación de sus veredictos.
- **Error propio, de P4b:** las cuatro listas de sha256 del repo del paquete de revisión de P4b llevan la ruta de un archivo de `docs/ppf/` cuyo nombre incluye un nombre propio. El grep de nombres de P4b no cubrió esas listas. En el paquete de P5 la ruta va como `<nombre>`; el de P4b queda como estaba, en el scratchpad.
- **Lo que encontré desactualizado en la tabla de reprocesamiento antes de P5** (no es de esta etapa):
  - su §4 decía «Contraste con esta tabla: OK, en las 38 filas»: desde P3c-2 (F08d) son 39, y con F08e, 40. Lo
    corregí, porque P5 cambia esa cuenta;
  - el mismo §4 dice «R00 a R32: las 40 variaciones»: desde P3c-2 (R13c) son 41 (`selftest_clave_cache.json`,
    `perfil_r2b.variaciones`). No lo corregí: no está entre las escrituras autorizadas;
  - las anclas a `prompt_r2b.py`, `cliente_e1.py` y `runner_corpus.py` del §1 y de las filas se corrieron con P3c-2,
    y P5 las corre otra vez. Corregí las de las líneas autorizadas y las de las filas que cambian (F08, F08c y F08e);
    las demás quedan como estaban.

## 1. Los dos controles previos (antes de tocar código)

**Documentación oficial, consultada el 05/10/2026:**
- `claude-sonnet-5`, el modelo de E3 (`runner_corpus.py:92`): su página dice, en «Good to know», que fijar
  `temperature`, `top_p` o `top_k` en un valor distinto del de por defecto devuelve un error 400
  (https://platform.claude.com/docs/en/models/sonnet-5/overview).
- La referencia de la API de mensajes marca `temperature` como obsoleto: los modelos lanzados después de Claude
  Opus 4.6 no admiten fijarlo; aceptan 1,0 por compatibilidad y rechazan cualquier otro valor
  (https://platform.claude.com/docs/en/api/messages).
- `claude-haiku-4-5`, el modelo de E1 (`runner_corpus.py:89`): salió el 15/10/2025
  (https://platform.claude.com/docs/en/models/haiku-4-5/overview), antes que Claude Opus 4.6, del 05/02/2026
  (https://platform.claude.com/docs/en/models/opus-4-6/overview). Su página no trae ninguna restricción de
  temperatura. El rango, de 0,0 a 1,0, y el valor por defecto, 1,0, están en la documentación del SDK instalado
  (anthropic 0.100.0, `resources/messages/messages.py:266-273`), que agrega que ni con 0,0 la respuesta es del todo
  determinística. La página no dice con esas palabras que el modelo acepta 0 y 1: lo leo del rango y de la
  restricción, que es solo para los modelos posteriores a Opus 4.6. La corrida lo confirma: los 54 pedidos de E1 con
  0 y la llamada forzada con 1 salieron sin error.
- La misma página de Haiku 4.5 da su retiro «no antes del 15/10/2026». Es el riesgo que el plan ya registra
  (`docs/plan_tesis.md:404`).

**La llamada** (`p5/sondeo_temperatura_e3.py`, desde una copia de HEAD, antes de tocar código): un pedido mínimo a
`claude-sonnet-5` con `temperature` 0 y `max_tokens` 8, sin caché ni reintentos. La API lo rechazó: error 400,
`invalid_request_error`, «`temperature` is deprecated for this model.» (`p5/salida/sondeo_temperatura_e3.json`). Un
error 400 no se factura.

## 2. El código

Solo con el perfil r2b y la forma r2. Archivos: `e1_extractor/prompt_r2b.py`, `corpus_v2/runner_corpus.py` (el
pedido del reintento por salida mal formada se arma ahí), `e1_extractor/cliente_e1.py` (solo comentarios) y los
selftests `e1_extractor/selftest_prompt_r2b.py` y `selftest_ub53.py`.

- **`prompt_r2b.py`:**
  - `TEMPERATURA_E1_R2B = 0` y `TEMPERATURA_REINTENTO_FORMA_R2B = 1`, con su comentario (`:105-110`);
  - `build_request_kwargs_r2b` agrega `"temperature": TEMPERATURA_E1_R2B` (`:445`);
  - `kwargs_reintento_forma_r2b(kwargs)` devuelve el pedido recibido, con su techo, y `temperature` 1, sin tocar
    el recibido (`:453-456`);
  - un párrafo de P5 en el docstring (`:39-42`) y las dos constantes y la función en `__all__`.
- **`runner_corpus.py`:** `kwargs_reintento_forma(kwargs, perfil)` (`:488-496`) delega en
  `prompt_r2b.kwargs_reintento_forma_r2b` con un perfil de forma r2 y, con los perfiles existentes, devuelve el
  mismo pedido (el mismo objeto). `fase_e1` arma con él el pedido del reintento (`:630-635`). El comentario de
  `:458-462` lo dice.
- **`cliente_e1.py`:** solo comentarios y docstrings (`:69-76`, `:279-283`, `:442-449`): con el perfil r2b, el
  reintento por forma deja de ser el mismo pedido. El cliente lo pasa tal cual, como antes.
- **Salen del mismo armado, con temperatura 0:** el primer intento, el reintento por corte y el tercer escalón
  (copias del pedido con otro `max_tokens`, `cliente_e1.py:430-438`) y el reintento del ratchet
  (`ratchet_e3.build_reextraccion_kwargs` con el perfil, `ratchet_e3.py:366-368`). Lo prueba `selftest_ub53`, P8.
- **No cambian:** el prefijo (`322c5a23e9b7`, con sus candados), el mensaje (candado `a9cb702c…`), el tool schema, el
  namespace (`e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7|think=0`) y el pedido de E3.
- **Los valores van como enteros, 0 y 1,** como `TEMPERATURE = 0` del agente de la evaluación
  (`evaluacion/harness.py:48`). La clave serializa el pedido, y `0` y `0.0` dan claves distintas: el valor queda
  fijado en la constante.
- **Selftests (sobre una copia):** `selftest_prompt_r2b` 55 de 55 (51 antes; la sección H suma 4) y
  `selftest_ub53` 58 de 58 (52 antes; P8 suma 6, con `fase_e1` y un stub: con el perfil r2b, el reintento por forma
  sale con temperatura 1 y el resto del pedido igual; con el perfil sellado, el mismo pedido sin temperatura).
- **Los perfiles existentes, byte a byte:** el anclaje del perfil sellado da 2.434 de 2.434 claves de E1 y 2.430 de
  2.430 de E3 (`selftest_clave_cache`), y la cadena r2a da los sha256 de C2, `70d51e42…` y `fa4c1043…`
  (`r2_codigo2/c2_cadena.py`).
- **Un control de otra unidad afirma que el reintento usa el mismo pedido:** `r2_codigo2/c2_sinteticos.py:144` (B1).
  Corre con el perfil del grafo de los diez TOs (el sellado) y el camino r2, y sigue siendo cierto: da 23 de 23. No lo
  edité. También `p4/correr_p4.py` y `p4b/correr_p4b.py` arman el reintento sin temperatura: corren desde la copia de
  su commit y no los edité.

## 3. La tabla de reprocesamiento y el selftest de claves

En `data/experiment/mantenimiento/tabla_reprocesamiento.md`:
- **F08** queda con el modelo y `max_tokens` (R12 y R13). La temperatura sale de ahí.
- **F08e, nueva:** la temperatura del pedido de E1 del perfil r2b, de la que salen el primer intento, el reintento
  por corte, el tercer escalón y el reintento del ratchet. Mueve la clave de E1 de todas las unidades: clase
  «todo». Su variación es **R14**, que antes agregaba `temperature` 0,0 a un pedido que no la tenía y ahora cambia
  el valor (0 → 1). R14 verifica además que el pedido lleva 0 y que, sin la temperatura, como en P4 y P4b, la clave
  es otra en las trece unidades de la muestra. Con el perfil sellado, V14 sigue como estaba.
- **F08c y R25:** el reintento por salida mal formada es el pedido que produjo la salida con `temperature` 1, en el
  namespace `-rforma1`. R25 verifica que difiere del primer intento solo en la temperatura y que su clave no es la
  del mismo pedido en ese namespace.
- **`:113`:** con el perfil r2b, E1 corre con temperatura 0, que no la vuelve determinística (6 de 27 iguales en
  P5), y E3 sin temperatura fijada.
- **De paso:** `:20` y `:22` con el hash de P3c (`322c5a23e9b7`), su ancla (`prompt_r2b.py:170-172`) y la de `:21`
  (`cliente_e1.py:76`), que P5 corrió; el pedido de E1 en `prompt_r2b.py:440-450`, y en la lista del §1 del pedido,
  la temperatura.
- **Por consecuencia:** las notas a F08c y F08e, F08e en la lista «Solo r2b» y el contraste en 40 filas (§0).

`selftest_clave_cache.json`, regenerado sobre una copia: veredicto OK, contraste con la tabla OK en las 40 filas,
las 41 variaciones del perfil r2b y las 25 del sellado dan lo esperado. Respecto del JSON anterior cambian la clave
de E1 de las trece unidades de la muestra r2b (la temperatura), la descripción y el detalle de R14 y R25 y la fila
F08e del contraste; las claves de E3 no cambian.

## 4. La selección y la proyección

- **Selección sellada** a las 10:25:30 (`p5/seleccion_p5.md`; `p5/salida/seleccion_p5.json`, sha256
  `a5640ffc…`). La corrida empezó a las 10:26:38.
  - E1: las 27 unidades de P4b.
  - E3: las 5 de la pata de P4b y 5 más por regla: `cla::5.1.1.1` y `cap::6.2.2.6`, y por sorteo con semilla
    declarada, `cap::5.3.1.3` (c), `cap::10.2.2.4` (d) y `polcre::5.3` (e).
  - El reintento forzado, sobre `ctacte::3.2.4`, la más corta.
- **Proyección** (`p5/salida/proyeccion_p5.json`, sobre lo medido en P4b con el mismo prefijo): USD 0,8796 central y
  1,3032 alta, dentro del tope.

## 5. Resultados

**a. Las claves.** Namespace `e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7|think=0`, el mismo del brazo de P3c
de P4b: cambia solo el pedido. Antes de correr, ninguna de las 27 claves con temperatura 0 era la de P4b (0 de 27)
ni estaba en la base de la tanda 0, la de P4 o la de P4b. Después, las 27 están en las dos bases de P5. El archivo
para T1 de U-REEXT-T0 es `p5/salida/claves_despues.json` (namespace, las 27 claves y la del reintento forzado).

**b. E1 contra E1** (`p5/salida/analisis_p5.json`, `medicion_b`):
- **6 de 27 respuestas salen iguales byte a byte** (las mismas 6 con las claves ordenadas): `ext::6.1.1`,
  `cla::6.5.4.5`, `ext::10.4.2.5`, `ext::10.3.6`, `ext::3.5.3::intro` y `cla::5.1.1::intro`.
- **De las 21 que difieren,** 5 solo en la redacción, con los mismos conteos (`cap::11.4`, `cap::10.2.2.4`,
  `ctacte::3.2.4`, `ctacte::3.2::intro` y `cap::6.2.2.6`), y 16 en algún conteo:
  - 13 en los nodos por tipo, con 33 nodos que cambian en total y 11 como máximo, en `cap::10.3.3.1` (de
    Condicion y Obligacion a Operacion, Restriccion y Potestad);
  - 3 en las normas (`ext::10.4.3.6`, `polcre::5.3` y `ext::3.5.3.1`), 13 en las relaciones y 4 en las omisiones.
- **Contra P4b**, que corrió sin temperatura fijada, cada corrida da 1 de 27 igual (`ext::6.1.1`).

**c. El ejemplo, en las dos corridas** (`medicion_c`):
- `cla::5.1.1::intro`: la Definicion «Cartera comercial — alcance», igual byte a byte en las dos.
- `cla::5.1.1.1`: la Excepcion, la Operacion «Inclusión en cartera comercial» y dos Condicion, el monto y el
  repago, cada una con `condicion_de` hacia esa Operacion. El `exceptua` de la Excepcion a la Operacion de los
  créditos se rechaza por la firma, como en P4b.
- En P4b, el brazo de P3c daba una sola Condicion y el anterior las tres piezas: con temperatura 0, las dos
  corridas dan las tres. Lo que daría U-REEXT-T0 es una respuesta más; la condición 10 de la tanda 1 se verifica en
  su grafo, como está decidido.

**d. Contra P4b, por grupo** (lectura asistida con los criterios de `p4b/marcas_p4b.py`, PENDIENTE de revisión;
`p5/marcas_p5.py`, `p5/salida/marcas_p5.json`). Cumplen, en A / B / brazo de P3c de P4b, y cuántas marcas cambian:

| Grupo | A | B | P4b | Cambian A contra P4b | Cambian B contra P4b | Cambian A contra B |
|---|---|---|---|---|---|---|
| a, transición | 1 de 1 | 0 de 1 | 0 de 1 | 1 de 1 | 0 de 1 | 1 de 1 |
| a | 1 de 3 | 1 de 3 | 2 de 3 | 1 de 3 | 1 de 3 | 0 de 3 |
| b1, ítems | 0 de 3 | 0 de 3 | 0 de 3 | 0 de 3 | 0 de 3 | 0 de 3 |
| b2, ítems | 0 de 3 | 0 de 3 | 0 de 3 | 0 de 3 | 0 de 3 | 0 de 3 |
| b, encabezados | 0 de 2 | 0 de 2 | 0 de 2 | 0 de 2 | 0 de 2 | 0 de 2 |
| c | 1 de 4 | 1 de 4 | 1 de 4 | 0 de 4 | 0 de 4 | 0 de 4 |
| d | 2 de 4 | 3 de 4 | 4 de 4 | 2 de 4 | 1 de 4 | 1 de 4 |
| e | 2 de 4 | 0 de 4 | 3 de 4 | 3 de 4 | 3 de 4 | 2 de 4 |
| ejemplo | 2 de 2 | 2 de 2 | 1 de 2 | 1 de 2 | 1 de 2 | 0 de 2 |
| f | 1 de 1 | 1 de 1 | 1 de 1 | 0 de 1 | 0 de 1 | 0 de 1 |
| **Total** | | | | **8 de 27** | **6 de 27** | **4 de 27** |

- **Lo que cambia:**
  - en a, `cap::10.3.3.1` registra en las dos corridas «De lo contrario, será de aplicación lo siguiente» como
    `meta_normativo`. Es una lectura dudosa: el «De lo contrario» es la condición del régimen alternativo;
  - en d, `cap::10.2.2.4` emite aparte, en las dos, el deber del encabezado como Condicion, otra lectura dudosa, y
    `ext::4.1.4.7` lo emite con tramo solo del encabezado en A;
  - en e, «las entidades», que el texto no nombra, vuelve: en `cap::6.3.2::intro` (A), `cap::6.3.2.1` (B) y
    `polcre::5.3` (las dos). Menciones de sujeto que verifican: 32 de 35 en A y 32 de 40 en B, contra 26 de 26 en
    P4b. Normas con `aplica_a`: 28 de 49 y 33 de 50, contra 19 de 42.
- **`cap::6.2.2.6`:** en las dos corridas, ningún porcentaje de `cap::tabla037` copiado y la omisión `tabla`
  declarada.
- **Omisiones `meta_normativo`:** 10 en A (6 con marca del contador) y 15 en B (10), contra 12 (7) en P4b.

**e. La salida** (`medicion_e`): A, 43.424 tokens, 1,959 por carácter de texto propio (22.166 caracteres), mediana
de 1.316 por unidad; B, 43.872, 1,979, mediana 1.448; P4b, 40.626, 1,833, mediana 1.274. A sobre P4b, 1,069; B sobre
P4b, 1,080; B sobre A, 1,010. La entrada sin caché es la misma en las tres (38.421 tokens): la temperatura no agrega
tokens. Por unidad, en `medicion_e.por_unidad`.

**f. E3 contra E3** (10 unidades, la primera verificación, sin el ciclo; `medicion_f_e3`):
- el mismo pedido y la misma clave en las dos corridas, en las 10;
- el mismo veredicto del modelo (`completo_ok` o `faltantes_detectados`) en 10 de 10, y la misma evaluación de
  `ratchet_e3` (completo, aceptable y bloqueantes) en 9 de 10. Iguales byte a byte, 6 de 10: las 6 `completo_ok`;
- en las 4 con un faltante, cambia el faltante: su tipo, su severidad o su nota. En `cap::5.3.1.3`, el mismo
  reclamo (las condiciones de i) que ii) no conecta) sale con severidad alta en A, que bloquea y haría reintentar
  la unidad en el ratchet, y media en B, que la acepta con un residual.

**g. El reintento forzado** (`p5/salida/reintento_forma_p5.json`): sobre `ctacte::3.2.4`, el pedido del primer
intento con `temperature` 1 (la única diferencia), `max_tokens` 8.192, namespace
`e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7-rforma1|think=0`, clave `cd9523519f36…` (la del primer intento,
`b65c1383375f…`). Respondió con `tool_use`, bien formado: 1.058 tokens de entrada y 507 de salida.

**h. La caché de prompts de la API:** la llamada del punto g leyó de la caché los 27.840 tokens del prefijo y no
escribió ninguno, un segundo después de la última llamada con temperatura 0 de la corrida A. El prefijo se lee entre
pedidos con temperatura 0 y 1. La corrida B tampoco escribió el prefijo (27 lecturas).

**i. El costo** (`p5/salida/costo_p5.json`):

| Paso | USD |
|---|---:|
| E1, corrida A (27 llamadas, una escritura del prefijo) | 0,3627 |
| Reintento forzado | 0,0064 |
| E1, corrida B (27 llamadas, sin escritura) | 0,3329 |
| E3, corrida A (10 llamadas, una escritura de su prefijo) | 0,1168 |
| E3, corrida B (10 llamadas) | 0,0890 |
| **Total** (presupuesto compartido, 0,907778) | **0,9078** |

La llamada de control del punto 1 dio error 400 y no se facturó.

**U-REEXT-T0**, con el método de P4b y los cocientes de cada corrida contra el brazo anterior de P4b (salida 0,947 y
0,957, entrada 1,026; en P4b la salida del brazo de P3c daba 0,886):
- de USD 44,70 a 48,97 central;
- con el tercer escalón, de 45,06 a 49,93;
- con el factor 1,4, de 63,93 a 69,91.

El tope de 72 alcanza, con menos margen que con P4b (67,83).

## 6. Límites

- **La variación sigue con temperatura 0.** 21 de 27 respuestas de E1 cambian entre dos corridas del mismo pedido,
  y la marca de lectura cambia en 4 de 27. Con grupos de 1 a 4 casos, una diferencia de uno o dos casos entre P4b y
  P5, o entre lecturas de U-REEXT-T0, cabe en la variación del modelo. El ejemplo salió completo en las dos
  corridas, pero son dos respuestas.
- **E3 corre sin temperatura fijada:** en 1 de 10 la evaluación decide distinto si la unidad reintenta.
- **La lectura de d es mía y asistida,** con los criterios de P4b, y tiene lecturas dudosas declaradas
  (`cap::10.3.3.1` y `cap::10.2.2.4`).
- **Las 27 unidades se eligieron por lectura en P4b:** los cocientes de salida son una cota para U-REEXT-T0, no
  una estimación de la tanda.

## 7. Controles

- **Doble corrida de USD 0 sobre una copia sin enlaces** del árbol de trabajo (`control_p5.sh`, en el paquete): la
  selección, la proyección, el análisis con las fichas, las marcas y el costo, más la batería de selftests y cadenas.
  - Las 8 salidas comparadas son iguales entre las dos corridas: las 6 de P5, el JSON del selftest de claves y la
    cadena r2a.
  - Las 6 de P5 son iguales a las de `p5/salida/`, y el JSON del selftest de claves, al del repo. La selección se
    reproduce con su sha256 sellado.
- **La batería, igual en las dos corridas:**
  - `selftest_prompt_r2b` 55/55, `selftest_ub53` 58/58, `selftest_e1` 80/80, `selftest_e3` 101/101,
    `selftest_e2` 41/41, `selftest_pyd_r2` 398/398, `selftest_r3` 109/109 y `selftest_r4` 26/26;
  - las cadenas de P3 27/27 y de P3b-2 20/20, y `c2_sinteticos` 23/23;
  - el selftest de claves, OK;
  - la cadena r2a, `70d51e42…` y `fa4c1043…`;
  - `selftest_manifiesto` da 44/49, con los 5 fallos de su P5 que la regla l de CLAUDE.md anuncia para una copia.
- **El repo:**
  - no cambió durante el control (12.922 archivos) ni durante la corrida con API (12.908);
  - ningún `.pyc` nuevo;
  - el grep de nombres de personas y de referencias a mensajes dio vacío sobre lo escrito.
- **Escrituras:**
  - el código y los selftests autorizados: `prompt_r2b.py`, `cliente_e1.py`, `runner_corpus.py`,
    `selftest_prompt_r2b.py` y `selftest_ub53.py`;
  - `tabla_reprocesamiento.md`, `selftest_clave_cache.py` y su JSON;
  - `data/experiment/prompt_r2/p5/` (7 scripts, el sello y 13 salidas);
  - este freno.
- **El log de usage de la corrida** (75 líneas: 55 de E1 y 20 de E3) quedó en la copia y va al paquete.

## 8. Para la autora

- Revisar la lectura asistida de d (`p5/marcas_p5.py`; fichas en `p5/salida/fichas_p5.md`).
- La línea «R00 a R32: las 40 variaciones» del §4 de la tabla, que son 41 desde P3c-2, y las anclas corridas
  (§0): no estaban autorizadas.
- El registro de modelos de r2b con la temperatura de cada pedido, que la nota del mandato pide, no estaba entre
  las escrituras de P5; el borrador del laudo de la release r2 (`docs/laudo_release_r2_pipeline.md:310-311`) se pone
  al día cuando se firme.
- El retiro de `claude-haiku-4-5` «no antes del 15/10/2026» (punto 1), frente al calendario de U-REEXT-T0.
- **PENDIENTE:** la revisión de este freno y el commit de P5.
