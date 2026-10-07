# Registro de las reuniones de mentores del 18 y el 19/08/2026

Registro de las decisiones de diseño de la evaluación tomadas en las dos reuniones, extraídas de mis notas contemporáneas.
Rige la convención del proyecto: cero nombres propios de personas; cada decisión se documenta por su justificación técnica y
se atribuye a la reunión, no a uno de los asistentes. Complementa (no reemplaza) el plan (`docs/plan_tesis.md`): este registro
dice qué se acordó; qué hizo el plan con cada acuerdo y qué desvíos quedan se decide aparte, por laudo. Se redacta siete
semanas después de las reuniones porque no tenían registro versionado (verificación del 06/10/2026, VERIF-DISENO-EVAL,
tarea 2: ni acta ni mención en `docs/` ni en los mensajes de commit de esa semana).

**Fechas:** 18/08/2026 y 19/08/2026 (las de mis notas; coherentes con el plan v2 y v3 del 18/08, `95a5534`, `132a830` y
`4859784`, y con los dos relevamientos del leaderboard MTEB del 18 y el 19/08 en `docs/decision_modelo_embeddings.md:21-25`).
**Asistentes, por rol:** 18/08: la autora y los mentores; 19/08: la autora y los mentores. **Modalidad:** reunión.

**Material presentado:** ninguno; reuniones de diseño.

La comparación de modelos del extractor no se trató en estas reuniones; su origen es la decisión de la autora del 05/10/2026
(`1d8fe9f`).

## 1. Comparación cara a cara con una recuperación tradicional

**D1 — Comparar el grafo con un sistema de recuperación por fragmentos con embeddings, y hacerlo pronto.** Dos agentes:
uno con el grafo disponible y otro con un índice de embeddings tradicional. Se hace sí o sí y temprano: si el sistema por
fragmentos rinde más que el grafo, la comparación muestra por dónde mejorar el grafo, y conviene saberlo durante el
desarrollo y no al final.
Palabras clave: «evaluación head to head con un RAG tradicional»; «embeddings tradicionales»; «avanzar con eso sí o sí»;
«mejor notarlo ahora que más adelante».

**D2 — Los agentes que evalúan el grafo son agentes nativos de Claude Code, para esta evaluación y para todas.** Se deja de
usar el harness propio. Cada agente se instancia con `claude -p` (el proceso recibe el mensaje, responde y termina; no abre
una sesión interactiva). Los agentes se pueden predefinir; se eligió `claude -p` en lugar de los subagentes por la
preocupación del aislamiento. El agente que tiene el grafo puede usar las herramientas nativas de
Claude Code, que buscan por palabras clave y que un agente usa bien, probando consultas distintas. Justificación: el harness
de Claude Code es una base de harness más fuerte que la propia y es configurable.
Palabras clave: «dejar de usar mi harness propio»; «tools nativas de claude code»; «claude -p»; «para esta evaluación y
todas»; «hacer todos agentes donde estoy evaluando al grafo nativos de claude code».

**D3 — Aislamiento de contexto verificado, configurado desde la documentación.** Antes de armar los agentes se lee la
documentación de Claude Code para configurar el aislamiento, que no viene por defecto: se tiene que poder afirmar que el
agente del sistema por fragmentos no accede al grafo, y que el del grafo no accede al índice.
Palabras clave: «isolated context»; «no viene de fábrica»; «estar literalmente seguros de que el RAG común no pueda
acceder al grafo»; «leer bien la documentación».

**D4 — Un solo agente y un solo prompt; el brazo es una variable declarada.** Si el brazo del grafo usara el agente propio
y el brazo por fragmentos otro agente, la comparación mediría dos agentes y no dos representaciones. Se resuelve con un
solo agente y un solo prompt, y lo que cambia entre brazos es el servidor MCP que se enchufa (el del grafo o el del índice
vectorial). El prompt es un argumento: un archivo de instrucciones por agente, que arma el agente que orquesta, o un texto
largo pasado como argumento de `claude -p`. En la tesis se reporta el harness fijo más el prompt propio declarado.
Palabras clave: «el brazo pasa a ser una variable declarada»; «el prompt es un argumento»; «el harness va fijo»;
«reportar que estoy usando el harness más el pedazo de prompt custom».

**D5 — Los dos brazos usan la misma segmentación: la de E0.** El índice vectorial se construye sobre los mismos fragmentos
de E0 que usa el grafo; la decisión de segmentación es una sola para los dos.
Palabras clave: «chunking: tomar la misma decisión para los dos, eso ya es el E0»; «índice vectorial sobre los mismos
chunks de E0».

**D6 — El modelo de embeddings se elige con criterio y se configura desde la model card de sus autores.** Se parte del
leaderboard MTEB (`huggingface.co/spaces/mteb/leaderboard`) filtrado por lo que hace falta: retrieval, español o
multilingüe, tamaño que entre en la máquina y modelos abiertos; se busca el mejor en general para su tamaño, no uno bueno
en una tarea puntual, porque el ranking cambia todos los meses. La búsqueda en el ranking puede ser asistida por un agente,
al que se le pasa el enlace del leaderboard para que ayude a filtrar (se mencionó como ejemplo la colección
Qwen3-Embedding, con la salvedad de que su elección no era reciente). Lo que no se delega es la configuración: sale de la
model card original de los autores, que tiene detalles de uso sin los cuales el modelo no funciona bien; no se usa un
valor por defecto ni se deja que un agente la fije.
Palabras clave: «MTEB leaderboard»; «el mejor en general … que domina para su tamaño»; «solo abiertos»; «entrar sí o sí a
la modelcard de los autores»; «no setear como default el modelo de embeddings»; «no dejes que claude code invente eso».

**D7 — Embeddings también sobre los nodos del grafo.** Se pueden agregar, con el mismo motor de embeddings que el índice
de fragmentos.
Palabras clave: «embeddings para los nodos se puede, agregarlos»; «un motor de embeddings igual para la comparación».

**D8 — Reportes de cada evaluación armados desde las trazas.** Se planteó como deseable, no como requisito: además de las
métricas, un agente toma las trazas de las evaluaciones hechas con Claude Code y arma un reporte prolijo, utilizable en la
tesis.
Palabras clave: «armar reportes prolijos»; «un agente que agarre las trazas y que arme un reporte».

## 2. Evaluación del contenido del grafo por tripletas

**D9 — Precisión: un gold de 100 tripletas etiquetado por la autora.** Cada tripleta se presenta como nodo, relación,
nodo y evidencia (el texto de donde se extrajo), y lleva dos juicios: si es correcta según la evidencia y qué tan
importante es para estar en el grafo. Se empieza por 10 para comprobar que la tarea se puede hacer, y se sigue de a 10
hasta 100. Ese conjunto es el gold de referencia.
Palabras clave: «evaluar unas 100 tripletas y este es mi recontra gold»; «empiezo por 10»; «de a 10»;
«nodo-relación-nodo-evidencia»; «CORRECTO» e «IMPORTANCIA».

**D10 — Un juez LLM hace la misma tarea y se calibra contra la autora.** El juez etiqueta las mismas tripletas; si el
acuerdo con la autora alcanza, se usa el juez para escalar la precisión y la importancia.
Palabras clave: «calibración de un LLM juez para que haga este trabajo con las primeras que adjudico yo»; «agreement».

**D11 — Cobertura (recall) por ranking de importancia.** Se toman fragmentos chicos al azar, donde un LLM extrae con más
precisión (un párrafo regulatorio rara vez tiene más de cinco cláusulas, y como mucho unas diez tripletas). Un LLM extrae de
cada fragmento la tripleta más importante, la que no puede faltar en un grafo de regulación. Otro LLM ordena todas por
importancia. La autora calibra las primeras 100 y revisa el orden. Después se busca, de arriba hacia abajo, cuáles están en
el grafo: es una evaluación de ranking (recall en las primeras k). Las que no están se revisan a mano después: si no son
importantes, no cuentan.
Palabras clave: «RECALL»; «pedazos random más chicos»; «la tripleta más importante … que no puede faltar en un KG de
regulaciones»; «ordenar de más importante a menos»; «calibración de las primeras 100 con humanos y chequear el orden»;
«recall at»; «evaluación humana post hoc».

**D12 — Etiquetado asistido y clasificación por experticia.** El pipeline de etiquetado también se arma con Claude Code: el
LLM propone la tripleta con la información o los enlaces para comprobarla, y la autora confirma con sí o no. El LLM además
clasifica las tripletas por dificultad y categoría: las que la autora puede etiquetar y las que necesitan a alguien que sepa
más del dominio.
Palabras clave: «etiquetado sugerido con LLM y aceptado con verificador humano»; «darte la información o links para que yo
pueda ver si es verdad o no»; «categorizar … las que puedo hacer yo y las que necesitan que alguien que sepa más».

## 3. Los dos grafos y las tareas extrínsecas

**D13 — Dos grafos: el que se evalúa y el corregido después.** La versión científica reporta el grafo tal como se evaluó y
no lo cambia. La tesis tiene dos contribuciones: el método para construir el grafo, con resultados sinceros de cuánto
rinde, y el grafo como entregable; para la segunda se puede corregir, después de evaluar, lo que la evaluación mostró, y
declararlo como posterior. Quedan dos grafos: el anterior a la evaluación, que es el evaluado, y el de uso industrial, el
mejor posible.
Palabras clave: «hay dos versiones del grafo»; «la versión científica es reportarlo y no cambiarlo»; «POST EVALUACIÓN
hice esto»; «el de antes de evaluar (el que se evalúa) y el de carácter industrial».

**D14 — La tesis muestra el grafo en tareas extrínsecas.** Además de evaluar el contenido del grafo, la tesis muestra si un
agente responde mejor con él.
Palabras clave: «mostraría sí o sí el grafo también en tareas extrínsecas».

## 4. Otros puntos tratados, sin decisión numerada

- Datos sintéticos para evaluar un sistema de preguntas: de un párrafo, un LLM propone preguntas y otro genera la respuesta,
  que queda como gold. Es lo que ya se hace en la evaluación extrínseca de desarrollo (EV2 y los pares sintéticos).
- La evaluación intrínseca no se hace a mano como vía principal: el contenido es muy específico y la anotación humana masiva
  no escala. El humano queda como referencia para calibrar (D9 y D10).
- Grafos de partes chicas de un documento, que serían más precisos y completos, con la pregunta de si lo que tienen está en
  el grafo completo: es el origen de la vía de cobertura de D11.
- Muestrear al azar una fracción del grafo (por ejemplo, un 10 %) para la precisión: se fijó en 100 tripletas (D9).

## 5. Dónde quedó registrada cada decisión en el plan (solo la ubicación; el estado y los desvíos se deciden aparte)

| decisión | fila o principio del plan | commit del registro |
|---|---|---|
| D1 | A2.0 a A2.3 (`:331-337`); B6.3 (f) (`:773`) | `95a5534` (18/08); laudos del 20/09 en `e58d41d` |
| D2 | A2.0-banco (iii) (`:332`); principio 8 (`:270-276`) | `95a5534`, `132a830` (18/08) |
| D3 | A2.0-banco (iv) (`:332`); A2.1 (`:335`) | `95a5534`; banco en `1fa79de` |
| D4 | A2.0-banco (iii) (`:332`); M-21 (`:1277`) | `95a5534`; banco en `1fa79de` |
| D5 | A2.1 (`:335`); A2.0-banco (ii) (`:332`) | `95a5534`; banco en `1fa79de` |
| D6 | A2.0b (`:334`); `docs/decision_modelo_embeddings.md` | `df9da34` (23/08) |
| D7 | B1.10 (`:369`) | `95a5534` |
| D8 | A2.0-reportes (`:333`) | `4859784` (18/08) |
| D9 a D12 | B4 (`:412-459`); D-b (`:961`); laudo D-f (`966253e`) | `87db24c` (23/08) |
| D13 | principio 9 (`:277-284`) | `87db24c`; nombres en `e58d41d` |
| D14 | B6.3 (b), (c), (e), (f) (`:773`) | `966253e` (27/08, B6.3 como evaluación final); (e) y (f) en `e58d41d` |

Confirmación de la autora: 07/10/2026.
