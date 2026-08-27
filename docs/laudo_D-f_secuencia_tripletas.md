# Laudo D-f — Secuencia de la evaluación intrínseca por tripletas (B4)

**Estado: FIRMADO — Agustina Videla Rivero, 27/08/2026.** Desde esta firma, D-f es vigente y rige
el plan; los ítems de los §4 y §5 rastrean su implementación pendiente.

## 1. Resolución

El **instrumento** de evaluación intrínseca por tripletas (precisión, importancia y recall por
ranking) se construye y se valida sobre **KG-Reextraído-r1**, que pertenece al conjunto de
desarrollo: ahí se itera sobre la escala de importancia, la regla de presencia, el umbral de
acuerdo del juez y el muestreo, sin límite de iteraciones y sin comprometer la validez de la
tesis.

La **medición que cuenta para la tesis** se corre **una única vez sobre el grafo escalado**, como
parte de la evaluación final pre-registrada (B6.3).

La corrida sobre r1 se reporta como **validación del instrumento**, no como el resultado
intrínseco de la tesis; el resultado intrínseco de la tesis es el del recurso final.

## 2. Fundamento

Es aplicación directa del marco desarrollo/test establecido en la reunión de mentores del
26/08/2026 para el conjunto del proyecto, incorporado al plan como **principio 10**: sobre el
conjunto de desarrollo se itera y se mide sin restricción; sobre el conjunto de test se mide una
sola vez, con pre-registro previo.

La alternativa —correr las tripletas una sola vez y directamente sobre el grafo escalado— dejaría
el instrumento sin validar en el momento en que produce el número que la tesis reporta, con dos
riesgos concretos: un umbral de acuerdo del juez calibrado sobre nada, y ninguna posibilidad de
detectar defectos del instrumento sin quemar la medición del conjunto de test.

## 3. Atribución

Esta aplicación específica a la secuencia de la evaluación por tripletas **es decisión de la
autora**. La reunión del 26/08 estableció el marco desarrollo/test para el proyecto, pero **no
trató explícitamente la secuencia de B4**; extenderlo a las tripletas es una inferencia razonable,
no una indicación recibida, y se registra como tal para no atribuir a terceros una decisión
propia.

## 4. Acción comprometida

- [ ] Mencionar esta decisión, con su atribución explícita, en el **próximo informe de avance** a
      los mentores, para que puedan objetarla si el marco no se aplicaba de este modo.

## 5. Consecuencias operativas — checkbox de implementación

- [ ] B4.1 (pre-registro de tripletas) declara el **doble rol** de la evaluación: validación del
      instrumento sobre r1 y medición única sobre el grafo escalado, con los criterios de lectura
      diferenciados para cada uno.
- [ ] B4.2–B4.4 se reportan explícitamente como validación del instrumento sobre el conjunto de
      desarrollo (no como resultado intrínseco de la tesis).
- [ ] B6.3 (evaluación final) incorpora las tripletas dentro de su pre-registro sellado.
- [ ] La release r2 sigue el principio 9: el grafo evaluado se sella y las correcciones que la
      evaluación motive se aplican en una versión posterior, declarada como tal.
