FIRMADO por la autora el 04/10/2026

MANDATO — U-RERESOL-CAT: SCRIPT QUE RE-RESUELVE LOS SUJETOS EN CUARENTENA Y REHACE EL GRAFO CUANDO CRECE EL CATÁLOGO.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad en DOS ETAPAS con FRENO obligatorio al final de cada una: R1 (diagnóstico y diseño, sin implementar)
  y R2 (implementación y prueba). Reporte corto (no más de 40 líneas) y espera del «seguí» escrito de la
  autora.
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa.
- PRECONDICIÓN: el cierre de C2 de U-R2-CODIGO-2 commiteado por la autora. C2 edita el ensamblado
  (docs/mandatos/UR2CODIGO2_correcciones_previas_a_reext.md) y esta unidad trabaja sobre ese commit. Si no
  está commiteado, frená sin escribir.
- R1 solo lee: puede correr en paralelo con P4 de U-PROMPT-R2 y con U-REEXT-T0. R2 espera el crudo guardado
  de U-REEXT-T0, porque su prueba corre sobre él.
- PLAZO: la unidad tiene que estar cerrada antes del primer crecimiento del catálogo de sujetos durante el
  escalado (docs/enmienda2_protocolo_entre_tandas_2026-10-04_catalogo.md).

CONTEXTO, con sus anclas.
- L-ESQ-R2 §4.2, P-d3 (`git show 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`, `:649`):
  «re-resolución por programa cuando cambia el sha256 del catálogo, y re-ensamblado de E2 a E5 a USD 0». P-d4
  (`:650-654`) pide los resueltos por versión del catálogo.
- La función existe y ningún script la aplica: `r1_e4.reresolver_registro`
  (data/experiment/reextraccion_v2/corpus_v2/r1_e4.py:469-489) solo se usa en la suite (LN-6,
  scripts/regression_kg.py:1766) y en data/experiment/r2_codigo/selftest_r3.py:236-245.
  data/experiment/catalogo_unico/code/reresolver_tanda0.py (`bd2122d`) calcula la re-resolución de los
  propuestos de r1 y no escribe nada.
- El ensamblado r2 resuelve los sujetos desde el crudo guardado con `r1_e4.resolver_relaciones_r2`
  (data/experiment/tanda0/code/ensamblar_tanda0.py:824) y toma el catálogo de `r1_e4.catalogo_r2()` (`:813`;
  r1_e4.py:522-541), sin parámetro: lee data/experiment/catalogo_unico/generados_r2/.
- El catálogo r2 es un solo archivo con candado. `modelos_r2.py:61-96` fija el sha256 de
  data/experiment/catalogo_unico/catalogo_sujetos_r2.json (`c3ad1581…`, `bd2122d`) y frena si no coincide. De
  ese archivo se genera todo (catalogo_unico/code/generar_desde_catalogo.py): lo que lee el código
  (`indice_e4_r2.json`, `labels_e2_r2.json`, `rol_por_to_r2.json`, `entrada_esqueleto_r2.json`,
  `ids_s19_r2.json` y `catalogo_suite_r2.json`) y lo que entra al request de E1 (`bloque_catalogo_r2.txt`,
  con su candado en e1_extractor/prompt_r2b.py:57, y `enums_tool_schema_r2.json`, el enum de `sujeto_id`).
- Consecuencia: hoy un id agregado al catálogo rompe el candado de `modelos_r2.py` y cambia el enum del tool
  schema, es decir, el request de E1. L-ESQ-R2 §7 ya lo declara como límite (`:862-864`): un id agregado solo
  al JSON se aplica en código a las menciones guardadas, y el modelo lo sugiere recién cuando se regenera el
  bloque del prompt. La tabla de reprocesamiento separa los dos casos: F11, el catálogo en el bloque del
  prompt, reprocesa todo; F13, el catálogo que solo lee el código, rehace E4 y el ensamblado
  (data/experiment/mantenimiento/tabla_reprocesamiento.md:94-97).
- Registro de la tanda 0 (`no_mapeados_sujetos.jsonl` de cada ensamblado r2a, campo `estado`): en
  KG-Tanda0-Diez-r2a, 48 filas, 40 en cuarentena y 8 resueltas a clase; de las 40, 27 tienen la mención
  verificada (25 exacta y 2 tokens) y 13 no. En KG-Tanda0-Desarrollo-r2a, 33 filas, 26 en cuarentena y 7
  resueltas a clase; de las 26, 17 verificadas y 9 no. `reresolver_registro` solo re-resuelve las verificadas.

R1. DIAGNÓSTICO Y DISEÑO (sin implementar).
1. Inventario: qué archivo lee el catálogo en cada paso (request de E1, validador, E2, E4, esqueleto, shapes
   y suite), con path:línea, y qué candado lo protege.
2. Cómo crece el catálogo sin cambiar el request de E1. El diseño separa dos catálogos: el que entra al
   request de E1, fijo por release, y el catálogo de resolución, que lee el código y puede crecer entre
   tandas. El resultado tiene que permitir que la tesis afirme que la re-resolución corre sin re-extraer
   sobre el catálogo de resolución. Dice qué candados cambian, qué lee `SUJETOS_R2_SET` en cada uso (`modelos_r2.py:95-96`, `:537-539`;
   ensamblar_tanda0.py:587 y `:825`) y cómo queda registrada en el grafo la versión del catálogo con la que se
   resolvió cada relación. Si no se puede sin cambiar el request, se dice: el crecimiento sería de la clase
   que reprocesa todo, y la decisión vuelve a la autora.
3. El script, en dos caminos que se verifican entre sí:
   a. sobre el registro guardado, `reresolver_registro` con el catálogo nuevo: qué filas pasan de cuarentena a
      resuelto;
   b. el ensamblado entero desde el crudo guardado, con el catálogo nuevo.
   Verificación: las diferencias entre el grafo anterior y el nuevo son exactamente las que predice (a), y el
   registro que escribe (b) es igual a la salida de (a). Lo que no explique (a) se lista y se lee. Se suman
   LN-6, las shapes de sujetos y la suite del perfil.
4. Qué pasa con cada elemento del grafo cuando una fila resuelve: la arista de sujeto, el nodo en cuarentena
   que queda sin aristas, las marcas de la relación y la fila del registro (`catalogo_sha256_resolucion`).
5. La prueba de R2 corre sobre el crudo guardado de U-REEXT-T0. R1 mide sobre el crudo de r2a, que es el que
   existe hoy, y lo declara.
FRENO R1, con el diseño y la lista de escrituras que pide R2. La autora aprueba las escrituras en el «seguí».

R2. IMPLEMENTACIÓN Y PRUEBA.
1. El script y su selftest, con las escrituras aprobadas en el «seguí» de R1.
2. Prueba obligatoria, sobre el crudo guardado de U-REEXT-T0: un catálogo de resolución de prueba, en el
   scratchpad, con un id agregado que resuelve una mención en cuarentena. Candidatas: «cuentacorrentista» e
   «integrantes de la Alta Gerencia». En el registro de r2a de diez tienen 3 filas cada una, con la mención
   verificada como exacta y el motivo `sin_match`. Si en el registro de U-REEXT-T0 ninguna de las dos está
   en cuarentena con la mención verificada, se elige otra con el mismo criterio y se declara. La más frecuente, «cliente que
   no es persona humana residente» (7 filas), no sirve: su mención no está verificada y `reresolver_registro`
   no la toca. El id de prueba no entra al catálogo del repo. Se reporta: las filas que resuelven, las que no
   y por qué, y las diferencias del grafo.
3. Controles:
   - con el catálogo sin cambios, el script no cambia nada: el grafo y el registro salen byte a byte iguales;
   - doble corrida, en dos directorios, byte a byte idéntica;
   - los ensamblados sellados se reproducen con el catálogo vigente;
   - todo corre sobre una copia sin enlaces, con el sha256 de los archivos del repo antes y después.
4. Procedimiento escrito, de no más de una página: qué se corre cuando crece el catálogo, en qué orden, qué se
   verifica y qué se reporta con la tanda (resueltos por versión del catálogo, P-d4).
FRENO R2, final.

ESCRITURAS. R1: solo data/experiment/reresolucion_catalogo/ (se crea) y el scratchpad. R2: además, las que la
autora apruebe en el «seguí» de R1.
PROHIBIDO: cambiar el catálogo (`catalogo_sujetos_r2.json`) o sus generados; cambiar el prefijo de E1, su tool
schema o sus candados; agregar un id al catálogo del repo; tocar los grafos y las salidas selladas; correr el
ensamblado sobre el repo; commitear.

DECISIONES DE LA AUTORA AL FIRMAR (04/10/2026).
1. La unidad se llama U-RERESOL-CAT y trabaja en data/experiment/reresolucion_catalogo/.
2. R1 puede correr en paralelo con P4 de U-PROMPT-R2 y con U-REEXT-T0.
3. La prueba de R2 corre sobre el crudo de U-REEXT-T0, con «cuentacorrentista» e «integrantes de la Alta
   Gerencia» como candidatas.
4. R1 diseña la separación entre el catálogo que entra al request de E1, fijo por release, y el catálogo de
   resolución que lee el código, que puede crecer entre tandas.

REQUISITOS: los de CLAUDE.md §4 (a a l), con PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; fuentes firmadas
leídas en el commit de su firma; todo conteo recomputado contra su artefacto; cero nombres de personas.

FIRMA. FIRMADO por la autora el 04/10/2026, con las cuatro decisiones de arriba.

NOTAS POSTERIORES A LA FIRMA. El texto firmado son las 105 líneas de arriba y no cambia.

- 04/10/2026 — R1 SE AMPLÍA CON EL ALCANCE DE LOS DOCUMENTOS NUEVOS Y CON LA REGLA DE CRECIMIENTO DEL CATÁLOGO
  (decisión de la autora). La unidad todavía no arrancó: espera el cierre de C2 de U-R2-CODIGO-2.
  Fe de erratas del CONTEXTO (`:31-34`). `rol_por_to_r2.json` figura ahí solo entre «lo que lee el código».
  También entra al request de E1: `e1_extractor/prompt_r2b.py:124` lo carga con candado propio (`:58` y `:66`)
  y con él arma la línea de alcance del mensaje (`linea_alcance`, `:328`, y `:356`). Causa: clasifiqué los
  generados por el módulo que los lee en el ensamblado y no seguí su uso en el mensaje.
  Hechos medidos (04/10/2026; comandos en el paquete de la revisión, fuera del repo):
  - El alcance por documento vive en el archivo del catálogo con candado: es el campo `rol_por_to` de cada
    sujeto de `catalogo_sujetos_r2.json`. De ahí sale `generados_r2/rol_por_to_r2.json`, con 71 entradas: 35
    con rol propio y 36 con una clase.
  - Del universo de 157 documentos, 71 tienen entrada y 86 no: los 84 «necesita reglas» (53 regímenes
    informativos y 31 de normativa general; protocolo firmado, `a304b89:168`) más docvig y fimipyme, los dos
    huecos que el laudo de B5.4 dejó sin rol, con re-mirada en la tanda 1
    (`docs/laudo_B5.4_fase1_catalogo.md:20-22`, `dea56ba`). Entre los 86 están los 12 no segmentables.
  - De los diez TOs de la tanda 0, nueve tienen alcance: seis con rol propio y tres con clase. Docvig no
    tiene. El ejemplo de la tanda 1 del protocolo tiene 12 documentos sin alcance, 6 de ellos regímenes
    informativos.
  - Sin entrada, el mensaje de E1 no lleva línea de alcance (`prompt_r2b.py:329-330`). En el ensamblado, una
    expresión colectiva queda sin sujeto por defecto (`corpus_v2/r1_e4.py:377`): gana la sugerencia del modelo
    si la hay (`:419`) y, si no, la fila va a cuarentena (`:443`).
  - Qué cambia cuando el alcance crece, simulado en memoria con `generar_desde_catalogo` (la simulación
    reproduce el bloque con candado, `c40054853bd8…`):
    - entrada de clase (un documento nuevo apunta a una clase que ya existe): el bloque del prefijo y el enum
      del tool schema no cambian. Cambian el sha256 del catálogo, el de `rol_por_to_r2.json` y el mensaje de
      las unidades de ese documento, y de ningún otro;
    - rol nuevo (un id de nivel rol): entra al bloque del prefijo («## Roles de alcance por TO») y al enum de
      `sujeto_id`. Cambia el request de todos los documentos.
  - El peso del alcance en la tanda 0: en KG-Tanda0-Diez-r2a, 4.086 de las 4.147 relaciones con sujeto se
    resolvieron por la sugerencia del modelo, y los ids más sugeridos son los roles de alcance (1.074 el de
    ext y 920 el de cap). La regla del sujeto por defecto resolvió 0 filas: el crudo de r2a trae mención en
    62 de las 4.147. Con el prefijo r2b la mención se emite siempre; cuánto resuelve entonces la regla se
    mide en U-REEXT-T0.
  R1 suma a su diseño:
  a. Cómo se le da rol de alcance y entrada de clase a un documento nuevo sin cambiar el request de los ya
     extraídos. El laudo de B5.4 fija el método (A2, `laudo_B5.4_fase1_catalogo.md:15-20`): clase existente
     cuando el pasaje de alcance nombra exactamente una o dos clases del catálogo, y rol nuevo en los demás
     casos. R1 dice:
     - qué candados cambian con una entrada de clase, y cómo queda registrado en el grafo con qué versión del
       alcance se extrajo y se resolvió cada documento;
     - qué pasa con un documento cuyo alcance no es una clase exacta. Hoy un rol nuevo cambia el prefijo y el
       tool schema. Opciones a evaluar: el rol vive solo en el catálogo de resolución y el mensaje nombra sus
       clases miembro; o el documento espera la release que rote el prefijo. Si ninguna sirve, se dice;
     - a qué lado de la separación del punto 2 de R1 queda `rol_por_to_r2.json`, que hoy está en los dos;
     - qué pasa con docvig, ya extraído sin alcance: si se le asigna después, sus 31 unidades se re-extraen.
  b. La regla de crecimiento del catálogo. Las entradas nuevas salen de dos fuentes:
     - el alcance de los documentos nuevos, antes de su extracción;
     - la cuarentena, al cierre de cada tanda, con un umbral de frecuencia a fijar y con aprobación de la
       autora.
     Entran solo al catálogo de resolución, y después corre el script de re-resolución. R1 propone el umbral
     con el registro de r2a a la vista, y dice cómo convive la regla con el límite que L-ESQ-R2 §7 declara
     (`4ef7650:862-864`): un id que no está en el bloque del prompt se aplica en código a las menciones
     guardadas, y el modelo no lo sugiere.
  Cuando R1 fije el mecanismo, las dos reglas van a una enmienda firmada del protocolo entre tandas, con el
  paso de lectura del alcance antes de la primera extracción de cada tanda. Hasta entonces no rigen.
  Las ESCRITURAS y lo PROHIBIDO del mandato no cambian: R1 diseña y no toca el catálogo.
- 04/10/2026 — TRES DECISIONES DE LA AUTORA SOBRE EL ALCANCE (segunda nota; la anterior quedó en `bb472b1`).
  1. El paso de lectura del alcance entre tandas asigna solo clases que ya existen: el método del laudo de
     B5.4 (`docs/laudo_B5.4_fase1_catalogo.md:15-20`) cuando el pasaje de alcance nombra exactamente una o dos
     clases del catálogo. Un documento que necesite un rol nuevo, incluidos los regímenes informativos que lo
     necesiten, entra sin línea de alcance, declarado, y sus menciones colectivas van a cuarentena hasta que
     su rol se decida en la release que corresponda. El laudo B5.5 no se enmienda: ESQ-RI-3 sigue abierta y
     atada a la release (plan `:695`). Con eso el paso no cambia el prompt entre tandas: una entrada de clase
     cambia solo el mensaje del documento nuevo.
     En el punto (a) de la nota anterior quedan fuera de R1 las dos opciones para un documento cuyo alcance
     no es una clase exacta: ese documento espera la release.
  2. R1 diseña además este cambio de código: cuando un documento no tiene alcance, la sugerencia del modelo
     para una expresión colectiva («las entidades») no gana, y la mención va a cuarentena. Hoy gana
     (`corpus_v2/r1_e4.py:419`), y sin sugerencia la fila ya va a cuarentena (`:377`, `:443`).
     R1 dice qué expresiones cuentan como colectivas (la lista de R3, `r1_e4.py:306`, o una ampliada), cómo
     queda el registro (motivo y sugerencia del modelo guardada) y cuántas filas habría cambiado en docvig,
     el único documento de la tanda 0 sin alcance.
     El cambio toca una regla firmada: L-ESQ-R2 §3.2 y §3.3 dicen que con R3 gana la sugerencia del modelo y
     que R4 es esa sugerencia (`git show 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`,
     `:565-582`). Si R1 confirma el diseño, va por enmienda firmada a L-ESQ-R2 antes de implementarse.
  3. Si la lectura asistida del alcance usa la API, la enmienda del protocolo que cree el paso le fija un
     tope. Es condición de esa enmienda.
  Cifras para el pre-registro de la tanda 1: 86 documentos sin alcance, de 157, y 31 de normativa general
  entre los 84 «necesita reglas».
- 04/10/2026 — FRENO R1 REVISADO; DECISIONES DE LA AUTORA PARA R2 (tercera nota; R1 quedó en `c98093a`). La
  medición de R1 se reproduce: `r1_medicion.py`, corrido dos veces sobre una copia, da el mismo
  `salidas/r1_medicion.json` (sha256 `6cdf86ee…`). Decisiones:
  a. W1 va como parámetro opcional del ensamblado, no como sustitución en memoria. El parámetro lleva también
     el conjunto de ids de resolución: reemplaza a `M.SUJETOS_R2_SET` en el merge entre TOs y en E2
     (`data/experiment/tanda0/code/ensamblar_tanda0.py:587` y `:956`), además del catálogo (`:935` y `:1155`)
     y de la entrada del esqueleto (`:585-586`). Sin el conjunto, E2 rechaza la relación al id nuevo
     (`e2_reduce/e2_lib.py:1053`) y no queda fila en el registro. R2 suma un control: cero relaciones
     rechazadas sin registro.
  b. La prueba usa T1, «cuentacorrentista» como id nuevo de prueba, y T2, «integrantes de la Alta Gerencia»
     como alias agregado a `Sujeto_alta_gerencia`. Ninguno entra al catálogo del repo.
  c. docvig queda sin alcance en U-REEXT-T0. Su lectura con el método del laudo de B5.4 no encuentra pasaje
     de alcance: el índice tiene cuatro secciones y ninguna lo es, y el texto nombra tres clases en lugares
     distintos. El catálogo del request no cambia y el laudo de B5.4 no necesita nota. Un alcance solo de
     resolución, inferido del título de su punto 3.6 («entidades financieras y cambiarias»), se decide con la
     medición de R2.
  d. Umbral de crecimiento: al menos 2 unidades distintas con la mención verificada en cuarentena, en el
     registro acumulado; después, lectura y aprobación de la autora. R2 lo recalibra con el registro de
     U-REEXT-T0.
  e. El control de reproducción de R2 es contra la cadena r2a del código del commit de la corrida (con
     `9f6361e`, `70d51e42…` y `fa4c1043…`), no contra los sellados, que se citan con `f8dedd4`.
  f. Los tres huecos del freno entran a R2: el registro acumulativo; un solo nombre de método para
     `reresolver_registro` y para la cadena; y el camino que vuelve a aplicar la decisión a las relaciones
     que resolvió el modelo, con la lista de las que cambian de destino y una muestra leída.
  g. La lista de expresiones colectivas deja afuera «la entidad» (806 apariciones por texto, contra 231 que
     cubre). R2 mide qué cambia si se la incluye, antes de decidir.
  h. La regla del colectivo sin alcance cambia L-ESQ-R2 §3.2 y §3.3. Va por la enmienda 6
     (`data/experiment/esq/enmienda6_L-ESQ-R2_colectivo_sin_alcance_2026-10-04.md`, BORRADOR — PENDIENTE DE
     FIRMA), que la autora firma antes de que R2 la implemente.
  i. La enmienda 6 suma un principio: en un documento sin alcance, una relación sin mención tampoco acepta
     la sugerencia del modelo y va a cuarentena, igual que la expresión colectiva. R2 mide cuántas relaciones
     irían a cuarentena por cada una de las dos reglas, antes de la firma. El punto e de P3c de U-PROMPT-R2
     (sin relación de sujeto cuando el texto no nombra al sujeto) cambia esos casos: la medición corre sobre
     el crudo de U-REEXT-T0, extraído con ese prefijo.
  j. La versión del catálogo queda registrada como propone el freno, sin tocar `modelos_r2` (G1).
  Las dos reglas de la primera nota (el crecimiento del catálogo y el paso de lectura del alcance) están en
  `docs/enmienda4_protocolo_entre_tandas_2026-10-04_crecimiento_del_catalogo_y_alcance.md`, BORRADOR —
  PENDIENTE DE FIRMA: se firma cuando R2 deje el script funcionando. Hasta entonces no rigen.
  El «seguí» de R2 está preparado, con R2 en dos pasos (R2-1, hasta la medición; R2-2, las dos reglas, con la
  enmienda 6 firmada). Su despacho está PENDIENTE: va después de U-REEXT-T0.
- **05/10/2026 — la mención que el texto no trae entra a la enmienda 6 (decisión de la autora).** Sale de P5
  de U-PROMPT-R2 (`data/experiment/prompt_r2/freno_p5.md`, sin commit al 05/10/2026): con el prefijo de P3c y
  temperatura 0, verifican 32 de 35 y 32 de 40 menciones de sujeto; las 11 que no verifican dicen «las
  entidades».
  - Una mención que no verifica se trata como una relación sin mención: en un documento sin alcance, la
    parte A la manda a cuarentena; en uno con alcance, la parte B la resuelve al rol del documento, si rige.
    Está en el borrador de la enmienda 6, en su versión del 05/10/2026.
  - R2 lo mide antes de la firma, con lo demás: en la tabla de A.2, la regla 2 en sus dos casos; de las
    menciones que no verifican, cuántas son una expresión colectiva y cuántas nombran otra cosa; y en la
    población de la parte B entran las normas cuya relación trae una mención que no verifica.
  - Queda abierto, y R2-1 lo propone: qué se hace con una relación sin mención, o con una mención que no
    verifica, de una norma que ya tiene otra relación con mención verificada.
  El «seguí» de R2 está actualizado con esto. Su despacho sigue PENDIENTE: va después de U-REEXT-T0.
- **06/10/2026 — decisiones de la autora sobre W2 y W3 de R2 (opciones de la mesa en el paquete `hoja_de_ruta_tanda1_mesa/`,
  `punto6_W2_W3_opciones_mesa.md`).** W2, dos cosas: (a) un solo nombre de método: `reresolver_registro` escribe el mismo
  nombre que la cadena del ensamblado (`R1_` más los criterios; hoy escribe `R1`, `corpus_v2/r1_e4.py:484-486`), con un
  selftest del caso; (b) el cargador del catálogo de resolución va como función nueva en `r1_e4.py`, junto a `catalogo_r2()`
  y con su propio candado, porque W1 (parámetro opcional del ensamblador, nota del 04/10/2026, punto a) necesita un
  cargador importable; una sola implementación del candado. W3: `scripts/regression_kg.py` recibe una opción para que LN-6
  lea los generados de resolución; sin ella, rutas fijas y salida byte a byte igual, para que el gate de cada tanda
  verifique la idempotencia contra el catálogo que de verdad usó el ensamblado. Las tres escrituras van después de
  U-SINCOLA-T0, que exige el código del sello intacto. R2 se despacha en dos pasos: R2-1 (script, prueba, medición de la
  enmienda 6 §A.2 y lectura de la parte B), firma de la enmienda 6, R2-2 (las dos reglas), firma de la enmienda 4.
- **06/10/2026 — revisión del FRENO R2-1 y decisiones de la autora (R2-1 sin commit al escribir esta nota; la nota anterior quedó en
  0a3ac81).**
  - La revisión independiente reprodujo R2-1 sobre una copia sin enlaces: los parches de W1 a W3 aplican limpio sobre HEAD (`235a295`);
    `selftest_reresolver_catalogo` 51/51, `selftest_r3` 116/116, `selftest_regression_kg` 184/184; la suite sobre las seis entradas
    selladas con el código de HEAD y con el nuevo, byte a byte; las seis cadenas con sus sha (r2a `70d51e42…` y `fa4c1043…`, r2b
    `a9631a64…` y `6e756043…`, sin cola `e22fae1a…` y `2922b72d…`). La parte B de la enmienda 6, releída a ciegas por la mesa sobre las 30
    fichas: 18 correctas, 5 incorrectas, 7 dudosas, lo mismo que la instancia, con dos divergencias (F18 `ext::3.17.3.3`, F27
    `ctacte::8.5.4`).
  - Decisiones. (1) La enmienda 6 se firma en su parte A; la parte B no se adopta (18 de 30; Wilson al 95 %, 0,42 a 0,76) y su cifra se
    declara como límite (`data/experiment/esq/enmienda6_L-ESQ-R2_colectivo_sin_alcance_2026-10-04.md`, firmada el 06/10/2026). (2)
    Adjudicación de las divergencias: F18 dudosa, F27 correcta; el conteo no cambia. (3) El rediseño de la parte B, derivar el rol solo
    cuando la norma no nombra otro sujeto, va al backlog (`data/backlog/backlog.jsonl`, BKL-0040) con una pre-medición en R2-2: cuántas de
    las 1.362 normas sin `aplica_a` contienen en su texto un label o alias de otro Sujeto del catálogo. (4) El caso abierto de las 5
    normas con una relación verificada y otra sin mención o que no verifica: sin derivada; la segunda relación sigue por R4 con su marca
    de mención. (5) Los tres puntos de R2-2: cuando un documento sin alcance recibe alcance, el script resuelve con la misma regla que la
    cadena (R4 si la mención verifica, si no R3; precisión a A.1.5, asentada en la firma); el estado de las filas resueltas por
    calificador se alinea al de la cadena (`resuelto_a_clase`), una línea en `reresolver_registro` con su caso de selftest; la fila sin
    mención en cuarentena queda como condición con disparador (si una tanda la produce, va sin nodo ni arista, con LN-5 y S28 contándola
    aparte) y se implementa entonces, fuera de esta unidad. (6) Las 51 menciones que no verifican por el artículo («del», «al»): defecto
    de normalización de `verificar_tramo` (`data/experiment/pyd_r2/code/validador_r2.py:209-230`, tokens sin contracciones); corrección por
    código, fila F14b, fuera de esta unidad: entra como ítem de U-OMISIONES-COD (las correcciones en código que salieron de T4), con
    pre-medición sobre el crudo r2b y vigencia desde la release siguiente.
  - W1 a W3 se aplican al repo en R2-1 bis («seguí» despachado el 06/10/2026, con SC2 de U-SINCOLA-T0 commiteada en `dde9f44`); el
    commit de R2-1 y R2-1 bis es de la autora. R2-2 se despacha después de ese commit.
- **07/10/2026 — revisión del FRENO R2-2 y decisiones de la autora (R2-2 sin commit al escribir esta nota; R2-1 y R2-1 bis en `0737497`).**
  - **Se reproduce, sobre una copia sin enlaces** (sin API, sin Neo4j): diffs de los seis archivos iguales a los del paquete (r1_e4 +48/−14,
    ensamblar_tanda0 +1/−1, reresolver_catalogo +196/−23, selftest_r3 +63, selftest_reresolver_catalogo +118, procedimiento +48/−44); r2b
    diez `892f3803…` (8.817/27.632) y sin cola diez `75f8e599…` (8.504/26.129), con diff exacto contra los sellados: +1 nodo
    `Sujeto_propuesto_las_entidades` y las 4 `aplica_a` de `docvig::3.4` (relaciones 5, 6, 7 y 9; 3 Obligacion y 1 Restriccion) que pasan
    de `Sujeto_sujeto_regulado` al propuesto, nada más; registro con 4 filas nuevas (`cuarentena`, `colectivo_sin_sujeto_por_defecto`,
    sugerencia `Sujeto_sujeto_regulado` guardada) y 0 cambiadas; r2a `70d51e42…`/`fa4c1043…` y los dos desarrollo `6e756043…`/`2922b72d…`
    byte a byte con el código nuevo y con el de HEAD; los nueve con alcance, `resolucion_sujetos` 2.605/2.534 y registro 291/286 byte a
    byte; las 15 filas `R2_calificador` con estado `resuelto_a_clase` (128 = 113 R4 + 15 en diez; 125 = 110 + 15 sin cola); S19 PASS→FAIL
    con exactamente 1 propuesto incompleto, S4/S5/S28/S23 cambian de cifra sin cambiar de estado, `sin_rol_de_alcance` 0→1; con el alcance
    de prueba (docvig → `Sujeto_entidad_financiera`) el grafo vuelve a `a9631a64…` y (a) = (b) = (a+); el mensaje de E1 con el registro
    cargado idéntico (sha `48fdec19…`) en las 2.439 unidades de la E0 r2b de los diez TOs y en los 13 casos del candado (`a9cb702c…`);
    selftests `selftest_r3` 124/124, `selftest_reresolver_catalogo` 66/66, `selftest_regression_kg` 184/184, `selftest_prompt_r2b` 55/55,
    `selftest_catalogo_unico` 60/60 (solo con el `.git` del repo a la vista: sobre una copia sin `.git` frena en K1, como ya pasa con el
    manifiesto, regla l). Suite entrada por entrada: r2a diez sin regresiones; las cuatro entradas r2b con las 3 regresiones preexistentes
    (RT-C5-3, RT-C6-1, RT-C6-2, declaradas en `bbc38dc`); los dos grafos nuevos de diez no tienen entrada en la fixture hasta re-sellar: el
    commit de R2-2 no deja la suite más en rojo de lo que ya está; lo que bloquea es S19. Las 12 filas del registro de alcance (9 con
    alcance, 3 sin: ri_oc, ceninf, cirmo3) coinciden con `data/experiment/catalogo_unico/registro_alcance_por_tanda.md`. La pre-medición B′
    cierra (1.362 / 986 / 968 / 946, sobre las normas de las unidades aceptadas de los 9 TOs con alcance del crudo r2b diez; «nombran otro
    Sujeto» = mención en el texto propio o heredado, no entidad). La clasificación de los archivos ajenos cierra. Repo sin cambios durante
    la verificación; 2.213 `.pyc`.
  - **Decisiones de la autora, asentadas.** (1) La parte A solo en r2b: `parte_a=False` por defecto en `resolver_relaciones_r2` y la cadena
    pasa `parte_a=(fase == "r2b")` (`ensamblar_tanda0.py:1237`). (2) Precisión a la decisión 2 del 06/10/2026: cuando un documento sin
    alcance recibe alcance, la fila de la regla 2 con sugerencia guardada se resuelve por R4 como en la cadena, aunque la mención no
    verifique (darle el rol es la parte B, no adoptada); conserva la marca `mencion_no_verificada` y se cuenta aparte (sección `parte_a`
    del reporte del script). (3) `prompt_r2b.py` no se toca en esta unidad: el cableado del registro de alcance al armar el mensaje
    (autorizado por la enmienda 4, §4, solo lectura del registro, sin cambiar el prefijo) queda como CONDICIÓN previa a la extracción de
    la tanda 1, después de la firma de la enmienda 4, en el checklist (11-bis) y en el pre-registro; mueve el candado del mensaje de E1,
    las claves de E1 de los documentos con alcance nuevo y una fila de la tabla de reprocesamiento.
  - **S19 bloqueante: decisión PENDIENTE de la autora.** Análisis de las tres salidas en `hoja_de_ruta_tanda1_mesa/analisis_S19_propuesto_sin_alcance_R2-2_mesa.md`
    (scratchpad de la mesa). Recomendación de la mesa: el propuesto de la parte A recibe como `padre_sugerido` la sugerencia guardada del
    modelo (`sujeto_id_modelo`) con la marca `padre_desde_sugerencia_modelo`, y, sin sugerencia, la raíz del catálogo con la marca
    `padre_por_defecto_generico`; S19 no se toca; nunca la exención. Donde: una etapa R2-3 (USD 0) de esta unidad, con un caso en
    `selftest_r3` y la fila F15d («solo código sobre lo guardado»).
  - **Hallazgo nuevo: `runner_corpus.py:1261` (`cerrar_e2_r2`, la E2 r2 por TO del runner) llama a `resolver_relaciones_r2` sin `parte_a`.**
    Es el flujo de la extracción de la tanda 1 (`runner_corpus.py:1446`); el grafo de la tanda sale del ensamblado, que sí la aplica, pero
    los artefactos por TO del runner (`grafo_r2_<to>.json`, `resolucion_sujetos.jsonl`, `no_mapeados_sujetos.jsonl`) quedarían sin la
    parte A en los documentos sin alcance. Corrección: `parte_a=perfil_forma_r2(PERFIL)` en esa línea, con un caso de selftest; va en R2-3
    (`hallazgo_runner_1261_parte_A_mesa.md`).
  - **Pre-medición B′ (BKL-0040):** la regla «no asignar el rol si la norma nombra otro sujeto» daría el rol a 1.362 − 986 = 376 normas (el
    28 % de las sin `aplica_a` de los nueve documentos con alcance), y no a 986. Observación de la verificación: «palabra entera» está
    implementada como «rodeada de espacios»; con límite de palabra (`\b`) serían 1.056 y 306. La precisión de la regla sigue sin medir:
    el rediseño necesita su lectura de 30 normas de las 376, como la parte B. Nada de esto rige.
  - **Re-sellado del grafo evaluado:** NO con R2-2 (los sha `892f3803…`/`75f8e599…` cambian otra vez con la salida de S19). Borrador de
    la etapa y de su orden con la corrección de bases en `borrador_resellado_grafo_evaluado_tanda0_mesa.md`.
  - **Firma de la enmienda 4 del protocolo:** lo que la enmienda pedía está (script con su prueba, registro de alcance legible por código,
    fila F08d en la tabla, umbral de 2 unidades medido en R2-1: 14 claves llegan a 2 en diez); la mesa recomienda firmarla después de R2-3
    (para no firmar una regla cuyo gate frena en S19), con las decisiones al firmar: umbral 2 confirmado, parte A solo en r2b, cableado
    del registro como condición 11-bis. Commit de R2-2 PENDIENTE de la autora.
- **07/10/2026 — decisiones de la autora sobre el FRENO R2-2 (R2-2 commiteada en `a079275`).** (1) S19: el propuesto de la parte A
  recibe como `padre_sugerido` la sugerencia guardada del modelo, con marca (`padre_desde_sugerencia_modelo`); sin sugerencia, la
  raíz del catálogo con marca (`padre_por_defecto_generico`); S19 no se toca. (2) Un solo re-sellado del grafo evaluado de la tanda 0:
  después del grupo C (bases de los relativos) de U-OMISIONES-COD v2 si corre antes del pre-registro de la tanda 1; si no, se
  re-sella con R2-3 y la corrección de bases rige desde la tanda 1, declarada. (3) La enmienda 4 al protocolo se firma después de
  R2-3. (4) R2-3 (USD 0): la salida de S19 y la corrección de `runner_corpus.py:1261` (`parte_a` en `cerrar_e2_r2`), con sus casos
  de selftest, sin re-sellar; despacho preparado por la mesa (`despacho_R2-3_URERESOL_CAT_mesa.md`). La tabla de reprocesamiento
  recibió el 07/10/2026 la fila F13c (registro de alcance por tanda) y F13 pasó a «solo código sobre lo guardado» (implementada
  por R2), con el selftest de claves corrido sobre una copia y su JSON regenerado.
- **07/10/2026 — revisión del FRENO R2-3 por la mesa (R2-3 sin commit al escribir esta nota; R2-2 en `a079275`).** Reproducido sobre una copia
  sin enlaces, sin API ni Neo4j: diffs +42/−1, +1/−1, +147, +3; la rama b′ (`:906-931`) toma solo filas en cuarentena con motivo de la parte A en
  documento sin alcance y propuesto sin padre, marca `padre_desde_sugerencia_modelo` con una única sugerencia del catálogo y, si no,
  `padre_por_defecto_generico` hacia `Sujeto_sujeto` (verificada: la única de 70 clases sin padre; `Sujeto_sujeto_regulado` cuelga de ella);
  corre antes del paso de las instancias y del paso c. r2b diez `40c54830…` (8.817/27.633) y sin cola diez `8d747e57…` (8.504/26.130): contra
  los sellados, +1 nodo, 4 `aplica_a` movidas y +1 `padre_sugerido` flaggeada, nada más; resumen (a) 1, (b) 0, `padre_por_defecto` 6,
  `sin_rol_de_alcance` 0; las otras cuatro cadenas byte a byte; shapes PASA, S19 PASS, 0 bloqueantes en FAIL; `cerrar_e2_r2` sobre docvig con el
  camino de imports del runner da las 4 filas byte a byte con el ensamblado (HEAD: R4); selftests 133/133, 66/66, 184/184, 55/55, 17/17
  (`catalogo_unico` solo con `.git`, declarado); suite: seis entradas byte a byte con las 3 regresiones r2b preexistentes; selftest de claves
  OK en 44 filas con el JSON byte a byte. Repo sin cambios durante la verificación; 2.213 `.pyc`.
  - **No se sostiene la afirmación sobre las anclas de la tabla** («12 de las 14 corren»): `r2_3_medicion.py anclas` solo trasladó números de
    línea con difflib; buscando el commit que introdujo cada cita (`git log -S`), 10 de las 14 nacieron en `2a857db` sobre un archivo de 1.299
    líneas y ya no caían en lo que nombran en HEAD (1.608), y `:955` de F15d no nombraba lo que la fila dice; solo 3 apuntaban bien. La mesa
    reescribió las 14 contra el árbol con R2-3 (1.649 líneas), por el texto que nombran, con una nota fechada en la tabla; el selftest de claves
    volvió a dar OK con el JSON igual. Error del freno declarado y corregido en el mismo commit.
  - **Decisión de la autora, regla general (R2-3 bis):** todo propuesto sin padre del modelo en un documento sin alcance, con cualquier motivo
    del registro (`sin_match`, `ambiguo`, `id_fuera_de_catalogo`, además de los tres de la parte A), toma la sugerencia del modelo si la hay y
    está en el catálogo, o la raíz `Sujeto_sujeto`, con su marca; un caso de prueba por motivo; antes de la tanda 1 (ri_oc, ceninf y cirmo3 sin
    alcance). En diez, el registro trae `sin_match` 147, calificador 128, `mencion_no_verificada` 19 y colectivo 4; los 6 propuestos que hoy
    reciben el rol por el paso c (9 filas `sin_match`, cap 5 y ext 4) quedarían sin padre sin alcance. Despacho de la mesa:
    `segui_R2-3bis_URERESOL_CAT_mesa.md`. La enmienda 4 al protocolo quedó en versión para firmar (decisiones al firmar propuestas); la autora
    la firma después de R2-3 bis.
  - Commit de R2-3 PENDIENTE de la autora (con las anclas de la tabla, la enmienda 4 para firmar y el registro de los 15 excluidos).
- **07/10/2026 (noche) — R2-3 commiteada en `803623a` y R2-3 bis en `dac7d57`; revisión del FRENO R2-3 bis por la mesa; cierre de R2.**
  Reproducido sobre copias sin enlaces, con el código de `dac7d57` y, como control, con el ensamblador de `803623a`, los dos puestos con
  `git archive` y verificados por sha contra `git show`.
  - **Parche.** 7 archivos: el ensamblador +9/−9, `selftest_r3` +77/−10, el procedimiento +4/−3, y cuatro nuevos. `runner_corpus.py` no
    cambia. En la rama b′ (`ensamblar_tanda0.py:906-931`) sale el filtro por `E4.MOTIVOS_PARTE_A` (`:909`). El archivo sigue con 1.649
    líneas, y las anclas de la tabla de reprocesamiento al ensamblador siguen apuntando a lo que nombran.
  - **Las seis cadenas** dan lo mismo con el ensamblador de `dac7d57` y con el de `803623a`: r2a `70d51e42…` y `fa4c1043…`; r2b diez
    `40c54830…` y sin cola diez `8d747e57…`; desarrollo `6e756043…` y sin cola desarrollo `2922b72d…`. `controles`, corrido dos veces, da
    el JSON commiteado byte a byte.
  - **Shapes** de las dos de diez: PASA, S19 PASS, 0 bloqueantes en FAIL.
  - **Selftests.**
    - `selftest_r3` da 140/140. Control negativo: con el ensamblador de `803623a` da 135/140, y fallan exactamente T11i y T12a a T12d.
    - `selftest_reresolver_catalogo` 66/66, `selftest_regression_kg` 184/184, `selftest_prompt_r2b` 55/55 y `pruebas_t3bis` 17/17.
    - `selftest_catalogo_unico` queda sin verificar en la copia: exige `.git` y frena en K1.
  - **Simulación.**
    - Dos corridas, iguales byte a byte al JSON commiteado; también recomputada sin importar el ensamblador.
    - Los 6 propuestos del paso c (cap: 2 con 5 filas; ext: 4 con 4) van a la raíz, con `padre_por_defecto_generico`; marca (a) 0,
      `sin_rol_de_alcance` 0, y S19 PASS en las cuatro variantes.
    - La cuarentena antes de normalizar: 4 + 19 + 147 = 170 filas.
  - **`selftest_clave_cache --salida-r2b`:** OK (A1r 2.449/2.449; A3r 1.386 y 1.054; contraste de 44 filas, 0 discrepancias); el JSON es
    igual al del repo.
  - **Control del repo.** Sin cambios durante la verificación: 1.352 archivos de las rutas tocadas, diff vacío; 2.213 `.pyc`.
  - **Una oración del FRENO, precisada.** El FRENO dice que «en la tanda 0 ningún propuesto fuera de la parte A está en un documento sin
    alcance», y no es exacto. En docvig, `Sujeto_propuesto_estas_verificaciones` tiene 2 filas `sin_match` en cuarentena. La rama b′ no lo
    toca porque el nodo ya trae `padre_sugerido` (`Sujeto_sujeto_regulado`). La oración exacta: ningún propuesto *sin padre del modelo*. No
    cambia ninguna cifra.
  - **Etiqueta a poner al día (PENDIENTE, en el próximo asiento de la tabla):** la fila F15d (`tabla_reprocesamiento.md:173`) describe
    `:906-931` como la regla de la parte A de R2-3, pero desde R2-3 bis cubre cualquier motivo.
  - **El error propio de R2-3 que declara el FRENO** está bien descrito en lo que afirma y en su causa. Le falta que el ancla `:955` de F15d
    nunca nombró su fila, y que de las 14 anclas eran correctas 3.
  - **Cierre de R2.** Con R2-3 bis queda cumplida la condición de la enmienda 4 al protocolo: el script funcionando, la parte A y la regla
    general del padre. La enmienda queda lista para firmar, actualizada hoy con lo que congela (§6) y lo que hace falta antes de la tanda 1
    (§7: la unidad del cableado del registro en `prompt_r2b.py`, después de la firma). U-RERESOL-CAT no tomó dos pases: BKL-0021 (opción c,
    decisión del 06/10) y BKL-0028. Van a la ficha del laudo B2.4. Siguen PENDIENTES de la autora la firma de la enmienda 4 y el cierre de
    la unidad.
- **07/10/2026 (noche) — nombres de los grafos (nota de equivalencia; protocolo de los dos grafos, §1, FIRMADO el 07/10/2026).** Donde las notas de este mandato dicen «grafo evaluado de la tanda 0» (por ejemplo, la decisión (2) del 07/10/2026 sobre el re-sellado único), léase «grafo sin cola de la tanda 0». «El grafo evaluado» queda para el escalado que se sella antes de B6.3. El texto firmado no cambia.
