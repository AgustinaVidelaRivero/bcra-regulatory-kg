# Shapes v2 — kg_claude-sonnet-4-5-20250929_r2.json

- Grafo: `../piloto/resultados/kg_claude-sonnet-4-5-20250929_r2.json`
- Fecha: 2026-07-26
- Nodos: 242 | Aristas: 396

| Regla | Resultado | Resumen |
|---|---|---|
| S1 | PASS | 396/396 válidas; 0 violaciones. |
| S2 | PASS | 0 aristas colgantes sobre 396. |
| S3 | PASS | 396/396 conformes; 0 violaciones. |
| S4 | PASS | Nodos OK: 242/242. Aristas OK: 396/396. Violaciones: 0. |
| S5 | PASS | Nodos OK: 242/242. Aristas OK: 396/396. Violaciones: 0. |
| S6 | PASS | Conjunto válido: 5 TOs + esquema. Violaciones: 0. |
| S7 | FAIL | 1 grupos violatorios (2 nodos). |
| S8 | WARN | 1 grupos cross-type. |
| S9 | PASS | 0 nodos con ambas keys. |
| S10 | PASS | Sin establecida_en: Obligacion=0, Restriccion=0, Excepcion=0 (total 0). |
| S11 | WARN | Sin aplica_a: Obligacion=1, Restriccion=8 (total 9). |
| S12 | FAIL | 2 Excepciones huérfanas. |
| S13 | PASS | 73/73 Sujetos con nivel válido; 0 violaciones. |

## S7 — detalle

```
[Operacion] 'clasificacion de deudores' (2 nodos): Operacion_clasificacion_deudores, Operacion_clasificacion
```

## S8 — detalle

```
'clasificacion de deudores': [TextoOrdenado] TextoOrdenado_to_clasificacion_deudores_actual_pdf, [Operacion] Operacion_clasificacion_deudores, [Operacion] Operacion_clasificacion
```

## S11 — detalle

```
Obligacion: Obligacion_en_todas_las_operaciones_de_cambio_canje_y_o_arbitraje_que_se_cursen_por_el_merc
Restriccion: Restriccion_los_creditos_de_esta_clase_que_superen_el_equivalente_a_dos_veces_el_importe_de_
Restriccion: Restriccion_el_pago_debe_corresponder_a_una_operacion_que_encuadra_en_codigos_de_concepto_es
Restriccion: Restriccion_el_pago_de_servicios_prestados_por_contraparte_vinculada_al_residente_punto_13_2
Restriccion: Restriccion_el_pago_de_servicios_prestados_por_contraparte_vinculada_al_residente_debe_concr
Restriccion: Restriccion_el_pago_de_fletes_de_exportacion_s31_en_que_los_fletes_forman_parte_de_la_condic
Restriccion: Restriccion_el_pago_de_fletes_de_importacion_s30_debe_concretarse_a_partir_de_la_fecha_de_pr
Restriccion: Restriccion_los_servicios_encuadrados_en_concepto_s24_prestados_por_contraparte_vinculada_pu
Restriccion: Restriccion_las_operaciones_originadas_en_servicios_por_contrapartes_vinculadas_continuan_al
```

## S12 — detalle

```
Excepcion_los_creditos_para_consumo_o_vivienda_se_exceptuan_de_la_cartera_comercial
Excepcion_quedan_exceptuadas_las_importaciones_realizadas_por_empresas_que_presten_servici
```
