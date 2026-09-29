# Atribución A0.2 de las celdas C2 a C5 (U-TANDA0-2A E6 b)

Regla sellada `data/experiment/ev2_reporte/regla_atribucion.md` (sha256 `20040e94c383286c…`), funciones importadas de `data/experiment/ev2_reporte/code/atribucion_fallas.py`. Veredictos por traza desde `data/experiment/ev2_tanda0/adjudicacion_SOLO_MESA/definitivos_por_par_tanda0_SOLO_MESA.json`. Generado por `data/experiment/ev2_tanda0/code/atribucion_tanda0.py`.

## Trazas base, contra su propio veredicto

| celda | índice | ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto | replay | replay fuerte |
|---|---|---|---|---|---|---|---|---|
| C1 (774acac) | GraphIndex | 8 | 7 | 1 | 19 | 5 | 40/40 | 40/40 |
| C2 | Neo4jIndex fulltext (KG_Reextraido_r1, índice nodos_fulltext_kg_reextraido_r1) | 6 | 0 | 2 | 23 | 9 | 40/40 | 40/40 |
| C3 | GraphIndex en memoria (tanda0_ens_desarrollo) | 8 | 2 | 4 | 17 | 9 | 40/40 | 40/40 |
| C4 | Neo4jIndex fulltext (KG_Tanda0_Desarrollo_r1, índice nodos_fulltext_kg_tanda0_desarrollo_r1) | 9 | 0 | 2 | 18 | 11 | 40/40 | 40/40 |
| C5 | GraphIndex en memoria (tanda0_ens_diez) | 0 | 4 | 0 | 8 | 8 | 20/20 | 20/20 |

## Re-corridas del §7 (secundaria)

- C2: 72 trazas (0 excluidas); clase {'alcanzabilidad': 0, 'ausencia_kg': 9, 'correcto': 3, 'generacion': 53, 'vista_no_consultada': 7}; replay 72/72, fuerte 72/72
- C3: 56 trazas (4 excluidas); clase {'alcanzabilidad': 4, 'ausencia_kg': 9, 'correcto': 5, 'generacion': 29, 'vista_no_consultada': 9}; replay 56/56, fuerte 56/56
- C4: 61 trazas (2 excluidas); clase {'alcanzabilidad': 0, 'ausencia_kg': 15, 'correcto': 3, 'generacion': 36, 'vista_no_consultada': 7}; replay 61/61, fuerte 61/61
- C5: 23 trazas (1 excluidas); clase {'alcanzabilidad': 3, 'ausencia_kg': 0, 'correcto': 3, 'generacion': 17, 'vista_no_consultada': 0}; replay 23/23, fuerte 23/23

## Pares definitivos parciales o incorrectos (plan, punto 3)

| celda | no estaba en el grafo | estaba y no se navegó | se consultó y falló |
|---|---|---|---|
| C1 (774acac) | 8 | 8 | 18 |
| C2 | 6 | 2 | 23 |
| C3 | 8 | 7 | 15 |
| C4 | 9 | 3 | 17 |
| C5 | 0 | 4 | 8 |

Incorrectos definitivos, uno por uno:
- C2 EV2F-007 [juez_base, base]: generacion (contenido)
- C2 EV2F-011 [juez_enc, enc_r1]: generacion (abstencion)
- C2 EV2F-017 [juez_base, base]: ausencia_kg (abstencion)
- C2 EV2F-023 [adjudicacion_base, base]: generacion (abstencion)
- C2 EV2F-024 [adjudicacion_s7, enc_r1]: ausencia_kg (contenido)
- C2 EV2F-025 [juez_base, base]: ausencia_kg (abstencion)
- C2 EV2F-031 [juez_base, base]: ausencia_kg (abstencion)
- C3 EV2F-006 [juez_enc, enc_r2]: alcanzabilidad (contenido)
- C3 EV2F-007 [juez_base, base]: alcanzabilidad (abstencion)
- C3 EV2F-011 [juez_base, base]: generacion (contenido)
- C3 EV2F-012 [adjudicacion_base, base]: alcanzabilidad (contenido)
- C3 EV2F-017 [juez_base, base]: ausencia_kg (abstencion)
- C3 EV2F-025 [juez_base, base]: ausencia_kg (contenido)
- C3 EV2F-031 [juez_base, base]: ausencia_kg (abstencion)
- C4 EV2F-007 [juez_base, base]: generacion (contenido)
- C4 EV2F-011 [juez_base, base]: generacion (abstencion)
- C4 EV2F-012 [adjudicacion_base, base]: generacion (contenido)
- C4 EV2F-013 [juez_base, base]: ausencia_kg (contenido)
- C4 EV2F-017 [juez_base, base]: ausencia_kg (abstencion)
- C4 EV2F-018 [adjudicacion_s7, enc_r2]: vista_no_consultada (contenido)
- C4 EV2F-025 [juez_base, base]: ausencia_kg (abstencion)
- C4 EV2F-031 [juez_base, base]: ausencia_kg (contenido)
- C5 T0F-003 [adjudicacion_base, base]: alcanzabilidad (contenido)
- C5 T0F-006 [juez_enc, enc_r1]: generacion (contenido)
- C5 T0F-017 [adjudicacion_base, base]: alcanzabilidad (abstencion)
- C5 T0F-018 [juez_base, base]: alcanzabilidad (contenido)

## Patrones de navegación de A1.8 (plan, punto 4)

| celda | trazas | (a) trazas con ancla vista por referencia sin abrir | (a) nodos | (b) llamadas salientes sobre Operacion con Restriccion entrante | (b) trazas |
|---|---|---|---|---|---|
| C2 | 112 | 4 | 20 | 22 | 19 |
| C3 | 96 | 0 | 0 | 12 | 11 |
| C4 | 101 | 2 | 5 | 16 | 12 |
| C5 | 43 | 0 | 0 | 4 | 4 |

## Punto 5 del plan

- no aplica a EV2 ni a C5: ninguna pregunta ancla en esos puntos (cla:5.1.1.1, cla:3.7)
