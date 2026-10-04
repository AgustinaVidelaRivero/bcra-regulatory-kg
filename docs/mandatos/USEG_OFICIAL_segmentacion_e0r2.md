BORRADOR — PENDIENTE DE FIRMA

MANDATO — U-SEG-OFICIAL: SEGMENTACIÓN OFICIAL CON e0-r2 DE LOS 152 TOs DEL UNIVERSO, VERSIONADA CON SU MANIFIESTO.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad chica, en DOS ETAPAS con FRENO obligatorio al final de cada una: S1 (manifiesto y corrida) y S2
  (diferencias contra la partición y cifras para la tesis). Reporte corto (no más de 40 líneas) y espera
  del «seguí» escrito de la autora.
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa.
- PRECONDICIÓN: el cierre de U-R2-CODIGO-2 commiteado por la autora. Su punto (f) cambia e0-r2
  (docs/mandatos/UR2CODIGO2_correcciones_previas_a_reext.md). La unidad corre con el código de ese commit
  y lo registra. Si el cierre no está commiteado, frená sin correr.

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
FRENO S1.

S2. DIFERENCIAS CONTRA LA PARTICIÓN Y CIFRAS.
1. Diferencias contra `b584_particion/`, atribuidas por clase como en el control de R5: ids desambiguados
   (L), unidades sin partir por tabla, ids de K, y lo que cambie el punto (f) de U-R2-CODIGO-2; texto
   distinto por tablas, pies, K y arrastre. Lo que ninguna clase explique se lista como «otra». Criterio
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

ESCRITURAS: data/experiment/segmentacion_oficial_e0r2/ y el scratchpad. Si hace falta un script de
comparación, va en esa carpeta; `r5_escalera_particion.py` se usa sin editar.
PROHIBIDO: editar e0_chunking/, `b584_particion/`, las salidas selladas de E0 y la E0 de la tanda 0;
tocar `.gitignore`; commitear. Si un control falla por el código de E0, se reporta y no se corrige acá.

DECISIONES DE LA AUTORA AL FIRMAR.
1. La carpeta de la salida (propuesta: data/experiment/segmentacion_oficial_e0r2/).
2. Si el manifiesto incluye a los 14 fuera de las tandas con su vía declarada (propuesta: sí, para que
   el artefacto cubra los 152), sujeto a la decisión sobre los no segmentables.
3. Si la salida se commitea entera o solo el manifiesto con los sha256 (tamaño a reportar en S1).

REQUISITOS: los de CLAUDE.md §4 (a a l), con PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; sha256 de los
archivos del repo antes y después de cada corrida; todo conteo recomputado contra su artefacto; cero
nombres de personas.
