# Nota de re-adjudicación — vara v3 (casos-control de run_3)

**Fecha:** 2026-07-15.

## Motivación

Los GTs de los casos-control los escribí el 2026-07-10, bajo la taxonomía vigente en ese
momento y con evidencia parcialmente fundada en las trazas almacenadas. Desde entonces pasaron
dos cosas que dejan a esa vara desincronizada del instrumento que debe calibrar. Primero, la
taxonomía llegó a v2.6.1: la prueba de alcanzabilidad se precisó como prueba **ex ante**
(v2.1), "pertinente" quedó definido por el test del nodo único (v2.2), el soporte de un claim
pasó a evaluarse contra TODO lo expuesto en los outputs completos de la trayectoria
(v2.3/v2.4), apareció la causa `aplicacion_erronea` (v2.5) y su criterio de desambiguación por
des-scoping (v2.6). Segundo, una auditoría de truncamiento demostró que **las trazas
almacenadas no son el contexto del agente**: el harness pasa outputs completos y almacena
truncados a 1.200 caracteres, así que toda afirmación de ausencia fundada solo en la traza
almacenada es inválida como evidencia.

Por eso re-expreso los GTs en la taxonomía vigente y re-fundo su evidencia en re-ejecuciones
determinísticas de las trayectorias y en barridos programáticos sobre el grafo congelado,
todos trackeados en `docs/evidencia_vara_v3/`. El objetivo es que la calibración mida al
verificador, y no la desincronización de vocabularios entre una vara vieja y una taxonomía
nueva, ni la diferencia entre lo que la traza almacenó y lo que el agente realmente vio.

**Disclosure.** Esta re-adjudicación ocurre **después** del gate #2. Los veredictos del
verificador permanecieron sellados durante todo el proceso: no se abrió ningún archivo de
`gate2_v57/` en ninguna de las tareas que produjeron la evidencia ni en esta escritura (cada
reporte de evidencia lista los archivos que abrió). El gate se reporta con **doble lectura**
— lectura A contra la vara anterior (`5bb58c0`), lectura B contra esta vara v3 — y ambas se
publican juntas, siempre.

**Evidencia (4 archivos, trackeados):**
- `docs/evidencia_vara_v3/expediente_readjudicacion.md` — vara anterior verbatim, taxonomía v2.6.1 verbatim, evidencia previa por caso.
- `docs/evidencia_vara_v3/auditoria_truncamiento_run3.md` — re-ejecución determinística de las trayectorias de CQ-017/020/031/034 (56/56 pasos verificados por igualdad de largos) y barridos de ausencia sobre outputs COMPLETOS.
- `docs/evidencia_vara_v3/evidencia_cq034.md` — respuesta del agente y veredictos del juez (frozen + post-hoc) para CQ-034; barrido del límite del 3.9.
- `docs/evidencia_vara_v3/verificaciones_vara_v3.md` — barridos programáticos sobre el grafo congelado (4.050 nodos, 6.634 edges) y simulación del índice léxico.

---

## CQ-025

**GT anterior (verbatim, `5bb58c0`):**

> - **Pata 1 (riesgo de mercado) — `{noise_sensitivity, contenido_kg}`, PRIMARIA (defecto de grafo):** el PDF (Punto 1.1 del TO de Régimen Informativo) ubica los datos de riesgo de mercado (puntos 4.3-4.5) en la lista de excepciones **trimestrales**. Pero el nodo `Operacion_calculo_de_riesgo_de_mercado` del grafo dice "mensual" — claim soportado por el nodo consultado pero incorrecto contra el PDF. El extractor confundió: en el pasaje, "mensual" califica al **código de consolidación** ("consolidado mensual"), no a la frecuencia de reporte, que es **trimestral** según el encabezado del bloque. El nodo afirma un contenido que contradice el PDF → `contenido_kg`.
> - **Pata 2 (ratio de apalancamiento) — falso positivo del juez (NO defecto de grafo ni de agente; sin par v2 — no es defecto del sistema):** el agente respondió correctamente que el apalancamiento es **trimestral** y citó bien el Punto 10.1 (verificado contra el PDF: el Punto 10.1.1 contiene "los datos se informarán con frecuencia trimestral"). El juez marcó esa afirmación como falsa, pero era correcta → ruido del juez, no un defecto del sistema.

**GT v3:** IDÉNTICO — par `{noise_sensitivity, contenido_kg}` primaria en pata 1, pata 2
falso positivo del juez, misma regla de acierto.

**Qué cambió y por qué:** nada en el par, la jerarquía, las patas ni la regla de acierto. Se
agrega la **exclusión explícita de `aplicacion_erronea`** caminando el test v2.6, porque la
categoría no existía cuando escribí el GT y este caso es exactamente el que la motivó: dejo a
la vista que la rama "nodo fiel" no se alcanza (el nodo contradice al PDF, el defecto es de
contenido, no de aplicación). Se agrega además la línea de disclosure de la relación
caso↔taxonomía: este caso expuso en el gate #1 el hueco "nodo fiel mal aplicado" y motivó la
creación de `aplicacion_erronea` (v2.5).

**Evidencia:** `docs/evidencia_vara_v3/expediente_readjudicacion.md` §1 (vara anterior
verbatim) y §2 (taxonomía v2.6.1: rama `noise_sensitivity` y criterio v2.6). CQ-025 quedó
fuera de la auditoría de truncamiento porque su GT no depende de afirmaciones de ausencia.

---

## CQ-017

**GT anterior (verbatim, `5bb58c0`):**

> - **Causa primaria — `{context_recall, estructural_kg}` (pata 2):** falta la arista cross-documento que une Protección (Punto **1.1.2.2**, operador de cambio alcanzado) con Exterior y Cambios (Punto **1.1**, entidad autorizada en el mercado de cambios). Sin esa conexión, la **pata 2** de la pregunta queda sin responder (el contexto que la conecta nunca apareció en la trayectoria).
> - **Causa primaria — `{noise_sensitivity, provenance_imprecisa}` (pata 1):** el nodo del operador de cambio tiene provenance a nivel grueso (**"Punto 1.1"**) en vez del específico (**"1.1.2.2"**). El agente reportó fielmente lo que el nodo decía (citó 1.1) — claim soportado por el nodo pero incorrecto contra el GT —, y por eso el juez marcó la **pata 1** como incorrecta pese a que el contenido era correcto.

**GT v3:** IDÉNTICO en pares, jerarquía (dos primarias), patas y regla de acierto ("ambas o
no es acierto").

**Qué cambió y por qué:** solo la **fundación de la evidencia**. El GT anterior afirmaba
ausencias apoyándose en la traza almacenada; la auditoría de truncamiento demostró que ese
apoyo no vale (el paso 10 de esta trayectoria tenía 11.828 caracteres en runtime y 1.216 en
la traza). La ausencia queda ahora demostrada contra outputs COMPLETOS re-ejecutados
("1.1.2.2", los portadores de la regla de Exterior 1.1 y el texto "entidad autorizada":
ausentes en los 15 pasos) y contra barridos programáticos del grafo entero: el nodo del
operador de cambio tiene exactamente 2 edges, ambos internos a Protección, con provenance
verbatim "Punto 1.1. Partes."; los 3 nodos del grafo que mencionan "entidad autorizada" no
tienen ningún edge con él; y sobre los 6.634 edges del grafo hay **0 aristas** entre un nodo
del operador y uno de entidad-autorizada/mercado-de-cambios. Se suma como refuerzo el hecho
del paso 10: el grafo SÍ expone 13 edges cross-documento desde `sujeto_obligado` hacia
operaciones de Exterior y ninguno porta la regla del 1.1 — lo que falta es la conexión
específica. Se agrega la **exclusión de `aplicacion_erronea` en la pata 1** (test v2.6,
categoría posterior al GT anterior): el nodo es fiel y pertinente; su defecto es la cita, no
el alcance.

**Evidencia:** `docs/evidencia_vara_v3/auditoria_truncamiento_run3.md` §3;
`docs/evidencia_vara_v3/verificaciones_vara_v3.md` §1 (1a-1d).

---

## CQ-031

**GT anterior (verbatim, `5bb58c0`):**

> **Atribución humana (re-adjudicada por la autora, 2026-07-10):** defecto del grafo → **`{context_recall, alcanzabilidad_kg}`**, ÚNICA primaria, pata 4.5. Evidencia: el nodo poblado `Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti` existe con el 4.5 verbatim en `properties.descripcion` ("Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas A no serán objeto de clasificación"), pero `buscar_nodos` indexa solo label/id; las búsquedas del agente en la traza (pasos 7, 9 y 11) no lo alcanzaron y la pata se respondió con la cesión del 4.6. Señal de `context_recall` en los propios datos del juez: `cobertura_patas` marca la pata "qué deudores no deben ser objeto de clasificación" como `no_cubierta`.

**GT v3:** IDÉNTICO en par (`{context_recall, alcanzabilidad_kg}`, única primaria, pata 4.5),
exclusión de la pata 4.4 y regla de acierto.

**Qué cambió y por qué:** la evidencia se reescribe caminando la **prueba ex ante v2.1 con
hechos medidos**, cosa que el GT anterior no podía hacer (la v2.1 es posterior y la medición
del índice no existía). Los hechos: "garantías" no está en la pregunta; fue expuesto al
agente en outputs completos desde el paso 2; el agente lo incorporó y lo usó en 4 búsquedas
desde el paso 8. Eso permite la **exclusión EMPÍRICA de `navegación`**: el agente ejecutó las
búsquedas razonables con el mejor vocabulario disponible y el índice no devolvió el portador —
0/10 apariciones en top-10, mejor rank 13. Y el mecanismo queda confirmado: el id truncado
del portador indexa el token `garanti`, que el token de búsqueda `garantias` no matchea
(score 0 en las consultas "garantías preferidas A" sin otra palabra del portador), mientras
que las consultas con palabras del propio nodo lo devuelven en posición 1. Además: (i) toda
cita a la auditoría GT previa (que vivía en un directorio no versionado) se reemplaza por las
secciones equivalentes del archivo trackeado de verificaciones — con esto cae también el
erratum que la acompañaba —; (ii) se consigna un **hallazgo lateral, explícitamente NO
secundaria del GT**: la provenance del portador dice "Punto 4.4" y su `descripcion` porta la
regla del 4.5 — una `provenance_imprecisa` latente que no participó de esta falla (el nodo
nunca fue alcanzado; corregir su provenance no cambia el caso) y queda para el backlog de
refinamiento.

**Evidencia:** `docs/evidencia_vara_v3/verificaciones_vara_v3.md` §2 (2a lookup y descripcion
verbatim; 2b tokens; 2c simulación de las 10 consultas; 2d simulación inversa);
`docs/evidencia_vara_v3/auditoria_truncamiento_run3.md` §1 (portador ausente en los 15
outputs completos; inventario de vocabulario ex ante).

---

## CQ-020

**GT anterior (verbatim, `5bb58c0`):**

> - **Causa primaria — `{context_recall, completitud_kg}` (defecto del grafo):** falta el nodo de **frecuencia de reporte para riesgo de crédito**; por su ausencia el agente **mis-aplica el nodo de frecuencia de riesgo de mercado**. Por la [regla de precedencia](taxonomia.md) el síntoma es `context_recall`: el nodo de riesgo de mercado NO cuenta como contexto de la pata de crédito (es un nodo de otro tema usado para rellenar), así que el dato pertinente nunca apareció en la trayectoria. Es lo que mueve el veredicto, y lo que un refinamiento del grafo podría arreglar.
> - **Causa secundaria — `{faithfulness, alucinacion_agente}` (defecto del agente; v1: generación-de-más — correcto en sustancia; lo que se corrige es QUÉ claims la componen):** la compone el claim **"0,08 es el coeficiente de capital mínimo"**, modo (b) del árbol (glosa de cosecha propia): ningún nodo del grafo ni pasaje del PDF lo nombra así (barridos de `70100000`/`0,08`/`APRc` sobre todos los campos + verificación contra 2.1 y 8.5.3 del corpus) — la evidencia es la constancia de búsqueda + la verificación negativa contra el PDF, sin nodo que exhibir. El otro claim `no_soportado` del juez —la fórmula alternativa "Código 70100000 (n) = …"— es **falso positivo del juez** (sin par v2 — no es defecto del sistema): está soportado por un nodo que el agente SÍ consultó (`Operacion_calculo_de_exigencia_por_riesgo`, `ver_nodo` en el paso 6 de su trayectoria) y es correcto contra el PDF (8.1.1); el juez es ciego al grafo y no podía verlo.

**GT v3:** primaria `{context_recall, completitud_kg}` IDÉNTICA (re-fundada). **La secundaria
`{faithfulness, alucinacion_agente}` SE DISUELVE**: el claim del 0,08 se re-adjudica como
**falso positivo del juez (sin par)**. El FP del 70100000 se mantiene tal cual. Regla de
acierto: sin cambio (detectar la primaria; la secundaria nunca fue exigida).

**Qué cambió y por qué:** dos cosas. (1) La **primaria se re-funda** en evidencia
determinística: ningún output de los 11 pasos asocia una frecuencia de reporte al riesgo de
crédito (los matches de frecuencia son de riesgo operacional, de riesgo de mercado, o del
nombre del archivo PDF en las provenances); la frecuencia general del R.I.-C.M. existe en el
grafo solo como location de provenance del nodo TextoOrdenado, no en las properties de ningún
nodo; y los 2 únicos nodos del grafo que combinan frecuencia con riesgo de crédito
(incrementos por excesos; incumplimientos de Grandes Exposiciones) se excluyen por el test
v2.2 — comparten tema pero no portan LA RESPUESTA a la pata (la frecuencia de reporte de la
exigencia CRC) — y además ninguno fue expuesto en la trayectoria. (2) La **secundaria se
disuelve** porque su fundamento fáctico era falso: el barrido del GT anterior usó variantes
léxicas equivocadas — "APRc" sin guion bajo y "0.08" con punto dan ausente, pero "0,08" y
"APR_c" dan presente (4 y 3 nodos respectivamente). El claim "0,08 es el coeficiente de
capital mínimo" está soportado por contenido EXPUESTO: los nodos abiertos con `ver_nodo` en
los pasos 4 y 6 exponen el coeficiente 0,08 en las fórmulas de la exigencia por riesgo de
crédito (paso 4, `Operacion_calculo_de_capital_minimo`: "C_RC = (k x 0,08 x APR_c) + INC";
paso 6, `Operacion_calculo_de_exigencia_por_riesgo`: "Código 70100000 (n) = k x 0,08 [ … ]"),
y esa fórmula es fiel al PDF (verificación contra el 8.1.1 ya registrada en la adjudicación
anterior). Caminando el árbol vigente: con soporte → `noise_sensitivity` → nodo fiel →
pertinente → `sin_defecto` (falso positivo del juez). Documento la corrección del barrido
para que el mecanismo del error quede a la vista. Consecuencia estructural: el set de
casos-control ya no contiene ninguna causa lado agente — disclosure agregado en la sección de
cobertura de la vara.

**Evidencia:** `docs/evidencia_vara_v3/auditoria_truncamiento_run3.md` §4 (4a barrido de
frecuencia en outputs; 4b barrido del kg con los 2 nodos marginales citados íntegros y su
ausencia en la trayectoria; 4c exposición del nodo de mercado);
`docs/evidencia_vara_v3/verificaciones_vara_v3.md` §3 (3a frecuencia general del R.I.-C.M.;
3b barrido "0,08"/"0.08"/"70100000"/"APRc"/"APR_c" con contenidos íntegros).

---

## CQ-034

**GT anterior (verbatim, `5bb58c0`):**

> **Atribución humana (confirmada — verificada contra el PDF):** defecto del grafo → **`{context_recall, completitud_kg}`**, primaria (límite faltante en la extracción — el dato pertinente nunca apareció en la trayectoria). Los límites son literales en el PDF: USD 100 con efectivo (3.8) y USD 200 para otras modalidades (3.9) del TO de Exterior.

**GT v3:** par `{context_recall, completitud_kg}` primaria, **RE-SCOPEADO a las dos patas
faltantes**: límite con débito en cuenta y límite general del 3.9 para otras modalidades. La
pata del efectivo/USD 100 (3.8) se consigna explícitamente como **SIN DEFECTO** de grafo,
agente ni juez. **Regla de acierto ENDURECIDA:** acierto = detectar
`{context_recall, completitud_kg}` como primaria, Y atribuir un defecto a la pata del
efectivo INVALIDA el acierto. Palanca: BAJO riesgo, con justificación corregida.

**Qué cambió y por qué:** el GT anterior afirmaba "el dato pertinente nunca apareció en la
trayectoria" para el caso entero, y la auditoría de truncamiento **refutó esa ausencia para
la pata del efectivo**: el nodo `Restriccion_limite_mensual_de_compra_en_efectivo` existe con
`umbral: "USD 100"` y provenance al Punto 3.8, fue expuesto en el paso 1, abierto completo
con `ver_nodo` en el paso 4, la respuesta lo usó bien y el juez lo confirmó (claim único
marcado "verdadero"; las 3 reps del frozen unánimes: correcta / parcial / cero afirmaciones
no soportadas). Para las patas que sí faltan, la ausencia queda demostrada con barridos
programáticos: "otras modalidades" da 0 matches en los 4.050 nodos; el único "USD 200" del
grafo es de otro alcance (retiros de efectivo en países no limítrofes, Punto 4.1); "A07" y
"A09" están ausentes de los outputs; el nodo de débito en cuenta enuncia la obligación sin
monto; y ningún nodo del grafo combina débito con un límite. Consigno además la **conducta
del agente como hallazgo**: declaró la ausencia honestamente (`respondible: false`, en las 4
respuestas registradas), buscó un límite de 300 dólares en cuatro consultas (pasos 9, 10, 13
y 14) y no lo afirmó — abstención ante el hueco en lugar de relleno con priors. La regla de
acierto se endurece porque la pata del efectivo está sana: un verificador que le atribuya un
defecto (p. ej. alucinación o navegación) está fabricando un falso positivo, y eso es
exactamente lo que la calibración debe penalizar. La palanca baja de riesgo con justificación
corregida: el grafo ya contiene el nodo espejo exacto
(`Restriccion_limite_mensual_de_compra_en_efectivo`, tipo `limite_cuantitativo`, campo
`umbral`); crear los faltantes es replicar un patrón existente con un valor literal único del
PDF — bajo = transcripción sobre patrón existente; alto = modelado nuevo (criterio
consistente con CQ-020).

**Evidencia:** `docs/evidencia_vara_v3/auditoria_truncamiento_run3.md` §2 (exposición y
apertura del nodo USD 100; barrido término por término; tabla resumen);
`docs/evidencia_vara_v3/evidencia_cq034.md` §1 (respuesta del agente verbatim, 4 registros),
§2 (veredictos del juez frozen por rep + agregado unánime + registro por claim y
cobertura_patas del juez post-hoc), §3 (barrido del 3.9 sobre el kg);
`docs/evidencia_vara_v3/verificaciones_vara_v3.md` §4 (nodo de débito íntegro; barrido
débito+límite).
