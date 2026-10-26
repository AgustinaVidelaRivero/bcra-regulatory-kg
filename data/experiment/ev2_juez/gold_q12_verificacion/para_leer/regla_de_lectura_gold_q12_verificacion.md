# La regla de lectura del gold de Q12, mitad de verificación (mesa, §276, 25/10/2026)

Escrita antes de que la autora lea. Es la de la mitad de ajuste (§128), con las respuestas de A2.2. La decisión de fondo está en el
registro, §9, tal cual: «Las 20 para verificarlo salen de las respuestas de A2.2 y sirven también como su muestra simétrica. Las leo a
ciegas, antes de ver cualquier veredicto.» (`docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md:295-297`).

## Qué leés

- **20 fichas, VG01 a VG20** (`fichas/`, o todas juntas en `fichas_VG01_a_VG20.html` y `fichas_VG01_a_VG20.md`). Cada una trae:
  - la pregunta;
  - la respuesta, tal cual la dio el sistema. Es lo mismo que vio el juez: solo el texto, sin las citas del sistema;
  - el ancla normativa, con su página;
  - los criterios del gold de EV2, cada uno con su cita textual de la norma y la página donde está.
- **Las fuentes:** los cinco PDF de `fuentes/`, copias de los de `data/experiment/subset/`, con el mismo sha256. Las páginas de las fichas
  son las de esos PDF, contadas desde 1.
- **Las fichas no dicen** de qué sistema sale cada respuesta (el grafo o uno de los dos sistemas por fragmentos), ni traen ningún
  veredicto o sugerencia de un modelo.
  - Algunas respuestas nombran su fuente («el grafo», «los fragmentos»). Van tal cual las vio el juez, y eso puede decir de qué sistema
    salen: se declara (D-10). Juzgás el contenido, no la fuente que nombra.
  - Los criterios no son veredictos: son el gold sellado de EV2, con el que el juez mide cada respuesta.

## Lo que no abrís mientras leés

- nada de A2.2 en el repo: los juicios del juez, las sesiones de cada sistema, la población;
- nada de EV2 en el repo;
- ningún resumen, conversación ni salida de un modelo sobre estas respuestas.

## Cómo leés cada ficha

1. **La pregunta y la respuesta,** enteras.
2. **La fuente:** abrís el PDF en la página del ancla y leés el punto, y donde haga falta, las páginas de las citas.
3. **Cada criterio, por separado:** ¿la respuesta contiene el contenido normativo que exige el criterio? Es la misma vara del juez
   (`data/experiment/ev2_juez/prompt_juez_v1.md:17-23`), para que se pueda comparar:
   - **cumplido:** la respuesta lo contiene. No hace falta literalidad: vale la equivalencia normativa, con los mismos sujetos,
     calificadores, modalidades, plazos y umbrales. Una paráfrasis fiel cumple; una versión que omite un calificador que cambia el
     alcance, no;
   - **no_cumplido:** el contenido falta, o la respuesta afirma algo que lo contradice.
   - Elegís siempre una de las dos. Si no estás segura, elegís la que te parezca y marcás «dudosa para mí».
   - Leés el criterio tal como está escrito. Si la cita o la fuente no lo sostienen así, lo marcás como «criterio mal planteado» y lo
     contás en la nota, pero el veredicto sigue siendo sobre el criterio escrito.
   - Si decidir pide un experto del dominio, das tu lectura y marcás «necesita experto del dominio».
   - El fragmento es opcional: el pasaje de la respuesta que te decidió.
4. **La respuesta entera:**
   - **la clasificación,** con la misma definición del juez (`prompt_juez_v1.md:43-49`):
     - **abstencion:** la respuesta declara no encontrar o no tener la información que pide la pregunta, aunque agregue contexto;
     - **contenido:** intenta responder con contenido sustantivo;
   - **error fuera de los criterios:** sí o no, y cuál. Por ejemplo, la respuesta afirma algo falso contra la fuente que ningún criterio
     toca. No entra en la comparación por criterio: es la columna que pidió la autora para estas 20, a ciegas al brazo (registro, §28);
   - **minutos:** cuánto te llevó, aproximado.
5. **El veredicto de la respuesta no lo elegís:** sale de tus criterios con la regla de EV2 (`data/experiment/ev2_juez/mapping.py:40-54`).

## La planilla

- `planilla_criterios_gold_q12_verificacion.csv`: un renglón por criterio. La llenás con las columnas vacías.
- `planilla_respuestas_gold_q12_verificacion.csv`: un renglón por ficha, 20 en total.
- Se abren con cualquier planilla de cálculo, en UTF-8. No cambiás los nombres de las columnas, ni el orden ni la cantidad de renglones.
- Cómo se mide el juez con lo que anotás: `como_se_mide_el_juez_gold_q12_verificacion.md`.

## El orden y las correcciones

- Leés de VG01 a VG20, en ese orden.
- Podés volver sobre una ficha anterior y corregirla. Si lo hacés, anotás en su nota «corregida al leer VGxx» y por qué.

## Cuánto te lleva (NO VERIFICADO)

- En la mitad de ajuste te llevó unas 1 h 25 min para 20, según tu cuenta (Q8, `:66-67`). Si te sirve, en dos tandas de 10.

## Al terminar

1. Exportás las dos planillas a CSV (con «,» o con «;»), con estos mismos nombres, en esta carpeta.
2. Corrés, desde esta carpeta: `python3 sellar_planillas_gold_q12_verificacion.py`. Controla las dos planillas y escribe
   `sello_gold_q12_verificacion.txt`. No pisa un sello que ya existe.
3. Avisás. Con eso la mesa abre la clave, cruza tu lectura con los juicios del juez y reporta las cifras del criterio de aceptación.
