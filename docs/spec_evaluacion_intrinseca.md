# Spec pre-registrada — Evaluación intrínseca del grafo

**Estado:** pre-registro. Este documento se sella por commit ANTES de que exista
`scripts/metricas_intrinsecas.py` o cualquier otra implementación de sus métricas.
**Escrituras de esta spec:** este archivo y una entrada en `docs/INDICE.md`.
**Valores:** este documento no contiene ningún valor de ninguna métrica para ningún
grafo del proyecto. Toda cifra que aparece es un valor publicado de la literatura,
con puntero a PDF y a tabla o sección.

**Convención de citas** (la del repo, `docs/literatura/README.md`): los papers se
referencian por su número de índice. En este documento:

- **[00]** — *RAGulating Compliance* (arXiv:2508.09893, 2025) —
  `docs/literatura/papers/00_ragulating_compliance.pdf`.
- **[05]** — *CORE-KG* (arXiv:2506.21607, 2025) —
  `docs/literatura/papers/05_core_kg_smuggling.pdf`.
- **[06]** — *LINK-KG* (arXiv:2510.26486, 2025) —
  `docs/literatura/papers/06_link_kg_smuggling.pdf`.

---

## 1. Propósito y alcance

Este documento pre-registra el set de métricas de evaluación intrínseca del grafo de
conocimiento regulatorio: las propiedades del artefacto medidas sobre el artefacto
mismo, sin pasar por la tarea. Define cada métrica con fórmula, numerador,
denominador, convención de cómputo, tipo de cota y rol en el gate, y pre-registra
(sección 7) las predicciones que la primera medición va a verificar.

**Qué no es.** No reemplaza la evaluación extrínseca. La selección del grafo ganador
de la fase comparativa se hizo a través de la tarea (harness KG-RAG + juez), y la
capacidad del sistema de responder preguntas se sigue midiendo por esa vía. Las
métricas intrínsecas de este set cumplen otra función: caracterizar el artefacto,
detectar regresiones estructurales baratas de medir, y —motivación directa de este
documento— exponer modos de falla del ensamblado que la evaluación por tarea detecta
tarde y caro.

**Relación con la propuesta de proyecto.** La propuesta (`docs/ppf/main.tex`, sección
de evaluación) promete "métricas de calidad estructural del grafo (densidad,
conectividad, ratio de duplicación) y cobertura de *Competency Questions* definidas a
priori". Este set las cumple: densidad es M8, conectividad se cubre con M4/M5/M6/M9,
ratio de duplicación con M1/M2 (y su espejo M3, que la propuesta no pedía y este
documento agrega por la regla constitucional de la sección 2), y cobertura de CQ con
M11, bajo el régimen especial de la sección 6.

**Orden de sellado.** Declaro explícitamente: este documento se sella por commit antes
de que exista su implementación. Si el código que calcula estas métricas existiera
antes que este documento, el pre-registro de la sección 7 no valdría nada — las
predicciones serían lecturas disfrazadas de apuestas. El commit que selle este archivo
antecede a `scripts/metricas_intrinsecas.py` en el historial del repo, y esa
precedencia es verificable por `git log`.

**Grafos en alcance.** Las mediciones de la pasada 1 (sección 8) se corren sobre el
grafo con el defecto de ensamblado (`data/experiment/grafo_v2/kg.json`) y el grafo
re-ensamblado (`data/experiment/grafo_v2/reensamblado_v3/kg.json`), que son el par
sobre el que las predicciones de la sección 7 están formuladas. Las definiciones son
aplicables a cualquier `kg.json` del proyecto con estructura
`{nodes: [{id, type, label, properties, provenance}], edges: [{source, target,
relation, provenance}]}`.

---

## 2. Regla constitucional del set

Dos reglas de admisión. Ninguna métrica entra al set si las viola.

**(a) Pareo.** Toda métrica de fusión va acompañada de su espejo. Una métrica de
sub-fusión (duplicación: dos nodos que deberían ser uno) sin su métrica de
sobre-fusión (conflación: un nodo que debería ser dos) es inadmisible en este set. El
motivo es deductivo y está desarrollado en la sección 3: optimizar contra una sola de
las dos direcciones empuja el sistema hacia la otra, y la métrica sola no puede verlo.

**(b) Denominador declarado.** Toda tasa declara numerador y denominador explícitos, y
el denominador debe estar aguas arriba de la transformación que la métrica evalúa. Una
tasa calculada sobre el resultado de la transformación que se quiere auditar no mide
nada: si la transformación descarta registros, el denominador se achica junto con el
numerador y la tasa se conserva impecable mientras el daño crece. El antecedente
concreto está en la sección 3.

Aplicación honesta de (b) a este mismo set: M1 y M2 normalizan por nodos totales del
grafo — un denominador aguas abajo de la fusión — porque esa es la fórmula del
protocolo publicado que adoptan (ver sección 4). Esa herencia queda declarada como
límite conocido de ambas filas, y lo que impide el punto ciego no es su denominador
sino el pareo con M3, cuyo denominador (menciones extraídas) sí está aguas arriba. Las
métricas nuevas de este set que auditan una transformación (M3, M10) cumplen (b) de
forma directa.

---

## 3. Antecedente que motiva la regla

**El caso de la regla (b), en términos mecánicos.** El chunker del pipeline corta el
texto en cada aparición de un punto numerado. En los Textos Ordenados del BCRA la
misma numeración aparece hasta en tres regiones distintas del documento: el índice del
principio, el articulado del cuerpo, y la tabla "norma de origen" del final. La clave
`{doc}::{numbering}` no identifica entonces un pasaje sino hasta tres. El ensamblado
original resolvía la colisión con un desempate por conteo ("sobrevive el chunk que más
entidades extrajo"), que premia sistemáticamente a la tabla de referencias cruzadas —
una lista de códigos de Comunicación, densa en strings extraíbles — por encima del
articulado, que es prosa normativa. Sobre ese resultado se calculaba una métrica de
cobertura por documento cuyo denominador eran los chunks sobrevivientes del desempate.
La métrica reportaba valor máximo: cada sobreviviente aportaba nodos. El articulado
descartado — el contenido normativo que el grafo existe para representar — no estaba
en el denominador, así que su pérdida era invisible para la métrica exacta que decía
medir cobertura. El denominador correcto eran los registros de entrada (los chunks que
entraron a extracción), no los sobrevivientes de la transformación auditada. M10 es la
métrica que este episodio exige, y la regla (b) es su generalización.

**El argumento de la regla (a), que es deductivo.** Sea un grafo donde una operación
de fusión colapsa nodos que no debían colapsarse (sobre-fusión). La operación reduce
el conteo de nodos y conserva las aristas, que se re-anclan en los nodos fusionados.
De ahí se siguen, sin hipótesis empírica alguna, tres consecuencias:

1. **Baja el conteo de duplicados.** Los pares que una métrica de duplicación habría
   marcado como redundantes ya no existen como pares: son un solo nodo. La métrica de
   sub-fusión mejora.
2. **Sube la relación aristas/nodos.** El numerador (aristas) se conserva y el
   denominador (nodos) cae. Toda métrica de conectividad media mejora.
3. **Se acortan los caminos medios.** Los nodos fusionados concentran las aristas de
   todos sus constituyentes y se vuelven hubs; los caminos que antes requerían varios
   saltos ahora atraviesan el hub. Toda métrica de distancia media mejora.

Es decir: un defecto grave (fundir una norma general con su versión de alcance
restringido es exactamente el error que un grafo regulatorio no puede permitirse)
mueve las tres familias de métricas intrínsecas estándar en la dirección de "mejor
grafo". La conclusión de clase: **las métricas intrínsecas estándar para KGs
construidos con LLM están diseñadas contra la sub-fusión y son ciegas — o directamente
favorables — a la sobre-fusión**, porque la sobre-fusión no fue el problema de esa
literatura. En [05] y [06] el modo de falla dominante es la fragmentación de menciones
("Y.", "A.Y.", "Defendant" como tres nodos — [05] §3.2, [06] §I), y todo su aparato de
medición (node duplication rate) apunta contra ese modo. El corpus regulatorio de este
proyecto tiene el problema inverso: entidades normativas cuya distinción fina es el
contenido mismo del grafo.

La verificación empírica de esta inversión sobre los grafos de este proyecto está
pre-registrada en la sección 7 (predicciones P-a, P-b, P-c) y **pendiente de
medición**.

---

## 4. Catálogo de métricas

Convenciones estructurales usadas por las definiciones (verificadas por inspección de
estructura, sin conteos): los nodos portan `id`, `type`, `label`, `properties`,
`provenance` (`source_doc` + `location`); las aristas portan `source`, `target`,
`relation`, `provenance`; las aristas son dirigidas; la lista de aristas admite
repeticiones del mismo triple `(source, target, relation)`; el grafo re-ensamblado
porta además `rol_fuente` en nodos y aristas.

| id | nombre | definición formal | fuente | numerador | denominador | dirección de mejora | determinismo | tipo de cota | rol en el gate | dependencias |
|---|---|---|---|---|---|---|---|---|---|---|
| M1 | tasa_duplicacion_publicada | Protocolo de [05] §5.1 "Duplicate Node Detection", etapa 1 solamente: similitud `partial_ratio` de RapidFuzz entre pares de nodos del mismo `type` (sobre `label`); pares con similitud ≥ 75 forman un grafo de similitud no dirigido; clusters = componentes conexas; conteo = Σ sobre clusters de (\|C\|−1); tasa = conteo / nodos totales del grafo. | [05], §5.1 y Tabla 1 (protocolo y valores de referencia) | Σ(\|C\|−1) sobre los clusters de similitud | nodos totales del grafo (aguas abajo — herencia del protocolo publicado, declarada en §2) | menor (con la salvedad de §5.b: parte del numerador son falsas fusiones deseables de distinguir) | determinística en etapa 1; el protocolo publicado agrega una etapa 2 de adjudicación humana ([05] §5.1) que acá se difiere (§10) | SUPERIOR: la etapa 2 de [05] solo remueve falsos positivos, así que la etapa 1 sola nunca subestima el conteo del protocolo completo | descriptiva; DECLARADA INFLADA para este corpus (§5.b) | RapidFuzz; campo `type` y `label` de los nodos |
| M2 | tasa_duplicacion_gate | Misma fórmula que M1 (grafo de similitud intra-tipo, umbral 75, componentes conexas, Σ(\|C\|−1) / nodos totales), con la similitud reemplazada: `ratio` de RapidFuzz (Levenshtein normalizado sobre las cadenas COMPLETAS) tras normalización de superficie (minúsculas, sin tildes, colapso de espacios y puntuación), SIN dominancia de substring. | variante propia sobre el protocolo de [05] §5.1; el motivo del reemplazo está en §5.b | Σ(\|C\|−1) sobre los clusters de similitud | nodos totales del grafo (misma herencia declarada que M1) | menor | determinística | SUPERIOR (mismo argumento que M1: una adjudicación posterior solo removería falsos positivos) | BLOQUEANTE en la pasada 2 | RapidFuzz; campos `type` y `label` |
| M3 | tasa_conflacion | Espejo de M1 (regla (a) de §2): Σ sobre nodos del grafo de (menciones_fusionadas − 1), donde menciones_fusionadas es la cantidad de menciones extraídas que el ensamblado fundió en ese nodo; tasa = esa suma / menciones extraídas totales. | SIN FUENTE en la literatura revisada ([00], [05], [06] no la definen ni la aproximan). Aporte propio de este set. La literatura no la tiene porque su modo de falla era el inverso (§3): midió cuánto quedó sin fundir, nunca cuánto se fundió de más. | Σ(menciones_fusionadas − 1) sobre los nodos | menciones extraídas totales (aguas arriba de la fusión — cumple (b)) | menor | determinística dado el registro de menciones por nodo | SUPERIOR de sobre-fusión: parte de las fusiones contadas son legítimas (menciones realmente correferentes), así que el valor acota por arriba la sobre-fusión real | BLOQUEANTE en la pasada 2 | requiere conteos a nivel mención cuya fuente es la caché de extracción (`data/experiment/grafo_v2/code/cache_v2/`); esa dependencia queda PENDIENTE DE CONFIRMACIÓN (§10) |
| M4 | average_degree | Convención fijada acá y que no cambia después: las aristas se deduplican por triple exacto `(source, target, relation)`; el grado de un nodo = entrantes + salientes sobre las aristas únicas; los self-loops se conservan y aportan 2 al grado de su nodo; average_degree = Σ grados / nodos totales. Los self-loops y la cantidad de aristas repetidas removidas se reportan como anexos de la métrica. | convención propia; [00] Tabla 1 reporta "Average Degree" sin declarar convención — se usa solo como orden de magnitud (§5.a) | Σ de grados (2·aristas únicas) | nodos totales | sin dirección declarada: NO SE REPORTA NUNCA SIN M6 (un average_degree que sube puede ser un hub contaminado engordando) | determinística | exacta (propiedad del artefacto bajo la convención fijada) | descriptiva; restricción de reporte conjunto con M6 | ninguna externa |
| M5 | avg_shortest_path | Camino mínimo promedio no ponderado sobre la versión NO dirigida del grafo de aristas únicas, computado EXCLUSIVAMENTE sobre la componente conexa mayor; promedio sobre todos los pares ordenados de nodos distintos de esa componente. Los nodos fuera de la componente mayor se excluyen del cómputo y su magnitud se reporta vía M9 (obligatorio junto a M5). | convención propia; [00] Tabla 1 reporta "Avg. Shortest Path" sin declarar convención — solo orden de magnitud (§5.a) | Σ de distancias entre pares de la componente mayor | cantidad de pares de la componente mayor | sin dirección declarada: NO SE REPORTA NUNCA SIN M6 (§3: los hubs acortan caminos) | determinística | exacta (bajo la convención fijada) | descriptiva; restricción de reporte conjunto con M6 y M9 | M9 (identificación de componentes) |
| M6 | concentracion_de_grado | Tres estadísticos sobre la distribución de grados de M4: (i) grado máximo; (ii) participación del percentil superior 1% de los nodos en el grado total (suma de grados del techo(1%·N) de nodos de mayor grado / suma total de grados); (iii) coeficiente de Gini de la distribución de grados. | convención propia; motivada por la especie `hub_contaminado` del backlog (`docs/spec_backlog_refinamiento.md` §2, ej. documentado en `docs/casos_gate_cqn2.md` §(a).4) | (i) un grado; (ii) suma de grados del top 1%; (iii) Gini | (ii) suma total de grados; (i) y (iii) no son tasas | menor concentración como indicio favorable, sin gate: hay hubs legítimos en un corpus regulatorio (sujetos obligados genuinamente transversales) | determinística | exacta | descriptiva, pero de reporte OBLIGATORIO junto a M4 y M5 (ninguna de las dos se publica sin esta) | M4 (distribución de grados). **Especie del backlog: `hub_contaminado`** |
| M7 | tasa_ruido_por_rol | Nodos cuya provenance apunta a un chunk cuyo rol documental no es normativo, sobre nodos totales. Vocabulario de roles REAL del módulo `data/experiment/grafo_v2/code/chunk_roles.py`: `cuerpo`, `indice`, `tabla_norma_origen`. Rol normativo = `cuerpo` (el módulo no usa la palabra "normativo"; la equivalencia se fija acá). Numerador = nodos con rol ∈ {`indice`, `tabla_norma_origen`}. | protocolo de ruido de [05] §5.1 "Noise Detection" y [06] §IV.D, reformulado: en ambos papers la métrica exige validación manual de un experto de dominio; acá el rol del chunk de origen es una propiedad derivable del pipeline, lo que convierte una métrica de juicio experto en una métrica REPRODUCIBLE. Dejo constancia de esa conversión como propiedad del diseño, no como equivalencia semántica exacta. | nodos con rol de origen no normativo | nodos totales del grafo | menor | DETERMINÍSTICA (esta es la conversión señalada: en [05]/[06] requiere experto; acá no) | INFERIOR: no captura nodos vacíos de semántica provenientes de chunks normativos (cáscaras nacidas del cuerpo del texto), así que subestima el ruido total | BLOQUEANTE en la pasada 2 | en el grafo re-ensamblado, campo `rol_fuente` de cada nodo; en el grafo con el defecto, atribución nodo→chunk vía la caché de extracción (misma dependencia pendiente que M3) + `chunk_roles.py`. **Especie del backlog: `cascara`** |
| M8 | densidad | Fórmula fijada acá y que no cambia: densidad de grafo dirigido simple = aristas únicas sin self-loops / (N·(N−1)), con N = nodos totales y aristas únicas según la deduplicación de M4. Los self-loops se excluyen del numerador (el denominador cuenta pares ordenados de nodos distintos). | fórmula estándar de densidad dirigida; la elección de variante (dirigida, sin self-loops, sobre aristas únicas) es convención propia fijada acá. Cumple la promesa explícita de la propuesta (`docs/ppf/main.tex`, sección de evaluación) | aristas únicas sin self-loops | N·(N−1) | sin dirección declarada (por §3: la sobre-fusión la sube) | determinística | exacta | descriptiva | convención de deduplicación de M4 |
| M9 | nodos_aislados y componentes_conexas | Sobre la versión no dirigida del grafo de aristas únicas: (i) cantidad de nodos con grado 0; (ii) cantidad de componentes conexas; (iii) fracción de nodos en la componente mayor (nodos de la componente mayor / nodos totales). | convención propia; [00] Tabla 1 tiene una fila de secciones no conectadas que NO es citable ni como referencia (ver §5.c) | (i) y (ii) conteos; (iii) nodos de la componente mayor | (iii) nodos totales | menos aislados y mayor fracción en la componente mayor como indicio, sin gate (§7 P-e declara ramas en ambas direcciones) | determinística | exacta | descriptiva; reporte obligatorio junto a M5 | ninguna externa |
| M10 | chunks_mudos | Chunks normativos que no aportan ningún nodo al grafo, sobre chunks normativos totales. Chunk normativo = chunk de entrada a extracción cuyo rol documental es cuerpo (equivalencia fijada en M7). "No aporta ningún nodo" = ningún nodo del grafo ensamblado rastrea su provenance a ese chunk. Deslinde terminológico: el pipeline de ensamblado llama "roles activos" a {cuerpo, tabla_norma_origen} y reporta un campo chunks_mudos computado sobre ese universo con un criterio más débil (dejar cualquier rastro: nodo, arista o provenance agregada). M10 no es ese campo: su universo es exclusivamente cuerpo — solo al articulado normativo se le exige aporte — y su criterio es estricto (aporte de nodo). Los dos números pueden diferir legítimamente y no deben compararse. | métrica propia; es la que el antecedente de §3 exige — el denominador son los registros de ENTRADA, no los sobrevivientes de ninguna transformación posterior (cumple (b) por construcción) | chunks activos con aporte cero | chunks activos totales (aguas arriba del ensamblado) | CERO (todo chunk normativo debería aportar al menos un nodo; un chunk mudo es articulado no representado) | determinística | exacta dado el registro chunk→nodos | BLOQUEANTE en la pasada 2. Es la métrica que expone directamente el modo de falla que originó este documento | `chunks_all.json` de la extracción + `chunk_roles.py` (roles) + atribución nodo→chunk del ensamblado |
| M11 | cobertura_CQ | Para cada competency question del eval set: ¿el grafo contiene el material que responde la pregunta? (existencia de los nodos/aristas portadores de la respuesta, verificada por lectura). Cobertura = preguntas con material presente / preguntas del set. Régimen especial completo en §6. | promesa de la propuesta (`docs/ppf/main.tex`, sección de evaluación); metodología de CQ referenciada en la literatura del repo (README de `docs/literatura/`, paper 04) sin protocolo numérico adoptado de ella | preguntas cuyo material de respuesta existe en el grafo | preguntas del eval set (definido fuera del grafo — aguas arriba; cumple (b)) | mayor, pero SIN SEGUIMIENTO: se mide una sola vez (§6) | NO determinística: requiere juicio de lectura (qué nodos "responden" una pregunta); por eso su medición es única, documentada pregunta por pregunta | sin cota declarada (es una lectura, no un estimador de un protocolo mayor) | descriptiva bajo el régimen especial de §6; JAMÁS bloqueante sobre el set quemado | eval set (`data/experiment/evaluacion/queries/`); §6 fija cuál condición habilita seguimiento |

---

## 5. Comparabilidad con la literatura y límites de las definiciones adoptadas

### 5.a Declaración de NO comparabilidad numérica

Ningún valor que este proyecto mida con M1–M11 es comparable numéricamente con los
valores publicados en [00], [05] o [06]. Motivos, enumerados:

1. **Idioma del corpus.** Los tres papers trabajan sobre inglés; este proyecto sobre
   castellano rioplatense normativo. Las similitudes de superficie (M1/M2) y el
   comportamiento del extractor no trasladan.
2. **Dominio.** [05] y [06] procesan narrativa judicial de casos de tráfico de
   personas (secciones "Opinion" de fallos, ~2000 palabras por caso — [05] §4.1);
   [00] procesa el eCFR (regulación sanitaria federal de EE. UU.). Este proyecto
   procesa Textos Ordenados del BCRA: prosa normativa densa en obligaciones, no
   narrativa de hechos.
3. **Tamaño y unidad de los grafos.** Los grafos de [05] y [06] son POR CASO y de
   decenas a poco más de dos centenas de nodos: en [06], Tabla I (casos cortos), el
   promedio de entidades totales por caso es 69.57 (GraphRAG), 36.43 (CORE-KG) y
   34.71 (LINK-KG); en la Tabla II (casos largos), 143.56, 59.89 y 58.44, con máximo
   de caso individual de 214 (Case 16, GraphRAG). En [05], el caso representativo del
   Apéndice C pasa de 86 nodos (baseline) a 42 (CORE-KG). Los promedios publicados
   agregan sobre **20 casos** en [05] (§4.1, Tabla 1) y **16 casos** en [06] (§IV.A,
   Tablas I–II). Este proyecto mide UN grafo único cuyo orden de magnitud, según los
   reportes de fases previas del repo, es de miles de nodos — la cifra exacta está
   pendiente de medición (pasada 1). Tasas normalizadas sobre poblaciones de tamaños
   tan distintos no se comparan.

Los valores publicados se usan exclusivamente como **orden de magnitud de
referencia**, y toda comparación de este proyecto es **INTERNA entre sus propios
grafos** (defectuoso vs re-ensamblado, baseline vs refinado).

### 5.b Por qué `partial_ratio` está declarado inflado para este corpus

`partial_ratio` es una similitud dominada por substring: puntúa alto cuando una cadena
está contenida (aproximadamente) en la otra, sin castigo por el material no compartido.
En un corpus regulatorio, una norma general y su versión con alcance restringido
difieren exactamente en modificadores ("entidades financieras" / "entidades
financieras que operen en cambios"; una obligación y la misma obligación "para
operaciones de hasta..."). Bajo dominancia de substring esos pares obtienen similitud
alta y se fusionan en el cluster — y son justamente los nodos que este trabajo debe
mantener distintos, porque la distinción de alcance ES el contenido regulatorio.

Dos anclas para esta declaración:

- **El propio ejemplo de [05]** (§5.1, "Duplicate Node Detection"): menciones de un
  vehículo con adjetivos distintos — `white pickup truck`, `stolen white pickup
  truck`, `white older Ford pickup truck` — se agrupan en el mismo cluster como una
  sola entidad. Para narrativa judicial eso es correcto (es el mismo vehículo). Para
  este corpus, el comportamiento análogo (fusionar la norma con su variante
  adjetivada de alcance) es exactamente el error inadmisible. El mismo ejemplo que
  [05] presenta como éxito del protocolo es la demostración de por qué el protocolo
  no sirve acá.
- **Este proyecto ya midió el mismo modo de falla con otro instrumento:** el
  clustering por embeddings sobre vocabulario regulatorio en castellano de la fase de
  resolución de entidades produjo fusiones falsas guiadas por adjetivos de dominio
  (variantes con modificador de alcance agrupadas como una entidad). El modo de falla
  no es del fuzzy matching en particular: es de toda similitud de superficie o
  semántica aplicada a un vocabulario donde el modificador porta la carga normativa.

Conclusión que dejo escrita: **que el número publicado no sirva para este corpus es un
RESULTADO de este trabajo, no una limitación de la medición.** M1 se conserva en el
set precisamente para documentar esa inversión con datos propios (predicción P-b), y
M2 existe porque el gate necesita una variante sin el mecanismo que infla a M1.

Constancia adicional: se adopta la variante de [05] para M1 y no la de [06], para
conservar la propiedad de cota. En [05] la etapa 2 del protocolo solo corrige falsos
positivos ("a manual review is conducted by a subject matter expert to correct false
positives" — [05] §5.1), de modo que la etapa 1 sola es cota superior del conteo del
protocolo completo. En [06] la etapa 2 además agrega duplicados no detectados ("a
subject matter expert manually reviews the clusters to remove false positives and add
missed duplicates" — [06] §IV.D, cierre / §V), y con eso el número de la etapa 1 deja
de ser cota en cualquier dirección.

### 5.c Salvedades sobre las fuentes, leídas del PDF

1. **Inconsistencia interna de [05].** La Tabla 1 (§5.1) reporta Node Duplication
   Rate: baseline 30.38%, CORE-KG 20.27%, mejora relativa **33.28%**. La prosa del
   Apéndice A (párrafo inicial de la página que discute las Figuras 1 y 2) dice:
   "Overall, CORE-KG achieves a relative reduction of **33.58%**, lowering the
   average duplication rate from 30.38% to 20.27%". Ambos valores acompañan el mismo
   par 30.38→20.27. Fijo acá que **se cita el valor de la tabla (33.28%)**, que
   además es el aritméticamente consistente con el par reportado y el que repiten el
   abstract, la §1 y la §6 del propio paper.
2. **Fila no interpretable de [00].** En la Tabla 1 de [00] (§7.3, "Evaluation
   Results for Section Overlap, Answer Accuracy, and Navigation Metrics"), la fila
   "Unconnected Sections Linked" reporta "5014 unconnected section" en la columna
   Without Triplets y "5011 connected sections" en la columna With Triplets: la
   etiqueta de la magnitud cambia de columna a columna (no conectadas / conectadas),
   no hay denominador, y el cuerpo del paper no define la métrica. Tal como está
   publicada no es interpretable. Queda **marcada como no citable** — ni como orden
   de magnitud. Las otras dos filas de navegación de esa tabla (Average Degree, Avg.
   Shortest Path) se citan solo como orden de magnitud, con la salvedad de que [00]
   no declara convención de cómputo (por eso M4 y M5 fijan la propia).

---

## 6. Régimen especial de la cobertura de CQ (M11)

El eval set original del proyecto, de estilo competency questions
(`data/experiment/evaluacion/queries/`), está **QUEMADO** como material de calibración
y de gates: fue usado para seleccionar el grafo ganador, diagnosticar fallas y
calibrar instrumentos, así que cualquier iteración del grafo contra él es entrenar
contra el test. Por lo tanto:

1. **Medición única y descriptiva.** La cobertura de CQ prometida en la propuesta se
   mide UNA sola vez sobre el set quemado: para cada pregunta, si el grafo contiene el
   material que la responde. Es lectura de solo consulta — una foto del artefacto, no
   una vara.
2. **Prohibición de optimización.** Regla de este documento: **no se itera nada contra
   M11 sobre el set quemado. Jamás se convierte en objetivo de optimización.** Ningún
   cambio al grafo se justifica, prioriza ni verifica por su efecto sobre esta
   cobertura. Si un refinamiento la mueve, el movimiento se reporta como observación,
   nunca como mérito.
3. **Condición que habilita una métrica viva.** Si se genera un eval set nuevo por
   generación ciega (instancia generadora sin acceso a los grafos, verificación contra
   el cuerpo de los PDFs — el procedimiento ya usado por el proyecto para extender su
   eval set), ese set puede portar competency questions frescas, y recién ahí la
   cobertura de CQ pasa a ser métrica viva sujeta a seguimiento entre versiones del
   grafo — hasta que ese set, a su vez, se queme por uso en calibración o gates.

La distinción es entonces entre dos condiciones del mismo instrumento: **set quemado →
M11 se mide una vez y queda congelada; set fresco de generación ciega → M11 es métrica
de seguimiento** hasta el quemado del set. La transición de un estado al otro es
unidireccional y se registra por commit.

---

## 7. Predicciones pre-registradas

Predicciones sobre el par de grafos en alcance (§1): el grafo con el defecto de
ensamblado y el grafo re-ensamblado. Sin ningún valor calculado — este documento se
sella antes de correr cualquier medición. Cada predicción declara su mecanismo; donde
el mecanismo admite dos salidas, se declaran ambas ramas sin expectativa.

- **P-a.** La relación aristas/nodos (M4) del grafo con el defecto será MAYOR que la
  del grafo re-ensamblado. Mecanismo: la sobre-fusión del ensamblado defectuoso
  conserva aristas y reduce nodos (§3, consecuencia 2); el re-ensamblado restituye
  nodos sin fabricar aristas nuevas en proporción.
- **P-b (CRUX).** M1 — con el protocolo publicado de [05] — dará un valor IGUAL O
  MAYOR en el grafo re-ensamblado que en el grafo con el defecto; es decir, **el grafo
  corregido se verá PEOR en la métrica publicada**. Mecanismo: los nodos restituidos
  por el re-ensamblado comparten categoría por construcción (variantes normativas del
  mismo punto, distinguidas por alcance), y el clustering fuzzy por `partial_ratio`
  los marcará como duplicados (§5.b). Esta es la inversión anunciada en §3, medida
  sobre datos propios.
- **P-c.** M6 (concentración de grado) será mayor en el grafo con el defecto.
  Mecanismo: la sobre-fusión crea hubs por acumulación de las aristas de los
  constituyentes (§3, consecuencia 3).
- **P-d.** DOS RAMAS, ambas admisibles, sin expectativa declarada. M5 puede resultar
  (i) menor en el grafo con el defecto — los hubs de la sobre-fusión acortan los
  caminos —, o (ii) menor en el grafo corregido — la remoción de nodos cáscara y el
  agregado de nodos reales bien conectados puede compactar la componente mayor. El
  pre-registro no apuesta rama: registra que ambas son consistentes con el modelo de
  §3 y que el valor observado se leerá junto a M6 y M9, nunca solo.
- **P-e.** DOS RAMAS para M9, con el mismo argumento: el re-ensamblado puede (i)
  reducir aislados/componentes (nodos restituidos que se conectan a material
  existente) o (ii) aumentarlos (nodos legítimos del articulado restituido que aún no
  tienen aristas hacia el resto). Sin expectativa declarada.

**VÁLVULA.** Si P-b resulta en la dirección contraria (M1 menor en el grafo
re-ensamblado), el argumento de inversión de la sección 3 queda debilitado en su
aplicación empírica a este corpus, y el trabajo vuelve a discusión ANTES de escribir
cualquier lectura de resultados. En ese escenario no se publica lectura alguna de la
pasada 1 que use el marco de §3 como premisa: primero se revisa el marco.

---

## 8. Las dos pasadas y el régimen del gate

**Pasada 1 — baseline descriptivo.** Medición de M1–M10 sobre los dos grafos en
alcance (M11 según su régimen de §6), SIN umbrales. Objeto: establecer el baseline
numérico del set y verificar las predicciones de la sección 7. La pasada 1 no aprueba
ni rechaza nada; produce el punto de referencia contra el cual la pasada 2 define no
regresión.

**Pasada 2 — gate de no regresión.** Umbrales de NO REGRESIÓN definidos contra el
baseline de la pasada 1, sellados por commit ANTES de que corra el instrumento nuevo
cuya salida van a auditar (el pipeline de re-extracción o el refinamiento que
corresponda). El gate se evalúa sobre las métricas bloqueantes; una regresión
bloqueante detiene la promoción del grafo nuevo hasta decisión registrada.

**Por qué esta versión no trae umbrales.** La ausencia es deliberada: no se pueden
pre-registrar honestamente umbrales sin baseline (serían números inventados, y un
umbral inventado o bien no muerde o bien muerde arbitrariamente), y no se pueden
sellar después de que corra el instrumento que van a auditar (serían umbrales elegidos
mirando el resultado). La única secuencia honesta es: sellar definiciones (este
documento) → medir baseline (pasada 1) → sellar umbrales contra ese baseline (commit
separado y posterior a la pasada 1, anterior a la corrida auditada) → correr y auditar
(pasada 2). El agregado de umbrales es, entonces, **un commit separado y posterior**,
que extiende este documento sin modificar sus definiciones.

**Reparto consistente con la columna "rol en el gate" de la sección 4:**

- **Bloqueantes en la pasada 2:** M2 (tasa_duplicacion_gate), M3 (tasa_conflacion),
  M7 (tasa_ruido_por_rol), M10 (chunks_mudos).
- **Descriptivas:** M1 (declarada inflada — se reporta para documentar la inversión,
  no gobierna), M4, M5, M6, M8, M9 (con las restricciones de reporte conjunto: M4 y
  M5 nunca sin M6; M5 nunca sin M9), y M11 (régimen especial de §6, jamás bloqueante
  sobre el set quemado).

Nótese que los cuatro bloqueantes cubren los dos lados del pareo de §2.a (M2
sub-fusión, M3 sobre-fusión) más las dos vías de ruido de ensamblado (M7 nodos desde
chunks no normativos, M10 articulado sin representación): el gate no puede satisfacerse
empujando el sistema hacia el defecto opuesto al que se corrige.

---

## 9. Restricciones para la implementación futura

La implementación de este set (`scripts/metricas_intrinsecas.py`, cuando exista) queda
sujeta a:

1. **Solo lectura.** No modifica ningún `kg.json`, caché, chunk ni artefacto de
   ninguna fase. Consume los archivos del repo tal como están.
2. **Cero llamadas a API.** Todas las métricas M1–M10 son computables sin LLM (la
   columna determinismo de §4 lo exige); M11 es lectura humana. Costo de inferencia
   de cualquier corrida del set: USD 0.
3. **Zonas selladas intactas.** No toca el cuarteto hasheado (`loader.py`,
   `harness.py`, `judge.py`, `llm_cache.py`), el cluster congelado, `cache/`,
   `queries/`, trazas, `posthoc_run/`, `frozen_run/`, logs, `run_1`–`run_5` ni ningún
   `kg.json`.
4. **Reproducible desde el repo.** Toda corrida es reproducible enteramente desde
   archivos versionados del repositorio (más los PDFs del subset para los roles de
   chunk, que el repo referencia); sin estado externo, sin red.
5. **Salida a ruta declarada.** Los resultados se escriben a
   `data/experiment/metricas_intrinsecas/` (un JSON por grafo medido, con
   identificador del grafo, fecha y versión de este documento), y a ningún otro lado.
6. **Convenciones vinculantes.** Toda convención de cómputo que la sección 4 fija
   (deduplicación de aristas de M4, self-loops de M4/M8, componente mayor de M5,
   normalización de superficie de M2, equivalencia rol normativo = `cuerpo` de
   M7/M10) es vinculante para la implementación. Un cambio de convención exige
   enmienda registrada de este documento ANTES de la corrida que la use, nunca ajuste
   silencioso en el código.

---

## 10. Diferimientos nombrados

Cada diferimiento con su candidata registrada — son decisiones de secuencia, no
omisiones:

1. **Adjudicación humana muestreada de M1 (etapa 2 del protocolo de [05]).** Diferida
   a la pasada 2. Motivo: la cota declarada de M1 (superior — la etapa 2 solo
   removería falsos positivos) sostiene las conclusiones de la pasada 1 tal como
   están formuladas en §7 (P-b afirma dirección, no magnitud), y la adjudicación
   humana es un recurso escaso que se gasta cuando el gate la necesita. Candidata
   registrada: muestreo estratificado por `type` de los clusters de M1/M2, con acta
   de adjudicación, en el mismo formato de actas ya usado por el proyecto.
2. **Adjudicación humana del ruido semántico no capturado por M7.** Diferida a la
   pasada 2, mismo motivo. M7 es cota inferior (no ve cáscaras nacidas de chunks
   normativos); la parte no capturada corresponde a la especie `cascara` del backlog y
   su detección fina hoy pasa por revisión de nodos sin description — candidata
   registrada: muestreo de nodos de bajo contenido (properties vacías o description
   ausente) con provenance de rol `cuerpo`, adjudicado a mano.
3. **Dependencia de M3 (y de M7 sobre el grafo defectuoso) respecto de la caché de
   extracción.** PENDIENTE DE CONFIRMACIÓN: la definición de M3 requiere conteos a
   nivel mención (cuántas menciones extraídas terminaron fundidas en cada nodo), cuya
   fuente candidata es la caché de extracción de la fase v2
   (`data/experiment/grafo_v2/code/cache_v2/`). Antes de la pasada 1 hay que
   confirmar que esa caché conserva las menciones pre-fusión con granularidad
   suficiente. Si no la conserva, M3 se reporta como no computable en esta iteración
   — con esta constancia como registro de que el faltante es de datos, no de diseño —
   y el pareo de §2.a se satisface provisoriamente documentando el límite, no
   retirando a M2 del gate.

---

## 11. Checklist de sellado

Afirmaciones explícitas al cierre, verificables sobre este mismo archivo:

- [x] **No aparece ningún valor de ninguna métrica para ningún grafo de este
  proyecto.** Toda cifra del documento es un valor publicado de [00], [05] o [06], o
  un parámetro de definición (umbral de similitud 75, percentil 1%).
- [x] **Todo valor publicado citado tiene puntero a PDF y a tabla o sección:** [05]
  Tabla 1 y §5.1, §4.1, Apéndice A, Apéndice C; [06] Tablas I–II, §IV.A, §IV.D, §V;
  [00] Tabla 1 y §7.3. Los tres PDFs viven en `docs/literatura/papers/`.
- [x] **Los umbrales de gate están deliberadamente ausentes**, con su justificación en
  §8 y su vía de agregado (commit separado y posterior al baseline) fijada.
- [x] **La convención de cómputo de M4, M5 y M8 queda fijada** (deduplicación por
  triple exacto, self-loops, componente conexa mayor, densidad dirigida sin
  self-loops) **y no cambia después**: toda modificación exige enmienda registrada
  antes de la corrida que la use (§9.6).
