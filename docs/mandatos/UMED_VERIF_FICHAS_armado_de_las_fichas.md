# Mandato U-MED-VERIF-FICHAS — el sorteo, las fichas, las planillas y la clave de U-MED-VERIF

**FIRMADO por la autora el 17/10/2026** (firma por mensaje de la autora, recibida a las 22:06:54; hoja de ruta de la mesa, §149), con
las decisiones (a), (a) y (a) del §9, las tres lecturas del diseño aprobadas (§4) y la precisión de la lista de exclusión (§3), que la
autora amplió a cualquier versión a la vista el mismo día (recibida a las 22:40:14; hoja de ruta de la mesa, §150), antes de todo sorteo
y antes del commit de este mandato. La versión para firmar la redactó la mesa el 17/10/2026 (§148; sha256 `6b82d335b5b4…`, en el paquete de la mesa). Rige desde esta firma.
USD 0, sin API. Corre apenas exista el commit de T5, que termina la tanda 1. El despacho lo escribe la mesa con el hash de ese commit.

**De dónde sale:**
- el diseño sellado de U-MED-VERIF: `fuera_del_repo/tesis_escritura/U-MED-VERIF/diseno_U-MED-VERIF_sellado_1710_v2.md`, sha256
  `5296703d672bfe0c435be9f0d5fdb8f981080d34f3c09a3fb79e5d4b0d929872`, sellado el 17/10/2026 a las 19:17:36
  (`sello_diseno_U-MED-VERIF_1710.txt`, en la misma carpeta). Rige entero; este mandato solo lo ejecuta;
- la respuesta de la mesa del 15/10/2026 (paquete de la mesa, `decisiones_110_mesa/umedverif/respuesta_U-MED-VERIF_mesa.md`, sha256
  `ec67b860…`), §1, §2 y §5;
- el pre-registro de la tanda 1, firmado en `95b18217`: el sello por commit (§5.1, `:498`), las muestras de la lectura de las aceptadas
  (§5.4, `:556`, y sus cadenas, `:1019-1062`) y el cegamiento de U-MED-VERIF (§7, `:900-909`);
- el código de la release, leído en HEAD (`ca5b39fd`), con las anclas de abajo;
- las decisiones de la autora del 17/10/2026, recibidas a las 22:06:54: las del §9, la aprobación de las lecturas del §4 y la precisión
  del §2 del diseño sobre la lista de exclusión (§3), fijada antes del sorteo;
- las decisiones de la autora del 17/10/2026, recibidas a las 22:40:14: la lista de exclusión cubre cualquier versión a la vista, y la
  regla de la lectura de `cid` (§3). Las dos van también a la §29 del registro de decisiones.

## 1. Qué hace

Sobre la tanda 1 tal como la sella su commit:
1. **el sorteo** de la muestra (diseño, §2);
2. **las fichas** de la etapa 1 y el material de la etapa 2 (diseño, §3 y §4);
3. **las dos planillas en blanco**, una por etapa (diseño, §5);
4. **la clave** de qué versión es la primera, en un archivo `NO_ABRIR_` (diseño, §4);
5. **el sello** de todo eso, con sha256 y hora.

No lee, no marca ni calcula ninguna cifra de la medición. La lectura, las pasadas y las cifras son de otras unidades.

## 2. Las fuentes, todas desde el commit del sello

- **Cómo lee:** con `git -C "$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg" --no-optional-locks show <commit del sello>:<ruta>`, nunca
  desde el árbol del repo.
- **El código que importa** sale del mismo commit, con `git archive <commit del sello> -- <rutas>` a su carpeta de trabajo, como copia
  (CLAUDE.md §4.l): sin enlaces, sin `.env` ni nada `NO_ABRIR_`, y con `python3 -B`.
- **Por TO,** en `data/experiment/reextraccion_v2/corpus_tanda1/salida_r2b/<to>/`:
  - `finales.jsonl`, con el último registro de cada `chunk_id` (`runner_corpus.py:309-310`): el `estado` define la población, y
    `validacion_final` es la nueva versión (`:909-913`; `ratchet_e3.py:508-532`);
  - `extracciones_e1.jsonl`, con el último registro de cada `chunk_id`: `validacion` es la primera versión (`runner_corpus.py:842-845`);
  - `veredictos.jsonl`: el registro de la unidad con `fase` «verificacion» e `intento` 0 (`ratchet_e3.py:492-506`), para las citas de
    la etapa 2.
- **El texto de cada unidad** (diseño, §4):
  - el chunk se reconstruye por el mismo camino que la fase E3 del runner (`runner_corpus.py:842-848`: `comun_e1.cargar_chunks`,
    `chunks_sin_ids_repetidos` y, con el perfil r2, `chunks_con_partes`), con el runner configurado por el manifiesto de la tanda 1
    (`configurar`, `:122-148`);
  - el texto de la ficha es `comun_e3.fuente_integro(chunk, bloque_de_lista=ratchet_e3._forma_r2(primera))` (`comun_e3.py:131`,
    `ratchet_e3.py:116`, `:283`): los mismos textos contra los que E3 verificó las citas (`fuente_para_citas`, `comun_e3.py:245`), con el
    bloque de la lista en los ítems y con los rótulos que separan el texto propio del heredado.
- **No lee:** `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, `cola_humana.jsonl`, ningún `NO_ABRIR_` de `tanda1/t2/` ni los `kg.json`.
  No los necesita.

## 3. El sorteo y la muestra (diseño, §2)

- **La población:** las unidades de los 20 TOs cuyo `estado` final es `aceptado_tras_reintento`.
- **El orden:** `random.Random(20261015).sample(ids, len(ids))`, con `ids = sorted(<ids de la población>)`.
- **La lista de exclusión** (precisión del diseño, §2, fijada por la autora el 17/10/2026 antes del sorteo; ampliada a las 22:40:14):
  toda unidad de la tanda 1 cuya extracción aparezca en el material de T4 que lee la autora, **en cualquier versión**, la final o la
  primera, no solo las de la lectura de las aceptadas. Es la razón del diseño: si vio la versión nueva, o la primera (por ejemplo, en la
  vigilancia (2)), en la ficha reconoce cuál de X e Y es la primera, y la lectura deja de ser a ciegas para ella.
  - **Las muestras que entran:** las de T4 que sortea T3 con las cadenas del pre-registro (`:556`, `:1019-1062`): `cola`,
    `aceptadas:items`, `aceptadas:no_items`, `vigilancia:1`, `vigilancia:2`, `vigilancia:3`, `vigilancia:7` y `observacion:12`, más las
    ampliaciones de las aceptadas si corren en T4.
  - **La ruta:** `data/experiment/tanda1/t3/muestras/unidades_a_la_vista_T4.json`, que escribe T3 y completa T4 con las ampliaciones. Por
    muestra, da cada unidad cuya extracción aparece en el material de T4 y qué versión muestra. Entran todas, muestren la versión que
    muestren.
  - **Su sha256:** el que sellan T3 y, con las ampliaciones, T4. Hoy no existe: el despacho lo copia del FRENO que lo selle, y esta
    unidad lo controla en el commit de T5 antes de sortear.
  - Las que no son `aceptado_tras_reintento` no cambian nada, porque no están en la población.
  - **La lectura de `cid`** (después de T5) muestra solo el texto de la unidad y la página del PDF, nunca la extracción, así que no suma
    unidades. Si su material llegara a mostrar una extracción, esas unidades entran a la lista antes del sorteo de esta unidad, con su
    ruta y su sha256 en el despacho.
- **La muestra:** las 30 primeras del orden que no están en la lista de exclusión, o todas las de la población que no lo están, si son
  menos de 30.
- **Las excluidas** que caen antes de completar la muestra se declaran en el FRENO con sus ids y la muestra de T4 de cada una.
- **El orden completo** va a `NO_ABRIR_sorteo_U-MED-VERIF.json`, porque su largo es la población. El FRENO da solo su sha256.

## 4. Las fichas (diseño, §3 y §4)

1. **Las dos versiones.**
   - De la primera y de la nueva se sacan `marcas_e3` y los metadatos que no son contenido: `advertencias`, `metricas`, `rechazos`,
     `forma_salida`, `local_id` e `indice_crudo`.
   - **El control de claves:** antes de armar nada, se juntan las claves de primer nivel de las validaciones, de las entidades y de
     las relaciones de las dos versiones de toda la muestra. Si queda una clave que aparece solo en las primeras o solo en las nuevas,
     se frena y se pregunta, porque delataría cuál es cuál. El FRENO da solo los nombres de las claves.
2. **X e Y:** por unidad, X es la primera si `random.Random(f"20261015:{chunk_id}").random() < 0.5`, y si no, la nueva.
   - Los elementos de cada versión van en un orden sorteado con `random.Random(f"20261015:{chunk_id}:X")` y `…:Y`, `.shuffle`, y se
     numeran después del sorteo: `XE1`, `XE2`, … para las entidades y `XR1`, … para las relaciones; lo mismo con Y.
   - Las dos versiones se escriben con la misma función. Un elemento igual en las dos sale con los mismos bytes, salvo su número.
   - Los extremos de una relación se muestran con el número y el `label` de su entidad; el nodo del TO, como «TO»; el sujeto de
     `aplica_a` y de `ejecuta`, con `sujeto_id` o `sujeto_propuesto`.
3. **La regla C** (diseño, §3):
   - **el texto de una entidad:** `properties.descripcion`, o `termino` en una definición, o `codigo` en una comunicación, normalizado
     (minúsculas, sin tildes, sin signos y con los espacios colapsados). El nodo del TO es «TO». Si una entidad no trae ninguno de los
     tres, se usa su `label` normalizado, como en la medición de la mesa del 15/10 (lectura aprobada por la autora al firmar);
   - **el pareo de entidades:** mismo `type`; `difflib.SequenceMatcher(None, a, b).ratio()` de 0,85 o más (1 si los textos son iguales);
     los mismos números, como multiconjunto de `re.findall(r"\d+", texto)`; y la misma cantidad del token «no». Se recorren los pares
     candidatos de mayor a menor cociente, con empate por el índice en X y después en Y, y cada entidad entra en un solo par (el orden
     de los pares y las semillas del punto 2, lecturas aprobadas por la autora al firmar);
   - **las relaciones,** sin las `establecida_en`: el mismo `predicate` y los 2 extremos traducidos por el pareo de entidades. Un extremo
     sin par no coincide con nada. Se comparan como multiconjuntos;
   - **las 3 listas:** en las dos (con sus dos números, `XE3 = YE5`), solo en X y solo en Y.
4. **La ficha de la etapa 1**, una por unidad, numeradas en el orden del sorteo:
   - el número de ficha y el `chunk_id`;
   - el texto de la unidad (§2);
   - X e Y enteras;
   - las 3 listas.
   - Sin citas, sin notas del verificador, sin marcas de copia y sin estados.
   - Nada fuera del texto de la unidad y de los elementos dice «primera», «nueva», «original», «reintento» ni «re-extracción».
5. **El material de la etapa 2,** en archivos aparte que el despacho de la lectora entrega recién después del sello de su etapa 1:
   - por unidad, las citas de los faltantes que dispararon la nueva extracción: los del registro de la verificación inicial con
     `bloqueante` y `cita_verificada` (`ratchet_e3.py:283-296`; son el feedback, `:564`; lectura aprobada por la autora al firmar);
   - solo `cita_textual_del_fuente`, numeradas `C1`, `C2`, …, sin `nota`, `tipo`, `severidad` ni `ubicacion`;
   - si la unidad tiene más de un registro de la verificación inicial (reanudación, `runner_corpus.py:34-38`), tienen que traer los
     mismos faltantes. Si no, se frena y se pregunta.
6. **Las planillas en blanco**, en TSV, con una fila por pregunta:
   - etapa 1, P2: `ficha`, `chunk_id`, `elemento` (cada elemento de «solo en X» y de «solo en Y») y `marca`, con las clases «Correcto»,
     «Incorrecto», «Está en la otra versión con otra redacción» y «Dudoso»;
   - etapa 2, P1: `ficha`, `chunk_id`, `cita`, `en_X` y `en_Y`, con las clases «Está», «No está» y «Dudoso».
7. **La clave** (`NO_ABRIR_clave_versiones.json`): por unidad, qué versión es X, y por elemento, su número en la ficha y su índice en
   la lista de entidades o de relaciones de su versión. Se abre recién después de sellar las 2 pasadas de la autora (diseño, §4).

## 5. Las condiciones para empezar

1. **El commit de T5, que termina la tanda 1** (pre-registro, §5.1, `:498`), existe. El despacho da su hash y el del commit de T2.
2. **`unidades_a_la_vista_T4.json` está en ese commit,** con el sha256 que sellaron T3 y T4 (§3).
3. **Este mandato firmado.**
4. **No entra en la fila de las ejecutoras del repo:** no escribe en el repo y lee lo commiteado con `git show`, como el sorteo de las
   preguntas («Lo que no necesita el repo», en el orden de la mesa, `decisiones_107_mesa/orden/orden_ejecutoras_en_el_repo_mesa.md:37-41`,
   que la v2 de la §108 no cambió en eso; respuesta de la mesa del 15/10, §5). Puede correr mientras otra ejecutora trabaja en el árbol.
5. **El respaldo** (diseño, §2): si a las 18:00 del 21/10/2026 el commit del sello no existe, esta unidad no corre sobre la tanda 1.
   Corre sobre la población del respaldo (la tanda 0 en `2d0f5277`, `data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/`, los 5
   documentos que no son de desarrollo, 59 unidades), con un despacho propio de la mesa que fija el manifiesto, las rutas y la lista
   de exclusión: las unidades que la autora leyó en el T4 de la tanda 0 (decisión 2 al firmar, (a)). Rigen las mismas reglas, y se
   declara lo que pide el diseño.

## 6. Los criterios de aceptación

Cada uno con su comando y su salida, en la carpeta de la unidad. Ninguno imprime cifras de la población ni del contenido de las fichas:
los controles dicen OK o FRENO.
1. **El paso 0**, con la carpeta personal reemplazada por `$HOME`: `pwd` (la carpeta de la unidad, fuera del repo); los dos commits del
   despacho existen (`git cat-file -t`), con su título; y el sha256 del diseño sellado.
2. **Lo leído es lo de T2:** `git diff --quiet <commit de T2> <commit del sello> --` sobre `finales.jsonl`, `extracciones_e1.jsonl` y
   `veredictos.jsonl` de los 20 TOs.
3. **El repo no cambia:** `git status --porcelain`, el HEAD y el conteo de `.pyc` del repo, iguales antes y después.
4. **La copia del código:** 0 enlaces, 0 nombres `.env*`, `*.env` o `NO_ABRIR_*`.
5. **La regla C, con casos sintéticos,** antes de tocar la muestra:
   - dos textos iguales se parean;
   - «plazo de 30 días» y «plazo de 60 días» no se parean;
   - «las entidades deberán informar al BCRA» y «las entidades no deberán informar al BCRA» no se parean;
   - «podrán» y «deberán», con el resto igual, se parean (el límite declarado del diseño);
   - dos tipos distintos no se parean;
   - y el pareo es 1 a 1.
6. **El texto de la ficha es el de E3:** toda cita de la etapa 2 de la muestra verifica con
   `comun_e3.cita_en_fuente(cita, chunk, ratchet_e3._forma_r2(primera))` contra el chunk reconstruido. Si una no verifica, se frena.
7. **El control de claves** del §4, punto 1.
8. **Ningún rastro en las fichas ni en las planillas:** un grep de `marcas_e3`, `copia_nota`, `advertencias`, `metricas`, `rechazos`,
   `forma_salida`, `local_id`, `indice_crudo` y `nota` da 0, y el de «primera», «nueva», «original», «reintento» y «re-extracción», fuera
   del texto de la unidad y de los elementos, da 0.
9. **El mismo formato:** con un caso sintético, un elemento igual en X y en Y sale con los mismos bytes, salvo su número.
10. **Determinismo:** dos corridas completas en dos carpetas dan los mismos sha256 en todos los archivos, los `NO_ABRIR_` incluidos.
11. **El sello:** `sello_U-MED-VERIF-FICHAS.txt`, con el sha256 y la hora de cada archivo (sorteo, fichas, material de la etapa 2,
    planillas y clave), y todos en solo lectura.
12. **El grep de convenciones.**

## 7. Escrituras, prohibiciones y requisitos

- **ESCRITURAS:**
  - `$HOME/INGENIERIA IA/TESIS/fuera_del_repo/tesis_escritura/U-MED-VERIF/fichas/`, que se crea: `etapa1/`, `etapa2/`, `planillas/`, los
    dos `NO_ABRIR_`, el sello, los scripts y sus salidas;
  - su carpeta de trabajo y su scratchpad;
  - el paquete de revisión y su copia permanente (CLAUDE.md §4.g).
- **PROHIBIDO:**
  - escribir en el repo, commitear, la API y la memoria;
  - abrir un `NO_ABRIR_` que no escribió esta unidad, y abrir los suyos después de escribirlos;
  - leer lo del §2 que no necesita; mirar el desglose de E3 más allá del `estado` que define la población;
  - mostrar en el FRENO o en el paquete cifras de la población o del contenido de las fichas: cuántas unidades, elementos o citas;
  - las carpetas vedadas de los despachos, y ningún `.env`.
- **REQUISITOS:**
  - CLAUDE.md §4, de a a l;
  - primera persona, castellano técnico, cero nombres de personas;
  - USD 0, sin API.
- **TIEMPO:** de 2 a 4 h de la ejecutora (NO VERIFICADO; sin comparable directo).
- **FRENO:** «FRENO U-MED-VERIF-FICHAS», con:
  - el paso 0 y los controles, cada uno OK o FRENO;
  - las excluidas con sus ids, y de las fichas, solo «30» o «menos de 30» (decisión 1): el número queda en el sorteo sellado;
  - los sha256 y las horas del sello;
  - los errores propios, con su causa.
  - La mesa lo revisa sin abrir los `NO_ABRIR_`, y escribe después el despacho de la lectora.

## 8. Lo que no hace

- La lectura, las 2 pasadas de la autora y la adjudicación (diseño, §7).
- Las cifras y el cruce con las marcas de copia (diseño, §6).
- La superposición con L-02: se declara cuando su muestra esté sellada (diseño, §7).

## 9. Decisiones de la autora al firmar

1. **El número de fichas en el FRENO.** **Decidido: (a).** El FRENO dice solo «30» o «menos de 30», y el número queda en el sorteo
   sellado (diseño, §4: «Su FRENO no lleva conteos de la población hasta que la autora lo pida»).
2. **La lista de exclusión del respaldo.** **Decidido: (a).** En el respaldo con la tanda 0 se excluyen también las unidades que la
   autora leyó en su T4, por la misma razón del diseño. El despacho del respaldo nombra la ruta de sus ids.
3. **Dónde va este mandato firmado.** **Decidido: (a).** Al repo, en `docs/mandatos/UMED_VERIF_FICHAS_armado_de_las_fichas.md`, con un
   commit que prepara la mesa.

## Firma

FIRMADO por la autora el 17/10/2026 (por mensaje, recibido a las 22:06:54; hoja de ruta de la mesa, §149), con las opciones (a), (a) y
(a), las lecturas del §4 aprobadas y la precisión del §3. Rige desde esta firma. La unidad corre cuando se cumplen las condiciones del §5.
