# Regla de clasificación por tipo — versión 2

FIRMADO por la autora — 2026-09-26

Fecha: 2026-09-26

Regla v1 transcrita íntegra a continuación; sha256 del archivo v1: 35c8be102b68c8ef385686bd037c3e0b788f23f5a112380902fc2c2924b4a072

# Regla de clasificación por tipo — conjunto EV2

Conjunto: `preguntas_ev2_fidelidad.json` (sha256 1d58733699c325c90510e1ead5f18eac6c3cd970ee3b0ab7ff141da539162b40), 40 preguntas.
Escrita el 20/09/2026, antes de leer ninguna pregunta con este fin.

## Material permitido

Para clasificar una pregunta se lee únicamente: la pregunta, su ancla, sus criterios y el texto oficial del punto ancla. No se consulta ninguna respuesta del agente, traza, veredicto del juez ni reporte de evaluación.

## Tipos

- dato directo: todos los criterios de la pregunta se satisfacen con el texto del punto ancla.
- varios puntos: al menos un criterio exige contenido que no está en el punto ancla sino en otro punto, al que el ancla remite o no.
- abstención: la respuesta correcta, según los criterios, es que la norma no lo prevé o que no hay dato.
- dudoso: no se puede decidir entre los anteriores con el material permitido; se anota el motivo y no se fuerza.

## Procedimiento

1. Las 40 preguntas se leen en un orden aleatorio con semilla 20260920, generado sobre la lista de ids ordenada alfabéticamente.
2. Cada pregunta recibe un tipo y una nota de una línea con el criterio que decidió.
3. La clasificación se guarda en un archivo aparte, `tipo_pregunta_ev2.json`. El JSON sellado del conjunto no se modifica.
4. Control: un modelo de lenguaje aplica esta misma regla de forma independiente sobre el mismo material permitido, sin ver la clasificación de la autora. Se reporta el acuerdo y cada desacuerdo con su adjudicación y su motivo.
5. La misma regla se aplica al conjunto de preguntas nuevas del test final cuando se construya.

## Quién clasifica

La autora. La clasificación de la autora es la que vale; el control del modelo se reporta y no la reemplaza.

## Enmienda 1 — 20/09/2026, antes de leer ninguna pregunta

El punto ancla comprende sus subpuntos: todo punto cuya numeración empieza con la del ancla seguida de un punto (por ejemplo, para el ancla 6.11, los puntos 6.11.1, 6.11.2 y sus descendientes) forma parte del texto del punto ancla a los fines de esta regla. «Otro punto» es todo punto que no cumple esa condición.

## Interpretación v2 (2026-09-26)

La regla v2 es la regla v1 intacta, incluida su Enmienda 1, más la interpretación siguiente. Nada más cambia.

Un criterio que pide una remisión tal como el ancla la enuncia no exige el contenido remitido. Que el ancla remita a otro punto no cambia el tipo de la pregunta si ningún criterio pide ese contenido.

Los dos ejemplos de esta interpretación son las dos filas de `tipo_pregunta_adjudicacion.csv` (sha256 84a598829a50404d1b4fd912f54c772d4651c1f62921fbfe7905d3e5e2aa8a75), transcritas con sus cuatro columnas (`orden`, `id`, `tipo_final`, `fundamento`) y el criterio que decidió.

Ejemplo 1
- id: EV2F-014
- orden: 20
- criterio: c4
- tipo_final: dato directo
- fundamento: c4 pide la regla de plazo tal como 13.5 la enuncia (plazo del servicio más otros 15 días corridos) y no el plazo concreto en días de 13.2; ningún criterio exige contenido de 13.2

Ejemplo 2
- id: EV2F-005
- orden: 30
- criterio: c1 a c5
- tipo_final: dato directo
- fundamento: c1 a c5 corresponden al encabezado de 4.6.1, 4.6.1.1, 4.6.1.2, 4.6.1.4 ii) y el cierre de 4.6.1; ningún criterio pide los requisitos de 3.16.1 a 3.16.4 a los que remite 4.6.1.3; que un criterio cubra menos ítems que el ancla no lo convierte en varios puntos

## Alcance

La regla v2 clasifica las preguntas nuevas de la tanda 0 (B6.0 fase 1, segunda parte) y el conjunto final de B6.3 (a). La clasificación sellada de las 40 preguntas de EV2 (40 dato directo, `tipo_pregunta_ev2.json`, sha256 f96055e098d0b59afcbd22ecae2c160147ec97cb0c038b4f783be546a8f53803) no se reemplaza ni se recalcula.

El procedimiento se aplica a cada conjunto nuevo con la semilla, el orden y el archivo de salida que declare el mandato de su clasificación.

## Qué no cambia

- La clasificación de las 40 preguntas de EV2 sellada en U-EV2-TIPO no se reemplaza.
- El control del modelo bajo la v2 se corre en una unidad aparte, después de la firma, y se reporta sin corregir nada.

## Firma

Firmada por la autora el 2026-09-26.
