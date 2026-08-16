# Clasificación por lectura de los desacuerdos — pasada 2 (fuente app, prompt v1 sha fd446f8e…)

Complementa la pre-clasificación mecánica de `reporte_desacuerdos.md` con una
lectura caso por caso. Regla usada: **evidencia** = el juez señaló mal el
fragmento o ignoró contenido presente en la respuesta; **etiqueta** = el juez
localizó bien la evidencia (fragmento verbatim o ausencia real) y clasificó
distinto que la humana en zona fronteriza. Es propuesta para la adjudicación
de la autora; no decide nada.

## Resumen numérico

- 25 preguntas: acuerdo 14 · desacuerdo 6 · requiere_adjudicacion 5. Acuerdo sobre decididas 14/20.
- Matriz humano→juez: correcto→correcto 1, correcto→parcial 5, correcto→req.adj. 1; parcial→parcial 10, parcial→incorrecto 1, parcial→req.adj. 4; incorrecto→incorrecto 3.
- Por criterio (proxy): humana `incorrecta` → 13/13 criterios `no_cumplido` (100%); humana `correcta` → 11/21 `cumplido` (los 10 restantes son los criterios "no preguntados" de abajo).
- No-determinismo: 87/92 pares unánimes; 5 no unánimes, todos con `dudoso` en juego (U6-011 c2, U6-004 c2, U6-010 c3, U6-019 c2, U6-001 c3); 0 `sin_consenso`.
- Fragmentos (276): 167 verbatim + 94 null; 15 marcados mecánicamente como no-verbatim/fuga — leídos uno a uno: 14 son concatenaciones de viñetas o diferencias de puntuación con contenido presente en la respuesta (U6-011 c1 ×3, U6-012 c2/c3 r3 con elipsis, U6-013 c3 ×3 un punto, U6-015 c4 ×3, U6-019 c1 ×3 una coma); **1 fuga real de gold: U6-001 c3 rep 2** (fragmento = cita del gold; veredicto `dudoso`; reps 1 y 3 `null`/`no_cumplido` → modal `no_cumplido`).

## A. Los 6 desacuerdos

| qid | humano | juez | par decisivo | clase | lectura |
|---|---|---|---|---|---|
| U6-021 | correcto | parcial | c3 no_cumplido (null ×3) | **etiqueta** — criterio no preguntado | La respuesta contiene fecha y SISCEN/T0003/SWIFT (c1, c2 cumplidos verbatim). c3 (monedas residuales 9999) es exactamente el "matiz" que la humana registró y perdonó (Laudo №1: no penalizar omisión de lo no preguntado). El juez no puede aplicar ese laudo porque el criterio existe. |
| U6-002 | correcto | parcial | c3 no_cumplido (null ×3) | **etiqueta** — criterio no preguntado | Los dos requisitos preguntados (balances auditados; monto asamblea) cumplidos verbatim. c3 (DDJJ firmada por representante legal) no fue preguntado ni respondido; ausencia real. |
| U6-017 | correcto | parcial | c3 no_cumplido (null ×3) | **etiqueta** — criterio no preguntado | 2,5% RPC y mayorías cumplidos (c2 cumplido aun sin "de la totalidad de los miembros": el juez perdonó el mismo matiz que la humana). c3 (conformidad con opinión fundada) no preguntado; ausencia real. |
| U6-013 | correcto | parcial | c2 no_cumplido (fragmento verbatim ×3) | **etiqueta** — calificador omitido | Plazo (c1) y ponderador 20% (c3) cumplidos. c2: la respuesta da "valuación a precios de mercado mensual" pero omite "activo limitado a los listados en 5.3.1.2."; el juez trata la lista como parte esencial del criterio; la humana lo dio por correcto. Evidencia bien localizada. |
| U6-023 | correcto | parcial | c2, c3 no_cumplido (null ×3 cada uno) | **etiqueta** — c2 matiz que la humana registró (Laudo №3: "omisión de la cláusula de cierre discrecional no altera el contenido"); c3 encuadre discriminatorio no preguntado | Núcleo (c1) cumplido verbatim. El juez penaliza exactamente lo que el Laudo №3 decidió no penalizar. |
| U6-009 | parcial | incorrecto | c1 no_cumplido (fragmento verbatim ×3: solo constancia aduanera); c2–c5 null | **etiqueta** — granularidad del criterio | La respuesta da 3/10 requisitos; la humana lo vio como parcial (algo respondió). c1 agrupa 3 documentos (constancia + factura + transporte): la respuesta tiene 1 de 3 y el juez lo marca no_cumplido entero; c2–c5 realmente ausentes. El mapping §2 da incorrecto porque ningún criterio queda cumplido. Frontera: si c1 estuviera partido en 3, el veredicto sería parcial. |

Ninguno de los 6 es de evidencia: en todos el fragmento es verbatim de la respuesta o la ausencia es real. **Patrón dominante (5/6): el juez penaliza criterios que la humana no penalizó por ser contenido no preguntado o matiz de cierre** (U6-021 c3, U6-002 c3, U6-017 c3, U6-023 c2/c3, y en menor medida U6-013 c2). Es una diferencia entre el estándar humano (Laudo №1/№3) y el conjunto de criterios, no un error de lectura del juez.

## B. Las 5 `requiere_adjudicacion` (el instrumento no decidió)

| qid | humano | criterios que disparan | lectura |
|---|---|---|---|
| U6-011 | parcial | c2 dudoso (dudoso/nc/dudoso) | c1 no_cumplido correcto (plazos 10/5 días hábiles de otro régimen vs 2º mes/30 días corridos — coincide con la humana). c2: la respuesta da el límite de depósitos pero omite "mientras persista" y "saldos al último día de cada mes"; el juez duda. Etiqueta fronteriza. |
| U6-005 | parcial | c1, c2 dudoso (×3 cada uno) | La respuesta enumera los mecanismos sin calificadores ("a nombre del cliente", GAFI) y presenta BOPREAL como regla general — el juez duda en c1/c2 (¿mecanismo nombrado sin calificador cumple?) y marca c3/c4 no_cumplido (coincide con la humana: "no se permite billetes" declarado inexistente). Etiqueta fronteriza; el `dudoso` es la salida honesta. |
| U6-004 | correcto | c2 dudoso (dudoso/dudoso/nc); c1, c3, c4 no_cumplido | Única `correcta` humana que el juez lleva a adjudicación. c1: la respuesta dice el umbral y "si declara que no posee… no se requiere conformidad" — equivalencia normativa que el juez no reconoce (exige la estructura regla/excepción explícita). c3/c4: vía alternativa y compromiso 3.16.2.2 no preguntados/ausentes. Etiqueta (severidad), no evidencia. |
| U6-010 | parcial | c3 dudoso (dudoso/nc/dudoso) | c1/c2 cumplidos verbatim. c3: "casos distintos a VPU-RIGI" es escueto y refiere a la conformidad, no al vencimiento; el juez duda. Nota: la interpolación contradictoria que la humana señaló ("intereses devengados antes del vencimiento") no está cubierta por ningún criterio → invisible al instrumento. |
| U6-019 | parcial | c2 dudoso (c/dudoso/dudoso) | c1 cumplido; c3, c4 no_cumplido (aspectos ausentes); c5 no_cumplido (la respuesta declara no saber "a disposición de quién" — coincide con la humana). c2: "los niveles que intervienen" sin atribuciones ni requisitos; el juez duda. Etiqueta fronteriza. |

## C. Observaciones sobre el instrumento (para laudo, sin decidir nada)

1. **Fuga de gold al fragmento**: 1/276 en esta pasada (U6-001 c3 r2), 3/276 en la pasada 1 (mismo par, otra respuesta). El par U6-001 c3 es sistemáticamente el que provoca la fuga (criterio largo, respuesta que roza el tema sin decirlo). Candidato a calibrador ya registrado por la autora.
2. **Criterios no preguntados**: c3 de U6-021, U6-002, U6-017; c2/c3 de U6-023; c3/c4 de U6-004; c3 de U6-019 — el juez los evalúa (correctamente, dada su instrucción) y arrastra `correcto`→`parcial`. La brecha es entre criterios y Laudo №1, no del juez. Decisión de la autora: (a) aceptar que el juez mide contra el gold completo, (b) marcar en el gold qué criterios son "núcleo preguntado", o (c) calibrador. No es un ajuste que yo pueda hacer.
3. **Clasificación auxiliar**: `abstencion` solo en U6-012 (3/3). U6-001, U6-005, U6-019 (flag app `respondible=False`) fueron `contenido` 3/3 — respuestas mixtas (contenido + una parte "no encontrado"). Consistente con la definición del prompt (abstención = declara no encontrar la información sustantiva); el flag del agente es más laxo.
4. **`dudoso` funciona como salida honesta**: los 6 modales `dudoso` caen en calificadores omitidos / formulaciones escuetas — exactamente el tipo de frontera para el que el pre-registro reserva la adjudicación humana.
