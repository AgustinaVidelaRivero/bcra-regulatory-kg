# Informe — Chequeo anti-solapamiento EV1 (2026-07-26)

*(Antecedente: la primera invocación de esta unidad frenó porque el adjunto no había llegado; con `EV1_preguntas.json` ya en `data/experiment/evaluacion_escalon1/`, el chequeo corrió tal como se había planificado.)*

**Resultado: 36 preguntas EV1 comparadas contra 61 quemadas únicas (2.196 pares). El fondo de similitud es bajo (mediana 0.091, p95 0.172). Hay 2 pares con score alto que leo como solapamiento real candidato (EV1-009 y la pata de clasificación de EV1-014), 1 probable (EV1-033) y 1 limítrofe (EV1-007); el resto del top 10 es coincidencia temática. NO se descartó ni modificó nada — el veredicto es humano.**

## Método y universo

- Similitud léxica normalizada (NFD sin diacríticos, minúsculas, sin puntuación): **Jaccard de tokens** (sin stopwords castellanas, largo >2) y **Jaccard de trigramas de caracteres**; score de ranking = promedio de ambos.
- Quemadas (solo lectura de `evaluacion/queries/`, zona sellada intacta): `eval_set_v1.json` (CQ, 23) · `eval_set_v2.json` (31) · `eval_set_v2_nuevas.json` (8) · `eval_set_cqn.json` (CQN, 15) · `eval_set_cqn2.json` (CQN2, 15) → **61 únicas** tras dedup por texto (v1 ⊂ v2; nuevas ⊂ v2). Los `*_runtime` son duplicados de corrida (mismo texto) y `candidatas/dev*` no pertenecen a las familias quemadas del mandato — excluidos, anotado. `docs/casos_gate_cqn2.md` referencia los mismos 11/15 casos cuyo texto vive en `eval_set_cqn2.json`.

## Top 10 pares más similares

| # | Score (tok/tri) | EV1 | Quemada | Lectura |
|---|---|---|---|---|
| 1 | 0.622 (0.571/0.672) | EV1-014 [sujeto] | CQN:CQN-008 | **Solapamiento real (parcial-alto)** |
| 2 | 0.574 (0.467/0.681) | EV1-009 [puntual] | CQ-008 | **Solapamiento real** |
| 3 | 0.400 (0.292/0.508) | EV1-014 [sujeto] | CQ-018 | Refuerza el #1 (mismo dato ya quemado ×2) |
| 4 | 0.386 (0.333/0.439) | EV1-010 [puntual] | CQ-006 | Temática |
| 5 | 0.379 (0.348/0.410) | EV1-028 [sujeto] | CQN-013 | Temática |
| 6 | 0.378 (0.308/0.448) | EV1-022 [sujeto] | CQN-001 | Temática |
| 7 | 0.356 (0.250/0.461) | EV1-033 [puntual] | CQ-033 | **Solapamiento real probable** |
| 8 | 0.343 (0.278/0.409) | EV1-007 [condicional] | CQ-033 | Limítrofe |
| 9 | 0.320 (0.233/0.407) | EV1-028 [sujeto] | CQN-008 | Temática (boilerplate) |
| 10 | 0.315 (0.250/0.381) | EV1-033 [puntual] | CQN2:CQN2-006 | Temática |

### Textos completos de los 10 pares

**#1 — EV1-014 vs CQN-008 (0.622)**
- EV1: "¿Están las empresas no financieras emisoras de tarjetas de crédito y/o compra alcanzadas por las normas sobre clasificación de deudores y, en su caso, con qué criterios deben clasificar a sus deudores?"
- QUEMADA: "¿Las empresas no financieras emisoras de tarjetas de crédito están alcanzadas por las normas de protección de los usuarios de servicios financieros y, a la vez, con qué criterio deben clasificar a sus deudores según las normas sobre clasificación de deudores?"

**#2 — EV1-009 vs CQ-008 (0.574)**
- EV1: "Cuando un cliente solicita conocer la última clasificación que le fue asignada, ¿en qué plazo debe la entidad financiera comunicársela y qué información debe acompañar?"
- QUEMADA: "Cuando un cliente lo solicita, ¿en qué plazo debe la entidad financiera comunicarle la última clasificación que le asignó?"

**#3 — EV1-014 vs CQ-018 (0.400)**
- QUEMADA: "Los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas, ¿deben cumplir con Protección al Usuario y, además, clasificar a sus deudores? ¿Bajo qué criterio clasifican?"

**#4 — EV1-010 vs CQ-006 (0.386)**
- EV1: "En la clasificación de la cartera para consumo o vivienda, ¿hasta cuántos días contados desde su otorgamiento se consideran de cumplimiento normal los adelantos transitorios en cuenta corriente?"
- QUEMADA: "En la cartera para consumo o vivienda, ¿hasta cuántos días de atraso se considera que un deudor está en 'situación normal'?"

**#5 — EV1-028 vs CQN-013 (0.379)**
- EV1: "Una asociación mutual que otorga financiaciones y se encuentra alcanzada por las normas sobre proveedores no financieros de crédito, ¿reviste el carácter de sujeto obligado de las normas de protección de los usuarios de servicios financieros por esas financiaciones?"
- QUEMADA: "¿Qué consecuencias sancionatorias enfrenta un sujeto obligado que incumple las normas sobre protección de los usuarios de servicios financieros?"

**#6 — EV1-022 vs CQN-001 (0.378)**
- EV1: "¿Qué sujetos residentes requieren la conformidad previa del BCRA para acceder al mercado de cambios con destino a la formación de activos externos y a la operatoria con derivados?"
- QUEMADA: "¿Qué monto mensual máximo puede comprar una persona humana residente, sin conformidad previa del BCRA, para la formación de activos externos, la remisión de ayuda familiar y la operatoria con derivados?"

**#7 — EV1-033 vs CQ-033 (0.356)**
- EV1: "¿Qué límites máximos rigen para la exigencia de capital mínimo por riesgo operacional de las entidades del grupo 2, según se trate de entidades del grupo A o del grupo B, y sobre qué base se calculan?"
- QUEMADA: "¿Cuál es el límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2, y bajo qué condiciones ese límite se reduce?"

**#8 — EV1-007 vs CQ-033 (0.343)**
- EV1: "¿Alcanza con que una entidad financiera del Grupo 2 pertenezca al Grupo A para informar la reducción de exigencia por riesgo operacional en la partida 36000001?"
- (QUEMADA = CQ-033, arriba)

**#9 — EV1-028 vs CQN-008 (0.320)** — textos ya citados (#5 y #1).

**#10 — EV1-033 vs CQN2-006 (0.315)**
- QUEMADA: "En el régimen informativo sobre exigencia e integración de capitales mínimos, ¿con qué frecuencia y mediante qué expresión se determina la exigencia de capital por riesgo operacional de las entidades del Grupo 1, y qué valor toma el multiplicador de pérdida interna?"

## Mi lectura (evidencia para tu veredicto — nada descartado)

**Solapamiento real (mismo dato puntual):**
- **EV1-009 ↔ CQ-008 (#2):** es prácticamente la misma pregunta — plazo para comunicar la última clasificación al cliente — con el apéndice "qué información debe acompañar". El dato central de la respuesta es el mismo. Candidata fuerte a descarte/regeneración.
- **EV1-014 ↔ CQN-008 + CQ-018 (#1, #3):** la pata "con qué criterio(s) clasifican a sus deudores las emisoras no financieras" es el mismo dato puntual (Clasificación 10.1: mora, cartera consumo) ya quemado DOS veces (CQN-008 y CQ-018). La pata de alcance difiere (EV1 pregunta por clasificación; CQN-008 por protección), pero el interrogante de criterio es idéntico. Solapamiento parcial-alto.

**Solapamiento real probable:**
- **EV1-033 ↔ CQ-033 (#7):** ambos piden los límites de la exigencia por riesgo operacional del Grupo 2; EV1 los desagrega por grupo A/B y base de cálculo, CQ-033 pide el límite y sus condiciones de reducción — la respuesta comparte la misma tabla/dato central. A tu criterio.

**Limítrofe:**
- **EV1-007 ↔ CQ-033 (#8):** el condicional de EV1 (¿alcanza pertenecer al Grupo A para informar la reducción en 36000001?) interroga una arista de las "condiciones de reducción" de CQ-033, pero con forma y dato de respuesta distintos (condición suficiente + partida). Bisagra entre real y temático.

**Coincidencia temática (mismo territorio, distinto interrogante — NO solapamiento):** #4 (adelantos transitorios ≠ días de atraso del deudor), #5 y #9 (los tokens compartidos son boilerplate "sujeto obligado/normas de protección"; los interrogantes — carácter de mutual vs sanciones vs criterio de emisoras — difieren), #6 (qué sujetos requieren conformidad ≠ monto máximo sin conformidad), #10 (límites G2 ≠ frecuencia/ILM G1).

Fondo general: fuera del top 10 los scores caen rápido (p95 = 0.172) — el set EV1 no muestra solapamiento masivo; los casos de arriba son puntuales y concentrados en Clasificación (criterio de emisoras, plazo de comunicación) y CapMin (límites riesgo operacional G2).

## Alcance

Solo lectura (queries/ y bestiario intactos); EV1_preguntas.json sin modificar; nada descartado ni regenerado — el veredicto y la eventual regeneración (protocolo §2: "los solapados se descartan y regeneran, con registro del conteo") son tuyos. Log completo del comparador en el scratchpad de sesión.
