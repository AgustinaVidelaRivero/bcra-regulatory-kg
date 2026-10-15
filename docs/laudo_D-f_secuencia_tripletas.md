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

## Notas posteriores a la firma

El texto firmado son las 54 líneas de arriba (`966253e`, sha256 `85f48f148444…`) y no cambia.

- **07/10/2026 — el grafo de la validación del instrumento (decisión 1 de la autora al llevar a versión para firmar el pre-registro de
  tripletas, `docs/preregistro_evaluacion_tripletas.md`).** La etapa de validación (B4.2 y B4.3) corre sobre **KG-Tanda0-Desarrollo-r2b-sincola**
  (`2922b72d…`, sello `dde9f44`/`235a295`; «grafo sin cola de la tanda 0»), no sobre KG-Reextraído-r1 como dice la letra de este laudo:
  r2b tiene el esquema congelado y la cadena del escalado, así que la escala de importancia y la regla de presencia se validan sobre el
  vocabulario que después se mide. Cambia el objeto de la validación, no la secuencia ni el doble rol del §5. Si ese grafo se re-sella
  antes del sorteo, vale el sello vigente al sortear.

- **15/10/2026 — el re-sellado único de los grafos r2b de la tanda 0.** Los grafos sellados que cita este documento tienen una versión posterior, del re-sellado único (`docs/mandatos/URESELLADO_T0_resellado_unico_grafos_r2b.md`, firmado; FRENO en `data/experiment/resellado_t0/FRENO_resellado_T0.md`): `2922b72d…` (KG-Tanda0-Desarrollo-r2b-sincola) → `66e745f5…` (KG-Tanda0-Desarrollo-r2b-sincola-rs1, 6.711 nodos y 21.996 aristas). Cambian por el código de U-OMISIONES-COD (`ded41d50`) y por las salidas de R0 (`1d690df3` y `2d0f5277`). El diff por campo y por causa está en `data/experiment/resellado_t0/salidas/`. Los sellados siguen sellados (principio 9); el commit del sello de los nuevos queda en `commit_sellado` de `data/experiment/neo4j/grafos.py`. Si el sorteo es posterior al sello del re-sellado, el sello vigente al sortear es el de `66e745f5…` (KG-Tanda0-Desarrollo-r2b-sincola-rs1). El texto firmado no cambia.
