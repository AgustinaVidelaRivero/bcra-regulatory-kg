BORRADOR — PENDIENTE DE FIRMA

MANDATO — U-SEG-OFICIAL: SEGMENTACIÓN OFICIAL CON e0-r2 DE LOS 152 TOs DEL UNIVERSO, VERSIONADA CON SU MANIFIESTO.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad en TRES ETAPAS con FRENO obligatorio al final de cada una: S0 (correcciones de E0 que cambian
  ids de la partición, y la E0 de ri_spi), S1 (manifiesto y corrida) y S2 (diferencias contra la
  partición y cifras para la tesis). Reporte corto (no más de 40 líneas) y espera del «seguí» escrito de
  la autora.
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa.
- PRECONDICIÓN: el cierre de U-R2-CODIGO-2 commiteado por la autora. Sus puntos (f), (h) y (l) cambian
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
Salen de la revisión independiente (reports/u_revision_libre/freno_b1.md) y de las enmiendas del
04/10/2026 a las adendas del laudo B5.5. No se ven en la tanda 0 y no entran a C2 de U-R2-CODIGO-2.
1. Sección escrita de otra forma (1.14): opecam («Seccón 3.»), garopt y snp_dd.
2. Rótulos de punto que no lo son (1.15): rdbcra, ri_niif, ri_tsa y ri_dsf.
3. Páginas de norma fuera de toda unidad (2.4): ri_cc, ri_tsa, snp_mep, venliq y fimipyme.
4. E0 de ri_spi: regla de marcador de letra y número («APARTADO A», «A.1.», «A.1.1.»). Hoy queda en una
   unidad de 18.565 caracteres. Es la unidad de E0 de ri_spi que piden las enmiendas.
Primero el diseño, sin implementar: cada regla con su censo sobre los 152 TOs (qué TOs y qué ids cambian).
FRENO S0-1. Después del «seguí», la implementación, solo en e0-r2. Controles:
- la E0 de la tanda 0 que dejó U-R2-CODIGO-2 (`salida_tanda0_r2b/`) no cambia un byte;
- cada id que cambia en la partición queda atribuido a una de las cuatro reglas, por TO; lo que ninguna
  explique es «otra» y se lee;
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
   (L), unidades sin partir por tabla, ids de K, lo que cambien los puntos (f), (h) y (l) de
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
