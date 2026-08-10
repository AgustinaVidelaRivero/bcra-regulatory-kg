# Diseño — pipeline de queries sintéticas desde el grafo (issue #3)

Documento de diseño. No implementa nada: define el pipeline de generación de
preguntas sintéticas muestreadas desde el grafo vigente, sus estratos, sus
puertas de calidad y sus métricas. La implementación y el laudo de volumen son
de una unidad posterior.

## 1. Objetivo

Este pipeline mide la **navegabilidad** del grafo: si lo que existe en el grafo
es alcanzable por el agente. Es un eje complementario y ortogonal al generador
ciego de U6, que mide fidelidad desde el corpus (si lo que la norma dice, está
en el grafo). Los dos ejes responden preguntas distintas y no se sustituyen.

Limitación declarada de entrada: este eje **no detecta ausencias**. Toda
pregunta nace de un subgrafo muestreado del grafo, y lo que no está en el grafo
no puede samplearse; por construcción, el pipeline es ciego a lo que falta. Las
ausencias son territorio del otro eje (generación ciega desde los PDFs) y del
censo estructural. Reportar navegabilidad como si fuera cobertura sería un
error de interpretación que este documento excluye desde el diseño.

La motivación de cobertura es concreta. Los 4 sets históricos de evaluación
(EV1, CQ, CQN, CQN2) tocan el 32,1 % del territorio normativo de los 5 TOs:
246 unidades del inventario, 48 quemadas enteras y 31 parciales, 167
disponibles
(fuente: `data/experiment/exploracion/mapa_territorio_quemado_5TOs_4sets.json`,
clave `totales`:
`python3 -c "import json; print(json.load(open('data/experiment/exploracion/mapa_territorio_quemado_5TOs_4sets.json'))['totales'])"`
→ `pct_tocado: 32.1`). El resto del territorio nunca fue interrogado. Y la
generación manual no escala: el set U6 costó una semana de trabajo por 25
preguntas aptas. Un pipeline sintético con gold por construcción es la única
vía realista para interrogar el territorio restante a un costo por pregunta
acotado.

## 2. Mecánica de generación

El ciclo por pregunta es:

1. Se **samplea un subgrafo** del grafo vigente (un arista, un camino, un
   vecindario — según el estrato, §3).
2. Un **LLM genera la pregunta** cuya respuesta ES ese subgrafo: la pregunta se
   redacta para que el subgrafo muestreado sea su respuesta completa y
   correcta.
3. El **agente corre** sobre el grafo con sus tres tools
   (`buscar_nodos` / `ver_nodo` / `ver_vecinos`).
4. Se **mide si llegó**: si el gold aparece en la traza (§7).

El gold existe por construcción — no hay que redactarlo, validarlo contra la
norma ni pagar adjudicación humana por caso: el subgrafo muestreado en el paso
1 es la clave.

El patrón de referencia es el synthesizer de deepeval
(https://deepeval.com/docs/synthesizer-introduction): goldens como tripla
input + expected + contexto, desacoplados de cualquier corrida concreta y
re-corribles entre versiones del sistema; *evolutions* como complicación
controlada de la pregunta base; y puertas de calidad sobre lo generado antes de
que entre al set. Tomo el patrón, no la librería: deepeval genera desde
documentos con chunking genérico, y este pipeline genera desde estructuras del
grafo — el muestreo estratificado de §3 no tiene equivalente en la herramienta.

## 3. Muestreo estratificado (cinco estratos)

- **E-A — aristas de 1 salto.** Alcanzabilidad básica: dado un par de nodos
  conectados, ¿el agente llega del uno al otro? Es el piso del eje; si esto
  falla, el resto no es interpretable.

- **E-B — caminos de 2-3 saltos**, con un sub-estrato explícito de caminos que
  exigen recorrer aristas **entrantes** en algún tramo. Este sub-estrato apunta
  directo a la asimetría direccional documentada en BKL-0027: en RT-C6-3 el
  rol `Sujeto_rol_sujeto_obligado_proteccion` tenía 7 aristas `miembro_de`
  entrantes, el agente pidió `ver_vecinos` en dirección saliente, recibió 0 y
  declaró la pregunta no-respondible pese a que el propio output informaba los
  vecinos entrantes (fuente: `data/backlog/backlog.jsonl`, entrada BKL-0027:
  `grep '"id": "BKL-0027"' data/backlog/backlog.jsonl`). Los nodos alcanzables
  solo "hacia atrás" son un blanco medible, y este sub-estrato los mide con N
  en vez de con un caso.

- **E-C — vecindarios de hub.** Preguntas de enumeración sobre nodos de alto
  grado: ¿el agente recupera los k vecinos que componen la respuesta, o corta
  antes? Es la familia de fallas de U6-009/012 (enumeraciones parciales sobre
  hubs).

- **E-D — pares de cláusulas cuasi-duplicadas con variación**, intra e
  inter-TO: dos puntos normativos casi idénticos que difieren en un
  calificador, un plazo o un alcance. La pregunta apunta a una de las
  variantes; se mide si el agente distingue la correcta o se queda con el
  primer match plausible. Es la familia de U6-008/010/011.

- **E-E — uniforme aleatorio sobre el grafo**, como control no sesgado.

Justificación del E-E: los estratos A-D derivan de modos de falla conocidos del
proyecto y funcionan como regression tests — miden si los mecanismos ya
documentados siguen operando. Pero medir **solo** ahí sesgaría la comparación
central a favor del grafo diseñado precisamente para arreglar esos modos de
falla: sería evaluar al alumno con las preguntas que motivaron su plan de
estudio. El estrato uniforme da la cobertura honesta — territorio muestreado
sin mirar el historial de fallas — y se reporta **por separado** de los
estratos dirigidos, nunca promediado con ellos.

## 4. Gold invariante entre grafos

El gold de cada pregunta se expresa en **anclas de provenance** (documento +
punto normativo), no en ids de nodo. La razón es estructural: los ids no viajan
entre grafos, y la medición central (issue #10) compara tres grafos — un gold
atado a ids de un grafo sería inaplicable a los otros dos.

Resolución por-grafo: los nodos-gold de cada grafo son los que portan esa
provenance. La misma ancla (TO + punto) resuelve a nodos distintos en cada
grafo, y la métrica se computa contra los nodos resueltos localmente.

Censo previo por grafo: antes de correr, se verifica para cada caso si el gold
existe en cada grafo. Si no existe, el caso se registra como **ausencia de ese
grafo** — que es un dato de fidelidad, no de navegabilidad — y se **excluye**
de la métrica de navegabilidad de ese grafo. Los dos ejes se reportan sin
mezclarse: un grafo al que le falta el gold no "falla navegación", le falta el
contenido, y confundir las dos cosas invalidaría la comparación.

## 5. Evolutions y diseño apareado

Cada gold genera **dos versiones** de la pregunta:

- **Literal**: puede compartir vocabulario con los nodos del gold.
- **Anti-léxica**: reformulada sin los tokens del `label` ni los de alta señal
  de la `descripcion` — como la escribiría un usuario que no conoce la jerga
  del grafo.

El delta de desempeño entre los pares literal/anti-léxica aísla el efecto de la
clausura léxica como medición propia. La clausura léxica es un mecanismo
documentado del proyecto: el agente no puede buscar lo que no sabe que existe,
y sin navegación estructural lo no-nombrado por la pregunta es inalcanzable
(fuente: `data/experiment/exploracion/adjudicacion/notas_adjudicacion_u6.md`,
mecanismo 6, casos U6-005/009/016/019). Hasta ahora ese mecanismo se observó
caso por caso; el diseño apareado lo convierte en una medición con N y con
control.

Además, el solape léxico pregunta↔gold se computa y se reporta como **variable
continua por pregunta** — no solo el contraste binario literal/anti-léxica,
sino el gradiente, que permite correlacionar solape con éxito de navegación.

Evolution adicional: **multicontexto** — preguntas cuya respuesta une puntos de
más de un TO. Aplicable a los estratos B (caminos que cruzan TOs) y D (pares
cuasi-duplicados inter-TO).

## 6. Puertas de calidad

Toda pregunta generada pasa por un validador mecánico antes de entrar al set,
siguiendo el patrón del validador de anclas de U6
(`data/experiment/exploracion/validar_anclas.py`):

- **(a) Resolución unívoca.** El gold declarado es efectivamente alcanzable en
  el grafo, y la pregunta no admite otro gold igual de válido. Es un chequeo
  estructural sobre el grafo, no un juicio semántico.
- **(b) Auto-contención.** La pregunta se entiende sin contexto externo — sin
  "el punto anterior", sin referencias al subgrafo que la generó.
- **(c) Exclusión de material quemado.** Cruce contra el mapa de territorio
  (`data/experiment/exploracion/mapa_territorio_quemado_5TOs_4sets.json`):
  ninguna pregunta sintética puede caer sobre anclas de EV1/CQ/CQN/CQN2.
- **(d) Para las anti-léxicas**: verificación de que el solape léxico queda
  bajo el umbral **y** de que la reformulación sigue resolviendo al mismo gold
  (una anti-léxica que cambió la respuesta no es una evolution, es otra
  pregunta).

Lo descartado se registra con motivo, no se tira. El precedente es la
generación U6: 14 de 39 preguntas generadas fueron descartadas por la
validación de anclas a lo largo de 4 rondas (39 generadas, 25 aptas; descartes
10 + 3 + 1 por ronda — fuente:
`data/experiment/exploracion/generacion/generacion_u6_registro.md`;
`grep -c '"id"' data/experiment/exploracion/generacion/generacion_u6_registro.md`
→ 39). Ese registro de descartes fue insumo de diagnóstico entonces y lo será
acá.

## 7. Métricas

**Primaria — determinística, sin juez: recall de gold en traza**, en dos
niveles:

- **Visto**: el nodo-gold apareció en resultados de `buscar_nodos`.
- **Consultado**: el nodo-gold recibió `ver_nodo` o llegó por `ver_vecinos`.

La brecha visto-sin-consultar no es ruido: es un modo de falla con nombre
propio — **selección post-búsqueda**, el nodo correcto aparece en los
resultados y el agente no lo abre (casos U6-003/012/020; fuente:
`data/experiment/exploracion/adjudicacion/notas_adjudicacion_u6.md`, mecanismo
4) — y se reporta como métrica separada, no subsumida en el recall.

**Secundaria — opcional y desacoplada: corrección de la respuesta final por
juez.** Solo si se lauda gastar en juez. La métrica primaria no lo necesita: se
computa por inspección determinística de la traza contra el gold resuelto. Esa
independencia del juez es una fortaleza de diseño del eje — el proyecto
documentó los límites del juicio automático, y una métrica de navegabilidad que
no depende de ningún veredicto LLM no hereda ninguno de esos límites.

## 8. Volumen, costo y secuencia

El volumen por estrato y el presupuesto de generación quedan como **preguntas
abiertas para el laudo de la unidad de implementación**, con estimación previa
obligatoria antes de gastar (patrón del proyecto: costo de API distinto de 0
solo con mandato y tope).

Secuencia:

1. La corrida de generación usa el **grafo vigente**
   (`data/experiment/grafo_v2/reensamblado_v3/kg.json` según
   `docs/tablero.md` §1).
2. El set resultante se **sella por commit antes de cualquier corrida de
   evaluación** — mismo régimen que todo eval set del proyecto.
3. El set sellado alimenta **EV2 (issue #4) como su eje de navegabilidad**.

Relación con EV2: este pipeline es una de las dos patas del set sellado; la
otra es el generador ciego desde PDFs (el eje de fidelidad, heredero del patrón
U6). EV2 se compone de ambos ejes, cada uno con su métrica y su reporte, sin
mezcla (§4).

## Referencias

- deepeval Synthesizer — patrón de goldens y evolutions:
  https://deepeval.com/docs/synthesizer-introduction
- Mapa de territorio quemado y validador de anclas:
  `data/experiment/exploracion/mapa_territorio_quemado_5TOs_4sets.json`,
  `data/experiment/exploracion/validar_anclas.py`
- BKL-0027 (`data/backlog/backlog.jsonl`) — asimetría direccional de
  `ver_vecinos`, fundamento del sub-estrato de aristas entrantes de E-B.
- Casos U6-003/008/009/010/011/012/020 y los mecanismos causales de
  `data/experiment/exploracion/adjudicacion/notas_adjudicacion_u6.md` —
  fundamento de los estratos C y D y de la métrica de selección post-búsqueda.
