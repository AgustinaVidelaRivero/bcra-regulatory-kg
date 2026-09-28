# Validador de shapes — perfil congelado

- **Grafo:** `data/experiment/reextraccion_v2/corpus_tanda0/ens_cinco/r1/kg.json`
- **sha256 del grafo:** `4097d4fd3f300cb1c2cf09bef59e3ccb9a30b1de18334e6230102a5a3106d00a`
- **Fecha:** 2026-09-28
- **Nodos:** 1979
- **Aristas:** 3983
- **Perfil:** congelado
- **Vocabulario:** `/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/esq/code/prompt_congelado.py` — sha256 del prefijo `e69feaaa04779bd6347cc9e3974d2c1749519f1230e70a0459e66f46517cd720` (hash system+tools `1be8304e3d77`); 9 tipos, 13 predicados, enum Obligacion.tipo de 6 (retirados: requisito_de_estructura)
- **Catálogo de sujetos:** `data/experiment/esq_v3_miembros/esquema_v3_clases.json` — 101 ids (66 clases, 35 roles)
- **Veredicto global: NO PASA** — bloqueantes en FAIL: S19

## Bloqueantes

### S1 — PASS

Toda arista usa una relación admitida por el perfil congelado: los 13 predicados de PREDICATES_CONGELADO ∪ las 4 de esqueleto (subclase_de/miembro_de/instancia_de/parte_de) ∪ padre_sugerido (nombre normalizado).

**Resultado:** 3983/3983 aristas con relación admitida (18 relaciones admitidas); 0 violaciones.

Sin violaciones.

### S2 — PASS

Integridad referencial: origen y destino de toda arista existen como nodos.

**Resultado:** 0 aristas colgantes sobre 3983.

Sin violaciones.

### S3 — PASS

Toda arista respeta las firmas del perfil congelado: DOMAIN_RANGE_CONGELADO (Sujeto como pseudo-tipo) ∪ esqueleto solo Sujeto->Sujeto ∪ referencia nodo->nodo solo si rol_fuente=referencia_cruzada ∪ padre_sugerido solo de Sujeto propuesto a Sujeto clase|rol. La referencia TextoOrdenado->Comunicacion sigue por la matriz.

**Resultado:** 3983/3983 aristas conformes a firma; 0 violaciones. Evaluadas: 3337 por matriz, 117 de esqueleto, 11 padre_sugerido; 518 referencias nodo->nodo admitidas por rol_fuente.

Sin violaciones.

### S4 — PASS

Todo nodo y toda arista tienen provenance dict con al menos {to, archivo, punto, rol_documental}, provenances lista no vacía con provenance == provenances[0]; para rol_documental distinto de esqueleto, to y archivo no vacíos (para esqueleto se admiten to nulo, chunk_id nulo y paginas vacía).

**Resultado:** Nodos OK: 1979/1979. Aristas OK: 3983/3983. Violaciones: 0.

Sin violaciones.

### S5 — PASS

Todo provenance.punto (de nodo y de arista) es una string no vacía.

**Resultado:** Nodos con punto: 1979/1979. Aristas: 3983/3983. Violaciones: 0.

Sin violaciones.

### S6 — PASS

Todo provenance.archivo pertenece a {properties.archivo de los nodos TextoOrdenado} ∪ {archivo de las provenances con rol_documental=esqueleto}; nada codificado a mano.

**Resultado:** Archivos válidos (41): TextoOrdenado ['ctacte.pdf', 'docvig.pdf', 'lingob.pdf', 'pagjub.pdf', 'polcre.pdf'] ∪ esqueleto ['TO_capitales_minimos_actual.pdf', 'TO_clasificacion_deudores_actual.pdf', 'TO_exterior_cambios_actual.pdf', 'TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'TO_regimen_informativo_contable_mensual_actual.pdf', 'adrei.pdf', 'autenf.pdf', 'ccbcra.pdf', 'convca.pdf', 'cryl.pdf', 'ctacor.pdf', 'depaho.pdf', 'efemin.pdf', 'esquema_v2_clases.json', 'esquema_v3_clases.json', 'fabcra.pdf', 'icmecma.pdf', 'lavdin.pdf', 'ordcom.pdf', 'osapsa.pdf', 'pfmipyme.pdf', 'pimf.pdf', 'ratiofn.pdf', 'rdbcra.pdf', 'repefe.pdf', 'retype.pdf', 'rmrtsd.pdf', 'rrci.pdf', 'servco.pdf', 'snp_atm.pdf', 'snp_debin.pdf', 'snp_psp.pdf', 'snp_spd.pdf', 'snp_tr_nc.pdf', 'supcon.pdf', 'traval.pdf']. Violaciones: 0.

Sin violaciones.

### S15 — PASS

ERROR — Todo rol tiene miembro_de no vacío O figura en la lista declarada de roles sin miembro adjudicable; los miembros son clases del árbol; la cuenta declarada coincide con la medida.

**Resultado:** 35 roles, 51 aristas miembro_de; 12 huérfanos (12 declarados, 0 sin declarar); 0 miembros que no son clase. Lista declarada: 12 ({'sin_id_en_catalogo': 6, 'aplanamiento_rechazado': 5, 'instancia_rechazada': 1}).

```

Lista declarada (12 roles; por causa: {'sin_id_en_catalogo': 6, 'aplanamiento_rechazado': 5, 'instancia_rechazada': 1}):
    - Sujeto_rol_alcance_adrei
    - Sujeto_rol_alcance_autenf
    - Sujeto_rol_alcance_ordcom
    - Sujeto_rol_alcance_pagjub
    - Sujeto_rol_alcance_pfmipyme
    - Sujeto_rol_alcance_pimf
    - Sujeto_rol_alcance_ratiofn
    - Sujeto_rol_alcance_rdbcra
    - Sujeto_rol_alcance_repefe
    - Sujeto_rol_alcance_retype
    - Sujeto_rol_alcance_snp_atm
    - Sujeto_rol_alcance_traval
```

### S19 — FAIL

ERROR — Catálogo de sujetos: todo Sujeto tiene nivel ∈ {clase, instancia, rol, propuesto}; si nivel ≠ propuesto, su id está en el catálogo (clases ∪ roles) del artefacto de --excepciones; si nivel = propuesto, tiene properties.cuarentena y properties.padre_sugerido.

**Resultado:** 114 Sujetos ({'clase': 61, 'instancia': 7, 'propuesto': 11, 'rol': 35}); catálogo de 101 ids; 2 fuera del catálogo, 0 con nivel inválido, 0 propuestos incompletos.

```
Sujeto_entidad_depositaria (nivel clase): id fuera del catálogo
Sujeto_entidad_girada (nivel clase): id fuera del catálogo
```

### S20 — PASS

ERROR — Enum de Obligacion.tipo: para todo nodo Obligacion, properties.tipo ∈ {presentacion_informativa|calculo|asignacion|comunicacion_a_cliente|reporte_al_supervisor|otra}. Valores retirados (requisito_de_estructura) y otros valores fuera del enum se cuentan por separado; bloqueante si cualquiera de los dos es distinto de 0.

**Resultado:** 741/741 Obligaciones con tipo en el enum. Valores retirados: 0 ({}). Otros valores fuera del enum: 0 ({}).

Sin violaciones.

## Informativas

### S7 — FAIL

ERROR — Unicidad exacta: no puede haber dos nodos con el mismo (type, label normalizado).

**Resultado:** 5 grupos violatorios (10 nodos involucrados).

```
[Obligacion] 'acreditar comisiones en cuenta corriente' (2 nodos):
    - Obligacion_acreditar_en_la_cuenta_corriente_de_la_entidad_participante_las_comisiones_recon_385120  (label: 'Acreditar comisiones en cuenta corriente')
    - Obligacion_el_bcra_procedera_a_acreditar_en_la_cuenta_corriente_de_la_entidad_participante__01caa5  (label: 'Acreditar comisiones en cuenta corriente')
[Obligacion] 'ratificar personalmente denuncia en sucursal' (2 nodos):
    - Obligacion_ratificar_personalmente_en_el_dia_la_denuncia_en_cualquier_sucursal_de_la_entida_be9b6f  (label: 'Ratificar personalmente denuncia en sucursal')
    - Obligacion_ratificar_personalmente_en_el_dia_la_denuncia_en_cualquier_sucursal_de_la_entida_f6eff7  (label: 'Ratificar personalmente denuncia en sucursal')
[Operacion] 'presentacion de declaracion jurada' (2 nodos):
    - Operacion_presentacion_de_declaracion_jurada_3380c7  (label: 'Presentación de declaración jurada')
    - Operacion_presentacion_de_declaracion_jurada_3380c7__pagjub  (label: 'Presentación de declaración jurada')
[Restriccion] 'falta de especificacion — carencia de valor como cheque' (2 nodos):
    - Restriccion_el_titulo_respecto_del_que_falta_la_orden_pura_y_simple_de_pagar_una_suma_determ_81749a  (label: 'Falta de especificación — carencia de valor como cheque')
    - Restriccion_el_titulo_respecto_del_que_falte_la_especificacion_de_la_fecha_de_pago_segun_art_e4b468  (label: 'Falta de especificación — carencia de valor como cheque')
[Restriccion] 'prohibicion de nuevas presentaciones — titulos rechazados' (2 nodos):
    - Restriccion_los_titulos_devueltos_por_falta_de_especificaciones_incluida_la_falta_de_numero__472e6e  (label: 'Prohibición de nuevas presentaciones — títulos rechazados')
    - Restriccion_los_titulos_devueltos_por_falta_de_especificaciones_no_podran_ser_objeto_de_nuev_d5c604  (label: 'Prohibición de nuevas presentaciones — títulos rechazados')
```

### S8 — WARN

WARN — Colisión de label normalizado entre types distintos.

**Resultado:** 5 grupos con el mismo label normalizado en types distintos.

```
'alta gerencia' (2 nodos):
    - [Definicion] Definicion_alta_gerencia_9cd93f
    - [Sujeto] Sujeto_propuesto_alta_gerencia
'pago a la vista de cheques' (2 nodos):
    - [Obligacion] Obligacion_pagar_a_la_vista_excepto_en_los_casos_a_que_se_refiere_el_punto_1_5_2_8_segundo__e66bb1
    - [Operacion] Operacion_pago_a_la_vista_de_cheques_994ac8
'pago de beneficios anses' (2 nodos):
    - [Operacion] Operacion_pago_de_beneficios_anses_5e43b5
    - [TextoOrdenado] TextoOrdenado_pagjub_pdf
'presentacion de documento de viaje mercosur' (2 nodos):
    - [Obligacion] Obligacion_documento_de_viaje_admitido_por_la_decision_mercosur_en_vigencia_2ecadd
    - [Operacion] Operacion_presentacion_de_documento_de_viaje_mercosur_be2ab6
'reconocimiento de intereses sobre saldos acreedores' (2 nodos):
    - [Operacion] Operacion_reconocimiento_de_intereses_sobre_saldos_acreedores_ecab11
    - [Potestad] Potestad_reconocimiento_de_intereses_sobre_saldos_acreedores_ecab11
```

### S9 — PASS

ERROR — Descripción canónica: ningún nodo tiene a la vez 'descripcion' y 'description'.

**Resultado:** 0 nodos con ambas keys.

```
Tabla por type (usa cada key / ambas / ninguna):
  Comunicacion: descripcion=0, description=0, ambas=0, ninguna=5 (total 5)
  Condicion: descripcion=205, description=0, ambas=0, ninguna=0 (total 205)
  Definicion: descripcion=87, description=0, ambas=0, ninguna=0 (total 87)
  Excepcion: descripcion=76, description=0, ambas=0, ninguna=0 (total 76)
  Obligacion: descripcion=741, description=0, ambas=0, ninguna=0 (total 741)
  Operacion: descripcion=492, description=0, ambas=0, ninguna=0 (total 492)
  Potestad: descripcion=90, description=0, ambas=0, ninguna=0 (total 90)
  Restriccion: descripcion=164, description=0, ambas=0, ninguna=0 (total 164)
  Sujeto: descripcion=0, description=0, ambas=0, ninguna=114 (total 114)
  TextoOrdenado: descripcion=0, description=0, ambas=0, ninguna=5 (total 5)

Nodos con AMBAS keys (0):
```

### S10 — FAIL

ERROR — Todo nodo del dominio congelado de establecida_en (Condicion/Definicion/Excepcion/Obligacion/Operacion/Potestad/Restriccion) tiene >=1 arista saliente establecida_en.

**Resultado:** Sin establecida_en: Condicion=28, Definicion=1, Excepcion=2, Obligacion=0, Operacion=134, Potestad=0, Restriccion=0 (total 165).

```
Condicion: 28 sin establecida_en
    - Condicion_afectacion_de_solvencia_y_o_liquidez_de_la_entidad_adf5c6
    - Condicion_avales_o_garantias_totales_moneda_extranjera_9122cd
    - Condicion_cheque_con_faltas_de_ortografia_2afd5e
    - Condicion_cheques_de_pago_diferido_emitidos_antes_de_solicitud_76e7aa
    - Condicion_cheques_librados_sobre_cuentas_de_personas_juridicas_60b6c7
    - Condicion_concurso_preventivo_del_librador_declarado_judicialmente_ea91d8
    - Condicion_condicion_dimensiones_complejidad_importancia_y_perfil_de_riesgo_de_la_entidad_17426d
    - Condicion_consistencia_con_politica_de_incentivos_8c4453
    - Condicion_contratos_de_venta_en_firme_moneda_extranjera_e05324
    - Condicion_controlante_es_compania_holding_no_financiera_65965b
    - Condicion_cumplimiento_previo_puntos_7_2_2_y_o_7_2_3_0960f1
    - Condicion_declaracion_judicial_de_concurso_preventivo_del_librador_dccda7
    - Condicion_defectos_formales_no_corregidos_en_tiempo_y_forma_03904a
    - Condicion_endoso_sin_especificaciones_de_5_1_4_292eb1
    - Condicion_endosos_que_excedan_limite_establecido_e329fc
    - Condicion_existencia_de_conflicto_de_intereses_5f5757
    - Condicion_grupo_a_segun_clasificacion_autoridades_4521ad
    - Condicion_incapaces_declarados_judicialmente_a8b341
    - Condicion_inclusion_de_subsidiarias_exterior_por_recursos_pais_48fa07
    - Condicion_mayores_de_75_anos_al_31_12_14_d50022
    - Condicion_no_suscripcion_de_documentos_rechazados_0ff39c
    - Condicion_omision_de_informe_de_pago_de_multas_90915f
    - Condicion_operaciones_relativas_al_fideicomiso_0b3c5c
    - Condicion_perdida_o_robo_de_tarjeta_fcf462
    - Condicion_plazo_hasta_31_12_27_804a28
    - Condicion_presentacion_realizada_y_aceptada_hasta_vencimiento_periodo_9520d9
    - Condicion_sujeto_a_condiciones_punto_1_5_2_3_7666d3
    - Condicion_verificacion_cumplimiento_de_recaudos_9e410e
Definicion: 1 sin establecida_en
    - Definicion_causa_de_fuerza_mayor_impedimento_insalvable_b05d3a
Excepcion: 2 sin establecida_en
    - Excepcion_sin_perjuicio_de_los_conceptos_que_deban_trasladar_a_los_clientes_por_tributos_r_ab7589
    - Excepcion_sin_perjuicio_de_los_servicios_adicionales_para_facilitar_la_carga_masiva_de_dic_c4c7e6
Obligacion: 0 sin establecida_en
Operacion: 134 sin establecida_en
    - Operacion_acreditacion_a_cuenta_de_anses_a60951
    - Operacion_acreditacion_de_importes_en_el_dia_09b87b
    - Operacion_apertura_de_cuentas_no_presencial_64eef3
    - Operacion_apertura_de_cuentas_por_personas_inhabilitadas_f25a52
    - Operacion_aplicacion_de_capacidad_de_prestamo_de_depositos_04d844
    - Operacion_aplicacion_de_recursos_propios_liquidos_193f03
    - Operacion_aplicacion_financiamiento_instrumentos_deuda_tesoro_e1881e
    - Operacion_atencion_de_cheques_con_defecto_formal_cantidad_4410a3
    - Operacion_cancelacion_de_autorizaciones_para_girar_a26106
    - Operacion_canje_de_moneda_extranjera_por_pen_a2b943
    - Operacion_capacitacion_y_entrenamiento_de_ejecutivos_y_directivos_20f15b
    - Operacion_cheques_comunes_y_de_pago_diferido_vencidos_2ed72f
    - Operacion_cheques_de_pago_diferido_registrados_con_defectos_formales_23ea28
    - Operacion_cheques_firmados_por_todos_los_titulares_220f8a
    - Operacion_cierre_de_cuenta_6cadbb
    - Operacion_cierre_de_cuentas_96c948
    - Operacion_cierre_de_cuentas_de_inhabilitados_65d5df
    - Operacion_compra_de_moneda_extranjera_4818a4
    - Operacion_comunicacion_al_bcra_de_rechazos_de_cheques_f94818
    - Operacion_comunicacion_de_modificacion_baja_de_rechazo_al_bcra_39db45
    - Operacion_comunicacion_de_rechazo_al_tenedor_1fe229
    - Operacion_comunicacion_de_saldo_al_cuentacorrentista_fae6f0
    - Operacion_comunicacion_inmediata_de_contingencia_743b3d
    - Operacion_comunicacion_rechazo_al_bcra_189044
    - Operacion_comunicacion_rechazo_al_librador_y_avalistas_bd21f6
    - Operacion_consignacion_de_informacion_al_dorso_de_cheques_d59483
    - Operacion_creacion_de_cheque_con_firmas_multiples_ba7ce5
    - Operacion_cumplimiento_de_requerimientos_legajo_unico_financiero_y_economico_df59a6
    - Operacion_debito_de_importes_de_ordenes_de_pago_inconsistentes_e670ba
    - Operacion_debito_de_penalidades_de_cuenta_corriente_40ec27
    - Operacion_debitos_automaticos_sobre_cuentas_216901
    - Operacion_debitos_sin_autorizacion_previa_5335ea
    - Operacion_defectos_de_aplicacion_netos_en_efectivo_cba64e
    - Operacion_deposito_de_cheques_en_plazos_de_compensacion_f4b417
    - Operacion_deposito_de_echeq_en_dolares_estadounidenses_647d40
    - Operacion_deposito_de_garantias_de_futuros_y_opciones_2fa004
    - Operacion_deposito_electronico_de_cheques_e4cb2c
    - Operacion_deposito_en_casa_girada_con_constancia_identificatoria_af3e7d
    - Operacion_deposito_por_transferencia_ordenada_por_entidad_4dc733
    - Operacion_deposito_u_operacion_con_echeq_ca293f
    - Operacion_depositos_en_cuenta_especial_de_regularizacion_monedas_extranjeras_dc971c
    - Operacion_depositos_en_cuentas_especiales_financiacion_de_exportaciones_95e322
    - Operacion_depositos_mediante_cajeros_automaticos_273683
    - Operacion_direccion_de_actividades_y_negocios_2ce9a7
    - Operacion_disponibilidad_de_informacion_sobre_actividades_f2da83
    - Operacion_disponibilidad_publica_de_informacion_sobre_actividades_8e6a11
    - Operacion_efectivo_pago_del_beneficio_001d45
    - Operacion_eliminacion_de_cotitular_de_cuenta_52dbc7
    - Operacion_emision_de_cheque_c50f16
    - Operacion_emision_de_cheques_6cacff
    - Operacion_emision_de_cheques_comunes_dd9423
    - Operacion_emision_de_cheques_en_pesos_o_usd_143065
    - Operacion_emision_de_cheques_por_personas_inhabilitadas_828f10
    - Operacion_emision_de_constancia_de_operacion_8ad94c
    - Operacion_emision_y_cobro_de_cheques_de_pago_diferido_9adeda
    - Operacion_emision_y_presentacion_de_cheques_1f5d1a
    - Operacion_endoso_de_cheques_648af4
    - Operacion_entrega_copia_dni_al_legajo_f2a1d8
    - Operacion_entrega_de_tarjetas_magneticas_c89025
    - Operacion_envio_de_informacion_sobre_movimientos_y_cheques_00617c
    - Operacion_establecimiento_de_comite_lavado_de_activos_y_financiamiento_del_terrorismo_e5c850
    - Operacion_evaluacion_de_codigo_de_gobierno_societario_21418b
    - Operacion_exhibicion_de_documento_anterior_bfbc29
    - Operacion_exhibicion_dni_m_o_dni_d_post_rectificacion_0444ac
    - Operacion_extracciones_a_traves_de_cajeros_automaticos_47772f
    - Operacion_falta_de_firma_del_librador_7c504b
    - Operacion_gestion_de_cobro_por_tercero_cheque_al_portador_o_nominal_41dcea
    - Operacion_gestion_de_echeq_514051
    - Operacion_identificacion_evaluacion_monitoreo_control_y_mitigacion_de_riesgos_b095a3
    - Operacion_imputacion_a_capacidad_de_prestamo_depositos_moneda_extranjera_49ff53
    - Operacion_inhabilitacion_de_cuentacorrentistas_4c01ff
    - Operacion_interaccion_con_red_de_cajeros_automaticos_96c01d
    - Operacion_liberacion_de_echeq_3cdc48
    - Operacion_libramiento_de_cheques_por_ordenante_34c96f
    - Operacion_libramiento_visualizacion_gestion_echeq_9bc437
    - Operacion_liquidacion_de_incentivos_economicos_fbadf9
    - Operacion_liquidacion_de_la_rendicion_de_cuentas_d7f07b
    - Operacion_monitoreo_de_operaciones_290854
    - Operacion_no_registracion_de_cheques_de_pago_diferido_57bd1c
    - Operacion_obtencion_constancia_cuil_de_renaper_o_anses_deaeb7
    - Operacion_obtencion_copia_documento_de_identidad_con_cuil_92997e
    - Operacion_obtencion_electronica_directa_de_constancia_cuit_cdi_de_arca_14af7e
    - Operacion_operaciones_en_terminales_puntos_de_venta_7627ce
    - Operacion_otorgamiento_asistencia_financiera_a_controlante_ce1e2d
    - Operacion_otorgamiento_de_aval_sobre_cheques_diferidos_7593ac
    - Operacion_otorgamiento_de_financiaciones_a_personas_humanas_f27564
    - Operacion_otorgamiento_de_financiaciones_sector_publico_no_financiero_de6a1d
    - Operacion_otorgamiento_de_garantias_a_residentes_en_exterior_6fa98b
    - Operacion_otorgamiento_de_nuevas_financiaciones_996921
    - Operacion_pago_a_la_vista_de_cheques_994ac8
    - Operacion_pago_a_la_vista_de_cheques_de_pago_diferido_788bb6
    - Operacion_pago_de_beneficios_anses_5e43b5
    - Operacion_pago_de_cheque_de_pago_diferido_e58469
    - Operacion_pago_de_cheques_3a6175
    - Operacion_pago_de_multas_por_clientela_8044ba
    - Operacion_participacion_en_redes_de_cajeros_automaticos_2b11c3
    - Operacion_presentacion_al_cobro_o_deposito_de_cheque_pago_diferido_6140d4
    - Operacion_presentacion_de_cheque_af29cc
    - Operacion_presentacion_de_cheques_836940
    - Operacion_presentacion_de_devolucion_camara_compensadora_31de30
    - Operacion_presentacion_de_titulos_devueltos_f01e8a
    - Operacion_presentacion_de_titulos_sin_fecha_de_creacion_d299a0
    - Operacion_prevencion_conflictos_de_intereses_403c59
    - Operacion_publicacion_de_tasa_de_interes_efectiva_anual_b294ae
    - Operacion_publicacion_de_uva_y_uvi_2c0786
    - Operacion_realizacion_de_actividades_mediante_estructuras_societarias_o_jurisdicciones_ext_6411c8
    - Operacion_recepcion_de_cuadernos_de_cheques_f4fe64
    - Operacion_rechazo_de_cheque_con_autorizacion_verbal_422211
    - Operacion_rechazo_de_cheque_por_orden_judicial_510b14
    - Operacion_rechazo_de_cheques_e_informacion_de_identificacion_4ba2a7
    - Operacion_rechazo_de_cheques_sin_percepcion_de_multas_254eeb
    - Operacion_rechazo_de_pago_cheques_nominativos_cdf851
    - Operacion_rechazo_de_registracion_cheques_pago_diferido_15e2b7
    - Operacion_reconocimiento_de_intereses_sobre_saldos_acreedores_ecab11
    - Operacion_registracion_de_cheques_9375f0
    - Operacion_registracion_de_cheques_de_pago_diferido_b760f1
    - Operacion_registracion_de_cheques_diferidos_da95c8
    - Operacion_registro_de_cheques_de_pago_diferido_ce6a07
    - Operacion_remision_cheque_rechazado_al_juzgado_8b8383
    - Operacion_remision_de_cheque_rechazado_al_juzgado_bfcff5
    - Operacion_rendicion_de_cuentas_presentacion_tardia_2be202
    - Operacion_representacion_ante_camara_electronica_compensacion_e77be6
    - Operacion_retiro_de_tarjeta_magnetica_3a985e
    - Operacion_revocacion_de_autorizaciones_para_librar_cheques_346e4b
    - Operacion_solicitud_de_declaracion_jurada_debida_diligencia_ocde_cf4312
    - Operacion_transferencia_de_cheques_diferidos_para_negociacion_bursatil_8523f7
    - Operacion_transferencia_de_cheques_mediante_endoso_eae465
    - Operacion_transmision_de_certificado_por_endoso_6ff931
    - Operacion_transmision_integra_de_echeq_al_repositorio_c8cba5
    - Operacion_uso_de_nombre_apellido_rectificado_genero_499e51
    - Operacion_uso_de_tarjetas_magneticas_en_cajeros_automaticos_1361d1
    - Operacion_utilizacion_de_instrumentos_y_metodologia_de_pago_29c114
    - Operacion_verificacion_de_secuencia_numerica_de_cheques_y_formulas_a0b2a4
    - Operacion_vigilancia_del_sistema_de_incentivos_economicos_92765a
Potestad: 0 sin establecida_en
Restriccion: 0 sin establecida_en
```

### S11 — WARN

WARN — Todo nodo del dominio congelado de aplica_a (Excepcion/Obligacion/Operacion/Potestad/Restriccion) tiene >=1 arista saliente aplica_a.

**Resultado:** Sin aplica_a: Excepcion=59, Obligacion=53, Operacion=421, Potestad=21, Restriccion=35 (total 589).

```
Excepcion: 59 sin aplica_a
    - Excepcion_a_fin_de_ser_excluidas_de_la_central_de_cheques_rechazados_y_o_de_la_central_de__aa36bc
    - Excepcion_cheques_librados_a_favor_de_los_titulares_de_las_cuentas_sobre_las_que_se_giren__0595fc
    - Excepcion_con_la_expresa_autorizacion_del_titular_de_la_cuenta_corriente_se_libera_la_obli_6b56b8
    - Excepcion_cuando_las_cuentas_esten_abiertas_a_nombre_de_personas_juridicas_podra_establece_648d8b
    - Excepcion_cuando_no_sea_exigible_la_inscripcion_en_el_registro_publico_de_comercio_por_no__8972d4
    - Excepcion_de_existir_prueba_en_contrario_del_pais_de_domicilio_aplicara_el_punto_2_1_2_2ebd0e
    - Excepcion_dicho_pago_no_exime_a_la_entidad_de_las_responsabilidades_civiles_que_pudieren_c_a2081e
    - Excepcion_dichos_recaudos_se_consideraran_cumplidos_en_los_casos_en_que_la_gestion_de_pres_7791d9
    - Excepcion_el_rechazo_por_la_causal_de_presentacion_anterior_a_fecha_de_pago_no_impide_una__f52fda
    - Excepcion_en_caso_de_no_existir_dicha_jerarquia_la_pertinente_presentacion_estara_a_cargo__80a40c
    - Excepcion_en_el_supuesto_de_adulteracion_el_rechazo_del_cheque_no_se_comunicara_cuando_exi_48b261
    - Excepcion_excepto_cuando_la_entidad_lo_obtenga_en_forma_electronica_o_digital_conforme_a_l_e133ce
    - Excepcion_excepto_cuando_la_gestion_de_cobro_sea_realizada_por_una_entidad_financiera_no_a_4058e9
    - Excepcion_excepto_cuando_se_empleen_boletas_de_deposito_282797
    - Excepcion_excepto_en_los_casos_previstos_en_el_segundo_parrafo_del_punto_2_1_2_y_en_los_pu_cc4193
    - Excepcion_excepto_que_se_observe_en_materia_de_comisiones_y_o_cargos_las_mismas_condicione_7b89fd
    - Excepcion_haberse_dispuesto_medidas_cautelares_sobre_los_fondos_destinados_para_el_pago_de_daf62d
    - Excepcion_insuficiencia_de_fondos_de_no_haberse_dispuesto_la_medida_cautelar_conforme_a_lo_6aa0c9
    - Excepcion_la_correspondiente_a_las_sucursales_de_los_bancos_extranjeros_que_debera_remitir_d28a5f
    - Excepcion_la_devolucion_del_documento_no_aplica_cuando_la_entidad_otorgue_su_aval_f89156
    - Excepcion_la_falta_de_firma_del_librador_no_determina_la_carencia_de_valor_como_cheque_cua_58850b
    - Excepcion_la_falta_de_recepcion_por_parte_del_librador_o_del_cuentacorrentista_de_los_avis_6f5b56
    - Excepcion_la_obligacion_no_aplicara_cuando_se_trate_de_modificaciones_en_el_numero_de_docu_bf163e
    - Excepcion_las_modificaciones_en_el_nombre_y_o_apellido_de_las_personas_fisicas_o_en_otros__4fe2e3
    - Excepcion_lo_previsto_en_este_parrafo_no_sera_de_aplicacion_cuando_el_cliente_reuna_la_con_0cac32
    - Excepcion_los_cheques_emitidos_con_anterioridad_a_la_pertinente_notificacion_de_cierre_ser_c450c1
    - Excepcion_los_gastos_podran_ser_trasladados_al_cuentacorrentista_cuando_el_pedido_de_modif_30fc7b
    - Excepcion_los_instrumentos_tlac_computables_como_responsabilidad_patrimonial_computable_co_e8e08e
    - Excepcion_no_aplica_en_los_casos_a_que_se_refiere_el_punto_1_5_2_8_segundo_parrafo_172a80
    - Excepcion_no_aplica_la_obligacion_de_informar_al_bcra_en_la_situacion_prevista_en_los_dos__1efc3e
    - Excepcion_no_corresponde_el_pago_cuando_se_trate_de_rechazos_producidos_entre_la_fecha_de__16f6a1
    - Excepcion_no_corresponde_la_presentacion_de_esas_declaraciones_juradas_por_cada_una_de_las_8e76e4
    - Excepcion_no_correspondera_la_comunicacion_al_bcra_de_los_rechazos_motivados_por_falsifica_ba82ed
    - Excepcion_no_implica_la_inclusion_en_la_causal_a_que_se_refiere_el_punto_9_1_2_a809ff
    - Excepcion_no_procedera_la_inclusion_respecto_de_apoderados_para_el_uso_de_la_cuenta_corrie_811545
    - Excepcion_no_se_considerara_error_el_rechazo_del_cheque_respecto_del_cual_haya_mediado_aut_52b4bc
    - Excepcion_no_se_consideraran_las_exportaciones_industriales_comprendidas_en_acuerdos_inter_c85d60
    - Excepcion_no_sera_necesaria_la_presentacion_del_documento_anterior_47ab11
    - Excepcion_podran_cumplimentar_el_requisito_de_cuil_obteniendo_una_copia_simple_en_papel_o__d87a86
    - Excepcion_quedan_excluidos_aquellos_defectos_de_aplicacion_que_se_originen_en_operaciones__0510cf
    - Excepcion_resultaran_de_aplicacion_las_disposiciones_sobre_extravio_sustraccion_o_adultera_a08c1d
    - Excepcion_salvo_decision_de_autoridad_competente_que_obligue_al_cierre_inmediato_c9d545
    - Excepcion_salvo_lo_previsto_en_el_apartado_12_2_3_2_2e4f79
    - Excepcion_salvo_que_resulte_aplicable_el_procedimiento_de_truncamiento_en_cuyo_caso_se_est_ebd2e2
    - Excepcion_salvo_que_se_tratara_de_un_cheque_girado_entre_distintos_establecimientos_de_un__96ec1c
    - Excepcion_salvo_que_se_utilicen_escrituras_mecanizadas_de_seguridad_e01ac3
    - Excepcion_se_exceptua_la_prohibicion_cuando_se_trate_de_inversiones_en_titulos_publicos_ex_6792e8
    - Excepcion_se_exceptuan_cuando_los_cheques_se_depositen_en_la_caja_de_valores_s_a_para_ser__01f444
    - Excepcion_se_exceptuan_de_la_limitacion_los_endosos_que_las_entidades_financieras_realicen_7ad0de
    - Excepcion_se_exceptuan_los_endosos_a_favor_del_bcra_cb7ccc
    - Excepcion_se_exceptuan_los_endosos_efectuados_en_los_echeq_c256ed
    - Excepcion_se_excluiran_del_monto_de_ventas_totales_aquellas_realizadas_por_la_empresa_en_e_2ec8f1
    - Excepcion_se_presenten_irregularidades_en_la_cadena_de_endosos_c098cd
    - Excepcion_se_verifique_la_situacion_prevista_en_el_segundo_parrafo_del_punto_6_4_6_1_insuf_510979
    - Excepcion_sin_perjuicio_de_la_eventual_aplicacion_de_los_motivos_de_rechazo_previstos_en_l_a2b7a7
    - Excepcion_sin_perjuicio_de_los_conceptos_que_deban_trasladar_a_los_clientes_por_tributos_r_ab7589
    - Excepcion_sin_perjuicio_de_los_servicios_adicionales_para_facilitar_la_carga_masiva_de_dic_c4c7e6
    - Excepcion_sin_perjuicio_del_pago_parcial_que_podra_efectuar_la_entidad_conforme_a_lo_dispu_cedb2b
    - Excepcion_valores_a_favor_de_terceros_destinados_al_pago_de_sueldos_y_otras_retribuciones__f31349
Obligacion: 53 sin aplica_a
    - Obligacion_adicionalmente_se_insertara_alguna_de_las_siguientes_expresiones_en_procuracion__57172c
    - Obligacion_asesorara_al_directorio_sobre_los_riesgos_de_la_entidad_f71ea4
    - Obligacion_certificacion_judicial_en_original_que_acredite_haber_efectuado_la_pertinente_de_1dcd97
    - Obligacion_constatar_tanto_en_los_cheques_librados_en_formato_papel_como_en_los_certificado_70814c
    - Obligacion_controlar_que_los_niveles_gerenciales_tomen_los_pasos_necesarios_para_identifica_152bee
    - Obligacion_cuando_existe_saldo_deudor_el_cierre_debera_al_menos_poder_ser_realizado_en_form_649f63
    - Obligacion_de_tratarse_de_documentos_expedidos_en_lengua_no_espanola_se_requerira_que_se_lo_495e94
    - Obligacion_debera_abonarse_la_suma_de_90_por_cada_modificacion_de_computo_en_la_central_de__984436
    - Obligacion_debera_asegurarse_la_continuidad_de_los_derechos_y_obligaciones_referidos_a_dich_b961cb
    - Obligacion_debera_ofrecerse_la_utilizacion_de_mecanismos_electronicos_simples_eficaces_e_in_3dc8dd
    - Obligacion_documento_de_viaje_admitido_por_la_decision_mercosur_en_vigencia_2ecadd
    - Obligacion_documento_que_lo_identifique_en_el_pais_de_residencia_expedido_de_conformidad_co_e3c3a0
    - Obligacion_el_aviso_debe_consignar_el_caracter_con_el_que_fue_impuesto_d6a60a
    - Obligacion_el_banco_central_de_la_republica_argentina_publicara_periodicamente_el_valor_dia_7c841a
    - Obligacion_el_bcra_debe_debitar_de_la_cuenta_corriente_de_la_entidad_participante_el_import_9323d6
    - Obligacion_el_bcra_procedera_a_debitar_de_la_cuenta_corriente_de_la_entidad_participante_el_cae03c
    - Obligacion_el_bcra_procesara_el_cierre_de_las_rendiciones_de_cuentas_pendientes_de_las_enti_6a70fd
    - Obligacion_el_certificado_sera_transmisible_ilimitadamente_por_endoso_en_identicas_condicio_01ffc1
    - Obligacion_el_comite_de_auditoria_debera_coordinar_los_esfuerzos_de_las_auditorias_externa__ebf1b3
    - Obligacion_el_comite_debe_vigilar_el_diseno_del_sistema_de_incentivos_economicos_al_persona_0cc044
    - Obligacion_el_documento_debe_contar_en_su_caso_con_certificacion_notarial_040a8f
    - Obligacion_el_documento_debe_presentarse_legalizado_consularmente_o_por_el_sistema_de_apost_846bf4
    - Obligacion_el_interviniente_a_quien_le_corresponde_el_anadido_debera_firmar_abarcando_tanto_2229fa
    - Obligacion_en_las_clausulas_del_contrato_de_cuenta_corriente_debera_preverse_que_los_debito_b97c7c
    - Obligacion_en_los_demas_aspectos_vinculados_a_la_figura_del_endoso_rige_lo_dispuesto_en_la__4d862e
    - Obligacion_esos_dispositivos_deberan_informar_previamente_al_cliente_las_operaciones_admiti_7ae550
    - Obligacion_la_alta_gerencia_como_una_buena_practica_sera_responsable_de_e1d834
    - Obligacion_la_constancia_de_la_comunicacion_de_adhesion_podra_quedar_en_poder_de_la_empresa_8ff859
    - Obligacion_la_proporcion_del_incentivo_economico_diferido_no_percibido_se_ajustara_en_funci_98e106
    - Obligacion_la_tasa_de_interes_se_calculara_sobre_el_equivalente_en_pesos_que_surja_de_aplic_df226b
    - Obligacion_las_disposiciones_de_esta_seccion_tienen_como_objetivo_reducir_los_estimulos_hac_fed77c
    - Obligacion_las_entidades_conservaran_constancia_escrita_de_la_notificacion_a_los_clientes_s_bfaf9b
    - Obligacion_las_entidades_deberan_observar_el_procedimiento_detallado_en_los_puntos_9_2_1_1__48f1fd
    - Obligacion_las_subsidiarias_en_el_exterior_quedaran_comprendidas_en_la_medida_en_que_ellas__67d8a3
    - Obligacion_los_auditores_externos_tienen_el_deber_de_ejercer_la_debida_diligencia_profesion_b23f1b
    - Obligacion_los_beneficiarios_gozaran_de_un_trato_diferencial_como_clientes_con_prioridad_de_4bf42b
    - Obligacion_los_beneficiarios_tendran_acceso_a_todas_las_cajas_de_la_casa_o_sucursal_donde_l_4377c6
    - Obligacion_no_sera_obligatoria_para_el_cliente_la_entrega_de_las_constancias_del_cuit_cuil__f0df0b
    - Obligacion_obligacion_de_confidencialidad_a_que_se_refieren_las_leyes_de_entidades_financie_9565ec
    - Obligacion_pasaporte_del_pais_de_origen_71c048
    - Obligacion_pasaporte_del_pais_de_origen_de_corresponder_visado_por_autoridad_consular_argen_a387da
    - Obligacion_presentacion_de_fotocopias_autenticadas_por_escribano_publico_de_los_documentos__ab60fc
    - Obligacion_quedan_sometidos_sin_derecho_a_reclamo_alguno_los_interesados_3c2b6f
    - Obligacion_se_ajustara_a_los_terminos_de_la_pertinente_disposicion_d17145
    - Obligacion_se_aplicara_lo_previsto_por_el_articulo_261_de_la_ley_19_550_bb22ec
    - Obligacion_se_debera_admitir_como_minimo_la_utilizacion_de_la_banca_por_internet_home_banki_eee0b8
    - Obligacion_se_demostrara_con_cualquiera_de_las_siguientes_alternativas_05c68a
    - Obligacion_sera_de_aplicacion_lo_previsto_en_la_seccion_6_segun_corresponda_y_complementari_f8f83b
    - Obligacion_solo_se_requerira_la_exhibicion_del_dni_m_o_dni_d_expedido_con_posterioridad_a_l_ce22b2
    - Obligacion_tanto_los_directores_independientes_como_aquellos_que_no_reunan_esa_condicion_pe_ebc4d0
    - Obligacion_tasa_de_interes_sera_calculada_sobre_el_equivalente_que_surja_de_aplicar_lo_prev_9e4273
    - Obligacion_todo_mandato_se_entendera_subsistente_hasta_tanto_su_revocacion_se_notifique_feh_b15d3e
    - Obligacion_verificar_la_firma_del_presentante_que_debera_insertarse_con_caracter_de_recibo_b64f02
Operacion: 421 sin aplica_a
    - Operacion_abono_a_los_fondos_al_librador_cecc5d
    - Operacion_aceptacion_de_presentacion_sin_inconsistencias_86851e
    - Operacion_aceptacion_de_presentacion_tardia_e7bd41
    - Operacion_acreditacion_a_cuenta_de_anses_a60951
    - Operacion_acreditacion_de_categoria_de_residencia_9ebec5
    - Operacion_acreditacion_de_cuenta_de_anses_26f486
    - Operacion_acreditacion_de_importe_total_de_instrucciones_5b5386
    - Operacion_acreditacion_de_importes_en_el_dia_09b87b
    - Operacion_acreditacion_de_nuevos_beneficios_y_otros_conceptos_3d8eda
    - Operacion_acreditacion_en_cuenta_transitoria_bcra_3eb4fd
    - Operacion_actividades_realizadas_estructura_compleja_cc68c1
    - Operacion_actualizacion_de_saldos_mediante_cer_096e98
    - Operacion_acuerdo_y_desembolso_de_financiaciones_en_pesos_2fc758
    - Operacion_adhesion_al_servicio_de_debito_automatico_empresa_prestadora_ente_recaudador_e2fd0a
    - Operacion_administracion_de_central_de_cheques_denunciados_extraviados_sustraidos_adultera_901c1c
    - Operacion_administracion_de_central_de_cheques_rechazados_4daf92
    - Operacion_administracion_de_central_de_cuentacorrentistas_inhabilitados_ebf3d1
    - Operacion_adulteracion_de_cheques_d78211
    - Operacion_adulteracion_de_cheques_y_documentos_2e1d01
    - Operacion_adulteracion_o_falsificacion_de_cheque_o_firmas_8a9da9
    - Operacion_agregado_de_hojas_para_transmision_garantia_7bae64
    - Operacion_alquiler_de_cajas_de_seguridad_9f7062
    - Operacion_apertura_de_cuenta_a_agrupaciones_politicas_aliadas_64bc0b
    - Operacion_apertura_de_cuenta_corriente_39abbe
    - Operacion_apertura_de_cuenta_corriente_bancaria_8effda
    - Operacion_apertura_de_cuentas_componentes_o_representantes_legales_cec9a6
    - Operacion_apertura_de_cuentas_no_presencial_64eef3
    - Operacion_apertura_de_cuentas_por_personas_inhabilitadas_f25a52
    - Operacion_apertura_no_presencial_cuenta_personas_juridicas_fc2329
    - Operacion_apertura_no_presencial_de_cuentas_electronicas_d2b308
    - Operacion_aplicacion_de_capacidad_de_prestamo_de_depositos_04d844
    - Operacion_aplicacion_de_capacidad_de_prestamo_en_me_a_importaciones_4d39c5
    - Operacion_aplicacion_de_recursos_propios_liquidos_193f03
    - Operacion_aplicacion_financiamiento_instrumentos_deuda_tesoro_e1881e
    - Operacion_aportacion_a_agrupaciones_politicas_o_fondo_partidario_929d1c
    - Operacion_aprobacion_de_operaciones_y_nuevos_productos_b2cfdd
    - Operacion_arrendamiento_financiero_leasing_4ad213
    - Operacion_asistencia_financiera_a_personas_vinculadas_1a702c
    - Operacion_atencion_de_cheques_al_cobro_0499c7
    - Operacion_atencion_de_cheques_con_defecto_formal_cantidad_4410a3
    - Operacion_auditoria_externa_conclusion_sobre_estados_financieros_8b1e58
    - Operacion_aval_de_cheque_pago_diferido_por_banco_87123d
    - Operacion_calculo_de_intereses_sobre_capital_en_pesos_423bab
    - Operacion_calculo_de_tasa_de_interes_efectiva_anual_142d89
    - Operacion_calculo_y_pago_de_intereses_2bb65e
    - Operacion_cambio_de_clave_pin_por_usuario_b70e3c
    - Operacion_cambio_de_domicilio_o_correo_contacto_e6f6ad
    - Operacion_cancelacion_de_autorizaciones_para_girar_a26106
    - Operacion_cancelacion_de_multas_por_rechazos_41dbce
    - Operacion_canje_de_moneda_extranjera_por_pen_a2b943
    - Operacion_capacitacion_y_entrenamiento_de_ejecutivos_y_directivos_20f15b
    - Operacion_certificacion_de_cheque_3c9fac
    - Operacion_cheque_certificado_36f3da
    - Operacion_cheque_certificado_emision_becfc5
    - Operacion_cheques_comunes_y_de_pago_diferido_vencidos_2ed72f
    - Operacion_cheques_de_pago_diferido_registrados_con_defectos_formales_23ea28
    - Operacion_cheques_firmados_por_todos_los_titulares_220f8a
    - Operacion_cierre_de_cuenta_6cadbb
    - Operacion_cierre_de_cuenta_corriente_a948b4
    - Operacion_cierre_de_cuenta_transferencia_fondos_remanentes_75623f
    - Operacion_cierre_de_cuentas_96c948
    - Operacion_cierre_de_cuentas_de_inhabilitados_65d5df
    - Operacion_cierre_de_rendiciones_de_cuentas_a8b1e4
    - Operacion_composicion_de_cuadernos_cheques_comunes_y_diferidos_70e3e1
    - Operacion_compra_de_moneda_extranjera_4818a4
    - Operacion_compra_o_cesion_de_financiaciones_7c0f78
    - Operacion_comprobacion_de_rechazo_de_cheque_07ba39
    - Operacion_comunicacion_al_bcra_de_rechazos_de_cheques_f94818
    - Operacion_comunicacion_al_bcra_de_rechazos_f744de
    - Operacion_comunicacion_de_modificacion_baja_de_rechazo_al_bcra_39db45
    - Operacion_comunicacion_de_rechazo_al_tenedor_1fe229
    - Operacion_comunicacion_de_saldo_al_cuentacorrentista_fae6f0
    - Operacion_comunicacion_inmediata_de_contingencia_743b3d
    - Operacion_comunicacion_rechazo_al_bcra_189044
    - Operacion_comunicacion_rechazo_al_librador_y_avalistas_bd21f6
    - Operacion_consignacion_de_denominacion_de_cuenta_en_rechazo_259e1a
    - Operacion_consignacion_de_informacion_al_dorso_de_cheques_d59483
    - Operacion_consignacion_del_motivo_de_rechazo_del_cheque_88379f
    - Operacion_consignacion_judicial_de_cheques_rechazados_d33e1b
    - Operacion_consignacion_judicial_del_importe_de_multa_b1005b
    - Operacion_correccion_de_problemas_identificados_d1152f
    - Operacion_creacion_de_cheque_con_firmas_multiples_ba7ce5
    - Operacion_credito_por_internet_e0963d
    - Operacion_credito_por_orden_telefonica_f7e811
    - Operacion_credito_por_transferencia_electronica_b5597b
    - Operacion_creditos_a_residentes_exterior_desfases_de_liquidacion_2e3633
    - Operacion_creditos_internos_en_cuentas_c1e98d
    - Operacion_cuentas_a_la_vista_en_bancos_del_exterior_ca97e1
    - Operacion_cuentas_de_corresponsalia_en_bancos_del_exterior_1335da
    - Operacion_cumplimiento_de_requerimientos_legajo_unico_financiero_y_economico_df59a6
    - Operacion_cursamiento_de_cheque_a_entidad_girada_2aad10
    - Operacion_dar_aviso_de_adulteracion_de_cheque_electronico_caf952
    - Operacion_dar_aviso_de_extravio_de_cheque_emitido_en_papel_cc1d4b
    - Operacion_dar_aviso_de_extravio_de_formulas_de_cheques_9ca48a
    - Operacion_debito_al_momento_de_presentacion_ade7d0
    - Operacion_debito_automatico_de_resumen_de_tarjeta_70fd25
    - Operacion_debito_de_cuenta_corriente_5d0731
    - Operacion_debito_de_cuenta_corriente_de_entidad_participante_a022db
    - Operacion_debito_de_cuenta_corriente_entidad_participante_7ae441
    - Operacion_debito_de_cuenta_corriente_ordenes_impagas_972745
    - Operacion_debito_de_importe_generando_saldo_deudor_a7a570
    - Operacion_debito_de_importes_de_ordenes_de_pago_inconsistentes_e670ba
    - Operacion_debito_de_multas_por_rechazo_de_cheques_3192fb
    - Operacion_debito_de_penalidades_de_cuenta_corriente_40ec27
    - Operacion_debito_indebido_de_comisiones_y_o_cargos_971da4
    - Operacion_debitos_automaticos_sobre_cuentas_216901
    - Operacion_debitos_internos_29af09
    - Operacion_debitos_por_cheques_cancelatorios_b7c52e
    - Operacion_debitos_sin_autorizacion_previa_5335ea
    - Operacion_defectos_de_aplicacion_netos_en_efectivo_cba64e
    - Operacion_delegacion_de_actividades_en_terceros_1a17eb
    - Operacion_denuncia_de_extravio_sustraccion_o_adulteracion_f08c5d
    - Operacion_deposito_cheque_caja_de_valores_negociacion_cc4530
    - Operacion_deposito_cheque_en_entidad_receptora_3261a2
    - Operacion_deposito_de_certificados_en_cuenta_20b843
    - Operacion_deposito_de_cheques_en_plazos_de_compensacion_f4b417
    - Operacion_deposito_de_echeq_5082ae
    - Operacion_deposito_de_echeq_en_dolares_estadounidenses_647d40
    - Operacion_deposito_de_efectivo_en_pesos_463472
    - Operacion_deposito_de_efectivo_o_cheques_01c34d
    - Operacion_deposito_de_garantias_de_futuros_y_opciones_2fa004
    - Operacion_deposito_electronico_de_cheques_e4cb2c
    - Operacion_deposito_en_casa_girada_con_constancia_identificatoria_af3e7d
    - Operacion_deposito_en_cuenta_especial_de_cheques_diferidos_4284b2
    - Operacion_deposito_por_transferencia_ordenada_por_entidad_4dc733
    - Operacion_deposito_u_operacion_con_echeq_ca293f
    - Operacion_depositos_a_plazo_fijo_en_entidades_del_exterior_494e61
    - Operacion_depositos_en_cuenta_especial_de_regularizacion_monedas_extranjeras_dc971c
    - Operacion_depositos_en_cuentas_especiales_financiacion_de_exportaciones_95e322
    - Operacion_depositos_en_moneda_extranjera_financiacion_28cc03
    - Operacion_depositos_mediante_cajeros_automaticos_273683
    - Operacion_depositos_por_ventanilla_o_cajeros_automaticos_49464d
    - Operacion_desarrollo_aplicacion_reproduccion_firmas_digitalizadas_cbee12
    - Operacion_desembolsos_de_fondos_financiacion_20c454
    - Operacion_devolucion_de_chequeras_con_datos_anteriores_84ecf7
    - Operacion_devolucion_de_cheques_a_libradores_dae122
    - Operacion_devolucion_de_echeq_al_librador_por_tenedor_4c6f48
    - Operacion_direccion_de_actividades_y_negocios_2ce9a7
    - Operacion_diseno_del_sistema_de_incentivos_economicos_al_personal_56a391
    - Operacion_disponibilidad_de_informacion_sobre_actividades_f2da83
    - Operacion_disponibilidad_publica_de_informacion_sobre_actividades_8e6a11
    - Operacion_efectivo_pago_del_beneficio_001d45
    - Operacion_eliminacion_de_cotitular_de_cuenta_52dbc7
    - Operacion_emision_certificado_nominativo_transferible_97100d
    - Operacion_emision_cheques_firmas_electronicas_digitalizadas_38a3e1
    - Operacion_emision_cheques_papel_reproduccion_firmas_electronica_8be4d3
    - Operacion_emision_de_certificado_para_ejercicio_de_acciones_civiles_f202a4
    - Operacion_emision_de_cheque_c50f16
    - Operacion_emision_de_cheque_de_pago_diferido_no_registrado_1e40e0
    - Operacion_emision_de_cheques_6cacff
    - Operacion_emision_de_cheques_comunes_dd9423
    - Operacion_emision_de_cheques_de_pago_diferido_47a688
    - Operacion_emision_de_cheques_en_formato_papel_con_reproduccion_digital_7e191d
    - Operacion_emision_de_cheques_en_pesos_o_usd_143065
    - Operacion_emision_de_cheques_formato_papel_92cd41
    - Operacion_emision_de_cheques_por_personas_inhabilitadas_828f10
    - Operacion_emision_de_constancia_de_operacion_8ad94c
    - Operacion_emision_y_cobro_de_cheques_de_pago_diferido_9adeda
    - Operacion_emision_y_entrega_de_formula_de_certificacion_1dd04d
    - Operacion_emision_y_presentacion_de_cheques_1f5d1a
    - Operacion_endoso_11ba72
    - Operacion_endoso_a_favor_del_bcra_7d8af7
    - Operacion_endoso_de_cheques_648af4
    - Operacion_endoso_en_echeq_027661
    - Operacion_endoso_para_obtencion_de_financiacion_a381c7
    - Operacion_entrega_copia_dni_al_legajo_f2a1d8
    - Operacion_entrega_de_tarjetas_magneticas_c89025
    - Operacion_envio_de_informacion_sobre_movimientos_y_cheques_00617c
    - Operacion_establecimiento_de_comite_lavado_de_activos_y_financiamiento_del_terrorismo_e5c850
    - Operacion_evaluacion_de_codigo_de_gobierno_societario_21418b
    - Operacion_evaluacion_de_riesgos_de_la_entidad_2f697b
    - Operacion_evaluacion_gestion_directorio_y_renovacion_alta_gerencia_d0b9e8
    - Operacion_evaluacion_procesos_control_interno_94aa0c
    - Operacion_exclusion_de_central_de_inhabilitados_fab64b
    - Operacion_exhibicion_de_documento_anterior_bfbc29
    - Operacion_exhibicion_dni_d_en_formato_credencial_virtual_8985e2
    - Operacion_exhibicion_dni_m_o_dni_d_post_rectificacion_0444ac
    - Operacion_extension_al_portador_de_cheque_de_pago_diferido_c72ebd
    - Operacion_extension_de_plazo_de_prestamo_uvi_e6e225
    - Operacion_extraccion_de_efectivo_en_cajero_automatico_8d8d06
    - Operacion_extracciones_a_traves_de_cajeros_automaticos_47772f
    - Operacion_extravio_de_cheques_y_documentos_e17067
    - Operacion_falsificacion_de_cheques_2b8840
    - Operacion_falta_de_firma_del_librador_7c504b
    - Operacion_financiacion_de_prestadores_de_servicios_exportados_9dab89
    - Operacion_financiacion_de_proveedores_de_servicios_de_exportacion_71f51a
    - Operacion_financiacion_de_proyectos_inversion_ganaderia_bovina_66ab3e
    - Operacion_financiacion_de_unidades_de_vivienda_uvi_1c1cab
    - Operacion_financiacion_de_uva_cer_ley_25_827_756c14
    - Operacion_financiacion_en_cuotas_de_compras_de_clientes_310e5c
    - Operacion_financiaciones_a_exportadores_con_flujo_futuro_de_ingresos_be9e60
    - Operacion_financiaciones_a_productores_bienes_exportacion_984579
    - Operacion_financiaciones_a_proveedores_de_bienes_y_servicios_proceso_productivo_3bbeee
    - Operacion_financiaciones_con_garantias_en_moneda_extranjera_11bef7
    - Operacion_financiaciones_destinos_no_previstos_2_1_1_a_2_1_6_6d6ec0
    - Operacion_financiaciones_directas_11e86a
    - Operacion_financiamiento_con_destino_comercio_exterior_7a28bb
    - Operacion_firma_electronica_en_echeq_39abe8
    - Operacion_funcion_de_auditoria_externa_3cb938
    - Operacion_funcion_de_auditoria_interna_b303ae
    - Operacion_gestion_de_cobro_por_tercero_cheque_al_portador_o_nominal_41dcea
    - Operacion_gestion_de_echeq_514051
    - Operacion_gestion_de_operaciones_y_riesgos_eba575
    - Operacion_gestion_de_registro_formato_papel_a6b85b
    - Operacion_giro_sobre_el_librador_0e2548
    - Operacion_giros_en_descubierto_a88209
    - Operacion_identificacion_de_denunciantes_mediante_documentos_40e459
    - Operacion_identificacion_de_presentante_cheque_papel_6a3d2c
    - Operacion_identificacion_evaluacion_monitoreo_control_y_mitigacion_de_riesgos_b095a3
    - Operacion_implementacion_procedimientos_gobierno_corporativo_4bd8aa
    - Operacion_imputacion_a_capacidad_de_prestamo_depositos_moneda_extranjera_49ff53
    - Operacion_imputacion_de_financiaciones_incorporadas_12bd29
    - Operacion_inclusion_en_central_de_cheques_denunciados_b68f29
    - Operacion_inclusion_en_central_de_cuentacorrentistas_inhabilitados_18cee7
    - Operacion_inclusion_en_central_de_inhabilitados_579dc0
    - Operacion_incorporacion_de_carteras_por_titulos_o_participaciones_59dbe7
    - Operacion_incorporacion_en_centrales_de_cheques_rechazados_e_inhabilitados_7fff4f
    - Operacion_inhabilitacion_de_cuentacorrentistas_4c01ff
    - Operacion_insercion_de_firma_en_cheque_para_cobro_o_deposito_761507
    - Operacion_interaccion_con_red_de_cajeros_automaticos_96c01d
    - Operacion_letras_y_notas_del_bcra_en_usd_3f1a26
    - Operacion_leyenda_en_devolucion_sin_registrar_647831
    - Operacion_liberacion_de_echeq_3cdc48
    - Operacion_libra_de_cheque_en_formato_papel_1dab7d
    - Operacion_libra_de_cheque_por_medios_electronicos_8ce589
    - Operacion_libracion_de_echeq_alegado_adulterado_905882
    - Operacion_libramiento_cheques_por_medios_electronicos_echeq_a00814
    - Operacion_libramiento_de_cheques_por_medios_electronicos_a29146
    - Operacion_libramiento_de_cheques_por_ordenante_34c96f
    - Operacion_libramiento_de_cheques_por_titulares_75e120
    - Operacion_libramiento_visualizacion_gestion_echeq_9bc437
    - Operacion_libramiento_y_o_gestion_de_echeq_3b1d76
    - Operacion_lineas_de_credito_a_bancos_del_exterior_facilitar_exportaciones_86d363
    - Operacion_liquidacion_de_incentivos_economicos_fbadf9
    - Operacion_liquidacion_de_la_rendicion_de_cuentas_d7f07b
    - Operacion_modificacion_de_computo_en_central_de_cheques_rechazados_462cd3
    - Operacion_modificacion_de_comunicaciones_de_rechazo_a2506c
    - Operacion_modificacion_de_condiciones_de_cuenta_corriente_be52c3
    - Operacion_modificacion_de_sistema_aprobado_42a6a7
    - Operacion_modificacion_del_numero_de_dni_103764
    - Operacion_modificacion_nombre_y_o_apellido_88e879
    - Operacion_monitoreo_de_operaciones_290854
    - Operacion_movimientos_de_fondos_derivados_rendicion_ff9b77
    - Operacion_movimientos_de_fondos_segun_presentacion_aceptada_5e3e58
    - Operacion_negociacion_bursatil_de_cheques_de_pago_diferido_7ce672
    - Operacion_negociacion_de_cheques_diferidos_af0737
    - Operacion_no_emision_de_comprobante_en_cajero_8448bf
    - Operacion_no_registracion_de_cheques_de_pago_diferido_57bd1c
    - Operacion_obligaciones_negociables_516ebb
    - Operacion_obtencion_constancia_cuil_de_renaper_o_anses_deaeb7
    - Operacion_obtencion_copia_documento_de_identidad_con_cuil_92997e
    - Operacion_obtencion_electronica_directa_de_constancia_cuit_cdi_de_arca_14af7e
    - Operacion_operaciones_a_traves_de_cajeros_automaticos_63fb57
    - Operacion_operaciones_con_subsidiarias_y_vinculados_add23d
    - Operacion_operaciones_en_terminales_puntos_de_venta_7627ce
    - Operacion_operaciones_por_ventanilla_ebfe32
    - Operacion_operar_con_directores_administradores_y_vinculados_967f5e
    - Operacion_otorgamiento_asistencia_financiera_a_controlante_ce1e2d
    - Operacion_otorgamiento_de_aval_sobre_cheques_diferidos_7593ac
    - Operacion_otorgamiento_de_financiaciones_sector_publico_no_financiero_de6a1d
    - Operacion_otorgamiento_de_garantias_a_residentes_en_exterior_6fa98b
    - Operacion_otorgamiento_de_incentivos_economicos_al_personal_1475cd
    - Operacion_otorgamiento_de_nuevas_financiaciones_996921
    - Operacion_otorgamiento_de_prestamo_pesos_variable_e4718d
    - Operacion_pago_a_la_vista_de_cheques_994ac8
    - Operacion_pago_a_la_vista_de_cheques_de_pago_diferido_788bb6
    - Operacion_pago_de_beneficios_anses_5e43b5
    - Operacion_pago_de_cheque_2a306d
    - Operacion_pago_de_cheque_cruzado_1b1710
    - Operacion_pago_de_cheque_de_pago_diferido_e58469
    - Operacion_pago_de_cheques_3a6175
    - Operacion_pago_de_cheques_de_ventanilla_1373fd
    - Operacion_pago_de_incentivo_economico_variable_diferido_732465
    - Operacion_pago_de_incentivos_economicos_al_personal_c0a655
    - Operacion_pago_de_multas_por_clientela_8044ba
    - Operacion_pago_de_ordenes_de_beneficios_anses_cad97b
    - Operacion_pago_de_prestamos_1dedfd
    - Operacion_pago_en_efectivo_de_cheques_e129b8
    - Operacion_pago_por_otro_medio_convenido_816153
    - Operacion_participacion_en_redes_de_cajeros_automaticos_2b11c3
    - Operacion_participacion_vinculacion_con_empresa_cajeros_e60ea3
    - Operacion_pases_y_cauciones_bursatiles_tomadas_en_pesos_7ccdb7
    - Operacion_percepcion_de_comisiones_cajero_automatico_277e95
    - Operacion_prefinanciacion_de_exportaciones_directas_d6d123
    - Operacion_presentacion_a_registro_de_cheques_0f95f8
    - Operacion_presentacion_al_cobro_cheque_en_formato_papel_19a208
    - Operacion_presentacion_al_cobro_de_cheques_510eec
    - Operacion_presentacion_al_cobro_de_dpf_a76156
    - Operacion_presentacion_al_cobro_de_echeq_c766b6
    - Operacion_presentacion_al_cobro_o_deposito_de_cheque_pago_diferido_6140d4
    - Operacion_presentacion_cheque_cobro_endosos_c0a9e9
    - Operacion_presentacion_cheque_para_cobro_3dcb57
    - Operacion_presentacion_constancia_cuit_6ac1e6
    - Operacion_presentacion_de_certificados_al_cobro_f41b1d
    - Operacion_presentacion_de_cheque_af29cc
    - Operacion_presentacion_de_cheque_mediante_depositaria_37c3ac
    - Operacion_presentacion_de_cheque_papel_al_cobro_a00f84
    - Operacion_presentacion_de_cheque_sin_especificaciones_requeridas_3d65e7
    - Operacion_presentacion_de_cheques_836940
    - Operacion_presentacion_de_cheques_al_cobro_1355fc
    - Operacion_presentacion_de_datos_identificatorios_aea2f8
    - Operacion_presentacion_de_declaracion_jurada_3380c7
    - Operacion_presentacion_de_declaracion_jurada_3380c7__pagjub
    - Operacion_presentacion_de_devolucion_camara_compensadora_31de30
    - Operacion_presentacion_de_documento_de_identidad_35714b
    - Operacion_presentacion_de_documento_de_viaje_mercosur_be2ab6
    - Operacion_presentacion_de_fases_rendicion_cuentas_4cf6a8
    - Operacion_presentacion_de_informacion_rendicion_de_cuentas_4b1114
    - Operacion_presentacion_de_informes_al_bcra_5fc76c
    - Operacion_presentacion_de_libreta_de_enrolamiento_9874e4
    - Operacion_presentacion_de_nota_con_datos_minimos_5725a8
    - Operacion_presentacion_de_nota_de_designacion_al_bcra_0b6b85
    - Operacion_presentacion_de_pasaporte_del_pais_de_origen_b199ab
    - Operacion_presentacion_de_rendicion_de_cuentas_b26ee5
    - Operacion_presentacion_de_titulo_como_cheque_c6f02e
    - Operacion_presentacion_de_titulos_devueltos_f01e8a
    - Operacion_presentacion_de_titulos_sin_fecha_de_creacion_d299a0
    - Operacion_presentacion_declaracion_jurada_rendicion_cuentas_c46e93
    - Operacion_presentacion_del_cartular_o_certificado_para_ejercicio_de_acciones_civiles_f33669
    - Operacion_presentacion_documento_nacional_de_identidad_digital_ceed70
    - Operacion_presentacion_electronica_de_cheques_al_cobro_155bae
    - Operacion_presentacion_instrumento_constitutivo_sas_499c56
    - Operacion_presentacion_por_mandatario_888151
    - Operacion_presentacion_rendicion_de_cuentas_periodo_tardio_1676e6
    - Operacion_prestamos_interfinancieros_imputacion_6f2e6a
    - Operacion_prestamos_uva_cartera_comercial_0edfd2
    - Operacion_prevencion_conflictos_de_intereses_403c59
    - Operacion_procesamiento_de_informacion_de_presentacion_6ac656
    - Operacion_procesamiento_de_informacion_rendicion_cuentas_544df2
    - Operacion_publicacion_de_tasa_de_interes_efectiva_anual_b294ae
    - Operacion_publicacion_de_uva_y_uvi_2c0786
    - Operacion_radicacion_de_cuenta_abierta_no_presencial_8e4535
    - Operacion_realizacion_de_actividades_mediante_estructuras_societarias_o_jurisdicciones_ext_6411c8
    - Operacion_realizacion_de_auditoria_externa_b2d66c
    - Operacion_realizacion_de_operaciones_diarias_984295
    - Operacion_recepcion_de_cuadernos_de_cheques_f4fe64
    - Operacion_recepcion_de_denuncia_de_extravio_bancaria_213316
    - Operacion_rechazo_cheque_defectos_formales_599818
    - Operacion_rechazo_cheque_insuficiencia_fondos_dedc32
    - Operacion_rechazo_de_cheque_207cc3
    - Operacion_rechazo_de_cheque_comun_o_diferido_a36303
    - Operacion_rechazo_de_cheque_con_autorizacion_verbal_422211
    - Operacion_rechazo_de_cheque_por_orden_judicial_510b14
    - Operacion_rechazo_de_cheque_por_plazo_vencido_8a9566
    - Operacion_rechazo_de_cheques_171a7c
    - Operacion_rechazo_de_cheques_e_informacion_de_identificacion_4ba2a7
    - Operacion_rechazo_de_cheques_por_suspension_de_servicio_de_pago_2d9fda
    - Operacion_rechazo_de_cheques_sin_percepcion_de_multas_254eeb
    - Operacion_rechazo_de_pago_cheques_nominativos_cdf851
    - Operacion_rechazo_de_registracion_cheques_pago_diferido_15e2b7
    - Operacion_rechazo_de_registracion_de_cheque_c58de6
    - Operacion_rechazo_echeq_dolares_estadounidenses_e7daec
    - Operacion_rechazo_registracion_cheque_diferido_a909be
    - Operacion_reconocimiento_de_intereses_sobre_saldos_acreedores_ecab11
    - Operacion_reconocimiento_de_tasas_de_interes_613a08
    - Operacion_rectificacion_datos_documentos_compensables_f7b2e2
    - Operacion_rectificacion_de_datos_de_identificacion_5210d9
    - Operacion_rectificacion_de_documentos_de_identidad_05f84f
    - Operacion_rectificacion_registral_de_sexo_nombre_ley_26_743_f6a4a6
    - Operacion_recuperacion_de_identidad_resolucion_judicial_bfcf03
    - Operacion_reembolso_de_capital_en_pesos_equivalentes_90baf8
    - Operacion_reembolso_de_capital_en_uvi_eae046
    - Operacion_reemplazo_de_tarjetas_de_debito_e73b43
    - Operacion_registracion_de_cheques_9375f0
    - Operacion_registracion_de_cheques_de_pago_diferido_b760f1
    - Operacion_registracion_de_cheques_diferidos_da95c8
    - Operacion_registro_de_cheque_de_pago_diferido_50f333
    - Operacion_registro_de_cheques_de_pago_diferido_ce6a07
    - Operacion_registro_de_novedad_en_repositorio_echeq_ab3fde
    - Operacion_registro_de_tenencias_de_instrumentos_tlac_78f227
    - Operacion_registro_del_cheque_de_pago_diferido_9eb22a
    - Operacion_registro_en_cuenta_corriente_o_cuenta_especial_eacb55
    - Operacion_remision_a_traves_de_casa_central_11058a
    - Operacion_remision_cheque_rechazado_al_juzgado_8b8383
    - Operacion_remision_de_cheque_rechazado_al_juzgado_bfcff5
    - Operacion_rendicion_de_cuentas_presentacion_tardia_2be202
    - Operacion_rendicion_de_ordenes_de_pago_de_beneficios_anses_f3a839
    - Operacion_representacion_ante_camara_electronica_compensacion_e77be6
    - Operacion_reproduccion_de_firmas_digitalizadas_para_libramiento_de_cheques_a1b02c
    - Operacion_retencion_de_cheque_de_pago_diferido_e55273
    - Operacion_retencion_de_tarjeta_en_cajero_automatico_b9ece1
    - Operacion_retiro_de_fondos_cuentas_corrientes_especiales_e2972c
    - Operacion_retiro_de_tarjeta_magnetica_3a985e
    - Operacion_reversion_de_debitos_debito_automatico_3d9935
    - Operacion_revision_periodica_de_estrategias_y_politicas_789cd6
    - Operacion_revocacion_de_autorizaciones_para_librar_cheques_346e4b
    - Operacion_seguimiento_de_actividades_de_gestion_de_riesgos_c5564c
    - Operacion_sistema_de_incentivos_economicos_al_personal_2ce27a
    - Operacion_sistema_de_retribuciones_y_sistema_de_incentivos_economicos_6b4bb5
    - Operacion_solicitud_de_declaracion_jurada_debida_diligencia_ocde_cf4312
    - Operacion_solicitud_de_exclusion_de_la_central_ced256
    - Operacion_suministro_de_datos_cheques_de_pago_diferido_1e6869
    - Operacion_suministro_de_informacion_de_atributos_juridicos_y_representantes_de_persona_jur_182da3
    - Operacion_suministro_de_informacion_de_identidad_y_datos_personales_de_persona_humana_9930bf
    - Operacion_suspension_de_debito_debito_automatico_8239ad
    - Operacion_sustraccion_de_cheques_y_documentos_861ea8
    - Operacion_tenencia_de_instrumentos_tlac_684a59
    - Operacion_tenencia_de_titulos_valores_del_exterior_e03e90
    - Operacion_transferencia_de_cheques_de_pago_diferido_para_negociacion_bursatil_fb6f47
    - Operacion_transferencia_de_cheques_diferidos_para_negociacion_bursatil_8523f7
    - Operacion_transferencia_de_cheques_mediante_endoso_eae465
    - Operacion_transferencia_de_fondos_a_saldos_inmovilizados_59a8ec
    - Operacion_transferencia_de_saldos_de_depositos_282eb9
    - Operacion_transferencias_con_destino_a_cuentas_a_la_vista_para_uso_judicial_d1c05c
    - Operacion_transferencias_desde_cuentas_a_la_vista_para_uso_judicial_2ae517
    - Operacion_transferencias_ordenadas_por_cuentacorrentista_6dd714
    - Operacion_transmision_de_certificado_por_endoso_6ff931
    - Operacion_transmision_endoso_a_otros_sujetos_b3557c
    - Operacion_transmision_integra_de_echeq_al_repositorio_c8cba5
    - Operacion_uso_de_cajeros_automaticos_fb3600
    - Operacion_uso_de_cheques_en_cuentas_corrientes_247103
    - Operacion_uso_de_nombre_apellido_rectificado_genero_499e51
    - Operacion_uso_de_tarjetas_magneticas_en_cajeros_automaticos_1361d1
    - Operacion_utilizacion_de_instrumentos_y_metodologia_de_pago_29c114
    - Operacion_utilizacion_de_subcuentas_3da36b
    - Operacion_utilizacion_de_tecnologia_para_reproduccion_de_firmas_digitalizadas_ec4cc0
    - Operacion_venta_de_cheques_de_mostrador_4ed52b
    - Operacion_venta_de_cheques_de_pago_financiero_4725d0
    - Operacion_verificacion_de_identidad_de_presentantes_22c750
    - Operacion_verificacion_de_secuencia_numerica_de_cheques_y_formulas_a0b2a4
    - Operacion_vigilancia_del_sistema_de_incentivos_economicos_92765a
Potestad: 21 sin aplica_a
    - Potestad_admision_unificacion_registro_firmas_en_tarjeta_unica_eca724
    - Potestad_alcance_de_efectos_de_la_autorizacion_otorgada_564c5b
    - Potestad_alta_gerencia_adopcion_de_decisiones_gerenciales_6f2b4d
    - Potestad_autoridad_competente_ordena_modificacion_dni_6c4dab
    - Potestad_bcra_abrira_cuentas_corrientes_especiales_1fd2b6
    - Potestad_buena_practica_miembros_independientes_con_gestion_de_riesgos_4e6586
    - Potestad_dni_d_en_formato_credencial_virtual_para_dispositivos_moviles_cc7e75
    - Potestad_encargo_a_organismo_externo_evaluacion_b15633
    - Potestad_exclusion_de_responsabilidad_por_inconsistencias_en_datos_c45322
    - Potestad_exigencia_de_otros_comites_normas_bcra_29b0f1
    - Potestad_implementacion_de_programas_de_capacitacion_comite_de_auditoria_45a642
    - Potestad_mantencion_de_negociabilidad_cheque_imputado_endosado_5d640c
    - Potestad_medios_de_presentacion_presencial_o_electronico_6c3094
    - Potestad_opcion_de_admitir_negociacion_bursatil_de_cheques_4ae791
    - Potestad_potestad_bcra_debito_por_falseamiento_ca728f
    - Potestad_recordatorios_periodicos_posteriores_recomendaciones_325d86
    - Potestad_requerir_certificado_echeq_rechazado_079427
    - Potestad_requerir_registro_de_cheque_diferido_en_forma_directa_7542ed
    - Potestad_resolucion_de_procedimiento_segun_seccion_7_041edc
    - Potestad_tenedor_legitimado_presentar_echeq_al_cobro_a66ad2
    - Potestad_validez_instrumentos_compensables_emitidos_con_datos_anteriores_885701
Restriccion: 35 sin aplica_a
    - Restriccion_contener_endosos_que_excedan_el_limite_establecido_en_el_punto_5_1_1_c8ec92
    - Restriccion_dicha_comprobacion_podra_efectuarse_una_vez_transcurrido_el_citado_termino_de_10_1ae498
    - Restriccion_el_agregado_de_hojas_solo_procedera_por_razones_de_espacio_b5aa6a
    - Restriccion_el_bcra_debitara_de_la_cuenta_corriente_de_la_entidad_el_importe_correspondiente_8a7823
    - Restriccion_el_bcra_debitara_de_la_cuenta_corriente_de_la_entidad_una_multa_equivalente_al_d_672770
    - Restriccion_el_cuentacorrentista_quedara_incurso_en_la_situacion_a_que_se_refiere_el_punto_8_1cabdb
    - Restriccion_el_lapso_convenido_no_podra_superar_los_5_dias_habiles_bancarios_337a9b
    - Restriccion_el_rechazo_total_de_la_presentacion_procedera_toda_vez_que_se_observen_por_lo_me_a677d6
    - Restriccion_en_caso_de_que_las_modificaciones_se_originen_en_un_error_operativo_que_afecte_e_829c88
    - Restriccion_en_defecto_de_presentacion_al_cobro_el_echeq_quedara_pendiente_hasta_la_fecha_de_c67862
    - Restriccion_en_la_medida_en_que_dichas_cartas_de_credito_sean_irrestrictas_779f0d
    - Restriccion_en_ningun_caso_el_registro_del_cheque_podra_demorarse_mas_de_15_dias_corridos_6a090a
    - Restriccion_esa_certificacion_mantendra_vigencia_durante_90_dias_corridos_desde_la_fecha_a_l_39bbb0
    - Restriccion_la_aceptacion_de_cheques_no_procede_cuando_medie_orden_judicial_en_contrario_ab456e
    - Restriccion_la_aceptacion_de_presentaciones_efectuadas_durante_el_periodo_de_presentacion_ta_8f7818
    - Restriccion_la_cantidad_de_registros_con_inconsistencias_en_alguno_de_los_archivos_supera_el_4cbdc1
    - Restriccion_la_denuncia_de_extravio_sustraccion_o_adulteracion_genera_la_imposibilidad_de_pr_143ee4
    - Restriccion_la_fecha_de_pago_no_puede_exceder_un_plazo_de_360_dias_en_los_cheques_de_pago_di_225b7c
    - Restriccion_la_nueva_clave_o_contrasena_personal_password_pin_seleccionada_por_el_usuario_no_841919
    - Restriccion_la_retencion_del_cheque_de_pago_diferido_no_podra_exceder_de_5_dias_corridos_con_8f8308
    - Restriccion_la_tacha_de_la_leyenda_de_cheque_para_acreditar_en_cuenta_se_tendra_por_no_hecha_6664c4
    - Restriccion_las_presentaciones_rechazadas_por_los_citados_motivos_se_consideraran_no_efectua_0ca7a1
    - Restriccion_las_retribuciones_deben_ser_determinadas_sobre_la_base_de_sumas_fijas_que_no_est_64361c
    - Restriccion_los_cheques_de_pago_diferido_transferidos_para_negociacion_en_bolsas_de_comercio_942a1b
    - Restriccion_monto_minimo_de_60_000_pesos_sesenta_mil_por_dia_en_una_unica_extraccion_en_caje_7090bd
    - Restriccion_no_correspondera_la_comunicacion_al_bcra_de_los_rechazos_48aa51
    - Restriccion_no_divulgar_el_numero_de_clave_personal_1d5dfa
    - Restriccion_no_escribir_el_numero_de_clave_personal_en_la_tarjeta_magnetica_provista_o_en_un_b8e447
    - Restriccion_no_se_han_acompanado_los_soportes_con_los_archivos_requeridos_o_ellos_no_pueden__a816f2
    - Restriccion_que_la_acreditacion_de_los_fondos_se_efectue_en_forma_inmediata_a_simple_requeri_13d907
    - Restriccion_requiriendo_a_ese_efecto_calificacion_internacional_de_riesgo_investment_grade_bae8f9
    - Restriccion_se_autorizara_el_libramiento_de_echeq_por_un_importe_global_maximo_en_funcion_de_4e1d99
    - Restriccion_son_nulos_el_endoso_del_girado_073aaf
    - Restriccion_son_nulos_el_endoso_parcial_54eacd
    - Restriccion_unicamente_el_destinatario_del_pago_puede_endosarlo_eff063
```

### S12 — FAIL

ERROR — Toda Excepcion tiene >=1 arista saliente exceptua o exceptua_obligacion.

**Resultado:** 27 Excepciones sin salida exceptua/exceptua_obligacion.

```
    - Excepcion_a_fin_de_ser_excluidas_de_la_central_de_cheques_rechazados_y_o_de_la_central_de__aa36bc
    - Excepcion_contenga_endosos_tachados_o_que_carezcan_de_los_requisitos_formales_establecidos_424d07
    - Excepcion_cuando_la_cantidad_escrita_en_letras_difiriese_de_la_expresada_en_numeros_se_est_20af1c
    - Excepcion_dicho_pago_no_exime_a_la_entidad_de_las_responsabilidades_civiles_que_pudieren_c_a2081e
    - Excepcion_en_caso_de_afectacion_de_la_solvencia_y_o_liquidez_de_la_entidad_se_tenga_por_no_49f140
    - Excepcion_en_caso_de_no_existir_dicha_jerarquia_la_pertinente_presentacion_estara_a_cargo__80a40c
    - Excepcion_en_el_supuesto_de_adulteracion_el_rechazo_del_cheque_no_se_comunicara_cuando_exi_48b261
    - Excepcion_haberse_dispuesto_medidas_cautelares_sobre_los_fondos_destinados_para_el_pago_de_daf62d
    - Excepcion_la_delegacion_no_afecta_las_responsabilidades_que_les_caben_a_los_funcionarios_d_340460
    - Excepcion_las_modificaciones_en_el_nombre_y_o_apellido_de_las_personas_fisicas_o_en_otros__4fe2e3
    - Excepcion_liberacion_de_la_obligacion_de_secreto_y_reserva_a_que_se_refieren_las_leyes_de__a3f751
    - Excepcion_los_cheques_en_los_casos_previstos_en_el_punto_6_2_no_son_susceptibles_de_rechaz_a2b1ce
    - Excepcion_no_corresponde_la_presentacion_de_esas_declaraciones_juradas_por_cada_una_de_las_8e76e4
    - Excepcion_no_correspondera_la_comunicacion_al_bcra_de_los_rechazos_cuando_se_haya_declarad_6b4948
    - Excepcion_no_correspondera_la_comunicacion_al_bcra_de_los_rechazos_motivados_por_el_pago_d_6ac373
    - Excepcion_no_correspondera_la_comunicacion_al_bcra_de_los_rechazos_motivados_por_falsifica_ba82ed
    - Excepcion_no_implica_la_inclusion_en_la_causal_a_que_se_refiere_el_punto_9_1_2_a809ff
    - Excepcion_no_procedera_la_inclusion_respecto_de_apoderados_para_el_uso_de_la_cuenta_corrie_811545
    - Excepcion_no_se_considerara_error_el_rechazo_del_cheque_respecto_del_cual_haya_mediado_aut_52b4bc
    - Excepcion_no_se_consideraran_las_exportaciones_industriales_comprendidas_en_acuerdos_inter_c85d60
    - Excepcion_resultaran_de_aplicacion_las_disposiciones_sobre_extravio_sustraccion_o_adultera_a08c1d
    - Excepcion_salvo_decision_de_autoridad_competente_que_obligue_al_cierre_inmediato_c9d545
    - Excepcion_se_exceptua_la_prohibicion_cuando_se_trate_de_inversiones_en_titulos_publicos_ex_6792e8
    - Excepcion_se_exceptuan_de_las_limitaciones_establecidas_en_este_punto_las_sucesivas_transm_9f4f1a
    - Excepcion_se_excluiran_del_monto_de_ventas_totales_aquellas_realizadas_por_la_empresa_en_e_2ec8f1
    - Excepcion_se_presumira_conformidad_con_el_movimiento_registrado_en_el_banco_cuando_no_hay__ad154b
    - Excepcion_sin_tener_en_cuenta_las_limitaciones_cuantitativas_previstas_en_los_puntos_2_1_9_7919c7
```

### S21 — WARN

INFORMATIVA — Coherencia de referencias nodo->nodo (rol_fuente=referencia_cruzada): properties.destino sin el prefijo <to>:: pertenece al CONJUNTO {p.punto for p in provenances} del nodo destino (nunca solo provenance[0]); desglose por properties.via.

**Resultado:** 518 referencias nodo->nodo ({'nodos_del_punto': 513, 'texto_ordenado': 5}); 5 incoherentes (por via: {'texto_ordenado': 5}).

```
idx 1789: Obligacion_las_entidades_financieras_comprendidas_exclusivamente_sus_casas_en_el_pais_obser_6ccac0 -> TextoOrdenado_polcre_pdf destino='polcre::TO' via='texto_ordenado': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4.1', '1.4.2']...
idx 1794: Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_consolidada_observa_8bde79 -> TextoOrdenado_polcre_pdf destino='polcre::TO' via='texto_ordenado': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4.1', '1.4.2']...
idx 2169: Obligacion_presentacion_de_fotocopias_autenticadas_por_escribano_publico_de_los_documentos__ab60fc -> TextoOrdenado_docvig_pdf destino='docvig::TO' via='texto_ordenado': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '2.1.1.1']...
idx 2172: Obligacion_presentacion_de_tipo_y_numero_del_documento_para_establecer_su_identificacion_se_f6fcb1 -> TextoOrdenado_docvig_pdf destino='docvig::TO' via='texto_ordenado': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '2.1.1.1']...
idx 2294: Obligacion_se_debera_consignar_al_dorso_la_firma_y_aclaracion_o_en_el_correspondiente_regis_5b4640 -> TextoOrdenado_docvig_pdf destino='docvig::TO' via='texto_ordenado': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '2.1.1.1']...
```

### S22 — PASS

INFORMATIVA — Coherencia de padre_sugerido: el destino de la arista es properties.padre_sugerido del origen y el origen está en cuarentena.

**Resultado:** 11 aristas padre_sugerido; 0 incoherentes (0 con destino distinto, 0 con origen fuera de cuarentena).

Sin violaciones.

### S23 — WARN

INFORMATIVA — aplica_a hacia sujetos en cuarentena: aristas aplica_a cuyo destino es un Sujeto de nivel propuesto (conteo; nunca bloqueante).

**Resultado:** 989 aristas aplica_a; 18 hacia Sujetos propuestos (11 destinos distintos).

```
idx 555: Excepcion_se_exceptuan_de_la_citada_limitacion_aquellos_endosos_efectuados_en_los_echeq_3c10fe -> Sujeto_propuesto_echeq
idx 567: Excepcion_se_exceptuan_de_las_limitaciones_establecidas_en_este_punto_cuando_los_cheques_s_8bb009 -> Sujeto_propuesto_caja_de_valores_s_a
idx 635: Obligacion_acompanar_la_nomina_de_los_cheques_comunes_y_de_pago_diferido_librados_a_la_fech_bd0f7f -> Sujeto_propuesto_cuentacorrentista
idx 720: Obligacion_asegurar_que_el_directorio_reciba_informacion_relevante_integra_y_oportuna_que_l_133f73 -> Sujeto_propuesto_alta_gerencia
idx 884: Obligacion_cumplir_con_los_objetivos_estrategicos_fijados_por_el_directorio_46a3f8 -> Sujeto_propuesto_alta_gerencia
idx 1067: Obligacion_devolver_los_no_utilizados_d29410 -> Sujeto_propuesto_cuentacorrentista
idx 1200: Obligacion_el_presentante_debera_acreditar_su_categoria_de_residencia_su_vigencia_y_el_tiem_f1c047 -> Sujeto_propuesto_presentante
idx 1319: Obligacion_en_las_entidades_financieras_publicas_la_definicion_de_la_politica_en_funcion_de_501edc -> Sujeto_propuesto_entidades_financieras_publicas
idx 1339: Obligacion_en_todos_los_casos_debera_acreditarse_la_categoria_de_residencia_su_vigencia_y_e_0871f4 -> Sujeto_propuesto_extranjeros_con_residencia_permanente_o_temporaria
idx 1488: Obligacion_implementar_las_politicas_procedimientos_procesos_y_controles_necesarios_para_ge_97575e -> Sujeto_propuesto_alta_gerencia
idx 1520: Obligacion_informar_los_anulados_24175b -> Sujeto_propuesto_cuentacorrentista
idx 1726: Obligacion_las_empresas_administradoras_de_las_redes_de_cajeros_automaticos_y_las_entidades_6be3de -> Sujeto_propuesto_empresas_administradoras_de_redes_de_cajeros_automaticos
idx 1909: Obligacion_las_personas_que_hayan_sido_incorporadas_a_la_central_de_cheques_rechazados_y_o__491251 -> Sujeto_propuesto_personas_que_hayan_sido_incorporadas_a_las_centrales
idx 2009: Obligacion_los_integrantes_de_la_alta_gerencia_deberan_ejercer_el_control_apropiado_del_per_d69406 -> Sujeto_propuesto_integrantes_de_la_alta_gerencia
idx 2011: Obligacion_los_integrantes_de_la_alta_gerencia_deberan_gestionar_el_negocio_bajo_su_supervi_2f0813 -> Sujeto_propuesto_integrantes_de_la_alta_gerencia
idx 2013: Obligacion_los_integrantes_de_la_alta_gerencia_deberan_tener_la_idoneidad_y_experiencia_nec_3381c3 -> Sujeto_propuesto_integrantes_de_la_alta_gerencia
idx 2729: Operacion_exclusion_de_inhabilitados_de_base_de_datos_cc5e08 -> Sujeto_propuesto_personas_inhabilitadas_por_decision_judicial_o_por_motivos_legales
idx 2994: Operacion_presentacion_de_dni_para_identificacion_16dca8 -> Sujeto_propuesto_extranjeros_con_residencia_permanente_o_temporaria
```

## Tabla resumen

| Severidad | Regla | Resultado | Resumen |
|---|---|---|---|
| bloqueante | S1 | PASS | 3983/3983 aristas con relación admitida (18 relaciones admitidas); 0 violaciones. |
| bloqueante | S2 | PASS | 0 aristas colgantes sobre 3983. |
| bloqueante | S3 | PASS | 3983/3983 aristas conformes a firma; 0 violaciones. Evaluadas: 3337 por matriz, 117 de esqueleto, 11 padre_sugerido; 518 referencias nodo->nodo admitidas por rol_fuente. |
| bloqueante | S4 | PASS | Nodos OK: 1979/1979. Aristas OK: 3983/3983. Violaciones: 0. |
| bloqueante | S5 | PASS | Nodos con punto: 1979/1979. Aristas: 3983/3983. Violaciones: 0. |
| bloqueante | S6 | PASS | Archivos válidos (41): TextoOrdenado ['ctacte.pdf', 'docvig.pdf', 'lingob.pdf', 'pagjub.pdf', 'polcre.pdf'] ∪ esqueleto ['TO_capitales_minimos_actual.pdf', 'TO_clasificacion_deudores_actual.pdf', 'TO_exterior_cambios_actual.pdf', 'TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'TO_regimen_informativo_contable_mensual_actual.pdf', 'adrei.pdf', 'autenf.pdf', 'ccbcra.pdf', 'convca.pdf', 'cryl.pdf', 'ctacor.pdf', 'depaho.pdf', 'efemin.pdf', 'esquema_v2_clases.json', 'esquema_v3_clases.json', 'fabcra.pdf', 'icmecma.pdf', 'lavdin.pdf', 'ordcom.pdf', 'osapsa.pdf', 'pfmipyme.pdf', 'pimf.pdf', 'ratiofn.pdf', 'rdbcra.pdf', 'repefe.pdf', 'retype.pdf', 'rmrtsd.pdf', 'rrci.pdf', 'servco.pdf', 'snp_atm.pdf', 'snp_debin.pdf', 'snp_psp.pdf', 'snp_spd.pdf', 'snp_tr_nc.pdf', 'supcon.pdf', 'traval.pdf']. Violaciones: 0. |
| bloqueante | S15 | PASS | 35 roles, 51 aristas miembro_de; 12 huérfanos (12 declarados, 0 sin declarar); 0 miembros que no son clase. Lista declarada: 12 ({'sin_id_en_catalogo': 6, 'aplanamiento_rechazado': 5, 'instancia_rechazada': 1}). |
| bloqueante | S19 | FAIL | 114 Sujetos ({'clase': 61, 'instancia': 7, 'propuesto': 11, 'rol': 35}); catálogo de 101 ids; 2 fuera del catálogo, 0 con nivel inválido, 0 propuestos incompletos. |
| bloqueante | S20 | PASS | 741/741 Obligaciones con tipo en el enum. Valores retirados: 0 ({}). Otros valores fuera del enum: 0 ({}). |
| informativa | S7 | FAIL | 5 grupos violatorios (10 nodos involucrados). |
| informativa | S8 | WARN | 5 grupos con el mismo label normalizado en types distintos. |
| informativa | S9 | PASS | 0 nodos con ambas keys. |
| informativa | S10 | FAIL | Sin establecida_en: Condicion=28, Definicion=1, Excepcion=2, Obligacion=0, Operacion=134, Potestad=0, Restriccion=0 (total 165). |
| informativa | S11 | WARN | Sin aplica_a: Excepcion=59, Obligacion=53, Operacion=421, Potestad=21, Restriccion=35 (total 589). |
| informativa | S12 | FAIL | 27 Excepciones sin salida exceptua/exceptua_obligacion. |
| informativa | S21 | WARN | 518 referencias nodo->nodo ({'nodos_del_punto': 513, 'texto_ordenado': 5}); 5 incoherentes (por via: {'texto_ordenado': 5}). |
| informativa | S22 | PASS | 11 aristas padre_sugerido; 0 incoherentes (0 con destino distinto, 0 con origen fuera de cuarentena). |
| informativa | S23 | WARN | 989 aristas aplica_a; 18 hacia Sujetos propuestos (11 destinos distintos). |

**Veredicto global: NO PASA**

## Numeración de las shapes nuevas del perfil

- S19: Catálogo de sujetos (bloqueante): todo Sujeto tiene nivel válido; si no es propuesto, su id está en el catálogo; si es propuesto, tiene cuarentena y padre_sugerido.
- S20: Enum de Obligacion.tipo (bloqueante): todo Obligacion.tipo está en el enum congelado; conteos separados de valores retirados y de otros valores fuera del enum.
- S21: Coherencia de referencias nodo→nodo (informativa): destino sin prefijo <to>:: pertenece al conjunto de puntos del nodo destino; desglose por via.
- S22: Coherencia de padre_sugerido (informativa): destino de la arista = properties.padre_sugerido del origen y el origen está en cuarentena.
- S23: aplica_a hacia sujetos en cuarentena (informativa): aristas aplica_a cuyo destino es Sujeto de nivel propuesto.

## Fuera del perfil

- S13, S14, S16, S17: no implementadas (se declaran para que su ausencia se lea; no se inventan).
- S18: número ya declarado en docs/esquema_v2_diseño.md con otro enunciado (umbral de limita); no se reutiliza.
