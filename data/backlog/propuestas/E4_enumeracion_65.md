# Propuesta E4 — Enumeración de niveles del 6.5 (cartera comercial) de Clasificación de Deudores

Entrada del backlog: **BKL-0004** (fuente escalon1_fallas, especie `ausencia`;
retriage v3: `vigente_sin_cambios`, con la confabulación del 7.2 registrada
aparte como BKL-0018).
Formato: `.claude/skills/kg-refinement/references/formato_propuesta.md`.
Precedente de estructura: `data/backlog/propuestas/C1_criterio_11.md`.
Estado: PROPUESTA — la aplicación es otra unidad, post-laudo explícito.

Grafo objetivo: `data/experiment/grafo_v2/reensamblado_v3/kg.json` (vigente).
Fuente de verdad: `data/experiment/subset/TO_clasificacion_deudores_actual.pdf`,
Sección 6, punto 6.5 (verbatim completo extraído como artefacto de la unidad:
`punto_6_5_clasificacion_verbatim_E4.txt` en el paquete de revisión).

```yaml
id_falla: "BKL-0004 (E4 · EV1-011, adjudicada humana 3-0 incorrecta en ambos brazos; ausencia ratificada en retriage v3)"
categoria_defecto: completitud_kg   # especie del backlog: ausencia — la enumeración nominada del 6.5 no existe en ningún nodo de v3 ("seguimiento especial": 0 hits; "en negociacion o con acuerdos": 0 hits)
palanca: grafo/esquema
cambio_exacto: >
  Crear en reensamblado_v3/kg.json 9 nodos y 17 aristas que nodifican la
  enumeración del punto 6.5 (niveles de clasificación de los deudores de la
  cartera comercial) y sus tres situaciones del seguimiento especial.
  Convención de ids verificada contra el código generador de v3
  (data/experiment/grafo_v2/code/assemble_v3.py, entity_slug_v3):
  Obligacion/Restriccion/Excepcion → slug(descripcion)[:80] + sha1(slug)[:6];
  Operacion → slug(label)[:80] + sha1(slug)[:6]. Los 9 ids fueron recomputados
  con esa función y verificados INEXISTENTES en el grafo vigente.

  NODOS (todos con rol_fuente: "restauracion_manual", trazable: no provienen
  del pipeline de extracción; provenance leída del PDF):

  N1 — nodo enumerador (encabezado del 6.5):
    id: "Obligacion_cada_cliente_y_la_totalidad_de_sus_financiaciones_comprendidas_se_incluira_en_un_772a57"
    type: "Obligacion"
    label: "Niveles de clasificación de los deudores de la cartera comercial
            (punto 6.5): cinco categorías — en situación normal, con seguimiento
            especial, con problemas, con alto riesgo de insolvencia, irrecuperable"
    properties:
      descripcion: "Cada cliente, y la totalidad de sus financiaciones
        comprendidas, se incluirá en una de las siguientes cinco categorías,
        las que se definen teniendo en cuenta las condiciones que se detallan
        en cada caso."
      tipo: "criterio_general"
      enumeracion: "6.5.1. En situación normal. · 6.5.2. Con seguimiento
        especial (6.5.2.1. En observación. · 6.5.2.2. En negociación o con
        acuerdos de refinanciación. · 6.5.2.3. En tratamiento especial.) ·
        6.5.3. Con problemas. · 6.5.4. Con alto riesgo de insolvencia. ·
        6.5.5. Irrecuperable."
    provenance: {source_doc: "TO_clasificacion_deudores_actual.pdf",
                 location: "Sección 6. Clasificación de los deudores de la cartera comercial. Punto 6.5. Niveles de clasificación."}
    provenances: [ (la misma) ]

  N2 — nivel 6.5.1:
    id: "Operacion_clasificacion_de_deudor_de_la_cartera_comercial_en_situacion_normal_6_5_1_1a22ee"
    type: "Operacion"
    label: "Clasificación de deudor de la cartera comercial en situación normal (6.5.1)"
    properties:
      tipo: "clasificación de deudor (cartera comercial)"
      descripcion: "El análisis del flujo de fondos del cliente demuestra que
        es capaz de atender adecuadamente todos sus compromisos financieros."
    provenance: {source_doc: "TO_clasificacion_deudores_actual.pdf",
                 location: "Sección 6. Clasificación de los deudores de la cartera comercial. Punto 6.5.1. En situación normal."}

  N3 — nivel 6.5.2 (el nivel que la pregunta fallada pedía desglosar):
    id: "Operacion_clasificacion_de_deudor_de_la_cartera_comercial_con_seguimiento_especial_6_5_2_s_1d1a4b"
    type: "Operacion"
    label: "Clasificación de deudor de la cartera comercial con seguimiento
            especial (6.5.2): situaciones en observación, en negociación o con
            acuerdos de refinanciación, y en tratamiento especial"
    properties:
      tipo: "clasificación de deudor (cartera comercial)"
      descripcion: "Con seguimiento especial. Comprende las situaciones:
        6.5.2.1. En observación; 6.5.2.2. En negociación o con acuerdos de
        refinanciación; 6.5.2.3. En tratamiento especial."
      nota_fuente: "descripcion compuesta de títulos verbatim del 6.5.2; el
        conectivo 'Comprende las situaciones:' no es textual del PDF"
      # LAUDO C-1 (aplicación): la descripcion queda como está y la composición
      # se declara en el propio nodo vía la property nota_fuente de arriba.
      # NOTA: el punto 6.5.2 del PDF es solo el título seguido de sus tres
      # subpuntos, sin párrafo introductorio propio. Esta descripcion es una
      # COMPOSICIÓN ESTRUCTURAL: los cuatro títulos son verbatim del PDF; el
      # conectivo "Comprende las situaciones:" es redacción propia. Flaggeado
      # para el laudo.
    provenance: {source_doc: "TO_clasificacion_deudores_actual.pdf",
                 location: "Sección 6. Clasificación de los deudores de la cartera comercial. Punto 6.5.2. Con seguimiento especial."}

  N4 — situación 6.5.2.1:
    id: "Operacion_seguimiento_especial_situacion_en_observacion_6_5_2_1_cartera_comercial_9ef6cc"
    type: "Operacion"
    label: "Seguimiento especial: situación en observación (6.5.2.1, cartera comercial)"
    properties:
      tipo: "clasificación de deudor (cartera comercial)"
      descripcion: "El análisis del flujo de fondos del cliente demuestra que,
        al momento de realizarse, puede atender la totalidad de sus compromisos
        financieros. Sin embargo, existen situaciones posibles que, de no ser
        controladas o corregidas oportunamente, podrían comprometer la
        capacidad futura de pago del cliente."
    provenance: {source_doc: "TO_clasificacion_deudores_actual.pdf",
                 location: "Sección 6. Clasificación de los deudores de la cartera comercial. Punto 6.5.2.1. En observación."}

  N5 — situación 6.5.2.2:
    id: "Operacion_seguimiento_especial_situacion_en_negociacion_o_con_acuerdos_de_refinanciacion_6_838263"
    type: "Operacion"
    label: "Seguimiento especial: situación en negociación o con acuerdos de refinanciación (6.5.2.2, cartera comercial)"
    properties:
      tipo: "clasificación de deudor (cartera comercial)"
      descripcion: "Incluye aquellos clientes que ante la imposibilidad de
        hacer frente al pago de sus obligaciones en las condiciones pactadas,
        manifiesten fehacientemente antes de los 60 días contados desde la
        fecha en que se verificó la mora en el pago de las obligaciones, la
        intención de refinanciar sus deudas, observando los demás indicadores
        pertinentes del punto 6.5.2.1."
    provenance: {source_doc: "TO_clasificacion_deudores_actual.pdf",
                 location: "Sección 6. Clasificación de los deudores de la cartera comercial. Punto 6.5.2.2. En negociación o con acuerdos de refinanciación."}

  N6 — situación 6.5.2.3:
    id: "Operacion_seguimiento_especial_situacion_en_tratamiento_especial_6_5_2_3_cartera_comercial_8569f5"
    type: "Operacion"
    label: "Seguimiento especial: situación en tratamiento especial (6.5.2.3, cartera comercial)"
    properties:
      tipo: "clasificación de deudor (cartera comercial)"
      descripcion: "Para las refinanciaciones otorgadas por primera vez dentro
        del año calendario y una vez que se haya cancelado la primera cuota de
        dicha refinanciación, el cliente podrá ser reclasificado por única vez
        en esta situación. Luego de la citada refinanciación y a los fines de
        la clasificación, deberá tenerse en cuenta únicamente la mora en el
        atraso de sus obligaciones."
    provenance: {source_doc: "TO_clasificacion_deudores_actual.pdf",
                 location: "Sección 6. Clasificación de los deudores de la cartera comercial. Punto 6.5.2.3. En tratamiento especial."}

  N7 — nivel 6.5.3:
    id: "Operacion_clasificacion_de_deudor_de_la_cartera_comercial_con_problemas_6_5_3_1e9da8"
    type: "Operacion"
    label: "Clasificación de deudor de la cartera comercial con problemas (6.5.3)"
    properties:
      tipo: "clasificación de deudor (cartera comercial)"
      descripcion: "El análisis del flujo de fondos del cliente demuestra que
        tiene problemas para atender normalmente la totalidad de sus
        compromisos financieros y que, de no ser corregidos, esos problemas
        pueden resultar en una pérdida para la entidad financiera."
    provenance: {source_doc: "TO_clasificacion_deudores_actual.pdf",
                 location: "Sección 6. Clasificación de los deudores de la cartera comercial. Punto 6.5.3. Con problemas."}

  N8 — nivel 6.5.4:
    id: "Operacion_clasificacion_de_deudor_de_la_cartera_comercial_con_alto_riesgo_de_insolvencia_6_495c77"
    type: "Operacion"
    label: "Clasificación de deudor de la cartera comercial con alto riesgo de insolvencia (6.5.4)"
    properties:
      tipo: "clasificación de deudor (cartera comercial)"
      descripcion: "El análisis del flujo de fondos del cliente demuestra que
        es altamente improbable que pueda atender la totalidad de sus
        compromisos financieros."
    provenance: {source_doc: "TO_clasificacion_deudores_actual.pdf",
                 location: "Sección 6. Clasificación de los deudores de la cartera comercial. Punto 6.5.4. Con alto riesgo de insolvencia."}

  N9 — nivel 6.5.5:
    id: "Operacion_clasificacion_de_deudor_de_la_cartera_comercial_irrecuperable_6_5_5_36b64c"
    type: "Operacion"
    label: "Clasificación de deudor de la cartera comercial irrecuperable (6.5.5)"
    properties:
      tipo: "clasificación de deudor (cartera comercial)"
      descripcion: "Las deudas de clientes incorporados a esta categoría se
        consideran incobrables. Si bien estos activos podrían tener algún valor
        de recuperación bajo un cierto conjunto de circunstancias futuras, su
        incobrabilidad es evidente al momento del análisis."
    provenance: {source_doc: "TO_clasificacion_deudores_actual.pdf",
                 location: "Sección 6. Clasificación de los deudores de la cartera comercial. Punto 6.5.5. Irrecuperable."}

  ARISTAS (17; todas con la provenance del nodo fuente del dato y
  rol_fuente "restauracion_manual"; endpoints existentes verificados):
    # patrón dominante del grafo: X --establecida_en--> TextoOrdenado
    # (2997 usos; 499 con source Operacion)
    1..9.  N1..N9 --establecida_en--> "TextoOrdenado_to_clasificacion_deudores_actual_pdf"
    # patrón dominante Obligacion --regula--> Operacion (797 usos): el
    # enumerador regula las cinco clasificaciones y las tres situaciones
    10. N1 --regula--> N2
    11. N1 --regula--> N3
    12. N1 --regula--> N4
    13. N1 --regula--> N5
    14. N1 --regula--> N6
    15. N1 --regula--> N7
    16. N1 --regula--> N8
    17. N1 --regula--> N9
  LÍMITE DE VOCABULARIO (flaggeado para el laudo): la pertenencia de las
  situaciones N4-N6 al nivel N3 pediría una arista Operacion→Operacion, pero
  el grafo vigente tiene CERO aristas Operacion→Operacion y las relaciones
  jerárquicas (subclase_de/parte_de/instancia_de/miembro_de) son 100%
  Sujeto→Sujeto. Crear una relación nueva es decisión de esquema que excede
  esta propuesta; la pertenencia queda portada léxicamente (labels de N4-N6
  arrancan con "Seguimiento especial:", y N3 enumera sus tres situaciones en
  label y descripcion). Si la adjudicadora prefiere la arista jerárquica
  explícita, es un agregado de esquema a laudar aparte.
cita_pdf: >
  [TO_clasificacion_deudores_actual.pdf, Sección 6, punto 6.5, pág. 3 del
  rótulo interno de sección — verbatim]: "Cada cliente, y la totalidad de sus
  financiaciones comprendidas, se incluirá en una de las siguientes cinco
  categorías, las que se definen teniendo en cuenta las condiciones que se
  detallan en cada caso."
  Títulos de los subpuntos (verbatim, con su pág. interna): "6.5.1. En
  situación normal." (pág. 3) · "6.5.2. Con seguimiento especial." (pág. 4) ·
  "6.5.2.1. En observación." (pág. 4) · "6.5.2.2. En negociación o con
  acuerdos de refinanciación." (pág. 6) · "6.5.2.3. En tratamiento especial."
  (pág. 7) · "6.5.3. Con problemas." (pág. 7) · "6.5.4. Con alto riesgo de
  insolvencia." (pág. 10) · "6.5.5. Irrecuperable." (pág. 12).
  Los párrafos definicionales citados en cada properties.descripcion (N2,
  N4-N9) son el primer párrafo (en N4, los dos primeros) de su subpunto,
  verbatim con guiones de corte de línea normalizados. El texto completo del
  6.5 (723 líneas de layout, incluidos los indicadores 6.5.x.y que esta
  propuesta NO nodifica) está en el artefacto
  punto_6_5_clasificacion_verbatim_E4.txt del paquete de revisión;
  reproducción: pdftotext -layout data/experiment/subset/TO_clasificacion_deudores_actual.pdf - | sed -n '835,1557p'
como_se_verificaria: >
  RE-TEST pre-especificado, en tres capas:
  (1) chunk-contra-PDF: releer el punto 6.5 del PDF (vía de cierre declarada
  en BKL-0004) y confirmar que cada properties.descripcion coincide
  literalmente con su subpunto, que la enumeracion de N1 reproduce los títulos
  sin agregar ni quitar categorías, y que las provenances dicen Sección 6 /
  punto correcto. EV1-011 está QUEMADA: no participa del re-test.
  (2) estructural: los 9 ids no colisionan, las 17 aristas existen y todos los
  endpoints resuelven (cero colgantes); los 39 nodos con provenance en el 7.2
  permanecen byte-idénticos.
  (3) réplica del índice (GraphIndex real sobre v3 + nodos en memoria, ya
  medida en esta propuesta — ver tabla): las queries reales del agente en las
  3 réplicas falladas devuelven los nodos propuestos dentro del corte de 10.
  PREGUNTAS NUEVAS DE VERIFICACIÓN (ninguna de EV1/CQ/CQN/CQN2; gold anclado
  en el verbatim de esta propuesta):
  RT-1 "¿En cuántas categorías debe incluirse cada cliente de la cartera
       comercial según el punto 6.5 y cómo se denomina cada una?" — gold:
       cinco; en situación normal / con seguimiento especial / con problemas /
       con alto riesgo de insolvencia / irrecuperable.
  RT-2 "¿Qué situaciones comprende la categoría 'con seguimiento especial' de
       la cartera comercial?" — gold: en observación (6.5.2.1); en negociación
       o con acuerdos de refinanciación (6.5.2.2); en tratamiento especial
       (6.5.2.3).
  RT-3 "¿Dentro de qué plazo debe manifestarse la intención de refinanciar las
       deudas para que un cliente sea clasificado 'en negociación o con
       acuerdos de refinanciación'?" — gold: fehacientemente antes de los 60
       días contados desde la fecha en que se verificó la mora.
  RT-4 "¿Bajo qué condiciones y cuántas veces puede reclasificarse a un
       cliente de cartera comercial en la situación 'en tratamiento
       especial'?" — gold: refinanciaciones otorgadas por primera vez dentro
       del año calendario, una vez cancelada la primera cuota; por única vez.
  RT-5 (control de no-regresión / deslinde, puente con BKL-0018): "¿El nivel
       'Riesgo medio' pertenece a la clasificación de la cartera comercial?" —
       gold: no; es un nivel del punto 7.2 (cartera de consumo y/o vivienda).
       Verifica que la corrección no mezcló regímenes y que la respuesta a
       RT-1 no importa niveles del 7.2.
categoria_riesgo: alto
justificacion_riesgo: >
  Aplicando el criterio fijo: la propuesta CREA estructura nueva (9 nodos, 17
  aristas), elige labels por medición de alcanzabilidad y contiene una
  descripcion compuesta (N3) — "creación de estructura nueva (aristas, tipos)"
  está enumerada como alto → revisión humana. Las descripciones N2, N4-N9 son
  transcripción literal, pero la decisión de des-colapso (qué nodifica y qué
  no) es juicio de modelado.
```

## Nota de anclaje (por qué el PDF y no la ficha ni el chunk)

La enumeración nominada del 6.5 no existe en v3: las sondas "seguimiento
especial" y "en negociacion o con acuerdos" dan 0 hits sobre id+label+
properties de los 4459 nodos del grafo vigente (mapeo delta v2→v3, §EV1-011:
`no_recuperable_por_v3`; reverificado en esta unidad). El 6.5 sí fue extraído
en 6 partes — 116 nodos de reglas sueltas portan provenance "Punto 6.5.
Niveles de clasificación. (parte 1..6)" — pero ninguno nodifica la enumeración
ni los nombres de las categorías: el des-colapso que v3 sí hizo para el 7.2
(niveles nominados como nodos `Operacion`) no ocurrió para el 6.5. Esta
propuesta restaura esa capa faltante con ancla EXCLUSIVA en el PDF (regla de
la unidad: la fuente de verdad es el PDF, no la ficha ni la respuesta del
agente); la provenance se escribe leída del PDF (Sección 6, puntos 6.5 a
6.5.5), no copiada de los chunks (parte 1..6).

## Verificación de alcanzabilidad léxica (medida, índice replicado)

Réplica del `GraphIndex` real (`data/experiment/evaluacion/harness.py`, tokens
sobre label+id) sobre v3 + los 9 nodos propuestos agregados EN MEMORIA (el
kg.json no se tocó). Las tres primeras queries son las que el agente Haiku usó
textualmente en las réplicas falladas de EV1-011; el resto, variantes
plausibles. Rank dentro del corte de 10:

| Query | Nodos propuestos en top-10 (rank) |
|---|---|
| "niveles clasificación deudores cartera comercial" (traza r1-r3, paso 1) | N1:1 · N7:4 · N9:5 · N2:6 · N3:8 |
| "seguimiento especial deudores" (traza r1-r3, paso 2) | N1:1 · N4:3 · N6:4 · N5:5 · N3:6 |
| "punto 6.5 niveles clasificación" (traza r1, paso 15) | N1:1 · N7:2 · N9:3 · N2:4 · N8:5 · N3:6 |
| "situaciones que integran el seguimiento especial" | N3:7 |
| "cinco categorías cartera comercial" | N1:1 · N7:7 · N9:8 · N2:9 · N4:10 |
| "en negociación o con acuerdos de refinanciación" | N5:1 · N3:2 |
| "situación normal cartera comercial" | N2:1 · N1:2 · N4:3 · N6:4 · N5:5 |

(La variante de labels sin "cinco categorías" en N1 y sin la enumeración de
situaciones en N3 dejaba fuera del top-10 a N1 en la query "cinco categorías
cartera comercial" y a todos en "situaciones que integran el seguimiento
especial"; la variante adoptada cubre las 7.)

## Qué NO se toca

- **Los 39 nodos con provenance en el "Punto 7.2. Niveles de clasificación"
  quedan intactos** — incluidos los 6 confusores señalados por el laudo 1b
  (`Operacion_clasificacion_en_nivel_situacion_normal_94ca1a`,
  `Operacion_clasificacion_en_nivel_riesgo_bajo_en_observacion_48fdc5`,
  `Operacion_clasificacion_en_nivel_riesgo_bajo_en_tratamiento_especial_a3a9d8`,
  `Operacion_clasificacion_en_nivel_riesgo_medio_61a12e`,
  `Restriccion_comprende_a_los_clientes_con_atrasos_de_mas_de_180_dias_hasta_un_ano_41d23c`,
  `Restriccion_comprende_a_los_clientes_insolventes_o_en_quiebra_con_nula_o_escasa_posibilidad__38a205`).
  Son legítimos de su régimen (7.2, cartera de consumo y/o vivienda); el
  defecto adjudicado es la AUSENCIA del 6.5, no la existencia del 7.2. La
  lectura del expediente es consistente con esto: sin desvío que reportar.
- La anotación/deslinde de régimen sobre los nodos del 7.2 es **BKL-0018**
  (acoplada a esta corrección, propuesta separada post-laudo de esta).
- No se nodifican los indicadores internos 6.5.x.y (6.5.1.1-6.5.1.6,
  6.5.3.1-6.5.3.12, 6.5.4.1-6.5.4.10, 6.5.5.1-6.5.5.9): varios ya existen como
  nodos sueltos de las partes 1..6 y duplicarlos crearía colisiones de
  contenido; cualquier enriquecimiento es otra propuesta.
- Ningún nodo ni arista existente se modifica o borra; el cambio es aditivo.

## Observación no bloqueante (conteo del 7.2)

El expediente E4 (§d) declara "33 nodos" con provenance en el 7.2; el conteo
reproducible hoy sobre el grafo vigente da 39 (37 excluyendo el nodo
`TextoOrdenado` y la `Comunicacion`):
`python3 - <<'PY' ... location startswith "Punto 7.2. Niveles de clasificación" and source_doc == "TO_clasificacion_deudores_actual.pdf" ... PY`
(comando completo en el paquete de revisión). La diferencia no afecta esta
propuesta (el 7.2 no se toca); se deja constancia para el laudo.
