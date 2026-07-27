# Lectura de resultados contra predicciones selladas — Escalón 1

Documento de lectura del protocolo sellado (protocolo_escalon1.md, brazo v2 = 11f0d4a). Tabla final adjudicada: run_3 31/36 (86,1%) vs grafo_v2 27/36 (75,0%); discordantes b=2 / c=6; fallas compartidas: EV1-011, 018, 028. Toda atribución causal citada proviene de la adjudicación humana registrada (adjudicacion_humana_2026-07-26.json, fichas, deslinde_fallas_v2_2026-07-27.md).

## P1 — REFUTADA en lo global, con causa adjudicada fuera del mecanismo predicho

La predicción (fidelidad v2 ≥ run_3, mejora concentrada en "sujeto" y "enumerativas") no se cumplió: el delta global es −4 y la familia "sujeto" empeoró (3/6 vs 5/6). Sin embargo, la adjudicación caso por caso muestra que **ninguna de las 9 fallas de v2 es atribuible al mecanismo del esquema**: el sistema de sujetos (enum cerrado + reglas + roles) no produjo un solo error en 216 corridas, y las tres fallas de la familia "sujeto" son de capa de contenido o alcance (EV1-015: dato existente no alcanzado, anclado en 10.4; EV1-028: salvedad del 1.1.2.5 ausente del grafo; EV1-029: el 3.1.1.1 esquivo con varianza de réplica). El matiz que la tabla global esconde: **v2 ganó la familia condicional (8/8 vs 7/8)** — precisamente la familia de la amputación de cláusulas — con EV1-035 como emblema: el brazo v2 portaba las condiciones de la excepción (4 unidades, vivienda única, ente público) que run_3 enunció amputadas. La lectura honesta de P1: el esquema cumplió en su territorio; el resultado global lo dominaron capas que la variable única deliberadamente no tocó.

## P2 — MECANISMO PRESENTE, NO OPERANTE: el harness es ciego a la estructura

El esqueleto existe y es navegable (70 nodos, 57 subclase_de, roles con grado 142–655), pero fue usado en solo 9 de 108 trazas (8,3%). En las trazas fallidas de EV1-015, el rol de Clasificación apareció en los resultados de búsqueda de las tres réplicas y el agente nunca lo abrió. La predicción asumía que crear los caminos bastaba para que se caminaran; el dato dice que **el agente congelado (prompt v1, sin conocimiento de la jerarquía) no explota la estructura nueva**. Este es un hallazgo central del escalón: la palanca del esquema requiere co-diseño con el navegador.

## P3 — CONFIRMADA dentro del umbral operativo

Fabricación: 0 casos en ambos brazos. Quimera: 1 caso en v2 (EV1-039, la sonda pre-registrada en acta ANTES de correr — la traza confirmó la vía exacta: los dos nodos con la tabla del 1.2 cruzada) vs 0 en run_3 — diferencia = 1 caso, dentro del umbral ≤1 por especie. Fallas H1 (dato en description no indexada): 2 en v2 (015, 018) vs 1 en run_3 (018, compartida) — diferencia = 1, dentro del umbral. Los controles negativos se comportaron como el protocolo exigía; el episodio de EV1-039 es además la demostración empírica más limpia del hallazgo rector de la tesis: el agente citó nodos reales del grafo y respondió la tabla invertida — grounded ≠ correct, con traza.

## P4 — ACTIVADA Y RE-ESPECIFICADA: el límite vinculante no es el truncamiento sino el no-uso más el presupuesto

Las enumerativas no mejoraron (9 vs 10), lo que activó la atribución candidata pre-registrada (límite-40 de ver_vecinos). La verificación prescripta arrojó un resultado más fino: los cinco roles superan largamente el límite (grado 142–655; todo ver_vecinos sobre un rol truncaría), **pero en las trazas fallidas el agente no consultó ningún nodo rol** — el truncamiento nunca llegó a ejecutarse. El cuello operativo fue la combinación de no-navegación estructural (P2) y agotamiento del presupuesto de herramientas (hit_tool_limit en 5 de 6 trazas fallidas de 015/031, y en 2 de 3 de la 015). P4 queda re-especificada para el siguiente escalón: antes que ampliar el límite de vecinos, el experimento pendiente es un agente que conozca la estructura (y, recién ante hubs efectivamente consultados, un ver_vecinos con orden y paginación).

## P5 — CONFIRMADA: dos costos del esquema documentados

(a) **Herencia sin excepciones ancladas amplifica la confianza en la sobre-generalización**: en EV1-028, el agente de v2 citó la arista miembro_de del esqueleto como evidencia de que los PNFC son sujetos obligados — la jerarquía existe, la salvedad de mutuales/cooperativas no está anclada a ella, y el resultado es un error con mejor respaldo aparente que el de run_3. Regla derivada para el refinamiento: toda arista de membresía con excepciones normativas conocidas debe portar o enlazar sus bloqueadores. (b) La distracción por nodos de esqueleto sin contenido normativo no se evidenció (el agente apenas los visita). 

## Hallazgo no previsto — el juez bajo flag no es confiable; nace el muestreo dirigido

El muestreo humano de los veredictos flaggeados movió 4 mayorías (dos en cada dirección de indulgencia: evasivas aprobadas de v2 en 015/031, no-respuestas aprobadas en ambos brazos en 018, y la amputación de run_3 aprobada en 035 — donde además el juez emitió veredictos opuestos sobre respuestas casi idénticas). Reglas resultantes, ya registradas en acta: todo veredicto flaggeado requiere muestreo humano antes de integrar tablas; el no-determinismo del juez refuerza N=3+mayoría y la vara de piezas esenciales.

## Síntesis del escalón

La pregunta de la variable única queda respondida con precisión: **cambiar solo el esquema — con corpus, harness, agente y juez congelados — no mejoró la fidelidad global (−4), mejoró la familia condicional, eliminó por completo las fallas de mecanismo de sujetos, y desplazó el cuello de botella a tres capas ahora medidas y deslindadas**: extracción de contenido (6 de 9 fallas: una quimera sondeada, tres ausencias, una amputación de calificadores, más la ausencia asimétrica de 011), alcanzabilidad léxica H1 (2 de 9, una compartida), y comportamiento/presupuesto del agente (transversal, con el esqueleto sub-navegado 9/108). Cada capa tiene su intervención natural y su experimento propio — refinamiento de contenido sobre el backlog adjudicado, índice sobre descriptions, y co-diseño agente-estructura — conforme al marco de calidad por etapas: cada mejora, su experimento.
