# U-PYD P3 — transiciones por la calibración

Comando: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/pyd_r2/code/transiciones_p3.py`.

Reglas de P2: `data/experiment/pyd_r2/code/reglas_comparacion.py` en `b706d37` (sha256 `213ab140aa29…`), ejecutadas en memoria.

## 1. Comparación de las cuantías ([c14], descripciones de los grafos)

| grafo | nodos | cuantías | cambian de comparación | cambian solo de regla | comparacion_asumida antes | después |
|---|---|---|---|---|---|---|
| r1 | 639 | 757 | 29 | 1 | 173 | 164 |
| desarrollo | 606 | 701 | 27 | 2 | 146 | 137 |
| cinco | 77 | 82 | 1 | 0 | 18 | 18 |
| diez | 683 | 783 | 28 | 2 | 164 | 155 |

### r1: hacia dónde

| comparación P2 | comparación P3 | cuantías |
|---|---|---|
| maximo_inclusivo | minimo_inclusivo | 10 |
| no_determinada | minimo_inclusivo | 9 |
| no_determinada | maximo_inclusivo | 5 |
| no_determinada | igual | 3 |
| coeficiente | maximo_inclusivo | 1 |
| coeficiente | minimo_estricto | 1 |
| maximo_inclusivo | maximo_inclusivo | 1 |

| regla P2 | regla P3 | cuantías |
|---|---|---|
| sin_marcador_plazo | compuesta:por_lo_menos | 9 |
| sin_marcador | compuesta:o_mas | 5 |
| sin_marcador | compuesta:mayor_o_igual | 3 |
| sin_marcador | igual:equivalente_a | 3 |
| sin_marcador | compuesta:menor_o_igual | 2 |
| sin_marcador | compuesta:o_menos | 2 |
| coeficiente | simple:raiz_super | 1 |
| coeficiente | sin_marcador_plazo | 1 |
| compuesta:hasta | negacion:raiz_super | 1 |
| sin_marcador | compuesta:por_lo_menos | 1 |
| sin_marcador | negacion:raiz_super | 1 |
| sin_marcador_plazo | compuesta:o_mas | 1 |

### desarrollo: hacia dónde

| comparación P2 | comparación P3 | cuantías |
|---|---|---|
| maximo_inclusivo | minimo_inclusivo | 9 |
| no_determinada | minimo_inclusivo | 8 |
| no_determinada | maximo_inclusivo | 6 |
| no_determinada | igual | 3 |
| maximo_inclusivo | maximo_inclusivo | 2 |
| coeficiente | minimo_estricto | 1 |

| regla P2 | regla P3 | cuantías |
|---|---|---|
| sin_marcador_plazo | compuesta:por_lo_menos | 9 |
| sin_marcador | compuesta:o_mas | 7 |
| sin_marcador | igual:equivalente_a | 3 |
| compuesta:hasta | negacion:raiz_super | 2 |
| sin_marcador | compuesta:menor_o_igual | 2 |
| sin_marcador | compuesta:o_menos | 2 |
| sin_marcador | negacion:raiz_super | 2 |
| coeficiente | simple:raiz_super | 1 |
| sin_marcador | compuesta:por_lo_menos | 1 |

### cinco: hacia dónde

| comparación P2 | comparación P3 | cuantías |
|---|---|---|
| no_determinada | igual | 1 |

| regla P2 | regla P3 | cuantías |
|---|---|---|
| sin_marcador | igual:equivalente_a | 1 |

### diez: hacia dónde

| comparación P2 | comparación P3 | cuantías |
|---|---|---|
| maximo_inclusivo | minimo_inclusivo | 9 |
| no_determinada | minimo_inclusivo | 8 |
| no_determinada | maximo_inclusivo | 6 |
| no_determinada | igual | 4 |
| maximo_inclusivo | maximo_inclusivo | 2 |
| coeficiente | minimo_estricto | 1 |

| regla P2 | regla P3 | cuantías |
|---|---|---|
| sin_marcador_plazo | compuesta:por_lo_menos | 9 |
| sin_marcador | compuesta:o_mas | 7 |
| sin_marcador | igual:equivalente_a | 4 |
| compuesta:hasta | negacion:raiz_super | 2 |
| sin_marcador | compuesta:menor_o_igual | 2 |
| sin_marcador | compuesta:o_menos | 2 |
| sin_marcador | negacion:raiz_super | 2 |
| coeficiente | simple:raiz_super | 1 |
| sin_marcador | compuesta:por_lo_menos | 1 |

### diez: cuantías que cambian

| nodo | cuantía | P2 | P3 | ventana |
|---|---|---|---|---|
| Condicion_credito_adicional_no_cancelado_en_refinanciacion_3 | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | la obligación de permanecer en esta categoría por lo menos 180 días |
| Condicion_deuda_por_importaciones_usd_500_000_o_menor_87bc52 | USD 500.000 | no_determinada / sin_marcador | maximo_inclusivo / compuesta:menor_o_igual | pago al 24/01/24 sea menor o igual al equivalente a USD 500.000 (dólares estadounidenses quinientos |
| Condicion_deudas_comerciales_previas_declaradas_y_bajo_limit | USD 500.000 | no_determinada / sin_marcador | maximo_inclusivo / negacion:raiz_super | Proveedores del Exterior y el monto total adeudado no superaba USD 500.000 |
| Condicion_discrepancia_1_nivel_con_2_acreedores_inferiores_6 | 20 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:por_lo_menos | aquella, cuyas acreencias en conjunto representen por lo menos el 20 % y sean inferiores |
| Condicion_discrepancia_1_nivel_y_40_minimo_57c289 | 40 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:o_mas | la asignada por aquella, cuyas acreencias —en conjunto— representen el 40 % o más del |
| Condicion_discrepancia_de_mas_de_un_nivel_entre_clasificacio | 40 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:o_mas | de 'sistema cerrado' en categorías inferiores, cuyas acreencias representen el 40 % o más del |
| Condicion_financiaciones_equivalentes_a_5_o_mas_rpc_activo_2 | 5 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:o_mas | Clientes cuyas financiaciones comprendidas en algún momento sean equivalentes al 5 % o más de |
| Condicion_monto_capital_mercado_cambios_hasta_31_12_23_no_su | 40% | maximo_inclusivo / compuesta:hasta | maximo_inclusivo / negacion:raiz_super | al mercado de cambios hasta el 31/12/23 no superó el 40% (cuarenta por ciento) |
| Condicion_monto_total_deuda_importaciones_menor_o_igual_usd_ | USD 500.000 | no_determinada / sin_marcador | maximo_inclusivo / compuesta:menor_o_igual | pendiente de pago sea menor o igual al equivalente a USD 500.000 (dólares estadounidenses quinientos |
| Condicion_saldo_subyacente_10_valor_original_35ae14 | 10 % | no_determinada / sin_marcador | maximo_inclusivo / compuesta:o_menos | Sólo pueda ejercerse cuando quede pendiente un 10 % o menos del |
| Obligacion_a_los_efectos_previstos_en_los_dos_ultimos_parraf | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | sido cancelada, deberán permanecer en esta categoría por lo menos 180 días, contados desde |
| Obligacion_a_partir_del_segundo_y_hasta_el_trigesimo_sexto_m | 10% | no_determinada / sin_marcador | igual / igual:equivalente_a | el trigésimo sexto mes, la exigencia mensual será equivalente al 10% del promedio de |
| Obligacion_el_deudor_que_encontrandose_clasificado_en_esta_c | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Obligacion_el_deudor_que_encontrandose_clasificado_en_esta_c | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Obligacion_el_deudor_que_encontrandose_clasificado_en_esta_c | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | crédito adicional, deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Obligacion_en_caso_de_que_se_desconozca_la_situacion_de_cump | 5% | no_determinada / sin_marcador | maximo_inclusivo / compuesta:o_menos | de que se desconozca la situación de cumplimiento correspondiente al 5% o menos de |
| Obligacion_en_el_curso_de_cada_trimestre_calendario_respecto | 5 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:o_mas | considerados cuyas financiaciones comprendidas en algún momento sean equivalentes al 5 % o más de |
| Obligacion_la_deduccion_sera_equivalente_al_100_del_valor_de | 100% | no_determinada / sin_marcador | igual / igual:equivalente_a | La deducción será equivalente al 100% del valor de |
| Obligacion_la_exigencia_mensual_de_capital_minimo_por_riesgo | 10% | no_determinada / sin_marcador | igual / igual:equivalente_a | 1 y 2 correspondiente al primer mes será equivalente al 10% de la sumatoria |
| Obligacion_la_recategorizacion_del_deudor_se_efectuara_al_me | 40 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:o_mas | aquel conjunto de entidades y fideicomisos financieros que representen el 40 % o más del |
| Obligacion_se_debera_recategorizar_al_deudor_cuando_exista_u | 40 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:o_mas | la asignada por aquella, cuyas acreencias —en conjunto— representen el 40 % o más del |
| Obligacion_se_debera_recategorizar_al_deudor_cuando_exista_u | 40 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:o_mas | la asignada por aquella, cuyas acreencias –en conjunto– representen el 40 % o más del |
| Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_ | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_ | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_ | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_ | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Restriccion_el_importe_resultante_de_aplicar_lo_dispuesto_en | 5% | coeficiente / coeficiente | minimo_estricto / simple:raiz_super | un acopio de su producción por un valor superior al 5% de su capacidad |
| Restriccion_el_monto_de_capital_por_el_cual_se_accedio_al_me | 40% | maximo_inclusivo / compuesta:hasta | maximo_inclusivo / negacion:raiz_super | al mercado de cambios hasta el 31/12/23 no superó el 40% (cuarenta por ciento) |
| Restriccion_el_monto_total_adeudado_a_la_fecha_de_cierre_del | USD 500.000 | no_determinada / sin_marcador | maximo_inclusivo / negacion:raiz_super | de cierre del mencionado registro no superaba el equivalente a USD 500.000 (dólares estadounidenses quinientos |
| Restriccion_multa_equivalente_al_4_del_valor_rechazado_con_m | 4% | no_determinada / sin_marcador | igual / igual:equivalente_a | Multa equivalente al 4% del valor rechazado |

### r1: cuantías que cambian

| nodo | cuantía | P2 | P3 | ventana |
|---|---|---|---|---|
| Obligacion_a_los_efectos_previstos_en_los_dos_ultimos_parraf | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | sido cancelada, deberán permanecer en esta categoría por lo menos 180 días, contados desde |
| Obligacion_cuando_exista_una_discrepancia_de_mas_de_un_nivel | 20 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:por_lo_menos | aquella, cuyas acreencias en conjunto representen por lo menos el 20 % y sean inferiores |
| Obligacion_cuando_la_contraprestacion_no_sea_recibida_en_el_ | cinco días hábiles | coeficiente / coeficiente | maximo_inclusivo / sin_marcador_plazo | Cuando la contraprestación no sea recibida en el plazo de cinco días hábiles desde la fecha |
| Obligacion_el_deudor_que_encontrandose_clasificado_en_esta_c | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Obligacion_el_deudor_que_haya_refinanciado_su_deuda_y_recibi | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | punto 2.2.5 deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Obligacion_el_importe_resultante_de_aplicar_lo_dispuesto_en_ | 5% | coeficiente / coeficiente | minimo_estricto / simple:raiz_super | un acopio de su producción por un valor superior al 5% de su capacidad |
| Obligacion_en_caso_de_que_se_desconozca_la_situacion_de_cump | 5 % | no_determinada / sin_marcador | maximo_inclusivo / compuesta:o_menos | de que se desconozca la situación de cumplimiento correspondiente al 5 % o menos de |
| Obligacion_en_el_curso_de_cada_trimestre_calendario_respecto | 5 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:o_mas | considerados cuyas financiaciones comprendidas en algún momento sean equivalentes al 5 % o más de |
| Obligacion_se_debera_recategorizar_al_deudor_cuando_exista_u | 40 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:o_mas | la asignada por aquella, cuyas acreencias –en conjunto– representen el 40 % o más del |
| Obligacion_se_debera_recategorizar_al_deudor_cuando_exista_u | 40 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:o_mas | la asignada por aquella, cuyas acreencias –en conjunto– representen el 40 % o más del |
| Restriccion_a_partir_del_segundo_y_hasta_el_trigesimo_sexto_ | 10% | no_determinada / sin_marcador | igual / igual:equivalente_a | el trigésimo sexto mes, la exigencia mensual será equivalente al 10% del promedio de |
| Restriccion_capital_ordinario_de_nivel_1_con1_debe_ser_mayor | 4,5 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:mayor_o_igual | de Nivel 1 (COn1) debe ser mayor o igual a 4,5 % sobre el total |
| Restriccion_debera_permanecer_en_esta_categoria_por_lo_menos | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | Deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Restriccion_el_deudor_clasificado_en_esta_categoria_que_haya | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_ | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_ | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_ | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_ | 180 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:por_lo_menos | sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la |
| Restriccion_el_monto_de_capital_por_el_cual_se_accedio_al_me | 40% | maximo_inclusivo / compuesta:hasta | maximo_inclusivo / negacion:raiz_super | al mercado de cambios hasta el 31/12/23 no superó el 40% (cuarenta por ciento) |
| Restriccion_el_monto_total_adeudado_a_la_fecha_de_cierre_del | USD 500.000 | no_determinada / sin_marcador | maximo_inclusivo / negacion:raiz_super | de cierre del mencionado registro no superaba el equivalente a USD 500.000 (dólares estadounidenses quinientos |
| Restriccion_el_monto_total_de_sus_deudas_por_importaciones_d | USD 500.000 | no_determinada / sin_marcador | maximo_inclusivo / compuesta:menor_o_igual | al 24/01/24 deberá ser menor o igual al equivalente a USD 500.000 (dólares estadounidenses quinientos |
| Restriccion_el_monto_total_de_sus_deudas_por_importaciones_d | USD 500.000 | no_determinada / sin_marcador | maximo_inclusivo / compuesta:menor_o_igual | pendiente de pago sea menor o igual al equivalente a USD 500.000 |
| Restriccion_inmuebles_cualquiera_sea_la_fecha_de_su_incorpor | 100 % | no_determinada / sin_marcador | igual / igual:equivalente_a |  La deducción será equivalente al 100 % del valor de |
| Restriccion_la_exposicion_maxima_frente_a_una_misma_contrapa | 75 veces | no_determinada / sin_marcador | igual / igual:equivalente_a |  el importe equivalente a 75 veces el Salario Mínimo, |
| Restriccion_la_recategorizacion_del_deudor_se_efectuara_al_m | 40 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:o_mas | aquel conjunto de entidades y fideicomisos financieros que representen el 40 % o más del |
| Restriccion_las_financiaciones_comprendidas_en_algun_momento | 5 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:o_mas | las financiaciones comprendidas en algún momento sean equivalentes al 5 % o más de |
| Restriccion_patrimonio_neto_basico_pnb_debe_ser_mayor_o_igua | 6 % | no_determinada / sin_marcador | minimo_inclusivo / compuesta:mayor_o_igual | Patrimonio Neto Básico (PNb) debe ser mayor o igual a 6 % sobre el total |
| Restriccion_responsabilidad_patrimonial_computable_rpc_debe_ | 8% | no_determinada / sin_marcador | minimo_inclusivo / compuesta:mayor_o_igual | Responsabilidad Patrimonial Computable (RPC) debe ser mayor o igual a 8% sobre el total |
| Restriccion_se_consideran_en_mora_a_las_exposiciones_subyace | 90 días | maximo_inclusivo / sin_marcador_plazo | minimo_inclusivo / compuesta:o_mas | exposiciones subyacentes cuando se verifiquen atrasos en los pagos de 90 días o más, estén |
| Restriccion_solo_pueda_ejercerse_cuando_quede_pendiente_un_1 | 10 % | no_determinada / sin_marcador | maximo_inclusivo / compuesta:o_menos | Sólo pueda ejercerse cuando quede pendiente un 10 % o menos del |

## 2. Validador sobre el crudo (prueba_crudo_t0.json, P2 contra P3)

Política: P2 `e0c81cff7710…`, P3 `82e8752aea1d…`.

| grupo|capa | campo | clave | P2 | P3 |
|---|---|---|---|---|
| r1|L0 | sujeto_mencion | no | 5 | 6 |
| r1|L0 | sujeto_mencion | tokens | 5 | 4 |
| r1|L0 | pendientes_no_mapeados | mencion_no_verificada | 5 | 6 |
| r1|L0r | sujeto_mencion | no | 7 | 8 |
| r1|L0r | sujeto_mencion | tokens | 2 | 1 |
| r1|L0r | pendientes_no_mapeados | mencion_no_verificada | 7 | 8 |
| cinco|L0 | sujeto_mencion | no | 3 | 4 |
| cinco|L0 | sujeto_mencion | tokens | 2 | 1 |
| cinco|L0 | pendientes_no_mapeados | mencion_no_verificada | 3 | 4 |
| diez|L0 | sujeto_mencion | no | 13 | 14 |
| diez|L0 | sujeto_mencion | tokens | 3 | 2 |
| diez|L0 | pendientes_no_mapeados | mencion_no_verificada | 12 | 13 |

Controles en P3: c1_todos_iguales_a_n1 = True, reconciliacion_filas_n1_que_cierran = [78, 78], c2_A_coincide = True, c2_B_coincide = True, c3_perdidos = 0, c3_omisiones_v3_contra_r2 = {'r1|L0r': [36, 37]}, c4_coincide = True.

