# Shapes v2 — kg_claude-haiku-4-5-20251001_r2.json

- Grafo: `../piloto/resultados/kg_claude-haiku-4-5-20251001_r2.json`
- Fecha: 2026-07-26
- Nodos: 246 | Aristas: 397

| Regla | Resultado | Resumen |
|---|---|---|
| S1 | PASS | 397/397 válidas; 0 violaciones. |
| S2 | PASS | 0 aristas colgantes sobre 397. |
| S3 | PASS | 397/397 conformes; 0 violaciones. |
| S4 | PASS | Nodos OK: 246/246. Aristas OK: 397/397. Violaciones: 0. |
| S5 | PASS | Nodos OK: 246/246. Aristas OK: 397/397. Violaciones: 0. |
| S6 | PASS | Conjunto válido: 5 TOs + esquema. Violaciones: 0. |
| S7 | PASS | 0 grupos violatorios (0 nodos). |
| S8 | WARN | 1 grupos cross-type. |
| S9 | PASS | 0 nodos con ambas keys. |
| S10 | PASS | Sin establecida_en: Obligacion=0, Restriccion=0, Excepcion=0 (total 0). |
| S11 | WARN | Sin aplica_a: Obligacion=6, Restriccion=7 (total 13). |
| S12 | FAIL | 1 Excepciones huérfanas. |
| S13 | PASS | 71/71 Sujetos con nivel válido; 0 violaciones. |

## S8 — detalle

```
'clasificacion de deudores': [TextoOrdenado] TextoOrdenado_to_clasificacion_deudores_actual_pdf, [Operacion] Operacion_clasificacion_de_deudor
```

## S11 — detalle

```
Obligacion: Obligacion_cuando_existan_obstaculos_para_la_rapida_repatriacion_de_beneficios_desde_una_su
Obligacion: Obligacion_consideracion_de_mora_al_terminar_emergencia
Obligacion: Obligacion_recibir_informacion_clara_suficiente_veraz_y_de_facil_acceso_y_visibilidad_acerc
Obligacion: Obligacion_los_usuarios_de_servicios_financieros_tienen_derecho_a_la_proteccion_de_su_segur
Obligacion: Obligacion_los_usuarios_de_servicios_financieros_tienen_derecho_a_la_libertad_de_eleccion_e
Obligacion: Obligacion_los_usuarios_de_servicios_financieros_tienen_derecho_a_condiciones_de_trato_equi
Restriccion: Restriccion_no_mejora_de_clasificacion_por_aplicacion_de_emergencia
Restriccion: Restriccion_el_pago_de_servicios_de_transporte_de_pasajeros_s03_solo_esta_permitido_para_acc
Restriccion: Restriccion_viajes_s06_excluye_operaciones_asociadas_a_retiros_y_o_consumos_con_tarjetas_de_
Restriccion: Restriccion_el_pago_de_fletes_s31_por_operaciones_de_exportacion_se_concreta_una_vez_que_la_
Restriccion: Restriccion_el_pago_de_fletes_s30_por_operaciones_de_importacion_se_concreta_a_partir_de_la_
Restriccion: Restriccion_aplicacion_de_exigencia_minima_cuando_n_0
Restriccion: Restriccion_limite_de_riesgo_de_tasa_interes
```

## S12 — detalle

```
Excepcion_no_sera_obligatoria_la_evaluacion_de_la_capacidad_de_pago_en_funcion_de_los_ingr
```
