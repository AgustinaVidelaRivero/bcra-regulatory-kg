# U-PROMPT-R2 — diseño de la etapa P3b (FRENO P3b-1)

04/10/2026. HEAD `8d01b04` al empezar y `0b98045` al cerrar; ese commit, de otras unidades, no toca este mandato
ni la cadena. USD 0: ninguna llamada a la API. Sin commit. Nada congelado ni implementado: P3b-2
espera el «seguí» de este freno.

## 0. Fuentes

- **El mandato:** `git show b901f6d:docs/mandatos/UPROMPT_R2_prefijo_nuevo.md`.
- **Sus notas de P3b, leídas completas en `8d01b04`:**
  - la etapa P3b: puntos a a l, dos frenos y escrituras;
  - los agregados del 04/10/2026: j con dos opciones, k con la medida de la copia de la nota y la cola
    humana marcada;
  - las `otras_propiedades` de la relación, que llegan a la arista, con `e2_lib.py` sumado a las escrituras;
  - el reparto de lo que dejó P3.
  Las notas entraron en `4f3bcff` y en `8d01b04`.
- **Diferencia con el «seguí».** El «seguí» dice que P3 está commiteada en `8d01b04`. El `git log` la muestra en
  `4aa92c7` («U-PROMPT-R2 P3 (USD 0): …»). `8d01b04` son las enmiendas firmadas al protocolo y la cola humana, y
  trae la última nota del mandato. Mandan los archivos.
- **Los hallazgos:**
  - la revisión independiente, `reports/u_revision_libre/` (`54f57cd`): `reporte.md`, `freno_a.md`,
    `freno_a1.md` y `freno_b1.md`;
  - U-DIAG-VINCULO, `reports/u_diag_vinculo/reporte.md` (`b0ee084`).
- **Corridas.** Todo corrió sobre una copia sin enlaces del repo, en el scratchpad (regla l), y escribe fuera
  del repo. Las salidas están copiadas en `p3b/salida/`.

## 1. El parche del prefijo (puntos a a f)

El parche son 12 reemplazos con ancla única sobre el texto congelado, como el borrador de P1
(`p3b/borrador_parche_p3b.py`).
- **Archivos:**
  - `salida/reemplazos_p3b_borrador.json`;
  - el prefijo con el parche: `salida/prefijo_r2b_parche_borrador.txt`;
  - lado a lado: `salida/lado_a_lado_p3b.md`.
- **Anclas y reversibilidad:** cada ancla aparece una vez, y deshaciendo los reemplazos en orden inverso vuelve el
  congelado byte a byte.

| | Congelado | Borrador |
|---|---|---|
| Caracteres | 51.780 | 55.105 (+3.325) |
| sha256 | `cdb374508523…` | `8d84364fc3b6…` |
| Hash canónico (system + tools) | `14d6b63b508e` | `3817de475c93` (no congelado) |
| Tool schema | `0c391f2b…` | sin cambio |

| Id | Punto (hallazgo) | Qué agrega |
|---|---|---|
| P3B-a1 | a (1.3) | En Obligacion, la RECOMENDACIÓN: se extrae como Obligacion, con `otras_propiedades.modalidad` = el tramo literal que la califica y la descripción que dice que es una recomendación; el código clasifica |
| P3B-a2 | a | En la composición, la modalidad suma «recomendación» |
| P3B-b1 | b (1.4) | En Restriccion, la CONSECUENCIA DE UN INCUMPLIMIENTO: Obligacion o Potestad de quien la aplica, si el texto lo nombra; si no, omisión `fuera_de_tipos` con su tramo; nunca Restriccion; `otras_propiedades.consecuencia` = el tramo literal |
| P3B-b2 | b | En UMBRALES, la remisión a esa regla |
| P3B-c1 | c (2.8) | En Excepcion, la CONEXIÓN: `exceptua` o `exceptua_obligacion` si la norma está en la unidad; si no, sin la relación, como la Condicion de R8 |
| P3B-d1, d2, d3 | d (3.2) | Definiciones de `regula`, `condiciona` y `requiere`, y la contradicción de `regula` desde Restriccion resuelta en el texto: la tabla lo admite (la matriz no cambia) y la regla dice que no se usa |
| P3B-ef1, g1 | e, f, g | El encabezado de la lista puede ir seguido de párrafos de cierre (lo señala el mensaje), en COMPOSICIÓN y en Condicion |
| P3B-f1 | f (U-DIAG-VINCULO) | Rama nueva de la composición: EXCEPCIONES, cada ítem es una Excepcion compuesta, sin `exceptua` cuando la norma está en otra unidad |
| P3B-e1 | e (1.18) | La lista dentro de la unidad: la composición vale también ahí, con los dos segmentos del texto propio |

**Fuentes de las definiciones de d.** Las definiciones salen de las operativas del esquema v2
(`docs/esquema_v2_diseño.md`, §2.1).
- `regula`: «gobierna la modalidad de la operación (cómo se hace)».
- `condiciona`: «la operación solo es accesible si la obligación se satisface».
- `requiere`: «ejecutar la operación dispara la obligación».

**No-filtración** (`p3b/nofiltracion_p3b.py` → `salida/nofiltracion_p3b.json`). Usa la regla de P1 contra el
prefijo congelado.
- **Población:** 5.376 chunks, de la E0 legada y la e0-r2 de los diez TOs y de los cuatro del estrato fuera de
  muestra.
- **Ventanas:** de las 610 ventanas de 5 palabras que agrega el prefijo y de las 230 de los literales nuevos
  (mensaje, NOTA de E3 y aviso del reintento), 0 aparecen en algún chunk.
- **Casos de control:** 0 bigramas o trigramas de los 37 casos en el texto agregado. Los casos son los de P1,
  `cla::5.1.1::intro` y las unidades de los hallazgos.

## 2. El mensaje de E1 (g, h) y la NOTA de E3 (i)

El borrador está en `p3b/mensaje_p3b_borrador.py`, con los conteos sobre la e0-r2 de la tanda 0 (2.434 unidades;
`salida/mensaje_p3b.json`). El lado a lado de los casos está en `salida/mensaje_p3b_lado_a_lado.md`.

**g, ítems que el mensaje no marca (1.2).**
- **Regla:** un chunk de punto es ítem si su herencia trae un bloque que no es de cierre y termina en «:», y
  después de él solo hay bloques de cierre o ninguno. Un cierre que termina en «:» no abre la lista: es el caso del
  que presenta la fórmula de los APR en `cap::8.5`.
- **Mensaje:** nombra el bloque («el bloque [intro | punto 8.5] termina en «:»…») y aclara que los cierres que
  siguen no son parte del encabezado.
- **Conteo:** de 706 ítems a 1.053, con los 347 que contó la revisión: ext 225, ctacte 40, cla 21, cap 19,
  polcre 18, pro 10, pagjub 7, lingob 5 y docvig 2. No se pierde ninguno, y `cap::8.5.1` a `8.5.3` están.
- **Recorte de herencia:** la regla da lo mismo si C2 de U-R2-CODIGO-2 recorta la herencia (su punto h), porque
  sin cierres el bloque con «:» es el último.

**h, mini-chunks que empiezan a mitad de oración (2.16).**
- **Regla:**
  - el último bloque heredado es el `encabezado` de la misma unidad;
  - ese encabezado no termina en «.», «:» ni «;»;
  - el texto del bloque empieza en minúscula.
- **Conteo:** 121 de 376 mini-chunks. Con solo «empieza en minúscula» serían 125, como en la revisión. Los 4 de
  diferencia (`cap::8.2.1::intro`, `8.2.2`, `8.3.2` y `8.3.4`) empiezan con el subíndice «n1» de una fórmula y
  tienen el título completo.
- **Mensaje:** la línea de la cadena de títulos avisa que su última línea es el comienzo de la oración del bloque,
  que se lee con él y que el `tramo` puede empezar ahí.
- **El par en el código** (`validador_r2.verificar_tramo_entidad`, en P3b-2): en esos 121, el tramo también se
  verifica contra el título y el cuerpo en orden de lectura, y se cuenta aparte.
- **Prueba:** con un tramo de 8 palabras que cruza del título al cuerpo, verifica hoy en 5 de 121 y en orden de
  lectura en 121 de 121.

**Mensajes de E1 que cambian:** 1.174 de 2.434, que son los 1.053 ítems y los 121 mini-chunks. El prefijo nuevo ya
cambia la clave de todas las unidades.

**i, NOTA de E3 para las omisiones declaradas (3.4).**
- **Cuándo va:** cuando la validación (forma r2) declara omisiones `meta_normativo`, `fuera_de_tipos` o
  `relacion_sin_predicado`.
- **Qué dice:** que un tramo declarado así no es un faltante, salvo que lo declarado no sea lo que dice su
  categoría.
- **Dónde:** se suma a `notas_r2` de `prompt_e3.py`, que pasa a recibir la validación. El prefijo de E3 y su
  candado no cambian.
- **Cuántas unidades:** no se puede contar en la tanda 0, porque el crudo v3 no trae categorías. Lo cuenta P4.

## 3. Quién decide en cada punto

Criterio de la nota: el modelo copia el marcador y el código clasifica, si la decisión depende de cómo se lee
una frase.

| Punto | Forma | Por qué |
|---|---|---|
| a, recomendación | mixta: el modelo reconoce y copia el marcador (`modalidad`), y el código clasifica | Que la oración aconseja y no manda es lectura del modelo; la clasificación del tramo copiado es código y se amplía entre tandas sin tocar el prefijo |
| b, consecuencia | decide el modelo, y copia el marcador (`consecuencia`) | Quién aplica la consecuencia y si el texto la manda o la habilita es lectura de la oración; el marcador permite clasificar y contar en código |
| c, Excepcion conectada | decide el modelo | Qué norma exceptúa la salvedad no tiene marcador copiable; el código solo controla la firma |
| d, predicados | decide el modelo | El sentido del vínculo entre un deber y un acto no tiene una forma léxica estable; el código controla la matriz |
| e, lista en la unidad | decide el modelo, y el código verifica el tramo de dos segmentos | Ver que una oración abre una lista dentro de la unidad y componer es lectura |
| f, lista de excepciones | decide el modelo, y el código verifica el tramo | Igual que e; el vínculo entre unidades queda para el ensamblado (U-DIAG-VINCULO, a-R) |
| g, ítems | decide el código | Sale de la estructura de E0 |
| h, mini-chunks a mitad de oración | decide el código (detección y verificación), y el modelo extrae | La detección es estructural |
| i, NOTA de E3 | decide el código cuándo va, y E3 juzga | La NOTA va según las categorías declaradas |
| j, veredictos como texto | código (opción 1) o modelo (opción 2) | §4 |
| k, reintento y copia de la nota | código, que compara y marca; el aviso del reintento es para el modelo | §5 |
| l, Comunicacion | decide el código, desde el tramo verificado | §6 |

## 4. j: veredictos de E3 como texto (2.2)

Medida en `p3b/lazo_e3_p3b.py` → `salida/lazo_e3_p3b.json`. Da lo mismo en `salida_dirigida` y en `salida`.

**Las 25 unidades.**
- Son 21 en la verificación (`cola_humana_veredicto_inutilizable`) y 4 en la re-verificación (`cola_humana`).
- El texto trae el veredicto entero en las 25: 17 `faltantes_detectados` y 8 `completo_ok`. En el campo
  `veredicto` de arriba no viene nada.
- 24 textos son el objeto JSON del veredicto completo, y `json.loads` los lee.
- El que falta es `cap::5.3.2.5`: la lista de faltantes seguida de `, "veredicto": "faltantes_detectados"}`, que no
  es un JSON válido. Con reparo se leen las 25: se toma el primer valor JSON (`raw_decode`) y el veredicto del
  resto.

**Opción 1: leer esa forma en código, sin API.** Con lo leído, la política vigente del ratchet
(`ratchet_e3.evaluar_veredicto`: LAUDO A, LAUDO B con su enmienda y verificación de citas) da:

| | Con reparo | Estricta |
|---|---|---|
| Salen de la cola | 20: 5 a `completo_ok_directo`, 11 a `aceptado_con_residuales`, 4 a `aceptado_tras_reintento` | 19 (la misma tabla sin `cap::5.3.2.5`) |
| Van a un reintento (faltante alto con cita verificada) | 4: `ext::9.3.10::intro`, `ctacte::6.4.1::intro`, `lingob::1.2.4`, `docvig::1.2.2` | 4 |
| Quedan en la cola | 1: `ric::5.1.3.2` (faltante alto sin cita verificada: inutilizable, como manda la política) | 2: esa y `cap::5.3.2.5`, sin leer |

- De las 11 que pasan a residuales, 2 tienen un faltante alto que LAUDO B exime (`ext::3.18.1::intro` y
  `ext::3.6.1::intro`).
- **El texto que no es JSON válido:** con el reparo se lee y se registra que se leyó así. Sin el reparo queda en la
  cola, con el error de formato.

**Opción 2: volver a pedir el veredicto a E3.**
- **Costo:** USD 0,007442 por llamada de E3. Es el gasto de E3 de la tanda 0 (USD 19,9529) dividido por sus 2.681
  llamadas, de los `resumen_e3.json` de `salida_dirigida`. Para las 25, USD 0,19.
- **Reintentos:** si E3 repitiera el contenido bien formado, el resultado sería el de la opción 1. Sumarían 4
  reintentos a USD 0,009154 más 0,007442 cada uno, y el total daría unos USD 0,25.
- **Riesgo:** la falla de formato fue de 25 en 2.681 llamadas (0,93 %), así que el pedido nuevo puede volver a
  fallar.
- **En U-REEXT-T0:** con unas 2.700 llamadas, son unas 25 llamadas extra, unos USD 0,19.

**Las dos opciones rigen solo con la forma «r2».** No implemento ninguna antes de la decisión. Recomiendo la 1 con
reparo, que es USD 0 y lee lo que E3 ya dijo, con la marca de cómo se leyó.

## 5. k: el reintento que reemplaza sin comparar (2.14) y la copia de la nota de E3

**Pérdidas en las 220 unidades aceptadas tras el reintento** (219 en `salida`).
- 18 quedan con menos entidades que en el primer intento, 27 con menos relaciones y 12 con menos de las dos.
- Son 33 unidades con menos de algo, y 91 relaciones de menos en total.
- Una regla de identidad por etiqueta o descripción normalizadas no sirve para emparejar: deja 472 entidades sin
  par en 161 unidades, porque el reintento reescribe las etiquetas.

| Opción | Qué hace | Unidades | Cola |
|---|---|---|---|
| k1, hoy | el reintento reemplaza a la primera extracción | 33 con pérdidas aceptadas sin marca | sin cambio |
| k2, a la cola | si el reintento tiene menos entidades o relaciones, la unidad va a la cola humana (marcada) | 33 | entran 33; no sale ninguna |
| k3, unión | se agregan los elementos de la primera que el reintento dejó | — | sin cambio. Pide una regla de identidad que no hay (472 sin par) |
| k4, marca | se acepta el reintento con la marca `reintento_con_menos_elementos`, que entra a la muestra de la tanda | 33 marcadas | sin cambio |

Ninguna opción saca unidades de la cola. Recomiendo k4: es la misma salida que la cola humana (adentro, marcado y
leído por muestra), y k3 no tiene una regla de identidad.

**Copia de la nota de E3.**
- **Regla:** la fijé en el docstring del script antes de la primera corrida; no está commiteada.
  - tokens de R-NORM (`validador_r2.norm_tokens`) y ventanas de 5 tokens seguidos;
  - una entidad del reintento copia la nota si su descripción o su etiqueta tiene una ventana que está en una
    `nota` de los faltantes que se le pasaron al reintento, y que no está ni en el texto de la unidad (propio y
    heredado) ni en sus citas.
- **Resultado:** 45 casos en 40 de las 220 unidades, listados en `salida/copia_nota_casos.md`.
  - `cla::6.3.3` está: su Condicion repite «cubiertos en otros puntos de».
  - La regla mide coincidencia de texto, no intención. No clasifiqué los 45 por lectura.

**Dos defensas (propuesta; solo con la forma «r2»).**
1. **El mensaje del reintento.** `bloque_feedback` suma una frase:
   > «Las notas del verificador explican qué falta y por qué; no son texto de la norma: no copies sus palabras
   > en descripciones, etiquetas ni tramos. Todo lo que extraigas sale del texto de la unidad.»
   La frase pasó la no-filtración. Con los perfiles existentes el bloque no cambia.
2. **Un control en código.** Con la misma regla de la medida, después de la re-extracción:
   - el ratchet marca las entidades cuya descripción o etiqueta lleva texto de la nota ausente de la unidad;
   - lo registra en el expediente y en un archivo de la corrida (`copias_nota_e3.jsonl`);
   - marca y no rechaza ni corrige.
   En la tanda 0 habría marcado 45 entidades en 40 unidades. La marca no llega al grafo, porque
   `runner_corpus.py` no está en las escrituras de P3b: queda en los registros de la corrida.

## 6. l: `derivar_comunicacion` y la ley escrita como «A-39» (1.12)

**Regla, solo con la forma «r2»** (`p3b/comunicacion_p3b.py` → `salida/comunicacion_p3b.json`). Se lee el tramo
de la entidad solo si verificó: es texto de la unidad, mientras que la etiqueta y el código los escribe el modelo.
1. Si el tramo nombra una Comunicación («com.» o «comunicación», la letra y el número, también en una enumeración
   como «A 5867, 5926 y 5970»), el tipo es esa letra y el número se controla contra el código.
2. Si no, y nombra una norma externa (`lexico_externa` de la política), es «externa».
3. Si no, no se deriva y se cuenta.

**Medida sobre los 22 nodos Comunicacion de KG-Tanda0-Diez-r2a.** El tramo verificado se aproxima con el texto de
la unidad.

| Hoy | Con la regla | Nodos |
|---|---|---|
| A | A | 11 |
| A | externa (`A-39`, «art. 39 inc. d) de la Ley 21.526», `ctacte::12.10.2`) | 1 |
| sin derivación | externa (1/17, 3/15, Res. 92/21) | 3 |
| sin derivación | sin sustento: no son normas | 7 |

- **Con la etiqueta en lugar del texto, no cambia nada:** el modelo escribió «Com. A 39 …» en la etiqueta. Por eso
  la regla lee el tramo verificado.
- **En el crudo del primer intento,** 31 entidades Comunicacion, sin cambio con la etiqueta; el efecto real lo mide
  P4.
- **La forma v3 no cambia.**

## 7. La modalidad copiada: cómo llega al código y al agente

Hoy las `otras_propiedades` de una entidad terminan en `properties_no_definidas` del nodo (P3). Esa clave queda
fuera de `properties`, y la vista del agente lleva solo `properties`: `comun_tanda0.py:78-94` y el cargador de
Neo4j.

Propuesta, sin cambiar el esquema:
- **El agente:** ve la modalidad en la descripción, que el prefijo manda decir («es una recomendación y no un
  deber»; para la consecuencia, lo dice el tipo y la descripción). Está en `properties.descripcion` y llega hoy.
- **El código:** en P3b-2, `validador_r2` (forma r2) clasifica `otras_propiedades.modalidad` y `.consecuencia` con
  una lista cerrada en código.
  - Valores: `recomendacion`, `consecuencia_de_incumplimiento` o `no_clasificada`, con contador.
  - Los guarda en `properties_no_definidas.modalidad_clasificada`, junto al tramo copiado.
  - Una forma nueva se agrega a la lista y se vuelve a aplicar sobre lo extraído, sin cambiar el prefijo.
- **La exportación** de `properties_no_definidas` al agente toca U-NAV-DISENO. Su requisito de las vistas ya pide
  exportar «las claves que quedan fuera de `properties`» (`docs/mandatos/UNAV_DISENO_navegacion_agente.md:117-121`,
  borrador). Propongo nombrar ahí `modalidad_clasificada`; es una nota a ese mandato, y la escribe la autora.

## 8. Lo que P3b-2 implementa además (sin opciones)

- **`e2_lib.py`, solo en el camino r2.** `ensamblar_r2` copia las `properties_no_definidas` de la relación a la
  arista (`AristaR2` ya las admite desde P3).
  - En una arista repetida, la primera procedencia gana, y una diferencia se cuenta como en los nodos.
  - Las relaciones de los grafos r2a no traen la clave (P3 la quita cuando está vacía), así que los cinco
    ensamblados sellados tienen que dar lo mismo byte a byte.
- **`ratchet_e3.py`, el campo `todo` de `cola_humana.jsonl`** (`:351-355`), solo con la forma «r2». Dice que la
  unidad entra al grafo marcada y que su revisión va por la muestra de cada tanda. Hoy dice «el chunk NO ingresa al
  grafo hasta resolución». No cambia qué entra al grafo.
- **`prompt_r2b.py`:**
  - el prefijo re-congelado, con sus candados, y los reemplazos nuevos;
  - `es_item` (g) y la detección de h;
  - el mensaje.
- **`perfil_e1.py`:** los candados del perfil r2b.
- **`prompt_e3.py`:** la NOTA i, con `notas_r2(chunk, validacion)`.
- **`validador_r2.py`:**
  - la verificación del tramo título→cuerpo (h);
  - la derivación de l;
  - la clasificación de la modalidad (§7).
- **Lo que decida la autora** sobre j y k, en `ratchet_e3.py`.
- **Selftests sobre una copia:** los de esos módulos, más la cadena sintética de P3 extendida con una relación con
  `otras_propiedades`.
- **Sellados:** se reproducen los cinco ensamblados y E0.
- **Estimación de costo** de la pareada y de U-REEXT-T0 con el prefijo nuevo: el prefijo agrega 3.325 caracteres
  por llamada de E1.
- **Orden con C2:** no corre a la vez que la implementación de C2 de U-R2-CODIGO-2. Antes de implementar miro
  `git status` y `git log`, porque comparten `selftest_pyd_r2.py`.

## 9. Fuera de la etapa y para P4

- **Fuera:**
  - el alcance en títulos sin «:» (2.7) va por código;
  - el plazo asumido máximo (1.8) pide una enmienda firmada;
  - el linaje (2.6) y las cuantías en tipos sin `umbrales` (2.10) se declaran como límite.
- **Un caso que P3b no resuelve:** `cap::8.5`. Aun compuesta, la comparación sale `no_determinada`, porque el
  sentido «mínimos» del encabezado no llega a la regla de comparación (hallazgo 16 de la revisión).
- **P4:**
  - suma `cla::5.1.1::intro` a los casos fijos;
  - suma un estrato de listas de excepciones elegidas por lectura;
  - mide las Condicion y Excepcion sin relación de ítems, las 121 unidades de h y la NOTA i;
  - no se autoriza hasta el FRENO P3b-2.
