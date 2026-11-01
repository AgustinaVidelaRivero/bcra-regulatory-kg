# La regla de lectura de la muestra de control del juez de B6.4 (mesa, §383, 01/11/2026)

Escrita antes de que la autora lea. Es la de B6.3 (`data/experiment/banco_mcp/b63/control_36/para_leer/regla_de_lectura_control_36_B63.md`),
con lo que fija el pre-registro de B6.4 (§5, `docs/preregistro_B6_4_evaluacion_confirmatoria_varios_puntos.md`, firmado en `55ee1a5a`,
renglones 201 a 207):
- 36 respuestas, 12 por brazo de los tres de las comparaciones principales, y 4 de cada tipo en cada brazo;
- la columna «error fuera de los criterios», a ciegas al brazo.

## Qué leés

- **36 fichas, C01 a C36** (`fichas/`, o todas juntas en `fichas_C01_a_C36.html` y `fichas_C01_a_C36.md`). Cada una trae:
  - la pregunta;
  - la respuesta, tal cual la dio el sistema. Es lo mismo que vio el juez: solo el texto, sin las citas del sistema;
  - los criterios de la pregunta, cada uno con su cita textual de la norma, en el orden en que los recibió el juez.
- **Las fichas no dicen:**
  - de qué sistema sale cada respuesta: el grafo o uno de los dos sistemas por fragmentos. El cuarto brazo de la corrida no está en la
    muestra;
  - de qué tipo es la pregunta: agregación, remisión, o condición y excepción;
  - ningún veredicto ni sugerencia de un modelo;
  - el texto ordenado de donde sale la pregunta, su documento ni sus páginas.
- **Algunas respuestas nombran su fuente** («el grafo», «los nodos», «los fragmentos», «los pasajes»). Van tal cual las vio el juez, y eso
  puede decir de qué sistema salen: se declara (D-10). Juzgás el contenido, no la fuente que nombra.
- **Los criterios no son veredictos:** son el gold de las preguntas de B6.4, con el que el juez mide cada respuesta.
- **Las 36 preguntas son distintas:** ninguna se repite.
- **Ninguna de las 36 pasó por tu adjudicación:** el sorteo deja fuera de la muestra las respuestas que van a la adjudicación y las que
  no tienen sus tres juicios en la lectura estricta (`data/experiment/banco_mcp/b64/control_36/sorteo/regla_sorteo_control_36_B64.md`).
  Una pregunta sí puede estar en las dos lecturas, con otra respuesta.

## Cuándo

El §13, punto 6, del pre-registro pone la muestra de 36 después de la lectura tolerante y la adjudicación. Leés las fichas cuando
termines la adjudicación.

## Lo que no abrís mientras leés

- nada de `fuera_del_repo/banco_b64/`: las sesiones de cada sistema, los juicios del juez y la población;
- de `fuera_del_repo/analisis_b64_corr/salidas/`, nada más que las consolas que ya leíste;
- ninguna clave: ni la del sorteo (`fuera_del_repo/banco_b64_control_36/clave_para_despues/`) ni la de tu adjudicación;
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
     toca.
     - En la planilla va en dos columnas, «error fuera de los criterios (sí/no)» y «cuál», como en B6.3.
     - No entra en la comparación por criterio: se cuenta aparte, por brazo, cuando se abra la clave.
     - Va en las 36. El pre-registro de B6.4 trae la columna y no la cláusula de B6.3 que la dejaba salir si las horas no daban, así que
       el sellador no sella con la columna vacía;
   - **minutos:** cuánto te llevó, aproximado.
5. **El veredicto de la respuesta no lo elegís:** sale de tus criterios con la regla de EV2 (`data/experiment/ev2_juez/mapping.py:40-54`).

## Las planillas

- `planilla_criterios_control_36_B64.csv`: un renglón por criterio, 135 en total (la cuenta que dio el sorteo). La llenás en las columnas
  vacías.
- `planilla_respuestas_control_36_B64.csv`: un renglón por ficha, 36 en total.
- Se abren con cualquier planilla de cálculo, en UTF-8. No cambiás los nombres de las columnas, ni el orden ni la cantidad de renglones.
- Cómo se mide el juez con lo que anotás: `como_se_mide_el_juez_control_36_B64.md`.

## El orden y las correcciones

- Leés de C01 a C36, en ese orden.
- Podés volver sobre una ficha anterior y corregirla. Si lo hacés, anotás en su nota «corregida al leer Cxx» y por qué.

## Cuánto te lleva (NO VERIFICADO)

En B6.3, entre la copia de las planillas vacías (10:46:07) y el sello de tu lectura (13:55:14) del 29/10 pasaron 3 h 09 min, con 130
criterios (`data/experiment/banco_mcp/b63/control_36/copia_vacia/sha256_copia_vacia_control_36_B63.txt` y
`para_leer/sello_control_36_B63.txt`). Es un techo: la copia es anterior a tu primera ficha. Con 135 criterios, unas 3 h. Si te sirve,
en tres tandas de 12.

## Al terminar

1. Exportás las dos planillas a CSV (con «,» o con «;»), con estos mismos nombres, en esta carpeta.
2. Corrés, desde esta carpeta, el sellador (el comando está en las instrucciones de la mesa). Controla las dos planillas y escribe
   `sello_control_36_B64.txt`. No pisa un sello que ya existe.
3. Avisás. Con eso la mesa controla el sello, abre la clave, cruza tu lectura con los juicios del juez y reporta las cifras.
