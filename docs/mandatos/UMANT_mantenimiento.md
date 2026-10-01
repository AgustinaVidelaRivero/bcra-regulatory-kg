FIRMADO por la autora — 2026-10-01

MANDATO — U-MANT: MANTENIMIENTO DEL RECURSO (QUÉ OBLIGA A REPROCESAR, EMPALME DE UN SUBGRAFO Y
CONTROL DEL SITIO DEL BCRA CON AVISO).
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad en TRES ETAPAS, con FRENO obligatorio al final de cada una: reporte corto (no más de
  40 líneas) y espera de la revisión y del «seguí» escrito de la autora. Ninguna etapa arranca
  sin él.
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa.
- M1 y M2 no acceden a la red. M3 hace pedidos al sitio público del BCRA, solo con el ok
  escrito de la autora al cierre de M2.

CONTEXTO. Plan, fila B2.11, unidad 12 (docs/plan_tesis.md:401); checklist P17 (:99); tablero
de correcciones, tabla «Requisitos de mantenimiento» (las dos filas de U-MANT).
- Por decisión de la autora del 30/09, la actualización y el mantenimiento son obligatorios en
  la tesis y en el repo (plan, D-i, :1006). Los cubren esta unidad y U-SUBGRAFO (unidad 13);
  la sección de la tesis la escribe la mesa de escritura con estos insumos (C1.11).
- U-JOB-ACT (cerrada, `9278923`; plan, :1102) construyó y corrió el job de actualización: 157
  de 157 TOs verificados el 2026-09-07, y tres de los cinco TOs del conjunto de desarrollo
  cambiaron en la fuente.
  - Su mandato excluía avisos y monitoreo (cota (a)). El 30/09 la autora revocó la exclusión
    de avisos: el control de los supuestos del sitio y el aviso ante cambios son requisito.
  - La regla dura (1) sigue rigiendo: el inventario sellado es de solo lectura.
- La unidad no depende de L-ESQ-R2 y corre en paralelo con el resto del ciclo (plan, :401).

Leé completos, antes de escribir una línea:
- la fila U-JOB-ACT del plan (:1102-1170), con la revocación del 30/09, y la decisión D-i
  (:1006);
- data/experiment/job_actualizacion/diseno_job_actualizacion.md:
  - §1, la cuenta del alcance: 103 + 55 = 158 entradas, una duplicada, 157 únicas;
  - §2.a.1, el endpoint del índice y las cuatro claves de cada entrada;
  - §6, cortesía y robustez con el sitio;
  - §2.a.6, periodicidad;
- data/experiment/job_actualizacion/code/lib_job.py:
  - `RE_PORTADA` (:64-66), `RE_TEXTO_ORDENADO` (:67-68), `RE_PIE` (:69-71) y
    `RE_PORTADA_PRESENTE` (:72-73);
  - la cobertura medida que declara el comentario de :62-63 (153 de 157 en
    sonda_procedencia.json);
- la corrida del 2026-09-07 en data/experiment/job_actualizacion/corridas/2026-09-07/
  (indice_crudo.json, reporte.md, verificacion_corrida.json, tabla_deltas.json);
- los marcadores de página de E0: data/experiment/reextraccion_v2/e0_chunking/e0_lib.py,
  `RE_PIE` (:224-229);
- la clave de caché: data/experiment/evaluacion/llm_cache.py (`canonical_request` y
  `compute_key`, :111-126); el laudo de r2, §3.2 (docs/laudo_release_r2_pipeline.md); y
  docs/decisiones_caching_extraccion.md, cuyas cinco decisiones son vinculantes;
- el armado del request de E1: data/experiment/b54_catalogo_v3/code/prompt_v3_b54.py
  (`build_request_kwargs_v3`, :524);
- el precedente de empalme: la re-extracción dirigida de tres unidades de cap
  (data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/reextraccion_dirigida.json)
  y los ensamblados sellados desde salida_dirigida/ (`1b8916c`);
- los principios 9 (:277) y 12 (:299) del plan;
- para la tercera fuente del empalme (M2, punto e):
  - data/raw/manifiesto.csv, filas `comunicacion_A` (1.666);
  - los PDFs locales de data/raw/02_comunicaciones_A/;
  - data/experiment/escalado_prep/inventario_tos.csv;
  - la partición de data/experiment/segmentacion_84/b584_particion/.

DECISIONES YA TOMADAS. No se re-deciden.
1. El control de los supuestos del sitio y el aviso ante cambios son requisito (revocación del
   30/09, fila U-JOB-ACT).
2. El inventario sellado es de solo lectura. El control compara y avisa; nunca reescribe
   inventarios, manifiestos ni PDFs congelados.
3. El corpus no se actualiza. Toda actualización es una release declarada, con laudo de la
   autora (principio 9).
4. La re-extracción del subgrafo afectado y su costo son de U-SUBGRAFO. Esta unidad escribe el
   procedimiento de empalme y lo demuestra en seco, sin llamar a la API.
5. El aviso es una salida del control: código de salida distinto de cero y un archivo
   `aviso.md` al frente de la corrida, con cada supuesto roto, su valor de línea de base y el
   valor observado (confirmado por la autora el 01/10). El disparo periódico no está decidido:
   M2 lo propone (punto f) y la autora lo decide en el freno de M2.

M1 — Tabla de qué obliga a reprocesar todo y qué no. USD 0, sin red.
a. Para cada tipo de cambio, en qué paso del pipeline entra y qué obliga a recomputar:
   - texto de un chunk en E0;
   - prefijo de E1;
   - tool schema de E1;
   - modelo o parámetros del request;
   - prompt de E3;
   - catálogo de sujetos: en el bloque del prompt o solo en el JSON;
   - validador y política por campo;
   - E2 y ensamblado;
   - E4 y esqueleto;
   - un TO nuevo;
   - un TO modificado en el sitio;
   - un chunk agregado o retirado por un cambio de numeración.

   Cada cambio cae en una de cuatro clases: nada, solo código sobre lo guardado, E1 y E3 de los
   chunks afectados, o todo. Cada fila lleva el principio que la rige (9 o 12) y la ancla de
   código.
b. Verificación contra la clave de caché, sin llamar a la API, con un selftest nuevo
   (data/experiment/mantenimiento/code/selftest_clave_cache.py):
   - sobre una muestra fija de chunks de la tanda 0, arma el request de E1 con
     `build_request_kwargs_v3` y calcula la clave con `compute_key`;
   - varía una entrada por vez (texto del chunk, prefijo, tool schema, parámetro del request,
     un cambio de solo código) y registra si la clave cambia;
   - lo mismo para E3 con su propio armado de request, si está en el repo; si no está, NO
     ENCONTRADO.

   La tabla de (a) y el selftest tienen que coincidir fila por fila. Una discrepancia es FRENO.
c. Salida: data/experiment/mantenimiento/tabla_reprocesamiento.md, con la tabla, el selftest y
   su comando, y un costo de referencia por clase con su ancla (por ejemplo, E1 a E3 de los
   diez TOs costó USD 40,35, ESTADO 28/09).
FRENO M1:
- la tabla;
- el resultado del selftest, fila por fila;
- el sha256 de lo escrito.

M2 — Control de los supuestos del sitio, y procedimiento de empalme. USD 0, sin red.
a. Declaración de los supuestos, cada uno con su fuente, su valor de línea de base, cómo se
   mide y qué dispara el aviso:
   - endpoint del índice y sus cuatro claves (`titulo`, `titulo_truncado`, `archivo`, `url`);
   - cantidad de entradas y de TOs únicos (158 y 157);
   - patrones de URL de los PDFs;
   - acierto de las regex de portada y pie de lib_job.py sobre los PDFs;
   - acierto de los marcadores de página de E0 (`RE_PIE` de e0_lib.py) sobre los PDFs.
b. Línea de base, medida sobre los artefactos guardados: el índice crudo congelado y el de la
   corrida del 2026-09-07, y los PDFs en disco. data/experiment/mantenimiento/control_sitio/
   linea_base.json, con doble corrida byte a byte idéntica.
c. Script de control, data/experiment/mantenimiento/control_sitio/control_sitio.py:
   - recibe un índice y un conjunto de PDFs y los compara contra la línea de base;
   - escribe `aviso.md` y sale con código distinto de cero si algún supuesto se rompe;
   - con los artefactos de la línea de base, sale 0 y sin aviso.
d. Selftest con alteraciones simuladas sobre copias en el scratchpad: una clave faltante, una
   entrada menos, una URL con otro patrón, un PDF sin portada y un PDF sin marcadores de
   página. Cada alteración tiene que disparar su aviso, y solo el suyo.
e. Procedimiento de empalme de un subgrafo re-extraído:
   data/experiment/mantenimiento/procedimiento_empalme.md. Cubre:
   - cómo se identifican las unidades cambiadas, con tres fuentes:
     - el sha del PDF y el diff por página del job, que localiza pero no compara el sentido
       (plan, fila U-JOB-ACT);
     - la tabla de origen de las disposiciones. La tienen 90 de 152 TOs
       (reports/u_insumos_cap/estadisticas_corpus.md:222, regla R14, `ded3494`);
     - las Comunicaciones nuevas que citan el punto que modifican. Ejemplo: la Comunicación
       «A» 8432 del 30/04/2026, página 1, dice «1. Sustituir el punto 1.3. del texto ordenado
       sobre Proveedores de Servicios de Pago por el siguiente:». Datos:
       - el PDF está en data/raw/02_comunicaciones_A/A8432_2026_ano_de_la_grandeza_argent.pdf
         (sha256 `bb1d079e…`, 6 páginas) y su fila en data/raw/manifiesto.csv:1701;
       - en la página 4 la misma Comunicación sustituye el punto 2.5;
       - ese TO es `snp_psp` en la partición (escalado_prep/inventario_tos.csv:71), y su
         punto 1.3 tiene 5 unidades de E0 (`snp_psp::1.3.1.1` a `snp_psp::1.3.2.2`,
         segmentacion_84/b584_particion/snp_psp/chunks_snp_psp.json).

       **Medición de la tercera fuente, USD 0 y sin red,** sobre las Comunicaciones «A»
       guardadas en data/raw: 1.666 PDFs, fila `comunicacion_A` de manifiesto.csv. Los PDFs son
       locales y no se versionan (.gitignore:33), así que la medición registra el sha256 de
       cada PDF que lee. Pasos, en este orden:
       1. **Ventana declarada antes de medir.** Por defecto, las Comunicaciones con
          `fecha_documento` en los doce meses previos a la última de manifiesto.csv
          (2026-05-08).
       2. **Regex declarada antes de aplicarse,** con las fórmulas «Sustituir el punto»,
          «Sustitúyese», «Incorpórase» y «Déjase sin efecto», y sus formas en plural. Las
          fórmulas que aparezcan después se reportan aparte y no se suman.
       3. **Conteo:** cuántas Comunicaciones de la ventana tienen al menos una fórmula, cuántas
          citas hay y cuántas nombran un punto y un texto ordenado.
       4. **Mapeo de cada cita:** del nombre del texto ordenado al TO (inventario_tos.csv,
          `titulo_oficial`), y del punto a sus unidades en la partición
          (segmentacion_84/b584_particion/<to>/chunks_<to>.json). Cada cita cae en una de
          tres categorías: mapeada a TO y unidades, mapeada solo a TO, o no mapeable (con el
          motivo).
       5. **Caso de control:** la «A» 8432, página 1 → `snp_psp`, punto 1.3, 5 unidades.

       Script data/experiment/mantenimiento/code/medir_citas_comunicaciones.py, con doble
       corrida byte a byte idéntica. Lo que la medición no pueda decidir se marca NO DECIDIBLE,
       sin forzar el mapeo;
   - qué hace el procedimiento con los 62 de 152 TOs sin tabla de origen: con qué fuentes
     localiza las unidades cambiadas y, si ninguna alcanza, qué re-extrae (por ejemplo, el TO
     entero), con su costo por clase según la tabla de M1;
   - qué se re-extrae;
   - cómo se sustituyen las salidas de esas unidades;
   - qué se re-ensambla;
   - qué controles se corren después (suite, shapes, la tabla de M1).

   Demostración en seco: reproducir por el procedimiento un ensamblado sellado de la tanda 0
   a partir de la salida base y de las tres unidades re-extraídas, y comparar su sha256 con el
   sellado. Si los artefactos guardados no alcanzan para reproducirlo, FRENO con el motivo,
   sin forzar la demostración.
f. Propuesta de disparo periódico, para que la autora la decida en el freno de M2. Cómo
   programar que el control corra solo, por ejemplo una vez por mes y solo sobre el índice del
   sitio. Para cada opción:
   - la periodicidad, con su justificación desde el diseño del job (§2.a.6);
   - el número de pedidos por corrida: solo el índice es un pedido; si incluye PDFs, cuántos y
     con qué pedidos condicionales;
   - dónde correría: por ejemplo, el programador de tareas de la máquina local o una tarea
     programada fuera de ella, con lo que cada opción necesita (credenciales, acceso al repo,
     dónde quedan las corridas);
   - a dónde llega el aviso y quién lo ve;
   - qué pasa si una corrida falla o no puede preguntar al sitio.

   La propuesta no se instala en M2: solo se escribe.
FRENO M2:
- los supuestos con su línea de base;
- el resultado del selftest por alteración;
- el resultado de la demostración del empalme;
- la propuesta de alcance de M3 (solo el índice, o el índice y los PDFs con pedidos
  condicionales), con el número de pedidos previsto;
- la propuesta de disparo periódico (punto f);
- la medición de la tercera fuente (punto e): ventana y regex declaradas, conteos, citas
  mapeadas por categoría y el caso de control de la «A» 8432;
- el sha256 de lo escrito.

M3 — Una corrida real del control contra el sitio. USD 0 de API. Solo con el ok escrito de la
autora sobre el alcance propuesto en M2.
a. Parámetros de cortesía del job (diseño, §6): un pedido cada 0,5 s, sin concurrencia, 60 s
   de timeout, 3 reintentos, User-Agent propio sin datos personales. Si el endpoint del índice
   no responde, la corrida se aborta antes de pedir un solo PDF.
b. Salida en data/experiment/mantenimiento/control_sitio/corridas/<fecha>/: el índice crudo, el
   resultado del control y `aviso.md` si corresponde.
c. El control no actualiza nada (decisiones 2 y 3). Si avisa, el reporte dice qué supuesto se
   rompió y qué parte del pipeline depende de él, según la tabla de M1.
FRENO M3, final:
- el resultado de la corrida y su aviso, si lo hay;
- la cantidad de pedidos hechos;
- el sha256 de lo escrito.

Commit de la autora.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j), en todas las etapas.
- Escrituras: solo data/experiment/mantenimiento/ (se crea) y tu scratchpad.
  - No se editan el plan, el checklist, el tablero, los laudos, el backlog ni scripts/.
  - No se edita data/experiment/job_actualizacion/: es de una unidad cerrada; se lee y, si
    hace falta, se importa en solo lectura.
  - No se tocan el inventario sellado, los manifiestos ni los PDFs congelados (decisión 2), y
    data/raw se lee en solo lectura.
  - Nada sellado se toca (CLAUDE.md §3). No commitees.
- Python:
  - PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B en todo Python.
  - Ningún __pycache__ ni .pyc nuevo: línea de base al inicio (conteo de .pyc) y control al
    cierre. data/experiment/job_actualizacion/code/ ya tiene un __pycache__; no se agregan
    archivos a él.
  - Dobles corridas byte a byte idénticas de todo lo que no dependa de la red.
- Afirmaciones y citas:
  - Toda afirmación lleva path:línea o comando.
  - Los conteos se recomputan antes de escribirse (§4 i). Sobre los cinco TOs de desarrollo,
    fracción cruda («tres de los cinco»), nunca porcentaje, y nunca combinada con la ventana de
    los 152.
  - Lo que no esté en un artefacto es NO ENCONTRADO.
  - La tesis no se cita por línea de docs/tesis/main.tex; la fuente es Overleaf.
  - Los mentores solo por rol; cero nombres propios.
- Si algo de este mandato contradice un archivo del repo, mandan los archivos y se reporta la
  contradicción.
- Revisión y checkpoint:
  - Paquete de revisión revision_UMANT_M<n>/ por etapa, con manifest.txt (sha256 y una línea
    por archivo) y nombres únicos.
  - Checkpoint checkpoint_UMANT.md en el scratchpad, actualizado al cierre de cada etapa y antes
    de cualquier compactación.
- Shell zsh: variables entre comillas o como arrays; ningún comentario con # dentro de los
  bloques de comandos para copiar.

CRITERIO DE ACEPTACIÓN por etapa:
- el reporte corto con las salidas pedidas;
- git status --short con solo data/experiment/mantenimiento/ como nuevo (más, en M3, la carpeta
  de la corrida, si la autora decide versionarla);
- M1: la tabla y el selftest de la clave de caché coinciden fila por fila;
- M2: con la línea de base el control sale 0 y sin aviso, y cada alteración simulada dispara
  su aviso y solo el suyo; la medición de la tercera fuente tiene la ventana y la regex
  declaradas antes, y reproduce el caso de control de la «A» 8432;
- M3: corrida hecha dentro del alcance aprobado, con los parámetros de cortesía;
- el grep de convenciones, pegado aunque dé vacío.

FRENO al final de cada etapa.
