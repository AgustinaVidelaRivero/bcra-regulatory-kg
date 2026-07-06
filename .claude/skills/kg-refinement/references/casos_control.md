# Casos-control para la calibración del Paso 3 (sub-fase A)

Referencia del **Paso 3, sub-fase A**. Antes de analizar todo el dataset, el agente corre su análisis sobre estas 5 preguntas, cuya atribución humana ya está documentada, y se compara su salida con la humana. **Si no coincide en el umbral, la skill se detiene para revisión y no escala.** La razón: nunca se confía en atribución no validada, y menos en corridas futuras que nadie supervisa de cerca.

**Las 5 preguntas-control:** CQ-031, CQ-034, CQ-017, CQ-020, CQ-025. Son las 5 fallas de `run_3` sobre `eval_set_v1`, ya diagnosticadas a mano por la autora.

---

## Cómo se usa este archivo

1. El agente investiga cada caso-control con el **mismo flujo evidencia→conclusión** del Paso 3 sub-fase B, **sin mirar la columna de atribución humana de abajo** (eso sería hacer trampa en la propia calibración).
2. Se compara la atribución del agente con la **atribución humana** registrada acá.
3. **Umbral de calibración:** sugerido **≥4 de 5** coincidencias. **El umbral exacto lo decide la autora**; es un parámetro afinable, no un valor congelado.
4. **Casos con [atribución múltiple](taxonomia.md):** la regla depende de cuántas causas sean **primarias** (las que mueven el veredicto). Hay tres patrones, y los casos-control los ejercen:
   - **Primaria + secundaria(s) — p. ej. CQ-020:** acierto si el agente detecta la **causa primaria**. Detectar la(s) secundaria(s) suma pero **no es obligatorio**. El porqué: la primaria es la que mueve el veredicto y la que un refinamiento del grafo podría arreglar, así que el verificador no se la puede perder; las secundarias son refinamiento de estilo, menos críticas para un pipeline cuyo objetivo es refinar el grafo.
   - **Varias primarias — p. ej. CQ-017:** acierto **solo si detecta TODAS las primarias**. Detectar una sola **no** es acierto, porque se perdió la mitad de la falla. El porqué: cuando la pregunta tiene patas independientes y cada defecto rompe una pata distinta, ninguna causa es prescindible — quedarse con una deja la otra pata sin diagnosticar y sin arreglar.
   - **Primaria de sistema + pata de ruido del juez — p. ej. CQ-025:** acierto si el agente detecta la **pata primaria de sistema** (en CQ-025, la `contenido_kg` de grafo). Reconocer la otra pata como **falso positivo del juez** suma pero **no es obligatorio**. La diferencia con CQ-017: acá **solo una pata es defecto del sistema**; la otra no es defecto de nada (es ruido de medición del juez), así que no se exige detectarla para acertar. Ojo: detectar la pata de sistema como defecto de **agente** (navegación) no es acierto — el dato correcto no existe en el grafo, así que el defecto es de grafo, no de navegación.
   - En cualquier caso, confundir primaria con secundaria —o viceversa— no es acierto: la jerarquía importa.

---

## La tabla de atribución humana

> **Nota de procedencia (importante, leer).** Las preguntas y sus `ground_truth_secciones`/`cita_textual` salen verbatim de `data/experiment/evaluacion/queries/eval_set_v2.json` (parseo real). La columna **palanca/riesgo esperados** sale de los ejemplos del Paso 4 del diseño de la skill. La columna **atribución humana (ground-truth de calibración)** está **confirmada por la autora contra su diagnóstico firmado** (las 5 fallas diagnosticadas a mano sobre v1; CQ-034 verificado además contra el PDF). Las fallas pueden tener [atribución múltiple](taxonomia.md), y los casos-control ejercen los tres patrones: **primaria + secundaria** (CQ-020), **varias primarias** (CQ-017) y **primaria de sistema + falso positivo del juez** (CQ-025).

### CQ-031 — `cadena_restriccion_excepcion` · TO: clasificacion
- **Pregunta:** ¿Qué deudores no deben ser objeto de clasificación y respecto de qué deudores no corresponde evaluar la capacidad de repago?
- **Ground-truth secciones:** Punto 4.5 (deudores que no deben clasificarse) · Punto 4.4 (financiaciones con garantías preferidas 'A').
- **Atribución humana (confirmada):** defecto del grafo → **completitud_kg** (nodo stub / enumeración del PDF no poblada).
- **Palanca/riesgo esperados (Paso 4):** grafo/esquema · **bajo riesgo** — poblar el nodo stub con la enumeración del PDF (transcripción verificable contra pasaje único).

### CQ-034 — `cadena_restriccion_excepcion` · TO: exterior
- **Pregunta:** Compra de moneda extranjera para atesorar: ¿qué límite mensual aplica con débito en cuenta vs. en efectivo, y qué límite general rige para otras modalidades de formación de activos externos?
- **Ground-truth secciones:** Punto 3.8 (billetes/depósitos, conceptos A07 y A09) · Punto 3.9 (otras modalidades, ayuda familiar, derivados).
- **Atribución humana (confirmada — verificada contra el PDF):** defecto del grafo → **completitud_kg** (límite faltante en la extracción). Los límites son literales en el PDF: USD 100 con efectivo (3.8) y USD 200 para otras modalidades (3.9) del TO de Exterior.
- **Palanca/riesgo esperados (Paso 4):** grafo/esquema · **bajo riesgo** — completar el límite contra el pasaje del PDF (transcripción de un dato literal único en 3.8/3.9; falla secundaria del diagnóstico de run_3).

### CQ-017 — `multi_norma` · TOs: proteccion, exterior
- **Pregunta:** Un operador de cambio, ¿está alcanzado por las normas de Protección de Usuarios y debe intervenir como entidad autorizada en el mercado de cambios?
- **Ground-truth secciones:** Protección, Punto 1.1.2.2 · Exterior y Cambios, Punto 1.1.
- **Atribución humana (confirmada — MIXTA con DOS causas, ambas PRIMARIAS):** es un caso de [atribución múltiple](taxonomia.md) con **dos defectos de grafo**, cada uno rompiendo una pata distinta de la pregunta. Como cada defecto mueve el veredicto de su pata, **ninguna es secundaria** (a diferencia de CQ-020).
  - **Causa primaria — `estructural_kg`:** falta la arista cross-documento que une Protección (Punto **1.1.2.2**, operador de cambio alcanzado) con Exterior y Cambios (Punto **1.1**, entidad autorizada en el mercado de cambios). Sin esa conexión, la **pata 2** de la pregunta queda sin responder.
  - **Causa primaria — `provenance_imprecisa`:** el nodo del operador de cambio tiene provenance a nivel grueso (**"Punto 1.1"**) en vez del específico (**"1.1.2.2"**). El agente reportó fielmente lo que el nodo decía (citó 1.1), y por eso el juez marcó la **pata 1** como incorrecta pese a que el contenido era correcto.
  - Cada causa va con sus tres piezas de evidencia (afirmación / nodo / fuente).
- **Calibración (difiere de CQ-020):** como las dos causas son primarias, el verificador **acierta solo si detecta ambas** (`estructural_kg` Y `provenance_imprecisa`). Detectar una sola **no** es acierto — se perdió la mitad de la falla. (En CQ-020 alcanza con la primaria porque la otra es secundaria de estilo.)
- **Palanca/riesgo esperados (Paso 4):** ambas → grafo/esquema · ambas **alto riesgo** — crear la arista cross-documento es estructura nueva, y corregir la provenance a nivel fino es decisión de modelado; las dos → revisión humana.

### CQ-020 — `multi_norma` · TOs: capitales, regimen
- **Pregunta:** ¿Cómo se calcula la exigencia de capital por riesgo de crédito (CRC) y con qué frecuencia se reporta al BCRA?
- **Ground-truth secciones:** Capitales, Punto 2.1 · Régimen Informativo, Punto 3.1.2 · Régimen Informativo, Punto 1.1 (frecuencia).
- **Atribución humana (confirmada — MIXTA, primaria + secundaria):** es un caso de [atribución múltiple](taxonomia.md).
  - **Causa primaria — `completitud_kg` (defecto del grafo):** falta el nodo de **frecuencia de reporte para riesgo de crédito**; por su ausencia el agente **mis-aplica el nodo de frecuencia de riesgo de mercado**. Es lo que mueve el veredicto, y lo que un refinamiento del grafo podría arreglar.
  - **Causa secundaria — `generación-de-más` (defecto del agente):** glosas sobre las variables de la fórmula CRC (k, APRc, INC) **sin soporte de ningún nodo** consultado — agregadas de su cosecha.
  - Cada causa va con sus tres piezas de evidencia (afirmación / nodo / fuente).
- **Palanca/riesgo esperados (Paso 4):** la primaria → grafo/esquema (crear el nodo de frecuencia faltante); la secundaria → prompt del agente RAG. Ambas de **alto riesgo** → revisión humana.
- **Por qué la primaria es ALTO riesgo (confirmado):** el nodo de frecuencia para riesgo de crédito **no existe — hay que crearlo de cero**, y crear estructura nueva es decisión de modelado, no transcripción de un dato literal único. Por eso difiere de CQ-034, que es bajo riesgo (ahí el dato está literal en el PDF y solo se completa).

### CQ-025 — `multi_norma` (frecuencia de reporte) · TO: regimen
- **Pregunta:** ¿Con qué frecuencia se informa la exigencia por riesgo de mercado y el ratio de apalancamiento?
- **Atribución humana (confirmada — verificada contra el PDF real — MIXTA: una pata de sistema PRIMARIA + una pata que es falso positivo del juez):** caso de [atribución múltiple](taxonomia.md), estructuralmente como CQ-017 (dos patas independientes), pero con causas de **distinto tipo**.
  - **Pata 1 (riesgo de mercado) — `contenido_kg`, PRIMARIA (defecto de grafo):** el PDF (Punto 1.1 del TO de Régimen Informativo) ubica los datos de riesgo de mercado (puntos 4.3-4.5) en la lista de excepciones **trimestrales**. Pero el nodo `Operacion_calculo_de_riesgo_de_mercado` del grafo dice "mensual". El extractor confundió: en el pasaje, "mensual" califica al **código de consolidación** ("consolidado mensual"), no a la frecuencia de reporte, que es **trimestral** según el encabezado del bloque. El nodo afirma un contenido que contradice el PDF → `contenido_kg`.
  - **Pata 2 (ratio de apalancamiento) — falso positivo del juez (NO defecto de grafo ni de agente):** el agente respondió correctamente que el apalancamiento es **trimestral** y citó bien el Punto 10.1 (verificado contra el PDF: el Punto 10.1.1 contiene "los datos se informarán con frecuencia trimestral"). El juez marcó esa afirmación como falsa, pero era correcta → ruido del juez, no un defecto del sistema.
- **Calibración (regla específica):** como la pata 1 es la causa primaria de **sistema** (defecto de grafo), el verificador **acierta si detecta la pata 1 como `contenido_kg` (defecto de grafo)**. Reconocer la pata 2 como **falso positivo del juez** suma pero es **secundario**. Detectar la pata 1 como "navegación" (defecto de agente) **NO** es acierto: el dato correcto (trimestral) **no existe en el grafo**, así que no es que el agente no lo encontró — es que el grafo lo tiene mal.
- **Palanca/riesgo esperados (Paso 4):** pata 1 → grafo/esquema (corregir el contenido del nodo: mensual→trimestral, contra el pasaje del PDF); pata 2 → ninguna acción sobre el sistema (ruido del juez, se reporta como falso positivo).

---

## Por qué estos 5 y no otros

Son las fallas reales de `run_3` ya diagnosticadas a mano: cubren los defectos de grafo de bajo riesgo (completitud: CQ-031, CQ-034), un caso de alto riesgo con **dos causas primarias de grafo** (estructural + provenance: CQ-017), un caso **mixto primaria-grafo + secundaria-agente** (CQ-020) y un caso **mixto `contenido_kg` (grafo) + falso positivo del juez** (CQ-025). Calibrar contra ellos prueba que el agente distingue las situaciones que el Paso 4 va a enrutar distinto, y que maneja los tres patrones de atribución múltiple. Si el agente no reproduce estas atribuciones conocidas, no hay razón para confiar en las que haga a escala sobre fallas sin diagnóstico previo.
