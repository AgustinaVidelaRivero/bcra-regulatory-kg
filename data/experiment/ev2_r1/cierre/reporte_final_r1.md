# Cierre de U-B1.8 — fidelidad EV2 de KG-Reextraído-r1

Generado 2026-08-24T17:15:31. Worksheet adjudicado sha `91c839c5e0b5681f…`; mapping §2 en código sobre las marcas humanas; regla de atribución A0.2 (`40603a9`) con funciones importadas; doble corrida byte-idéntica.

## 1. Tabla final (r1 AL LADO de las selladas; las selladas se citan de `reporte_ev2.md` §2, no se re-miden)

| Grafo | correcto | parcial | incorrecto | cobertura de criterios (164) | abstenciones (base) |
|---|---|---|---|---|---|
| KG-Base (12c226e2) | 3 | 20 | 17 | 56 | 9/40 |
| KG-Refinado (26fac8b4) | 5 | 26 | 9 | 73 | 4/40 |
| KG-Reextraído (8e2eadee) | 4 | 27 | 9 | 70 | 7/40 |
| **KG-Reextraído-r1 (0226e947)** | 6 | 26 | 8 | 69 | 6/40 |

- vías de los 40 definitivos: {'juez_base': 11, 'juez_enc': 21, 'adjudicacion_base': 5, 'adjudicacion_s7': 3}

## 2. Muestra simétrica — tasa de error del juez (no reemplaza veredictos)

- acuerdo exacto: 4/4; acuerdo por criterio: 15/15
- sobre-acreditación del juez (criterio: juez cumplido / humana no): 0; sub-acreditación (juez no / humana sí): 0
- flip descendente de correctos auditados: 0/1

  - ADJ1-8b2faed3 [muestra_parcial_incorrecto]: juez parcial / humana parcial — criterios 5/5
  - ADJ1-883e85a3 [muestra_parcial_incorrecto]: juez parcial / humana parcial — criterios 4/4
  - ADJ1-cd109f5d [muestra_parcial_incorrecto]: juez incorrecto / humana incorrecto — criterios 4/4
  - ADJ1-9e3a589f [muestra_correcto]: juez correcto / humana correcto — criterios 2/2

## 3. Atribución causal A0.2 (r1)

### 3.a Trazas base (40, contra su propio veredicto)

| ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto | replay | replay fuerte |
|---|---|---|---|---|---|---|
| 8 | 7 | 1 | 19 | 5 | 40/40 | 40/40 |

- clase × veredicto: {'correcto': {'correcto': 5}, 'incorrecto': {'generacion': 2, 'alcanzabilidad': 2, 'ausencia_kg': 3}, 'parcial': {'ausencia_kg': 5, 'vista_no_consultada': 1, 'generacion': 17, 'alcanzabilidad': 5}}
- clase × auxiliar: {'abstencion': {'generacion': 2, 'ausencia_kg': 3, 'alcanzabilidad': 1}, 'contenido': {'ausencia_kg': 5, 'correcto': 5, 'vista_no_consultada': 1, 'generacion': 17, 'alcanzabilidad': 6}}
- anclas no resueltas: 9 {'granularidad': 7, 'contenedor': 2}
- sensibilidad por descendientes (informativa, H24): {'generacion': 4, 'vista_no_consultada': 2, 'alcanzabilidad': 1, 'ausencia_kg': 1}

### 3.b Re-corridas §7 (secundaria, contra su propio veredicto)

- 71 trazas (1 excluida/s sin veredicto propio); clase: {'ausencia_kg': 11, 'alcanzabilidad': 11, 'vista_no_consultada': 0, 'generacion': 42, 'correcto': 7}; replay 71/71, fuerte 71/71

### 3.c Pares definitivos (traza representativa)

- clase × definitivo: {'correcto': {'correcto': 6}, 'incorrecto': {'generacion': 3, 'alcanzabilidad': 2, 'ausencia_kg': 3}, 'parcial': {'ausencia_kg': 5, 'vista_no_consultada': 1, 'generacion': 15, 'alcanzabilidad': 5}}
- incorrectos definitivos, uno por uno:
  - EV2F-001 [juez_base, base]: generacion (abstencion)
  - EV2F-007 [juez_enc, enc_r1]: generacion (contenido)
  - EV2F-016 [juez_base, base]: alcanzabilidad (contenido)
  - EV2F-017 [juez_base, base]: ausencia_kg (abstencion)
  - EV2F-023 [juez_base, base]: alcanzabilidad (abstencion)
  - EV2F-025 [juez_base, base]: ausencia_kg (abstencion)
  - EV2F-031 [juez_base, base]: ausencia_kg (abstencion)
  - EV2F-034 [juez_base, base]: generacion (abstencion)

## 4. Lectura P1–P5 (formato fijo del pre-registro §7)

| predicción | número predicho (umbral/banda) | número observado | veredicto |
|---|---|---|---|
| P1 | censo: presentes(r1) >= 31/40 (no-resueltas <= 9) | presentes 31/40 (no-resueltas 9) | **cumplida** |
| P2a | trazas base ausencia_kg < 9, con diagnóstico granularidad < 8 | ausencia_kg 8 (granularidad 6) | **cumplida** |
| P2b | incorrectos definitivos con clase ausencia_kg < 4 | incorrectos definitivos ausencia_kg 3 de 8 | **cumplida** |
| P3 | generacion en trazas base dentro de 21 ± 3 ([18, 24]) | generacion 19 | **cumplida** |
| P4 | techo de retrieval (alcanzabilidad + vista_no_consultada, trazas base) dentro de 6 ± 3 ([3, 9]); < 3 = hallazgo contra H17 | alcanzabilidad 7 + vista_no_consultada 1 = 8 | **cumplida** |
| P5 | incorrectos definitivos <= 9; dirección de correctos/parciales reportada con tamaño (diferencias de 1–3 preguntas no son señal) | incorrectos 8; correctos 6 (selladas 3/5/4); parciales 26 (selladas 20/26/27) | **cumplida** |

## 5. Costos de la unidad (desde dbs; comando: gasto_dbs_r1.py)

| etapa | USD |
|---|---|
| agente base N=1 | 1.409 |
| juez base N=3 | 1.4415 |
| agente §7 N=3 | 2.4632 |
| juez §7 N=3 | 1.9746 |
| adjudicación + cierre | 0.0 |
| **TOTAL** | **7.2883** |

Precios: verificados 2026-08-23 contra platform.claude.com/docs/en/about-claude/pricing: haiku-4.5 1/5 (cache 1,25x/0,10x); sonnet-4.6 3/15.
