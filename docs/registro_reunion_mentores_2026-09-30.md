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

Puntos técnicos y su resolución:
1. Umbrales: cómo representar las cuantías y los plazos de una norma. Resuelto con la enmienda de umbrales al esquema, firmada, que agrega la propiedad umbral a las entidades de norma.
2. Validación de los valores cerrados: que todos se controlen por código y no solo en las instrucciones. Resuelto con la validación por modelos pydantic.
3. Sujetos que no se pueden mapear al catálogo: definir su proceso. Resuelto con la cuarentena de las menciones sin resolver y su re-resolución por código (U-RERESOL-CAT), sin volver a extraer.
4. Actualización y mantenimiento del grafo: qué cambios exigen reprocesar todo y cuáles no, cómo incorporar normas nuevas, actualizar solo el subgrafo afectado a partir de las comunicaciones que modifican puntos concretos, y un control que avise cuando algo cambia en la fuente. Resuelto con el job de actualización ante cambio normativo (U-JOB-ACT), la tabla de reprocesamiento y el protocolo entre tandas. En la tesis va al capítulo 6.

## Cambios aplicados
Los pedidos de estructura 1 a 8 y los cuatro puntos técnicos, aplicados en la versión de la tesis en Overleaf, donde la autora y los mentores editan. Esa versión entra al repo en la próxima sincronización desde Overleaf, con su commit.

## Validación (entre el 30/09/2026 y el 06/10/2026)
Los mentores validaron en persona el capítulo 3 con los cambios aplicados, sobre la versión en Overleaf. Por decisión de la autora, la evidencia de la validación es este registro, sin confirmación escrita aparte.

## Devolución posterior (07/10/2026)
La devolución de los mentores del 07/10/2026 sobre la estructura del capítulo 3 (tres partes: los documentos, el esquema final presentado primero con tablas, y su validación) es de presentación y no cambia el esquema validado.

## Pendientes de P7
1. Destinos de los ocho límites de la Tabla 4: a determinar por la instancia del plan contra este registro.
2. Principio de gobierno de la enmienda: a determinar por la instancia del plan contra el principio de diseño de este registro.

## Confirmación
Confirmado por la autora el 07/10/2026. Cumple la condición 1 de la tanda 1 (checklist, P6).

## Nota de la mesa (07/10/2026): anclas de los puntos técnicos y precisiones

Verificación contra el repo en HEAD `0ea2d74`, posterior a la confirmación. No cambia el texto confirmado: da el ancla de cada «Resuelto» y
dice dónde la frase es más amplia que lo que hay en el repo. Detalle en el paquete de la mesa (`hechos_acta_3009_insumo_mesa.md`).

1. **Umbrales.**
   - Lo resuelve L-ESQ-R2, FIRMADA (`4ef7650`), §1 «Umbrales».
   - Precisión: L-ESQ-R2 es la enmienda del esquema de la release r2 entera, no una «enmienda de umbrales».
   - El umbral pasa a ser una lista, con tramo literal, valor, unidad, comparación y base, en Restriccion, Obligacion, Condicion y
     Excepcion; Restriccion ya lo tenía como opcional, y Potestad y Definicion no lo llevan.
   - Atar cada valor a su sujeto u operación sigue como límite (trabajo futuro C1.7).
   - Las enmiendas 3 y 5 a L-ESQ-R2 ajustan sus reglas.
2. **Valores cerrados.**
   - Lo resuelve U-PYD (mandato `3ffb99d`; P1 `eb277ce`, P2 `b706d37`, P3 `57a8dd2`): `modelos_r2.py` con pydantic, usados por
     `validador_r2` y por `validador_e1`.
   - Precisión: controlar no es siempre rechazar. La política por campo (`pyd_r2/politica_campos_r2.json`) rechaza unos campos,
     normaliza otros y registra con marca otros. `Operacion.tipo` es texto libre.
   - En r2b quedan 34 y 24 Comunicacion sin `tipo` sin tratar (tablero de correcciones, fila de valores fuera de lista), con su
     corrección en U-OMISIONES-COD.
3. **Sujetos no mapeables.**
   - El proceso lo define L-ESQ-R2, §3 y §4, diseñado en U-LISTAS-NOMAP (`9c5331c`, `acc310e`).
   - La cuarentena de los documentos sin alcance viene de la enmienda 6 a L-ESQ-R2 (parte A FIRMADA).
   - La re-resolución por código es U-RERESOL-CAT (mandato `f87ec4a`; R2 cerrada, `1190a8a`), con la enmienda 4 al protocolo
     (FIRMADA, `53bbd6f`).
   - Precisión: «sin volver a extraer» vale para el catálogo de resolución. Un id nuevo en el catálogo del request, o un rol de alcance
     nuevo, cambia el pedido a E1 y va a la release siguiente (tabla de reprocesamiento, F11 y F13).
4. **Actualización y mantenimiento.**
   - U-JOB-ACT está cerrada (`9278923`, 07/09/2026). Su exclusión de avisos se revocó el 30/09.
   - El control que avisa cuando cambia la fuente, la tabla de reprocesamiento y el empalme son de **U-MANT** (mandato `36edf24`; M1
     `e18d616`, M2 `7ed5ced`, M3 `98400e5`; cerrada el 02/10/2026). El disparo mensual está documentado pero no instalado
     (`data/experiment/mantenimiento/control_sitio/instalacion_disparo_mensual.md`).
   - La actualización de solo el subgrafo afectado es **U-SUBGRAFO**, abierta (plan, B2.11, unidad 13).
   - El protocolo entre tandas (`a304b89`) trata las correcciones entre tandas, no el cambio normativo.
   - En la tesis, el mantenimiento va al capítulo 6. La tabla de reprocesamiento se cita además en la construcción por etapas del
     capítulo 4.

**Pendientes de P7, con lo que hay en el repo** (para la instancia del plan):
1. **El principio de gobierno de la enmienda es otro principio.** Está en el §1 del laudo del esquema congelado
   (`data/experiment/esq/laudo_esquema_congelado.md:15-18`, `2593d4d`): se retira lo que produce falsedad en campo estructurado; se
   acepta con residuo declarado la omisión visible o el error con tasa medida.
   - El principio de diseño de este registro corresponde a los principios 11 y 12 del plan (`docs/plan_tesis.md:301-302`).
   - L-ESQ-R2 los articula: el 11 decide qué representa el esquema, y el §1 qué se emite en una release sellada.
2. **Los ocho límites de la Tabla 4** (la versión enviada el 11/09, `main.tex@ed389c4`).
   - Los cuatro puntos técnicos cubren en parte uno (el 1, hechos con valor n-arios, por el punto 1) y tocan otro sin resolverlo (el
     8, obligaciones sin lista cerrada, por el punto 2).
   - No cubren los otros seis: el supuesto de otra unidad, el vaciamiento, la regla 9, el deber que migra a Condicion, el mismo
     contenido en dos cajas y la calidad entre corridas.
   - Sus destinos hoy son límites declarados, vigilancias o enmiendas ya firmadas.

