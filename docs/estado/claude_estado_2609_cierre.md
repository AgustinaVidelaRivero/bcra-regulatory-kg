# Estado del proyecto — 26/09/2026 — tanda 0 pre-registrada y sellada

Escrito por la mesa revisora (chat) al cierre de la sesión del 25-26/09. Reemplaza, para lo que sigue, la sección de pendientes del traspaso del 24/09; todo lo demás de ese traspaso sigue vigente. Lo que no se verificó contra un artefacto va marcado NO VERIFICADO.

## §1. Qué pasó desde el traspaso del 24/09

1. Reunión con una mentora (25/09): sugirió correr el esquema congelado con el pipeline entero sobre 5 documentos nuevos y evaluar el grafo de caja negra, sin fichas manuales; contar relaciones nuevas y tripletas entre documentos; fijar modelo, versión, fecha y vía por corrida; feedback de escritura (lector = alguien de la misma carrera; no nombrar un concepto antes de presentarlo; un mismo ejemplo que crece). Notas en el PDF de la autora del 25/09.
2. La autora decidió hacerlo como **tanda 0** (unidad B6.0), primera corrida del escalado, no como test aparte.
3. Tres commits, todos en `main`, **ninguno pusheado al cierre** (NO VERIFICADO después):
   - `d714582` — plan: B6.0 asentada, observaciones (10) y (11), registro de modelos en C1.9.
   - `c80b03f` — `docs/preregistro_tanda0.md` (911 líneas) y `data/experiment/esq/enmienda_ventana_correccion_2026-09-25.md` (109 líneas), firmados por la autora. **Este es el sello de las predicciones.**
   - `0835874` — plan: (a)(b)(c) de B6.0 resueltos, primera parte de la fase 1 cerrada, siete gates técnicos, regla v2 de tipo de pregunta.
4. `adjudicar.py` sigue sin rastrear en la raíz (preexistente del 16/08). Decisión de la autora pendiente: versionar o no, y dónde.

## §2. Decisiones de la autora (25/09), ya asentadas

- D1 Conjunto de la tanda 0: **ctacte, lingob, polcre, pagjub, docvig** (671 unidades, 172 páginas), de los 10 reservados de `scoping_esq1.md` §4.5, por regla sin sorteo (orden por unidades desc., posiciones 1,3,5,7,9). Reservados: depinv, rrci, gescre, retype, snp_atm. **No se cambian**: después de la elección se supo que los reservados suman más remisiones «fuera del inventario» (gescre 5); eso es información posterior a la regla.
- D2 La misma corrida re-extrae los 5 TOs de desarrollo con el congelado. **Cuatro celdas de EV2**: C1 r1+GraphIndex (sellada `774acac`, se agrega), C2 r1+Neo4j fulltext, C3 desarrollo-congelado+GraphIndex, C4 desarrollo-congelado+Neo4j fulltext. Mismo harness congelado, firma v1 de las tres herramientas, **sin tools v2** (laudo A1.6:47). Tres celdas nuevas = uso único de EV2 (principio 7, plan :209-212; precedente A1.5/A2.3/A3.1).
- D3 Ventana de corrección única del §7 del laudo congelado **puede abrirse tras la tanda 0**; sigue siendo una sola; si se usa, los 5 dejan de ser vírgenes y B6.3 (a) los excluye. Enmienda con fecha, laudo intacto (sha `64c5da88…`).
- D4 Fase 2 no arranca sin ok escrito de la autora, que espera respuesta del mentor. La fase 1 se hace sin pedir permiso porque no gasta ni toca documentos.
- D5 Una extracción, **tres ensamblados** determinísticos: desarrollo solo (C3/C4), tanda 0 sola (observación (10) de la tanda 0), los diez (observación (11) y preguntas nuevas).
- D6 Tope USD 100. Estimación A7: USD 69,18; ≈ 76,5 con preguntas nuevas.
- D7 E1 corre como corrió r1, **sin temperatura fijada**, declarado como límite de reproducibilidad; no se edita `cliente_e1.py` para esta tanda. (La mesa había recomendado 0 y cambió: fijarla exige código nuevo antes de una corrida sellada y mete una segunda variable en C1 vs C3.)
- D8 Preguntas nuevas sobre los cinco: **al menos una de varios puntos por documento y dos de abstención en total**. Las cuotas del conjunto final de B6.3 (a) siguen abiertas.
- D9 Observaciones (10) relaciones por unidad (base 12.010/1.763 = 6,81 en r1) y (11) aristas cross-TO (base 188) y remisiones «fuera del inventario» que se resuelven (predicción 4 de 106: polcre 2, docvig 2): **observaciones sin umbral**. Único criterio de retiro: principio de gobierno del §1.

## §3. Lo que falta antes de correr (fase 2), en orden

Gates técnicos (plan, sub-ítem de B6.0; todos USD 0):
1. Cableado de r1 en `ensamblar_corpus.py` (los pasos viven en `ensamblar_r1.py` `185e042`).
2. Shapes con perfil congelado — B2.2 fase 2. **Borrador de mandato en el scratchpad de la instancia del plan** (`mandato_UB22_fase2_BORRADOR.md`); la mesa lo revisa antes de despachar.
3. Regression suite — B2.1 fase 2. Borrador ídem.
4. Runner de EV2 sobre `GraphAgentNeo4j` fulltext, firma v1 (módulo nuevo, sin editar sellados; patrón `ev2_r1/code/comun_r1.py`).
5. Registro en `grafos.py` y carga en Neo4j del grafo de desarrollo re-extraído.
6. Intrínsecas a generación 3 y `ucita2_indicadores.py` parametrizado.
7. Manifiesto de la tanda 0 (`perfil_e1: "v3_b54"`, diez TOs, `rol_alcance` null para docvig; se escribe en el mandato de fase 2).

Además:
- **Regla v2 de tipo de pregunta**, a sellar antes de clasificar las preguntas de la tanda 0 (sub-ítem bajo U-EV2-TIPO). Sin dependencias; primer mandato a despachar.
- **Segunda parte de la fase 1**: la autora lee los cinco documentos (empezar por docvig, 14 pp.) y escribe preguntas con criterios y ancla; se sellan por commit. El mandato se calibra con el primer documento leído.
- **Aviso al mentor y a la mentora**: contar la tanda 0 con el pre-registro sellado y preguntar si está bien correrla antes de la lectura del capítulo 3 o esperar. No enviado al cierre.

Regla de la mesa: un mandato por unidad, a Claude Code fresca, revisión del reporte antes del siguiente. La instancia del plan asienta; no ejecuta ni redacta mandatos de ejecución.

## §4. Decisiones abiertas de la autora (sin cambio desde el 24/09 salvo las marcadas)

- Notas rojas de la intro; D-i objetivo 6; cuotas del conjunto final B6.3 (a); confirmación Neo4j para B6.3; `adjudicar.py`; decisión 5 de la intro (nodo Sujeto en Fig. 1; no aparece en el traspaso, NO VERIFICADO si está cerrada).
- Nueva: cuándo y cómo plantear al mentor la duda de estructura (construcción del grafo en el capítulo 3) y la tanda 0; puede ir en un solo mensaje.
- Nueva: guardarraíles de escritura de la mentora (lector par de la carrera, conceptos antes de usarlos, ejemplo único) y U-EJEMPLO: **no asentados a propósito**; son decisiones de prosa para después del ok del capítulo 3.

## §5. Lo que aprendimos esta sesión (para no repetirlo)

- Una sugerencia de mentor no cierra una decisión abierta: se asienta como «sugerido el X, decidido por la autora el Y».
- Dos revisiones independientes (mesa y plan) del mismo entregable recomputaron lo mismo; conviene mantener el circuito.
- Errores de la mesa detectados por la instancia del plan y corregidos: «vigilancia ya asentada» sobre temperatura de E1 (era pendiente); `meta.cost` (es `trace.cost_usd`); tools v2 en la celda Neo4j; el costo de EV2 sobre r1 es USD 7,29 completo (agente + juez + §7), en :305, no juez solo en :303.
- La sesión inventó un «dicho en la reunión del 16/09» a partir del guion; el guion es lo que se llevaba, no lo que se dijo.
- La firma va **antes** del commit que sella (encabezado FIRMADO + fecha); no se commitea un documento «PENDIENTE DE FIRMA» como sello.

## §6. Contradicciones anotadas sin resolver (del 25/09, siguen)

- E1: 395/20.094 rechazos (traspaso, graphrag_comparacion) vs 320/19.838 (U-EXP5). Corridas distintas, sin aclarar.
- `graphrag_comparacion_cap3` «Dónde va» superado (2.2.3 + párrafo 3.6, no `sec:graphrag`).
- Numeración de secciones del cap. 3 en documentos del 11-16/09 corrida en uno respecto del traspaso.
- Documentos viejos usan «conjunto de prueba» para los 10 de validación; la palabra está reservada.
- `diseno_evaluaciones_mentores` §0 tiene al juez EV2 como no corrido; superado.

## §7. Primeros pasos de la próxima sesión

1. Confirmar `git status` limpio salvo `adjudicar.py` y si hubo `git push`.
2. Redactar/enviar el aviso al mentor y la mentora.
3. Mandato de la regla v2 de tipo de pregunta (mesa lo redacta; ejecutora fresca; BORRADOR — PENDIENTE DE FIRMA; reclasificar las 40 de EV2 con v2 como control de que ninguna cambia).
4. Revisar el borrador de B2.2 fase 2 de la instancia del plan; despachar.
5. Mientras, la autora lee docvig y escribe sus preguntas; con eso se calibra el mandato de la segunda parte de la fase 1.


---

## §8. Actualización al cierre del 26/09 (segunda parte del día)

### Commits del día, todos pusheados (remoto en `7d88db3`)
- `41abf18` regla v2 de tipo de pregunta firmada (v1 intacta, sha del bloque = v1; interpretación del 21/09; alcance con oración del procedimiento).
- `b6e5b4d` control del modelo bajo la v2 (U-EV2-TIPO-V2b): 40/40 con el tipo final, 2 cambios vs control v1 (EV2F-014, EV2F-005); claude-sonnet-4-6, T=0, USD 0,3981 en el JSON y en la db.
- `b2174fd`, `99fdf4f`, `798a208` asientos del plan.
- `de8a2b1` **carpeta nueva `docs/mandatos/`**: los mandatos despachados se commitean firmados (decisión de la autora 26/09). Primero: `UB22_fase2_perfil_congelado.md`.
- `f4c8e93` **U-B2.2 fase 2 cerrada, gate 2 de la tanda 0**: `--perfil congelado` en `shapes_validator.py` (vocabulario leído de `prompt_congelado.py`, candado sha `e69feaaa…`), shapes S19 catálogo y S20 enum bloqueantes, S21–S23 informativas, S9 informativa; selftest 57/57; sin perfil byte-idéntico a HEAD. Línea de base de r1 para B2.3 en `reports/shapes_r1_0226e947_congelado_lineabase_B23.json` (sha `c0a91770…`).
- `7d88db3` rescate del scratchpad de la instancia del plan.

### Hallazgos de B2.2 fase 2 (asentados en el plan)
- **Ningún grafo del repo tiene esqueleto v3**: la inyección en `ensamblar_corpus.py` es condicional a `perfil_e1: "v3_b54"` y el manifiesto de desarrollo no lo declara. S15 PASS solo se verá en los grafos de la tanda 0. El gate 2 se cierra como instrumento, no como S15 en verde.
- **Obligacion `ext 10.4.3.1` con `tipo=verificacion_informativa`**, fuera del enum congelado y de los retirados, en r1 y en desarrollo. No se corrige (principio 9); backlog pendiente; vigilancia en la re-extracción C3/C4.
- Tres premisas del mandato del 15/09 estaban caídas (referencia de la corrida 1 anterior a S15; sha de la corrida 2 con fecha adentro; `salida/kg.json` sin esqueleto). Regla nueva: los shas de referencia en mandatos van sobre artefactos sin fecha adentro, y la instancia del plan coteja cada insumo contra HEAD antes de entregar un mandato.

### Incidente y regla nueva de evidencia
- Los scratchpads de las instancias viven en `/private/tmp/claude-501/<repo>/<sesión>/scratchpad/`; macOS los borra. El de la instancia del plan se vació el 26/09 (mandatos reconstruidos desde el registro de sesión; no verificables). **El inventario de B2.1 fase 1 (15/09) y su paquete se perdieron: la fase 1 se rehace**, con salida en `reports/revision_UB21_diag/`.
- Backup de todo `/private/tmp/claude-501` en `~/INGENIERIA IA/TESIS/claude_scratchpads_backup/2026-09-26` (284 MB, fuera del repo).
- Regla: toda evidencia que el plan cite se copia al repo (`reports/`) antes del FRENO; los mandatos despachados van a `docs/mandatos/`. `docs/registro_modelos_BORRADOR.md` ahora vive en el repo.

### Circuito ajustado
- La mesa redacta mandatos; **la instancia del plan los coteja contra los artefactos antes del despacho** (rutas, shas, líneas); la ejecutora ejecuta; la instancia del plan y la mesa revisan el reporte por separado; la autora firma y commitea.

### Gates de la fase 2 de la tanda 0, estado al cierre
1. Cableado de r1 — PENDIENTE. 2. Shapes perfil congelado — **HECHO** (`f4c8e93`). 3. Regression suite — PENDIENTE; antes, re-diagnóstico B2.1 fase 1 (mandato en redacción por la instancia del plan). 4. Runner EV2 Neo4j — PENDIENTE. 5. Registro y carga Neo4j — PENDIENTE. 6. Intrínsecas gen 3 + U-CITA-2 — PENDIENTE. 7. Manifiesto tanda 0 — PENDIENTE.
- Regla v2 de tipo de pregunta: **sellada y controlada** (`41abf18`, `b6e5b4d`); lista para clasificar las preguntas de la tanda 0.

### Decisiones de la autora del 26/09
- No espera el ok del mentor para correr la tanda 0 (decisión 5 del pre-registro y :86 del plan exigirán una enmienda de una línea el día de la corrida si él no respondió). Aviso a mentores: **sigue sin enviarse**.
- Mandatos al repo; S9 informativa; numeración S19–S23; línea de base en `reports/`.

### Primeros pasos de la próxima sesión
1. Recibir de la instancia del plan el mandato de re-diagnóstico de B2.1 fase 1; la mesa lo revisa; firma; `docs/mandatos/`; despacho.
2. Fase 2 de B2.1 con el borrador corregido (ruta `reextraccion_v2/e2_reduce/e2_lib.py`).
3. Mandato de higiene: `adjudicar.py` y entrada del hallazgo S20 en el backlog.
4. La autora: docvig y preguntas; aviso a mentores.
