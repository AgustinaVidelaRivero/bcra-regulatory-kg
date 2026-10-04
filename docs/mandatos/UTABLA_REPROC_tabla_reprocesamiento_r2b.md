FIRMADO por la autora el 04/10/2026

MANDATO — U-TABLA-REPROC: LA TABLA DE QUÉ OBLIGA A REPROCESAR, ACTUALIZADA AL PERFIL r2b.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Una etapa, con FRENO al final. Si aparece una contradicción en la que el texto firmado es el que está mal,
  FRENO intermedio antes de seguir. Reporte corto (no más de 40 líneas) y espera del «seguí» de la autora.
- Costo de API: USD 0. Sin API y sin red. Las dbs de caché se abren en solo lectura (`mode=ro&immutable=1`).
- PRECONDICIÓN: el cierre de C2 de U-R2-CODIGO-2 commiteado por la autora; P3b-2 de U-PROMPT-R2 va antes que
  C2. Si no están commiteados, frená sin escribir.
- PLAZO: antes de la tanda 1.

CONTEXTO, con sus anclas.
- La tabla es data/experiment/mantenimiento/tabla_reprocesamiento.md, de M1 de U-MANT (`e18d616`): 21 filas,
  de F01 a F19 con F11b, F18a y F18b. No cambió desde ese commit
  (`git log -- data/experiment/mantenimiento/tabla_reprocesamiento.md`).
- Su selftest es data/experiment/mantenimiento/code/selftest_clave_cache.py, sin API. En `e18d616` dio el
  anclaje de E1 en 2.434 de 2.434 y el de E3 en 2.430 de 2.430, y el contraste en 21 de 21.
- La tesis la va a citar como la única fuente de qué exige cada cambio (sección 4.6).
- Lo que la tabla no recoge (verificación de la sección 4.6 de la tesis, 04/10/2026):
  a. el perfil r2b: el prefijo y el tool schema nuevos, el mensaje de E1 y la NOTA de E3;
  b. el candado del prefijo de E3 (`924ef4d`);
  c. el reintento y la partición por corte de r2 (e1_extractor/cliente_e1.py:68; `26d274d`);
  d. los dos validadores, con exigencias distintas: el de E1, antes de E3, y el de r2, al ensamblar;
  e. el código nuevo del ensamblado: umbrales, `remite_a`, sujetos por relación y unión r2;
  f. las tablas forzadas a residual (nota del 03/10/2026 al protocolo entre tandas, §6).
- Tres contradicciones con el protocolo entre tandas (docs/protocolo_entre_tandas.md, `a304b89`) y con su
  enmienda 2:
  1. F05. El protocolo la pone entre las filas que pagan E1 y E3 de las afectadas (`:82`); la tabla la
     clasifica como solo código sobre lo guardado (tabla_reprocesamiento.md:88).
  2. F10. El protocolo dice que en la clase «todo» todas las unidades pagan E1 y E3 (`:84-85`); la tabla
     dice que con un cambio del prompt de E3 paga solo E3 y que E1 sale de la caché (`:93`).
  3. Catálogo. La enmienda 2 (`0b98045:13-16`) clasifica el crecimiento del catálogo con la fila F13. Con
     el catálogo único de r2, un id nuevo llega también al bloque del prompt y al enum del tool schema, que
     es la fila F11 (`:94`). La separación la diseña U-RERESOL-CAT
     (docs/mandatos/URERESOL_CAT_reresolucion_catalogo.md).

TAREAS.
1. Actualizar la tabla para el perfil r2b. Se revisa cada una de las 21 filas y se suman las que falten.
   Como mínimo, las de los cambios de P3b y de C2:
   - reintento por salida de E1 mal formada, con su namespace propio;
   - recorte de la herencia en e0-r2;
   - metadato de los pies (`pies_<to>.json`);
   - unión de las operaciones por punto;
   - catálogo de resolución separado del catálogo del request. Si R1 de U-RERESOL-CAT no cerró, la fila
     queda declarada como pendiente, con su ancla.
   Cada fila dice qué cambia, por dónde entra, qué se rehace, si cambia la clave de E1 y la de E3, su clase
   y su ancla path:línea.
2. Verificar cada fila contra la composición real de las claves de caché, como en M1 de U-MANT:
   - el selftest se extiende al perfil r2b;
   - el anclaje se hace sobre las dbs de U-REEXT-T0, si para entonces existen; si no, sobre las de la tanda
     0 con el perfil sellado, y se declara;
   - cada fila tiene su contraste: una variación mínima mueve la clave, o no la mueve, como dice la fila.
3. Resolver las tres contradicciones. El protocolo y sus enmiendas mandan, por estar firmados: la tabla se
   alinea con ellos. Si la composición real de la clave muestra que el que está mal es el texto firmado, no
   se toca: se reporta con su evidencia en el FRENO intermedio y la autora decide la enmienda.
4. Actualizar el costo de referencia por clase (§5 de la tabla) con la tarifa del prefijo nuevo.
FRENO final: la tabla nueva lado a lado con la de `e18d616` (filas nuevas, cambiadas e iguales), el selftest,
las tres contradicciones con su resolución o su reporte, y lo que queda pendiente.

ESCRITURAS: data/experiment/mantenimiento/tabla_reprocesamiento.md,
data/experiment/mantenimiento/code/selftest_clave_cache.py con su salida, un freno en
data/experiment/mantenimiento/, y el scratchpad.
PROHIBIDO: editar el protocolo, sus enmiendas o cualquier texto firmado; editar la cadena (E0 a E5); escribir
en las cachés; commitear.

DECISIONES DE LA AUTORA AL FIRMAR (04/10/2026).
1. La unidad se llama U-TABLA-REPROC.
2. No espera al cierre de R1 de U-RERESOL-CAT: la fila del catálogo queda declarada como pendiente, con su
   ancla.
3. El anclaje del selftest no espera a las dbs de U-REEXT-T0: corre sobre las de la tanda 0 con el perfil
   sellado, declarado, y se corre de nuevo cuando existan las de U-REEXT-T0.

REQUISITOS: los de CLAUDE.md §4 (a a l), con PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; fuentes firmadas
leídas en el commit de su firma; todo conteo recomputado contra su artefacto; cero nombres de personas.

FIRMA. FIRMADO por la autora el 04/10/2026, con las tres decisiones de arriba. Se despacha sobre el commit de
C2 de U-R2-CODIGO-2, junto con U-RERESOL-CAT.

NOTAS POSTERIORES A LA FIRMA. El texto firmado son las 77 líneas de arriba (sha256 `85df5030…`) y no cambia.

- 04/10/2026 — FRENO FINAL REVISADO; ENMIENDA 3 AL PROTOCOLO Y FE DE ERRATAS DE LA ENMIENDA 2, FIRMADAS POR LA
  AUTORA. El freno (data/experiment/mantenimiento/freno_utabla_reproc.md, sin commit) se reproduce sobre una
  copia: el selftest, corrido dos veces, da el mismo JSON que el del repo (sha256 `f5cf44bb…`), con el
  contraste en las 38 filas. La tabla pasa de 21 a 38 filas: 15 iguales, 6 cambiadas y 17 nuevas.
  Los cuatro hallazgos sobre textos firmados se sostienen. Los repetí con un programa propio sobre las 2.439
  unidades de `salida_tanda0_r2b/`: páginas y metadatos no mueven ninguna clave (F05); el texto de sistema y
  el modelo de E3 mueven las 2.439 claves de E3 y ninguna de E1 (F10); un id más en el catálogo frena y,
  puesto en el bloque o en el enum, mueve las 2.439 claves de E1 (F11, no F13); y la salida validada entra al
  mensaje de E3 (F14), en 59 de 59 salidas reales de la pareada de P4.
  Quedan firmadas, con commit PENDIENTE: la enmienda 3 al protocolo entre tandas
  (docs/enmienda3_protocolo_entre_tandas_2026-10-04_clases_de_reprocesamiento.md) y la fe de erratas al pie de
  la enmienda 2 (docs/enmienda2_protocolo_entre_tandas_2026-10-04_catalogo.md).
  Lo que sigue queda en T5 del borrador de U-REEXT-T0: el anclaje del perfil r2b sobre sus dbs, el §5 con la
  tarifa observada y la cita de la enmienda 3 en las filas F05, F10 y F14 de la tabla, que hoy dicen «enmienda
  en curso». La fila F13 se completa al cerrar R1 de U-RERESOL-CAT.
  Dos hallazgos del freno quedan a decisión de la autora, con la propuesta de la revisión: dónde se les pone
  candado a los tres insumos que no entran al hash del prefijo (F04b, F22 y F22b, F23), y el namespace de E3,
  que el perfil r2b comparte con la tanda 0.
