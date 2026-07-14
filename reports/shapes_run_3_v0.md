# Validador de shapes v0 — capas 1 y 2

- **Grafo:** `/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/run_3_ppf_core/kg.json`
- **Fecha:** 2026-07-14
- **Nodos:** 4050
- **Aristas:** 6634

## S1 — PASS

Toda arista usa una de las 12 relaciones del esquema (nombre normalizado).

**Resultado:** 6634/6634 aristas con relación válida; 0 violaciones.

Sin violaciones.

## S2 — PASS

Integridad referencial: origen y destino de toda arista existen como nodos.

**Resultado:** 0 aristas colgantes sobre 6634.

Sin violaciones.

## S3 — PASS

Toda arista respeta la matriz de firmas dominio -> rango declarada en FIRMAS.

**Resultado:** 6634/6634 aristas conformes a firma; 0 violaciones.

Sin violaciones.

## S4 — PASS

Todo nodo y toda arista tienen provenance dict con exactamente source_doc y location, strings no vacías.

**Resultado:** Nodos OK: 4050/4050. Aristas OK: 6634/6634. Violaciones: 0.

Sin violaciones.

## S5 — PASS

Todo location (de nodo y de arista) contiene 'punto' (normalizado).

**Resultado:** Nodos con 'punto': 4050/4050. Aristas: 6634/6634. Violaciones: 0.

Sin violaciones.

## S6 — PASS

Todo source_doc pertenece al conjunto de valores de 'archivo' de los nodos TextoOrdenado.

**Resultado:** Archivos válidos (5): ['TO_capitales_minimos_actual.pdf', 'TO_clasificacion_deudores_actual.pdf', 'TO_exterior_cambios_actual.pdf', 'TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'TO_regimen_informativo_contable_mensual_actual.pdf']. Violaciones: 0.

Sin violaciones.

## S7 — FAIL

ERROR — Unicidad exacta: no puede haber dos nodos con el mismo (type, label normalizado).

**Resultado:** 48 grupos violatorios (103 nodos involucrados).

```
[Excepcion] 'excepcion vpu rigi' (2 nodos):
    - Excepcion_no_aplica_si_el_cliente_es_un_vehiculo_de_proyecto_unico_vpu_adherido_al_rigi_qu  (label: 'Excepción VPU RIGI')
    - Excepcion_no_resultara_aplicable_cuando_el_cliente_es_un_vehiculo_de_proyecto_unico_vpu_ad  (label: 'Excepción VPU RIGI')
[Obligacion] 'archivar documentacion' (2 nodos):
    - Obligacion_archivar_documentacion  (label: 'Archivar documentación')
    - Obligacion_archivar_a_disposicion_del_bcra_toda_la_documentacion_utilizada_en_el_marco_del_  (label: 'Archivar documentación')
[Obligacion] 'boleto de venta de cambio' (2 nodos):
    - Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_importador_  (label: 'Boleto de venta de cambio')
    - Obligacion_boleto_de_venta_de_cambio  (label: 'Boleto de venta de cambio')
[Obligacion] 'calcular exposicion riesgo credito contraparte' (2 nodos):
    - Obligacion_la_exposicion_al_riesgo_de_credito_de_contraparte_ead_se_calculara_por_separado_  (label: 'Calcular exposición riesgo crédito contraparte')
    - Obligacion_calcular_exposicion_riesgo_credito_contraparte  (label: 'Calcular exposición riesgo crédito contraparte')
[Obligacion] 'certificacion de liquidacion en mercado de cambios' (2 nodos):
    - Obligacion_certificacion_de_liquidacion_en_mercado_de_cambios  (label: 'Certificación de liquidación en mercado de cambios')
    - Obligacion_en_caso_de_que_los_montos_hayan_sido_percibidos_en_moneda_extranjera_en_el_pais_  (label: 'Certificación de liquidación en mercado de cambios')
[Obligacion] 'declaracion jurada de caracter genuino' (2 nodos):
    - Obligacion_declaracion_jurada_de_caracter_genuino  (label: 'Declaración jurada de carácter genuino')
    - Obligacion_por_el_valor_de_los_descuentos_y_gastos_de_servicios_pagaderos_en_el_exterior_qu  (label: 'Declaración jurada de carácter genuino')
[Obligacion] 'declaracion jurada del exportador' (2 nodos):
    - Obligacion_declaracion_jurada_del_exportador  (label: 'Declaración jurada del exportador')
    - Obligacion_la_entidad_debe_contar_con_una_declaracion_jurada_del_exportador_en_la_que_se_de  (label: 'Declaración jurada del exportador')
[Obligacion] 'demostrar registro ingreso aduanero' (2 nodos):
    - Obligacion_demostrar_registro_ingreso_aduanero  (label: 'Demostrar registro ingreso aduanero')
    - Obligacion_el_requisito_de_ingreso_y_liquidacion_de_las_divisas_se_considerara_cumplimentad  (label: 'Demostrar registro ingreso aduanero')
[Obligacion] 'obtener conformidad previa bcra' (2 nodos):
    - Obligacion_obtener_conformidad_previa_bcra  (label: 'Obtener conformidad previa BCRA')
    - Obligacion_obtener_conformidad_previa_del_bcra_para_acceso_al_mercado_de_cambios_con_anteri  (label: 'Obtener conformidad previa BCRA')
[Obligacion] 'realizar boleto de cambio' (2 nodos):
    - Obligacion_realizar_boleto_de_cambio  (label: 'Realizar boleto de cambio')
    - Obligacion_la_entidad_debera_realizar_un_boleto_de_compra_y_o_venta_de_cambio_conforme_a_lo  (label: 'Realizar boleto de cambio')
[Obligacion] 'valuacion diaria a precios de mercado' (2 nodos):
    - Obligacion_valuacion_diaria_a_precios_de_mercado  (label: 'Valuación diaria a precios de mercado')
    - Obligacion_las_posiciones_se_valuan_a_precios_de_mercado_al_menos_diariamente_y_en_el_caso_  (label: 'Valuación diaria a precios de mercado')
[Operacion] 'acceso al mercado de cambios' (5 nodos):
    - Operacion_acceso_al_mercado_de_cambios  (label: 'Acceso al mercado de cambios')
    - Operacion_acceso_a_mercado_de_cambios  (label: 'Acceso al mercado de cambios')
    - Operacion_acceso_al_mercado_de_cambios_para_pago_exterior  (label: 'Acceso al mercado de cambios')
    - Operacion_acceso_a_mercado_de_cambios_para_cancelacion_de_lineas_de_credito  (label: 'Acceso al mercado de cambios')
    - Operacion_acceso_a_mercado_de_cambios_para_operaciones_de_egreso  (label: 'Acceso al mercado de cambios')
[Operacion] 'asuncion de riesgo de cambio' (2 nodos):
    - Operacion_asuncion_de_riesgo_de_cambio  (label: 'Asunción de riesgo de cambio')
    - Operacion_asuncion_de_riesgo  (label: 'Asunción de riesgo de cambio')
[Operacion] 'boleto de venta de cambio' (2 nodos):
    - Operacion_boleto_de_cambio  (label: 'Boleto de venta de cambio')
    - Operacion_registro_cambio  (label: 'Boleto de venta de cambio')
[Operacion] 'calculo de exigencia de capital' (2 nodos):
    - Operacion_calculo_de_capital  (label: 'Cálculo de exigencia de capital')
    - Operacion_calculo_de_exigencia  (label: 'Cálculo de exigencia de capital')
[Operacion] 'cancelacion de capital e intereses' (3 nodos):
    - Operacion_cancelacion_de_endeudamientos_financieros  (label: 'Cancelación de capital e intereses')
    - Operacion_cancelacion_de_deuda_financiera  (label: 'Cancelación de capital e intereses')
    - Operacion_cancelacion_de_deuda  (label: 'Cancelación de capital e intereses')
[Operacion] 'cancelacion de garantias comerciales' (2 nodos):
    - Operacion_cancelacion_de_garantia  (label: 'Cancelación de garantías comerciales')
    - Operacion_cancelacion_de_cartas_de_credito_o_letras_avaladas  (label: 'Cancelación de garantías comerciales')
[Operacion] 'cancelacion de lineas de credito' (2 nodos):
    - Operacion_cancelacion_de_lineas_de_credito_del_exterior  (label: 'Cancelación de líneas de crédito')
    - Operacion_cancelacion_de_linea_de_credito_del_exterior  (label: 'Cancelación de líneas de crédito')
[Operacion] 'clasificacion de deudor' (2 nodos):
    - Operacion_clasificacion_de_deudor_en_categoria  (label: 'Clasificación de deudor')
    - Operacion_clasificacion_de_deudor_segun_mora  (label: 'Clasificación de deudor')
[Operacion] 'cobro de comisiones y cargos' (2 nodos):
    - Operacion_cobro_de_comisiones_y_cargos  (label: 'Cobro de comisiones y cargos')
    - Operacion_cobro_de_comisiones_y_cargos_a_usuarios  (label: 'Cobro de comisiones y cargos')
[Operacion] 'compra de moneda extranjera' (2 nodos):
    - Operacion_compra_de_moneda_extranjera  (label: 'Compra de moneda extranjera')
    - Operacion_compra_de_moneda_extranjera_para_constituir_garantias  (label: 'Compra de moneda extranjera')
[Operacion] 'compras de bienes al exterior' (2 nodos):
    - Operacion_compra_de_bienes_en_el_exterior  (label: 'Compras de bienes al exterior')
    - Operacion_compra_de_bienes  (label: 'Compras de bienes al exterior')
[Operacion] 'derivados de credito' (2 nodos):
    - Operacion_derivados_de_credito  (label: 'Derivados de crédito')
    - Operacion_derivado_de_credito  (label: 'Derivados de crédito')
[Operacion] 'descalce de monedas' (2 nodos):
    - Operacion_operacion_con_divisa  (label: 'Descalce de monedas')
    - Operacion_descalce_de_monedas_entre_exposicion_y_activo_en_garantia  (label: 'Descalce de monedas')
[Operacion] 'endeudamiento financiero con exterior' (2 nodos):
    - Operacion_endeudamiento_de_caracter_financiero_con_el_exterior  (label: 'Endeudamiento financiero con exterior')
    - Operacion_endeudamiento_financiero_con_exterior  (label: 'Endeudamiento financiero con exterior')
[Operacion] 'evaluacion de capacidad de repago' (2 nodos):
    - Operacion_evaluacion_de_capacidad  (label: 'Evaluación de capacidad de repago')
    - Operacion_evaluacion_crediticia  (label: 'Evaluación de capacidad de repago')
[Operacion] 'incremento cartera irregular' (2 nodos):
    - Operacion_incremento_de_cartera_irregular  (label: 'Incremento cartera irregular')
    - Operacion_clasificacion_de_deudores_en_situacion_irregular  (label: 'Incremento cartera irregular')
[Operacion] 'liquidacion de divisas' (2 nodos):
    - Operacion_operacion_con_moneda_extranjera  (label: 'Liquidación de divisas')
    - Operacion_liquidacion_de_divisas  (label: 'Liquidación de divisas')
[Operacion] 'liquidacion en mercado de cambios' (3 nodos):
    - Operacion_liquidacion_de_valores  (label: 'Liquidación en mercado de cambios')
    - Operacion_liquidacion_de_divisas_en_mercado_de_cambios  (label: 'Liquidación en mercado de cambios')
    - Operacion_ingreso_y_liquidacion_de_divisas_en_mercado_de_cambios  (label: 'Liquidación en mercado de cambios')
[Operacion] 'operacion de cambio' (2 nodos):
    - Operacion_cambio  (label: 'Operación de cambio')
    - Operacion_cambio_de_moneda  (label: 'Operación de cambio')
[Operacion] 'operaciones al contado' (2 nodos):
    - Operacion_operacion_al_contado  (label: 'Operaciones al contado')
    - Operacion_operacion_de_cambios_al_contado  (label: 'Operaciones al contado')
[Operacion] 'operaciones con contrapartes vinculadas' (2 nodos):
    - Operacion_operacion_con_contraparte_vinculada  (label: 'Operaciones con contrapartes vinculadas')
    - Operacion_exportacion_a_contrapartes_vinculadas  (label: 'Operaciones con contrapartes vinculadas')
[Operacion] 'operaciones con derivados otc' (3 nodos):
    - Operacion_operacion_con_derivados_otc  (label: 'Operaciones con derivados OTC')
    - Operacion_operaciones_con_derivados_otc  (label: 'Operaciones con derivados OTC')
    - Operacion_derivados_over_the_counter  (label: 'Operaciones con derivados OTC')
[Operacion] 'operaciones de liquidacion diferida' (2 nodos):
    - Operacion_operacion_de_liquidacion_diferida  (label: 'Operaciones de liquidación diferida')
    - Operacion_operaciones_de_liquidacion_diferida  (label: 'Operaciones de liquidación diferida')
[Operacion] 'otorgamiento de credito' (2 nodos):
    - Operacion_otorgamiento_de_credito  (label: 'Otorgamiento de crédito')
    - Operacion_otorgamiento_de_credito_a_deudor_en_concurso  (label: 'Otorgamiento de crédito')
[Operacion] 'otorgamiento de garantias' (2 nodos):
    - Operacion_garantia  (label: 'Otorgamiento de garantías')
    - Operacion_otorgamiento_de_garantia  (label: 'Otorgamiento de garantías')
[Operacion] 'pago de endeudamientos financieros' (2 nodos):
    - Operacion_pago_de_capital_e_intereses  (label: 'Pago de endeudamientos financieros')
    - Operacion_pago_de_capital_e_intereses_de_endeudamientos_financieros  (label: 'Pago de endeudamientos financieros')
[Operacion] 'pago de utilidades y dividendos' (3 nodos):
    - Operacion_pago_de_utilidades_y_dividendos_a_accionistas_no_residentes  (label: 'Pago de utilidades y dividendos')
    - Operacion_pago_de_utilidades_y_dividendos  (label: 'Pago de utilidades y dividendos')
    - Operacion_distribucion_de_ganancias  (label: 'Pago de utilidades y dividendos')
[Operacion] 'prefinanciacion de exportaciones' (2 nodos):
    - Operacion_prefinanciacion_de_exportaciones  (label: 'Prefinanciación de exportaciones')
    - Operacion_prefinanciacion_de_exportaciones_con_fondeo_externo  (label: 'Prefinanciación de exportaciones')
[Operacion] 'presentacion de consulta o reclamo' (2 nodos):
    - Operacion_presentacion_de_usuario  (label: 'Presentación de consulta o reclamo')
    - Operacion_presentacion_de_consulta_o_reclamo_de_usuario  (label: 'Presentación de consulta o reclamo')
[Operacion] 'publicidad de productos y servicios' (2 nodos):
    - Operacion_comunicacion_comercial  (label: 'Publicidad de productos y servicios')
    - Operacion_publicidad  (label: 'Publicidad de productos y servicios')
[Operacion] 'repatriacion de aportes de inversion' (2 nodos):
    - Operacion_repatriacion_de_aportes_de_inversion_directa  (label: 'Repatriación de aportes de inversión')
    - Operacion_repatriacion_de_aportes  (label: 'Repatriación de aportes de inversión')
[Operacion] 'repatriacion de inversiones directas' (2 nodos):
    - Operacion_repatriacion_de_inversiones  (label: 'Repatriación de inversiones directas')
    - Operacion_repatriacion_de_inversion_extranjera  (label: 'Repatriación de inversiones directas')
[Operacion] 'solicitud de concurso preventivo' (2 nodos):
    - Operacion_solicitud_de_concurso_preventivo  (label: 'Solicitud de concurso preventivo')
    - Operacion_insolvencia  (label: 'Solicitud de concurso preventivo')
[Operacion] 'suscripcion de bonos bopreal' (2 nodos):
    - Operacion_suscripcion_de_bonos  (label: 'Suscripción de bonos BOPREAL')
    - Operacion_suscripcion_de_instrumentos  (label: 'Suscripción de bonos BOPREAL')
[Operacion] 'tenencia de titulos valores' (2 nodos):
    - Operacion_tenencia_de_titulos_valores  (label: 'Tenencia de títulos valores')
    - Operacion_tenencia_de_valores  (label: 'Tenencia de títulos valores')
[Restriccion] 'situacion financiera iliquida' (2 nodos):
    - Restriccion_presente_una_situacion_financiera_iliquida_y_un_nivel_de_flujo_de_fondos_que_no_  (label: 'Situación financiera ilíquida')
    - Restriccion_el_cliente_debe_presentar_una_situacion_financiera_iliquida_y_muy_alto_nivel_de_  (label: 'Situación financiera ilíquida')
[Restriccion] 'tipo de cambio libremente pactado' (2 nodos):
    - Restriccion_tipo_de_cambio_libremente_pactado  (label: 'Tipo de cambio libremente pactado')
    - Restriccion_las_operaciones_de_cambio_en_divisas_extranjeras_seran_realizadas_al_tipo_de_cam  (label: 'Tipo de cambio libremente pactado')
```

## S8 — WARN

WARN — Colisión de label normalizado entre types distintos.

**Resultado:** 8 grupos con el mismo label normalizado en types distintos.

```
'boleto de venta de cambio' (4 nodos):
    - [Operacion] Operacion_boleto_de_cambio
    - [Obligacion] Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_importador_
    - [Operacion] Operacion_registro_cambio
    - [Obligacion] Obligacion_boleto_de_venta_de_cambio
'ingreso y liquidacion de divisas' (2 nodos):
    - [Operacion] Operacion_ingreso_y_liquidacion_de_divisas_de_exportaciones
    - [Obligacion] Obligacion_ingreso_y_liquidacion_de_divisas
'liquidacion de cobros de exportaciones' (2 nodos):
    - [Obligacion] Obligacion_obligacion_de_liquidacion_de_los_cobros_de_exportaciones_de_bienes_y_servicios
    - [Operacion] Operacion_liquidacion_de_ingresos_por_exportaciones
'liquidacion en mercado de cambios' (4 nodos):
    - [Operacion] Operacion_liquidacion_de_valores
    - [Obligacion] Obligacion_se_compromete_a_liquidar_en_el_mercado_de_cambios_dentro_de_los_5_cinco_dias_hab
    - [Operacion] Operacion_liquidacion_de_divisas_en_mercado_de_cambios
    - [Operacion] Operacion_ingreso_y_liquidacion_de_divisas_en_mercado_de_cambios
'organismos internacionales' (2 nodos):
    - [EntidadFinanciera] EntidadFinanciera_organismo_internacional
    - [Excepcion] Excepcion_organismos_internacionales_e_instituciones_que_cumplan_funciones_de_agencias_ofi
'precancelacion simultanea nuevo endeudamiento' (2 nodos):
    - [Excepcion] Excepcion_precancelacion_de_otras_financiaciones_en_moneda_extranjera_de_entidades_financi
    - [Operacion] Operacion_precancelacion_simultanea_con_liquidacion_de_nuevo_endeudamiento
'valuacion diaria a precios de mercado' (3 nodos):
    - [Obligacion] Obligacion_valuacion_diaria_a_precios_de_mercado
    - [Restriccion] Restriccion_las_operaciones_neteadas_deben_valuarse_diariamente_a_precios_de_mercado
    - [Obligacion] Obligacion_las_posiciones_se_valuan_a_precios_de_mercado_al_menos_diariamente_y_en_el_caso_
'valuacion posiciones a termino' (2 nodos):
    - [Operacion] Operacion_valuacion_de_posiciones
    - [Obligacion] Obligacion_valuacion_posiciones_a_termino
```

## S9 — FAIL

ERROR — Descripción canónica: ningún nodo tiene a la vez 'descripcion' y 'description'.

**Resultado:** 53 nodos con ambas keys.

```
Tabla por type (usa cada key / ambas / ninguna):
  Comunicacion: descripcion=0, description=0, ambas=0, ninguna=699 (total 699)
  EntidadFinanciera: descripcion=0, description=0, ambas=0, ninguna=130 (total 130)
  Excepcion: descripcion=206, description=54, ambas=2, ninguna=0 (total 258)
  Obligacion: descripcion=733, description=532, ambas=17, ninguna=0 (total 1248)
  Operacion: descripcion=0, description=373, ambas=0, ninguna=519 (total 892)
  Restriccion: descripcion=569, description=283, ambas=34, ninguna=0 (total 818)
  TextoOrdenado: descripcion=0, description=0, ambas=0, ninguna=5 (total 5)

Nodos con AMBAS keys (53):
    - [Restriccion] Restriccion_aplicacion_de_ccf_del_0_desde_01_01_25_al_30_06_25_y_del_5_desde_01_07_25_al_31_
    - [Restriccion] Restriccion_el_requerimiento_de_capital_por_riesgo_de_credito_de_contraparte_equivaldra_a_la
    - [Restriccion] Restriccion_las_entidades_deberan_optar_por_un_unico_metodo_para_la_aplicacion_de_la_tecnica
    - [Restriccion] Restriccion_no_se_permitira_descalce_de_plazos_bajo_metodo_simple
    - [Restriccion] Restriccion_se_admite_descalce_de_monedas_al_emplear_metodo_simple_sin_tratamiento_adicional
    - [Restriccion] Restriccion_los_garantes_y_contragarantes_admisibles_se_limitaran
    - [Obligacion] Obligacion_seleccionar_un_unico_metodo_para_aplicar_la_tecnica_de_cobertura
    - [Obligacion] Obligacion_comunicar_con_6_meses_de_anticipacion_cambios_de_metodo
    - [Obligacion] Obligacion_ajustar_el_valor_de_la_cobertura_segun_lo_previsto_en_punto_5_4_5
    - [Obligacion] Obligacion_aplicar_aforo_hfx_para_ajustar_importe_por_fluctuaciones_de_tipos_de_cambio
    - [Obligacion] Obligacion_cumplir_disposiciones_para_admitir_descalce_de_plazos
    - [Obligacion] Obligacion_observar_disposiciones_para_permitir_descalce_de_monedas
    - [Restriccion] Restriccion_el_periodo_minimo_de_mantenimiento_para_operaciones_de_pase_con_liquidacion_repo
    - [Restriccion] Restriccion_el_periodo_minimo_de_mantenimiento_para_otras_operaciones_en_mercado_de_capitale
    - [Restriccion] Restriccion_el_periodo_minimo_de_mantenimiento_para_prestamos_garantizados_con_revaluacion_d
    - [Restriccion] Restriccion_aforo_del_30_para_operaciones_sft_donde_la_entidad_financiera_preste_instrumento
    - [Restriccion] Restriccion_no_se_permitira_la_aplicacion_de_cobertura_del_riesgo_de_credito_para_sft_donde_
    - [Restriccion] Restriccion_operaciones_de_financiacion_con_titulos_valores_que_cumplan_condiciones_pueden_r
    - [Obligacion] Obligacion_los_acuerdos_de_neteo_bilateral_que_alcancen_a_operaciones_de_financiacion_con_t
    - [Obligacion] Obligacion_los_acuerdos_de_compensacion_deben_proporcionar_derecho_a_terminar_y_liquidar_de
    - [Obligacion] Obligacion_los_acuerdos_deben_permitir_la_compensacion_de_perdidas_y_ganancias_resultantes_
    - [Obligacion] Obligacion_los_acuerdos_deben_permitir_la_rapida_liquidacion_o_compensacion_de_los_activos_
    - [Obligacion] Obligacion_los_acuerdos_deben_tener_validez_legal_en_toda_jurisdiccion_pertinente_ante_even
    - [Restriccion] Restriccion_las_operaciones_neteadas_deben_valuarse_diariamente_a_precios_de_mercado
    - [Restriccion] Restriccion_los_activos_que_garanticen_operaciones_compensadas_deben_ser_activos_admitidos_e
    - [Restriccion] Restriccion_los_instrumentos_son_identicos_si_tienen_igual_emisor_cupon_moneda_y_vencimiento
    - [Restriccion] Restriccion_no_se_permitira_la_exclusion_o_compensacion_de_posiciones_en_diferentes_monedas
    - [Restriccion] Restriccion_para_compensacion_las_posiciones_deben_referirse_a_los_mismos_subyacentes_tener_
    - [Restriccion] Restriccion_para_futuros_la_exclusion_procede_si_los_nocionales_e_instrumentos_subyacentes_r
    - [Restriccion] Restriccion_la_tasa_de_referencia_debe_ser_identica_con_correspondencia_cercana_entre_cupone
    - [Restriccion] Restriccion_para_swaps_fras_y_forwards_la_proxima_fecha_de_reajuste_debe_cumplir_menos_de_un
    - [Restriccion] Restriccion_los_swaps_de_monedas_y_tasas_de_interes_los_fras_los_forwards_de_moneda_y_los_fu
    - [Excepcion] Excepcion_en_futuros_cuyo_subyacente_sea_un_titulo_de_deuda_o_indice_de_titulos_de_deuda_s
    - [Obligacion] Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado
    - [Restriccion] Restriccion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi
    - [Restriccion] Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti
    - [Restriccion] Restriccion_se_debera_recategorizar_cuando_exista_discrepancia_de_mas_de_un_nivel_entre_clas
    - [Restriccion] Restriccion_las_acreencias_en_conjunto_deben_representar_el_40_o_mas_del_total_informado_por
    - [Obligacion] Obligacion_recategorizacion_del_deudor_a_partir_del_mes_siguiente_al_de_puesta_a_disposicio
    - [Obligacion] Obligacion_la_entidad_debera_informar_la_asuncion_de_la_tarea_de_seguimiento_al_bcra
    - [Restriccion] Restriccion_entidades_que_han_notificado_al_bcra_que_optaron_por_no_operar_en_comercio_exter
    - [Restriccion] Restriccion_no_podra_modificarse_voluntariamente_si_se_ha_producido_vencimiento_del_plazo_pa
    - [Restriccion] Restriccion_procedimiento_de_cambio_cuando_la_entidad_nominada_opto_por_no_operar_en_comerci
    - [Excepcion] Excepcion_la_constancia_de_aceptacion_por_parte_de_la_nueva_entidad_libera_a_la_entidad_pr
    - [Restriccion] Restriccion_se_aplicara_como_maximo_el_tipo_de_cambio_vendedor
    - [Restriccion] Restriccion_para_debito_automatico_aplicara_tipo_de_cambio_vendedor_para_operaciones_electro
    - [Obligacion] Obligacion_publicacion_del_tipo_de_cambio_vendedor_por_canales_electronicos
    - [Restriccion] Restriccion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales
    - [Obligacion] Obligacion_incrementar_valores_en_una_unidad_cuando_el_primer_digito_de_las_fracciones_sea_
    - [Obligacion] Obligacion_convertir_importes_en_moneda_extranjera_a_pesos
    - [Restriccion] Restriccion_la_informacion_tendra_frecuencia_trimestral_para_codigo_3
    - [Restriccion] Restriccion_cargo_de_capital_escalonado_segun_dias_habiles_posteriores_a_liquidacion
    - [Restriccion] Restriccion_cargo_adicional_de_capital_por_financiaciones_agricolas_con_acopio_superior_al_5
```

## S10 — FAIL

ERROR — Toda unidad regulatoria (Obligacion/Restriccion/Excepcion) tiene >=1 arista saliente establecida_en.

**Resultado:** Sin establecida_en: Obligacion=4, Restriccion=8, Excepcion=111 (total 123).

```
Obligacion: 4 sin establecida_en
    - Obligacion_poner_a_disposicion_informacion_via_home_banking
    - Obligacion_mantener_saldo_actualizado_de_financiaciones
    - Obligacion_la_entidad_debera_verificar_las_condiciones_indicadas_en_el_punto_9_3_1
    - Obligacion_la_entidad_debera_contar_con_la_documentacion_que_le_permita_verificar_el_cumpli
Restriccion: 8 sin establecida_en
    - Restriccion_factor_de_conversion_crediticia_ccf_100
    - Restriccion_limitacion_proporcion_capital_ingresado
    - Restriccion_limite_monto_acumulado_repatriaciones
    - Restriccion_restriccion_destino_garantia_endeudamientos
    - Restriccion_excepcion_por_gastos_de_transferencia_internacional
    - Restriccion_limite_anual_usd_36_000_para_personas_humanas
    - Restriccion_acreditacion_en_cuenta_especial_decreto_679_22
    - Restriccion_validacion_de_cuentas_virtuales_autorizadas
Excepcion: 111 sin establecida_en
    - Excepcion_se_excluye_del_tratamiento_de_ponderador_jurisdiccion_a_lineas_contingentes_auto
    - Excepcion_se_excluye_de_este_tratamiento_a_los_titulos_entregados_en_garantia_de_las_opera
    - Excepcion_excepcion_criterio_antiquedad_quiebra
    - Excepcion_excepcion_actividades_rotativas
    - Excepcion_excepto_que_la_cartera_subyacente_este_lo_suficientemente_atomizada_y_su_perfil_
    - Excepcion_esta_regla_no_sera_aplicable_a_las_operaciones_en_las_que_el_nocional_varia_debi
    - Excepcion_cuando_la_reestructuracion_de_la_obligacion_subyacente_no_este_contemplada_por_e
    - Excepcion_se_realicen_ajustes_por_razones_objetivas
    - Excepcion_el_bcra_establezca_que_se_debe_hacer_una_reduccion_generalizada_del_valor_si_pos
    - Excepcion_se_produzca_un_evento_idiosincrasico_y_extraordinario_del_que_resulte_una_reducc
    - Excepcion_se_realicen_mejoras_de_caracter_permanente_en_el_inmueble_que_incrementen_su_val
    - Excepcion_no_aplica_a_la_deficiencia_correspondiente_al_ultimo_dia_del_mes
    - Excepcion_la_emision_de_nuevas_acciones_como_consecuencia_de_haberse_producido_alguno_de_t
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_que_se_registren_respect
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_otros_bancos
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_sucursales_y
    - Excepcion_no_se_deduciran_los_saldos_que_con_caracter_transitorio_y_circunstancial_se_orig
    - Excepcion_no_se_consideraran_las_inversiones_obligatorias_que_deban_realizar_las_sucursale
    - Excepcion_excepcion_apertura_legajo_deudores_de_servicios_publicos
    - Excepcion_excepcion_informacion_de_repago_si_deuda_cubierta
    - Excepcion_excepcion_radicacion_en_lugar_distinto
    - Excepcion_financiaciones_sin_responsabilidad_para_el_cedente_amparadas_con_seguros_de_cred
    - Excepcion_salvo_situaciones_de_fuerza_mayor_ajenas_a_su_voluntad
    - Excepcion_pago_con_documentacion_de_financiacion_local_o_exterior
    - Excepcion_pago_con_financiacion_de_organismos_internacionales
    - Excepcion_pago_con_certificacion_de_acceso_a_divisas
    - Excepcion_pago_mediante_canje_de_fondos_bopreal
    - Excepcion_pago_con_bopreal_serie_1_suscripcion_50
    - Excepcion_pago_con_bopreal_serie_1_suscripcion_25
    - Excepcion_pago_por_mipyme_con_condiciones_especificas
    - Excepcion_el_pago_corresponde_a_servicios_comprendidos_en_los_puntos_13_2_1_o_13_2_2
    - Excepcion_el_pago_corresponda_a_la_cancelacion_de_deudas_por_operaciones_financiadas_o_gar
    - Excepcion_el_cliente_cuenta_por_el_equivalente_al_monto_a_pagar_con_una_certificacion_por_
    - Excepcion_el_pago_se_concreta_mediante_la_realizacion_de_un_canje_y_o_arbitraje_con_los_fo
    - Excepcion_el_pago_se_concreta_en_el_marco_de_lo_dispuesto_en_el_punto_4_8_4_por_un_cliente
    - Excepcion_el_pago_se_concreta_en_el_marco_de_lo_dispuesto_en_el_punto_4_8_5_por_un_cliente
    - Excepcion_el_pago_es_concretado_a_partir_del_10_02_24_por_una_persona_humana_o_una_persona
    - Excepcion_exportaciones_de_bienes_de_proyecto_exportacion_estrategica_de_largo_plazo_embar
    - Excepcion_exportaciones_de_bienes_de_proyecto_exportacion_estrategica_embarcadas_luego_del
    - Excepcion_exportaciones_de_bienes_de_proyecto_no_exportacion_estrategica_embarcadas_dentro
    - Excepcion_exportaciones_de_bienes_de_proyecto_no_exportacion_estrategica_embarcadas_luego_
    - Excepcion_cobros_por_prestacion_de_servicios_a_no_residente_por_vpu_rigi_quedan_exceptuado
    - Excepcion_cobros_anticipados_prefinanciaciones_y_posfinanciaciones_quedan_exceptuadas_por_
    - Excepcion_excepcion_para_vpu_adheridos_a_rigi
    - Excepcion_excepcion_para_servicios_de_personas_humanas
    - Excepcion_excepcion_para_servicios_de_economia_del_conocimiento
    - Excepcion_excepcion_para_operaciones_de_turismo_internacional
    - Excepcion_no_aplicable_punto_3_12_1
    - Excepcion_organismos_internacionales_e_instituciones_que_cumplan_funciones_de_agencias_ofi
    - Excepcion_representaciones_diplomaticas_y_consulares_y_personal_diplomatico_acreditado_en_
    - Excepcion_representaciones_en_el_pais_de_tribunales_autoridades_u_oficinas_misiones_especi
    - Excepcion_transferencias_al_exterior_a_nombre_de_personas_humanas_beneficiarias_de_jubilac
    - Excepcion_compra_de_billetes_en_moneda_extranjera_de_personas_humanas_no_residentes_en_con
    - Excepcion_transferencias_a_cuentas_bancarias_en_el_exterior_de_personas_humanas_por_fondos
    - Excepcion_repatriaciones_de_inversiones_directas_de_no_residentes_en_empresas_que_no_sean_
    - Excepcion_repatriaciones_de_inversiones_directas_de_no_residentes_hasta_el_monto_de_aporte
    - Excepcion_repatriaciones_de_inversiones_directas_a_traves_del_residente_que_adquirio_parti
    - Excepcion_repatriaciones_de_aportes_de_inversion_directa_de_no_residentes_en_una_vehiculo_
    - Excepcion_este_requisito_no_resultara_aplicable_para_el_acceso_al_mercado_para_las_cancela
    - Excepcion_este_requisito_no_resultara_a_aplicacion_para_aquellas_operaciones_de_egresos_qu
    - Excepcion_las_transferencias_de_titulos_valores_a_entidades_depositarias_del_exterior_real
    - Excepcion_la_entrega_de_activos_locales_con_el_objeto_de_cancelar_una_deuda_con_una_agenci
    - Excepcion_las_ventas_de_titulos_valores_con_liquidacion_en_moneda_extranjera_cuando_la_tot
    - Excepcion_las_repatriaciones_del_capital_y_rentas_asociadas_a_inversiones_directas_de_no_r
    - Excepcion_el_exportador_podra_solicitar_que_el_plazo_sea_ampliado_hasta_el_quinto_dia_habi
    - Excepcion_no_resultara_aplicable_cuando_se_cumpla_la_totalidad_de_las_siguientes_condicion
    - Excepcion_no_resultara_aplicable_cuando_se_trate_de_operaciones_propias_de_las_entidades_f
    - Excepcion_no_resultara_aplicable_cuando_se_trate_de_un_endeudamiento_financiero_comprendid
    - Excepcion_no_resultara_aplicable_cuando_se_trate_de_un_pago_de_intereses_compensatorios_qu
    - Excepcion_no_resultara_aplicable_cuando_el_cliente_es_un_vehiculo_de_proyecto_unico_vpu_ad
    - Excepcion_no_resultara_aplicable_cuando_se_trate_de_un_pago_de_intereses_que_se_concreta_s
    - Excepcion_no_resultara_aplicable_cuando_el_cliente_cuente_con_una_certificacion_por_los_re
    - Excepcion_no_resultara_aplicable_cuando_el_cliente_cuente_con_una_certificacion_de_aumento
    - Excepcion_el_requisito_de_demostracion_de_ingreso_y_liquidacion_de_divisas_se_considera_cu
    - Excepcion_endeudamientos_originados_a_partir_del_01_09_19_que_no_generen_desembolsos_por_s
    - Excepcion_el_requisito_se_considera_cumplimentado_por_el_monto_de_los_gastos_de_otorgamien
    - Excepcion_por_la_diferencia_entre_el_valor_efectivo_y_el_valor_nominal_en_emisiones_de_tit
    - Excepcion_por_la_porcion_que_corresponda_a_una_capitalizacion_de_intereses_prevista_en_el_
    - Excepcion_por_la_porcion_de_los_nuevos_titulos_de_deuda_entregadas_en_canje_recompra_y_o_r
    - Excepcion_por_la_porcion_de_las_emisiones_de_titulos_de_deuda_con_registro_publico_realiza
    - Excepcion_por_la_porcion_suscripta_con_moneda_extranjera_en_el_pais_de_emisiones_de_titulo
    - Excepcion_si_no_se_cumplen_las_condiciones_de_exportaciones_previas_o_destino_de_fondos_la
    - Excepcion_endeudamientos_con_el_exterior_originados_a_partir_del_01_09_19_en_una_refinanci
    - Excepcion_endeudamientos_con_vida_promedio_no_inferior_a_2_anos_originados_entre_27_08_21_
    - Excepcion_excepcion_por_liquidaciones_en_mercado_de_cambios
    - Excepcion_excepcion_por_titulos_denominados_en_moneda_extranjera
    - Excepcion_excepcion_por_certificacion_de_exportaciones
    - Excepcion_excepcion_por_certificacion_de_acceso_a_divisas
    - Excepcion_cancelacion_en_el_pais_a_partir_de_su_vencimiento_de_capital_e_intereses_de_fina
    - Excepcion_cancelacion_de_giros_en_descubierto_en_cuentas_corrientes_en_dolares_estadounide
    - Excepcion_emisiones_de_titulos_de_deuda_realizadas_a_partir_del_01_09_19_con_objeto_de_ref
    - Excepcion_emisiones_realizadas_a_partir_del_29_11_19_de_titulos_de_deuda_con_registro_publ
    - Excepcion_para_titulos_de_deuda_emitidos_por_entidades_financieras_locales_a_traves_de_ope
    - Excepcion_pagares_con_oferta_publica_emitidos_en_marco_de_resolucion_general_1_003_24_de_c
    - Excepcion_valores_de_deuda_fiduciaria_emitidos_por_fiduciarios_de_fideicomisos_financieros
    - Excepcion_emisiones_de_valores_comprendidos_en_puntos_3_6_1_3_a_3_6_1_5_que_no_generaron_d
    - Excepcion_financiaciones_de_entidades_locales_por_consumos_en_moneda_extranjera_mediante_t
    - Excepcion_precancelacion_de_otras_financiaciones_en_moneda_extranjera_de_entidades_financi
    - Excepcion_si_la_financiacion_precancelada_por_el_cliente_hubiese_sido_otorgada_a_partir_de
    - Excepcion_precancelacion_de_intereses_en_marco_de_proceso_de_canje_de_titulos_de_deuda_emi
    - Excepcion_precancelacion_de_capital_e_intereses_de_titulo_de_deuda_comprendido_en_punto_3_
    - Excepcion_se_podran_liquidar_en_pesos_en_el_pais_solamente_aquellas_operaciones_concertada
    - Excepcion_cuando_se_trate_de_la_venta_de_bonos_bopreal_adquiridos_por_el_vendedor_en_una_s
    - Excepcion_podran_ser_contraparte_sucursales_o_agencias_en_exterior_de_bancos_oficiales_loc
    - Excepcion_salvo_que_el_cliente_pueda_demostrar_que_no_puede_hacerlo_de_dicha_forma_por_cau
    - Excepcion_solicitud_de_extension_de_plazo
    - Excepcion_excepto_cuando_por_un_monto_igual_o_superior_al_excedente_el_deudor_registraba_l
    - Excepcion_excepto_cuando_el_deudor_contaba_con_una_certificacion_de_aumento_de_exportacion
    - Excepcion_excepto_cuando_el_deudor_contaba_con_una_certificacion_por_los_regimenes_de_acce
    - Excepcion_informacion_con_frecuencia_trimestral
    - Excepcion_excepcion_para_ratio_de_apalancamiento
```

## S11 — WARN

WARN — Toda Obligacion y Restriccion tiene >=1 arista saliente aplica_a.

**Resultado:** Sin aplica_a: Obligacion=458, Restriccion=297 (total 755).

```
Obligacion: 458 sin aplica_a
    - Obligacion_considerar_factores_ecai_en_asignacion
    - Obligacion_se_computara_el_importe_que_surja_de_aplicar_a_los_valores_contables_de_los_inst
    - Obligacion_se_considerara_la_ultima_calificacion_informada_para_el_calculo_de_la_exigencia_
    - Obligacion_a_los_fines_de_calcular_el_limite_se_aplicara_el_citado_porcentaje_al_saldo_de_l
    - Obligacion_la_exposicion_total_sera_el_monto_bruto_sin_computar_las_coberturas_del_riesgo_d
    - Obligacion_las_partidas_fuera_de_balance_se_computaran_luego_de_aplicar_el_factor_de_conver
    - Obligacion_a_los_efectos_de_considerar_en_las_exposiciones_minoristas_normativas_a_los_cred
    - Obligacion_recategorizacion_de_posiciones_de_deuda_como_acciones
    - Obligacion_el_ponderador_de_riesgo_de_exposiciones_a_entidades_financieras_no_puede_ser_inf
    - Obligacion_computar_conceptos_sobre_saldos_mensuales
    - Obligacion_computar_saldos_al_cierre_trimestral
    - Obligacion_utilizar_calificacion_de_ecai_admitida
    - Obligacion_tener_en_cuenta_disposiciones_especificas_por_tipo_de_exposicion
    - Obligacion_aplicar_criterio_posicion_neta_para_sector_publico_no_financiero
    - Obligacion_incluir_saldos_de_deuda_y_compromisos_eventuales
    - Obligacion_el_computo_se_efectuara_neto_de_las_previsiones_por_riesgo_de_desvalorizacion
    - Obligacion_el_importe_por_encima_de_este_10_debera_deducirse_de_cada_uno_de_los_niveles_de_
    - Obligacion_si_la_entidad_financiera_carece_de_suficiente_capital_para_efectuar_la_deduccion
    - Obligacion_los_importes_por_debajo_del_umbral_que_no_se_deducen_se_ponderan_en_funcion_del_
    - Obligacion_ambos_componentes_se_ponderaran_por_un_factor_de_correlacion_que_determinara_el_
    - Obligacion_los_derivados_que_hagan_referencia_a_indices_de_credito_se_consideraran_como_si_
    - Obligacion_se_utilizara_un_modelo_de_factor_unico_para_dividir_el_riesgo_de_cada_entidad_de
    - Obligacion_la_compensacion_o_cobertura_total_estaran_permitidas_entre_todas_las_operaciones
    - Obligacion_la_documentacion_provisional_inicial_oferta_o_prospecto_provisional_y_de_apoyo_t
    - Obligacion_la_documentacion_final_de_la_oferta_o_el_prospecto_debera_estar_disponible_desde
    - Obligacion_toda_esa_documentacion_debera_ser_apropiadamente_revisada_por_consultores_legale
    - Obligacion_los_inversores_deberan_ser_notificados_con_la_debida_anticipacion_respecto_de_cu
    - Obligacion_tanto_en_la_oferta_inicial_como_en_la_documentacion_contractual_deberia_incluirs
    - Obligacion_la_entidad_financiera_debera_deducir_del_capital_ordinario_de_nivel_uno_con1_el_
    - Obligacion_se_debera_deducir_del_capital_ordinario_de_nivel_uno_con1_todo_incremento_del_ca
    - Obligacion_debera_deducir_del_capital_ordinario_de_nivel_uno_con1_el_importe_total_en_conce
    - Obligacion_el_activo_ponderado_por_riesgo_correspondiente_a_una_posicion_de_titulizacion_se
    - Obligacion_el_importe_de_la_posicion_de_titulizacion_se_calculara_como_la_suma_del_valor_co
    - Obligacion_se_debe_conocer_en_todo_momento_la_composicion_del_conjunto_subyacente_de_exposi
    - Obligacion_las_coberturas_del_riesgo_de_credito_deben_cumplir_los_requisitos_establecidos_e
    - Obligacion_la_entidad_debe_transferir_a_terceros_el_riesgo_de_credito_asociado_a_las_exposi
    - Obligacion_se_debe_contar_con_dictamen_juridico_competente_que_confirme_la_exigibilidad_del
    - Obligacion_se_debera_demostrar_la_existencia_de_los_obstaculos_que_impiden_ajustarse_a_los_
    - Obligacion_debera_informarse_toda_condicion_o_evento_que_pueda_retrasar_o_impedir_la_transf
    - Obligacion_se_debera_contar_con_suficiente_informacion_a_nivel_de_cada_prestamo_o_en_el_cas
    - Obligacion_se_debera_suministrar_al_menos_trimestralmente_durante_la_vida_de_la_titulizacio
    - Obligacion_las_fechas_de_corte_de_los_datos_deberan_estar_en_linea_con_las_utilizadas_para_
    - Obligacion_la_cartera_inicial_debera_ser_revisada_por_un_contador_publico_independiente_a_e
    - Obligacion_los_riesgos_de_tasa_de_interes_y_de_moneda_extranjera_deberan_mitigarse_en_forma
    - Obligacion_se_debera_demostrar_que_tales_riesgos_son_adecuadamente_mitigados_a_traves_de_in
    - Obligacion_esa_informacion_debera_incluir_la_porcion_del_monto_nocional_cubierto_asi_como_u
    - Obligacion_el_alcance_y_adecuacion_de_la_cobertura_deberan_ser_explicados_y_divulgados_a_lo
    - Obligacion_el_orden_de_prelacion_en_el_pago_de_todos_los_compromisos_debera_estar_clarament
    - Obligacion_todos_los_eventos_desencadenantes_que_puedan_afectar_el_orden_de_prelacion_en_lo
    - Obligacion_los_reportes_deberan_contener_informacion_que_identifique_cualquier_incumplimien
    - Obligacion_tambien_deberan_proveer_informacion_que_permita_realizar_un_seguimiento_de_la_ev
    - Obligacion_cuando_uno_de_estos_eventos_ocurra_entre_dos_fechas_de_pago_previstas_se_debera_
    - Obligacion_las_titulizaciones_con_periodos_rotativos_deberan_establecer_eventos_de_amortiza
    - Obligacion_luego_de_la_ocurrencia_de_un_incumplimiento_u_otro_evento_desencadenante_de_la_a
    - Obligacion_calcular_nocional_para_cada_estado
    - Obligacion_emplear_promedio_ponderado_de_nocional
    - Obligacion_multiplicar_nocional_por_factor_de_apalancamiento
    - Obligacion_multiplicar_nocional_por_numero_de_intercambios
    - Obligacion_aplicar_parametro_delta_regulatorio
    - Obligacion_calcular_parametros_de_opciones
    - Obligacion_calcular_parametros_de_segmentos_cdo
    - Obligacion_considerar_lo_dispuesto
    - Obligacion_cumplir_requisitos_de_custodio
    - Obligacion_aplicar_ponderador_segregado_por_producto
    - Obligacion_aplicacion_de_aforos_a_sft
    - Obligacion_la_ccp_la_entidad_financiera_la_autoridad_de_control_de_la_ccp_u_otro_organismo_
    - Obligacion_las_entidades_financieras_deberan_asegurarse_de_que_la_composicion_de_las_exposi
    - Obligacion_las_entidades_deberan_informar_todo_otro_tipo_de_compromiso_con_las_ccp_y_su_nat
    - Obligacion_ajustar_el_valor_de_la_cobertura_segun_lo_previsto_en_punto_5_4_5
    - Obligacion_aplicar_aforo_hfx_para_ajustar_importe_por_fluctuaciones_de_tipos_de_cambio
    - Obligacion_cumplir_disposiciones_para_admitir_descalce_de_plazos
    - Obligacion_observar_disposiciones_para_permitir_descalce_de_monedas
    - Obligacion_cuando_la_proteccion_crediticia_proporcionada_por_un_mismo_proveedor_tenga_plazo
    - Obligacion_la_reduccion_o_transferencia_del_riesgo_de_credito_a_traves_del_uso_de_tecnicas_
    - Obligacion_la_instrumentacion_de_la_garantia_debera_asegurar_que_la_entidad_tenga_el_derech
    - Obligacion_las_entidades_deberan_cumplir_con_todos_los_requisitos_legales_necesarios_a_fin_
    - Obligacion_las_entidades_financieras_deberan_contar_con_procedimientos_claros_y_solidos_que
    - Obligacion_cuando_el_activo_recibido_en_garantia_sea_mantenido_en_custodia_las_entidades_fi
    - Obligacion_debe_representar_un_derecho_crediticio_directo_frente_al_proveedor_de_la_protecc
    - Obligacion_en_caso_de_incumplimiento_de_la_contraparte_la_entidad_financiera_puede_emprende
    - Obligacion_la_garantia_es_una_obligacion_explicitamente_documentada_que_asume_el_garante
    - Obligacion_los_eventos_de_credito_especificados_por_las_partes_contratantes_deberan_incluir
    - Obligacion_sera_necesario_establecer_con_exactitud_el_periodo_durante_el_cual_podran_obtene
    - Obligacion_debera_identificarse_claramente_a_las_partes_responsables_de_determinar_si_ocurr
    - Obligacion_los_acuerdos_de_compensacion_deben_proporcionar_derecho_a_terminar_y_liquidar_de
    - Obligacion_los_acuerdos_deben_permitir_la_compensacion_de_perdidas_y_ganancias_resultantes_
    - Obligacion_los_acuerdos_deben_permitir_la_rapida_liquidacion_o_compensacion_de_los_activos_
    - Obligacion_los_acuerdos_deben_tener_validez_legal_en_toda_jurisdiccion_pertinente_ante_even
    - Obligacion_se_reconocera_la_proteccion_crediticia_provista_por_entes_admisibles_cuando_las_
    - Obligacion_se_reconocera_la_proteccion_crediticia_en_la_medida_de_que_el_ponderador_de_ries
    - Obligacion_los_plazos_de_vencimiento_deberan_medirse_en_forma_conservadora_considerando_el_
    - Obligacion_con_relacion_a_la_crc_se_debera_tener_en_cuenta_las_opciones_incorporadas_que_pu
    - Obligacion_el_aforo_por_descalce_de_monedas_debera_incrementarse_proporcionalmente_utilizan
    - Obligacion_el_valor_del_inmueble_sea_el_resultado_de_una_tasacion_que_cumpla_criterios_de_v
    - Obligacion_cualquier_derecho_sobre_el_inmueble_debera_ser_juridicamente_exigible_y_la_docum
    - Obligacion_toda_la_informacion_que_se_solicite_tanto_en_la_originacion_del_prestamo_como_du
    - Obligacion_evaluar_ajustes_por_margenes_y_costos
    - Obligacion_evaluar_ajustes_en_todas_las_posiciones
    - Obligacion_sefyc_verificar_saldos_al_cierre
    - Obligacion_computar_posiciones_netas
    - Obligacion_calcular_exigencia_por_dos_riesgos
    - Obligacion_incluir_derivados_en_computo
    - Obligacion_declarar_futuros_a_precio_de_mercado
    - Obligacion_declarar_indices_al_valor_nocional
    - Obligacion_tratar_swaps_como_dos_posiciones
    - Obligacion_neteado_de_posiciones_compensadas
    - Obligacion_vigilar_y_gestionar_arbitraje_deliberado
    - Obligacion_tratamiento_de_posiciones_excedentes
    - Obligacion_compensacion_de_posiciones_contrarias
    - Obligacion_se_deberan_calcular_los_coeficientes_delta_gamma_y_vega_para_las_posiciones_en_o
    - Obligacion_las_entidades_que_usen_modelos_propios_deberan_poner_a_disposicion_de_la_sefyc_t
    - Obligacion_las_posiciones_ponderadas_por_delta_cuyo_subyacente_sean_titulos_de_deuda_o_tasa
    - Obligacion_las_exigencias_de_capital_para_cubrir_los_riesgos_gamma_y_vega_se_calcularan_por
    - Obligacion_calcular_exigencia_capital_riesgo_gamma
    - Obligacion_calcular_exigencia_capital_riesgo_vega
    - Obligacion_calcular_exigencia_total_capital_riesgo_vega
    - Obligacion_ib_ingreso_bruto_de_periodos_de_12_meses_consecutivos_siempre_que_sea_positivo_c
    - Obligacion_de_los_rubros_contables_mencionados_en_i_y_ii_se_excluiran_los_siguientes_concep
    - Obligacion_incluir_resultados_con_dictamen_auditor
    - Obligacion_aplicar_porcentajes_sobre_saldo_neto_acumulado
    - Obligacion_presentar_estado_financiero_con_informe_auditor_al_bcra
    - Obligacion_si_hubiera_compensacion_a_los_tenedores_de_estos_instrumentos_por_la_quita_reali
    - Obligacion_presentar_copia_de_acta_certificada_de_asamblea
    - Obligacion_contar_con_intervencion_del_auditor_externo
    - Obligacion_presentar_estado_financiero_ante_bcra
    - Obligacion_incorporacion_criterio_informacion
    - Obligacion_abrir_legajo_de_firmante_librador_deudor
    - Obligacion_poner_a_disposicion_legajos_de_deudores
    - Obligacion_reunir_elementos_de_juicio_en_legajo
    - Obligacion_mantener_clasificacion_en_planillas_separadas
    - Obligacion_incluir_informacion_de_margenes_crediticios
    - Obligacion_mantener_declaracion_jurada_de_vinculacion
    - Obligacion_incluir_informacion_de_corresponsales_en_legajo
    - Obligacion_constar_analisis_de_graduacion_del_credito
    - Obligacion_anexar_carpetas_crediticia_legal_y_administracion
    - Obligacion_llevar_legajo_en_lugar_de_radicacion
    - Obligacion_informacion_de_deudores_segun_regimenes
    - Obligacion_solo_se_aplicaran_los_criterios_precedentes_cuando_se_trate_de_operaciones_del_t
    - Obligacion_evaluar_capacidad_de_repago_del_deudor
    - Obligacion_medir_exposicion_en_moneda_extranjera
    - Obligacion_analizar_capacidad_de_pago_con_variaciones_cambiarias
    - Obligacion_considerar_escenarios_de_variacion_cambiaria
    - Obligacion_evaluar_riesgo_pais_para_clientes_residentes_en_exterior
    - Obligacion_evaluar_situacion_economica_del_pais_deudor
    - Obligacion_evaluar_deuda_externa_del_pais
    - Obligacion_evaluar_cuenta_corriente_del_pais
    - Obligacion_evaluar_historial_financiero_del_pais
    - Obligacion_la_revision_debera_efectuarse_como_minimo_con_la_periodicidad_que_se_indica_segu
    - Obligacion_revision_en_el_curso_de_cada_semestre_calendario_respecto_de_clientes_cuyas_fina
    - Obligacion_al_cierre_del_primer_semestre_calendario_el_examen_debera_haber_alcanzado_no_men
    - Obligacion_en_el_curso_del_ejercicio_economico_en_los_demas_casos_por_lo_que_a_su_finalizac
    - Obligacion_a_fin_de_determinar_el_importe_de_la_cancelacion_se_admitira_computar_el_50_de_l
    - Obligacion_sera_requisito_indispensable_contar_con_la_opinion_favorable_sobre_la_calidad_de
    - Obligacion_debera_plantear_a_la_superintendencia_de_entidades_financieras_y_cambiarias_cada
    - Obligacion_de_no_haberse_alcanzado_el_acuerdo_dentro_del_plazo_establecido_debera_reclasifi
    - Obligacion_para_las_refinanciaciones_otorgadas_por_primera_vez_dentro_del_ano_calendario_y_
    - Obligacion_luego_de_la_refinanciacion_y_a_los_fines_de_la_clasificacion_debera_tenerse_en_c
    - Obligacion_permanecer_en_categoria_180_dias
    - Obligacion_a_los_fines_de_la_clasificacion_debera_tenerse_en_cuenta_la_mora_en_el_atraso_de
    - Obligacion_a_los_fines_de_establecer_los_dias_de_atraso_en_el_caso_de_las_financiaciones_in
    - Obligacion_no_se_considerara_refinanciacion_la_asistencia_que_se_otorgue_a_los_deudores_cla
    - Obligacion_en_caso_de_verificarse_atrasos_mayores_a_31_dias_en_el_pago_de_los_servicios_de_
    - Obligacion_en_caso_de_verificarse_refinanciaciones_en_condiciones_distintas_a_las_senaladas
    - Obligacion_corresponde_reclasificacion_inmediata_del_deudor_en_nivel_determinado_por_sumato
    - Obligacion_se_verifiquen_los_restantes_requisitos_normativos_aplicables
    - Obligacion_las_fechas_de_vencimiento_y_los_montos_de_capital_a_pagar_de_la_financiacion_oto
    - Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_importador_en_la_que_se_
    - Obligacion_la_entidad_adicionalmente_debera_contar_con_una_declaracion_jurada_del_importado
    - Obligacion_verificacion_de_requisitos_para_excepcion
    - Obligacion_registro_en_padron_de_deuda_comercial
    - Obligacion_declaracion_de_operacion_en_relevamiento_de_activos
    - Obligacion_declaracion_jurada_del_cliente
    - Obligacion_copia_del_documento_de_salida_de_zona_primaria_aduanera
    - Obligacion_copia_de_la_solicitud_particular_autenticada_por_autoridad_aduanera_competente_e
    - Obligacion_copia_del_certificado_y_o_constancia_de_autorizacion_emitido_por_la_fuerza_armad
    - Obligacion_se_presente_el_formulario_zfe_de_oficializacion_de_ingreso_de_los_bienes_al_pais
    - Obligacion_se_presente_el_documento_de_transferencia_aduanera_de_dominio_autorizado_por_la_
    - Obligacion_la_informacion_que_surge_de_la_factura_comercial_sea_consistente_con_la_informac
    - Obligacion_se_cuente_con_la_certificacion_de_la_entidad_a_cargo_del_seguimiento_del_zfi_de_
    - Obligacion_la_entidad_que_cursa_el_pago_al_exterior_debera_intervenir_el_documento_aduanero
    - Obligacion_el_boleto_de_venta_debera_efectuarse_a_nombre_de_la_propia_entidad_en_calidad_de
    - Obligacion_el_boleto_de_cambio_de_venta_se_realizara_por_los_conceptos_b06_b14_b15_o_b22_se
    - Obligacion_si_en_el_monto_total_de_la_transferencia_se_incluyeran_otros_conceptos_que_no_fo
    - Obligacion_incluir_anexo_con_datos_de_despachos
    - Obligacion_verificar_requisitos_pago_anticipado
    - Obligacion_presentar_documentacion_compra_exterior
    - Obligacion_registrar_ingreso_aduanero_importacion
    - Obligacion_reportar_extension_plazo_sepaimpo
    - Obligacion_solicitar_conformidad_bcra
    - Obligacion_avalar_razonabilidad_montos_a_pagar
    - Obligacion_solicitar_conformidad_bcra_por_monto
    - Obligacion_consultar_regimen_informativo_sepaimpo
    - Obligacion_verificar_demoras_cliente_sepaimpo
    - Obligacion_presentacion_de_factura_comercial
    - Obligacion_verificacion_de_requisitos_con_donacion
    - Obligacion_verificacion_de_liquidacion_de_cobros
    - Obligacion_verificar_documentacion_aduanera
    - Obligacion_controlar_montos_de_pagos
    - Obligacion_verificar_encuadramiento_operaciones_financiadas
    - Obligacion_emitir_certificaciones_de_acceso
    - Obligacion_verificar_requisitos_previo_a_emision
    - Obligacion_obtener_declaracion_jurada_de_importador
    - Obligacion_emitir_certificacion_para_afectacion
    - Obligacion_verificar_correspondencia_pago_operacion
    - Obligacion_emitir_certificacion_para_cancelacion_exterior
    - Obligacion_emitir_certificacion_para_bopreal
    - Obligacion_inhabilitar_zfi_para_pagos
    - Obligacion_emitir_certificacion_para_imputacion_exportaciones
    - Obligacion_emitir_certificacion_para_financiaciones_exportacion
    - Obligacion_reportar_circunstancias
    - Obligacion_registrar_diferencia_aduanera
    - Obligacion_mantener_registro_de_certificaciones
    - Obligacion_archivar_documentacion
    - Obligacion_verificacion_de_requisitos_normativos
    - Obligacion_informacion_obligatoria_en_certificacion
    - Obligacion_transmision_de_certificacion_a_entidad_pagadora
    - Obligacion_devolucion_de_certificaciones_no_utilizadas
    - Obligacion_informacion_en_certificacion_de_afectacion
    - Obligacion_transmision_segura_de_certificacion_de_afectacion
    - Obligacion_reporte_al_bcra_de_utilizacion_de_certificacion
    - Obligacion_obligacion_de_reportar_circunstancias_modificatorias
    - Obligacion_verificacion_de_condiciones_para_cesion
    - Obligacion_obligacion_requisitos_aplicables_para_acceso_mercado_cambios
    - Obligacion_si_el_otorgamiento_de_la_financiacion_es_anterior_a_la_fecha_de_prestacion_o_dev
    - Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_servicios_de_fletes_por_opera
    - Obligacion_si_el_otorgamiento_de_la_financiacion_es_posterior_a_la_fecha_de_prestacion_o_de
    - Obligacion_el_cliente_haya_registrado_la_totalidad_de_sus_deudas_por_importaciones_de_biene
    - Obligacion_la_entidad_cuente_con_una_declaracion_jurada_del_cliente_en_la_que_conste_que_la
    - Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_debia_ser_concretado_por_el_c
    - Obligacion_incorporacion_a_seguimiento_apx
    - Obligacion_las_operaciones_de_cambio_deberan_sujetarse_a_los_requisitos_y_a_la_reglamentaci
    - Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios
    - Obligacion_declaracion_jurada_del_exportador
    - Obligacion_neutralidad_fiscal_en_operaciones
    - Obligacion_confeccion_de_boletos_sin_movimiento_de_pesos
    - Obligacion_declaracion_jurada_de_servicios_de_economia_del_conocimiento
    - Obligacion_presentacion_de_certificacion_de_exportaciones
    - Obligacion_confeccion_de_boletos_para_turismo
    - Obligacion_liquidacion_por_monto_acreditado
    - Obligacion_aplicacion_de_cobros_a_cancelacion
    - Obligacion_acumulacion_en_cuentas_abiertas
    - Obligacion_ingresar_contravalor_en_divisas
    - Obligacion_liquidar_en_mercado_cambios
    - Obligacion_los_divisas_deben_haber_ingresado_por_el_mercado_de_cambios_en_los_plazos_establ
    - Obligacion_contar_con_una_certificacion_de_incremento_de_exportaciones_asociadas_a_la_econo
    - Obligacion_cumplimiento_a_los_restantes_requisitos_establecidos_en_los_puntos_2_2_2_2_o_7_8
    - Obligacion_el_beneficiario_debera_nominar_una_unica_entidad_financiera_local_que_sera_la_re
    - Obligacion_la_entidad_nominada_debe_emitir_las_certificaciones_de_incremento_de_exportacion
    - Obligacion_la_entidad_debera_antes_de_la_emision_de_cada_certificacion_constatar_el_valor_d
    - Obligacion_la_entidad_debe_contar_con_una_declaracion_jurada_del_exportador_en_la_que_se_de
    - Obligacion_constatar_cumplimiento_de_condiciones_y_requisitos
    - Obligacion_reportar_seguimiento_cumplimentado_al_bcra
    - Obligacion_emitir_certificacion_de_cumplido
    - Obligacion_realizar_denuncia_de_incumplido
    - Obligacion_notificar_modificacion_de_permiso_incumplido
    - Obligacion_reportar_cierre_de_incumplido
    - Obligacion_remitir_certificacion_de_incumplido_en_gestion_de_cobro
    - Obligacion_realizar_rectificaciones_de_seguimiento
    - Obligacion_reportar_extensiones_de_plazo_de_liquidacion
    - Obligacion_acreditacion_en_cuenta_local
    - Obligacion_verificar_mecanismos_legales_de_reduccion
    - Obligacion_verificar_pasivo_declarado_en_rale
    - Obligacion_precancelacion_de_lineas_de_credito
    - Obligacion_cumplir_requisito_complementario_vpu_rigi
    - Obligacion_certificar_el_cumplimiento_de_las_condiciones_de_elegibilidad_de_las_operaciones
    - Obligacion_efectuar_el_seguimiento_de_los_permisos_de_embarques_cuyos_cobros_se_mantengan_e
    - Obligacion_efectuar_el_seguimiento_de_las_garantias_constituidas_y_de_las_cuentas_especiale
    - Obligacion_certificar_el_cumplimiento_de_las_condiciones_para_la_elegibilidad_del_proyecto
    - Obligacion_efectuar_el_seguimiento_de_la_ejecucion_del_proyecto_y_su_financiacion
    - Obligacion_la_certificacion_que_se_presente_en_el_bcra_debera_contener_como_minimo_el_detal
    - Obligacion_la_certificacion_que_emita_la_entidad_financiera_debera_basarse_en_las_proyeccio
    - Obligacion_la_entidad_solicitara_los_dictamenes_profesionales_que_estime_necesarios_para_as
    - Obligacion_la_documentacion_utilizada_por_la_entidad_financiera_y_hojas_de_trabajo_que_aval
    - Obligacion_el_cambio_de_entidad_debe_quedar_registrado_en_el_bcra
    - Obligacion_la_entidad_previa_debe_remitir_el_detalle_de_las_certificaciones_emitidas_a_nomb
    - Obligacion_verificar_declaracion_de_activos
    - Obligacion_acceso_a_mercado_de_cambios_por_fecha
    - Obligacion_conformidad_previa_bcra_precancelacion
    - Obligacion_conformidad_previa_contraparte_vinculada
    - Obligacion_verificar_requisitos_normativos
    - Obligacion_la_entidad_debera_contar_con_una_certificacion_para_el_acceso_al_mercado_de_camb
    - Obligacion_el_deudor_debera_demostrar_haber_registrado_exportaciones_con_anterioridad_a_la_
    - Obligacion_obtener_conformidad_previa_del_bcra_para_acceso_al_mercado_de_cambios_con_anteri
    - Obligacion_la_vida_promedio_del_nuevo_endeudamiento_sea_mayor_a_la_vida_promedio_remanente_
    - Obligacion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_en_nin
    - Obligacion_en_caso_de_que_el_nuevo_endeudamiento_sea_una_prefinanciacion_de_exportaciones_d
    - Obligacion_el_monto_abonado_antes_del_vencimiento_corresponde_a_los_intereses_devengados_a_
    - Obligacion_la_vida_promedio_de_los_nuevos_titulos_de_deuda_es_mayor_a_la_vida_promedio_rema
    - Obligacion_el_monto_acumulado_de_los_vencimientos_de_capital_de_los_nuevos_titulos_en_ningu
    - Obligacion_verificar_calificacion_de_deuda
    - Obligacion_verificar_declaracion_en_relevamiento_externo
    - Obligacion_verificar_condiciones_de_acceso_al_mercado_de_cambios
    - Obligacion_verificar_requisitos_complementarios
    - Obligacion_realizar_boleto_de_venta_de_cambio
    - Obligacion_la_obligacion_califica_como_una_deuda_por_importaciones_de_servicios_segun_lo_in
    - Obligacion_la_operacion_se_encuentra_declarada_en_caso_de_corresponder_en_la_ultima_present
    - Obligacion_el_cliente_cumple_los_requisitos_complementarios_previstos_en_los_puntos_3_16_1_
    - Obligacion_cuenta_con_una_declaracion_jurada_del_cliente_en_la_que_deja_constancia_de_que_l
    - Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_importador_
    - Obligacion_documentacion_de_deuda_pendiente
    - Obligacion_declaracion_de_operacion_en_relevamiento
    - Obligacion_declaracion_jurada_de_acreedor
    - Obligacion_firma_de_declaracion_por_representante
    - Obligacion_registro_de_boleto_de_cambio
    - Obligacion_verificacion_de_origen_de_fondos
    - Obligacion_declaracion_de_fondos_no_remitidos
    - Obligacion_documentacion_de_avalo_de_deuda
    - Obligacion_verificar_declaracion_en_relevamiento
    - Obligacion_cumplimiento_de_requisitos_de_mercado_cambios
    - Obligacion_presentacion_de_declaracion_jurada
    - Obligacion_boleto_de_venta_de_cambio
    - Obligacion_se_podra_consultar_los_tipos_de_cambio_minoristas_de_referencia_tcmr_comprador_y
    - Obligacion_presentacion_de_documento_identidad
    - Obligacion_uso_de_firmas_electronicas_digitales
    - Obligacion_identificacion_por_canales_electronicos
    - Obligacion_identificar_pago_a_nivel_de_beneficiario
    - Obligacion_confeccionar_boleto_a_nombre_de_la_entidad
    - Obligacion_ordenante_empresa_del_exterior
    - Obligacion_programas_prevencion_lavado_de_activos
    - Obligacion_emitir_certificacion_de_ingreso_y_liquidacion
    - Obligacion_presumir_residencia_por_permanencia_anual
    - Obligacion_clasificar_persona_juridica_residente
    - Obligacion_clasificar_sucursal_residente_por_inscripcion
    - Obligacion_clasificar_residencia_por_representante_legal
    - Obligacion_el_exportador_debera_seleccionar_una_entidad_como_responsable_de_su_seguimiento
    - Obligacion_la_entidad_sera_la_unica_responsable_de_emitir_los_certificados_de_aplicacion_qu
    - Obligacion_seguimiento_de_permiso_de_exportacion
    - Obligacion_descuento_de_montos_en_exceso
    - Obligacion_verificar_declaracion_sira_estado_salida
    - Obligacion_verificar_declaracion_sirase_aprobada
    - Obligacion_demostrar_registro_ingreso_aduanero
    - Obligacion_certificacion_de_aplicacion_de_porcion_no_liquidada
    - Obligacion_ingreso_y_liquidacion_de_operacion
    - Obligacion_la_entidad_encargada_del_seguimiento_debera_verificar_el_cumplimiento_de_las_con
    - Obligacion_se_debera_contar_con_la_certificacion_de_la_entidad_que_curso_la_operacion_de_ca
    - Obligacion_responsabilidad_de_ingreso_y_liquidacion_de_divisas
    - Obligacion_computo_de_liquidaciones_de_divisas
    - Obligacion_plazo_de_ingreso_y_liquidacion_desde_cumplido_de_embarque
    - Obligacion_computo_de_monto_por_valor_fob_definitivo
    - Obligacion_imputacion_de_liquidaciones_entre_permisos
    - Obligacion_otorgamiento_de_cumplido_ante_demora_de_permiso_definitivo
    - Obligacion_cumplido_de_permiso_definitivo_asociado_a_embarque_anterior
    - Obligacion_registro_simultaneo_de_liquidacion_y_egreso
    - Obligacion_confeccion_de_boletos_de_operacion
    - Obligacion_el_exportador_debera_presentar_ante_la_entidad_encargada_de_seguimiento_document
    - Obligacion_cumplan_las_condiciones_previstas_en_el_punto_7_9_2
    - Obligacion_destinados_a_la_financiacion_de_proyectos_que_cumplen_las_condiciones_previstas_
    - Obligacion_la_entidad_debera_informar_la_asuncion_de_la_tarea_de_seguimiento_al_bcra
    - Obligacion_notificar_cambio_a_nueva_entidad
    - Obligacion_certificacion_de_liquidacion_o_excepcion
    - Obligacion_oficializacion_exportacion_ventaja_exponotitoneroso
    - Obligacion_documentacion_entrega_gratuita_de_bienes
    - Obligacion_declaracion_jurada_exportador_operatoria_gratuita
    - Obligacion_certificacion_auditor_externo_consistencia_declaraciones
    - Obligacion_declaracion_jurada_reembarco_zona_franca
    - Obligacion_declaracion_jurada_reexportacion_raf_rr01
    - Obligacion_certificacion_afectacion_reimportacion_sepaimpo
    - Obligacion_factura_exportacion_valor_neto_subregimen_ec03_eg03_ec04_eg13
    - Obligacion_la_documentacion_permite_constatar_que_la_entrega_de_la_mercaderia_exportada_se_
    - Obligacion_la_entidad_cuente_con_una_certificacion_emitida_por_una_entidad_en_la_que_conste
    - Obligacion_la_entidad_emisora_de_la_certificacion_debera_previamente_verificar_el_cumplimie
    - Obligacion_contar_con_una_declaracion_jurada_del_referido_agente_local_en_la_que_conste_que
    - Obligacion_en_caso_de_que_los_montos_hayan_sido_percibidos_en_moneda_extranjera_en_el_pais_
    - Obligacion_la_entidad_cuenta_con_documentacion_que_le_permite_constatar_que_la_operacion_de
    - Obligacion_en_el_caso_de_tratarse_de_una_operacion_encuadrada_en_el_decreto_492_23_la_entid
    - Obligacion_el_exportador_haya_demostrado_que_el_valor_a_afectar_corresponde_a_cobros_de_exp
    - Obligacion_la_entidad_debera_verificar_las_condiciones_indicadas_en_el_punto_9_3_1
    - Obligacion_la_entidad_debera_contar_con_la_documentacion_que_le_permita_verificar_el_cumpli
    - Obligacion_incluir_datos_minimos_en_certificacion
    - Obligacion_expresar_montos_en_moneda_liquidada
    - Obligacion_aplicar_normas_generales
    - Obligacion_supervision_del_bcra
    - Obligacion_la_descripcion_y_especificacion_completa_del_producto_y_o_servicio_debe_constar_
    - Obligacion_la_razon_social_cuit_y_domicilio_legal_del_sujeto_obligado_debe_constar_en_el_co
    - Obligacion_identificacion_del_usuario_de_servicios_financieros_nombres_y_apellidos_completo
    - Obligacion_las_comisiones_y_cargos_asi_como_los_terminos_y_condiciones_y_demas_circunstanci
    - Obligacion_en_el_caso_de_prestamos_hipotecarios_en_pesos_para_la_compra_de_vivienda_que_per
    - Obligacion_clausula_de_revocacion_en_donde_se_indique_que_el_usuario_tiene_derecho_a_revoca
    - Obligacion_la_facultad_de_revocacion_debe_ser_informada_al_usuario_en_todo_documento_que_le
    - Obligacion_el_derecho_del_usuario_de_efectuar_en_cualquier_momento_del_plazo_del_credito_la
    - Obligacion_el_derecho_del_usuario_de_realizar_operaciones_por_ventanilla_sin_restricciones_
    - Obligacion_el_contrato_debe_incluir_la_leyenda_usted_puede_consultar_el_regimen_de_transpar
    - Obligacion_el_derecho_de_solicitar_la_apertura_de_la_caja_de_ahorros_en_pesos_con_las_prest
    - Obligacion_cuando_se_genere_un_incremento_en_el_costo_total_de_los_restantes_productos_o_se
    - Obligacion_las_operaciones_que_se_pueden_realizar_con_el_producto_o_servicio_de_que_se_trat
    - Obligacion_los_aspectos_de_gratuidad_asociados_al_producto_o_servicio_contratado
    - Obligacion_las_bonificaciones_convenidas_las_condiciones_para_su_aplicacion_y_su_plazo_de_v
    - Obligacion_para_las_operaciones_de_financiacion_de_cualquier_tipo_todos_los_aspectos_contem
    - Obligacion_el_importe_del_capital_prestado_el_monto_total_a_pagar_la_cantidad_de_cuotas_per
    - Obligacion_los_limites_de_compra_de_compra_en_cuotas_de_financiacion_y_de_adelanto_de_diner
    - Obligacion_para_cuentas_de_depositos_y_tarjetas_de_credito_la_periodicidad_para_la_generaci
    - Obligacion_para_las_financiaciones_en_general_las_causales_los_efectos_de_la_mora_y_los_pro
    - Obligacion_las_facultades_procedimientos_y_canales_para_la_tramitacion_del_cierre_de_cuenta
    - Obligacion_la_facultad_de_revocacion_segun_lo_establecido_en_el_apartado_v_del_punto_2_3_1_
    - Obligacion_en_el_caso_de_multiproductos_paquetes_de_productos_se_debera_informar_las_cuenta
    - Obligacion_los_canales_habilitados_para_la_realizacion_de_reclamos
    - Obligacion_otras_cuestiones_particulares_que_impliquen_un_riesgo_inherente_para_el_usuario
    - Obligacion_en_el_contrato_deberan_encontrarse_taxativamente_especificadas_las_condiciones_q
    - Obligacion_los_incrementos_en_las_tasas_de_interes_comisiones_y_o_cargos_deben_ser_justific
    - Obligacion_en_el_caso_de_que_el_sujeto_obligado_pretenda_incorporar_nuevos_conceptos_en_cal
    - Obligacion_el_usuario_de_servicios_financieros_debe_ser_notificado_de_las_modificaciones_qu
    - Obligacion_las_notificaciones_por_cambios_de_condiciones_pactadas_seran_en_todos_los_casos_
    - Obligacion_las_notificaciones_deberan_efectuarse_mediante_documento_escrito_dirigido_al_dom
    - Obligacion_en_el_cuerpo_de_las_notificaciones_deberan_incluirse_la_leyenda_usted_podra_opta
    - Obligacion_garantizar_acceso_facil_a_informacion_en_sitio_web
    - Obligacion_la_informacion_incorporada_a_esta_base_de_datos_debera_conservarse_por_el_termin
    - Obligacion_en_el_registro_de_reintegros_de_importes_rri_se_deberan_asentar_los_montos_reint
    - Obligacion_en_el_registro_de_denuncias_ante_las_instancias_judiciales_y_o_administrativas_d
    - Obligacion_contribuir_a_la_mejora_de_los_mencionados_procesos_los_controles_relacionados_y_
    - Obligacion_proponer_al_directorio_o_autoridad_equivalente_a_los_funcionarios_para_el_desemp
    - Obligacion_participar_en_el_proceso_de_definicion_y_aprobacion_de_nuevos_productos_y_servic
    - Obligacion_verificar_el_adecuado_funcionamiento_del_proceso_de_analisis_de_las_causas_gener
    - Obligacion_evaluar_los_reportes_trimestrales_que_genere_el_responsable_de_atencion_al_usuar
    - Obligacion_evaluar_los_informes_emitidos_por_la_auditoria_interna_la_auditoria_externa_y_la
    - Obligacion_velar_por_el_cumplimiento_de_los_requerimientos_informativos_del_bcra_que_son_ma
    - Obligacion_elevar_al_directorio_o_autoridad_equivalente_como_minimo_trimestralmente_un_repo
    - Obligacion_para_el_caso_de_los_sujetos_obligados_no_alcanzados_por_la_obligacion_prevista_e
    - Obligacion_como_minimo_una_vez_al_ano_el_servicio_de_atencion_al_usuario_de_servicios_finan
    - Obligacion_la_auditoria_interna_debe_verificar_que_se_proporciona_a_los_usuarios_de_servici
    - Obligacion_se_debe_notificar_en_el_cuerpo_del_contrato_cuales_son_los_conceptos_sobre_los_c
    - Obligacion_se_debe_notificar_en_el_contrato_a_los_usuarios_de_servicios_financieros_sobre_l
    - Obligacion_los_registros_centralizados_de_consultas_y_reclamos_rccr_de_reintegros_de_import
    - Obligacion_el_sujeto_obligado_se_le_debera_informar_el_estado_del_tramite_cada_vez_que_lo_r
    - Obligacion_el_sujeto_obligado_debera_ante_la_solicitud_del_usuario_de_servicios_financieros
    - Obligacion_si_el_tramite_ha_finalizado_el_usuario_de_servicios_financieros_tendra_derecho_a
    - Obligacion_la_gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros_brindara
    - Obligacion_dando_orientacion_a_los_usuarios_de_servicios_financieros_sobre_la_manera_de_can
    - Obligacion_tambien_se_recibiran_de_los_usuarios_de_servicios_financieros_por_igual_via_come
    - Obligacion_indicar_datos_de_identificacion_en_reclamo
    - Obligacion_adjuntar_documentacion_de_identificacion
    - Obligacion_relatar_hechos_y_reclamo_previo
    - Obligacion_proveer_datos_de_identificacion_del_reclamo
    - Obligacion_acompanar_documentacion_del_reclamo
    - Obligacion_analizar_practicas_de_sujetos_obligados
    - Obligacion_remitir_presentaciones_a_autoridades_competentes
    - Obligacion_presentar_informacion_con_frecuencia_mensual
    - Obligacion_informar_ratio_de_apalancamiento
    - Obligacion_informar_riesgo_tasa_interes_eve
    - Obligacion_debera_presentarse_conciliacion_de_estados_contables_trimestrales_en_el_marco_de
    - Obligacion_de_reunir_los_requisitos_se_consignara_en_la_partida_60500000_la_porcion_pertine
    - Obligacion_se_consignara_como_numero_y_fecha_de_resolucion_la_de_la_comunicacion_a_6456_y_s
    - Obligacion_dichos_importes_se_consignaran_una_vez_computadas_las_facilidades_otorgadas_por_
    - Obligacion_cuando_se_trate_de_informacion_ingresada_fuera_de_termino_o_incumplimientos_dete
    - Obligacion_adicionalmente_se_computaran_los_siguientes_incrementos_exposicion_crediticia_re
    - Obligacion_se_registrara_el_incremento_calculado_por_la_entidad_aplicando_los_porcentajes_e
    - Obligacion_para_la_determinacion_de_la_exigencia_total_computable_del_periodo_n_se_consider
    - Obligacion_computar_datos_por_saldos_al_fin_del_periodo
    - Obligacion_informar_cargo_de_capital_dvp
    - Obligacion_consignar_exposiciones_ccp
    - Obligacion_se_reemplazaran_las_dos_ultimas_posiciones_de_cada_partida_de_exigencia_por_el_u
    - Obligacion_la_determinacion_de_esta_exigencia_se_efectuara_por_cada_moneda_a_cuyos_efectos_
    - Obligacion_de_corresponder_las_monedas_residuales_se_identificaran_con_codigo_de_moneda_999
    - Obligacion_este_riesgo_se_discriminara_por_mercado_entendido_a_estos_efectos_como_el_pais_e
    - Obligacion_informar_exigencia_de_capitales_por_riesgo
    - Obligacion_la_partida_correspondiente_al_bic_se_informara_por_el_importe_calculado_en_funci
    - Obligacion_cada_termino_dentro_de_los_3_componentes_y_el_resultado_monetario_debe_ser_infor
    - Obligacion_en_cuanto_a_los_activos_que_generan_intereses_sera_el_importe_que_surja_de_reexp
    - Obligacion_primero_se_debe_determinar_el_valor_de_las_partidas_netas_que_correspondan_por_e
Restriccion: 297 sin aplica_a
    - Restriccion_ecai_elegible_para_calificaciones
    - Restriccion_a_partir_del_01_02_13_comenzaran_a_excluirse_los_instrumentos_de_capital_que_dej
    - Restriccion_su_reconocimiento_como_rpc_se_limitara_al_90_del_valor_obtenido_a_partir_de_esa_
    - Restriccion_instrumentos_no_amortizables
    - Restriccion_instrumento_sin_obligacion_para_emisor
    - Restriccion_instrumento_con_derecho_residual
    - Restriccion_exclusion_de_acciones_estructuradas_de_replicacion_crediticia
    - Restriccion_efectivo_en_caja_en_transito_y_en_cajeros_automaticos_con_ponderador_de_riesgo_0
    - Restriccion_cuentas_corrientes_y_especiales_en_bcra_con_ponderador_de_riesgo_0
    - Restriccion_oro_amonedado_o_en_barras_con_ponderador_de_riesgo_0
    - Restriccion_efectivo_en_transito_de_cobro_con_ponderador_de_riesgo_20
    - Restriccion_exposicion_al_bcra_en_pesos_con_ponderador_de_riesgo_0
    - Restriccion_exposicion_a_gobiernos_locales_en_pesos_con_ponderador_de_riesgo_0
    - Restriccion_cuotas_de_financiaciones_no_deben_exceder_del_30_de_ingresos_del_deudor_al_momen
    - Restriccion_financiaciones_a_sector_publico_no_financiero_con_ponderador_de_riesgo_0
    - Restriccion_exposicion_a_bmd_que_cumplen_criterios_basilea_con_ponderador_0
    - Restriccion_exposicion_a_entidades_grupo_1_grado_a_con_ponderador_general_40
    - Restriccion_exposicion_de_corto_plazo_a_entidades_grupo_1_con_ponderador_20
    - Restriccion_empresas_con_grado_de_inversion_con_ponderador_de_riesgo_65
    - Restriccion_exposiciones_minoristas_transaccionales_con_ponderador_de_riesgo_45
    - Restriccion_apoyo_crediticio_que_no_supere_55_del_valor_del_inmueble_residencial_con_pondera
    - Restriccion_importe_que_supere_55_del_valor_inmueble_residencial_se_aplica_ponderador_de_con
    - Restriccion_hasta_55_del_valor_inmueble_comercial_se_aplica_el_menor_entre_60_o_ponderador_c
    - Restriccion_ccf_sustitutos_crediticios_directos
    - Restriccion_ccf_partidas_contingentes_comerciales
    - Restriccion_ccf_cartas_de_credito_comercial_corto_plazo
    - Restriccion_ccf_ventas_con_pacto_recompra
    - Restriccion_ccf_compromisos_adquisicion_activos
    - Restriccion_ccf_lineas_emision_titulos_corto_plazo
    - Restriccion_ccf_lineas_credito_comprometidas
    - Restriccion_ccf_compromisos_cancelables_discrecional
    - Restriccion_aplicacion_de_ccf_menor_en_compromisos
    - Restriccion_limite_de_deduccion_de_prevision_normal
    - Restriccion_aplicacion_del_mayor_ponderador_por_operacion
    - Restriccion_prohibicion_de_ponderador_menor_para_deudores_no_calificados
    - Restriccion_tratamiento_total_de_exposicion_en_incumplimiento
    - Restriccion_las_empresas_con_grado_de_inversion_son_aquellas_con_capacidad_suficiente_para_a
    - Restriccion_la_empresa_con_grado_de_inversion_o_su_controlante_debera_haber_emitido_titulos_
    - Restriccion_la_financiacion_especializada_de_grandes_proyectos_de_infraestructura_es_aquella
    - Restriccion_no_se_incluyen_los_proyectos_relacionados_con_la_actividad_inmobiliaria
    - Restriccion_la_financiacion_especializada_de_grandes_proyectos_de_infraestructura_debera_ten
    - Restriccion_un_proyecto_se_encuentra_en_etapa_preoperativa_si_a_el_ente_creado_para_gestiona
    - Restriccion_la_compensacion_no_estara_disponible_para_los_componentes_idiosincrasicos
    - Restriccion_no_deberan_existir_disposiciones_que_requieran_la_inmediata_liquidacion_de_los_a
    - Restriccion_los_derechos_del_inversor_deberan_estar_claramente_definidos_en_toda_circunstanc
    - Restriccion_el_ejercicio_de_dicha_opcion_no_sea_obligatorio_sino_que_este_sujeto_a_la_discre
    - Restriccion_la_opcion_de_exclusion_no_este_estructurada_con_el_fin_de_evitar_que_los_inverso
    - Restriccion_solo_pueda_ejercerse_cuando_quede_pendiente_un_10_o_menos_del_valor_original_de_
    - Restriccion_no_se_podra_aplicar_el_tratamiento_de_transparencia_look_through_si_se_trata_de_
    - Restriccion_los_activos_admitidos_como_garantia_se_limitan_a_los_especificados_en_los_puntos
    - Restriccion_los_garantes_admisibles_se_limitan_a_los_estipulados_en_el_punto_5_4_1_los_spe_n
    - Restriccion_los_instrumentos_utilizados_para_transferir_el_riesgo_de_credito_no_contienen_cl
    - Restriccion_la_entidad_financiera_originante_no_podra_excluir_las_exposiciones_objeto_de_tit
    - Restriccion_no_se_podra_reconocer_el_empleo_de_tecnicas_de_crc_para_la_cobertura_de_la_posic
    - Restriccion_factor_de_conversion_crediticia_ccf_100
    - Restriccion_exclusion_de_reservas_sin_mejora_crediticia
    - Restriccion_definicion_de_exposiciones_en_mora
    - Restriccion_ponderador_de_riesgo_1250
    - Restriccion_ajuste_de_k_para_desconocimiento_de_cumplimiento
    - Restriccion_una_titulizacion_se_considerara_simple_transparente_y_comparable_stc_si_se_trata
    - Restriccion_una_titulizacion_debe_involucrar_una_transferencia_real_de_activos_en_los_termin
    - Restriccion_los_criterios_stc_deberan_cumplirse_en_todo_momento
    - Restriccion_los_activos_subyacentes_deberan_estar_constituidos_por_documentos_a_cobrar_o_der
    - Restriccion_los_flujos_de_fondos_deberan_estar_contractualmente_identificados_ser_periodicos
    - Restriccion_las_tasas_de_interes_o_de_descuento_de_referencia_deberan_ser_tasas_de_interes_d
    - Restriccion_el_reembolso_a_los_inversores_en_la_titulizacion_debera_provenir_principalmente_
    - Restriccion_prohibicion_transferencia_activos_en_mora
    - Restriccion_prohibicion_gestion_activa_discrecional
    - Restriccion_prohibicion_retitulizaciones
    - Restriccion_el_pago_de_los_compromisos_de_una_titulizacion_no_debera_depender_de_la_venta_o_
    - Restriccion_los_unicos_derivados_admisibles_son_los_que_se_toman_para_la_genuina_cobertura_d
    - Restriccion_las_coberturas_que_no_se_realicen_a_traves_de_derivados_solo_seran_admisibles_si
    - Restriccion_ademas_deberan_estar_disponibles_y_haber_sido_integramente_fondeadas
    - Restriccion_los_titulos_valores_subordinados_no_deberan_tener_preferencia_de_pago_sobre_los_
    - Restriccion_la_titulizacion_no_debe_ser_estructurada_como_una_cascada_inversa_de_modo_que_lo
    - Restriccion_condicion_enfoque_lta_inversiones_subsiguientes
    - Restriccion_aplicacion_fba_en_inversiones_subsiguientes
    - Restriccion_tope_apalancamiento_ajustado
    - Restriccion_el_plazo_residual_sera_el_plazo_hasta_la_proxima_fecha_de_reformulacion
    - Restriccion_cuando_se_aplique_a_conjuntos_de_cobertura_de_derivados_sobre_bases_el_sf_corres
    - Restriccion_cuando_se_aplique_a_conjuntos_de_cobertura_de_operaciones_sobre_la_volatilidad_e
    - Restriccion_exposiciones_por_compras_en_cuotas_con_tarjeta_credito_hasta_25_11_21
    - Restriccion_demas_activos_y_partidas_fuera_de_balance
    - Restriccion_no_estan_comprendidas_las_exposiciones_originadas_en_operaciones_al_contado_que_
    - Restriccion_identico_criterio_se_aplicara_para_la_determinacion_del_periodo_de_mantenimiento
    - Restriccion_garantia_no_resguardada_en_nica
    - Restriccion_exencion_de_capital_para_garantias_protegidas
    - Restriccion_exencion_para_garantias_de_clientes_protegidas
    - Restriccion_ponderador_2_o_4_para_garantias_de_cliente_en_ccp
    - Restriccion_no_extension_automatica_por_cantidad_operaciones
    - Restriccion_no_se_permitira_descalce_de_plazos_bajo_metodo_simple
    - Restriccion_se_admite_descalce_de_monedas_al_emplear_metodo_simple_sin_tratamiento_adicional
    - Restriccion_los_garantes_y_contragarantes_admisibles_se_limitaran
    - Restriccion_salvo_impago_por_parte_del_comprador_de_la_proteccion_de_una_deuda_derivada_del_
    - Restriccion_debe_ser_incondicional_el_contrato_de_proteccion_no_debe_contener_ninguna_clausu
    - Restriccion_cuando_la_garantia_cubra_unicamente_el_capital_se_considerara_que_los_intereses_
    - Restriccion_para_permitir_descalce_a_la_obligacion_de_referencia_sea_de_categoria_similar_o_
    - Restriccion_el_periodo_de_vigencia_del_derivado_de_credito_no_podra_ser_inferior_a_cualquier
    - Restriccion_los_terminos_de_la_obligacion_subyacente_deberan_contemplar_que_el_consentimient
    - Restriccion_se_permite_un_descalce_entre_la_obligacion_subyacente_y_la_obligacion_utilizada_
    - Restriccion_si_el_importe_del_derivado_fuera_inferior_o_igual_al_de_la_obligacion_subyacente
    - Restriccion_solo_se_reconoceran_los_swaps_de_incumplimiento_crediticio_y_de_rendimiento_tota
    - Restriccion_no_podran_reconocerse_como_crc_otros_tipos_de_derivados_de_credito_incluyendo_a_
    - Restriccion_operaciones_de_financiacion_con_titulos_valores_que_cumplan_condiciones_pueden_r
    - Restriccion_las_operaciones_neteadas_deben_valuarse_diariamente_a_precios_de_mercado
    - Restriccion_los_activos_que_garanticen_operaciones_compensadas_deben_ser_activos_admitidos_e
    - Restriccion_las_franquicias_por_debajo_de_las_cuales_no_se_recibira_compensacion_en_caso_de_
    - Restriccion_de_haber_descalce_de_plazos_de_vencimiento_la_crc_que_tenga_un_plazo_de_vencimie
    - Restriccion_cuando_la_proteccion_crediticia_y_la_exposicion_esten_denominadas_en_distintas_m
    - Restriccion_el_valor_del_inmueble_se_corresponda_al_del_momento_del_otorgamiento
    - Restriccion_el_repago_de_las_financiaciones_no_debera_depender_significativamente_del_flujo_
    - Restriccion_los_prestamos_no_deberan_ser_destinados_a_empresas_o_entes_de_proposito_especial
    - Restriccion_reconocimiento_compensacion_parcial_riesgo
    - Restriccion_limitacion_reduccion_multiples_posiciones
    - Restriccion_prohibicion_compensacion_en_enesimo_incumplimiento
    - Restriccion_tratamiento_monedas_extranjeras_residuales
    - Restriccion_los_instrumentos_son_identicos_si_tienen_igual_emisor_cupon_moneda_y_vencimiento
    - Restriccion_para_compensacion_las_posiciones_deben_referirse_a_los_mismos_subyacentes_tener_
    - Restriccion_para_futuros_la_exclusion_procede_si_los_nocionales_e_instrumentos_subyacentes_r
    - Restriccion_la_tasa_de_referencia_debe_ser_identica_con_correspondencia_cercana_entre_cupone
    - Restriccion_para_swaps_fras_y_forwards_la_proxima_fecha_de_reajuste_debe_cumplir_menos_de_un
    - Restriccion_exclusion_de_acciones_preferidas
    - Restriccion_inclusion_limitada_efectos_gamma_negativos
    - Restriccion_limite_maximo_previsiones_por_incobrabilidad
    - Restriccion_deduccion_de_conceptos_deducibles_del_co_n1
    - Restriccion_deduccion_de_conceptos_deducibles_del_ca_n1
    - Restriccion_deduccion_de_conceptos_deducibles_del_pnc
    - Restriccion_el_importe_de_esta_rpc_que_sera_admisible_como_pnc_excluye_los_importes_reconoci
    - Restriccion_la_diferencia_positiva_resultante_de_comparar_el_importe_de_la_prevision_regulat
    - Restriccion_saldo_a_favor_por_aplicacion_del_impuesto_a_la_ganancia_minima_presunta_neto_de_
    - Restriccion_saldos_en_cuentas_de_corresponsalia_respecto_de_bancos_del_exterior_que_no_cumpl
    - Restriccion_titulos_de_credito_titulos_valores_certificados_de_depositos_a_plazo_fijo_y_otro
    - Restriccion_titulos_emitidos_por_gobiernos_de_paises_extranjeros_que_no_cumplan_con_lo_previ
    - Restriccion_titulos_valores_e_instrumentos_de_deuda_no_contemplados_en_los_puntos_8_4_1_19_y
    - Restriccion_accionistas
    - Restriccion_inmuebles_cualquiera_sea_la_fecha_de_su_incorporacion_al_patrimonio_destinados_o
    - Restriccion_activos_intangibles_netos_de_la_respectiva_depreciacion_acumulada_incluye_la_lla
    - Restriccion_partidas_pendientes_de_imputacion_saldos_deudores_otras
    - Restriccion_diferencias_por_insuficiencia_de_constitucion_de_las_previsiones_por_riesgo_de_i
    - Restriccion_registro_previo_en_estados_financieros
    - Restriccion_plazo_maximo_de_comunicacion_de_cambios
    - Restriccion_umbral_de_deuda_cliente_sector_privado
    - Restriccion_umbral_de_2_5_rpc_para_aprobacion
    - Restriccion_el_importe_a_considerar_sera_el_nivel_maximo_del_valor_de_ventas_totales_anuales
    - Restriccion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi
    - Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti
    - Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion
    - Restriccion_parametros_sectoriales_de_revision
    - Restriccion_en_los_casos_de_acuerdos_superiores_al_equivalente_a_2_5_veces_el_importe_de_ref
    - Restriccion_los_deudores_que_hayan_cancelado_la_totalidad_de_los_intereses_devengados_podran
    - Restriccion_los_deudores_que_no_hubieran_cancelado_por_lo_menos_los_intereses_devengados_den
    - Restriccion_los_deudores_que_hayan_recibido_credito_adicional_en_los_terminos_del_punto_2_2_
    - Restriccion_los_deudores_que_incurran_en_atrasos_de_mas_de_31_dias_respecto_de_las_condicion
    - Restriccion_no_interrumpir_computo_de_plazos
    - Restriccion_requisito_direccion_integra
    - Restriccion_requisito_sistema_de_informacion
    - Restriccion_requisito_sector_economico_viable
    - Restriccion_requisito_competitividad_y_tecnologia
    - Restriccion_restriccion_sobre_deudores_morosos
    - Restriccion_condiciones_pases_activos
    - Restriccion_restriccion_fondos_asistencia_crediticia
    - Restriccion_los_adelantos_transitorios_en_cuenta_corriente_se_consideraran_de_cumplimiento_n
    - Restriccion_los_deudores_que_hayan_refinanciado_sus_deudas_aun_no_habiendo_incurrido_en_atra
    - Restriccion_los_sobregiros_en_cuenta_corriente_bancaria_por_importes_que_excedan_los_margene
    - Restriccion_en_cuanto_a_la_situacion_juridica_del_deudor_se_considerara_si_mantiene_convenio
    - Restriccion_las_acreencias_en_conjunto_deben_representar_el_40_o_mas_del_total_informado_por
    - Restriccion_las_operaciones_no_comprendidas_en_el_punto_10_6_6
    - Restriccion_las_posiciones_arancelarias_de_los_bienes_no_correspondan_a_aquellas_comprendida
    - Restriccion_la_suma_de_los_pagos_anticipados_cursados_en_el_marco_de_este_punto_no_supera_el
    - Restriccion_la_suma_de_los_pagos_anticipados_a_la_vista_y_de_deuda_comercial_sin_registro_de
    - Restriccion_si_el_otorgamiento_de_la_financiacion_es_anterior_de_la_fecha_de_arribo_al_pais_
    - Restriccion_si_el_otorgamiento_de_la_financiacion_es_posterior_al_arribo_al_pais_de_los_bien
    - Restriccion_la_porcion_de_los_endeudamientos_financieros_que_sea_utilizada_en_virtud_de_lo_d
    - Restriccion_conformidad_previa_del_bcra_para_acceso_al_mercado_de_cambios
    - Restriccion_limite_de_deuda_para_mipyme
    - Restriccion_limite_de_pagos_en_mecanismos_especiales
    - Restriccion_pagos_sujetos_a_seguimiento
    - Restriccion_plazo_maximo_365_dias_para_financiacion_complementaria
    - Restriccion_para_cartas_de_credito_o_letras_avaladas_emitidas_u_otorgadas_a_partir_del_13_12
    - Restriccion_los_conceptos_mencionados_seran_aplicables_a_todo_monto_pagado_que_forme_parte_d
    - Restriccion_limite_de_multiples_despachos_de_importacion
    - Restriccion_seran_consideradas_las_condenas_dictadas_por_hasta_5_cinco_anos_anteriores_a_la_
    - Restriccion_hasta_cinco_prorrogas_sucesivas_de_hasta_180_dias_corridos
    - Restriccion_valor_adeudado_no_supere_equivalente_de_usd_100_000_cuando_se_usa_companias_de_s
    - Restriccion_si_el_importador_percibe_un_monto_en_moneda_extranjera_el_mismo_debera_ser_ingre
    - Restriccion_extension_de_plazos_no_superior_a_545_dias_corridos_para_pagos_anticipados_de_bi
    - Restriccion_prohibicion_de_cambio_sin_certificaciones_pendientes
    - Restriccion_limite_de_monto_a_superar
    - Restriccion_validez_de_certificaciones
    - Restriccion_prohibicion_de_cobro_de_comisiones_por_reporte
    - Restriccion_condiciones_previas_para_cesion_de_seguimiento
    - Restriccion_requisito_codificacion_conceptual_de_servicio
    - Restriccion_requisito_gastos_de_operatoria_habitual
    - Restriccion_requisito_fletes_de_exportacion_con_embarque
    - Restriccion_requisito_fletes_de_importacion
    - Restriccion_requisito_servicios_personales_de_contraparte_vinculada
    - Restriccion_requisito_plazo_90_dias_para_servicio_no_comprendido
    - Restriccion_requisito_plazo_contrapartes_vinculadas
    - Restriccion_la_porcion_del_endeudamiento_financiero_que_sea_utilizada_en_virtud_de_lo_dispue
    - Restriccion_se_requerira_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios
    - Restriccion_el_monto_total_de_sus_deudas_por_importaciones_de_bienes_y_servicios_previas_al_
    - Restriccion_los_pagos_por_deudas_de_bienes_o_servicios_realizados_en_el_marco_de_los_mecanis
    - Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o
    - Restriccion_limitacion_proporcion_capital_ingresado
    - Restriccion_limite_monto_acumulado_repatriaciones
    - Restriccion_restriccion_destino_garantia_endeudamientos
    - Restriccion_la_operacion_podra_incluir_bienes_que_no_revistan_la_condicion_de_bien_de_capita
    - Restriccion_la_normativa_alcanzada_por_la_estabilidad_cambiaria_contemplada_en_los_articulos
    - Restriccion_las_operaciones_de_cambio_en_divisas_extranjeras_seran_realizadas_al_tipo_de_cam
    - Restriccion_el_contravalor_de_la_exportacion_de_bienes_y_servicios_debera_ingresarse_al_pais
    - Restriccion_el_acceso_al_mercado_de_cambios_para_compra_de_moneda_extranjera_metales_precios
    - Restriccion_se_prohiben_practicas_y_operaciones_tendientes_a_eludir_a_traves_de_titulos_publ
    - Restriccion_excepcion_por_gastos_de_transferencia_internacional
    - Restriccion_limite_anual_usd_36_000_para_personas_humanas
    - Restriccion_acreditacion_en_cuenta_especial_decreto_679_22
    - Restriccion_validacion_de_cuentas_virtuales_autorizadas
    - Restriccion_plazo_maximo_liquidacion
    - Restriccion_los_montos_de_las_divisas_no_pueden_resultar_alcanzadas_por_ningun_otro_tratamie
    - Restriccion_el_monto_de_las_certificaciones_obtenidas_para_el_periodo_trimestral_de_referenc
    - Restriccion_los_cobros_de_exportaciones_que_pretenden_enmarcarse_en_este_mecanismo_no_fueron
    - Restriccion_instrumentacion_de_movimientos_a_cuenta_local
    - Restriccion_contraparte_no_residente_no_vinculada
    - Restriccion_beneficiario_no_residente_de_garantia
    - Restriccion_que_en_el_dia_en_que_solicita_el_acceso_al_mercado_y_en_los_90_dias_corridos_ant
    - Restriccion_los_requisitos_se_evaluan_en_el_dia_en_que_solicita_el_acceso_al_mercado_y_en_lo
    - Restriccion_el_compromiso_se_extiende_por_los_90_dias_corridos_subsiguientes_desde_que_requi
    - Restriccion_la_totalidad_de_los_fondos_obtenidos_de_ventas_se_haya_utilizado_o_sera_utilizad
    - Restriccion_el_plazo_para_la_liquidacion_de_divisas_no_debe_ser_posterior_a_la_fecha_hasta_l
    - Restriccion_no_deberan_considerarse_los_bienes_exportados_a_traves_de_operaciones_exceptuada
    - Restriccion_cuando_el_cliente_sea_beneficiario_del_decreto_277_22_los_montos_de_certificacio
    - Restriccion_la_nueva_entidad_quedara_habilitada_para_emitir_nuevas_certificaciones_una_vez_q
    - Restriccion_en_la_medida_que_se_encuentre_vigente_el_requisito_de_conformidad_previa_del_bcr
    - Restriccion_los_punitorios_u_otros_equivalentes_que_se_devenguen_desde_el_01_01_25_continuar
    - Restriccion_las_deudas_comprendidas_en_este_punto_continuaran_sujetas_a_la_conformidad_previ
    - Restriccion_cuando_el_emisor_de_la_tarjeta_sea_una_entidad_financiera_el_titular_podra_cance
    - Restriccion_operaciones_comerciales_con_brasil_no_podran_tener_plazo_de_pago_que_exceda_360_
    - Restriccion_las_transacciones_de_titulos_valores_concertadas_en_el_exterior_no_podran_liquid
    - Restriccion_contra_cable_sobre_cuentas_bancarias_a_nombre_del_cliente_en_una_entidad_del_ext
    - Restriccion_contra_cable_sobre_una_cuenta_de_terceros_en_el_exterior_que_no_se_encuentre_rad
    - Restriccion_la_venta_de_los_titulos_en_el_origen_de_la_operacion_no_debera_tenerse_en_cuenta
    - Restriccion_la_venta_no_habilitara_al_cliente_a_concretar_las_operaciones_de_titulos_valores
    - Restriccion_sujecion_a_disposiciones_de_compra_de_moneda_extranjera
    - Restriccion_plazo_de_destinacion_de_fondos
    - Restriccion_casa_matriz_en_pais_miembro_basilea
    - Restriccion_prohibicion_uso_para_operaciones_ilegales
    - Restriccion_recepcion_fondos_exclusivamente_infraestructura_financiera
    - Restriccion_plazo_maximo_de_liquidacion_contado
    - Restriccion_sujecion_a_norma_cambiaria
    - Restriccion_exclusion_de_activos_de_la_pgc
    - Restriccion_control_de_montos_en_exceso
    - Restriccion_fecha_minima_de_origen_financiacion
    - Restriccion_vencimiento_minimo_de_capital
    - Restriccion_vencimiento_final_minimo_de_365_dias
    - Restriccion_vencimiento_minimo_de_2_anos_para_titulos
    - Restriccion_plazo_aplicacion_fondos_120_dias
    - Restriccion_el_plazo_maximo_de_liquidacion_para_el_cobro_de_las_exportaciones_no_podra_exced
    - Restriccion_esta_opcion_estara_disponible_hasta_alcanzar_el_125_ciento_veinticinco_por_cient
    - Restriccion_el_exportador_haya_registrado_imputaciones_por_las_modalidades_admitidas_por_al_
    - Restriccion_la_entidad_podra_extender_el_plazo_hasta_los_120_ciento_veinte_dias_corridos_a_c
    - Restriccion_conformidad_previa_del_bcra_para_prefinanciaciones_anteriores
    - Restriccion_restriccion_de_otros_tratamientos_cambiarios_diferenciales
    - Restriccion_los_fondos_excedentes_del_125_deben_ser_ingresados_y_liquidados_en_el_mercado_de
    - Restriccion_su_vida_promedio_no_sea_inferior_a_1_un_ano_considerando_los_pagos_de_servicios_
    - Restriccion_fondos_hayan_sido_ingresados_y_liquidados_en_el_mercado_de_cambios_a_partir_del_
    - Restriccion_la_repatriacion_se_produzca_con_posterioridad_a_la_fecha_de_finalizacion_y_puest
    - Restriccion_su_vida_promedio_sea_no_inferior_a_2_anos_anos_y_el_primer_pago_de_capital_no_se
    - Restriccion_su_vida_promedio_sea_no_inferior_a_3_tres_anos_y_el_primer_pago_de_capital_no_se
    - Restriccion_su_emision_haya_tenido_lugar_entre_el_07_01_21_y_el_31_12_23
    - Restriccion_considerando_el_conjunto_de_la_operacion_la_vida_promedio_de_la_nueva_deuda_impl
    - Restriccion_con_una_vida_promedio_no_inferior_a_2_dos_anos
    - Restriccion_concertadas_a_partir_entre_el_09_10_20_y_el_31_12_23
    - Restriccion_no_podra_modificarse_voluntariamente_si_se_ha_producido_vencimiento_del_plazo_pa
    - Restriccion_procedimiento_de_cambio_cuando_la_entidad_nominada_opto_por_no_operar_en_comerci
    - Restriccion_requisito_de_documentacion_comercial
    - Restriccion_plazo_segun_mayor_proporcion_fob
    - Restriccion_ajuste_de_vencimiento_a_dia_habil
    - Restriccion_aplicacion_de_ampliacion_de_plazo
    - Restriccion_aplicacion_de_reduccion_de_plazo
    - Restriccion_limite_usd_25_000_para_imputacion_sin_divisas
    - Restriccion_el_exportador_y_el_importador_no_esten_vinculados_en_forma_directa_o_indirecta_d
    - Restriccion_la_entidad_debe_contar_con_documentacion_debidamente_certificada_que_acredite_la
    - Restriccion_en_caso_de_que_el_valor_fob_del_permiso_definitivo_resultase_inferior_al_valor_f
    - Restriccion_la_entidad_debera_contar_con_la_certificacion_de_liquidacion_emitida_por_la_enti
    - Restriccion_exportaciones_de_bienes_enviados_al_exterior_con_fines_promocionales_amparadas_p
    - Restriccion_el_agente_local_no_ha_utilizado_este_mecanismo_por_un_monto_superior_al_equivale
    - Restriccion_la_entidad_podra_considerar_cumplimentado_el_seguimiento_de_un_permiso_de_embarq
    - Restriccion_exclusion_de_cobros_de_exportacion
    - Restriccion_la_revocacion_sera_sin_costo_ni_responsabilidad_alguna_para_el_usuario_en_la_med
    - Restriccion_no_podran_aplicarse_comisiones_ni_cargos_por_contratacion_y_o_administracion_de_
    - Restriccion_no_podran_aplicarse_comisiones_ni_cargos_por_generacion_de_resumenes_de_cuenta_y
    - Restriccion_no_podran_aplicarse_comisiones_ni_cargos_por_evaluacion_otorgamiento_y_o_adminis
    - Restriccion_no_podran_aplicarse_comisiones_ni_cargos_por_gastos_de_tasacion_notariales_o_de_
    - Restriccion_la_modificacion_no_debe_alterar_el_objeto_del_contrato_ni_importar_un_desmedro_r
    - Restriccion_la_limitacion_de_comisiones_por_ventanilla_tambien_alcanza_en_las_casas_operativ
    - Restriccion_el_usuario_puede_informar_al_bcra_si_transcurre_el_plazo_de_diez_10_dias_habiles
    - Restriccion_suspension_envio_consolidacion_nivel_3
    - Restriccion_ratio_apalancamiento_consolidacion_nivel_3
```

## S12 — FAIL

ERROR — Toda Excepcion tiene >=1 arista saliente exceptua o exceptua_obligacion.

**Resultado:** 27 Excepciones sin salida exceptua/exceptua_obligacion.

```
    - Excepcion_debera_considerarse_dentro_del_concepto_cuotas_aquellas_que_el_cliente_tenga_por
    - Excepcion_el_tratamiento_otorgado_a_la_exposicion_al_sector_publico_no_financiero_no_sera_
    - Excepcion_con_excepcion_de_los_casos_contemplados_en_el_punto_4_1
    - Excepcion_los_deudores_por_pases_activos_ventas_a_termino_y_ventas_al_contado_a_liquidar_e
    - Excepcion_compras_a_termino_por_pases_pasivos_a_termino_no_vinculadas_a_pases_pasivos_y_al
    - Excepcion_primas_por_opciones_de_compra_y_de_venta_tomadas_estan_excluidas
    - Excepcion_anticipos_por_pago_de_jubilaciones_y_pensiones_estan_excluidos
    - Excepcion_anticipos_y_prestamos_al_fondo_de_garantia_de_los_depositos_estan_excluidos
    - Excepcion_obligaciones_negociables_compradas_emisiones_propias_estan_excluidas
    - Excepcion_creditos_frente_al_banco_central_de_la_republica_argentina_estan_excluidos
    - Excepcion_garantias_otorgadas_por_obligaciones_directas_estan_excluidas
    - Excepcion_garantias_otorgadas_a_favor_del_banco_central_estan_excluidas
    - Excepcion_activos_que_deben_deducirse_a_los_fines_del_calculo_de_la_responsabilidad_patrim
    - Excepcion_financiaciones_y_avales_fianzas_y_otras_responsabilidades_otorgados_por_sucursal
    - Excepcion_la_clasificacion_se_verifica_a_partir_del_momento_en_que_no_habiendo_sido_rechaz
    - Excepcion_sin_necesidad_de_contar_con_conformidad_previa_del_bcra_si_este_requisito_estuvi
    - Excepcion_excepcion_por_punto_3_13
    - Excepcion_pagos_a_contraparte_vinculada_sin_la_conformidad_previa_requerida_en_el_punto_3_
    - Excepcion_pagos_de_endeudamiento_cuyo_acreedor_sea_contraparte_vinculada_sin_la_conformida
    - Excepcion_si_la_financiacion_precancelada_por_el_cliente_hubiese_sido_otorgada_a_partir_de
    - Excepcion_pagar_a_la_fecha_de_cierre_de_la_operacion_de_recompra_y_o_rescate_sin_necesidad
    - Excepcion_cuando_el_cliente_sea_un_vehiculo_de_proyecto_unico_vpu_adherido_al_rigi_que_dec
    - Excepcion_exclusion_de_divisas_extranjeras
    - Excepcion_operaciones_exceptuadas
    - Excepcion_operaciones_aduaneras_especiales_exceptuadas_del_seguimiento_de_secoexpo_que_inc
    - Excepcion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid
    - Excepcion_los_requerimientos_relacionados_con_situaciones_que_hubieren_dado_lugar_a_accion
```

## Tabla resumen

| Regla | Resultado | Resumen |
|---|---|---|
| S1 | PASS | 6634/6634 aristas con relación válida; 0 violaciones. |
| S2 | PASS | 0 aristas colgantes sobre 6634. |
| S3 | PASS | 6634/6634 aristas conformes a firma; 0 violaciones. |
| S4 | PASS | Nodos OK: 4050/4050. Aristas OK: 6634/6634. Violaciones: 0. |
| S5 | PASS | Nodos con 'punto': 4050/4050. Aristas: 6634/6634. Violaciones: 0. |
| S6 | PASS | Archivos válidos (5): ['TO_capitales_minimos_actual.pdf', 'TO_clasificacion_deudores_actual.pdf', 'TO_exterior_cambios_actual.pdf', 'TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'TO_regimen_informativo_contable_mensual_actual.pdf']. Violaciones: 0. |
| S7 | FAIL | 48 grupos violatorios (103 nodos involucrados). |
| S8 | WARN | 8 grupos con el mismo label normalizado en types distintos. |
| S9 | FAIL | 53 nodos con ambas keys. |
| S10 | FAIL | Sin establecida_en: Obligacion=4, Restriccion=8, Excepcion=111 (total 123). |
| S11 | WARN | Sin aplica_a: Obligacion=458, Restriccion=297 (total 755). |
| S12 | FAIL | 27 Excepciones sin salida exceptua/exceptua_obligacion. |
