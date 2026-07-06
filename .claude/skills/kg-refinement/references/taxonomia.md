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
| **navegación** | El agente **no encontró** info que SÍ estaba en el grafo. | Existe un nodo relevante y fiel; la trayectoria muestra que el agente no lo consultó o lo descartó. |
| **generación-de-más** | El agente **agregó glosas o afirmaciones no soportadas** por los nodos que consultó. | La respuesta contiene afirmaciones que no están en ningún nodo de la trayectoria. |

---

## Las tres piezas de evidencia (obligatorias por atribución)

Toda atribución se cierra citando estas tres piezas. Sin las tres, la conclusión es opinión, no evidencia:

1. **Afirmación** — qué dijo el agente (de la respuesta).
2. **Nodo** — qué nodo(s) consultó / qué decía (de la trayectoria + el grafo).
3. **Fuente** — qué dice el PDF en el punto relevante.

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

## Herramientas del verificador

El subagente verificador (aislado, ver SKILL.md) decide **cuáles usar y en qué orden** — eso es criterio del agente. Las disponibles:

- **Buscar en el grafo** — cualquier nodo, no solo el que el agente usó. Sirve para responder "¿existía un nodo relevante que el agente no consultó?".
- **Leer el PDF** en un punto/página específico. Sirve para responder "¿qué dice realmente la fuente?".
- **Ver la trayectoria del agente** — qué nodos miró y cuáles no. Sirve para reconstruir el camino real, no el supuesto.

**Recordatorio de método (Paso 3):** arrancá desde el síntoma ("esta respuesta falló"), recolectá evidencia con estas herramientas y *recién después* concluí. No empieces mirando el nodo ni asumiendo que la causa es el grafo.
