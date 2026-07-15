# Expediente de re-adjudicación de la vara — material compilado (SOLO LECTURA)

Fecha de compilación: 2026-07-15. HEAD del repo: `c0b96a4`. Propósito: compilar el material
para re-expresar los GTs de los 5 casos-control (run_3) en la taxonomía v2.6.1. La adjudicación
se hace fuera de esta sesión. **Este archivo no contiene análisis ni propuestas de
re-adjudicación: solo material copiado verbatim + chequeo estructural.** Única escritura de la
tarea: este archivo.

---

# SECCIÓN 1 — VARA ACTUAL, VERBATIM

Output de `git log --oneline -1 -- .claude/skills/kg-refinement/references/casos_control.md`:

```
5bb58c0 casos_control: GTs re-expresados en taxonomía v2 (pares síntoma+causa) + 2 re-adjudicaciones de la autora: CQ-031 → {context_recall, alcanzabilidad_kg} única primaria (pata 4.4 no integra la falla); CQ-020 secundaria recompuesta (claim 0,08 modo b; fórmula 70100000 = falso positivo del juez, nodo consultado en traza). Cobertura de lados documentada
```

Confirmado: el último commit que toca la vara es `5bb58c0`, como esperaba el protocolo.

Contenido completo de `.claude/skills/kg-refinement/references/casos_control.md` tal como está
en HEAD (copiado sin resumir ni reordenar; los encabezados originales `#`/`##`/`###` se
preservan dentro del bloque de cita para no mezclarlos con la estructura de este expediente):

````markdown
# Casos-control para la calibración del Paso 3 (sub-fase A)

Referencia del **Paso 3, sub-fase A**. Antes de analizar todo el dataset, el agente corre su análisis sobre estas 5 preguntas, cuya atribución humana ya está documentada, y se compara su salida con la humana. **Si no coincide en el umbral, la skill se detiene para revisión y no escala.** La razón: nunca se confía en atribución no validada, y menos en corridas futuras que nadie supervisa de cerca.

**Las 5 preguntas-control:** CQ-031, CQ-034, CQ-017, CQ-020, CQ-025. Son las 5 fallas de `run_3` sobre `eval_set_v1`, ya diagnosticadas a mano por la autora.

---

## Cómo se usa este archivo

1. El agente investiga cada caso-control con el **mismo flujo evidencia→conclusión** del Paso 3 sub-fase B, **sin mirar la columna de atribución humana de abajo** (eso sería hacer trampa en la propia calibración).
2. Se compara la atribución del agente con la **atribución humana** registrada acá.
3. **Umbral de calibración:** sugerido **≥4 de 5** coincidencias. **El umbral exacto lo decide la autora**; es un parámetro afinable, no un valor congelado.
4. **Casos con [atribución múltiple](taxonomia.md):** la regla depende de cuántas causas sean **primarias** (las que mueven el veredicto). Hay tres patrones, y los casos-control los ejercen:
   - **Primaria + secundaria(s) — p. ej. CQ-020:** acierto si el agente detecta la **causa primaria**. Detectar la(s) secundaria(s) suma pero **no es obligatorio**. El porqué: la primaria es la que mueve el veredicto y la que un refinamiento del grafo podría arreglar, así que el verificador no se la puede perder; las secundarias son menos críticas para un pipeline cuyo objetivo es refinar el grafo.
   - **Varias primarias — p. ej. CQ-017:** acierto **solo si detecta TODAS las primarias**. Detectar una sola **no** es acierto, porque se perdió la mitad de la falla. El porqué: cuando la pregunta tiene patas independientes y cada defecto rompe una pata distinta, ninguna causa es prescindible — quedarse con una deja la otra pata sin diagnosticar y sin arreglar.
   - **Primaria de sistema + pata de ruido del juez — p. ej. CQ-025:** acierto si el agente detecta la **pata primaria de sistema** (en CQ-025, la `contenido_kg` de grafo). Reconocer la otra pata como **falso positivo del juez** suma pero **no es obligatorio**. La diferencia con CQ-017: acá **solo una pata es defecto del sistema**; la otra no es defecto de nada (es ruido de medición del juez), así que no se exige detectarla para acertar. Ojo: detectar la pata de sistema como defecto de **agente** (navegación) no es acierto — el dato correcto no existe en el grafo, así que el defecto es de grafo, no de navegación.
   - En cualquier caso, confundir primaria con secundaria —o viceversa— no es acierto: la jerarquía importa.

---

## La tabla de atribución humana

> **Nota de procedencia (importante, leer).** Las preguntas y sus `ground_truth_secciones`/`cita_textual` salen verbatim de `data/experiment/evaluacion/queries/eval_set_v2.json` (parseo real). La columna **palanca/riesgo esperados** sale de los ejemplos del Paso 4 del diseño de la skill. La columna **atribución humana (ground-truth de calibración)** está **confirmada por la autora contra su diagnóstico firmado** (las 5 fallas diagnosticadas a mano sobre `eval_set_v1`; CQ-034 verificado además contra el PDF), con **dos re-adjudicaciones de la autora del 2026-07-10** que reemplazan al diagnóstico firmado donde difieren: CQ-031 (primaria) y la composición de la secundaria de CQ-020 — ver la nota de re-adjudicación en cada caso. **Vocabulario:** desde el 2026-07-10 los GTs están re-expresados en la **taxonomía v2** — pares `{sintoma_capa1, causa_capa2}`, ver `taxonomia.md` —; el diagnóstico firmado original usaba el vocabulario v1 y la correspondencia está en `mapeo_taxonomia_v1_v2.md`. La re-expresión conserva causa, jerarquía, patas y evidencia; solo agrega el síntoma de capa 1. Las fallas pueden tener [atribución múltiple](taxonomia.md), y los casos-control ejercen los tres patrones: **primaria + secundaria** (CQ-020), **varias primarias** (CQ-017) y **primaria de sistema + falso positivo del juez** (CQ-025).

### CQ-031 — `cadena_restriccion_excepcion` · TO: clasificacion
- **Pregunta:** ¿Qué deudores no deben ser objeto de clasificación y respecto de qué deudores no corresponde evaluar la capacidad de repago?
- **Ground-truth secciones:** Punto 4.5 (deudores que no deben clasificarse) · Punto 4.4 (financiaciones con garantías preferidas 'A').
- **Atribución humana (re-adjudicada por la autora, 2026-07-10):** defecto del grafo → **`{context_recall, alcanzabilidad_kg}`**, ÚNICA primaria, pata 4.5. Evidencia: el nodo poblado `Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti` existe con el 4.5 verbatim en `properties.descripcion` ("Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas A no serán objeto de clasificación"), pero `buscar_nodos` indexa solo label/id; las búsquedas del agente en la traza (pasos 7, 9 y 11) no lo alcanzaron y la pata se respondió con la cesión del 4.6. Señal de `context_recall` en los propios datos del juez: `cobertura_patas` marca la pata "qué deudores no deben ser objeto de clasificación" como `no_cubierta`.
- **La pata 4.4 NO integra la falla** (sin entrada propia): sus 3 claims fueron marcados `verdadero` por el juez — el agente la respondió bien con el nodo del 4.4 (`ver_nodo` en el paso 4 de la traza).
- **Nota de re-adjudicación (autora, 2026-07-10):** reemplaza el `completitud_kg` del diagnóstico firmado. Motivada por la auditoría GT (`posthoc_run/auditoria_gt/CQ-031.md`, barrido programático sobre todos los campos de los 4.050 nodos) y por la taxonomía v2 (que distingue "falta" de "está pero no se llega"); decisión de la autora. Erratum de la auditoría: dice "paso 5", pero en la traza el nodo del 4.4 aparece en el paso 2 y se abre con `ver_nodo` en el paso 4.
- **Palanca/riesgo esperados (Paso 4):** grafo/esquema · **ALTO riesgo** — exponer léxicamente el contenido (renombrar label/id del nodo portador o indexar descriptions), decisión de modelado.

### CQ-034 — `cadena_restriccion_excepcion` · TO: exterior
- **Pregunta:** Compra de moneda extranjera para atesorar: ¿qué límite mensual aplica con débito en cuenta vs. en efectivo, y qué límite general rige para otras modalidades de formación de activos externos?
- **Ground-truth secciones:** Punto 3.8 (billetes/depósitos, conceptos A07 y A09) · Punto 3.9 (otras modalidades, ayuda familiar, derivados).
- **Atribución humana (confirmada — verificada contra el PDF):** defecto del grafo → **`{context_recall, completitud_kg}`**, primaria (límite faltante en la extracción — el dato pertinente nunca apareció en la trayectoria). Los límites son literales en el PDF: USD 100 con efectivo (3.8) y USD 200 para otras modalidades (3.9) del TO de Exterior.
- **Palanca/riesgo esperados (Paso 4):** grafo/esquema · **bajo riesgo** — completar el límite contra el pasaje del PDF (transcripción de un dato literal único en 3.8/3.9; falla secundaria del diagnóstico de run_3).

### CQ-017 — `multi_norma` · TOs: proteccion, exterior
- **Pregunta:** Un operador de cambio, ¿está alcanzado por las normas de Protección de Usuarios y debe intervenir como entidad autorizada en el mercado de cambios?
- **Ground-truth secciones:** Protección, Punto 1.1.2.2 · Exterior y Cambios, Punto 1.1.
- **Atribución humana (confirmada — MIXTA con DOS causas, ambas PRIMARIAS):** es un caso de [atribución múltiple](taxonomia.md) con **dos defectos de grafo**, cada uno rompiendo una pata distinta de la pregunta. Como cada defecto mueve el veredicto de su pata, **ninguna es secundaria** (a diferencia de CQ-020).
  - **Causa primaria — `{context_recall, estructural_kg}` (pata 2):** falta la arista cross-documento que une Protección (Punto **1.1.2.2**, operador de cambio alcanzado) con Exterior y Cambios (Punto **1.1**, entidad autorizada en el mercado de cambios). Sin esa conexión, la **pata 2** de la pregunta queda sin responder (el contexto que la conecta nunca apareció en la trayectoria).
  - **Causa primaria — `{noise_sensitivity, provenance_imprecisa}` (pata 1):** el nodo del operador de cambio tiene provenance a nivel grueso (**"Punto 1.1"**) en vez del específico (**"1.1.2.2"**). El agente reportó fielmente lo que el nodo decía (citó 1.1) — claim soportado por el nodo pero incorrecto contra el GT —, y por eso el juez marcó la **pata 1** como incorrecta pese a que el contenido era correcto.
  - Cada causa va con sus tres piezas de evidencia (afirmación / nodo / fuente).
- **Calibración (difiere de CQ-020):** como las dos causas son primarias, el verificador **acierta solo si detecta ambas** (`estructural_kg` Y `provenance_imprecisa`). Detectar una sola **no** es acierto — se perdió la mitad de la falla. (En CQ-020 alcanza con la primaria porque la otra es secundaria.)
- **Palanca/riesgo esperados (Paso 4):** ambas → grafo/esquema · ambas **alto riesgo** — crear la arista cross-documento es estructura nueva, y corregir la provenance a nivel fino es decisión de modelado; las dos → revisión humana.

### CQ-020 — `multi_norma` · TOs: capitales, regimen
- **Pregunta:** ¿Cómo se calcula la exigencia de capital por riesgo de crédito (CRC) y con qué frecuencia se reporta al BCRA?
- **Ground-truth secciones:** Capitales, Punto 2.1 · Régimen Informativo, Punto 3.1.2 · Régimen Informativo, Punto 1.1 (frecuencia).
- **Atribución humana (confirmada — MIXTA, primaria + secundaria):** es un caso de [atribución múltiple](taxonomia.md).
  - **Causa primaria — `{context_recall, completitud_kg}` (defecto del grafo):** falta el nodo de **frecuencia de reporte para riesgo de crédito**; por su ausencia el agente **mis-aplica el nodo de frecuencia de riesgo de mercado**. Por la [regla de precedencia](taxonomia.md) el síntoma es `context_recall`: el nodo de riesgo de mercado NO cuenta como contexto de la pata de crédito (es un nodo de otro tema usado para rellenar), así que el dato pertinente nunca apareció en la trayectoria. Es lo que mueve el veredicto, y lo que un refinamiento del grafo podría arreglar.
  - **Causa secundaria — `{faithfulness, alucinacion_agente}` (defecto del agente; v1: generación-de-más — correcto en sustancia; lo que se corrige es QUÉ claims la componen):** la compone el claim **"0,08 es el coeficiente de capital mínimo"**, modo (b) del árbol (glosa de cosecha propia): ningún nodo del grafo ni pasaje del PDF lo nombra así (barridos de `70100000`/`0,08`/`APRc` sobre todos los campos + verificación contra 2.1 y 8.5.3 del corpus) — la evidencia es la constancia de búsqueda + la verificación negativa contra el PDF, sin nodo que exhibir. El otro claim `no_soportado` del juez —la fórmula alternativa "Código 70100000 (n) = …"— es **falso positivo del juez** (sin par v2 — no es defecto del sistema): está soportado por un nodo que el agente SÍ consultó (`Operacion_calculo_de_exigencia_por_riesgo`, `ver_nodo` en el paso 6 de su trayectoria) y es correcto contra el PDF (8.1.1); el juez es ciego al grafo y no podía verlo. **NO componen la secundaria** las glosas sobre k, APR_c e INC: el juez marcó esos claims `verdadero`.
  - **Nota de re-adjudicación de la secundaria (autora, 2026-07-10):** la hipótesis intermedia `{faithfulness, completitud_kg}` se descartó porque la precondición del re-lanzamiento encontró el nodo portador de la fórmula (`Operacion_calculo_de_exigencia_por_riesgo`); el barrido inicial lo había perdido por variante léxica (buscaba "APRc", el nodo escribe "APR_c").
  - Cada causa va con sus tres piezas de evidencia (afirmación / nodo / fuente).
- **Palanca/riesgo esperados (Paso 4):** la primaria → grafo/esquema (crear el nodo de frecuencia faltante); la secundaria → prompt del agente RAG. Ambas de **alto riesgo** → revisión humana.
- **Por qué la primaria es ALTO riesgo (confirmado):** el nodo de frecuencia para riesgo de crédito **no existe — hay que crearlo de cero**, y crear estructura nueva es decisión de modelado, no transcripción de un dato literal único. Por eso difiere de CQ-034, que es bajo riesgo (ahí el dato está literal en el PDF y solo se completa).

### CQ-025 — `multi_norma` (frecuencia de reporte) · TO: regimen
- **Pregunta:** ¿Con qué frecuencia se informa la exigencia por riesgo de mercado y el ratio de apalancamiento?
- **Atribución humana (confirmada — verificada contra el PDF real — MIXTA: una pata de sistema PRIMARIA + una pata que es falso positivo del juez):** caso de [atribución múltiple](taxonomia.md), estructuralmente como CQ-017 (dos patas independientes), pero con causas de **distinto tipo**.
  - **Pata 1 (riesgo de mercado) — `{noise_sensitivity, contenido_kg}`, PRIMARIA (defecto de grafo):** el PDF (Punto 1.1 del TO de Régimen Informativo) ubica los datos de riesgo de mercado (puntos 4.3-4.5) en la lista de excepciones **trimestrales**. Pero el nodo `Operacion_calculo_de_riesgo_de_mercado` del grafo dice "mensual" — claim soportado por el nodo consultado pero incorrecto contra el PDF. El extractor confundió: en el pasaje, "mensual" califica al **código de consolidación** ("consolidado mensual"), no a la frecuencia de reporte, que es **trimestral** según el encabezado del bloque. El nodo afirma un contenido que contradice el PDF → `contenido_kg`.
  - **Pata 2 (ratio de apalancamiento) — falso positivo del juez (NO defecto de grafo ni de agente; sin par v2 — no es defecto del sistema):** el agente respondió correctamente que el apalancamiento es **trimestral** y citó bien el Punto 10.1 (verificado contra el PDF: el Punto 10.1.1 contiene "los datos se informarán con frecuencia trimestral"). El juez marcó esa afirmación como falsa, pero era correcta → ruido del juez, no un defecto del sistema.
- **Calibración (regla específica):** como la pata 1 es la causa primaria de **sistema** (defecto de grafo), el verificador **acierta si detecta la pata 1 como `contenido_kg` (defecto de grafo)**. Reconocer la pata 2 como **falso positivo del juez** suma pero es **secundario**. Detectar la pata 1 como "navegación" (defecto de agente) **NO** es acierto: el dato correcto (trimestral) **no existe en el grafo**, así que no es que el agente no lo encontró — es que el grafo lo tiene mal.
- **Palanca/riesgo esperados (Paso 4):** pata 1 → grafo/esquema (corregir el contenido del nodo: mensual→trimestral, contra el pasaje del PDF); pata 2 → ninguna acción sobre el sistema (ruido del juez, se reporta como falso positivo).

---

## Por qué estos 5 y no otros

Son las fallas reales de `run_3` ya diagnosticadas a mano: cubren completitud de bajo riesgo (CQ-034), alcanzabilidad léxica de alto riesgo (CQ-031), un caso de alto riesgo con **dos causas primarias de grafo** (estructural + provenance: CQ-017), un caso **mixto primaria-grafo + secundaria-agente** (CQ-020) y un caso **mixto `contenido_kg` (grafo) + falso positivo del juez** (CQ-025). Calibrar contra ellos prueba que el agente distingue las situaciones que el Paso 4 va a enrutar distinto, y que maneja los tres patrones de atribución múltiple. Si el agente no reproduce estas atribuciones conocidas, no hay razón para confiar en las que haga a escala sobre fallas sin diagnóstico previo.

**Cobertura de lados (v2):** las CINCO PRIMARIAS son lado grafo; la única causa lado agente del set es la secundaria de CQ-020 (`{faithfulness, alucinacion_agente}`, no exigida para el acierto). La discriminación de frontera lado-agente se ejercita en el dev set de calibración; queda abierta la incorporación futura de un caso-control con primaria lado agente.
````

*(Fin del contenido verbatim de `casos_control.md` — 75 líneas, completo.)*

---

# SECCIÓN 2 — TAXONOMÍA VIGENTE, VERBATIM

Fuente: `.claude/skills/kg-refinement/references/taxonomia.md` en HEAD.

**Versión declarada en el archivo (reporte sin corregir):** el archivo NO tiene un campo único
"versión = v2.6.1". El título (línea 1) dice **"Taxonomía v2 (dos capas, alineada RAGAS) +
herramientas del verificador"**, y la versión más reciente del changelog es **"v2.6.1
(2026-07-15) — corrección documental (sin cambio normativo)"**. Es decir: la versión vigente
según el changelog es v2.6.1; el título genérico dice "v2". Se reporta tal cual, sin corregir.

## 2(a) — Definiciones completas de las categorías de capa 2 (causas raíz), verbatim

````markdown
## Capa 2 — Causa raíz (cerrada)

### Defectos del grafo

El dato falla por algo del KG, no por cómo lo usó el agente.

| Categoría | Qué significa | Evidencia que la confirma |
|---|---|---|
| **contenido_kg** | Un nodo **contradice** el PDF (dice algo que el PDF no dice, o lo dice mal). | El nodo afirma X; el pasaje del PDF dice no-X o algo incompatible. |
| **completitud_kg** | Falta información que el PDF **sí tiene** (nodo stub/vacío, extracción incompleta, dato ausente). | El PDF contiene el dato; en el grafo el nodo está vacío, truncado o ausente el campo. Exige constancia de búsqueda (campo `busquedas`). |
| **estructural_kg** | Falta un **nodo o una arista** que la pregunta necesita para conectar la información. | Los datos existen sueltos pero no hay relación que los una (ej. cruce entre dos TOs). |
| **provenance_imprecisa** | El nodo **cita un punto que no funda su contenido** (la cita apunta a otro lado: índice, sección equivocada). | La `location`/`source_doc` del nodo no contiene el contenido que dice fundamentar. |
| **alcanzabilidad_kg** (nueva en v2) | El **nodo portador existe con el contenido correcto**, pero es **inalcanzable por la búsqueda léxica**: `buscar_nodos` indexa label/id, no description, y ninguna búsqueda razonable desde los términos de la pregunta lo devuelve. "Términos de la pregunta" = vocabulario **ex ante** del agente (pregunta + outputs COMPLETOS de su propia trayectoria); lo aprendido del PDF/GT durante la verificación NO cuenta (v2.1). | Exhibir el nodo (quote de su contenido) + constancia de búsqueda (campo `busquedas`) mostrando que los términos plausibles del vocabulario ex ante NO lo alcanzan y que solo se alcanza con palabras del propio nodo. |

### Defectos del agente

La información estaba bien en el grafo; el problema es cómo el agente la usó.

| Categoría | Qué significa | Evidencia que la confirma |
|---|---|---|
| **navegación** | El agente **no encontró** info que SÍ estaba en el grafo y era alcanzable. | Existe un nodo relevante, fiel y alcanzable con búsquedas razonables — la carga de la prueba es **exhibirlo**, con quote de su CONTENIDO (no su label); la trayectoria muestra que el agente no lo consultó o lo descartó. |
| **alucinacion_agente** | El agente **agregó glosas o afirmaciones no soportadas** por los nodos que consultó. Dos modos: **(a)** el grafo TENÍA el dato y el agente afirmó sin soporte de su trayectoria; **(b)** **glosa de cosecha propia**: ni el grafo ni el PDF tienen el dato. | La respuesta contiene afirmaciones que no están en ningún nodo de la trayectoria. Modo (a): exhibir el nodo portador (quote de su contenido). Modo (b): constancia de búsqueda (campo `busquedas`) + verificación negativa contra el PDF (`leer_pasaje_pdf`) — acá NO hay nodo que exhibir. |
| **aplicacion_erronea** (nueva en v2.5) | El agente **usó contenido fiel de un nodo consultado fuera de su alcance** (otra cartera, otro régimen, otra sección u otro concepto que el que la pata pregunta). El contenido es correcto en su contexto de origen; la aplicación a esta pata es incorrecta. (Palanca del Paso 4: prompt del agente RAG.) **Criterio (v2.6): SOLO aplica si el ALCANCE está declarado EN el contenido del nodo (cartera, régimen, sección) y el agente lo ignoró. Si el nodo OMITE su alcance (label genérico, definición sin marca de cartera/régimen), el defecto es del grafo → `contenido_kg` por des-scoping. Test: ¿el nodo, leído solo, le avisa a un lector que su contenido es de otro alcance? Sí → `aplicacion_erronea`. No → `contenido_kg`.** | El nodo con su quote y provenance + el pasaje del PDF que muestra el **alcance real** del contenido + la identificación del **alcance que la pata requería**. |

### Sin defecto y abstención

| Categoría | Lado | Qué significa |
|---|---|---|
| **sin_defecto** | ninguno | La respuesta en realidad no estaba mal: posible falso positivo del juez. Atribución de **último recurso**: exige descartar activamente cada defecto de la taxonomía, uno por uno, documentando el descarte. |
| **frontera_no_determinada** | indeterminado | Tras investigar a fondo, la evidencia no alcanza para decidir entre DOS categorías. **Abstención honesta de primera clase**: una etiqueta equivocada es PEOR que una abstención honesta; adivinar no es atribuir. Exige (a) documentar qué se buscó y qué se encontró (campo `busquedas`), (b) nombrar las DOS categorías en disputa (campo `entre`), (c) declarar qué evidencia faltante decidiría el caso (campo `evidencia_faltante`). |
````

## 2(b) — Mapa síntoma→causas con sus criterios de decisión, verbatim

Nota de compilación: el "mapa síntoma→causas" del archivo es la sección "Árbol de decisión
capa 1 → capa 2". Se copia completa, incluida su línea de cierre. (Los criterios del árbol
referencian la regla de precedencia y el test de pertinencia v2.2 definidos en la sección
"Capa 1" del mismo archivo; esa sección no fue pedida y no se copia acá.)

````markdown
## Árbol de decisión capa 1 → capa 2

El síntoma (capa 1) determina qué preguntas hacer para llegar a la causa (capa 2):

- **faithfulness** → ¿el grafo tenía el dato?
  - Encontrado (exhibirlo, quote de su contenido) → `alucinacion_agente`.
  - No encontrado + búsqueda exhaustiva documentada (términos plausibles cubiertos, campo `busquedas`) → ¿el PDF tiene el dato? (`leer_pasaje_pdf`):
    - Sí → `completitud_kg` (el hueco del grafo empujó la glosa).
    - No → `alucinacion_agente` (glosa de cosecha propia; acá NO hay nodo que exhibir — la evidencia es la constancia de búsqueda + la verificación negativa contra el PDF).
  - No encontrado sin garantía de exhaustividad → `frontera_no_determinada`.
- **noise_sensitivity** → ¿el nodo consultado es fiel al PDF?
  - Contradice el PDF → `contenido_kg`.
  - La cita apunta a otro lado (índice, sección equivocada) → `provenance_imprecisa`.
  - Es fiel → ¿el nodo es PERTINENTE a la pata (test v2.2)?
    - Sí → `sin_defecto` (falso positivo del juez).
    - No, y el dato pertinente SÍ estaba disponible/expuesto en la trayectoria → `aplicacion_erronea` — **SOLO si el ALCANCE está declarado EN el contenido del nodo** (cartera, régimen, sección) y el agente lo ignoró. Si el nodo OMITE su alcance (label genérico, definición sin marca de cartera/régimen), el defecto es del grafo → `contenido_kg` por des-scoping. Test: ¿el nodo, leído solo, le avisa a un lector que su contenido es de otro alcance? Sí → `aplicacion_erronea`. No → `contenido_kg`.
    - No, y el dato pertinente NO estaba disponible → esto debió resolverse como `context_recall` a nivel pata (C1a); revisá la clasificación del síntoma antes de emitir.
- **context_recall** → ¿existe nodo portador del dato faltante?
  - Existe y las búsquedas razonables del agente lo alcanzaban → `navegación`.
  - Existe pero solo se alcanza con palabras del propio nodo (no de la pregunta) → `alcanzabilidad_kg`.
  - No existe → `completitud_kg` (falta el dato) o `estructural_kg` (falta la conexión).
  - **Prueba de alcanzabilidad (v2.1):** "búsquedas razonables" y "términos de la pregunta" = vocabulario disponible EX ANTE para el agente — los términos de la pregunta más los que los outputs COMPLETOS de su propia trayectoria le expusieron. El vocabulario aprendido del PDF o del ground truth durante la verificación NO cuenta para esta prueba.

La constancia de búsqueda es lo único que distingue "falta" (`completitud_kg`) de "está pero no se llega" (`alcanzabilidad_kg`) de "no lo encontré yo" (`frontera_no_determinada`).
````

## 2(c) — Changelog completo, verbatim

````markdown
> **Changelog v1 → v2:** la v1 era de una sola capa. La etiqueta **generación-de-más** se eliminó como categoría y se partió: su síntoma es `faithfulness` (capa 1) y su causa lado-agente pasa a llamarse `alucinacion_agente` (capa 2). Se agregó `alcanzabilidad_kg` (lado grafo, sin equivalente v1). Las corridas viejas (calibraciones v1–v4 del verificador, mapa de defectos de la Fase 2.3) se leen con el vocabulario v1: ver la tabla de correspondencia en `mapeo_taxonomia_v1_v2.md`.
> **v2.1 (2026-07-14):** se precisa la prueba de alcanzabilidad (rama `context_recall` del árbol y fila `alcanzabilidad_kg`): "búsquedas razonables" y "términos de la pregunta" = vocabulario disponible **ex ante** para el agente (la pregunta + lo que los outputs COMPLETOS de su propia trayectoria le expusieron); el vocabulario aprendido del PDF o del ground truth durante la verificación NO cuenta.
> **v2.2 (2026-07-14):** se precisa "pertinente" en la regla de precedencia: el nodo que porta LA RESPUESTA a la pata, no información sobre su tema (test del nodo único).
> **v2.3 (2026-07-14):** se precisa "soporte": "soportado por lo consultado" = el contenido EXPUESTO al agente en los outputs COMPLETOS de su trayectoria — incluye los `resumen_propiedades` de resultados de `buscar_nodos`, no solo lo abierto con `ver_nodo`. (Coherente con la noción ex ante de v2.1.)
> **v2.4 (2026-07-14):** el soporte de un claim se evalúa contra TODO el contenido expuesto (pertinente o no); la pertinencia gobierna solo C1a (context_recall por pata), nunca el test de soporte por claim (C1b); faithfulness exige verificación previa con ver_paso_completo de los pasos truncados que pudieron exponer el contenido.
> **v2.5 (2026-07-14) — expuesto por el gate #1, caso run_3/CQ-025: el árbol no tenía salida para "nodo fiel mal aplicado":** nueva causa de capa 2, lado agente, `aplicacion_erronea`; la rama `noise_sensitivity`/"nodo fiel" ahora bifurca por pertinencia (test v2.2) en vez de salir directo a `sin_defecto`. La taxonomía sigue CERRADA (con esta categoría incluida).
> **v2.6 (2026-07-15) — la desambiguación de `aplicacion_erronea` faltaba en ESTE archivo; estaba solo en la vara, que el verificador no lee:** criterio des-scoping vs aplicación en la definición y en la rama `noise_sensitivity` (SOLO es `aplicacion_erronea` si el alcance está declarado EN el nodo; si el nodo lo omite → `contenido_kg`); regla de jerarquía nueva en atribución múltiple (si TODOS los claims centrales fallidos son falsos positivos del juez, el caso NO tiene primaria).
> **v2.6.1 (2026-07-15) — corrección documental (sin cambio normativo):** la nota de "Ejemplos resueltos" afirmaba que el ensamblado por referencia incluye las piezas de evidencia y la atribución múltiple; el código (`taxonomia_section()`) corta antes (desde el encabezado de Capa 1 hasta el de Las tres piezas, exclusive), así que esas secciones —incluida la regla de jerarquía v2.6— viajan en el bloque fijo del prompt de `verificador.py`. (Ojo: los marcadores de corte no deben citarse literalmente con su prefijo de encabezado fuera de su sección — el ensamblador usa la PRIMERA ocurrencia.)
````

---

# SECCIÓN 3 — EVIDENCIA PREVIA POR CASO

Output de `git ls-files | grep referencias_dev_set`:

```
.claude/skills/kg-refinement/references/referencias_dev_set.md
```

**Aclaración estructural imprescindible (sin la cual esta sección se malinterpreta):**
`referencias_dev_set.md` es el archivo del **DEV SET** — casos de `run_1`/`run_5` usados como
banco de iteración del verificador. **NO contiene secciones para los 5 casos-control de
`run_3`**; su propio texto dice: "Los 5 casos-control de `run_3` son el GATE FINAL
pre-registrado […] Los 5 casos-control de run_3 NO se corren durante la iteración". Las
secciones del archivo que comparten número de CQ con los casos-control son **casos distintos
sobre otros grafos** (misma pregunta, otro run): `off/run_5/CQ-017`, `off/run_1/CQ-020`,
`off/run_1/CQ-031`. Estado por caso-control:

| Caso-control (run_3) | Sección en `referencias_dev_set.md` | Qué hay |
|---|---|---|
| CQ-017 | **NO hay sección del caso run_3.** Existe `## Caso off/run_5/CQ-017` (misma pregunta, grafo run_5) — se copia abajo. | homólogo dev |
| CQ-020 | **NO hay sección del caso run_3.** Existe `## Caso off/run_1/CQ-020` (misma pregunta, grafo run_1) — se copia abajo. | homólogo dev |
| CQ-025 | **NO hay sección — ni de run_3 ni homóloga.** CQ-025 no aparece en el archivo. | nada |
| CQ-031 | **NO hay sección del caso run_3.** Existe `## Caso off/run_1/CQ-031` (misma pregunta, grafo run_1) — se copia abajo. La nota de re-adjudicación de ese caso dev cita un **contrafáctico empírico de run_3/CQ-031** (evidencia previa directamente relevante a la vara). | homólogo dev |
| CQ-034 | **NO hay sección — ni de run_3 ni homóloga.** CQ-034 no aparece en el archivo. | nada |

Conforme al criterio de aceptación, se dice explícitamente en lugar de rellenar: **CQ-025 y
CQ-034 no tienen sección en `referencias_dev_set.md`.** Los tres homólogos dev existentes se
copian verbatim y completos a continuación (son evidencia previa sobre las mismas preguntas,
adjudicada por la autora, aunque sobre otros grafos).

## 3.1 — CQ-017: sección homóloga `## Caso off/run_5/CQ-017`, verbatim y completa

````markdown
## Caso off/run_5/CQ-017

**Pregunta:** Un operador de cambio, ¿está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros y debe intervenir como entidad autorizada en el mercado de cambios?

Adjudicación de la autora, 2026-07-13, asistida por revisión:

- **Pata 2** ("debe intervenir como entidad autorizada") — **DOS PRIMARIAS, SOBREDETERMINADA** (re-adjudicada por la autora, 2026-07-14, por los micro-hechos de la iteración 4):
  - **`{context_recall, alcanzabilidad_kg}` PRIMARIA (a):** los portadores de la regla de Exterior 1.1 existen (`intervencion_de_entidades_autorizadas_en_operaciones_de_camb`, `entidades_financieras_o_cambiarias_autorizadas__agencia_cambio`, `entidades_autorizadas_a_operar_en_cambios__otra`) pero ninguno apareció en las búsquedas del agente (pasos 3/12/15, re-ejecutados determinísticamente); por la regla de precedencia, el nodo entidad_operadora usado para rellenar no cuenta como contexto de la pata.
  - **`{noise_sensitivity, contenido_kg}` PRIMARIA (b) — reemplaza a la secundaria `{faithfulness, alucinacion_agente}` (modo b) del 2026-07-13:** el claim central es eco casi verbatim del `resumen_propiedades` de `operador_de_cambios__otra` ("Entidad financiera autorizada a operar en el mercado de cambios"), expuesto al agente en runtime en los pasos 1 (pos. 7) y 12 (pos. 8), ambos en tramo truncado (re-ejecución determinística 2026-07-14); la description contradice el PDF (Exterior 1.1: "financieras **o cambiarias**" — categorías distintas) y su provenance (Punto 4.8, disposiciones BOPREAL) no funda el contenido — **agravante `provenance_imprecisa` documentada**.
  - **Nota de sobredeterminación:** cada primaria alcanza SOLA para romper la pata (contrafácticos: portadores del 1.1 alcanzables → el agente encuentra la regla correcta; description del nodo corregida → el eco del agente sale correcto). Patrón nuevo, **consignado para la reunión de mentores**.
  - **Regla de acierto del caso:** patrón "varias primarias" de `casos_control.md` — el acierto exige detectar AMBAS.
- **Pata 2 — claim** "Existen entidades denominadas 'entidades operadoras en mercado de cambios' que son entidades financieras autorizadas..." — **`{noise_sensitivity, contenido_kg}` SECUNDARIA.** Evidencia: soportado por `entidad_operadora_en_mercado_de_cambios__otra`, cuyo contenido omite "o cambiarias" (contra Exterior 1.1) y cuya provenance (Punto 3.16) no funda el contenido (verificado: el 3.16 es requisitos de egresos/ARCA).
- **Pata 1 — claim de la enumeración de sujetos obligados** — **`{noise_sensitivity, contenido_kg}` SECUNDARIA** (re-adjudicado 2026-07-14). Evidencia: soportado por el nodo `sujeto_obligado` (abierto en el paso 13), que enumera 5 categorías; el PDF Punto 1.1.2 enumera 7 (agrega 1.1.2.6 PSPCP y 1.1.2.7 PSI/billetera digital, verificado 2026-07-14) — claim soportado por nodo consultado e **incompleto contra el PDF**.
  - **Nota de re-adjudicación (autora, 2026-07-14):** reemplaza el FALSO POSITIVO DEL JUEZ del 2026-07-13, cuya verificación chequeó **presencia** de la enumeración pero no su **exhaustividad** contra el PDF.
- **Pata 1 — las 4 glosas de obligaciones** (información clara, trato equitativo, acceso igualitario, resolución de reclamos) — **FALSOS POSITIVOS DEL JUEZ, sin par** (re-adjudicado 2026-07-14). Evidencia: los 4 edges (`debe_garantizar → trato_equitativo_y_digno` y `→ derecho_a_informacion_clara_y_suficiente`; `debe_adoptar → acceso_igualitario_a_servicios_financieros`; `recae_sobre → consideracion_y_resolucion_fundada_de_reclamos`) existen en el output COMPLETO del paso 10 del agente (re-ejecución determinística, auditoría 2026-07-14); el agente los tuvo en runtime (el harness pasa outputs completos y almacena truncados) y son fieles al PDF (1.1.2, 1.2, 2.x).
  - **Nota de re-adjudicación (autora, 2026-07-14):** fundada en la auditoría de truncamiento — la traza almacenada no es el contexto del agente (`harness.py` pasa outputs completos al agente y almacena truncados); verificación por re-ejecución determinística.

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion.md` (scratch, no versionado).
````

**Otras notas tracked relevantes a CQ-017 (rutas + una línea, sin copiar contenido):**
- `data/experiment/evaluacion/adjudicacion_FIRMADO.json` — diagnóstico firmado original de la autora sobre las 5 fallas de run_3 (vocabulario v1), base de la vara actual.
- `data/experiment/evaluacion/adjudicacion_pendiente.json`, `adjudicacion_worksheet.json`, `adjudicacion_worksheet.md` — material de trabajo de esa adjudicación.
- `data/experiment/evaluacion/frozen_run/reporte_final.md` (y `reporte_final_draft.md`) — veredictos originales del frozen por CQ.
- `data/experiment/evaluacion/posthoc_run/revision_prompt_v4/tabla_v1_v4.md` — qué emitió cada versión v1–v4 del verificador sobre CQ-017.
- `docs/especificacion_verificador_v57.md` — historia del instrumento; incluye la medición N=3 de CQ-017 (perfil "parcial estable en sobredeterminación").
- `docs/protocolo_gate2.md` — protocolo pre-registrado del gate #2, del que estos 5 casos son la vara.
- `docs/hallazgos_tesis.md` y `docs/ARQUITECTURA.md` — menciones del caso en hallazgos/arquitectura.
- `.claude/skills/kg-refinement/references/mapeo_taxonomia_v1_v2.md` — correspondencia v1→v2 para leer el diagnóstico firmado.
- `data/experiment/evaluacion/queries/eval_set_v1.json`, `eval_set_v2.json`, `candidatas.json` — texto de la pregunta y `ground_truth_secciones`.
- `data/experiment/evaluacion/verificador.py`, `verifier_pilot.py` — código del verificador; menciones del caso en comentarios/estructura.

## 3.2 — CQ-020: sección homóloga `## Caso off/run_1/CQ-020`, verbatim y completa

````markdown
## Caso off/run_1/CQ-020

**Pregunta:** ¿Cómo se calcula la exigencia de capital por riesgo de crédito (CRC) y con qué frecuencia se reporta al BCRA?

Adjudicación de la autora, 2026-07-13, asistida por revisión:

- **Pata 1 (cálculo) — claim central** "INC es el Incremento de exigencia por riesgo de crédito por excesos en participaciones en capital de empresas" — **`{noise_sensitivity, contenido_kg}` PRIMARIA.** Evidencia (precisada 2026-07-14, sin cambio de par ni jerarquía): el claim reproduce casi verbatim el label del nodo `req_incremento_de_exigencia_por_riesgo_de_credito_por_excesos_en_participaciones_en_capital_de_empresas_inc`, que estaba en el **TRAMO TRUNCADO** del output del paso 1 (5º resultado — visible en runtime, no en la traza almacenada), junto con su resumen ("Exigencia de capital adicional por inversiones significativas en empresas que exceden límites regulados"); ese label conflata INC(inversiones significativas, límites 15%/60% dentro de APRC) con el INC de la fórmula CRC (excesos en activos inmovilizados etc., Capitales 2.1) — soporte infiel al PDF.
  - **Nota de re-adjudicación (autora, 2026-07-14):** precisión de evidencia fundada en la auditoría de truncamiento — la traza almacenada no es el contexto del agente (`harness.py` pasa outputs completos al agente y almacena truncados); verificación por re-ejecución determinística.
- **Los otros 7 claims negativos** (k escala 1-1,19; k asignado por SEFyC; APRC suma con ponderadores; reporte vía R.I.-C.M.; y las 3 secundarias del R.I.-C.M.) — **FALSOS POSITIVOS DEL JUEZ, sin par.** Evidencia: soportados por los nodos abiertos (`req_factor_k`, `con_activos_ponderados_por_riesgo_de_credito_aprc`, `ins_regimen_informativo_contable_mensual`, `rep_regimen_informativo_contable_mensual_sobre_capitales_minimos`) y correctos contra el PDF (Capitales 2.1: escala k 1/1,03/1,08/1,13/1,19, calificación SEFYC, expresión de APRC; Régimen 1.1: frecuencia mensual por defecto).
- **Pata 2 (frecuencia)** — "mensual vía R.I.-C.M." — **sin defecto.** Evidencia: soportado por `ins_regimen_informativo_contable_mensual` (abierto en el paso 9) y correcto contra Régimen 1.1 (la exigencia por riesgo de crédito no está en las excepciones trimestrales).

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion.md` (scratch, no versionado).
````

**Otras notas tracked relevantes a CQ-020 (rutas + una línea):**
- `data/experiment/evaluacion/posthoc_run/revision_prompt_v4/caso_CQ-020.md` — nota de caso dedicada de la revisión del prompt v4 (única de los 5 junto con CQ-034 que tiene archivo propio).
- Los comunes listados en 3.1 aplican igual: `adjudicacion_FIRMADO.json` + worksheets, `frozen_run/reporte_final.md`, `tabla_v1_v4.md`, `docs/especificacion_verificador_v57.md` (medición N=3: "discrepancia sistemática en conflación sutil"), `docs/protocolo_gate2.md`, `docs/hallazgos_tesis.md`, `docs/ARQUITECTURA.md`, `mapeo_taxonomia_v1_v2.md`, `queries/eval_set_v1.json`/`eval_set_v2.json`/`candidatas.json`.

## 3.3 — CQ-025: sin sección en `referencias_dev_set.md`

**CQ-025 NO tiene sección en `referencias_dev_set.md` (ni del caso run_3 ni homóloga de otro
run). No se rellena con material de otra fuente.**

**Notas tracked relevantes a CQ-025 (rutas + una línea):**
- `.claude/skills/kg-refinement/references/taxonomia.md` — el changelog v2.5 registra que el gate #1 sobre run_3/CQ-025 expuso el hueco "nodo fiel mal aplicado" y motivó `aplicacion_erronea`.
- `docs/especificacion_verificador_v57.md` — resultados del caso por versión; el disclosure inter-gates de `c0b96a4` registra el asterisco CQ-025→v2.5.
- `docs/protocolo_gate2.md` — protocolo del gate #2 (CQ-025 es uno de los 5 de la vara; disclosure del asterisco).
- `data/experiment/evaluacion/posthoc_run/revision_prompt_v4/tabla_v1_v4.md` — fila CQ-025 de la comparación v1–v4 (✗ navegación en las 4 versiones).
- `docs/hallazgos_tesis.md` — menciones del caso (además, CLAUDE.md lo registra como caso de expansión de corpus: apunta a un TO fuera del subset).
- `data/experiment/evaluacion/verifier_pilot.py` — código del pilot; menciones del caso.
- `data/experiment/evaluacion/queries/eval_set_v1.json`/`eval_set_v2.json`/`candidatas.json` — texto de la pregunta.
- Comunes: `adjudicacion_FIRMADO.json` no aparece en el grep de CQ-025 (el id no figura en ese JSON) — se reporta tal cual; `frozen_run/reporte_final.md` tampoco aparece en el grep para este caso.

## 3.4 — CQ-031: sección homóloga `## Caso off/run_1/CQ-031`, verbatim y completa

````markdown
## Caso off/run_1/CQ-031

**Pregunta:** ¿Qué deudores no deben ser objeto de clasificación y respecto de qué deudores no corresponde evaluar la capacidad de repago?

Adjudicación de la autora, 2026-07-13, asistida por revisión:

- **Pata 1** ("qué deudores no deben ser objeto de clasificación") — **UNA PRIMARIA + UNA SECUNDARIA** (re-adjudicada por la autora, 2026-07-14):
  - **`{context_recall, alcanzabilidad_kg}` PRIMARIA — ítem 4.5:** el portador `rsj_deudor_con_garantias_preferidas_a` existe, fiel, pero es inalcanzable **ex ante**: label sin vocabulario de la pregunta; no apareció en las 8 buscar_nodos de la traza (outputs completos, re-ejecutados) y "garantías" no fue expuesto al agente por ningún output de los pasos 1–14. Aplica la prueba de alcanzabilidad ex ante de `taxonomia.md` v2.1.
  - **`{context_recall, navegación}` SECUNDARIA — ítem 4.6:** el edge `ope_clasificacion_de_deudores --no_está_sujeta_a--> ope_creditos_cedidos_sin_responsabilidad_para_el_cedente` (prov. p.15) fue **visible en runtime** en el output completo del paso 15 (`harness.py` pasa outputs completos al agente y almacena truncados en la traza) y no fue explotado.
  - **Nota de re-adjudicación (autora, 2026-07-14):** la jerarquía del ítem 4.6 se corrige (primaria → secundaria) por el **contrafáctico empírico de run_3/CQ-031** — el agente de run_3 respondió la pata 1 únicamente con la cesión del 4.6 y el juez la reprobó igual (claim central `no_soportado`; cita al 4.6 marcada `falso`), demostrando que el 4.6 solo NO mueve el veredicto: lo decisivo es el 4.5 (la `cita_textual` del GT). El desacuerdo surgió en la iteración 2 del verificador v5.1; la corrección se funda en el contrafáctico, no en el output del instrumento. (Historia del GT: 2026-07-13 primaria única `alcanzabilidad_kg`; 2026-07-14 AM mixta con dos primarias, motivada por la iteración 1 y el micro-hecho del paso 15 — los `ver_vecinos` completos de los pasos 5 y 6 no exponen ningún portador; 2026-07-14 esta corrección de jerarquía.)
- **Pata 2** ("respecto de qué deudores no corresponde evaluar la capacidad de repago") — **`{context_recall, alcanzabilidad_kg}` PRIMARIA.** Evidencia: el dato GT (4.4) nunca apareció en la trayectoria; los portadores `cla_garantias_preferidas_a` y `cla_financiaciones_con_garantias_preferidas_a` son alcanzables solo por vocabulario propio ("garantías preferidas"), no por los términos de la pregunta.
- **Los 2 claims de "monto reducido" marcados falso por el juez** — **FALSOS POSITIVOS DEL JUEZ, sin par** (no es defecto del sistema). Evidencia: claim 1 soportado por `cla_deudores_por_prestamos_de_monto_reducido` y correcto contra el PDF (TO Clasificación, Sección 7: "No será obligatoria la evaluación de la capacidad de pago en función de los ingresos [...] préstamos de monto reducido"); claim 2 ídem con salvedad (generaliza sin el calificador "por ingresos").

Material del caso: dossier completo en `posthoc_run/dev_set/hoja_adjudicacion.md` (scratch, no versionado).
````

**Otras notas tracked relevantes a CQ-031 (rutas + una línea):**
- `.claude/skills/kg-refinement/references/formato_propuesta.md` — formato de propuesta de cambio de la skill; usa CQ-031 como ejemplo.
- `data/experiment/evaluacion/demo_evaluacion.html` y `gen_demo_html.py` — demo HTML de la evaluación que incluye la traza de CQ-031.
- **Advertencia de disponibilidad:** la vara cita `posthoc_run/auditoria_gt/CQ-031.md` (auditoría GT, barrido sobre los 4.050 nodos) como motivación de la re-adjudicación del 2026-07-10 — ese archivo **NO está tracked** (el directorio `posthoc_run/auditoria_gt/` está gitignored); existe solo como scratch local.
- Comunes: `adjudicacion_FIRMADO.json` + worksheets, `frozen_run/reporte_final.md`, `tabla_v1_v4.md` (fila CQ-031 + nota al pie "GT en re-adjudicación" con el hallazgo de inalcanzabilidad léxica), `docs/especificacion_verificador_v57.md` (medición N=3: "varianza genuina 1/1/1 → triage humano"), `docs/protocolo_gate2.md`, `docs/hallazgos_tesis.md`, `mapeo_taxonomia_v1_v2.md`, `queries/*.json`, `verifier_pilot.py`.

## 3.5 — CQ-034: sin sección en `referencias_dev_set.md`

**CQ-034 NO tiene sección en `referencias_dev_set.md` (ni del caso run_3 ni homóloga de otro
run). No se rellena con material de otra fuente.**

**Notas tracked relevantes a CQ-034 (rutas + una línea):**
- `data/experiment/evaluacion/posthoc_run/revision_prompt_v4/caso_CQ-034.md` — nota de caso dedicada (la falla de formato del v4 con sustancia correcta: JSON inválido pero diagnóstico `completitud_kg` en `final_raw`).
- `data/experiment/evaluacion/posthoc_run/revision_prompt_v4/tabla_v1_v4.md` — fila CQ-034 + nota al pie sobre la falla operativa del v4.
- Comunes: `adjudicacion_FIRMADO.json` + worksheets, `frozen_run/reporte_final.md`, `docs/especificacion_verificador_v57.md`, `docs/protocolo_gate2.md`, `docs/hallazgos_tesis.md`, `docs/ARQUITECTURA.md`, `mapeo_taxonomia_v1_v2.md`, `queries/*.json`, `verifier_pilot.py`.

---

# SECCIÓN 4 — CHEQUEO ESTRUCTURAL DE LOS JSONs DEL GATE (SOLO CLAVES Y CONTEOS)

Restricción respetada: **no se leyó, extrajo, citó ni parafraseó ningún VALOR** de campos de
veredicto, síntoma, causa, justificación o texto libre del verificador. Todos los comandos
son `jq` de claves, tipos y longitudes. En particular, el valor del campo `voto` (top-level)
y los valores de `atribuciones`/`razonamiento`/`extraccion_traza`/`detectores` **no fueron
abiertos**. Los únicos valores leídos son `n_reps` (campo de conteo, necesario para el
objetivo del chequeo) y los derivados estructurales `type`/`length`.

**Comando 1 — claves de nivel superior:**

```
$ cd data/experiment/evaluacion/posthoc_run/dev_set/gate2_v57
$ for f in *.json; do echo "=== $f ==="; jq -c 'keys' "$f"; done
=== off_run_3_CQ-017.json ===
["id_falla","n_reps","repeticiones","run","voto"]
=== off_run_3_CQ-020.json ===
["id_falla","n_reps","repeticiones","run","voto"]
=== off_run_3_CQ-025.json ===
["id_falla","n_reps","repeticiones","run","voto"]
=== off_run_3_CQ-031.json ===
["id_falla","n_reps","repeticiones","run","voto"]
=== off_run_3_CQ-034.json ===
["id_falla","n_reps","repeticiones","run","voto"]
```

**Comando 2 — tipo y longitud de `repeticiones` + campo de conteo `n_reps`:**

```
$ for f in *.json; do echo "=== $f ==="; jq -c '{tipo_repeticiones: (.repeticiones | type), cantidad_repeticiones: (.repeticiones | length), n_reps: .n_reps}' "$f"; done
=== off_run_3_CQ-017.json ===
{"tipo_repeticiones":"array","cantidad_repeticiones":3,"n_reps":3}
=== off_run_3_CQ-020.json ===
{"tipo_repeticiones":"array","cantidad_repeticiones":3,"n_reps":3}
=== off_run_3_CQ-025.json ===
{"tipo_repeticiones":"array","cantidad_repeticiones":3,"n_reps":3}
=== off_run_3_CQ-031.json ===
{"tipo_repeticiones":"array","cantidad_repeticiones":3,"n_reps":3}
=== off_run_3_CQ-034.json ===
{"tipo_repeticiones":"array","cantidad_repeticiones":3,"n_reps":3}
```

**Comando 3 — claves de cada repetición (nombres de campos solamente):**

```
$ for f in *.json; do echo "=== $f ==="; jq -c '.repeticiones[] | keys' "$f"; done
=== off_run_3_CQ-017.json ===
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
=== off_run_3_CQ-020.json ===
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
=== off_run_3_CQ-025.json ===
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
=== off_run_3_CQ-031.json ===
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
=== off_run_3_CQ-034.json ===
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
["_meta","atribuciones","detectores","errores_formato","extraccion_traza","formato_invalido","id_falla","razonamiento","run"]
```

**Conclusión del chequeo (objetivo cumplido):**

| Archivo | Repeticiones (clave `repeticiones`, array) | `n_reps` | Consistente |
|---|---|---|---|
| off_run_3_CQ-017.json | 3 | 3 | ✓ |
| off_run_3_CQ-020.json | 3 | 3 | ✓ |
| off_run_3_CQ-025.json | 3 | 3 | ✓ |
| off_run_3_CQ-031.json | 3 | 3 | ✓ |
| off_run_3_CQ-034.json | 3 | 3 | ✓ |

Los 5 JSONs contienen **exactamente 3 repeticiones cada uno**, bajo la clave `repeticiones`
(array), con `n_reps=3` consistente. Las claves top-level son uniformes
(`id_falla, n_reps, repeticiones, run, voto`) y cada repetición tiene el mismo conjunto de 9
campos (`_meta, atribuciones, detectores, errores_formato, extraccion_traza,
formato_invalido, id_falla, razonamiento, run`). Ningún valor de contenido fue citado.

---

*Fin del expediente. Compilación solo-lectura; la adjudicación ocurre fuera de esta sesión.*
