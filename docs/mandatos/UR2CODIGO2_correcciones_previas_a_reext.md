FIRMADO por la autora el 03/10/2026

MANDATO — U-R2-CODIGO-2: CORRECCIONES DE CÓDIGO PREVIAS A LA RE-EXTRACCIÓN DE LA TANDA 0.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad chica, en DOS ETAPAS con FRENO obligatorio al final de cada una: C1 (diagnóstico, censos y
  diseño, sin editar el código de la cadena) y C2 (implementación y controles). Reporte corto (no más
  de 40 líneas) y espera del «seguí» escrito de la autora. Ninguna etapa arranca sin él.
- Costo de API: USD 0 en las dos etapas. Ninguna llamada a la API; Neo4j no se usa.
- Corre antes de U-REEXT-T0 (plan, B2.11, unidad 11, docs/plan_tesis.md:400).

CONTEXTO. La medición de U-MED-R2A cerró con seis hallazgos que se corrigen en código antes de
re-extraer los diez TOs de la tanda 0 (`git show 4244028:data/experiment/medicion_r2a/m3_freno.md`):
- M3.b: de las 30 citas a puntos inexistentes de diez, 18 son del detector (la cita es de otra norma y
  se leyó como interna del TO de origen; quedaron irresolubles) y 7 tocan el bloque 4.4 de ric, que E0
  no segmentó (2 de categoría E0 y 5 no decidibles);
- M3.c: la pasada residual de E4 tiene 24 propuestos y propone 0 resoluciones;
- M3.d: dos plazos con cuantía temporal fueron a `frecuencia` («24 hs. hábiles» y «hasta el quinto día
  hábil posterior al vencimiento…»), porque la detección de cuantías no reconoce «hs.» ni el ordinal;
- mediciones adicionales: 2.540 de las 3.801 menciones en texto heredado de diez (1.859 de 2.993 en
  desarrollo) son la línea «Sección N.» leída como cita de su propia sección; y 4 unidades de diez y 3
  de desarrollo quedan sin validación porque E1 devolvió una salida mal formada.
U-PROMPT-R2 está en curso y escribe en archivos que esta unidad también toca (runner_corpus.py,
ensamblar_tanda0.py, el perfil de E1). Por eso C1 no edita la cadena, y C2 tiene una precondición.

PRECONDICIONES. Verificalas con git log y git status antes de cada etapa; si alguna no se cumple,
FRENO sin escribir nada.
- C1: M3 de U-MED-R2A commiteada (`4244028`).
- C2: P2 de U-PROMPT-R2 commiteada, y ningún archivo de las escrituras de esta unidad con cambios sin
  commit de otra sesión.

Leé completos, antes de escribir una línea:
- la fila de la unidad 11 del plan (:400) y las notas fechadas del mandato de U-PROMPT-R2
  (docs/mandatos/UPROMPT_R2_prefijo_nuevo.md);
- data/experiment/medicion_r2a/m3_freno.md y las lecturas de M3.b y M3.d (m3/lecturas/), en `4244028`;
- la enmienda 2 de L-ESQ-R2 (`git show 5f9a731:data/experiment/esq/enmienda2_L-ESQ-R2_remite_a_2026-10-02.md`)
  y las reglas (a) a (i) de las remisiones (data/experiment/r2_codigo/reglas_remisiones_postR3.md);
- docs/decisiones_caching_extraccion.md, cinco decisiones vinculantes (para el punto b);
- data/experiment/mantenimiento/tabla_reprocesamiento.md (clases y filas F01 a F05);
- el código que se toca: corpus_v2/r1_referencias.py, corpus_v2/runner_corpus.py,
  e1_extractor/cliente_e1.py, data/experiment/pyd_r2/code/reglas_comparacion.py y validador_r2.py,
  data/experiment/tanda0/code/ensamblar_tanda0.py, y e0_chunking/e0_lib.py y correr_e0.py.

DECISIONES YA TOMADAS. No se re-deciden.
1. La pasada residual de E4 se retira del perfil r2 (decisión de la autora del 03/10/2026, con M3.c;
   es la decisión 6 del mandato de U-MED-R2A).
2. Esta unidad no cambia el prefijo, el tool schema ni el mensaje de E1, ni la NOTA ni el prefijo de
   E3: eso es de U-PROMPT-R2.
3. De las reglas de `remite_a` solo cambia lo del punto (a). La atribución de la remisión al nodo es
   otra unidad, posterior a U-REEXT-T0 (plan, :400).
4. Los perfiles existentes dan el resultado byte a byte igual: todo cambio de comportamiento rige
   solo con el perfil r2.
5. Los grafos r2a versionados (KG-Tanda0-Diez-r2a, `99fe2bfa…`; KG-Tanda0-Desarrollo-r2a, `93a7af72…`),
   la E0 e0-r2 versionada (salida_tanda0_r2/, `f8dedd4`) y la entrada r2 de la fixture
   (`estado_esperado` `f8246902…`, `c50b094`) no se pisan ni se re-sellan: los controles corren sobre
   copias y reportan la diferencia. Re-sellar es decisión de la autora.
6. El reintento del punto (b) se prueba con el cliente simulado. Las llamadas reales son de
   U-REEXT-T0, dentro de su tope de USD 69.
7. Una cita sin norma nombrada a un punto que el TO de origen no tiene (patrón (3) del punto a) queda
   irresoluble: no se adivina la norma (decisión de la autora del 03/10/2026).

TAREA

C1 — Diagnóstico, censos y diseño. USD 0. No edita el código de la cadena: sus scripts y reportes van
en data/experiment/r2_codigo2/ (se crea).
a. Detector de citas externas, por patrón. Las 18 filas «detector» de M3.b quedaron irresolubles: no
   crearon ninguna `remite_a` falsa, porque el número leído como interno no existía en el TO de origen.
   Lo que hay que medir y corregir es el mismo error cuando el número sí existe en ese TO. Para cada
   fila, decí qué regla y qué línea de r1_referencias.py la clasifica como interna (`:185`, `:194`).
   Los tres patrones:
   (1) número seguido del nombre de otra norma, con o sin título intermedio: «de la NIIF 9», «de las
       normas de “X”», «de las normas “X”», «de la “Reglamentación de la cuenta corriente bancaria”»
       (B01, B03, B04, B07, B08, B10, B11, B12 y B16). Nunca es interna. Si la norma nombrada es un TO
       del corpus, se resuelve como externa a ese TO.
   (2) «del Anexo de la Comunicación A NNNN» (B13, B14, B15 y B17): va al registro de citas a
       Comunicaciones (`comunicaciones_registro.json` del ensamblado).
   (3) cita sin norma nombrada a un punto que el TO no tiene, por continuación de una cita anterior o
       dentro de un modelo (B19, B21, B22, B29 y B30): queda irresoluble (decisión 7).
   Proponé la regla de los patrones (1) y (2).
   Censo: sobre los dos grafos r2a, las aristas `remite_a` internas que hoy crea el patrón (1) cuando
   el número existe en el TO de origen. Son relaciones falsas: contalas y listalas, con su chunk, su
   tramo y la norma nombrada.
b. Reintento ante una salida de E1 mal formada. Caracterizá las 4 unidades de diez (`cap::5.3.2.3`,
   `ext::6.5.3`, `ric::6.3` y `ctacte::5.6.1`) y las 3 de desarrollo (las tres primeras): qué trae el
   crudo (falta `relations`; `entities` viene como texto), dónde lo rechaza la cadena
   (pyd_r2/code/validador_r2.py:487; e1_extractor/validador_e1.py:232) y por qué hoy no se reintenta.
   Diseñá el reintento, solo con el perfil r2: cuándo dispara, su tope por unidad, su namespace y su
   clave de caché (decisiones de caching), dónde se persiste el crudo del reintento y qué pasa cuando
   el tope se agota. Precedente: el reintento por corte (cliente_e1.py:68; runner_corpus.py:523).
   Decí además si alguno de los casos admite una reparación determinística sin llamar a la API; es una
   opción para la autora, no se adopta sin su decisión.
c. Cuantías. Qué formas no reconoce `detectar_cuantias` (reglas_comparacion.py:185): «hs.» y los
   ordinales («quinto día hábil»), y las que aparezcan al buscarlas. Censo sobre los textos de los diez
   TOs: cuántas cuantías nuevas se detectan, cuántos elementos de umbral cambian en los grafos r2a y
   cuántos plazos dejan de ir a `frecuencia`.
d. Contador de menciones en texto heredado. Definí el contador sin el encabezado de sección leído como
   cita de sí mismo (r1_referencias.py:1198). Listá, con path:línea, cada documento o artefacto que
   cita la cifra vieja, incluido reglas_remisiones_postR3.md:102 (2.870, sin verificar si está
   inflada), y proponé el texto de la fe de erratas. La unidad no edita el plan ni el tablero.
e. Pasada residual de E4. Qué código y qué salidas la componen en el perfil r2
   (ensamblar_tanda0.py:868-873; e4_pasada_residual_medida.json) y qué lector depende de ellas.
f. Segmentación del bloque 4.4 de ric, entero: 4.4, 4.4.1, 4.4.2, 4.4.3 y 4.4.4. Hay dos causas a
   diagnosticar:
   - «4.4.3. Riesgo de cambio» y «4.4.4. Riesgo de posiciones en opciones» son encabezados del PDF (p.
     18) y quedaron dentro del texto de `ric::4.3.3` (páginas 15 a 18), en la E0 legada y en e0-r2
     (B26 y B27 de M3.b);
   - 4.4, 4.4.1 y 4.4.2 ni siquiera aparecen en el texto extraído; las citas que los nombran hablan de
     un «modelo inserto» y de un «Cuadro inserto» (B18, B23, B24, B25 y B28).
   Proponé la corrección en e0-r2 y decí si va dentro de e0-r2 o pide otra versión de E0, y qué
   implica para la clave de caché. Censo: qué ids cambian en los diez TOs de la tanda 0 y en los 152
   TOs de la partición con la corrección.
g. Dos lecturas de M3.b a verificar, sin cambiar los veredictos: B02, si el punto 3.6 de cap existe en
   el PDF; y B20, si el párrafo de `ric::12.1.2` nombra otra norma antes de citar el 5.1.2.1. Reportá
   lo que encuentres, con la página del PDF y el texto.
FRENO C1: el reporte, la tabla de las seis correcciones (qué archivo cambia, qué cambia en los grafos
r2a, qué decide la autora), los censos y el resultado de (g). La autora decide qué entra a C2.

C2 — Implementación y controles. USD 0.
Implementá lo aprobado en el FRENO C1, con sus selftests. Control de cada punto:
a. patrón (1): las nueve filas dejan de clasificarse como internas, el caso NIIF 9 no resuelve a
   `cap::5.5` y las que nombran un TO del corpus se resuelven como externas a ese TO; patrón (2): las
   cuatro filas van al registro de citas a Comunicaciones; patrón (3): las cinco siguen irresolubles;
   y las `remite_a` internas falsas del censo de C1 dejan de crearse, con la lista de las que cambian;
b. con el cliente simulado, las 4 unidades de diez y las 3 de desarrollo disparan el reintento y, con
   una respuesta bien formada, dejan de quedar sin validación; agotado el tope, quedan en una lista
   declarada; con los perfiles existentes no hay reintento y los requests son byte a byte iguales;
c. «24 hs. hábiles» y «hasta el quinto día hábil posterior al vencimiento…» se detectan como cuantías;
   el selftest de las reglas pasa con los casos nuevos; el censo de los elementos que cambian;
d. el contador nuevo en los dos grafos (hoy 3.801 y 2.993, con 2.540 y 1.859 autocitas de encabezado),
   sin que cambie ninguna arista `remite_a` por este punto;
e. el perfil r2 ya no corre la pasada residual, y el grafo no cambia por este punto;
f. `ric::4.4.3` y `ric::4.4.4` aparecen como unidades con su texto; 4.4, 4.4.1 y 4.4.2 también, si el
   diagnóstico de C1 muestra que su texto se puede extraer, y si no, quedan declarados con su causa;
   en el resto de la tanda 0 y de los 152 TOs no cambia ningún id salvo los declarados.
Controles de siempre, sobre copias (regla l):
- la E0 legada de los diez TOs de la tanda 0, reproducida (34 de 34 archivos);
- los tres ensamblados sellados (`eab2fdd0…`, `dd42d6d9…` y `4097d4fd…`), reproducidos con `--entrada`
  de ruta absoluta;
- los dos grafos r2a, reproducidos salvo los cambios declarados: la diferencia de nodos y aristas, por
  causa;
- la suite del perfil r2 contra la entrada sellada y las shapes, sin regresiones; todo ítem que cambie
  de estado se reporta;
- doble corrida byte a byte idéntica de lo que la etapa escribe.
FRENO C2, final: la tabla de controles, las diferencias contra r2a por causa, los selftests y la lista
de lo que U-REEXT-T0 hereda de esta unidad.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–l), en las dos etapas.
- Escrituras, y solo estas:
  - C1: data/experiment/r2_codigo2/ (se crea) y tu scratchpad;
  - C2, además, según lo aprobado: corpus_v2/r1_referencias.py (a, d); corpus_v2/runner_corpus.py y
    e1_extractor/cliente_e1.py, solo para el reintento del perfil r2 (b);
    pyd_r2/code/reglas_comparacion.py (c); tanda0/code/ensamblar_tanda0.py (e, y d si el contador se
    reporta ahí); e0_chunking/e0_lib.py y correr_e0.py, solo en la versión e0-r2 (f); y los selftests
    de esos módulos.
  - No se editan: los prefijos, los prompts y los perfiles sellados; modelos_r2.py, validador_r2.py y
    validador_e1.py; prompt_e3.py y ratchet_e3.py; e0_tablas.py; la suite, las shapes y la fixture;
    data/experiment/prompt_r2/ y data/experiment/medicion_r2a/; los grafos y las E0 versionados; el
    plan, el checklist, el tablero, los laudos ni el backlog. Nada sellado se toca (CLAUDE.md §3).
    No commitees.
- Fuentes firmadas por commit (regla k) y verificaciones sobre copia armada copiando, con el sha256
  del repo antes y después (regla l).
- Python: PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; ningún .pyc nuevo, con línea de base al
  inicio y control al cierre; las dbs de caché solo con `file:…?immutable=1`.
- Afirmaciones y citas: path:línea o comando; conteos recomputados antes de escribirse; lo que no esté
  en un artefacto es NO ENCONTRADO; cero nombres propios.
- Si algo de este mandato contradice un archivo del repo, mandan los archivos y se reporta la
  contradicción.
- Paquete de revisión revision_UR2CODIGO2_C<n>/ por etapa, con manifest.txt y nombres únicos.
- Shell zsh: variables entre comillas o como arrays; ningún comentario con # dentro de los bloques de
  comandos para copiar.

CRITERIO DE ACEPTACIÓN por etapa:
- el reporte corto con las salidas pedidas y sus casos de control;
- git status --short con solo los archivos autorizados de la etapa;
- la reproducción byte a byte de lo sellado con los perfiles existentes;
- doble corrida byte a byte idéntica de lo que la etapa escribe;
- el grep de convenciones, pegado aunque dé vacío.

FRENO al final de cada etapa.

NOTAS POSTERIORES A LA FIRMA. El texto firmado no se edita; estas notas se leen junto con él.
- **04/10/2026 — firma, cierre de C1 y decisiones de la autora sobre el FRENO C1.** La firma está
  commiteada en `95dfd98` y C1 en `92dc684` (`data/experiment/r2_codigo2/freno_c1.md`). La revisión
  reprodujo byte a byte las 15 salidas de C1 sobre una copia del repo. C1 corrige dos supuestos de este
  texto, que se leen con él:
  - punto (a): el patrón (1) no crea ninguna `remite_a` falsa en los grafos r2a. Las falsas son 11 en
    cada grafo y vienen del patrón (2): la cita de `ext::10.4.4` al «punto 10.3.6. del Anexo de la
    Comunicación A 7914», resuelta contra `ext::10.3.6`;
  - punto (f): el texto de 4.4, 4.4.1 y 4.4.2 sí está extraído. El PDF de ric lo imprime en la p. 16 con
    los números 4.3, 4.3.1 y 4.3.2; es un error de numeración de la norma.
  Decisiones de la autora para C2, las de su «seguí»:
  1. (a) La regla que propuso C1. Patrón (1): nunca interna; externa si la norma nombrada es un TO del
     corpus. Patrón (2), Anexo de una Comunicación: irresoluble con su causa propia, y la cita entra al
     registro de citas a Comunicaciones. Patrón (3): irresoluble.
  2. (b) Un reintento por unidad, con el mismo pedido y namespace propio (sufijo `-rforma1`), solo con
     el perfil r2. Sin reparación determinística. Si se agota, la unidad va a una lista declarada.
  3. (c) Se suman «hs.», «hábil» en singular y «o más». Los ordinales, solo con marcador de comparación
     («hasta el», «dentro del», «a más tardar»). C2 lista cada elemento de umbral que cambia por «o más».
     Control: ningún elemento hoy correcto cambia, incluida la base del 25 % de `cap::6.11`.
     «o más» pegado a la cuantía ya tiene regla desde la calibración de P3 de U-PYD
     (`git show 57a8dd2:data/experiment/pyd_r2/code/reglas_comparacion.py`, «solo pospuestos y pegados a
     la cuantía»); lo nuevo es la forma con «o más» entre el paréntesis y la unidad (`freno_c1.md`, §c).
  4. (d) El contador nuevo, sin las autocitas de encabezado. Las 7 autorreferencias salen del registro
     de citas: no son citas.
  5. (e) La clave de la pasada residual queda en el reporte, marcada como retirada, para que
     `data/experiment/medicion_r2a/m2_medicion.py:294` siga leyéndola.
  6. (f) ABL: los tres encabezados de la p. 16 de ric se renumeran por una lista explícita, solo para
     ese bloque, y la unidad guarda el número tal como está impreso, en sus flags, con la corrección
     declarada. Control: las citas a 4.4.1 y 4.4.2 resuelven; los otros 9 TOs de la tanda 0 y los 152 de
     la partición no cambian ningún id.
  7. La salida nueva de e0-r2 es la que lee U-REEXT-T0. La pareada de U-PROMPT-R2 usa la E0 versionada
     en `f8dedd4`, y lo declara.
  Escritura que se suma a las de C2: `data/experiment/r2_codigo/selftest_r3.py`, solo para sumar los
  casos nuevos.
  La fe de erratas del punto (d) la asienta la revisión, no la unidad
  (`data/experiment/r2_codigo/reglas_remisiones_postR3.md`, nota del 04/10/2026).
  C2 arranca cuando P2 de U-PROMPT-R2 esté commiteada (precondición de este mandato); el «seguí» está
  PENDIENTE de envío.
- **04/10/2026 — salida nueva de e0-r2 de la tanda 0 (decisión de la autora).** Precisa el punto 7 de la
  nota anterior. La salida nueva de e0-r2 de los diez TOs de la tanda 0 la genera C2, en un directorio
  nuevo y versionado: `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/`. Es una escritura
  autorizada, que se suma a las de C2. `salida_tanda0_r2/` (`f8dedd4`) no se pisa. U-REEXT-T0 lee la E0
  de ese directorio; la pareada de U-PROMPT-R2 sigue con la versionada en `f8dedd4`.
  Control:
  - doble corrida, en dos directorios, byte a byte idéntica;
  - contra `salida_tanda0_r2/`, los archivos de los otros 9 TOs son iguales byte a byte;
  - en ric cambian solo los ids declarados: se agregan `ric::4.4::intro`, `ric::4.4.1`, `ric::4.4.2`,
    `ric::4.4.3` y `ric::4.4.4`, y cambia el texto de `ric::4.3.3`; ningún otro id de ric cambia;
  - en los archivos agregados de la salida (`conteos.json` y los demás), cambia solo la entrada de ric.
  C2 no edita los manifiestos r2b (`20b7f60`), que apuntan a `salida_tanda0_r2`: el manifiesto que lea
  U-REEXT-T0 se fija en su mandato.
- **04/10/2026 — orden con U-PROMPT-R2 y manifiestos (decisiones de la autora).** C2 arranca sobre el
  commit de P3 de U-PROMPT-R2. Se suma a las precondiciones de C2, porque las dos etapas editan
  `corpus_v2/runner_corpus.py`. Los manifiestos r2b los actualiza U-REEXT-T0 como su primer paso, para
  que lean `salida_tanda0_r2b/`; C2 no los toca. La pareada de U-PROMPT-R2 (P4) sigue con la E0 de
  `f8dedd4`.
- **04/10/2026 — punto (h): tope de la herencia en e0-r2 (decisión de la autora).** Se suma a C2.
  Hallazgo de la revisión de U-NOSEG-LIMITE (`7aed71c`): `e0_chunking/e0_lib.py:1618-1650`
  (`herencia_de`) le da a cada unidad el título y todos los segmentos no terminales de cada ancestro
  (intro, intersticial y cierre), sin tope. El umbral de tamaño (`correr_e0.py:74`) solo parte el texto
  propio de las unidades terminales. E1 imprime la herencia entera. En la partición de 152 TOs, 95
  unidades de 11 TOs heredan más de 13.091 caracteres, con un máximo de 264.912; en la tanda 0 hay una
  sola, `ric::11.2.3`, con 15.170 (medición sobre `segmentacion_84/b584_particion/` y sobre
  `salida_tanda0_r2/`).
  C2 empieza por el diseño del recorte: lo presenta en un FRENO intermedio corto, sin implementarlo, y
  espera el «seguí». Condiciones del diseño:
  1. conserva los títulos de todos los ancestros y el final de cada bloque heredado, donde está la
     cláusula que abre la lista y que la regla de composición del prefijo necesita;
  2. dice qué hace con los cierres, que a veces valen para todos los ítems («lo dispuesto
     precedentemente no rige para…»);
  3. mide cuántas unidades cambian y qué texto se recorta, en la tanda 0 y en los 152 TOs;
  4. rige solo en e0-r2, y el recorte queda declarado en la unidad.
  El umbral de referencia es 13.091 caracteres, el tamaño objetivo de una parte (`correr_e0.py:75`); el
  diseño puede proponer otro, con su medición. Lo que el punto (h) cambie en la tanda 0 se suma a los
  cambios declarados del control de `salida_tanda0_r2b/`.
- **04/10/2026 — puntos (i) a (l): agregados a C2 que salen de la revisión independiente (decisión de la
  autora).** Fuente: `reports/u_revision_libre/freno_b1.md`, pieza 2 (commit PENDIENTE).
  i. Comparación invertida o con el borde equivocado (1.9), en `pyd_r2/code/reglas_comparacion.py`: la
     negación que queda fuera del alcance de la regla y «igual o superior» leído como estricto.
     Referencia de la revisión: 12 de 79 umbrales de reglas simples.
  j. «Ponderador» que pisa al comparador pegado a la cuantía (1.10). Referencia: 28 de 140 `coeficiente`.
  k. La comparación lee el marcador del segmento del encabezado en un tramo compuesto (`cap::8.5.1` a
     `8.5.3`, «límites mínimos»): hoy da `no_determinada`. Se prueba con el tramo de dos segmentos del
     diseño del prefijo, sobre un caso sintético.
  l. Las colas de título que son texto de la norma (2.3), en `e0_chunking/e0_lib.py`, solo en e0-r2. De
     73, 6 son norma, todas en ric (pp. 15, 30, 54 y 59). Cambia el texto de `ric::4.3.1.2`,
     `ric::6.1.2`, `ric::11.2::intro` y `ric::12.4`: se suma a los cambios declarados del control de
     `salida_tanda0_r2b/`.
  Control de i, j y k, como en (c): la lista de cada elemento que cambia en los dos grafos r2a, y ningún
  elemento hoy correcto cambia. Control de l: los renglones recuperados, con su página; y en los otros 9
  TOs de la tanda 0 y en los 152 de la partición, ningún renglón se pierde ni se gana sin declarar.
  No entran a C2:
  - el plazo sin marcador asumido como máximo (1.8): es regla de L-ESQ-R2 §1.3 (`4ef7650`) y cambiarla
    pide una enmienda firmada;
  - los cambios de E0 que mueven ids de la partición (1.14, 1.15 y 2.4): van en la etapa previa de
    U-SEG-OFICIAL.
  Orden: C2 arranca sobre el commit de P3 de U-PROMPT-R2. Comparte `pyd_r2/code/selftest_pyd_r2.py` con
  la etapa P3b de esa unidad: las dos implementaciones no corren a la vez.
- **04/10/2026 — puntos (m) a (r): agregados a C2 (decisiones de la autora).** Salen de la enmienda 3 a
  L-ESQ-R2, del FRENO P3 de U-PROMPT-R2 (`data/experiment/prompt_r2/freno_p3.md`, §5; commit de P3 PENDIENTE)
  y de la verificación de la sección 4.5 de la tesis. Rigen solo con el perfil r2 y la fase r2b: los grafos
  r2a sellados se siguen reproduciendo byte a byte.
  m. Plazo sin marcador (enmienda 3 a L-ESQ-R2,
     `data/experiment/esq/enmienda3_L-ESQ-R2_plazo_sin_marcador_2026-10-04.md`, FIRMADA por la autora el
     04/10/2026; commit de la firma PENDIENTE). En `pyd_r2/code/reglas_comparacion.py:443-447`, el plazo sin
     marcador recibe `no_determinada`, conserva la regla `sin_marcador_plazo` y no lleva la marca
     `comparacion_asumida`; el docstring (`:44-45`) se alinea. En `selftest_pyd_r2.py`, los cuatro casos que
     hoy esperan la marca pasan a esperar `no_determinada`. Referencia: 176 elementos en diez y 157 en
     desarrollo.
  n. Versión y materia del TextoOrdenado (FRENO P3, §5.1). La decisión 16 del mandato de U-PROMPT-R2 dice
     que se derivan «como ya hace la canonización de E4», pero E4 deriva solo el archivo
     (`corpus_v2/r1_e4.py:228`).
     - e0-r2 (`e0_chunking/e0_lib.py`, solo en esa versión): antes de recortar el pie de cada página
       (`separar_encabezado_pie`, `pie_desde_version`), guarda como metadato de la salida la versión, la
       Comunicación y la fecha que trae el pie, por página.
     - El ensamblado r2b (`tanda0/code/ensamblar_tanda0.py`) pone en el TextoOrdenado la versión vigente y la
       materia. La materia sale del título del inventario, que el ensamblado ya lee
       (`r1_referencias.titulos_de_inventario`, `ensamblar_tanda0.py:588`).
     - El diseño se presenta en el freno de diseño con el que empieza C2, junto con (h), sin implementar. Dice
       cómo se define la versión vigente de un TO a partir de los pies de sus páginas, dónde se guarda el
       metadato y qué pasa con las páginas sin pie y con los pies que no se leen.
     - Condiciones: el texto de las unidades y el mensaje de E1 no cambian; los `chunks_<to>.json` de los
       otros 9 TOs siguen byte a byte iguales a los de `salida_tanda0_r2/` (el metadato va en un archivo
       propio por TO, o el diseño propone otra forma que conserve ese control).
     - Medida de la revisión sobre los diez TOs (736 páginas): 608 traen un pie que se lee, 119 no traen pie
       (carátula, índice y tabla de origen) y en 9 el pie no se lee (cla 5, lingob 2 y polcre 2). La
       Comunicación del pie más reciente coincide con la «Última comunicación incorporada» de la carátula en
       los 8 TOs donde la carátula se lee; ric no tiene carátula y la de pagjub trae un carácter sin mapear.
  o. Límite relativo y cuantía en la misma entidad (FRENO P3, §5.3). `llenar_umbrales_r2` reemplaza la lista
     (`ensamblar_tanda0.py:750-751`) y el elemento relativo que deja `validador_r2` se pierde. La lista se
     completa, no se reemplaza. Sobre los dos grafos r2a no cambia ningún elemento, porque el límite relativo
     existe solo con la forma «r2»: la prueba es un caso sintético con los dos elementos en la misma entidad.
  p. Omisiones en el ensamblado (FRENO P3, §5.4). El ensamblado r2b escribe `omisiones.jsonl` en su salida,
     con la categoría, el tramo y la nota de cada omisión, y con `source` y `destino` cuando los trae: es
     donde lo lee LN-7 (`scripts/regression_kg.py:1777-1785`), que hoy da no_aplicable. La suite no se edita.
  q. Aristas derivadas que tocan un nodo que solo viene de la cola humana (FRENO P3, §5.6). El ensamblado
     marca la cola (`ensamblar_tanda0.py:829`) antes de derivar `remite_a` (`:881`) y `establecida_en`
     (`:892`), y esas aristas quedan sin la marca: 788 en diez y 763 en desarrollo. El ensamblado r2b las
     cuenta aparte, después de derivar: por predicado, en su reporte, con la lista en un archivo de la salida.
     La marca en la arista no entra a C2: `AristaR2` admite en `remite_a` solo `alcance`, `destino` y
     `evidencia`, y en la `establecida_en` derivada ninguna propiedad (`pyd_r2/code/modelos_r2.py`); llevarla
     pide cambiar ese invariante y es decisión de la autora.
  r. Base de un umbral con el resolvedor de `remite_a` (L-ESQ-R2 §1.3 (c), `4ef7650:254-255`: la base se
     resuelve «por el mecanismo de remisiones»). `resolver_base` (`ensamblar_tanda0.py:640-660`) usa hoy
     `detectar_menciones`, el detector de r1, sin las reglas (a) a (i) de `remite_a`. Pasa a usar el mismo
     resolvedor que `remite_a` (`r1_referencias.detectar_menciones_r2`). Censo: las bases que cambian en los
     dos grafos r2a. Hoy, en diez, 15 resuelven por remisión, 4 por definición y 141 no resuelven; en
     desarrollo, 15, 3 y 136. Caso de control: la base de `cla::5.1.1.1` («importe de referencia establecido
     en el punto 3.7») sigue resolviendo a `cla::3.7`.
  Control de (m) a (r), como en (c): la lista de cada elemento que cambia en los dos grafos r2a, y ningún
  elemento hoy correcto cambia. En (o) y (p) esa lista es vacía y la prueba es sintética.
  Escrituras: las ya autorizadas de C2. Ningún punto suma un archivo nuevo de código.
  Orden: no cambia. C2 arranca sobre el commit de P3, y su implementación no corre a la vez que la de P3b.
- **04/10/2026 — punto (s) y decisiones de la autora sobre (q) y el freno de diseño.** P3 de U-PROMPT-R2 quedó
  commiteada en `4aa92c7`, y la enmienda 3 a L-ESQ-R2 del punto (m), firmada, en `8d01b04`.
  s. El conteo de elementos de extracción sin verificar pasa al reporte del ensamblado r2b. Hoy está solo en
     el reporte del E2 r2 de cada TO (`corpus_v2/runner_corpus.py:1007`, `conteo_paso_por_e3`, escrito en
     `:1089`): entidades sin `paso_por_e3`, relaciones con `no_verificada_e3`, excluidos por no haber pasado,
     unidades sin los índices de E3 y, aparte, la cola humana por estado. El reporte del ensamblado cuenta
     hoy solo las relaciones y las aristas con la marca (`tanda0/code/ensamblar_tanda0.py:841-842` y `:922`).
     El ensamblado r2b lleva a su reporte el conteo entero, por TO y en total: es el que va a leer el control
     que exige cero. Control: en el ensamblado sintético de P3, el total del reporte del ensamblado es la
     suma de los reportes del E2 r2. Solo r2b: el reporte de los grafos r2a sellados no cambia. Entra en la
     implementación, después del freno de diseño.
  Punto (q): se queda como está registrado. Las aristas derivadas que tocan un nodo que solo viene de la cola
  humana se cuentan aparte; no llevan la marca, y `pyd_r2/code/modelos_r2.py` no se suma a las escrituras de
  C2.
  Freno de diseño: C2 empieza por un freno de diseño con (h) y (n), sin implementar.
- **04/10/2026 — la unión de las operaciones por punto va a P3b de U-PROMPT-R2 (decisión de la autora).** Con
  la fase r2b, la Operacion deja de fundirse por etiqueta entre puntos distintos
  (`docs/mandatos/UPROMPT_R2_prefijo_nuevo.md`, nota del 04/10/2026). No es un punto de C2. Lo que le toca a
  C2:
  - P3b puede necesitar una línea en cada sitio de llamada de `e2_lib.ensamblar_r2`
    (`tanda0/code/ensamblar_tanda0.py:825` y `corpus_v2/runner_corpus.py:1061`), para pasarle la fase. Son
    archivos de C2: la implementación que vaya segunda trabaja sobre el commit de la primera;
  - si P3b va primero, la corrida de control de C2 sobre el crudo de r2a con las reglas de r2b incluye la
    separación de las operaciones. C2 la lista aparte, atribuida a P3b, y no la cuenta entre sus cambios.
    Referencia: 37 operaciones pasan a ser 89 en desarrollo y 59 pasan a ser 148 en diez.
- **04/10/2026 — FRENO C2-diseño aprobado, y fe de erratas de las cifras de los pies (decisiones de la
  autora).** El diseño quedó commiteado en `918b9c5` (`data/experiment/r2_codigo2/freno_c2_diseno.md`). La
  revisión reprodujo sobre una copia `c2d_pies.json` y las secciones de la tanda 0 y de la partición de
  `c2d_herencia.json`. Queda aprobado como está:
  - (h): umbral U = 13.091 caracteres y B = 2.000 por bloque. Los cierres conservan su comienzo. El marcador
    de una línea lleva el rol del bloque, y la unidad declara el recorte en `herencia_recortada`. La frase
    del mensaje de E1 que explica el marcador la suma P3b de U-PROMPT-R2.
  - (n): `pies_<to>.json` por TO, solo en e0-r2. La versión vigente es la del pie con la fecha de vigencia
    más reciente entre las páginas legibles; en un empate, la de mayor número. El valor tiene la forma
    «Comunicación A 8378 (vigencia 20/12/2025)». La materia es el título oficial del inventario tal cual, sin
    el punto final, leído sin normalizar de `escalado_prep/inventario_tos.csv` y de `inventario_resumen.json`.
  Fe de erratas de la nota de los puntos (m) a (r) (`8d01b04`), punto n, «Medida de la revisión». De las 736
  páginas de los diez TOs, 617 traen un pie que se lee, 119 no traen pie y ninguna trae un pie ilegible. Las
  119 son 9 de carátula, 40 de tabla de origen y 70 de historial; las páginas de índice sí tienen pie
  (`data/experiment/r2_codigo2/salidas/c2d_pies.json`, `totales`). La nota decía 608, 119 y 9, y «carátula,
  índice y tabla de origen». Causa: la expresión de la revisión no aceptaba la comilla de cierre invertida de
  7 pies de cla y polcre ni el carácter sin mapear en la versión de hoja de 2 pies de lingob, y las páginas
  sin pie se rotularon sin leerlas. La coincidencia con la carátula no cambia: 8 de 8.
  Orden: la implementación de C2 arranca cuando P3b-2 de U-PROMPT-R2 esté commiteada.
- **04/10/2026 — punto (t) y casos de la cadena sintética (decisiones de la autora, tras el FRENO P3b-2 de
  U-PROMPT-R2).**
  t. Las marcas de E3 de la lectura del veredicto como texto y del reintento con menos elementos llegan al
     reporte. Hoy quedan en `finales.jsonl` (`validacion_final.marcas_e3`, claves `lectura_veredicto_e3` y
     `reintento_con_menos_elementos`), y `vistos_por_e3` de `corpus_v2/runner_corpus.py` pasa solo la de la
     copia de la nota. Son dos líneas en esa función, solo con la forma r2: las dos marcas van también en
     `vistos["marcas"]`, y de ahí llegan a la validación y al conteo de E2 (`e2_lib`, `stats["p3b"]`). Con
     los perfiles existentes la salida no cambia. Control: en la cadena sintética de P3b-2, el reporte de E2
     cuenta las unidades con cada marca.
  Control del punto (s): pasa a la cadena sintética de P3b-2
  (`data/experiment/prompt_r2/p3b2/cadena_sintetica_p3b2.py`), que recorre el ratchet, `entrada_r2`, el
  validador, E2 y el ensamblado r2b.
  Cadena sintética de P3 (`data/experiment/prompt_r2/p3/cadena_sintetica_p3.py`): su caso «LÍMITE» de las
  omisiones espera que LN-7 dé no_aplicable sobre el ensamblado. Con el punto (p) pasa a resuelto. C2
  actualiza ese caso esperado y el resumen de la cadena (`p3/salida/resumen_cadena_sintetica_p3.json`): los
  dos archivos se suman a sus escrituras, solo para ese caso.
- **04/10/2026 — FRENO C2 revisado; correcciones antes del commit y enmienda 5 a L-ESQ-R2 en borrador
  (decisiones de la autora).** El freno de la implementación (`data/experiment/r2_codigo2/freno_c2.md`, sin
  commit) se revisó sobre una copia y se reproduce: la E0 `salida_tanda0_r2b/` (57 de 57, doble corrida),
  `c2_cadena.json`, `c2_sinteticos.json` y `c2_e0.json` byte a byte (este, con la partición de los 152 TOs
  corrida de nuevo), `c2_control_repro.json` salvo el control del repo (durante esa corrida escribí estos
  asientos), la cadena de P3 (27 de 27), la de P3b-2 (18 de 20), `selftest_pyd_r2` (378 de 378) y
  `selftest_r3` (109 de 109).
  1. Punto (i), «o no». Un «no» precedido por «o» («sea o no», «haya o no», «represente o no») no niega el
     verbo y queda fuera de la regla. Caso de control: `cap::6.2.2.3`, donde «represente o no un rendimiento
     menor a 3 % anual» pasaba de coeficiente a mínimo inclusivo. Con la corrección, el «3 %» queda como
     máximo estricto, por «menor a».
  2. «Más del» y «menos del» valen como «más de» y «menos de». Esta corrección no es de la autora: la sumé
     al revisar el freno, con su encargo de sumar las correcciones necesarias, y ella la confirma o la saca
     al despachar. En cada grafo r2a cambian 4 elementos (`cla::6.3.2`, `cap::8.4.2.1`, `cla::6.5.4.7` y
     `cap::3.1.11.2`), medidos con una simulación fuera del repo.
  3. Cadena sintética de P3b-2 (`data/experiment/prompt_r2/p3b2/cadena_sintetica_p3b2.py`). Sus casos de
     `:260` y `:289` afirman el comportamiento que cambia el punto (t). C2 actualiza esos dos casos y el
     resumen (`p3b2/salida/resumen_cadena_sintetica_p3b2.json`): los dos archivos se suman a sus escrituras,
     solo para eso.
  4. (i) y (j) cambian el §1.3 firmado de L-ESQ-R2 (la negación de un verbo alcanza más de tres palabras;
     el comparador pegado a la cuantía gana sobre el coeficiente). Van por la enmienda 5, en BORRADOR —
     PENDIENTE DE FIRMA: `data/experiment/esq/enmienda5_L-ESQ-R2_negacion_y_comparador_pegado_2026-10-04.md`.
     La autora la firma cuando C2 aplique las correcciones.
  5. (l) queda en la lista de páginas de ric (pp. 15, 30, 54 y 59). La medición de la regla general sobre
     los 152 TOs se registró en S0 del borrador de U-SEG-OFICIAL, punto 5.
  6. (m): cambian nueve expectativas de `selftest_pyd_r2.py`, no cuatro. Es consecuencia de la enmienda 3 y
     quedó como nota al pie de esa enmienda.
  7. Con el código de C2, la cadena r2a deja de dar los sha256 sellados, por los cambios que el freno
     declara (umbrales de 46 y 42 nodos y las `remite_a` del punto a). El control de reproducibilidad del
     borrador de U-REEXT-T0 se reescribió: los tres ensamblados r1, byte a byte; los dos r2a, contra los
     sha256 que deje el cierre de C2.
  El despacho de las correcciones a la instancia de C2 y el commit de C2 son de la autora: PENDIENTES.
- **04/10/2026 — decisiones de la autora sobre la revisión del FRENO C2; correcciones despachadas.** La nota
  anterior quedó en `75003eb`. La autora informó que le mandó a la instancia de C2 el mensaje de correcciones
  tal como estaba.
  1. «Más del» y «menos del» como «más de» y «menos de»: aceptado. Deja de estar pendiente de confirmación.
  2. Que la cadena r2a deje de dar los sha256 sellados con el código de C2: aceptado. Los dos grafos sellados
     siguen en el repo y se reproducen con el código de `f8dedd4`, el commit que los selló; la tesis cita sus
     cifras con ese commit. Lo reproduje el 04/10/2026 sobre una copia de ese commit armada con `git
     archive`, sin enlaces: `99fe2bfa…` y `93a7af72…`, byte a byte. La copia necesitó dos entradas que el
     repo no versiona: los diez PDF, con el sha256 del manifiesto `tanda0_ens_diez.json`, y
     `data/experiment/reextraccion_v2/e3_verificador/cache/e1_reintentos.db` (sha256 `e71380308cbe…`).
  3. La línea del mensaje sobre el punto (f), la lista de renumeraciones sin el padre sintético: aceptada.
  El commit de C2 sigue PENDIENTE: espera el freno corregido.
- **04/10/2026 — FRENO C2 corregido, verificado; enmienda 5 a L-ESQ-R2 FIRMADA por la autora.** La nota
  anterior quedó en `bb472b1`. El freno actualizado (`data/experiment/r2_codigo2/freno_c2.md`, sin commit)
  aplica las correcciones pedidas. Lo reproduje sobre una copia nueva:
  - `c2_cadena.json`, `c2_sinteticos.json`, `c2_e0.json`, `c2_control_repro.json` y los resúmenes de las dos
    cadenas sintéticas, byte a byte;
  - cadena de P3, 27 de 27; cadena de P3b-2, 20 de 20, con doble corrida;
  - `selftest_pyd_r2`, 385 de 385 (G15, 42 casos), y `selftest_r3`, 109 de 109; los demás selftests, como
    en el freno.
  Con el código final, la cadena r2a da `70d51e42…` (diez) y `fa4c1043…` (desarrollo): frente a los sellados
  cambian los umbrales de 50 y de 46 nodos y las `remite_a` del punto (a).
  Cifras por regla de la enmienda 5, verificadas contra el detalle de C2 y contra una simulación propia que
  da los mismos nodos: negación e «igual o superior», 13 y 11; comparador pegado, 26 y 26; «o no», 1 y 1;
  «más del» y «menos del», 4 y 4. Las filas suman 44 y 42 y los elementos distintos son 42 y 40.
  Las tres fallas previas de los selftests son las mismas con el código de HEAD y con el de C2 (salida
  idéntica, salvo la ruta de la copia): `selftest_canal_abierto_e1`, 45 bien y 1 falla; `selftest_gate6`,
  que en una copia aborta porque busca el `.venv` de la copia; y `selftest_muestra_aristas_obs12`, con una
  aserción sobre los archivos de su salida.
  La enmienda 5 quedó FIRMADA por la autora el 04/10/2026
  (`data/experiment/esq/enmienda5_L-ESQ-R2_negacion_y_comparador_pegado_2026-10-04.md`; commit de la firma
  PENDIENTE), con las cifras finales y las dos precisiones de C2 sobre su §1.
  Escrituras de C2 para su commit: 13 archivos modificados, 10 nuevos en `data/experiment/r2_codigo2/` y la
  carpeta `e0_chunking/salida_tanda0_r2b/`, con 57 archivos. El commit de C2 es de la autora: PENDIENTE.
