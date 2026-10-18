# Mandato U-PROC-HERENCIA — C1 y C2: la procedencia de los tramos que solo vio E1, para la re-aplicación única

**FIRMADO por la autora el 18/10/2026** (firma por mensaje de la autora, recibida a las 17:01:45; hoja de ruta de la mesa, §163), sobre
la v3 para firmar (sha256 `68a3104d6eac1e95096875d2169fc71bbde72aa189d52e7b9748ba656095a54e`, en el paquete de la mesa, `decisiones_161_mesa/mandato/`), con la decisión 3 del §9 como la puso la
mesa: el id del nodo va como código. La v3 la redactó la mesa el 18/10/2026 (§159 a §161), con las dos decisiones del §9 que la autora
tomó el 18/10/2026 (recibidas a las 16:11:07) y la cláusula de cegamiento por U-MED-VERIF que pidió antes de firmar (recibida a las
16:24:10; §7 bis). Rige desde esta firma. USD 0,
sin API. No escribe en el repo. Corre cuando la extracción de la tanda final ya está corriendo (§5), la ventana que eligió la autora. El
despacho lo escribe la mesa con el commit de ese momento y las carpetas que escribe la extracción.

**De dónde sale:**
- la decisión de la autora del 18/10/2026, recibida a las 15:39:16 (§159): C1 y C2 van a la re-aplicación única, como los propuso la mesa,
  con cuatro condiciones:
  1. «La regla es una sola y se aplica igual a las tres tandas en la re-aplicación única. Nada se corrige a mano.»
  2. «La medición antes y después, sobre el acumulado de las tandas 0 y 1, trae las remisiones de la (11), la suite, las shapes y los
     conteos. Si cambia alguna remite_a, si aparece una regresión no declarada o si cambia la cantidad de nodos o de aristas, la
     ejecutora frena y me muestra los casos antes de seguir.»
  3. «Unir nodos con los de la unidad de origen espera a lo que encuentre la (3). Sacarlos, no.»
  4. La cláusula v2 de las carpetas vedadas (§7).
- las decisiones de la autora del 18/10/2026, recibidas a las 16:11:07 (§160): las dos del §9; la ventana, con la extracción corriendo; y la
  cuenta del patrón en la tanda final, que sale de C2 en la re-aplicación única y no va en el pre-registro de la tanda final;
- la cláusula de cegamiento por U-MED-VERIF de la autora del 18/10/2026, recibida a las 16:24:10 (§161; §7 bis), con la regla de exclusión
  del mandato firmado de U-MED-VERIF-FICHAS (`c0d3ab17`, §3);
- la propuesta de la mesa (§158, `decisiones_158_mesa/revision_entre_tandas/propuesta_correccion_bloques_E1_mesa.md`, en el paquete de la
  mesa) y la §31 del registro de decisiones (`8863327f`);
- la enmienda 8 al protocolo entre tandas, firmada en `54902301`: R3, la re-aplicación única (`:50-55`), y R5, el corte del grupo 2
  (`:66-69`). El grafo de cada tanda se sigue sellando sin corregir (principio 9);
- el código de HEAD, con las anclas de abajo. En `8863327f`, `ensamblar_tanda0.py` es el del commit `ded41d50`.

## 1. Qué pasa y qué hace

- **El mensaje de E1 trae toda la herencia de la unidad,** con la instrucción de no extraer de esos bloques salvo del que abre la lista
  (`data/experiment/reextraccion_v2/e1_extractor/prompt_r2b.py:346` y `:357`). **El texto de E3 trae solo los títulos, el bloque de la
  lista y el texto propio** (`data/experiment/reextraccion_v2/e3_verificador/comun_e3.py:131-160`). Los demás bloques heredados los ve
  E1 y no E3.
- **El rol documental de cada procedencia sale del punto que declara E1** (`e1_extractor/comun_e1.py:90-102`).
- **G-r ya corrige el punto y el rol** de las entidades declaradas con el punto de un ancestro: si el tramo está en el texto propio, el
  punto pasa a la unidad; si está en el bloque heredado de un ancestro, a ese ancestro, con el rol de ese bloque
  (`data/experiment/tanda0/code/ensamblar_tanda0.py:1410`, `corregir_procedencia_g_r`, con el localizador `ubicar_tramo_g_r` de `:1367`;
  se llama en `:1650`). **Salta las declaradas con el punto propio.** Esas son las de C1.
- **C1, el punto y el rol.** Es G-r extendida, con la misma función y el mismo localizador. En una entidad de uno de los tipos de G-r
  (`TIPOS_G_R`, `ensamblar_tanda0.py:1363`; decisión 1 del §9), declarada con el punto propio, cuando se cumplen las tres condiciones:
  1. el tramo, normalizado con `comun_e3.normalizar_para_cita` (`comun_e3.py:226`), no está en el texto de E3 de la unidad
     (`comun_e3.fuente_integro(chunk, bloque_de_lista=True)`);
  2. `ubicar_tramo_g_r` lo ubica como `parrafo` en el bloque heredado de un ancestro;
  3. ese bloque no es el que abre la lista (`comun_e3.indices_bloque_lista`, `comun_e3.py:111`);

  entonces:
  - el punto pasa a ser el de ese ancestro, y el rol, `herencia_<tipo del bloque>`, como hace G-r con las declaradas con un ancestro;
  - lo que declaró E1 queda en dos campos nuevos de la procedencia, `punto_declarado_e1` y `rol_declarado_e1`;
  - el `chunk_id` no cambia: en una procedencia de herencia es la unidad que extrajo, por la convención del ensamblado. Las páginas y los
    ancestros los rehace `enriquecer_procedencias_r2` (`:1220`) como en toda procedencia de herencia.
- **C2, la marca.** `tramo_fuera_del_texto_de_e3: true` en la procedencia, en el `kg.json`. Va cuando se cumplen las dos condiciones:
  1. el tramo cumple la condición 1 de C1;
  2. el tramo está, normalizado igual, en un bloque heredado que no es un título ni el que abre la lista.

  Vale para todo tipo y todo punto declarado, después de G-r y de C1.
- **La cuenta de C2 en la tanda final** la informa la re-aplicación única, cuando la prende sobre el acumulado de las tres tandas. Es la
  cuenta del patrón en la tanda final, que no va en su pre-registro (decisión de la autora del 18/10/2026).
- **La bandera:** las dos van detrás de un parámetro nuevo, `procedencia_heredada`, apagado por defecto, en `correr_cadena_r2` (`:1596`),
  en `ensamblar_manifiesto_r2` (`:1892`) y en la línea de comandos (`--procedencia-heredada`). Siguen el modelo de `cat_resolucion` y
  `--catalogo-resolucion` (`:2019`): sin la opción, el ensamblado es el de siempre. Así:
  - el grafo de cada tanda, también el de la tanda final, se arma y se sella sin la corrección (principio 9);
  - la re-aplicación única la prende para el acumulado de las tres tandas.
- **Una sola regla:** el código no nombra ninguna unidad, ningún nodo ni ningún TO, y es el mismo para las tres tandas. Cada tanda usa su
  propia E0. Nada se corrige a mano.
- **Lo que no hace:**
  - no saca ni une ningún nodo. Unir con el nodo de la unidad de origen espera a lo que encuentre la (3);
  - no toca el prompt, E3, las salidas de E1 y E3, las cachés ni ningún grafo sellado.

## 2. Las fuentes

Todas desde el commit que da el despacho, leídas en la copia (§7):
- el código: `tanda0/code/ensamblar_tanda0.py`, `reextraccion_v2/e3_verificador/comun_e3.py` y `reextraccion_v2/e1_extractor/comun_e1.py`;
- la cadena del T3 de la tanda 1: `data/experiment/tanda1/t3/scripts/cadena_t3.sh` (los grafos `acum_treinta` y `acum_treinta_sincola`)
  y `gate_t3.sh` (shapes y suite);
- los dos `kg.json` del acumulado de las tandas 0 y 1, restaurados en la copia desde su `.gz` con `scripts/kg_gz.py restaurar`. Tienen
  que dar el sha256 de su sello: `0435d41f9c7b…` el sin cola y `e63536d1…` el con cola;
- el selftest de la clave de la caché: `data/experiment/mantenimiento/code/selftest_clave_cache.py`, con la variación R19;
- para el cegamiento (§7 bis), lo que dé el despacho: si la muestra de las FICHAS ya está sorteada y, si lo está, las rutas y los sha256
  de su sorteo y de su lista de exclusión.

## 3. La medición, antes y después

Sobre la copia, para `acum_treinta` y `acum_treinta_sincola`:
1. **Antes:** el ensamblado con el código entregado y la bandera apagada. Tiene que dar el `kg.json` de su sello byte a byte. Si no, frenás.
2. **Después:** el mismo ensamblado con `--procedencia-heredada`.
3. **Lo que comparás,** con su script y su salida:
   - **las remisiones de la (11):** el conjunto de las aristas `remite_a` (origen, destino y procedencia), antes y después.
     `detectar_y_resolver` (`:1728`) lee el texto del punto de la procedencia (`corpus_v2/r1_referencias.py:911-934`);
   - **la suite** (`gate_t3.sh`, `suite`): antes y después, con las regresiones declaradas al lado (RT-C5-3, RT-C6-1 y RT-C6-2; E4-a1 y
     E4-a4, BKL-0048);
   - **las shapes** (`gate_t3.sh`, `shapes`): antes y después, regla por regla;
   - **los conteos:** nodos y aristas, por tipo y por predicado. `derivar_establecida_en` (`:1742`) también lee la procedencia;
   - **lo que cambió:**
     - cada procedencia que tocó C1, con la unidad, el código del nodo, el punto y el rol de antes y de después (§7 bis, punto 2);
     - cuántas marca C2, por tanda;
     - las que cumplen la condición 1 y el tipo de C1 pero no las otras dos, cada una con el lugar que da `ubicar_tramo_g_r`.
4. **Frenás y mostrás los casos antes de seguir** (condición 2 de la autora), con la regla del §7 bis, en cuatro casos:
   - si cambia alguna `remite_a`;
   - si aparece una regresión no declarada;
   - si cambia la cantidad de nodos o de aristas;
   - si cambia una regla bloqueante de las shapes.
5. **Lo que espera la mesa,** medido en la §158 con `normalizar_para_cita` y no con el localizador del validador:
   - C2: 134 procedencias, 65 de la tanda 0 y 69 de la tanda 1;
   - C1, con los tipos de G-r (decisión 1): 71, 32 de la tanda 0 y 39 de la tanda 1. Las 5 Comunicacion declaradas con el punto propio
     quedan fuera de C1, y C2 las marca.

   Si tus cuentas difieren, listás en el FRENO, una por una y con la forma del §7 bis, punto 2, las procedencias de la diferencia. La
   mesa las cruza con su medición, por el código del nodo.

## 4. El selftest y la tabla

- **`data/experiment/proc_herencia/selftest_procedencia_heredada.py`, una rama por caso,** sobre unidades armadas a mano en el selftest,
  sin datos del corpus:
  - declarada con el punto propio y con el tramo solo en un párrafo heredado de un ancestro: C1 cambia el punto y el rol, guarda lo
    declarado, y C2 marca;
  - el tramo en el texto propio, en un título, en el bloque que abre la lista o en ninguna parte: ni C1 ni C2;
  - sin tramo;
  - un mini-chunk;
  - una Comunicacion, que está fuera de `TIPOS_G_R`: C1 no cambia nada y C2 marca;
  - declarada con un ancestro: G-r como siempre, y C2 marca si corresponde;
  - con la bandera apagada: la salida de G-r de HEAD, igual.
- **R19:** `selftest_clave_cache.py`, sobre la copia, da lo mismo que con el código de HEAD. Si el código de C1 y C2 va en un módulo nuevo,
  lo sumás a `MODULOS_SOLO_CODIGO_R2` (`selftest_clave_cache.py:178`).
- **La fila de la tabla de reprocesamiento** (`data/experiment/mantenimiento/tabla_reprocesamiento.md`), después de F15e. Va con este
  texto, y en «Ancla», las líneas de la función, del parámetro y de su llamada en el código que entregás:

  `| F15f | Procedencia de un tramo que solo vio E1 (C1 y C2, U-PROC-HERENCIA): el punto y el rol de una entidad declarada con el punto propio cuyo tramo está solo en un bloque heredado que E3 no ve, y la marca tramo_fuera_del_texto_de_e3 | ensamblado r2, sobre el crudo guardado, con --procedencia-heredada (apagada por defecto: sin ella, el ensamblado de siempre) | E2, remisiones y lo que sigue, en código | no cambia | no cambia | solo código sobre lo guardado | 12 | … | R19 |`

## 5. Las condiciones para empezar

- **Paso 0, con la carpeta personal reemplazada por `$HOME`.** Pegás la salida en el FRENO; si algo da otra cosa, frenás sin escribir:
  - `pwd`, y `git --no-optional-locks log -1 --format='%h %s'`: el commit es el que da el despacho;
  - la extracción de la tanda final está corriendo y es la única ejecutora en el repo. Vos no escribís en él.
- **No arrancás** si el despacho no lo dice. El despacho va después de su T1 y del «seguí» a su T2. No arrancás tampoco durante el
  segundo tramo de T4, T5, FICHAS o el despacho de la tanda final.
- **La copia:**
  - excluye las carpetas que escribe la extracción de la tanda final, que nombra el despacho;
  - controlás, archivo por archivo, que cada archivo que usás tenga el blob de HEAD (`git hash-object` contra
    `git --no-optional-locks ls-files -s`). Los dos `kg.json`, restaurados desde su `.gz`, dan el sha256 de su sello.

## 6. Los criterios de aceptación

1. El selftest pasa todas sus ramas, y R19 da lo mismo que en HEAD.
2. Con la bandera apagada, los dos `kg.json` del acumulado salen byte a byte iguales a sus sellos.
3. La medición del §3 está entera, con cada cifra al lado de su script y de su salida. Si se dio alguno de los cuatro casos del §3,
   punto 4, el FRENO muestra los casos y no sigue.
4. El código no nombra ninguna unidad, ningún nodo ni ningún TO: un grep de `::` y de los ids de los TOs sobre el diff da 0.
5. La fila F15f está con sus anclas.
6. El grep de convenciones del CLAUDE.md, §5, sobre todo lo que entregás, da 0. Lo pegás aunque dé vacío.

## 7. Escrituras, prohibiciones y requisitos

- **Escribís solo** en tu scratchpad y en la copia permanente de tu paquete. Al repo no, y no commiteás.
  - El código entra después, con el commit de la autora, entre ejecutoras y después del sello de la tanda final.
  - Lo usa la re-aplicación única, que tiene su propio mandato.
- **Copias del repo sin `.env` ni `NO_ABRIR_`:**
  - la copia va con
    `rsync -a --no-links --exclude=/.git --exclude=/.venv --exclude=/.venv-app --exclude=.DS_Store --exclude=__pycache__ --exclude='.env' --exclude='.env.*' --exclude='*.env' --exclude='NO_ABRIR_*' <repo>/ <copia>/`,
    más las exclusiones del §5;
  - el control (`find` de los cuatro nombres y de los enlaces) da 0 antes de correr nada. Si no da 0, frenás y borrás esos archivos por
    nombre, sin abrirlos;
  - nunca un `git clone` para correr algo, y los `.env` no se abren nunca;
  - los selftests y la cadena corren sobre la copia (CLAUDE.md, §4.l).
- **Carpetas vedadas** (cláusula v2 del 18/10/2026):
  - en `~/INGENIERIA IA/TESIS/fuera_del_repo/`: `adjudicacion_s1ter/`, `adjudicacion_s1quater/`, `correccion_E0/`, `lecturas_ciegas/`,
    `lectura_lote2/`, `respaldo_memoria/`, `NO_ABRIR_evidencia_adjudicacion_s1quater/` y
    `scratchpads/7f2f135f-40fb-45a2-bde1-6cddd2868d0e/`;
  - las carpetas de lectura de la autora: `gold_q12_ajuste/`, `lectura_alcance_tf/`, `lectura_desamb/`, `lecturas_1710/` y
    `lectura_calibradores_desamb/`;
  - y `~/Desktop/traspaso_etapa2/`;
  - el paquete de la mesa tampoco se abre: lo que necesitás está en este mandato;
  - una búsqueda que pueda recorrerlas las excluye.
- **Lo que no abrís:** ningún `NO_ABRIR_`, salvo los dos de las FICHAS del §7 bis, punto 3, y solo en memoria. Tampoco ninguna clave
  aparte ni la transcripción de ninguna sesión lectora. No escribís en la memoria.
- **Los heredocs** van siempre con el delimitador entre comillas.
- **Checkpoint:** antes de una compactación, escribís en tu scratchpad qué hiciste, qué falta, qué archivos tocaste y qué quedó abierto, y
  das la ruta.

## 7 bis. El cegamiento por U-MED-VERIF

Cláusula de la autora del 18/10/2026, recibida a las 16:24:10 (§161). La medición toca unidades de la tanda 1, y el FRENO puede llegar
después del sorteo de las FICHAS de U-MED-VERIF, mientras la autora lee esa muestra. Si ve la extracción de una unidad de la muestra, esa
lectura deja de ser a ciegas para ella.

1. **Nada por estado de E3 ni de los reintentos.** El FRENO y el paquete no dan ninguna cifra ni lista por estado de E3, ni nada de los
   reintentos (`n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las marcas de E3). Las cuentas van por tanda y, si hace
   falta, por TO o por tipo de nodo.
2. **Cada procedencia, sin contenido.** En el FRENO y en el paquete, cada procedencia va con su unidad, el código del nodo, el punto y el
   rol, de antes y de después. Nunca van el label, la descripción ni el tramo.
   - El id del nodo tampoco va tal cual. Lleva el tipo y un trozo del texto del nodo (la convención de `ensamblar_corpus.py:7-13`; por
     ejemplo, `Condicion_cliente_no_persona_humana_residente__…`).
   - Va como código: los primeros 12 caracteres hexadecimales del sha256 del id, en UTF-8. La tabla código → id va solo a
     `NO_ABRIR_codigos_de_nodos_U-PROC-HERENCIA.json`, en el paquete (decisión 3 del §9).
3. **Antes de mostrar cualquier contenido de una extracción de la tanda 1** (el label, la descripción, el tramo, el id, las aristas o las
   remisiones de un nodo; por ejemplo, en un caso del §3, punto 4), aplicás la regla de exclusión de las FICHAS (`c0d3ab17`, §3):
   - **si la muestra todavía no está sorteada** (lo dice el despacho), las unidades de ese contenido entran a la lista de exclusión
     antes del sorteo:
     - las listás en `unidades_a_la_vista_U-PROC-HERENCIA.json`, con cada unidad y qué se mostró;
     - su sha256 va en el FRENO;
     - la mesa las suma al despacho de las FICHAS y controla, sin ver su tamaño, que la población siga dando 30;
   - **si ya está sorteada,** armás la muestra en memoria: las 30 primeras del orden del sorteo que no están en su lista de exclusión.
     - El sorteo y la lista son los dos `NO_ABRIR_` que nombra el despacho. Son los únicos que abrís, y solo para esto.
     - Una unidad de la muestra no muestra nada: su caso va a `NO_ABRIR_casos_en_espera_U-PROC-HERENCIA.json` y espera a que cierre la
       lectura de U-MED-VERIF.
     - No escribís la muestra en ningún archivo, no la imprimís y no das ni su tamaño ni sus ids;
   - **las unidades de la tanda 0** no están en la población de U-MED-VERIF: su contenido se muestra sin esta regla.
4. **De los casos en espera, el FRENO dice solo sí o no:** si hay casos en espera, y si alguno cae en un caso de freno del §3, punto 4. No
   dice cuántos ni cuáles.
5. **Si un caso en espera frena la corrección** antes del corte del sábado 24 a las 12:00, frenás y avisás sin mostrar la extracción. La
   autora y la mesa lo resuelven.
6. **La revisión de la mesa** sigue la misma regla: no le muestra a la autora contenido de una extracción de la tanda 1 sin aplicarla, y
   no abre los `NO_ABRIR_` de este paquete.

## 8. Cómo terminás

- **El paquete `revision_U-PROC-HERENCIA/`** en tu scratchpad, con su `manifest.txt` (sha256 y una línea por archivo, con nombres únicos).
  Lleva:
  - el `ensamblar_tanda0.py` entregado y su diff contra HEAD;
  - el selftest y su consola;
  - la consola de R19;
  - las salidas y las consolas de la medición, y la fila F15f.
- **Su copia** con `ditto` en `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/<id de tu sesión>/scratchpad/revision_U-PROC-HERENCIA/`,
  con los sha256 del manifest verificados en la copia.
- **El FRENO** (`FRENO_U-PROC-HERENCIA.md`, en el paquete):
  - el paso 0 y la medición del §3, con cada cifra junto a su script;
  - el cegamiento (§7 bis): la rama que rigió (muestra sorteada o no), el sha256 de `unidades_a_la_vista_U-PROC-HERENCIA.json` si
    corresponde, y el sí o no de los casos en espera;
  - los criterios del §6, uno por uno;
  - los casos, si los hay;
  - los errores propios, con su causa;
  - la ruta de la copia y su verificación.
- Esperás la revisión de la mesa y, si hay casos, la decisión de la autora.

## 9. Decisiones de la autora

Tomadas el 18/10/2026, recibidas a las 16:11:07 (hoja de ruta de la mesa, §160), sobre la v1:
1. **Los tipos de C1:** la (a), los de G-r (`TIPOS_G_R`, `ensamblar_tanda0.py:1363`): 71 procedencias en el acumulado. Es la misma regla
   que G-r, y una Comunicacion no es un tipo de contenido para el ensamblado (`TIPOS_SIN_CONTENIDO_A`). C2 marca las de todos los tipos.
2. **Los nombres:** `tramo_fuera_del_texto_de_e3` para la marca, y `punto_declarado_e1` y `rol_declarado_e1` para lo que declaró E1.

Tomada al firmar la v3, el 18/10/2026 (recibida a las 17:01:45; §163):

3. **El id del nodo en el FRENO, como código** (§7 bis, punto 2). El id lleva un trozo del texto del nodo, así que muestra parte de la
   extracción: en el FRENO va el código, como lo puso la mesa.

## Firma

**FIRMADO por la autora el 18/10/2026,** por mensaje recibido a las 17:01:45 (hoja de ruta de la mesa, §163): «U-PROC-HERENCIA: firmo la
v3 (decisiones_161_mesa/mandato/UPROC_HERENCIA_procedencia_de_tramos_heredados_v3_PARA_FIRMAR.md), con la decisión 3 como la pusiste: el
id del nodo va como código.» El texto firmado es el de la v3 (sha256 `68a3104d6eac1e95096875d2169fc71bbde72aa189d52e7b9748ba656095a54e`), con este encabezado y esta sección. El despacho lo escribe
la mesa cuando la extracción de la tanda final ya corre (§5).
