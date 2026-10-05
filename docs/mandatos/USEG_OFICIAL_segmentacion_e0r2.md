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
