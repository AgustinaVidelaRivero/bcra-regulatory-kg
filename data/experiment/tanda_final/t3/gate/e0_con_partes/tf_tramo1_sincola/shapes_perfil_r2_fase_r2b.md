# Validador de shapes — perfil r2

- **Grafo:** `data/experiment/reextraccion_v2/corpus_tanda_final/ens_tramo1_r2b_sincola/r2/kg.json`
- **sha256 del grafo:** `bbda74cda7e071e27782b41b06d7557e2c153e8afff7ea3f6540bdd520c3615f`
- **Fecha:** 2026-10-20
- **Nodos:** 2207
- **Aristas:** 3822
- **Perfil:** r2 (fase r2b)
- **Vocabulario:** `<SCRATCHPAD>/t3/copia_t3/data/experiment/pyd_r2/generados/enums_r2.json` (sha256 `abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241`); marcas de nodo de `<SCRATCHPAD>/t3/copia_t3/data/experiment/pyd_r2/code/modelos_r2.py`: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']
- **Catálogo único (S19, S29):** `<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json` — 110 ids
- **Lista de S15:** `<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json`
- **Registro (S28):** `data/experiment/reextraccion_v2/corpus_tanda_final/ens_tramo1_r2b_sincola/r2/no_mapeados_sujetos.jsonl`
- **E0 (S31):** `data/experiment/tanda_final/t3/e0_con_partes/tanda_final_corrida1`
- **Veredicto global: PASA**

## Bloqueantes

### S1 — PASS

Toda arista usa una relación admitida por el perfil r2: los 13 predicados de enums_r2.json ∪ remite_a (enmienda 2 de L-ESQ-R2) ∪ las 4 de esqueleto ∪ padre_sugerido.

**Resultado:** 3822/3822 aristas con relación admitida (19 relaciones admitidas); 0 violaciones.

Sin violaciones.

### S2 — PASS

Integridad referencial: origen y destino de toda arista existen como nodos.

**Resultado:** 0 aristas colgantes sobre 3822.

Sin violaciones.

### S3 — PASS

Toda arista respeta las firmas del perfil r2: matriz ampliada de enums_r2.json (firmas_r2, con condicion_de -> Operacion|Potestad) ∪ remite_a con origen en los siete tipos de contenido y destino en esos siete o TextoOrdenado ∪ esqueleto solo Sujeto->Sujeto ∪ padre_sugerido solo de Sujeto propuesto a Sujeto clase|rol. Una referencia con origen distinto de TextoOrdenado es violación, con o sin rol_fuente.

**Resultado:** 3822/3822 aristas conformes a firma; 0 violaciones. Evaluadas: 2898 por matriz, 737 remite_a, 126 de esqueleto, 61 padre_sugerido.

Sin violaciones.

### S4 — PASS

Todo nodo y toda arista tienen provenance dict con al menos {to, archivo, punto, rol_documental}, provenances lista no vacía con provenance == provenances[0]; para rol_documental distinto de esqueleto, to y archivo no vacíos (para esqueleto se admiten to nulo, chunk_id nulo y paginas vacía).

**Resultado:** Nodos OK: 2207/2207. Aristas OK: 3822/3822. Violaciones: 0.

Sin violaciones.

### S5 — PASS

Todo provenance.punto (de nodo y de arista) es una string no vacía.

**Resultado:** Nodos con punto: 2207/2207. Aristas: 3822/3822. Violaciones: 0.

Sin violaciones.

### S6 — PASS

Todo provenance.archivo pertenece a {properties.archivo de los nodos TextoOrdenado} ∪ {archivo de las provenances con rol_documental=esqueleto}; nada codificado a mano.

**Resultado:** Archivos válidos (70): TextoOrdenado ['asomut.pdf', 'cedin.pdf', 'consyr.pdf', 'micemp.pdf', 'ri_acsf.pdf', 'ri_ai.pdf', 'ri_bdp.pdf', 'ri_cr.pdf', 'ri_dsf.pdf', 'ri_esd.pdf', 'ri_ieccm.pdf', 'ri_iepsp.pdf', 'ri_iesinap.pdf', 'ri_ii_31_12_19.pdf', 'ri_laft.pdf', 'ri_msrl.pdf', 'ri_nge.pdf', 'ri_ot.pdf', 'ri_psp.pdf', 'ri_pspapt.pdf', 'ri_rcl.pdf', 'ri_secoexpo.pdf', 'ri_sef.pdf', 'ri_tar.pdf', 'ri_transpa.pdf', 'ri_tsa.pdf', 'ri_tvf.pdf', 'ribspc.pdf', 'seggar.pdf', 'verac.pdf'] ∪ esqueleto ['TO_capitales_minimos_actual.pdf', 'TO_clasificacion_deudores_actual.pdf', 'TO_exterior_cambios_actual.pdf', 'TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'TO_regimen_informativo_contable_mensual_actual.pdf', 'actgar.pdf', 'adrei.pdf', 'autenf.pdf', 'catalogo_sujetos_v3.json', 'ccbcra.pdf', 'convca.pdf', 'cryl.pdf', 'ctacor.pdf', 'depaho.pdf', 'efemin.pdf', 'esquema_v2_clases.json', 'esquema_v3_clases.json', 'fabcra.pdf', 'icmecma.pdf', 'lavdin.pdf', 'lingob.pdf', 'ordcom.pdf', 'osapsa.pdf', 'pagjub.pdf', 'pfmipyme.pdf', 'pimf.pdf', 'ratiofn.pdf', 'rdbcra.pdf', 'repefe.pdf', 'retype.pdf', 'rmrtsd.pdf', 'rrci.pdf', 'servco.pdf', 'snp_atm.pdf', 'snp_debin.pdf', 'snp_psp.pdf', 'snp_spd.pdf', 'snp_tr_nc.pdf', 'supcon.pdf', 'traval.pdf']. Violaciones: 0.

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

### S18 — PASS

ERROR — Reescrita (L-ESQ-R2 §1.5): Restriccion de tipo limite_cuantitativo => lista de umbrales no vacía o marca (el umbral guardado sin lista: campos_heredados_v3.umbral o properties_no_definidas.umbral; en r2b, también la marca properties_no_definidas.umbral_no_cuantificable del ensamblado). El enunciado de docs/esquema_v2_diseño.md:325 no rige en el perfil r2.

**Resultado:** 23 Restricciones limite_cuantitativo: 23 con lista, 0 con el umbral guardado sin lista (marca), 0 sin ninguna.

Sin violaciones.

### S19 — PASS

ERROR — Catálogo de sujetos: todo Sujeto tiene nivel ∈ {clase, instancia, rol, propuesto}; si nivel ≠ propuesto, su id está en el catálogo (clases ∪ roles) del artefacto de --excepciones; si nivel = propuesto, tiene properties.cuarentena y properties.padre_sugerido.

**Resultado:** 171 Sujetos ({'clase': 70, 'instancia': 5, 'propuesto': 61, 'rol': 35}); catálogo de 110 ids; 0 fuera del catálogo, 0 con nivel inválido, 0 propuestos incompletos.

Sin violaciones.

### S20 — PASS

ERROR — Enum de Obligacion.tipo del perfil r2: en la lista o con la marca fuera_de_lista. Lista: {presentacion_informativa|calculo|asignacion|comunicacion_a_cliente|reporte_al_supervisor|otra}.

**Resultado:** 850 nodos Obligacion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 0.

Sin violaciones.

### S24 — PASS

ERROR — Enum de Restriccion.tipo (bloqueante salvo la marca fuera_de_lista). Lista: {prohibicion|limite_cuantitativo|limite_cualitativo}.

**Resultado:** 94 nodos Restriccion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 0.

Sin violaciones.

### S25 — PASS

ERROR — Enum de Comunicacion.tipo, con «externa» (bloqueante salvo la marca fuera_de_lista). Lista: {A|B|C|externa}.

**Resultado:** 49 nodos Comunicacion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 17.

Sin violaciones.

### S26 — PASS

ERROR — Claves cerradas por tipo: las properties de cada nodo de los nueve tipos están en claves_por_tipo de enums_r2.json o en MARCAS_NODO de modelos_r2.py; lo demás vive en properties_no_definidas.

**Resultado:** 2036 nodos evaluados; 0 violaciones {}; marcas de nodo admitidas: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to'].

Sin violaciones.

### S28 — PASS

ERROR — Sujeto propuesto con fila en el registro de no mapeados (bloqueante).

**Resultado:** 61 Sujetos propuestos; 229 filas en el registro; 0 propuestos sin fila.

Sin violaciones.

### S29 — PASS

ERROR — Destino de padre_sugerido en el catálogo único (bloqueante: U-CAT-UNICO está cerrada).

**Resultado:** 61 aristas padre_sugerido; 0 con destino fuera del catálogo único (110 ids).

Sin violaciones.

### S30 — PASS

ERROR — alcance de remite_a en la lista cerrada y coherente con los extremos (bloqueante). Coherencia: to_entero si el destino es un TextoOrdenado (destino <to>::TO); si no, interna cuando el TO de la unidad citada es el de la procedencia de la arista y externa cuando es otro (enmienda 2 de L-ESQ-R2, §3).

**Resultado:** 737 aristas remite_a ({'interna': 736, 'to_entero': 1}); 0 violaciones.

Sin violaciones.

### S31 — PASS

ERROR — evidencia de remite_a: tramo literal de un único tramo del texto de E0 de su chunk_id (bloqueante; sin --e0, NO COMPUTABLE). Tramo = el texto propio del chunk o uno de sus tramos heredados, cada uno por separado; nunca la concatenación. Si la evidencia no está en el chunk de provenance, se busca en las otras procedencias de la arista (fusión).

**Resultado:** 737 aristas remite_a: {'en_un_tramo_del_chunk_de_la_arista': 737}; 0 violaciones.

Sin violaciones.

### S27 — PASS

ERROR — Arista de sujeto con mención y método (informativa en r2a, bloqueante desde r2b). Fase: r2b.

**Resultado:** 549 aristas de sujeto fuera del esqueleto; 0 sin mención, verificación o método ({}).

Sin violaciones.

## Informativas

### S7 — FAIL

ERROR — Unicidad exacta: no puede haber dos nodos con el mismo (type, label normalizado).

**Resultado:** 50 grupos violatorios (122 nodos involucrados).

```
[Comunicacion] 'decreto 1292/96' (2 nodos):
    - Comunicacion_decreto_1292_96  (label: 'Decreto 1292/96')
    - Comunicacion_decreto_n_1292_96  (label: 'Decreto 1292/96')
[Comunicacion] 'decreto 540/95' (2 nodos):
    - Comunicacion_decreto_540_95  (label: 'Decreto 540/95')
    - Comunicacion_decreto_n_540_95  (label: 'Decreto 540/95')
[Comunicacion] 'to presentacion de informaciones' (2 nodos):
    - Comunicacion_presentacion_de_informaciones_al_banco_central  (label: 'TO Presentación de informaciones')
    - Comunicacion_presentacion_de_informaciones_al_banco_central__ri_laft  (label: 'TO Presentación de informaciones')
[Condicion] 'aprobacion por organo de administracion' (3 nodos):
    - Condicion_aprobacion_por_organo_de_administracion__el_informe_debe_haber_sido_aprobado_por_3b0dc8  (label: 'Aprobación por órgano de administración')
    - Condicion_aprobacion_por_organo_de_administracion__el_informe_tecnico_y_la_declaracion_de__968acc  (label: 'Aprobación por órgano de administración')
    - Condicion_aprobacion_por_organo_de_administracion__los_informes_deben_ser_aprobados_por_el_7e2d61  (label: 'Aprobación por órgano de administración')
[Condicion] 'cedin identificado como aplicado' (2 nodos):
    - Condicion_cedin_identificado_como_aplicado__el_cedin_esta_identificado_tanto_en_el_cuerpo__ab03b2  (label: 'CEDIN identificado como APLICADO')
    - Condicion_cedin_identificado_como_aplicado__el_cedin_se_encuentra_identificado_tanto_en_el_cf8993  (label: 'CEDIN identificado como APLICADO')
[Condicion] 'cuando corresponda segun disposiciones vigentes' (2 nodos):
    - Condicion_cuando_corresponda_segun_disposiciones_vigentes__la_obligacion_de_informar_se_ac_741ddd  (label: 'Cuando corresponda según disposiciones vigentes')
    - Condicion_cuando_corresponda_segun_disposiciones_vigentes__la_obligacion_de_informar_se_ac_f8b8a0  (label: 'Cuando corresponda según disposiciones vigentes')
[Definicion] 'agencias complementarias de servicios financieros' (2 nodos):
    - Definicion_agencias_complementarias_de_servicios_financieros__unidad_de_servicio_con_codigo_63ca7e  (label: 'Agencias complementarias de servicios financieros')
    - Definicion_agencias_complementarias_de_servicios_financieros__unidades_de_servicios_compren_be3cd6  (label: 'Agencias complementarias de servicios financieros')
[Definicion] 'depositos operativos en otras entidades' (2 nodos):
    - Definicion_depositos_operativos_en_otras_entidades__codigo_355000_m_depositos_operativos_ma_7c70d6  (label: 'Depósitos operativos en otras entidades')
    - Definicion_depositos_operativos_en_otras_entidades__depositos_operativos_mantenidos_en_otra_dd4ac3  (label: 'Depósitos operativos en otras entidades')
[Definicion] 'fed — fondeo estable disponible' (2 nodos):
    - Definicion_fed_fondeo_estable_disponible__categoria_que_comprende_capital_regulador_total_i_0ff83e  (label: 'FED — Fondeo Estable Disponible')
    - Definicion_fed_fondeo_estable_disponible__componente_de_la_categoria_fed_con_codigo_10000_c_ef0a34  (label: 'FED — Fondeo Estable Disponible')
[Definicion] 'fer — fondeo estable requerido' (2 nodos):
    - Definicion_fer_fondeo_estable_requerido__categoria_que_comprende_monedas_y_billetes_deposit_9260d6  (label: 'FER — Fondeo Estable Requerido')
    - Definicion_fer_fondeo_estable_requerido__componente_de_la_categoria_fed_con_codigo_20000_cu_c52a87  (label: 'FER — Fondeo Estable Requerido')
[Definicion] 'otras entradas contractuales de efectivo' (2 nodos):
    - Definicion_otras_entradas_contractuales_de_efectivo__codigo_370000_m_otras_entradas_contrac_e6e700  (label: 'Otras entradas contractuales de efectivo')
    - Definicion_otras_entradas_contractuales_de_efectivo__otras_entradas_contractuales_de_efecti_f5fa3b  (label: 'Otras entradas contractuales de efectivo')
[Definicion] 'otras entradas en funcion de la contraparte' (2 nodos):
    - Definicion_otras_entradas_en_funcion_de_la_contraparte__codigo_350000_m_otras_entradas_en_f_295252  (label: 'Otras entradas en función de la contraparte')
    - Definicion_otras_entradas_en_funcion_de_la_contraparte__otras_entradas_en_funcion_de_la_con_e74934  (label: 'Otras entradas en función de la contraparte')
[Definicion] 'provincial — codificacion anexo i' (2 nodos):
    - Definicion_provincial_codificacion_anexo_i__segun_la_codificacion_de_la_tabla_del_anexo_i___cc87db  (label: 'Provincial — codificación Anexo I')
    - Definicion_provincial_codificacion_anexo_i__segun_la_codificacion_de_la_tabla_del_anexo_i___ebaefc  (label: 'Provincial — codificación Anexo I')
[Excepcion] 'excepcion asociaciones mutuales y cooperativas' (2 nodos):
    - Excepcion_las_asociaciones_mutuales_y_cooperativas_quedan_exceptuadas_del_requerimiento_de_ee7618  (label: 'Excepción asociaciones mutuales y cooperativas')
    - Excepcion_quedan_exceptuadas_del_regimen_informativo_las_asociaciones_mutuales_y_cooperati_506828  (label: 'Excepción asociaciones mutuales y cooperativas')
[Excepcion] 'excepcion cheques pagados capturados por cliente' (2 nodos):
    - Excepcion_no_aplica_lo_previsto_en_el_punto_3_3_cuando_se_trate_de_cheques_pagados_present_b8481f  (label: 'Excepción cheques pagados capturados por cliente')
    - Excepcion_no_aplica_lo_previsto_en_el_punto_3_4_certificacion_de_las_reproducciones_cuando_856b16  (label: 'Excepción cheques pagados capturados por cliente')
[Excepcion] 'excepcion verificaciones — cedin aplicado' (2 nodos):
    - Excepcion_no_se_realizaran_las_verificaciones_previstas_en_el_punto_7_cuando_el_cedin_se_e_337225  (label: 'Excepción verificaciones — CEDIN APLICADO')
    - Excepcion_no_se_realizaran_las_verificaciones_previstas_en_el_punto_cuando_el_cedin_se_enc_cd2f6c  (label: 'Excepción verificaciones — CEDIN aplicado')
[Excepcion] 'exclusion depositos personas vinculadas' (2 nodos):
    - Excepcion_quedan_excluidos_de_la_garantia_los_depositos_efectuados_por_personas_vinculadas_6cd717  (label: 'Exclusión depósitos personas vinculadas')
    - Excepcion_quedan_excluidos_de_la_garantia_los_depositos_efectuados_por_personas_vinculadas_c70df8  (label: 'Exclusión depósitos personas vinculadas')
[Obligacion] 'consignar provincia — municipios' (2 nodos):
    - Obligacion_para_municipios_se_debera_consignar_unicamente_la_provincia_a_la_que_corresponde_d8cd09  (label: 'Consignar provincia — municipios')
    - Obligacion_para_municipios_se_debera_consignar_unicamente_la_provincia_a_la_que_corresponde_fb9361  (label: 'Consignar provincia — municipios')
[Obligacion] 'conversion de moneda extranjera a pesos' (2 nodos):
    - Obligacion_los_importes_en_moneda_extranjera_se_convertiran_a_pesos_utilizando_el_tipo_de_c_1f1e7c  (label: 'Conversión de moneda extranjera a pesos')
    - Obligacion_los_importes_en_moneda_extranjera_se_convertiran_a_pesos_utilizando_el_tipo_de_c_ffc19e  (label: 'Conversión de moneda extranjera a pesos')
[Obligacion] 'elaboracion por profesionales matriculados con certificacion' (2 nodos):
    - Obligacion_el_informe_debe_ser_elaborado_por_profesionales_o_asociaciones_de_profesionales__88a4a6  (label: 'Elaboración por profesionales matriculados con certificación')
    - Obligacion_el_informe_debera_ser_elaborado_por_profesionales_o_asociaciones_de_profesionale_2d782e  (label: 'Elaboración por profesionales matriculados con certificación')
[Obligacion] 'emision de informe especial' (2 nodos):
    - Obligacion_emitir_el_presente_informe_especial_basado_en_la_tarea_profesional_detallada_en__d5c517  (label: 'Emisión de informe especial')
    - Obligacion_emitir_un_informe_especial_basado_en_la_tarea_profesional_para_cumplir_con_los_r_924955  (label: 'Emisión de informe especial')
[Obligacion] 'informar apellidos segun punto 2.3' (2 nodos):
    - Obligacion_se_informaran_los_apellidos_teniendo_en_cuenta_las_indicaciones_contenidas_en_el_fcf916  (label: 'Informar apellidos según punto 2.3')
    - Obligacion_se_informaran_los_apellidos_teniendo_en_cuenta_las_indicaciones_contenidas_en_el_fd602a  (label: 'Informar apellidos según punto 2.3')
[Obligacion] 'informar fecha y numero de resolucion bcra' (2 nodos):
    - Obligacion_deber_de_informar_la_fecha_y_numero_de_la_resolucion_del_bcra_que_se_haya_expedi_cecf66  (label: 'Informar fecha y número de Resolución BCRA')
    - Obligacion_deber_de_informar_la_fecha_y_numero_de_la_resolucion_del_bcra_que_se_haya_expedi_e3b6c3  (label: 'Informar fecha y número de Resolución BCRA')
[Obligacion] 'informar nacionalidad con codigo swift' (2 nodos):
    - Obligacion_se_informara_el_pais_que_corresponda_ingresando_el_pertinente_codigo_swift_de_pa_413c25  (label: 'Informar nacionalidad con código Swift')
    - Obligacion_se_informara_el_pais_que_corresponda_ingresando_el_pertinente_codigo_swift_de_pa_f81670  (label: 'Informar nacionalidad con código Swift')
[Obligacion] 'informar numero de destinacion de exportacion' (2 nodos):
    - Obligacion_deber_de_informar_el_numero_de_destinacion_de_exportacion_para_la_cual_se_inform_bf0619  (label: 'Informar número de destinación de exportación')
    - Obligacion_debera_informarse_el_numero_de_embarque_o_destinacion_de_exportacion_que_se_denu_ea870e  (label: 'Informar número de destinación de exportación')
[Obligacion] 'informar tipo y numero de documento de identidad' (2 nodos):
    - Obligacion_se_informaran_el_tipo_y_numero_de_documento_de_identidad_de_los_responsables_con_b57e77  (label: 'Informar tipo y número de documento de identidad')
    - Obligacion_se_informaran_el_tipo_y_numero_de_documento_de_identidad_de_los_responsables_de__514c8f  (label: 'Informar tipo y número de documento de identidad')
[Obligacion] 'informar tipo y numero de identificacion fiscal' (2 nodos):
    - Obligacion_se_informaran_el_tipo_y_numero_de_identificacion_fiscal_de_los_responsables_teni_daebba  (label: 'Informar tipo y número de identificación fiscal')
    - Obligacion_se_informaran_el_tipo_y_numero_de_identificacion_fiscal_teniendo_en_cuenta_las_i_0889de  (label: 'Informar tipo y número de identificación fiscal')
[Obligacion] 'mantener procedimientos actualizados y adecuados' (2 nodos):
    - Obligacion_debera_prestarse_debida_atencion_al_mantenimiento_de_procedimientos_actualizados_7863d3  (label: 'Mantener procedimientos actualizados y adecuados')
    - Obligacion_la_direccion_debe_prestar_debida_atencion_al_mantenimiento_de_procedimientos_act_7ca28b  (label: 'Mantener procedimientos actualizados y adecuados')
[Obligacion] 'presentacion mensual de requerimiento' (2 nodos):
    - Obligacion_presentacion_mensual_del_requerimiento_a_partir_del_inicio_de_operaciones_con_ve_d1924a  (label: 'Presentación mensual de requerimiento')
    - Obligacion_presentar_mensualmente_el_requerimiento_de_informacion_sobre_consultas_y_reclamo_449e34  (label: 'Presentación mensual de requerimiento')
[Obligacion] 'redondeo de magnitudes segun primer digito de fracciones' (2 nodos):
    - Obligacion_se_incrementaran_los_valores_en_una_unidad_cuando_el_primer_digito_de_las_fracci_542925  (label: 'Redondeo de magnitudes según primer dígito de fracciones')
    - Obligacion_se_incrementaran_los_valores_en_una_unidad_cuando_el_primer_digito_de_las_fracci_c62d55  (label: 'Redondeo de magnitudes según primer dígito de fracciones')
[Obligacion] 'redondeo de magnitudes segun regla de digito' (2 nodos):
    - Obligacion_incrementar_valores_en_una_unidad_cuando_el_primer_digito_de_las_fracciones_sea__cc8548  (label: 'Redondeo de magnitudes según regla de dígito')
    - Obligacion_redondeo_de_magnitudes_incrementar_los_valores_en_una_unidad_cuando_el_primer_di_d197b5  (label: 'Redondeo de magnitudes según regla de dígito')
[Obligacion] 'registro de importes en miles de pesos' (3 nodos):
    - Obligacion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales__ri_ai_2_2_0beb2c  (label: 'Registro de importes en miles de pesos')
    - Obligacion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales__ri_tsa_3_1_9fe2c6  (label: 'Registro de importes en miles de pesos')
    - Obligacion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales__ribspc_s2_49526c  (label: 'Registro de importes en miles de pesos')
[Obligacion] 'registro de importes en miles de pesos sin decimales' (3 nodos):
    - Obligacion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales__ri_esd_sbloque1_9d0b4b  (label: 'Registro de importes en miles de pesos sin decimales')
    - Obligacion_registrar_los_importes_en_miles_de_pesos_sin_decimales__ri_psp_si_38454c  (label: 'Registro de importes en miles de pesos sin decimales')
    - Obligacion_registro_de_importes_en_miles_de_pesos_sin_decimales__ri_tsa_s1_ed4af5  (label: 'Registro de importes en miles de pesos sin decimales')
[Obligacion] 'responsabilidad consistencia datos reportados' (2 nodos):
    - Obligacion_las_entidades_reportantes_son_responsables_de_que_los_datos_a_presentar_sean_con_7b62cf  (label: 'Responsabilidad consistencia datos reportados')
    - Obligacion_las_entidades_reportantes_son_responsables_de_que_los_datos_a_presentar_sean_con_cb26de  (label: 'Responsabilidad consistencia datos reportados')
[Obligacion] 'vencimiento presentacion 20/2' (2 nodos):
    - Obligacion_el_vencimiento_para_la_presentacion_operara_el_dia_20_2_o_dia_habil_siguiente_si_3fc041  (label: 'Vencimiento presentación 20/2')
    - Obligacion_vencimiento_para_la_presentacion_del_informe_el_dia_20_de_febrero_o_dia_habil_si_675a64  (label: 'Vencimiento presentación 20/2')
[Operacion] 'certificacion de incumplido en gestion de cobro' (2 nodos):
    - Operacion_certificacion_de_incumplido_en_gestion_de_cobro__ri_secoexpo_sb_97a2eb  (label: 'Certificación de incumplido en gestión de cobro')
    - Operacion_certificacion_de_incumplido_en_gestion_de_cobro__ri_secoexpo_sbloque3_36fcf2  (label: 'Certificación de incumplido en gestión de cobro')
[Operacion] 'denuncia de incumplido' (2 nodos):
    - Operacion_denuncia_de_incumplido__ri_secoexpo_sb_2386a4  (label: 'Denuncia de incumplido')
    - Operacion_denuncia_de_incumplido__ri_secoexpo_sbloque2_a51a1d  (label: 'Denuncia de incumplido')
[Operacion] 'depositos en pesos y moneda extranjera' (2 nodos):
    - Operacion_depositos_en_pesos_y_moneda_extranjera__seggar_5_1_5d1ac2  (label: 'Depósitos en pesos y moneda extranjera')
    - Operacion_depositos_en_pesos_y_moneda_extranjera__seggar_s6_a6e361  (label: 'Depósitos en pesos y moneda extranjera')
[Operacion] 'emision de informe especial sobre cumplimiento normativo' (2 nodos):
    - Operacion_emision_de_informe_especial_sobre_cumplimiento_normativo__ri_iepsp_a_s1_e39c47  (label: 'Emisión de informe especial sobre cumplimiento normativo')
    - Operacion_emision_de_informe_especial_sobre_cumplimiento_normativo__ri_iesinap_a_s1_4efa4c  (label: 'Emisión de informe especial sobre cumplimiento normativo')
[Operacion] 'pago de cedin' (2 nodos):
    - Operacion_pago_de_cedin__cedin_13_2_3_ab7285  (label: 'Pago de CEDIN')
    - Operacion_pago_de_cedin__cedin_s12_8ceeb1  (label: 'Pago de CEDIN')
[Operacion] 'pago del cedin' (2 nodos):
    - Operacion_pago_del_cedin__cedin_12_3_b37ba6  (label: 'Pago del CEDIN')
    - Operacion_pago_del_cedin__cedin_13_1_5f8934  (label: 'Pago del CEDIN')
[Potestad] 'transmision del cedin por endoso' (2 nodos):
    - Potestad_transmision_del_cedin_por_endoso__el_cedin_podra_seguir_siendo_transmitido_media_048c41  (label: 'Transmisión del CEDIN por endoso')
    - Potestad_transmision_del_cedin_por_endoso__el_cedin_puede_transmitirse_entre_endosante_y__4363dc  (label: 'Transmisión del CEDIN por endoso')
[Restriccion] 'prohibicion de agregados al cuerpo del certificado' (2 nodos):
    - Restriccion_no_se_admiten_agregados_de_ningun_tipo_al_cuerpo_del_cedin__cedin_s14_bfe97b  (label: 'Prohibición de agregados al cuerpo del certificado')
    - Restriccion_no_se_admiten_agregados_de_ningun_tipo_al_cuerpo_del_certificado_en_el_endoso__c_9ebfa1  (label: 'Prohibición de agregados al cuerpo del certificado')
[Restriccion] 'prohibicion de registrar titulos profesionales' (2 nodos):
    - Restriccion_no_deberan_registrarse_titulos_profesionales_o_de_otro_tipo_en_el_campo_de_apell_18696f  (label: 'Prohibición de registrar títulos profesionales')
    - Restriccion_no_deberan_registrarse_titulos_profesionales_o_de_otro_tipo_en_los_nombres_infor_9ee25a  (label: 'Prohibición de registrar títulos profesionales')
[Restriccion] 'tope aporte adicional — una vez aporte normal' (2 nodos):
    - Restriccion_el_aporte_adicional_no_podra_superar_una_vez_el_aporte_normal__seggar_s3_00fe82  (label: 'Tope aporte adicional — una vez aporte normal')
    - Restriccion_el_aporte_adicional_resultante_de_la_ponderacion_de_factores_no_podra_superar_un_b4b20e  (label: 'Tope aporte adicional — una vez aporte normal')
[Sujeto] 'la entidad' (3 nodos):
    - Sujeto_propuesto_la_entidad  (label: 'la entidad')
    - Sujeto_propuesto_la_entidad__ri_nge  (label: 'la entidad')
    - Sujeto_propuesto_la_entidad__ri_sef  (label: 'la entidad')
[Sujeto] 'la informacion' (3 nodos):
    - Sujeto_propuesto_la_informacion  (label: 'La información')
    - Sujeto_propuesto_la_informacion__ri_ai  (label: 'La información')
    - Sujeto_propuesto_la_informacion__ri_tsa  (label: 'la información')
[Sujeto] 'las entidades' (19 nodos):
    - Sujeto_propuesto_las_entidades  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__cedin  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__consyr  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ri_acsf  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ri_ai  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ri_dsf  (label: 'Las entidades')
    - Sujeto_propuesto_las_entidades__ri_ii_31_12_19  (label: 'Las entidades')
    - Sujeto_propuesto_las_entidades__ri_laft  (label: 'Las entidades')
    - Sujeto_propuesto_las_entidades__ri_nge  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ri_ot  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ri_rcl  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ri_secoexpo  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ri_sef  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ri_tar  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ri_tsa  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ri_tvf  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ribspc  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__seggar  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__verac  (label: 'las entidades')
[TextoOrdenado] 'regimen informativo contable' (2 nodos):
    - TextoOrdenado_ri_bdp_pdf  (label: 'Régimen Informativo Contable')
    - TextoOrdenado_ri_rcl_pdf  (label: 'Régimen Informativo Contable')
[TextoOrdenado] 'regimen informativo contable mensual' (2 nodos):
    - TextoOrdenado_ri_nge_pdf  (label: 'Régimen Informativo Contable Mensual')
    - TextoOrdenado_ri_tar_pdf  (label: 'Régimen Informativo Contable Mensual')
```

### S8 — WARN

WARN — Colisión de label normalizado entre types distintos.

**Resultado:** 3 grupos con el mismo label normalizado en types distintos.

```
'emision de informe especial' (3 nodos):
    - [Obligacion] Obligacion_emitir_el_presente_informe_especial_basado_en_la_tarea_profesional_detallada_en__d5c517
    - [Obligacion] Obligacion_emitir_un_informe_especial_basado_en_la_tarea_profesional_para_cumplir_con_los_r_924955
    - [Operacion] Operacion_emision_de_informe_especial__ri_iesinap_a_s4_ae6a68
'presentacion del cedin ante entidad financiera' (2 nodos):
    - [Operacion] Operacion_presentacion_del_cedin_ante_entidad_financiera__cedin_s5_9c8698
    - [Potestad] Potestad_presentacion_del_cedin_ante_entidad_financiera__el_cedin_podra_presentarse_ante__3fb30d
'responsable de area gerencial' (2 nodos):
    - [Definicion] Definicion_responsable_de_area_gerencial__maximo_y_unico_responsable_por_area_con_cargo_jer_1f5a4f
    - [Sujeto] Sujeto_propuesto_responsable_de_area_gerencial
```

### S9 — PASS

ERROR — Descripción canónica: ningún nodo tiene a la vez 'descripcion' y 'description'.

**Resultado:** 0 nodos con ambas keys.

```
Tabla por type (usa cada key / ambas / ninguna):
  Comunicacion: descripcion=0, description=0, ambas=0, ninguna=49 (total 49)
  Condicion: descripcion=181, description=0, ambas=0, ninguna=0 (total 181)
  Definicion: descripcion=463, description=0, ambas=0, ninguna=0 (total 463)
  Excepcion: descripcion=68, description=0, ambas=0, ninguna=0 (total 68)
  Obligacion: descripcion=835, description=0, ambas=0, ninguna=15 (total 850)
  Operacion: descripcion=256, description=0, ambas=0, ninguna=0 (total 256)
  Potestad: descripcion=45, description=0, ambas=0, ninguna=0 (total 45)
  Restriccion: descripcion=94, description=0, ambas=0, ninguna=0 (total 94)
  Sujeto: descripcion=0, description=0, ambas=0, ninguna=171 (total 171)
  TextoOrdenado: descripcion=0, description=0, ambas=0, ninguna=30 (total 30)

Nodos con AMBAS keys (0):
```

### S10 — PASS

Todo nodo del dominio r2 de establecida_en (Condicion/Definicion/Excepcion/Obligacion/Operacion/Potestad/Restriccion) tiene >=1 arista saliente establecida_en.

**Resultado:** Sin establecida_en: Condicion=0, Definicion=0, Excepcion=0, Obligacion=0, Operacion=0, Potestad=0, Restriccion=0 (total 0).

```
Condicion: 0 sin establecida_en
Definicion: 0 sin establecida_en
Excepcion: 0 sin establecida_en
Obligacion: 0 sin establecida_en
Operacion: 0 sin establecida_en
Potestad: 0 sin establecida_en
Restriccion: 0 sin establecida_en
```

### S11 — WARN

Todo nodo del dominio r2 de aplica_a (Excepcion/Obligacion/Operacion/Potestad/Restriccion) tiene >=1 arista saliente aplica_a.

**Resultado:** Sin aplica_a: Excepcion=58, Obligacion=418, Operacion=239, Potestad=28, Restriccion=59 (total 802).

```
Excepcion: 58 sin aplica_a
    - Excepcion_cuando_el_domicilio_aun_no_cuente_con_la_codificacion_postal_del_nuevo_sistema_p_e3e9b0
    - Excepcion_cuando_no_se_cuente_con_pasaporte_se_consignara_otros_y_se_asignara_numeracion_c_eb5485
    - Excepcion_cuando_por_el_tipo_de_producto_no_resulte_exigible_la_identificacion_fiscal_se_i_608231
    - Excepcion_cuando_se_informe_la_opcion_otras_operaciones_no_mencionadas_en_los_items_preced_afcfe2
    - Excepcion_el_servicio_de_ayuda_economica_queda_excluido_del_encuadramiento_regulatorio_cua_5c0df2
    - Excepcion_es_admisible_la_presentacion_de_facturas_o_recibos_en_legal_forma_como_alternati_e9ab5f
    - Excepcion_exencion_del_impuesto_sobre_los_creditos_y_debitos_en_cuentas_bancarias_y_otras__aabde1
    - Excepcion_la_exigencia_de_antiguedad_minima_de_un_ano_no_aplica_a_integrantes_activos_o_ad_75ffcf
    - Excepcion_la_exigencia_de_colocar_la_leyenda_deposito_sin_garantia_no_regira_cuando_las_op_03470f
    - Excepcion_la_informacion_de_ubicacion_no_aplica_para_las_agencias_complementarias_de_servi_e35044
    - Excepcion_la_prestacion_del_servicio_de_ayuda_economica_queda_excluida_de_la_prohibicion_d_79579e
    - Excepcion_la_prestacion_del_servicio_de_ayuda_economica_queda_excluida_del_encuadramiento__ff9f06
    - Excepcion_las_adendas_que_impliquen_incorporar_o_discontinuar_actividades_delegadas_quedan_5c042a
    - Excepcion_las_asociaciones_mutuales_y_cooperativas_quedan_exceptuadas_del_requerimiento_de_ee7618
    - Excepcion_las_entidades_financieras_que_consoliden_con_otra_s_entidad_es_financiera_s_qued_bf5463
    - Excepcion_las_entidades_financieras_que_no_sean_sucursales_de_entidades_extranjeras_quedan_05aeae
    - Excepcion_las_personas_juridicas_domiciliadas_en_territorio_nacional_que_sean_consideradas_658d52
    - Excepcion_los_saldos_inmovilizados_provenientes_de_depositos_y_otras_operaciones_excluidas_0fc68c
    - Excepcion_no_aplica_el_vencimiento_del_dia_22_a_los_regimenes_que_tienen_un_vencimiento_di_3d28f9
    - Excepcion_no_aplica_la_ausencia_de_vencimiento_en_lo_que_corresponda_en_materia_de_prescri_545fdc
    - Excepcion_no_aplica_la_consignacion_de_cese_cuando_hay_reeleccion_para_el_mismo_cargo_debe_cf0aff
    - Excepcion_no_aplica_la_obligacion_de_presentacion_a_los_pnfc_y_psp_no_considerados_como_su_120efa
    - Excepcion_no_aplica_lo_previsto_en_el_punto_3_3_cuando_se_trate_de_cheques_pagados_present_b8481f
    - Excepcion_no_aplica_lo_previsto_en_el_punto_3_4_certificacion_de_las_reproducciones_cuando_856b16
    - Excepcion_no_es_necesario_informar_el_ingreso_total_de_las_divisas_pendientes_de_una_desti_cec6e2
    - Excepcion_no_es_requisito_que_los_profesionales_o_asociaciones_de_profesionales_se_encuent_a22200
    - Excepcion_no_se_completara_la_informacion_relativa_a_votos_para_entidades_constituidas_baj_d5ae9a
    - Excepcion_no_se_debe_suministrar_informacion_de_accionistas_cuando_el_accionista_sea_otra__e83e88
    - Excepcion_no_se_informara_al_b_c_r_a_ni_a_aquellos_deudores_cuyo_saldo_de_deuda_sea_inferi_b353e5
    - Excepcion_no_se_informara_el_tipo_de_cupon_para_titulos_representativos_de_capital_accione_6a34b6
    - Excepcion_no_se_informaran_el_bcra_ni_los_deudores_cuyo_saldo_de_deuda_sea_inferior_a_25_m_ed952a
    - Excepcion_no_se_informaran_el_tipo_y_numero_de_identificacion_fiscal_para_los_estados_naci_6c704b
    - Excepcion_no_se_informaran_los_datos_15_a_19_cuando_no_hubiera_ninguna_aplicacion_parcial__4b969d
    - Excepcion_no_se_realizaran_las_verificaciones_previstas_en_el_punto_7_cuando_el_cedin_se_e_337225
    - Excepcion_no_se_realizaran_las_verificaciones_previstas_en_el_punto_cuando_el_cedin_se_enc_cd2f6c
    - Excepcion_no_se_requiere_informacion_en_el_dato_de_identificacion_de_la_financiacion_cuand_937d81
    - Excepcion_para_los_reportes_b_4_y_b_5_el_dato_nro_de_identificacion_no_se_informara_except_f92a4b
    - Excepcion_queda_exceptuada_de_la_regla_de_conservacion_a_partir_de_los_2_anos_la_documenta_deca05
    - Excepcion_quedan_exceptuadas_del_regimen_informativo_las_asociaciones_mutuales_y_cooperati_506828
    - Excepcion_quedan_exceptuados_de_la_obligacion_de_presentar_informes_aquellos_pnfc_y_psp_no_9e5bc7
    - Excepcion_quedan_excluidos_de_la_cobertura_de_la_garantia_los_depositos_e_inversiones_a_pl_997177
    - Excepcion_quedan_excluidos_de_la_cobertura_del_seguro_de_garantia_los_cedip_transmitidos_a_537f53
    - Excepcion_quedan_excluidos_de_la_garantia_los_depositos_a_la_vista_en_los_que_se_convengan_e10bcd
    - Excepcion_quedan_excluidos_de_la_garantia_los_depositos_adquiridos_por_endoso__seggar_s6_7a5ac8
    - Excepcion_quedan_excluidos_de_la_garantia_los_depositos_captados_a_tasas_superiores_a_la_d_b8b351
    - Excepcion_quedan_excluidos_de_la_garantia_los_depositos_cuando_los_limites_de_tasa_de_inte_56bcf9
    - Excepcion_quedan_excluidos_de_la_garantia_los_depositos_e_inversiones_a_plazo_que_superen__925324
    - Excepcion_quedan_excluidos_de_la_garantia_los_depositos_efectuados_por_personas_vinculadas_6cd717
    - Excepcion_quedan_excluidos_de_la_garantia_los_depositos_efectuados_por_personas_vinculadas_c70df8
    - Excepcion_quedan_excluidos_de_los_alcances_de_la_garantia_los_depositos_a_plazo_fijo_de_ti_dc8c19
    - Excepcion_se_exceptua_de_la_prohibicion_de_percibir_cargos_la_percepcion_por_los_conceptos_94d601
    - Excepcion_se_excluyen_del_calculo_de_la_tasa_promedio_los_prestamos_otorgados_para_refinan_746fdc
    - Excepcion_se_excluyen_las_asistencias_previstas_en_el_punto_2_2_de_las_normas_sobre_relaci_c5441d
    - Excepcion_se_excluyen_las_financiaciones_que_se_encuentren_cubiertas_con_garantias_preferi_bcc582
    - Excepcion_se_excluyen_las_partidas_deducibles_de_la_rpc__ri_ai_3_3_f19601
    - Excepcion_se_excluyen_los_activos_sujetos_a_inmovilizacion_informados_en_otros_codigos__ri_a98f26
    - Excepcion_se_suspende_la_observancia_de_las_regulaciones_tecnicas_sobre_base_consolidada_t_e84893
    - Excepcion_suspension_de_la_observancia_de_las_regulaciones_tecnicas_sobre_base_consolidada_42809b
Obligacion: 418 sin aplica_a
    - Obligacion_a_los_fines_de_informar_los_datos_correspondientes_a_las_tarjetas_de_credito_los_75b9ea
    - Obligacion_a_los_fines_del_redondeo_de_las_magnitudes_se_incrementaran_los_valores_en_una_u_b555b4
    - Obligacion_a_los_fines_del_redondeo_de_las_magnitudes_se_incrementaran_los_valores_en_una_u_c9ecd7
    - Obligacion_a_los_fines_del_redondeo_de_las_magnitudes_se_incrementaran_los_valores_en_una_u_f52a2c
    - Obligacion_agrupacion_de_cada_partida_segun_el_medio_de_pago_y_esquema_de_pago_correspondie_8fec43
    - Obligacion_ante_incumplimiento_de_las_disposiciones_se_aplicara_el_regimen_disciplinario_de_684206
    - Obligacion_ante_la_identificacion_de_un_nuevo_riesgo_o_modificacion_relevante_de_uno_existe_b7f93c
    - Obligacion_calculo_de_la_cantidad_de_productos_al_cierre_de_cada_mes_para_cada_producto_o_s_a0b791
    - Obligacion_clasificacion_de_transferencias_segun_el_modelo_de_informacion_del_punto_iii_2_d_4adafb
    - Obligacion_codificar_los_productos_conforme_a_la_tabla_1_anexa_a_la_presente_seccion__ri_ts_52fd28
    - Obligacion_con_respecto_a_las_personas_juridicas_se_informara_segun_el_pais_de_domicilio__r_df3525
    - Obligacion_considerar_partidas_contables_de_activo_pasivo_exceptuando_saldos_deudores_acree_c3953e
    - Obligacion_consignar_el_codigo_de_moneda_siguiendo_las_disposiciones_del_quinto_parrafo_de__e24dfc
    - Obligacion_consignar_la_cantidad_de_casos_con_resoluciones_en_contra_del_usuario_en_el_peri_83677f
    - Obligacion_cuando_aun_no_se_haya_inscripto_la_subdivision_de_las_unidades_en_el_registro_de_84c821
    - Obligacion_cuando_el_deudor_no_este_incluido_en_el_padron_de_la_afip_debe_informarse_segun__c74443
    - Obligacion_cuando_el_deudor_no_este_incluido_en_el_padron_de_la_afip_debera_informarse_segu_8b4c84
    - Obligacion_cuando_el_domicilio_no_posea_numero_debe_informarse_entre_que_calles_o_en_que_es_3e665d
    - Obligacion_cuando_el_fiduciario_contrata_empresa_constructora_para_realizar_la_obra_debe_ex_c1b005
    - Obligacion_cuando_el_titular_no_este_incluido_en_el_padron_de_personas_fisicas_y_juridicas__cec5e5
    - Obligacion_cuando_existan_tenencias_cuyos_titulares_no_puedan_ser_identificados_agruparlas__f73a72
    - Obligacion_cuando_existe_participacion_directa_en_el_capital_social_debe_informarse_el_porc_097315
    - Obligacion_cuando_importes_se_registren_en_cuentas_distintas_del_capital_informar_saldos_co_00a762
    - Obligacion_cuando_la_contraparte_significativa_sea_un_fondo_comun_de_inversion_identificarl_a948cd
    - Obligacion_cuando_los_importes_se_encuentren_denominados_en_pesos_aplicar_el_tipo_de_cambio_8d65b7
    - Obligacion_cuando_se_informen_tramites_de_traslados_de_unidades_de_servicios_los_datos_corr_fa7fc8
    - Obligacion_cuando_una_persona_sea_designada_para_un_cargo_distinto_al_que_ocupaba_consignar_7f849e
    - Obligacion_cumplimiento_de_los_requerimientos_de_etica_establecidos_por_la_rt_37__ri_iesina_a059d0
    - Obligacion_cupones_cortados_y_no_cobrados_de_amortizacion_interes_y_amortizacion_e_interes__cb9799
    - Obligacion_dato_que_debe_consignarse_en_la_solicitud_de_baja_de_reportes_codigo_de_reporte__ecf083
    - Obligacion_dato_que_debe_consignarse_en_la_solicitud_de_baja_de_reportes_cuit_del_exportado_c47730
    - Obligacion_dato_que_debe_consignarse_en_la_solicitud_de_baja_de_reportes_motivo_de_baja_com_859eda
    - Obligacion_dato_que_debe_consignarse_en_la_solicitud_de_baja_de_reportes_numero_de_destinac_0a36d7
    - Obligacion_dato_que_debe_consignarse_en_la_solicitud_de_baja_de_reportes_numero_de_identifi_69e655
    - Obligacion_de_reunir_los_requisitos_citados_se_consignara_en_la_partida_401_la_porcion_pert_149af4
    - Obligacion_debe_consignarse_si_la_unidad_se_encuentra_dentro_de_la_sede_con_funcionamiento__9bbb72
    - Obligacion_deber_de_considerar_la_mayor_cantidad_de_elementos_de_juicio_disponibles_para_la_1f6a96
    - Obligacion_deber_de_considerar_las_tasas_nominales_anuales_maximas_aplicadas_respecto_de_la_02ca29
    - Obligacion_deber_de_consignar_el_plazo_promedio_de_resolucion_expresado_en_cantidad_de_dias_6f3b8b
    - Obligacion_deber_de_consignar_la_cantidad_de_casos_en_que_se_resolvio_a_favor_del_usuario_e_abee8c
    - Obligacion_deber_de_emplear_papel_de_seguridad_que_cuente_con_marca_de_agua_exclusiva_de_ca_5ab9d6
    - Obligacion_deber_de_formalizar_un_acta_de_apertura_del_proceso_de_reproduccion_que_contenga_d90dc7
    - Obligacion_deber_de_incluir_en_la_certificacion_de_obra_datos_del_inmueble_destino_habitaci_99ca1a
    - Obligacion_deber_de_incluir_en_los_certificados_de_obra_todos_los_componentes_del_costo_de__26fa82
    - Obligacion_deber_de_informar_el_c_u_i_t_del_exportador_en_la_certificacion_de_extension_de__c50b8b
    - Obligacion_deber_de_informar_el_codigo_de_extension_que_debe_corresponder_a_los_codigos_esp_22cabd
    - Obligacion_deber_de_informar_el_codigo_de_la_tabla_no_8_que_corresponda_al_tipo_de_responsa_8b5ab4
    - Obligacion_deber_de_informar_el_numero_de_destinacion_de_exportacion_para_la_cual_se_inform_bf0619
    - Obligacion_deber_de_informar_la_actividad_de_los_deudores_comerciales_y_los_que_pertenezcan_a015f6
    - Obligacion_deber_de_informar_la_fecha_de_cumplido_de_embarque_otorgada_por_la_aduana__ri_se_d24d60
    - Obligacion_deber_de_informar_la_fecha_y_numero_de_la_resolucion_del_bcra_que_se_haya_expedi_e3b6c3
    - Obligacion_deber_de_informar_la_identificacion_de_la_financiacion_mediante_el_numero_de_la__bf12de
    - Obligacion_deber_de_informar_la_nueva_fecha_de_vencimiento_para_la_liquidacion_de_divisas___5b5427
    - Obligacion_deber_de_informar_los_aumentos_reducciones_y_o_altas_de_tarifas_respecto_de_las__a63a60
    - Obligacion_deber_de_informar_los_datos_de_operaciones_de_consumo_totalizados_por_mes_incluy_24a4ee
    - Obligacion_deber_de_informar_los_datos_totalizando_la_cantidad_de_terminales_de_punto_de_ve_2d25b7
    - Obligacion_deber_de_informar_los_mismos_datos_mas_el_indicado_en_el_punto_5_13_con_relacion_66725b
    - Obligacion_deber_de_informar_los_puntos_5_1_a_5_12_respecto_de_los_funcionarios_nombrados_c_2c09e9
    - Obligacion_deber_de_mencionar_en_la_certificacion_el_numero_de_soporte_de_informacion_gener_2ac38c
    - Obligacion_deber_de_notificar_el_descuento_estimado_que_el_mercado_secundario_o_el_pertinen_f936f4
    - Obligacion_deber_de_que_todo_certificado_de_obra_acompanado_parcial_o_final_cumpla_con_los__c48f48
    - Obligacion_deber_de_remitir_informacion_vinculada_con_el_precio_vigente_el_precio_previsto__13e462
    - Obligacion_deber_de_utilizar_el_codigo_999_cuando_se_trate_de_personas_fisicas_no_comprendi_dec06a
    - Obligacion_deber_de_utilizar_el_esquema_inserto_en_el_cuadro_6_para_la_confeccion_de_la_inf_c3137b
    - Obligacion_debera_consignarse_el_codigo_postal_correspondiente_al_nuevo_sistema_de_codifica_49c9ba
    - Obligacion_debera_consignarse_el_numero_interno_de_incumplido_asignado_por_la_entidad__ri_s_6de211
    - Obligacion_debera_consignarse_la_posicion_arancelaria_cuyo_valor_fob_es_el_mas_representati_6bb70d
    - Obligacion_debera_informarse_el_c_u_i_t_del_exportador_y_su_razon_social_o_denominacion_en__db2261
    - Obligacion_debera_informarse_el_codigo_de_divisa_del_valor_fob_de_acuerdo_con_codificacion__1ae598
    - Obligacion_debera_informarse_el_codigo_de_imputacion__ri_secoexpo_sbloque2_f99a40
    - Obligacion_debera_informarse_el_monto_pendiente_de_liquidacion_y_o_negociacion_a_la_fecha_d_e13be9
    - Obligacion_debera_informarse_el_numero_de_embarque_o_destinacion_de_exportacion_que_se_denu_ea870e
    - Obligacion_debera_informarse_el_numero_de_secuencia_de_liquidaciones_aplicaciones_u_otras_i_5a962b
    - Obligacion_debera_informarse_el_numero_otorgado_a_la_certificacion_de_cumplido_de_la_destin_a303d3
    - Obligacion_debera_informarse_el_valor_de_otros_elementos_incluidos_en_la_condicion_de_venta_0b0011
    - Obligacion_debera_informarse_el_valor_fob_de_la_destinacion__ri_secoexpo_sbloque2_e29ab9
    - Obligacion_debera_informarse_la_fecha_de_cumplido_de_embarque_otorgada_por_la_aduana__ri_se_776f03
    - Obligacion_debera_informarse_la_fecha_de_cumplido_fecha_de_la_ultima_imputacion_solo_en_el__5b59e6
    - Obligacion_debera_informarse_la_fecha_de_imputacion__ri_secoexpo_sbloque2_7d4e0c
    - Obligacion_debera_informarse_la_fecha_de_oficializacion_de_la_destinacion_de_exportacion__r_3b3349
    - Obligacion_debera_informarse_la_fecha_de_vencimiento_para_la_liquidacion_de_divisas_aplicab_d2f7c5
    - Obligacion_debera_proporcionarse_la_clave_unica_de_identificacion_tributaria_c_u_i_t_del_su_864446
    - Obligacion_debera_remitirse_informacion_que_incluya_el_precio_vigente_el_precio_previsto_el_8eb992
    - Obligacion_devolucion_de_toda_la_documentacion_a_la_entidad_presentante_cuando_existan_disc_7018d6
    - Obligacion_discriminar_por_especie_y_en_proporcion_del_patrimonio_del_fondo_o_fideicomiso_l_5d5b29
    - Obligacion_distribuir_el_saldo_al_cierre_del_trimestre_por_bandas_temporales_segun_su_estru_32810d
    - Obligacion_efectuar_calculo_en_base_consolidada_trimestral_considerando_las_disposiciones_e_a4b6e8
    - Obligacion_efectuar_calculo_en_base_individual_entidad_financiera_y_sucursales_en_el_pais_u_bfa319
    - Obligacion_el_acta_de_retencion_debe_ser_suscripta_por_el_funcionario_que_efectuo_el_rechaz_000ce4
    - Obligacion_el_campo_de_participacion_debe_ser_integrado_unicamente_cuando_existe_una_partic_5187c9
    - Obligacion_el_dato_codigo_de_imputacion_debe_corresponder_a_uno_de_los_codigos_de_la_tabla__43f3e4
    - Obligacion_el_dato_sobre_el_inciso_del_punto_que_contempla_la_excepcion_a_integrar_como_inf_d9547c
    - Obligacion_el_dato_sobre_el_inciso_normativo_que_preve_el_mecanismo_a_integrar_como_informa_1ed0b3
    - Obligacion_el_dato_valor_pendiente_debe_coincidir_con_el_valor_que_surge_de_restar_al_valor_831dc9
    - Obligacion_el_endoso_en_el_certificado_debera_contener_el_domicilio_del_endosante__cedin_s4_b29c9d
    - Obligacion_el_endoso_en_el_certificado_debera_contener_la_aclaracion_de_identidad_del_endos_3b3527
    - Obligacion_el_endoso_en_el_certificado_debera_contener_la_firma_del_endosante__cedin_s4_3e5412
    - Obligacion_el_endoso_en_el_certificado_debera_contener_los_datos_de_identificacion_tributar_56beed
    - Obligacion_el_equivalente_en_dolares_estadounidenses_del_monto_pendiente_de_cumplimiento_se_6fcbcb
    - Obligacion_el_estado_de_situacion_del_certificado_de_inversion_los_datos_ingresados_y_su_ha_2ba988
    - Obligacion_el_importe_debe_corresponder_al_precio_de_una_operacion_individual_e_incluir_el__f1e50d
    - Obligacion_el_informe_anual_del_revisor_externo_independiente_debera_ser_enviado_junto_con__2beb60
    - Obligacion_el_informe_debe_certificar_la_situacion_en_la_materia_al_01_11_22__ri_ieccm_s3_e7177c
    - Obligacion_el_informe_debe_contener_ademas_la_opinion_sobre_el_cumplimiento_de_las_normas_s_6fa846
    - Obligacion_el_informe_debe_realizarse_conforme_al_modelo_y_procedimientos_establecidos_en_e_35c629
    - Obligacion_el_informe_debe_ser_elaborado_por_profesionales_o_asociaciones_de_profesionales__88a4a6
    - Obligacion_el_informe_debera_ser_elaborado_por_profesionales_o_asociaciones_de_profesionale_2d782e
    - Obligacion_el_informe_tecnico_de_autoevaluacion_de_riesgos_de_la_ft_y_su_metodologia_y_la_d_5da8e4
    - Obligacion_el_mismo_criterio_de_consistencia_debe_aplicarse_al_informar_la_cartera_que_cons_8ca51f
    - Obligacion_el_monto_de_la_garantia_debe_distribuirse_proporcionalmente_entre_los_titulares__839168
    - Obligacion_el_presente_regimen_informativo_se_presentara_con_las_formalidades_del_regimen_i_3a4ce0
    - Obligacion_el_regimen_informativo_se_presentara_por_semana_estadistica_con_vencimiento_a_la_88b2a4
    - Obligacion_el_requerimiento_abarcara_el_periodo_comprendido_entre_el_1_1_y_el_31_12_de_cada_e68bfa
    - Obligacion_el_sistema_de_seguro_de_garantia_de_los_depositos_debe_disponer_el_reintegro_a_s_cf1e3d
    - Obligacion_el_tarifario_completo_debe_incluir_las_comisiones_nomencladas_conforme_al_aparta_8701c6
    - Obligacion_el_tarifario_debe_cumplir_con_todas_las_condiciones_e_informacion_requerida_por__cc9cf2
    - Obligacion_el_tarifario_debe_incluir_el_mes_de_vigencia__ri_transpa_sb_07a5e9
    - Obligacion_el_tarifario_debe_incluir_informacion_sobre_aumentos_notificados_a_los_clientes__77af02
    - Obligacion_el_tarifario_debe_incluir_la_denominacion_de_la_entidad__ri_transpa_sb_7d591c
    - Obligacion_el_tarifario_debe_incluir_las_tarifas__ri_transpa_sb_243529
    - Obligacion_el_tarifario_debe_incluir_las_tasas__ri_transpa_sb_e5bd23
    - Obligacion_el_tenedor_desposeido_debe_comunicar_de_inmediato_el_extravio_sustraccion_o_dest_9969df
    - Obligacion_el_valor_total_imputado_debera_expresarse_en_la_moneda_consignada_para_el_valor__914763
    - Obligacion_el_vencimiento_del_informe_opera_el_dia_20_12_2022__ri_ieccm_s3_b4af90
    - Obligacion_el_vencimiento_para_la_presentacion_operara_el_dia_20_2_o_dia_habil_siguiente_si_3fc041
    - Obligacion_el_vencimiento_para_las_presentaciones_de_los_informes_operara_el_dia_20_o_dia_h_99c817
    - Obligacion_el_vendedor_debe_presentar_copia_autenticada_por_el_escribano_interviniente_de_l_d009e9
    - Obligacion_emitir_el_presente_informe_especial_basado_en_la_tarea_profesional_detallada_en__d5c517
    - Obligacion_emitir_un_informe_especial_basado_en_la_tarea_profesional_para_cumplir_con_los_r_924955
    - Obligacion_en_aquellos_cargos_relacionados_con_el_concepto_responsable_de_otras_gerencias_s_7dce4d
    - Obligacion_en_caso_de_informar_un_certificado_de_participacion_o_titulo_de_deuda_de_fideico_f71b23
    - Obligacion_en_caso_de_que_el_cedin_no_se_encuentre_identificado_como_ya_aplicado_a_los_dest_808ece
    - Obligacion_en_caso_de_una_cesion_consignar_ent_cedente_en_el_dato_codigo_ventaja_opcion_y_e_0fa905
    - Obligacion_en_caso_que_el_tramite_informado_se_trate_de_la_apertura_de_una_sucursal_no_prev_85d0e1
    - Obligacion_en_el_acta_de_retencion_se_deben_asentar_todas_las_caracteristicas_y_datos_del_c_0aad10
    - Obligacion_en_la_informacion_adicional_1_correspondiente_al_codigo_a16_se_debera_consignar__cef061
    - Obligacion_en_la_informacion_adicional_2_de_los_codigos_a11_a12_y_a13_se_debera_indicar_si__ee3a40
    - Obligacion_en_las_solicitudes_de_autorizacion_de_unidades_de_servicios_en_el_exterior_no_se_5bcea1
    - Obligacion_en_los_casos_de_adelantos_se_informara_cada_cuenta_corriente_con_saldo_deudor__r_dac1dd
    - Obligacion_en_los_casos_de_solicitud_de_acceso_al_servicio_de_cobro_con_transferencia_la_pr_1ad686
    - Obligacion_en_los_casos_de_unidad_en_sede_con_funcionamiento_las_24_horas_o_alejada_de_la_e_0e3876
    - Obligacion_en_los_casos_en_que_no_se_haya_especificado_el_alcance_de_las_franquicias_el_cri_34ee54
    - Obligacion_en_lugar_de_la_fecha_de_creacion_correspondera_informar_la_fecha_de_canje_en_el__f87dab
    - Obligacion_en_reemplazo_de_la_identidad_tipo_y_numero_de_identificacion_del_cedin_original__3a7c7f
    - Obligacion_en_todos_los_casos_la_documentacion_debe_incluir_la_mencion_de_haber_sido_cancel_fa6355
    - Obligacion_es_necesario_unificar_los_criterios_aplicables_al_presente_regimen_a_partir_de_l_813557
    - Obligacion_especificar_en_el_dato_codigo_ventaja_opcion_a_que_tipo_de_dato_se_hace_referenc_016ce7
    - Obligacion_identificar_deudores_que_posean_financiaciones_en_que_al_menos_para_una_de_ellas_41abc5
    - Obligacion_identificar_la_contraparte_significativa_mediante_clave_de_identificacion_c_d_i__d5c3ab
    - Obligacion_identificar_la_contraparte_significativa_mediante_clave_unica_de_identificacion__ed668c
    - Obligacion_identificar_la_contraparte_significativa_mediante_codigo_unico_de_identificacion_74f186
    - Obligacion_incluir_adicionalmente_una_partida_residual_denominada_otras_agencias_donde_se_a_b71784
    - Obligacion_incrementar_valores_en_una_unidad_cuando_el_primer_digito_de_las_fracciones_sea__cc8548
    - Obligacion_indicar_en_la_solicitud_la_clausula_o_punto_del_contrato_donde_se_encuentra_cont_03190a
    - Obligacion_indicar_en_la_solicitud_la_clausula_o_punto_del_contrato_donde_se_encuentra_cont_0db920
    - Obligacion_indicar_en_la_solicitud_la_clausula_o_punto_del_contrato_donde_se_encuentra_cont_2b6462
    - Obligacion_indicar_en_la_solicitud_la_clausula_o_punto_del_contrato_donde_se_encuentra_cont_4d89a8
    - Obligacion_indicar_en_la_solicitud_la_clausula_o_punto_del_contrato_donde_se_encuentra_cont_5e142a
    - Obligacion_indicar_en_la_solicitud_la_clausula_o_punto_del_contrato_donde_se_encuentra_cont_6d7a14
    - Obligacion_indicar_en_la_solicitud_la_clausula_o_punto_del_contrato_donde_se_encuentra_cont_84e2c0
    - Obligacion_indicar_en_la_solicitud_la_clausula_o_punto_del_contrato_donde_se_encuentra_cont_92df48
    - Obligacion_indicar_en_la_solicitud_la_clausula_o_punto_del_contrato_donde_se_encuentra_cont_a14930
    - Obligacion_indicar_en_la_solicitud_la_clausula_o_punto_del_contrato_donde_se_encuentra_cont_c5872c
    - Obligacion_indicar_en_la_solicitud_la_clausula_o_punto_del_contrato_donde_se_encuentra_cont_ef582c
    - Obligacion_indicar_si_la_contraparte_es_vinculada_o_no_a_la_entidad_financiera__ri_tsa_s3_5b514c
    - Obligacion_informacion_de_cantidad_total_de_clientes_desagregados_por_uso_comercial_o_perso_cc3a86
    - Obligacion_informacion_de_cantidad_total_de_clientes_involucrados_en_transacciones_y_transf_3d1055
    - Obligacion_informacion_de_cantidad_total_de_cuentas_de_pago_desagregadas_por_uso_comercial__52efd0
    - Obligacion_informacion_de_cantidad_total_de_cuentas_de_pago_involucradas_en_transacciones_y_c0aa9f
    - Obligacion_informacion_de_la_cantidad_de_tarjetas_titulares_en_el_caso_de_tarjetas_de_credi_ce728f
    - Obligacion_informacion_de_la_tasa_efectiva_anual_expresada_en_porcentaje_con_dos_decimales__0778c9
    - Obligacion_informacion_de_la_tasa_efectiva_anual_expresada_en_porcentaje_con_dos_decimales__4a1f72
    - Obligacion_informacion_de_la_tasa_efectiva_anual_expresada_en_porcentaje_con_dos_decimales__57c310
    - Obligacion_informacion_de_la_tasa_efectiva_anual_expresada_en_porcentaje_con_dos_decimales__a7d17b
    - Obligacion_informacion_de_tarifas_en_pesos_excepto_comision_por_uso_de_cajeros_automaticos__fa9ef6
    - Obligacion_informacion_de_tarifas_vigentes_correspondientes_a_valores_maximos_sin_deducir_b_aa47a0
    - Obligacion_informacion_del_importe_de_la_tarifa_para_el_periodo_completo_establecido_en_la__f138f2
    - Obligacion_informacion_trimestral_segun_codigos_de_modelos__ri_tsa_s1_65a5dc
    - Obligacion_informar_acerca_de_las_cesiones_del_seguimiento__ri_secoexpo_sa_082fc8
    - Obligacion_informar_datos_de_contacto_nombre_y_apellido_telefono_de_contacto_y_correo_elect_a62f14
    - Obligacion_informar_el_codigo_de_esquema_de_pago_utilizado_de_acuerdo_con_la_tabla_2__ri_ps_9ae2f8
    - Obligacion_informar_el_codigo_del_proveedor_de_la_billetera_digital_interoperable_registrad_4f6953
    - Obligacion_informar_el_codigo_del_rubro_de_comercio_mcc_segun_tabla_6_que_recibe_los_fondos_0a8eaa
    - Obligacion_informar_el_importe_para_las_bandas_temporales_1_mes_1_a_3_meses_4_a_6_meses_7_a_14c283
    - Obligacion_informar_el_lugar_de_emision_de_la_tarjeta_utilizada_pais_o_exterior_segun_la_ta_686f82
    - Obligacion_informar_el_saldo_de_los_contratos_vigentes_al_cierre_del_trimestre_respecto_de__a37178
    - Obligacion_informar_el_saldo_para_las_bandas_temporales_1_mes_1_a_3_meses_4_a_6_meses_7_a_1_553364
    - Obligacion_informar_intereses_y_ajustes_devengados_cuando_corresponda_y_otras_partidas_acce_7de406
    - Obligacion_informar_la_cantidad_de_locales_o_sucursales_de_las_agencias_complementarias_inc_e4d90b
    - Obligacion_informar_la_cantidad_total_de_operaciones_de_adquirencia_totalizando_las_operaci_9a5dc3
    - Obligacion_informar_los_datos_solicitados_en_los_puntos_2_13_a_2_21_de_la_seccion_de_direct_07d97a
    - Obligacion_informar_los_mismos_datos_mas_el_indicado_en_el_punto_3_11_con_relacion_a_aquell_d3762d
    - Obligacion_informar_mensualmente_las_modificaciones_en_el_codigo_postal_derivadas_de_cambio_461631
    - Obligacion_informar_mensualmente_los_cambios_que_pudieran_producirse_en_la_condicion_de_per_c5c8b9
    - Obligacion_informar_mensualmente_los_clientes_dados_de_baja_en_el_mes_bajo_informe__ri_bdp__b669e2
    - Obligacion_informar_mensualmente_los_clientes_incorporados_en_el_mes_bajo_informe__ri_bdp_s_499c8a
    - Obligacion_informar_para_cada_especie_la_totalidad_de_partidas_con_saldo_correspondiente_a__9a3aa6
    - Obligacion_informar_sobre_la_base_del_trabajo_realizado_que_de_los_procedimientos_ejecutado_50255c
    - Obligacion_informar_sobre_la_base_del_trabajo_realizado_que_de_los_procedimientos_ejecutado_b0510c
    - Obligacion_informar_una_unica_casilla_de_correo_electronico_a_utilizar_tanto_por_el_titular_bee7c0
    - Obligacion_junto_con_la_presentacion_de_los_apartados_c_y_d_debe_adjuntarse_un_archivo_con__493e2b
    - Obligacion_la_autoevaluacion_de_riesgo_y_la_revision_externa_independiente_pueden_realizars_7083b5
    - Obligacion_la_calidad_de_las_financiaciones_estara_determinada_en_funcion_de_las_normas_sob_381b66
    - Obligacion_la_certificacion_de_obra_debe_incluir_datos_del_inmueble_costo_de_la_refaccion_a_a671ba
    - Obligacion_la_comunicacion_del_inicio_de_actividades_implicara_la_obligacion_de_presentar_c_686092
    - Obligacion_la_declaracion_jurada_debe_contar_con_legalizacion_del_consejo_profesional_de_ci_9ab896
    - Obligacion_la_documentacion_debe_incluir_la_mencion_de_haber_sido_cancelada_mediante_la_apl_8d3c21
    - Obligacion_la_entidad_financiera_debe_remitir_al_bcra_el_certificado_rechazado_el_acta_de_r_4ee35d
    - Obligacion_la_entidad_financiera_debe_retener_los_documentos_presentados_que_deberan_encont_30fa56
    - Obligacion_la_informacion_consolidada_mensual_debe_incluir_las_operaciones_de_los_entes_pre_15bfd2
    - Obligacion_la_informacion_que_las_entidades_publiquen_en_sus_sitios_de_internet_debe_ser_co_a0131d
    - Obligacion_la_informacion_se_integrara_mensualmente_con_los_datos_correspondientes_al_inven_df5e5b
    - Obligacion_la_informacion_se_remitira_de_acuerdo_con_lo_establecido_en_las_normas_sobre_pre_52cca1
    - Obligacion_la_notificacion_debe_contener_el_importe_numero_y_serie_del_cedin_descripcion_de_3b4361
    - Obligacion_la_persona_que_presento_el_cedin_sera_invitada_a_suscribir_el_acta_de_retencion__6c1af0
    - Obligacion_la_presentacion_anual_correspondiente_al_ano_en_que_se_produce_la_solicitud_en_e_2251c0
    - Obligacion_la_presentacion_de_la_informacion_debera_realizarse_con_la_antelacion_prevista_e_1a8ace
    - Obligacion_la_presentacion_se_considerara_validada_cuando_todas_las_categorias_establecidas_003793
    - Obligacion_la_remision_de_nuevos_datos_con_un_numero_de_incumplimiento_ya_reportado_debera__43ad60
    - Obligacion_la_serie_y_numeracion_del_cedin_deberan_constar_en_el_cuerpo_del_certificado_y_e_b26853
    - Obligacion_la_situacion_que_correspondera_informar_hasta_la_cancelacion_de_la_financiacion__6c1b2c
    - Obligacion_las_altas_de_comisiones_de_nuevos_productos_y_o_servicios_deben_identificarse_es_b0558c
    - Obligacion_las_comisiones_previstas_en_el_apartado_a_deben_incorporarse_en_el_tarifario_con_73530f
    - Obligacion_las_comisiones_seran_abonadas_por_el_suscriptor_del_cedin_punto_1_1__cedin_13_2_322830
    - Obligacion_las_comisiones_seran_abonadas_por_quien_lo_presente_al_cobro_punto_8__cedin_13_2_bdbf09
    - Obligacion_las_comisiones_seran_abonadas_por_quien_lo_presente_para_verificar_su_aplicacion_01f58a
    - Obligacion_las_denuncias_de_extravio_sustraccion_o_destruccion_de_cedin_tendran_vigencia_a__898918
    - Obligacion_las_diferencias_por_redondeo_se_imputaran_a_utilidades_diversas_otras_o_perdidas_e3924e
    - Obligacion_las_entidades_financieras_deberan_proceder_al_retiro_de_los_certificados_requeri_ee7d19
    - Obligacion_las_entidades_financieras_deberan_recibir_solicitudes_en_horario_de_10_a_12_en_e_c65fa9
    - Obligacion_las_informaciones_de_los_puntos_1_2_y_1_3_deberan_contar_con_legalizacion_del_co_96b627
    - Obligacion_las_novedades_que_se_registren_sobre_denuncias_de_incumplido_abiertas_cuyo_valor_55f832
    - Obligacion_las_operaciones_de_los_entes_a_que_refieren_los_incisos_ii_y_iii_del_punto_6_2_d_feb03d
    - Obligacion_las_personas_de_nacionalidad_argentina_y_las_extranjeras_residentes_en_el_pais_s_8c380f
    - Obligacion_las_solicitudes_de_baja_procesadas_exitosamente_que_correspondan_a_reportes_b_2__47784b
    - Obligacion_los_archivos_encriptados_seran_identificados_dentro_de_idear_con_el_titulo_secoe_f0f323
    - Obligacion_los_cargos_deben_informarse_por_cada_producto__ri_transpa_sb_295645
    - Obligacion_los_criterios_de_computo_de_las_franquicias_estaran_determinados_por_la_resoluci_7e8b5a
    - Obligacion_los_datos_11_8_a_11_11_para_unidades_de_servicios_en_el_exterior_deberan_complet_721343
    - Obligacion_los_datos_15_a_19_secuencia_de_imputacion_fecha_de_imputacion_codigo_de_imputaci_1704cc
    - Obligacion_los_datos_1_a_14_repetiran_el_valor_para_cada_uno_de_los_registros_que_compongan_737316
    - Obligacion_los_datos_deberan_informarse_totalizando_las_operaciones_por_consumos_efectuados_ebe523
    - Obligacion_los_datos_del_beneficiario_final_no_deben_ser_consignados_sino_hasta_el_momento__53b157
    - Obligacion_los_datos_fecha_de_accion_informacion_adicional_1_e_informacion_adicional_2_debe_4d5e97
    - Obligacion_los_depositos_judiciales_se_imputaran_bajo_la_denominacion_de_la_causa_a_cuya_or_bbc4d3
    - Obligacion_los_deudores_cuyas_financiaciones_esten_totalmente_cubiertas_con_garantias_prefe_7b174a
    - Obligacion_los_funcionarios_deben_extraer_copias_de_la_documentacion_identificatoria_del_pr_0b51eb
    - Obligacion_los_importes_de_saldos_contables_en_moneda_extranjera_se_convertiran_a_pesos_de__9c2fbd
    - Obligacion_los_importes_de_valores_residuales_deberan_informarse_en_moneda_original_sin_con_080063
    - Obligacion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales__ri_ai_2_2_0beb2c
    - Obligacion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales__ribspc_s2_49526c
    - Obligacion_los_importes_se_registraran_en_miles_sin_decimales__ri_pspapt_s0_b13153
    - Obligacion_los_informes_tecnico_de_autoevaluacion_declaracion_de_tolerancia_al_riesgo_e_inf_885073
    - Obligacion_los_montos_de_las_partidas_consignados_en_el_apartado_b_y_d_deberan_coincidir_co_f2d5bb
    - Obligacion_los_montos_se_registraran_en_miles_sin_decimales__ri_tvf_sbloque1_3d7c78
    - Obligacion_los_montos_se_registraran_en_unidades_sin_decimales__ri_ot_sbloque1_1466a4
    - Obligacion_los_saldos_contables_y_valores_residuales_deberan_informarse_con_el_signo_que_co_ca95a0
    - Obligacion_los_saldos_se_informaran_de_acuerdo_con_los_grados_de_consolidacion_definidos_en_0e1897
    - Obligacion_los_sujetos_obligados_deberan_informar_los_aumentos_y_reducciones_en_tarifas_las_32a20e
    - Obligacion_los_sujetos_obligados_deberan_presentar_la_informacion_sobre_tarifario_nomenclad_8eb1b6
    - Obligacion_los_sujetos_obligados_deberan_presentar_las_modificaciones_incluidas_en_el_apart_b7f915
    - Obligacion_los_sujetos_referidos_deberan_remitir_el_informe_especial_conforme_al_modelo_ins_b32a58
    - Obligacion_los_totales_de_asistencia_crediticia_y_responsabilidades_eventuales_deberan_ser__ad84d1
    - Obligacion_mediante_el_presente_regimen_informativo_se_informaran_las_solicitudes_de_autori_25533e
    - Obligacion_notificacion_del_numero_o_codigo_de_reclamo_asignado_dentro_de_tres_dias_habiles_ee00f2
    - Obligacion_obligacion_de_consignar_informacion_respecto_de_la_cantidad_de_casos_resueltos_e_d9cc1d
    - Obligacion_obligacion_de_remitir_documentacion_adicional_especificada_en_los_items_siguient_f88625
    - Obligacion_obtener_los_datos_necesarios_para_la_determinacion_del_coeficiente_de_cobertura__fcc1f0
    - Obligacion_para_accionistas_cuyas_tenencias_correspondan_ser_informados_en_forma_agrupada_c_3e626c
    - Obligacion_para_aquellos_instrumentos_que_se_encuentran_alcanzados_por_el_punto_6_2_de_las__ba85a7
    - Obligacion_para_cada_reporte_se_informaran_los_datos_que_corresponda_segun_el_detalle_que_s_94305e
    - Obligacion_para_cerrar_el_incumplido_debera_remitirse_una_vez_remitida_la_certificacion_de__0adc1d
    - Obligacion_para_definir_al_deudor_se_deben_tener_en_cuenta_los_conceptos_del_texto_ordenado_a3db75
    - Obligacion_para_depositos_judiciales_utilizar_como_numero_de_identificacion_aquel_con_el_qu_c2d3ca
    - Obligacion_para_el_tipo_de_unidad_de_servicio_codigo_37_el_numero_de_tramite_de_ac_sera_el__e29972
    - Obligacion_para_la_remision_del_informe_se_deben_tener_en_cuenta_las_especificaciones_estab_fa9d88
    - Obligacion_para_la_remision_se_tendran_en_cuenta_las_especificaciones_establecidas_en_la_se_bc6c84
    - Obligacion_para_las_personas_extranjeras_residentes_en_el_exterior_se_consignara_como_tipo__a59ecd
    - Obligacion_para_las_tarjetas_de_credito_se_debera_informar_solo_a_la_persona_juridica_titul_b19f60
    - Obligacion_para_los_cargos_401_y_402_de_la_tabla_no_4_de_gerentes_informar_los_datos_solici_c5c3dc
    - Obligacion_para_los_cruces_de_consistencia_indicados_se_tendran_en_cuenta_de_corresponder_l_474354
    - Obligacion_para_municipios_se_debera_consignar_unicamente_la_provincia_a_la_que_corresponde_d8cd09
    - Obligacion_para_municipios_se_debera_consignar_unicamente_la_provincia_a_la_que_corresponde_fb9361
    - Obligacion_para_opciones_de_cartera_propia_informar_solo_partidas_fuera_de_balance_consigna_f78153
    - Obligacion_para_otros_proveedores_no_financieros_de_credito_que_soliciten_acceso_al_servici_c09290
    - Obligacion_para_personas_fisicas_accionistas_se_informaran_apellidos_y_nombres_teniendo_en__49b023
    - Obligacion_para_personas_fisicas_y_sociedades_de_hecho_consignar_apellidos_y_nombres_en_for_d14f03
    - Obligacion_para_personas_juridicas_accionistas_se_consignara_su_razon_social_o_denominacion_ebd197
    - Obligacion_para_restantes_personas_juridicas_consignar_razon_social_o_denominacion_en_forma_a783db
    - Obligacion_para_unidades_de_servicio_codigo_37_agencias_complementarias_de_servicios_financ_1d6d21
    - Obligacion_planificacion_y_ejecucion_de_la_tarea_profesional_de_forma_que_permita_emitir_el_0e014d
    - Obligacion_por_cada_concepto_de_la_tabla_de_conceptos_de_reclamos_se_debera_informar_el_sto_00bf21
    - Obligacion_por_cada_concepto_de_la_tabla_de_conceptos_de_reclamos_se_debera_informar_la_can_528c59
    - Obligacion_presentacion_anual_de_informe__ri_iesinap_s3_f28efe
    - Obligacion_presentacion_anual_del_requerimiento__ri_iepsp_s3_75588d
    - Obligacion_presentacion_del_informe_del_ano_de_autorizacion_como_administrador_de_esquemas__a05e85
    - Obligacion_presentacion_del_primer_informe_correspondiente_al_31_12_del_ano_siguiente_a_la__b4ac58
    - Obligacion_presentacion_mensual_del_requerimiento_a_partir_del_inicio_de_operaciones_con_ve_d1924a
    - Obligacion_presentar_certificado_de_dominio_del_terreno_emitido_por_registro_de_propiedad_i_3a9ef6
    - Obligacion_presentar_copia_autenticada_por_escribano_del_contrato_social_o_de_fideicomiso_p_6b0410
    - Obligacion_presentar_copia_autenticada_por_escribano_del_instrumento_que_constituyo_los_der_a136a0
    - Obligacion_presentar_copia_del_plano_de_obra_aprobado_por_autoridad_competente_que_evidenci_1b5efe
    - Obligacion_presentar_permiso_o_autorizacion_de_obra_otorgado_por_la_autoridad_jurisdicciona_18f6e7
    - Obligacion_presentar_proyecto_de_nota_del_representante_legal_manifestando_con_caracter_de__f6e138
    - Obligacion_redondeo_de_magnitudes_incrementar_los_valores_en_una_unidad_cuando_el_primer_di_d197b5
    - Obligacion_remision_de_documentacion_correspondiente_a_la_operacion_adjunta_al_cedin_en_cas_31fa11
    - Obligacion_reporte_desagregado_de_prestamos_partidas_70xx000_dentro_de_partidas_10xxxxx_cre_0cb99a
    - Obligacion_respecto_de_los_cajeros_automaticos_terminales_de_autoservicio_otros_dispositivo_1259e4
    - Obligacion_resultan_de_aplicacion_los_articulos_1o_3o_y_38_de_la_ley_de_entidades_financier_da2311
    - Obligacion_se_agregara_una_descripcion_detallada_del_calculo_del_importe_para_el_periodo_in_a96cd7
    - Obligacion_se_aplicara_la_metodologia_para_la_conversion_a_moneda_nacional_detallada_en_el__831668
    - Obligacion_se_aplicara_para_este_campo_el_procedimiento_indicado_en_el_segundo_y_tercer_par_0380c4
    - Obligacion_se_aplicara_para_los_puntos_3_3_y_3_4_el_procedimiento_indicado_en_el_segundo_y__2dce32
    - Obligacion_se_aplicara_para_los_puntos_5_3_y_5_4_el_procedimiento_indicado_en_el_segundo_y__9aaf97
    - Obligacion_se_consignara_como_numero_y_fecha_de_resolucion_la_de_la_presente_comunicacion___794f2b
    - Obligacion_se_consignara_la_fecha_del_ultimo_ajuste_de_la_tasa_de_interes__ri_dsf_s10_7a0a80
    - Obligacion_se_consignara_la_razon_social_o_denominacion_de_la_entidad_o_empresa__ri_ii_31_1_abbed0
    - Obligacion_se_debe_incluir_la_tarifa_vigente_la_nueva_y_el_porcentaje_de_variacion_detallan_cb7021
    - Obligacion_se_debe_informar_el_importe_de_la_tarifa_para_el_periodo_completo_indicando_la_p_8770ac
    - Obligacion_se_debe_informar_la_cantidad_de_accionistas_que_componen_el_grupo_solo_en_el_cas_d0456c
    - Obligacion_se_debe_informar_la_razon_social_o_denominacion_de_personas_juridicas_en_forma_c_986346
    - Obligacion_se_debe_informar_los_apellidos_y_nombres_de_personas_humanas_y_sociedades_de_hec_369bab
    - Obligacion_se_debe_presentar_ante_la_entidad_financiera_en_el_momento_de_la_operacion_la_do_95f4f9
    - Obligacion_se_deben_identificar_las_comisiones_de_nuevos_productos_cuando_corresponda__ri_t_2f5105
    - Obligacion_se_deben_tener_en_cuenta_las_disposiciones_de_la_seccion_4_sobre_verificacion_vi_eb8293
    - Obligacion_se_debera_consignar_la_calle_numero_piso_departamento_localidad_partido_provinci_806809
    - Obligacion_se_debera_consignar_la_fecha_de_incorporacion_a_la_tenencia_para_las_especies_co_20ac50
    - Obligacion_se_debera_consignar_si_la_especie_integra_o_no_el_margen_de_trading_correspondie_d77a39
    - Obligacion_se_debera_detallar_la_apertura_de_las_cuatro_principales_ubicaciones_geograficas_458372
    - Obligacion_se_debera_identificar_aquellos_deudores_cuya_asistencia_se_haya_informado_en_los_a8b51e
    - Obligacion_se_debera_identificar_aquellos_deudores_cuya_asistencia_se_haya_informado_en_los_d178fb
    - Obligacion_se_debera_identificar_aquellos_deudores_radicados_en_zonas_afectadas_por_el_temp_6083ee
    - Obligacion_se_debera_identificar_aquellos_deudores_sin_asistencia_crediticia_previa_en_la_e_2e64d2
    - Obligacion_se_debera_identificar_si_la_financiacion_es_otorgada_en_condiciones_preferencial_e9a431
    - Obligacion_se_debera_indicar_la_moneda_en_la_que_fue_pactada_la_operacion_de_acuerdo_a_la_c_871be1
    - Obligacion_se_debera_indicar_si_la_operacion_se_encuentra_alcanzada_por_los_terminos_de_dis_1378ef
    - Obligacion_se_debera_indicar_si_se_trata_de_cupon_de_amortizacion_interes_o_interes_y_amort_048f83
    - Obligacion_se_debera_informar_apellidos_y_nombres_en_forma_completa_para_personas_humanas_y_41f9f3
    - Obligacion_se_debera_informar_el_codigo_asignado_por_la_caja_de_valores_s_a_para_los_cupone_e1bdb8
    - Obligacion_se_debera_informar_el_codigo_de_cuenta_del_r_i_balance_de_saldos_para_la_imputac_90096f
    - Obligacion_se_debera_informar_el_codigo_siscen_de_cada_especie__ri_tvf_sbloque3_17a2a4
    - Obligacion_se_debera_informar_el_importe_correspondiente_a_los_intereses_documentados_no_de_679c2e
    - Obligacion_se_debera_informar_el_saldo_de_cada_especie_en_la_respectiva_partida_contable__r_f2bcc0
    - Obligacion_se_debera_informar_el_valor_residual_de_cada_especie_por_la_delta_de_las_opcione_517fda
    - Obligacion_se_debera_informar_el_valor_residual_de_cada_especie_y_cupones_de_amortizacion___848d13
    - Obligacion_se_debera_informar_razon_social_o_denominacion_en_forma_completa_para_restantes__136daf
    - Obligacion_se_debera_informar_si_la_especie_se_encuentra_alcanzada_por_la_exigencia_de_capi_3c85b9
    - Obligacion_se_debera_integrar_el_codigo_de_marca_asignado_en_la_tabla_denominada_tabla_marc_dc00ab
    - Obligacion_se_debera_mantener_actualizada_la_base_de_datos_con_el_inventario_de_las_unidade_d45665
    - Obligacion_se_debera_senalar_los_deudores_clasificados_por_irrecuperables_segun_ultimo_parr_90ba69
    - Obligacion_se_debera_senalar_los_deudores_clasificados_por_recategorizacion_obligatoria__ri_411253
    - Obligacion_se_debera_senalar_los_deudores_clasificados_por_refinanciaciones__ri_dsf_8_1_cabecf
    - Obligacion_se_debera_senalar_los_deudores_clasificados_por_situacion_juridica_incluyendo_co_52d0c2
    - Obligacion_se_debera_tener_en_cuenta_el_grado_casa_matriz_y_sucursales_en_el_pais_a_los_efe_92c2c0
    - Obligacion_se_deberan_comunicar_las_conversiones_de_sucursales_en_el_exterior_en_oficinas_d_d8046a
    - Obligacion_se_deberan_comunicar_los_cierres_de_cualquiera_de_las_unidades_de_servicios__ri__ab757c
    - Obligacion_se_deberan_comunicar_los_reemplazos_de_cajeros_automaticos_terminales_de_autoser_6bbcd3
    - Obligacion_se_deberan_comunicar_los_traslados_temporarios_y_permanentes_en_el_pais_y_en_el__a48479
    - Obligacion_se_deberan_tener_en_cuenta_las_disposiciones_contenidas_en_la_seccion_4_de_verif_e14014
    - Obligacion_se_efectuara_un_control_de_consistencia_por_rubro_sector_y_linea_entre_la_inform_39fecc
    - Obligacion_se_establezcan_metodos_adecuados_de_certificacion_de_autenticidad_de_las_copias__1b1f84
    - Obligacion_se_incluira_el_total_resultante_de_la_suma_de_los_montos_correspondientes_a_los__d9ef39
    - Obligacion_se_incluiran_de_corresponder_las_operaciones_con_los_entes_a_que_refieren_los_in_f6ad5d
    - Obligacion_se_incrementaran_los_valores_en_una_unidad_cuando_el_primer_digito_de_las_fracci_542925
    - Obligacion_se_incrementaran_los_valores_en_una_unidad_cuando_el_primer_digito_de_las_fracci_c99071
    - Obligacion_se_indicara_el_codigo_postal_de_la_sucursal_originante__ri_dsf_s10_9f405b
    - Obligacion_se_indicara_el_costo_financiero_total_vigente_a_la_fecha_a_la_que_se_refiere_la__36b400
    - Obligacion_se_indicara_el_monto_original_aplicado_a_cada_uno_de_los_siguientes_destinos_pro_794bb5
    - Obligacion_se_indicara_el_numero_original_asignado_a_la_operacion_otorgado_por_el_sistema_d_3b89a8
    - Obligacion_se_indicara_la_situacion_de_la_mipyme_al_momento_del_otorgamiento_de_las_financi_bb8b50
    - Obligacion_se_indicara_la_tasa_de_interes_nominal_anual_vigente_a_la_fecha_a_la_que_se_refi_3c08cf
    - Obligacion_se_indicara_la_tasa_nominal_anual_pactada_en_el_formulario_de_prestamo__ri_dsf_s_42543b
    - Obligacion_se_informara_el_codigo_de_identificacion_asignado_por_la_red_que_integra__ri_sef_1cfd1f
    - Obligacion_se_informara_el_codigo_de_la_tabla_no_7_que_corresponda_al_tipo_de_actividad__ri_c4f4cc
    - Obligacion_se_informara_el_e_mail_del_responsable__ri_ii_31_12_19_5_9_713600
    - Obligacion_se_informara_el_nombre_del_cargo_funcional_asignado_en_la_estructura_organizativ_221a61
    - Obligacion_se_informara_el_numero_de_acta_mediante_la_cual_el_directorio_o_consejo_de_admin_2aece2
    - Obligacion_se_informara_el_pais_que_corresponda_ingresando_el_pertinente_codigo_swift_de_pa_413c25
    - Obligacion_se_informara_el_pais_que_corresponda_ingresando_el_pertinente_codigo_swift_de_pa_f81670
    - Obligacion_se_informara_el_tipo_de_documento_de_identidad_de_acuerdo_con_el_detalle_de_la_t_a55191
    - Obligacion_se_informara_el_tipo_de_identificacion_utilizando_los_codigos_de_la_tabla_no_2_t_1e3e5d
    - Obligacion_se_informara_la_actividad_teniendo_en_cuenta_la_clasificacion_establecida_en_la__1be2d7
    - Obligacion_se_informara_la_fecha_a_partir_de_la_cual_el_funcionario_fue_designado_en_la_res_6707c0
    - Obligacion_se_informara_la_fecha_en_la_que_el_gerente_ceso_en_sus_funciones__ri_ii_31_12_19_b35a70
    - Obligacion_se_informara_la_fecha_en_que_el_directivo_asumio_el_cargo__ri_ii_31_12_19_2_10_89db34
    - Obligacion_se_informara_la_fecha_en_que_el_directivo_ceso_en_sus_funciones__ri_ii_31_12_19__d4a1db
    - Obligacion_se_informara_la_fecha_en_que_el_directivo_fue_designado__ri_ii_31_12_19_2_8_0692c9
    - Obligacion_se_informara_la_fecha_en_que_el_funcionario_fue_designado_solo_en_el_caso_del_ge_84d983
    - Obligacion_se_informara_la_fecha_en_que_el_gerente_asumio_el_cargo__ri_ii_31_12_19_3_10_b405f6
    - Obligacion_se_informara_la_fecha_en_que_el_responsable_ceso_en_sus_funciones__ri_ii_31_12_1_2ab524
    - Obligacion_se_informara_la_frecuencia_de_actualizacion_de_la_tasa_en_meses__ri_dsf_s10_0ca43d
    - Obligacion_se_informara_la_red_de_cajeros_automaticos_que_integra_link_banelco_o_propia__ri_6f5f2a
    - Obligacion_se_informara_la_totalidad_de_los_deudores_de_las_entidades_financieras_y_otros_e_1682c2
    - Obligacion_se_informara_la_ubicacion_de_acuerdo_con_el_detalle_del_punto_a_correspondiente__f4530e
    - Obligacion_se_informara_para_cada_una_de_las_operaciones_garantizadas_por_sociedades_de_gar_1a3337
    - Obligacion_se_informara_si_la_unidad_de_servicio_posee_interconexion_con_otras_redes__ri_se_6f5545
    - Obligacion_se_informara_un_e_mail_adicional_de_contacto_en_el_caso_que_el_responsable_no_po_bd3ced
    - Obligacion_se_informaran_el_tipo_y_numero_de_documento_de_identidad_de_los_responsables_con_b57e77
    - Obligacion_se_informaran_el_tipo_y_numero_de_identificacion_fiscal_de_los_responsables_teni_daebba
    - Obligacion_se_informaran_las_financiaciones_y_conceptos_de_los_clientes_cuyo_saldo_de_deuda_a15867
    - Obligacion_se_informaran_los_apellidos_teniendo_en_cuenta_las_indicaciones_contenidas_en_el_fcf916
    - Obligacion_se_informaran_los_apellidos_teniendo_en_cuenta_las_indicaciones_contenidas_en_el_fd602a
    - Obligacion_se_informaran_los_nombres_en_forma_completa_segun_consta_en_el_padron_de_la_agen_47a542
    - Obligacion_se_informaran_los_nombres_teniendo_en_cuenta_las_indicaciones_contenidas_en_el_p_213f6a
    - Obligacion_se_informaran_los_nombres_teniendo_en_cuenta_las_indicaciones_contenidas_en_el_p_9c1111
    - Obligacion_se_ingresara_en_este_concepto_el_nombre_de_la_provincia_municipalidad_o_ente_pub_f1a190
    - Obligacion_se_integraran_el_tipo_y_numero_de_documento_de_identidad_solo_para_las_personas__da7f95
    - Obligacion_se_mantendra_provisoriamente_el_dato_registrado_por_la_entidad_cuando_la_persona_e949cb
    - Obligacion_se_presentara_el_informe_correspondiente_al_ano_en_que_se_produce_la_inscripcion_e948c6
    - Obligacion_se_proveeran_respecto_de_cada_una_de_las_personas_juridicas_informadas_un_detall_9b113a
    - Obligacion_se_tendran_en_cuenta_las_definiciones_de_los_terminos_segun_el_punto_7_1_para_la_42eddc
    - Obligacion_se_utilizaran_como_medidas_idoneas_para_la_clasificacion_de_actividad_el_valor_a_8c19c6
    - Obligacion_sedesa_debe_formular_la_pertinente_denuncia_cuando_advierta_irregularidades_o_un_11ffd1
    - Obligacion_seran_de_aplicacion_las_disposiciones_en_la_materia_establecidas_por_la_autorida_126f7a
    - Obligacion_sin_perjuicio_de_integrarse_los_datos_del_tipo_y_numero_de_documento_tambien_cor_97d309
    - Obligacion_suministrar_el_detalle_de_toda_informacion_complementaria_suministrada_por_la_ad_c16399
    - Obligacion_vencimiento_para_la_presentacion_del_informe_el_dia_20_de_febrero_o_dia_habil_si_675a64
    - Obligacion_verificar_que_se_acompane_la_documentacion_correspondiente_a_la_aplicacion_del_c_91f4c8
Operacion: 239 sin aplica_a
    - Operacion_actualizacion_de_contenido_dfe__consyr_1_4_2_1_34872a
    - Operacion_adelanto_en_efectivo__ri_tar_4_1_4_1766e6
    - Operacion_adicion_de_previsiones_por_riesgo_de_incobrabilidad__seggar_3_2_a0f17d
    - Operacion_adquisicion_de_materiales_construccion_a_proveedores_inscriptos__cedin_7_1_3_2_c2d38b
    - Operacion_adquisicion_de_materiales_construccion_a_proveedores_no_inscriptos__cedin_7_1_3__f22ac0
    - Operacion_almacenamiento_de_dfe_en_medios_de_largo_plazo__consyr_1_4_2_5_04e2b8
    - Operacion_apertura_de_sucursales_en_el_exterior__ri_sef_p3_s1_3b5653
    - Operacion_aplicacion_de_divisas_cancelacion_capital_com_a_7770__ri_secoexpo_sbloque10_496a43
    - Operacion_aplicacion_de_divisas_cancelacion_capital_decreto_492_23__ri_secoexpo_sbloque10_45782f
    - Operacion_aplicacion_de_divisas_cancelacion_capital_posfinanciaciones_exportaciones__ri_se_8dcdb4
    - Operacion_aplicacion_de_divisas_cancelacion_capital_titulos_deuda_canje__ri_secoexpo_sbloq_237cf3
    - Operacion_aplicacion_de_divisas_cancelacion_intereses_com_a_7770__ri_secoexpo_sbloque10_bec272
    - Operacion_aplicacion_de_divisas_cancelacion_intereses_posfinanciaciones_exportaciones__ri__c55074
    - Operacion_aplicacion_de_divisas_cancelacion_intereses_titulos_deuda_canje__ri_secoexpo_sbl_6094b2
    - Operacion_aplicacion_de_divisas_punto_7_10_to_eyc_otros_conceptos__ri_secoexpo_sbloque10_f5fa7e
    - Operacion_aplicacion_de_divisas_repatriacion_aporte_inversion_directa__ri_secoexpo_sbloque_59e5e0
    - Operacion_aplicacion_de_procedimientos_de_verificacion__ri_iesinap_a_s4_7d8890
    - Operacion_aplicacion_del_cedin_a_destino_admitido__cedin_s14_b9cf5e
    - Operacion_aplicaciones_y_otras_imputaciones__ri_secoexpo_sb_32697e
    - Operacion_aporte_adicional_por_factores__seggar_s3_e57599
    - Operacion_asistencia_crediticia_con_garantias_preferidas_a__ri_esd_s1_11ed3c
    - Operacion_asistencia_crediticia_con_garantias_preferidas_b__ri_esd_s1_b267a7
    - Operacion_asistencia_crediticia_sin_garantias_preferidas__ri_esd_s1_054260
    - Operacion_autorizacion_bcra__ri_secoexpo_sbloque10_d4a036
    - Operacion_baja_de_compras_de_moneda_extranjera__ri_ot_13_2_6ff9b0
    - Operacion_baja_de_reportes_de_exportacion__ri_secoexpo_sbloque8_cc0baf
    - Operacion_bienes_exportados_temporalmente_reimportacion_no_razonable__ri_secoexpo_sbloque1_5ff7da
    - Operacion_bienes_rechazados_reimportacion__ri_secoexpo_sbloque10_8253fe
    - Operacion_calculo_de_monto_total_ponderado_fed__ri_tsa_3_3_2_ca0da6
    - Operacion_calculo_de_monto_total_ponderado_fer__ri_tsa_3_3_2_0d4065
    - Operacion_calculo_del_coeficiente_lcr__ri_msrl_sbloque1_4d984a
    - Operacion_calculo_del_indice_ic_con_camels__seggar_7_1_dafa7a
    - Operacion_calculo_diario_del_nsfr__ri_tsa_2_1_51e550
    - Operacion_calculo_plazo_promedio_resolucion_en_dias__ri_cr_3_1_b0cf5e
    - Operacion_calculo_rcl_pesos_y_moneda_extranjera__ri_rcl_1_2_f2ea03
    - Operacion_calculo_tasa_maxima_interes_punitorio_tarjetas__ri_tar_4_1_3_b8b7ca
    - Operacion_cambio_de_cedin_por_otros_equivalentes__cedin_9_1_1e9300
    - Operacion_cancelacion_del_cedin__cedin_12_3_4673dc
    - Operacion_cantidad_clientes_con_inversiones_fondos_comunes__ri_psp_sii_e68e58
    - Operacion_cantidad_cuentas_de_pago_con_saldo__ri_psp_sii_c93c9d
    - Operacion_cantidad_cuentas_pago_saldo_pendiente_liquidacion__ri_psp_sii_eb410c
    - Operacion_cantidad_de_tarjetas_adicionales_emitidas__ri_tar_2_2_e14d6b
    - Operacion_cantidad_de_tarjetas_titulares_emitidas__ri_tar_2_2_448056
    - Operacion_cantidad_total_cuentas_de_pago_clientes__ri_psp_sii_87619b
    - Operacion_certificacion_de_cumplido__ri_secoexpo_sb_0124f6
    - Operacion_certificacion_de_cumplido_de_exportacion__ri_secoexpo_sb_e681b6
    - Operacion_certificacion_de_extension_de_plazo__ri_secoexpo_sb_f7ef1d
    - Operacion_certificacion_de_incumplido_en_gestion_de_cobro__ri_secoexpo_sb_97a2eb
    - Operacion_certificacion_de_incumplido_en_gestion_de_cobro__ri_secoexpo_sbloque3_36fcf2
    - Operacion_certificacion_de_obra_por_profesional__cedin_7_1_2_a71621
    - Operacion_certificacion_de_obra_suscripta_por_profesional__cedin_7_1_3_1_2c69ce
    - Operacion_certificacion_de_reproducciones__consyr_3_4_2_69a079
    - Operacion_certificacion_y_registro_traslacion__cedin_6_4_a0e242
    - Operacion_certificado_de_acreditacion_mipyme__micemp_1_1_68a315
    - Operacion_cesion_del_seguimiento__ri_secoexpo_sb_f53ba1
    - Operacion_cierre_del_proceso_de_reproduccion__consyr_3_3_1_2_c22156
    - Operacion_clasificacion_tpv_por_uso__ri_pspapt_sb_72f025
    - Operacion_cobertura_de_devolucion_de_capital_e_intereses__seggar_5_3_1_9301af
    - Operacion_cobros_locales_exportaciones_ranchos__ri_secoexpo_sbloque10_1e979a
    - Operacion_compra_a_termino_moneda_extranjera_liquidable_en_exterior__ri_ot_13_4_32d51b
    - Operacion_compra_a_termino_moneda_extranjera_liquidable_en_pesos__ri_ot_13_4_5fdf5f
    - Operacion_compra_de_terrenos_lotes_parcelas_galpones_locales_oficinas_cocheras_y_viviendas_21c8ef
    - Operacion_compraventa_valores_negociables_decreto_492_23__ri_secoexpo_sbloque10_08fbce
    - Operacion_comprobacion_de_documentacion_cedin__cedin_7_2_91a798
    - Operacion_conceptos_fob_aduana_no_forman_parte_condicion_venta__ri_secoexpo_sbloque10_e5c442
    - Operacion_conformacion_del_lote_de_documentos__consyr_3_3_2_d67387
    - Operacion_conservacion_de_reproducciones_de_comprobantes__consyr_3_1_66661a
    - Operacion_conservacion_de_soportes_de_informacion__consyr_3_5_398e6d
    - Operacion_consignacion_judicial_del_importe_cedin__cedin_13_1_8efd70
    - Operacion_constitucion_de_cuentas_e_imposiciones_conjuntas__seggar_5_3_2_924619
    - Operacion_consumos_a_facturar_en_futuras_liquidaciones__ri_tar_3_1_2_fd11fe
    - Operacion_consumos_con_tarjetas_en_el_pais__ri_pspapt_sa_c41992
    - Operacion_correccion_del_aporte_normal_segun_indice__seggar_s7_a607da
    - Operacion_creacion_del_sistema_de_seguro_de_garantia_de_depositos__seggar_8_1_555e0e
    - Operacion_cuantificacion_de_tpv__ri_pspapt_sb_23ee92
    - Operacion_debito_de_aportes_en_cuentas_corrientes__seggar_s4_b33bdc
    - Operacion_declaracion_de_tolerancia_al_riesgo__ri_laft_2_2_1_5b6c60
    - Operacion_declaracion_jurada_certificada_por_contador_publico__micemp_1_3_293c62
    - Operacion_denuncia_de_incumplido__ri_secoexpo_sb_2386a4
    - Operacion_deposito_en_caja_de_ahorros__seggar_5_1_3_ea30b3
    - Operacion_depositos_en_forma_de_saldos_inmovilizados__seggar_5_1_7_c71f1a
    - Operacion_depositos_en_pesos_y_moneda_extranjera__seggar_5_1_5d1ac2
    - Operacion_depositos_en_pesos_y_moneda_extranjera__seggar_s6_a6e361
    - Operacion_descuentos_y_gastos_servicios_pagaderos_exterior__ri_secoexpo_sbloque10_a3f64f
    - Operacion_determinacion_de_relaciones_efecto_de_franquicias__ri_ai_4_2_7cffa7
    - Operacion_determinacion_del_coeficiente_lcr__ri_msrl_s2_f2b3e9
    - Operacion_devolucion_de_cheques_pagados_a_libradores__consyr_3_2_4_1_6522f1
    - Operacion_devolucion_de_documentacion_defectuosa__cedin_7_4_ddc61a
    - Operacion_distribucion_de_dfe__consyr_1_4_2_4_d18ab1
    - Operacion_emision_de_cedin_en_dolares_estadounidenses__cedin_2_1_3_36d4f5
    - Operacion_emision_de_informe_especial__ri_iesinap_a_s4_ae6a68
    - Operacion_emision_de_informe_especial_sobre_cumplimiento_normativo__ri_iepsp_a_s1_e39c47
    - Operacion_emision_de_informe_especial_sobre_cumplimiento_normativo__ri_iesinap_a_s1_4efa4c
    - Operacion_emision_de_tarjeta_en_el_pais__ri_pspapt_s5_df2b9c
    - Operacion_entrega_de_cedin_a_clientes__cedin_s12_661b06
    - Operacion_establecimiento_de_multas__ri_iesinap_a_s4_d4ca14
    - Operacion_estado_de_situacion_de_deudores_consolidado_con_filiales_y_subsidiarias__ri_nge__554518
    - Operacion_exportacion_beneficios_cambiarios_decreto_929_13__ri_secoexpo_sbloque10_caa18d
    - Operacion_exportacion_beneficios_cambiarios_rigi__ri_secoexpo_sbloque10_b78cab
    - Operacion_exportaciones_bienes_importados_temporalmente_sin_giro_divisas__ri_secoexpo_sblo_4ce7e1
    - Operacion_exportaciones_cobertura_embarques_con_faltantes__ri_secoexpo_sbloque10_81be6c
    - Operacion_exportaciones_cobertura_embarques_siniestrados__ri_secoexpo_sbloque10_a7d45d
    - Operacion_exportaciones_no_susceptibles_contravalor_divisas__ri_secoexpo_sbloque10_45763f
    - Operacion_faltantes_mermas_y_deficiencias_permisos_embarque__ri_secoexpo_sbloque10_4e817c
    - Operacion_financiacion_sujeta_a_interes__ri_tar_3_1_3_e44c33
    - Operacion_formalizacion_de_acta_de_apertura__consyr_3_3_1_1_e22da4
    - Operacion_formulas_no_completadas_objeto_de_extravio_sustraccion_o_destruccion__cedin_s12_ed8243
    - Operacion_gastos_bancarios_ejecucion_cobro__ri_secoexpo_sbloque10_8cfca5
    - Operacion_gastos_no_incorporados_colocacion_producto_exterior__ri_secoexpo_sbloque10_287104
    - Operacion_generacion_de_nuevos_dfe__consyr_1_4_2_1_61c17c
    - Operacion_identificacion_de_cedin_extraviado_sustraido_o_destruido__cedin_12_2_2_2d8ef2
    - Operacion_identificacion_del_estado_titular_de_capital__ri_ii_31_12_19_4_1_1_405313
    - Operacion_identificacion_del_presentante_mediante_documento__cedin_12_2_1_7cf711
    - Operacion_imputacion_permiso_provisorio_ajuste_fob__ri_secoexpo_sbloque10_0d0bed
    - Operacion_imputaciones_complemento_precios_revisables__ri_secoexpo_sbloque10_861682
    - Operacion_inclusion_saldo_financiaciones_clientes_vinculados__ri_ai_3_3_10a066
    - Operacion_incorporacion_de_imagenes_digitalizadas_al_home_banking__consyr_1_3_885433
    - Operacion_incorporacion_de_leyenda_aplicado_en_dorso__cedin_7_3_3f2744
    - Operacion_incremento_proporcional_de_participacion__seggar_s1_eaf46d
    - Operacion_indicacion_de_dias_de_atraso_en_obligaciones__ri_dsf_8_2_176c57
    - Operacion_indicacion_situacion_mipyme_al_otorgamiento_de_financiaciones__ri_dsf_s10_62c8d0
    - Operacion_informacion_de_concentracion_de_fondeo_por_producto_significativo__ri_tsa_s3_ee0295
    - Operacion_informacion_de_cupon_de_renta__ri_tvf_sbloque5_b04dc3
    - Operacion_informacion_de_descripcion_de_titulos_valores__ri_tvf_sbloque5_e061b3
    - Operacion_informacion_de_destinaciones_de_exportacion_de_bienes__ri_secoexpo_sa_c76499
    - Operacion_informacion_de_franquicias_disminuciones_de_exceso_de_inmovilizacion__ri_ai_3_4_86d706
    - Operacion_informacion_de_franquicias_disminuciones_en_conceptos_computables__ri_ai_3_4_c2f440
    - Operacion_informacion_de_franquicias_integracion_patrimonial__ri_ai_3_4_401b61
    - Operacion_informacion_de_tarifas_de_comisiones__ri_transpa_sa_de1328
    - Operacion_informacion_de_vinculacion_del_cliente__ri_dsf_s5_c99e12
    - Operacion_informacion_del_ratio_de_fondeo_neto_estable__ri_tsa_3_2_194ca4
    - Operacion_informe_anual_revisor_externo_independiente__ri_laft_2_2_1_5ebe5b
    - Operacion_informe_consumos_facturados_liquidaciones__ri_tar_3_1_1_1b3d66
    - Operacion_informe_de_monto_total_por_moneda_de_origen__ri_pspapt_s12_f0376b
    - Operacion_informe_de_operaciones_de_adquirencia_por_metodo_de_iniciacion__ri_pspapt_s6_9b9b2b
    - Operacion_informe_especial_de_cumplimiento__ri_iesinap_a1_s0_41b18e
    - Operacion_informe_modalidad_de_pago_adquirencia__ri_pspapt_s7_3cb416
    - Operacion_informe_tecnico_autoevaluacion_riesgos_la_ft__ri_laft_2_2_1_7da49a
    - Operacion_ingreso_de_codigo_de_cargo_en_tabla__ri_ii_31_12_19_2_6_2_db357a
    - Operacion_ingreso_de_codigo_de_tipo_de_relacion__ri_ii_31_12_19_6_1_a0f3c6
    - Operacion_ingresos_liquidados_empresas_procesadoras_pagos__ri_secoexpo_sbloque10_c2d1d3
    - Operacion_instrumentacion_de_documentos_en_soportes_electronicos__consyr_1_4_f3e258
    - Operacion_integracion_de_informacion_de_categoria__ri_sef_p1_s13_21d544
    - Operacion_inversiones_a_plazo__seggar_5_1_6_05ec5a
    - Operacion_libre_disponibilidad_divisas_decreto_443_23__ri_secoexpo_sbloque10_363962
    - Operacion_mercaderia_siniestrada_anterior_entrega__ri_secoexpo_sbloque10_b0d4dd
    - Operacion_multas_demoras_entrega_bienes__ri_secoexpo_sbloque10_f89ec4
    - Operacion_notificacion_de_cesion_del_seguimiento__ri_secoexpo_sb_266731
    - Operacion_obtencion_listado_de_multas_cobradas__ri_iesinap_a_s4_cdfa35
    - Operacion_opcion_de_compra_de_moneda_extranjera__ri_ot_2_2_e415f4
    - Operacion_operaciones_aduaneras_exceptuadas_seguimiento__ri_secoexpo_sbloque10_b8ac3f
    - Operacion_operaciones_con_lectura_de_codigos_qr__ri_pspapt_s8_82882a
    - Operacion_operaciones_con_personas_vinculadas_a_ardides__verac_s4_1b96ec
    - Operacion_operaciones_en_a3_mercados_con_identificacion_de_contraparte__ri_ot_3_11_c578f3
    - Operacion_operatorias_con_cedin__cedin_13_8_a8a662
    - Operacion_otorgamiento_de_prestamos_en_condiciones_preferenciales__ri_dsf_s9_f3e4c3
    - Operacion_otorgamiento_de_prestamos_personales_sin_garantia_real__ri_tar_4_1_1_421031
    - Operacion_otros_mecanismos_seguimiento_no_detallados__ri_secoexpo_sbloque10_ff77ae
    - Operacion_pago_de_cedin__cedin_13_2_3_ab7285
    - Operacion_pago_de_cedin__cedin_s12_8ceeb1
    - Operacion_pago_del_cedin__cedin_12_3_b37ba6
    - Operacion_pago_del_cedin__cedin_13_1_5f8934
    - Operacion_participacion_en_fideicomiso_accionista_de_sedesa__seggar_s1_df8849
    - Operacion_permanencia_en_estado_en_proceso_de_agencias_complementarias__ri_sef_p2_s0_66bf95
    - Operacion_preparacion_del_balance_de_saldos__ribspc_s1_34ce9d
    - Operacion_presentacion_de_codigo_de_tipo_de_responsable__ri_ii_31_12_19_5_6_e13d12
    - Operacion_presentacion_de_copia_de_factura_de_materiales__cedin_5_1_7b6d66
    - Operacion_presentacion_de_estados_financieros_o_contables__micemp_1_2_89b305
    - Operacion_presentacion_de_informacion_sobre_tarifario__ri_transpa_sbloque3_e68bab
    - Operacion_presentacion_de_proyecto_de_certificacion_de_obra__cedin_5_1_df2106
    - Operacion_presentacion_de_proyecto_de_escritura_traslativa__cedin_5_1_bfcd64
    - Operacion_presentacion_de_proyecto_de_instrumento_de_derechos__cedin_5_1_6385e4
    - Operacion_presentacion_de_solicitud_de_autorizacion_agencias_complementarias__ri_sef_p2_s0_083cb9
    - Operacion_presentacion_declaracion_tolerancia_al_riesgo__ri_laft_2_3_1_40e388
    - Operacion_presentacion_del_cedin_ante_entidad_financiera__cedin_s5_9c8698
    - Operacion_presentacion_formulario_anexo_iii__ri_sef_p1_s8_d7579c
    - Operacion_presentacion_informe_revisor_externo__ri_laft_2_3_2_b9f790
    - Operacion_presentacion_informe_tecnico_autoevaluacion_la_ft__ri_laft_2_3_1_f73c13
    - Operacion_presentacion_rte_ante_bcra__ri_laft_1_1_f56379
    - Operacion_realizacion_de_almacenamiento_simultaneo_con_creacion__consyr_1_4_2_2_c6fc5e
    - Operacion_realizacion_de_operacion_en_agencias_complementarias__ri_acsf_sbloque3_94ac5e
    - Operacion_recepcion_de_cedin__cedin_11_1_0e6055
    - Operacion_rechazo_de_pedido_de_cobertura__seggar_5_3_4_b83a7a
    - Operacion_recibir_certificado_con_documentacion__cedin_6_1_5e1cae
    - Operacion_reembarco_bienes_zona_franca_zfre__ri_secoexpo_sbloque10_bbf7ae
    - Operacion_reemplazo_del_cedin__cedin_12_3_d0cec3
    - Operacion_reexportacion_mercaderia_regimen_factoria__ri_secoexpo_sbloque10_ec4daf
    - Operacion_registro_de_fecha_de_inicio_o_baja_de_actividades__ri_sef_p1_s9_2b8931
    - Operacion_registro_de_reproducciones_de_cheques__consyr_3_4_3_ff29a0
    - Operacion_registro_de_transaccion_de_canje_en_sistema__cedin_9_2_976a4a
    - Operacion_remision_de_archivos_de_documentacion__consyr_1_3_ded575
    - Operacion_remision_de_informacion_al_bcra__consyr_3_2_3_a69ef1
    - Operacion_remision_de_informe_especial_sobre_cumplimiento_de_normas_snp_transferencias__ri_c26e34
    - Operacion_reporte_de_aplicaciones_e_imputaciones_de_divisas__ri_secoexpo_sbloque5_b91b97
    - Operacion_reporte_de_condicion_de_pep__ri_laft_3_3_f5cf90
    - Operacion_reporte_de_transacciones_en_efectivo_de_alto_monto__ri_laft_2_1_1_41c526
    - Operacion_reportes_de_operaciones_sospechosas__ri_laft_2_1_3_3d2e89
    - Operacion_reproduccion_de_cheques_pagados__consyr_3_2_4_7a5227
    - Operacion_reproduccion_de_documentacion_interna__consyr_3_2_1_09cc53
    - Operacion_responsabilidades_eventuales_con_contragarantias_preferidas_a__ri_esd_s2_846984
    - Operacion_responsabilidades_eventuales_con_contragarantias_preferidas_b__ri_esd_s2_c2f2ba
    - Operacion_responsabilidades_eventuales_sin_contragarantias_preferidas__ri_esd_s2_0b1eae
    - Operacion_retenciones_impositivas_pais_destino__ri_secoexpo_sbloque10_9d0d47
    - Operacion_revision_externa_independiente_sistema_prevencion_la_ft__ri_laft_1_4_a19dd3
    - Operacion_saldo_clientes_invertidos_fondos_comunes_dinero__ri_psp_sii_29cc70
    - Operacion_saldo_fondos_acreditados_cuentas_de_pago__ri_psp_sii_164781
    - Operacion_saldo_pendiente_acreditacion_cuentas_pago__ri_psp_sii_68425d
    - Operacion_seleccion_de_codigo_de_cargo_sucursal_local__ri_ii_31_12_19_2_6_3_cac18e
    - Operacion_solicitud_de_certificados_mediante_nota__cedin_3_2_a8cd3d
    - Operacion_solicitud_documento_fisico_cheque_por_librador__consyr_s2_582d31
    - Operacion_suministro_de_constancia_de_verificacion_cedin__cedin_s6_a117bd
    - Operacion_suministro_de_informacion_complementaria_de_exportacion__ri_secoexpo_s17_c0998d
    - Operacion_suscripcion_de_cedin__cedin_1_1_4df80a
    - Operacion_suscripcion_y_emision_por_cuenta_y_orden_del_bcra__cedin_13_2_1_610ae1
    - Operacion_sustitucion_del_cedin__cedin_13_1_59d74b
    - Operacion_tasa_maxima_interes_compensatorio_adelanto_en_efectivo__ri_tar_4_2_3f5f27
    - Operacion_tasa_maxima_interes_compensatorio_financiacion_saldos_tarjetas_credito__ri_tar_4_05513b
    - Operacion_tasa_maxima_interes_punitorio_tarjetas_credito__ri_tar_4_2_55f7cc
    - Operacion_tasas_de_prestamos_personales_sin_garantia_real__ri_tar_4_2_30a095
    - Operacion_tenencia_de_activos_financieros__verac_2_1_b64dba
    - Operacion_transmision_de_cedin_por_endoso__cedin_s4_487841
    - Operacion_uso_de_papel_de_seguridad__cedin_2_2_1_f00b9c
    - Operacion_venta_a_termino_moneda_extranjera_liquidable_en_exterior__ri_ot_13_4_1d5da6
    - Operacion_venta_a_termino_moneda_extranjera_liquidable_en_pesos__ri_ot_13_4_49777b
    - Operacion_verificacion_aplicacion_cedin_fideicomisos_sociedades_constructoras__cedin_7_1_2_73fda0
    - Operacion_verificacion_coincidencia_datos_bcra_certificado__cedin_6_4_85deba
    - Operacion_verificacion_comunicacion_simultanea_a_participantes__ri_iesinap_a_s4_705e56
    - Operacion_verificacion_control_precios_aceptadores__ri_iesinap_a_s4_f7db60
    - Operacion_verificacion_cumplimiento_requerimientos_bcra__ri_iesinap_a_s4_d76b7f
    - Operacion_verificacion_de_caracteristicas_formales_y_de_seguridad__cedin_6_2_01622b
    - Operacion_verificacion_de_condicion_mipyme__micemp_s2_bb5130
    - Operacion_verificacion_de_impedimentos_para_pago__cedin_s8_292d85
    - Operacion_verificacion_del_certificado_y_aplicacion_y_cobro_simultaneo__cedin_s5_d3f0b9
    - Operacion_verificacion_elaboracion_reporte_directorio__ri_iesinap_a_s4_0751c9
    - Operacion_verificacion_existencia_base_de_reclamos_y_quejas__ri_iesinap_a_s4_4a2357
    - Operacion_verificacion_pagos_qr_desde_billeteras_digitales__ri_iesinap_a_s4_27c470
    - Operacion_verificacion_politicas_y_procedimientos_snp__ri_iesinap_a_s4_c49b79
    - Operacion_verificacion_reglas_esquema_transferencias_inmediatas__ri_iesinap_a_s4_16202f
    - Operacion_verificacion_regularidad_cadena_endosos__cedin_6_4_9b2b69
Potestad: 28 sin aplica_a
    - Potestad_admision_de_firmas_olografas_en_documentos_electronicos__se_admiten_las_firmas_o_fb71af
    - Potestad_admision_de_soportes_electronicos__se_autoriza_el_uso_de_soportes_electronicos_o_daf2f5
    - Potestad_aplicacion_cedin_a_proporcion_costo_construccion_y_terreno__facultad_de_aplicar__581d5d
    - Potestad_aplicacion_cedin_emprendimientos_comerciales_con_viviendas__facultad_de_consider_3ad8fa
    - Potestad_aplicacion_cedin_unica_operacion_o_parcial__la_aplicacion_de_cedin_puede_realiza_82eb72
    - Potestad_aplicar_cedin_a_espacios_comunes_de_complejos_habitacionales__se_habilita_la_apl_480c08
    - Potestad_autorizacion_del_bcra_para_pago_del_certificado__el_bcra_autoriza_a_la_entidad_f_5234f0
    - Potestad_bcra_reemplaza_denominacion_por_padron_afip__el_bcra_podra_reemplazar_la_denomin_de1971
    - Potestad_canje_de_cedin_por_otros_de_menor_denominacion__los_cedin_pueden_ser_canjeados_p_b5503d
    - Potestad_cobro_o_transmision_posterior_del_cedin_aplicado__el_cedin_aplicado_puede_ser_co_018d15
    - Potestad_complementacion_con_documentacion_adicional__la_entidad_tiene_la_facultad_de_com_3b3bd1
    - Potestad_complementacion_con_informacion_adicional__la_entidad_podra_complementar_las_inf_4951df
    - Potestad_computo_requisitos_sepyme_a_partir_de__facultad_de_efectuar_el_computo_de_los_re_41e4ba
    - Potestad_considerar_cedin_como_aplicados_en_cesion_de_boleto__en_el_caso_de_cesion_de_bol_10b5c2
    - Potestad_consignacion_de_aclaraciones_sobre_bonificaciones__facultad_de_consignar_aclarac_2f9cd2
    - Potestad_exclusion_automatica_de_reporte_b_2__en_caso_de_que_se_procese_exitosamente_una__7694c8
    - Potestad_exclusion_automatica_de_reporte_b_3__en_caso_de_que_se_procese_exitosamente_una__3e335b
    - Potestad_gestion_de_cobro_por_fiduciario_o_sociedad_constructora__en_fideicomisos_inmobil_59dbe0
    - Potestad_opcion_de_transferencia_a_otra_entidad_financiera__el_beneficiario_puede_optar_p_850d92
    - Potestad_presentacion_del_cedin_ante_entidad_financiera__el_cedin_podra_presentarse_ante__3fb30d
    - Potestad_reemplazo_de_datos_por_bcra_desde_padron_de_deudores__el_banco_central_tiene_la__b309ae
    - Potestad_requerimiento_de_anticipo_de_aportes_minimos_normales__el_banco_central_de_la_re_93179a
    - Potestad_sedesa_requerir_justificacion_de_fondos__sedesa_tiene_la_facultad_de_requerir_a__47a3e7
    - Potestad_solicitar_copias_de_documentacion_en_sucursal__el_cliente_tiene_la_facultad_de_s_83820a
    - Potestad_solicitud_de_multiples_cedin__el_suscriptor_podra_solicitar_uno_o_mas_cedin_por__c5261f
    - Potestad_transmision_del_cedin_por_endoso__el_cedin_podra_seguir_siendo_transmitido_media_048c41
    - Potestad_transmision_del_cedin_por_endoso__el_cedin_puede_transmitirse_entre_endosante_y__4363dc
    - Potestad_uso_codigo_99999_tarjetas_exterior_esquema_no_incluido__en_caso_de_tarjetas_emit_4074e3
Restriccion: 59 sin aplica_a
    - Restriccion_cada_cedin_sera_emitido_por_un_maximo_de_us_100_000__cedin_2_1_5_859f81
    - Restriccion_cada_cedin_sera_emitido_por_un_minimo_de_us_100__cedin_2_1_5_d11aba
    - Restriccion_cualquier_condicion_en_el_endoso_no_prevista_en_estas_normas_se_tendra_por_no_es_07c41c
    - Restriccion_cuando_la_cantidad_de_eventos_en_los_conceptos_otros_de_la_tabla_de_conceptos_de_c02f1b
    - Restriccion_el_aporte_adicional_no_podra_superar_una_vez_el_aporte_normal__seggar_s3_00fe82
    - Restriccion_el_aporte_adicional_resultante_de_la_ponderacion_de_factores_no_podra_superar_un_b4b20e
    - Restriccion_el_codigo_de_motivo_2_solo_se_admitira_en_el_caso_de_incumplidos_cerrados_es_dec_40feff
    - Restriccion_el_documento_no_debe_ser_eliminable_una_vez_creado__consyr_1_4_2_2_8dead5
    - Restriccion_el_documento_no_puede_ser_modificado_una_vez_creado__consyr_1_4_2_2_460707
    - Restriccion_el_documento_no_puede_ser_reemplazado_una_vez_creado__consyr_1_4_2_2_32de3c
    - Restriccion_el_importe_debe_corresponder_al_precio_de_una_operacion_individual_e_incluir_el__25b0a1
    - Restriccion_el_indice_iar_a_se_acota_entre_un_minimo_de_1_y_un_maximo_de_2_si_el_resultado_d_03f6d4
    - Restriccion_el_indice_ic_resultado_final_de_la_formula_se_acota_entre_un_minimo_de_1_y_un_ma_7d127a
    - Restriccion_el_indice_ipr_f_se_acota_entre_un_minimo_de_1_y_un_maximo_de_2_5_si_el_resultado_e5285b
    - Restriccion_el_informe_especial_no_debe_ser_utilizado_referenciado_o_distribuido_con_proposi_bb78c3
    - Restriccion_el_monto_total_cubierto_por_la_garantia_no_podra_exceder_50_000_000_por_los_conc_fe3883
    - Restriccion_el_numero_de_casa_no_podra_ser_utilizado_para_otra_unidad_aunque_aquella_haya_si_291f9e
    - Restriccion_el_sistema_de_seguro_de_garantia_de_los_depositos_no_debe_comprometer_los_recurs_90aaa2
    - Restriccion_el_tamano_de_letra_del_tarifario_completo_debe_cumplir_con_las_exigencias_del_pu_082679
    - Restriccion_el_total_de_los_datos_a_proporcionar_individual_y_colectivamente_debe_sumar_el_1_519330
    - Restriccion_el_total_garantizado_a_una_persona_determinada_por_acumulacion_de_cuentas_y_depo_e587c8
    - Restriccion_el_valor_contable_de_las_restantes_especies_informadas_no_incluidas_en_las_parti_5f49b6
    - Restriccion_en_cuentas_e_imposiciones_constituidas_a_nombre_de_dos_o_mas_personas_el_limite__e8ba38
    - Restriccion_en_operaciones_a_nombre_de_dos_o_mas_personas_la_garantia_se_prorratea_entre_tit_5afb6f
    - Restriccion_exclusion_de_transferencias_realizadas_mediante_esquema_propio_del_pspcp_no_curs_5c8983
    - Restriccion_la_disposicion_de_los_productos_debe_respetar_el_ordenamiento_establecido_en_el__8e31e7
    - Restriccion_la_presentacion_de_documentacion_provisoria_no_podra_realizarse_con_antelacion_m_5ae1c1
    - Restriccion_la_tasa_de_retribucion_de_los_importes_recibidos_no_puede_exceder_la_tasa_establ_b47a27
    - Restriccion_las_adendas_que_involucren_nuevas_incorporaciones_de_agencias_complementarias_qu_c21f10
    - Restriccion_las_denuncias_registradas_en_el_bcra_impediran_el_pago_del_certificado__cedin_s1_7e14ac
    - Restriccion_las_especies_deberan_ser_informadas_solo_en_el_primer_nivel_de_consolidacion_en__ec5550
    - Restriccion_las_tarifas_deben_expresarse_en_la_moneda_en_que_se_cobra__ri_transpa_sb_f22732
    - Restriccion_las_tasas_deben_expresarse_en_porcentaje_con_dos_decimales__ri_transpa_sb_49798c
    - Restriccion_limite_cualitativo_la_informacion_debe_abarcar_solo_las_terminales_fisicas_en_co_0c0a23
    - Restriccion_los_activos_utilizados_como_facilidades_permanentes_en_operaciones_con_bancos_ce_5d1480
    - Restriccion_los_cedin_no_devengaran_interes_alguno__cedin_13_6_049da3
    - Restriccion_los_cedin_no_tendran_fecha_de_vencimiento__cedin_13_6_1635b9
    - Restriccion_los_precios_aplicados_por_administrador_procesador_a_aceptadores_deben_ser_aplic_9315d5
    - Restriccion_no_corresponde_la_aplicacion_de_cedin_para_el_exclusivo_pago_de_honorarios_profe_d6b0be
    - Restriccion_no_correspondera_consignar_descripciones_relativas_al_nivel_jerarquico_o_escalaf_ba6043
    - Restriccion_no_deben_recibirse_o_demandarse_fondos_de_terceros_entendiendo_por_ellos_a_los_t_4445b9
    - Restriccion_no_deberan_registrarse_titulos_profesionales_o_de_otro_tipo_en_los_nombres_infor_9ee25a
    - Restriccion_no_se_admiten_agregados_de_ningun_tipo_al_cuerpo_del_cedin__cedin_s14_bfe97b
    - Restriccion_no_se_admiten_agregados_de_ningun_tipo_al_cuerpo_del_certificado_en_el_endoso__c_9ebfa1
    - Restriccion_no_se_admitira_el_codigo_de_motivo_2_para_la_rectificacion_de_reportes_b_5_dado__0249d3
    - Restriccion_no_se_admitira_la_utilizacion_del_codigo_e98_en_caso_de_que_ya_existiese_un_codi_c89cf8
    - Restriccion_no_se_consolidara_la_informacion_en_los_casos_de_grupos_o_conjuntos_economicos___2b19cb
    - Restriccion_no_se_consolidara_la_informacion_en_los_casos_de_grupos_o_conjuntos_economicos___8929cf
    - Restriccion_no_se_deben_cursar_mas_rapidamente_las_operaciones_de_aceptadores_vinculados__ri_0cf4a7
    - Restriccion_no_se_deduciran_bonificaciones_descuentos_u_otros_en_las_tarifas_estos_deben_inf_a7f818
    - Restriccion_no_se_deduciran_las_previsiones_por_riesgo_de_incobrabilidad_sobre_la_cartera_co_414d5c
    - Restriccion_no_se_incluiran_las_partidas_correspondientes_a_participaciones_en_otras_socieda_617b81
    - Restriccion_no_se_permite_la_aplicacion_de_cedin_para_la_cancelacion_de_cuotas_pendientes_de_fca113
    - Restriccion_prohibicion_de_aplicar_cedin_para_el_exclusivo_pago_de_honorarios_profesionales__df21da
    - Restriccion_quedan_excluidas_como_beneficiarias_todas_las_personas_juridicas_que_no_sean_otr_215186
    - Restriccion_sanciones_por_incumplimiento_de_los_articulos_1o_3o_y_38_de_la_ley_de_entidades__52c31e
    - Restriccion_se_excluyen_de_la_obligacion_de_conservacion_los_cheques_suscritos_por_terceros__271b03
    - Restriccion_se_prohibe_el_uso_de_soportes_electronicos_cuando_la_legislacion_y_o_reglamentac_8b80c7
    - Restriccion_si_se_verifica_falta_de_coincidencia_entre_los_datos_presentados_ante_el_bcra_y__f6ad5b
```

### S12 — FAIL

ERROR — Toda Excepcion tiene >=1 arista saliente exceptua o exceptua_obligacion.

**Resultado:** 36 Excepciones sin salida exceptua/exceptua_obligacion.

```
    - Excepcion_cuando_no_se_cuente_con_pasaporte_se_consignara_otros_y_se_asignara_numeracion_c_eb5485
    - Excepcion_cuando_por_el_tipo_de_producto_no_resulte_exigible_la_identificacion_fiscal_se_i_608231
    - Excepcion_el_servicio_de_ayuda_economica_queda_excluido_del_encuadramiento_regulatorio_cua_5c0df2
    - Excepcion_entidades_financieras_con_filiales_en_el_pais_y_en_el_exterior_quedan_exceptuada_bf92db
    - Excepcion_es_admisible_la_presentacion_de_facturas_o_recibos_en_legal_forma_como_alternati_e9ab5f
    - Excepcion_exencion_del_impuesto_sobre_los_creditos_y_debitos_en_cuentas_bancarias_y_otras__aabde1
    - Excepcion_la_exigencia_de_antiguedad_minima_de_un_ano_no_aplica_a_integrantes_activos_o_ad_75ffcf
    - Excepcion_la_prestacion_del_servicio_de_ayuda_economica_queda_excluida_del_encuadramiento__ff9f06
    - Excepcion_las_adendas_que_impliquen_incorporar_o_discontinuar_actividades_delegadas_quedan_5c042a
    - Excepcion_las_entidades_con_sucursales_en_el_exterior_utilizaran_el_nivel_de_consolidacion_1a758e
    - Excepcion_los_codigos_de_los_cargos_de_responsable_de_la_gerencia_general_y_responsable_de_f451c4
    - Excepcion_los_pspcp_y_opnfc_quedan_exceptuados_de_presentar_informacion_en_apartados_disti_a3aeb5
    - Excepcion_los_saldos_inmovilizados_provenientes_de_depositos_y_otras_operaciones_excluidas_0fc68c
    - Excepcion_no_aplica_lo_previsto_en_el_punto_3_3_cuando_se_trate_de_cheques_pagados_present_b8481f
    - Excepcion_no_aplica_lo_previsto_en_el_punto_3_4_certificacion_de_las_reproducciones_cuando_856b16
    - Excepcion_no_es_necesario_informar_el_ingreso_total_de_las_divisas_pendientes_de_una_desti_cec6e2
    - Excepcion_no_es_requisito_que_los_profesionales_o_asociaciones_de_profesionales_se_encuent_a22200
    - Excepcion_no_se_informaran_los_datos_15_a_19_cuando_no_hubiera_ninguna_aplicacion_parcial__4b969d
    - Excepcion_no_se_realizaran_las_verificaciones_previstas_en_el_punto_7_cuando_el_cedin_se_e_337225
    - Excepcion_no_se_realizaran_las_verificaciones_previstas_en_el_punto_cuando_el_cedin_se_enc_cd2f6c
    - Excepcion_para_entidades_cambiarias_que_no_dispongan_del_cargo_jerarquico_de_gerente_en_al_b09373
    - Excepcion_quedan_excluidos_de_la_cobertura_de_la_garantia_los_depositos_e_inversiones_a_pl_997177
    - Excepcion_quedan_excluidos_de_la_cobertura_del_seguro_de_garantia_los_cedip_transmitidos_a_537f53
    - Excepcion_quedan_excluidos_de_la_cobertura_los_depositos_de_entidades_financieras_en_otros_0cce63
    - Excepcion_quedan_excluidos_de_la_garantia_los_depositos_a_la_vista_en_los_que_se_convengan_e10bcd
    - Excepcion_quedan_excluidos_de_la_garantia_los_depositos_cuando_los_limites_de_tasa_de_inte_56bcf9
    - Excepcion_quedan_excluidos_de_la_garantia_los_depositos_e_inversiones_a_plazo_que_superen__925324
    - Excepcion_quedan_excluidos_de_la_garantia_los_depositos_efectuados_por_personas_vinculadas_c70df8
    - Excepcion_quedan_excluidos_de_los_alcances_de_la_garantia_los_depositos_a_plazo_fijo_de_ti_dc8c19
    - Excepcion_se_excluyen_del_calculo_de_la_tasa_promedio_los_prestamos_otorgados_para_refinan_746fdc
    - Excepcion_se_excluyen_las_asistencias_previstas_en_el_punto_2_2_de_las_normas_sobre_relaci_c5441d
    - Excepcion_se_excluyen_las_financiaciones_que_se_encuentren_cubiertas_con_garantias_preferi_bcc582
    - Excepcion_se_excluyen_las_partidas_deducibles_de_la_rpc__ri_ai_3_3_f19601
    - Excepcion_se_excluyen_los_activos_sujetos_a_inmovilizacion_informados_en_otros_codigos__ri_a98f26
    - Excepcion_se_suspende_la_observancia_de_las_regulaciones_tecnicas_sobre_base_consolidada_t_e84893
    - Excepcion_suspension_de_la_observancia_de_las_regulaciones_tecnicas_sobre_base_consolidada_42809b
```

### S21 — WARN

INFORMATIVA — Coherencia de remisiones entre puntos (remite_a o referencia con rol_fuente=referencia_cruzada; scripts/remisiones.py): properties.destino sin el prefijo <to>:: pertenece al CONJUNTO {p.punto for p in provenances} del nodo destino; desglose por properties.alcance (las de alcance to_entero apuntan al TextoOrdenado y se cuentan como incoherentes por construcción del enunciado).

**Resultado:** 737 remisiones ({'interna': 736, 'to_entero': 1}); 1 incoherentes (por alcance: {'to_entero': 1}).

```
idx 2691: Obligacion_se_debera_identificar_si_la_financiacion_es_otorgada_en_condiciones_preferencial_e9a431 -> TextoOrdenado_micemp_pdf destino='micemp::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', 'S0', 'S1']...
```

### S22 — PASS

INFORMATIVA — Coherencia de padre_sugerido: el destino de la arista es properties.padre_sugerido del origen y el origen está en cuarentena.

**Resultado:** 61 aristas padre_sugerido; 0 incoherentes (0 con destino distinto, 0 con origen fuera de cuarentena).

Sin violaciones.

### S23 — WARN

INFORMATIVA — aplica_a hacia sujetos en cuarentena: aristas aplica_a cuyo destino es un Sujeto de nivel propuesto (conteo; nunca bloqueante).

**Resultado:** 547 aristas aplica_a; 184 hacia Sujetos propuestos (61 destinos distintos).

```
idx 927: Excepcion_las_entidades_con_sucursales_en_el_exterior_utilizaran_el_nivel_de_consolidacion_1a758e -> Sujeto_propuesto_las_entidades_con_sucursales_en_el_exterior
idx 937: Excepcion_los_pspcp_y_opnfc_quedan_exceptuados_de_presentar_informacion_en_apartados_disti_a3aeb5 -> Sujeto_propuesto_opnfc
idx 985: Excepcion_quedan_exceptuados_de_la_obligacion_de_presentar_informes_los_pnfc_y_psp_no_cons_4db43c -> Sujeto_propuesto_aquellos_no_considerados_como_sujetos_obligados
idx 1024: Obligacion_a_los_fines_del_redondeo_de_las_magnitudes_se_incrementaran_los_valores_en_una_u_aa4a0f -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1029: Obligacion_acompanar_constancia_de_la_recepcion_de_los_materiales_ya_sea_como_leyenda_en_el_d72136 -> Sujeto_propuesto_quien_paga_con_cedin
idx 1040: Obligacion_aplicar_el_tratamiento_establecido_por_el_texto_ordenado_de_las_normas_sobre_inc_28c4f5 -> Sujeto_propuesto_las_entidades__ri_ai
idx 1047: Obligacion_calculo_del_rcl_sobre_base_consolidada_mensual_considerando_las_disposiciones_es_88d145 -> Sujeto_propuesto_las_entidades__ri_rcl
idx 1049: Obligacion_calculo_del_rcl_sobre_base_individual_considerando_la_entidad_financiera_y_sus_s_f59479 -> Sujeto_propuesto_las_entidades__ri_rcl
idx 1067: Obligacion_consignar_la_tasa_nominal_anual_maxima_de_interes_compensatorio_aplicada_a_los_a_c73d6a -> Sujeto_propuesto_las_entidades__ri_tar
idx 1070: Obligacion_consignar_los_valores_diarios_resultantes_del_calculo_del_nsfr_con_dos_decimales_5636bb -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1073: Obligacion_conversion_diaria_de_importes_en_moneda_extranjera_a_pesos_usando_el_tipo_de_cam_fdb993 -> Sujeto_propuesto_las_entidades__ri_rcl
idx 1075: Obligacion_convertir_diariamente_los_importes_en_moneda_extranjera_a_pesos_utilizando_el_ti_c43555 -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1113: Obligacion_cuando_no_existan_operaciones_a_reportar_en_un_mes_se_debera_consignar_la_opcion_645a8d -> Sujeto_propuesto_las_entidades__ri_laft
idx 1115: Obligacion_cuando_no_se_cobre_alguno_de_los_conceptos_enumerados_en_los_productos_financier_ad5c7d -> Sujeto_propuesto_las_entidades_alcanzadas
idx 1120: Obligacion_cuando_se_presente_alguna_de_las_situaciones_de_exclusion_tasas_superiores_a_ref_0d51ca -> Sujeto_propuesto_las_entidades__seggar
idx 1122: Obligacion_cuando_se_produzca_el_cierre_del_proceso_de_reproduccion_se_debera_emitir_en_la__e39a94 -> Sujeto_propuesto_las_entidades__consyr
idx 1124: Obligacion_cuando_se_trate_de_operaciones_realizadas_en_a3_mercados_y_pueda_identificarse_l_600c38 -> Sujeto_propuesto_las_entidades__ri_ot
idx 1126: Obligacion_cuando_se_trate_de_operaciones_realizadas_en_a3_mercados_y_pueda_identificarse_l_6cb11c -> Sujeto_propuesto_las_entidades__ri_ot
idx 1131: Obligacion_cuando_una_persona_sea_designada_para_un_cargo_distinto_al_que_ocupaba_consignar_07d624 -> Sujeto_propuesto_una_persona
idx 1134: Obligacion_cumplimentar_las_disposiciones_del_punto_9_7_de_la_seccion_9_del_texto_ordenado__c64ae7 -> Sujeto_propuesto_la_entidad__ri_sef
idx 1155: Obligacion_de_corresponder_se_incorporaran_las_operaciones_de_los_entes_a_que_refieren_los__34e5a0 -> Sujeto_propuesto_los_entes
idx 1159: Obligacion_deben_incluirse_en_los_datos_requeridos_los_impuestos_que_correspondan_a_cada_co_d4471a -> Sujeto_propuesto_las_entidades_alcanzadas
idx 1163: Obligacion_deber_de_consignar_el_importe_de_franquicias_otorgadas_por_el_banco_central_que__2e4f65 -> Sujeto_propuesto_las_entidades__ri_ai
idx 1168: Obligacion_deber_de_consignar_la_tasa_nominal_anual_maxima_de_interes_punitorio_aplicada_a__710585 -> Sujeto_propuesto_las_entidades__ri_tar
idx 1171: Obligacion_deber_de_desagregar_los_saldos_y_flujos_utilizando_los_codigos_de_partidas_previ_dc6a7d -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1214: Obligacion_deber_de_incluir_el_importe_de_las_franquicias_otorgadas_por_el_banco_central_qu_7bc650 -> Sujeto_propuesto_las_entidades__ri_ai
idx 1220: Obligacion_deber_de_informar_compras_y_ventas_a_termino_y_opciones_de_moneda_extranjera_ide_326a6b -> Sujeto_propuesto_las_entidades__ri_ot
idx 1230: Obligacion_deber_de_informar_el_importe_de_las_franquicias_otorgadas_por_el_banco_central_q_c5c715 -> Sujeto_propuesto_las_entidades__ri_ai
idx 1232: Obligacion_deber_de_informar_el_mail_institucional_de_la_entidad__ri_ii_31_12_19_1_3_25f2c9 -> Sujeto_propuesto_las_entidades__ri_ii_31_12_19
idx 1234: Obligacion_deber_de_informar_el_monto_correspondiente_a_lineas_de_prestamos_otorgados_en_co_518d30 -> Sujeto_propuesto_las_entidades__ri_dsf
idx 1239: Obligacion_deber_de_informar_el_porcentaje_de_rendimiento_anual_del_cupon_de_renta_del_peri_940365 -> Sujeto_propuesto_las_entidades__ri_tvf
idx 1241: Obligacion_deber_de_informar_en_forma_inmediata_a_la_gerencia_de_supervision_correspondient_84e9c0 -> Sujeto_propuesto_las_entidades__ri_rcl
idx 1275: Obligacion_deber_de_informar_la_fecha_y_numero_de_la_resolucion_del_bcra_que_se_haya_expedi_cecf66 -> Sujeto_propuesto_entidades_financieras_entidades_cambiarias
idx 1291: Obligacion_deber_de_informar_los_flujos_de_entradas_y_salidas_de_efectivo_y_de_valores_proc_c3d04a -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1320: Obligacion_deber_de_informar_los_valores_del_rcl_determinados_en_cada_dia_del_mes_tanto_en__f314b0 -> Sujeto_propuesto_las_entidades__ri_rcl
idx 1324: Obligacion_deber_de_informar_toda_persona_fisica_o_juridica_con_la_que_se_establecen_relaci_33b955 -> Sujeto_propuesto_las_entidades
idx 1326: Obligacion_deber_de_informar_una_descripcion_de_la_especie_emisor_moneda_serie_y_clase_del__f184ee -> Sujeto_propuesto_las_entidades__ri_tvf
idx 1328: Obligacion_deber_de_integrar_el_numero_de_tramite_en_la_informacion_solicitada_en_funcion_d_677ae3 -> Sujeto_propuesto_las_entidades__ri_sef
idx 1335: Obligacion_deber_de_observar_lo_prescripto_en_el_punto_1_5_2_de_las_normas_sobre_ratio_de_c_15d5d9 -> Sujeto_propuesto_las_entidades__ri_rcl
idx 1337: Obligacion_deber_de_preparar_el_balance_de_saldos_con_los_datos_correspondientes_al_ultimo__a07bc6 -> Sujeto_propuesto_las_entidades__ribspc
idx 1348: Obligacion_deber_de_utilizar_el_esquema_inserto_en_el_cuadro_1_anexo_a_la_presente_seccion__2d5203 -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1358: Obligacion_debera_constar_en_forma_visible_e_impresa_al_frente_o_al_dorso_de_todos_los_docu_0145c6 -> Sujeto_propuesto_las_entidades__seggar
idx 1376: Obligacion_debera_informarse_el_codigo_de_provincia_de_acuerdo_con_el_anexo_i_codigo_de_pro_1b5fdc -> Sujeto_propuesto_las_entidades__ri_sef
idx 1390: Obligacion_debera_informarse_la_denominacion_de_la_contraparte_de_la_operacion_mediante_ape_d2cef0 -> Sujeto_propuesto_las_entidades__ri_ot
idx 1410: Obligacion_deberan_integrar_la_informacion_de_categoria_de_la_unidad_de_servicio_en_funcion_f86d63 -> Sujeto_propuesto_las_entidades__ri_sef
idx 1457: Obligacion_el_cedin_canjeado_debe_ser_remitido_al_bcra_conforme_a_lo_previsto_en_el_punto_1_56f34b -> Sujeto_propuesto_el_cedin_canjeado
idx 1459: Obligacion_el_cedin_canjeado_debe_ser_retenido_colocandose_en_su_reverso_la_leyenda_canjead_52b908 -> Sujeto_propuesto_el_cedin_canjeado
idx 1483: Obligacion_el_importe_se_determinara_en_funcion_de_los_ultimos_datos_disponibles_incrementa_85b5b1 -> Sujeto_propuesto_las_entidades__seggar
idx 1508: Obligacion_el_proceso_de_reproduccion_debera_ajustarse_a_los_siguientes_recaudos_minimos_si_45afd8 -> Sujeto_propuesto_el_proceso_de_reproduccion
idx 1512: Obligacion_el_regimen_debe_informarse_por_novedad_las_modificaciones_de_datos_se_ingresan_e_2b96e1 -> Sujeto_propuesto_las_entidades_alcanzadas
idx 1536: Obligacion_en_caso_de_no_tener_un_vencimiento_concreto_el_flujo_de_fondos_pertinente_se_con_9c2f96 -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1543: Obligacion_en_casos_de_aprobacion_parcial_la_entidad_solicitante_debera_realizar_una_nueva__30d94f -> Sujeto_propuesto_la_entidad_solicitante
idx 1569: Obligacion_en_los_dias_en_que_no_se_registren_novedades_reiterar_el_valor_del_nsfr_del_dia__93d486 -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1572: Obligacion_en_los_dias_sin_novedades_se_reitera_el_valor_del_dia_inmediato_anterior__ri_rcl_ff3026 -> Sujeto_propuesto_las_entidades__ri_rcl
idx 1589: Obligacion_explicar_los_origenes_de_variaciones_importantes_del_lcr_durante_el_periodo_info_077ded -> Sujeto_propuesto_las_entidades__ri_rcl
idx 1597: Obligacion_identificar_las_actividades_que_se_delegaran_en_funcion_de_la_tabla_establecida__c4fa93 -> Sujeto_propuesto_las_solicitudes_de_autorizacion
idx 1626: Obligacion_inclusion_de_datos_relacionados_con_tarjetas_de_credito_de_todo_tipo_de_clientes_20873f -> Sujeto_propuesto_las_entidades__ri_tar
idx 1630: Obligacion_inclusion_en_los_datos_sobre_consumos_facturados_o_a_facturar_del_cuadro_2_de_lo_ddb2d2 -> Sujeto_propuesto_las_entidades__ri_tar
idx 1657: Obligacion_informacion_con_frecuencia_mensual__ri_ai_2_1_062d58 -> Sujeto_propuesto_la_informacion__ri_ai
idx 1705: Obligacion_informar_al_bcra_a_traves_del_sistema_habilitado_al_efecto_la_situacion_de_aplic_a0b4a0 -> Sujeto_propuesto_las_entidades__cedin
idx 1713: Obligacion_informar_el_lugar_de_emplazamiento_de_acuerdo_con_el_detalle_del_punto_b_corresp_80d8df -> Sujeto_propuesto_las_entidades__ri_sef
idx 1715: Obligacion_informar_el_pais_de_ubicacion_de_la_unidad_de_servicio_segun_el_codigo_swift__ri_e4e376 -> Sujeto_propuesto_las_entidades__ri_sef
idx 1726: Obligacion_informar_la_moneda_de_origen_de_las_operaciones_de_adquirencia_utilizando_el_cod_fa999f -> Sujeto_propuesto_los_datos
idx 1728: Obligacion_informar_la_tasa_promedio_ponderada_nominal_anual_de_los_prestamos_personales_si_036de9 -> Sujeto_propuesto_las_entidades__ri_tar
idx 1731: Obligacion_informar_los_datos_de_accionistas_de_personas_juridicas_que_sean_accionistas_de__98e3d4 -> Sujeto_propuesto_las_entidades__ri_ii_31_12_19
idx 1766: Obligacion_informar_los_mismos_datos_mas_el_punto_2_11_respecto_de_quienes_hubieran_cesado__713e67 -> Sujeto_propuesto_aquellos_que_por_finalizacion_del_mandato_u_otras_causas_hubieran_cesado_en_sus_
idx 1777: Obligacion_informar_valor_maximo_nsfr_mensual__ri_tsa_2_2_326249 -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1779: Obligacion_informar_valor_minimo_nsfr_mensual__ri_tsa_2_2_f4aef6 -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1781: Obligacion_informar_valores_del_ratio_nsfr_mensual__ri_tsa_2_2_943f6a -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1787: Obligacion_integracion_con_datos_del_mes_bajo_analisis__ri_ai_2_1_336de0 -> Sujeto_propuesto_la_informacion__ri_ai
idx 1793: Obligacion_integrar_en_la_solicitud_el_codigo_interurbano_y_telefono_de_la_unidad_de_servic_faf47d -> Sujeto_propuesto_las_entidades__ri_sef
idx 1803: Obligacion_la_cantidad_de_activo_subyacente_debe_informarse_como_el_importe_en_la_moneda_co_05828f -> Sujeto_propuesto_las_entidades__ri_ot
idx 1829: Obligacion_la_direccion_debe_prestar_debida_atencion_al_mantenimiento_de_procedimientos_act_7ca28b -> Sujeto_propuesto_la_direccion
idx 1832: Obligacion_la_documentacion_debera_incluir_todos_los_componentes_del_costo_de_la_refaccion__39b6e9 -> Sujeto_propuesto_las_entidades__cedin
idx 1834: Obligacion_la_documentacion_que_se_reciba_en_copia_debera_estar_inicialada_por_los_presenta_500fe5 -> Sujeto_propuesto_los_presentantes
idx 1915: Obligacion_la_entidad_interviniente_debe_identificar_la_aplicacion_del_cedin_en_el_dorso_de_6f8b83 -> Sujeto_propuesto_la_entidad_interviniente
idx 1922: Obligacion_la_informacion_debe_integrarse_en_pesos_o_la_denominacion_que_corresponda_con_do_231522 -> Sujeto_propuesto_las_entidades_alcanzadas
idx 1926: Obligacion_la_informacion_proporcionada_debe_indicar_su_validez_para_las_provincias_selecci_03542e -> Sujeto_propuesto_las_entidades_alcanzadas
idx 1929: Obligacion_la_informacion_requerida_en_los_puntos_ii_b_y_ii_c_debera_ser_integrada_en_forma_80b98d -> Sujeto_propuesto_las_entidades__ri_acsf
idx 1938: Obligacion_la_presentacion_de_informacion_tiene_caracter_de_declaracion_jurada_los_director_28b71b -> Sujeto_propuesto_la_entidad__ri_nge
idx 1949: Obligacion_las_adendas_con_nuevas_incorporaciones_de_agencias_complementarias_implicaran_un_b25602 -> Sujeto_propuesto_la_entidad__ri_sef
idx 1951: Obligacion_las_adendas_que_impliquen_incorporar_o_discontinuar_actividades_delegadas_implic_301223 -> Sujeto_propuesto_la_entidad__ri_sef
idx 1954: Obligacion_las_asociaciones_mutuales_y_cooperativas_que_sean_otros_proveedores_no_financier_d86623 -> Sujeto_propuesto_aquellos_otros_proveedores_no_financieros_de_credito_que_sean_asociaciones_mutua
idx 1976: Obligacion_las_entidades_alcanzadas_deben_informar_los_datos_solicitados_a_traves_del_sitio_adcebf -> Sujeto_propuesto_las_entidades_alcanzadas
idx 1978: Obligacion_las_entidades_deben_consignar_en_el_modelo_de_informacion_la_cantidad_de_tarjeta_d7480a -> Sujeto_propuesto_las_entidades__ri_tar
idx 1982: Obligacion_las_entidades_deben_consignar_nueve_datos_especificos_en_la_certificacion_de_cum_2feb3c -> Sujeto_propuesto_las_entidades__ri_secoexpo
idx 1985: Obligacion_las_entidades_deben_continuar_informando_a_sus_deudores_mientras_persistan_las_g_6fee0a -> Sujeto_propuesto_las_entidades__ri_dsf
idx 1987: Obligacion_las_entidades_deben_cumplimentar_el_requerimiento_cuando_se_hayan_producido_nove_2e2237 -> Sujeto_propuesto_las_entidades__ri_ii_31_12_19
idx 1991: Obligacion_las_entidades_deben_informar_el_porcentaje_de_cuentas_que_corresponden_a_persona_e3f95a -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1993: Obligacion_las_entidades_deben_informar_el_porcentaje_de_cuentas_que_corresponden_a_persona_f865a3 -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1995: Obligacion_las_entidades_deben_informar_la_cantidad_de_cuentas_declarables__ri_tsa_sbloque3_a4fecc -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1997: Obligacion_las_entidades_deben_informar_si_registran_cuentas_declarables_en_pesos_y_o_en_mo_fbc04b -> Sujeto_propuesto_las_entidades__ri_tsa
idx 1999: Obligacion_las_entidades_deben_informar_su_situacion_como_obligadas_o_no_obligadas__ri_tsa__1dae0c -> Sujeto_propuesto_las_entidades__ri_tsa
idx 2001: Obligacion_las_entidades_deben_presentar_la_fecha_a_la_que_corresponde_la_informacion_solic_f16ceb -> Sujeto_propuesto_las_entidades__ri_tsa
idx 2005: Obligacion_las_entidades_deben_remitir_informacion_de_las_destinaciones_de_exportacion_de_b_83abbd -> Sujeto_propuesto_las_entidades__ri_secoexpo
idx 2008: Obligacion_las_entidades_deben_seguir_informando_a_sus_deudores_en_la_medida_que_continuen__0065ca -> Sujeto_propuesto_las_entidades__ri_dsf
idx 2010: Obligacion_las_entidades_deberan_aplicar_los_aforos_y_los_respectivos_factores_en_la_etapa__8031bc -> Sujeto_propuesto_esta_institucion
idx 2012: Obligacion_las_entidades_deberan_consignar_la_ubicacion_geografica_de_la_unidad_de_servicio_e40915 -> Sujeto_propuesto_las_entidades__ri_sef
idx 2014: Obligacion_las_entidades_deberan_efectuar_un_aporte_adicional_diferenciado_segun_sea_el_res_890778 -> Sujeto_propuesto_las_entidades__seggar
idx 2018: Obligacion_las_entidades_deberan_integrar_la_informacion_requerida_en_funcion_del_tipo_y_et_98d7ba -> Sujeto_propuesto_las_entidades__ri_sef
idx 2020: Obligacion_las_entidades_deberan_mantener_a_disposicion_de_su_clientela_los_textos_completo_72bb58 -> Sujeto_propuesto_las_entidades__seggar
idx 2022: Obligacion_las_entidades_deberan_numerar_secuencialmente_las_unidades_que_dependen_de_una_m_0eda27 -> Sujeto_propuesto_las_unidades
idx 2024: Obligacion_las_entidades_deberan_remitir_al_bcra_un_ejemplar_del_informe_anual_del_revisor__e83efa -> Sujeto_propuesto_las_entidades__ri_laft
idx 2026: Obligacion_las_entidades_deberan_remitir_la_totalidad_de_reportes_de_transacciones_en_efect_c9c044 -> Sujeto_propuesto_las_entidades__ri_laft
idx 2040: Obligacion_las_entidades_financieras_deberan_aplicar_lo_previsto_en_las_normas_sobre_preven_414f39 -> Sujeto_propuesto_las_entidades__cedin
idx 2068: Obligacion_las_entidades_financieras_deberan_reflejar_el_verdadero_caracter_y_la_existencia_f5098f -> Sujeto_propuesto_las_entidades__verac
idx 2074: Obligacion_las_entidades_financieras_deberan_remitir_la_informacion_que_debe_acompanar_la_s_206e5c -> Sujeto_propuesto_las_entidades__ri_sef
idx 2079: Obligacion_las_entidades_financieras_deberan_satisfacer_los_requisitos_generales_para_la_pr_8d0937 -> Sujeto_propuesto_las_entidades__consyr
idx 2108: Obligacion_las_entidades_o_empresas_constituidas_en_el_exterior_que_no_posean_esa_identific_314b20 -> Sujeto_propuesto_las_entidades_o_empresas_constituidas_en_el_exterior
idx 2113: Obligacion_las_entidades_recibiran_informacion_del_apartado_a_mediante_archivos_encriptados_6ac3d7 -> Sujeto_propuesto_las_entidades__ri_secoexpo
idx 2125: Obligacion_las_informaciones_tendran_el_alcance_previsto_para_el_nivel_de_consolidacion_men_61fc9e -> Sujeto_propuesto_las_informaciones
idx 2129: Obligacion_las_novedades_que_se_registren_deben_ser_informadas_remitiendo_una_nueva_certifi_7a8b00 -> Sujeto_propuesto_las_novedades
idx 2134: Obligacion_las_operaciones_de_swaps_de_moneda_deben_informarse_desagregando_la_transaccion__ddfb05 -> Sujeto_propuesto_las_entidades__ri_ot
idx 2136: Obligacion_las_operaciones_rescindidas_o_ejercidas_con_anterioridad_a_la_fecha_de_vencimien_b7f054 -> Sujeto_propuesto_las_entidades__ri_ot
idx 2138: Obligacion_las_operaciones_sin_vencimiento_deberan_informarse_como_bajas_siempre_que_se_can_2300ec -> Sujeto_propuesto_las_entidades__ri_ot
idx 2141: Obligacion_las_reducciones_en_las_comisiones_y_o_cargos_se_informaran_dentro_de_los_treinta_8edd64 -> Sujeto_propuesto_las_reducciones_en_las_comisiones_y_o_cargos
idx 2143: Obligacion_las_registraciones_contables_que_efectuen_las_entidades_deben_reflejar_en_forma__20bf90 -> Sujeto_propuesto_las_entidades__verac
idx 2145: Obligacion_las_salidas_se_asignaran_a_las_bandas_temporales_teniendo_en_cuenta_la_primera_f_a02687 -> Sujeto_propuesto_las_entidades__ri_tsa
idx 2148: Obligacion_las_tasas_se_registraran_en_tanto_por_ciento_con_dos_decimales__ri_tar_s1_70f3b5 -> Sujeto_propuesto_las_entidades__ri_tar
idx 2150: Obligacion_los_accionistas_que_deban_ser_informados_en_forma_agrupada_tenencias_inferiores__722775 -> Sujeto_propuesto_las_entidades__ri_ii_31_12_19
idx 2152: Obligacion_los_accionistas_que_deban_ser_informados_en_forma_agrupada_tenencias_inferiores__c9f5e0 -> Sujeto_propuesto_las_entidades__ri_ii_31_12_19
idx 2164: Obligacion_los_componentes_del_regimen_deben_ser_presentados_a_la_superintendencia_de_entid_3d7156 -> Sujeto_propuesto_las_entidades__ri_nge
idx 2211: Obligacion_los_documentos_entregados_en_reemplazo_del_cedin_presentado_al_canje_mantendran__32dd06 -> Sujeto_propuesto_los_que_se_entreguen_en_su_reemplazo
idx 2234: Obligacion_los_importes_en_moneda_extranjera_se_convertiran_a_pesos_utilizando_el_tipo_de_c_ffc19e -> Sujeto_propuesto_las_entidades__ri_tsa
idx 2237: Obligacion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales__ri_esd_sbloque1_9d0b4b -> Sujeto_propuesto_los_importes
idx 2239: Obligacion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales__ri_tsa_3_1_9fe2c6 -> Sujeto_propuesto_las_entidades__ri_tsa
idx 2243: Obligacion_los_importes_se_registraran_en_pesos_sin_decimales__ri_tar_s1_65eb91 -> Sujeto_propuesto_las_entidades__ri_tar
idx 2246: Obligacion_los_inventarios_de_clientes_los_extractos_bancarios_y_toda_documentacion_respald_80a784 -> Sujeto_propuesto_los_pspcp
idx 2248: Obligacion_los_meses_se_consideraran_segun_mes_calendario_independientemente_de_su_cantidad_97a557 -> Sujeto_propuesto_las_entidades__ri_tsa
idx 2253: Obligacion_los_movimientos_deben_informarse_totalizando_las_operaciones_de_cada_dia_de_la_s_7b8f44 -> Sujeto_propuesto_las_entidades__ri_ot
idx 2272: Obligacion_los_socios_gerentes_y_gerentes_no_socios_en_sociedades_de_responsabilidad_limita_8c28df -> Sujeto_propuesto_sociedad_de_responsabilidad_limitada
idx 2296: Obligacion_mantendra_su_frecuencia_trimestral_con_datos_de_cada_mes_del_trimestre_y_su_venc_adb29a -> Sujeto_propuesto_la_informacion__ri_tsa
idx 2298: Obligacion_mantener_a_disposicion_de_la_sefyc_el_valor_diario_del_ratio_nsfr_calculado_de_a_4979af -> Sujeto_propuesto_las_entidades__ri_tsa
idx 2302: Obligacion_mientras_no_se_cuente_con_documentos_que_contengan_las_leyendas_en_forma_impresa_03f32f -> Sujeto_propuesto_las_entidades__seggar
idx 2322: Obligacion_para_cada_periodo_informado_se_controlara_que_se_encuentre_presentado_el_periodo_f12db4 -> Sujeto_propuesto_las_entidades__ri_laft
idx 2330: Obligacion_para_el_calculo_de_las_relaciones_vi_aprc_rpc_etc_se_deben_considerar_los_import_33a972 -> Sujeto_propuesto_las_entidades__seggar
idx 2338: Obligacion_para_la_conversion_de_los_saldos_en_dolares_se_utilizara_el_tipo_de_cambio_de_re_f5d168 -> Sujeto_propuesto_las_entidades__ri_tar
idx 2346: Obligacion_para_las_unidades_de_servicio_codigo_37_la_numeracion_secuencial_debe_realizarse_eb4e9f -> Sujeto_propuesto_las_unidades_de_servicio_codigo_37
idx 2357: Obligacion_para_operaciones_sin_vencimiento_siempre_debe_informarse_su_baja_cuando_se_cance_91b910 -> Sujeto_propuesto_las_entidades__ri_ot
idx 2360: Obligacion_para_personas_fisicas_accionistas_se_informara_el_tipo_y_numero_de_identificacio_58ca14 -> Sujeto_propuesto_personas_fisicas
idx 2378: Obligacion_para_personas_juridicas_constituidas_en_el_exterior_que_no_posean_clave_unica_de_64b30b -> Sujeto_propuesto_las_constituidas_en_el_exterior
idx 2386: Obligacion_por_cada_entidad_financiera_en_la_que_se_encuentren_acreditados_fondos_de_cuenta_cf75fe -> Sujeto_propuesto_los_pspcp
idx 2388: Obligacion_por_cada_fondo_comun_de_dinero_en_el_que_se_encuentren_invertidos_fondos_de_clie_0a6073 -> Sujeto_propuesto_los_pspcp
idx 2390: Obligacion_por_cada_una_de_las_actividades_detalladas_en_la_tabla_de_actividades_comprendid_3dccc4 -> Sujeto_propuesto_las_entidades__ri_acsf
idx 2392: Obligacion_por_cada_una_de_las_actividades_detalladas_en_la_tabla_de_actividades_comprendid_de99ed -> Sujeto_propuesto_las_entidades__ri_acsf
idx 2398: Obligacion_presentacion_de_cedin_pagados_mediante_nota_en_original_y_copia_con_membrete_y_f_134045 -> Sujeto_propuesto_las_entidades__cedin
idx 2402: Obligacion_presentacion_mensual_de_informaciones__ri_tar_s1_b34583 -> Sujeto_propuesto_las_entidades__ri_tar
idx 2445: Obligacion_proporcionar_informaciones_de_los_puntos_2_1_a_2_10_y_2_12_a_2_21_respecto_de_ca_4b11c7 -> Sujeto_propuesto_cada_uno_de_los_integrantes_del_directorio_titulares_y_suplentes_gerencia_en_el_
idx 2496: Obligacion_proporcionar_respecto_de_las_areas_gerenciales_detalladas_en_la_tabla_no_4_geren_839304 -> Sujeto_propuesto_las_entidades__ri_ii_31_12_19
idx 2546: Obligacion_remision_de_documentacion_sobre_las_condiciones_operativas_en_las_cuales_funcion_a486e9 -> Sujeto_propuesto_las_entidades__ri_sef
idx 2548: Obligacion_remision_de_documentacion_sobre_novedades_respecto_a_las_sucursales_en_el_exteri_3669d0 -> Sujeto_propuesto_las_entidades__ri_sef
idx 2552: Obligacion_remision_del_listado_de_cuit_cuil_de_las_personas_que_hayan_realizado_al_menos_u_d0a56c -> Sujeto_propuesto_las_entidades__ri_acsf
idx 2558: Obligacion_remitir_con_frecuencia_mensual_junto_con_el_detalle_diario_del_ratio_de_cobertur_3c35c0 -> Sujeto_propuesto_las_entidades__ri_rcl
idx 2566: Obligacion_remitir_por_primera_vez_la_informacion_en_forma_completa_consignando_los_datos_q_ea9d8f -> Sujeto_propuesto_la_informacion
idx 2570: Obligacion_remitir_una_copia_del_contrato_marco_a_la_gerencia_de_autorizaciones_con_las_for_16deda -> Sujeto_propuesto_la_entidad__ri_sef
idx 2575: Obligacion_respecto_de_cada_uno_de_los_dias_del_mes_bajo_informe_se_deberan_integrar_los_da_b4d3a4 -> Sujeto_propuesto_los_pspcp
idx 2633: Obligacion_se_debera_consignar_el_codigo_interurbano_telefono_directo_fax_y_telefono_de_la__5e684d -> Sujeto_propuesto_las_entidades__ri_ii_31_12_19
idx 2702: Obligacion_se_debera_indicar_si_se_trata_de_una_solicitud_de_autorizacion_para_aprobacion_d_7cb478 -> Sujeto_propuesto_las_entidades__ri_sef
idx 2712: Obligacion_se_debera_informar_el_tipo_de_unidad_de_servicio_de_acuerdo_con_el_detalle_del_a_2e4a75 -> Sujeto_propuesto_las_entidades__ri_sef
idx 2721: Obligacion_se_debera_integrar_informacion_sobre_el_tipo_de_tramite_segun_las_opciones_descr_973929 -> Sujeto_propuesto_las_entidades__ri_sef
idx 2723: Obligacion_se_debera_integrar_la_informacion_de_fecha_de_inicio_o_baja_de_actividades_en_fu_03f3b6 -> Sujeto_propuesto_las_entidades__ri_sef
idx 2777: Obligacion_se_informara_el_e_mail_del_gerente__ri_ii_31_12_19_3_12_7b77f2 -> Sujeto_propuesto_las_entidades__ri_ii_31_12_19
idx 2791: Obligacion_se_informara_el_tipo_de_accionista_de_acuerdo_con_el_codigo_de_la_tabla_no_5_que_b1ebca -> Sujeto_propuesto_las_entidades__ri_ii_31_12_19
idx 2822: Obligacion_se_informaran_el_tipo_y_numero_de_documento_de_identidad_de_los_responsables_de__514c8f -> Sujeto_propuesto_las_entidades__ri_ii_31_12_19
idx 2834: Obligacion_se_informaran_el_tipo_y_numero_de_identificacion_fiscal_teniendo_en_cuenta_las_i_0889de -> Sujeto_propuesto_responsable_de_area_gerencial
idx 2841: Obligacion_se_informaran_los_apellidos_en_forma_completa_segun_consta_en_el_padron_de_la_ag_74c75f -> Sujeto_propuesto_las_entidades__ri_ii_31_12_19
idx 2876: Obligacion_se_suspende_el_envio_de_informaciones_con_codigo_de_consolidacion_3_a_partir_del_62cec8 -> Sujeto_propuesto_las_entidades__ri_ai
idx 2893: Obligacion_sedesa_debe_rechazar_o_posponer_hasta_su_reconocimiento_judicial_el_pedido_de_co_282087 -> Sujeto_propuesto_sedesa
idx 2904: Obligacion_siempre_debe_informarse_el_precio_de_tarifario_del_producto__ri_transpa_s14_d477b5 -> Sujeto_propuesto_las_entidades_alcanzadas
idx 2928: Obligacion_utilizar_el_numero_de_tramite_generado_por_la_presentacion_inicial_al_momento_de_3eff90 -> Sujeto_propuesto_la_entidad__ri_sef
idx 3073: Operacion_financiacion_a_otras_mutuales__asomut_2_2_d4084c -> Sujeto_propuesto_otras_mutuales
idx 3099: Operacion_informacion_de_codigo_swift_del_mercado__ri_tvf_s14_4a51f3 -> Sujeto_propuesto_las_entidades__ri_tvf
idx 3351: Potestad_facultad_de_ofrecer_mejores_condiciones__la_entidad_puede_ofrecer_en_cualquiera__355770 -> Sujeto_propuesto_la_entidad
idx 3367: Potestad_remitir_nuevas_certificaciones_de_ampliacion__facultad_de_remitir_nuevas_certifi_76bf69 -> Sujeto_propuesto_las_entidades__ri_secoexpo
idx 3396: Restriccion_cuando_se_informa_una_operacion_con_codigo_de_condicion_n_5_el_monto_en_dolares__ff2027 -> Sujeto_propuesto_una_operacion
idx 3412: Restriccion_el_mail_institucional_debe_ser_generico_para_la_recepcion_de_todo_tipo_de_consul_f3353b -> Sujeto_propuesto_las_entidades__ri_ii_31_12_19
idx 3536: Restriccion_los_valores_diarios_resultantes_del_calculo_del_rcl_se_consignaran_con_dos_decim_b10ad9 -> Sujeto_propuesto_las_entidades__ri_rcl
idx 3540: Restriccion_no_correspondera_efectuar_supuestos_acerca_de_la_fecha_de_vencimiento_de_los_ins_fcb8ef -> Sujeto_propuesto_las_entidades__ri_tsa
idx 3545: Restriccion_no_deberan_registrarse_titulos_profesionales_o_de_otro_tipo_en_el_campo_de_apell_18696f -> Sujeto_propuesto_las_entidades__ri_ii_31_12_19
idx 3548: Restriccion_no_puede_aplicarse_a_los_usuarios_de_servicios_financieros_un_costo_cargo_o_tasa_8f7326 -> Sujeto_propuesto_la_entidad
idx 3568: Restriccion_no_se_efectuaran_supuestos_de_renovacion_de_los_pasivos_existentes_ni_de_realiza_0de1ce -> Sujeto_propuesto_las_entidades__ri_tsa
idx 3574: Restriccion_prohibicion_de_consignar_los_campos_identificacion_fiscal_y_denominacion_de_la_c_de47dd -> Sujeto_propuesto_las_entidades__ri_ot
idx 3581: Restriccion_se_prohibe_la_realizacion_de_operaciones_o_actos_que_impliquen_la_constitucion_d_951a79 -> Sujeto_propuesto_las_entidades__verac
idx 3583: Restriccion_se_prohibe_llevar_a_cabo_ardides_o_acciones_que_desnaturalicen_el_caracter_de_lo_68f47f -> Sujeto_propuesto_las_entidades__verac
```

### S32 — PASS

INFORMATIVA — Cuantía en la descripción => elemento en la lista (informativa; L-ESQ-R2 §1.5 y reports/u_umbral/reporte_u_umbral.md §2): en los tipos con lista de umbrales, un nodo cuya descripción trae una cuantía (reglas_comparacion.detectar_cuantias) tiene la lista no vacía o el umbral guardado (marca); aparte, las cuantías de la descripción sin un elemento de igual valor y unidad.

**Resultado:** 72 nodos con cuantía en la descripción: 72 con lista, 0 con el umbral guardado (marca), 0 sin ninguna {}; cuantías de la descripción 91, sin elemento de igual valor y unidad 5.

Sin violaciones.

## Tabla resumen

| Severidad | Regla | Resultado | Resumen |
|---|---|---|---|
| bloqueante | S1 | PASS | 3822/3822 aristas con relación admitida (19 relaciones admitidas); 0 violaciones. |
| bloqueante | S2 | PASS | 0 aristas colgantes sobre 3822. |
| bloqueante | S3 | PASS | 3822/3822 aristas conformes a firma; 0 violaciones. Evaluadas: 2898 por matriz, 737 remite_a, 126 de esqueleto, 61 padre_sugerido. |
| bloqueante | S4 | PASS | Nodos OK: 2207/2207. Aristas OK: 3822/3822. Violaciones: 0. |
| bloqueante | S5 | PASS | Nodos con punto: 2207/2207. Aristas: 3822/3822. Violaciones: 0. |
| bloqueante | S6 | PASS | Archivos válidos (70): TextoOrdenado ['asomut.pdf', 'cedin.pdf', 'consyr.pdf', 'micemp.pdf', 'ri_acsf.pdf', 'ri_ai.pdf', 'ri_bdp.pdf', 'ri_cr.pdf', 'ri_dsf.pdf', 'ri_esd.pdf', 'ri_ieccm.pdf', 'ri_iepsp.pdf', 'ri_iesinap.pdf', 'ri_ii_31_12_19.pdf', 'ri_laft.pdf', 'ri_msrl.pdf', 'ri_nge.pdf', 'ri_ot.pdf', 'ri_psp.pdf', 'ri_pspapt.pdf', 'ri_rcl.pdf', 'ri_secoexpo.pdf', 'ri_sef.pdf', 'ri_tar.pdf', 'ri_transpa.pdf', 'ri_tsa.pdf', 'ri_tvf.pdf', 'ribspc.pdf', 'seggar.pdf', 'verac.pdf'] ∪ esqueleto ['TO_capitales_minimos_actual.pdf', 'TO_clasificacion_deudores_actual.pdf', 'TO_exterior_cambios_actual.pdf', 'TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'TO_regimen_informativo_contable_mensual_actual.pdf', 'actgar.pdf', 'adrei.pdf', 'autenf.pdf', 'catalogo_sujetos_v3.json', 'ccbcra.pdf', 'convca.pdf', 'cryl.pdf', 'ctacor.pdf', 'depaho.pdf', 'efemin.pdf', 'esquema_v2_clases.json', 'esquema_v3_clases.json', 'fabcra.pdf', 'icmecma.pdf', 'lavdin.pdf', 'lingob.pdf', 'ordcom.pdf', 'osapsa.pdf', 'pagjub.pdf', 'pfmipyme.pdf', 'pimf.pdf', 'ratiofn.pdf', 'rdbcra.pdf', 'repefe.pdf', 'retype.pdf', 'rmrtsd.pdf', 'rrci.pdf', 'servco.pdf', 'snp_atm.pdf', 'snp_debin.pdf', 'snp_psp.pdf', 'snp_spd.pdf', 'snp_tr_nc.pdf', 'supcon.pdf', 'traval.pdf']. Violaciones: 0. |
| bloqueante | S15 | PASS | 35 roles, 51 aristas miembro_de; 12 huérfanos (12 declarados, 0 sin declarar); 0 miembros que no son clase. Lista declarada: 12 ({'sin_id_en_catalogo': 6, 'aplanamiento_rechazado': 5, 'instancia_rechazada': 1}). |
| bloqueante | S18 | PASS | 23 Restricciones limite_cuantitativo: 23 con lista, 0 con el umbral guardado sin lista (marca), 0 sin ninguna. |
| bloqueante | S19 | PASS | 171 Sujetos ({'clase': 70, 'instancia': 5, 'propuesto': 61, 'rol': 35}); catálogo de 110 ids; 0 fuera del catálogo, 0 con nivel inválido, 0 propuestos incompletos. |
| bloqueante | S20 | PASS | 850 nodos Obligacion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 0. |
| bloqueante | S24 | PASS | 94 nodos Restriccion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 0. |
| bloqueante | S25 | PASS | 49 nodos Comunicacion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 17. |
| bloqueante | S26 | PASS | 2036 nodos evaluados; 0 violaciones {}; marcas de nodo admitidas: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']. |
| bloqueante | S28 | PASS | 61 Sujetos propuestos; 229 filas en el registro; 0 propuestos sin fila. |
| bloqueante | S29 | PASS | 61 aristas padre_sugerido; 0 con destino fuera del catálogo único (110 ids). |
| bloqueante | S30 | PASS | 737 aristas remite_a ({'interna': 736, 'to_entero': 1}); 0 violaciones. |
| bloqueante | S31 | PASS | 737 aristas remite_a: {'en_un_tramo_del_chunk_de_la_arista': 737}; 0 violaciones. |
| bloqueante | S27 | PASS | 549 aristas de sujeto fuera del esqueleto; 0 sin mención, verificación o método ({}). |
| informativa | S7 | FAIL | 50 grupos violatorios (122 nodos involucrados). |
| informativa | S8 | WARN | 3 grupos con el mismo label normalizado en types distintos. |
| informativa | S9 | PASS | 0 nodos con ambas keys. |
| informativa | S10 | PASS | Sin establecida_en: Condicion=0, Definicion=0, Excepcion=0, Obligacion=0, Operacion=0, Potestad=0, Restriccion=0 (total 0). |
| informativa | S11 | WARN | Sin aplica_a: Excepcion=58, Obligacion=418, Operacion=239, Potestad=28, Restriccion=59 (total 802). |
| informativa | S12 | FAIL | 36 Excepciones sin salida exceptua/exceptua_obligacion. |
| informativa | S21 | WARN | 737 remisiones ({'interna': 736, 'to_entero': 1}); 1 incoherentes (por alcance: {'to_entero': 1}). |
| informativa | S22 | PASS | 61 aristas padre_sugerido; 0 incoherentes (0 con destino distinto, 0 con origen fuera de cuarentena). |
| informativa | S23 | WARN | 547 aristas aplica_a; 184 hacia Sujetos propuestos (61 destinos distintos). |
| informativa | S32 | PASS | 72 nodos con cuantía en la descripción: 72 con lista, 0 con el umbral guardado (marca), 0 sin ninguna {}; cuantías de la descripción 91, sin elemento de igual valor y unidad 5. |

**Veredicto global: PASA**

## Numeración de las shapes del perfil r2

- S18: Reescrita (L-ESQ-R2 §1.5): Restriccion de tipo limite_cuantitativo => lista de umbrales no vacía o marca (el umbral guardado sin lista: campos_heredados_v3.umbral o properties_no_definidas.umbral; en r2b, también la marca properties_no_definidas.umbral_no_cuantificable del ensamblado). El enunciado de docs/esquema_v2_diseño.md:325 no rige en el perfil r2.
- S24: Enum de Restriccion.tipo (bloqueante salvo la marca fuera_de_lista).
- S25: Enum de Comunicacion.tipo, con «externa» (bloqueante salvo la marca fuera_de_lista).
- S26: Claves cerradas por tipo (bloqueante).
- S27: Arista de sujeto con mención y método (informativa en r2a, bloqueante desde r2b).
- S28: Sujeto propuesto con fila en el registro de no mapeados (bloqueante).
- S29: Destino de padre_sugerido en el catálogo único (bloqueante: U-CAT-UNICO está cerrada).
- S30: alcance de remite_a en la lista cerrada y coherente con los extremos (bloqueante).
- S31: evidencia de remite_a: tramo literal de un único tramo del texto de E0 de su chunk_id (bloqueante; sin --e0, NO COMPUTABLE).
- S32: Cuantía en la descripción => elemento en la lista (informativa; L-ESQ-R2 §1.5 y reports/u_umbral/reporte_u_umbral.md §2): en los tipos con lista de umbrales, un nodo cuya descripción trae una cuantía (reglas_comparacion.detectar_cuantias) tiene la lista no vacía o el umbral guardado (marca); aparte, las cuantías de la descripción sin un elemento de igual valor y unidad.
