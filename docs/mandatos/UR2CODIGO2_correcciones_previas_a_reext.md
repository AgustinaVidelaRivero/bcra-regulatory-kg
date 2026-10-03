BORRADOR — PENDIENTE DE FIRMA de la autora (redactado el 03/10/2026)

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
  se resolvió como interna del TO de origen) y 2 son de E0 (dos puntos de ric que el PDF trae y E0 no
  segmentó);
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

TAREA

C1 — Diagnóstico, censos y diseño. USD 0. No edita el código de la cadena: sus scripts y reportes van
en data/experiment/r2_codigo2/ (se crea).
a. Detector de citas externas. Para cada una de las 18 filas «detector» de M3.b, decí qué regla y qué
   línea de r1_referencias.py la clasifica como interna (`:185`, `:194`). Son de dos clases:
   - la cita nombra la otra norma en su tramo (13): NIIF 9 (B01, B03, B04, resueltas como `cap::5.5`),
     «Grandes exposiciones al riesgo de crédito» (B10, B11, B12, B16), la «Reglamentación de la cuenta
     corriente bancaria», que es otro TO (B07, B08), y el Anexo de la Comunicación A 7914 (B13, B14,
     B15, B17);
   - la norma surge del contexto y la cita no la nombra (5): B19, B21, B22, B29 y B30.
   Proponé la regla para cada clase. Requisito: «el punto X de <otra norma>» y los puntos de otro TO no
   pueden generar una `remite_a` interna. Para la segunda clase, decí qué contexto habría que mirar y
   qué riesgo tiene; la autora decide en el FRENO C1 si entra.
   Censo: sobre los dos grafos r2a, cuántas aristas `remite_a` internas cambian con la regla propuesta
   (dejan de ser internas, cambian de destino o desaparecen), por causa, con la lista.
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
f. Segmentación de ric 4.4.3 y 4.4.4. Diagnosticá por qué E0 no las segmentó: «4.4.3. Riesgo de
   cambio» y «4.4.4. Riesgo de posiciones en opciones» son encabezados del PDF (p. 18) y quedaron
   dentro del texto de `ric::4.3.3` (páginas 15 a 18), en la E0 legada y en e0-r2. Decí qué pasa con
   4.4, 4.4.1 y 4.4.2, que cinco citas nombran y cuyos encabezados no aparecen en el texto extraído.
   Proponé la corrección en e0-r2 y decí si va dentro de e0-r2 o pide otra versión de E0, y qué
   implica para la clave de caché. Censo: qué ids cambian en los diez TOs de la tanda 0 y en los 152
   TOs de la partición con la corrección.
FRENO C1: el reporte, la tabla de las seis correcciones (qué archivo cambia, qué cambia en los grafos
r2a, qué decide la autora) y los censos. La autora decide qué entra a C2.

C2 — Implementación y controles. USD 0.
Implementá lo aprobado en el FRENO C1, con sus selftests. Control de cada punto:
a. ninguna de las 18 filas (o de las que la autora apruebe) queda como cita interna del TO de origen;
   el caso NIIF 9 no resuelve a `cap::5.5`; el censo de las `remite_a` internas que cambian, por causa;
b. con el cliente simulado, las 4 unidades de diez y las 3 de desarrollo disparan el reintento y, con
   una respuesta bien formada, dejan de quedar sin validación; agotado el tope, quedan en una lista
   declarada; con los perfiles existentes no hay reintento y los requests son byte a byte iguales;
c. «24 hs. hábiles» y «hasta el quinto día hábil posterior al vencimiento…» se detectan como cuantías;
   el selftest de las reglas pasa con los casos nuevos; el censo de los elementos que cambian;
d. el contador nuevo en los dos grafos (hoy 3.801 y 2.993, con 2.540 y 1.859 autocitas de encabezado),
   sin que cambie ninguna arista `remite_a` por este punto;
e. el perfil r2 ya no corre la pasada residual, y el grafo no cambia por este punto;
f. `ric::4.4.3` y `ric::4.4.4` aparecen como unidades con su texto, y en el resto de la tanda 0 y de
   los 152 TOs no cambia ningún id salvo los declarados.
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
