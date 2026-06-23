# Banco de preguntas probables del jurado — y cómo responderlas

Ordenadas por probabilidad. Las primeras 8 son casi seguras. Practicá decirlas en voz alta.

---

## A. Sobre el modelado del KG (lo que más le importa a Luciano)

**0a. ¿Qué es un Knowledge Graph? (definilo en una frase)**
> Un KG modela entidades del mundo real como nodos y las relaciones entre ellas como aristas
> etiquetadas. La unidad básica es la tripleta Sujeto–Predicado–Objeto; por ejemplo
> "Comunicación A 7106 — modifica — Punto 3.16.3.4 del Texto Ordenado". En mi grafo las
> relaciones son del dominio: aplica_a, recae_sobre, excepciona_a, requiere, exime_a,
> autoriza, condiciona.

**0b. ¿Por qué se te ocurrió un KG? / ¿De dónde sacaste la idea?**
> Por dos lados. Conceptualmente, porque el problema ya tiene forma de grafo: las normas se
> modifican, se derogan, se referencian y tienen jerarquía —eso es una red de nodos y aristas,
> el KG calza con la estructura real del dominio. Y académicamente no es una idea aislada: hay
> una línea activa de LLM+KG —el roadmap de Pan et al., GraphRAG de Microsoft, y trabajos
> en regulación como RAGulating Compliance y FinReflectKG. Yo lo traigo a un corpus nuevo:
> el BCRA, en castellano.
> *(Origen del proceso, si lo piden: arranqué en scoring crediticio, vi que su núcleo es tabular
> —no de lenguaje—, pivoteé a explicabilidad normativa de decisiones automatizadas, y con mi
> mentor aterrizó en modelar la regulación misma como KG.)*

**0c. Los KGs existen hace años — ¿cuál es la novedad / por qué es una tesis?**
> La contribución no es inventar el concepto de KG, sino el modelado riguroso de un KG sobre
> un corpus regulatorio complejo, en castellano, con una metodología de evaluación seria.
> Construir un KG con LLMs hoy sale relativamente rápido; lo difícil y valioso es modelarlo
> bien y demostrar que está bien hecho. Justamente los cuatro vacíos que identifiqué —fidelidad
> sin medir, baselines débiles, todo en inglés, costo sin reportar— son los que nadie cubrió.
> Ahí está el aporte.

**0d. ¿Dónde se usan los KGs? / ¿Qué paradigma de LLM+KG usás?**
> Se usan en búsqueda (Google Knowledge Graph), Wikidata, sistemas de recomendación, KGs
> empresariales. En la era LLM, Pan et al. distinguen tres usos: KG para mejorar el LLM,
> LLM para construir el KG, y synergized. Mi trabajo usa los dos primeros: construyo el KG
> con un LLM (extracción con Haiku) y después lo uso para responder consultas (caso de uso 2).

**1. ¿Por qué un Knowledge Graph y no simplemente un RAG mejor / un RAG con re-ranking?**
> Porque el RAG denso fragmenta el corpus en chunks y al hacerlo disuelve las referencias
> cruzadas entre normas, que es justamente la estructura que importa acá. La recuperación por
> similitud además es frágil en regulación: normas cercanas en embedding space pueden tener
> efectos opuestos. El grafo modela esas relaciones de forma explícita y me habilita
> razonamiento multi-hop y trazabilidad nativa. De hecho mi caso 2 es exactamente esa
> comparación cabeza a cabeza, para medir empíricamente cuánto aporta.

**2. ¿Qué esquema de modelado vas a usar? ¿Schema-light o schema fijo?**
> Un híbrido: un núcleo cerrado de entidades core del dominio —Comunicación, Texto
> Ordenado, Operación, Restricción, Obligación, Excepción, Entidad Financiera— y el resto
> emergente, schema-light, inspirado en RAGulating Compliance. Y la razón de no decidirlo a
> dedo es que corrí cinco estrategias en paralelo para elegirlo con datos, no por intuición.

**3. ¿Cómo modelás una condición regulatoria? ¿Texto o valores estructurados?**
> *(Esta es una decisión real que discutí con mi mentor.)* Híbrido: dejo el texto de la
> condición como propiedad principal, y extraigo los valores numéricos —por ejemplo "atraso
> máximo 180 días", "5% de la responsabilidad patrimonial"— solo cuando el patrón es trivial
> de detectar. El trade-off es: si extraigo los valores, puedo responder consultas como "qué
> categorías permiten atrasos mayores a 90 días" directo desde el grafo; si los dejo como
> texto, eso lo tiene que resolver el LLM y pierde precisión. Pero extraerlos es un pipeline
> extra con posible error, así que voy gradual.

**4. ¿Por qué Haiku para la extracción y no un modelo más grande?**
> Es la decisión del protocolo experimental: quiero un modelo costo-eficiente para la
> extracción masiva, que es donde está el volumen de llamadas. La calidad la controlo con el
> schema y con la evaluación contra gold standard. Donde hace falta más capacidad —por
> ejemplo resolución de entidades— evalúo usar un modelo más grande, y de hecho una de mis
> cinco estrategias usó Sonnet para esa etapa.

**5. ¿Cómo resolvés que la misma entidad aparezca nombrada de formas distintas (coreference / canonicalización)?**
> Con un módulo de canonicalización de entidades y coreference resolution type-aware, que es
> una técnica que tomo de los papers LINK-KG y CORE-KG. Algunas de mis estrategias lo
> hacen de forma determinística —normalización de slug más heurísticas— y otra con un LLM.
> Comparar ambas es parte del experimento.

---

## B. Sobre la evaluación (la parte "científica")

**6. ¿Cómo vas a evaluar que el grafo está "bien"? Esto es lo más difícil.**
> En dos planos. El principal es sobre el grafo: calidad estructural —densidad, conectividad,
> ratio de duplicación— y calidad de extracción a nivel de tripleta, con precision y recall
> contra un **gold standard anotado manualmente** sobre una muestra representativa. El
> segundo plano es funcional, sobre los casos de uso. Reconozco que construir el gold standard
> con criterios de muestreo explícitos es una de las actividades centrales y más costosas del
> proyecto, no un detalle.

**7. ¿Cómo construís el gold standard y de qué tamaño?**
> Por anotación manual sobre una muestra representativa del corpus; el tamaño final y los
> criterios de muestreo los dimensiono en la fase inicial y los reporto junto con los resultados.
> Es deliberadamente un objetivo de diseño explícito, porque la validez de toda la evaluación
> de extracción depende de eso.

**8. En el caso 2, ¿qué baseline de RAG usás? ¿No es auto-comparativo?**
> Justamente uno de los vacíos que identifiqué es que las comparaciones publicadas usan
> baselines débiles o auto-referenciales. Por eso uso un RAG tradicional fuerte e
> independiente sobre el mismo corpus, con métricas estándar —faithfulness, answer
> correctness, citation accuracy— complementadas con RAGAS y FActScore, y reporto costo y
> latencia, que casi nadie reporta.

**9. ¿Cómo medís "faithfulness" y "citation accuracy" concretamente?**
> Faithfulness con RAGAS y FActScore, que descomponen la respuesta en afirmaciones
> atómicas y verifican cuántas están soportadas por la evidencia recuperada. Citation accuracy
> con una métrica propia: qué proporción de las citas que da el sistema apuntan efectivamente
> a la norma correcta. La trazabilidad nativa del grafo es lo que hace esto verificable.

---

## C. Sobre datos, alcance y factibilidad

**10. El corpus es enorme (158 Textos Ordenados, miles de Comunicaciones). ¿Vas a procesar todo?**
> No de entrada. Trabajo con un subset acotado y representativo —hoy cinco Textos
> Ordenados, 564 páginas, que cubren los dominios más densos: cambiario, deudores, capitales
> mínimos— para iterar el modelado rápido. Una vez fijado el schema, escalo. La prioridad
> metodológica es el modelado y la evaluación, no la cobertura total del corpus.

**11. ¿Cómo manejás que la normativa cambia en el tiempo (las Comunicaciones modifican los TOs)?**
> La versión es un atributo del nodo: puedo tener un nodo en versión 5 y otro en versión 4, y
> modelar la cadena de modificaciones. Las Comunicaciones A las uso como metadato que
> documenta cómo cambió la norma; el contenido del KG sale del Texto Ordenado vigente.
> Para el mantenimiento, la idea a futuro es un job periódico —pensado mensual— que
> re-corre el scraper y captura las normas nuevas o modificadas (el "diff").
> *(Honestidad del estado actual, si repreguntan: el scraper ya es idempotente —si lo re-corro
> saltea lo descargado y no re-paga lo hecho—, así que está listo para schedularse; el job
> periódico en sí y la detección automática de diff son el siguiente paso, todavía no están
> corriendo. La actualización del grafo en el tiempo la planteo como trabajo futuro, en línea con
> lo que conversé con mis mentores.)*

**12. ¿Por qué el BCRA y no una regulación en inglés con datos más limpios?**
> Porque ahí está la contribución. La literatura está casi toda en inglés; no hay evidencia
> empírica sobre regulación financiera en castellano ni un KG público del BCRA. Trabajar
> sobre datos en castellano técnico-financiero, con su estructura referencial característica,
> aporta un caso de estudio latinoamericano que hoy falta. Y los Textos Ordenados del BCRA
> están sorprendentemente bien estructurados, lo que los hace un buen punto de partida.

**13. ¿El cronograma es realista? Son dos casos de uso en seis meses.**
> Es el principal vector de riesgo y lo declaro explícitamente. Mi plan de mitigación es una
> priorización clara: el modelado, construcción y evaluación rigurosa del KG, más el gold
> standard, son la contribución central y se completan sí o sí. Los dos casos de uso van en
> orden secuencial, y si hay que ajustar, priorizo el de explicabilidad sobre la comparación
> KG-RAG.

---

## D. Técnicas / herramientas

**14. ¿Dónde vas a almacenar y consultar el grafo cuando crezca?**
> Hoy estoy con RDFLib en memoria, que sirve para experimentar pero no escala. Para el grafo
> real evalúo un servidor SPARQL; los candidatos son Apache Jena Fuseki —estándar
> académico, open source—, GraphDB —mejor UI de visualización— y Neo4j con el plugin
> n10s, más popular en industria pero no RDF nativo. La decisión la cierro al escalar; para la
> fase de modelado no es bloqueante.

**15. ¿Por qué corriste cinco schemas en paralelo? ¿No es desperdicio?**
> Al contrario, es la forma de tomar la decisión más crítica del proyecto con evidencia y no por
> intuición. Como hoy puedo tener un KG end-to-end en una hora, corrí cinco estrategias
> distintas sobre el mismo subset y mido cuál funciona mejor downstream. Cuesta entre 4 y 15
> dólares cada una; es barato comparado con elegir mal el schema y rehacer todo el corpus.

**16. ¿Cuál de los cinco schemas ganó?**
> Todavía no lo decidí: ese es justamente el siguiente paso, la evaluación comparativa. El
> experimento ya me validó que el pipeline funciona y me dio las métricas estructurales de cada
> uno; ahora corro las consultas de evaluación para elegir el que mejor responde.

---

## E. Si admito una limitación (con naturalidad, sin esconder)

- **El gold standard es trabajo manual costoso** → lo reconozco como actividad central, no marginal.
- **El cronograma es ajustado** → tengo priorización explícita de mitigación.
- **El experimento de schemas no es el KG final** → lo digo yo antes de que me lo pregunten.
- **El costo varía bastante (4 a 15 USD)** → es un hallazgo: el costo depende del diseño.

---

## Frases de seguridad si me trabo o no sé algo

- "Esa es una buena pregunta; mi intuición es X, pero es justamente algo que voy a resolver empíricamente en la fase de Y."
- "No lo tengo cerrado todavía; lo tengo identificado como una decisión de diseño de la fase inicial."
- "Lo abordaría de la siguiente manera..." *(y doy el camino, aunque no el resultado)*.
