# Formato de una propuesta de cambio

Referencia del **Paso 4**. Cada cambio propuesto se escribe con **este schema fijo**. La razón de fijarlo: el **Paso 5 lo consume** para aplicar los cambios y demostrar mejora — si el formato varía entre propuestas, no se puede aplicar de forma confiable ni auditar. El *contenido* de cada campo es criterio del agente; la *estructura* no.

---

## Campos (todos obligatorios)

| Campo | Qué va | Por qué es obligatorio |
|---|---|---|
| `id_falla` | El identificador de la falla atribuida en el Paso 3 (p. ej. la CQ + nodo) a la que responde este cambio. | **Toda propuesta se ancla en una falla atribuida** — no hay cambios por intuición. Rastrea el cambio a su defecto con evidencia. |
| `categoria_defecto` | La categoría de la taxonomía cerrada (`contenido_kg`, `completitud_kg`, `estructural_kg`, `provenance_imprecisa`, `navegación`, `generación-de-más`) que **esta** propuesta ataca. Si la falla tuvo [atribución múltiple](taxonomia.md), se genera **una propuesta por causa** (cada una con su `categoria_defecto`); indicá si la causa es primaria o secundaria. | Conecta el cambio con la atribución del Paso 3; debe ser una de las categorías cerradas. Una propuesta = una causa, para que el Paso 5 sepa qué defecto ataca cada cambio. |
| `palanca` | `grafo/esquema` · `prompt_agente` · `corpus`. | Define qué se toca. `corpus` no modifica el grafo: se reporta como límite. |
| `cambio_exacto` | La modificación concreta y aplicable: qué nodo/arista/campo, con qué valor; o el texto exacto del ajuste de prompt; o el TO faltante a señalar. | El Paso 5 tiene que poder aplicarlo sin interpretar. "Mejorar el nodo X" no es aplicable; "poblar el campo `enumeracion` del nodo X con [valor]" sí. |
| `cita_pdf` | La cita textual del PDF que **funda** el cambio: documento + punto/página + el texto literal. | **Candado anti-entrenar-contra-el-test.** El criterio de validez es "lo dice el PDF", **nunca** "hace pasar la pregunta". El ancla es la fuente, jamás la respuesta esperada. |
| `como_se_verificaria` | Cómo se comprobaría que el cambio es fiel a la fuente (qué chequear contra el PDF). | Hace verificable la propuesta y prepara la revisión humana. |
| `categoria_riesgo` | `bajo` (→ automático) · `alto` (→ revisión humana). | Enruta la aplicación. Ver criterio abajo. |
| `justificacion_riesgo` | Por qué cae en esa categoría, aplicando el criterio fijo (no al humor). | La clasificación debe ser consistente entre corridas. |

---

## Criterio de riesgo (fijo — se aplica, no se reinterpreta)

- **`bajo` → automático:** transcripción de un dato verificable contra un pasaje **único e inequívoco** del PDF, **sin decisión de modelado ni interpretación**. Ej.: poblar un nodo stub con una enumeración explícita del PDF; completar un límite numérico textual.
- **`alto` → revisión humana:** creación de estructura nueva (aristas, tipos), cambios de prompt del agente, datos con ambigüedad o excepciones, o cualquier cosa que requiera juicio de dominio regulatorio. Ej.: una arista cross-documento; un ajuste de prompt.
- **Ante la duda → `alto`.** El default seguro es pedir aprobación; lo automático es la excepción justificada, no la regla.

---

## Registro auditable de los cambios automáticos

Los cambios `bajo` que se aplican solos dejan rastro de **qué cambió, en qué nodo, anclado en qué cita**. La razón: que la revisión humana final sea un chequeo liviano sobre una lista acotada, no una auditoría a ciegas del grafo entero.

---

## Ejemplo (estructura; los valores son ilustrativos)

```yaml
id_falla: "CQ-031 / nodo:clasificacion-deudores-no-clasificables"
categoria_defecto: completitud_kg
palanca: grafo/esquema
cambio_exacto: >
  Poblar el campo `contenido` del nodo stub
  "clasificacion-deudores-no-clasificables" con la enumeración del punto 4.5
  (deudores con financiaciones cubiertas totalmente con garantías preferidas 'A')
  y vincularlo al punto 4.4 (no corresponde evaluar capacidad de repago).
cita_pdf: >
  [Clasificación 4.5] "Los deudores cuyas financiaciones se encuentren cubiertas
  totalmente con garantías preferidas 'A' no serán objeto de clasificación [...]".
  [Clasificación 4.4] "No corresponderá la evaluación de la capacidad de repago
  respecto de las financiaciones que se encuentren respaldadas con tales garantías."
como_se_verificaria: >
  Releer puntos 4.4 y 4.5 del TO de Clasificación de Deudores y confirmar que el
  texto poblado coincide literalmente, sin agregar deudores no enumerados.
categoria_riesgo: bajo
justificacion_riesgo: >
  Transcripción de una enumeración explícita y única del PDF, sin modelado ni
  interpretación. El dato está literal en 4.5/4.4.
```

> El ejemplo usa CQ-031 porque el diseño lo da como caso típico de bajo riesgo. No es una plantilla a copiar: el `cambio_exacto`, la `cita_pdf` y la clasificación los produce el agente para cada falla real, anclados en el PDF.
