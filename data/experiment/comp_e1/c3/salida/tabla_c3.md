# Cifras finales de U-COMP-E1 (C3) — criterio sellado aplicado con la lectura adjudicada

Control previo: 804 líneas, 19 adjudicadas (14 cambian, 5 ratifican), 785 iguales byte a byte. Tabla de códigos abierta a las 2026-10-08T10:48:25+00:00: A = S1, H = S2, K = O2, N = H0, W = O1.

## Criterio (peor de las dos corridas de cada brazo)

| brazo | modelo | C1: Condicion con relación (corrida 1, corrida 2) | peor | ≥ 113 | Wilson inf. 95 % (peor) | C2: omisiones normativas extraídas con tramo verificado (c1, c2) | peor | ≥ 41 | Wilson inf. 95 % (peor) | cumple |
|---|---|---|---|---|---|---|---|---|---|---|
| S | claude-sonnet-5-5 | 60, 67 de 137 | 60 | no | 0.3577 | 20, 22 de 46 | 20 | no | 0.3021 | NO |
| O | claude-opus-5-5 | 91, 95 de 137 | 91 | no | 0.5816 | 19, 18 de 46 | 18 | no | 0.2639 | NO |
| Haiku (referencia T4) | claude-haiku-4-5 | 43 de 137 | — | no | 0.2421 | 0 de 46 (por definición) | — | no | 0.0000 | NO |

**Resultado: ningún brazo cumple el criterio.**

## M1 por corrida (137 supuestos del grupo c, lectura adjudicada)

| corrida (código) | modelo | con relación | dentro de norma | fusionado | omitido | sin relación | subtipos (presente / heredado / no emitida) |
|---|---|---|---|---|---|---|---|
| Haiku, T4 | claude-haiku-4-5 | 43 | 76 | 7 | 3 | 8 | {'norma_en_heredado': 4, 'norma_presente': 3, 'norma_no_emitida': 1} |
| S1 (A) | claude-sonnet-5-5 | 60 | 65 | 5 | 2 | 5 | 3 / 2 / 0 |
| S2 (H) | claude-sonnet-5-5 | 67 | 61 | 7 | 0 | 2 | 1 / 1 / 0 |
| O1 (W) | claude-opus-5-5 | 91 | 38 | 1 | 0 | 7 | 1 / 6 / 0 |
| O2 (K) | claude-opus-5-5 | 95 | 35 | 1 | 0 | 6 | 2 / 4 / 0 |

## M2 por corrida (las 46 omisiones normativas de T4; las 14 no normativas aparte)

| corrida (código) | normativas: verificado / no verificable / omisión otra vez / ausente | no normativas (14) | remisiones puras (5, dentro de las 46) | categorías de «omisión otra vez» |
|---|---|---|---|---|
| Haiku, T4 | 0 / 0 / 46 / 0 (por definición) | — | — | meta_normativo 46 |
| S1 (A) | 20 / 0 / 3 / 23 | 5 / 0 / 0 / 9 | 2 / 0 / 0 / 3 | {'fuera_de_tipos': 3} |
| S2 (H) | 22 / 4 / 2 / 18 | 2 / 1 / 0 / 11 | 3 / 0 / 0 / 2 | {'relacion_sin_predicado': 1, 'fuera_de_tipos': 1} |
| O1 (W) | 19 / 0 / 2 / 25 | 4 / 0 / 1 / 9 | 3 / 0 / 0 / 2 | {'fuera_de_tipos': 2, 'meta_normativo': 1} |
| O2 (K) | 18 / 1 / 3 / 24 | 4 / 0 / 1 / 9 | 3 / 0 / 0 / 2 | {'fuera_de_tipos': 3, 'meta_normativo': 1} |

## Cifra complementaria del texto propio (declarada posterior al resultado; NO entra al criterio)

De las 46 omisiones normativas, 26 tienen su oración en el texto propio y 20 en el heredado (campo `en` de T4).

| corrida (código) | texto propio (26): verificado / no verificable / omisión otra vez / ausente | texto heredado (20): verificado / no verificable / omisión otra vez / ausente |
|---|---|---|
| S1 (A) | 16 / 0 / 2 / 8 | 4 / 0 / 1 / 15 |
| S2 (H) | 17 / 2 / 2 / 5 | 5 / 2 / 0 / 13 |
| O1 (W) | 15 / 0 / 2 / 9 | 4 / 0 / 0 / 16 |
| O2 (K) | 16 / 0 / 3 / 7 | 2 / 1 / 0 / 17 |

## Quinto código (N = intento 0 de Haiku en las 8 unidades con reintento; descriptivo)

M1 (11 supuestos): condicion_con_relacion 5, dentro_de_norma 5, fusionado 1, omitido 0, sin_relacion 0; subtipos {'norma_en_heredado': 0, 'norma_presente': 0, 'norma_no_emitida': 0}.
M2 (5 omisiones; 4 normativas): normativas 3 / 0 / 1 / 0; no normativas 0 / 0 / 1 / 0.

## M3 — variación entre corridas (descriptivo, c1/salida/m3_c1.json)

| brazo | modelo | en las dos | misma clave | iguales byte a byte | ambas sin error | cortes c1/c2 | sin herramienta c1/c2 | mal formadas c1/c2 | refusals c1/c2 |
|---|---|---|---|---|---|---|---|---|---|
| S | claude-sonnet-5-5 | 87 | 87 | 1 (cla::3.5::intro) | 87 | 0/0 | 0/0 | 0/0 | 0/0 |
| O | claude-opus-5-5 | 87 | 87 | 4 (cap::7.1.3::intro, cla::3.5::intro, ctacte::2.3.5::intro, ext::2.1) | 87 | 0/0 | 0/0 | 0/0 | 0/0 |

## M4 y costo real (descriptivo, c1/salida/m4_c1.json, presupuesto.json)

| corrida | modelo | entidades / relaciones / omisiones | tramo de entidad no verificable | tramo de omisión no verificable | rechazos r2 | entrada | cache read | cache write | salida | USD | USD/unidad |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | claude-sonnet-5-5 | 582 / 844 / 34 | 20/501 | 1/34 | 4 | 137116 | 3075876 | 35766 | 193686 | 2.915682 | 0.033513 |
| S2 | claude-sonnet-5-5 | 601 / 935 / 33 | 22/519 | 1/33 | 0 | 137116 | 3111642 | 0 | 200838 | 2.904940 | 0.03339 |
| O1 | claude-opus-5-5 | 689 / 1055 / 38 | 8/612 | 0/38 | 0 | 137116 | 3075962 | 35767 | 188410 | 5.110691 | 0.058743 |
| O2 | claude-opus-5-5 | 691 / 1029 / 40 | 18/615 | 0/40 | 0 | 137116 | 3111729 | 0 | 186725 | 4.905310 | 0.056382 |

**Gasto real: USD 15.836623 de 35** (S 5.820622, O 10.016001); salida del intento 0 de Haiku sobre las mismas 87 unidades: 178739 tokens. C2 y C3 sin API.

