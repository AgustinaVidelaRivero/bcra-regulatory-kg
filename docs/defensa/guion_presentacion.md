# Guion — Presentación Propuesta de PF (Defensa Oral)

**Agustina Videla Rivero · Knowledge Graph para la regulación del BCRA**
Tiempo objetivo: **10 minutos** · 11 slides · ~50-55 seg por slide
Fecha: 8 de junio de 2026

> **Narrativa (orden actual, por bloques):**
> Problema (2-3) → Propuesta: KG abstracto (4) → **Idea concreta: el ejemplo (5)** → Contexto:
> estado del arte (6) → Cómo lo hago (7-8) → **Lo logrado (9-10-11)**: factibilidad, experimento,
> grafos reales.
> *Clave del orden: la hipótesis abstracta (4) se aterriza enseguida con el ejemplo (5); así, cuando
> llega la metodología (7-8), el jurado ya entiende qué es el grafo.*

---

## Reglas que me dijo el profe (recordar antes de empezar)

- **Las primeras 3 slides me las sé de memoria, palabra por palabra.** El arranque es lo que da confianza.
- **NO leo las slides.** La slide es soporte; el centro soy yo. Miro al jurado y al público.
- **Justifico el PORQUÉ de cada decisión**, no solo el qué.
- **Vocabulario técnico**, nada de "tipo", "o sea", "más o menos". Llamo a las cosas por su nombre.
- **Admito limitaciones** con naturalidad. El jurado ya leyó el informe; ocultar resta.
- **Controlo el tiempo.** Si me estoy yendo, sintetizo y avanzo. No me clavo en una slide.
- Es una **venta de mi trabajo**: que se interesen y quieran leer el informe. No cuento TODO.

---

## SLIDE 1 — Portada (~20 seg) [DE MEMORIA]

> "Buenos días. Mi nombre es Agustina Videla Rivero y les voy a presentar mi propuesta de
> Proyecto Final: un **Knowledge Graph para la regulación del Banco Central de la República
> Argentina**. La idea central es modelar la normativa del BCRA de forma estructurada y
> trazable, y demostrar su utilidad sobre dos casos de uso aplicados. Mi mentor es Luciano
> Del Corro y mi comentor Juan Wisznia."

*(Respiro. Miro al jurado. Avanzo.)*

---

## SLIDE 2 — El problema (~50 seg) [DE MEMORIA]

**Mensaje clave: cumplir la regulación del BCRA es genuinamente difícil, y un asistente no alcanza con que sea correcto: tiene que ser auditable.**
**Versión directa, sin anécdota (el ejemplo concreto va en la slide 5, no lo adelanto acá). Ágil.**

> "Cumplir la regulación del BCRA es difícil porque el cuerpo normativo es **enorme, dinámico
> y densamente cruzado**. Lo que pasa es que el BCRA consolida toda la normativa vigente
> sobre un tema en un único documento que llama **Texto Ordenado** —uno de cambiario, uno
> de clasificación de deudores, uno de capitales mínimos— y además hay **miles de
> Comunicaciones** que los van modificando y citando entre sí continuamente. El resultado es
> que **una sola decisión operativa suele depender de varias normas a la vez**.
>
> Y acá está el punto que motiva todo el trabajo: un asistente sobre esta normativa **no solo
> tiene que ser correcto factualmente, tiene que ser auditable**. Uno tiene que poder rastrear
> de dónde sale cada afirmación, hasta la norma exacta."

*Nota: el ejemplo concreto (CEDEAR/dólares) NO va acá — aparece fresco en la slide 5. Así no
lo repito y la slide 2 queda ágil.*

---

## SLIDE 3 — La tensión (~50 seg) [DE MEMORIA]

**Mensaje clave: las herramientas de hoy no capturan la estructura referencial ni la trazabilidad. OJO: RAG no es inútil — es mi baseline; el punto es que tiene limitaciones ESTRUCTURALES acá.**

> "¿Por qué no alcanza con lo que hay hoy? Un **LLM solo** alucina y no me da trazabilidad:
> su conocimiento está diluido en los pesos, así que aunque acierte no puede decirme de qué
> norma lo sacó.
>
> **RAG denso** —el enfoque estándar— mejora bastante, porque condiciona la respuesta en
> texto real recuperado del corpus, no en la memoria del modelo. Pero hereda **dos
> limitaciones estructurales** en este corpus. Primero, parte la normativa en fragmentos, en
> *chunks*, y al fragmentar **se pierden las referencias cruzadas entre normas** —cada chunk
> queda aislado, sin saber qué otra norma lo modifica o lo excepciona. Segundo, recupera por
> **embeddings densos**, similitud semántica, que es frágil acá: dos normas pueden estar
> pegadas en el espacio de embeddings y tener **efectos jurídicos opuestos** —una permite,
> otra prohíbe; una es la regla, otra la excepción.
>
> Lo que hace falta es lo contrario: **relaciones explícitas entre normas, trazabilidad a la
> fuente, y poder razonar cadenas causales** que conectan varias normas. La pregunta que
> organiza la tesis es: **¿cómo modelo esa estructura de forma trazable?**"

---

## SLIDE 4 — La hipótesis (~45 seg)

**Mensaje clave: representar la regulación como Knowledge Graph. Decir el objetivo general explícito. Cierra anticipando el ejemplo concreto que viene enseguida.**

> "Mi hipótesis es que la respuesta es representar la regulación como un **Knowledge Graph**:
> una estructura de nodos y aristas, no un texto recuperado por similitud. Y elegí un KG por
> una razón concreta: **la estructura del problema ya es una red** —normas que se modifican,
> se referencian y tienen jerarquía—, así que el grafo calza con la forma real del dominio.
>
> Esto me da tres cosas, y no es casualidad que sean estas tres: **cada una es exactamente lo
> que al RAG le faltaba**. **Conocimiento estructurado** —relaciones, no solo texto— donde
> antes perdíamos las referencias; **trazabilidad nativa** —cada hecho a su fuente— donde el
> LLM no podía citar; y **razonamiento multi-hop** —encadenar varias normas— donde la
> similitud no seguía la cadena.
>
> Entonces el **objetivo general** del trabajo es: **diseñar, construir y evaluar un Knowledge
> Graph de la regulación del BCRA, con foco en la calidad del modelado y la trazabilidad, y
> aplicarlo a dos casos de uso** que demuestren su utilidad. Y para que no quede en abstracto,
> déjenme mostrarles enseguida qué significa esto en concreto."

---

## SLIDE 5 — La idea, en concreto (~55 seg)

**Mensaje clave: ATERRIZA la hipótesis abstracta que acabo de plantear, con un ejemplo real. Acá se entiende todo. Es también un anticipo del caso de uso 1 (explicabilidad). Mostrar la cadena + a quién le sirve + remate contra RAG.**

> "Acabo de decir 'modelar la regulación como un grafo'. Déjenme mostrarles en concreto qué
> significa eso, con un caso real: **por qué un cliente no puede comprar dólares después de
> operar en bolsa**.
>
> En el grafo, eso deja de ser un 'no' sin explicación y pasa a ser una **cadena causal que se
> lee paso a paso**: la **operación** —compra de títulos— **activa** una **restricción** —no poder
> acceder al MULC, el mercado oficial de cambios—; esa restricción **exige** una **obligación**
> —una declaración jurada—; y la restricción está **establecida por** una **Comunicación** del
> BCRA que **modifica** el **Texto Ordenado** de Exterior y Cambios.
>
> Esa cadena es la **respuesta al 'por qué'**, y le sirve a dos públicos: a la **persona**, que
> entiende por qué le bloquearon la operación, y al **banco**, que puede justificar esa decisión
> ante un regulador citando la norma. Y **cada nodo y cada arista guarda un puntero a su
> sección fuente**, así que la cadena entera es **auditable hasta el origen**. Esto es lo que un
> RAG sobre chunks no me puede dar —y es, de hecho, uno de los dos casos de uso que voy a
> desarrollar: el **sistema de explicabilidad**."

*"Agéntico" (si lo menciono o me preguntan) = no es una sola llamada al LLM; es un agente que
razona en pasos y usa el grafo como herramienta para recorrer la cadena.*

---

## SLIDE 6 — Estado del arte (~60 seg)

**Mensaje clave: hay antecedentes, pero tienen 4 vacíos concretos. Esos vacíos son mi contribución. Cada antecedente lo conecto con lo mío; los vacíos los digo con fuerza.**
**Peso invertido: antecedentes livianos (cada uno engancha con mi trabajo), vacíos = lo importante.**

> "El trabajo se apoya en literatura reciente, y conviene verla como una progresión. **RAG**
> (2020) es la base: responder preguntas condicionando la generación con texto recuperado —y
> es justamente el baseline que voy a comparar. **GraphRAG**, de Microsoft (2024), le suma la
> idea de grafo al RAG: es el framework de referencia, pero es genérico, no pensado para
> regulación ni para castellano. **RAGulating Compliance** (2025) es el más cercano a lo mío:
> lleva el KG con LLM a regulación —la FDA— de forma multi-agente y schema-light, y de ahí
> tomo la inspiración para mi esquema híbrido. Y **FinReflectKG** (2025) construye un KG
> financiero con razonamiento multi-hop, y mostró que el KG-RAG puede mejorar la respuesta y
> a la vez reducir el costo —eso motiva directamente mi comparación cabeza a cabeza.
>
> Pero al revisarlos encontré **cuatro vacíos** que mi trabajo aborda: primero, la **fidelidad no
> se mide** con métricas estándar como RAGAS o FActScore, aunque reducir alucinaciones es la
> motivación declarada. Segundo, las comparaciones usan **baselines débiles**, muchas veces
> auto-referenciales. Tercero, está casi **todo en inglés**: no hay evidencia en castellano. Y
> cuarto, **casi nunca se reporta el costo** computacional.
>
> Por eso el BCRA es el escenario ideal: es **público, densamente cross-referenciado, de alto
> impacto, y no existe un KG público que lo represente**."

*Si voy corta de tiempo: recorto las conexiones de los antecedentes (digo solo qué hace cada
uno) pero NUNCA recorto los 4 vacíos — son mi contribución.*

---

## SLIDE 7 — Metodología: cómo se construye (~60 seg)

**Mensaje clave: pipeline reproducible en 3 pasos. NO afirmar el híbrido como cerrado: el schema se está validando con los 5 experimentos. Eso ES la iteración sobre subsets, y es puente al experimento (slide 10).**

> "¿Cómo construyo el grafo? Tres etapas.
>
> **Uno, el corpus**: tomo la lista oficial de Textos Ordenados del BCRA y los descargo, junto
> con las Comunicaciones, con un scraper que respeta los límites del sitio y deja **manifiesto y
> logs** de todo lo que baja. Por eso es **reproducible**: cualquiera vuelve a correrlo y obtiene
> el mismo corpus. Y está pensado para correrse periódicamente —la idea es un job mensual—
> y así capturar las normas nuevas o modificadas, manteniendo el corpus al día.
>
> **Dos, la extracción**: extraigo las **tripletas con un LLM, Haiku**. Y acá hay una decisión que
> no quise tomar a ciegas: en vez de fijar el schema por intuición, **corrí cinco estrategias
> distintas** —de schema-light puro a schema fijo, incluyendo el híbrido que propuse en mi
> propuesta— y **cuál uso finalmente sale de compararlas, no de asumirlo**.
>
> **Tres, la trazabilidad**: cada nodo y cada arista guarda un **puntero explícito a su sección
> fuente** —el documento y el punto—, que es lo que vimos en el ejemplo de la cadena.
>
> Y todo esto descansa en una decisión de método —la de abajo—: **itero rápido sobre subsets
> acotados antes de escalar**, porque un cambio de modelado tiene **efectos enormes aguas
> abajo**, sobre los dos casos de uso. Si me equivoco en el schema con todo el corpus ya
> construido, rehago todo. Ese experimento de los cinco schemas —que les muestro más
> adelante— es, justamente, esta iteración."

---

## SLIDE 8 — Metodología: evaluación en dos planos (~60 seg)

**Mensaje clave: la evaluación del GRAFO es la contribución central; la funcional demuestra utilidad. Esto es lo que Luciano más remarcó.**

> "La evaluación tiene dos planos. El **plano A, la evaluación del grafo, es la contribución
> central** del trabajo. Tiene dos componentes: **calidad estructural** —densidad,
> conectividad, ratio de duplicación— y **calidad de extracción** a nivel de tripleta, medida
> con precision y recall contra un **gold standard** anotado manualmente.
>
> El **plano B es la evaluación funcional**, que mide la utilidad en la práctica sobre los casos
> de uso. En el caso 1, explicabilidad: si reconstruye bien la **cadena causal** —como la del
> ejemplo que vimos. Y en el caso 2, KG-RAG contra RAG tradicional: mido **faithfulness,
> citation accuracy y costo**.
>
> El **foco está en cómo modelo y evalúo el grafo**, no en los casos de uso. ¿Por qué? Porque
> **construir un KG con un LLM hoy es relativamente rápido**; lo difícil —y lo que la literatura
> no resolvió— es **modelarlo bien y demostrar con rigor que está bien hecho**. Ahí está la
> contribución: una metodología de evaluación de KGs sobre normativa, replicable a otros
> corpus. Los casos de uso demuestran que el grafo **sirve**, pero el aporte de investigación es
> la **construcción y la evaluación rigurosa del KG** —y por eso, si el tiempo aprieta, es lo que
> priorizo."

---

## SLIDE 9 — Factibilidad y resultados esperados (~50 seg)

**Mensaje clave: la factibilidad está DEMOSTRADA, no prometida. Cada ítem = un riesgo eliminado. El estrella: pipeline end-to-end + grafo sobre 5 TOs (la parte más incierta, ya probada). Anticipa el experimento (slide 10). NO repetir métricas.**

> "Sobre la **factibilidad**, el mensaje es uno: lo más riesgoso ya está validado, no es una
> promesa. Los **datos son públicos** —así que no hay riesgo legal ni de privacidad— y ya los
> tengo descargados. El **scraping está validado**. Y lo más importante: ya tengo un **primer
> pipeline de extracción corriendo end-to-end**, con un grafo trazable construido sobre cinco
> Textos Ordenados. O sea, la parte más incierta —que efectivamente *se pueda construir* el
> grafo— ya la probé; lo que queda es escalar y refinar, no inventar. En la próxima slide les
> muestro esa evidencia en concreto.
>
> Del otro lado, los **resultados esperados** son todos artefactos **verificables y publicables**: el
> KG trazable con su esquema documentado, el sistema de explicabilidad, y la comparación
> KG-RAG vs RAG. Y además dejo **recursos para la comunidad** —un gold standard de tripletas
> y un eval set curado en castellano— que hoy no existen."

---

## SLIDE 10 — Resultados preliminares: experimento de schema (~70 seg) [SLIDE CLAVE]

**Mensaje clave: corrí 5 estrategias de schema EN PARALELO para decidir el diseño empíricamente. El schema es la decisión MÁS crítica (efectos downstream) y no se puede saber a priori → por eso lo pruebo, no lo asumo. Los números NO muestran un ganador, muestran que el schema cambia el grafo radicalmente. Valida factibilidad, NO es el KG final. Decirlo explícito.**

> "Y esto es lo que ya validé empíricamente. La **decisión más crítica del proyecto es el diseño
> del schema** —cómo modelo el grafo—, porque un cambio de modelado tiene efectos enormes
> aguas abajo: si elijo mal y ya construí todo el corpus y los casos de uso encima, **rehago todo**.
> Y el problema es que **no hay forma de saber a priori cuál schema es el mejor**. Entonces, en
> vez de elegir por intuición, **corrí cinco estrategias distintas en paralelo sobre el mismo
> subset** —cookbook, papers del estado del arte, schema rígido, schema-light pura, e híbrida— y
> las comparo empíricamente. Como hoy un KG end-to-end se arma rápido, me puedo permitir
> probar cinco y decidir con datos.
>
> Cada una produjo un **Knowledge Graph completo, trazable, end-to-end**: extracción con
> Haiku, ensamblaje, y el grafo final en JSON. Los cinco grafos tienen entre **3.300 y 6.200
> nodos** y entre **3.400 y 6.600 relaciones**, con **100% de provenance**. El costo fue de entre
> **4 y 15 dólares por estrategia**, y ahí ya hay un hallazgo: la estrategia que evita resolución
> con LLM cuesta un tercio. Y ojo —estos números **no muestran un ganador**: muestran que el
> schema **cambia el grafo radicalmente**, casi el doble de nodos entre una estrategia y otra. Por
> eso justamente hay que evaluarlo en serio, no asumirlo.
>
> Quiero ser clara en una cosa: **este experimento valida que el pipeline funciona y me da
> datos para elegir el diseño final; no es el KG definitivo.** Lo que sigue es la **evaluación
> comparativa** —correr preguntas complejas contra los cinco grafos y medir cuál responde
> mejor—; eso elige el schema ganador, y con ese escalo al corpus completo."

---

## SLIDE 11 — Cómo se ve uno de los grafos + cierre (~50 seg)

**Mensaje clave: arrancar por el subgrafo (lo logrado, datos reales, conecta con el ejemplo de la slide 5); después el grafo completo (honestidad: núcleo + fragmentación). Esa estructura apareció en los 5 KGs → es lo que toca evaluar y mejorar tras elegir el schema. Cierre de toda la charla.**

> "Por último, así se ve uno de los grafos por dentro —el de la estrategia híbrida. Empiezo por
> la derecha: este es un **subgrafo**, un zoom a una parte del grafo, la cadena de un deudor
> moroso en el régimen cambiario. Y fíjense que es **la misma idea del ejemplo de la cadena que
> vimos al principio, pero ahora con datos reales extraídos**: cobertura de seguro, deudor
> moroso, gestión de cobro, encadenados y trazables. **Eso es lo que busco.**
>
> A la izquierda está el grafo completo, los miles de nodos juntos: un **núcleo bien conectado**,
> pero también **componentes aislados alrededor** —fragmentación. Y soy honesta con esto: esta
> estructura, núcleo más fragmentación, **apareció más o menos en los cinco grafos**. Es,
> justamente, lo que me toca **evaluar y mejorar** en las próximas iteraciones —una vez que la
> evaluación comparativa me diga con cuál de los cinco schemas me quedo. No la escondo, es el
> trabajo que sigue.
>
> En resumen: la propuesta es modelar la regulación del BCRA como un grafo trazable; **ya
> validé que es factible**; y lo que sigue es la evaluación rigurosa y los dos casos de uso.
> **Muchas gracias.**"

---

## Cierre / transición a preguntas

> "Quedo a disposición para las preguntas."

*(Postura tranquila. Si no sé algo, lo reconozco y digo cómo lo abordaría. Es una charla entre pares.)*
