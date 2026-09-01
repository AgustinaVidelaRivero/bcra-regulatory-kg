# Plan de cierre de la tesis — v10 (2026-09-01)

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

**Fe de erratas de mensajes de commit** (los mensajes no se enmiendan; manda el estado de los
archivos): `966253e` dice que los laudos D-g y D-f quedan **pendientes de firma**, cuando ambos se
**firmaron en el mismo acto** y ese commit ya los contiene firmados. El estado correcto es el de
`docs/laudo_D-g_alcance_corpus.md` y `docs/laudo_D-f_secuencia_tripletas.md`.
`8dea823` (laudo ESQ-2) contiene «/bin/zsh» donde el mensaje decía «$0» (expansión de shell al
commitear con comillas dobles); el archivo `docs/laudo_ESQ-2_diseno.md` está intacto.
`930f289` (fe de erratas de ranking ESQ-2) tiene dos artefactos cosméticos de pegado de terminal
(«decada» por «de cada»; «0,Wilson» sin espacio); el archivo
`data/experiment/esq/fe_erratas_prerregistro_esq2_ranking.md` está intacto.

Changelog: v1 (2026-08-17) — plan inicial con revisión de mesa (nomenclatura canónica,
laudos requeridos, principio 7, tarifas, cuello de botella de revisión, gate informativo de
intrínsecas, mapa de mecanismos con fuentes M-1…M-19, B2.6–B2.8) y cierres registrados de
U-A0, U-C0.1, U-A1.1, U-A1.2.
v2 (2026-08-18) — reencuadre por los resultados de A1.4 (el cuello es la política del agente,
no el retriever) y por el rediseño del head-to-head (un solo harness y un solo prompt para
los dos brazos, con el brazo como variable declarada vía MCP):
principio 8 (dos instrumentos declarados), banco de evaluación en Claude Code + MCP
(A2.0/A2.0b), A1.7 re-enfocada como puente de calibración de agente (absorbe A3),
embeddings sobre nodos (B1.10), re-corrida de robustez como unidad condicional (A2.5),
M-21 en el mapa de mecanismos.
v3 (2026-08-18) — A2.0 se parte en tres unidades con el gate primero (A2.0-gate → A2.0-banco →
A2.0-reportes: el gate de trazabilidad es condición de posibilidad del banco y falla barato);
nota de equivalencia de nomenclatura; transversal de **checkpoint en disco** agregado a §3.
v7 (2026-08-23) — cierre de U-B1a: **KG-Reextraído-r1** (sha `0226e947…`, 6.529/17.772, T1–T7
7/7, muestra de 30 referencias inspeccionada 30/30 OK por la autora); B1.1–B1.7 hechas; fila de
r1 en la nomenclatura; pendientes de laudo y tests de reglas de E4 anotados en B2; entrada r1
en `neo4j/grafos.py` como prerrequisito de carga.
v8 (2026-08-28) — reencuadre por la reunión de mentores del 26/08: principio 10 (los cinco TOs
son conjunto de DESARROLLO; el corpus escalado es el conjunto de TEST y el objeto central);
D-g/D-f resueltas por laudo firmado y D-h (tesis de recurso; la comparación baja a validación
de diseño); bloque ESQ como T1 bloqueante del escalado con fuga al test cerrada
(documentos_excluidos_esq.json); B5/B6 re-tierados a T1; B6.3 rediseñada como EVALUACIÓN FINAL
con pre-registro propio; secuencia ESQ-RI para el régimen informativo con el hallazgo del
modelo de datos (fe1fe36); U-RW y lecturas de la reunión; cola de mejoras diferidas creada.
v9 (2026-08-31) — saga del control de esquema cerrada: escalera P1/P1′/P1″ falsada
(U-ESQ-1c/1d/1e; canal declarativo inviable — deformación semántica, inestable), calibración
del modo (ii) con P-cal falsada por su segunda mitad (U-ESQ-2-cal `eadf4a5`: capacidad sí,
precisión no) → RAMA (b): censo por LLM CERRADO con doble evidencia, ESQ-2 protocolizada como
única vía, D7 muerto; hueco de potestades confirmado en corpus real; ruta crítica reescrita.
v10 (2026-09-01) — U-ESQ-2 ejecutada y cerrada (`a7788c1`, bajo laudo `8dea823` + pre-registro
`2240c9c`): gate de paridad 10/10 USD 0, extracción E1-solo 762/762 a USD 4,1079, fe de erratas
de ranking `930f289` (round-robin anidado disparador × TO, cegado de origen restaurado),
worksheet de 75 fichas listo; corrección D4 del laudo derramada al plan (se queman 10
documentos, no 20); ruta crítica: sigue la lectura de la autora → spot-check de mesa → tabla
con Wilson → ESQ-3; fes de erratas de mensajes `8dea823` y `930f289` registradas.
v6 (2026-08-23) — rediseño de la evaluación intrínseca y arranque de la escritura:
principio 9 (el grafo evaluado se sella; las correcciones producen una versión posterior);
B4 rediseñada como evaluación intrínseca a nivel tripleta con dos vías (precisión con juicio
de correctitud + importancia sobre muestra del grafo; recall por ranking de importancia sobre
tripletas extraídas de fragmentos) y juez LLM calibrado contra adjudicación humana; B6.3
reusa ese instrumento sobre el grafo escalado; C1 con estructura de introducción en ocho
ideas, reglas de estilo y template LaTeX del taller; prompt custom del banco como argumento
sellado (A2.0-banco).
v5 (2026-08-23) — cierre de A2.0b: modelo de embeddings laudado por bake-off propio
(`docs/decision_modelo_embeddings.md`); requisitos del laudo incorporados a A2.0-banco (ii) y
B1.10; hallazgos del bake-off agregados a C0.3.
v4 (2026-08-18) — cierre de A2.0-gate (veredicto PASA CON CONDICIONES) y laudo de sus siete
requisitos (`docs/laudo_gate_trazabilidad.md`): R1–R7 entran como diseño de A2.0-banco, el banco
expone la **firma v1** de las tools (R2, opción B) y en consecuencia **A1.7 usa C10 como base
congelada**; la demostración por clase debe repetirse **sobre MCP** dentro de A2.0-banco.

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
**Ablación de retrieval (A1.4, factorial 2×2 sobre KG-Refinado, 400 trazas, USD 11,19; fuente
`data/experiment/ablacion_retrieval/corrida/resultados/`):** de las 20 anclas anti-léxicas
que el control falla, **7 son falla de búsqueda (nunca vistas) y 13 son falla de selección
del agente (vistas y no abiertas)**. BM25 recupera 2 de esas 7 y no toca las 13 → ningún IC
bootstrap anti-léxico excluye el 0 (P2 refutada). Donde sí gana es en lo literal, **por
ranking y no por cobertura**: mismas 52/53 vistas, brecha vista-sin-consultar 6 → 1, recall
consultada 0,887 → 0,981 (IC excluye 0), con `hit_tool_limit` 36 % (C00) → 29 % (BM25) →
24 % (C11) y abstenciones 20 % (C00) → 11 % (BM25). Las tools v2 no movieron la aguja
porque **el agente nunca paginó** (0 de 275 llamadas) — tercera instancia medida de "mecanismo presente, no operante" (esqueleto 8,3 %
en el escalón 1; alucinación con retrieval perfecto BKL-0026 3/3; paginación 0/275).
**Consecuencia de plan: el cuello de botella es la política del agente, no el retriever.**

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
8. **Dos instrumentos, declarados y no intercambiables.** (a) el **harness congelado**
   (Haiku 4.5, 3 tools, 15 tool calls, juez v2.1.1) sostiene todo lo sellado — Fase 2.3,
   escalón 1/1b, EV2, A1.4; (b) el **banco Claude Code + MCP** (A2.0-gate → A2.0-banco) sostiene el
   head-to-head, donde la validez viene de que **los dos brazos comparten la misma caja
   negra**. Los resultados de un instrumento **no se cruzan** con los del otro en una misma
   tabla; el puente entre ambos es A1.7, medido con material propio. Nada sellado se
   re-corre para reemplazarse: los resultados nuevos se **agregan**, nunca sustituyen.
9. **El grafo evaluado se sella y no se corrige.** Toda evaluación (extrínseca o
   intrínseca) se reporta sobre el grafo tal como estaba al sellarse; los defectos que la
   evaluación revela se corrigen en una **versión posterior**, declarada como tal (release
   r+1 del ciclo B2.6). La tesis tiene así dos contribuciones con dos objetos: el **método**
   (cuánto rinde, con resultados sinceros sobre el grafo pre-corrección) y el **entregable**
   (el mejor grafo posible, post-evaluación, con las correcciones trazadas a los hallazgos
   que las motivaron). Nunca se presenta el segundo como si fuera el primero.
10. **Conjunto de desarrollo vs conjunto de test.** Los cinco Textos Ordenados del subset son
    el **conjunto de desarrollo** (train/eval) del proyecto: sobre ellos se itera, se ajusta el
    algoritmo y se corren todas las evaluaciones de desarrollo — EV2, refinamiento, ablaciones,
    tripletas —, sin límite de iteración y sin que eso comprometa la validez de la tesis. El
    **corpus BCRA escalado es el conjunto de test** y el **objeto central de la tesis**: sobre
    él se corre UNA evaluación final, pre-registrada antes de mirarla, sin iterar sobre sus
    resultados. Consecuencia directa: presentar la tesis como un estudio sobre los cinco TOs
    sería sobreajustar el documento; los experimentos del subset se presentan como lo que son
    —el desarrollo y la validación del método— y el resultado que sostiene la tesis se mide
    sobre el recurso final. El principio 7 (EV2 es examen) sigue rigiendo **dentro** del
    conjunto de desarrollo: EV2 no se re-mide ni se ajusta mirando sus resultados. Origen:
    marco establecido en la reunión de mentores del 26/08/2026; su aplicación a cada unidad
    concreta se registra por laudo (D-g, D-f).

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
- [x] A1.4 (I, tope laudado **USD 20** — corrige el «~$12» original; gasto real **USD 11,19**) **HECHA en `ffc6ff6`** (artefactos en `data/experiment/ablacion_retrieval/corrida/`) — corrida factorial {booleano, BM25} × {tools v1, v2} sobre KG-Refinado (`26fac8b4`), 50 pares × 2 variantes × 4 celdas = **400 trazas**, N=1, **0 cross-hits**, replay estándar + fuerte 400/400 con doble corrida byte-idéntica, 1 error técnico persistido (C10 `EB-005::antilexica`, misma firma que EA-013). Lectura mecánica contra los umbrales sellados: **P1 cumplida** (Δ_c(C00)=0,264), **P2 no cumplida** (BM25 sube literal 0,887→0,981 y anti 0,623→0,679 sin cerrar la brecha), **P3 cumplida**, **P4 no cumplida** (tools v2 no mejora E-B/entrante ni `hit_tool_limit` con booleano; el agente nunca paginó), **P5 cumplida** (C11 mejor: 0,698 anti, ganancia aditiva), **P6 no cumplida** (huérfanos: consultada v2 = v1). Ningún IC bootstrap anti-léxico excluye 0; los literales BM25 sí. **Laudo de config:** **C11 {BM25, tools v2}**, elegida mecánicamente de la tabla sellada (P5) sin abrir EV2.
- [ ] A1.5 (I, ~$5) Fidelidad EV2 (40 preguntas) de KG-Refinado con la mejor configuración de retrieval → "KG-RAG en su mejor forma" para A2. Mismo juez, mismo mapping, adjudicación simétrica 10 %. **Rige el principio 7**: una sola medición sobre EV2, configuración elegida y sellada en A1.3/A1.4/A1.7 sobre material propio, nunca ajustada mirando EV2. **Fusión con A2.2 APROBADA CON CONDICIÓN:** si **A1.7 cierra antes**, esta medición no se corre por separado — el brazo "KG-RAG en su mejor forma" (config de retrieval + política) entra como un brazo más de la medición única de A2.2. **Si A1.7 no cierra a tiempo**, A1.5 vuelve a ser medición propia con la config **C11** y se declara así en el reporte.
- [x] A1.6 (H) **HECHA — laudo en `docs/laudo_promocion_backend.md`**: BM25 (Neo4j full-text, config sellada en el pre-registro de A1.4) pasa a ser el retriever por defecto de la app y del escalado, con el in-memory como fallback declarado; tools v2 NO se promueven (efecto no atribuible; el banco expone la firma v1 por R2); el laudo no afirma que BM25 cierre la brecha anti-léxica. Cierra #5. Enunciado original: ¿el índice BM25 pasa a ser el backend por defecto de la app y del escalado? Cerrar #5. **Escribible ya con la evidencia de A1.4**: BM25 gana en literal (+0,094, IC excluye 0), baja `hit_tool_limit` (36 %→29 %; 37 %→24 % con tools v2) y abstenciones (20 %→11 %), busca ~3× más rápido y **no regresa** (P3 cumplida); tools v2 saca BKL-0027 del espacio de acciones por diseño, con la nota de que la paginación quedó sin uso (0/275). **[LAUDO ESCRITO REQUERIDO — toca compromisos del PPF/alcance]**: no arranca sin laudo redactado y fechado por la autora.
- [ ] A1.7 (H+I, ~$12: ~$2 de pares frescos + ~$10 de corrida) **Ablación de agente / política — puente de calibración entre los dos instrumentos (principio 8)** — T1, atacar las 13 anclas anti-léxicas que ningún factor de A1.4 movió. Pre-registro sellado propio (mismo molde que A1.3), material **nuevo** (pares sintéticos semilla `sinteticas-faseA-v4`; EV2 no se abre), **mismo KG y mismas tools vía el servidor MCP de A2.0-banco**, y una sola variable por brazo: (a) **agente congelado C10 {BM25, tools v1} vs agente Claude Code** (la comparación central: si un agente más fuerte cierra la brecha de selección, es hallazgo; si no la cierra, es hallazgo mayor). **La base es C10 y no C11 por el laudo del gate** (`docs/laudo_gate_trazabilidad.md`, R2 opción B: el banco expone la firma v1, así que la comparación con tools v1 en los dos lados sigue siendo de una sola variable; C10 también está medida en la tabla sellada de A1.4); (b) presupuesto de pasos (15 → 25) en el agente congelado; (c) `contexto_de(id, saltos≤2, presupuesto_tokens)` — el punto de extensión declarado en A1.2 — que devuelve el subgrafo de los top-k en UNA llamada, **del lado del harness congelado** (el banco expone v1). Predicciones con umbral: brecha vista-sin-consultar anti-léxica baja ≥ ⅓; `hit_tool_limit` (o su equivalente declarado en el banco nuevo) anti-léxico baja ≥ 15 puntos; recall consultada anti-léxico sube; **la clase `generación` no cambia** (si cambia, es hallazgo, no ruido). Replay determinístico + IC bootstrap apareado. **Absorbe A3** (el agente de Claude Code ya es de clase Sonnet). Depende de A2.0-banco para el brazo (a).
Depende de: A0 (para leer resultados con la atribución). Riesgo: contenedor Docker en la máquina de corrida; mitigación: `SQLite FTS5` como plan B ya evaluado en `decision_backend_grafo.md`.

### A2 · Baseline RAG tradicional y head-to-head (issue #12, pregunta rectora) — T1 · S3–S5
- [x] **A2.0-gate** (I, USD 0 en fase A; fase B USD 1,30 de tope 2) **HECHA (fases A y B)** — veredicto **PASA CON CONDICIONES**: la atribución causal se reconstruye desde una sesión de Claude Code en las cuatro clases, con el código de A0.2 importado, replay estándar y fuerte en verde y doble corrida byte-idéntica (**10/11 PASS**; el caso 11 falla el replay por el contrato v2 de las tools). Artefactos en `data/experiment/banco_mcp/gate/` (`veredicto_gate.md`, `inventario_campos.md`, `corrida/`, `sesiones/`), sellados en `c09663a`. Laudo de los siete requisitos en **`docs/laudo_gate_trazabilidad.md`**. **Fase B en `b08095a`** (sesiones reales con `claude -p`, pre-declaración sellada antes de correr): maquinaria 9/9 (replay estándar + fuerte, determinismo, re-adaptación byte-idéntica, 35 tool calls sin rechazos); las patologías de A1.4 **se replican con otro modelo y agente real** (`vista_no_consultada` emerge sola en GATE-04; el caso (V,F,V) de la regla ocurre en GATE-03); P0 (prompt de sistema del harness) medido: 9.412 tokens en modo seguro vs 19.074 con la configuración local; ratio de caché 12,2× lecturas por escritura. **Tres requisitos nuevos para A2.0-banco**: **R8** una sesión usa varios modelos → la metadata de modelo es un inventario, no un string; **R9** el `total_cost_usd` del CLI sobrefactura ~3× (1,2983 vs 0,4191 recomputado) → el banco computa costo desde tokens con precios sellados; **R10** la configuración del harness es variable sellada. Enunciado original de la unidad: Adaptador de sesión de Claude Code → traza del formato del repo, demostrando **por clase** (`ausencia_kg`, `alcanzabilidad`, `vista_no_consultada`, `generacion`) que **el replay determinístico y la atribución causal de A0.2 sobreviven** (`data/experiment/ev2_reporte/regla_atribucion.md`, `40603a9`). Se hace contra sesiones de Claude Code capturadas a mano con **tools de juguete que imitan el contrato** de las tools del grafo: **no requiere el banco ni los servidores MCP**. Si algo no sobrevive → **freno y laudo antes de construir nada**: A2 cambiaría de forma (la atribución causal es el diferencial de la tesis, no un accesorio) y eso hay que saberlo **antes** de gastar en infraestructura. **Va primero porque falla barato.**
- [x] **A2.0-banco** (I; fase A USD 0 + fase B USD 0,534 de tope 3) **HECHA en `1fa79de` (fases A y B)** — banco operativo con los dos brazos corriendo de punta a punta: 12/12 sesiones con servidores `connected` y tools en init, 43/43 tool calls correlacionadas al log R1 (fuente de verdad; 0 truncados), JSON del contrato 12/12, adaptación sin rechazos, **replay estándar y fuerte 4/4 y determinismo 4/4 en el brazo KG** bajo los tres veredictos, aislamiento end-to-end (a)–(d) con `respondible:false` y 0 llamadas ante pedidos fuera de capacidad. **P0 de `--bare` con tools: kg 3.134 / vector 2.728 tokens** (el 9.412 de safe-mode queda como referencia histórica de otra versión). **R9 == CLI 12/12 (razón 1,000) en CLI ≥ 2.1.221** — validación cruzada nueva; el banco sigue computando desde tokens. **Desvíos declarados**: corrida 1 (12/12 `pending`, `tools=[]`, 0 llamadas; USD 0,093) conservada como evidencia con su diagnóstico — el agente simuló llamadas en prosa en 7/8 y en una fabricó la respuesta completa de la tool (evidencia para C0.3/C1.7, **encuadre**: fabricación bajo contradicción de configuración, no propensión en condiciones normales); anclas del smoke corregidas por territorio quemado ANTES de correr (chequeo `verificar_territorio.py` obligatorio en adelante); **re-sellado de versión del CLI** 2.1.196 → 2.1.241 con historial en config (laudo C1a; el gate queda como evidencia bajo 2.1.196) y de prompt (regla de honestidad C1c + lista de TOs corregida). **Hallazgo H-B2**: `--max-turns 12` no disparó con `num_turns=14` — semántica a caracterizar antes del pre-registro de A2.1. Enunciado original: **El banco: Claude Code + MCP** — el brazo de evaluación pasa a ser una **variable declarada** (qué servidor MCP se enchufa), no dos harness distintos. Piezas: (i) **servidor MCP del KG** que **reusa** `Neo4jIndex` (A1.1) y expone las tools con la **firma v1** (`buscar_nodos` BM25, `ver_nodo`, `ver_vecinos(id, direccion)`) por el laudo R2 — nada se reimplementa; la paginación, el filtro por relación y `contexto_de` (A1.2) **quedan fuera del banco** y siguen disponibles del lado del harness congelado; (ii) **servidor MCP vectorial** sobre los **chunks de E0** en composición propio + herencia (índice local determinístico, sin servicio externo) con **`microsoft/harrier-oss-v1-0.6b` según el laudo A2.0b** (`docs/decision_modelo_embeddings.md` §7–§8): revisión pinneada, `float32`, `max_seq_length=32768`, prompt `web_search_query` **solo en consultas** y nunca en documentos, con test de asimetría; versiones de librería del bake-off pinneadas en el `requirements.txt` del banco; (iii) los dos agentes vía `claude -p` (no interactivo) con `--model` fijo; **el prompt custom entra como argumento** (archivo de instrucciones por brazo o string pasado a `claude -p`), es parte de la configuración sellada (R10), idéntico entre brazos salvo la descripción de la tool, y en la tesis se reporta como «harness fijo + prompt custom declarado»; (iv) **aislamiento verificado, no asumido**, por capacidad y no por contenido: (a) inventario de tools por brazo, (b) denegación de acceso a los artefactos del grafo (`kg.json`, directorios del backend) y (c) al puerto de la base, (d) test positivo por brazo; (v) **metadata por traza**: model id exacto devuelto por la API, vía de credenciales, versión de cada servidor MCP, sha256 del `kg.json` y del índice vectorial, config del retriever, e inventario de tools efectivamente disponibles en esa sesión; (vi) **vía de credenciales parametrizada** (suscripción / API / Bedrock) con identidad estructural verificable por hash y umbral de switch declarado como número (trazas u horas), con los límites de uso verificados **antes** de una corrida larga; (vii) selftest integrador y estimación de la corrida; (viii) **los siete requisitos laudados en `docs/laudo_gate_trazabilidad.md`, como diseño y no como parche**: **R1** log de llamadas del lado del servidor con entrada y salida íntegras (la sesión es índice, no fuente de verdad — el registro de sesión trunca resultados a 30.000 chars); **R2** el banco expone la **firma v1** de las tools (opción laudada; no se escribe driver de replay nuevo ni se edita `metrica.py`); **R3** marca de completitud por sesión, y toda traza sin ella se excluye de la métrica y se declara —nunca se atribuye—, porque dos clases se afirman por ausencia y un paso perdido migra la clase en silencio; **R4** contrato de salida estructurada fijado en el prompt, idéntico en los dos brazos; **R5** criterio de corte declarado y registrado por traza (reemplaza al tope de 15 llamadas; no se compara numéricamente con `hit_tool_limit`); **R6** aislamiento por capacidad (ya previsto); **R7** mapa de numeración de pasos a identificadores de llamada; (ix) **R8–R10 de la fase B del gate** (`b08095a`): metadata de modelo como inventario por traza; costo computado desde tokens con precios sellados, nunca del `total_cost_usd` del CLI; configuración del harness (modo seguro vs local, P0 ≈ 9,4k vs 19,1k tokens) sellada y registrada por traza; (x) **repetir la demostración por clase del gate sobre el transporte MCP** —condición de aceptación, no extra: lo demostrado en A2.0-gate vale para tool calls de sesión— y **medir y declarar el tope de tamaño de resultados por MCP**. **Depende de A2.0-gate**: se construye sabiendo **qué debe persistir cada servidor** para que el adaptador funcione (si el gate exige campos extra en la salida de las tools, entran en el diseño de los servidores, no como parche posterior). Limitación declarada: el prompt interno de Claude Code no está bajo control de la autora; la validez interna viene de que **ambos brazos comparten la misma caja negra**.
- [ ] **A2.0-reportes** (I, $0) **Agente de reportes** sobre trazas ya adaptadas: arma el informe con las tablas del repo desde las trazas del banco. **Depende de A2.0-gate y A2.0-banco** (sin trazas adaptadas no hay insumo). Es lo último y lo más recortable de los tres.
- [x] A2.0b (H) **HECHA — laudo en `docs/decision_modelo_embeddings.md`**: elegido **`microsoft/harrier-oss-v1-0.6b`** (MIT, revisión `f9b9dc8d…`) por bake-off propio sobre el corpus (`data/experiment/bakeoff_embeddings/`, USD 0): gana las 6 celdas recall@{1,5,10} × {literal, anti-léxica} contra los elegibles bajo la regla principal (n=50 por variante), menor brecha (+16 pp), y la referencia no elegible por licencia no lo supera en ninguna columna. El criterio sellado ex ante no resolvió (control n=30 subpotenciado) y la elección se declara como tal, no como superioridad estadística. Hallazgos colaterales: complementariedad léxico/denso medida (BM25 72 vs 52 literal; 16 vs 36 anti-léxica) y la brecha anti-léxica sobrevive a un tercer instrumento. Requisitos para el banco en §8 del laudo (prompt de query obligatorio y asimétrico con test; despliegue de lo medido; versiones pinneadas). Enunciado original: fecha del snapshot del leaderboard (MTEB), filtros aplicados (retrieval · multilingüe/español · tamaño que entra), **solo modelos abiertos** con licencia registrada, y los **detalles de uso leídos de la model card original** (prefijos o instrucción de query, normalización, dimensión, longitud máxima) — nunca un default silencioso ni parámetros inferidos por una instancia. **[LAUDO ESCRITO REQUERIDO — toca compromisos del PPF/alcance]**: bloquea la pieza (ii) de A2.0-banco y B1.10.
- [ ] A2.1 (H+I) **Pre-registro sellado** — **prerrequisito H-B2 (de A2.0-banco)**: caracterizar la semántica de `num_turns` vs `--max-turns` (disparó 14 con tope 12) y fijar el criterio de corte R5 sobre una señal verificada antes de sellar. Baseline BM25 sobre los **chunks de E0** (unidades estructurales + herencia; mismo texto que vio el extractor — el baseline no pierde por chunking tonto), top-k=5, **el mismo agente del banco A2.0 en los dos brazos** (no el harness congelado) con una sola tool de recuperación por brazo, mismo juez de fidelidad EV2, mismas 40 preguntas; brazo denso con el modelo laudado en A2.0b (chunks de E0; la variante de chunks 512 que prometía `gaps.md` queda como secundaria si hay tiempo). GraphRAG-MS: **descartado con laudo** (costo, opacidad, fuera de criterio de citabilidad). Predicciones: incorrectos, criterios cubiertos, abstenciones, latencia, costo por pregunta. **Se corre sobre el banco de A2.0-banco** (mismo agente, mismo modelo, mismo prompt, mismos chunks de E0; el brazo es el servidor MCP enchufado), con el **aislamiento verificado como precondición** y con **declaración explícita de no-comparabilidad con la tabla de EV2** (principio 8). El brazo denso **deja de ser opcional**: es el brazo RAG. **La comparación NO se rediseña** (grafo vs bolsa de chunks es la pregunta del PPF y el brazo KG puro se mantiene tal cual). Se agregan dos cosas: (a) **predicción explícita de la asimetría texto-crudo vs representación-comprimida** — el RAG recupera el texto fuente con todo su vocabulario superficial mientras el KG recupera label + descripción, y A1.4 mostró que esa superficie es el 35 % de las fallas anti-léxicas de búsqueda; (b) el **brazo híbrido** de B1.9 (nodos + texto fuente indexado por provenance) como tercer brazo, que aísla el efecto de representación con el mismo texto recuperado en los dos lados.
- [ ] A2.2 (I, ~$15) Corrida N=1 + N=3 parciales + auditoría 10 % + adjudicación simétrica (mismo protocolo EV2). **Rige el principio 7**: el baseline se diseña y sella en A2.1 (con material propio para cualquier ajuste), y se mide sobre EV2 una sola vez. **Medición única con todos los brazos** (RAG-BM25 · KG puro en su mejor config · híbrido B1.9), en una sola pasada de juez y una sola ronda de adjudicación simétrica — absorbe A1.5 si A1.7 cerró antes (ver A1.5).
- [ ] A2.3 (I, $0) Tabla head-to-head final: KG-Base · KG-Refinado · KG-Reextraído · KG-Refinado+BM25(+tools v2) · RAG-BM25 · (RAG-denso), con incorrectos, criterios cubiertos, abstenciones, latencia p50/p95, costo/pregunta, costo de construcción → **gráfico Pareto fidelidad-vs-costo** (vacío #5).
- [ ] A2.4 (H) Laudo de aplicaciones (issue #12): la app de consulta con citas + circuito de feedback **es** la aplicación demostrada (U6: 25 preguntas reales de usuarios). Caso de uso 1 (explicabilidad agéntica): **descope escrito** con justificación (priorización invertida respecto del PPF, registrada) o demo mínima de 3 cadenas sobre preguntas multi-norma de EV2 sin métrica nueva. Recomendación: descope + demo mínima solo si A1–A2 cierran en fecha. **[LAUDO ESCRITO REQUERIDO — toca compromisos del PPF/alcance]**: no arranca sin laudo redactado y fechado por la autora.
- [ ] A2.5 (I+H, ~$25) **CONDICIONAL T2 — robustez de la comparación entre grafos bajo el banco nuevo**: ¿la ventaja del esquema v2 sobre KG-Base sobrevive a un agente más fuerte? Gates para que entre: (i) A2.0-gate pasado (adaptador de trazas funcionando), (ii) A2 cerrado, (iii) calendario, (iv) **pre-registro con regla de canonicidad declarada ANTES** — la tabla canónica de «qué grafo es mejor» sigue siendo la del harness congelado (EV2, juez validado, adjudicación humana); esta medición se reporta como **robustez**, no la reemplaza, (v) una sola medición por sistema (principio 7). Si no entra, se declara como trabajo futuro con el diseño ya escrito.
Depende de: A2.0-gate → A2.0-banco (en ese orden) y A1.5/A1.7. Habilita: C (Resultados/Discusión).
Nota de nomenclatura (rastreabilidad): la unidad que hasta la v2 figuraba como **A2.0** queda
partida en **A2.0-gate**, **A2.0-banco** y **A2.0-reportes**; **A2.0b sigue siendo el laudo del
modelo de embeddings** (no se renumera, para que los commits, mandatos e issues anteriores que
citan «A2.0» y «A2.0b» sigan siendo rastreables). Toda referencia previa a «A2.0» sin sufijo se
lee como el conjunto de las tres.
Nota de multiplicidad: con 40 preguntas y varios brazos, las diferencias de 1–3 preguntas **no se leen como señal** — se reportan con IC y se dice explícitamente cuándo el n no alcanza.

### A3 · Ablación de modelo del agente — **ABSORBIDA POR A1.7** (el agente de Claude Code ya es de clase Sonnet; el contraste modelo/política se mide ahí, con material propio y sin gastar EV2). Se conserva el enunciado original como referencia:
- [–] A3.1 (I, ~$10) Sonnet como respondedor sobre KG-Refinado+BM25, mismas 40 preguntas: ¿persiste "grounded ≠ correct" (BKL-0026 3/3 con retrieval perfecto)? Si persiste, es del paradigma, no del modelo chico. Pre-registrado.

---

## Carril B — Grafo y pipeline (paralelo al carril A)

### B1 · Terminar el pipeline: E4/E5 + referencias cruzadas + provenance rica — T1 · S1–S3
Objetivo: que el pipeline nuevo sea completo, generalizable y produzca un grafo que pueda
promoverse a vigente. Todo código puro salvo lo marcado.
- [x] B1.1 (**HECHA en U-B1a**, `185e042` — paridad 70/82 con KG-Refinado; 19 nodos creados + 51 enriquecidos; 41 `padre_sugerido` flaggeadas) (I, $0) **E5 esqueleto**: portar `build_skeleton` de `grafo_v2/code/assemble.py` a `ensamblar_corpus.py` (clases + roles por TO, `subclase_de`/`miembro_de`/`instancia_de`), aristas `padre_sugerido` flaggeadas para propuestos. Hoy: 0 aristas de esqueleto.
- [x] B1.2 (**HECHA en U-B1a**, `185e042` — 43→44 propuestos: 3 resueltos por reglas declaradas (label exacto normalizado / alias declarado / slug del id / singularización por token / sigla entre paréntesis condicionada a `padre_sugerido`), 41 en cuarentena; TextoOrdenado 6→5; 2.321 conflictos = 2.125 variantes materia/version + **196 reales** persistidos sin resolver) (I, $0) **E4 determinístico**: resolución de `sujeto_propuesto` por alias normalizado contra el catálogo (`resuelto_por_alias`), filtro de ruido en conflictos de properties (`materia`/`version`), `TextoOrdenado` solo desde provenance (hoy 6 para 5 TOs). Los ~170 conflictos reales quedan registrados para E4-LLM (T3).
- [x] B1.3 (**HECHA en U-B1a**, `185e042` — 1.089 menciones → 837 resueltas (20 parciales) / 252 irresolubles (115 frontera ancla/chunk, 106 normas fuera del subset, 26 punto inexistente en E0, 4 autorreferencia, 1 anáfora); **5.645 aristas `referencia` nuevas** (188 cross-TO + 6 al TO), todas con evidencia; muestra de 30 inspeccionada por la autora **30/30 OK**; 55 menciones-rango (fan-out máx 76, mediana 15)) (I, $0) **Referencias cruzadas norma→norma** como aristas `referencia` (regex sobre "punto X.Y de las normas sobre Z" + resolución contra inventario de TOs y puntos de E0). Hoy: 0 aristas norma→norma, 113 nodos que remiten en texto. Habilita multi-hop real (debilidad compartida de la Fase 2.3) y es la capacidad que un RAG por chunks no tiene.
- [x] B1.4 (**HECHA en U-B1a**, `185e042` — 52.561 provenances enriquecidas con `chunk_id`, `paginas`, `ancestros`; 0 inconsistencias contra `estructura_<to>.json`) (I, $0) **Provenance rica**: `chunk_id`, `paginas`, `ancestros` en cada provenance (arregla la asimetría de granularidad de KG-Reextraído en censos por ancla).
- [x] B1.5 (**HECHA en U-B1a**, `185e042` — `r1_invariantes.py` 10/10; S0 reproduce el sellado byte a byte; guarda cross-TO: 23 merges (todos `Sujeto` de catálogo), 5 colisiones de contenido registradas sin fusionar (`adjudicacion_cross_to.json`)) (I, $0) `ensamblar_corpus.py`: selftest + aserciones de invariantes (conservación, unicidad, sin colgantes, provenance) + guarda de merge cross-TO (solo `Sujeto` de catálogo; el resto a registro/adjudicación — hoy 5 merges de contenido silenciosos).
- [x] B1.6 (**HECHA en U-B1a**, `185e042` — 79/80 unidades de cola ingresan con su E1 válido (`cap::4.2.1.2` sin E1 válido sigue rechazada): 394 nodos y 646 aristas flaggeados; recomputo derivado de política (0 llamadas): cola 79→68, informativo) (I, $0) Cola humana **ingresa flaggeada** (`estado_e3`) en vez de perderse (80 unidades; incluye `ext::3.9::intro`); guardia B extendida a cualquier tipo + guardia "cita = label" (recomputo sobre veredictos pagados, precedente `recompute_politica_enm01.py`).
- [x] B1.7 (**HECHA en U-B1a**, `185e042` — `salida_r1/kg.json` sha `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a`, 6.529 nodos / 17.772 aristas, doble corrida byte-idéntica, 0 colgantes, T1–T7 7/7 (T2 ahora 6 nodos en 5 puntos incluido 7.11.5, que entró con la cola). Diff: +351 nodos; `referencia` 34→5.680 (5.645 de B1.3 + 1 TO→Comunicación que entró con la cola = +5.646; el «5.645 vs 5.646» del reporte son dos cantidades distintas, no un error)) (I, $0) Re-ensamblar → **KG-Reextraído-r1** (mismos crudos de E1/E3, sin API), tests de respuesta conocida ampliados (ver B2), sha sellado. Es la primera release que llega al gate de B2.6: hasta el laudo B3.1 las intrínsecas se computan y reportan en modo INFORMATIVO, no bloquean.
- [x] B1.8 (**HECHA en U-B1.8**, sello `774acac` — tabla definitiva de r1 **6 correcto / 26 parcial / 8 incorrecto** al lado de las selladas (3/20/17 · 5/26/9 · 4/27/9); vías 11 juez_base / 21 juez_enc / 5 adjudicación base / 3 adjudicación §7; **P1–P5 6/6 cumplidas** (P1 31/40 en el borde exacto, laudo del censo; P2a ausencia 8<9 con granularidad 6<8; P2b 3<4 — la predicción central; P3 generación 19∈[18,24]; P4 techo 8∈[3,9] sin evidencia contra H17, interior rotado vista→alcanzabilidad; P5 incorrectos 8≤9); juez vs autora en muestra simétrica 4/4 y 15/15 con 0 sobre / 0 sub-acreditación (leído con la salvedad de `ev2_r1/adjudicacion/nota_episodios_adjudicacion.md`); atribución A0.2 (regla `40603a9`/`85d9fdb`): trazas base 8 ausencia / 7 alcanzabilidad / 1 vista / 19 generación / 5 correcto, los 8 incorrectos definitivos = 3 ausencia + 2 alcanzabilidad + 3 generación, replay estándar y fuerte 40/40 + 71/71; 3 desvíos del §7 declarados con evidencia (recuperación EV2F-029, retoma del juez por 503, wrapper de freno de retoma con guardia real); costo real USD 7,29 desde dbs vs ~$3 estimados, bajo tope escalonado laudado 3,5 + 5,5. **r1 es el primer grafo bajo 9 incorrectos y el de más correctos, pero dentro de la banda de no-señal contra KG-Refinado (6/26/8 vs 5/26/9; cobertura 69 vs 73)**. LAUDO DE PROMOCIÓN TOMADO 2026-08-25: r1 VIGENTE (`docs/laudo_promocion_r1_vigente.md`; migración declarada por `data/experiment/neo4j/plan_carga_r1.md`, tablero §1 se actualiza en el commit del switch); el brazo KG de A2.1 se decide en el pre-registro de A2.1 citando la tabla de `774acac`, no acá) (I, ~$3 → real 7,29) Fidelidad EV2 de KG-Reextraído-r1 (40 preguntas, mismo protocolo) → ¿supera a KG-Refinado? **Rige el principio 7**: KG-Reextraído-r1 quedó medido sobre EV2 una sola vez; B1.1–B1.7 se validan con regression suite y material propio (B2), nunca contra resultados de EV2. Insumo de la release r2 (nada se corrige en r1): 7 anclas de granularidad + 2 de contenedor del censo, más los pendientes de U-B1a.
- [x] U-MIG-r1 (**HECHA**, ejecuta el laudo `81587f9` vía `data/experiment/neo4j/plan_carga_r1.md`) (I, ~USD 0,04) Migración del vigente: r1 cargado en Neo4j bajo `:KG_Reextraido_r1` (6.529/17.772, 0 colgantes, huella loader==Neo4j, equivalencia 454/454 paridad, labels vecinos intactos, índice full-text con la definición común); `r1_vigente` primera entrada de `GRAFOS_EXPLICITOS` con adapter `r1_vista_runtime` (`_cargar_grafo()` único punto de carga, `verificar_sha` antes de servir); `tablero.md` §1 actualizado (KG-Refinado → medido/sellado, sin borrarse ni descargarse). Smoke LLM (1 turno autorizado, ≈USD 0,04): cita `Punto 6.7` verificada verbatim contra el PDF; composición por navegación estructural (`ver_vecinos` → 3 obligaciones entrantes) **sobre aristas pre-existentes en KG-Reextraído** — dato para U-APP/A2, no evidencia del salto de aristas de r1 (matiz verificado por mesa contra ambos kg.json). Registros: contradicción de mandato (USD 0 vs smoke; error de redacción de mesa, resolución del ejecutor correcta), fe de erratas de `plan_carga_r1.md` (índices en `indices.py`).
- [x] U-APP (**HECHA**, sello `dcab8e6`, I, real USD 0,028509) **Deudas de la app saldadas**: (1) consecuencia app del laudo A1.6 (`89055c5`) implementada — `GraphAgentNeo4j` `modo='fulltext'` como default (`r1_vigente` y `v3_vigente` contra su label e índice; run_1..run_5 siguen GraphIndex), fallback declarado en DOS niveles (arranque y runtime, `backend`/`backend_motivo` en `/runs`, flag de prueba sin tumbar el contenedor), ambos estados demostrados y re-verificados por mesa; `_ToolLogMixin` conserva el registro de tool calls; cuarteto/`grafos.py`/`neo4j_index.py`/`llm_backend.py` byte-intactos (el harness ya capturaba usage por llamada — la instrumentación lee de la traza). (2) usage por turno en el jsonl de sesiones: tokens crudos por llamada + agregado, SIN USD hardcodeado, retrocompatible (formato viejo se sigue leyendo; `backend_grafo` aditivo, `backend` LLM intacto para `adaptador_sesiones.py`); 5 tests nuevos (`app/test_u_app.py`). Smoke con backend fulltext: misma pregunta que U-MIG-r1, costo REAL desde usage persistido **USD 0,028509**, reproducible desde los tokens crudos del turno —**20.134 de entrada, 1.675 de salida, sin cache**, a tarifas de `harness.py:53-56` (1,00 y 5,00 USD/MTok)— anotados acá porque el jsonl que los respalda está gitignoreado (tope 0,10). En cola (cosmético, anotado): deduplicación de citas repetidas en la respuesta de la app. **Deuda declarada (deploy)**: el venv del EC2 no tiene el driver `neo4j` → hasta instalarlo (+ servidor accesible) el deploy serviría en `graphindex/fallback` declarado; **acción: instalar el driver ANTES del pull, y smoke con backend Bedrock después del pull**. **Deuda de mesa SALDADA (27/08)**: verificación cruzada por recomputo independiente contra disco en `dcab8e6` — **7/7 ítems coinciden, sin divergencias** (sellos del cuarteto + `grafos.py`/`neo4j_index.py`/`llm_backend.py` idénticos a `dcab8e6^`; default de backend leído del código y ejecutado en `/runs`; fallback en dos niveles demostrado con el flag existente sin caer el servicio; usage crudo sin USD y retrocompatibilidad verificada incluido `adaptador_sesiones.py`; 5/5 tests; costo recomputado 0,028509; alcance de `dcab8e6` = 4 archivos de `app/` + plan, y de `966253e` = solo `docs/`). **Deuda del venv del EC2: declarada y NO confirmada** —no verificable localmente—, se verifica en el propio EC2 antes del pull. **Deuda anotada (no bloquea el pull)**: la suite de la app son los 5 tests nacidos con U-APP; **no hay regresión sobre el comportamiento previo** de la app.
- [ ] B1.9 (I, $0) **Capa de texto fuente indexada por provenance** — el grafo ya tiene el puntero exacto al chunk de E0 y hoy solo lo usa para citar. Indexar el **texto del chunk** y rutear los hits a los nodos que lo declaran en su provenance, como índice adicional del retriever (determinístico, sin LLM). Motivación medida (A1.4): 7 de las 20 fallas anti-léxicas son «nunca vista» porque la representación comprimida (label + descripción) perdió el vocabulario superficial que la pregunta usa. Se declara siempre como **brazo híbrido**, nunca como «el KG»; se mide sobre pares frescos (nunca EV2) y entra como tercer brazo de A2.
- [ ] B1.10 (I, ~$0–2) **Embeddings sobre los nodos del KG** (índice denso HNSW en Neo4j) y **retriever híbrido BM25 + denso**, con `harrier-oss-v1-0.6b` (laudo A2.0b) y **pares frescos** (los v3 ya se usaron para medir y para elegir). Justificación medida, no intuición: A1.4 refutó P2 — lo léxico no cierra una brecha semántica; las 7 anclas «nunca vistas» son el blanco. Se mide sobre pares frescos (nunca EV2) con el mismo instrumental de A1.4, y si gana entra como configuración del brazo KG en A2. Complementa a B1.9 (texto fuente por provenance): uno recupera la superficie, el otro la semántica.
**Pendientes de laudo que deja U-B1a (insumo de B1.8/B2 y de la release r2, principio 9 — nada de esto se corrige en r1):** (a) rangos «puntos X.1 a X.n»: hoy se expanden a todos los nodos de cada punto; alternativa rango → contenedor común con fallback a expansión; (b) 196 conflictos reales de properties (E4-LLM futuro); (c) 5 adjudicaciones cross-TO de contenido (4 Operacion + 1 Obligacion); (d) 41 `padre_sugerido` flaggeados; (e) recomputo de política de cola (79→68) como informativo. **Prerrequisito de carga en Neo4j**: entrada de r1 en `data/experiment/neo4j/grafos.py` (path `corpus_v2/salida_r1/kg.json`, sha `0226e947…`) antes de cualquier `cargar_kg.py`.
Depende de: nada. Paralelizable con A0/A1 (directorios disjuntos).

### B2 · Refinamiento generalizable: del parche manual a la regression suite — T1 · S2–S3
Objetivo: que "refinar" signifique arreglar el pipeline y re-correr, no editar el grafo.
- [ ] B2.1 (I, $0) `scripts/regression_kg.py`: convierte cada BKL cerrado (C1–C7, BKL-0024/0025, RT-*), los tests T1–T7 de r1 **y las reglas declaradas de E4** (resolución de propuestos por label exacto / alias declarado / slug / singularización por token / sigla condicionada; TextoOrdenado solo desde provenance; materia/version como variantes) en **tests de respuesta conocida determinísticos** ejecutables sobre cualquier `kg.json` (nodo presente / ancla / valor / arista / rank en `buscar_nodos`). Salida: tabla defecto → resuelto/persiste — **entregable transferido explícitamente desde el issue #9 (cerrado en U-C0.1) a esta sub-tarea**.
- [ ] B2.2 (I, $0) `scripts/shapes_validator.py` a esquema v2 (unidad 2 del tablero, pendiente desde julio): shapes de dominio/rango, provenance obligatoria, sujeto en catálogo o cuarentena. **Desde U-B1a**: extender `DOMAIN_RANGE`/shapes para `referencia` nodo→nodo y `padre_sugerido` (hoy fuera del esquema; las aristas llevan `rol_fuente`), y **todo test o shape que lea «el punto de un nodo» debe usar el conjunto de provenances, no `provenance[0]`** (138 aristas `referencia` cuyo destino exacto ≠ `provenance[0]` del nodo destino por fusión).
- [ ] B2.3 (I, $0) Correr regression + shapes sobre KG-Base, KG-Refinado, KG-Reextraído, KG-Reextraído-r1 → tabla en Resultados.
- [ ] B2.4 (H) Laudo de los 15 BKL `triaged`: 9 son de asignación de sujeto (descenso/estrechamiento/clase forzada) → **una** corrección sistemática vía prompt/validador de E1 (no vía edición del grafo), verificada por B2.1; 4 de alcanzabilidad → A1; 2 de modelado (BKL-0020/0021) → laudo; BKL-0018 → anotación de régimen.
- [ ] B2.5 (I) Actualizar `docs/spec_backlog_refinamiento.md`: el circuito pasa a tener dos vías (parche sellado sobre vigente / corrección en pipeline + re-extracción + regression) y cuándo se usa cada una. Campo nuevo obligatorio en cada entrada: `capa_pipeline` ∈ {E0, E1-prompt, E1-validador, catálogo, E2, E3, ensamblado, retriever, agente} — la entrada nombra la REGLA a corregir, no el nodo.
- [ ] B2.6 (I+H, $0) **Protocolo del ciclo de refinamiento a nivel pipeline ("releases")** — `docs/protocolo_ciclo_refinamiento.md`: síntoma (regression fallida / 👎 app / pregunta fresca / intrínseca fuera de umbral) → atribución (determinística de primer nivel A0.2; verificador solo sobre muestra priorizada) → entrada de backlog con `capa_pipeline` + test nuevo en la regression suite → cambio en el pipeline → re-corrida cache-aware (E0/E2/ensamblado $0; E1/E3 pagan solo si rota el prefijo → los cambios de prompt/catálogo se agrupan en releases) → **gate de release** = regression suite + shapes v2 + intrínsecas con umbrales (B3) + material propio (pares sintéticos con semilla nueva, preguntas frescas tipo U6) — nunca EV2 (principio 7). Hasta el laudo B3.1, las intrínsecas participan del gate en modo INFORMATIVO (se computan y reportan en cada release, no bloquean); pasan a bloqueantes recién con umbrales laudados → laudo → grafo versionado (KG-Reextraído-r2, r3…) con sha, tabla regression, intrínsecas y costo → promoción a vigente / carga en Neo4j. Doble vía explícita: el **hotfix** sellado sobre el vigente sigue existiendo (la app no espera una re-extracción), pero nace con su test en la regression suite, así la próxima release lo resuelve por diseño o falla el gate. Declara qué NO escala (adjudicación humana de veredictos, gold, verificador fuera de familia) y cómo se acota (muestras priorizadas por frecuencia de síntoma y territorio).
- [ ] B2.7 (H+I, ~$25) **Gate chico del verificador en la familia gen-3** (KG-Reextraído / KG-Reextraído-r1): 4 casos con vara sellada, criterio cero-silenciosos + ≥3/4 (mismo protocolo que U5, `docs/protocolo_gate_u5.md`). Sin esto el Motor 3 no puede diagnosticar sobre el grafo que va a ser el vigente. Se combina con A0.3 (misma muestra) para no pagar dos veces.
- [ ] B2.8 (I, $0) **`docs/metodo_construccion_refinamiento_kg.md`** — el método completo, de PDF a grafo vigente y su mantenimiento, escrito como especificación reutilizable (entradas, etapas E0–E5, gates, regression, releases, retriever, intake, roles humano/máquina, costos por etapa) con puntero al experimento que demuestra cada mecanismo (§6 de este plan). Es el documento que la tesis convierte en capítulo de Metodología y el que se sigue en B6.
- [ ] B2.9 (I, $0) **Detector de huérfanos de label** como chequeo determinístico de la regression suite (B2.1) y de shapes (B2.2): un nodo es huérfano de label si ningún token de contenido de su label lo trae al top-10 con `buscar_nodos` booleano (definición ya codificada en el muestreo de A1.3). Evidencia de que es defecto **del grafo** y no del retriever: P6 de A1.4 — BM25 no los ve y las tools v2 no los rescatan. Corrección en el pipeline, no a mano: regla de label distintivo en E1/E5 y/o campo `terminos` derivado del texto fuente (**nunca inventado**), verificada por el propio detector.

### B3 · Métricas intrínsecas pasada 2 (spec §8) — T2 · S3
- [ ] B3.1 (H) Laudo de umbrales de M2/M3/M7/M10 (bloqueantes) — sobre la evidencia de la pasada 1.
- [ ] B3.2 (I, $0) Correr M1–M11 sobre KG-Base, KG-Refinado (post-C7), KG-Reextraído y KG-Reextraído-r1; M11 (cobertura CQ) sobre las anclas de EV2 (régimen especial: medición única, no bloqueante). Alias de industria (compression ratio / false merge rate) como columnas.
- [ ] B3.3 (I, $0) Propuesta pre-registrada de **M12 densidad de referencias cruzadas**, **M13 completitud de provenance** y **M14 solapamiento léxico entre label+descripción y el texto fuente** (aditivas a la spec, con laudo). M14 sale de A1.4: es la candidata a predecir alcanzabilidad anti-léxica y el mejor puente intrínseco↔extrínseco para B3.4.
- [ ] B3.4 (I) Cruce intrínseco ↔ extrínseco (EV2): ¿alguna métrica intrínseca predice fidelidad? Tabla + hallazgo (probablemente "no, y eso es el punto": P-b).

### B4 · Evaluación intrínseca a nivel tripleta: precisión, importancia y recall (promesa "no negociable" del PPF) — T1 · S4–S5
Objetivo: medir la **calidad de extracción** del grafo a nivel tripleta sin adjudicación manual
masiva, con dos vías separadas y un juez LLM calibrado contra adjudicación humana. **Secuencia: D-f, laudo firmado 27/08/2026** (`docs/laudo_D-f_secuencia_tripletas.md`; el planteo original ofrecía dos escenarios excluyentes E1/E2, superados por el principio 10): el instrumento se construye y valida sobre **KG-Reextraído-r1** —conjunto de desarrollo, donde se itera sin restricción y donde el juez queda calibrado y el protocolo probado— y la **medición que cuenta para la tesis** se corre una única vez sobre el **grafo escalado**, dentro de la evaluación final pre-registrada (B6.3), porque el objeto de la tesis es el recurso final. B4.1 (el diseño) avanza igual y debe declarar el doble rol. Reemplaza el diseño anterior de anotación ciega
de tripletas gold sobre 25 unidades.
- [ ] B4.1 (H+I, $0) **Diseño sellado** (`docs/preregistro_evaluacion_tripletas.md`). **Dos
  requisitos incorporados por decisión de la autora desde la consolidación de related work
  (`docs/mapa_related_work.md` §2)**: el pre-registro DEBE incluir (i) **intervalos de Wilson
  para toda proporción reportada** (exigencia 4 del mapa; precedente YAGO, Tabla 1 — robusto en
  muestras chicas, y hoy el repo reporta fracciones peladas) y (ii) la **desagregación de la
  precisión por etapa del pipeline E0–E5**, además de por tipo de relación y por TO (exigencia
  5; la provenance de r1 —`chunk_id`, `paginas`, `estado_e3`— y el campo `capa_pipeline` de
  B4.4 lo vuelven barato; precedente YAGO: precisión por heurística de extracción). Contenido:
  (a) **vía
  de precisión** — muestra aleatoria con semilla de **100 tripletas del grafo** (estratificada
  por tipo de relación y por TO), presentadas como nodo–relación–nodo **+ evidencia** (el texto
  fuente que la provenance señala; con B1.4, chunk y páginas), con dos juicios por tripleta:
  **correcta** (la evidencia la sostiene: sujetos, valores, calificadores, modalidad) e
  **importancia** (escala corta declarada: ¿merece estar en un KG regulatorio?); (b) **vía de
  recall** — de una muestra de fragmentos de E0 (párrafos/unidades chicas, donde un LLM no se
  pierde: ≤ 5–10 cláusulas), un LLM extrae **la tripleta más importante que no puede faltar**
  en un KG de regulación; otro LLM **rankea** el conjunto por importancia; la **presencia en el
  grafo** se decide por regla declarada (match de sujeto/objeto normalizados + relación, con
  política de descendientes explícita — ver hallazgo de la frontera ancla/chunk) → **recall@k
  sobre el ranking de importancia**; (c) **juez LLM** con prompt congelado por sha, N=3 modal,
  ciego al grafo de origen; (d) **calibración**: la autora adjudica primero **de a 10** hasta
  100 (correctitud + importancia) y, aparte, valida el **orden** de las top-100 del ranking;
  acuerdo juez–humana medido en ambas direcciones (mismo patrón que el juez de fidelidad EV2);
  el juez escala al resto solo si el acuerdo lo habilita, con umbral declarado; (e) las
  tripletas **ausentes** del grafo van a adjudicación **post hoc** (¿importaba o no?) — lo
  presente no se adjudica; (f) categorización asistida por LLM de dificultad/experticia para
  priorizar qué adjudica la autora; (g) material: fragmentos **frescos** (no los chunks cuyas
  anclas ya están quemadas por EV2/sintéticas), EV2 no se abre; (h) predicciones con umbral y
  tope de costo. **[LAUDO ESCRITO REQUERIDO — toca compromisos del PPF/alcance]** (D-b).
- [ ] B4.2 (H) **Adjudicación humana**: 100 tripletas de precisión (correctitud + importancia)
  y orden de las top-100 de recall, en tandas de 10 con freno tras la primera tanda para
  ajustar la ficha (no el juez). Sellado por commit antes de correr el juez sobre el resto.
- [ ] B4.3 (I, ~$10) **Juez calibrado y corrida**: acuerdo juez–humana; si pasa el umbral,
  juez sobre la muestra ampliada (precisión) y sobre el ranking completo (recall);
  presencia en el grafo por regla; **precisión@100 (correctas), precisión ponderada por
  importancia, recall@10/50/100 del ranking de importancia**, por tipo de relación y por TO;
  adjudicación post hoc de las ausentes importantes. Todo con replay determinístico de la
  regla de presencia y costo desde tokens.
- [ ] B4.4 (I, $0) **Lectura y cruce**: lista de ausencias importantes → entradas de backlog con
  `capa_pipeline` (insumo de la release r2 = grafo post-evaluación, principio 9); cruce con
  EV2 (¿las ausencias explican fallas de fidelidad?) y con M1–M3/M12–M14 (B3.4). Publicable
  como dataset (C2).
Si el tiempo no da: laudo escrito de reducción (50 tripletas de precisión, top-50 de recall)
— nunca silencio. Depende de: B1 (KG-Reextraído-r1). Habilita: B2.6 (release r2), B6.3, C1.6.

### ESQ · Validación del esquema ANTES del escalado — **T1 · BLOQUEANTE de B5/B6**
Origen: reunión de mentores del 26/08/2026. El esquema actual se diseñó mirando únicamente los
cinco TOs del subset; antes de aplicarlo a todo el corpus hay que medir cuánto se le escapa,
porque una vez escalado **volver atrás es inviable** (costo de re-extracción del corpus completo).
Dos evaluaciones independientes sobre documentos **fuera del subset**, en este orden (la ciega
primero, para que el análisis cualitativo no contamine el conteo), y un gate que las lee.
- [~] ESQ-1 (I, **tope USD 9,00 laudado** — presupuesto 6,38, cota alta 7,14, a re-presupuestar
  con el recargo medido del control, D7) **Test ciego de generalización del esquema** — diseño
  LAUDADO en `docs/laudo_ESQ-1_diseno.md` (`94bb7a7`) y pre-registro SELLADO (`38be6e5`, cinco
  predicciones P1–P5): correr el extractor en **modo (i) con canal abierto**
  (`tipo_propuesto`/`predicado_propuesto`, calcados de `sujeto_propuesto`) sobre **10 documentos
  nuevos** del universo **`escalado_prep/`** (corrección D3 del laudo: NO `data/raw` — allí 3.171
  PDFs no cruzan contra el inventario y 62 de 152 TOs producen cero unidades), sorteo
  estratificado con semilla 20260827 (762 unidades, 254 páginas), **lectura absoluta con brazo D
  pareado** (20 unidades de desarrollo re-corridas sin el atajo del rol, D5). El punto de diseño
  del «cero por construcción» quedó RESUELTO por el laudo D1 (canales cerrados: 0 de 8.009
  entidades validadas y 2 de 11.827 relaciones crudas fuera de esquema; el único canal abierto
  disparó 56/39 en crudo) y la fe de erratas `7072626` fijó que **la medición lee del bloque
  crudo** (el validado descarta propuestas por motivos ajenos a la propuesta, sesgo hacia banda
  A); se reportan los dos números y la brecha es un dato. Criterio de lectura sellado: bandas
  §7.4 + regla de normalización §7.5 (D9, no calibradas); un cero solo se lee tras control
  aprobado; banda A obliga a revisar el instrumento antes de aceptarla. **Registro obligatorio**:
  los IDs de los 10+10 documentos al archivo versionado
  `data/experiment/esq/documentos_excluidos_esq.json` (ver nota de alcance del bloque).
  **Sub-unidades, secuencia fijada por el pre-registro `38be6e5` y corregida por `7072626`
  (instrumento → canal abierto → control → corrida):**
  - [x] U-ESQ-1a **instrumento de cadenas distintas** (HECHA, `181e262`): lista pelada sin
    frecuencias/origen/spread, selftest 24/24 con ancla de datos reales.
  - [x] U-ESQ-1a-bis **extensión a bloque crudo** (HECHA, `56c601d`):
    `CANALES` por pares (bloque, canal), `--bloque` obligatorio sin default, selftest 52/52 con
    anclas crudo 56/39 y validado 54/38, brecha exacta verificada, mutación de control del
    centinela.
  - [x] U-ESQ-1b **canal abierto** (HECHA, `8f52f3b`): `tipo_propuesto`/`predicado_propuesto` en
    prompt + tool schema + normalización del validador (el validador NO filtra la medición: se
    lee del crudo, fe de erratas `7072626`); namespace de caché aislado; rige
    `docs/decisiones_caching_extraccion.md`. Lista «anotado sin tocar» registrada en la entrada 4
    de `docs/cola_mejoras_diferidas.md`.
  - [x] **U-ESQ-1c — Control de instrumento** (HECHA; commit de cierre + diagnóstico `d6527a6`):
    **P1 FALSADA** — A 0/20 (≥10), B 3/10 (≥7), C 0/10 pasa; resultado NULO por banda sellada;
    USD 0,4223. Diagnóstico (U-ESQ-1c-diag): comparabilidad verificada (modelo pineado),
    clasificación MEZCLA — brazo A con premisa mala pre-declarada, brazo B con pool contaminado
    por re-expresabilidad, bug objetivo de la description del tool.
  - [x] **U-ESQ-1d — Control rediseñado P1′** (HECHA; adenda sellada `e68e861`; sello del cierre
    `c25273f`): description corregida solo en modo
    abierto (cerrado byte-idéntico), 10 dopadas aprobadas por la autora (1 reemplazo por colisión
    con canal vecino), corrida USD 0,1836. **P1′ FALSADA** — A′ 0/10 (tipo 0/5, predicado 0/5),
    C 0/10 pasa. **Hallazgo central: deformación semántica** (ver abajo). Recargo D7 re-medido:
    **lectura GLOBAL adoptada por la autora como número PROVISORIO** (+18,6 % → re-presupuesto
    ESQ-1 USD 6,51; se reemplaza por el medido bajo el prefijo de O2).
  - [x] **U-ESQ-1e — O2: neutralización de los cierres** (HECHA, sello `0e50e3d`; adenda P1″
    sellada `6cb0121`): cambio de una sola variable verificado (fixtures por sha, diff del system
    = exactamente los dos reemplazos, cerrado byte-idéntico). **P1″ FALSADA — A′ 0/10 (tipo 0/5,
    predicado 0/5), C 0/10 pasa**: con los cierres neutralizados y la instrucción explícita de
    emitir por el canal, el modelo volvió a forzar las 10 cláusulas. Sub-hallazgo: la deformación
    es INESTABLE entre corridas (3/10 cambiaron de caja errónea; una perdió el umbral que la
    corrida anterior había capturado). USD 0,18396. **ESCALERA CERRADA por adenda §5.c.**
  - **DECLARACIÓN FORMAL (autora, 31/08/2026): ESQ-1 en modo (i) es IRREALIZABLE tal como fue
    pre-registrado.** El pre-registro `38be6e5` queda **FALSADO-CERRADO**: P1, P1′ y P1″ falsadas
    en escalera sellada (commits de U-ESQ-1c, `c25273f`, `0e50e3d`); P2–P5 nunca corrieron y
    quedan sin leer; la demostración de la escalera —el canal declarativo es inviable con este
    modelo y este prompt— es el resultado. Saga completa del control: USD 0,79 de tope 9,00. El
    re-presupuesto D7 (lectura global 6,52, sostenida por la autora) queda como **número
    dormido**: solo revive si el censo revive por la rama (a) del árbol de U-ESQ-2-cal.
  - [x] **U-ESQ-2-cal — Control del instrumento de descubrimiento (modo ii)** (HECHA, sello
    `eadf4a5`; pre-registro `bca863f`): instrumento nuevo calibrado contra la vara sellada (10 dopadas de
    `c25273f` por sha + 10 limpias de C), manifiesto del prompt aprobado por la autora con
    contrato sha-bound, corrida 20/20 en USD 0,1297 de tope 0,50, modelo resuelto
    `claude-haiku-4-5-20251001` en las 20 llamadas, adjudicación de la autora fila por fila
    (`data/experiment/esq/control/adjudicacion_descubrimiento_cal.md`). **P-cal FALSADA por su
    segunda mitad**: A′ 9/10 PASA (tipo 4/5, predicado 5/5, 0 cruces — capacidad demostrada:
    el modelo ve y nombra lo plantado cuando descubrir es la única tarea) pero **C 7/10 con
    espurias (umbral ≤1/10) NO PASA** — inunda de falsos positivos el texto limpio: un censo
    habría SOBRECONTADO la deriva; el brazo C existía para esto. **RAMA (b) DECLARADA por el
    árbol sellado: el censo por LLM queda CERRADO con este modelo, con DOBLE evidencia —
    extrayendo deforma (escalera P1/P1′/P1″), descubriendo sobrecuenta (P-cal)**. El D7 global
    6,52 pasa de dormido a **MUERTO**. Sub-hallazgo en limpias: facultades discrecionales
    REALES en texto de producción (veedor, extensión de plazo, permiso adicional, códigos de
    consolidación) — el hueco de potestades pasa de hipótesis plantada a hallazgo en corpus
    real → C1.7 y ESQ-3.
  - [x] **Resolución del árbol: RAMA (b)** — ESQ-2 protocolizada es la única vía; no hay censo.

**HALLAZGO — deformación semántica: conforme-al-esquema ≠ fiel (U-ESQ-1d; alcance propio, va a
ESQ-3 y C1.7).** En el control P1′ el modelo leyó las 10 cláusulas plantadas y las extrajo
TODAS forzadas dentro del esquema: ni una omisión (regla de omitir desobedecida) ni una
propuesta (canal desobedecido) — re-tipado semánticamente erróneo (sanción→Excepcion,
presunción→Restriccion, facultad→Obligacion) y relaciones sin firma posible **nominalizadas
como entidades válidas** conectadas con predicados válidos. El esquema no filtra el contenido
que no encaja: **lo deforma en extracciones esquema-conformes**, invisibles justamente porque
validan. **Sub-hallazgo (U-ESQ-1e, `0e50e3d`): la deformación es INESTABLE** — mismo modelo,
misma unidad, distinta caja errónea entre corridas, con pérdida no determinística de detalles
(un umbral capturado en una corrida desapareció en la siguiente): el contenido deformado no
tiene siquiera una firma estable que lo delate. Implicación declarada: el grafo de producción
puede contener contenido fuera-de-esquema deformado en cajas válidas. **Ampliación (U-ESQ-2-cal,
adjudicación de la autora): el hueco de POTESTADES pasa de hipótesis plantada a hallazgo en
producción** — facultades discrecionales reales de la autoridad detectadas en texto limpio del
corpus (designación de veedor, extensión de plazo, permiso adicional, códigos de consolidación):
la categoría deóntica de permiso/facultad no existe en el esquema y su contenido real está en el
corpus → tratamiento en ESQ-3, conclusión de diseño en C1.7. Es el hermano del hallazgo rector (grounded ≠ correct → conforme ≠
fiel) y es candidato a resultado central del capítulo del esquema (C1.7), con su tratamiento
operativo en ESQ-3 y la posible protocolización de detección en ESQ-2.
- [~] ESQ-2 (H+I) **Test de cobertura del esquema, PROTOCOLIZADO** — desde la rama (b) del
  árbol de U-ESQ-2-cal es **la única vía** de evaluación de cobertura (el censo por LLM quedó
  cerrado con doble evidencia). Gobernado por tres documentos sellados: el laudo
  `docs/laudo_ESQ-2_diseno.md` (`8dea823`: tope propio USD 6,50 del remanente D6; extracción
  E1-solo PROVISIONAL pre-B5.4 con **cota superior de omisiones declarada**; corrección D4 —
  el universo son **los 10 TOs del sorteo sellado de ESQ-1**, los 10 originales de ESQ-2
  quedan VÍRGENES para B6.3: se queman 10 documentos, no 20), el pre-registro
  `data/experiment/esq/prerregistro_esq2.md` (`2240c9c`: gate de paridad como precondición;
  muestra 38 azarosas + 37 dirigidas; firmas (a)–(g) — que incorporan las tres firmas de la
  entrada 9 de la cola, la lección de falsos positivos de U-ESQ-2-cal y las potestades como
  familia (d); ficha pareada con DUDA como categoría propia; Wilson con alcance declarado solo
  sobre la azarosa; criterio de decisión de ESQ-3 sellado NO CALIBRADO) y la fe de erratas de
  ranking `data/experiment/esq/fe_erratas_prerregistro_esq2_ranking.md` (`930f289`).
  - [x] **U-ESQ-2 — gate + extracción + muestra + fichas** (HECHA, sello `a7788c1`): gate de
    paridad por caché **10/10 hits, 0 misses, USD 0** (validación recomputada == persistida);
    extracción E1-solo **762/762 unidades** de los 10 TOs a **USD 4,1079** (estimación 5,04,
    tope 6,50; modelo resuelto `claude-haiku-4-5-20251001` en las 762; db propia ignorada por
    el `.gitignore` de `esq/` con 22 sellos sha256 versionados);
    `documentos_excluidos_esq.json` creado (10 IDs, sha 10/10 contra manifest). Hallazgo de
    ejecución: la regla de ranking sellada degeneró en **36/37 dirigidas en un solo TO**
    (actgar, alfabéticamente primero en `chunk_id`); el ejecutor la implementó literal y
    reportó sin desviarse → corregida por la fe de erratas `930f289` ANTES de toda lectura
    (**round-robin anidado disparador × TO**; ventana declarada: cero fichas leídas, azarosa
    intacta). Muestra final 75 = 38 azarosas (sorteo semilla 20260901, **reproducido
    independientemente por la mesa**) + 37 dirigidas sobre los 10 TOs (máximo por TO 14/75,
    cegado de origen restaurado); worksheet de 75 fichas auto-contenidas con 75/75 marcas null
    y **sin marca de origen**; selftest 28/28 (incluye 5 checks anti-monopolio). **Saga ESQ
    acumulada: USD 5,03 de tope 9,00.**
  - [ ] **Lectura de la autora** (H, $0): tandas de 10–15 con
    `data/experiment/esq/code/leer_fichas_esq2.py`; checkpoint de ritmo tras la primera tanda
    (ajuste de N solo por laudo declarado) → **spot-check de mesa 10/75** → tabla de
    resultados con Wilson (solo la azarosa generaliza; la dirigida se reporta aparte y nunca
    promueve sola) → salida: inventario de huecos con cita al texto que los revela, insumo
    directo de ESQ-3.
- [ ] ESQ-3 (H+I, $0) **Gate: lectura conjunta + retoques + laudo de esquema congelado**. Lee
  ESQ-1 y ESQ-2, decide los **últimos retoques** del esquema (agregar/renombrar/fusionar tipos y
  relaciones, con su justificación) y emite el **laudo de esquema congelado**: versión final
  pre-escalado, con sha, que es la que se aplica al corpus completo. **[LAUDO ESCRITO REQUERIDO —
  toca compromisos del PPF/alcance]**. Ningún ítem de B5/B6 arranca sin este laudo.
  Checklist del gate: [ ] **cola de mejoras diferidas revisada** (`docs/cola_mejoras_diferidas.md`
  — resuelve o re-difiere con destino explícito las entradas 2, 3, 4 y 7, y se pronuncia sobre
  la 5).
**Secuencia corregida para el bloque de régimen informativo** (U-B5.6-0; reemplaza el orden implícito «parser de tablas → decisión sobre el bloque», que la fe de erratas `docs/fe_erratas_D10_causa_regimen_informativo.md` desarma). Cuatro piezas, en este orden, cada una con su justificación propia:
- [ ] ESQ-RI-1 (I, $0) **Modo de lectura sin raíz de sección**: la causa proximal del cero es la compuerta de rol de página de E0 (`e0_lib.py:206-207`: sin página de índice previa, todas las páginas quedan en `portada`), y 47 de 53 TOs están en esa condición. Desbloquea **44 de 53**. Es lo primero porque sin esto ninguna otra pieza puede siquiera medirse sobre el bloque. Caso aparte a tratar con remedio propio: 1 TO que sí llega a cuerpo y produce cero por no tener ninguna línea con formato de sección.
- [ ] ESQ-RI-2 = **B5.6** (parser de tablas). Alcanza al 12,4 % de las palabras del bloque y a 23 de 53 TOs; **se construye igual aunque el bloque quede afuera**, por RX-10 sobre normativa general.
- [ ] ESQ-RI-3 (H+I) **Extensión del esquema como pieza propia**, no como ajuste de otra unidad: sin ella la familia mayor del bloque —71 % de sus páginas— no tiene representación posible (ver hallazgo del modelo de datos, abajo). Requiere laudo, porque cambia el esquema.
- [ ] ESQ-RI-4 **Ciclo ESQ del bloque** (su propio ESQ-1/ESQ-2/ESQ-3), exigido por el laudo `94bb7a7` §D10 antes de que el esquema se congele para esa familia.

**HALLAZGO — el modelo de datos no admite hechos con valor (alcance propio, excede al régimen informativo).** Descubierto por U-B5.6-0 y verificado por mesa contra el tool schema. El esquema vigente no puede representar el contenido del bloque, y falta en **dos lugares independientes**: (a) **no hay tipo de entidad para el sujeto de una fila informativa** — los seis tipos son `Obligacion`, `Restriccion`, `Excepcion`, `Operacion` (deónticos y operacionales) más `TextoOrdenado` y `Comunicacion` (contenedores documentales), y una partida contable no es ninguno; forzarla es exactamente lo que el prompt de extracción prohíbe (`prompt_e1.py:134`: «Es preferible no extraer algo a forzarlo en una caja equivocada»); (b) **las relaciones no admiten valor** — el tool schema de `relations` no tiene campo `properties` y declara `additionalProperties: false` (`prompt_e1.py:232-257`), y los 12 predicados son binarios sin atributo, de modo que un hecho del tipo «esta partida pondera al 0 %» **no tiene dónde vivir**. Las entidades sí tienen `properties`; las relaciones no. **Esto no es una limitación del régimen informativo sino del modelo de datos**, y reaparece en cualquier norma que fije un valor —un ponderador, una alícuota, un plazo asociado a un caso—, incluida la normativa general ya extraída. **Candidato a conclusión de diseño de la tesis** (limitación bien argumentada = contribución, no disculpa): qué puede y qué no puede representar un KG de propiedad-valor sobre normativa cuantitativa, y qué costaría admitir hechos n-arios. Se decide su tratamiento en ESQ-RI-3 y en la escritura de C1.7.

**Nota de alcance y fuga al conjunto de test (principio 10).** ESQ mide el **esquema**, no la
calidad del grafo: no es una evaluación de fidelidad ni sustituye a B4, y **no consume el conjunto
de preguntas del test** (no se evalúan respuestas sobre estos documentos, se inspecciona la
extracción). Pero **sí traslada sus documentos al conjunto de desarrollo a efectos del
esquema**: ESQ-3 retoca el esquema en función de lo que esos documentos revelan, de modo que el
esquema final ya los vio. **Corrección D4 del laudo `8dea823`**: ESQ-2 reutiliza los 10 TOs del
sorteo sellado de ESQ-1 (universo que había quedado muerto sin correr) y los 10 originales de
ESQ-2 quedan vírgenes — **se queman 10 documentos, no 20**. Consecuencia obligatoria: esos 10
documentos quedan **excluidos de la evaluación final** (B6.3) y sus IDs se registran en el
archivo versionado
`data/experiment/esq/documentos_excluidos_esq.json`, que B6.3 cita al construir su eval set. Los
documentos siguen entrando al grafo escalado —lo que se excluye es su uso como material de
evaluación final—, y esa exclusión se declara en el reporte de B6.3.
**Cola de mejoras diferidas**: todo lo que este bloque encuentra y decide no corregir para no
contaminar la medición se registra en `docs/cola_mejoras_diferidas.md`; ningún gate cierra sin
revisarla.

### B5 · Escalado: endurecimiento y prerrequisitos (issue #6, #11) — **T1** (ruta crítica desde la reunión del 26/08; era T2) · S4–S5
La cola de lo diferido-para-no-contaminar que este bloque debe absorber antes de escalar vive en
`docs/cola_mejoras_diferidas.md` (regla: defectos del objeto medido se corrigen después de medir
y antes de escalar).
- [ ] B5.1 (I, $0) A1: parametrizar runner/E2/ensamblado por manifiesto (hoy cableado a 5 TOs; `censo_oraculo[to]` → KeyError; `LIMITACIONES_E0` hardcodeado; `ROL_POR_TO` con 5 keys); modo E2 sin oráculo. **Gancho de infraestructura (anotado, NO es compromiso de construirlo)**: la parametrización debe **contemplar la posibilidad** de construir un índice de fragmentos sobre el corpus escalado —el insumo que requeriría un eventual brazo comparativo en B6.3 (ver su regla de admisibilidad)—, porque dejar el gancho ahora es mucho más barato que agregarlo después. Si el brazo no se corre, el gancho queda sin usar y no cuesta nada.
- [ ] B5.2 (I, $0) A3: regex de E0 (`Sección N[.:]`, `Índice` sin guiones con guarda) → paridad 5/5 byte a byte + selftest 57/57 obligatorios; health-check por TO (`(cid:NN)`, páginas sin Sección). **CORRECCIÓN medida (U-B5.6-0, `docs/fe_erratas_D10_causa_regimen_informativo.md` §b): B5.2 NO desbloquea el bloque de régimen informativo.** En esos documentos la palabra que el regex busca no aparece —no hay marcador que relajar— y en un caso su única aparición es prosa sobre «índices de actualización», que un regex más laxo tomaría como marcador falso. B5.2 se mantiene por lo que fue escrita (paridad sobre normativa general y health-check); lo que desbloquea el bloque es el modo de lectura sin raíz de sección (ESQ-RI-1).
- [ ] B5.3 (I, $0) A4/A5: `max_tokens` con reintento 16k→32k en el mismo pase; sub-chunking por ítems para TOs nuevos; no cerrar fase con errores reintentables; tope compartido entre clientes.
- [ ] B5.4 (H+I) **Catálogo de sujetos v3** congelado (SNP: entidad girada/depositaria/receptora/originante; bancos centrales, FMI, BIS, CCP; rol de alcance por TO nuevo) → rota el prefijo cacheado de E1 (aceptado). A2 de la auditoría.
- [ ] B5.5 (H) **Laudo D5**: corpus a escalar — **T1, NO RECORTABLE** desde la reunión del 26/08 (el escalado es el objeto central de la tesis, no un capítulo opcional: el laudo ya no decide *si* se escala sino *qué y en qué orden*). Recomendación: los 68 digeribles primero (2.009 pág., 6.340 unidades, ~USD 123); RI (53 TOs, 0 digeribles) como segunda vuelta si B5.6 lo habilita. **[LAUDO ESCRITO REQUERIDO — toca compromisos del PPF/alcance]**: no arranca sin laudo redactado y fechado por la autora. Prerrequisito adicional: laudo de esquema congelado (ESQ-3). Checklist del gate: [ ] **cola de mejoras diferidas revisada** (`docs/cola_mejoras_diferidas.md` — las entradas 1 y 6 deben estar resueltas o re-diferidas con destino explícito antes de escalar; la 8 define el contenido de r2).
- [ ] B5.6 (I, $0) Módulo de tablas (pdfplumber `extract_tables` con provenance, sin LLM) — RX-10 y montos invertidos. **CORRECCIÓN medida (U-B5.6-0, fe de erratas §c): NO decide el destino del bloque de régimen informativo.** El parser alcanza a 23 de 53 TOs y al 12,4 % de las palabras del bloque: decide el de UNA de sus cinco familias estructurales. **Se construye igual y por sí solo**, porque RX-10 es un defecto de correctitud sobre **normativa general** —dos montos invertidos verificados— y ese defecto vive en el grafo que la tesis entrega. Su prioridad ya no depende de lo que se decida sobre el bloque.
- [ ] B5.7 (I) Issue #6: documento de costos con tarifas reales + caching + experimento óptimo dentro de USD 200 (con B5.5). Laudo D4 warm-then-parallel (throughput: ~13 s/unidad → ~29 h secuenciales para 8.010).

### B6 · Escalado: corrida por tandas (issue #11) — **T1** (ruta crítica desde la reunión del 26/08; era T2) · S6–S7 (máquina; humano mínimo)
- [ ] B6.1 (I, ~$40) Tanda 1: 20 TOs digeribles (normativa general prioritaria), E0–E5, **gate de release de B2.6** (regression + shapes + intrínsecas + material propio) antes de ensamblar, carga en Neo4j, app sirviendo el grafo. Reporte: volúmenes, costo real vs estimado, incidencias. Es la primera ejecución del método de B2.8 de punta a punta sobre TOs nunca vistos.
- [ ] B6.2 (I, ~$85) Tanda 2: resto de digeribles (48) si tanda 1 cierra sin sorpresas. Créditos AWS/Bedrock si aplica (`app/llm_backend.py` ya soporta Bedrock).
- [ ] B6.3 (H+I, ~$25–40 **a estimar**) **EVALUACIÓN FINAL DE LA TESIS sobre el grafo escalado** — rediseñada por el principio 10 (era «sanity funcional descriptivo»). Es la medición del **conjunto de test**: se corre **una sola vez**, con **pre-registro sellado propio** (mismo molde que EV2 / A1.3: hipótesis, umbrales, criterios de lectura y tope de costo declarados ANTES de mirar resultado alguno). Componentes: (a) **eval set fresco sobre el corpus amplio** —preguntas nuevas con gold por criterios, selladas antes de correr, construidas sobre TOs **disjuntos del subset de desarrollo (los cinco TOs) Y de los 10 documentos de ESQ-1/ESQ-2 (misma lista, corrección D4 del laudo `8dea823`)** listados en `data/experiment/esq/documentos_excluidos_esq.json` (creado en `a7788c1`, 10 IDs con sha256 verificados contra el manifest), porque el esquema final se retocó mirándolos (ver nota de alcance del bloque ESQ); jamás EV2, que es material de desarrollo y está quemado. La disjunción se verifica contra ese archivo y se declara en el reporte—; (b) fidelidad con el juez calibrado + adjudicación humana simétrica; (c) atribución causal determinística A0.2; (d) **evaluación intrínseca por tripletas** con el instrumento ya validado sobre r1 (D-f): precisión, importancia y recall del gran grafo. **Sin brazo comparativo por defecto** (D-h: la tesis se enuncia como trabajo de recurso; la comparación contra recuperación por fragmentos es validación de diseño sobre el conjunto de desarrollo, no la pregunta central de la evaluación final). **Regla de admisibilidad de una eventual comparación sobre el grafo escalado — A DECIDIR EN EL MOMENTO DEL PRE-REGISTRO DE B6.3, no antes**: si se la quiere con **peso confirmatorio**, debe estar **declarada en el pre-registro sellado** de B6.3 (brazo, material, métrica y umbrales, antes de mirar nada); si se corre **después** de conocido el resultado de B6.3, se reporta explícitamente como **análisis exploratorio posterior** y **nunca al mismo nivel** que la evaluación confirmatoria. Regla dura: si el resultado obliga a tocar el pipeline, el arreglo produce una **release posterior** y se declara como tal (principio 9) — no se re-corre esta evaluación para mejorar el número.
- [ ] B6.4 (I) Cierre #11: reporte de escalado (vacío #5: costo, throughput, latencia).
Condición de arranque: **ESQ-3 laudado (esquema congelado)** + B1, B2, B5 cerrados y A2 en curso o cerrado. Si S6 llega sin B5 cerrado → se recorta a tanda 1 con laudo; **el escalado en sí ya no se descopa** (es el objeto central, D-g), lo que se ajusta es su alcance (D5/B5.5).

---

## Carril C — Escritura, gobernanza y publicación (siempre en paralelo)

### C0 · Gobernanza inmediata — T1 · S1
- [x] C0.1 (I) **HECHA** — `docs/tablero.md`, `docs/INDICE.md` y `README.md` actualizados a HEAD `85d9fdb` en el commit `2977e69` (tablero con EV2 cerrado: tabla definitiva, validación del juez, mapa causal U-A0, 8 desvíos del período, backlog por regla de estado efectivo, intake por casos; INDICE con las lecturas del período; README a agosto 2026 con nomenclatura canónica). Issues ejecutados por la autora con `gh`: cierres #8/#9/#10 y aperturas por bloque de este plan. El entregable de #9 "tabla defecto → resuelto/persiste" quedó transferido explícitamente a B2.1.
- [x] C0.2 (H) **HECHA** — este plan vive en `docs/plan_tesis.md` (commit de la autora al cierre de esta unidad); protocolo de actualización en la cabecera; se actualiza al cierre de cada unidad.
- [x] C0.3 (**HECHA** — H14–H26 numerados con estado/evidencia/alcance/destino, incluidos los dos del banco: H25 fabricación bajo contradicción de configuración con su encuadre exacto y H26 semántica del corte; bloque «Pendientes» actualizado — dos resueltos, nombre propio removido por convención) (I) `docs/hallazgos_tesis.md`: H14–H20 (inversión métricas intrínsecas P-b; juez bajo flag no confiable; mecanismo presente no operante; defecto de ensamblado +2 con denominador aguas arriba; brecha literal↔anti-léxica; arquitectura > prompt (enmienda 01); alucinación sistemática con retrieval perfecto; esquema v2 halva incorrectos / pipeline nuevo empata sin parches). Corregir `rol_fuente`→`rol_documental`, nota T2 (4 puntos), E4/E5 no ejecutados. **Hallazgos nuevos de A1.4 a numerar**: (i) la brecha anti-léxica **sobrevive** a BM25 y a mejores tools — de 20 fallas, 7 de búsqueda y 13 de selección del agente; el límite es la política, no el retriever; (ii) «mecanismo presente, no operante» queda con **tres instancias medidas** (esqueleto 8,3 %, alucinación con retrieval perfecto 3/3, paginación 0/275); (iii) **BM25 mejora por ranking, no por cobertura** (52→52 vistas; brecha vista-sin-consultar 6→1). **Del bake-off de embeddings (A2.0b)**: (iv) complementariedad léxico/denso medida sobre pasajes de E0 (BM25 72 vs 52 literal@1; 16 vs 36 anti-léxica@1) y la brecha anti-léxica sobrevive a un tercer instrumento; (v) la **frontera ancla/chunk**, cuarta aparición (`data/experiment/bakeoff_embeddings/hallazgo_frontera_ancla_chunk.md`): toda medición cross-capa declara su política de descendientes antes de medir.
- [ ] C0.4 (H) Laudos de descope escritos: caso de uso 1 (o demo mínima), GraphRAG-MS, versionado temporal (future work con diseño), régimen sin-gold, Graphiti, sub-corpus en inglés. Registrar la inversión de prioridad respecto del PPF §mitigación con justificación técnica. **[LAUDO ESCRITO REQUERIDO — toca compromisos del PPF/alcance]**: ninguna unidad que dependa de estos descopes arranca sin laudo redactado y fechado por la autora.
- [ ] C0.5 (I) `docs/backlog_reextraccion.md`: RX-04 corregido; RX-01..09 cerrados con evidencia del pipeline nuevo; RX-10 abierto → B5.6.
- [ ] C0.6 (I, $0) **Pendiente de la próxima pasada de C0**: (a) en `docs/tablero.md` §5, reemplazar "plan de tesis de la autora (documento de trabajo, no commiteado)" por la referencia a `docs/plan_tesis.md`; (b) actualizar el párrafo "Migración Neo4j" del `docs/tablero.md` (cola de unidades / estado del backend) con el estado post-A1.1: backend con paridad verificada 322/322 en `9e131bf`, modos `paridad`/`fulltext`, `GraphAgentNeo4j`, no inyectado en el pipeline de evaluación; A1.2 como punto de extensión.

### C1 · Esqueleto y redacción de la tesis (skill `latex-udesa`) — T1 · S1–S9
**Arranca ya** (S2): el trabajo y el entregable están claros; nada impide escribir. Base: el
**template LaTeX del taller** (la autora lo incorpora a `docs/tesis/` o a un directorio de
fuentes versionado; `docs/ppf/main.tex` es el antecedente de estilo). **Reglas de escritura
vinculantes**: un párrafo = una idea; una oración = un concepto; cada párrafo conecta con el
siguiente, sin remates; corta (el material es nítido, no necesita verbosidad); **visual** —
figuras y esquemas del grafo y del pipeline en cada capítulo donde aporten; **self-contained**
para un lector técnico no experto en NLP (background amplio, explicar qué es un KG), con
estructura que permita al experto saltear el background y leer contribuciones; la primera
pasada puede ser asistida, pero se reescribe con voz propia y se revisa contra estas reglas
(las estructuras genéricas de LLM se rechazan). Referencia de background: una tesis con buen
capítulo de KG, pendiente de recibir como insumo de lectura.
Capítulos (borrador → revisión → final), cada uno alimentado por un bloque:
- [ ] C1.1 **Introducción** — estructura en ocho ideas (cada una un párrafo o dos): (1) los LLM habilitaron la construcción de KGs a escala y por qué los KGs importan para RAG; (2) limitaciones actuales, **solo las que este trabajo resuelve** (fidelidad no medida, comparación sin baseline justo, castellano/banca central, costo, evaluación intrínseca ciega a la sobre-fusión); (3) «acá se resuelve X, Y, Z»; (4) overview del método (corpus → esquema → E0–E5 → retrieval → evaluación bajo custodia → refinamiento por releases); (5) el grafo en sí (esquema, sujetos, provenance) con **una figura** de un subgrafo real; (6) la evaluación: «los grafos son difíciles de evaluar, por eso se desarrolló…» (juez de dos pasos, fidelidad por criterios, atribución causal, tripletas con importancia); (7) los números principales (EV2 3/20/17 · 5/26/9 · 4/27/9; ablación; head-to-head cuando exista); (8) lista de contribuciones. Pregunta + tres sub-preguntas + hallazgo rector quedan dentro de (3)/(6). **Primer borrador en S2**, antes de que haya más resultados: se actualiza después. (S2–S3)
  - [x] C1.1 **tramo 1** (ideas 1–4: Motivación + Definición del problema) — redactado y sellado en `fffdbef` sobre esqueleto aprobado, con tuneo de la autora.
  - [x] C1.1 **tramo 1b — HECHO**, sello `5ff8be7` (verificado por mesa el 27/08: marcador `[PENDIENTE MENTORES — D-g]` retirado de `main.tex` y párrafo 4 reformulado con el encuadre de recurso de D-h). Alcance original: el cierre del párrafo 2 (hoy «cinco Textos Ordenados … densidad realista + evaluación exhaustiva», con marcador `[PENDIENTE MENTORES — D-g]`) y el enunciado del párrafo 4 (hoy «sobre cinco Textos Ordenados») se reescriben con el marco desarrollo/test: el objeto es el corpus regulatorio completo y los cinco TOs son el conjunto donde se construyó y validó el método. Se retira el marcador al aplicar. Borrador de mesa → tuneo de la autora (mismo circuito que el tramo 1).
  - [ ] C1.1 **tramo de objetivos — DESBLOQUEADO por D-g**: el objetivo general se formula sobre el corpus completo (recurso final) y los específicos incluyen la validación del método sobre el conjunto de desarrollo.
  - [ ] C1.1 **tramo de Estado del arte — DESBLOQUEADO**: el material de background llegó (ver U-RW y `docs/lecturas_reunion_2026-08-26.md`).
- [~] U-INV **Inventario del recurso** (EN VUELO, sin pasar por revisión de mesa — fila mínima
  para que la cola la vea; el detalle lo completa su propia revisión al cierre). Working set
  declarado: `docs/tesis/inventario_recurso.md` (nuevo), `.gitignore` (línea
  `!docs/tesis/inventario_recurso.md`), y ediciones en vuelo de `docs/tesis/main.tex` y
  `docs/tesis/bibliografia.bib`. **Nada de ese working set viaja en commits de otras unidades**
  (regla ya aplicada en los pases recientes: add por ruta explícita).
- [x] U-RW (**HECHA y CONSOLIDADA**, `70352b8`) **Related work de *releases* de KG post-LLM** (compromiso de la reunión del 26/08; encuadre: tesis de recurso). Ejecutada en dos partes: unidad de solo-descubrimiento (tabla de candidatos con triage y consultas auditables) + lectura en diagonal y mapa de exigencias por la mesa. **Consolidada a `docs/mapa_related_work.md`** (§2: mapa de 10 exigencias con estado/evidencia/dónde-se-resuelve; §3 estados finales de lecturas; §4 candidatos; §5 selección para lectura en serio) y `docs/lecturas_reunion_2026-08-26.md` actualizado. **Marcas confirmadas por la autora y ya registradas en el plan** (Wilson + desagregación por etapa en B4.1; checklist FAIR en C2.1; exigencias 6 y 7 en la agenda de mentores). El riesgo de material-en-sesiones quedó resuelto por la consolidación. Alimenta C1.2 y el Estado del arte.
- [ ] C1.2 Marco teórico + literatura (00–09, 5 vacíos, playbook como contraste; nota "graph engineering"). (S2)
- [ ] C1.3 Corpus y esquema (2.1, 2.2, esquema v2, catálogo de sujetos, ejes A/B, herencia). (S2–S3)
- [ ] C1.4 **El método** — construcción y refinamiento de un KG regulatorio de punta a punta (sigue B2.8): pipeline E0–E5 (diseño, principios, enmienda 01 con P1–P3, costos, limitaciones) + ciclo de refinamiento por releases (B2.6) + retriever/backend + intake. Cada mecanismo con puntero al experimento que lo demuestra (§6). (S3–S4, cierra con B1/B2)
- [ ] C1.5 Metodología de evaluación bajo custodia (pre-registro, sets ciegos, juez 2 pasos, juez de fidelidad por criterios, verificador v7', taxonomía, métricas intrínsecas, regression suite, backend/retrieval) + **los dos instrumentos declarados** (principio 8): harness congelado para lo sellado, banco Claude Code + MCP para el head-to-head, con el puente A1.7 y el adaptador de trazas que preserva la atribución. (S3–S5)
- [ ] C1.6 Resultados: 2.3; escalón 1/1b; C1–C7; intrínsecas; EV2 (fidelidad+navegabilidad+atribución); ablación retrieval; head-to-head; gold tripletas; escalado. (S5–S8)
- [ ] C1.7 Discusión: grounded ≠ correct; retrieval ≠ estructura; humano-en-el-loop (H7/H8, Motor 3 no validado); misreadings de métricas; **el techo del retrieval es bajo** — la ingeniería de búsqueda compra lo literal (ranking), lo semántico exige política de agente o representación distinta (A1.4: 7 de búsqueda vs 13 de selección); límites (multi-hop, tablas, sujetos, familia del verificador; **concentración del pool de anclas del corpus** — 175 anclas, 28/37 compartidas entre sets sintéticos, `ablacion_retrieval/anexo_solapamiento_anclas.md`, `68c79dc`); descopes; **reproducibilidad de un harness de terceros** (el prompt interno no es propio; se mitiga fijando modelo, registrando el model id real por traza y apoyando la validez en que ambos brazos comparten la misma caja negra). (S7–S8)
- [ ] C1.8 Conclusiones + trabajo futuro (temporalidad, E4-LLM, RI, explicabilidad). (S8)
- [ ] C1.9 Anexos: reproducción (comandos), costos, sellos/sha, glosario. (S8–S9)
- [ ] C1.10 Revisión integral + defensa (guion, banco de preguntas actualizado: Q8/Q16, puntos incómodos redactados). (S9–S10)

### C2 · Publicación y reproducibilidad — T2 · S8
- [ ] C2.1 (I) Release etiquetado + Zenodo/DOI: KG (KG-Refinado y KG-Reextraído-r1 con sha), eval sets sellados (EV2 preguntas+criterios, pares sintéticos, U6), gold de tripletas, scripts de métricas/regression, README de reproducción. Cumple "público" del PPF. **Agregado por decisión de la autora (mapa de related work, exigencia 8): checklist FAIR explícito como parte del entregable** — licencia declarada, forma de acceso/endpoint y código publicados (precedente del KG legal del paper 04: RDF con CC-BY, endpoint y código).
- [ ] C2.2 (I) `docs/ARQUITECTURA.md` snapshot final.

---

## 2. Cronograma sugerido (10 semanas; una unidad por carril por semana)

| Sem | Carril A | Carril B | Carril C |
|---|---|---|---|
| S1 (17–23 ago) | A0.1–A0.2 (U-A0) | — (U-B1a entra recién al cierre revisado de U-A0 o de U-C0) | C0.1–C0.5, C1.1 (U-C0) |
| S2 (24–30 ago) | A0.3–A0.4, A1.1–A1.3 | B1.1–B1.7 (U-B1a, arranque condicionado), B2.1 | C1.1 (borrador de intro), C1.2–C1.3 |
| S3 (31 ago–6 sep) | A1.4–A1.5 | B2.2–B2.5, B3 | C1.4–C1.5 |
| S4 (7–13 sep) | A1.6, A2.1–A2.2 | B1.8, B4.1–B4.2, B5.1–B5.4 | C1.5 |
| S5 (14–20 sep) | A2.3–A2.4 | B4.3–B4.4, B5.5–B5.7 | C1.6 |
| S6 (21–27 sep) | A3 (T2) | B6.1 | C1.6–C1.7 |
| S7 (28 sep–4 oct) | — | B6.2–B6.4 | C1.7 |
| S8 (5–11 oct) | buffer | buffer | C1.8–C1.9, C2 |
| S9–S10 (12–26 oct) | — | — | C1.10 |

**Reordenamiento por la reunión del 26/08, actualizado por la rama (b) de U-ESQ-2-cal** (el
cronograma de arriba es previo y queda como referencia histórica): la ruta crítica es
**ESQ-2 protocolizada (U-ESQ-2 ejecutada `a7788c1`; resta la lectura de la autora) → ESQ-3 →
B5 → B6.1/B6.2 → B6.3 (evaluación final)** — la corrida ESQ-1
del diseño original ya no existe —, y ESQ entra **antes** que cualquier ítem de escalado. A2 (head-to-head),
B4 sobre r1, B1.9/B1.10 y los casos de uso se re-encuadran como trabajo sobre el conjunto de
desarrollo: siguen valiendo como experimentos de la tesis, pero ceden prioridad de calendario
frente a ESQ y al escalado. El presupuesto de abajo no incorpora aún ESQ-1 (a estimar).

Presupuesto API estimado del plan: A ≈ 105 (incluye A1.4 real **USD 11,19** de tope 20, A1.7 ~12, A2.0 ~0 en construcción, A2.5 condicional ~25) · B ≈ 137 (escalado 125 + resto + B1.10) · C 0 → ~USD 242
(+ ~USD 30 de reserva)\*. El escalado usa el budget de #6 / créditos AWS.

\* Vigencia de las tarifas: las estimaciones usan tarifas vigentes al 17/08. El precio de
Sonnet USD 2/10 por MTok quedó **confirmado como estándar** (no era intro con vencimiento;
re-verificado en U-A1.3, `68c79dc`), así que la alerta de vencimiento del 31/08 queda sin
efecto. Se mantiene la regla: toda autorización de fase B re-verifica tarifa contra
documentación oficial y re-estima antes de correr; el buffer de USD 30 se declara en la
autorización correspondiente si una tarifa cambia.

Regla de recorte si S5 llega atrasado: se recorta primero **B6** (a tanda 1 o descope),
después **B3.3–B3.4** (A3 ya quedó absorbida por A1.7). Nunca se recorta A2 ni C1.
Prioridad entre las unidades nuevas nacidas de A1.4, si el calendario aprieta:
**A1.7 > B2.9 > B1.9** (las dos últimas cuestan USD 0). De las nacidas del rediseño del
head-to-head: **A2.0-gate, A2.0-banco y A2.0b son T1 y no se recortan** (sin gate no se sabe si el banco sirve, y sin banco no hay head-to-head); **A2.0-reportes sí es recortable**;
**B1.10 y A2.5 son las primeras en caer**, en ese orden.
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
- **CHECKPOINT EN DISCO (transversal obligatorio de todo mandato).** Antes de cualquier
  compactación de contexto, y al cerrar cada entregable numerado, la instancia escribe el
  estado exacto en `scratchpad/checkpoint_<unidad>.md` y **reporta su ruta**. Contenido
  mínimo: entregables terminados con su ruta; entregable en curso y en qué punto quedó;
  decisiones tomadas con su justificación; desvíos declarados; comandos corridos y su
  resultado; qué falta. Se redacta **para que un ejecutor nuevo continúe sin la instancia**,
  no como resumen propio. Si compactó, lo declara y cita el checkpoint desde el que siguió.
  Justificación: la compactación es un **modo de falla silencioso** — la instancia no puede
  verificar qué perdió y reporta con la misma fluidez, así que el estado tiene que vivir en
  disco y no en su memoria.
- **Cadencia**: cierre semanal → tablero + plan actualizados en un solo commit.

## 4. Primeras unidades a delegar (esta semana)

1. **U-A0** (carril A): reporte consolidado EV2 + atribución determinística de primer nivel
   con regla pre-registrada (A0.1–A0.2). $0. Entregable en `data/experiment/ev2_reporte/`.
2. **U-C0** (carril C): actualización de tablero/INDICE/README/hallazgos H14–H20/backlog RX
   (C0.1, C0.3, C0.5) + esqueleto LaTeX de capítulos con mapa bloque→sección (C1.1 borrador).
   $0. Los laudos C0.2/C0.4 son de la autora.
3. **U-B1a** (carril B; condición de arranque **cumplida**: U-A0 cerrada en `40603a9`/`85d9fdb`
   y U-C0.1 en `2977e69`): invariantes + guarda de merge cross-TO de `ensamblar_corpus` (B1.5),
   E4 determinístico (B1.2), E5 esqueleto (B1.1), referencias cruzadas norma→norma (B1.3),
   provenance rica (B1.4), cola humana flaggeada con recomputo de política (B1.6) y
   re-ensamblado KG-Reextraído-r1 sin API (B1.7) — **alcance B1.1–B1.7**; B1.8 (fidelidad EV2
   de r1) es unidad aparte con pre-registro. $0.

## 5. Decisiones que solo la autora puede tomar (esta semana)

Las decisiones D-a..D-e las toma la autora; cada una queda registrada como laudo escrito con
justificación técnica antes de ejecutar la unidad que la usa.

- D-a Casos de uso: (i) explicabilidad agéntica — descope escrito vs demo mínima (A2.4 / C0.4); (ii) **log de operaciones → cadena causal**: valorado positivamente en la reunión del 26/08 y **estacionado por indicación de la misma reunión** como capítulo final independiente, a retomar después de la evaluación final del grafo escalado (no compite con la ruta crítica ESQ → escalado → evaluación final).
- D-b Evaluación intrínseca a nivel tripleta (B4 rediseñada): alcance (100 tripletas de precisión, top-100 de recall), escala de importancia, regla de presencia y umbral de acuerdo del juez. **[LAUDO ESCRITO REQUERIDO — toca compromisos del PPF/alcance]**: B4 no arranca sin laudo redactado y fechado por la autora.
- D-c Corpus a escalar (D5) y si el escalado entra o se recorta a tanda 1.
- D-d Umbrales de intrínsecas pasada 2 (B3.1).
- D-e **RESUELTA**: el plan vive en `docs/plan_tesis.md` (C0.2); issues por bloque abiertos en U-C0.1.
- D-f **RESUELTA — laudo firmado 27/08/2026** (borrador redactado: `docs/laudo_D-f_secuencia_tripletas.md`):
  secuencia de la evaluación intrínseca de tripletas (B4). Dirección adoptada: el **instrumento**
  de tripletas se construye y valida sobre KG-Reextraído-r1 —conjunto de desarrollo, donde se
  itera sin restricción— y la **medición que cuenta para la tesis** se corre una única vez sobre
  el grafo escalado, dentro de la evaluación final pre-registrada (B6.3). **Atribución**: es
  aplicación del marco desarrollo/test del principio 10; la reunión del 26/08 **no trató
  explícitamente** la secuencia de tripletas, de modo que esta aplicación específica es decisión
  de la autora y se menciona como tal en el próximo informe de avance. **No bloquea**: B4.1
  (pre-registro), B1, B2, B5.1–B5.4, A2, C1. **Sí ordena**: B4.2–B4.4 corren sobre r1 como
  validación del instrumento (sin ser el resultado de la tesis), B6.3 incluye la corrida que
  cuenta, y la **release r2** sigue el principio 9. **Checkbox de implementación (lección A1.6:
  un laudo sin consecuencia implementada es una deuda silenciosa)**: [ ] B4.1 declara en su
  pre-registro el doble rol (validación en r1 / medición en el escalado); [ ] B6.3 incorpora
  tripletas como parte de la evaluación final pre-registrada.
- D-g **RESUELTA — laudo firmado 27/08/2026** (borrador redactado: `docs/laudo_D-g_alcance_corpus.md`):
  ALCANCE DEL CORPUS EN LA TESIS — **resuelta en la reunión de mentores del 26/08/2026**. El
  **objeto central de la tesis es el KG escalado de la regulación del BCRA**; los cinco Textos
  Ordenados del subset son el conjunto de desarrollo (train/eval) sobre el que se construyó y se
  validó el método, y sus experimentos se presentan como tales. Fundamento tal como se planteó
  en la reunión: sostener la tesis sobre los cinco TOs sería sobreajustar el documento; el
  trabajo se centra en el recurso. Ver principio 10. **Consecuencias**: (a) la escritura queda
  desbloqueada con esta dirección — el marcador `[PENDIENTE MENTORES — D-g]` de
  `docs/tesis/main.tex` se resuelve reescribiendo el cierre del párrafo 2 y el enunciado del
  párrafo 4, y el objetivo general se formula sobre el corpus completo; (b) el escalado deja de
  ser un capítulo opcional y pasa a ser ruta crítica (B5/B6 re-tierados a T1); (c) antes de
  escalar es obligatorio el bloque **ESQ** (validación del esquema), porque una vez escalado
  volver atrás es inviable. **Checkbox de implementación (lección A1.6)**: [ ] reescritura de
  P2/P4 y objetivo general en `main.tex` (C1.1 tramo 1b); [ ] B5/B6 re-tierados y ESQ como
  bloqueante (aplicado en este plan); [ ] B6.3 rediseñada como evaluación final (aplicado en
  este plan); [ ] mención del cambio de alcance en el próximo informe de avance.

- D-h **RESUELTA — decisión de la autora, 27/08/2026**: ENCUADRE DEL ENUNCIADO DE LA TESIS. La
  tesis se enuncia como **trabajo de recurso**: construye y evalúa un grafo de conocimiento de la
  normativa del BCRA. La **comparación contra recuperación por fragmentos deja de ser la pregunta
  central** y pasa a ser **validación de diseño sobre el conjunto de desarrollo** (principio 10).
  **Consecuencias**: (a) B6.3 **no lleva brazo comparativo por defecto**; (b) A2 (head-to-head)
  conserva todo su valor como validación de diseño sobre el subset, y así se reporta; (c) la
  redacción del párrafo 4 de la introducción ya refleja este encuadre (C1.1 tramo 1b). **Riesgo
  declarado**: modifica el enunciado declarado en el PPF. **Acción comprometida**: [ ] mencionarlo
  explícitamente a los mentores en el próximo informe de avance, para que puedan objetarlo.

- **RESUELTA (28/08/2026, por la autora) — contenedores no-lista del crudo:** 7 de 1.769 registros del crudo de desarrollo traen un contenedor con tipo distinto de lista (4 cortes por `max_tokens` con `relations: null`, 3 con `entities` como string; en `validacion` los 1.769 tienen ambos contenedores como lista; documentado y asertado en el selftest de U-ESQ-1a-bis). **Resolución**: se mantiene la tolerancia —elevarlos a error sería una decisión que el pre-registro no tomó—; el resumen de la corrida de ESQ-1 **DEBE reportar el conteo de contenedores no-lista**, para que la pérdida sea visible y no silenciosa (**requisito que entra al mandato de la corrida**); y B5.3 (reintento 16k→32k) queda como remedio de fondo de la causa.

**Agenda de la reunión del 26/08/2026 — CUMPLIDA** (5/5): (1) D-g resuelta (alcance: el objeto
central es el corpus escalado; los cinco TOs son desarrollo) → principio 10 + laudo firmado
27/08/2026; (2) D5 deja de ser recortable: el scope del escalado pasa a ruta crítica, el laudo de
corpus a escalar (B5.5) sigue pendiente pero ya no decide *si* se escala sino *en qué orden*; (3)
D-f **no fue tratada** en la reunión — se resuelve por laudo de la autora aplicando el principio
10 (ver D-f); (4) material de background **recibido** (registrado en
`docs/lecturas_reunion_2026-08-26.md`) → cierra el pedido vigente y habilita C1.2 / Estado del
arte; (5) informe de avance presentado (B1.8 `774acac`, promoción `81587f9`).

**RUTA CRÍTICA vigente (actualizada por el cierre de U-ESQ-2, `a7788c1`)**:
`ESQ-2 protocolizada (única vía de cobertura; U-ESQ-2 EJECUTADA — gate 10/10, extracción
762/762 a USD 4,1079, worksheet de 75 fichas listo con cegado restaurado por la fe de erratas
930f289; resta: lectura de la autora en tandas de 10–15 con checkpoint de ritmo → spot-check
de mesa 10/75 → tabla con Wilson) → ESQ-3 (retoques
+ laudo de esquema congelado, con TODO el material: escalera, calibración, deformación,
potestades, firmas de la cola) → escalado (B5/B6) → evaluación final sobre el grafo escalado
(B6.3, pre-registro propio)`. La corrida ESQ-1 del diseño original ya no existe (modo (i)
irrealizable, `38be6e5` falsado-cerrado). Todo lo demás —A2 (head-to-head), B1.9/B1.10, B4
sobre r1, casos de uso— es trabajo sobre el **conjunto de desarrollo**: valioso, se presenta
como experimento, y no bloquea la ruta crítica.

**Compromisos de la reunión pendientes de ejecución**: barrida de related work de *releases* de
KG post-LLM en cualquier disciplina, con foco en trabajos que presentan un **recurso** como el de
esta tesis (unidad U-RW, insumos en `docs/lecturas_reunion_2026-08-26.md`); y el caso de uso de
**log de operaciones → cadena causal** queda **estacionado como capítulo final independiente**, a
retomar después de la evaluación final (registrado en D-a.ii).

**AGENDA DE LA PRÓXIMA REUNIÓN DE MENTORES — punto del régimen informativo, en su forma nueva.**
Reemplaza al punto anterior («¿se escala el bloque de régimen informativo o queda declarado
fuera?»), que U-B5.6-0 dejó mal planteado: **ya no es una decisión binaria**. El bloque tiene
**cinco familias estructurales con costos distintos**: dos se desbloquean con el modo de lectura
sin raíz de sección (ESQ-RI-1, $0), una necesita el parser de tablas (B5.6, que hay que construir
igual por RX-10 sobre normativa general), y **la mayor —71 % de las páginas del bloque— exige
extender el esquema** (ESQ-RI-3), porque el modelo de datos no admite hechos con valor (ver
hallazgo, bloque ESQ). La pregunta que va a la reunión es **hasta dónde se llega**, con los costos
medidos a la vista, familia por familia. Se lleva ANTES de laudar D5, como fijó el laudo `94bb7a7`
§D10. Insumos: `docs/fe_erratas_D10_causa_regimen_informativo.md` y
`data/experiment/escalado_prep/scoping_b5_6_tabular_reginf.md`.

**PRÓXIMO INFORME DE AVANCE — todo lo comprometido, en un solo lugar (nada se evapora entre
reuniones).** Menciones comprometidas por laudo, aún no cumplidas: (1) el **cambio de alcance**
de D-g (el objeto central es el corpus escalado; checkbox del laudo `docs/laudo_D-g_alcance_corpus.md`);
(2) el **encuadre de recurso** de D-h (la comparación baja a validación de diseño — modifica el
enunciado del PPF; checkbox en D-h); (3) la **atribución** de D-f (la aplicación del marco
desarrollo/test a las tripletas fue decisión de la autora, no tratada en la reunión; checkbox
del laudo `docs/laudo_D-f_secuencia_tripletas.md`). Puntos de agenda acumulados abajo: régimen
informativo familia-por-familia (pre-D5), exigencias 6 y 7 del related work, y la historia
completa del control de ESQ-1 como informado. Al fijarse fecha: armar guion con la skill de
reunión sobre este bloque.

**AGENDA — punto INFORMADO (no de decisión): la historia completa del control de ESQ-1 —
escalera + calibración + rama.** (1) Tres controles pre-registrados y falsados en escalera
sellada (P1/P1′/P1″; commits de U-ESQ-1c, `c25273f`, `0e50e3d`): el canal declarativo es
inviable — el extractor conforma al esquema todo lo que no encaja (deformación semántica,
inestable entre corridas). (2) Calibración del modo (ii) con pre-registro nuevo (`bca863f`,
final de un solo tiro): **P-cal falsada por su segunda mitad** — capacidad sí (A′ 9/10: el
modelo ve y nombra lo plantado cuando descubrir es la única tarea), precisión no (C 7/10 con
falsos positivos: un censo habría sobrecontado la deriva). (3) **Rama (b) del árbol sellado: el
censo por LLM queda CERRADO con doble evidencia — extrayendo deforma, descubriendo
sobrecuenta — y ESQ-2 protocolizada es la única vía.** Bonus del control: el hueco de
potestades confirmado en corpus real. Costo total de la saga (escalera + calibración):
USD 0,92 de tope 9,00.

**AGENDA — punto nuevo: dos exigencias del related work que tocan alcance (decisión de los
mentores, no compromisos; `docs/mapa_related_work.md` §2, exigencias 6 y 7).** (a) ¿Se valida el
recurso contra **normativa posterior a la construcción**? Precedente PrimeKG: holdout temporal
(40 terapias FDA posteriores al corte, verificando ausencia de fuga); el corpus vivo del BCRA la
vuelve natural — la pregunta es si entra como parte de B6.3, como unidad propia, o queda como
trabajo futuro declarado. (b) ¿Qué protocolo cubre el **cambio normativo** (el TO cambia: ¿qué
pasa con el grafo?)? El circuito de releases de B2.8 cubre el refinamiento por defectos, no la
actualización por cambio de fuente — el hueco es real y la pregunta es su tratamiento: ¿capítulo,
unidad, o limitación declarada con el diseño escrito?

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
| M-13 | Retriever BM25/Neo4j y tools v2 (retrieval ≠ estructura) | Ablación factorial 2×2 pre-registrada, 400 trazas: BM25 mejora lo literal por ranking (0,887→0,981) y **no cierra** la brecha anti-léxica (P2 refutada); tools v2 sin efecto medible (paginación 0/275); latencia p50/p95 por celda | `9e131bf` + `9141351` (backend y tools) + `68c79dc` (pre-registro) + corrida A1.4 (`data/experiment/ablacion_retrieval/corrida/resultados/`) | hecho |
| M-14 | Intake de feedback de la app → backlog (Motor 2) | U6 (25 preguntas reales), BKL-0024/0025, cola de intake cerrada | `0d5fd10` (`scripts/adaptador_sesiones.py`); `b337152` (`exploracion/adjudicacion/u6_adjudicacion_humana.jsonl`); `data/backlog/intake/cola_intake.jsonl` | hecho |
| M-15 | Comparación justa KG-RAG vs RAG sobre los mismos chunks de E0 | A2 head-to-head + Pareto, sobre el banco de M-21 (mismo agente y mismo prompt en los dos brazos) | — (depende de A2.0-gate y A2.0-banco) | **pendiente** |
| M-16 | Escalado por tandas con gate de release y reporte de costo/throughput | B5–B6 (68 TOs digeribles), con ESQ-1/2/3 como prerrequisito bloqueante | — (prep `111ed19`, `escalado_prep/resumen_escalado.md`) | **pendiente / T1 — ruta crítica (D-g)** |
| M-17 | Evaluación intrínseca a nivel tripleta sin anotación masiva: precisión con juicio de correctitud + importancia sobre muestra del grafo con evidencia; recall por ranking de importancia sobre tripletas extraídas de fragmentos; juez LLM calibrado contra adjudicación humana en tandas; adjudicación post hoc solo de ausencias | B4 sobre KG-Reextraído-r1 (sellado, principio 9); reuso sobre el grafo escalado en B6.3 | — | **pendiente** |
| M-18 | Circuito de custodia revisor-ejecutor para investigación con agentes LLM: mandatos por unidad con criterios de aceptación, frenos declarados, laudos de la autora, pre-registro por commit, verificación de mesa contra archivos (nunca narrativa), errores de ambos lados detectados y documentados | Registros de desvíos declarados del período: sello tardío `9c44516`; pasada inválida de calibración documentada; commit tardío declarado en `b624865`. Destino en la tesis: C1.5 (metodología) + candidato a sección propia de contribuciones | `CLAUDE.md` (reglas del circuito, §4 a–h); mensaje de commit `9c44516` ("sello efectivo 2026-08-13… pre-registro válido"); `data/experiment/ev2_juez/calibracion/registro_calibracion.md` (commit `1a0ac5c`); mensaje de commit `b624865` ("commit tardío respecto del cierre de la unidad, detectado por la unidad §7") | hecho |
| M-19 | Atribución causal de fallas determinística de primer nivel (presente→consultada→vista→generación, por replay de trazas, USD 0, reproducible al byte; abstención como columna cruzada) | EV2: 120 trazas base + 191 §7 atribuidas; perfiles de falla distintos en el empate 9-9; generación clase modal 17/25/21; techo de retrieval 14/7/6 (H1–H7) | `40603a9` (regla sellada pre-cómputo, `data/experiment/ev2_reporte/regla_atribucion.md`, selftest 24/24) + `85d9fdb` (`data/experiment/ev2_reporte/salida/atribucion_fallas.{json,md}`, doble corrida byte-idéntica) | hecho |
| M-20 | Descomposición experimental retrieval / tools / política del agente (factorial con material propio, replay determinístico, IC bootstrap apareado) como método para localizar el cuello de botella de un sistema KG-RAG | A1.4 (índice × tools: el cuello no era ninguno de los dos) + A1.7 (política) | `68c79dc` (pre-registro) + corrida A1.4; A1.7 pendiente | parcial (A1.4 hecho, A1.7 pendiente) |
| M-21 | Banco de evaluación por MCP: el brazo (grafo / vector DB) como **variable declarada**, un solo agente y un solo prompt para todos los brazos, aislamiento verificado por capacidad, y adaptador de trazas que preserva el replay y la atribución causal | A2.0-gate (adaptador, por clase) + A2.0-banco (servidores y aislamiento) + A2.1/A2.2 (head-to-head) + A1.7 (puente entre instrumentos) | `c09663a`/`b08095a` (gate) + `1fa79de` (banco) | **parcial (gate y banco hechos; head-to-head pendiente)** |

Regla: un mecanismo solo figura "hecho" con fuente verificable en esta columna.
