FIRMADO por la autora — 2026-09-27 (gate 4 de la fase 2 de B6.0)

MANDATO — U-GATE4-RUNNER-NEO4J (GATE 4 DE LA FASE 2 DE B6.0): RUNNER DE EV2
SOBRE GraphAgentNeo4j EN MODO FULLTEXT, FIRMA V1.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar. Costo de API 0:
esta unidad no hace ninguna llamada real; el runner queda gateado como los
anteriores y su primera corrida real es la celda C2 de la fase 2, con
mandato propio y tope propio.

CONTEXTO (tres líneas). El pre-registro de la tanda 0
(docs/preregistro_tanda0.md, sellado en c80b03f) define las celdas C2 y C4
como el harness congelado de firma v1 corriendo sobre GraphAgentNeo4j en
modo fulltext (A3.1, componentes fijos; A3.2, configuración de Neo4j
sellada por su definición). A5 registra que ningún runner de EV2 instancia
esa clase: runner_ev2.correr_grafo arma FullCaptureAgent(GraphAgent) sobre
GraphIndex (data/experiment/ev2_corrida/code/runner_ev2.py:64-84,126-232;
sha256 c4b067f9…, commit bb89a8e). Esta unidad escribe el runner nuevo como
módulo aparte, sin editar ningún módulo sellado, con el patrón de
ev2_r1/code/comun_r1.py (extensión en memoria) y el precedente de captura
sobre Neo4jIndex de ablacion_retrieval/corrida/agente_celda.py:121-169.
Leé el pre-registro A3.1 a A3.3 y A6, el laudo A1.6
(docs/laudo_promocion_backend.md §3 y :47-51) y los cinco archivos citados
antes de escribir.

DECISIONES YA TOMADAS. No se re-deciden.
1. Sellados que no se editan: el cuarteto de evaluación (harness.py sha256
   fd267e83…, loader, judge, llm_cache), runner_ev2.py, comun_ev2.py,
   comun_r1.py, agente_neo4j.py, neo4j_index.py, indices.py, grafos.py,
   conexion.py, cargar_kg.py. El runner nuevo los importa; verificá y pegá
   el sha256 de harness.py, runner_ev2.py, agente_neo4j.py (403a9b42…) y
   neo4j_index.py (5f38db1b…) al inicio y al cierre.
2. Agente: GraphAgentNeo4j (agente_neo4j.py:56-65; constructor (indice,
   client, cache_conversation)) sobre Neo4jIndex(driver, grafo,
   modo="fulltext") (neo4j_index.py:93-109), con el driver de
   conexion.abrir_driver (conexion.py:27-31). Firma v1 de las tres
   herramientas, tal como la sirve el harness; las tools v2 de A1.2 no se
   usan (laudo A1.6:47-51). Modelo, temperatura y tope de llamadas son los
   del harness (:47, :48, :50); el runner no los redefine.
3. Captura completa: una subclase FullCaptureAgentNeo4j(GraphAgentNeo4j)
   que replica el _run_tool y el ask_capturando de
   runner_ev2.FullCaptureAgent (:64-84) sin heredar de él, como hace
   agente_celda.py:156-169. La lista full_outputs queda 1:1 con
   trace.steps.
4. Traza por caso con la MISMA estructura que las de C1
   (ev2_r1/trazas/ev2_r1_base/EV2F-*.json): claves de primer nivel meta,
   pregunta, trace (= vars(QuestionTrace)), steps_full y raw_turns_agent,
   y en meta las mismas claves que escribe runner_ev2.py:158-181 (unidad,
   label, grafo, kg_path, kg_sha256, eje, caso_id, …, model, temperature,
   max_tool_calls, thinking_enabled, timestamps, code_version,
   graph_fingerprint, cache_turnos, fidelidad_sin_evaluar), más:
   meta.backend = GraphAgentNeo4j.backend (agente_neo4j.py:67-73: backend,
   grafo, nombre_canonico, kg_sha256, modo, indice_fulltext) y
   meta.model_segun_api = lista ordenada de los valores distintos de
   raw.model en raw_turns_agent (regla C1.9 del plan y A6 del
   pre-registro: el id devuelto por la API por llamada). El juez v1
   (ev2_r1/code/juez_r1.py:61-83) y los indicadores de cita
   (scripts/ucita2_indicadores.py) leen meta.caso_id,
   trace.final_json.respuesta, trace.parse_ok y trace.seen_provenances:
   nada de eso cambia de nombre ni de forma.
5. Caché y namespace: lc.CachingClient con domain "agent", una db por
   corrida en data/experiment/ev2_tanda0/cache/<label>.db, y namespace
   lc.make_namespace("agent", code_ver=lc.code_version(),
   graph_fp=<sha256 del kg.json registrado en grafos.py para ese grafo> +
   "|neo4j:" + modo + ":" + nombre del índice, thinking=False). No se
   reutiliza build_cache_client de runner_ev2 (exige un KnowledgeGraph con
   .path, runner_ev2.py:90-95): GraphAgentNeo4j corre sobre un kg vacío
   (agente_neo4j.py:47-51). Que el namespace incluya modo e índice
   garantiza que nunca colisiona con las dbs de C1.
6. Casos: por default los 40 casos de fidelidad de EV2 en el orden sellado
   de C1 (comun_r1.casos_fidelidad_r1 y el orden persistido orden-ev2-r1,
   pre-registro de r1 §4), para que C2 sea comparable con C1 (A3.3, par C1
   vs C2). Argumento --casos RUTA para un JSON alternativo (las preguntas
   nuevas sobre los cinco, cuando existan), con el mismo formato {caso_id,
   eje, pregunta}.
7. Gating de gasto idéntico al de runner_r1.py:17-23,99-100: el modo real
   exige --autorizado-fase-b y --tope USD; sin los dos, aborta sin llamar a
   nada; freno por proyección de correr_grafo (estado_gasto). En esta
   unidad el modo real NO se ejecuta.
8. Interfaz: python3 -B data/experiment/ev2_tanda0/code/runner_ev2_neo4j.py
   --grafo <clave de grafos.py: KG_Reextraido_r1 hoy; la del grafo de
   desarrollo re-extraído cuando el gate 5 la registre> --modo fulltext
   --label <label> [--casos RUTA] [--outdir RUTA] [--db RUTA]
   [--autorizado-fase-b --tope USD]. Salida por default en
   data/experiment/ev2_tanda0/trazas/<label>/ con resumen_<label>.json
   como en runner_ev2.py:212-227. Sin --outdir explícito fuera del repo, la
   unidad no escribe trazas en el repo (ver escrituras).

TAREA (una sola unidad): escribir el runner de la decisión 8 y su selftest,
y correr el selftest.
a. data/experiment/ev2_tanda0/code/runner_ev2_neo4j.py con las decisiones
   2 a 8; docstring que declare qué reutiliza por import y qué replica (y
   por qué no puede importarlo).
b. data/experiment/ev2_tanda0/code/selftest_runner_ev2_neo4j.py, solo
   stdlib más los módulos del repo, con dos bloques y --outdir y --db
   obligatorios hacia tu scratchpad:
   (i) OFFLINE, sin Neo4j y sin API: un cliente falso con el patrón de
   ev2_r1/code/selftest_r1.py (respuestas scripteadas con tool_use y un
   final_json válido) y un stub de Neo4jIndex con las tres herramientas
   sobre tres nodos inventados; verifica que el runner aborta sin
   --autorizado-fase-b y --tope, que la traza tiene exactamente las claves
   de la decisión 4 (comparadas contra las claves de
   ev2_r1/trazas/ev2_r1_base/EV2F-001.json, salvo u_b18 y las dos nuevas),
   que steps_full es 1:1 con trace.steps, que meta.model_segun_api sale
   del raw.model del cliente falso, que meta.backend trae modo fulltext y
   el índice, que el tope de 15 llamadas del harness corta con
   hit_tool_limit true cuando el cliente falso pide 16, y que el namespace
   de la caché contiene el sha del grafo, el modo y el índice.
   (ii) INTEGRACIÓN, con Neo4j arriba y sin API: el mismo cliente falso,
   pero Neo4jIndex real sobre KG_Reextraido_r1 en modo fulltext; el
   cliente falso pide buscar_nodos con una consulta cuyo primer resultado
   conocés de antemano por una consulta directa al índice (mostrala),
   ver_nodo de ese id y ver_vecinos; verifica que los outputs capturados
   en steps_full vienen de Neo4j (mismo id que la consulta directa), que
   trace.seen_provenances no queda vacío y que el sha256 del grafo en
   meta.backend es 0226e947…. Precondición: docker ps --filter name=neo4j
   muestra el contenedor Up (healthy) (docker-compose.yml:34-40). Si no
   está arriba, NO lo levantes ni toques Docker: reportá el comando y su
   salida, marcá el bloque (ii) como NO CORRIDO y frená igual con el
   bloque (i) en verde; el gate queda a la espera de la autora.
c. Correr el selftest completo y pegar su salida.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j).
- Escrituras permitidas: los dos archivos nuevos bajo
  data/experiment/ev2_tanda0/code/ (directorio nuevo) y tu scratchpad.
  Ninguna traza, db ni resumen dentro del repo en esta unidad: --outdir y
  --db del selftest apuntan al scratchpad. Nada más: ni los sellados de la
  decisión 1, ni .gitignore, ni docs/, ni el plan. No commitees. Costo de
  API 0: ningún cliente real se construye; ANTHROPIC_API_KEY no se lee.
- PYTHONDONTWRITEBYTECODE=1 en todo Python que corras; ningún __pycache__
  ni .pyc nuevo en el repo. Corré con .venv/bin/python (el driver de Neo4j
  y el SDK están ahí; anotá las versiones).
- Zonas selladas de CLAUDE.md §3 intactas; ningún kg.json se lee salvo por
  el sha256 que grafos.py ya verifica.
- Toda afirmación con path:línea o comando; conteos recomputados antes de
  escribirse (§4.i); lo que no esté en un artefacto es NO ENCONTRADO.
- Cero nombres propios de personas; los mentores solo por rol.
- Paquete de revisión revision_GATE4/ en tu scratchpad con manifest.txt
  (sha256 y una línea por archivo): los dos scripts, la salida del
  selftest, las trazas del selftest, la salida de la consulta directa al
  índice, los sha de los sellados al inicio y al cierre, y el estado del
  árbol. Reporte al frenar de no más de 40 líneas.
- Si tu contexto se acerca al límite o vas a compactar, ANTES escribí en
  tu scratchpad checkpoint_GATE4.md con qué decisiones (1–8) están
  implementadas y qué bloques del selftest corriste, y reportá la ruta.

CRITERIO DE ACEPTACIÓN, con salida en el reporte: sha256 de los cuatro
sellados de la decisión 1 iguales al inicio y al cierre; git status --short
mostrando solo data/experiment/ev2_tanda0/ como no rastreado, más
adjudicar.py y lo que otras unidades tengan en curso, enumerado; --help del
runner pegado; bloque (i) en verde con la cuenta de casos; bloque (ii) en
verde con la consulta directa y el id coincidente, o NO CORRIDO con el
docker ps pegado; ninguna traza ni db bajo el repo (find
data/experiment/ev2_tanda0 -name "*.json" -o -name "*.db" pegado, vacío);
grep de convenciones sobre los dos scripts, pegado aunque dé vacío.

FRENO al terminar. La autora revisa el diff antes de commitear; el gate 4
se cierra en el plan con el commit y con el bloque (ii) corrido.
