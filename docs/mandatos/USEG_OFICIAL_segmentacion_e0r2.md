BORRADOR — PENDIENTE DE FIRMA

MANDATO — U-SEG-OFICIAL: SEGMENTACIÓN OFICIAL CON e0-r2 DE LOS 152 TOs DEL UNIVERSO, VERSIONADA CON SU MANIFIESTO.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad en TRES ETAPAS con FRENO obligatorio al final de cada una: S0 (correcciones de E0 que cambian
  ids de la partición, y la E0 de ri_spi), S1 (manifiesto y corrida) y S2 (diferencias contra la
  partición y cifras para la tesis). Reporte corto (no más de 40 líneas) y espera del «seguí» escrito de
  la autora.
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa.
- PRECONDICIÓN: el cierre de U-R2-CODIGO-2 commiteado por la autora. Sus puntos (f), (h), (l) y (n) cambian
  e0-r2 (docs/mandatos/UR2CODIGO2_correcciones_previas_a_reext.md). S0 edita E0 sobre ese commit, y S1
  corre con el código que deje S0 y lo registra. Si el cierre no está commiteado, frená sin escribir.

CONTEXTO, con sus anclas.
- La partición vigente (data/experiment/segmentacion_84/b584_particion/) la produjo el código de B5.8.4,
  no `correr_e0.py` (docs/checklist_pre_escalado.md:85). `particion_152.json`, clave `agregados`: 138
  reconocidos plenos (4.183 páginas, 9.266 unidades), 2 parciales (2.413 páginas, 46 unidades) y 12 no
  segmentables (161 páginas, 12 unidades); 9.324 unidades en total. Modo de lectura en
  `conteos_b584.json`: 91 vigente, 5 con marcadores y 56 sin raíz.
- El checklist `:85` pide regenerarla antes de la tanda 1 con `correr_e0.py --version-e0 e0-r2`, con la
  regla L y la escalera, con el código de `e1c9456` o posterior. Con el punto (f) de U-R2-CODIGO-2, la
  versión que corresponde es la e0-r2 del cierre de esa unidad.
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
   - Riesgo, con la salida medida en la tanda 0 con el prefijo sellado (0,86 tokens por carácter de texto
     propio en la mediana de las unidades de 3.000 caracteres o más, y 1,12 en el percentil 90): el reintento
     alcanza hasta unos 19.000 caracteres con la mediana y 14.600 con el percentil 90.
     - Clase A, 8 unidades: no se pueden partir y pasan de 19.000. Terminarían sin extracción, con error
       declarado: `cateloc::S2`, `snp_mep::S7`, `manori::S2`, `ri_laft::3.7`, `manori::S4`, `ri_niif::3.2`,
       `seggar::8.2` y `ri_oc::3.51`.
     - Clase B, 12 unidades: se parten, pero su parte mayor pasa de 19.000 y no se vuelve a partir.
     - Clase C, 8 unidades: entre 14.600 y 19.000, en el borde.
     - Clase D, 29 unidades: entran en el reintento.
     La capacidad se recalcula con los tokens de salida por carácter que mida U-REEXT-T0 con el prefijo r2b.
   El diseño decide, con su censo de ids por TO:
   a. Ninguna unidad se saltea sin declararla: los cinco mini-chunks que hoy E0 saltea en silencio pasan a
      declarados, y la partición por tamaño dice si los alcanza.
   b. Ninguna unidad de la tanda 0 cambia, `cap::4.2.1.2` incluida (26.726 caracteres en e0-r2, declarada
      por tabla serializada). Si un arreglo la tocara, se declara y lo decide la autora.
   c. Para las 8 unidades de la clase A, S0 propone una solución (una regla por párrafo o por página, u
      otra) o las declara como límite con su cifra.
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
   byte a byte la e0-r2 de la tanda 0 que deje U-R2-CODIGO-2; los cinco de desarrollo no son de la
   partición y no entran.
5. Censo de vigencia. Por cada uno de los 152 TOs, las marcas de su carátula y de su título en el índice
   («Derogado», «Vigente hasta», «vigente al»), con la página y la línea. El manifiesto declara qué TOs
   son vigentes. Casos ya conocidos: `manual` («Vigente hasta el 31/12/2017») y ri_ao («RI Derogado por
   la Com. A 8262»). Una marca nueva es hallazgo y se reporta; la decisión es de la autora.
6. Herencia por unidad. La herencia máxima por unidad y la lista de las unidades que superen el umbral
   que fije el punto (h) de U-R2-CODIGO-2 (referencia: 13.091 caracteres), con su TO, su texto propio y
   el bloque heredado mayor. Sobre la partición de B5.8.4 eran 95 unidades de 11 TOs.
FRENO S1.

S2. DIFERENCIAS CONTRA LA PARTICIÓN Y CIFRAS.
1. Diferencias contra `b584_particion/`, atribuidas por clase como en el control de R5: ids desambiguados
   (L), unidades sin partir por tabla, ids de K, lo que cambien los puntos (f), (h), (l) y (n) de
   U-R2-CODIGO-2 y lo que cambie S0; texto distinto por tablas, pies, K y arrastre. Lo que ninguna clase explique se lista como «otra». Criterio
   de aceptación: «otra» en 0, o cada caso leído y explicado.
2. Diferencias contra la escalera de R5, si la corrida de R5 se puede reproducir con `e1c9456`: solo las
   que explican K-a′+K-b y el punto (f).
3. Cifras que la tesis va a citar, cada una con el archivo, la clave y el comando que la reproduce:
   - TOs por vía y por modo de lectura; páginas y unidades por clase;
   - unidades totales, chunks terminales y mini-chunks; unidades partidas por tamaño;
   - tablas detectadas y unidades con tabla serializada;
   - ids desambiguados y chunks de índice que quedan, por TO;
   - encabezados conservados por K, por TO;
   - los 12 no segmentables y los 2 parciales, con sus páginas.
   Van a `cifras_segmentacion_oficial.md` en la carpeta de la salida. Es el artefacto que lee la
   verificación de las marcas [AL CIERRE: e0-r2] de la sección 4.1 (docs/insumos_escritura.md, §6).
FRENO S2, final.

ESCRITURAS: data/experiment/segmentacion_oficial_e0r2/ y el scratchpad. En S0, además:
data/experiment/reextraccion_v2/e0_chunking/e0_lib.py y correr_e0.py, solo en la versión e0-r2, y sus
selftests. Si hace falta un script de comparación, va en la carpeta de la salida;
`r5_escalera_particion.py` se usa sin editar.
PROHIBIDO: editar `b584_particion/`, las salidas selladas de E0 y la E0 de la tanda 0; cambiar la versión
legada de E0; tocar `.gitignore`; commitear. En S1 y S2 el código de E0 no se edita: si un control falla
por el código, se reporta y no se corrige ahí.

DECISIONES DE LA AUTORA AL FIRMAR.
1. La carpeta de la salida (propuesta: data/experiment/segmentacion_oficial_e0r2/).
2. Si el manifiesto incluye a los 14 fuera de las tandas con su vía declarada (propuesta: sí, para que
   el artefacto cubra los 152), sujeto a la decisión sobre los no segmentables.
3. Si la salida se commitea entera o solo el manifiesto con los sha256 (tamaño a reportar en S1).

REQUISITOS: los de CLAUDE.md §4 (a a l), con PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; sha256 de los
archivos del repo antes y después de cada corrida; todo conteo recomputado contra su artefacto; cero
nombres de personas.
