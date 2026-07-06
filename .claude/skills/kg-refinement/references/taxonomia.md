# Taxonomía de causas (cerrada) + herramientas del verificador

Referencia del **Paso 3**. Toda atribución de falla cae en **exactamente una** de las categorías de abajo. La taxonomía es **cerrada**: no inventes categorías nuevas. La razón es poder agregar y comparar resultados entre corridas — si cada corrida usa su propio vocabulario, los mapas de defectos no se pueden comparar. Si una falla no entra en ninguna categoría, eso mismo es un hallazgo: reportalo explícitamente en lugar de forzarla.

---

## Defectos del grafo

El dato falla por algo del KG, no por cómo lo usó el agente.

| Categoría | Qué significa | Evidencia que la confirma |
|---|---|---|
| **contenido_kg** | Un nodo **contradice** el PDF (dice algo que el PDF no dice, o lo dice mal). | El nodo afirma X; el pasaje del PDF dice no-X o algo incompatible. |
| **completitud_kg** | Falta información que el PDF **sí tiene** (nodo stub/vacío, extracción incompleta). | El PDF contiene el dato; en el grafo el nodo está vacío, truncado o ausente el campo. |
| **estructural_kg** | Falta un **nodo o una arista** que la pregunta necesita para conectar la información. | Los datos existen sueltos pero no hay relación que los una (ej. cruce entre dos TOs). |
| **provenance_imprecisa** | El nodo **cita un punto que no funda su contenido** (la cita apunta a otro lado: índice, sección equivocada). | La `location`/`source_doc` del nodo no contiene el contenido que dice fundamentar. |

## Defectos del agente

La información estaba bien en el grafo; el problema es cómo el agente la usó.

| Categoría | Qué significa | Evidencia que la confirma |
|---|---|---|
| **navegación** | El agente **no encontró** info que SÍ estaba en el grafo. | Existe un nodo relevante y fiel — la carga de la prueba es **exhibirlo**, con quote de su CONTENIDO (no su label); la trayectoria muestra que el agente no lo consultó o lo descartó. |
| **generación-de-más** | El agente **agregó glosas o afirmaciones no soportadas** por los nodos que consultó. | La respuesta contiene afirmaciones que no están en ningún nodo de la trayectoria. Ojo: un claim puede ser fácticamente CIERTO y aun así ser generación-de-más — lo que se juzga es el soporte, no la verdad. |

## Sin defecto y abstención (v4)

| Categoría | Lado | Qué significa |
|---|---|---|
| **sin_defecto** | ninguno | La respuesta en realidad no estaba mal: posible falso positivo del juez. Atribución de **último recurso**: exige descartar activamente cada defecto de la taxonomía, uno por uno, documentando el descarte. |
| **frontera_no_determinada** | indeterminado | Tras investigar a fondo, la evidencia no alcanza para decidir entre DOS categorías (típicamente navegación vs completitud_kg). **Abstención honesta de primera clase**: una etiqueta equivocada es PEOR que una abstención honesta; adivinar no es atribuir. Exige (a) documentar qué se buscó y qué se encontró (campo `busquedas`), (b) nombrar las DOS categorías en disputa (campo `entre`), (c) declarar qué evidencia faltante decidiría el caso (campo `evidencia_faltante`). |

**La bifurcación clave (navegación / completitud / frontera):** la diferencia se decide con la búsqueda PROPIA del verificador del nodo que respondería, y tiene TRES salidas, no dos:
- Encontraste el nodo que responde → `navegación` (exhibiéndolo, quote de su contenido).
- NO lo encontraste Y la búsqueda fue exhaustiva (términos plausibles cubiertos, documentados) → `completitud_kg`, con la constancia de búsqueda como evidencia.
- NO lo encontraste pero NO podés garantizar exhaustividad → `frontera_no_determinada`.

La constancia de búsqueda es lo único que distingue "falta" (completitud) de "está mal" (contenido) de "no lo encontré yo" (frontera).

---

## Las tres piezas de evidencia (obligatorias por atribución) — con anclaje textual (v4)

Toda atribución se cierra citando estas tres piezas. Sin las tres, la conclusión es opinión, no evidencia:

1. **Afirmación** — qué dijo el agente (de la respuesta).
2. **Nodo** — qué nodo(s) consultó / qué decía (de la trayectoria + el grafo).
3. **Fuente** — qué dice el PDF en el punto relevante.

**Anclaje textual (v4):** cada pieza es un objeto `{quote, ubicacion}` — `quote` es cita VERBATIM (no paráfrasis) y `ubicacion` dice dónde vive (id de nodo / source_doc+location del PDF / paso N de la trayectoria / respuesta final). Regla: si no se puede citar textualmente el lugar exacto donde se rompe el circuito, no hay evidencia suficiente para esa etiqueta. Además, el contrato incluye el campo **`busquedas`** (lista `{consulta, resultado}`), obligatorio para `completitud_kg` y `frontera_no_determinada`.

El cruce de las tres es lo que decide la categoría:
- ¿El dato estaba en el grafo? (Nodo vs Fuente) → distingue defecto-de-grafo de defecto-de-agente.
- ¿El agente lo encontró/usó bien? (Afirmación vs Nodo) → distingue navegación de generación-de-más.
- ¿El nodo era fiel al PDF? (Nodo vs Fuente) → distingue contenido_kg / completitud_kg / provenance_imprecisa.

---

## Atribución múltiple: una falla puede tener más de una causa

Una falla mapea a **una o más** categorías de la taxonomía. La taxonomía sigue siendo **cerrada** — las categorías no cambian; lo que se permite es que una misma falla se atribuya a varias de ellas a la vez.

Cuando hay más de una, se distinguen:

- **Causa primaria:** la que **mueve el veredicto** — la que hace fallar la respuesta. Puede haber **más de una primaria**: cuando la pregunta tiene patas independientes y un defecto distinto rompe cada pata, cada uno es primario (ninguno es prescindible para que la respuesta deje de estar mal). Ver CQ-017 en `casos_control.md`.
- **Causa(s) secundaria(s):** otras causas realmente presentes en la falla, pero que **no son lo que rompe** la respuesta (p. ej. un defecto de estilo que estaría igual aunque la pregunta acertara).

**Cada atribución —primaria o secundaria— lleva igual sus tres piezas de evidencia** (afirmación / nodo / fuente). Una secundaria no documentada con evidencia no es una secundaria: es una conjetura, y no se registra.

**Por qué se permite (y no se fuerza una sola):** las fallas reales suelen tener varias causas, y forzar a elegir una pierde información. A veces, además, **una causa de grafo empuja una de agente**: el nodo correcto no existe, así que el agente se ve obligado a rellenar con lo que tiene (mis-aplica otro nodo, o agrega glosas de su cosecha). Esa cadena causal —el hueco del grafo provoca el desvío del agente— es un **hallazgo valioso**, no ruido: dice que arreglando el grafo podría desaparecer también el síntoma de agente. Registrar las dos causas preserva ese diagnóstico; quedarse con una lo borra.

Distinguir primaria de secundaria no es una jerarquía cosmética: es lo que conecta el Paso 3 con el enrutamiento del Paso 4 (qué cambio ataca lo que de verdad rompe la respuesta) y con la regla de calibración (ver `casos_control.md`).

---

## Procedimiento en fases (v4)

El verificador no usa las tools "en el orden que decida": sigue tres fases, y cada una alimenta a la siguiente.

- **FASE A — EXTRACCIÓN** (sin tools, solo con el contexto): lista los tool calls del agente con argumentos, qué devolvió cada uno y si era pertinente, en qué paso está la decisión que llevó al error (con cita textual; si el agente actuó bien sobre lo que tenía, se declara explícitamente — eso es evidencia de lado grafo, no un campo vacío), el fragmento de thinking de esa decisión si existe, y las patas según el step1 del juez. El resultado va al campo `extraccion_traza` del JSON final (lo consume el reporte HTML).
- **FASE B — INVESTIGACIÓN**: por cada pata fallida, el cruce de las tres fuentes usando las tools. Acá entra el ESQUEMA DEL GRAFO (inyectado en el contexto): razonar qué nodo/arista DEBERÍA existir para responder y chequear si existe.
- **FASE C — ATRIBUCIÓN**: recién acá se etiqueta (o se abstiene con `frontera_no_determinada`), con los anclajes textuales.

## Herramientas del verificador

Dentro de la FASE B, el verificador decide **cuáles usar y cuántas veces** — eso es criterio del agente. Las disponibles (las 3 de grafo del harness + 1 de PDF):

- **buscar_nodos / ver_nodo / ver_vecinos** — cualquier nodo del grafo, no solo los que el agente usó. Sirven para responder "¿existía un nodo relevante que el agente no consultó?".
- **leer_pasaje_pdf** en un punto/página específico. Sirve para responder "¿qué dice realmente la fuente?". Si la ubicación no ancla, devuelve `localizacion_pdf="fallida"` como señal explícita.

La **trayectoria del agente** (tool calls + resultados + thinking por turno si existe) no es una tool: viene en el contexto inicial de la falla, junto con la descomposición del juez (step1), los claims que el juez aprobó (para no re-litigar) y el contenido íntegro de los nodos vistos.

**Ejemplos resueltos:** el system prompt del verificador (`verificador.py`) incluye una sección de EJEMPLOS RESUELTOS con 3 casos reales de run_1/run_5 (nunca de run_3 — los casos-control siguen ciegos) que enseñan el método y el formato de anclaje. Viven en el prompt, no acá.

**Recordatorio de método (Paso 3):** arrancá desde el síntoma ("esta respuesta falló"), recolectá evidencia con estas herramientas y *recién después* concluí. No empieces mirando el nodo ni asumiendo que la causa es el grafo. La pregunta guía es "¿por qué el juez marcó mal esta respuesta?", nunca "¿es verdadera la afirmación del agente?".
