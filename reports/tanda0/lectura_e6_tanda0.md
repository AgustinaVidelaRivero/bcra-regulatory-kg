# Lecturas de grafo de E6 (U-TANDA0-2A, tanda 0)

Generado por `data/experiment/tanda0/code/lectura_e6_tanda0.py` desde `reports/tanda0/lectura_e6_tanda0.json`. Sin umbral (decisión 6 del pre-registro).

## Observación (10): aristas de extracción por unidad (A4.1)

| ensamblado | total | referencia | esqueleto | extracción | unidades | por unidad | banda | lectura |
|---|---|---|---|---|---|---|---|---|
| r1 (base) | 17772 | 5680 | 82 | 12010 | 1763 | 6.81 | | |
| cinco | 3983 | 521 | 117 | 3345 | 671 | 4.99 | [5.0, 8.0] | debajo de la banda |
| desarrollo | 15007 | 4256 | 117 | 10634 | 1763 | 6.03 | [6.81, 8.0] | debajo de la banda |
| diez | 18932 | 4836 | 117 | 13979 | 2434 | 5.74 |  | informativo (A4.1 no predice sobre el ensamblado de diez) |

## Observación (11): remisiones y aristas entre documentos (A4.2)

| ensamblado | menciones | resueltas | parciales | irresolubles | fuera del inventario | aristas_cross_to |
|---|---|---|---|---|---|---|
| r1 (base) | 1089 | 837 | 20 | 252 | 106 | 188 |
| cinco | 169 | 115 | 4 | 54 | 26 | 3 |
| desarrollo | 783 | 570 | 22 | 213 | 94 | 124 |
| diez | 952 | 695 | 26 | 257 | 107 | 186 |

- aristas_cross_to en el grafo de desarrollo re-extraído: predicho 188 ± 20, observado 124 (fuera)
- aristas_cross_to en el ensamblado de diez: predicho mayor que 188, observado 186 (no cumple)
- remisiones de desarrollo a los cinco: fuera del inventario en desarrollo 4 {'docvig': 2, 'polcre': 2}; en diez hacia los cinco, por estado {'resuelta': 4}, por TO {'docvig': 2, 'polcre': 2}; siguen fuera del inventario 0
- las menciones salen de la extracción (E1), no del texto de E0: el ensamblado de desarrollo tiene 783 contra 1089 de r1, así que las 106 de r1 no se pueden seguir una por una; el conteo comparable es el de esta clave

## Vigilancias (1) a (9) (A4.3)

- (1) migraciones tipo-Condicion contra la guarda de modalidad — línea de base: 1/12 en fresca. {"medida": "no medida: el muestreo quedó «a definir en fase 2» (A4.3) y el mandato no lo definió; se reporta la población", "poblacion": {"cinco": {"aristas_condicion_de": 127, "nodos_Condicion": 205}, "desarrollo": {"aristas_condicion_de": 448, "nodos_Condicion": 1178}, "diez": {"aristas_condicion_de": 575, "nodos_Condicion": 1383}}}
- (2) vaciamientos (unidad sin relaciones aceptadas) — línea de base: v1 2/43 · v2 2/27. {"medida": "conteo de unidades con 0 relaciones aceptadas; la lectura de muestra que A4.3 cruza con ese conteo no se hizo (muestreo no definido)", "por_to": {"cap": {"cero_relaciones_final": 9, "cero_relaciones_primer_intento": 13, "con_error_final": 5, "unidades_e1": 462, "unidades_finales": 462}, "cla": {"cero_relaciones_final": 0, "cero_relaciones_primer_intento": 1, "con_error_final": 2, "unidades_e1": 143, "unidades_finales": 143}, "ctacte": {"cero_relaciones_final": 11, "cero_relaciones_primer_intento": 23, "con_error_final": 18, "unidades_e1": 388, "unidades_finales": 388}, "docvig": {"cero_relaciones_final": 0, "cero_relaciones_primer_intento": 2, "con_error_final": 3, "unidades_e1": 31, "unidades_finales": 31}, "ext": {"cero_relaciones_final": 22, "cero_relaciones_primer_intento": 28, "con_error_final": 30, "unidades_e1": 973, "unidades_finales": 973}, "lingob": {"cero_relaciones_final": 0, "cero_relaciones_primer_intento": 2, "con_error_final": 6, "unidades_e1": 139, "unidades_finales": 139}, "pagjub": {"cero_relaciones_final": 0, "cero_relaciones_primer_intento": 0, "con_error_final": 0, "unidades_e1": 52, "unidades_finales": 52}, "polcre": {"cero_relaciones_final": 0, "cero_relaciones_primer_intento": 0, "con_error_final": 0, "unidades_e1": 61, "unidades_finales": 61}, "pro": {"cero_relaciones_final": 1, "cero_relaciones_primer_intento": 3, "con_error_final": 2, "unidades_e1": 101, "unidades_finales": 101}, "ric": {"cero_relaciones_final": 3, "cero_relaciones_primer_intento": 5, "con_error_final": 5, "unidades_e1": 84, "unidades_finales": 84}}, "total_cero_relaciones_final": 46, "total_unidades": 2434}
- (3) duplicación de contenido entre cajas — línea de base: 5 casos v1. {"medida": "no medida: A4.3 deja el muestreo «a definir en fase 2» y el mandato no fijó instrumento"}
- (4) un nodo TextoOrdenado por TO — línea de base: 2 archivos afectados en lecturas. {"por_ensamblado": {"cinco": {"ctacte": 1, "docvig": 1, "lingob": 1, "pagjub": 1, "polcre": 1}, "desarrollo": {"cap": 1, "cla": 1, "ext": 1, "pro": 1, "ric": 1}, "diez": {"cap": 1, "cla": 1, "ctacte": 1, "docvig": 1, "ext": 1, "lingob": 1, "pagjub": 1, "polcre": 1, "pro": 1, "ric": 1}}, "todos_uno": true}
- (5) emisiones residuales de requisito_de_estructura — línea de base: 0 por construcción. {"hallazgo_S20_ext_10_4_3_1": {"rechazos_por_motivo": {"firma_invalida": 1}, "relations_in": 5, "relations_out": 4, "tipo_obligacion_normalizados": 0, "tipo_obligacion_requisito_de_estructura": 0}, "tipo_obligacion_normalizados": {"cap": 0, "cla": 0, "ctacte": 2, "docvig": 0, "ext": 0, "lingob": 1, "pagjub": 0, "polcre": 0, "pro": 0, "ric": 0}, "tipo_obligacion_requisito_de_estructura": {"cap": 0, "cla": 0, "ctacte": 0, "docvig": 0, "ext": 0, "lingob": 0, "pagjub": 0, "polcre": 0, "pro": 0, "ric": 0}}
- (6) unidades propias vacías (health-check de E0) — línea de base: sin línea de base numérica. {"fuente": "reports/tanda0/healthcheck_e0_tanda0_cinco.json", "por_to": {"ctacte": {"senales": {"cid": {"lineas": 0, "muestras": [], "paginas": []}, "cobertura_no_exacta": null, "paginas_sin_seccion": {"avisos_pagina_cuerpo_sin_seccion": 0, "paginas": [], "paginas_cuerpo": 60, "secciones_parseadas": 13, "sin_pagina_de_cuerpo": false}, "unidades_anomalas_por_tamano": {"anomalas": [], "chunks_terminales": 336, "max_chars_propio": 2870, "mediana_chars_propio": 241.0, "umbral_chars": 26182}}, "veredicto": "sano"}, "docvig": {"senales": {"cid": {"lineas": 0, "muestras": [], "paginas": []}, "cobertura_no_exacta": null, "paginas_sin_seccion": {"avisos_pagina_cuerpo_sin_seccion": 0, "paginas": [], "paginas_cuerpo": 8, "secciones_parseadas": 4, "sin_pagina_de_cuerpo": false}, "unidades_anomalas_por_tamano": {"anomalas": [], "chunks_terminales": 29, "max_chars_propio": 1146, "mediana_chars_propio": 237, "umbral_chars": 26182}}, "veredicto": "sano"}, "lingob": {"senales": {"cid": {"lineas": 2, "muestras": [{"pagina": 13, "rol": "cuerpo", "texto": "Versión: (cid:21)a. COMUNICACIÓN “A” 5599 Página 1"}, {"pagina": 14, "rol": "cuerpo", "texto": "Versión: (cid:21)a. COMUNICACIÓN “A” 5599 Página 2"}], "paginas": [13, 14]}, "cobertura_no_exacta": null, "paginas_sin_seccion": {"avisos_pagina_cuerpo_sin_seccion": 0, "paginas": [], "paginas_cuerpo": 19, "secciones_parseadas": 8, "sin_pagina_de_cuerpo": false}, "unidades_anomalas_por_tamano": {"anomalas": [], "chunks_terminales": 118, "max_chars_propio": 1544, "mediana_chars_propio": 197.5, "umbral_chars": 26182}}, "veredicto": ["cid"]}, "pagjub": {"senales": {"cid": {"lineas": 2, "muestras": [{"pagina": 1, "rol": "portada", "texto": "-Última comunicación incorporada: “A” (cid:25)386-"}, {"pagina": 1, "rol": "portada", "texto": "07 12 (cid:26)"}], "paginas": [1]}, "cobertura_no_exacta": null, "paginas_sin_seccion": {"avisos_pagina_cuerpo_sin_seccion": 0, "paginas": [], "paginas_cuerpo": 10, "secciones_parseadas": 3, "sin_pagina_de_cuerpo": false}, "unidades_anomalas_por_tamano": {"anomalas": [], "chunks_terminales": 43, "max_chars_propio": 2146, "mediana_chars_propio": 230, "umbral_chars": 26182}}, "veredicto": ["cid"]}, "polcre": {"senales": {"cid": {"lineas": 0, "muestras": [], "paginas": []}, "cobertura_no_exacta": null, "paginas_sin_seccion": {"avisos_pagina_cuerpo_sin_seccion": 0, "paginas": [], "paginas_cuerpo": 19, "secciones_parseadas": 10, "sin_pagina_de_cuerpo": false}, "unidades_anomalas_por_tamano": {"anomalas": [], "chunks_terminales": 55, "max_chars_propio": 1714, "mediana_chars_propio": 468, "umbral_chars": 26182}}, "veredicto": "sano"}}}
- (7) roles de alcance en ejecuta — línea de base: n = 1 en la muestra pareada de B5.4. {"medida": "población (aristas ejecuta con origen Sujeto_rol_alcance_<to>); la tasa sin apoyo textual pide muestreo, no definido", "por_ensamblado": {"cinco": {"ejecuta": 36, "ejecuta_con_rol_alcance": 0}, "desarrollo": {"ejecuta": 121, "ejecuta_con_rol_alcance": 21}, "diez": {"ejecuta": 157, "ejecuta_con_rol_alcance": 21}}}
- (8) tasa de sujeto_propuesto — línea de base: {'sujeto_id': 3905, 'sujeto_propuesto': 124, 'tasa_pct': 3.08}. {"cinco": {"sujeto_id": 981, "sujeto_propuesto": 19, "tasa_pct": 1.9}, "desarrollo": {"sujeto_id": 2977, "sujeto_propuesto": 42, "tasa_pct": 1.39}, "diez": {"sujeto_id": 3958, "sujeto_propuesto": 61, "tasa_pct": 1.52}, "fuente": "validacion.relaciones de extracciones_finales_<to>.jsonl (relaciones aceptadas de E1)"}
- (9) emisiones de Sujeto_entidad_originante_de_transferencia — línea de base: 13 menciones / 5 TOs en fase 1; 2→1 en la unidad adversarial. {"aristas_en_kg": {"cinco": 0, "desarrollo": 5, "diez": 5}, "emisiones_E1_por_to": {"cap": 4, "cla": 0, "ctacte": 0, "docvig": 0, "ext": 1, "lingob": 0, "pagjub": 0, "polcre": 0, "pro": 0, "ric": 0}, "nota": "A4.3: ninguno de los cinco nuevos es del dominio de pagos"}

## Plan (1): aristas referencia por tipo de origen

- cinco: {'Excepcion': 80, 'Obligacion': 222, 'Operacion': 146, 'Restriccion': 70, 'TextoOrdenado': 3}; desde Condicion, Potestad o Definicion: 0
- desarrollo: {'Excepcion': 510, 'Obligacion': 1409, 'Operacion': 1805, 'Restriccion': 518, 'TextoOrdenado': 14}; desde Condicion, Potestad o Definicion: 0
- diez: {'Excepcion': 590, 'Obligacion': 1677, 'Operacion': 1953, 'Restriccion': 599, 'TextoOrdenado': 17}; desde Condicion, Potestad o Definicion: 0

## Plan (2): rechazos de E1 por par

- 982 rechazos `firma_invalida` en 65 pares (`reports/u_audit_tipos_v3/p4_resumen.json`, sha256 `e63e2618faa96708…`); primeros pares: Condicion –condicion_de→ Operacion 424; Condicion –condicion_de→ Potestad 231; Condicion –aplica_a→ Sujeto 45; Excepcion –exceptua→ Operacion 27; Definicion –aplica_a→ Sujeto 23; Excepcion –exceptua_obligacion→ Restriccion 19; Condicion –condicion_de→ Definicion 17; Condicion –condiciona→ Operacion 15

## Plan (6): aristas entre documentos distintos

Regla: documento de un nodo = conjunto de valores `to` de sus `provenances`; una arista va entre documentos distintos si origen y destino tienen un solo documento cada uno y son distintos; si alguno tiene más de un documento (Sujeto del catálogo, nodos fundidos) se cuenta aparte como «con nodo multidocumento».

- cinco: {'esqueleto': {'con_nodo_multidocumento': 7, 'entre_documentos': 3, 'mismo_documento': 2, 'sin_procedencia': 105}, 'extraccion': {'con_nodo_multidocumento': 880, 'entre_documentos': 2, 'mismo_documento': 2461, 'sin_procedencia': 2}, 'referencia': {'con_nodo_multidocumento': 0, 'entre_documentos': 3, 'mismo_documento': 518, 'sin_procedencia': 0}}; nodos multidocumento 6
  - entre documentos por relación: {'esqueleto:subclase_de': 3, 'extraccion:padre_sugerido': 2, 'referencia:referencia': 3}
- desarrollo: {'esqueleto': {'con_nodo_multidocumento': 28, 'entre_documentos': 0, 'mismo_documento': 5, 'sin_procedencia': 84}, 'extraccion': {'con_nodo_multidocumento': 303, 'entre_documentos': 0, 'mismo_documento': 10325, 'sin_procedencia': 6}, 'referencia': {'con_nodo_multidocumento': 0, 'entre_documentos': 124, 'mismo_documento': 4132, 'sin_procedencia': 0}}; nodos multidocumento 19
  - entre documentos por relación: {'referencia:referencia': 124}
- diez: {'esqueleto': {'con_nodo_multidocumento': 36, 'entre_documentos': 5, 'mismo_documento': 5, 'sin_procedencia': 71}, 'extraccion': {'con_nodo_multidocumento': 1212, 'entre_documentos': 2, 'mismo_documento': 12758, 'sin_procedencia': 7}, 'referencia': {'con_nodo_multidocumento': 0, 'entre_documentos': 186, 'mismo_documento': 4650, 'sin_procedencia': 0}}; nodos multidocumento 21
  - entre documentos por relación: {'esqueleto:subclase_de': 5, 'extraccion:padre_sugerido': 2, 'referencia:referencia': 186}

## Control de las tres aplica_a (checklist del gate)

- {'cinco': {'nodos_de_ri_tii_o_ri_pscpp': 0, 'presentes': 0}, 'desarrollo': {'nodos_de_ri_tii_o_ri_pscpp': 0, 'presentes': 0}, 'diez': {'nodos_de_ri_tii_o_ri_pscpp': 0, 'presentes': 0}}; control vacuo en la tanda 0: ri_tii y ri_pscpp no están en ningún ensamblado

## Suite de regresión

- cinco: {'items': 46, 'no_aplicable': 13, 'persiste': 22, 'resuelto': 11}
- desarrollo: {'items': 46, 'no_aplicable': 8, 'persiste': 16, 'resuelto': 22}
- diez: {'items': 46, 'no_aplicable': 8, 'persiste': 18, 'resuelto': 20}
- desarrollo contra la entrada KG-Reextraido-r1 de la fixture: {'no_aplicable → no_aplicable': 7, 'no_aplicable → persiste': 2, 'persiste → no_aplicable': 1, 'persiste → persiste': 8, 'persiste → resuelto': 1, 'resuelto → persiste': 6, 'resuelto → resuelto': 21}

| ítem | r1 (fixture) | desarrollo |
|---|---|---|
| BKL-0003 | persiste | persiste |
| BKL-0004 | persiste | persiste |
| BKL-0005 | resuelto | resuelto |
| BKL-0006 | persiste | no_aplicable |
| BKL-0007 | persiste | persiste |
| BKL-0017 | persiste | persiste |
| BKL-0019 | persiste | persiste |
| BKL-0023 | no_aplicable | no_aplicable |
| BKL-0026 | no_aplicable | no_aplicable |
| BKL-0027 | no_aplicable | no_aplicable |
| BKL-0028 | no_aplicable | persiste |
| BKL-0029 | no_aplicable | persiste |
| E4-a1 | resuelto | resuelto |
| E4-a2 | resuelto | resuelto |
| E4-a3 | resuelto | resuelto |
| E4-a4 | resuelto | resuelto |
| E4-a5 | resuelto | resuelto |
| E4-a6 | resuelto | resuelto |
| E4-a7 | resuelto | persiste |
| E4-a8 | resuelto | persiste |
| E4-b | resuelto | resuelto |
| E4-c | no_aplicable | no_aplicable |
| I1 | no_aplicable | no_aplicable |
| I2 | no_aplicable | no_aplicable |
| I3 | resuelto | resuelto |
| I4 | resuelto | resuelto |
| I5 | resuelto | resuelto |
| RT-C5-1 | persiste | persiste |
| RT-C5-2 | persiste | persiste |
| RT-C5-3 | persiste | resuelto |
| RT-C5-4 | persiste | persiste |
| RT-C5-5 | no_aplicable | no_aplicable |
| RT-C6-1 | resuelto | resuelto |
| RT-C6-2 | resuelto | resuelto |
| RT-C6-3 | resuelto | resuelto |
| RT-C6-4 | resuelto | resuelto |
| RT-C7-1 | resuelto | resuelto |
| RT-C7-2 | resuelto | resuelto |
| RT-C7-3 | resuelto | resuelto |
| T1 | resuelto | resuelto |
| T2 | resuelto | persiste |
| T3 | resuelto | resuelto |
| T4 | resuelto | persiste |
| T5 | resuelto | persiste |
| T6 | resuelto | resuelto |
| T7 | resuelto | persiste |

## Intrínsecas (generación 3) y shapes

| métrica | r1 | desarrollo | cinco | diez |
|---|---|---|---|---|
| M10_chunks_mudos | 0.000567 | 0.001702 | 0.00149 | 0.001643 |
| M11_cobertura_CQ | None | None | None | None |
| M1_tasa_duplicacion_publicada | 0.54189 | 0.492944 | 0.342597 | 0.490795 |
| M2_tasa_duplicacion_gate | 0.273396 | 0.251176 | 0.133906 | 0.232195 |
| M3_tasa_conflacion | None | None | None | None |
| M4_average_degree | 5.444019 | 4.705864 | 4.025265 | 4.58624 |
| M5_avg_shortest_path | 3.767985 | 3.618413 | 3.659463 | 3.985075 |
| M6_concentracion_de_grado | {'gini_grado': 0.567389, 'grado_max': 2345, 'participacion_top1pct': 0.287869} | {'gini_grado': 0.605899, 'grado_max': 2789, 'participacion_top1pct': 0.348804} | {'gini_grado': 0.555455, 'grado_max': 1008, 'participacion_top1pct': 0.360156} | {'gini_grado': 0.597302, 'grado_max': 2789, 'participacion_top1pct': 0.354426} |
| M7_tasa_ruido_por_rol | 0.0 | 0.0 | 0.0 | 0.0 |
| M8_densidad | 0.00041697 | 0.00036897 | 0.00101751 | 0.00027779 |
| M9_nodos_aislados_y_componentes | {'componentes_conexas': 107, 'fraccion_en_componente_mayor': 0.983458, 'nodos_aislados': 105} | {'componentes_conexas': 95, 'fraccion_en_componente_mayor': 0.985262, 'nodos_aislados': 94} | {'componentes_conexas': 39, 'fraccion_en_componente_mayor': 0.980798, 'nodos_aislados': 38} | {'componentes_conexas': 121, 'fraccion_en_componente_mayor': 0.985465, 'nodos_aislados': 120} |

- shapes cinco: NO PASA; bloqueantes en FAIL ['S19']
- shapes desarrollo: NO PASA; bloqueantes en FAIL ['S19']
- shapes diez: NO PASA; bloqueantes en FAIL ['S19']

## Costo real de 2a

| etapa | USD | tope |
|---|---|---|
| E2 (E1 18.07154 + E3 con reintentos 22.277978) | 40.349518 | 60.0 |
| re-extracción dirigida | 0.461274 | 1.0 |
| E5 {'C2': 6.658455, 'C3': 6.218223, 'C4': 6.135934, 'C5': 2.245114} | 21.257726 | 40.0 |
| E5.c (adjudicación y cierre) | 0.0 | |
| **total 2a** | **62.068518** | 100.0 (estimación A7 69.18) |
