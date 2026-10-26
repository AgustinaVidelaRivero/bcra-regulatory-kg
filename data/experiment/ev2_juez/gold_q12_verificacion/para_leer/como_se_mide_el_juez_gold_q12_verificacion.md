# Cómo se mide el juez con el gold de Q12, mitad de verificación (mesa, §276, 25/10/2026)

Fijado antes de que la autora lea. Es el de la mitad de ajuste (§128), con las dos propuestas que la autora confirmó para esa mitad
(16/10 y 17/10, §145), y el criterio de aceptación, que rige en esta.

## Qué se compara

- **Del lado del juez:** sus juicios de N = 1 de A2.2 sobre estas mismas 20 respuestas, ya hechos (paso 3): el modal de sus tres
  repeticiones por criterio (`modales`), el veredicto de la respuesta (`veredicto_pregunta`) y la clasificación modal, por id opaco
  (`data/experiment/banco_mcp/a2_2/juez/n1/agregados_n1_ciego.json`). Es el juez de EV2 tal cual: `claude-sonnet-4-6` con el prompt v1
  congelado (`fd446f8e…`; pre-registro de A2.2, §4).
- **Del lado de la autora:** las dos planillas de esta carpeta, selladas.
- **El cruce:** la mesa lo hace después del sello, abriendo la clave del sorteo. Antes, nadie mira los juicios de esas 20.
- Ninguna de las 20 es una `requiere_adjudicacion` (la regla del sorteo): ningún criterio del juez es «dudoso».

## Las cifras

1. **Acuerdo por criterio:** mismo veredicto del juez y de la autora, sobre todos los pares (respuesta, criterio), con su Wilson al 95 %.
2. **Acuerdo por respuesta,** sobre las 20: mismo veredicto de la respuesta (correcto, parcial o incorrecto). El de la autora sale de
   sus criterios con la misma regla del juez (`data/experiment/ev2_juez/mapping.py:40-54`).
3. **Las dos direcciones del error,** por criterio y por respuesta:
   - A: el juez acredita lo que la autora no (juez «cumplido», autora «no_cumplido»);
   - B: el juez no acredita lo que la autora sí (juez «no_cumplido», autora «cumplido»).
4. **La clasificación abstención o contenido:** acuerdo sobre las 20.
5. **Lo que se informa aparte,** con su lista de pares: los criterios marcados «dudosa para mí», «necesita experto del dominio» o
   «criterio mal planteado»; los errores fuera de los criterios; los minutos.
- **Las marcas de la autora** (la propuesta confirmada en la §145): la cifra principal va sobre todos los pares, con todas las marcas
  adentro; al lado, la misma cifra sin los pares marcados «necesita experto del dominio» o «criterio mal planteado».

## El criterio de aceptación

- Tal cual (registro, §9, `:298-299`): «El criterio de aceptación, como lo proponés: en la mitad de verificación, Wilson inferior de al
  menos 0,85 por criterio y al menos 18 de 20 por respuesta. Si no se cumple, frenás y decido.»
- Y si no se cumple, la decisión ya tomada, la 3 de Q8, tal cual: «si la verificación no pasa, B6.3 se juzga con el juez, la cifra se
  informa con su acuerdo medido y todo lo dudoso va a mi lectura».
- La cifra que decide es la principal, con todas las marcas adentro.
