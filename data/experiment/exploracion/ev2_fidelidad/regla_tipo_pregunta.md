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
