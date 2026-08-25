# Nota de episodios de la adjudicación de U-B1.8 (mesa revisora)

Registro de los episodios que rodean la adjudicación humana del worksheet de
r1, para que la lectura de la muestra simétrica sea honesta. Ningún episodio
altera los veredictos definitivos: en la población A (8 pares
`requiere_adjudicacion`) la marca humana es definitiva por diseño, y en la
muestra B las marcas no reemplazan veredictos (miden la tasa de error del
juez).

## Episodio 1 — exposición parcial de identidad de la muestra B (mesa)

Durante la verificación cruzada del freno 4 (previa a la adjudicación), las
salidas intermedias de la revisión de mesa imprimieron los ids de pregunta de
la muestra B y las vías de agregación por par del §7. Ese material era
visible en la conversación de revisión antes de volcar las marcas.

- Riesgo: sesgo pro-acuerdo en las 4 fichas de muestra — si quien adjudica
  recuerda qué preguntas cayeron en la muestra y qué dijo el juez, el acuerdo
  juez/humana deja de ser una medición completamente ciega. No afecta a las
  9 fichas de población A: allí la marca humana es la definitiva sea cual
  sea.
- Mitigación aplicada: adjudicación ficha por ficha contra el PDF del TO y la
  cita del gold, en el orden aleatorizado del worksheet, sin re-consultar las
  salidas de la revisión.
- Lectura con salvedad: el acuerdo observado (exacto 4/4; por criterio 15/15;
  sobre-acreditación 0, sub-acreditación 0) se reporta con esta salvedad
  declarada. El episodio fue declarado en el freno 4, antes de la
  adjudicación, y queda como limitación menor de la medición de tasa de error
  del juez en esta unidad — no de los veredictos definitivos.

## Episodio 2 — alcance de marcadores del censo ciego (ejecutor, ya declarado)

El censo ciego del worksheet publica por diseño el resumen de población
(fichas por origen), igual que el censo del molde `03ebe83`; el selftest
no-fuga le aplica el subconjunto de marcadores de identidad (ids opacos,
sufijos, shas, ids de pregunta), y la lista completa aplica al worksheet.
Declarado por el ejecutor en la entrega del freno 4 y verificado por la mesa.

## Episodio 3 — Documento de veredictos propuestos, descartado

Durante la sesión de adjudicación, la autora recibió un documento con
veredictos propuestos para las 13 fichas, generado por una instancia
LLM (origen no registrado por la autora; no puede descartarse contacto
previo con material des-cegador). El documento fue descartado sin
volcarse: la adjudicación se rehízo íntegramente en sesión guiada,
ficha por ficha, con las citas del gold y las respuestas a la vista.
Las marcas definitivas de la autora divergen del documento descartado
en veredictos individuales (p. ej. F12-C3, F13-C1) y en el agregado
(21 cumplidos contra ~27 propuestos; el documento además contenía
errores de conteo), lo que evidencia adjudicación independiente. El
episodio se declara como limitación de proceso; los veredictos
definitivos provienen exclusivamente de las marcas de la autora
(diff de transcripción auditado, sha 91c839c5…).

## Verificación

Los episodios 1 y 2 constan en la conversación de revisión de la unidad; el
episodio 3 fue declarado por la autora en el cierre (los 21 cumplidos de sus
marcas se verifican contra el worksheet: 21/49, resto no_cumplido); la
verificación independiente del cierre (mapping §2 recomputado sobre las 49
marcas, re-agregación de los 8 votos ADJ, acuerdo de muestra recomputado
desde archivos) reprodujo exactamente la tabla definitiva 6/26/8 y el
acuerdo 4/4 · 15/15.
