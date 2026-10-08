# Registro de reunión: devolución y validación del capítulo 3

**CONFIRMADO por la autora el 07/10/2026.** Reemplaza al BORRADOR del 06/10/2026, que queda en la historia del repo. Rige la convención
del proyecto: cero nombres propios de personas, y cada decisión documentada por su justificación técnica.

## Devolución (30/09/2026)
Asistentes: el mentor, la revisora de escritura y la autora.
Material leído: capítulos 1 y 3 (hasta la sección 3.6), en la versión de la tesis en Overleaf al 30/09/2026.

Pedidos sobre la estructura:
1. Separar el esquema (capítulo 3) de la construcción del grafo (capítulo 4).
2. Abrir el capítulo 3 mostrando un documento del BCRA y un análisis cualitativo de sus características, y derivar de ese análisis el esquema, que se presenta al final del capítulo.
3. Más tablas, figuras e información estructurada; menos contenido dentro de los párrafos.
4. Definir cada término antes de usarlo.
5. Una introducción breve para cada capítulo.
6. En el capítulo 4, una figura del pipeline en la introducción, una sección por componente y después el ciclo y la construcción por etapas.
7. Un mismo ejemplo conductor a lo largo de toda la tesis, desde el texto crudo hasta el grafo.
8. Lector objetivo: un egresado de la carrera que no conoce el BCRA y quizás tampoco los grafos.

Principio de diseño: el esquema se define a partir de la información de los documentos y de su uso, y es independiente del pipeline. El pipeline se adapta al esquema, y no al revés. Como criterio general, evitar reprocesar todo ante un cambio y adaptar lo más posible por código.

Puntos técnicos y su estado (al 07/10/2026; **corrección de la autora del 07/10/2026**, que reemplaza a «Puntos técnicos y su resolución»):
1. Umbrales: cómo representar las cuantías y los plazos de una norma. Respondido con la ley de esquema L-ESQ-R2, firmada, que extiende la propiedad umbral a cuatro tipos de norma (Restriccion ya la tenía).
2. Validación de los valores cerrados: que todos se controlen por código y no solo en las instrucciones. Respondido con la validación por modelos pydantic, que controla todas las listas; los valores que no se pueden derivar quedan marcados, y el residuo (las Comunicacion sin tipo) se corrige en U-OMISIONES-COD.
3. Sujetos que no se pueden mapear al catálogo: definir su proceso. Respondido con la cuarentena de las menciones sin resolver y su re-resolución por código contra el catálogo de resolución (U-RERESOL-CAT), sin volver a extraer; un rol nuevo entra por el procedimiento de crecimiento del catálogo (enmienda 4 al protocolo entre tandas).
4. Actualización y mantenimiento del grafo: qué cambios exigen reprocesar todo y cuáles no, cómo incorporar normas nuevas, actualizar solo el subgrafo afectado a partir de las comunicaciones que modifican puntos concretos, y un control que avise cuando algo cambia en la fuente. Respondido en parte: la tabla de reprocesamiento y el protocolo entre tandas dicen qué cambios exigen reprocesar; el job de actualización ante cambio normativo (U-JOB-ACT) y el control de la fuente (U-MANT) cubren las normas nuevas y los cambios del sitio; la actualización solo del subgrafo afectado (U-SUBGRAFO) sigue abierta. En la tesis va al capítulo 6.

## Cambios aplicados
Los pedidos de estructura 1 a 8 y los cuatro puntos técnicos, aplicados en la versión de la tesis en Overleaf, donde la autora y los mentores editan. Esa versión entra al repo en la próxima sincronización desde Overleaf, con su commit.

## Validación (entre el 30/09/2026 y el 06/10/2026)
Los mentores validaron en persona el capítulo 3 con los cambios aplicados, sobre la versión en Overleaf. Por decisión de la autora, la evidencia de la validación es este registro, sin confirmación escrita aparte.

## Devolución posterior (07/10/2026)
La devolución de los mentores del 07/10/2026 sobre la estructura del capítulo 3 (tres partes: los documentos, el esquema final presentado primero con tablas, y su validación) es de presentación y no cambia el esquema validado.

## Pendientes de P7 (corrección de la autora del 07/10/2026)
1. Destinos de los ocho límites de la Tabla 4: NO TRATADO en esta reunión; pasa a la próxima reunión con los mentores.
2. Principio de gobierno de la enmienda: NO TRATADO en esta reunión; pasa a la próxima reunión con los mentores.

## Confirmación
Confirmado por la autora el 07/10/2026. Cumple la condición 1 de la tanda 1 (checklist, P6).
