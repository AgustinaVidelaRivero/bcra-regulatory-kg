# Cómo se mide el juez con la muestra de control de B6.3 (mesa, unidad C36_a, 29/10/2026)

Fijado antes de que la autora lea. Es el de la mitad de verificación de Q8
(`data/experiment/ev2_juez/gold_q12_verificacion/para_leer/como_se_mide_el_juez_gold_q12_verificacion.md`), con lo que fija el
pre-registro de B6.3 (§7.3, `docs/preregistro_B6_3_evaluacion_final.md:406-418`).

## Qué se compara

- **Del lado del juez:** sus juicios de B6.3 sobre estas mismas 36 respuestas, ya hechos: el modal de sus tres repeticiones por criterio
  (`modales`), el veredicto de la respuesta (`veredicto_pregunta`) y la clasificación modal, por id opaco
  (`fuera_del_repo/banco_b63/juez/agregados_b63_ciego.json`). Es el juez de EV2 tal cual: `claude-sonnet-4-6` con el prompt v1 congelado
  (`fd446f8e…`; pre-registro de B6.3, §7.1).
- **Del lado de la autora:** las dos planillas de esta carpeta, selladas.
- **El cruce:** la mesa lo hace después del sello, abriendo la clave del sorteo, con `../cruce/cruce_control_36_B63.py`. El cruce controla
  primero el sello y las planillas, y recién después abre la clave y los juicios del juez; si el sello no da, frena sin abrirlos.
- Ninguna de las 36 es una `requiere_adjudicacion` (la regla del sorteo): ningún criterio del juez es «dudoso».

## Las cifras, por tipo (varios puntos: 27 respuestas; dato directo: 9) y en total

1. **Acuerdo por criterio:** mismo veredicto del juez y de la autora, sobre todos los pares (respuesta, criterio), con su Wilson al 95 %.
2. **Acuerdo por respuesta:** mismo veredicto de la respuesta (correcto, parcial o incorrecto). El de la autora sale de sus criterios con
   la misma regla del juez (`data/experiment/ev2_juez/mapping.py:40-54`). Se informa sin umbral.
3. **Las dos direcciones del error,** por criterio y por respuesta:
   - A: el juez acredita lo que la autora no (juez «cumplido», autora «no_cumplido»);
   - B: el juez no acredita lo que la autora sí (juez «no_cumplido», autora «cumplido»).
4. **La clasificación abstención o contenido:** acuerdo sobre las 36.
5. **El error fuera de los criterios:** cuántas respuestas lo tienen, por brazo (de 12 cada uno) y por tipo, con sus fichas. No entra en
   las cifras de acuerdo. Si la columna salió (vacía en las 36), se declara.
6. **Lo que se informa aparte,** con su lista de pares: los criterios marcados «dudosa para mí», «necesita experto del dominio» o
   «criterio mal planteado»; los minutos.
- **Las marcas de la autora:** la cifra principal va sobre todos los pares, con todas las marcas adentro; al lado, la misma cifra sin los
  pares marcados «necesita experto del dominio» o «criterio mal planteado».

## El piso de varios puntos

- Tal cual (§7.3): «en varios puntos, el piso de Q12 por criterio: Wilson inferior de al menos 0,85»; «el acuerdo por respuesta se
  informa sin umbral».
- El Wilson inferior de varios puntos se compara sin redondear, sobre la cifra principal, con todas las marcas adentro. Dato directo se
  informa sin piso.
- Si no llega, tal cual (§7.3): «si no llega al piso, la cifra de varios puntos va con el acuerdo medido al lado, la hipótesis secundaria
  se declara como medida con ese juez, y lo dudoso va a la lectura de la autora.»
