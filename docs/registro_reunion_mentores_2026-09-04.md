# Registro de la reunión de mentores del 04/09/2026

Registro de los mandatos técnicos y decisiones de la reunión, extraídos de
mis notas contemporáneas. Rige la convención del proyecto: cero nombres
propios de personas; cada decisión se documenta por su justificación
técnica. Complementa (no reemplaza) los puntos de agenda del plan
(`docs/plan_tesis.md`), que este registro cierra o mantiene vigentes según
se indica.

Material presentado: las evaluaciones del esquema pre-escalado (carril ESQ
completo: falsación del test ciego, ESQ-2 con 75 fichas, retoques ESQ-3 y
esquema congelado `2593d4d`), la barrida de related work de releases, la
Introducción escrita, y la existencia de un contacto de la industria
bancaria dispuesto a colaborar. Recepción general: aval al material
presentado; los mandatos siguen.

## 1. Gate de validación del esquema: lectura del capítulo (reemplaza toda alternativa experimental)

Mandato: escribir en el informe (Overleaf) el **capítulo de esquema y
validación pre-escalado**, completo — diseño del esquema, procedimiento,
metodología, catálogo de sujetos, las evaluaciones pre-escalado sobre los
10 TOs nuevos, las fichas adjudicadas, el esquema nuevo y cómo está
testeado. Los mentores lo leen y **validan metodología y esquema por
lectura** (motivo declarado: en la reunión no se captan bien metodologías y
números). Validado el capítulo, el esquema queda habilitado para escalar.

Consecuencias registradas:

- El punto CONSULTADO de la agenda (riesgo 15/157; ¿test de generalización
  adicional con TOs vírgenes?) queda **respondido por esta vía**: no se
  ordenó test adicional; la validación externa toma la forma de lectura del
  capítulo. La ventana de la tanda 1 (laudo `2593d4d` §7) sigue vigente
  como mitigación operativa.
- El escalado queda **gateado a la validación del capítulo**, además de sus
  prerrequisitos internos (B5.3–B5.5).
- Unidad derivada: **U-CAP-ESQ** (escritura del capítulo; esqueleto previo
  aprobado por la autora; fuentes exclusivamente los documentos sellados
  del carril ESQ; rigen la skill de escritura de tesis y el mapa de
  fuentes, como en la Introducción).

## 2. Actualización ante cambio normativo (exigencia 7 del mapa): pasa de hueco a compromiso

Mandato: diseñar un **job recurrente mensual** que re-scrapee los Textos
Ordenados, persista versiones con su procedencia documental (qué documento
salió de qué resolución), detecte los **deltas** contra el corpus que tengo
(scrapeado en marzo de 2026 y congelado por sha en
`data/experiment/escalado_prep/`), y — apoyándose en que el grafo registra
procedencia por elemento — **mapee qué partes del grafo quedaron afectadas**
por cada cambio, para actualizar solo esas. Reacción registrada: el
mecanismo es importante y **tiene que estar** en la tesis.

- La exigencia 7 del mapa de related work (`docs/mapa_related_work.md` §2)
  pasa de PARCIAL a **compromiso de diseño con forma definida** (la
  actualización del estado en el mapa viaja con la unidad que lo diseñe).
- **Sinergia registrada y endosada por la mesa revisora** (se escribe
  también en el diseño de la unidad, para que no viva solo en sesiones): el
  corpus congelado es de marzo de 2026, de modo que **la primera corrida
  del job produce el delta marzo→presente: material normativo posterior al
  corte de construcción**, que es exactamente el insumo que la exigencia 6
  (validación temporal, precedente PrimeKG) necesita. Un diseño alimenta
  dos exigencias; la decisión de usar ese delta como validación temporal
  sigue siendo propia (la exigencia 6 no se trató explícitamente, ver §5).
- El scraper idempotente con manifiesto ya existe (`src/`); la unidad nueva
  diseña scheduling, tabla de deltas por sha, mapeo delta→provenance→partes
  afectadas y reporte mensual. La ejecución de la actualización del grafo
  puede quedar como release declarada (principio 9).
- Unidad derivada: **U-JOB-ACT** (diseño, $0; construcción con laudo
  propio).

## 3. Validación experta del recurso (exigencia 3 del mapa → B4): protocolo acordado

La colaboración con la industria queda encuadrada como **anotación
experta**: en la tesis se puede afirmar que el método de generación del
grafo fue verificado por expertos si un experto del dominio actúa de
anotador sobre un **subsample**, y se reportan métricas de performance con
estadística sobre esa muestra (la práctica de intervalos sobre muestra ya
está estrenada en ESQ-2). Dos modos registrados:

- **Literal**: presentar tripletas (dos nodos y una arista) y preguntar si
  están bien.
- **Conversacional**: conversación estructurada grabada (con permiso),
  preguntas generales de compliance; de la conversación se extraen claims
  (con asistencia LLM) y se verifica si esas relaciones existen en el
  grafo; lo que no se pueda reciclar de la conversación se pregunta
  directo.

Destino en el plan: alimenta **B4** (precisión sobre muestra con
adjudicación humana — exigencia 3) y el diseño del pipeline de evaluación
puede recibir aporte de la industria (datos, validación); se explora en la
reunión con el contacto.

## 4. Reunión con el contacto de la industria: encuadre acordado

- La reunión próxima es **exploratoria, no de demostración**: preguntas
  generales sobre sus procesos (¿usan RAG?; procesos de compliance;
  proyectos), sin forzar el caso de uso del grafo en la conversación.
  Después proceso lo escuchado a solas y vuelvo con una propuesta concreta.
- **Grabar con permiso.**
- El guion de preguntas se prepara por separado (unidad U-PREP-CONTACTO,
  $0); la propuesta posterior puede incluir los dos modos de anotación del
  §3 y el eventual aporte al pipeline de evaluación.

## 5. Puntos NO tratados explícitamente (se registran para que no se promuevan solos)

- **Exigencia 6 (validación temporal) como decisión formal**: no se trató;
  queda como decisión de diseño propia, con el insumo del §2.
- **Régimen informativo familia-por-familia (punto pre-D5 de la agenda)**:
  no se trató; **sigue vigente en la agenda**.
- **Estructura de capítulos del informe y licencia/depósito (C2.1)**: no se
  trataron; el diseño es propio (con la mesa) y los mentores lo revisan al
  leer el informe — si al revisar piden cambios, se incorporan entonces.

## 6. Related work: tarea puntual sobre evaluación por etapas (exigencia 5)

Mandato: investigar la metodología para **evaluar el pipeline por etapas**
(o reportar la métrica de error por paso) y **proponerla a los mentores**
después. Casillero existente: exigencia 5 del mapa (precedente: precisión
por heurística de extracción en YAGO), con destino B4.1; lo nuevo es
adelantar la investigación y llevarla como propuesta. Unidad derivada:
**U-EXP5** (investigación, $0).

## 7. Unidades derivadas de esta reunión (resumen)

| Unidad | Qué | Costo | Gatea |
|---|---|---|---|
| U-CAP-ESQ | Capítulo de esquema y validación pre-escalado en el informe | $0 (escritura) | el escalado (validación por lectura) |
| U-JOB-ACT | Diseño del job mensual de actualización (deltas + provenance) | $0 (diseño) | exigencia 7; habilita material para la 6 |
| U-PREP-CONTACTO | Guion de la reunión exploratoria con la industria | $0 | la colaboración del §3 |
| U-EXP5 | Investigación de evaluación por etapas, propuesta a mentores | $0 | exigencia 5 / B4.1 |

El orden operativo y las dependencias quedan en el plan
(`docs/plan_tesis.md`, bloque de la reunión del 04/09).
