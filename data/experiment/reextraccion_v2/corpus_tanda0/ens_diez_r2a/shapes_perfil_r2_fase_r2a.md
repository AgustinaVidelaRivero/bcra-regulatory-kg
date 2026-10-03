# Validador de shapes — perfil r2

- **Grafo:** `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/r2/kg.json`
- **sha256 del grafo:** `99fe2bfa0de05704e4c636bdf9b0455a30e29b378e3b0e61eadc49dad3f7c649`
- **Fecha:** 2026-10-03
- **Nodos:** 8358
- **Aristas:** 29499
- **Perfil:** r2 (fase r2a)
- **Vocabulario:** `/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/pyd_r2/generados/enums_r2.json` (sha256 `abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241`); marcas de nodo de `/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/pyd_r2/code/modelos_r2.py`: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']
- **Catálogo único (S19, S29):** `/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json` — 110 ids
- **Lista de S15:** `/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json`
- **Registro (S28):** `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/r2/no_mapeados_sujetos.jsonl`
- **E0 (S31):** `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2`
- **Veredicto global: NO PASA** — bloqueantes en FAIL: S18

## Bloqueantes

### S1 — PASS

Toda arista usa una relación admitida por el perfil r2: los 13 predicados de enums_r2.json ∪ remite_a (enmienda 2 de L-ESQ-R2) ∪ las 4 de esqueleto ∪ padre_sugerido.

**Resultado:** 29499/29499 aristas con relación admitida (19 relaciones admitidas); 0 violaciones.

Sin violaciones.

### S2 — PASS

Integridad referencial: origen y destino de toda arista existen como nodos.

**Resultado:** 0 aristas colgantes sobre 29499.

Sin violaciones.

### S3 — PASS

Toda arista respeta las firmas del perfil r2: matriz ampliada de enums_r2.json (firmas_r2, con condicion_de -> Operacion|Potestad) ∪ remite_a con origen en los siete tipos de contenido y destino en esos siete o TextoOrdenado ∪ esqueleto solo Sujeto->Sujeto ∪ padre_sugerido solo de Sujeto propuesto a Sujeto clase|rol. Una referencia con origen distinto de TextoOrdenado es violación, con o sin rol_fuente.

**Resultado:** 29499/29499 aristas conformes a firma; 0 violaciones. Evaluadas: 15349 por matriz, 14000 remite_a, 126 de esqueleto, 24 padre_sugerido.

Sin violaciones.

### S4 — PASS

Todo nodo y toda arista tienen provenance dict con al menos {to, archivo, punto, rol_documental}, provenances lista no vacía con provenance == provenances[0]; para rol_documental distinto de esqueleto, to y archivo no vacíos (para esqueleto se admiten to nulo, chunk_id nulo y paginas vacía).

**Resultado:** Nodos OK: 8358/8358. Aristas OK: 29499/29499. Violaciones: 0.

Sin violaciones.

### S5 — PASS

Todo provenance.punto (de nodo y de arista) es una string no vacía.

**Resultado:** Nodos con punto: 8358/8358. Aristas: 29499/29499. Violaciones: 0.

Sin violaciones.

### S6 — PASS

Todo provenance.archivo pertenece a {properties.archivo de los nodos TextoOrdenado} ∪ {archivo de las provenances con rol_documental=esqueleto}; nada codificado a mano.

**Resultado:** Archivos válidos (43): TextoOrdenado ['TO_capitales_minimos_actual.pdf', 'TO_clasificacion_deudores_actual.pdf', 'TO_exterior_cambios_actual.pdf', 'TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'TO_regimen_informativo_contable_mensual_actual.pdf', 'ctacte.pdf', 'docvig.pdf', 'lingob.pdf', 'pagjub.pdf', 'polcre.pdf'] ∪ esqueleto ['actgar.pdf', 'adrei.pdf', 'autenf.pdf', 'catalogo_sujetos_v3.json', 'ccbcra.pdf', 'convca.pdf', 'cryl.pdf', 'ctacor.pdf', 'depaho.pdf', 'efemin.pdf', 'esquema_v2_clases.json', 'esquema_v3_clases.json', 'fabcra.pdf', 'icmecma.pdf', 'lavdin.pdf', 'ordcom.pdf', 'osapsa.pdf', 'pfmipyme.pdf', 'pimf.pdf', 'ratiofn.pdf', 'rdbcra.pdf', 'repefe.pdf', 'retype.pdf', 'rmrtsd.pdf', 'rrci.pdf', 'servco.pdf', 'snp_atm.pdf', 'snp_debin.pdf', 'snp_psp.pdf', 'snp_spd.pdf', 'snp_tr_nc.pdf', 'supcon.pdf', 'traval.pdf']. Violaciones: 0.

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

### S18 — FAIL

ERROR — Reescrita (L-ESQ-R2 §1.5): Restriccion de tipo limite_cuantitativo => lista de umbrales no vacía o marca (el umbral guardado sin lista: campos_heredados_v3.umbral o properties_no_definidas.umbral). El enunciado de docs/esquema_v2_diseño.md:325 no rige en el perfil r2.

**Resultado:** 301 Restricciones limite_cuantitativo: 253 con lista, 22 con el umbral guardado sin lista (marca), 26 sin ninguna.

```
nodo Restriccion_cuando_la_suma_de_los_requisitos_de_capital_de_una_entidad_financiera_por_exposi_496100: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='Cuando la suma de los requisitos de capital de una entidad financiera por exposiciones con')
nodo Restriccion_cuando_la_utilizacion_de_los_mecanismos_del_punto_7_9_redunde_en_un_monto_que_ex_7b059c: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='Cuando la utilización de los mecanismos del punto 7.9. redunde en un monto que exceda lo p')
nodo Restriccion_el_bcra_debitara_de_la_cuenta_corriente_de_la_entidad_una_multa_equivalente_al_d_844239: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='El BCRA debitará de la cuenta corriente de la entidad una multa equivalente al doble de la')
nodo Restriccion_el_doble_del_periodo_de_riesgo_de_margen_para_conjuntos_de_neteo_con_disputas_pe_a32c59: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='El doble del período de riesgo de margen para conjuntos de neteo con disputas pendientes. ')
nodo Restriccion_el_importe_de_los_depositos_en_moneda_nacional_y_extranjera_no_podra_exceder_del_06fb84: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='El importe de los depósitos –en moneda nacional y extranjera– no podrá exceder del nivel q')
nodo Restriccion_el_monto_acumulado_de_las_certificaciones_aplicadas_no_supera_el_monto_del_aport_3dadf9: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='el monto acumulado de las certificaciones aplicadas no supera el monto del aporte oportuna')
nodo Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_no_podra_ex_ddef79: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='El monto acumulado de las repatriaciones de capital del no residente no podrá exceder la s')
nodo Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_de_los_nuevos_titulos_en_ningu_3a852e: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='el monto acumulado de los vencimientos de capital de los nuevos títulos en ningún momento,')
nodo Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_en_nin_78f93f: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún moment')
nodo Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_en_nin_a2451c: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='El monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún moment')
nodo Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_en_nin_fa0531: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún moment')
nodo Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_titulo_de_deuda_en_n_a98486: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='El monto acumulado de los vencimientos de capital del nuevo título de deuda en ningún mome')
nodo Restriccion_el_monto_total_abonado_por_concepto_de_utilidades_y_dividendos_a_accionistas_no__24214c: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='El monto total abonado por concepto de utilidades y dividendos a accionistas no residentes')
nodo Restriccion_el_monto_total_abonado_por_este_concepto_a_accionistas_no_residentes_incluido_el_19b1b2: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='El monto total abonado por este concepto a accionistas no residentes, incluido el pago cuy')
nodo Restriccion_en_el_caso_de_una_extraccion_con_una_tarjeta_prepaga_sera_de_aplicacion_el_limit_7282fd: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='En el caso de una extracción con una tarjeta prepaga será de aplicación el límite dispuest')
nodo Restriccion_la_exigencia_de_capital_por_las_posiciones_de_titulizacion_retenidas_o_recomprad_645f26: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='La exigencia de capital por las posiciones de titulización retenidas o recompradas por la ')
nodo Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en__bec264: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7')
nodo Restriccion_la_tasacion_no_resulte_mayor_al_precio_de_mercado__cap_2_9_2_3_db61d6: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='la tasación no resulte mayor al precio de mercado')
nodo Restriccion_la_tasacion_no_sea_mayor_al_precio_de_adquisicion_en_los_casos_en_que_el_prestam_61fcb8: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='la tasación no sea mayor al precio de adquisición en los casos en que el préstamo con gara')
nodo Restriccion_las_operaciones_de_titulizacion_que_incluyan_una_opcion_de_exclusion_que_no_cump_03ec35: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='Las operaciones de titulización que incluyan una opción de exclusión que no cumpla la tota')
nodo Restriccion_los_adelantos_previstos_en_el_punto_3_2_5_de_las_normas_sobre_financiamiento_al__2e7086: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion="Los adelantos previstos en el punto 3.2.5. de las normas sobre 'Financiamiento al sector p")
nodo Restriccion_los_montos_abonados_por_este_mecanismo_en_el_conjunto_de_las_entidades_y_por_el__1748a7: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='Los montos abonados por este mecanismo en el conjunto de las entidades y por el conjunto d')
nodo Restriccion_los_pagos_por_deudas_de_bienes_o_servicios_realizados_en_el_marco_de_los_mecanis_8cf706: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='Los pagos por deudas de bienes o servicios realizados en el marco de los mecanismos previs')
nodo Restriccion_no_podra_excederse_el_nivel_de_depositos_alcanzados_en_el_mes_en_el_que_se_origi_d96af6: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='No podrá excederse el nivel de depósitos alcanzados en el mes en el que se origine el incu')
nodo Restriccion_por_hasta_el_monto_que_surge_de_considerar_el_monto_acumulado_de_los_beneficios__c372cb: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='por hasta el monto que surge de considerar el monto acumulado de los beneficios totales re')
nodo Restriccion_que_el_total_de_los_pagos_realizados_con_imputacion_a_la_oficializacion_de_impor_9fecf6: limite_cuantitativo sin lista de umbrales ni umbral guardado (descripcion='Que el total de los pagos realizados con imputación a la oficialización de importación, in')
```

### S19 — PASS

ERROR — Catálogo de sujetos: todo Sujeto tiene nivel ∈ {clase, instancia, rol, propuesto}; si nivel ≠ propuesto, su id está en el catálogo (clases ∪ roles) del artefacto de --excepciones; si nivel = propuesto, tiene properties.cuarentena y properties.padre_sugerido.

**Resultado:** 134 Sujetos ({'clase': 70, 'instancia': 5, 'propuesto': 24, 'rol': 35}); catálogo de 110 ids; 0 fuera del catálogo, 0 con nivel inválido, 0 propuestos incompletos.

Sin violaciones.

### S20 — PASS

ERROR — Enum de Obligacion.tipo del perfil r2: en la lista o con la marca fuera_de_lista. Lista: {presentacion_informativa|calculo|asignacion|comunicacion_a_cliente|reporte_al_supervisor|otra}.

**Resultado:** 2415 nodos Obligacion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 0.

Sin violaciones.

### S24 — PASS

ERROR — Enum de Restriccion.tipo (bloqueante salvo la marca fuera_de_lista). Lista: {prohibicion|limite_cuantitativo|limite_cualitativo}.

**Resultado:** 805 nodos Restriccion; 0 violaciones; fuera de lista con marca: 4 {'limite_temporal': 3, 'obligacion_cualitativa': 1}; sin valor: 0.

Sin violaciones.

### S25 — PASS

ERROR — Enum de Comunicacion.tipo, con «externa» (bloqueante salvo la marca fuera_de_lista). Lista: {A|B|C|externa}.

**Resultado:** 22 nodos Comunicacion; 0 violaciones; fuera de lista con marca: 6 {'otro': 2, 'referencia': 3, 'TO': 1}; sin valor: 1.

Sin violaciones.

### S26 — PASS

ERROR — Claves cerradas por tipo: las properties de cada nodo de los nueve tipos están en claves_por_tipo de enums_r2.json o en MARCAS_NODO de modelos_r2.py; lo demás vive en properties_no_definidas.

**Resultado:** 8224 nodos evaluados; 0 violaciones {}; marcas de nodo admitidas: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to'].

Sin violaciones.

### S28 — PASS

ERROR — Sujeto propuesto con fila en el registro de no mapeados (bloqueante).

**Resultado:** 24 Sujetos propuestos; 48 filas en el registro; 0 propuestos sin fila.

Sin violaciones.

### S29 — PASS

ERROR — Destino de padre_sugerido en el catálogo único (bloqueante: U-CAT-UNICO está cerrada).

**Resultado:** 24 aristas padre_sugerido; 0 con destino fuera del catálogo único (110 ids).

Sin violaciones.

### S30 — PASS

ERROR — alcance de remite_a en la lista cerrada y coherente con los extremos (bloqueante). Coherencia: to_entero si el destino es un TextoOrdenado (destino <to>::TO); si no, interna cuando el TO de la unidad citada es el de la procedencia de la arista y externa cuando es otro (enmienda 2 de L-ESQ-R2, §3).

**Resultado:** 14000 aristas remite_a ({'externa': 949, 'interna': 13021, 'to_entero': 30}); 0 violaciones.

Sin violaciones.

### S31 — PASS

ERROR — evidencia de remite_a: tramo literal de un único tramo del texto de E0 de su chunk_id (bloqueante; sin --e0, NO COMPUTABLE). Tramo = el texto propio del chunk o uno de sus tramos heredados, cada uno por separado; nunca la concatenación. Si la evidencia no está en el chunk de provenance, se busca en las otras procedencias de la arista (fusión).

**Resultado:** 14000 aristas remite_a: {'en_un_tramo_del_chunk_de_la_arista': 14000}; 0 violaciones.

Sin violaciones.

## Informativas

### S7 — FAIL

ERROR — Unicidad exacta: no puede haber dos nodos con el mismo (type, label normalizado).

**Resultado:** 52 grupos violatorios (113 nodos involucrados).

```
[Condicion] 'abastecimiento del area franca sin reexportacion' (2 nodos):
    - Condicion_abastecimiento_del_area_franca_sin_reexportacion__la_exportacion_al_area_franca__6b1f45  (label: 'Abastecimiento del área franca sin reexportación')
    - Condicion_abastecimiento_del_area_franca_sin_reexportacion__que_las_exportaciones_supongan_a4db4b  (label: 'Abastecimiento del área franca sin reexportación')
[Condicion] 'autorizacion expresa del cliente para debitos' (2 nodos):
    - Condicion_autorizacion_expresa_del_cliente_para_debitos__que_medie_autorizacion_expresa_de_7dcbd4  (label: 'Autorización expresa del cliente para débitos')
    - Condicion_autorizacion_expresa_del_cliente_para_debitos__siempre_que_medie_autorizacion_ex_aaf725  (label: 'Autorización expresa del cliente para débitos')
[Condicion] 'beneficiario regimen fomento economia conocimiento' (2 nodos):
    - Condicion_beneficiario_regimen_fomento_economia_conocimiento__personas_juridicas_que_sean__dd5414  (label: 'Beneficiario régimen fomento economía conocimiento')
    - Condicion_beneficiario_regimen_fomento_economia_conocimiento__personas_juridicas_sean_bene_8a8e34  (label: 'Beneficiario régimen fomento economía conocimiento')
[Condicion] 'cliente beneficiario directo decreto 277/22' (3 nodos):
    - Condicion_cliente_beneficiario_directo_decreto_277_22__cuando_el_cliente_sea_beneficiario__690295  (label: 'Cliente beneficiario directo Decreto 277/22')
    - Condicion_cliente_beneficiario_directo_decreto_277_22__que_el_cliente_sea_beneficiario_dir_527959  (label: 'Cliente beneficiario directo Decreto 277/22')
    - Condicion_cliente_beneficiario_directo_decreto_277_22__que_el_cliente_sea_un_beneficiario__47522b  (label: 'Cliente beneficiario directo Decreto 277/22')
[Condicion] 'cliente cumple requisitos complementarios puntos 3.16.1 a 3.16.4' (2 nodos):
    - Condicion_cliente_cumple_requisitos_complementarios_puntos_3_16_1_a_3_16_4__el_cliente_cum_2b0f5c  (label: 'Cliente cumple requisitos complementarios puntos 3.16.1 a 3.16.4')
    - Condicion_cliente_cumple_requisitos_complementarios_puntos_3_16_1_a_3_16_4__el_cliente_cum_6a9614  (label: 'Cliente cumple requisitos complementarios puntos 3.16.1 a 3.16.4')
[Condicion] 'cliente es vpu adherido al rigi' (3 nodos):
    - Condicion_cliente_es_vpu_adherido_al_rigi__el_cliente_es_un_vehiculo_de_proyecto_unico_vpu_55308d  (label: 'Cliente es VPU adherido al RIGI')
    - Condicion_cliente_es_vpu_adherido_al_rigi__el_cliente_es_un_vehiculo_de_proyecto_unico_vpu_d28181  (label: 'Cliente es VPU adherido al RIGI')
    - Condicion_cliente_es_vpu_adherido_al_rigi__el_cliente_es_un_vehiculo_de_proyecto_unico_vpu_f39248  (label: 'Cliente es VPU adherido al RIGI')
[Condicion] 'cliente no es persona humana residente' (2 nodos):
    - Condicion_cliente_no_es_persona_humana_residente__el_cliente_no_sea_una_persona_humana_res_027ac8  (label: 'Cliente no es persona humana residente')
    - Condicion_cliente_no_es_persona_humana_residente__en_el_caso_de_que_el_cliente_no_sea_una__fa5529  (label: 'Cliente no es persona humana residente')
[Condicion] 'cumplimiento de condiciones especificadas' (2 nodos):
    - Condicion_cumplimiento_de_condiciones_especificadas__cuando_se_reunan_las_condiciones_espe_638264  (label: 'Cumplimiento de condiciones especificadas')
    - Condicion_cumplimiento_de_condiciones_especificadas__la_aplicacion_de_cobros_de_exportacio_efec5a  (label: 'Cumplimiento de condiciones especificadas')
[Condicion] 'cumplimiento de requisitos aplicables' (3 nodos):
    - Condicion_cumplimiento_de_requisitos_aplicables__en_la_medida_que_se_cumplan_los_requisito_29371e  (label: 'Cumplimiento de requisitos aplicables')
    - Condicion_cumplimiento_de_requisitos_aplicables__en_la_medida_que_se_cumplan_los_requisito_72fa2f  (label: 'Cumplimiento de requisitos aplicables')
    - Condicion_cumplimiento_de_requisitos_aplicables__se_cumplan_los_requisitos_aplicables__ext_0f724b  (label: 'Cumplimiento de requisitos aplicables')
[Condicion] 'cumplimiento de requisitos generales' (2 nodos):
    - Condicion_cumplimiento_de_requisitos_generales__en_la_medida_que_se_cumplan_los_requisitos_019837  (label: 'Cumplimiento de requisitos generales')
    - Condicion_cumplimiento_de_requisitos_generales__en_la_medida_que_se_cumplan_los_requisitos_3623b5  (label: 'Cumplimiento de requisitos generales')
[Condicion] 'cumplimiento requisitos punto 7.9' (2 nodos):
    - Condicion_cumplimiento_requisitos_punto_7_9__en_la_medida_que_se_cumplan_los_requisitos_pr_3ceef0  (label: 'Cumplimiento requisitos punto 7.9')
    - Condicion_cumplimiento_requisitos_punto_7_9__se_cumplan_los_requisitos_previstos_en_el_pun_c5bc7b  (label: 'Cumplimiento requisitos punto 7.9')
[Condicion] 'declaracion en relevamiento de activos y pasivos externos' (3 nodos):
    - Condicion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__cuenta_con_constancia_53d537  (label: 'Declaración en Relevamiento de activos y pasivos externos')
    - Condicion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__la_operacion_se_encue_771004  (label: 'Declaración en Relevamiento de activos y pasivos externos')
    - Condicion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__se_encuentra_declarad_fed5b7  (label: 'Declaración en Relevamiento de activos y pasivos externos')
[Condicion] 'fondos percibidos o acreditados en exterior' (2 nodos):
    - Condicion_fondos_percibidos_o_acreditados_en_exterior__cuando_los_fondos_hayan_sido_percib_ecbe6d  (label: 'Fondos percibidos o acreditados en exterior')
    - Condicion_fondos_percibidos_o_acreditados_en_exterior__en_caso_de_fondos_percibidos_o_acre_cd9853  (label: 'Fondos percibidos o acreditados en exterior')
[Condicion] 'ingreso dentro plazos normativos establecidos' (2 nodos):
    - Condicion_ingreso_dentro_plazos_normativos_establecidos__los_cobros_deben_ingresar_dentro__563f82  (label: 'Ingreso dentro plazos normativos establecidos')
    - Condicion_ingreso_dentro_plazos_normativos_establecidos__los_cobros_ingresen_dentro_de_los_d90b19  (label: 'Ingreso dentro plazos normativos establecidos')
[Condicion] 'marco de puntos 3.3, 3.5, 3.6 y 10.3.2' (2 nodos):
    - Condicion_marco_de_puntos_3_3_3_5_3_6_y_10_3_2__en_el_marco_de_lo_dispuesto_en_los_puntos__2b95b4  (label: 'Marco de puntos 3.3, 3.5, 3.6 y 10.3.2')
    - Condicion_marco_de_puntos_3_3_3_5_3_6_y_10_3_2__las_disposiciones_aplican_en_el_marco_de_l_44b319  (label: 'Marco de puntos 3.3, 3.5, 3.6 y 10.3.2')
[Condicion] 'servicios prestados o devengados hasta 12/12/23' (3 nodos):
    - Condicion_servicios_prestados_o_devengados_hasta_12_12_23__que_los_servicios_importados_ha_67dcb3  (label: 'Servicios prestados o devengados hasta 12/12/23')
    - Condicion_servicios_prestados_o_devengados_hasta_12_12_23__servicios_prestados_o_devengado_8351b1  (label: 'Servicios prestados o devengados hasta 12/12/23')
    - Condicion_servicios_prestados_o_devengados_hasta_12_12_23__servicios_prestados_o_devengado_905714  (label: 'Servicios prestados o devengados hasta 12/12/23')
[Condicion] 'verificacion previa de cumplimiento de requisitos' (3 nodos):
    - Condicion_verificacion_previa_de_cumplimiento_de_requisitos__en_la_medida_que_verifique_pr_6a2208  (label: 'Verificación previa de cumplimiento de requisitos')
    - Condicion_verificacion_previa_de_cumplimiento_de_requisitos__en_la_medida_que_verifique_pr_b8c3b0  (label: 'Verificación previa de cumplimiento de requisitos')
    - Condicion_verificacion_previa_de_cumplimiento_de_requisitos__que_se_verifique_previamente__241ea5  (label: 'Verificación previa de cumplimiento de requisitos')
[Condicion] 'vida promedio del nuevo endeudamiento mayor a la remanente' (2 nodos):
    - Condicion_vida_promedio_del_nuevo_endeudamiento_mayor_a_la_remanente__la_vida_promedio_del_94e1db  (label: 'Vida promedio del nuevo endeudamiento mayor a la remanente')
    - Condicion_vida_promedio_del_nuevo_endeudamiento_mayor_a_la_remanente__la_vida_promedio_del_cf2852  (label: 'Vida promedio del nuevo endeudamiento mayor a la remanente')
[Condicion] 'vigencia del requisito de conformidad previa bcra' (2 nodos):
    - Condicion_vigencia_del_requisito_de_conformidad_previa_bcra__en_la_medida_que_se_encuentre_600a66  (label: 'Vigencia del requisito de conformidad previa BCRA')
    - Condicion_vigencia_del_requisito_de_conformidad_previa_bcra__en_la_medida_que_se_encuentre_aa6b6c  (label: 'Vigencia del requisito de conformidad previa BCRA')
[Definicion] 'empresas con grado de inversion' (2 nodos):
    - Definicion_empresas_con_grado_de_inversion__aquellas_con_capacidad_suficiente_para_atender__816f31  (label: 'Empresas con grado de inversión')
    - Definicion_empresas_con_grado_de_inversion__empresas_con_grado_de_inversion_con_un_ponderad_28cec7  (label: 'Empresas con grado de inversión')
[Definicion] 'fc — componente financiero' (2 nodos):
    - Definicion_fc_componente_financiero__componente_financiero_promediado_sobre_3_periodos_de_1_4deb27  (label: 'FC — componente financiero')
    - Definicion_fc_componente_financiero__componente_financiero_se_determinara_por_la_siguiente__c0b2d9  (label: 'FC — Componente financiero')
[Definicion] 'ildc — componente de intereses, arrendamientos y dividendos' (2 nodos):
    - Definicion_ildc_componente_de_intereses_arrendamientos_y_dividendos__componente_de_interese_b332f1  (label: 'ILDC — Componente de intereses, arrendamientos y dividendos')
    - Definicion_ildc_componente_de_intereses_arrendamientos_y_dividendos__componente_de_interese_c171cc  (label: 'ILDC — componente de intereses, arrendamientos y dividendos')
[Definicion] 'margen de variacion' (2 nodos):
    - Definicion_margen_de_variacion__garantia_efectivamente_constituida_por_un_miembro_compensad_3d155b  (label: 'Margen de variación')
    - Definicion_margen_de_variacion__margen_de_variacion_que_protege_a_las_partes_contratantes_d_877b6a  (label: 'Margen de variación')
[Definicion] 'mpor — periodo de riesgo de margen' (2 nodos):
    - Definicion_mpor_periodo_de_riesgo_de_margen__lapso_entre_el_ultimo_intercambio_de_garantias_d9b51c  (label: 'MPOR — Período de riesgo de margen')
    - Definicion_mpor_periodo_de_riesgo_de_margen__periodo_de_riesgo_de_margen_correspondiente_al_dcddf4  (label: 'MPOR — período de riesgo de margen')
[Definicion] 'posicion comprada neta' (2 nodos):
    - Definicion_posicion_comprada_neta__la_posicion_comprada_bruta_menos_la_posicion_vendida_en__aafd84  (label: 'Posición comprada neta')
    - Definicion_posicion_comprada_neta__se_incluye_la_posicion_comprada_neta_es_decir_la_posicio_2173a2  (label: 'Posición comprada neta')
[Definicion] 'rm — resultado monetario total' (2 nodos):
    - Definicion_rm_resultado_monetario_total__resultado_monetario_total__cap_7_1_1_a8dd67  (label: 'RM — Resultado monetario total')
    - Definicion_rm_resultado_monetario_total__resultado_monetario_total_promediado_sobre_3_perio_55e537  (label: 'RM — resultado monetario total')
[Definicion] 'sc — componente de servicios' (2 nodos):
    - Definicion_sc_componente_de_servicios__componente_de_servicios_promediado_sobre_3_periodos__d7cf36  (label: 'SC — componente de servicios')
    - Definicion_sc_componente_de_servicios__componente_de_servicios_se_determinara_por_la_siguie_2dbe79  (label: 'SC — Componente de servicios')
[Definicion] 'va — valor absoluto' (2 nodos):
    - Definicion_va_valor_absoluto__valor_absoluto__cap_5_3_2_5_414837  (label: 'VA — valor absoluto')
    - Definicion_va_valor_absoluto__valor_absoluto__cap_7_1_1_d7fee6  (label: 'VA — Valor absoluto')
[Definicion] 'vpu adherido al rigi' (2 nodos):
    - Definicion_vpu_adherido_al_rigi__vehiculo_de_proyecto_unico_vpu_adherido_al_regimen_de_ince_7bb7b8  (label: 'VPU adherido al RIGI')
    - Definicion_vpu_adherido_al_rigi__vehiculo_de_proyecto_unico_vpu_adherido_al_regimen_de_ince_d20627  (label: 'VPU adherido al RIGI')
[Obligacion] 'acreditar comisiones en cuenta corriente' (2 nodos):
    - Obligacion_acreditar_en_la_cuenta_corriente_de_la_entidad_participante_las_comisiones_recon_3b3366  (label: 'Acreditar comisiones en cuenta corriente')
    - Obligacion_el_bcra_procedera_a_acreditar_en_la_cuenta_corriente_de_la_entidad_participante__2dcceb  (label: 'Acreditar comisiones en cuenta corriente')
[Obligacion] 'confeccionar boletos de cambio a nombre propio' (3 nodos):
    - Obligacion_las_entidades_deberan_confeccionar_boletos_de_cambio_a_nombre_propio_cuando_corr_b1fb4c  (label: 'Confeccionar boletos de cambio a nombre propio')
    - Obligacion_las_entidades_deberan_confeccionar_boletos_de_cambio_a_nombre_propio_cuando_las__942216  (label: 'Confeccionar boletos de cambio a nombre propio')
    - Obligacion_las_entidades_deberan_confeccionar_boletos_de_cambio_a_nombre_propio_cuando_las__e49ec9  (label: 'Confeccionar boletos de cambio a nombre propio')
[Obligacion] 'conformidad previa bcra — acceso mercado cambios' (2 nodos):
    - Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_188b2b  (label: 'Conformidad previa BCRA — acceso mercado cambios')
    - Obligacion_se_requerira_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_a3d274  (label: 'Conformidad previa BCRA — acceso mercado cambios')
[Obligacion] 'conformidad previa del bcra requerida' (3 nodos):
    - Obligacion_los_deudores_de_capital_e_intereses_vencidos_con_contrapartes_vinculadas_estan_s_beedd2  (label: 'Conformidad previa del BCRA requerida')
    - Obligacion_quedan_sujetos_a_la_conformidad_previa_del_bcra__ext_13_1_e18f64  (label: 'Conformidad previa del BCRA requerida')
    - Obligacion_se_requerira_la_conformidad_previa_del_bcra_en_caso_de_tratarse_de_prefinanciaci_8ec494  (label: 'Conformidad previa del BCRA requerida')
[Obligacion] 'conservar documentacion respaldatoria' (2 nodos):
    - Obligacion_conservar_la_documentacion_respaldatoria_a_fin_de_dar_de_baja_o_modificar_el_per_340eb4  (label: 'Conservar documentación respaldatoria')
    - Obligacion_debera_obrar_en_poder_del_sujeto_obligado_la_documentacion_respaldatoria_de_las__61ce77  (label: 'Conservar documentación respaldatoria')
[Obligacion] 'convalidacion operacion en sistema online bcra' (2 nodos):
    - Obligacion_en_todos_los_casos_la_entidad_debera_al_momento_de_dar_acceso_al_mercado_de_camb_b1a088  (label: 'Convalidación operación en sistema online BCRA')
    - Obligacion_la_entidad_debera_al_momento_de_dar_acceso_al_mercado_de_cambios_contar_con_la_c_e44563  (label: 'Convalidación operación en sistema online BCRA')
[Obligacion] 'cumplimentar requerimientos de informacion del bcra' (2 nodos):
    - Obligacion_cumplimentar_los_requerimientos_de_informacion_que_establezca_el_bcra_respecto_a_a6b079  (label: 'Cumplimentar requerimientos de información del BCRA')
    - Obligacion_cumplimentar_los_requerimientos_de_informacion_que_establezca_el_bcra_respecto_a_b5bd16  (label: 'Cumplimentar requerimientos de información del BCRA')
[Obligacion] 'debitar penalidades de cuenta corriente' (2 nodos):
    - Obligacion_debitar_de_la_cuenta_corriente_de_la_entidad_participante_las_penalidades_previs_6b1c45  (label: 'Debitar penalidades de cuenta corriente')
    - Obligacion_debitar_de_la_cuenta_corriente_de_la_entidad_participante_las_penalidades_previs_f9f5a7  (label: 'Debitar penalidades de cuenta corriente')
[Obligacion] 'intervencion de documentacion aduanera' (2 nodos):
    - Obligacion_la_entidad_interviniente_debera_intervenir_la_documentacion_aduanera_por_los_pag_424eeb  (label: 'Intervención de documentación aduanera')
    - Obligacion_la_entidad_tambien_debera_realizar_la_correspondiente_intervencion_de_la_documen_1ef938  (label: 'Intervención de documentación aduanera')
[Obligacion] 'ratificar personalmente denuncia en sucursal' (2 nodos):
    - Obligacion_ratificar_personalmente_en_el_dia_la_denuncia_en_cualquier_sucursal_de_la_entida_51c9be  (label: 'Ratificar personalmente denuncia en sucursal')
    - Obligacion_ratificar_personalmente_en_el_dia_la_denuncia_en_cualquier_sucursal_de_la_entida_ad56c2  (label: 'Ratificar personalmente denuncia en sucursal')
[Obligacion] 'realizar boleto de venta de cambio' (3 nodos):
    - Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_de_la_empresa_q_42b2a0  (label: 'Realizar boleto de venta de cambio')
    - Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_cliente_por_f44a3a  (label: 'Realizar boleto de venta de cambio')
    - Obligacion_la_mencionada_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del__283b1a  (label: 'Realizar boleto de venta de cambio')
[Obligacion] 'tratamiento general para posteriores refinanciaciones' (2 nodos):
    - Obligacion_para_las_posteriores_refinanciaciones_recibiran_el_tratamiento_general_previsto__3e7064  (label: 'Tratamiento general para posteriores refinanciaciones')
    - Obligacion_para_las_posteriores_refinanciaciones_recibiran_el_tratamiento_general_previsto__956ed2  (label: 'Tratamiento general para posteriores refinanciaciones')
[Obligacion] 'verificacion de cumplimiento de condiciones' (2 nodos):
    - Obligacion_la_entidad_encargada_del_seguimiento_debera_verificar_el_cumplimiento_de_las_sig_14a4b6  (label: 'Verificación de cumplimiento de condiciones')
    - Obligacion_la_entidad_responsable_debera_verificar_el_cumplimiento_de_las_condiciones_estip_285ee7  (label: 'Verificación de cumplimiento de condiciones')
[Operacion] 'financiacion a importadores del exterior' (2 nodos):
    - Operacion_financiacion_a_importadores_del_exterior_e50e77  (label: 'Financiación a importadores del exterior')
    - Operacion_financiacion_a_importadores_del_exterior_e50e77__polcre  (label: 'Financiación a importadores del exterior')
[Operacion] 'financiaciones a clientes agricolas no mipyme' (2 nodos):
    - Operacion_financiaciones_a_clientes_agricolas_no_mipyme_5faf23  (label: 'Financiaciones a clientes agrícolas no MiPyME')
    - Operacion_financiaciones_a_clientes_agricolas_no_mipyme_5faf23__cap  (label: 'Financiaciones a clientes agrícolas no MiPyME')
[Operacion] 'presentacion de declaracion jurada' (2 nodos):
    - Operacion_presentacion_de_declaracion_jurada_3380c7  (label: 'Presentación de declaración jurada')
    - Operacion_presentacion_de_declaracion_jurada_3380c7__pagjub  (label: 'Presentación de declaración jurada')
[Potestad] 'acceso al mercado de cambios — residentes con endeudamientos' (2 nodos):
    - Potestad_acceso_al_mercado_de_cambios_residentes_con_endeudamientos__las_entidades_podran_32398c  (label: 'Acceso al mercado de cambios — residentes con endeudamientos')
    - Potestad_acceso_al_mercado_de_cambios_residentes_con_endeudamientos__las_entidades_podran_dc033c  (label: 'Acceso al mercado de cambios — residentes con endeudamientos')
[Potestad] 'facultad de dar acceso al mercado de cambios' (2 nodos):
    - Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__las_entidades_podran_dar_acceso_al_1dccc4  (label: 'Facultad de dar acceso al mercado de cambios')
    - Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__las_entidades_podran_dar_acceso_al_446f8f  (label: 'Facultad de dar acceso al mercado de cambios')
[Potestad] 'solicitar ampliacion plazo liquidacion divisas' (2 nodos):
    - Potestad_solicitar_ampliacion_plazo_liquidacion_divisas__el_exportador_podra_solicitar_a__e89a3a  (label: 'Solicitar ampliación plazo liquidación divisas')
    - Potestad_solicitar_ampliacion_plazo_liquidacion_divisas__el_exportador_podra_solicitar_qu_d5f02a  (label: 'Solicitar ampliación plazo liquidación divisas')
[Restriccion] 'falta de especificacion — carencia de valor como cheque' (2 nodos):
    - Restriccion_el_titulo_respecto_del_que_falta_la_orden_pura_y_simple_de_pagar_una_suma_determ_bd5651  (label: 'Falta de especificación — carencia de valor como cheque')
    - Restriccion_el_titulo_respecto_del_que_falte_la_especificacion_de_la_fecha_de_pago_segun_art_a9876c  (label: 'Falta de especificación — carencia de valor como cheque')
[Restriccion] 'permanencia minima 180 dias con credito adicional' (2 nodos):
    - Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_categoria_haya_refinanciado_su_d_9b4b78  (label: 'Permanencia mínima 180 días con crédito adicional')
    - Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_categoria_haya_refinanciado_su_d_ed4225  (label: 'Permanencia mínima 180 días con crédito adicional')
[Restriccion] 'ponderador 150% — deuda subordinada' (2 nodos):
    - Restriccion_exposiciones_a_deuda_subordinada_ponderador_de_riesgo_del_150__cap_2_12_10_2_533e48  (label: 'Ponderador 150% — Deuda subordinada')
    - Restriccion_ponderador_de_riesgo_del_150_para_deuda_subordinada_e_instrumentos_de_capital_qu_0a3a8c  (label: 'Ponderador 150% — deuda subordinada')
[Restriccion] 'prohibicion de nuevas presentaciones — titulos rechazados' (2 nodos):
    - Restriccion_los_titulos_devueltos_por_falta_de_especificaciones_incluida_la_falta_de_numero__38cd57  (label: 'Prohibición de nuevas presentaciones — títulos rechazados')
    - Restriccion_los_titulos_devueltos_por_falta_de_especificaciones_no_podran_ser_objeto_de_nuev_3833af  (label: 'Prohibición de nuevas presentaciones — títulos rechazados')
```

### S8 — WARN

WARN — Colisión de label normalizado entre types distintos.

**Resultado:** 34 grupos con el mismo label normalizado en types distintos.

```
'acceso al mercado de cambios' (2 nodos):
    - [Condicion] Condicion_acceso_al_mercado_de_cambios__se_cumplen_las_condiciones_previstas_en_el_punto_1_8d8ef1
    - [Operacion] Operacion_acceso_al_mercado_de_cambios_b8c486
'acceso al mercado de cambios para pagos de servicios de no residentes' (2 nodos):
    - [Operacion] Operacion_acceso_al_mercado_de_cambios_para_pagos_de_servicios_de_no_residentes_279ff0
    - [Potestad] Potestad_acceso_al_mercado_de_cambios_para_pagos_de_servicios_de_no_residentes__las_entid_4ca7e6
'alta gerencia' (2 nodos):
    - [Definicion] Definicion_alta_gerencia__gerencia_general_y_gerentes_que_tengan_poder_decisorio_y_dependan_3aa73e
    - [Sujeto] Sujeto_alta_gerencia
'anticipo de exportaciones de bienes liquidado' (2 nodos):
    - [Definicion] Definicion_anticipo_de_exportaciones_de_bienes_liquidado__adelanto_en_divisas_efectuado_a_n_ae152e
    - [Operacion] Operacion_anticipo_de_exportaciones_de_bienes_liquidado_d62044
'anticipo de fondos propios del exterior' (2 nodos):
    - [Condicion] Condicion_anticipo_de_fondos_propios_del_exterior__cuando_los_exportadores_anticipen_fondo_2e9403
    - [Operacion] Operacion_anticipo_de_fondos_propios_del_exterior_f7e482
'autoaseguramiento riesgos fallecimiento invalidez' (2 nodos):
    - [Operacion] Operacion_autoaseguramiento_riesgos_fallecimiento_invalidez_f87002
    - [Potestad] Potestad_autoaseguramiento_riesgos_fallecimiento_invalidez__alternativamente_podran_autoa_873e27
'cancelacion de capital/intereses con divisas' (2 nodos):
    - [Condicion] Condicion_cancelacion_de_capital_intereses_con_divisas__aplicacion_de_divisas_a_la_cancela_39bf57
    - [Operacion] Operacion_cancelacion_de_capital_intereses_con_divisas_28e145
'clasificacion de deudores' (2 nodos):
    - [Operacion] Operacion_clasificacion_de_deudores_82042f
    - [TextoOrdenado] TextoOrdenado_to_clasificacion_deudores_actual_pdf
'clasificacion de deudores segun mora' (2 nodos):
    - [Obligacion] Obligacion_las_empresas_no_financieras_emisoras_de_tarjetas_de_credito_y_o_compra_y_los_otr_07405c
    - [Operacion] Operacion_clasificacion_de_deudores_segun_mora_595d13
'clasificacion en irrecuperable por falta de evaluacion' (2 nodos):
    - [Obligacion] Obligacion_correspondera_clasificar_en_la_categoria_de_irrecuperable_a_los_clientes_que_cua_6b04ad
    - [Restriccion] Restriccion_los_clientes_se_clasificaran_en_categoria_irrecuperable_en_caso_de_no_efectuarse_f3d7ec
'clientes' (2 nodos):
    - [Definicion] Definicion_clientes__personas_humanas_o_juridicas_y_los_patrimonios_y_otras_universalidades_6b3a3a
    - [Sujeto] Sujeto_cliente
'comunicacion fehaciente de certificaciones emitidas' (2 nodos):
    - [Condicion] Condicion_comunicacion_fehaciente_de_certificaciones_emitidas__la_entidad_cedente_ha_comun_df1db3
    - [Operacion] Operacion_comunicacion_fehaciente_de_certificaciones_emitidas_9294e5
'confeccion dos boletos sin movimiento pesos' (2 nodos):
    - [Condicion] Condicion_confeccion_dos_boletos_sin_movimiento_pesos__a_los_efectos_del_registro_de_estas_49f765
    - [Obligacion] Obligacion_a_los_efectos_del_registro_de_estas_operaciones_se_deberan_confeccionar_dos_bole_7ee0ad
'conformidad previa bcra — acceso mercado de cambios' (2 nodos):
    - [Obligacion] Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_522d8e
    - [Restriccion] Restriccion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_d1ce15
'conformidad previa del bcra' (2 nodos):
    - [Condicion] Condicion_conformidad_previa_del_bcra__se_cuente_con_la_conformidad_previa_del_bcra__ext_9_459513
    - [Obligacion] Obligacion_se_requerira_la_conformidad_previa_del_bcra__ext_10_4_2_8_677de9
'declaracion en relevamiento de activos y pasivos externos' (4 nodos):
    - [Condicion] Condicion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__cuenta_con_constancia_53d537
    - [Condicion] Condicion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__la_operacion_se_encue_771004
    - [Condicion] Condicion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__se_encuentra_declarad_fed5b7
    - [Obligacion] Obligacion_la_operacion_se_encuentra_declarada_en_caso_de_corresponder_en_la_ultima_present_c19348
'emision de certificaciones de aplicacion' (2 nodos):
    - [Operacion] Operacion_emision_de_certificaciones_de_aplicacion_bf0334
    - [Potestad] Potestad_emision_de_certificaciones_de_aplicacion__la_entidad_podra_emitir_las_certificac_96dd42
'exposiciones en situacion de incumplimiento' (2 nodos):
    - [Definicion] Definicion_exposiciones_en_situacion_de_incumplimiento__comprende_a_todas_aquellas_exposici_0cd2eb
    - [Operacion] Operacion_exposiciones_en_situacion_de_incumplimiento_104f61
'extension plazo ingreso liquidacion divisas' (2 nodos):
    - [Operacion] Operacion_extension_plazo_ingreso_liquidacion_divisas_d523f1
    - [Potestad] Potestad_extension_plazo_ingreso_liquidacion_divisas__la_entidad_encargada_del_seguimient_c19729
'financiacion especializada grandes proyectos infraestructura' (2 nodos):
    - [Definicion] Definicion_financiacion_especializada_grandes_proyectos_infraestructura__aquella_en_la_que__8ee414
    - [Operacion] Operacion_financiacion_especializada_grandes_proyectos_infraestructura_91c15f
'gobiernos locales' (2 nodos):
    - [Definicion] Definicion_gobiernos_locales__comprende_a_la_administracion_central_de_provincias_de_la_ciu_de933d
    - [Sujeto] Sujeto_gobierno_local
'ingreso y liquidacion de divisas por exportacion' (2 nodos):
    - [Obligacion] Obligacion_ambas_partes_documentante_y_propietario_de_la_mercaderia_son_responsables_del_cu_3aa260
    - [Operacion] Operacion_ingreso_y_liquidacion_de_divisas_por_exportacion_6e62aa
'nuevos aportes de inversion directa de no residentes' (2 nodos):
    - [Condicion] Condicion_nuevos_aportes_de_inversion_directa_de_no_residentes__que_la_liquidacion_sea_equ_66f65c
    - [Operacion] Operacion_nuevos_aportes_de_inversion_directa_de_no_residentes_3fcab3
'opciones sobre acciones' (2 nodos):
    - [Condicion] Condicion_opciones_sobre_acciones__en_el_caso_de_las_opciones_sobre_acciones_cada_mercado__df1ca4
    - [Operacion] Operacion_opciones_sobre_acciones_30e016
'operacion propia alcanzada por obligacion de ingreso y liquidacion' (2 nodos):
    - [Condicion] Condicion_operacion_propia_alcanzada_por_obligacion_de_ingreso_y_liquidacion__cuando_una_o_1ceab4
    - [Operacion] Operacion_operacion_propia_alcanzada_por_obligacion_de_ingreso_y_liquidacion_58449b
'pago a la vista de cheques' (2 nodos):
    - [Obligacion] Obligacion_pagar_a_la_vista_excepto_en_los_casos_a_que_se_refiere_el_punto_1_5_2_8_segundo__ee7488
    - [Operacion] Operacion_pago_a_la_vista_de_cheques_994ac8
'pago de beneficios anses' (2 nodos):
    - [Operacion] Operacion_pago_de_beneficios_anses_5e43b5
    - [TextoOrdenado] TextoOrdenado_pagjub_pdf
'posicion general de cambios (pgc)' (2 nodos):
    - [Definicion] Definicion_posicion_general_de_cambios_pgc__comprendera_la_totalidad_de_los_activos_externo_0fafc9
    - [Operacion] Operacion_posicion_general_de_cambios_pgc_4fc69a
'presentacion de documento de viaje mercosur' (2 nodos):
    - [Obligacion] Obligacion_documento_de_viaje_admitido_por_la_decision_mercosur_en_vigencia__docvig_2_1_1_1_d019c6
    - [Operacion] Operacion_presentacion_de_documento_de_viaje_mercosur_be2ab6
'reclasificacion al nivel inmediato superior' (2 nodos):
    - [Obligacion] Obligacion_los_clientes_cuyas_deudas_hayan_sido_refinanciadas_mediante_obligaciones_de_pago_43449c
    - [Operacion] Operacion_reclasificacion_al_nivel_inmediato_superior_052195
'reconocimiento cobertura riesgo credito' (2 nodos):
    - [Obligacion] Obligacion_a_los_efectos_del_reconocimiento_de_la_cobertura_del_riesgo_de_credito_se_tendra_941ede
    - [Operacion] Operacion_reconocimiento_cobertura_riesgo_credito_69e3dd
'reconocimiento de intereses sobre saldos acreedores' (2 nodos):
    - [Operacion] Operacion_reconocimiento_de_intereses_sobre_saldos_acreedores_ecab11
    - [Potestad] Potestad_reconocimiento_de_intereses_sobre_saldos_acreedores__podran_reconocerse_sobre_lo_580205
'titulizacion tradicional' (2 nodos):
    - [Definicion] Definicion_titulizacion_tradicional__es_una_estructura_en_la_que_se_utilizan_los_flujos_de__6d32d3
    - [Operacion] Operacion_titulizacion_tradicional_6f56d4
'vida promedio minima de 1 ano' (2 nodos):
    - [Condicion] Condicion_vida_promedio_minima_de_1_ano__en_la_medida_que_su_vida_promedio_no_sea_inferior_407db7
    - [Restriccion] Restriccion_su_vida_promedio_sea_no_inferior_a_1_un_ano_considerando_los_vencimientos_de_cap_0b95c5
```

### S9 — PASS

ERROR — Descripción canónica: ningún nodo tiene a la vez 'descripcion' y 'description'.

**Resultado:** 0 nodos con ambas keys.

```
Tabla por type (usa cada key / ambas / ninguna):
  Comunicacion: descripcion=0, description=0, ambas=0, ninguna=22 (total 22)
  Condicion: descripcion=1409, description=0, ambas=0, ninguna=0 (total 1409)
  Definicion: descripcion=631, description=0, ambas=0, ninguna=0 (total 631)
  Excepcion: descripcion=411, description=0, ambas=0, ninguna=0 (total 411)
  Obligacion: descripcion=2415, description=0, ambas=0, ninguna=0 (total 2415)
  Operacion: descripcion=2047, description=0, ambas=0, ninguna=0 (total 2047)
  Potestad: descripcion=474, description=0, ambas=0, ninguna=0 (total 474)
  Restriccion: descripcion=805, description=0, ambas=0, ninguna=0 (total 805)
  Sujeto: descripcion=0, description=0, ambas=0, ninguna=134 (total 134)
  TextoOrdenado: descripcion=0, description=0, ambas=0, ninguna=10 (total 10)

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

**Resultado:** Sin aplica_a: Excepcion=289, Obligacion=231, Operacion=1506, Potestad=98, Restriccion=207 (total 2331).

```
Excepcion: 289 sin aplica_a
    - Excepcion_a_esos_efectos_no_se_considerara_refinanciacion_la_asistencia_que_se_otorgue_a_l_d58e0e
    - Excepcion_a_excepcion_de_las_opciones_sobre_acciones_e_indices_bursatiles_que_se_tratan_en_15f11f
    - Excepcion_a_excepcion_de_los_casos_en_que_la_falta_de_pago_del_importador_se_origine_en_un_d22094
    - Excepcion_a_fin_de_ser_excluidas_de_la_central_de_cheques_rechazados_y_o_de_la_central_de__28499b
    - Excepcion_aplicacion_de_exigencia_adicional_de_2_puede_extenderse_a_posiciones_opuestas_en_75792d
    - Excepcion_aquellos_productos_que_no_contengan_soja_estan_exceptuados_de_la_posicion_arance_61ba81
    - Excepcion_asistencia_crediticia_concedida_a_traves_de_las_sucursales_o_subsidiarias_en_el__4bbc86
    - Excepcion_bancos_u_otras_instituciones_financieras_del_exterior_sujetos_a_supervision_sobr_40b084
    - Excepcion_casa_matriz_de_las_sucursales_locales_de_bancos_del_exterior_o_sus_filiales_y_su_9cfe9d
    - Excepcion_cheques_librados_a_favor_de_los_titulares_de_las_cuentas_sobre_las_que_se_giren__4ade64
    - Excepcion_con_excepcion_de_los_casos_contemplados_en_el_punto_4_1__cap_2_12_14_0199cf
    - Excepcion_con_la_expresa_autorizacion_del_titular_de_la_cuenta_corriente_se_libera_la_obli_979152
    - Excepcion_cuando_al_menos_se_haya_cumplido_con_el_pago_sin_haber_incurrido_en_atrasos_supe_0c91be
    - Excepcion_cuando_el_cliente_sea_un_vehiculo_de_proyecto_unico_adherido_al_rigi_que_haya_de_ca4d6b
    - Excepcion_cuando_el_cliente_sea_un_vpu_adherido_al_rigi_que_cumple_con_la_declaracion_de_i_63ccad
    - Excepcion_cuando_el_cva_no_sea_aplicable_tampoco_lo_sera_el_factor_de_1_5__cap_3_2_1_2_2514ef
    - Excepcion_cuando_el_cva_no_sea_aplicable_tampoco_lo_sera_el_factor_de_1_5_tal_es_el_caso_d_8341dc
    - Excepcion_cuando_la_entidad_emplee_para_la_gestion_de_dichas_posiciones_el_valor_actual_ne_2af5c8
    - Excepcion_cuando_las_cuentas_esten_abiertas_a_nombre_de_personas_juridicas_podra_establece_5e0c64
    - Excepcion_cuando_los_adelantos_superen_el_limite_autorizado_y_o_no_sean_cancelados_en_los__28b441
    - Excepcion_cuando_no_corresponda_evaluar_la_capacidad_de_repago_del_deudor_por_encontrarse__8dc813
    - Excepcion_cuando_no_sea_exigible_la_inscripcion_en_el_registro_publico_de_comercio_por_no__7d3fb1
    - Excepcion_cuando_se_trate_de_modificaciones_en_los_valores_de_comisiones_y_o_cargos_debida_307309
    - Excepcion_cuando_una_entidad_financiera_compre_proteccion_crediticia_a_traves_de_un_swap_d_4047f7
    - Excepcion_de_existir_prueba_en_contrario_del_pais_de_domicilio_aplicara_el_punto_2_1_2__do_88c562
    - Excepcion_dicho_pago_no_exime_a_la_entidad_de_las_responsabilidades_civiles_que_pudieren_c_b89534
    - Excepcion_dichos_recaudos_se_consideraran_cumplidos_en_los_casos_en_que_la_gestion_de_pres_5a7857
    - Excepcion_el_acceso_al_mercado_de_cambios_antes_de_lo_indicado_no_requerira_conformidad_pr_4045c8
    - Excepcion_el_acceso_tambien_podra_ser_dado_a_los_fideicomisos_constituidos_en_el_pais_para_d870c5
    - Excepcion_el_bcra_establezca_que_se_debe_hacer_una_reduccion_generalizada_del_valor_si_pos_d67fe0
    - Excepcion_el_cliente_puede_demostrar_que_no_puede_cancelar_de_dicha_forma_por_causas_ajena_05ca45
    - Excepcion_el_importe_resultante_luego_de_realizar_el_ajuste_por_volatilidad_sera_inferior__553081
    - Excepcion_el_importe_resultante_luego_de_realizar_el_ajuste_por_volatilidad_sera_superior__b46a5c
    - Excepcion_el_limite_del_40_no_aplica_cuando_el_deudor_contaba_con_una_certificacion_de_aum_f1f59a
    - Excepcion_el_limite_del_40_no_aplica_cuando_el_deudor_contaba_con_una_certificacion_por_lo_5554b8
    - Excepcion_el_limite_del_40_no_aplica_cuando_por_un_monto_igual_o_superior_al_excedente_el__17647d
    - Excepcion_el_limite_del_40_no_aplica_cuando_por_un_monto_igual_o_superior_al_excedente_el__dc9af8
    - Excepcion_el_limite_se_incrementa_a_usd_200_dolares_estadounidenses_doscientos_por_operaci_3cf84c
    - Excepcion_el_maiz_pisingallo_esta_exceptuado_de_la_posicion_arancelaria_1005_90_10__ext_7__9682b2
    - Excepcion_el_plazo_no_resulta_aplicable_a_las_ventas_que_se_realicen_con_liquidacion_contr_d08314
    - Excepcion_el_plazo_para_realizar_la_denuncia_se_contara_a_partir_de_la_fecha_en_que_tomo_c_b25cbb
    - Excepcion_el_punto_3_16_3_solo_sera_aplicable_para_clientes_que_no_sean_personas_humanas_r_0fbf79
    - Excepcion_el_punto_3_16_3_solo_sera_aplicable_para_clientes_que_no_sean_personas_humanas_r_9e21f3
    - Excepcion_el_rechazo_por_la_causal_de_presentacion_anterior_a_fecha_de_pago_no_impide_una__614cf8
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_resultara_aplicable_cuando_el_pag_d1792a
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_54512c
    - Excepcion_el_requisito_no_se_aplicara_a_las_financiaciones_a_personas_humanas_que_esten_ga_08f050
    - Excepcion_el_requisito_no_se_aplicara_a_los_inmuebles_rurales__cap_2_9_2_2_c7b934
    - Excepcion_ello_independientemente_de_las_comisiones_y_o_cargos_que_correspondan_por_la_ges_99f22b
    - Excepcion_ello_salvo_que_por_aplicacion_de_otras_pautas_corresponda_categorizarlo_en_el_ni_fe4de9
    - Excepcion_en_caso_de_no_disponer_de_la_documentacion_de_capitalizacion_el_cliente_debera_p_02c7de
    - Excepcion_en_caso_de_no_disponer_de_la_documentacion_que_avale_la_capitalizacion_definitiv_b119c3
    - Excepcion_en_caso_de_no_efectuarse_la_evaluacion_cualquiera_sea_el_motivo_estos_clientes_s_4567df
    - Excepcion_en_caso_de_no_existir_dicha_jerarquia_la_pertinente_presentacion_estara_a_cargo__7d9c2d
    - Excepcion_en_caso_de_que_alguna_de_las_personas_detallada_en_el_punto_3_16_3_3_sea_un_ente_bca387
    - Excepcion_en_caso_de_que_el_trimestre_de_referencia_sea_el_cuarto_de_2022_del_monto_dispon_fdcb70
    - Excepcion_en_caso_de_que_la_operacion_haya_sido_liquidada_por_mas_de_una_entidad_cada_una__82eb29
    - Excepcion_en_caso_de_quiebra_o_liquidacion__cap_8_3_3_6_eb1900
    - Excepcion_en_casos_de_datos_provenientes_de_liquidaciones_forzadas_ventas_criticas_o_merca_41c356
    - Excepcion_en_el_caso_de_operaciones_comprendidas_en_el_punto_7_11_1_6_tambien_se_admitira__8bacc5
    - Excepcion_en_el_caso_de_operaciones_fuera_del_horario_de_atencion_de_las_entidades_financi_7d339e
    - Excepcion_en_el_supuesto_de_adulteracion_el_rechazo_del_cheque_no_se_comunicara_cuando_exi_d7b80d
    - Excepcion_en_la_medida_en_que_la_seleccion_no_sea_discrecional_la_incorporacion_de_credito_f18918
    - Excepcion_en_los_casos_de_deudores_por_servicios_publicos_o_por_tarjetas_de_credito_no_ser_bdf5ac
    - Excepcion_es_optativo_cuando_el_saldo_de_deuda_sea_inferior_al_monto_establecido_en_el_pun_43b84c
    - Excepcion_estan_exceptuados_de_la_exigencia_de_presentacion_de_declaracion_jurada_los_deud_a69451
    - Excepcion_estan_exceptuados_los_inmuebles_adquiridos_mediante_subasta_judicial_del_requisi_e6a68f
    - Excepcion_este_requisito_complementario_no_resultara_aplicable_cuando_el_acceso_al_mercado_d78b8a
    - Excepcion_este_requisito_no_resultara_aplicable_cuando_el_cliente_sea_un_vehiculo_de_proye_2eddd8
    - Excepcion_este_requisito_no_resultara_aplicable_cuando_la_operacion_encuadre_en_alguna_de__792c96
    - Excepcion_este_requisito_no_resultara_aplicable_cuando_la_operacion_encuadre_en_alguna_de__c7629f
    - Excepcion_este_requisito_no_resultara_aplicable_cuando_la_operacion_encuadre_en_alguna_de__e5c528
    - Excepcion_este_requisito_no_resultara_aplicable_cuando_se_cumpla_la_totalidad_de_las_sigui_18df73
    - Excepcion_este_requisito_no_resultara_aplicable_si_el_cliente_es_un_vehiculo_de_proyecto_u_86ed3d
    - Excepcion_este_requisito_no_sera_de_aplicacion_para_el_sector_publico__ext_10_4_2_6_bea64a
    - Excepcion_este_requisito_no_sera_de_aplicacion_para_las_personas_juridicas_que_tengan_a_su_90b061
    - Excepcion_este_requisito_no_sera_de_aplicacion_para_los_fideicomisos_constituidos_con_apor_06d633
    - Excepcion_este_requisito_no_sera_de_aplicacion_para_todas_las_organizaciones_empresariales_6f291a
    - Excepcion_excepcion_de_la_restriccion_cuando_el_registro_o_custodia_se_encuentre_a_cargo_d_f10360
    - Excepcion_excepcion_de_liquidacion_de_cobros_de_exportaciones_de_bienes_y_servicios_para_l_a4c243
    - Excepcion_excepto_cuando_la_entidad_constate_que_el_pago_encuadra_en_alguna_de_las_situaci_ea7059
    - Excepcion_excepto_cuando_la_entidad_lo_obtenga_en_forma_electronica_o_digital_conforme_a_l_4bc806
    - Excepcion_excepto_cuando_la_garantia_cubra_unicamente_el_capital_en_cuyo_caso_se_considera_f27c65
    - Excepcion_excepto_cuando_la_gestion_de_cobro_sea_realizada_por_una_entidad_financiera_no_a_8bcbe6
    - Excepcion_excepto_cuando_se_empleen_boletas_de_deposito__ctacte_2_1_4_47dfcb
    - Excepcion_excepto_en_caso_de_liquidacion_de_la_entidad_cuando_asi_correspondiese__cap_8_3__f00327
    - Excepcion_excepto_en_los_casos_previstos_en_el_segundo_parrafo_del_punto_2_1_2_y_en_los_pu_27d57a
    - Excepcion_excepto_para_aquellos_casos_en_que_expresamente_se_prevea_la_posibilidad_de_que__6042e7
    - Excepcion_excepto_para_la_cancelacion_en_el_pais_a_partir_de_su_vencimiento_de_capital_e_i_fadf10
    - Excepcion_excepto_que_la_repatriacion_se_concrete_a_partir_de_un_canje_y_o_arbitraje_con_l_6bde71
    - Excepcion_excepto_que_se_observe_en_materia_de_comisiones_y_o_cargos_las_mismas_condicione_684de1
    - Excepcion_excepto_que_se_trate_de_asociaciones_mutuales_o_cooperativas__pro_1_1_2_5_830979
    - Excepcion_excepto_que_se_trate_de_las_exposiciones_a_que_se_refieren_los_puntos_2_12_2_2_y_c1fd56
    - Excepcion_excepto_que_se_trate_de_operaciones_contra_cable_que_utilicen_cuentas_de_tercero_b5169c
    - Excepcion_financiaciones_que_cuenten_con_aval_de_banco_del_exterior_que_cumpla_con_lo_prev_5c44d7
    - Excepcion_financiaciones_vinculadas_a_operaciones_de_comercio_exterior__cla_6_5_5_8_978d37
    - Excepcion_financiaciones_vinculadas_a_operaciones_de_compraventa_de_titulos_valores_concer_69c70e
    - Excepcion_garantias_otorgadas_a_favor_del_bcra_y_por_obligaciones_directas_quedan_excluida_75470f
    - Excepcion_haberse_dispuesto_medidas_cautelares_sobre_los_fondos_destinados_para_el_pago_de_52d740
    - Excepcion_incluso_cuando_no_se_cumplan_los_requisitos_establecidos_para_el_acceso_del_clie_8ee7c7
    - Excepcion_insuficiencia_de_fondos_de_no_haberse_dispuesto_la_medida_cautelar_conforme_a_lo_eba857
    - Excepcion_la_cobertura_del_riesgo_de_credito_que_tenga_un_plazo_de_vencimiento_original_in_21fdb8
    - Excepcion_la_conformidad_previa_del_bcra_no_sera_requerida_cuando_se_trate_de_un_endeudami_8a5eff
    - Excepcion_la_conformidad_previa_no_aplica_cuando_adicionalmente_a_los_restantes_requisitos_bbbca6
    - Excepcion_la_constancia_de_aceptacion_por_parte_de_esta_ultima_liberara_a_la_entidad_previ_568e20
    - Excepcion_la_constancia_de_aceptacion_por_parte_de_la_nueva_entidad_libera_a_la_entidad_pr_7057fb
    - Excepcion_la_correspondiente_a_las_sucursales_de_los_bancos_extranjeros_que_debera_remitir_dec3c5
    - Excepcion_la_devolucion_del_documento_no_aplica_cuando_la_entidad_otorgue_su_aval__ctacte__c0ce64
    - Excepcion_la_ead_de_un_conjunto_de_neteo_que_solo_comprende_opciones_vendidas_podra_ser_ce_03e1e0
    - Excepcion_la_exigencia_maxima_de_capital_para_las_entidades_financieras_originantes_previs_39cc2a
    - Excepcion_la_exportacion_a_consumo_de_bienes_que_conforman_el_equipaje_no_acompanado_expor_8d8720
    - Excepcion_la_falta_de_firma_del_librador_no_determina_la_carencia_de_valor_como_cheque_cua_5533b6
    - Excepcion_la_falta_de_recepcion_por_parte_del_librador_o_del_cuentacorrentista_de_los_avis_74c171
    - Excepcion_la_limitacion_del_40_no_aplica_cuando_por_un_monto_igual_o_superior_al_excedente_2ce742
    - Excepcion_la_limitacion_del_40_no_aplica_cuando_por_un_monto_igual_o_superior_al_excedente_490b1a
    - Excepcion_la_limitacion_del_40_no_aplica_cuando_por_un_monto_igual_o_superior_al_excedente_7d78b5
    - Excepcion_la_limitacion_del_40_no_aplica_cuando_por_un_monto_igual_o_superior_al_excedente_a725df
    - Excepcion_la_liquidacion_de_las_divisas_remitidas_a_la_entidad_local_por_la_contraparte_pa_46d35f
    - Excepcion_la_obligacion_no_aplicara_cuando_se_trate_de_modificaciones_en_el_numero_de_docu_87b4ec
    - Excepcion_la_operacion_de_exportacion_a_consumo_con_destinacion_de_importacion_temporaria__e5384e
    - Excepcion_la_parte_de_la_exposicion_cubierta_estara_sujeta_a_un_minimo_del_20_salvo_lo_dis_a6671e
    - Excepcion_la_perdida_de_beneficios_y_o_baja_de_restantes_productos_o_servicios_no_aplica_a_2b8ba9
    - Excepcion_la_permanencia_de_180_dias_no_aplica_cuando_por_aplicacion_de_otras_pautas_corre_93799c
    - Excepcion_la_presencia_de_una_opcion_de_exclusion_no_originara_exigencia_de_capital_alguna_3980a9
    - Excepcion_la_prohibicion_de_instalacion_de_oficinas_de_representacion_en_el_exterior_no_ap_5551c2
    - Excepcion_la_reduccion_en_las_tasas_de_interes_pactadas_no_se_considera_indicador_de_alto__f7d28a
    - Excepcion_las_asistencias_asi_otorgadas_no_seran_consideradas_a_los_fines_a_que_se_refiere_57a4ed
    - Excepcion_las_asistencias_otorgadas_en_las_condiciones_a_que_se_refiere_el_segundo_parrafo_a053a3
    - Excepcion_las_disposiciones_sobre_reintegro_no_aplicaran_en_la_medida_en_que_se_opongan_a__5071fb
    - Excepcion_las_entidades_no_observaran_esta_exigencia_de_capital_cuando_se_trate_de_operaci_8d5936
    - Excepcion_las_exportaciones_correspondientes_a_los_capitulos_26_excepto_las_posiciones_260_3698d9
    - Excepcion_las_exportaciones_embarcadas_dentro_del_ano_de_plazo_quedan_exceptuadas_del_0_ce_e8d1db
    - Excepcion_las_exportaciones_embarcadas_luego_del_plazo_de_1_un_ano_quedan_exceptuadas_del__c4bd2f
    - Excepcion_las_exportaciones_embarcadas_luego_del_plazo_de_2_dos_anos_quedan_exceptuadas_de_30fa91
    - Excepcion_las_exportaciones_embarcadas_luego_del_plazo_de_3_tres_anos_quedan_exceptuadas_d_cc6aaa
    - Excepcion_las_garantias_otorgadas_a_favor_del_banco_central_de_la_republica_argentina_esta_c6705d
    - Excepcion_las_importaciones_realizadas_por_empresas_que_presten_servicios_de_aeronavegacio_7d5e5c
    - Excepcion_las_inversiones_en_acciones_estructuradas_con_el_objeto_de_replicar_la_realidad__9fc561
    - Excepcion_las_liquidaciones_encuadradas_en_la_operatoria_con_titulos_valores_por_cuenta_y__a14a87
    - Excepcion_las_modificaciones_en_el_nombre_y_o_apellido_de_las_personas_fisicas_o_en_otros__4f6ec2
    - Excepcion_las_modificaciones_que_resulten_economicamente_mas_beneficiosas_para_el_usuario__b88772
    - Excepcion_las_operaciones_aduaneras_bajo_regimen_de_muestras_articulos_560_al_565_de_la_le_2b56fd
    - Excepcion_las_operaciones_aduaneras_por_ventajas_aduaneras_u_otras_situaciones_previstas_e_ddf087
    - Excepcion_las_operaciones_aduaneras_que_se_detallan_en_el_punto_8_5_17_estan_exceptuadas_d_32627b
    - Excepcion_las_operaciones_correspondientes_a_regimen_de_franquicia_diplomatica_articulos_5_8653ef
    - Excepcion_las_operaciones_de_financiacion_con_titulos_valores_securities_financing_transac_10078f
    - Excepcion_las_operaciones_seran_consideradas_como_sin_garantia__cap_5_2_2_6_75b7b2
    - Excepcion_las_posiciones_que_esten_compensadas_con_instrumentos_identicos_quedan_exceptuad_971778
    - Excepcion_las_primas_por_opciones_de_compra_y_de_venta_tomadas_estan_excluidas_de_las_fina_1046dd
    - Excepcion_las_siguientes_garantias_otorgadas_por_obligaciones_directas__cla_2_2_2_1_3305df
    - Excepcion_las_ventas_con_liquidacion_en_moneda_extranjera_en_el_exterior_o_las_transferenc_12e83f
    - Excepcion_las_ventas_con_liquidacion_en_moneda_extranjera_en_el_pais_o_en_el_exterior_de_l_ed92e4
    - Excepcion_lo_previsto_en_este_parrafo_no_sera_de_aplicacion_cuando_el_cliente_reuna_la_con_3f67cd
    - Excepcion_los_cheques_emitidos_con_anterioridad_a_la_pertinente_notificacion_de_cierre_ser_2b449e
    - Excepcion_los_deudores_en_situacion_irregular_no_seran_clasificados_en_la_categoria_irrecu_1df386
    - Excepcion_los_endeudamientos_desembolsados_con_anterioridad_al_01_09_19__ext_3_5_1_1_ea60b7
    - Excepcion_los_gastos_podran_ser_trasladados_al_cuentacorrentista_cuando_el_pedido_de_modif_8ac074
    - Excepcion_los_instrumentos_tlac_computables_como_responsabilidad_patrimonial_computable_co_2798b4
    - Excepcion_los_limites_maximos_y_minimos_establecidos_sobre_las_tasas_de_interes_no_seran_c_3d8d2b
    - Excepcion_los_margenes_acordados_para_los_descubiertos_en_cuenta_corriente_y_los_limites_d_5eebb1
    - Excepcion_los_permisos_que_revistan_la_condicion_de_incumplido_en_gestion_de_cobro_no_sera_e424b4
    - Excepcion_los_requisitos_previstos_en_los_puntos_4_3_2_1_y_4_3_2_2_no_resultaran_aplicable_2f20e0
    - Excepcion_los_requisitos_previstos_en_los_puntos_4_3_2_1_y_4_3_2_2_no_resultaran_aplicable_8c3121
    - Excepcion_los_sobregiros_en_cuenta_corriente_bancaria_por_importes_que_excedan_los_margene_612648
    - Excepcion_los_titulos_valores_emitidos_por_la_contraparte_o_un_vinculado_a_ella_no_son_adm_284931
    - Excepcion_no_alcanza_la_exigencia_de_documentacion_en_braille_a_comprobantes_por_operacion_41a7d2
    - Excepcion_no_aplica_el_plazo_maximo_de_10_dias_cuando_i_se_trata_de_la_situacion_prevista__7b9d44
    - Excepcion_no_aplica_en_los_casos_a_que_se_refiere_el_punto_1_5_2_8_segundo_parrafo__ctacte_149688
    - Excepcion_no_aplica_la_conformidad_previa_del_bcra_cuando_la_operacion_encuadre_en_alguna__b2882c
    - Excepcion_no_aplica_la_obligacion_de_informar_al_bcra_en_la_situacion_prevista_en_los_dos__fb1192
    - Excepcion_no_aplicara_el_requisito_de_conformidad_previa_del_bcra_para_las_operaciones_de__49dde3
    - Excepcion_no_aplicara_la_clasificacion_obligatoria_de_irrecuperable_en_el_caso_de_deudores_f39997
    - Excepcion_no_corresponde_el_pago_cuando_se_trate_de_rechazos_producidos_entre_la_fecha_de__fb3aa1
    - Excepcion_no_corresponde_la_presentacion_de_esas_declaraciones_juradas_por_cada_una_de_las_3f16c1
    - Excepcion_no_correspondera_la_comunicacion_al_bcra_de_los_rechazos_motivados_por_falsifica_4e2685
    - Excepcion_no_deberan_considerarse_aquellos_bienes_que_cuenten_con_las_ventajas_aduaneras_e_8db920
    - Excepcion_no_deberan_considerarse_las_exportaciones_a_consumo_con_despacho_de_importacion__e4682a
    - Excepcion_no_deberan_considerarse_los_bienes_exportados_a_traves_de_operaciones_exceptuada_dbdb4d
    - Excepcion_no_es_necesario_contar_con_la_conformidad_previa_del_bcra_para_dar_acceso_al_mer_88abf6
    - Excepcion_no_estan_comprendidas_las_exposiciones_originadas_en_operaciones_al_contado_y_qu_3ef8db
    - Excepcion_no_implica_la_inclusion_en_la_causal_a_que_se_refiere_el_punto_9_1_2__ctacte_9_1_f30446
    - Excepcion_no_procedera_la_inclusion_respecto_de_apoderados_para_el_uso_de_la_cuenta_corrie_bd5f64
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_cancelaciones_d_5c85cf
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_operaciones_de__1f6142
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_operaciones_de__7c7aef
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_operaciones_de__a30320
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_operaciones_de__a7331c
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_operaciones_de__d73c45
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_operaciones_pro_a64b5f
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_pagos_al_exteri_775a4f
    - Excepcion_no_resultara_aplicable_el_requisito_de_conformidad_previa_del_bcra_cuando_el_cli_63b0b8
    - Excepcion_no_resultara_aplicable_el_requisito_de_conformidad_previa_del_bcra_cuando_la_ope_5987a2
    - Excepcion_no_se_considerara_error_el_rechazo_del_cheque_respecto_del_cual_haya_mediado_aut_845735
    - Excepcion_no_se_consideraran_comprendidas_en_la_definicion_de_nuevas_financiaciones_o_refi_10d1e7
    - Excepcion_no_se_consideraran_las_exportaciones_industriales_comprendidas_en_acuerdos_inter_a49332
    - Excepcion_no_se_consideraran_las_inversiones_obligatorias_que_deban_realizar_las_sucursale_1bd8b2
    - Excepcion_no_se_consideraran_refinanciaciones_otorgadas_a_productores_cuando_ello_resulte__655289
    - Excepcion_no_se_deberan_computar_los_montos_de_instrumentos_con_vinculacion_crediticia_u_o_4fd27e
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_bancos_u_otr_0cafa1
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_la_casa_matr_a64805
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_otros_bancos_e3fd87
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_sucursales_y_804456
    - Excepcion_no_se_deduciran_los_saldos_que_con_caracter_transitorio_y_circunstancial_se_orig_129ec9
    - Excepcion_no_se_incluyen_las_exposiciones_a_instrumentos_previstas_en_el_punto_2_11__cap_2_c00232
    - Excepcion_no_se_incluyen_las_operaciones_de_pase_que_no_hayan_podido_liquidarse_en_el_comp_5fc127
    - Excepcion_no_se_incluyen_los_ingresos_de_importaciones_temporarias_sin_giro_de_divisas__ex_ca6f8b
    - Excepcion_no_se_incluyen_los_registros_aduaneros_por_importaciones_suspensivas_de_deposito_d9a363
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_para_acceso_al_mercado_de_cambios_cua_b538f9
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_para_la_operatoria_con_derivados_cuan_c331f3
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_si_tal_requisito_estuviese_vigente_al_b09e58
    - Excepcion_no_sera_aplicable_en_el_caso_de_financiaciones_otorgadas_a_traves_de_la_suscripc_dbd82f
    - Excepcion_no_sera_de_aplicacion_en_las_operaciones_con_contrapartes_a_las_cuales_el_bcra_l_b593bf
    - Excepcion_no_sera_necesaria_la_presentacion_del_documento_anterior__docvig_3_3_1_634ebf
    - Excepcion_operaciones_aduaneras_de_envios_de_asistencia_y_salvamento_estan_exceptuadas_del_a11f9e
    - Excepcion_operaciones_aduaneras_exceptuadas_del_seguimiento_por_regimen_de_corredores_de_c_902de7
    - Excepcion_operaciones_aduaneras_realizadas_mediante_medios_de_transporte_de_guerra_segurid_a54d05
    - Excepcion_otros_bancos_del_exterior_autorizados_a_intervenir_en_los_regimenes_de_convenios_cb5d0a
    - Excepcion_para_fondos_percibidos_o_acreditados_en_exterior_se_considera_cumplimentado_ingr_8f26da
    - Excepcion_para_vpu_rigi_que_declararon_ante_la_autoridad_de_aplicacion_intencion_de_usar_b_09194d
    - Excepcion_pases_activos_de_dolares_estadounidenses_y_de_titulos_valores_publicos_nacionale_8444f9
    - Excepcion_podran_cumplimentar_el_requisito_de_cuil_obteniendo_una_copia_simple_en_papel_o__ee24a1
    - Excepcion_por_la_porcion_que_corresponda_a_una_capitalizacion_de_intereses_prevista_en_el__c859ad
    - Excepcion_quedan_excluidas_de_la_operacion_s06_viajes_las_operaciones_asociadas_a_retiros__8821fa
    - Excepcion_quedan_excluidos_aquellos_defectos_de_aplicacion_que_se_originen_en_operaciones__3af64e
    - Excepcion_quedan_excluidos_de_la_definicion_de_divisas_en_moneda_extranjera_las_monedas_y__2658b5
    - Excepcion_ratio_de_apalancamiento_mantiene_la_consolidacion_3_como_excepcion_a_la_suspensi_a7ea00
    - Excepcion_regimen_de_donacion_de_organos_y_sangre_humana_resolucion_384_97_de_la_administr_15f424
    - Excepcion_resultara_aplicable_lo_dispuesto_en_el_punto_14_1_4__ext_7_1_4_3e0d47
    - Excepcion_resultaran_de_aplicacion_las_disposiciones_sobre_extravio_sustraccion_o_adultera_163cc6
    - Excepcion_salvo_decision_de_autoridad_competente_que_obligue_al_cierre_inmediato__ctacte_9_4c156e
    - Excepcion_salvo_lo_previsto_en_el_apartado_12_2_3_2__ctacte_12_2_3_1_83b5e5
    - Excepcion_salvo_que_el_cliente_cuente_con_una_declaracion_jurada_en_la_que_deje_constancia_1cfb39
    - Excepcion_salvo_que_la_operacion_quedase_comprendida_en_la_situacion_prevista_en_el_punto__226fd3
    - Excepcion_salvo_que_la_operacion_quedase_comprendida_en_la_situacion_prevista_en_el_punto__2f5d8b
    - Excepcion_salvo_que_por_aplicacion_de_otras_pautas_corresponda_categorizarlo_en_el_nivel_i_66a0e4
    - Excepcion_salvo_que_resulte_aplicable_el_procedimiento_de_truncamiento_en_cuyo_caso_se_est_efef9b
    - Excepcion_salvo_que_se_tratara_de_un_cheque_girado_entre_distintos_establecimientos_de_un__14b027
    - Excepcion_salvo_que_se_trate_de_evaluaciones_privadas__cap_10_2_2_3_5da656
    - Excepcion_salvo_que_se_utilicen_escrituras_mecanizadas_de_seguridad__ctacte_2_1_1_6_8addf4
    - Excepcion_salvo_situaciones_de_fuerza_mayor_ajenas_a_la_voluntad_del_importador_se_exceptu_58c52c
    - Excepcion_se_admitira_unicamente_el_crecimiento_originado_por_el_devengamiento_de_interese_4eac3d
    - Excepcion_se_exceptua_de_la_prohibicion_general_el_pago_en_el_pais_a_partir_de_su_vencimie_d7fb56
    - Excepcion_se_exceptua_la_prohibicion_cuando_se_trate_de_inversiones_en_titulos_publicos_ex_57ee07
    - Excepcion_se_exceptua_la_prohibicion_para_la_cancelacion_en_el_pais_a_partir_del_vencimien_5328c8
    - Excepcion_se_exceptuan_cuando_los_cheques_se_depositen_en_la_caja_de_valores_s_a_para_ser__3d03c8
    - Excepcion_se_exceptuan_de_la_limitacion_los_endosos_que_las_entidades_financieras_realicen_5e7a96
    - Excepcion_se_exceptuan_los_endosos_a_favor_del_bcra__ctacte_5_1_1_1_628d4a
    - Excepcion_se_exceptuan_los_endosos_efectuados_en_los_echeq__ctacte_5_1_1_1_f7f18b
    - Excepcion_se_excluiran_del_monto_de_ventas_totales_aquellas_realizadas_por_la_empresa_en_e_330ac3
    - Excepcion_se_excluye_del_tratamiento_previsto_en_los_acapites_i_y_ii_a_las_lineas_continge_584fb8
    - Excepcion_se_excluyen_las_exposiciones_previstas_en_el_punto_2_11__cap_2_6_1_26d090
    - Excepcion_se_excluyen_los_casos_en_que_las_acciones_se_refieren_a_la_discusion_sobre_otros_97eb4c
    - Excepcion_se_excluyen_los_casos_en_que_las_acciones_se_refieren_a_la_discusion_sobre_otros_d9aec5
    - Excepcion_se_excluyen_tanto_las_estructuras_en_las_que_se_utilizan_los_flujos_de_efectivo__b97094
    - Excepcion_se_observara_lo_establecido_en_el_acapite_i_aplicacion_de_obligacion_presentar_p_6270f0
    - Excepcion_se_permite_la_liquidacion_mediante_deposito_en_cuentas_de_terceros_cuando_se_tra_67a33a
    - Excepcion_se_podra_excluir_del_computo_de_la_exigencia_de_capital_por_riesgo_general_de_me_6bf531
    - Excepcion_se_presenten_irregularidades_en_la_cadena_de_endosos__ctacte_6_1_1_2_da2095
    - Excepcion_se_produzca_un_evento_idiosincrasico_y_extraordinario_del_que_resulte_una_reducc_5bd358
    - Excepcion_se_realicen_ajustes_por_razones_objetivas__cap_2_9_2_3_0ede88
    - Excepcion_se_realicen_mejoras_de_caracter_permanente_en_el_inmueble_que_incrementen_su_val_5e1b23
    - Excepcion_se_trata_de_un_endeudamiento_financiero_comprendido_en_este_punto_3_5_con_una_vi_cf65e6
    - Excepcion_se_trate_de_operaciones_propias_de_las_entidades_financieras_locales__ext_3_3_3__9c78fb
    - Excepcion_se_trate_de_operaciones_propias_de_las_entidades_financieras_locales__ext_3_5_6__30cd5f
    - Excepcion_se_trate_de_un_endeudamiento_financiero_comprendido_en_este_punto_3_5_que_encuad_34e8c1
    - Excepcion_se_trate_de_un_endeudamiento_financiero_comprendido_en_este_punto_3_5_que_tenga__8f3fdb
    - Excepcion_se_verifique_la_situacion_prevista_en_el_segundo_parrafo_del_punto_6_4_6_1_insuf_4770ce
    - Excepcion_si_el_cliente_es_beneficiario_directo_del_decreto_277_22_el_valor_de_los_benefic_4de2a4
    - Excepcion_si_es_necesario_llegar_al_50_de_cobertura_del_primer_semestre_se_completara_con__992483
    - Excepcion_si_existiesen_fondos_destinados_al_pago_de_fletes_de_importaciones_de_bienes_no__0538dd
    - Excepcion_si_no_se_cumple_al_menos_una_de_las_dos_condiciones_senaladas_registro_de_export_5fa54d
    - Excepcion_sin_la_conformidad_previa_requerida_en_el_punto_3_3_3__ext_3_18_1_1_40df42
    - Excepcion_sin_la_conformidad_previa_requerida_en_el_punto_3_3_3_para_pagos_de_intereses_de_53053c
    - Excepcion_sin_necesidad_de_contar_con_la_conformidad_previa_del_bcra_si_tal_requisito_estu_0eaf7c
    - Excepcion_sin_necesidad_de_contar_con_la_conformidad_previa_del_bcra_si_tal_requisito_estu_677da6
    - Excepcion_sin_perjuicio_de_la_eventual_aplicacion_de_los_motivos_de_rechazo_previstos_en_l_ddc711
    - Excepcion_sin_perjuicio_de_lo_anterior_estan_exceptuadas_las_deudas_que_reunan_todas_las_c_c8ae33
    - Excepcion_sin_perjuicio_de_lo_previsto_en_los_puntos_5_1_a_5_3_de_las_normas_sobre_autoriz_baa6fe
    - Excepcion_sin_perjuicio_de_los_conceptos_que_deban_trasladar_a_los_clientes_por_tributos_r_24d05b
    - Excepcion_sin_perjuicio_de_los_servicios_adicionales_para_facilitar_la_carga_masiva_de_dic_6aa88a
    - Excepcion_sin_perjuicio_de_su_informacion_segun_las_normas_que_se_establezcan_en_los_regim_033592
    - Excepcion_sin_perjuicio_del_pago_parcial_que_podra_efectuar_la_entidad_conforme_a_lo_dispu_664b93
    - Excepcion_sucursales_y_subsidiarias_de_entidades_financieras_locales_sujetas_al_regimen_de_31bcff
    - Excepcion_tambien_se_podra_computar_el_valor_de_los_fletes_que_conste_en_la_documentacion__41ac37
    - Excepcion_tampoco_se_consideraran_dentro_de_ese_concepto_las_refinanciaciones_otorgadas_a__cf6430
    - Excepcion_titulos_de_deuda_con_registro_publico_en_el_pais_comprendidos_en_el_punto_3_5_qu_657d92
    - Excepcion_transferencias_realizadas_por_representaciones_en_el_pais_de_tribunales_autorida_0f045d
    - Excepcion_unicamente_se_admitira_la_constitucion_de_las_garantias_en_cuentas_abiertas_en_e_c9043d
    - Excepcion_valores_a_favor_de_terceros_destinados_al_pago_de_sueldos_y_otras_retribuciones__d33b7b
Obligacion: 231 sin aplica_a
    - Obligacion_a_efectos_de_generar_confianza_respecto_tanto_de_la_exactitud_de_lo_informado_so_4b4001
    - Obligacion_a_fin_de_asegurar_que_los_fiduciarios_y_administradores_tengan_amplia_experienci_f9c517
    - Obligacion_a_fin_de_asistir_a_los_inversores_en_la_realizacion_de_un_apropiado_proceso_de_d_9d5311
    - Obligacion_a_las_categorias_bcra_gobierno_nacional_gobiernos_provinciales_municipales_y_de__edc717
    - Obligacion_a_los_conceptos_citados_en_los_puntos_precedentes_se_les_restaran_de_corresponde_ce0884
    - Obligacion_a_los_efectos_del_reconocimiento_de_la_cobertura_del_riesgo_de_credito_se_tendra_941ede
    - Obligacion_a_los_efectos_del_registro_de_estas_operaciones_se_deberan_confeccionar_dos_bole_ca6aed
    - Obligacion_a_partir_de_su_incorporacion_al_seguimiento_resultaran_de_aplicacion_las_normas__2d885e
    - Obligacion_acompanar_la_documentacion_que_acredite_el_reclamo_informado_o_indicar_su_locali_60729f
    - Obligacion_adicionalmente_al_momento_de_la_inclusion_del_activo_en_la_cartera_de_subyacente_11e0a2
    - Obligacion_adicionalmente_se_insertara_alguna_de_las_siguientes_expresiones_en_procuracion__9759d1
    - Obligacion_adjuntar_copia_simple_o_imagen_del_documento_de_identificacion_del_presentante_y_2864d8
    - Obligacion_al_calcular_la_exigencia_maxima_de_capital_se_deducira_el_total_de_las_ganancias_6c2c9b
    - Obligacion_analisis_adecuado_de_la_situacion_economica_y_financiera_del_deudor__cla_3_1_f98786
    - Obligacion_asesorara_al_directorio_sobre_los_riesgos_de_la_entidad__lingob_4_2_1_18f3c4
    - Obligacion_bajo_el_mba_el_apalancamiento_se_medira_usando_el_maximo_apalancamiento_permitid_9a66a4
    - Obligacion_calculo_de_la_exposicion_a_las_operaciones_de_financiacion_con_titulos_valores_c_7916d2
    - Obligacion_certificacion_judicial_en_original_que_acredite_haber_efectuado_la_pertinente_de_e6a10f
    - Obligacion_confeccion_de_las_declaraciones_juradas_previstas_en_los_puntos_3_16_3_1_y_3_16__40777b
    - Obligacion_constancia_de_las_publicaciones_que_hagan_saber_el_inicio_del_tramite_falencial__824d9c
    - Obligacion_constatar_tanto_en_los_cheques_librados_en_formato_papel_como_en_los_certificado_000e3f
    - Obligacion_controlar_que_los_niveles_gerenciales_tomen_los_pasos_necesarios_para_identifica_95242f
    - Obligacion_correspondera_considerarlas_como_exposiciones_a_empresas_del_sector_privado_no_f_7cea83
    - Obligacion_cualquier_valor_excedente_de_las_acciones_que_componen_la_canasta_por_encima_del_db6ba3
    - Obligacion_cuando_el_ingreso_corresponda_a_exportaciones_a_paraguay_o_a_uruguay_facturadas__fc95e3
    - Obligacion_cuando_esos_estandares_se_vean_afectados_por_cambios_el_originante_debera_comuni_1a9744
    - Obligacion_cuando_existe_saldo_deudor_el_cierre_debera_al_menos_poder_ser_realizado_en_form_6a71a6
    - Obligacion_cuenten_con_una_certificacion_de_incremento_de_exportaciones_asociadas_a_la_econ_4e7fcd
    - Obligacion_dando_orientacion_a_los_usuarios_de_servicios_financieros_sobre_la_manera_de_can_b47788
    - Obligacion_de_corresponder_debera_informarse_toda_condicion_o_evento_que_pueda_retrasar_o_i_630702
    - Obligacion_de_haberse_realizado_el_pago_en_moneda_extranjera_documentacion_por_la_cual_se_l_9f69bb
    - Obligacion_de_haberse_realizado_el_pago_en_moneda_extranjera_se_requerira_certificacion_de__d184b4
    - Obligacion_de_tratarse_de_documentos_expedidos_en_lengua_no_espanola_se_requerira_que_se_lo_879f63
    - Obligacion_debe_contarse_con_la_certificacion_de_afectacion_emitida_por_la_entidad_encargad_4d9675
    - Obligacion_debera_abonarse_la_suma_de_90_por_cada_modificacion_de_computo_en_la_central_de__8c6482
    - Obligacion_debera_asegurarse_la_continuidad_de_los_derechos_y_obligaciones_referidos_a_dich_7683d6
    - Obligacion_debera_demostrarse_ante_la_entidad_encargada_del_seguimiento_de_ese_pago_y_por_h_02ef73
    - Obligacion_debera_identificarse_claramente_a_las_partes_responsables_de_determinar_si_ocurr_380ccc
    - Obligacion_debera_ofrecerse_la_utilizacion_de_mecanismos_electronicos_simples_eficaces_e_in_8514d9
    - Obligacion_debera_tenerse_en_cuenta_lo_dispuesto_en_el_punto_4_3__cap_2_12_14_d75ecb
    - Obligacion_deberian_incluirse_disposiciones_que_contemplen_el_reemplazo_de_los_administrado_f1fab8
    - Obligacion_debiendo_cumplirse_con_los_requisitos_aplicables_para_formacion_de_activos_exter_86f742
    - Obligacion_debiendose_verificarse_los_restantes_requisitos_habituales__ext_7_3_11_eb6b5f
    - Obligacion_del_50_de_las_ganancias_de_las_entidades_financieras_controladas_en_la_proporcio_c14844
    - Obligacion_demostrar_el_registro_de_ingreso_aduanero_de_los_bienes_dentro_de_los_90_noventa_4944f1
    - Obligacion_documento_de_viaje_admitido_por_la_decision_mercosur_en_vigencia__docvig_2_1_1_1_d019c6
    - Obligacion_documento_que_lo_identifique_en_el_pais_de_residencia_expedido_de_conformidad_co_606711
    - Obligacion_efectuar_el_seguimiento_de_los_permisos_de_embarques_cuyos_cobros_se_mantengan_e_9476f7
    - Obligacion_el_acceso_al_mercado_de_cambios_con_anterioridad_al_vencimiento_requerira_la_con_9908e9
    - Obligacion_el_aviso_debe_consignar_el_caracter_con_el_que_fue_impuesto__ctacte_10_2_1_4_3cef8e
    - Obligacion_el_banco_central_de_la_republica_argentina_publicara_periodicamente_el_valor_dia_e4c995
    - Obligacion_el_bcra_debe_debitar_de_la_cuenta_corriente_de_la_entidad_participante_el_import_52b514
    - Obligacion_el_bcra_procedera_a_debitar_de_la_cuenta_corriente_de_la_entidad_participante_el_50f8dd
    - Obligacion_el_bcra_procesara_el_cierre_de_las_rendiciones_de_cuentas_pendientes_de_las_enti_0ab518
    - Obligacion_el_boleto_de_compra_se_confeccionara_por_un_codigo_de_concepto_que_identifique_q_bcfc47
    - Obligacion_el_boleto_de_venta_se_confeccionara_por_el_monto_correspondiente_con_el_codigo_d_e3b924
    - Obligacion_el_calculo_de_k_ccp_debera_hacerse_como_minimo_con_periodicidad_trimestral__cap__777f23
    - Obligacion_el_certificado_sera_transmisible_ilimitadamente_por_endoso_en_identicas_condicio_537ae5
    - Obligacion_el_cliente_cumple_la_totalidad_de_las_condiciones_estipuladas_en_cada_caso__ext__87b604
    - Obligacion_el_cliente_debe_contar_con_una_certificacion_por_los_regimenes_de_acceso_a_divis_f0e0d8
    - Obligacion_el_cliente_debe_haber_actualizado_la_declaracion_jurada_previamente_presentada_s_8eb001
    - Obligacion_el_cliente_debe_haber_presentado_declaracion_jurada_sobre_si_reviste_o_no_el_car_3783e3
    - Obligacion_el_cliente_debera_firmar_una_declaracion_jurada_en_la_que_se_compromete_a_ingres_b7e0f3
    - Obligacion_el_cliente_debera_presentar_la_documentacion_que_avale_la_capitalizacion_definit_310d7d
    - Obligacion_el_cliente_debera_presentar_un_documento_de_identidad_admitido_en_las_normas_sob_ec96d0
    - Obligacion_el_cliente_que_acceda_al_mercado_de_cambios_usando_este_mecanismo_debera_nominar_3fd3a1
    - Obligacion_el_comite_de_auditoria_debera_coordinar_los_esfuerzos_de_las_auditorias_externa__0c0fc1
    - Obligacion_el_comite_debe_vigilar_el_diseno_del_sistema_de_incentivos_economicos_al_persona_ecb77d
    - Obligacion_el_contrato_de_fideicomiso_debera_incluir_el_modo_de_sustitucion_del_fiduciario__f2e648
    - Obligacion_el_desempeno_se_debera_verificar_durante_un_periodo_minimo_de_5_anos_en_el_caso__2613ed
    - Obligacion_el_deudor_que_encontrandose_clasificado_en_esta_categoria_haya_refinanciado_su_d_872a15
    - Obligacion_el_documento_a_cobrar_o_derecho_de_credito_transferido_no_es_objeto_de_litigios__c6b6e0
    - Obligacion_el_documento_debe_contar_en_su_caso_con_certificacion_notarial__docvig_2_5_902cb1
    - Obligacion_el_documento_debe_presentarse_legalizado_consularmente_o_por_el_sistema_de_apost_835a8a
    - Obligacion_el_estado_financiero_debera_contar_con_la_intervencion_del_auditor_externo_previ_790fbf
    - Obligacion_el_estado_financiero_debera_estar_acompanado_de_un_informe_especial_del_auditor__1dd527
    - Obligacion_el_estado_financiero_debera_haber_sido_previamente_presentados_ante_el_bcra__cap_869392
    - Obligacion_el_excedente_de_rpc_atribuible_a_los_inversores_minoritarios_resultara_de_multip_c965bf
    - Obligacion_el_exportador_debe_aportar_constancia_de_la_presentacion_efectuada_para_obtener__8e74cd
    - Obligacion_el_exportador_debera_presentar_una_declaracion_jurada_en_la_cual_identifique_el__99b9ee
    - Obligacion_el_fiduciario_o_administrador_debera_en_todo_momento_actuar_en_forma_razonable_p_900c6b
    - Obligacion_el_interviniente_a_quien_le_corresponde_el_anadido_debera_firmar_abarcando_tanto_f1f234
    - Obligacion_el_monto_maximo_de_las_certificaciones_para_el_exportador_sera_informado_a_las_e_e12c50
    - Obligacion_el_obligado_al_pago_no_cuenta_con_un_historial_de_credito_desfavorable_en_algun__ddfc77
    - Obligacion_el_obligado_al_pago_no_cuenta_con_una_evaluacion_de_una_agencia_de_calificacion__e7ba64
    - Obligacion_el_obligado_al_pago_no_ha_sido_sometido_a_un_proceso_de_quiebra_o_de_reestructur_1130e7
    - Obligacion_el_otorgamiento_de_asistencia_con_metodo_especifico_de_evaluacion_no_obsta_a_que_6d3ddb
    - Obligacion_el_plazo_tambien_sera_aplicable_para_las_operaciones_que_correspondan_a_las_tran_cb1166
    - Obligacion_el_ponderador_de_riesgo_que_corresponda_a_la_contraparte_se_aplicara_a_la_suma_d_1d6a78
    - Obligacion_el_riesgo_de_tasa_de_interes_del_derivado_se_computara_conforme_a_lo_indicado_en_dc4358
    - Obligacion_el_sistema_online_tomara_en_consideracion_exclusivamente_los_ingresos_de_divisas_9e007c
    - Obligacion_en_caso_de_corresponder_los_instrumentos_que_permitan_a_quien_se_presenta_actuar_bc1d85
    - Obligacion_en_caso_de_levantarse_el_pedido_de_quiebra_el_deudor_podra_ser_reclasificado_en__236ce8
    - Obligacion_en_caso_de_no_contar_con_la_documentacion_de_capitalizacion_definitiva_el_vpu_de_4e5a85
    - Obligacion_en_caso_de_no_disponer_de_la_documentacion_de_capitalizacion_definitiva_el_vpu_d_ba019c
    - Obligacion_en_caso_de_que_al_momento_de_concretarse_el_acceso_el_cliente_no_cuente_con_la_d_1565b9
    - Obligacion_en_caso_de_que_el_vpu_contemple_la_posibilidad_de_aplicar_cobros_de_exportacione_db34ab
    - Obligacion_en_caso_de_tratarse_de_la_repatriacion_de_un_cobro_de_capital_la_entidad_debera__97433a
    - Obligacion_en_caso_de_verificarse_atrasos_mayores_a_31_dias_en_el_pago_de_los_servicios_de__54d8b6
    - Obligacion_en_defecto_de_la_demostracion_del_registro_de_ingreso_aduanero_proceder_al_reing_be6832
    - Obligacion_en_el_caso_de_carteras_atomizadas_tales_documentos_o_derechos_deberan_ser_origin_b3918b
    - Obligacion_en_el_caso_de_deudores_que_hayan_solicitado_el_concurso_preventivo_correspondera_4a6968
    - Obligacion_en_el_caso_de_que_la_legislacion_aplicable_a_la_titulizacion_no_se_ajuste_a_los__ce34cc
    - Obligacion_en_estos_dos_ultimos_casos_deberan_observarse_los_requisitos_incluidos_en_el_pun_a36886
    - Obligacion_en_las_clausulas_del_contrato_de_cuenta_corriente_debera_preverse_que_los_debito_bd1ff7
    - Obligacion_en_los_demas_aspectos_vinculados_a_la_figura_del_endoso_rige_lo_dispuesto_en_la__8b96ae
    - Obligacion_en_todos_los_casos_debera_acreditarse_la_categoria_de_residencia_su_vigencia_y_e_bbc812
    - Obligacion_esos_dispositivos_deberan_informar_previamente_al_cliente_las_operaciones_admiti_a7744c
    - Obligacion_existencia_del_registro_de_ingreso_aduanero_a_su_nombre_o_a_nombre_de_un_tercero_0dc0a5
    - Obligacion_factura_comercial_emitida_por_el_comprador_a_su_cliente_en_el_exterior_donde_con_bb14da
    - Obligacion_haya_liquidado_los_montos_cubiertos_por_la_compania_de_seguro_por_el_credito_imp_6afa5d
    - Obligacion_identico_criterio_se_aplicara_para_la_determinacion_del_periodo_de_mantenimiento_932a39
    - Obligacion_la_alta_gerencia_como_una_buena_practica_sera_responsable_de__lingob_3_1_de7782
    - Obligacion_la_asociacion_denunciante_debera_acreditar_su_condicion_de_entidad_reconocida_y__460e50
    - Obligacion_la_ccp_la_entidad_financiera_la_autoridad_de_control_de_la_ccp_u_otro_organismo__1a01b3
    - Obligacion_la_constancia_de_la_comunicacion_de_adhesion_podra_quedar_en_poder_de_la_empresa_71e800
    - Obligacion_la_declaracion_jurada_debera_estar_firmada_por_el_representante_legal_de_la_empr_d2d412
    - Obligacion_la_documentacion_debera_estar_legalizada_por_autoridad_consular_o_conforme_a_lo__3e5321
    - Obligacion_la_documentacion_debera_estar_legalizada_por_autoridad_consular_o_conforme_a_lo__8c86e4
    - Obligacion_la_emision_de_una_certificacion_por_parte_de_la_entidad_implica_que_a_la_fecha_d_42e3e7
    - Obligacion_la_entidad_cuente_con_documentacion_que_acredite_el_efectivo_ingreso_de_la_inver_67736a
    - Obligacion_la_entidad_cuente_con_una_declaracion_jurada_del_cliente_en_la_cual_deje_constan_9811b4
    - Obligacion_la_entidad_debe_verificar_que_el_deudor_hubiese_tenido_acceso_para_realizar_el_p_68543b
    - Obligacion_la_entidad_debera_certificar_por_los_mecanismos_establecidos_que_se_ha_cumplido__d44f00
    - Obligacion_la_entidad_debera_contar_con_la_correspondiente_certificacion_de_la_entidad_enca_d50ad6
    - Obligacion_la_entidad_debera_verificar_en_el_sistema_online_implementado_por_el_bcra_que_el_7ef1cc
    - Obligacion_la_entidad_encargada_del_seguimiento_del_zfi_en_el_sepaimpo_debe_emitir_la_corre_7e345d
    - Obligacion_la_entidad_financiera_ha_concretado_el_registro_de_la_financiacion_ante_el_bcra__1dd46e
    - Obligacion_la_entidad_interviniente_cuenta_con_una_declaracion_jurada_del_exportador_en_la__d72bd9
    - Obligacion_la_entidad_interviniente_debe_contar_con_i_declaracion_jurada_del_exportador_ii__781b24
    - Obligacion_la_entidad_interviniente_debera_contar_con_una_certificacion_de_la_entidad_encar_4df3a9
    - Obligacion_la_entidad_podra_considerar_cumplimentado_parcial_o_totalmente_el_seguimiento_de_cbfd77
    - Obligacion_la_entidad_podra_dar_acceso_al_mercado_de_cambios_para_el_pago_al_exterior_en_la_be6d14
    - Obligacion_la_entidad_responsable_debera_verificar_el_cumplimiento_de_las_condiciones_estip_285ee7
    - Obligacion_la_entidad_verifico_que_las_cantidades_y_descripciones_de_la_mercaderia_de_la_fa_ed87eb
    - Obligacion_la_exigencia_maxima_agregada_para_todas_las_posiciones_en_la_misma_titulizacion__f6fa02
    - Obligacion_la_forma_de_la_remuneracion_de_quienes_tengan_responsabilidad_fiduciaria_deberia_998e9e
    - Obligacion_la_gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros_tramitar_953a49
    - Obligacion_la_informacion_que_surja_del_legajo_unico_financiero_y_economico_establecido_por_87d3ee
    - Obligacion_la_liquidacion_en_el_mercado_de_cambios_de_las_divisas_asociadas_a_la_devolucion_ba8152
    - Obligacion_la_precancelacion_de_capital_e_intereses_sea_efectuada_en_manera_simultanea_con__436096
    - Obligacion_la_proporcion_del_incentivo_economico_diferido_no_percibido_se_ajustara_en_funci_5b2b1a
    - Obligacion_la_solicitud_de_autorizacion_de_aportes_de_capital_con_los_instrumentos_a_que_se_fedd4d
    - Obligacion_la_tasa_de_interes_se_calculara_sobre_el_equivalente_en_pesos_que_surja_de_aplic_53a34b
    - Obligacion_las_certificaciones_tendran_una_validez_de_10_diez_dias_habiles_a_contar_desde_l_1d957d
    - Obligacion_las_disposiciones_de_esta_seccion_tienen_como_objetivo_reducir_los_estimulos_hac_10e01e
    - Obligacion_las_entidades_adheridas_al_sistema_deberan_reportar_las_cotizaciones_comprador_y_3b1764
    - Obligacion_las_entidades_conservaran_constancia_escrita_de_la_notificacion_a_los_clientes_s_9f91a4
    - Obligacion_las_entidades_deberan_observar_el_procedimiento_detallado_en_los_puntos_9_2_1_1__ea68f4
    - Obligacion_las_exposiciones_con_garantia_hipotecaria_clasificadas_como_normativas_deberan_c_4b5d52
    - Obligacion_las_fechas_de_corte_de_los_datos_deberan_estar_en_linea_con_las_utilizadas_para__516546
    - Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_defi_3b082c
    - Obligacion_las_operaciones_de_cambio_en_divisas_extranjeras_deberan_sujetarse_a_los_requisi_75f345
    - Obligacion_las_participaciones_seran_netas_de_las_previsiones_por_riesgo_de_desvalorizacion_4dcb72
    - Obligacion_las_politicas_procedimientos_y_controles_de_gestion_de_riesgos_deberan_estar_bie_7f8720
    - Obligacion_las_posiciones_compradas_y_vendidas_en_la_misma_especie_podran_computarse_en_ter_6ca513
    - Obligacion_las_subsidiarias_en_el_exterior_quedaran_comprendidas_en_la_medida_en_que_ellas__8295e4
    - Obligacion_liquidacion_de_los_cobros_de_exportaciones_de_bienes_y_servicios__ext_2_6_1_ff8ba9
    - Obligacion_lo_cual_sera_acreditado_mediante_copia_con_legalizacion_consular_de_la_normativa_9928c0
    - Obligacion_los_aportes_se_deberan_registrar_a_su_valor_contable_capital_intereses_ajustes_d_39f8d0
    - Obligacion_los_auditores_externos_tienen_el_deber_de_ejercer_la_debida_diligencia_profesion_f90a2e
    - Obligacion_los_beneficiarios_gozaran_de_un_trato_diferencial_como_clientes_con_prioridad_de_277835
    - Obligacion_los_beneficiarios_tendran_acceso_a_todas_las_cajas_de_la_casa_o_sucursal_donde_l_61cbe6
    - Obligacion_los_boletos_deberan_quedar_registrados_independientemente_de_cual_sea_el_momento_44741b
    - Obligacion_los_casos_que_no_cumplan_las_condiciones_requeridas_quedaran_sujetos_a_la_confor_9db58f
    - Obligacion_los_cobros_no_aplicados_y_las_quitas_concedidas_en_forma_previa_a_la_refinanciac_46f41c
    - Obligacion_los_cobros_y_los_pagos_asociados_a_esta_operatoria_deberan_ser_cursados_utilizan_cc896d
    - Obligacion_los_conceptos_registrados_en_pfb_deben_convertirse_en_equivalentes_crediticios_m_d15704
    - Obligacion_los_documentos_a_cobrar_o_derechos_de_credito_titulizados_deberan_satisfacer_cri_f820e2
    - Obligacion_los_flujos_de_fondos_nocionales_netos_sujetos_a_reapreciacion_en_cada_banda_temp_8dda4d
    - Obligacion_los_flujos_de_fondos_nocionales_sujetos_a_reapreciacion_se_deben_asignar_a_sus_c_447fc4
    - Obligacion_los_flujos_de_fondos_nocionales_sujetos_a_reapreciacion_se_deben_asignar_a_sus_c_a3e27f
    - Obligacion_los_importes_se_consignaran_en_valores_absolutos__ric_11_1_1_ff7153
    - Obligacion_los_pagos_por_adelantado_y_o_anticipos_efectuados_en_oportunidad_de_la_refinanci_881082
    - Obligacion_luego_de_la_citada_refinanciacion_y_a_los_fines_de_la_clasificacion_debera_tener_8a2eb1
    - Obligacion_no_ha_utilizado_ya_este_mecanismo_por_estos_fondos_cobrados_en_el_pais__ext_4_6__0ce9a4
    - Obligacion_no_obstante_en_el_caso_de_futuros_en_los_que_el_subyacente_sea_un_titulo_de_deud_c2e802
    - Obligacion_no_sera_obligatoria_para_el_cliente_la_entrega_de_las_constancias_del_cuit_cuil__be003a
    - Obligacion_obligacion_de_confidencialidad_a_que_se_refieren_las_leyes_de_entidades_financie_78fb47
    - Obligacion_obligacion_de_ingreso_y_o_liquidacion_del_contravalor_en_divisas_por_exportacion_617af5
    - Obligacion_obligacion_de_liquidacion_de_cobros_de_exportaciones_de_bienes__ext_7_8_4_22312f
    - Obligacion_obligacion_de_liquidacion_los_cobros_de_exportaciones_de_servicios__ext_2_2_2_b1a34c
    - Obligacion_operada_la_liquidacion_del_seguro_la_documentacion_respectiva_se_completara_con__1cb479
    - Obligacion_para_adoptar_la_decision_de_aportes_de_capital_la_asamblea_tuvo_a_su_disposicion_805fb2
    - Obligacion_para_asegurar_total_transparencia_hacia_los_inversores_las_obligaciones_contract_afcefe
    - Obligacion_para_el_resto_de_las_exposiciones_el_desempeno_debera_verificarse_durante_7_anos_a5b65f
    - Obligacion_para_las_posteriores_refinanciaciones_recibiran_el_tratamiento_general_previsto__956ed2
    - Obligacion_para_mejorar_la_transparencia_y_claridad_sobre_todos_los_ingresos_egresos_y_dema_d60897
    - Obligacion_pasaporte_del_pais_de_origen__docvig_2_1_1_1_c464f4
    - Obligacion_pasaporte_del_pais_de_origen_de_corresponder_visado_por_autoridad_consular_argen_584d16
    - Obligacion_pasaporte_del_pais_de_origen_de_corresponder_visado_por_autoridad_consular_argen_59b76b
    - Obligacion_permitir_la_compensacion_de_las_perdidas_y_ganancias_resultantes_de_las_operacio_85d574
    - Obligacion_permitir_la_rapida_liquidacion_o_compensacion_de_los_activos_admitidos_en_garant_15578f
    - Obligacion_presentacion_de_fotocopias_autenticadas_por_escribano_publico_de_los_documentos__7a5b92
    - Obligacion_proporcionar_a_la_parte_que_no_se_encuentra_en_situacion_de_incumplimiento_el_de_fc5e08
    - Obligacion_proveer_conjuntamente_con_la_presentacion_los_datos_de_identificacion_del_reclam_836224
    - Obligacion_que_a_la_entidad_interviniente_le_conste_que_el_comprador_argentino_ha_liquidado_e8b9c1
    - Obligacion_que_la_sefyc_se_expida_al_respecto_seran_de_10_dias_habiles__cap_6_7_2_2_192723
    - Obligacion_quedan_sometidos_sin_derecho_a_reclamo_alguno_los_interesados__ctacte_12_2_0ffa14
    - Obligacion_revision_periodica_de_su_situacion_en_cuanto_a_las_condiciones_objetivas_y_subje_422dc9
    - Obligacion_se_ajustara_a_los_terminos_de_la_pertinente_disposicion__ctacte_9_1_4_f253c4
    - Obligacion_se_aplicara_lo_previsto_por_el_articulo_261_de_la_ley_19_550__lingob_6_2_6_0ba4b6
    - Obligacion_se_computara_el_importe_que_surja_de_aplicar_a_los_valores_contables_de_los_inst_f49fe2
    - Obligacion_se_debera_admitir_como_minimo_la_utilizacion_de_la_banca_por_internet_home_banki_d1c334
    - Obligacion_se_debera_evaluar_si_los_sistemas_de_informacion_y_las_funciones_de_reporte_son__0ba045
    - Obligacion_se_debera_suministrar_al_menos_trimestralmente_durante_la_vida_de_la_titulizacio_216d1a
    - Obligacion_se_demostrara_con_cualquiera_de_las_siguientes_alternativas__ctacte_8_3_da1b48
    - Obligacion_se_demostrara_con_cualquiera_de_las_siguientes_alternativas__ctacte_8_4_ba2ab3
    - Obligacion_se_demuestre_el_registro_de_ingreso_aduanero_de_bienes_por_un_valor_equivalente__338c74
    - Obligacion_se_determinara_teniendo_en_cuenta_lo_dispuesto_en_las_normas_sobre_capitales_min_3ef039
    - Obligacion_se_reconocera_la_cobertura_del_riesgo_de_credito_mediante_la_utilizacion_de_las__8db7fc
    - Obligacion_se_remitiran_las_presentaciones_recibidas_a_las_autoridades_administrativas_con__35dac3
    - Obligacion_se_verifiquen_la_totalidad_de_las_condiciones_previstas_en_cada_caso_para_que_la_c98f70
    - Obligacion_sera_de_aplicacion_lo_previsto_en_la_seccion_6_segun_corresponda_y_complementari_fe2fb8
    - Obligacion_si_el_exportador_considera_que_existen_errores_en_la_forma_en_que_un_permiso_de__95f961
    - Obligacion_si_el_siniestro_fue_liquidado_en_moneda_local_copia_del_extracto_bancario_donde__f53e97
    - Obligacion_si_el_siniestro_fue_liquidado_en_moneda_local_copia_del_resumen_de_cuenta_de_dep_da920e
    - Obligacion_si_hubiera_compensacion_a_los_tenedores_de_estos_instrumentos_por_la_quita_reali_47f69a
    - Obligacion_si_la_aplicacion_del_desembolso_en_divisas_fuese_posterior_a_la_fecha_del_regist_b4d354
    - Obligacion_si_la_financiacion_fue_otorgada_por_el_propio_proveedor_el_boleto_se_registrara__35caea
    - Obligacion_si_para_proceder_a_la_liquidacion_de_la_proteccion_crediticia_fuera_necesario_qu_c6066e
    - Obligacion_sobre_los_conceptos_a_y_pfb_se_aplicaran_los_ponderadores_de_riesgo_de_contrapar_b9dc32
    - Obligacion_solo_se_requerira_la_exhibicion_del_dni_m_o_dni_d_expedido_con_posterioridad_a_l_f5843a
    - Obligacion_su_observancia_se_computara_a_base_de_los_saldos_registrados_al_ultimo_dia_de_ca_296006
    - Obligacion_tanto_en_la_oferta_inicial_como_en_la_documentacion_contractual_deberia_incluirs_a2b86b
    - Obligacion_tanto_los_directores_independientes_como_aquellos_que_no_reunan_esa_condicion_pe_f7f930
    - Obligacion_tasa_de_interes_sera_calculada_sobre_el_equivalente_que_surja_de_aplicar_lo_prev_7c98cd
    - Obligacion_todo_mandato_se_entendera_subsistente_hasta_tanto_su_revocacion_se_notifique_feh_bbd871
    - Obligacion_todo_riesgo_de_tipo_de_cambio_que_surja_de_posiciones_compensadas_debera_computa_c780ba
    - Obligacion_toma_conocimiento_de_que_no_tendra_acceso_al_mercado_de_cambios_para_repatriar_e_d17e63
    - Obligacion_verificar_la_firma_del_presentante_que_debera_insertarse_con_caracter_de_recibo__fee523
Operacion: 1506 sin aplica_a
    - Operacion_abono_a_los_fondos_al_librador_cecc5d
    - Operacion_absorcion_de_perdidas_instrumentos_d873e6
    - Operacion_accesibilidad_puntos_de_atencion_usuario_d1215d
    - Operacion_acceso_a_divisas_produccion_incremental_petroleo_gas_19c086
    - Operacion_acceso_a_mercado_cambios_prestamos_financieros_exterior_contrapartes_vinculadas_2764d3
    - Operacion_acceso_a_mercado_de_cambios_con_certificacion_ca24a0
    - Operacion_acceso_a_mercado_de_cambios_endeudamiento_9950c3
    - Operacion_acceso_a_mercado_de_cambios_titulos_deuda_exterior_99ae4e
    - Operacion_acceso_al_mercado_cambios_formacion_activos_externos_522a22
    - Operacion_acceso_al_mercado_de_cambio_operaciones_s3_1_a_s3_15_f2f0d5
    - Operacion_acceso_al_mercado_de_cambios_b8c486
    - Operacion_acceso_al_mercado_de_cambios_compra_de_moneda_extranjera_8c2013
    - Operacion_acceso_al_mercado_de_cambios_fideicomisos_144617
    - Operacion_acceso_al_mercado_de_cambios_garantias_financieras_8bb13b
    - Operacion_acceso_al_mercado_de_cambios_garantias_y_avales_2dc854
    - Operacion_acceso_al_mercado_de_cambios_importaciones_5a5d0a
    - Operacion_acceso_al_mercado_de_cambios_otras_compras_de_bienes_75b52d
    - Operacion_acceso_al_mercado_de_cambios_pago_anticipado_de_importaciones_6dd329
    - Operacion_acceso_al_mercado_de_cambios_pago_importaciones_2e8c59
    - Operacion_acceso_al_mercado_de_cambios_pago_medicamentos_e47e9d
    - Operacion_acceso_al_mercado_de_cambios_pago_medicamentos_pendiente_ceb32b
    - Operacion_acceso_al_mercado_de_cambios_pago_servicios_no_residentes_4e2bf8
    - Operacion_acceso_al_mercado_de_cambios_pagos_aduaneros_pendientes_428f98
    - Operacion_acceso_al_mercado_de_cambios_pagos_de_importaciones_b90e84
    - Operacion_acceso_al_mercado_de_cambios_pagos_de_intereses_764d73
    - Operacion_acceso_al_mercado_de_cambios_pagos_por_importaciones_daebe5
    - Operacion_acceso_al_mercado_de_cambios_para_importaciones_temporales_139551
    - Operacion_acceso_al_mercado_de_cambios_para_pago_diferido_ad26af
    - Operacion_acceso_al_mercado_de_cambios_para_pago_exterior_ff3848
    - Operacion_acceso_al_mercado_de_cambios_para_pagos_de_servicios_9cef10
    - Operacion_acceso_al_mercado_de_cambios_por_egresos_vpu_rigi_c1b1b1
    - Operacion_acceso_cambios_titulos_deuda_ars_suscriptos_exterior_a68bae
    - Operacion_acceso_diario_mercado_cambios_compra_moneda_extranjera_c39577
    - Operacion_acceso_mercado_cambios_cancelacion_obligaciones_en_moneda_extranjera_ce63dd
    - Operacion_acceso_mercado_cambios_egresos_vpu_ce1319
    - Operacion_aceleracion_de_devolucion_de_pagos_futuros_7d06c4
    - Operacion_aceptacion_de_presentacion_sin_inconsistencias_86851e
    - Operacion_aceptacion_de_presentacion_tardia_e7bd41
    - Operacion_acreditacion_a_cuenta_de_anses_a60951
    - Operacion_acreditacion_de_categoria_de_residencia_9ebec5
    - Operacion_acreditacion_de_cuenta_de_anses_26f486
    - Operacion_acreditacion_de_fondos_en_cuentas_de_corresponsalia_df1e9d
    - Operacion_acreditacion_de_fondos_en_cuentas_locales_332567
    - Operacion_acreditacion_de_importe_total_de_instrucciones_5b5386
    - Operacion_acreditacion_de_importes_en_el_dia_09b87b
    - Operacion_acreditacion_de_nuevos_beneficios_y_otros_conceptos_3d8eda
    - Operacion_acreditacion_de_resultado_de_liquidacion_de_cambios_en_cuenta_local_cee6ab
    - Operacion_acreditacion_en_cuenta_transitoria_bcra_3eb4fd
    - Operacion_acreditacion_en_cuentas_en_moneda_extranjera_9a83ed
    - Operacion_actividades_realizadas_estructura_compleja_cc68c1
    - Operacion_actuacion_como_agente_de_pago_en_la_republica_argentina_85ef04
    - Operacion_actualizacion_de_saldos_mediante_cer_096e98
    - Operacion_acuerdo_y_desembolso_de_financiaciones_en_pesos_2fc758
    - Operacion_acumulacion_de_cobros_de_exportaciones_de_servicios_b8262c
    - Operacion_acumulacion_de_cobros_de_exportaciones_en_cuentas_82a9da
    - Operacion_acumulacion_de_fondos_en_cuentas_del_exterior_y_o_del_pais_4d42b6
    - Operacion_acumulacion_de_fondos_en_cuentas_exterior_pais_60854b
    - Operacion_adelantos_en_cuenta_corriente_889211
    - Operacion_adhesion_al_rigi_por_vpu_8fe38f
    - Operacion_adhesion_al_servicio_de_debito_automatico_empresa_prestadora_ente_recaudador_e2fd0a
    - Operacion_adhesion_selectiva_a_productos_en_contrato_multiproducto_5e58d8
    - Operacion_administracion_de_central_de_cheques_denunciados_extraviados_sustraidos_adultera_901c1c
    - Operacion_administracion_de_central_de_cheques_rechazados_4daf92
    - Operacion_administracion_de_central_de_cuentacorrentistas_inhabilitados_ebf3d1
    - Operacion_adquisicion_de_bienes_medico_sanitarios_para_donacion_610685
    - Operacion_adquisicion_de_certificados_de_depositos_argentinos_representativos_de_acciones__75deba
    - Operacion_adquisicion_de_tarjetas_de_regalo_exterior_47d17b
    - Operacion_adquisicion_de_titulos_valores_con_liquidacion_extranjera_ecea73
    - Operacion_adquisicion_de_titulos_valores_representativos_de_deuda_privada_emitida_en_juris_c2f3ca
    - Operacion_adquisicion_en_el_pais_de_titulos_valores_emitidos_por_no_residentes_con_liquida_132ccb
    - Operacion_adquisicion_joyas_piedras_preciosas_metales_df6ba7
    - Operacion_adquisicion_titulos_valores_suscripcion_primaria_dc707d
    - Operacion_adquisiciones_de_entidades_financieras_fc4c7a
    - Operacion_adulteracion_de_cheques_d78211
    - Operacion_adulteracion_de_cheques_y_documentos_2e1d01
    - Operacion_adulteracion_o_falsificacion_de_cheque_o_firmas_8a9da9
    - Operacion_afectacion_de_importaciones_por_solicitud_particular_o_courier_aaee67
    - Operacion_afectacion_de_oficializacion_a_pago_con_ingreso_aduanero_pendiente_39858a
    - Operacion_afectacion_de_registro_aduanero_oficializacion_importacion_sepaimpo_429942
    - Operacion_aforo_de_activos_recibidos_en_garantia_7fd8c6
    - Operacion_agregado_de_hojas_para_transmision_garantia_7bae64
    - Operacion_agrupacion_de_adicionales_por_entidad_derivados_de_credito_9c298a
    - Operacion_agrupacion_de_financiaciones_comerciales_con_creditos_consumo_vivienda_18c542
    - Operacion_agrupamiento_de_financiaciones_comerciales_con_creditos_de_consumo_o_vivienda_0f2001
    - Operacion_ajuste_de_valores_corrientes_posiciones_menos_liquidas_ea4042
    - Operacion_ajuste_de_valuacion_productos_complejos_ce7239
    - Operacion_alquiler_de_cajas_de_seguridad_9f7062
    - Operacion_alteracion_de_tasas_comisiones_y_cargos_9853cf
    - Operacion_analisis_y_modificacion_de_clasificacion_de_deudor_eb956c
    - Operacion_anticipo_de_exportacion_documentado_en_moneda_de_destino_6f7be4
    - Operacion_anticipo_de_exportaciones_de_bienes_liquidado_d62044
    - Operacion_anticipo_por_pago_de_jubilaciones_y_pensiones_76070c
    - Operacion_anticipos_al_fondo_de_garantia_depositos_df1acb
    - Operacion_anticipos_cursados_por_sml_a_partir_02_09_19_2883e1
    - Operacion_anticipos_de_efectivo_agente_de_pago_titulizacion_c89e6c
    - Operacion_anticipos_y_prefinanciaciones_de_exportacion_5d8ce2
    - Operacion_anticipos_y_prefinanciaciones_de_exportaciones_del_exterior_109801
    - Operacion_apertura_de_cuenta_a_agrupaciones_politicas_aliadas_64bc0b
    - Operacion_apertura_de_cuenta_corriente_39abbe
    - Operacion_apertura_de_cuenta_corriente_bancaria_8effda
    - Operacion_apertura_de_cuentas_a_la_vista_443444
    - Operacion_apertura_de_cuentas_componentes_o_representantes_legales_cec9a6
    - Operacion_apertura_de_cuentas_no_presencial_64eef3
    - Operacion_apertura_de_cuentas_por_personas_inhabilitadas_f25a52
    - Operacion_apertura_no_presencial_cuenta_personas_juridicas_fc2329
    - Operacion_apertura_no_presencial_de_cuentas_electronicas_d2b308
    - Operacion_aplicacion_cobros_exportaciones_servicios_6b5107
    - Operacion_aplicacion_de_ajuste_delta_regulatorio_21f0c4
    - Operacion_aplicacion_de_calificacion_a_creditos_quirografarios_7f28db
    - Operacion_aplicacion_de_capacidad_de_prestamo_de_depositos_04d844
    - Operacion_aplicacion_de_capacidad_de_prestamo_en_me_a_importaciones_4d39c5
    - Operacion_aplicacion_de_divisas_a_operaciones_de_exportacion_3551f1
    - Operacion_aplicacion_de_divisas_a_operaciones_de_financiacion_d4996b
    - Operacion_aplicacion_de_divisas_de_anticipos_a_cancelacion_de_prefinanciaciones_0ac48e
    - Operacion_aplicacion_de_divisas_de_cobros_a_cancelacion_de_vencimientos_16a6b1
    - Operacion_aplicacion_de_divisas_de_cobros_cancelacion_de_vencimientos_5f020e
    - Operacion_aplicacion_de_divisas_de_exportacion_de_bienes_e85f19
    - Operacion_aplicacion_de_divisas_para_cobros_exportacion_741268
    - Operacion_aplicacion_de_divisas_por_cobros_exportaciones_cancelacion_deuda_86d9a9
    - Operacion_aplicacion_de_evaluacion_de_credito_de_alta_calidad_8ad920
    - Operacion_aplicacion_de_factor_de_volatilidad_edec25
    - Operacion_aplicacion_de_fondos_en_moneda_extranjera_contra_moneda_local_d06ca7
    - Operacion_aplicacion_de_ponderador_de_baja_calificacion_aa9c74
    - Operacion_aplicacion_de_recursos_propios_liquidos_193f03
    - Operacion_aplicacion_de_tecnica_activos_como_garantia_d99e7a
    - Operacion_aplicacion_de_tecnicas_de_cobertura_del_riesgo_de_credito_2c4eb9
    - Operacion_aplicacion_de_tratamiento_sector_publico_no_financiero_de0171
    - Operacion_aplicacion_divisas_cancelacion_servicios_prestamo_cd43c8
    - Operacion_aplicacion_factor_conversion_crediticia_3d81e8
    - Operacion_aplicacion_financiamiento_instrumentos_deuda_tesoro_e1881e
    - Operacion_aplicacion_metodologia_estandar_a_equivalente_delta_71629e
    - Operacion_aplicacion_ponderador_riesgo_contraparte_6afcd2
    - Operacion_aplicacion_tasas_en_operaciones_de_financiacion_2d942c
    - Operacion_aportacion_a_agrupaciones_politicas_o_fondo_partidario_929d1c
    - Operacion_aporte_de_inversion_extranjera_directa_b244ff
    - Operacion_aportes_de_capital_en_efectivo_c56c6c
    - Operacion_aprobacion_de_operaciones_y_nuevos_productos_b2cfdd
    - Operacion_arbitraje_sin_debito_de_moneda_extranjera_81bbd5
    - Operacion_arbitraje_sin_transferencia_al_exterior_9a73b4
    - Operacion_arrendamiento_financiero_leasing_4ad213
    - Operacion_arrendamientos_financieros_da0039
    - Operacion_aseguramiento_de_instrumentos_en_ca_ac2fcc
    - Operacion_asentamiento_en_rccr_consultas_y_reclamos_dac9bf
    - Operacion_asignacion_a_bandas_temporales_posiciones_delta_deuda_interes_0b6387
    - Operacion_asignacion_aporte_fondo_garantia_por_subcuenta_8cb4ed
    - Operacion_asignacion_de_calificaciones_crediticias_b1543f
    - Operacion_asignacion_de_calificaciones_ecai_a_ponderadores_0a94a2
    - Operacion_asignacion_de_derivados_sobre_bases_a_conjuntos_especificos_cf4333
    - Operacion_asignacion_de_derivados_sobre_volatilidad_a_conjuntos_especificos_46739e
    - Operacion_asignacion_de_exposicion_al_grado_c_d3e41a
    - Operacion_asignacion_de_niveles_de_calidad_crediticia_eaf388
    - Operacion_asignacion_de_ponderador_de_riesgo_a_exposiciones_en_moneda_extranjera_e98b52
    - Operacion_asignacion_de_ponderadores_a_exposiciones_10e9f3
    - Operacion_asignacion_margen_inicial_integrado_a_exposiciones_d7529f
    - Operacion_asignacion_perdidas_definitiva_mecanismo_quita_bb18bf
    - Operacion_asistencia_crediticia_otorgada_en_el_mes_ba9f08
    - Operacion_asistencia_financiera_a_personas_vinculadas_1a702c
    - Operacion_asuncion_de_pago_futuro_por_garante_1dd3d0
    - Operacion_atencion_a_usuarios_con_discapacidad_auditiva_del_habla_466303
    - Operacion_atencion_de_cheques_al_cobro_0499c7
    - Operacion_atencion_de_cheques_con_defecto_formal_cantidad_4410a3
    - Operacion_atencion_de_financiaciones_con_fondos_de_lineas_asignadas_47b8c8
    - Operacion_auditoria_externa_conclusion_sobre_estados_financieros_8b1e58
    - Operacion_aumento_exportaciones_bienes_2023_077a4f
    - Operacion_autoaseguramiento_riesgos_fallecimiento_invalidez_f87002
    - Operacion_autorizacion_de_sobregiro_en_cuenta_corriente_bancaria_3a2586
    - Operacion_aval_de_cheque_pago_diferido_por_banco_87123d
    - Operacion_avales_sobre_cheques_de_pago_diferido_982cee
    - Operacion_bloqueo_o_inhabilitacion_de_productos_servicios_por_seguridad_c2714c
    - Operacion_boleto_compra_a19_aplicacion_fondos_dccc99
    - Operacion_boleto_de_cambio_de_venta_importaciones_bc5385
    - Operacion_boleto_de_compra_venta_de_cambio_988448
    - Operacion_boleto_de_compra_y_o_venta_de_cambio_54c880
    - Operacion_boleto_de_venta_con_constancia_de_pago_de_fletes_1b1f21
    - Operacion_boleto_de_venta_de_cambio_adjudicacion_bonos_bopreal_2b2b24
    - Operacion_boleto_de_venta_de_cambio_bopreal_8e69da
    - Operacion_boleto_de_venta_de_cambio_para_utilidades_9bf919
    - Operacion_boleto_de_venta_de_cambio_por_bonos_bopreal_073365
    - Operacion_boleto_garantias_exportaciones_bienes_servicios_63ec95
    - Operacion_boleto_venta_cancelacion_servicio_deuda_fe1228
    - Operacion_calculo_activos_ponderados_por_riesgo_bc1489
    - Operacion_calculo_comparativo_fob_anos_t_y_t_1_c71712
    - Operacion_calculo_cr_operaciones_con_margen_variacion_b6bfc5
    - Operacion_calculo_cr_operaciones_sin_margen_variacion_491247
    - Operacion_calculo_de_activos_ponderados_por_riesgo_64a8bb
    - Operacion_calculo_de_adicional_para_derivados_de_tasa_de_interes_e97c1b
    - Operacion_calculo_de_adicional_para_derivados_de_tipo_de_cambio_8a965b
    - Operacion_calculo_de_compensacion_a_nivel_de_entidad_derivados_de_credito_497337
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_credito_3430df
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_mercado_6f686a
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_tasa_bandas_de_plazo_0c39e5
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_tipo_de_cambio_6c7e1d
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_especifico_de_emisor_d04ead
    - Operacion_calculo_de_exigencia_por_riesgo_de_credito_00b696
    - Operacion_calculo_de_exigencia_riesgo_general_tasa_interes_0f47e7
    - Operacion_calculo_de_exigencias_capital_riesgo_tasa_interes_468b15
    - Operacion_calculo_de_exposicion_ajustada_por_crc_8ce3eb
    - Operacion_calculo_de_exposicion_riesgo_tipo_de_cambio_tasa_0ed0d3
    - Operacion_calculo_de_factor_plazo_por_tipo_de_operacion_05047d
    - Operacion_calculo_de_intereses_sobre_capital_en_pesos_423bab
    - Operacion_calculo_de_nocional_ajustado_para_derivados_fx_294149
    - Operacion_calculo_de_nocional_ajustado_para_derivados_sobre_acciones_y_commodities_cfac6f
    - Operacion_calculo_de_nocional_efectivo_para_derivados_fx_469b46
    - Operacion_calculo_de_nocional_efectivo_por_banda_temporal_tasa_de_interes_cde4a1
    - Operacion_calculo_de_posicion_neta_total_8e39af
    - Operacion_calculo_de_previsiones_regulatorias_373550
    - Operacion_calculo_de_previsiones_sobre_tenencias_3b7c91
    - Operacion_calculo_de_rpc_mediante_inclusion_diferencia_prevision_niif_9_11f33d
    - Operacion_calculo_de_tasa_de_interes_efectiva_anual_142d89
    - Operacion_calculo_de_tipos_de_cambio_minoristas_de_referencia_afb412
    - Operacion_calculo_de_vu_opciones_sobre_acciones_indices_oro_divisas_8492ab
    - Operacion_calculo_de_vu_opciones_sobre_tasas_bonos_86e1a3
    - Operacion_calculo_del_activo_ponderado_por_riesgo_24c877
    - Operacion_calculo_del_bi_a_nivel_consolidado_cfa5fc
    - Operacion_calculo_del_bi_a_nivel_individual_813f8f
    - Operacion_calculo_del_bi_a_nivel_subconsolidado_4253dc
    - Operacion_calculo_del_costo_financiero_total_4df7e7
    - Operacion_calculo_del_indicador_de_negocio_bi_a56544
    - Operacion_calculo_delta_neto_opciones_oro_monedas_b3d553
    - Operacion_calculo_e_informacion_del_bic_2e706c
    - Operacion_calculo_ead_derivados_con_sa_ccr_edb20f
    - Operacion_calculo_ead_por_netting_set_6628f0
    - Operacion_calculo_ead_sft_24acd4
    - Operacion_calculo_epf_operaciones_con_margen_variacion_9ef918
    - Operacion_calculo_epf_operaciones_sin_margen_variacion_627247
    - Operacion_calculo_equivalente_delta_metodo_delta_plus_ac03f4
    - Operacion_calculo_eve0_valor_economico_escenario_base_f54a0d
    - Operacion_calculo_eve_estandarizada_6af9d5
    - Operacion_calculo_eve_valor_economico_del_patrimonio_2900c8
    - Operacion_calculo_excedente_atribuible_accionistas_minoritarios_347688
    - Operacion_calculo_exigencia_capital_exposiciones_ccp_no_calificadas_7cf1a6
    - Operacion_calculo_exigencia_capital_minimo_riesgo_operacional_14fce4
    - Operacion_calculo_exigencia_capital_opciones_129ee8
    - Operacion_calculo_exigencia_capital_riesgo_de_tasa_interes_ef04b8
    - Operacion_calculo_exigencia_capital_riesgo_operacional_mes_1_f92a63
    - Operacion_calculo_exigencia_capital_riesgo_operacional_mes_37_en_adelante_4798fb
    - Operacion_calculo_exigencia_capital_riesgo_operacional_meses_2_a_36_b100fb
    - Operacion_calculo_exigencia_de_capital_minimo_por_riesgo_operacional_dc3acb
    - Operacion_calculo_exigencia_por_riesgo_general_de_tasa_7d9295
    - Operacion_calculo_exigencia_riesgo_de_mercado_base_individual_consolidado_4b7110
    - Operacion_calculo_exigencia_riesgo_de_mercado_posiciones_ultimo_dia_19731f
    - Operacion_calculo_exigencia_riesgo_posiciones_opciones_4515fd
    - Operacion_calculo_flujos_fondos_netos_2c5025
    - Operacion_calculo_importe_reconocido_capital_ordinario_306d10
    - Operacion_calculo_kao_opciones_automaticas_sobre_tasas_2c4a1a
    - Operacion_calculo_limite_concentracion_exposiciones_22a237
    - Operacion_calculo_maxima_perdida_posible_posicion_comprada_ff0fae
    - Operacion_calculo_maxima_perdida_posible_posicion_vendida_50432c
    - Operacion_calculo_requerimiento_capital_hipotetico_ccp_a72ae4
    - Operacion_calculo_riesgo_tasa_interes_cartera_eve_estandarizada_9d4104
    - Operacion_calculo_riesgo_tasa_interes_cartera_inversion_eve_c5ebb8
    - Operacion_calculo_suma_perdidas_agregacion_por_escenario_a86e1b
    - Operacion_calculo_total_exigencia_riesgo_tasa_especifico_80231e
    - Operacion_calculo_variacion_eve_resta_escenarios_8342a5
    - Operacion_calculo_y_pago_de_intereses_2bb65e
    - Operacion_calificacion_crediticia_por_ecai_2951e6
    - Operacion_calificacion_de_deudor_10a6b6
    - Operacion_cambio_de_clave_pin_por_usuario_b70e3c
    - Operacion_cambio_de_domicilio_o_correo_contacto_e6f6ad
    - Operacion_canalizacion_de_operaciones_sml_3daa7e
    - Operacion_canalizacion_mediante_compraventa_de_titulos_valores_f89e00
    - Operacion_cancelacion_al_exterior_de_deudas_no_comerciales_de_importacion_b39ff5
    - Operacion_cancelacion_al_vencimiento_de_endeudamientos_financieros_9a5961
    - Operacion_cancelacion_capital_e_intereses_endeudamiento_financiero_exterior_5579c2
    - Operacion_cancelacion_capital_e_intereses_endeudamientos_6c4f2b
    - Operacion_cancelacion_cartas_credito_letras_avaladas_garantizando_importaciones_26be92
    - Operacion_cancelacion_consumos_tarjeta_extranjera_3b537d
    - Operacion_cancelacion_de_anticipos_de_exportacion_con_fondos_de_cobros_350dc7
    - Operacion_cancelacion_de_autorizaciones_para_girar_a26106
    - Operacion_cancelacion_de_capital_e_intereses_endeudamiento_financiero_8fe0b6
    - Operacion_cancelacion_de_capital_e_intereses_endeudamientos_financieros_ef116a
    - Operacion_cancelacion_de_capital_intereses_con_divisas_28e145
    - Operacion_cancelacion_de_consumos_en_moneda_extranjera_895150
    - Operacion_cancelacion_de_deuda_por_operacion_financiada_2f6d75
    - Operacion_cancelacion_de_deudas_por_operaciones_financiadas_internacionales_077563
    - Operacion_cancelacion_de_endeudamientos_financieros_a3eaa6
    - Operacion_cancelacion_de_financiaciones_en_moneda_extranjera_669f07
    - Operacion_cancelacion_de_garantias_comerciales_importaciones_5fd9dd
    - Operacion_cancelacion_de_garantias_importaciones_de_bienes_fd33e7
    - Operacion_cancelacion_de_lineas_de_credito_financiacion_comercio_exterior_24e83e
    - Operacion_cancelacion_de_lineas_de_credito_importaciones_de_bienes_6059ed
    - Operacion_cancelacion_de_multas_por_rechazos_41dbce
    - Operacion_cancelacion_de_servicios_de_capital_e_intereses_f6c6e7
    - Operacion_cancelacion_de_servicios_de_titulos_valores_a5f346
    - Operacion_cancelacion_del_capital_de_financiacion_4d8439
    - Operacion_cancelacion_deudas_comerciales_importacion_bienes_b3c635
    - Operacion_cancelacion_en_pais_vencimiento_capital_e_intereses_93e620
    - Operacion_canje_de_moneda_extranjera_por_pen_a2b943
    - Operacion_canje_de_titulos_valores_emitidos_por_residentes_por_activos_externos_d36ef3
    - Operacion_canje_y_arbitraje_con_clientes_2e4818
    - Operacion_canje_y_o_arbitraje_bopreal_755b55
    - Operacion_canje_y_o_arbitraje_con_fondos_en_moneda_extranjera_79af90
    - Operacion_canje_y_o_arbitraje_fondos_bopreal_325782
    - Operacion_canjes_de_instrumentos_cambios_8aec4e
    - Operacion_canjes_y_arbitrajes_con_clientes_4a86e3
    - Operacion_canjes_y_arbitrajes_con_clientes_ingresos_divisas_exterior_213553
    - Operacion_capacitacion_y_entrenamiento_de_ejecutivos_y_directivos_20f15b
    - Operacion_capitalizacion_depositos_e_intermediacion_financiera_0aadd6
    - Operacion_ccf_100_compromisos_de_adquisicion_de_activos_7b64fc
    - Operacion_ccf_100_sustitutos_crediticios_directos_e8777c
    - Operacion_ccf_100_ventas_de_activos_con_recompra_94b55c
    - Operacion_ccf_10_compromisos_cancelables_discrecional_dca238
    - Operacion_ccf_20_cartas_de_credito_comercial_corto_plazo_60a604
    - Operacion_ccf_40_lineas_de_credito_comprometidas_0a7f01
    - Operacion_ccf_50_lineas_de_emision_de_titulos_nif_ruf_d74f48
    - Operacion_ccf_50_partidas_contingentes_comerciales_89bd5a
    - Operacion_celebracion_de_acuerdos_sobre_prelacion_en_cobro_7804fa
    - Operacion_certificacion_cumplimiento_elegibilidad_proyecto_916f86
    - Operacion_certificacion_de_afectacion_en_sepaimpo_97dd5c
    - Operacion_certificacion_de_aplicacion_de_divisas_a_cancelacion_35793d
    - Operacion_certificacion_de_aplicacion_pago_de_dividendos_ff7b1b
    - Operacion_certificacion_de_beneficios_decreto_277_22_utilizados_por_cliente_70652f
    - Operacion_certificacion_de_cheque_3c9fac
    - Operacion_certificacion_de_incumplido_en_gestion_de_cobro_3e809f
    - Operacion_certificacion_de_vinculacion_de_exportaciones_a_proyecto_aprobado_808813
    - Operacion_certificacion_emitida_por_entidad_liquidadora_sobre_no_emision_de_certificacione_6603cf
    - Operacion_cesion_sin_recurso_en_entidad_del_exterior_c93d89
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
    - Operacion_clasificacion_de_deudor_con_insolvencia_5e1b78
    - Operacion_clasificacion_de_deudores_82042f
    - Operacion_clasificacion_de_deudores_por_mora_5d5ac5
    - Operacion_clasificacion_de_deudores_por_sgr_y_fondos_de_garantia_c74cac
    - Operacion_clasificacion_de_deudores_segun_mora_595d13
    - Operacion_clasificacion_de_exposiciones_a_instrumentos_b2dd92
    - Operacion_clasificacion_deudores_creditos_fideicomitidos_2c30f7
    - Operacion_clasificacion_en_categoria_alto_riesgo_de_insolvencia_1adb85
    - Operacion_clasificacion_en_grupo_1_o_grupo_2_7315bb
    - Operacion_clasificacion_titulos_publicos_rendimiento_dual_179b67
    - Operacion_cobertura_de_pagos_por_garantia_b508c3
    - Operacion_cobertura_del_riesgo_de_credito_en_evaluacion_de_emision_d06438
    - Operacion_cobertura_mediante_activos_admitidos_como_garantia_bbfa32
    - Operacion_cobranza_anticipada_de_exportacion_de_bienes_6d7e86
    - Operacion_cobro_comision_y_cargo_operaciones_a8e152
    - Operacion_cobro_comisiones_cargos_seguros_saldo_deudor_423c45
    - Operacion_cobro_de_comisiones_por_reporte_de_circunstancias_3c02ce
    - Operacion_cobro_de_comisiones_y_cargos_a_usuarios_acccac
    - Operacion_cobro_de_exportacion_con_demostracion_de_gestion_sin_gestion_judicial_c4a227
    - Operacion_cobro_de_exportacion_de_bienes_con_liquidacion_en_mercado_7ce7b2
    - Operacion_cobro_de_exportacion_de_servicios_por_persona_humana_2884d8
    - Operacion_cobro_de_exportacion_documentado_en_moneda_de_destino_eb0227
    - Operacion_cobro_de_exportaciones_de_bienes_o_servicios_e15530
    - Operacion_cobro_de_exportaciones_de_bienes_y_servicios_b612da
    - Operacion_cobro_de_exportaciones_regimen_fomento_decreto_234_21_8776a6
    - Operacion_cobro_de_utilidades_y_dividendos_desde_01_09_19_c5637e
    - Operacion_cobro_en_divisas_por_exportacion_de_bienes_ebe7d2
    - Operacion_cobro_exportacion_bienes_exceptuado_5c2aa2
    - Operacion_cobro_exportaciones_bienes_beneficiarios_economia_conocimiento_875a70
    - Operacion_cobro_local_por_exportacion_3425c3
    - Operacion_cobro_servicios_no_conexos_sml_paraguay_y_uruguay_d5db45
    - Operacion_cobros_de_exportaciones_de_bienes_73b35d
    - Operacion_cobros_de_exportaciones_de_bienes_en_proyectos_de_inversion_04be00
    - Operacion_cobros_de_exportaciones_de_servicios_economia_conocimiento_8052da
    - Operacion_cobros_elegibles_mecanismo_7_10_depositados_17536a
    - Operacion_cobros_exportaciones_bienes_6a95b1
    - Operacion_cobros_exportaciones_bienes_mercado_de_cambios_7557be
    - Operacion_cobros_exportaciones_de_bienes_cc7695
    - Operacion_cobros_locales_por_exportaciones_a_medios_transporte_bandera_extranjera_6c6fcc
    - Operacion_cobros_por_siniestros_de_cobertura_exportacion_d9a434
    - Operacion_cobros_turismo_internacional_no_residentes_43a4fc
    - Operacion_comercio_exterior_directo_9f55d2
    - Operacion_compensacion_de_componentes_sistematicos_derivados_de_credito_6ff74a
    - Operacion_compensacion_entre_tipos_de_commodities_dentro_de_conjunto_8e77d6
    - Operacion_compensacion_parcial_correlacion_negativa_94780b
    - Operacion_compensacion_posiciones_compradas_vendidas_47f747
    - Operacion_compensaciones_horizontales_posiciones_netas_ee4986
    - Operacion_composicion_de_cuadernos_cheques_comunes_y_diferidos_70e3e1
    - Operacion_compra_de_bienes_revendidos_al_exterior_sin_paso_por_pais_5d9310
    - Operacion_compra_de_cartera_creditos_6cef4a
    - Operacion_compra_de_cartera_creditos_minoristas_930297
    - Operacion_compra_de_fondos_y_pago_de_bonos_bopreal_e25e97
    - Operacion_compra_de_instrumentos_93181f
    - Operacion_compra_de_instrumentos_para_pnc_11f556
    - Operacion_compra_de_moneda_extranjera_4818a4
    - Operacion_compra_de_moneda_extranjera_anticipada_44812f
    - Operacion_compra_de_moneda_extranjera_con_debito_cuenta_local_cf9764
    - Operacion_compra_de_moneda_extranjera_con_tarjeta_de_compra_cb3e92
    - Operacion_compra_de_moneda_extranjera_con_tarjeta_de_credito_dde703
    - Operacion_compra_de_moneda_extranjera_con_tarjeta_prepaga_79aa43
    - Operacion_compra_de_moneda_extranjera_garantia_de_servicios_de_deuda_externa_fd8f7c
    - Operacion_compra_de_moneda_extranjera_garantias_de_endeudamiento_c1cc9d
    - Operacion_compra_de_moneda_extranjera_para_garantias_6f3257
    - Operacion_compra_de_obligaciones_negociables_de_emision_propia_b51c73
    - Operacion_compra_moneda_extranjera_clientes_no_residentes_161194
    - Operacion_compra_moneda_extranjera_para_garantias_8e8d15
    - Operacion_compra_o_cesion_de_financiaciones_7c0f78
    - Operacion_compra_titulos_valores_mercado_secundario_4d0bef
    - Operacion_compra_venta_moneda_extranjera_en_caracter_de_cliente_c40d38
    - Operacion_compra_y_venta_de_contratos_de_opciones_e7649e
    - Operacion_compras_en_cuotas_de_pasajes_al_exterior_22570e
    - Operacion_compraventa_titulos_valores_con_liquidacion_moneda_extranjera_y_venta_moneda_loc_6d946b
    - Operacion_compraventa_titulos_valores_liquidacion_moneda_extranjera_ca0b73
    - Operacion_comprobacion_de_rechazo_de_cheque_07ba39
    - Operacion_compromiso_de_presentacion_dentro_de_365_dias_desde_inicio_de_tramite_87f530
    - Operacion_computo_como_capital_participaciones_minoritarias_consolidadas_331b1c
    - Operacion_computo_de_aportes_en_especie_en_mercado_cambios_13689b
    - Operacion_computo_de_exigencia_capital_por_riesgo_credito_eb9eaf
    - Operacion_computo_de_exigencia_de_capital_por_riesgo_de_credito_de_contraparte_eeacd7
    - Operacion_computo_exigencia_capital_derivados_acciones_6fc56f
    - Operacion_computo_exposicion_total_bruta_229ef1
    - Operacion_computo_exposiciones_dolar_linked_0ec467
    - Operacion_computo_resultado_positivo_ultimo_ejercicio_8e5c8a
    - Operacion_comunicacion_al_bcra_de_rechazos_de_cheques_f94818
    - Operacion_comunicacion_al_bcra_de_rechazos_f744de
    - Operacion_comunicacion_de_clasificacion_de_deudor_a_cliente_4b4635
    - Operacion_comunicacion_de_modificacion_baja_de_rechazo_al_bcra_39db45
    - Operacion_comunicacion_de_rechazo_al_tenedor_1fe229
    - Operacion_comunicacion_de_saldo_al_cuentacorrentista_fae6f0
    - Operacion_comunicacion_fehaciente_de_certificaciones_emitidas_9294e5
    - Operacion_comunicacion_inmediata_de_contingencia_743b3d
    - Operacion_comunicacion_rechazo_al_bcra_189044
    - Operacion_comunicacion_rechazo_al_librador_y_avalistas_bd21f6
    - Operacion_concertacion_de_cambio_sobre_fondos_acreditados_572532
    - Operacion_concertacion_de_titulos_valores_en_el_pais_28bf13
    - Operacion_condonacion_de_deuda_del_acreedor_a4900a
    - Operacion_confeccion_boleto_cambio_a19_depositos_191124
    - Operacion_confeccion_boletos_de_cambio_a_nombre_propio_89711d
    - Operacion_confeccion_de_boleto_de_venta_importaciones_de_bienes_22aefb
    - Operacion_confeccion_de_boletos_sin_movimiento_de_pesos_aff787
    - Operacion_consideracion_de_exportacion_no_generadora_de_contravalor_aa8b22
    - Operacion_consideracion_de_incidencia_de_grupo_de_contrapartes_conectadas_90abc8
    - Operacion_consideracion_de_instrumentos_cer_a_tasa_fija_3131fc
    - Operacion_consignacion_de_denominacion_de_cuenta_en_rechazo_259e1a
    - Operacion_consignacion_de_informacion_al_dorso_de_cheques_d59483
    - Operacion_consignacion_del_motivo_de_rechazo_del_cheque_88379f
    - Operacion_consignacion_en_partida_60500000_para_neutralizacion_88ccaa
    - Operacion_consignacion_exigencia_riesgo_especifico_tasa_interes_848889
    - Operacion_consignacion_exigencia_riesgo_general_acciones_b1e838
    - Operacion_consignacion_judicial_de_cheques_rechazados_d33e1b
    - Operacion_consignacion_judicial_del_importe_de_multa_b1005b
    - Operacion_consolidacion_de_bases_para_capitales_minimos_e28adb
    - Operacion_consolidacion_de_posiciones_en_sucursales_y_subsidiarias_a1eedc
    - Operacion_constatacion_de_certificado_de_inversion_para_exportacion_12ea40
    - Operacion_constitucion_del_legajo_del_deudor_85a6d2
    - Operacion_consulta_del_regimen_de_transparencia_dd23cd
    - Operacion_contratacion_de_productos_y_servicios_a_distancia_115307
    - Operacion_contratacion_de_seguros_accesorios_a_servicios_financieros_32d06e
    - Operacion_contratacion_seguro_sobre_saldo_deudor_7a0636
    - Operacion_contrato_a_termino_de_moneda_oro_ba0b0b
    - Operacion_convenio_de_pago_por_concordato_o_arreglo_privado_816f60
    - Operacion_conversion_de_compromisos_en_equivalentes_crediticios_3664b4
    - Operacion_conversion_de_moneda_extranjera_a_pesos_34693e
    - Operacion_conversion_de_posicion_neta_a_pesos_1b3591
    - Operacion_conversion_de_swaps_apalancados_a_nocionales_no_apalancados_2483aa
    - Operacion_conversion_instrumento_en_acciones_ordinarias_06ff00
    - Operacion_correccion_de_problemas_identificados_d1152f
    - Operacion_creacion_de_cheque_con_firmas_multiples_ba7ce5
    - Operacion_crecimiento_de_depositos_c29e52
    - Operacion_credito_adicional_post_refinanciacion_91d562
    - Operacion_credito_por_internet_e0963d
    - Operacion_credito_por_orden_telefonica_f7e811
    - Operacion_credito_por_transferencia_electronica_b5597b
    - Operacion_creditos_a_residentes_exterior_desfases_de_liquidacion_2e3633
    - Operacion_creditos_documentarios_853778
    - Operacion_creditos_documentarios_utilizados_pago_diferido_da2551
    - Operacion_creditos_frente_al_bcra_7476b8
    - Operacion_creditos_internos_en_cuentas_c1e98d
    - Operacion_creditos_por_arrendamientos_financieros_72a28a
    - Operacion_creditos_vivienda_propia_compra_construccion_o_refaccion_9bef1a
    - Operacion_cuantificacion_de_exposicion_por_moneda_320d78
    - Operacion_cuentas_a_la_vista_en_bancos_del_exterior_ca97e1
    - Operacion_cuentas_corrientes_y_especiales_en_bcra_6c80a4
    - Operacion_cuentas_de_corresponsalia_en_bancos_del_exterior_1335da
    - Operacion_cumplido_de_embarque_permiso_definitivo_c6d27a
    - Operacion_cumplimiento_de_requerimientos_legajo_unico_financiero_y_economico_df59a6
    - Operacion_cumplimiento_parcial_total_seguimiento_permiso_embarque_7dc5c0
    - Operacion_cumplimiento_seguimiento_exportacion_decreto_929_13_07516a
    - Operacion_cursamiento_de_cheque_a_entidad_girada_2aad10
    - Operacion_custodia_de_titulos_representativos_de_inversiones_a2192e
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
    - Operacion_declaracion_de_incumplimiento_y_liquidacion_de_garantia_be62c9
    - Operacion_declaracion_de_operacion_en_relevamiento_1917ae
    - Operacion_declaracion_de_operacion_en_relevamiento_de_activos_y_pasivos_externos_0449d7
    - Operacion_declaracion_jurada_cliente_activos_externos_liquidos_f1daa9
    - Operacion_deduccion_de_importes_de_activos_de_rpc_5f0068
    - Operacion_deduccion_de_titulos_de_gobiernos_extranjeros_33fe07
    - Operacion_defectos_de_aplicacion_netos_en_efectivo_cba64e
    - Operacion_delegacion_de_actividades_en_terceros_1a17eb
    - Operacion_demas_posiciones_de_titulizacion_fuera_de_balance_1048e4
    - Operacion_denuncia_de_extravio_sustraccion_o_adulteracion_f08c5d
    - Operacion_denuncia_de_incumplido_permiso_30291e
    - Operacion_deposito_al_bcra_en_pesos_fuente_de_fondos_en_pesos_438fe7
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
    - Operacion_deposito_fondos_en_cuentas_exterior_844127
    - Operacion_deposito_por_transferencia_ordenada_por_entidad_4dc733
    - Operacion_deposito_u_operacion_con_echeq_ca293f
    - Operacion_depositos_a_plazo_fijo_en_entidades_del_exterior_494e61
    - Operacion_depositos_en_cuenta_especial_de_regularizacion_monedas_extranjeras_dc971c
    - Operacion_depositos_en_cuentas_especiales_financiacion_de_exportaciones_95e322
    - Operacion_depositos_en_moneda_extranjera_financiacion_28cc03
    - Operacion_depositos_mediante_cajeros_automaticos_273683
    - Operacion_depositos_plazo_riesgo_retiro_anticipado_bab2db
    - Operacion_depositos_por_ventanilla_o_cajeros_automaticos_49464d
    - Operacion_derivado_otc_261a55
    - Operacion_derivados_de_credito_cobertura_de_obligaciones_63a309
    - Operacion_desarrollo_aplicacion_reproduccion_firmas_digitalizadas_cbee12
    - Operacion_descubiertos_en_cuenta_corriente_a47c89
    - Operacion_descuento_de_operacion_en_entidad_exterior_f4c930
    - Operacion_desembolso_en_divisas_por_financiacion_exterior_47f602
    - Operacion_desembolsos_de_fondos_financiacion_20c454
    - Operacion_desembolsos_en_divisas_para_importaciones_bb410c
    - Operacion_desembolsos_simultaneos_por_mercado_de_cambios_a9531e
    - Operacion_designacion_de_entidad_financiera_local_5c7ab3
    - Operacion_designacion_de_entidad_financiera_local_seguimiento_operacion_exportacion_6657ee
    - Operacion_destinaciones_suspensivas_exportaciones_temporarias_969431
    - Operacion_deteccion_de_transferencias_con_informacion_incompleta_c647cd
    - Operacion_determinacion_cva_ajuste_de_valuacion_credito_e1bdd2
    - Operacion_determinacion_de_la_rpc_en_fusion_6e4bdd
    - Operacion_determinacion_de_nocional_para_operaciones_sin_nocional_claramente_definido_ac6464
    - Operacion_determinacion_de_ponderadores_de_riesgo_e2260f
    - Operacion_determinacion_de_responsabilidad_patrimonial_computable_f90837
    - Operacion_determinacion_del_requisito_de_capital_52da79
    - Operacion_determinacion_diaria_integracion_capital_74f137
    - Operacion_determinacion_ead_contraparte_derivados_344877
    - Operacion_determinacion_excedente_capital_ordinario_9c2a28
    - Operacion_determinacion_exigencia_capital_riesgo_credito_3d2a1e
    - Operacion_determinacion_exigencia_riesgo_de_mercado_a00f32
    - Operacion_determinacion_exigencia_riesgo_mercado_calculo_maximo_c87cbb
    - Operacion_determinacion_importe_posicion_abierta_neta_moneda_2b051d
    - Operacion_determinacion_incluso_exclusion_cartera_negociacion_817ccc
    - Operacion_determinacion_montos_pendientes_facturacion_en_monedas_distintas_cac557
    - Operacion_determinacion_participacion_maxima_multiples_tramos_e819f0
    - Operacion_determinacion_participacion_maxima_tramo_unico_17c862
    - Operacion_deuda_subordinada_e_instrumentos_de_capital_3caf39
    - Operacion_devolucion_de_chequeras_con_datos_anteriores_84ecf7
    - Operacion_devolucion_de_cheques_a_libradores_dae122
    - Operacion_devolucion_de_echeq_al_librador_por_tenedor_4c6f48
    - Operacion_devolucion_de_fondos_del_exterior_pago_con_registro_aduanero_pendiente_5bfc79
    - Operacion_devolucion_de_operaciones_cursadas_por_sml_432a11
    - Operacion_devolucion_fondos_al_emisor_285a51
    - Operacion_devoluciones_de_pagos_anticipados_f15e84
    - Operacion_direccion_de_actividades_y_negocios_2ce9a7
    - Operacion_diseno_de_nuevos_productos_y_servicios_369a28
    - Operacion_diseno_del_sistema_de_incentivos_economicos_al_personal_56a391
    - Operacion_disponibilidad_de_informacion_sobre_actividades_f2da83
    - Operacion_disponibilidad_publica_de_informacion_sobre_actividades_8e6a11
    - Operacion_distribucion_de_dividendos_en_efectivo_3be1a3
    - Operacion_diversificacion_de_cartera_minorista_889e0d
    - Operacion_division_de_exposicion_entre_tecnicas_crc_b20552
    - Operacion_division_de_riesgo_en_componentes_derivados_sobre_acciones_a95627
    - Operacion_division_de_riesgo_en_componentes_derivados_sobre_commodities_ed6293
    - Operacion_efectivo_pago_del_beneficio_001d45
    - Operacion_egreso_por_mercado_de_cambios_con_regimen_de_acceso_a_divisas_900f82
    - Operacion_egresos_de_fondos_al_exterior_verificacion_de_cuits_dd6b7e
    - Operacion_egresos_por_mercado_de_cambios_e8a13a
    - Operacion_ejercicio_de_opcion_como_respaldo_crediticio_implicito_4f3618
    - Operacion_ejercicio_de_opcion_de_exclusion_e086f2
    - Operacion_elaboracion_de_boleto_global_diario_dcd97f
    - Operacion_elaboracion_de_reportes_atencion_al_usuario_fe26fd
    - Operacion_elaboracion_programas_trabajo_e_informes_auditoria_a402c1
    - Operacion_elaboracion_y_provision_de_nomina_de_deudores_morosos_802e7d
    - Operacion_eliminacion_de_cotitular_de_cuenta_52dbc7
    - Operacion_emision_certificacion_afectacion_sepaimpo_aee1f9
    - Operacion_emision_certificacion_de_aplicacion_capital_e_intereses_60aef5
    - Operacion_emision_certificaciones_acceso_mercado_de_cambios_bba520
    - Operacion_emision_certificaciones_de_aplicacion_de_divisas_7623b4
    - Operacion_emision_certificado_nominativo_transferible_97100d
    - Operacion_emision_cheques_firmas_electronicas_digitalizadas_38a3e1
    - Operacion_emision_cheques_papel_reproduccion_firmas_electronica_8be4d3
    - Operacion_emision_de_cartas_de_credito_adf0c0
    - Operacion_emision_de_certificacion_aumento_exportaciones_bienes_50628f
    - Operacion_emision_de_certificacion_de_cumplido_b96564
    - Operacion_emision_de_certificacion_de_ingreso_y_liquidacion_de_divisas_e7963c
    - Operacion_emision_de_certificacion_por_posfinanciaciones_32f096
    - Operacion_emision_de_certificaciones_acceso_mercado_cambios_2ca44b
    - Operacion_emision_de_certificaciones_aplicacion_divisas_607b72
    - Operacion_emision_de_certificaciones_de_acceso_a_divisas_f9529e
    - Operacion_emision_de_certificaciones_de_acceso_al_mercado_de_cambios_dfbda2
    - Operacion_emision_de_certificaciones_de_aplicacion_de_cobros_d78c73
    - Operacion_emision_de_certificaciones_de_aumento_de_exportaciones_414e35
    - Operacion_emision_de_certificaciones_de_aumento_exportaciones_e1473a
    - Operacion_emision_de_certificaciones_de_divisas_37cc99
    - Operacion_emision_de_certificaciones_detalles_de_seguimiento_d5a48a
    - Operacion_emision_de_certificado_para_ejercicio_de_acciones_civiles_f202a4
    - Operacion_emision_de_cheque_c50f16
    - Operacion_emision_de_cheque_de_pago_diferido_no_registrado_1e40e0
    - Operacion_emision_de_cheque_no_a_la_orden_para_movimiento_de_fondos_e75db2
    - Operacion_emision_de_cheques_6cacff
    - Operacion_emision_de_cheques_comunes_dd9423
    - Operacion_emision_de_cheques_de_pago_diferido_47a688
    - Operacion_emision_de_cheques_en_formato_papel_con_reproduccion_digital_7e191d
    - Operacion_emision_de_cheques_en_pesos_o_usd_143065
    - Operacion_emision_de_cheques_formato_papel_92cd41
    - Operacion_emision_de_cheques_por_personas_inhabilitadas_828f10
    - Operacion_emision_de_constancia_de_consulta_o_reclamo_07991f
    - Operacion_emision_de_constancia_de_operacion_8ad94c
    - Operacion_emision_de_garantia_por_pedido_residente_e0003f
    - Operacion_emision_de_instrumentos_en_pnc_8a0afe
    - Operacion_emision_de_letras_avaladas_3ad992
    - Operacion_emision_de_nota_de_credito_28812a
    - Operacion_emision_de_nota_escrita_con_resolucion_ab54c7
    - Operacion_emision_de_nuevas_acciones_d687a0
    - Operacion_emision_de_titulos_de_deuda_1d989c
    - Operacion_emision_de_titulos_de_deuda_7_11_1_5_y_7_11_1_6_e4e9c4
    - Operacion_emision_de_titulos_de_deuda_con_registro_exterior_e4f3e2
    - Operacion_emision_de_titulos_de_deuda_exterior_registro_pais_acceso_cambios_61b9a9
    - Operacion_emision_de_titulos_de_deuda_post_01_09_19_para_refinanciar_0f67fb
    - Operacion_emision_titulos_deuda_moneda_extranjera_8d61fd
    - Operacion_emision_titulos_deuda_moneda_extranjera_con_registro_publico_2d9c48
    - Operacion_emision_y_cobro_de_cheques_de_pago_diferido_9adeda
    - Operacion_emision_y_entrega_de_formula_de_certificacion_1dd04d
    - Operacion_emision_y_presentacion_de_cheques_1f5d1a
    - Operacion_empleo_de_tecnicas_de_cobertura_operaciones_sinteticas_c2ed8d
    - Operacion_enajenacion_de_activos_no_financieros_no_producidos_fd9001
    - Operacion_encomienda_de_clasificacion_al_sector_de_creditos_f7e0db
    - Operacion_endeudamientos_con_el_exterior_en_moneda_extranjera_7fc030
    - Operacion_endeudamientos_financieros_con_el_exterior_2c221d
    - Operacion_endoso_11ba72
    - Operacion_endoso_a_favor_del_bcra_7d8af7
    - Operacion_endoso_de_cheques_648af4
    - Operacion_endoso_en_echeq_027661
    - Operacion_endoso_para_obtencion_de_financiacion_a381c7
    - Operacion_entrega_copia_dni_al_legajo_f2a1d8
    - Operacion_entrega_de_billetes_o_acreditacion_de_fondos_e91290
    - Operacion_entrega_de_billetes_o_fondos_formacion_de_activos_externos_d08166
    - Operacion_entrega_de_fondos_locales_o_activos_locales_para_recibir_activos_externos_198895
    - Operacion_entrega_de_instrumentos_en_mercado_de_cambios_110541
    - Operacion_entrega_de_tarjetas_magneticas_c89025
    - Operacion_envio_de_informacion_sobre_movimientos_y_cheques_00617c
    - Operacion_envio_partida_39000000_periodo_julio_2015_4091a8
    - Operacion_envios_asistencia_y_salvamento_ley_22_415_95f5fd
    - Operacion_establecimiento_de_comite_lavado_de_activos_y_financiamiento_del_terrorismo_e5c850
    - Operacion_estimacion_de_riesgos_por_combinacion_de_posiciones_1ce95f
    - Operacion_estrategia_de_negociacion_documentada_d1e6fe
    - Operacion_evaluacion_de_capacidad_de_repago_d42960
    - Operacion_evaluacion_de_codigo_de_gobierno_societario_21418b
    - Operacion_evaluacion_de_riesgos_de_la_entidad_2f697b
    - Operacion_evaluacion_de_sujetos_de_credito_con_apertura_de_legajo_78e678
    - Operacion_evaluacion_diaria_de_parametros_en_valuacion_a_modelo_572bc3
    - Operacion_evaluacion_gestion_directorio_y_renovacion_alta_gerencia_d0b9e8
    - Operacion_evaluacion_procesos_control_interno_94aa0c
    - Operacion_exceso_de_margenes_de_credito_por_lineas_especificas_bef38b
    - Operacion_exclusion_de_central_de_inhabilitados_fab64b
    - Operacion_exclusion_de_conceptos_deducibles_del_computo_rm_d96734
    - Operacion_exclusion_de_exposiciones_subyacentes_del_calculo_de_activos_ponderados_49f137
    - Operacion_exclusion_de_futuros_y_forwards_con_subyacentes_aad2ae
    - Operacion_exclusion_operaciones_discontinuadas_del_bi_3aa389
    - Operacion_exhibicion_de_documento_anterior_bfbc29
    - Operacion_exhibicion_dni_d_en_formato_credencial_virtual_8985e2
    - Operacion_exhibicion_dni_m_o_dni_d_post_rectificacion_0444ac
    - Operacion_exigencia_capital_derivado_enesimo_incumplimiento_n_1_2d4c08
    - Operacion_exigencia_de_capital_por_commodities_1dac48
    - Operacion_exigencia_de_capital_por_tipo_de_cambio_aaeaf4
    - Operacion_exportacion_a_consumo_con_importacion_temporaria_1588aa
    - Operacion_exportacion_a_consumo_de_automotores_3ad5fc
    - Operacion_exportacion_a_consumo_radicacion_exterior_9e2590
    - Operacion_exportacion_aae_a_areas_francas_nacionales_56afe6
    - Operacion_exportacion_comprendida_decreto_443_23_e3f93b
    - Operacion_exportacion_de_bienes_0026b2
    - Operacion_exportacion_de_bienes_por_vpu_rigi_5645aa
    - Operacion_exportacion_de_valores_mediante_regimen_ec51_d397cc
    - Operacion_exportacion_desde_territorio_nacional_continental_al_area_franca_325703
    - Operacion_exportaciones_bienes_con_fines_promocionales_74ed90
    - Operacion_exportaciones_territorio_continental_a_area_aduanera_especial_e3b8f4
    - Operacion_exposicion_a_bmd_que_cumplen_criterios_de_admisibilidad_9a5a9c
    - Operacion_exposicion_a_entidades_financieras_corto_plazo_3ff5fb
    - Operacion_exposicion_a_entidades_financieras_demas_9e45d0
    - Operacion_exposicion_crediticia_con_cobertura_de_riesgo_de_credito_c4140c
    - Operacion_exposicion_frente_contraparte_individual_772d37
    - Operacion_exposicion_garantia_hipotecaria_inmuebles_comerciales_87bb5f
    - Operacion_exposiciones_a_acciones_4baa91
    - Operacion_exposiciones_a_bancos_multilaterales_de_desarrollo_919e2d
    - Operacion_exposiciones_a_ccp_b3994e
    - Operacion_exposiciones_a_empresas_03f0db
    - Operacion_exposiciones_a_entidades_financieras_481fc3
    - Operacion_exposiciones_a_instrumentos_014c82
    - Operacion_exposiciones_a_instrumentos_deuda_subordinada_719f82
    - Operacion_exposiciones_a_instrumentos_participaciones_en_capital_3a77b8
    - Operacion_exposiciones_con_entidades_de_contraparte_central_3e7288
    - Operacion_exposiciones_con_garantia_hipotecaria_e1cab3
    - Operacion_exposiciones_en_el_activo_codigo_45110000_bb7888
    - Operacion_exposiciones_en_situacion_de_incumplimiento_104f61
    - Operacion_exposiciones_garantizadas_por_sgr_o_fondo_publico_9fec24
    - Operacion_exposiciones_minoristas_82110c
    - Operacion_exposiciones_minoristas_normativas_no_transaccionales_f44033
    - Operacion_extension_al_portador_de_cheque_de_pago_diferido_c72ebd
    - Operacion_extension_de_contragarantias_exterior_991c53
    - Operacion_extension_de_plazo_de_prestamo_uvi_e6e225
    - Operacion_extension_del_plazo_120_dias_corridos_996935
    - Operacion_extension_del_plazo_hasta_plazo_previsto_en_punto_7_1_1_4_8e468f
    - Operacion_extension_plazo_ingreso_liquidacion_divisas_d523f1
    - Operacion_extraccion_de_efectivo_en_cajero_automatico_8d8d06
    - Operacion_extracciones_a_traves_de_cajeros_automaticos_47772f
    - Operacion_extravio_de_cheques_y_documentos_e17067
    - Operacion_facilidades_adicionales_margenes_vigentes_acordados_60351e
    - Operacion_facilidades_de_liquidez_titulizacion_9e9de2
    - Operacion_falsificacion_de_cheques_2b8840
    - Operacion_falta_de_firma_del_librador_7c504b
    - Operacion_financiacion_comercial_de_importacion_53c0f5
    - Operacion_financiacion_comercial_importacion_de_bienes_dee2df
    - Operacion_financiacion_comercial_para_importacion_de_bienes_de_capital_110ddf
    - Operacion_financiacion_computada_como_ingresada_y_liquidada_6d2187
    - Operacion_financiacion_con_titulos_valores_susceptibles_de_aforo_nulo_7dcf86
    - Operacion_financiacion_de_consumos_en_moneda_extranjera_con_tarjetas_8303ec
    - Operacion_financiacion_de_exportaciones_24e773
    - Operacion_financiacion_de_importaciones_con_aplicacion_a_cobros_exportaciones_2bc642
    - Operacion_financiacion_de_operaciones_de_comercio_exterior_d19145
    - Operacion_financiacion_de_prestadores_de_servicios_exportados_9dab89
    - Operacion_financiacion_de_proveedores_de_servicios_de_exportacion_71f51a
    - Operacion_financiacion_de_proyectos_inversion_ganaderia_bovina_66ab3e
    - Operacion_financiacion_de_proyectos_inversion_nacional_4e01cd
    - Operacion_financiacion_de_unidades_de_vivienda_uvi_1c1cab
    - Operacion_financiacion_de_uva_cer_ley_25_827_756c14
    - Operacion_financiacion_en_cuotas_de_compras_de_clientes_310e5c
    - Operacion_financiacion_especializada_grandes_proyectos_infraestructura_91c15f
    - Operacion_financiacion_mipyme_y_actividad_profesional_9b7954
    - Operacion_financiacion_u_otorgamiento_de_garantia_anterior_a_13_12_23_459923
    - Operacion_financiaciones_a_clientes_agricolas_no_mipyme_5faf23
    - Operacion_financiaciones_a_clientes_agricolas_no_mipyme_5faf23__cap
    - Operacion_financiaciones_a_exportadores_con_flujo_futuro_de_ingresos_be9e60
    - Operacion_financiaciones_a_mipymes_534b02
    - Operacion_financiaciones_a_productores_bienes_exportacion_984579
    - Operacion_financiaciones_a_proveedores_de_bienes_y_servicios_proceso_productivo_3bbeee
    - Operacion_financiaciones_asociadas_a_importaciones_de_bienes_a3239b
    - Operacion_financiaciones_asociadas_a_importaciones_habilitadas_633f47
    - Operacion_financiaciones_comerciales_en_moneda_extranjera_503e01
    - Operacion_financiaciones_comerciales_pagos_a_vista_importaciones_bienes_25e0ce
    - Operacion_financiaciones_comerciales_pagos_diferidos_importaciones_bienes_c7b77f
    - Operacion_financiaciones_con_amortizacion_periodica_personas_humanas_07ab20
    - Operacion_financiaciones_con_garantias_en_moneda_extranjera_11bef7
    - Operacion_financiaciones_con_garantias_preferidas_a_ca48e7
    - Operacion_financiaciones_de_exportaciones_f060f3
    - Operacion_financiaciones_de_importaciones_de_bienes_656436
    - Operacion_financiaciones_destinos_no_previstos_2_1_1_a_2_1_6_6d6ec0
    - Operacion_financiaciones_directas_11e86a
    - Operacion_financiaciones_en_moneda_extranjera_por_ef_locales_9acfec
    - Operacion_financiaciones_financieras_pagos_a_vista_importaciones_bienes_c97af4
    - Operacion_financiaciones_financieras_pagos_diferidos_importaciones_bienes_574b0f
    - Operacion_financiaciones_pagos_importaciones_bienes_52489b
    - Operacion_financiaciones_rotativas_revolving_bc8efb
    - Operacion_financiaciones_sin_responsabilidad_cedente_con_seguros_credito_e33570
    - Operacion_financiamiento_con_destino_comercio_exterior_7a28bb
    - Operacion_financiamiento_exportacion_a909a6
    - Operacion_financiamiento_sector_publico_no_financiero_2f41c7
    - Operacion_firma_electronica_en_echeq_39abe8
    - Operacion_funcion_de_auditoria_externa_3cb938
    - Operacion_funcion_de_auditoria_interna_b303ae
    - Operacion_futuro_sobre_indice_de_bonos_corporativos_2e8039
    - Operacion_futuros_y_contratos_a_termino_combinacion_de_posiciones_e92395
    - Operacion_garantia_hipotecaria_con_inmueble_terminado_0e5a68
    - Operacion_gestion_activa_de_posiciones_b4502e
    - Operacion_gestion_activa_posiciones_cartera_negociacion_0e621d
    - Operacion_gestion_de_cobro_por_agencia_de_recupero_6de780
    - Operacion_gestion_de_cobro_por_aseguradora_da7121
    - Operacion_gestion_de_cobro_por_tercero_cheque_al_portador_o_nominal_41dcea
    - Operacion_gestion_de_echeq_514051
    - Operacion_gestion_de_operaciones_y_riesgos_eba575
    - Operacion_gestion_de_registro_formato_papel_a6b85b
    - Operacion_gestion_de_riesgos_de_mercado_9e360a
    - Operacion_giro_sobre_el_librador_0e2548
    - Operacion_giros_en_descubierto_a88209
    - Operacion_habilitacion_de_nueva_entidad_para_emision_de_certificaciones_bebac7
    - Operacion_identificacion_de_denunciantes_mediante_documentos_40e459
    - Operacion_identificacion_de_presentante_cheque_papel_6a3d2c
    - Operacion_identificacion_evaluacion_monitoreo_control_y_mitigacion_de_riesgos_b095a3
    - Operacion_identificacion_por_codigo_de_comision_nacional_de_valores_514cb4
    - Operacion_implementacion_procedimientos_gobierno_corporativo_4bd8aa
    - Operacion_importacion_posiciones_arancelarias_ncm_8802_f58c9c
    - Operacion_imposibilitar_uso_de_productos_servicios_por_medidas_de_seguridad_15e35f
    - Operacion_imputacion_a_capacidad_de_prestamo_depositos_moneda_extranjera_49ff53
    - Operacion_imputacion_cumplimiento_seguimiento_permiso_rigi_4ab19b
    - Operacion_imputacion_de_credito_al_tercero_principal_pagador_avalista_o_codeudor_bd92ec
    - Operacion_imputacion_de_creditos_cedidos_sin_responsabilidad_f629f9
    - Operacion_imputacion_de_financiaciones_incorporadas_12bd29
    - Operacion_imputacion_de_liquidaciones_a_permiso_embarque_03fd5b
    - Operacion_imputacion_de_multas_por_demora_en_entrega_824513
    - Operacion_imputacion_exportacion_temporal_con_perdida_de_valor_b02aaa
    - Operacion_imputacion_gastos_colocacion_bienes_exterior_2fd647
    - Operacion_imputacion_oficializacion_a_excepcion_de_ingreso_y_liquidacion_26d489
    - Operacion_inclusion_de_instrumentos_en_pnc_e94b0a
    - Operacion_inclusion_de_posiciones_en_cartera_de_negociacion_bc636b
    - Operacion_inclusion_en_central_de_cheques_denunciados_b68f29
    - Operacion_inclusion_en_central_de_cuentacorrentistas_inhabilitados_18cee7
    - Operacion_inclusion_en_central_de_inhabilitados_579dc0
    - Operacion_incorporacion_de_carteras_por_titulos_o_participaciones_59dbe7
    - Operacion_incorporacion_de_dividendo_cupon_con_reajuste_2c7f67
    - Operacion_incorporacion_de_inmuebles_al_patrimonio_42a508
    - Operacion_incorporacion_en_centrales_de_cheques_rechazados_e_inhabilitados_7fff4f
    - Operacion_incremento_tenencias_moneda_extranjera_ab92a1
    - Operacion_incumplimiento_del_capital_minimo_exigido_58cfb3
    - Operacion_informacion_de_exposiciones_fuera_de_balance_bf3ab2
    - Operacion_informacion_de_exposiciones_sft_4dce44
    - Operacion_informacion_de_incumplimientos_activos_inmovilizados_3e5a14
    - Operacion_informacion_de_incumplimientos_derivados_sobre_commodities_00b289
    - Operacion_informacion_de_incumplimientos_graduacion_del_credito_aab62c
    - Operacion_informacion_de_incumplimientos_grandes_exposiciones_f447b0
    - Operacion_informacion_de_incumplimientos_sector_publico_no_financiero_4c3db2
    - Operacion_informacion_del_ratio_de_apalancamiento_958bfc
    - Operacion_informar_reduccion_exigencia_en_partida_36000001_862a12
    - Operacion_informar_reduccion_exigencia_en_partida_36000004_5b7f27
    - Operacion_informe_auditoria_externa_sobre_cumplimiento_iosco_cpmi_74d848
    - Operacion_informe_mensual_informacion_posiciones_y_exigencia_f6c688
    - Operacion_informe_total_de_letras_hipotecarias_escriturales_6576c1
    - Operacion_ingreso_contravalor_exportacion_en_divisas_0ce029
    - Operacion_ingreso_de_anticipos_prefinanciaciones_y_posfinanciaciones_del_exterior_3bcbe7
    - Operacion_ingreso_de_bienes_con_despacho_a_plaza_por_solicitud_particular_o_courier_be40df
    - Operacion_ingreso_de_divisas_por_mercado_de_cambios_bbfa94
    - Operacion_ingreso_de_fondos_divisas_destino_beneficiarios_finales_b414f5
    - Operacion_ingreso_de_recuperos_de_seguro_en_mercado_de_cambios_2c2e57
    - Operacion_ingreso_y_liquidacion_cobros_exportaciones_bf3a95
    - Operacion_ingreso_y_liquidacion_de_cobros_de_exportacion_cc95e6
    - Operacion_ingreso_y_liquidacion_de_cobros_de_exportaciones_fd7234
    - Operacion_ingreso_y_liquidacion_de_contravalor_en_divisas_d8486c
    - Operacion_ingreso_y_liquidacion_de_divisas_dc00d4
    - Operacion_ingreso_y_liquidacion_de_divisas_de_exportacion_cd242d
    - Operacion_ingreso_y_liquidacion_de_divisas_en_mercado_de_cambios_a2158d
    - Operacion_ingreso_y_liquidacion_de_divisas_exportacion_concentrados_minerales_b6dc1e
    - Operacion_ingreso_y_liquidacion_de_divisas_exportacion_precios_revisables_099c9f
    - Operacion_ingreso_y_liquidacion_de_divisas_financiacion_importacion_2dea6e
    - Operacion_ingreso_y_liquidacion_de_divisas_por_exportacion_6e62aa
    - Operacion_ingreso_y_liquidacion_divisas_mercado_cambios_f79465
    - Operacion_ingreso_y_liquidacion_en_mercado_de_cambios_4fb095
    - Operacion_ingreso_y_liquidacion_titulos_deuda_exterior_6ad647
    - Operacion_inhabilitacion_de_cuentacorrentistas_4c01ff
    - Operacion_inhabilitacion_zfi_ingreso_zona_franca_1c89d4
    - Operacion_insercion_de_firma_en_cheque_para_cobro_o_deposito_761507
    - Operacion_instalacion_de_oficinas_de_representacion_en_exterior_0e801f
    - Operacion_instalacion_de_sucursales_en_el_exterior_7a7180
    - Operacion_instrumento_con_obligacion_diferible_indefinidamente_548434
    - Operacion_instrumento_con_opcion_de_cancelacion_mediante_acciones_0e2f02
    - Operacion_instrumento_con_opcion_del_tenedor_de_pago_en_acciones_e2f378
    - Operacion_integracion_de_exigencia_basica_capital_e446e9
    - Operacion_interaccion_con_red_de_cajeros_automaticos_96c01d
    - Operacion_intermediacion_de_contratos_de_seguros_generales_1c7073
    - Operacion_inversion_en_emision_con_calificacion_ae98cf
    - Operacion_legalizacion_de_documentacion_autoridad_consular_o_convenio_de_la_haya_af32b3
    - Operacion_letras_aceptadas_pago_diferido_9cc923
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
    - Operacion_limites_de_compra_tarjeta_de_credito_ade36c
    - Operacion_lineas_de_credito_a_bancos_del_exterior_facilitar_exportaciones_86d363
    - Operacion_liquidacion_de_activos_no_imprescindibles_b2d088
    - Operacion_liquidacion_de_divisas_por_cobro_de_exportaciones_ed86ac
    - Operacion_liquidacion_de_divisas_por_cobros_de_exportacion_fc5c43
    - Operacion_liquidacion_de_divisas_por_procesadores_de_pagos_e5ce30
    - Operacion_liquidacion_de_financiaciones_en_moneda_extranjera_d050b0
    - Operacion_liquidacion_de_fondos_moneda_extranjera_4c9a77
    - Operacion_liquidacion_de_incentivos_economicos_fbadf9
    - Operacion_liquidacion_de_la_rendicion_de_cuentas_d7f07b
    - Operacion_liquidacion_de_montos_por_exportador_84980c
    - Operacion_liquidacion_de_seguro_de_mercaderia_siniestrada_0f734c
    - Operacion_liquidacion_divisas_devolucion_pagos_importaciones_f1e2ef
    - Operacion_liquidacion_divisas_exportaciones_4d4afa
    - Operacion_liquidacion_en_mercado_cambios_servicios_financieros_e32a15
    - Operacion_liquidacion_en_mercado_de_cambios_d7d852
    - Operacion_liquidacion_en_pesos_en_el_pais_bb8004
    - Operacion_liquidacion_moneda_extranjera_exportacion_49a3b1
    - Operacion_liquidacion_simultanea_cobros_anticipados_exportacion_74f96c
    - Operacion_liquidacion_simultanea_de_cobros_anticipados_o_prefinanciaciones_e778a8
    - Operacion_liquidacion_simultanea_de_financiaciones_en_moneda_extranjera_3b1b32
    - Operacion_liquidacion_ventas_titulos_valores_fb2856
    - Operacion_liquidaciones_nuevas_de_anticipos_y_prefinanciaciones_4d46e5
    - Operacion_llevanza_del_legajo_en_medios_magneticos_electronicos_u_otros_82e4a0
    - Operacion_mantencion_en_custodia_de_activos_garantia_c730dc
    - Operacion_mantener_posicion_neta_en_productos_basicos_5436ed
    - Operacion_mantener_posiciones_en_acciones_139550
    - Operacion_mantener_posiciones_en_commodities_2cffc9
    - Operacion_mantener_posiciones_en_moneda_extranjera_908af4
    - Operacion_mantener_transferencias_pendientes_de_liquidacion_eed0ce
    - Operacion_mantenimiento_del_registro_de_reintegros_de_importes_dec4ce
    - Operacion_material_promocional_regimen_aduanero_b7433e
    - Operacion_medicion_de_riesgo_especifico_en_titulos_valores_0a63af
    - Operacion_medicion_de_riesgo_general_de_mercado_en_titulos_valores_184a5e
    - Operacion_medicion_sistema_derivados_tasas_interes_4d7e69
    - Operacion_medios_de_comunicacion_cambios_negativos_clasificacion_f7a20b
    - Operacion_metodo_sustitucion_ponderadores_e11e83
    - Operacion_modificacion_condiciones_contratadas_61bd5f
    - Operacion_modificacion_de_clasificacion_en_la_central_de_deudores_c89e2b
    - Operacion_modificacion_de_computo_en_central_de_cheques_rechazados_462cd3
    - Operacion_modificacion_de_comunicaciones_de_rechazo_a2506c
    - Operacion_modificacion_de_condiciones_de_cuenta_corriente_be52c3
    - Operacion_modificacion_de_entidad_nominada_emision_certificaciones_e38003
    - Operacion_modificacion_de_entidad_nominada_para_emision_de_certificaciones_538b55
    - Operacion_modificacion_de_productos_y_servicios_existentes_eb2e10
    - Operacion_modificacion_de_sistema_aprobado_42a6a7
    - Operacion_modificacion_del_numero_de_dni_103764
    - Operacion_modificacion_nombre_y_o_apellido_88e879
    - Operacion_monitoreo_de_operaciones_290854
    - Operacion_movimientos_de_fondos_derivados_rendicion_ff9b77
    - Operacion_movimientos_de_fondos_segun_presentacion_aceptada_5e3e58
    - Operacion_muestras_bajo_ley_22_415_articulos_560_565_77ad22
    - Operacion_multiplicador_de_epf_factor_de_garantia_en_exceso_55f905
    - Operacion_negociacion_bursatil_de_cheques_de_pago_diferido_7ce672
    - Operacion_negociacion_contravalor_exportacion_en_mercado_de_cambios_3956ab
    - Operacion_negociacion_de_acciones_compradas_o_vendidas_06e61b
    - Operacion_negociacion_de_cheques_diferidos_af0737
    - Operacion_neteamiento_derivado_accion_identico_22c970
    - Operacion_no_emision_de_comprobante_en_cajero_8448bf
    - Operacion_no_registracion_de_cheques_de_pago_diferido_57bd1c
    - Operacion_nominacion_de_entidad_financiera_para_certificacion_de_exportaciones_e5d888
    - Operacion_notificacion_sefyc_de_ajuste_de_previsiones_05b1d2
    - Operacion_nuevos_aportes_de_inversion_directa_de_no_residentes_3fcab3
    - Operacion_nuevos_endeudamientos_financieros_comprendidos_en_3_5_16e777
    - Operacion_obligaciones_me_entre_residentes_52e312
    - Operacion_obligaciones_negociables_516ebb
    - Operacion_obtencion_constancia_cuil_de_renaper_o_anses_deaeb7
    - Operacion_obtencion_copia_documento_de_identidad_con_cuil_92997e
    - Operacion_obtencion_de_certificacion_de_auditor_externo_bfcb16
    - Operacion_obtencion_de_proteccion_crediticia_maxima_prelacion_6565a2
    - Operacion_obtencion_de_proteccion_crediticia_tramos_subordinados_c420ac
    - Operacion_obtencion_electronica_directa_de_constancia_cuit_cdi_de_arca_14af7e
    - Operacion_oferta_de_suscripcion_de_bonos_bopreal_en_nombre_del_cliente_66a5e9
    - Operacion_oficializacion_del_despacho_de_importacion_a75d61
    - Operacion_opciones_sobre_acciones_30e016
    - Operacion_operacion_aduanera_regimen_bara_9e3521
    - Operacion_operacion_aduanera_regimen_vmi1_0a1237
    - Operacion_operacion_cobertura_tasa_de_interes_residente_dd9715
    - Operacion_operacion_con_activo_efectivo_o_titulos_instrumentos_bcra_con_aforo_af8394
    - Operacion_operacion_con_ccp_no_calificada_dbde8f
    - Operacion_operacion_con_qccp_16a95e
    - Operacion_operacion_de_cambio_305a62
    - Operacion_operacion_de_egreso_para_vpu_rigi_9e4134
    - Operacion_operacion_de_pase_en_cartera_de_negociacion_f293b1
    - Operacion_operacion_de_reembarco_7f2ddd
    - Operacion_operacion_en_mercado_de_cambios_1718c1
    - Operacion_operacion_encuadrada_en_decreto_492_23_560ae8
    - Operacion_operacion_propia_alcanzada_por_obligacion_de_ingreso_y_liquidacion_58449b
    - Operacion_operaciones_a_traves_de_cajeros_automaticos_63fb57
    - Operacion_operaciones_aduaneras_guerra_seguridad_policia_0fbbb1
    - Operacion_operaciones_aduaneras_por_ventajas_arancelarias_11f7c3
    - Operacion_operaciones_al_contado_a_liquidar_no_fallidas_f258f5
    - Operacion_operaciones_al_contado_con_titulos_oro_o_moneda_extranjera_9dc774
    - Operacion_operaciones_comprendidas_puntos_7_9_y_7_10_3028df
    - Operacion_operaciones_con_derivados_cartera_de_negociacion_688397
    - Operacion_operaciones_con_derivados_no_comprendidas_0e5406
    - Operacion_operaciones_con_derivados_otc_o_mercados_regulados_6e6186
    - Operacion_operaciones_con_ejercicio_de_opcion_exportador_a6d576
    - Operacion_operaciones_con_subsidiarias_y_vinculados_add23d
    - Operacion_operaciones_con_titulos_valores_pendientes_de_liquidacion_54ad52
    - Operacion_operaciones_con_titulos_valores_y_otros_activos_43240a
    - Operacion_operaciones_cursadas_sml_paraguay_uruguay_1c31f5
    - Operacion_operaciones_de_anticipos_y_prefinanciaciones_del_exterior_1404cf
    - Operacion_operaciones_de_cambio_65a95e
    - Operacion_operaciones_de_cambio_canje_y_o_arbitraje_221389
    - Operacion_operaciones_de_cambio_entre_entidades_7d061b
    - Operacion_operaciones_de_financiamiento_con_aplicacion_de_divisas_d8b9bb
    - Operacion_operaciones_de_importadores_no_regularizadas_0e7f22
    - Operacion_operaciones_de_negociacion_con_ccp_44e6c1
    - Operacion_operaciones_de_pase_repo_eb6ce7
    - Operacion_operaciones_de_titulos_valores_por_diferencia_b86001
    - Operacion_operaciones_derivados_financieros_residentes_no_autorizados_17f156
    - Operacion_operaciones_dvp_entrega_contra_pago_con_riesgo_de_exposicion_positiva_0aeba9
    - Operacion_operaciones_dvp_fallidas_a8ff95
    - Operacion_operaciones_en_terminales_puntos_de_venta_7627ce
    - Operacion_operaciones_exporta_simple_8b5fe4
    - Operacion_operaciones_financiadas_deuda_por_importacion_de_bienes_42fab2
    - Operacion_operaciones_no_dvp_05da87
    - Operacion_operaciones_no_dvp_entrega_unilateral_sin_contrapartida_simultanea_3e2d84
    - Operacion_operaciones_no_dvp_incumplimiento_quinto_dia_99133a
    - Operacion_operaciones_no_dvp_prestamo_111b2d
    - Operacion_operaciones_por_ventanilla_ebfe32
    - Operacion_operaciones_sujetas_a_neteo_bilateral_valido_4667fb
    - Operacion_operaciones_sujetas_a_novacion_bb83f9
    - Operacion_operar_con_directores_administradores_y_vinculados_967f5e
    - Operacion_operatoria_con_derivados_4f0c87
    - Operacion_originacion_de_creditos_entidad_14367d
    - Operacion_originacion_directa_o_indirecta_de_exposiciones_fcf50e
    - Operacion_otorgamiento_asistencia_financiera_a_controlante_ce1e2d
    - Operacion_otorgamiento_certificacion_cumplido_0187f5
    - Operacion_otorgamiento_de_asistencia_financiera_evaluacion_especifica_382302
    - Operacion_otorgamiento_de_aval_sobre_cheques_diferidos_7593ac
    - Operacion_otorgamiento_de_financiaciones_sector_publico_no_financiero_de6a1d
    - Operacion_otorgamiento_de_garantias_84c90b
    - Operacion_otorgamiento_de_garantias_a_residentes_en_exterior_6fa98b
    - Operacion_otorgamiento_de_garantias_financieras_e7259a
    - Operacion_otorgamiento_de_garantias_localmente_6e87d1
    - Operacion_otorgamiento_de_incentivos_economicos_al_personal_1475cd
    - Operacion_otorgamiento_de_nuevas_financiaciones_996921
    - Operacion_otorgamiento_de_prestamo_pesos_variable_e4718d
    - Operacion_otorgamiento_de_prestamos_con_garantia_hipotecaria_7a77f8
    - Operacion_otorgamiento_de_prestamos_hipotecarios_9bd23d
    - Operacion_otorgamiento_de_prorrogas_para_documentacion_aduanera_siniestrada_e60fed
    - Operacion_otra_retransferencia_de_fondos_00c399
    - Operacion_otros_creditos_acordados_b71050
    - Operacion_pago_a_la_vista_contra_documentacion_de_embarque_967ea8
    - Operacion_pago_a_la_vista_de_cheques_994ac8
    - Operacion_pago_a_la_vista_de_cheques_de_pago_diferido_788bb6
    - Operacion_pago_a_la_vista_de_importaciones_de_bienes_bc4c79
    - Operacion_pago_al_exterior_bienes_deposito_franco_bd6e5f
    - Operacion_pago_al_exterior_bienes_importados_obras_infraestructura_ebbfc5
    - Operacion_pago_al_exterior_de_importaciones_por_solicitud_particular_o_courier_dbb562
    - Operacion_pago_al_exterior_importacion_desde_zona_franca_880425
    - Operacion_pago_al_exterior_importaciones_zonas_francas_transferencia_aduanera_9109a8
    - Operacion_pago_anticipado_a_la_vista_diferido_importacion_bienes_6a9e15
    - Operacion_pago_anticipado_de_importaciones_de_bienes_9a731f
    - Operacion_pago_anticipado_importacion_bienes_aduanero_pendiente_47c4f1
    - Operacion_pago_anticipado_importaciones_bienes_f433a5
    - Operacion_pago_capital_e_intereses_moneda_extranjera_126f50
    - Operacion_pago_capital_e_intereses_titulos_deuda_moneda_extranjera_74c4e1
    - Operacion_pago_capital_endeudamiento_financiero_exterior_9edfd4
    - Operacion_pago_capital_intereses_titulos_deuda_registro_publico_ce0ad1
    - Operacion_pago_de_beneficios_anses_5e43b5
    - Operacion_pago_de_capital_adeudado_porcion_compensable_d41f0c
    - Operacion_pago_de_capital_de_deudas_comerciales_por_importacion_bf8525
    - Operacion_pago_de_capital_e_intereses_con_contrapartes_vinculadas_5e3b7b
    - Operacion_pago_de_capital_e_intereses_de_deudas_por_importacion_f140bb
    - Operacion_pago_de_capital_e_intereses_endeudamiento_financiero_exterior_b07ad6
    - Operacion_pago_de_capital_e_intereses_endeudamientos_222456
    - Operacion_pago_de_capital_e_intereses_endeudamientos_financieros_1adc36
    - Operacion_pago_de_capital_financiaciones_locales_rigi_defa7a
    - Operacion_pago_de_cheque_2a306d
    - Operacion_pago_de_cheque_cruzado_1b1710
    - Operacion_pago_de_cheque_de_pago_diferido_e58469
    - Operacion_pago_de_cheques_3a6175
    - Operacion_pago_de_cheques_de_ventanilla_1373fd
    - Operacion_pago_de_deuda_comercial_al_exterior_con_condicion_cumplida_8f599b
    - Operacion_pago_de_deudas_comerciales_por_importaciones_eb72a4
    - Operacion_pago_de_deudas_de_bienes_o_servicios_en_cambios_c92cb1
    - Operacion_pago_de_deudas_por_servicios_de_no_residentes_116c6c
    - Operacion_pago_de_endeudamientos_financieros_con_demostracion_de_ingreso_aduanero_a9414a
    - Operacion_pago_de_fletes_exportacion_con_cumplido_embarque_dc0eb1
    - Operacion_pago_de_fletes_importacion_s30_8bf9cb
    - Operacion_pago_de_honorarios_participaciones_y_gratificaciones_2352a1
    - Operacion_pago_de_importacion_con_imputacion_al_despacho_4bc19a
    - Operacion_pago_de_importaciones_con_ingreso_aduanero_pendiente_c82d08
    - Operacion_pago_de_importaciones_con_registro_de_ingreso_aduanero_pendiente_45589e
    - Operacion_pago_de_importaciones_de_bienes_62e021
    - Operacion_pago_de_importaciones_de_bienes_ferroviarios_31066c
    - Operacion_pago_de_importaciones_de_bienes_mediante_cambios_bc79c1
    - Operacion_pago_de_incentivo_economico_variable_diferido_732465
    - Operacion_pago_de_incentivos_economicos_al_personal_c0a655
    - Operacion_pago_de_intereses_compensatorios_deudas_con_contrapartes_vinculadas_1e8917
    - Operacion_pago_de_intereses_con_acceso_mercado_cambios_7f8aea
    - Operacion_pago_de_intereses_de_deuda_comercial_por_importacion_28276f
    - Operacion_pago_de_intereses_deuda_comercial_importacion_ea238a
    - Operacion_pago_de_intereses_deudas_comerciales_5919f6
    - Operacion_pago_de_intereses_devengados_porcion_compensable_61dd48
    - Operacion_pago_de_intereses_devengados_sin_atrasos_superiores_a_31_dias_8aba2d
    - Operacion_pago_de_intereses_financiaciones_rigi_cf2d1b
    - Operacion_pago_de_intereses_y_capital_financiaciones_rigi_07d28d
    - Operacion_pago_de_multas_por_clientela_8044ba
    - Operacion_pago_de_oficializacion_de_importacion_4ef9d5
    - Operacion_pago_de_oficializacion_de_importacion_no_comprendida_f359ab
    - Operacion_pago_de_ordenes_de_beneficios_anses_cad97b
    - Operacion_pago_de_otros_servicios_de_salud_628b2b
    - Operacion_pago_de_pagares_con_oferta_publica_emitidos_bajo_cnv_fd274b
    - Operacion_pago_de_prestamos_1dedfd
    - Operacion_pago_de_punitorios_y_equivalentes_deudas_con_contrapartes_vinculadas_66ae16
    - Operacion_pago_de_servicio_audiovisual_y_conexo_5a991f
    - Operacion_pago_de_servicio_con_contraparte_vinculada_0284f0
    - Operacion_pago_de_servicio_de_salud_asistencia_al_viajero_67799b
    - Operacion_pago_de_servicio_de_transporte_de_pasajeros_3dec76
    - Operacion_pago_de_servicio_de_viajes_aaf499
    - Operacion_pago_de_servicio_del_gobierno_93ec27
    - Operacion_pago_de_servicios_de_no_residentes_8c6a60
    - Operacion_pago_de_servicios_no_conexos_al_comercio_exterior_3eab71
    - Operacion_pago_de_servicios_personales_culturales_y_recreativos_b91cd2
    - Operacion_pago_de_servicios_prestados_por_no_residentes_452fae
    - Operacion_pago_de_utilidades_y_dividendos_a_accionistas_no_residentes_c7ec69
    - Operacion_pago_de_utilidades_y_dividendos_accionistas_no_residentes_dcf15f
    - Operacion_pago_de_valores_de_deuda_fiduciaria_39c480
    - Operacion_pago_deuda_importacion_bienes_no_comercial_b12910
    - Operacion_pago_deudas_moneda_extranjera_entre_residentes_cd0b55
    - Operacion_pago_diferido_importacion_bienes_con_registro_ingreso_04a2f8
    - Operacion_pago_en_efectivo_de_cheques_e129b8
    - Operacion_pago_exterior_insumos_hidrocarburos_offshore_2e3a78
    - Operacion_pago_fletes_importacion_no_incluidos_compra_e93515
    - Operacion_pago_importaciones_bienes_servicios_moneda_local_ff24d5
    - Operacion_pago_mediante_canje_y_o_arbitraje_23cc48
    - Operacion_pago_pagares_oferta_publica_cnv_capital_e_intereses_f2000e
    - Operacion_pago_por_compra_venta_no_presencial_de_bienes_18f10e
    - Operacion_pago_por_consumo_con_tarjeta_debito_servicios_digitales_no_asociados_a_viajes_853ea7
    - Operacion_pago_por_otro_medio_convenido_816153
    - Operacion_pago_por_retiros_consumos_con_tarjeta_debito_otros_s36_d6b83d
    - Operacion_pago_proporcional_fondos_parcialmente_liquidados_237f45
    - Operacion_pago_unico_de_garantia_por_garante_e6925b
    - Operacion_pago_utilidades_y_dividendos_auditados_5439fa
    - Operacion_pagos_al_exterior_adquisicion_criptoactivos_6e8219
    - Operacion_pagos_al_exterior_por_tarjetas_de_credito_compra_debito_o_prepagas_e06914
    - Operacion_pagos_anticipados_al_exterior_previos_a_entrega_0649a2
    - Operacion_pagos_anticipados_vista_diferidos_de_importaciones_c0f4bd
    - Operacion_pagos_capital_e_intereses_endeudamientos_financieros_fba987
    - Operacion_pagos_capital_intereses_endeudamientos_financieros_5bd018
    - Operacion_pagos_capital_intereses_titulos_deuda_emitidos_bf55d2
    - Operacion_pagos_contra_presentacion_documentacion_embarque_b0f5cd
    - Operacion_pagos_de_capital_e_intereses_de_endeudamientos_b3e6c0
    - Operacion_pagos_de_capital_intereses_titulos_deuda_exterior_a8b506
    - Operacion_pagos_de_importaciones_y_compras_de_bienes_al_exterior_faebce
    - Operacion_pagos_de_servicios_prestados_por_no_residentes_3cc0f4
    - Operacion_pagos_en_el_exterior_con_fondos_de_libre_disponibilidad_9451e0
    - Operacion_pagos_importaciones_argentinas_documentados_en_pesos_bd1158
    - Operacion_pagos_importaciones_sin_registro_aduanero_pendiente_c94d3a
    - Operacion_pagos_otros_endeudamientos_financieros_exterior_50e778
    - Operacion_pagos_por_importaciones_de_bienes_y_servicios_sml_bb3be9
    - Operacion_pagos_por_servicios_capital_de_prestamos_financieros_8f0c4b
    - Operacion_pagos_refinanciaciones_punto_3_5_fb7bc6
    - Operacion_pagos_refinanciaciones_titulos_no_punto_3_5_1f60f0
    - Operacion_pagos_titulos_deuda_en_me_pagaderos_en_pais_c93000
    - Operacion_participacion_en_entidades_financieras_del_exterior_8123bb
    - Operacion_participacion_en_juegos_de_azar_y_apuestas_075f34
    - Operacion_participacion_en_redes_de_cajeros_automaticos_2b11c3
    - Operacion_participacion_vinculacion_con_empresa_cajeros_e60ea3
    - Operacion_partidas_pendientes_de_imputacion_saldos_deudores_1bbd89
    - Operacion_pase_con_ponderador_0_participante_esencial_85623e
    - Operacion_pase_con_ponderador_10_contraparte_no_esencial_d60987
    - Operacion_pases_y_cauciones_bursatiles_tomadas_en_pesos_7ccdb7
    - Operacion_pasivos_por_derivados_a_valor_razonable_931aca
    - Operacion_patrocinio_de_programa_abcp_o_titulizacion_b0c05a
    - Operacion_percepcion_de_comisiones_cajero_automatico_277e95
    - Operacion_pnb_calculo_del_patrimonio_neto_basico_d773d4
    - Operacion_ponderacion_de_activos_en_fondos_78daac
    - Operacion_ponderacion_de_exposiciones_incumplidas_835d02
    - Operacion_ponderacion_de_inversion_en_fondo_8e1470
    - Operacion_ponderacion_de_posiciones_de_titulizacion_d20c47
    - Operacion_ponderacion_de_posiciones_por_sensibilidad_a_tasas_4ba0ad
    - Operacion_ponderacion_por_riesgo_evaluaciones_externas_cf5300
    - Operacion_ponderacion_por_riesgo_exposiciones_moneda_extranjera_95a1e2
    - Operacion_ponderacion_por_riesgo_exposiciones_moneda_nacional_5cb0f0
    - Operacion_posfinanciacion_de_exportaciones_de_bienes_liquidada_f5a9e8
    - Operacion_posfinanciacion_del_exterior_por_descuentos_f8ab7c
    - Operacion_posicion_comprada_subyacente_y_comprada_put_434584
    - Operacion_posicion_general_de_cambios_pgc_4fc69a
    - Operacion_posicion_ponderada_por_delta_db8c3b
    - Operacion_posicion_ponderada_por_delta_opciones_sobre_productos_basicos_d53348
    - Operacion_posicion_vendida_subyacente_y_comprada_call_ecf9e7
    - Operacion_posicionamiento_en_titulos_riesgo_especifico_fc9008
    - Operacion_posiciones_brutas_en_bandas_temporales_7e9386
    - Operacion_posiciones_de_titulizacion_0f745e
    - Operacion_posiciones_en_instrumentos_de_negociacion_33841b
    - Operacion_posiciones_en_monedas_extranjeras_y_commodities_91b8ae
    - Operacion_posiciones_en_opciones_contado_9a54d6
    - Operacion_posiciones_en_opciones_termino_714c96
    - Operacion_posiciones_susceptibles_estandarizacion_tasa_fija_1cdaa5
    - Operacion_posiciones_susceptibles_estandarizacion_tasa_variable_e0ddab
    - Operacion_posiciones_titulizacion_cartera_negociacion_ff63a8
    - Operacion_precancelacion_de_capital_e_intereses_de_titulo_de_deuda_18ec3d
    - Operacion_precancelacion_de_capital_e_intereses_vpu_rigi_777640
    - Operacion_precancelacion_de_financiaciones_bcca11
    - Operacion_precancelacion_de_intereses_canje_de_titulos_9cd821
    - Operacion_precancelacion_intereses_deudas_comerciales_302e84
    - Operacion_prefinanciacion_de_exportaciones_directas_d6d123
    - Operacion_prefinanciacion_de_exportaciones_fb472c
    - Operacion_prefinanciacion_de_exportaciones_liquidada_b7e7ac
    - Operacion_prefinanciaciones_de_exportaciones_1e0cb8
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
    - Operacion_presentacion_de_documentacion_de_capitalizacion_definitiva_56b351
    - Operacion_presentacion_de_documento_de_identidad_35714b
    - Operacion_presentacion_de_documento_de_viaje_mercosur_be2ab6
    - Operacion_presentacion_de_fases_rendicion_cuentas_4cf6a8
    - Operacion_presentacion_de_informacion_rendicion_de_cuentas_4b1114
    - Operacion_presentacion_de_informes_al_bcra_5fc76c
    - Operacion_presentacion_de_libreta_de_enrolamiento_9874e4
    - Operacion_presentacion_de_nota_con_datos_minimos_5725a8
    - Operacion_presentacion_de_nota_de_designacion_al_bcra_0b6b85
    - Operacion_presentacion_de_pasaporte_del_pais_de_origen_b199ab
    - Operacion_presentacion_de_plan_de_regularizacion_b1bab6
    - Operacion_presentacion_de_reclamo_ante_bcra_8a05b2
    - Operacion_presentacion_de_rendicion_de_cuentas_b26ee5
    - Operacion_presentacion_de_reporte_sobre_consultas_y_reclamos_07528d
    - Operacion_presentacion_de_titulo_como_cheque_c6f02e
    - Operacion_presentacion_de_titulos_devueltos_f01e8a
    - Operacion_presentacion_de_titulos_sin_fecha_de_creacion_d299a0
    - Operacion_presentacion_declaracion_jurada_cliente_accesorios_y_repuestos_f51907
    - Operacion_presentacion_declaracion_jurada_rendicion_cuentas_c46e93
    - Operacion_presentacion_del_cartular_o_certificado_para_ejercicio_de_acciones_civiles_f33669
    - Operacion_presentacion_documentacion_comercial_por_exportador_668e4c
    - Operacion_presentacion_documento_nacional_de_identidad_digital_ceed70
    - Operacion_presentacion_electronica_de_cheques_al_cobro_155bae
    - Operacion_presentacion_instrumento_constitutivo_sas_499c56
    - Operacion_presentacion_por_mandatario_888151
    - Operacion_presentacion_rendicion_de_cuentas_periodo_tardio_1676e6
    - Operacion_prestacion_de_servicios_por_contrapartes_vinculadas_cb949e
    - Operacion_prestamos_al_fondo_de_garantia_depositos_575218
    - Operacion_prestamos_financieros_liquidados_en_mercado_de_cambios_6fe80a
    - Operacion_prestamos_financieros_otorgados_por_contrapartes_vinculadas_a21d1e
    - Operacion_prestamos_interfinancieros_imputacion_6f2e6a
    - Operacion_prestamos_personales_6fdfb3
    - Operacion_prestamos_personales_preacordados_9973c8
    - Operacion_prestamos_prendarios_c851b6
    - Operacion_prestamos_tasa_fija_riesgo_cancelacion_anticipada_4a1bad
    - Operacion_prestamos_uva_cartera_comercial_0edfd2
    - Operacion_prevencion_conflictos_de_intereses_403c59
    - Operacion_primas_por_opciones_de_compra_y_venta_tomadas_00e0b7
    - Operacion_procesamiento_de_informacion_de_presentacion_6ac656
    - Operacion_procesamiento_de_informacion_rendicion_cuentas_544df2
    - Operacion_programa_abcp_con_facilidad_de_liquidez_5b761d
    - Operacion_provision_banca_por_internet_y_banca_movil_accesibles_028cc8
    - Operacion_provision_de_proteccion_crediticia_total_o_proporcional_1c5bce
    - Operacion_provision_informacion_para_computo_exigencia_capital_fondos_garantia_0374fe
    - Operacion_publicacion_de_cotizaciones_en_portal_bcra_721502
    - Operacion_publicacion_de_modelos_de_contratos_de_adhesion_87b56d
    - Operacion_publicacion_de_tasa_de_interes_efectiva_anual_b294ae
    - Operacion_publicacion_de_uva_y_uvi_2c0786
    - Operacion_publicidad_de_productos_y_o_servicios_financieros_8d4af3
    - Operacion_radicacion_de_cuenta_abierta_no_presencial_8e4535
    - Operacion_realizacion_de_actividades_mediante_estructuras_societarias_o_jurisdicciones_ext_6411c8
    - Operacion_realizacion_de_auditoria_externa_b2d66c
    - Operacion_realizacion_de_operaciones_cambiarias_en_el_exterior_30ca6f
    - Operacion_realizacion_de_operaciones_diarias_984295
    - Operacion_recategorizacion_de_deudor_e91b27
    - Operacion_recategorizacion_del_deudor_c577ea
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
    - Operacion_reclasificacion_de_deudor_07ccfb
    - Operacion_reclasificacion_del_deudor_a5593d
    - Operacion_recompra_de_instrumentos_propios_9a5947
    - Operacion_reconocimiento_de_conceptos_de_otros_resultados_integrales_996c22
    - Operacion_reconocimiento_de_intereses_sobre_saldos_acreedores_ecab11
    - Operacion_reconocimiento_de_tasas_de_interes_613a08
    - Operacion_reconocimiento_participacion_minoritaria_capital_ordinario_6fdddd
    - Operacion_rectificacion_datos_documentos_compensables_f7b2e2
    - Operacion_rectificacion_de_datos_de_identificacion_5210d9
    - Operacion_rectificacion_de_documentos_de_identidad_05f84f
    - Operacion_rectificacion_registral_de_sexo_nombre_ley_26_743_f6a4a6
    - Operacion_recuperacion_de_identidad_resolucion_judicial_bfcf03
    - Operacion_redescuento_de_documentos_en_otras_entidades_financieras_e4739c
    - Operacion_reduccion_o_transferencia_del_riesgo_de_credito_fbdadf
    - Operacion_reduccion_posiciones_activos_financieros_e9c491
    - Operacion_reembolso_de_capital_en_pesos_equivalentes_90baf8
    - Operacion_reembolso_de_capital_en_uvi_eae046
    - Operacion_reemplazo_de_tarjetas_de_debito_e73b43
    - Operacion_reevaluacion_de_clasificacion_de_deudores_1d2671
    - Operacion_refinanciacion_de_deuda_obligaciones_periodicas_93e02d
    - Operacion_refinanciacion_del_capital_adeudado_8bd9fb
    - Operacion_refinanciacion_deuda_comercial_importacion_3c43ab
    - Operacion_refinanciamiento_deuda_titulos_publicos_exterior_2fc8b1
    - Operacion_reformulacion_de_derivados_a_valor_razonable_cero_0ff31c
    - Operacion_regimen_de_exportacion_en_consignacion_0d6162
    - Operacion_regimen_de_rancho_medios_transporte_bandera_nacional_02ce92
    - Operacion_registracion_de_cheques_9375f0
    - Operacion_registracion_de_cheques_de_pago_diferido_b760f1
    - Operacion_registracion_de_cheques_diferidos_da95c8
    - Operacion_registrar_en_sepaimpo_baja_de_diferencia_de_valor_aduanero_bee529
    - Operacion_registro_ante_bcra_enmarque_financiacion_a9c2a4
    - Operacion_registro_cambiario_operaciones_propias_d7382f
    - Operacion_registro_de_caps_floors_combinacion_bono_variable_y_opciones_europeas_631e12
    - Operacion_registro_de_cheque_de_pago_diferido_50f333
    - Operacion_registro_de_cheques_de_pago_diferido_ce6a07
    - Operacion_registro_de_denuncias_ante_instancias_judiciales_y_o_administrativas_328d18
    - Operacion_registro_de_importes_en_miles_de_pesos_7a8d76
    - Operacion_registro_de_imputaciones_al_seguimiento_5ae7ae
    - Operacion_registro_de_liquidaciones_de_divisas_por_devoluciones_0e4a71
    - Operacion_registro_de_novedad_en_repositorio_echeq_ab3fde
    - Operacion_registro_de_operacion_con_cliente_eca8ed
    - Operacion_registro_de_operaciones_cambiarias_f6b0f6
    - Operacion_registro_de_operaciones_con_boletos_sin_movimiento_fa57d8
    - Operacion_registro_de_operaciones_propias_en_fecha_de_efecto_1edd92
    - Operacion_registro_de_permiso_en_condicion_incumplido_ba9369
    - Operacion_registro_de_tenencias_de_instrumentos_tlac_78f227
    - Operacion_registro_de_vencimientos_de_capital_603f3d
    - Operacion_registro_del_cheque_de_pago_diferido_9eb22a
    - Operacion_registro_en_cuenta_corriente_o_cuenta_especial_eacb55
    - Operacion_registro_rioc_seguimiento_operaciones_cambios_b3aebb
    - Operacion_registro_y_seguimiento_de_importaciones_de_bienes_de_capital_cec494
    - Operacion_rehabilitacion_de_productos_y_servicios_3a62d9
    - Operacion_reimportacion_mercaderia_rechazada_en_destino_c45172
    - Operacion_relevamiento_de_activos_y_pasivos_externos_declaracion_ef80ec
    - Operacion_remision_a_traves_de_casa_central_11058a
    - Operacion_remision_cheque_rechazado_al_juzgado_8b8383
    - Operacion_remision_de_ayuda_familiar_4f9dc9
    - Operacion_remision_de_cheque_rechazado_al_juzgado_bfcff5
    - Operacion_remision_de_datos_en_rioc_9bf525
    - Operacion_remision_de_informaciones_contables_a_sefyc_5142c3
    - Operacion_rendicion_de_cuentas_presentacion_tardia_2be202
    - Operacion_rendicion_de_ordenes_de_pago_de_beneficios_anses_f3a839
    - Operacion_renovacion_de_equipos_e_instalaciones_en_puntos_de_atencion_aeb57d
    - Operacion_repago_de_financiaciones_92394a
    - Operacion_repatriacion_aportes_inversion_directa_vpu_rigi_a501c6
    - Operacion_repatriacion_de_aportes_inversion_directa_2580cf
    - Operacion_repatriacion_de_inversion_directa_reduccion_de_capital_95fe9c
    - Operacion_repatriacion_inversiones_directas_aplicacion_divisas_a2c3d1
    - Operacion_repatriacion_inversiones_directas_no_residentes_2bdd03
    - Operacion_repatriacion_inversiones_no_residentes_6dd1c3
    - Operacion_repatriaciones_capital_e_inversiones_directas_b07cf4
    - Operacion_reporte_al_bcra_de_cambio_de_entidad_seguimiento_8b5c98
    - Operacion_reporte_de_cotizaciones_comprador_y_vendedor_c7cc0f
    - Operacion_reporte_de_exposiciones_por_derivados_ffe32c
    - Operacion_reporte_de_ingreso_bruto_del_periodo_e972a3
    - Operacion_reporte_de_prorroga_en_sepaimpo_8327f3
    - Operacion_reporte_en_sepaimpo_de_circunstancias_modificatorias_c5f2ff
    - Operacion_reporte_sepaimpo_afectaciones_despachos_importacion_0286df
    - Operacion_reporte_sepaimpo_zfe_con_transferencia_aduanera_06321a
    - Operacion_reposicion_de_capital_bc6dc6
    - Operacion_representacion_ante_camara_electronica_compensacion_e77be6
    - Operacion_reproduccion_de_firmas_digitalizadas_para_libramiento_de_cheques_a1b02c
    - Operacion_rescate_de_instrumento_897ea5
    - Operacion_rescate_de_instrumentos_del_ca_450b3b
    - Operacion_rescision_relaciones_contractuales_boton_baja_8f9e65
    - Operacion_restitucion_de_capital_48a922
    - Operacion_retencion_de_cheque_de_pago_diferido_e55273
    - Operacion_retencion_de_tarjeta_en_cajero_automatico_b9ece1
    - Operacion_retencion_impositiva_destino_exterior_f2b8e7
    - Operacion_retiro_de_fondos_cuentas_corrientes_especiales_e2972c
    - Operacion_retiro_de_tarjeta_magnetica_3a985e
    - Operacion_retitulizacion_8cc287
    - Operacion_retransferencia_fondos_a_corresponsales_5b24e4
    - Operacion_reversion_de_debitos_debito_automatico_3d9935
    - Operacion_revision_de_cartera_comercial_b58aa2
    - Operacion_revision_exhaustiva_esquema_medicion_riesgo_mercado_aa3850
    - Operacion_revision_periodica_de_estrategias_y_politicas_789cd6
    - Operacion_revocacion_de_aceptacion_de_producto_o_servicio_f08bf6
    - Operacion_revocacion_de_autorizaciones_para_librar_cheques_346e4b
    - Operacion_segregacion_aportes_fondo_garantia_por_tipo_producto_f580da
    - Operacion_seguimiento_anticipos_financiaciones_exportacion_40f298
    - Operacion_seguimiento_de_actividades_de_gestion_de_riesgos_c5564c
    - Operacion_seguimiento_de_fondos_pendientes_de_aplicacion_2bf6f2
    - Operacion_seguimiento_de_negociaciones_de_divisas_por_exportaciones_c212a9
    - Operacion_seguimiento_de_oficializaciones_de_importacion_15fa75
    - Operacion_seguimiento_de_oficializaciones_de_importacion_por_entidad_nominada_b653eb
    - Operacion_seguimiento_de_operaciones_para_proyectos_punto_7_9_2_311ff3
    - Operacion_seguimiento_de_pago_con_ingreso_aduanero_pendiente_8dada3
    - Operacion_seguimiento_de_pagos_de_importaciones_sepaimpo_e80d19
    - Operacion_seguimiento_de_pagos_registro_aduanero_ab8ef8
    - Operacion_seguimiento_de_permiso_de_embarque_fe0266
    - Operacion_seguimiento_de_permisos_de_embarques_71618d
    - Operacion_seguimiento_ejecucion_proyecto_financiacion_6433fd
    - Operacion_seguimiento_negociaciones_secoexpo_db2a13
    - Operacion_seguimiento_periodico_aplicacion_medicion_riesgo_eeac2c
    - Operacion_seguimiento_permisos_de_embarques_en_el_exterior_c82ddc
    - Operacion_seleccion_alternativa_de_entidad_nominada_por_primer_ingreso_9dce1e
    - Operacion_seleccion_de_calificaciones_para_exposicion_455555
    - Operacion_seleccion_de_entidad_nominada_por_exportacion_e53ec6
    - Operacion_seleccion_inicial_de_entidad_nominada_cf3073
    - Operacion_seleccion_inicial_de_entidad_nominada_por_exportador_144778
    - Operacion_separacion_y_agregacion_de_operaciones_por_conjunto_de_cobertura_9ad803
    - Operacion_sistema_de_incentivos_economicos_al_personal_2ce27a
    - Operacion_sistema_de_retribuciones_y_sistema_de_incentivos_economicos_6b4bb5
    - Operacion_solicitud_de_declaracion_jurada_debida_diligencia_ocde_cf4312
    - Operacion_solicitud_de_exclusion_de_la_central_ced256
    - Operacion_solicitud_de_productos_o_servicios_financieros_3520fd
    - Operacion_subrogacion_de_derechos_de_cobro_por_aseguradora_8a2df0
    - Operacion_suministro_de_datos_cheques_de_pago_diferido_1e6869
    - Operacion_suministro_de_informacion_de_atributos_juridicos_y_representantes_de_persona_jur_182da3
    - Operacion_suministro_de_informacion_de_identidad_y_datos_personales_de_persona_humana_9930bf
    - Operacion_supervision_consolidada_de_entidades_financieras_a00b1d
    - Operacion_suscripcion_bopreal_no_residentes_602ad0
    - Operacion_suscripcion_bopreal_por_deuda_pendiente_2adc56
    - Operacion_suscripcion_bopreal_por_importadores_d218dc
    - Operacion_suscripcion_bopreal_por_importadores_servicios_94b293
    - Operacion_suscripcion_bopreal_por_utilidades_dividendos_5c082b
    - Operacion_suscripcion_de_bonos_para_reconstruccion_de_argentina_libre_bopreal_d620a7
    - Operacion_suscripcion_de_bopreal_a24f7f
    - Operacion_suscripcion_de_bopreal_por_deudores_eeabbe
    - Operacion_suspension_de_debito_debito_automatico_8239ad
    - Operacion_suspension_de_operaciones_en_divisas_400827
    - Operacion_sustraccion_de_cheques_y_documentos_861ea8
    - Operacion_swap_descripcion_activo_subyacente_0940d1
    - Operacion_swap_especificacion_activo_comprado_vendido_1ac520
    - Operacion_swap_informacion_de_nocional_17f2a9
    - Operacion_swap_precio_pactado_tramo_fijo_9a3792
    - Operacion_tarea_de_clasificacion_71550f
    - Operacion_tenencia_de_activos_posiciones_compradas_y_vendidas_a974ed
    - Operacion_tenencia_de_efectivo_en_caja_transito_y_cajeros_automaticos_d44d8d
    - Operacion_tenencia_de_instrumentos_tlac_684a59
    - Operacion_tenencia_de_oro_amonedado_o_barras_buena_entrega_028209
    - Operacion_tenencia_de_titulos_de_credito_fisicamente_fuera_de_la_entidad_965909
    - Operacion_tenencia_de_titulos_valores_del_exterior_e03e90
    - Operacion_titulizacion_con_facilidades_de_credito_rotativas_5c63c1
    - Operacion_titulizacion_con_opcion_de_exclusion_incompleta_01496e
    - Operacion_titulizacion_sintetica_con_adquisicion_de_proteccion_bea652
    - Operacion_titulizacion_sintetica_con_compra_de_proteccion_por_tramos_39e0ab
    - Operacion_titulizacion_tradicional_6f56d4
    - Operacion_titulizacion_tradicional_con_posicion_de_maxima_preferencia_e4c1b2
    - Operacion_tramite_aduanero_por_ingreso_de_bienes_a_zonas_francas_60d69c
    - Operacion_transferencia_al_exterior_de_fondos_no_residente_acreedor_vpu_b845cc
    - Operacion_transferencia_bonos_bopreal_a_depositarios_en_exterior_90eb82
    - Operacion_transferencia_de_cheques_de_pago_diferido_para_negociacion_bursatil_fb6f47
    - Operacion_transferencia_de_cheques_diferidos_para_negociacion_bursatil_8523f7
    - Operacion_transferencia_de_cheques_mediante_endoso_eae465
    - Operacion_transferencia_de_fondos_a_cuentas_en_psp_546d15
    - Operacion_transferencia_de_fondos_a_saldos_inmovilizados_59a8ec
    - Operacion_transferencia_de_fondos_con_informacion_del_beneficiario_a66d8a
    - Operacion_transferencia_de_responsabilidad_a_terceros_c0954a
    - Operacion_transferencia_de_riesgo_de_exposicion_en_tramos_e49548
    - Operacion_transferencia_de_saldos_de_depositos_282eb9
    - Operacion_transferencia_de_titulos_valores_a_entidades_depositarias_del_exterior_5edfa0
    - Operacion_transferencia_directa_de_fondos_a_cuenta_local_del_cliente_bfe94d
    - Operacion_transferencia_fondos_a_cuentas_inversion_administradores_exterior_a94a89
    - Operacion_transferencia_moneda_cuenta_misma_moneda_1627c8
    - Operacion_transferencia_moneda_extranjera_representaciones_diplomaticas_b4e508
    - Operacion_transferencia_real_de_activos_titulizacion_c2537f
    - Operacion_transferencia_titulos_valores_a_depositarios_exterior_9a393f
    - Operacion_transferencias_con_destino_a_cuentas_a_la_vista_para_uso_judicial_d1c05c
    - Operacion_transferencias_desde_cuentas_a_la_vista_para_uso_judicial_2ae517
    - Operacion_transferencias_ordenadas_por_cuentacorrentista_6dd714
    - Operacion_transformacion_de_entidades_financieras_2a8c78
    - Operacion_transmision_de_certificado_por_endoso_6ff931
    - Operacion_transmision_endoso_a_otros_sujetos_b3557c
    - Operacion_transmision_integra_de_echeq_al_repositorio_c8cba5
    - Operacion_tratamiento_acciones_preferidas_convertibles_05e94d
    - Operacion_tratamiento_de_exposiciones_subyacentes_titulizacion_tradicional_cb8889
    - Operacion_tratamiento_de_opciones_0f920f
    - Operacion_tratamiento_de_posiciones_en_fondos_20c13b
    - Operacion_tratamiento_de_titulos_bopreal_post_recompra_3e549b
    - Operacion_tratamiento_depositos_sin_vencimiento_f3656a
    - Operacion_tratamiento_proporcional_de_cobertura_de_riesgo_de_credito_72f2ec
    - Operacion_tratamiento_segun_punto_3_1_13_3_6aff6d
    - Operacion_tratamiento_titulos_vendidos_recomprados_pase_pasivo_2f38da
    - Operacion_tratamiento_y_resolucion_de_consultas_y_reclamos_f61064
    - Operacion_uso_de_cajeros_automaticos_fb3600
    - Operacion_uso_de_cheques_en_cuentas_corrientes_247103
    - Operacion_uso_de_nombre_apellido_rectificado_genero_499e51
    - Operacion_uso_de_tarjetas_magneticas_en_cajeros_automaticos_1361d1
    - Operacion_uso_del_enfoque_estandarizado_para_ponderadores_de_titulizacion_0929c6
    - Operacion_utilizacion_de_calificaciones_crediticias_ecai_4d0878
    - Operacion_utilizacion_de_fondos_de_pgc_para_pagos_a_proveedores_bb9393
    - Operacion_utilizacion_de_garantias_en_cobertura_de_riesgo_d37883
    - Operacion_utilizacion_de_instrumentos_y_metodologia_de_pago_29c114
    - Operacion_utilizacion_de_subcuentas_3da36b
    - Operacion_utilizacion_de_tecnologia_para_reproduccion_de_firmas_digitalizadas_ec4cc0
    - Operacion_valuacion_a_mercado_de_posiciones_0b9aa4
    - Operacion_valuacion_a_mercado_o_a_modelo_de_posiciones_8cdc20
    - Operacion_valuacion_a_modelo_7696c2
    - Operacion_valuacion_de_posiciones_menos_liquidas_c103fd
    - Operacion_valuacion_diaria_a_precios_de_mercado_34c4b8
    - Operacion_valuacion_posiciones_a_termino_moneda_extranjera_y_oro_4e7d52
    - Operacion_venta_bonos_bopreal_con_liquidacion_en_moneda_extranjera_6553d5
    - Operacion_venta_con_obligacion_de_recompra_bopreal_60f4d5
    - Operacion_venta_de_cheques_de_mostrador_4ed52b
    - Operacion_venta_de_cheques_de_pago_financiero_4725d0
    - Operacion_venta_de_divisas_con_debito_en_cuentas_e8a4d4
    - Operacion_venta_de_titulos_valores_con_liquidacion_en_moneda_extranjera_4af05a
    - Operacion_venta_de_titulos_valores_contra_cable_en_exterior_554147
    - Operacion_venta_interna_de_bienes_previo_al_registro_aduanero_598fbb
    - Operacion_venta_titulos_valores_con_liquidacion_moneda_extranjera_exterior_8bd351
    - Operacion_venta_titulos_valores_mercado_secundario_64b088
    - Operacion_verificacion_consistencia_con_registros_aduaneros_99ecc2
    - Operacion_verificacion_de_condiciones_para_operaciones_de_exportacion_c651d4
    - Operacion_verificacion_de_identidad_de_presentantes_22c750
    - Operacion_verificacion_de_secuencia_numerica_de_cheques_y_formulas_a0b2a4
    - Operacion_verificacion_destinacion_exportacion_ante_aduana_94e920
    - Operacion_verificacion_independiente_de_precios_datos_a31d4d
    - Operacion_verificacion_previa_a_certificacion_c5f0b6
    - Operacion_vigilancia_del_sistema_de_incentivos_economicos_92765a
Potestad: 98 sin aplica_a
    - Potestad_acceso_mercado_cambios_para_pagos_de_servicios__las_entidades_podran_dar_acceso__3e413b
    - Potestad_acceso_precancelacion_lineas_credito_financiacion_precancelada_deudor__tambien_p_f17c28
    - Potestad_admision_de_pago_desde_fecha_estimada_de_embarque_para_emisiones_posteriores_a_1_c31dd8
    - Potestad_admision_pago_a_vista_desde_fecha_embarque_mas_15_dias__se_admitira_que_el_pago__850400
    - Potestad_admision_unificacion_registro_firmas_en_tarjeta_unica__se_admitira_la_unificacio_35ae61
    - Potestad_alcance_de_efectos_de_la_autorizacion_otorgada__la_autorizacion_que_se_otorgue_p_86f189
    - Potestad_alta_gerencia_adopcion_de_decisiones_gerenciales__es_recomendable_que_la_alta_ge_3ac088
    - Potestad_aplicacion_ampliada_hasta_40_anual_de_permisos__los_casos_previstos_en_el_punto__ff49e7
    - Potestad_aplicacion_de_tratamiento_otc_a_estructura_multinivel__este_tratamiento_tambien__457436
    - Potestad_aplicacion_de_valor_k_por_defecto__en_tanto_no_se_comunique_la_calificacion_asig_3e3da6
    - Potestad_asignacion_de_ponderador_especifico_partidas_12100000_y_1222000__solo_para_las_p_90a9cd
    - Potestad_autoridad_aplicacion_fija_terminos_cobros_divisas__la_autoridad_de_aplicacion_fi_264816
    - Potestad_autoridad_competente_ordena_modificacion_dni__a_instancias_de_autoridad_competen_c74168
    - Potestad_autorizacion_del_bcra_para_operaciones_de_cambio__el_banco_central_de_la_republi_495a3c
    - Potestad_autorizacion_previa_de_aportes_en_titulos_valores__la_sefyc_queda_facultada_para_5eb7eb
    - Potestad_autorizar_conformidad_incremento_tenencias__el_bcra_podra_otorgar_conformidad_pr_a12c93
    - Potestad_bcra_abrira_cuentas_corrientes_especiales__el_bcra_abrira_dos_cuentas_corrientes_50434e
    - Potestad_bcra_determina_qccp_en_jurisdiccion_sin_principios__en_caso_de_que_la_ccp_este_l_96caec
    - Potestad_buena_practica_miembros_independientes_con_gestion_de_riesgos__se_considera_como_cb68ef
    - Potestad_cancelacion_intereses_desde_fecha_financiacion__tambien_se_admitira_la_cancelaci_4ab52c
    - Potestad_cliente_puede_ser_reclasificado_por_unica_vez__el_cliente_podra_ser_reclasificad_8780e1
    - Potestad_compensacion_de_lados_diferentes_de_swaps__sujeto_a_las_mismas_condiciones_tambi_225e87
    - Potestad_computar_valor_fletes_documentacion_transporte__tambien_se_podra_computar_el_val_6c010b
    - Potestad_computo_del_plazo_en_periodo_de_no_utilizacion__dicho_plazo_podra_computarse_com_e01901
    - Potestad_computo_plazo_como_periodo_no_utilizacion_beneficio__dicho_plazo_podra_computars_6efeb7
    - Potestad_comunicacion_de_caracteristicas_de_seguimiento__las_caracteristicas_del_seguimie_06317b
    - Potestad_conformidad_previa_del_bcra_acceso_anticipado__el_acceso_al_mercado_de_cambios_a_ac74c1
    - Potestad_consideracion_alternativa_fondos_acreditados_en_exterior__en_el_caso_de_fondos_p_a50415
    - Potestad_considerar_operacion_garantizada_por_agencia_oficial_credito__las_entidades_podr_47124e
    - Potestad_decision_direccion_general_de_aduanas__la_direccion_general_de_aduanas_decide_si_2df5cc
    - Potestad_derecho_a_informacion_clara_y_accesible__los_usuarios_tienen_derecho_a_recibir_i_87190c
    - Potestad_derecho_a_libertad_de_eleccion__los_usuarios_de_servicios_financieros_tienen_der_9f6981
    - Potestad_derecho_a_proteccion_de_seguridad_e_intereses_economicos__los_usuarios_de_servic_6c39e6
    - Potestad_derecho_a_trato_equitativo_y_digno__los_usuarios_de_servicios_financieros_tienen_ae7d19
    - Potestad_descalce_en_obligacion_de_determinacion_de_evento_de_credito__se_permite_un_desc_97e47c
    - Potestad_descalce_entre_obligacion_subyacente_y_de_referencia__se_admitira_que_el_derivad_bfbe41
    - Potestad_designacion_de_veedor_por_sefyc__la_superintendencia_de_entidades_financieras_y__77c80d
    - Potestad_dni_d_en_formato_credencial_virtual_para_dispositivos_moviles__el_dni_d_en_forma_ece59e
    - Potestad_encargo_a_organismo_externo_evaluacion__la_evaluacion_anual_puede_ser_encargada__a1d5fa
    - Potestad_encomendar_tarea_de_clasificacion__la_tarea_de_clasificacion_podra_ser_encomenda_b86b11
    - Potestad_entidades_podran_dar_acceso_pago_intereses_y_capital_operaciones_14_2_1__en_el_m_a580ce
    - Potestad_entidades_podran_dar_acceso_pagos_capital_porcion_proporcional_fondos_parciales__3f679f
    - Potestad_entidades_podran_dar_acceso_pagos_intereses_porcion_proporcional_fondos_parciale_4fec25
    - Potestad_exclusion_de_responsabilidad_por_inconsistencias_en_datos__el_banco_central_de_l_bbdcc1
    - Potestad_exigencia_de_otros_comites_normas_bcra__los_citados_comites_no_son_excluyentes_d_60519c
    - Potestad_extension_plazo_operaciones_contraparte_vinculada__se_podra_extender_el_plazo_ha_79369a
    - Potestad_facultad_criterio_de_imputacion_de_conceptos_a_cancelacion__la_forma_en_que_se_i_fee150
    - Potestad_facultad_de_cliente_certificado_de_acceder_a_divisas__el_cliente_que_cuente_con__956d2b
    - Potestad_facultad_de_otorgar_acceso_mercado_de_cambios__la_entidad_interviniente_podra_da_7f4708
    - Potestad_facultad_de_solicitar_certificacion__a_solicitud_del_importador_la_entidad_proce_9344a9
    - Potestad_facultad_metodos_especificos_de_evaluacion_de_capacidad__no_sera_obligatoria_la__204220
    - Potestad_fiduciario_o_administrador_no_financiero_basarse_en_regimen_de_supervision__en_e_8ea53d
    - Potestad_fondos_en_cuentas_de_entidades_financieras_del_exterior__los_fondos_tambien_podr_ccf65a
    - Potestad_implementacion_de_programas_de_capacitacion_comite_de_auditoria__el_comite_de_au_97887c
    - Potestad_inclusion_diversa_de_exposiciones_subyacentes__las_exposiciones_subyacentes_a_la_e2a3c7
    - Potestad_inclusion_en_partida_12700000_ajuste_niif_no_asignado__cuando_no_resulte_factibl_ef3b8e
    - Potestad_liberacion_de_pagos_a_cargo_de_arca_certificacion__la_certificacion_de_cumplido__315350
    - Potestad_libertad_de_pacto_en_tipo_de_cambio__las_operaciones_de_cambio_en_divisas_extran_9aebd8
    - Potestad_mantencion_de_negociabilidad_cheque_imputado_endosado__cuando_el_destinatario_de_46d4dd
    - Potestad_mantenimiento_de_clasificacion_en_planillas_separadas__a_los_fines_de_la_actuali_cf9cc6
    - Potestad_medios_de_presentacion_presencial_o_electronico__las_presentaciones_o_actualizac_ebcf37
    - Potestad_modificacion_posterior_de_entidad_nominada__el_importador_podra_modificar_poster_878aea
    - Potestad_obligacion_de_referencia_distinta_en_liquidacion_efectivo__si_la_obligacion_de_r_ec4322
    - Potestad_opcion_de_admitir_negociacion_bursatil_de_cheques__el_titular_puede_optar_por_ad_074564
    - Potestad_opcion_de_solicitar_datos_en_momento_de_solicitud_de_credito__los_clientes_tiene_04d834
    - Potestad_opcion_rescision_sin_cargo_antes_de_vigencia__el_usuario_de_servicios_financiero_954f33
    - Potestad_pago_fletes_a_partir_embarque_punto_10_10_2_1__el_pago_podra_realizarse_a_partir_efdbc9
    - Potestad_permitir_al_cliente_prefinanciaciones_con_fondeo__permitiran_al_cliente_acceso_a_02bd29
    - Potestad_potestad_bcra_debito_por_falseamiento__el_bcra_a_pedido_de_la_anses_esta_faculta_688063
    - Potestad_potestad_de_los_clientes_para_suscribir_bopreal__los_clientes_podran_suscribir_b_ad2471
    - Potestad_potestad_de_tomar_concepto_de_condicion_de_compra_para_valor__a_los_efectos_del__b55ba2
    - Potestad_reclasificacion_a_nivel_superior_si_otras_deudas_cumplen_condiciones__el_deudor__7346b7
    - Potestad_reclasificacion_a_nivel_superior_tras_pago_de_3_cuotas_sin_atraso__los_clientes__c71560
    - Potestad_reclasificacion_a_niveles_superiores__podra_reclasificarselo_en_niveles_superior_138478
    - Potestad_reclasificacion_a_niveles_superiores_si_se_levanta_pedido_de_quiebra__en_caso_de_4135e9
    - Potestad_reclasificacion_a_situacion_normal_por_cumplimiento_de_convenios__cuando_se_obse_2cff4c
    - Potestad_reclasificacion_a_situacion_normal_tras_pago_de_intereses__cuando_al_menos_se_ha_3bba33
    - Potestad_reclasificacion_inicial_sujeta_a_no_objecion_sefyc__la_reclasificacion_inicial_d_042421
    - Potestad_reconocimiento_parcial_cuando_reestructuracion_no_contemplada__cuando_la_reestru_4fa2d6
    - Potestad_recordatorios_periodicos_posteriores_recomendaciones__sin_perjuicio_de_la_obliga_c8180c
    - Potestad_reducir_exigencia_de_capital_de_manera_proporcional__se_admitira_reducir_la_exig_b0505b
    - Potestad_reimputacion_de_cobros_bienes_reemplazados__el_monto_que_surja_de_la_utilizacion_5d9de8
    - Potestad_requerir_certificado_echeq_rechazado__el_tenedor_legitimado_de_un_echeq_rechazad_1fbee1
    - Potestad_requerir_registro_de_cheque_diferido_en_forma_directa__el_titular_de_una_cuenta__6543dd
    - Potestad_resolucion_de_procedimiento_segun_seccion_7__se_estara_a_lo_dispuesto_en_la_secc_12705c
    - Potestad_sefyc_disponer_exclusiones_en_materia_deductiva__la_sefyc_podra_disponer_exclusi_59af78
    - Potestad_seguimiento_del_estado_de_presentacion__el_usuario_de_servicios_financieros_tien_163720
    - Potestad_seleccion_posterior_de_entidad__en_caso_de_que_el_importador_no_haya_nominado_a__91f507
    - Potestad_solicitar_ampliacion_de_plazo_hasta_quinto_dia_habil__el_exportador_podra_solici_fcc817
    - Potestad_solicitar_nota_escrita_con_resolucion__si_el_tramite_ha_finalizado_el_usuario_de_fbe8b2
    - Potestad_solicitud_de_conformidad_bcra_ampliacion_mayor__agotados_los_plazos_que_puede_ot_32bc73
    - Potestad_supervision_de_actuacion_de_sujetos_obligados__el_banco_central_de_la_republica__257fd2
    - Potestad_suscripcion_bopreal_hasta_monto_de_deuda__los_clientes_podran_suscribir_bonos_pa_3af7f4
    - Potestad_tenedor_legitimado_presentar_echeq_al_cobro__el_tenedor_legitimado_podra_efectua_c2a4c0
    - Potestad_uso_de_garantias_acumuladas_para_pago_de_servicios__las_garantias_acumuladas_en__5e3088
    - Potestad_utilizacion_de_correo_electronico_para_notificacion__se_admite_utilizar_correo_e_527154
    - Potestad_validez_instrumentos_compensables_emitidos_con_datos_anteriores__los_cheques_com_0b0ded
    - Potestad_verificacion_de_no_distorsion_de_saldos__la_sefyc_verificara_que_no_se_distorsio_aa14a5
Restriccion: 207 sin aplica_a
    - Restriccion_0_cero_por_ciento_de_obligacion_de_ingreso_y_o_liquidacion_del_contravalor_en_di_fa0eaa
    - Restriccion_100_ciento_por_ciento_de_obligacion_de_ingreso_y_o_liquidacion_del_contravalor_e_5219ec
    - Restriccion_10_diez_por_ciento_cuando_corresponda_a_bienes_que_tienen_asignado_un_plazo_de_6_8301b0
    - Restriccion_20_veinte_por_ciento_de_obligacion_de_ingreso_y_o_liquidacion_del_contravalor_en_24531f
    - Restriccion_40_cuarenta_por_ciento_de_obligacion_de_ingreso_y_o_liquidacion_del_contravalor__507a6c
    - Restriccion_5_cinco_por_ciento_cuando_corresponda_a_bienes_que_tienen_asignado_un_plazo_de_3_f0003d
    - Restriccion_a_los_efectos_del_cumplimiento_del_citado_punto_se_debera_contar_con_calificacio_0c8789
    - Restriccion_a_razon_de_un_maximo_mensual_equivalente_al_10_diez_por_ciento_del_monto_total_d_50e0a0
    - Restriccion_a_razon_de_un_maximo_mensual_equivalente_al_10_diez_por_ciento_del_monto_total_d_c38fe7
    - Restriccion_al_momento_de_la_evaluacion_no_debera_existir_evidencia_que_indique_la_posibilid_08547d
    - Restriccion_banco_de_pagos_internacionales_fondo_monetario_internacional_banco_central_europ_558809
    - Restriccion_contener_endosos_que_excedan_el_limite_establecido_en_el_punto_5_1_1__ctacte_6_1_396a01
    - Restriccion_cuando_el_futuro_o_forward_permita_entregar_una_gama_de_instrumentos_la_exclusio_79a765
    - Restriccion_cuando_la_entidad_tenga_multiples_posiciones_a_riesgo_en_instrumentos_de_credito_43f714
    - Restriccion_cuando_la_suma_de_los_requisitos_de_capital_de_una_entidad_financiera_por_exposi_496100
    - Restriccion_cuando_se_cumple_compensacion_integra_de_ambos_lados_ningun_lado_de_la_operacion_20bc53
    - Restriccion_cuando_se_referencie_a_un_unico_deudor_sf_credito_se_determina_en_funcion_de_su__170a1f
    - Restriccion_cuando_se_trate_de_depositos_y_otras_obligaciones_por_intermediacion_financiera__a63a39
    - Restriccion_cuando_se_trate_de_futuros_la_exclusion_solo_procedera_si_los_nocionales_e_instr_4f50a0
    - Restriccion_cuando_se_verifica_compensacion_de_riesgo_especifico_en_operaciones_de_cobertura_84a4a7
    - Restriccion_derivados_que_hagan_referencia_a_indice_de_acciones_se_tratan_como_si_hicieran_r_a40721
    - Restriccion_derivados_que_hagan_referencia_a_indices_de_credito_se_consideran_como_si_hicier_dd7286
    - Restriccion_dicha_comprobacion_podra_efectuarse_una_vez_transcurrido_el_citado_termino_de_10_07688d
    - Restriccion_dichas_operaciones_deberan_haber_sido_autorizadas_por_la_aduana__ext_8_5_17_26_6bb4f4
    - Restriccion_el_acceso_al_mercado_de_cambios_debera_producirse_una_vez_transcurridos_como_min_17f3a1
    - Restriccion_el_acceso_al_mercado_de_cambios_debera_producirse_una_vez_transcurridos_como_min_b4823b
    - Restriccion_el_acceso_al_mercado_de_cambios_debera_producirse_una_vez_transcurridos_como_min_f46ecb
    - Restriccion_el_acceso_al_mercado_de_cambios_no_podra_exceder_el_monto_de_la_certificacion_de_f1f345
    - Restriccion_el_acceso_al_mercado_de_cambios_para_la_repatriacion_de_inversiones_de_no_reside_819232
    - Restriccion_el_acceso_al_mercado_de_cambios_se_produce_no_antes_de_los_2_dos_anos_corridos_c_b9d9dc
    - Restriccion_el_agregado_de_hojas_solo_procedera_por_razones_de_espacio__ctacte_5_1_7_803aa2
    - Restriccion_el_ajuste_por_apalancamiento_al_requisito_de_capital_por_participacion_en_fondo__b9521e
    - Restriccion_el_bcra_debitara_de_la_cuenta_corriente_de_la_entidad_el_importe_correspondiente_521774
    - Restriccion_el_bcra_debitara_de_la_cuenta_corriente_de_la_entidad_una_multa_equivalente_al_d_844239
    - Restriccion_el_cliente_no_ha_utilizado_este_mecanismo_por_un_monto_superior_al_equivalente_d_59f2a5
    - Restriccion_el_cuentacorrentista_quedara_incurso_en_la_situacion_a_que_se_refiere_el_punto_8_9cde3e
    - Restriccion_el_cumplimiento_de_obligaciones_tiene_lugar_cuando_no_se_recurra_a_nuevas_financ_f4164a
    - Restriccion_el_doble_del_periodo_de_riesgo_de_margen_para_conjuntos_de_neteo_con_disputas_pe_a32c59
    - Restriccion_el_exceso_a_los_limites_para_la_afectacion_de_activos_en_garantia_segun_lo_dispu_a7eca2
    - Restriccion_el_importador_no_haya_hecho_uso_de_esta_alternativa_por_un_monto_mayor_al_equiva_a8ff52
    - Restriccion_el_inversor_no_tendra_ningun_derecho_a_acelerar_la_devolucion_de_los_pagos_futur_0fac34
    - Restriccion_el_lapso_convenido_no_podra_superar_los_5_dias_habiles_bancarios__ctacte_5_5_2_d0e147
    - Restriccion_el_monto_acumulado_de_las_certificaciones_aplicadas_no_supera_el_monto_del_aport_3dadf9
    - Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_no_debe_ser_52def0
    - Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_no_podra_ex_ddef79
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_de_los_nuevos_titulos_en_ningu_3a852e
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_de_los_nuevos_titulos_en_ningu_562076
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_en_nin_13aade
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_en_nin_a2451c
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_en_nin_db9de7
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_en_nin_fa0531
    - Restriccion_el_monto_total_abonado_por_este_mecanismo_no_supere_el_equivalente_al_5_cinco_po_0534d9
    - Restriccion_el_monto_total_de_deudas_abonadas_en_el_mes_calendario_bajo_este_mecanismo_no_su_6132c6
    - Restriccion_el_pago_debia_resultar_elegible_de_acuerdo_con_lo_dispuesto_en_el_punto_4_6_1__e_3f2f80
    - Restriccion_el_pago_no_supere_el_equivalente_al_50_cincuenta_por_ciento_del_monto_liquidado__7850c6
    - Restriccion_el_periodo_de_plazo_regulatorio_no_podra_ser_menor_que_10_dias_habiles__cap_4_2__0c8e33
    - Restriccion_el_ponderador_aplicable_a_las_coberturas_provistas_por_swaps_de_incumplimiento_c_72ba80
    - Restriccion_el_ponderador_aplicable_a_las_coberturas_provistas_por_swaps_de_incumplimiento_c_f993eb
    - Restriccion_el_ponderador_de_riesgo_de_la_parte_de_la_exposicion_cubierta_podra_ser_inferior_6ef649
    - Restriccion_el_ponderador_de_riesgo_de_las_exposiciones_a_entidades_financieras_no_puede_ser_c4fa7d
    - Restriccion_el_ponderador_de_riesgo_se_aplica_al_55_del_valor_del_inmueble_la_porcion_que_no_e0fc75
    - Restriccion_el_ponderador_de_riesgo_sera_del_150_o_el_que_resulte_de_multiplicar_por_1_5_el__28b1cd
    - Restriccion_el_ponderador_sera_de_10_para_coberturas_por_swaps_de_incumplimiento_crediticio__c55228
    - Restriccion_el_presente_punto_detalla_el_computo_de_la_exigencia_de_capital_para_cubrir_ries_3e537a
    - Restriccion_el_producto_del_ponderador_de_riesgo_promedio_del_fondo_y_el_apalancamiento_del__a66280
    - Restriccion_el_programa_de_encuadramiento_no_debera_superar_los_6_meses_de_plazo_para_cumpli_b1b82b
    - Restriccion_el_rechazo_total_de_la_presentacion_procedera_toda_vez_que_se_observen_por_lo_me_29d6ae
    - Restriccion_el_tratamiento_en_el_marco_de_la_ley_de_emergencia_agropecuaria_no_podra_implica_b94c1b
    - Restriccion_el_valor_de_mercado_de_estas_operaciones_no_supere_a_la_diferencia_entre_el_valo_5faea0
    - Restriccion_el_valor_de_mercado_de_otras_ventas_de_titulos_valores_no_debe_superar_la_difere_6e7ab8
    - Restriccion_el_valor_nominal_de_los_nuevos_titulos_entregados_en_concepto_de_prima_de_partic_2af558
    - Restriccion_en_caso_de_que_las_modificaciones_se_originen_en_un_error_operativo_que_afecte_e_932fa7
    - Restriccion_en_defecto_de_presentacion_al_cobro_el_echeq_quedara_pendiente_hasta_la_fecha_de_c01626
    - Restriccion_en_derivados_de_credito_de_enesimo_incumplimiento_con_n_mayor_que_1_no_se_permit_84681b
    - Restriccion_en_el_caso_de_que_el_cliente_no_sea_una_persona_humana_y_se_haya_constituido_has_b51af1
    - Restriccion_en_el_caso_de_que_el_monto_adeudado_fuera_superior_a_usd_25_000__ext_9_3_7_eedc89
    - Restriccion_en_el_caso_de_una_extraccion_con_una_tarjeta_prepaga_sera_de_aplicacion_el_limit_7282fd
    - Restriccion_en_la_medida_en_que_dichas_cartas_de_credito_sean_irrestrictas__polcre_2_1_17_d9aae0
    - Restriccion_en_ningun_caso_el_registro_del_cheque_podra_demorarse_mas_de_15_dias_corridos__c_4e1283
    - Restriccion_en_un_derivado_con_intercambios_multiples_del_principal_el_nocional_se_multiplic_6b306d
    - Restriccion_endeudamientos_financieros_comprendidos_en_el_punto_3_5__ext_7_9_1_5_93526f
    - Restriccion_esa_certificacion_mantendra_vigencia_durante_90_dias_corridos_desde_la_fecha_a_l_fb15f9
    - Restriccion_esta_alternativa_solo_sera_valida_en_la_medida_que_en_el_ano_calendario_consider_5d94d5
    - Restriccion_esta_opcion_estara_disponible_hasta_alcanzar_el_125_ciento_veinticinco_por_cient_d09e6c
    - Restriccion_esta_reduccion_de_la_ead_por_las_perdidas_por_cva_incurridas_no_se_aplica_para_l_315b51
    - Restriccion_hasta_un_tope_de_usd_5_000_dolares_estadounidenses_cinco_mil__ext_8_5_17_20_8e3460
    - Restriccion_la_aceptacion_de_cheques_no_procede_cuando_medie_orden_judicial_en_contrario__ct_09fd9c
    - Restriccion_la_aceptacion_de_presentaciones_efectuadas_durante_el_periodo_de_presentacion_ta_2baf1e
    - Restriccion_la_cantidad_de_registros_con_inconsistencias_en_alguno_de_los_archivos_supera_el_a431bf
    - Restriccion_la_capitalizacion_de_deuda_no_podra_implicar_una_limitacion_o_suspension_al_dere_aafe23
    - Restriccion_la_certificacion_de_auditor_externo_es_requerida_cuando_el_monto_a_imputar_super_0f23b1
    - Restriccion_la_cuenta_de_terceros_no_debe_encontrarse_radicada_en_paises_o_territorios_donde_3adde0
    - Restriccion_la_denuncia_de_extravio_sustraccion_o_adulteracion_genera_la_imposibilidad_de_pr_924474
    - Restriccion_la_deuda_del_cliente_por_todo_concepto_mas_el_importe_de_la_financiacion_solicit_f0ae07
    - Restriccion_la_ead_para_un_conjunto_de_neteo_con_margenes_de_variacion_tendra_como_limite_su_fe9655
    - Restriccion_la_emision_de_estas_certificaciones_solo_se_podra_realizar_una_vez_inhabilitado__c6009e
    - Restriccion_la_entidad_del_exterior_sobre_la_cual_se_gira_el_cable_no_debera_estar_constitui_5b8eec
    - Restriccion_la_extension_de_los_plazos_no_podra_superar_los_365_trescientos_sesenta_y_cinco__d58bcd
    - Restriccion_la_extension_de_los_plazos_no_podra_superar_los_545_quinientos_cuarenta_y_cinco__e97a2e
    - Restriccion_la_fecha_de_pago_no_puede_exceder_un_plazo_de_360_dias_en_los_cheques_de_pago_di_b15b39
    - Restriccion_la_imputacion_de_multas_solo_procede_cuando_existen_demoras_del_exportador_en_la_a863c1
    - Restriccion_la_nueva_clave_o_contrasena_personal_password_pin_seleccionada_por_el_usuario_no_c54348
    - Restriccion_la_nueva_deuda_financiera_no_podra_anticipar_vencimientos_respecto_de_la_deuda_c_8daa82
    - Restriccion_la_nueva_deuda_no_implique_la_realizacion_de_pagos_antes_de_la_fecha_en_que_el_c_8968ef
    - Restriccion_la_opcion_de_exclusion_no_este_estructurada_con_el_fin_de_evitar_que_los_inverso_7255c6
    - Restriccion_la_operacion_podra_incluir_bienes_que_no_revistan_la_condicion_de_bien_de_capita_0501fe
    - Restriccion_la_operacion_podra_incluir_bienes_que_no_revistan_la_condicion_de_bien_de_capita_4195f2
    - Restriccion_la_operacion_podra_permanecer_en_gestion_de_cobro_mientras_se_demuestre_la_vigen_0f61be
    - Restriccion_la_perdida_por_cva_se_calcula_sin_compensar_con_los_ajustes_de_valuacion_del_deb_9d92db
    - Restriccion_la_recategorizacion_del_deudor_se_efectuara_a_partir_del_mes_siguiente_al_de_pue_e1af72
    - Restriccion_la_recategorizacion_se_efectuara_al_menos_en_la_categoria_inmediata_superior_a_a_198ffe
    - Restriccion_la_retencion_del_cheque_de_pago_diferido_no_podra_exceder_de_5_dias_corridos_con_147203
    - Restriccion_la_sola_existencia_de_5_000_operaciones_o_mas_en_un_conjunto_de_neteo_no_determi_c3dbba
    - Restriccion_la_suscripcion_local_no_supere_el_25_veinticinco_por_ciento_de_la_suscripcion_to_a5dcde
    - Restriccion_la_tacha_de_la_leyenda_de_cheque_para_acreditar_en_cuenta_se_tendra_por_no_hecha_fc7dd7
    - Restriccion_la_titulizacion_no_contiene_clausulas_mediante_las_cuales_la_entidad_financiera__fdcd0c
    - Restriccion_la_titulizacion_no_contiene_clausulas_mediante_las_cuales_se_aumente_el_rendimie_68462e
    - Restriccion_la_titulizacion_no_contiene_clausulas_mediante_las_cuales_se_obligue_a_la_origin_bbd6c1
    - Restriccion_las_acciones_preferidas_no_convertibles_quedan_excluidas_de_la_exigencia_de_capi_4838f2
    - Restriccion_las_calificaciones_crediticias_efectuadas_por_ecai_solo_podran_ser_utilizadas_pa_217484
    - Restriccion_las_facilidades_adicionales_sobre_margenes_vigentes_no_se_consideraran_nuevas_fi_419947
    - Restriccion_las_franquicias_deberan_ser_ponderadas_por_riesgo_al_1250__cap_5_4_4_388f91
    - Restriccion_las_operaciones_bilaterales_con_un_acuerdo_de_margen_de_variacion_unidireccional_d62186
    - Restriccion_las_operaciones_que_impliquen_la_importacion_de_billetes_de_pesos_argentinos_que_40e13f
    - Restriccion_las_participaciones_en_entidades_financieras_del_exterior_son_deducibles__cap_8__25d0d7
    - Restriccion_las_participaciones_en_entidades_financieras_se_deducen_excepto_cuando_rijan_fra_a60c05
    - Restriccion_las_presentaciones_rechazadas_por_los_citados_motivos_se_consideraran_no_efectua_b284dc
    - Restriccion_las_reservas_a_integrar_con_ingresos_futuros_provenientes_de_los_activos_subyace_e3c630
    - Restriccion_las_retribuciones_deben_ser_determinadas_sobre_la_base_de_sumas_fijas_que_no_est_331c7b
    - Restriccion_los_adelantos_previstos_en_el_punto_3_2_5_de_las_normas_sobre_financiamiento_al__2e7086
    - Restriccion_los_adelantos_previstos_en_el_punto_3_2_5_de_las_normas_sobre_financiamiento_al__de2b4d
    - Restriccion_los_arreglos_privados_deben_contar_con_la_opinion_del_auditor_externo_cuando_aun_1f5bf1
    - Restriccion_los_cheques_de_pago_diferido_transferidos_para_negociacion_en_bolsas_de_comercio_01c0bd
    - Restriccion_los_clientes_se_clasificaran_en_categoria_irrecuperable_en_caso_de_no_efectuarse_f3d7ec
    - Restriccion_los_contratos_con_clausulas_de_abandono_o_ruptura_walkaway_clauses_clausulas_que_36b293
    - Restriccion_los_documentos_a_cobrar_y_creditos_transferidos_luego_de_la_fecha_en_que_se_conc_fd66c5
    - Restriccion_los_endeudamientos_financieros_y_o_aportes_de_inversion_extranjera_directa_no_po_a6b389
    - Restriccion_los_estandares_no_deberan_ser_menos_rigurosos_que_aquellos_aplicados_a_los_activ_02613a
    - Restriccion_los_excesos_de_margenes_de_credito_por_lineas_especificas_no_seran_considerados__7ca6b9
    - Restriccion_los_instrumentos_no_deben_estar_ya_incluidos_en_el_co_capital_ordinario__cap_8_2_c20cc1
    - Restriccion_los_nuevos_titulos_de_deuda_contemplen_como_minimo_1_un_ano_de_gracia_para_el_pa_08b194
    - Restriccion_los_pagos_elegibles_solo_se_consideran_comprendidos_en_los_puntos_4_8_1_1_y_4_8__691fd0
    - Restriccion_los_swaps_de_monedas_y_tasas_de_interes_los_fras_los_forwards_de_moneda_y_los_fu_7c2c80
    - Restriccion_monto_maximo_de_usd_50_dolares_estadounidenses_cincuenta_por_operacion_de_adelan_89c383
    - Restriccion_monto_minimo_de_60_000_pesos_sesenta_mil_por_dia_en_una_unica_extraccion_en_caje_a45b48
    - Restriccion_no_computar_las_operaciones_de_financiacion_con_titulos_valores_sft__ric_10_1_4__e0de13
    - Restriccion_no_computar_los_conceptos_correspondientes_a_derivados__ric_10_1_4_1_66bdc9
    - Restriccion_no_correspondera_la_comunicacion_al_bcra_de_los_rechazos__ctacte_6_4_6_4_8dbd24
    - Restriccion_no_deben_considerarse_activos_externos_liquidos_disponibles_a_aquellos_fondos_de_a0693a
    - Restriccion_no_divulgar_el_numero_de_clave_personal__ctacte_12_1_2_3_6dfaa2
    - Restriccion_no_escribir_el_numero_de_clave_personal_en_la_tarjeta_magnetica_provista_o_en_un_93bfc3
    - Restriccion_no_estan_sujetas_a_estas_normas_las_concertaciones_y_cancelaciones_de_operacione_851f8e
    - Restriccion_no_se_han_acompanado_los_soportes_con_los_archivos_requeridos_o_ellos_no_pueden__53aa43
    - Restriccion_no_se_incluyen_clausulas_de_amortizacion_anticipada_que_de_acuerdo_con_lo_previs_9ac207
    - Restriccion_no_se_incluyen_opciones_de_rescision_o_eventos_desencadenantes_de_la_extincion_d_e038d1
    - Restriccion_no_se_permitira_la_exclusion_o_compensacion_de_posiciones_en_diferentes_monedas__6ed5f0
    - Restriccion_no_se_podran_efectuar_mejoras_en_las_clasificaciones_de_los_clientes_si_los_mism_430d4d
    - Restriccion_obligacion_de_ingreso_y_o_liquidacion_por_la_totalidad_del_contravalor_en_divisa_3f2aea
    - Restriccion_para_el_calculo_de_las_variables_a_y_d_la_sobrecolateralizacion_y_los_fondos_int_070fce
    - Restriccion_para_operaciones_sin_margen_de_variacion_el_horizonte_temporal_minimo_sera_el_me_36e536
    - Restriccion_periodo_de_riesgo_de_margen_minimo_de_20_dias_habiles_para_conjuntos_de_neteo_cu_abf3e3
    - Restriccion_periodo_de_riesgo_de_margen_mpor_minimo_de_5_dias_habiles_para_operaciones_de_de_66b039
    - Restriccion_periodo_de_riesgo_de_margen_mpor_minimo_de_al_menos_10_dias_habiles_para_operaci_378e26
    - Restriccion_plazo_minimo_un_ano__polcre_6_1_1_3_2c4b81
    - Restriccion_ponderador_de_riesgo_de_85_para_exposiciones_a_mipyme_que_no_se_ajustan_a_los_cr_3490ef
    - Restriccion_ponderador_de_riesgo_del_100_para_exposiciones_a_entes_del_sector_publico_no_fin_19d6bd
    - Restriccion_ponderador_de_riesgo_del_100_para_exposiciones_a_entes_del_sector_publico_no_fin_793b11
    - Restriccion_ponderador_de_riesgo_del_100_para_exposiciones_a_entes_del_sector_publico_no_fin_fd27ee
    - Restriccion_ponderador_de_riesgo_del_150_para_exposiciones_a_entes_del_sector_publico_no_fin_1758ef
    - Restriccion_ponderador_de_riesgo_del_20_para_exposiciones_a_entes_del_sector_publico_no_fina_ca58ad
    - Restriccion_ponderador_de_riesgo_del_50_para_exposiciones_a_entes_del_sector_publico_no_fina_912e64
    - Restriccion_ponderador_de_riesgo_general_para_exposiciones_a_entidades_financieras_grado_a_4_4d8ae4
    - Restriccion_ponderador_de_riesgo_general_para_exposiciones_a_entidades_financieras_grado_b_7_ccc0d2
    - Restriccion_ponderador_de_riesgo_general_para_exposiciones_a_entidades_financieras_grado_c_1_b249a9
    - Restriccion_ponderador_de_riesgo_para_exposiciones_de_corto_plazo_a_entidades_financieras_gr_8b2b52
    - Restriccion_ponderador_de_riesgo_para_exposiciones_de_corto_plazo_a_entidades_financieras_gr_e45cb7
    - Restriccion_ponderador_de_riesgo_para_exposiciones_de_corto_plazo_a_entidades_financieras_gr_eb39a2
    - Restriccion_que_la_acreditacion_de_los_fondos_se_efectue_en_forma_inmediata_a_simple_requeri_05cfd9
    - Restriccion_queda_exceptuada_de_la_excepcion_la_cancelacion_de_giros_en_descubierto_en_cuent_efeec1
    - Restriccion_reduccion_por_aplicacion_del_limite_del_11_meses_1_a_12__ric_5_2_5_011a03
    - Restriccion_reduccion_por_aplicacion_del_limite_del_14_meses_1_a_12__ric_5_2_5_d02083
    - Restriccion_reduccion_por_aplicacion_del_limite_del_17_meses_1_a_12__ric_5_2_5_737154
    - Restriccion_reduccion_por_aplicacion_del_limite_del_20_entidades_grupo_a_meses_1_a_12__ric_5_ad6a34
    - Restriccion_reduccion_por_aplicacion_del_limite_del_5_meses_1_a_12__ric_5_2_5_8f67ba
    - Restriccion_reduccion_por_aplicacion_del_limite_del_7_meses_1_a_12__ric_5_2_5_1f0421
    - Restriccion_reduccion_por_aplicacion_del_limite_del_8_meses_1_a_12__ric_5_2_5_a748f8
    - Restriccion_repatriaciones_de_inversiones_directas_de_no_residentes_hasta_el_monto_de_los_ap_f58687
    - Restriccion_requiriendo_a_ese_efecto_calificacion_internacional_de_riesgo_investment_grade___ff5119
    - Restriccion_respecto_del_apoyo_crediticio_que_no_supere_el_55_del_valor_del_inmueble_se_apli_36fee9
    - Restriccion_se_aplicara_el_ponderador_de_riesgo_del_75_para_las_exposiciones_a_personas_huma_c1b54d
    - Restriccion_se_aplicara_el_ponderador_de_riesgo_del_85_para_las_exposiciones_a_mipyme__cap_2_d96332
    - Restriccion_se_aplicara_ponderador_de_10_a_entidades_del_exterior_que_no_cumplan_con_lo_prev_96a14a
    - Restriccion_se_aplicaran_los_ponderadores_previstos_en_el_punto_2_12_para_el_resto_de_las_ex_630671
    - Restriccion_se_autorizara_el_libramiento_de_echeq_por_un_importe_global_maximo_en_funcion_de_3e530d
    - Restriccion_se_establece_ponderador_de_0_para_el_sector_publico_no_financiero_y_banco_centra_104909
    - Restriccion_se_establece_ponderador_de_3_para_el_resto_de_las_contrapartes_excepto_que_se_tr_8bb46b
    - Restriccion_se_establece_un_minimo_de_0_al_efecto_de_evitar_que_el_costo_de_reposicion_sea_n_34229b
    - Restriccion_se_permite_compensacion_integra_de_operaciones_de_una_entidad_pero_solo_se_permi_089154
    - Restriccion_se_reconoce_proteccion_crediticia_de_empresas_con_grado_de_inversion_de_acuerdo__75f56c
    - Restriccion_si_se_pudiera_aplicar_mas_de_un_ponderador_a_una_exposicion_determinada_se_deber_f9ffa6
    - Restriccion_si_un_fondo_de_garantia_respalda_productos_sujetos_a_riesgo_de_liquidacion_y_pro_ff5434
    - Restriccion_sobre_el_importe_que_supere_el_55_del_valor_del_inmueble_se_aplicara_el_ponderad_5c36f3
    - Restriccion_solo_la_parte_de_las_reservas_que_este_sujeta_a_la_absorcion_de_perdidas_y_propo_5e4c0e
    - Restriccion_son_nulos_el_endoso_del_girado__ctacte_5_1_5_0da6e1
    - Restriccion_son_nulos_el_endoso_parcial__ctacte_5_1_5_6c63cc
    - Restriccion_su_vida_promedio_sea_no_inferior_a_1_un_ano_considerando_los_vencimientos_de_cap_0b95c5
    - Restriccion_unicamente_el_destinatario_del_pago_puede_endosarlo__ctacte_5_4_0dfbb1
```

### S12 — FAIL

ERROR — Toda Excepcion tiene >=1 arista saliente exceptua o exceptua_obligacion.

**Resultado:** 221 Excepciones sin salida exceptua/exceptua_obligacion.

```
    - Excepcion_a_esos_efectos_no_se_considerara_refinanciacion_la_asistencia_que_se_otorgue_a_l_d58e0e
    - Excepcion_a_fin_de_ser_excluidas_de_la_central_de_cheques_rechazados_y_o_de_la_central_de__28499b
    - Excepcion_acceso_al_mercado_de_cambios_incluso_cuando_no_se_cumplan_los_requisitos_estable_a39a35
    - Excepcion_anticipos_por_pago_de_jubilaciones_y_pensiones_estan_excluidos_de_las_financiaci_ca6c68
    - Excepcion_anticipos_y_prestamos_al_fondo_de_garantia_de_los_depositos_estan_excluidos_de_l_849b30
    - Excepcion_aplicacion_de_exigencia_adicional_de_2_puede_extenderse_a_posiciones_opuestas_en_75792d
    - Excepcion_calculo_del_riesgo_de_tasa_de_interes_en_la_cartera_de_inversion_tendra_frecuenc_0bf3e6
    - Excepcion_contenga_endosos_tachados_o_que_carezcan_de_los_requisitos_formales_establecidos_1230a8
    - Excepcion_contractualmente_no_estuviera_previsto_que_una_facilidad_de_liquidez_cubra_activ_b43186
    - Excepcion_cuando_al_menos_se_haya_cumplido_con_el_pago_sin_haber_incurrido_en_atrasos_supe_0c91be
    - Excepcion_cuando_el_cliente_sea_un_vehiculo_de_proyecto_unico_adherido_al_rigi_que_haya_de_ca4d6b
    - Excepcion_cuando_en_estos_casos_sea_factible_el_computo_de_la_crc_su_reconocimiento_sera_p_2c0908
    - Excepcion_cuando_existan_obstaculos_para_la_rapida_repatriacion_de_beneficios_desde_una_su_d8a545
    - Excepcion_cuando_la_cantidad_escrita_en_letras_difiriese_de_la_expresada_en_numeros_se_est_9f697c
    - Excepcion_cuando_los_adelantos_superen_el_limite_autorizado_y_o_no_sean_cancelados_en_los__28b441
    - Excepcion_cuando_no_corresponda_evaluar_la_capacidad_de_repago_del_deudor_por_encontrarse__8dc813
    - Excepcion_datos_complementarios_vinculados_al_calculo_de_la_exigencia_por_riesgo_de_mercad_917a7d
    - Excepcion_dicho_pago_no_exime_a_la_entidad_de_las_responsabilidades_civiles_que_pudieren_c_b89534
    - Excepcion_el_acceso_al_mercado_de_cambios_antes_de_lo_indicado_no_requerira_conformidad_pr_4045c8
    - Excepcion_el_acceso_al_mercado_de_cambios_antes_de_lo_indicado_se_permite_en_el_caso_de_pr_2f0313
    - Excepcion_el_acceso_tambien_podra_ser_dado_a_los_fideicomisos_constituidos_en_el_pais_para_d870c5
    - Excepcion_el_bcra_establezca_que_se_debe_hacer_una_reduccion_generalizada_del_valor_si_pos_d67fe0
    - Excepcion_el_pago_es_concretado_mediante_canje_y_o_arbitraje_con_fondos_depositados_en_cue_7becd8
    - Excepcion_el_plazo_no_resulta_aplicable_a_las_ventas_que_se_realicen_con_liquidacion_contr_d08314
    - Excepcion_el_plazo_para_realizar_la_denuncia_se_contara_a_partir_de_la_fecha_en_que_tomo_c_b25cbb
    - Excepcion_el_punto_3_16_3_solo_sera_aplicable_para_clientes_que_no_sean_personas_humanas_r_0fbf79
    - Excepcion_el_punto_3_16_3_solo_sera_aplicable_para_clientes_que_no_sean_personas_humanas_r_9e21f3
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_resultara_aplicable_cuando_se_cum_6b45a6
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_54512c
    - Excepcion_el_requisito_de_ingreso_y_liquidacion_de_divisas_se_considera_cumplimentado_para_27ea86
    - Excepcion_en_caso_de_afectacion_de_la_solvencia_y_o_liquidez_de_la_entidad_se_tenga_por_no_4be440
    - Excepcion_en_caso_de_no_efectuarse_la_evaluacion_cualquiera_sea_el_motivo_estos_clientes_s_4567df
    - Excepcion_en_caso_de_no_existir_dicha_jerarquia_la_pertinente_presentacion_estara_a_cargo__7d9c2d
    - Excepcion_en_caso_de_que_alguna_de_las_personas_detallada_en_el_punto_3_16_3_3_sea_un_ente_bca387
    - Excepcion_en_caso_de_que_la_operacion_haya_sido_liquidada_por_mas_de_una_entidad_cada_una__82eb29
    - Excepcion_en_casos_de_datos_provenientes_de_liquidaciones_forzadas_ventas_criticas_o_merca_41c356
    - Excepcion_en_cuanto_a_las_exportaciones_desde_el_territorio_nacional_continental_al_area_f_9eb0fd
    - Excepcion_en_el_caso_de_operaciones_comprendidas_en_el_punto_7_11_1_6_tambien_se_admitira__8bacc5
    - Excepcion_en_el_caso_de_que_las_entidades_financieras_no_ejercieran_esa_opcion_corresponde_446a12
    - Excepcion_en_el_supuesto_de_adulteracion_el_rechazo_del_cheque_no_se_comunicara_cuando_exi_d7b80d
    - Excepcion_en_estos_casos_los_usuarios_de_servicios_financieros_pueden_requerir_y_recibir_i_f50c7d
    - Excepcion_en_estrategias_donde_la_entidad_asuma_posicion_contraria_en_exactamente_el_mismo_55b403
    - Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c_ef574e
    - Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c_f09bfc
    - Excepcion_este_requerimiento_no_sera_de_aplicacion_para_el_caso_de_exposiciones_a_gobierno_89943a
    - Excepcion_este_requisito_no_resultara_aplicable_cuando_se_cumpla_la_totalidad_de_las_sigui_18df73
    - Excepcion_este_requisito_no_sera_de_aplicacion_para_el_sector_publico__ext_10_4_2_6_bea64a
    - Excepcion_este_requisito_no_sera_de_aplicacion_para_las_personas_juridicas_que_tengan_a_su_90b061
    - Excepcion_este_requisito_no_sera_de_aplicacion_para_los_fideicomisos_constituidos_con_apor_06d633
    - Excepcion_este_requisito_no_sera_de_aplicacion_para_todas_las_organizaciones_empresariales_6f291a
    - Excepcion_excepcion_a_la_prohibicion_de_acceso_al_mercado_de_cambios_para_pagos_de_obligac_946421
    - Excepcion_excepcion_de_liquidacion_de_cobros_de_exportaciones_de_bienes_y_servicios_para_l_a4c243
    - Excepcion_excepto_cuando_la_garantia_cubra_unicamente_el_capital_en_cuyo_caso_se_considera_f27c65
    - Excepcion_excepto_para_aquellos_casos_en_que_expresamente_se_prevea_la_posibilidad_de_que__6042e7
    - Excepcion_excepto_que_la_repatriacion_se_concrete_a_partir_de_un_canje_y_o_arbitraje_con_l_6bde71
    - Excepcion_excepto_que_se_trate_de_asociaciones_mutuales_o_cooperativas__pro_1_1_2_5_830979
    - Excepcion_exencion_de_ingreso_de_divisas_para_exportaciones_del_area_aduanera_especial_al__a789ea
    - Excepcion_exportacion_a_consumo_de_automotores_de_fabricacion_nacional_sus_partes_y_piezas_4906fb
    - Excepcion_exportaciones_a_zonas_francas_nacionales_estan_exceptuadas_del_seguimiento_de_pe_7d3913
    - Excepcion_exportaciones_de_bienes_enviados_al_exterior_con_fines_promocionales_estan_excep_b1eaad
    - Excepcion_exportaciones_desde_el_territorio_nacional_continental_al_area_aduanera_especial_da482e
    - Excepcion_financiaciones_y_avales_fianzas_y_otras_responsabilidades_otorgados_por_subsidia_7d2233
    - Excepcion_financiaciones_y_avales_fianzas_y_otras_responsabilidades_otorgados_por_sucursal_91562a
    - Excepcion_garantias_otorgadas_a_favor_del_bcra_y_por_obligaciones_directas_quedan_excluida_75470f
    - Excepcion_haberse_dispuesto_medidas_cautelares_sobre_los_fondos_destinados_para_el_pago_de_52d740
    - Excepcion_incluso_cuando_no_se_cumplan_los_requisitos_establecidos_para_el_acceso_del_clie_8ee7c7
    - Excepcion_informacion_sobre_ratio_de_apalancamiento_seccion_10_tendra_frecuencia_trimestra_24c8fc
    - Excepcion_la_cancelacion_de_pagos_en_concepto_de_dividendos_o_intereses_no_debera_constitu_5df73c
    - Excepcion_la_cobertura_del_riesgo_de_credito_que_tenga_un_plazo_de_vencimiento_original_in_21fdb8
    - Excepcion_la_conformidad_previa_del_bcra_no_sera_requerida_cuando_se_trate_de_un_endeudami_8a5eff
    - Excepcion_la_constancia_de_aceptacion_por_parte_de_esta_ultima_liberara_a_la_entidad_previ_568e20
    - Excepcion_la_constancia_de_aceptacion_por_parte_de_la_nueva_entidad_libera_a_la_entidad_pr_7057fb
    - Excepcion_la_delegacion_no_afecta_las_responsabilidades_que_les_caben_a_los_funcionarios_d_a0b647
    - Excepcion_la_ead_de_un_conjunto_de_neteo_que_solo_comprende_opciones_vendidas_podra_ser_ce_03e1e0
    - Excepcion_la_entrega_de_activos_locales_con_el_objeto_de_cancelar_una_deuda_con_una_agenci_fb3012
    - Excepcion_la_exigencia_maxima_de_capital_para_las_entidades_financieras_originantes_previs_39cc2a
    - Excepcion_la_exportacion_a_consumo_de_bienes_que_conforman_el_equipaje_no_acompanado_expor_8d8720
    - Excepcion_la_limitacion_del_40_no_aplica_cuando_por_un_monto_igual_o_superior_al_excedente_2ce742
    - Excepcion_la_limitacion_del_40_no_aplica_cuando_por_un_monto_igual_o_superior_al_excedente_490b1a
    - Excepcion_la_limitacion_del_40_no_aplica_cuando_por_un_monto_igual_o_superior_al_excedente_7d78b5
    - Excepcion_la_limitacion_del_40_no_aplica_cuando_por_un_monto_igual_o_superior_al_excedente_a725df
    - Excepcion_la_parte_de_la_exposicion_cubierta_estara_sujeta_a_un_minimo_del_20_salvo_lo_dis_a6671e
    - Excepcion_la_perdida_de_beneficios_y_o_baja_de_restantes_productos_o_servicios_no_aplica_a_2b8ba9
    - Excepcion_la_permanencia_de_180_dias_no_aplica_cuando_por_aplicacion_de_otras_pautas_corre_93799c
    - Excepcion_la_precancelacion_de_capital_e_intereses_de_un_titulo_de_deuda_comprendido_en_el_c4404d
    - Excepcion_la_presencia_de_una_opcion_de_exclusion_no_originara_exigencia_de_capital_alguna_3980a9
    - Excepcion_la_presente_reduccion_de_exigencia_regira_para_entidades_del_grupo_2_que_pertene_96f236
    - Excepcion_la_prohibicion_de_acceso_al_mercado_de_cambios_no_aplica_cuando_el_pago_se_concr_80c0c5
    - Excepcion_la_reduccion_en_las_tasas_de_interes_pactadas_no_se_considera_indicador_de_alto__f7d28a
    - Excepcion_las_asistencias_asi_otorgadas_no_seran_consideradas_a_los_fines_a_que_se_refiere_57a4ed
    - Excepcion_las_cajas_de_credito_cooperativas_estan_exceptuadas_de_las_exigencias_de_capital_c8a39e
    - Excepcion_las_destinaciones_suspensivas_de_exportaciones_temporarias_articulos_349_a_373_d_2d7557
    - Excepcion_las_exportaciones_correspondientes_a_los_capitulos_26_excepto_las_posiciones_260_3698d9
    - Excepcion_las_exportaciones_de_valores_billetes_monedas_etc_mediante_el_regimen_ec51_estan_fda742
    - Excepcion_las_garantias_otorgadas_a_favor_del_banco_central_de_la_republica_argentina_esta_c6705d
    - Excepcion_las_inversiones_en_acciones_estructuradas_con_el_objeto_de_replicar_la_realidad__9fc561
    - Excepcion_las_modificaciones_en_el_nombre_y_o_apellido_de_las_personas_fisicas_o_en_otros__4f6ec2
    - Excepcion_las_operaciones_aduaneras_bajo_regimen_de_muestras_articulos_560_al_565_de_la_le_2b56fd
    - Excepcion_las_operaciones_aduaneras_por_ventajas_aduaneras_u_otras_situaciones_previstas_e_ddf087
    - Excepcion_las_operaciones_correspondientes_a_regimen_de_franquicia_diplomatica_articulos_5_8653ef
    - Excepcion_las_operaciones_de_trasbordo_conforme_a_articulos_410_a_416_de_la_ley_22_415_que_12e99c
    - Excepcion_las_operaciones_seran_consideradas_como_sin_garantia__cap_5_2_2_6_75b7b2
    - Excepcion_las_personas_juridicas_inscriptas_en_el_registro_nacional_de_beneficiarios_del_r_553936
    - Excepcion_las_primas_por_opciones_de_compra_y_de_venta_tomadas_estan_excluidas_de_las_fina_1046dd
    - Excepcion_las_siguientes_garantias_otorgadas_por_obligaciones_directas__cla_2_2_2_1_3305df
    - Excepcion_las_transferencias_de_titulos_valores_a_entidades_depositarias_del_exterior_real_6bdff8
    - Excepcion_las_ventas_con_liquidacion_en_moneda_extranjera_en_el_exterior_o_las_transferenc_12e83f
    - Excepcion_las_ventas_con_liquidacion_en_moneda_extranjera_en_el_pais_o_en_el_exterior_de_l_ed92e4
    - Excepcion_las_ventas_de_titulos_valores_con_liquidacion_en_moneda_extranjera_en_el_pais_o__b22c35
    - Excepcion_liberacion_de_la_obligacion_de_secreto_y_reserva_a_que_se_refieren_las_leyes_de__f78030
    - Excepcion_los_cheques_en_los_casos_previstos_en_el_punto_6_2_no_son_susceptibles_de_rechaz_e41f58
    - Excepcion_los_clientes_no_deberan_tener_en_cuenta_en_las_declaraciones_juradas_indicadas_l_100acc
    - Excepcion_los_clientes_que_hayan_adquirido_bonos_bopreal_en_una_suscripcion_primaria_no_de_e948f3
    - Excepcion_los_cobros_por_la_prestacion_de_servicios_a_un_no_residente_por_parte_de_un_vpu__f9e744
    - Excepcion_los_creditos_frente_al_banco_central_de_la_republica_argentina_estan_excluidos_d_233b25
    - Excepcion_los_defectos_originados_en_el_computo_del_50_en_lugar_del_100_de_los_resultados__eec858
    - Excepcion_los_deudores_en_situacion_irregular_no_seran_clasificados_en_la_categoria_irrecu_1df386
    - Excepcion_los_endeudamientos_desembolsados_con_anterioridad_al_01_09_19__ext_3_5_1_1_ea60b7
    - Excepcion_los_permisos_que_revistan_la_condicion_de_incumplido_en_gestion_de_cobro_no_sera_e424b4
    - Excepcion_los_requisitos_previstos_en_los_puntos_4_3_2_1_y_4_3_2_2_no_resultaran_aplicable_2f20e0
    - Excepcion_los_sobregiros_en_cuenta_corriente_bancaria_por_importes_que_excedan_los_margene_612648
    - Excepcion_no_aplica_el_plazo_maximo_de_10_dias_cuando_i_se_trata_de_la_situacion_prevista__7b9d44
    - Excepcion_no_aplica_la_deduccion_a_titulos_valores_e_instrumentos_de_deuda_ya_contemplados_ea7506
    - Excepcion_no_corresponde_la_presentacion_de_esas_declaraciones_juradas_por_cada_una_de_las_3f16c1
    - Excepcion_no_correspondera_el_rechazo_de_solicitudes_de_financiacion_por_el_solo_dato_de_l_4a6f85
    - Excepcion_no_correspondera_la_comunicacion_al_bcra_de_los_rechazos_cuando_se_haya_declarad_f08275
    - Excepcion_no_correspondera_la_comunicacion_al_bcra_de_los_rechazos_motivados_por_el_pago_d_513196
    - Excepcion_no_correspondera_la_comunicacion_al_bcra_de_los_rechazos_motivados_por_falsifica_4e2685
    - Excepcion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi_a5b51b
    - Excepcion_no_deberan_considerarse_aquellos_bienes_que_cuenten_con_las_ventajas_aduaneras_e_8db920
    - Excepcion_no_deberan_considerarse_las_exportaciones_a_consumo_con_despacho_de_importacion__e4682a
    - Excepcion_no_deberan_considerarse_los_bienes_exportados_a_traves_de_operaciones_exceptuada_dbdb4d
    - Excepcion_no_es_necesaria_la_conformidad_previa_del_bcra_para_dar_acceso_al_cliente_vpu_ad_52f5e2
    - Excepcion_no_es_necesario_contar_con_la_conformidad_previa_del_bcra_para_dar_acceso_al_mer_88abf6
    - Excepcion_no_estan_comprendidas_las_exposiciones_originadas_en_operaciones_al_contado_y_qu_3ef8db
    - Excepcion_no_implica_la_inclusion_en_la_causal_a_que_se_refiere_el_punto_9_1_2__ctacte_9_1_f30446
    - Excepcion_no_procedera_la_inclusion_respecto_de_apoderados_para_el_uso_de_la_cuenta_corrie_bd5f64
    - Excepcion_no_resulta_aplicable_la_declaracion_jurada_para_aquellas_operaciones_de_egresos__a80457
    - Excepcion_no_resulta_aplicable_la_declaracion_jurada_para_cancelaciones_de_financiaciones__f50878
    - Excepcion_no_resulta_aplicable_la_declaracion_jurada_para_las_repatriaciones_de_inversione_caf94d
    - Excepcion_no_resulta_aplicable_la_declaracion_jurada_para_operaciones_comprendidas_en_el_p_c7135a
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_cancelaciones_d_5c85cf
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_operaciones_de__1f6142
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_operaciones_de__7c7aef
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_operaciones_de__a30320
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_operaciones_de__a7331c
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_operaciones_de__d73c45
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_operaciones_pro_a64b5f
    - Excepcion_no_resulta_de_aplicacion_el_requisito_de_declaracion_jurada_para_pagos_al_exteri_775a4f
    - Excepcion_no_resultara_aplicable_el_requisito_de_conformidad_previa_del_bcra_cuando_la_ope_5987a2
    - Excepcion_no_resultara_exigible_la_liquidacion_en_el_mercado_de_cambios_de_los_fondos_en_m_20c887
    - Excepcion_no_se_considerara_error_el_rechazo_del_cheque_respecto_del_cual_haya_mediado_aut_845735
    - Excepcion_no_se_consideraran_comprendidas_en_la_definicion_de_nuevas_financiaciones_o_refi_10d1e7
    - Excepcion_no_se_consideraran_las_exportaciones_industriales_comprendidas_en_acuerdos_inter_a49332
    - Excepcion_no_se_consideraran_refinanciaciones_otorgadas_a_productores_cuando_ello_resulte__655289
    - Excepcion_no_se_deberan_computar_los_montos_de_instrumentos_con_vinculacion_crediticia_u_o_4fd27e
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_bancos_u_otr_0cafa1
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_la_casa_matr_a64805
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_otros_bancos_e3fd87
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_sucursales_y_804456
    - Excepcion_no_se_deduciran_los_saldos_que_con_caracter_transitorio_y_circunstancial_se_orig_129ec9
    - Excepcion_no_se_incluyen_las_exposiciones_a_instrumentos_previstas_en_el_punto_2_11__cap_2_c00232
    - Excepcion_no_se_incluyen_los_ingresos_de_importaciones_temporarias_sin_giro_de_divisas__ex_ca6f8b
    - Excepcion_no_se_incluyen_los_registros_aduaneros_por_importaciones_suspensivas_de_deposito_d9a363
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_para_acceso_al_mercado_de_cambios_cua_b538f9
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_para_acceso_al_mercado_de_cambios_par_774d09
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_si_tal_requisito_estuviese_vigente_al_b09e58
    - Excepcion_no_sera_aplicable_en_el_caso_de_financiaciones_otorgadas_a_traves_de_la_suscripc_dbd82f
    - Excepcion_no_sera_de_aplicacion_en_las_operaciones_con_contrapartes_a_las_cuales_el_bcra_l_b593bf
    - Excepcion_operaciones_aduaneras_de_envios_de_asistencia_y_salvamento_estan_exceptuadas_del_a11f9e
    - Excepcion_operaciones_aduaneras_de_los_subregimenes_bara_y_vmi1_en_el_marco_de_la_operator_d956ad
    - Excepcion_operaciones_aduaneras_exceptuadas_del_seguimiento_por_regimen_de_corredores_de_c_902de7
    - Excepcion_operaciones_aduaneras_realizadas_mediante_medios_de_transporte_de_guerra_segurid_a54d05
    - Excepcion_operaciones_de_reembarco_consignadas_mediante_los_subregimenes_re01_re04_re05_re_4b5aa2
    - Excepcion_operaciones_en_regimen_de_exportacion_en_consignacion_estan_exceptuadas_del_segu_de4462
    - Excepcion_organismos_internacionales_e_instituciones_que_cumplan_funciones_de_agencias_ofi_878831
    - Excepcion_para_fondos_percibidos_o_acreditados_en_exterior_se_considera_cumplimentado_ingr_8f26da
    - Excepcion_para_ser_reconocida_no_es_requisito_que_una_ecai_evalue_empresas_en_mas_de_un_pa_d204b1
    - Excepcion_quedan_exceptuados_de_la_obligacion_de_liquidacion_los_cobros_de_exportaciones_d_373b41
    - Excepcion_quedan_excluidas_de_la_operacion_s06_viajes_las_operaciones_asociadas_a_retiros__8821fa
    - Excepcion_quedan_excluidos_de_la_definicion_de_divisas_en_moneda_extranjera_las_monedas_y__2658b5
    - Excepcion_quedaran_exceptuados_de_la_obligacion_de_liquidacion_en_la_medida_que_ingresen_d_9c8508
    - Excepcion_quedaran_exceptuados_de_la_obligacion_de_liquidacion_los_cobros_de_exportaciones_2ad519
    - Excepcion_quedaran_exceptuados_de_la_obligacion_de_liquidacion_los_cobros_de_exportaciones_fd4966
    - Excepcion_regimen_de_donacion_de_organos_y_sangre_humana_resolucion_384_97_de_la_administr_15f424
    - Excepcion_regimen_de_equipaje_articulos_488_al_505_de_la_ley_22_415_operacion_exceptuada_d_6ffb20
    - Excepcion_regimen_de_rancho_articulos_506_al_516_de_la_ley_22_415_en_medios_de_transporte__5ddfb6
    - Excepcion_resultara_aplicable_lo_dispuesto_en_el_punto_14_1_4__ext_7_1_4_3e0d47
    - Excepcion_resultaran_de_aplicacion_las_disposiciones_sobre_extravio_sustraccion_o_adultera_163cc6
    - Excepcion_salvo_decision_de_autoridad_competente_que_obligue_al_cierre_inmediato__ctacte_9_4c156e
    - Excepcion_se_admitira_que_el_legajo_del_cliente_se_encuentre_en_un_lugar_distinto_del_de_r_f80ae3
    - Excepcion_se_considera_cumplimentado_el_requisito_de_ingreso_y_liquidacion_de_divisas_por__bbdcac
    - Excepcion_se_exceptua_la_prohibicion_cuando_se_trate_de_inversiones_en_titulos_publicos_ex_57ee07
    - Excepcion_se_exceptuan_de_las_limitaciones_establecidas_en_este_punto_las_sucesivas_transm_2c9c06
    - Excepcion_se_excluiran_del_monto_de_ventas_totales_aquellas_realizadas_por_la_empresa_en_e_330ac3
    - Excepcion_se_excluyen_las_exposiciones_previstas_en_el_punto_2_11__cap_2_6_1_26d090
    - Excepcion_se_excluyen_los_casos_en_que_las_acciones_se_refieren_a_la_discusion_sobre_otros_97eb4c
    - Excepcion_se_excluyen_los_casos_en_que_las_acciones_se_refieren_a_la_discusion_sobre_otros_d9aec5
    - Excepcion_se_excluyen_tanto_las_estructuras_en_las_que_se_utilizan_los_flujos_de_efectivo__b97094
    - Excepcion_se_observara_lo_establecido_en_el_acapite_i_aplicacion_de_obligacion_presentar_p_6270f0
    - Excepcion_se_permite_la_liquidacion_mediante_deposito_en_cuentas_de_terceros_cuando_se_tra_67a33a
    - Excepcion_se_podran_excluir_las_posiciones_opuestas_por_el_mismo_importe_en_una_misma_espe_599a2d
    - Excepcion_se_podran_excluir_los_derivados_swaps_forwards_futuros_y_forward_rate_agreements_e219fe
    - Excepcion_se_presumira_conformidad_con_el_movimiento_registrado_en_el_banco_cuando_no_hay__ba1a34
    - Excepcion_se_produzca_un_evento_idiosincrasico_y_extraordinario_del_que_resulte_una_reducc_5bd358
    - Excepcion_se_realicen_ajustes_por_razones_objetivas__cap_2_9_2_3_0ede88
    - Excepcion_se_realicen_mejoras_de_caracter_permanente_en_el_inmueble_que_incrementen_su_val_5e1b23
    - Excepcion_se_trata_de_un_endeudamiento_financiero_comprendido_en_este_punto_3_5_con_una_vi_cf65e6
    - Excepcion_se_trate_de_operaciones_propias_de_las_entidades_financieras_locales__ext_3_3_3__9c78fb
    - Excepcion_se_trate_de_operaciones_propias_de_las_entidades_financieras_locales__ext_3_5_6__30cd5f
    - Excepcion_si_existiesen_fondos_destinados_al_pago_de_fletes_de_importaciones_de_bienes_no__0538dd
    - Excepcion_si_no_se_cumple_al_menos_una_de_las_dos_condiciones_senaladas_registro_de_export_5fa54d
    - Excepcion_sin_la_conformidad_previa_requerida_en_el_punto_3_3_3__ext_3_18_1_1_40df42
    - Excepcion_sin_la_conformidad_previa_requerida_en_el_punto_3_3_3_para_pagos_de_intereses_de_53053c
    - Excepcion_sin_necesidad_de_contar_con_la_conformidad_previa_del_bcra_si_tal_requisito_estu_0eaf7c
    - Excepcion_sin_necesidad_de_contar_con_la_conformidad_previa_del_bcra_si_tal_requisito_estu_677da6
    - Excepcion_sin_necesidad_de_contar_con_la_conformidad_previa_del_bcra_si_tal_requisito_estu_aee5c7
    - Excepcion_sin_perjuicio_del_cumplimiento_en_forma_individual_las_entidades_financieras_con_2d4c67
    - Excepcion_sin_tener_en_cuenta_las_limitaciones_cuantitativas_previstas_en_los_puntos_2_1_9_63df18
    - Excepcion_tampoco_se_consideraran_dentro_de_ese_concepto_las_refinanciaciones_otorgadas_a__cf6430
    - Excepcion_unicamente_se_admitira_la_constitucion_de_las_garantias_en_cuentas_abiertas_en_e_c9043d
```

### S21 — WARN

INFORMATIVA — Coherencia de remisiones entre puntos (remite_a o referencia con rol_fuente=referencia_cruzada; scripts/remisiones.py): properties.destino sin el prefijo <to>:: pertenece al CONJUNTO {p.punto for p in provenances} del nodo destino; desglose por properties.alcance (las de alcance to_entero apuntan al TextoOrdenado y se cuentan como incoherentes por construcción del enunciado).

**Resultado:** 14000 remisiones ({'interna': 13021, 'externa': 949, 'to_entero': 30}); 30 incoherentes (por alcance: {'to_entero': 30}).

```
idx 6202: Definicion_codigo_70810000_exigencia_metodologia_hasta_29_02_16__exigencia_por_riesgo_de_me_36c545 -> TextoOrdenado_to_capitales_minimos_actual_pdf destino='cap::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.4.1']...
idx 6628: Definicion_documentos_de_identificacion_en_vigencia__documentos_de_identificacion_en_vigenc_c99955 -> TextoOrdenado_docvig_pdf destino='docvig::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '2.1.1.1']...
idx 6836: Definicion_ficc_indice_cartera_irregular_entidad__cociente_expresado_en_tanto_por_ciento_en_312a32 -> TextoOrdenado_to_clasificacion_deudores_actual_pdf destino='cla::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '10.1', '10.2.1']...
idx 6838: Definicion_ficcs_indice_cartera_irregular_sistema__cociente_expresado_en_tanto_por_ciento_e_e51d51 -> TextoOrdenado_to_clasificacion_deudores_actual_pdf destino='cla::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '10.1', '10.2.1']...
idx 7354: Definicion_normas_proteccion_usuarios_caracter_complementario__las_normas_sobre_proteccion__0ae32b -> TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf destino='pro::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 7472: Definicion_operadores_de_cambio_sujetos_obligados__operadores_de_cambio_por_las_operaciones_372d8b -> TextoOrdenado_to_exterior_cambios_actual_pdf destino='ext::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.5']...
idx 9724: Obligacion_a_los_efectos_de_la_aplicacion_de_las_presentes_disposiciones_debera_cumplirse_c_526351 -> TextoOrdenado_polcre_pdf destino='polcre::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4.1', '1.4.2']...
idx 10880: Obligacion_deberan_observar_las_disposiciones_de_las_normas_sobre_proteccion_de_los_usuario_59c646 -> TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf destino='pro::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 11276: Obligacion_el_cliente_debera_presentar_un_documento_de_identidad_admitido_en_las_normas_sob_ec96d0 -> TextoOrdenado_docvig_pdf destino='docvig::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '2.1.1.1']...
idx 12852: Obligacion_esta_informacion_debera_incluir_clasificacion_promedio_de_los_deudores_conforme__9259c1 -> TextoOrdenado_to_clasificacion_deudores_actual_pdf destino='cla::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '10.1', '10.2.1']...
idx 13112: Obligacion_indicar_nombre_apellido_numero_de_documento_de_identificacion_valido_conforme_a__0f35ab -> TextoOrdenado_docvig_pdf destino='docvig::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '2.1.1.1']...
idx 14848: Obligacion_las_entidades_certificaran_que_los_datos_senalados_en_la_nota_de_presentacion_so_946160 -> TextoOrdenado_docvig_pdf destino='docvig::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '2.1.1.1']...
idx 14849: Obligacion_las_entidades_certificaran_que_los_datos_senalados_en_la_nota_de_presentacion_so_946160 -> TextoOrdenado_pagjub_pdf destino='pagjub::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.5']...
idx 15209: Obligacion_las_entidades_financieras_comprendidas_exclusivamente_sus_casas_en_el_pais_obser_b45f35 -> TextoOrdenado_polcre_pdf destino='polcre::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4.1', '1.4.2']...
idx 15221: Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_consolidada_observa_356738 -> TextoOrdenado_polcre_pdf destino='polcre::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4.1', '1.4.2']...
idx 15482: Obligacion_las_entidades_identificaran_en_la_nota_de_presentacion_los_nombres_apellidos_tip_0ff1c8 -> TextoOrdenado_docvig_pdf destino='docvig::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '2.1.1.1']...
idx 15483: Obligacion_las_entidades_identificaran_en_la_nota_de_presentacion_los_nombres_apellidos_tip_0ff1c8 -> TextoOrdenado_pagjub_pdf destino='pagjub::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.5']...
idx 15538: Obligacion_las_entidades_remitiran_al_bcra_los_archivos_contenidos_en_los_soportes_de_infor_4adace -> TextoOrdenado_docvig_pdf destino='docvig::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '2.1.1.1']...
idx 15539: Obligacion_las_entidades_remitiran_al_bcra_los_archivos_contenidos_en_los_soportes_de_infor_4adace -> TextoOrdenado_pagjub_pdf destino='pagjub::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.5']...
idx 17019: Obligacion_presentacion_de_fotocopias_autenticadas_por_escribano_publico_de_los_documentos__7a5b92 -> TextoOrdenado_docvig_pdf destino='docvig::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '2.1.1.1']...
idx 17025: Obligacion_presentacion_de_tipo_y_numero_del_documento_para_establecer_su_identificacion_se_c283d6 -> TextoOrdenado_docvig_pdf destino='docvig::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '2.1.1.1']...
idx 17339: Obligacion_se_debera_consignar_al_dorso_la_firma_y_aclaracion_o_en_el_correspondiente_regis_88fd95 -> TextoOrdenado_docvig_pdf destino='docvig::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '2.1.1.1']...
idx 17431: Obligacion_se_determinara_teniendo_en_cuenta_lo_dispuesto_en_las_normas_sobre_capitales_min_3ef039 -> TextoOrdenado_to_capitales_minimos_actual_pdf destino='cap::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.4.1']...
idx 20691: Operacion_financiacion_de_importacion_de_bienes_de_capital_3c985a -> TextoOrdenado_to_clasificacion_deudores_actual_pdf destino='cla::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '10.1', '10.2.1']...
idx 22122: Operacion_pago_de_ordenes_de_beneficios_anses_cad97b -> TextoOrdenado_docvig_pdf destino='docvig::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '2.1.1.1']...
idx 22123: Operacion_pago_de_ordenes_de_beneficios_anses_cad97b -> TextoOrdenado_pagjub_pdf destino='pagjub::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.5']...
idx 22894: Operacion_presentacion_de_rendicion_de_cuentas_b26ee5 -> TextoOrdenado_docvig_pdf destino='docvig::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '2.1.1.1']...
idx 22895: Operacion_presentacion_de_rendicion_de_cuentas_b26ee5 -> TextoOrdenado_pagjub_pdf destino='pagjub::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.5']...
idx 23660: Operacion_tenencia_de_oro_amonedado_o_barras_buena_entrega_028209 -> TextoOrdenado_to_exterior_cambios_actual_pdf destino='ext::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.5']...
idx 23663: Operacion_tenencia_de_oro_amonedado_o_en_barras_40484d -> TextoOrdenado_to_exterior_cambios_actual_pdf destino='ext::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.5']...
```

### S22 — PASS

INFORMATIVA — Coherencia de padre_sugerido: el destino de la arista es properties.padre_sugerido del origen y el origen está en cuarentena.

**Resultado:** 24 aristas padre_sugerido; 0 incoherentes (0 con destino distinto, 0 con origen fuera de cuarentena).

Sin violaciones.

### S23 — WARN

INFORMATIVA — aplica_a hacia sujetos en cuarentena: aristas aplica_a cuyo destino es un Sujeto de nivel propuesto (conteo; nunca bloqueante).

**Resultado:** 3929 aristas aplica_a; 37 hacia Sujetos propuestos (24 destinos distintos).

```
idx 9326: Excepcion_representaciones_diplomaticas_y_consulares_y_personal_diplomatico_acreditado_en__d6b618 -> Sujeto_propuesto_personal_diplomatico_acreditado
idx 9327: Excepcion_representaciones_diplomaticas_y_consulares_y_personal_diplomatico_acreditado_en__d6b618 -> Sujeto_propuesto_representaciones_diplomaticas_y_consulares
idx 9407: Excepcion_se_exceptuan_de_la_citada_limitacion_aquellos_endosos_efectuados_en_los_echeq__c_58a6d7 -> Sujeto_propuesto_echeq
idx 9419: Excepcion_se_exceptuan_de_las_limitaciones_establecidas_en_este_punto_cuando_los_cheques_s_00ca25 -> Sujeto_propuesto_caja_de_valores_s_a
idx 9847: Obligacion_acompanar_la_nomina_de_los_cheques_comunes_y_de_pago_diferido_librados_a_la_fech_76daf6 -> Sujeto_propuesto_cuentacorrentista
idx 10514: Obligacion_cuenten_con_politicas_y_practicas_de_uso_tendientes_a_garantizar_que_sus_cliente_020b16 -> Sujeto_propuesto_empresas_del_grupo_economico_de_la_procesadora_de_pagos
idx 11055: Obligacion_devolver_los_no_utilizados__ctacte_9_2_1_1_18cf75 -> Sujeto_propuesto_cuentacorrentista
idx 11191: Obligacion_el_beneficiario_debera_nominar_una_unica_entidad_financiera_local_que_sera_la_re_a42bfd -> Sujeto_propuesto_beneficiario_de_certificaciones_de_incremento_de_exportaciones
idx 11245: Obligacion_el_cliente_debe_dejar_constancia_mediante_declaracion_jurada_de_que_no_ha_adquir_1146c3 -> Sujeto_propuesto_cliente_que_no_es_persona_humana_residente
idx 11247: Obligacion_el_cliente_debe_dejar_constancia_mediante_declaracion_jurada_de_que_no_ha_adquir_aeac32 -> Sujeto_propuesto_cliente_que_no_es_persona_humana_residente
idx 11249: Obligacion_el_cliente_debe_dejar_constancia_mediante_declaracion_jurada_de_que_no_ha_adquir_ea3719 -> Sujeto_propuesto_cliente_que_no_es_persona_humana_residente
idx 11251: Obligacion_el_cliente_debe_dejar_constancia_mediante_declaracion_jurada_de_que_no_ha_concer_8acfee -> Sujeto_propuesto_cliente_que_no_es_persona_humana_residente
idx 11253: Obligacion_el_cliente_debe_dejar_constancia_mediante_declaracion_jurada_de_que_no_ha_entreg_fef327 -> Sujeto_propuesto_cliente_que_no_es_persona_humana_residente
idx 11255: Obligacion_el_cliente_debe_dejar_constancia_mediante_declaracion_jurada_de_que_no_ha_realiz_5b728f -> Sujeto_propuesto_cliente_que_no_es_persona_humana_residente
idx 11257: Obligacion_el_cliente_debe_dejar_constancia_mediante_declaracion_jurada_de_que_no_ha_realiz_dd4532 -> Sujeto_propuesto_cliente_que_no_es_persona_humana_residente
idx 11672: Obligacion_el_originante_fiduciario_debera_divulgar_toda_la_informacion_necesaria_respecto__ad075a -> Sujeto_propuesto_originante_fiduciario
idx 11738: Obligacion_el_presentante_debera_acreditar_su_categoria_de_residencia_su_vigencia_y_el_tiem_08576c -> Sujeto_propuesto_presentante
idx 12033: Obligacion_en_base_a_la_informacion_provista_el_inversor_debera_realizar_sus_propias_evalua_d22b39 -> Sujeto_propuesto_inversor
idx 12038: Obligacion_en_base_a_la_informacion_provista_el_inversor_debera_realizar_sus_propias_evalua_d74458 -> Sujeto_propuesto_inversor
idx 12763: Obligacion_en_todos_los_casos_debera_acreditarse_la_categoria_de_residencia_su_vigencia_y_e_004682 -> Sujeto_propuesto_extranjeros_con_residencia_permanente_o_temporaria
idx 13134: Obligacion_informar_los_anulados__ctacte_9_2_1_1_bfb1f9 -> Sujeto_propuesto_cuentacorrentista
idx 14825: Obligacion_las_empresas_administradoras_de_las_redes_de_cajeros_automaticos_y_las_entidades_fa3f0b -> Sujeto_propuesto_empresas_administradoras_de_las_redes_de_cajeros_automaticos
idx 15701: Obligacion_las_personas_que_hayan_sido_incorporadas_a_la_central_de_cheques_rechazados_y_o__e83784 -> Sujeto_propuesto_personas_que_hayan_sido_incorporadas_a_las_centrales
idx 15794: Obligacion_las_restantes_operaciones_de_derivados_financieros_que_quieran_ser_cursadas_con__7487f9 -> Sujeto_propuesto_residentes_que_no_sean_entidades_autorizadas_a_operar_en_cambios
idx 15834: Obligacion_los_administradores_de_las_carteras_crediticias_deberan_suministrar_la_informaci_cd43e4 -> Sujeto_propuesto_administradores_de_las_carteras_crediticias
idx 15911: Obligacion_los_beneficiarios_del_regimen_de_acceso_a_divisas_para_la_produccion_incremental_a07097 -> Sujeto_propuesto_beneficiarios_del_regimen_de_acceso_a_divisas_para_la_produccion_incremental_de_
idx 16289: Obligacion_los_integrantes_de_la_alta_gerencia_deberan_ejercer_el_control_apropiado_del_per_7ba7f3 -> Sujeto_propuesto_integrantes_de_la_alta_gerencia
idx 16291: Obligacion_los_integrantes_de_la_alta_gerencia_deberan_gestionar_el_negocio_bajo_su_supervi_ea7885 -> Sujeto_propuesto_integrantes_de_la_alta_gerencia
idx 16293: Obligacion_los_integrantes_de_la_alta_gerencia_deberan_tener_la_idoneidad_y_experiencia_nec_15a3bd -> Sujeto_propuesto_integrantes_de_la_alta_gerencia
idx 16299: Obligacion_los_inversores_y_tenedores_de_las_posiciones_de_titulizacion_deberan_tener_en_cu_845230 -> Sujeto_propuesto_inversores_y_tenedores
idx 16796: Obligacion_para_las_entidades_del_grupo_a_aplicar_lo_establecido_en_el_punto_5_4_2_3_i_de_l_627a44 -> Sujeto_propuesto_entidades_del_grupo_a
idx 16804: Obligacion_para_las_posiciones_retenidas_en_las_que_el_originante_haya_transferido_el_riesg_9a7160 -> Sujeto_propuesto_originante
idx 17939: Obligacion_todas_las_empresas_del_grupo_economico_de_la_procesadora_de_pagos_incluyendo_la__5712be -> Sujeto_propuesto_empresas_del_grupo_economico_de_la_procesadora_de_pagos
idx 20490: Operacion_exclusion_de_inhabilitados_de_base_de_datos_cc5e08 -> Sujeto_propuesto_personas_inhabilitadas_por_decision_judicial_o_por_motivos_legales
idx 22857: Operacion_presentacion_de_dni_para_identificacion_16dca8 -> Sujeto_propuesto_extranjeros_con_residencia_permanente_o_temporaria
idx 24581: Potestad_aplicacion_a_centrales_de_deposito_de_valores__ello_tambien_resulta_aplicable_a__a9a3e7 -> Sujeto_propuesto_centrales_locales_de_deposito_colectivo_de_valores
idx 27814: Restriccion_las_restantes_entidades_salvo_bancos_y_cajas_de_credito_cooperativas_deberan_man_24fa49 -> Sujeto_propuesto_restantes_entidades
```

### S27 — WARN

INFORMATIVA — Arista de sujeto con mención y método (informativa en r2a, bloqueante desde r2b). Fase: r2a.

**Resultado:** 4086 aristas de sujeto fuera del esqueleto; 4026 sin mención, verificación o método ({'sin_mencion': 4026}).

```
idx 7923: aplica_a Excepcion_acceso_al_mercado_de_cambios_incluso_cuando_no_se_cumplan_los_requisitos_estable_a39a35 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 7929: aplica_a Excepcion_anticipos_por_pago_de_jubilaciones_y_pensiones_estan_excluidos_de_las_financiaci_ca6c68 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 7931: aplica_a Excepcion_anticipos_y_prestamos_al_fondo_de_garantia_de_los_depositos_estan_excluidos_de_l_849b30 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 7940: aplica_a Excepcion_calculo_del_riesgo_de_tasa_de_interes_en_la_cartera_de_inversion_tendra_frecuenc_0bf3e6 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 7956: aplica_a Excepcion_contenga_endosos_tachados_o_que_carezcan_de_los_requisitos_formales_establecidos_1230a8 -> Sujeto_banco: sin mención
idx 7958: aplica_a Excepcion_contractualmente_no_estuviera_previsto_que_una_facilidad_de_liquidez_cubra_activ_b43186 -> Sujeto_rol_alcance_capmin: sin mención
idx 7992: aplica_a Excepcion_cuando_en_estos_casos_sea_factible_el_computo_de_la_crc_su_reconocimiento_sera_p_2c0908 -> Sujeto_rol_alcance_capmin: sin mención
idx 7994: aplica_a Excepcion_cuando_existan_obstaculos_para_la_rapida_repatriacion_de_beneficios_desde_una_su_d8a545 -> Sujeto_sujeto_del_perimetro_consolidado: sin mención
idx 7996: aplica_a Excepcion_cuando_la_cantidad_escrita_en_letras_difiriese_de_la_expresada_en_numeros_se_est_9f697c -> Sujeto_banco: sin mención
idx 8015: aplica_a Excepcion_datos_complementarios_vinculados_al_calculo_de_la_exigencia_por_riesgo_de_mercad_917a7d -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 8030: aplica_a Excepcion_el_acceso_al_mercado_de_cambios_antes_de_lo_indicado_se_permite_en_el_caso_de_pr_2f0313 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8043: aplica_a Excepcion_el_cliente_es_un_vehiculo_de_proyecto_unico_vpu_adherido_al_regimen_de_incentivo_d68027 -> Sujeto_vpu_rigi: sin mención
idx 8094: aplica_a Excepcion_el_limite_maximo_establecido_precedentemente_se_reducira_a_11_cuando_la_entidad__2ad49c -> Sujeto_rol_alcance_capmin: sin mención
idx 8101: aplica_a Excepcion_el_pago_es_concretado_mediante_canje_y_o_arbitraje_con_fondos_depositados_en_cue_7becd8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8167: aplica_a Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_resultara_aplicable_cuando_se_cum_6b45a6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8179: aplica_a Excepcion_el_requisito_de_ingreso_y_liquidacion_de_divisas_se_considera_cumplimentado_para_27ea86 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8190: aplica_a Excepcion_en_caso_de_afectacion_de_la_solvencia_y_o_liquidez_de_la_entidad_se_tenga_por_no_4be440 -> Sujeto_entidad_financiera: sin mención
idx 8212: aplica_a Excepcion_en_cuanto_a_las_exportaciones_desde_el_territorio_nacional_continental_al_area_f_9eb0fd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8223: aplica_a Excepcion_en_el_caso_de_que_la_adquisicion_de_titulos_valores_se_haya_concretado_con_liqui_110a42 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8226: aplica_a Excepcion_en_el_caso_de_que_las_entidades_financieras_no_ejercieran_esa_opcion_corresponde_446a12 -> Sujeto_rol_alcance_capmin: sin mención
idx 8229: aplica_a Excepcion_en_estos_casos_los_usuarios_de_servicios_financieros_pueden_requerir_y_recibir_i_f50c7d -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 8231: aplica_a Excepcion_en_estrategias_donde_la_entidad_asuma_posicion_contraria_en_exactamente_el_mismo_55b403 -> Sujeto_rol_alcance_capmin: sin mención
idx 8235: aplica_a Excepcion_en_las_situaciones_que_se_detallan_a_continuacion_se_admitira_tambien_la_utiliza_6a7544 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8240: aplica_a Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c_ef574e -> Sujeto_rol_alcance_capmin: sin mención
idx 8242: aplica_a Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c_f09bfc -> Sujeto_rol_alcance_capmin: sin mención
idx 8251: aplica_a Excepcion_este_requerimiento_no_sera_de_aplicacion_para_el_caso_de_exposiciones_a_gobierno_89943a -> Sujeto_rol_alcance_capmin: sin mención
idx 8348: aplica_a Excepcion_este_requisito_no_resultara_aplicable_para_el_acceso_al_mercado_para_las_cancela_4a0109 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8379: aplica_a Excepcion_este_requisito_no_sera_de_aplicacion_para_i_el_sector_publico_ii_todas_las_organ_3552bf -> Sujeto_fideicomiso: sin mención
idx 8381: aplica_a Excepcion_este_requisito_no_sera_de_aplicacion_para_i_el_sector_publico_ii_todas_las_organ_3552bf -> Sujeto_sector_publico_no_financiero: sin mención
idx 8388: aplica_a Excepcion_excepcion_a_la_prohibicion_de_acceso_al_mercado_de_cambios_para_el_pago_de_pagar_525855 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8391: aplica_a Excepcion_excepcion_a_la_prohibicion_de_acceso_al_mercado_de_cambios_para_pagos_de_obligac_946421 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8393: aplica_a Excepcion_excepcion_aplicable_cuando_se_trate_de_un_endeudamiento_financiero_comprendido_e_2891e6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8408: aplica_a Excepcion_excepcionalmente_mediando_autorizacion_previa_de_la_sefyc_podran_admitirse_aport_4be23e -> Sujeto_rol_alcance_capmin: sin mención
idx 8411: aplica_a Excepcion_excepto_cuando_adicionalmente_a_los_restantes_requisitos_aplicables_la_entidad_v_294c0e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8414: aplica_a Excepcion_excepto_cuando_la_entidad_constate_que_el_pago_encuadra_en_alguna_de_las_situaci_511717 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8491: aplica_a Excepcion_exencion_de_ingreso_de_divisas_para_exportaciones_del_area_aduanera_especial_al__a789ea -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8493: aplica_a Excepcion_exportacion_a_consumo_de_automotores_de_fabricacion_nacional_sus_partes_y_piezas_4906fb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8495: aplica_a Excepcion_exportaciones_a_zonas_francas_nacionales_estan_exceptuadas_del_seguimiento_de_pe_7d3913 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8497: aplica_a Excepcion_exportaciones_de_bienes_enviados_al_exterior_con_fines_promocionales_estan_excep_b1eaad -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8499: aplica_a Excepcion_exportaciones_desde_el_territorio_nacional_continental_al_area_aduanera_especial_da482e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8507: aplica_a Excepcion_financiaciones_y_avales_fianzas_y_otras_responsabilidades_otorgados_por_subsidia_7d2233 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 8509: aplica_a Excepcion_financiaciones_y_avales_fianzas_y_otras_responsabilidades_otorgados_por_sucursal_91562a -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 8514: aplica_a Excepcion_informacion_sobre_ratio_de_apalancamiento_seccion_10_tendra_frecuencia_trimestra_24c8fc -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 8519: aplica_a Excepcion_la_cancelacion_de_pagos_en_concepto_de_dividendos_o_intereses_no_debera_constitu_5df73c -> Sujeto_rol_alcance_capmin: sin mención
idx 8529: aplica_a Excepcion_la_delegacion_no_afecta_las_responsabilidades_que_les_caben_a_los_funcionarios_d_a0b647 -> Sujeto_rol_alcance_pagjub: sin mención
idx 8539: aplica_a Excepcion_la_designacion_de_personal_con_funciones_de_representacion_no_implica_una_delega_064ef9 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 8545: aplica_a Excepcion_la_entrega_de_activos_locales_con_el_objeto_de_cancelar_una_deuda_con_una_agenci_fb3012 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8602: aplica_a Excepcion_la_precancelacion_de_capital_e_intereses_de_un_titulo_de_deuda_comprendido_en_el_c4404d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8616: aplica_a Excepcion_la_presente_reduccion_de_exigencia_regira_para_entidades_del_grupo_2_que_pertene_96f236 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 8618: aplica_a Excepcion_la_prohibicion_de_acceso_al_mercado_de_cambios_no_aplica_cuando_el_pago_se_concr_80c0c5 -> Sujeto_cliente: sin mención
idx 8623: aplica_a Excepcion_la_toma_de_conocimiento_sin_formulacion_de_observaciones_por_parte_del_directori_8a3a23 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 8626: aplica_a Excepcion_la_venta_de_los_titulos_en_el_origen_de_la_operacion_no_debera_tenerse_en_cuenta_214eac -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8678: aplica_a Excepcion_las_cajas_de_credito_cooperativas_estan_exceptuadas_de_las_exigencias_de_capital_c8a39e -> Sujeto_caja_de_credito_cooperativa: sin mención
idx 8680: aplica_a Excepcion_las_destinaciones_suspensivas_de_exportaciones_temporarias_articulos_349_a_373_d_2d7557 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8708: aplica_a Excepcion_las_exportaciones_de_bienes_efectuadas_por_un_vpu_adherido_al_rigi_por_un_proyec_8775b8 -> Sujeto_vpu_rigi: sin mención
idx 8711: aplica_a Excepcion_las_exportaciones_de_efectos_personales_que_hacen_a_la_profesion_u_oficio_de_per_6e41c2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8714: aplica_a Excepcion_las_exportaciones_de_valores_billetes_monedas_etc_mediante_el_regimen_ec51_estan_fda742 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8755: aplica_a Excepcion_las_operaciones_de_trasbordo_conforme_a_articulos_410_a_416_de_la_ley_22_415_que_12e99c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8758: aplica_a Excepcion_las_personas_juridicas_inscriptas_en_el_registro_nacional_de_beneficiarios_del_r_553936 -> Sujeto_beneficiario_economia_conocimiento: sin mención
idx 8760: aplica_a Excepcion_las_personas_juridicas_inscriptas_en_el_registro_nacional_de_beneficiarios_del_r_df19a6 -> Sujeto_beneficiario_economia_conocimiento: sin mención
idx 8767: aplica_a Excepcion_las_transferencias_de_titulos_valores_a_entidades_depositarias_del_exterior_real_6bdff8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8816: aplica_a Excepcion_las_ventas_de_titulos_valores_con_liquidacion_en_moneda_extranjera_en_el_pais_o__b22c35 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8818: aplica_a Excepcion_liberacion_de_la_obligacion_de_secreto_y_reserva_a_que_se_refieren_las_leyes_de__f78030 -> Sujeto_entidad_financiera: sin mención
idx 8822: aplica_a Excepcion_lo_previsto_en_este_punto_requisitos_minimos_de_contratos_incluyendo_clausula_de_e65c6d -> Sujeto_entidad_financiera: sin mención
idx 8830: aplica_a Excepcion_los_cheques_en_los_casos_previstos_en_el_punto_6_2_no_son_susceptibles_de_rechaz_e41f58 -> Sujeto_banco: sin mención
idx 8832: aplica_a Excepcion_los_clientes_no_deberan_tener_en_cuenta_en_las_declaraciones_juradas_indicadas_l_100acc -> Sujeto_cliente: sin mención
idx 8874: aplica_a Excepcion_los_clientes_que_hayan_adquirido_bonos_bopreal_en_una_suscripcion_primaria_no_de_e948f3 -> Sujeto_cliente: sin mención
idx 8937: aplica_a Excepcion_los_cobros_anticipados_de_exportaciones_de_bienes_las_prefinanciaciones_y_las_po_fc4ab1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 8940: aplica_a Excepcion_los_cobros_por_la_prestacion_de_servicios_a_un_no_residente_por_parte_de_un_vpu__f9e744 -> Sujeto_vpu_rigi: sin mención
idx 8942: aplica_a Excepcion_los_creditos_frente_al_banco_central_de_la_republica_argentina_estan_excluidos_d_233b25 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 8944: aplica_a Excepcion_los_defectos_originados_en_el_computo_del_50_en_lugar_del_100_de_los_resultados__eec858 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 8952: aplica_a Excepcion_los_limites_maximos_17_grupo_b_14_grupo_c_se_reduciran_a_11_y_a_8_respectivament_245ed4 -> Sujeto_rol_alcance_capmin: sin mención
idx 8976: aplica_a Excepcion_no_aplica_el_procedimiento_de_comunicacion_de_rechazo_en_la_situacion_prevista_e_7c089a -> Sujeto_banco: sin mención
idx 8999: aplica_a Excepcion_no_aplica_la_deduccion_a_titulos_valores_e_instrumentos_de_deuda_ya_contemplados_ea7506 -> Sujeto_rol_alcance_capmin: sin mención
idx 9015: aplica_a Excepcion_no_aplicara_el_cierre_o_revocacion_de_autorizaciones_cuando_se_trate_de_cuentas__27b213 -> Sujeto_banco: sin mención
idx 9025: aplica_a Excepcion_no_correspondera_el_rechazo_de_solicitudes_de_financiacion_por_el_solo_dato_de_l_4a6f85 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 9027: aplica_a Excepcion_no_correspondera_la_comunicacion_al_bcra_de_los_rechazos_cuando_se_haya_declarad_f08275 -> Sujeto_banco: sin mención
idx 9037: aplica_a Excepcion_no_correspondera_la_comunicacion_al_bcra_de_los_rechazos_motivados_por_el_pago_d_513196 -> Sujeto_banco: sin mención
idx 9040: aplica_a Excepcion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi_a5b51b -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9047: aplica_a Excepcion_no_es_necesaria_la_conformidad_previa_del_bcra_para_dar_acceso_al_cliente_vpu_ad_52f5e2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9088: aplica_a Excepcion_no_estan_obligadas_al_seguimiento_aquellas_entidades_financieras_y_casas_de_camb_21fd28 -> Sujeto_casa_de_cambio: sin mención
idx 9089: aplica_a Excepcion_no_estan_obligadas_al_seguimiento_aquellas_entidades_financieras_y_casas_de_camb_21fd28 -> Sujeto_entidad_financiera: sin mención
idx 9097: aplica_a Excepcion_no_resulta_aplicable_el_requisito_de_conformidad_previa_cuando_se_trate_de_un_pa_a3bce7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9100: aplica_a Excepcion_no_resulta_aplicable_la_declaracion_jurada_para_aquellas_operaciones_de_egresos__a80457 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9104: aplica_a Excepcion_no_resulta_aplicable_la_declaracion_jurada_para_cancelaciones_de_financiaciones__f50878 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9106: aplica_a Excepcion_no_resulta_aplicable_la_declaracion_jurada_para_las_repatriaciones_de_inversione_caf94d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9112: aplica_a Excepcion_no_resulta_aplicable_la_declaracion_jurada_para_operaciones_comprendidas_en_el_p_c7135a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9202: aplica_a Excepcion_no_resultara_exigible_la_liquidacion_en_el_mercado_de_cambios_de_los_fondos_en_m_20c887 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9235: aplica_a Excepcion_no_se_requerira_conformidad_previa_del_bcra_cuando_el_pago_es_concretado_por_una_fa612e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9238: aplica_a Excepcion_no_se_requiere_conformidad_previa_del_bcra_cuando_la_entidad_cuenta_al_momento_d_2a9e4a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9242: aplica_a Excepcion_no_se_requiere_conformidad_previa_del_bcra_para_acceso_al_mercado_de_cambios_par_774d09 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9258: aplica_a Excepcion_no_sera_obligatoria_la_apertura_del_legajo_en_los_casos_de_deudores_por_servicio_90a2a5 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9261: aplica_a Excepcion_no_son_elegibles_aquellas_entidades_financieras_y_casas_de_cambio_que_hayan_noti_8583d5 -> Sujeto_casa_de_cambio: sin mención
idx 9262: aplica_a Excepcion_no_son_elegibles_aquellas_entidades_financieras_y_casas_de_cambio_que_hayan_noti_8583d5 -> Sujeto_entidad_financiera: sin mención
idx 9266: aplica_a Excepcion_operaciones_aduaneras_de_los_subregimenes_bara_y_vmi1_en_el_marco_de_la_operator_d956ad -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9270: aplica_a Excepcion_operaciones_de_reembarco_consignadas_mediante_los_subregimenes_re01_re04_re05_re_4b5aa2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9272: aplica_a Excepcion_operaciones_en_regimen_de_exportacion_en_consignacion_estan_exceptuadas_del_segu_de4462 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9274: aplica_a Excepcion_organismos_internacionales_e_instituciones_que_cumplan_funciones_de_agencias_ofi_878831 -> Sujeto_agencia_oficial_de_credito: sin mención
idx 9275: aplica_a Excepcion_organismos_internacionales_e_instituciones_que_cumplan_funciones_de_agencias_ofi_878831 -> Sujeto_organismo_internacional: sin mención
idx 9280: aplica_a Excepcion_para_ser_reconocida_no_es_requisito_que_una_ecai_evalue_empresas_en_mas_de_un_pa_d204b1 -> Sujeto_ecai: sin mención
idx 9293: aplica_a Excepcion_por_la_diferencia_entre_el_valor_efectivo_y_el_valor_nominal_en_emisiones_de_tit_a94034 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9298: aplica_a Excepcion_queda_permitido_el_acceso_al_mercado_de_cambios_para_la_cancelacion_en_el_pais_a_b9ab6f -> Sujeto_entidad_financiera: sin mención
idx 9301: aplica_a Excepcion_quedan_exceptuados_de_la_obligacion_de_liquidacion_los_cobros_de_exportaciones_d_373b41 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9307: aplica_a Excepcion_quedaran_exceptuados_de_la_obligacion_de_liquidacion_en_la_medida_que_ingresen_d_4e9c78 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9310: aplica_a Excepcion_quedaran_exceptuados_de_la_obligacion_de_liquidacion_en_la_medida_que_ingresen_d_9c8508 -> Sujeto_beneficiario_economia_conocimiento: sin mención
idx 9312: aplica_a Excepcion_quedaran_exceptuados_de_la_obligacion_de_liquidacion_los_cobros_de_exportaciones_2ad519 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9314: aplica_a Excepcion_quedaran_exceptuados_de_la_obligacion_de_liquidacion_los_cobros_de_exportaciones_65a1bb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9317: aplica_a Excepcion_quedaran_exceptuados_de_la_obligacion_de_liquidacion_los_cobros_de_exportaciones_fd4966 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9322: aplica_a Excepcion_regimen_de_equipaje_articulos_488_al_505_de_la_ley_22_415_operacion_exceptuada_d_6ffb20 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9324: aplica_a Excepcion_regimen_de_rancho_articulos_506_al_516_de_la_ley_22_415_en_medios_de_transporte__5ddfb6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9370: aplica_a Excepcion_se_admitira_que_el_legajo_del_cliente_se_encuentre_en_un_lugar_distinto_del_de_r_f80ae3 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9374: aplica_a Excepcion_se_considera_cumplimentado_el_requisito_de_ingreso_y_liquidacion_de_divisas_por__bbdcac -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9387: aplica_a Excepcion_se_exceptua_del_acceso_prohibido_al_mercado_de_cambios_para_el_pago_de_deudas_y__0bfaef -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9410: aplica_a Excepcion_se_exceptuan_de_la_citada_limitacion_los_endosos_a_favor_del_bcra__ctacte_5_1_1_31a0b4 -> Sujeto_bcra: sin mención
idx 9415: aplica_a Excepcion_se_exceptuan_de_las_limitaciones_establecidas_en_este_punto_a_los_endosos_que_la_470135 -> Sujeto_entidad_financiera: sin mención
idx 9416: aplica_a Excepcion_se_exceptuan_de_las_limitaciones_establecidas_en_este_punto_a_los_endosos_que_la_470135 -> Sujeto_fiduciario_de_fideicomiso_financiero: sin mención
idx 9422: aplica_a Excepcion_se_exceptuan_de_las_limitaciones_establecidas_en_este_punto_las_sucesivas_transm_2c9c06 -> Sujeto_sujeto: sin mención
idx 9445: aplica_a Excepcion_se_podran_excluir_las_posiciones_opuestas_por_el_mismo_importe_en_una_misma_espe_599a2d -> Sujeto_rol_alcance_capmin: sin mención
idx 9447: aplica_a Excepcion_se_podran_excluir_los_derivados_swaps_forwards_futuros_y_forward_rate_agreements_e219fe -> Sujeto_rol_alcance_capmin: sin mención
idx 9468: aplica_a Excepcion_se_presumira_conformidad_con_el_movimiento_registrado_en_el_banco_cuando_no_hay__ba1a34 -> Sujeto_banco: sin mención
idx 9511: aplica_a Excepcion_se_trate_de_un_pago_de_intereses_compensatorios_que_se_devenguen_a_partir_del_01_920de0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9551: aplica_a Excepcion_sin_necesidad_de_contar_con_la_conformidad_previa_del_bcra_si_tal_requisito_estu_aee5c7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9565: aplica_a Excepcion_sin_perjuicio_del_cumplimiento_en_forma_individual_las_entidades_financieras_con_2d4c67 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9569: aplica_a Excepcion_sin_tener_en_cuenta_las_limitaciones_cuantitativas_previstas_en_los_puntos_2_1_9_63df18 -> Sujeto_entidad_financiera: sin mención
idx 9622: aplica_a Obligacion_365_trescientos_sesenta_y_cinco_dias_corridos_para_las_operaciones_que_se_concre_15dc23 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9625: aplica_a Obligacion_a_efectos_de_cumplir_con_el_principio_de_transferencia_real_debera_realizarse_un_615bae -> Sujeto_rol_alcance_capmin: sin mención
idx 9628: aplica_a Obligacion_a_efectos_de_informar_los_resultados_de_cada_uno_de_los_periodos_de_12_meses_cor_f07dc1 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 9630: aplica_a Obligacion_a_este_efecto_se_considerara_la_ultima_calificacion_informada_para_el_calculo_de_300df1 -> Sujeto_rol_alcance_capmin: sin mención
idx 9632: aplica_a Obligacion_a_este_fin_el_computo_de_los_plazos_no_se_interrumpira_por_el_otorgamiento_de_re_ee32e1 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9661: aplica_a Obligacion_a_fin_de_determinar_el_importe_de_la_cancelacion_se_admitira_computar_el_50_de_l_2958b9 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9664: aplica_a Obligacion_a_fin_de_determinar_el_importe_de_la_cancelacion_se_admitira_computar_el_50_de_l_54ab95 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9666: aplica_a Obligacion_a_fin_de_determinar_el_importe_de_la_cancelacion_se_admitira_computar_el_50_de_l_aab46b -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9668: aplica_a Obligacion_a_fin_de_determinar_el_importe_de_las_financiaciones_comprendidas_en_la_exposici_4732c5 -> Sujeto_rol_alcance_capmin: sin mención
idx 9670: aplica_a Obligacion_a_fin_de_facilitar_las_verificaciones_que_realice_el_bcra__ctacte_9_4_fc5062 -> Sujeto_banco: sin mención
idx 9672: aplica_a Obligacion_a_la_entidad_en_que_se_deposita_el_cheque_cuando_sea_distinta_de_la_girada_le_co_3e8493 -> Sujeto_entidad_depositaria: sin mención
idx 9678: aplica_a Obligacion_a_la_parte_no_cubierta_se_le_aplicara_el_ponderador_de_riesgo_que_le_corresponda_c95e87 -> Sujeto_rol_alcance_capmin: sin mención
idx 9682: aplica_a Obligacion_a_los_conceptos_citados_en_los_puntos_precedentes_se_les_restaran_de_corresponde_5c1d6c -> Sujeto_rol_alcance_capmin: sin mención
idx 9685: aplica_a Obligacion_a_los_conceptos_citados_en_los_puntos_precedentes_se_les_restaran_los_conceptos__38377e -> Sujeto_rol_alcance_capmin: sin mención
idx 9687: aplica_a Obligacion_a_los_efectos_de_considerar_en_las_exposiciones_minoristas_normativas_a_los_cred_093be4 -> Sujeto_rol_alcance_capmin: sin mención
idx 9689: aplica_a Obligacion_a_los_efectos_de_determinar_el_ponderador_de_riesgo_a_aplicar_a_las_exposiciones_79c4c4 -> Sujeto_rol_alcance_capmin: sin mención
idx 9720: aplica_a Obligacion_a_los_efectos_de_determinar_los_montos_pendientes_en_los_casos_de_facturaciones__b41642 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9722: aplica_a Obligacion_a_los_efectos_de_la_aplicacion_de_las_presentes_disposiciones_debera_cumplirse_c_526351 -> Sujeto_rol_alcance_capmin: sin mención
idx 9725: aplica_a Obligacion_a_los_efectos_de_la_emision_de_la_certificacion_se_computara_el_monto_del_docume_cabd72 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9733: aplica_a Obligacion_a_los_efectos_del_registro_de_estas_operaciones_se_deberan_confeccionar_dos_bole_7ee0ad -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9736: aplica_a Obligacion_a_los_efectos_del_registro_de_estas_operaciones_se_deberan_confeccionar_dos_bole_a5c0e6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9738: aplica_a Obligacion_a_los_efectos_del_registro_de_estas_operaciones_se_deberan_confeccionar_dos_bole_be095f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9741: aplica_a Obligacion_a_los_efectos_del_registro_de_estas_operaciones_se_deberan_confeccionar_dos_bole_d8b0dd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9744: aplica_a Obligacion_a_los_efectos_del_registro_de_las_operaciones_admitidas_en_los_puntos_3_11_1_3_1_59963c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9777: aplica_a Obligacion_a_los_efectos_previstos_en_los_dos_ultimos_parrafos_anteriores_y_aun_cuando_se_h_129dda -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9779: aplica_a Obligacion_a_los_efectos_que_los_cobros_de_exportaciones_aplicados_puedan_ser_imputados_al__01883a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9781: aplica_a Obligacion_a_los_fines_de_calcular_el_limite_definido_en_el_parrafo_precedente_se_aplicara__5abc26 -> Sujeto_rol_alcance_capmin: sin mención
idx 9784: aplica_a Obligacion_a_los_fines_de_establecer_los_dias_de_atraso_en_el_caso_de_las_financiaciones_in_c6f24f -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9786: aplica_a Obligacion_a_los_fines_de_la_clasificacion_debera_tenerse_en_cuenta_el_flujo_de_fondos_proy_a72bd6 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9788: aplica_a Obligacion_a_los_fines_de_la_clasificacion_debera_tenerse_en_cuenta_unicamente_la_mora_en_e_9a9337 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9790: aplica_a Obligacion_a_los_fines_de_la_comparacion_el_sujeto_obligado_debera_informarle_al_usuario_la_b5a35f -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 9793: aplica_a Obligacion_a_los_fines_de_la_imputacion_de_las_financiaciones_sera_de_aplicacion_lo_previst_0f9bc1 -> Sujeto_entidad_financiera: sin mención
idx 9795: aplica_a Obligacion_a_los_fines_de_la_presentacion_al_cobro_del_cheque_librado_en_formato_papel_dire_f78799 -> Sujeto_banco: sin mención
idx 9798: aplica_a Obligacion_a_los_fines_del_redondeo_de_las_magnitudes_se_incrementaran_los_valores_en_una_u_525475 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 9801: aplica_a Obligacion_a_nivel_consolidado_el_bi_se_calcula_a_base_de_los_valores_consolidados_de_los_i_58a7c6 -> Sujeto_rol_alcance_capmin: sin mención
idx 9803: aplica_a Obligacion_a_nivel_individual_deben_utilizarse_las_cifras_del_bi_de_cada_subsidiaria__cap_7_2a98de -> Sujeto_rol_alcance_capmin: sin mención
idx 9805: aplica_a Obligacion_a_partir_de_la_fecha_limite_establecida_en_el_punto_2_5_4_se_procedera_conforme__d17f97 -> Sujeto_rol_alcance_pagjub: sin mención
idx 9813: aplica_a Obligacion_a_partir_del_comienzo_de_cada_uno_de_los_ultimos_cinco_anos_de_vida_de_cada_emis_023f40 -> Sujeto_rol_alcance_capmin: sin mención
idx 9816: aplica_a Obligacion_a_partir_del_segundo_y_hasta_el_trigesimo_sexto_mes_la_exigencia_mensual_sera_eq_020025 -> Sujeto_rol_alcance_capmin: sin mención
idx 9819: aplica_a Obligacion_a_requerimiento_del_titular_la_entidad_debe_proporcionar_chequeras_con_formulas__e0da87 -> Sujeto_banco: sin mención
idx 9821: aplica_a Obligacion_a_solicitud_de_cada_cliente_dentro_de_los_10_dias_corridos_del_pedido_la_entidad_783e8b -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9823: aplica_a Obligacion_a_tales_efectos_debera_verificar_previamente_que_se_cumplen_la_totalidad_de_requ_6dd5ee -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9844: aplica_a Obligacion_acceso_al_registro_centralizado_de_consultas_y_reclamos_asi_como_la_documentacio_f35c42 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 9849: aplica_a Obligacion_acreditar_en_el_dia_los_importes_que_se_le_entreguen_para_el_credito_de_la_cuent_111865 -> Sujeto_banco: sin mención
idx 9853: aplica_a Obligacion_acreditar_en_la_cuenta_corriente_de_la_entidad_participante_las_comisiones_recon_3b3366 -> Sujeto_rol_alcance_pagjub: sin mención
idx 9856: aplica_a Obligacion_actualizar_la_firma_registrada_cada_vez_que_la_entidad_lo_estime_necesario__ctac_bb1e03 -> Sujeto_banco: sin mención
idx 9858: aplica_a Obligacion_actuar_coordinadamente_cuando_corresponda_con_el_personal_que_lo_represente_a_ni_a7e9a0 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 9860: aplica_a Obligacion_ademas_en_los_legajos_deberan_constar_los_analisis_que_se_lleven_a_cabo_con_moti_53c63a -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9862: aplica_a Obligacion_adicionalmente_a_los_restantes_requisitos_que_le_sean_aplicables_a_la_operacion__2e60d5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9865: aplica_a Obligacion_adicionalmente_el_sujeto_obligado_debera_verificar_si_este_tipo_de_situaciones_q_e9b873 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 9868: aplica_a Obligacion_adicionalmente_y_en_igual_plazo_las_entidades_financieras_que_brinden_servicios__f113fb -> Sujeto_entidad_financiera: sin mención
idx 9871: aplica_a Obligacion_administracion_del_registro_de_firmas_digitalizadas_reproducidas_electronicament_ac6927 -> Sujeto_banco: sin mención
idx 9873: aplica_a Obligacion_adoptar_acciones_que_reduzcan_su_reiteracion__pro_s3_4099c6 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 9875: aplica_a Obligacion_adoptar_los_procedimientos_necesarios_para_efectuar_el_pago_de_cheques_asumiendo_aa0279 -> Sujeto_banco: sin mención
idx 9878: aplica_a Obligacion_adoptar_los_recaudos_necesarios_a_los_fines_de_asegurar_que_el_cuentacorrentista_a998e3 -> Sujeto_banco: sin mención
idx 9880: aplica_a Obligacion_adoptar_los_recaudos_necesarios_a_los_fines_de_asegurar_que_el_cuentacorrentista_b5cbe7 -> Sujeto_banco: sin mención
idx 9882: aplica_a Obligacion_agregar_dentro_de_las_48_horas_habiles_de_presentada_la_nota_a_que_se_refiere_el_7cdfa3 -> Sujeto_banco: sin mención
idx 9892: aplica_a Obligacion_al_calcular_la_tasa_el_cociente_entre_el_numerador_y_el_denominador_anualizado_d_f1d938 -> Sujeto_banco: sin mención
idx 9894: aplica_a Obligacion_al_determinar_el_vencimiento_de_una_posicion_de_titulizacion_se_debera_tener_en__3efcdf -> Sujeto_rol_alcance_capmin: sin mención
idx 9896: aplica_a Obligacion_al_equivalente_delta_se_agregan_exigencias_adicionales_para_la_cobertura_de_los__5bd2a0 -> Sujeto_rol_alcance_capmin: sin mención
idx 9898: aplica_a Obligacion_al_evaluar_la_capacidad_de_repago_el_enfasis_debera_ponerse_en_el_analisis_de_lo_3b39de -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9900: aplica_a Obligacion_al_importe_que_surja_de_estas_expresiones_se_le_aplicara_el_ponderador_correspon_ef2caa -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 9905: aplica_a Obligacion_al_momento_de_evaluar_la_capacidad_de_pago_de_la_contraparte_individual_las_enti_59f37d -> Sujeto_rol_alcance_capmin: sin mención
idx 9907: aplica_a Obligacion_al_momento_de_identificar_al_donante_se_debera_obtener_el_numero_de_clave_bancar_edcac5 -> Sujeto_banco: sin mención
idx 9910: aplica_a Obligacion_al_momento_de_la_aplicacion_de_los_fondos_adquiridos_se_debera_efectuar_un_bolet_e70ceb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9914: aplica_a Obligacion_al_momento_del_otorgamiento_de_financiaciones_a_personas_humanas_se_debera_tener_2fe533 -> Sujeto_entidad_financiera: sin mención
idx 9917: aplica_a Obligacion_al_momento_del_otorgamiento_de_financiaciones_a_personas_humanas_se_debera_tener_b4130f -> Sujeto_persona_humana: sin mención
idx 9920: aplica_a Obligacion_al_rechazar_un_cheque_la_entidad_girada_debe_hacer_constar_la_negativa_con_firma_8140a6 -> Sujeto_banco: sin mención
idx 9922: aplica_a Obligacion_al_recibir_los_extractos_hacer_llegar_a_la_entidad_su_conformidad_con_el_saldo_o_5b67d4 -> Sujeto_banco: sin mención
idx 9939: aplica_a Obligacion_al_retirar_la_chequera_el_titular_debe_dejar_constancia_en_el_recibo_de_que_libe_df9f74 -> Sujeto_banco: sin mención
idx 9941: aplica_a Obligacion_alcanzar_cobertura_del_servicio_con_cajeros_automaticos_accesibles_en_al_menos_e_b93699 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 9944: aplica_a Obligacion_ambas_partes_documentante_y_propietario_de_la_mercaderia_son_responsables_del_cu_3aa260 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9947: aplica_a Obligacion_ante_pedido_posterior_del_tenedor_cursado_por_medio_de_la_entidad_depositaria_o__0b9ccd -> Sujeto_banco: sin mención
idx 9949: aplica_a Obligacion_ante_pedido_posterior_del_tenedor_cursado_por_medio_de_la_entidad_depositaria_o__165f1a -> Sujeto_banco: sin mención
idx 9950: aplica_a Obligacion_ante_pedido_posterior_del_tenedor_cursado_por_medio_de_la_entidad_depositaria_o__165f1a -> Sujeto_entidad_depositaria: sin mención
idx 9952: aplica_a Obligacion_ante_requerimiento_que_formule_la_sefyc_y_con_efectividad_a_la_fecha_que_en_cada_83ee75 -> Sujeto_rol_alcance_capmin: sin mención
idx 9954: aplica_a Obligacion_antes_de_devolverlo_debera_hacer_constar_esa_negativa_al_dorso_del_mismo_titulo__cd7598 -> Sujeto_banco: sin mención
idx 9956: aplica_a Obligacion_apertura_del_legajo_para_deudores_en_concurso_preventivo_con_creditos_posteriore_e7aa5f -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 9958: aplica_a Obligacion_aplicacion_de_intereses_segun_la_tasa_que_aplica_el_banco_de_la_nacion_argentina_b4ec88 -> Sujeto_banco: sin mención
idx 9960: aplica_a Obligacion_aplicacion_de_las_condiciones_establecidas_en_los_incisos_i_y_ii_para_que_la_rep_a9d2e7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9962: aplica_a Obligacion_aplicando_en_los_demas_aspectos_las_correspondientes_disposiciones_establecidas__bee9f3 -> Sujeto_rol_alcance_capmin: sin mención
idx 9964: aplica_a Obligacion_aplicar_estas_disposiciones_asi_como_las_que_el_sujeto_obligado_establezca_en_ma_a540a1 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 9966: aplica_a Obligacion_aplicara_la_comision_respectiva_por_el_concepto_de_saldos_inmovilizados__ctacte__57fb60 -> Sujeto_banco: sin mención
idx 9968: aplica_a Obligacion_aplicaran_50_de_las_ganancias_o_100_de_las_perdidas_desde_el_ultimo_estado_finan_b4e261 -> Sujeto_rol_alcance_capmin: sin mención
idx 9970: aplica_a Obligacion_aprobar_y_supervisar_la_implementacion_del_codigo_de_gobierno_societario_y_de_lo_593396 -> Sujeto_entidad_financiera: sin mención
idx 9972: aplica_a Obligacion_apruebe_el_diseno_y_funcionamiento_del_sistema_de_retribuciones_de_todo_el_perso_04a908 -> Sujeto_entidad_financiera: sin mención
idx 9975: aplica_a Obligacion_apruebe_politicas_de_educacion_y_entrenamiento_al_personal_en_materia_de_genero__c03682 -> Sujeto_entidad_financiera: sin mención
idx 9977: aplica_a Obligacion_apruebe_politicas_de_seleccion_de_personal_que_promuevan_ambitos_de_trabajo_incl_85c85a -> Sujeto_entidad_financiera: sin mención
idx 9979: aplica_a Obligacion_aquel_se_trasladara_al_primer_dia_habil_bancario_siguiente__ctacte_12_5_5640eb -> Sujeto_banco: sin mención
idx 9981: aplica_a Obligacion_arbitrar_los_medios_necesarios_para_evitar_que_se_realicen_pagos_duplicados_tota_aef77a -> Sujeto_banco: sin mención
idx 9983: aplica_a Obligacion_arbitrar_medios_para_que_comunicaciones_avisos_y_o_publicidades_realizadas_por_s_795ba2 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 9986: aplica_a Obligacion_archivar_a_disposicion_del_bcra_toda_la_documentacion_utilizada_en_el_marco_del__483b3b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9988: aplica_a Obligacion_archivar_a_disposicion_del_bcra_toda_la_documentacion_utilizada_en_el_marco_del__4b98e4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 9991: aplica_a Obligacion_archivar_las_actuaciones_vinculadas_a_la_denuncia_recibida_y_a_los_rechazos_efec_7d377b -> Sujeto_banco: sin mención
idx 9993: aplica_a Obligacion_archivar_las_actuaciones_vinculadas_a_la_denuncia_recibida_y_a_los_rechazos_efec_9c2bfe -> Sujeto_banco: sin mención
idx 9995: aplica_a Obligacion_archivar_las_actuaciones_vinculadas_a_la_denuncia_recibida_y_a_los_rechazos_efec_ba4c8d -> Sujeto_banco: sin mención
idx 9999: aplica_a Obligacion_asegurar_que_el_echeq_sea_librado_sin_defectos_formales_y_conforme_a_los_mecanis_9091c5 -> Sujeto_banco: sin mención
idx 10002: aplica_a Obligacion_asegurar_que_la_informacion_sobre_operaciones_se_pone_a_disposicion_del_publico__a03e4b -> Sujeto_entidad_financiera: sin mención
idx 10004: aplica_a Obligacion_asegurar_que_las_actividades_de_la_entidad_cumplan_con_niveles_de_seguridad_y_so_59e72e -> Sujeto_entidad_financiera: sin mención
idx 10007: aplica_a Obligacion_asegurar_que_las_actividades_de_la_entidad_sean_consistentes_con_la_estrategia_d_d2a3c2 -> Sujeto_entidad_financiera: sin mención
idx 10009: aplica_a Obligacion_asegurar_que_los_terminos_de_la_contratacion_puedan_ser_leidos_descargados_y_gua_a8fa7c -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10011: aplica_a Obligacion_asegurar_que_se_lleve_a_cabo_una_evaluacion_anual_del_sistema_de_incentivos_econ_51df5e -> Sujeto_entidad_financiera: sin mención
idx 10013: aplica_a Obligacion_asegurarse_de_introducir_el_sobre_que_contenga_el_efectivo_o_cheques_conjuntamen_35a417 -> Sujeto_usuario_de_servicios_financieros: sin mención
idx 10015: aplica_a Obligacion_asegurarse_de_que_la_informacion_sobre_estas_actividades_y_sus_riesgos_esta_disp_8f006b -> Sujeto_entidad_financiera: sin mención
idx 10017: aplica_a Obligacion_asegurarse_de_que_tales_medios_les_permitan_dar_total_cumplimiento_a_la_normativ_1e75c6 -> Sujeto_banco: sin mención
idx 10019: aplica_a Obligacion_asegure_una_relacion_efectiva_con_los_supervisores__lingob_2_1_13_af5741 -> Sujeto_entidad_financiera: sin mención
idx 10021: aplica_a Obligacion_asegurese_de_que_se_implementen_conforme_a_lo_previsto_los_sistemas_de_retribuci_95fa0f -> Sujeto_entidad_financiera: sin mención
idx 10025: aplica_a Obligacion_asignar_responsabilidades_al_personal_de_la_entidad__lingob_3_1_4_0a7692 -> Sujeto_entidad_financiera: sin mención
idx 10027: aplica_a Obligacion_asignar_un_numero_de_identificacion_numero_apx_que_permitira_la_incorporacion_al_04a2fd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10029: aplica_a Obligacion_asimismo_pondra_en_conocimiento_del_interesado_el_tramite_cumplido__ctacte_8_8_2_097382 -> Sujeto_banco: sin mención
idx 10031: aplica_a Obligacion_asumir_sus_responsabilidades_frente_a_los_accionistas_y_tener_en_cuenta_los_inte_c76158 -> Sujeto_entidad_financiera: sin mención
idx 10034: aplica_a Obligacion_bancos_otras_instituciones_financieras_del_exterior_y_otros_prestatarios_no_radi_bfe7da -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10036: aplica_a Obligacion_cada_comunicacion_al_banco_central_de_la_republica_argentina_incluira_informacio_a863c8 -> Sujeto_banco: sin mención
idx 10038: aplica_a Obligacion_cada_lado_de_un_swap_de_moneda_se_debera_imputar_a_la_escala_de_vencimientos_de__52cb7b -> Sujeto_rol_alcance_capmin: sin mención
idx 10040: aplica_a Obligacion_cada_termino_dentro_de_los_3_componentes_y_el_resultado_monetario_debe_ser_calcu_8515d6 -> Sujeto_rol_alcance_capmin: sin mención
idx 10042: aplica_a Obligacion_cada_termino_dentro_de_los_3_componentes_y_el_resultado_monetario_debe_ser_infor_c52248 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10044: aplica_a Obligacion_cada_uno_de_los_citados_archivos_debera_ser_entregado_a_la_gerencia_de_cuentas_c_f67862 -> Sujeto_rol_alcance_pagjub: sin mención
idx 10052: aplica_a Obligacion_capital_minimo_necesario_para_cubrir_el_riesgo_de_mantener_posiciones_en_moneda__a46d6a -> Sujeto_rol_alcance_capmin: sin mención
idx 10055: aplica_a Obligacion_caracteristicas_de_la_configuracion_utilizada_para_esta_aplicacion_equipos_de_re_570916 -> Sujeto_banco: sin mención
idx 10057: aplica_a Obligacion_cerciorarse_de_que_los_controles_internos_sobre_las_actividades_realizadas_a_tra_840ea7 -> Sujeto_entidad_financiera: sin mención
idx 10060: aplica_a Obligacion_cerciorarse_de_que_los_controles_internos_sobre_las_actividades_realizadas_a_tra_c7150c -> Sujeto_entidad_financiera: sin mención
idx 10063: aplica_a Obligacion_certifica_en_caracter_de_entidad_encargada_del_seguimiento_de_la_oficializacion__d144d4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10067: aplica_a Obligacion_certificar_el_cumplimiento_de_las_condiciones_de_elegibilidad_de_las_operaciones_650be0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10070: aplica_a Obligacion_certificar_el_cumplimiento_de_las_condiciones_para_la_elegibilidad_del_proyecto__20a2de -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10073: aplica_a Obligacion_certifique_la_validez_formal_del_pertinente_cheque_a_la_fecha_en_que_se_lo_trans_8ed52d -> Sujeto_banco: sin mención
idx 10075: aplica_a Obligacion_claras_lineas_de_reporte_de_la_informacion_para_los_responsables_del_proceso_de__988bde -> Sujeto_rol_alcance_capmin: sin mención
idx 10077: aplica_a Obligacion_coadyuvar_a_la_observancia_de_las_obligaciones_emergentes_de_la_normativa_aplica_77b24c -> Sujeto_entidad_financiera: sin mención
idx 10080: aplica_a Obligacion_como_minimo_una_vez_al_ano_el_servicio_de_atencion_al_usuario_de_servicios_finan_85fcf1 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10082: aplica_a Obligacion_como_parte_del_procedimiento_de_valuacion_a_mercado_o_a_modelo_las_entidades_deb_fb01c6 -> Sujeto_rol_alcance_capmin: sin mención
idx 10085: aplica_a Obligacion_comprenda_el_marco_regulatorio__lingob_2_1_13_3607c7 -> Sujeto_entidad_financiera: sin mención
idx 10087: aplica_a Obligacion_comprobar_que_el_comite_de_auditoria_de_la_entidad_financiera_supervise_la_labor_683245 -> Sujeto_entidad_financiera: sin mención
idx 10089: aplica_a Obligacion_comprobar_que_la_alta_gerencia_siga_politicas_claras_que_eviten_la_realizacion_d_e9a7e9 -> Sujeto_entidad_financiera: sin mención
idx 10091: aplica_a Obligacion_comprometa_el_tiempo_y_la_dedicacion_necesarios_para_cumplir_con_sus_responsabil_d8059f -> Sujeto_entidad_financiera: sin mención
idx 10093: aplica_a Obligacion_computaran_100_de_los_quebrantos_que_no_se_encuentren_considerados_en_los_estado_3c07aa -> Sujeto_rol_alcance_capmin: sin mención
idx 10095: aplica_a Obligacion_computaran_100_de_los_resultados_del_ejercicio_en_curso_registrados_al_cierre_de_abc68a -> Sujeto_rol_alcance_capmin: sin mención
idx 10097: aplica_a Obligacion_computaran_100_de_los_resultados_registrados_hasta_el_ultimo_estado_financiero_t_ca675f -> Sujeto_rol_alcance_capmin: sin mención
idx 10099: aplica_a Obligacion_comunicacion_por_escrito_a_la_superintendencia_de_entidades_financieras_y_cambia_16582f -> Sujeto_banco: sin mención
idx 10101: aplica_a Obligacion_comunicar_a_la_entidad_cualquier_modificacion_de_sus_contratos_sociales_estatuto_fe7a1a -> Sujeto_banco: sin mención
idx 10109: aplica_a Obligacion_comunicar_a_los_usuarios_que_no_divulguen_el_numero_de_clave_personal_ni_lo_escr_f61d85 -> Sujeto_banco: sin mención
idx 10111: aplica_a Obligacion_comunicar_de_inmediato_a_la_entidad_la_contingencia_ocurrida_telefonicamente_o_p_e3523c -> Sujeto_banco: sin mención
idx 10113: aplica_a Obligacion_comunicar_la_circunstancia_de_diferencia_entre_comprobante_e_importe_a_los_banco_5cb248 -> Sujeto_usuario_de_servicios_financieros: sin mención
idx 10115: aplica_a Obligacion_con_indicacion_precisa_de_las_fechas_de_comienzo_y_de_finalizacion_asi_como_sus__218d8c -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10117: aplica_a Obligacion_con_la_comunicacion_de_modificacion_de_funcionarios_es_necesario_proceder_a_la_r_a721c8 -> Sujeto_rol_alcance_pagjub: sin mención
idx 10123: aplica_a Obligacion_con_relacion_a_la_crc_se_debera_tener_en_cuenta_las_opciones_incorporadas_que_pu_23124d -> Sujeto_rol_alcance_capmin: sin mención
idx 10125: aplica_a Obligacion_con_relacion_a_los_restantes_requisitos_previstos_en_el_articulo_4_del_decreto_6_c70fb1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10127: aplica_a Obligacion_con_relacion_al_diseno_de_los_registros_de_cabecera_y_de_detalle_se_debera_obser_9dc4b6 -> Sujeto_rol_alcance_pagjub: sin mención
idx 10129: aplica_a Obligacion_con_respecto_a_los_creditos_que_se_asignen_a_los_tramos_i_y_ii_de_los_margenes_a_c54507 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10131: aplica_a Obligacion_condicion_de_persona_expuesta_politicamente_declaracion_jurada_de_pep_o_no_pep___5222b6 -> Sujeto_banco: sin mención
idx 10133: aplica_a Obligacion_confeccion_de_declaraciones_juradas_previstas_en_los_puntos_3_16_3_1_y_3_16_3_2__bb4aa3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10225: aplica_a Obligacion_conservar_constancia_de_haber_permitido_el_ejercicio_del_derecho_a_documentacion_1572ca -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10227: aplica_a Obligacion_conservar_constancia_del_ejercicio_de_ese_derecho_por_parte_de_dichos_usuarios___44cb48 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10229: aplica_a Obligacion_conservar_la_documentacion_respaldatoria_a_fin_de_dar_de_baja_o_modificar_el_per_340eb4 -> Sujeto_banco: sin mención
idx 10231: aplica_a Obligacion_conservaran_debidamente_ordenadas_las_actuaciones_que_se_produzcan_a_raiz_de_su__b364ee -> Sujeto_banco: sin mención
idx 10233: aplica_a Obligacion_conservaran_debidamente_ordenadas_las_actuaciones_que_se_produzcan_a_raiz_de_su__fc5e8c -> Sujeto_banco: sin mención
idx 10235: aplica_a Obligacion_consignar_al_dorso_de_los_cheques_librados_en_formato_papel_o_certificados_nomin_230abb -> Sujeto_banco: sin mención
idx 10238: aplica_a Obligacion_consignar_c_si_el_contrato_es_una_compra_a_termino_o_v_si_es_una_venta_a_termino_11fe3f -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10240: aplica_a Obligacion_consignar_el_plazo_residual_del_activo_subyacente_ej_en_un_futuro_sobre_un_titul_f7e13f -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10242: aplica_a Obligacion_consignar_el_valor_del_subyacente_pactado_ej_valor_de_la_tasa_fija_pactada_valor_4a2192 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10244: aplica_a Obligacion_consignar_la_tasa_de_cupon_corriente_cuando_corresponda_ej_en_un_futuro_sobre_un_5e4606 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10246: aplica_a Obligacion_consolidar_el_total_de_las_posiciones_de_las_subsidiarias_en_las_que_la_entidad__effbca -> Sujeto_rol_alcance_capmin: sin mención
idx 10250: aplica_a Obligacion_constancia_fehaciente_de_aprobacion_de_la_operatoria_de_emision_de_instrumentos__3bc4db -> Sujeto_banco: sin mención
idx 10253: aplica_a Obligacion_contar_adicionalmente_con_una_certificacion_de_auditor_externo_en_la_cual_se_dej_6321bd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10255: aplica_a Obligacion_contar_con_conformidad_previa_del_bcra_para_acceder_al_mercado_de_cambios_para_r_436d13 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 10256: aplica_a Obligacion_contar_con_conformidad_previa_del_bcra_para_acceder_al_mercado_de_cambios_para_r_436d13 -> Sujeto_entidad_financiera: sin mención
idx 10259: aplica_a Obligacion_contar_con_la_correspondiente_convalidacion_respecto_al_cumplimiento_de_lo_previ_9fc721 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10265: aplica_a Obligacion_contar_con_la_expresa_autorizacion_del_titular_de_la_cuenta_corriente_para_propo_85d4ef -> Sujeto_banco: sin mención
idx 10267: aplica_a Obligacion_contar_con_la_opinion_del_auditor_externo_de_la_entidad_sobre_la_factibilidad_de_f9c3b8 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10269: aplica_a Obligacion_contar_con_la_opinion_favorable_sobre_la_calidad_de_las_garantias_formulada_por__35685e -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10271: aplica_a Obligacion_contar_con_procedimientos_efectivos_que_permitan_detectar_aquellas_transferencia_36e564 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10275: aplica_a Obligacion_contar_con_reproductor_de_texto_a_voz_en_home_banking_y_banca_movil_para_permiti_487dfb -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10278: aplica_a Obligacion_contar_con_un_plan_apropiado_para_la_sucesion_de_los_principales_ejecutivos__lin_0c2b46 -> Sujeto_entidad_financiera: sin mención
idx 10280: aplica_a Obligacion_contar_con_una_declaracion_jurada_del_referido_agente_local_en_la_que_conste_que_fc57c7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10282: aplica_a Obligacion_contar_con_una_declaracion_jurada_del_representante_legal_del_vpu_o_un_apoderado_28711a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10291: aplica_a Obligacion_contendran_las_enunciaciones_esenciales_requeridas_por_los_articulos_2_4_y_54_de_37b122 -> Sujeto_banco: sin mención
idx 10293: aplica_a Obligacion_contribuir_a_la_mejora_de_los_mencionados_procesos_los_controles_relacionados_y__9276ef -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10296: aplica_a Obligacion_copia_de_la_solicitud_particular_autenticada_por_autoridad_aduanera_competente_e_095902 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10298: aplica_a Obligacion_corresponde_que_al_momento_en_que_la_pertinente_informacion_quede_disponible_en__88d0e6 -> Sujeto_banco: sin mención
idx 10300: aplica_a Obligacion_correspondera_clasificar_en_la_categoria_de_irrecuperable_a_los_clientes_que_cua_6b04ad -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10304: aplica_a Obligacion_correspondera_la_reclasificacion_inmediata_del_deudor_en_el_nivel_siguiente_infe_4baee4 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10306: aplica_a Obligacion_correspondera_la_reclasificacion_inmediata_en_el_nivel_siguiente_inferior_cuando_e5b25a -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10308: aplica_a Obligacion_correspondera_mantener_en_la_casa_central_de_la_entidad_una_copia_del_legajo_de__b6e098 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10310: aplica_a Obligacion_correspondera_reconocer_el_importe_de_los_gastos_que_resulten_razonables_realiza_f4c264 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10312: aplica_a Obligacion_cualquier_derecho_sobre_el_inmueble_debera_ser_juridicamente_exigible__cap_2_9_2_8a8968 -> Sujeto_rol_alcance_capmin: sin mención
idx 10314: aplica_a Obligacion_cualquier_modificacion_en_la_nomina_de_funcionarios_designados_debera_realizarse_8321f8 -> Sujeto_rol_alcance_pagjub: sin mención
idx 10316: aplica_a Obligacion_cualquier_recurso_y_o_aclaracion_sobre_la_rendicion_de_cuentas_realizada_debera__c48c82 -> Sujeto_rol_alcance_pagjub: sin mención
idx 10318: aplica_a Obligacion_cualquier_restitucion_de_capital_requerira_la_autorizacion_previa_de_la_sefyc__c_0fb80c -> Sujeto_rol_alcance_capmin: sin mención
idx 10321: aplica_a Obligacion_cuando_el_cliente_mantenga_financiaciones_por_ambos_conceptos_los_creditos_para__9c8951 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10323: aplica_a Obligacion_cuando_el_cuentacorrentista_no_acredite_la_formulacion_de_la_denuncia_judicial_i_b1998c -> Sujeto_banco: sin mención
idx 10325: aplica_a Obligacion_cuando_el_importe_garantizado_sea_inferior_al_monto_de_la_exposicion_y_las_parte_ca7a1f -> Sujeto_rol_alcance_capmin: sin mención
idx 10342: aplica_a Obligacion_cuando_el_monto_a_imputar_al_permiso_por_este_mecanismo_supere_el_equivalente_a__3cbcee -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10344: aplica_a Obligacion_cuando_el_monto_a_imputar_supere_usd_25_000_la_entidad_debera_contar_con_una_cer_307f91 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10347: aplica_a Obligacion_cuando_el_monto_adeudado_sea_superior_a_usd_25_000_dolares_estadounidenses_veint_d1bda0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10349: aplica_a Obligacion_cuando_el_pago_a_nombre_del_cliente_encuadre_en_el_punto_10_10_2_3_se_debera_dej_e55a35 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10358: aplica_a Obligacion_cuando_el_proveedor_de_proteccion_pueda_solicitar_anticipadamente_la_liquidacion_5724e5 -> Sujeto_rol_alcance_capmin: sin mención
idx 10360: aplica_a Obligacion_cuando_el_riesgo_subyacente_originado_en_exposiciones_en_derivados_o_fuera_de_ba_545589 -> Sujeto_rol_alcance_capmin: sin mención
idx 10363: aplica_a Obligacion_cuando_el_sujeto_obligado_pretenda_incorporar_nuevos_conceptos_en_calidad_de_com_d0e4c2 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10366: aplica_a Obligacion_cuando_el_usuario_posea_en_la_entidad_financiera_obligada_una_cuenta_a_la_vista__eace80 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10368: aplica_a Obligacion_cuando_en_la_misma_liquidacion_esten_involucradas_dos_o_mas_destinaciones_de_exp_c40039 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10371: aplica_a Obligacion_cuando_estas_cuentas_sean_utilizadas_por_mercados_o_camaras_compensadoras_de_cap_8ba9f2 -> Sujeto_banco: sin mención
idx 10378: aplica_a Obligacion_cuando_la_certificacion_sea_emitida_sobre_un_echeq_la_entidad_certificante_deber_0086ce -> Sujeto_banco: sin mención
idx 10380: aplica_a Obligacion_cuando_la_consulta_o_el_reclamo_sea_iniciada_o_llamando_a_una_linea_o_central_te_90c14f -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10383: aplica_a Obligacion_cuando_la_devolucion_se_curse_por_intermedio_de_una_camara_compensadora_la_fecha_e78433 -> Sujeto_banco: sin mención
idx 10386: aplica_a Obligacion_cuando_la_entidad_debiera_rectificar_una_rendicion_de_cuentas_posteriormente_a_l_86b886 -> Sujeto_rol_alcance_pagjub: sin mención
idx 10388: aplica_a Obligacion_cuando_la_entidad_decida_el_cobro_de_una_comision_y_o_cargo_por_estas_operacione_31da97 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10391: aplica_a Obligacion_cuando_la_entidad_decida_el_cobro_de_una_comision_y_o_cargo_por_estas_operacione_b20ce8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10393: aplica_a Obligacion_cuando_la_entidad_desarrolle_modelos_propios_estos_se_deberan_basar_en_supuestos_30abad -> Sujeto_rol_alcance_capmin: sin mención
idx 10396: aplica_a Obligacion_cuando_la_entidad_financiera_preste_servicios_de_compensacion_a_clientes_aplicar_363bcc -> Sujeto_miembro_compensador: sin mención
idx 10399: aplica_a Obligacion_cuando_la_entidad_financiera_realice_operaciones_con_una_qccp_debera_determinar__a65dcb -> Sujeto_rol_alcance_capmin: sin mención
idx 10402: aplica_a Obligacion_cuando_la_entidad_financiera_sea_cliente_del_miembro_compensador_y_no_se_cumplan_f03816 -> Sujeto_rol_alcance_capmin: sin mención
idx 10404: aplica_a Obligacion_cuando_la_entidad_no_emplee_el_metodo_simplificado_para_el_computo_de_la_exigenc_323a05 -> Sujeto_rol_alcance_capmin: sin mención
idx 10409: aplica_a Obligacion_cuando_la_envergadura_del_sujeto_obligado_y_o_la_naturaleza_y_complejidad_de_sus_a00b94 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10411: aplica_a Obligacion_cuando_la_estructura_del_modelo_requiera_datos_en_todos_los_escenarios_0_a_6_par_4cec77 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10419: aplica_a Obligacion_cuando_la_estructura_involucre_a_un_spe_se_considerara_que_todas_las_exposicione_fe6ff9 -> Sujeto_rol_alcance_capmin: sin mención
idx 10421: aplica_a Obligacion_cuando_la_gestion_de_cobro_o_registracion_se_haya_efectuado_con_intervencion_de__2bb70f -> Sujeto_entidad_girada: sin mención
idx 10423: aplica_a Obligacion_cuando_la_gestion_se_efectua_con_intervencion_de_camara_compensadora_la_entidad__827d02 -> Sujeto_entidad_depositaria: sin mención
idx 10425: aplica_a Obligacion_cuando_la_inclusion_corresponda_a_una_persona_fisica_las_entidades_deberan_proce_79148d -> Sujeto_banco: sin mención
idx 10428: aplica_a Obligacion_cuando_la_presentacion_se_efectue_a_traves_de_mandatario_o_beneficiario_de_una_c_3d009c -> Sujeto_banco: sin mención
idx 10430: aplica_a Obligacion_cuando_la_proteccion_crediticia_proporcionada_por_un_mismo_proveedor_tenga_plazo_901021 -> Sujeto_rol_alcance_capmin: sin mención
idx 10432: aplica_a Obligacion_cuando_la_proteccion_crediticia_y_la_exposicion_esten_denominadas_en_distintas_m_cc5ee4 -> Sujeto_rol_alcance_capmin: sin mención
idx 10434: aplica_a Obligacion_cuando_los_activos_de_un_miembro_compensador_o_cliente_se_coloquen_en_garantia_a_768a95 -> Sujeto_rol_alcance_capmin: sin mención
idx 10436: aplica_a Obligacion_cuando_los_activos_hayan_sido_adquiridos_a_terceros_el_originante_fiduciario_de__9b9e29 -> Sujeto_rol_alcance_capmin: sin mención
idx 10438: aplica_a Obligacion_cuando_los_aportes_contabilizados_provengan_de_la_capitalizacion_de_deuda_subord_b28211 -> Sujeto_rol_alcance_capmin: sin mención
idx 10440: aplica_a Obligacion_cuando_los_terminos_se_refieren_a_resultados_la_reexpresion_operara_desde_el_mes_771e13 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10442: aplica_a Obligacion_cuando_n_sea_igual_a_cero_n_0_debera_observarse_una_exigencia_equivalente_al_lim_53037f -> Sujeto_rol_alcance_capmin: sin mención
idx 10446: aplica_a Obligacion_cuando_para_una_exposicion_existan_mas_de_dos_calificaciones_crediticias_se_util_26bca2 -> Sujeto_rol_alcance_capmin: sin mención
idx 10449: aplica_a Obligacion_cuando_se_empleen_boletas_estas_deberan_contener_como_minimo_los_siguientes_dato_5f63d5 -> Sujeto_banco: sin mención
idx 10451: aplica_a Obligacion_cuando_se_genere_un_incremento_en_el_costo_total_de_los_restantes_productos_o_se_dbde0b -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10459: aplica_a Obligacion_cuando_se_inscriban_las_entidades_deberan_indicar_i_codigo_de_la_entidad_financi_3304e8 -> Sujeto_banco: sin mención
idx 10461: aplica_a Obligacion_cuando_se_inscriban_las_entidades_deberan_indicar_ii_su_situacion_obligada_no_ob_58d992 -> Sujeto_banco: sin mención
idx 10463: aplica_a Obligacion_cuando_se_inscriban_las_entidades_deberan_indicar_iii_si_registran_cuentas_decla_cf280a -> Sujeto_banco: sin mención
idx 10465: aplica_a Obligacion_cuando_se_inscriban_las_entidades_deberan_indicar_v_porcentaje_de_esas_cuentas_q_70ca9c -> Sujeto_banco: sin mención
idx 10467: aplica_a Obligacion_cuando_se_inscriban_las_entidades_en_caso_afirmativo_deberan_indicar_iv_cantidad_588d40 -> Sujeto_banco: sin mención
idx 10469: aplica_a Obligacion_cuando_se_modifique_el_valor_de_las_comisiones_el_cuerpo_de_las_notificaciones_d_98975d -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10472: aplica_a Obligacion_cuando_se_reconozcan_intereses_sobre_los_saldos_acreedores_se_informaran_las_tas_458193 -> Sujeto_banco: sin mención
idx 10475: aplica_a Obligacion_cuando_se_transfieran_cheques_de_pago_diferido_en_deposito_para_su_negociacion_e_4ee981 -> Sujeto_banco: sin mención
idx 10477: aplica_a Obligacion_cuando_se_trate_de_depositos_de_cheques_u_ordenes_de_pago_oficial_nominativas_de_07874f -> Sujeto_banco: sin mención
idx 10479: aplica_a Obligacion_cuando_se_trate_de_depositos_de_cheques_u_ordenes_de_pago_oficial_nominativas_de_9b1e42 -> Sujeto_banco: sin mención
idx 10481: aplica_a Obligacion_cuando_se_trate_de_informacion_ingresada_fuera_de_termino_o_incumplimientos_dete_ce9dba -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10483: aplica_a Obligacion_cuando_se_trate_de_informacion_ingresada_fuera_de_termino_o_incumplimientos_dete_e62904 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10485: aplica_a Obligacion_cuando_se_trate_de_liquidaciones_de_tarjetas_de_credito_de_sistemas_abiertos_las_06f4be -> Sujeto_banco: sin mención
idx 10488: aplica_a Obligacion_cuando_se_trate_de_solicitudes_de_productos_o_servicios_sometidas_a_aprobacion_p_46a1f8 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10490: aplica_a Obligacion_cuando_un_producto_basico_forme_parte_de_un_contrato_a_plazo_hubiera_que_entrega_7ec5e3 -> Sujeto_rol_alcance_capmin: sin mención
idx 10500: aplica_a Obligacion_cuando_un_tercero_desarrolle_tareas_relativas_a_servicios_ofrecidos_por_los_suje_5e227b -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10502: aplica_a Obligacion_cuando_una_entidad_financiera_se_niegue_a_pagar_un_cheque_comun_o_de_pago_diferi_19c55d -> Sujeto_banco: sin mención
idx 10505: aplica_a Obligacion_cuando_uno_de_estos_eventos_ocurra_entre_dos_fechas_de_pago_previstas_se_debera__590c43 -> Sujeto_rol_alcance_capmin: sin mención
idx 10507: aplica_a Obligacion_cuenta_con_copia_de_la_factura_comercial_emitida_en_el_exterior_a_nombre_de_la_p_6f2875 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10509: aplica_a Obligacion_cuenta_con_una_declaracion_jurada_del_cliente_en_la_que_deja_constancia_de_que_e_9cfa6f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10512: aplica_a Obligacion_cuenta_con_una_declaracion_jurada_del_cliente_en_la_que_deja_constancia_de_que_l_ab9370 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10521: aplica_a Obligacion_cumplimentar_la_totalidad_de_ambas_obligaciones_dentro_de_los_5_dias_habiles_ban_34f643 -> Sujeto_banco: sin mención
idx 10523: aplica_a Obligacion_cumplimentar_los_requerimientos_de_informacion_que_establezca_el_bcra_respecto_a_a6b079 -> Sujeto_entidad_financiera: sin mención
idx 10525: aplica_a Obligacion_cumplimentar_los_requerimientos_de_informacion_que_establezca_el_bcra_respecto_a_b5bd16 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10527: aplica_a Obligacion_cumplimentar_los_requerimientos_de_informacion_que_establezca_el_bcra_respecto_a_fd4043 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10529: aplica_a Obligacion_cumplimiento_de_las_obligaciones_a_cargo_de_las_entidades_giradas_en_el_procedim_0b97e1 -> Sujeto_entidad_girada: sin mención
idx 10533: aplica_a Obligacion_cumplir_con_los_resguardos_de_secreto_a_que_se_refieren_el_art_39_de_la_ley_de_e_06c059 -> Sujeto_banco: sin mención
idx 10535: aplica_a Obligacion_custodiar_los_elementos_de_seguridad_convenidos_para_el_libramiento_visualizacio_588b20 -> Sujeto_banco: sin mención
idx 10538: aplica_a Obligacion_dar_a_usuarios_con_dificultades_visuales_la_opcion_de_obtener_en_sistema_braille_9a5b26 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10540: aplica_a Obligacion_dar_aviso_a_la_entidad_girada_en_caso_de_detectar_su_adulteracion_o_emision_apoc_12f6ca -> Sujeto_banco: sin mención
idx 10542: aplica_a Obligacion_dar_aviso_a_la_entidad_por_escrito_del_extravio_sustraccion_o_adulteracion_de_la_2c06fb -> Sujeto_banco: sin mención
idx 10544: aplica_a Obligacion_dar_cuenta_a_la_entidad_por_escrito_de_cualquier_cambio_de_domicilio_o_correo_el_5e359d -> Sujeto_banco: sin mención
idx 10547: aplica_a Obligacion_de_aprobar_la_estrategia_global_del_negocio_y_la_politica_y_de_instruir_a_la_alt_ea26ca -> Sujeto_entidad_financiera: sin mención
idx 10550: aplica_a Obligacion_de_corresponder_la_consolidacion_mensual_codigo_2_considerara_las_operaciones_de_ce75d5 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10552: aplica_a Obligacion_de_corresponder_las_monedas_residuales_puntos_6_2_2_2_y_6_2_2_7_de_las_normas_so_c329f4 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10561: aplica_a Obligacion_de_ejercerse_esta_opcion_debera_aplicarse_con_caracter_general_a_toda_la_cartera_9451d6 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10563: aplica_a Obligacion_de_entenderse_que_una_exposicion_podria_estar_sujeta_a_distintos_ponderadores_es_06428e -> Sujeto_rol_alcance_capmin: sin mención
idx 10569: aplica_a Obligacion_de_mantener_vigentes_los_planes_de_contingencia__lingob_2_4_4_8e5f0d -> Sujeto_entidad_financiera: sin mención
idx 10572: aplica_a Obligacion_de_no_haberse_alcanzado_el_acuerdo_dentro_del_plazo_establecido_debera_reclasifi_3ed9b7 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10574: aplica_a Obligacion_de_no_verificarse_la_correspondencia_debera_proceder_a_la_devolucion_de_la_trans_212809 -> Sujeto_banco: sin mención
idx 10576: aplica_a Obligacion_de_optar_por_esta_posibilidad_la_entidad_financiera_debera_contar_con_una_oficin_ac6bac -> Sujeto_entidad_financiera: sin mención
idx 10578: aplica_a Obligacion_de_ser_aceptada_la_opcion_de_extension_debera_incluirse_la_correspondiente_claus_9dff66 -> Sujeto_entidad_financiera: sin mención
idx 10581: aplica_a Obligacion_de_tratarse_de_monedas_extranjeras_distintas_del_dolar_estadounidense_se_convert_7d6328 -> Sujeto_rol_alcance_capmin: sin mención
idx 10583: aplica_a Obligacion_de_tratarse_de_una_ccp_que_no_califica_seran_de_aplicacion_las_previsiones_del_p_c6ea07 -> Sujeto_rol_alcance_capmin: sin mención
idx 10592: aplica_a Obligacion_de_tratarse_del_destino_previsto_en_el_punto_2_1_14_se_deberan_considerar_a_efec_b8d5de -> Sujeto_entidad_financiera: sin mención
idx 10597: aplica_a Obligacion_debe_evaluar_con_cuidado_las_practicas_de_la_entidad_en_materia_de_incentivos_cu_bff6ec -> Sujeto_entidad_financiera: sin mención
idx 10599: aplica_a Obligacion_debe_incluir_en_el_codigo_de_etica_estandares_que_abarquen_aspectos_referidos_a__a3ba56 -> Sujeto_entidad_financiera: sin mención
idx 10601: aplica_a Obligacion_debe_incluir_en_el_codigo_de_etica_estandares_que_abarquen_aspectos_referidos_a__f96099 -> Sujeto_entidad_financiera: sin mención
idx 10603: aplica_a Obligacion_debe_incluirse_numero_de_cuenta_o_codigo_internacional_de_cuenta_bancaria_iban___825e0c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10605: aplica_a Obligacion_debe_incluirse_numero_de_identificacion_del_cliente_en_la_entidad_ordenante__ext_c2887b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10607: aplica_a Obligacion_debe_representar_un_derecho_crediticio_directo_frente_al_proveedor_de_la_protecc_0e5362 -> Sujeto_rol_alcance_capmin: sin mención
idx 10609: aplica_a Obligacion_debe_ser_incondicional_el_contrato_de_proteccion_no_debe_contener_ninguna_clausu_f091da -> Sujeto_rol_alcance_capmin: sin mención
idx 10613: aplica_a Obligacion_debera_adjuntarse_el_compromiso_escrito_del_banco_suscripto_por_identico_nivel_f_603db6 -> Sujeto_banco: sin mención
idx 10619: aplica_a Obligacion_debera_calcularse_el_importe_equivalente_en_pesos_al_tipo_de_cambio_vendedor_del_e4c193 -> Sujeto_rol_alcance_capmin: sin mención
idx 10621: aplica_a Obligacion_debera_calcularse_la_exigencia_de_capital_multiplicando_la_exposicion_actual_pos_31d52d -> Sujeto_rol_alcance_capmin: sin mención
idx 10624: aplica_a Obligacion_debera_como_minimo_mantener_el_capital_requerido_por_todas_las_exposiciones_suby_be8042 -> Sujeto_rol_alcance_capmin: sin mención
idx 10627: aplica_a Obligacion_debera_considerarse_la_posibilidad_de_liquidacion_de_activos_no_imprescindibles__3463a0 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10629: aplica_a Obligacion_debera_considerarse_lo_dispuesto_en_el_punto_3_1_12__cap_3_1_3_4d3b28 -> Sujeto_entidad_originante_de_transferencia: sin mención
idx 10637: aplica_a Obligacion_debera_contar_para_la_puesta_en_vigencia_con_su_previa_autorizacion__ctacte_3_3__75261e -> Sujeto_banco: sin mención
idx 10640: aplica_a Obligacion_debera_contarse_con_los_datos_de_cada_empresa_y_representante_en_las_cuentas_cor_411711 -> Sujeto_banco: sin mención
idx 10642: aplica_a Obligacion_debera_contemplar_previamente_que_las_necesidades_de_los_usuarios_de_servicios_f_bfb14a -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10645: aplica_a Obligacion_debera_contemplarse_un_procedimiento_de_atencion_personalizado_para_aquellos_cli_2eadb5 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10647: aplica_a Obligacion_debera_darse_cumplimiento_al_requisito_complementario_previsto_en_el_punto_14_4__1e1a94 -> Sujeto_vpu_rigi: sin mención
idx 10657: aplica_a Obligacion_debera_declararse_en_la_partida_38000000_si_se_adopta_la_asignacion_de_los_flujo_683b3c -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10665: aplica_a Obligacion_debera_deducir_del_capital_ordinario_de_nivel_uno_co_n1_el_importe_total_en_conc_72ba3c -> Sujeto_rol_alcance_capmin: sin mención
idx 10670: aplica_a Obligacion_debera_dejar_constancia_del_termino_por_el_cual_se_extiende_la_certificacion__ct_7f1bae -> Sujeto_banco: sin mención
idx 10674: aplica_a Obligacion_debera_especificarse_expresamente_la_moneda_en_que_opera_la_cuenta_pesos_o_dolar_acf2e2 -> Sujeto_banco: sin mención
idx 10677: aplica_a Obligacion_debera_especificarse_tasa_de_interes_efectiva_anual_equivalente_al_calculo_de_lo_0d64e3 -> Sujeto_banco: sin mención
idx 10679: aplica_a Obligacion_debera_estar_adecuada_a_los_criterios_aplicables_en_materia_de_politica_de_credi_f5b3ad -> Sujeto_entidad_financiera: sin mención
idx 10687: aplica_a Obligacion_debera_informar_en_las_notas_a_los_estados_financieros_de_publicacion_el_efecto__2256ac -> Sujeto_rol_alcance_capmin: sin mención
idx 10689: aplica_a Obligacion_debera_informar_en_las_notas_a_los_estados_financieros_de_publicacion_que_ha_pre_6cd00f -> Sujeto_rol_alcance_capmin: sin mención
idx 10691: aplica_a Obligacion_debera_informarse_la_partida_39000000_por_todas_las_entidades_que_cumplan_los_re_d36be5 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10693: aplica_a Obligacion_debera_notificarse_a_traves_de_correo_electronico_del_usuario_en_aquellos_casos__df987d -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10695: aplica_a Obligacion_debera_notificarse_de_tal_circunstancia_y_resultados_a_su_responsable_de_atencio_79f0e5 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10697: aplica_a Obligacion_debera_notificarse_la_acreditacion_del_reintegro_o_su_puesta_a_disposicion_media_4ee630 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10699: aplica_a Obligacion_debera_notificarse_mediante_documento_escrito_dirigido_al_domicilio_del_usuario__23b79a -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10701: aplica_a Obligacion_debera_obrar_en_poder_del_sujeto_obligado_la_documentacion_respaldatoria_de_las__61ce77 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10703: aplica_a Obligacion_debera_observar_los_requisitos_de_debida_diligencia_para_usar_el_enfoque_estanda_551bcf -> Sujeto_rol_alcance_capmin: sin mención
idx 10712: aplica_a Obligacion_debera_presentar_una_certificacion_extendida_por_auditor_externo_o_contador_publ_fd7e7d -> Sujeto_entidad_financiera: sin mención
idx 10714: aplica_a Obligacion_debera_presentarse_en_original_y_duplicado__pagjub_2_1_8e9802 -> Sujeto_rol_alcance_pagjub: sin mención
idx 10716: aplica_a Obligacion_debera_preverse_el_debito_por_el_pago_de_cheques_de_ventanilla_a_sus_representan_029cd7 -> Sujeto_banco: sin mención
idx 10719: aplica_a Obligacion_debera_preverse_la_obligacion_de_actualizacion_de_la_declaracion_jurada_por_part_a3e395 -> Sujeto_banco: sin mención
idx 10721: aplica_a Obligacion_debera_proceder_de_igual_forma_cuando_tuviese_conocimiento_de_que_un_cheque_en_f_166fa5 -> Sujeto_banco: sin mención
idx 10723: aplica_a Obligacion_debera_rechazarse_la_registracion_de_los_cheques_de_pago_diferido_presentados_a__3f0335 -> Sujeto_banco: sin mención
idx 10725: aplica_a Obligacion_debera_rechazarse_la_registracion_de_los_cheques_de_pago_diferido_presentados_a__b021ba -> Sujeto_banco: sin mención
idx 10727: aplica_a Obligacion_debera_reintegrarse_el_importe_cobrado_o_adeudado_dentro_de_los_cinco_5_dias_hab_f9c846 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10729: aplica_a Obligacion_debera_reintegrarse_el_importe_cobrado_o_adeudado_dentro_de_los_diez_10_dias_hab_996044 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10738: aplica_a Obligacion_debera_remitir_al_bcra_la_certificacion_de_incumplido_en_gestion_de_cobro_para_e_f88870 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10740: aplica_a Obligacion_debera_ser_aprobado_por_el_directorio_o_autoridad_equivalente_del_sujeto_obligad_e1dac1 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10742: aplica_a Obligacion_debera_someterse_el_modelo_a_examenes_periodicos_a_fin_de_determinar_la_fiabilid_1a61e1 -> Sujeto_rol_alcance_capmin: sin mención
idx 10744: aplica_a Obligacion_debera_tenerse_en_cuenta_lo_dispuesto_en_el_punto_3_1__cap_2_12_11_abfea9 -> Sujeto_rol_alcance_capmin: sin mención
idx 10755: aplica_a Obligacion_debera_tenerse_en_cuenta_lo_dispuesto_en_el_punto_4_2__cap_2_12_15_39fe90 -> Sujeto_rol_alcance_capmin: sin mención
idx 10767: aplica_a Obligacion_debera_tenerse_en_cuenta_lo_dispuesto_en_la_seccion_5__cap_2_12_9_3_efc1ec -> Sujeto_rol_alcance_capmin: sin mención
idx 10774: aplica_a Obligacion_debera_verificar_previamente_que_se_cumplen_la_totalidad_de_requisitos_estableci_d59155 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10776: aplica_a Obligacion_debera_verificar_previamente_que_se_cumplen_la_totalidad_de_requisitos_estableci_faf36a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10778: aplica_a Obligacion_debera_verificar_que_la_documentacion_comercial_resulte_consistente_con_los_regi_f3ff38 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10780: aplica_a Obligacion_deberan_adoptarse_los_recaudos_de_seguridad_necesarios_para_evitar_el_uso_indebi_16e692 -> Sujeto_banco: sin mención
idx 10782: aplica_a Obligacion_deberan_aplicar_los_metodos_y_ponderadores_que_son_de_aplicacion_cuando_las_oper_a6b936 -> Sujeto_rol_alcance_capmin: sin mención
idx 10784: aplica_a Obligacion_deberan_clasificar_a_los_deudores_de_los_creditos_fideicomitidos_de_acuerdo_con__f48c36 -> Sujeto_fiduciario_de_fideicomiso_financiero: sin mención
idx 10787: aplica_a Obligacion_deberan_comunicarse_a_los_usuarios_las_recomendaciones_y_recaudos_para_el_uso_de_77b27b -> Sujeto_banco: sin mención
idx 10789: aplica_a Obligacion_deberan_comunicarse_a_los_usuarios_recomendaciones_sobre_cambiar_el_codigo_de_id_46e3c3 -> Sujeto_banco: sin mención
idx 10792: aplica_a Obligacion_deberan_consignarse_como_minimo_los_siguientes_datos_numero_de_consulta_o_reclam_bed2c5 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10795: aplica_a Obligacion_deberan_consignarse_el_nombre_y_apellido_completo_del_no_residente_tal_cual_cons_e75976 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10797: aplica_a Obligacion_deberan_contar_con_una_estrategia_de_negociacion_claramente_documentada_respecto_3c5dd7 -> Sujeto_rol_alcance_capmin: sin mención
idx 10799: aplica_a Obligacion_deberan_convertir_los_compromisos_pasibles_de_ser_cancelados_discrecional_y_unil_3ce962 -> Sujeto_entidad_financiera: sin mención
idx 10802: aplica_a Obligacion_deberan_cumplimentarse_los_requisitos_establecidos_para_las_personas_humanas_res_1c08e3 -> Sujeto_banco: sin mención
idx 10816: aplica_a Obligacion_deberan_detallarse_los_procedimientos_correspondientes_a_las_situaciones_de_disc_6fbc0c -> Sujeto_banco: sin mención
idx 10818: aplica_a Obligacion_deberan_dirigir_una_nota_a_la_gerencia_de_cuentas_corrientes_del_bcra_suscripta__4f71e5 -> Sujeto_rol_alcance_pagjub: sin mención
idx 10828: aplica_a Obligacion_deberan_efectuarse_mediante_nota_dirigida_a_la_gerencia_principal_de_seguridad_d_82d0f4 -> Sujeto_banco: sin mención
idx 10830: aplica_a Obligacion_deberan_estar_identificados_con_la_leyenda_boton_de_arrepentimiento_o_boton_de_b_6235f0 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10832: aplica_a Obligacion_deberan_evitar_la_condescendencia_masculina_conocida_como_mansplaining__pro_2_4_cb7c2f -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10835: aplica_a Obligacion_deberan_evitar_reproducir_mensajes_homofobicos_lesbofobicos_y_transfobicos__pro__ddf998 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10838: aplica_a Obligacion_deberan_evitar_utilizar_la_imagen_de_la_mujer_como_mero_objeto_desvinculado_del__326bf9 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10841: aplica_a Obligacion_deberan_existir_respecto_de_las_garantias_otorgadas_localmente_contragarantias_e_0cfee9 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10843: aplica_a Obligacion_deberan_facilitar_su_atencion_en_las_casas_operativas_por_medio_de_su_personal_c_b9861b -> Sujeto_entidad_financiera: sin mención
idx 10844: aplica_a Obligacion_deberan_facilitar_su_atencion_en_las_casas_operativas_por_medio_de_su_personal_c_b9861b -> Sujeto_psi_billetera_digital: sin mención
idx 10845: aplica_a Obligacion_deberan_facilitar_su_atencion_en_las_casas_operativas_por_medio_de_su_personal_c_b9861b -> Sujeto_pspcp: sin mención
idx 10848: aplica_a Obligacion_deberan_informar_las_modificaciones_de_los_cargos__pro_2_5_dbe7be -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 10849: aplica_a Obligacion_deberan_informar_las_modificaciones_de_los_cargos__pro_2_5_dbe7be -> Sujeto_entidad_financiera: sin mención
idx 10850: aplica_a Obligacion_deberan_informar_las_modificaciones_de_los_cargos__pro_2_5_dbe7be -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 10851: aplica_a Obligacion_deberan_informar_las_modificaciones_de_los_cargos__pro_2_5_dbe7be -> Sujeto_pspcp: sin mención
idx 10854: aplica_a Obligacion_deberan_informar_los_flujos_asignados_a_todas_las_bandas_o_puntos_medios_para_ca_83305c -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10862: aplica_a Obligacion_deberan_informarse_las_partidas_que_registren_importes_considerando_los_atributo_b25ab1 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10870: aplica_a Obligacion_deberan_informarse_los_cambios_negativos_en_la_clasificacion_a_los_deudores_que__97984f -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10872: aplica_a Obligacion_deberan_ingresarse_los_cargos_resultantes_dentro_del_termino_de_10_dias_habiles__59a8dc -> Sujeto_rol_alcance_capmin: sin mención
idx 10874: aplica_a Obligacion_deberan_mantenerse_a_disposicion_de_la_sefyc_los_importes_correspondientes_a_los_1ce3ed -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10876: aplica_a Obligacion_deberan_mantenerse_actualizados_e_informarse_por_medio_del_regimen_informativo_e_41ccf1 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10878: aplica_a Obligacion_deberan_observar_las_disposiciones_de_las_normas_sobre_proteccion_de_los_usuario_59c646 -> Sujeto_banco: sin mención
idx 10881: aplica_a Obligacion_deberan_observar_para_garantizar_su_capacidad_de_absorcion_de_perdidas__cap_8_3__e93321 -> Sujeto_rol_alcance_capmin: sin mención
idx 10884: aplica_a Obligacion_deberan_prever_que_en_caso_de_quiebra_de_la_entidad_y_una_vez_satisfecha_la_tota_e88f02 -> Sujeto_rol_alcance_capmin: sin mención
idx 10886: aplica_a Obligacion_deberan_proporcionar_a_la_sefyc_toda_la_informacion_que_esta_les_requiera_para_c_dcd59a -> Sujeto_fiduciario_de_fideicomiso_financiero: sin mención
idx 10888: aplica_a Obligacion_deberan_proporcionarse_en_terminos_claros_y_consistentes_las_politicas_y_procedi_591fb8 -> Sujeto_rol_alcance_capmin: sin mención
idx 10890: aplica_a Obligacion_deberan_publicar_en_su_sitio_de_internet_institucional_los_modelos_de_contrato_d_8af265 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10893: aplica_a Obligacion_deberan_recibir_atencion_prioritaria_en_las_casas_operativas_y_quedar_eximidos_d_a47cee -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 10895: aplica_a Obligacion_deberan_registrar_los_siguientes_datos_cuando_abran_cuentas_corrientes_bancarias_b65e1c -> Sujeto_banco: sin mención
idx 10897: aplica_a Obligacion_deberan_reportarse_las_desviaciones_al_nivel_gerencial_pertinente_y_cuando_fuere_118824 -> Sujeto_entidad_financiera: sin mención
idx 10899: aplica_a Obligacion_deberan_ser_liquidadas_en_el_mercado_de_cambios_al_momento_de_su_desembolso__ext_98879b -> Sujeto_entidad_financiera: sin mención
idx 10901: aplica_a Obligacion_deberan_ser_liquidadas_en_el_mercado_de_cambios_como_requisito_para_el_posterior_44ec02 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10906: aplica_a Obligacion_deberan_solicitar_a_sus_clientes_titulares_de_cuentas_declarables_que_sean_perso_49185d -> Sujeto_banco: sin mención
idx 10914: aplica_a Obligacion_deberan_solicitar_a_sus_clientes_titulares_de_cuentas_declarables_que_sean_perso_8bed76 -> Sujeto_banco: sin mención
idx 10922: aplica_a Obligacion_deberan_solicitar_a_sus_clientes_titulares_de_cuentas_declarables_que_sean_perso_956444 -> Sujeto_banco: sin mención
idx 10924: aplica_a Obligacion_deberan_tenerse_en_cuenta_las_instrucciones_de_computo_del_presente_punto_y_los__2ee01b -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 10952: aplica_a Obligacion_debiendo_como_minimo_informar_respecto_de_ellos_nombres_y_apellidos_completos_o__b02261 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10955: aplica_a Obligacion_debiendo_constituirse_domicilio_especial_obligatoriamente_en_la_republica_argent_6b6b08 -> Sujeto_banco: sin mención
idx 10957: aplica_a Obligacion_debiendo_constituirse_este_ultimo_domicilio_especial_en_la_republica_argentina_e_5732f6 -> Sujeto_banco: sin mención
idx 10963: aplica_a Obligacion_debiendo_en_todos_los_casos_documentarse_el_analisis_efectuado__cla_3_2_ee6d71 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 10966: aplica_a Obligacion_debiendo_los_pedidos_ser_canalizados_por_una_entidad_autorizada_a_realizar_este__3df8fe -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10968: aplica_a Obligacion_debiendo_prestar_especial_atencion_entre_otros_aspectos_a_que_el_movimiento_que__402aad -> Sujeto_banco: sin mención
idx 10970: aplica_a Obligacion_debiendo_tomar_por_defecto_como_cuenta_primaria_en_estos_casos_a_la_cuenta_en_mo_98334d -> Sujeto_entidad_financiera: sin mención
idx 10972: aplica_a Obligacion_debiendose_identificar_el_numero_de_la_oficializacion_del_despacho_de_importacio_ff8ee4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 10974: aplica_a Obligacion_debiendose_prever_la_emision_de_las_pertinentes_constancias_con_los_datos_esenci_313f28 -> Sujeto_banco: sin mención
idx 10977: aplica_a Obligacion_debitar_de_la_cuenta_corriente_de_la_entidad_participante_el_importe_de_las_orde_273704 -> Sujeto_rol_alcance_pagjub: sin mención
idx 10979: aplica_a Obligacion_debitar_de_la_cuenta_corriente_de_la_entidad_participante_las_penalidades_previs_6b1c45 -> Sujeto_rol_alcance_pagjub: sin mención
idx 10985: aplica_a Obligacion_debitar_de_la_cuenta_corriente_de_la_entidad_participante_las_penalidades_previs_f9f5a7 -> Sujeto_rol_alcance_pagjub: sin mención
idx 10990: aplica_a Obligacion_debitara_de_la_cuenta_corriente_de_la_entidad_participante_la_totalidad_del_impo_d2b9f8 -> Sujeto_rol_alcance_pagjub: sin mención
idx 10992: aplica_a Obligacion_debitara_de_la_cuenta_transitoria_habilitada_al_efecto_los_importes_de_ordenes_d_3049b8 -> Sujeto_rol_alcance_pagjub: sin mención
idx 10996: aplica_a Obligacion_defina_y_apruebe_con_claridad_las_de_la_alta_gerencia__lingob_2_4_1_d848e9 -> Sujeto_entidad_financiera: sin mención
idx 10998: aplica_a Obligacion_definir_los_riesgos_a_asumir_por_la_entidad__lingob_1_2_3_c01784 -> Sujeto_entidad_financiera: sin mención
idx 11000: aplica_a Obligacion_definir_politicas_procedimientos_y_estrategias_adecuados_para_aprobar_estructura_429e92 -> Sujeto_entidad_financiera: sin mención
idx 11002: aplica_a Obligacion_definir_y_entender_el_proposito_de_estas_actividades_y_comprobar_que_se_cumple_e_66b6ef -> Sujeto_entidad_financiera: sin mención
idx 11004: aplica_a Obligacion_dejando_libre_para_la_utilizacion_por_la_entidad_girada_los_sectores_destinados__9c46c1 -> Sujeto_entidad_depositaria: sin mención
idx 11006: aplica_a Obligacion_dejar_constancia_de_la_identificacion_del_acreedor_en_el_boleto_de_compra__ext_7_225bf5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11008: aplica_a Obligacion_dejar_constancia_en_el_respectivo_legajo_de_la_comunicacion_del_rechazo__ctacte__ebedd2 -> Sujeto_banco: sin mención
idx 11013: aplica_a Obligacion_dentro_de_cada_serie_la_numeracion_sera_correlativa__ctacte_5_5_5_2b3e4d -> Sujeto_banco: sin mención
idx 11016: aplica_a Obligacion_dentro_de_los_10_dias_corridos_de_haber_cumplimentado_los_requisitos_establecido_0bf5aa -> Sujeto_banco: sin mención
idx 11018: aplica_a Obligacion_denunciar_de_inmediato_esta_situacion_al_banco_que_la_otorgo__ctacte_12_1_2_10_f09fea -> Sujeto_banco: sin mención
idx 11020: aplica_a Obligacion_desarrollar_procedimientos_de_analisis_de_cartera_que_aseguren_un_analisis_adecu_3d6cea -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 11022: aplica_a Obligacion_desarrollar_procesos_que_identifiquen_evaluen_monitoreen_controlen_y_mitiguen_lo_8b23bc -> Sujeto_entidad_financiera: sin mención
idx 11024: aplica_a Obligacion_describir_el_activo_comprado_o_vendido_a_futuro_ej_tasa_de_interes_badlar_privad_81e569 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 11026: aplica_a Obligacion_describir_el_activo_subyacente_del_swap_conforme_a_los_ejemplos_especificados_ta_6189ee -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 11028: aplica_a Obligacion_descripcion_de_controles_cruzados__ctacte_3_3_8_2_0d4266 -> Sujeto_banco: sin mención
idx 11030: aplica_a Obligacion_descripcion_de_la_politica_de_obtencion_de_copias_de_respaldo_backups__ctacte_3__8bb113 -> Sujeto_banco: sin mención
idx 11032: aplica_a Obligacion_descripcion_del_mecanismo_de_encripcion_utilizado_para_dar_confidencialidad_al_a_56c3cf -> Sujeto_banco: sin mención
idx 11034: aplica_a Obligacion_descripcion_del_procedimiento_adoptado_cuando_a_los_fines_de_la_actualizacion_de_59ae8f -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 11036: aplica_a Obligacion_descripcion_detallada_de_la_generacion_almacenamiento_y_acceso_a_los_registros_d_9265c3 -> Sujeto_banco: sin mención
idx 11038: aplica_a Obligacion_descripcion_detallada_del_procedimiento_de_administracion_del_inventario_fisico__7fe08d -> Sujeto_banco: sin mención
idx 11040: aplica_a Obligacion_desde_el_01_06_24_y_hasta_el_31_12_24_correspondera_que_tales_entidades_en_funci_4c2100 -> Sujeto_rol_alcance_capmin: sin mención
idx 11042: aplica_a Obligacion_desde_el_trigesimo_septimo_mes_la_exigencia_mensual_se_calculara_de_acuerdo_con__6c1b5e -> Sujeto_rol_alcance_capmin: sin mención
idx 11045: aplica_a Obligacion_designar_las_personas_que_tendran_a_su_cargo_la_correcta_aplicacion_de_la_metodo_3ca677 -> Sujeto_rol_alcance_capmin: sin mención
idx 11047: aplica_a Obligacion_despues_de_calcular_el_total_de_los_activos_ponderados_por_riesgo_del_fondo_apr__339c1d -> Sujeto_rol_alcance_capmin: sin mención
idx 11049: aplica_a Obligacion_detalle_de_las_causales_y_o_situaciones_que_pueden_motivar_el_cierre_de_la_cuent_1127e9 -> Sujeto_banco: sin mención
idx 11051: aplica_a Obligacion_detalle_del_os_cheque_s_numero_e_importe__ctacte_10_2_2_1_bb88ad -> Sujeto_banco: sin mención
idx 11053: aplica_a Obligacion_devolver_a_la_entidad_todos_los_cheques_en_blanco_que_conserve_al_momento_de_sol_9c2f05 -> Sujeto_banco: sin mención
idx 11057: aplica_a Obligacion_diagramas_en_bloque__ctacte_3_3_8_2_dec363 -> Sujeto_banco: sin mención
idx 11059: aplica_a Obligacion_dicha_conformidad_estara_referida_con_opinion_fundada_en_todos_los_casos_tanto_a_17ad30 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 11061: aplica_a Obligacion_dicha_nota_que_debera_confeccionarse_respetando_el_contenido_y_la_estructura_que_040085 -> Sujeto_rol_alcance_pagjub: sin mención
idx 11068: aplica_a Obligacion_dicha_revision_que_podra_estar_a_cargo_de_la_auditoria_interna_de_la_entidad_deb_20c7c2 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 11072: aplica_a Obligacion_dichas_disposiciones_tambien_se_aplicaran_en_las_sucursales_en_el_exterior_en_la_9f6b6f -> Sujeto_entidad_financiera: sin mención
idx 11074: aplica_a Obligacion_dichas_evaluaciones_deberan_basarse_en_metodologias_que_combinen_enfoques_cualit_b068ef -> Sujeto_ecai: sin mención
idx 11076: aplica_a Obligacion_dicho_legajo_debera_contar_con_informacion_acerca_de_los_margenes_crediticios_di_79fcb8 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 11078: aplica_a Obligacion_dicho_manual_debera_ser_aprobado_por_el_directorio_o_autoridad_equivalente_de_la_590b7d -> Sujeto_banco: sin mención
idx 11080: aplica_a Obligacion_dichos_importes_se_consignaran_una_vez_computadas_las_facilidades_otorgadas_por__fd808b -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 11082: aplica_a Obligacion_dirigir_el_proceso_de_analisis_de_las_causas_generadoras_de_los_eventos_de_recla_c5c63d -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11105: aplica_a Obligacion_divulgacion_de_informacion_sobre_estructura_organizacional_organigrama_general_l_5743d0 -> Sujeto_entidad_financiera: sin mención
idx 11109: aplica_a Obligacion_domicilio_registrado_en_el_banco_girado__ctacte_10_2_2_1_ef2c4a -> Sujeto_banco: sin mención
idx 11111: aplica_a Obligacion_efectuada_la_registracion_se_devolvera_el_documento_con_la_constancia_que_acredi_648160 -> Sujeto_banco: sin mención
idx 11113: aplica_a Obligacion_efectuar_el_seguimiento_de_la_ejecucion_del_proyecto_y_su_financiacion__ext_7_9__f04d3b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11115: aplica_a Obligacion_efectuar_el_seguimiento_de_las_garantias_constituidas_y_de_las_cuentas_especiale_9f21f3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11118: aplica_a Obligacion_ejerza_la_debida_diligencia_en_el_proceso_de_contratacion_y_seguimiento_de_la_la_fc09d5 -> Sujeto_entidad_financiera: sin mención
idx 11120: aplica_a Obligacion_el_acceso_a_la_citada_informacion_debera_ser_facil_y_directo_desde_la_pagina_de__82e80b -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11124: aplica_a Obligacion_el_acceso_al_mercado_de_cambios_para_la_formacion_de_activos_externos_requerira__79cfea -> Sujeto_bcra: sin mención
idx 11127: aplica_a Obligacion_el_acceso_al_mercado_de_cambios_para_la_repatriacion_de_inversiones_de_no_reside_51094b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11129: aplica_a Obligacion_el_acceso_al_mercado_de_cambios_para_la_repatriacion_de_inversiones_de_no_reside_87f918 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11133: aplica_a Obligacion_el_acceso_al_mercado_de_cambios_para_operatoria_con_derivados_requerira_la_confo_b38c11 -> Sujeto_bcra: sin mención
idx 11141: aplica_a Obligacion_el_acceso_al_mercado_de_cambios_tiene_lugar_a_partir_de_la_fecha_de_vencimiento__7c39cf -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11144: aplica_a Obligacion_el_acceso_al_mercado_local_de_cambios_para_cancelar_anticipos_u_otras_financiaci_27a670 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11146: aplica_a Obligacion_el_activo_recibido_en_garantia_debera_contar_con_una_valuacion_a_precios_de_merc_00f61a -> Sujeto_rol_alcance_capmin: sin mención
idx 11149: aplica_a Obligacion_el_acuerdo_con_la_entidad_financiera_debera_concertarse_dentro_de_los_90_o_180_d_a1228d -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 11151: aplica_a Obligacion_el_aforo_debera_incrementarse_proporcionalmente_utilizando_la_formula_de_la_raiz_2f57c6 -> Sujeto_rol_alcance_capmin: sin mención
idx 11153: aplica_a Obligacion_el_alcance_y_adecuacion_de_la_cobertura_deberan_ser_explicados_y_divulgados_a_lo_d9cf00 -> Sujeto_rol_alcance_capmin: sin mención
idx 11155: aplica_a Obligacion_el_analisis_de_estas_condiciones_debera_ser_llevado_a_cabo_por_el_originante_o_f_d1211d -> Sujeto_rol_alcance_capmin: sin mención
idx 11157: aplica_a Obligacion_el_area_de_supervision_y_seguimiento_de_la_sefyc_podra_requerir_que_operaciones__4e13ea -> Sujeto_sefyc: sin mención
idx 11160: aplica_a Obligacion_el_aviso_del_cierre_de_la_cuenta_debera_incluir_el_motivo_que_origina_el_cierre__0fce6c -> Sujeto_banco: sin mención
idx 11163: aplica_a Obligacion_el_banco_girado_debera_entregar_al_librador_o_al_portador_del_cheque_librado_en__f711ec -> Sujeto_banco: sin mención
idx 11166: aplica_a Obligacion_el_bcra_en_el_mismo_dia_de_la_aceptacion_procedera_a__pagjub_2_8_3_ed3db2 -> Sujeto_bcra: sin mención
idx 11168: aplica_a Obligacion_el_bcra_en_el_mismo_dia_de_la_aceptacion_procedera_a__pagjub_2_8_4_89a703 -> Sujeto_bcra: sin mención
idx 11170: aplica_a Obligacion_el_bcra_en_el_mismo_dia_de_la_aceptacion_procedera_a_acciones_de_liquidacion_de__296624 -> Sujeto_bcra: sin mención
idx 11172: aplica_a Obligacion_el_bcra_procedera_a_acreditar_en_la_cuenta_corriente_de_la_entidad_participante__24eb8a -> Sujeto_rol_alcance_pagjub: sin mención
idx 11174: aplica_a Obligacion_el_bcra_procedera_a_acreditar_en_la_cuenta_corriente_de_la_entidad_participante__2dcceb -> Sujeto_rol_alcance_pagjub: sin mención
idx 11176: aplica_a Obligacion_el_bcra_procedera_a_acreditar_en_la_cuenta_corriente_de_la_entidad_participante__991cc9 -> Sujeto_rol_alcance_pagjub: sin mención
idx 11178: aplica_a Obligacion_el_bcra_procedera_a_debitar_de_la_cuenta_corriente_de_la_entidad_participante_el_060c20 -> Sujeto_rol_alcance_pagjub: sin mención
idx 11182: aplica_a Obligacion_el_bcra_procedera_a_debitar_de_la_cuenta_corriente_de_la_entidad_participante_el_d49831 -> Sujeto_rol_alcance_pagjub: sin mención
idx 11185: aplica_a Obligacion_el_bcra_procesara_la_informacion_respectiva_y_pondra_a_disposicion_de_la_entidad_3c4177 -> Sujeto_bcra: sin mención
idx 11187: aplica_a Obligacion_el_bcra_tomara_conocimiento_de_la_utilizacion_de_esta_certificacion_a_traves_del_b7a3f4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11189: aplica_a Obligacion_el_bcra_utilizara_la_informacion_recibida_a_efectos_de_analizar_las_practicas_y__a8e107 -> Sujeto_bcra: sin mención
idx 11192: aplica_a Obligacion_el_beneficiario_debera_nominar_una_unica_entidad_financiera_local_que_sera_la_re_a42bfd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11194: aplica_a Obligacion_el_boleto_de_compra_se_confeccionara_con_un_codigo_de_concepto_que_identifique_q_018fae -> Sujeto_entidad_financiera: sin mención
idx 11196: aplica_a Obligacion_el_boleto_de_compra_se_confeccionara_por_un_codigo_de_concepto_que_identifique_q_4f0295 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11206: aplica_a Obligacion_el_boleto_de_venta_debera_efectuarse_a_nombre_de_la_propia_entidad_en_calidad_de_f3e1b8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11213: aplica_a Obligacion_el_boleto_de_venta_se_confeccionara_con_el_codigo_de_concepto_de_pago_diferido_d_2ec78c -> Sujeto_entidad_financiera: sin mención
idx 11215: aplica_a Obligacion_el_boleto_de_venta_se_confeccionara_con_el_codigo_de_concepto_que_refleje_el_pag_924c1c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11217: aplica_a Obligacion_el_boleto_de_venta_se_confeccionara_con_el_codigo_de_concepto_que_refleje_el_tip_6faf81 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11220: aplica_a Obligacion_el_boleto_debera_ser_confeccionado_a_nombre_de_la_entidad_que_cursa_la_operacion_e3843b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11228: aplica_a Obligacion_el_calculo_de_k_debera_reflejar_los_efectos_de_cualquier_cobertura_del_riesgo_de_6167f1 -> Sujeto_rol_alcance_capmin: sin mención
idx 11230: aplica_a Obligacion_el_calculo_de_la_exigencia_de_capital_por_riesgo_de_tipo_de_cambio_requiere_cuan_bc1cce -> Sujeto_rol_alcance_capmin: sin mención
idx 11232: aplica_a Obligacion_el_calendario_de_pagos_de_los_incentivos_sea_sensible_al_horizonte_temporal_de_l_18fa27 -> Sujeto_entidad_financiera: sin mención
idx 11234: aplica_a Obligacion_el_cambio_de_entidad_debera_ser_notificado_al_bcra__ext_3_17_5_570366 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11237: aplica_a Obligacion_el_cierre_de_las_cuentas_y_o_la_cancelacion_de_las_autorizaciones_debera_efectua_85ab1e -> Sujeto_banco: sin mención
idx 11241: aplica_a Obligacion_el_cierre_del_incumplido_debera_realizarse_dentro_de_los_5_cinco_dias_habiles_de_e0cd6d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11265: aplica_a Obligacion_el_cliente_debera_comprometerse_a_presentar_la_documentacion_de_la_capitalizacio_68bdc8 -> Sujeto_cliente: sin mención
idx 11268: aplica_a Obligacion_el_cliente_debera_haber_realizado_una_revision_legal_adecuada_y_llevar_a_cabo_es_4f5faf -> Sujeto_cliente: sin mención
idx 11270: aplica_a Obligacion_el_cliente_debera_presentar_la_documentacion_que_avale_la_capitalizacion_definit_19ab8b -> Sujeto_cliente: sin mención
idx 11273: aplica_a Obligacion_el_cliente_debera_presentar_la_documentacion_que_avale_la_capitalizacion_definit_8307d9 -> Sujeto_vpu_rigi: sin mención
idx 11279: aplica_a Obligacion_el_cliente_haya_registrado_la_totalidad_de_sus_deudas_por_importaciones_de_biene_12d0f8 -> Sujeto_mipyme: sin mención
idx 11282: aplica_a Obligacion_el_cliente_que_no_sea_persona_humana_residente_debe_declarar_bajo_juramento_el_d_f5690d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11284: aplica_a Obligacion_el_cliente_que_realiza_la_operacion_de_cambio_debera_ser_identificado_por_la_ent_47a757 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11289: aplica_a Obligacion_el_comite_de_incentivos_al_personal_debe_emplear_su_criterio_para_calcular_el_aj_2fc031 -> Sujeto_entidad_financiera: sin mención
idx 11291: aplica_a Obligacion_el_comite_de_incentivos_al_personal_esta_encargado_de_vigilar_que_el_sistema_de__038510 -> Sujeto_entidad_financiera: sin mención
idx 11294: aplica_a Obligacion_el_comprador_de_la_proteccion_podra_reconocer_la_proteccion_de_un_tramo_de_su_po_610394 -> Sujeto_rol_alcance_capmin: sin mención
idx 11306: aplica_a Obligacion_el_computo_de_activos_y_pasivos_se_realizara_a_base_del_promedio_mensual_de_sald_320c7f -> Sujeto_entidad_financiera: sin mención
idx 11309: aplica_a Obligacion_el_computo_se_hara_en_base_a_una_distribucion_entre_las_distintas_categorias_en__4c94ea -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11311: aplica_a Obligacion_el_contrato_de_cesion_de_los_creditos_debera_contener_clausulas_por_las_cuales_e_5ecc89 -> Sujeto_rol_alcance_capmin: sin mención
idx 11339: aplica_a Obligacion_el_contrato_debe_contener_clausula_de_revocacion_indicando_que_el_usuario_de_ser_a402ad -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11341: aplica_a Obligacion_el_contrato_debe_contener_el_derecho_de_solicitar_la_apertura_de_la_caja_de_ahor_8f66cc -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11343: aplica_a Obligacion_el_contrato_debe_contener_el_derecho_del_usuario_de_efectuar_en_cualquier_moment_2a57d7 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11355: aplica_a Obligacion_el_contrato_debe_contener_el_derecho_del_usuario_de_realizar_operaciones_por_ven_d1e59b -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11368: aplica_a Obligacion_el_contrato_debe_contener_la_leyenda_usted_puede_consultar_el_regimen_de_transpa_0fdc7f -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11370: aplica_a Obligacion_el_contravalor_de_la_exportacion_de_bienes_y_servicios_debera_ingresarse_al_pais_3f3430 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11374: aplica_a Obligacion_el_contravalor_percibido_por_la_enajenacion_de_activos_no_financieros_no_produci_336dcd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11377: aplica_a Obligacion_el_correspondiente_registro_de_un_ingreso_sera_responsabilidad_de_la_entidad_int_832de6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11380: aplica_a Obligacion_el_cr_se_calculara_a_nivel_de_conjunto_de_neteo__cap_4_2_1_1_22ae05 -> Sujeto_rol_alcance_capmin: sin mención
idx 11449: aplica_a Obligacion_el_deudor_demuestre_el_ingreso_y_liquidacion_de_divisas_en_el_mercado_de_cambios_6eec1d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11451: aplica_a Obligacion_el_deudor_demuestre_el_ingreso_y_liquidacion_de_divisas_en_el_mercado_de_cambios_fb3733 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11453: aplica_a Obligacion_el_deudor_que_encontrandose_clasificado_en_esta_categoria_haya_refinanciado_su_d_1fe0b4 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 11455: aplica_a Obligacion_el_deudor_que_encontrandose_clasificado_en_esta_categoria_haya_refinanciado_su_d_53bbdc -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 11458: aplica_a Obligacion_el_directivo_responsable_de_proteccion_de_los_usuarios_de_servicios_financieros__39c18a -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11460: aplica_a Obligacion_el_directivo_responsable_de_proteccion_de_los_usuarios_de_servicios_financieros__97eee1 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 11461: aplica_a Obligacion_el_directivo_responsable_de_proteccion_de_los_usuarios_de_servicios_financieros__97eee1 -> Sujeto_entidad_financiera: sin mención
idx 11462: aplica_a Obligacion_el_directivo_responsable_de_proteccion_de_los_usuarios_de_servicios_financieros__97eee1 -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 11464: aplica_a Obligacion_el_directorio_a_traves_de_la_intervencion_del_comite_de_auditoria_tiene_la_respo_58aaa0 -> Sujeto_entidad_financiera: sin mención
idx 11466: aplica_a Obligacion_el_directorio_aprueba_los_objetivos_estrategicos_establecidos_segun_el_objeto_so_29051e -> Sujeto_entidad_financiera: sin mención
idx 11468: aplica_a Obligacion_el_directorio_comunica_los_objetivos_estrategicos_y_los_valores_societarios_a_to_af87e3 -> Sujeto_entidad_financiera: sin mención
idx 11470: aplica_a Obligacion_el_directorio_de_la_entidad_financiera_sera_responsable_de__lingob_1_3_085e2c -> Sujeto_entidad_financiera: sin mención
idx 11472: aplica_a Obligacion_el_directorio_debera_adoptar_medidas_y_asegurar_que_los_riesgos_de_estas_activid_8d4629 -> Sujeto_entidad_financiera: sin mención
idx 11474: aplica_a Obligacion_el_directorio_debera_asegurar_que_la_alta_gerencia_de_cumplimiento_a_las_politic_92dfa4 -> Sujeto_entidad_financiera: sin mención
idx 11476: aplica_a Obligacion_el_directorio_debera_asegurarse_de_que_el_profesional_que_lleva_a_cabo_la_funcio_793192 -> Sujeto_entidad_financiera: sin mención
idx 11478: aplica_a Obligacion_el_directorio_debera_establecer_politicas_y_limites_para_el_uso_de_estructuras_c_c58b3b -> Sujeto_entidad_financiera: sin mención
idx 11480: aplica_a Obligacion_el_directorio_debera_establecer_politicas_y_limites_para_operar_con_determinadas_847a14 -> Sujeto_entidad_financiera: sin mención
idx 11482: aplica_a Obligacion_el_directorio_establecera_y_hara_cumplir_lineas_claras_de_responsabilidad_en_tod_7b9d14 -> Sujeto_entidad_financiera: sin mención
idx 11484: aplica_a Obligacion_el_directorio_o_autoridad_equivalente_de_los_sujetos_obligados_debera_nombrar_a__eb4fc3 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11486: aplica_a Obligacion_el_directorio_o_autoridad_equivalente_debera_evaluar_los_reportes_que_le_eleve_e_ed5596 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11492: aplica_a Obligacion_el_directorio_prestara_especial_atencion_al_diseno_controles_e_implementacion_de_38dcb9 -> Sujeto_entidad_financiera: sin mención
idx 11494: aplica_a Obligacion_el_directorio_se_asegurara_de_que_la_alta_gerencia_implemente_procedimientos_par_7ca71d -> Sujeto_entidad_financiera: sin mención
idx 11497: aplica_a Obligacion_el_directorio_supervisa_los_objetivos_estrategicos_y_los_valores_societarios__li_58e12e -> Sujeto_entidad_financiera: sin mención
idx 11499: aplica_a Obligacion_el_directorio_supervisara_la_gestion_de_la_alta_gerencia_y_su_consistencia_con_l_be3b9f -> Sujeto_entidad_financiera: sin mención
idx 11501: aplica_a Obligacion_el_directorio_y_cada_uno_de_sus_miembros_segun_corresponda_deberan_velar_por_la__9c4ae1 -> Sujeto_entidad_financiera: sin mención
idx 11503: aplica_a Obligacion_el_directorio_y_la_alta_gerencia_deberan_entender_en_la_estructura_operativa_de__b94fc7 -> Sujeto_entidad_financiera: sin mención
idx 11507: aplica_a Obligacion_el_directorio_y_la_alta_gerencia_se_aseguraran_de_que_se_apliquen_politicas_y_pr_b3fb67 -> Sujeto_entidad_financiera: sin mención
idx 11512: aplica_a Obligacion_el_ejercicio_de_esa_opcion_debera_ser_comunicado_a_la_sefyc_con_un_preaviso_de_3_e723f1 -> Sujeto_rol_alcance_capmin: sin mención
idx 11514: aplica_a Obligacion_el_endoso_debera_ser_puro_y_simple_y_contendra_la_firma_del_endosante_o_sera_efe_eb6581 -> Sujeto_banco: sin mención
idx 11520: aplica_a Obligacion_el_excedente_de_pnb_atribuible_a_los_inversores_minoritarios_resultara_de_multip_4f634b -> Sujeto_rol_alcance_capmin: sin mención
idx 11523: aplica_a Obligacion_el_excedente_de_pnb_de_la_subsidiaria_se_calcula_como_el_pnb_de_la_subsidiaria_n_e9078c -> Sujeto_rol_alcance_capmin: sin mención
idx 11527: aplica_a Obligacion_el_excedente_de_rpc_de_la_subsidiaria_se_calcula_como_la_rpc_de_la_subsidiaria_n_853a2a -> Sujeto_rol_alcance_capmin: sin mención
idx 11530: aplica_a Obligacion_el_exportador_debe_presentar_una_declaracion_jurada_en_la_cual_identifique_el_do_4fe6b2 -> Sujeto_exportador: sin mención
idx 11532: aplica_a Obligacion_el_exportador_debera_demostrar_en_forma_fehaciente_su_gestion_de_cobro_a_traves__b31905 -> Sujeto_exportador: sin mención
idx 11536: aplica_a Obligacion_el_exportador_debera_nominar_una_unica_entidad_financiera_local_que_sera_la_resp_aaacc0 -> Sujeto_exportador: sin mención
idx 11543: aplica_a Obligacion_el_exportador_demuestre_su_gestion_de_cobro_a_traves_de_los_reclamos_efectuados__bab7fa -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11571: aplica_a Obligacion_el_financiamiento_que_se_acuerde_y_los_vencimientos_que_se_establezcan_deberan_g_8fac12 -> Sujeto_entidad_financiera: sin mención
idx 11573: aplica_a Obligacion_el_girado_procedera_a_comunicar_el_rechazo_al_bcra_en_la_oportunidad_y_mediante__eddcdb -> Sujeto_banco: sin mención
idx 11575: aplica_a Obligacion_el_girado_procedera_a_comunicar_el_rechazo_al_librador_cuentacorrentista_mandata_84dd91 -> Sujeto_banco: sin mención
idx 11577: aplica_a Obligacion_el_girado_retendra_el_cartular_o_certificado_para_aplicarle_el_curso_normal_que__0d5a52 -> Sujeto_entidad_girada: sin mención
idx 11579: aplica_a Obligacion_el_grado_de_sofisticacion_de_las_evaluaciones_de_debida_diligencia_debera_ser_pr_53e7d0 -> Sujeto_rol_alcance_capmin: sin mención
idx 11581: aplica_a Obligacion_el_importador_debe_haber_demostrado_que_a_la_fecha_de_origen_de_la_financiacion__d7e093 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11583: aplica_a Obligacion_el_importe_de_estas_participaciones_teniendo_en_cuenta_el_tipo_de_instrumento_de_a653ee -> Sujeto_rol_alcance_capmin: sin mención
idx 11585: aplica_a Obligacion_el_importe_de_la_multa_generada_por_rechazo_de_echeq_en_dolares_estadounidenses__a8f29d -> Sujeto_banco: sin mención
idx 11588: aplica_a Obligacion_el_importe_de_las_multas_sera_debitado_por_las_entidades_bancarias_de_las_respec_fa303e -> Sujeto_banco: sin mención
idx 11590: aplica_a Obligacion_el_importe_que_se_reconocera_en_el_pnb_de_la_entidad_financiera_sera_el_importe__435165 -> Sujeto_rol_alcance_capmin: sin mención
idx 11593: aplica_a Obligacion_el_importe_que_se_reconocera_en_la_rpc_de_la_entidad_financiera_sera_el_importe__186513 -> Sujeto_rol_alcance_capmin: sin mención
idx 11596: aplica_a Obligacion_el_incumplimiento_se_considerara_firme_aplicandose_el_procedimiento_establecido__dd2f76 -> Sujeto_rol_alcance_capmin: sin mención
idx 11616: aplica_a Obligacion_el_ingreso_y_liquidacion_de_divisas_debera_concretarse_en_30_treinta_dias_corrid_9fded4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11619: aplica_a Obligacion_el_ingreso_y_liquidacion_de_las_divisas_por_el_mercado_de_cambios_debera_concret_3ffda8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11622: aplica_a Obligacion_el_ingreso_y_liquidacion_de_las_divisas_por_el_mercado_de_cambios_debera_concret_421c83 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11625: aplica_a Obligacion_el_instrumento_que_origina_la_participacion_minoritaria_debe_observar_todos_los__c2c605 -> Sujeto_rol_alcance_capmin: sin mención
idx 11629: aplica_a Obligacion_el_legajo_del_deudor_se_debera_llevar_en_el_lugar_de_radicacion_de_la_cuenta__cl_32aab5 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 11631: aplica_a Obligacion_el_librador_cuenta_con_un_plazo_maximo_de_2_dias_habiles_bancarios_para_regulari_d67556 -> Sujeto_banco: sin mención
idx 11633: aplica_a Obligacion_el_librador_debera_extender_en_cada_oportunidad_una_certificacion_en_la_que_cons_671e34 -> Sujeto_banco: sin mención
idx 11635: aplica_a Obligacion_el_manual_de_procedimiento_respectivo_debera_encontrarse_a_disposicion_del_bcra__6e8980 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11637: aplica_a Obligacion_el_manual_debera_estar_a_disposicion_permanente_de_la_superintendencia_de_entida_c203e1 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 11639: aplica_a Obligacion_el_margen_inicial_aportado_por_los_clientes_al_miembro_compensador_mitigara_su_e_76d3b9 -> Sujeto_miembro_compensador: sin mención
idx 11641: aplica_a Obligacion_el_miembro_compensador_considerara_su_exposicion_con_un_cliente_incluyendo_la_po_d9152a -> Sujeto_miembro_compensador: sin mención
idx 11643: aplica_a Obligacion_el_mismo_procedimiento_sera_de_aplicacion_para_toda_modificacion_que_se_realice__0b0794 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11645: aplica_a Obligacion_el_mismo_tratamiento_se_aplicara_a_todo_otro_instrumento_en_el_cual_el_riesgo_de_33b41b -> Sujeto_rol_alcance_capmin: sin mención
idx 11647: aplica_a Obligacion_el_monto_alcanzado_por_la_obligacion_de_ingreso_y_liquidacion_de_divisas_se_comp_baba6f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11652: aplica_a Obligacion_el_neto_del_equivalente_delta_de_estas_opciones_se_incorporara_a_la_exposicion_e_d589aa -> Sujeto_rol_alcance_capmin: sin mención
idx 11657: aplica_a Obligacion_el_objetivo_de_la_politica_de_transparencia_en_el_gobierno_societario_es_proveer_ac0d3b -> Sujeto_entidad_financiera: sin mención
idx 11662: aplica_a Obligacion_el_orden_de_prelacion_en_el_pago_de_todos_los_compromisos_debera_estar_clarament_6c4bfd -> Sujeto_rol_alcance_capmin: sin mención
idx 11664: aplica_a Obligacion_el_ordenante_debe_incluir_apellidos_y_nombres_completos_o_denominacion_social_se_4e468a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11666: aplica_a Obligacion_el_ordenante_debe_incluir_domicilio_o_numero_de_dni_o_numero_de_cuit_cuil_cdi_o__ed542e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11668: aplica_a Obligacion_el_originante_de_la_titulizacion_asi_como_el_acreedor_inicial_de_los_creditos_ti_8e03bd -> Sujeto_rol_alcance_capmin: sin mención
idx 11670: aplica_a Obligacion_el_originante_debera_demostrar_al_inversor_que_los_activos_transferidos_han_sido_9abb06 -> Sujeto_rol_alcance_capmin: sin mención
idx 11703: aplica_a Obligacion_el_originante_o_fiduciario_debera_poner_a_disposicion_de_los_inversores_tanto_an_7f1655 -> Sujeto_rol_alcance_capmin: sin mención
idx 11706: aplica_a Obligacion_el_otorgamiento_de_asistencia_financiera_a_residentes_en_el_exterior_solo_proced_d54304 -> Sujeto_entidad_financiera: sin mención
idx 11710: aplica_a Obligacion_el_pago_de_dividendos_cupones_se_efectuara_con_cargo_a_partidas_distribuibles_en_c9ce1c -> Sujeto_rol_alcance_capmin: sin mención
idx 11712: aplica_a Obligacion_el_pago_del_incentivo_economico_variable_se_realizara_con_acciones_de_la_entidad_f58878 -> Sujeto_entidad_financiera: sin mención
idx 11714: aplica_a Obligacion_el_patrimonio_neto_basico_pnb_debera_calcularse_como_el_importe_resultante_de_mu_5c86ad -> Sujeto_rol_alcance_capmin: sin mención
idx 11717: aplica_a Obligacion_el_pedido_de_conformidad_del_bcra_para_dar_por_regularizada_parte_o_el_total_de__b844d2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11719: aplica_a Obligacion_el_plazo_de_ingreso_y_liquidacion_de_divisas_se_contara_a_partir_de_la_fecha_de__9aafec -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11722: aplica_a Obligacion_el_plazo_de_vencimiento_de_la_exposicion_subyacente_se_calculara_como_el_mayor_p_ae4274 -> Sujeto_rol_alcance_capmin: sin mención
idx 11726: aplica_a Obligacion_el_ponderador_de_riesgo_aplicado_a_los_activos_en_garantia_aportados_por_la_enti_625d30 -> Sujeto_rol_alcance_capmin: sin mención
idx 11728: aplica_a Obligacion_el_ponderador_de_riesgo_correspondiente_a_la_ccp_se_aplicara_a_los_activos_o_las_0c86bb -> Sujeto_rol_alcance_capmin: sin mención
idx 11730: aplica_a Obligacion_el_ponderador_de_riesgo_de_los_instrumentos_a_tasa_variable_dependera_de_que_el__53998c -> Sujeto_rol_alcance_capmin: sin mención
idx 11740: aplica_a Obligacion_el_presente_requerimiento_debera_ser_cumplido_por_todas_las_entidades_financiera_74af35 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 11742: aplica_a Obligacion_el_promedio_de_las_exigencias_por_riesgo_de_credito_se_calculara_en_esta_institu_dba987 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 11744: aplica_a Obligacion_el_proveedor_de_proteccion_debera_calcular_su_exigencia_de_capital_como_si_mantu_85b993 -> Sujeto_rol_alcance_capmin: sin mención
idx 11754: aplica_a Obligacion_el_que_origine_o_activamente_promocione_una_titulizacion_debera_retener_una_expo_c65c3d -> Sujeto_rol_alcance_capmin: sin mención
idx 11756: aplica_a Obligacion_el_registro_de_esas_operaciones_se_debera_realizar_en_la_fecha_de_su_concertacio_f2abed -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11759: aplica_a Obligacion_el_reporte_consignara_segun_corresponda_un_desglose_por_los_siguientes_criterios_090e3c -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11762: aplica_a Obligacion_el_reporte_debera_contener_estadisticas_comparativas_respecto_de_periodos_anteri_7d7090 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11765: aplica_a Obligacion_el_requisito_de_ingreso_y_liquidacion_de_las_divisas_de_las_financiaciones_conte_249cf7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11778: aplica_a Obligacion_el_responsable_del_regimen_informativo_y_el_auditor_externo_de_la_entidad_debera_2f14e6 -> Sujeto_banco: sin mención
idx 11783: aplica_a Obligacion_el_responsable_del_regimen_informativo_y_el_auditor_externo_de_la_entidad_verifi_6d162b -> Sujeto_banco: sin mención
idx 11785: aplica_a Obligacion_el_resto_de_las_entidades_financieras_deberan_tratar_a_los_depositos_sin_vencimi_f28aa3 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 11787: aplica_a Obligacion_el_resto_de_los_dias_permaneceran_en_una_base_a_disposicion_de_la_sefyc__ric_4_3_a0c79c -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 11789: aplica_a Obligacion_el_resto_del_capital_que_vencia_fue_como_minimo_refinanciado_con_un_nuevo_endeud_7dc216 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11791: aplica_a Obligacion_el_resto_del_capital_que_vencia_fue_como_minimo_refinanciado_con_un_nuevo_endeud_ad4522 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11794: aplica_a Obligacion_el_resto_del_valor_facturado_segun_la_condicion_de_venta_pactada_se_ha_cumplimen_20310e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11796: aplica_a Obligacion_el_resto_del_valor_facturado_segun_la_condicion_de_venta_pactada_se_ha_cumplimen_f3fecc -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11874: aplica_a Obligacion_el_resultado_de_la_liquidacion_de_cambios_debera_acreditarse_en_una_cuenta_local_cae97b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11876: aplica_a Obligacion_el_resultado_positivo_del_ultimo_ejercicio_cerrado_se_computara_una_vez_que_se_c_173ab3 -> Sujeto_rol_alcance_capmin: sin mención
idx 11886: aplica_a Obligacion_el_saldo_actualizado_de_la_totalidad_de_las_financiaciones_otorgadas_que_compren_782601 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 11888: aplica_a Obligacion_el_saldo_de_deuda_pendiente_se_compute_sin_deducir_previsiones_por_riesgo_de_inc_a0c2c8 -> Sujeto_rol_alcance_capmin: sin mención
idx 11895: aplica_a Obligacion_el_saldo_de_las_financiaciones_y_otras_exposiciones_se_registrara_en_los_codigos_d0be06 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 11902: aplica_a Obligacion_el_seguimiento_de_todas_las_operaciones_que_queden_comprendidas_en_los_puntos_7__d0420d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11906: aplica_a Obligacion_el_seguimiento_estara_a_cargo_de_la_entidad_que_otorgo_la_financiacion_hasta_su__24486e -> Sujeto_entidad_financiera: sin mención
idx 11908: aplica_a Obligacion_el_seguimiento_quedara_a_cargo_de_la_entidad_nominada_en_cumplimiento_a_lo_estab_f2be11 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11912: aplica_a Obligacion_el_seguimiento_quedara_a_cargo_de_la_entidad_que_a_pedido_del_exportador_y_luego_d16075 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11918: aplica_a Obligacion_el_seguimiento_quedara_inicialmente_a_cargo_de_la_entidad_que_de_curso_a_la_liqu_84117c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11920: aplica_a Obligacion_el_sello_de_la_entidad_financiera_acreditara_que_obra_en_su_poder_la_correspondi_3f97ab -> Sujeto_banco: sin mención
idx 11922: aplica_a Obligacion_el_sistema_de_incentivos_economicos_al_personal_no_deberia_asignar_igual_importe_9101ac -> Sujeto_entidad_financiera: sin mención
idx 11924: aplica_a Obligacion_el_sistema_de_incentivos_economicos_se_aplicara_con_mayores_recaudos_a_medida_qu_8d126e -> Sujeto_entidad_financiera: sin mención
idx 11927: aplica_a Obligacion_el_sistema_de_medicion_debera_abarcar_a_todos_los_derivados_de_tasas_de_interes__834f73 -> Sujeto_rol_alcance_capmin: sin mención
idx 11931: aplica_a Obligacion_el_sistema_vincule_el_monto_destinado_al_pago_de_incentivos_con_el_desempeno_y_e_d7f89b -> Sujeto_entidad_financiera: sin mención
idx 11934: aplica_a Obligacion_el_sujeto_obligado_debera_ante_la_solicitud_del_usuario_de_servicios_financieros_e511b3 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11937: aplica_a Obligacion_el_sujeto_obligado_debera_aplicar_1_5_veces_la_tasa_promedio_correspondiente_al__2dad05 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11939: aplica_a Obligacion_el_sujeto_obligado_y_quienes_resulten_responsables_seran_pasibles_de_la_aplicaci_e72398 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11941: aplica_a Obligacion_el_titular_de_la_cuenta_corriente_debe_suscribir_un_acuerdo_que_establezca_que_n_344d9a -> Sujeto_banco: sin mención
idx 11943: aplica_a Obligacion_el_total_de_flujos_de_fondos_asignados_de_cada_banda_debe_coincidir_con_los_tota_99db7c -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 11945: aplica_a Obligacion_el_unico_boleto_de_cambio_debera_contener_un_anexo_con_la_firma_del_cliente_en_e_e13848 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11947: aplica_a Obligacion_el_usuario_de_servicios_financieros_debe_ser_notificado_de_las_modificaciones_qu_89ecc2 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11950: aplica_a Obligacion_el_valor_del_inmueble_se_corresponda_al_del_momento_del_otorgamiento__cap_2_9_2__3eef81 -> Sujeto_rol_alcance_capmin: sin mención
idx 11952: aplica_a Obligacion_el_valor_del_inmueble_sea_el_resultado_de_una_tasacion_que_cumpla_los_siguientes_06b166 -> Sujeto_rol_alcance_capmin: sin mención
idx 11955: aplica_a Obligacion_el_vinculo_con_el_prestador_se_establezca_mediante_contratos_que_contemplen_clar_9158c2 -> Sujeto_entidad_financiera: sin mención
idx 11958: aplica_a Obligacion_elaborar_y_elevar_al_directorio_o_autoridad_equivalente_en_el_caso_de_los_sujeto_ac318d -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11975: aplica_a Obligacion_elevar_al_directorio_o_autoridad_equivalente_como_minimo_trimestralmente_un_repo_8bdfee -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 11977: aplica_a Obligacion_emitir_a_pedido_del_importador_certificaciones_con_el_detalle_correspondiente_pa_9e8e65 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11979: aplica_a Obligacion_emitir_a_pedido_del_importador_certificaciones_con_el_detalle_correspondiente_pa_a2153e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 11985: aplica_a Obligacion_emitir_a_pedido_del_importador_las_certificaciones_que_habilitaran_la_suscripcio_1d8eb8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12007: aplica_a Obligacion_emplear_los_elementos_de_seguridad_y_procedimientos_convenidos_para_el_libramien_50932f -> Sujeto_banco: sin mención
idx 12012: aplica_a Obligacion_emplear_los_procedimientos_establecidos_en_la_respectiva_guia_operativa_para_rem_97f7f2 -> Sujeto_banco: sin mención
idx 12019: aplica_a Obligacion_empleara_igual_procedimiento_en_los_casos_de_inhabilitaciones_de_cuentacorrentis_b47a40 -> Sujeto_banco: sin mención
idx 12022: aplica_a Obligacion_empresas_no_financieras_emisoras_de_tarjetas_de_credito_y_o_compra_son_sujetos_o_657dd5 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 12024: aplica_a Obligacion_en_ambos_casos_el_presentante_sera_el_destinatario_de_la_otra_fotocopia_certific_d1eee9 -> Sujeto_entidad_girada: sin mención
idx 12026: aplica_a Obligacion_en_ambos_casos_la_cobertura_debera_extinguir_totalmente_el_monto_adeudado_en_cas_f408aa -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12030: aplica_a Obligacion_en_aquellos_casos_en_que_no_se_establezcan_disposiciones_especificas_para_cada_u_d47eaf -> Sujeto_rol_alcance_capmin: sin mención
idx 12069: aplica_a Obligacion_en_caso_contrario_codigo_0__ric_12_4_514e37 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12071: aplica_a Obligacion_en_caso_contrario_se_empleara_el_fba_para_determinar_los_ponderadores_de_las_inv_554173 -> Sujeto_rol_alcance_capmin: sin mención
idx 12074: aplica_a Obligacion_en_caso_de_acuerdos_de_margenes_y_de_conjuntos_de_neteo_multiples_se_aplicaran_l_d05738 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12161: aplica_a Obligacion_en_caso_de_certificar_el_cumplido_del_permiso_debera_reportar_tambien_el_cierre__e03e8e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12163: aplica_a Obligacion_en_caso_de_cheques_librados_en_formato_papel_identificar_al_presentante_del_cheq_6eb7c5 -> Sujeto_banco: sin mención
idx 12166: aplica_a Obligacion_en_caso_de_corresponder_modelo_del_poder_mediante_el_cual_los_titulares_de_cuent_29e47e -> Sujeto_banco: sin mención
idx 12168: aplica_a Obligacion_en_caso_de_defectos_lo_comunicara_de_inmediato_al_librador_para_que_este_los_sal_dd1d31 -> Sujeto_entidad_girada: sin mención
idx 12170: aplica_a Obligacion_en_caso_de_existir_una_reduccion_del_plazo_vigente_el_plazo_reducido_solo_regira_7d230c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12174: aplica_a Obligacion_en_caso_de_no_cancelarse_las_multas_en_las_condiciones_senaladas_los_efectos_de__11de30 -> Sujeto_banco: sin mención
idx 12178: aplica_a Obligacion_en_caso_de_no_disponerla_documentacion_de_capitalizacion_debera_presentar_consta_d40430 -> Sujeto_cliente: sin mención
idx 12180: aplica_a Obligacion_en_caso_de_pagos_con_registro_de_ingreso_aduanero_se_debera_contar_con_la_corres_73d8b9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12182: aplica_a Obligacion_en_caso_de_preverse_el_libramiento_de_cheques_por_medios_electronicos_echeq_debe_8ee145 -> Sujeto_banco: sin mención
idx 12184: aplica_a Obligacion_en_caso_de_producirse_incorporaciones_compras_de_activos_durante_el_mes_se_tomar_3d9fae -> Sujeto_rol_alcance_capmin: sin mención
idx 12187: aplica_a Obligacion_en_caso_de_que_el_cheque_haya_sido_presentado_a_traves_de_una_entidad_depositari_2318da -> Sujeto_entidad_depositaria: sin mención
idx 12190: aplica_a Obligacion_en_caso_de_que_el_cliente_este_incluido_en_el_listado_de_cuits_con_operaciones_i_a16ec9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12193: aplica_a Obligacion_en_caso_de_que_el_contrato_prevea_como_causal_de_cierre_de_la_cuenta_haber_incur_a7edf0 -> Sujeto_banco: sin mención
idx 12198: aplica_a Obligacion_en_caso_de_que_el_nuevo_endeudamiento_sea_una_prefinanciacion_de_exportaciones_d_e58d5e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12200: aplica_a Obligacion_en_caso_de_que_el_usuario_obtuviera_con_cualquiera_de_las_tres_aseguradoras_ofre_698524 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12203: aplica_a Obligacion_en_caso_de_que_exista_una_ampliacion_del_plazo_para_un_producto_el_nuevo_plazo_s_4bb957 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12206: aplica_a Obligacion_en_caso_de_que_la_devolucion_reconociera_causas_concurrentes_con_la_de_insuficie_baa6a0 -> Sujeto_banco: sin mención
idx 12209: aplica_a Obligacion_en_caso_de_que_la_entidad_decida_su_cobro_por_el_servicio_de_registro_de_cheques_ea5708 -> Sujeto_banco: sin mención
idx 12211: aplica_a Obligacion_en_caso_de_que_la_entidad_depositaria_no_sea_la_girada_aquella_cursara_a_esta_ul_c972d0 -> Sujeto_banco: sin mención
idx 12214: aplica_a Obligacion_en_caso_de_que_la_entidad_expanda_una_facilidad_de_liquidez_para_cubrir_activos__c1075d -> Sujeto_rol_alcance_capmin: sin mención
idx 12220: aplica_a Obligacion_en_caso_de_que_la_importacion_de_bienes_encuadre_en_los_puntos_10_3_3_10_9_1_10__05962d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12246: aplica_a Obligacion_en_caso_de_que_la_inversion_corresponda_a_una_operacion_comprendida_en_el_punto__606185 -> Sujeto_entidad_financiera: sin mención
idx 12255: aplica_a Obligacion_en_caso_de_que_la_transferencia_corresponda_a_la_misma_moneda_en_la_que_esta_den_7131a9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12257: aplica_a Obligacion_en_caso_de_que_la_transferencia_corresponda_a_la_misma_moneda_en_la_que_esta_den_81eca3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12260: aplica_a Obligacion_en_caso_de_que_se_desconozca_la_situacion_de_cumplimiento_correspondiente_al_5_o_61d6b3 -> Sujeto_rol_alcance_capmin: sin mención
idx 12262: aplica_a Obligacion_en_caso_de_que_se_mantengan_activos_deducibles_conforme_a_esta_disposicion_la_en_fabf70 -> Sujeto_rol_alcance_capmin: sin mención
idx 12264: aplica_a Obligacion_en_caso_de_que_se_trate_de_servicios_prestados_a_residentes_paraguayos_o_uruguay_fc8bbd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12270: aplica_a Obligacion_en_caso_de_ventas_de_estos_activos_cierres_de_posiciones_debera_tenerse_en_cuent_dbea99 -> Sujeto_rol_alcance_capmin: sin mención
idx 12273: aplica_a Obligacion_en_caso_de_verificarse_atrasos_mayores_a_31_dias_en_el_pago_de_los_servicios_de__b377ca -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 12275: aplica_a Obligacion_en_caso_de_verificarse_atrasos_mayores_a_31_dias_en_el_pago_de_los_servicios_de__ef142e -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 12277: aplica_a Obligacion_en_caso_de_verificarse_refinanciaciones_en_condiciones_distintas_a_las_senaladas_649817 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 12279: aplica_a Obligacion_en_caso_que_la_entidad_registre_posiciones_significativas_en_otras_monedas_disti_7b9270 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12287: aplica_a Obligacion_en_casos_de_derivados_de_credito_de_enesimo_incumplimiento_acapite_iv_las_entida_c140ae -> Sujeto_rol_alcance_capmin: sin mención
idx 12290: aplica_a Obligacion_en_casos_de_incertidumbre_acerca_de_si_una_determinada_operacion_debe_considerar_7b5e38 -> Sujeto_rol_alcance_capmin: sin mención
idx 12292: aplica_a Obligacion_en_casos_de_incertidumbre_sobre_si_una_operacion_debe_considerarse_titulizacion__2d05c7 -> Sujeto_rol_alcance_capmin: sin mención
idx 12294: aplica_a Obligacion_en_casos_de_pagos_con_registro_de_ingreso_aduanero_pendiente_el_cliente_debera_d_b5b7b0 -> Sujeto_cliente: sin mención
idx 12296: aplica_a Obligacion_en_casos_donde_el_valor_de_mercado_del_subyacente_sea_cero_como_en_caps_floors_y_bbc9f4 -> Sujeto_rol_alcance_capmin: sin mención
idx 12299: aplica_a Obligacion_en_cuanto_a_los_activos_que_generan_intereses_sera_el_importe_que_surja_de_reexp_a0e4d5 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12302: aplica_a Obligacion_en_dichos_informes_se_debera_mencionar_la_cuit_o_el_cuil_o_la_cdi_segun_correspo_2455de -> Sujeto_banco: sin mención
idx 12304: aplica_a Obligacion_en_el_analisis_que_se_lleve_a_cabo_debera_tenerse_en_cuenta_de_corresponder_la_e_2a5138 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 12306: aplica_a Obligacion_en_el_analisis_que_se_lleve_a_cabo_debera_tenerse_en_cuenta_de_corresponder_la_e_b06dd1 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 12308: aplica_a Obligacion_en_el_boleto_de_cambio_debera_constar_el_caracter_de_declaracion_jurada_del_orde_2d8d12 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12311: aplica_a Obligacion_en_el_caso_de_aportes_de_inversion_directa_el_cliente_debera_presentar_la_docume_679540 -> Sujeto_cliente: sin mención
idx 12313: aplica_a Obligacion_en_el_caso_de_cartas_de_credito_o_letras_avaladas_emitidas_u_otorgadas_a_partir__a8267a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12318: aplica_a Obligacion_en_el_caso_de_entidades_en_las_cuales_los_miembros_del_directorio_cumplan_tambie_8662d3 -> Sujeto_entidad_financiera: sin mención
idx 12320: aplica_a Obligacion_en_el_caso_de_exposiciones_a_entidades_financieras_exposiciones_a_empresas_expos_fa480d -> Sujeto_rol_alcance_capmin: sin mención
idx 12323: aplica_a Obligacion_en_el_caso_de_financiaciones_propias_del_proveedor_o_aquellas_que_impliquen_pago_02b4fa -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12326: aplica_a Obligacion_en_el_caso_de_las_entidades_financieras_publicas_ademas_debera_mantener_de_corre_fc6d27 -> Sujeto_entidad_financiera: sin mención
idx 12328: aplica_a Obligacion_en_el_caso_de_las_exposiciones_subyacentes_a_las_operaciones_con_derivados_reali_54fd20 -> Sujeto_rol_alcance_capmin: sin mención
idx 12344: aplica_a Obligacion_en_el_caso_de_las_financiaciones_estas_deberan_ser_atendidas_por_las_filiales_o__300024 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 12347: aplica_a Obligacion_en_el_caso_de_las_financiaciones_estas_deberan_ser_atendidas_por_las_sucursales__4f691e -> Sujeto_rol_alcance_capmin: sin mención
idx 12349: aplica_a Obligacion_en_el_caso_de_las_titulizaciones_sinteticas_a_las_que_se_aporten_fondos_se_deber_564a03 -> Sujeto_rol_alcance_capmin: sin mención
idx 12351: aplica_a Obligacion_en_el_caso_de_los_instrumentos_de_deuda_computables_como_ca_o_pnc_al_admitir_los_d96a25 -> Sujeto_rol_alcance_capmin: sin mención
idx 12354: aplica_a Obligacion_en_el_caso_de_multiproductos_paquetes_de_productos_se_debera_informar_las_cuenta_fae158 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12363: aplica_a Obligacion_en_el_caso_de_no_haber_dado_curso_a_la_operacion_en_el_mercado_de_cambios_la_ent_b2a3a7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12374: aplica_a Obligacion_en_el_caso_de_operaciones_anteriores_al_02_09_19_la_entidad_debera_intervenir_la_e3a457 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12376: aplica_a Obligacion_en_el_caso_de_operaciones_comprendidas_en_el_punto_7_3_8_que_no_registren_liquid_dddda5 -> Sujeto_exportador: sin mención
idx 12419: aplica_a Obligacion_en_el_caso_de_operaciones_comprendidas_en_el_seguimiento_de_anticipos_y_otras_fi_0af78d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12421: aplica_a Obligacion_en_el_caso_de_pagos_con_registro_de_ingreso_aduanero_pendiente_la_operacion_qued_dbf35f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12431: aplica_a Obligacion_en_el_caso_de_pagos_concretados_a_partir_de_financiaciones_de_entidades_financie_0a9463 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12434: aplica_a Obligacion_en_el_caso_de_posiciones_fuera_de_balance_debera_aplicarse_un_factor_de_conversi_fc47d2 -> Sujeto_rol_alcance_capmin: sin mención
idx 12445: aplica_a Obligacion_en_el_caso_de_prestamos_hipotecarios_en_pesos_ofrecidos_por_entidades_financiera_43356f -> Sujeto_entidad_financiera: sin mención
idx 12447: aplica_a Obligacion_en_el_caso_de_prestamos_hipotecarios_en_pesos_ofrecidos_por_entidades_financiera_8f6bd8 -> Sujeto_entidad_financiera: sin mención
idx 12449: aplica_a Obligacion_en_el_caso_de_prestamos_personales_prendarios_o_hipotecarios_y_otros_prestamos_e_c32a95 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12451: aplica_a Obligacion_en_el_caso_de_que_deban_aguardar_para_ser_atendidos_se_les_debera_proveer_de_asi_0265ea -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12453: aplica_a Obligacion_en_el_caso_de_que_el_monto_adeudado_fuera_superior_a_usd_25_000_dolares_estadoun_cb1181 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12455: aplica_a Obligacion_en_el_caso_de_que_la_adquisicion_de_titulos_valores_se_haya_concretado_con_liqui_110a42 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12458: aplica_a Obligacion_en_el_caso_de_que_las_exposiciones_cubiertas_tengan_vencimientos_diferentes_se_u_2713b2 -> Sujeto_rol_alcance_capmin: sin mención
idx 12460: aplica_a Obligacion_en_el_caso_de_que_se_prevea_la_entrega_efectiva_de_instrumentos_operados_en_el_m_ad1583 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12462: aplica_a Obligacion_en_el_caso_de_que_se_valuen_a_modelo_los_parametros_se_evaluan_con_una_periodici_63bac9 -> Sujeto_rol_alcance_capmin: sin mención
idx 12465: aplica_a Obligacion_en_el_caso_de_que_una_exportacion_este_compuesta_por_distintos_productos_el_plaz_71f169 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12468: aplica_a Obligacion_en_el_caso_de_registrarse_excesos_en_los_limites_crediticios_globales_debera_inf_e7e79b -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12470: aplica_a Obligacion_en_el_caso_de_registrarse_excesos_en_los_limites_crediticios_individuales_debera_87b717 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12472: aplica_a Obligacion_en_el_caso_de_retitulizaciones_cuya_cartera_subyacente_consista_en_tramos_de_tit_336efb -> Sujeto_rol_alcance_capmin: sin mención
idx 12474: aplica_a Obligacion_en_el_caso_de_tarjetas_de_credito_los_limites_de_compra_de_compra_en_cuotas_de_f_907714 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12476: aplica_a Obligacion_en_el_caso_de_una_devolucion_de_fondos_del_exterior_asociada_a_un_pago_con_regis_67abee -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12479: aplica_a Obligacion_en_el_caso_de_una_importacion_oficializada_hasta_el_31_10_19_previamente_a_la_em_520a4c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12481: aplica_a Obligacion_en_el_caso_del_echeq_la_entidad_girada_informara_al_librador_el_importe_total_au_84a075 -> Sujeto_entidad_girada: sin mención
idx 12483: aplica_a Obligacion_en_el_codigo_15000000_se_consignara_el_cargo_adicional_de_capital_resultante_de__c723c6 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12490: aplica_a Obligacion_en_el_correspondiente_legajo_debera_quedar_constancia_de_la_aceptacion_o_no_de_e_4c3ae8 -> Sujeto_entidad_financiera: sin mención
idx 12492: aplica_a Obligacion_en_el_correspondiente_legajo_debera_quedar_constancia_de_que_el_cliente_ha_tomad_d0556c -> Sujeto_entidad_financiera: sin mención
idx 12494: aplica_a Obligacion_en_el_cuerpo_de_las_notificaciones_deberan_incluirse_las_leyendas_usted_podra_op_d26726 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12497: aplica_a Obligacion_en_el_curso_de_cada_trimestre_calendario_respecto_de_clientes_individualmente_co_acaa65 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 12499: aplica_a Obligacion_en_el_documento_suscripto_se_consignara_respecto_de_los_conceptos_incluidos_y_de_a42cf3 -> Sujeto_banco: sin mención
idx 12515: aplica_a Obligacion_en_el_extracto_informar_datos_de_transferencias_segun_lo_previsto_en_normas_sobr_88d13d -> Sujeto_banco: sin mención
idx 12518: aplica_a Obligacion_en_el_extracto_informar_i_si_se_producen_debitos_automaticos_denominacion_empres_1544e4 -> Sujeto_banco: sin mención
idx 12521: aplica_a Obligacion_en_el_legajo_se_reuniran_todos_los_elementos_de_juicio_que_se_tengan_en_cuenta_p_e96647 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 12523: aplica_a Obligacion_en_el_mismo_dia_de_la_presentacion_y_en_el_horario_habilitado_se_procedera_a_su__e25539 -> Sujeto_rol_alcance_pagjub: sin mención
idx 12526: aplica_a Obligacion_en_el_registro_de_la_operacion_debera_consignarse_el_nombre_y_apellido_completos_bac9b8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12528: aplica_a Obligacion_en_el_registro_de_la_operacion_debera_consignarse_el_nombre_y_apellido_completos_de6926 -> Sujeto_entidad_cambiaria: sin mención
idx 12529: aplica_a Obligacion_en_el_registro_de_la_operacion_debera_consignarse_el_nombre_y_apellido_completos_de6926 -> Sujeto_entidad_financiera: sin mención
idx 12531: aplica_a Obligacion_en_el_registro_se_asentaran_todas_las_intervenciones_originadas_en_denuncias_efe_540a9e -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12533: aplica_a Obligacion_en_el_resto_de_los_casos_deberan_usar_el_metodo_delta_plus_contemplado_en_el_pun_d6937f -> Sujeto_rol_alcance_capmin: sin mención
idx 12542: aplica_a Obligacion_en_el_resumen_se_hara_constar_el_importe_total_debitado_en_el_periodo_en_concept_d88a32 -> Sujeto_banco: sin mención
idx 12545: aplica_a Obligacion_en_el_resumen_se_hara_constar_el_plazo_de_compensacion_vigente_para_la_operatori_f72768 -> Sujeto_banco: sin mención
idx 12548: aplica_a Obligacion_en_el_resumen_se_hara_constar_la_clave_bancaria_uniforme_cbu_para_que_el_cliente_89996a -> Sujeto_banco: sin mención
idx 12551: aplica_a Obligacion_en_el_supuesto_de_ingreso_fuera_del_termino_fijado_deberan_abonarse_los_pertinen_eed4e7 -> Sujeto_rol_alcance_capmin: sin mención
idx 12553: aplica_a Obligacion_en_el_tratamiento_de_transparencia_la_posicion_de_maxima_preferencia_recibira_un_c3e071 -> Sujeto_rol_alcance_capmin: sin mención
idx 12562: aplica_a Obligacion_en_el_trato_que_dispensen_a_todas_las_personas_humanas_incluso_cuando_no_revista_183e31 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12570: aplica_a Obligacion_en_ese_analisis_se_pondra_enfasis_en_la_medicion_del_grado_de_exposicion_que_se__db6838 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 12572: aplica_a Obligacion_en_este_registro_se_deberan_asentar_los_montos_reintegrados_a_los_usuarios_ident_4406c0 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12575: aplica_a Obligacion_en_este_ultimo_caso_las_entidades_deberan_poner_a_disposicion_de_la_sefyc_tanto__557510 -> Sujeto_rol_alcance_capmin: sin mención
idx 12578: aplica_a Obligacion_en_la_banda_0_cero_se_informaran_los_saldos_a_fin_del_ultimo_mes_del_trimestre___556cd6 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12586: aplica_a Obligacion_en_la_certificacion_emitida_por_la_entidad_encargada_del_seguimiento_de_la_ofici_16e39d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12588: aplica_a Obligacion_en_la_certificacion_que_emita_la_entidad_debera_constar_al_menos_la_informacion__e0cbe6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12590: aplica_a Obligacion_en_la_certificacion_que_emita_la_entidad_debera_constar_al_menos_la_siguiente_in_1d5602 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12592: aplica_a Obligacion_en_la_certificacion_que_emita_la_entidad_para_habilitar_el_acceso_al_mercado_de__b7e080 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12594: aplica_a Obligacion_en_la_declaracion_jurada_del_cliente_debera_constar_expresamente_el_valor_de_sus_cbe3b4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12599: aplica_a Obligacion_en_la_informacion_sobre_base_consolidada_mensual_codigos_de_consolidacion_2_o_9__808d31 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12601: aplica_a Obligacion_en_la_materia_de_calculo_de_exigencia_de_capital_por_riesgo_de_credito_seran_de__26e860 -> Sujeto_rol_alcance_capmin: sin mención
idx 12604: aplica_a Obligacion_en_la_medida_de_lo_posible_el_proceso_de_evaluacion_debera_estar_libre_de_toda_r_3a239f -> Sujeto_ecai: sin mención
idx 12606: aplica_a Obligacion_en_la_medida_en_que_existan_fondos_suficientes_seran_abonados_cheques_segun_lo_p_7eaf2c -> Sujeto_banco: sin mención
idx 12619: aplica_a Obligacion_en_la_medida_que_la_entidad_no_cuente_con_el_registro_de_la_oficializacion_del_d_530af9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12621: aplica_a Obligacion_en_la_medida_que_la_verificacion_de_la_mercaderia_por_parte_de_la_aduana_no_cons_bca1ea -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12623: aplica_a Obligacion_en_la_nota_de_designacion_se_deben_explicitar_los_apellidos_y_nombres_tipo_y_n_d_b99a46 -> Sujeto_rol_alcance_pagjub: sin mención
idx 12625: aplica_a Obligacion_en_la_nota_debera_consignarse_el_numero_de_identificacion_de_la_operacion_numero_0e2aff -> Sujeto_entidad_financiera: sin mención
idx 12627: aplica_a Obligacion_en_la_sede_en_la_cual_desempene_sus_funciones_el_responsable_de_atencion_al_usua_a5934e -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12632: aplica_a Obligacion_en_las_partidas_correspondientes_a_cada_componente_ildc_sc_fc_rm_se_informaran_l_b030de -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12634: aplica_a Obligacion_en_las_presentaciones_debera_constar_un_analisis_de_la_entidad_interviniente_del_52bfde -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12636: aplica_a Obligacion_en_los_boletos_debera_constar_la_firma_del_cliente_que_realiza_la_operacion_de_c_5c1c7f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12639: aplica_a Obligacion_en_los_casos_de_adoptarse_metodos_especificos_de_evaluacion_a_los_efectos_del_ot_4c68df -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 12641: aplica_a Obligacion_en_los_casos_de_cheques_firmados_por_la_persona_a_cuya_orden_este_una_cuenta_en__cbb897 -> Sujeto_banco: sin mención
idx 12644: aplica_a Obligacion_en_los_casos_de_clientes_del_sector_privado_no_financiero_cuya_deuda_en_la_entid_fe7730 -> Sujeto_entidad_financiera: sin mención
idx 12647: aplica_a Obligacion_en_los_casos_de_clientes_residentes_en_el_exterior_debera_tenerse_en_cuenta_tamb_5f3152 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 12649: aplica_a Obligacion_en_los_casos_de_compensacion_de_riesgo_especifico_acapites_i_a_iii_se_tomara_la__9637d8 -> Sujeto_rol_alcance_capmin: sin mención
idx 12652: aplica_a Obligacion_en_los_casos_de_compromisos_asumidos_por_la_entidad_el_vencimiento_de_la_posicio_67d81d -> Sujeto_rol_alcance_capmin: sin mención
idx 12654: aplica_a Obligacion_en_los_casos_de_corresponsales_el_legajo_debera_contener_la_informacion_y_demas__4ab95e -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 12656: aplica_a Obligacion_en_los_casos_de_creditos_cedidos_a_favor_de_la_entidad_sin_responsabilidad_para__701cb0 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 12658: aplica_a Obligacion_en_los_casos_de_debito_automatico_del_resumen_de_tarjeta_de_credito_y_frente_a_l_5fe1ac -> Sujeto_banco: sin mención
idx 12660: aplica_a Obligacion_en_los_casos_de_devoluciones_de_pagos_anticipados_de_importaciones_de_bienes_se__ad708d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12662: aplica_a Obligacion_en_los_casos_de_las_entidades_financieras_el_analisis_debera_tener_en_cuenta_la__05823c -> Sujeto_banco: sin mención
idx 12664: aplica_a Obligacion_en_los_casos_de_regulaciones_sobre_base_consolidada_se_asimilaran_las_partidas_a_47ade8 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12666: aplica_a Obligacion_en_los_casos_de_retitulizaciones_la_entidad_debera_tener_ademas_de_la_informacio_dd8757 -> Sujeto_rol_alcance_capmin: sin mención
idx 12668: aplica_a Obligacion_en_los_casos_en_los_que_la_entidad_haya_constituido_una_prevision_especifica_o_t_fa617f -> Sujeto_rol_alcance_capmin: sin mención
idx 12670: aplica_a Obligacion_en_los_casos_en_que_empresas_no_financieras_operen_sus_propios_cajeros_automatic_c40d09 -> Sujeto_entidad_financiera: sin mención
idx 12673: aplica_a Obligacion_en_los_casos_en_que_la_presidencia_del_directorio_sea_ejercida_por_un_miembro_qu_2efe38 -> Sujeto_entidad_financiera: sin mención
idx 12675: aplica_a Obligacion_en_los_casos_en_que_los_cheques_se_depositen_en_la_caja_de_valores_s_a_para_ser__88806a -> Sujeto_banco: sin mención
idx 12677: aplica_a Obligacion_en_los_casos_en_que_los_criterios_hagan_referencia_a_activos_subyacentes_y_el_co_162811 -> Sujeto_rol_alcance_capmin: sin mención
idx 12708: aplica_a Obligacion_en_los_casos_encuadrados_en_los_puntos_7_6_3_2_y_7_6_3_4_en_la_medida_que_el_mon_12187c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12713: aplica_a Obligacion_en_los_casos_que_corresponda_se_computara_la_absorcion_prevista_en_la_partida_21_57abe4 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12715: aplica_a Obligacion_en_los_codigos_551100_xx_a_551700_xx_se_consignaran_los_importes_de_exigencia_qu_4df0a9 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12720: aplica_a Obligacion_en_los_codigos_60100000_a_61100000_se_incluiran_los_importes_que_surjan_como_con_3a5486 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12722: aplica_a Obligacion_en_los_contratos_celebrados_entre_el_usuario_de_servicios_financieros_y_los_suje_0ad971 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12724: aplica_a Obligacion_en_los_convenios_que_las_entidades_financieras_concierten_con_sus_clientes_para__2ffaef -> Sujeto_banco: sin mención
idx 12728: aplica_a Obligacion_en_los_restantes_casos_se_requerira_la_conformidad_previa_del_bcra_para_acceder__0609ad -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12731: aplica_a Obligacion_en_lugar_de_calcular_el_ajuste_de_valuacion_del_credito_cva_asociado_a_las_expos_b6b3f4 -> Sujeto_rol_alcance_capmin: sin mención
idx 12743: aplica_a Obligacion_en_operaciones_de_cambio_y_otras_donde_no_este_claro_que_lado_constituye_el_suby_3aa1b3 -> Sujeto_rol_alcance_capmin: sin mención
idx 12746: aplica_a Obligacion_en_oportunidad_del_envio_de_resumenes_de_cuenta_el_sujeto_obligado_debera_inclui_92193f -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12748: aplica_a Obligacion_en_su_caracter_de_entidad_seguidora_del_pago_la_entidad_sera_responsable_de_las__3666db -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12750: aplica_a Obligacion_en_su_participacion_en_la_cadena_de_pagos_de_transferencias_electronicas_de_fond_7b9613 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12753: aplica_a Obligacion_en_sus_clausulas_se_debera_prever_como_minimo__ctacte_1_5_60909c -> Sujeto_banco: sin mención
idx 12755: aplica_a Obligacion_en_tal_caso_debera_sumar_las_posiciones_individuales_netas_dentro_de_cada_banda__4c5f84 -> Sujeto_rol_alcance_capmin: sin mención
idx 12757: aplica_a Obligacion_en_titulizaciones_sinteticas_la_entidad_que_adquiera_proteccion_debera_mantener__1be7b2 -> Sujeto_rol_alcance_capmin: sin mención
idx 12760: aplica_a Obligacion_en_todas_las_operaciones_de_cambio_canje_y_o_arbitraje_que_se_cursen_por_el_merc_1f3428 -> Sujeto_entidad_cambiaria: sin mención
idx 12761: aplica_a Obligacion_en_todas_las_operaciones_de_cambio_canje_y_o_arbitraje_que_se_cursen_por_el_merc_1f3428 -> Sujeto_entidad_financiera: sin mención
idx 12766: aplica_a Obligacion_en_todos_los_casos_en_que_se_detectaren_indicios_de_un_fraude_cambiario_las_enti_aa26a0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12768: aplica_a Obligacion_en_todos_los_casos_la_entidad_debera_al_momento_de_dar_acceso_al_mercado_de_camb_b1a088 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12770: aplica_a Obligacion_en_todos_los_casos_la_entidad_debera_al_momento_de_dar_acceso_al_mercado_de_camb_be200f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12772: aplica_a Obligacion_en_todos_los_casos_la_entidad_debera_exigir_una_declaracion_jurada_sobre_el_cara_5efeb6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12775: aplica_a Obligacion_en_todos_los_casos_la_entidad_debera_obtener_evidencia_de_que_el_cliente_posee_i_f1f433 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12777: aplica_a Obligacion_en_todos_los_casos_la_entidad_debera_obtener_la_declaracion_jurada_sobre_el_cara_cce282 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12779: aplica_a Obligacion_en_todos_los_casos_la_entidad_interviniente_debera_contar_con_documentacion_en_l_718a0f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12781: aplica_a Obligacion_en_todos_los_casos_la_entidad_interviniente_debera_contar_con_documentacion_en_l_c97fac -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12783: aplica_a Obligacion_en_todos_los_casos_la_operacion_debera_estar_incorporada_al_seguimiento_de_antic_0abbdb -> Sujeto_vpu_rigi: sin mención
idx 12785: aplica_a Obligacion_en_todos_los_casos_las_entidades_financieras_los_pspcp_y_los_psi_deberan_observa_a4c2f1 -> Sujeto_entidad_financiera: sin mención
idx 12786: aplica_a Obligacion_en_todos_los_casos_las_entidades_financieras_los_pspcp_y_los_psi_deberan_observa_a4c2f1 -> Sujeto_psi_billetera_digital: sin mención
idx 12787: aplica_a Obligacion_en_todos_los_casos_las_entidades_financieras_los_pspcp_y_los_psi_deberan_observa_a4c2f1 -> Sujeto_pspcp: sin mención
idx 12790: aplica_a Obligacion_en_todos_los_casos_se_debera_contar_con_una_declaracion_jurada_del_cliente_en_la_ed5824 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12792: aplica_a Obligacion_en_todos_los_casos_se_debera_entregar_a_los_usuarios_de_servicios_financieros_co_5a8ba4 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12794: aplica_a Obligacion_en_todos_los_casos_se_debera_requerir_una_lista_detallada_de_los_beneficiarios_o_ce700b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12797: aplica_a Obligacion_en_todos_los_casos_se_debera_verificar_la_vigencia_del_documento_de_identidad_pr_25303b -> Sujeto_sujeto_regulado: sin mención
idx 12800: aplica_a Obligacion_encarguen_a_los_auditores_internos_que_evaluen_la_eficacia_de_los_controles_inte_d87acb -> Sujeto_entidad_financiera: sin mención
idx 12802: aplica_a Obligacion_encomiende_a_los_auditores_externos_la_evaluacion_de_los_procesos_de_control_int_0e65f5 -> Sujeto_entidad_financiera: sin mención
idx 12805: aplica_a Obligacion_encontrarse_ubicados_en_un_lugar_destacado_en_cuanto_a_visibilidad_y_tamano_del__4c2f02 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12807: aplica_a Obligacion_entender_en_la_estructura_operativa_de_la_entidad_conforme_a_lo_contemplado_en_e_7825d5 -> Sujeto_entidad_financiera: sin mención
idx 12815: aplica_a Obligacion_entienda_la_estructura_operativa_de_la_entidad_conforme_a_lo_previsto_en_el_punt_d0b7bc -> Sujeto_entidad_financiera: sin mención
idx 12823: aplica_a Obligacion_enunciar_las_actividades_de_negociacion_que_la_entidad_incluye_en_esta_cartera___e02835 -> Sujeto_rol_alcance_capmin: sin mención
idx 12825: aplica_a Obligacion_enviar_al_titular_de_la_cuenta_cuando_se_utilice_la_modalidad_de_cheques_de_pago_64e873 -> Sujeto_banco: sin mención
idx 12827: aplica_a Obligacion_es_deseable_incluir_en_los_sitios_publicos_de_las_entidades_financieras_paginas__476957 -> Sujeto_entidad_financiera: sin mención
idx 12829: aplica_a Obligacion_es_deseable_incluir_en_los_sitios_publicos_de_las_entidades_financieras_paginas__dcbcf5 -> Sujeto_entidad_financiera: sin mención
idx 12831: aplica_a Obligacion_es_necesario_en_orden_a_las_buenas_practicas_que_el_directorio_y_la_alta_gerenci_605dc4 -> Sujeto_entidad_financiera: sin mención
idx 12833: aplica_a Obligacion_es_preciso_en_orden_a_las_buenas_practicas_que_el_directorio_a_traves_de_la_inte_8236be -> Sujeto_entidad_financiera: sin mención
idx 12836: aplica_a Obligacion_es_recomendable_una_apropiada_divulgacion_de_la_informacion_hacia_el_depositante_85b71a -> Sujeto_entidad_financiera: sin mención
idx 12838: aplica_a Obligacion_ese_sistema_debe_ser_parte_integral_de_la_gestion_de_riesgos_y_del_gobierno_soci_f43cda -> Sujeto_entidad_financiera: sin mención
idx 12842: aplica_a Obligacion_especificar_el_valor_nocional_incluyendo_la_moneda_o_unidad_de_medida_ej_usd_25__8bb66f -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12844: aplica_a Obligacion_especifique_sus_facultades_y_responsabilidades__lingob_2_4_1_ace15f -> Sujeto_entidad_financiera: sin mención
idx 12846: aplica_a Obligacion_esta_deduccion_se_computara_en_la_medida_que_subsista_el_riesgo_de_credito_y_en__675039 -> Sujeto_rol_alcance_capmin: sin mención
idx 12848: aplica_a Obligacion_esta_entidad_sera_la_unica_responsable_de_emitir_los_certificados_de_aplicacion__f5f920 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12850: aplica_a Obligacion_esta_informacion_debera_incluir_clasificacion_promedio_de_los_deudores_conforme__9259c1 -> Sujeto_rol_alcance_capmin: sin mención
idx 12853: aplica_a Obligacion_esta_informacion_debera_incluir_diversificacion_geografica_y_sectorial__cap_3_1__3e0c2a -> Sujeto_rol_alcance_capmin: sin mención
idx 12855: aplica_a Obligacion_esta_informacion_debera_incluir_financiaciones_en_gestion_judicial__cap_3_1_3_2_2c0382 -> Sujeto_rol_alcance_capmin: sin mención
idx 12857: aplica_a Obligacion_esta_informacion_debera_incluir_porcentaje_de_financiaciones_vencidas_con_detall_63a6b1 -> Sujeto_rol_alcance_capmin: sin mención
idx 12859: aplica_a Obligacion_esta_informacion_debera_incluir_porcentaje_de_la_deuda_inicial_subyacente_cancel_f8f37b -> Sujeto_rol_alcance_capmin: sin mención
idx 12861: aplica_a Obligacion_esta_informacion_debera_incluir_ratio_promedio_de_monto_desembolsado_sobre_el_va_56739a -> Sujeto_rol_alcance_capmin: sin mención
idx 12863: aplica_a Obligacion_esta_informacion_debera_incluir_tasa_de_ocupacion_de_los_inmuebles__cap_3_1_3_2_df730e -> Sujeto_rol_alcance_capmin: sin mención
idx 12865: aplica_a Obligacion_esta_informacion_debera_incluir_tasas_de_incumplimiento__cap_3_1_3_2_1c1aa9 -> Sujeto_rol_alcance_capmin: sin mención
idx 12867: aplica_a Obligacion_esta_informacion_debera_incluir_tipo_de_exposicion__cap_3_1_3_2_7eb843 -> Sujeto_rol_alcance_capmin: sin mención
idx 12869: aplica_a Obligacion_esta_informacion_debera_incluir_tipo_de_propiedad_tal_como_vivienda_o_inmueble_c_37d772 -> Sujeto_rol_alcance_capmin: sin mención
idx 12871: aplica_a Obligacion_establecer_bajo_la_guia_del_directorio_un_sistema_de_control_interno_efectivo__l_8f5b29 -> Sujeto_entidad_financiera: sin mención
idx 12873: aplica_a Obligacion_establecer_claramente_las_responsabilidades_en_materia_de_gobierno_societario_pa_7490e6 -> Sujeto_entidad_financiera: sin mención
idx 12875: aplica_a Obligacion_establecer_las_politicas_para_cumplir_los_objetivos_societarios__lingob_1_2_1_fce15c -> Sujeto_entidad_financiera: sin mención
idx 12877: aplica_a Obligacion_establecer_procesos_adecuados_para_la_aprobacion_de_operaciones_y_nuevos_product_71ab2f -> Sujeto_entidad_financiera: sin mención
idx 12879: aplica_a Obligacion_establecer_una_estructura_gerencial_que_fomente_la_asuncion_de_responsabilidades_78d359 -> Sujeto_entidad_financiera: sin mención
idx 12881: aplica_a Obligacion_establecera_los_objetivos_estrategicos_y_un_codigo_de_etica_que_reuna_los_estand_4e59b0 -> Sujeto_entidad_financiera: sin mención
idx 12883: aplica_a Obligacion_establezca_canales_de_comunicacion__lingob_2_1_11_bf3c08 -> Sujeto_entidad_financiera: sin mención
idx 12885: aplica_a Obligacion_establezca_estandares_de_desempeno_para_la_alta_gerencia_compatibles_con_los_obj_a1326f -> Sujeto_entidad_financiera: sin mención
idx 12887: aplica_a Obligacion_estan_sujetas_a_un_seguimiento_activo_con_relacion_a_las_fuentes_de_informacion__94f71f -> Sujeto_rol_alcance_capmin: sin mención
idx 12890: aplica_a Obligacion_estar_constituido_de_modo_tal_que_le_permita_ejercitar_un_juicio_competente_e_in_fd926e -> Sujeto_entidad_financiera: sin mención
idx 12892: aplica_a Obligacion_estar_sujeto_a_un_seguimiento_desde_la_fecha_de_acceso_al_mercado_de_cambios_has_8ef53a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12894: aplica_a Obligacion_estar_suscripta_por_dos_de_los_funcionarios_responsables_de_la_rendicion_de_cuen_e3f919 -> Sujeto_rol_alcance_pagjub: sin mención
idx 12904: aplica_a Obligacion_estas_disposiciones_tambien_resultan_aplicables_a_los_anexos_al_legajo_del_clien_225592 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 12906: aplica_a Obligacion_estas_financiaciones_deberan_ser_incluidas_a_efectos_de_determinar_el_total_de_f_f4b03e -> Sujeto_entidad_financiera: sin mención
idx 12915: aplica_a Obligacion_estas_normas_son_de_aplicacion_a_todos_los_sujetos_obligados_enumerados_en_el_pu_35f186 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12917: aplica_a Obligacion_estas_operaciones_deberan_ser_canceladas_con_fondos_originados_en_el_cobro_de_ex_8d78b2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12920: aplica_a Obligacion_estas_politicas_deberan_contemplar_la_divulgacion_de_informacion_general_sobre_l_7bfc47 -> Sujeto_entidad_financiera: sin mención
idx 12923: aplica_a Obligacion_este_procedimiento_tambien_se_empleara_ante_cualquier_modificacion_del_manual_qu_5a00b3 -> Sujeto_banco: sin mención
idx 12925: aplica_a Obligacion_este_registro_estara_a_disposicion_del_bcra__ext_11_2_1_7_db1931 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12927: aplica_a Obligacion_este_riesgo_se_discriminara_por_mercado_entendido_a_estos_efectos_como_el_pais_e_c7305d -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12929: aplica_a Obligacion_estos_calculos_deberan_ser_consistentes_con_la_informacion_reportada_en_los_cuad_d2b47d -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12931: aplica_a Obligacion_estos_pagos_se_cursaran_con_un_boleto_de_venta_a_nombre_del_cliente_por_el_conce_ffe397 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 12933: aplica_a Obligacion_estos_recursos_deberan_permitirles_estar_en_contacto_permanente_con_el_directori_6dc69c -> Sujeto_ecai: sin mención
idx 12935: aplica_a Obligacion_estos_sistemas_deberan_estar_integrados_a_los_demas_sistemas_de_gestion_de_riesg_70b537 -> Sujeto_rol_alcance_capmin: sin mención
idx 12937: aplica_a Obligacion_evaluar_los_informes_emitidos_por_la_auditoria_interna_la_auditoria_externa_y_la_89e4ce -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12939: aplica_a Obligacion_evaluar_los_reportes_trimestrales_que_genere_el_responsable_de_atencion_al_usuar_3d7cb5 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 12941: aplica_a Obligacion_evaluara_el_riesgo_que_supone_concentrar_actividades_en_uno_o_pocos_prestadores__c161c1 -> Sujeto_entidad_financiera: sin mención
idx 12944: aplica_a Obligacion_evalue_anualmente_teniendo_en_consideracion_como_minimo_estos_lineamientos_si_el_e87282 -> Sujeto_entidad_financiera: sin mención
idx 12946: aplica_a Obligacion_evitar_la_realizacion_de_actividades_a_traves_de_estructuras_societarias_o_de_ju_61e5b8 -> Sujeto_entidad_financiera: sin mención
idx 12948: aplica_a Obligacion_evite_conflictos_de_intereses_incluso_potenciales_en_relacion_con_sus_actividade_084416 -> Sujeto_entidad_financiera: sin mención
idx 12950: aplica_a Obligacion_exigencia_de_capital_para_una_posicion_comprada_en_el_subyacente_y_comprada_en_l_5713c4 -> Sujeto_rol_alcance_capmin: sin mención
idx 12953: aplica_a Obligacion_exigencia_de_capital_para_una_posicion_vendida_en_el_subyacente_y_comprada_en_la_8fc03f -> Sujeto_rol_alcance_capmin: sin mención
idx 12956: aplica_a Obligacion_exigencia_de_capital_por_riesgo_de_posiciones_en_productos_basicos__cap_6_5_131744 -> Sujeto_rol_alcance_capmin: sin mención
idx 12961: aplica_a Obligacion_exigencia_por_riesgo_operacional_segun_el_punto_5_1__ric_8_1_7_dadf4f -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 12963: aplica_a Obligacion_exijan_a_las_gerencias_la_rapida_correccion_de_los_problemas__lingob_5_1_1_2_6d1544 -> Sujeto_entidad_financiera: sin mención
idx 12967: aplica_a Obligacion_exposicion_al_riesgo_de_credito_de_contraparte_del_fondo_se_debera_calcular_de_a_75bdc8 -> Sujeto_rol_alcance_capmin: sin mención
idx 12974: aplica_a Obligacion_facilitar_las_verificaciones_que_realice_el_banco_central_de_la_republica_argent_26af4f -> Sujeto_banco: sin mención
idx 12977: aplica_a Obligacion_falta_de_pago_de_la_correspondiente_multa_dentro_de_los_30_dias_corridos_de_la_n_00b8a5 -> Sujeto_banco: sin mención
idx 12981: aplica_a Obligacion_fecha_y_lugar_de_nacimiento_datos_requeridos_para_identificacion_de_titulares_de_de54fc -> Sujeto_banco: sin mención
idx 12983: aplica_a Obligacion_fecha_y_numero_de_inscripcion_en_el_pertinente_registro_oficial__ctacte_1_3_2_4_a4aee4 -> Sujeto_banco: sin mención
idx 12985: aplica_a Obligacion_finalizado_ese_plazo_sera_de_aplicacion_el_punto_4_3_4__cap_4_3_2_09fd1e -> Sujeto_rol_alcance_capmin: sin mención
idx 12993: aplica_a Obligacion_firmarlos_de_puno_y_letra_o_por_los_medios_alternativos_que_se_autoricen__ctacte_fd7610 -> Sujeto_banco: sin mención
idx 12996: aplica_a Obligacion_fomente_el_buen_funcionamiento_de_la_entidad_financiera__lingob_2_1_13_45b636 -> Sujeto_entidad_financiera: sin mención
idx 12998: aplica_a Obligacion_fomenten_la_independencia_del_auditor_interno_respecto_de_las_areas_y_procesos_c_4aa79c -> Sujeto_entidad_financiera: sin mención
idx 13000: aplica_a Obligacion_fotocopiar_por_duplicado_el_anverso_y_reverso_del_cheque_librado_en_formato_pape_3c6508 -> Sujeto_banco: sin mención
idx 13002: aplica_a Obligacion_garantizar_que_usuarios_con_dificultad_visual_tengan_acceso_a_plataformas_operat_d2b987 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 13004: aplica_a Obligacion_guardar_la_constancia_de_entrega_y_en_su_caso_de_la_personeria_del_receptor__cta_996fd4 -> Sujeto_banco: sin mención
idx 13006: aplica_a Obligacion_guardar_la_tarjeta_magnetica_en_un_lugar_seguro_y_verificar_periodicamente_su_ex_1d7853 -> Sujeto_banco: sin mención
idx 13008: aplica_a Obligacion_haber_verificado_que_se_encuentra_declarada_en_caso_de_corresponder_en_la_ultima_385108 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13010: aplica_a Obligacion_habilitar_a_traves_del_servicio_de_banca_por_internet_home_banking_o_en_su_defec_b96b13 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 13012: aplica_a Obligacion_haran_constar_la_fecha_en_que_tiene_lugar_esa_presentacion_a_partir_de_la_cual_c_1cecc5 -> Sujeto_banco: sin mención
idx 13014: aplica_a Obligacion_hasta_tanto_se_le_haya_notificado_la_aprobacion_de_los_aportes_y_en_la_medida_en_21558e -> Sujeto_rol_alcance_capmin: sin mención
idx 13016: aplica_a Obligacion_hasta_tanto_se_le_haya_notificado_la_aprobacion_de_los_aportes_y_en_la_medida_en_b1e95c -> Sujeto_rol_alcance_capmin: sin mención
idx 13029: aplica_a Obligacion_identicas_condiciones_se_deberan_cumplir_para_que_la_entidad_financiera_de_ese_t_791a7b -> Sujeto_rol_alcance_capmin: sin mención
idx 13033: aplica_a Obligacion_identico_tratamiento_correspondera_aplicar_a_los_cheques_de_pago_diferido_regist_3913ce -> Sujeto_banco: sin mención
idx 13036: aplica_a Obligacion_identificacion_de_la_entidad_remitente_casa_o_filial_en_que_se_encuentra_radicad_cdabc3 -> Sujeto_banco: sin mención
idx 13038: aplica_a Obligacion_identificacion_de_la_organizacion_de_los_archivos_utilizados_en_esta_operatoria__a10a70 -> Sujeto_banco: sin mención
idx 13040: aplica_a Obligacion_identificacion_de_los_dos_funcionarios_remitentes_autorizados_al_efecto_por_la_e_ed4d0d -> Sujeto_entidad_girada: sin mención
idx 13042: aplica_a Obligacion_identificacion_del_soporte_inicial_de_los_registros_de_firmas__ctacte_3_3_8_2_db94ff -> Sujeto_banco: sin mención
idx 13044: aplica_a Obligacion_identificacion_y_presentacion_de_la_profesion_oficio_industria_comercio_o_princi_19a7d5 -> Sujeto_banco: sin mención
idx 13046: aplica_a Obligacion_identificar_a_la_persona_que_presenta_el_cheque_en_ventanilla_inclusive_cuando_e_f4b15b -> Sujeto_banco: sin mención
idx 13048: aplica_a Obligacion_identificar_el_pago_a_nivel_de_cada_beneficiario_del_pais_o_del_exterior__ext_5__842ca9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13050: aplica_a Obligacion_identificar_en_el_extracto_las_operaciones_realizadas_por_cuenta_propia_o_por_cu_9266d7 -> Sujeto_banco: sin mención
idx 13053: aplica_a Obligacion_identificar_evaluar_y_gestionar_los_riesgos_originados_en_tales_actividades_como_229865 -> Sujeto_entidad_financiera: sin mención
idx 13055: aplica_a Obligacion_identificar_los_distintos_tipos_de_transaccion_mediante_un_codigo_especifico_que_d08167 -> Sujeto_banco: sin mención
idx 13058: aplica_a Obligacion_identificar_los_riesgos_significativos__cap_6_8_3_1_2633df -> Sujeto_rol_alcance_capmin: sin mención
idx 13060: aplica_a Obligacion_implementar_las_estrategias_y_politicas_aprobadas_por_el_directorio__lingob_1_4__aa4410 -> Sujeto_entidad_financiera: sin mención
idx 13064: aplica_a Obligacion_implementar_sistemas_apropiados_de_control_interno_y_monitorear_su_efectividad___849ce3 -> Sujeto_entidad_financiera: sin mención
idx 13066: aplica_a Obligacion_implica_el_mantenimiento_de_espacios_amplios_entre_puestos_de_atencion__pro_2_2__2d6ae0 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 13069: aplica_a Obligacion_implica_la_eliminacion_de_escalones_desniveles_o_cualquier_otra_clase_de_obstacu_e4e109 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 13072: aplica_a Obligacion_implica_la_incorporacion_de_elementos_que_orienten_o_faciliten_la_circulacion__p_4f77b0 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 13075: aplica_a Obligacion_implica_la_instalacion_de_rampas_para_facilitar_el_acceso__pro_2_2_4_1_59558d -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 13078: aplica_a Obligacion_incluir_en_el_aviso_de_rechazo_al_pago_o_a_la_registracion_de_cheques_el_domicil_c18f05 -> Sujeto_banco: sin mención
idx 13080: aplica_a Obligacion_incluir_en_el_aviso_de_rechazo_al_pago_o_a_la_registracion_de_cheques_los_nombre_00c511 -> Sujeto_banco: sin mención
idx 13082: aplica_a Obligacion_incluir_en_el_calculo_de_la_posicion_abierta_neta_la_posicion_neta_a_plazo_confo_dce1c7 -> Sujeto_rol_alcance_capmin: sin mención
idx 13084: aplica_a Obligacion_incluir_en_el_calculo_de_la_posicion_abierta_neta_la_posicion_neta_al_contado_co_59cd07 -> Sujeto_rol_alcance_capmin: sin mención
idx 13086: aplica_a Obligacion_incluir_en_el_calculo_de_la_posicion_abierta_neta_las_garantias_otorgadas_e_inst_263b8c -> Sujeto_rol_alcance_capmin: sin mención
idx 13088: aplica_a Obligacion_incluir_en_la_denuncia_el_tipo_y_numeros_de_los_documentos_afectados__ctacte_7_2_4b6b12 -> Sujeto_banco: sin mención
idx 13090: aplica_a Obligacion_incluir_en_las_clausulas_del_contrato_de_cuenta_corriente_la_nomina_de_los_debit_628912 -> Sujeto_banco: sin mención
idx 13093: aplica_a Obligacion_incluir_en_las_transferencias_de_fondos_con_el_exterior_y_en_sus_respectivos_men_0b0e50 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13095: aplica_a Obligacion_incluir_en_las_transferencias_de_fondos_con_el_exterior_y_en_sus_respectivos_men_af90b4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13098: aplica_a Obligacion_incluir_en_las_transferencias_de_fondos_con_el_exterior_y_en_sus_respectivos_men_e94af4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13101: aplica_a Obligacion_incluir_las_cuentas_bancarias_unicas_de_las_que_sean_titulares_las_agrupaciones__0de20e -> Sujeto_banco: sin mención
idx 13103: aplica_a Obligacion_incrementos_por_excesos_verificados_a_los_limites_de_participacion_en_el_capital_fd4cab -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 13105: aplica_a Obligacion_indicar_en_los_campos_correspondientes_el_activo_comprado_y_el_activo_vendido_se_82ee88 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 13107: aplica_a Obligacion_indicar_expresamente_si_la_tasa_de_interes_comisiones_y_cargos_podran_modificars_b9863c -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 13110: aplica_a Obligacion_indicar_nombre_apellido_numero_de_documento_de_identificacion_valido_conforme_a__0f35ab -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 13113: aplica_a Obligacion_indicar_si_el_desarrollo_de_la_aplicacion_fue_realizado_internamente_en_el_banco_307cc7 -> Sujeto_banco: sin mención
idx 13115: aplica_a Obligacion_informacion_adecuada_sobre_el_proposito_estrategias_riesgos_y_controles_respecto_0390c8 -> Sujeto_entidad_financiera: sin mención
idx 13117: aplica_a Obligacion_informando_al_directorio_sobre_sus_conclusiones_con_periodicidad_anual_o_cuando__b716e6 -> Sujeto_entidad_financiera: sin mención
idx 13119: aplica_a Obligacion_informar_a_la_sefyc_los_fundamentos_que_sustenten_el_criterio_aplicado_respecto__ea336f -> Sujeto_rol_alcance_capmin: sin mención
idx 13121: aplica_a Obligacion_informar_al_bcra_los_rechazos_de_cheques_por_defectos_formales_los_rechazos_a_la_19f4c5 -> Sujeto_banco: sin mención
idx 13123: aplica_a Obligacion_informar_al_cuentacorrentista_el_saldo_que_registren_las_correspondientes_cuenta_6ef6b0 -> Sujeto_banco: sin mención
idx 13126: aplica_a Obligacion_informar_dentro_de_las_24_hs_habiles_siguientes_a_la_recepcion_de_la_denuncia_en_97c7ab -> Sujeto_banco: sin mención
idx 13128: aplica_a Obligacion_informar_el_porcentaje_de_representacion_de_cada_genero_en_el_directorio_el_orga_8c2b2a -> Sujeto_entidad_financiera: sin mención
idx 13130: aplica_a Obligacion_informar_el_saldo_de_la_cuenta_corriente_involucrada_en_el_aviso_del_cierre_de_l_d927e3 -> Sujeto_banco: sin mención
idx 13132: aplica_a Obligacion_informar_la_operacion_como_una_compra_de_billetes_de_moneda_extranjera_codigo_de_cfa3ba -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13136: aplica_a Obligacion_informarle_al_usuario_la_situacion_mediante_el_empleo_de_alguno_de_los_medios_el_1dc014 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 13139: aplica_a Obligacion_instruir_a_la_alta_gerencia_para_que_implemente_los_procedimientos_de_gestion_de_40d7f9 -> Sujeto_entidad_financiera: sin mención
idx 13141: aplica_a Obligacion_integrar_el_capital_minimo_exigido_dentro_de_los_60_dias_corridos_de_su_otorgami_7a3bf7 -> Sujeto_rol_alcance_capmin: sin mención
idx 13143: aplica_a Obligacion_integrar_los_cheques_en_pesos_o_dolares_estadounidenses_segun_corresponda__ctact_92c734 -> Sujeto_banco: sin mención
idx 13146: aplica_a Obligacion_junto_con_la_nota_deberan_presentarse_por_separado_dos_archivos_conteniendo_en_u_a6b359 -> Sujeto_rol_alcance_pagjub: sin mención
idx 13148: aplica_a Obligacion_junto_con_la_nota_deberan_presentarse_por_separado_dos_archivos_en_el_otro_un_de_c5499f -> Sujeto_rol_alcance_pagjub: sin mención
idx 13150: aplica_a Obligacion_la_accesibilidad_a_los_puntos_de_atencion_al_usuario_casas_operativas_y_cajeros__7f6e05 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 13153: aplica_a Obligacion_la_aceptacion_de_las_obligaciones_conlleva_la_responsabilidad_ineludible_de_las__159f9d -> Sujeto_banco: sin mención
idx 13154: aplica_a Obligacion_la_aceptacion_de_las_obligaciones_conlleva_la_responsabilidad_ineludible_de_las__159f9d -> Sujeto_cliente: sin mención
idx 13156: aplica_a Obligacion_la_afectacion_de_la_rpc_por_aplicacion_de_lo_senalado_determinara_la_obligacion__1deede -> Sujeto_rol_alcance_capmin: sin mención
idx 13158: aplica_a Obligacion_la_alta_gerencia_bajo_la_supervision_del_directorio_debera_documentar_este_proce_c8bc92 -> Sujeto_entidad_financiera: sin mención
idx 13161: aplica_a Obligacion_la_alta_gerencia_debera_conocer_que_elementos_de_las_carteras_de_negociacion_o_d_439636 -> Sujeto_rol_alcance_capmin: sin mención
idx 13163: aplica_a Obligacion_la_alta_gerencia_entre_otros_aspectos_sera_responsable_de__lingob_1_4_6b76cc -> Sujeto_entidad_financiera: sin mención
idx 13165: aplica_a Obligacion_la_aplicacion_de_cobros_de_exportaciones_de_endeudamientos_financieros_estara_ha_af0fe5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13167: aplica_a Obligacion_la_aplicacion_de_comisiones_y_o_cargos_debe_quedar_circunscripta_a_la_efectiva_p_f9fcb0 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 13169: aplica_a Obligacion_la_aplicacion_de_la_tecnica_requerira_emplear_unicamente_el_metodo_de_sustitucio_4c35f6 -> Sujeto_rol_alcance_capmin: sin mención
idx 13171: aplica_a Obligacion_la_aplicacion_de_los_recursos_propios_liquidos_debera_ajustarse_al_criterio_gene_a2d951 -> Sujeto_entidad_financiera: sin mención
idx 13174: aplica_a Obligacion_la_asignacion_de_fondos_tendra_en_cuenta_el_costo_y_el_nivel_de_riesgo_de_liquid_236176 -> Sujeto_entidad_financiera: sin mención
idx 13176: aplica_a Obligacion_la_asignacion_de_fondos_tendra_en_cuenta_el_costo_y_la_cantidad_de_capital_reque_4860fc -> Sujeto_entidad_financiera: sin mención
idx 13178: aplica_a Obligacion_la_asignacion_de_fondos_tendra_en_cuenta_la_probabilidad_de_que_se_materialicen__d20b9e -> Sujeto_entidad_financiera: sin mención
idx 13180: aplica_a Obligacion_la_asistencia_crediticia_que_otorguen_las_entidades_financieras_debera_estar_ori_1fd853 -> Sujeto_entidad_financiera: sin mención
idx 13193: aplica_a Obligacion_la_auditoria_interna_debera_llevar_a_cabo_una_revision_exhaustiva_del_esquema_qu_212218 -> Sujeto_rol_alcance_capmin: sin mención
idx 13199: aplica_a Obligacion_la_calificacion_debera_tener_en_cuenta_y_reflejar_toda_la_exposicion_al_riesgo_d_7feb91 -> Sujeto_rol_alcance_capmin: sin mención
idx 13201: aplica_a Obligacion_la_capacidad_de_prestamo_de_los_depositos_en_moneda_extranjera_debera_aplicarse__ee3051 -> Sujeto_entidad_financiera: sin mención
idx 13204: aplica_a Obligacion_la_cartera_debera_estar_diversificada__cap_2_8_3_2_9acfad -> Sujeto_rol_alcance_capmin: sin mención
idx 13206: aplica_a Obligacion_la_cartera_debera_ser_gestionada_de_forma_activa_y_las_posiciones_valuadas_en_fo_bee932 -> Sujeto_rol_alcance_capmin: sin mención
idx 13208: aplica_a Obligacion_la_casa_operativa_debera_ser_informada_al_cliente_en_el_momento_de_su_asignacion_4741ea -> Sujeto_entidad_financiera: sin mención
idx 13215: aplica_a Obligacion_la_certificacion_de_aplicacion_debera_contener_como_minimo_la_siguiente_informac_51c9d3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13217: aplica_a Obligacion_la_certificacion_debera_ser_acreditada_en_la_forma_prevista_en_el_punto_5_5_4__c_745e47 -> Sujeto_banco: sin mención
idx 13225: aplica_a Obligacion_la_certificacion_que_emita_la_entidad_financiera_debera_basarse_en_flujos_de_div_fdcc1e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13227: aplica_a Obligacion_la_certificacion_que_emita_la_entidad_financiera_debera_basarse_en_las_proyeccio_fd892f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13229: aplica_a Obligacion_la_certificacion_que_emita_la_entidad_financiera_debera_basarse_en_proporcion_de_3a00be -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13231: aplica_a Obligacion_la_certificacion_que_emita_la_entidad_financiera_debera_basarse_en_ventas_extern_3c0596 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13233: aplica_a Obligacion_la_certificacion_que_se_presente_en_el_bcra_debera_contener_como_minimo_el_detal_8a9433 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13235: aplica_a Obligacion_la_certificacion_que_se_presente_en_el_bcra_debera_contener_si_existen_endeudami_fc1001 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13237: aplica_a Obligacion_la_certificacion_que_se_presente_en_el_bcra_debera_contener_su_numero_de_identif_5179ec -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13239: aplica_a Obligacion_la_circunstancia_de_aprobacion_ad_referendum_debera_ser_expuesta_en_nota_a_los_e_6ee741 -> Sujeto_rol_alcance_capmin: sin mención
idx 13241: aplica_a Obligacion_la_circunstancia_de_que_el_aval_sea_otorgado_por_un_banco_debera_constar_en_el_c_da2eae -> Sujeto_banco: sin mención
idx 13243: aplica_a Obligacion_la_clasificacion_de_los_deudores_debera_efectuarse_con_una_periodicidad_que_atie_5c816d -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 13246: aplica_a Obligacion_la_clasificacion_de_los_deudores_y_el_calculo_de_las_previsiones_por_riesgo_de_i_aa5703 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 13248: aplica_a Obligacion_la_compensacion_de_posiciones_en_las_carteras_de_inversion_y_de_negociacion_solo_2d3b8a -> Sujeto_rol_alcance_capmin: sin mención
idx 13255: aplica_a Obligacion_la_cual_debera_contener_como_minimo_el_monto_proyectado_a_invertir__ext_7_9_4_147cfc -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13257: aplica_a Obligacion_la_cual_debera_contener_como_minimo_la_composicion_del_financiamiento__ext_7_9_4_570bdc -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13259: aplica_a Obligacion_la_cual_debera_contener_como_minimo_la_descripcion_del_proyecto__ext_7_9_4_2249d8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13261: aplica_a Obligacion_la_cuenta_debera_estar_operativa_el_dia_habil_bancario_siguiente_a_aquel_en_que__f13004 -> Sujeto_banco: sin mención
idx 13275: aplica_a Obligacion_la_decision_de_capitalizacion_de_los_conceptos_indicados_en_los_puntos_8_6_1_a_8_5b7345 -> Sujeto_rol_alcance_capmin: sin mención
idx 13286: aplica_a Obligacion_la_decision_de_incluir_ingresos_y_egresos_futuros_se_debera_adoptar_de_modo_cons_cbb64b -> Sujeto_rol_alcance_capmin: sin mención
idx 13288: aplica_a Obligacion_la_declaracion_jurada_debera_estar_firmada_por_el_cliente_no_residente_o_su_repr_e2683a -> Sujeto_persona_humana: sin mención
idx 13290: aplica_a Obligacion_la_declaracion_jurada_debera_estar_firmada_por_el_cliente_o_su_representante_leg_859859 -> Sujeto_cliente: sin mención
idx 13293: aplica_a Obligacion_la_deduccion_se_efectuara_por_el_importe_del_mayor_saldo_registrado_durante_el_m_4db618 -> Sujeto_rol_alcance_capmin: sin mención
idx 13295: aplica_a Obligacion_la_deduccion_se_efectuara_por_el_importe_del_mayor_saldo_registrado_durante_el_m_e846d0 -> Sujeto_rol_alcance_capmin: sin mención
idx 13298: aplica_a Obligacion_la_deduccion_sera_equivalente_al_100_del_valor_de_dichos_bienes_desde_su_incorpo_6fbffe -> Sujeto_rol_alcance_capmin: sin mención
idx 13301: aplica_a Obligacion_la_denominacion_de_los_productos_o_servicios_en_las_solicitudes_contratos_sistem_294962 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 13305: aplica_a Obligacion_la_determinacion_de_esta_exigencia_se_efectuara_por_cada_moneda_a_cuyos_efectos__41330e -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 13307: aplica_a Obligacion_la_devolucion_de_las_certificaciones_no_utilizadas_sera_efectuada_entre_las_enti_0063e2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13309: aplica_a Obligacion_la_documentacion_debe_demostrar_que_el_pago_garantizado_debia_ser_concretado_por_2f125f -> Sujeto_entidad_financiera: sin mención
idx 13314: aplica_a Obligacion_la_documentacion_debe_permitir_determinar_el_detalle_de_los_bienes_a_importar_la_df23d0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13318: aplica_a Obligacion_la_documentacion_final_de_la_oferta_o_el_prospecto_debera_estar_disponible_desde_a75e97 -> Sujeto_rol_alcance_capmin: sin mención
idx 13320: aplica_a Obligacion_la_documentacion_provisional_inicial_oferta_o_prospecto_provisional_y_de_apoyo_t_140710 -> Sujeto_rol_alcance_capmin: sin mención
idx 13322: aplica_a Obligacion_la_documentacion_que_avale_la_causal_de_la_demora_que_respalda_la_ampliacion_del_d7aa35 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13324: aplica_a Obligacion_la_documentacion_que_instrumente_la_titulizacion_debera_incluir_una_opinion_lega_a1b57f -> Sujeto_rol_alcance_capmin: sin mención
idx 13326: aplica_a Obligacion_la_documentacion_relativa_a_la_designacion_de_los_responsables_de_atencion_al_us_3a70b0 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 13336: aplica_a Obligacion_la_documentacion_respaldatoria_de_la_implementacion_y_aquella_resultante_de_la_o_4f3816 -> Sujeto_banco: sin mención
idx 13338: aplica_a Obligacion_la_documentacion_utilizada_para_certificar_el_concepto_y_monto_de_las_divisas_im_163b25 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13340: aplica_a Obligacion_la_documentacion_utilizada_para_certificar_el_concepto_y_monto_de_las_divisas_im_65af51 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13342: aplica_a Obligacion_la_documentacion_utilizada_por_la_entidad_financiera_y_hojas_de_trabajo_que_aval_28c200 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13344: aplica_a Obligacion_la_documentacion_vinculada_con_la_crc_debera_observar_los_requisitos_legales_vig_49fb19 -> Sujeto_rol_alcance_capmin: sin mención
idx 13346: aplica_a Obligacion_la_documentacion_y_el_proceso_legal_para_la_ejecucion_debera_permitir_a_la_entid_109aac -> Sujeto_rol_alcance_capmin: sin mención
idx 13348: aplica_a Obligacion_la_ead_reducida_se_utilizara_tambien_para_el_calculo_del_ajuste_de_valuacion_de__fcf14d -> Sujeto_miembro_compensador: sin mención
idx 13359: aplica_a Obligacion_la_emision_de_nuevas_acciones_como_consecuencia_de_haberse_producido_alguno_de_t_d3034e -> Sujeto_rol_alcance_capmin: sin mención
idx 13377: aplica_a Obligacion_la_entidad_a_cargo_del_seguimiento_de_los_pagos_con_registro_de_ingreso_aduanero_a76755 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13379: aplica_a Obligacion_la_entidad_a_cargo_del_seguimiento_debera_considerar_como_utilizada_toda_certifi_4429d9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13381: aplica_a Obligacion_la_entidad_a_cargo_del_seguimiento_debera_incorporar_en_el_sepaimpo_los_registro_2414d2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13383: aplica_a Obligacion_la_entidad_a_cargo_del_seguimiento_debera_notificarle_la_voluntad_del_beneficiar_523a22 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13385: aplica_a Obligacion_la_entidad_a_cargo_del_seguimiento_debera_notificarle_la_voluntad_del_exportador_2d2bc8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13387: aplica_a Obligacion_la_entidad_a_cargo_del_seguimiento_debera_notificarle_la_voluntad_del_exportador_47bab0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13389: aplica_a Obligacion_la_entidad_a_cargo_del_seguimiento_debera_notificarle_la_voluntad_del_exportador_8202b0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13391: aplica_a Obligacion_la_entidad_a_cargo_del_seguimiento_debera_notificarle_la_voluntad_del_exportador_eaa062 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13393: aplica_a Obligacion_la_entidad_aceptara_los_cheques_librados_por_cualquiera_de_los_titulares_aun_en__d25805 -> Sujeto_banco: sin mención
idx 13396: aplica_a Obligacion_la_entidad_adicionalmente_debera_contar_con_una_declaracion_jurada_del_importado_10ec5b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13399: aplica_a Obligacion_la_entidad_adicionalmente_debera_contar_con_una_declaracion_jurada_del_importado_20916a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13401: aplica_a Obligacion_la_entidad_avalista_debera_emitir_certificado_nominativo_transferible_segun_mode_b7eed2 -> Sujeto_banco: sin mención
idx 13403: aplica_a Obligacion_la_entidad_bancaria_debera_poner_en_conocimiento_del_bcra_el_cobro_de_las_corres_c31e19 -> Sujeto_banco: sin mención
idx 13405: aplica_a Obligacion_la_entidad_calculara_el_monto_alcanzado_por_la_obligacion_a_partir_de_la_informa_55e96d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13407: aplica_a Obligacion_la_entidad_cuenta_con_documentacion_que_le_permite_constatar_que_la_operacion_de_d41b6b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13409: aplica_a Obligacion_la_entidad_cuenta_con_una_declaracion_jurada_del_cliente_en_la_que_consta_que_el_c8a860 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13411: aplica_a Obligacion_la_entidad_cuenta_con_una_declaracion_jurada_del_exportador_en_la_que_deje_const_b3630b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13414: aplica_a Obligacion_la_entidad_cuente_con_documentacion_que_le_permita_verificar_el_caracter_genuino_0199b4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13416: aplica_a Obligacion_la_entidad_cuente_con_documentacion_que_le_permita_verificar_que_el_exportador_h_40cc87 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13418: aplica_a Obligacion_la_entidad_cuente_con_documentacion_que_le_permita_verificar_que_en_caso_de_corr_525ca6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13420: aplica_a Obligacion_la_entidad_cuente_con_la_certificacion_de_liquidacion_de_los_fondos_en_el_mercad_e5180e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13423: aplica_a Obligacion_la_entidad_cuente_con_una_declaracion_jurada_del_cliente_en_la_que_conste_que_la_a5898d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13425: aplica_a Obligacion_la_entidad_debe_contar_con_certificacion_para_el_acceso_al_mercado_de_cambios_em_eee685 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13427: aplica_a Obligacion_la_entidad_debe_contar_con_documentacion_fehaciente_que_avale_que_la_fecha_de_ot_67019d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13429: aplica_a Obligacion_la_entidad_debe_contar_con_la_documentacion_debidamente_certificada_que_acredite_67a7c5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13431: aplica_a Obligacion_la_entidad_debe_contar_con_los_documentos_de_embarque_dentro_de_los_50_cincuenta_71f072 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13433: aplica_a Obligacion_la_entidad_debe_contar_con_una_declaracion_jurada_del_cliente_en_la_cual_deje_co_ef5cbb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13435: aplica_a Obligacion_la_entidad_debe_informar_los_rechazos_de_cheques_al_bcra_conforme_al_regimen_ope_ae234d -> Sujeto_banco: sin mención
idx 13446: aplica_a Obligacion_la_entidad_debe_mantener_la_exigencia_de_capital_correspondiente_a_todas_sus_pos_d9cd6a -> Sujeto_rol_alcance_capmin: sin mención
idx 13448: aplica_a Obligacion_la_entidad_debe_suministrar_informaciones_al_bcra_referidas_a_las_multas_percibi_f7078d -> Sujeto_banco: sin mención
idx 13451: aplica_a Obligacion_la_entidad_debera_adicionalmente_contar_con_documentacion_que_demuestre_que_por__623c81 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13453: aplica_a Obligacion_la_entidad_debera_adicionalmente_remitir_la_certificacion_del_cumplimiento_de_la_a8b640 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13455: aplica_a Obligacion_la_entidad_debera_al_momento_de_dar_acceso_al_mercado_de_cambios_contar_con_la_c_e44563 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13457: aplica_a Obligacion_la_entidad_debera_al_momento_de_dar_acceso_al_mercado_de_cambios_contar_con_la_c_f963b5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13459: aplica_a Obligacion_la_entidad_debera_antes_de_la_emision_de_cada_certificacion_constatar_el_valor_d_d34ca1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13464: aplica_a Obligacion_la_entidad_debera_comprender_todas_las_caracteristicas_estructurales_de_los_prog_9a0c9a -> Sujeto_rol_alcance_capmin: sin mención
idx 13466: aplica_a Obligacion_la_entidad_debera_considerar_la_evaluacion_de_la_calidad_y_disponibilidad_de_los_1339ec -> Sujeto_rol_alcance_capmin: sin mención
idx 13469: aplica_a Obligacion_la_entidad_debera_considerar_la_liquidez_del_mercado_la_capacidad_de_obtener_cob_5129b0 -> Sujeto_rol_alcance_capmin: sin mención
idx 13472: aplica_a Obligacion_la_entidad_debera_constatar_adicionalmente_que_el_pago_cumple_alguna_de_las_sigu_65318e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13484: aplica_a Obligacion_la_entidad_debera_contar_con_declaracion_jurada_del_cliente_en_que_conste_que_en_5686d1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13486: aplica_a Obligacion_la_entidad_debera_contar_con_documentacion_adicional_que_le_permita_certificar_e_900b47 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13488: aplica_a Obligacion_la_entidad_debera_contar_con_documentacion_tecnica_que_le_permita_certificar_la__8c0476 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13490: aplica_a Obligacion_la_entidad_debera_contar_con_la_certificacion_de_liquidacion_emitida_por_la_enti_0c8f4f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13492: aplica_a Obligacion_la_entidad_debera_contar_con_la_conformidad_previa_del_bcra__ext_3_16_2_222a31 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13494: aplica_a Obligacion_la_entidad_debera_contar_con_la_conformidad_previa_del_bcra_en_el_caso_de_que_el_8abb6f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13497: aplica_a Obligacion_la_entidad_debera_contar_con_la_conformidad_previa_del_bcra_para_operaciones_con_659d6b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13500: aplica_a Obligacion_la_entidad_debera_contar_con_la_correspondiente_certificacion_de_afectacion_emit_a0237b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13502: aplica_a Obligacion_la_entidad_debera_contar_con_la_correspondiente_certificacion_de_afectacion_emit_e091e2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13504: aplica_a Obligacion_la_entidad_debera_contar_con_la_correspondiente_certificacion_de_la_entidad_enca_c74fd1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13507: aplica_a Obligacion_la_entidad_debera_contar_con_la_correspondiente_declaracion_jurada_del_cliente_e_dbab90 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13509: aplica_a Obligacion_la_entidad_debera_contar_con_la_declaracion_jurada_del_exportador_respecto_al_ca_b7275b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13511: aplica_a Obligacion_la_entidad_debera_contar_con_la_documentacion_de_la_cual_surjan_los_montos_corre_f4138d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13513: aplica_a Obligacion_la_entidad_debera_contar_con_la_documentacion_emitida_por_la_secretaria_de_trans_96cf38 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13515: aplica_a Obligacion_la_entidad_debera_contar_con_la_documentacion_que_demuestre_que_al_momento_de_la_50957b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13522: aplica_a Obligacion_la_entidad_debera_contar_con_la_documentacion_que_demuestre_que_al_momento_de_la_6fe5f6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13529: aplica_a Obligacion_la_entidad_debera_contar_con_la_documentacion_que_demuestre_que_se_han_cumplimen_8a31f8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13531: aplica_a Obligacion_la_entidad_debera_contar_con_la_validacion_de_la_declaracion_del_relevamiento_de_9b6370 -> Sujeto_entidad_financiera: sin mención
idx 13533: aplica_a Obligacion_la_entidad_debera_contar_con_los_elementos_que_le_permitan_constatar_el_caracter_101f02 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13535: aplica_a Obligacion_la_entidad_debera_contar_con_una_certificacion_de_aplicacion_emitida_por_la_enca_530193 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13537: aplica_a Obligacion_la_entidad_debera_contar_con_una_certificacion_de_auditor_externo_en_la_cual_se__2ca941 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13539: aplica_a Obligacion_la_entidad_debera_contar_con_una_certificacion_de_auditor_externo_en_la_cual_se__70087d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13542: aplica_a Obligacion_la_entidad_debera_contar_con_una_certificacion_de_la_entidad_encargada_del_segui_8dee2e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13551: aplica_a Obligacion_la_entidad_debera_contar_con_una_certificacion_emitida_por_la_entidad_que_dio_cu_8cd178 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13553: aplica_a Obligacion_la_entidad_debera_contar_con_una_certificacion_para_el_acceso_al_mercado_de_camb_2877d5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13555: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_cliente_en_la_cual_deje__a9ff85 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13558: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_cliente_en_la_que_conste_19bae9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13560: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_cliente_en_la_que_conste_359420 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13562: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_cliente_en_la_que_conste_932e46 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13564: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_cliente_en_la_que_conste_e15424 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13566: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_cliente_en_la_que_conste_e26f38 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13568: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_cliente_en_la_que_deja_c_2ed3e8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13570: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_cliente_en_la_que_deje_c_1b1db0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13575: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_exportador_detallando_el_f783a8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13578: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_exportador_en_la_que_con_cf3363 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13580: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_exportador_indicando_que_c53a9b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13582: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_importador_en_la_cual_de_bcab02 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13584: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_importador_en_la_cual_de_c78b6e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13586: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_importador_en_la_que_se__9c3a2e -> Sujeto_entidad_financiera: sin mención
idx 13588: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_firmada_por_el_representante_88b380 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13590: aplica_a Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_firmada_por_el_representante_e3f2f2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13592: aplica_a Obligacion_la_entidad_debera_cumplir_con_lo_previsto_en_el_punto_3_1_de_las_normas_sobre_ev_f9f4b1 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 13594: aplica_a Obligacion_la_entidad_debera_cumplir_con_lo_previsto_en_el_punto_3_1_del_to_sobre_evaluacio_c30531 -> Sujeto_rol_alcance_capmin: sin mención
idx 13596: aplica_a Obligacion_la_entidad_debera_dar_cumplimiento_a_las_disposiciones_dadas_a_conocer_por_el_re_3abed3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13598: aplica_a Obligacion_la_entidad_debera_dejar_registradas_las_certificaciones_de_aplicacion_emitidas_p_b435b9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13600: aplica_a Obligacion_la_entidad_debera_determinar_el_plazo_aplicable_a_cada_exportacion_a_partir_de_l_97634a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13614: aplica_a Obligacion_la_entidad_debera_efectuar_el_correspondiente_registro_a_su_nombre_por_los_inter_6e261d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13616: aplica_a Obligacion_la_entidad_debera_emitir_una_certificacion_de_cumplido_para_aquellas_destinacion_0f360a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13618: aplica_a Obligacion_la_entidad_debera_encuadrarse_en_la_exigencia_a_mas_tardar_en_el_segundo_mes_sig_7f76ad -> Sujeto_rol_alcance_capmin: sin mención
idx 13621: aplica_a Obligacion_la_entidad_debera_exigir_ademas_de_la_documentacion_senalada_una_declaracion_jur_6ebe41 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13624: aplica_a Obligacion_la_entidad_debera_exigir_una_declaracion_jurada_sobre_el_caracter_genuino_de_los_349f1f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13626: aplica_a Obligacion_la_entidad_debera_informar_la_asuncion_al_bcra__ext_8_2_eadb9b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13628: aplica_a Obligacion_la_entidad_debera_inhabilitar_el_zfi_para_la_realizacion_de_pagos__ext_11_1_1_9_e1da10 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13631: aplica_a Obligacion_la_entidad_debera_integrar_capital_por_las_posiciones_de_titulizacion_que_conser_dadd91 -> Sujeto_entidad_originante_de_transferencia: sin mención
idx 13633: aplica_a Obligacion_la_entidad_debera_intervenir_dejando_constancia_de_la_fecha_y_monto_pagado_al_ex_d2a2ad -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13635: aplica_a Obligacion_la_entidad_debera_intervenir_la_documentacion_aduanera_dejando_constancia_de_la__0785e4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13637: aplica_a Obligacion_la_entidad_debera_llevar_un_legajo_de_cada_deudor_de_su_cartera_asi_como_de_cada_d986bd -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 13639: aplica_a Obligacion_la_entidad_debera_llevar_un_registro_actualizado_de_las_personas_habilitadas_en__49e8e2 -> Sujeto_banco: sin mención
idx 13641: aplica_a Obligacion_la_entidad_debera_notificar_cualquier_modificacion_en_la_situacion_de_un_permiso_31b00e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13643: aplica_a Obligacion_la_entidad_debera_obtener_evidencia_de_que_el_cliente_posee_ingresos_y_o_activos_11cc93 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13645: aplica_a Obligacion_la_entidad_debera_proporcionar_en_ese_mismo_acto_constancia_del_respectivo_trami_396a6c -> Sujeto_banco: sin mención
idx 13650: aplica_a Obligacion_la_entidad_debera_realizar_la_denuncia_dentro_de_los_10_diez_dias_habiles_contad_1c911a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13652: aplica_a Obligacion_la_entidad_debera_realizar_previamente_la_correspondiente_registracion_o_constat_962df8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13654: aplica_a Obligacion_la_entidad_debera_realizar_un_boleto_de_compra_y_o_venta_de_cambio_segun_corresp_055a31 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13661: aplica_a Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_de_la_empresa_q_42b2a0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13663: aplica_a Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_cliente_por_445c45 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13686: aplica_a Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_cliente_por_f44a3a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13688: aplica_a Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_importador__bca138 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13690: aplica_a Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_importador__bec81b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13693: aplica_a Obligacion_la_entidad_debera_registrar_ante_el_bcra_toda_operacion_que_realice_en_el_mercad_79842c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13695: aplica_a Obligacion_la_entidad_debera_reportar_en_el_sepaimpo_cuando_se_convalide_un_monto_comprendi_ffa742 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13698: aplica_a Obligacion_la_entidad_debera_reportar_la_extension_otorgada_en_el_sepaimpo__ext_10_4_2_4_f5c345 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13700: aplica_a Obligacion_la_entidad_debera_reportarlo_al_bcra_dentro_de_los_5_cinco_dias_habiles_de_conva_dd8a7e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13703: aplica_a Obligacion_la_entidad_debera_requerir_una_declaracion_jurada_del_cliente_respecto_a_que_la__2b21ea -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13705: aplica_a Obligacion_la_entidad_debera_tambien_registrar_en_sus_bases_de_datos_cualquier_otra_circuns_bd439a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13707: aplica_a Obligacion_la_entidad_debera_tener_acceso_en_todo_momento_a_la_informacion_sobre_el_comport_061130 -> Sujeto_rol_alcance_capmin: sin mención
idx 13709: aplica_a Obligacion_la_entidad_debera_verificar_el_cumplimiento_de_la_totalidad_de_los_restantes_req_c251ec -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13730: aplica_a Obligacion_la_entidad_debera_verificar_los_requisitos_habituales_a_los_efectos_de_certifica_29cd07 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13732: aplica_a Obligacion_la_entidad_debera_verificar_previamente_a_dar_curso_a_operaciones_de_egresos_de__6fd6ad -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13735: aplica_a Obligacion_la_entidad_debera_verificar_previamente_a_emitir_cada_certificacion_el_cumplimie_7946b1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13738: aplica_a Obligacion_la_entidad_debera_verificar_previamente_a_emitir_cada_certificacion_el_cumplimie_d43adb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13740: aplica_a Obligacion_la_entidad_debera_verificar_previamente_a_emitir_cada_certificacion_la_correspon_9a08b2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13742: aplica_a Obligacion_la_entidad_debera_verificar_previamente_que_se_cumplen_la_totalidad_de_los_requi_46ae54 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13744: aplica_a Obligacion_la_entidad_debera_verificar_que_cada_cuota_sea_separada_en_el_componente_de_pago_02d402 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13746: aplica_a Obligacion_la_entidad_debera_verificar_que_el_cliente_haya_dado_cumplimiento_en_caso_de_cor_79853d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13748: aplica_a Obligacion_la_entidad_debera_verificar_que_el_cliente_haya_dado_cumplimiento_en_caso_de_cor_c13abd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13750: aplica_a Obligacion_la_entidad_debera_verificar_que_la_operacion_encuadra_en_alguna_de_las_situacion_50a7ee -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13758: aplica_a Obligacion_la_entidad_debera_verificar_que_la_operacion_encuadra_en_alguna_de_las_situacion_de1a9c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13765: aplica_a Obligacion_la_entidad_depositaria_emitira_los_pertinentes_certificados_nominativos_transfer_5c2034 -> Sujeto_entidad_depositaria: sin mención
idx 13767: aplica_a Obligacion_la_entidad_depositaria_especificara_en_el_dorso_del_cheque_en_la_zona_reservada__0b9c17 -> Sujeto_entidad_depositaria: sin mención
idx 13769: aplica_a Obligacion_la_entidad_efectuara_la_pertinente_comunicacion_al_banco_central_de_la_republica_b445f2 -> Sujeto_banco: sin mención
idx 13771: aplica_a Obligacion_la_entidad_en_la_cual_se_le_acreditaron_los_fondos_al_exportador_debera_asumir_e_caa84b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13773: aplica_a Obligacion_la_entidad_encargada_del_seguimiento_de_la_oficializacion_del_despacho_de_import_229f16 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13776: aplica_a Obligacion_la_entidad_encargada_del_seguimiento_de_la_oficializacion_del_despacho_de_import_e4aeca -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13778: aplica_a Obligacion_la_entidad_encargada_del_seguimiento_de_la_prefinanciacion_cancelada_registrara__4735e6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13780: aplica_a Obligacion_la_entidad_encargada_del_seguimiento_de_un_permiso_de_embarque_debera_registrar__d9acfe -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13783: aplica_a Obligacion_la_entidad_encargada_del_seguimiento_debera_adicionalmente_realizar_el_seguimien_f90ccc -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13790: aplica_a Obligacion_la_entidad_encargada_del_seguimiento_debera_reportar_cuando_otorgue_extensiones__5ff8c9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13793: aplica_a Obligacion_la_entidad_encargada_del_seguimiento_debera_reportar_en_el_sepaimpo_toda_circuns_9829f0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13795: aplica_a Obligacion_la_entidad_encargada_del_seguimiento_debera_tomar_los_montos_en_exceso_a_cuenta__c91243 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13798: aplica_a Obligacion_la_entidad_encargada_del_seguimiento_debera_verificar_el_cumplimiento_de_las_sig_14a4b6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13801: aplica_a Obligacion_la_entidad_encargada_del_seguimiento_sera_la_responsable_de_constatar_el_cumplim_9f7034 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13807: aplica_a Obligacion_la_entidad_financiera_administradora_debera_asumir_la_responsabilidad_del_cumpli_f1472d -> Sujeto_banco: sin mención
idx 13809: aplica_a Obligacion_la_entidad_financiera_administradora_debera_representar_a_dicha_empresa_ante_la__4b5d05 -> Sujeto_banco: sin mención
idx 13811: aplica_a Obligacion_la_entidad_financiera_debe_divulgar_informacion_sobre_sus_practicas_de_incentivo_ada010 -> Sujeto_entidad_financiera: sin mención
idx 13813: aplica_a Obligacion_la_entidad_financiera_debe_tener_derecho_a_recibir_cualquiera_de_estos_pagos_del_865002 -> Sujeto_rol_alcance_capmin: sin mención
idx 13815: aplica_a Obligacion_la_entidad_financiera_debera_conservar_la_formula_de_certificacion_hasta_tanto_e_0370f7 -> Sujeto_banco: sin mención
idx 13817: aplica_a Obligacion_la_entidad_financiera_debera_considerar_a_las_ccp_que_no_califican_como_entidade_a38e86 -> Sujeto_rol_alcance_capmin: sin mención
idx 13819: aplica_a Obligacion_la_entidad_financiera_debera_contar_en_todo_momento_con_las_autorizaciones_neces_bc4590 -> Sujeto_rol_alcance_capmin: sin mención
idx 13827: aplica_a Obligacion_la_entidad_financiera_debera_deducir_del_capital_ordinario_de_nivel_uno_co_n1_el_c06c11 -> Sujeto_rol_alcance_capmin: sin mención
idx 13833: aplica_a Obligacion_la_entidad_financiera_debera_extender_el_plazo_originalmente_previsto_para_el_pr_01171b -> Sujeto_entidad_financiera: sin mención
idx 13836: aplica_a Obligacion_la_entidad_financiera_debera_implementar_adecuadas_funciones_de_control_interno__3e0f29 -> Sujeto_entidad_financiera: sin mención
idx 13838: aplica_a Obligacion_la_entidad_financiera_debera_informar_el_origen_de_dicha_circunstancia_a_la_sefy_5426b7 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 13840: aplica_a Obligacion_la_entidad_financiera_debera_realizar_las_rectificaciones_necesarias_para_que_ta_44faab -> Sujeto_entidad_financiera: sin mención
idx 13842: aplica_a Obligacion_la_entidad_financiera_debera_reponer_el_capital_y_o_reducir_sus_posiciones_de_ac_84cbf0 -> Sujeto_rol_alcance_capmin: sin mención
idx 13844: aplica_a Obligacion_la_entidad_financiera_depositaria_o_girada_debera_emitirlo_conforme_a_lo_estable_8f69d0 -> Sujeto_entidad_depositaria: sin mención
idx 13845: aplica_a Obligacion_la_entidad_financiera_depositaria_o_girada_debera_emitirlo_conforme_a_lo_estable_8f69d0 -> Sujeto_entidad_girada: sin mención
idx 13847: aplica_a Obligacion_la_entidad_financiera_designada_debera_remitir_por_nota_dirigida_a_la_gerencia_p_9c55e8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13849: aplica_a Obligacion_la_entidad_financiera_designada_por_el_beneficiario_para_la_emision_de_las_certi_05ec19 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13851: aplica_a Obligacion_la_entidad_financiera_encargada_del_seguimiento_de_anticipos_y_otras_financiacio_393644 -> Sujeto_entidad_financiera: sin mención
idx 13855: aplica_a Obligacion_la_entidad_financiera_local_debera_registrar_ante_el_bcra_que_el_importador_ejer_9670e2 -> Sujeto_entidad_financiera: sin mención
idx 13857: aplica_a Obligacion_la_entidad_financiera_local_nominada_sera_la_responsable_de_emitir_las_certifica_6e653e -> Sujeto_entidad_financiera: sin mención
idx 13859: aplica_a Obligacion_la_entidad_financiera_que_actue_en_caracter_de_miembro_compensador_de_una_ccp_po_b7a624 -> Sujeto_miembro_compensador: sin mención
idx 13862: aplica_a Obligacion_la_entidad_financiera_que_cuente_con_multiples_tecnicas_de_crc_para_cubrir_una_u_9646c1 -> Sujeto_rol_alcance_capmin: sin mención
idx 13865: aplica_a Obligacion_la_entidad_financiera_que_haya_realizado_el_pago_entrega_si_al_final_de_la_jorna_87f077 -> Sujeto_rol_alcance_capmin: sin mención
idx 13867: aplica_a Obligacion_la_entidad_financiera_que_haya_rechazado_cheques_sin_haber_percibido_en_tiempo_y_9561ca -> Sujeto_banco: sin mención
idx 13869: aplica_a Obligacion_la_entidad_financiera_receptora_de_la_transferencia_debera_verificar_que_la_cuen_013060 -> Sujeto_banco: sin mención
idx 13871: aplica_a Obligacion_la_entidad_financiera_se_debe_abstener_de_crear_en_ocasion_de_la_emision_de_acci_20b6fb -> Sujeto_rol_alcance_capmin: sin mención
idx 13873: aplica_a Obligacion_la_entidad_financiera_y_los_funcionarios_designados_conforme_al_punto_1_4_seran__1249e1 -> Sujeto_rol_alcance_pagjub: sin mención
idx 13883: aplica_a Obligacion_la_entidad_girada_debera_certificar_que_la_numeracion_de_los_instrumentos_corres_c7f1c3 -> Sujeto_entidad_girada: sin mención
idx 13886: aplica_a Obligacion_la_entidad_girada_devolvera_el_cheque_al_presentante_beneficiario_del_instrument_f1368e -> Sujeto_entidad_girada: sin mención
idx 13888: aplica_a Obligacion_la_entidad_girada_procedera_a_la_pertinente_registracion_una_vez_superadas_tales_1d7d8e -> Sujeto_entidad_girada: sin mención
idx 13890: aplica_a Obligacion_la_entidad_girada_procedera_al_rechazo_por_defecto_formal_de_cada_uno_de_los_che_a9f5b6 -> Sujeto_entidad_girada: sin mención
idx 13893: aplica_a Obligacion_la_entidad_girada_producira_la_pertinente_informacion_al_bcra_conforme_al_regime_e148f8 -> Sujeto_entidad_girada: sin mención
idx 13895: aplica_a Obligacion_la_entidad_girada_que_rechace_la_registracion_procedera_a_hacer_constar_tal_dete_a9a1ee -> Sujeto_entidad_girada: sin mención
idx 13897: aplica_a Obligacion_la_entidad_girada_verificara_la_existencia_de_defectos_en_la_creacion_del_instru_4a44e5 -> Sujeto_entidad_girada: sin mención
idx 13899: aplica_a Obligacion_la_entidad_ha_constatado_en_el_sistema_online_implementado_a_tal_efecto_que_lo_d_69dd10 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13901: aplica_a Obligacion_la_entidad_ha_registrado_la_operacion_en_el_sistema_online_implementado_a_tal_ef_aaa486 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13905: aplica_a Obligacion_la_entidad_interviniente_debe_contar_con_una_declaracion_jurada_del_exportador_e_3e6e06 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13907: aplica_a Obligacion_la_entidad_interviniente_debera_adicionalmente_contar_con_una_declaracion_jurada_6ae8af -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13909: aplica_a Obligacion_la_entidad_interviniente_debera_constatar_el_caracter_genuino_de_la_operacion_y__08a942 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13912: aplica_a Obligacion_la_entidad_interviniente_debera_contar_con_documentacion_en_la_que_conste_explic_6adcfe -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13914: aplica_a Obligacion_la_entidad_interviniente_debera_contar_con_documentacion_en_la_que_conste_explic_f31030 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13917: aplica_a Obligacion_la_entidad_interviniente_debera_contar_con_una_certificacion_de_la_entidad_encar_bb92e8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13919: aplica_a Obligacion_la_entidad_interviniente_debera_contar_con_una_declaracion_jurada_del_cliente_en_e2222e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13921: aplica_a Obligacion_la_entidad_interviniente_debera_intervenir_la_documentacion_aduanera_por_los_pag_424eeb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13923: aplica_a Obligacion_la_entidad_interviniente_debera_intervenir_la_documentacion_aduanera_por_los_pag_8579ee -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13925: aplica_a Obligacion_la_entidad_interviniente_debera_intervenir_la_documentacion_aduanera_por_los_pag_a7d248 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13927: aplica_a Obligacion_la_entidad_interviniente_debera_requerir_al_importador_una_declaracion_jurada_en_307a44 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13929: aplica_a Obligacion_la_entidad_interviniente_debera_requerir_una_declaracion_jurada_del_exportador_r_79d173 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13931: aplica_a Obligacion_la_entidad_interviniente_haya_verificado_que_el_endeudamiento_cuyo_servicio_sera_b6552e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13934: aplica_a Obligacion_la_entidad_nominada_debera_registrar_en_el_sepaimpo_la_baja_del_valor_correspond_353a7e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13936: aplica_a Obligacion_la_entidad_nominada_debera_tomar_registro_de_los_montos_de_los_beneficios_recono_f3ef6e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13938: aplica_a Obligacion_la_entidad_nominada_por_el_exportador_para_el_seguimiento_de_este_mecanismo_ante_9fb939 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13940: aplica_a Obligacion_la_entidad_nominada_por_el_importador_es_la_responsable_de_verificar_el_cumplimi_74285d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13942: aplica_a Obligacion_la_entidad_nominada_por_el_importador_para_el_seguimiento_de_la_oficializacion_d_f82988 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13944: aplica_a Obligacion_la_entidad_nominada_por_un_exportador_debera_notificar_al_bcra_mediante_nota_dir_42b09f -> Sujeto_entidad_financiera: sin mención
idx 13946: aplica_a Obligacion_la_entidad_nominada_registrara_en_los_siguientes_365_trescientos_sesenta_y_cinco_40cb9a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13957: aplica_a Obligacion_la_entidad_nominada_tendra_acceso_a_informacion_detallada_que_le_permita_cumplim_ae18c5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13961: aplica_a Obligacion_la_entidad_por_la_cual_se_curso_el_pago_sera_la_entidad_encargada_de_dicho_segui_916fe5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13963: aplica_a Obligacion_la_entidad_previa_debera_remitir_a_la_nueva_entidad_el_detalle_de_las_certificac_6ec574 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13965: aplica_a Obligacion_la_entidad_previa_le_haya_remitido_el_detalle_de_las_certificaciones_emitidas_a__dad708 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 13967: aplica_a Obligacion_la_entidad_proveedora_debera_calcular_su_exigencia_de_capital_como_si_mantuviera_29ff75 -> Sujeto_rol_alcance_capmin: sin mención
idx 13979: aplica_a Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debera_co_17943c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14002: aplica_a Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debera_co_49e6af -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14004: aplica_a Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debera_co_89edad -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14027: aplica_a Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debera_co_cdc694 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14050: aplica_a Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debera_co_e000c5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14052: aplica_a Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debera_co_f29d76 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14054: aplica_a Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debera_ve_4cee7f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14062: aplica_a Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debera_ve_64b92c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14064: aplica_a Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debera_ve_88a075 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14066: aplica_a Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debera_ve_d60472 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14068: aplica_a Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debera_ve_ed8286 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14070: aplica_a Obligacion_la_entidad_que_cursa_el_pago_al_exterior_debera_intervenir_el_documento_aduanero_839d4f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14072: aplica_a Obligacion_la_entidad_que_interviene_adicionalmente_debera_considerar_los_siguientes_elemen_6eaf41 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14074: aplica_a Obligacion_la_entidad_que_posee_la_posicion_de_titulizacion_debera_comprender_en_todo_momen_6e68ae -> Sujeto_rol_alcance_capmin: sin mención
idx 14076: aplica_a Obligacion_la_entidad_receptora_de_la_transferencia_emitira_a_pedido_del_exportador_una_cer_a7d576 -> Sujeto_entidad_receptora: sin mención
idx 14078: aplica_a Obligacion_la_entidad_requerira_con_los_recaudos_que_establezca_que_el_o_los_titulares_de_l_c75902 -> Sujeto_banco: sin mención
idx 14082: aplica_a Obligacion_la_entidad_se_ajustara_al_procedimiento_establecido_en_el_punto_1_4_2_1_en_el_ca_cfb648 -> Sujeto_rol_alcance_capmin: sin mención
idx 14102: aplica_a Obligacion_la_entidad_solicitara_los_dictamenes_profesionales_que_estime_necesarios_para_as_32725c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14104: aplica_a Obligacion_la_entidad_solo_aceptara_cheques_firmados_por_todos_los_titulares__ctacte_12_2_2_a0b0e4 -> Sujeto_banco: sin mención
idx 14107: aplica_a Obligacion_la_entidad_tambien_debera_realizar_la_correspondiente_intervencion_de_la_documen_1ef938 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14109: aplica_a Obligacion_la_entidad_tiene_la_obligacion_de_conservar_los_legajos_con_toda_la_informacion__c34203 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 14111: aplica_a Obligacion_la_entidad_transfiere_a_terceros_el_riesgo_de_credito_asociado_a_las_exposicione_c0b57f -> Sujeto_rol_alcance_capmin: sin mención
idx 14113: aplica_a Obligacion_la_entidad_vendedora_debera_entregar_los_billetes_en_moneda_extranjera_o_acredit_4fed04 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14116: aplica_a Obligacion_la_entidad_vendedora_debera_entregar_los_billetes_o_cheques_de_viajero_en_moneda_a73773 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14119: aplica_a Obligacion_la_entidad_verifique_que_el_cliente_cuenta_por_el_equivalente_al_monto_a_pagar_c_c33728 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14121: aplica_a Obligacion_la_evaluacion_de_la_necesidad_de_efectuar_ajustes_debe_alcanzar_a_todas_las_posi_642c2b -> Sujeto_rol_alcance_capmin: sin mención
idx 14124: aplica_a Obligacion_la_exigencia_computada_basada_en_el_enfoque_estandar_para_la_medicion_de_la_exig_0ca274 -> Sujeto_rol_alcance_capmin: sin mención
idx 14127: aplica_a Obligacion_la_exigencia_de_capital_minimo_que_las_entidades_financieras_deberan_tener_integ_74c602 -> Sujeto_rol_alcance_capmin: sin mención
idx 14129: aplica_a Obligacion_la_exigencia_de_capital_para_hacer_frente_a_un_descalce_de_plazos_de_vencimiento_48d370 -> Sujeto_rol_alcance_capmin: sin mención
idx 14142: aplica_a Obligacion_la_exigencia_de_capital_para_una_posicion_de_titulizacion_se_determinara_teniend_acba06 -> Sujeto_rol_alcance_capmin: sin mención
idx 14144: aplica_a Obligacion_la_exigencia_de_capital_por_el_riesgo_de_tasa_de_interes_se_debera_calcular_resp_fef61a -> Sujeto_rol_alcance_capmin: sin mención
idx 14146: aplica_a Obligacion_la_exigencia_de_capital_por_la_tenencia_de_acciones_se_obtendra_como_la_suma_de__35aa65 -> Sujeto_rol_alcance_capmin: sin mención
idx 14150: aplica_a Obligacion_la_exigencia_de_capital_se_obtendra_como_la_suma_de_los_siguientes_cuatro_compon_f1e10b -> Sujeto_rol_alcance_capmin: sin mención
idx 14152: aplica_a Obligacion_la_exigencia_de_capital_sera_el_8_de_la_posicion_neta_total__cap_6_4_3_624f9d -> Sujeto_rol_alcance_capmin: sin mención
idx 14155: aplica_a Obligacion_la_exigencia_final_rcd_surgira_de_la_sumatoria_de_las_exigencias_ead_informadas__bac6f2 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 14231: aplica_a Obligacion_la_exigencia_final_rcd_surgira_de_la_sumatoria_de_las_exposiciones_al_riesgo_de__86036b -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 14324: aplica_a Obligacion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_de_las_entidades_f_e63bfb -> Sujeto_rol_alcance_capmin: sin mención
idx 14327: aplica_a Obligacion_la_exigencia_por_riesgo_de_credito_de_contraparte_de_las_operaciones_con_derivad_9a19d7 -> Sujeto_rol_alcance_capmin: sin mención
idx 14334: aplica_a Obligacion_la_exigencia_por_riesgo_especifico_se_determinara_por_separado_multiplicando_el__d0df9a -> Sujeto_rol_alcance_capmin: sin mención
idx 14348: aplica_a Obligacion_la_exigencia_se_obtendra_como_la_suma_de_dos_exigencias_calculadas_por_separado__18adab -> Sujeto_rol_alcance_capmin: sin mención
idx 14350: aplica_a Obligacion_la_existencia_de_procedimientos_internos_destinados_a_prevenir_el_uso_indebido_d_78fc18 -> Sujeto_ecai: sin mención
idx 14352: aplica_a Obligacion_la_exposicion_al_riesgo_de_tasa_de_interes_o_de_tipo_de_cambio_del_otro_lado_del_3a573b -> Sujeto_rol_alcance_capmin: sin mención
idx 14367: aplica_a Obligacion_la_exposicion_debida_a_dichas_operaciones_se_calculara_conforme_al_enfoque_estan_432534 -> Sujeto_rol_alcance_capmin: sin mención
idx 14379: aplica_a Obligacion_la_facultad_de_revocacion_debe_ser_informada_al_usuario_en_todo_documento_que_le_7e3786 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 14381: aplica_a Obligacion_la_facultad_de_revocacion_segun_lo_establecido_en_el_apartado_v_del_punto_2_3_1__c750aa -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 14402: aplica_a Obligacion_la_fecha_de_vencimiento_de_la_financiacion_otorgada_debe_ser_compatible_con_los__61fc14 -> Sujeto_entidad_financiera: sin mención
idx 14413: aplica_a Obligacion_la_fecha_de_vencimiento_que_le_corresponde_a_una_exportacion_sera_aquella_result_e8a935 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14416: aplica_a Obligacion_la_firma_en_la_constancia_de_cobro_debe_estar_certificada_por_escribano_publico__0e4a29 -> Sujeto_banco: sin mención
idx 14418: aplica_a Obligacion_la_firma_insertada_en_un_cheque_al_solo_efecto_de_su_cobro_o_deposito_no_constit_1ccec4 -> Sujeto_banco: sin mención
idx 14446: aplica_a Obligacion_la_garantia_depositada_que_no_este_resguardada_en_caso_de_quiebra_debera_ser_con_2a2c91 -> Sujeto_rol_alcance_capmin: sin mención
idx 14472: aplica_a Obligacion_la_garantia_hipotecaria_debera_ser_en_primer_grado_o_cualquiera_sea_su_grado_de__e7b093 -> Sujeto_rol_alcance_capmin: sin mención
idx 14474: aplica_a Obligacion_la_gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros_brindara_dfa46e -> Sujeto_bcra: sin mención
idx 14477: aplica_a Obligacion_la_homogeneidad_de_los_activos_subyacentes_debera_evaluarse_teniendo_en_consider_fbd142 -> Sujeto_rol_alcance_capmin: sin mención
idx 14479: aplica_a Obligacion_la_identificacion_del_cliente_a_nombre_de_quien_sera_registrada_la_operacion_deb_000dfb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14481: aplica_a Obligacion_la_imputacion_del_monto_ingresado_al_cumplimiento_del_permiso_de_embarque_requer_bdd6c2 -> Sujeto_exportador: sin mención
idx 14483: aplica_a Obligacion_la_informacion_a_banco_central_de_la_republica_argentina_bcra_sobre_los_pagos_de_771db4 -> Sujeto_banco: sin mención
idx 14486: aplica_a Obligacion_la_informacion_a_que_refieren_los_puntos_4_1_1_1_a_4_1_1_8_del_presente_regimen__eb6bce -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 14509: aplica_a Obligacion_la_informacion_antes_descripta_debera_ser_registrada_ante_el_repositorio_cuando__3596e6 -> Sujeto_banco: sin mención
idx 14512: aplica_a Obligacion_la_informacion_debera_ser_actualizada_por_parte_de_la_entidad_en_el_mes_de_dicie_077592 -> Sujeto_banco: sin mención
idx 14514: aplica_a Obligacion_la_informacion_declarada_conforme_a_lo_establecido_precedentemente_tendra_caract_da43d1 -> Sujeto_banco: sin mención
idx 14516: aplica_a Obligacion_la_informacion_incorporada_a_esta_base_de_datos_debera_conservarse_por_el_termin_b5a7a2 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 14519: aplica_a Obligacion_la_informacion_necesaria_para_calcular_las_variables_k_sa_w_a_d_k_a_y_k_ssfa_k_a_51a0e5 -> Sujeto_rol_alcance_capmin: sin mención
idx 14521: aplica_a Obligacion_la_informacion_que_surja_del_legajo_unico_financiero_y_economico_establecido_por_47d044 -> Sujeto_banco: sin mención
idx 14525: aplica_a Obligacion_la_informacion_referida_a_estos_documentos_sera_dada_de_baja_cuando_la_entidad_f_360710 -> Sujeto_banco: sin mención
idx 14534: aplica_a Obligacion_la_informacion_sobre_el_indicador_de_negocios_de_los_periodos_anteriores_debe_se_a8b502 -> Sujeto_rol_alcance_capmin: sin mención
idx 14537: aplica_a Obligacion_la_informacion_sobre_los_clientes_alcanzados_debera_ser_presentada_ante_la_arca__bfee75 -> Sujeto_banco: sin mención
idx 14539: aplica_a Obligacion_la_informacion_tendra_frecuencia_mensual_y_se_integrara_con_datos_referidos_al_m_7979fe -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 14541: aplica_a Obligacion_la_informacion_tendra_frecuencia_trimestral_y_se_integrara_con_saldos_al_cierre__1b4200 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 14543: aplica_a Obligacion_la_instrumentacion_de_la_garantia_debera_asegurar_que_la_entidad_tenga_el_derech_51d897 -> Sujeto_rol_alcance_capmin: sin mención
idx 14545: aplica_a Obligacion_la_integracion_se_determinara_en_forma_diaria_de_acuerdo_con_lo_establecido_en_e_a2ba80 -> Sujeto_rol_alcance_capmin: sin mención
idx 14550: aplica_a Obligacion_la_intervencion_de_terceros_debera_estar_prevista_en_el_manual_de_procedimientos_9b6113 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 14552: aplica_a Obligacion_la_liquidacion_de_las_distintas_modalidades_de_incentivos_economicos_al_personal_ee6c57 -> Sujeto_entidad_financiera: sin mención
idx 14556: aplica_a Obligacion_la_maxima_perdida_posible_se_debera_calcular_para_cada_posicion_individual__cap__0d9d1c -> Sujeto_rol_alcance_capmin: sin mención
idx 14558: aplica_a Obligacion_la_mencion_a_incluir_respecto_de_ese_motivo_sera_sin_fondos_suficientes_disponib_434983 -> Sujeto_banco: sin mención
idx 14560: aplica_a Obligacion_la_mencionada_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del__17f7a5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14562: aplica_a Obligacion_la_mencionada_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del__283b1a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14565: aplica_a Obligacion_la_mencionada_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del__375487 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14588: aplica_a Obligacion_la_metodologia_de_evaluacion_de_cada_segmento_del_mercado_debera_previamente_hab_4d4e95 -> Sujeto_ecai: sin mención
idx 14591: aplica_a Obligacion_la_metodologia_debera_haber_estado_sujeta_en_ese_lapso_a_la_comprobacion_riguros_8a44f4 -> Sujeto_ecai: sin mención
idx 14594: aplica_a Obligacion_la_metodologia_utilizada_para_asignar_las_calificaciones_crediticias_debera_ser__348c14 -> Sujeto_ecai: sin mención
idx 14597: aplica_a Obligacion_la_normativa_de_estabilidad_cambiaria_contemplada_en_los_articulos_201_y_205_de__a5039a -> Sujeto_vpu_rigi: sin mención
idx 14599: aplica_a Obligacion_la_nota_debera_contener_como_minimo_copia_del_certificado_de_inversion_para_expo_5543ad -> Sujeto_entidad_financiera: sin mención
idx 14601: aplica_a Obligacion_la_notificacion_de_las_recomendaciones_debera_efectuarse_al_momento_de_la_apertu_54d460 -> Sujeto_banco: sin mención
idx 14604: aplica_a Obligacion_la_nueva_entidad_quedara_habilitada_para_emitir_nuevas_certificaciones_una_vez_q_0799a2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14606: aplica_a Obligacion_la_nueva_entidad_sera_considerada_responsable_una_vez_que_el_cambio_de_entidad_h_13194b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14608: aplica_a Obligacion_la_obligacion_de_consignar_el_numero_de_identificacion_personal_o_cuit_o_cdi_seg_3fe5ec -> Sujeto_banco: sin mención
idx 14610: aplica_a Obligacion_la_opcion_solo_podra_cambiarse_con_un_preaviso_de_6_meses_a_la_superintendencia__3f3640 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 14612: aplica_a Obligacion_la_operacion_se_encuentra_declarada_en_caso_de_corresponder_en_la_ultima_present_3ba036 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14615: aplica_a Obligacion_la_operacion_se_encuentra_declarada_en_caso_de_corresponder_en_la_ultima_present_c19348 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14618: aplica_a Obligacion_la_partida_correspondiente_al_bic_se_informara_por_el_importe_calculado_en_funci_ca58d8 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 14623: aplica_a Obligacion_la_posicion_neta_de_cada_producto_basico_se_convertira_a_pesos_utilizando_su_pre_d66eca -> Sujeto_rol_alcance_capmin: sin mención
idx 14625: aplica_a Obligacion_la_posicion_ponderada_por_delta_se_incorporara_al_calculo_descripto_en_el_punto__ceb8f8 -> Sujeto_rol_alcance_capmin: sin mención
idx 14631: aplica_a Obligacion_la_posicion_ponderada_por_delta_se_incorporara_por_el_metodo_simplificado_confor_a3be97 -> Sujeto_rol_alcance_capmin: sin mención
idx 14647: aplica_a Obligacion_la_presentacion_de_la_rendicion_de_cuentas_debera_efectuarse_hasta_el_quinto_dia_e4fd9a -> Sujeto_rol_alcance_pagjub: sin mención
idx 14649: aplica_a Obligacion_la_presentacion_debe_ser_efectuada_por_el_usuario_su_representante_legal_o_apode_a1cf5e -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 14651: aplica_a Obligacion_la_presentacion_debera_ser_dirigida_a_la_gerencia_principal_de_proteccion_al_usu_06d41c -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 14653: aplica_a Obligacion_la_presentacion_del_instrumento_constitutivo_debidamente_inscripto_de_la_persona_6b3141 -> Sujeto_banco: sin mención
idx 14655: aplica_a Obligacion_la_presente_informacion_sobre_exigencias_se_complementara_con_informacion_relati_71a674 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 14659: aplica_a Obligacion_la_publicacion_de_informes_sobre_los_aspectos_del_gobierno_societario_puede_asis_23623f -> Sujeto_entidad_financiera: sin mención
idx 14661: aplica_a Obligacion_la_recategorizacion_del_deudor_se_efectuara_al_menos_en_la_categoria_inmediata_s_375b81 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 14663: aplica_a Obligacion_la_reevaluacion_debera_realizarse_dentro_de_los_tres_meses_respecto_de_los_demas_255252 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 14666: aplica_a Obligacion_la_reevaluacion_debera_ser_inmediata_cuando_se_trate_de_clientes_cuyas_financiac_258d94 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 14670: aplica_a Obligacion_la_rendicion_de_cuentas_debera_presentarse_en_la_gerencia_de_cuentas_corrientes__b39607 -> Sujeto_rol_alcance_pagjub: sin mención
idx 14672: aplica_a Obligacion_la_resolucion_de_la_presentacion_debera_ser_notificada_por_escrito_al_usuario_de_a449e0 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 14674: aplica_a Obligacion_la_responsabilidad_de_una_entidad_financiera_surge_de_su_eventual_caracter_de_be_326f19 -> Sujeto_banco: sin mención
idx 14676: aplica_a Obligacion_la_responsabilidad_patrimonial_computable_se_determinara_en_funcion_de_los_saldo_105bcf -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 14679: aplica_a Obligacion_la_revision_debera_efectuarse_como_minimo_con_la_periodicidad_que_se_indica_segu_688f86 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 14681: aplica_a Obligacion_la_revision_debera_estar_concluida_antes_de_presentarse_a_la_superintendencia_de_8b2670 -> Sujeto_sefyc: sin mención
idx 14683: aplica_a Obligacion_la_sefyc_debera_expedirse_dentro_de_los_30_dias_corridos_siguientes_a_la_present_364083 -> Sujeto_sefyc: sin mención
idx 14695: aplica_a Obligacion_la_superintendencia_de_entidades_financieras_y_cambiarias_tendra_en_cuenta_las_p_393d70 -> Sujeto_sefyc: sin mención
idx 14698: aplica_a Obligacion_la_tarea_de_clasificacion_podra_ser_encomendada_a_un_area_independiente_del_sect_5f5232 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 14706: aplica_a Obligacion_la_totalidad_de_los_fondos_obtenidos_debera_aplicarse_en_un_plazo_de_120_ciento__edbff7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14708: aplica_a Obligacion_la_utilizacion_de_este_mecanismo_debera_resultar_neutral_en_materia_fiscal__ext__0db4ba -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14710: aplica_a Obligacion_la_valuacion_se_debera_hacer_a_mercado_siempre_que_sea_posible__cap_6_10_1_2_3d5e31 -> Sujeto_rol_alcance_capmin: sin mención
idx 14713: aplica_a Obligacion_la_venta_de_las_divisas_es_cursada_con_debito_en_cuentas_del_cliente_en_entidade_c786b9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14715: aplica_a Obligacion_la_venta_de_las_divisas_sera_cursada_con_debito_en_cuentas_del_cliente_en_entida_58483b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14718: aplica_a Obligacion_la_venta_de_moneda_extranjera_liquidada_por_el_cliente_debera_ser_registrada_ant_2e999b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14720: aplica_a Obligacion_la_verificacion_del_cumplimiento_de_las_politicas_y_procedimientos_debera_estar__654bab -> Sujeto_rol_alcance_capmin: sin mención
idx 14722: aplica_a Obligacion_las_acciones_conducentes_a_regularizar_los_defectos_de_integracion_diaria_que_su_520e00 -> Sujeto_rol_alcance_capmin: sin mención
idx 14724: aplica_a Obligacion_las_afectaciones_con_imputacion_a_un_pago_deberan_ser_incorporadas_en_el_sepaimp_670e37 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14726: aplica_a Obligacion_las_altas_comisiones_de_nuevos_productos_y_o_servicios_que_deseen_comercializar__6d9dcf -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 14727: aplica_a Obligacion_las_altas_comisiones_de_nuevos_productos_y_o_servicios_que_deseen_comercializar__6d9dcf -> Sujeto_entidad_financiera: sin mención
idx 14728: aplica_a Obligacion_las_altas_comisiones_de_nuevos_productos_y_o_servicios_que_deseen_comercializar__6d9dcf -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 14729: aplica_a Obligacion_las_altas_comisiones_de_nuevos_productos_y_o_servicios_que_deseen_comercializar__6d9dcf -> Sujeto_pspcp: sin mención
idx 14732: aplica_a Obligacion_las_altas_comisiones_de_nuevos_productos_y_o_servicios_que_deseen_comercializar__a09832 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 14733: aplica_a Obligacion_las_altas_comisiones_de_nuevos_productos_y_o_servicios_que_deseen_comercializar__a09832 -> Sujeto_entidad_financiera: sin mención
idx 14734: aplica_a Obligacion_las_altas_comisiones_de_nuevos_productos_y_o_servicios_que_deseen_comercializar__a09832 -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 14735: aplica_a Obligacion_las_altas_comisiones_de_nuevos_productos_y_o_servicios_que_deseen_comercializar__a09832 -> Sujeto_pspcp: sin mención
idx 14737: aplica_a Obligacion_las_boletas_deberan_contener_sello_de_la_casa_receptora__ctacte_2_1_1_6_a5e7c1 -> Sujeto_banco: sin mención
idx 14739: aplica_a Obligacion_las_bonificaciones_convenidas_las_condiciones_para_su_aplicacion_y_su_plazo_de_v_26457c -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 14741: aplica_a Obligacion_las_casas_y_agencias_de_cambio_inscriptas_antes_del_01_09_19_y_que_no_hubieran_o_5fad09 -> Sujeto_agencia_de_cambio: sin mención
idx 14742: aplica_a Obligacion_las_casas_y_agencias_de_cambio_inscriptas_antes_del_01_09_19_y_que_no_hubieran_o_5fad09 -> Sujeto_casa_de_cambio: sin mención
idx 14745: aplica_a Obligacion_las_citadas_declaraciones_juradas_y_la_documentacion_respaldatoria_que_podran_se_72ac9e -> Sujeto_banco: sin mención
idx 14747: aplica_a Obligacion_las_clausulas_del_contrato_deben_ser_comprensibles_y_autosuficientes_teniendo_po_f71d9c -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 14749: aplica_a Obligacion_las_coberturas_que_no_sean_admisibles_para_cva_deberan_recibir_el_mismo_tratamie_cf517c -> Sujeto_rol_alcance_capmin: sin mención
idx 14765: aplica_a Obligacion_las_comisiones_y_los_cargos_asociados_al_producto_o_servicio_y_el_mecanismo_para_2af4e1 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 14781: aplica_a Obligacion_las_companias_financieras_que_realicen_en_forma_directa_operaciones_de_comercio__6b934a -> Sujeto_compania_financiera: sin mención
idx 14784: aplica_a Obligacion_las_conclusiones_de_la_verificacion_del_cumplimiento_deberan_volcarse_semestralm_2d31ad -> Sujeto_banco: sin mención
idx 14789: aplica_a Obligacion_las_conclusiones_seran_volcadas_semestralmente_en_un_informe_especial_conforme_a_d8c729 -> Sujeto_banco: sin mención
idx 14791: aplica_a Obligacion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid_e632c6 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 14793: aplica_a Obligacion_las_consultas_y_o_reclamos_que_para_su_respuesta_al_cliente_requieren_del_analis_c9c78e -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 14795: aplica_a Obligacion_las_contrapartes_deberan_encuadrarse_en_alguno_de_los_siguientes_grados__cap_2_6_af4ac2 -> Sujeto_rol_alcance_capmin: sin mención
idx 14797: aplica_a Obligacion_las_cuentas_corrientes_deberan_contar_con_el_uso_de_cheques__ctacte_1_2_b4eaf5 -> Sujeto_banco: sin mención
idx 14800: aplica_a Obligacion_las_cuotas_deberan_tener_frecuencia_mensual_en_ambos_casos_sistema_frances_y_ale_307ebc -> Sujeto_entidad_financiera: sin mención
idx 14804: aplica_a Obligacion_las_decisiones_que_adopte_deben_ser_compatibles_con_la_evaluacion_de_la_situacio_f0027e -> Sujeto_entidad_financiera: sin mención
idx 14806: aplica_a Obligacion_las_disposiciones_de_esta_seccion_seran_de_aplicacion_para_las_entidades_financi_ad8469 -> Sujeto_entidad_financiera: sin mención
idx 14810: aplica_a Obligacion_las_distintas_consultas_o_pedidos_de_conformidad_previa_que_realicen_los_cliente_bc3eea -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14812: aplica_a Obligacion_las_ecai_deberan_contar_con_recursos_suficientes_para_poder_realizar_evaluacione_13d684 -> Sujeto_ecai: sin mención
idx 14814: aplica_a Obligacion_las_ecai_deberan_cumplir_cada_uno_de_los_siguientes_seis_criterios__cap_10_2_2_38efe2 -> Sujeto_ecai: sin mención
idx 14816: aplica_a Obligacion_las_ecai_deberan_divulgar_el_caracter_general_de_sus_acuerdos_de_remuneracion_co_954e6c -> Sujeto_ecai: sin mención
idx 14818: aplica_a Obligacion_las_ecai_deberan_divulgar_las_tasas_de_incumplimiento_efectivamente_registradas__e831a5 -> Sujeto_ecai: sin mención
idx 14820: aplica_a Obligacion_las_ecai_deberan_divulgar_su_codigo_de_conducta__cap_10_2_2_4_9c81c1 -> Sujeto_ecai: sin mención
idx 14822: aplica_a Obligacion_las_ecai_deberan_divulgar_sus_metodos_de_evaluacion_incluida_la_definicion_de_in_7d0c1e -> Sujeto_ecai: sin mención
idx 14824: aplica_a Obligacion_las_empresas_administradoras_de_las_redes_de_cajeros_automaticos_y_las_entidades_fa3f0b -> Sujeto_entidad_financiera: sin mención
idx 14828: aplica_a Obligacion_las_empresas_no_financieras_emisoras_de_tarjetas_de_credito_y_o_compra_y_los_otr_07405c -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 14829: aplica_a Obligacion_las_empresas_no_financieras_emisoras_de_tarjetas_de_credito_y_o_compra_y_los_otr_07405c -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 14833: aplica_a Obligacion_las_entidades_aceptaran_en_todos_los_casos_los_cheques_librados_por_la_persona_a_577d82 -> Sujeto_banco: sin mención
idx 14837: aplica_a Obligacion_las_entidades_adoptaran_las_medidas_que_aseguren_el_estricto_cumplimiento_de_las_111e7b -> Sujeto_banco: sin mención
idx 14839: aplica_a Obligacion_las_entidades_adoptaran_las_medidas_que_aseguren_el_estricto_cumplimiento_de_las_132a31 -> Sujeto_banco: sin mención
idx 14841: aplica_a Obligacion_las_entidades_aplicaran_parametros_validos_para_cada_sector_y_consideraran_otras_9de00d -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 14843: aplica_a Obligacion_las_entidades_cambiarias_deberan_suspender_sus_operaciones_en_caso_de_encontrars_097a05 -> Sujeto_entidad_cambiaria: sin mención
idx 14846: aplica_a Obligacion_las_entidades_certificaran_que_los_datos_senalados_en_la_nota_de_presentacion_so_946160 -> Sujeto_rol_alcance_pagjub: sin mención
idx 14851: aplica_a Obligacion_las_entidades_conservaran_la_copia_de_las_tareas_realizadas_en_el_legajo_del_cli_aaea92 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14853: aplica_a Obligacion_las_entidades_consultaran_la_central_de_cuentacorrentistas_inhabilitados_que_adm_d02831 -> Sujeto_banco: sin mención
idx 14856: aplica_a Obligacion_las_entidades_deben_cumplir_con_los_limites_minimos_establecidos_para_apr_la_fal_0448b0 -> Sujeto_rol_alcance_capmin: sin mención
idx 14858: aplica_a Obligacion_las_entidades_deben_establecer_procedimientos_para_determinar_la_necesidad_de_re_341be4 -> Sujeto_rol_alcance_capmin: sin mención
idx 14861: aplica_a Obligacion_las_entidades_deben_incluir_y_reportar_el_codigo_70100000_conforme_al_calculo_es_cfcdca -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 14864: aplica_a Obligacion_las_entidades_deben_rechazar_cheques_cuando_existe_una_orden_judicial_incluyendo_ba53ca -> Sujeto_banco: sin mención
idx 14867: aplica_a Obligacion_las_entidades_deben_utilizar_politicas_procedimientos_y_procesos_adecuados_para__e8388f -> Sujeto_rol_alcance_capmin: sin mención
idx 14869: aplica_a Obligacion_las_entidades_deberan_acompanar_el_registro_de_firmas_de_los_funcionarios_design_576474 -> Sujeto_rol_alcance_pagjub: sin mención
idx 14871: aplica_a Obligacion_las_entidades_deberan_adoptar_los_recaudos_necesarios_a_efectos_de_evitar_que_se_5726d4 -> Sujeto_banco: sin mención
idx 14873: aplica_a Obligacion_las_entidades_deberan_adoptar_normas_y_procedimientos_internos_tendientes_a_evit_68c61b -> Sujeto_banco: sin mención
idx 14875: aplica_a Obligacion_las_entidades_deberan_aplicar_un_ajuste_por_apalancamiento_al_requisito_de_capit_365dcb -> Sujeto_rol_alcance_capmin: sin mención
idx 14877: aplica_a Obligacion_las_entidades_deberan_calcular_el_requerimiento_de_capital_por_riesgo_de_credito_68b9a1 -> Sujeto_rol_alcance_capmin: sin mención
idx 14893: aplica_a Obligacion_las_entidades_deberan_calcular_la_exigencia_de_capital_por_cada_posicion_neta_en_fe848c -> Sujeto_rol_alcance_capmin: sin mención
idx 14896: aplica_a Obligacion_las_entidades_deberan_cerrar_esas_cuentas_aun_en_las_que_figuren_con_otros_titul_3ec164 -> Sujeto_banco: sin mención
idx 14900: aplica_a Obligacion_las_entidades_deberan_confeccionar_boletos_de_cambio_a_nombre_propio_cuando_corr_b1fb4c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14903: aplica_a Obligacion_las_entidades_deberan_confeccionar_boletos_de_cambio_a_nombre_propio_cuando_las__942216 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14905: aplica_a Obligacion_las_entidades_deberan_confeccionar_boletos_de_cambio_a_nombre_propio_cuando_las__e49ec9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14908: aplica_a Obligacion_las_entidades_deberan_considerar_la_realidad_o_finalidad_economica_de_la_transac_bed37f -> Sujeto_rol_alcance_capmin: sin mención
idx 14910: aplica_a Obligacion_las_entidades_deberan_constatar_fehacientemente_que_las_personas_comprendidas_no_044d79 -> Sujeto_banco: sin mención
idx 14913: aplica_a Obligacion_las_entidades_deberan_constatar_fehacientemente_que_las_personas_comprendidas_no_2ac48a -> Sujeto_banco: sin mención
idx 14916: aplica_a Obligacion_las_entidades_deberan_constatar_que_las_personas_no_hayan_incurrido_en_falta_de__1a6edf -> Sujeto_banco: sin mención
idx 14919: aplica_a Obligacion_las_entidades_deberan_consultar_en_el_apartado_regimen_informativo_sepaimpo_del__81f4e5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14922: aplica_a Obligacion_las_entidades_deberan_consultar_en_el_apartado_regimen_informativo_sepaimpo_del__e32320 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 14924: aplica_a Obligacion_las_entidades_deberan_contar_con_estrategias_politicas_practicas_y_procedimiento_ae8279 -> Sujeto_entidad_financiera: sin mención
idx 14926: aplica_a Obligacion_las_entidades_deberan_contar_con_opinion_legal_escrita_y_fundada_que_concluya_qu_90e74f -> Sujeto_rol_alcance_capmin: sin mención
idx 14982: aplica_a Obligacion_las_entidades_deberan_contar_con_politicas_y_procedimientos_claramente_definidos_5548a9 -> Sujeto_rol_alcance_capmin: sin mención
idx 14984: aplica_a Obligacion_las_entidades_deberan_contar_con_politicas_y_procedimientos_claramente_definidos_85103d -> Sujeto_rol_alcance_capmin: sin mención
idx 14987: aplica_a Obligacion_las_entidades_deberan_contar_con_procedimientos_para_asegurar_que_las_caracteris_4b4860 -> Sujeto_rol_alcance_capmin: sin mención
idx 15043: aplica_a Obligacion_las_entidades_deberan_contar_con_procedimientos_que_permitan_informar_al_benefic_ba6869 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15045: aplica_a Obligacion_las_entidades_deberan_cumplimentar_los_requisitos_complementarios_que_constan_en_747b1d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15047: aplica_a Obligacion_las_entidades_deberan_cumplimentar_los_requisitos_complementarios_que_constan_en_c8002b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15049: aplica_a Obligacion_las_entidades_deberan_cumplimentar_los_requisitos_previstos_en_la_ley_25_326_de__23922b -> Sujeto_banco: sin mención
idx 15051: aplica_a Obligacion_las_entidades_deberan_cumplir_con_las_normas_sobre_prevencion_del_lavado_de_acti_8bf54d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15053: aplica_a Obligacion_las_entidades_deberan_cumplir_con_lo_establecido_en_el_punto_1_1_para_la_integra_c862d4 -> Sujeto_rol_alcance_capmin: sin mención
idx 15057: aplica_a Obligacion_las_entidades_deberan_cumplir_con_los_restantes_requisitos_normativos_aplicables_0ea5b6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15059: aplica_a Obligacion_las_entidades_deberan_cumplir_con_todos_los_requisitos_legales_necesarios_a_fin__fceb33 -> Sujeto_rol_alcance_capmin: sin mención
idx 15061: aplica_a Obligacion_las_entidades_deberan_dar_al_cliente_la_opcion_de_extender_el_numero_de_cuotas_o_bd6f73 -> Sujeto_entidad_financiera: sin mención
idx 15063: aplica_a Obligacion_las_entidades_deberan_dar_cumplimiento_a_los_requisitos_de_identificacion_de_sus_08d3e7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15065: aplica_a Obligacion_las_entidades_deberan_demostrar_al_bcra_que_cuentan_con_un_contrato_o_acuerdo_de_777f0e -> Sujeto_rol_alcance_capmin: sin mención
idx 15121: aplica_a Obligacion_las_entidades_deberan_dentro_de_los_cinco_5_dias_habiles_de_finalizado_el_tramit_6faeb5 -> Sujeto_entidad_financiera: sin mención
idx 15127: aplica_a Obligacion_las_entidades_deberan_desarrollar_implementar_y_mejorar_sistemas_para_realizar_u_52880b -> Sujeto_rol_alcance_capmin: sin mención
idx 15130: aplica_a Obligacion_las_entidades_deberan_documentar_si_pueden_transferir_el_riesgo_o_las_exposicion_449ab8 -> Sujeto_rol_alcance_capmin: sin mención
idx 15132: aplica_a Obligacion_las_entidades_deberan_emplear_el_metodo_de_medicion_estandar_previsto_en_el_punt_45887c -> Sujeto_rol_alcance_capmin: sin mención
idx 15135: aplica_a Obligacion_las_entidades_deberan_evaluar_explicitamente_la_necesidad_de_ajustar_la_valuacio_b35c85 -> Sujeto_rol_alcance_capmin: sin mención
idx 15138: aplica_a Obligacion_las_entidades_deberan_evaluar_si_corresponde_efectuar_ajustes_por_margenes_sprea_66825c -> Sujeto_rol_alcance_capmin: sin mención
idx 15141: aplica_a Obligacion_las_entidades_deberan_identificar_los_prestamos_interfinancieros_e_informar_esa__c239ae -> Sujeto_entidad_financiera: sin mención
idx 15143: aplica_a Obligacion_las_entidades_deberan_incorporar_los_datos_de_identificacion_del_cliente_en_el_s_3a5fe5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15145: aplica_a Obligacion_las_entidades_deberan_informar_opciones_indicando_descripcion_del_activo_subyace_213adc -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 15147: aplica_a Obligacion_las_entidades_deberan_informar_todo_otro_tipo_de_compromiso_con_las_ccp_y_su_nat_c297da -> Sujeto_rol_alcance_capmin: sin mención
idx 15150: aplica_a Obligacion_las_entidades_deberan_optar_por_un_unico_metodo_para_la_aplicacion_de_la_tecnica_b7cce4 -> Sujeto_rol_alcance_capmin: sin mención
idx 15152: aplica_a Obligacion_las_entidades_deberan_presentar_un_plan_de_regularizacion_y_saneamiento_dentro_d_c2fe9d -> Sujeto_rol_alcance_capmin: sin mención
idx 15172: aplica_a Obligacion_las_entidades_deberan_proveer_evidencia_de_que_permanentemente_vigilan_la_corres_3fe277 -> Sujeto_rol_alcance_capmin: sin mención
idx 15174: aplica_a Obligacion_las_entidades_deberan_realizar_el_correspondiente_boleto_de_venta_dejando_consta_6d4edf -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15176: aplica_a Obligacion_las_entidades_deberan_recabar_previamente_el_consentimiento_del_respectivo_clien_14d4dc -> Sujeto_banco: sin mención
idx 15178: aplica_a Obligacion_las_entidades_deberan_satisfacer_las_exigencias_al_cierre_de_cada_dia_habil__cap_de072b -> Sujeto_rol_alcance_capmin: sin mención
idx 15180: aplica_a Obligacion_las_entidades_deberan_simultaneamente_efectuar_sin_costo_alguno_para_el_cliente__e73a74 -> Sujeto_entidad_financiera: sin mención
idx 15183: aplica_a Obligacion_las_entidades_deberan_tener_implementados_mecanismos_de_seguridad_informatica_qu_0e516f -> Sujeto_banco: sin mención
idx 15186: aplica_a Obligacion_las_entidades_deberan_tener_implementados_mecanismos_de_seguridad_informatica_qu_1cf44b -> Sujeto_banco: sin mención
idx 15188: aplica_a Obligacion_las_entidades_deberan_tener_implementados_mecanismos_de_seguridad_informatica_qu_935751 -> Sujeto_banco: sin mención
idx 15190: aplica_a Obligacion_las_entidades_deberan_verificar_que_el_cliente_liquida_simultaneamente_cobros_an_d643f7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15193: aplica_a Obligacion_las_entidades_deberan_verificar_que_el_cliente_por_el_monto_que_pretende_abonar__00a72a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15195: aplica_a Obligacion_las_entidades_deberan_verificar_si_las_personas_incluidas_en_la_central_de_cuent_719434 -> Sujeto_banco: sin mención
idx 15197: aplica_a Obligacion_las_entidades_del_grupo_a_calcularan_el_componente_adicional_por_las_opciones_au_b48c6c -> Sujeto_banco: sin mención
idx 15199: aplica_a Obligacion_las_entidades_encargadas_del_seguimiento_de_las_oficializaciones_involucradas_en_e12d09 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15201: aplica_a Obligacion_las_entidades_encargadas_del_seguimiento_deberan_cumplimentar_los_reportes_de_in_9d4062 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15203: aplica_a Obligacion_las_entidades_financieras_a_traves_de_sus_responsables_del_area_de_riesgos_deber_fe44e8 -> Sujeto_rol_alcance_capmin: sin mención
idx 15205: aplica_a Obligacion_las_entidades_financieras_calcularan_la_responsabilidad_patrimonial_computable_a_f035bd -> Sujeto_rol_alcance_capmin: sin mención
idx 15207: aplica_a Obligacion_las_entidades_financieras_comprendidas_exclusivamente_sus_casas_en_el_pais_obser_b45f35 -> Sujeto_entidad_financiera: sin mención
idx 15210: aplica_a Obligacion_las_entidades_financieras_comprendidas_sus_filiales_en_el_pais_y_en_el_exterior__659eb7 -> Sujeto_entidad_financiera: sin mención
idx 15212: aplica_a Obligacion_las_entidades_financieras_comprendidas_sus_filiales_en_el_pais_y_en_el_exterior__b0fbca -> Sujeto_entidad_financiera: sin mención
idx 15214: aplica_a Obligacion_las_entidades_financieras_con_significativa_dimension_complejidad_importancia_ec_9c48a3 -> Sujeto_entidad_financiera: sin mención
idx 15216: aplica_a Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_consolidada_observa_356738 -> Sujeto_entidad_financiera: sin mención
idx 15222: aplica_a Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_consolidada_observa_59e7e5 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 15224: aplica_a Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_consolidada_observa_89a55e -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 15226: aplica_a Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_consolidada_observa_c7737c -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 15228: aplica_a Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_consolidada_observa_e5f867 -> Sujeto_sujeto_del_perimetro_consolidado: sin mención
idx 15231: aplica_a Obligacion_las_entidades_financieras_deben_dar_a_conocer_al_publico_de_manera_regular_a_tra_00f2fa -> Sujeto_rol_alcance_capmin: sin mención
idx 15233: aplica_a Obligacion_las_entidades_financieras_deben_dar_a_conocer_al_publico_de_manera_regular_a_tra_0c0ddb -> Sujeto_rol_alcance_capmin: sin mención
idx 15235: aplica_a Obligacion_las_entidades_financieras_deben_dar_a_conocer_al_publico_de_manera_regular_a_tra_fc112f -> Sujeto_rol_alcance_capmin: sin mención
idx 15237: aplica_a Obligacion_las_entidades_financieras_deberan_adoptar_las_medidas_necesarias_para_asegurar_q_90440b -> Sujeto_rol_alcance_capmin: sin mención
idx 15240: aplica_a Obligacion_las_entidades_financieras_deberan_adoptar_los_siguientes_recaudos_en_relacion_co_efcfb2 -> Sujeto_banco: sin mención
idx 15242: aplica_a Obligacion_las_entidades_financieras_deberan_adoptar_procedimientos_tecnologias_y_controles_c6b0a0 -> Sujeto_banco: sin mención
idx 15245: aplica_a Obligacion_las_entidades_financieras_deberan_ajustar_los_valores_de_la_exposicion_y_del_act_f6ff34 -> Sujeto_rol_alcance_capmin: sin mención
idx 15248: aplica_a Obligacion_las_entidades_financieras_deberan_ajustar_su_esquema_de_cobro_de_conceptos_de_tr_525240 -> Sujeto_banco: sin mención
idx 15250: aplica_a Obligacion_las_entidades_financieras_deberan_arbitrar_las_medidas_necesarias_para_identific_90562a -> Sujeto_entidad_financiera: sin mención
idx 15252: aplica_a Obligacion_las_entidades_financieras_deberan_arbitrar_los_medios_necesarios_para_obtener_y__51172a -> Sujeto_banco: sin mención
idx 15255: aplica_a Obligacion_las_entidades_financieras_deberan_arbitrar_los_medios_para_que_en_todos_los_caje_bd528e -> Sujeto_banco: sin mención
idx 15258: aplica_a Obligacion_las_entidades_financieras_deberan_asegurarse_de_que_la_composicion_de_las_exposi_39c820 -> Sujeto_rol_alcance_capmin: sin mención
idx 15264: aplica_a Obligacion_las_entidades_financieras_deberan_como_minimo_tomar_en_consideracion_hasta_que_p_8fc624 -> Sujeto_rol_alcance_capmin: sin mención
idx 15266: aplica_a Obligacion_las_entidades_financieras_deberan_como_minimo_tomar_en_consideracion_lo_siguient_5fe75f -> Sujeto_rol_alcance_capmin: sin mención
idx 15268: aplica_a Obligacion_las_entidades_financieras_deberan_comunicar_a_los_deudores_los_cambios_negativos_2d344b -> Sujeto_entidad_financiera: sin mención
idx 15270: aplica_a Obligacion_las_entidades_financieras_deberan_conservar_constancia_del_ofrecimiento_expreso__798eab -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 15272: aplica_a Obligacion_las_entidades_financieras_deberan_considerar_las_siguientes_definiciones_a_los_f_42c680 -> Sujeto_rol_alcance_capmin: sin mención
idx 15274: aplica_a Obligacion_las_entidades_financieras_deberan_contar_con_procedimientos_claros_y_solidos_que_2555f6 -> Sujeto_rol_alcance_capmin: sin mención
idx 15276: aplica_a Obligacion_las_entidades_financieras_deberan_contar_con_requisitos_adicionales_para_incluir_718558 -> Sujeto_rol_alcance_capmin: sin mención
idx 15278: aplica_a Obligacion_las_entidades_financieras_deberan_cumplir_los_siguientes_requisitos_cuando_admit_6088c8 -> Sujeto_entidad_financiera: sin mención
idx 15281: aplica_a Obligacion_las_entidades_financieras_deberan_demostrar_a_la_sefyc_que_los_ponderadores_de_r_c33a1c -> Sujeto_rol_alcance_capmin: sin mención
idx 15283: aplica_a Obligacion_las_entidades_financieras_deberan_establecer_politicas_para_el_otorgamiento_de_l_9c3ebb -> Sujeto_rol_alcance_capmin: sin mención
idx 15286: aplica_a Obligacion_las_entidades_financieras_deberan_establecer_que_calificaciones_o_categorias_de__3d9030 -> Sujeto_rol_alcance_capmin: sin mención
idx 15289: aplica_a Obligacion_las_entidades_financieras_deberan_identificar_fehacientemente_a_quienes_efectuen_982fea -> Sujeto_banco: sin mención
idx 15292: aplica_a Obligacion_las_entidades_financieras_deberan_informar_la_identidad_de_quien_realice_las_don_59ba0f -> Sujeto_banco: sin mención
idx 15295: aplica_a Obligacion_las_entidades_financieras_deberan_informar_las_ecai_que_utilizan_para_ponderar_e_0ff0fe -> Sujeto_rol_alcance_capmin: sin mención
idx 15297: aplica_a Obligacion_las_entidades_financieras_deberan_mantener_esos_fondos_en_saldos_inmovilizados_a_a8bfe5 -> Sujeto_banco: sin mención
idx 15299: aplica_a Obligacion_las_entidades_financieras_deberan_notificar_al_beneficiario_del_aporte_de_la_sit_071bcb -> Sujeto_banco: sin mención
idx 15301: aplica_a Obligacion_las_entidades_financieras_deberan_observar_los_requisitos_de_divulgacion_en_caso_c4d077 -> Sujeto_rol_alcance_capmin: sin mención
idx 15304: aplica_a Obligacion_las_entidades_financieras_deberan_observar_un_requerimiento_de_capital_adicional_b7f8dd -> Sujeto_rol_alcance_capmin: sin mención
idx 15306: aplica_a Obligacion_las_entidades_financieras_deberan_observar_una_exigencia_de_capital_por_el_riesg_0dbb8f -> Sujeto_rol_alcance_capmin: sin mención
idx 15322: aplica_a Obligacion_las_entidades_financieras_deberan_obtener_en_forma_electronica_y_directa_de_las__255a3f -> Sujeto_banco: sin mención
idx 15324: aplica_a Obligacion_las_entidades_financieras_deberan_obtener_la_constancia_del_cuit_en_forma_electr_b09c40 -> Sujeto_banco: sin mención
idx 15326: aplica_a Obligacion_las_entidades_financieras_deberan_ofrecer_a_sus_clientes_la_posibilidad_de_selec_81ae19 -> Sujeto_entidad_financiera: sin mención
idx 15328: aplica_a Obligacion_las_entidades_financieras_deberan_ofrecer_a_sus_clientes_la_posibilidad_de_selec_ec6232 -> Sujeto_entidad_financiera: sin mención
idx 15330: aplica_a Obligacion_las_entidades_financieras_deberan_ofrecer_la_caja_de_ahorros_en_pesos_con_las_pr_af2a1a -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 15332: aplica_a Obligacion_las_entidades_financieras_deberan_permitir_el_cierre_de_la_cuenta_corriente_en_c_b65914 -> Sujeto_banco: sin mención
idx 15337: aplica_a Obligacion_las_entidades_financieras_deberan_presentar_informacion_sobre_la_operatoria_ante_b43a59 -> Sujeto_banco: sin mención
idx 15340: aplica_a Obligacion_las_entidades_financieras_deberan_prestar_el_servicio_en_el_horario_de_atencion__3044f8 -> Sujeto_rol_alcance_pagjub: sin mención
idx 15342: aplica_a Obligacion_las_entidades_financieras_deberan_realizar_el_seguimiento_necesario_con_el_objet_c7e7b1 -> Sujeto_rol_alcance_capmin: sin mención
idx 15344: aplica_a Obligacion_las_entidades_financieras_deberan_registrar_el_numero_de_inscripcion_en_el_regis_6cb9ed -> Sujeto_banco: sin mención
idx 15346: aplica_a Obligacion_las_entidades_financieras_deberan_suspender_sus_operaciones_en_divisas_en_el_cas_c40294 -> Sujeto_entidad_financiera: sin mención
idx 15349: aplica_a Obligacion_las_entidades_financieras_deberan_tomar_en_consideracion_en_que_medida_las_expos_ee85ba -> Sujeto_rol_alcance_capmin: sin mención
idx 15351: aplica_a Obligacion_las_entidades_financieras_deberan_tomar_en_consideracion_en_que_medida_las_valua_110ffe -> Sujeto_rol_alcance_capmin: sin mención
idx 15353: aplica_a Obligacion_las_entidades_financieras_deberan_verificar_que_los_clientes_cuentan_con_una_cap_24c1fd -> Sujeto_entidad_financiera: sin mención
idx 15355: aplica_a Obligacion_las_entidades_financieras_del_grupo_1_deberan_adoptar_medidas_adecuadas_y_razona_9fa2fd -> Sujeto_rol_alcance_capmin: sin mención
idx 15357: aplica_a Obligacion_las_entidades_financieras_del_grupo_1_deberan_asignar_a_las_exposiciones_denomin_e07d9d -> Sujeto_rol_alcance_capmin: sin mención
idx 15367: aplica_a Obligacion_las_entidades_financieras_del_grupo_1_deberan_clasificar_las_exposiciones_a_inst_2806d2 -> Sujeto_rol_alcance_capmin: sin mención
idx 15370: aplica_a Obligacion_las_entidades_financieras_del_grupo_1_deberan_clasificar_las_exposiciones_a_inst_81a423 -> Sujeto_rol_alcance_capmin: sin mención
idx 15374: aplica_a Obligacion_las_entidades_financieras_del_grupo_1_deberan_clasificar_las_exposiciones_a_inst_bf72ca -> Sujeto_rol_alcance_capmin: sin mención
idx 15377: aplica_a Obligacion_las_entidades_financieras_del_grupo_1_deberan_contar_con_acceso_a_informacion_so_24ba4c -> Sujeto_rol_alcance_capmin: sin mención
idx 15379: aplica_a Obligacion_las_entidades_financieras_del_grupo_1_deberan_contar_con_politicas_procesos_sist_42f2e8 -> Sujeto_rol_alcance_capmin: sin mención
idx 15381: aplica_a Obligacion_las_entidades_financieras_del_grupo_1_deberan_llevar_a_cabo_los_analisis_de_las__498e86 -> Sujeto_rol_alcance_capmin: sin mención
idx 15383: aplica_a Obligacion_las_entidades_financieras_del_grupo_1_deberan_llevar_a_cabo_un_proceso_de_debida_65880c -> Sujeto_rol_alcance_capmin: sin mención
idx 15385: aplica_a Obligacion_las_entidades_financieras_del_grupo_1_deberan_poder_demostrar_a_la_sefyc_que_sus_9d15d6 -> Sujeto_rol_alcance_capmin: sin mención
idx 15387: aplica_a Obligacion_las_entidades_financieras_del_grupo_1_deberan_tener_en_cuenta_la_realidad_econom_70554f -> Sujeto_banco_comercial: sin mención
idx 15389: aplica_a Obligacion_las_entidades_financieras_del_grupo_2_deberan_asignar_a_las_exposiciones_a_sus_c_3a0f7b -> Sujeto_rol_alcance_capmin: sin mención
idx 15392: aplica_a Obligacion_las_entidades_financieras_del_grupo_2_deberan_clasificar_las_exposiciones_a_inst_bc55d7 -> Sujeto_rol_alcance_capmin: sin mención
idx 15395: aplica_a Obligacion_las_entidades_financieras_del_grupo_a_recibiran_el_tratamiento_dispuesto_en_el_p_8c0969 -> Sujeto_entidad_financiera: sin mención
idx 15404: aplica_a Obligacion_las_entidades_financieras_en_funcionamiento_al_01_06_24_deberan_observar_la_exig_ee827f -> Sujeto_rol_alcance_capmin: sin mención
idx 15411: aplica_a Obligacion_las_entidades_financieras_implementaran_efectivamente_en_su_organizacion_un_codi_51d64e -> Sujeto_entidad_financiera: sin mención
idx 15413: aplica_a Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr_36c5b7 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 15414: aplica_a Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr_36c5b7 -> Sujeto_entidad_financiera: sin mención
idx 15415: aplica_a Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr_36c5b7 -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 15417: aplica_a Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr_ad2306 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 15418: aplica_a Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr_ad2306 -> Sujeto_entidad_financiera: sin mención
idx 15419: aplica_a Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr_ad2306 -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 15421: aplica_a Obligacion_las_entidades_financieras_los_pspcp_las_empresas_no_financieras_emisoras_de_tarj_450508 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 15422: aplica_a Obligacion_las_entidades_financieras_los_pspcp_las_empresas_no_financieras_emisoras_de_tarj_450508 -> Sujeto_entidad_financiera: sin mención
idx 15423: aplica_a Obligacion_las_entidades_financieras_los_pspcp_las_empresas_no_financieras_emisoras_de_tarj_450508 -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 15424: aplica_a Obligacion_las_entidades_financieras_los_pspcp_las_empresas_no_financieras_emisoras_de_tarj_450508 -> Sujeto_pspcp: sin mención
idx 15427: aplica_a Obligacion_las_entidades_financieras_los_pspcp_y_los_psi_deberan_promover_la_capacitacion_d_73cabb -> Sujeto_entidad_financiera: sin mención
idx 15428: aplica_a Obligacion_las_entidades_financieras_los_pspcp_y_los_psi_deberan_promover_la_capacitacion_d_73cabb -> Sujeto_psi_billetera_digital: sin mención
idx 15429: aplica_a Obligacion_las_entidades_financieras_los_pspcp_y_los_psi_deberan_promover_la_capacitacion_d_73cabb -> Sujeto_pspcp: sin mención
idx 15432: aplica_a Obligacion_las_entidades_financieras_pagadoras_no_deberan_deducir_del_importe_neto_que_corr_7de865 -> Sujeto_rol_alcance_pagjub: sin mención
idx 15434: aplica_a Obligacion_las_entidades_financieras_que_empleen_este_tipo_de_estructuras_productos_o_instr_e93fcf -> Sujeto_entidad_financiera: sin mención
idx 15436: aplica_a Obligacion_las_entidades_financieras_que_no_cuenten_con_los_datos_sobre_sus_perdidas_anuale_d85ff9 -> Sujeto_rol_alcance_capmin: sin mención
idx 15438: aplica_a Obligacion_las_entidades_financieras_que_ofrezcan_cuentas_a_la_vista_deberan_permitir_que_s_459e51 -> Sujeto_entidad_financiera: sin mención
idx 15441: aplica_a Obligacion_las_entidades_financieras_que_operen_comprando_y_o_vendiendo_cualquiera_sea_su_i_b4d7df -> Sujeto_rol_alcance_capmin: sin mención
idx 15443: aplica_a Obligacion_las_entidades_financieras_que_operen_con_alguno_de_los_tipos_de_cuentas_a_la_vis_6c48ea -> Sujeto_banco: sin mención
idx 15445: aplica_a Obligacion_las_entidades_financieras_que_operen_con_cuentas_a_la_vista_que_admiten_deposito_b73f4a -> Sujeto_banco: sin mención
idx 15447: aplica_a Obligacion_las_entidades_financieras_que_participen_del_servicio_de_pago_de_beneficios_por__42a8a5 -> Sujeto_rol_alcance_pagjub: sin mención
idx 15450: aplica_a Obligacion_las_entidades_financieras_que_pertenezcan_al_grupo_a_cuya_sociedad_controlante_s_598db4 -> Sujeto_rol_alcance_capmin: sin mención
idx 15453: aplica_a Obligacion_las_entidades_financieras_que_sean_miembros_compensadores_aplicaran_un_ponderado_3ee713 -> Sujeto_rol_alcance_capmin: sin mención
idx 15460: aplica_a Obligacion_las_entidades_financieras_requieran_de_su_personal_el_compromiso_de_no_utilizar__10fb55 -> Sujeto_entidad_financiera: sin mención
idx 15462: aplica_a Obligacion_las_entidades_financieras_se_clasificaran_en_grupo_1_y_grupo_2_conforme_a_lo_pre_de9252 -> Sujeto_rol_alcance_capmin: sin mención
idx 15468: aplica_a Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_188b2b -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 15469: aplica_a Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_188b2b -> Sujeto_entidad_financiera: sin mención
idx 15471: aplica_a Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_522d8e -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 15472: aplica_a Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_522d8e -> Sujeto_entidad_financiera: sin mención
idx 15476: aplica_a Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_d71c4a -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 15477: aplica_a Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_d71c4a -> Sujeto_entidad_financiera: sin mención
idx 15480: aplica_a Obligacion_las_entidades_identificaran_en_la_nota_de_presentacion_los_nombres_apellidos_tip_0ff1c8 -> Sujeto_rol_alcance_pagjub: sin mención
idx 15484: aplica_a Obligacion_las_entidades_participantes_deberan_designar_por_lo_menos_dos_funcionarios_respo_34fd11 -> Sujeto_rol_alcance_pagjub: sin mención
idx 15486: aplica_a Obligacion_las_entidades_participantes_que_no_hubieran_efectuado_la_presentacion_de_su_resp_bca80b -> Sujeto_rol_alcance_pagjub: sin mención
idx 15495: aplica_a Obligacion_las_entidades_podran_dar_acceso_al_mercado_de_cambios_para_cursar_pagos_de_servi_27527f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15497: aplica_a Obligacion_las_entidades_por_sus_operaciones_propias_en_caracter_de_cliente_deberan_dar_cum_be9fc5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15527: aplica_a Obligacion_las_entidades_que_no_cumplan_con_la_integracion_de_la_exigencia_basica_de_capita_f022cc -> Sujeto_rol_alcance_capmin: sin mención
idx 15530: aplica_a Obligacion_las_entidades_que_no_cumplan_con_la_obligacion_de_informar_el_pago_de_las_multas_e8c03a -> Sujeto_banco: sin mención
idx 15532: aplica_a Obligacion_las_entidades_que_no_cumplan_con_la_obligacion_de_informar_las_denuncias_de_cheq_97e0e0 -> Sujeto_banco: sin mención
idx 15534: aplica_a Obligacion_las_entidades_que_no_cumplan_con_la_obligacion_de_informar_los_rechazos_o_cancel_1ad67c -> Sujeto_banco: sin mención
idx 15536: aplica_a Obligacion_las_entidades_remitiran_al_bcra_los_archivos_contenidos_en_los_soportes_de_infor_4adace -> Sujeto_rol_alcance_pagjub: sin mención
idx 15540: aplica_a Obligacion_las_entidades_utilizaran_los_datos_rectificados_en_toda_la_documentacion_que_emi_5065be -> Sujeto_entidad_financiera: sin mención
idx 15543: aplica_a Obligacion_las_evaluaciones_de_credito_de_las_ecai_deben_ser_confiables_para_terceros_indep_620774 -> Sujeto_ecai: sin mención
idx 15545: aplica_a Obligacion_las_evaluaciones_deberan_ser_objeto_de_un_control_constante_y_responder_a_los_ca_09ecac -> Sujeto_ecai: sin mención
idx 15548: aplica_a Obligacion_las_evaluaciones_individuales_los_elementos_clave_que_subyacen_a_las_evaluacione_206959 -> Sujeto_ecai: sin mención
idx 15550: aplica_a Obligacion_las_exigencias_de_capital_para_cubrir_los_riesgos_gamma_y_vega_se_calcularan_por_ce6c75 -> Sujeto_rol_alcance_capmin: sin mención
idx 15554: aplica_a Obligacion_las_exigencias_de_capital_se_calcularan_por_separado_para_las_posiciones_en_peso_221e6d -> Sujeto_rol_alcance_capmin: sin mención
idx 15556: aplica_a Obligacion_las_exposiciones_al_sector_publico_no_financiero_de_titulos_publicos_nacionales__9cfee5 -> Sujeto_rol_alcance_capmin: sin mención
idx 15560: aplica_a Obligacion_las_exposiciones_deberan_asignarse_a_los_grados_b_o_c_si_se_verifica_que_la_enti_7541ea -> Sujeto_rol_alcance_capmin: sin mención
idx 15573: aplica_a Obligacion_las_exposiciones_deberan_asignarse_al_grado_c_cuando_la_entidad_financiera_prest_b79999 -> Sujeto_rol_alcance_capmin: sin mención
idx 15575: aplica_a Obligacion_las_exposiciones_deberan_asignarse_al_grado_c_cuando_se_verifique_que_la_entidad_99f4d0 -> Sujeto_rol_alcance_capmin: sin mención
idx 15577: aplica_a Obligacion_las_exposiciones_deberan_instrumentarse_como_financiaciones_rotativas_revolving__aa349c -> Sujeto_rol_alcance_capmin: sin mención
idx 15584: aplica_a Obligacion_las_exposiciones_denominadas_en_moneda_extranjera_pero_cuyo_cobro_de_servicios_s_487830 -> Sujeto_rol_alcance_capmin: sin mención
idx 15587: aplica_a Obligacion_las_exposiciones_incluiran_los_saldos_de_deuda_y_los_compromisos_eventuales_mult_215ac9 -> Sujeto_rol_alcance_capmin: sin mención
idx 15589: aplica_a Obligacion_las_facultades_procedimientos_y_canales_para_la_tramitacion_del_cierre_de_cuenta_1ac1c9 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 15592: aplica_a Obligacion_las_financiaciones_se_imputaran_netas_de_las_previsiones_por_riesgos_de_incobrab_ced863 -> Sujeto_entidad_financiera: sin mención
idx 15595: aplica_a Obligacion_las_financiaciones_y_capacidad_de_prestamo_deberan_ser_computadas_de_acuerdo_con_e883d7 -> Sujeto_entidad_financiera: sin mención
idx 15602: aplica_a Obligacion_las_formulas_de_certificacion_estaran_compuestas_ademas_por_un_talon_que_servira_355125 -> Sujeto_banco: sin mención
idx 15605: aplica_a Obligacion_las_formulas_de_certificacion_observaran_los_mismos_requisitos_sobre_dimension_f_443e60 -> Sujeto_banco: sin mención
idx 15608: aplica_a Obligacion_las_formulas_de_certificacion_seran_debidamente_identificadas_mediante_serie_y_n_4ed60e -> Sujeto_banco: sin mención
idx 15611: aplica_a Obligacion_las_fuentes_de_informacion_y_el_acceso_a_los_datos_asi_como_los_fundamentos_que__100da0 -> Sujeto_rol_alcance_capmin: sin mención
idx 15613: aplica_a Obligacion_las_inhabilitaciones_originadas_en_la_falta_de_pago_de_la_correspondiente_multa__ad5d12 -> Sujeto_banco: sin mención
idx 15615: aplica_a Obligacion_las_inversiones_en_instrumentos_de_capital_que_no_cumplan_con_los_criterios_para_8cfab9 -> Sujeto_rol_alcance_capmin: sin mención
idx 15618: aplica_a Obligacion_las_medidas_de_desempeno_del_personal_que_realiza_tareas_de_control_financiero_y_d16884 -> Sujeto_entidad_financiera: sin mención
idx 15620: aplica_a Obligacion_las_mismas_formalidades_se_requeriran_con_respecto_a_todas_las_personas_que_sean_946170 -> Sujeto_banco: sin mención
idx 15622: aplica_a Obligacion_las_modificaciones_de_la_nomina_de_los_responsables_designados_del_gerente_gener_230f0c -> Sujeto_rol_alcance_capmin: sin mención
idx 15624: aplica_a Obligacion_las_modificaciones_en_las_condiciones_pactadas_incluyendo_el_importe_de_las_comi_c58ecf -> Sujeto_banco: sin mención
idx 15641: aplica_a Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe_0b2584 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 15644: aplica_a Obligacion_las_notificaciones_deberan_efectuarse_mediante_documento_escrito_dirigido_al_dom_f0cc6a -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 15647: aplica_a Obligacion_las_notificaciones_por_cambios_de_condiciones_pactadas_nuevos_conceptos_y_o_valo_ee0add -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 15650: aplica_a Obligacion_las_obligaciones_de_constatar_la_regularidad_de_la_serie_de_endosos_y_verificar__ef9bf3 -> Sujeto_entidad_girada: sin mención
idx 15652: aplica_a Obligacion_las_opciones_sobre_acciones_e_indices_bursatiles_se_incorporaran_a_la_medida_de__a30b4c -> Sujeto_rol_alcance_capmin: sin mención
idx 15654: aplica_a Obligacion_las_opciones_y_sus_subyacentes_deberan_estar_sujetas_a_una_exigencia_de_capital__34fe52 -> Sujeto_rol_alcance_capmin: sin mención
idx 15658: aplica_a Obligacion_las_operaciones_cursadas_quedaran_incorporadas_al_sepaimpo_a_partir_de_su_report_fc2573 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15663: aplica_a Obligacion_las_operaciones_de_cambio_entre_entidades_deberan_ser_realizadas_a_traves_del_si_32988e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15666: aplica_a Obligacion_las_operaciones_de_cambio_seran_realizadas_al_tipo_de_cambio_que_sea_libremente__845633 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15669: aplica_a Obligacion_las_operaciones_de_compraventa_de_titulos_valores_con_liquidacion_en_moneda_extr_7c7d2b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15672: aplica_a Obligacion_las_operaciones_de_pase_estaran_sujetas_a_la_exigencia_de_capital_por_riesgo_de__329272 -> Sujeto_rol_alcance_capmin: sin mención
idx 15680: aplica_a Obligacion_las_operaciones_propias_de_la_entidad_deberan_registrarse_en_la_fecha_en_que_se__3052f0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15683: aplica_a Obligacion_las_operaciones_que_se_pueden_realizar_con_el_producto_o_servicio_de_que_se_trat_4b5642 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 15685: aplica_a Obligacion_las_operaciones_se_computaran_a_partir_de_la_fecha_de_su_concertacion_incluidas__1b7bb6 -> Sujeto_rol_alcance_capmin: sin mención
idx 15687: aplica_a Obligacion_las_participaciones_en_fondos_se_deberan_tratar_de_acuerdo_con_uno_o_mas_de_los__ba6268 -> Sujeto_rol_alcance_capmin: sin mención
idx 15690: aplica_a Obligacion_las_participaciones_minoritarias_que_no_confieren_control_en_poder_de_terceros_e_a771d2 -> Sujeto_rol_alcance_capmin: sin mención
idx 15695: aplica_a Obligacion_las_personas_juridicas_titulares_de_cuentas_corrientes_deben_acreditar_el_objeto_273364 -> Sujeto_banco: sin mención
idx 15697: aplica_a Obligacion_las_personas_juridicas_titulares_de_cuentas_corrientes_deben_acreditar_el_plazo__3c01e2 -> Sujeto_banco: sin mención
idx 15699: aplica_a Obligacion_las_personas_juridicas_titulares_de_cuentas_corrientes_deben_acreditar_la_fecha__41dc5d -> Sujeto_banco: sin mención
idx 15730: aplica_a Obligacion_las_politicas_relativas_a_los_conflictos_de_intereses_la_naturaleza_y_extension__bea4af -> Sujeto_entidad_financiera: sin mención
idx 15733: aplica_a Obligacion_las_politicas_y_procedimientos_deberan_tomar_en_consideracion_la_capacidad_de_la_10cf89 -> Sujeto_rol_alcance_capmin: sin mención
idx 15735: aplica_a Obligacion_las_posiciones_a_termino_en_moneda_extranjera_y_en_oro_se_valuaran_a_los_tipos_d_e8c539 -> Sujeto_rol_alcance_capmin: sin mención
idx 15739: aplica_a Obligacion_las_posiciones_en_los_respectivos_instrumentos_y_los_componentes_de_exigencia_se_960df2 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 15741: aplica_a Obligacion_las_posiciones_imputadas_a_cada_banda_temporal_deberan_ponderarse_por_un_factor__0b1142 -> Sujeto_rol_alcance_capmin: sin mención
idx 15750: aplica_a Obligacion_las_posiciones_ponderadas_deberan_compensarse_compradas_vendidas_dentro_de_cada__39bdae -> Sujeto_rol_alcance_capmin: sin mención
idx 15753: aplica_a Obligacion_las_posiciones_superpuestas_se_ponderaran_de_acuerdo_con_lo_establecido_en_el_pu_1f625d -> Sujeto_rol_alcance_capmin: sin mención
idx 15763: aplica_a Obligacion_las_presentaciones_de_las_entidades_deberan_ser_realizadas_en_la_mesa_de_entrada_861c57 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15765: aplica_a Obligacion_las_presentaciones_que_se_efectuen_deberan_acompanar_un_legajo_especifico_que_co_c821c7 -> Sujeto_banco: sin mención
idx 15767: aplica_a Obligacion_las_previsiones_especificas_asociadas_a_las_posiciones_de_titulizacion_se_consid_1ec487 -> Sujeto_rol_alcance_capmin: sin mención
idx 15776: aplica_a Obligacion_las_principales_decisiones_gerenciales_en_orden_a_las_buenas_practicas_seran_ado_a1ac35 -> Sujeto_entidad_financiera: sin mención
idx 15778: aplica_a Obligacion_las_proporciones_previstas_deben_ser_progresivas_y_aumentar_significativamente_e_a6d2cd -> Sujeto_entidad_financiera: sin mención
idx 15780: aplica_a Obligacion_las_prorrogas_deberan_ser_registradas_por_la_entidad_encargada_del_seguimiento_d_5bb029 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15782: aplica_a Obligacion_las_reducciones_en_las_comisiones_y_o_cargos_deberan_ser_informadas_al_bcra_dent_ae52ec -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 15783: aplica_a Obligacion_las_reducciones_en_las_comisiones_y_o_cargos_deberan_ser_informadas_al_bcra_dent_ae52ec -> Sujeto_entidad_financiera: sin mención
idx 15784: aplica_a Obligacion_las_reducciones_en_las_comisiones_y_o_cargos_deberan_ser_informadas_al_bcra_dent_ae52ec -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 15785: aplica_a Obligacion_las_reducciones_en_las_comisiones_y_o_cargos_deberan_ser_informadas_al_bcra_dent_ae52ec -> Sujeto_pspcp: sin mención
idx 15788: aplica_a Obligacion_las_reglas_de_neteo_offseting_rules_para_riesgo_de_mercado_se_aplicaran_en_base__5ac9d4 -> Sujeto_rol_alcance_capmin: sin mención
idx 15791: aplica_a Obligacion_las_respectivas_posiciones_se_consignaran_en_los_codigos_561000_xx_m_b_compradas_919ad8 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 15809: aplica_a Obligacion_las_retransferencias_de_fondos_a_corresponsales_de_otras_entidades_locales_o_la__c9e12a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15811: aplica_a Obligacion_las_sociedades_de_garantia_reciproca_y_los_fondos_de_garantia_de_caracter_public_e718e9 -> Sujeto_fondo_de_garantia_publico: sin mención
idx 15812: aplica_a Obligacion_las_sociedades_de_garantia_reciproca_y_los_fondos_de_garantia_de_caracter_public_e718e9 -> Sujeto_sociedad_de_garantia_reciproca: sin mención
idx 15818: aplica_a Obligacion_las_titulizaciones_con_periodos_rotativos_deberan_establecer_eventos_de_amortiza_a2ea21 -> Sujeto_rol_alcance_capmin: sin mención
idx 15820: aplica_a Obligacion_las_transferencias_deberan_ser_ordenadas_por_el_cuentacorrentista_cualquiera_sea_b0c468 -> Sujeto_banco: sin mención
idx 15823: aplica_a Obligacion_lo_anterior_debera_establecerse_en_los_instrumentos_que_acuerden_la_realizacion__8410f2 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 15826: aplica_a Obligacion_lo_que_debera_ser_suficientemente_acreditado_por_este_a_satisfaccion_de_la_entid_610647 -> Sujeto_banco: sin mención
idx 15828: aplica_a Obligacion_lo_requerido_respecto_a_las_declaraciones_sira_o_sirase_resulta_aplicable_al_mom_adfb62 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15830: aplica_a Obligacion_los_activos_comprendidos_en_esta_seccion_deben_deducirse_a_los_fines_del_calculo_8ecb6f -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 15832: aplica_a Obligacion_los_activos_subyacentes_deberan_estar_constituidos_por_documentos_a_cobrar_o_der_923a00 -> Sujeto_rol_alcance_capmin: sin mención
idx 15836: aplica_a Obligacion_los_ajustes_al_valor_corriente_de_las_posiciones_menos_liquidas_del_punto_6_10_2_76c0a7 -> Sujeto_rol_alcance_capmin: sin mención
idx 15845: aplica_a Obligacion_los_alcances_y_las_definiciones_referidas_a_sujetos_alcanzados_cuentas_y_datos_a_84bac9 -> Sujeto_banco: sin mención
idx 15847: aplica_a Obligacion_los_analisis_previos_al_otorgamiento_de_financiaciones_y_refinanciaciones_deben__53bf77 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 15850: aplica_a Obligacion_los_anticipos_prefinanciaciones_y_posfinanciaciones_del_exterior_deberan_ser_ing_d77a5a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15852: aplica_a Obligacion_los_aportes_de_titulos_valores_publicos_nacionales_deberan_registrarse_a_su_valo_86b07f -> Sujeto_rol_alcance_capmin: sin mención
idx 15867: aplica_a Obligacion_los_archivos_correspondientes_a_las_ordenes_de_pago_pagadas_e_impagas_se_deberan_899ed6 -> Sujeto_rol_alcance_pagjub: sin mención
idx 15869: aplica_a Obligacion_los_archivos_deberan_tener_las_siguientes_caracteristicas_tipo_de_archivo_ascii__72bbf6 -> Sujeto_rol_alcance_pagjub: sin mención
idx 15871: aplica_a Obligacion_los_aspectos_de_gratuidad_asociados_al_producto_o_servicio_contratado__pro_2_3_1_bcfaaa -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 15874: aplica_a Obligacion_los_aumentos_en_las_comisiones_que_deseen_implementar_deberan_ser_previamente_in_c6e9fc -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 15875: aplica_a Obligacion_los_aumentos_en_las_comisiones_que_deseen_implementar_deberan_ser_previamente_in_c6e9fc -> Sujeto_entidad_financiera: sin mención
idx 15876: aplica_a Obligacion_los_aumentos_en_las_comisiones_que_deseen_implementar_deberan_ser_previamente_in_c6e9fc -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 15877: aplica_a Obligacion_los_aumentos_en_las_comisiones_que_deseen_implementar_deberan_ser_previamente_in_c6e9fc -> Sujeto_pspcp: sin mención
idx 15880: aplica_a Obligacion_los_avisos_deben_incluir_la_fecha_de_emision_como_requisito_comun_de_contenido_m_b77c14 -> Sujeto_banco: sin mención
idx 15882: aplica_a Obligacion_los_avisos_que_corresponda_enviar_a_los_libradores_a_los_titulares_de_cuentas_co_25982f -> Sujeto_banco: sin mención
idx 15884: aplica_a Obligacion_los_bancos_adoptaran_todas_las_medidas_tendientes_a_mantener_a_buen_recaudo_las__ceb77b -> Sujeto_banco: sin mención
idx 15886: aplica_a Obligacion_los_bancos_comerciales_que_ejerzan_la_funcion_de_agente_de_registro_de_letras_hi_11388a -> Sujeto_banco_comercial: sin mención
idx 15888: aplica_a Obligacion_los_bancos_comerciales_que_ejerzan_la_funcion_de_custodia_de_los_titulos_represe_2d81b0 -> Sujeto_banco_comercial: sin mención
idx 15891: aplica_a Obligacion_los_bancos_deberan_alertar_y_recomendar_a_los_usuarios_acerca_de_las_precaucione_00783f -> Sujeto_banco: sin mención
idx 15894: aplica_a Obligacion_los_bancos_deberan_emitir_la_pertinente_constancia_con_los_datos_esenciales_de_l_351eb1 -> Sujeto_banco: sin mención
idx 15896: aplica_a Obligacion_los_bancos_deberan_exponer_en_pizarras_colocadas_en_los_locales_de_atencion_al_p_5116b2 -> Sujeto_banco: sin mención
idx 15899: aplica_a Obligacion_los_bancos_deberan_exponer_informacion_sobre_la_tasa_de_interes_efectiva_anual_q_be2ab7 -> Sujeto_banco: sin mención
idx 15901: aplica_a Obligacion_los_bancos_deberan_exponer_informacion_sobre_las_tasas_de_interes_que_abonen_sob_ea7e1f -> Sujeto_banco: sin mención
idx 15904: aplica_a Obligacion_los_bancos_deberan_mantener_archivada_la_constancia_de_que_el_cliente_ha_recibid_8e2cb6 -> Sujeto_banco: sin mención
idx 15906: aplica_a Obligacion_los_bancos_explicitaran_en_un_manual_de_procedimientos_las_condiciones_que_obser_d14de2 -> Sujeto_banco: sin mención
idx 15908: aplica_a Obligacion_los_beneficiarios_del_radpip_y_o_radpign_deberan_nominar_una_unica_entidad_finan_6060bf -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15916: aplica_a Obligacion_los_boletos_deberan_ser_registrados_en_la_fecha_en_que_se_origino_la_financiacio_028b8d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15918: aplica_a Obligacion_los_boletos_deberan_ser_registrados_en_la_fecha_en_que_se_produjo_el_registro_de_3a5c4b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15920: aplica_a Obligacion_los_calculos_a_nivel_subconsolidado_deben_realizarse_utilizando_las_cifras_del_b_98a1d7 -> Sujeto_rol_alcance_capmin: sin mención
idx 15922: aplica_a Obligacion_los_canales_habilitados_para_la_realizacion_de_reclamos__pro_2_3_1_4_1102c4 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 15931: aplica_a Obligacion_los_certificados_depositados_en_cuenta_o_como_valor_al_cobro_seran_objeto_del_mi_127f94 -> Sujeto_banco: sin mención
idx 15935: aplica_a Obligacion_los_certificados_seran_entregados_al_presentante_del_cheque_de_pago_diferido_baj_0e7785 -> Sujeto_banco: sin mención
idx 15937: aplica_a Obligacion_los_cheques_de_pago_diferido_les_seran_presentados_al_cobro_por_la_avalista_depo_ad63bd -> Sujeto_banco: sin mención
idx 15939: aplica_a Obligacion_los_cheques_presentados_electronicamente_al_cobro_deberan_consignar_en_el_frente_f7ee42 -> Sujeto_banco: sin mención
idx 15941: aplica_a Obligacion_los_citados_flujos_de_fondos_nocionales_futuros_se_asignaran_a_19_bandas_tempora_7affa8 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 15949: aplica_a Obligacion_los_clientes_cuyas_deudas_hayan_sido_refinanciadas_mediante_obligaciones_de_pago_43449c -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 15953: aplica_a Obligacion_los_clientes_de_la_entidad_tanto_residentes_en_el_pais_de_los_sectores_publico_y_8b3c06 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 15955: aplica_a Obligacion_los_clientes_deberan_presentar_la_siguiente_documentacion_respaldatoria__docvig__8cee9b -> Sujeto_cliente: sin mención
idx 15957: aplica_a Obligacion_los_clientes_deberan_proporcionar_informacion_financiera_actualizada_estados_fin_630ca8 -> Sujeto_cliente: sin mención
idx 15959: aplica_a Obligacion_los_cobros_de_exportaciones_de_bienes_y_servicios_anticipos_prefinanciaciones_y__960f05 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15962: aplica_a Obligacion_los_cobros_de_exportaciones_deberan_ser_ingresados_y_liquidados_en_el_mercado_de_ef8210 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15965: aplica_a Obligacion_los_cobros_deberan_ser_ingresadas_y_liquidadas_en_el_mercado_de_cambios_dentro_d_e9e6c7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15968: aplica_a Obligacion_los_cobros_deberan_ser_ingresados_y_liquidados_en_mercado_de_cambios_en_plazo_no_ca7449 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 15974: aplica_a Obligacion_los_componentes_de_la_exigencia_por_riesgo_general_de_tasa_se_calcularan_conform_7c5490 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 15977: aplica_a Obligacion_los_conceptos_que_se_debitaran_de_la_cuenta_corriente_siempre_que_medie_autoriza_517963 -> Sujeto_banco: sin mención
idx 15990: aplica_a Obligacion_los_conjuntos_de_neteo_aplicables_a_las_entidades_financieras_que_actuen_como_mi_d1625c -> Sujeto_rol_alcance_capmin: sin mención
idx 16036: aplica_a Obligacion_los_contratos_como_minimo_deben_contener_la_descripcion_y_especificacion_complet_6b76fe -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16038: aplica_a Obligacion_los_contratos_deben_contener_identificacion_del_usuario_de_servicios_financieros_369eb4 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16040: aplica_a Obligacion_los_contratos_deben_contener_la_razon_social_cuit_y_domicilio_legal_del_sujeto_o_0e73d5 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16042: aplica_a Obligacion_los_contratos_deben_contener_las_comisiones_y_cargos_asi_como_los_terminos_y_con_59f26e -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16044: aplica_a Obligacion_los_contratos_deben_contener_los_restantes_requisitos_normativamente_reglamentad_ee041e -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16046: aplica_a Obligacion_los_contratos_deben_ser_de_clara_redaccion_y_con_tamano_de_tipografia_minimo_de__7b5326 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16048: aplica_a Obligacion_los_controles_internos_deberan_ser_acordes_al_tamano_y_a_la_complejidad_de_la_ac_a8b7ee -> Sujeto_entidad_financiera: sin mención
idx 16050: aplica_a Obligacion_los_correspondientes_cuentacorrentistas_seran_excluidos_de_dicha_central_a_parti_28c5c5 -> Sujeto_banco: sin mención
idx 16052: aplica_a Obligacion_los_creditos_incorporados_por_compras_de_cartera_tendran_el_mismo_tratamiento_qu_56775d -> Sujeto_rol_alcance_capmin: sin mención
idx 16056: aplica_a Obligacion_los_datos_a_que_se_refiere_la_informacion_de_exigencia_por_riesgo_de_credito_se__2f7e78 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 16058: aplica_a Obligacion_los_datos_de_mercado_deberan_proceder_en_la_medida_de_lo_posible_de_las_mismas_f_7ff64e -> Sujeto_rol_alcance_capmin: sin mención
idx 16061: aplica_a Obligacion_los_datos_para_direccionamiento_de_presentaciones_deberan_encontrarse_disponible_000e13 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16063: aplica_a Obligacion_los_datos_se_informaran_con_frecuencia_trimestral_sobre_base_individual_y_consol_ec0697 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 16065: aplica_a Obligacion_los_datos_se_informaran_con_frecuencia_trimestral_y_se_integraran_con_los_datos__5b59da -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 16075: aplica_a Obligacion_los_defectos_de_aplicacion_netos_de_los_saldos_de_efectivo_estaran_sujetos_a_un__6e0af5 -> Sujeto_entidad_financiera: sin mención
idx 16078: aplica_a Obligacion_los_depositos_en_monedas_extranjeras_distintas_al_dolar_estadounidense_seran_con_0c66be -> Sujeto_entidad_financiera: sin mención
idx 16081: aplica_a Obligacion_los_derechos_del_inversor_deberan_estar_claramente_definidos_en_toda_circunstanc_46c71e -> Sujeto_rol_alcance_capmin: sin mención
idx 16083: aplica_a Obligacion_los_derivados_de_credito_que_permitan_la_liquidacion_en_efectivo_seran_reconocid_6f2651 -> Sujeto_rol_alcance_capmin: sin mención
idx 16086: aplica_a Obligacion_los_derivados_se_convertiran_en_posiciones_en_su_correspondiente_subyacente__cap_535f07 -> Sujeto_rol_alcance_capmin: sin mención
idx 16089: aplica_a Obligacion_los_deudores_de_capital_e_intereses_vencidos_con_contrapartes_vinculadas_estan_s_beedd2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16112: aplica_a Obligacion_los_deudores_excluidos_precedentemente_deberan_ser_clasificados_y_sus_deudas_pre_392505 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 16114: aplica_a Obligacion_los_deudores_que_incurran_en_atrasos_de_mas_de_31_dias_respecto_de_las_condicion_71e0db -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 16116: aplica_a Obligacion_los_deudores_que_no_hubieran_cancelado_por_lo_menos_los_intereses_devengados_den_81653c -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 16118: aplica_a Obligacion_los_dictamenes_deberan_ser_complementados_con_dictamenes_sobre_los_aspectos_tecn_c9d29e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16121: aplica_a Obligacion_los_ejemplares_del_contrato_deben_suscribirse_a_un_solo_efecto_y_en_el_acto_de_l_b0d9cb -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16123: aplica_a Obligacion_los_elementos_respaldatorios_y_los_soportes_de_informacion_que_contienen_las_rep_364a2d -> Sujeto_banco: sin mención
idx 16125: aplica_a Obligacion_los_endosos_deberan_ser_extendidos_con_la_clausula_para_su_negociacion_en_mercad_2c7020 -> Sujeto_banco: sin mención
idx 16128: aplica_a Obligacion_los_eventos_de_credito_especificados_por_las_partes_contratantes_deberan_incluir_8e7b89 -> Sujeto_rol_alcance_capmin: sin mención
idx 16131: aplica_a Obligacion_los_exportadores_que_efectuen_liquidaciones_de_moneda_extranjera_asociadas_a_las_7b60fa -> Sujeto_exportador: sin mención
idx 16167: aplica_a Obligacion_los_exportadores_que_opten_por_este_mecanismo_deberan_designar_una_entidad_finan_8ded28 -> Sujeto_exportador: sin mención
idx 16173: aplica_a Obligacion_los_exportadores_que_pretendan_aplicar_estas_operaciones_a_embarques_oficializad_768559 -> Sujeto_exportador: sin mención
idx 16175: aplica_a Obligacion_los_exportadores_que_registren_anticipos_u_otras_financiaciones_de_exportacion_c_01d4da -> Sujeto_exportador: sin mención
idx 16183: aplica_a Obligacion_los_fondos_debitados_indebidamente_por_comisiones_y_o_cargos_deberan_ser_reinteg_30c58f -> Sujeto_banco: sin mención
idx 16186: aplica_a Obligacion_los_fondos_depositados_seran_abonados_contra_la_presentacion_del_respectivo_cart_959212 -> Sujeto_entidad_girada: sin mención
idx 16188: aplica_a Obligacion_los_fondos_en_moneda_extranjera_que_no_se_utilicen_en_la_cancelacion_del_servici_e5fde0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16190: aplica_a Obligacion_los_fondos_excedentes_deben_ser_ingresados_y_liquidados_en_el_mercado_de_cambios_a3c944 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16192: aplica_a Obligacion_los_fondos_excedentes_deberan_ser_ingresados_y_liquidados_en_el_mercado_de_cambi_547475 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16195: aplica_a Obligacion_los_fondos_excedentes_ser_ingresados_y_liquidados_en_el_mercado_de_cambios_dentr_dae142 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16198: aplica_a Obligacion_los_fondos_recibidos_por_los_clientes_en_virtud_de_financiaciones_en_moneda_extr_3bc31d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16200: aplica_a Obligacion_los_fondos_y_su_asignacion_dentro_de_la_entidad_tendran_en_cuenta_el_rango_compl_f46df8 -> Sujeto_entidad_financiera: sin mención
idx 16202: aplica_a Obligacion_los_funcionarios_designados_seran_los_representantes_naturales_de_la_entidad_fre_5fc80f -> Sujeto_rol_alcance_pagjub: sin mención
idx 16204: aplica_a Obligacion_los_fundamentos_de_los_criterios_adoptados_en_el_codigo_de_gobierno_societario_d_eaf5a8 -> Sujeto_entidad_financiera: sin mención
idx 16206: aplica_a Obligacion_los_futuros_sobre_indices_bursatiles_deberan_declararse_al_valor_de_mercado_del__f3459d -> Sujeto_rol_alcance_capmin: sin mención
idx 16208: aplica_a Obligacion_los_futuros_y_forwards_deberan_expresarse_como_cantidades_nocionales_de_barriles_cf9049 -> Sujeto_rol_alcance_capmin: sin mención
idx 16210: aplica_a Obligacion_los_futuros_y_forwards_sobre_acciones_individuales_deberan_declararse_al_precio__611e52 -> Sujeto_rol_alcance_capmin: sin mención
idx 16212: aplica_a Obligacion_los_importes_en_moneda_extranjera_se_convertiran_a_pesos_utilizando_el_tipo_de_c_64bba8 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 16214: aplica_a Obligacion_los_importes_no_retirados_seran_transferidos_a_saldos_inmovilizados__ctacte_9_2__b04ae9 -> Sujeto_banco: sin mención
idx 16216: aplica_a Obligacion_los_importes_por_debajo_del_umbral_que_no_se_deducen_se_ponderan_en_funcion_del__1e4f1d -> Sujeto_rol_alcance_capmin: sin mención
idx 16226: aplica_a Obligacion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales__ric_1_2_f58b33 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 16228: aplica_a Obligacion_los_incentivos_economicos_al_personal_se_vinculen_con_la_contribucion_individual_d08d61 -> Sujeto_entidad_financiera: sin mención
idx 16231: aplica_a Obligacion_los_incentivos_que_se_determinen_mediante_el_sistema_las_medidas_de_riesgo_y_los_b2b2f1 -> Sujeto_entidad_financiera: sin mención
idx 16233: aplica_a Obligacion_los_incentivos_resulten_adecuados_a_su_rol_en_la_organizacion__lingob_6_2_3_381565 -> Sujeto_entidad_financiera: sin mención
idx 16235: aplica_a Obligacion_los_incentivos_se_ajusten_en_funcion_de_todos_los_riesgos_que_toma_el_personal_i_9d417e -> Sujeto_entidad_financiera: sin mención
idx 16237: aplica_a Obligacion_los_incrementos_en_las_tasas_de_interes_comisiones_y_o_cargos_deben_ser_justific_14edca -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16250: aplica_a Obligacion_los_instrumentos_cuyo_rendimiento_se_determine_en_funcion_del_coeficiente_de_est_f0bf8e -> Sujeto_rol_alcance_capmin: sin mención
idx 16253: aplica_a Obligacion_los_instrumentos_derivados_tales_como_futuros_forwards_swaps_y_las_opciones_trat_96130c -> Sujeto_rol_alcance_capmin: sin mención
idx 16262: aplica_a Obligacion_los_instrumentos_imputados_a_la_cartera_de_negociacion_deberan_estar_valuados_en_7f587a -> Sujeto_rol_alcance_capmin: sin mención
idx 16268: aplica_a Obligacion_los_instrumentos_incluidos_en_el_ca_deberan_estar_subordinados_a_depositantes_ac_54af57 -> Sujeto_rol_alcance_capmin: sin mención
idx 16270: aplica_a Obligacion_los_instrumentos_incluidos_en_el_ca_deberan_estar_totalmente_suscriptos_e_integr_cca9d3 -> Sujeto_rol_alcance_capmin: sin mención
idx 16272: aplica_a Obligacion_los_instrumentos_incluidos_en_el_ca_deberan_observar_los_siguientes_requisitos___034256 -> Sujeto_rol_alcance_capmin: sin mención
idx 16274: aplica_a Obligacion_los_instrumentos_incluidos_en_el_pnc_deberan_estar_totalmente_suscriptos_e_integ_17075a -> Sujeto_rol_alcance_capmin: sin mención
idx 16276: aplica_a Obligacion_los_instrumentos_propios_recomprados_que_cumplan_con_los_criterios_para_su_inclu_61c59a -> Sujeto_rol_alcance_capmin: sin mención
idx 16279: aplica_a Obligacion_los_instrumentos_que_son_parte_del_pasivo_deberan_absorber_perdidas_cuando_el_co_92366a -> Sujeto_rol_alcance_capmin: sin mención
idx 16295: aplica_a Obligacion_los_intereses_y_otros_ingresos_devengados_a_cobrar_y_a_pagar_se_incluiran_en_la__84d1a3 -> Sujeto_rol_alcance_capmin: sin mención
idx 16297: aplica_a Obligacion_los_inversores_deberan_ser_notificados_con_la_debida_anticipacion_respecto_de_cu_573728 -> Sujeto_rol_alcance_capmin: sin mención
idx 16304: aplica_a Obligacion_los_mecanismos_a_instrumentar_entre_el_banco_y_sus_clientes_deberan_asegurar_el__f54cca -> Sujeto_banco: sin mención
idx 16305: aplica_a Obligacion_los_mecanismos_a_instrumentar_entre_el_banco_y_sus_clientes_deberan_asegurar_el__f54cca -> Sujeto_cliente: sin mención
idx 16307: aplica_a Obligacion_los_miembros_del_directorio_deberan_contar_con_los_conocimientos_y_competencias__701bc4 -> Sujeto_entidad_financiera: sin mención
idx 16309: aplica_a Obligacion_los_miembros_del_directorio_deberan_obrar_con_lealtad_y_con_la_diligencia_de_un__acb6a2 -> Sujeto_entidad_financiera: sin mención
idx 16311: aplica_a Obligacion_los_montos_de_las_certificaciones_por_los_regimenes_de_acceso_a_divisas_para_la__e7c3f1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16313: aplica_a Obligacion_los_montos_deberan_estar_expresados_en_la_moneda_que_oportunamente_fue_liquidada_b0b7ad -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16315: aplica_a Obligacion_los_movimientos_en_pesos_resultantes_de_la_liquidacion_de_operaciones_de_comprav_9de674 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16318: aplica_a Obligacion_los_niveles_que_intervienen_en_el_analisis_y_decision_en_el_otorgamiento_de_las__ad1f58 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 16320: aplica_a Obligacion_los_pagos_cursados_quedaran_sujetos_a_un_seguimiento_para_verificar_que_se_efect_38fb6e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16323: aplica_a Obligacion_los_pagos_deberan_regirse_por_las_normas_que_sean_aplicables_para_la_cancelacion_35eb49 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16328: aplica_a Obligacion_los_pagos_por_deudas_originadas_en_la_adquisicion_de_servicios_a_no_residentes_q_a6e1fb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16330: aplica_a Obligacion_los_pedidos_al_bcra_deben_ser_canalizados_por_una_entidad_autorizada_a_realizar__c39d32 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16332: aplica_a Obligacion_los_pedidos_de_conformidad_deberan_ser_presentados_ante_el_bcra_exclusivamente_p_49d9d3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16334: aplica_a Obligacion_los_pedidos_para_pago_de_oficializaciones_que_requieran_conformidad_del_bcra_deb_7d080e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16336: aplica_a Obligacion_los_plazos_previstos_en_el_punto_13_2_se_computaran_a_partir_de_la_fecha_estimad_dbbd2d -> Sujeto_entidad_financiera: sin mención
idx 16347: aplica_a Obligacion_los_plazos_previstos_en_el_punto_13_2_se_computaran_desde_la_ultima_fecha_mencio_90ab1f -> Sujeto_entidad_financiera: sin mención
idx 16358: aplica_a Obligacion_los_ponderadores_de_las_bandas_se_aplicaran_sobre_la_posicion_bruta_en_monedas_r_abd3cb -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 16361: aplica_a Obligacion_los_ponderadores_de_riesgo_a_aplicar_a_las_posiciones_de_una_titulizacion_y_a_la_e2297c -> Sujeto_rol_alcance_capmin: sin mención
idx 16364: aplica_a Obligacion_los_ponderadores_de_riesgo_se_aplicaran_por_operacion__cap_2_5_2_092152 -> Sujeto_rol_alcance_capmin: sin mención
idx 16367: aplica_a Obligacion_los_ponderadores_para_las_inversiones_subsiguientes_del_fondo_b_en_el_fondo_c_y__f6df2b -> Sujeto_rol_alcance_capmin: sin mención
idx 16370: aplica_a Obligacion_los_procedimientos_generales_metodologias_y_supuestos_utilizados_por_las_ecai_pa_7da25b -> Sujeto_ecai: sin mención
idx 16372: aplica_a Obligacion_los_procedimientos_implementados_de_manera_que_permita_apreciar_el_proceso_segui_289833 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 16374: aplica_a Obligacion_los_procedimientos_internos_deberan_establecer_mecanismos_de_reporte_al_responsa_c9de59 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16376: aplica_a Obligacion_los_procedimientos_tecnologias_y_controles_utilizados_para_la_apertura_en_forma__941d5d -> Sujeto_banco: sin mención
idx 16379: aplica_a Obligacion_los_procesos_de_monitoreo_y_control_deberan_permitir_la_concatenacion_de_las_ope_e3ec6b -> Sujeto_rol_alcance_lavdin: sin mención
idx 16381: aplica_a Obligacion_los_proveedores_de_servicios_de_creditos_entre_particulares_a_traves_de_platafor_7b1b38 -> Sujeto_pscpp: sin mención
idx 16385: aplica_a Obligacion_los_rechazos_de_cheques_generaran_las_multas_legalmente_establecidas__ctacte_6_5_13b8dc -> Sujeto_banco: sin mención
idx 16396: aplica_a Obligacion_los_rechazos_no_se_comunicaran_unicamente_en_los_casos_en_que_hubiera_sido_posib_6c4c20 -> Sujeto_banco: sin mención
idx 16407: aplica_a Obligacion_los_reportes_deberan_contener_informacion_que_identifique_cualquier_incumplimien_db20aa -> Sujeto_rol_alcance_capmin: sin mención
idx 16409: aplica_a Obligacion_los_reportes_del_directivo_responsable_de_proteccion_de_los_usuarios_de_servicio_175b7e -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16411: aplica_a Obligacion_los_reportes_elaborados_por_el_responsable_de_atencion_al_usuario_de_servicios_f_c09e92 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16417: aplica_a Obligacion_los_reportes_integrales_escritos_anuales_de_la_auditoria_interna_del_sujeto_obli_64b945 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16419: aplica_a Obligacion_los_responsables_de_la_gestion_de_riesgos_deberan_conocer_las_debilidades_de_los_19980c -> Sujeto_rol_alcance_capmin: sin mención
idx 16421: aplica_a Obligacion_los_responsables_nombrados_titular_y_suplente_s_deberan_asegurar_la_adecuada_ate_19b2b1 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16427: aplica_a Obligacion_los_restantes_derivados_sobre_acciones_y_las_posiciones_fuera_de_balance_sensibl_3705cd -> Sujeto_rol_alcance_capmin: sin mención
idx 16430: aplica_a Obligacion_los_resultados_por_su_gestion_en_la_entidad_frente_al_directorio__lingob_3_1_5_2accb6 -> Sujeto_entidad_financiera: sin mención
idx 16432: aplica_a Obligacion_los_riesgos_de_tasa_de_interes_y_de_moneda_extranjera_deberan_mitigarse_en_forma_c4c890 -> Sujeto_rol_alcance_capmin: sin mención
idx 16434: aplica_a Obligacion_los_saldos_adeudados_se_actualizaran_mediante_la_aplicacion_del_indice_del_costo_76629a -> Sujeto_entidad_financiera: sin mención
idx 16436: aplica_a Obligacion_los_saldos_correspondientes_a_instrumentos_actualizables_por_cer_uva_uvi_deberan_7795c6 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 16444: aplica_a Obligacion_los_saldos_remanentes_luego_de_transcurridos_dichos_lapsos_seran_puestos_a_dispo_1fa9e2 -> Sujeto_banco: sin mención
idx 16446: aplica_a Obligacion_los_sistemas_y_controles_deben_garantizar_a_los_directores_y_o_gerentes_de_la_en_f61414 -> Sujeto_rol_alcance_capmin: sin mención
idx 16448: aplica_a Obligacion_los_soportes_mencionados_deberan_tener_un_rotulo_externo_en_el_cual_se_consigne__f2e566 -> Sujeto_rol_alcance_pagjub: sin mención
idx 16450: aplica_a Obligacion_los_sujetos_alcanzados_deberan_cumplimentar_el_relevamiento_de_activos_y_pasivos_1f3971 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16452: aplica_a Obligacion_los_sujetos_obligados_deberan_adoptar_las_acciones_necesarias_para_garantizar_es_238d57 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16454: aplica_a Obligacion_los_sujetos_obligados_deberan_adoptar_los_recaudos_necesarios_a_los_efectos_de_p_b79a4c -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16456: aplica_a Obligacion_los_sujetos_obligados_deberan_considerar_y_resolver_fundadamente_contemplando_lo_47409d -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16458: aplica_a Obligacion_los_sujetos_obligados_deberan_contar_con_hipervinculo_que_permita_al_usuario_res_7c5239 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16460: aplica_a Obligacion_los_sujetos_obligados_deberan_contar_con_sendos_hipervinculos_que_permitan_al_us_6ca1a9 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16462: aplica_a Obligacion_los_sujetos_obligados_deberan_contratar_un_seguro_sobre_saldo_deudor_con_cobertu_47d4df -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16465: aplica_a Obligacion_los_sujetos_obligados_deberan_efectuar_la_evaluacion_como_sujetos_de_credito_con_13681e -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 16468: aplica_a Obligacion_los_sujetos_obligados_deberan_entregar_a_los_usuarios_antes_de_su_formalizacion__423e35 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16470: aplica_a Obligacion_los_sujetos_obligados_deberan_entregar_a_los_usuarios_un_resumen_del_contrato_qu_14dd99 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16472: aplica_a Obligacion_los_sujetos_obligados_deberan_establecer_este_servicio_para_dar_tratamiento_y_re_97c0d4 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16474: aplica_a Obligacion_los_sujetos_obligados_deberan_evitar_practicas_o_acciones_que_reflejen_o_promuev_8814e8 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16477: aplica_a Obligacion_los_sujetos_obligados_deberan_explicitar_en_un_manual_de_procedimiento_los_pasos_e6a039 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16479: aplica_a Obligacion_los_sujetos_obligados_deberan_ofrecer_a_los_usuarios_de_servicios_financieros_po_e5c1f2 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16482: aplica_a Obligacion_los_sujetos_obligados_tendran_aplicacion_de_las_disposiciones_de_la_seccion_5_en_55c23a -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16485: aplica_a Obligacion_los_swaps_en_los_que_un_tramo_sea_un_precio_fijo_y_el_otro_el_precio_de_mercado__c79976 -> Sujeto_rol_alcance_capmin: sin mención
idx 16487: aplica_a Obligacion_los_tenedores_de_instrumentos_computables_deberan_hacer_expresa_renuncia_a_cualq_23f83d -> Sujeto_rol_alcance_capmin: sin mención
idx 16489: aplica_a Obligacion_los_terminos_a_que_se_refiere_el_punto_1_4_2_2_acapite_i_para_la_presentacion_de_f6376e -> Sujeto_rol_alcance_capmin: sin mención
idx 16497: aplica_a Obligacion_los_titulares_de_la_cuenta_corriente_seran_ilimitadamente_responsables_de_la_emi_ee4142 -> Sujeto_cliente: sin mención
idx 16500: aplica_a Obligacion_los_titulos_de_deuda_con_registro_publico_en_el_exterior_otros_endeudamientos_de_601eff -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16513: aplica_a Obligacion_luego_de_la_ocurrencia_de_un_incumplimiento_u_otro_evento_desencadenante_de_la_a_c5118e -> Sujeto_rol_alcance_capmin: sin mención
idx 16515: aplica_a Obligacion_mantener_a_disposicion_de_la_sefyc_un_registro_de_los_beneficios_obtenidos_por_e_7aee5e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16527: aplica_a Obligacion_mantener_acreditados_los_fondos_por_el_importe_correspondiente_al_total_de_los_c_dd18a3 -> Sujeto_banco: sin mención
idx 16533: aplica_a Obligacion_mantener_pendientes_de_liquidacion_en_el_mercado_de_cambios_y_o_de_acreditacion__4a88d5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16536: aplica_a Obligacion_mantener_suficiente_provision_de_fondos_o_contar_con_la_correspondiente_autoriza_efa354 -> Sujeto_banco: sin mención
idx 16538: aplica_a Obligacion_mantener_un_registro_de_las_certificaciones_emitidas_de_las_anuladas_y_otros_mov_620d7c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16540: aplica_a Obligacion_mantener_un_registro_de_todos_los_movimientos_con_imputacion_al_pago_de_importac_1d0482 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16542: aplica_a Obligacion_mantienen_vigencia_el_procedimiento_y_los_plazos_previstos_en_el_punto_4_2_2_4___676511 -> Sujeto_banco: sin mención
idx 16550: aplica_a Obligacion_mediante_transferencia_de_fondos_desde_y_hacia_cuentas_a_la_vista_a_nombre_del_c_bbf36b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16553: aplica_a Obligacion_metodologia_de_acceso_al_sistema__ctacte_3_3_8_3_85ea74 -> Sujeto_banco: sin mención
idx 16555: aplica_a Obligacion_metodologia_de_actualizacion_del_archivo_de_firmas_digitalizadas__ctacte_3_3_8_3_a1373c -> Sujeto_banco: sin mención
idx 16557: aplica_a Obligacion_metodologia_de_actualizacion_del_registro_de_firmas__ctacte_3_3_8_2_152a40 -> Sujeto_banco: sin mención
idx 16559: aplica_a Obligacion_metodologia_de_administracion_de_claves__ctacte_3_3_8_3_b4f365 -> Sujeto_banco: sin mención
idx 16561: aplica_a Obligacion_metodologia_de_captura_y_almacenamiento_de_firmas__ctacte_3_3_8_2_6d0e91 -> Sujeto_banco: sin mención
idx 16563: aplica_a Obligacion_mientras_que_el_personal_encargado_de_la_negociacion_puede_realizar_la_valuacion_814bb8 -> Sujeto_rol_alcance_capmin: sin mención
idx 16566: aplica_a Obligacion_modelo_de_carta_compromiso_del_banco_mediante_la_cual_informara_a_los_titulares__33ea77 -> Sujeto_banco: sin mención
idx 16568: aplica_a Obligacion_modelo_del_contrato_de_adhesion_mutua_a_suscribir_entre_los_clientes_titulares_d_be874d -> Sujeto_banco: sin mención
idx 16570: aplica_a Obligacion_monitorear_a_los_gerentes_de_las_distintas_areas_de_manera_consistente_con_las_p_6521d9 -> Sujeto_entidad_financiera: sin mención
idx 16572: aplica_a Obligacion_monitoree_el_cumplimiento_de_los_objetivos_societarios__lingob_2_1_11_b28290 -> Sujeto_entidad_financiera: sin mención
idx 16574: aplica_a Obligacion_monitoree_el_perfil_de_riesgo_de_la_entidad__lingob_2_1_2_55c2d7 -> Sujeto_entidad_financiera: sin mención
idx 16576: aplica_a Obligacion_monitoree_las_operaciones_de_sus_sucursales_y_de_las_subsidiarias_que_controla_y_2f33d1 -> Sujeto_entidad_financiera: sin mención
idx 16578: aplica_a Obligacion_monitoree_que_los_auditores_externos_cumplan_con_los_estandares_profesionales_pa_13fbf2 -> Sujeto_entidad_financiera: sin mención
idx 16580: aplica_a Obligacion_monto_a_deducir_del_ca_total_del_exceso_sobre_el_10_multiplicado_por_la_proporci_b492d9 -> Sujeto_rol_alcance_capmin: sin mención
idx 16583: aplica_a Obligacion_monto_a_deducir_del_co_total_del_exceso_sobre_el_10_multiplicado_por_la_proporci_9b93f2 -> Sujeto_rol_alcance_capmin: sin mención
idx 16586: aplica_a Obligacion_monto_a_deducir_del_pnc_total_del_exceso_sobre_el_10_multiplicado_por_la_proporc_1469a1 -> Sujeto_rol_alcance_capmin: sin mención
idx 16589: aplica_a Obligacion_motivo_por_el_que_se_cursa_la_notificacion_cierre_de_la_cuenta_corriente_indican_014ca5 -> Sujeto_banco: sin mención
idx 16591: aplica_a Obligacion_motivo_por_el_que_se_cursa_la_notificacion_rechazo_consignando_alguna_de_las_cau_312aa5 -> Sujeto_banco: sin mención
idx 16593: aplica_a Obligacion_motivo_por_el_que_se_cursa_la_notificacion_suspension_del_servicio_de_pago_de_ch_561e35 -> Sujeto_banco: sin mención
idx 16595: aplica_a Obligacion_no_corresponde_el_cobro_a_los_usuarios_de_conceptos_que_no_observen_las_condicio_203bc1 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16608: aplica_a Obligacion_no_desconocer_el_deposito_u_operacion_realizada_con_un_echeq_que_sea_efectuada_m_1e9ccd -> Sujeto_banco: sin mención
idx 16611: aplica_a Obligacion_no_desconocer_el_echeq_librado_mediante_el_uso_de_los_elementos_y_procedimientos_254106 -> Sujeto_banco: sin mención
idx 16614: aplica_a Obligacion_no_digitar_la_clave_personal_en_presencia_de_personas_ajenas_aun_cuando_pretenda_7d6440 -> Sujeto_usuario_de_servicios_financieros: sin mención
idx 16616: aplica_a Obligacion_no_facilitar_la_tarjeta_magnetica_a_terceros_ya_que_ella_es_de_uso_personal__cta_95cf21 -> Sujeto_usuario_de_servicios_financieros: sin mención
idx 16623: aplica_a Obligacion_no_olvidar_retirar_la_tarjeta_magnetica_al_finalizar_las_operaciones__ctacte_12__ec0138 -> Sujeto_banco: sin mención
idx 16625: aplica_a Obligacion_no_se_presentara_la_informacion_consolidada_mensual_debiendo_consignar_en_su_lug_e8bf2f -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 16628: aplica_a Obligacion_no_utilizar_los_cajeros_automaticos_cuando_se_encuentren_mensajes_o_situaciones__817fdc -> Sujeto_banco: sin mención
idx 16630: aplica_a Obligacion_nombres_y_apellidos_completos_de_los_denunciantes_tipo_y_numero_de_los_documento_694320 -> Sujeto_banco: sin mención
idx 16632: aplica_a Obligacion_normas_de_procedimiento_y_comunicaciones_internas_del_banco__ctacte_3_3_8_2_09af87 -> Sujeto_banco: sin mención
idx 16634: aplica_a Obligacion_notificacion_de_que_se_debitara_de_la_cuenta_el_importe_de_la_multa_establecida__afb5e9 -> Sujeto_banco: sin mención
idx 16636: aplica_a Obligacion_notificar_a_los_supervisores_sobre_operaciones_incluyendo_informacion_pertinente_63490d -> Sujeto_entidad_financiera: sin mención
idx 16638: aplica_a Obligacion_notificar_al_bcra_cada_inversion_ingresada_para_financiar_el_proyecto_informando_cf85f2 -> Sujeto_entidad_financiera: sin mención
idx 16640: aplica_a Obligacion_notificar_al_cliente_la_circunstancia_de_que_la_cuota_supera_el_10_por_medios_el_b8a54e -> Sujeto_entidad_financiera: sin mención
idx 16642: aplica_a Obligacion_notificar_al_cuentacorrentista_cuando_se_entreguen_tarjetas_magneticas_para_ser__9ea3e7 -> Sujeto_banco: sin mención
idx 16644: aplica_a Obligacion_notificar_al_directorio_sobre_operaciones_incluyendo_informacion_pertinente_sobr_924a88 -> Sujeto_entidad_financiera: sin mención
idx 16646: aplica_a Obligacion_notificar_la_situacion_al_cliente_mediante_medios_electronicos_de_comunicacion_e_d78c47 -> Sujeto_banco: sin mención
idx 16648: aplica_a Obligacion_notificar_su_nombramiento_a_la_gerencia_principal_de_exterior_y_cambios_del_bcra_4e5860 -> Sujeto_entidad_financiera: sin mención
idx 16650: aplica_a Obligacion_numero_de_la_comunicacion_y_la_fecha_en_que_si_asi_correspondiere_fue_cursado_el_29fefe -> Sujeto_banco: sin mención
idx 16652: aplica_a Obligacion_numero_de_la_cuenta_corriente_a_la_que_se_imputa_el_aviso__ctacte_10_2_1_5_5d0cac -> Sujeto_banco: sin mención
idx 16655: aplica_a Obligacion_obligacion_de_informar_al_bcra_los_rechazos_y_o_el_pago_de_las_correspondientes__acbaa1 -> Sujeto_banco: sin mención
idx 16663: aplica_a Obligacion_obligacion_de_liquidacion_de_exportaciones_realizadas_y_pendientes_de_cobro__ext_89eee9 -> Sujeto_exportador: sin mención
idx 16666: aplica_a Obligacion_obligacion_del_importador_de_ingresar_por_el_mercado_de_cambios_dentro_de_los_20_8b5217 -> Sujeto_importador: sin mención
idx 16668: aplica_a Obligacion_obligacion_del_importador_de_ingresar_por_el_mercado_de_cambios_dentro_de_los_20_b75795 -> Sujeto_importador: sin mención
idx 16670: aplica_a Obligacion_observar_las_normas_legales_reglamentarias_y_disposiciones_vigentes_en_materia_d_4ae878 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16672: aplica_a Obligacion_obtener_estimaciones_fiables_de_los_principales_supuestos_y_parametros_utilizado_e48702 -> Sujeto_rol_alcance_capmin: sin mención
idx 16676: aplica_a Obligacion_otorgar_a_los_titulos_recuperados_el_mismo_tratamiento_que_a_los_titulos_adquiri_aa6a05 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16679: aplica_a Obligacion_otorgar_al_usuario_los_medios_tecnicos_necesarios_para_que_antes_de_la_contratac_cb589f -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16681: aplica_a Obligacion_otorgar_por_los_elementos_a_que_se_refiere_el_punto_9_2_1_1_el_pertinente_recibo_aea158 -> Sujeto_banco: sin mención
idx 16687: aplica_a Obligacion_otras_cuestiones_particulares_que_impliquen_un_riesgo_inherente_para_el_usuario__523eae -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16689: aplica_a Obligacion_pagar_a_la_vista_excepto_en_los_casos_a_que_se_refiere_el_punto_1_5_2_8_segundo__ee7488 -> Sujeto_banco: sin mención
idx 16698: aplica_a Obligacion_pagos_en_el_exterior_con_fondos_de_libre_disponibilidad_que_deberan_ser_informad_258d8c -> Sujeto_importador: sin mención
idx 16727: aplica_a Obligacion_para_cada_nivel_de_subconsolidacion_las_posiciones_vendidas_y_compradas_en_un_mi_5488c1 -> Sujeto_rol_alcance_capmin: sin mención
idx 16730: aplica_a Obligacion_para_calcular_el_adicional_epf_cuando_las_garantias_intercambiadas_sean_insufici_6371f5 -> Sujeto_rol_alcance_capmin: sin mención
idx 16732: aplica_a Obligacion_para_calcular_los_requerimientos_de_capital_se_debera_expresar_cada_posicion_en__7c68b9 -> Sujeto_rol_alcance_capmin: sin mención
idx 16734: aplica_a Obligacion_para_cartas_de_credito_o_letras_avaladas_emitidas_u_otorgadas_a_partir_del_13_12_e2ef7f -> Sujeto_entidad_financiera: sin mención
idx 16736: aplica_a Obligacion_para_cualquier_otra_posicion_de_titulizacion_no_incluida_en_e3_las_entidades_deb_6a8e10 -> Sujeto_rol_alcance_capmin: sin mención
idx 16749: aplica_a Obligacion_para_cuentas_de_depositos_y_tarjetas_de_credito_la_periodicidad_para_la_generaci_60316a -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16751: aplica_a Obligacion_para_determinar_el_valor_de_mercado_del_nocional_subyacente_se_seguiran_las_disp_83cd36 -> Sujeto_rol_alcance_capmin: sin mención
idx 16757: aplica_a Obligacion_para_determinar_la_naturaleza_del_aporte_se_debera_considerar_la_sustancia_del_a_95e2d7 -> Sujeto_rol_alcance_capmin: sin mención
idx 16759: aplica_a Obligacion_para_documentos_emitidos_hasta_la_fecha_de_notificacion_del_cierre_procedera_su__e291d2 -> Sujeto_banco: sin mención
idx 16762: aplica_a Obligacion_para_el_calculo_del_importe_correspondiente_al_mes_n_procedera_tenerse_en_cuenta_d3927a -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 16764: aplica_a Obligacion_para_el_calculo_se_deberan_emplear_modelos_aprobados_por_mercados_de_opciones_au_c4eecb -> Sujeto_rol_alcance_capmin: sin mención
idx 16766: aplica_a Obligacion_para_el_caso_de_cheques_librados_por_medios_electronicos_o_comprendidos_en_la_op_79d5d5 -> Sujeto_banco: sin mención
idx 16769: aplica_a Obligacion_para_el_caso_de_la_contratacion_a_distancia_el_plazo_de_revocacion_se_contara_a__f6f879 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16772: aplica_a Obligacion_para_financiaciones_otorgadas_a_partir_del_13_12_23_la_entidad_debera_contar_con_faa58b -> Sujeto_entidad_financiera: sin mención
idx 16780: aplica_a Obligacion_para_la_estimacion_del_valor_razonable_mediante_tecnicas_de_valuacion_las_entida_d3db5f -> Sujeto_rol_alcance_capmin: sin mención
idx 16783: aplica_a Obligacion_para_la_regularizacion_del_incumplimiento_en_la_forma_prevista_en_el_punto_6_7_2_eaf7d0 -> Sujeto_rol_alcance_capmin: sin mención
idx 16789: aplica_a Obligacion_para_las_coberturas_de_riesgo_de_credito_vendidas_o_compradas_por_la_entidad_se__56190a -> Sujeto_rol_alcance_capmin: sin mención
idx 16798: aplica_a Obligacion_para_las_financiaciones_en_general_las_causales_los_efectos_de_la_mora_y_los_pro_a1e7fa -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16800: aplica_a Obligacion_para_las_operaciones_de_financiacion_de_cualquier_tipo_todos_los_aspectos_contem_f12961 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16802: aplica_a Obligacion_para_las_posiciones_menos_liquidas_que_exigen_de_las_entidades_mayores_recaudos__6e28bc -> Sujeto_rol_alcance_capmin: sin mención
idx 16830: aplica_a Obligacion_para_las_posteriores_refinanciaciones_recibiran_el_tratamiento_general_previsto__3e7064 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 16833: aplica_a Obligacion_para_los_casos_en_que_el_presentante_no_reciba_automaticamente_el_numero_de_su_c_6de73f -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16835: aplica_a Obligacion_para_los_contratos_de_derivados_distintos_a_los_derivados_de_credito_como_los_sw_c0fcd1 -> Sujeto_rol_alcance_capmin: sin mención
idx 16837: aplica_a Obligacion_para_los_importadores_comprendidos_en_el_parrafo_anterior_las_entidades_deberan__d0083a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16840: aplica_a Obligacion_para_los_mecanismos_previstos_en_los_puntos_10_5_4_10_5_5_1_y_10_5_5_2_la_entida_41c9c9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16895: aplica_a Obligacion_para_opciones_con_plazo_residual_de_mas_de_seis_meses_el_precio_de_ejercicio_se__3c5c66 -> Sujeto_rol_alcance_capmin: sin mención
idx 16898: aplica_a Obligacion_para_proceder_al_efectivo_pago_del_beneficio_se_requerira_la_documentacion_estab_54d479 -> Sujeto_rol_alcance_pagjub: sin mención
idx 16900: aplica_a Obligacion_para_que_la_crc_sea_reconocida_la_exposicion_debera_estar_cubierta_durante_todo__e08c90 -> Sujeto_rol_alcance_capmin: sin mención
idx 16903: aplica_a Obligacion_para_que_la_operacion_no_quede_comprendida_por_el_requisito_de_conformidad_previ_210dce -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16905: aplica_a Obligacion_para_quedar_habilitada_para_emitir_las_certificaciones_la_entidad_tambien_debera_b585a6 -> Sujeto_entidad_financiera: sin mención
idx 16907: aplica_a Obligacion_para_su_calculo_solo_se_permitira_netear_las_posiciones_opuestas_respecto_de_una_c5846f -> Sujeto_rol_alcance_capmin: sin mención
idx 16910: aplica_a Obligacion_participar_en_el_diseno_de_nuevos_productos_y_servicios_asi_como_en_la_modificac_6d460c -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16913: aplica_a Obligacion_participar_en_el_proceso_de_definicion_y_aprobacion_de_nuevos_productos_y_servic_3dbdd5 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16915: aplica_a Obligacion_participar_en_la_modificacion_de_los_existentes_para_su_adecuacion_a_la_normativ_9cdca8 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 16921: aplica_a Obligacion_pasaran_a_informar_codigos_1_y_9_solo_si_consolidan_con_alguno_de_los_entes_a_qu_de9613 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 16923: aplica_a Obligacion_pedir_al_cuentacorrentista_su_conformidad_por_escrito_respecto_del_extracto_envi_959d44 -> Sujeto_banco: sin mención
idx 16926: aplica_a Obligacion_perfiles_de_usuarios_habilitados_supervisor_operador_auditor_etc__ctacte_3_3_8_3_9a00f3 -> Sujeto_banco: sin mención
idx 16928: aplica_a Obligacion_periodicamente_debera_efectuar_un_seguimiento_de_su_correcta_aplicacion_y_los_ca_bd6895 -> Sujeto_rol_alcance_capmin: sin mención
idx 16940: aplica_a Obligacion_plazo_de_vencimiento_original_no_inferior_a_cinco_anos__cap_8_3_3_4_4ca739 -> Sujeto_rol_alcance_capmin: sin mención
idx 16943: aplica_a Obligacion_politica_de_conducta_en_los_negocios_y_o_codigo_de_etica__lingob_7_1_5_fd4869 -> Sujeto_entidad_financiera: sin mención
idx 16945: aplica_a Obligacion_politica_o_estructura_de_gobierno_aplicable__lingob_7_1_5_f8ea28 -> Sujeto_entidad_financiera: sin mención
idx 16947: aplica_a Obligacion_politicas_y_procedimientos_claramente_definidos_para_verificar_que_las_posicione_587d9a -> Sujeto_rol_alcance_capmin: sin mención
idx 16949: aplica_a Obligacion_politicas_y_procedimientos_documentados_para_el_proceso_de_valuacion_incluye_def_aadad7 -> Sujeto_rol_alcance_capmin: sin mención
idx 16951: aplica_a Obligacion_por_cada_oficializacion_del_despacho_de_importacion_el_importador_debera_nominar_bcb911 -> Sujeto_importador: sin mención
idx 16953: aplica_a Obligacion_por_cada_operacion_comprendida_el_exportador_debera_seleccionar_una_entidad_como_11f330 -> Sujeto_exportador: sin mención
idx 16955: aplica_a Obligacion_por_cada_operacion_de_cambio_canje_y_o_arbitraje_las_entidades_deberan_realizar__790c18 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16960: aplica_a Obligacion_por_cada_operacion_que_presente_el_exportador_requerir_una_declaracion_jurada_de_99d615 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16962: aplica_a Obligacion_por_cada_periodo_de_pago_las_entidades_participantes_deberan_presentar_una_nota__8e61bc -> Sujeto_rol_alcance_pagjub: sin mención
idx 16964: aplica_a Obligacion_por_estas_operaciones_las_entidades_financieras_deberan_permitir_la_acreditacion_7b3a82 -> Sujeto_entidad_financiera: sin mención
idx 16966: aplica_a Obligacion_por_las_operaciones_del_punto_3_11_3_al_momento_de_constitucion_de_las_garantias_844872 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 16999: aplica_a Obligacion_por_lo_que_a_su_finalizacion_la_revision_debera_haber_alcanzado_a_la_totalidad_d_6eff20 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 17001: aplica_a Obligacion_por_los_beneficiarios_distintos_del_librador_solo_sera_necesario_el_cumplimiento_1d7e95 -> Sujeto_banco: sin mención
idx 17005: aplica_a Obligacion_por_los_pagos_que_se_realicen_la_entidad_debera_informar_en_el_sepaimpo_dentro_d_ddaec6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17007: aplica_a Obligacion_por_todo_acceso_al_mercado_de_cambios_por_pagos_de_importaciones_de_bienes_con_r_da9a72 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17009: aplica_a Obligacion_posibilitar_la_rehabilitacion_de_los_productos_servicios_a_traves_de_alguno_de_l_d337c9 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17012: aplica_a Obligacion_posibilitar_la_rehabilitacion_de_los_productos_servicios_en_forma_presencial_en__88686b -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17015: aplica_a Obligacion_presentacion_de_declaracion_jurada_comprometiendose_a_liquidar_en_el_mercado_de__6690aa -> Sujeto_importador: sin mención
idx 17020: aplica_a Obligacion_presentacion_de_tipo_y_numero_del_documento_para_establecer_su_identificacion_se_c283d6 -> Sujeto_banco: sin mención
idx 17026: aplica_a Obligacion_presentar_constancia_de_haber_denunciado_el_hecho_como_delito_en_los_terminos_de_59b811 -> Sujeto_banco: sin mención
idx 17030: aplica_a Obligacion_presentar_copia_del_documento_de_salida_de_zona_primaria_aduanera__ext_10_3_4_2_29fd1c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17032: aplica_a Obligacion_previamente_a_efectuar_la_apertura_de_la_cuenta_de_la_alianza_electoral_las_enti_76ab3c -> Sujeto_banco: sin mención
idx 17034: aplica_a Obligacion_previamente_se_debera_plantear_cada_situacion_en_forma_individual_ante_la_sefyc__617dde -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 17036: aplica_a Obligacion_previo_a_su_deduccion_debera_absorberse_el_importe_de_la_prevision_por_riesgo_de_6b2f68 -> Sujeto_rol_alcance_capmin: sin mención
idx 17040: aplica_a Obligacion_primero_se_debe_determinar_el_valor_de_las_partidas_netas_que_correspondan_por_e_8510f7 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17043: aplica_a Obligacion_producto_de_seguridad_utilizado__ctacte_3_3_8_3_f1f68b -> Sujeto_banco: sin mención
idx 17045: aplica_a Obligacion_promover_que_la_politica_para_incentivar_economicamente_al_personal_se_ajuste_a__ce8a2e -> Sujeto_entidad_financiera: sin mención
idx 17047: aplica_a Obligacion_promover_y_revisar_en_forma_periodica_las_estrategias_generales_de_negocios_de_l_b43d27 -> Sujeto_entidad_financiera: sin mención
idx 17050: aplica_a Obligacion_promover_y_revisar_en_forma_periodica_las_politicas_de_riesgos_de_la_entidad_fin_8573c6 -> Sujeto_entidad_financiera: sin mención
idx 17053: aplica_a Obligacion_promueva_la_capacitacion_y_desarrollo_de_los_ejecutivos_y_defina_programas_de_en_04e1c3 -> Sujeto_entidad_financiera: sin mención
idx 17056: aplica_a Obligacion_propender_a_las_correcciones_que_eviten_que_se_originen_nuevos_casos__pro_3_1_1__b95670 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17058: aplica_a Obligacion_proponer_al_directorio_o_autoridad_equivalente_a_los_funcionarios_para_el_desemp_8ec4c8 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17065: aplica_a Obligacion_proporcionar_o_poner_a_disposicion_del_usuario_de_servicios_financieros_un_ejemp_8600ea -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17067: aplica_a Obligacion_proporcionarle_al_usuario_un_mecanismo_de_confirmacion_expresa_de_la_decision_de_929a82 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17069: aplica_a Obligacion_provea_los_mecanismos_para_que_los_informes_a_ser_presentados_por_los_auditores__37c9e4 -> Sujeto_entidad_financiera: sin mención
idx 17073: aplica_a Obligacion_que_asegure_que_la_entidad_cuenta_con_medios_adecuados_para_promover_la_toma_de__e367af -> Sujeto_entidad_financiera: sin mención
idx 17076: aplica_a Obligacion_que_los_registros_centralizados_de_consultas_y_reclamos_rccr_de_reintegros_de_im_e920b5 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17078: aplica_a Obligacion_que_se_completara_en_caso_de_corresponder_incorporando_a_clientes_cuyo_endeudami_2726fb -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 17080: aplica_a Obligacion_que_se_les_ha_notificado_en_el_contrato_a_los_usuarios_de_servicios_financieros__22ff7c -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17082: aplica_a Obligacion_que_se_les_ha_notificado_en_el_cuerpo_del_contrato_cuales_son_los_conceptos_sobr_d34461 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17084: aplica_a Obligacion_que_se_proporciona_a_los_usuarios_de_servicios_financieros_copia_de_los_formular_3ae689 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17087: aplica_a Obligacion_quedan_sujetos_a_la_conformidad_previa_del_bcra__ext_13_1_e18f64 -> Sujeto_bcra: sin mención
idx 17089: aplica_a Obligacion_quedando_a_cargo_del_seguimiento_la_entidad_que_le_dio_curso_los_datos_asociados_6d56e7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17091: aplica_a Obligacion_ratificar_personalmente_en_el_dia_la_denuncia_en_cualquier_sucursal_de_la_entida_001104 -> Sujeto_banco: sin mención
idx 17093: aplica_a Obligacion_ratificar_personalmente_en_el_dia_la_denuncia_en_cualquier_sucursal_de_la_entida_435fb4 -> Sujeto_banco: sin mención
idx 17095: aplica_a Obligacion_ratificar_personalmente_en_el_dia_la_denuncia_en_cualquier_sucursal_de_la_entida_51c9be -> Sujeto_banco: sin mención
idx 17097: aplica_a Obligacion_ratificar_personalmente_en_el_dia_la_denuncia_en_cualquier_sucursal_de_la_entida_ad56c2 -> Sujeto_banco: sin mención
idx 17099: aplica_a Obligacion_realice_la_autoevaluacion_de_su_desempeno_como_organo_y_de_cada_uno_de_sus_miemb_048c74 -> Sujeto_entidad_financiera: sin mención
idx 17101: aplica_a Obligacion_rechazar_el_pago_de_los_cheques_o_certificados_nominativos_de_registracion_que_s_199f68 -> Sujeto_banco: sin mención
idx 17103: aplica_a Obligacion_rechazar_la_registracion_de_cheques_de_pago_diferido_que_se_presenten_a_registra_1e2963 -> Sujeto_banco: sin mención
idx 17105: aplica_a Obligacion_recibir_y_dar_curso_a_las_presentaciones_concernientes_al_sujeto_obligado_que_re_c4927d -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17107: aplica_a Obligacion_reconozcan_la_importancia_de_los_procesos_de_auditoria_y_control_interno_y_la_co_4ce6d2 -> Sujeto_entidad_financiera: sin mención
idx 17109: aplica_a Obligacion_redactarlos_en_idioma_nacional__ctacte_1_5_1_8_fbcde9 -> Sujeto_banco: sin mención
idx 17112: aplica_a Obligacion_reemplazar_a_los_principales_ejecutivos_cuando_sea_necesario__lingob_2_1_8_0da4a5 -> Sujeto_entidad_financiera: sin mención
idx 17114: aplica_a Obligacion_registrar_la_operacion_en_el_sistema_online_instrumentado_por_el_bcra__ext_14_4__285f66 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17117: aplica_a Obligacion_registrar_los_domicilios_real_y_legal_inscriptos_en_la_justicia_electoral__ctact_e81940 -> Sujeto_banco: sin mención
idx 17119: aplica_a Obligacion_reintegrar_los_cuadernos_de_cheques_donde_figure_el_domicilio_anterior__ctacte_1_4a8fcf -> Sujeto_banco: sin mención
idx 17121: aplica_a Obligacion_relatar_en_forma_clara_y_precisa_los_hechos_y_el_reclamo_efectuado_a_la_entidad__468143 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17123: aplica_a Obligacion_remitir_el_cheque_librado_en_formato_papel_o_certificado_nominativo_transferible_10145b -> Sujeto_banco: sin mención
idx 17129: aplica_a Obligacion_remitir_el_cheque_o_certificado_nominativo_transferible_rechazado_retenido_segun_aacf9e -> Sujeto_banco: sin mención
idx 17134: aplica_a Obligacion_remitiran_los_correspondientes_avisos_sobre_el_cierre_de_cuentas_o_revocacion_de_aa9d0d -> Sujeto_banco: sin mención
idx 17136: aplica_a Obligacion_reportar_al_bcra_la_falta_de_cumplimiento_por_parte_del_importador_en_la_medida__7b5b00 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17138: aplica_a Obligacion_reportar_al_bcra_todas_las_otras_circunstancias_de_las_que_tomen_conocimiento_y__6ef980 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17140: aplica_a Obligacion_reportar_el_valor_del_subyacente_pactado_en_el_tramo_fijo_de_la_operacion__ric_4_7cc802 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17142: aplica_a Obligacion_reportar_en_el_sepaimpo_dentro_de_los_5_cinco_dias_habiles_siguientes_a_la_fecha_3e6fe0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17144: aplica_a Obligacion_reportar_en_el_sepaimpo_las_prorrogas_en_los_plazos_que_fuesen_concedidas_a_las__b78ddc -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17147: aplica_a Obligacion_reportar_en_el_sepaimpo_los_zfe_con_transferencia_aduanera_de_dominio_asociados__d75c8a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17150: aplica_a Obligacion_reportar_en_el_sepaimpo_todas_las_otras_circunstancias_de_las_que_tome_conocimie_a2da5b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17153: aplica_a Obligacion_reportar_periodicamente_al_directorio_sobre_el_cumplimiento_de_los_objetivos__li_703045 -> Sujeto_entidad_financiera: sin mención
idx 17155: aplica_a Obligacion_reportar_por_el_sepaimpo_al_bcra_las_afectaciones_de_despachos_de_importacion_im_f6e132 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17158: aplica_a Obligacion_reportar_valor_nocional_sobre_el_que_se_calculan_los_pagos_de_flujos_a_pagar_y_f_749997 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17160: aplica_a Obligacion_reporte_del_codigo_70800000_con_la_exigencia_segun_riesgo_de_mercado_para_las_po_1dbfaf -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17163: aplica_a Obligacion_requisitos_que_cada_una_de_las_partes_deberan_observar_en_la_ocasion_del_cierre__a5a63a -> Sujeto_banco: sin mención
idx 17165: aplica_a Obligacion_respecto_de_clientes_por_financiaciones_en_moneda_extranjera_cualquiera_sea_la_f_a14e51 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 17167: aplica_a Obligacion_respecto_de_los_elementos_que_seguidamente_se_mencionan_netos_de_los_conceptos_d_0108d5 -> Sujeto_rol_alcance_capmin: sin mención
idx 17169: aplica_a Obligacion_retencion_de_los_cheques_de_pago_diferido_al_momento_de_su_registracion_para_sub_aad2e5 -> Sujeto_banco: sin mención
idx 17171: aplica_a Obligacion_retirar_el_comprobante_que_la_maquina_entregue_al_finalizar_la_operacion_de_depo_0b9713 -> Sujeto_usuario_de_servicios_financieros: sin mención
idx 17173: aplica_a Obligacion_revertir_las_operaciones_debitadas_segun_instrucciones_expresas_del_titular_vinc_4711b2 -> Sujeto_banco: sin mención
idx 17183: aplica_a Obligacion_revise_el_diseno_y_el_funcionamiento_en_la_entidad_del_sistema_de_retribuciones__601035 -> Sujeto_entidad_financiera: sin mención
idx 17187: aplica_a Obligacion_se_abstenga_de_tomar_decisiones_cuando_haya_conflicto_de_intereses_que_le_impida_fb1b3b -> Sujeto_entidad_financiera: sin mención
idx 17189: aplica_a Obligacion_se_aclarara_en_la_clausula_de_revocacion_que_dicha_revocacion_sera_sin_costo_ni__1d53cd -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17191: aplica_a Obligacion_se_acreditara_dentro_de_las_24_horas_habiles_anteriores_al_comienzo_de_cada_peri_e984ea -> Sujeto_rol_alcance_pagjub: sin mención
idx 17193: aplica_a Obligacion_se_acreditaran_los_importes_correspondientes_a_nuevos_beneficios_u_otros_concept_5d640c -> Sujeto_rol_alcance_pagjub: sin mención
idx 17195: aplica_a Obligacion_se_admitira_la_aplicacion_de_divisas_de_cobros_de_exportaciones_de_bienes_a_la_c_855454 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17197: aplica_a Obligacion_se_agregara_una_descripcion_detallada_del_calculo_de_la_franquicia_para_el_perio_ed5334 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17199: aplica_a Obligacion_se_ajustara_a_lo_previsto_en_el_regimen_operativo_pertinente_basado_en_el_numero_f5a6b1 -> Sujeto_banco: sin mención
idx 17203: aplica_a Obligacion_se_ajustaran_a_lo_establecido_por_el_bcra__ctacte_3_1_fd418e -> Sujeto_banco: sin mención
idx 17205: aplica_a Obligacion_se_anexaran_al_legajo_del_deudor_las_carpetas_crediticia_legal_y_de_administraci_7a25ef -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 17208: aplica_a Obligacion_se_aplicara_a_la_exposicion_la_ponderacion_de_riesgo_mas_alta__cap_10_3_2_2_6d578e -> Sujeto_rol_alcance_capmin: sin mención
idx 17212: aplica_a Obligacion_se_aplicara_un_requerimiento_de_capital_a_las_entidades_financieras_situadas_en__469c95 -> Sujeto_rol_alcance_capmin: sin mención
idx 17214: aplica_a Obligacion_se_aplicara_una_exigencia_de_capital_adicional_de_2_de_la_posicion_neta_comprada_7ae1db -> Sujeto_rol_alcance_capmin: sin mención
idx 17216: aplica_a Obligacion_se_aplicara_una_exigencia_de_capital_de_4_a_las_posiciones_que_surjan_de_estrate_b22594 -> Sujeto_rol_alcance_capmin: sin mención
idx 17218: aplica_a Obligacion_se_aplicaran_las_normas_sobre_financiamiento_al_sector_publico_no_financiero_en__19f677 -> Sujeto_entidad_financiera: sin mención
idx 17221: aplica_a Obligacion_se_aplicaran_los_criterios_especificados_anteriormente_considerando_la_apertura__cbfd60 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17223: aplica_a Obligacion_se_aplicaran_periodos_de_mantenimiento_minimo_de_acuerdo_con_punto_5_3_2_3_para__8f310b -> Sujeto_rol_alcance_capmin: sin mención
idx 17233: aplica_a Obligacion_se_asegurara_de_que_la_alta_gerencia_implemente_procedimientos_para_promover_con_3f69c8 -> Sujeto_entidad_financiera: sin mención
idx 17235: aplica_a Obligacion_se_asegurara_de_que_la_alta_gerencia_implemente_procedimientos_que_prevengan_y_o_71e2d9 -> Sujeto_entidad_financiera: sin mención
idx 17237: aplica_a Obligacion_se_asegurara_de_que_se_practique_una_debida_diligencia_para_seleccionar_a_los_pr_2c98e6 -> Sujeto_entidad_financiera: sin mención
idx 17240: aplica_a Obligacion_se_asegure_de_que_la_alta_gerencia_realiza_un_seguimiento_apropiado_y_consistent_85c8f4 -> Sujeto_entidad_financiera: sin mención
idx 17242: aplica_a Obligacion_se_asegure_de_que_las_politicas_y_practicas_de_retribucion_de_la_entidad_sean_co_0f48bc -> Sujeto_entidad_financiera: sin mención
idx 17244: aplica_a Obligacion_se_asumen_y_gestionan_por_personal_con_autonomia_para_decidir_dentro_de_los_limi_497c7c -> Sujeto_rol_alcance_capmin: sin mención
idx 17246: aplica_a Obligacion_se_compromete_a_liquidar_en_el_mercado_de_cambios_dentro_de_los_5_cinco_dias_hab_048cc0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17251: aplica_a Obligacion_se_computara_el_mayor_valor_que_surja_del_siguiente_calculo_codigo_70800000_max__fcf883 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17253: aplica_a Obligacion_se_computara_en_la_expresion_de_apr_c_la_exposicion_crediticia_resultante_de_la__8df443 -> Sujeto_rol_alcance_capmin: sin mención
idx 17255: aplica_a Obligacion_se_computaran_los_siguientes_incrementos_exposicion_crediticia_resultante_de_la__14d9d2 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17257: aplica_a Obligacion_se_computaran_los_siguientes_incrementos_utilizacion_de_los_cupos_crediticios_am_b63746 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17259: aplica_a Obligacion_se_considera_una_buena_practica_que_en_el_caso_de_que_se_decida_abonar_importes__2d1077 -> Sujeto_entidad_financiera: sin mención
idx 17261: aplica_a Obligacion_se_considera_una_buena_practica_que_las_entidades_financieras_al_extinguir_el_vi_4d38e9 -> Sujeto_entidad_financiera: sin mención
idx 17263: aplica_a Obligacion_se_considerara_cumplido_lo_requerido_con_el_ingreso_de_los_fondos_a_la_pgc_de_la_a852da -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17265: aplica_a Obligacion_se_considerara_la_ultima_calificacion_informada_para_el_calculo_de_la_exigencia__768b58 -> Sujeto_rol_alcance_capmin: sin mención
idx 17267: aplica_a Obligacion_se_considerara_la_ultima_calificacion_informada_para_el_calculo_de_la_exigencia__e80a37 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17269: aplica_a Obligacion_se_consideraran_las_situaciones_que_cada_persona_registre__ctacte_8_5_1_1be6a3 -> Sujeto_banco: sin mención
idx 17271: aplica_a Obligacion_se_consideraran_los_saldos_al_cierre_del_trimestre__cap_2_3_2_5c6ed1 -> Sujeto_rol_alcance_capmin: sin mención
idx 17273: aplica_a Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_de_posiciones_en_opciones_para_353498 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17275: aplica_a Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_especifico_de_tasa_de_interes__3ac6dd -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17280: aplica_a Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_general_de_acciones_adicional__cd8749 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17297: aplica_a Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_general_de_acciones_para_el_ul_5656e5 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17303: aplica_a Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_general_de_tasa_de_interes_par_0e434c -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17305: aplica_a Obligacion_se_consignaran_en_la_partida_12500000_por_cada_ponderador_que_corresponda_aplica_62f35f -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17308: aplica_a Obligacion_se_constituira_un_solo_domicilio_especial__ctacte_1_3_1_5_3392bf -> Sujeto_banco: sin mención
idx 17310: aplica_a Obligacion_se_continuara_informando_codigo_de_consolidacion_3_no_obstante_las_operaciones_a_5fd728 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17312: aplica_a Obligacion_se_cuente_con_dictamen_juridico_competente_que_confirme_la_exigibilidad_del_cont_04d505 -> Sujeto_rol_alcance_capmin: sin mención
idx 17314: aplica_a Obligacion_se_debe_determinar_en_primer_lugar_el_valor_de_las_partidas_netas_que_correspond_31966c -> Sujeto_rol_alcance_capmin: sin mención
idx 17316: aplica_a Obligacion_se_debe_satisfacer_la_totalidad_de_los_requisitos_operativos_listados_condicione_d671f6 -> Sujeto_rol_alcance_capmin: sin mención
idx 17318: aplica_a Obligacion_se_debera_acreditar_el_cumplimiento_de_los_restantes_requisitos_generales_y_espe_218504 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17321: aplica_a Obligacion_se_debera_acreditar_el_cumplimiento_de_los_restantes_requisitos_generales_y_espe_6e89c8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17327: aplica_a Obligacion_se_debera_ajustar_el_valor_corriente_de_estas_posiciones_y_vigilar_en_forma_perm_c40e06 -> Sujeto_rol_alcance_capmin: sin mención
idx 17329: aplica_a Obligacion_se_debera_analizar_dejando_constancia_fundamentada_de_la_decision_adoptada_en_el_39b09e -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 17331: aplica_a Obligacion_se_debera_analizar_dejando_constancia_fundamentada_de_la_decision_adoptada_en_el_917d7b -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 17335: aplica_a Obligacion_se_debera_aplicar_el_tratamiento_de_division_tanto_al_cr_costo_de_reposicion_com_8e88ba -> Sujeto_rol_alcance_capmin: sin mención
idx 17337: aplica_a Obligacion_se_debera_consignar_al_dorso_la_firma_y_aclaracion_o_en_el_correspondiente_regis_88fd95 -> Sujeto_banco: sin mención
idx 17340: aplica_a Obligacion_se_debera_contar_con_informacion_verificable_sobre_perdidas_e_incumplimientos_re_5dac28 -> Sujeto_rol_alcance_capmin: sin mención
idx 17342: aplica_a Obligacion_se_debera_contar_con_la_certificacion_de_la_entidad_que_curso_la_operacion_de_ca_f7d586 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17344: aplica_a Obligacion_se_debera_deducir_del_capital_ordinario_de_nivel_uno_co_n1_todo_incremento_del_c_962f75 -> Sujeto_rol_alcance_capmin: sin mención
idx 17346: aplica_a Obligacion_se_debera_demostrar_que_tales_riesgos_son_adecuadamente_mitigados_a_traves_de_in_31fd9d -> Sujeto_rol_alcance_capmin: sin mención
idx 17348: aplica_a Obligacion_se_debera_especificar_i_tasa_de_interes_anual_efectiva_equivalente_al_calculo_de_0c612f -> Sujeto_banco: sin mención
idx 17378: aplica_a Obligacion_se_debera_instruir_al_personal_de_atencion_al_publico_en_orden_a_la_sensibilidad_7e41b9 -> Sujeto_entidad_cambiaria: sin mención
idx 17379: aplica_a Obligacion_se_debera_instruir_al_personal_de_atencion_al_publico_en_orden_a_la_sensibilidad_7e41b9 -> Sujeto_entidad_financiera: sin mención
idx 17381: aplica_a Obligacion_se_debera_observar_el_esquema_de_responsabilidades_incluido_en_los_convenios_for_249efa -> Sujeto_banco: sin mención
idx 17383: aplica_a Obligacion_se_debera_presentar_adicionalmente_a_los_requisitos_generales_establecidos_para__2f00e3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17385: aplica_a Obligacion_se_debera_prever_en_los_contratos_que_la_entidad_compensara_al_cliente_los_gasto_6b5e46 -> Sujeto_banco: sin mención
idx 17387: aplica_a Obligacion_se_debera_recategorizar_al_deudor_cuando_exista_una_discrepancia_de_mas_de_un_ni_59f6ff -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 17389: aplica_a Obligacion_se_debera_recategorizar_al_deudor_cuando_exista_una_discrepancia_de_mas_de_un_ni_f8a1c5 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 17393: aplica_a Obligacion_se_debera_utilizar_el_valor_mas_prudente_del_intervalo_precio_de_compra_precio_d_d79d45 -> Sujeto_rol_alcance_capmin: sin mención
idx 17396: aplica_a Obligacion_se_debera_verificar_los_requisitos_previstos_en_cada_caso_reemplazando_la_consta_7c7850 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17398: aplica_a Obligacion_se_deberan_calcular_tambien_los_coeficientes_gamma_y_vega__cap_6_6_3_1_d766cc -> Sujeto_rol_alcance_capmin: sin mención
idx 17400: aplica_a Obligacion_se_deberan_definir_detalladamente_los_procedimientos_de_atencion_aplicables_a_ca_696df7 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17402: aplica_a Obligacion_se_deberan_extremar_los_recaudos_a_fin_de_prevenir_la_operatoria_con_personas_qu_aaea15 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 17403: aplica_a Obligacion_se_deberan_extremar_los_recaudos_a_fin_de_prevenir_la_operatoria_con_personas_qu_aaea15 -> Sujeto_sujeto_regulado: sin mención
idx 17406: aplica_a Obligacion_se_deberan_implementar_procedimientos_formales_de_control_de_las_modificaciones__aa5d07 -> Sujeto_rol_alcance_capmin: sin mención
idx 17408: aplica_a Obligacion_se_deberan_ponderar_asumiendo_que_la_cartera_subyacente_ha_sido_invertida_hasta__2ad02f -> Sujeto_rol_alcance_capmin: sin mención
idx 17411: aplica_a Obligacion_se_deberan_validar_de_forma_independiente_las_formulas_matematicas_los_supuestos_e74189 -> Sujeto_rol_alcance_capmin: sin mención
idx 17414: aplica_a Obligacion_se_deduciran_los_ajustes_de_valuacion_por_el_riesgo_de_credito_de_la_entidad_fin_2a803e -> Sujeto_rol_alcance_capmin: sin mención
idx 17419: aplica_a Obligacion_se_demostrara_con_cualquiera_de_las_siguientes_alternativas_deposito_en_la_casa__375ed3 -> Sujeto_banco: sin mención
idx 17422: aplica_a Obligacion_se_determinara_la_exigencia_de_capital_por_riesgo_de_credito_aplicando_la_siguie_91ccb4 -> Sujeto_rol_alcance_capmin: sin mención
idx 17424: aplica_a Obligacion_se_determinara_la_exigencia_por_riesgo_de_mercado_con_los_valores_que_se_registr_5ad64b -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17427: aplica_a Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_segun_ad89e5 -> Sujeto_rol_alcance_capmin: sin mención
idx 17432: aplica_a Obligacion_se_determinaran_las_posiciones_netas_compradas_y_netas_vendidas_para_cada_moneda_8d7ac2 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17435: aplica_a Obligacion_se_establecen_lineamientos_para_la_valuacion_prudente_de_las_posiciones_contabil_1ca1cb -> Sujeto_rol_alcance_capmin: sin mención
idx 17437: aplica_a Obligacion_se_evaluara_si_el_sistema_atiende_a_sus_objetivos_cultura_y_actividades_y_si_est_09808e -> Sujeto_entidad_financiera: sin mención
idx 17439: aplica_a Obligacion_se_fije_una_politica_vinculada_a_la_delegacion_de_actividades_y_a_la_seleccion_d_57bf51 -> Sujeto_entidad_financiera: sin mención
idx 17442: aplica_a Obligacion_se_hara_constar_la_leyenda_que_corresponda_incluir_en_materia_de_garantia_de_los_f32896 -> Sujeto_banco: sin mención
idx 17445: aplica_a Obligacion_se_informan_a_la_alta_gerencia_como_parte_del_proceso_de_gestion_de_riesgos__cap_a6edcf -> Sujeto_rol_alcance_capmin: sin mención
idx 17447: aplica_a Obligacion_se_informara_el_bic_calculado__ric_5_2_1_18aa0c -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17450: aplica_a Obligacion_se_informara_el_ingreso_bruto_del_periodo_x__ric_5_2_3_bfffd4 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17452: aplica_a Obligacion_se_informara_la_correspondiente_reduccion_de_exigencia_en_las_partidas_36000001__57e5ba -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17454: aplica_a Obligacion_se_informara_una_sola_partida_3600000y_reflejando_la_situacion_de_la_entidad_res_c0dbad -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17456: aplica_a Obligacion_se_informaran_al_bcra_los_casos_comprendidos_en_los_puntos_8_3_y_8_4_dentro_de_l_4f7f54 -> Sujeto_banco: sin mención
idx 17460: aplica_a Obligacion_se_informaran_dos_partes_de_la_operacion_uno_cuando_el_contrato_subyacente_entra_79475c -> Sujeto_rol_alcance_capmin: sin mención
idx 17462: aplica_a Obligacion_se_informaran_las_exposiciones_en_el_activo_siguiendo_lo_dispuesto_en_los_puntos_9ba01f -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17464: aplica_a Obligacion_se_informaran_las_exposiciones_fuera_de_balance_conforme_a_lo_dispuesto_en_los_p_47c6ae -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17466: aplica_a Obligacion_se_informaran_las_exposiciones_por_derivados_siguiendo_lo_dispuesto_en_los_punto_2aca62 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17468: aplica_a Obligacion_se_informaran_las_exposiciones_por_operaciones_de_financiacion_con_valores_sft_c_8a30ee -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17470: aplica_a Obligacion_se_informaran_los_activos_ponderados_por_riesgo_parametro_para_el_calculo_de_los_6bf71d -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17472: aplica_a Obligacion_se_informaran_los_incrementos_a_la_exigencia_segun_riesgo_de_credito_generados_p_60f94f -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17474: aplica_a Obligacion_se_informaran_por_el_importe_correspondiente_al_cargo_de_capital__ric_3_1_5_81bd78 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17482: aplica_a Obligacion_se_informaran_utilizando_los_codigos_previstos_en_el_punto_4_4_2_a_para_cada_com_0ec5b8 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17485: aplica_a Obligacion_se_insertara_alguna_de_las_siguientes_expresiones_en_procuracion_valor_al_cobro__d4ec1f -> Sujeto_banco: sin mención
idx 17487: aplica_a Obligacion_se_le_debera_informar_el_estado_del_tramite_cada_vez_que_lo_requiera__pro_3_2_2__fb310e -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17489: aplica_a Obligacion_se_les_aplicaran_las_exigencias_de_capital_por_riesgo_especifico_y_riesgo_genera_70f082 -> Sujeto_rol_alcance_capmin: sin mención
idx 17491: aplica_a Obligacion_se_liquidaran_hasta_el_dia_anterior_al_de_operarse_el_cierre_de_la_cuenta__ctact_6492a4 -> Sujeto_banco: sin mención
idx 17493: aplica_a Obligacion_se_observara_el_siguiente_proceso__ctacte_6_4_7_fd57c7 -> Sujeto_banco: sin mención
idx 17496: aplica_a Obligacion_se_podra_usar_el_valor_contable_en_el_caso_de_las_opciones_sobre_monedas_no_incl_904a61 -> Sujeto_rol_alcance_capmin: sin mención
idx 17498: aplica_a Obligacion_se_presente_el_formulario_zfe_de_oficializacion_de_ingreso_de_los_bienes_al_pais_89d839 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17500: aplica_a Obligacion_se_presumira_como_lugar_de_creacion_el_del_domicilio_del_librador_que_figure_en__8936ed -> Sujeto_banco: sin mención
idx 17502: aplica_a Obligacion_se_procedera_a_clasificar_a_la_compania_de_seguros_en_funcion_de_la_mora_segun_l_89e5d0 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 17505: aplica_a Obligacion_se_recibiran_de_los_usuarios_de_servicios_financieros_por_igual_via_comentarios__5cb777 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17509: aplica_a Obligacion_se_reconocera_la_proteccion_crediticia_provista_por_los_entes_listados_en_la_med_b52b55 -> Sujeto_rol_alcance_capmin: sin mención
idx 17511: aplica_a Obligacion_se_reemplazaran_las_dos_ultimas_posiciones_de_cada_partida_de_exigencia_por_el_u_8f0087 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17514: aplica_a Obligacion_se_regira_por_los_plazos_de_presentacion_previstos_para_el_regimen_informativo_c_8dfdad -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17524: aplica_a Obligacion_se_registrara_el_incremento_calculado_por_la_entidad_aplicando_los_porcentajes_e_6d2b79 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17531: aplica_a Obligacion_se_requerira_la_conformidad_previa_del_bcra__ext_10_4_2_8_677de9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17533: aplica_a Obligacion_se_requerira_la_conformidad_previa_del_bcra__ext_10_4_3_7_adbf4c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17535: aplica_a Obligacion_se_requerira_la_conformidad_previa_del_bcra_cuando_el_acreedor_sea_una_contrapar_114c9c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17555: aplica_a Obligacion_se_requerira_la_conformidad_previa_del_bcra_cuando_el_cliente_registre_por_opera_ec0051 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17557: aplica_a Obligacion_se_requerira_la_conformidad_previa_del_bcra_en_caso_de_tratarse_de_prefinanciaci_8ec494 -> Sujeto_bcra: sin mención
idx 17559: aplica_a Obligacion_se_requerira_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_58d9de -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17573: aplica_a Obligacion_se_requerira_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_7c9cac -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17584: aplica_a Obligacion_se_requerira_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_95b25d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17586: aplica_a Obligacion_se_requerira_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_a3d274 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17588: aplica_a Obligacion_se_requerira_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_ca343d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17590: aplica_a Obligacion_se_requerira_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_d69e27 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17593: aplica_a Obligacion_se_requerira_la_exhibicion_del_dni_m_o_dni_d_expedido_con_posterioridad_a_la_rec_775bcf -> Sujeto_cliente: sin mención
idx 17595: aplica_a Obligacion_se_responsabilice_por_las_actividades_delegadas_en_terceros_las_cuales_deben_aju_ff5e0d -> Sujeto_entidad_financiera: sin mención
idx 17598: aplica_a Obligacion_se_responsabilizara_de_que_esos_objetivos_y_estandares_sean_ampliamente_difundid_5acdaa -> Sujeto_entidad_financiera: sin mención
idx 17600: aplica_a Obligacion_se_reuna_con_regularidad_con_la_alta_gerencia_para_revisar_las_politicas__lingob_bf824d -> Sujeto_entidad_financiera: sin mención
idx 17602: aplica_a Obligacion_se_reuna_con_regularidad_con_los_auditores_internos_para_revisar_los_resultados__a4d2c6 -> Sujeto_entidad_financiera: sin mención
idx 17604: aplica_a Obligacion_se_tendran_en_cuenta_las_clasificaciones_efectuadas_segun_la_evaluacion_de_las_e_385509 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 17606: aplica_a Obligacion_se_tome_en_cuenta_los_riesgos_que_el_personal_asume_en_nombre_de_la_entidad_cons_70f934 -> Sujeto_entidad_financiera: sin mención
idx 17608: aplica_a Obligacion_se_utilizara_cuit_cuil_cdi_cie_o_dni_del_cliente_que_realiza_la_operacion__ext_5_b05c22 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17612: aplica_a Obligacion_se_valuan_a_precios_de_mercado_al_menos_diariamente__cap_6_9_2_4_8b9c39 -> Sujeto_rol_alcance_capmin: sin mención
idx 17616: aplica_a Obligacion_seleccionar_a_los_principales_ejecutivos_de_la_entidad_financiera__lingob_2_1_8_9cb696 -> Sujeto_entidad_financiera: sin mención
idx 17618: aplica_a Obligacion_sera_aplicable_el_plazo_vigente_en_el_pais_de_destino__ext_7_5_1_d1bcd7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17622: aplica_a Obligacion_sera_obligacion_consignar_numero_de_clave_de_identificacion_tributaria_cuit_cuil_8c3ff6 -> Sujeto_banco: sin mención
idx 17625: aplica_a Obligacion_sera_requisito_indispensable_que_el_cuentacorrentista_cumpla_la_exigencia_a_que__5ac96f -> Sujeto_persona_juridica: sin mención
idx 17634: aplica_a Obligacion_sera_suficiente_que_la_entidad_cuente_con_la_declaracion_jurada_del_exportador_y_2f8d95 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17636: aplica_a Obligacion_seran_de_aplicacion_las_disposiciones_sobre_posiciones_compensadas_del_acapite_i_f6d0d6 -> Sujeto_rol_alcance_capmin: sin mención
idx 17661: aplica_a Obligacion_seran_elegibles_para_el_exportador_quedando_obligadas_a_llevar_a_cabo_las_respon_4b4852 -> Sujeto_casa_de_cambio: sin mención
idx 17662: aplica_a Obligacion_seran_elegibles_para_el_exportador_quedando_obligadas_a_llevar_a_cabo_las_respon_4b4852 -> Sujeto_entidad_financiera: sin mención
idx 17664: aplica_a Obligacion_seran_transmitidas_por_la_entidad_emisora_a_la_entidad_por_la_cual_se_curse_el_p_b5eba9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17666: aplica_a Obligacion_si_al_quinto_dia_habil_aun_no_se_concreto_la_contrapartida_pactada_la_entidad_fi_0109e5 -> Sujeto_rol_alcance_capmin: sin mención
idx 17670: aplica_a Obligacion_si_como_resultado_del_proceso_de_debida_diligencia_surgen_ponderadores_mayores_a_11f34a -> Sujeto_rol_alcance_capmin: sin mención
idx 17672: aplica_a Obligacion_si_dichos_activos_fueran_de_caracter_rotativo_se_tendra_que_utilizar_el_vencimie_e22e90 -> Sujeto_rol_alcance_capmin: sin mención
idx 17674: aplica_a Obligacion_si_el_cajero_le_retiene_la_tarjeta_o_no_emite_el_comprobante_correspondiente_com_08c1b8 -> Sujeto_banco: sin mención
idx 17678: aplica_a Obligacion_si_el_cuentacorrentista_acredita_dicha_formulacion_remitir_el_cheque_o_certifica_11a8e8 -> Sujeto_banco: sin mención
idx 17684: aplica_a Obligacion_si_el_exportador_recibiera_cobros_por_tal_exportacion_estos_tambien_se_encontrar_2a3656 -> Sujeto_exportador: sin mención
idx 17686: aplica_a Obligacion_si_el_importador_percibiera_un_monto_en_moneda_extranjera_el_mismo_debera_ser_in_fbbc61 -> Sujeto_importador: sin mención
idx 17691: aplica_a Obligacion_si_en_el_monto_total_de_la_transferencia_se_incluyeran_otros_conceptos_que_no_fo_f25240 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17693: aplica_a Obligacion_si_existen_fondos_destinados_al_pago_de_fletes_de_importaciones_de_bienes_no_inc_418390 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17697: aplica_a Obligacion_si_la_entidad_aplica_metodo_delta_plus_codigo_314000_xx_codigo_554210_xx_codigo__b061d1 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17700: aplica_a Obligacion_si_la_entidad_aplica_metodo_simplificado_codigo_314000_xx_codigo_554100_xx__ric__9e60aa -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17703: aplica_a Obligacion_si_la_entidad_financiera_carece_de_suficiente_capital_para_efectuar_la_deduccion_2ab5d0 -> Sujeto_rol_alcance_capmin: sin mención
idx 17706: aplica_a Obligacion_si_la_entidad_financiera_no_pudiese_demostrar_que_los_acuerdos_de_neteo_cumplen__cd7667 -> Sujeto_rol_alcance_capmin: sin mención
idx 17708: aplica_a Obligacion_si_la_entidad_no_pudiera_realizar_el_calculo_del_precio_de_ejercicio_versus_prec_8c3ec4 -> Sujeto_rol_alcance_capmin: sin mención
idx 17711: aplica_a Obligacion_si_la_fecha_resultante_fuese_un_dia_no_habil_el_vencimiento_se_trasladara_al_pri_cc6217 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17715: aplica_a Obligacion_si_la_solicitud_de_liquidacion_de_la_operacion_por_anticipado_esta_sujeta_a_la_d_b80f24 -> Sujeto_rol_alcance_capmin: sin mención
idx 17717: aplica_a Obligacion_si_las_prestaciones_se_convienen_con_posterioridad_a_la_apertura_de_la_cuenta_se_96d72a -> Sujeto_banco: sin mención
idx 17733: aplica_a Obligacion_si_n_0_debera_observarse_una_exigencia_equivalente_al_limite_previsto_en_el_punt_fcacfe -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17736: aplica_a Obligacion_si_no_fuera_posible_acreditar_en_cuenta_a_la_vista_o_no_se_tratare_de_una_entida_669add -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17738: aplica_a Obligacion_si_para_financiar_sus_posiciones_en_productos_basicos_la_entidad_financiera_estu_c42e34 -> Sujeto_rol_alcance_capmin: sin mención
idx 17749: aplica_a Obligacion_si_se_carece_de_informacion_sobre_el_subyacente_para_el_calculo_se_tomara_el_tot_115e3f -> Sujeto_rol_alcance_capmin: sin mención
idx 17752: aplica_a Obligacion_si_se_deducen_los_margenes_deberan_informar_los_flujos_y_el_factor_de_descuento__ab4887 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17760: aplica_a Obligacion_si_se_incluyen_los_margenes_comerciales_solo_se_informaran_los_flujos_y_el_facto_0e7774 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17768: aplica_a Obligacion_si_tampoco_se_conocen_los_nocionales_se_debera_emplear_una_estimacion_conservado_a08c07 -> Sujeto_rol_alcance_capmin: sin mención
idx 17771: aplica_a Obligacion_si_una_vez_superados_los_inconvenientes_existentes_el_importador_efectuara_el_pa_7d7e9c -> Sujeto_exportador: sin mención
idx 17773: aplica_a Obligacion_siempre_que_se_disponga_de_ellas_y_en_la_medida_de_lo_posible_deberan_utilizarse_016d3b -> Sujeto_rol_alcance_capmin: sin mención
idx 17776: aplica_a Obligacion_siendo_los_responsables_ultimos_de_las_operaciones_de_aprobar_la_estrategia_glob_536779 -> Sujeto_entidad_financiera: sin mención
idx 17778: aplica_a Obligacion_similar_tratamiento_se_aplicara_a_las_estructuras_multinivel_de_clientes_entre_c_5e73dc -> Sujeto_miembro_compensador: sin mención
idx 17780: aplica_a Obligacion_simultaneamente_el_girado_procedera_a_comunicarlo_en_la_misma_forma_al_tenedor_o_cfde61 -> Sujeto_banco: sin mención
idx 17782: aplica_a Obligacion_sobre_la_posicion_neta_resultante_del_neteamiento_se_aplicaran_las_exigencias_de_aea332 -> Sujeto_rol_alcance_capmin: sin mención
idx 17799: aplica_a Obligacion_solicitar_fehacientemente_al_cuentacorrentista_dentro_de_las_48_horas_habiles_ba_06866d -> Sujeto_banco: sin mención
idx 17801: aplica_a Obligacion_solo_se_informara_el_codigo_de_moneda_m_para_los_codigos_en_los_que_esta_identif_ef400c -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 17804: aplica_a Obligacion_son_gestionadas_por_un_equipo_de_negociacion__cap_6_9_2_1_97c6f1 -> Sujeto_rol_alcance_capmin: sin mención
idx 17807: aplica_a Obligacion_soporte_de_residencia_de_la_aplicacion_fisico_y_logico__ctacte_3_3_8_3_6496cf -> Sujeto_banco: sin mención
idx 17810: aplica_a Obligacion_su_realizacion_se_efectuara_de_conformidad_con_las_disposiciones_operativas_esta_06fd84 -> Sujeto_banco: sin mención
idx 17812: aplica_a Obligacion_suministrar_la_informacion_en_tiempo_y_forma_a_la_sefyc_conforme_al_regimen_info_f450f0 -> Sujeto_rol_alcance_capmin: sin mención
idx 17814: aplica_a Obligacion_suministro_de_muestras_del_papel_a_utilizar_debe_cumplir_con_la_normativa_vigent_c4fde7 -> Sujeto_banco: sin mención
idx 17816: aplica_a Obligacion_supervisara_la_calidad_de_la_informacion_de_las_subsidiarias_y_sucursales_y_el_c_f2d421 -> Sujeto_entidad_financiera: sin mención
idx 17818: aplica_a Obligacion_supervise_a_la_alta_gerencia_de_la_entidad_ejerciendo_su_autoridad_para_obtener__544c12 -> Sujeto_entidad_financiera: sin mención
idx 17820: aplica_a Obligacion_sus_terminos_y_condiciones_deberan_incluir_una_disposicion_en_virtud_de_la_cual__497306 -> Sujeto_rol_alcance_capmin: sin mención
idx 17828: aplica_a Obligacion_tal_informacion_debera_ser_remitida_a_los_deudores_comprendidos_dentro_de_los_45_82e69f -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 17830: aplica_a Obligacion_tales_exclusiones_deberan_ser_divulgadas_conforme_a_los_requisitos_que_se_establ_e7dd72 -> Sujeto_rol_alcance_capmin: sin mención
idx 17832: aplica_a Obligacion_tambien_deben_ser_asentados_en_el_mencionado_registro_aquellos_reclamos_que_repr_8a9418 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17834: aplica_a Obligacion_tambien_se_contemplaran_los_debitos_por_la_venta_de_cheques_de_mostrador_y_chequ_7242d9 -> Sujeto_banco: sin mención
idx 17865: aplica_a Obligacion_tanto_la_entidad_financiera_cliente_como_el_miembro_compensador_deberan_dar_a_es_93529c -> Sujeto_miembro_compensador: sin mención
idx 17866: aplica_a Obligacion_tanto_la_entidad_financiera_cliente_como_el_miembro_compensador_deberan_dar_a_es_93529c -> Sujeto_rol_alcance_capmin: sin mención
idx 17910: aplica_a Obligacion_tasa_de_interes_la_convenida_libremente_entre_las_partes_que_se_calculara_sobre__82cfc0 -> Sujeto_entidad_financiera: sin mención
idx 17923: aplica_a Obligacion_tendra_caracter_de_declaracion_jurada__pagjub_2_1_669a1a -> Sujeto_rol_alcance_pagjub: sin mención
idx 17925: aplica_a Obligacion_tener_las_cuentas_al_dia__ctacte_1_5_2_1_96b07f -> Sujeto_banco: sin mención
idx 17927: aplica_a Obligacion_tener_un_adecuado_sistema_de_informacion_que_permita_conocer_en_forma_permanente_bb9846 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 17929: aplica_a Obligacion_tipo_marcas_de_seguridad_etc__ctacte_3_3_8_4_4f172d -> Sujeto_banco: sin mención
idx 17931: aplica_a Obligacion_toda_esa_documentacion_debera_ser_apropiadamente_revisada_por_consultores_legale_e7ba25 -> Sujeto_rol_alcance_capmin: sin mención
idx 17933: aplica_a Obligacion_toda_la_informacion_que_se_solicite_tanto_en_la_originacion_del_prestamo_como_du_e3ecce -> Sujeto_rol_alcance_capmin: sin mención
idx 17935: aplica_a Obligacion_todas_las_casas_operativas_de_estos_sujetos_obligados_deberan_entregar_a_los_ref_962b99 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17937: aplica_a Obligacion_todas_las_comisiones_cargos_costos_gastos_seguros_y_o_cualquier_otro_concepto_ex_e01679 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 17941: aplica_a Obligacion_todas_las_entidades_financieras_y_casas_de_cambio_estan_obligadas_a_llevar_a_cab_735a56 -> Sujeto_casa_de_cambio: sin mención
idx 17942: aplica_a Obligacion_todas_las_entidades_financieras_y_casas_de_cambio_estan_obligadas_a_llevar_a_cab_735a56 -> Sujeto_entidad_financiera: sin mención
idx 17944: aplica_a Obligacion_todas_las_informaciones_que_se_remitan_al_banco_central_de_la_republica_argentin_8e90ec -> Sujeto_banco: sin mención
idx 17946: aplica_a Obligacion_todas_las_liquidaciones_de_las_operaciones_de_futuros_en_mercados_regulados_forw_e3a848 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17948: aplica_a Obligacion_todo_activo_que_la_entidad_financiera_constituya_en_garantia_de_estas_operacione_6e03f1 -> Sujeto_rol_alcance_capmin: sin mención
idx 17954: aplica_a Obligacion_todos_los_activos_incluidos_en_la_cartera_de_negociacion_que_verifiquen_las_cond_93d2ba -> Sujeto_rol_alcance_capmin: sin mención
idx 17956: aplica_a Obligacion_todos_los_derechos_inherentes_a_los_documentos_a_cobrar_y_creditos_deberan_ser_t_16f931 -> Sujeto_rol_alcance_capmin: sin mención
idx 17958: aplica_a Obligacion_todos_los_eventos_desencadenantes_que_puedan_afectar_el_orden_de_prelacion_en_lo_7b4240 -> Sujeto_rol_alcance_capmin: sin mención
idx 17960: aplica_a Obligacion_todos_los_motivos_en_que_se_funda_el_rechazo_del_cheque_deberan_consignarse__cta_3a2166 -> Sujeto_banco: sin mención
idx 17964: aplica_a Obligacion_tomar_por_defecto_como_cuenta_primaria_la_cuenta_en_moneda_extranjera_del_client_9cf9b1 -> Sujeto_entidad_financiera: sin mención
idx 17966: aplica_a Obligacion_tomar_registro_de_las_liquidaciones_de_divisas_asociadas_a_devoluciones_de_pagos_668e92 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17968: aplica_a Obligacion_tome_conocimiento_de_la_politica_de_gobierno_societario_de_sus_subsidiarias__lin_713b82 -> Sujeto_entidad_financiera: sin mención
idx 17970: aplica_a Obligacion_trabajar_en_estrecha_colaboracion_en_su_caso_con_el_comite_de_gestion_de_riesgos_78a6df -> Sujeto_entidad_financiera: sin mención
idx 17972: aplica_a Obligacion_transcurrido_el_periodo_de_30_dias_la_entidad_financiera_efectuara_el_cierre_de__ad810a -> Sujeto_banco: sin mención
idx 17975: aplica_a Obligacion_transferir_los_fondos_remanentes_a_las_cuentas_pertenecientes_a_las_agrupaciones_2713f9 -> Sujeto_banco: sin mención
idx 17978: aplica_a Obligacion_transmitir_al_repositorio_en_forma_integra_los_echeq_y_todas_las_novedades_relac_5588d4 -> Sujeto_banco: sin mención
idx 17981: aplica_a Obligacion_una_ecai_debera_ser_independiente_y_no_estar_sujeta_a_presiones_politicas_ni_eco_335ff5 -> Sujeto_ecai: sin mención
idx 17983: aplica_a Obligacion_una_entidad_financiera_debe_registrar_el_aporte_de_capital_en_el_regimen_informa_92ba57 -> Sujeto_entidad_financiera: sin mención
idx 17985: aplica_a Obligacion_una_proporcion_sustancial_debe_ser_variable_y_pagarse_en_funcion_de_una_evaluaci_6e3511 -> Sujeto_entidad_financiera: sin mención
idx 17987: aplica_a Obligacion_una_proporcion_sustancial_del_incentivo_economico_variable_se_abone_de_manera_di_8d5c3c -> Sujeto_entidad_financiera: sin mención
idx 17989: aplica_a Obligacion_utilice_efectivamente_el_trabajo_llevado_a_cabo_por_las_auditorias_interna_y_ext_41d889 -> Sujeto_entidad_financiera: sin mención
idx 17991: aplica_a Obligacion_utilicen_en_forma_oportuna_y_eficaz_las_conclusiones_de_la_auditoria_interna__li_4c6ee2 -> Sujeto_entidad_financiera: sin mención
idx 17993: aplica_a Obligacion_utilizados_los_plazos_maximos_con_sus_sucesivas_renovaciones_la_entidad_registra_3fb8ce -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17995: aplica_a Obligacion_utilizados_los_plazos_maximos_con_sus_sucesivas_renovaciones_la_entidad_registra_8d8760 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 17998: aplica_a Obligacion_utilizar_efectivamente_el_trabajo_llevado_a_cabo_por_las_auditorias_interna_y_ex_e96e92 -> Sujeto_entidad_financiera: sin mención
idx 18000: aplica_a Obligacion_utilizar_la_documentacion_habitual_que_emplean_en_los_contratos_presenciales__pr_1bd4af -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 18002: aplica_a Obligacion_velar_por_el_correcto_funcionamiento_de_los_mecanismos_de_seguridad_convenidos_p_dd14e4 -> Sujeto_banco: sin mención
idx 18005: aplica_a Obligacion_velar_por_el_cumplimiento_de_las_disposiciones_de_la_seccion_2_en_todos_los_punt_81e0ae -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 18007: aplica_a Obligacion_velar_por_el_cumplimiento_de_los_requerimientos_informativos_del_bcra_que_son_ma_e184f1 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 18009: aplica_a Obligacion_verificar_el_adecuado_funcionamiento_del_proceso_de_analisis_de_las_causas_gener_08b056 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 18013: aplica_a Obligacion_verificar_el_cumplimiento_de_todos_los_requisitos_establecidos_por_la_normativa__d49dc6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18015: aplica_a Obligacion_verificar_en_el_caso_de_operaciones_financiadas_que_la_misma_queda_encuadrada_co_a104ba -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18023: aplica_a Obligacion_verificar_que_la_documentacion_presentada_por_el_importador_sea_consistente_con__028503 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18025: aplica_a Obligacion_verificar_que_la_publicidad_que_por_cualquier_medio_realice_el_sujeto_obligado_s_3b76e3 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 18027: aplica_a Obligacion_verificar_que_se_cumplan_las_condiciones_especificadas_a_continuacion__ext_3_3_cafc57 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18029: aplica_a Obligacion_vigilar_el_adecuado_funcionamiento_de_los_procesos_relacionados_con_la_proteccio_34827f -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 18031: aplica_a Obligacion_vigilar_el_ejercicio_de_las_responsabilidades_asignadas__lingob_3_1_4_33682b -> Sujeto_entidad_financiera: sin mención
idx 18033: aplica_a Obligacion_vigilar_la_evaluacion_periodica_del_cumplimiento_de_la_legislacion_y_regulacion__768532 -> Sujeto_entidad_financiera: sin mención
idx 18035: aplica_a Obligacion_vigilaran_la_integridad_de_la_informacion_financiera_y_no_financiera_de_las_tran_eebf93 -> Sujeto_entidad_financiera: sin mención
idx 18037: aplica_a Obligacion_vigile_el_diseno_y_el_funcionamiento_en_la_entidad_del_sistema_de_retribuciones__96915f -> Sujeto_entidad_financiera: sin mención
idx 18041: aplica_a Operacion_abono_certificado_nominativo_al_presentante_265569 -> Sujeto_banco: sin mención
idx 18053: aplica_a Operacion_acceso_a_informacion_aduanera_basica_3a86fb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18055: aplica_a Operacion_acceso_a_informacion_detallada_aduanera_be92ea -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18057: aplica_a Operacion_acceso_a_mercado_cambios_con_financiacion_importaciones_934d06 -> Sujeto_cliente: sin mención
idx 18059: aplica_a Operacion_acceso_a_mercado_cambios_fondos_endeudamiento_9546ca -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18087: aplica_a Operacion_acceso_a_mercado_de_cambios_para_pago_de_deudas_elegibles_e2d614 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18152: aplica_a Operacion_acceso_al_mercado_de_cambios_cliente_con_facturas_apocrifas_bf6a32 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18154: aplica_a Operacion_acceso_al_mercado_de_cambios_como_apoderado_0ed97e -> Sujeto_entidad_cambiaria: sin mención
idx 18155: aplica_a Operacion_acceso_al_mercado_de_cambios_como_apoderado_0ed97e -> Sujeto_entidad_financiera: sin mención
idx 18178: aplica_a Operacion_acceso_al_mercado_de_cambios_con_financiacion_de_importacion_fee3fe -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18181: aplica_a Operacion_acceso_al_mercado_de_cambios_exportadores_4939da -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18184: aplica_a Operacion_acceso_al_mercado_de_cambios_garantias_en_moneda_extranjera_8cf221 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18204: aplica_a Operacion_acceso_al_mercado_de_cambios_liquidacion_de_endeudamiento_8087bf -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18219: aplica_a Operacion_acceso_al_mercado_de_cambios_pago_intereses_y_capital_40c718 -> Sujeto_vpu_rigi: sin mención
idx 18224: aplica_a Operacion_acceso_al_mercado_de_cambios_pago_titulos_deuda_17bb96 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18227: aplica_a Operacion_acceso_al_mercado_de_cambios_pagos_de_endeudamientos_refinanciados_fab730 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18234: aplica_a Operacion_acceso_al_mercado_de_cambios_para_cancelacion_de_cartas_de_credito_o_letras_aval_96609f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18238: aplica_a Operacion_acceso_al_mercado_de_cambios_para_cancelacion_de_lineas_8815e4 -> Sujeto_entidad_financiera: sin mención
idx 18246: aplica_a Operacion_acceso_al_mercado_de_cambios_para_cancelacion_de_lineas_de_credito_2d4f92 -> Sujeto_entidad_financiera: sin mención
idx 18254: aplica_a Operacion_acceso_al_mercado_de_cambios_para_endeudamientos_financieros_8212fc -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18275: aplica_a Operacion_acceso_al_mercado_de_cambios_para_pago_7b4cb8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18279: aplica_a Operacion_acceso_al_mercado_de_cambios_para_pago_al_exterior_8e7327 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18282: aplica_a Operacion_acceso_al_mercado_de_cambios_para_pago_de_capital_47d879 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18291: aplica_a Operacion_acceso_al_mercado_de_cambios_para_pagos_de_servicios_de_no_residentes_279ff0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18294: aplica_a Operacion_acceso_al_mercado_de_cambios_por_pago_deuda_comercial_servicios_8b2530 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18296: aplica_a Operacion_acceso_al_mercado_de_cambios_simultaneo_con_liquidacion_e54a47 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18298: aplica_a Operacion_acceso_anticipado_al_mercado_de_cambios_por_deuda_de_tarjetas_e255a7 -> Sujeto_entidad_financiera: sin mención
idx 18302: aplica_a Operacion_acceso_financiaciones_comerciales_importacion_bienes_capital_dcbb33 -> Sujeto_entidad_cambiaria: sin mención
idx 18303: aplica_a Operacion_acceso_financiaciones_comerciales_importacion_bienes_capital_dcbb33 -> Sujeto_entidad_financiera: sin mención
idx 18320: aplica_a Operacion_acceso_informacion_arca_requisitos_exportacion_64c8fe -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18322: aplica_a Operacion_acceso_informacion_permisos_embarque_secoexpo_166dfd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18324: aplica_a Operacion_acceso_mercado_cambios_cancelacion_garantias_financieras_0d0f8a -> Sujeto_entidad_financiera: sin mención
idx 18328: aplica_a Operacion_acceso_mercado_cambios_pago_deudas_elegibles_a1d5bd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18330: aplica_a Operacion_acceso_mercado_cambios_para_pago_importacion_532770 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18333: aplica_a Operacion_acceso_mercado_de_cambios_pago_capital_deudas_elegibles_97bac7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18336: aplica_a Operacion_acceso_simultaneo_mercado_cambios_y_liquidacion_fondos_anticipos_prefinanciacion_b5648a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18343: aplica_a Operacion_acreditacion_de_cheque_en_cuenta_829c1c -> Sujeto_entidad_girada: sin mención
idx 18345: aplica_a Operacion_acreditacion_de_comisiones_en_cuenta_corriente_163a86 -> Sujeto_rol_alcance_pagjub: sin mención
idx 18350: aplica_a Operacion_acreditacion_de_cuenta_tras_vencimiento_159b84 -> Sujeto_banco: sin mención
idx 18360: aplica_a Operacion_acreditacion_en_cuenta_transitoria_del_bcra_5820a3 -> Sujeto_bcra: sin mención
idx 18375: aplica_a Operacion_acumulacion_fondos_de_cobros_en_cuentas_del_exterior_pais_048c68 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18390: aplica_a Operacion_acumular_fondos_de_exportaciones_en_cuentas_en_me_dbb31d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18424: aplica_a Operacion_administracion_del_rccr_1eca80 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 18436: aplica_a Operacion_administracion_del_rdja_3bfc55 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 18440: aplica_a Operacion_administracion_del_rri_07a27b -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 18452: aplica_a Operacion_adquisicion_titulos_publicos_pesos_f76299 -> Sujeto_sector_publico_no_financiero: sin mención
idx 18464: aplica_a Operacion_agregacion_de_epf_nivel_de_conjunto_de_neteo_4420f7 -> Sujeto_rol_alcance_capmin: sin mención
idx 18484: aplica_a Operacion_anticipo_de_fondos_propios_del_exterior_f7e482 -> Sujeto_exportador: sin mención
idx 18492: aplica_a Operacion_anticipos_exportaciones_argentinas_pesos_bfa7bc -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18496: aplica_a Operacion_anticipos_y_prefinanciaciones_de_exportaciones_no_liquidadas_e80570 -> Sujeto_exportador: sin mención
idx 18500: aplica_a Operacion_apertura_cuenta_corriente_bancaria_agrupaciones_politicas_6bae99 -> Sujeto_banco: sin mención
idx 18508: aplica_a Operacion_apertura_de_cuenta_especial_9bced2 -> Sujeto_banco: sin mención
idx 18513: aplica_a Operacion_apertura_de_cuentas_corrientes_especiales_4a48a2 -> Sujeto_rol_alcance_pagjub: sin mención
idx 18520: aplica_a Operacion_aplicacion_cobros_divisas_exportaciones_bienes_8f0c3b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18522: aplica_a Operacion_aplicacion_cobros_exportaciones_bienes_regimen_fomento_inversion_2961c0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18526: aplica_a Operacion_aplicacion_cobros_exportaciones_operaciones_financieras_985227 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18531: aplica_a Operacion_aplicacion_de_calificacion_unica_ecai_618426 -> Sujeto_rol_alcance_capmin: sin mención
idx 18533: aplica_a Operacion_aplicacion_de_capacidad_de_prestamo_a_titulos_de_deuda_y_certificados_de_partici_0f737a -> Sujeto_entidad_financiera: sin mención
idx 18565: aplica_a Operacion_aplicacion_de_cobros_a_cancelacion_de_financiacion_28df57 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18590: aplica_a Operacion_aplicacion_de_ponderadores_de_riesgo_segun_grupo_164f65 -> Sujeto_rol_alcance_capmin: sin mención
idx 18595: aplica_a Operacion_aplicacion_de_tratamiento_a_exposiciones_hipotecarias_grupo_2_0537e8 -> Sujeto_rol_alcance_capmin: sin mención
idx 18700: aplica_a Operacion_aplicacion_tratamiento_exposicion_incumplida_0bd0a7 -> Sujeto_rol_alcance_capmin: sin mención
idx 18707: aplica_a Operacion_aporte_de_titulos_valores_publicos_nacionales_000c92 -> Sujeto_rol_alcance_capmin: sin mención
idx 18710: aplica_a Operacion_apoyo_crediticio_con_garantia_hipotecaria_residencial_116349 -> Sujeto_rol_alcance_capmin: sin mención
idx 18716: aplica_a Operacion_arbitrajes_y_canjes_en_el_exterior_55702f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18718: aplica_a Operacion_arreglos_privados_con_refinanciacion_48c49b -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 18740: aplica_a Operacion_asignacion_coeficientes_segun_tipo_de_bien_59f28c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18748: aplica_a Operacion_asignacion_de_derivados_a_clases_de_activos_d08ce7 -> Sujeto_rol_alcance_capmin: sin mención
idx 18753: aplica_a Operacion_asignacion_de_grado_c_a_exposiciones_9a55dd -> Sujeto_rol_alcance_capmin: sin mención
idx 18755: aplica_a Operacion_asignacion_de_grado_de_riesgo_a_exposiciones_7e8e70 -> Sujeto_rol_alcance_capmin: sin mención
idx 18757: aplica_a Operacion_asignacion_de_instrumentos_segun_plazo_residual_o_tasa_variable_d482f2 -> Sujeto_rol_alcance_capmin: sin mención
idx 18766: aplica_a Operacion_asignacion_de_ponderador_parte_cubierta_6b4f1b -> Sujeto_rol_alcance_capmin: sin mención
idx 18769: aplica_a Operacion_asignacion_de_ponderadores_de_riesgo_mediante_scra_fadbf8 -> Sujeto_rol_alcance_capmin: sin mención
idx 18777: aplica_a Operacion_asignacion_ponderador_riesgo_0_financiacion_sector_publico_ec5cd8 -> Sujeto_rol_alcance_capmin: sin mención
idx 18779: aplica_a Operacion_asignacion_ponderador_riesgo_soberano_gobiernos_no_financieros_y_bcra_e6969d -> Sujeto_rol_alcance_capmin: sin mención
idx 18788: aplica_a Operacion_atender_cheques_emitidos_hasta_dia_anterior_a_notificacion_f33cdb -> Sujeto_banco: sin mención
idx 18791: aplica_a Operacion_aumento_capacidad_transporte_exportaciones_obras_infraestructura_portuaria_85234b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 18795: aplica_a Operacion_autorizacion_aportes_capital_instrumentos_deuda_b38a10 -> Sujeto_rol_alcance_capmin: sin mención
idx 18813: aplica_a Operacion_aval_de_cheques_por_depositaria_2ea9ef -> Sujeto_entidad_depositaria: sin mención
idx 18816: aplica_a Operacion_avales_fianzas_y_otras_responsabilidades_c4d64b -> Sujeto_rol_alcance_capmin: sin mención
idx 18878: aplica_a Operacion_calculo_bi_combinaciones_de_negocios_e6a2af -> Sujeto_rol_alcance_capmin: sin mención
idx 18880: aplica_a Operacion_calculo_capital_riesgo_especifico_acciones_9cb499 -> Sujeto_rol_alcance_capmin: sin mención
idx 18882: aplica_a Operacion_calculo_capital_riesgo_general_mercado_acciones_7f0654 -> Sujeto_rol_alcance_capmin: sin mención
idx 18884: aplica_a Operacion_calculo_capital_riesgo_operacional_grupo_2_7ad371 -> Sujeto_rol_alcance_capmin: sin mención
idx 18902: aplica_a Operacion_calculo_cva_neto_de_dva_d851d1 -> Sujeto_rol_alcance_capmin: sin mención
idx 18904: aplica_a Operacion_calculo_de_activo_ponderado_por_riesgo_b8fb4e -> Sujeto_rol_alcance_capmin: sin mención
idx 18909: aplica_a Operacion_calculo_de_cambio_diario_portafolio_de_activos_ebb3c1 -> Sujeto_rol_alcance_capmin: sin mención
idx 18912: aplica_a Operacion_calculo_de_cr_acuerdo_de_margen_sobre_multiples_conjuntos_062d8f -> Sujeto_rol_alcance_capmin: sin mención
idx 18914: aplica_a Operacion_calculo_de_ead_neta_de_cva_dbac58 -> Sujeto_rol_alcance_capmin: sin mención
idx 18916: aplica_a Operacion_calculo_de_epf_exposicion_potencial_futura_a2131a -> Sujeto_rol_alcance_capmin: sin mención
idx 18918: aplica_a Operacion_calculo_de_exigencia_capital_riesgo_gamma_2eb9fb -> Sujeto_rol_alcance_capmin: sin mención
idx 18920: aplica_a Operacion_calculo_de_exigencia_capital_riesgo_vega_25a414 -> Sujeto_rol_alcance_capmin: sin mención
idx 18922: aplica_a Operacion_calculo_de_exigencia_capital_subtramo_cubierto_82d66e -> Sujeto_rol_alcance_capmin: sin mención
idx 18943: aplica_a Operacion_calculo_de_exigencia_capital_subtramo_no_cubierto_42f471 -> Sujeto_rol_alcance_capmin: sin mención
idx 18953: aplica_a Operacion_calculo_de_exigencia_de_capital_por_cva_e4a7a8 -> Sujeto_rol_alcance_capmin: sin mención
idx 18975: aplica_a Operacion_calculo_de_exigencia_de_capital_riesgo_credito_contraparte_derivados_afb07d -> Sujeto_rol_alcance_capmin: sin mención
idx 18978: aplica_a Operacion_calculo_de_exigencia_de_capital_riesgo_credito_contraparte_sft_284113 -> Sujeto_rol_alcance_capmin: sin mención
idx 18994: aplica_a Operacion_calculo_de_nocional_ajustado_a_nivel_de_operacion_f9f550 -> Sujeto_rol_alcance_capmin: sin mención
idx 19001: aplica_a Operacion_calculo_de_posiciones_en_derivados_281e88 -> Sujeto_rol_alcance_capmin: sin mención
idx 19006: aplica_a Operacion_calculo_de_responsabilidad_patrimonial_computable_1109a0 -> Sujeto_rol_alcance_capmin: sin mención
idx 19024: aplica_a Operacion_calculo_del_importe_de_la_posicion_de_titulizacion_e30bd0 -> Sujeto_rol_alcance_capmin: sin mención
idx 19027: aplica_a Operacion_calculo_del_monto_maximo_de_certificaciones_2de0b2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19075: aplica_a Operacion_calculo_exigencia_capital_riesgo_precio_opciones_20f1d0 -> Sujeto_rol_alcance_capmin: sin mención
idx 19077: aplica_a Operacion_calculo_exigencia_capital_riesgo_tasa_interes_d2820e -> Sujeto_rol_alcance_capmin: sin mención
idx 19080: aplica_a Operacion_calculo_exigencia_por_riesgo_de_cambio_531343 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 19090: aplica_a Operacion_calculo_exigencia_riesgo_opciones_7ee58f -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 19097: aplica_a Operacion_calculo_exposicion_ajustada_operaciones_neteo_d9238e -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 19106: aplica_a Operacion_calculo_exposicion_financiacion_titulos_valores_9e9bf7 -> Sujeto_rol_alcance_capmin: sin mención
idx 19114: aplica_a Operacion_calculo_monto_maximo_certificaciones_anuales_bffee1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19121: aplica_a Operacion_calculo_ponderador_exposicion_garantia_hipotecaria_no_normativa_32967a -> Sujeto_rol_alcance_capmin: sin mención
idx 19130: aplica_a Operacion_calculo_ponderador_riesgo_posicion_titulizacion_3d232c -> Sujeto_rol_alcance_capmin: sin mención
idx 19132: aplica_a Operacion_calculo_posicion_abierta_neta_moneda_extranjera_ae2049 -> Sujeto_rol_alcance_capmin: sin mención
idx 19138: aplica_a Operacion_calculo_posicion_en_opciones_759c89 -> Sujeto_rol_alcance_capmin: sin mención
idx 19140: aplica_a Operacion_calculo_promedio_erc_periodos_marzo_diciembre_2015_8c1b22 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 19142: aplica_a Operacion_calculo_prudente_de_ltv_807d58 -> Sujeto_rol_alcance_capmin: sin mención
idx 19162: aplica_a Operacion_cambio_de_entidad_responsable_534693 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19199: aplica_a Operacion_cancelacion_de_consumos_en_dolares_de_tarjetas_5d8204 -> Sujeto_entidad_financiera: sin mención
idx 19201: aplica_a Operacion_cancelacion_de_consumos_en_dolares_empresas_emisoras_0f4431 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 19214: aplica_a Operacion_cancelacion_de_lineas_de_credito_del_exterior_4d830e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19234: aplica_a Operacion_cancelacion_garantias_comerciales_importacion_4d91d8 -> Sujeto_entidad_financiera: sin mención
idx 19236: aplica_a Operacion_canje_arbitraje_con_fondos_en_cuenta_local_3f26e1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19241: aplica_a Operacion_canje_y_arbitraje_fondos_en_cuenta_local_498bdc -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19295: aplica_a Operacion_clasificacion_de_cliente_con_alto_riesgo_ca015e -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 19297: aplica_a Operacion_clasificacion_de_credito_en_cartera_comercial_ed966c -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 19299: aplica_a Operacion_clasificacion_de_deuda_criterio_basico_435820 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 19301: aplica_a Operacion_clasificacion_de_deudor_con_alto_riesgo_059d6e -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 19304: aplica_a Operacion_clasificacion_de_deudor_en_categoria_con_problemas_23b112 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 19306: aplica_a Operacion_clasificacion_de_deudor_en_situacion_normal_af3f13 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 19309: aplica_a Operacion_clasificacion_de_deudores_pautas_objetivas_807095 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 19322: aplica_a Operacion_clasificacion_de_exposiciones_hipotecarias_normativas_no_normativas_016143 -> Sujeto_rol_alcance_capmin: sin mención
idx 19326: aplica_a Operacion_clasificacion_en_categoria_irrecuperable_201e68 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 19332: aplica_a Operacion_clasificacion_en_grupos_por_importancia_sistemica_f775cc -> Sujeto_rol_alcance_capmin: sin mención
idx 19334: aplica_a Operacion_clasificacion_irrecuperable_clientes_sector_privado_ed7193 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 19338: aplica_a Operacion_cobertura_con_swap_incumplimiento_crediticio_937e84 -> Sujeto_rol_alcance_capmin: sin mención
idx 19343: aplica_a Operacion_cobertura_riesgo_credito_activos_garantia_b15054 -> Sujeto_rol_alcance_capmin: sin mención
idx 19352: aplica_a Operacion_cobro_de_exportacion_de_servicios_a_no_residente_6b6ada -> Sujeto_vpu_rigi: sin mención
idx 19358: aplica_a Operacion_cobro_de_exportacion_percibido_post_embarque_62d970 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19368: aplica_a Operacion_cobro_efectivo_de_divisas_del_embarque_a20a08 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19383: aplica_a Operacion_cobro_local_por_exportacion_regimen_ranchos_233e11 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19385: aplica_a Operacion_cobro_o_adeudo_de_importes_al_usuario_61d23e -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 19403: aplica_a Operacion_cobros_exportaciones_argentinas_pesos_be6caa -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19418: aplica_a Operacion_cobros_exportaciones_ingreso_y_liquidacion_mercado_de_cambios_vpu_rigi_ac3768 -> Sujeto_vpu_rigi: sin mención
idx 19425: aplica_a Operacion_cobros_y_pagos_de_jubilaciones_y_pensiones_a29bca -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19432: aplica_a Operacion_compensacion_integra_posiciones_cubiertas_derivados_credito_861b3d -> Sujeto_rol_alcance_capmin: sin mención
idx 19451: aplica_a Operacion_compensacion_posiciones_cortas_y_largas_5f55e6 -> Sujeto_rol_alcance_capmin: sin mención
idx 19455: aplica_a Operacion_compra_de_bienes_al_exterior_con_anticipo_6a4152 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19464: aplica_a Operacion_compra_de_billetes_en_moneda_extranjera_turismo_76ea7b -> Sujeto_persona_humana: sin mención
idx 19467: aplica_a Operacion_compra_de_billetes_y_depositos_en_moneda_extranjera_fae2db -> Sujeto_persona_humana: sin mención
idx 19471: aplica_a Operacion_compra_de_divisas_financiacion_local_otorgada_726d8d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19473: aplica_a Operacion_compra_de_divisas_linea_de_credito_exterior_242569 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19502: aplica_a Operacion_compra_de_moneda_extranjera_debito_en_cuenta_local_9d7638 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19506: aplica_a Operacion_compra_de_moneda_extranjera_para_constitucion_de_garantias_c2c477 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19508: aplica_a Operacion_compra_de_moneda_extranjera_para_formacion_de_activos_externos_1ef9de -> Sujeto_fideicomiso: sin mención
idx 19509: aplica_a Operacion_compra_de_moneda_extranjera_para_formacion_de_activos_externos_1ef9de -> Sujeto_fondo_comun_de_inversion: sin mención
idx 19510: aplica_a Operacion_compra_de_moneda_extranjera_para_formacion_de_activos_externos_1ef9de -> Sujeto_gobierno_local: sin mención
idx 19512: aplica_a Operacion_compra_de_moneda_extranjera_para_formacion_de_activos_externos_1ef9de -> Sujeto_universalidad: sin mención
idx 19525: aplica_a Operacion_compra_moneda_extranjera_billetes_depositos_debito_cuenta_770928 -> Sujeto_persona_humana: sin mención
idx 19530: aplica_a Operacion_compra_o_venta_de_futuros_y_contratos_a_termino_07ee16 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 19538: aplica_a Operacion_compraventa_de_billetes_y_metales_preciosos_d5b6b1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19540: aplica_a Operacion_compraventa_titulos_valores_cable_sobre_cuentas_bancarias_exterior_a2fffc -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19542: aplica_a Operacion_compraventa_titulos_valores_con_liquidacion_moneda_extranjera_9d089c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19548: aplica_a Operacion_computacion_de_precios_de_liquidacion_6f9d2a -> Sujeto_rol_alcance_capmin: sin mención
idx 19554: aplica_a Operacion_computo_de_exigencia_capital_titulos_valores_29ac8e -> Sujeto_rol_alcance_capmin: sin mención
idx 19559: aplica_a Operacion_computo_de_financiaciones_como_ingresadas_y_liquidadas_en_cambios_6da3c0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19560: aplica_a Operacion_computo_de_financiaciones_como_ingresadas_y_liquidadas_en_cambios_6da3c0 -> Sujeto_vpu_rigi: sin mención
idx 19577: aplica_a Operacion_computo_diario_de_integracion_de_capital_7ab6a2 -> Sujeto_rol_alcance_capmin: sin mención
idx 19588: aplica_a Operacion_computo_mensual_de_conceptos_base_individual_y_consolidada_6c2637 -> Sujeto_rol_alcance_capmin: sin mención
idx 19595: aplica_a Operacion_comunicacion_de_identificacion_del_destinatario_d9d4c6 -> Sujeto_banco: sin mención
idx 19642: aplica_a Operacion_confeccion_boleto_de_compra_financiacion_24d579 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19657: aplica_a Operacion_confeccion_de_dos_boletos_sin_movimiento_fondos_rioc_8a899e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19666: aplica_a Operacion_conformacion_de_comite_de_proteccion_8997f8 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 19668: aplica_a Operacion_conservacion_y_remision_de_datos_seccion_8_db1267 -> Sujeto_rol_alcance_lavdin: sin mención
idx 19670: aplica_a Operacion_consideracion_de_ccp_como_qccp_por_entidades_financieras_833bf8 -> Sujeto_rol_alcance_capmin: sin mención
idx 19676: aplica_a Operacion_consignacion_de_exigencia_por_riesgo_de_tipo_de_cambio_eeffbb -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 19681: aplica_a Operacion_consignacion_de_valor_de_exigencia_riesgo_especifico_196959 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 19685: aplica_a Operacion_consignacion_exigencia_riesgo_commodities_742df5 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 19702: aplica_a Operacion_constancia_de_cobro_extendida_por_acreedor_8ff3cc -> Sujeto_banco: sin mención
idx 19704: aplica_a Operacion_constancia_de_cobro_extendida_por_tenedor_legitimado_echeq_351234 -> Sujeto_banco: sin mención
idx 19707: aplica_a Operacion_constitucion_de_fideicomisos_financieros_del_multilateral_311e6e -> Sujeto_entidad_financiera: sin mención
idx 19709: aplica_a Operacion_constitucion_de_garantias_en_moneda_extranjera_984924 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19711: aplica_a Operacion_constitucion_de_previsiones_por_riesgo_incobrabilidad_11ad96 -> Sujeto_rol_alcance_capmin: sin mención
idx 19715: aplica_a Operacion_consumos_exterior_con_debito_inmediato_6da32c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19732: aplica_a Operacion_conversion_derivados_a_posiciones_subyacentes_a5217d -> Sujeto_rol_alcance_capmin: sin mención
idx 19736: aplica_a Operacion_conversion_partidas_fuera_de_balance_ccf_2e1b79 -> Sujeto_rol_alcance_capmin: sin mención
idx 19767: aplica_a Operacion_cumplimiento_seguimiento_exportacion_6c18d7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19779: aplica_a Operacion_debito_de_comisiones_pactadas_libremente_52a0b3 -> Sujeto_banco: sin mención
idx 19796: aplica_a Operacion_debito_de_cuenta_corriente_ordenes_inconsistentes_f49b0a -> Sujeto_rol_alcance_pagjub: sin mención
idx 19800: aplica_a Operacion_debito_de_multa_de_la_cuenta_corriente_bcra_b959c0 -> Sujeto_banco: sin mención
idx 19810: aplica_a Operacion_debito_ordenes_de_pago_impagas_en_cuenta_corriente_bcra_6478cc -> Sujeto_rol_alcance_pagjub: sin mención
idx 19812: aplica_a Operacion_debito_y_reserva_de_importes_cheque_certificado_f28e4a -> Sujeto_banco: sin mención
idx 19831: aplica_a Operacion_deduccion_de_titulos_subordinados_de_otras_ef_9f360c -> Sujeto_rol_alcance_capmin: sin mención
idx 19833: aplica_a Operacion_deduccion_saldos_en_cuentas_de_corresponsalia_ec223d -> Sujeto_rol_alcance_capmin: sin mención
idx 19836: aplica_a Operacion_definicion_de_conjuntos_de_cobertura_por_clase_de_activo_b8a42f -> Sujeto_rol_alcance_capmin: sin mención
idx 19839: aplica_a Operacion_demanda_judicial_para_cobro_de_acreencia_aa93cb -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 19842: aplica_a Operacion_denuncia_de_extravio_sustraccion_o_adulteracion_de_cheques_c1dcd4 -> Sujeto_banco: sin mención
idx 19856: aplica_a Operacion_deposito_cobros_exportacion_bienes_7e29e5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 19888: aplica_a Operacion_deposito_de_importes_con_intereses_en_casa_girada_6177cc -> Sujeto_banco: sin mención
idx 19898: aplica_a Operacion_deposito_en_efectivo_en_entidad_financiera_d75244 -> Sujeto_rol_alcance_capmin: sin mención
idx 19904: aplica_a Operacion_deposito_para_negociacion_en_bolsas_142e18 -> Sujeto_banco: sin mención
idx 19924: aplica_a Operacion_designacion_de_directivo_responsable_de_proteccion_4bc473 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 19925: aplica_a Operacion_designacion_de_directivo_responsable_de_proteccion_4bc473 -> Sujeto_entidad_financiera: sin mención
idx 19926: aplica_a Operacion_designacion_de_directivo_responsable_de_proteccion_4bc473 -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 19932: aplica_a Operacion_designacion_de_entidad_financiera_para_seguimiento_de_proyecto_5890c8 -> Sujeto_exportador: sin mención
idx 20030: aplica_a Operacion_determinacion_de_bic_expresion_matematica_bb0065 -> Sujeto_rol_alcance_capmin: sin mención
idx 20032: aplica_a Operacion_determinacion_de_exigencia_de_capital_minimo_por_riesgo_operacional_2a19e5 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 20121: aplica_a Operacion_determinacion_exigencia_total_computable_esquema_calculo_9217b9 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 20125: aplica_a Operacion_determinacion_mensual_cro_grupo_1_bb29a4 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 20127: aplica_a Operacion_determinacion_mensual_ro_grupo_2_e1dad4 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 20133: aplica_a Operacion_determinacion_ponderador_riesgo_inversion_fondo_a_en_fondo_b_c0a4c8 -> Sujeto_rol_alcance_capmin: sin mención
idx 20145: aplica_a Operacion_diferencia_positiva_prevision_regulatoria_vs_contable_c7f6c1 -> Sujeto_rol_alcance_capmin: sin mención
idx 20153: aplica_a Operacion_disposicion_de_fondos_por_causahabientes_c24691 -> Sujeto_banco: sin mención
idx 20157: aplica_a Operacion_division_de_conjunto_de_neteo_multiples_acuerdos_46b542 -> Sujeto_rol_alcance_capmin: sin mención
idx 20163: aplica_a Operacion_division_de_tramo_en_subtramos_por_cobertura_1518d6 -> Sujeto_rol_alcance_capmin: sin mención
idx 20192: aplica_a Operacion_emision_acciones_ordinarias_por_subsidiarias_1af269 -> Sujeto_rol_alcance_capmin: sin mención
idx 20195: aplica_a Operacion_emision_certificacion_aplicacion_repatriacion_aporte_inversion_fc1dcd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20222: aplica_a Operacion_emision_de_boleto_de_cambio_concepto_b14_f4bc57 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20225: aplica_a Operacion_emision_de_boleto_de_cambio_concepto_b15_c1d619 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20228: aplica_a Operacion_emision_de_boleto_de_cambio_concepto_b22_105fbd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20231: aplica_a Operacion_emision_de_boleto_de_cambio_conceptos_b06_9f9acb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20234: aplica_a Operacion_emision_de_boleto_de_venta_con_concepto_especifico_1c9402 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20237: aplica_a Operacion_emision_de_certificacion_acceso_al_mercado_de_cambios_edc166 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20241: aplica_a Operacion_emision_de_certificacion_de_aplicacion_671a7c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20246: aplica_a Operacion_emision_de_certificacion_de_aumento_de_exportaciones_0d3634 -> Sujeto_entidad_financiera: sin mención
idx 20252: aplica_a Operacion_emision_de_certificacion_para_afectacion_de_despacho_6b924f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20263: aplica_a Operacion_emision_de_certificaciones_de_acceso_cambios_96c3b8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20266: aplica_a Operacion_emision_de_certificaciones_de_aplicacion_bf0334 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20332: aplica_a Operacion_emision_de_certificaciones_de_aplicacion_de_divisas_9d4e8f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20338: aplica_a Operacion_emision_de_certificaciones_de_exportaciones_4a052b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20340: aplica_a Operacion_emision_de_certificaciones_de_incremento_de_exportaciones_92fce4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20344: aplica_a Operacion_emision_de_certificaciones_para_afectar_oficializacion_3e9dfb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20363: aplica_a Operacion_emision_de_factura_por_residente_aa3f97 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20395: aplica_a Operacion_emision_de_titulos_de_deuda_residentes_en_moneda_extranjera_12114b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20408: aplica_a Operacion_emision_titulos_deuda_aplicacion_cobros_exportaciones_2f46f9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20415: aplica_a Operacion_emitir_certificaciones_acceso_mercado_cambios_8bb43d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20424: aplica_a Operacion_endoso_a_favor_de_entidades_financieras_131732 -> Sujeto_banco: sin mención
idx 20429: aplica_a Operacion_endoso_a_fiduciarios_de_fideicomisos_financieros_e31a40 -> Sujeto_fiduciario_de_fideicomiso_financiero: sin mención
idx 20434: aplica_a Operacion_enfoque_integral_reduccion_de_la_exposicion_627666 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 20443: aplica_a Operacion_enfoque_simple_sustitucion_de_ponderadores_e75a31 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 20452: aplica_a Operacion_entrega_de_certificados_al_tenedor_f5006b -> Sujeto_banco: sin mención
idx 20454: aplica_a Operacion_entrega_de_chequeras_en_formato_papel_0d2c05 -> Sujeto_banco: sin mención
idx 20456: aplica_a Operacion_entrega_de_cuadernos_de_cheques_a051f1 -> Sujeto_banco: sin mención
idx 20460: aplica_a Operacion_entrega_de_nuevos_titulos_en_canje_rescate_financiero_1bcf16 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20462: aplica_a Operacion_entrega_de_saldo_por_fallecimiento_incapacidad_ordenante_63aef4 -> Sujeto_banco: sin mención
idx 20468: aplica_a Operacion_envio_extracto_cuenta_corriente_856548 -> Sujeto_banco: sin mención
idx 20492: aplica_a Operacion_exclusion_de_instrumentos_de_capital_rpc_4ea2fb -> Sujeto_rol_alcance_capmin: sin mención
idx 20494: aplica_a Operacion_exclusion_de_posiciones_compensadas_en_riesgo_especifico_y_general_44c993 -> Sujeto_rol_alcance_capmin: sin mención
idx 20501: aplica_a Operacion_exigencia_capital_derivado_primer_incumplimiento_65175e -> Sujeto_rol_alcance_capmin: sin mención
idx 20508: aplica_a Operacion_exportacion_a_paraguay_o_uruguay_facturada_en_moneda_de_destino_261fff -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20514: aplica_a Operacion_exportacion_de_efectos_personales_52dacb -> Sujeto_persona_humana: sin mención
idx 20518: aplica_a Operacion_exportacion_por_cuenta_y_orden_de_terceros_c15b10 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20525: aplica_a Operacion_exposicion_a_entidades_financieras_grupo_1_233946 -> Sujeto_rol_alcance_capmin: sin mención
idx 20527: aplica_a Operacion_exposicion_a_otros_estados_soberanos_bec787 -> Sujeto_rol_alcance_capmin: sin mención
idx 20529: aplica_a Operacion_exposicion_a_sector_publico_no_financiero_extranjero_e0879e -> Sujeto_rol_alcance_capmin: sin mención
idx 20546: aplica_a Operacion_exposiciones_con_coberturas_riesgo_credito_5e9790 -> Sujeto_rol_alcance_capmin: sin mención
idx 20566: aplica_a Operacion_extension_de_plazos_por_causales_ajenas_08876f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20573: aplica_a Operacion_extension_plazo_exportaciones_bajo_decretos_492_23_549_23_597_23_28_23_df5fca -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20587: aplica_a Operacion_extension_plazo_liquidacion_divisas_posfinanciaciones_totales_091be3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20589: aplica_a Operacion_extension_plazo_liquidacion_divisas_prefinanciaciones_totales_d946f9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20591: aplica_a Operacion_extension_plazo_prefinanciacion_parcial_mas_posfinanciaciones_4ff208 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20601: aplica_a Operacion_financiacion_a_beneficiarios_seguridad_social_pesos_ponderador_0_ea42dd -> Sujeto_rol_alcance_capmin: sin mención
idx 20603: aplica_a Operacion_financiacion_a_importadores_del_exterior_e50e77 -> Sujeto_entidad_financiera: sin mención
idx 20606: aplica_a Operacion_financiacion_a_importadores_del_exterior_e50e77__polcre -> Sujeto_entidad_financiera: sin mención
idx 20608: aplica_a Operacion_financiacion_a_productores_procesadores_o_acopiadores_c67489 -> Sujeto_entidad_financiera: sin mención
idx 20610: aplica_a Operacion_financiacion_a_residentes_garantizada_por_carta_de_credito_stand_by_102ace -> Sujeto_entidad_financiera: sin mención
idx 20613: aplica_a Operacion_financiacion_comercial_hasta_dos_veces_importe_referencia_3941be -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 20689: aplica_a Operacion_financiacion_de_importacion_de_bienes_de_capital_3c985a -> Sujeto_entidad_financiera: sin mención
idx 20693: aplica_a Operacion_financiacion_de_importaciones_por_agencia_oficial_6ba0fb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20697: aplica_a Operacion_financiacion_de_prestamos_hipotecarios_uvi_e8f246 -> Sujeto_entidad_financiera: sin mención
idx 20700: aplica_a Operacion_financiacion_de_proyectos_de_inversion_1b7a90 -> Sujeto_entidad_financiera: sin mención
idx 20706: aplica_a Operacion_financiacion_de_uvi_sistema_aleman_27567d -> Sujeto_entidad_financiera: sin mención
idx 20708: aplica_a Operacion_financiacion_de_uvi_sistema_frances_87aee7 -> Sujeto_entidad_financiera: sin mención
idx 20712: aplica_a Operacion_financiacion_importacion_bienes_cancelada_06e88a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20714: aplica_a Operacion_financiacion_mediante_prestamos_sindicados_ff3fad -> Sujeto_entidad_financiera: sin mención
idx 20717: aplica_a Operacion_financiacion_proyectos_inversion_sector_energetico_4dcb46 -> Sujeto_entidad_financiera: sin mención
idx 20782: aplica_a Operacion_financiaciones_otorgadas_por_sucursales_y_subsidiarias_96ae91 -> Sujeto_rol_alcance_capmin: sin mención
idx 20794: aplica_a Operacion_formulacion_de_descargo_por_incumplimiento_f7c8ae -> Sujeto_rol_alcance_capmin: sin mención
idx 20800: aplica_a Operacion_ganancias_por_ventas_titulizacion_8dbe2b -> Sujeto_rol_alcance_capmin: sin mención
idx 20836: aplica_a Operacion_giro_de_divisas_al_exterior_utilidades_y_dividendos_bd5c55 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20838: aplica_a Operacion_giro_de_divisas_por_utilidades_plan_gas_8f07a6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20842: aplica_a Operacion_giro_de_divisas_utilidades_y_dividendos_98b2d4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20845: aplica_a Operacion_giro_de_utilidades_y_dividendos_al_exterior_31f15a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20855: aplica_a Operacion_identificacion_cliente_firmas_electronicas_digitales_99dae0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20860: aplica_a Operacion_identificacion_del_cliente_operaciones_cambio_presencial_8d48df -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20864: aplica_a Operacion_identificacion_del_cliente_por_canales_electronicos_e0a216 -> Sujeto_entidad_cambiaria: sin mención
idx 20865: aplica_a Operacion_identificacion_del_cliente_por_canales_electronicos_e0a216 -> Sujeto_entidad_financiera: sin mención
idx 20866: aplica_a Operacion_identificacion_del_cliente_por_canales_electronicos_e0a216 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20870: aplica_a Operacion_identificacion_mediante_pasaporte_documento_habilitante_no_residentes_a686a6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20885: aplica_a Operacion_importacion_y_exportacion_de_moneda_nacional_3e878f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20888: aplica_a Operacion_impresion_de_certificados_echeq_rechazados_991ff5 -> Sujeto_banco: sin mención
idx 20890: aplica_a Operacion_impuracion_fob_aduana_conceptos_no_ventas_ceb000 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20893: aplica_a Operacion_imputacion_a_cartera_de_negociacion_c45350 -> Sujeto_rol_alcance_capmin: sin mención
idx 20895: aplica_a Operacion_imputacion_complementaria_precios_revisables_concentrados_minerales_378deb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20897: aplica_a Operacion_imputacion_componente_accionario_en_swap_3c6f3b -> Sujeto_rol_alcance_capmin: sin mención
idx 20899: aplica_a Operacion_imputacion_componente_tasa_interes_en_swap_05c7ca -> Sujeto_rol_alcance_capmin: sin mención
idx 20922: aplica_a Operacion_imputacion_de_cobro_de_mercaderia_siniestrada_f950f5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20930: aplica_a Operacion_imputacion_de_faltantes_y_mermas_524b82 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20943: aplica_a Operacion_imputacion_de_multas_por_demora_en_entrega_de_bienes_44a707 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20946: aplica_a Operacion_imputacion_de_multas_por_demoras_en_entrega_de_bienes_0a7dfe -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20948: aplica_a Operacion_imputacion_de_pago_en_sepaimpo_como_gestion_de_cobro_e25208 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20950: aplica_a Operacion_imputacion_de_posiciones_en_titulos_y_derivados_a_escalas_de_vencimientos_cdb3fe -> Sujeto_rol_alcance_capmin: sin mención
idx 20952: aplica_a Operacion_imputacion_descuentos_y_gastos_pagaderos_en_exterior_a2352e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20958: aplica_a Operacion_imputacion_gastos_bancarios_cobro_exportacion_7f6d3f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20963: aplica_a Operacion_imputacion_gastos_transporte_locales_gtosant736ca_7e6772 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20965: aplica_a Operacion_imputacion_lado_swap_de_moneda_f9a5a2 -> Sujeto_rol_alcance_capmin: sin mención
idx 20970: aplica_a Operacion_inclusion_en_central_cheques_sobre_cuentas_de_personas_juridicas_9ff4f1 -> Sujeto_banco: sin mención
idx 20978: aplica_a Operacion_inclusion_en_central_de_cheques_rechazados_d61a21 -> Sujeto_banco: sin mención
idx 20985: aplica_a Operacion_inclusion_instrumentos_ca_emitidos_por_subsidiarias_196520 -> Sujeto_rol_alcance_capmin: sin mención
idx 20990: aplica_a Operacion_incorporacion_bienes_importados_temporalmente_en_exportaciones_c4b605 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 20998: aplica_a Operacion_inferencia_ponderador_coberturas_riesgo_mercado_11ce51 -> Sujeto_rol_alcance_capmin: sin mención
idx 21008: aplica_a Operacion_informar_al_bcra_reclamo_no_respondido_629163 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 21014: aplica_a Operacion_informe_de_activos_intangibles_netos_847484 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21021: aplica_a Operacion_informe_de_aportes_sin_capitalizacion_autorizada_629b62 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21023: aplica_a Operacion_informe_de_bienes_inmuebles_sin_escritura_traslativa_6d229b -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21025: aplica_a Operacion_informe_de_calculos_eve_estandarizada_ric_363aab -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21028: aplica_a Operacion_informe_de_conceptos_deducibles_con1_no_incluidos_1a2097 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21030: aplica_a Operacion_informe_de_cuentas_de_corresponsalia_con_entidades_sin_investment_grade_dd414e -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21032: aplica_a Operacion_informe_de_excesos_a_limites_de_afectacion_de_activos_64c808 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21034: aplica_a Operacion_informe_de_ganancias_por_titulizacion_c01c14 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21040: aplica_a Operacion_informe_de_insuficiencia_de_provisiones_por_incobrabilidad_af6bc4 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21044: aplica_a Operacion_informe_de_inversiones_en_capital_de_empresas_complementarias_138321 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21050: aplica_a Operacion_informe_de_llave_negativa_registrada_b386b2 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21052: aplica_a Operacion_informe_de_mayor_saldo_de_titulos_subordinados_e7a5da -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21054: aplica_a Operacion_informe_de_saldo_a_favor_por_impuesto_a_ganancia_minima_presunta_5e033f -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21056: aplica_a Operacion_informe_de_titulos_de_gobiernos_extranjeros_con_calificacion_inferior_6201c6 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21062: aplica_a Operacion_informe_de_titulos_valores_no_fisicamente_en_poder_fffa1f -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21078: aplica_a Operacion_ingreso_de_cobros_por_sistema_monedas_locales_c42d3a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21081: aplica_a Operacion_ingreso_de_exportacion_a_traves_del_sistema_de_moneda_locales_0008e3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21085: aplica_a Operacion_ingreso_divisas_transporte_locales_exportacion_servicios_a0281a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21087: aplica_a Operacion_ingreso_y_liquidacion_60_dias_corridos_c57b4f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21100: aplica_a Operacion_ingreso_y_liquidacion_de_cobros_de_servicios_en_cambios_2d0931 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21122: aplica_a Operacion_ingreso_y_liquidacion_divisas_exportacion_839856 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21126: aplica_a Operacion_ingreso_y_liquidacion_divisas_por_empresa_procesadora_dc54e1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21134: aplica_a Operacion_ingreso_y_liquidacion_endeudamientos_o_aportes_de_inversion_15dd8b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21147: aplica_a Operacion_ingreso_y_remision_de_transferencias_de_ayuda_familiar_bdf384 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21149: aplica_a Operacion_ingresos_de_divisas_empresa_procesadora_de_pagos_c203c9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21153: aplica_a Operacion_inscripcion_en_padron_de_entidades_obligadas_cooperacion_tributaria_ca1c68 -> Sujeto_banco: sin mención
idx 21174: aplica_a Operacion_intercambio_de_garantias_valor_de_mercado_neto_bd836d -> Sujeto_rol_alcance_capmin: sin mención
idx 21177: aplica_a Operacion_intervencion_de_cheque_y_emision_de_recibo_d77fb2 -> Sujeto_banco: sin mención
idx 21181: aplica_a Operacion_inversion_en_fondos_fondo_a_en_fondo_b_0450f6 -> Sujeto_rol_alcance_capmin: sin mención
idx 21183: aplica_a Operacion_inversiones_directas_en_exterior_empresas_residentes_811e31 -> Sujeto_entidad_financiera: sin mención
idx 21185: aplica_a Operacion_inversiones_en_capital_de_entidades_financieras_supervision_consolidada_abe6af -> Sujeto_rol_alcance_capmin: sin mención
idx 21187: aplica_a Operacion_inversiones_en_instrumentos_computables_como_capital_regulatorio_98e4ce -> Sujeto_rol_alcance_capmin: sin mención
idx 21189: aplica_a Operacion_inversiones_en_instrumentos_de_capital_de_entidades_332d7c -> Sujeto_rol_alcance_capmin: sin mención
idx 21205: aplica_a Operacion_libramiento_de_echeq_fb56a0 -> Sujeto_banco: sin mención
idx 21215: aplica_a Operacion_liquidacion_de_divisas_en_cambios_5ace13 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21283: aplica_a Operacion_liquidacion_y_capitalizacion_de_intereses_sobre_saldos_acreedores_d5f301 -> Sujeto_banco: sin mención
idx 21286: aplica_a Operacion_liquidaciones_de_fondos_moneda_extranjera_financiacion_a_importadores_6ee4dd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21300: aplica_a Operacion_mantenimiento_de_cuenta_abierta_con_suspension_de_cheques_d02895 -> Sujeto_banco: sin mención
idx 21304: aplica_a Operacion_mantenimiento_de_posiciones_de_negociacion_06dd1d -> Sujeto_rol_alcance_capmin: sin mención
idx 21312: aplica_a Operacion_metodo_de_evaluacion_del_riesgo_grupo_1_36a933 -> Sujeto_rol_alcance_capmin: sin mención
idx 21330: aplica_a Operacion_monitoreo_y_control_lavado_de_activos_18f20c -> Sujeto_rol_alcance_lavdin: sin mención
idx 21332: aplica_a Operacion_monitoreo_y_revision_del_sistema_de_incentivos_b2cff9 -> Sujeto_entidad_financiera: sin mención
idx 21417: aplica_a Operacion_opciones_compradas_determinacion_capital_f14145 -> Sujeto_rol_alcance_capmin: sin mención
idx 21429: aplica_a Operacion_operacion_de_canje_y_o_arbitraje_con_fondos_de_bopreal_fad3ae -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21431: aplica_a Operacion_operacion_de_compra_venta_minorista_2a3886 -> Sujeto_casa_de_cambio: sin mención
idx 21433: aplica_a Operacion_operacion_de_cuenta_corriente_uniones_transitorias_1866ec -> Sujeto_banco: sin mención
idx 21436: aplica_a Operacion_operacion_de_cuenta_en_pesos_o_dolares_8d367f -> Sujeto_banco: sin mención
idx 21474: aplica_a Operacion_operaciones_de_arbitraje_y_canje_en_exterior_f2909a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21477: aplica_a Operacion_operaciones_de_cambio_canje_o_arbitraje_con_bcra_y_entidades_556dd3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21482: aplica_a Operacion_operaciones_de_cambio_de_moneda_extranjera_ff9d15 -> Sujeto_entidad_cambiaria: sin mención
idx 21483: aplica_a Operacion_operaciones_de_cambio_de_moneda_extranjera_ff9d15 -> Sujeto_entidad_financiera: sin mención
idx 21486: aplica_a Operacion_operaciones_de_financiacion_con_titulos_valores_pase_c332e7 -> Sujeto_rol_alcance_capmin: sin mención
idx 21500: aplica_a Operacion_operaciones_dvp_entrega_contra_pago_f8b4af -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 21524: aplica_a Operacion_operaciones_por_servicios_de_renta_y_capital_72df83 -> Sujeto_entidad_cambiaria: sin mención
idx 21525: aplica_a Operacion_operaciones_por_servicios_de_renta_y_capital_72df83 -> Sujeto_entidad_financiera: sin mención
idx 21660: aplica_a Operacion_operatoria_con_derivados_en_moneda_extranjera_b85390 -> Sujeto_fideicomiso: sin mención
idx 21661: aplica_a Operacion_operatoria_con_derivados_en_moneda_extranjera_b85390 -> Sujeto_fondo_comun_de_inversion: sin mención
idx 21662: aplica_a Operacion_operatoria_con_derivados_en_moneda_extranjera_b85390 -> Sujeto_gobierno_local: sin mención
idx 21664: aplica_a Operacion_operatoria_con_derivados_en_moneda_extranjera_b85390 -> Sujeto_universalidad: sin mención
idx 21678: aplica_a Operacion_otorgamiento_cumplido_permiso_embarque_provisorio_700042 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21683: aplica_a Operacion_otorgamiento_de_financiacion_complementaria_365_dias_6a2a56 -> Sujeto_entidad_financiera: sin mención
idx 21685: aplica_a Operacion_otorgamiento_de_financiacion_uva_cartera_consumo_vivienda_506cd7 -> Sujeto_entidad_financiera: sin mención
idx 21687: aplica_a Operacion_otorgamiento_de_financiaciones_a_personas_humanas_f27564 -> Sujeto_persona_humana: sin mención
idx 21693: aplica_a Operacion_otorgamiento_de_garantias_locales_f334ff -> Sujeto_banco: sin mención
idx 21717: aplica_a Operacion_otras_ventas_titulos_valores_liquidacion_cable_terceros_54f414 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21723: aplica_a Operacion_pago_a_la_vista_de_importacion_de_bienes_45f1f9 -> Sujeto_mipyme: sin mención
idx 21724: aplica_a Operacion_pago_a_la_vista_de_importacion_de_bienes_45f1f9 -> Sujeto_persona_humana: sin mención
idx 21743: aplica_a Operacion_pago_anticipado_importaciones_bienes_de_capital_cf67cb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21746: aplica_a Operacion_pago_capital_e_intereses_endeudamientos_cc6725 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21757: aplica_a Operacion_pago_capital_e_intereses_endeudamientos_financieros_0da822 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21769: aplica_a Operacion_pago_capital_e_intereses_titulos_deuda_cobro_exportaciones_5f08ca -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21772: aplica_a Operacion_pago_capital_e_intereses_titulos_deuda_registrados_49a664 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21781: aplica_a Operacion_pago_capital_e_intereses_vpu_rigi_4bc3c0 -> Sujeto_vpu_rigi: sin mención
idx 21818: aplica_a Operacion_pago_capital_intereses_compensatorios_contrapartes_vinculadas_d60fe3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21839: aplica_a Operacion_pago_de_bienes_importados_alquiler_con_opcion_b803d5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21843: aplica_a Operacion_pago_de_capital_de_deuda_por_importacion_de_servicios_0a9aed -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21872: aplica_a Operacion_pago_de_capital_e_intereses_de_titulos_valores_887b14 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21908: aplica_a Operacion_pago_de_capital_e_intereses_titulos_deuda_exterior_455f71 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21944: aplica_a Operacion_pago_de_capital_o_intereses_de_titulos_de_deuda_ea9231 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21957: aplica_a Operacion_pago_de_deudas_comerciales_importaciones_de_bienes_5406b5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21979: aplica_a Operacion_pago_de_deudas_comerciales_por_importaciones_de_servicios_434fb3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 21987: aplica_a Operacion_pago_de_deudas_con_accionistas_no_residentes_1a9a1f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22009: aplica_a Operacion_pago_de_importacion_con_conformidad_bcra_5e9b53 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22027: aplica_a Operacion_pago_de_importacion_marco_punto_4_8_5_7ca3b3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22041: aplica_a Operacion_pago_de_importaciones_contra_documentacion_embarque_3cd5d5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22051: aplica_a Operacion_pago_de_intereses_conformidad_previa_bcra_d42fa5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22054: aplica_a Operacion_pago_de_intereses_de_deudas_por_importaciones_d600d4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22160: aplica_a Operacion_pago_de_servicio_no_comprendido_7794e5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22188: aplica_a Operacion_pago_de_servicio_no_comprendido_por_contraparte_vinculada_657f17 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22205: aplica_a Operacion_pago_de_servicio_no_residente_9454ac -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22233: aplica_a Operacion_pago_de_servicio_prestado_por_no_residente_3e5171 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22247: aplica_a Operacion_pago_de_servicios_prestados_con_antelacion_1bfcff -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22272: aplica_a Operacion_pago_de_servicios_servicios_prestados_devengados_desde_13_12_23_f39e3d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22315: aplica_a Operacion_pago_deudas_accionistas_no_residentes_utilidades_dividendos_de20da -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22317: aplica_a Operacion_pago_deudas_comerciales_importacion_bienes_bopreal_3e02aa -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22339: aplica_a Operacion_pago_deudas_comerciales_importaciones_servicios_dec8fa -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22349: aplica_a Operacion_pago_importacion_bienes_capital_927a13 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22351: aplica_a Operacion_pago_importacion_medicamento_critico_31eb65 -> Sujeto_persona_humana: sin mención
idx 22352: aplica_a Operacion_pago_importacion_medicamento_critico_31eb65 -> Sujeto_persona_juridica: sin mención
idx 22355: aplica_a Operacion_pago_intereses_devengados_impagos_capital_pendiente_5a1c7f -> Sujeto_vpu_rigi: sin mención
idx 22391: aplica_a Operacion_pago_intereses_devengados_refinanciacion_229fe6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22393: aplica_a Operacion_pago_jubilaciones_beneficios_previsionales_sml_39d62b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22397: aplica_a Operacion_pago_parcial_de_cheque_e1bcf4 -> Sujeto_banco: sin mención
idx 22399: aplica_a Operacion_pago_por_cartas_de_credito_o_letras_23332b -> Sujeto_entidad_financiera: sin mención
idx 22407: aplica_a Operacion_pago_prima_recompra_o_rescate_anticipado_eeeefa -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22410: aplica_a Operacion_pago_servicio_no_residente_bopreal_9f6637 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22451: aplica_a Operacion_pago_servicios_no_residentes_recompra_rescate_deuda_7c6c55 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22475: aplica_a Operacion_pago_titulos_deuda_capital_e_intereses_0abd8a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22515: aplica_a Operacion_pagos_de_capital_deudas_importacion_bienes_hasta_12_12_23_b71be9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22519: aplica_a Operacion_pagos_de_importaciones_de_bienes_de_capital_991919 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22522: aplica_a Operacion_pagos_de_intereses_deuda_comercial_importacion_servicios_28eed8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22525: aplica_a Operacion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_ea069c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22560: aplica_a Operacion_pagos_titulos_de_deuda_suscriptos_exterior_porcion_moneda_extranjera_pais_aa4dd5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22567: aplica_a Operacion_participaciones_en_emisoras_tarjetas_credito_debito_823598 -> Sujeto_rol_alcance_capmin: sin mención
idx 22569: aplica_a Operacion_participaciones_en_empresas_arrendamiento_financiero_f37618 -> Sujeto_rol_alcance_capmin: sin mención
idx 22571: aplica_a Operacion_participaciones_transitorias_en_empresas_facilitacion_desarrollo_3343ce -> Sujeto_rol_alcance_capmin: sin mención
idx 22584: aplica_a Operacion_ponderacion_de_exposiciones_con_fondo_como_directas_f47187 -> Sujeto_rol_alcance_capmin: sin mención
idx 22601: aplica_a Operacion_ponderacion_posicion_titulizacion_1250_ff9764 -> Sujeto_rol_alcance_capmin: sin mención
idx 22603: aplica_a Operacion_posfinanciacion_a_importadores_del_exterior_5e10eb -> Sujeto_entidad_financiera: sin mención
idx 22643: aplica_a Operacion_precancelacion_capital_e_intereses_con_liquidacion_fondos_exterior_7fa09f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22654: aplica_a Operacion_precancelacion_capital_e_intereses_con_liquidacion_fondos_nuevo_titulo_62d972 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22667: aplica_a Operacion_precancelacion_capital_intereses_vpu_rigi_85df5c -> Sujeto_vpu_rigi: sin mención
idx 22716: aplica_a Operacion_precancelacion_de_capital_e_intereses_liquidacion_simultanea_fff07f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22727: aplica_a Operacion_precancelacion_de_capital_e_intereses_simultanea_con_nuevo_titulo_19b496 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22760: aplica_a Operacion_precancelacion_de_financiaciones_en_moneda_extranjera_8497e2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22773: aplica_a Operacion_precancelacion_de_intereses_en_canje_de_titulos_2b9be7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22785: aplica_a Operacion_prefinanciacion_a_importadores_del_exterior_c06cd0 -> Sujeto_entidad_financiera: sin mención
idx 22792: aplica_a Operacion_prefinanciaciones_de_exportaciones_fondeo_exterior_21b543 -> Sujeto_entidad_cambiaria: sin mención
idx 22793: aplica_a Operacion_prefinanciaciones_de_exportaciones_fondeo_exterior_21b543 -> Sujeto_entidad_financiera: sin mención
idx 22804: aplica_a Operacion_presentacion_consolidada_con_filiales_interior_codigo_1_2f3b66 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 22806: aplica_a Operacion_presentacion_consolidado_mensual_codigo_2_62b3ac -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 22808: aplica_a Operacion_presentacion_consolidado_mensual_sin_consolidacion_cruzada_codigo_9_58a9d6 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 22810: aplica_a Operacion_presentacion_consolidado_trimestral_codigo_3_a7b55c -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 22828: aplica_a Operacion_presentacion_de_cheque_al_cobro_o_registracion_81abfa -> Sujeto_banco: sin mención
idx 22838: aplica_a Operacion_presentacion_de_cheques_diferidos_en_mercados_de_valores_19ab98 -> Sujeto_banco: sin mención
idx 22853: aplica_a Operacion_presentacion_de_declaracion_jurada_de_cliente_ead29e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22862: aplica_a Operacion_presentacion_de_exigencia_por_riesgo_de_acciones_a061ad -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 22864: aplica_a Operacion_presentacion_de_exigencia_por_riesgo_de_posiciones_en_opciones_aa5f51 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 22866: aplica_a Operacion_presentacion_de_exigencia_por_riesgo_de_posiciones_en_productos_basicos_3ea591 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 22868: aplica_a Operacion_presentacion_de_exigencia_por_riesgo_de_tasa_86952c -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 22870: aplica_a Operacion_presentacion_de_exigencia_por_riesgo_de_tipo_de_cambio_49947d -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 22872: aplica_a Operacion_presentacion_de_factura_de_exportacion_imputacion_de_divisas_33636b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22887: aplica_a Operacion_presentacion_de_reclamo_al_bcra_por_usuario_02ec34 -> Sujeto_usuario_de_servicios_financieros: sin mención
idx 22891: aplica_a Operacion_presentacion_de_reclamo_insatisfactorio_al_bcra_35142f -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 22914: aplica_a Operacion_presentacion_factura_proforma_bien_importado_eb09d7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22930: aplica_a Operacion_presentacion_modelo_cuadro_11_2_1_a_fc5ba5 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 22932: aplica_a Operacion_presentacion_modelo_cuadro_11_2_1_b_b53ce3 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 22934: aplica_a Operacion_presentacion_modelo_cuadro_11_2_2_a_4200df -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 22936: aplica_a Operacion_presentacion_modelo_cuadro_11_2_2_b_f89254 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 22938: aplica_a Operacion_presentacion_no_consolidada_con_filiales_interior_codigo_0_67c6ec -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 22943: aplica_a Operacion_prestacion_de_servicios_a_clientes_3832f9 -> Sujeto_banco: sin mención
idx 22946: aplica_a Operacion_prestamo_financiero_con_flujo_de_exportaciones_a94890 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 22948: aplica_a Operacion_prestamos_a_instituciones_de_microcredito_002138 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 22951: aplica_a Operacion_prestamos_a_microemprendedores_c49821 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 22962: aplica_a Operacion_prestamos_interfinancieros_uva_b60504 -> Sujeto_entidad_financiera: sin mención
idx 22975: aplica_a Operacion_previsiones_por_riesgo_incobrabilidad_226e68 -> Sujeto_rol_alcance_capmin: sin mención
idx 22997: aplica_a Operacion_prorroga_del_plazo_de_demostracion_del_registro_de_ingreso_aduanero_2d4306 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23001: aplica_a Operacion_provision_cajeros_automaticos_accesibles_para_usuarios_con_dificultades_visuales_c698ec -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 23033: aplica_a Operacion_publicacion_paginas_internet_home_banking_accesible_5b9daa -> Sujeto_usuario_de_servicios_financieros: sin mención
idx 23048: aplica_a Operacion_recategorizacion_directa_a_niveles_superiores_325ddf -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 23060: aplica_a Operacion_recepcion_de_presentaciones_multiples_canales_19e55d -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 23062: aplica_a Operacion_rechazar_cheques_emitidos_hasta_dia_anterior_a_notificacion_092e66 -> Sujeto_banco: sin mención
idx 23077: aplica_a Operacion_rechazo_de_cheque_por_defecto_formal_ee7c7e -> Sujeto_banco: sin mención
idx 23103: aplica_a Operacion_reclasificacion_al_nivel_inmediato_superior_052195 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 23107: aplica_a Operacion_reclasificacion_en_tratamiento_especial_por_refinanciacion_0cd96a -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 23110: aplica_a Operacion_recompra_posiciones_titulizacion_por_originantes_7976ee -> Sujeto_rol_alcance_capmin: sin mención
idx 23112: aplica_a Operacion_recompra_y_reembarque_de_mercaderia_ee6f94 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23114: aplica_a Operacion_reconocimiento_cobertura_riesgo_credito_69e3dd -> Sujeto_rol_alcance_capmin: sin mención
idx 23117: aplica_a Operacion_reconocimiento_de_instrumentos_en_rpc_de_entidad_financiera_49e5ec -> Sujeto_rol_alcance_capmin: sin mención
idx 23120: aplica_a Operacion_reconocimiento_de_pnb_de_subsidiarias_en_el_pnb_de_la_entidad_financiera_7d5519 -> Sujeto_rol_alcance_capmin: sin mención
idx 23131: aplica_a Operacion_reduccion_de_exigencia_por_riesgo_operacional_2b2972 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 23133: aplica_a Operacion_reduccion_exigencia_partida_36000002_469fa0 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 23135: aplica_a Operacion_reduccion_exigencia_partida_36000003_e0fd6b -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 23137: aplica_a Operacion_reduccion_exigencia_partida_36000005_6d0605 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 23139: aplica_a Operacion_reduccion_exigencia_partida_36000006_162e60 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 23144: aplica_a Operacion_reembarco_de_bienes_desde_zonas_francas_nacionales_a9c02a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23171: aplica_a Operacion_reevaluacion_de_clasificacion_deudor_e2cf81 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 23173: aplica_a Operacion_reexportacion_de_mercaderia_raf_no_utilizada_051dfa -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23177: aplica_a Operacion_refinanciacion_de_deuda_comercial_8bb60c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23184: aplica_a Operacion_refinanciaciones_posteriores_a25680 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 23196: aplica_a Operacion_registro_aportes_a_valor_de_mercado_f24515 -> Sujeto_rol_alcance_capmin: sin mención
idx 23207: aplica_a Operacion_registro_aportes_acciones_punto_8_6_3_3c6b78 -> Sujeto_rol_alcance_capmin: sin mención
idx 23219: aplica_a Operacion_registro_de_beneficios_cedidos_a_proveedores_directos_e3e05b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23230: aplica_a Operacion_registro_de_debitos_por_multas_1e13e9 -> Sujeto_banco: sin mención
idx 23235: aplica_a Operacion_registro_de_importes_ordenados_por_anses_c54a40 -> Sujeto_rol_alcance_pagjub: sin mención
idx 23241: aplica_a Operacion_registro_de_operacion_con_cliente_ante_bcra_739405 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23244: aplica_a Operacion_registro_de_operacion_persona_humana_residente_apoderada_20598f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23273: aplica_a Operacion_registro_depositos_y_obligaciones_valor_contable_707d46 -> Sujeto_rol_alcance_capmin: sin mención
idx 23324: aplica_a Operacion_repatriacion_aportes_inversion_directa_accionistas_no_residentes_ab7287 -> Sujeto_vpu_rigi: sin mención
idx 23329: aplica_a Operacion_repatriacion_de_aportes_inversion_directa_vpu_rigi_aea171 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23338: aplica_a Operacion_repatriacion_de_inversiones_de_portafolio_no_residentes_750669 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23347: aplica_a Operacion_repatriacion_de_inversiones_directas_mediante_residente_53992a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23350: aplica_a Operacion_repatriacion_de_inversiones_directas_no_residentes_a3f52b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23352: aplica_a Operacion_repatriacion_de_servicios_de_capital_y_rentas_no_residentes_dce0e0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23354: aplica_a Operacion_repatriacion_inversion_directa_no_residentes_84304e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23363: aplica_a Operacion_repatriacion_inversiones_directas_no_residentes_con_certificacion_decreto_277_22_4f0568 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23366: aplica_a Operacion_repatriacion_inversiones_portafolio_no_residentes_4a013c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23396: aplica_a Operacion_respaldo_implicito_de_titulizacion_88500f -> Sujeto_rol_alcance_capmin: sin mención
idx 23410: aplica_a Operacion_retiros_de_efectivo_en_el_exterior_con_tarjeta_debito_debito_inmediato_895110 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23417: aplica_a Operacion_revision_de_clasificacion_semestre_calendario_89a2d0 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 23432: aplica_a Operacion_revocacion_o_rescision_producto_servicio_62bf80 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 23453: aplica_a Operacion_seguimiento_de_pagos_de_importaciones_con_registro_pendiente_2bbe91 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23465: aplica_a Operacion_seguimiento_especifico_de_exportadores_e4cef5 -> Sujeto_exportador: sin mención
idx 23467: aplica_a Operacion_seguimiento_exportaciones_de_bienes_7901d9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23479: aplica_a Operacion_servicios_de_cobranza_por_cuenta_de_terceros_debitos_automaticos_directos_ff6503 -> Sujeto_banco: sin mención
idx 23483: aplica_a Operacion_solicitud_de_caja_de_ahorros_en_pesos_615e58 -> Sujeto_entidad_financiera: sin mención
idx 23512: aplica_a Operacion_suscripcion_bopreal_por_utilidades_y_dividendos_2ea962 -> Sujeto_cliente: sin mención
idx 23514: aplica_a Operacion_suscripcion_de_bonos_bopreal_086e60 -> Sujeto_importador_de_bienes: sin mención
idx 23521: aplica_a Operacion_suscripcion_de_bonos_bopreal_deudores_485f4f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23546: aplica_a Operacion_suscripcion_de_bonos_bopreal_por_deudores_de_importaciones_91fbcd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23589: aplica_a Operacion_suscripcion_de_bopreal_operacion_de_financiamiento_0e5b1d -> Sujeto_cliente: sin mención
idx 23592: aplica_a Operacion_suscripcion_de_bopreal_por_deuda_vencida_58fe7e -> Sujeto_cliente: sin mención
idx 23617: aplica_a Operacion_suscripcion_de_bopreal_por_importadores_12cfe7 -> Sujeto_importador_de_bienes: sin mención
idx 23618: aplica_a Operacion_suscripcion_de_bopreal_por_importadores_12cfe7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23625: aplica_a Operacion_sustitucion_de_ponderador_de_riesgo_cobertura_con_activos_7d77e6 -> Sujeto_rol_alcance_capmin: sin mención
idx 23630: aplica_a Operacion_sustitucion_de_ponderadores_garantias_personales_ea0cd8 -> Sujeto_rol_alcance_capmin: sin mención
idx 23640: aplica_a Operacion_swap_tasa_interes_con_referencia_a_indice_bursatil_ce7a54 -> Sujeto_rol_alcance_capmin: sin mención
idx 23642: aplica_a Operacion_swap_tasa_variable_recibida_fija_pagada_48729c -> Sujeto_rol_alcance_capmin: sin mención
idx 23644: aplica_a Operacion_swaps_de_acciones_como_dos_posiciones_nocionales_77917b -> Sujeto_rol_alcance_capmin: sin mención
idx 23647: aplica_a Operacion_tenencia_de_acciones_en_indice_bursatil_principal_0e06d2 -> Sujeto_rol_alcance_capmin: sin mención
idx 23652: aplica_a Operacion_tenencia_de_cuotapartes_depository_receipts_cedear_o_ceva_a91fe0 -> Sujeto_rol_alcance_capmin: sin mención
idx 23661: aplica_a Operacion_tenencia_de_oro_amonedado_o_en_barras_40484d -> Sujeto_rol_alcance_capmin: sin mención
idx 23665: aplica_a Operacion_tenencia_de_titulos_de_deuda_de_empresas_investment_grade_463b7e -> Sujeto_rol_alcance_capmin: sin mención
idx 23667: aplica_a Operacion_tenencia_de_titulos_de_fideicomisos_financieros_b204a5 -> Sujeto_rol_alcance_capmin: sin mención
idx 23669: aplica_a Operacion_tenencia_de_titulos_del_sector_publico_4e6446 -> Sujeto_rol_alcance_capmin: sin mención
idx 23716: aplica_a Operacion_transferencia_a_traves_de_entidad_financiera_del_exterior_a60dc8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23718: aplica_a Operacion_transferencia_al_exterior_capital_titulos_deuda_post_08_11_24_e49743 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23720: aplica_a Operacion_transferencia_al_exterior_de_agentes_locales_724e05 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23725: aplica_a Operacion_transferencia_al_exterior_por_beneficiarios_de_jubilaciones_pensiones_d6f24d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23772: aplica_a Operacion_transferencia_de_divisas_al_exterior_centrales_de_deposito_24ec96 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23774: aplica_a Operacion_transferencia_de_divisas_al_exterior_de_personas_humanas_77eeda -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23776: aplica_a Operacion_transferencia_de_divisas_pago_importaciones_69b1e8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23806: aplica_a Operacion_transferencia_fondos_desde_hacia_exterior_30e134 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23885: aplica_a Operacion_transferencias_a_cuentas_bancarias_en_el_exterior_293d36 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23893: aplica_a Operacion_transmision_de_certificaciones_por_medio_seguro_d4ccf1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 23897: aplica_a Operacion_transmision_de_cheque_por_endoso_d920ba -> Sujeto_banco: sin mención
idx 23902: aplica_a Operacion_tratamiento_de_contrapartes_conectadas_grupo_unico_27f536 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 23912: aplica_a Operacion_tratamiento_exposiciones_mipyme_no_normativas_a8f3d7 -> Sujeto_rol_alcance_capmin: sin mención
idx 23923: aplica_a Operacion_tratamiento_transparencia_posicion_maxima_preferencia_49c400 -> Sujeto_rol_alcance_capmin: sin mención
idx 23937: aplica_a Operacion_truncamiento_de_cheques_3ea845 -> Sujeto_banco: sin mención
idx 23942: aplica_a Operacion_uso_de_forwards_y_derivados_en_productos_basicos_20b900 -> Sujeto_rol_alcance_capmin: sin mención
idx 23952: aplica_a Operacion_utilizacion_consistente_ecai_3de9a3 -> Sujeto_rol_alcance_capmin: sin mención
idx 24016: aplica_a Operacion_venta_de_bonos_bopreal_liquidacion_cable_terceros_d5fa79 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24065: aplica_a Operacion_venta_de_divisas_cancelacion_linea_credito_e62044 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24068: aplica_a Operacion_venta_de_divisas_importaciones_y_servicios_asociados_b08bd3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24074: aplica_a Operacion_venta_o_cesion_de_cartera_con_responsabilidad_f0db6c -> Sujeto_rol_alcance_capmin: sin mención
idx 24136: aplica_a Operacion_verificar_cumplimiento_de_plazos_importador_b192a2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24141: aplica_a Operacion_volcado_de_manual_de_procedimientos_f20ee3 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 24143: aplica_a Potestad_acceso_a_cliente_para_pago_intereses_y_capital_sin_conformidad_bcra__las_entidad_18b444 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24145: aplica_a Potestad_acceso_a_mercado_para_compra_de_moneda_extranjera__los_residentes_con_endeudamie_e27e35 -> Sujeto_fideicomiso: sin mención
idx 24146: aplica_a Potestad_acceso_a_mercado_para_compra_de_moneda_extranjera__los_residentes_con_endeudamie_e27e35 -> Sujeto_persona_humana: sin mención
idx 24165: aplica_a Potestad_acceso_a_niveles_superiores_clasificacion__el_deudor_podra_acceder_a_niveles_sup_60644a -> Sujeto_deudor: sin mención
idx 24174: aplica_a Potestad_acceso_al_cliente_para_pagar_financiacion_comercial__las_entidades_podran_dar_ac_205872 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24191: aplica_a Potestad_acceso_al_mercado_cambios_vpu_por_financiaciones_rigi__las_entidades_podran_dar__d53d37 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24215: aplica_a Potestad_acceso_al_mercado_de_cambios_clientes__los_clientes_podran_acceder_al_mercado_de_472ba4 -> Sujeto_cliente: sin mención
idx 24217: aplica_a Potestad_acceso_al_mercado_de_cambios_con_fondos_bopreal__los_clientes_podran_acceder_al__2fb652 -> Sujeto_cliente: sin mención
idx 24225: aplica_a Potestad_acceso_al_mercado_de_cambios_excepcion_conformidad_previa_bcra__queda_eximida_la_f37683 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24227: aplica_a Potestad_acceso_al_mercado_de_cambios_financiaciones_comerciales__las_entidades_podran_da_772f64 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24229: aplica_a Potestad_acceso_al_mercado_de_cambios_financiaciones_e_inversion_directa__las_entidades_p_01ee52 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24231: aplica_a Potestad_acceso_al_mercado_de_cambios_giro_de_divisas_utilidades_y_dividendos__las_entida_30708b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24233: aplica_a Potestad_acceso_al_mercado_de_cambios_habilitacion__las_personas_juridicas_que_tengan_a_s_9d36e4 -> Sujeto_persona_juridica: sin mención
idx 24235: aplica_a Potestad_acceso_al_mercado_de_cambios_pago_al_exterior__la_entidad_interviniente_podra_da_6dbab3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24237: aplica_a Potestad_acceso_al_mercado_de_cambios_pago_bienes_deposito_franco__la_entidad_intervinien_269bad -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24239: aplica_a Potestad_acceso_al_mercado_de_cambios_pagos_importaciones_zonas_francas__la_entidad_inter_8ec680 -> Sujeto_entidad_cambiaria: sin mención
idx 24240: aplica_a Potestad_acceso_al_mercado_de_cambios_pagos_importaciones_zonas_francas__la_entidad_inter_8ec680 -> Sujeto_entidad_financiera: sin mención
idx 24261: aplica_a Potestad_acceso_al_mercado_de_cambios_para_compras_revendidas_al_exterior__la_entidad_int_14991c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24263: aplica_a Potestad_acceso_al_mercado_de_cambios_para_pago_insumos_offshore__la_entidad_intervinient_bdba31 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24265: aplica_a Potestad_acceso_al_mercado_de_cambios_para_pagos__las_entidades_podran_dar_acceso_al_merc_366e6a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24267: aplica_a Potestad_acceso_al_mercado_de_cambios_para_pagos_con_registro_pendiente__las_entidades_po_0cecd3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24271: aplica_a Potestad_acceso_al_mercado_de_cambios_para_pagos_de_importaciones__la_entidad_intervinien_beaf9a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24292: aplica_a Potestad_acceso_al_mercado_de_cambios_para_pagos_de_servicios_de_no_residentes__las_entid_4ca7e6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24294: aplica_a Potestad_acceso_al_mercado_de_cambios_para_pagos_de_servicios_no_residentes__las_entidade_1438a3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24296: aplica_a Potestad_acceso_al_mercado_de_cambios_previo__las_entidades_podran_dar_acceso_al_mercado__d630fe -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24316: aplica_a Potestad_acceso_al_mercado_de_cambios_residentes_con_endeudamientos__las_entidades_podran_32398c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24318: aplica_a Potestad_acceso_al_mercado_de_cambios_residentes_con_endeudamientos__las_entidades_podran_dc033c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24320: aplica_a Potestad_acceso_de_clientes_a_pagos_elegibles__los_clientes_podran_en_la_medida_que_se_cu_a0446f -> Sujeto_cliente: sin mención
idx 24322: aplica_a Potestad_acceso_gobiernos_locales_mercado_de_cambios_obras_infraestructura__los_gobiernos_183450 -> Sujeto_gobierno_local: sin mención
idx 24324: aplica_a Potestad_acceso_gobiernos_locales_pago_exterior_obras_infraestructura__los_gobiernos_loca_7617a2 -> Sujeto_gobierno_local: sin mención
idx 24326: aplica_a Potestad_acceso_mercado_cambios_a_clientes__las_entidades_podran_dar_acceso_al_mercado_de_ce4ae1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24328: aplica_a Potestad_acceso_mercado_cambios_a_partir_vencimiento_cancelacion_lineas_credito__las_enti_0218d7 -> Sujeto_entidad_financiera: sin mención
idx 24330: aplica_a Potestad_acceso_mercado_cambios_cancelacion_financiaciones__las_entidades_tambien_podran__be331c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24332: aplica_a Potestad_acceso_mercado_cambios_cancelacion_garantias_importacion__la_entidad_tendra_acce_673b46 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24338: aplica_a Potestad_acceso_mercado_cambios_pago_capital_deudas_bopreal__los_clientes_que_suscribiero_082e8d -> Sujeto_cliente: sin mención
idx 24364: aplica_a Potestad_acceso_mercado_cambios_pago_primas_y_garantias__las_entidades_podran_dar_acceso__5bc7e4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24366: aplica_a Potestad_acceso_mercado_cambios_para_pago_gastos_emision_servicios_no_residentes__la_enti_a85cda -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24368: aplica_a Potestad_acceso_mercado_cambios_para_pago_prima_recompra_rescate_hasta_5__la_entidad_podr_a74244 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24371: aplica_a Potestad_acceso_mercado_cambios_para_pagos_diferidos_importaciones__las_entidades_podran__b773d9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24375: aplica_a Potestad_acceso_mercado_cambios_vpu_adherido__las_entidades_podran_tambien_dar_acceso_en__9a526a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24377: aplica_a Potestad_acceso_mercado_de_cambios_para_residentes_con_endeudamientos_y_prefinanciaciones_e27ecf -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24395: aplica_a Potestad_acceso_parcial_pagos_capital_fondos_parcialmente_computables__las_entidades_podr_e7a0b5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24397: aplica_a Potestad_acceso_parcial_pagos_intereses_fondos_parcialmente_computables__las_entidades_po_129948 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24400: aplica_a Potestad_acceso_sin_conformidad_previa_bcra_pago_intereses_y_capital__las_entidades_podra_744cfe -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24402: aplica_a Potestad_acceso_sin_conformidad_previa_bcra_pago_proporcional__las_entidades_podran_dar_a_7dc84a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24404: aplica_a Potestad_acceso_vpu_sin_conformidad_previa_bcra__las_entidades_podran_dar_acceso_al_vpu_a_54e00f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24406: aplica_a Potestad_aceptacion_alternativa_declaracion_jurada_adicional__en_caso_de_que_el_cliente_t_4702a1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24411: aplica_a Potestad_aceptacion_y_habilitacion_para_emitir_certificaciones__la_nueva_entidad_queda_fa_b72068 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24413: aplica_a Potestad_aceptar_cambio_de_entidad_nominada__la_nueva_entidad_puede_aceptar_ser_designada_4ae868 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24415: aplica_a Potestad_aceptar_certificado_acreditacion_hidrocarburos__la_entidad_podra_considerar_cump_b98393 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24417: aplica_a Potestad_acuerdo_libre_sobre_forma_de_cancelacion__las_entidades_y_sus_clientes_podran_co_916306 -> Sujeto_banco: sin mención
idx 24419: aplica_a Potestad_acumulacion_cobros_exportaciones_servicios__se_admitira_que_los_cobros_de_export_99cfee -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24421: aplica_a Potestad_acumulacion_de_fondos_de_exportacion_en_cuentas_exteriores__se_admite_que_los_fo_0260a3 -> Sujeto_vpu_rigi: sin mención
idx 24436: aplica_a Potestad_adicion_de_importe_en_previsiones_rpc_consolidada__la_entidad_que_consolide_podr_166c30 -> Sujeto_rol_alcance_capmin: sin mención
idx 24438: aplica_a Potestad_adicionar_llave_de_negocio_negativa_a_rpc__se_podra_adicionar_el_importe_corresp_a0615d -> Sujeto_rol_alcance_capmin: sin mención
idx 24440: aplica_a Potestad_admision_aplicacion_divisas_a_cancelacion_capital_e_intereses_porcion_no_liquida_f318c6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24442: aplica_a Potestad_admision_de_acceso_para_pago_de_servicios__tambien_sera_admisible_el_acceso_para_0076a1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24466: aplica_a Potestad_admision_de_aplicacion_de_divisas_a_cancelacion_de_vencimientos__se_admitira_la__c16001 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24468: aplica_a Potestad_admision_de_cobros_de_exportaciones_para_operaciones_del_regimen__se_admitira_la_9ca496 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24470: aplica_a Potestad_admision_de_contratos_multiproducto_escindibles__se_admitiran_contratos_multipro_a3ee81 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 24478: aplica_a Potestad_admision_de_debitos_internos_conforme_condiciones__se_admitiran_en_las_condicion_5266c9 -> Sujeto_banco: sin mención
idx 24491: aplica_a Potestad_admision_descalce_de_monedas_metodo_integral__el_descalce_de_monedas_se_admitira_d531b7 -> Sujeto_rol_alcance_capmin: sin mención
idx 24504: aplica_a Potestad_admision_descalce_de_monedas_metodo_simple__el_descalce_de_monedas_entre_la_expo_157cc5 -> Sujeto_rol_alcance_capmin: sin mención
idx 24506: aplica_a Potestad_admision_descalce_plazos_de_vencimiento__el_descalce_de_plazos_de_vencimiento_se_6c1745 -> Sujeto_rol_alcance_capmin: sin mención
idx 24537: aplica_a Potestad_admision_repatriacion_inversion_directa__la_repatriacion_de_aportes_de_inversion_ce15e7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24539: aplica_a Potestad_admision_tenencia_titulos_carteras_constituidas_exterior__se_admite_la_tenencia__e198c7 -> Sujeto_entidad_financiera: sin mención
idx 24542: aplica_a Potestad_admitir_afectacion_de_bienes_remitidos_por_empresa_distinta__las_entidades_tambi_56c763 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24544: aplica_a Potestad_admitir_creditos_a_residentes_exterior_desfases_liquidacion__se_admite_la_existe_3984b7 -> Sujeto_entidad_financiera: sin mención
idx 24546: aplica_a Potestad_admitir_firmas_de_funcionarios_delegados__alternativamente_se_admitiran_las_firm_b171ae -> Sujeto_rol_alcance_pagjub: sin mención
idx 24552: aplica_a Potestad_admitir_identificadores_alternativos__en_las_situaciones_que_se_detallan_a_conti_dc6259 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24554: aplica_a Potestad_aforo_nulo_en_financiacion_de_titulos_valores__las_operaciones_de_financiacion_c_7f4547 -> Sujeto_rol_alcance_capmin: sin mención
idx 24577: aplica_a Potestad_alusion_adicional_al_paquete_comercial__se_puede_aludir_adicionalmente_al_paquet_2e1ce3 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 24579: aplica_a Potestad_anses_establece_aspectos_no_previstos__en_los_aspectos_no_previstos_por_la_prese_aa4644 -> Sujeto_rol_alcance_pagjub: sin mención
idx 24583: aplica_a Potestad_aplicacion_ampliada_beneficio_durante_2_anos_consecutivos__los_casos_previstos_e_3bc33b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24592: aplica_a Potestad_aplicacion_de_divisas_cobros_exportacion_a_vencimientos__se_admitira_la_aplicaci_ea2bd2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24594: aplica_a Potestad_aplicacion_de_limites_para_ponderador_de_maxima_preferencia__se_podran_aplicar_l_49864c -> Sujeto_rol_alcance_capmin: sin mención
idx 24609: aplica_a Potestad_aplicacion_ponderador_menor_por_transparencia__si_el_ponderador_que_surge_de_la__54461f -> Sujeto_rol_alcance_capmin: sin mención
idx 24611: aplica_a Potestad_aplicar_comisiones_por_precancelacion__la_precancelacion_total_o_parcial_de_fina_4b5c0b -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 24613: aplica_a Potestad_aplicar_comisiones_sobre_fondos_no_utilizados__en_las_operaciones_de_credito_los_91fcd7 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 24615: aplica_a Potestad_aplicar_tratamiento_de_transparencia_look_through__la_entidad_que_posea_o_garant_8e0b48 -> Sujeto_rol_alcance_capmin: sin mención
idx 24624: aplica_a Potestad_aplicar_vencimiento_contractual_instrumentos_proteccion_crediticia__para_los_ins_397d0d -> Sujeto_rol_alcance_capmin: sin mención
idx 24626: aplica_a Potestad_asegurar_comprension_de_deberes_auditores_externos__el_directorio_a_traves_del_c_e63d15 -> Sujeto_entidad_financiera: sin mención
idx 24628: aplica_a Potestad_asignacion_apx_repatriacion_aportes__en_caso_de_que_el_vpu_contemple_la_posibili_f55f06 -> Sujeto_entidad_financiera: sin mención
idx 24630: aplica_a Potestad_asignacion_de_casa_operativa_para_radicacion__las_entidades_financieras_podran_a_74df33 -> Sujeto_entidad_financiera: sin mención
idx 24645: aplica_a Potestad_atencion_obligatoria_de_cheques_no_rechazables__seran_atendidos_los_cheques_pres_53806a -> Sujeto_banco: sin mención
idx 24647: aplica_a Potestad_autoaseguramiento_riesgos_fallecimiento_invalidez__alternativamente_podran_autoa_873e27 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 24651: aplica_a Potestad_autorizacion_acceso_mercado_cambios_pago_dividendos_vpu__las_entidades_podran_da_b60444 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24662: aplica_a Potestad_autorizacion_acceso_mercado_cambios_sin_conformidad_previa_bcra__las_entidades_p_88f983 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24664: aplica_a Potestad_autorizacion_circunstancial_de_sobregiros_en_cuenta_corriente__el_personal_con_a_eac999 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 24666: aplica_a Potestad_autorizacion_dar_acceso_mercado_cambios_cancelacion_deuda_extranjera__las_entida_4950ed -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24668: aplica_a Potestad_autorizacion_de_acumulacion_de_fondos_en_cuentas__se_admitira_que_los_fondos_ori_605a17 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24671: aplica_a Potestad_autorizacion_devolucion_cheques_negociacion__los_cheques_podran_ser_devueltos_a__286b98 -> Sujeto_banco: sin mención
idx 24673: aplica_a Potestad_autorizacion_discrecional_para_acceso_cambios__las_entidades_podran_dar_acceso_a_3eb8e0 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24675: aplica_a Potestad_autorizacion_individual_para_sistemas_de_firma_digitalizada__el_bcra_autorizara__739174 -> Sujeto_banco: sin mención
idx 24677: aplica_a Potestad_autorizacion_para_librar_echeq__podran_librarse_echeq_a_favor_de_una_persona_det_b15397 -> Sujeto_banco: sin mención
idx 24679: aplica_a Potestad_autorizacion_para_librar_endosar_echeq_tras_cumplimiento__la_entidad_financiera__34385e -> Sujeto_banco: sin mención
idx 24692: aplica_a Potestad_autorizacion_previa_sefyc_para_aportes_en_especie__la_sefyc_podra_autorizar_prev_658aa7 -> Sujeto_sefyc: sin mención
idx 24695: aplica_a Potestad_autorizar_divulgacion_datos_cheques_diferidos_operatoria_bursatil__autorizar_a_q_036372 -> Sujeto_banco: sin mención
idx 24697: aplica_a Potestad_aval_electronico_de_echeq__los_echeq_podran_ser_avalados_en_forma_electronica_si_3d8bd7 -> Sujeto_banco: sin mención
idx 24699: aplica_a Potestad_basarse_en_calculos_de_terceros_para_ponderadores__las_entidades_financieras_pod_a6cbe3 -> Sujeto_rol_alcance_capmin: sin mención
idx 24703: aplica_a Potestad_bcra_otorga_conformidad_de_regularizacion__el_bcra_tendra_la_facultad_de_otorgar_6a5f86 -> Sujeto_bcra: sin mención
idx 24705: aplica_a Potestad_bcra_procedera_en_dia_de_aceptacion__el_bcra_en_el_mismo_dia_de_la_aceptacion_pr_5b44c6 -> Sujeto_bcra: sin mención
idx 24707: aplica_a Potestad_boton_de_arrepentimiento_revocacion_de_aceptacion__revocar_la_aceptacion_del_pro_11c00c -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 24729: aplica_a Potestad_calcular_costo_reposicion_como_costo_reposicion_neto__el_costo_de_reposicion_tot_ef191a -> Sujeto_rol_alcance_capmin: sin mención
idx 24773: aplica_a Potestad_cambio_de_metodo_con_preaviso_6_meses__las_entidades_podran_cambiar_el_metodo_em_9d85a2 -> Sujeto_rol_alcance_capmin: sin mención
idx 24775: aplica_a Potestad_canalizar_internamente_requerimientos_derivados_de_acciones_legales__los_requeri_8820bc -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 24777: aplica_a Potestad_cancelacion_discrecional_de_dividendos_cupones__la_entidad_financiera_podra_en_t_1ef118 -> Sujeto_rol_alcance_capmin: sin mención
idx 24779: aplica_a Potestad_cancelacion_en_moneda_extranjera_o_pesos__el_titular_podra_cancelar_los_consumos_2a7610 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24782: aplica_a Potestad_canje_y_arbitraje_sin_conformidad_bcra__las_restantes_operaciones_de_canje_y_arb_c61511 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24784: aplica_a Potestad_canjes_y_arbitrajes_potestad_condicionada__las_entidades_podran_dar_curso_a_esta_eb175e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24786: aplica_a Potestad_clasificacion_de_exposiciones_minoristas_normativas__las_entidades_financieras_p_3f84a3 -> Sujeto_rol_alcance_capmin: sin mención
idx 24788: aplica_a Potestad_clasificacion_en_situacion_normal_si_intereses_pagos__podran_ser_clasificados_en_fb4813 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 24790: aplica_a Potestad_clasificar_por_flujo_de_fondos_proyectado__los_clientes_sin_asistencia_creditici_559447 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 24792: aplica_a Potestad_cliente_podra_formalizar_adhesion_entidad_o_empresa__el_cliente_podra_formalizar_93092e -> Sujeto_cliente: sin mención
idx 24794: aplica_a Potestad_cliente_podra_manifestar_desafectacion_o_baja_del_servicio__igual_opcion_cabra_p_e5202d -> Sujeto_cliente: sin mención
idx 24797: aplica_a Potestad_clientes_pueden_suscribir_bopreal_hasta_suma_adeudada__los_clientes_podran_suscr_6a16f9 -> Sujeto_cliente: sin mención
idx 24820: aplica_a Potestad_clientes_residentes_canalizar_operaciones_sml__los_clientes_residentes_podran_ca_38655f -> Sujeto_cliente: sin mención
idx 24822: aplica_a Potestad_combinacion_de_enfoques_para_requisito_de_capital__las_entidades_podran_usar_una_dc0240 -> Sujeto_rol_alcance_capmin: sin mención
idx 24830: aplica_a Potestad_compensacion_posiciones_compradas_vendidas__en_el_calculo_de_la_exigencia_por_ri_986f68 -> Sujeto_rol_alcance_capmin: sin mención
idx 24832: aplica_a Potestad_compensacion_posiciones_contrarias_mercados_diferentes__se_podran_compensar_no_a_3c2a75 -> Sujeto_rol_alcance_capmin: sin mención
idx 24834: aplica_a Potestad_computacion_de_liquidaciones_y_aplicaciones_de_divisas__la_entidad_encargada_del_62e745 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24846: aplica_a Potestad_conceder_lineas_de_credito_a_bancos_del_exterior__se_podran_conceder_lineas_de_c_f8f60a -> Sujeto_entidad_financiera: sin mención
idx 24848: aplica_a Potestad_confeccion_unico_boleto_multiples_oficializaciones__cuando_la_concertacion_de_ca_966e89 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24850: aplica_a Potestad_conformidad_previa_bcra_cancelacion_cobros__el_bcra_queda_facultado_para_otorgar_db542b -> Sujeto_bcra: sin mención
idx 24853: aplica_a Potestad_conformidad_previa_del_bcra_pago_oficializacion__el_bcra_puede_otorgar_o_denegar_705ec4 -> Sujeto_bcra: sin mención
idx 24855: aplica_a Potestad_conformidad_previa_del_bcra_para_casos_incumplientes__los_casos_que_no_cumplan_l_2c92d7 -> Sujeto_bcra: sin mención
idx 24864: aplica_a Potestad_consideracion_de_cumplimiento_de_seguimiento_permiso_de_embarque__la_entidad_pod_d6f2af -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24866: aplica_a Potestad_consideracion_de_rectificacion_informacion_secoexpo_o_arca__la_entidad_podra_con_e0c2c3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24868: aplica_a Potestad_consideracion_parcial_o_total_del_seguimiento_de_permiso__la_entidad_podra_consi_213ac9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24870: aplica_a Potestad_considerar_cumplimentado_seguimiento_permiso_embarque__la_entidad_podra_consider_57352c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24872: aplica_a Potestad_considerar_operacion_garantizada_por_agencia_oficial__las_entidades_podran_consi_7755ef -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24875: aplica_a Potestad_considerar_operacion_garantizada_por_aseguradora__las_entidades_podran_considera_142f55 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24877: aplica_a Potestad_considerar_operacion_garantizada_por_aseguradora_privada_por_cuenta_de_gobierno__302af8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24879: aplica_a Potestad_considerar_pago_equivalente_a_beneficiario_distinto__las_entidades_podran_consid_9802c7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24881: aplica_a Potestad_contemplar_criterio_de_paridad_de_genero_para_composicion_del_organo_de_fiscaliz_f286a0 -> Sujeto_entidad_financiera: sin mención
idx 24890: aplica_a Potestad_control_de_actividades_funcionarios_influyentes__ejerza_el_control_de_las_activi_8ea78a -> Sujeto_entidad_financiera: sin mención
idx 24892: aplica_a Potestad_dar_acceso_al_mercado_de_cambios_fideicomisos__las_entidades_podran_dar_acceso_a_ff3810 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24894: aplica_a Potestad_dar_acceso_al_mercado_de_cambios_residentes_con_garantias_de_deuda__las_entidade_ad092c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24896: aplica_a Potestad_dar_acceso_mercado_cambios_a_residentes__las_entidades_podran_dar_acceso_al_merc_42e51b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24914: aplica_a Potestad_dar_acceso_mercado_cambios_endeudamientos_y_prefinanciaciones_de_exportacion__la_bb9f6b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24932: aplica_a Potestad_dar_acceso_mercado_cambios_fideicomisos_para_garantizar_servicios__el_acceso_tam_e3795f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24934: aplica_a Potestad_dar_cumplido_de_embarque_del_permiso_definitivo__las_entidades_podran_dar_el_cum_642b46 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24937: aplica_a Potestad_deduccion_previsiones_especificas_posiciones_1250__las_entidades_originantes_pod_0b6341 -> Sujeto_rol_alcance_capmin: sin mención
idx 24939: aplica_a Potestad_definir_libremente_condiciones_instrumentacion_operaciones_crediticias__las_enti_8298f2 -> Sujeto_entidad_financiera: sin mención
idx 24941: aplica_a Potestad_delegacion_en_terceros_rendicion_de_cuentas__los_responsables_de_la_rendicion_de_75b1f8 -> Sujeto_rol_alcance_pagjub: sin mención
idx 24947: aplica_a Potestad_derecho_de_cliente_a_solicitar_primera_reimpresion_sin_costo__por_su_parte_los_c_00c171 -> Sujeto_cliente: sin mención
idx 24952: aplica_a Potestad_determinacion_libre_nivel_posicion_general_cambios__las_entidades_financieras_po_040507 -> Sujeto_entidad_financiera: sin mención
idx 24954: aplica_a Potestad_disponer_perdida_de_beneficios_por_revocacion_multiproducto__la_revocacion_o_res_312cd3 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 24962: aplica_a Potestad_divulgacion_de_memoria_del_directorio_y_estados_financieros__es_recomendable_que_420f31 -> Sujeto_entidad_financiera: sin mención
idx 24965: aplica_a Potestad_ejercicio_de_facultades_disciplinarias_bcra__de_advertir_incumplimientos_ejercer_4f4f76 -> Sujeto_bcra: sin mención
idx 24967: aplica_a Potestad_elaboracion_boleto_global_diario__las_entidades_podran_elaborar_un_boleto_global_679d1f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 24969: aplica_a Potestad_eleccion_enfoque_simplificado_opciones__las_entidades_podran_usar_el_enfoque_sim_b90178 -> Sujeto_rol_alcance_capmin: sin mención
idx 24974: aplica_a Potestad_eleccion_metodo_calculo_opciones__la_entidad_podra_aplicar_un_solo_metodo_de_los_917348 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 24988: aplica_a Potestad_eleccion_metodo_delta_plus_opciones__las_entidades_podran_usar_el_metodo_delta_p_11556c -> Sujeto_rol_alcance_capmin: sin mención
idx 24997: aplica_a Potestad_emision_certificacion_bajo_requisitos_verificados__la_entidad_nominada_podra_emi_c0a382 -> Sujeto_entidad_financiera: sin mención
idx 24999: aplica_a Potestad_emision_certificaciones_aplicacion_divisas_cancelacion_capital_e_intereses__la_e_b4b5eb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25008: aplica_a Potestad_emision_de_certificaciones_cuando_se_verifican_requisitos__la_entidad_nominada_p_cfc005 -> Sujeto_entidad_financiera: sin mención
idx 25010: aplica_a Potestad_emision_de_certificaciones_de_aplicacion__la_entidad_podra_emitir_las_certificac_96dd42 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25021: aplica_a Potestad_emision_de_certificaciones_decreto_277_22__en_el_caso_de_que_el_cliente_sea_un_b_08e8c5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25023: aplica_a Potestad_emision_de_certificaciones_operaciones_parcialmente_liquidadas__se_podra_emitir__9aa27c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25032: aplica_a Potestad_emision_de_certificaciones_por_porcion_no_liquidada__la_entidad_podra_emitir_cer_d322ae -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25034: aplica_a Potestad_emision_de_certificaciones_proporcionales__se_podran_emitir_las_certificaciones__91ce9b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25036: aplica_a Potestad_emision_de_cheques_con_firmas_digitalizadas__podran_emitirse_cheques_mediante_el_e1c562 -> Sujeto_banco: sin mención
idx 25038: aplica_a Potestad_emision_facultativa_de_certificaciones__se_podran_emitir_las_certificaciones_de__2c8593 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25040: aplica_a Potestad_emitir_certificacion_de_aplicacion_de_divisas__la_entidad_podra_emitir_una_certi_baa5cb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25042: aplica_a Potestad_emitir_certificacion_de_aplicacion_repatriacion_aportes_inversion_directa__la_en_f2e67a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25046: aplica_a Potestad_emitir_certificaciones_de_aplicacion_con_imputacion_a_operacion__la_entidad_tamb_9803e5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25048: aplica_a Potestad_emitir_certificaciones_de_aplicacion_de_divisas_a_pago_de_utilidades_y_dividendo_20a3d3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25052: aplica_a Potestad_emitir_certificaciones_de_aplicacion_divisas_a_cancelacion__la_entidad_podra_emi_c4170a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25065: aplica_a Potestad_emitir_certificaciones_de_aplicacion_divisas_cancelacion__la_entidad_podra_emiti_66f564 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25076: aplica_a Potestad_emitir_certificaciones_regimenes_acceso_divisas__en_el_caso_de_que_el_cliente_se_fa2b8a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25079: aplica_a Potestad_encomendar_clasificacion_a_profesionales_externos__el_ejercicio_de_la_opcion_de__7b183d -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 25082: aplica_a Potestad_endoso_electronico_de_echeq__los_echeq_podran_ser_endosados_en_forma_electronica_9b86a6 -> Sujeto_banco: sin mención
idx 25084: aplica_a Potestad_entidad_autorizada_a_dar_acceso_al_mercado_de_cambios_para_pago_al_exterior__la__e52737 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25086: aplica_a Potestad_entidad_elige_titulo_a_entregar_futuro_con_gama_de_instrumentos__la_entidad_podr_7c94ce -> Sujeto_rol_alcance_capmin: sin mención
idx 25088: aplica_a Potestad_entidad_facultada_considerar_cumplimentado_condiciones_alternativas__la_entidad__e1419d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25118: aplica_a Potestad_entidades_autorizadas_a_dar_acceso_a_residentes__las_entidades_podran_dar_acceso_392f7a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25120: aplica_a Potestad_entidades_autorizadas_para_dar_acceso_mercado_cambios_con_requisitos__las_entida_4af3fe -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25122: aplica_a Potestad_entidades_dar_acceso_mercado_cambios__las_entidades_podran_dar_acceso_al_mercado_1dbda6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25142: aplica_a Potestad_entidades_facultadas_dar_acceso_sin_conformidad_previa_bcra__las_entidades_podra_551abe -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25191: aplica_a Potestad_establecer_reglamentaciones_contra_elusion_normativa__facultese_al_banco_central_62fc00 -> Sujeto_bcra: sin mención
idx 25193: aplica_a Potestad_establecer_supuestos_para_acceso_al_mercado_de_cambios__el_banco_central_de_la_r_51823b -> Sujeto_bcra: sin mención
idx 25195: aplica_a Potestad_establecimiento_del_comite_de_gestion_de_riesgos__las_entidades_financieras_qued_55c5d6 -> Sujeto_entidad_financiera: sin mención
idx 25197: aplica_a Potestad_establecimiento_horarios_especiales_adicionales__dentro_de_lo_que_dispongan_las__8b5e14 -> Sujeto_rol_alcance_pagjub: sin mención
idx 25199: aplica_a Potestad_evaluacion_cumplimiento_y_ajustes_sefyc__la_sefyc_evaluara_su_cumplimiento_a_los_2fe664 -> Sujeto_sefyc: sin mención
idx 25201: aplica_a Potestad_exclusion_de_exposiciones_spe_de_activos_subyacentes__a_los_fines_del_calculo_de_0719e1 -> Sujeto_rol_alcance_capmin: sin mención
idx 25203: aplica_a Potestad_exclusion_de_exposiciones_titulizadas_calculo_apr__la_entidad_originante_podra_e_bc33a1 -> Sujeto_rol_alcance_capmin: sin mención
idx 25205: aplica_a Potestad_exclusion_de_ingresos_y_egresos_futuros_esperados__las_entidades_podran_excluir__a8eb82 -> Sujeto_rol_alcance_capmin: sin mención
idx 25207: aplica_a Potestad_exclusion_de_posiciones_opuestas_en_misma_categoria__las_entidades_podran_exclui_797fac -> Sujeto_rol_alcance_capmin: sin mención
idx 25216: aplica_a Potestad_exclusion_de_tenencias_de_titulos_para_colocar_en_plazo_de_cinco_dias__podran_ex_5a981b -> Sujeto_rol_alcance_capmin: sin mención
idx 25218: aplica_a Potestad_exclusion_inmediata_partidas_bi_aprobadas__una_vez_aprobada_la_solicitud_la_enti_f033f5 -> Sujeto_rol_alcance_capmin: sin mención
idx 25220: aplica_a Potestad_exclusion_posiciones_partidas_deducibles__las_entidades_podran_excluir_las_posic_f8d877 -> Sujeto_rol_alcance_capmin: sin mención
idx 25222: aplica_a Potestad_exclusion_titulos_para_colocacion_cinco_dias__podran_excluirse_las_tenencias_de__95b930 -> Sujeto_rol_alcance_capmin: sin mención
idx 25224: aplica_a Potestad_exhibicion_de_dni_d_en_formato_credencial_virtual__el_dni_d_en_formato_credencia_187c5f -> Sujeto_entidad_financiera: sin mención
idx 25226: aplica_a Potestad_exhibicion_dni_d_en_casas_operativas_de_entidades_financieras__el_dni_d_en_forma_b9fe2c -> Sujeto_entidad_financiera: sin mención
idx 25228: aplica_a Potestad_exigencia_acciones_correctivas_incumplimiento_criterios_stc__cuando_la_sefyc_det_bd61c3 -> Sujeto_sefyc: sin mención
idx 25259: aplica_a Potestad_exigencia_de_acciones_correctivas_por_sefyc_ante_incumplimiento_stc__cuando_la_s_ef43ff -> Sujeto_sefyc: sin mención
idx 25265: aplica_a Potestad_exportador_puede_aplicar_divisas_de_anticipos_y_prefinanciaciones__el_exportador_160f39 -> Sujeto_exportador: sin mención
idx 25269: aplica_a Potestad_extender_plazo_liquidacion_permiso_embarque__la_entidad_encargada_del_seguimient_fcaca7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25271: aplica_a Potestad_extension_de_plazo_liquidacion_permiso_embarque__la_entidad_encargada_del_seguim_f9499e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25273: aplica_a Potestad_extension_de_plazo_nacionalizacion_con_mayor_duracion__si_la_nacionalizacion_de__e817fe -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25293: aplica_a Potestad_extension_del_plazo_hasta_120_dias__la_entidad_podra_extender_el_plazo_hasta_los_06dff1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25295: aplica_a Potestad_extension_plazo_ingreso_liquidacion_divisas__la_entidad_encargada_del_seguimient_c19729 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25308: aplica_a Potestad_extension_plazo_liquidacion_permiso_embarque__la_entidad_encargada_del_seguimien_7ada34 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25322: aplica_a Potestad_extensiones_plazo_ingreso_liquidacion_divisas__la_entidad_encargada_del_seguimie_ab8d99 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25324: aplica_a Potestad_facultad_acceso_cambios_gastos_emision_y_servicios__la_entidad_podra_darle_acces_11aba5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25326: aplica_a Potestad_facultad_acceso_mercado_cambios_ef_garantias_y_creditos__las_entidades_financier_cab568 -> Sujeto_entidad_financiera: sin mención
idx 25328: aplica_a Potestad_facultad_acceso_mercado_cambios_fondos_bopreal__los_clientes_podran_acceder_al_m_05f5cf -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25336: aplica_a Potestad_facultad_acceso_mercado_cambios_intereses_devengados__la_entidad_podra_darle_acc_103765 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25338: aplica_a Potestad_facultad_acceso_mercado_cambios_pagos_titulos__las_entidades_podran_dar_acceso_a_eff97c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25340: aplica_a Potestad_facultad_acceso_mercado_de_cambios_importaciones__las_entidades_podran_dar_acces_a0c0e6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25342: aplica_a Potestad_facultad_admitir_aplicacion_cobros_exportaciones__se_admitira_la_aplicacion_de_c_c466a5 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25362: aplica_a Potestad_facultad_aplicar_reducciones_sin_demora__las_reducciones_en_las_comisiones_y_o_c_6890c7 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 25363: aplica_a Potestad_facultad_aplicar_reducciones_sin_demora__las_reducciones_en_las_comisiones_y_o_c_6890c7 -> Sujeto_entidad_financiera: sin mención
idx 25364: aplica_a Potestad_facultad_aplicar_reducciones_sin_demora__las_reducciones_en_las_comisiones_y_o_c_6890c7 -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 25365: aplica_a Potestad_facultad_aplicar_reducciones_sin_demora__las_reducciones_en_las_comisiones_y_o_c_6890c7 -> Sujeto_pspcp: sin mención
idx 25367: aplica_a Potestad_facultad_contratar_o_no_seguro_vida_saldo_deudor__sera_decision_del_sujeto_oblig_2bd2ff -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 25370: aplica_a Potestad_facultad_dar_acceso_repatriacion_capital_no_residente__las_entidades_podran_dar__cf2de2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25372: aplica_a Potestad_facultad_de_acceder_al_mercado_de_cambios__las_entidades_financieras_locales_pod_d1a6fb -> Sujeto_entidad_financiera: sin mención
idx 25374: aplica_a Potestad_facultad_de_acceso_al_cliente_para_pago_de_intereses_y_capital__las_entidades_po_a7c1d4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25398: aplica_a Potestad_facultad_de_acceso_al_mercado_de_cambios_no_residente_acreedor__las_entidades_po_8cdf1c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25400: aplica_a Potestad_facultad_de_acceso_para_pagos_proporcionales_de_fondos_parcialmente_ingresados___acdc47 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25424: aplica_a Potestad_facultad_de_aceptacion_de_cambio_de_entidad_nominada__en_el_caso_de_aceptar_la_n_37352f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25426: aplica_a Potestad_facultad_de_afectar_importaciones_sujeto_a_condiciones__la_entidad_encargada_del_6d9cc2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25429: aplica_a Potestad_facultad_de_computar_diferencia_prevision_niif_9_como_con1__las_entidades_financ_15ac5f -> Sujeto_rol_alcance_capmin: sin mención
idx 25431: aplica_a Potestad_facultad_de_considerar_cumplimentado_seguimiento__la_entidad_podra_considerar_cu_74d4b2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25433: aplica_a Potestad_facultad_de_considerar_cumplimentado_seguimiento_hasta_25__la_entidad_podra_cons_e99b22 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25435: aplica_a Potestad_facultad_de_considerar_exportacion_sin_contravalor__la_entidad_podra_considerar__c93b3f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25437: aplica_a Potestad_facultad_de_cursar_operaciones_sml_en_paraguay_y_uruguay__facultad_de_cursar_ope_3ca66f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25439: aplica_a Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__las_entidades_podran_dar_acceso_al_1dccc4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25441: aplica_a Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__las_entidades_podran_dar_acceso_al_446f8f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25443: aplica_a Potestad_facultad_de_dar_acceso_para_pago_intereses_capital_vpu_con_fondos_parciales__en__a50c73 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25445: aplica_a Potestad_facultad_de_efectuar_retiros_de_fondos__podran_efectuarse_retiros_de_fondos_en_l_3add9a -> Sujeto_rol_alcance_pagjub: sin mención
idx 25447: aplica_a Potestad_facultad_de_emitir_certificaciones__la_entidad_podra_emitir_las_certificaciones__e6d93d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25449: aplica_a Potestad_facultad_de_exclusion_de_exposiciones_subyacentes__la_entidad_originante_podra_e_4a4234 -> Sujeto_entidad_originante_de_transferencia: sin mención
idx 25451: aplica_a Potestad_facultad_de_la_entidad_de_cobrar_registro__la_entidad_puede_decidir_cobrar_por_e_d68e94 -> Sujeto_banco: sin mención
idx 25454: aplica_a Potestad_facultad_de_otorgar_garantias_a_exterior__las_entidades_financieras_podran_otorg_9790fa -> Sujeto_entidad_financiera: sin mención
idx 25456: aplica_a Potestad_facultad_de_otorgar_nuevas_financiaciones__la_entidad_financiera_podra_otorgarle_259aca -> Sujeto_entidad_financiera: sin mención
idx 25458: aplica_a Potestad_facultad_de_realizar_arbitrajes_y_canjes_exterior__las_entidades_podran_realizar_a39025 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25460: aplica_a Potestad_facultad_de_requerir_informacion_con_frecuencia_segun_garantias_preferidas_b__cu_032d0e -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 25464: aplica_a Potestad_facultad_imputar_cumplimiento_seguimiento_rigi__la_entidad_podra_considerar_cump_65eb29 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25466: aplica_a Potestad_facultad_imputar_diferencia_fob_permiso_definitivo_provisorio__cuando_el_valor_f_89104e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25469: aplica_a Potestad_facultad_realizar_arbitrajes_y_canjes_en_el_exterior__las_entidades_podran_reali_9ca437 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25501: aplica_a Potestad_garantias_de_entidades_financieras_locales_o_del_exterior__estas_financiaciones__565335 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25503: aplica_a Potestad_gestion_de_areas_considerando_opiniones_de_comites__gestionar_las_distintas_area_578926 -> Sujeto_entidad_financiera: sin mención
idx 25505: aplica_a Potestad_habilitacion_acceso_mercado_cambios_para_pagos_fideicomiso__las_entidades_podran_1a7b95 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25507: aplica_a Potestad_habilitacion_aplicacion_cobros_exportaciones_repatriaciones_vpu_rigi__la_aplicac_7bec4a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25509: aplica_a Potestad_habilitacion_aplicacion_cobros_exportaciones_y_servicios__la_aplicacion_de_cobro_ca248a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25511: aplica_a Potestad_habilitacion_cobros_de_exportaciones_financiaciones_importaciones__financiacione_fcc3ec -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25513: aplica_a Potestad_habilitacion_de_cobro_en_divisas_para_exportaciones__se_admitira_la_aplicacion_d_69e486 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25515: aplica_a Potestad_habilitacion_para_aplicar_cobros_exportaciones__la_aplicacion_de_cobros_de_expor_9c019e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25517: aplica_a Potestad_habilitacion_para_cancelar_servicios_de_endeudamiento__los_endeudamientos_financ_2934fc -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25519: aplica_a Potestad_habilitacion_para_cancelar_servicios_desde_vencimiento__las_emisiones_de_titulos_025f03 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25521: aplica_a Potestad_habilitar_acceso_al_mercado_de_cambios__las_entidades_podran_dar_acceso_al_merca_1181cd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25524: aplica_a Potestad_importador_opcion_excepcion_demostracion_ingreso_fondos__el_importador_podra_opt_3bf167 -> Sujeto_importador: sin mención
idx 25526: aplica_a Potestad_imputacion_alternativa_liquidaciones_permiso_embarque__las_liquidaciones_y_o_apl_188f0b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25528: aplica_a Potestad_imputacion_de_divisas_al_embarque_de_reemplazo__en_caso_de_haberse_imputado_cobr_94661a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25530: aplica_a Potestad_imputacion_de_financiaciones_con_ingresos_en_moneda_extranjera__aun_cuando_los_i_e5cb5f -> Sujeto_entidad_financiera: sin mención
idx 25532: aplica_a Potestad_imputacion_de_financiaciones_transferidas_a_capacidad_prestamo__podran_imputarse_fe1a05 -> Sujeto_entidad_financiera: sin mención
idx 25548: aplica_a Potestad_imputacion_de_prestamos_interfinancieros__las_entidades_podran_imputar_a_los_rec_25a5f1 -> Sujeto_entidad_financiera: sin mención
idx 25550: aplica_a Potestad_imputacion_discrecional_creditos_a_deudor_en_concurso__a_los_fines_de_esta_clasi_390176 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 25552: aplica_a Potestad_imputacion_discrecional_creditos_sobre_documentos_cedidos__igual_temperamento_po_b1f847 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 25554: aplica_a Potestad_inclusion_de_directores_independientes_y_calificados__la_independencia_y_objetiv_1049a7 -> Sujeto_entidad_financiera: sin mención
idx 25558: aplica_a Potestad_incorporacion_progresiva_de_mujeres_en_designaciones_y_renovaciones__se_recomien_70837b -> Sujeto_entidad_financiera: sin mención
idx 25560: aplica_a Potestad_independencia_incentivos_personal_control_financiero_y_riesgo__se_considera_como_6d8dbe -> Sujeto_entidad_financiera: sin mención
idx 25562: aplica_a Potestad_ingreso_y_liquidacion_por_deudor_o_empresa_grupo_economico__los_endeudamientos_f_a2e04d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25564: aplica_a Potestad_iniciacion_de_oficio_de_acciones_correctivas__el_bcra_iniciara_de_oficio_accione_b4b0c4 -> Sujeto_bcra: sin mención
idx 25566: aplica_a Potestad_interpretacion_contractual_favorable_al_usuario__la_interpretacion_del_contrato__f3b61a -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 25568: aplica_a Potestad_interpretacion_obligacion_menos_gravosa_ante_dudas__cuando_existan_dudas_sobre_e_c2fdca -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 25572: aplica_a Potestad_limitacion_de_exigencia_posicion_individual_derivado_credito_titulizacion__las_e_af32b2 -> Sujeto_rol_alcance_capmin: sin mención
idx 25574: aplica_a Potestad_liquidacion_en_pesos_titulos_concertados_en_el_pais__aquellas_operaciones_concer_1f651f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25576: aplica_a Potestad_liquidacion_otras_ventas_titulos_valores_con_limite_de_valor__los_clientes_podra_b2e6df -> Sujeto_cliente: sin mención
idx 25623: aplica_a Potestad_mantencion_de_depositos_en_garantias_en_exterior__las_entidades_financieras_podr_c060f6 -> Sujeto_entidad_financiera: sin mención
idx 25626: aplica_a Potestad_mantener_cuentas_en_bancos_del_exterior__las_entidades_financieras_podran_manten_806037 -> Sujeto_entidad_financiera: sin mención
idx 25628: aplica_a Potestad_mantener_tratamiento_qccp_periodo_transitorio__en_los_casos_en_que_una_ccp_deje__a7c258 -> Sujeto_rol_alcance_capmin: sin mención
idx 25632: aplica_a Potestad_metodo_simplificado_opciones_compradas__las_entidades_que_solo_compren_opciones__70a0d7 -> Sujeto_rol_alcance_capmin: sin mención
idx 25637: aplica_a Potestad_modificacion_de_entidad_nominada__el_exportador_puede_modificar_la_entidad_nomin_c696c9 -> Sujeto_exportador: sin mención
idx 25640: aplica_a Potestad_modificacion_posterior_del_seguimiento_por_exportador__pudiendo_el_exportador_mo_dd6e7e -> Sujeto_exportador: sin mención
idx 25642: aplica_a Potestad_modificar_entidad_seguimiento_a_voluntad__a_voluntad_del_exportador_podra_modifi_bd16cf -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25644: aplica_a Potestad_no_involucrarse_en_decisiones_menores__no_se_involucre_en_la_toma_de_decisiones__466169 -> Sujeto_entidad_financiera: sin mención
idx 25646: aplica_a Potestad_no_residentes_suscripcion_bopreal__los_clientes_no_residentes_podran_suscribir_b_f3e2de -> Sujeto_cliente: sin mención
idx 25655: aplica_a Potestad_no_reune_condicion_independencia_por_vinculo_familiar__un_miembro_del_directorio_5614c8 -> Sujeto_entidad_financiera: sin mención
idx 25658: aplica_a Potestad_observar_criterio_paridad_genero_conformacion_directorio__se_considera_una_buena_71bf8e -> Sujeto_entidad_financiera: sin mención
idx 25660: aplica_a Potestad_opcion_conformacion_comite_alternativo__cuando_la_dimension_operatoria_y_o_clien_4c4286 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 25663: aplica_a Potestad_opcion_de_agrupamiento_de_financiaciones_comerciales__a_opcion_de_la_entidad_las_bb688f -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 25666: aplica_a Potestad_opcion_de_agrupar_financiaciones_comerciales__el_ejercicio_de_la_opcion_de_agrup_136bd4 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 25669: aplica_a Potestad_opcion_de_deducir_margenes_comerciales__las_entidades_pueden_optar_por_deducir_l_3a8cea -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 25677: aplica_a Potestad_opcion_de_forma_de_emision_certificados__los_certificados_podran_extenderse_a_so_415a1d -> Sujeto_entidad_depositaria: sin mención
idx 25679: aplica_a Potestad_opcion_de_imputar_diferencia_en_reembarque__podra_imputarse_al_embarque_por_el_c_e5c420 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25681: aplica_a Potestad_opcion_de_instrumentacion_de_fondos_transferencia_o_cheque__los_movimientos_de_f_9b7680 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25683: aplica_a Potestad_opcion_de_proteccion_crediticia_en_tramos__la_entidad_financiera_podra_obtener_p_0be4a1 -> Sujeto_rol_alcance_capmin: sin mención
idx 25694: aplica_a Potestad_opcion_expandir_posiciones_superpuestas__la_entidad_podra_expandir_las_posicione_852c97 -> Sujeto_rol_alcance_capmin: sin mención
idx 25696: aplica_a Potestad_opcion_imputacion_a_escala_unica_monedas_residuales__cuando_el_total_de_las_oper_93083c -> Sujeto_rol_alcance_capmin: sin mención
idx 25698: aplica_a Potestad_opcion_incluir_ingresos_egresos_futuros_cubiertos__a_discrecion_de_la_entidad_in_b73ffa -> Sujeto_rol_alcance_capmin: sin mención
idx 25701: aplica_a Potestad_opcion_separar_posiciones_superpuestas__la_entidad_podra_separar_o_expandir_sus__80daee -> Sujeto_rol_alcance_capmin: sin mención
idx 25703: aplica_a Potestad_opcion_transmision_cheque_con_clausula__transmision_de_cheques_con_clausula_no_a_51316f -> Sujeto_banco: sin mención
idx 25705: aplica_a Potestad_operaciones_por_ventanilla_sin_restricciones__los_usuarios_de_servicios_financie_f81c2e -> Sujeto_usuario_de_servicios_financieros: sin mención
idx 25726: aplica_a Potestad_operar_sin_limite_de_horario_mercado_de_cambios__las_entidades_podran_operar_sin_5580b1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25728: aplica_a Potestad_otorgar_acceso_al_mercado_de_cambios_para_compras_de_tiendas_libres_de_impuestos_239155 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25730: aplica_a Potestad_otorgar_acceso_al_mercado_de_cambios_residentes_con_aplicacion_especifica__las_e_0f7141 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25732: aplica_a Potestad_otorgar_acceso_mercado_cambios_deudas_no_comerciales__la_entidad_interviniente_p_d17f03 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25734: aplica_a Potestad_otorgar_adelanto_en_efectivo_en_el_exterior__las_entidades_financieras_y_otras_e_df3204 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 25735: aplica_a Potestad_otorgar_adelanto_en_efectivo_en_el_exterior__las_entidades_financieras_y_otras_e_df3204 -> Sujeto_entidad_financiera: sin mención
idx 25737: aplica_a Potestad_otorgar_aval_sin_restriccion_de_registro__podra_ser_otorgado_sobre_cheques_de_pa_d2ff2c -> Sujeto_banco: sin mención
idx 25739: aplica_a Potestad_otorgar_prestamos_pesos_con_retribucion_variable__las_entidades_financieras_podr_24090d -> Sujeto_entidad_financiera: sin mención
idx 25755: aplica_a Potestad_pactar_retribuciones_por_negociacion_bursatil_de_cheques__por_las_prestaciones_d_beea6d -> Sujeto_banco: sin mención
idx 25757: aplica_a Potestad_pago_directo_a_clientes_cheques_cruzados__los_cheques_con_cruzamiento_general_o__7e2c57 -> Sujeto_banco: sin mención
idx 25764: aplica_a Potestad_permanencia_en_situacion_normal_deudores_refinanciados_hasta_2_veces_en_12_meses_87a041 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 25766: aplica_a Potestad_permanencia_fondos_en_cuentas_exterior_sin_restriccion_gafi__los_fondos_tambien__487333 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25771: aplica_a Potestad_permiso_descalce_de_monedas__el_descalce_de_monedas_se_permitira_siempre_que_se__17afd7 -> Sujeto_rol_alcance_capmin: sin mención
idx 25783: aplica_a Potestad_permitir_reversion_del_aporte__las_entidades_financieras_deberan_permitir_la_rev_fae5de -> Sujeto_banco: sin mención
idx 25785: aplica_a Potestad_plazo_de_6_meses_para_aplicar_nuevas_disposiciones__las_entidades_financieras_qu_151009 -> Sujeto_rol_alcance_capmin: sin mención
idx 25787: aplica_a Potestad_plazo_para_presentacion_hasta_undecimo_dia_habil__la_presentacion_de_la_rendicio_3eb893 -> Sujeto_rol_alcance_pagjub: sin mención
idx 25789: aplica_a Potestad_podran_suscribir_bopreal_importadores__los_importadores_de_bienes_podran_suscrib_06ffbd -> Sujeto_importador_de_bienes: sin mención
idx 25791: aplica_a Potestad_potestad_ajustes_valuacion_modelo__cuando_sea_necesario_se_deberan_hacer_ajustes_421c83 -> Sujeto_rol_alcance_capmin: sin mención
idx 25797: aplica_a Potestad_potestad_de_afectar_registro_aduanero_requisitos_cumplidos__la_entidad_encargada_365949 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25811: aplica_a Potestad_potestad_de_ejercer_acciones_contra_garante__en_caso_de_incumplimiento_de_la_con_9a7220 -> Sujeto_rol_alcance_capmin: sin mención
idx 25813: aplica_a Potestad_potestad_de_emitir_certificaciones_de_divisas__la_entidad_podra_emitir_las_certi_980150 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25817: aplica_a Potestad_potestad_de_valuar_a_modelo_cuando_no_sea_posible_mercado__se_podra_valuar_a_mod_616cdb -> Sujeto_rol_alcance_capmin: sin mención
idx 25819: aplica_a Potestad_potestad_gestiones_baja_rechazos_fuera_de_termino__la_formulacion_de_la_citada_d_337df0 -> Sujeto_banco: sin mención
idx 25821: aplica_a Potestad_potestad_medidas_prudentes_ajustes_verificacion__a_efectos_de_una_verificacion_i_4c6db2 -> Sujeto_rol_alcance_capmin: sin mención
idx 25823: aplica_a Potestad_potestad_no_reconocer_compensaciones_entre_bandas_temporales_tasa_de_interes__la_b4e4c6 -> Sujeto_rol_alcance_capmin: sin mención
idx 25825: aplica_a Potestad_potestad_sefyc_para_requerir_definiciones_precisas_de_commodities__el_area_de_su_b1c962 -> Sujeto_sefyc: sin mención
idx 25827: aplica_a Potestad_precancelacion_de_capital_e_intereses_de_linea_de_credito__si_la_financiacion_pr_4bef55 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25829: aplica_a Potestad_promocion_de_mecanismos_de_gestion_con_equidad_de_genero__promueva_mecanismos_de_bd62ee -> Sujeto_entidad_financiera: sin mención
idx 25831: aplica_a Potestad_prorrogas_hasta_5_180_dias_para_documentacion_aduanera__la_entidad_a_cargo_del_s_dd777b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25833: aplica_a Potestad_realizacion_de_compensaciones_horizontales__las_entidades_podran_realizar_dos_se_7ea5e2 -> Sujeto_rol_alcance_capmin: sin mención
idx 25835: aplica_a Potestad_realizacion_sin_restricciones_arbitraje_con_debito_de_moneda_extranjera__las_ope_7bf2ea -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25837: aplica_a Potestad_realizar_canjes_y_arbitrajes_no_asociados_a_ingresos_de_divisas__las_entidades_p_47928d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25839: aplica_a Potestad_recategorizacion_de_deuda_como_acciones__a_los_fines_del_cumplimiento_de_estas_d_1fe0e4 -> Sujeto_sefyc: sin mención
idx 25841: aplica_a Potestad_reclasificacion_a_nivel_superior_por_cancelacion_porcentual__cuando_se_trate_de__7ae9f7 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 25843: aplica_a Potestad_reclasificacion_a_nivel_superior_por_cumplimiento_de_cuotas__los_clientes_cuyas__1b6cd4 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 25851: aplica_a Potestad_reclasificacion_al_nivel_superior_refinanciacion_periodica__los_clientes_cuyas_d_832ec9 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 25854: aplica_a Potestad_reclasificacion_unica_en_tratamiento_especial__el_cliente_podra_ser_reclasificad_166523 -> Sujeto_cliente: sin mención
idx 25856: aplica_a Potestad_recomendacion_establecimiento_de_otros_comites_especializados__se_recomienda_el__14a497 -> Sujeto_entidad_financiera: sin mención
idx 25858: aplica_a Potestad_reconocer_activos_dados_en_garantia_por_spe__se_podran_reconocer_los_activos_dad_db01ee -> Sujeto_rol_alcance_capmin: sin mención
idx 25860: aplica_a Potestad_reconocer_garantia_aportada_cliente_tanto_tramo_ccp_miembro_como_cliente_miembro_5cda5a -> Sujeto_miembro_compensador: sin mención
idx 25862: aplica_a Potestad_reconocer_proteccion_crediticia_en_titulizaciones__al_calcular_la_exigencia_de_c_19cacb -> Sujeto_rol_alcance_capmin: sin mención
idx 25864: aplica_a Potestad_reconocimiento_de_cobertura_por_comprador__la_entidad_financiera_compradora_de_l_2d8c78 -> Sujeto_rol_alcance_capmin: sin mención
idx 25870: aplica_a Potestad_reconocimiento_de_coberturas_capital_en_titulizaciones__se_podra_reconocer_el_em_b9cc1d -> Sujeto_rol_alcance_capmin: sin mención
idx 25872: aplica_a Potestad_reconocimiento_de_intereses_sobre_saldos_acreedores__podran_reconocerse_sobre_lo_580205 -> Sujeto_banco: sin mención
idx 25876: aplica_a Potestad_recurrir_a_otra_informacion_divulgada_por_fondo__las_fuentes_de_informacion_no_s_07e032 -> Sujeto_rol_alcance_capmin: sin mención
idx 25878: aplica_a Potestad_reduccion_exigencia_capital_posicion_cubierta_primer_incumplimiento__cuando_la_e_6b0d92 -> Sujeto_rol_alcance_capmin: sin mención
idx 25881: aplica_a Potestad_reemplazo_talon_por_duplicado_formula_opcion_banco__dicho_talon_podra_ser_reempl_4188f7 -> Sujeto_banco: sin mención
idx 25884: aplica_a Potestad_reiterar_presentacion_rechazada__si_la_presentacion_es_rechazada_podra_ser_reali_a2656e -> Sujeto_rol_alcance_pagjub: sin mención
idx 25888: aplica_a Potestad_requerimiento_de_certificaciones_de_acceso__las_entidades_podran_requerirle_las__470bd1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25892: aplica_a Potestad_rescate_de_instrumentos_ca_cinco_anos_minimo__la_entidad_financiera_podra_rescat_f4fccb -> Sujeto_rol_alcance_capmin: sin mención
idx 25894: aplica_a Potestad_rescate_de_instrumentos_transcurridos_5_anos__la_entidad_financiera_podra_rescat_042dab -> Sujeto_rol_alcance_capmin: sin mención
idx 25897: aplica_a Potestad_revision_ponderador_2_aplicacion_a_indices_diversificados__sera_objeto_de_revisi_6a456b -> Sujeto_sefyc: sin mención
idx 25899: aplica_a Potestad_se_admite_descalce_monedas_sin_tratamiento__se_admitira_el_descalce_de_monedas_e_557a32 -> Sujeto_rol_alcance_capmin: sin mención
idx 25901: aplica_a Potestad_se_admitira_la_aplicacion_de_divisas_de_cobros__se_admitira_la_aplicacion_de_div_d6b5c5 -> Sujeto_entidad_cambiaria: sin mención
idx 25902: aplica_a Potestad_se_admitira_la_aplicacion_de_divisas_de_cobros__se_admitira_la_aplicacion_de_div_d6b5c5 -> Sujeto_entidad_financiera: sin mención
idx 25904: aplica_a Potestad_sefyc_acceso_a_informacion_sobre_incentivos__la_superintendencia_de_entidades_fi_c31602 -> Sujeto_sefyc: sin mención
idx 25906: aplica_a Potestad_sefyc_aprobacion_capitalizacion__la_decision_de_capitalizacion_sera_ad_referendu_b6e91f -> Sujeto_sefyc: sin mención
idx 25909: aplica_a Potestad_sefyc_exigir_medidas_especificas_entidad_atipica__la_sefyc_podra_exigirle_a_la_e_af6e57 -> Sujeto_sefyc: sin mención
idx 25913: aplica_a Potestad_solicitar_ampliacion_de_plazo_exportador__el_exportador_podra_solicitar_a_la_ent_6a5b88 -> Sujeto_exportador: sin mención
idx 25916: aplica_a Potestad_solicitar_ampliacion_plazo_liquidacion_divisas__el_exportador_podra_solicitar_a__e89a3a -> Sujeto_exportador: sin mención
idx 25918: aplica_a Potestad_solicitar_ampliacion_plazo_liquidacion_divisas__el_exportador_podra_solicitar_qu_d5f02a -> Sujeto_exportador: sin mención
idx 25919: aplica_a Potestad_solicitar_ampliacion_plazo_liquidacion_divisas__el_exportador_podra_solicitar_qu_d5f02a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 25921: aplica_a Potestad_solicitar_informacion_sobre_uso_de_cajeros_automaticos__solicitar_al_personal_de_7c732c -> Sujeto_banco: sin mención
idx 25924: aplica_a Potestad_solicitar_nuevas_copias_de_contrato_vigente__el_usuario_de_servicios_financieros_4eaba3 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 25925: aplica_a Potestad_solicitar_nuevas_copias_de_contrato_vigente__el_usuario_de_servicios_financieros_4eaba3 -> Sujeto_usuario_de_servicios_financieros: sin mención
idx 25927: aplica_a Potestad_solicitud_ampliacion_plazo_liquidacion_hasta_quinto_dia_habil__el_exportador_pod_3ee826 -> Sujeto_exportador: sin mención
idx 25929: aplica_a Potestad_solicitud_de_ampliacion_de_plazo_liquidacion_divisas__el_exportador_podra_solici_2731b5 -> Sujeto_exportador: sin mención
idx 25936: aplica_a Potestad_solicitud_exclusion_operaciones_discontinuadas_del_bi__las_entidades_financieras_059a50 -> Sujeto_rol_alcance_capmin: sin mención
idx 25938: aplica_a Potestad_solicitud_extension_plazo_por_determinacion_precio__el_exportador_podra_solicita_6dfc73 -> Sujeto_exportador: sin mención
idx 25943: aplica_a Potestad_solicitud_parcial_total_cumplimiento_seguimiento_permiso__el_exportador_podra_so_097945 -> Sujeto_exportador: sin mención
idx 25949: aplica_a Potestad_solucionar_rechazos_y_reintentar_presentacion__hasta_la_fecha_limite_la_entidad__945412 -> Sujeto_rol_alcance_pagjub: sin mención
idx 25951: aplica_a Potestad_suministro_de_informacion_de_clientes_en_apertura_remota__las_entidades_financie_9ebb8d -> Sujeto_banco: sin mención
idx 25955: aplica_a Potestad_suscripcion_de_bopreal_hasta_monto_de_deuda_pendiente__los_importadores_de_biene_ace6ef -> Sujeto_importador_de_bienes: sin mención
idx 25957: aplica_a Potestad_suscripcion_de_bopreal_hasta_monto_de_intereses_compensatorios__por_hasta_el_mon_318dda -> Sujeto_cliente: sin mención
idx 25976: aplica_a Potestad_suspension_automatica_sin_comunicacion_del_bcra__la_suspension_procedera_sin_que_67a973 -> Sujeto_bcra: sin mención
idx 25978: aplica_a Potestad_suspension_del_tratamiento_stc_por_sefyc__cuando_la_sefyc_detecte_que_una_tituli_56450a -> Sujeto_sefyc: sin mención
idx 25983: aplica_a Potestad_suspension_tratamiento_stc_incumplimiento_criterios__la_sefyc_podra_determinar_q_90afbd -> Sujeto_sefyc: sin mención
idx 26015: aplica_a Potestad_tenedor_solicitar_certificacion_oficial_de_rechazo__el_tenedor_podra_a_fin_de_co_b5e0d7 -> Sujeto_cliente: sin mención
idx 26017: aplica_a Potestad_tenedor_verificar_rechazo_en_sitio_bcra__el_tenedor_de_un_cheque_rechazado_por_i_50e057 -> Sujeto_cliente: sin mención
idx 26019: aplica_a Potestad_titular_puede_cancelar_en_moneda_extranjera_o_pesos__el_titular_podra_cancelar_l_c72ab7 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 26021: aplica_a Potestad_usar_informacion_de_reglamento_o_legislacion_nacional__bajo_el_enfoque_mba_las_e_54a1ba -> Sujeto_rol_alcance_capmin: sin mención
idx 26024: aplica_a Potestad_usuario_puede_informar_al_bcra_de_reclamo__el_usuario_de_servicios_financieros_p_af68fc -> Sujeto_usuario_de_servicios_financieros: sin mención
idx 26027: aplica_a Potestad_utilizacion_inmediata_de_tecnologia_para_uso_propio__la_utilizacion_de_la_tecnol_86d318 -> Sujeto_banco: sin mención
idx 26029: aplica_a Potestad_utilizacion_mecanismos_punto_7_9_en_adicion__los_exportadores_podran_utilizar_lo_c28e4d -> Sujeto_exportador: sin mención
idx 26042: aplica_a Potestad_venta_de_bopreal_contra_cable_en_exterior__los_clientes_que_hayan_adquirido_bono_81dd49 -> Sujeto_cliente: sin mención
idx 26063: aplica_a Restriccion_15_quince_por_ciento_cuando_corresponda_a_bienes_que_tienen_asignado_un_plazo_de_32c86b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26069: aplica_a Restriccion_180_ciento_ochenta_dias_corridos_para_el_resto_de_los_bienes__ext_7_1_1_4_9e53ce -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26080: aplica_a Restriccion_a_fin_de_asegurar_que_solo_se_asignen_a_una_titulizacion_documentos_a_cobrar_o_d_c636f5 -> Sujeto_rol_alcance_capmin: sin mención
idx 26082: aplica_a Restriccion_a_la_fecha_de_corte_el_monto_total_de_las_exposiciones_a_un_deudor_en_particular_76fc89 -> Sujeto_rol_alcance_capmin: sin mención
idx 26084: aplica_a Restriccion_a_la_fecha_de_corte_teniendo_en_cuenta_las_tecnicas_de_cobertura_del_riesgo_cred_45d39f -> Sujeto_rol_alcance_capmin: sin mención
idx 26086: aplica_a Restriccion_a_la_fecha_de_corte_teniendo_en_cuenta_las_tecnicas_de_cobertura_del_riesgo_cred_962d2b -> Sujeto_rol_alcance_capmin: sin mención
idx 26088: aplica_a Restriccion_a_la_fecha_de_corte_teniendo_en_cuenta_las_tecnicas_de_cobertura_del_riesgo_cred_d51da9 -> Sujeto_rol_alcance_capmin: sin mención
idx 26090: aplica_a Restriccion_a_la_fecha_de_corte_teniendo_en_cuenta_las_tecnicas_de_cobertura_del_riesgo_cred_e8950f -> Sujeto_rol_alcance_capmin: sin mención
idx 26092: aplica_a Restriccion_a_las_entidades_participantes_que_efectuaran_la_presentacion_de_la_rendicion_de__2228cb -> Sujeto_rol_alcance_pagjub: sin mención
idx 26095: aplica_a Restriccion_a_los_46_o_mas_dias_habiles_posteriores_a_la_fecha_de_liquidacion_la_exigencia_d_64e8b7 -> Sujeto_rol_alcance_capmin: sin mención
idx 26098: aplica_a Restriccion_a_los_efectos_del_cumplimiento_de_los_citados_puntos_se_debera_contar_con_califi_a61ec4 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 26102: aplica_a Restriccion_a_partir_del_reconocimiento_inicial_cada_doce_meses_dicho_limite_se_reduce_en_10_4b96aa -> Sujeto_rol_alcance_capmin: sin mención
idx 26109: aplica_a Restriccion_al_banco_de_pagos_internacionales_al_fondo_monetario_internacional_al_banco_cent_623767 -> Sujeto_banco_central_del_exterior: sin mención
idx 26110: aplica_a Restriccion_al_banco_de_pagos_internacionales_al_fondo_monetario_internacional_al_banco_cent_623767 -> Sujeto_banco_multilateral_de_desarrollo: sin mención
idx 26111: aplica_a Restriccion_al_banco_de_pagos_internacionales_al_fondo_monetario_internacional_al_banco_cent_623767 -> Sujeto_fmi: sin mención
idx 26113: aplica_a Restriccion_al_bcra_en_pesos_cuando_su_fuente_de_fondos_sea_en_esa_moneda_ponderador_0__cap__71cc55 -> Sujeto_rol_alcance_capmin: sin mención
idx 26116: aplica_a Restriccion_al_cierre_del_primer_semestre_calendario_el_examen_debera_haber_alcanzado_no_men_67265b -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 26122: aplica_a Restriccion_ante_la_deteccion_de_inconsistencias_en_la_documentacion_presentada_por_un_clien_b5e8af -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26125: aplica_a Restriccion_aplicar_ponderador_de_riesgo_del_1250_a_los_compromisos_no_desembolsados_con_ccp_ed13df -> Sujeto_rol_alcance_capmin: sin mención
idx 26128: aplica_a Restriccion_aplicara_el_tipo_de_cambio_vendedor_para_operaciones_efectuadas_a_traves_de_medi_795f4a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26134: aplica_a Restriccion_banco_de_pagos_internacionales_fondo_monetario_internacional_banco_central_europ_fa9535 -> Sujeto_banco_multilateral_de_desarrollo: sin mención
idx 26135: aplica_a Restriccion_banco_de_pagos_internacionales_fondo_monetario_internacional_banco_central_europ_fa9535 -> Sujeto_fmi: sin mención
idx 26140: aplica_a Restriccion_bcra_gobierno_nacional_gobiernos_provinciales_municipales_y_de_la_caba_en_pesos__7f69d2 -> Sujeto_bcra: sin mención
idx 26141: aplica_a Restriccion_bcra_gobierno_nacional_gobiernos_provinciales_municipales_y_de_la_caba_en_pesos__7f69d2 -> Sujeto_sector_publico_no_financiero: sin mención
idx 26144: aplica_a Restriccion_bcra_y_sector_publico_no_financiero_demas_categorias_exigencia_de_capital_por_ri_94fc53 -> Sujeto_bcra: sin mención
idx 26145: aplica_a Restriccion_bcra_y_sector_publico_no_financiero_demas_categorias_exigencia_de_capital_por_ri_94fc53 -> Sujeto_sector_publico_no_financiero: sin mención
idx 26148: aplica_a Restriccion_cada_comunicacion_al_bcra_incluira_informaciones_referidas_a_esas_situaciones_co_f8e077 -> Sujeto_banco: sin mención
idx 26151: aplica_a Restriccion_cargo_directo_de_capital_del_100_cuando_los_pagos_no_se_realicen_dentro_de_46_o__0b36c0 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 26160: aplica_a Restriccion_cargo_directo_de_capital_del_50_cuando_los_pagos_no_se_realicen_dentro_de_entre__89cbb1 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 26169: aplica_a Restriccion_cargo_directo_de_capital_del_75_cuando_los_pagos_no_se_realicen_dentro_de_entre__124605 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 26178: aplica_a Restriccion_cargo_directo_de_capital_del_8_cuando_los_pagos_no_se_realicen_dentro_de_entre_5_37753f -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 26187: aplica_a Restriccion_cargos_en_exceso_de_los_costos_de_los_servicios_que_terceros_les_cobraron_a_los__0235e5 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 26190: aplica_a Restriccion_causas_de_fuerza_mayor_al_momento_de_la_presentacion_del_cheque_que_impidan_su_p_6b82ff -> Sujeto_banco: sin mención
idx 26193: aplica_a Restriccion_cheque_cuya_fecha_de_emision_es_posterior_al_dia_de_su_presentacion_al_cobro_o_d_9d5774 -> Sujeto_banco: sin mención
idx 26195: aplica_a Restriccion_clausulas_que_amplien_derechos_del_sujeto_obligado_se_tendran_por_no_escritas__p_f29264 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 26197: aplica_a Restriccion_clausulas_que_importen_una_renuncia_o_restriccion_a_los_derechos_del_usuario_de__7607c5 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 26199: aplica_a Restriccion_comisiones_en_exceso_de_las_maximas_fijadas_por_el_bcra_que_sean_de_aplicacion___27266d -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 26202: aplica_a Restriccion_como_el_periodo_de_liquidacion_close_out_para_las_operaciones_compensadas_de_los_143ac7 -> Sujeto_miembro_compensador: sin mención
idx 26204: aplica_a Restriccion_como_maximo_8_dias_corridos_despues_de_finalizado_cada_mes_y_o_el_periodo_menor__8e0a93 -> Sujeto_banco: sin mención
idx 26222: aplica_a Restriccion_contrato_social_vencido_al_momento_de_la_emision_del_cheque__ctacte_6_1_2_3_400e73 -> Sujeto_banco: sin mención
idx 26225: aplica_a Restriccion_cualquier_mecanismo_previsto_en_las_normas_cambiarias_que_tome_en_consideracion__273db0 -> Sujeto_vpu_rigi: sin mención
idx 26232: aplica_a Restriccion_cualquier_mecanismo_previsto_en_las_normas_cambiarias_que_tome_en_consideracion__2b01a6 -> Sujeto_vpu_rigi: sin mención
idx 26235: aplica_a Restriccion_cuando_el_cliente_no_este_protegido_de_sufrir_perdidas_en_caso_de_falta_de_pago__d1e044 -> Sujeto_cliente: sin mención
idx 26238: aplica_a Restriccion_cuando_el_total_de_participaciones_en_el_capital_de_entidades_financieras_empres_56b683 -> Sujeto_rol_alcance_capmin: sin mención
idx 26241: aplica_a Restriccion_cuando_la_cuenta_opera_en_dolares_estadounidenses_solo_se_podran_girar_cheques_l_1f077c -> Sujeto_banco: sin mención
idx 26244: aplica_a Restriccion_cuando_la_entidad_que_reciba_los_activos_en_garantia_sea_la_ccp_se_aplicara_un_p_06f892 -> Sujeto_rol_alcance_capmin: sin mención
idx 26247: aplica_a Restriccion_cuando_la_medida_de_riesgo_de_tasa_de_interes_eve_estandarizada_supere_el_15_del_77f20a -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 26262: aplica_a Restriccion_cuando_la_utilizacion_de_los_mecanismos_del_punto_7_9_redunde_en_un_monto_que_ex_7b059c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26267: aplica_a Restriccion_cuando_se_otorgue_asistencia_en_moneda_distinta_de_la_de_los_recursos_del_exteri_633948 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 26273: aplica_a Restriccion_cuando_se_trate_de_firmas_extranjeras_que_no_cumplan_con_lo_indicado_en_el_parra_cf18b2 -> Sujeto_banco: sin mención
idx 26277: aplica_a Restriccion_cuando_se_trate_de_instrumentos_que_no_satisfagan_la_definicion_de_activos_admit_c4b8c1 -> Sujeto_rol_alcance_capmin: sin mención
idx 26281: aplica_a Restriccion_cuando_se_value_a_modelo_se_deberan_aplicar_criterios_aun_mas_conservadores__cap_202589 -> Sujeto_rol_alcance_capmin: sin mención
idx 26286: aplica_a Restriccion_cuentas_corrientes_y_especiales_en_el_bcra_y_ordenes_de_pago_a_cargo_del_bcra_ti_58b15f -> Sujeto_rol_alcance_capmin: sin mención
idx 26289: aplica_a Restriccion_de_haber_descalce_de_plazos_de_vencimiento_la_crc_que_tenga_un_plazo_de_vencimie_0b8aa7 -> Sujeto_rol_alcance_capmin: sin mención
idx 26291: aplica_a Restriccion_de_los_rubros_contables_de_ingresos_financieros_y_por_servicios_menos_egresos_y__3e2956 -> Sujeto_rol_alcance_capmin: sin mención
idx 26293: aplica_a Restriccion_de_otorgarse_la_asistencia_en_moneda_distinta_de_la_de_los_recursos_del_exterior_2cdec5 -> Sujeto_rol_alcance_capmin: sin mención
idx 26295: aplica_a Restriccion_debera_financiarse_hasta_la_fecha_estimada_de_embarque_de_los_bienes_en_origen_m_f8d7bc -> Sujeto_entidad_financiera: sin mención
idx 26303: aplica_a Restriccion_debera_rechazarse_la_registracion_de_los_cheques_de_pago_diferido_cuando_conteng_5204bd -> Sujeto_banco: sin mención
idx 26308: aplica_a Restriccion_debiendo_aplicar_como_maximo_en_este_caso_el_tipo_de_cambio_vendedor_de_la_entid_4ffed7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26311: aplica_a Restriccion_demas_exposiciones_a_entidades_financieras_ponderador_100__cap_2_12_4_2_68abf0 -> Sujeto_rol_alcance_capmin: sin mención
idx 26328: aplica_a Restriccion_el_acceso_al_mercado_de_cambios_por_parte_de_clientes_para_la_precancelacion_de__406d20 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26332: aplica_a Restriccion_el_activo_recibido_en_garantia_se_limitara_a_aquellos_listados_en_el_punto_5_3_1_ddaea1 -> Sujeto_rol_alcance_capmin: sin mención
idx 26349: aplica_a Restriccion_el_agente_local_no_ha_utilizado_este_mecanismo_por_un_monto_superior_al_equivale_b9a1ec -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26354: aplica_a Restriccion_el_ajuste_debe_reflejar_la_iliquidez_de_la_posicion__cap_6_10_2_1_dc2a85 -> Sujeto_rol_alcance_capmin: sin mención
idx 26358: aplica_a Restriccion_el_analisis_del_flujo_de_fondos_del_cliente_demuestra_que_es_altamente_improbabl_6e0fe0 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 26362: aplica_a Restriccion_el_cargo_que_el_sujeto_obligado_aplique_al_usuario_no_podra_ser_superior_al_que__c10204 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 26365: aplica_a Restriccion_el_cheque_es_rechazable_cuando_el_firmante_carece_de_poder_valido_o_vigente_al_m_5b4d1a -> Sujeto_banco: sin mención
idx 26369: aplica_a Restriccion_el_cliente_no_supere_en_el_mes_calendario_en_el_conjunto_de_las_entidades_y_por__d91325 -> Sujeto_persona_humana: sin mención
idx 26371: aplica_a Restriccion_el_cliente_no_tendra_acceso_al_mercado_de_cambios_para_pagar_el_equivalente_de_l_03fe48 -> Sujeto_cliente: sin mención
idx 26373: aplica_a Restriccion_el_computo_de_los_plazos_no_se_interrumpira_por_el_otorgamiento_de_renovaciones__0aa55a -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 26376: aplica_a Restriccion_el_computo_se_efectuara_neto_de_las_previsiones_por_riesgo_de_desvalorizacion__c_1f5ca7 -> Sujeto_rol_alcance_capmin: sin mención
idx 26378: aplica_a Restriccion_el_control_no_debe_quedar_exclusivamente_a_cargo_de_la_alta_gerencia__lingob_6_2_8d9345 -> Sujeto_entidad_financiera: sin mención
idx 26383: aplica_a Restriccion_el_descalce_de_plazos_de_vencimiento_entre_la_exposicion_y_el_activo_admitido_co_0d01f1 -> Sujeto_rol_alcance_capmin: sin mención
idx 26386: aplica_a Restriccion_el_desempeno_de_la_titulizacion_no_debera_depender_de_una_seleccion_de_los_subya_fb22a5 -> Sujeto_rol_alcance_capmin: sin mención
idx 26388: aplica_a Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_categoria_haya_refinanciado_su_d_9b4b78 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 26390: aplica_a Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_categoria_haya_refinanciado_su_d_ed4225 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 26392: aplica_a Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_categoria_haya_refinanciado_su_d_ee5f57 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 26394: aplica_a Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_categoria_haya_refinanciado_su_d_ef4a3f -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 26396: aplica_a Restriccion_el_diferimiento_no_debe_ser_menor_a_un_periodo_de_tres_anos_siempre_que_dicho_pe_e8288e -> Sujeto_entidad_financiera: sin mención
idx 26399: aplica_a Restriccion_el_endeudamiento_tenga_una_vida_promedio_no_inferior_a_los_2_dos_anos__ext_3_5_4_9f0dee -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26401: aplica_a Restriccion_el_endoso_que_no_contenga_las_especificaciones_establecidas_en_el_punto_5_1_4_no_a2fd7f -> Sujeto_banco: sin mención
idx 26408: aplica_a Restriccion_el_horizonte_temporal_de_riesgo_minimo_a_aplicar_a_dichas_exposiciones_sera_el_m_42d081 -> Sujeto_rol_alcance_capmin: sin mención
idx 26412: aplica_a Restriccion_el_importe_de_esta_rpc_que_sera_admisible_como_pnc_excluye_los_importes_reconoci_e6bf0e -> Sujeto_rol_alcance_capmin: sin mención
idx 26426: aplica_a Restriccion_el_importe_de_este_pnb_que_sera_admisible_como_ca_excluye_los_importes_reconocid_9dbcc3 -> Sujeto_rol_alcance_capmin: sin mención
idx 26435: aplica_a Restriccion_el_importe_de_los_cargos_que_el_sujeto_obligado_transfiera_a_los_usuarios_no_pod_4dfd16 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 26437: aplica_a Restriccion_el_importe_de_los_depositos_en_moneda_nacional_y_extranjera_no_podra_exceder_del_06fb84 -> Sujeto_rol_alcance_capmin: sin mención
idx 26441: aplica_a Restriccion_el_importe_resultante_de_aplicar_lo_dispuesto_en_la_seccion_2_debera_ser_multipl_730045 -> Sujeto_rol_alcance_capmin: sin mención
idx 26447: aplica_a Restriccion_el_importe_se_reducira_al_2_con_minimo_50_y_maximo_25_000_cuando_se_cancele_el_c_9afada -> Sujeto_banco: sin mención
idx 26456: aplica_a Restriccion_el_libramiento_de_cheques_de_pago_diferido_quedara_condicionado_a_la_existencia__7565f2 -> Sujeto_banco: sin mención
idx 26458: aplica_a Restriccion_el_monto_acumulado_de_aplicaciones_de_capital_e_intereses_emitidas_por_las_opera_4a780b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26483: aplica_a Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_en_nin_78f93f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26491: aplica_a Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_titulo_de_deuda_en_n_a98486 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26494: aplica_a Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_en_ningun_momento_superara_el__a91018 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26497: aplica_a Restriccion_el_monto_anual_aplicado_no_supere_el_equivalente_al_60_sesenta_por_ciento_del_mo_3abf98 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26503: aplica_a Restriccion_el_monto_aplicado_en_el_ano_calendario_no_supere_el_equivalente_al_25_veinticinc_764cff -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26505: aplica_a Restriccion_el_monto_aplicado_no_supere_el_20_veinte_por_ciento_del_monto_en_divisas_que_cor_7d7fc8 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26508: aplica_a Restriccion_el_monto_de_capital_por_el_cual_se_accedio_al_mercado_de_cambios_hasta_el_31_12__77b058 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26511: aplica_a Restriccion_el_monto_de_la_conversion_o_quita_debera_ser_como_minimo_aquel_que_le_permita_a__3ff518 -> Sujeto_rol_alcance_capmin: sin mención
idx 26515: aplica_a Restriccion_el_monto_de_la_transferencia_no_excedera_el_monto_percibido_por_jubilaciones_y_o_8fd11b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26518: aplica_a Restriccion_el_monto_de_las_certificaciones_obtenidas_para_el_periodo_trimestral_de_referenc_8c66af -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26521: aplica_a Restriccion_el_monto_de_los_pagos_y_otros_movimientos_registrados_con_imputacion_al_despacho_99368c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26524: aplica_a Restriccion_el_monto_de_suscripcion_de_bopreal_no_podra_exceder_el_equivalente_en_moneda_loc_691a1b -> Sujeto_cliente: sin mención
idx 26527: aplica_a Restriccion_el_monto_diario_de_acceso_no_supere_el_20_veinte_por_ciento_del_monto_previsto_e_5fa666 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26530: aplica_a Restriccion_el_monto_por_el_cual_se_utiliza_este_mecanismo_se_computa_a_los_efectos_de_los_l_c7a881 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26533: aplica_a Restriccion_el_monto_total_abonado_por_concepto_de_utilidades_y_dividendos_a_accionistas_no__24214c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26536: aplica_a Restriccion_el_monto_total_abonado_por_este_concepto_a_accionistas_no_residentes_incluido_el_19b1b2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26541: aplica_a Restriccion_el_monto_total_adeudado_a_la_fecha_de_cierre_del_mencionado_registro_no_superaba_fbc9b3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26545: aplica_a Restriccion_el_nuevo_titulo_de_deuda_contempla_1_un_ano_de_gracia_para_el_pago_de_capital_y__f838e2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26547: aplica_a Restriccion_el_pago_de_los_compromisos_de_una_titulizacion_no_debera_depender_de_la_venta_o__4cc7b3 -> Sujeto_rol_alcance_capmin: sin mención
idx 26556: aplica_a Restriccion_el_pago_no_se_realiza_con_anterioridad_a_la_fecha_de_vencimiento_de_la_obligacio_7adcba -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26560: aplica_a Restriccion_el_papel_a_utilizar_debe_cumplir_con_la_normativa_vigente_al_respecto__ctacte_3__f8795b -> Sujeto_banco: sin mención
idx 26563: aplica_a Restriccion_el_periodo_de_vigencia_del_derivado_de_credito_no_podra_ser_inferior_a_cualquier_2701bb -> Sujeto_rol_alcance_capmin: sin mención
idx 26597: aplica_a Restriccion_el_ponderador_de_riesgo_estara_basado_en_la_calificacion_especifica_de_la_emisio_3df249 -> Sujeto_rol_alcance_capmin: sin mención
idx 26599: aplica_a Restriccion_el_ponderador_de_riesgo_para_efectivo_en_caja_en_transito_cuando_la_entidad_fina_575684 -> Sujeto_rol_alcance_capmin: sin mención
idx 26602: aplica_a Restriccion_el_ponderador_de_riesgo_para_exposiciones_minoristas_normativas_no_transaccional_33d84f -> Sujeto_rol_alcance_capmin: sin mención
idx 26605: aplica_a Restriccion_el_ponderador_de_riesgo_para_operaciones_al_contado_a_liquidar_no_fallidas_es_0__503af2 -> Sujeto_rol_alcance_capmin: sin mención
idx 26611: aplica_a Restriccion_el_ponderador_resultante_estara_sujeto_a_un_minimo_de_100_para_retitulizaciones__c3e29c -> Sujeto_rol_alcance_capmin: sin mención
idx 26613: aplica_a Restriccion_el_ponderador_resultante_estara_sujeto_a_un_minimo_de_10_para_los_tramos_de_maxi_f4ca8c -> Sujeto_rol_alcance_capmin: sin mención
idx 26631: aplica_a Restriccion_el_ponderador_resultante_estara_sujeto_a_un_minimo_de_15_para_los_tramos_subordi_5aeb77 -> Sujeto_rol_alcance_capmin: sin mención
idx 26649: aplica_a Restriccion_el_ponderador_resultante_estara_sujeto_a_un_minimo_de_15_para_titulizaciones_que_eb2ba6 -> Sujeto_rol_alcance_capmin: sin mención
idx 26681: aplica_a Restriccion_el_premio_que_el_sujeto_obligado_reciba_del_usuario_no_podra_ser_superior_al_imp_9a1233 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 26687: aplica_a Restriccion_el_proceso_de_asignacion_debera_abarcar_todos_los_ponderadores_de_riesgo_previst_5f2e1a -> Sujeto_rol_alcance_capmin: sin mención
idx 26690: aplica_a Restriccion_el_proceso_de_asignacion_mapping_debera_ser_objetivo_y_ofrecer_una_distribucion__e52807 -> Sujeto_rol_alcance_capmin: sin mención
idx 26695: aplica_a Restriccion_el_rechazo_de_cheques_con_la_causal_de_la_suspension_del_servicio_de_pago_que_no_1c8122 -> Sujeto_banco: sin mención
idx 26702: aplica_a Restriccion_el_rechazo_de_un_cheque_de_pago_diferido_cuando_la_fecha_de_presentacion_al_cobr_8d94a2 -> Sujeto_banco: sin mención
idx 26707: aplica_a Restriccion_el_reconocimiento_como_rpc_se_limitara_al_90_del_valor_obtenido_mediante_la_apli_128a3d -> Sujeto_rol_alcance_capmin: sin mención
idx 26710: aplica_a Restriccion_el_repago_de_las_financiaciones_no_debera_depender_significativamente_del_flujo__09446d -> Sujeto_rol_alcance_capmin: sin mención
idx 26713: aplica_a Restriccion_el_requerimiento_de_capital_sera_el_15_de_la_posicion_neta_ya_sea_corta_o_larga__08eb97 -> Sujeto_rol_alcance_capmin: sin mención
idx 26716: aplica_a Restriccion_el_requisito_de_capitales_minimos_que_se_determine_para_los_instrumentos_origina_48c5d8 -> Sujeto_rol_alcance_capmin: sin mención
idx 26718: aplica_a Restriccion_el_seguimiento_de_las_negociaciones_de_divisas_no_es_exigible_para_operaciones_q_074d6a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26720: aplica_a Restriccion_el_titulo_no_podra_estar_redactado_en_idioma_que_no_sea_el_idioma_nacional__ctac_a2b06b -> Sujeto_banco: sin mención
idx 26723: aplica_a Restriccion_el_titulo_que_carezca_de_identificacion_tributaria_laboral_o_de_identidad_del_li_bc3e82 -> Sujeto_banco: sin mención
idx 26726: aplica_a Restriccion_el_titulo_que_carezca_del_domicilio_del_librador_no_vale_como_cheque__ctacte_3_2_533419 -> Sujeto_banco: sin mención
idx 26729: aplica_a Restriccion_el_titulo_que_carezca_del_nombre_del_librador_no_vale_como_cheque__ctacte_3_2_1__af9dc4 -> Sujeto_banco: sin mención
idx 26732: aplica_a Restriccion_el_titulo_respecto_del_que_falta_la_orden_pura_y_simple_de_pagar_una_suma_determ_bd5651 -> Sujeto_banco: sin mención
idx 26735: aplica_a Restriccion_el_titulo_respecto_del_que_falte_la_especificacion_de_la_fecha_de_pago_segun_art_a9876c -> Sujeto_banco: sin mención
idx 26738: aplica_a Restriccion_el_titulo_respecto_del_que_se_presentare_alguna_de_las_siguientes_situaciones_en_bd02b7 -> Sujeto_banco: sin mención
idx 26741: aplica_a Restriccion_el_titulo_respecto_del_que_se_presentare_alguna_de_las_siguientes_situaciones_en_f0528b -> Sujeto_banco: sin mención
idx 26744: aplica_a Restriccion_el_titulo_respecto_del_que_se_presente_alguna_de_las_situaciones_enumeradas_incl_7a7021 -> Sujeto_banco: sin mención
idx 26747: aplica_a Restriccion_el_total_de_los_vencimientos_por_las_cuotas_de_todas_las_financiaciones_de_la_en_71533e -> Sujeto_rol_alcance_capmin: sin mención
idx 26751: aplica_a Restriccion_el_tratamiento_otorgado_a_la_exposicion_al_sector_publico_no_financiero_no_sera__165fb3 -> Sujeto_rol_alcance_capmin: sin mención
idx 26754: aplica_a Restriccion_el_tratamiento_que_se_dispense_en_el_marco_de_la_emergencia_agropecuaria_no_podr_fea2c2 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 26756: aplica_a Restriccion_el_valor_acumulado_pendiente_de_liquidacion_adeudado_al_exportador_por_el_no_res_5b56d3 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26853: aplica_a Restriccion_el_valor_maximo_de_n_es_3_no_admitiendose_la_superposicion_de_meses_en_la_confor_befff6 -> Sujeto_rol_alcance_capmin: sin mención
idx 26857: aplica_a Restriccion_ello_no_puede_implicar_costo_alguno_para_el_presentante_y_o_cuentacorrentista__c_adbb9c -> Sujeto_banco: sin mención
idx 26859: aplica_a Restriccion_en_caso_de_fallecimiento_o_incapacidad_de_algunos_titulares_se_requerira_orden_j_72aa90 -> Sujeto_banco: sin mención
idx 26861: aplica_a Restriccion_en_caso_de_que_el_cliente_sea_beneficiario_directo_del_decreto_277_22_la_aplicac_9830dc -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26866: aplica_a Restriccion_en_caso_de_que_se_trate_de_un_cheque_librado_en_formato_papel_y_se_hubiera_gesti_ae4936 -> Sujeto_banco: sin mención
idx 26874: aplica_a Restriccion_en_el_caso_de_la_republica_federativa_del_brasil_las_operaciones_comerciales_no__c6526e -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26876: aplica_a Restriccion_en_el_caso_de_los_activos_listados_en_los_acapites_iii_iv_y_vi_sera_condicion_qu_0541c7 -> Sujeto_rol_alcance_capmin: sin mención
idx 26878: aplica_a Restriccion_en_el_caso_de_precancelacion_total_no_se_admitira_la_aplicacion_de_comisiones_cu_6bb1ee -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 26887: aplica_a Restriccion_en_la_medida_que_el_monto_a_imputar_al_permiso_por_este_mecanismo_supere_el_equi_fb62ca -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26889: aplica_a Restriccion_en_la_medida_que_los_fondos_no_sean_debitados_de_una_cuenta_en_moneda_extranjera_354c6d -> Sujeto_persona_humana: sin mención
idx 26890: aplica_a Restriccion_en_la_medida_que_los_fondos_no_sean_debitados_de_una_cuenta_en_moneda_extranjera_354c6d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26903: aplica_a Restriccion_en_las_operaciones_de_compraventa_con_titulos_valores_los_titulos_valores_deben__64a225 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26906: aplica_a Restriccion_en_los_contratos_de_tarjeta_de_credito_el_consentimiento_a_modificaciones_en_las_996684 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 26911: aplica_a Restriccion_en_ningun_caso_la_capitalizacion_de_deuda_podra_implicar_una_limitacion_o_suspen_dd3b99 -> Sujeto_rol_alcance_capmin: sin mención
idx 26913: aplica_a Restriccion_en_ningun_caso_podran_aplicarse_comisiones_y_o_cargos_al_usuario_aun_cuando_habi_c86b19 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 26916: aplica_a Restriccion_en_ningun_caso_podran_aplicarse_comisiones_y_o_cargos_al_usuario_por_servicios_f_5471e5 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 26919: aplica_a Restriccion_en_ningun_caso_se_permite_la_liquidacion_de_estas_operaciones_mediante_el_pago_e_5f9513 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26923: aplica_a Restriccion_en_tal_caso_cuando_se_utilizan_calculos_de_terceros_el_ponderador_a_aplicar_sera_f6ede7 -> Sujeto_rol_alcance_capmin: sin mención
idx 26926: aplica_a Restriccion_en_todos_los_casos_se_utilizara_un_mpor_minimo_de_10_dias_para_el_calculo_de_las_e168be -> Sujeto_rol_alcance_capmin: sin mención
idx 26941: aplica_a Restriccion_entidades_financieras_exigencia_de_capital_por_riesgo_especifico_8__cap_6_2_1_1_31b55e -> Sujeto_entidad_financiera: sin mención
idx 26944: aplica_a Restriccion_entre_16_y_30_dias_habiles_posteriores_a_la_fecha_de_liquidacion_la_exigencia_de_5e654e -> Sujeto_rol_alcance_capmin: sin mención
idx 26947: aplica_a Restriccion_entre_31_y_45_dias_habiles_posteriores_a_la_fecha_de_liquidacion_la_exigencia_de_f6338a -> Sujeto_rol_alcance_capmin: sin mención
idx 26950: aplica_a Restriccion_entre_5_y_15_dias_habiles_posteriores_a_la_fecha_de_liquidacion_la_exigencia_de__f8d19f -> Sujeto_rol_alcance_capmin: sin mención
idx 26956: aplica_a Restriccion_esta_declaracion_debera_ser_firmada_por_el_importador_o_quien_ejerza_su_represen_3d3ed2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26958: aplica_a Restriccion_esta_delegacion_sera_valida_solo_a_los_efectos_operativos_del_presente_regimen_s_affbac -> Sujeto_rol_alcance_pagjub: sin mención
idx 26968: aplica_a Restriccion_esta_limitacion_tambien_alcanza_en_las_casas_operativas_distintas_a_aquella_en_l_b94949 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 26971: aplica_a Restriccion_esta_opcion_estara_disponible_hasta_alcanzar_el_125_ciento_veinticinco_por_cient_7404d2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26974: aplica_a Restriccion_esta_opcion_estara_disponible_hasta_alcanzar_el_125_ciento_veinticinco_por_cient_be15ce -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 26979: aplica_a Restriccion_establezcan_la_inversion_de_la_carga_de_la_prueba_en_perjuicio_del_usuario_de_se_de7005 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 26981: aplica_a Restriccion_estan_sujetas_a_limites_que_se_supervisan_para_comprobar_su_adecuacion__cap_6_9__f8f9bb -> Sujeto_rol_alcance_capmin: sin mención
idx 26984: aplica_a Restriccion_este_limite_se_aplicara_por_separado_a_cada_instrumento_ya_sea_que_se_compute_en_332cab -> Sujeto_rol_alcance_capmin: sin mención
idx 26987: aplica_a Restriccion_este_mecanismo_no_podra_ser_utilizado_por_los_aumentos_de_exportaciones_de_biene_a125e7 -> Sujeto_beneficiario_economia_conocimiento: sin mención
idx 26990: aplica_a Restriccion_estos_gastos_no_podran_ser_trasladados_al_cuentacorrentista_salvo_que_el_pedido__4aef04 -> Sujeto_banco: sin mención
idx 26992: aplica_a Restriccion_evitar_la_realizacion_de_actividades_a_traves_de_estructuras_societarias_o_juris_eddb46 -> Sujeto_entidad_financiera: sin mención
idx 26995: aplica_a Restriccion_exhibidos_bajo_el_nombre_contratos_de_adhesion_ley_24_240_de_defensa_del_consumi_615f3a -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 26997: aplica_a Restriccion_exigencia_de_capital_por_riesgo_general_de_mercado_de_la_que_se_pueden_excluir_p_4f01b6 -> Sujeto_rol_alcance_capmin: sin mención
idx 26999: aplica_a Restriccion_exposiciones_a_deuda_subordinada_ponderador_de_riesgo_del_150__cap_2_12_10_2_533e48 -> Sujeto_rol_alcance_capmin: sin mención
idx 27002: aplica_a Restriccion_exposiciones_a_participaciones_en_el_capital_ponderador_de_riesgo_del_250__cap_2_47d84b -> Sujeto_rol_alcance_capmin: sin mención
idx 27005: aplica_a Restriccion_exposiciones_a_personas_humanas_y_juridicas_originadas_por_compras_en_cuotas_efe_60fc0e -> Sujeto_rol_alcance_capmin: sin mención
idx 27008: aplica_a Restriccion_exposiciones_con_garantia_hipotecaria_normativas_sobre_inmuebles_residenciales_e_e342f3 -> Sujeto_rol_alcance_capmin: sin mención
idx 27010: aplica_a Restriccion_exposiciones_de_corto_plazo_a_entidades_financieras_ponderador_20__cap_2_12_4_2_82fda2 -> Sujeto_rol_alcance_capmin: sin mención
idx 27013: aplica_a Restriccion_exposiciones_garantizadas_por_sociedades_de_garantia_reciproca_o_fondos_de_garan_d4d43a -> Sujeto_rol_alcance_capmin: sin mención
idx 27016: aplica_a Restriccion_exposiciones_o_tramos_no_cubiertos_por_coberturas_del_riesgo_de_credito_de_la_se_1a5e8f -> Sujeto_rol_alcance_capmin: sin mención
idx 27025: aplica_a Restriccion_exposiciones_o_tramos_no_cubiertos_por_coberturas_del_riesgo_de_credito_de_la_se_99244d -> Sujeto_rol_alcance_capmin: sin mención
idx 27034: aplica_a Restriccion_exposiciones_o_tramos_no_cubiertos_por_coberturas_del_riesgo_de_credito_de_la_se_fc8cca -> Sujeto_rol_alcance_capmin: sin mención
idx 27043: aplica_a Restriccion_falta_de_alguna_de_las_especificaciones_contenidas_en_los_articulos_2_incisos_1__f9f9ec -> Sujeto_banco: sin mención
idx 27046: aplica_a Restriccion_falta_de_conformidad_en_la_recepcion_de_cuadernos_de_cheques__ctacte_6_1_2_6_793a1a -> Sujeto_banco: sin mención
idx 27056: aplica_a Restriccion_falta_de_firmas_adicionales_a_la_o_las_existentes_cuando_se_requiera_la_firma_de_58d4ac -> Sujeto_banco: sin mención
idx 27059: aplica_a Restriccion_firmante_incluido_en_la_central_de_cuentacorrentistas_inhabilitados_al_momento_d_a71c7f -> Sujeto_banco: sin mención
idx 27062: aplica_a Restriccion_habiendose_presentado_se_encuentra_incompleta__pagjub_2_7_1_fb79f8 -> Sujeto_rol_alcance_pagjub: sin mención
idx 27065: aplica_a Restriccion_hasta_el_importe_equivalente_al_55_del_valor_del_inmueble_se_aplicara_el_pondera_7e2fb0 -> Sujeto_rol_alcance_capmin: sin mención
idx 27070: aplica_a Restriccion_impedimento_para_instalacion_de_oficinas_de_representacion_en_el_exterior_except_aa642c -> Sujeto_rol_alcance_capmin: sin mención
idx 27073: aplica_a Restriccion_impedimento_para_instalacion_de_sucursales_en_el_exterior__cap_1_4_2_1_2a358b -> Sujeto_rol_alcance_capmin: sin mención
idx 27076: aplica_a Restriccion_impedimento_para_participacion_en_entidades_financieras_del_exterior__cap_1_4_2__f65b21 -> Sujeto_rol_alcance_capmin: sin mención
idx 27079: aplica_a Restriccion_impedimento_para_transformacion_de_entidades_financieras__cap_1_4_2_1_9f7ea0 -> Sujeto_rol_alcance_capmin: sin mención
idx 27082: aplica_a Restriccion_impedir_el_uso_de_echeq_por_personas_o_en_condiciones_no_autorizadas__ctacte_1_5_aab9ce -> Sujeto_banco: sin mención
idx 27085: aplica_a Restriccion_impedir_el_uso_de_elementos_de_seguridad_de_echeq_por_personas_o_en_condiciones__68b72a -> Sujeto_banco: sin mención
idx 27088: aplica_a Restriccion_importes_adeudados_al_usuario_por_haber_liquidado_en_forma_incorrecta_promocione_dbe2da -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 27091: aplica_a Restriccion_importes_en_exceso_de_lo_oportunamente_pactado_entre_el_usuario_y_el_sujeto_obli_5461b0 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 27094: aplica_a Restriccion_incumplimiento_al_nivel_de_la_tasa_de_interes_maxima_aplicable_a_financiaciones__d6342f -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 27097: aplica_a Restriccion_independientemente_de_la_cartera_a_la_que_esten_asignados_los_activos_constituid_00e072 -> Sujeto_rol_alcance_capmin: sin mención
idx 27123: aplica_a Restriccion_independientemente_de_que_esten_registradas_en_la_cartera_de_negociacion_o_en_la_371993 -> Sujeto_rol_alcance_capmin: sin mención
idx 27125: aplica_a Restriccion_inmuebles_cuya_registracion_contable_no_se_encuentre_respaldada_con_la_pertinent_4e25c6 -> Sujeto_rol_alcance_capmin: sin mención
idx 27128: aplica_a Restriccion_instrumentos_con_oferta_publica_autorizada_emitidos_por_empresas_y_otras_persona_9cb1c7 -> Sujeto_aseguradora: sin mención
idx 27129: aplica_a Restriccion_instrumentos_con_oferta_publica_autorizada_emitidos_por_empresas_y_otras_persona_9cb1c7 -> Sujeto_entidad_cambiaria: sin mención
idx 27130: aplica_a Restriccion_instrumentos_con_oferta_publica_autorizada_emitidos_por_empresas_y_otras_persona_9cb1c7 -> Sujeto_fiduciario_de_fideicomiso_financiero: sin mención
idx 27133: aplica_a Restriccion_instrumentos_de_deuda_en_moneda_extranjera_del_tesoro_nacional_por_hasta_el_impo_4cd74c -> Sujeto_entidad_financiera: sin mención
idx 27149: aplica_a Restriccion_la_acumulacion_de_fondos_estara_disponible_hasta_alcanzar_el_125_ciento_veintici_446d5b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27152: aplica_a Restriccion_la_aplicacion_de_la_capacidad_de_prestamo_de_depositos_en_moneda_extranjera_a_lo_44dd70 -> Sujeto_entidad_financiera: sin mención
idx 27155: aplica_a Restriccion_la_aplicacion_de_las_divisas_al_capital_intereses_y_otros_conceptos_permitidos_s_1e4a40 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27158: aplica_a Restriccion_la_aplicacion_de_las_divisas_solo_podra_ser_convalidada_por_la_entidad_encargada_2e94e2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27161: aplica_a Restriccion_la_aplicacion_del_tratamiento_de_emergencia_agropecuaria_no_podra_extenderse_mas_1ee0a5 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 27163: aplica_a Restriccion_la_aplicacion_estara_sujeta_al_cumplimiento_de_los_requisitos_establecidos_en_lo_3a39e3 -> Sujeto_rol_alcance_capmin: sin mención
idx 27165: aplica_a Restriccion_la_ausencia_de_cualquiera_de_esos_requisitos_hara_responsable_a_la_entidad_por_l_c6a090 -> Sujeto_banco: sin mención
idx 27167: aplica_a Restriccion_la_ausencia_de_cualquiera_de_los_requisitos_establecidos_hara_responsable_a_la_e_40f58f -> Sujeto_banco: sin mención
idx 27169: aplica_a Restriccion_la_cancelacion_de_dividendos_o_intereses_no_debe_imponer_restricciones_a_la_enti_de417e -> Sujeto_rol_alcance_capmin: sin mención
idx 27171: aplica_a Restriccion_la_cancelacion_de_giros_en_descubierto_en_cuentas_corrientes_en_dolares_estadoun_bbf2c0 -> Sujeto_cliente: sin mención
idx 27174: aplica_a Restriccion_la_cancelacion_de_las_lineas_destinadas_a_la_financiacion_de_operaciones_de_impo_521182 -> Sujeto_entidad_financiera: sin mención
idx 27189: aplica_a Restriccion_la_cantidad_total_de_casos_y_montos_consignados_en_la_declaracion_jurada_difiere_133545 -> Sujeto_rol_alcance_pagjub: sin mención
idx 27197: aplica_a Restriccion_la_declaracion_jurada_debera_ser_firmada_por_el_importador_o_quien_ejerza_su_rep_dcfe50 -> Sujeto_importador: sin mención
idx 27204: aplica_a Restriccion_la_devolucion_sin_registrar_no_debera_informarse_al_banco_central_de_la_republic_0364ee -> Sujeto_banco: sin mención
idx 27206: aplica_a Restriccion_la_duracion_no_podra_exceder_los_30_dias_corridos_desde_la_fecha_de_la_eleccion__470ff1 -> Sujeto_banco: sin mención
idx 27215: aplica_a Restriccion_la_entidad_financiera_emisora_de_la_tarjeta_de_debito_no_podra_percibir_de_sus_c_8469ab -> Sujeto_entidad_financiera: sin mención
idx 27218: aplica_a Restriccion_la_entidad_financiera_no_debera_tener_la_expectativa_ni_crearla_en_el_mercado_de_9fc7a9 -> Sujeto_rol_alcance_capmin: sin mención
idx 27221: aplica_a Restriccion_la_entidad_financiera_originante_no_podra_excluir_las_exposiciones_objeto_de_tit_000adb -> Sujeto_rol_alcance_capmin: sin mención
idx 27250: aplica_a Restriccion_la_entidad_financiera_originante_no_podra_reconocer_el_empleo_de_tecnicas_de_crc_2390bd -> Sujeto_rol_alcance_capmin: sin mención
idx 27278: aplica_a Restriccion_la_entidad_financiera_podra_mantener_inversiones_en_instrumentos_computables_com_56be97 -> Sujeto_rol_alcance_capmin: sin mención
idx 27281: aplica_a Restriccion_la_entidad_financiera_y_los_funcionarios_seran_pasibles_de_las_sanciones_previst_d9cd16 -> Sujeto_rol_alcance_pagjub: sin mención
idx 27283: aplica_a Restriccion_la_entidad_no_podra_presentar_una_declaracion_jurada_con_datos_falsos__pagjub_2__3974e9 -> Sujeto_rol_alcance_pagjub: sin mención
idx 27286: aplica_a Restriccion_la_entidad_podra_considerar_cumplimentado_el_seguimiento_de_un_permiso_de_embarq_25e495 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27288: aplica_a Restriccion_la_entidad_rechazara_cheques_cuando_falten_fondos_disponibles_suficientes_acredi_17727c -> Sujeto_banco: sin mención
idx 27290: aplica_a Restriccion_la_evaluacion_debe_ser_conducida_en_forma_independiente_de_la_alta_gerencia_de_l_fa2877 -> Sujeto_entidad_financiera: sin mención
idx 27292: aplica_a Restriccion_la_exigencia_de_capital_minimo_por_riesgo_operacional_no_podra_superar_el_20_del_d7aaa2 -> Sujeto_rol_alcance_capmin: sin mención
idx 27298: aplica_a Restriccion_la_exigencia_de_capital_por_commodities_se_aplicara_a_la_posicion_total_en_cada__703eb7 -> Sujeto_rol_alcance_capmin: sin mención
idx 27301: aplica_a Restriccion_la_exigencia_de_capital_por_el_riesgo_general_de_mercado_alcanza_a_todas_las_pos_c0d6f0 -> Sujeto_rol_alcance_capmin: sin mención
idx 27303: aplica_a Restriccion_la_exigencia_de_capital_por_las_posiciones_de_titulizacion_retenidas_o_recomprad_645f26 -> Sujeto_rol_alcance_capmin: sin mención
idx 27305: aplica_a Restriccion_la_exigencia_de_capital_por_riesgo_de_tipo_de_cambio_se_aplicara_a_la_posicion_t_0f7b60 -> Sujeto_rol_alcance_capmin: sin mención
idx 27308: aplica_a Restriccion_la_exigencia_de_capital_por_riesgo_especifico_de_las_posiciones_de_titulizacion__608885 -> Sujeto_rol_alcance_capmin: sin mención
idx 27314: aplica_a Restriccion_la_exigencia_de_capital_por_riesgo_especifico_sera_del_8_de_la_posicion_bruta_en_3c3c77 -> Sujeto_rol_alcance_capmin: sin mención
idx 27317: aplica_a Restriccion_la_exigencia_de_capital_por_riesgo_general_de_mercado_sera_del_8_de_la_posicion__46c566 -> Sujeto_rol_alcance_capmin: sin mención
idx 27320: aplica_a Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_2_del_gr_228a07 -> Sujeto_rol_alcance_capmin: sin mención
idx 27331: aplica_a Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_2_del_gr_71936f -> Sujeto_rol_alcance_capmin: sin mención
idx 27342: aplica_a Restriccion_la_exigencia_de_capital_por_titulos_valores_se_computara_respecto_de_los_instrum_4c97d5 -> Sujeto_rol_alcance_capmin: sin mención
idx 27345: aplica_a Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en__6c2af3 -> Sujeto_rol_alcance_capmin: sin mención
idx 27357: aplica_a Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en__bec264 -> Sujeto_rol_alcance_capmin: sin mención
idx 27365: aplica_a Restriccion_la_exportacion_a_consumo_de_bienes_excluidos_del_regimen_de_equipaje_esta_except_414a4b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27368: aplica_a Restriccion_la_exposicion_debera_estar_garantizada_por_un_inmueble_terminado__cap_2_9_2_2_38507e -> Sujeto_rol_alcance_capmin: sin mención
idx 27371: aplica_a Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar_38cff3 -> Sujeto_persona_humana: sin mención
idx 27372: aplica_a Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar_38cff3 -> Sujeto_rol_alcance_capmin: sin mención
idx 27375: aplica_a Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar_e1f0ef -> Sujeto_mipyme: sin mención
idx 27376: aplica_a Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar_e1f0ef -> Sujeto_persona_humana: sin mención
idx 27377: aplica_a Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar_e1f0ef -> Sujeto_rol_alcance_capmin: sin mención
idx 27380: aplica_a Restriccion_la_exposicion_total_con_cada_contraparte_individual_unico_beneficiario_o_conjunt_0bf7eb -> Sujeto_rol_alcance_capmin: sin mención
idx 27388: aplica_a Restriccion_la_falta_de_cumplimiento_de_cualquiera_de_los_limites_minimos_sera_considerada_i_b603ec -> Sujeto_rol_alcance_capmin: sin mención
idx 27391: aplica_a Restriccion_la_falta_de_inclusion_en_los_documentos_de_la_tasa_de_interes_y_o_del_costo_fina_84d2da -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 27393: aplica_a Restriccion_la_falta_del_numero_de_orden_impreso_en_el_cuerpo_del_cheque_librado_en_formato__d6b6e1 -> Sujeto_banco: sin mención
idx 27399: aplica_a Restriccion_la_figura_de_incumplido_en_gestion_de_cobro_no_podra_ser_aplicada_por_la_entidad_58a090 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27401: aplica_a Restriccion_la_garantia_constituida_por_el_miembro_compensador_incluyendo_efectivo_titulos_v_767d79 -> Sujeto_miembro_compensador: sin mención
idx 27403: aplica_a Restriccion_la_garantia_constituida_por_un_cliente_mantenida_por_un_custodio_y_protegida_de__744c49 -> Sujeto_cliente: sin mención
idx 27406: aplica_a Restriccion_la_informacion_se_referira_a_posiciones_en_pesos_cuadros_11_2_1_a_y_11_2_2_a_y_e_646156 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 27414: aplica_a Restriccion_la_intervencion_de_terceros_no_releva_a_la_entidad_de_su_responsabilidad_por_la__b7c8a0 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 27416: aplica_a Restriccion_la_inversion_en_el_fondo_debera_ponderarse_al_1250_cuando_no_se_pueda_recurrir_n_eeea6f -> Sujeto_rol_alcance_capmin: sin mención
idx 27419: aplica_a Restriccion_la_mencionada_venta_no_habilitara_al_cliente_a_concretar_las_operaciones_de_titu_e5cd96 -> Sujeto_cliente: sin mención
idx 27429: aplica_a Restriccion_la_modificacion_no_debe_alterar_el_objeto_del_contrato_ni_importar_un_desmedro_r_20b3d2 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 27444: aplica_a Restriccion_la_parte_de_la_exposicion_cubierta_recibira_el_ponderador_de_riesgo_correspondie_0ab4b9 -> Sujeto_rol_alcance_capmin: sin mención
idx 27448: aplica_a Restriccion_la_porcion_de_los_endeudamientos_financieros_que_sea_utilizada_en_virtud_de_lo_d_078eef -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27451: aplica_a Restriccion_la_porcion_del_endeudamiento_financiero_que_sea_utilizada_en_virtud_de_lo_dispue_7c14de -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27454: aplica_a Restriccion_la_posibilidad_de_autorizar_giros_en_descubierto_estara_sujeta_a_las_normas_vige_c647ef -> Sujeto_banco: sin mención
idx 27463: aplica_a Restriccion_la_revision_debera_alcanzar_como_minimo_el_20_de_la_cartera_activa_total__cla_3__f070fe -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 27471: aplica_a Restriccion_la_suma_de_los_pagos_anticipados_a_la_vista_y_de_deuda_comercial_sin_registro_de_204c50 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27474: aplica_a Restriccion_la_suma_de_los_pagos_anticipados_cursados_en_el_marco_de_este_punto_no_supera_el_7579e6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27481: aplica_a Restriccion_la_tasacion_no_dependa_de_la_situacion_economica_del_prestatario__cap_2_9_2_3_264424 -> Sujeto_rol_alcance_capmin: sin mención
idx 27483: aplica_a Restriccion_la_tasacion_no_resulte_mayor_al_precio_de_mercado__cap_2_9_2_3_db61d6 -> Sujeto_rol_alcance_capmin: sin mención
idx 27485: aplica_a Restriccion_la_tasacion_no_se_base_en_la_expectativa_de_que_se_incrementara_el_precio_del_in_1b6835 -> Sujeto_rol_alcance_capmin: sin mención
idx 27487: aplica_a Restriccion_la_tasacion_no_sea_mayor_al_precio_de_adquisicion_en_los_casos_en_que_el_prestam_61fcb8 -> Sujeto_rol_alcance_capmin: sin mención
idx 27492: aplica_a Restriccion_la_titulizacion_no_debe_ser_estructurada_como_una_cascada_inversa_de_modo_que_lo_180778 -> Sujeto_rol_alcance_capmin: sin mención
idx 27494: aplica_a Restriccion_la_verificacion_independiente_de_los_precios_requiere_de_un_mayor_grado_de_preci_c0d2bf -> Sujeto_rol_alcance_capmin: sin mención
idx 27506: aplica_a Restriccion_las_casas_y_agencias_de_cambio_no_podran_incrementar_sin_conformidad_previa_del__cde4a8 -> Sujeto_agencia_de_cambio: sin mención
idx 27507: aplica_a Restriccion_las_casas_y_agencias_de_cambio_no_podran_incrementar_sin_conformidad_previa_del__cde4a8 -> Sujeto_casa_de_cambio: sin mención
idx 27510: aplica_a Restriccion_las_certificaciones_solo_podran_emitirse_en_la_medida_que_la_entidad_tenga_const_7c0109 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27513: aplica_a Restriccion_las_clausulas_que_por_su_contenido_redaccion_o_presentacion_no_sea_razonable_esp_66c33c -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 27515: aplica_a Restriccion_las_coberturas_que_no_se_realicen_a_traves_de_derivados_solo_seran_admisibles_si_43c5eb -> Sujeto_rol_alcance_capmin: sin mención
idx 27517: aplica_a Restriccion_las_comisiones_y_cargos_aplicados_a_los_usuarios_de_servicios_financieros_se_aju_a3c145 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 27519: aplica_a Restriccion_las_compensaciones_en_la_zona_2_bandas_1_2_2_3_3_4_4_5_5_7_7_10_anos_estan_sujet_28217a -> Sujeto_rol_alcance_capmin: sin mención
idx 27522: aplica_a Restriccion_las_compensaciones_en_la_zona_3_bandas_10_15_15_20_mas_de_20_anos_estan_sujetas__90136a -> Sujeto_rol_alcance_capmin: sin mención
idx 27525: aplica_a Restriccion_las_compensaciones_entre_posiciones_dentro_de_la_zona_1_bandas_0_1_1_3_3_6_6_12__2e4250 -> Sujeto_rol_alcance_capmin: sin mención
idx 27528: aplica_a Restriccion_las_condiciones_del_manual_deberan_basarse_en_criterios_objetivos_no_pudiendo_fi_2a950c -> Sujeto_banco: sin mención
idx 27530: aplica_a Restriccion_las_contrapartes_individuales_cuyo_saldo_de_exposiciones_computables_a_fin_del_m_ce9e9e -> Sujeto_rol_alcance_capmin: sin mención
idx 27533: aplica_a Restriccion_las_cuotas_de_todas_las_financiaciones_de_la_entidad_que_cuenten_con_sistema_de__ee2d9d -> Sujeto_rol_alcance_capmin: sin mención
idx 27536: aplica_a Restriccion_las_demas_posiciones_de_titulizacion_registradas_en_partidas_fuera_de_balance_re_e52d9b -> Sujeto_rol_alcance_capmin: sin mención
idx 27539: aplica_a Restriccion_las_entidades_deben_mantener_exigencia_de_capital_por_el_riesgo_de_mantener_posi_ecf934 -> Sujeto_rol_alcance_capmin: sin mención
idx 27542: aplica_a Restriccion_las_entidades_financieras_deberan_aplicar_un_ponderador_de_riesgo_del_1250_a_sus_6d7858 -> Sujeto_rol_alcance_capmin: sin mención
idx 27545: aplica_a Restriccion_las_entidades_financieras_no_podran_hacer_uso_de_las_tecnicas_de_coberturas_del__a4b419 -> Sujeto_rol_alcance_capmin: sin mención
idx 27548: aplica_a Restriccion_las_entidades_financieras_no_podran_registrar_tenencias_de_instrumentos_tlac_emi_275986 -> Sujeto_entidad_financiera: sin mención
idx 27551: aplica_a Restriccion_las_entidades_financieras_no_podran_tener_ningun_tipo_de_participacion_ni_vincul_36ddec -> Sujeto_entidad_financiera: sin mención
idx 27554: aplica_a Restriccion_las_entidades_financieras_pagadoras_no_deberan_deducir_del_importe_neto_que_corr_87753f -> Sujeto_rol_alcance_pagjub: sin mención
idx 27557: aplica_a Restriccion_las_entidades_financieras_que_pertenezcan_al_grupo_a_no_podran_otorgar_directa_o_730866 -> Sujeto_banco: sin mención
idx 27566: aplica_a Restriccion_las_entidades_financieras_solo_podran_acordar_y_desembolsar_nuevas_financiacione_f9411c -> Sujeto_entidad_financiera: sin mención
idx 27569: aplica_a Restriccion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_d1ce15 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 27570: aplica_a Restriccion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_d1ce15 -> Sujeto_entidad_financiera: sin mención
idx 27573: aplica_a Restriccion_las_entidades_financieras_y_los_proveedores_no_financieros_de_credito_no_deberan_3551e2 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 27574: aplica_a Restriccion_las_entidades_financieras_y_los_proveedores_no_financieros_de_credito_no_deberan_3551e2 -> Sujeto_entidad_financiera: sin mención
idx 27575: aplica_a Restriccion_las_entidades_financieras_y_los_proveedores_no_financieros_de_credito_no_deberan_3551e2 -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 27578: aplica_a Restriccion_las_entidades_financieras_y_los_proveedores_no_financieros_de_credito_no_deberan_a33409 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 27579: aplica_a Restriccion_las_entidades_financieras_y_los_proveedores_no_financieros_de_credito_no_deberan_a33409 -> Sujeto_entidad_financiera: sin mención
idx 27580: aplica_a Restriccion_las_entidades_financieras_y_los_proveedores_no_financieros_de_credito_no_deberan_a33409 -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 27583: aplica_a Restriccion_las_entidades_financieras_y_los_proveedores_no_financieros_de_credito_no_deberan_b3fbc7 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 27584: aplica_a Restriccion_las_entidades_financieras_y_los_proveedores_no_financieros_de_credito_no_deberan_b3fbc7 -> Sujeto_entidad_financiera: sin mención
idx 27585: aplica_a Restriccion_las_entidades_financieras_y_los_proveedores_no_financieros_de_credito_no_deberan_b3fbc7 -> Sujeto_proveedor_no_financiero_de_credito: sin mención
idx 27588: aplica_a Restriccion_las_entidades_giradas_o_depositarias_no_podran_recibir_cheques_de_pago_diferido__6ba4be -> Sujeto_entidad_depositaria: sin mención
idx 27589: aplica_a Restriccion_las_entidades_giradas_o_depositarias_no_podran_recibir_cheques_de_pago_diferido__6ba4be -> Sujeto_entidad_girada: sin mención
idx 27592: aplica_a Restriccion_las_entidades_no_podran_cambiar_arbitrariamente_de_ecai__cap_10_3_1_3_c9dee6 -> Sujeto_rol_alcance_capmin: sin mención
idx 27595: aplica_a Restriccion_las_entidades_no_podran_cobrar_cargos_ni_comisiones_por_los_reemplazos_de_tarjet_d3fe44 -> Sujeto_banco: sin mención
idx 27617: aplica_a Restriccion_las_entidades_no_podran_cobrar_comisiones_por_reportar_circunstancias_que_impliq_33df5f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27620: aplica_a Restriccion_las_entidades_no_podran_cobrar_comisiones_por_reportar_circunstancias_que_impliq_b3bb20 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27623: aplica_a Restriccion_las_entidades_no_podran_comprar_titulos_valores_en_el_mercado_secundario_con_liq_d0a0c9 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27626: aplica_a Restriccion_las_entidades_no_podran_escoger_la_mejor_de_las_evaluaciones_proporcionadas_por__d57e1f -> Sujeto_rol_alcance_capmin: sin mención
idx 27629: aplica_a Restriccion_las_entidades_no_podran_utilizar_fondos_de_su_pgc_para_realizar_pagos_a_proveedo_ae93fe -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27632: aplica_a Restriccion_las_entidades_que_no_cumplan_con_las_obligaciones_de_informar_podran_ser_sancion_a9ad62 -> Sujeto_banco: sin mención
idx 27634: aplica_a Restriccion_las_entidades_que_titulicen_sinteticamente_las_exposiciones_a_traves_de_la_compr_f898c7 -> Sujeto_rol_alcance_capmin: sin mención
idx 27636: aplica_a Restriccion_las_entidades_solo_podran_vender_titulos_valores_en_el_mercado_secundario_con_li_dd7c73 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27639: aplica_a Restriccion_las_evaluaciones_externas_que_correspondan_a_una_unidad_de_un_grupo_economico_no_46c3ab -> Sujeto_rol_alcance_capmin: sin mención
idx 27642: aplica_a Restriccion_las_exigencias_a_ser_incluidas_dentro_del_calculo_del_promedio_de_erc_se_extiend_e655ee -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 27645: aplica_a Restriccion_las_exportaciones_de_bienes_efectuadas_por_un_vpu_adherido_al_rigi_estan_sujetas_25a066 -> Sujeto_vpu_rigi: sin mención
idx 27649: aplica_a Restriccion_las_facilidades_de_liquidez_por_parte_de_la_entidad_financiera_que_actua_como_ag_e0fc9c -> Sujeto_rol_alcance_capmin: sin mención
idx 27652: aplica_a Restriccion_las_financiaciones_a_deudores_clasificados_en_categoria_irrecuperable_y_que_se_e_c925fb -> Sujeto_entidad_financiera: sin mención
idx 27655: aplica_a Restriccion_las_financiaciones_de_los_puntos_7_11_1_1_a_7_11_1_4_no_tengan_vencimientos_de_c_017d83 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27667: aplica_a Restriccion_las_financiaciones_de_los_puntos_7_11_1_5_a_7_11_1_6_no_registren_vencimientos_d_1910b7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27681: aplica_a Restriccion_las_financiaciones_no_podran_superar_el_10_de_la_capacidad_de_prestamo__polcre_2_9c21bb -> Sujeto_entidad_financiera: sin mención
idx 27685: aplica_a Restriccion_las_garantias_acumuladas_en_moneda_extranjera_no_superen_el_equivalente_al_125_c_d95281 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27688: aplica_a Restriccion_las_garantias_acumuladas_en_moneda_extranjera_que_podran_ser_utilizadas_para_el__6866ec -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27691: aplica_a Restriccion_las_inversiones_directas_de_no_residentes_no_pueden_ser_en_empresas_que_sean_con_29e1d2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27694: aplica_a Restriccion_las_obligaciones_negociables_compradas_emisiones_propias_quedan_excluidas_de_los_5f8dae -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 27697: aplica_a Restriccion_las_opciones_sobre_acciones_e_indices_bursatiles_se_excluiran_junto_con_sus_suby_dfd362 -> Sujeto_rol_alcance_capmin: sin mención
idx 27754: aplica_a Restriccion_las_operaciones_de_pase_en_las_cuales_la_contraparte_no_sea_un_participante_esen_9f4389 -> Sujeto_rol_alcance_capmin: sin mención
idx 27757: aplica_a Restriccion_las_operaciones_de_pase_estaran_sujetas_a_un_ponderador_de_riesgo_del_0_cuando_l_f92231 -> Sujeto_rol_alcance_capmin: sin mención
idx 27760: aplica_a Restriccion_las_operaciones_de_titulizacion_que_incluyan_una_opcion_de_exclusion_que_no_cump_03ec35 -> Sujeto_rol_alcance_capmin: sin mención
idx 27763: aplica_a Restriccion_las_operaciones_en_las_que_la_exposicion_y_el_activo_recibido_en_garantia_esten__541b74 -> Sujeto_rol_alcance_capmin: sin mención
idx 27766: aplica_a Restriccion_las_operaciones_originadas_en_la_prestacion_de_servicios_por_parte_de_contrapart_820eb2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27771: aplica_a Restriccion_las_otras_exposiciones_crediticias_no_calificadas_del_emisor_seran_tratadas_como_602651 -> Sujeto_rol_alcance_capmin: sin mención
idx 27777: aplica_a Restriccion_las_participaciones_en_fideicomisos_quedan_comprendidas_en_la_medida_en_que_el_r_596a77 -> Sujeto_rol_alcance_capmin: sin mención
idx 27779: aplica_a Restriccion_las_partidas_fuera_de_balance_que_refieran_a_compromisos_estaran_sujetas_al_meno_941040 -> Sujeto_rol_alcance_capmin: sin mención
idx 27781: aplica_a Restriccion_las_perdidas_deben_divulgarse_antes_y_despues_de_exclusiones_no_relevantes_para__901098 -> Sujeto_rol_alcance_capmin: sin mención
idx 27783: aplica_a Restriccion_las_perdidas_deben_divulgarse_netas_de_recuperos_efectivamente_percibidos__cap_7_11f11a -> Sujeto_rol_alcance_capmin: sin mención
idx 27785: aplica_a Restriccion_las_politicas_practicas_y_procedimientos_de_los_sujetos_obligados_no_podran_repr_e58e79 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 27787: aplica_a Restriccion_las_posiciones_arancelarias_de_los_bienes_de_capital_a_importar_no_correspondan__1d44ef -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27793: aplica_a Restriccion_las_posiciones_brutas_en_cada_banda_temporal_estaran_sujetas_a_los_ponderadores__5b317c -> Sujeto_rol_alcance_capmin: sin mención
idx 27804: aplica_a Restriccion_las_posiciones_de_titulizacion_a_las_que_no_se_les_pueda_aplicar_el_enfoque_esta_bcb906 -> Sujeto_rol_alcance_capmin: sin mención
idx 27808: aplica_a Restriccion_las_previsiones_generales_de_las_exposiciones_subyacentes_no_se_tendran_en_cuent_897118 -> Sujeto_rol_alcance_capmin: sin mención
idx 27810: aplica_a Restriccion_las_previsiones_por_riesgo_de_incobrabilidad_no_superaran_el_1_25_de_los_activos_97005c -> Sujeto_rol_alcance_capmin: sin mención
idx 27819: aplica_a Restriccion_las_tasas_de_interes_o_de_descuento_de_referencia_deberan_ser_tasas_de_interes_d_3b0091 -> Sujeto_rol_alcance_capmin: sin mención
idx 27821: aplica_a Restriccion_las_transacciones_de_titulos_valores_concertadas_en_el_exterior_no_podran_liquid_d30402 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27824: aplica_a Restriccion_las_unicas_coberturas_admisibles_para_el_calculo_de_la_exigencia_de_capital_por__64534e -> Sujeto_rol_alcance_capmin: sin mención
idx 27839: aplica_a Restriccion_limite_a_la_exigencia_por_riesgo_operacional_para_entidades_incluidas_en_los_gru_36bee5 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 27841: aplica_a Restriccion_limite_maximo_equivalente_a_usd_100_dolares_estadounidenses_cien_en_el_conjunto__46a1bb -> Sujeto_persona_humana: sin mención
idx 27844: aplica_a Restriccion_los_activos_admitidos_como_garantia_deberan_limitarse_a_aquellos_enumerados_en_e_4a8c8a -> Sujeto_rol_alcance_capmin: sin mención
idx 27847: aplica_a Restriccion_los_activos_admitidos_como_garantia_se_limitan_a_los_especificados_en_los_puntos_f44f92 -> Sujeto_rol_alcance_capmin: sin mención
idx 27868: aplica_a Restriccion_los_anticipos_de_efectivo_por_parte_de_la_entidad_financiera_que_actua_como_agen_4b2bb8 -> Sujeto_rol_alcance_capmin: sin mención
idx 27871: aplica_a Restriccion_los_aportes_no_podran_ser_efectuados_en_especie_deben_ser_efectuados_en_efectivo_d72e11 -> Sujeto_rol_alcance_capmin: sin mención
idx 27875: aplica_a Restriccion_los_bancos_salvo_cajas_de_credito_cooperativas_deberan_mantener_un_capital_minim_8ce70c -> Sujeto_banco: sin mención
idx 27878: aplica_a Restriccion_los_beneficios_cambiarios_del_rigi_no_podran_ser_acumulados_con_otros_incentivos_fd334c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27880: aplica_a Restriccion_los_bienes_clasificados_como_bk_deben_representar_como_minimo_el_90_noventa_por__75c58a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27882: aplica_a Restriccion_los_casos_que_no_encuadren_en_lo_expuesto_precedentemente_requeriran_la_conformi_e350b4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27884: aplica_a Restriccion_los_certificados_de_deposito_a_plazo_fijo_solo_pueden_colocarse_en_entidades_que_2d8347 -> Sujeto_entidad_financiera: sin mención
idx 27887: aplica_a Restriccion_los_cheques_comunes_solo_podran_contener_hasta_un_endoso__ctacte_5_1_1_1_489e7b -> Sujeto_banco: sin mención
idx 27890: aplica_a Restriccion_los_cheques_de_pago_diferido_presentados_a_registro_deberan_ser_rechazados_cuand_bd41c0 -> Sujeto_banco: sin mención
idx 27893: aplica_a Restriccion_los_cheques_de_pago_diferido_solo_podran_contener_hasta_2_dos_endosos__ctacte_5__e0bf31 -> Sujeto_banco: sin mención
idx 27898: aplica_a Restriccion_los_cheques_no_pueden_contener_inscripciones_de_propaganda__ctacte_3_2_4_b05579 -> Sujeto_banco: sin mención
idx 27901: aplica_a Restriccion_los_cheques_podran_ser_presentados_a_registro_hasta_el_dia_anterior_a_su_vencimi_f325bf -> Sujeto_banco: sin mención
idx 27904: aplica_a Restriccion_los_cheques_que_se_presenten_al_cobro_o_en_su_caso_a_la_registracion_hasta_el_31_794564 -> Sujeto_banco: sin mención
idx 27907: aplica_a Restriccion_los_clientes_podran_suscribir_bonos_bopreal_por_hasta_el_equivalente_al_monto_en_f20501 -> Sujeto_cliente: sin mención
idx 27910: aplica_a Restriccion_los_clientes_que_sean_deudores_en_situacion_irregular_conforme_a_la_nomina_elabo_e7a6d2 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 27913: aplica_a Restriccion_los_cobros_de_exportaciones_que_pretenden_enmarcarse_en_este_mecanismo_no_fueron_775bcc -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 27916: aplica_a Restriccion_los_conceptos_de_retribuciones_y_utilidades_no_podran_integrar_los_cargos_que_se_a34fb9 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 27974: aplica_a Restriccion_los_criterios_stc_deberan_cumplirse_en_todo_momento__cap_3_1_14_cf5010 -> Sujeto_rol_alcance_capmin: sin mención
idx 27979: aplica_a Restriccion_los_datos_consignados_en_la_declaracion_jurada_en_cuanto_a_cantidad_de_casos_y_m_de3813 -> Sujeto_rol_alcance_pagjub: sin mención
idx 27981: aplica_a Restriccion_los_datos_que_se_suministren_referidos_a_cada_una_de_las_situaciones_previstas_e_1a90f4 -> Sujeto_banco: sin mención
idx 27984: aplica_a Restriccion_los_defectos_de_aplicacion_que_se_originen_en_operaciones_de_canje_dispuestas_po_0f8c2a -> Sujeto_entidad_financiera: sin mención
idx 27987: aplica_a Restriccion_los_derechos_y_o_facultades_reconocidos_al_usuario_por_estas_normas_no_pueden_en_0885c0 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 27989: aplica_a Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti_17ae50 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 27996: aplica_a Restriccion_los_endeudamientos_financieros_y_o_los_aportes_de_inversion_extranjera_directa_n_25f380 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28002: aplica_a Restriccion_los_funcionarios_que_se_designen_deberan_desempenarse_en_cargos_de_rango_gerenci_0d18aa -> Sujeto_rol_alcance_pagjub: sin mención
idx 28004: aplica_a Restriccion_los_garantes_admisibles_se_limitan_a_los_estipulados_en_el_punto_5_4_1_los_spe_n_424c66 -> Sujeto_rol_alcance_capmin: sin mención
idx 28015: aplica_a Restriccion_los_garantes_y_contragarantes_admisibles_se_limitaran_a_aquellos_listados_en_el__ef19e9 -> Sujeto_rol_alcance_capmin: sin mención
idx 28031: aplica_a Restriccion_los_importadores_de_bienes_podran_suscribir_bonos_bopreal_por_hasta_el_monto_de__68d392 -> Sujeto_importador_de_bienes: sin mención
idx 28034: aplica_a Restriccion_los_importadores_de_servicios_podran_suscribir_bopreal_por_hasta_el_monto_de_la__d89a77 -> Sujeto_importador_de_servicios: sin mención
idx 28037: aplica_a Restriccion_los_importes_no_ingresados_en_tiempo_y_forma_a_esta_institucion_por_las_entidade_0a8915 -> Sujeto_banco: sin mención
idx 28040: aplica_a Restriccion_los_importes_se_consignaran_sin_signo_excepto_para_aquellos_casos_en_que_expresa_50a7ee -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 28042: aplica_a Restriccion_los_incentivos_no_deberian_debilitar_la_politica_establecida_en_materia_de_mante_21198c -> Sujeto_entidad_financiera: sin mención
idx 28044: aplica_a Restriccion_los_incentivos_se_eliminan_cuando_se_registren_perdidas_en_la_entidad_division_o_ac6280 -> Sujeto_entidad_financiera: sin mención
idx 28047: aplica_a Restriccion_los_incentivos_se_reducen_cuando_los_resultados_de_la_entidad_de_la_division_o_d_254f50 -> Sujeto_entidad_financiera: sin mención
idx 28050: aplica_a Restriccion_los_incumplimientos_a_esta_normativa_se_encontraran_alcanzados_por_la_ley_del_re_1579f4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28052: aplica_a Restriccion_los_incumplimientos_en_el_envio_de_la_informacion_estaran_sujetos_a_la_aplicacio_1e726a -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28054: aplica_a Restriccion_los_informes_a_ser_presentados_por_los_auditores_externos_no_deben_contener_limi_cdf09b -> Sujeto_entidad_financiera: sin mención
idx 28056: aplica_a Restriccion_los_instrumentos_incluidos_en_el_ca_no_habran_sido_comprados_con_la_financiacion_ffc028 -> Sujeto_rol_alcance_capmin: sin mención
idx 28058: aplica_a Restriccion_los_instrumentos_incluidos_en_el_pnc_no_podran_estar_asegurados_ni_cubiertos_por_b0072f -> Sujeto_rol_alcance_capmin: sin mención
idx 28061: aplica_a Restriccion_los_instrumentos_incluidos_en_el_pnc_no_podran_estar_cubiertos_por_alguna_garant_1131b9 -> Sujeto_rol_alcance_capmin: sin mención
idx 28064: aplica_a Restriccion_los_instrumentos_incluidos_en_el_pnc_no_podran_ser_objeto_de_cualquier_otro_acue_0ca927 -> Sujeto_rol_alcance_capmin: sin mención
idx 28067: aplica_a Restriccion_los_instrumentos_no_contienen_clausulas_que_contemplen_aumentos_de_la_posicion_a_37b99c -> Sujeto_rol_alcance_capmin: sin mención
idx 28069: aplica_a Restriccion_los_instrumentos_no_contienen_clausulas_que_incrementen_el_costo_de_la_proteccio_92c265 -> Sujeto_rol_alcance_capmin: sin mención
idx 28071: aplica_a Restriccion_los_instrumentos_no_contienen_clausulas_que_incrementen_el_rendimiento_pagadero__7af7b8 -> Sujeto_rol_alcance_capmin: sin mención
idx 28073: aplica_a Restriccion_los_instrumentos_no_contienen_clausulas_que_obliguen_a_la_entidad_originante_a_a_279d8a -> Sujeto_rol_alcance_capmin: sin mención
idx 28076: aplica_a Restriccion_los_instrumentos_utilizados_para_transferir_el_riesgo_de_credito_no_contienen_cl_7cb61a -> Sujeto_rol_alcance_capmin: sin mención
idx 28078: aplica_a Restriccion_los_montos_abonados_por_este_mecanismo_en_el_conjunto_de_las_entidades_y_por_el__1748a7 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28082: aplica_a Restriccion_los_montos_de_las_divisas_a_ser_afectadas_en_el_marco_de_lo_dispuesto_en_el_capi_923ad8 -> Sujeto_beneficiario_economia_conocimiento: sin mención
idx 28084: aplica_a Restriccion_los_montos_de_las_divisas_a_ser_afectadas_en_el_marco_de_lo_dispuesto_en_el_capi_d84312 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28089: aplica_a Restriccion_los_numeros_asignados_a_las_presentaciones_deberan_ser_correlativos_y_la_base_de_7a1230 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 28100: aplica_a Restriccion_los_pagos_por_deudas_de_bienes_o_servicios_realizados_en_el_marco_de_los_mecanis_8cf706 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28111: aplica_a Restriccion_los_prestamos_a_instituciones_de_microcredito_no_pueden_exceder_el_equivalente_a_eed32e -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 28115: aplica_a Restriccion_los_prestamos_no_deberan_ser_destinados_a_empresas_o_entes_de_proposito_especial_3a5fff -> Sujeto_rol_alcance_capmin: sin mención
idx 28118: aplica_a Restriccion_los_prestamos_no_deberan_ser_destinados_a_empresas_o_entes_de_proposito_especial_7cc940 -> Sujeto_rol_alcance_capmin: sin mención
idx 28121: aplica_a Restriccion_los_punitorios_u_otros_equivalentes_que_se_devenguen_desde_el_01_01_25_continuar_a1c5ac -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28124: aplica_a Restriccion_los_riesgos_sujetos_a_esta_exigencia_de_capital_son_los_riesgos_de_las_posicione_4b00b8 -> Sujeto_rol_alcance_capmin: sin mención
idx 28126: aplica_a Restriccion_los_sistemas_electronicos_de_reproduccion_de_firmas_digitalizadas_no_podran_util_e3b0df -> Sujeto_banco: sin mención
idx 28129: aplica_a Restriccion_los_subtramos_que_no_son_de_maxima_preferencia_se_deberan_tratar_como_posiciones_8e8236 -> Sujeto_rol_alcance_capmin: sin mención
idx 28149: aplica_a Restriccion_los_sujetos_obligados_no_podran_percibir_de_los_usuarios_ningun_tipo_de_comision_ca3b32 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 28152: aplica_a Restriccion_los_sujetos_obligados_no_podran_percibir_de_los_usuarios_ningun_tipo_de_retribuc_f14e4e -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 28155: aplica_a Restriccion_los_sujetos_obligados_no_podran_registrar_retribuciones_ni_utilidades_por_los_se_c09940 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 28159: aplica_a Restriccion_los_swaps_referidos_a_diferentes_productos_basicos_no_podran_compensarse__cap_6__6db5e8 -> Sujeto_rol_alcance_capmin: sin mención
idx 28161: aplica_a Restriccion_los_terminos_contractuales_no_deberan_contener_clausula_alguna_que_pudiera_origi_3e6c4d -> Sujeto_rol_alcance_capmin: sin mención
idx 28163: aplica_a Restriccion_los_tipos_de_cambio_minorista_comprador_y_vendedor_ofrecidos_no_podran_diferir_e_043cb9 -> Sujeto_entidad_cambiaria: sin mención
idx 28166: aplica_a Restriccion_los_titulos_devueltos_por_esas_situaciones_no_podran_ser_objeto_de_nuevas_presen_54f24e -> Sujeto_banco: sin mención
idx 28169: aplica_a Restriccion_los_titulos_devueltos_por_falta_de_especificaciones_incluida_la_falta_de_numero__38cd57 -> Sujeto_banco: sin mención
idx 28173: aplica_a Restriccion_los_titulos_devueltos_por_falta_de_especificaciones_no_podran_ser_objeto_de_nuev_3833af -> Sujeto_banco: sin mención
idx 28176: aplica_a Restriccion_los_titulos_devueltos_por_las_situaciones_enumeradas_en_3_2_1_no_podran_ser_obje_a0716d -> Sujeto_banco: sin mención
idx 28178: aplica_a Restriccion_los_titulos_devueltos_por_las_situaciones_que_los_hacen_carecer_de_valor_como_ch_62cb56 -> Sujeto_banco: sin mención
idx 28180: aplica_a Restriccion_los_titulos_emitidos_por_gobiernos_de_paises_extranjeros_que_no_cumplan_con_lo_p_5a28d1 -> Sujeto_rol_alcance_capmin: sin mención
idx 28182: aplica_a Restriccion_los_titulos_valores_subordinados_no_deberan_tener_preferencia_de_pago_sobre_los__677a9b -> Sujeto_rol_alcance_capmin: sin mención
idx 28184: aplica_a Restriccion_los_unicos_derivados_admisibles_son_los_que_se_toman_para_la_genuina_cobertura_d_a9dfe5 -> Sujeto_rol_alcance_capmin: sin mención
idx 28189: aplica_a Restriccion_motivo_de_inclusion_en_la_central_de_cheques_rechazados_no_registracion_de_chequ_c5e87d -> Sujeto_banco: sin mención
idx 28192: aplica_a Restriccion_multa_equivalente_al_4_del_valor_rechazado_con_minimo_100_y_maximo_50_000__ctact_c37c2a -> Sujeto_banco: sin mención
idx 28197: aplica_a Restriccion_ninguna_exposicion_con_deudores_no_calificados_podra_recibir_un_ponderador_de_ri_3eca1e -> Sujeto_rol_alcance_capmin: sin mención
idx 28199: aplica_a Restriccion_ninguna_exposicion_crediticia_incluyendo_creditos_titulos_valores_y_responsabili_0d9696 -> Sujeto_rol_alcance_capmin: sin mención
idx 28206: aplica_a Restriccion_no_contar_con_la_expresion_presentado_electronicamente_al_cobro_en_el_frente_y_o_84edb5 -> Sujeto_banco: sin mención
idx 28210: aplica_a Restriccion_no_correspondera_la_comunicacion_al_bcra_de_los_rechazos_motivados_por_errores_i_7fae75 -> Sujeto_banco: sin mención
idx 28212: aplica_a Restriccion_no_correspondera_realizar_registro_cambiario_a_nombre_de_la_propia_entidad_por_m_49a088 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28219: aplica_a Restriccion_no_debera_existir_una_correlacion_positiva_sustancial_entre_la_calidad_creditici_412764 -> Sujeto_rol_alcance_capmin: sin mención
idx 28222: aplica_a Restriccion_no_deberan_abonar_en_efectivo_cheques_comunes_o_de_pago_diferido_extendidos_al_p_0df03f -> Sujeto_banco: sin mención
idx 28225: aplica_a Restriccion_no_deberan_considerarse_en_el_calculo_del_k_cva_otros_tipos_de_cobertura_del_rie_d3f7c3 -> Sujeto_rol_alcance_capmin: sin mención
idx 28240: aplica_a Restriccion_no_deberan_existir_disposiciones_que_requieran_la_inmediata_liquidacion_de_los_a_f49e0e -> Sujeto_rol_alcance_capmin: sin mención
idx 28243: aplica_a Restriccion_no_emitir_cheques_comunes_apartandose_de_las_condiciones_convenidas_por_escrito__de1557 -> Sujeto_banco: sin mención
idx 28245: aplica_a Restriccion_no_es_requisito_que_una_ecai_evalue_empresas_en_mas_de_un_pais_para_ser_reconoci_327dba -> Sujeto_ecai: sin mención
idx 28249: aplica_a Restriccion_no_estar_asegurados_ni_cubiertos_por_alguna_garantia_del_emisor_o_de_un_vinculad_39acf8 -> Sujeto_rol_alcance_capmin: sin mención
idx 28252: aplica_a Restriccion_no_existir_clausulas_de_remuneracion_escalonada_creciente_u_otros_incentivos_par_77e34b -> Sujeto_rol_alcance_capmin: sin mención
idx 28255: aplica_a Restriccion_no_haber_sido_comprados_con_la_financiacion_directa_o_indirecta_de_la_entidad_fi_bad064 -> Sujeto_rol_alcance_capmin: sin mención
idx 28258: aplica_a Restriccion_no_haber_sido_comprados_por_la_entidad_financiera_ni_por_alguna_entidad_que_ella_6b1f59 -> Sujeto_rol_alcance_capmin: sin mención
idx 28261: aplica_a Restriccion_no_haber_sido_comprados_por_la_entidad_financiera_ni_por_alguna_entidad_que_ella_aea9a2 -> Sujeto_rol_alcance_capmin: sin mención
idx 28264: aplica_a Restriccion_no_incorporar_un_dividendo_cupon_que_se_reajuste_periodicamente_en_funcion_en_to_ea321f -> Sujeto_rol_alcance_capmin: sin mención
idx 28266: aplica_a Restriccion_no_operar_en_condiciones_mas_favorables_que_las_acordadas_de_ordinario_a_su_clie_3b89af -> Sujeto_entidad_financiera: sin mención
idx 28269: aplica_a Restriccion_no_podra_devengar_ningun_tipo_de_comision_y_o_cargo_desde_la_fecha_de_presentaci_32a44a -> Sujeto_banco: sin mención
idx 28274: aplica_a Restriccion_no_podra_excederse_el_nivel_de_depositos_alcanzados_en_el_mes_en_el_que_se_origi_d96af6 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 28277: aplica_a Restriccion_no_podra_usarse_la_calificacion_si_la_exposicion_crediticia_no_es_igual_o_prefer_722cf8 -> Sujeto_rol_alcance_capmin: sin mención
idx 28280: aplica_a Restriccion_no_podran_aplicarse_comisiones_a_las_operaciones_efectuadas_por_ventanilla_por_l_b95886 -> Sujeto_banco: sin mención
idx 28314: aplica_a Restriccion_no_podran_aplicarse_comisiones_ni_cargos_por_contratacion_y_o_administracion_de__ead06f -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 28317: aplica_a Restriccion_no_podran_aplicarse_comisiones_ni_cargos_por_depositos_de_efectivo_en_pesos_en_c_94e96d -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 28320: aplica_a Restriccion_no_podran_aplicarse_comisiones_ni_cargos_por_evaluacion_otorgamiento_y_o_adminis_e39c60 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 28323: aplica_a Restriccion_no_podran_aplicarse_comisiones_ni_cargos_por_gastos_de_tasacion_notariales_o_de__d56d29 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 28326: aplica_a Restriccion_no_podran_aplicarse_comisiones_ni_cargos_por_generacion_de_resumenes_de_cuenta_y_534fa0 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 28329: aplica_a Restriccion_no_podran_aplicarse_comisiones_ni_cargos_por_operaciones_efectuadas_por_ventanil_2eb299 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 28332: aplica_a Restriccion_no_podran_arrojar_saldo_deudor__pagjub_3_2_1_4_f98ec4 -> Sujeto_rol_alcance_pagjub: sin mención
idx 28334: aplica_a Restriccion_no_podran_distribuirse_dividendos_en_efectivo_ni_efectuarse_pagos_de_honorarios__c04544 -> Sujeto_rol_alcance_capmin: sin mención
idx 28338: aplica_a Restriccion_no_podran_incluirse_deudores_cuyas_obligaciones_hayan_sido_refinanciadas_por_la__7d7c50 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 28340: aplica_a Restriccion_no_podran_reconocerse_como_crc_otros_tipos_de_derivados_de_credito_incluyendo_a__0f1eb6 -> Sujeto_rol_alcance_capmin: sin mención
idx 28343: aplica_a Restriccion_no_podran_reconocerse_los_spe_como_garantes_admisibles__cap_3_1_13_c53b59 -> Sujeto_rol_alcance_capmin: sin mención
idx 28345: aplica_a Restriccion_no_podran_registrarse_tenencias_de_titulos_valores_publicos_y_privados_del_exter_cd22ab -> Sujeto_entidad_financiera: sin mención
idx 28348: aplica_a Restriccion_no_podran_tener_clausulas_de_remuneracion_escalonada_creciente_ni_otros_incentiv_6c9d18 -> Sujeto_rol_alcance_capmin: sin mención
idx 28350: aplica_a Restriccion_no_podran_utilizarse_terminos_que_no_esten_previstos_en_la_ley_de_cheques_o_en_l_4e7b03 -> Sujeto_banco: sin mención
idx 28353: aplica_a Restriccion_no_poseer_caracteristicas_que_dificulten_la_recapitalizacion_tales_como_requerir_e39f06 -> Sujeto_rol_alcance_capmin: sin mención
idx 28355: aplica_a Restriccion_no_prevalecera_el_criterio_de_considerar_la_causal_por_falta_de_fondos_cuando_el_9dc7fa -> Sujeto_banco: sin mención
idx 28360: aplica_a Restriccion_no_prever_pago_de_ningun_tipo_en_concepto_de_capital_excepto_en_caso_de_liquidac_66b9bf -> Sujeto_rol_alcance_capmin: sin mención
idx 28362: aplica_a Restriccion_no_puede_procederse_al_pago_de_un_cheque_cuando_existe_concurso_preventivo_del_l_11812c -> Sujeto_banco: sin mención
idx 28370: aplica_a Restriccion_no_puede_procederse_al_pago_de_un_cheque_cuando_se_detecta_adulteracion_o_falsif_3eb76b -> Sujeto_banco: sin mención
idx 28373: aplica_a Restriccion_no_pueden_incorporar_un_dividendo_cupon_que_se_reajuste_periodicamente_en_funcio_ed489c -> Sujeto_rol_alcance_capmin: sin mención
idx 28376: aplica_a Restriccion_no_se_admite_aplicar_los_depositos_en_cuentas_especiales_para_acreditar_financia_d05b7b -> Sujeto_entidad_financiera: sin mención
idx 28379: aplica_a Restriccion_no_se_admite_la_compensacion_entre_posiciones_en_diferentes_productos_basicos_ni_d671bf -> Sujeto_rol_alcance_capmin: sin mención
idx 28381: aplica_a Restriccion_no_se_admitira_el_descalce_de_plazos_de_vencimiento__cap_5_3_1_1_7c4720 -> Sujeto_rol_alcance_capmin: sin mención
idx 28383: aplica_a Restriccion_no_se_admitira_que_los_cheques_lleven_mas_de_3_firmas__ctacte_1_5_1_8_153ca9 -> Sujeto_banco: sin mención
idx 28386: aplica_a Restriccion_no_se_admitiran_depositos_ni_creditos_por_transferencias_ordenadas_por_las_entid_aebd0e -> Sujeto_rol_alcance_pagjub: sin mención
idx 28389: aplica_a Restriccion_no_se_admitiran_los_aportes_de_esta_clase_de_instrumentos_cuando_no_se_verifique_90dfb8 -> Sujeto_rol_alcance_capmin: sin mención
idx 28391: aplica_a Restriccion_no_se_aplicara_el_plazo_minimo_de_veinte_dias_habiles_para_el_calculo_del_period_1f37ac -> Sujeto_rol_alcance_capmin: sin mención
idx 28394: aplica_a Restriccion_no_se_computaran_como_endosos_a_los_fines_del_limite_establecido_en_el_punto_5_1_0ceaad -> Sujeto_banco: sin mención
idx 28421: aplica_a Restriccion_no_se_dara_reconocimiento_a_la_cobertura_del_riesgo_de_credito_que_ya_se_encuent_c71798 -> Sujeto_rol_alcance_capmin: sin mención
idx 28424: aplica_a Restriccion_no_se_ha_incluido_la_declaracion_jurada__pagjub_2_7_1_d69451 -> Sujeto_rol_alcance_pagjub: sin mención
idx 28428: aplica_a Restriccion_no_se_incluiran_dentro_de_las_previsiones_por_riesgo_de_incobrabilidad_computabl_17f197 -> Sujeto_rol_alcance_capmin: sin mención
idx 28452: aplica_a Restriccion_no_se_permite_la_compensacion_de_ajustes_de_valuacion_por_riesgo_de_credito_prop_1ffa6b -> Sujeto_rol_alcance_capmin: sin mención
idx 28455: aplica_a Restriccion_no_se_permite_la_compensacion_o_cobertura_entre_conjuntos_de_cobertura_de_commod_2411ae -> Sujeto_rol_alcance_capmin: sin mención
idx 28458: aplica_a Restriccion_no_se_permitira_seleccionar_solo_los_flujos_futuros_esperados_que_reduzcan_la_po_88f709 -> Sujeto_rol_alcance_capmin: sin mención
idx 28460: aplica_a Restriccion_no_se_podran_cobrar_comisiones_y_o_cargos_diferenciales_a_usuarios_con_dificulta_5fa5d1 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 28464: aplica_a Restriccion_no_se_podran_percibir_de_los_clientes_cargos_ni_comisiones_por_el_proceso_vincul_e26e7d -> Sujeto_entidad_financiera: sin mención
idx 28467: aplica_a Restriccion_no_se_puede_acceder_al_mercado_de_cambios_para_pagos_de_capital_e_intereses_de_e_ab515b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28493: aplica_a Restriccion_no_se_requiere_seguimiento_de_divisas_para_la_exportacion_a_consumo_con_destinac_ff5e10 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28495: aplica_a Restriccion_no_ser_objeto_de_cualquier_otro_acuerdo_que_mejore_juridica_o_economicamente_el__3747ac -> Sujeto_rol_alcance_capmin: sin mención
idx 28498: aplica_a Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces_18611a -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 28501: aplica_a Restriccion_no_tendra_acceso_al_mercado_de_cambios_para_repatriar_el_equivalente_de_estos_fo_998a4b -> Sujeto_persona_humana: sin mención
idx 28503: aplica_a Restriccion_no_valdra_como_cheque_aquella_emision_cuya_fecha_de_vencimiento_sea_anterior_o_i_0e2262 -> Sujeto_banco: sin mención
idx 28506: aplica_a Restriccion_o_del_4_si_se_da_el_caso_del_anteultimo_parrafo_del_acapite_iii__cap_4_3_3_1_13901e -> Sujeto_rol_alcance_capmin: sin mención
idx 28508: aplica_a Restriccion_obligacion_de_ingreso_y_liquidacion_de_cobranzas_de_exportacion_de_bienes__ext_1_497e27 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28511: aplica_a Restriccion_obligaciones_entre_el_5_y_menos_del_20_del_patrimonio_cuando_persista_el_pedido__eaf42c -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 28513: aplica_a Restriccion_obligaciones_que_sean_iguales_o_superiores_al_20_del_patrimonio_del_cliente__cla_b79740 -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 28515: aplica_a Restriccion_otros_importes_generados_en_forma_impropia_por_su_naturaleza_tales_como_interese_2d5cc6 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 28518: aplica_a Restriccion_otros_soberanos_y_sus_bancos_centrales_exigencia_de_capital_por_riesgo_especific_d12997 -> Sujeto_banco_central_del_exterior: sin mención
idx 28521: aplica_a Restriccion_pagos_de_capital_e_intereses_de_endeudamientos_financieros_con_el_exterior_cuyo__7220a2 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28538: aplica_a Restriccion_pagos_de_intereses_de_deudas_comerciales_por_importacion_de_bienes_y_servicios_c_3db3fd -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28549: aplica_a Restriccion_para_exposiciones_a_bancos_multilaterales_de_desarrollo_bmd_con_calificacion_de__4cf197 -> Sujeto_rol_alcance_capmin: sin mención
idx 28552: aplica_a Restriccion_para_exposiciones_a_bancos_multilaterales_de_desarrollo_bmd_con_calificacion_de__56b968 -> Sujeto_rol_alcance_capmin: sin mención
idx 28555: aplica_a Restriccion_para_exposiciones_a_bancos_multilaterales_de_desarrollo_bmd_con_calificacion_de__813c13 -> Sujeto_rol_alcance_capmin: sin mención
idx 28558: aplica_a Restriccion_para_exposiciones_a_bancos_multilaterales_de_desarrollo_bmd_con_calificacion_de__aff2e1 -> Sujeto_rol_alcance_capmin: sin mención
idx 28561: aplica_a Restriccion_para_exposiciones_a_bancos_multilaterales_de_desarrollo_bmd_con_calificacion_inf_e17853 -> Sujeto_rol_alcance_capmin: sin mención
idx 28564: aplica_a Restriccion_para_exposiciones_a_bancos_multilaterales_de_desarrollo_bmd_no_calificados_ponde_68bb44 -> Sujeto_rol_alcance_capmin: sin mención
idx 28567: aplica_a Restriccion_para_la_aplicacion_del_metodo_integral_el_valor_de_la_cobertura_debera_ajustarse_54c0a2 -> Sujeto_rol_alcance_capmin: sin mención
idx 28582: aplica_a Restriccion_para_reflejar_los_riesgos_de_base_y_de_brecha_temporal_se_aplicara_una_exigencia_2c7ec0 -> Sujeto_rol_alcance_capmin: sin mención
idx 28584: aplica_a Restriccion_para_sociedades_por_acciones_simplificadas_sas_unicamente_se_requerira_la_presen_c1bff6 -> Sujeto_banco: sin mención
idx 28598: aplica_a Restriccion_partidas_de_efectivo_que_esten_en_tramite_de_ser_percibidas_cheques_y_giros_al_c_910e64 -> Sujeto_rol_alcance_capmin: sin mención
idx 28603: aplica_a Restriccion_permitan_al_sujeto_obligado_directa_o_indirectamente_alterar_el_importe_de_las_t_beeecf -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 28606: aplica_a Restriccion_plazo_minimo_un_ano__polcre_6_1_1_2_1a5ef6 -> Sujeto_entidad_financiera: sin mención
idx 28611: aplica_a Restriccion_ponderador_de_riesgo_0_para_calificaciones_de_aaa_hasta_aa__cap_2_12_2_5_52c020 -> Sujeto_rol_alcance_capmin: sin mención
idx 28614: aplica_a Restriccion_ponderador_de_riesgo_0_para_oro_amonedado_o_en_barras_de_buena_entrega__cap_2_12_c123ee -> Sujeto_rol_alcance_capmin: sin mención
idx 28617: aplica_a Restriccion_ponderador_de_riesgo_100_para_calificaciones_de_bb_hasta_b__cap_2_12_2_5_cbe55e -> Sujeto_rol_alcance_capmin: sin mención
idx 28620: aplica_a Restriccion_ponderador_de_riesgo_100_para_exposiciones_no_calificadas__cap_2_12_2_5_03c782 -> Sujeto_rol_alcance_capmin: sin mención
idx 28623: aplica_a Restriccion_ponderador_de_riesgo_150_para_calificaciones_inferiores_a_b__cap_2_12_2_5_0f8a8e -> Sujeto_rol_alcance_capmin: sin mención
idx 28626: aplica_a Restriccion_ponderador_de_riesgo_20_para_calificaciones_de_a_hasta_a__cap_2_12_2_5_516c0a -> Sujeto_rol_alcance_capmin: sin mención
idx 28629: aplica_a Restriccion_ponderador_de_riesgo_50_para_calificaciones_de_bbb_hasta_bbb__cap_2_12_2_5_95ab16 -> Sujeto_rol_alcance_capmin: sin mención
idx 28632: aplica_a Restriccion_ponderador_de_riesgo_de_0_para_exposicion_a_gobiernos_sector_publico_no_financie_a012c3 -> Sujeto_rol_alcance_capmin: sin mención
idx 28635: aplica_a Restriccion_ponderador_de_riesgo_de_0_para_exposiciones_a_bancos_multilaterales_de_desarroll_d3b893 -> Sujeto_rol_alcance_capmin: sin mención
idx 28638: aplica_a Restriccion_ponderador_de_riesgo_de_100_para_exposicion_a_gobiernos_sector_publico_no_financ_515e31 -> Sujeto_rol_alcance_capmin: sin mención
idx 28641: aplica_a Restriccion_ponderador_de_riesgo_de_100_para_exposicion_a_gobiernos_sector_publico_no_financ_809cdb -> Sujeto_rol_alcance_capmin: sin mención
idx 28644: aplica_a Restriccion_ponderador_de_riesgo_de_150_para_exposicion_a_gobiernos_sector_publico_no_financ_0c2a27 -> Sujeto_rol_alcance_capmin: sin mención
idx 28647: aplica_a Restriccion_ponderador_de_riesgo_de_20_para_exposicion_a_gobiernos_sector_publico_no_financi_694756 -> Sujeto_rol_alcance_capmin: sin mención
idx 28650: aplica_a Restriccion_ponderador_de_riesgo_de_50_para_exposicion_a_gobiernos_sector_publico_no_financi_ffc38c -> Sujeto_rol_alcance_capmin: sin mención
idx 28660: aplica_a Restriccion_ponderador_de_riesgo_del_100_para_exposiciones_con_calificacion_crediticia_de_bb_b578e4 -> Sujeto_rol_alcance_capmin: sin mención
idx 28663: aplica_a Restriccion_ponderador_de_riesgo_del_130_para_financiacion_especializada_de_grandes_proyecto_12616b -> Sujeto_rol_alcance_capmin: sin mención
idx 28671: aplica_a Restriccion_ponderador_de_riesgo_del_150_para_exposiciones_con_calificacion_crediticia_de_bb_6c0ba5 -> Sujeto_rol_alcance_capmin: sin mención
idx 28674: aplica_a Restriccion_ponderador_de_riesgo_del_200_para_exposiciones_con_calificacion_crediticia_infer_e3bfa8 -> Sujeto_rol_alcance_capmin: sin mención
idx 28677: aplica_a Restriccion_ponderador_de_riesgo_del_200_para_exposiciones_sin_calificacion_crediticia_no_ca_d9c98b -> Sujeto_rol_alcance_capmin: sin mención
idx 28682: aplica_a Restriccion_ponderador_de_riesgo_del_20_para_exposiciones_con_calificacion_crediticia_de_aaa_e5eb86 -> Sujeto_rol_alcance_capmin: sin mención
idx 28690: aplica_a Restriccion_ponderador_de_riesgo_del_50_para_exposiciones_con_calificacion_crediticia_de_a_h_8501d8 -> Sujeto_rol_alcance_capmin: sin mención
idx 28705: aplica_a Restriccion_por_el_importe_que_supere_el_55_del_valor_del_inmueble_se_aplicara_el_ponderador_543c32 -> Sujeto_rol_alcance_capmin: sin mención
idx 28708: aplica_a Restriccion_por_hasta_el_monto_proporcional_a_la_relacion_entre_el_monto_fob_total_en_divisa_d3267f -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28711: aplica_a Restriccion_por_hasta_el_monto_que_surge_de_considerar_el_monto_acumulado_de_los_beneficios__c372cb -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28714: aplica_a Restriccion_por_la_extension_de_plazo_la_cuota_no_supere_el_30_de_los_ingresos_computables___85822b -> Sujeto_entidad_financiera: sin mención
idx 28717: aplica_a Restriccion_presenta_defectos_formales_de_integracion__pagjub_2_7_1_39b766 -> Sujeto_rol_alcance_pagjub: sin mención
idx 28720: aplica_a Restriccion_prohibicion_de_tenencia_de_instrumentos_tlac_en_sucursales_y_subsidiarias_del_ex_e17275 -> Sujeto_entidad_financiera: sin mención
idx 28726: aplica_a Restriccion_que_el_total_de_los_pagos_realizados_con_imputacion_a_la_oficializacion_de_impor_9fecf6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28733: aplica_a Restriccion_quedan_exceptuadas_las_importaciones_realizadas_por_empresas_que_presten_servici_bc8dce -> Sujeto_importador_de_bienes: sin mención
idx 28743: aplica_a Restriccion_ratio_de_apalancamiento_mantendra_su_frecuencia_trimestral_datos_del_mes_de_cier_0ce6ab -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 28751: aplica_a Restriccion_reduccion_de_la_exigencia_para_entidades_financieras_del_grupo_2_que_pertenezcan_67dad8 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 28769: aplica_a Restriccion_requiere_calificacion_internacional_de_riesgo_comprendida_en_categoria_investmen_6eaacd -> Sujeto_rol_obligado_a_clasificar_clasificacion: sin mención
idx 28773: aplica_a Restriccion_requisito_complementario_aplicable_al_acceso_al_mercado_de_cambios_del_vpu_con_l_653c4a -> Sujeto_vpu_rigi: sin mención
idx 28777: aplica_a Restriccion_resultara_suspendida_la_posibilidad_de_librar_nuevos_echeq_o_endosarlos_hasta_da_873d84 -> Sujeto_banco: sin mención
idx 28782: aplica_a Restriccion_revocacion_de_la_autorizacion_para_funcionar_si_no_se_integra_el_capital_minimo__717f5d -> Sujeto_rol_alcance_capmin: sin mención
idx 28784: aplica_a Restriccion_salvo_impago_por_parte_del_comprador_de_la_proteccion_de_una_deuda_derivada_del__5ae76a -> Sujeto_rol_alcance_capmin: sin mención
idx 28827: aplica_a Restriccion_se_asegurara_de_que_la_delegacion_no_perjudique_a_los_clientes_ni_la_seguridad_d_ccae05 -> Sujeto_entidad_financiera: sin mención
idx 28832: aplica_a Restriccion_se_compromete_a_no_adquirir_certificados_de_depositos_argentinos_representativos_2c06d6 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28835: aplica_a Restriccion_se_compromete_a_no_adquirir_en_el_pais_titulos_valores_emitidos_por_no_residente_490884 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28838: aplica_a Restriccion_se_compromete_a_no_adquirir_titulos_valores_representativos_de_deuda_privada_emi_23bdac -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28841: aplica_a Restriccion_se_compromete_a_no_concertar_ventas_en_el_pais_de_titulos_valores_con_liquidacio_b25031 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28844: aplica_a Restriccion_se_compromete_a_no_entregar_fondos_en_moneda_local_ni_otros_activos_locales_exce_3edd10 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28847: aplica_a Restriccion_se_compromete_a_no_realizar_canjes_de_titulos_valores_emitidos_por_residentes_po_d4f8ec -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28850: aplica_a Restriccion_se_compromete_a_no_realizar_transferencias_de_titulos_valores_a_entidades_deposi_23d4ba -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28853: aplica_a Restriccion_se_debera_aplicar_a_la_posicion_neta_un_ponderador_de_riesgo_del_1250__cap_6_2_1_9e4646 -> Sujeto_rol_alcance_capmin: sin mención
idx 28855: aplica_a Restriccion_se_demuestre_el_registro_de_ingreso_aduanero_de_bienes_por_un_valor_equivalente__6ee8c4 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28940: aplica_a Restriccion_se_excluye_la_tenencia_de_instrumentos_de_deuda_emitidos_por_esas_empresas__cap__f17ef4 -> Sujeto_rol_alcance_capmin: sin mención
idx 28942: aplica_a Restriccion_se_excluyen_a_las_exposiciones_con_garantia_hipotecaria_sobre_vivienda_residenci_3f6b5b -> Sujeto_rol_alcance_capmin: sin mención
idx 28944: aplica_a Restriccion_se_excluyen_las_participaciones_en_el_capital_de_mipyme__cap_2_8_1_4fc78a -> Sujeto_rol_alcance_capmin: sin mención
idx 28946: aplica_a Restriccion_se_informara_el_mayor_saldo_de_la_asistencia_crediticia_otorgada_en_el_mes_cuand_c36e4b -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 28948: aplica_a Restriccion_se_informaran_las_previsiones_por_riesgo_de_incobrabilidad_correspondientes_a_fi_89d47c -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 28950: aplica_a Restriccion_se_observen_faltas_de_ortografia__ctacte_6_2_4_07708a -> Sujeto_banco: sin mención
idx 28954: aplica_a Restriccion_se_permitira_netear_las_posiciones_opuestas_respecto_de_una_misma_especie_inclui_2777a0 -> Sujeto_rol_alcance_capmin: sin mención
idx 28957: aplica_a Restriccion_se_prohibe_el_acceso_al_mercado_de_cambios_para_el_pago_de_deudas_y_otras_obliga_2e5b05 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28962: aplica_a Restriccion_se_prohibe_el_giro_sobre_el_librador__ctacte_6_1_2_7_86436e -> Sujeto_banco: sin mención
idx 28965: aplica_a Restriccion_se_prohibe_el_pago_de_cheques_con_irregularidades_en_la_cadena_de_endosos_confor_7918df -> Sujeto_banco: sin mención
idx 28968: aplica_a Restriccion_se_prohibe_proceder_al_pago_de_un_cheque_cuando_su_plazo_de_validez_legal_ha_ven_b7d355 -> Sujeto_banco: sin mención
idx 28971: aplica_a Restriccion_se_prohiben_practicas_y_operaciones_tendientes_a_eludir_a_traves_de_titulos_publ_2afb91 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 28975: aplica_a Restriccion_se_reconoce_proteccion_crediticia_de_bancos_multilaterales_de_desarrollo_a_que_s_726c65 -> Sujeto_banco_multilateral_de_desarrollo: sin mención
idx 28992: aplica_a Restriccion_se_reconoce_proteccion_crediticia_de_entidades_financieras_como_garantes_o_contr_fda9a2 -> Sujeto_entidad_financiera: sin mención
idx 28994: aplica_a Restriccion_se_reconoce_proteccion_crediticia_de_organismos_internacionales_a_los_que_se_les_a9a355 -> Sujeto_organismo_internacional: sin mención
idx 28999: aplica_a Restriccion_se_reconoce_proteccion_crediticia_de_sociedades_de_garantia_reciproca_y_fondos_d_25de4f -> Sujeto_fondo_de_garantia_publico: sin mención
idx 29000: aplica_a Restriccion_se_reconoce_proteccion_crediticia_de_sociedades_de_garantia_reciproca_y_fondos_d_25de4f -> Sujeto_sociedad_de_garantia_reciproca: sin mención
idx 29002: aplica_a Restriccion_se_reconoce_proteccion_crediticia_del_sector_publico_no_financiero_como_garante__2a4b90 -> Sujeto_sector_publico_no_financiero: sin mención
idx 29004: aplica_a Restriccion_se_reconoceran_solo_las_garantias_emitidas_o_proteccion_provista_en_el_caso_de_d_2ce66f -> Sujeto_rol_alcance_capmin: sin mención
idx 29016: aplica_a Restriccion_se_requerira_la_conformidad_previa_del_bcra_cuando_el_acreedor_sea_una_contrapar_114c9c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 29035: aplica_a Restriccion_se_requerira_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_4b79f1 -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 29037: aplica_a Restriccion_se_requerira_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_58d9de -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 29049: aplica_a Restriccion_se_requerira_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_95b25d -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 29052: aplica_a Restriccion_se_suspende_el_envio_de_informaciones_con_codigo_de_consolidacion_3_con_la_excep_6bac12 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 29054: aplica_a Restriccion_se_tendran_por_no_escritas_las_clausulas_que_coloquen_al_usuario_de_servicios_fi_eeb30b -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 29056: aplica_a Restriccion_se_tendran_por_no_escritas_las_clausulas_que_desnaturalicen_las_obligaciones_del_31b213 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 29058: aplica_a Restriccion_se_tendran_por_no_escritas_las_clausulas_que_impongan_obstaculos_onerosos_para_e_d1d3e6 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 29060: aplica_a Restriccion_se_tendran_por_no_escritas_las_clausulas_que_transfieran_la_responsabilidad_del__c3d654 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 29063: aplica_a Restriccion_sector_privado_no_financiero_demas_categorias_exigencia_de_capital_por_riesgo_es_237c88 -> Sujeto_sector_privado_no_financiero: sin mención
idx 29066: aplica_a Restriccion_si_el_cliente_utiliza_efectivo_el_monto_comprado_por_el_cliente_no_supere_el_equ_76242c -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 29069: aplica_a Restriccion_si_el_cliente_utiliza_efectivo_el_monto_comprado_por_el_cliente_no_supere_el_equ_c870b7 -> Sujeto_persona_humana: sin mención
idx 29072: aplica_a Restriccion_si_el_cuaderno_no_fuere_retirado_personalmente_por_el_titular_de_la_cuenta_el_gi_a67042 -> Sujeto_entidad_girada: sin mención
idx 29075: aplica_a Restriccion_si_el_proveedor_del_exterior_es_una_contraparte_vinculada_con_el_importador_o_se_26144b -> Sujeto_rol_entidad_autorizada_exterior: sin mención
idx 29078: aplica_a Restriccion_si_la_entidad_no_conociera_la_situacion_de_cumplimiento_para_mas_del_5_de_la_pos_7a200f -> Sujeto_rol_alcance_capmin: sin mención
idx 29080: aplica_a Restriccion_si_la_garantia_es_mantenida_por_la_ccp_y_no_esta_protegida_de_su_quiebra_se_le_d_277f3c -> Sujeto_rol_alcance_capmin: sin mención
idx 29082: aplica_a Restriccion_si_se_informa_codigo_554100_xx_no_podran_admitirse_codigos_554210_xx_y_o_554220__35ea57 -> Sujeto_rol_entidad_comprendida_reginf: sin mención
idx 29092: aplica_a Restriccion_si_una_entidad_puede_demostrar_que_en_todos_los_casos_el_cumplimiento_de_las_obl_35d208 -> Sujeto_rol_alcance_capmin: sin mención
idx 29095: aplica_a Restriccion_siendo_aplicable_como_maximo_en_este_caso_el_tipo_de_cambio_vendedor_aplicable_p_3428a0 -> Sujeto_entidad_financiera: sin mención
idx 29098: aplica_a Restriccion_siendo_aplicable_en_este_caso_el_tipo_de_cambio_vendedor_por_canales_electronico_ea3bd3 -> Sujeto_empresa_no_financiera_emisora_de_tarjetas: sin mención
idx 29101: aplica_a Restriccion_sin_deducir_el_100_del_importe_de_la_prevision_por_riesgo_de_incobrabilidad_corr_6afe20 -> Sujeto_rol_alcance_capmin: sin mención
idx 29113: aplica_a Restriccion_sin_deducir_el_100_del_importe_de_la_prevision_por_riesgo_de_incobrabilidad_de_l_690255 -> Sujeto_rol_alcance_capmin: sin mención
idx 29116: aplica_a Restriccion_sin_superar_el_5_de_los_depositos_en_moneda_extranjera_de_la_entidad__polcre_2_1_6844ad -> Sujeto_entidad_financiera: sin mención
idx 29122: aplica_a Restriccion_solo_se_admitiran_calificaciones_globales_internacionales__cap_10_2_3_a62e6c -> Sujeto_rol_alcance_capmin: sin mención
idx 29125: aplica_a Restriccion_solo_se_incluiran_en_el_calculo_de_capital_los_efectos_gamma_netos_que_sean_nega_de40a4 -> Sujeto_rol_alcance_capmin: sin mención
idx 29128: aplica_a Restriccion_solo_se_reconoceran_los_swaps_de_incumplimiento_crediticio_y_de_rendimiento_tota_194a3a -> Sujeto_rol_alcance_capmin: sin mención
idx 29137: aplica_a Restriccion_tasas_de_interes_comisiones_y_o_cargos_sin_el_cumplimiento_de_lo_previsto_en_los_390366 -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 29159: aplica_a Restriccion_titulos_con_tachaduras_o_enmiendas_no_salvadas_por_el_librador_no_valen_como_che_6cda63 -> Sujeto_banco: sin mención
idx 29161: aplica_a Restriccion_titulos_de_credito_titulos_valores_certificados_de_depositos_a_plazo_fijo_y_otro_d77d1c -> Sujeto_rol_alcance_capmin: sin mención
idx 29164: aplica_a Restriccion_toda_consulta_o_reclamo_debera_ser_definitivamente_resuelta_o_dentro_del_plazo_m_a5c93b -> Sujeto_rol_sujeto_obligado_proteccion: sin mención
idx 29166: aplica_a Restriccion_todo_incentivo_economico_que_exceda_lo_previsto_en_las_disposiciones_legales_y_o_7fbc80 -> Sujeto_entidad_financiera: sin mención
idx 29168: aplica_a Restriccion_un_titulo_que_carece_de_la_denominacion_cheque_o_cheque_de_pago_diferido_inserta_83d1e6 -> Sujeto_banco: sin mención
idx 29171: aplica_a Restriccion_un_titulo_que_carezca_de_la_especificacion_de_la_fecha_de_creacion_no_vale_como__afccaa -> Sujeto_banco: sin mención
idx 29176: ejecuta Sujeto_agencia_oficial_de_credito -> Operacion_financiacion_de_importaciones_por_agencia_oficial_6ba0fb: sin mención
idx 29180: ejecuta Sujeto_aseguradora -> Operacion_gestion_de_cobro_por_aseguradora_da7121: sin mención
idx 29181: ejecuta Sujeto_aseguradora -> Operacion_subrogacion_de_derechos_de_cobro_por_aseguradora_8a2df0: sin mención
idx 29183: ejecuta Sujeto_banco -> Operacion_comunicacion_al_bcra_de_rechazos_f744de: sin mención
idx 29184: ejecuta Sujeto_banco -> Operacion_consignacion_de_denominacion_de_cuenta_en_rechazo_259e1a: sin mención
idx 29185: ejecuta Sujeto_banco -> Operacion_debito_de_multas_por_rechazo_de_cheques_3192fb: sin mención
idx 29186: ejecuta Sujeto_banco -> Operacion_desarrollo_aplicacion_reproduccion_firmas_digitalizadas_cbee12: sin mención
idx 29187: ejecuta Sujeto_banco -> Operacion_exclusion_de_central_de_inhabilitados_fab64b: sin mención
idx 29188: ejecuta Sujeto_banco -> Operacion_inclusion_en_central_de_inhabilitados_579dc0: sin mención
idx 29189: ejecuta Sujeto_banco -> Operacion_leyenda_en_devolucion_sin_registrar_647831: sin mención
idx 29190: ejecuta Sujeto_banco -> Operacion_otorgamiento_de_aval_sobre_cheques_diferidos_7593ac: sin mención
idx 29191: ejecuta Sujeto_banco -> Operacion_pago_de_cheque_cruzado_1b1710: sin mención
idx 29192: ejecuta Sujeto_banco -> Operacion_recepcion_de_denuncia_de_extravio_bancaria_213316: sin mención
idx 29193: ejecuta Sujeto_banco -> Operacion_reconocimiento_de_intereses_sobre_saldos_acreedores_ecab11: sin mención
idx 29194: ejecuta Sujeto_banco -> Operacion_registro_de_novedad_en_repositorio_echeq_ab3fde: sin mención
idx 29195: ejecuta Sujeto_banco -> Operacion_utilizacion_de_tecnologia_para_reproduccion_de_firmas_digitalizadas_ec4cc0: sin mención
idx 29201: ejecuta Sujeto_bcra -> Operacion_acreditacion_de_comisiones_en_cuenta_corriente_163a86: sin mención
idx 29202: ejecuta Sujeto_bcra -> Operacion_administracion_de_central_de_cheques_denunciados_extraviados_sustraidos_adultera_901c1c: sin mención
idx 29203: ejecuta Sujeto_bcra -> Operacion_administracion_de_central_de_cheques_rechazados_4daf92: sin mención
idx 29204: ejecuta Sujeto_bcra -> Operacion_administracion_de_central_de_cuentacorrentistas_inhabilitados_ebf3d1: sin mención
idx 29205: ejecuta Sujeto_bcra -> Operacion_apertura_de_cuentas_corrientes_especiales_4a48a2: sin mención
idx 29206: ejecuta Sujeto_bcra -> Operacion_calculo_de_tipos_de_cambio_minoristas_de_referencia_afb412: sin mención
idx 29207: ejecuta Sujeto_bcra -> Operacion_debito_de_cuenta_corriente_ordenes_impagas_972745: sin mención
idx 29208: ejecuta Sujeto_bcra -> Operacion_elaboracion_y_provision_de_nomina_de_deudores_morosos_802e7d: sin mención
idx 29209: ejecuta Sujeto_bcra -> Operacion_modificacion_de_computo_en_central_de_cheques_rechazados_462cd3: sin mención
idx 29210: ejecuta Sujeto_bcra -> Operacion_publicacion_de_uva_y_uvi_2c0786: sin mención
idx 29224: ejecuta Sujeto_cliente -> Operacion_acceso_a_mercado_de_cambios_con_certificacion_ca24a0: sin mención
idx 29225: ejecuta Sujeto_cliente -> Operacion_acreditacion_en_cuentas_en_moneda_extranjera_9a83ed: sin mención
idx 29226: ejecuta Sujeto_cliente -> Operacion_canalizacion_de_operaciones_sml_3daa7e: sin mención
idx 29227: ejecuta Sujeto_cliente -> Operacion_concertacion_de_cambio_sobre_fondos_acreditados_572532: sin mención
idx 29228: ejecuta Sujeto_cliente -> Operacion_reclasificacion_en_tratamiento_especial_por_refinanciacion_0cd96a: sin mención
idx 29229: ejecuta Sujeto_cliente -> Operacion_repatriacion_de_servicios_de_capital_y_rentas_no_residentes_dce0e0: sin mención
idx 29230: ejecuta Sujeto_cliente -> Operacion_suscripcion_bopreal_no_residentes_602ad0: sin mención
idx 29231: ejecuta Sujeto_cliente -> Operacion_suscripcion_de_bonos_bopreal_086e60: sin mención
idx 29238: ejecuta Sujeto_deudor -> Operacion_ingreso_y_liquidacion_de_divisas_en_mercado_de_cambios_a2158d: sin mención
idx 29241: ejecuta Sujeto_ecai -> Operacion_asignacion_de_niveles_de_calidad_crediticia_eaf388: sin mención
idx 29245: ejecuta Sujeto_empresa_no_financiera_emisora_de_tarjetas -> Operacion_imposibilitar_uso_de_productos_servicios_por_medidas_de_seguridad_15e35f: sin mención
idx 29250: ejecuta Sujeto_entidad_cambiaria -> Operacion_posfinanciacion_de_exportaciones_de_bienes_liquidada_f5a9e8: sin mención
idx 29259: ejecuta Sujeto_entidad_depositaria -> Operacion_adulteracion_o_falsificacion_de_cheque_o_firmas_8a9da9: sin mención
idx 29261: ejecuta Sujeto_entidad_financiera -> Operacion_acceso_al_mercado_de_cambios_garantias_financieras_8bb13b: sin mención
idx 29262: ejecuta Sujeto_entidad_financiera -> Operacion_certificacion_de_vinculacion_de_exportaciones_a_proyecto_aprobado_808813: sin mención
idx 29263: ejecuta Sujeto_entidad_financiera -> Operacion_constatacion_de_certificado_de_inversion_para_exportacion_12ea40: sin mención
idx 29264: ejecuta Sujeto_entidad_financiera -> Operacion_designacion_de_entidad_financiera_para_seguimiento_de_proyecto_5890c8: sin mención
idx 29265: ejecuta Sujeto_entidad_financiera -> Operacion_emision_de_certificaciones_de_incremento_de_exportaciones_92fce4: sin mención
idx 29266: ejecuta Sujeto_entidad_financiera -> Operacion_evaluacion_de_codigo_de_gobierno_societario_21418b: sin mención
idx 29267: ejecuta Sujeto_entidad_financiera -> Operacion_financiaciones_comerciales_en_moneda_extranjera_503e01: sin mención
idx 29268: ejecuta Sujeto_entidad_financiera -> Operacion_financiaciones_de_exportaciones_f060f3: sin mención
idx 29269: ejecuta Sujeto_entidad_financiera -> Operacion_imposibilitar_uso_de_productos_servicios_por_medidas_de_seguridad_15e35f: sin mención
idx 29270: ejecuta Sujeto_entidad_financiera -> Operacion_otorgamiento_de_garantias_a_residentes_en_exterior_6fa98b: sin mención
idx 29271: ejecuta Sujeto_entidad_financiera -> Operacion_posfinanciacion_de_exportaciones_de_bienes_liquidada_f5a9e8: sin mención
idx 29272: ejecuta Sujeto_entidad_financiera -> Operacion_prefinanciaciones_de_exportaciones_1e0cb8: sin mención
idx 29273: ejecuta Sujeto_entidad_financiera -> Operacion_registro_ante_bcra_enmarque_financiacion_a9c2a4: sin mención
idx 29274: ejecuta Sujeto_entidad_financiera -> Operacion_registro_y_seguimiento_de_importaciones_de_bienes_de_capital_cec494: sin mención
idx 29275: ejecuta Sujeto_entidad_financiera -> Operacion_revision_periodica_de_estrategias_y_politicas_789cd6: sin mención
idx 29276: ejecuta Sujeto_entidad_financiera -> Operacion_seguimiento_de_actividades_de_gestion_de_riesgos_c5564c: sin mención
idx 29277: ejecuta Sujeto_entidad_financiera -> Operacion_seguimiento_de_fondos_pendientes_de_aplicacion_2bf6f2: sin mención
idx 29278: ejecuta Sujeto_entidad_financiera -> Operacion_seguimiento_de_permisos_de_embarques_71618d: sin mención
idx 29279: ejecuta Sujeto_entidad_financiera -> Operacion_suministro_de_datos_cheques_de_pago_diferido_1e6869: sin mención
idx 29280: ejecuta Sujeto_entidad_financiera -> Operacion_venta_de_divisas_con_debito_en_cuentas_e8a4d4: sin mención
idx 29303: ejecuta Sujeto_entidad_girada -> Operacion_adulteracion_o_falsificacion_de_cheque_o_firmas_8a9da9: sin mención
idx 29304: ejecuta Sujeto_entidad_girada -> Operacion_emision_y_entrega_de_formula_de_certificacion_1dd04d: sin mención
idx 29305: ejecuta Sujeto_entidad_girada -> Operacion_rechazo_de_cheque_con_autorizacion_verbal_422211: sin mención
idx 29306: ejecuta Sujeto_entidad_girada -> Operacion_rechazo_de_cheques_171a7c: sin mención
idx 29307: ejecuta Sujeto_entidad_girada -> Operacion_rechazo_de_registracion_de_cheque_c58de6: sin mención
idx 29308: ejecuta Sujeto_entidad_girada -> Operacion_registracion_de_cheques_9375f0: sin mención
idx 29310: ejecuta Sujeto_entidad_originante_de_transferencia -> Operacion_comunicacion_fehaciente_de_certificaciones_emitidas_9294e5: sin mención
idx 29311: ejecuta Sujeto_entidad_originante_de_transferencia -> Operacion_extension_de_contragarantias_exterior_991c53: sin mención
idx 29313: ejecuta Sujeto_entidad_receptora -> Operacion_acreditacion_de_fondos_en_cuentas_de_corresponsalia_df1e9d: sin mención
idx 29314: ejecuta Sujeto_entidad_receptora -> Operacion_comunicacion_fehaciente_de_certificaciones_emitidas_9294e5: sin mención
idx 29317: ejecuta Sujeto_exportador -> Operacion_acumular_fondos_de_exportaciones_en_cuentas_en_me_dbb31d: sin mención
idx 29319: ejecuta Sujeto_fideicomiso -> Operacion_compra_de_moneda_extranjera_para_garantias_6f3257: sin mención
idx 29332: ejecuta Sujeto_importador -> Operacion_ingreso_de_recuperos_de_seguro_en_mercado_de_cambios_2c2e57: sin mención
idx 29334: ejecuta Sujeto_importador_de_bienes -> Operacion_importacion_posiciones_arancelarias_ncm_8802_f58c9c: sin mención
idx 29335: ejecuta Sujeto_importador_de_bienes -> Operacion_suscripcion_bopreal_por_importadores_d218dc: sin mención
idx 29341: ejecuta Sujeto_mipyme -> Operacion_pago_de_servicios_de_no_residentes_8c6a60: sin mención
idx 29345: ejecuta Sujeto_persona_humana -> Operacion_acceso_al_mercado_cambios_formacion_activos_externos_522a22: sin mención
idx 29346: ejecuta Sujeto_persona_humana -> Operacion_compra_de_moneda_extranjera_para_garantias_6f3257: sin mención
idx 29347: ejecuta Sujeto_persona_humana -> Operacion_denuncia_de_extravio_sustraccion_o_adulteracion_de_cheques_c1dcd4: sin mención
idx 29348: ejecuta Sujeto_persona_humana -> Operacion_extraccion_de_efectivo_en_cajero_automatico_8d8d06: sin mención
idx 29349: ejecuta Sujeto_persona_humana -> Operacion_financiaciones_con_amortizacion_periodica_personas_humanas_07ab20: sin mención
idx 29350: ejecuta Sujeto_persona_humana -> Operacion_operatoria_con_derivados_4f0c87: sin mención
idx 29351: ejecuta Sujeto_persona_humana -> Operacion_pago_de_servicios_de_no_residentes_8c6a60: sin mención
idx 29352: ejecuta Sujeto_persona_humana -> Operacion_remision_de_ayuda_familiar_4f9dc9: sin mención
idx 29354: ejecuta Sujeto_persona_juridica -> Operacion_extraccion_de_efectivo_en_cajero_automatico_8d8d06: sin mención
idx 29387: ejecuta Sujeto_proveedor_no_financiero_de_credito -> Operacion_imposibilitar_uso_de_productos_servicios_por_medidas_de_seguridad_15e35f: sin mención
idx 29398: ejecuta Sujeto_rol_alcance_capmin -> Operacion_asuncion_de_pago_futuro_por_garante_1dd3d0: sin mención
idx 29399: ejecuta Sujeto_rol_alcance_capmin -> Operacion_calculo_de_rpc_mediante_inclusion_diferencia_prevision_niif_9_11f33d: sin mención
idx 29400: ejecuta Sujeto_rol_alcance_capmin -> Operacion_calculo_exigencia_capital_riesgo_precio_opciones_20f1d0: sin mención
idx 29401: ejecuta Sujeto_rol_alcance_capmin -> Operacion_cobertura_de_pagos_por_garantia_b508c3: sin mención
idx 29402: ejecuta Sujeto_rol_alcance_capmin -> Operacion_compra_de_cartera_creditos_minoristas_930297: sin mención
idx 29403: ejecuta Sujeto_rol_alcance_capmin -> Operacion_descubiertos_en_cuenta_corriente_a47c89: sin mención
idx 29404: ejecuta Sujeto_rol_alcance_capmin -> Operacion_determinacion_del_requisito_de_capital_52da79: sin mención
idx 29405: ejecuta Sujeto_rol_alcance_capmin -> Operacion_exclusion_operaciones_discontinuadas_del_bi_3aa389: sin mención
idx 29406: ejecuta Sujeto_rol_alcance_capmin -> Operacion_informe_auditoria_externa_sobre_cumplimiento_iosco_cpmi_74d848: sin mención
idx 29407: ejecuta Sujeto_rol_alcance_capmin -> Operacion_limites_de_compra_tarjeta_de_credito_ade36c: sin mención
idx 29408: ejecuta Sujeto_rol_alcance_capmin -> Operacion_operaciones_con_derivados_cartera_de_negociacion_688397: sin mención
idx 29409: ejecuta Sujeto_rol_alcance_capmin -> Operacion_pago_unico_de_garantia_por_garante_e6925b: sin mención
idx 29410: ejecuta Sujeto_rol_alcance_capmin -> Operacion_ponderacion_de_exposiciones_incumplidas_835d02: sin mención
idx 29411: ejecuta Sujeto_rol_alcance_capmin -> Operacion_prestamos_personales_preacordados_9973c8: sin mención
idx 29412: ejecuta Sujeto_rol_alcance_capmin -> Operacion_provision_informacion_para_computo_exigencia_capital_fondos_garantia_0374fe: sin mención
idx 29413: ejecuta Sujeto_rol_alcance_capmin -> Operacion_reduccion_posiciones_activos_financieros_e9c491: sin mención
idx 29414: ejecuta Sujeto_rol_alcance_capmin -> Operacion_reposicion_de_capital_bc6dc6: sin mención
idx 29415: ejecuta Sujeto_rol_alcance_capmin -> Operacion_rescate_de_instrumento_897ea5: sin mención
idx 29416: ejecuta Sujeto_rol_alcance_capmin -> Operacion_rescate_de_instrumentos_del_ca_450b3b: sin mención
idx 29417: ejecuta Sujeto_rol_alcance_capmin -> Operacion_tenencia_de_efectivo_en_caja_transito_y_cajeros_automaticos_d44d8d: sin mención
idx 29418: ejecuta Sujeto_rol_alcance_capmin -> Operacion_valuacion_a_mercado_o_a_modelo_de_posiciones_8cdc20: sin mención
idx 29419: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_acceso_al_mercado_de_cambios_b8c486: sin mención
idx 29420: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_acceso_al_mercado_de_cambios_fideicomisos_144617: sin mención
idx 29421: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_acceso_al_mercado_de_cambios_importaciones_5a5d0a: sin mención
idx 29422: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_acceso_al_mercado_de_cambios_pago_anticipado_de_importaciones_6dd329: sin mención
idx 29423: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_acceso_mercado_cambios_cancelacion_obligaciones_en_moneda_extranjera_ce63dd: sin mención
idx 29424: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_afectacion_de_registro_aduanero_oficializacion_importacion_sepaimpo_429942: sin mención
idx 29425: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_anticipo_de_exportacion_documentado_en_moneda_de_destino_6f7be4: sin mención
idx 29426: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_aplicacion_cobros_divisas_exportaciones_bienes_8f0c3b: sin mención
idx 29427: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_aplicacion_cobros_exportaciones_servicios_6b5107: sin mención
idx 29428: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_arbitrajes_y_canjes_en_el_exterior_55702f: sin mención
idx 29429: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_boleto_de_venta_de_cambio_bopreal_8e69da: sin mención
idx 29430: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_cancelacion_al_vencimiento_de_endeudamientos_financieros_9a5961: sin mención
idx 29431: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_cancelacion_de_financiaciones_en_moneda_extranjera_669f07: sin mención
idx 29432: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_canjes_y_arbitrajes_con_clientes_4a86e3: sin mención
idx 29433: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_cobro_de_exportacion_documentado_en_moneda_de_destino_eb0227: sin mención
idx 29434: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_cobros_elegibles_mecanismo_7_10_depositados_17536a: sin mención
idx 29435: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_compra_de_moneda_extranjera_anticipada_44812f: sin mención
idx 29436: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_compra_de_moneda_extranjera_garantia_de_servicios_de_deuda_externa_fd8f7c: sin mención
idx 29437: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_compra_de_moneda_extranjera_garantias_de_endeudamiento_c1cc9d: sin mención
idx 29438: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_compra_de_moneda_extranjera_para_garantias_6f3257: sin mención
idx 29439: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_cumplido_de_embarque_permiso_definitivo_c6d27a: sin mención
idx 29440: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_deposito_fondos_en_cuentas_exterior_844127: sin mención
idx 29441: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_emision_de_certificaciones_de_acceso_al_mercado_de_cambios_dfbda2: sin mención
idx 29442: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_extension_plazo_ingreso_liquidacion_divisas_d523f1: sin mención
idx 29443: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_financiacion_comercial_para_importacion_de_bienes_de_capital_110ddf: sin mención
idx 29444: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_financiacion_de_proyectos_inversion_nacional_4e01cd: sin mención
idx 29445: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_financiaciones_asociadas_a_importaciones_de_bienes_a3239b: sin mención
idx 29446: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_giro_de_divisas_al_exterior_utilidades_y_dividendos_bd5c55: sin mención
idx 29447: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_liquidacion_divisas_exportaciones_4d4afa: sin mención
idx 29448: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_operacion_en_mercado_de_cambios_1718c1: sin mención
idx 29449: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_operaciones_cursadas_sml_paraguay_uruguay_1c31f5: sin mención
idx 29450: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_operaciones_de_cambio_de_moneda_extranjera_ff9d15: sin mención
idx 29451: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_operaciones_financiadas_deuda_por_importacion_de_bienes_42fab2: sin mención
idx 29452: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_otorgamiento_de_prorrogas_para_documentacion_aduanera_siniestrada_e60fed: sin mención
idx 29453: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_pago_de_fletes_importacion_s30_8bf9cb: sin mención
idx 29454: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_pago_de_oficializacion_de_importacion_4ef9d5: sin mención
idx 29455: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_pagos_de_capital_deudas_importacion_bienes_hasta_12_12_23_b71be9: sin mención
idx 29456: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_presentacion_documentacion_comercial_por_exportador_668e4c: sin mención
idx 29457: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_reporte_de_cotizaciones_comprador_y_vendedor_c7cc0f: sin mención
idx 29458: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_reporte_en_sepaimpo_de_circunstancias_modificatorias_c5f2ff: sin mención
idx 29459: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_reporte_sepaimpo_afectaciones_despachos_importacion_0286df: sin mención
idx 29460: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_seguimiento_de_oficializaciones_de_importacion_por_entidad_nominada_b653eb: sin mención
idx 29461: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_suscripcion_de_bopreal_a24f7f: sin mención
idx 29462: ejecuta Sujeto_rol_entidad_autorizada_exterior -> Operacion_verificacion_destinacion_exportacion_ante_aduana_94e920: sin mención
idx 29465: ejecuta Sujeto_sefyc -> Operacion_deduccion_de_importes_de_activos_de_rpc_5f0068: sin mención
idx 29476: ejecuta Sujeto_usuario_de_servicios_financieros -> Operacion_presentacion_de_reclamo_ante_bcra_8a05b2: sin mención
idx 29478: ejecuta Sujeto_vpu_rigi -> Operacion_pago_de_capital_adeudado_porcion_compensable_d41f0c: sin mención
idx 29479: ejecuta Sujeto_vpu_rigi -> Operacion_pago_de_intereses_devengados_porcion_compensable_61dd48: sin mención
idx 29480: ejecuta Sujeto_vpu_rigi -> Operacion_precancelacion_de_capital_e_intereses_vpu_rigi_777640: sin mención
```

## Tabla resumen

| Severidad | Regla | Resultado | Resumen |
|---|---|---|---|
| bloqueante | S1 | PASS | 29499/29499 aristas con relación admitida (19 relaciones admitidas); 0 violaciones. |
| bloqueante | S2 | PASS | 0 aristas colgantes sobre 29499. |
| bloqueante | S3 | PASS | 29499/29499 aristas conformes a firma; 0 violaciones. Evaluadas: 15349 por matriz, 14000 remite_a, 126 de esqueleto, 24 padre_sugerido. |
| bloqueante | S4 | PASS | Nodos OK: 8358/8358. Aristas OK: 29499/29499. Violaciones: 0. |
| bloqueante | S5 | PASS | Nodos con punto: 8358/8358. Aristas: 29499/29499. Violaciones: 0. |
| bloqueante | S6 | PASS | Archivos válidos (43): TextoOrdenado ['TO_capitales_minimos_actual.pdf', 'TO_clasificacion_deudores_actual.pdf', 'TO_exterior_cambios_actual.pdf', 'TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'TO_regimen_informativo_contable_mensual_actual.pdf', 'ctacte.pdf', 'docvig.pdf', 'lingob.pdf', 'pagjub.pdf', 'polcre.pdf'] ∪ esqueleto ['actgar.pdf', 'adrei.pdf', 'autenf.pdf', 'catalogo_sujetos_v3.json', 'ccbcra.pdf', 'convca.pdf', 'cryl.pdf', 'ctacor.pdf', 'depaho.pdf', 'efemin.pdf', 'esquema_v2_clases.json', 'esquema_v3_clases.json', 'fabcra.pdf', 'icmecma.pdf', 'lavdin.pdf', 'ordcom.pdf', 'osapsa.pdf', 'pfmipyme.pdf', 'pimf.pdf', 'ratiofn.pdf', 'rdbcra.pdf', 'repefe.pdf', 'retype.pdf', 'rmrtsd.pdf', 'rrci.pdf', 'servco.pdf', 'snp_atm.pdf', 'snp_debin.pdf', 'snp_psp.pdf', 'snp_spd.pdf', 'snp_tr_nc.pdf', 'supcon.pdf', 'traval.pdf']. Violaciones: 0. |
| bloqueante | S15 | PASS | 35 roles, 51 aristas miembro_de; 12 huérfanos (12 declarados, 0 sin declarar); 0 miembros que no son clase. Lista declarada: 12 ({'sin_id_en_catalogo': 6, 'aplanamiento_rechazado': 5, 'instancia_rechazada': 1}). |
| bloqueante | S18 | FAIL | 301 Restricciones limite_cuantitativo: 253 con lista, 22 con el umbral guardado sin lista (marca), 26 sin ninguna. |
| bloqueante | S19 | PASS | 134 Sujetos ({'clase': 70, 'instancia': 5, 'propuesto': 24, 'rol': 35}); catálogo de 110 ids; 0 fuera del catálogo, 0 con nivel inválido, 0 propuestos incompletos. |
| bloqueante | S20 | PASS | 2415 nodos Obligacion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 0. |
| bloqueante | S24 | PASS | 805 nodos Restriccion; 0 violaciones; fuera de lista con marca: 4 {'limite_temporal': 3, 'obligacion_cualitativa': 1}; sin valor: 0. |
| bloqueante | S25 | PASS | 22 nodos Comunicacion; 0 violaciones; fuera de lista con marca: 6 {'otro': 2, 'referencia': 3, 'TO': 1}; sin valor: 1. |
| bloqueante | S26 | PASS | 8224 nodos evaluados; 0 violaciones {}; marcas de nodo admitidas: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']. |
| bloqueante | S28 | PASS | 24 Sujetos propuestos; 48 filas en el registro; 0 propuestos sin fila. |
| bloqueante | S29 | PASS | 24 aristas padre_sugerido; 0 con destino fuera del catálogo único (110 ids). |
| bloqueante | S30 | PASS | 14000 aristas remite_a ({'externa': 949, 'interna': 13021, 'to_entero': 30}); 0 violaciones. |
| bloqueante | S31 | PASS | 14000 aristas remite_a: {'en_un_tramo_del_chunk_de_la_arista': 14000}; 0 violaciones. |
| informativa | S7 | FAIL | 52 grupos violatorios (113 nodos involucrados). |
| informativa | S8 | WARN | 34 grupos con el mismo label normalizado en types distintos. |
| informativa | S9 | PASS | 0 nodos con ambas keys. |
| informativa | S10 | PASS | Sin establecida_en: Condicion=0, Definicion=0, Excepcion=0, Obligacion=0, Operacion=0, Potestad=0, Restriccion=0 (total 0). |
| informativa | S11 | WARN | Sin aplica_a: Excepcion=289, Obligacion=231, Operacion=1506, Potestad=98, Restriccion=207 (total 2331). |
| informativa | S12 | FAIL | 221 Excepciones sin salida exceptua/exceptua_obligacion. |
| informativa | S21 | WARN | 14000 remisiones ({'interna': 13021, 'externa': 949, 'to_entero': 30}); 30 incoherentes (por alcance: {'to_entero': 30}). |
| informativa | S22 | PASS | 24 aristas padre_sugerido; 0 incoherentes (0 con destino distinto, 0 con origen fuera de cuarentena). |
| informativa | S23 | WARN | 3929 aristas aplica_a; 37 hacia Sujetos propuestos (24 destinos distintos). |
| informativa | S27 | WARN | 4086 aristas de sujeto fuera del esqueleto; 4026 sin mención, verificación o método ({'sin_mencion': 4026}). |

**Veredicto global: NO PASA**

## Numeración de las shapes del perfil r2

- S18: Reescrita (L-ESQ-R2 §1.5): Restriccion de tipo limite_cuantitativo => lista de umbrales no vacía o marca (el umbral guardado sin lista: campos_heredados_v3.umbral o properties_no_definidas.umbral). El enunciado de docs/esquema_v2_diseño.md:325 no rige en el perfil r2.
- S24: Enum de Restriccion.tipo (bloqueante salvo la marca fuera_de_lista).
- S25: Enum de Comunicacion.tipo, con «externa» (bloqueante salvo la marca fuera_de_lista).
- S26: Claves cerradas por tipo (bloqueante).
- S27: Arista de sujeto con mención y método (informativa en r2a, bloqueante desde r2b).
- S28: Sujeto propuesto con fila en el registro de no mapeados (bloqueante).
- S29: Destino de padre_sugerido en el catálogo único (bloqueante: U-CAT-UNICO está cerrada).
- S30: alcance de remite_a en la lista cerrada y coherente con los extremos (bloqueante).
- S31: evidencia de remite_a: tramo literal de un único tramo del texto de E0 de su chunk_id (bloqueante; sin --e0, NO COMPUTABLE).
