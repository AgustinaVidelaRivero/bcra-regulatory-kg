# Taxonomía v2 (dos capas, alineada RAGAS) + herramientas del verificador

Referencia del **Paso 3**. La taxonomía tiene **DOS CAPAS**: la **capa 1** clasifica el **síntoma** de cada claim fallido con los nombres estándar de RAGAS (en inglés); la **capa 2** atribuye la **causa raíz** (en castellano). Toda atribución emite **el par `{sintoma_capa1, causa_capa2}`**. Ambas capas son **cerradas**: no inventes categorías nuevas. La razón es poder agregar y comparar resultados entre corridas — si cada corrida usa su propio vocabulario, los mapas de defectos no se pueden comparar. Si una falla no entra en ninguna categoría, eso mismo es un hallazgo: reportalo explícitamente en lugar de forzarla.

> **Changelog v1 → v2:** la v1 era de una sola capa. La etiqueta **generación-de-más** se eliminó como categoría y se partió: su síntoma es `faithfulness` (capa 1) y su causa lado-agente pasa a llamarse `alucinacion_agente` (capa 2). Se agregó `alcanzabilidad_kg` (lado grafo, sin equivalente v1). Las corridas viejas (calibraciones v1–v4 del verificador, mapa de defectos de la Fase 2.3) se leen con el vocabulario v1: ver la tabla de correspondencia en `mapeo_taxonomia_v1_v2.md`.
> **v2.1 (2026-07-14):** se precisa la prueba de alcanzabilidad (rama `context_recall` del árbol y fila `alcanzabilidad_kg`): "búsquedas razonables" y "términos de la pregunta" = vocabulario disponible **ex ante** para el agente (la pregunta + lo que los outputs COMPLETOS de su propia trayectoria le expusieron); el vocabulario aprendido del PDF o del ground truth durante la verificación NO cuenta.

---

## Capa 1 — Síntoma (por claim fallido, nombres RAGAS)

**Regla de precedencia:** los síntomas se evalúan **POR PATA** y **EN ORDEN** — un claim mal aplicado (soportado por un nodo NO pertinente a la pata) calificaría a la vez como `noise_sensitivity` y `context_recall`, y las dos ramas llevan a causas distintas. Gana el primero que aplica:

1. **context_recall** — ¿apareció en la trayectoria el dato PERTINENTE a la pata (el que la responde)? Si nunca apareció → `context_recall`, aunque el agente haya rellenado la pata con otro nodo no pertinente.
2. **faithfulness** — el dato pertinente apareció; ¿el claim tiene soporte en lo consultado? Sin soporte → `faithfulness`.
3. **noise_sensitivity** — tiene soporte; ¿es correcto contra el PDF/GT? Incorrecto → `noise_sensitivity`.

> **"Pertinente"** = el nodo que porta el dato que la pata pregunta; un nodo de otro tema usado para rellenar no cuenta como contexto de la pata.

Exactamente estas tres:

| Síntoma | Qué significa |
|---|---|
| **faithfulness** | Claim **no soportado** por los nodos que el agente consultó. Ojo: un claim puede ser fácticamente CIERTO y aun así fallar faithfulness — lo que se juzga es el soporte, no la verdad. |
| **noise_sensitivity** | Claim **soportado por un nodo consultado**, pero **incorrecto** contra el PDF/ground truth. |
| **context_recall** | Una **pata de la pregunta quedó sin dato** — el contexto necesario nunca apareció en la trayectoria. |

## Capa 2 — Causa raíz (cerrada)

### Defectos del grafo

El dato falla por algo del KG, no por cómo lo usó el agente.

| Categoría | Qué significa | Evidencia que la confirma |
|---|---|---|
| **contenido_kg** | Un nodo **contradice** el PDF (dice algo que el PDF no dice, o lo dice mal). | El nodo afirma X; el pasaje del PDF dice no-X o algo incompatible. |
| **completitud_kg** | Falta información que el PDF **sí tiene** (nodo stub/vacío, extracción incompleta, dato ausente). | El PDF contiene el dato; en el grafo el nodo está vacío, truncado o ausente el campo. Exige constancia de búsqueda (campo `busquedas`). |
| **estructural_kg** | Falta un **nodo o una arista** que la pregunta necesita para conectar la información. | Los datos existen sueltos pero no hay relación que los una (ej. cruce entre dos TOs). |
| **provenance_imprecisa** | El nodo **cita un punto que no funda su contenido** (la cita apunta a otro lado: índice, sección equivocada). | La `location`/`source_doc` del nodo no contiene el contenido que dice fundamentar. |
| **alcanzabilidad_kg** (nueva en v2) | El **nodo portador existe con el contenido correcto**, pero es **inalcanzable por la búsqueda léxica**: `buscar_nodos` indexa label/id, no description, y ninguna búsqueda razonable desde los términos de la pregunta lo devuelve. "Términos de la pregunta" = vocabulario **ex ante** del agente (pregunta + outputs COMPLETOS de su propia trayectoria); lo aprendido del PDF/GT durante la verificación NO cuenta (v2.1). | Exhibir el nodo (quote de su contenido) + constancia de búsqueda (campo `busquedas`) mostrando que los términos plausibles del vocabulario ex ante NO lo alcanzan y que solo se alcanza con palabras del propio nodo. |

### Defectos del agente

La información estaba bien en el grafo; el problema es cómo el agente la usó.

| Categoría | Qué significa | Evidencia que la confirma |
|---|---|---|
| **navegación** | El agente **no encontró** info que SÍ estaba en el grafo y era alcanzable. | Existe un nodo relevante, fiel y alcanzable con búsquedas razonables — la carga de la prueba es **exhibirlo**, con quote de su CONTENIDO (no su label); la trayectoria muestra que el agente no lo consultó o lo descartó. |
| **alucinacion_agente** | El agente **agregó glosas o afirmaciones no soportadas** por los nodos que consultó. Dos modos: **(a)** el grafo TENÍA el dato y el agente afirmó sin soporte de su trayectoria; **(b)** **glosa de cosecha propia**: ni el grafo ni el PDF tienen el dato. | La respuesta contiene afirmaciones que no están en ningún nodo de la trayectoria. Modo (a): exhibir el nodo portador (quote de su contenido). Modo (b): constancia de búsqueda (campo `busquedas`) + verificación negativa contra el PDF (`leer_pasaje_pdf`) — acá NO hay nodo que exhibir. |

### Sin defecto y abstención

| Categoría | Lado | Qué significa |
|---|---|---|
| **sin_defecto** | ninguno | La respuesta en realidad no estaba mal: posible falso positivo del juez. Atribución de **último recurso**: exige descartar activamente cada defecto de la taxonomía, uno por uno, documentando el descarte. |
| **frontera_no_determinada** | indeterminado | Tras investigar a fondo, la evidencia no alcanza para decidir entre DOS categorías. **Abstención honesta de primera clase**: una etiqueta equivocada es PEOR que una abstención honesta; adivinar no es atribuir. Exige (a) documentar qué se buscó y qué se encontró (campo `busquedas`), (b) nombrar las DOS categorías en disputa (campo `entre`), (c) declarar qué evidencia faltante decidiría el caso (campo `evidencia_faltante`). |

---

## Árbol de decisión capa 1 → capa 2

El síntoma (capa 1) determina qué preguntas hacer para llegar a la causa (capa 2):

- **faithfulness** → ¿el grafo tenía el dato?
  - Encontrado (exhibirlo, quote de su contenido) → `alucinacion_agente`.
  - No encontrado + búsqueda exhaustiva documentada (términos plausibles cubiertos, campo `busquedas`) → ¿el PDF tiene el dato? (`leer_pasaje_pdf`):
    - Sí → `completitud_kg` (el hueco del grafo empujó la glosa).
    - No → `alucinacion_agente` (glosa de cosecha propia; acá NO hay nodo que exhibir — la evidencia es la constancia de búsqueda + la verificación negativa contra el PDF).
  - No encontrado sin garantía de exhaustividad → `frontera_no_determinada`.
- **noise_sensitivity** → ¿el nodo consultado es fiel al PDF?
  - Contradice el PDF → `contenido_kg`.
  - La cita apunta a otro lado (índice, sección equivocada) → `provenance_imprecisa`.
  - Es fiel → `sin_defecto` (falso positivo del juez).
- **context_recall** → ¿existe nodo portador del dato faltante?
  - Existe y las búsquedas razonables del agente lo alcanzaban → `navegación`.
  - Existe pero solo se alcanza con palabras del propio nodo (no de la pregunta) → `alcanzabilidad_kg`.
  - No existe → `completitud_kg` (falta el dato) o `estructural_kg` (falta la conexión).
  - **Prueba de alcanzabilidad (v2.1):** "búsquedas razonables" y "términos de la pregunta" = vocabulario disponible EX ANTE para el agente — los términos de la pregunta más los que los outputs COMPLETOS de su propia trayectoria le expusieron. El vocabulario aprendido del PDF o del ground truth durante la verificación NO cuenta para esta prueba.

La constancia de búsqueda es lo único que distingue "falta" (`completitud_kg`) de "está pero no se llega" (`alcanzabilidad_kg`) de "no lo encontré yo" (`frontera_no_determinada`).

---

## Las tres piezas de evidencia (obligatorias por atribución) — con anclaje textual

Toda atribución se cierra citando estas tres piezas. Sin las tres, la conclusión es opinión, no evidencia:

1. **Afirmación** — qué dijo el agente (de la respuesta).
2. **Nodo** — qué nodo(s) consultó / qué decía (de la trayectoria + el grafo).
3. **Fuente** — qué dice el PDF en el punto relevante.

**Anclaje textual:** cada pieza es un objeto `{quote, ubicacion}` — `quote` es cita VERBATIM (no paráfrasis) y `ubicacion` dice dónde vive (id de nodo / source_doc+location del PDF / paso N de la trayectoria / respuesta final). Regla: si no se puede citar textualmente el lugar exacto donde se rompe el circuito, no hay evidencia suficiente para esa etiqueta. Además, el contrato incluye el campo **`busquedas`** (lista `{consulta, resultado}`), obligatorio para `completitud_kg`, `alcanzabilidad_kg` y `frontera_no_determinada`.

El cruce de las tres es lo que decide el par:
- ¿El claim está soportado por lo consultado? (Afirmación vs Nodo) → decide el síntoma de capa 1 (`faithfulness` vs `noise_sensitivity`); una pata sin dato en toda la trayectoria → `context_recall`.
- ¿El dato estaba en el grafo? (Nodo vs Fuente + búsqueda propia) → distingue defecto-de-grafo de defecto-de-agente en capa 2.
- ¿El nodo era fiel al PDF? (Nodo vs Fuente) → distingue `contenido_kg` / `completitud_kg` / `provenance_imprecisa`.

---

## Atribución múltiple: una falla puede tener más de una causa

Una falla mapea a **uno o más** pares `{sintoma_capa1, causa_capa2}`. La taxonomía sigue siendo **cerrada** — las categorías no cambian; lo que se permite es que una misma falla se atribuya a varias a la vez.

Cuando hay más de una, se distinguen:

- **Causa primaria:** la que **mueve el veredicto** — la que hace fallar la respuesta. Puede haber **más de una primaria**: cuando la pregunta tiene patas independientes y un defecto distinto rompe cada pata, cada uno es primario (ninguno es prescindible para que la respuesta deje de estar mal). Ver CQ-017 en `casos_control.md`.
- **Causa(s) secundaria(s):** otras causas realmente presentes en la falla, pero que **no son lo que rompe** la respuesta (p. ej. un defecto de estilo que estaría igual aunque la pregunta acertara).

**Cada atribución —primaria o secundaria— lleva igual sus tres piezas de evidencia** (afirmación / nodo / fuente). Una secundaria no documentada con evidencia no es una secundaria: es una conjetura, y no se registra.

**Por qué se permite (y no se fuerza una sola):** las fallas reales suelen tener varias causas, y forzar a elegir una pierde información. A veces, además, **una causa de grafo empuja una de agente**: el nodo correcto no existe, así que el agente se ve obligado a rellenar con lo que tiene (mis-aplica otro nodo, o agrega glosas de su cosecha). Esa cadena causal —el hueco del grafo provoca el desvío del agente— es un **hallazgo valioso**, no ruido: dice que arreglando el grafo podría desaparecer también el síntoma de agente. Registrar las dos causas preserva ese diagnóstico; quedarse con una lo borra.

Distinguir primaria de secundaria no es una jerarquía cosmética: es lo que conecta el Paso 3 con el enrutamiento del Paso 4 (qué cambio ataca lo que de verdad rompe la respuesta) y con la regla de calibración (ver `casos_control.md`).

---

## Procedimiento en fases

El verificador no usa las tools "en el orden que decida": sigue tres fases, y cada una alimenta a la siguiente.

- **FASE A — EXTRACCIÓN** (sin tools, solo con el contexto): lista los tool calls del agente con argumentos, qué devolvió cada uno y si era pertinente, en qué paso está la decisión que llevó al error (con cita textual; si el agente actuó bien sobre lo que tenía, se declara explícitamente — eso es evidencia de lado grafo, no un campo vacío), el fragmento de thinking de esa decisión si existe, y las patas según el step1 del juez. El resultado va al campo `extraccion_traza` del JSON final (lo consume el reporte HTML).
- **FASE B — INVESTIGACIÓN**: por cada pata fallida, el cruce de las tres fuentes usando las tools. Acá entra el ESQUEMA DEL GRAFO (inyectado en el contexto): razonar qué nodo/arista DEBERÍA existir para responder y chequear si existe. Para el síntoma `context_recall`, la FASE B incluye probar si el nodo portador se alcanza desde los términos de la pregunta (decide `navegación` vs `alcanzabilidad_kg`).
- **FASE C — ATRIBUCIÓN**: recién acá se etiqueta (o se abstiene con `frontera_no_determinada`), con los anclajes textuales. La FASE C emite **SIEMPRE el par `{sintoma_capa1, causa_capa2}` por atribución** — nunca una capa sola.

## Herramientas del verificador

Dentro de la FASE B, el verificador decide **cuáles usar y cuántas veces** — eso es criterio del agente. Las disponibles (las 3 de grafo del harness + 1 de PDF):

- **buscar_nodos / ver_nodo / ver_vecinos** — cualquier nodo del grafo, no solo los que el agente usó. Sirven para responder "¿existía un nodo relevante que el agente no consultó?" y, con búsquedas desde los términos de la pregunta, "¿era alcanzable?".
- **leer_pasaje_pdf** en un punto/página específico. Sirve para responder "¿qué dice realmente la fuente?". Si la ubicación no ancla, devuelve `localizacion_pdf="fallida"` como señal explícita.

La **trayectoria del agente** (tool calls + resultados + thinking por turno si existe) no es una tool: viene en el contexto inicial de la falla, junto con la descomposición del juez (step1), los claims que el juez aprobó (para no re-litigar) y el contenido íntegro de los nodos vistos.

**Ejemplos resueltos:** el system prompt del verificador (`verificador.py`, v5) incluye una sección de EJEMPLOS RESUELTOS con 3 casos reales de run_1/run_5 más 1 ejemplo negativo ("error frecuente — no hacer"), todos en vocabulario v2 (pares `{sintoma_capa1, causa_capa2}`) y nunca de run_3 (gate) ni de los casos del dev set. Viven en el prompt, no acá. Desde v5 el prompt ENSAMBLA esta taxonomía en runtime leyendo este archivo (secciones Capa 1 → Árbol de decisión → piezas de evidencia → atribución múltiple): editar acá ES editar el prompt.

**Recordatorio de método (Paso 3):** arrancá desde el síntoma ("esta respuesta falló"), recolectá evidencia con estas herramientas y *recién después* concluí. No empieces mirando el nodo ni asumiendo que la causa es el grafo. La pregunta guía es "¿por qué el juez marcó mal esta respuesta?", nunca "¿es verdadera la afirmación del agente?".
