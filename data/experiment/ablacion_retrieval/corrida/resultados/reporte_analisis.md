# Análisis de la ablación de retrieval — U-A1.4 (generado por analisis_ablacion.py)

Pares apareados (presentes en las 4 celdas): **50**; trazas por celda: {'C00_booleano_v1': 100, 'C10_bm25_v1': 100, 'C01_booleano_v2': 100, 'C11_bm25_v2': 100}; faltantes por celda: {'C00_booleano_v1': [], 'C10_bm25_v1': [], 'C01_booleano_v2': [], 'C11_bm25_v2': []}.

Replay: C00_booleano_v1: estándar=True fuerte=True cruce_inmemory=True; C10_bm25_v1: estándar=True fuerte=True; C01_booleano_v2: estándar=True fuerte=True; C11_bm25_v2: estándar=True fuerte=True

## Tabla central (grupo `todos`, pares apareados)

| celda | variante | n_casos | n_anclas | vistas | consultadas | brecha v-s-c | recall vista micro | recall vista macro | recall consultada micro | recall consultada macro |
|---|---|---|---|---|---|---|---|---|---|---|
| C00_booleano_v1 | literal | 50 | 53 | 52 | 47 | 6 | 0.9811 | 0.9900 | 0.8868 | 0.8800 |
| C00_booleano_v1 | antilexica | 50 | 53 | 46 | 33 | 13 | 0.8679 | 0.8800 | 0.6226 | 0.6300 |
| C10_bm25_v1 | literal | 50 | 53 | 52 | 52 | 1 | 0.9811 | 0.9900 | 0.9811 | 0.9800 |
| C10_bm25_v1 | antilexica | 50 | 53 | 48 | 36 | 12 | 0.9057 | 0.9100 | 0.6792 | 0.6800 |
| C01_booleano_v2 | literal | 50 | 53 | 52 | 47 | 6 | 0.9811 | 0.9900 | 0.8868 | 0.8900 |
| C01_booleano_v2 | antilexica | 50 | 53 | 46 | 32 | 15 | 0.8679 | 0.8700 | 0.6038 | 0.5900 |
| C11_bm25_v2 | literal | 50 | 53 | 53 | 52 | 1 | 1.0000 | 1.0000 | 0.9811 | 0.9800 |
| C11_bm25_v2 | antilexica | 50 | 53 | 47 | 37 | 11 | 0.8868 | 0.8900 | 0.6981 | 0.6900 |

Brecha Δ = literal − anti-léxica por celda (grupo `todos`):

| celda | Δ vista micro | Δ vista macro | Δ consultada micro | Δ consultada macro |
|---|---|---|---|---|
| C00_booleano_v1 | 0.1132 | 0.1100 | 0.2642 | 0.2500 |
| C10_bm25_v1 | 0.0754 | 0.0800 | 0.3019 | 0.3000 |
| C01_booleano_v2 | 0.1132 | 0.1200 | 0.2830 | 0.3000 |
| C11_bm25_v2 | 0.1132 | 0.1100 | 0.2830 | 0.2900 |

## Cohorte núcleo limpio (E-E) — separada, no promediada con la otra

| celda | variante | n_casos | n_anclas | vistas | consultadas | brecha v-s-c | recall vista micro | recall consultada micro | recall consultada macro |
|---|---|---|---|---|---|---|---|---|---|
| C00_booleano_v1 | literal | 11 | 11 | 11 | 9 | 2 | 1.0000 | 0.8182 | 0.8182 |
| C00_booleano_v1 | antilexica | 11 | 11 | 10 | 6 | 4 | 0.9091 | 0.5455 | 0.5455 |
| C10_bm25_v1 | literal | 11 | 11 | 11 | 11 | 0 | 1.0000 | 1.0000 | 1.0000 |
| C10_bm25_v1 | antilexica | 11 | 11 | 9 | 6 | 3 | 0.8182 | 0.5455 | 0.5455 |
| C01_booleano_v2 | literal | 11 | 11 | 11 | 10 | 1 | 1.0000 | 0.9091 | 0.9091 |
| C01_booleano_v2 | antilexica | 11 | 11 | 10 | 6 | 4 | 0.9091 | 0.5455 | 0.5455 |
| C11_bm25_v2 | literal | 11 | 11 | 11 | 11 | 0 | 1.0000 | 1.0000 | 1.0000 |
| C11_bm25_v2 | antilexica | 11 | 11 | 9 | 6 | 3 | 0.8182 | 0.5455 | 0.5455 |

## Cohorte dirigida (E-A..E-D) — separada, no promediada con la otra

| celda | variante | n_casos | n_anclas | vistas | consultadas | brecha v-s-c | recall vista micro | recall consultada micro | recall consultada macro |
|---|---|---|---|---|---|---|---|---|---|
| C00_booleano_v1 | literal | 39 | 42 | 41 | 38 | 4 | 0.9762 | 0.9048 | 0.8974 |
| C00_booleano_v1 | antilexica | 39 | 42 | 36 | 27 | 9 | 0.8571 | 0.6429 | 0.6538 |
| C10_bm25_v1 | literal | 39 | 42 | 41 | 41 | 1 | 0.9762 | 0.9762 | 0.9744 |
| C10_bm25_v1 | antilexica | 39 | 42 | 39 | 30 | 9 | 0.9286 | 0.7143 | 0.7179 |
| C01_booleano_v2 | literal | 39 | 42 | 41 | 37 | 5 | 0.9762 | 0.8810 | 0.8846 |
| C01_booleano_v2 | antilexica | 39 | 42 | 36 | 26 | 11 | 0.8571 | 0.6190 | 0.6026 |
| C11_bm25_v2 | literal | 39 | 42 | 42 | 41 | 1 | 1.0000 | 0.9762 | 0.9744 |
| C11_bm25_v2 | antilexica | 39 | 42 | 38 | 31 | 8 | 0.9048 | 0.7381 | 0.7308 |

## Por estrato × variante (recall micro; macro en el JSON)

| celda | estrato | variante | n_casos | n_anclas | vistas | consultadas | brecha | recall vista micro | recall consultada micro |
|---|---|---|---|---|---|---|---|---|---|
| C00_booleano_v1 | E-A | literal | 13 | 15 | 14 | 14 | 1 | 0.9333 | 0.9333 |
| C00_booleano_v1 | E-A | antilexica | 13 | 15 | 11 | 9 | 2 | 0.7333 | 0.6000 |
| C00_booleano_v1 | E-B | literal | 18 | 19 | 19 | 19 | 0 | 1.0000 | 1.0000 |
| C00_booleano_v1 | E-B | antilexica | 18 | 19 | 19 | 14 | 5 | 1.0000 | 0.7368 |
| C00_booleano_v1 | E-D | literal | 8 | 8 | 8 | 5 | 3 | 1.0000 | 0.6250 |
| C00_booleano_v1 | E-D | antilexica | 8 | 8 | 6 | 4 | 2 | 0.7500 | 0.5000 |
| C00_booleano_v1 | E-E | literal | 11 | 11 | 11 | 9 | 2 | 1.0000 | 0.8182 |
| C00_booleano_v1 | E-E | antilexica | 11 | 11 | 10 | 6 | 4 | 0.9091 | 0.5455 |
| C10_bm25_v1 | E-A | literal | 13 | 15 | 14 | 15 | 0 | 0.9333 | 1.0000 |
| C10_bm25_v1 | E-A | antilexica | 13 | 15 | 13 | 12 | 1 | 0.8667 | 0.8000 |
| C10_bm25_v1 | E-B | literal | 18 | 19 | 19 | 19 | 0 | 1.0000 | 1.0000 |
| C10_bm25_v1 | E-B | antilexica | 18 | 19 | 19 | 15 | 4 | 1.0000 | 0.7895 |
| C10_bm25_v1 | E-D | literal | 8 | 8 | 8 | 7 | 1 | 1.0000 | 0.8750 |
| C10_bm25_v1 | E-D | antilexica | 8 | 8 | 7 | 3 | 4 | 0.8750 | 0.3750 |
| C10_bm25_v1 | E-E | literal | 11 | 11 | 11 | 11 | 0 | 1.0000 | 1.0000 |
| C10_bm25_v1 | E-E | antilexica | 11 | 11 | 9 | 6 | 3 | 0.8182 | 0.5455 |
| C01_booleano_v2 | E-A | literal | 13 | 15 | 14 | 14 | 1 | 0.9333 | 0.9333 |
| C01_booleano_v2 | E-A | antilexica | 13 | 15 | 14 | 12 | 3 | 0.9333 | 0.8000 |
| C01_booleano_v2 | E-B | literal | 18 | 19 | 19 | 18 | 1 | 1.0000 | 0.9474 |
| C01_booleano_v2 | E-B | antilexica | 18 | 19 | 17 | 10 | 7 | 0.8947 | 0.5263 |
| C01_booleano_v2 | E-D | literal | 8 | 8 | 8 | 5 | 3 | 1.0000 | 0.6250 |
| C01_booleano_v2 | E-D | antilexica | 8 | 8 | 5 | 4 | 1 | 0.6250 | 0.5000 |
| C01_booleano_v2 | E-E | literal | 11 | 11 | 11 | 10 | 1 | 1.0000 | 0.9091 |
| C01_booleano_v2 | E-E | antilexica | 11 | 11 | 10 | 6 | 4 | 0.9091 | 0.5455 |
| C11_bm25_v2 | E-A | literal | 13 | 15 | 15 | 15 | 0 | 1.0000 | 1.0000 |
| C11_bm25_v2 | E-A | antilexica | 13 | 15 | 12 | 11 | 2 | 0.8000 | 0.7333 |
| C11_bm25_v2 | E-B | literal | 18 | 19 | 19 | 19 | 0 | 1.0000 | 1.0000 |
| C11_bm25_v2 | E-B | antilexica | 18 | 19 | 19 | 16 | 3 | 1.0000 | 0.8421 |
| C11_bm25_v2 | E-D | literal | 8 | 8 | 8 | 7 | 1 | 1.0000 | 0.8750 |
| C11_bm25_v2 | E-D | antilexica | 8 | 8 | 7 | 4 | 3 | 0.8750 | 0.5000 |
| C11_bm25_v2 | E-E | literal | 11 | 11 | 11 | 11 | 0 | 1.0000 | 1.0000 |
| C11_bm25_v2 | E-E | antilexica | 11 | 11 | 9 | 6 | 3 | 0.8182 | 0.5455 |

## Diferencias apareadas (punto e IC bootstrap 95 %, semilla `bootstrap-ablacion-v1`, 10000 remuestreos, n_pares=50)

| estadístico | punto | IC95 inf | IC95 sup |
|---|---|---|---|
| dif_consultada_micro::literal::C10_bm25_v1-C00_booleano_v1 | 0.0943 | 0.0192 | 0.1800 |
| dif_consultada_macro::literal::C10_bm25_v1-C00_booleano_v1 | 0.1000 | 0.0200 | 0.1800 |
| dif_vista_micro::literal::C10_bm25_v1-C00_booleano_v1 | 0.0000 | 0.0000 | 0.0000 |
| dif_consultada_micro::antilexica::C10_bm25_v1-C00_booleano_v1 | 0.0566 | -0.0800 | 0.1964 |
| dif_consultada_macro::antilexica::C10_bm25_v1-C00_booleano_v1 | 0.0500 | -0.1000 | 0.2000 |
| dif_vista_micro::antilexica::C10_bm25_v1-C00_booleano_v1 | 0.0377 | -0.0600 | 0.1373 |
| dif_consultada_micro::literal::C01_booleano_v2-C00_booleano_v1 | 0.0000 | -0.0545 | 0.0566 |
| dif_consultada_macro::literal::C01_booleano_v2-C00_booleano_v1 | 0.0100 | -0.0300 | 0.0600 |
| dif_vista_micro::literal::C01_booleano_v2-C00_booleano_v1 | 0.0000 | 0.0000 | 0.0000 |
| dif_consultada_micro::antilexica::C01_booleano_v2-C00_booleano_v1 | -0.0189 | -0.1569 | 0.1111 |
| dif_consultada_macro::antilexica::C01_booleano_v2-C00_booleano_v1 | -0.0400 | -0.1700 | 0.0900 |
| dif_vista_micro::antilexica::C01_booleano_v2-C00_booleano_v1 | 0.0000 | -0.1000 | 0.1071 |
| dif_consultada_micro::literal::C11_bm25_v2-C00_booleano_v1 | 0.0943 | 0.0192 | 0.1800 |
| dif_consultada_macro::literal::C11_bm25_v2-C00_booleano_v1 | 0.1000 | 0.0200 | 0.1800 |
| dif_vista_micro::literal::C11_bm25_v2-C00_booleano_v1 | 0.0189 | 0.0000 | 0.0566 |
| dif_consultada_micro::antilexica::C11_bm25_v2-C00_booleano_v1 | 0.0755 | -0.0943 | 0.2353 |
| dif_consultada_macro::antilexica::C11_bm25_v2-C00_booleano_v1 | 0.0600 | -0.1100 | 0.2300 |
| dif_vista_micro::antilexica::C11_bm25_v2-C00_booleano_v1 | 0.0189 | -0.0962 | 0.1296 |
| dif_consultada_micro::literal::C11_bm25_v2-C10_bm25_v1 | 0.0000 | 0.0000 | 0.0000 |
| dif_consultada_macro::literal::C11_bm25_v2-C10_bm25_v1 | 0.0000 | 0.0000 | 0.0000 |
| dif_vista_micro::literal::C11_bm25_v2-C10_bm25_v1 | 0.0189 | 0.0000 | 0.0566 |
| dif_consultada_micro::antilexica::C11_bm25_v2-C10_bm25_v1 | 0.0189 | -0.0784 | 0.1154 |
| dif_consultada_macro::antilexica::C11_bm25_v2-C10_bm25_v1 | 0.0100 | -0.0900 | 0.1100 |
| dif_vista_micro::antilexica::C11_bm25_v2-C10_bm25_v1 | -0.0189 | -0.1091 | 0.0588 |
| dif_consultada_micro::literal::C11_bm25_v2-C01_booleano_v2 | 0.0943 | 0.0192 | 0.1765 |
| dif_consultada_macro::literal::C11_bm25_v2-C01_booleano_v2 | 0.0900 | 0.0200 | 0.1700 |
| dif_vista_micro::literal::C11_bm25_v2-C01_booleano_v2 | 0.0189 | 0.0000 | 0.0566 |
| dif_consultada_micro::antilexica::C11_bm25_v2-C01_booleano_v2 | 0.0943 | -0.0566 | 0.2457 |
| dif_consultada_macro::antilexica::C11_bm25_v2-C01_booleano_v2 | 0.1000 | -0.0600 | 0.2600 |
| dif_vista_micro::antilexica::C11_bm25_v2-C01_booleano_v2 | 0.0189 | -0.0943 | 0.1321 |
| delta_c_micro::C00_booleano_v1 | 0.2642 | 0.1321 | 0.3962 |
| delta_c_micro::C10_bm25_v1 | 0.3019 | 0.1818 | 0.4259 |
| delta_c_micro::C01_booleano_v2 | 0.2830 | 0.1509 | 0.4200 |
| delta_c_micro::C11_bm25_v2 | 0.2830 | 0.1509 | 0.4231 |
| dif_delta_c_micro::C10_bm25_v1-C00_booleano_v1 | 0.0377 | -0.1154 | 0.1961 |
| dif_delta_c_micro::C11_bm25_v2-C01_booleano_v2 | 0.0000 | -0.1569 | 0.1569 |
| dif_delta_c_micro::C01_booleano_v2-C00_booleano_v1 | 0.0189 | -0.1273 | 0.1765 |
| dif_delta_c_micro::C11_bm25_v2-C10_bm25_v1 | -0.0189 | -0.1154 | 0.0784 |
| interaccion_anti_micro::(C11-C00)-[(C10-C00)+(C01-C00)] | 0.0377 | -0.0962 | 0.1800 |

## Predicciones P1–P6 (evaluación mecánica, umbrales sellados; regla de lectura textual)

| predicción | veredicto | detalle |
|---|---|---|
| P1 (gate Δ_c(C00) ≥ 0.15) | **cumplida** | Δ_c(C00) = 0.2642 (lit 0.8868 → anti 0.6226); n_pares 50 |
| P2 (Δ_c(C10) ≤ ½Δ_c(C00) y Δ_c(C11) ≤ ½Δ_c(C01)) | **no cumplida** | Δ_c = {'C00_booleano_v1': 0.2642, 'C10_bm25_v1': 0.3019, 'C01_booleano_v2': 0.283, 'C11_bm25_v2': 0.283}; C10/C00 ratio 1.1427 (False); C11/C01 ratio 1.0000 (False) |
| P3 (no regresión literal, margen 0.05) | **cumplida** | consultada_lit_C10_vs_C00: 0.9811 vs 0.8868 → True; consultada_lit_C11_vs_C01: 0.9811 vs 0.8868 → True; vista_lit_C10_vs_C00: 0.9811 vs 0.9811 → True; vista_lit_C11_vs_C01: 1.0000 vs 0.9811 → True |
| P4 (tools v2, direccional) | **no cumplida** | i_EB_entrante: no cumplida; ii_a_hit_tool_limit_baja: no cumplida; ii_b_clase_K_mejora_mas: cumplida; iii_efecto_T_menor_que_R: cumplida |
| P5 (C11 mejor y aditiva ≤ 0.1) | **cumplida** | anti micro {'C00_booleano_v1': 0.6226, 'C10_bm25_v1': 0.6792, 'C01_booleano_v2': 0.6038, 'C11_bm25_v2': 0.6981}; mejor C11_bm25_v2; interacción 0.0377 |
| P6 (huérfanos de label, 11 pares) | **no cumplida** | vista {'C00_booleano_v1': 0.3636, 'C10_bm25_v1': 0.4091, 'C01_booleano_v2': 0.2273, 'C11_bm25_v2': 0.5} (C10 ≤ C00+0.1: True); consultada v1 0.4773 vs v2 0.4773 (False); paginación v2 {'C01_booleano_v2': {'pagina_gt1': 0, 'ver_vecinos': 123, 'tasa': 0.0}, 'C11_bm25_v2': {'pagina_gt1': 0, 'ver_vecinos': 152, 'tasa': 0.0}} |

Detalle P4:

- `i_EB_entrante`: **no cumplida** — {"n_pares": 9, "recall_c_micro_ambas": {"C00_booleano_v1": 0.85, "C10_bm25_v1": 0.9, "C01_booleano_v2": 0.7, "C11_bm25_v2": 0.9}, "por_variante": {"literal": {"C00_booleano_v1": 1.0, "C10_bm25_v1": 1.0, "C01_booleano_v2": 0.9, "C11_bm25_v2": 1.0}, "antilexica": {"C00_booleano_v1": 0.7, "C10_bm25_v1": 0.8, "C01_booleano_v2": 0.5, "C11_bm25_v2": 0.8}}, "C01_gt_C00": false, "C11_gt_C10": false}
- `ii_a_hit_tool_limit_baja`: **no cumplida** — {"tasa_hit_tool_limit": {"C00_booleano_v1": 0.36, "C10_bm25_v1": 0.29, "C01_booleano_v2": 0.37, "C11_bm25_v2": 0.24}, "C01_lt_C00": false, "C11_lt_C10": true}
- `ii_b_clase_K_mejora_mas`: **cumplida** — {"K_n_unidades": 43, "K_n_pares": 35, "K_mejoran_en_C01": 6, "K_fraccion": 0.1395, "resto_n_unidades": 57, "resto_n_pares": 42, "resto_mejoran_en_C01": 1, "resto_fraccion": 0.0175}
- `iii_efecto_T_menor_que_R`: **cumplida** — {"efecto_T_C01_menos_C00": -0.0188, "efecto_R_C10_menos_C00": 0.0566}

## Tasas y latencias por celda

| celda | n_trazas | hit_tool_limit (tasa) | abstención (tasa) | parse_ok (tasa) | errores técnicos | tool calls media | latencia p50 s | latencia p95 s | costo USD (CLI) | replay OK |
|---|---|---|---|---|---|---|---|---|---|---|
| C00_booleano_v1 | 100 | 36 (0.3600) | 20 (0.2000) | 100 (1.0000) | 0 | 10.25 | 17.661 | 28.968 | 2.8292 | True |
| C10_bm25_v1 | 100 | 29 (0.2900) | 11 (0.1100) | 99 (0.9900) | 1 | 10.02 | 16.449 | 28.026 | 2.7669 | True |
| C01_booleano_v2 | 100 | 37 (0.3700) | 15 (0.1500) | 100 (1.0000) | 0 | 10.16 | 19.973 | 30.680 | 2.8519 | True |
| C11_bm25_v2 | 100 | 24 (0.2400) | 12 (0.1200) | 100 (1.0000) | 0 | 9.51 | 16.714 | 31.664 | 2.7468 | True |

Latencia por tool (p50 / p95, s) y uso de paginación/filtro en ver_vecinos:

- C00_booleano_v1: buscar_nodos n=608 p50=0.0328 p95=0.1112; ver_nodo n=286 p50=0.0041 p95=0.0170; ver_vecinos n=131 p50=0.0087 p95=0.0219; llamadas {'buscar_nodos': 608, 'ver_nodo': 286, 'ver_vecinos': 131}; pagina>1 {'n': 0, 'de': 131, 'tasa': 0.0}; con relación {'n': 0, 'de': 131, 'tasa': 0.0}
- C10_bm25_v1: buscar_nodos n=535 p50=0.0123 p95=0.0381; ver_nodo n=305 p50=0.0039 p95=0.0162; ver_vecinos n=162 p50=0.0095 p95=0.0226; llamadas {'buscar_nodos': 535, 'ver_nodo': 305, 'ver_vecinos': 162}; pagina>1 {'n': 0, 'de': 162, 'tasa': 0.0}; con relación {'n': 0, 'de': 162, 'tasa': 0.0}
- C01_booleano_v2: buscar_nodos n=615 p50=0.0349 p95=0.1268; ver_nodo n=278 p50=0.0040 p95=0.0168; ver_vecinos n=123 p50=0.0144 p95=0.0403; llamadas {'buscar_nodos': 615, 'ver_nodo': 278, 'ver_vecinos': 123}; pagina>1 {'n': 0, 'de': 123, 'tasa': 0.0}; con relación {'n': 5, 'de': 123, 'tasa': 0.0407}
- C11_bm25_v2: buscar_nodos n=504 p50=0.0109 p95=0.0306; ver_nodo n=295 p50=0.0041 p95=0.0159; ver_vecinos n=152 p50=0.0147 p95=0.0313; llamadas {'buscar_nodos': 504, 'ver_nodo': 295, 'ver_vecinos': 152}; pagina>1 {'n': 0, 'de': 152, 'tasa': 0.0}; con relación {'n': 7, 'de': 152, 'tasa': 0.0461}

## Operacionalizaciones declaradas

- **nivel_P1_P5**: grupo `todos` (todos los pares apareados), recall MICRO pooled por ancla — mismo nivel que la referencia EV2 (0,958→0,620); las cohortes E-E y E-A..E-D se reportan aparte y no entran promediadas
- **pares_apareados**: solo pares con las 2 variantes presentes en las 4 celdas entran a la tabla central, a las diferencias y a P1–P6; los faltantes se listan
- **P4_i**: sub-estrato E-B/entrante; recall consultada micro POOLED sobre ambas variantes (el pre-registro no fija variante); se reporta además por variante
- **P4_ii_a**: tasa de hit_tool_limit = trazas con hit_tool_limit / trazas de la celda (ambas variantes)
- **P4_ii_b**: clase K = (par, variante) cuya traza en C00 tiene hit_tool_limit o n_brecha > 0; 'pasa a consultada' = recall_consultada(C01) > recall_consultada(C00) (estrictamente mayor); se compara la fracción en K vs el resto; evaluable si K y resto tienen >= 8 pares distintos
- **P4_iii**: efecto de T = recall_c anti micro (C01 − C00); efecto de R = (C10 − C00); cumplida si T < R
- **P4_veredicto**: cumplida si (i), (ii-a), (ii-b) y (iii) cumplidas; no cumplida si alguna no cumplida; no evaluable si alguna no evaluable y ninguna no cumplida
- **P5**: mejor celda = C11 estrictamente máxima en recall consultada micro anti-léxica; aditividad |(C11−C00) − [(C10−C00)+(C01−C00)]| <= 0,10
- **P6**: unidad = (par, variante, nodo gold huérfano de label) sobre los 11 pares marcados ex-ante; (i) fracción vista C10 <= C00 + 0,10; (ii) fracción consultada en celdas v2 (C01 ∪ C11 pooled) > celdas v1 (C00 ∪ C10 pooled), y además por par de celdas; tasa de paginación = llamadas ver_vecinos con pagina > 1 / llamadas ver_vecinos, en celdas v2
- **abstencion**: traza con parse_ok y final_json.respondible == false
- **error_tecnico**: traza con trace.error no nulo (persistida; la métrica se computa sobre sus steps)
- **percentil**: interpolación lineal entre órdenes (tipo numpy default) sobre los valores presentes
- **no_evaluable_n**: una clase con < 8 pares distintos es no evaluable a priori
