FIRMADO por la autora el 05/10/2026 (firma por mensaje de la autora; versión para firmar en `f1e4e1b`). La decisión 6 queda abierta: es precondición de S2.

MANDATO — U-SEG-OFICIAL: SEGMENTACIÓN OFICIAL CON e0-r2 DE LOS 152 TOs DEL UNIVERSO, VERSIONADA CON SU MANIFIESTO.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad en TRES ETAPAS con FRENO obligatorio al final de cada una: S0 (correcciones de E0 que cambian
  ids de la partición, y la E0 de ri_spi), S1 (manifiesto y corrida) y S2 (diferencias contra la
  partición y cifras para la tesis). Reporte corto (no más de 40 líneas) y espera del «seguí» escrito de
  la autora.
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa.
- PRECONDICIÓN, cumplida: el cierre de U-R2-CODIGO-2, C2, commiteado por la autora en `9f6361e`
  (04/10/2026). Sus puntos (f), (h), (l) y (n) cambian e0-r2
  (docs/mandatos/UR2CODIGO2_correcciones_previas_a_reext.md). S0 edita E0 sobre el código vigente, y S1
  corre con el código que deje S0 y lo registra.
- CONVIVENCIA CON U-REEXT-T0 (mandato firmado en `e2027dd`), que el 05/10/2026 está en T2, extrayendo.
  - Su runner importa `correr_e0` en el momento en que una unidad corta (`corpus_v2/runner_corpus.py:476` y
    `:673`), y su selftest de claves carga `e0_lib` y `correr_e0`
    (data/experiment/mantenimiento/code/selftest_clave_cache.py:919 y :1212). Sus verificaciones corren
    sobre copias del árbol de trabajo.
  - S0-1, el diseño, puede correr en paralelo: lee el repo y escribe solo en la carpeta de la unidad y en
    el scratchpad. El prototipo de cada regla va en una copia, nunca en el repo. Esa copia no lleva las
    bases de caché ni `corpus_tanda0/salida_r2b/`. El control de sha256 del repo excluye, declarado, lo que
    U-REEXT-T0 escribe mientras corre: esa carpeta, las bases de caché de E1 y de E3, los logs de usage y
    data/experiment/reext_t0/.
  - S0-2, la implementación, edita `e0_lib.py` y `correr_e0.py`: no arranca hasta que la autora haya
    commiteado el FRENO T5 de U-REEXT-T0 (decisión 4). Antes de editar, mostrá ese commit con
    `git log`. Si no está, frená sin escribir.
  - S1 y S2 no editan código y escriben solo en la carpeta de la unidad.

CONTEXTO, con sus anclas.
- La partición vigente (data/experiment/segmentacion_84/b584_particion/) la produjo el código de B5.8.4,
  no `correr_e0.py` (docs/checklist_pre_escalado.md:85). `particion_152.json`, clave `agregados`: 138
  reconocidos plenos (4.183 páginas, 9.266 unidades), 2 parciales (2.413 páginas, 46 unidades) y 12 no
  segmentables (161 páginas, 12 unidades); 9.324 unidades en total. Modo de lectura en
  `conteos_b584.json`: 91 vigente, 5 con marcadores y 56 sin raíz.
- El checklist `:85` pide regenerarla antes de la tanda 1 con `correr_e0.py --version-e0 e0-r2`, con la
  regla L y la escalera, con el código de `e1c9456` o posterior. Con el punto (f) de U-R2-CODIGO-2, la
  versión que corresponde es la e0-r2 del cierre de esa unidad (`9f6361e`).
- La escalera ya se controló sobre los 152 en R5 de U-R2-CODIGO, en el scratchpad
  (data/experiment/r2_codigo/r5_freno.md, §D; `r5_escalera_particion.py`): ningún TO que la partición
  segmenta quedó en 0 chunks; 128 TOs con los mismos ids; 69 ids desambiguados (L), 7 unidades sin partir
  por tabla y 205 ids de K en 19 TOs. Con K-a′+K-b quedaron 93 ids de K en 16 TOs (`e1c9456`). Esa corrida
  no está versionada: la tesis no la cita.

S0. CORRECCIONES DE E0 QUE CAMBIAN IDS DE LA PARTICIÓN (decisión de la autora del 04/10/2026).
Salen de la revisión independiente (reports/u_revision_libre/freno_b1.md), de las enmiendas del
04/10/2026 a las adendas del laudo B5.5, del FRENO C2 de U-R2-CODIGO-2 (punto 5) y del censo de unidades
grandes (punto 6). No se ven en la tanda 0 y no entran a C2 de U-R2-CODIGO-2.
1. Sección escrita de otra forma (1.14): opecam («Seccón 3.»), garopt y snp_dd.
2. Rótulos de punto que no lo son (1.15): rdbcra, ri_niif, ri_tsa y ri_dsf.
3. Páginas de norma fuera de toda unidad (2.4): ri_cc, ri_tsa, snp_mep, venliq y fimipyme.
4. E0 de ri_spi: regla de marcador de letra y número («APARTADO A», «A.1.», «A.1.1.»). Hoy queda en una
   unidad de 18.565 caracteres. Es la unidad de E0 de ri_spi que piden las enmiendas.
5. Cola de título en toda página (punto l de C2 de U-R2-CODIGO-2; decisión de la autora del 04/10/2026, tras
   el FRENO C2). En C2 la regla rige solo en cuatro páginas de ric (pp. 15, 30, 54 y 59;
   `correr_e0.COLA_TITULO_ESTRICTA_E0_R2`), porque aplicada a toda página mueve ids de la partición. La
   medición de la regla general (`continua_titulo`) sobre los 152 TOs la dejó C2
   (data/experiment/r2_codigo2/salidas/c2_e0.json, `particion_152_cola_en_toda_pagina`; comando:
   `data/experiment/r2_codigo2/c2_e0_152.py --salida <dir> --cola-en-toda-pagina`). La revisión del freno
   la reprodujo sobre una copia, con el archivo regenerado byte a byte:
   - recupera 34 renglones en 7 TOs: cirmo3 (2), cryl (1), manori (1), ri2_ci (8), snp_cheq (2), snp_mep (2)
     y fabcra (18). Los 16 de los seis primeros son texto corrido de la norma. Los 18 de fabcra son las
     celdas de su tabla002, que deja de serializarse y pierde sus 12 renglones de tabla;
   - mueve ids en un TO: en snp_cheq aparece `snp_cheq::7.1::intersticial::290`, el orden de los ids comunes
     cambia y cambian 179 chunks, 13 de ellos por el recorte de la herencia (punto h de C2);
   - en total cambian 267 chunks en 14 TOs, contra 93 en 9 TOs con la lista de páginas.
   El diseño decide si la regla general entra, y con qué guarda para snp_cheq y para la tabla de fabcra, o si
   la lista de páginas se amplía a los seis TOs con texto corrido recuperado.
6. Unidades que no entran en una llamada de E1 (decisión de la autora del 04/10/2026). Censo sobre los 152 TOs
   con e0-r2 y el código de C2 de U-R2-CODIGO-2 (9.385 unidades; scripts y salidas en el paquete de la
   revisión del 04/10/2026, fuera del repo: esta etapa lo recomputa y lo versiona).
   - 57 unidades en 32 TOs miden más de 13.091 caracteres con su herencia: 46 por su texto propio y 11 por
     texto propio más herencia. Son 22 secciones sin puntos, 12 puntos terminales, 11 partes de puntos
     terminales que E0 ya partió, 7 cierres, 4 chapeaux de sección y 1 intro; ningún intersticial.
   - La partición por tamaño de E0 (`correr_e0.py:74-76`: umbral de 26.182 caracteres de texto propio,
     objetivo de 13.091 por parte) partió 5 unidades en 23 partes. No cubre a las otras: 27 están entre
     13.091 y 26.182, bajo el umbral; 13 pasan el umbral y quedan declaradas sin partir (11 por tabla
     serializada y 2 sin ítems); y 5 mini-chunks pasan el umbral y `subdividir_unidades_grandes` los saltea
     sin declararlos: `manual::S2::cierre` (255.192 caracteres), `nmaeef::S11::chapeau_seccion`,
     `ri_ccna::S8::cierre`, `manori::S1::cierre` y `manori::S3::cierre`.
   - En E1, con el perfil r2, una unidad que corta a 8.192 tokens se reintenta a 16.384 y, si vuelve a
     cortar, se parte por ítems sin cortar tablas (`particionar_por_corte`). Simulado sobre las 46 unidades
     que no son partes: 30 se pueden partir y 16 no, por falta de ítems. Una parte no se vuelve a partir. En
     19 de las 30 la parte mayor pasa de 13.091 caracteres, y en 6, de 26.182.
   - Riesgo, con la salida que midió P4 de U-PROMPT-R2 con el prefijo de P3b-2 (04/10/2026): 1,175 tokens
     por carácter de texto propio, mediana de 6 unidades de 3.000 caracteres o más (de 3.109 a 9.825), con
     0,224 de mínimo y 1,498 de máximo. El reintento de 16.384 tokens alcanza unos 13.944 caracteres con la
     mediana y 10.937 con el máximo; el primer intento, 6.972 y 5.469. Con el prefijo sellado las cifras
     eran 0,86 de mediana y 1,12 de percentil 90 (40 unidades de la tanda 0): unos 19.000 y 14.600
     caracteres.
     Por texto propio, 66 unidades en 37 TOs pasan de 10.937 caracteres, y 43 en 30 TOs, de 13.944.
     - Clase A, 14 unidades: no se pueden partir y pasan de 13.944. Terminarían sin extracción, con error
       declarado. Son las 8 que ya estaban (`cateloc::S2`, `snp_mep::S7`, `manori::S2`, `ri_laft::3.7`,
       `manori::S4`, `ri_niif::3.2`, `seggar::8.2` y `ri_oc::3.51`) y 6 más: `ri_spi::S0`, `ri_psp::SIII`,
       `ri_iepsp::S4`, `nmcief::S3::chapeau_seccion`, `ri_tsa::3.2` y `dmrd::S0`.
     - Clase B, 15 unidades: se parten, pero su parte mayor pasa de 13.944 y no se vuelve a partir.
     - Clase C, 32 unidades: entre 10.937 y 13.944, en el borde. De ellas, 10 quedan ahí después de
       partirse y 12 son partes que ya hizo E0.
     - Clase D, 5 unidades: entran en el reintento después de partirse.
     Con las cifras del prefijo sellado las clases eran 8, 12, 8 y 29, sobre las 57 unidades de más de
     13.091 caracteres con su herencia. De esas 57, 3 no pasan de 10.937 caracteres de texto propio y salen
     del censo; entran 12 que no estaban.
     Es una cota: la medición de P4 tiene 6 unidades, ninguna de 10.000 caracteres o más, y con el prefijo
     sellado la razón baja con el tamaño (0,46, 0,69 y 0,84 en las tres de más de 10.000 de la tanda 0).
     La capacidad se recalcula con los tokens de salida por carácter que mida T2 de U-REEXT-T0 sobre todas
     sus unidades, con el prefijo de P3c de U-PROMPT-R2 (`322c5a23e9b7`) y temperatura 0. Si su FRENO T2 no
     está commiteado al hacer el diseño, el punto 6 se diseña con esta cota y se recalcula cuando esté: la
     clase de una unidad puede cambiar.
   El diseño decide, con su censo de ids por TO:
   a. Ninguna unidad se saltea sin declararla: los cinco mini-chunks que hoy E0 saltea en silencio pasan a
      declarados, y la partición por tamaño dice si los alcanza.
   b. Ninguna unidad de la tanda 0 cambia, `cap::4.2.1.2` incluida (26.726 caracteres en e0-r2, declarada
      por tabla serializada). Si un arreglo la tocara, se declara y lo decide la autora.
   c. Para las unidades de la clase A (14 con la cota de P4; eran 8 con las cifras del prefijo sellado), S0
      propone una solución (una regla por párrafo o por página, u otra) o las declara como límite con su
      cifra.
   d. Si la partición por tamaño parte respetando los bloques de tabla, como ya hace `particionar_por_corte`,
      en lugar de declarar la unidad sin partir; qué se hace con una parte que sigue grande; y si el umbral
      baja del de desarrollo (26.182) para e0-r2, con los ids que mueve.
Primero el diseño, sin implementar: cada regla con su censo sobre los 152 TOs (qué TOs y qué ids cambian).
FRENO S0-1. Después del «seguí», la implementación, solo en e0-r2. Controles:
- la E0 de la tanda 0 que dejó U-R2-CODIGO-2 (`salida_tanda0_r2b/`) no cambia un byte;
- cada id que cambia en la partición queda atribuido a una de las seis reglas, por TO; lo que ninguna
  explique es «otra» y se lee;
- toda unidad que pase del umbral de la partición por tamaño queda partida o declarada: ninguna salteada;
- los TOs que ninguna regla toca dan los mismos ids que antes (guarda 1 de la adenda 2 al laudo B5.5);
- cada regla, con la fila de la tabla de reprocesamiento que le corresponde
  (data/experiment/mantenimiento/tabla_reprocesamiento.md, F01 a F03 u otra), y el selftest de claves corrido
  sobre una copia, con el contraste en OK: ninguna clave de la tanda 0 se mueve. Si hace falta una fila
  nueva, se propone en el freno y no se escribe;
- selftests de E0 sobre una copia, y doble corrida byte a byte igual.
FRENO S0-2.

S1. MANIFIESTO Y CORRIDA.
1. Manifiesto de los 152, en el formato de `manifiesto_corpus` (data/experiment/reextraccion_v2/): id,
   archivo, sha256 del PDF de data/experiment/escalado_prep/pdfs/ contra el de la descarga
   (`escalado_prep/descarga_log.json`, 152 entradas), y la vía de cada TO:
   - por punto: los TOs que e0-r2 segmenta por la escalera, con su modo de lectura;
   - por página: los que no tienen espina reconocible. Hoy la vía de páginas existe solo como salida de
     U-COB-A (data/experiment/cobertura_bloque_a/chunks_a2.json: 191 unidades de 9 TOs); e0-r2 no la
     produce. El manifiesto la declara por TO, con su fuente, y no la regenera;
   - fuera: los declarados referencia pura y los parciales, con su causa
     (`adjudicaciones_b584.json`, `e_no_segmentables`).
   La clase de cada TO sale de `particion_152.json`; si e0-r2 la cambia, es hallazgo y se reporta.
2. Corrida: `correr_e0.py --version-e0 e0-r2 --manifiesto <manifiesto> --salida <dir>`, primero en el
   scratchpad. Doble corrida en directorios distintos, byte a byte iguales.
3. Salida versionada en data/experiment/segmentacion_oficial_e0r2/ (se crea): los chunks por TO,
   `version_e0.json`, `ids_desambiguados.json`, `encabezados_conservados.json`, las tablas, el manifiesto
   y un `manifest_salida.json` con el sha256 de cada archivo, el commit del código y el comando.
4. Controles: health-check de E0 por TO; ningún TO de la vía por punto en 0 chunks; ningún id repetido.
   Los cinco TOs de la tanda 0 que son de la partición (ctacte, lingob, polcre, pagjub y docvig) dan
   byte a byte la e0-r2 de la tanda 0 que dejó U-R2-CODIGO-2 (`salida_tanda0_r2b/`, `9f6361e`); los cinco
   de desarrollo no son de la partición y no entran.
5. Censo de vigencia. Por cada uno de los 152 TOs, las marcas de su carátula y de su título en el índice
   («Derogado», «Vigente hasta», «vigente al»), con la página y la línea. El manifiesto declara qué TOs
   son vigentes. Casos ya conocidos: `manual` («Vigente hasta el 31/12/2017») y ri_ao («RI Derogado por
   la Com. A 8262»). Una marca nueva es hallazgo y se reporta; la decisión es de la autora.
6. Herencia por unidad. La herencia máxima por unidad y la lista de las unidades que lleven el recorte del
   punto (h) de C2 de U-R2-CODIGO-2 (`correr_e0.TOPE_HERENCIA_E0_R2`, `correr_e0.py:80`), con su TO, su
   texto propio y el bloque heredado mayor. Sobre la partición de B5.8.4, 95 unidades de 11 TOs pasaban de
   13.091 caracteres de herencia; el FRENO C2 da, sobre los 152, 93 unidades en 9 TOs
   (data/experiment/r2_codigo2/freno_c2.md:69).
FRENO S1.

S2. DIFERENCIAS CONTRA LA PARTICIÓN Y CIFRAS.
PRECONDICIÓN DE S2 (decisión 6, abierta al firmar): antes de despachar S2, la autora fija contra el texto
vigente del capítulo 4 las definiciones del punto 4: qué TOs forman cada conjunto, qué es una clase de
documento y qué documentos «toman el primer nivel como sección». Llegan en el «seguí» de S2. Sin ellas,
el punto 4 no se computa: frená.
1. Diferencias contra `b584_particion/`, atribuidas por clase como en el control de R5: ids desambiguados
   (L), unidades sin partir por tabla, ids de K, lo que cambien los puntos (f), (h), (l) y (n) de
   U-R2-CODIGO-2 y lo que cambie S0; texto distinto por tablas, pies, K y arrastre. Lo que ninguna clase
   explique se lista como «otra». Criterio de aceptación: «otra» en 0, o cada caso leído y explicado.
2. Diferencias contra la escalera de R5, si la corrida de R5 se puede reproducir con `e1c9456`: solo las
   que explican K-a′+K-b y el punto (f).
3. Cifras que la tesis va a citar, cada una con el archivo, la clave y el comando que la reproduce:
   - TOs por vía y por modo de lectura; páginas y unidades por clase;
   - unidades totales, chunks terminales y mini-chunks; unidades partidas por tamaño;
   - tablas detectadas y unidades con tabla serializada;
   - ids desambiguados y chunks de índice que quedan, por TO;
   - encabezados conservados por K, por TO;
   - los 12 no segmentables y los 2 parciales, con sus páginas.
4. Cifras que la tesis toma de la segmentación fuera de la sección 4.1 (hallazgo de la escritura del
   capítulo 4, del 05/10/2026). Hoy salen de la partición legada:
   reports/u_insumos_cap/estadisticas_corpus.md (`ded3494`) y reports/u_cap3_datos/datos.md, D3. Se
   recomputan sobre la segmentación oficial, y cada una va al lado de la cifra legada, con su diferencia:
   a. las unidades por conjunto (desarrollo, validación y universo a escalar), en total y por tipo de
      unidad;
   b. los puntos de la estructura y el porcentaje de terminales, por clase de documento;
   c. los documentos que toman el primer nivel como sección o no son segmentables, con la lista de TOs de
      cada grupo.
   Las definiciones de los conjuntos, de la clase de documento y del «primer nivel como sección» son las de
   la precondición de S2: no se toman del reporte legado. Lo que hay para fijarlas:
   - el reporte legado agrupa por conjunto (`desarrollo_5`, `tanda0_5` y `corpus_152`: 1.763, 671 y 9.324
     unidades; 1.475 de 1.810, 577 de 710 y 7.413 de 9.105 puntos terminales) y por categoría (normativa
     general y régimen informativo), y cuenta 56 TOs en modo de lectura sin raíz;
   - el borrador del 30/09/2026 de los capítulos 3 y 4 agrupa los documentos en tres grupos, según cuánto
     de su contenido está escrito como puntos normativos numerados: 138, 2 y 12 (dato de la autora; ese
     texto no está en el repo: NO VERIFICADA). Son las cantidades de las tres clases de la partición
     (`particion_152.json`, `agregados`: 138 reconocidos plenos, 2 parciales y 12 no segmentables).
   La fuente de los TOs que no son de la partición es la e0-r2 de la tanda 0 (`salida_tanda0_r2b/`,
   `9f6361e`), que esta unidad solo lee. Si una regla del reporte legado no se puede aplicar igual sobre
   e0-r2, se declara y no se adapta en silencio.
   Los puntos 3 y 4 van a `cifras_segmentacion_oficial.md` en la carpeta de la salida, cada cifra con su
   archivo, su clave y su comando, recomputada contra su artefacto. Es el artefacto que lee la verificación
   de las marcas [AL CIERRE: e0-r2] de la sección 4.1 (docs/insumos_escritura.md, §6), y del que la tesis
   toma las cifras del punto 4.
FRENO S2, final.

ESCRITURAS: data/experiment/segmentacion_oficial_e0r2/ y el scratchpad. En S0-2, y solo desde que se cumpla
la condición de la convivencia: data/experiment/reextraccion_v2/e0_chunking/e0_lib.py y correr_e0.py, solo
en la versión e0-r2, y sus selftests. Si hace falta un script de comparación, va en la carpeta de la salida;
`r5_escalera_particion.py` se usa sin editar.
PROHIBIDO: editar `b584_particion/`, las salidas selladas de E0 y la E0 de la tanda 0
(`salida_tanda0_r2b/`); tocar `corpus_tanda0/`, las bases de caché, data/experiment/reext_t0/ o cualquier
archivo que U-REEXT-T0 esté escribiendo; editar código del repo en S0-1; cambiar la versión legada de E0;
editar la tabla de reprocesamiento; tocar `.gitignore`; commitear. En S1 y S2 el código de E0 no se edita:
si un control falla por el código, se reporta y no se corrige ahí.

DECISIONES DE LA AUTORA AL FIRMAR, tomadas el 05/10/2026.
1. La carpeta de la salida: data/experiment/segmentacion_oficial_e0r2/.
2. El manifiesto incluye a los 14 fuera de las tandas, con la vía que les fijan las enmiendas firmadas a
   las adendas 1 y 2 del laudo B5.5 (`e82e22f`), para que el artefacto cubra los 152.
3. Si la salida se commitea entera o solo el manifiesto con los sha256 se decide en el FRENO S1, con el
   tamaño medido.
4. S0-2, que edita código de E0, arranca desde el commit del FRENO T5 de U-REEXT-T0: T3 y T5 también
   corren código de E0 sobre copias del árbol de trabajo.
5. S0-1 arranca ya, en paralelo con T2 de U-REEXT-T0.
6. ABIERTA. Las definiciones del punto 4 de S2 no se firman ahora, porque salen de un reporte legado y no
   del texto de la tesis. Se fijan contra el texto vigente del capítulo 4 antes de despachar S2
   (precondición de S2).
7. La clase A del punto 6 de S0 son las 14 de la cota de P4, recalculadas con la medición de T2 de
   U-REEXT-T0. La decisión del 04/10/2026 hablaba de 8.
8. S0-2 lleva el control de la tabla de reprocesamiento y del selftest de claves.

REQUISITOS: los de CLAUDE.md §4 (a a l), con PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; corridas,
selftests y verificaciones sobre una copia sin enlaces, con el sha256 de los archivos del repo antes y
después, con las exclusiones declaradas de la convivencia; fuentes firmadas leídas en el commit de su firma;
todo conteo recomputado contra su artefacto; cada dato con su ancla o marcado NO VERIFICADA; cero nombres
de personas; paquete de revisión con manifest.

NOTAS POSTERIORES A LA FIRMA. El texto firmado no se edita; estas notas se leen junto con él.
- **05/10/2026 — complemento del punto 4 de S2 (decisión de la autora, tras VERIF-SEG-OFICIAL-41).** La firma
  quedó commiteada en `e543cb2`, y S0-1 está despachada. En `cifras_segmentacion_oficial.md` también van,
  cada cifra con su archivo, su clave y su comando, recomputada contra su artefacto:
  - 4.d. La lista de las reglas de segmentación vigentes en e0-r2, las que queden después de S0-2, con los
    documentos que usa cada una. Sirve para rehacer la tabla de reglas de la tesis, que hoy sale de la
    partición legada (reports/u_cap3_datos/datos.md, D3). Cada regla va con el lugar del código donde está
    y con la lista de los TOs en los que actúa, sacada de la salida de S1.
  - 4.e. Las unidades por grupo de documentos, con sus documentos y sus páginas, en tres grupos: los
    escritos en puntos de principio a fin, los que tienen fichas y listados de registro, y los no
    segmentables. Y una fila aparte con lo que queda fuera del grafo según las enmiendas a las adendas 1 y 2
    del laudo B5.5 (docs/enmiendas_adendas_1_y_2_laudo_B5.5_2026-10-04.md, leídas en `e82e22f`), con la
    razón de cada caso. Legadas, para poner al lado (`particion_152.json`, `agregados`): 138 documentos,
    4.183 páginas y 9.266 unidades; 2, 2.413 y 46; y 12, 161 y 12.
  - Los tres grupos de 4.e son la propuesta de la autora para la «clase de documento» de la decisión 6.
    Corresponden a las tres clases de `particion_152.json`: 138 reconocidos plenos, 2 parciales y 12 no
    segmentables. Se confirma antes del despacho de S2, junto con las otras dos definiciones (los conjuntos
    y el «primer nivel como sección»). Hasta entonces rige la precondición de S2.
- **05/10/2026 — séptimo punto del diseño de S0-1: párrafos sin numerar que empiezan con un número de
  punto (decisión de la autora, tras la verificación VSEG41 del 03/10/2026).** La nota anterior quedó en
  `2bfda2a`.
  - El hallazgo. Entre los párrafos sin numerar del universo (los intersticiales de e0-r2), 36 tienen como
    primera línea un número de punto de 2 o más niveles y pueden ser subpuntos que la segmentación no
    reconoce: 27 en ri_mmsef, 6 en rdbcra, 2 en ri_dcpc y 1 en snp_cheq. De ellos, 28 quedan atribuidos a una
    sección (27 a S2 de ri_mmsef y 1 a S3 de snp_cheq) y 8 a un punto (6 a `rdbcra::2.3` y 2 a
    `ri_dcpc::3.1`). La cifra es de esa verificación, que corrió sobre una copia con la e0-r2 de su fecha,
    anterior a C2 de U-R2-CODIGO-2; su lista no está en el repo.
  - Qué se suma. El diseño de S0-1 lleva un séptimo punto, junto con las seis reglas: el censo de esos
    párrafos recomputado con el código vigente, si se reconocen como subpuntos y con qué regla, y qué TOs y
    qué ids cambian en los 152. Se diseña junto con la regla 2 (rótulos de punto que no lo son; rdbcra está
    en las dos), la regla 1 y la guarda de snp_cheq de la regla 5, porque se cruzan.
  - Condición. La E0 de la tanda 0 sigue byte a byte igual, y los documentos que la regla no toca dan los
    mismos ids. Si no se puede corregir así, queda registrado como límite medido, con la lista de los casos.
  - En los controles del FRENO S0-2, «una de las seis reglas» se lee como «una de las siete».
- **05/10/2026 — lectura de cortes contra el PDF y censo de renglones: puntos 7 y 8 de S1, y su cifra en S2
  (decisiones de la autora).** La nota anterior quedó en `b56984c`.
  - Por qué. Ningún control de E0 mide si cada unidad empieza y termina donde empieza y termina su punto:
    los que hay son regresión contra lo sellado, invariantes que calcula el propio código y censos de
    síntomas. El invariante de cero pérdida da exacto en los 152 TOs (`conteos_b584.json`), y la revisión
    independiente encontró renglones fuera de toda unidad (reports/u_revision_libre/freno_a.md, 2.3 y 2.4).
  - S1, punto 7: lectura de cortes.
    - Qué se lee. Una muestra de unidades de la corrida de S1, cada una contra la página del PDF renderizada
      como imagen. No contra el texto que extrae la librería de E0.
    - Criterio. Una unidad es correcta si: (1) empieza donde empieza su punto; (2) termina donde termina;
      (3) no trae texto de otro punto ni restos de encabezados o pies de página; (4) no le falta texto
      propio; y (5) su número es el del punto.
    - Tres reglas para los casos dudosos. Una parte de una unidad partida por tamaño es correcta si corta en
      un límite de ítem y está declarada. Los guiones de silabeo no son error. Un párrafo sin numerar es
      correcto si cubre exactamente ese párrafo.
    - Dos clases de error; cada error lleva su clase y su subclase. De corte: empieza fuera de su punto,
      termina fuera de su punto, le falta texto propio, trae texto de otro punto, o su número no es el del
      punto. De limpieza: restos de encabezado o restos de pie de página.
    - Muestra, según la clase que el manifiesto de S1 le da a cada TO:
      - primer grupo, los documentos escritos en puntos de principio a fin (los reconocidos plenos): 90
        unidades, 40 de TOs en modo de lectura vigente, 10 en marcadores y 40 sin raíz;
      - segundo grupo: las unidades por punto de ri2_pm, todas (25 en la partición);
      - tercer grupo: un juicio por cada documento no segmentable (12 en la partición): que no tenga una
        numeración de puntos que la segmentación debió reconocer.
    - Sorteo. Semilla `U-SEG-OFICIAL:cortes:2026-10-05`. Por estrato,
      `random.Random(f"{semilla}:{estrato}").sample(ids, n)`, con `ids` = los ids de todas las unidades del
      estrato (puntos terminales, párrafos sin numerar, secciones sin puntos y partes), ordenados. Si un
      estrato tiene menos unidades que su tamaño, se leen todas.
    - Sello previo. El criterio, la muestra y la semilla quedan fijados cuando esta nota se commitea, antes
      de la corrida de S1. El primer paso de S1 muestra ese commit; si la nota no está commiteada, frená.
      Después de la corrida, la instancia sortea y deja la lista de la muestra con su sha256 y su hora,
      antes del freno: de cada unidad, su id, su TO, sus páginas, su tipo y su texto propio; y, de cada
      estrato del primer grupo, cuántas unidades tiene, que es su peso en la estimación ponderada. La
      instancia de la unidad no lee ni marca.
    - Quién lee. La instancia que revisa el FRENO S1, que renderiza las páginas desde los PDF. La autora
      revisa todas las unidades marcadas como error o como dudosas, y 20 de las correctas, sorteadas con la
      semilla `U-SEG-OFICIAL:cortes:2026-10-05:revision`. Valen las marcas que queden después de esa
      revisión.
    - Piso. En el primer grupo, la cota inferior de Wilson al 95 % de la proporción de unidades sin error de
      corte tiene que ser de 0,90 o más. Se calcula sobre las 90, sin ponderar por estrato: con 90, se
      cumple con hasta 3 errores de corte (0,907) y no con 4 (0,891). Se reporta también por modo de
      lectura, como fracción. Los errores de limpieza se cuentan y se reportan por grupo, y no frenan.
    - Dos cifras del primer grupo, y el reporte dice cuál es cuál.
      - La del piso: la cota inferior de Wilson sobre las 90, sin ponderar. Decide si la salida de S1 pasa.
      - La del corpus, que es la que cita la tesis: la estimación ponderada por el tamaño de cada modo de
        lectura, con su intervalo. El peso de un modo son sus unidades sobre las del primer grupo en la
        corrida de S1 (los mismos `ids` del sorteo). La estimación es la suma, por modo, de su peso por su
        fracción de unidades sin error de corte. El intervalo es el de Wilson al 95 % con esa estimación y
        con el tamaño efectivo de la muestra, 1 / Σ(peso² / unidades leídas del modo), sin redondear. Es
        una aproximación: trata a la muestra ponderada como una simple de ese tamaño, y se declara así.
    - Si no llega al piso, la salida de S1 no se commitea y S2 no se despacha: la autora decide si vuelve a
      S0 o si queda como límite declarado con su cifra.
    - Una unidad con error que sea de un TO de la tanda 0 cuenta para el piso y, además, se reporta aparte:
      su corrección cambiaría la E0 de la tanda 0 (`salida_tanda0_r2b/`), y la decide la autora.
    - ri_spi. Si S0 le dio unidades, deja de ser del tercer grupo: se leen 10 de sus unidades, sorteadas con
      la misma semilla, con el criterio del primer grupo, y se reportan aparte, sin entrar al piso.
  - S1, punto 8: censo de renglones. Por cada página de los 152 PDF, los renglones del texto del PDF que no
    están en ninguna unidad ni en un rol declarado (portada, índice, historial, tabla de origen, ficha de
    registro, encabezado o pie). Un renglón quitado por estar en la zona de encabezado o de pie cuenta como
    rol declarado solo si se repite en otras páginas del documento; si no se repite, va a la lista. La
    regla de comparación se declara antes de correr. Se reporta el total por TO y la lista de páginas con
    sus renglones; lo que no tenga explicación se lee. No tiene piso.
  - S2, punto 4.f. `cifras_segmentacion_oficial.md` lleva el resultado de la lectura de cortes (por grupo,
    las unidades correctas como fracción; en el primer grupo, además, las dos cifras, la del piso y la
    ponderada, cada una con su nombre y su intervalo; los errores por clase y subclase, con la lista de
    los casos) y el del censo de renglones.
  - El piso es condición de la tanda 1 (docs/checklist_pre_escalado.md:81, condición 7).
- **05/10/2026 — S2, punto 4.g: la tabla de las marcas del capítulo 4 (decisión de la autora).** La nota
  anterior quedó en `2faff14`.
  - Para qué. Al aprobarse el FRENO S2, la autora arma un mandato de escritura que resuelve las marcas del
    capítulo 4 que dependen de esta unidad: [PENDIENTE: S0 de U-SEG-OFICIAL] y [AL CIERRE: U-SEG-OFICIAL]
    (docs/plan_tesis.md:404). Las marcas están en la fuente de Overleaf y no se ven desde el repo. Esta
    tabla hace que ese mandato sea mecánico.
  - Qué va. En `cifras_segmentacion_oficial.md`, una tabla con una fila por marca, o por dato si una marca
    pide varios. De cada fila: a qué se refiere, la cifra o el dato que la resuelve, el archivo y la clave
    de donde sale, y el comando que lo reproduce. Como mínimo, estas filas:
    1. los párrafos sin numerar que empiezan con un número de punto (36 en la verificación del 03/10/2026):
       cuántos son con el código vigente, cuáles pasan a ser subpuntos y cuáles quedan como límite (S0,
       punto 7);
    2. ri_spi: si quedó segmentado, con qué regla y en cuántas unidades (S0, punto 4);
    3. los documentos no segmentables, uno por uno, con sus páginas;
    4. las cifras y la tabla de los grupos de documentos, con la fila de lo que queda fuera del grafo (4.e);
    5. la tabla de los conjuntos de la sección 3.6 de la tesis (4.a);
    6. la tabla de reglas del apéndice: las reglas vigentes, con los documentos que usa cada una (4.d);
    7. las unidades partidas por tamaño: cuántas, en cuántas partes, y las que quedan sin partir, con su
       causa;
    8. la regla de tablas: en cuántos TOs corre, en cuántos encuentra tablas y cuántas unidades llevan una
       tabla serializada.
  - Si el «seguí» de S2 trae la lista literal de las marcas, la tabla lleva una fila por cada una, con su
    texto. Si una marca no se puede resolver con lo que dejó esta unidad, su fila lo dice, con la razón: no
    se completa con una cifra legada.
  - Las filas 4, 5 y 6 dependen de las definiciones de la precondición de S2.
  - No entran las marcas de U-BLOQUE-A: esperan a la tanda 3.
- **05/10/2026 — decisiones de la autora sobre el FRENO S0-1; corrección del censo de renglones de S1; dos
  diseños más antes de S0-2.** S0-1 quedó commiteada en `3920323`, con el prototipo revisado, como parche sin
  aplicar, en `s0_1/parche/`.
  - La revisión independiente reprodujo S0-1 sobre una copia: la tanda 0, 57 de 57 archivos iguales; 23 TOs
    cambian y 129 salen idénticos; las unidades pasan de 9.385 a 9.533; la cobertura, exacta en los 152; y el
    censo del punto 7, de 36 a 0.
  - Decisiones.
    1. Regla 5: la lista de 9 páginas (cirmo3 19, cryl 27, manori 6, ri2_ci 8, 9, 16 y 24, snp_cheq 80 y
       snp_mep 19). No la regla general.
    2. Acompañamiento T: se adopta.
    3. Regla 6. En E0: la partición por renglones entra en la partición por tamaño (más de 26.182
       caracteres); el umbral no baja, y las unidades con tabla serializada no se parten en E0. En E1: la
       partición por corte (`correr_e0.particionar_por_corte`, que usa el runner de E1) de las unidades de
       la tanda 0 no cambia. Con el prototipo de S0-1 cambiaba en dos, `cap::4.2.1.2` y `ric::11.2::intro`
       (hallazgo de la revisión). La partición por renglones rige en E1 solo donde hoy no hay salida y el
       tercer escalón no alcanza. El objetivo de las partes se fija con la medición de T2 de U-REEXT-T0.
    4. ri_cc (pp. 2 a 47) y ri_tsa (pp. 3 a 61): E0 no cambia. S1 las declara en el manifiesto como
       páginas de norma sin unidad, con su censo: 105 páginas y 101.721 caracteres
       (`s0_1/censos/censo_r3b.json`, sin las carátulas). Entran por la vía de página con la tanda 3, en
       U-BLOQUE-A (docs/plan_tesis.md:772).
    5. El catálogo 11.x de rdbcra y la lista de puntos leída como cuerpo (manori, ri_niif y dmrd): la
       instancia de S0-1 diseña las dos reglas con su censo, sin implementar, antes de S0-2. Rigen las
       condiciones de S0-1 y una más: la partición por corte de las unidades de la tanda 0 no cambia. Si la
       de rdbcra no sale limpia, deja marcadas sus 97 unidades terminales 11.x, para decidir si se extraen.
       Tiene su freno. S0-2 implementa solo lo que la autora apruebe.
  - Corrección al punto 8 de S1 (censo de renglones, nota de `2faff14`). Como estaba escrito, el rol de
    portada y el de índice contaban como rol declarado, y el censo no listaría las páginas de ri_cc y de
    ri_tsa, que tienen rol de portada y son norma. Se precisa: toda página con rol de portada o de índice
    que no sea la primera página del documento va a la lista, con sus renglones y cuántos son de texto
    corrido. Se leen las que tengan texto corrido.
- **05/10/2026 — decisiones de la autora sobre el FRENO S0-1 bis.** S0-1 bis quedó commiteada en `d9d2212`
  (44 archivos: `s0_1bis/` y `FRENO_S0-1bis.md`), con el prototipo revisado como parche sin aplicar en
  `s0_1bis/parche/` (el completo sobre `9f6361e` y el incremental sobre el de S0-1; los dos dan `e0_lib.py`
  `81c3409851ba82a3…` y `correr_e0.py` `f737028b1918cce0…`).
  - La revisión independiente reprodujo S0-1 bis sobre una copia: la tanda 0, 57 de 57 archivos iguales; 145 TOs
    iguales a la corrida final de S0-1 y 7 que cambian; las unidades pasan de 9.533 a 9.555 (179 ids nuevos y 157
    que desaparecen); la partición por corte de las 2.439 unidades de la tanda 0, igual a la de `9f6361e` con
    1,175 y con 1,498 (`435af2fe…`); las 119 filas del catálogo de rdbcra recontadas (91 con unidad y 28
    rechazadas); y otras 10 filas leídas contra el PDF con semilla propia, las 10 con su descripción, su gravedad
    y sus multas, sin texto de otra fila.
  - Decisiones.
    1. Regla 9: las dos partes, 9a (acepta el número de la fila, que la celda prueba) y 9b (lleva a la unidad de
       su fila los renglones de su banda). Los 49 ids que cambian en rdbcra (28 nuevos y 21 que desaparecen) se
       atribuyen a la regla 9.
    2. Páginas de índice leídas como cuerpo (adfsp p. 3, ceninf p. 2, cirmo3 pp. 3 y 4, nmaeef p. 2 y ri_niif
       p. 1): rol de índice, como ampliación de la regla 3 sobre lo que la regla 8 detecta: una página cuyo
       contenido, quitados el encabezado, el pie, las líneas «Sección N.» y «Tabla de correlaciones.», es una
       lista de la regla 8 entera, es índice, siga o no a otra página de índice. Con su censo de páginas, que
       incluye también nmaeef pp. 14 y 36 y ri2_ae p. 13 (índices de anexos cuyos rótulos hoy se rechazan y
       quedan como texto dentro de otra unidad), y con el control de que una página de índice nueva no vuelva
       portada a una página de cuerpo anterior (ceninf p. 1). Efecto medido por la revisión al forzar el rol en
       las 6 páginas: desaparecen `adfsp::S6`, `cirmo3::S7`, `nmaeef::S0` y `ri_niif::S1`; aparece `ri_niif::S0`
       con el cuerpo de la Sección 1 (pp. 2 a 4); `ceninf::S1::chapeau_seccion` queda con el chapeau de la p. 3;
       cobertura exacta; 152 renglones pasan de cuerpo a rol declarado. El límite de ri_niif se declara: la línea
       «Sección 1.» está en mitad de la p. 2 y E0 solo lee encabezados de sección en la zona de título.
    3. Orden de los renglones dentro de cada fila del catálogo: en el prototipo es el del PDF, y en las filas de
       varias líneas el renglón del número con la gravedad y las multas cae en mitad de la descripción
       (`rdbcra::11.2.1`, hallazgo de la revisión). S0-2 evalúa el orden por celda (número, descripción,
       gravedad, multas), con la condición de que no cambie nada fuera de rdbcra.
    4. El comentario del bloque «Regla 8 de S0» del prototipo describe un subconjunto de lo que el código
       acepta entre rótulos; se corrige en S0-2.
  - Quedan para el «seguí» de S0-2: la razón de tokens por carácter, la capacidad del tercer escalón y el
    objetivo de las partes, con la medición de T2 de U-REEXT-T0, y el commit del FRENO T5.
- **06/10/2026 — el hallazgo 1.16 de U-REVISION-LIBRE entra al censo de S1 (decisión de la autora; condición 9 de la
  tanda 1).** El cierre de una lista que queda dentro del último ítem (`reports/u_revision_libre/reporte.md:50`; un caso
  conocido, `pro::1.1.2.7`, PDF p. 3) se censa en S1 sobre los 152 TOs, como una línea más del censo de renglones (punto 7
  de S1), con la lista de casos. Según la cifra, S2 lo declara límite o la regla entra en la release siguiente de E0 (S0-2
  cierra antes que S1 y no cambia por esto).
- **06/10/2026 — revisión del FRENO S0-2 y decisiones de la autora (S0-2 sin commit al escribir esta nota; la nota anterior
  quedó en 0a3ac81).**
  - La revisión independiente reprodujo S0-2 sobre una copia sin enlaces (el código de S0-2 y, como base, el código de E0 de
    HEAD, `9f6361e`): la tanda 0, 57 de 57 archivos iguales a `salida_tanda0_r2b/`; los 152 TOs, 26 cambian y 126 salen byte a
    byte iguales a la corrida base; 9.554 unidades (base 9.385; 553 ids nuevos y 384 que desaparecen), con el conteo de los 26
    igual al del FRENO; doble corrida sin diferencias; selftest_e0 84/84, b52 39/39, b581 34/34, b582 59/59, b583 33/33;
    selftest de claves OK con el contraste en OK y salida igual a la del repo, sin mover ninguna clave de la tanda 0; las 119
    filas del catálogo limpias con el mismo detalle; 10 unidades partidas y 9 enteras con tabla serializada sobre el umbral.
    Conciliación de las unidades: 9.385 con el código de C2 (`s0_1/DISENO_S0-1.md:18`) → 9.533 con S0-1 (+423 −275) → 9.555
    con S0-1 bis (+179 −157) → 9.554 con S0-2; la diferencia de −1 con S0-1 bis son los 41 eventos de las decisiones 5 y 8
    (3 ids nuevos y 4 que desaparecen; `s0_2/censos/conciliacion_S0-1_S0-1bis_S0-2.json`).
  - Decisión 8 (páginas de índice). La regla escrita alcanzaba 4 de las 6 páginas; S0-2 admitió tres formas más (rótulo pegado
    al número, palabra partida y título antes del primer rótulo) y con ellas pasan a índice las 6 y, además, nmaeef p. 14 y
    ri2_ae p. 13 (178 renglones, 152 en las 6). La revisión leyó esas dos páginas contra el PDF: las dos son el índice del
    Anexo II (rótulos 1 a 2.8, sin texto normativo); nmaeef p. 36, que abre con una lista de rótulos y sigue con cuerpo, queda
    como cuerpo, y ceninf p. 1 también; fuera de las 8 páginas no cambia ningún rol (`s0_2/censos/censo_rol_indice.json`).
    Decisión: se aceptan las tres formas, acotadas por el censo de páginas de la regla (`s0_2/scripts/censo_rol_indice.py`):
    toda página que cambie de rol en una corrida futura es hallazgo y se reporta antes de usarse.
  - Decisión 9 (orden por celda en el catálogo de rdbcra). La revisión verificó sobre el PDF (pp. 36 a 54, `pdftotext -layout`)
    que en las 119 filas el número, la gravedad y las multas comparten renglón y que en 63 ese renglón lleva además un tramo
    de la descripción; el orden por celda partiría ese renglón, dejaría texto fuera de los renglones del PDF y el control por
    renglones (`s0_1bis/scripts/control_filas_catalogo.py`) no podría dar limpia ninguna fila. Decisión: se ratifica que no se
    adopta; la unidad de cada fila conserva el orden del PDF, con las 119 filas limpias. La lectura de cortes de S1 y la
    verificación literal del tramo de E1 necesitan renglones enteros del PDF.
  - Fila F19b de la tabla de reprocesamiento (unidad agregada o retirada por una regla de segmentación de E0, sin cambio en el
    PDF). La propuesta del FRENO la dejaba sin variación del selftest de claves; el contraste exige una por fila
    (`mantenimiento/code/selftest_clave_cache.py:1704-1705`), así que la fila cita R24 (la unidad nueva de la renumeración,
    tokens cambia/cambia), verificado con el selftest de claves sobre una copia con la fila (OK). Decisión: se suma la fila, con
    su nota por fila y la línea del contraste corregida a 42 filas (el texto decía 40 desde 53b7708 y el selftest de 0a3ac81 ya
    contaba 41), en el commit de S0-2.
  - Para S1: el código es el de S0-2, sin interruptores (`s0_2/REPORTE_S0-2.md` §7); 7 de las 8 páginas que pasaron a índice van
    a la lista del censo de renglones; el rótulo del estrato en la semilla del sorteo es el valor literal de `modo_lectura` de
    `segmentacion_84/b584_particion/conteos_b584.json` (vigente, marcadores, sin_raiz); ri_spi, con 95 unidades en S0-2, sale
    del tercer grupo y se leen 10 de sus unidades aparte.
- **07/10/2026 — resultado de S1 y de su lectura de cortes: NO llega al piso; decisiones de la autora PENDIENTES (S1 sin commit, por la
  nota del 05/10/2026: sin piso, la salida no se commitea y S2 no se despacha).** La revisión independiente del FRENO S1 (sesión de solo
  lectura; paquete `revision_USEG_OFICIAL_S1_mesa/`) reprodujo los controles (doble corrida 768 y 768 archivos, 0 distintos; tanda 0 25 de
  25 byte a byte; 9.554 unidades; sorteo recomputado igual a la muestra sellada `6ed08891…`) y leyó las 136 unidades de la muestra contra
  las páginas del PDF (son 136, no 137: 90 + 25 + 11 + 10; hallazgo de la autora). Cifra del piso: 73 de 90 sin error de corte, cota inferior
  de Wilson al 95 % **0,718** (con las 2 dudosas como error, 71 de 90, 0,694); el piso de 0,90 admite 3 errores y hubo 17, en 11 TOs. Por
  modo: vigente 39 de 40, marcadores 5 de 10, sin raíz 29 de 40. Cifra del corpus, ponderada por el peso de cada modo (0,871 / 0,025 /
  0,104): 0,937, con un intervalo aproximado [0,836; 0,978]. Mecanismos de los 17: cuerpo de punto que queda como intersticial del padre
  partido por renglón (7: ri_dcpc ×4, nmcief ×2, snp_cheq); numeración o título no leído y pegado a la unidad anterior (7: seggar, ri_tar,
  ri_sef, nmcief, ri_ccna, ri_icpipsp, nmaeef); índice del Anexo I leído como cuerpo (2: ri2_ae p. 3); primer renglón tomado como título
  (1: seguef 2.1.6). La mesa verificó siete de los 17 contra la página (uno por mecanismo; `verificacion_muestra_errores_S1_y_S0-3_mesa.md`
  en el scratchpad de la mesa): los siete coinciden. Censo de los 28 renglones sin explicación: 7 renglones de norma perdidos por la regla
  K de la zona de encabezado (fimipyme p. 4, ri_cc pp. 60 y 62) y colas de título (ri2_ci p. 5); la clase «parte de un título heredado»
  tiene 14 renglones (no 20), todos títulos de sección. Dos documentos con la raíz mal segmentada: ri_cc (tres regímenes con numeración
  que reinicia) y ri_ai (sección 2 no abierta). Glosa corregida: «35 de 35 entradas de agregados iguales» incluye 15 ausentes en los dos
  lados (sub_chunking, encabezados_conservados e ids_desambiguados).
  - El resultado no depende de la lectura de la autora: para llegar al piso habría que revertir 14 de los 17 errores. La autora propone
    leer ahora 5 o 6 casos (uno por mecanismo) y hacer la lectura completa de la nota del 05/10/2026 sobre la muestra de la corrida que
    siga a la corrección. La mesa lo considera compatible con esa nota si la lectura de hoy se asienta como lectura de calibración (fecha
    y casos) y la revisión del piso se hace entera, con otra semilla, sobre la muestra nueva.
  - Decisión PENDIENTE de la autora: volver a S0 con una etapa acotada (S0-3) antes de la tanda 1, o declarar el límite con su cifra.
    Recomendación de la mesa: S0-3 acotada (3 a 4 días de calendario, USD 0, reversible, con la tanda 0 byte a byte como control), porque
    corregir después de extraer cuesta re-extracción por unidad y re-sellado por tanda, y 7 de los 17 errores llevan texto de otro punto
    al punto equivocado. Alcance propuesto (cinco mecanismos; los dos documentos de raíz como límite declarado) y muestra nueva con otra
    semilla: en el documento de la mesa citado arriba. ri_spi (clase y vía), ri_tar p. 1 r. 10 y las vías de ri2_pm y ri_spi se deciden
    después de la corrida nueva.
  - Commit de S1 mientras tanto (propuesta): el registro de la medición (freno, manifiesto, reporte, controles, sorteo y marcas de
    lectura), no `s1/e0/` (47 MB), que la corrida siguiente reemplaza y queda en un tar.gz fuera del repo con su sha.
- **07/10/2026 — decisión de la autora: S0-3, acotada, antes de la tanda 1.** S1 no se commitea entera: se commitea el registro de la
  medición (freno, manifiesto, reporte, controles, censos, sorteo y las marcas de la lectura de cortes de la revisión, copiadas a
  `s1/lectura_cortes/`) y `s1/e0/` queda en un tar.gz fuera del repo con su sha256. S0-3 cubre cinco mecanismos (cuerpo de punto
  como intersticial del padre; numeración o título no leído; índice leído como cuerpo; primer renglón como título; la zona de
  encabezado de la regla K con los renglones perdidos y las colas de título), con censo previo por regla, los 25 archivos de la
  tanda 0 byte a byte y el selftest de claves sin mover ninguna clave de la tanda 0; después S1-bis con la lectura de cortes entera
  de la nota del 05/10/2026 sobre una muestra nueva, con otra semilla. Sobre ri_cc y ri_ai (análisis de la mesa en
  `analisis_ri_cc_ri_ai_fuera_de_la_extraccion_mesa.md`): ri_ai cae en la tanda 3 y su defecto (la línea «Sección 2.» en el 6.º
  renglón de la zona de encabezado) entra en el mecanismo 5 de S0-3; ri_cc está en el ejemplo de la tanda 1 pero su defecto es de
  sub-documento (tres regímenes con numeración que reinicia; 14 de sus 35 unidades y 63.845 de 88.994 caracteres en la parte mal
  segmentada) y la regla que lo corrige es un mecanismo nuevo, con riesgo sobre ri_tsa y ri2_pm: la mesa recomienda dejarlo fuera
  de la tanda 1 (la cuota del estrato 2 se completa con otro RI en el pre-registro), declararlo como límite de sub-documento y
  corregirlo en una S0-4 antes de la tanda 3; decisión PENDIENTE de la autora, escrita en el despacho de S0-3 como supuesto. La
  lectura de calibración de la autora (5 o 6 casos de la muestra de S1) se asienta con fecha y casos cuando ocurra.
- **07/10/2026 — revisión del FRENO S0-3 por la mesa y decisiones de la autora (S0-3 sin commit al escribir esta nota; el registro de S1 en
  `ee7c07c`).** Reproducido sobre una copia sin enlaces, con el parche aplicado solo en la copia (dos diffs sobre `26c6502`: `e0_lib.py`,
  `correr_e0.py`, `selftest_e0.py`, +483/−43, más el de interruptores; sha iguales a los del LEEME; hunk por regla: 1b en un solo hunk y las
  guardas en los declarados; dos refactorizaciones fuera de los flags, equivalentes y controladas con el prototipo sin reglas): tanda 0 **57 de
  57** byte a byte con `salida_tanda0_r2b/` y los 25 de la tanda 0 dentro de los 152 iguales; el prototipo no corre el mecanismo 4 en la tanda
  0 (`TOS_TANDA0_SIN_M4`); doble corrida de los 152, 768 y 768 archivos, 0 distintos entre sí y 0 contra la corrida de la instancia;
  conciliación propia contra S1: 9.554 → 9.409, +70 −215, 64 TOs, por TO igual al censo (ri_mmsef cambia dos avisos y un campo del nodo, no
  unidades: el freno decía «solo un aviso»); mecanismo 4 en los 152: 150 intros en 51 TOs (104 con dos puntos, 30 de un renglón, 16 de
  varios); selftests 110/110, 39/39, 34/34, 59/59, 33/33; selftest de claves OK con el JSON igual al del repo; los 17 errores de S1 antes y
  después: 12 cambian hacia la corrección (listados uno por uno) y 5 quedan con el texto igual (ri_sef S0, nmaeef 2.9, nmcief
  S3::chapeau_seccion, ri_ccna S8::cierre::parte7, ri_icpipsp S8); Wilson inferior con 5 en 90 = 0,8765 y P(≤ 3 en 90 | 5/90) = 0,2570.
  Repo sin cambios durante la verificación; 2.213 `.pyc`.
  - **Decisión: no ir a S1-bis con S0-3 solo.** Comparación de la mesa (`analisis_S0-4_vs_exclusion_parcial_mesa.md`): adelantar **S0-4**, la
    regla de sub-documento, antes de S1-bis (recomendado y preferido por la autora), con lista explícita de TOs donde corre (los del censo de
    reinicios de numeración: ri_sef, nmcief, ri_ccna, ri_icpipsp, ri_cc y los que el censo sume), ri_tsa y ri2_pm fuera por lista hasta una
    lectura propia, y los dos controles duros (tanda 0 byte a byte; selftest de claves). La alternativa (declararlos parcialmente segmentables
    y sacarlos de la tanda 1) recorta el corpus a medida del piso y saca de la tanda 1 a nmcief y ri_ccna, que tienen alcance decidido.
    nmaeef 2.9 queda como límite declarado (el inverso del mecanismo 1). El código de E0 del repo se cambia una sola vez, con S0-4 (el
    parche de S0-3 es su base). Costo: 2 días de S0-4, después S1-bis con la lectura de cortes entera y S2.
  - **Regla 1b y guardas:** tocan solo lo declarado (hunk por regla verificado). **Apartados de ri_ai S4:** fuera, para S0-4.
  - **Mecanismo 4 en la tanda 0 (lectura de la mesa sobre la muestra de 15 de los 123 intros que cambiarían; sorteo
    `S0-3:mecanismo4:muestra_mesa`; material en `trabajo54/out_mesa/mecanismo4_tanda0_cambios.md`).** Dos familias. (i) **Títulos partidos
    en dos renglones** (12 de 15: `ext::11.1.5`, `cap::2.12.10`, `ext::7.11`, `ctacte::1.3`, `ext::9.3.10`, `ext::9.3.1`, `ctacte::10.2.2`,
    `ext::10.10`, `ext::9.3.3`, `ext::11.1.3`, `ext::3.17`, `cap::5.2.3`): E0 toma el primer renglón como título y el segundo («ellas.»,
    «ques.», «previsto en la Sección 8.).») abre el intro; el mecanismo 4 antepone el rótulo al intro, que pasa a repetir el título que ya
    está en la herencia y sigue sin texto normativo propio cuando era de un renglón: **neutro**, mueve el defecto en vez de corregirlo. (ii)
    **Oración tomada como título** (3 de 15: `ext::3.17.3` «La entidad nominada deberá tomar registro…», `cap::6.9.2` «Políticas y
    procedimientos… para asegurarse de que:», `ext::5.5.1` «Incluir en las transferencias…»): el intro empezaba a mitad de la oración; el
    mecanismo 4 lo completa: **corrección real** del mismo tipo que seguef 2.1.6, aunque la etiqueta de título siga en la herencia (E1 ya
    veía la oración entera por la herencia, así que el efecto sobre la extracción es chico). Recomendación: **(a), excluir la tanda 0 del
    mecanismo 4**, como corre el prototipo: 12 de 15 cambios son neutros y los 3 reales no justifican re-extraer 738 unidades (unos USD 15 de
    E1 y E3 a la tarifa de referencia) ni un re-sellado más. Para los 152, reemplazar el mecanismo 4 por dos reglas acotadas en S0-4: (4a)
    «oración-título», que abre el intro desde el rótulo solo cuando el renglón del título es una oración (termina en «:» o lleva verbo
    deóntico), y (4b) «título envuelto», que **junta al título el renglón que lo completa** (el título no termina en punto o termina en guion
    de corte, y el renglón siguiente, en la misma columna, es corto y termina en punto) y no emite el intro vacío: así se juntan los 30
    títulos partidos de los 152 (y los 22 de la tanda 0 quedan declarados), con su censo y su caso de selftest.
  - **Mecanismo 1b:** incluir (corrige snp_cheq, 109 ids; un solo hunk). **Guardas:** se aceptan (tocan solo lo declarado). **Apartados de ri_ai
    S4:** fuera, para S0-4. La atribución por regla de los 1.206 eventos se reproduce byte a byte (cada regla sola sobre los 152: 1a −69, 1b −109, 2a +11 −3,
    2b 0, 2c +42 −25, 3 +15 −9, 4 0 ids y 762 unidades que cambian, 5a y 5b 0, 5c +2; interacción 0) y la tanda 0 da 57 de 57 con cada
    regla sola; control más fuerte que el del freno: el parche con todos los interruptores apagados deja los 768 archivos de los 152 y
    los 57 de la tanda 0 byte a byte iguales, así que las dos refactorizaciones fuera de los flags son inertes.
  - **Decisiones de la autora sobre S0-3 (07/10/2026, noche):** (1) **S0-4 antes de S1-bis**, con el diseño de la mesa: regla de
    sub-documento con lista explícita de TOs (ri_sef, nmcief, ri_ccna, ri_icpipsp y ri_cc), ri_tsa y ri2_pm fuera por lista hasta una
    lectura propia (siguen `parcial_declarado`), los dos controles duros intactos (tanda 0 byte a byte; selftest de claves sin mover ninguna
    clave de la tanda 0) y el código de E0 del repo cambiado una sola vez, en S0-4, con el parche de S0-3 como base. (2) **Mecanismo 4:**
    excluido de la tanda 0 y reemplazado en los 152 por dos reglas acotadas, «oración-título» (4a) y «título envuelto» (4b), que también
    quedan fuera de la tanda 0 por lista; los 22 títulos partidos y las 3 oraciones tomadas como título de la tanda 0 se declaran como límite.
    (3) **Regla 1b y guardas:** sí. (4) **Apartados de ri_ai S4:** a S0-4. nmaeef 2.9 queda como límite declarado. Despacho de S0-4
    preparado por la mesa (`despacho_S0-4_USEG_OFICIAL_mesa.md`), con el hash del commit de S0-3 como único hueco.
  - Commit de S0-3 PENDIENTE de la autora (registro de la etapa: parche, diseño, censos y freno); el código de E0 del repo no cambia hasta S0-4. **[Corrección del 07/10/2026, noche: commiteado en `2185807`.]**
- **07/10/2026 (noche) — FRENO S0-4a revisado por la mesa sobre una copia, y decisiones de la autora.** S0-4a no tocó el repo. Su parche,
  aplicado sobre el código de E0 de HEAD, da los tres sha256 del LEEME; el mecanismo 4 ya no está en el código.
  - **Controles duros: se reproducen.**
    - Tanda 0: 57 de 57 con la configuración final, con todo apagado y con cada una de las 14 reglas sola; los 25 de la tanda 0
      dentro de los 152, iguales.
    - Todo apagado igual a S1 (768 de 768); solo las reglas de S0-3, igual a S0-3 sin el mecanismo 4 (768 de 768); doble corrida con 0
      distintos.
    - Selftests: `selftest_e0` 134/134 y b52, b581, b582 y b583 en verde. Los dos casos corregidos (ri_spi 95 → 93 y
      `nmcief::A2::3.2.1`) son efectos reales de S0-4.
    - El selftest de claves da OK.
  - **Conciliación: se reproduce,** con un script de atribución propio.
    - 9.409 son las unidades de S0-3 sin el mecanismo 4 y 9.554 las de S0-4. Contra S0-3 hay 54 TOs y 1.095 eventos, cada uno de una
      sola regla.
    - Contra S1 hay 64 TOs y 1.530 eventos (+357 −357); volver a 9.554 es coincidencia.
    - La única interacción, `nmcief::A4::S1`, aparece solo con sd y 2a juntas.
  - **Proyección: se reproduce.** De los 17 errores del primer grupo de la lectura de cortes de S1, 16 van hacia la corrección;
    `nmaeef::2.9` no cambia. Salvedad: en ri2_ae las raíces 3 a 8 siguen rechazadas por la guarda de columna.
  - **Decisiones de la autora:**
    - (a) **La tanda 0 sigue excluida de 4a y 4b.** Cifra a declarar: 123 puntos (la familia del mecanismo 4), de los que 4a y 4b
      tocarían 114 (53 por 4a, 61 por 4b, 22 de ellos retirando la intro) y 9 no tienen regla.
      - Precisión de la mesa: la muestra de 15 de S0-3 (12 sin efecto en el contenido, 3 correcciones chicas) no representa las
        proporciones del censo (12 de 15 en 4b contra 61 de 123; hipergeométrica P = 0,011).
      - Por eso «3 correcciones chicas» no se extrapola: la clase 4a tiene 53 puntos y mezcla oraciones con títulos de tres renglones.
      - El «22 + 3» mezclaba un censo (las intros de un renglón) con un conteo de la muestra.
    - (b) **Formulario, circular y sdg3, aceptados** (decisiones 1 y 2 del diseño, §8). Cada una tiene su caso sintético y su caso
      medido, con los eventos esperados:
      - formulario: 6 límites y 42 unidades nuevas en ri_ccna;
      - circular: 3 límites y 14 unidades en ri_icpipsp;
      - sdg3: 1 evento, `nmcief::A1P2::S4`.
    - (e) **El orden:** la reversión de O5 va antes de S0-4b, para que el selftest de claves corra contra el JSON vigente. Hecha por la
      mesa; el commit está PENDIENTE de la autora.
  - **Respuestas de la mesa, para decidir:**
    - (c) **ri_ccna, ítems 31 a 40.**
      - Los rechaza la guarda `raiz_mayor_a_max` (`MAX_RAIZ = 30`, `e0_lib.py:1853`).
      - Un prototipo que acepta, dentro de un sub-documento, solo la raíz que sucede exactamente a la anterior deja 10 unidades más en
        ri_ccna (149 → 159) y no cambia nada en los otros cuatro TOs de la lista; los códigos 101 a 126 de ri_sef no son sucesores.
      - Recomendación: corregirlo en una S0-4a-bis antes de S0-4b, porque el código se cambia una sola vez y ri_ccna está en la tanda 1.
      - B.1 y B.2, y A.3, quedan como límite declarado: 2 unidades y 12 de los 40 ítems de la lista B con el id de otro ítem.
      - La unidad de 57.922 caracteres de ri_cc (`ri_cc::RIP::S0`) está declarada sin partir (tabla serializada) y queda fuera de la
        tanda 1: va a la vía de página con la tanda 3. No bloquea S0-4b.
      - Para la condición 12 de la tanda 1 sí entran `nmcief::A6::S0` (23.071), `manori::1.5.1` (15.949) y `ri_oc::3.51` (19.239). En
        los 152, las unidades de más de 13.944 caracteres pasan de 34 a 29.
    - (d) **Los 35 TOs fuera de la lista** con límites de sub-documento (87 límites; censo igual al del FRENO): 6 de la tanda 1, 6 sin
      tanda (que el criterio del protocolo pone en la 2), 18 sin tanda (criterio: tanda 3) y 5 fuera.
      - Los de la tanda 1 son manori, ri_gerc, ri_oc, ri_pgn, ri_rml y snp_tr. Solo **ri_oc** pide atención antes de S1-bis:
        `ri_oc::3.51` (pp. 15-25) se lleva los Anexos I y II y el Apartado B, que es texto de otro punto.
      - Sumarlo a la lista separaría los anexos pero no el Apartado B, y el régimen de la página 1 prefijaría todos los ids; haría falta
        una guarda.
      - Recomendación: medirlo en S0-4a-bis como variante sin aplicar, y decidir con la cifra; si no, límite declarado y condición 12.
      - Los otros cinco de la tanda 1 no requieren acción por esta regla.
  - **Siguen PENDIENTES del diseño §8:** la 3 (un rótulo sin numeración que reinicia abre su sub-documento), la 4 (la lista de verbos de
    4a y 4b, con debe(n), puede(n), será(n) y tendrá(n)) y la 5 (los casos del §7 dentro de los sub-documentos: límite declarado u otra
    regla).
    - Recomendación de la mesa: la 3 y la 4 como están diseñadas, porque los controles duros pasan con ellas y 4a y 4b no tocan la
      tanda 0; la 5 como límite declarado, salvo ri_ccna 31 a 40 (S0-4a-bis).
  - **Discrepancias menores con el FRENO:** ri_mmsef cambia 3 avisos y un campo de la estructura, sin unidades (no «un aviso»); ri_tsa
    figura en el manifiesto de S1 como `reconocido_pleno`, no `parcial_declarado`.
  - **«Seguí»** preparado por la mesa: S0-4a-bis y después S0-4b, en el paquete de la mesa (`segui_S0-4a-bis_y_S0-4b_USEG_OFICIAL_mesa.md`).
- **08/10/2026 — FRENO S0-4a-bis revisado por la mesa sobre una copia, y decisiones de la autora.**
  - **Revisión de la mesa.** S0-4a-bis corrió sobre una copia, sin tocar el repo (parche sobre `26c6502`, el código de E0 de HEAD). La mesa
    lo reprodujo en una copia propia sin enlaces, sin API; repo sin cambios fuera de `docs/` y 2.213 `.pyc`. Se reproduce todo:
    - el parche final por los dos caminos: `e0_lib.py` `7e56f857…`, `correr_e0.py` `2559b6c2…`, `selftest_e0.py` `a776126d…`; contra el de
      S0-4a cambia solo la regla sdmax (interruptor en `REGLAS_S0_4`, `correr_e0.py:128`; `e0_lib.py:1387`, `:1738-1742` y `:1784-1787`);
    - sdmax: ri_ccna de 149 a 159 unidades, 11 eventos (`D1A3::S30` de 2.285 a 350 caracteres; `S31` a `S40` nuevas); los otros cuatro TOs
      de la lista sin cambios; los 24 códigos del Anexo II de ri_sef siguen rechazados; en los 152, de 9.554 a 9.564 unidades;
    - los controles duros, con la regla prendida y apagada: tanda 0 57 de 57 (también con el script secuencial); regla apagada = S0-4a y
      todo apagado = S1, 768 de 768 (y contra `s1/manifest_salida.json`); doble corrida con 0 distintos; selftest de claves con VEREDICTO OK
      y salida igual a `923dd900…`; `selftest_e0` 137/137, b52 39/39, b581 34/34, b582 59/59, b583 33/33;
    - la conciliación: contra S0-4a, 1 TO y 11 eventos, todos de sdmax; contra S1, 1.540 = 1.530 + 10, con `nmcief::A4::S1` como única
      interacción;
    - las anclas de F19b: `correr_e0.py:95-100` no se mueve, `:327-339 → :353-365`, `:576-585 → :602-611`, `:1266 → :1295`;
      `e0_lib.py:352 → :360`, `:473 → :552`;
    - ri_oc, medido sin aplicar: de 128 a 133 unidades, 12 eventos; `ri_oc::3.51` de 19.239 a 12.206 caracteres, con el Apartado B en
      11.427 de ellos; 5 unidades nuevas y 3 renombres; las unidades de más de 13.944 caracteres (16.384 / 1,175, `:86`) pasan de 29 a 28;
      la guarda no toca a los cinco TOs de la lista;
    - los 53 puntos 4a de la tanda 0: 53 de 53 con la oración entera en la herencia de sus 249 unidades hijas; control negativo 52/1;
    - las dos correcciones a S0-4a: ri_tsa es `reconocido_pleno` (`s1/controles_S1.json`); ri_mmsef cambia 3 avisos y, con precisión, el
      `text_col` del nodo 2.2 (de null a 76,6), no «un aviso».
  - **Decisiones de la autora (08/10/2026):**
    1. **(a) ri_oc: se aplica la variante**, porque ri_oc está en la tanda 1 y la variante saca los anexos de `ri_oc::3.51`, que baja de
       19.239 a 12.206 caracteres, por debajo del umbral de unidades grandes. La guarda es código nuevo: corre su vuelta de controles sobre
       una copia, con la misma batería, antes de S0-4b. El Apartado B, que queda dentro de 3.51, es límite declarado.
    2. **(b) ri_ccna no se declara: se corrige en la misma vuelta**, antes de S0-4b. Las 47 unidades de B.3 a B.40 heredan «B. PRUEBAS
       SUSTANTIVAS», y `D1A3::S2` se separa en A.3, B.1 y B.2, cada cosa con su caso de selftest y su atribución sola. Si alguna no se puede
       corregir sin mover otros TOs, la vuelta lo reporta con su cifra y la autora la declara. Reemplaza a la decisión 5 del §8 de S0-4a para
       lo que quedaba de ri_ccna. Prototipo de la mesa sobre una copia: un sub-documento de «letra», por lista, corrige la herencia de las
       47 y separa B.1 y B.2 sin mover nada fuera de ri_ccna en los cinco TOs de la lista (159 → 163 unidades); A.3 sigue pegado a A.2.2 y
       pide otra pieza; sin lista, la misma forma tocaría manori y ri_dsf.
    3. **(c) La tanda 0 queda excluida de 4a y 4b**, declarada con lo que midió esta etapa: 123 puntos; 53 de la clase 4a, en los que la
       oración llega entera por la herencia de las unidades hijas, así que E1 la veía; 61 de la 4b, cosméticos; 9 sin regla.
    4. **(d) Sí a la nota fechada** con las dos correcciones a S0-4a, que S0-4b agrega al copiar el diseño de S0-4a al repo.
    5. **(e)** La mesa prepara el despacho de la vuelta (S0-4a-ter: la guarda de ri_oc y las dos reglas de ri_ccna, con la batería entera)
       y pone al día la parte 2 del «seguí» (S0-4b) con sdmax, ri_oc, ri_ccna y el parche final de la vuelta.
  - **Ruta:** S0-4a-ter → S0-4b → S1-bis → S2. Suma una vuelta (del orden de un día) a la cadena de segmentación, que sigue siendo la crítica.
- **08/10/2026 (tarde) — decisiones de la autora: el diseño de S0-4, la vuelta S0-4a-ter y los límites de E0 del barrido.**
  1. **Decisiones 3, 4 y 5 del §8 del diseño de S0-4a**, que la autora dio a la instancia en el «seguí» de S0-4a-bis: la 3 (el rótulo sin
     numeración que reinicia abre su sub-documento igual) y la 4 (la lista de verbos de 4a y 4b: la del despacho más debe(n), puede(n),
     será(n), tendrá(n)), como están diseñadas; la 5, los casos del §7 dentro de los sub-documentos, como límite declarado, salvo ri_ccna,
     que se corrige en S0-4a-bis (ítems 31 a 40) y en S0-4a-ter (B.3 a B.40 y `D1A3::S2`).
  2. **S0-4a-ter, despachada el 08/10/2026** en la sesión de S0-4 (la guarda de ri_oc y las dos reglas de ri_ccna), con un agregado de
     la autora: en la misma vuelta se evalúa el Apartado B de `ri_oc::3.51` (11.427 de sus 12.206 caracteres) y se separa solo si se puede
     con una forma acotada a ri_oc, con su interruptor, su caso de selftest y la misma batería, sin mover otros TOs. Si no entra, queda
     declarado con su cifra en el pre-registro de la tanda 1 (E0-04 del barrido).
  3. **Los límites de sub-documento del censo de S0-4a** (87 en 35 TOs; E0-05 del barrido; cifra del censo de S0-4a, que entra al repo
     con S0-4b): los de las tandas 2 y 3 (19 en 6 TOs y 37 en 18 TOs, por el criterio de tandas del protocolo, `docs/protocolo_entre_tandas.md:175-182`)
     pasan a una **release de E0 antes de la tanda 2**, sin re-extraer (un TO que todavía no se extrajo no paga nada; protocolo, §3); los de
     los 6 TOs de la tanda 1 (17: manori 8, ri_oc 3, ri_rml 3, ri_gerc 1, ri_pgn 1, snp_tr 1) quedan declarados, salvo lo que corrija
     S0-4a-ter en ri_oc. Son detecciones, no lecturas, con falsos positivos conocidos.
  4. **El hallazgo 1.16** (E0-06; 118 candidatos en 55 TOs en el censo de S1, `s1/censo_renglones_S1.json`): S1-bis lo mide en su muestra
     y S2 propone la regla; si es acotada y de bajo riesgo, entra en la release de E0 antes de la tanda en la que cae. En la tanda 1 hay
     **33 candidatos en 10 TOs** (depaho 8, lingeef 8, ayccef 5, cajasc 4, adrei 2, manori 2, cirmo3 1, efemin 1, ri_rml 1, snp_tr 1;
     iguales con S0-4a-bis). El resto: tanda 0, 11 en 3 TOs; tanda 2, 68 en 37; tanda 3, 5 en 4; fuera, 1 (ri_spi).
  5. **`nmaeef::2.9` (E0-02, tanda 2) y la «Sección 1.» de ri_niif (E0-03, tanda 3):** grupo 2, por lista, en la release de E0 antes de la
     tanda 2. `nmaeef::2.9` es además uno de los 118 candidatos del hallazgo 1.16, y el único leído como error.
  - **Precisión:** no hay un archivo con la asignación de las tandas 2 y 3; las cifras por tanda de los puntos 3 y 4 salen del criterio
    del protocolo, que reproduce el reparto 6 / 6 / 18 / 5 de la nota del 07/10/2026 (cálculo de la mesa del 08/10/2026).
