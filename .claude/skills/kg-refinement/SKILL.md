---
name: kg-refinement
description: Pipeline repetible de 5 pasos para refinar de forma iterativa y basada en evidencia el grafo de conocimiento regulatorio ganador (run_3) de la tesis BCRA — detecta dónde falla el sistema KG-RAG, atribuye la causa sin sesgo (grafo vs agente), propone cambios anclados en el PDF, los aplica sobre una copia y demuestra mejora medible side-by-side contra el baseline. Usá esta skill SIEMPRE que el trabajo sea de la fase de refinamiento — Fase 2.5; docs previos la llamaban erróneamente "Fase 2.4" (2.4 es el verificador) —: refinar/mejorar run_3, diagnosticar por qué falla una pregunta del eval set, atribuir una falla a grafo o agente, proponer o aplicar cambios al grafo ganador, correr trazas para análisis de fallas, o demostrar que un cambio mejoró el sistema sin introducir regresiones. Disparala aunque el usuario no diga "refinamiento" — si habla de arreglar run_3, de por qué el RAG falla una CQ, o de comparar grafo antes/después, es esto.
---

# Refinamiento del grafo (Fase 2.5)

Pipeline repetible para **refinar el grafo ganador `run_3`** de forma iterativa y basada en evidencia: detectar dónde falla el sistema KG-RAG, atribuir la causa sin sesgo, proponer cambios concretos, aplicarlos y demostrar mejora medible sobre el mismo dataset.

**Por qué como skill y no como script suelto:** congela "el camino bueno" para que el agente no lo redescubra cada vez. El ciclo se corre muchas veces; empaquetarlo como skill lo hace barato, estable y confiable, en lugar de un loop agéntico que improvisa el método en cada corrida.

**Dónde encaja:** Fase 2.5 de la tesis (en los informes de la autora, 2.4 es el verificador — `verificador.py` —, no el refinamiento). La Fase 2.3 ya eligió a `run_3` comparando los 5 grafos — esa selección está cerrada y no se reabre acá. Esta skill trabaja **solo sobre `run_3`** (con la única extensión transitoria de abajo para entradas del backlog sobre `grafo_v2`); los otros 4 grafos del experimento quedan congelados.

**Punto de entrada del trabajo:** las entradas en estado **`triaged`** de `data/backlog/backlog.jsonl` (contrato de datos y frontera de skills en `docs/spec_backlog_refinamiento.md`, §2 y §4). Cada entrada porta fuente, `diagnostico` (jerarquía de confianza), `especie`, evidencia por punteros y la `verificacion` declarada; esta skill las consume para proponer (Paso 4), aplicar y demostrar (Paso 5). El ciclo dataset-completo (Pasos 1→3 sobre el eval set) sigue vigente como circuito de **detección** de fallas nuevas que el backlog aún no registra — sus fallas atribuidas alimentan el backlog, no lo puentean. Qué entradas pasan (o no) por el Paso 3 lo fija la regla anti-re-atribución del Paso 3.

**Restricción transitoria (alcance por grafo):** sobre `grafo_v2` esta skill consume **únicamente** entradas con `diagnostico: adjudicado_humano`, hasta que exista el aparato espejo de v2 — vara/casos-control propios de ese esquema y su re-calibración, pre-requisito registrado en la spec, §7 —. La copia de trabajo `run_3_refinamiento/`, la calibración del Paso 3 y el baseline del Paso 5 son run_3-específicos; nada de eso se reutiliza sobre v2 sin ese aparato.

## Principio de diseño rector

Se fija duro **solo** lo que rompe el método si se hace distinto; todo lo demás se da como default razonado y se devuelve el criterio al agente. Para cada instrucción, la pregunta es: *¿esto invalida el resultado si se hace distinto?* Si sí → es fijo, y abajo está el porqué. Si no → es criterio del agente. Cuando un paso marca algo como **fijo**, no es una orden seca: viene con su razón, para que entiendas qué se rompería al desviarte y puedas ejercer buen juicio en todo lo demás.

## Cuándo se detiene la skill (y no improvisa)

Tres puntos de parada dura, porque seguir de largo invalidaría el resultado:
- **Paso 1:** si no hay un dataset apto, se detiene y lo señala — no inventa preguntas.
- **Paso 3:** si la calibración contra los casos-control falla, se detiene para revisión — no escala una atribución no validada.
- **Paso 4:** ante la duda sobre el riesgo de un cambio, va a revisión humana — no lo aplica automático.

En esos tres casos, parar y reportar **es** el comportamiento correcto, no una falla.

---

## Invariantes globales (valen para todos los pasos)

- **El original nunca se toca.** Todo el refinamiento trabaja sobre una copia (`run_3_refinamiento/`). El `run_3` original queda intacto como baseline inmutable del Paso 5. Esto es lo único que permite afirmar, al final, que la mejora se debe al refinamiento y no a otra cosa: sin un baseline congelado no hay con qué comparar.
- **NO commits** — los maneja la autora. No corras `git commit`/`git push`.
- **Reportes verificables:** rutas y números exactos provenientes de parseo real, nunca estimaciones. Si no parseaste el dato, no lo afirmes.
- **Validar antes de escalar:** calibrar contra juicio humano antes de confiar en una salida a escala. Es el patrón consistente del proyecto y la razón de ser de la calibración del Paso 3.

## Aislamiento por subagentes (convención transversal a los Pasos 2 y 3)

Dos usos distintos de subagentes, ambos por anti-sesgo, no por paralelismo:
- **Paso 2 — agente RAG como usuario puro:** cada query la responde un subagente que solo ve la query y las herramientas del grafo — nada del experimento, del código, ni del objetivo de refinamiento. Así la traza refleja cómo respondería un usuario real, no un agente que "sabe" que está siendo evaluado.
- **Paso 3 — verificador aislado por falla:** cada falla la investiga un subagente que arranca limpio, sin contexto de las otras fallas ni del objetivo de refinamiento.

Esto cuesta más (no se reusa trabajo entre fallas) y es un trade-off deliberado: **aislamiento por encima de eficiencia**, porque acá la validez de la atribución importa más que el costo. Una corrida futura **no debe** "optimizar" compartiendo contexto entre subagentes — rompería el anti-sesgo que justifica todo el Paso 3.

---

## PASO 1 — Conseguir y validar el dataset

**Qué hace:** verifica que existe un dataset de queries difícil y apto, y lo carga. **NO lo genera.**

**Insumo concreto actual:** `data/experiment/evaluacion/queries/eval_set_v2.json` (31 preguntas, generado a ciegas, con margen de mejora conocido en `multi_norma` y cadenas de restricción/excepción).

**Fijo (y por qué):**
- **El dataset no lo genera el agente que refina**, ni ningún agente con acceso a los grafos. Si quien refina escribe las preguntas, el refinamiento es trivial: se "examina" con preguntas que él ya sabe resolver. El dataset se genera a ciegas contra los PDFs, en un proceso aparte. (Regla dura del diseño del proyecto.)
- **El dataset debe ser difícil y no saturado.** Si el sistema ya acierta casi todo, no hay margen para demostrar mejora. Verificá que haya suficiente proporción de fallas reales antes de seguir.
- **El mismo dataset se usa en el Paso 5 para demostrar.** No se cambia de dataset entre diagnóstico y demostración — sería comparar peras con manzanas.

**Criterio del agente:** casi nada — es verificación. Confirmá que el dataset existe, cumple los requisitos y reportá su composición (tipos, cantidad, distribución). **Si no hay dataset apto, detenete y señalalo — no improvises uno.**

---

## PASO 2 — Generar las trazas

**Qué hace:** corre cada query del dataset con el agente RAG sobre la **copia de trabajo** del grafo, guardando la traza completa. Reutiliza la infraestructura existente (`runners/run_posthoc.py` + `llm_cache.py`).

> **Prerrequisito:** si `data/experiment/run_3_refinamiento/` no existe todavía, leé `references/preparar-run3-refinamiento.md` y creala con ese procedimiento (requiere aprobación de la autora para el cableado del loader). Sin la copia, este paso no puede correr.

**Fijo (y por qué):**
- **Se corre sobre la copia (`run_3_refinamiento`), no el original.** Coherente con el invariante del baseline intacto.
- **Se guarda la traza COMPLETA, no solo la respuesta final.** El Paso 3 necesita la trayectoria entera (qué nodos consultó, cómo razonó) para atribuir sin sesgo. Sin traza completa, el Paso 3 no puede investigar.
- **Mismas condiciones que el baseline** (mismo modelo, misma config). Para que la comparación del Paso 5 sea justa: la única variable es el grafo.
- **Usa la caché.** No re-paga lo ya corrido.
- **Agente RAG como usuario puro** (ver "Aislamiento por subagentes" arriba).

**Criterio del agente:** prácticamente nada — ejecución mecánica con la infraestructura existente. Lanzá las corridas y confirmá que se completaron sin truncamientos ni fallos.

---

## PASO 3 — Analizar trazas y atribuir la causa (el corazón del método)

**Qué hace:** identifica dónde falló el sistema y atribuye cada falla a su causa (grafo / navegación del agente / generación del agente / sin_defecto / abstención `frontera_no_determinada`), **recolectando evidencia ANTES de concluir**, dentro de una taxonomía cerrada. Antes de analizar todo el dataset, **se calibra** contra casos-control con atribución humana conocida; solo escala si la calibración pasa.

**Regla anti-re-atribución (entradas del backlog):** una entrada con `diagnostico` distinto de `sin_diagnostico` (`adjudicado_humano`, `verificador_validado`, `verificador_exploratorio`) **NO pasa por este paso**: su atribución ya fue laudada por un humano o emitida por el circuito de intake, y se respeta — re-atribuir desde cero duplicaría ese trabajo y arriesga atribuciones en conflicto entre la entrada y este paso. Para el anclaje del Paso 4, la atribución que porta la entrada vale como atribución del Paso 3. Este paso queda reservado para las fallas nuevas del ciclo dataset-completo y para las entradas `sin_diagnostico`.

> Leé `references/taxonomia.md` para la taxonomía cerrada de causas y las herramientas del verificador.
> Leé `references/casos_control.md` para las preguntas-control y su atribución humana (sub-fase A).

### Sub-fase A — Calibración (OBLIGATORIA, antes de escalar)
- El agente corre su análisis sobre las preguntas-control con atribución humana ya documentada: **CQ-031, CQ-034, CQ-017, CQ-020, CQ-025** (detalle en `references/casos_control.md`).
- Se compara su atribución con la humana.
- Si coincide en el umbral aceptable → procede a la sub-fase B. Si no → **se detiene para revisión** y reporta la discrepancia. No se escala con calibración fallida.
- **Umbral:** parámetro a afinar (sugerido ≥4 de 5). CQ-025 es el caso "fuera de corpus", especial; puede tratarse aparte al fijar el umbral. El umbral exacto lo decide la autora — ver `references/casos_control.md`.

### Sub-fase B — Análisis a escala (solo si la calibración pasó)
Para cada pregunta fallida, flujo **evidencia → conclusión**:
1. Parte del síntoma ("esta respuesta falló"), **sin asumir dónde está el problema**.
2. Recolecta evidencia con las herramientas que decidas: qué afirmó el agente, qué nodos consultó, qué dice el PDF, qué nodos relevantes existían que no usó.
3. Con la evidencia junta, concluye: ¿el dato estaba en el grafo? ¿el agente lo encontró? ¿el nodo era fiel al PDF?
4. Atribuye dentro de la taxonomía cerrada, citando la evidencia con **anclaje textual** (cada pieza es `{quote verbatim, ubicacion}`). Una falla puede tener **una o más causas**: si es mixta, marcá la primaria (la que mueve el veredicto) y la(s) secundaria(s), cada una con sus tres piezas de evidencia. Si tras investigar a fondo la evidencia no alcanza para decidir entre dos categorías, la salida correcta es la abstención `frontera_no_determinada` — con constancia de búsqueda (campo `busquedas`) y qué evidencia faltante decidiría el caso (ver `references/taxonomia.md`).

El verificador trabaja en fases (v4): EXTRACCIÓN de la traza (su output va al campo `extraccion_traza` del contrato, que consume el reporte HTML) → INVESTIGACIÓN por pata → ATRIBUCIÓN anclada. Detalle en `references/taxonomia.md`.

**Fijo (y por qué):**
- **Arranca desde la pregunta fallida, NO desde el nodo.** Evita el sesgo de atribución hacia el grafo (riesgo señalado explícitamente en el diseño: si se parte queriendo culpar al grafo, la atribución nace sesgada). Empezar mirando el nodo predispone a culpar al grafo.
- **Recolecta evidencia ANTES de concluir; no forma hipótesis de entrada.** Evita el sesgo de confirmación: si arranca con "es el grafo", busca solo lo que lo confirma.
- **Toda atribución va con sus tres piezas de evidencia citadas** (afirmación / nodo / fuente), cada una **anclada textualmente** (`{quote verbatim, ubicacion}`): si no se puede citar el lugar exacto donde se rompe el circuito, no hay evidencia suficiente para esa etiqueta. La atribución es verificable, no una opinión del agente.
- **Taxonomía CERRADA.** Para poder agregar y comparar resultados entre corridas. No inventes categorías nuevas; si algo no entra, eso mismo es un hallazgo a reportar.
- **La calibración es obligatoria y BLOQUEA el escalado si falla.** Nunca se confía en atribución no validada, ni en corridas futuras que nadie supervisa de cerca. La skill se auto-valida en cada corrida.
- **Verificador aislado por falla** (ver "Aislamiento por subagentes" arriba). El aislamiento entre fallas es lo que hace cada atribución independiente; no lo desactives.

**Criterio del agente:**
- Cuánto investigar cada caso (cuántas consultas, cuándo concluir que ya hay evidencia suficiente).
- Qué herramientas usar y en qué orden.
- Qué hipótesis perseguir si la evidencia inicial no alcanza.

---

## PASO 4 — Proponer cambios (híbrido por riesgo)

**Qué hace:** toma las fallas atribuidas del Paso 3 y, para cada una, propone un cambio concreto, eligiendo la palanca y clasificando el riesgo. Los cambios de bajo riesgo se aplican solos (anclados en PDF); los de alto riesgo se frenan para revisión humana.

> Leé `references/formato_propuesta.md` para el schema estructurado que debe tener cada propuesta (lo consume el Paso 5).

**Las tres palancas (elegís según el defecto):**
- **Grafo/esquema:** poblar un nodo vacío, completar una extracción, crear una arista, corregir provenance.
- **Prompt del agente RAG:** ajustar la instrucción (ej. para la generación-de-más).
- **Corpus:** señalar que falta un TO. **No modifica el grafo** — se reporta como límite. No se inventa regulación faltante.

**Enrutamiento por riesgo (el criterio que separa automático de revisión):**
- **Bajo riesgo → automático:** transcripción de un dato verificable contra un pasaje **único e inequívoco** del PDF, sin decisión de modelado ni interpretación. Ej.: poblar el nodo stub de CQ-031 con la enumeración del PDF; completar el límite de CQ-034.
- **Alto riesgo → revisión humana:** creación de estructura nueva (aristas, tipos), cambios de prompt del agente, datos con ambigüedad o excepciones, o cualquier cosa que requiera juicio de dominio regulatorio. Ej.: la arista cross-documento de CQ-017; el ajuste de prompt de CQ-020.

**Fijo (y por qué):**
- **La clasificación de riesgo usa el criterio explícito** (transcripción-verificable vs decisión-de-modelado/interpretación). Para que sea consistente entre corridas, no al humor del agente.
- **Ante la duda, un cambio va a revisión, no a automático.** El default seguro es pedir aprobación; lo automático es la excepción justificada.
- **Todo cambio automático va anclado en cita textual del PDF, NO en la respuesta esperada.** Este es el **candado anti-entrenar-contra-el-test**. El criterio de un cambio válido es "lo dice el PDF", nunca "hace pasar la pregunta". Sin esto, el pipeline metería datos que hacen acertar el test sin fundamento real — el propio "grounded ≠ correct" que la tesis denuncia.
- **Toda propuesta se ancla en una falla atribuida del Paso 3.** No se proponen cambios por intuición; cada cambio rastrea a un defecto con evidencia. Evita "mejorar" lo que no estaba roto.
- **El formato de cada propuesta es estructurado y fijo** (defecto / palanca / cambio exacto / cita PDF / cómo se verificaría / categoría de riesgo). El Paso 5 lo consume; si el formato varía, no se puede aplicar de forma confiable. Ver `references/formato_propuesta.md`.
- **Los cambios automáticos dejan un registro auditable** (qué cambió, en qué nodo, anclado en qué cita). Para que la revisión humana final sea un chequeo liviano, no una auditoría a ciegas del grafo entero.

**Criterio del agente:**
- Qué cambio específico propone para cada defecto.
- En qué categoría de riesgo cae (aplicando el criterio fijo).
- Cómo prioriza si hay muchos defectos (cuáles de alto impacto).

---

## PASO 5 — Aplicar y demostrar mejora

**Qué hace:** aplica los cambios aprobados sobre la copia, re-corre el dataset **completo** sobre el grafo refinado en las mismas condiciones que el baseline, y produce una comparación lado a lado que separa mejoras de regresiones.

**El flujo:**
1. Confirma que los cambios (automáticos + aprobados por el humano) están aplicados sobre la copia.
2. Re-corre el dataset **completo** sobre la copia refinada, en las **mismas condiciones exactas** que el baseline.
3. Compara contra el baseline (`run_3` original, mismas condiciones) pregunta por pregunta.
4. Reporta separando: preguntas que **MEJORARON** (fallaban→aciertan), que **EMPEORARON** (acertaban→fallan = regresiones), y **SIN CAMBIO**.
5. Veredicto neto: ¿el refinamiento mejoró el sistema en conjunto?

**Fijo (y por qué):**
- **El baseline es `run_3` ORIGINAL en las MISMAS condiciones exactas que el refinado.** La única variable que cambia es el grafo; si no, no se puede atribuir la mejora al refinamiento.
- **Se re-corre el dataset COMPLETO, no solo las preguntas refinadas.** Para cazar regresiones escondidas: un cambio puede arreglar una pregunta y romper otra (sobre todo los de prompt). Reportar solo las arregladas es engañarse.
- **El reporte separa mejoras de regresiones explícitamente.** El resultado honesto es el NETO, no el conteo de aciertos nuevos.
- **Caché por namespace separado** (baseline vs refinado tienen `graph_fingerprint` distinto). No se contamina una corrida con resultados de la otra. (Ya lo maneja `llm_cache`.)

**Criterio del agente:**
- Cómo presenta la comparación (visualización, orden).
- Qué análisis adicional ofrece si aparecen regresiones.

**Parámetro N (repeticiones por pregunta) — con regla de decisión:**
- **Default N=1** para el desarrollo iterativo (explorás hipótesis, no concluís).
- **N=3 con veredicto modal** para reportar un resultado como conclusión (mentores, tesis, cualquier afirmación de mejora que defiendas).
- **Regla:** si la mejora medida es del tamaño del ruido conocido del juez o menor (≈1–2 preguntas), subí a N=3 antes de afirmar que funcionó. Si la mejora es grande y clara (varias preguntas), N=1 ya alcanza como evidencia para iterar.
- El parámetro **tiene dueño** (la autora lo setea según la fase) y **regla** (esta). No lo improvisa el agente. La decisión de N para el reporte de tesis está ligada a la pregunta abierta de N=3 sin caché de la Fase 2.3, pendiente con los mentores.

---

## Las salvaguardas, en una vista (lo que hace defendible al pipeline)

Estas decisiones están tomadas; la skill las ejecuta, no las rediscute.

1. **Anti-sesgo de atribución** (Paso 3): arranca del síntoma, evidencia antes que hipótesis.
2. **Auto-validación** (Paso 3): calibración obligatoria contra casos-control antes de escalar.
3. **Anti-entrenar-contra-el-test** (Paso 4): cambios anclados en el PDF, no en la respuesta esperada.
4. **Control humano donde importa** (Paso 4): híbrido por riesgo; modelado/interpretación → revisión.
5. **Anti-regresiones escondidas** (Paso 5): se re-corre el dataset completo, se separan mejoras de regresiones.
6. **Anti-ruido del juez** (Paso 5): N configurable con regla de decisión.
7. **Dataset íntegro** (Paso 1): ciego, difícil, no generado por quien refina.
8. **Baseline inmutable** (invariante): el original nunca se toca, siempre se compara contra él.
9. **Aislamiento por subagentes** (Pasos 2 y 3): el agente RAG responde como usuario puro; cada falla se investiga con un subagente que arranca limpio, sin contaminación entre fallas.

---

## Archivos de referencia

Leelos cuando el paso correspondiente lo indique — no hace falta cargarlos de entrada.

- `references/preparar-run3-refinamiento.md` — creación de la copia de trabajo `run_3_refinamiento/` (una sola vez; cableado del loader con aprobación de la autora). **Paso 2, prerrequisito.** ⚠ Depende de una reference de otra skill: `.claude/skills/llm-capture/references/extender-run-files.md`.
- `references/taxonomia.md` — taxonomía cerrada de causas (defectos del grafo vs del agente) + herramientas del verificador. **Paso 3.**
- `references/casos_control.md` — las 5 preguntas-control con su atribución humana, para la calibración. **Paso 3, sub-fase A.**
- `references/formato_propuesta.md` — schema estructurado de una propuesta de cambio (lo consume el Paso 5). **Paso 4.**
