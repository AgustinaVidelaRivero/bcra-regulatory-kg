# Shapes v2 — kg_claude-opus-4-5-20251101_r1.json

- Grafo: `../piloto/resultados/kg_claude-opus-4-5-20251101_r1.json`
- Fecha: 2026-07-26
- Nodos: 223 | Aristas: 370

| Regla | Resultado | Resumen |
|---|---|---|
| S1 | PASS | 370/370 válidas; 0 violaciones. |
| S2 | PASS | 0 aristas colgantes sobre 370. |
| S3 | PASS | 370/370 conformes; 0 violaciones. |
| S4 | PASS | Nodos OK: 223/223. Aristas OK: 370/370. Violaciones: 0. |
| S5 | PASS | Nodos OK: 223/223. Aristas OK: 370/370. Violaciones: 0. |
| S6 | PASS | Conjunto válido: 5 TOs + esquema. Violaciones: 0. |
| S7 | PASS | 0 grupos violatorios (0 nodos). |
| S8 | WARN | 1 grupos cross-type. |
| S9 | PASS | 0 nodos con ambas keys. |
| S10 | PASS | Sin establecida_en: Obligacion=0, Restriccion=0, Excepcion=0 (total 0). |
| S11 | PASS | Sin aplica_a: Obligacion=0, Restriccion=0 (total 0). |
| S12 | FAIL | 11 Excepciones huérfanas. |
| S13 | PASS | 74/74 Sujetos con nivel válido; 0 violaciones. |

## S8 — detalle

```
'clasificacion de deudores': [TextoOrdenado] TextoOrdenado_to_clasificacion_deudores_actual_pdf, [Operacion] Operacion_clasificacion
```

## S12 — detalle

```
Excepcion_los_creditos_para_consumo_o_vivienda_estan_excluidos_de_la_cartera_comercial
Excepcion_no_se_consideraran_dentro_de_ese_concepto_las_refinanciaciones_otorgadas_a_produ
Excepcion_a_fin_de_verificar_el_cumplimiento_de_las_obligaciones_de_naturaleza_comercial_c
Excepcion_quedan_exceptuadas_las_importaciones_realizadas_por_empresas_que_presten_servici
Excepcion_el_pago_corresponde_a_una_operacion_que_encuadra_en_los_codigos_de_concepto_s03_
Excepcion_los_gastos_que_abonen_las_entidades_al_exterior_por_su_operatoria_habitual
Excepcion_el_pago_corresponde_a_s31_servicios_de_fletes_por_operaciones_de_exportaciones_d
Excepcion_el_pago_corresponde_a_s30_servicios_de_fletes_por_operaciones_de_importaciones_d
Excepcion_el_pago_corresponde_a_s24_otros_servicios_personales_culturales_y_recreativos_pr
Excepcion_servicio_no_comprendido_en_13_2_1_a_13_2_5_provisto_por_contraparte_no_vinculada
Excepcion_excepto_que_se_trate_de_asociaciones_mutuales_o_cooperativas_por_las_financiacio
```
