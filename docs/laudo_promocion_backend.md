# Laudo A1.6 — Promoción del backend de retrieval (cierra issue #5)

Fecha: 2026-08-23 · Estado: **laudado**. Unidad del plan: A1.6 (`docs/plan_tesis.md`).
Antecedente: `docs/decision_backend_grafo.md` (2026-07-25) adoptó Neo4j Community con la
condición de que la promoción a backend por defecto se decidiera con el par
booleano-vs-BM25 medido sobre el mismo grafo. Ese par está medido. Este laudo lo cierra.

## 1. Evidencia sobre la que decido

Toda cifra sale de archivos commiteados; ningún número viene de memoria.

- **Backend inyectado con paridad verificada** (`9e131bf`, `data/experiment/neo4j/`):
  `Neo4jIndex` con modos `paridad` (réplica byte-idéntica del índice booleano in-memory) y
  `fulltext` (Lucene/BM25, analyzer `spanish`, campos label + descripción + id); paridad de
  `ver_nodo`/`ver_vecinos` **322/322** byte-idéntica sobre KG-Refinado (`26fac8b4`) y
  KG-Reextraído (`8e2eadee`); cargas con sha en `KG_Meta`; latencia de búsqueda
  ~3× menor que el booleano de paridad (`data/experiment/ablacion_retrieval/corrida/resultados/`,
  tasas por celda: `buscar_nodos` p50 0,012 s vs 0,033 s).
- **Tools v2** (`9141351`): `ver_vecinos` bidireccional elimina BKL-0027 del espacio de
  acciones por diseño; selftest 231/231; señal BM25 fuera del set sellado (CQN2-015 0/8 → 7/8).
- **Ablación pre-registrada** (`68c79dc`, corrida `ffc6ff6`; `analisis_ablacion.json`):
  factorial {booleano, BM25} × {tools v1, v2} sobre KG-Refinado, 400 trazas, 0 cross-hits,
  replay 400/400 con doble corrida byte-idéntica. Sobre el control C00 {booleano, v1}:
  - **P3 (no regresión) cumplida**: el recall vista literal no cambia (52/53 en ambos; IC de
    la diferencia [0; 0]) y el recall consultada literal **sube** 0,887 → 0,981
    (`dif_consultada_micro::literal::C10−C00` = **+0,094, IC95 [+0,019; +0,180]**, único
    efecto del experimento cuyo IC excluye el 0).
  - `hit_tool_limit`: 36 % (C00) → 29 % (C10, BM25) → 24 % (C11, BM25 + tools v2).
  - Abstenciones: 20 % (C00) → 11 % (C10).
  - **P2 no cumplida**: la brecha anti-léxica **no se cierra** (0,623 → 0,679; ningún IC
    anti-léxico excluye el 0). BM25 mejora **por ranking, no por cobertura** (mismas vistas;
    brecha vista-sin-consultar 6 → 1).
  - **P4 no cumplida**: las tools v2 no muestran efecto atribuible; el agente no paginó en
    ninguna de las 275 llamadas.
- **Gate de trazabilidad** (`docs/laudo_gate_trazabilidad.md`, R2): el banco de evaluación
  expone la **firma v1** de las tools.

## 2. Decisión

1. **BM25 (Neo4j full-text, modo `fulltext` de `Neo4jIndex`) pasa a ser el retriever por
   defecto de la app y del escalado.** Fundamento: mejora medida y con IC en lo literal, menos
   agotamiento de presupuesto, menos abstenciones, más rápido, y **cero regresión** respecto
   del índice booleano. Configuración que se promueve: la sellada en el pre-registro de la
   ablación (`data/experiment/ablacion_retrieval/preregistro_ablacion.md` §2: analyzer,
   campos con `id_texto`, ranking `score DESC, size(label) ASC, id ASC`, score no expuesto,
   `tokens_matcheados` con la fórmula del harness).
2. **Tools v2 NO se promueven como default.** El efecto no es atribuible y el banco de
   evaluación expone la firma v1 (R2). La bidireccionalidad de `ver_vecinos` queda como
   capacidad disponible del backend (`data/experiment/agente_v2/`) para la app y para
   experimentos con pre-registro propio; no entra en ninguna medición sin ser declarada como
   variable.
3. **Lo que este laudo NO afirma**: que BM25 resuelva la brecha anti-léxica. La evidencia
   dice lo contrario, y el bake-off de embeddings (`docs/decision_modelo_embeddings.md`)
   confirma que tampoco un retriever denso la cierra solo. El cuello de botella está en la
   política de selección del agente (13 de 20 fallas anti-léxicas son "vista y no abierta")
   y su tratamiento es A1.7 y B1.9/B1.10, no este laudo.

## 3. Alcance y consecuencias

- **App** (`app/main.py`): el agente de la app pasa a `GraphAgentNeo4j` con `modo='fulltext'`
  como default, manteniendo el `GraphIndex` in-memory como fallback declarado. Es una
  edición de la app, no del cuarteto congelado; se hace por subclase, como ya está construido.
- **Escalado** (B5/B6): Neo4j es el backend del corpus completo; el índice booleano
  in-memory no se usa a escala.
- **Mediciones selladas**: nada de lo medido con el índice booleano se re-corre. Los
  resultados con BM25 se **agregan**, nunca sustituyen (principio 8 del plan).
- **Issue #5**: se cierra con este laudo como entregable. Criterio de cierre cumplido:
  carga verificada, adaptador con paridad, benchmark de latencia y decisión de promoción
  escrita.

## 4. Regla que no cambia

Cualquier cambio posterior de configuración del retriever (campos, analyzer, top-K, modo
híbrido léxico + denso) es una variable de pre-registro medida con material propio; no se
ajusta mirando el set de evaluación sellado (principio 7).
