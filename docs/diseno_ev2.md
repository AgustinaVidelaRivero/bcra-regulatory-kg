# Diseño de EV2 — set sellado de medición de la re-extracción (issue #4)

Documento de diseño. No genera preguntas ni autoriza corridas: define la
composición, las cohortes, el gold, el protocolo de sellado y las métricas del
set EV2, y deja las decisiones de volumen y método de evaluación como preguntas
abiertas para laudo (§8). Todo número citado lleva la ruta o el comando que lo
reproduce.

---

## 1. Objetivo y rol en la secuencia

EV2 es el set sellado que mide la re-extracción. La medición central (issue
#10) compara tres sistemas sobre este set: el grafo v2-reextraído (pipeline de
`docs/diseno_reextraccion_v2.md`), el grafo v3 vigente
(`data/experiment/grafo_v2/reensamblado_v3/kg.json`, 4.469 nodos / 8.073
aristas post-C7, sha256 `26fac8b4…`; `docs/tablero.md` §1) y el baseline
congelado.

Regla de secuencia no negociable: **EV2 se genera, se valida y se SELLA POR
COMMIT antes de que exista el grafo v2** — el examen antes que el examinado. La
corrida de la re-extracción (issue #9) queda gateada por ese sellado, como ya
lo declara `docs/diseno_reextraccion_v2.md` §6. La lección viene del material
quemado del proyecto (EV1/CQ/CQN/CQN2): un eval set conocido durante el
desarrollo deja de servir como medición. Simétricamente, la generación de EV2
no puede ver ningún output del pipeline v2 — que a esa altura no debe existir
(§6).

## 2. Composición: dos ejes

EV2 se compone de dos ejes ortogonales, cada uno con su métrica y su reporte,
sin mezcla. Responden preguntas distintas y no se sustituyen.

**Eje de FIDELIDAD (desde el corpus).** Mide si lo que la norma dice está en
el grafo y es respondible. Generación ciega heredera del protocolo U6
(`docs/protocolo_u6.md`): una instancia aislada que recibe solo los PDFs
congelados (`data/experiment/subset/`, sha256 verificados antes de generar,
igual que en U6 §4), con semillas declaradas y registro de descartes, y con el
mismo síntoma de diseño — preguntas naturales ancladas a punto normativo
exacto, producidas sin ver el grafo ni las evaluaciones previas. La disciplina
de blind eval generation del protocolo U6 se hereda entera.

**Eje de NAVEGABILIDAD (desde el grafo).** Mide si lo que está en el grafo es
alcanzable por el agente. Es el pipeline de queries sintéticas de
`docs/diseno_queries_sinteticas.md`, con sus cinco estratos (E-A a E-E), su
gold por anclas de provenance invariante entre grafos, y sus pares
literal/anti-léxica. Su limitación declarada — no detecta ausencias — es
exactamente lo que el eje de fidelidad cubre.

Regla de derivación entre ejes (heredada de `docs/diseno_queries_sinteticas.md`
§4): el censo previo por grafo verifica, antes de correr, si el gold de cada
caso sintético existe en cada grafo. Un caso cuyo gold no existe en un grafo se
registra como **ausencia de ese grafo** — dato de fidelidad — y se excluye de
la métrica de navegabilidad de ese grafo. Un grafo al que le falta el
contenido no "falla navegación": le falta el contenido, y confundir las dos
cosas invalidaría la comparación.

## 3. Cohortes y contaminación controlada

EV2 distingue dos cohortes que se generan, se etiquetan y se reportan por
separado.

**Núcleo limpio.** Compuesto por:

- las preguntas del eje de fidelidad ancladas en **territorio virgen fresco**:
  sin cruce con las anclas de EV1/CQ/CQN/CQN2 ni con las 25 anclas de U6
  (que quedaron quemadas al usarse, `docs/protocolo_u6.md` §9), validado
  mecánicamente contra el mapa de territorio
  (`data/experiment/exploracion/mapa_territorio_quemado_5TOs_4sets.json`)
  extendido con U6 como quinto set;
- el **estrato uniforme E-E** del eje sintético — territorio muestreado sin
  mirar el historial de fallas.

**El veredicto de mejora de v2 descansa EXCLUSIVAMENTE en el núcleo limpio.**

**Cohorte dirigida** (etiquetada, reportada aparte). Compuesta por:

- las **25 preguntas de U6 ya adjudicadas** como regression tests, con su
  adjudicación humana sellada en el commit `b337152` (7 correctas / 15
  parciales / 3 incorrectas;
  `data/experiment/exploracion/adjudicacion/u6_adjudicacion_humana.jsonl`,
  25 líneas: `wc -l` sobre el archivo). Esto resuelve la pregunta abierta
  §7.c de `docs/diseno_reextraccion_v2.md`: las U6 no se absorben como gold
  semilla del núcleo — entran como cohorte dirigida separada;
- los **estratos dirigidos E-A/E-B/E-C/E-D** del eje sintético, derivados de
  modos de falla documentados (asimetría direccional BKL-0027, enumeración
  sobre hubs, cuasi-duplicados con variación);
- los **tests de respuesta conocida del backlog**
  (`docs/diseno_reextraccion_v2.md` §5): BKL-0024 contra el censo E2, la
  familia chapeau contra la herencia E0, los portadores de la cláusula del
  125 % contra la anti-fusión E4, las amputaciones BKL-0003/0004/0005 contra
  el verificador E3, y los re-tests C1–C7
  (`data/backlog/retests/C{1..7}_retest_*.md`).

Justificación de la separación: el pipeline v2 se diseñó desde los mecanismos
de falla que estas cohortes codifican — el chunking con herencia desde el
mecanismo chapeau, el censo desde BKL-0024, la anti-fusión desde U6-008, el
verificador desde las amputaciones del backlog. La cohorte dirigida mide si
los mecanismos conocidos se resolvieron, no la calidad general del grafo:
promediarla con el núcleo limpio inflaría el delta por construcción — sería
evaluar al alumno con las preguntas que motivaron su plan de estudio (el
argumento es el mismo que fundamenta el estrato E-E en
`docs/diseno_queries_sinteticas.md` §3).

## 4. Dosificación del eje de fidelidad

El territorio disponible para generación fresca es de **167 unidades, el
67,9 % del inventario de 246** (167/246 = 67,9 %; fuente:
`python3 -c "import json; print(json.load(open('data/experiment/exploracion/mapa_territorio_quemado_5TOs_4sets.json'))['totales'])"`
→ `disponibles: 167`, `unidades: 246`, `pct_tocado: 32.1`), menos las anclas
U6 que la regeneración del mapa incorpore como quinto set (§3).

Regla laudada: **dosificación proporcional al tamaño y a la virginidad por
TO**. Exterior y Cambios — el TO más grande y más virgen (100/116 unidades
disponibles, 13,8 % tocado; fuente: clave `por_to.ext.conteos` del mismo
mapa) — pesa más, igual que en la dosificación U6 (`docs/protocolo_u6.md`
§3). Los números exactos por TO quedan como pregunta abierta para la unidad
de generación (§8.a), con la proporcionalidad como regla ya laudada acá.

Las unidades parcialmente quemadas siguen el régimen del protocolo U6 §2:
disponibles con precaución, con validación mecánica contra la tabla de anclas
internas del mapa (patrón `validar_anclas.py`) y descarte-y-regeneración de
toda candidata cuya ancla caiga en material quemado o lo abarque.

## 5. Gold del eje de fidelidad: anclas + criterios

Cada pregunta del eje de fidelidad lleva:

- el **ancla normativa exacta** (TO + punto), y
- una **lista de criterios verificables** que la respuesta debe satisfacer:
  los elementos que debe contener, cada uno con su cita textual del PDF.

**NO se redacta respuesta esperada en prosa.** Justificación: el gold fuerte
redactado exige adjudicación humana por caso — el precedente U6 costó una
semana de trabajo por 25 preguntas aptas (`docs/diseno_queries_sinteticas.md`
§1) y su adjudicación requirió el expediente completo sellado en `b337152`.
Las anclas + criterios, en cambio:

- son **generables por la misma instancia ciega** que produce la pregunta
  (tiene el PDF a la vista; declarar qué elementos del punto debe contener la
  respuesta no exige más ceguera que declarar el ancla);
- son **validables mecánicamente**, extendiendo el patrón de
  `data/experiment/exploracion/validar_anclas.py`: cada criterio debe anclar
  a texto real del PDF en el punto declarado — un criterio cuya cita no
  aparece en el fuente descarta la candidata;
- son **evaluables después** por cualquiera de los dos métodos en discusión:
  juez calibrado con ejemplos resueltos (siguiendo el hallazgo H12 citado en
  `docs/diseno_reextraccion_v2.md` §3-E3) o adjudicación humana selectiva.

La decisión del método de evaluación de respuestas es de la unidad de corrida,
no de este documento (§8.c); el set debe servir a cualquiera de los dos, y el
formato anclas + criterios es el que lo garantiza.

## 6. Protocolo de sellado

**Un solo commit sella**, en un mismo estado del árbol:

1. las dos patas del set completo — preguntas de ambos ejes con sus goldens
   (anclas + criterios en fidelidad; anclas de provenance en navegabilidad);
2. las varas: los criterios verificables por pregunta;
3. el protocolo de corrida: orden de ejecución, repeticiones por pregunta,
   topes de costo;
4. los sha256 de todos los artefactos anteriores.

La generación deja **registro con semillas y descartes** — precedente:
`data/experiment/exploracion/generacion/generacion_u6_registro.md` (39
candidatas, 25 aptas, descartes con motivo por ronda).

Después del sellado el set **no se edita**: toda desviación se documenta como
enmienda separada, nunca como ajuste silencioso (mismo régimen de válvula que
`docs/protocolo_u6.md` §8). Dos gates temporales cierran el protocolo:

- **ninguna corrida de evaluación ocurre antes del commit de sellado**, y
- **la generación del set no puede ver ningún output del pipeline v2** — que a
  esa altura no debe existir, porque la corrida de la re-extracción (issue #9)
  está gateada por este mismo sellado (§1).

## 7. Métricas y reporte

Por eje, sin mezcla:

- **Fidelidad** → cumplimiento de criterios por pregunta: qué fracción de los
  criterios verificables satisface la respuesta del sistema. La evaluación es
  por juez calibrado con ejemplos resueltos o por adjudicación humana
  selectiva — a laudar en la unidad de corrida (§8.c).
- **Navegabilidad** → las métricas de `docs/diseno_queries_sinteticas.md` §7:
  recall determinístico de gold en traza en dos niveles (**visto** en
  `buscar_nodos` / **consultado** vía `ver_nodo` o `ver_vecinos`), la
  **brecha de selección post-búsqueda** como métrica separada, y el **delta
  literal/anti-léxica** del diseño apareado, con el solape léxico como
  variable continua por pregunta.

El reporte se estructura **por cohorte** (núcleo limpio vs. dirigida — el
veredicto de mejora sale solo del núcleo, §3), **por grafo** (v2-reextraído,
v3, baseline congelado, con las ausencias de cada grafo reportadas en el eje
de fidelidad según la regla del §2), y con **contabilidad completa de costos**
(generación, validación, corrida, evaluación), con tope declarado ex ante —
el mismo compromiso de reporte de costos que `docs/diseno_reextraccion_v2.md`
§6 declara como parte del aporte.

## 8. Preguntas abiertas para laudo

- **(a) Volúmenes**: cantidad de preguntas por eje y, dentro del eje de
  fidelidad, por TO (con la proporcionalidad del §4 como regla ya laudada);
  presupuesto de generación con estimación previa obligatoria antes de gastar.
- **(b) Repeticiones por pregunta en la corrida**: el proyecto documentó
  no-determinismo a temperatura 0 y usa N=3 en casos de frontera; cuántas
  reps por pregunta paga la medición central es decisión de costo a laudar.
- **(c) Método de evaluación del eje de fidelidad**: juez calibrado con
  ejemplos resueltos, adjudicación humana selectiva, o mixto por muestreo
  (juez en todo + adjudicación humana sobre una muestra para validar al juez).

---

## Referencias

- `docs/diseno_reextraccion_v2.md` — pipeline v2 (E0–E5), backlog como
  especificación y batería de pruebas (§5), gating por EV2 (§6), pregunta
  abierta §7.c que este documento resuelve (§3).
- `docs/diseno_queries_sinteticas.md` — eje de navegabilidad: estratos,
  gold por provenance, censo previo (§4), pares literal/anti-léxica,
  métricas determinísticas (§7).
- `docs/protocolo_u6.md` — protocolo heredado del eje de fidelidad:
  generación ciega solo-PDFs, validación mecánica de anclas, dosificación
  por territorio, régimen de válvula.
- `data/experiment/exploracion/mapa_territorio_quemado_5TOs_4sets.json` —
  mapa de territorio quemado/disponible (246 unidades, 167 disponibles).
- `data/experiment/exploracion/adjudicacion/` — adjudicación humana U6
  sellada en `b337152` (25 casos: 7 correctas / 15 parciales / 3
  incorrectas), laudos №0–5 y notas pre-registradas.
- `data/experiment/exploracion/generacion/generacion_u6_registro.md` —
  precedente del registro de generación con semillas y descartes.
