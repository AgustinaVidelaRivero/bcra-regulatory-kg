# Plan de cierre de la tesis — v1 (2026-08-17)

Plan vivo, por bloques y sub-tareas. Es el documento que gobierna la cola de unidades del
proyecto desde el 2026-08-17 (`docs/tablero.md` §5 lo referencia como cola vigente).
Horizonte: fin estimado del PF **octubre 2026** (`docs/ppf/main.tex:61`) → ~10 semanas
desde la fecha de la v1.

**Protocolo de actualización.** (i) Todo mandato de unidad cita este plan por id de
sub-tarea. (ii) Al frenar, la instancia entrega una *propuesta* de actualización
(checkboxes, commits, números, desvíos); nunca edita este archivo por su cuenta salvo
mandato explícito. (iii) La autora revisa, lauda y commitea plan + tablero en un mismo
commit al cierre de cada unidad o semana. (iv) Los cambios de forma (bloques nuevos,
recortes, reordenamientos) suben la versión del título y dejan una línea en el changelog
de abajo; los cambios de estado no. (v) La historia del plan es `git log -- docs/plan_tesis.md`.

Convenciones: `[ ]` pendiente · `[~]` en curso · `[x]` hecho (con commit) · `[–]` descartado
con laudo. Cada sub-tarea lleva: dueño (H = humana/autora, I = instancia ejecutora),
costo API estimado, dependencia, entregable sellado. Costos en USD.

Changelog: v1 (2026-08-17) — plan inicial con revisión de mesa (nomenclatura canónica,
laudos requeridos, principio 7, tarifas, cuello de botella de revisión, gate informativo de
intrínsecas, mapa de mecanismos con fuentes M-1…M-19, B2.6–B2.8) y cierres registrados de
U-A0, U-C0.1, U-A1.1, U-A1.2.

---

## 0. Punto de partida (verificado contra archivos al 2026-08-17, HEAD `64de678`)

**Resultado central ya obtenido — EV2 fidelidad (40 preguntas ciegas, 164 criterios, juez
validado 11/12 contra adjudicación humana, 98,1 % por criterio):**

Nombres canónicos de los grafos según `docs/nomenclatura_grafos.md` (commit `237fb8f`):
**KG-Base** (`12c226e2`; alias `run_3`, `run_3_ppf_core`, baseline de la Fase 2.3),
**KG-Refinado** (`26fac8b4`; alias `v3`, `reensamblado_v3`, vigente: esquema v2 + C1–C7),
**KG-Reextraído** (`8e2eadee`; alias `v2`, `corpus_v2`, "v2-reextraído": pipeline E0–E3, sin
parches). En este plan se usan solo esos nombres.

| grafo | correcto | parcial | incorrecto | criterios cubiertos (corrida base) | abstenciones (base) |
|---|---|---|---|---|---|
| KG-Base (baseline 2.3) | 3 | 20 | **17** | 58/164 = 35,4 % | 9/40 |
| KG-Refinado (vigente, esquema v2 + C1–C7) | 5 | 26 | 9 | 75/164 = 45,7 % | 4/40 |
| KG-Reextraído (pipeline E0–E3, sin parches) | 4 | 27 | 9 | 65/164 = 39,6 % | 7/40 |

Nota sobre la cobertura por criterios: la columna es la de la **corrida base** (58/75/65).
La cobertura **definitiva** (recomputada desde los veredictos definitivos, con la regla de
respuesta representativa por par) es **KG-Base 56/164 = 34,2 % · KG-Refinado 73/164 =
44,5 % · KG-Reextraído 70/164 = 42,7 %** (`data/experiment/ev2_reporte/reporte_ev2.md` §3,
commit `85d9fdb`). Ambas métricas quedan declaradas; en prosa se cita cuál se usa.

Lecturas: (i) ambos grafos del pipeline refinado (KG-Refinado y KG-Reextraído) reducen los
incorrectos casi a la mitad respecto del baseline KG-Base (9 y 9 contra 17); el esquema v2 es
el factor común de ambos;
(ii) el pipeline nuevo, **sin E4/E5 ni parches manuales** (E4/E5: definidos en
`docs/diseno_reextraccion_v2.md`, líneas 197–212 y 214–220, no ejecutados — verificación
cerrada en esta revisión), empata con KG-Refinado refinado a mano;
(iii) ni el mejor grafo cubre la mitad de lo que la norma dice → la palanca grande está en
cobertura + retrieval + agente, no en "más grafo".
Navegabilidad (recall consultada literal→anti-léxica): KG-Refinado 0.958→0.620, KG-Base
0.716→0.493, KG-Reextraído 0.396→0.271 (KG-Refinado juega de local: los pares se
muestrearon de KG-Refinado).
**Mapa causal de fallas (A0.2, determinístico, USD 0; fuente
`data/experiment/ev2_reporte/salida/atribucion_fallas.md`, commit `85d9fdb`):** el empate
9-9 esconde perfiles de falla distintos — KG-Refinado falla por navegación con ancla presente
(5/9), KG-Reextraído por granularidad de ancla (4/9, contenido en sub-puntos 3/4);
generación es la clase modal en los tres grafos (KG-Base 17 / KG-Refinado 25 /
KG-Reextraído 21: grounded ≠ correct cuantificado); techo de retrieval dimensionado
(alcanzabilidad + vista: 14 / 7 / 6).

**Promesas del PPF sin cumplir (fuente: `docs/ppf/main.tex`, `docs/literatura/gaps.md`,
`docs/defensa/`):** (a) gold standard de tripletas anotado a mano — declarado "no
negociable"; (b) caso de uso 1 explicabilidad agéntica — cero rastro en el repo;
(c) caso de uso 2 KG-RAG vs RAG tradicional — 4 baselines prometidos, ninguno corrido;
(d) latencia p50/p95 — no medida; (e) KG y eval set "públicos" — no publicados;
(f) versionado temporal — declarado trabajo futuro; (g) prosa de tesis — **cero**.
**Issues abiertos:** #5 Neo4j, #6 costos escalado (USD 200), #8/#9/#10 (cerrables: hechos),
#11 escalado (créditos AWS reservados), #12 KG-RAG vs RAG + aplicaciones.
**Documentación de estado atrasada:** `tablero.md` (07-08), `README.md` (julio),
`hallazgos_tesis.md` (07-06), `INDICE.md` sin lecturas nuevas.

---

## 1. Principios del plan (por qué este orden)

1. **Primero lo que responde la pregunta titular con lo que ya existe** (atribución de las
   fallas EV2, retrieval, baseline RAG); después lo que agranda el sistema (escalado).
2. **La escritura arranca ya y corre en paralelo siempre**: cada bloque termina con su
   sección redactada, no con "material para redactar".
3. **Nada nuevo sin pre-registro sellado**; nada se compara si no aísla una variable.
4. **Escalar recién cuando el pipeline sea generalizable y esté endurecido** (E4/E5,
   regression suite, prerrequisitos A1–A9); escalar es demostración de costo/throughput
   (vacío #5), no otra comparación.
5. **Descopes por laudo escrito**, nunca por omisión: caso de uso 1, GraphRAG-MS,
   versionado temporal, sin-gold, Graphiti.
6. **Tres carriles en paralelo** (A medición · B grafo/pipeline · C escritura/gobernanza),
   una unidad por instancia por sesión, directorios disjuntos, cero commits de instancia,
   paquete de revisión al frenar (reglas g/h de CLAUDE.md).
7. EV2 es examen, no set de desarrollo: cada sistema o configuración nueva se evalúa sobre
   EV2 UNA sola vez, con pre-registro sellado previo; ningún componente se ajusta mirando
   resultados de EV2 para volver a medirse en EV2. Las iteraciones de desarrollo usan
   material propio (pares sintéticos nuevos, preguntas frescas tipo U6), nunca el examen.

Tiers: **T1** = sin esto la tesis no cierra · **T2** = la hace mucho mejor · **T3** = si sobra.

---

## Carril A — Medición (secuencial: cada bloque alimenta al siguiente)

### A0 · Cierre formal de EV2 y atribución determinística de las fallas — T1 · S1
Objetivo: convertir los 120+198 veredictos en un mapa "¿falló el grafo, el retriever o el
agente?" sin pagar verificador, usando el replay determinístico que ya existe.
- [x] A0.1 (I, $0) **HECHA** — Reporte consolidado EV2 por eje × cohorte × grafo (fidelidad + navegabilidad + ausencias + costos totales, USD 35,62 recomputados desde archivos), cierre de issue #10. Entregable: `data/experiment/ev2_reporte/reporte_ev2.md` + recomputo determinístico, sellados en `40603a9`; §12 y texto de cierre de #10 actualizados en `85d9fdb`.
- [x] A0.2 (I, $0) **HECHA** — Atribución determinística de primer nivel: fase A (regla `regla_atribucion.md`, 4 clases con precedencia presente→consultada→vista, veredicto por traza de esa misma respuesta, abstención como columna cruzada, selftest 24/24) ratificada y sellada en `40603a9`; fase B sellada en `85d9fdb` (`salida/atribucion_fallas.{json,md}`, hallazgos H1–H7, replay 120/120 base + 191/191 §7, doble corrida byte-idéntica).
- [ ] A0.3 (H+I, ~$25) Muestra de 12 casos (4 por grafo, estratificados) al verificador v7' N=3 (validado en-familia grafo_v2 `2c7487bb`/KG-Refinado; en KG-Base exploratorio) + laudo humano → sub-especies (amputación, quimera, alucinación con retrieval perfecto…). Sirve de puente con la taxonomía y de calibración de A0.2. **Afinada por H5 (`85d9fdb`)**: el sub-diagnóstico prioriza los casos generación × abstención (nodo-ancla cáscara: el ancla fue consultada pero el nodo no porta el contenido) además de la muestra estratificada. **Gatillo laudado (cierre de A1.3):** se ejecuta junto con B2.7 (muestra compartida con el gate gen-3); descope declarado si aprieta el calendario: solo los casos generación × abstención de H5.
- [x] A0.4 (H) **CUMPLIDA** — la sensibilidad informativa por descendientes de la fase B de A0.2 (misma evidencia, commit `85d9fdb`: ausencia_kg total en KG-Base/KG-Refinado vs granularidad de ancla en KG-Reextraído) cubre el análisis de las 20 "ausencias" de KG-Reextraído; el sellado de navegabilidad no se modificó.
Depende de: nada. Habilita: A1 (qué debe arreglar el retriever), B1 (qué debe arreglar el grafo), C (Resultados).

### A1 · Neo4j: inyección + ablación de retrieval (issue #5) — T1 · S2–S3
Objetivo: separar "estructura del grafo" de "algoritmo de búsqueda/expresividad de tools".
Es lo que hace defendible cualquier resultado del head-to-head A2.
- [x] A1.1 (I, $0) **HECHA en `9e131bf`** — backend Neo4j con inyección por subclase y paridad verificada: `docker-compose` con Neo4j 5.26.9 pinneado + `requirements.txt`; KG-Refinado (`26fac8b4`) 4.469/8.073 y KG-Reextraído (`8e2eadee`) 6.178/11.415 cargados con sha en `KG_Meta`, idempotencia por huella; `Neo4jIndex` con modos `paridad`/`fulltext` + `GraphAgentNeo4j` (el cuarteto no se editó); selftest de paridad **322/322 byte-idénticos** sobre ambos grafos (BKL-0022/0027 como tests de respuesta conocida); latencia registrada; tabla qué-cambia/qué-no en `data/experiment/neo4j/README.md` §G. **NO inyectado en el pipeline de evaluación**; A1.2 (retriever BM25 + tools v2) queda como punto de extensión declarado. USD 0.
- [x] A1.2 (I, $0) **HECHA en `9141351` (+ `5078f51`)** — tools v2 sobre Neo4j como módulo aparte (`data/experiment/agente_v2/`, harness intacto): `buscar_nodos` BM25; `ver_vecinos` bidireccional/paginado (offset, techo `por_pagina` 40)/filtro por relación — BKL-0027 eliminado del espacio de acciones, BKL-0022 alcanzable en cualquier posición; `ver_nodo` adaptador byte-idéntico; `contexto_de` como punto de extensión; `GraphAgentV2` con `ask` verificado igual al harness salvo 2 sustituciones; selftest **231/231** con esperados derivados del `kg.json`, doble corrida byte-idéntica; señal BM25 medida fuera de EV2 (CQN2-015 0/8→7/8 en KG-Reextraído; BKL-0022 sin cambio — huérfano de label, no de algoritmo); principio 7 respetado. USD 0. **Laudos**: diff mínimo del prompt APROBADO como parte del factor tools; API=v1 / sin `direccion` / paginación offset / techo 40 ratificados; nota BKL-0022 aplicada al backlog en `5078f51` (desvío declarado: `9141351` la daba por aplicada y el append había fallado — corregido).
- [x] A1.3 (H+I, ~$2) **HECHA en `68c79dc`** — pre-registro sellado de la ablación (`data/experiment/ablacion_retrieval/preregistro_ablacion.md`): factorial 2×2 sobre KG-Refinado (`26fac8b4`), celdas selladas por sha, config de retriever congelada, factor "tools v2" como paquete {tools v2 + specs JSON + 2 líneas de prompt aprobadas}, predicciones **P1–P6 con umbrales**, tope de A1.4 = **USD 20**; **50 pares nuevos** con semilla `sinteticas-faseA-v3` (sin estrato E-C por colisión estructural con EV2 detectada sin abrir EV2; 11 huérfanos de label identificados ex ante para P6); generación USD 1,70. Desvíos declarados en el mensaje del commit. **Nota registrada** (`data/experiment/ablacion_retrieval/anexo_solapamiento_anclas.md`): 28/37 anclas compartidas con el eje sintético de EV2 por concentración del pool de 175 anclas; identidad de pares 0/100 — la concentración del pool es una **limitación estructural del corpus** que va a la Discusión (C1.7).
- [ ] A1.4 (I, ~$12) Corrida factorial sobre **KG-Refinado**: {booleano, BM25} × {tools actuales, tools v2}, N=1, réplica determinística de navegabilidad ($0) + latencia end-to-end por pregunta (p50/p95, de las trazas). Opcional: BM25+HNSW híbrido.
- [ ] A1.5 (I, ~$5) Fidelidad EV2 (40 preguntas) de KG-Refinado con la mejor configuración de retrieval → "KG-RAG en su mejor forma" para A2. Mismo juez, mismo mapping, adjudicación simétrica 10 %. **Rige el principio 7**: una sola medición sobre EV2, configuración elegida y sellada en A1.3/A1.4 sobre pares sintéticos nuevos, nunca ajustada mirando EV2.
- [ ] A1.6 (H) Laudo de promoción: ¿el índice BM25 pasa a ser el backend por defecto de la app y del escalado? Cerrar #5. **[LAUDO ESCRITO REQUERIDO — toca compromisos del PPF/alcance]**: no arranca sin laudo redactado y fechado por la autora.
Depende de: A0 (para leer resultados con la atribución). Riesgo: contenedor Docker en la máquina de corrida; mitigación: `SQLite FTS5` como plan B ya evaluado en `decision_backend_grafo.md`.

### A2 · Baseline RAG tradicional y head-to-head (issue #12, pregunta rectora) — T1 · S4–S5
- [ ] A2.1 (H+I) **Pre-registro sellado**: baseline BM25 sobre los **chunks de E0** (unidades estructurales + herencia; mismo texto que vio el extractor — el baseline no pierde por chunking tonto), top-k=5, mismo agente Haiku con una sola tool `buscar_pasajes`, mismo juez de fidelidad EV2, mismas 40 preguntas; brazo denso opcional (BGE-M3 local, chunks 512 como prometía `gaps.md`) si hay tiempo. GraphRAG-MS: **descartado con laudo** (costo, opacidad, fuera de criterio de citabilidad). Predicciones: incorrectos, criterios cubiertos, abstenciones, latencia, costo por pregunta.
- [ ] A2.2 (I, ~$15) Corrida N=1 + N=3 parciales + auditoría 10 % + adjudicación simétrica (mismo protocolo EV2). **Rige el principio 7**: el baseline se diseña y sella en A2.1 (con material propio para cualquier ajuste), y se mide sobre EV2 una sola vez.
- [ ] A2.3 (I, $0) Tabla head-to-head final: KG-Base · KG-Refinado · KG-Reextraído · KG-Refinado+BM25(+tools v2) · RAG-BM25 · (RAG-denso), con incorrectos, criterios cubiertos, abstenciones, latencia p50/p95, costo/pregunta, costo de construcción → **gráfico Pareto fidelidad-vs-costo** (vacío #5).
- [ ] A2.4 (H) Laudo de aplicaciones (issue #12): la app de consulta con citas + circuito de feedback **es** la aplicación demostrada (U6: 25 preguntas reales de usuarios). Caso de uso 1 (explicabilidad agéntica): **descope escrito** con justificación (priorización invertida respecto del PPF, registrada) o demo mínima de 3 cadenas sobre preguntas multi-norma de EV2 sin métrica nueva. Recomendación: descope + demo mínima solo si A1–A2 cierran en fecha. **[LAUDO ESCRITO REQUERIDO — toca compromisos del PPF/alcance]**: no arranca sin laudo redactado y fechado por la autora.
Depende de: A1.5. Habilita: C (Resultados/Discusión).

### A3 · Ablación de modelo del agente — T2 · S6
- [ ] A3.1 (I, ~$10) Sonnet como respondedor sobre KG-Refinado+BM25, mismas 40 preguntas: ¿persiste "grounded ≠ correct" (BKL-0026 3/3 con retrieval perfecto)? Si persiste, es del paradigma, no del modelo chico. Pre-registrado.

---

## Carril B — Grafo y pipeline (paralelo al carril A)

### B1 · Terminar el pipeline: E4/E5 + referencias cruzadas + provenance rica — T1 · S1–S3
Objetivo: que el pipeline nuevo sea completo, generalizable y produzca un grafo que pueda
promoverse a vigente. Todo código puro salvo lo marcado.
- [ ] B1.1 (I, $0) **E5 esqueleto**: portar `build_skeleton` de `grafo_v2/code/assemble.py` a `ensamblar_corpus.py` (clases + roles por TO, `subclase_de`/`miembro_de`/`instancia_de`), aristas `padre_sugerido` flaggeadas para propuestos. Hoy: 0 aristas de esqueleto.
- [ ] B1.2 (I, $0) **E4 determinístico**: resolución de `sujeto_propuesto` por alias normalizado contra el catálogo (`resuelto_por_alias`), filtro de ruido en conflictos de properties (`materia`/`version`), `TextoOrdenado` solo desde provenance (hoy 6 para 5 TOs). Los ~170 conflictos reales quedan registrados para E4-LLM (T3).
- [ ] B1.3 (I, $0) **Referencias cruzadas norma→norma** como aristas `referencia` (regex sobre "punto X.Y de las normas sobre Z" + resolución contra inventario de TOs y puntos de E0). Hoy: 0 aristas norma→norma, 113 nodos que remiten en texto. Habilita multi-hop real (debilidad compartida de la Fase 2.3) y es la capacidad que un RAG por chunks no tiene.
- [ ] B1.4 (I, $0) **Provenance rica**: `chunk_id`, `paginas`, `ancestros` en cada provenance (arregla la asimetría de granularidad de KG-Reextraído en censos por ancla).
- [ ] B1.5 (I, $0) `ensamblar_corpus.py`: selftest + aserciones de invariantes (conservación, unicidad, sin colgantes, provenance) + guarda de merge cross-TO (solo `Sujeto` de catálogo; el resto a registro/adjudicación — hoy 5 merges de contenido silenciosos).
- [ ] B1.6 (I, $0) Cola humana **ingresa flaggeada** (`estado_e3`) en vez de perderse (80 unidades; incluye `ext::3.9::intro`); guardia B extendida a cualquier tipo + guardia "cita = label" (recomputo sobre veredictos pagados, precedente `recompute_politica_enm01.py`).
- [ ] B1.7 (I, $0) Re-ensamblar → **KG-Reextraído-r1** (mismos crudos de E1/E3, sin API), tests de respuesta conocida ampliados (ver B2), sha sellado. Es la primera release que llega al gate de B2.6: hasta el laudo B3.1 las intrínsecas se computan y reportan en modo INFORMATIVO, no bloquean.
- [ ] B1.8 (I, ~$3) Fidelidad EV2 de KG-Reextraído-r1 (40 preguntas, mismo protocolo) → ¿supera a KG-Refinado? Laudo de promoción a vigente (`app/main.py` `GRAFOS_EXPLICITOS`). **Rige el principio 7**: KG-Reextraído-r1 se mide sobre EV2 una sola vez; B1.1–B1.7 se validan con regression suite y material propio (B2), nunca contra resultados de EV2.
Depende de: nada. Paralelizable con A0/A1 (directorios disjuntos).

### B2 · Refinamiento generalizable: del parche manual a la regression suite — T1 · S2–S3
Objetivo: que "refinar" signifique arreglar el pipeline y re-correr, no editar el grafo.
- [ ] B2.1 (I, $0) `scripts/regression_kg.py`: convierte cada BKL cerrado (C1–C7, BKL-0024/0025, RT-*) y los tests T1–T3 en **tests de respuesta conocida determinísticos** ejecutables sobre cualquier `kg.json` (nodo presente / ancla / valor / arista / rank en `buscar_nodos`). Salida: tabla defecto → resuelto/persiste — **entregable transferido explícitamente desde el issue #9 (cerrado en U-C0.1) a esta sub-tarea**.
- [ ] B2.2 (I, $0) `scripts/shapes_validator.py` a esquema v2 (unidad 2 del tablero, pendiente desde julio): shapes de dominio/rango, provenance obligatoria, sujeto en catálogo o cuarentena.
- [ ] B2.3 (I, $0) Correr regression + shapes sobre KG-Base, KG-Refinado, KG-Reextraído, KG-Reextraído-r1 → tabla en Resultados.
- [ ] B2.4 (H) Laudo de los 15 BKL `triaged`: 9 son de asignación de sujeto (descenso/estrechamiento/clase forzada) → **una** corrección sistemática vía prompt/validador de E1 (no vía edición del grafo), verificada por B2.1; 4 de alcanzabilidad → A1; 2 de modelado (BKL-0020/0021) → laudo; BKL-0018 → anotación de régimen.
- [ ] B2.5 (I) Actualizar `docs/spec_backlog_refinamiento.md`: el circuito pasa a tener dos vías (parche sellado sobre vigente / corrección en pipeline + re-extracción + regression) y cuándo se usa cada una. Campo nuevo obligatorio en cada entrada: `capa_pipeline` ∈ {E0, E1-prompt, E1-validador, catálogo, E2, E3, ensamblado, retriever, agente} — la entrada nombra la REGLA a corregir, no el nodo.
- [ ] B2.6 (I+H, $0) **Protocolo del ciclo de refinamiento a nivel pipeline ("releases")** — `docs/protocolo_ciclo_refinamiento.md`: síntoma (regression fallida / 👎 app / pregunta fresca / intrínseca fuera de umbral) → atribución (determinística de primer nivel A0.2; verificador solo sobre muestra priorizada) → entrada de backlog con `capa_pipeline` + test nuevo en la regression suite → cambio en el pipeline → re-corrida cache-aware (E0/E2/ensamblado $0; E1/E3 pagan solo si rota el prefijo → los cambios de prompt/catálogo se agrupan en releases) → **gate de release** = regression suite + shapes v2 + intrínsecas con umbrales (B3) + material propio (pares sintéticos con semilla nueva, preguntas frescas tipo U6) — nunca EV2 (principio 7). Hasta el laudo B3.1, las intrínsecas participan del gate en modo INFORMATIVO (se computan y reportan en cada release, no bloquean); pasan a bloqueantes recién con umbrales laudados → laudo → grafo versionado (KG-Reextraído-r2, r3…) con sha, tabla regression, intrínsecas y costo → promoción a vigente / carga en Neo4j. Doble vía explícita: el **hotfix** sellado sobre el vigente sigue existiendo (la app no espera una re-extracción), pero nace con su test en la regression suite, así la próxima release lo resuelve por diseño o falla el gate. Declara qué NO escala (adjudicación humana de veredictos, gold, verificador fuera de familia) y cómo se acota (muestras priorizadas por frecuencia de síntoma y territorio).
- [ ] B2.7 (H+I, ~$25) **Gate chico del verificador en la familia gen-3** (KG-Reextraído / KG-Reextraído-r1): 4 casos con vara sellada, criterio cero-silenciosos + ≥3/4 (mismo protocolo que U5, `docs/protocolo_gate_u5.md`). Sin esto el Motor 3 no puede diagnosticar sobre el grafo que va a ser el vigente. Se combina con A0.3 (misma muestra) para no pagar dos veces.
- [ ] B2.8 (I, $0) **`docs/metodo_construccion_refinamiento_kg.md`** — el método completo, de PDF a grafo vigente y su mantenimiento, escrito como especificación reutilizable (entradas, etapas E0–E5, gates, regression, releases, retriever, intake, roles humano/máquina, costos por etapa) con puntero al experimento que demuestra cada mecanismo (§6 de este plan). Es el documento que la tesis convierte en capítulo de Metodología y el que se sigue en B6.

### B3 · Métricas intrínsecas pasada 2 (spec §8) — T2 · S3
- [ ] B3.1 (H) Laudo de umbrales de M2/M3/M7/M10 (bloqueantes) — sobre la evidencia de la pasada 1.
- [ ] B3.2 (I, $0) Correr M1–M11 sobre KG-Base, KG-Refinado (post-C7), KG-Reextraído y KG-Reextraído-r1; M11 (cobertura CQ) sobre las anclas de EV2 (régimen especial: medición única, no bloqueante). Alias de industria (compression ratio / false merge rate) como columnas.
- [ ] B3.3 (I, $0) Propuesta pre-registrada de **M12 densidad de referencias cruzadas** y **M13 completitud de provenance** (aditivas a la spec, con laudo).
- [ ] B3.4 (I) Cruce intrínseco ↔ extrínseco (EV2): ¿alguna métrica intrínseca predice fidelidad? Tabla + hallazgo (probablemente "no, y eso es el punto": P-b).

### B4 · Gold standard de tripletas (promesa "no negociable" del PPF) — T1 · S2–S4
Objetivo mínimo defendible: precisión/recall de extracción a nivel tripleta sobre una
muestra estratificada, con protocolo ciego. Es humano-intensivo; acotar.
- [ ] B4.1 (H+I) Diseño sellado: 5 unidades de E0 por TO (25 unidades, ~1.100 chars mediana), muestreo con semilla, anotación **por instancia ciega** de tripletas gold (tipo, label, relación, sujeto, provenance) + revisión de la autora (mismo patrón que criterios U6, Laudos A–D); regla de matching (exacto tras normalización / parcial por juez humano).
- [ ] B4.2 (H) Anotación + revisión (~200–300 tripletas). Sellado por commit.
- [ ] B4.3 (I, $0) P/R por grafo (KG-Base, KG-Refinado, KG-Reextraído, KG-Reextraído-r1) y por tipo; cruce con EV2 y con M1–M3. Publicable como dataset (B7).
Si el tiempo no da: laudo escrito de reducción de alcance (3 unidades × 5 TOs) — nunca silencio.

### B5 · Escalado: endurecimiento y prerrequisitos (issue #6, #11) — T2 · S4–S5
- [ ] B5.1 (I, $0) A1: parametrizar runner/E2/ensamblado por manifiesto (hoy cableado a 5 TOs; `censo_oraculo[to]` → KeyError; `LIMITACIONES_E0` hardcodeado; `ROL_POR_TO` con 5 keys); modo E2 sin oráculo.
- [ ] B5.2 (I, $0) A3: regex de E0 (`Sección N[.:]`, `Índice` sin guiones con guarda) → paridad 5/5 byte a byte + selftest 57/57 obligatorios; health-check por TO (`(cid:NN)`, páginas sin Sección).
- [ ] B5.3 (I, $0) A4/A5: `max_tokens` con reintento 16k→32k en el mismo pase; sub-chunking por ítems para TOs nuevos; no cerrar fase con errores reintentables; tope compartido entre clientes.
- [ ] B5.4 (H+I) **Catálogo de sujetos v3** congelado (SNP: entidad girada/depositaria/receptora/originante; bancos centrales, FMI, BIS, CCP; rol de alcance por TO nuevo) → rota el prefijo cacheado de E1 (aceptado). A2 de la auditoría.
- [ ] B5.5 (H) **Laudo D5** con mentores: corpus a escalar. Recomendación: los 68 digeribles primero (2.009 pág., 6.340 unidades, ~USD 123); RI (53 TOs, 0 digeribles) como segunda vuelta si B5.6 lo habilita. **[LAUDO ESCRITO REQUERIDO — toca compromisos del PPF/alcance]**: no arranca sin laudo redactado y fechado por la autora.
- [ ] B5.6 (I, $0) Módulo de tablas (pdfplumber `extract_tables` con provenance, sin LLM) — RX-10 y montos invertidos; decide el destino del bloque RI.
- [ ] B5.7 (I) Issue #6: documento de costos con tarifas reales + caching + experimento óptimo dentro de USD 200 (con B5.5). Laudo D4 warm-then-parallel (throughput: ~13 s/unidad → ~29 h secuenciales para 8.010).

### B6 · Escalado: corrida por tandas (issue #11) — T2 · S6–S7 (máquina; humano mínimo)
- [ ] B6.1 (I, ~$40) Tanda 1: 20 TOs digeribles (normativa general prioritaria), E0–E5, **gate de release de B2.6** (regression + shapes + intrínsecas + material propio) antes de ensamblar, carga en Neo4j, app sirviendo el grafo. Reporte: volúmenes, costo real vs estimado, incidencias. Es la primera ejecución del método de B2.8 de punta a punta sobre TOs nunca vistos.
- [ ] B6.2 (I, ~$85) Tanda 2: resto de digeribles (48) si tanda 1 cierra sin sorpresas. Créditos AWS/Bedrock si aplica (`app/llm_backend.py` ya soporta Bedrock).
- [ ] B6.3 (I, ~$5) Sanity funcional sobre el grafo escalado: 10 preguntas ciegas nuevas (protocolo U6) por instancia aislada, N=1, juez EV2 → solo descriptivo (no comparación).
- [ ] B6.4 (I) Cierre #11: reporte de escalado (vacío #5: costo, throughput, latencia).
Condición de arranque: B1, B2, B5 cerrados y A2 en curso o cerrado. Si S6 llega sin B5 cerrado → **se recorta a tanda 1** o se descopa con laudo.

---

## Carril C — Escritura, gobernanza y publicación (siempre en paralelo)

### C0 · Gobernanza inmediata — T1 · S1
- [x] C0.1 (I) **HECHA** — `docs/tablero.md`, `docs/INDICE.md` y `README.md` actualizados a HEAD `85d9fdb` en el commit `2977e69` (tablero con EV2 cerrado: tabla definitiva, validación del juez, mapa causal U-A0, 8 desvíos del período, backlog por regla de estado efectivo, intake por casos; INDICE con las lecturas del período; README a agosto 2026 con nomenclatura canónica). Issues ejecutados por la autora con `gh`: cierres #8/#9/#10 y aperturas por bloque de este plan. El entregable de #9 "tabla defecto → resuelto/persiste" quedó transferido explícitamente a B2.1.
- [x] C0.2 (H) **HECHA** — este plan vive en `docs/plan_tesis.md` (commit de la autora al cierre de esta unidad); protocolo de actualización en la cabecera; se actualiza al cierre de cada unidad.
- [ ] C0.3 (I) `docs/hallazgos_tesis.md`: H14–H20 (inversión métricas intrínsecas P-b; juez bajo flag no confiable; mecanismo presente no operante; defecto de ensamblado +2 con denominador aguas arriba; brecha literal↔anti-léxica; arquitectura > prompt (enmienda 01); alucinación sistemática con retrieval perfecto; esquema v2 halva incorrectos / pipeline nuevo empata sin parches). Corregir `rol_fuente`→`rol_documental`, nota T2 (4 puntos), E4/E5 no ejecutados.
- [ ] C0.4 (H) Laudos de descope escritos: caso de uso 1 (o demo mínima), GraphRAG-MS, versionado temporal (future work con diseño), régimen sin-gold, Graphiti, sub-corpus en inglés. Registrar la inversión de prioridad respecto del PPF §mitigación con justificación técnica. **[LAUDO ESCRITO REQUERIDO — toca compromisos del PPF/alcance]**: ninguna unidad que dependa de estos descopes arranca sin laudo redactado y fechado por la autora.
- [ ] C0.5 (I) `docs/backlog_reextraccion.md`: RX-04 corregido; RX-01..09 cerrados con evidencia del pipeline nuevo; RX-10 abierto → B5.6.
- [ ] C0.6 (I, $0) **Pendiente de la próxima pasada de C0**: (a) en `docs/tablero.md` §5, reemplazar "plan de tesis de la autora (documento de trabajo, no commiteado)" por la referencia a `docs/plan_tesis.md`; (b) actualizar el párrafo "Migración Neo4j" del `docs/tablero.md` (cola de unidades / estado del backend) con el estado post-A1.1: backend con paridad verificada 322/322 en `9e131bf`, modos `paridad`/`fulltext`, `GraphAgentNeo4j`, no inyectado en el pipeline de evaluación; A1.2 como punto de extensión.

### C1 · Esqueleto y redacción de la tesis (skill `latex-udesa`) — T1 · S1–S9
Capítulos (borrador → revisión → final), cada uno alimentado por un bloque:
- [ ] C1.1 Introducción + pregunta + tres sub-preguntas (esquema / retrieval-vs-estructura / KG-RAG vs RAG) + hallazgo rector. (S1–S2)
- [ ] C1.2 Marco teórico + literatura (00–09, 5 vacíos, playbook como contraste; nota "graph engineering"). (S2)
- [ ] C1.3 Corpus y esquema (2.1, 2.2, esquema v2, catálogo de sujetos, ejes A/B, herencia). (S2–S3)
- [ ] C1.4 **El método** — construcción y refinamiento de un KG regulatorio de punta a punta (sigue B2.8): pipeline E0–E5 (diseño, principios, enmienda 01 con P1–P3, costos, limitaciones) + ciclo de refinamiento por releases (B2.6) + retriever/backend + intake. Cada mecanismo con puntero al experimento que lo demuestra (§6). (S3–S4, cierra con B1/B2)
- [ ] C1.5 Metodología de evaluación bajo custodia (pre-registro, sets ciegos, juez 2 pasos, juez de fidelidad por criterios, verificador v7', taxonomía, métricas intrínsecas, regression suite, backend/retrieval). (S3–S5)
- [ ] C1.6 Resultados: 2.3; escalón 1/1b; C1–C7; intrínsecas; EV2 (fidelidad+navegabilidad+atribución); ablación retrieval; head-to-head; gold tripletas; escalado. (S5–S8)
- [ ] C1.7 Discusión: grounded ≠ correct; retrieval ≠ estructura; humano-en-el-loop (H7/H8, Motor 3 no validado); misreadings de métricas; límites (multi-hop, tablas, sujetos, familia del verificador; **concentración del pool de anclas del corpus** — 175 anclas, 28/37 compartidas entre sets sintéticos, `ablacion_retrieval/anexo_solapamiento_anclas.md`, `68c79dc`); descopes. (S7–S8)
- [ ] C1.8 Conclusiones + trabajo futuro (temporalidad, E4-LLM, RI, explicabilidad). (S8)
- [ ] C1.9 Anexos: reproducción (comandos), costos, sellos/sha, glosario. (S8–S9)
- [ ] C1.10 Revisión integral + defensa (guion, banco de preguntas actualizado: Q8/Q16, puntos incómodos redactados). (S9–S10)

### C2 · Publicación y reproducibilidad — T2 · S8
- [ ] C2.1 (I) Release etiquetado + Zenodo/DOI: KG (KG-Refinado y KG-Reextraído-r1 con sha), eval sets sellados (EV2 preguntas+criterios, pares sintéticos, U6), gold de tripletas, scripts de métricas/regression, README de reproducción. Cumple "público" del PPF.
- [ ] C2.2 (I) `docs/ARQUITECTURA.md` snapshot final.

---

## 2. Cronograma sugerido (10 semanas; una unidad por carril por semana)

| Sem | Carril A | Carril B | Carril C |
|---|---|---|---|
| S1 (17–23 ago) | A0.1–A0.2 (U-A0) | — (U-B1a entra recién al cierre revisado de U-A0 o de U-C0) | C0.1–C0.5, C1.1 (U-C0) |
| S2 (24–30 ago) | A0.3–A0.4, A1.1–A1.3 | B1.1–B1.7 (U-B1a, arranque condicionado), B2.1 | B4.1, C1.2–C1.3 |
| S3 (31 ago–6 sep) | A1.4–A1.5 | B2.2–B2.5, B3 | B4.2, C1.4–C1.5 |
| S4 (7–13 sep) | A1.6, A2.1–A2.2 | B1.8, B5.1–B5.4 | B4.2–B4.3, C1.5 |
| S5 (14–20 sep) | A2.3–A2.4 | B5.5–B5.7 | C1.6 |
| S6 (21–27 sep) | A3 (T2) | B6.1 | C1.6–C1.7 |
| S7 (28 sep–4 oct) | — | B6.2–B6.4 | C1.7 |
| S8 (5–11 oct) | buffer | buffer | C1.8–C1.9, C2 |
| S9–S10 (12–26 oct) | — | — | C1.10 |

Presupuesto API estimado del plan: A ≈ 70 · B ≈ 135 (escalado 125 + resto) · C 0 → ~USD 205
(+ ~USD 30 de reserva)\*. El escalado usa el budget de #6 / créditos AWS.

\* Vigencia de las tarifas: las estimaciones usan tarifas vigentes al 17/08. El precio de
Sonnet USD 2/10 por MTok quedó **confirmado como estándar** (no era intro con vencimiento;
re-verificado en U-A1.3, `68c79dc`), así que la alerta de vencimiento del 31/08 queda sin
efecto. Se mantiene la regla: toda autorización de fase B re-verifica tarifa contra
documentación oficial y re-estima antes de correr; el buffer de USD 30 se declara en la
autorización correspondiente si una tarifa cambia.

Regla de recorte si S5 llega atrasado: se recorta primero **B6** (a tanda 1 o descope),
después **A3**, después **B3.3–B3.4**. Nunca se recorta A2 ni C1.
Si S4 llega atrasado, B2.8 (documento del método) se reduce a esqueleto más secciones ya
existentes y se completa durante la escritura de C1.4; B2.6 (protocolo del ciclo) y B2.1
(regression suite) no se recortan — son los que el escalado ejecuta.

---

## 3. Cómo se ejecuta (instancias en paralelo)

- **El recurso limitante del plan es el ancho de banda de revisión y laudo de la autora**
  (cada freno = revisión de mesa + laudo + aplicación de actualización), más las tareas
  humano-intensivas B4.2 (anotación de tripletas) y C1 (escritura). Por eso el arranque
  corre con DOS carriles (U-A0 y U-C0) y el tercero entra al cierre revisado de uno de ellos.
- **Una unidad = un mandato** (skill `redaccion-prompt-ejecutor`): objetivo, escrituras
  enumeradas, criterios de aceptación, tope de API, "qué NO tocar", paquete de revisión.
  El mandato cita este plan por id (p. ej. "Unidad B1.1–B1.3").
- **Paralelismo seguro**: hasta 3 instancias simultáneas, **una por carril**, con
  directorios disjuntos: A → `data/experiment/{ev2_reporte,neo4j,agente_v2,rag_baseline}/`;
  B → `data/experiment/reextraccion_v2/`, `scripts/`; C → `docs/`, `docs/tesis/`.
  Nadie toca el cuarteto congelado, las zonas selladas ni la caché de otra instancia.
- **Al frenar**: reporte pegable + `revision_<unidad>/` con manifest sha256 + **propuesta
  de actualización de este plan** (checkboxes, números, desvíos). La autora revisa,
  laudea, commitea y aplica la actualización del plan.
- **Revisión** con la skill `revision-outputs-agente` antes de aceptar cualquier reporte;
  el juez y el verificador nunca ven adjudicaciones humanas; los sets sellados no se abren
  para diseñar nada.
- **Cadencia**: cierre semanal → tablero + plan actualizados en un solo commit.

## 4. Primeras unidades a delegar (esta semana)

1. **U-A0** (carril A): reporte consolidado EV2 + atribución determinística de primer nivel
   con regla pre-registrada (A0.1–A0.2). $0. Entregable en `data/experiment/ev2_reporte/`.
2. **U-C0** (carril C): actualización de tablero/INDICE/README/hallazgos H14–H20/backlog RX
   (C0.1, C0.3, C0.5) + esqueleto LaTeX de capítulos con mapa bloque→sección (C1.1 borrador).
   $0. Los laudos C0.2/C0.4 son de la autora.
3. **U-B1a** (carril B, **condicionada al cierre revisado de U-A0 o de U-C0**): E5 esqueleto +
   E4 determinístico + referencias cruzadas + provenance rica + selftest de
   `ensamblar_corpus` (B1.1–B1.5), re-ensamblado KG-Reextraído-r1 sin API (B1.7). $0.

## 5. Decisiones que solo la autora puede tomar (esta semana)

Las decisiones D-a..D-e las toma la autora; cada una queda registrada como laudo escrito con
justificación técnica antes de ejecutar la unidad que la usa.

- D-a Caso de uso 1: descope escrito vs demo mínima (A2.4 / C0.4).
- D-b Gold de tripletas: alcance (25 unidades) y quién anota (instancia ciega + revisión). **[LAUDO ESCRITO REQUERIDO — toca compromisos del PPF/alcance]**: B4 no arranca sin laudo redactado y fechado por la autora.
- D-c Corpus a escalar (D5) y si el escalado entra o se recorta a tanda 1.
- D-d Umbrales de intrínsecas pasada 2 (B3.1).
- D-e **RESUELTA**: el plan vive en `docs/plan_tesis.md` (C0.2); issues por bloque abiertos en U-C0.1.

## 6. Mapa de contribución: mecanismo → experimento que lo demuestra → estado

La tesis se lee como UN método (B2.8 / C1.4) y cada mecanismo del método tiene su
demostración. Esta tabla es la que se mantiene al día; lo que no tenga demostración al
cierre se declara como mecanismo propuesto sin validar.

| # | Mecanismo del método | Demostración (experimento / artefacto sellado) | Fuente (commit/archivo) | Estado |
|---|---|---|---|---|
| M-1 | Esquema cerrado con catálogo de sujetos y provenance por elemento (esquema v2) | Fase 2.3 (5 estrategias, KG-Base gana); escalón 1/1b (216 corridas sin error de sujeto); EV2: ambos grafos v2 halvan incorrectos vs KG-Base | `docs/esquema_v2_diseño.md`, `docs/spec_extraccion_v2.md`; `d56020e` (`frozen_run/reporte_final.md`); `2c261aa` (`lectura_P1P5_escalon1.md`), `e77b11f` (`docs/lectura_escalon1b.md`); `64de678` (`cruce_definitivo_por_grafo_SOLO_MESA.md`) | hecho |
| M-2 | Chunking estructural con herencia y mini-chunks (E0) | cobertura línea a línea 0 huérfanas; enmienda 01 P1 (60→0 faltantes heredados); paridad 152/152 en E0 seco | `e287fe3` + `d082812` (`reextraccion_v2/e0_chunking/INFORME_E0.md`, `salida_enm01/`); `111ed19` (`escalado_prep/referencia_subset.json`) | hecho |
| M-3 | Extractor chico con prefijo cacheado y validador determinístico (E1) | caching 87/87 y 101/101 hits; costo USD 32,97 por 5 TOs; candado doble de namespace | `cd76991` (`reextraccion_v2/e1_extractor/INFORME_E1_FASEA.md`); `6212dfa` (`docs/decisiones_caching_extraccion.md`); `5273c0c` (`corpus_v2/salida/estado_corpus.json`) | hecho |
| M-4 | Reduce determinístico con dedup exacto, fan-in y censo (E2) | RX-01 (102 descartes) cerrado: 0 duplicados/ausentes en 1.763; M10 chunks mudos 53→0 | `8d0fac4` (`reextraccion_v2/e2_reduce/INFORME_E2.md`); `5273c0c` (`corpus_v2/salida/<to>/reporte_e2_<to>.json`); `c6f808e` (`metricas_intrinsecas/pasada1_resumen.md`, fila M10) | hecho |
| M-5 | Verificador de completitud en contexto fresco con citas verificadas y ratchet tope 1 (E3) | tests T1–T3 3/3; cola 29,9 %→21,8 % (P2 refutada, publicada) → 4,5 % corpus | `e287fe3` (`reextraccion_v2/e3_verificador/INFORME_E3_FASEA.md`, `remedicion_citas/`); `d082812` (`faseB_pro_enm01/analisis_enm01.json`); `5273c0c` (`corpus_v2/salida/tests_respuesta_conocida.json`) | hecho |
| M-6 | Resolución consciente de variación + esqueleto de clases (E4/E5) | B1 → KG-Reextraído-r1; fidelidad EV2 una vez (B1.8); regression (B2.3) | — | **pendiente** |
| M-7 | Referencias cruzadas norma→norma como aristas (multi-hop) | B1.3 + M12 (B3.3) + casos multi-norma en A2/A0 | — | **pendiente** |
| M-8 | Evaluación bajo custodia: sets ciegos sellados, juez de dos pasos, juez de fidelidad por criterios, adjudicación simétrica | Fase 2.3 (200 claims firmados); EV2 (11/12, 98,1 %); calibración U6 | `7d118ee` (eval_set_v1 ciego); `d56020e` (`frozen_run/reporte_final.md`, `adjudicacion_FIRMADO.json`); `9c44516` (sello EV2, `manifest_ev2.txt`); `1a0ac5c` (`ev2_juez/calibracion/registro_calibracion.md`); `64de678` (`adjudicacion/reporte_muestra_simetrica.md`) | hecho |
| M-9 | Verificador de atribución grafo-vs-agente con taxonomía cerrada y capa determinística | ciclo 2 (cero silenciosos), gate U5 (en-familia); B2.7 gen-3 | `7cc3bd2` (`docs/lectura_ciclo2.md`); `f5bfb2c` (`docs/lectura_gate_u5.md`); `docs/especificacion_verificador_v57.md`, `docs/especificacion_capa_deterministica.md` | hecho / **gate gen-3 pendiente** |
| M-10 | Métricas intrínsecas pareadas con denominador aguas arriba | pasada 1 (P-b confirmada); pasada 2 con umbrales (B3) | `cdf90e6` (`docs/spec_evaluacion_intrinseca.md`, pre-registro); `c6f808e` (`metricas_intrinsecas/pasada1_resumen.md`); `38ac8b1` (laudo M7) | hecho / pasada 2 pendiente |
| M-11 | Circuito de refinamiento con backlog tipado, propuestas selladas y re-test | C1–C7 (re-tests 4/4…38/38; C5 5/5, C6 deslinde de capas) | `docs/spec_backlog_refinamiento.md`; `data/backlog/backlog.jsonl`; `data/backlog/retests/C{1..7}_retest_*.md` (commits `d9e7e9b`, `756d6ec`, `05984e1` entre otros) | hecho |
| M-12 | Refinamiento a nivel pipeline: regression suite + shapes + releases + hotfix con test | B2.1–B2.6; primera ejecución completa en B6.1 | — | **pendiente** |
| M-13 | Retriever BM25/Neo4j y tools v2 (retrieval ≠ estructura) | A1 ablación pre-registrada; latencia p50/p95 | — (backend experimental `c26cb9b`, `data/experiment/neo4j/README.md`, no inyectado) | **pendiente** |
| M-14 | Intake de feedback de la app → backlog (Motor 2) | U6 (25 preguntas reales), BKL-0024/0025, cola de intake cerrada | `0d5fd10` (`scripts/adaptador_sesiones.py`); `b337152` (`exploracion/adjudicacion/u6_adjudicacion_humana.jsonl`); `data/backlog/intake/cola_intake.jsonl` | hecho |
| M-15 | Comparación justa KG-RAG vs RAG sobre los mismos chunks de E0 | A2 head-to-head + Pareto | — | **pendiente** |
| M-16 | Escalado por tandas con gate de release y reporte de costo/throughput | B5–B6 (68 TOs digeribles) | — (prep `111ed19`, `escalado_prep/resumen_escalado.md`) | **pendiente / T2** |
| M-17 | Gold de tripletas y P/R de extracción | B4 | — | **pendiente** |
| M-18 | Circuito de custodia revisor-ejecutor para investigación con agentes LLM: mandatos por unidad con criterios de aceptación, frenos declarados, laudos de la autora, pre-registro por commit, verificación de mesa contra archivos (nunca narrativa), errores de ambos lados detectados y documentados | Registros de desvíos declarados del período: sello tardío `9c44516`; pasada inválida de calibración documentada; commit tardío declarado en `b624865`. Destino en la tesis: C1.5 (metodología) + candidato a sección propia de contribuciones | `CLAUDE.md` (reglas del circuito, §4 a–h); mensaje de commit `9c44516` ("sello efectivo 2026-08-13… pre-registro válido"); `data/experiment/ev2_juez/calibracion/registro_calibracion.md` (commit `1a0ac5c`); mensaje de commit `b624865` ("commit tardío respecto del cierre de la unidad, detectado por la unidad §7") | hecho |
| M-19 | Atribución causal de fallas determinística de primer nivel (presente→consultada→vista→generación, por replay de trazas, USD 0, reproducible al byte; abstención como columna cruzada) | EV2: 120 trazas base + 191 §7 atribuidas; perfiles de falla distintos en el empate 9-9; generación clase modal 17/25/21; techo de retrieval 14/7/6 (H1–H7) | `40603a9` (regla sellada pre-cómputo, `data/experiment/ev2_reporte/regla_atribucion.md`, selftest 24/24) + `85d9fdb` (`data/experiment/ev2_reporte/salida/atribucion_fallas.{json,md}`, doble corrida byte-idéntica) | hecho |

Regla: un mecanismo solo figura "hecho" con fuente verificable en esta columna.
