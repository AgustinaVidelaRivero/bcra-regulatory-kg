# Registro: criterios de calibración U6 (insumo del juez de fidelidad EV2)

Operacionaliza el §5 del pre-registro sellado
(docs/preregistro_evaluacion_fidelidad_ev2.md, commit be8a84f): la fuente de
calibración del juez son las 25 preguntas de U6 ya adjudicadas humanamente.
U6 carecía de gold estructurado (Laudo №0 de U6: adjudicación informada
contra el ancla, sin criterios); este registro documenta cómo se produjo.

## Método de redacción (Laudo A — delegación a instancia ciega)

Los 93 criterios originales fueron redactados por una instancia ejecutora
ciega cuyo único insumo fue preguntas_u6.json (id, to, ancla, pregunta) y los
5 PDFs de los TO. La instancia jamás vio las respuestas del agente, la
adjudicación humana ni las notas de adjudicación. Decisión metodológica de la
autora: la instancia ciega está menos contaminada que la autora, que conoce
respuestas y veredictos. Redacción guiada por "qué debe contener una
respuesta correcta según el texto normativo del ancla", con la regla de
alcance del Laudo №1 de U6 (no se evalúa lo que la pregunta no pide).

## Revisión independiente

Una segunda instancia (contaminación declarada: conoce el proyecto) revisó
los 93 criterios limitándose a dos chequeos texto-contra-texto: fidelidad
criterio→cita y alcance (Laudo №1). Resultado: 93/93 citas existentes en el
texto normativo (verificación adicional del cuadro 11.2.1 contra la imagen
de página), cero fabricaciones, tres bordes de alcance elevados a la autora.

## Laudos de la autora sobre los bordes

- **Laudo B**: U6-006 criterio #3 (fecha de vigencia 20/01/25) ELIMINADO —
  la pregunta no pide vigencia; mantenerlo violaría el Laudo №1.
- **Laudo C**: U6-013 criterio #3 RECORTADO (se quita la cláusula sobre la
  parte no cubierta, no preguntada); la cita_textual queda intacta porque la
  oración fuente es indivisible.
- **Laudo D**: citas tabulares ACEPTADAS con nota: en U6-022 (#2, #3) y
  U6-012, los fragmentos son verbatim pero su contigüidad refleja la
  linealización del extractor de PDF, no prosa contigua del documento.
  En U6-022, dos citas provienen del texto introductorio 11.1/11.1.1 que
  define explícitamente las instrucciones de los cuadros 11.2.1 a) y b).

## Estado final

25 preguntas, 92 criterios (2–5 por pregunta), cada uno con cita textual.
Verificación mecánica pre-laudos: 93/93 (check_citas_u6.py, pdftotext,
normalización mínima declarada en el propio script). Post-laudos: 92/92
esperado (las ediciones no tocaron ninguna cita); re-verificación
independiente a cargo del ejecutor del juez (pdfplumber) antes de la
primera pasada de calibración.
sha256 criterios_u6.json: b8d6578902dc1f18b0a8239c2c05a5f556cbe7162c4bcf042cc12c94bb2c2a5d

## Limitación declarada

La calibración del juez usa criterios producidos post-hoc sobre preguntas
cuyas respuestas y veredictos ya existían. La mitigación es estructural
(redactor ciego + revisión limitada a texto-contra-texto + bordes laudados
por la autora) y se declara como limitación del set de calibración. El set
de medición real (EV2) no comparte esta limitación: sus 164 criterios fueron
generados a ciegas y sellados (9c44516) antes de toda corrida.