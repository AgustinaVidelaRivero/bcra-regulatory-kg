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
