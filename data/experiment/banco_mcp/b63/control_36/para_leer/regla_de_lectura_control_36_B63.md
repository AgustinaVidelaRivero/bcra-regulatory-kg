# La regla de lectura de la muestra de control del juez de B6.3 (mesa, unidad C36_a, 29/10/2026)

Escrita antes de que la autora lea. Es la de la mitad de verificación de Q8
(`data/experiment/ev2_juez/gold_q12_verificacion/para_leer/regla_de_lectura_gold_q12_verificacion.md`), con las respuestas de B6.3 y lo
que fija su pre-registro (§7.3, `docs/preregistro_B6_3_evaluacion_final.md:406-418`): 36 respuestas, 12 por brazo, 9 de varios puntos y 3
de dato directo en cada uno; el acuerdo del juez se informa por tipo; la columna «error fuera de los criterios (sí o no, y cuál)», a
ciegas al brazo; y la muestra se lee «apenas esté».

## Qué leés

- **36 fichas, C01 a C36** (`fichas/`, o todas juntas en `fichas_C01_a_C36.html` y `fichas_C01_a_C36.md`). Cada una trae:
  - la pregunta;
  - la respuesta, tal cual la dio el sistema. Es lo mismo que vio el juez: solo el texto, sin las citas del sistema;
  - los criterios de la pregunta, cada uno con su cita textual de la norma.
- **Las fichas no dicen** de qué sistema sale cada respuesta (el grafo o uno de los dos sistemas por fragmentos), ni de qué tipo es la
  pregunta (varios puntos o dato directo), ni traen ningún veredicto o sugerencia de un modelo. Tampoco traen el texto ordenado de donde
  sale la pregunta, su documento ni sus páginas: B6.3 deja el TO fuera de la ficha.
  - Algunas respuestas nombran su fuente («el grafo», «los nodos», «los fragmentos», «los pasajes»). Van tal cual las vio el juez, y eso
    puede decir de qué sistema salen: se declara (D-10). Juzgás el contenido, no la fuente que nombra.
  - Los criterios no son veredictos: son el gold de las preguntas de B6.3, con el que el juez mide cada respuesta.
- Las 36 preguntas son distintas: ninguna se repite.

## Lo que no abrís mientras leés

- nada de B6.3 en el repo (`data/experiment/banco_mcp/b63/`) ni en `fuera_del_repo/banco_b63/`: los juicios del juez, las sesiones de
  cada sistema, la población;
- la clave del sorteo;
- ningún resumen, conversación ni salida de un modelo sobre estas respuestas.

## Cómo leés cada ficha

1. **La pregunta y la respuesta,** enteras.
2. **La fuente:** la cita textual de cada criterio. Si para decidir hace falta leer más de la norma que la cita, lo anotás en la nota.
3. **Cada criterio, por separado:** ¿la respuesta contiene el contenido normativo que exige el criterio? Es la misma vara del juez
   (`data/experiment/ev2_juez/prompt_juez_v1.md:17-23`), para que se pueda comparar:
   - **cumplido:** la respuesta lo contiene. No hace falta literalidad: vale la equivalencia normativa, con los mismos sujetos,
     calificadores, modalidades, plazos y umbrales. Una paráfrasis fiel cumple; una versión que omite un calificador que cambia el
     alcance, no;
   - **no_cumplido:** el contenido falta, o la respuesta afirma algo que lo contradice.
   - Elegís siempre una de las dos. Si no estás segura, elegís la que te parezca y marcás «dudosa para mí».
   - Leés el criterio tal como está escrito. Si la cita no lo sostiene así, lo marcás como «criterio mal planteado» y lo contás en la nota,
     pero el veredicto sigue siendo sobre el criterio escrito.
   - Si decidir pide un experto del dominio, das tu lectura y marcás «necesita experto del dominio».
   - El fragmento es opcional: el pasaje de la respuesta que te decidió.
4. **La respuesta entera:**
   - **la clasificación,** con la misma definición del juez (`prompt_juez_v1.md:43-49`):
     - **abstencion:** la respuesta declara no encontrar o no tener la información que pide la pregunta, aunque agregue contexto;
     - **contenido:** intenta responder con contenido sustantivo;
   - **error fuera de los criterios: sí o no, y cuál.** Por ejemplo, la respuesta afirma algo falso contra la norma que ningún criterio
     toca. Es la columna del pre-registro, «error fuera de los criterios (sí o no, y cuál)», a ciegas al brazo; en la planilla va en dos
     columnas, «error fuera de los criterios (sí/no)» y «cuál», como en la mitad de verificación de Q8. No entra en la comparación por
     criterio: la mesa la cuenta aparte, por brazo, cuando abra la clave. Si las horas no dan, es la primera que sale, declarada
     (pre-registro, §7.3): la dejás vacía en las 36, y el sellador lo anota;
   - **minutos:** cuánto te llevó, aproximado.
5. **El veredicto de la respuesta no lo elegís:** sale de tus criterios con la regla de EV2 (`data/experiment/ev2_juez/mapping.py:40-54`).

## Las planillas

- `planilla_criterios_control_36_B63.csv`: un renglón por criterio, 130 en total. La llenás con las columnas vacías.
- `planilla_respuestas_control_36_B63.csv`: un renglón por ficha, 36 en total.
- Se abren con cualquier planilla de cálculo, en UTF-8. No cambiás los nombres de las columnas, ni el orden ni la cantidad de renglones.
- Cómo se mide el juez con lo que anotás: `como_se_mide_el_juez_control_36_B63.md`.

## El orden y las correcciones

- Leés de C01 a C36, en ese orden.
- Podés volver sobre una ficha anterior y corregirla. Si lo hacés, anotás en su nota «corregida al leer Cxx» y por qué.

## Cuánto te lleva (NO VERIFICADO)

- Al ritmo de la mitad de ajuste de Q8, unas 1 h 25 min para 20 según tu cuenta (Q8, `:66-67`), 36 llevarían unas 2 h 30 min. Estas son
  respuestas de B6.3, en su mayoría de varios puntos, y pueden ser más largas. Si te sirve, en tres tandas de 12.

## Al terminar

1. Exportás las dos planillas a CSV (con «,» o con «;»), con estos mismos nombres, en esta carpeta.
2. Corrés, desde esta carpeta: `python3 sellar_planillas_control_36_B63.py`. Controla las dos planillas y escribe
   `sello_control_36_B63.txt`. No pisa un sello que ya existe.
3. Avisás. Con eso la mesa abre la clave, cruza tu lectura con los juicios del juez (`../cruce/cruce_control_36_B63.py`) y reporta las
   cifras por tipo.
