# La adjudicación de B6.3: qué hay en esta carpeta y cómo se lee

Para leer a ciegas, antes de ver cualquier cifra de B6.3. La decisión: «Lo dudoso de B6.3, todo para mí.» (registro, §9). El
veredicto de estas respuestas lo pone tu adjudicación, no el mapping del juez (`docs/preregistro_evaluacion_fidelidad_ev2.md:39-41`).

## Qué hay

- **22 fichas, A01 a A22** (`fichas/`), y las mismas todas juntas en `fichas_A01_a_A22.md`, y en `fichas_A01_a_A22.html` para leer en el navegador.
  Cada ficha trae la pregunta, la respuesta tal cual la vio el juez y todos los criterios del gold, cada uno con su cita textual.
- **Los criterios que adjudicás** van marcados **A ADJUDICAR** en cada ficha. Los demás no los marcás: conservan lo que dio el juez.
  En total son 22.
- **`planilla_adjudicacion_b63.csv`:** la planilla, un renglón por criterio que adjudicás, vacía. Su copia vacía, `planilla_adjudicacion_b63_vacia.csv`, con su sha256 en
  `planilla_adjudicacion_b63_vacia.sha256`.
- **`sellar_planilla_adjudicacion_b63.py`:** el sello de la planilla, al terminar.

Las fichas no dicen de qué sistema sale cada respuesta, ni traen ningún veredicto del juez, la sesión ni el documento. Algunas respuestas
nombran su fuente («el grafo», «los fragmentos») o sus herramientas: van tal cual las vio el juez, y eso se declara (D-10). Juzgás el
contenido, no la fuente que nombra.

## Cómo leés cada criterio marcado

Es la misma vara del juez (`data/experiment/ev2_juez/prompt_juez_v1.md:17-23`) y la de Q8:
- **cumplido:** la respuesta contiene el contenido normativo que exige el criterio. No hace falta literalidad: vale la equivalencia
  normativa, con los mismos sujetos, calificadores, modalidades, plazos y umbrales;
- **no cumplido:** el contenido falta, o la respuesta afirma algo que lo contradice.

Elegís siempre una de las dos. El comentario es libre: ahí va si dudaste, si el criterio te parece mal planteado o si pide un experto
del dominio. Leés de A01 a A22, en ese orden; si corregís una ficha anterior, lo anotás en su comentario.

## Lo que no abrís mientras leés

- nada de B6.3 en `fuera_del_repo/banco_b63/` ni en el repo (`data/experiment/banco_mcp/b63/real/`): los juicios del juez y las
  sesiones de cada sistema;
- la clave, que dice de qué sistema sale cada ficha: está en el paquete de la revisión, no en esta carpeta;
- ningún resumen, conversación ni salida de un modelo sobre estas respuestas.

## Al terminar

1. Exportás la planilla a CSV (con «,» o con «;»), con este mismo nombre, en esta carpeta.
2. Corrés, desde esta carpeta: `python3 sellar_planilla_adjudicacion_b63.py`. Controla la planilla y escribe
   `sello_adjudicacion_b63.txt`. No pisa un sello que ya existe.
3. Avisás. Con eso, la etapa C calcula el veredicto de cada respuesta: el mapping de EV2 sobre tus marcas y el modal del juez de los
   demás criterios.
