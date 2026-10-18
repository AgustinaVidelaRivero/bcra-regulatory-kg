# La regla de lectura del gold de Q12, mitad de ajuste (mesa, §128, 16/10/2026)

Escrita antes de que la autora lea. La decisión de fondo está en el registro, §9: «Yo armo primero un gold propio, a ciegas, sin ver
ninguna sugerencia de un modelo, y el juez se calibra contra ese gold antes de usarlo» (§8), y «Las 20 para ajustar el juez salen de
respuestas de EV2 que ya existen» (`docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md:261-263`, `:294-297`).

## Qué leés

- **20 fichas, G01 a G20** (`fichas/`, o todas juntas en `fichas_G01_a_G20.html` y `fichas_G01_a_G20.md`). Cada una trae:
  - la pregunta;
  - la respuesta, tal cual la dio el sistema. Es lo mismo que vio el juez de EV2: solo el texto, sin las citas del sistema;
  - el ancla normativa, con su página;
  - los criterios del gold de EV2, cada uno con su cita textual de la norma y la página donde está.
- **Las fuentes:** los cinco PDF de `fuentes/`, copias de los de `data/experiment/subset/`, con el mismo sha256. Las páginas de las fichas
  son las de esos PDF, contadas desde 1.
- **Las fichas no dicen** de qué sistema sale cada respuesta, ni traen ningún veredicto o sugerencia de un modelo: ni del juez, ni de la
  adjudicación de EV2.
  - Algunas respuestas nombran «el grafo» o «el Knowledge Graph», porque los tres sistemas navegan un grafo. Eso no dice cuál.
  - Los criterios no son veredictos: son el gold sellado de EV2 (`9c44516`), con el que el juez mide cada respuesta.

## Lo que no abrís mientras leés

- `clave_para_despues/`, que dice el sistema de cada ficha;
- nada de EV2 en el repo: veredictos del juez, adjudicaciones, reportes, trazas. Ahí están los veredictos, y también las respuestas de
  los otros dos sistemas a las mismas preguntas;
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
   - Si decidir pide un experto del dominio, das tu lectura y marcás «necesita experto del dominio» (§8: «lo que necesite uno se marca y se
     declara»).
   - El fragmento es opcional: el pasaje de la respuesta que te decidió.
4. **La respuesta entera:**
   - **la clasificación,** con la misma definición del juez (`prompt_juez_v1.md:43-49`):
     - **abstencion:** la respuesta declara no encontrar o no tener la información que pide la pregunta, aunque agregue contexto;
     - **contenido:** intenta responder con contenido sustantivo;
   - **error fuera de los criterios:** sí o no, y cuál. Por ejemplo, la respuesta afirma algo falso contra la fuente que ningún criterio
     toca. Esto no entra en la comparación por criterio: sirve para ajustar el juez y para la tesis («grounded ≠ correct»);
   - **minutos:** cuánto te llevó, aproximado.
5. **El veredicto de la respuesta no lo elegís:** sale de tus criterios con la regla de EV2 (`data/experiment/ev2_juez/mapping.py:40-54`). Si
   todos están cumplidos, es correcto; si ninguno, incorrecto; si hay de los dos, parcial.

## La planilla

- `planilla_criterios_gold_q12_ajuste.csv`: un renglón por criterio, 82 en total. La llenás con las columnas vacías.
- `planilla_respuestas_gold_q12_ajuste.csv`: un renglón por ficha, 20 en total.
- Se abren con cualquier planilla de cálculo, en UTF-8. No cambiás los nombres de las columnas, ni el orden ni la cantidad de renglones.
- Cómo se va a medir el juez con lo que anotás: `como_se_mide_el_juez_gold_q12.md`.

## El orden y las correcciones

- Leés de G01 a G20, en ese orden.
- Podés volver sobre una ficha anterior y corregirla. Si lo hacés, anotás en su nota «corregida al leer Gxx» y por qué.

## Cuánto te lleva (NO VERIFICADO)

- **Lo que hay:** 20 respuestas, de 264 a 1.505 caracteres (mediana 748; 16.067 en total), y 82 criterios, de 3 a 5 por ficha. Las
  páginas ya están dadas.
- **A 5 a 8 minutos por ficha,** como estimó el diseño de la §108: de 1 h 40 min a 2 h 40 min, más unos 15 minutos para la planilla.
- **Si te sirve,** en dos tandas de 10, con un corte en el medio.

## Al terminar

Guardás las dos planillas en la misma carpeta y avisás. Con eso la mesa abre la clave, cruza tu gold con los veredictos de EV2 (que ya
existen y no se pagan) y reporta las cifras de `como_se_mide_el_juez_gold_q12.md`.
