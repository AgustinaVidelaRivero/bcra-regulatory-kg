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

## Notas al pie

- **27/10/2026 — La cobertura de T vuelve al diseño completo del §5 del pre-registro de tripletas, con el juez de presencia del 5.6.**
  FIRMADA por la autora; el commit de la firma es el que agrega esta nota (decisiones de la autora del 27/10/2026, recibidas a las
  15:19:08 y a las 16:15:16; registro de decisiones del 15/10/2026, §141 a §143). Rige desde la firma, antes del sorteo de los 600 y de
  cualquier extracción.
  1. **Por qué,** la autora, tal cual (15:19:08): «quiero correr el diseño completo del §5 del pre-registro de tripletas, el que armé con
     los mentores, en lugar de la versión mínima de 30. Es volver a lo pre-registrado, decidido antes de cualquier extracción.» Y
     (16:15:16): «Quiero la cobertura tal cual el §7 y el §5 del pre-registro de tripletas, con el juez de presencia del §5.6.» Este
     documento sigue fijando la población (§2), la extracción (§4) y la regla de presencia (§5) donde valen; lo que cambia es lo de esta
     nota.
  2. **La población:** la del §2, sin cambios: 2.783 pasajes de los 77 documentos (sha256 de la lista `51c44c7c…`).
  3. **El sorteo:** 600 pasajes, con la semilla `B4-TRIPLETAS-T:cobertura_600:2026-10-27`,
     `random.Random(semilla).sample(sorted(población), 600)`. El acta se sella antes de cualquier extracción, con el orden del sorteo.
  4. **El pool de calibración del juez (5.6):** 20 pasajes más, disjuntos de los 600 y de las 30 de D-9, con la semilla
     `B4-TRIPLETAS-T:cobertura_600:pool_20:2026-10-27`, `random.Random(semilla).sample(sorted(población sin los 600 ni las 30), 20)`, en
     la misma acta. Nunca son de las 100 primeras.
  5. **La extracción (5.3):** la del §4, `claude-opus-5-5` con el prompt y los parámetros de V, una tripleta por pasaje y el tramo
     verificado por código, para los 600, las 30 y los 20 del pool. Sin tramo verificado, la tripleta se descarta y se cuenta. El piloto
     del §8 son los 10 primeros del orden del sorteo: después de ellos, el comando para y muestra la proyección con los tokens medidos.
     Después del piloto se extraen primero los 20 del pool.
  6. **El puntaje y el orden (5.4):** `claude-sonnet-5-5` puntúa cada tripleta de los 600 de 1 a 5 con la rúbrica de V, 3 veces, y se
     ordenan por el puntaje medio, con el desempate por el orden del sorteo.
  7. **El juez de presencia (5.6, el paso 2, con la metodología del §4):**
     - `claude-sonnet-4-6` a temperatura 0, por la API con captura íntegra y caché (`CachingClient`, `evaluacion/llm_cache.py`), con el
       prompt congelado por su sha256 antes de la corrida;
     - clasifica el sujeto, el predicado y el objeto de la tripleta abierta contra el subgrafo, cada uno en expresado, parcial o
       ausente, nombrando el nodo o la arista que lo expresa, y marca cuando requiere adjudicación humana. El código controla que lo
       nombrado exista en el subgrafo: si no existe, la respuesta cuenta como mal formada, se reintenta una vez y, si sigue, esa
       repetición va a adjudicación. El código computa el veredicto con la regla del 5.6;
     - los calibradores: los 20 del pool, resueltos por la autora con su subgrafo a la vista, componente por componente, en su hoja;
     - N = 3, con un cliente, una base de caché y un namespace por repetición, y 0 cruces entre las tres bases antes de agregar (4.4);
       el veredicto modal, y el empate sin consenso, que va a adjudicación;
     - el prompt lleva el candado del 4.7, tal cual: «Este prompt no se modifica sin decisión escrita de la autora. Todo cambio se
       justifica con evidencia del texto de la norma, nunca con la etiqueta esperada de un caso.» Una sola recalibración, declarada,
       con casos del pool y nunca con las 100; si la autora la decide, re-corre el conjunto de calibración y las 100, con su tope;
     - juzga la presencia de las 100 primeras a ciegas de la lectura de la autora, que lee sin ver sus veredictos: sus salidas quedan
       selladas y fuera de la hoja hasta que la autora selle su lectura;
     - su piloto son las 10 primeras, ×3: el comando para y muestra la proyección con los tokens medidos.
  8. **La lectura de la autora,** en una sola hoja, una pasada por renglón, sin la posición, en el orden que da la semilla
     `B4-TRIPLETAS-T:cobertura_600:hoja:2026-10-27`, y la hoja de los 20 del pool, aparte y antes del juez:
     - la importancia (la escala de 3.4) de las 100 primeras y de 30 de control sorteadas entre las posiciones 101 y 300 (5.5), con la
       semilla `B4-TRIPLETAS-T:cobertura_600:control:2026-10-27`, `random.Random(semilla).sample(sorted(posiciones), 30)`;
     - la presencia de las 100 primeras, con su subgrafo a la vista (5.6, el paso 1, con la política de este documento, §4), componente
       por componente, como la del juez;
     - en las ausentes de las 100 primeras, la revisión del 5.8: si la tripleta es correcta según el pasaje (si no, es un error del
       gold, sale del denominador y se cuenta). El error de presencia del 5.8 no aplica, porque la presencia de las 100 es la de la
       autora.
  9. **El acuerdo del juez:** con las dos lecturas selladas, sobre las 100 primeras. Una fila acuerda si el veredicto modal del juez es
     el de la autora, los dos con la regla del 5.6; las que el juez manda a adjudicación o deja sin consenso cuentan como desacuerdo. Se
     informa el acuerdo, el kappa de Cohen sobre las tres clases (en las que deciden los dos) y la distribución de las repeticiones
     (unanimidad, 2 a 1, sin consenso). **El juez escala si acuerda en al menos 84 de 100.** Si pasa, en esta tesis no mide nada más:
     queda validado para medir la presencia sin la autora.
  10. **El orden pasa (5.5)** si al menos 80 de las 100 primeras son esenciales o útiles y esa proporción supera a la de las 30 de
      control. Si no pasa, el recall se informa sobre las que la autora marcó esenciales, sin el orden.
  11. **Lo que se informa (5.7 y 5.8):** el recall@10, @50 y @100 de la lectura de la autora, presentes / k con Wilson al 95 %, con las
      parciales aparte, crudo y depurado, con sus conteos; y el acuerdo del juez, del punto 9. Las ausentes importantes van al backlog
      con su capa, como insumo del grafo corregido, nunca del evaluado.
  12. **Las 30 del control de D-9** (acta `73a6fab307043b3809ac903be235300981cda47adfd8407895a100ead6145ec9`) quedan como la red:
      - se extraen con los 600; si alguna está entre ellos, se usa la misma extracción;
      - su presencia va al principio de la hoja;
      - si la lectura de la autora no se cierra antes del jueves 29/10/2026 a las 18:00, se informa D-9 sobre ellas, como dicen el §5 y
        el §6 de este documento, y al lado lo que esté cerrado del completo (el orden del 5.5, si están sus 130 marcas);
      - si se cierra, van al lado como el control de D-9;
      - el acuerdo del juez no cuenta para ese corte: si la lectura se cierra a tiempo y el juez no, el recall se informa igual y el
        acuerdo, cuando esté.
  13. **Los topes,** con freno por proyección en cada script y el registro del gasto por llamada:
      - la extracción, USD 40, con freno en 34;
      - el puntaje, USD 12, con freno en 10,20;
      - el juez de presencia, USD 25, con freno en 21,25.
      Suman 77 y pasan en 22 los USD 55 del §8 para T: se declara como desvío del §8. La recalibración del 4.7, si la autora la decide,
      lleva su tope aparte, que firma al decidirla.
  - El texto firmado no cambia.

- **27/10/2026 — La lectura de la autora en dos hojas: la importancia, a ciegas de la posición, antes que la presencia.** FIRMADA por
  la autora; el commit de la firma es el que agrega esta nota (decisión de la autora del 27/10/2026, recibida a las 21:49:00; registro
  de decisiones del 15/10/2026, §147). Cambia el punto 8 de la nota anterior. Rige desde la firma, antes de armar las hojas y de
  cualquier extracción.
  1. **Por qué:** la hoja única del punto 8 pedía la presencia solo en las 100 primeras, así que sus columnas decían qué renglón era de
     las 100 y cuál de control, y el 5.5 pide la importancia «mezcladas y sin ver la posición». La autora, tal cual: «El ciego del 5.5:
     la importancia se lee antes, en una hoja aparte.»
  2. **La hoja de importancia:** las 130 (las 100 primeras y las 30 de control), mezcladas con la semilla de la hoja,
     `B4-TRIPLETAS-T:cobertura_600:hoja:2026-10-27`, con `random.Random(semilla).sample(sorted(las 130), 130)`. Todas con las mismas
     columnas: el pasaje con su herencia y la tripleta con su tramo, y la importancia en la escala de 3.4. Sin el subgrafo, sin la
     posición, sin el puntaje y sin ninguna propuesta de un modelo. La autora la sella antes de abrir la hoja de presencia.
  3. **La hoja de presencia:** primero las 30 de D-9 y después las 100 primeras, en el orden de la hoja de importancia restringido a
     ellas. Un pasaje de los dos grupos va una sola vez, entre las 30, con todas sus columnas. Cada renglón trae el pasaje con su
     herencia, la tripleta con su tramo y el subgrafo en la forma compacta, con la presencia componente por componente. La revisión del
     5.8 (si la tripleta es correcta según el pasaje: sí, no o no decidible) va en las 30 de D-9, siempre, y en las 100 primeras solo
     cuando su presencia queda ausente; en las demás no va, y el sellador frena si trae un valor. Sin la importancia, sin la posición y
     sin ninguna propuesta de un modelo ni del juez.
  4. **El recall depurado (5.8):** saca del denominador solo las ausentes de las 100 primeras que la autora marca «no» según el pasaje.
     Las «no decidible» quedan y se cuentan.
  5. **Lo demás** de la nota anterior queda igual.
  - El texto firmado no cambia.

- **28/10/2026 — El juez de presencia con `claude-opus-5-5`, como el juez de precisión v2 y v3.** FIRMADA por la autora; el commit de
  la firma es el que agrega esta nota (decisión de la autora del 28/10/2026, recibida a las 07:58:57; registro de decisiones del
  15/10/2026, §153). Cambia los puntos 7 y 13 de la primera nota. Rige desde la firma, antes de que el juez juzgue nada y antes de la
  lectura de las 100.
  1. **La decisión, tal cual:** «El juez de presencia de la cobertura pasa a claude-opus-5-5, como el juez de precisión v2 y v3. Lo
     decido antes de que juzgue nada y antes de leer las 100.» Cuando se decidió, el juez no había corrido: no había ninguna corrida
     suya en `fuera_del_repo/tripletas_t_cob/corridas/`.
  2. **El modelo y sus parámetros,** los del juez de precisión v2 y v3 (enmienda 4, punto 2, y enmienda 5, punto 4, del pre-registro
     de tripletas):
     - `claude-opus-5-5`, sin `temperature`, porque la API no la acepta en ese modelo;
     - el razonamiento adaptativo, que en ese modelo no se apaga, con el esfuerzo `medium` puesto explícito;
     - `max_tokens` 16.000, que deja lugar al razonamiento sin pasar a streaming, como el juez v2
       (`fuera_del_repo/tripletas_v_juez/v2/codigo/juez_v2.py`, congelado en
       `data/experiment/tripletas_v/juez_v2/congelacion_juez_v2_sha256.txt`);
     - sin respaldo en otro modelo: un pedido que la API rechaza deja esa repetición sin voto, y se cuenta;
     - el veredicto sale solo de los bloques de texto de la respuesta. El razonamiento queda en la caché y no se lee;
     - una versión de código nueva, así la caché no mezcla un modelo con otro.

     Lo demás del punto 7 queda igual:
     - el prompt congelado por su sha256 antes de la corrida, con el bloque fijo del juez de V y los 20 calibradores de la hoja que
       selló la autora;
     - N = 3, con un cliente, una base y un espacio de nombres por repetición, y 0 cruces antes de agregar;
     - el control de lo nombrado, con su reintento y la adjudicación;
     - el veredicto modal y la regla del 5.6;
     - el piloto de las 10 primeras, ×3, con su proyección.
  3. **El costo y el tope, recalculados** (la mesa, `estimar_juez_presencia_T_opus_mesa.py` y su consola, en su paquete, §314):
     - **la cuenta:** la de la nota anterior, con los precios de `claude-opus-5-5` (4 / 20, escritura 5 y lectura 0,2 por millón) y
       2,26 caracteres por token, los medidos con ese modelo en el humo del juez v2;
     - **la salida, con el razonamiento:** 1.458 tokens en la mediana, la medida en ese mismo humo, y 4.000 en el alto. Los dos son del
       juez de precisión, NO VERIFICADOS para este juez: los mide su piloto, que proyecta con los tokens reales antes de seguir;
     - **una corrida sobre las 100, ×3:** de USD 16,55 (la mediana) a 36,60 (el alto);
     - **el tope:** USD 45, con freno en 38,25. Es el criterio de la nota anterior: el alto por 1,2, redondeado hacia arriba a 5, y el
       freno, el 85 %;
     - **lo ya gastado:** la extracción, USD 3,7044, y el puntaje, 2,8423 (sus registros del gasto). Con el alto del juez, T suma
       43,15, dentro de los USD 55 del §8. Los topes suman 97 (40, 12 y 45) y pasan en 42 esos 55: se declara como desvío del §8,
       como en la primera nota, con lo gastado al lado.
  4. **El desvío, declarado.** El juez cambia de modelo respecto del 5.6 del pre-registro de tripletas (`claude-sonnet-4-6` a
     temperatura 0) y del punto 7 de la primera nota. La decisión se tomó antes de que el juez juzgue nada y antes de la lectura de las
     100, así que no depende de ningún resultado del juez ni de esa lectura.
  5. **El límite:** la extracción abierta (5.3) también es `claude-opus-5-5`, así que el juez de presencia y el extractor del recall
     son el mismo modelo y pueden compartir sesgos sobre lo que una tripleta dice.
     - El acuerdo con la lectura de la autora sobre las 100 lo mide, con su umbral de la primera nota.
     - El juez no es el extractor del grafo medido: E1 es `claude-haiku-4-5` (5.3).
  6. **Cuándo:** el juez corre después de B6.3 (decisión de la autora del 28/10/2026, recibida a las 07:53:55). El cambio y su prueba
     van antes, a USD 0.
  - El texto firmado no cambia.
