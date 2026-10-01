# U-PYD P2 — mediciones (ventana de la mención, reglas de comparación, largo del tramo)

Comando: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/pyd_r2/code/mediciones_p2.py`. Declaraciones D-VENT, D-COMP y D-LARGO en el docstring del script, fijadas antes de correr.

## 1. Ventana de la verificación por tokens

Población: 63 menciones (`sujeto_propuesto`, crudo L0 de diez; N1 63). Exactas 45 (N1 45); por tokens sin tope y no exactas 8 (N1 8). Coincide con N1: True. Semilla del chunk ajeno: 20261001.

| holgura h | propias aceptadas (de 63) | propias por tokens | ajenas aceptadas (de 63) | ajenas exactas | ajenas por tokens | todos los otros: aceptados | todos los otros: por tokens | pares (mención, otro chunk) |
|---|---|---|---|---|---|---|---|---|
| 0 | 45 | 0 | 6 | 6 | 0 | 2041 | 0 | 39076 |
| 1 | 47 | 2 | 6 | 6 | 0 | 2045 | 4 | 39076 |
| 2 | 48 | 3 | 6 | 6 | 0 | 2045 | 4 | 39076 |
| 3 | 48 | 3 | 6 | 6 | 0 | 2047 | 6 | 39076 |
| 4 | 49 | 4 | 8 | 6 | 2 | 2067 | 26 | 39076 |
| 5 | 49 | 4 | 8 | 6 | 2 | 2068 | 27 | 39076 |
| 6 | 49 | 4 | 8 | 6 | 2 | 2078 | 37 | 39076 |
| 8 | 49 | 4 | 8 | 6 | 2 | 2078 | 37 | 39076 |
| 10 | 49 | 4 | 8 | 6 | 2 | 2085 | 44 | 39076 |
| 15 | 49 | 4 | 8 | 6 | 2 | 2094 | 53 | 39076 |
| 20 | 50 | 5 | 8 | 6 | 2 | 2099 | 58 | 39076 |
| sin tope | 53 | 8 | 8 | 6 | 2 | 2152 | 111 | 39076 |

Menciones que verifican solo por tokens contra su propio chunk:

| chunk | relación | mención | holgura mínima | chunk ajeno | en el ajeno |
|---|---|---|---|---|---|
| cla::6.5.5.7 | 6 | administradores de carteras crediticias | 1 | cla::6.5.3.4 | None |
| ctacte::4.2.1 | 2 | Titular de cuenta corriente | 1 | ctacte::6.4.7.2 | None |
| ctacte::4.2.1 | 3 | Tenedor de cheque | 20 | ctacte::10.2.2.1 | None |
| ctacte::8.8.1.2 | 5 | personas inhabilitadas por decisión judicial o por motivos legales | 4 | ctacte::1.5.2.1 | None |
| ctacte::12.8.2 | 2 | Empresas administradoras de redes de cajeros automáticos | 2 | ctacte::10.2.1.2 | None |
| ext::2.6.2::intro | 4 | beneficiario de certificaciones de incremento de exportaciones | 93 | ext::3.16.3.4 | None |
| ext::3.17.2::intro | 5 | beneficiarios del Régimen de acceso a divisas para la producción incremental de petróleo (RADPIP) y/o gas natural (RADPIGN) | 114 | ext::7.9.5 | None |
| ext::10.4.2.7 | 7 | Organizaciones empresariales con participación mayoritaria del Estado Nacional | 26 | ext::8.4.3.3 | None |

## 2. Reglas de comparación sobre las ventanas de cuantía

Anclas del comando [c14] en el texto firmado: True.

| grafo | nodos con cuantía [c14] | sin campo | tablero (con, sin) | coincide | cuantías detectadas | nodos sin cuantía detectada | comparacion_asumida | no_determinada |
|---|---|---|---|---|---|---|---|---|
| r1 | 639 | 218 | [639, 218] | True | 757 | 1 | 173 | 152 |
| desarrollo | 606 | 287 | [606, 287] | True | 701 | 2 | 146 | 140 |
| cinco | 77 | 36 | [77, 36] | True | 82 | 5 | 18 | 5 |
| diez | 683 | 323 | [683, 323] | True | 783 | 7 | 164 | 145 |

### Frecuencia de cada forma — desarrollo

| regla | cuantías |
|---|---|
| sin_marcador_plazo | 146 |
| coeficiente | 141 |
| sin_marcador | 140 |
| compuesta:dentro_de | 72 |
| simple:raiz_super | 40 |
| negacion:raiz_super | 39 |
| compuesta:hasta | 25 |
| compuesta:adyacencia_minimo | 12 |
| compuesta:al_menos | 12 |
| compuesta:como_minimo | 12 |
| compuesta:igual_o_superior | 9 |
| negacion:inferior | 9 |
| simple:mayor | 8 |
| negacion:mayor | 6 |
| negacion:raiz_exced | 6 |
| simple:inferior | 6 |
| simple:mas_de | 6 |
| simple:raiz_exced | 4 |
| compuesta:adyacencia_maximo | 3 |
| negacion:mas_de | 2 |
| compuesta:un_minimo_de | 1 |
| negacion:menor | 1 |
| simple:menos_de | 1 |

| comparación | cuantías |
|---|---|
| maximo_inclusivo | 299 |
| coeficiente | 141 |
| no_determinada | 140 |
| minimo_estricto | 58 |
| minimo_inclusivo | 56 |
| maximo_estricto | 7 |

Candidatas para «igual» entre las cuantías sin marcador: sin_marcador:de_a_secas 51, sin_marcador:equivalente_a 12, sin_marcador:igual_a 2, sin_marcador:sera_de 2, sin_marcador_plazo:de_a_secas 51, sin_marcador_plazo:equivalente_a 1, sin_marcador_plazo:sera_de 6.

Formas no cubiertas entre las cuantías sin marcador: sin_marcador:entre 2, sin_marcador:limite 20, sin_marcador:maximo_no_adyacente 9, sin_marcador:mayor_menor_inferior_sin_a 3, sin_marcador:o_mas_pospuesto 7, sin_marcador:o_menos_pospuesto 2, sin_marcador:por_lo_menos 1, sin_marcador:tope 2, sin_marcador_plazo:entre 9, sin_marcador_plazo:maximo_no_adyacente 2, sin_marcador_plazo:mayor_menor_inferior_sin_a 3, sin_marcador_plazo:minimo_no_adyacente 4, sin_marcador_plazo:por_lo_menos 9.

### Frecuencia de cada forma — diez

| regla | cuantías |
|---|---|
| sin_marcador_plazo | 164 |
| sin_marcador | 145 |
| coeficiente | 141 |
| compuesta:dentro_de | 95 |
| simple:raiz_super | 49 |
| negacion:raiz_super | 44 |
| compuesta:hasta | 28 |
| compuesta:adyacencia_minimo | 18 |
| compuesta:al_menos | 13 |
| compuesta:como_minimo | 12 |
| negacion:raiz_exced | 10 |
| compuesta:igual_o_superior | 9 |
| negacion:inferior | 9 |
| simple:mayor | 8 |
| compuesta:adyacencia_maximo | 7 |
| simple:mas_de | 7 |
| negacion:mayor | 6 |
| simple:inferior | 6 |
| simple:raiz_exced | 4 |
| negacion:mas_de | 2 |
| negacion:menor | 2 |
| simple:menos_de | 2 |
| compuesta:como_maximo | 1 |
| compuesta:un_minimo_de | 1 |

| comparación | cuantías |
|---|---|
| maximo_inclusivo | 357 |
| no_determinada | 145 |
| coeficiente | 141 |
| minimo_estricto | 68 |
| minimo_inclusivo | 64 |
| maximo_estricto | 8 |

Candidatas para «igual» entre las cuantías sin marcador: sin_marcador:de_a_secas 54, sin_marcador:equivalente_a 14, sin_marcador:igual_a 2, sin_marcador:sera_de 2, sin_marcador_plazo:de_a_secas 58, sin_marcador_plazo:equivalente_a 1, sin_marcador_plazo:sera_de 7.

Formas no cubiertas entre las cuantías sin marcador: sin_marcador:entre 2, sin_marcador:limite 21, sin_marcador:maximo_no_adyacente 9, sin_marcador:mayor_menor_inferior_sin_a 3, sin_marcador:o_mas_pospuesto 7, sin_marcador:o_menos_pospuesto 2, sin_marcador:por_lo_menos 1, sin_marcador:tope 2, sin_marcador_plazo:entre 9, sin_marcador_plazo:maximo_no_adyacente 2, sin_marcador_plazo:mayor_menor_inferior_sin_a 6, sin_marcador_plazo:minimo_no_adyacente 5, sin_marcador_plazo:por_lo_menos 9.

### Frecuencia de cada forma — r1

| regla | cuantías |
|---|---|
| sin_marcador_plazo | 173 |
| sin_marcador | 152 |
| coeficiente | 140 |
| compuesta:dentro_de | 59 |
| compuesta:hasta | 46 |
| negacion:raiz_super | 42 |
| simple:raiz_super | 42 |
| compuesta:al_menos | 16 |
| compuesta:igual_o_superior | 12 |
| compuesta:como_minimo | 10 |
| negacion:mayor | 9 |
| simple:mas_de | 8 |
| simple:mayor | 8 |
| compuesta:adyacencia_minimo | 7 |
| negacion:raiz_exced | 7 |
| simple:raiz_exced | 6 |
| simple:inferior | 5 |
| compuesta:adyacencia_maximo | 4 |
| simple:menor | 3 |
| negacion:mas_de | 2 |
| negacion:menor | 2 |
| compuesta:como_maximo | 1 |
| compuesta:un_minimo_de | 1 |
| negacion:inferior | 1 |
| simple:menos_de | 1 |

| comparación | cuantías |
|---|---|
| maximo_inclusivo | 343 |
| no_determinada | 152 |
| coeficiente | 140 |
| minimo_estricto | 64 |
| minimo_inclusivo | 49 |
| maximo_estricto | 9 |

Candidatas para «igual» entre las cuantías sin marcador: sin_marcador:de_a_secas 50, sin_marcador:equivalente_a 14, sin_marcador:igual_a 5, sin_marcador:sera_de 4, sin_marcador_plazo:de_a_secas 65, sin_marcador_plazo:equivalente_a 2, sin_marcador_plazo:sera_de 5.

Formas no cubiertas entre las cuantías sin marcador: sin_marcador:entre 7, sin_marcador:limite 16, sin_marcador:maximo_no_adyacente 7, sin_marcador:mayor_menor_inferior_sin_a 6, sin_marcador:minimo_no_adyacente 1, sin_marcador:o_mas_pospuesto 5, sin_marcador:o_menos_pospuesto 2, sin_marcador:por_lo_menos 1, sin_marcador:tope 1, sin_marcador_plazo:entre 6, sin_marcador_plazo:maximo_no_adyacente 2, sin_marcador_plazo:mayor_menor_inferior_sin_a 1, sin_marcador_plazo:minimo_no_adyacente 5, sin_marcador_plazo:o_mas_pospuesto 1, sin_marcador_plazo:por_lo_menos 9.

### Fuente del marcador de coeficiente (A-COEF)

| grafo | fuente:palabra |
|---|---|
| r1 | descripcion:coefici 11, descripcion:factor 2, descripcion:pondera 26, titulo:factor 2, titulo:pondera 6, tramo:coefici 5, tramo:factor 1, tramo:pondera 87 |
| desarrollo | descripcion:factor 1, descripcion:pondera 34, titulo:pondera 4, tramo:coefici 2, tramo:factor 4, tramo:pondera 96 |
| cinco |  |
| diez | descripcion:factor 1, descripcion:pondera 34, titulo:pondera 4, tramo:coefici 2, tramo:factor 4, tramo:pondera 96 |

### Propuesta para «igual» (A-IGUAL) — diez: 13 cuantías sin marcador con «igual/equivalente a» adyacente, 6 sin motivo de exclusión; 2 con compuesta inversa

| forma | nodo | regla actual | cuantía | excluida por | ventana |
|---|---|---|---|---|---|
| igual | Condicion_deuda_por_importaciones_usd_500_000_o_menor_87bc52 | sin_marcador | USD 500.000 | compuesta_inversa | pago al 24/01/24 sea menor o igual al equivalente a USD 500.000 (dólares estadounidenses quinientos |
| igual | Condicion_financiaciones_equivalentes_a_5_o_mas_rpc_activo_2 | sin_marcador | 5 % | o_mas_o_menos_pospuesto | Clientes cuyas financiaciones comprendidas en algún momento sean equivalentes al 5 % o más de |
| igual | Condicion_monto_total_deuda_importaciones_menor_o_igual_usd_ | sin_marcador | USD 500.000 | compuesta_inversa | pendiente de pago sea menor o igual al equivalente a USD 500.000 (dólares estadounidenses quinientos |
| igual | Excepcion_si_es_necesario_llegar_al_50_de_cobertura_del_prim | sin_marcador | dos veces | — | o del activo del fideicomiso financiero, o del equivalente a dos veces el importe de |
| igual | Obligacion_a_partir_del_segundo_y_hasta_el_trigesimo_sexto_m | sin_marcador | 10% | — | el trigésimo sexto mes, la exigencia mensual será equivalente al 10% del promedio de |
| igual | Obligacion_en_el_curso_de_cada_trimestre_calendario_respecto | sin_marcador | 5 % | o_mas_o_menos_pospuesto | considerados cuyas financiaciones comprendidas en algún momento sean equivalentes al 5 % o más de |
| igual | Obligacion_la_deduccion_sera_equivalente_al_100_del_valor_de | sin_marcador | 100% | — | La deducción será equivalente al 100% del valor de |
| igual | Obligacion_la_exigencia_mensual_de_capital_minimo_por_riesgo | sin_marcador | 10% | — | 1 y 2 correspondiente al primer mes será equivalente al 10% de la sumatoria |
| igual | Restriccion_a_razon_de_un_maximo_mensual_equivalente_al_10_d | sin_marcador | 10% | maximo_minimo_tope_limite | a razón de un máximo mensual equivalente al 10% (diez por ciento) |
| igual | Restriccion_el_cliente_no_supere_en_el_mes_calendario_en_el_ | sin_marcador | USD 200 | — | por el conjunto de los conceptos señalados, el equivalente a USD 200 (dólares estadounidenses doscientos) |
| igual | Restriccion_el_monto_total_adeudado_a_la_fecha_de_cierre_del | sin_marcador | USD 500.000 | raiz_super_exced | de cierre del mencionado registro no superaba el equivalente a USD 500.000 (dólares estadounidenses quinientos |
| igual | Restriccion_limite_maximo_equivalente_a_usd_100_dolares_esta | sin_marcador | USD 100 | maximo_minimo_tope_limite | Límite máximo equivalente a USD 100 (dólares estadounidenses cien) |
| igual | Restriccion_multa_equivalente_al_4_del_valor_rechazado_con_m | sin_marcador | 4% | — | Multa equivalente al 4% del valor rechazado |
| inversa | Condicion_deuda_por_importaciones_usd_500_000_o_menor_87bc52 | sin_marcador | USD 500.000 | — | pago al 24/01/24 sea menor o igual al equivalente a USD 500.000 (dólares estadounidenses quinientos |
| inversa | Condicion_monto_total_deuda_importaciones_menor_o_igual_usd_ | sin_marcador | USD 500.000 | — | pendiente de pago sea menor o igual al equivalente a USD 500.000 (dólares estadounidenses quinientos |

Raíces «super-»/«exced-» no reconocidas en cuantías sin marcador (A-RAIZ): sin_marcador:superaba 2.

### Propuesta para «igual» (A-IGUAL) — r1: 17 cuantías sin marcador con «igual/equivalente a» adyacente, 7 sin motivo de exclusión; 5 con compuesta inversa

| forma | nodo | regla actual | cuantía | excluida por | ventana |
|---|---|---|---|---|---|
| igual | Obligacion_al_cierre_del_primer_semestre_calendario_el_exame | sin_marcador | dos veces | — | o del activo del fideicomiso financiero, o del equivalente a dos veces el importe de |
| igual | Obligacion_en_el_curso_de_cada_semestre_calendario_respecto_ | sin_marcador | dos veces | — |  –o el equivalente a dos veces el importe de |
| igual | Obligacion_en_el_curso_de_cada_trimestre_calendario_respecto | sin_marcador | 5 % | o_mas_o_menos_pospuesto | considerados cuyas financiaciones comprendidas en algún momento sean equivalentes al 5 % o más de |
| igual | Restriccion_a_partir_del_segundo_y_hasta_el_trigesimo_sexto_ | sin_marcador | 10% | — | el trigésimo sexto mes, la exigencia mensual será equivalente al 10% del promedio de |
| igual | Restriccion_a_razon_de_un_maximo_mensual_equivalente_al_10_d | sin_marcador | 10% | maximo_minimo_tope_limite | a razón de un máximo mensual equivalente al 10% (diez por ciento) |
| igual | Restriccion_capital_ordinario_de_nivel_1_con1_debe_ser_mayor | sin_marcador | 4,5 % | compuesta_inversa | de Nivel 1 (COn1) debe ser mayor o igual a 4,5 % sobre el total |
| igual | Restriccion_el_cliente_no_supere_en_el_mes_calendario_en_el_ | sin_marcador | USD 200 | — | por el conjunto de los conceptos señalados, el equivalente a USD 200 (dólares estadounidenses doscientos) |
| igual | Restriccion_el_monto_maximo_sera_el_que_resulte_menor_entre_ | sin_marcador | 30% | — | el aumento total del punto 3.18.2.1 y el equivalente al 30% (treinta por ciento) |
| igual | Restriccion_el_monto_total_adeudado_a_la_fecha_de_cierre_del | sin_marcador | USD 500.000 | raiz_super_exced | de cierre del mencionado registro no superaba el equivalente a USD 500.000 (dólares estadounidenses quinientos |
| igual | Restriccion_el_monto_total_de_sus_deudas_por_importaciones_d | sin_marcador | USD 500.000 | compuesta_inversa | al 24/01/24 deberá ser menor o igual al equivalente a USD 500.000 (dólares estadounidenses quinientos |
| igual | Restriccion_el_monto_total_de_sus_deudas_por_importaciones_d | sin_marcador | USD 500.000 | compuesta_inversa | pendiente de pago sea menor o igual al equivalente a USD 500.000 |
| igual | Restriccion_inmuebles_cualquiera_sea_la_fecha_de_su_incorpor | sin_marcador | 100 % | — |  La deducción será equivalente al 100 % del valor de |
| igual | Restriccion_la_exigencia_mensual_de_capital_minimo_por_riesg | sin_marcador | 10% | maximo_minimo_tope_limite | mínimo por riesgo operacional del primer mes será equivalente al 10% de la sumatoria |
| igual | Restriccion_la_exposicion_maxima_frente_a_una_misma_contrapa | sin_marcador | 75 veces | — |  el importe equivalente a 75 veces el Salario Mínimo, |
| igual | Restriccion_las_financiaciones_comprendidas_en_algun_momento | sin_marcador | 5 % | o_mas_o_menos_pospuesto | las financiaciones comprendidas en algún momento sean equivalentes al 5 % o más de |
| igual | Restriccion_patrimonio_neto_basico_pnb_debe_ser_mayor_o_igua | sin_marcador | 6 % | compuesta_inversa | Patrimonio Neto Básico (PNb) debe ser mayor o igual a 6 % sobre el total |
| igual | Restriccion_responsabilidad_patrimonial_computable_rpc_debe_ | sin_marcador | 8% | compuesta_inversa | Responsabilidad Patrimonial Computable (RPC) debe ser mayor o igual a 8% sobre el total |
| inversa | Restriccion_capital_ordinario_de_nivel_1_con1_debe_ser_mayor | sin_marcador | 4,5 % | — | de Nivel 1 (COn1) debe ser mayor o igual a 4,5 % sobre el total |
| inversa | Restriccion_el_monto_total_de_sus_deudas_por_importaciones_d | sin_marcador | USD 500.000 | — | al 24/01/24 deberá ser menor o igual al equivalente a USD 500.000 (dólares estadounidenses quinientos |
| inversa | Restriccion_el_monto_total_de_sus_deudas_por_importaciones_d | sin_marcador | USD 500.000 | — | pendiente de pago sea menor o igual al equivalente a USD 500.000 |
| inversa | Restriccion_patrimonio_neto_basico_pnb_debe_ser_mayor_o_igua | sin_marcador | 6 % | — | Patrimonio Neto Básico (PNb) debe ser mayor o igual a 6 % sobre el total |
| inversa | Restriccion_responsabilidad_patrimonial_computable_rpc_debe_ | sin_marcador | 8% | — | Responsabilidad Patrimonial Computable (RPC) debe ser mayor o igual a 8% sobre el total |

Raíces «super-»/«exced-» no reconocidas en cuantías sin marcador (A-RAIZ): sin_marcador:superaba 1.

### «factor» como marcador de coeficiente — diez (5 cuantías)

| nodo | tipo | fuente del marcador | cuantía | ventana |
|---|---|---|---|---|
| Condicion_no_conocer_factor_exposicion_potencial_futura_6946 | Condicion | tramo | 15% | determinar la exposición potencial futura, se empleará un factor de 15%, que es |
| Restriccion_el_importe_resultante_de_aplicar_lo_dispuesto_en | Restriccion | descripcion | 5% | un acopio de su producción por un valor superior al 5% de su capacidad |
| Restriccion_las_demas_posiciones_de_titulizacion_registradas | Restriccion | tramo | 100% | de balance recibirán un Factor de Conversión Crediticia (CCF) del 100% |
| Restriccion_las_facilidades_de_liquidez_por_parte_de_la_enti | Restriccion | tramo | 100% | de titulización recibirán un Factor de Conversión Crediticia (CCF) del 100% |
| Restriccion_los_anticipos_de_efectivo_por_parte_de_la_entida | Restriccion | tramo | 100% | de titulización recibirán un Factor de Conversión Crediticia (CCF) del 100% |

### «factor» como marcador de coeficiente — r1 (5 cuantías)

| nodo | tipo | fuente del marcador | cuantía | ventana |
|---|---|---|---|---|
| Excepcion_cuando_no_se_conozca_el_factor_a_aplicar_para_dete | Excepcion | tramo | 15% | determinar la exposición potencial futura, se empleará un factor de 15%, que es |
| Obligacion_cuando_la_contraprestacion_no_sea_recibida_en_el_ | Obligacion | descripcion | cinco días hábiles | Cuando la contraprestación no sea recibida en el plazo de cinco días hábiles desde la fecha |
| Obligacion_el_importe_resultante_de_aplicar_lo_dispuesto_en_ | Obligacion | descripcion | 5% | un acopio de su producción por un valor superior al 5% de su capacidad |
| Obligacion_las_demas_posiciones_de_titulizacion_registradas_ | Obligacion | titulo | 100 % | registradas en partidas fuera de balance recibirán un CCF del 100 % |
| Obligacion_las_facilidades_de_liquidez_y_de_anticipos_de_efe | Obligacion | titulo | 100 % | que actúa como agente de pago recibirán un CCF del 100 % |

## 3. Largo mínimo del tramo de las omisiones (provisional)

Chunks con omisión en el crudo L0 de diez: 80 (N1 80; coincide True). Criterio declarado: menor n con fracción de n-gramas únicos en su chunk ≥ 0.95, n de 1 a 10: None. Extensión posterior (A-LARGO), n hasta 40: 11. Tokens del texto propio: {'minimo': 3, 'mediana': 187, 'maximo': 4232}.

| n | posiciones | únicas en su chunk | fracción |
|---|---|---|---|
| 1 | 26611 | 5581 | 0.2097 |
| 2 | 26531 | 14666 | 0.5528 |
| 3 | 26451 | 19029 | 0.7194 |
| 4 | 26371 | 21162 | 0.8025 |
| 5 | 26292 | 22368 | 0.8508 |
| 6 | 26213 | 23145 | 0.883 |
| 7 | 26134 | 23656 | 0.9052 |
| 8 | 26055 | 24023 | 0.922 |
| 9 | 25976 | 24286 | 0.9349 |
| 10 | 25897 | 24482 | 0.9454 |
| 11 | 25819 | 24613 | 0.9533 |
| 12 | 25741 | 24704 | 0.9597 |
| 13 | 25663 | 24761 | 0.9649 |
| 14 | 25585 | 24802 | 0.9694 |
| 15 | 25507 | 24822 | 0.9731 |
| 16 | 25429 | 24832 | 0.9765 |
| 17 | 25351 | 24829 | 0.9794 |
| 18 | 25273 | 24814 | 0.9818 |
| 19 | 25195 | 24789 | 0.9839 |
| 20 | 25117 | 24756 | 0.9856 |
| 21 | 25040 | 24719 | 0.9872 |
| 22 | 24963 | 24673 | 0.9884 |
| 23 | 24886 | 24628 | 0.9896 |
| 24 | 24809 | 24583 | 0.9909 |
| 25 | 24733 | 24535 | 0.992 |
| 26 | 24657 | 24484 | 0.993 |
| 27 | 24581 | 24432 | 0.9939 |
| 28 | 24505 | 24378 | 0.9948 |
| 29 | 24429 | 24319 | 0.9955 |
| 30 | 24353 | 24260 | 0.9962 |
| 31 | 24277 | 24199 | 0.9968 |
| 32 | 24201 | 24135 | 0.9973 |
| 33 | 24126 | 24068 | 0.9976 |
| 34 | 24051 | 24001 | 0.9979 |
| 35 | 23976 | 23934 | 0.9982 |
| 36 | 23901 | 23865 | 0.9985 |
| 37 | 23826 | 23794 | 0.9987 |
| 38 | 23751 | 23723 | 0.9988 |
| 39 | 23676 | 23652 | 0.999 |
| 40 | 23602 | 23582 | 0.9992 |

