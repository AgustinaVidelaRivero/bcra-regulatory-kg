# Laudo D-g — Alcance del corpus en la tesis

**Estado: FIRMADO — Agustina Videla Rivero, 27/08/2026.** Decisión de referencia: reunión de
mentores del 26/08/2026. Desde esta firma, D-g es vigente y rige el plan; los ítems del §4
rastrean su implementación pendiente.

## 1. Resolución

El **objeto central de la tesis es el grafo de conocimiento escalado de la regulación del Banco
Central de la República Argentina**. Los cinco Textos Ordenados del subset dejan de ser el objeto
del estudio y pasan a ser, explícitamente, el **conjunto de desarrollo** (train/eval) sobre el
que se construyó, se ajustó y se validó el método.

En consecuencia:

- Todo el trabajo experimental hecho sobre los cinco TOs —EV2, el circuito de refinamiento, la
  atribución causal de fallas, las ablaciones de retrieval, el head-to-head— **se presenta como
  lo que es**: el desarrollo y la validación del método, con sus resultados sinceros. No se
  descarta nada.
- El resultado que sostiene la tesis se mide sobre el **recurso final**: una evaluación única
  sobre el grafo escalado, pre-registrada antes de mirarla (B6.3).
- El escalado deja de ser un capítulo opcional de escalabilidad y pasa a ser **ruta crítica**.

## 2. Fundamento

Tal como se planteó en la reunión: sostener la tesis sobre los cinco Textos Ordenados sería
**sobreajustar el documento** al material sobre el que se iteró. Un trabajo cuyo aporte es un
recurso —un KG de la regulación— debe presentar y evaluar ese recurso en su forma final, no en el
subconjunto que sirvió para desarrollarlo.

La formulación operativa que ordena el proyecto es el marco desarrollo/test: sobre el conjunto de
desarrollo se itera y se mide sin restricción; sobre el conjunto de test se mide una sola vez.
Este marco queda incorporado al plan como **principio 10**, y generaliza el principio 7 (EV2 es
examen) llevándolo del nivel del eval set al nivel del corpus.

## 3. Alcance y qué NO decide este laudo

- **No decide el scope del escalado** (qué TOs, en qué orden, con qué presupuesto): eso es D5 /
  B5.5, que sigue pendiente de laudo propio. Lo que este laudo sí fija es que ese laudo ya no
  decide *si* se escala.
- **No autoriza escalar todavía**: la validación del esquema (bloque ESQ) es prerrequisito
  bloqueante, porque una vez escalado el corpus, revertir el esquema es inviable por costo.
- **No invalida ni re-mide nada sellado**: EV2 y todas las mediciones del conjunto de desarrollo
  conservan su valor y su lectura; cambian de rol narrativo, no de contenido.
- **No modifica el principio 9**: el grafo evaluado se sella y las correcciones producen una
  release posterior, también en el conjunto de test.

## 4. Consecuencias operativas — checkbox de implementación

Un laudo sin consecuencia implementada es una deuda silenciosa (lección de A1.6, cuya consecuencia
sobre la app quedó sin implementar hasta que una revisión la detectó). Este laudo se considera
ejecutado cuando:

- [ ] `docs/tesis/main.tex`: reescritura del cierre del párrafo 2 y del enunciado del párrafo 4
      con el marco desarrollo/test, y **retiro del marcador** `[PENDIENTE MENTORES — D-g]`
      (C1.1 tramo 1b).
- [ ] `docs/tesis/main.tex`: objetivo general formulado sobre el corpus completo; objetivos
      específicos incluyen la validación del método sobre el conjunto de desarrollo.
- [ ] `docs/plan_tesis.md`: principio 10 incorporado; B5/B6 re-tierados a T1; bloque ESQ
      declarado bloqueante del escalado; B6.3 rediseñada como evaluación final con pre-registro
      propio; D5/B5.5 re-etiquetada no recortable. *(Anticipado en el plan; se marca al firmar
      el laudo: el checkbox rastrea implementación posterior a la firma — lección A1.6.)*
- [ ] Mención explícita del cambio de alcance en el próximo informe de avance.
