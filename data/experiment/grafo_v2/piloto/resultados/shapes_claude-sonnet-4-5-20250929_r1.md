# Shapes v2 — kg_claude-sonnet-4-5-20250929_r1.json

- Grafo: `../piloto/resultados/kg_claude-sonnet-4-5-20250929_r1.json`
- Fecha: 2026-07-26
- Nodos: 248 | Aristas: 452

| Regla | Resultado | Resumen |
|---|---|---|
| S1 | PASS | 452/452 válidas; 0 violaciones. |
| S2 | PASS | 0 aristas colgantes sobre 452. |
| S3 | PASS | 452/452 conformes; 0 violaciones. |
| S4 | PASS | Nodos OK: 248/248. Aristas OK: 452/452. Violaciones: 0. |
| S5 | PASS | Nodos OK: 248/248. Aristas OK: 452/452. Violaciones: 0. |
| S6 | PASS | Conjunto válido: 5 TOs + esquema. Violaciones: 0. |
| S7 | PASS | 0 grupos violatorios (0 nodos). |
| S8 | WARN | 1 grupos cross-type. |
| S9 | PASS | 0 nodos con ambas keys. |
| S10 | PASS | Sin establecida_en: Obligacion=0, Restriccion=0, Excepcion=0 (total 0). |
| S11 | WARN | Sin aplica_a: Obligacion=0, Restriccion=4 (total 4). |
| S12 | FAIL | 8 Excepciones huérfanas. |
| S13 | PASS | 72/72 Sujetos con nivel válido; 0 violaciones. |

## S8 — detalle

```
'clasificacion de deudores': [TextoOrdenado] TextoOrdenado_to_clasificacion_deudores_actual_pdf, [Operacion] Operacion_clasificacion_de_deudores
```

## S11 — detalle

```
Restriccion: Restriccion_seran_elegibles_para_el_importador_quedando_obligadas_a_llevar_a_cabo_las_respon
Restriccion: Restriccion_la_emision_de_estas_certificaciones_solo_se_podra_realizar_una_vez_inhabilitado_
Restriccion: Restriccion_la_presente_reduccion_de_exigencia_regira_para_entidades_del_grupo_2_que_pertene
Restriccion: Restriccion_esta_reduccion_se_aplicara_respecto_de_las_entidades_que_cumplan_los_requisitos_
```

## S12 — detalle

```
Excepcion_a_los_efectos_de_la_determinacion_de_la_rpc_sobre_base_consolidada_la_entidad_qu
Excepcion_a_los_efectos_de_la_determinacion_de_la_rpc_se_podra_adicionar_el_importe_corres
Excepcion_los_creditos_para_consumo_o_vivienda_que_superen_el_equivalente_a_dos_veces_el_i
Excepcion_no_se_consideraran_dentro_de_ese_concepto_las_refinanciaciones_otorgadas_a_produ
Excepcion_no_se_consideraran_comprendidas_en_esas_definiciones_las_facilidades_adicionales
Excepcion_no_se_consideraran_comprendidas_en_esas_definiciones_las_renovaciones_periodicas
Excepcion_cuando_se_hayan_asignado_al_deudor_margenes_de_credito_por_lineas_de_prestamo_es
Excepcion_quedan_exceptuadas_las_importaciones_realizadas_por_empresas_que_presten_servici
```
