FIRMADO por la autora el 05/10/2026 (firma por mensaje de la autora; versión para firmar en `1d8fe9f`, sobre el borrador de `f959beb`)

MANDATO — U-REEXT-T0: RE-EXTRACCIÓN DE LOS DIEZ TOs DE LA TANDA 0 CON EL PERFIL r2b, GATE DE r2b Y PRIMERA
LECTURA DE LA COLA HUMANA.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar, y docs/decisiones_caching_extraccion.md antes de
tocar cualquier llamada al modelo: sus cinco decisiones son vinculantes.
- Unidad en CINCO ETAPAS, T1 a T5, con FRENO obligatorio al final de cada una: reporte corto (no más de 40
  líneas) y espera del «seguí» escrito de la autora.
- Costo de API: solo en T2, con tope de USD 80 para E1 a E3 de los diez TOs (decisión de la autora del
  05/10/2026, tras el FRENO P5 de U-PROMPT-R2; antes era USD 72, y antes, 69; docs/plan_tesis.md:400). Fuera
  de T2, USD 0 y ninguna llamada a la API. Si la proyección de T2 pasa el tope, se frena y se reporta: el
  tope no se sube solo.
- Plataforma y modelos: la API de Anthropic para E1 y para E3, en toda la release r2b (decisión de la
  autora del 05/10/2026). E1 corre con `claude-haiku-4-5` y temperatura 0, y E3, con `claude-sonnet-5`
  (`corpus_v2/runner_corpus.py:89-94`). Esta unidad no cambia la plataforma, el cliente ni un modelo.
- PRECONDICIONES, todas commiteadas por la autora. Si falta alguna, frená sin escribir.
  - De U-PROMPT-R2: P4, la pareada (`2ed47a0`); P3c-1, el diseño del ajuste (`438bbd5`); P3c-2, el prefijo
    re-congelado y los candados de F04b, F22, F22b y F23 (`66cde30`); la corrección de la clase modalidad
    del contador (`bb212f1`); P4b, la prueba corta (`046e493`); y P5, la etapa que fija la temperatura de
    E1 (decisión de la autora del 05/10/2026; `53b7708`).
  - De U-R2-CODIGO-2: el cierre de C2, con el código y `salida_tanda0_r2b/` (`9f6361e`).
- Código: el del pipeline es el del commit de P5 de U-PROMPT-R2, que sobre `bb212f1` cambia solo la
  temperatura del pedido. El prefijo no recibe otro ajuste antes de esta unidad (decisión de la autora del
  05/10/2026, tras el FRENO P4b).
- Caché: las bases de P4 y de P4b de U-PROMPT-R2 no se reutilizan en esta unidad (decisiones de la autora
  del 04/10/2026). Las de P5 tampoco: T4 compara la respuesta de esta unidad con las de P5.
- Corpus: el congelado. No se actualiza ningún PDF (decisión de la autora del 02/10/2026, plan `:400`).

CONTEXTO, con sus anclas.
- Qué es: E1 a E3 de los diez TOs de la tanda 0 (pro, cla, ric, cap, ext, ctacte, lingob, polcre, pagjub y
  docvig) con el prefijo nuevo, sobre la e0-r2 que deja C2, y sus ensamblados r2b. Es la release r2b: de ella
  dependen la tanda 1 (docs/checklist_pre_escalado.md:60-66) y la columna «r2b» del tablero
  (docs/tablero_correcciones.md, 26 filas).
- Manifiestos r2b: data/experiment/reextraccion_v2/manifiestos/tanda0_10tos_r2b.json,
  tanda0_ens_diez_r2b.json y tanda0_ens_desarrollo_r2b.json (`20b7f60`). Hoy apuntan a
  `e0_chunking/salida_tanda0_r2`, el primero trae el tope anterior, de USD 69, y sus `sellos` están vacíos.
- Referencias de costo: E1 a E3 de los diez TOs con el prefijo sellado costó USD 40,35 (plan `:400`). Con
  el prefijo de P3c (`322c5a23e9b7`) y temperatura 0, la re-estimación de P4 con los cocientes que midió P5
  (salida 0,947 y 0,957, y entrada 1,026, de las del prefijo de P3b-2) da una central de USD 44,70, con la
  salida ponderada por estrato, a 48,97, sin ponderar; con el tercer escalón, de 45,06 a 49,93; y por el
  factor 1,4, de 63,93 a 69,91 (data/experiment/prompt_r2/p5/salida/costo_p5.json). Sin temperatura fijada,
  P4b daba hasta 67,83. Es una cota: las 27 unidades se eligieron por lectura y son cortas (22.166
  caracteres de texto propio entre todas). El tope de 80 deja USD 10,09 sobre la cota más alta: con 72
  quedaban 2,09, menos que la diferencia entre dos mediciones de las mismas unidades (P5 midió un 7 % más
  de salida que P4b). El runner frena en cada checkpoint si la proyección del total pasa el tope.
- Gate: docs/laudo_release_r2_pipeline.md, §3.1 (puntos 1 a 8), y docs/protocolo_entre_tandas.md, §1 y §4,
  con su enmienda 3 sobre las clases de reprocesamiento
  (docs/enmienda3_protocolo_entre_tandas_2026-10-04_clases_de_reprocesamiento.md, FIRMADA el 04/10/2026).
- Textos firmados que rigen acá: L-ESQ-R2 (`4ef7650`) con sus enmiendas 2 (`5f9a731`), 3 (`8d01b04`), 4
  (`5c58f38`), 5, sobre la negación y el comparador pegado a la cuantía (`3a4b980`), y 7, sobre la regla 9
  (`44c6e1b`, con su nota posterior a la firma); y la enmienda al protocolo sobre la cola humana
  (`8d01b04`) con su nota (`0b98045`). La enmienda 6 a L-ESQ-R2 está en BORRADOR y no rige.
- La temperatura y la variación del modelo (decisiones de la autora del 05/10/2026).
  - Hasta P4b, E1 y E3 corrieron sin temperatura fijada: ningún pedido llevaba `temperature`, `top_p` ni
    `top_k`, y regía el valor por defecto del proveedor, que la documentación del SDK instalado da en 1,0
    (anthropic 0.100.0, `resources/messages/messages.py:266-273`). Los tres pedidos de P4b que ya estaban en
    la base de P4 son idénticos byte a byte, con la misma clave, y dieron respuestas distintas: en
    `cla::5.1.1.1`, sin la Excepcion en P4 y con ella en P4b; en `cap::6.2.2.6`, 17 normas y 5.236 tokens de
    salida en P4, y 1 norma y 1.590 tokens en P4b.
  - Con el perfil r2b, E1 corre con temperatura 0, fijada en el pedido, y el reintento por salida mal
    formada (namespace `-rforma1`), con temperatura 1, para obtener una respuesta distinta
    (`e1_extractor/prompt_r2b.py:109-110`; P5 de U-PROMPT-R2). La temperatura 0 no vuelve determinística la
    respuesta: en P5, de las 27 unidades pedidas dos veces, 6 respuestas salieron idénticas, 5 difieren solo
    en la redacción y 16 en algún conteo, y la marca de lectura cambia en 4 de 27.
  - E3 corre sin temperatura fijada, y su variación es un límite declarado (decisión de la autora del
    05/10/2026). Su modelo, `claude-sonnet-5`, rechaza con un error 400 un valor de `temperature`, `top_p` o
    `top_k` distinto del de por defecto (https://platform.claude.com/docs/en/models/sonnet-5/overview,
    consultada el 05/10/2026; en P5 la API devolvió ese error), y no se cambia. En P5, sobre 10 unidades
    verificadas dos veces, el veredicto coincidió en las 10 y la evaluación en 9: en una, la severidad de un
    mismo reclamo decide distinto si la unidad reintenta.
  - El grafo es reproducible por la caché, no por el modelo.
  - Consecuencias para esta unidad:
    - cada unidad se extrae una vez;
    - esta unidad no cambia el modelo ni los parámetros del pedido, y no vuelve a extraer una unidad para
      que un control dé: lo que el pipeline reintenta es lo que reintentan su código y su ratchet.
- Lo que P4b dejó sin mejorar, y se mide acá (decisión de la autora del 05/10/2026;
  data/experiment/prompt_r2/freno_p4b.md): las listas que exceptúan, en sus dos tipos (b1 y b2: ninguno de
  tres en cada brazo); una Condicion por supuesto (grupo c); y las omisiones `meta_normativo` con contenido
  normativo, sobre todo las que copian el texto heredado de un encabezado o de un cierre (6 de 12 con el
  prefijo de P3c). Con la cifra de esta unidad, cada una se corrige en código entre tandas o se declara
  como límite. Por el protocolo entre tandas, §6 (decisión D1), el prefijo ya no cambia durante el escalado.
- Efecto esperado del punto e de P3c: bajan las normas con `aplica_a`, porque el extractor ya no nombra un
  sujeto que el texto no nombra. En el crudo de P4b, 36 de 54 normas con el prefijo de P3b-2 y 19 de 42 con
  el de P3c; fuera de las 4 unidades del grupo e, elegidas porque su texto no nombra al sujeto, 29 de 47 y
  19 de 36. En P4, 129 de 143 con el prefijo sellado y 111 de 157 con el de P3b-2. Lo que se pierde se
  recupera con la parte B de la enmienda 6 a L-ESQ-R2, si llega a regir.
- Menciones que el texto no trae. Con temperatura 0, en P5, vuelven: verifican 32 de 35 y 32 de 40
  menciones de sujeto, contra 26 de 26 en P4b; las 11 que no verifican dicen «las entidades». Las normas con
  `aplica_a` son 28 de 49 y 33 de 50. La enmienda 6, en BORRADOR, pasa a tratar esas menciones como
  relaciones sin mención (decisión de la autora del 05/10/2026). Hasta su firma rige la regla de hoy: las
  resuelve la sugerencia del modelo.

T1 — PREPARACIÓN EN SECO Y SUITE (USD 0).
1. Manifiestos r2b: `rutas.e0_salida` pasa a data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/;
   los sellos, a los del prefijo re-congelado; y el tope global, a USD 80. Es el primer paso de la unidad
   (decisión de la autora del 04/10/2026).
2. Control de las entradas, cada una contra su valor de «Lo que llega de las unidades anteriores»: el hash
   y el sha256 del prefijo y el del tool schema; el namespace de E1; el prefijo y el namespace de E3; los
   57 archivos de `salida_tanda0_r2b/` contra los del commit de C2; el candado del catálogo; la temperatura
   del pedido de E1 (0) y la del reintento por salida mal formada (1); y el código: entre el commit de P5
   y el HEAD de la corrida no cambió ningún archivo de la cadena de E0 a E5, de los validadores ni de los
   perfiles (`git diff --stat 53b7708 HEAD`, sobre esas rutas, vacío).
   - Candados de los insumos que no entran al hash del prefijo (decisión de la autora del 04/10/2026): la
     lista de tablas forzadas a residual (F04b), las líneas fijas del mensaje de E1 (F22 y F22b) y las
     NOTAS de E3 (F23). Los puso P3c-2 de U-PROMPT-R2. T1 solo los verifica: que los módulos cargan con sus
     sha256 esperados y que en el selftest de claves las variaciones R29, R29b, R30 y R32 dan «frena».
   - `e1_extractor/selftest_prompt_r2b.py` lee `salida_tanda0_r2/` y exige que ninguna unidad lleve
     `herencia_recortada` (`:146` y `:200-201`). Al pasar a `salida_tanda0_r2b/`, ese caso cambia: la única
     unidad con el recorte es `ric::11.2.3`, y su mensaje lleva la línea del recorte una vez. El archivo se
     suma a las escrituras de la unidad solo para ese caso.
   - Los scripts de `data/experiment/medicion_r2a/` que importan `reglas_comparacion` o `r1_referencias`
     dan otras cifras con el código de C2. No se vuelven a correr acá: sus salidas selladas son de r2a.
   - Rol de alcance: nueve de los diez TOs lo tienen en `rol_por_to_r2.json` (seis con rol propio y tres con
     clase). Docvig no lo tiene, por el laudo de B5.4 (`docs/laudo_B5.4_fase1_catalogo.md:20-22`): se extrae
     sin línea de alcance, como en r2a, y se declara. En r2a tuvo 20 relaciones con sujeto, 17 resueltas por
     la sugerencia del modelo y 3 en cuarentena.
   - Unidades grandes de `salida_tanda0_r2b/`, para la corrida en seco: `cap::4.2.1.2` (26.726 caracteres
     propios), `ric::11.2::intro` (15.051), `cap::3.1.14.1` (12.101) y `cap::4.3.3.1` (10.981). Con el
     prefijo sellado, las tres de cap dieron 11.925, 8.371 y 9.212 tokens de salida: superan los 8.192 del
     primer intento y entran en el reintento de 16.384. Si alguna corta también en el reintento, solo
     `cap::4.2.1.2` se puede partir por ítems; lo que no se puede partir, y las partes que cortan, van al
     tercer escalón, con techo de 40.960 tokens.
     Con la salida que midió P4 con el prefijo de P3b-2 (1,175 tokens por carácter de texto propio: mediana
     de 6 unidades de 3.109 a 9.825 caracteres, de 0,224 a 1,498), en el reintento entran unos 13.944
     caracteres, y 10.937 con el máximo. Por esa cuenta quedan fuera `ric::11.2::intro`, que no se puede
     partir, y `cap::4.2.1.2`: se parte en dos, de 15.056 y 11.669 caracteres, la parte mayor también pasa
     de 13.944 y una parte no se vuelve a partir. Las otras dos quedan en el borde. Es una cota: la razón
     baja con el tamaño (con el prefijo sellado, las tres de cap dieron 0,46, 0,69 y 0,84). Por su salida
     sellada y el crecimiento medido en P4 (×1,276 en el conjunto y hasta ×1,58 en las unidades de 3.000
     caracteres o más, sin `ric::9.2.1`), `cap::4.2.1.2` daría entre 15.200 y 18.900 tokens. P4b y P5
     midieron unidades cortas y no cambian esta cota: con temperatura 0, la salida de P5 fue 0,947 y 0,957 de
     la del prefijo de P3b-2. La salida de un mismo pedido varía: sin temperatura fijada, de 5.236 a 1.590
     tokens en `cap::6.2.2.6`; con temperatura 0, las dos corridas de P5 sumaron 43.424 y 43.872. La corrida
     en seco lista las cuatro, con el mecanismo que cubre a cada una.
3. Corrida en seco, sin llamar a la API: el request de cada unidad, su namespace y su clave de caché; las
   unidades por TO; la estimación por TO contra el tope; los namespaces de los reintentos.
   - Control contra P5: la clave de cada una de las 27 unidades de P4b se compara con la que dejó P5 de
     U-PROMPT-R2 con temperatura 0 (data/experiment/prompt_r2/p5/salida/claves_despues.json). Se espera que
     coincidan las 27, y que ninguna sea la del brazo de P3c de P4b, que corrió sin temperatura fijada. Si
     alguna difiere de la de P5, se reporta con su causa en el FRENO T1: o cambió algo del pedido desde P5, o
     el runner arma el pedido de otra forma que su script.
4. Suite y shapes antes del gate:
   a. T6 y E4-b se parametrizan por los TextoOrdenado de los TOs del manifiesto del grafo bajo prueba, en
      lugar de los cinco de desarrollo fijos (scripts/regression_kg.py:1304-1313; E4-b depende de T6);
   b. la shape informativa «cuantía en la descripción ⇒ elemento en la lista» (L-ESQ-R2 §1.5);
   c. la entrada de la suite que fija las dos firmas nuevas de `condicion_de` (→ Operacion y → Potestad),
      con el conteo de relaciones no verificadas por E3, que tiene que ser 0 (L-ESQ-R2 §6.5);
   d. una entrada por cada id nuevo decidido, leída contra su chunk (L-ESQ-R2 §7.5);
   e. el control que exige cero elementos de extracción sin verificar, con la especificación del FRENO P3 de
      U-PROMPT-R2 (data/experiment/prompt_r2/freno_p3.md, A3, seis puntos; `4aa92c7`). Lee el conteo del
      reporte del ensamblado r2b (punto s de C2). La cola humana es la excepción explícita y se cuenta aparte.
   f. un test por punto para `BKL-0001` (`cap::2.8.3.3`) y para `BKL-0002` (`ext::3.5.3`), como T1 lo es de
      `BKL-0024`: el contenido que tiene que estar sale del expediente del retriage
      (data/backlog/expediente_retriage_v3.md, E1 y E2). Decisión de la autora del 04/10/2026.
   Los selftests de la suite y de las shapes corren sobre una copia. En las entradas ya selladas de la
   fixture cambian solo T6 y E4-b.
5. Entrada de la suite para los grafos r2b: el estado esperado, ítem por ítem, propuesto para que la autora
   lo selle ANTES del gate de T3 (laudo de r2, §3.1, punto 2). `BKL-0004` (la enumeración del 6.5 de
   Clasificación) persiste en r2a sin corrección dirigida: si persiste en r2b, entra al estado esperado como
   falla conocida, con su evidencia.
6. Las 15 preguntas de control: un script versionado que repite el procedimiento de la revisión independiente
   (reports/u_revision_libre/freno_a.md:70-72; `54f57cd`). Primero reproduce su resultado sobre
   KG-Tanda0-Diez-r2a: 8 bien, 2 en parte, 3 con algo falso y 2 sin respuesta. Si no lo reproduce, se declara
   la diferencia pregunta por pregunta.
7. Lo que T4 lee, sellado antes de T2, con su sha256 y su hora. Nada de esto mira una extracción.
   a. Las 27 unidades de P4b: ya están selladas (data/experiment/prompt_r2/p4b/salida/seleccion_p4b.json,
      sha256 `e2551cf3…`).
   b. Las listas de b1 y de b2 de la tanda 0 que las lecturas anteriores ya identificaron, once, cada una
      con su tipo (b1, lo que queda afuera de una clase; b2, las condiciones de una sola excepción) y con la
      lectura de donde sale: la del ejemplo (`cla::5.1.1`); las cuatro que P4 dejó aparte por ser las
      condiciones de una sola excepción (`ext::3.5.4`, `ext::2.6.1`, `ext::7.8.4` y `ext::2.7`;
      data/experiment/prompt_r2/p4/estrato_listas_excepciones.md); las dos de P4b (`ctacte::3.2`, con su
      lectura dudosa declarada, y `ext::3.5.3`); y las cuatro que P4b excluyó por leídas antes
      (`ext::3.13.1`, `ext::3.6.1`, `ext::3.6.4` y `ext::10.11`;
      data/experiment/prompt_r2/p4b/seleccion_p4b.md). No se buscan listas nuevas.
   c. El orden sorteado del grupo c, con la definición de forma del pool c de P4b (una cuantía y al menos
      dos marcas de supuesto en el texto propio; data/experiment/prompt_r2/p4b/seleccion_p4b.py, `pools`),
      sobre toda la tanda 0 y sin las exclusiones de P4b. Semilla declarada.
   d. Las semillas de los sorteos de T4 que dependen de la salida de T2 (las omisiones `meta_normativo`).
FRENO T1.

T2 — EXTRACCIÓN, E1 A E3 (tope USD 80).
- Perfil r2b, los diez TOs, en el orden del manifiesto. Salida nueva en
  data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/ (se crea).
- Con lo que traen P3b-2, C2 y P3c-2: el reintento por salida de E1 mal formada; los veredictos de E3 que
  llegan como texto, leídos en código; el reintento con menos elementos, marcado; la marca de la copia de
  la nota; y el tercer escalón del reintento por corte.
- Registro del modelo de cada llamada, con la temperatura que lleva su pedido guardado: 0 en E1, 1 en el
  reintento por salida mal formada, y «default del proveedor» en E3, cuyo pedido no la lleva. Costo real
  contra el estimado, por etapa y por TO.
- Contadores: vocabulario retirado, que tiene que ser 0; unidades por estado final; unidades sin validación,
  listadas; unidades con cada marca de E3 (`lectura_veredicto_e3`, `reintento_con_menos_elementos` y
  `copia_nota_e3`); salidas mal formadas y sus reintentos; unidades que cortan en el primer intento, en el
  reintento y las partidas por corte, con sus tokens de salida; las unidades que usan el tercer escalón del
  reintento (P3c-2 de U-PROMPT-R2), con su marca; y los tokens de salida por carácter de texto propio de
  todas las unidades (decisión de la autora del 04/10/2026): la mediana, el percentil 90 y el máximo por
  tramo de tamaño del texto propio; aparte, las unidades de 3.000 caracteres o más (con el prefijo sellado,
  mediana 0,86 en 40 unidades; en P4, 1,175 en 6) y, una por una, las de 10.000 o más. Con esa medición se
  recalcula la capacidad del reintento (docs/checklist_pre_escalado.md, condición 12).
- Omisiones `meta_normativo` (enmienda 7 a L-ESQ-R2, §3, con su nota; decisiones de la autora del 04/10 y
  del 05/10/2026), por TO y en total:
  - cuántas hay, y cuántas traen una marca de alguna de las siete clases (deber, prohibición, facultad,
    condición, excepción, alcance y modalidad), con las tres subclases de modalidad (contador de
    `validador_r2`). El contador no suma marcas nuevas: las siete formas que se le escaparon en P4b se
    escribirían mirando los casos;
  - aparte, las que tienen el tramo solo en el texto heredado (en P4b, 6 de 12 con el prefijo de P3c);
  - cuántas objetó E3 con su NOTA de las omisiones, y en cuántas el reintento recuperó el contenido (en
    P4b, una: `ext::3.5.3::intro`). El criterio con que se cuenta una objeción se declara antes de contar.
- Normas con sujeto: cuántas normas (Obligacion, Restriccion y Potestad) llevan `aplica_a`, por TO y en
  total, en el crudo y después de la validación (referencias, en el contexto).
- Menciones de sujeto: cuántas relaciones `aplica_a` y `ejecuta` traen una mención que no verifica, por TO,
  con la mención y la unidad de cada una. Es el insumo de la medición de R2 de U-RERESOL-CAT para la
  enmienda 6.
- Control de la caché de E3 (decisión de la autora del 04/10/2026). El namespace de E3 del perfil r2b es el
  de la tanda 0. Se cuentan los aciertos de caché de E3 contra entradas anteriores a la corrida
  (`created_at` anterior a su inicio). Se espera 0; si hay alguno, se lista con su unidad y su clave.
FRENO T2.

T3 — ENSAMBLADOS, REGISTRO Y GATE DE r2b (USD 0).
1. Dos ensamblados r2b, diez y desarrollo, en corpus_tanda0/ens_diez_r2b/ y ens_desarrollo_r2b/ (se crean).
   Doble corrida byte a byte idéntica, y el sha256 de cada `kg.json`.
2. Gate (laudo de r2, §3.1), con la entrada de la suite ya sellada por la autora:
   - shapes: `scripts/shapes_validator.py --perfil r2 --fase r2b --e0 <salida_tanda0_r2b>`;
   - suite: `scripts/regression_kg.py --perfil r2 --esperado scripts/regression_kg_esperado.json`; 0
     regresiones;
   - contadores de E1; intrínsecas de generación 3 e indicadores de cita, informativos;
   - reproducibilidad: los tres ensamblados r1 se reproducen byte a byte. Los dos r2a ya no dan los sha256
     sellados (`99fe2bfa…` y `93a7af72…`): con el código de C2 cambian los umbrales y las `remite_a` que su
     cierre declara, y el control es contra `70d51e42…` (diez) y `fa4c1043…` (desarrollo), los de ese
     cierre (decisión de la autora del 04/10/2026). Los sellados siguen en el repo y se reproducen con el
     código de `f8dedd4`, que es el commit con el que la tesis cita sus cifras. Los selftests siguen en
     verde;
   - nunca EV2;
   - la columna «r2b» del tablero de correcciones, con el comando de cada fila.
3. Controles propios de esta unidad, cada uno con su comando y su cifra:
   a. cero elementos de extracción sin verificar, con la cola humana aparte (T1, punto 4.e);
   b. el criterio de la remisión del ejemplo: al menos una arista `remite_a` desde un nodo anclado en
      `cla::5.1.1.1` hacia uno anclado en `cla::3.7` (enmienda 2 de L-ESQ-R2, §9; checklist `:64`);
   c. la condición 10 de la tanda 1, como está definida (checklist `:81`; decisión de la autora del
      05/10/2026): el nodo de la Excepcion de `cla::5.1.1.1` existe, y desde los nodos de
      `cla::5.1.1::intro` se llega a los de sus hijos por la jerarquía de la procedencia, sin agente. Se
      reporta además si `cla::5.1.1::intro` dejó la Definicion de alcance y cuántas Condicion tiene
      `cla::5.1.1.1`. En P5, con temperatura 0, el ejemplo salió completo en las dos corridas; esta unidad
      trae una respuesta más. Si el nodo no está, se reporta y la condición vuelve a la autora: la unidad no
      se vuelve a extraer acá;
   d. el cierre de `BKL-0035` y de `BKL-0039`, medido sobre la extracción final, después de E3: ningún nodo
      de `ctacte::8.3::intro`, `ctacte::8.4::intro` ni `ctacte::6.4.7::intro` es una Obligacion cuyo contenido
      sea solo el encabezado de la lista (data/backlog/backlog.jsonl, `condicion_de_cierre`);
   e. el vínculo entre unidades, forma A: cuántas Condicion de incisos quedan sin `condicion_de` con destino
      en el encabezado de un ancestro (con la matriz congelada eran 36 de las 56 sin `condicion_de`, sobre 458);
   f. ningún elemento de umbral con `comparacion_asumida`, y los plazos sin marcador contados (enmienda 3);
   g. los diez TextoOrdenado con su versión y su materia;
   h. `omisiones.jsonl` del ensamblado y LN-7;
   i. las aristas derivadas que tocan un nodo que solo viene de la cola humana, contadas aparte;
   j. ninguna Operacion junta más de un punto;
   k. las claves `modalidad`, `consecuencia`, `modalidad_clasificada` y `copia_nota_e3` de
      `properties_no_definidas`, contadas aparte de las demás;
   l. los mini-chunks que empiezan a mitad de oración con un tramo de dos segmentos, contados: la
      verificación en orden de lectura cubre solo el tramo simple (límite declarado en el FRENO P3b-2).
   Controles del backlog (decisión de la autora del 04/10/2026, tras el recuento de las 39 entradas):
   m. el cierre de `BKL-0032`, `BKL-0033` y `BKL-0036`, cada uno con su condición de cierre leída contra su
      chunk: `docvig::3.3::cierre` (polaridad de la excepción), `ctacte::7.3.1.5` (ninguna Obligacion de la
      baja en la Central con `aplica_a` hacia el banco) y `lingob::2.3.2.2` (la Operacion conserva el
      calificador «en condiciones más favorables…»);
   n. `BKL-0038`: el conteo de las aristas `limita` y `prohibe` por `coherencia_tipo_predicado` en los dos
      grafos r2b (en r2a, 4 `limita` incoherentes en cada uno), y la lectura de los 3 chunks de esas 4
      aristas, `cap::6.2.1.4`, `ext::3.5.6.6` y `cap::4.3.3.1`, que dice en cada una si está mal el tipo o el
      predicado;
   o. los ocho patrones de asignación de sujeto, `BKL-0009` a `BKL-0016`, leídos caso por caso sobre el grafo
      r2b contra sus chunks (data/backlog/expediente_retriage_v3.md, T1 a T8; el remedio de cada uno, en
      data/experiment/prompt_r2/diseno_prefijo_r2.md, §6.2). Es el insumo del laudo de B2.4;
   p. `BKL-0028`: la re-adjudicación del miembro del rol de ctacor (nota del 01/10/2026 en el backlog);
   q. `BKL-0021`: si el registro de no mapeados de r2b trae la mención de la entidad nominada por el
      importador; si no la trae, se cierra como «no reaparece» en el laudo de B2.4;
   r. `BKL-0031`: el detector de casi duplicados (data/experiment/r2_codigo/r4_detector_casi_duplicados.py)
      corrido sobre los dos grafos r2b, como dato para la revisión de fusionados posterior a esta unidad.
4. Registro de los dos grafos en data/experiment/neo4j/grafos.py y carga en Neo4j local (precedente:
   `cf6ca42`). Se controla que la marca de la cola humana de los nodos llega.
FRENO T3. La autora sella los grafos.

T4 — LECTURA DE LA COLA HUMANA Y PREGUNTAS DE CONTROL (USD 0 de API).
1. Cola humana, primera medición (enmienda al protocolo del 04/10/2026 y su nota): si la cola de los diez
   TOs tiene más de 30 unidades, se sortean 30 con la semilla declarada antes de leer; si tiene 30 o menos,
   se leen todas. Lectura asistida con revisión de la autora. Unidad con error: al menos un nodo o una
   relación que el texto de la unidad no sostiene; las omisiones se reportan aparte. Se reporta el intervalo
   de Wilson al 95 % y se aplica la regla: 25 % sobre el límite superior con muestra, o 10 % sobre la tasa
   observada con la cola entera.
2. Las 15 preguntas de control sobre KG-Tanda0-Diez-r2b, con el script de T1: el cambio, pregunta por
   pregunta. No son evaluación ni se reportan como resultado.
3. Copia de la nota de E3. `copia_nota_e3` marca una posible copia: no afirma que lo sea. Los casos
   marcados en esta corrida se leen con la regla de data/experiment/prompt_r2/p3b2/regla_lectura_copia_nota.md,
   fijada antes de leer, y se reporta cuántos son copias reales. Referencia: sobre el crudo de r2a, 11 de 45.
   Si la precisión sigue baja, la regla se ajusta en código entre tandas: no en esta unidad.
4. Unidades con la marca del tercer escalón del reintento (decisión de la autora del 04/10/2026). Se leen
   todas, no una muestra: la extracción de cada una contra el texto de su unidad, con el mismo criterio de
   error de la cola humana, y aparte lo que E3 no reclamó. Se reporta cuántas son, cuántas tienen error y
   cuántos tokens de salida usó cada una. Con ese número la autora decide si hace falta algo para el
   escalado. No entran a la muestra de la cola humana por llevar la marca.
5. Las 27 unidades de P4b, sobre la extracción de esta unidad (decisiones de la autora del 05/10/2026). P5
   de U-PROMPT-R2 las pidió dos veces con temperatura 0. Donde la clave coincide con la de P5 (T1, punto
   3), esta unidad trae una tercera respuesta al mismo pedido.
   a. Por grupo, cuántos casos cumplen lo que mide el grupo, con las reglas de marcado de P4b
      (data/experiment/prompt_r2/p4b/marcas_p4b.py), como fracción y con la razón de cada caso.
   b. La variación, en las unidades con la misma clave: unidad por unidad, si la respuesta de esta corrida
      es idéntica a las de P5 y, si difiere, en cuánto (nodos, normas y omisiones), y en cuántos casos
      cambia la marca del grupo. Se compara con la medición de P5, no con P4b, que corrió sin temperatura
      fijada.
6. Las listas que exceptúan (b1 y b2), con las once listas selladas en T1 (punto 7.b): por lista y por
   ítem, si la extracción da la forma de la regla del prefijo (en b1, la Excepcion del miembro con la norma
   exceptuada; en b2, la Condicion del supuesto con el cuantificador y la norma exceptuada; y en el
   encabezado, la Definicion de la clase, en b1, o la norma unida a su excepción, en b2). Como fracción,
   por tipo. `ctacte::3.2` es de lectura dudosa como b1 y se reporta aparte, declarada (decisión de la
   autora del 05/10/2026).
7. Una Condicion por supuesto (grupo c): 30 unidades, en el orden sorteado en T1 (punto 7.c). Se decide
   sobre el texto, antes de mirar la extracción, si la unidad tiene más de un supuesto; las que no, se
   saltean y se cuentan. Si el pool no llega a 30, se leen todas. Se reporta la tasa con su intervalo de
   Wilson al 95 %.
8. Omisiones `meta_normativo`, por lectura (enmienda 7, §3; L-ESQ-R2, §5.3, la muestra de control;
   decisión de la autora del 05/10/2026). Dos sorteos, con las semillas de T1: 30 omisiones sin marca del
   contador y 30 con marca; si un grupo tiene 30 o menos, se leen todas. De cada una se dice si su tramo
   es contenido normativo según el §1 de la enmienda 7, y si es contenido habilitante. Se reporta, por
   grupo, la tasa con su intervalo de Wilson al 95 %, y aparte las que tienen el tramo en el texto
   heredado. Con la de las sin marca se estima cuántas normativas se le escapan al contador.
Las lecturas de los puntos 5 a 8 son asistidas, con revisión de la autora.
FRENO T4.

T5 — REPORTE (USD 0).
- Costos, cifras del gate, la columna «r2b» del tablero y los controles de T3, cada cifra con su comando.
- Lo que P4b dejó sin mejorar, con las cifras de T2 y de T4: las listas que exceptúan, una Condicion por
  supuesto, y las omisiones `meta_normativo` con contenido normativo, con las del texto heredado aparte. De
  cada una, lo que se puede corregir en código entre tandas y lo que quedaría como límite declarado con su
  cifra. Decide la autora.
- La variación del modelo: la medición de P5, la del punto 5.b de T4 y la de los veredictos de E3, que
  corre sin temperatura fijada.
- Lo que sigue a esta unidad, sin hacerlo: la lectura de confirmación de `condicion_de` → Operacion y →
  Potestad; la medición de la `remite_a` estructural (30 aristas, piso de Wilson 0,75) y del lado del
  destino, después de la unidad que atribuye `remite_a` por tramo; la alternativa de unión de las
  operaciones por encabezado (30 uniones, piso 0,75); la recuperación por tramo de lo que el reintento dejó;
  y R2 de U-RERESOL-CAT sobre este crudo, que incluye la lectura de la parte B de la enmienda 6 a L-ESQ-R2
  (decisiones de la autora del 04/10/2026): en un documento con alcance, una norma sin mención recibe
  `aplica_a` hacia el rol de alcance de su documento, como relación derivada y marcada como tal, solo si la
  lectura llega al piso (28 correctas de 30).
- Claves de la caché (decisión de la autora del 04/10/2026, tras el freno de U-TABLA-REPROC):
  - se vuelve a correr data/experiment/mantenimiento/code/selftest_clave_cache.py con
    `--salida-r2b data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b`, sobre una copia: es el anclaje
    del perfil r2b (A1r y A3r), que hoy da NO_VERIFICABLE porque no hay claves de r2b en las dbs. Si la E0 de
    la corrida no es `salida_tanda0_r2b/`, cambia también la constante `E0_TANDA0_R2B` del selftest;
  - el §5 de data/experiment/mantenimiento/tabla_reprocesamiento.md reemplaza el costo de referencia
    estimado del perfil r2b (E1 USD 0,010544 y E3 USD 0,010333 por unidad) por la tarifa observada en esta
    corrida, con su comando;
  - en las filas F05, F10 y F14 de la tabla, «enmienda en curso» pasa a citar la enmienda 3 del protocolo
    entre tandas, firmada el 04/10/2026.
FRENO T5, final.

ESCRITURAS: los tres manifiestos r2b; corpus_tanda0/salida_r2b/, ens_diez_r2b/ y ens_desarrollo_r2b/;
scripts/regression_kg.py, scripts/shapes_validator.py y sus selftests, solo para el punto 4 de T1;
scripts/regression_kg_esperado.json, solo con la entrada que selle la autora; data/experiment/neo4j/grafos.py,
solo las dos entradas nuevas; docs/tablero_correcciones.md, solo la columna «r2b»;
e1_extractor/selftest_prompt_r2b.py, solo para el caso de `herencia_recortada` (T1, punto 2); una carpeta de
la unidad, data/experiment/reext_t0/ (se crea), para frenos, scripts, listas selladas, lecturas y reportes;
data/experiment/mantenimiento/tabla_reprocesamiento.md (solo el §5 y la cita de la enmienda en F05, F10 y
F14), selftest_clave_cache.json (la salida) y, solo si cambia la E0, la constante del selftest; y el
scratchpad.
PROHIBIDO: editar el prefijo, el tool schema, la cadena de E0 a E5 o los validadores (si un control falla
por el código, se reporta y no se corrige acá); cambiar el modelo o los parámetros del pedido, incluida la
temperatura; volver a extraer una unidad fuera de los reintentos del pipeline; tocar las salidas y los
grafos sellados de r1 y de r2a; correr EV2 o cualquier celda con agente; usar las 15 preguntas como
evaluación; actualizar el corpus; commitear.

DECISIONES DE LA AUTORA AL FIRMAR, tomadas el 05/10/2026.
1. El tope de T2: USD 80 (antes, USD 72). La re-estimación con lo medido en P5 llega a 69,91 con el factor
   1,4.
2. Las celdas con agente de la tanda 0 no se vuelven a correr sobre los grafos r2b en esta unidad
   (referencia de su costo: USD 21,2577).
3. Las carpetas de salida: `salida_r2b/`, `ens_diez_r2b/`, `ens_desarrollo_r2b/` y
   `data/experiment/reext_t0/`.
4. El registro de los dos grafos y su carga en Neo4j van en esta unidad, en T3.
5. La semilla del sorteo de la cola humana: `U-REEXT-T0:cola-humana:2026-10-05`.
Ya decididas por la autora el 05/10/2026, y en el texto de arriba: la temperatura de E1, en 0, y la del
reintento por salida mal formada, en 1, con P5 de U-PROMPT-R2 como precondición; la temperatura de E3, que
queda sin fijar, declarada como límite, sin cambiar su modelo; la condición 10, si el nodo de la Excepcion no
sale en esta corrida (T3, punto 3.c); y las tres lecturas nuevas de T4: la variación (punto 5.b), 30 unidades
del grupo c (punto 7) y 30 omisiones `meta_normativo` con marca (punto 8).

LO QUE LLEGA DE LAS UNIDADES ANTERIORES, con su commit. T1 lo controla.
- De P3c-2 de U-PROMPT-R2 (data/experiment/prompt_r2/freno_p3c2.md; `66cde30`). Reemplaza a lo de P3b-2
  (`c8c3970`: hash `3817de475c93`).
  - El prefijo: hash `322c5a23e9b7`, sha256 `ccffa4e3…`, 59.909 caracteres y 27.840 tokens medidos. El
    parche de P3c tiene sha256 `5e3761c1…` y se aplica sobre el prefijo de P3b-2 (`8d84364f…`).
  - El namespace de E1: `e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7|think=0`.
  - El tool schema no cambia (`0c391f2b…`). El prefijo de E3 y su namespace tampoco (`21a836c7de6d`).
  - Los candados de lo que no entra al hash del prefijo:
    - la lista de tablas forzadas a residual, con `cap::tabla037`: sha256 `98cc96b2…`;
    - el mensaje de E1: fixture `candado_mensaje_r2b.json`, sha256 `4d69f7f4…`, y mensaje `a9cb702c…`;
    - el mensaje de E3: fixture `candado_mensaje_e3.json`, sha256 `e8fa5dc4…`, y mensaje `da17c22e…`.
  - El tercer escalón del reintento: techo de 40.960 tokens, marca `escalon_3` en el registro de E1 y en su
    resumen, y error definitivo `max_tokens_hit_tras_escalon_3`.
  - Los contadores nuevos del validador: `omisiones.meta_normativo_con_marca`, con sus siete clases,
    `omisiones.tramo_solo_heredado` y `omisiones.tramo_orden_de_lectura`.
  - En el manifiesto, las unidades con tabla serializada confiable pasan de 37 a 36, por `cap::6.2.2.6`.
  La fase le llega a E2 por el parámetro `fase` de `ensamblar_r2`.
- De la corrección de la clase modalidad (data/experiment/prompt_r2/freno_p3c2_modalidad.md, con su nota;
  `bb212f1`): las tres subclases de modalidad del contador (opción, consejo y forma), cada una con su
  contador (`omisiones.meta_normativo_con_marca:modalidad.<subclase>`). Ninguna clave cambia.
- De P4b de U-PROMPT-R2 (data/experiment/prompt_r2/freno_p4b.md; `046e493`; USD 0,8111 de un tope de 1,5).
  Corrió sin temperatura fijada.
  - La salida con el prefijo de P3c: 40.626 tokens en 27 unidades, 0,886 de la del prefijo de P3b-2, y
    1,833 tokens por carácter de texto propio en unidades cortas; la entrada sin caché, 1,026. La
    proyección de T1 las usa como cota.
  - El ejemplo, con el prefijo de P3c: `cla::5.1.1::intro` deja la Definicion de alcance; `cla::5.1.1.1`
    deja la Excepcion, la Operacion de clasificar y una de las dos Condicion, y su `exceptua` hacia la
    Operacion se rechaza por la firma. Es una respuesta por unidad.
  - La API aceptó el techo completo del tercer escalón, 40.960 tokens, con transmisión (`ctacte::3.2.4`).
  - `cap::6.2.2.6`: sin valores de `cap::tabla037` y con la omisión `tabla` declarada.
  - La pata de E3: su NOTA de las omisiones recuperó el contenido de `ext::3.5.3::intro` y no reclamó el
    encabezado heredado de `ext::13.1.4`.
- De P5 de U-PROMPT-R2 (data/experiment/prompt_r2/freno_p5.md; `53b7708`; USD 0,9078 de un tope de 1,5). Su
  commit es el del código de esta unidad.
  - La temperatura: `TEMPERATURA_E1_R2B = 0` y `TEMPERATURA_REINTENTO_FORMA_R2B = 1`
    (`e1_extractor/prompt_r2b.py:109-110`). El pedido del reintento por salida mal formada lo arma
    `runner_corpus.kwargs_reintento_forma`. En la tabla de reprocesamiento, la fila F08e y la variación R14;
    para el reintento, F08c y R25. La tabla tiene 40 filas, y el selftest de claves, 41 variaciones del
    perfil r2b.
  - No cambian el prefijo, el mensaje, el tool schema, el namespace de E1 ni el pedido de E3. Cambia la clave
    de E1 de todas las unidades.
  - Las claves de las 27 unidades con temperatura 0, para el control del punto 3 de T1:
    data/experiment/prompt_r2/p5/salida/claves_despues.json.
  - La variación medida, entre dos corridas del mismo pedido: en E1, 6 de 27 respuestas idénticas, 5 que
    difieren solo en la redacción y 16 en algún conteo; en E3, sobre 10 unidades, el mismo veredicto en 10 y
    la misma evaluación en 9.
  - El ejemplo, con temperatura 0, en las dos corridas: `cla::5.1.1::intro` deja la Definicion de alcance, y
    `cla::5.1.1.1`, la Excepcion, la Operacion de clasificar y una Condicion por cada condición. El
    `exceptua` de la Excepcion hacia la Operacion se rechaza por la firma, como en P4b.
  - La salida: 43.424 y 43.872 tokens en las 27 unidades, 1,959 y 1,979 por carácter de texto propio; contra
    la del prefijo de P3b-2, 0,947 y 0,957. La entrada no cambia con la temperatura.
  - La caché de prompts de la API se sigue leyendo entre un pedido con temperatura 0 y uno con 1.
  - Los selftests que cambian: `selftest_prompt_r2b`, 55 de 55, y `selftest_ub53`, 58 de 58.
- De C2 de U-R2-CODIGO-2 (data/experiment/r2_codigo2/freno_c2.md; `9f6361e`).
  - `salida_tanda0_r2b/`: 57 archivos, con sus diez `pies_<to>.json`, sin cambios desde ese commit al
    05/10/2026 (`git diff --stat 9f6361e -- data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/`,
    vacío). Frente a `salida_tanda0_r2/` cambia solo ric, con los cambios que declara ese freno.
  - El namespace del reintento por salida mal formada: el de E1 con el sufijo `-rforma1`.
  - El reporte del ensamblado r2b trae el total de lo que pasó por E3, las tres marcas de E3 (puntos s y t)
    y las aristas derivadas que tocan la cola humana (`aristas_derivadas_cola_humana.json`, punto q).
  - Los grafos de la cadena r2a con ese código: `70d51e42…` (diez) y `fa4c1043…` (desarrollo).
- De P4 de U-PROMPT-R2 (data/experiment/prompt_r2/freno_p4.md; `2ed47a0`): costó USD 1,1086, de un tope de
  2. En su corrida, el prefijo de P3b-2 no emitió la Excepcion de `cla::5.1.1.1`; en P4b, el mismo pedido la
  emitió. La clasificación de la modalidad detectó 2 recomendaciones y ninguna consecuencia.

REQUISITOS: los de CLAUDE.md §4 (a a l), con PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; verificaciones y
selftests sobre una copia sin enlaces, con el sha256 de los archivos del repo antes y después; fuentes
firmadas leídas en el commit de su firma; todo conteo recomputado contra su artefacto; los conteos sobre
grupos chicos, como fracción y sin porcentaje; cero nombres de personas.

NOTAS POSTERIORES A LA FIRMA. El texto firmado no se edita; estas notas se leen junto con él.
- **06/10/2026 — decisiones de la autora sobre el FRENO T2 (T2 en `3d793aa`).** La corrida de T2 costó USD
  49,6598 de un tope de 80 y dejó 2.439 unidades con estado final: 1.337 completo_ok_directo, 811
  aceptado_con_residuales, 216 aceptado_tras_reintento, 73 en la cola humana y 2 sin validación
  (`data/experiment/reext_t0/freno_t2.md`).
  - La revisión independiente reprodujo T2 sobre copias de la salida, de las bases y del usage: los estados, el
    gasto (24,7195 de E1 y 24,9403 de E3), las 5.378 filas nuevas de las bases contra las 5.378 líneas nuevas de
    usage, la temperatura de cada pedido (0 en E1, 1 en el reintento por forma, 0 en los reintentos del ratchet,
    sin fijar en E3), los 7 cortes (6 en 8.192 y 1 en 16.384, `cap::4.2.1.2`) y las dos cifras de 404 omisiones
    `meta_normativo`, que cuentan conjuntos distintos (las 404 con marca del contador en la validación final y las
    404 objetadas por E3 en el crudo de la primera verificación tienen 136 omisiones en común).
  - Decisiones.
    1. Defecto del runner. `corpus_v2/runner_corpus.py` no agrega `e0_chunking` al `sys.path` (`:64-67`), e
       `import correr_e0` falla en `corresponde_escalon_3` (`:476`) y en la partición por corte (`:673`); el
       import solo se ejecuta cuando el reintento de 16.384 también corta, así que alcanzó a una sola unidad,
       `cap::4.2.1.2`, que quedó sin validación. Se corrige antes de T3, en una etapa T2-bis con tope de USD 3:
       la línea de `sys.path` para `e0_chunking` y un interruptor `--reabrir-fase` que reabre las fases cerradas
       de un TO conservando su gasto como gasto previo (sin el interruptor, nada cambia). La corrección no mueve
       ninguna clave de caché (fila F20 de la tabla de reprocesamiento, cuya ancla suma el bloque del path; el
       selftest de claves tiene que dar 0 cambios). En ese archivo el código del pipeline deja de ser el de
       `53b7708`; el commit de T2-bis pasa a ser la referencia.
    2. `cap::4.2.1.2` se re-extrae en T2-bis con el runner corregido y el código de E0 de HEAD, que es el de
       `9f6361e`: la partición por corte de 15.056 y 11.669 caracteres, la misma que S0-2 de U-SEG-OFICIAL tiene
       que conservar. E1 re-llama solo las unidades con error; E3 verifica solo las partes. El código de E0 no se
       toca. T3 espera a T2-bis.
    3. `cap::3.1.1.2`: sus dos salidas (temperatura 0 y 1) son `tool_use` con dos entidades y sin la clave
       `relations`, y `validador_e1` rechaza el chunk entero. Recibe un segundo reintento por forma, con sufijo
       `-rforma2` y temperatura 1, una sola vez; si vuelve mal formada, queda sin validación, declarada. La regla
       «sin reparación determinística» de C2 no cambia.
    4. Medición para la regla 6 en E1 de S0-2 de U-SEG-OFICIAL (nota del 05/10/2026 al pie de su mandato,
       `d59921f`): se toma el p90 de la salida por carácter de las 39 unidades de 3.000 caracteres o más, 1,5051
       (mediana 1,1582). Capacidad del tercer escalón: 40.960 / 1,5051 = 27.214 caracteres; objetivo de las
       partes por renglones: 16.384 / 1,5051 = 10.886. El objetivo de la partición por ítems (13.091) no cambia.
       Con la mediana no cambiaba ninguna clase del diseño de S0-1 bis; con el p90 cambian `ri2_cs::S3` y
       `ri_cc::S3` (su parte de 27.274 caracteres pasa a partirse por renglones). Se elige el p90 porque la
       capacidad es la guarda contra una unidad sin salida y la razón de las unidades grandes de T2 va de 0,25 a
       1,79.
    5. La lección de T1 (la corrida en seco agregaba `e0_chunking` al path por su cuenta y por eso no vio el
       defecto) queda en CLAUDE.md, §4, regla l: la corrida en seco de un runner ejercita el mismo camino de
       imports y de código que el runner, sin arreglar el `sys.path` por fuera.
- **06/10/2026 — decisiones de la autora sobre el FRENO T2-bis (T2-bis en `4ab7a0a`; fila P20 del checklist en
  `e1c84c1`).** T2-bis costó USD 0,49291 de un tope de 3 (`data/experiment/reext_t0/freno_t2bis.md`): `cap::4.2.1.2`
  se partió en 15.056 y 11.669 caracteres (la partición de `9f6361e`); la parte 2 salió en `-rforma1`, E3 la aceptó
  con residuales y aporta 22 nodos al E2 r2 de cap (2.168 → 2.190); la parte 1 salió mal formada en 16.384, en
  `-rforma1` y en `-rforma2`, y `cap::3.1.1.2` también en `-rforma2`: las dos quedaron sin validación. La revisión
  independiente reprodujo las cifras sobre copias (9 filas nuevas y 9 líneas de usage, el gasto por tokens, la
  partición, 188 de 188 archivos del E2 y del E2 r2 de los diez TOs iguales a T2) y encontró que las 12 salidas mal
  formadas de T2 y T2-bis (8 primeros intentos, 2 en `-rforma1` y 2 en `-rforma2`) tienen el mismo defecto: traen
  `entities` como lista y no traen la clave `relations`.
  - Decisiones.
    1. Corrección de `cerrar_e2` (fuera de los puntos a–c del despacho de T2-bis; autorizada en la sesión y
       confirmada aquí): la unidad partida por corte va al fan-in del E2 del perfil de E1 con su último registro de
       E1 (error `particionada_por_corte`), como rechazada en E1, y el reporte la declara aparte, reemplazada por
       sus partes, que entran al E2 r2. Sin particiones nada cambia; con la corrección, el E2 y el E2 r2 de los diez
       TOs regenerados sobre la salida de T2 salen byte a byte iguales (188 de 188).
    2. Reparación acotada de la salida de E1 sin la clave `relations`: solo después de agotar los reintentos por
       forma (`-rforma1` y `-rforma2`); solo si la salida es un dict con `entities` lista, sin la clave `relations`,
       y con `relations = []` el validador de E1 la acepta; la unidad queda marcada en su registro
       (`reparacion_forma`) y contada aparte en el resumen de E1; E3 la verifica como a cualquier otra y, si faltan
       relaciones, las reclama (el ratchet las pide). Es la única excepción a la regla «sin reparación
       determinística» de C2 de U-R2-CODIGO-2; cualquier otra salida mal formada sigue el camino de siempre. No
       mueve ninguna clave de E1 (actúa sobre la respuesta guardada, no sobre el pedido); las unidades reparadas
       pagan E3. Fila en la tabla de reprocesamiento: F08c ampliada (segundo reintento y reparación), con una
       variación nueva del selftest de claves para el namespace `-rforma2`, o una fila propia (F08f) si F08c queda
       ambigua; lo propone T2-ter en su freno.
    3. T2-ter, antes de T3, con tope de USD 1: la reparación aplicada a `cap::4.2.1.2::parte1` y a `cap::3.1.1.2`
       sobre sus salidas guardadas (0 llamadas a E1; E3 de las dos unidades y sus reintentos del ratchet); la
       corrección de A1r en `data/experiment/mantenimiento/code/selftest_clave_cache.py` (la clave del reintento por
       forma se arma con `prompt_r2b.kwargs_reintento_forma_r2b`, y en `-rforma2` para el segundo reintento), que T5
       necesita como anclaje del perfil r2b; y la tabla de reprocesamiento (las 24 menciones con anclas desplazadas
       por el código de T2-bis, `data/experiment/reext_t0/t2bis/anclas_desplazadas_tabla.txt`, y F08c).
    4. La razón de tokens por carácter para la regla 6 en E1 de S0-2 de U-SEG-OFICIAL se mantiene en 1,5051 (p90 de
       T2 sin las partes): con las partes da 1,4820 (41 unidades) o 1,4936 (40 con E1 válida); la única unidad del
       diseño de S0-1 bis entre 27.214 y 27.638 caracteres es `ri_cc::S3`, que con 1,5051 se parte por renglones.
    5. La reparación se declara en la tesis como procedimiento, con su cifra (cuántas unidades se repararon y sobre
       cuántas salidas mal formadas), que T5 toma del resumen de E1 de la corrida; el capítulo 4 la describe junto
       con el reintento por forma.
  - Selftests que fallan desde HEAD por causas ajenas a estas unidades: `selftest_clave_cache` (A1r arma la clave del
    reintento por forma con el pedido base, sin la temperatura 1 de P5: código de `2a857db` que P5 no actualizó,
    visible desde que existe `salida_r2b/`, `3d793aa`) y `selftest_canal_abierto_e1` (bloque B, 45 de 46, desde
    `0e50e3d`, 31/08/2026). El primero se corrige en T2-ter; el segundo, con la parada ordenada por SIGUSR1 y el tope
    por corrida, en la unidad de mantenimiento del runner (checklist, fila P20, `e1c84c1`).
- **06/10/2026 — decisiones de la autora sobre el FRENO T2-ter (T2-ter en `ad99ac7`).** T2-ter costó USD 0,249002
  de un tope de 1 (`data/experiment/reext_t0/freno_t2ter.md`): la reparación acotada se aplicó a `cap::4.2.1.2::parte1`
  y a `cap::3.1.1.2` sobre sus salidas guardadas, sin pagar E1 (7 aciertos de caché); `cap::3.1.1.2` quedó
  aceptado_con_residuales con 2 nodos; la parte 1, tras un reintento del ratchet, en la cola humana con 54 nodos
  marcados; sin validación 0; el E2 r2 de cap pasó de 2.190 a 2.244 nodos; A1r del selftest de claves corregido (de
  FRENO a OK, con la variación R25b) y la tabla de reprocesamiento re-anclada (0 desplazadas). La revisión
  independiente reprodujo las cifras sobre copias (la cuenta de las 2.439, el gasto por tokens, las 4 filas nuevas y las
  4 líneas de usage, el selftest de claves en OK) y recontó la cifra de la reparación desde los registros.
  - Decisiones.
    1. Fila F08f de la tabla de reprocesamiento (reparación acotada), escrita en la revisión: clave de E1 «no cambia»,
       clave de E3 «cambia (las reparadas)», clase «E3 de las afectadas», anclas `runner_corpus.py:542-559`,
       `:710-720`, `:727-728` y `:816-819`. Cita la variación R18 (la de F14: la salida validada de E1 alterada en
       código mueve la clave de E3 y no la de E1), porque el contraste del selftest de claves exige que toda variación
       citada exista y la variación propia que proponía T2-ter (R25c) no está implementada: con ella la tabla hacía
       fallar el selftest. La variación propia queda pendiente para la unidad de mantenimiento del runner (checklist,
       fila P20). F08c vuelve a describir solo los dos reintentos por forma (R25, R25b).
    2. Cifra de la reparación para la tesis, recontada desde `extracciones_e1.jsonl` y las bases: 12 salidas de E1 mal
       formadas en 8 unidades (8 primeros intentos, 2 en `-rforma1` y 2 en `-rforma2`, todas con `entities` lista y sin
       la clave `relations`); 6 unidades resueltas con un reintento, 2 reparadas (`cap::3.1.1.2` y
       `cap::4.2.1.2::parte1`) y 0 agotadas. El «seguí» de T2-ter decía «10 unidades y 8 resueltas»: error de la
       revisión, no del repo (la nota anterior da las 12 salidas por intento, sin cifra de unidades); corregido.
    3. La parte 1 de `cap::4.2.1.2` integra la población de la cola humana de T4 (74 entradas: 73 unidades y la
       parte 1). El sorteo se hace en T4 con la semilla y el procedimiento sellados en T1
       (`data/experiment/reext_t0/sellos_t4.json`); corrido en la revisión sobre la cola actual, la parte 1 sale
       sorteada. Si al llegar a T4 la cola fuera otra y la parte 1 no saliera, se lee aparte y declarada. Los sellos
       no se tocan.
  - Para la unidad de mantenimiento del runner (checklist, fila P20): guardar en la marca `reparacion_forma` del
    registro de E1 la clave de caché o el sha256 de la salida original del modelo, porque hoy esa salida (la tercera,
    la que se repara) queda solo en la caché y se recupera recomputando la clave; y la variación propia de F08f en el
    selftest de claves.
- **06/10/2026 — decisiones de la autora sobre el FRENO T3 (T3 en `c499eb3`).** El gate de r2b no pasó: shapes S3,
  S18, S19 y S28 en FAIL y 6 regresiones de la suite en cada grafo (BKL-0006, BKL-0023, RT-C5-3, RT-C6-1, RT-C6-2 y
  LN-5), con los grafos ensamblados en `data/experiment/reextraccion_v2/corpus_tanda0/ens_{diez,desarrollo}_r2b/`
  (kg.json `12c5cfc3…` y `6de41495…`; `data/experiment/reext_t0/freno_t3.md`). La revisión independiente reprodujo los
  dos ensamblados, la doble corrida, las 6 regresiones y las 4 shapes sobre una copia fresca, y leyó cada falla en los
  nodos y en el texto de su unidad. La fixture de la suite no se tocó: los `kg_sha256` de las entradas r2b se completan
  una sola vez, con los grafos finales.
  - Decisiones.
    1. **T3-bis**, antes de T4, con USD 0: correcciones de código y re-ensamblado de los dos grafos, con el gate de
       nuevo. En el ensamblado: la colisión cross-TO de un propuesto actualiza su fila en `no_mapeados_sujetos.jsonl`
       (LN-5 y S28); un `padre_sugerido` hacia una instancia se reemplaza por su clase o se quita con marca, y un
       propuesto cuya mención es un pronombre o una palabra vacía se descarta con marca (S3); un propuesto sin
       `padre_sugerido` recibe el rol de alcance de su TO con la marca `padre_por_defecto` (S19). En el normalizador de
       umbrales de E2: la cuantía que viene de una celda de tabla serializada hereda la unidad del rótulo de la tabla y
       gana valor y unidad normalizados (BKL-0006 y BKL-0023 pasan con su sello intacto). S18 en dos piezas: el
       ensamblado escribe la marca r2b `umbral_no_cuantificable` en las Restricciones `limite_cuantitativo` sin cuantía
       detectable en descripción, tramo ni celdas, y la shape la cuenta como «umbral guardado sin lista»; lo que la
       shape espera no cambia. `remite_a` no se toca: el detector ya lee el texto de la unidad.
    2. **BKL-0021** («la entidad nominada», Exterior): opción (c), un rol nuevo en el catálogo por U-RERESOL-CAT
       (enmienda 4 al protocolo: censo, laudo, ítem nuevo en la suite y entrada en el esqueleto); mientras tanto,
       opción (d): los dos propuestos siguen en cuarentena, declarados. Hoy las menciones de la figura van 16 al rol
       de alcance de Exterior, 4 a `Sujeto_entidad_financiera` y 4 a los dos propuestos.
    3. **Declaraciones, posteriores al resultado y con su lectura** (se escriben en el freno de T3-bis con los textos
       pegados; ninguna expectativa sellada cambia por el resultado):
       - RT-C6-1 y RT-C6-2: la norma (`pro::1.1.2.5`) dice «excepto que se trate de asociaciones mutuales **o**
         cooperativas, por las financiaciones que otorguen»; la descripción de la Excepcion de r2b dice «las asociaciones
         mutuales **y** cooperativas, en lo que respecta a las financiaciones que otorguen». Es una **desviación de
         fidelidad del modelo en la descripción** («y» por «o»), con el alcance igual (cada clase queda exceptuada) y
         el `tramo` fiel («excepto que se trate de asociaciones mutuales o cooperativas»); la Definicion del mismo
         chunk conserva el «o».
       - RT-C5-3: «antes de 60 días desde la mora» por «antes de los 60 días contados desde la fecha en que se
         verificó la mora»: **paráfrasis sin cambio de sentido**; el ítem está mal diseñado para r2b porque compara
         literalmente un gold escrito para extracción textual.
       - `remite_a`: sobre el texto propio de las 2.439 unidades el detector del perfil r2 encuentra 1.385 citas; r2b
         registra 1.380 y deja 5 sin registrar (`cla::3.3.4` → 1.1.4 y 1.1.5, `ctacte::6.2::intro` → 6.1,
         `ctacte::7.2.2.5` → 1.3.1.9, `ext::7.9.3::intersticial` → 7.9.2), que valdrían 4 aristas en 1 unidad. La baja
         de 620 aristas frente a r2a es fan-out en el destino (los Operacion anclados en los puntos citados pasan de
         3.133 a 1.684), no pérdida de citas.
    4. **Para la tesis**: el caso de RT-C6 ilustra el papel del tramo literal frente a la descripción: el tramo (la
       cita textual que E1 guarda y E3 verifica) conserva el conector de la norma mientras la descripción lo cambia;
       la fidelidad se audita en el tramo, y la descripción es la lectura del modelo. Registrado en
       `docs/insumos_escritura.md`, sección 7.
- **06/10/2026 — decisiones de la autora sobre el FRENO T3-bis (T3-bis en `bbc38dc`; sello de los grafos r2b en
  `c9540c0`).** El gate de r2b pasa con los grafos re-ensamblados: diez
  `a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57` (8.816 nodos / 27.632 aristas) y desarrollo
  `6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2` (6.990 / 23.445); shapes bloqueantes en PASS en
  los dos (S18 con 14 y 13 marcados), suite con 0 regresiones nuevas, LN-5, BKL-0006 y BKL-0023 en resuelto, 3
  regresiones declaradas (RT-C5-3, RT-C6-1 y RT-C6-2), 56 coincidencias y 9 NO VERIFICADAS
  (`data/experiment/reext_t0/freno_t3bis.md`). La revisión independiente reprodujo sobre una copia los dos sha, la
  doble corrida (los directorios difieren solo en la ruta de salida que guarda el reporte del ensamblador), las shapes
  en PASS y las 3 regresiones; leyó el código y confirmó que las correcciones del ensamblado corren solo con el perfil
  r2b (`if r2b:` en `correr_cadena_r2`; r1 y r2a se siguen reproduciendo).
  - Decisiones.
    1. La marca de S18 va en `properties_no_definidas.umbral_no_cuantificable` (con `_motivo` y `_detector_sha256`),
       como la puso la instancia: ponerla en `properties` exige tocar `modelos_r2.py` (`NodoR2` es `extra="forbid"` y
       S26 cierra `properties` por tipo), que está sellado. La shape S18 la cuenta como «umbral guardado sin lista».
       Se confirma la ampliación tomada en la sesión: también se marcan las cuantías que están solo en celdas de una
       tabla residual forzada (`cap::tabla037`, 1 nodo por grafo), con su motivo y el sha256 de la lista (`98cc96b2…`).
    2. Propuestos (decisión 1 de T3-bis): se confirman los descartes de «se» y «cada una» por mención vacía (2 aristas
       quitadas por grafo, con fila «descartado») y los 6 propuestos con `padre_por_defecto` (4 de ext hacia
       `Sujeto_rol_entidad_autorizada_exterior`, 2 de cap hacia `Sujeto_rol_alcance_capmin`). Los propuestos cuya
       mención es un verbo («podrán», `pro::2.3.12.1`, padre sugerido por E1 `Sujeto_rol_sujeto_obligado_proteccion`;
       «Deberá rechazarse», `ctacte::6.3.1`, padre sugerido `Sujeto_banco`; conservan el padre de E1, no el de por
       defecto) y los demostrativos y anafóricos («Esta entidad», «esta Institución», «Esta delegación», «Dichas
       evaluaciones», «Los casos», «Estas verificaciones») quedan listados, con la norma, la unidad, la mención y el
       tramo, como insumo de U-RERESOL-CAT, sin otra regla ahora (lista en el paquete de la revisión y en
       `t3bis/salida/declaraciones_t3bis.md`): en diez, 2 verbales (los dos) y 2 descartados; en desarrollo, 1 verbal
       («podrán»; ctacte no está) y 2 descartados.
    3. Sellado, en este orden, ya hecho: (i) el commit de T3-bis (`bbc38dc`: código, ensamblados, declaraciones, freno
       y `t3bis/`), sin la fixture; (ii) con ese hash, el commit del sello (`c9540c0`): los dos `kg_sha256` de la
       fixture completados sin otro cambio (verificado por la revisión: el resto de la fixture es idéntico),
       `commit_sellado` = `bbc38dc` en las dos entradas r2b de `data/experiment/neo4j/grafos.py`, y la recarga de los
       dos grafos en Neo4j con gate 5 OK (`t3bis/salida/neo4j_sello_*/carga_neo4j_tanda0.json`: `KG_Meta` lleva el
       sha y `commit_sellado` `bbc38dc`; `verificar_carga` compara solo `kg_sha256`).
    4. Las declaraciones de la decisión 5 de T3 quedan escritas en `t3bis/salida/declaraciones_t3bis.md` con los textos
       de la norma y de los nodos; valen como posteriores al resultado.
  - Sigue T4 (lectura de la cola humana y preguntas de control) con los grafos sellados; la cola tiene 74 entradas, con
    la parte 1 de `cap::4.2.1.2`; el tercer escalón no tiene casos en r2b.

- **06/10/2026 — decisiones de la autora sobre el FRENO T4, primer tramo (sorteos, fichas y puntos 2 a 4;
  `data/experiment/reext_t0/freno_t4.md` y `t4/`, sin commit al escribir esta nota; T3-bis en `bbc38dc`, sello de los
  grafos r2b en `c9540c0`).** Las lecturas de los puntos 1 y 5 a 8 son propuestas de la instancia; la adjudicación de
  la autora llega con el «seguí» del segundo tramo. Decisiones sobre las preguntas del freno:
    1. Cada punto mantiene la regla fijada antes de leer. En `ext::10.3.6` la marca del punto 5 (la regla de P4b sobre
       la respuesta de E1, reusada de P5) es «cumple»; con la regla del punto 7 esa misma respuesta no cumpliría (la
       porción con pagos a la vista va dentro de la Excepcion) y la extracción final, tras el reintento, cumple. La
       diferencia se declara; no se reconcilia.
    2. Una remisión sin contenido propio no es normativa: cuenta solo si trae una de las siete clases del contador
       (deber, facultad, condición, excepción, alcance, modalidad, cuantificador). El reporte da las dos cifras, con y
       sin remisiones.
    3. Las recomendaciones («es deseable», «se recomienda», «es conveniente», «debería») son normativas, como
       modalidad de consejo.
    4. «Habilitante» se lee con la definición del pre-registro de ESQ-3b v2 (`40493c9`) y el §4 de la enmienda 7
       (`44c6e1b`): una norma cuyo efecto es que un sujeto pueda realizar algo.
    5. Las omisiones cuyo tramo está en el texto heredado se reportan aparte; la pérdida real se cuenta sobre el tramo
       propio.
  Medida complementaria del punto 7, declarada posterior al resultado: además de la cifra del criterio sellado por
  unidad, el segundo tramo computa una medida descriptiva por supuesto: de todos los supuestos identificados en las
  fichas de las 30 unidades, cuántos quedaron como Condicion con su relación hacia la norma que condicionan, cuántos
  dentro de una norma, cuántos fusionados, cuántos omitidos y cuántos sin relación, con su intervalo de Wilson al
  95 %, desglosado por documento. La cifra del criterio sellado no cambia.
  Regla de la cola humana: con la propuesta de la instancia (12 con error de 30; 13 si la dudosa cuenta) el límite
  superior de Wilson al 95 % de la tasa de error es 0,577 (0,608), y la regla del 25 % de la enmienda al protocolo
  (`docs/enmienda_protocolo_entre_tandas_2026-10-04_cola_humana.md`, §1, punto 6, que tolera hasta 2 errores en 30) se
  dispara: las 74 unidades de la cola humana de la tanda 0 se re-procesan o salen del grafo evaluado de esta tanda,
  y se reporta cuál de las dos y por qué. Cuál, lo decide la autora tras la adjudicación: PENDIENTE.
  Adjudicación (06/10/2026, tras el commit del primer tramo en `be6b074`), por mayoría de tres lecturas: la de la
  instancia, la de la revisión (completas en los puntos 1, 6, 7 y 8) y una tercera de la autora en los puntos 7 y 8.
  Punto 1: `cap::6.2.2.4` sin error. Punto 5: vale la propuesta, declarado sin segunda lectura. Punto 6: vale la
  propuesta, incluidas las 3 dudosas. Punto 7: `polcre::7.1.2` no_cumple con la etiqueta sin_relacion; `ric::9.1.3`
  no_cumple. Punto 8: con marca 14 (`lingob::3.2::intro`) y 26 (`cla::6.5.5.9`) normativas y dudosas (modalidad y
  alcance); en lo demás vale la propuesta. No hay control al azar con una lectura adicional de la autora: el control
  es la coincidencia de dos lecturas independientes completas de los puntos 1, 6, 7 y 8, con una tercera en los
  puntos 7 y 8, y la adjudicación de la autora sobre las divergencias.

- **06/10/2026 — decisiones de la autora sobre el FRENO T4, segundo tramo (`data/experiment/reext_t0/freno_t4_tramo2.md`,
  sin commit al escribir esta nota; primer tramo en `be6b074`, nota anterior en `04cec96`).**
    1. Cola humana. Con la adjudicación, 12 de 30 unidades con error (Wilson al 95 %: 0,246–0,577): la regla del 25 %
       se dispara, y la autora decide que las 74 unidades de la cola humana de la tanda 0 **salen del grafo evaluado de
       la tanda 0**, como fija la enmienda al protocolo del 04/10/2026 (§1, punto 6). La forma de la salida (un
       ensamblado nuevo sin las 74, o un filtro sobre el grafo sellado en la carga y en la evaluación) queda PENDIENTE,
       a decidir con la comparación de la revisión.
    2. Fe de erratas de la decisión 2 de la nota del 06/10/2026 (`04cec96`): las siete clases del contador de
       omisiones `meta_normativo` (`data/experiment/pyd_r2/code/validador_r2.py`, `MARCAS_META_NORMATIVO`) son deber,
       prohibición, facultad, condición, excepción, alcance y modalidad; la nota decía «cuantificador» en lugar de
       «prohibición». La decisión no cambia (una remisión sin contenido propio cuenta solo si trae una de las siete
       clases) y ninguna cifra cambia: las 5 remisiones puras no traen ninguna clase de las dos listas.
    3. Decisiones posteriores (06/10/2026, con el segundo tramo commiteado en `889b2f9`). La forma de la salida es la
       (a): un ensamblado nuevo sin la cola, en una unidad corta después de T5 (nombre propuesto: U-SINCOLA-T0;
       registrada en `docs/plan_tesis.md`, B2.11), con `ensamblar_tanda0.py --sin-cola` y el criterio de toda la
       procedencia en la cola (313 nodos y 1.503 aristas salen; los 21 nodos compartidos se quedan), su sello, su
       entrada en la suite (las expectativas de la entrada r2b sellada, sin cambiar ninguna; lo que difiera por la
       salida de la cola, declarado) y su recarga en Neo4j. T5 la reporta y no la ejecuta.
    4. Adjudicación de la clasificación por supuesto del punto 7: en `ext::4.1.3.2`, «emisoras no financieras» va
       **dentro de una norma** (es el sujeto de la Operacion por `aplica_a`), no omitido, como lo leyó la revisión.
       Cifras por supuesto que quedan, sobre 137 (Wilson al 95 %): Condicion con relación 43 (0,242–0,396), dentro de
       una norma 77 (0,478–0,642), fusionados 7 (0,025–0,102), omitidos 2 (0,004–0,052), sin relación 8 (0,030–0,111).
       Observación que se declara con el denominador: las filas de la fase A que enumeran (i) a vii), a) a d), i) a
       iii), los tres «cuando») se cuentan por miembro, y dos filas («desde el 14/04/25 con pagos a la vista», en
       `ext::10.4.4` y `ext::10.3.6`) se parten en fecha y porción; la columna `miembro` de `tasas_t4.json` lo
       documenta. La cifra del criterio sellado (1 de 30) no cambia.
- **06/10/2026 — decisiones de la autora sobre el FRENO T5, final (`data/experiment/reext_t0/freno_t5.md` y
  `reporte_u_reext_t0.md`; T4 en `be6b074` y `889b2f9`, notas en `04cec96` y `c9d4c40`): CIERRE DE LA UNIDAD.**
  1. Revisión de la mesa, sobre una copia sin enlaces (0 enlaces; sha256 de las carpetas que la corrida puede tocar antes y
     después, 513 archivos, sin cambios; 2.213 `.pyc`): `t5/comandos_t5.sh` corrido entero; `anexo_cifras_t5.md` byte a byte
     igual al del repo y al del paquete; `anexo_cifras_t5.json` igual salvo los sha de `suite_diez_r2b.json` y
     `suite_desarrollo_r2b.json`, que llevan la ruta de escritura (P20, punto 6); controles a–r iguales a
     `controles_t3bis.json`; el tablero derivado igual al del repo; shapes, selftest de claves (A1r y A3r OK, JSON igual byte
     a byte al que T5 copió al repo), preguntas sin cola y reparación acotada iguales; las consolas de la suite difieren solo
     en la línea «escrito:» con la ruta. Gasto final 50,401698 de 80. `git diff` de `tabla_reprocesamiento.md`: solo F05
     (`:140`), F10 (`:150`), F14 (`:157`) y el §5 (`:340-375`, dentro de `:338-392`).
  2. El enlace `.venv` momentáneo en la copia de la instancia (contra la regla l, declarado por ella): la comparación de sha
     de la instancia (cambian solo la tabla, el JSON del selftest y el `debug.log` de Neo4j, que git ignora) y el control de la
     mesa (ningún archivo de `.venv` del repo modificado el 06/10/2026 después de las 12:00) confirman que nada se escribió a
     través del enlace. Queda como error declarado, sin efecto.
  3. Correcciones autorizadas por la autora sobre las cuatro desactualizaciones que T5 reportó sin tocar: tablero de
     correcciones `:55` (el `kg_sha256` de la fixture está completo desde `c9540c0`); tabla de reprocesamiento, §4 (nota a
     A1r y A3r, que dan OK) y sus notas de `:129`, `:187-188`, `:220` y `:245` (la enmienda 3 al protocolo está firmada,
     `0cb0c70`); `docs/insumos_escritura.md` §7, ítem 2 (son 26 de 30 unidades con un supuesto dentro de una norma tras la
     adjudicación de `ext::4.1.3.2`, recontado sobre los 137 supuestos; cifras finales del punto 8); checklist P20, punto 3
     (`selftest_clave_cache` da OK; queda `selftest_canal_abierto_e1`). Pendientes que la mesa vio y no estaban autorizados: el
     §6 de la tabla (`:405` y `:414`) repite «NO_VERIFICABLE hasta que existan las dbs», y la nota de `:129` dice «F13
     pendiente de R1 de U-RERESOL-CAT» cuando R1 ya cerró (`c98093a`).
  4. Lo que sigue, según el reporte y las decisiones del día: U-SINCOLA-T0 (grafo evaluado sin la cola, forma (a); mandato
     en borrador); la unidad de mantenimiento de la fila P20 (ocho puntos); las correcciones en código que salieron de T4,
     en una unidad propia entre tandas; el experimento de comparación de modelos de E1 en B6.4, con los dos hallazgos de T4
     como línea de base; la forma A del vínculo declarada límite (condición 6, checklist `:81`).
  5. Con el commit de este freno, del reporte, de `t5/` y de estas correcciones, U-REEXT-T0 queda CERRADA. Commit PENDIENTE
     de la autora.
