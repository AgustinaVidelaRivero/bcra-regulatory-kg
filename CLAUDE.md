# CLAUDE.md — bcra-regulatory-kg

## 1. Qué es este proyecto

Tesis de Ingeniería en IA (UdeSA): ¿organizar los textos regulatorios del BCRA
como Knowledge Graph mejora la fidelidad de un sistema RAG frente a retrieval
tradicional? Hallazgo rector: **grounded ≠ correct** — una respuesta anclada en
el grafo puede seguir siendo incorrecta contra la norma.
Pipeline: un agente Haiku navega el grafo con tres tools (`buscar_nodos` /
`ver_nodo` / `ver_vecinos`); un juez evalúa contra clave; un verificador
diagnóstico atribuye causas con capa determinística encima.
Corpus: 5 Textos Ordenados del BCRA (`data/experiment/subset/`, read-only).

## 2. Mapa de lectura

- Antes de cualquier tarea: `docs/tablero.md` (estado vigente y cola de unidades).
- Historia y cadena de validaciones: `docs/INDICE.md`.
- Los documentos sellados por commit son LA fuente de verdad: ante cualquier
  conflicto con memoria de sesión, resúmenes o herramientas externas, mandan
  los archivos commiteados.

## 3. Zonas selladas — NUNCA editar, mover ni borrar

- `data/experiment/grafo_v2/kg.json` (medición sellada) y los cinco runs:
  `data/experiment/run_{1_cookbook,2_papers,3_ppf_core,4_schema_light,5_hybrid}/`.
- Todo eval set (`data/experiment/evaluacion/queries/` y el material EV1 de
  `data/experiment/evaluacion_escalon1/`). EV1/CQ/CQN/CQN2 son material
  QUEMADO: no sirven como re-test ni objetivo de nada.
- Cuarteto hasheado de evaluación: `data/experiment/evaluacion/{loader,harness,judge,llm_cache}.py`.
- Cluster congelado del verificador: `data/experiment/evaluacion/{verificador,capa_deterministica,capa_deterministica_v62,s1_fuentes,s1_fuentes_v04,test_alcanzabilidad}.py`
  (hashes sellados en `posthoc_run/dev_set/extraccion_h2h_ciclo2.md` §Sello).
- Cachés y datos sellados: `data/experiment/evaluacion/cache/`,
  `data/experiment/grafo_v2/code/cache/` y `code/cache_v2/`,
  `data/experiment/evaluacion/trazas/`, `posthoc_run/` (incluye las dbs
  `escalon1*_r{1,2,3}.db`), `frozen_run/`, `frozen_smoke/`.
- `.gitignore` no se toca sin mandato explícito.

El grafo VIGENTE (el único editable, y solo vía el circuito de refinamiento con
propuesta sellada + laudo) es el que declara `docs/tablero.md`.

## 4. Circuito de trabajo

Toda sesión ejecuta UNA unidad definida por un prompt-mandato con escrituras
enumeradas y criterios de aceptación. Reglas duras:

a. NUNCA commitear — los commits son de la autora, post-revisión.
b. Al terminar, FRENAR y esperar revisión.
c. Lo no autorizado explícitamente está prohibido.
d. Si algo del mandato contradice un archivo del repo, mandan los archivos y
   se reporta la contradicción.
e. Errores propios se reportan con causa; no se ocultan.
f. Costo de API distinto de 0 solo si el mandato lo autoriza con tope.
g. PAQUETE DE REVISIÓN: al frenar, armar un directorio `revision_<unidad>/`
   en el scratchpad de la sesión con TODOS los archivos que la revisión
   independiente necesita, con nombres únicos y descriptivos que incluyan
   unidad y estado (`kg_post_C4.json`, `backlog_post_C4.jsonl` — NUNCA
   nombres genéricos como `kg.json`, que colisionan al subirse), más un
   `manifest.txt` con sha256 y una línea de descripción por archivo. Los
   archivos del repo NO se renombran ni se copian dentro del repo: el
   paquete es una copia de cortesía para la revisión, fuera del repo.
   COPIA PERMANENTE (08/10/2026): al frenar, el paquete se copia también
   a `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/`, con la misma ruta
   relativa que tiene bajo la carpeta del proyecto en `/private/tmp/claude-501/`
   (`<sesión>/scratchpad/revision_<unidad>/`), con `ditto`, y se verifican en
   la copia los sha256 de su `manifest.txt`. El FRENO dice la ruta de la
   copia y el resultado de la verificación. Lo que la revisión o el repo
   necesiten y viva fuera del paquete (bases pagadas, tar.gz de salidas,
   registros que una etapa posterior copia al repo) va dentro del paquete.
   Motivo: macOS borra cada noche lo de `/private/tmp` con más de 3 días
   (`com.apple.tmp_cleaner`), y paquetes citados por el repo ya se perdieron
   (inventario de la mesa del 08/10/2026; el resguardo de ese día está en
   la misma carpeta, con su `manifest_sha256_20261008_1207.txt`).
h. REPORTE Y ARTEFACTOS: el reporte final de la unidad se redacta para ser
   pegado como texto (conciso, con los verbatims imprescindibles); todo
   artefacto extenso (archivos completos, tablas largas, JSONs) va al
   paquete de revisión de la regla g, referenciado por nombre — no pegado
   en el reporte. Regla práctica: un bloque que supera ~40 líneas es
   artefacto, no reporte.
i. CONTEOS: todo tally que aparezca en prosa (reportes, frenos, mensajes
   de commit) se RECOMPUTA contra el artefacto que lo respalda ANTES de
   escribirse — un desglose cuya suma no cierra, o un total sin desglose
   verificable, es un defecto reportable. Lección de U-B5.1: un "33 ítems"
   del freno resultó ser 25 numerados + una sección en prosa, y llegó
   hasta el borrador del mensaje de commit antes de ser cazado.
   AMPLIACIÓN (07/09/2026): la regla se extiende de los tallies a TODA
   AFIRMACIÓN FÁCTICA SOBRE EL MUNDO que entre a un laudo, registro o
   mandato — fechas de adquisición, procedencia de un artefacto,
   versiones, autoría de un dato: cada una lleva su ancla (archivo,
   comando o commit que la respalda) o se marca EN EL PROPIO TEXTO como
   NO VERIFICADA, con esas palabras. Un dato que se atenúa
   ("aproximadamente marzo", "hacia mayo") sigue leyéndose como hecho:
   el hedge no reemplaza la marca. Un dato sin ancla es defecto
   reportable aunque suene correcto. Precedente: "marzo de 2026" se
   propagó a tres documentos, uno de ellos un laudo FIRMADO, porque
   nadie le pidió su ancla — y el ancla estaba a un comando de
   distancia (docs/fe_erratas_fecha_corpus_congelado.md).
j. ACCIONES DE LA AUTORA: ningún bloque, reporte, laudo, pase ni mensaje
   de commit afirma como HECHA una acción que solo la autora ejecuta
   (commit, despacho de mandato, firma) sin su confirmación explícita;
   hasta esa confirmación se escribe como PENDIENTE o PREPARADA. Estas
   acciones no dejan rastro verificable en el repo hasta consumarse, así
   que la verificación contra archivos no las cubre: la confirmación de
   la autora es la única evidencia admisible. Precedentes: el commit de
   U-B5.1 (mensaje preparado, commit no corrido, detectado tarde por
   git log) y el despacho fantasma de U-B5.3 (afirmado "en curso" desde
   el 04/09, despachado recién el 05/09, con la afirmación falsa
   arrastrada hasta un laudo firmado — fe de erratas
   docs/fe_erratas_despacho_UB53.md).
k. FUENTES FIRMADAS: las fuentes de un documento firmado (laudo,
   enmienda, mandato, pre-registro) se leen en el commit de la firma
   (`git show <commit>:<ruta>`), con su sha256 verificado, nunca en el
   archivo actual. Un documento firmado puede recibir después notas
   fechadas, que cambian el sha del archivo sin cambiar el texto
   firmado. Y una verificación nunca corre un generador sobre el repo:
   lo corre sobre una copia en el scratchpad. Precedentes, del
   01/10/2026: la nota posterior a la firma de L-ESQ-R2 (7ac1b5c) rompió
   la re-derivación del catálogo r2, que leía el archivo actual (falló
   K1; corregido en 5084781, plan, principio 9); y, al verificarlo, la
   mesa revisora corrió el derivador sobre el repo y sobrescribió el
   JSON, que hubo que restaurar desde una copia.
l. COPIAS PARA VERIFICAR: la copia sobre la que corre una verificación
   (regla k) se arma copiando los archivos, nunca con enlaces
   simbólicos que apunten al repo: lo que se escribe a través de un
   enlace se escribe en el repo. Y la corrida controla que el repo no
   cambie: toma el sha256 de sus archivos antes y después, y los
   compara. Precedente, del 02/10/2026: en R4 de U-R2-CODIGO, el
   espejo de una verificación tenía `data/experiment/r2_codigo` como
   enlace simbólico al repo; al escribir ahí el código de HEAD se
   pisaron tres archivos del repo (`r3d_remisiones.py`,
   `selftest_r3.py` y `rk_fuera_de_muestra.py`), que hubo que
   restaurar (`data/experiment/r2_codigo/r4_freno.md`, «Error propio,
   con su causa»; 26d274d).
   Los selftests también corren sobre la copia.
   `corpus_v2/selftest_corpus.py` borra y regenera
   `corpus_v2/salida_selftest/`, que tiene archivos rastreados. Y
   `selftest_manifiesto.py` solo da P5 en verde desde la raíz del repo,
   porque el reporte sellado de E2 guarda la ruta absoluta de su
   entrada: sobre una copia el resultado correcto trae esos 5 fallos,
   y un resultado sin ellos indica que corrió sobre el repo.
   Precedente, del 03/10/2026: en P2 de U-PROMPT-R2, `selftest_corpus`
   corrió sobre el repo y reescribió 11 archivos rastreados, que hubo
   que restaurar (`data/experiment/prompt_r2/freno_p2.md`, §7).
   La corrida en seco de un runner ejercita el mismo camino de imports
   y de código que el runner: importa el runner y llama a sus
   funciones, sin arreglar el `sys.path` por fuera, y recorre las
   ramas que la corrida real puede tomar (corte, reintento, partición,
   tercer escalón, salida mal formada). Precedente, del 05/10/2026: en
   T1 de U-REEXT-T0 la corrida en seco agregaba `e0_chunking` al
   `sys.path` (`data/experiment/reext_t0/t1_corrida_en_seco.py:54`) y
   el runner no (`corpus_v2/runner_corpus.py:64-67`); en T2,
   `import correr_e0` falló al partir por corte y `cap::4.2.1.2` quedó
   sin validación (`data/experiment/reext_t0/freno_t2.md`).

## 4bis. Prompt caching en extracción

Antes de tocar `data/experiment/grafo_v2/code/extract.py` o cualquier call
site LLM de extracción, leer `docs/decisiones_caching_extraccion.md`; sus
cinco decisiones son vinculantes.

## 5. Convenciones de documentos

- Primera persona del singular.
- Cero nombres propios de personas; toda decisión se documenta por su
  justificación técnica, nunca por su origen conversacional o por quién la pidió.
- Todo número con el comando o la ruta que lo reproduce.
- Grep de convenciones al cierre de cada unidad (pegar aunque dé vacío).
- Castellano técnico.

## 6. Estructura del repo

- `app/` — app web de chat sobre los KGs (agente RAG con citas y registro de feedback).
- `data/raw/` — corpus BCRA descargado (scraper idempotente + manifiesto); `data/processed/`, `data/kg/` — vacíos (legado).
- `data/experiment/` — subset de 5 TOs, run_1..run_5, grafo_v2 (+ reensamblado_v3, vigente), evaluación (2.3/2.3+/2.4), escalón 1, métricas intrínsecas.
- `data/backlog/` — backlog unificado de refinamiento (`backlog.jsonl`, propuestas selladas, retests).
- `docs/` — especificaciones, protocolos, lecturas, tablero, INDICE, literatura, ppf, defensa, tesis.
- `scripts/` — herramientas versionadas (métricas intrínsecas, shapes_validator).
- `src/` — scraper y extracción legacy (pre-Fase 2.2).
- `sessions_server/` — sesiones jsonl cosechadas de la app (insumo del intake).
- `notebooks/`, `reports/` — exploración puntual y reportes sueltos.
- `_archive_riesgo_crediticio/` — archivo del scope viejo.
