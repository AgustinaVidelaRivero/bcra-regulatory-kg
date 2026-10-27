# La cobertura de T con la regla D-9: el control de 30 (para firmar)

Para firmar antes del sorteo. Fija la población, la semilla y cómo se lee la presencia de la cobertura de T, que ningún texto firmado
fijaba: ni el §7 del pre-registro de tripletas (`4afbe511`) ni el §10.1 del de B6.3 (`adf20f3b`) dicen de dónde salen las 30, con qué
semilla ni cómo se leen, y no hay semilla para los 600 fragmentos.

## 1. Lo que rige

- **D-9, ampliada** (registro de decisiones, §99, decisión 10, sobre el borrador del pre-registro de B6.3), tal cual: «si el juez de
  presencia no pasa en V, o si la cobertura de V no cerró el miércoles 28 a las 18:00, la cobertura de T se informa con la presencia que
  yo decido en el control de 30, con su intervalo de Wilson y sin la cifra del juez, declarada como medición humana sobre 30.»
- **La decisión de la autora del 27/10/2026** (recibida a las 10:24:11), tal cual: «La cobertura de T: la opción (a), la mínima que
  cumple D-9. Escribí para que firme, antes del sorteo, la población, la semilla y cómo leo la presencia. La extracción va en un hueco
  sin otro paso pago, después de N6 y antes de B6.3, y mi presencia de las 30, el miércoles antes de las 18:00.»
- **La población, la decisión de la autora del 27/10/2026** (recibida a las 10:49:03), tal cual: «la población usa los mismos documentos que
  el §3.1 del pre-registro de B6.3, los 77 elegibles, sin los 14 TOs de N3 ni los contaminados. La cobertura mide la extracción del
  grafo, y en un documento que recibió una corrección hecha para él sale mejor por construcción. Así la tesis tiene un solo conjunto de
  test. Es más estricto que la letra del §7 de tripletas, lo decido antes del sorteo y se declara en el documento.» Se declara acá: el
  §7 del pre-registro de tripletas pide solo que los fragmentos sean disjuntos de los 15 y de los 5 de desarrollo.
- **Lo que no corre, declarado como desvío del §5 del pre-registro de tripletas:** los 600 fragmentos, el puntaje de importancia
  (5.4), la calibración del orden (5.5), el juez de presencia (5.6, paso 2) y el recall@k (5.7). La cifra de la cobertura de T es la
  presencia de las 30.

## 2. La población

Un fragmento es una unidad de la E0 del grafo evaluado (`data/experiment/tanda_final/t3/acumulado/e0_acumulado_128_r2b/`, en HEAD) que
cumple las cuatro cosas:
1. **es terminal y su texto propio tiene de 80 a 1.500 caracteres** (5.1 del pre-registro de tripletas);
2. **es de uno de los 77 documentos elegibles del §3.1 del pre-registro de B6.3** (decisión de la autora, §1), que están en
   `data/experiment/esq/cobertura_T_tos_poblacion_2026-10-27.json`, en el mismo commit que este documento. Son el conjunto de los
   documentos del sorteo de documentos de B6.3, sellado el 23/10/2026 (sha256 `4e751e23…`), sin su orden ni sus olas: los 78 de
   `elegibles_O2.json` sin `rdbcra`, y sin contaminados. Como en el §3.1, quedan fuera los cinco de desarrollo, los 15 de
   `documentos_excluidos_evaluacion_final.json` y los 14 TOs de N3;
3. **está en el grafo evaluado** (§10.1 del pre-registro de B6.3): al menos un nodo del grafo evaluado tiene una procedencia en esa
   unidad; no es de una unidad de la cola humana, que el grafo sin cola no trae; ni de una unidad cuya extracción terminó con error en
   la cadena del grafo evaluado, según sus registros sellados;
4. **no es un ancla de EV2 ni de los pares sintéticos v3 y v4, ni uno de sus descendientes** (5.1).
La ejecutora la arma por código desde HEAD y la sella con el sorteo: su lista en claro, su sha256 y sus cuentas por TO y por cada
exclusión.

## 3. La semilla y el sorteo

- **Semilla:** `B4-TRIPLETAS-T:cobertura:2026-10-27`.
- **Método:** `random.Random(semilla).sample(sorted(población), 30)`, sobre las claves `to::unidad` ordenadas, como el de V. El orden
  sorteado es el orden de lectura.
- **El acta,** sellada con su sha256 y su hora antes de cualquier extracción: la población, la muestra y sus sha256.

## 4. La extracción y el subgrafo

- **La extracción abierta** (5.3): `claude-opus-5-5`, que no es el extractor del grafo evaluado (`claude-haiku-4-5`), con el prompt de
  extracción de la vía de cobertura de V sin cambiarlo (`TEXTO_EXTRACCION` de `prompts_cob_v.py` de U-TRIP-V-COB, versión `v1`), una
  tripleta por fragmento, con su tramo literal. El código verifica el tramo
  contra el texto; sin tramo verificado, la tripleta se descarta y se cuenta, y ese fragmento sale del denominador.
- **El subgrafo candidato** (5.6, paso 1): la regla de V con la política P1 que decidió la autora para toda la vía de cobertura (la
  unidad, las de sus ancestros que le heredan texto y solo sus hijos directos), en la forma compacta, con las aristas de contenido.
- **El paso pago:** solo las 30 extracciones, en un hueco sin otro paso pago, después de N6 y antes de B6.3. Tope USD 1, con freno en
  0,60.

## 5. Cómo lee la autora la presencia

Por cada una de las 30, la hoja trae el fragmento (texto propio y heredado), la tripleta con su tramo y su subgrafo candidato. La autora
marca, sin ninguna propuesta de un modelo sobre la presencia:
- **cada componente** (sujeto, predicado y objeto): expresado, parcial o ausente, y el id del nodo o de la arista que lo expresa;
- **si la tripleta es correcta según el fragmento:** sí, no o no decidible.
El código controla que lo nombrado exista en el subgrafo y computa con la regla del 5.6: **presente**, los tres expresados; **parcial**,
sujeto y objeto expresados con el predicado parcial, o dos expresados y uno parcial; **ausente**, el resto.

## 6. Lo que se informa

- **La presencia:** presentes / decididas, con Wilson al 95 %, y las parciales aparte, sobre las 30 menos las descartadas en la
  extracción. **Cruda y depurada:** la depurada saca las tripletas que la autora marcó incorrectas según el fragmento, que se cuentan
  como errores del gold (5.8).
- **Al lado:** las descartadas en la extracción y las no decidibles, cada una con su cuenta.
- **Declarado:** es una medición humana sobre 30, sin la cifra del juez (D-9), y no corren los 600 ni el ranking (§1).

## Firma

Firmado por la autora con el commit que agrega este documento. No se modifica después de la firma: un cambio va en una nota fechada al
pie.
