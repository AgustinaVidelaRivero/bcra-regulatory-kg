FIRMADO por la autora — 2026-09-28 (re-extracción dirigida de tres unidades de cap, antes de E3 de 2a)

MANDATO — U-TANDA0-2A-DIR: RE-EXTRACCIÓN DIRIGIDA DE TRES UNIDADES DE CAP
EN LA TANDA 0, ANTES DE E3.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar. Unidad en DOS
ETAPAS con FRENO obligatorio al final de cada una: reporte corto (no más
de 40 líneas) y espera de la revisión y del «seguí» escrito de la autora.
Tope de gasto de la unidad: USD 1,00. Costo de API 0 en D1; gasto solo en
D2.

CONTEXTO. E2 de U-TANDA0-2A cerró en ad6d5ad con tres unidades de cap sin
extraer: cap::3.1.14.1, cap::4.2.1.2 y cap::4.3.3.1. Cortaron a 8.192 y el
reintento a 32.768 (cliente_e1.py:60) fue rechazado por la guarda del SDK
(_base_client.py:731-740). En r1 esas tres pasaron por
data/experiment/reextraccion_v2/corpus_v2/reextraccion_dirigida.py
(5273c0c) a 16.384: dos recuperadas y cap::4.2.1.2 cortó de nuevo
(corpus_v2/salida/reextraccion_dirigida.json). Leé completos ese script,
docs/decisiones_caching_extraccion.md, la fila B6.0 fase 2a del plan
(cierre de E2 e incidencia) y los módulos que D1 nombra antes de escribir
una línea.
Base: decisión 2 y A1 del pre-registro de la tanda 0 (mismos pasos que
produjeron r1); r1 incluyó esta re-extracción dirigida por laudo posterior
a la corrida (5273c0c). Decisión de la autora del 28/09: se aplica también
a la tanda 0, antes de E3, y E3 de 2a toma salida_dirigida/ como entrada.

DECISIONES YA TOMADAS. No se re-deciden.
1. Se re-extraen solo esas tres unidades, con max_tokens 16.384
   (runner_corpus.py:87, MAX_TOKENS_REINTENTO) y el MISMO request que la
   corrida de E2 en todo lo demás: perfil v3_b54 del manifiesto
   tanda0_10tos.json, prompt v3, namespace v3. A 16.384 la guarda del SDK
   no actúa (3.600 × 16.384 / 128.000 = 460,8 s).
2. El script de r1 NO se corre ni se edita: escribe en corpus_v2/salida
   (:49), aborta por su assert de fase cerrada (:78) y arma el request con
   el prompt v2 (:111), el validador sin esquema (:136) y el ratchet sin
   perfil (:168). Se replica su lógica en un módulo nuevo:
   data/experiment/tanda0/code/reextraccion_dirigida_tanda0.py, que
   importa los mismos módulos sin editar ninguno y llama a
   runner_corpus.configurar con el manifiesto tanda0_10tos.json.
3. En el módulo nuevo, contra el script de r1: request con
   PERFIL.build_request_kwargs(chunk, model=MODEL_E1, max_tokens=16384);
   validar_salida con esquema=PERFIL.esquema; ciclo_ratchet con
   perfil=PERFIL; chunks de rc.E0_DIR (salida_tanda0); clientes E1 y de
   reintentos con prefijo_hash=PERFIL.prefijo_hash_para_namespace (como
   runner_corpus.py:800-803 y :820-824); run_label tanda0_dirigida_e1,
   tanda0_dirigida_e3 y tanda0_dirigida_reint; CASOS con las tres unidades
   de cap y nada más.
4. Tope USD 1,00 COMPARTIDO por los tres clientes con
   PresupuestoCompartido (runner_corpus.py:149) sobre un archivo nuevo,
   presupuesto_reextraccion_dirigida.json. No un tope por cliente: la
   dirigida de r1 gastó 0,5277 con tope 0,50 por esa razón.
5. Las salidas de E2 commiteadas en ad6d5ad no se tocan. Se trabaja sobre
   data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/, copia
   completa de corpus_tanda0/salida/ hecha al inicio de D1 (git guarda un
   solo objeto por contenido idéntico, así que la copia no duplica el
   repo). Sobre la copia, el módulo hace lo que hizo r1: append a
   cap/extracciones_e1.jsonl y cap/finales.jsonl (last-wins), fase
   reextraccion_dirigida en estado_corpus.json, compactar_e1 y cerrar_e2
   solo de cap. La etapa E3 de U-TANDA0-2A toma salida_dirigida/ como
   entrada.
6. Lo que falle de nuevo va a cola humana con su expediente, como en r1.
   La recuperación no es criterio de aceptación.

D1 — Módulo, selftest y copia. USD 0.
a. Copia corpus_tanda0/salida/ a corpus_tanda0/salida_dirigida/ y mostrá
   el output de diff -r entre las dos, que debe ser vacío.
b. Módulo nuevo según las decisiones 2 a 5, y selftest
   data/experiment/tanda0/code/selftest_dirigida_tanda0.py con clientes
   stub, sin red, que verifique: solo las tres unidades; escritura solo
   bajo salida_dirigida/; los nueve TOs distintos de cap intactos; el
   gasto combinado frena antes de superar el tope.
c. PRUEBA DEL REQUEST, con evidencia: con max_tokens 8.192, el request que
   arma el módulo para cada una de las tres unidades debe dar la misma
   clave (llm_cache.compute_key sobre el namespace y el request canónico)
   que las tres filas de e1_extraccion.db con run_label corpus_cap_e1 y
   stop_reason max_tokens del 27/09/2026. Pegá las seis claves.
FRENO D1: reporte con el diff -r, el selftest, las seis claves, sha256 de
los sellados al inicio y al cierre, .pyc al inicio y al cierre.

D2 — Corrida. Tope USD 1,00.
a. Precios del día verificados y pegados antes de correr, iguales a
   P_E1 y P_E3 del runner; si difieren, FRENO sin gastar.
b. Corrida del módulo. Al cierre: desenlace por unidad (estado de E3,
   entidades, relaciones, residuales, o motivo de cola humana); gasto
   desde las dbs por run_label con la fórmula D2, contra la estimación de
   la mesa de USD 0,43 (el costo de las tres en r1 recalculado a los
   precios actuales) y contra el tope; nuevo grafo_cap.json con nodos y
   aristas, y el fan-in de cap; diff -r entre salida/ y salida_dirigida/,
   que solo puede mostrar archivos de cap/ y estado_corpus.json, más el
   presupuesto nuevo y el resumen de la dirigida.
c. Registro de modelos por llamada de las tres run_label, desde las dbs
   (cache.model y request_json), en
   reports/tanda0/registro_modelos_2a_dirigida.json.
FRENO D2: reporte con lo de b y c, incidencias, git status --short y grep
de convenciones.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j).
- Escrituras: solo corpus_tanda0/salida_dirigida/, los dos módulos nuevos
  bajo data/experiment/tanda0/code/, el registro de D2.c y tu
  scratchpad. corpus_tanda0/salida/, corpus_v2/ y todo lo sellado de
  CLAUDE.md §3 son solo lectura. Ningún módulo del pipeline se edita. No
  commitees.
- PYTHONDONTWRITEBYTECODE=1 en todo Python, con .venv/bin/python. Ningún
  __pycache__ ni .pyc nuevo.
- Toda afirmación con path:línea o comando; conteos recomputados antes de
  escribirse (§4.i); lo que no esté en un artefacto es NO ENCONTRADO. Cero
  nombres propios.
- Paquete de revisión revision_TANDA0_2A_DIR_D<n>/ con manifest.txt por
  etapa. Checkpoint checkpoint_TANDA0_2A_DIR.md en el scratchpad al cierre
  de cada etapa y antes de cualquier compactación.

CRITERIO DE ACEPTACIÓN. D1: diff -r vacío, selftest en verde, seis
claves coincidentes de a pares, sellados sin cambio. D2: gasto ≤ USD 1,00
desde las dbs, las tres unidades con desenlace registrado, diff -r
limitado a lo declarado en D2.b, registro de modelos completo.

FRENO al final de D1 y de D2.
