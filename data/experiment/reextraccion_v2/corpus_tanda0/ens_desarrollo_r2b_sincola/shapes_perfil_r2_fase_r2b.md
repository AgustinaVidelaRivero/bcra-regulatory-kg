# Validador de shapes — perfil r2

- **Grafo:** `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2b_sincola/r2/kg.json`
- **sha256 del grafo:** `2922b72dca2c2bcb204a04f53fc89f265ac2c57e83e6aaab2ce1af8b82d413e4`
- **Fecha:** 2026-10-06
- **Nodos:** 6723
- **Aristas:** 22084
- **Perfil:** r2 (fase r2b)
- **Vocabulario:** `/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/pyd_r2/generados/enums_r2.json` (sha256 `abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241`); marcas de nodo de `/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/pyd_r2/code/modelos_r2.py`: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']
- **Catálogo único (S19, S29):** `/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json` — 110 ids
- **Lista de S15:** `/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json`
- **Registro (S28):** `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2b_sincola/r2/no_mapeados_sujetos.jsonl`
- **E0 (S31):** `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b`
- **Veredicto global: PASA**

## Bloqueantes

### S1 — PASS

Toda arista usa una relación admitida por el perfil r2: los 13 predicados de enums_r2.json ∪ remite_a (enmienda 2 de L-ESQ-R2) ∪ las 4 de esqueleto ∪ padre_sugerido.

**Resultado:** 22084/22084 aristas con relación admitida (19 relaciones admitidas); 0 violaciones.

Sin violaciones.

### S2 — PASS

Integridad referencial: origen y destino de toda arista existen como nodos.

**Resultado:** 0 aristas colgantes sobre 22084.

Sin violaciones.

### S3 — PASS

Toda arista respeta las firmas del perfil r2: matriz ampliada de enums_r2.json (firmas_r2, con condicion_de -> Operacion|Potestad) ∪ remite_a con origen en los siete tipos de contenido y destino en esos siete o TextoOrdenado ∪ esqueleto solo Sujeto->Sujeto ∪ padre_sugerido solo de Sujeto propuesto a Sujeto clase|rol. Una referencia con origen distinto de TextoOrdenado es violación, con o sin rol_fuente.

**Resultado:** 22084/22084 aristas conformes a firma; 0 violaciones. Evaluadas: 10518 por matriz, 11374 remite_a, 126 de esqueleto, 66 padre_sugerido.

Sin violaciones.

### S4 — PASS

Todo nodo y toda arista tienen provenance dict con al menos {to, archivo, punto, rol_documental}, provenances lista no vacía con provenance == provenances[0]; para rol_documental distinto de esqueleto, to y archivo no vacíos (para esqueleto se admiten to nulo, chunk_id nulo y paginas vacía).

**Resultado:** Nodos OK: 6723/6723. Aristas OK: 22084/22084. Violaciones: 0.

Sin violaciones.

### S5 — PASS

Todo provenance.punto (de nodo y de arista) es una string no vacía.

**Resultado:** Nodos con punto: 6723/6723. Aristas: 22084/22084. Violaciones: 0.

Sin violaciones.

### S6 — PASS

Todo provenance.archivo pertenece a {properties.archivo de los nodos TextoOrdenado} ∪ {archivo de las provenances con rol_documental=esqueleto}; nada codificado a mano.

**Resultado:** Archivos válidos (40): TextoOrdenado ['TO_capitales_minimos_actual.pdf', 'TO_clasificacion_deudores_actual.pdf', 'TO_exterior_cambios_actual.pdf', 'TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'TO_regimen_informativo_contable_mensual_actual.pdf'] ∪ esqueleto ['actgar.pdf', 'adrei.pdf', 'autenf.pdf', 'catalogo_sujetos_v3.json', 'ccbcra.pdf', 'convca.pdf', 'cryl.pdf', 'ctacor.pdf', 'depaho.pdf', 'efemin.pdf', 'esquema_v2_clases.json', 'esquema_v3_clases.json', 'fabcra.pdf', 'icmecma.pdf', 'lavdin.pdf', 'lingob.pdf', 'ordcom.pdf', 'osapsa.pdf', 'pagjub.pdf', 'pfmipyme.pdf', 'pimf.pdf', 'ratiofn.pdf', 'rdbcra.pdf', 'repefe.pdf', 'retype.pdf', 'rmrtsd.pdf', 'rrci.pdf', 'servco.pdf', 'snp_atm.pdf', 'snp_debin.pdf', 'snp_psp.pdf', 'snp_spd.pdf', 'snp_tr_nc.pdf', 'supcon.pdf', 'traval.pdf']. Violaciones: 0.

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

**Resultado:** 306 Restricciones limite_cuantitativo: 293 con lista, 13 con el umbral guardado sin lista (marca), 0 sin ninguna.

Sin violaciones.

### S19 — PASS

ERROR — Catálogo de sujetos: todo Sujeto tiene nivel ∈ {clase, instancia, rol, propuesto}; si nivel ≠ propuesto, su id está en el catálogo (clases ∪ roles) del artefacto de --excepciones; si nivel = propuesto, tiene properties.cuarentena y properties.padre_sugerido.

**Resultado:** 176 Sujetos ({'clase': 70, 'instancia': 5, 'propuesto': 66, 'rol': 35}); catálogo de 110 ids; 0 fuera del catálogo, 0 con nivel inválido, 0 propuestos incompletos.

Sin violaciones.

### S20 — PASS

ERROR — Enum de Obligacion.tipo del perfil r2: en la lista o con la marca fuera_de_lista. Lista: {presentacion_informativa|calculo|asignacion|comunicacion_a_cliente|reporte_al_supervisor|otra}.

**Resultado:** 1618 nodos Obligacion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 0.

Sin violaciones.

### S24 — PASS

ERROR — Enum de Restriccion.tipo (bloqueante salvo la marca fuera_de_lista). Lista: {prohibicion|limite_cuantitativo|limite_cualitativo}.

**Resultado:** 633 nodos Restriccion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 0.

Sin violaciones.

### S25 — PASS

ERROR — Enum de Comunicacion.tipo, con «externa» (bloqueante salvo la marca fuera_de_lista). Lista: {A|B|C|externa}.

**Resultado:** 62 nodos Comunicacion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 24.

Sin violaciones.

### S26 — PASS

ERROR — Claves cerradas por tipo: las properties de cada nodo de los nueve tipos están en claves_por_tipo de enums_r2.json o en MARCAS_NODO de modelos_r2.py; lo demás vive en properties_no_definidas.

**Resultado:** 6547 nodos evaluados; 0 violaciones {}; marcas de nodo admitidas: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to'].

Sin violaciones.

### S28 — PASS

ERROR — Sujeto propuesto con fila en el registro de no mapeados (bloqueante).

**Resultado:** 66 Sujetos propuestos; 185 filas en el registro; 0 propuestos sin fila.

Sin violaciones.

### S29 — PASS

ERROR — Destino de padre_sugerido en el catálogo único (bloqueante: U-CAT-UNICO está cerrada).

**Resultado:** 66 aristas padre_sugerido; 0 con destino fuera del catálogo único (110 ids).

Sin violaciones.

### S30 — PASS

ERROR — alcance de remite_a en la lista cerrada y coherente con los extremos (bloqueante). Coherencia: to_entero si el destino es un TextoOrdenado (destino <to>::TO); si no, interna cuando el TO de la unidad citada es el de la procedencia de la arista y externa cuando es otro (enmienda 2 de L-ESQ-R2, §3).

**Resultado:** 11374 aristas remite_a ({'externa': 425, 'interna': 10933, 'to_entero': 16}); 0 violaciones.

Sin violaciones.

### S31 — PASS

ERROR — evidencia de remite_a: tramo literal de un único tramo del texto de E0 de su chunk_id (bloqueante; sin --e0, NO COMPUTABLE). Tramo = el texto propio del chunk o uno de sus tramos heredados, cada uno por separado; nunca la concatenación. Si la evidencia no está en el chunk de provenance, se busca en las otras procedencias de la arista (fusión).

**Resultado:** 11374 aristas remite_a: {'en_un_tramo_del_chunk_de_la_arista': 11374}; 0 violaciones.

Sin violaciones.

### S27 — PASS

ERROR — Arista de sujeto con mención y método (informativa en r2a, bloqueante desde r2b). Fase: r2b.

**Resultado:** 1781 aristas de sujeto fuera del esqueleto; 0 sin mención, verificación o método ({}).

Sin violaciones.

## Informativas

### S7 — FAIL

ERROR — Unicidad exacta: no puede haber dos nodos con el mismo (type, label normalizado).

**Resultado:** 188 grupos violatorios (435 nodos involucrados).

```
[Comunicacion] 'ley de entidades financieras' (2 nodos):
    - Comunicacion_ley_de_entidades_financieras  (label: 'Ley de Entidades Financieras')
    - Comunicacion_ley_de_entidades_financieras__ext  (label: 'Ley de Entidades Financieras')
[Condicion] 'acreditacion de ingresos de divisas en cuenta' (2 nodos):
    - Condicion_acreditacion_de_ingresos_de_divisas_en_cuenta__la_emision_de_certificaciones_est_dff83f  (label: 'Acreditación de ingresos de divisas en cuenta')
    - Condicion_acreditacion_de_ingresos_de_divisas_en_cuenta__se_verifica_cuando_en_la_cuenta_d_bb3229  (label: 'Acreditación de ingresos de divisas en cuenta')
[Condicion] 'beneficiario directo del decreto 277/22' (2 nodos):
    - Condicion_beneficiario_directo_del_decreto_277_22__el_cliente_debe_ser_un_beneficiario_dir_29432c  (label: 'Beneficiario directo del Decreto 277/22')
    - Condicion_beneficiario_directo_del_decreto_277_22__el_cliente_es_un_beneficiario_directo_d_19f443  (label: 'Beneficiario directo del Decreto 277/22')
[Condicion] 'beneficiario sea proveedor exterior' (2 nodos):
    - Condicion_beneficiario_sea_proveedor_exterior__el_beneficiario_del_pago_debe_ser_el_provee_545e13  (label: 'Beneficiario sea proveedor exterior')
    - Condicion_beneficiario_sea_proveedor_exterior__el_beneficiario_del_pago_debe_ser_el_provee_f00722  (label: 'Beneficiario sea proveedor exterior')
[Condicion] 'cancelacion de primera cuota de refinanciacion' (2 nodos):
    - Condicion_cancelacion_de_primera_cuota_de_refinanciacion__se_ha_cancelado_la_primera_cuota_e2b368  (label: 'Cancelación de primera cuota de refinanciación')
    - Condicion_cancelacion_de_primera_cuota_de_refinanciacion__una_vez_que_se_haya_cancelado_la_3675ab  (label: 'Cancelación de primera cuota de refinanciación')
[Condicion] 'cartas de credito emitidas a partir del 13/12/23' (2 nodos):
    - Condicion_cartas_de_credito_emitidas_a_partir_del_13_12_23__cartas_de_credito_o_letras_ava_015c66  (label: 'Cartas de crédito emitidas a partir del 13/12/23')
    - Condicion_cartas_de_credito_emitidas_a_partir_del_13_12_23__condicion_temporal_cartas_de_c_5e4d85  (label: 'Cartas de crédito emitidas a partir del 13/12/23')
[Condicion] 'cartas de credito emitidas a partir del 14/04/25' (2 nodos):
    - Condicion_cartas_de_credito_emitidas_a_partir_del_14_04_25__cartas_de_credito_o_letras_ava_259aa4  (label: 'Cartas de crédito emitidas a partir del 14/04/25')
    - Condicion_cartas_de_credito_emitidas_a_partir_del_14_04_25__condicion_temporal_cartas_de_c_ab23a1  (label: 'Cartas de crédito emitidas a partir del 14/04/25')
[Condicion] 'cliente beneficiario directo decreto 277/22' (3 nodos):
    - Condicion_cliente_beneficiario_directo_decreto_277_22__el_cliente_es_beneficiario_directo__250953  (label: 'Cliente beneficiario directo Decreto 277/22')
    - Condicion_cliente_beneficiario_directo_decreto_277_22__el_cliente_es_un_beneficiario_direc_8f733e  (label: 'Cliente beneficiario directo Decreto 277/22')
    - Condicion_cliente_beneficiario_directo_decreto_277_22__supuesto_en_el_que_el_cliente_es_be_831568  (label: 'Cliente beneficiario directo Decreto 277/22')
[Condicion] 'cliente cuenta con certificacion decreto 277/22' (3 nodos):
    - Condicion_cliente_cuenta_con_certificacion_decreto_277_22__el_cliente_cuenta_con_una_certi_0a1d0e  (label: 'Cliente cuenta con Certificación Decreto 277/22')
    - Condicion_cliente_cuenta_con_certificacion_decreto_277_22__el_cliente_cuenta_con_una_certi_183588  (label: 'Cliente cuenta con Certificación Decreto 277/22')
    - Condicion_cliente_cuenta_con_certificacion_decreto_277_22__el_cliente_cuenta_con_una_certi_868378  (label: 'Cliente cuenta con Certificación Decreto 277/22')
[Condicion] 'cliente es vpu adherido al rigi con declaracion de beneficios' (2 nodos):
    - Condicion_cliente_es_vpu_adherido_al_rigi_con_declaracion_de_beneficios__el_cliente_es_un__2fef4f  (label: 'Cliente es VPU adherido al RIGI con declaración de beneficios')
    - Condicion_cliente_es_vpu_adherido_al_rigi_con_declaracion_de_beneficios__el_cliente_es_un__3b1456  (label: 'Cliente es VPU adherido al RIGI con declaración de beneficios')
[Condicion] 'cliente suscribio bopreal serie 1 minimo 50%' (2 nodos):
    - Condicion_cliente_suscribio_bopreal_serie_1_minimo_50__cliente_que_suscribio_bopreal_serie_857c64  (label: 'Cliente suscribió BOPREAL Serie 1 mínimo 50%')
    - Condicion_cliente_suscribio_bopreal_serie_1_minimo_50__el_cliente_debe_haber_suscrito_bopr_2c91be  (label: 'Cliente suscribió BOPREAL Serie 1 mínimo 50%')
[Condicion] 'cliente vpu adherido al rigi con declaracion de beneficios' (2 nodos):
    - Condicion_cliente_vpu_adherido_al_rigi_con_declaracion_de_beneficios__el_cliente_es_un_veh_ad73e1  (label: 'Cliente VPU adherido al RIGI con declaración de beneficios')
    - Condicion_cliente_vpu_adherido_al_rigi_con_declaracion_de_beneficios__el_cliente_es_un_vpu_33f5a2  (label: 'Cliente VPU adherido al RIGI con declaración de beneficios')
[Condicion] 'cumplimiento de la totalidad de condiciones' (2 nodos):
    - Condicion_cumplimiento_de_la_totalidad_de_condiciones__la_facultad_de_dar_acceso_al_mercad_500658  (label: 'Cumplimiento de la totalidad de condiciones')
    - Condicion_cumplimiento_de_la_totalidad_de_condiciones__la_facultad_de_emitir_las_certifica_ced793  (label: 'Cumplimiento de la totalidad de condiciones')
[Condicion] 'cumplimiento de requisitos aplicables' (3 nodos):
    - Condicion_cumplimiento_de_requisitos_aplicables__la_operacion_se_realiza_en_la_medida_que__266ed7  (label: 'Cumplimiento de requisitos aplicables')
    - Condicion_cumplimiento_de_requisitos_aplicables__se_requiere_el_cumplimiento_de_los_requis_5c1b73  (label: 'Cumplimiento de requisitos aplicables')
    - Condicion_cumplimiento_de_requisitos_aplicables__se_requiere_el_cumplimiento_de_los_requis_ad314b  (label: 'Cumplimiento de requisitos aplicables')
[Condicion] 'cumplimiento de requisitos punto 7.9' (3 nodos):
    - Condicion_cumplimiento_de_requisitos_punto_7_9__se_cumplan_los_requisitos_previstos_en_el__7a682b  (label: 'Cumplimiento de requisitos punto 7.9')
    - Condicion_cumplimiento_de_requisitos_punto_7_9__se_requiere_el_cumplimiento_de_los_requisi_be2d9d  (label: 'Cumplimiento de requisitos punto 7.9')
    - Condicion_cumplimiento_de_requisitos_punto_7_9__se_requiere_el_cumplimiento_de_los_requisi_ce134d  (label: 'Cumplimiento de requisitos punto 7.9')
[Condicion] 'cumplimiento requisitos aplicables' (2 nodos):
    - Condicion_cumplimiento_requisitos_aplicables__la_facultad_de_acceder_al_mercado_de_cambios_5d8a1f  (label: 'Cumplimiento requisitos aplicables')
    - Condicion_cumplimiento_requisitos_aplicables__se_requiere_el_cumplimiento_de_los_requisito_8416a8  (label: 'Cumplimiento requisitos aplicables')
[Condicion] 'cumplimiento requisitos complementarios 3.16.1 a 3.16.4' (2 nodos):
    - Condicion_cumplimiento_requisitos_complementarios_3_16_1_a_3_16_4__el_cliente_debe_cumplir_7a1075  (label: 'Cumplimiento requisitos complementarios 3.16.1 a 3.16.4')
    - Condicion_cumplimiento_requisitos_complementarios_3_16_1_a_3_16_4__el_cliente_debe_cumplir_9b16ba  (label: 'Cumplimiento requisitos complementarios 3.16.1 a 3.16.4')
[Condicion] 'cumplimiento totalidad condiciones siguientes' (2 nodos):
    - Condicion_cumplimiento_totalidad_condiciones_siguientes__la_excepcion_se_aplica_cuando_se__f2a37e  (label: 'Cumplimiento totalidad condiciones siguientes')
    - Condicion_cumplimiento_totalidad_condiciones_siguientes__se_requiere_el_cumplimiento_de_la_ed6360  (label: 'Cumplimiento totalidad condiciones siguientes')
[Condicion] 'declaracion en relevamiento de activos y pasivos externos' (4 nodos):
    - Condicion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__el_pasivo_debe_encont_0ad9a0  (label: 'Declaración en Relevamiento de activos y pasivos externos')
    - Condicion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__la_entidad_debe_conta_ab8dfd  (label: 'Declaración en Relevamiento de activos y pasivos externos')
    - Condicion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__la_operacion_debe_enc_4ca3b2  (label: 'Declaración en Relevamiento de activos y pasivos externos')
    - Condicion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__la_operacion_debe_enc_e95286  (label: 'Declaración en Relevamiento de activos y pasivos externos')
[Condicion] 'declaracion jurada del exportador' (5 nodos):
    - Condicion_declaracion_jurada_del_exportador__contar_con_una_declaracion_jurada_del_exporta_9beeeb  (label: 'Declaración jurada del exportador')
    - Condicion_declaracion_jurada_del_exportador__el_exportador_debe_presentar_una_declaracion__b44efd  (label: 'Declaración jurada del exportador')
    - Condicion_declaracion_jurada_del_exportador__la_entidad_debe_contar_con_una_declaracion_ju_774452  (label: 'Declaración jurada del exportador')
    - Condicion_declaracion_jurada_del_exportador__la_entidad_debe_contar_con_una_declaracion_ju_f12e52  (label: 'Declaración jurada del exportador')
    - Condicion_declaracion_jurada_del_exportador__la_entidad_interviniente_debe_contar_con_una__62bd5a  (label: 'Declaración jurada del exportador')
[Condicion] 'direccion incompetente y/o deshonesta' (2 nodos):
    - Condicion_direccion_incompetente_y_o_deshonesta__el_cliente_cuenta_con_una_direccion_incom_165de4  (label: 'Dirección incompetente y/o deshonesta')
    - Condicion_direccion_incompetente_y_o_deshonesta__el_cliente_cuenta_con_una_direccion_que_e_3e2288  (label: 'Dirección incompetente y/o deshonesta')
[Condicion] 'disponibilidad de documentacion verificadora' (2 nodos):
    - Condicion_disponibilidad_de_documentacion_verificadora__la_emision_de_certificaciones_esta_c4268d  (label: 'Disponibilidad de documentación verificadora')
    - Condicion_disponibilidad_de_documentacion_verificadora__la_entidad_debe_contar_con_la_docu_abd794  (label: 'Disponibilidad de documentación verificadora')
[Condicion] 'distribucion determinada por asamblea de accionistas' (2 nodos):
    - Condicion_distribucion_determinada_por_asamblea_de_accionistas__la_distribucion_debe_ser_d_f35055  (label: 'Distribución determinada por asamblea de accionistas')
    - Condicion_distribucion_determinada_por_asamblea_de_accionistas__la_suscripcion_de_bopreal__4bc39e  (label: 'Distribución determinada por asamblea de accionistas')
[Condicion] 'documentacion de cumplimiento de condiciones al otorgamiento' (2 nodos):
    - Condicion_documentacion_de_cumplimiento_de_condiciones_al_otorgamiento__la_entidad_debe_co_3fd638  (label: 'Documentación de cumplimiento de condiciones al otorgamiento')
    - Condicion_documentacion_de_cumplimiento_de_condiciones_al_otorgamiento__la_entidad_debe_co_6e2119  (label: 'Documentación de cumplimiento de condiciones al otorgamiento')
[Condicion] 'elegibilidad segun punto 4.4' (2 nodos):
    - Condicion_elegibilidad_segun_punto_4_4__la_operacion_debe_ser_elegible_de_acuerdo_con_lo_d_97b1bb  (label: 'Elegibilidad según punto 4.4')
    - Condicion_elegibilidad_segun_punto_4_4__los_pagos_deben_resultar_elegibles_de_acuerdo_con__24608a  (label: 'Elegibilidad según punto 4.4')
[Condicion] 'elegibilidad segun punto 4.5' (2 nodos):
    - Condicion_elegibilidad_segun_punto_4_5__la_operacion_debe_resultar_elegible_de_acuerdo_con_01f3cb  (label: 'Elegibilidad según punto 4.5')
    - Condicion_elegibilidad_segun_punto_4_5__la_operacion_debe_ser_elegible_de_acuerdo_con_lo_d_fe9d8d  (label: 'Elegibilidad según punto 4.5')
[Condicion] 'elegibilidad segun punto 4.6.1' (2 nodos):
    - Condicion_elegibilidad_segun_punto_4_6_1__la_operacion_es_elegible_conforme_a_lo_estableci_4cf167  (label: 'Elegibilidad según punto 4.6.1')
    - Condicion_elegibilidad_segun_punto_4_6_1__los_dividendos_deben_ser_elegibles_de_acuerdo_co_faa83e  (label: 'Elegibilidad según punto 4.6.1')
[Condicion] 'elegibilidad segun punto 4.6.2' (2 nodos):
    - Condicion_elegibilidad_segun_punto_4_6_2__la_repatriacion_de_inversiones_de_portafolio_est_5f70fa  (label: 'Elegibilidad según punto 4.6.2')
    - Condicion_elegibilidad_segun_punto_4_6_2__las_inversiones_debian_resultar_elegibles_de_acu_86fe1d  (label: 'Elegibilidad según punto 4.6.2')
[Condicion] 'elegibilidad segun punto 4.7' (2 nodos):
    - Condicion_elegibilidad_segun_punto_4_7__las_contrapartes_vinculadas_deben_resultar_elegibl_c54b88  (label: 'Elegibilidad según punto 4.7')
    - Condicion_elegibilidad_segun_punto_4_7__los_pagos_deben_resultar_elegibles_de_acuerdo_con__79985c  (label: 'Elegibilidad según punto 4.7')
[Condicion] 'endeudamiento financiero comprendido en 3.5.' (2 nodos):
    - Condicion_endeudamiento_financiero_comprendido_en_3_5__el_acto_regulado_es_un_endeudamient_7f4096  (label: 'Endeudamiento financiero comprendido en 3.5.')
    - Condicion_endeudamiento_financiero_comprendido_en_3_5__el_endeudamiento_debe_estar_compren_af610f  (label: 'Endeudamiento financiero comprendido en 3.5.')
[Condicion] 'incidencia de situacion de contrapartes conectadas' (2 nodos):
    - Condicion_incidencia_de_situacion_de_contrapartes_conectadas__debe_tenerse_en_cuenta_la_ev_5b0779  (label: 'Incidencia de situación de contrapartes conectadas')
    - Condicion_incidencia_de_situacion_de_contrapartes_conectadas__en_el_analisis_debe_consider_c8dae0  (label: 'Incidencia de situación de contrapartes conectadas')
[Condicion] 'informacion inconsistente y desactualizada' (2 nodos):
    - Condicion_informacion_inconsistente_y_desactualizada__la_informacion_no_es_consistente_y_n_0aa68c  (label: 'Información inconsistente y desactualizada')
    - Condicion_informacion_inconsistente_y_desactualizada__la_informacion_no_es_consistente_y_n_7769e4  (label: 'Información inconsistente y desactualizada')
[Condicion] 'insolvencia posterior del importador extranjero' (2 nodos):
    - Condicion_insolvencia_posterior_del_importador_extranjero__el_importador_extranjero_ha_cai_4ff7f8  (label: 'Insolvencia posterior del importador extranjero')
    - Condicion_insolvencia_posterior_del_importador_extranjero__el_importador_extranjero_ha_cai_bb2bf6  (label: 'Insolvencia posterior del importador extranjero')
[Condicion] 'liquidacion en mercado de cambios' (2 nodos):
    - Condicion_liquidacion_en_mercado_de_cambios__la_financiacion_debe_estar_liquidada_en_el_me_699493  (label: 'Liquidación en mercado de cambios')
    - Condicion_liquidacion_en_mercado_de_cambios__los_titulos_de_deuda_deben_haber_sido_liquida_7e9594  (label: 'Liquidación en mercado de cambios')
[Condicion] 'monto supera usd 25.000' (4 nodos):
    - Condicion_monto_supera_usd_25_000__condicion_el_monto_a_imputar_al_permiso_supera_usd_25_0_57a82d  (label: 'Monto supera USD 25.000')
    - Condicion_monto_supera_usd_25_000__el_monto_a_imputar_al_permiso_por_este_mecanismo_supera_bd2c71  (label: 'Monto supera USD 25.000')
    - Condicion_monto_supera_usd_25_000__el_monto_a_imputar_al_permiso_por_este_mecanismo_supera_df4671  (label: 'Monto supera USD 25.000')
    - Condicion_monto_supera_usd_25_000__el_monto_a_imputar_al_permiso_por_este_mecanismo_supera_eaf179  (label: 'Monto supera USD 25.000')
[Condicion] 'no utilizacion previa del mecanismo' (2 nodos):
    - Condicion_no_utilizacion_previa_del_mecanismo__el_cliente_no_debe_haber_utilizado_ya_este__baacf3  (label: 'No utilización previa del mecanismo')
    - Condicion_no_utilizacion_previa_del_mecanismo__el_cliente_no_ha_utilizado_previamente_este_e76df4  (label: 'No utilización previa del mecanismo')
[Condicion] 'nuevo titulo con 1 ano de gracia y vida promedio mayor' (2 nodos):
    - Condicion_nuevo_titulo_con_1_ano_de_gracia_y_vida_promedio_mayor__el_nuevo_titulo_de_deuda_27d799  (label: 'Nuevo título con 1 año de gracia y vida promedio mayor')
    - Condicion_nuevo_titulo_con_1_ano_de_gracia_y_vida_promedio_mayor__el_nuevo_titulo_de_deuda_adb2f3  (label: 'Nuevo título con 1 año de gracia y vida promedio mayor')
[Condicion] 'observancia de criterios punto 8.3.5' (2 nodos):
    - Condicion_observancia_de_criterios_punto_8_3_5__la_inclusion_debe_observar_los_criterios_e_68ddba  (label: 'Observancia de criterios punto 8.3.5')
    - Condicion_observancia_de_criterios_punto_8_3_5__se_deben_observar_los_criterios_establecid_04fb97  (label: 'Observancia de criterios punto 8.3.5')
[Condicion] 'observancia de requisitos especificados' (2 nodos):
    - Condicion_observancia_de_requisitos_especificados__se_deben_observar_los_requisitos_que_se_399422  (label: 'Observancia de requisitos especificados')
    - Condicion_observancia_de_requisitos_especificados__se_requiere_la_observancia_de_los_requi_249979  (label: 'Observancia de requisitos especificados')
[Condicion] 'operacion declarada en presentacion vencida de relevamiento' (2 nodos):
    - Condicion_operacion_declarada_en_presentacion_vencida_de_relevamiento__la_operacion_debe_e_501d96  (label: 'Operación declarada en presentación vencida de Relevamiento')
    - Condicion_operacion_declarada_en_presentacion_vencida_de_relevamiento__la_operacion_debe_e_79ea4c  (label: 'Operación declarada en presentación vencida de Relevamiento')
[Condicion] 'operacion declarada en relevamiento de activos y pasivos externos' (2 nodos):
    - Condicion_operacion_declarada_en_relevamiento_de_activos_y_pasivos_externos__la_operacion__545007  (label: 'Operación declarada en Relevamiento de activos y pasivos externos')
    - Condicion_operacion_declarada_en_relevamiento_de_activos_y_pasivos_externos__la_operacion__ae505a  (label: 'Operación declarada en Relevamiento de activos y pasivos externos')
[Condicion] 'operacion no comprendida en punto 10.10.2.11' (2 nodos):
    - Condicion_operacion_no_comprendida_en_punto_10_10_2_11__salvo_que_la_operacion_quedase_com_8c7dd2  (label: 'Operación no comprendida en punto 10.10.2.11')
    - Condicion_operacion_no_comprendida_en_punto_10_10_2_11__salvo_que_la_operacion_quedase_com_8fa9cf  (label: 'Operación no comprendida en punto 10.10.2.11')
[Condicion] 'pago cancelacion deudas operaciones financiadas/garantizadas' (3 nodos):
    - Condicion_pago_cancelacion_deudas_operaciones_financiadas_garantizadas__el_pago_correspond_eda573  (label: 'Pago cancelación deudas operaciones financiadas/garantizadas')
    - Condicion_pago_cancelacion_deudas_operaciones_financiadas_garantizadas__el_pago_debe_corre_151cb4  (label: 'Pago cancelación deudas operaciones financiadas/garantizadas')
    - Condicion_pago_cancelacion_deudas_operaciones_financiadas_garantizadas__el_pago_debe_corre_8357d9  (label: 'Pago cancelación deudas operaciones financiadas/garantizadas')
[Condicion] 'pago en marco punto 4.8.4' (2 nodos):
    - Condicion_pago_en_marco_punto_4_8_4__el_pago_debe_ser_concretado_en_el_marco_de_lo_dispues_f24aab  (label: 'Pago en marco punto 4.8.4')
    - Condicion_pago_en_marco_punto_4_8_4__el_pago_se_concreta_en_el_marco_de_lo_dispuesto_en_el_eaff85  (label: 'Pago en marco punto 4.8.4')
[Condicion] 'pago en marco punto 4.8.5' (2 nodos):
    - Condicion_pago_en_marco_punto_4_8_5__el_pago_debe_ser_concretado_en_el_marco_de_lo_dispues_6539aa  (label: 'Pago en marco punto 4.8.5')
    - Condicion_pago_en_marco_punto_4_8_5__el_pago_se_concreta_en_el_marco_de_lo_dispuesto_en_el_e3769a  (label: 'Pago en marco punto 4.8.5')
[Condicion] 'pago mediante canje y/o arbitraje con fondos bopreal' (2 nodos):
    - Condicion_pago_mediante_canje_y_o_arbitraje_con_fondos_bopreal__el_pago_se_concreta_median_708a9d  (label: 'Pago mediante canje y/o arbitraje con fondos BOPREAL')
    - Condicion_pago_mediante_canje_y_o_arbitraje_con_fondos_bopreal__el_pago_se_realiza_mediant_1678c1  (label: 'Pago mediante canje y/o arbitraje con fondos BOPREAL')
[Condicion] 'pagos con ingreso aduanero pendiente' (2 nodos):
    - Condicion_pagos_con_ingreso_aduanero_pendiente__cuando_los_pagos_tengan_registro_de_ingres_7fd651  (label: 'Pagos con ingreso aduanero pendiente')
    - Condicion_pagos_con_ingreso_aduanero_pendiente__cuando_se_trate_de_pagos_con_registro_de_i_41bb72  (label: 'Pagos con ingreso aduanero pendiente')
[Condicion] 'pertenencia a grupos a, b o c' (2 nodos):
    - Condicion_pertenencia_a_grupos_a_b_o_c__la_entidad_del_grupo_2_debe_pertenecer_a_los_grupo_923379  (label: 'Pertenencia a Grupos A, B o C')
    - Condicion_pertenencia_a_grupos_a_b_o_c__la_entidad_financiera_del_grupo_2_pertenece_a_los__ecdd7c  (label: 'Pertenencia a Grupos A, B o C')
[Condicion] 'plazo minimo 2 anos desde liquidacion' (2 nodos):
    - Condicion_plazo_minimo_2_anos_desde_liquidacion__el_acceso_al_mercado_de_cambios_debe_prod_b5e2b2  (label: 'Plazo mínimo 2 años desde liquidación')
    - Condicion_plazo_minimo_2_anos_desde_liquidacion__el_acceso_al_mercado_de_cambios_debe_prod_bbaa57  (label: 'Plazo mínimo 2 años desde liquidación')
[Condicion] 'refinanciacion con quitas de capital' (2 nodos):
    - Condicion_refinanciacion_con_quitas_de_capital__el_cliente_ha_refinanciado_su_deuda_con_ot_8bb55e  (label: 'Refinanciación con quitas de capital')
    - Condicion_refinanciacion_con_quitas_de_capital__el_deudor_ha_refinanciado_su_deuda_con_oto_15e025  (label: 'Refinanciación con quitas de capital')
[Condicion] 'servicios prestados a partir del 13/12/23' (3 nodos):
    - Condicion_servicios_prestados_a_partir_del_13_12_23__la_condicion_se_aplica_cuando_los_ser_3682b4  (label: 'Servicios prestados a partir del 13/12/23')
    - Condicion_servicios_prestados_a_partir_del_13_12_23__la_operacion_debe_corresponder_a_serv_98cf43  (label: 'Servicios prestados a partir del 13/12/23')
    - Condicion_servicios_prestados_a_partir_del_13_12_23__los_servicios_deben_haber_sido_o_sera_a5012d  (label: 'Servicios prestados a partir del 13/12/23')
[Condicion] 'sistema de informacion inadecuado' (2 nodos):
    - Condicion_sistema_de_informacion_inadecuado__el_cliente_tiene_un_sistema_de_informacion_in_0fc1d9  (label: 'Sistema de información inadecuado')
    - Condicion_sistema_de_informacion_inadecuado__el_cliente_tiene_un_sistema_de_informacion_in_b6dd83  (label: 'Sistema de información inadecuado')
[Condicion] 'solicitud de aplicacion a permisos de embarque' (3 nodos):
    - Condicion_solicitud_de_aplicacion_a_permisos_de_embarque__el_exportador_solicita_la_aplica_4b172d  (label: 'Solicitud de aplicación a permisos de embarque')
    - Condicion_solicitud_de_aplicacion_a_permisos_de_embarque__el_exportador_solicita_la_aplica_60121b  (label: 'Solicitud de aplicación a permisos de embarque')
    - Condicion_solicitud_de_aplicacion_a_permisos_de_embarque__el_exportador_solicita_la_aplica_6e5905  (label: 'Solicitud de aplicación a permisos de embarque')
[Condicion] 'verificacion de condiciones enumeradas' (2 nodos):
    - Condicion_verificacion_de_condiciones_enumeradas__cuando_se_verifique_alguna_de_las_siguie_2b9899  (label: 'Verificación de condiciones enumeradas')
    - Condicion_verificacion_de_condiciones_enumeradas__se_verifiquen_las_siguientes_condiciones_816657  (label: 'Verificación de condiciones enumeradas')
[Condicion] 'verificacion de condiciones punto 9.3.1' (2 nodos):
    - Condicion_verificacion_de_condiciones_punto_9_3_1__se_debe_verificar_las_condiciones_indic_270f55  (label: 'Verificación de condiciones punto 9.3.1')
    - Condicion_verificacion_de_condiciones_punto_9_3_1__verificacion_de_las_condiciones_indicad_ef95b9  (label: 'Verificación de condiciones punto 9.3.1')
[Condicion] 'verificacion de condiciones punto 9.3.1.' (2 nodos):
    - Condicion_verificacion_de_condiciones_punto_9_3_1__se_verifica_el_cumplimiento_de_las_cond_fd8ef2  (label: 'Verificación de condiciones punto 9.3.1.')
    - Condicion_verificacion_de_condiciones_punto_9_3_1__se_verifiquen_las_condiciones_indicadas_c3f73a  (label: 'Verificación de condiciones punto 9.3.1.')
[Condicion] 'verificacion previa de cumplimiento de requisitos' (3 nodos):
    - Condicion_verificacion_previa_de_cumplimiento_de_requisitos__la_entidad_debe_verificar_pre_22143f  (label: 'Verificación previa de cumplimiento de requisitos')
    - Condicion_verificacion_previa_de_cumplimiento_de_requisitos__se_debe_verificar_previamente_9ea1c6  (label: 'Verificación previa de cumplimiento de requisitos')
    - Condicion_verificacion_previa_de_cumplimiento_de_requisitos__se_verifica_previamente_que_s_df31a0  (label: 'Verificación previa de cumplimiento de requisitos')
[Condicion] 'verificacion previa de requisitos para acceso al mercado' (2 nodos):
    - Condicion_verificacion_previa_de_requisitos_para_acceso_al_mercado__el_acceso_al_mercado_d_dd2815  (label: 'Verificación previa de requisitos para acceso al mercado')
    - Condicion_verificacion_previa_de_requisitos_para_acceso_al_mercado__la_entidad_intervinien_340d50  (label: 'Verificación previa de requisitos para acceso al mercado')
[Condicion] 'vida promedio del nuevo endeudamiento mayor a remanente' (2 nodos):
    - Condicion_vida_promedio_del_nuevo_endeudamiento_mayor_a_remanente__la_vida_promedio_del_nu_97f3de  (label: 'Vida promedio del nuevo endeudamiento mayor a remanente')
    - Condicion_vida_promedio_del_nuevo_endeudamiento_mayor_a_remanente__la_vida_promedio_del_nu_98c541  (label: 'Vida promedio del nuevo endeudamiento mayor a remanente')
[Condicion] 'vida promedio minima 2 anos' (2 nodos):
    - Condicion_vida_promedio_minima_2_anos__el_endeudamiento_financiero_debe_tener_una_vida_pro_6cc9a5  (label: 'Vida promedio mínima 2 años')
    - Condicion_vida_promedio_minima_2_anos__la_emision_de_titulos_de_deuda_debe_tener_una_vida__bcbb90  (label: 'Vida promedio mínima 2 años')
[Condicion] 'vida promedio no inferior a 2 anos' (3 nodos):
    - Condicion_vida_promedio_no_inferior_a_2_anos__el_endeudamiento_debe_tener_una_vida_promedi_3b6df4  (label: 'Vida promedio no inferior a 2 años')
    - Condicion_vida_promedio_no_inferior_a_2_anos__el_endeudamiento_debe_tener_una_vida_promedi_a483e4  (label: 'Vida promedio no inferior a 2 años')
    - Condicion_vida_promedio_no_inferior_a_2_anos__la_vida_promedio_del_endeudamiento_debe_ser__32a8ca  (label: 'Vida promedio no inferior a 2 años')
[Condicion] 'vida promedio nuevos titulos mayor a remanente' (2 nodos):
    - Condicion_vida_promedio_nuevos_titulos_mayor_a_remanente__la_vida_promedio_de_los_nuevos_t_32e6df  (label: 'Vida promedio nuevos títulos mayor a remanente')
    - Condicion_vida_promedio_nuevos_titulos_mayor_a_remanente__la_vida_promedio_de_los_nuevos_t_a2c7dc  (label: 'Vida promedio nuevos títulos mayor a remanente')
[Condicion] 'vigencia requisito conformidad previa bcra' (2 nodos):
    - Condicion_vigencia_requisito_conformidad_previa_bcra__condicion_de_vigencia_del_requisito__345191  (label: 'Vigencia requisito conformidad previa BCRA')
    - Condicion_vigencia_requisito_conformidad_previa_bcra__la_condicion_de_que_el_requisito_de__e1da5b  (label: 'Vigencia requisito conformidad previa BCRA')
[Definicion] 'activos ponderados por riesgo de credito (apr)' (2 nodos):
    - Definicion_activos_ponderados_por_riesgo_de_credito_apr__activos_ponderados_por_riesgo_de_c_72d0cd  (label: 'Activos ponderados por riesgo de crédito (APR)')
    - Definicion_activos_ponderados_por_riesgo_de_credito_apr__activos_ponderados_por_riesgo_de_c_787f47  (label: 'Activos ponderados por riesgo de crédito (APR)')
[Definicion] 'bi — indicador de negocio' (3 nodos):
    - Definicion_bi_indicador_de_negocio__aproximacion_al_riesgo_operacional_a_partir_de_la_infor_0d34b3  (label: 'BI — Indicador de negocio')
    - Definicion_bi_indicador_de_negocio__indicador_de_negocio_codigo_34000000__ric_5_2_2_07b8b4  (label: 'BI — Indicador de negocio')
    - Definicion_bi_indicador_de_negocio__valor_absoluto_de_la_suma_de_los_componentes_intereses__df8c59  (label: 'BI — indicador de negocio')
[Definicion] 'bic — componente del indicador de negocio' (2 nodos):
    - Definicion_bic_componente_del_indicador_de_negocio__componente_del_indicador_de_negocio_cal_eb7c58  (label: 'BIC — componente del indicador de negocio')
    - Definicion_bic_componente_del_indicador_de_negocio__componente_del_indicador_de_negocio_que_1eff58  (label: 'BIC — componente del indicador de negocio')
[Definicion] 'costo de reposicion (cr)' (2 nodos):
    - Definicion_costo_de_reposicion_cr__costo_de_reposicion_calculado_de_acuerdo_con_el_punto_4__8bc247  (label: 'Costo de reposición (CR)')
    - Definicion_costo_de_reposicion_cr__exposicion_presente_respecto_de_la_contraparte_que_no_pu_8e6a24  (label: 'Costo de reposición (CR)')
[Definicion] 'cuit del importador' (2 nodos):
    - Definicion_cuit_del_importador__dato_que_debe_constar_en_la_certificacion_que_emite_la_enti_378896  (label: 'CUIT del importador')
    - Definicion_cuit_del_importador__dato_que_debe_constar_en_la_certificacion_que_emite_la_enti_774f59  (label: 'CUIT del importador')
[Definicion] 'deuda comercial por importacion de bienes' (2 nodos):
    - Definicion_deuda_comercial_por_importacion_de_bienes__a_los_efectos_del_acceso_al_mercado_d_cba64f  (label: 'Deuda comercial por importación de bienes')
    - Definicion_deuda_comercial_por_importacion_de_bienes__pagos_por_deudas_originadas_en_import_0bb51b  (label: 'Deuda comercial por importación de bienes')
[Definicion] 'deuda comercial por importacion — financiacion local' (2 nodos):
    - Definicion_deuda_comercial_por_importacion_financiacion_local__financiacion_a_cualquier_pla_02134d  (label: 'Deuda comercial por importación — financiación local')
    - Definicion_deuda_comercial_por_importacion_financiacion_local__financiacion_a_cualquier_pla_d3ba4b  (label: 'Deuda comercial por importación — financiación local')
[Definicion] 'factor de conversion crediticia (ccf)' (2 nodos):
    - Definicion_factor_de_conversion_crediticia_ccf__factor_de_conversion_crediticia__cap_2_1_294f90  (label: 'Factor de conversión crediticia (CCF)')
    - Definicion_factor_de_conversion_crediticia_ccf__factor_de_conversion_crediticia_con_valores_7be7d4  (label: 'Factor de conversión crediticia (CCF)')
[Definicion] 'fc — componente financiero' (4 nodos):
    - Definicion_fc_componente_financiero__componente_financiero__ric_5_1_1_930f4f  (label: 'FC — componente financiero')
    - Definicion_fc_componente_financiero__componente_financiero_determinado_como_va_resultado_ne_64f088  (label: 'FC — Componente financiero')
    - Definicion_fc_componente_financiero__componente_financiero_prom_codigo_34300000__ric_5_2_2_c0e1b0  (label: 'FC — Componente financiero')
    - Definicion_fc_componente_financiero__comprende_a_resultado_neto_de_la_cartera_de_negociacio_f4af7c  (label: 'FC — Componente financiero')
[Definicion] 'ildc — componente de intereses, arrendamientos y dividendos' (4 nodos):
    - Definicion_ildc_componente_de_intereses_arrendamientos_y_dividendos__componente_de_interese_03b890  (label: 'ILDC — Componente de intereses, arrendamientos y dividendos')
    - Definicion_ildc_componente_de_intereses_arrendamientos_y_dividendos__componente_de_interese_082f66  (label: 'ILDC — Componente de intereses, arrendamientos y dividendos')
    - Definicion_ildc_componente_de_intereses_arrendamientos_y_dividendos__componente_de_interese_f9adf6  (label: 'ILDC — componente de intereses, arrendamientos y dividendos')
    - Definicion_ildc_componente_de_intereses_arrendamientos_y_dividendos__comprende_a_ingresos_p_db33a2  (label: 'ILDC — Componente de intereses, arrendamientos y dividendos')
[Definicion] 'ilm — multiplicador de perdida interna' (2 nodos):
    - Definicion_ilm_multiplicador_de_perdida_interna__multiplicador_de_perdida_interna_igual_a_1_637ff5  (label: 'ILM — multiplicador de pérdida interna')
    - Definicion_ilm_multiplicador_de_perdida_interna__multiplicador_de_perdida_interna_igual_a_1_ecdf0e  (label: 'ILM — multiplicador de pérdida interna')
[Definicion] 'informacion requerida en certificacion' (2 nodos):
    - Definicion_informacion_requerida_en_certificacion__dato_que_debe_constar_en_la_certificacio_7ae5ac  (label: 'Información requerida en certificación')
    - Definicion_informacion_requerida_en_certificacion__dato_que_debe_constar_en_la_certificacio_7bcff8  (label: 'Información requerida en certificación')
[Definicion] 'operaciones de entrega contra pago fallidas (dvp)' (2 nodos):
    - Definicion_operaciones_de_entrega_contra_pago_fallidas_dvp__operaciones_de_entrega_contra_p_9dcdd6  (label: 'Operaciones de entrega contra pago fallidas (DvP)')
    - Definicion_operaciones_de_entrega_contra_pago_fallidas_dvp__operaciones_de_entrega_contra_p_ba01c6  (label: 'Operaciones de entrega contra pago fallidas (DvP)')
[Definicion] 'operaciones sin entrega contra pago (no dvp)' (2 nodos):
    - Definicion_operaciones_sin_entrega_contra_pago_no_dvp__operaciones_sin_entrega_contra_pago__6265de  (label: 'Operaciones sin entrega contra pago (no DvP)')
    - Definicion_operaciones_sin_entrega_contra_pago_no_dvp__operaciones_sin_entrega_contra_pago__6ca06b  (label: 'Operaciones sin entrega contra pago (no DvP)')
[Definicion] 'partidas fuera de balance (pfb)' (3 nodos):
    - Definicion_partidas_fuera_de_balance_pfb__medida_de_la_exposicion_identificada_con_codigo_4_6ae08f  (label: 'Partidas fuera de balance (PFB)')
    - Definicion_partidas_fuera_de_balance_pfb__partidas_fuera_de_balance__ric_3_1_2_6c11b5  (label: 'Partidas fuera de balance (PFB)')
    - Definicion_partidas_fuera_de_balance_pfb__partidas_fuera_de_balance_conceptos_computables_n_5d1680  (label: 'Partidas fuera de balance (PFB)')
[Definicion] 'ponderador de riesgo (p)' (2 nodos):
    - Definicion_ponderador_de_riesgo_p__ponderador_de_riesgo_de_cada_contraparte_i_expresado_en__87d08f  (label: 'Ponderador de riesgo (p)')
    - Definicion_ponderador_de_riesgo_p__ponderador_de_riesgo_en_tanto_por_uno__cap_2_1_e4f550  (label: 'Ponderador de riesgo (p)')
[Definicion] 'responsabilidad patrimonial computable' (2 nodos):
    - Definicion_responsabilidad_patrimonial_computable__magnitud_calculada_como_co_cd_ca_cd_pnc__1e8a96  (label: 'Responsabilidad patrimonial computable')
    - Definicion_responsabilidad_patrimonial_computable__magnitud_que_surge_de_la_suma_del_patrim_73fd69  (label: 'Responsabilidad patrimonial computable')
[Definicion] 'rm — resultado monetario total' (4 nodos):
    - Definicion_rm_resultado_monetario_total__resultado_monetario_total__cap_7_1_1_a8dd67  (label: 'RM — Resultado monetario total')
    - Definicion_rm_resultado_monetario_total__resultado_monetario_total__ric_5_1_1_28bcfc  (label: 'RM — resultado monetario total')
    - Definicion_rm_resultado_monetario_total__resultado_monetario_total_no_medido_en_valores_abs_72549e  (label: 'RM — Resultado monetario total')
    - Definicion_rm_resultado_monetario_total__resultado_monetario_total_prom_codigo_34400000__ri_02cbda  (label: 'RM — Resultado Monetario total')
[Definicion] 'sc — componente de servicios' (4 nodos):
    - Definicion_sc_componente_de_servicios__componente_de_servicios__ric_5_1_1_ac1db0  (label: 'SC — componente de servicios')
    - Definicion_sc_componente_de_servicios__componente_de_servicios_determinado_como_max_otros_i_e04e79  (label: 'SC — Componente de servicios')
    - Definicion_sc_componente_de_servicios__componente_de_servicios_prom_codigo_34200000__ric_5__5c272f  (label: 'SC — Componente de servicios')
    - Definicion_sc_componente_de_servicios__comprende_a_ingresos_por_honorarios_y_comisiones_ing_8a9433  (label: 'SC — Componente de servicios')
[Definicion] 'va — valor absoluto' (3 nodos):
    - Definicion_va_valor_absoluto__valor_absoluto__cap_7_1_1_d7fee6  (label: 'VA — Valor absoluto')
    - Definicion_va_valor_absoluto__valor_absoluto__ric_5_1_1_b87622  (label: 'VA — valor absoluto')
    - Definicion_va_valor_absoluto__valor_absoluto_de_una_magnitud__cap_5_3_2_5_618d1a  (label: 'VA — valor absoluto')
[Excepcion] 'excepcion fondos en moneda extranjera depositados localmente' (2 nodos):
    - Excepcion_quedan_exceptuados_de_la_prohibicion_de_entrega_de_activos_locales_los_fondos_en_fd967a  (label: 'Excepción fondos en moneda extranjera depositados localmente')
    - Excepcion_quedan_exceptuados_de_la_prohibicion_de_entregar_fondos_en_moneda_local_u_otros__3998c2  (label: 'Excepción fondos en moneda extranjera depositados localmente')
[Excepcion] 'excepcion liquidacion cobros exportaciones economia conocimiento' (3 nodos):
    - Excepcion_excepcion_de_liquidacion_de_cobros_de_exportaciones_de_bienes_y_servicios_para_l_a4c243  (label: 'Excepción liquidación cobros exportaciones economía conocimiento')
    - Excepcion_las_personas_juridicas_inscriptas_en_el_registro_nacional_de_beneficiarios_del_r_40c235  (label: 'Excepción liquidación cobros exportaciones economía conocimiento')
    - Excepcion_las_personas_juridicas_inscriptas_en_el_registro_nacional_de_beneficiarios_del_r_5d94f5  (label: 'Excepción liquidación cobros exportaciones economía conocimiento')
[Excepcion] 'excepcion punto 3.16.3 para personas humanas residentes' (2 nodos):
    - Excepcion_el_punto_3_16_3_no_aplica_a_clientes_que_sean_personas_humanas_residentes__ext_4_d9364f  (label: 'Excepción punto 3.16.3 para personas humanas residentes')
    - Excepcion_el_punto_3_16_3_no_es_aplicable_para_clientes_que_sean_personas_humanas_resident_1b5e2b  (label: 'Excepción punto 3.16.3 para personas humanas residentes')
[Excepcion] 'excepcion — cancelaciones de financiaciones en moneda extranjera' (2 nodos):
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_aplica_para_las_cancelaciones_de__9e4229  (label: 'Excepción — cancelaciones de financiaciones en moneda extranjera')
    - Excepcion_no_aplican_los_requisitos_de_declaracion_jurada_de_los_puntos_3_16_3_1_a_3_16_3__9fa252  (label: 'Excepción — cancelaciones de financiaciones en moneda extranjera')
[Excepcion] 'liberacion de obligaciones por aceptacion' (2 nodos):
    - Excepcion_la_constancia_de_aceptacion_de_la_nueva_entidad_libera_a_la_entidad_previa_de_su_7aebd3  (label: 'Liberación de obligaciones por aceptación')
    - Excepcion_la_entidad_previa_queda_liberada_de_sus_obligaciones_hacia_adelante_una_vez_que__0f1c80  (label: 'Liberación de obligaciones por aceptación')
[Obligacion] 'admision de aplicacion de divisas de cobros de exportaciones' (2 nodos):
    - Obligacion_se_admitira_la_aplicacion_de_divisas_de_cobros_de_exportaciones_de_bienes_a_la_c_48447c  (label: 'Admisión de aplicación de divisas de cobros de exportaciones')
    - Obligacion_se_admitira_la_aplicacion_de_divisas_de_cobros_de_exportaciones_de_bienes_a_la_c_c2da26  (label: 'Admisión de aplicación de divisas de cobros de exportaciones')
[Obligacion] 'atencion de financiaciones con fondos de lineas asignadas' (2 nodos):
    - Obligacion_las_filiales_o_subsidiarias_locales_deberan_atender_las_financiaciones_unicament_1c3ea8  (label: 'Atención de financiaciones con fondos de líneas asignadas')
    - Obligacion_las_financiaciones_deberan_ser_atendidas_exclusivamente_solo_con_fondos_provenie_0be6ca  (label: 'Atención de financiaciones con fondos de líneas asignadas')
[Obligacion] 'canalizacion de pedidos por entidad autorizada' (2 nodos):
    - Obligacion_los_pedidos_de_conformidad_previa_deben_ser_canalizados_a_traves_de_una_entidad__44e7b3  (label: 'Canalización de pedidos por entidad autorizada')
    - Obligacion_los_pedidos_de_conformidad_previa_deben_ser_canalizados_a_traves_de_una_entidad__852e15  (label: 'Canalización de pedidos por entidad autorizada')
[Obligacion] 'confeccion de dos boletos sin movimiento de pesos' (2 nodos):
    - Obligacion_para_el_registro_de_estas_operaciones_se_deben_confeccionar_dos_boletos_sin_movi_f345a9  (label: 'Confección de dos boletos sin movimiento de pesos')
    - Obligacion_se_deberan_confeccionar_dos_boletos_sin_movimiento_de_pesos_el_boleto_de_compra__f0d4a9  (label: 'Confección de dos boletos sin movimiento de pesos')
[Obligacion] 'confeccionar boletos de cambio a nombre propio' (2 nodos):
    - Obligacion_las_entidades_deberan_confeccionar_boletos_de_cambio_a_nombre_propio_para_cobros_4d7b03  (label: 'Confeccionar boletos de cambio a nombre propio')
    - Obligacion_las_entidades_deberan_confeccionar_boletos_de_cambio_a_nombre_propio_para_operac_ea4f74  (label: 'Confeccionar boletos de cambio a nombre propio')
[Obligacion] 'conformidad previa bcra — acceso mercado cambios' (4 nodos):
    - Obligacion_las_entidades_deberan_obtener_conformidad_previa_del_bcra_para_acceder_al_mercad_ec7e8c  (label: 'Conformidad previa BCRA — acceso mercado cambios')
    - Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_930255  (label: 'Conformidad previa BCRA — acceso mercado cambios')
    - Obligacion_obtener_conformidad_previa_del_bcra_para_acceder_al_mercado_de_cambios_para_real_622122  (label: 'Conformidad previa BCRA — acceso mercado cambios')
    - Obligacion_se_requerira_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_95b25d  (label: 'Conformidad previa BCRA — acceso mercado cambios')
[Obligacion] 'conformidad previa bcra — intereses contraparte vinculada' (2 nodos):
    - Obligacion_se_requiere_conformidad_previa_del_bcra_para_el_pago_de_intereses_cuando_el_acre_662a11  (label: 'Conformidad previa BCRA — intereses contraparte vinculada')
    - Obligacion_se_requiere_la_conformidad_previa_del_bcra_para_el_pago_de_intereses_de_deudas_c_e62e9c  (label: 'Conformidad previa BCRA — intereses contraparte vinculada')
[Obligacion] 'conformidad previa del bcra para acceso al mercado de cambios' (2 nodos):
    - Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_f706c4  (label: 'Conformidad previa del BCRA para acceso al mercado de cambios')
    - Obligacion_se_requiere_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios__ad5761  (label: 'Conformidad previa del BCRA para acceso al mercado de cambios')
[Obligacion] 'constar informacion minima en certificacion' (2 nodos):
    - Obligacion_en_la_certificacion_que_emita_la_entidad_para_habilitar_el_acceso_al_mercado_de__c1e772  (label: 'Constar información mínima en certificación')
    - Obligacion_la_certificacion_que_emita_la_entidad_debera_contener_al_menos_la_informacion_es_bd623b  (label: 'Constar información mínima en certificación')
[Obligacion] 'contar con certificacion de afectacion sepaimpo' (2 nodos):
    - Obligacion_en_el_caso_de_cancelaciones_del_capital_de_deudas_comerciales_por_importaciones__3d535a  (label: 'Contar con certificación de afectación SEPAIMPO')
    - Obligacion_la_entidad_debe_contar_con_la_certificacion_de_afectacion_correspondiente_emitid_35f3e5  (label: 'Contar con certificación de afectación SEPAIMPO')
[Obligacion] 'contar con declaracion jurada del importador' (2 nodos):
    - Obligacion_la_entidad_debe_contar_con_una_declaracion_jurada_del_importador_en_la_cual_cons_dfc639  (label: 'Contar con declaración jurada del importador')
    - Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_importador_en_la_cual_co_d83e40  (label: 'Contar con declaración jurada del importador')
[Obligacion] 'cumplimentar requerimientos de informacion bcra' (2 nodos):
    - Obligacion_la_entidad_financiera_designada_por_el_beneficiario_debera_cumplimentar_los_requ_79cf7c  (label: 'Cumplimentar requerimientos de información BCRA')
    - Obligacion_la_entidad_financiera_local_encargada_del_seguimiento_debera_cumplimentar_los_re_df07ff  (label: 'Cumplimentar requerimientos de información BCRA')
[Obligacion] 'emitir certificaciones a pedido del importador' (2 nodos):
    - Obligacion_la_entidad_nominada_debera_emitir_a_pedido_del_importador_certificaciones_con_el_f99c5c  (label: 'Emitir certificaciones a pedido del importador')
    - Obligacion_la_entidad_nominada_por_el_importador_para_el_seguimiento_de_la_oficializacion_d_651cfd  (label: 'Emitir certificaciones a pedido del importador')
[Obligacion] 'firma de declaracion jurada por cliente o representante' (2 nodos):
    - Obligacion_la_declaracion_jurada_debe_estar_firmada_por_el_cliente_no_residente_su_represen_3b057c  (label: 'Firma de declaración jurada por cliente o representante')
    - Obligacion_la_declaracion_jurada_debe_estar_firmada_por_el_cliente_su_representante_legal_o_c66330  (label: 'Firma de declaración jurada por cliente o representante')
[Obligacion] 'habilitacion de aplicacion de cobros de exportaciones' (2 nodos):
    - Obligacion_la_aplicacion_de_cobros_de_exportaciones_y_servicios_estara_habilitada_para_el_p_3894fc  (label: 'Habilitación de aplicación de cobros de exportaciones')
    - Obligacion_la_aplicacion_de_cobros_de_exportaciones_y_servicios_estara_habilitada_para_el_p_39a9e5  (label: 'Habilitación de aplicación de cobros de exportaciones')
[Obligacion] 'liquidacion en mercado de cambios al desembolso' (2 nodos):
    - Obligacion_las_prefinanciaciones_posfinanciaciones_y_financiaciones_deberan_ser_liquidadas__9e1b1a  (label: 'Liquidación en mercado de cambios al desembolso')
    - Obligacion_los_fondos_recibidos_por_los_clientes_en_virtud_de_financiaciones_en_moneda_extr_3bc31d  (label: 'Liquidación en mercado de cambios al desembolso')
[Obligacion] 'realizar boleto de venta de cambio — bonos bopreal' (2 nodos):
    - Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_de_la_empresa_q_42b2a0  (label: 'Realizar boleto de venta de cambio — bonos BOPREAL')
    - Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_cliente_ide_ef6510  (label: 'Realizar boleto de venta de cambio — bonos BOPREAL')
[Obligacion] 'verificacion de requisitos — suscripcion bopreal' (3 nodos):
    - Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_debera_verificar_que_el_cliente_299b5e  (label: 'Verificación de requisitos — suscripción BOPREAL')
    - Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debe_veri_13f6d3  (label: 'Verificación de requisitos — suscripción BOPREAL')
    - Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debera_ve_f753f7  (label: 'Verificación de requisitos — suscripción BOPREAL')
[Operacion] 'acceso al mercado de cambios' (3 nodos):
    - Operacion_acceso_al_mercado_de_cambios__ext_10_4_3_66ef01  (label: 'Acceso al mercado de cambios')
    - Operacion_acceso_al_mercado_de_cambios__ext_13_1_5_f43995  (label: 'Acceso al mercado de cambios')
    - Operacion_acceso_al_mercado_de_cambios__ext_3_4_77a47c  (label: 'Acceso al mercado de cambios')
[Operacion] 'acceso al mercado de cambios con fondos de financiacion' (2 nodos):
    - Operacion_acceso_al_mercado_de_cambios_con_fondos_de_financiacion__ext_10_10_2_3_22d385  (label: 'Acceso al mercado de cambios con fondos de financiación')
    - Operacion_acceso_al_mercado_de_cambios_con_fondos_de_financiacion__ext_13_3_1_306283  (label: 'Acceso al mercado de cambios con fondos de financiación')
[Operacion] 'acceso al mercado de cambios para cancelacion de lineas de credito' (2 nodos):
    - Operacion_acceso_al_mercado_de_cambios_para_cancelacion_de_lineas_de_credito__ext_10_7_1_a927dd  (label: 'Acceso al mercado de cambios para cancelación de líneas de crédito')
    - Operacion_acceso_al_mercado_de_cambios_para_cancelacion_de_lineas_de_credito__ext_13_6_cb12c5  (label: 'Acceso al mercado de cambios para cancelación de líneas de crédito')
[Operacion] 'acceso al mercado de cambios para compra de moneda extranjera' (2 nodos):
    - Operacion_acceso_al_mercado_de_cambios_para_compra_de_moneda_extranjera__ext_3_11_3_684fb8  (label: 'Acceso al mercado de cambios para compra de moneda extranjera')
    - Operacion_acceso_al_mercado_de_cambios_para_compra_de_moneda_extranjera__ext_7_8_5_2_9378c6  (label: 'Acceso al mercado de cambios para compra de moneda extranjera')
[Operacion] 'acceso al mercado de cambios para pago de deudas elegibles' (2 nodos):
    - Operacion_acceso_al_mercado_de_cambios_para_pago_de_deudas_elegibles__ext_4_8_4_46b9be  (label: 'Acceso al mercado de cambios para pago de deudas elegibles')
    - Operacion_acceso_al_mercado_de_cambios_para_pago_de_deudas_elegibles__ext_4_8_5_f3470a  (label: 'Acceso al mercado de cambios para pago de deudas elegibles')
[Operacion] 'acceso al mercado de cambios para residentes' (2 nodos):
    - Operacion_acceso_al_mercado_de_cambios_para_residentes__ext_3_11_2_d881e8  (label: 'Acceso al mercado de cambios para residentes')
    - Operacion_acceso_al_mercado_de_cambios_para_residentes__ext_3_11_3_05287a  (label: 'Acceso al mercado de cambios para residentes')
[Operacion] 'acumulacion de fondos de exportacion en cuentas' (2 nodos):
    - Operacion_acumulacion_de_fondos_de_exportacion_en_cuentas__ext_14_3_2_c89163  (label: 'Acumulación de fondos de exportación en cuentas')
    - Operacion_acumulacion_de_fondos_de_exportacion_en_cuentas__ext_7_11_5_f64bb6  (label: 'Acumulación de fondos de exportación en cuentas')
[Operacion] 'anticipos y prefinanciaciones de exportaciones del exterior' (2 nodos):
    - Operacion_anticipos_y_prefinanciaciones_de_exportaciones_del_exterior__ext_9_1_3_be60d6  (label: 'Anticipos y prefinanciaciones de exportaciones del exterior')
    - Operacion_anticipos_y_prefinanciaciones_de_exportaciones_del_exterior__ext_9_1_4_a570a7  (label: 'Anticipos y prefinanciaciones de exportaciones del exterior')
[Operacion] 'aplicacion ampliada de cobros de exportaciones' (2 nodos):
    - Operacion_aplicacion_ampliada_de_cobros_de_exportaciones__ext_7_10_4_e0cadf  (label: 'Aplicación ampliada de cobros de exportaciones')
    - Operacion_aplicacion_ampliada_de_cobros_de_exportaciones__ext_7_10_5_0e2e9e  (label: 'Aplicación ampliada de cobros de exportaciones')
[Operacion] 'aplicacion de divisas de cobros de exportaciones' (2 nodos):
    - Operacion_aplicacion_de_divisas_de_cobros_de_exportaciones__ext_3_17_3_2_296356  (label: 'Aplicación de divisas de cobros de exportaciones')
    - Operacion_aplicacion_de_divisas_de_cobros_de_exportaciones__ext_7_3_d1d2da  (label: 'Aplicación de divisas de cobros de exportaciones')
[Operacion] 'boleto de venta de cambio — bonos bopreal' (2 nodos):
    - Operacion_boleto_de_venta_de_cambio_bonos_bopreal__ext_4_6_2_e18cc0  (label: 'Boleto de venta de cambio — bonos BOPREAL')
    - Operacion_boleto_de_venta_de_cambio_bonos_bopreal__ext_4_7_c55cc3  (label: 'Boleto de venta de cambio — bonos BOPREAL')
[Operacion] 'calculo de exigencia de capital por riesgo de credito' (2 nodos):
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_credito__cap_2_1_427f6d  (label: 'Cálculo de exigencia de capital por riesgo de crédito')
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_credito__ric_3_1_2_d223d8  (label: 'Cálculo de exigencia de capital por riesgo de crédito')
[Operacion] 'calculo de exigencia de capital por riesgo de mercado' (3 nodos):
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_mercado__cap_6_1_1_5_5f23a6  (label: 'Cálculo de exigencia de capital por riesgo de mercado')
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_mercado__cap_6_1_4_3_0a20b5  (label: 'Cálculo de exigencia de capital por riesgo de mercado')
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_mercado__cap_6_1_7a5b56  (label: 'Cálculo de exigencia de capital por riesgo de mercado')
[Operacion] 'cancelacion de cartas de credito o letras avaladas' (2 nodos):
    - Operacion_cancelacion_de_cartas_de_credito_o_letras_avaladas__ext_10_3_6_ea9f41  (label: 'Cancelación de cartas de crédito o letras avaladas')
    - Operacion_cancelacion_de_cartas_de_credito_o_letras_avaladas__ext_10_4_4_359edc  (label: 'Cancelación de cartas de crédito o letras avaladas')
[Operacion] 'cancelacion de garantias comerciales de importaciones' (2 nodos):
    - Operacion_cancelacion_de_garantias_comerciales_de_importaciones__ext_10_3_1_3_fb78d4  (label: 'Cancelación de garantías comerciales de importaciones')
    - Operacion_cancelacion_de_garantias_comerciales_de_importaciones__ext_10_4_1_4_9ce2b8  (label: 'Cancelación de garantías comerciales de importaciones')
[Operacion] 'canje y/o arbitraje con fondos en moneda extranjera' (2 nodos):
    - Operacion_canje_y_o_arbitraje_con_fondos_en_moneda_extranjera__ext_10_10_2_14_325767  (label: 'Canje y/o arbitraje con fondos en moneda extranjera')
    - Operacion_canje_y_o_arbitraje_con_fondos_en_moneda_extranjera__ext_13_3_9_f12094  (label: 'Canje y/o arbitraje con fondos en moneda extranjera')
[Operacion] 'clasificacion de cliente con alto riesgo de insolvencia' (2 nodos):
    - Operacion_clasificacion_de_cliente_con_alto_riesgo_de_insolvencia__cla_6_5_4_3_259a9b  (label: 'Clasificación de cliente con alto riesgo de insolvencia')
    - Operacion_clasificacion_de_cliente_con_alto_riesgo_de_insolvencia__cla_6_5_4_84f05b  (label: 'Clasificación de cliente con alto riesgo de insolvencia')
[Operacion] 'clasificacion de deudor en categoria con problemas' (3 nodos):
    - Operacion_clasificacion_de_deudor_en_categoria_con_problemas__cla_6_5_3_12_046b1b  (label: 'Clasificación de deudor en categoría Con problemas')
    - Operacion_clasificacion_de_deudor_en_categoria_con_problemas__cla_6_5_3_7_19aa49  (label: 'Clasificación de deudor en categoría Con problemas')
    - Operacion_clasificacion_de_deudor_en_categoria_con_problemas__cla_6_5_3_9_4aa3d2  (label: 'Clasificación de deudor en categoría Con problemas')
[Operacion] 'clasificacion de deudores' (3 nodos):
    - Operacion_clasificacion_de_deudores__cla_3_2_ccda30  (label: 'Clasificación de deudores')
    - Operacion_clasificacion_de_deudores__cla_3_3_2_aa3de8  (label: 'Clasificación de deudores')
    - Operacion_clasificacion_de_deudores__cla_4_5_0d8876  (label: 'Clasificación de deudores')
[Operacion] 'clasificacion de exposiciones a instrumentos' (2 nodos):
    - Operacion_clasificacion_de_exposiciones_a_instrumentos__cap_2_11_1_de5fe0  (label: 'Clasificación de exposiciones a instrumentos')
    - Operacion_clasificacion_de_exposiciones_a_instrumentos__cap_2_11_2_48b152  (label: 'Clasificación de exposiciones a instrumentos')
[Operacion] 'clasificacion en categoria irrecuperable' (5 nodos):
    - Operacion_clasificacion_en_categoria_irrecuperable__cla_6_5_5_2_8c3036  (label: 'Clasificación en categoría Irrecuperable')
    - Operacion_clasificacion_en_categoria_irrecuperable__cla_6_5_5_6_017f19  (label: 'Clasificación en categoría Irrecuperable')
    - Operacion_clasificacion_en_categoria_irrecuperable__cla_6_5_5_7_84f047  (label: 'Clasificación en categoría Irrecuperable')
    - Operacion_clasificacion_en_categoria_irrecuperable__cla_6_5_5_8_a1c2c5  (label: 'Clasificación en categoría Irrecuperable')
    - Operacion_clasificacion_en_categoria_irrecuperable__cla_6_5_5_9_87280d  (label: 'Clasificación en categoría Irrecuperable')
[Operacion] 'cobro de exportacion percibido luego del embarque' (2 nodos):
    - Operacion_cobro_de_exportacion_percibido_luego_del_embarque__ext_8_5_20_2_517d79  (label: 'Cobro de exportación percibido luego del embarque')
    - Operacion_cobro_de_exportacion_percibido_luego_del_embarque__ext_8_5_20_87ea45  (label: 'Cobro de exportación percibido luego del embarque')
[Operacion] 'compra de moneda extranjera para garantias' (2 nodos):
    - Operacion_compra_de_moneda_extranjera_para_garantias__ext_3_11_1_260284  (label: 'Compra de moneda extranjera para garantías')
    - Operacion_compra_de_moneda_extranjera_para_garantias__ext_7_9_6_97386f  (label: 'Compra de moneda extranjera para garantías')
[Operacion] 'compra de moneda extranjera — formacion de activos externos' (2 nodos):
    - Operacion_compra_de_moneda_extranjera_formacion_de_activos_externos__ext_3_10_0aaec8  (label: 'Compra de moneda extranjera — formación de activos externos')
    - Operacion_compra_de_moneda_extranjera_formacion_de_activos_externos__ext_3_9_5_b31762  (label: 'Compra de moneda extranjera — formación de activos externos')
[Operacion] 'designacion de entidad financiera para seguimiento' (2 nodos):
    - Operacion_designacion_de_entidad_financiera_para_seguimiento__ext_7_10_2_4_f34369  (label: 'Designación de entidad financiera para seguimiento')
    - Operacion_designacion_de_entidad_financiera_para_seguimiento__ext_7_9_3_fb6177  (label: 'Designación de entidad financiera para seguimiento')
[Operacion] 'determinacion de responsabilidad patrimonial computable' (2 nodos):
    - Operacion_determinacion_de_responsabilidad_patrimonial_computable__cap_1_3_8113e7  (label: 'Determinación de responsabilidad patrimonial computable')
    - Operacion_determinacion_de_responsabilidad_patrimonial_computable__ric_6_1_e931c1  (label: 'Determinación de responsabilidad patrimonial computable')
[Operacion] 'determinacion exigencia riesgo de mercado' (2 nodos):
    - Operacion_determinacion_exigencia_riesgo_de_mercado__ric_12_2_3d7459  (label: 'Determinación exigencia riesgo de mercado')
    - Operacion_determinacion_exigencia_riesgo_de_mercado__ric_4_1_1_1_b7cee7  (label: 'Determinación exigencia riesgo de mercado')
[Operacion] 'emision de certificacion de aumento de exportaciones' (2 nodos):
    - Operacion_emision_de_certificacion_de_aumento_de_exportaciones__ext_3_18_2_4_515653  (label: 'Emisión de certificación de aumento de exportaciones')
    - Operacion_emision_de_certificacion_de_aumento_de_exportaciones__ext_3_18_2_762dd5  (label: 'Emisión de Certificación de aumento de exportaciones')
[Operacion] 'emision de certificaciones de acceso al mercado de cambios' (2 nodos):
    - Operacion_emision_de_certificaciones_de_acceso_al_mercado_de_cambios__ext_11_1_1_4_736b6e  (label: 'Emisión de certificaciones de acceso al mercado de cambios')
    - Operacion_emision_de_certificaciones_de_acceso_al_mercado_de_cambios__ext_11_1_1_7_83b37e  (label: 'Emisión de certificaciones de acceso al mercado de cambios')
[Operacion] 'emision de certificaciones de aplicacion' (4 nodos):
    - Operacion_emision_de_certificaciones_de_aplicacion__ext_9_3_13_6303cb  (label: 'Emisión de certificaciones de aplicación')
    - Operacion_emision_de_certificaciones_de_aplicacion__ext_9_3_2_98a996  (label: 'Emisión de certificaciones de aplicación')
    - Operacion_emision_de_certificaciones_de_aplicacion__ext_9_3_6_e1f723  (label: 'Emisión de certificaciones de aplicación')
    - Operacion_emision_de_certificaciones_de_aplicacion__ext_9_3_81e1ab  (label: 'Emisión de certificaciones de aplicación')
[Operacion] 'emision de certificaciones de aplicacion de divisas' (3 nodos):
    - Operacion_emision_de_certificaciones_de_aplicacion_de_divisas__ext_9_3_11_bd1f81  (label: 'Emisión de certificaciones de aplicación de divisas')
    - Operacion_emision_de_certificaciones_de_aplicacion_de_divisas__ext_9_3_1_e30f26  (label: 'Emisión de certificaciones de aplicación de divisas')
    - Operacion_emision_de_certificaciones_de_aplicacion_de_divisas__ext_9_3_9_b3b62e  (label: 'Emisión de certificaciones de aplicación de divisas')
[Operacion] 'emision de certificaciones de aumento de exportaciones' (2 nodos):
    - Operacion_emision_de_certificaciones_de_aumento_de_exportaciones__ext_3_17_2_1_a0fd83  (label: 'Emisión de Certificaciones de aumento de exportaciones')
    - Operacion_emision_de_certificaciones_de_aumento_de_exportaciones__ext_3_17_3_4_7ccd35  (label: 'Emisión de Certificaciones de aumento de exportaciones')
[Operacion] 'emision de instrumentos por entidad financiera' (2 nodos):
    - Operacion_emision_de_instrumentos_por_entidad_financiera__cap_8_2_2_1_d185e3  (label: 'Emisión de instrumentos por entidad financiera')
    - Operacion_emision_de_instrumentos_por_entidad_financiera__cap_8_2_3_1_775f38  (label: 'Emisión de instrumentos por entidad financiera')
[Operacion] 'endeudamientos financieros con el exterior' (2 nodos):
    - Operacion_endeudamientos_financieros_con_el_exterior__ext_14_2_1_1_f0d73a  (label: 'Endeudamientos financieros con el exterior')
    - Operacion_endeudamientos_financieros_con_el_exterior__ext_9_1_6_0ad525  (label: 'Endeudamientos financieros con el exterior')
[Operacion] 'financiacion comercial por importacion de bienes' (2 nodos):
    - Operacion_financiacion_comercial_por_importacion_de_bienes__ext_7_11_1_1_9b325b  (label: 'Financiación comercial por importación de bienes')
    - Operacion_financiacion_comercial_por_importacion_de_bienes__ext_7_11_1_2_dff428  (label: 'Financiación comercial por importación de bienes')
[Operacion] 'financiaciones otorgadas por sucursales y subsidiarias locales' (2 nodos):
    - Operacion_financiaciones_otorgadas_por_sucursales_y_subsidiarias_locales__cap_2_2_3_45d3af  (label: 'Financiaciones otorgadas por sucursales y subsidiarias locales')
    - Operacion_financiaciones_otorgadas_por_sucursales_y_subsidiarias_locales__cla_2_2_4_961c21  (label: 'Financiaciones otorgadas por sucursales y subsidiarias locales')
[Operacion] 'liquidacion de divisas en mercado de cambios' (2 nodos):
    - Operacion_liquidacion_de_divisas_en_mercado_de_cambios__ext_10_3_2_4_8db3c7  (label: 'Liquidación de divisas en mercado de cambios')
    - Operacion_liquidacion_de_divisas_en_mercado_de_cambios__ext_9_1_1_ccb2b4  (label: 'Liquidación de divisas en mercado de cambios')
[Operacion] 'nominacion de entidad financiera responsable' (2 nodos):
    - Operacion_nominacion_de_entidad_financiera_responsable__ext_3_17_2_a9cf04  (label: 'Nominación de entidad financiera responsable')
    - Operacion_nominacion_de_entidad_financiera_responsable__ext_3_18_2_c9b118  (label: 'Nominación de entidad financiera responsable')
[Operacion] 'otorgamiento de garantias localmente' (2 nodos):
    - Operacion_otorgamiento_de_garantias_localmente__cap_2_2_3_4_c238ac  (label: 'Otorgamiento de garantías localmente')
    - Operacion_otorgamiento_de_garantias_localmente__cla_2_2_4_4_562d10  (label: 'Otorgamiento de garantías localmente')
[Operacion] 'pago capital e intereses endeudamientos financieros' (2 nodos):
    - Operacion_pago_capital_e_intereses_endeudamientos_financieros__ext_7_10_1_2_ff2c83  (label: 'Pago capital e intereses endeudamientos financieros')
    - Operacion_pago_capital_e_intereses_endeudamientos_financieros__ext_7_9_1_1_f08d8a  (label: 'Pago capital e intereses endeudamientos financieros')
[Operacion] 'pago capital e intereses titulos deuda con registro' (3 nodos):
    - Operacion_pago_capital_e_intereses_titulos_deuda_con_registro__ext_7_9_1_11_e67e56  (label: 'Pago capital e intereses títulos deuda con registro')
    - Operacion_pago_capital_e_intereses_titulos_deuda_con_registro__ext_7_9_1_8_d1a595  (label: 'Pago capital e intereses títulos deuda con registro')
    - Operacion_pago_capital_e_intereses_titulos_deuda_con_registro__ext_7_9_1_9_a33aa5  (label: 'Pago capital e intereses títulos deuda con registro')
[Operacion] 'pago de capital e intereses de endeudamientos financieros' (2 nodos):
    - Operacion_pago_de_capital_e_intereses_de_endeudamientos_financieros__ext_7_9_1_4_6a52b3  (label: 'Pago de capital e intereses de endeudamientos financieros')
    - Operacion_pago_de_capital_e_intereses_de_endeudamientos_financieros__ext_7_9_1_5_0837d0  (label: 'Pago de capital e intereses de endeudamientos financieros')
[Operacion] 'pago de importacion de bien con registro aduanero' (2 nodos):
    - Operacion_pago_de_importacion_de_bien_con_registro_aduanero__ext_10_11_5_4b359d  (label: 'Pago de importación de bien con registro aduanero')
    - Operacion_pago_de_importacion_de_bien_con_registro_aduanero__ext_10_11_6_de7af6  (label: 'Pago de importación de bien con registro aduanero')
[Operacion] 'pago de importaciones con ingreso aduanero pendiente' (2 nodos):
    - Operacion_pago_de_importaciones_con_ingreso_aduanero_pendiente__ext_10_5_c49b34  (label: 'Pago de importaciones con ingreso aduanero pendiente')
    - Operacion_pago_de_importaciones_con_ingreso_aduanero_pendiente__ext_11_2_18e4d3  (label: 'Pago de importaciones con ingreso aduanero pendiente')
[Operacion] 'pago de intereses deuda comercial importacion' (2 nodos):
    - Operacion_pago_de_intereses_deuda_comercial_importacion__ext_3_17_1_3_b58e24  (label: 'Pago de intereses deuda comercial importación')
    - Operacion_pago_de_intereses_deuda_comercial_importacion__ext_3_3_abc8da  (label: 'Pago de intereses deuda comercial importación')
[Operacion] 'pago deudas comerciales importaciones servicios' (2 nodos):
    - Operacion_pago_deudas_comerciales_importaciones_servicios__ext_3_14_5_2_ec9bf5  (label: 'Pago deudas comerciales importaciones servicios')
    - Operacion_pago_deudas_comerciales_importaciones_servicios__ext_4_8_1_2_0abf53  (label: 'Pago deudas comerciales importaciones servicios')
[Operacion] 'precancelacion de intereses en canje de titulos' (2 nodos):
    - Operacion_precancelacion_de_intereses_en_canje_de_titulos__ext_3_5_3_3_3d2b7d  (label: 'Precancelación de intereses en canje de títulos')
    - Operacion_precancelacion_de_intereses_en_canje_de_titulos__ext_3_6_4_3_a8a33d  (label: 'Precancelación de intereses en canje de títulos')
[Operacion] 'registro de operacion en sistema online bcra' (2 nodos):
    - Operacion_registro_de_operacion_en_sistema_online_bcra__ext_14_4_2_5c90f7  (label: 'Registro de operación en sistema online BCRA')
    - Operacion_registro_de_operacion_en_sistema_online_bcra__ext_3_8_3_ba4c1f  (label: 'Registro de operación en sistema online BCRA')
[Operacion] 'repatriacion de inversiones directas no residentes' (2 nodos):
    - Operacion_repatriacion_de_inversiones_directas_no_residentes__ext_7_10_1_4_48c957  (label: 'Repatriación de inversiones directas no residentes')
    - Operacion_repatriacion_de_inversiones_directas_no_residentes__ext_7_9_1_2_ab0610  (label: 'Repatriación de inversiones directas no residentes')
[Operacion] 'repatriacion inversion directa no residentes' (4 nodos):
    - Operacion_repatriacion_inversion_directa_no_residentes__ext_3_13_1_7_fa6676  (label: 'Repatriación inversión directa no residentes')
    - Operacion_repatriacion_inversion_directa_no_residentes__ext_3_13_1_8_c88e8f  (label: 'Repatriación inversión directa no residentes')
    - Operacion_repatriacion_inversion_directa_no_residentes__ext_3_13_1_9_d4e204  (label: 'Repatriación inversión directa no residentes')
    - Operacion_repatriacion_inversion_directa_no_residentes__ext_3_17_1_6_22c487  (label: 'Repatriación inversión directa no residentes')
[Operacion] 'revision de cartera comercial' (2 nodos):
    - Operacion_revision_de_cartera_comercial__cla_6_1_25ae6d  (label: 'Revisión de cartera comercial')
    - Operacion_revision_de_cartera_comercial__cla_6_3_3_cf7276  (label: 'Revisión de cartera comercial')
[Operacion] 'suscripcion bopreal por utilidades y dividendos' (2 nodos):
    - Operacion_suscripcion_bopreal_por_utilidades_y_dividendos__ext_4_6_1_f1b06c  (label: 'Suscripción BOPREAL por utilidades y dividendos')
    - Operacion_suscripcion_bopreal_por_utilidades_y_dividendos__ext_4_6_2_1_ff1ee1  (label: 'Suscripción BOPREAL por utilidades y dividendos')
[Operacion] 'suscripcion de bonos bopreal' (2 nodos):
    - Operacion_suscripcion_de_bonos_bopreal__ext_4_4_b998b5  (label: 'Suscripción de bonos BOPREAL')
    - Operacion_suscripcion_de_bonos_bopreal__ext_4_6_2_3_7576c6  (label: 'Suscripción de bonos BOPREAL')
[Operacion] 'venta de divisas con debito en cuentas' (2 nodos):
    - Operacion_venta_de_divisas_con_debito_en_cuentas__ext_10_3_2_2_46dbdd  (label: 'Venta de divisas con débito en cuentas')
    - Operacion_venta_de_divisas_con_debito_en_cuentas__ext_10_4_2_3_bd6009  (label: 'Venta de divisas con débito en cuentas')
[Potestad] 'acceso al mercado de cambios para pago al exterior' (2 nodos):
    - Potestad_acceso_al_mercado_de_cambios_para_pago_al_exterior__la_entidad_interviniente_tie_c3cc8d  (label: 'Acceso al mercado de cambios para pago al exterior')
    - Potestad_acceso_al_mercado_de_cambios_para_pago_al_exterior__la_entidad_podra_dar_acceso__25765f  (label: 'Acceso al mercado de cambios para pago al exterior')
[Potestad] 'acceso al mercado de cambios para pago de servicios' (3 nodos):
    - Potestad_acceso_al_mercado_de_cambios_para_pago_de_servicios__las_entidades_estan_faculta_599420  (label: 'Acceso al mercado de cambios para pago de servicios')
    - Potestad_acceso_al_mercado_de_cambios_para_pago_de_servicios__las_entidades_estan_faculta_e645ce  (label: 'Acceso al mercado de cambios para pago de servicios')
    - Potestad_acceso_al_mercado_de_cambios_para_pago_de_servicios__las_entidades_podran_dar_ac_b63f8f  (label: 'Acceso al mercado de cambios para pago de servicios')
[Potestad] 'acceso al mercado de cambios para pagos de servicios' (2 nodos):
    - Potestad_acceso_al_mercado_de_cambios_para_pagos_de_servicios__las_entidades_estan_facult_2541aa  (label: 'Acceso al mercado de cambios para pagos de servicios')
    - Potestad_acceso_al_mercado_de_cambios_para_pagos_de_servicios__las_entidades_estan_facult_3307dd  (label: 'Acceso al mercado de cambios para pagos de servicios')
[Potestad] 'acceso al mercado de cambios sin conformidad previa del bcra' (2 nodos):
    - Potestad_acceso_al_mercado_de_cambios_sin_conformidad_previa_del_bcra__las_entidades_pued_406981  (label: 'Acceso al mercado de cambios sin conformidad previa del BCRA')
    - Potestad_acceso_al_mercado_de_cambios_sin_conformidad_previa_del_bcra__las_entidades_qued_15c9dd  (label: 'Acceso al mercado de cambios sin conformidad previa del BCRA')
[Potestad] 'acceso al mercado de cambios — clientes' (2 nodos):
    - Potestad_acceso_al_mercado_de_cambios_clientes__las_entidades_estan_facultadas_a_dar_acce_5de80c  (label: 'Acceso al mercado de cambios — clientes')
    - Potestad_acceso_al_mercado_de_cambios_clientes__los_clientes_quedan_facultados_para_acced_557ecd  (label: 'Acceso al mercado de cambios — clientes')
[Potestad] 'acceso mercado cambios mediante canje/arbitraje bopreal' (2 nodos):
    - Potestad_acceso_mercado_cambios_mediante_canje_arbitraje_bopreal__los_clientes_quedan_fac_2cd827  (label: 'Acceso mercado cambios mediante canje/arbitraje BOPREAL')
    - Potestad_acceso_mercado_cambios_mediante_canje_arbitraje_bopreal__los_clientes_tienen_la__855fb4  (label: 'Acceso mercado cambios mediante canje/arbitraje BOPREAL')
[Potestad] 'acceso mercado cambios para pago gastos emision y servicios' (2 nodos):
    - Potestad_acceso_mercado_cambios_para_pago_gastos_emision_y_servicios__la_entidad_podra_da_22952a  (label: 'Acceso mercado cambios para pago gastos emisión y servicios')
    - Potestad_acceso_mercado_cambios_para_pago_gastos_emision_y_servicios__la_entidad_podra_da_e0e752  (label: 'Acceso mercado cambios para pago gastos emisión y servicios')
[Potestad] 'considerar operacion garantizada por aseguradora privada' (2 nodos):
    - Potestad_considerar_operacion_garantizada_por_aseguradora_privada__las_entidades_podran_c_048bd3  (label: 'Considerar operación garantizada por aseguradora privada')
    - Potestad_considerar_operacion_garantizada_por_aseguradora_privada__las_entidades_tienen_l_4a05e7  (label: 'Considerar operación garantizada por aseguradora privada')
[Potestad] 'facultad de acceso al mercado de cambios' (2 nodos):
    - Potestad_facultad_de_acceso_al_mercado_de_cambios__el_cliente_que_cuente_con_una_certific_ce3e5b  (label: 'Facultad de acceso al mercado de cambios')
    - Potestad_facultad_de_acceso_al_mercado_de_cambios__los_clientes_que_cumplen_las_condicion_132b56  (label: 'Facultad de acceso al mercado de cambios')
[Potestad] 'facultad de considerar cumplimentado el seguimiento' (3 nodos):
    - Potestad_facultad_de_considerar_cumplimentado_el_seguimiento__facultad_de_la_entidad_de_c_6aa7b5  (label: 'Facultad de considerar cumplimentado el seguimiento')
    - Potestad_facultad_de_considerar_cumplimentado_el_seguimiento__la_entidad_esta_facultada_a_7fee14  (label: 'Facultad de considerar cumplimentado el seguimiento')
    - Potestad_facultad_de_considerar_cumplimentado_el_seguimiento__la_entidad_esta_facultada_a_8c67aa  (label: 'Facultad de considerar cumplimentado el seguimiento')
[Potestad] 'facultad de dar acceso al mercado de cambios' (9 nodos):
    - Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__la_entidad_interviniente_esta_facu_b82ae0  (label: 'Facultad de dar acceso al mercado de cambios')
    - Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__la_entidad_interviniente_tiene_la__ad9e24  (label: 'Facultad de dar acceso al mercado de cambios')
    - Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__la_entidad_interviniente_tiene_la__fbebc9  (label: 'Facultad de dar acceso al mercado de cambios')
    - Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__las_entidades_estan_facultadas_a_d_0a6843  (label: 'Facultad de dar acceso al mercado de cambios')
    - Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__las_entidades_estan_facultadas_par_ac89fe  (label: 'Facultad de dar acceso al mercado de cambios')
    - Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__las_entidades_podran_dar_acceso_al_0df561  (label: 'Facultad de dar acceso al mercado de cambios')
    - Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__las_entidades_quedan_facultadas_a__713df0  (label: 'Facultad de dar acceso al mercado de cambios')
    - Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__las_entidades_tienen_la_facultad_d_87cd09  (label: 'Facultad de dar acceso al mercado de cambios')
    - Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__las_entidades_tienen_la_facultad_d_db79ee  (label: 'Facultad de dar acceso al mercado de cambios')
[Potestad] 'facultad de emitir certificaciones de aplicacion' (6 nodos):
    - Potestad_facultad_de_emitir_certificaciones_de_aplicacion__facultad_de_emitir_certificaci_3d96c5  (label: 'Facultad de emitir certificaciones de aplicación')
    - Potestad_facultad_de_emitir_certificaciones_de_aplicacion__la_entidad_esta_facultada_a_em_2ea65e  (label: 'Facultad de emitir certificaciones de aplicación')
    - Potestad_facultad_de_emitir_certificaciones_de_aplicacion__la_entidad_esta_facultada_para_2eadea  (label: 'Facultad de emitir certificaciones de aplicación')
    - Potestad_facultad_de_emitir_certificaciones_de_aplicacion__la_entidad_esta_facultada_para_3d153b  (label: 'Facultad de emitir certificaciones de aplicación')
    - Potestad_facultad_de_emitir_certificaciones_de_aplicacion__la_entidad_tiene_la_facultad_d_50e9c4  (label: 'Facultad de emitir certificaciones de aplicación')
    - Potestad_facultad_de_emitir_certificaciones_de_aplicacion__la_entidad_tiene_la_facultad_d_9887fc  (label: 'Facultad de emitir certificaciones de aplicación')
[Potestad] 'facultad realizar arbitrajes y canjes en exterior' (2 nodos):
    - Potestad_facultad_realizar_arbitrajes_y_canjes_en_exterior__las_entidades_autorizadas_que_cab9aa  (label: 'Facultad realizar arbitrajes y canjes en exterior')
    - Potestad_facultad_realizar_arbitrajes_y_canjes_en_exterior__las_entidades_financieras_y_c_b6910a  (label: 'Facultad realizar arbitrajes y canjes en exterior')
[Potestad] 'habilitacion para emitir nuevas certificaciones' (2 nodos):
    - Potestad_habilitacion_para_emitir_nuevas_certificaciones__la_nueva_entidad_queda_habilita_1e7eeb  (label: 'Habilitación para emitir nuevas certificaciones')
    - Potestad_habilitacion_para_emitir_nuevas_certificaciones__la_nueva_entidad_queda_habilita_220980  (label: 'Habilitación para emitir nuevas certificaciones')
[Potestad] 'solicitud de ampliacion de plazo para liquidacion de divisas' (2 nodos):
    - Potestad_solicitud_de_ampliacion_de_plazo_para_liquidacion_de_divisas__el_exportador_podr_6c2fd7  (label: 'Solicitud de ampliación de plazo para liquidación de divisas')
    - Potestad_solicitud_de_ampliacion_de_plazo_para_liquidacion_de_divisas__el_exportador_podr_a654d4  (label: 'Solicitud de ampliación de plazo para liquidación de divisas')
[Restriccion] 'limitacion activos admitidos como garantia' (2 nodos):
    - Restriccion_el_activo_recibido_en_garantia_se_limitara_a_aquellos_listados_en_el_punto_5_3_1_ddaea1  (label: 'Limitación activos admitidos como garantía')
    - Restriccion_los_activos_admitidos_como_garantia_se_limitan_a_los_enumerados_en_el_punto_5_3__d463af  (label: 'Limitación activos admitidos como garantía')
[Restriccion] 'limite acumulado de vencimientos de capital del nuevo endeudamiento' (2 nodos):
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_no_pod_69cd35  (label: 'Límite acumulado de vencimientos de capital del nuevo endeudamiento')
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_no_pod_864b9b  (label: 'Límite acumulado de vencimientos de capital del nuevo endeudamiento')
[Restriccion] 'limite monto acumulado vencimientos capital nuevo endeudamiento' (3 nodos):
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_no_pod_4d5eb0  (label: 'Límite monto acumulado vencimientos capital nuevo endeudamiento')
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_no_pod_60b35d  (label: 'Límite monto acumulado vencimientos capital nuevo endeudamiento')
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_no_pod_dd4fee  (label: 'Límite monto acumulado vencimientos capital nuevo endeudamiento')
[Restriccion] 'limite monto certificacion — acceso cambios' (2 nodos):
    - Restriccion_el_acceso_al_mercado_de_cambios_esta_limitado_al_monto_de_la_certificacion_otorg_cec881  (label: 'Límite monto certificación — acceso cambios')
    - Restriccion_el_acceso_al_mercado_de_cambios_no_podra_exceder_el_monto_de_la_certificacion__e_6ec9a6  (label: 'Límite monto certificación — acceso cambios')
[Restriccion] 'limite participacion en capital de cada empresa' (2 nodos):
    - Restriccion_la_participacion_en_el_capital_de_cada_empresa_no_podra_exceder_el_15__ric_3_1_2_0d81e5  (label: 'Límite participación en capital de cada empresa')
    - Restriccion_limite_maximo_de_participacion_en_el_capital_de_cada_empresa_del_15_de_la_respon_f13096  (label: 'Límite participación en capital de cada empresa')
[Restriccion] 'limite total participaciones en capital de empresas' (2 nodos):
    - Restriccion_el_total_de_participaciones_en_el_capital_de_empresas_no_podra_exceder_el_60__ri_0d90e2  (label: 'Límite total participaciones en capital de empresas')
    - Restriccion_limite_maximo_de_total_de_participaciones_en_el_capital_de_empresas_del_60_de_la_ae6a57  (label: 'Límite total participaciones en capital de empresas')
[Restriccion] 'ponderador 100% — calificacion bb+ hasta b-' (2 nodos):
    - Restriccion_ponderador_de_riesgo_del_100_para_exposiciones_a_entes_del_sector_publico_no_fin_5eeb6b  (label: 'Ponderador 100% — calificación BB+ hasta B-')
    - Restriccion_ponderador_de_riesgo_del_100_para_exposiciones_a_otros_estados_soberanos_o_sus_b_52a4bb  (label: 'Ponderador 100% — calificación BB+ hasta B-')
[Restriccion] 'ponderador 100% — no calificado' (2 nodos):
    - Restriccion_ponderador_de_riesgo_del_100_para_exposiciones_a_entes_del_sector_publico_no_fin_31aab8  (label: 'Ponderador 100% — No calificado')
    - Restriccion_ponderador_de_riesgo_del_100_para_exposiciones_a_otros_estados_soberanos_o_sus_b_bb0420  (label: 'Ponderador 100% — no calificado')
[Restriccion] 'ponderador 150% — calificacion inferior a b-' (2 nodos):
    - Restriccion_ponderador_de_riesgo_del_150_para_exposiciones_a_entes_del_sector_publico_no_fin_1758ef  (label: 'Ponderador 150% — calificación Inferior a B-')
    - Restriccion_ponderador_de_riesgo_del_150_para_exposiciones_a_otros_estados_soberanos_o_sus_b_13adab  (label: 'Ponderador 150% — calificación inferior a B-')
[Restriccion] 'prohibicion acceso mercado cambios — deudas entre residentes' (3 nodos):
    - Restriccion_se_prohibe_el_acceso_al_mercado_de_cambios_para_el_pago_de_deudas_y_otras_obliga_1b0df3  (label: 'Prohibición acceso mercado cambios — deudas entre residentes')
    - Restriccion_se_prohibe_el_acceso_al_mercado_de_cambios_para_el_pago_de_deudas_y_otras_obliga_2e5b05  (label: 'Prohibición acceso mercado cambios — deudas entre residentes')
    - Restriccion_se_prohibe_el_acceso_al_mercado_de_cambios_para_el_pago_de_deudas_y_otras_obliga_ee2a38  (label: 'Prohibición acceso mercado cambios — deudas entre residentes')
[Restriccion] 'prohibicion dividendo/cupon reajustable por riesgo de credito' (2 nodos):
    - Restriccion_los_instrumentos_incluidos_en_el_pnc_no_pueden_incorporar_un_dividendo_o_cupon_q_bd7dca  (label: 'Prohibición dividendo/cupón reajustable por riesgo de crédito')
    - Restriccion_no_incorporar_un_dividendo_o_cupon_que_se_reajuste_periodicamente_en_funcion_en__5625f6  (label: 'Prohibición dividendo/cupón reajustable por riesgo de crédito')
[Restriccion] 'prohibicion pago sin conformidad previa' (2 nodos):
    - Restriccion_prohibicion_de_realizar_pagos_de_capital_e_intereses_de_endeudamientos_financier_03fe7e  (label: 'Prohibición pago sin conformidad previa')
    - Restriccion_se_prohibe_realizar_pagos_de_capital_e_intereses_de_endeudamientos_financieros_c_12edad  (label: 'Prohibición pago sin conformidad previa')
[Sujeto] 'la entidad' (2 nodos):
    - Sujeto_propuesto_la_entidad  (label: 'la entidad')
    - Sujeto_propuesto_la_entidad__ext  (label: 'la entidad')
```

### S8 — WARN

WARN — Colisión de label normalizado entre types distintos.

**Resultado:** 31 grupos con el mismo label normalizado en types distintos.

```
'acceso al mercado de cambios para pago al exterior' (3 nodos):
    - [Operacion] Operacion_acceso_al_mercado_de_cambios_para_pago_al_exterior__ext_10_4_2_63c1c2
    - [Potestad] Potestad_acceso_al_mercado_de_cambios_para_pago_al_exterior__la_entidad_interviniente_tie_c3cc8d
    - [Potestad] Potestad_acceso_al_mercado_de_cambios_para_pago_al_exterior__la_entidad_podra_dar_acceso__25765f
'acceso al mercado de cambios para pagos de servicios' (3 nodos):
    - [Operacion] Operacion_acceso_al_mercado_de_cambios_para_pagos_de_servicios__ext_13_4_b33276
    - [Potestad] Potestad_acceso_al_mercado_de_cambios_para_pagos_de_servicios__las_entidades_estan_facult_2541aa
    - [Potestad] Potestad_acceso_al_mercado_de_cambios_para_pagos_de_servicios__las_entidades_estan_facult_3307dd
'activos admitidos como garantia' (2 nodos):
    - [Condicion] Condicion_activos_admitidos_como_garantia__la_proteccion_debe_consistir_en_alguno_de_los_a_0cc173
    - [Definicion] Definicion_activos_admitidos_como_garantia__aquellos_listados_en_los_puntos_5_3_1_2_o_5_3_2_a0f455
'adquisicion de titulos valores con liquidacion en moneda extranjera' (2 nodos):
    - [Condicion] Condicion_adquisicion_de_titulos_valores_con_liquidacion_en_moneda_extranjera__los_titulos_3468f2
    - [Operacion] Operacion_adquisicion_de_titulos_valores_con_liquidacion_en_moneda_extranjera__ext_8_5_20__0cd234
'aplicacion de divisas de cobros a cancelacion de vencimientos' (2 nodos):
    - [Obligacion] Obligacion_se_admitira_la_aplicacion_de_divisas_de_cobros_de_exportaciones_de_bienes_a_la_c_88452c
    - [Operacion] Operacion_aplicacion_de_divisas_de_cobros_a_cancelacion_de_vencimientos__ext_7_11_1_bb7cfc
'canje y/o arbitraje con fondos en moneda extranjera' (3 nodos):
    - [Condicion] Condicion_canje_y_o_arbitraje_con_fondos_en_moneda_extranjera__la_operacion_se_concreta_me_43ed8f
    - [Operacion] Operacion_canje_y_o_arbitraje_con_fondos_en_moneda_extranjera__ext_10_10_2_14_325767
    - [Operacion] Operacion_canje_y_o_arbitraje_con_fondos_en_moneda_extranjera__ext_13_3_9_f12094
'certificacion de acceso al mercado de cambios' (2 nodos):
    - [Condicion] Condicion_certificacion_de_acceso_al_mercado_de_cambios__la_entidad_debe_contar_con_certif_49c9b6
    - [Obligacion] Obligacion_la_entidad_debe_contar_con_una_certificacion_para_el_acceso_al_mercado_de_cambio_091dae
'compra de moneda extranjera para garantias' (3 nodos):
    - [Condicion] Condicion_compra_de_moneda_extranjera_para_garantias__el_acceso_se_condiciona_a_que_la_com_c8c356
    - [Operacion] Operacion_compra_de_moneda_extranjera_para_garantias__ext_3_11_1_260284
    - [Operacion] Operacion_compra_de_moneda_extranjera_para_garantias__ext_7_9_6_97386f
'computo de plazos sin interrupcion por renovaciones' (2 nodos):
    - [Condicion] Condicion_computo_de_plazos_sin_interrupcion_por_renovaciones__el_computo_de_los_plazos_de_53c493
    - [Obligacion] Obligacion_el_computo_de_los_plazos_de_atrasos_no_se_interrumpira_por_el_otorgamiento_de_re_6a48c7
'conformidad previa bcra — acceso mercado cambios' (5 nodos):
    - [Obligacion] Obligacion_las_entidades_deberan_obtener_conformidad_previa_del_bcra_para_acceder_al_mercad_ec7e8c
    - [Obligacion] Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_930255
    - [Obligacion] Obligacion_obtener_conformidad_previa_del_bcra_para_acceder_al_mercado_de_cambios_para_real_622122
    - [Obligacion] Obligacion_se_requerira_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_95b25d
    - [Potestad] Potestad_conformidad_previa_bcra_acceso_mercado_cambios__el_bcra_debe_otorgar_conformidad_cb6af8
'conformidad previa del bcra para acceso al mercado de cambios' (3 nodos):
    - [Obligacion] Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_f706c4
    - [Obligacion] Obligacion_se_requiere_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios__ad5761
    - [Potestad] Potestad_conformidad_previa_del_bcra_para_acceso_al_mercado_de_cambios__el_bcra_tiene_la__2a81f1
'cumplimiento de requisitos complementarios' (2 nodos):
    - [Condicion] Condicion_cumplimiento_de_requisitos_complementarios__el_residente_que_abono_las_utilidade_56354e
    - [Obligacion] Obligacion_las_entidades_deberan_cumplimentar_los_requisitos_complementarios_detallados_en__bd3b31
'declaracion en relevamiento de activos y pasivos externos' (5 nodos):
    - [Condicion] Condicion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__el_pasivo_debe_encont_0ad9a0
    - [Condicion] Condicion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__la_entidad_debe_conta_ab8dfd
    - [Condicion] Condicion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__la_operacion_debe_enc_4ca3b2
    - [Condicion] Condicion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__la_operacion_debe_enc_e95286
    - [Operacion] Operacion_declaracion_en_relevamiento_de_activos_y_pasivos_externos__ext_3_3_1_6eb660
'declaracion jurada exportador caracter genuino' (2 nodos):
    - [Condicion] Condicion_declaracion_jurada_exportador_caracter_genuino__la_entidad_debe_contar_con_decla_63af5e
    - [Obligacion] Obligacion_la_entidad_debe_contar_con_declaracion_jurada_del_exportador_respecto_al_caracte_1f1985
'descalce de plazos de vencimiento' (2 nodos):
    - [Condicion] Condicion_descalce_de_plazos_de_vencimiento__cuando_existe_descalce_de_plazos_de_vencimien_661160
    - [Definicion] Definicion_descalce_de_plazos_de_vencimiento__situacion_en_la_que_el_plazo_de_vencimiento_r_27d656
'emision de certificaciones de aplicacion de divisas' (4 nodos):
    - [Operacion] Operacion_emision_de_certificaciones_de_aplicacion_de_divisas__ext_9_3_11_bd1f81
    - [Operacion] Operacion_emision_de_certificaciones_de_aplicacion_de_divisas__ext_9_3_1_e30f26
    - [Operacion] Operacion_emision_de_certificaciones_de_aplicacion_de_divisas__ext_9_3_9_b3b62e
    - [Potestad] Potestad_emision_de_certificaciones_de_aplicacion_de_divisas__las_entidades_autorizadas_p_2b3f22
'exportacion a consumo — bienes excluidos equipaje' (2 nodos):
    - [Definicion] Definicion_exportacion_a_consumo_bienes_excluidos_equipaje__bienes_tales_como_automotores_m_38025a
    - [Operacion] Operacion_exportacion_a_consumo_bienes_excluidos_equipaje__ext_8_5_17_18_6336e1
'exposiciones minoristas no normativas' (2 nodos):
    - [Definicion] Definicion_exposiciones_minoristas_no_normativas__categoria_de_exposiciones_minoristas_que__bd984f
    - [Operacion] Operacion_exposiciones_minoristas_no_normativas__cap_2_12_6_3_d9ae14
'financiaciones rotativas (revolving)' (2 nodos):
    - [Definicion] Definicion_financiaciones_rotativas_revolving__financiaciones_en_las_cuales_los_prestatario_c1655f
    - [Operacion] Operacion_financiaciones_rotativas_revolving__cap_2_8_3_1_f03b91
'garantias directas, explicitas, irrevocables e incondicionales' (2 nodos):
    - [Condicion] Condicion_garantias_directas_explicitas_irrevocables_e_incondicionales__las_garantias_o_de_1caf50
    - [Operacion] Operacion_garantias_directas_explicitas_irrevocables_e_incondicionales__cap_5_4_1_68cb37
'gobiernos locales' (2 nodos):
    - [Definicion] Definicion_gobiernos_locales__administracion_central_de_provincias_de_la_ciudad_autonoma_de_08fb40
    - [Sujeto] Sujeto_gobierno_local
'ingreso y liquidacion de contravalor en divisas' (2 nodos):
    - [Obligacion] Obligacion_residentes_que_perciben_contravalor_por_enajenacion_de_activos_no_financieros_no_9219d4
    - [Operacion] Operacion_ingreso_y_liquidacion_de_contravalor_en_divisas__ext_7_1_1_be3c7b
'liquidacion en mercado de cambios' (3 nodos):
    - [Condicion] Condicion_liquidacion_en_mercado_de_cambios__la_financiacion_debe_estar_liquidada_en_el_me_699493
    - [Condicion] Condicion_liquidacion_en_mercado_de_cambios__los_titulos_de_deuda_deben_haber_sido_liquida_7e9594
    - [Operacion] Operacion_liquidacion_en_mercado_de_cambios__ext_2_3_e731f3
'liquidacion simultanea de financiaciones en moneda extranjera' (2 nodos):
    - [Condicion] Condicion_liquidacion_simultanea_de_financiaciones_en_moneda_extranjera__la_operacion_se_c_effdef
    - [Operacion] Operacion_liquidacion_simultanea_de_financiaciones_en_moneda_extranjera__ext_10_10_2_14_77eb84
'llevar legajo del deudor en lugar de radicacion' (2 nodos):
    - [Obligacion] Obligacion_deber_de_llevar_el_legajo_del_deudor_en_el_lugar_de_radicacion_de_la_cuenta__cla_12ee2d
    - [Operacion] Operacion_llevar_legajo_del_deudor_en_lugar_de_radicacion__cla_3_4_4_9ae76e
'mantener pendientes transferencias sin informacion minima' (2 nodos):
    - [Obligacion] Obligacion_mantener_pendientes_de_liquidacion_en_el_mercado_de_cambios_y_o_de_acreditacion__4a88d5
    - [Operacion] Operacion_mantener_pendientes_transferencias_sin_informacion_minima__ext_5_5_4_34d713
'presentacion de declaracion jurada del cliente' (2 nodos):
    - [Obligacion] Obligacion_la_entidad_debe_contar_con_una_declaracion_jurada_del_cliente_no_residente_en_la_c0b552
    - [Operacion] Operacion_presentacion_de_declaracion_jurada_del_cliente__ext_3_9_3_b95a60
'reclasificacion inmediata — atrasos mayores a 31 dias' (2 nodos):
    - [Obligacion] Obligacion_cuando_se_verifiquen_atrasos_mayores_a_31_dias_en_el_pago_de_los_servicios_de_la_37c7cd
    - [Operacion] Operacion_reclasificacion_inmediata_atrasos_mayores_a_31_dias__cla_7_2_2_1_41d5f2
'reconocimiento cobertura riesgo de credito' (2 nodos):
    - [Condicion] Condicion_reconocimiento_cobertura_riesgo_de_credito__condicion_para_la_aplicacion_de_lo_d_f33e24
    - [Operacion] Operacion_reconocimiento_cobertura_riesgo_de_credito__cap_10_3_3_3_749992
'requerir informacion con frecuencia segun garantias preferidas' (2 nodos):
    - [Obligacion] Obligacion_cuando_las_financiaciones_cuenten_con_garantias_preferidas_b_la_entidad_podra_re_f8792e
    - [Potestad] Potestad_requerir_informacion_con_frecuencia_segun_garantias_preferidas__cuando_las_finan_611862
'transferencia de riesgo de credito a terceros' (2 nodos):
    - [Condicion] Condicion_transferencia_de_riesgo_de_credito_a_terceros__se_ha_transferido_a_uno_o_mas_ter_d2d2dd
    - [Obligacion] Obligacion_la_entidad_debe_transferir_a_terceros_el_riesgo_de_credito_asociado_a_las_exposi_7cb2a7
```

### S9 — PASS

ERROR — Descripción canónica: ningún nodo tiene a la vez 'descripcion' y 'description'.

**Resultado:** 0 nodos con ambas keys.

```
Tabla por type (usa cada key / ambas / ninguna):
  Comunicacion: descripcion=0, description=0, ambas=0, ninguna=62 (total 62)
  Condicion: descripcion=1588, description=0, ambas=0, ninguna=0 (total 1588)
  Definicion: descripcion=588, description=0, ambas=0, ninguna=0 (total 588)
  Excepcion: descripcion=350, description=0, ambas=0, ninguna=0 (total 350)
  Obligacion: descripcion=1612, description=0, ambas=0, ninguna=6 (total 1618)
  Operacion: descripcion=1386, description=0, ambas=0, ninguna=0 (total 1386)
  Potestad: descripcion=317, description=0, ambas=0, ninguna=0 (total 317)
  Restriccion: descripcion=633, description=0, ambas=0, ninguna=0 (total 633)
  Sujeto: descripcion=0, description=0, ambas=0, ninguna=176 (total 176)
  TextoOrdenado: descripcion=0, description=0, ambas=0, ninguna=5 (total 5)

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

**Resultado:** Sin aplica_a: Excepcion=326, Obligacion=515, Operacion=1229, Potestad=100, Restriccion=434 (total 2604).

```
Excepcion: 326 sin aplica_a
    - Excepcion_algunos_criterios_stc_como_garantias_y_facilidades_de_liquidez_se_verifican_solo_fe3a38
    - Excepcion_ciertas_informaciones_tendran_frecuencia_trimestral_en_lugar_de_mensual__ric_1_1_3ab582
    - Excepcion_cuando_deba_recategorizarse_al_deudor_en_la_categoria_2_sera_considerado_en_obse_cafe07
    - Excepcion_cuando_el_cliente_no_dispone_de_la_documentacion_que_avala_la_capitalizacion_def_724c73
    - Excepcion_cuando_el_cliente_sea_un_vpu_adherido_al_rigi_que_declaro_ante_la_autoridad_de_a_6bc913
    - Excepcion_cuando_el_cliente_sea_un_vpu_adherido_al_rigi_que_declaro_hacer_uso_de_los_benef_28134e
    - Excepcion_cuando_el_cliente_sea_un_vpu_adherido_al_rigi_que_declaro_hacer_uso_de_los_benef_2f6458
    - Excepcion_cuando_el_cobro_de_los_servicios_o_venta_de_la_inversion_sea_percibido_en_moneda_8686cc
    - Excepcion_cuando_existan_obstaculos_para_la_rapida_repatriacion_de_beneficios_desde_una_su_d8a545
    - Excepcion_cuando_fondos_se_perciben_o_acreditan_en_el_exterior_se_considera_cumplido_el_in_e7f38d
    - Excepcion_cuando_la_entidad_emplea_valor_actual_neto_para_la_gestion_de_posiciones_se_util_63cb6b
    - Excepcion_cuando_la_exportacion_se_concrete_en_fecha_que_corresponda_menor_porcentaje_de_e_6fd707
    - Excepcion_cuando_la_garantia_cubre_unicamente_el_capital_los_intereses_y_otros_pagos_no_cu_5c61e7
    - Excepcion_cuando_la_nacionalizacion_requiere_plazo_mayor_y_el_pago_se_concreta_conforme_a__474c21
    - Excepcion_cuando_los_fletes_corresponden_a_una_operacion_de_importacion_encuadrada_en_el_p_4d69f1
    - Excepcion_cuando_margenes_de_credito_por_lineas_especificas_se_excedan_no_se_consideran_re_407e41
    - Excepcion_cuando_se_han_imputado_cobros_de_exportaciones_y_o_aplicaciones_de_divisas_al_pe_631959
    - Excepcion_cuando_sea_factible_el_computo_de_la_crc_con_descalce_de_plazos_se_reconoce_parc_a86e99
    - Excepcion_demoras_en_la_oficializacion_por_decisiones_del_importador_motivadas_en_cuestion_14903e
    - Excepcion_el_acceso_al_mercado_de_cambios_se_extiende_tambien_a_los_fideicomisos_constitui_a589fd
    - Excepcion_el_acceso_al_mercado_de_cambios_tambien_se_extiende_a_los_fideicomisos_constitui_31fb86
    - Excepcion_el_deudor_puede_reclasificarse_a_situacion_normal_cuando_se_observen_las_situaci_576e53
    - Excepcion_el_deudor_puede_reclasificarse_al_nivel_superior_en_situacion_normal_cuando_se_h_e511de
    - Excepcion_el_factor_de_1_5_no_se_aplica_cuando_cva_no_es_aplicable_en_exposiciones_con_ent_a1691b
    - Excepcion_el_importe_resultante_del_ajuste_por_volatilidad_no_sera_inferior_en_el_caso_de__c82567
    - Excepcion_el_importe_resultante_del_ajuste_por_volatilidad_no_sera_superior_en_el_caso_de__9c1271
    - Excepcion_el_limite_de_usd_50_se_incrementa_a_usd_200_por_operacion_cuando_los_retiros_de__795cff
    - Excepcion_el_limite_del_40_no_aplica_cuando_el_deudor_contaba_con_una_certificacion_de_aum_7c41e5
    - Excepcion_el_limite_del_40_no_aplica_cuando_el_deudor_contaba_con_una_certificacion_por_lo_6bde76
    - Excepcion_el_limite_del_40_no_aplica_cuando_el_deudor_registraba_liquidaciones_en_el_merca_a18797
    - Excepcion_el_limite_del_40_no_aplica_cuando_el_deudor_registraba_liquidaciones_en_el_merca_ef134b
    - Excepcion_el_mantenimiento_por_parte_de_la_cedente_de_la_administracion_de_las_exposicione_154e1a
    - Excepcion_el_margen_inicial_no_comprende_los_aportes_a_la_ccp_en_concepto_de_acuerdos_para_482ca5
    - Excepcion_el_plazo_de_90_dias_no_aplica_a_las_ventas_con_liquidacion_contra_cable_en_cuent_65bfb8
    - Excepcion_el_plazo_de_dos_anos_desde_el_primer_ingreso_de_divisas_puede_computarse_como_pa_0e125d
    - Excepcion_el_plazo_de_dos_anos_desde_el_primer_ingreso_de_divisas_puede_computarse_como_pa_6e1f70
    - Excepcion_el_punto_3_16_3_no_aplica_a_clientes_que_sean_personas_humanas_residentes__ext_4_d9364f
    - Excepcion_el_punto_3_16_3_no_es_aplicable_para_clientes_que_sean_personas_humanas_resident_1b5e2b
    - Excepcion_el_regimen_de_equipaje_queda_exceptuado_del_seguimiento_de_negociaciones_de_divi_c923b3
    - Excepcion_el_regimen_de_exportacion_para_compensar_envios_con_deficiencias_queda_exceptuad_d81053
    - Excepcion_el_regimen_de_muestras_queda_exceptuado_del_seguimiento_de_permisos_de_embarque__aff595
    - Excepcion_el_regimen_de_pacotilla_queda_exceptuado_del_seguimiento_de_divisas_por_exportac_3e5aed
    - Excepcion_el_regimen_de_removido_queda_exceptuado_del_seguimiento_de_negociaciones_de_divi_ba43a2
    - Excepcion_el_requerimiento_de_debida_diligencia_no_aplica_a_exposiciones_a_gobiernos_y_ban_8b95eb
    - Excepcion_el_requisito_complementario_para_egresos_no_aplica_cuando_el_vpu_accede_al_merca_4ad6fe
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_aplica_cuando_la_operacion_encuad_4a6a75
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_aplica_cuando_la_operacion_encuad_4c3318
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_aplica_cuando_la_operacion_encuad_6a6b44
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_aplica_para_las_cancelaciones_de__9e4229
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_resultara_aplicable_cuando_la_ope_3e1a92
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_resultara_aplicable_cuando_la_ope_c482f5
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_resultara_aplicable_cuando_se_cum_1d239f
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_se_aplica_a_los_fideicomisos_cons_38e914
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_se_aplica_a_organizaciones_empres_37f9c6
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_se_aplica_al_sector_publico__ext__f09df2
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_para_acceso_al_mercado_de_cambios_no_f72214
    - Excepcion_el_requisito_de_no_realizar_el_pago_con_anterioridad_al_vencimiento_no_aplica_cu_2b736e
    - Excepcion_el_requisito_de_que_el_cliente_no_registre_situaciones_de_demora_no_sera_de_apli_564910
    - Excepcion_el_requisito_de_que_el_cliente_no_registre_situaciones_de_demora_no_sera_de_apli_797559
    - Excepcion_el_requisito_de_que_el_cliente_no_registre_situaciones_de_demora_no_sera_de_apli_9392a4
    - Excepcion_el_requisito_de_que_el_cliente_no_registre_situaciones_de_demora_no_sera_de_apli_d20a1a
    - Excepcion_el_tratamiento_de_exposicion_al_sector_publico_no_financiero_no_aplica_cuando_el_7992a0
    - Excepcion_en_situaciones_especiales_que_se_detallan_a_continuacion_se_admitira_tambien_la__821fc2
    - Excepcion_excepcion_a_la_aplicacion_del_mayor_aforo_cuando_la_entidad_pueda_aplicar_el_enf_322f58
    - Excepcion_excepcion_a_la_exigencia_de_conformidad_previa_del_bcra_para_acceso_al_mercado_d_795196
    - Excepcion_excepcion_a_la_exigencia_de_conformidad_previa_del_bcra_para_pagos_de_servicios__739ad0
    - Excepcion_excepcion_a_la_exigencia_de_ead_positiva_la_ead_de_un_conjunto_de_neteo_que_comp_ba3faf
    - Excepcion_excepcion_a_la_obligacion_de_permanecer_180_dias_en_la_categoria_cuando_por_apli_238f47
    - Excepcion_excepcion_a_la_prohibicion_de_acceso_al_mercado_de_cambios_para_el_pago_de_deuda_6cd392
    - Excepcion_excepcion_a_la_prohibicion_de_acceso_al_mercado_de_cambios_para_la_cancelacion_e_a6a6c7
    - Excepcion_excepcion_a_la_prohibicion_de_aplicar_incumplido_en_gestion_de_cobro_cuando_la_f_8bb39b
    - Excepcion_excepcion_a_la_restriccion_de_consignar_importes_sin_signo_se_permite_informar_c_d6d789
    - Excepcion_excepcion_a_la_suspension_del_envio_de_informaciones_con_codigo_de_consolidacion_6e93d3
    - Excepcion_excepcion_a_permanencia_de_180_dias_puede_categorizarse_en_nivel_inferior_si_otr_bf1260
    - Excepcion_excepcion_al_limite_del_40_cuando_por_un_monto_igual_o_superior_al_excedente_el__6bec98
    - Excepcion_excepcion_al_ponderador_minimo_del_20_conforme_a_lo_dispuesto_en_el_punto_5_3_1__afd5e2
    - Excepcion_excepcion_al_requisito_de_conformidad_previa_del_bcra_cuando_el_pago_de_interese_9dc914
    - Excepcion_excepcion_al_requisito_de_conformidad_previa_del_bcra_cuando_el_pago_de_interese_b27a7b
    - Excepcion_excepcion_de_liquidacion_de_cobros_de_exportaciones_de_bienes_y_servicios_para_l_a4c243
    - Excepcion_excepcion_futuros_cuyo_subyacente_sea_un_titulo_de_deuda_o_indice_de_titulos_de__b7695f
    - Excepcion_excepcionalmente_mediando_autorizacion_previa_de_la_sefyc_podran_admitirse_aport_e91a54
    - Excepcion_exceptua_el_requisito_de_conformidad_previa_del_bcra_para_el_acceso_al_mercado_d_0e351b
    - Excepcion_exclusion_de_tenencias_de_titulos_valores_suscriptos_para_ser_colocados_dentro_d_45c622
    - Excepcion_exencion_de_la_exigencia_de_capital_adicional_de_2_cuando_la_entidad_asume_la_po_02af66
    - Excepcion_exencion_de_la_exigencia_de_capital_adicional_de_2_cuando_la_entidad_mantiene_la_64807b
    - Excepcion_exencion_del_requisito_de_ingreso_de_divisas_para_exportaciones_al_area_franca_c_9731bb
    - Excepcion_exencion_del_seguimiento_de_ingreso_de_divisas_para_exportaciones_del_area_aduan_c391ff
    - Excepcion_garantia_de_cliente_mantenida_por_custodio_y_protegida_contra_quiebra_de_ccp_mie_1b71a1
    - Excepcion_garantia_de_miembro_compensador_efectivo_titulos_otros_activos_excesos_de_margen_f1677a
    - Excepcion_gastos_en_inmuebles_y_otros_activos_fijos_derivados_de_eventos_de_perdida_por_ri_3977b6
    - Excepcion_la_cancelacion_discrecional_de_dividendos_o_intereses_no_constituye_por_si_sola__360a9e
    - Excepcion_la_cancelacion_discrecional_de_dividendos_o_intereses_no_faculta_a_los_tenedores_f6fe9b
    - Excepcion_la_condicion_de_que_conste_en_el_permiso_de_embarque_la_ventaja_aduanera_exponot_936d9e
    - Excepcion_la_conformidad_previa_del_bcra_no_es_requerida_cuando_la_entidad_cuenta_con_una__cd9beb
    - Excepcion_la_conformidad_previa_del_bcra_se_considera_cumplida_cuando_el_cliente_registra__7da372
    - Excepcion_la_constancia_de_aceptacion_de_la_nueva_entidad_libera_a_la_entidad_previa_de_su_7aebd3
    - Excepcion_la_declaracion_jurada_del_cliente_respecto_a_sus_tenencias_de_activos_externos_l_9a2ec8
    - Excepcion_la_designacion_de_personal_con_funciones_de_representacion_no_implica_una_delega_414e35
    - Excepcion_la_entidad_previa_queda_liberada_de_sus_obligaciones_hacia_adelante_una_vez_que__0f1c80
    - Excepcion_la_exigencia_de_documentacion_en_braille_no_aplica_a_comprobantes_de_operaciones_4d7e15
    - Excepcion_la_incorporacion_de_creditos_en_periodos_de_rotacion_o_su_sustitucion_recompra_p_49376d
    - Excepcion_la_instalacion_de_oficinas_de_representacion_en_el_exterior_esta_permitida_cuand_61a953
    - Excepcion_la_liquidacion_de_las_divisas_remitidas_a_la_entidad_local_por_la_contraparte_pa_ed793b
    - Excepcion_la_operacion_no_queda_comprendida_por_el_requisito_de_conformidad_previa_cuando__49ca9d
    - Excepcion_la_prohibicion_de_acceso_al_mercado_de_cambios_no_aplica_cuando_la_repatriacion__cb334c
    - Excepcion_la_prohibicion_de_acelerar_la_devolucion_de_pagos_futuros_no_aplica_en_caso_de_q_ee0036
    - Excepcion_la_prohibicion_de_clasificacion_no_afecta_la_obligacion_de_informar_segun_las_no_c7c2c0
    - Excepcion_la_renta_obtenida_por_el_alquiler_a_no_residentes_de_inmuebles_ubicados_en_el_pa_d256a4
    - Excepcion_la_restriccion_de_permanencia_minima_aplica_aun_cuando_el_deudor_haya_cancelado__a7b0ae
    - Excepcion_las_asistencias_crediticias_otorgadas_a_clientes_sin_asistencia_previa_no_seran__c12237
    - Excepcion_las_asistencias_otorgadas_en_las_condiciones_del_segundo_parrafo_del_punto_6_5_n_e2ee81
    - Excepcion_las_cajas_de_ahorros_en_pesos_cuando_se_encuentren_abiertas_quedan_exceptuadas_d_536eb1
    - Excepcion_las_concertaciones_y_cancelaciones_de_operaciones_de_futuros_en_mercados_regulad_d69f60
    - Excepcion_las_condiciones_de_no_anticipacion_de_vencimientos_y_no_realizacion_de_pagos_ant_bfa635
    - Excepcion_las_entidades_no_observaran_la_exigencia_de_capital_por_cva_cuando_se_trate_de_o_41aa33
    - Excepcion_las_entidades_no_observaran_la_exigencia_de_capital_por_cva_en_operaciones_celeb_bcd8d9
    - Excepcion_las_entidades_pueden_considerar_como_operacion_garantizada_por_una_agencia_ofici_b711f8
    - Excepcion_las_exportaciones_a_zonas_francas_nacionales_quedan_exceptuadas_del_seguimiento__614b11
    - Excepcion_las_exportaciones_de_bienes_efectuadas_por_un_vpu_adherido_al_rigi_por_un_proyec_71be79
    - Excepcion_las_exportaciones_de_bienes_enviados_al_exterior_con_fines_promocionales_amparad_17c336
    - Excepcion_las_exportaciones_desde_el_territorio_nacional_continental_al_area_aduanera_espe_7e7921
    - Excepcion_las_exposiciones_a_instrumentos_previstas_en_el_punto_2_11_quedan_excluidas_de_l_761376
    - Excepcion_las_garantias_otorgadas_a_favor_del_bcra_y_por_obligaciones_directas_quedan_excl_93e113
    - Excepcion_las_hipotecas_sobre_inmuebles_rurales_constituidas_como_garantias_adicionales_se_1068ad
    - Excepcion_las_inversiones_directas_en_el_exterior_no_forman_parte_de_la_posicion_general_d_bc8382
    - Excepcion_las_inversiones_en_acciones_estructuradas_cuyo_objeto_es_replicar_la_realidad_ec_b1f258
    - Excepcion_las_liquidaciones_en_la_operatoria_con_titulos_valores_por_cuenta_y_orden_de_tur_e471cd
    - Excepcion_las_modificaciones_que_resulten_economicamente_mas_beneficiosas_para_el_usuario__526fa3
    - Excepcion_las_obligaciones_negociables_compradas_que_constituyen_emisiones_propias_quedan__ed3fd2
    - Excepcion_las_opciones_sobre_acciones_e_indices_bursatiles_quedan_exceptuadas_del_computo__ec1185
    - Excepcion_las_operaciones_aduaneras_correspondientes_al_regimen_de_franquicia_diplomatica__8c20c8
    - Excepcion_las_operaciones_de_repatriacion_de_inversiones_de_no_residentes_y_otras_compras__06b419
    - Excepcion_las_operaciones_de_trasbordo_quedan_exceptuadas_del_seguimiento_de_negociaciones_953d1f
    - Excepcion_las_operaciones_pueden_mantener_el_tratamiento_de_qccp_durante_tres_meses_despue_1b6715
    - Excepcion_las_primas_por_opciones_de_compra_y_de_venta_tomadas_quedan_excluidas_de_las_fin_03237b
    - Excepcion_las_refinanciaciones_otorgadas_a_productores_agropecuarios_derivadas_de_la_aplic_6ad645
    - Excepcion_las_ventas_y_compras_a_termino_de_divisas_o_valores_externos_no_forman_parte_de__2bd0ac
    - Excepcion_los_activos_externos_de_terceros_en_custodia_no_forman_parte_de_la_posicion_gene_073141
    - Excepcion_los_creditos_frente_al_banco_central_de_la_republica_argentina_quedan_excluidos__748419
    - Excepcion_los_creditos_para_consumo_o_vivienda_quedan_exceptuados_de_la_cartera_comercial__956a9c
    - Excepcion_los_defectos_originados_en_el_computo_del_50_en_lugar_del_100_de_los_resultados__0ee001
    - Excepcion_los_demas_activos_locales_en_moneda_extranjera_no_forman_parte_de_la_posicion_ge_843db8
    - Excepcion_los_depositos_en_el_bcra_en_moneda_extranjera_en_cuentas_a_nombre_de_la_entidad__e04a8a
    - Excepcion_los_incisos_i_iii_y_iv_del_punto_10_3_2_1_quedan_reemplazados_por_requisitos_dis_ef5b0e
    - Excepcion_los_margenes_acordados_para_descubiertos_en_cuenta_corriente_los_limites_de_comp_135d17
    - Excepcion_los_permisos_que_revistan_la_condicion_de_incumplido_en_gestion_de_cobro_no_sera_91c91a
    - Excepcion_los_sobregiros_en_cuenta_corriente_bancaria_que_excedan_margenes_acordados_o_sin_411236
    - Excepcion_los_titulos_de_credito_son_deducibles_cuando_su_registro_o_custodia_se_encuentre_3bcb82
    - Excepcion_los_titulos_de_credito_son_deducibles_cuando_su_registro_o_custodia_se_encuentre_7b2568
    - Excepcion_los_titulos_de_credito_son_deducibles_cuando_su_registro_o_custodia_se_encuentre_b1d640
    - Excepcion_los_titulos_valores_emitidos_por_la_contraparte_o_un_vinculado_a_ella_no_son_adm_5e0be2
    - Excepcion_no_aplica_el_plazo_maximo_de_diez_10_dias_habiles_cuando_i_se_trata_de_la_situac_6123a1
    - Excepcion_no_aplica_el_tratamiento_del_punto_4_3_a_los_casos_contemplados_en_el_punto_4_1__d8cdd7
    - Excepcion_no_aplica_la_facultad_de_exclusion_cuando_las_cantidades_de_ingresos_y_egresos_f_a5ea17
    - Excepcion_no_aplica_la_obligacion_de_cancelacion_con_fondos_de_cobros_de_exportacion_cuand_38c9ce
    - Excepcion_no_aplica_la_obligacion_de_disponibilidad_publica_cuando_se_trata_de_evaluacione_d0cab3
    - Excepcion_no_aplica_la_obligacion_de_liquidacion_en_mercado_de_cambios_al_desembolso_cuand_0e7536
    - Excepcion_no_aplica_la_permanencia_minima_de_180_dias_si_por_aplicacion_de_otras_pautas_co_b3f551
    - Excepcion_no_aplican_los_requisitos_de_declaracion_jurada_de_los_puntos_3_16_3_1_a_3_16_3__6e9660
    - Excepcion_no_aplican_los_requisitos_de_declaracion_jurada_de_los_puntos_3_16_3_1_a_3_16_3__8c538c
    - Excepcion_no_aplican_los_requisitos_de_declaracion_jurada_de_los_puntos_3_16_3_1_a_3_16_3__9fa252
    - Excepcion_no_aplican_los_requisitos_de_declaracion_jurada_de_los_puntos_3_16_3_1_a_3_16_3__e1d560
    - Excepcion_no_es_necesaria_la_presentacion_de_declaracion_jurada_por_parte_de_entes_del_sec_1e688a
    - Excepcion_no_es_obligatoria_evaluacion_de_capacidad_de_pago_por_ingresos_del_prestatario_c_51b967
    - Excepcion_no_es_obligatoria_la_apertura_del_legajo_en_los_casos_de_deudores_por_servicios__1fee27
    - Excepcion_no_es_obligatorio_incorporar_flujo_de_fondos_estados_contables_ni_informacion_pa_b350ee
    - Excepcion_no_resulta_aplicable_el_requisito_de_verificacion_de_la_fecha_de_vencimiento_del_902a1f
    - Excepcion_no_resultan_aplicables_los_requisitos_de_los_puntos_4_3_2_1_y_4_3_2_2_en_las_com_c4da8f
    - Excepcion_no_resultara_aplicable_el_requisito_de_conformidad_previa_cuando_el_cliente_cuen_cf5ae1
    - Excepcion_no_resultara_aplicable_el_requisito_de_conformidad_previa_del_bcra_cuando_se_tra_908c0e
    - Excepcion_no_se_aplica_el_plazo_minimo_de_20_dias_habiles_para_calculo_de_mpor_en_conjunto_55c988
    - Excepcion_no_se_aplica_el_requisito_de_inmueble_terminado_a_las_financiaciones_a_personas__94075b
    - Excepcion_no_se_aplica_el_requisito_de_inmueble_terminado_a_los_inmuebles_rurales__cap_2_9_134c21
    - Excepcion_no_se_clasifican_en_la_categoria_irrecuperable_los_deudores_cuando_las_financiac_b48e28
    - Excepcion_no_se_considera_refinanciacion_la_asistencia_a_deudores_en_situacion_normal_que__62369c
    - Excepcion_no_se_consideran_activos_externos_liquidos_disponibles_los_fondos_depositados_en_5cc339
    - Excepcion_no_se_consideran_en_el_computo_las_exportaciones_a_consumo_con_despacho_de_impor_06995e
    - Excepcion_no_se_consideran_en_el_computo_los_bienes_exportados_a_traves_de_operaciones_exc_17098a
    - Excepcion_no_se_consideran_en_el_computo_los_bienes_que_cuenten_con_las_ventajas_aduaneras_b40852
    - Excepcion_no_se_consideran_refinanciaciones_las_otorgadas_a_productores_cuando_resulten_de_59f60f
    - Excepcion_no_se_consideraran_las_inversiones_obligatorias_que_deban_realizar_las_sucursale_1bd8b2
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_bancos_u_otr_0cafa1
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_la_casa_matr_a64805
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_otros_bancos_e9ef5e
    - Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_sucursales_y_804456
    - Excepcion_no_se_deduciran_los_saldos_que_con_caracter_transitorio_y_circunstancial_se_orig_129ec9
    - Excepcion_no_se_incluyen_los_ingresos_de_importaciones_temporarias_sin_giro_de_divisas_en__2f0aae
    - Excepcion_no_se_incluyen_los_registros_aduaneros_por_importaciones_suspensivas_de_deposito_37c1f3
    - Excepcion_no_se_reconoce_la_proteccion_crediticia_cuando_una_entidad_financiera_compra_pro_20ddc6
    - Excepcion_no_se_requerira_la_conformidad_previa_del_bcra_cuando_la_entidad_constate_que_el_da4f1e
    - Excepcion_no_se_requiere_conformidad_previa_cuando_se_trate_de_endeudamiento_financiero_co_590fb0
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_cuando_el_cliente_es_un_vpu_adherido__7613fb
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_cuando_el_endeudamiento_financiero_en_c27534
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_cuando_el_pago_corresponda_a_cancelac_ecd002
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_cuando_la_entidad_verifica_adicionalm_a2e009
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_cuando_la_operacion_encuadra_en_finan_b07e82
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios__28d5ad
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_si_el_deudor_encuadra_en_alguna_de_la_642184
    - Excepcion_no_se_requiere_la_conformidad_previa_del_bcra_cuando_el_cliente_cuente_con_una_c_c551e9
    - Excepcion_no_se_requiere_la_conformidad_previa_del_bcra_cuando_el_pago_encuadra_en_alguna__48c4a7
    - Excepcion_no_se_requiere_la_conformidad_previa_del_bcra_si_tal_requisito_estuviese_vigente_d1ad37
    - Excepcion_no_sera_aplicable_lo_dispuesto_en_el_articulo_197_de_la_ley_general_de_sociedade_b1a072
    - Excepcion_no_sera_exigible_la_liquidacion_en_el_mercado_de_cambios_de_fondos_en_moneda_ext_11e2d9
    - Excepcion_no_sera_obligatoria_la_apertura_del_legajo_en_los_casos_de_deudores_por_servicio_90a2a5
    - Excepcion_operacion_aduanera_exceptuada_del_seguimiento_de_divisas_por_exportaciones_de_bi_d09dfb
    - Excepcion_operacion_aduanera_exceptuada_del_seguimiento_de_permiso_de_embarque_por_el_valo_7a63d9
    - Excepcion_operacion_aduanera_exceptuada_del_seguimiento_de_permisos_de_embarque_por_el_reg_3f0d8c
    - Excepcion_operacion_exceptuada_del_seguimiento_de_divisas_por_exportaciones_de_bienes_por__6c3e8d
    - Excepcion_operacion_exceptuada_del_seguimiento_de_divisas_por_exportaciones_exportacion_a__11a101
    - Excepcion_operacion_exceptuada_del_seguimiento_de_permisos_de_embarque_por_el_valor_que_co_a2b7b5
    - Excepcion_operaciones_de_envios_de_asistencia_y_salvamento_quedan_exceptuadas_del_seguimie_9a7b16
    - Excepcion_para_entidades_con_codigo_3_en_el_caso_de_riesgo_de_mercado_y_riesgo_operacional_54677f
    - Excepcion_para_exposiciones_subyacentes_a_operaciones_con_derivados_realizadas_por_el_fond_bd73d5
    - Excepcion_para_financiaciones_otorgadas_a_partir_del_14_04_25_se_admite_que_el_vencimiento_fd8077
    - Excepcion_para_modificaciones_en_los_valores_de_comisiones_y_o_cargos_debidamente_aceptado_be2e4c
    - Excepcion_para_operaciones_comprendidas_en_el_punto_7_11_1_6_se_admite_la_cancelacion_de_i_cfcb67
    - Excepcion_para_operaciones_del_concepto_s30_servicios_de_fletes_por_operaciones_de_importa_097d85
    - Excepcion_provisiones_relacionadas_con_eventos_de_perdidas_por_riesgo_operacional_si_contr_d394cd
    - Excepcion_queda_exceptuada_la_condicion_prevista_en_el_inciso_viii_del_punto_10_3_2_1_para_2af89a
    - Excepcion_queda_exceptuada_la_exigencia_de_conformidad_previa_del_bcra_cuando_la_entidad_c_775604
    - Excepcion_queda_exceptuada_la_exigencia_de_conformidad_previa_del_bcra_para_el_acceso_al_m_925684
    - Excepcion_queda_exceptuada_la_prohibicion_de_acceso_al_mercado_de_cambios_para_la_cancelac_bffd7e
    - Excepcion_queda_exceptuada_la_prohibicion_de_prever_pago_de_capital_en_caso_de_liquidacion_55719e
    - Excepcion_queda_exceptuada_la_restriccion_de_acceso_al_mercado_de_cambios_cuando_el_pago_s_7285db
    - Excepcion_quedan_exceptuadas_de_la_clasificacion_de_financiaciones_las_compras_a_termino_p_d8cf5c
    - Excepcion_quedan_exceptuadas_de_la_clasificacion_las_garantias_otorgadas_a_favor_del_banco_6b6ab5
    - Excepcion_quedan_exceptuadas_de_la_exigencia_de_conformidad_previa_del_bcra_las_operacione_685962
    - Excepcion_quedan_exceptuadas_de_la_exigencia_de_conformidad_previa_del_bcra_las_operacione_f131d7
    - Excepcion_quedan_exceptuadas_de_la_exigencia_de_conformidad_previa_del_bcra_las_transferen_31329a
    - Excepcion_quedan_exceptuadas_de_la_obligacion_de_llevar_a_cabo_el_seguimiento_las_entidade_c40d8a
    - Excepcion_quedan_exceptuadas_de_la_prohibicion_de_entrega_de_fondos_o_activos_a_personas_v_83f3bf
    - Excepcion_quedan_exceptuadas_de_la_prohibicion_de_liquidacion_mediante_deposito_en_cuentas_81c0bd
    - Excepcion_quedan_exceptuadas_de_la_prohibicion_de_ponderador_menor_para_deudores_no_califi_c515ac
    - Excepcion_quedan_exceptuadas_de_la_prohibicion_las_emisiones_de_titulos_de_deuda_realizada_743f77
    - Excepcion_quedan_exceptuadas_de_la_prohibicion_las_operaciones_concertadas_en_el_pais_que__7314f5
    - Excepcion_quedan_exceptuadas_del_alcance_de_las_garantias_comprendidas_las_garantias_otorg_b97cd3
    - Excepcion_quedan_exceptuadas_del_alcance_de_las_normas_sobre_proveedores_no_financieros_de_f8a3ba
    - Excepcion_quedan_exceptuadas_del_plazo_de_60_dias_las_exportaciones_de_las_posiciones_aran_61ca34
    - Excepcion_quedan_exceptuadas_del_plazo_de_60_dias_las_exportaciones_de_las_posiciones_aran_7c43a6
    - Excepcion_quedan_exceptuadas_del_requisito_de_conformidad_previa_del_bcra_las_transferenci_11f54f
    - Excepcion_quedan_exceptuadas_del_requisito_de_ponderador_no_inferior_al_de_la_jurisdiccion_7ca369
    - Excepcion_quedan_exceptuadas_del_seguimiento_las_exportaciones_a_consumo_de_bienes_excluid_91dc80
    - Excepcion_quedan_exceptuadas_del_seguimiento_las_exportaciones_a_consumo_de_bienes_que_con_0cdfce
    - Excepcion_quedan_exceptuadas_del_seguimiento_las_operaciones_aduaneras_correspondientes_al_02b73f
    - Excepcion_quedan_exceptuadas_del_seguimiento_las_operaciones_aduaneras_de_los_subregimenes_cb964d
    - Excepcion_quedan_exceptuadas_del_seguimiento_las_operaciones_aduaneras_detalladas_en_el_pu_755ad7
    - Excepcion_quedan_exceptuadas_del_seguimiento_las_operaciones_aduaneras_realizadas_mediante_7283c7
    - Excepcion_quedan_exceptuadas_las_entidades_financieras_y_casas_de_cambio_que_hayan_notific_2e913d
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_20_10_realizadas_po_681e4e
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_20_21_realizadas_po_935cb3
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_20_22_realizadas_po_d82fde
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_20_90_realizadas_po_ef78aa
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_30_10_realizadas_po_b41efb
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_30_21_realizadas_po_204741
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_30_29_realizadas_po_a6f183
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_30_31_realizadas_po_40a657
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_30_39_realizadas_po_cd1aa8
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_30_90_realizadas_po_09bc83
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_40_10_realizadas_po_486382
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_40_90_realizadas_po_e049d8
    - Excepcion_quedan_exceptuadas_las_situaciones_de_fuerza_mayor_ajenas_a_la_voluntad_del_impo_8c302b
    - Excepcion_quedan_exceptuados_de_esta_condicion_los_deudores_comprendidos_en_el_punto_6_5_2_0a6ac9
    - Excepcion_quedan_exceptuados_de_la_clasificacion_de_deudores_los_anticipos_por_pago_de_jub_393494
    - Excepcion_quedan_exceptuados_de_la_clasificacion_de_deudores_los_anticipos_y_prestamos_al__ea5289
    - Excepcion_quedan_exceptuados_de_la_clasificacion_de_deudores_los_deudores_por_pases_activo_4242cf
    - Excepcion_quedan_exceptuados_de_la_clasificacion_en_irrecuperable_los_deudores_en_concurso_e0afc3
    - Excepcion_quedan_exceptuados_de_la_obligacion_de_liquidacion_los_cobros_de_exportaciones_d_5097bc
    - Excepcion_quedan_exceptuados_de_la_obligacion_de_liquidacion_los_cobros_de_exportaciones_d_62ea28
    - Excepcion_quedan_exceptuados_de_la_obligacion_de_liquidacion_los_cobros_de_exportaciones_d_697ee1
    - Excepcion_quedan_exceptuados_de_la_obligacion_de_presentar_declaracion_jurada_los_deudores_5290f6
    - Excepcion_quedan_exceptuados_de_la_prohibicion_de_entrega_de_activos_locales_los_fondos_en_fd967a
    - Excepcion_quedan_exceptuados_de_la_prohibicion_de_entregar_fondos_en_moneda_local_u_otros__3998c2
    - Excepcion_quedan_exceptuados_de_la_restriccion_los_inmuebles_adquiridos_mediante_subasta_j_104d53
    - Excepcion_quedan_exceptuados_de_los_requisitos_de_anterioridad_y_plazo_minimo_desde_emisio_274e7c
    - Excepcion_quedan_exceptuados_del_regimen_de_aportes_en_efectivo_la_negociacion_de_acciones_33d6a6
    - Excepcion_quedan_exceptuados_del_requisito_de_conformidad_previa_los_pagos_de_intereses_co_c5d782
    - Excepcion_quedan_exceptuados_del_requisito_de_demostrar_ingreso_y_liquidacion_de_divisas_e_8a218a
    - Excepcion_quedan_excluidas_de_la_exigencia_de_capital_por_riesgo_de_credito_de_contraparte_6a7c99
    - Excepcion_quedan_excluidas_de_las_exposiciones_minoristas_las_exposiciones_con_garantia_hi_701361
    - Excepcion_quedan_excluidas_de_los_conceptos_comprendidos_las_posiciones_en_acciones_en_la__1d53cf
    - Excepcion_quedan_excluidas_del_alcance_de_este_punto_las_exposiciones_previstas_en_el_punt_5bd492
    - Excepcion_quedan_excluidas_del_computo_de_la_exigencia_de_capital_las_operaciones_de_pase__3b2a22
    - Excepcion_quedan_excluidos_de_la_definicion_de_divisas_en_moneda_extranjera_las_monedas_y__2658b5
    - Excepcion_quedan_excluidos_de_los_conceptos_comprendidos_los_activos_fijos__ric_11_1_9495fe
    - Excepcion_quedan_excluidos_de_los_conceptos_comprendidos_los_activos_que_se_deducen_del_ca_690cfb
    - Excepcion_se_admite_computar_el_valor_de_los_fletes_no_incluidos_en_la_condicion_de_compra_9b6f8a
    - Excepcion_se_admite_la_constitucion_de_garantias_en_cuentas_abiertas_en_entidades_financie_4dccaf
    - Excepcion_se_admite_que_el_legajo_del_cliente_este_en_lugar_distinto_del_de_radicacion_de__265175
    - Excepcion_se_aplicara_un_ponderador_del_10_a_entidades_del_exterior_que_no_cumplan_con_lo__0482b5
    - Excepcion_se_considera_como_operacion_garantizada_por_agencia_oficial_de_credito_aquella_c_0cb920
    - Excepcion_se_exceptua_del_limite_de_depositos_el_crecimiento_originado_por_el_devengamient_16c011
    - Excepcion_se_exceptua_del_requisito_de_conformidad_previa_del_bcra_cuando_el_deudor_encuad_a23a55
    - Excepcion_se_exceptua_del_requisito_de_conformidad_previa_del_bcra_para_acceso_al_mercado__2f2a40
    - Excepcion_se_exceptua_del_requisito_de_demostrar_ingreso_y_liquidacion_de_divisas_en_el_me_e2dc16
    - Excepcion_se_exceptua_el_requisito_de_cumplimiento_de_los_requisitos_establecidos_para_el__f53f5c
    - Excepcion_se_exceptua_el_requisito_de_que_el_valor_del_inmueble_corresponda_al_del_momento_326899
    - Excepcion_se_exceptua_el_requisito_de_que_el_valor_del_inmueble_corresponda_al_del_momento_64e0e5
    - Excepcion_se_exceptua_el_requisito_de_que_el_valor_del_inmueble_corresponda_al_del_momento_9b44ad
    - Excepcion_se_exceptua_el_requisito_de_que_el_valor_del_inmueble_corresponda_al_del_momento_bd353c
    - Excepcion_se_exceptua_la_exigencia_de_conformidad_previa_del_bcra_para_acceso_al_mercado_d_b49855
    - Excepcion_se_exceptua_la_exigencia_de_que_todos_los_bienes_sean_bienes_de_capital_cuando_l_7fbc72
    - Excepcion_se_exceptua_la_prohibicion_de_acceso_al_mercado_de_cambios_para_emisiones_de_val_ec6b21
    - Excepcion_se_exceptua_la_prohibicion_de_acceso_al_mercado_de_cambios_para_la_cancelacion_e_4a4cb0
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_la_asistencia_crediticia_conced_3867e8
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_la_casa_matriz_de_las_sucursale_7c8053
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_las_financiaciones_que_cuenten__9fe9db
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_las_financiaciones_vinculadas_a_6a7a2f
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_las_financiaciones_vinculadas_a_d63b84
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_las_sucursales_y_subsidiarias_d_15cc52
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_los_bancos_u_otras_institucione_808f11
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_los_pases_activos_de_dolares_es_c15c53
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_otros_bancos_del_exterior_autor_9645c8
    - Excepcion_se_excluyen_del_tratamiento_de_ccf_100_para_ventas_de_activos_con_pacto_de_recom_6ad668
    - Excepcion_se_excluyen_los_casos_en_que_las_acciones_judiciales_se_refieren_a_la_discusion__cd1dc1
    - Excepcion_se_permite_el_reconocimiento_de_activos_admisibles_dados_en_garantia_por_entes_d_0dbb18
    - Excepcion_se_permite_emitir_certificaciones_por_la_porcion_no_liquidada_de_operaciones_del_42b5e8
    - Excepcion_se_permite_que_exista_descalce_entre_los_plazos_de_vencimiento_de_la_posicion_su_716bf8
    - Excepcion_se_permite_reconocimiento_parcial_del_derivado_de_credito_cuando_la_reestructura_9395d7
    - Excepcion_se_permite_usar_el_valor_contable_en_lugar_del_valor_de_mercado_para_opciones_so_7432f5
    - Excepcion_se_podra_excluir_del_computo_de_la_exigencia_de_capital_por_riesgo_general_de_me_a4468e
    - Excepcion_se_pueden_excluir_las_posiciones_opuestas_por_el_mismo_importe_en_una_misma_espe_40c628
    - Excepcion_se_pueden_excluir_los_derivados_swaps_forwards_futuros_y_fras_estrechamente_rela_3228ae
    - Excepcion_sera_aplicable_la_excepcion_prevista_en_el_punto_14_1_3_para_clientes_vpu_adheri_44947b
    - Excepcion_si_el_cliente_no_dispone_de_la_documentacion_de_capitalizacion_definitiva_puede__edb3eb
    - Excepcion_si_el_ponderador_resultante_del_tratamiento_de_transparencia_es_menor_que_el_pon_2927b7
    - Excepcion_si_las_entidades_financieras_no_ejercen_la_opcion_de_clasificacion_todas_las_exp_cc5c60
Obligacion: 515 sin aplica_a
    - Obligacion_a_efectos_de_una_verificacion_independiente_de_los_precios_cuando_las_fuentes_de_cef9f1
    - Obligacion_a_fin_de_determinar_el_importe_de_la_cancelacion_se_admite_computar_el_50_de_las_144069
    - Obligacion_a_fin_de_determinar_el_importe_de_la_cancelacion_se_admitira_computar_el_50_de_l_ffcc75
    - Obligacion_a_la_parte_no_cubierta_se_le_aplicara_el_ponderador_de_riesgo_que_le_corresponda_c95e87
    - Obligacion_a_los_conceptos_citados_en_los_puntos_precedentes_se_les_restaran_de_corresponde_5c1d6c
    - Obligacion_a_los_efectos_de_determinar_el_costo_de_reposicion_el_aforo_de_los_activos_recib_0038d1
    - Obligacion_a_los_efectos_del_registro_de_estas_operaciones_se_deberan_confeccionar_dos_bole_a5c0e6
    - Obligacion_a_los_fines_del_calculo_de_la_exigencia_por_riesgo_de_mercado_se_reemplazaran_la_a4b239
    - Obligacion_a_partir_del_comienzo_de_cada_uno_de_los_ultimos_cinco_anos_de_vida_de_cada_emis_023f40
    - Obligacion_acreditar_con_copia_del_escrito_de_iniciacion_de_demanda_certificada_por_el_juzg_f4ddce
    - Obligacion_acreditar_el_cumplimiento_de_los_restantes_requisitos_generales_y_especificos_qu_3b0c25
    - Obligacion_acreditar_la_existencia_de_restricciones_cambiarias_mediante_copia_con_legalizac_bed99c
    - Obligacion_al_importe_que_surja_de_las_expresiones_de_calculo_de_exposicion_ajustada_se_le__3e1be4
    - Obligacion_al_momento_de_inclusion_del_activo_en_la_cartera_de_subyacentes_debe_haberse_reg_f8c0b1
    - Obligacion_aplicacion_de_exigencias_de_capital_por_riesgo_especifico_y_riesgo_general_de_me_fd05c7
    - Obligacion_aplicar_a_los_derivados_convertidos_las_exigencias_de_capital_por_riesgo_especif_0472f0
    - Obligacion_aplicar_los_criterios_especificados_anteriormente_considerando_la_apertura_conce_c6cf85
    - Obligacion_asignar_un_numero_de_identificacion_numero_apx_que_permita_la_incorporacion_de_l_f6893a
    - Obligacion_cada_termino_dentro_de_los_3_componentes_ildc_sc_fc_y_el_resultado_monetario_rm__9cbead
    - Obligacion_calcular_el_efecto_gamma_para_cada_opcion_segun_la_formula_efecto_gamma_1_2_gamm_1bb688
    - Obligacion_calcular_el_excedente_de_pnb_atribuible_a_los_inversores_minoritarios_multiplica_983454
    - Obligacion_calcular_el_excedente_de_pnb_de_la_subsidiaria_como_el_pnb_de_la_subsidiaria_net_454be4
    - Obligacion_calcular_el_importe_de_pnb_reconocible_en_la_entidad_financiera_como_el_importe__3ec9fe
    - Obligacion_calcular_k_ccp_df_pref_cm_y_df_ccp_de_forma_tal_que_la_autoridad_de_control_de_l_b61ac1
    - Obligacion_calcular_la_exigencia_de_capital_total_por_riesgo_gamma_como_la_suma_del_valor_a_baae44
    - Obligacion_calcular_la_exigencia_total_de_capital_por_riesgo_vega_como_la_suma_del_valor_ab_5a4d54
    - Obligacion_contar_con_certificacion_de_aplicacion_emitida_por_la_entidad_encargada_del_segu_97b78f
    - Obligacion_contar_con_la_correspondiente_certificacion_de_la_entidad_encargada_del_seguimie_2fc16f
    - Obligacion_costo_de_reposicion_total_de_contratos_relevantes_puede_calcularse_como_costo_de_de6414
    - Obligacion_cualquier_valor_excedente_de_las_acciones_que_componen_la_canasta_por_encima_del_db6ba3
    - Obligacion_cuando_a_una_exposicion_determinada_pudiera_aplicarse_mas_de_un_ponderador_debe__9b4ded
    - Obligacion_cuando_cliente_no_cumple_requisitos_de_proteccion_exposicion_con_miembro_compens_c9249a
    - Obligacion_cuando_corresponda_identificar_las_monedas_residuales_conforme_a_los_puntos_6_2__16ccbb
    - Obligacion_cuando_el_legajo_se_lleve_en_medios_electronicos_u_otra_tecnologia_similar_deber_b3d9a6
    - Obligacion_cuando_el_riesgo_subyacente_de_exposiciones_en_derivados_o_fuera_de_balance_este_036abc
    - Obligacion_cuando_el_usuario_obtiene_un_seguro_mas_economico_directamente_de_una_asegurador_e259c8
    - Obligacion_cuando_la_exclusion_se_aprueba_durante_un_periodo_intermedio_de_calculo_sera_com_1bbc19
    - Obligacion_cuando_la_liquidacion_de_la_proteccion_crediticia_requiera_transferencia_de_la_o_c86947
    - Obligacion_cuando_la_notificacion_sea_por_via_electronica_debe_ser_clara_de_facil_acceso_pa_89e4c0
    - Obligacion_cuando_la_operacion_ha_sido_liquidada_por_mas_de_una_entidad_cada_una_puede_cert_cc744f
    - Obligacion_cuando_las_exposiciones_cubiertas_tienen_vencimientos_diferentes_se_usara_el_pla_3c3e0d
    - Obligacion_cuando_las_financiaciones_cuenten_con_garantias_preferidas_b_la_entidad_podra_re_f8792e
    - Obligacion_cuando_las_garantias_intercambiadas_no_sean_suficientes_para_cubrir_la_epf_se_de_210669
    - Obligacion_cuando_los_activos_sean_adquiridos_a_terceros_el_originante_fiduciario_debe_revi_c84274
    - Obligacion_cuando_los_aportes_a_un_fondo_de_garantia_se_segregan_por_tipo_de_producto_la_ex_b772a4
    - Obligacion_cuando_los_aportes_al_fondo_de_garantia_para_incumplimientos_df_de_un_miembro_no_abdf5b
    - Obligacion_cuando_los_estandares_de_originacion_se_vean_afectados_por_cambios_el_originante_2b9521
    - Obligacion_cuando_no_se_conoce_el_costo_de_reposicion_debe_utilizarse_el_valor_nocional_com_373ddb
    - Obligacion_cuando_no_se_conoce_el_factor_para_determinar_la_exposicion_potencial_futura_deb_becc54
    - Obligacion_cuando_no_se_conoce_ni_el_costo_de_reposicion_ni_el_factor_de_exposicion_potenci_241e00
    - Obligacion_cuando_no_se_dispone_de_informacion_sobre_el_riesgo_subyacente_de_exposiciones_e_b32fa4
    - Obligacion_cuando_se_adopten_metodos_especificos_de_evaluacion_para_el_otorgamiento_de_asis_0ff591
    - Obligacion_cuando_se_incorporan_activos_durante_el_mes_se_debe_tomar_solamente_la_variacion_187aaa
    - Obligacion_cuando_se_sustituyen_posiciones_no_significativas_por_limites_internos_estos_lim_03095d
    - Obligacion_cuando_se_verifiquen_atrasos_mayores_a_31_dias_en_el_pago_de_los_servicios_de_la_37c7cd
    - Obligacion_cuando_sea_necesario_se_deberan_hacer_ajustes_a_la_valuacion_observando_de_corre_d14052
    - Obligacion_cuando_tampoco_se_conocen_los_nocionales_de_las_posiciones_en_derivados_debe_emp_1c66ed
    - Obligacion_cuando_un_tramo_de_maxima_preferencia_es_estratificado_en_tramos_o_cubierto_parc_e4e9b0
    - Obligacion_cuando_una_subcuenta_contiene_tanto_derivados_como_sft_la_ead_de_esa_subcuenta_s_f26403
    - Obligacion_cuantificar_la_exposicion_en_cada_moneda_como_parte_del_calculo_de_la_exigencia__b457a2
    - Obligacion_de_corresponder_la_consolidacion_mensual_codigo_2_para_datos_complementarios_vin_c40d71
    - Obligacion_de_corresponder_se_incluiran_en_la_partida_20600000_los_quebrantos_no_contabiliz_54b9d9
    - Obligacion_de_las_dos_calificaciones_seleccionadas_las_de_menores_ponderadores_debe_aplicar_fd994e
    - Obligacion_de_reunir_los_requisitos_citados_se_consignara_en_la_partida_60500000_la_porcion_117d13
    - Obligacion_debe_contarse_con_dictamen_juridico_competente_que_confirme_la_exigibilidad_del__e17a80
    - Obligacion_debe_contarse_con_informacion_verificable_sobre_perdidas_e_incumplimientos_de_ac_a7aa83
    - Obligacion_debe_contarse_con_suficiente_informacion_a_nivel_de_cada_prestamo_o_para_cartera_8bd075
    - Obligacion_debe_contarse_con_una_declaracion_jurada_del_cliente_en_la_que_conste_que_tiene__7d2b70
    - Obligacion_debe_identificarse_claramente_a_las_partes_responsables_de_determinar_si_ocurrio_7f5cf7
    - Obligacion_debe_informarse_toda_condicion_o_evento_que_pueda_retrasar_o_impedir_la_transfer_e686a5
    - Obligacion_debe_realizarse_cesion_efectiva_de_derechos_para_cumplir_con_transferencia_real__b9310b
    - Obligacion_debe_suministrarse_al_menos_trimestralmente_durante_la_vida_de_la_titulizacion_d_9e5bd1
    - Obligacion_deben_permanecer_en_esta_categoria_minimo_180_dias_desde_la_fecha_mas_reciente_e_693b31
    - Obligacion_deben_reclasificarse_en_categoria_con_alto_riesgo_de_insolvencia_si_no_cancelan__b82d71
    - Obligacion_deber_de_absorber_previo_a_la_deduccion_de_la_diferencia_positiva_el_importe_de__199b3e
    - Obligacion_deber_de_computar_la_exposicion_al_riesgo_de_tasa_de_interes_o_de_tipo_de_cambio_7a7097
    - Obligacion_deber_de_considerar_en_la_evaluacion_de_la_capacidad_de_pago_la_posibilidad_de_q_2b0997
    - Obligacion_deber_de_consignar_el_nombre_y_apellido_completo_del_no_residente_tal_cual_const_35adf0
    - Obligacion_deber_de_consignar_el_pais_emisor_del_instrumento_de_identificacion__ext_5_7_3_1_525d30
    - Obligacion_deber_de_elaborar_boletos_diferenciados_con_las_formalidades_habituales_por_cada_f15722
    - Obligacion_deber_de_garantizar_que_usuarios_con_dificultad_visual_tengan_acceso_a_plataform_9e4d1f
    - Obligacion_deber_de_identificar_el_numero_de_la_oficializacion_del_despacho_de_importacion__b1165e
    - Obligacion_deber_de_incluir_un_anexo_con_la_firma_del_cliente_en_el_cual_conste_el_listado__790701
    - Obligacion_deber_de_ofrecer_a_usuarios_con_dificultades_visuales_la_opcion_de_obtener_en_si_252aec
    - Obligacion_debera_cumplirse_con_lo_establecido_en_el_texto_ordenado_sobre_politica_de_credi_c2b9be
    - Obligacion_debera_someterse_el_modelo_a_examenes_periodicos_a_fin_de_determinar_la_fiabilid_1a61e1
    - Obligacion_debera_tenerse_en_cuenta_lo_dispuesto_en_el_punto_3_1_para_el_tratamiento_de_pos_77f0e6
    - Obligacion_debera_tenerse_en_cuenta_lo_dispuesto_en_el_punto_4_2_para_las_operaciones_con_d_4023cf
    - Obligacion_deberan_existir_contragarantias_extendidas_por_la_casa_matriz_o_sus_sucursales_e_754e67
    - Obligacion_deberan_proporcionarse_en_terminos_claros_y_consistentes_las_politicas_y_procedi_591fb8
    - Obligacion_deberan_proveer_informacion_que_permita_realizar_un_seguimiento_de_la_evolucion__db8ce4
    - Obligacion_dejar_constancia_de_la_identificacion_del_acreedor_o_de_quien_realiza_el_aporte__d4889a
    - Obligacion_dejar_constancia_en_el_boleto_de_venta_de_que_el_pago_diferido_de_importaciones__8f6cd5
    - Obligacion_dejar_constancia_en_el_boleto_de_venta_que_el_pago_se_concreta_por_el_presente_m_f62690
    - Obligacion_demostrar_el_registro_de_ingreso_aduanero_de_los_bienes_dentro_de_los_plazos_nor_31d73f
    - Obligacion_determinacion_diaria_de_integracion_de_capital__cap_6_7_1_faca13
    - Obligacion_determinar_la_exigencia_por_cada_moneda_identificando_la_partida_segun_su_moneda_9154b7
    - Obligacion_el_acceso_al_mercado_local_de_cambios_para_cancelar_anticipos_u_otras_financiaci_27a670
    - Obligacion_el_activo_recibido_en_garantia_debe_contar_con_una_valuacion_a_precios_de_mercad_399b66
    - Obligacion_el_aforo_por_descalce_de_monedas_debera_incrementarse_proporcionalmente_utilizan_38827e
    - Obligacion_el_alcance_y_adecuacion_de_la_cobertura_deberan_ser_explicados_y_divulgados_a_lo_d9cf00
    - Obligacion_el_analisis_de_capacidad_de_repago_debera_tener_en_cuenta_la_liquidez_del_interm_fe5302
    - Obligacion_el_analisis_del_flujo_de_fondos_del_cliente_demuestra_que_es_capaz_de_atender_ad_cc70f3
    - Obligacion_el_bcra_informara_a_las_entidades_el_monto_maximo_de_certificaciones_para_cada_e_edccbf
    - Obligacion_el_boleto_de_compra_debe_confeccionarse_por_un_codigo_de_concepto_que_identifiqu_7361d9
    - Obligacion_el_boleto_de_venta_debe_confeccionarse_por_el_monto_correspondiente_con_el_codig_0e168b
    - Obligacion_el_calculo_de_k_ccp_debe_hacerse_como_minimo_con_periodicidad_trimestral__cap_4__ff927f
    - Obligacion_el_calculo_del_promedio_de_erc_incluye_unicamente_las_exigencias_hasta_la_que_co_b6a7c1
    - Obligacion_el_cliente_debe_presentar_la_documentacion_que_avale_la_capitalizacion_definitiv_76a18d
    - Obligacion_el_cliente_debe_presentar_la_documentacion_que_avale_la_capitalizacion_definitiv_79ea37
    - Obligacion_el_cliente_debera_comprometerse_a_presentar_la_correspondiente_certificacion_por_fcc9fb
    - Obligacion_el_cliente_debera_firmar_una_declaracion_jurada_comprometiendose_a_ingresar_y_li_7db932
    - Obligacion_el_cliente_debera_presentar_una_declaracion_jurada_dejando_constancia_de_que_los_cf7b67
    - Obligacion_el_cliente_que_acceda_al_mercado_de_cambios_debera_nominar_a_una_entidad_para_qu_c1adc3
    - Obligacion_el_cliente_se_compromete_a_no_adquirir_certificados_de_depositos_argentinos_repr_85f0d8
    - Obligacion_el_cliente_se_compromete_a_no_adquirir_en_el_pais_titulos_valores_emitidos_por_n_a156f5
    - Obligacion_el_cliente_se_compromete_a_no_adquirir_titulos_valores_representativos_de_deuda__6fb336
    - Obligacion_el_cliente_se_compromete_a_no_concertar_ventas_en_el_pais_de_titulos_valores_con_8e88f6
    - Obligacion_el_cliente_se_compromete_a_no_entregar_fondos_en_moneda_local_ni_otros_activos_l_30d2f5
    - Obligacion_el_cliente_se_compromete_a_no_realizar_canjes_de_titulos_valores_emitidos_por_re_675089
    - Obligacion_el_cliente_se_compromete_a_no_realizar_transferencias_de_titulos_valores_a_entid_73745e
    - Obligacion_el_computo_de_los_plazos_de_atrasos_no_se_interrumpira_por_el_otorgamiento_de_re_6a48c7
    - Obligacion_el_computo_del_monto_maximo_de_certificaciones_se_hara_en_base_a_una_distribucio_6a108a
    - Obligacion_el_contrato_de_cesion_debe_contener_clausulas_por_las_cuales_el_originante_garan_80c684
    - Obligacion_el_contrato_de_fideicomiso_debera_incluir_el_modo_de_sustitucion_del_fiduciario__f2e648
    - Obligacion_el_contrato_de_proteccion_crediticia_debe_representar_un_derecho_crediticio_dire_98a949
    - Obligacion_el_contrato_de_proteccion_debe_ser_incondicional_sin_clausulas_que_escapen_al_co_1e4a6b
    - Obligacion_el_contravalor_de_la_exportacion_de_bienes_y_servicios_debera_ingresarse_al_pais_8ae3ba
    - Obligacion_el_deudor_clasificado_en_esta_categoria_que_haya_refinanciado_su_deuda_y_recibid_56ca69
    - Obligacion_el_deudor_clasificado_en_riesgo_alto_que_haya_refinanciado_su_deuda_y_recibido_c_dc867b
    - Obligacion_el_documento_a_cobrar_o_derecho_de_credito_transferido_no_debe_ser_objeto_de_lit_2afab6
    - Obligacion_el_ejercicio_de_la_opcion_de_exclusion_que_ha_servido_de_mejora_crediticia_se_co_275203
    - Obligacion_el_estado_financiero_debe_estar_acompanado_de_un_informe_especial_del_auditor_ex_756d2d
    - Obligacion_el_estado_financiero_debe_haber_sido_previamente_presentado_ante_el_bcra__cap_8__b8ba65
    - Obligacion_el_estado_financiero_debera_contar_con_la_intervencion_del_auditor_externo_previ_838596
    - Obligacion_el_excedente_de_rpc_atribuible_a_los_inversores_minoritarios_resultara_de_multip_7e7c94
    - Obligacion_el_excedente_de_rpc_de_la_subsidiaria_se_calcula_como_la_rpc_de_la_subsidiaria_n_b1b936
    - Obligacion_el_exportador_debe_seleccionar_una_entidad_para_que_realice_el_seguimiento_de_la_d48471
    - Obligacion_el_exportador_debera_presentar_ante_la_entidad_encargada_del_seguimiento_del_per_0881a9
    - Obligacion_el_fiduciario_o_administrador_debera_en_todo_momento_actuar_en_forma_razonable_p_900c6b
    - Obligacion_el_importador_debe_demostrar_que_a_la_fecha_de_origen_de_la_financiacion_contaba_be18a1
    - Obligacion_el_importador_debe_nominar_una_entidad_para_cada_oficializacion_del_despacho_de__fa601b
    - Obligacion_el_importador_debera_informar_a_la_entidad_de_seguimiento_sobre_los_pagos_en_el__e63787
    - Obligacion_el_importe_que_se_reconocera_en_la_rpc_de_la_entidad_financiera_sera_el_importe__186513
    - Obligacion_el_ingreso_y_liquidacion_de_las_divisas_por_el_mercado_de_cambios_debera_concret_7605cc
    - Obligacion_el_inversor_debe_realizar_sus_propias_evaluaciones_respecto_del_cumplimiento_de__91f449
    - Obligacion_el_legajo_de_corresponsales_debe_contener_informacion_sobre_identificacion_calif_7067c1
    - Obligacion_el_legajo_debe_incluir_informacion_sobre_margenes_crediticios_discriminados_por__3c7a6e
    - Obligacion_el_margen_inicial_aportado_por_clientes_al_miembro_compensador_mitiga_su_exposic_aba080
    - Obligacion_el_mecanismo_de_asignacion_de_perdidas_debe_reducir_el_importe_a_reintegrar_en_c_0c9bc6
    - Obligacion_el_mecanismo_de_asignacion_de_perdidas_debe_reducir_la_deuda_representada_por_el_afca5a
    - Obligacion_el_mecanismo_de_asignacion_de_perdidas_debe_reducir_total_o_parcialmente_los_pag_1bd099
    - Obligacion_el_monto_utilizado_bajo_esta_modalidad_debe_computarse_a_los_efectos_de_los_limi_78f795
    - Obligacion_el_numero_apx_quedara_a_cargo_de_la_propia_entidad_financiera__ext_14_5_7_bba138
    - Obligacion_el_obligado_al_pago_no_debe_contar_con_evaluacion_de_agencia_de_calificacion_de__5623c3
    - Obligacion_el_obligado_al_pago_no_debe_contar_con_historial_de_credito_desfavorable_en_algu_061ede
    - Obligacion_el_obligado_al_pago_no_debe_haber_sido_sometido_a_proceso_de_quiebra_o_reestruct_7b0c81
    - Obligacion_el_orden_de_prelacion_en_el_pago_de_todos_los_compromisos_debera_estar_clarament_6c4bfd
    - Obligacion_el_originante_de_la_titulizacion_y_el_acreedor_inicial_de_los_creditos_titulizad_a6f28d
    - Obligacion_el_originante_debe_demostrar_al_inversor_que_los_activos_transferidos_fueron_gen_16b4ae
    - Obligacion_el_originante_fiduciario_debe_divulgar_toda_la_informacion_necesaria_respecto_de_640a80
    - Obligacion_el_originante_o_fiduciario_debera_poner_a_disposicion_de_los_inversores_tanto_an_7f1655
    - Obligacion_el_pago_de_dividendos_o_cupones_debera_efectuarse_con_cargo_a_partidas_distribui_d2ee9c
    - Obligacion_el_pago_de_los_compromisos_de_una_titulizacion_no_debera_depender_de_la_venta_o__4cc7b3
    - Obligacion_el_pago_garantizado_debia_ser_concretado_por_el_cliente_a_partir_de_la_fecha_que_2293ed
    - Obligacion_el_pago_garantizado_debia_ser_concretado_por_el_cliente_a_partir_de_la_fecha_que_2b0d14
    - Obligacion_el_pais_debe_identificarse_de_acuerdo_con_la_codificacion_del_country_codes_del__b7bd9c
    - Obligacion_el_periodo_minimo_de_mantenimiento_se_extiende_si_las_operaciones_o_activos_reci_263558
    - Obligacion_el_plazo_de_ingreso_y_liquidacion_de_divisas_se_contara_a_partir_de_la_fecha_de__9aafec
    - Obligacion_el_ponderador_de_riesgo_de_la_contraparte_debe_aplicarse_a_la_suma_del_costo_de__f35620
    - Obligacion_el_ponderador_de_riesgo_de_la_contraparte_debe_sustituirse_por_el_ponderador_de__058451
    - Obligacion_el_que_origine_o_activamente_promocione_una_titulizacion_debera_retener_una_expo_c65c3d
    - Obligacion_el_ratio_de_apalancamiento_mantendra_su_frecuencia_trimestral_datos_del_mes_de_c_d61b1e
    - Obligacion_el_reembolso_a_los_inversores_debe_provenir_principalmente_del_producido_de_los__becdfb
    - Obligacion_el_requisito_de_ingreso_y_liquidacion_de_divisas_en_el_mercado_de_cambios_se_con_a39367
    - Obligacion_el_resto_del_capital_que_vencia_debe_ser_refinanciado_como_minimo_con_un_nuevo_e_6d09b0
    - Obligacion_el_resto_del_valor_facturado_segun_la_condicion_de_venta_pactada_debe_cumpliment_082508
    - Obligacion_el_riesgo_de_tasa_de_interes_del_derivado_se_computara_conforme_a_lo_indicado_en_dc4358
    - Obligacion_el_saldo_de_deuda_pendiente_debe_computarse_sin_deducir_previsiones_por_riesgo_d_dbffe5
    - Obligacion_el_sujeto_obligado_debe_conservar_constancia_de_haber_permitido_el_ejercicio_del_0e550e
    - Obligacion_el_tratamiento_de_las_garantias_aportadas_por_la_segunda_ccp_a_la_primera_como_m_446e4e
    - Obligacion_el_valor_de_k_debe_computarse_sobre_la_cartera_subyacente_de_la_operacion_origin_38b7cf
    - Obligacion_el_valor_de_la_cobertura_debe_ajustarse_conforme_a_las_disposiciones_del_punto_5_c5e703
    - Obligacion_el_valor_del_inmueble_debe_corresponder_al_del_momento_del_otorgamiento_del_cred_b08572
    - Obligacion_el_valor_del_inmueble_debe_ser_resultado_de_una_tasacion_que_se_ajuste_a_una_val_14bec1
    - Obligacion_el_valor_del_inmueble_debe_ser_resultado_de_una_tasacion_que_se_realice_en_forma_510a9a
    - Obligacion_el_vpu_debe_comprometerse_a_presentar_la_documentacion_de_la_capitalizacion_defi_de4be6
    - Obligacion_en_caso_de_no_disponer_de_la_documentacion_de_capitalizacion_definitiva_el_vpu_d_2c4bac
    - Obligacion_en_caso_de_que_el_vpu_contemple_la_posibilidad_de_aplicar_cobros_de_exportacione_7830ac
    - Obligacion_en_caso_de_venta_de_activos_debe_tenerse_en_cuenta_la_perdida_o_ganancia_resulta_db5e32
    - Obligacion_en_el_analisis_de_capacidad_de_repago_se_debera_poner_enfasis_en_la_medicion_del_818354
    - Obligacion_en_el_analisis_debe_tenerse_en_cuenta_de_corresponder_la_eventual_incidencia_que_bde00d
    - Obligacion_en_el_caso_de_financiaciones_propias_del_proveedor_o_aquellas_que_impliquen_pago_86368b
    - Obligacion_en_el_caso_de_pagos_concretados_a_partir_de_financiaciones_de_entidades_financie_c95c0f
    - Obligacion_en_la_aplicacion_del_metodo_integral_el_importe_del_activo_debe_ajustarse_median_6e52a3
    - Obligacion_en_la_clausula_de_revocacion_debe_aclararse_que_la_revocacion_sera_sin_costo_ni__23bcb4
    - Obligacion_en_la_declaracion_jurada_del_cliente_debera_constar_expresamente_el_valor_de_sus_cbe3b4
    - Obligacion_en_la_documentacion_de_la_operacion_debe_constar_la_identificacion_de_la_factura_39a0e2
    - Obligacion_en_las_declaraciones_juradas_no_deberan_considerarse_la_entrega_de_activos_local_89789a
    - Obligacion_en_las_declaraciones_juradas_no_deberan_considerarse_las_ventas_con_liquidacion__02a39c
    - Obligacion_en_las_declaraciones_juradas_no_deberan_considerarse_las_ventas_con_liquidacion__29ca23
    - Obligacion_en_las_declaraciones_juradas_no_deberan_considerarse_las_ventas_de_titulos_valor_a40845
    - Obligacion_en_las_declaraciones_juradas_para_cumplimiento_de_puntos_3_16_3_1_y_3_16_3_2_no__4742c8
    - Obligacion_en_los_casos_de_devoluciones_de_pagos_anticipados_de_importaciones_de_bienes_se__ad708d
    - Obligacion_en_los_casos_enunciados_en_los_acapites_i_a_iii_se_debera_tomar_la_mayor_de_las__490ca6
    - Obligacion_en_los_restantes_casos_el_seguimiento_quedara_inicialmente_a_cargo_de_la_entidad_6bfd8e
    - Obligacion_en_retitulizaciones_con_cartera_subyacente_mixta_tramos_de_titulizacion_y_otros__72f913
    - Obligacion_en_todos_los_casos_la_operacion_debera_estar_incorporada_al_seguimiento_de_antic_0abbdb
    - Obligacion_entidades_con_codigo_3_deberan_incluir_los_datos_previstos_para_los_codigos_0_1__91c102
    - Obligacion_entidades_con_codigo_3_deberan_presentar_informacion_con_frecuencia_trimestral_i_405c16
    - Obligacion_entidades_con_codigo_9_deberan_incluir_en_la_declaracion_en_los_casos_que_corres_0b4a23
    - Obligacion_entidades_con_codigo_9_deberan_incluir_en_la_declaracion_en_los_casos_que_corres_1047aa
    - Obligacion_entidades_con_codigo_9_deberan_incluir_en_la_declaracion_en_los_casos_que_corres_51987b
    - Obligacion_entidades_con_codigo_9_deberan_incluir_en_la_declaracion_en_los_casos_que_corres_a037f6
    - Obligacion_entidades_con_codigo_9_deberan_presentar_declaracion_conteniendo_calculo_del_rie_1bbcdf
    - Obligacion_entidades_con_codigo_9_deberan_presentar_declaracion_conteniendo_exigencia_por_r_21c30b
    - Obligacion_entidades_con_codigo_9_deberan_presentar_declaracion_conteniendo_exigencia_por_r_379d3e
    - Obligacion_entidades_con_codigo_9_deberan_presentar_declaracion_conteniendo_exigencia_por_r_d1668e
    - Obligacion_entidades_con_codigo_9_deberan_presentar_declaracion_conteniendo_responsabilidad_75f3e2
    - Obligacion_estimar_los_riesgos_inherentes_a_la_combinacion_de_posiciones_compradas_y_vendid_9ddcc6
    - Obligacion_extension_del_plazo_hasta_120_ciento_veinte_dias_corridos_cuando_el_exportador_h_35d31e
    - Obligacion_extension_del_plazo_hasta_el_previsto_en_el_punto_7_1_1_4_cuando_el_exportador_n_2b2d30
    - Obligacion_garantia_depositada_sin_proteccion_en_caso_de_quiebra_debe_considerarse_para_mon_408d31
    - Obligacion_identicas_condiciones_deben_cumplirse_para_tratamiento_de_exposicion_de_cliente__487289
    - Obligacion_identico_criterio_de_excepcion_al_plazo_minimo_se_aplicara_para_determinacion_de_0dabad
    - Obligacion_identico_tratamiento_de_garantia_se_aplica_a_estructuras_multinivel_de_clientes__47e43d
    - Obligacion_incluir_en_las_transferencias_de_fondos_con_el_exterior_y_en_sus_respectivos_men_026bda
    - Obligacion_informacion_de_los_saldos_a_fin_del_ultimo_mes_del_trimestre_en_la_banda_0_cero__c690bc
    - Obligacion_informar_cambios_negativos_en_clasificacion_a_deudores_en_situaciones_3_4_o_5_y__2a912f
    - Obligacion_ingreso_y_liquidacion_de_anticipos_prefinanciaciones_y_posfinanciaciones_del_ext_7c32db
    - Obligacion_k_a_para_la_exposicion_a_una_retitulizacion_es_el_promedio_ponderado_por_la_expo_9c7551
    - Obligacion_la_aplicacion_de_cobros_de_exportaciones_y_servicios_estara_habilitada_para_el_p_3894fc
    - Obligacion_la_aplicacion_de_cobros_de_exportaciones_y_servicios_estara_habilitada_para_el_p_39a9e5
    - Obligacion_la_aplicacion_de_cobros_de_exportaciones_y_servicios_estara_habilitada_para_el_p_b2a2df
    - Obligacion_la_aplicacion_de_cobros_de_exportaciones_y_servicios_estara_habilitada_para_el_p_fd5493
    - Obligacion_la_aplicacion_de_cobros_de_exportaciones_y_servicios_estara_habilitada_para_pago_9b3606
    - Obligacion_la_aplicacion_de_cobros_de_exportaciones_y_servicios_estara_habilitada_para_repa_c7b013
    - Obligacion_la_aplicacion_de_la_tecnica_de_cobertura_mediante_garantias_personales_estara_su_fe1644
    - Obligacion_la_cartera_inicial_debe_ser_revisada_por_un_contador_publico_independiente_para__23ff95
    - Obligacion_la_certificacion_de_aplicacion_debe_contener_como_minimo_cuit_y_denominacion_del_eb267e
    - Obligacion_la_conformidad_debe_estar_referida_con_opinion_fundada_en_todos_los_casos_tanto__cc565e
    - Obligacion_la_declaracion_jurada_debe_estar_firmada_por_el_cliente_su_representante_legal_o_c66330
    - Obligacion_la_declaracion_jurada_debe_estar_firmada_por_el_representante_legal_de_la_empres_4133a2
    - Obligacion_la_deduccion_del_capital_ordinario_de_nivel_uno_sera_equivalente_al_100_del_valo_64a0b5
    - Obligacion_la_deduccion_se_efectuara_por_el_importe_del_mayor_saldo_registrado_durante_el_m_4db618
    - Obligacion_la_documentacion_de_la_titulizacion_debe_incluir_opinion_legal_independiente_que_fac7dd
    - Obligacion_la_documentacion_debera_estar_legalizada_por_autoridad_consular_o_conforme_a_lo__3e5321
    - Obligacion_la_documentacion_debera_estar_legalizada_por_autoridad_consular_o_conforme_a_lo__8c86e4
    - Obligacion_la_documentacion_final_de_la_oferta_o_el_prospecto_debera_estar_disponible_desde_a75e97
    - Obligacion_la_documentacion_provisional_inicial_oferta_o_prospecto_provisional_y_de_apoyo_d_664ae7
    - Obligacion_la_documentacion_que_permite_determinar_la_existencia_de_una_compra_de_bienes_al_8557f4
    - Obligacion_la_documentacion_utilizada_para_certificar_el_concepto_y_monto_de_las_divisas_im_163b25
    - Obligacion_la_documentacion_vinculada_con_la_cobertura_del_riesgo_de_credito_debe_observar__3d5f55
    - Obligacion_la_ead_reducida_debe_utilizarse_tambien_para_calculo_del_ajuste_de_valuacion_de__8984fd
    - Obligacion_la_entidad_debe_contar_con_certificacion_de_la_entidad_encargada_del_seguimiento_7bfe40
    - Obligacion_la_entidad_debe_contar_con_una_certificacion_para_el_acceso_al_mercado_de_cambio_091dae
    - Obligacion_la_entidad_debe_contar_con_una_declaracion_jurada_del_cliente_en_la_que_conste_q_6972f1
    - Obligacion_la_entidad_debera_acreditar_el_cumplimiento_de_los_restantes_requisitos_generale_e4535b
    - Obligacion_la_entidad_debera_contar_con_una_certificacion_de_la_entidad_encargada_del_segui_8dee2e
    - Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_importador__0a2aa9
    - Obligacion_la_entidad_es_originalmente_nominada_por_el_importador_ante_la_arca__ext_11_1_7b7329
    - Obligacion_la_entidad_financiera_debe_concertar_acuerdo_dentro_de_90_dias_si_acuerdos_con_h_d6ff19
    - Obligacion_la_entidad_financiera_debe_concretar_el_registro_de_la_financiacion_ante_el_bcra_894b59
    - Obligacion_la_entidad_financiera_debe_contar_con_la_correspondiente_certificacion_de_la_ent_786b70
    - Obligacion_la_entidad_financiera_local_designada_debera_efectuar_el_seguimiento_de_las_gara_2e2ec0
    - Obligacion_la_entidad_interviniente_debe_contar_con_una_certificacion_de_la_entidad_encarga_c42c98
    - Obligacion_la_entidad_interviniente_debe_contar_con_una_certificacion_emitida_por_la_entida_0e7bbe
    - Obligacion_la_entidad_nominada_es_responsable_de_verificar_el_cumplimiento_de_las_condicion_a5915e
    - Obligacion_la_entidad_nominada_por_el_importador_para_realizar_el_seguimiento_de_las_oficia_08e768
    - Obligacion_la_exigencia_de_capital_por_cva_correspondiente_a_la_totalidad_de_contrapartes_s_98f6b8
    - Obligacion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_se_determinara_ten_b9cec2
    - Obligacion_la_exigencia_se_obtendra_como_la_suma_de_dos_exigencias_calculadas_por_separado__b9e7d4
    - Obligacion_la_exposicion_al_riesgo_de_credito_de_contraparte_del_fondo_debe_calcularse_de_a_4e8dce
    - Obligacion_la_financiacion_en_moneda_extranjera_por_importaciones_de_servicios_otorgada_por_837470
    - Obligacion_la_financiacion_especializada_de_grandes_proyectos_de_infraestructura_debera_ten_1b27fc
    - Obligacion_la_financiacion_especializada_de_grandes_proyectos_de_infraestructura_debera_ten_cf0bf4
    - Obligacion_la_financiacion_especializada_de_grandes_proyectos_de_infraestructura_debera_ten_e81833
    - Obligacion_la_informacion_debera_incluir_el_porcentaje_de_financiaciones_vencidas_con_detal_2fa2ab
    - Obligacion_la_informacion_debera_incluir_el_porcentaje_de_la_deuda_inicial_subyacente_cance_491b03
    - Obligacion_la_informacion_debera_incluir_el_ratio_promedio_de_monto_desembolsado_sobre_el_v_18b8a6
    - Obligacion_la_informacion_debera_incluir_el_tipo_de_exposicion_en_la_medida_en_que_resulte__ccabfb
    - Obligacion_la_informacion_debera_incluir_el_tipo_de_propiedad_tal_como_vivienda_o_inmueble__9ff2bb
    - Obligacion_la_informacion_debera_incluir_la_clasificacion_promedio_de_los_deudores_conforme_42c267
    - Obligacion_la_informacion_debera_incluir_la_diversificacion_geografica_y_sectorial_en_la_me_522cc5
    - Obligacion_la_informacion_debera_incluir_la_porcion_del_monto_nocional_cubierto_asi_como_un_544775
    - Obligacion_la_informacion_debera_incluir_la_tasa_de_ocupacion_de_los_inmuebles_en_la_medida_c9112d
    - Obligacion_la_informacion_debera_incluir_las_financiaciones_en_gestion_judicial_en_la_medid_9efd50
    - Obligacion_la_informacion_debera_incluir_las_tasas_de_incumplimiento_en_la_medida_en_que_re_c24a22
    - Obligacion_la_informacion_necesaria_para_calcular_las_siguientes_variables_sera_provista_o__36e741
    - Obligacion_la_informacion_que_surja_del_legajo_unico_financiero_y_economico_sera_considerad_da3dae
    - Obligacion_la_informacion_sobre_composicion_de_exposiciones_de_ccp_y_datos_para_calculo_de__724ce3
    - Obligacion_la_liquidacion_de_los_fondos_por_parte_del_emisor_queda_sujeta_a_las_normas_apli_5ef6c5
    - Obligacion_la_metodologia_de_evaluacion_debe_haber_estado_sujeta_a_comprobacion_rigurosa_de_9fa012
    - Obligacion_la_nueva_entidad_queda_habilitada_para_emitir_nuevas_certificaciones_una_vez_que_d8836e
    - Obligacion_la_operacion_quedara_incorporada_al_correspondiente_seguimiento_previsto_en_el_p_d2d863
    - Obligacion_la_parte_de_la_exposicion_no_cubierta_por_garantia_o_proteccion_crediticia_se_co_00080d
    - Obligacion_la_parte_protegida_de_la_exposicion_recibira_el_tratamiento_aplicable_a_las_gara_8d4894
    - Obligacion_la_presentacion_de_base_consolidada_trimestral_se_regira_por_los_plazos_de_prese_bc0f57
    - Obligacion_la_presentacion_de_base_individual_se_regira_por_los_plazos_de_presentacion_prev_50f0b9
    - Obligacion_la_sefyc_debera_expedirse_sobre_el_descargo_dentro_de_los_30_dias_corridos_sigui_cd9577
    - Obligacion_la_seleccion_de_activos_debe_estar_sujeta_a_criterios_de_elegibilidad_claramente_00df74
    - Obligacion_la_solicitud_de_autorizacion_de_aportes_de_capital_debera_acompanarse_de_copia_d_4333e6
    - Obligacion_la_totalidad_de_los_fondos_suscriptos_en_el_pais_debe_haber_sido_liquidado_en_el_9f4d80
    - Obligacion_la_utilizacion_de_este_mecanismo_debera_resultar_neutral_en_materia_fiscal__ext__0db4ba
    - Obligacion_la_verificacion_de_los_precios_de_mercado_o_de_los_datos_del_modelo_debe_estar_a_c09736
    - Obligacion_la_verificacion_independiente_de_precios_se_debe_llevar_a_cabo_al_menos_con_peri_27a83a
    - Obligacion_las_calificaciones_en_moneda_extranjera_se_utilizaran_para_ponderar_por_riesgo_l_832d14
    - Obligacion_las_calificaciones_en_moneda_nacional_se_utilizaran_solamente_para_ponderar_por__9ee8ea
    - Obligacion_las_coberturas_deberan_estar_disponibles_y_haber_sido_integramente_fondeadas__ca_610b42
    - Obligacion_las_coberturas_del_riesgo_de_credito_deben_cumplir_los_requisitos_establecidos_e_3f726a
    - Obligacion_las_contrapartes_deberan_encuadrarse_en_alguno_de_los_siguientes_grados_de_riesg_870682
    - Obligacion_las_ecai_deberan_utilizar_una_metodologia_rigurosa_sistematica_y_sujeta_a_valida_0c86b4
    - Obligacion_las_entidades_autorizadas_deberan_efectuar_un_seguimiento_de_los_pagos_cursados__53342a
    - Obligacion_las_entidades_deberan_considerar_la_realidad_o_finalidad_economica_de_la_transac_bed37f
    - Obligacion_las_entidades_deberan_contar_con_opinion_legal_escrita_y_fundada_que_concluya_qu_ee3f1e
    - Obligacion_las_entidades_deberan_maximizar_el_uso_de_datos_observables_cuando_sean_relevant_ab6445
    - Obligacion_las_entidades_deberan_obtener_conformidad_previa_del_bcra_para_acceder_al_mercad_ec7e8c
    - Obligacion_las_entidades_deberan_valuar_a_mercado_siempre_que_sea_posible_utilizando_el_val_b4943c
    - Obligacion_las_entidades_obligadas_deben_deducir_ciertos_activos_a_los_fines_del_calculo_de_ef913e
    - Obligacion_las_entidades_tienen_la_facultad_de_excluir_las_posiciones_comprendidas_en_las_p_783f27
    - Obligacion_las_evaluaciones_de_calificaciones_crediticias_deberan_ser_objeto_de_control_con_9bf591
    - Obligacion_las_exposiciones_a_mipyme_que_no_se_ajusten_a_los_criterios_para_las_exposicione_5975fb
    - Obligacion_las_exposiciones_potenciales_futuras_epf_calculadas_a_nivel_de_conjunto_de_neteo_a6bd5a
    - Obligacion_las_exposiciones_registradas_en_el_activo_del_fondo_deben_ponderarse_asumiendo_q_879580
    - Obligacion_las_fuentes_de_informacion_el_acceso_a_los_datos_y_los_fundamentos_que_demuestre_c3b657
    - Obligacion_las_inversiones_en_instrumentos_de_capital_que_no_cumplan_con_los_criterios_para_8cfab9
    - Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe_2f15f6
    - Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_defi_9eb03c
    - Obligacion_las_notificaciones_deben_incluir_la_leyenda_que_remite_al_regimen_de_transparenc_5711db
    - Obligacion_las_notificaciones_deben_incluir_la_leyenda_usted_podra_optar_por_rescindir_el_c_c73ec2
    - Obligacion_las_operaciones_cursadas_deben_ser_incorporadas_al_sepaimpo_a_partir_de_su_repor_766344
    - Obligacion_las_operaciones_de_anticipos_prefinanciaciones_de_exportaciones_y_otras_financia_dbdde5
    - Obligacion_las_operaciones_de_cambio_deben_realizarse_al_tipo_de_cambio_que_sea_libremente__f0a770
    - Obligacion_las_operaciones_deberan_abonarse_por_alguno_de_los_siguientes_mecanismos__ext_4__78d64f
    - Obligacion_las_operaciones_se_regiran_por_lo_dispuesto_en_los_puntos_3_9_y_3_10_segun_corre_a5dc2b
    - Obligacion_las_partes_contratantes_de_derivados_de_credito_deben_especificar_eventos_de_cre_8d9d8c
    - Obligacion_las_politicas_procedimientos_y_controles_de_gestion_de_riesgos_deberan_estar_bie_7f8720
    - Obligacion_las_posiciones_ponderadas_deberan_compensarse_compradas_vendidas_dentro_de_cada__ffba8f
    - Obligacion_las_tasas_de_interes_o_de_descuento_de_referencia_deben_ser_tasas_de_mercado_y_d_db5923
    - Obligacion_las_titulizaciones_con_periodos_rotativos_deberan_establecer_eventos_de_amortiza_01921b
    - Obligacion_los_activos_subyacentes_deben_ser_homogeneos_en_tipo_jurisdiccion_legislacion_ap_486988
    - Obligacion_los_acuerdos_de_compensacion_deben_permitir_la_compensacion_de_perdidas_y_gananc_dd3c0c
    - Obligacion_los_acuerdos_de_compensacion_deben_permitir_la_rapida_liquidacion_o_compensacion_31664c
    - Obligacion_los_acuerdos_de_compensacion_deben_proporcionar_a_la_parte_que_no_se_encuentra_e_912243
    - Obligacion_los_acuerdos_de_compensacion_deben_tener_validez_legal_junto_con_los_derechos_de_54daff
    - Obligacion_los_acuerdos_de_neteo_bilateral_que_alcancen_a_operaciones_de_financiacion_con_t_ea7416
    - Obligacion_los_aforos_a_ser_aplicados_a_las_operaciones_de_financiacion_con_titulos_valores_71d419
    - Obligacion_los_aforos_se_modificaran_utilizando_la_formula_de_la_raiz_cuadrada_del_tiempo_c_5d85a7
    - Obligacion_los_ajustes_al_valor_corriente_de_las_posiciones_menos_liquidas_se_deben_deducir_85cfa2
    - Obligacion_los_calculos_deberan_ser_consistentes_con_la_informacion_reportada_en_los_cuadro_103acc
    - Obligacion_los_caps_o_floors_se_deberan_registrar_como_una_combinacion_de_un_bono_a_interes_63b63a
    - Obligacion_los_conceptos_registrados_en_pfb_deben_convertirse_en_equivalentes_crediticios_m_c3ef21
    - Obligacion_los_contratos_deben_contener_clausula_de_revocacion_que_indique_que_el_usuario_d_1ec6e9
    - Obligacion_los_contratos_deben_contener_el_derecho_de_solicitar_la_apertura_de_la_caja_de_a_6e7316
    - Obligacion_los_contratos_deben_contener_el_derecho_del_usuario_de_efectuar_en_cualquier_mom_3e412e
    - Obligacion_los_contratos_deben_contener_el_derecho_del_usuario_de_realizar_operaciones_por__88daee
    - Obligacion_los_contratos_deben_contener_la_descripcion_y_especificacion_completa_del_produc_0fcad9
    - Obligacion_los_contratos_deben_contener_la_identificacion_del_usuario_de_servicios_financie_2ace2e
    - Obligacion_los_contratos_deben_contener_la_leyenda_usted_puede_consultar_el_regimen_de_tran_cf1b12
    - Obligacion_los_contratos_deben_contener_la_razon_social_cuit_y_domicilio_legal_del_sujeto_o_0e73d5
    - Obligacion_los_contratos_deben_contener_las_comisiones_y_cargos_asi_como_los_terminos_y_con_59f26e
    - Obligacion_los_contratos_deben_contener_los_restantes_requisitos_normativamente_reglamentad_ee041e
    - Obligacion_los_contratos_que_instrumenten_las_operaciones_de_cobertura_deberan_ser_los_usua_7acdaf
    - Obligacion_los_datos_de_mercado_deberan_proceder_en_la_medida_de_lo_posible_de_las_mismas_f_7ff64e
    - Obligacion_los_derechos_del_inversor_deberan_estar_claramente_definidos_en_toda_circunstanc_46c71e
    - Obligacion_los_descalces_de_monedas_deberan_tomarse_en_consideracion_a_los_efectos_de_calcu_a79318
    - Obligacion_los_deudores_excluidos_de_la_categoria_irrecuperable_deberan_ser_clasificados_y__f4bf8f
    - Obligacion_los_documentos_a_cobrar_o_derechos_de_credito_titulizados_deben_satisfacer_crite_93e022
    - Obligacion_los_fiduciarios_y_administradores_deberan_demostrar_que_cuentan_con_habilidades__13374c
    - Obligacion_los_flujos_de_fondos_de_los_activos_subyacentes_deben_estar_contractualmente_ide_2080de
    - Obligacion_los_flujos_de_fondos_nocionales_netos_sujetos_a_reapreciacion_en_cada_banda_temp_3cc3d2
    - Obligacion_los_flujos_de_fondos_nocionales_sujetos_a_reapreciacion_de_depositos_a_plazo_con_492ea3
    - Obligacion_los_flujos_de_fondos_nocionales_sujetos_a_reapreciacion_de_prestamos_a_tasa_de_i_4d3da9
    - Obligacion_los_fondos_excedentes_deben_ser_ingresados_y_liquidados_en_el_mercado_de_cambios_a26e9b
    - Obligacion_los_fondos_excedentes_deben_ser_ingresados_y_liquidados_en_el_mercado_de_cambios_a3c944
    - Obligacion_los_fondos_excedentes_que_superen_el_125_de_los_servicios_por_capital_e_interese_f5bc95
    - Obligacion_los_importes_en_moneda_extranjera_se_convertiran_a_pesos_utilizando_el_tipo_de_c_64bba8
    - Obligacion_los_importes_por_debajo_del_umbral_que_no_se_deducen_se_ponderan_en_funcion_del__1e4f1d
    - Obligacion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales__ric_1_2_f58b33
    - Obligacion_los_incrementos_en_las_tasas_de_interes_comisiones_y_o_cargos_deben_ser_justific_86ec5d
    - Obligacion_los_instrumentos_deberan_observar_requisitos_adicionales_para_garantizar_su_capa_e9354a
    - Obligacion_los_instrumentos_incluidos_en_el_coeficiente_de_adecuacion_de_capital_deberan_ob_94f447
    - Obligacion_los_instrumentos_incluidos_en_el_pnc_deben_estar_totalmente_suscriptos_e_integra_385c70
    - Obligacion_los_instrumentos_incluidos_en_el_pnc_deberan_tener_un_plazo_de_vencimiento_origi_c4cd79
    - Obligacion_los_inversores_deberan_ser_notificados_con_la_debida_anticipacion_respecto_de_cu_573728
    - Obligacion_los_inversores_y_tenedores_de_posiciones_de_titulizacion_deben_tener_en_cuenta_l_047ed8
    - Obligacion_los_legajos_deben_incluir_los_analisis_realizados_por_aplicacion_de_normas_sobre_aace6c
    - Obligacion_los_limites_maximos_establecidos_se_aplicaran_sobre_la_responsabilidad_patrimoni_fb916f
    - Obligacion_los_montos_de_las_certificaciones_por_los_regimenes_de_acceso_a_divisas_para_la__1b6a62
    - Obligacion_los_ponderadores_de_riesgo_a_aplicar_a_las_posiciones_de_una_titulizacion_y_a_la_e2297c
    - Obligacion_los_reportes_deberan_contener_informacion_que_identifique_cualquier_incumplimien_d9cd0d
    - Obligacion_los_responsables_titular_y_suplente_deben_asegurar_la_adecuada_atencion_de_los_u_4bbf2e
    - Obligacion_los_riesgos_de_tasa_de_interes_y_de_moneda_extranjera_deberan_mitigarse_en_forma_c4c890
    - Obligacion_los_sujetos_obligados_deben_arbitrar_medios_para_que_comunicaciones_avisos_y_pub_261571
    - Obligacion_los_terminos_y_condiciones_de_los_instrumentos_deberan_incluir_una_disposicion_q_22dbbf
    - Obligacion_los_titulos_de_deuda_con_registro_publico_en_el_exterior_otros_endeudamientos_de_b7803e
    - Obligacion_luego_de_la_ocurrencia_de_un_incumplimiento_u_otro_evento_desencadenante_de_la_a_c5118e
    - Obligacion_luego_de_la_refinanciacion_y_a_los_fines_de_la_clasificacion_debera_tenerse_en_c_795fc1
    - Obligacion_mantener_disponible_el_saldo_actualizado_de_todas_las_financiaciones_otorgadas_i_8e8deb
    - Obligacion_mantener_en_el_legajo_declaracion_jurada_sobre_vinculacion_e_influencia_controla_bc5e32
    - Obligacion_monto_a_deducir_del_ca_total_del_exceso_sobre_el_10_multiplicado_por_la_proporci_b492d9
    - Obligacion_monto_a_deducir_del_co_total_del_exceso_sobre_el_10_multiplicado_por_la_proporci_9b93f2
    - Obligacion_monto_a_deducir_del_pnc_total_del_exceso_sobre_el_10_multiplicado_por_la_proporc_1469a1
    - Obligacion_obligacion_de_aplicar_factor_de_conversion_crediticia_ccf_a_posiciones_fuera_de__5d8a42
    - Obligacion_obligacion_de_observar_el_tratamiento_de_coberturas_de_riesgo_de_credito_vendida_3c5436
    - Obligacion_obligacion_de_permanecer_en_la_categoria_de_alto_riesgo_de_insolvencia_por_lo_me_2848aa
    - Obligacion_obligacion_de_ponderar_las_posiciones_superpuestas_conforme_lo_establecido_en_pu_d6380b
    - Obligacion_obligacion_de_utilizar_la_metodologia_especificada_en_seccion_4_para_contratos_d_2ff7d4
    - Obligacion_para_aportes_de_capital_referidos_en_punto_8_6_3_los_instrumentos_de_deuda_deber_30479c
    - Obligacion_para_asegurar_total_transparencia_hacia_los_inversores_y_asistirlos_en_el_proces_c95462
    - Obligacion_para_carteras_atomizadas_los_documentos_o_derechos_deben_originarse_en_el_curso__f08fc6
    - Obligacion_para_clientes_con_financiaciones_en_moneda_extranjera_independientemente_de_la_f_2de135
    - Obligacion_para_conjuntos_de_neteo_que_contengan_operaciones_con_activos_en_garantia_iliqui_7ca000
    - Obligacion_para_cumplir_con_los_puntos_3_1_o_3_2_de_las_normas_sobre_evaluaciones_creditici_04ee8e
    - Obligacion_para_derivados_de_credito_con_liquidacion_en_efectivo_debe_existir_un_solido_pro_51bb0b
    - Obligacion_para_determinar_el_importe_de_la_cancelacion_se_admitira_computar_el_50_de_las_g_a55d8b
    - Obligacion_para_determinar_el_valor_de_mercado_del_nocional_subyacente_seguir_las_disposici_3ae365
    - Obligacion_para_determinar_la_naturaleza_del_aporte_se_debera_considerar_la_sustancia_del_a_95e2d7
    - Obligacion_para_determinar_las_exigencias_de_codigo_3_se_tendran_en_cuenta_las_instruccione_e1b664
    - Obligacion_para_el_calculo_de_la_exigencia_que_corresponda_integrar_se_considerara_la_ultim_48f523
    - Obligacion_para_el_calculo_de_las_variables_a_y_d_la_sobrecolateralizacion_y_los_fondos_int_978728
    - Obligacion_para_el_calculo_del_costo_financiero_total_se_debe_tomar_en_cuenta_la_tasa_de_in_c1c11e
    - Obligacion_para_el_primer_periodo_de_vigencia_marzo_2015_la_cantidad_de_exigencias_a_consid_363530
    - Obligacion_para_el_riesgo_vega_calcular_la_exigencia_de_capital_multiplicando_la_suma_de_lo_97d087
    - Obligacion_para_financiaciones_mediante_tarjetas_de_credito_los_dias_de_atraso_se_establece_17771f
    - Obligacion_para_las_operaciones_comprendidas_en_el_punto_9_1_8_el_seguimiento_quedara_a_car_357efa
    - Obligacion_para_las_operaciones_comprendidas_en_los_puntos_9_1_6_y_9_1_7_el_seguimiento_que_84d498
    - Obligacion_para_las_operaciones_de_financiacion_debe_aplicarse_lo_dispuesto_en_el_punto_3_2_1be0fe
    - Obligacion_para_las_posiciones_entre_marzo_y_diciembre_2015_el_calculo_del_promedio_de_erc__0bd97a
    - Obligacion_para_las_posiciones_retenidas_en_las_que_el_originante_haya_transferido_el_riesg_8d2d06
    - Obligacion_para_los_activos_listados_en_los_acapites_iii_titulos_valores_del_sector_publico_bdea0f
    - Obligacion_para_mejorar_la_transparencia_y_claridad_sobre_todos_los_ingresos_egresos_y_dema_848118
    - Obligacion_para_monedas_extranjeras_distintas_del_dolar_estadounidense_convertirlas_a_dolar_28c0f9
    - Obligacion_para_opciones_sobre_acciones_indices_bursatiles_oro_o_monedas_extranjeras_calcul_77273b
    - Obligacion_para_opciones_sobre_tasas_de_interes_cuyo_subyacente_sea_un_bono_calcular_vu_mul_0871f9
    - Obligacion_para_operaciones_de_los_puntos_7_11_1_2_a_7_11_1_6_lo_requerido_respecto_a_las_d_a72bf7
    - Obligacion_para_que_cuotapartes_emitidas_por_fondos_comunes_de_inversion_depository_receipt_dee28e
    - Obligacion_ponderador_de_riesgo_correspondiente_a_ccp_se_aplica_a_activos_o_garantias_aport_9e3c1a
    - Obligacion_presentacion_adicional_de_la_factura_comercial_emitida_en_el_pais_por_quien_figu_b8de24
    - Obligacion_presentacion_de_la_exigencia_por_riesgo_operacional_segun_lo_establecido_en_el_p_a5a9e7
    - Obligacion_previamente_se_debera_plantear_cada_situacion_en_forma_individual_a_la_sefyc__cl_afe1e6
    - Obligacion_quien_ingresa_los_fondos_debera_demostrar_que_el_mecanismo_de_pago_utilizado_pre_081b9b
    - Obligacion_reclasificacion_del_deudor_al_nivel_inmediato_superior_cuando_haya_cumplido_con__69143f
    - Obligacion_reconocimiento_total_o_parcial_de_la_cobertura_del_riesgo_de_credito_mediante_la_50555f
    - Obligacion_reevaluacion_de_la_clasificacion_dentro_de_los_tres_meses_respecto_de_los_demas__4802a2
    - Obligacion_reevaluacion_inmediata_de_la_clasificacion_de_clientes_cuyas_financiaciones_comp_0d274e
    - Obligacion_remitir_informacion_de_cambios_negativos_a_deudores_dentro_de_45_dias_de_la_recl_5b7c90
    - Obligacion_resultan_de_aplicacion_las_normas_generales_en_materia_de_seguimiento_de_anticip_60bd62
    - Obligacion_reunir_en_el_legajo_todos_los_elementos_de_juicio_para_evaluaciones_y_clasificac_bf749b
    - Obligacion_se_admite_mantener_la_clasificacion_en_planillas_separadas_si_el_procedimiento_d_64f406
    - Obligacion_se_admitira_la_aplicacion_de_cobros_en_divisas_por_exportaciones_de_bienes_que_c_83f87d
    - Obligacion_se_admitira_la_aplicacion_de_cobros_en_divisas_por_exportaciones_de_bienes_que_c_dd4bb9
    - Obligacion_se_admitira_la_aplicacion_de_divisas_de_cobros_de_exportaciones_de_bienes_a_la_c_48447c
    - Obligacion_se_admitira_la_aplicacion_de_divisas_de_cobros_de_exportaciones_de_bienes_a_la_c_672afb
    - Obligacion_se_admitira_la_aplicacion_de_divisas_de_cobros_de_exportaciones_de_bienes_a_la_c_88452c
    - Obligacion_se_admitira_la_aplicacion_de_divisas_de_cobros_de_exportaciones_de_bienes_a_la_c_c2da26
    - Obligacion_se_admitira_la_aplicacion_de_divisas_de_cobros_de_exportaciones_de_bienes_a_la_c_d06f12
    - Obligacion_se_admitira_que_el_pago_garantizado_tuviera_que_ser_concretado_a_partir_de_la_fe_51fa85
    - Obligacion_se_agregara_una_descripcion_detallada_del_calculo_del_importe_para_el_periodo_in_edfa00
    - Obligacion_se_aplicaran_los_periodos_de_mantenimiento_minimo_del_punto_5_3_2_3_para_sft_y_d_471eb7
    - Obligacion_se_aplicaran_los_ponderadores_de_riesgo_de_contraparte_p_por_operacion_a_los_con_f42691
    - Obligacion_se_computara_el_importe_que_surja_de_aplicar_a_los_valores_contables_de_los_inst_f49fe2
    - Obligacion_se_considerara_cumplido_lo_requerido_con_el_ingreso_de_los_fondos_a_la_posicion__395cea
    - Obligacion_se_considerara_la_ultima_calificacion_informada_para_el_calculo_de_la_exigencia__768b58
    - Obligacion_se_consignara_como_numero_y_fecha_de_resolucion_la_de_la_comunicacion_a_6456__ri_422734
    - Obligacion_se_continuara_informando_codigo_de_consolidacion_3_para_el_ratio_de_apalancamien_48a766
    - Obligacion_se_debe_aplicar_el_tratamiento_de_division_de_conjuntos_de_neteo_tanto_al_calcul_e6c3f2
    - Obligacion_se_debe_computar_el_equivalente_en_la_moneda_del_pais_destino_de_la_exportacion__481490
    - Obligacion_se_debe_contar_con_la_certificacion_de_la_entidad_que_curso_la_operacion_de_canj_c51997
    - Obligacion_se_debe_determinar_en_primer_lugar_el_valor_de_las_partidas_netas_que_correspond_ac5573
    - Obligacion_se_debera_considerar_el_tamano_y_la_estructura_de_la_deuda_externa_en_relacion_c_75cefa
    - Obligacion_se_debera_considerar_la_evaluacion_del_historial_financiero_del_pais_de_residenc_b0d845
    - Obligacion_se_debera_considerar_la_situacion_economica_del_pais_de_residencia_del_deudor_y__d3e41f
    - Obligacion_se_debera_considerar_las_debilidades_implicitas_en_la_cuenta_corriente_del_pais__b1510b
    - Obligacion_se_debera_demostrar_que_tales_riesgos_son_adecuadamente_mitigados_a_traves_de_in_1eb75d
    - Obligacion_se_debera_evaluar_si_los_sistemas_de_informacion_y_las_funciones_de_reporte_son__31c7d3
    - Obligacion_se_debera_tener_en_cuenta_los_criterios_definidos_en_la_seccion_2_de_las_normas__e2e1ac
    - Obligacion_se_deberan_implementar_procedimientos_formales_de_control_de_las_modificaciones__aa5d07
    - Obligacion_se_deberan_validar_de_forma_independiente_las_formulas_matematicas_los_supuestos_563c3d
    - Obligacion_se_incluye_la_posicion_comprada_neta_posicion_comprada_bruta_menos_la_posicion_v_89470e
    - Obligacion_se_incrementaran_los_valores_en_una_unidad_cuando_el_primer_digito_de_las_fracci_231d60
    - Obligacion_se_informaran_dos_partes_de_la_operacion_uno_cuando_el_contrato_subyacente_entra_79475c
    - Obligacion_se_integraran_las_partidas_que_corresponda_segun_el_periodo_informado_codigos_20_a62c71
    - Obligacion_se_recomienda_que_la_forma_de_la_remuneracion_de_quienes_tengan_responsabilidad__c79cdb
    - Obligacion_se_recomienda_que_se_incluyan_disposiciones_que_contemplen_el_reemplazo_de_los_a_5f061b
    - Obligacion_se_recomienda_que_tanto_en_la_oferta_inicial_como_en_la_documentacion_contractua_ed740c
    - Obligacion_se_reconocera_la_proteccion_crediticia_provista_por_empresas_con_grado_de_invers_748ccf
    - Obligacion_se_requerira_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios_7c9cac
    - Obligacion_se_requiere_la_conformidad_previa_del_bcra_cuando_el_acreedor_sea_una_contrapart_407bf7
    - Obligacion_se_requiere_la_conformidad_previa_del_bcra_para_acceder_al_mercado_de_cambios_pa_4d4f6c
    - Obligacion_se_requiere_la_conformidad_previa_del_bcra_para_el_pago_de_intereses_cuando_el_a_212b04
    - Obligacion_se_requiere_la_conformidad_previa_del_bcra_para_el_pago_de_intereses_de_deudas_c_e62e9c
    - Obligacion_se_suspende_el_envio_de_informaciones_con_codigo_de_consolidacion_3_a_partir_del_20973d
    - Obligacion_se_utilizara_cuit_cuil_cdi_cie_o_dni_del_cliente_que_realiza_la_operacion_para_e_5ce310
    - Obligacion_se_volcaran_en_un_manual_de_procedimientos_de_clasificacion_y_prevision__cla_3_3_c18b85
    - Obligacion_sera_admisible_el_acceso_para_el_pago_de_servicios_prestados_o_devengados_a_part_214be8
    - Obligacion_sera_requisito_indispensable_contar_con_la_opinion_favorable_sobre_la_calidad_de_74e824
    - Obligacion_seran_de_aplicacion_las_disposiciones_contenidas_en_la_seccion_2_del_to_sobre_in_d6db9c
    - Obligacion_si_el_exportador_considera_que_existen_errores_en_la_forma_en_que_un_permiso_de__95f961
    - Obligacion_si_el_pago_del_seguro_se_realizo_en_moneda_extranjera_el_monto_percibido_debera__da143a
    - Obligacion_si_entidad_financiera_no_puede_demostrar_que_acuerdos_de_neteo_cumplen_requisito_1507fd
    - Obligacion_si_existen_fondos_destinados_al_pago_de_fletes_de_importaciones_de_bienes_no_inc_795e58
    - Obligacion_si_la_aplicacion_del_desembolso_en_divisas_fuese_posterior_a_la_fecha_del_regist_b4d354
    - Obligacion_si_la_diferencia_de_prevision_es_negativa_debera_informarse_con_ese_signo_previa_c9d410
    - Obligacion_si_la_financiacion_fue_otorgada_por_el_propio_proveedor_el_boleto_de_compra_se_r_8dc6bb
    - Obligacion_si_la_financiacion_fue_otorgada_por_otros_acreedores_del_exterior_habilitados_el_0dc0ef
    - Obligacion_si_la_legislacion_aplicable_no_se_ajusta_a_los_requisitos_de_cesion_efectiva_deb_880153
    - Obligacion_si_no_se_alcanza_acuerdo_dentro_del_plazo_debe_reclasificarse_al_deudor_en_la_ca_36428a
    - Obligacion_siempre_que_se_disponga_de_ellas_y_en_la_medida_de_lo_posible_deberan_utilizarse_016d3b
    - Obligacion_toda_esa_documentacion_debera_ser_apropiadamente_revisada_por_consultores_legale_e7ba25
    - Obligacion_todo_activo_en_garantia_al_que_la_ccp_pueda_recurrir_en_caso_de_incumplimiento_d_6d32bd
    - Obligacion_todo_riesgo_de_tipo_de_cambio_que_surja_de_posiciones_compensadas_en_mercados_di_7cafae
    - Obligacion_todos_los_derechos_inherentes_a_los_documentos_a_cobrar_y_creditos_deberan_ser_t_16f931
    - Obligacion_todos_los_eventos_desencadenantes_que_puedan_afectar_el_orden_de_prelacion_en_lo_7b4240
    - Obligacion_utilizar_el_tipo_de_cambio_de_referencia_del_dolar_estadounidense_difundido_por__b847df
Operacion: 1229 sin aplica_a
    - Operacion_absorcion_de_perdidas_en_instrumentos__cap_8_3_4_1_f35b51
    - Operacion_accesibilidad_a_puntos_de_atencion_al_usuario__pro_2_2_4_1_d7a59a
    - Operacion_acceso_a_divisas_bienes_con_plazo_30_dias__ext_3_18_3_1_4fc7a3
    - Operacion_acceso_a_informacion_de_permisos_de_embarque__ext_8_3_1ca3e8
    - Operacion_acceso_a_informacion_detallada_de_oficializacion__ext_11_1_2_86d8f7
    - Operacion_acceso_adicional_para_garantias_avales_y_cancelacion_de_lineas_de_credito__ext_1_bf342d
    - Operacion_acceso_al_mercado_de_cambios__ext_10_4_3_66ef01
    - Operacion_acceso_al_mercado_de_cambios__ext_13_1_5_f43995
    - Operacion_acceso_al_mercado_de_cambios__ext_3_4_77a47c
    - Operacion_acceso_al_mercado_de_cambios_cancelacion_de_garantias__ext_11_2_1_5_7fbb7c
    - Operacion_acceso_al_mercado_de_cambios_como_apoderado__ext_5_7_3_3_6fdc23
    - Operacion_acceso_al_mercado_de_cambios_con_certificacion__ext_3_17_1_dceba5
    - Operacion_acceso_al_mercado_de_cambios_con_certificacion_de_exportaciones__ext_3_18_1_ac026b
    - Operacion_acceso_al_mercado_de_cambios_con_fondos_de_financiacion__ext_13_3_1_306283
    - Operacion_acceso_al_mercado_de_cambios_con_liquidacion_de_endeudamiento__ext_13_3_3_8adf1c
    - Operacion_acceso_al_mercado_de_cambios_con_liquidacion_simultanea__ext_10_10_2_4_ba9935
    - Operacion_acceso_al_mercado_de_cambios_operaciones_a_termino__ext_6_4_a219ea
    - Operacion_acceso_al_mercado_de_cambios_pago_de_intereses__ext_3_3_2_700024
    - Operacion_acceso_al_mercado_de_cambios_pago_insumos_hidrocarburos_offshore__ext_10_9_1_c3e480
    - Operacion_acceso_al_mercado_de_cambios_pago_medicamentos__ext_10_6_2_bbd520
    - Operacion_acceso_al_mercado_de_cambios_pago_medicamentos_con_ingreso_aduanero_pendiente__e_7dbf9f
    - Operacion_acceso_al_mercado_de_cambios_pagos_con_registro_aduanero_pendiente__ext_10_6_3_04bb48
    - Operacion_acceso_al_mercado_de_cambios_para_cancelacion_de_obligaciones__ext_3_6_2_793fea
    - Operacion_acceso_al_mercado_de_cambios_para_compra_de_moneda_extranjera__ext_3_11_3_684fb8
    - Operacion_acceso_al_mercado_de_cambios_para_compra_de_moneda_extranjera__ext_7_8_5_2_9378c6
    - Operacion_acceso_al_mercado_de_cambios_para_pago_anticipado__ext_10_4_2_e7eb03
    - Operacion_acceso_al_mercado_de_cambios_para_pago_de_bienes_en_depositos_francos__ext_10_9__8c57af
    - Operacion_acceso_al_mercado_de_cambios_para_pago_de_deudas_elegibles__ext_4_8_5_f3470a
    - Operacion_acceso_al_mercado_de_cambios_para_pago_de_importaciones__ext_10_3_2_e82681
    - Operacion_acceso_al_mercado_de_cambios_para_pago_de_importaciones_desde_zonas_francas__ext_4e2e68
    - Operacion_acceso_al_mercado_de_cambios_para_pago_diferido__ext_10_6_5_364426
    - Operacion_acceso_al_mercado_de_cambios_para_pagos_de_importaciones__ext_10_1_9ed65e
    - Operacion_acceso_al_mercado_de_cambios_para_pagos_de_intereses__ext_3_3_1e8afa
    - Operacion_acceso_al_mercado_de_cambios_para_pagos_de_servicios__ext_13_4_b33276
    - Operacion_acceso_al_mercado_de_cambios_para_pagos_diferidos__ext_10_10_1_901b73
    - Operacion_acceso_al_mercado_de_cambios_para_residentes__ext_3_11_2_d881e8
    - Operacion_acceso_al_mercado_de_cambios_para_residentes__ext_3_11_3_05287a
    - Operacion_acceso_al_mercado_de_cambios_residentes__ext_3_11_3_06b1a3
    - Operacion_acceso_al_mercado_de_cambios_simultaneo_con_liquidacion_de_fondos__ext_13_3_2_221d4e
    - Operacion_acceso_mercado_cambios_cancelacion_endeudamientos_con_contraparte_vinculada__ext_754911
    - Operacion_acceso_mercado_cambios_cancelacion_financiaciones__ext_3_6_3_9d7db5
    - Operacion_acceso_mercado_cambios_pago_primas_derivados__ext_3_12_1_699064
    - Operacion_acceso_mercado_cambios_pago_titulos_deuda_refinanciados__ext_3_5_1_7_9b1d78
    - Operacion_acceso_mercado_cambios_pago_utilidades_y_dividendos__ext_14_2_2_a0a1a8
    - Operacion_acceso_mercado_cambios_pagos_importaciones_con_registro_aduanero_pendiente__ext__c77820
    - Operacion_acceso_mercado_cambios_titulos_deuda_refinanciacion__ext_3_5_1_12_44d76c
    - Operacion_acreditacion_de_fondos_en_cuenta_bancaria_en_el_exterior__ext_3_8_2_5a17b7
    - Operacion_acreditacion_de_fondos_en_cuenta_de_corresponsalia__ext_5_6_6653f5
    - Operacion_acreditacion_de_fondos_en_cuenta_en_moneda_extranjera__ext_3_8_2_792b8d
    - Operacion_acreditacion_en_cuentas_en_moneda_extranjera__ext_5_6_d58daf
    - Operacion_acreditacion_fondos_en_cuenta_especial__ext_7_8_4_2_0fbd4d
    - Operacion_activos_intangibles_netos_de_amortizaciones__ric_6_1_2_e0ca9e
    - Operacion_actuacion_como_apoderado_de_no_residente__ext_5_7_3_4_311706
    - Operacion_acuerdo_habilitacion_agente_de_pago__ext_5_8_2_1_d176f4
    - Operacion_acumulacion_cobros_exportaciones_servicios_en_cuentas__ext_2_2_5_4df49e
    - Operacion_acumulacion_de_cobros_de_exportaciones_en_cuentas__ext_3_5_5_eca7b2
    - Operacion_acumulacion_de_fondos_de_exportacion_en_cuentas__ext_14_3_2_c89163
    - Operacion_acumulacion_de_fondos_de_exportacion_en_cuentas__ext_7_11_5_f64bb6
    - Operacion_acumulacion_de_fondos_de_exportacion_en_cuentas_del_exterior__ext_7_9_5_a18d7b
    - Operacion_acumulacion_de_fondos_de_exportaciones_en_cuentas_extranjeras__ext_7_8_5_1_999d13
    - Operacion_adelantos_en_cuenta_corriente__cla_2_1_5_3_39b9cc
    - Operacion_administracion_del_registro_centralizado_de_consultas_y_reclamos__pro_3_1_1_7_6166cc
    - Operacion_administracion_del_registro_de_denuncias_ante_instancias_judiciales_y_o_administ_0ab5ef
    - Operacion_administracion_del_registro_de_reintegros_de_importes__pro_3_1_1_7_20b61d
    - Operacion_admision_de_activos_como_garantia_en_operaciones_de_pase__cap_6_1_3_2_1e7982
    - Operacion_admision_de_activos_como_garantia_metodo_simple__cap_5_3_1_2_f5db38
    - Operacion_adopcion_de_metodos_especificos_de_evaluacion__cla_3_3_7_cba9a3
    - Operacion_adquisicion_de_bienes_medicos_sanitarios_en_el_exterior__ext_10_6_5_ca3964
    - Operacion_adquisicion_de_bonos_bopreal_en_suscripcion_primaria__ext_4_8_2_545db1
    - Operacion_adquisicion_de_criptoactivos__ext_4_1_4_5_8dfcc9
    - Operacion_adquisicion_de_entidades_financieras__cap_11_1_2cc24b
    - Operacion_adquisicion_de_exposiciones_subyacentes_por_spe__cap_3_1_1_8_58d318
    - Operacion_adquisicion_de_joyas_piedras_preciosas_y_metales_preciosos__ext_4_1_4_6_97af97
    - Operacion_adquisicion_de_tarjetas_de_regalo_exterior__ext_4_1_4_7_a30d7d
    - Operacion_adquisicion_de_titulos_en_suscripcion_primaria__ext_5_9_5_73059b
    - Operacion_adquisicion_de_titulos_valores_con_liquidacion_en_moneda_extranjera__ext_8_5_20__0cd234
    - Operacion_afectacion_de_activos_en_garantia__cap_8_4_1_15_806c3d
    - Operacion_afectacion_de_importaciones_por_solicitud_particular_o_courier__ext_10_5_2_ea49c0
    - Operacion_afectacion_de_oficializacion_a_pago_con_ingreso_aduanero_pendiente__ext_10_6_5_a3bd8c
    - Operacion_agrupacion_de_financiaciones_comerciales_con_creditos_de_consumo_o_vivienda__cla_b9098d
    - Operacion_agrupamiento_de_financiaciones_comerciales_con_creditos_de_consumo_o_vivienda__c_61574e
    - Operacion_ajuste_de_exposicion_y_garantia_por_volatilidad__cap_5_3_2_ed3e6c
    - Operacion_ajuste_de_valor_corriente_de_posiciones_menos_liquidas__cap_6_10_2_2_6c297a
    - Operacion_ajuste_de_valor_corriente_posiciones_menos_liquidas__cap_6_10_2_4_d083ea
    - Operacion_ampliacion_de_plazo_para_ingreso_y_liquidacion_de_divisas__ext_7_5_0b1daf
    - Operacion_analisis_de_cartera__cla_3_1_dff9c4
    - Operacion_analisis_de_practicas_y_conductas_de_sujetos_obligados__pro_4_2_2_a16863
    - Operacion_analisis_y_decision_en_otorgamiento_de_facilidades__cla_3_3_2_d8a1a7
    - Operacion_anexion_de_carpetas_al_legajo_prestamos_hipotecarios_prendarios__cla_3_4_3_c8caa8
    - Operacion_anticipo_de_exportaciones_de_bienes_liquidado__ext_7_3_1_b3a1e3
    - Operacion_anticipos_cursados_por_sml__ext_9_7_66d0f7
    - Operacion_anticipos_de_exportaciones_a_paraguay_o_uruguay__ext_9_7_a0b7c0
    - Operacion_anticipos_de_exportaciones_argentinas_en_moneda_destino__ext_4_2_5_1aa1e5
    - Operacion_anticipos_de_exportaciones_argentinas_en_pesos__ext_4_2_1_f4f531
    - Operacion_anticipos_y_prefinanciaciones_de_exportaciones_del_exterior__ext_9_1_3_be60d6
    - Operacion_anticipos_y_prefinanciaciones_de_exportaciones_del_exterior__ext_9_1_4_a570a7
    - Operacion_anticipos_y_prefinanciaciones_de_exportaciones_del_exterior_pendientes__ext_7_3__1fe80f
    - Operacion_apertura_de_cuentas_a_la_vista__pro_2_3_1_948d69
    - Operacion_apertura_de_legajo_de_firmante_en_creditos_cedidos__cla_3_4_1_54cd93
    - Operacion_aplicacion_ampliada_de_cobros_de_exportaciones__ext_7_10_4_e0cadf
    - Operacion_aplicacion_ampliada_de_cobros_de_exportaciones__ext_7_10_5_0e2e9e
    - Operacion_aplicacion_cobros_exportaciones_regimen_fomento_inversion__ext_7_3_9_712333
    - Operacion_aplicacion_de_ampliacion_de_plazo_a_exportaciones__ext_8_4_2_cb55a5
    - Operacion_aplicacion_de_cobros_a_cancelacion_de_titulos_valores__ext_2_2_4_51aaf4
    - Operacion_aplicacion_de_cobros_a_repatriacion_de_aportes__ext_2_2_4_d839be
    - Operacion_aplicacion_de_cobros_de_exportaciones_a_cancelacion_de_financiacion__ext_7_11_2__09c1e5
    - Operacion_aplicacion_de_cobros_de_exportaciones_de_servicios__ext_2_2_4_e0af38
    - Operacion_aplicacion_de_cobros_en_divisas_exportaciones__ext_7_10_1_744acb
    - Operacion_aplicacion_de_divisas_a_cancelacion_de_financiacion__ext_7_11_2_c9dd3b
    - Operacion_aplicacion_de_divisas_a_operaciones_de_cobro_de_exportaciones__ext_7_10_2_6cd682
    - Operacion_aplicacion_de_divisas_cobros_exportaciones__ext_7_10_2_3_bb10dd
    - Operacion_aplicacion_de_divisas_de_anticipos_a_cancelacion_de_prefinanciaciones__ext_7_8_3_adcef2
    - Operacion_aplicacion_de_divisas_de_cobros_a_cancelacion_de_vencimientos__ext_7_11_1_bb7cfc
    - Operacion_aplicacion_de_divisas_de_cobros_de_exportaciones__ext_3_17_3_2_296356
    - Operacion_aplicacion_de_divisas_de_cobros_de_exportaciones__ext_7_3_d1d2da
    - Operacion_aplicacion_de_divisas_de_exportacion_de_bienes__ext_8_4_3_2_c6432f
    - Operacion_aplicacion_de_metodologia_estandar_exigencia_de_capital_por_riesgo_general_de_me_0676b6
    - Operacion_aplicacion_de_multas_por_demoras_en_entrega__ext_8_5_13_f156af
    - Operacion_aplicacion_de_ponderacion_de_riesgo_a_exposicion__cap_10_3_2_2_48e26c
    - Operacion_aplicacion_de_ponderadores_de_riesgo_por_operacion__cap_2_5_2_207dff
    - Operacion_aplicacion_de_tecnica_de_activos_admitidos_como_garantia__cap_5_1_1_b64455
    - Operacion_aplicacion_de_tecnica_de_cobertura_con_garantias_personales__cap_5_1_2_1adbd4
    - Operacion_aplicacion_del_plazo_en_exportaciones_multiproducto__ext_8_4_2_d4a2cd
    - Operacion_aplicacion_divisas_anticipos_prefinanciaciones_posfinanciaciones__ext_7_3_11_dc4549
    - Operacion_aporte_de_depositos_y_obligaciones_por_intermediacion_financiera__cap_8_6_3_88b353
    - Operacion_aporte_en_instrumentos_de_regulacion_monetaria_del_bcra__cap_8_6_2_8d753b
    - Operacion_aportes_de_capital_en_efectivo__cap_8_6_df62f3
    - Operacion_aportes_de_inversion_extranjera_directa__ext_9_1_7_7d37e5
    - Operacion_aportes_registrados_sin_autorizacion_de_capitalizacion__ric_6_1_2_a31657
    - Operacion_arbitraje_sin_transferencias_al_exterior__ext_3_14_4_a9fbb3
    - Operacion_arbitrajes_y_canjes_en_el_exterior__ext_5_12_b69958
    - Operacion_arrendamientos_financieros__cap_2_8_3_1_c07041
    - Operacion_asentamiento_en_rccr_de_presentaciones__pro_3_1_3_bb99ee
    - Operacion_asiento_en_rccr_de_consultas_que_requieren_analisis__pro_3_1_3_3fa479
    - Operacion_asiento_en_rccr_de_reclamos_por_incumplimiento__pro_3_1_3_b37611
    - Operacion_asignacion_coeficiente_15_aumento_exportaciones_bienes__ext_3_18_3_3_27238b
    - Operacion_asignacion_coeficientes_por_tipo_de_bien__ext_3_18_3_885709
    - Operacion_asignacion_de_calificaciones_crediticias__cap_10_2_2_1_8bf9e3
    - Operacion_asignacion_de_calificaciones_ecai_a_ponderadores__cap_10_3_1_1_4f23d1
    - Operacion_asignacion_de_flujos_a_bandas_temporales_o_puntos_medios__ric_11_1_1_6be37e
    - Operacion_asignacion_de_niveles_de_calidad_crediticia__cap_10_3_1_2_3c3cec
    - Operacion_asignacion_de_perdidas_definitiva_al_instrumento__cap_8_3_2_12_2ff779
    - Operacion_asignacion_de_ponderador_a_exposicion_cubierta__cap_5_4_6f6b9c
    - Operacion_asignacion_de_ponderadores_de_riesgo__cap_2_6_3_c67fbb
    - Operacion_asignacion_de_ponderadores_de_riesgo_scra__cap_2_6_2_40a150
    - Operacion_asignacion_instrumentos_tasa_fija_plazo_residual__cap_6_2_2_3_6aeb28
    - Operacion_asignacion_instrumentos_tasa_variable_plazo_ajuste__cap_6_2_2_3_f1e109
    - Operacion_asignacion_ponderador_contraparte_exposicion_sin_garantia__cap_2_12_8_3_b9925f
    - Operacion_asignacion_ponderador_riesgo_exposiciones_moneda_extranjera__cap_2_5_3_1ce012
    - Operacion_asignacion_posiciones_delta_a_bandas_temporales__cap_6_6_3_2_6ba42b
    - Operacion_aumento_de_capacidad_de_transporte_construccion_de_infraestructura__ext_7_9_2_2_13e9c4
    - Operacion_aumento_exportaciones_bienes_ano_2023__ext_3_18_1_de50ec
    - Operacion_aumento_produccion_bienes_financiacion_proyecto_inversion__ext_7_9_2_1_d59e42
    - Operacion_autorizacion_circunstancial_de_sobregiros_en_cuenta_corriente__cla_3_3_8_3fedc8
    - Operacion_bienes_inmuebles_para_uso_propio_sin_escritura_inscripta__ric_6_1_2_d88ca6
    - Operacion_bloqueo_de_tarjetas_y_o_inhabilitacion_de_acceso__pro_2_3_6_48c034
    - Operacion_bloqueo_de_tarjetas_y_o_inhabilitacion_de_acceso_a_home_banking__pro_2_3_6_df91a3
    - Operacion_boleto_de_cambio_de_venta_cancelacion_garantias_comerciales__ext_10_3_7_4ece1a
    - Operacion_boleto_de_cambio_de_venta_pagos_deudas_comerciales__ext_10_3_7_f4fcf6
    - Operacion_boleto_de_cambio_de_venta_pagos_diferidos_importaciones__ext_10_3_7_28d373
    - Operacion_boleto_de_cambio_de_venta_pagos_diferidos_importaciones_bienes_capital__ext_10_3_b06993
    - Operacion_boleto_de_cambio_de_venta_pagos_importaciones__ext_10_4_5_bb6627
    - Operacion_boleto_de_compra_y_o_venta_de_cambio__ext_1_4_5cc8bc
    - Operacion_boleto_de_venta_de_cambio_bonos_bopreal__ext_4_6_2_e18cc0
    - Operacion_boleto_de_venta_de_cambio_bonos_bopreal__ext_4_7_c55cc3
    - Operacion_boleto_de_venta_de_cambio_codigo_b26_bopreal__ext_4_4_d904aa
    - Operacion_boleto_de_venta_de_cambio_importador__ext_4_5_5618df
    - Operacion_boleto_de_venta_de_cambio_utilidades_y_dividendos_bopreal__ext_4_6_1_3d53ec
    - Operacion_boletos_simultaneos_compra_venta_financiacion_comercial__ext_10_7_2_db06d2
    - Operacion_cajeros_automaticos_con_accesibilidad_visual__pro_2_2_2_edea17
    - Operacion_calculo_apr_posicion_titulizacion__cap_3_1_5_4_7eca66
    - Operacion_calculo_bi_a_nivel_consolidado__cap_7_1_1_2_ee1c6b
    - Operacion_calculo_bi_a_nivel_individual__cap_7_1_1_2_992eb2
    - Operacion_calculo_bi_a_nivel_subconsolidado__cap_7_1_1_2_4a1829
    - Operacion_calculo_bi_con_periodos_de_negocios_adquiridos__cap_7_1_1_4_d27399
    - Operacion_calculo_bic__ric_5_2_1_aac5e1
    - Operacion_calculo_co_4_5_de_apr__cap_8_5_1_53cb75
    - Operacion_calculo_coeficientes_gamma_y_vega__cap_6_6_3_1_08aaba
    - Operacion_calculo_de_activo_ponderado_por_riesgo_metodo_integral__cap_5_3_2_3_e5dafc
    - Operacion_calculo_de_activos_ponderados_por_riesgo__ric_8_1_9_4e3e6b
    - Operacion_calculo_de_activos_ponderados_por_riesgo_del_fondo__cap_3_2_1_2_baefc4
    - Operacion_calculo_de_bic_por_tramos_de_bi__cap_7_1_2_793fe8
    - Operacion_calculo_de_capital_por_riesgo_especifico__cap_6_2_1_ece8ca
    - Operacion_calculo_de_cr_para_multiples_acuerdos_sobre_margenes__cap_4_2_1_3_899f16
    - Operacion_calculo_de_desestimaciones_horizontales__ric_4_4_2_0afdbd
    - Operacion_calculo_de_desestimaciones_verticales__ric_4_4_2_efe471
    - Operacion_calculo_de_ead_por_conjunto_de_neteo__cap_4_2_1_27bb12
    - Operacion_calculo_de_equivalente_delta_metodo_delta_plus__cap_6_6_3_bfb9e6
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_credito__ric_3_1_2_d223d8
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_mercado__cap_6_1_1_5_5f23a6
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_mercado__cap_6_1_4_3_0a20b5
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_mercado__cap_6_1_7a5b56
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_tasa_de_interes__cap_6_2_febd94
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_especifico_y_general__cap_6_3_1_315732
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_general_de_mercado__cap_6_2_2_1_d794d7
    - Operacion_calculo_de_exigencia_de_capital_por_riesgo_operacional__ric_5_1_1_6a3adb
    - Operacion_calculo_de_exigencia_maxima_agregada__cap_3_1_12_d193fb
    - Operacion_calculo_de_exigencia_por_riesgo_de_acciones_adicional_por_derivados__ric_4_2_8a1c3e
    - Operacion_calculo_de_exigencia_por_riesgo_de_acciones_especifico__ric_4_2_63800d
    - Operacion_calculo_de_exigencia_por_riesgo_de_acciones_general__ric_4_2_94997d
    - Operacion_calculo_de_exigencia_por_riesgo_de_acciones_total__ric_4_2_2e633e
    - Operacion_calculo_de_exigencia_por_riesgo_de_opciones__ric_4_2_e66555
    - Operacion_calculo_de_exigencia_por_riesgo_de_posiciones_en_commodities__ric_4_2_259390
    - Operacion_calculo_de_exigencia_por_riesgo_de_tasa__ric_4_2_7614b3
    - Operacion_calculo_de_exigencia_por_riesgo_de_tasa_especifico__ric_4_2_9f76af
    - Operacion_calculo_de_exigencia_por_riesgo_de_tasa_general__ric_4_2_ddb04d
    - Operacion_calculo_de_exigencia_por_riesgo_de_tipo_de_cambio__ric_4_2_0f1702
    - Operacion_calculo_de_exigencia_por_riesgo_general_de_tasa__ric_4_4_2_db58a6
    - Operacion_calculo_de_exigencias_de_capital_gamma_y_vega__cap_6_6_3_6_239c02
    - Operacion_calculo_de_exposicion_a_operaciones_de_financiacion_con_titulos_valores__cap_s5_7e37e4
    - Operacion_calculo_de_exposicion_ajustada_por_crc__cap_5_3_2_1_59122a
    - Operacion_calculo_de_exposicion_al_riesgo_de_tasa_de_interes__cap_6_4_2_2_f7ddd6
    - Operacion_calculo_de_fecha_de_vencimiento__ext_8_4_2_28c94e
    - Operacion_calculo_de_medida_de_riesgo_eve_estandarizada__ric_11_2_3_63dcce
    - Operacion_calculo_de_patrimonio_neto_complementario__cap_8_2_3_93b759
    - Operacion_calculo_de_plazo_en_futuros_y_fras__cap_6_2_3_3_d3a727
    - Operacion_calculo_de_posicion_neta_total__cap_6_4_3_98a721
    - Operacion_calculo_de_requerimiento_de_capital_hipotetico_ccp__cap_4_3_3_2_6a5682
    - Operacion_calculo_de_requisito_de_capital_miembro_compensador__cap_4_3_3_2_f2b841
    - Operacion_calculo_de_tipos_de_cambio_minoristas_de_referencia_tcmr__ext_5_2_1_1610a4
    - Operacion_calculo_del_cr_a_nivel_de_conjunto_de_neteo__cap_4_2_1_1_b183c5
    - Operacion_calculo_del_monto_a_ingresar_y_liquidar__ext_8_4_1_74654a
    - Operacion_calculo_del_plazo_de_vencimiento_de_la_crc__cap_5_4_5_cca453
    - Operacion_calculo_del_plazo_de_vencimiento_de_la_exposicion_subyacente__cap_5_4_5_b4056a
    - Operacion_calculo_del_ponderador_de_riesgo_rw__cap_3_1_11_3_1a11f8
    - Operacion_calculo_diario_de_posiciones_e_instrumentos__ric_4_3_097dde
    - Operacion_calculo_diferencia_prevision_regulatoria_vs_contable__cap_8_4_1_1_1222a5
    - Operacion_calculo_equivalente_delta_opciones_sobre_acciones__cap_6_6_3_3_8787f1
    - Operacion_calculo_exigencia_capital_exposiciones_ccp_no_calificadas__cap_4_3_4_2afd09
    - Operacion_calculo_exigencia_capital_minimo_riesgo_operacional__cap_7_3_1_b21cd4
    - Operacion_calculo_exigencia_capital_operaciones_dvp_fallidas__cap_4_1_1_d0ce63
    - Operacion_calculo_exigencia_capital_riesgo_credito_contraparte__cap_6_1_3_1_9c6b87
    - Operacion_calculo_exigencia_capital_riesgo_precio_opciones__cap_6_1_4_2_41c9f2
    - Operacion_calculo_exigencia_capital_riesgo_tipo_cambio__cap_6_4_1_fb1bdd
    - Operacion_calculo_exigencia_riesgo_commodities__ric_4_1_1_9_7547a9
    - Operacion_calculo_exigencia_riesgo_credito_contraparte_derivados__cap_6_1_3_3_e2d61d
    - Operacion_calculo_exigencia_riesgo_credito_sin_inc__ric_8_1_1_394a94
    - Operacion_calculo_exigencia_riesgo_de_mercado__ric_8_1_8_a6ca32
    - Operacion_calculo_exigencia_riesgo_especifico_acciones__ric_4_1_1_4_fe72da
    - Operacion_calculo_exigencia_riesgo_especifico_tasa_interes__ric_4_1_1_2_87a19f
    - Operacion_calculo_exigencia_riesgo_general_acciones__ric_4_1_1_5_ca217a
    - Operacion_calculo_exigencia_riesgo_general_tasa__ric_4_3_1_2_5db4f9
    - Operacion_calculo_exigencia_riesgo_opciones_metodo_simplificado__ric_4_4_4_f6638b
    - Operacion_calculo_exigencia_riesgo_operacional__ric_8_1_7_2477a0
    - Operacion_calculo_importe_posicion_titulizacion__cap_3_1_5_4_1b0b52
    - Operacion_calculo_maxima_perdida_posible_posicion_comprada__cap_6_2_1_3_231603
    - Operacion_calculo_maxima_perdida_posible_posicion_vendida__cap_6_2_1_3_9015fd
    - Operacion_calculo_medida_riesgo_eve_estandarizada__ric_11_1_4_c19133
    - Operacion_calculo_medida_total_riesgo_opciones_automaticas_kao__ric_11_1_4_49d84f
    - Operacion_calculo_mensual_de_exigencia_por_riesgo_operacional__ric_5_1_2_890fe2
    - Operacion_calculo_monto_maximo_certificaciones_anuales__ext_3_18_3_55aac5
    - Operacion_calculo_monto_obligacion_ingreso_liquidacion_divisas__ext_7_8_2_2_a14e6e
    - Operacion_calculo_nocional_efectivo_derivados_tasa_de_interes_por_banda_temporal__cap_4_2__2f5c36
    - Operacion_calculo_pnb_6_de_apr__cap_8_5_2_3270a6
    - Operacion_calculo_posicion_en_opcion_delta__cap_6_6_3_1_18dd4c
    - Operacion_calculo_prudente_del_ltv__cap_2_9_2_3_bce3f2
    - Operacion_calculo_riesgo_gamma_opciones__ric_4_4_4_9171c4
    - Operacion_calculo_riesgo_tasa_interes_eve_estandarizada__ric_8_1_2_aa9f99
    - Operacion_calculo_riesgo_vega_opciones__ric_4_4_4_a28ec5
    - Operacion_calculo_separado_de_activos_ponderados_por_riesgo__cap_5_2_1_5_69896e
    - Operacion_calculo_suma_perdidas_por_escenario__ric_11_1_4_e22c42
    - Operacion_calculo_valor_economico_patrimonio__ric_11_1_4_fc79eb
    - Operacion_calculo_valor_economico_patrimonio_escenario_base__ric_11_1_4_1dbb63
    - Operacion_calculo_variacion_valor_economico_patrimonio__ric_11_1_4_f582bc
    - Operacion_cambio_de_valor_diario_en_portafolio_de_activos__cap_6_7_1_2_0953f5
    - Operacion_cambio_neto_en_posiciones_en_opciones__cap_6_2_2_1_bf9d6d
    - Operacion_canalizacion_de_operaciones_a_traves_del_sml__ext_4_2_9fb060
    - Operacion_cancelacion_capital_intereses_endeudamientos_vpu_rigi__ext_3_5_6_5_1553c5
    - Operacion_cancelacion_de_anticipos_u_otras_financiaciones_de_exportacion__ext_7_7_078ad7
    - Operacion_cancelacion_de_capital_e_intereses_de_endeudamientos_financieros__ext_3_5_6_dd184b
    - Operacion_cancelacion_de_deudas_por_operaciones_financiadas__ext_10_11_1_9340ad
    - Operacion_cancelacion_de_garantias_comerciales_de_importaciones__ext_10_3_1_3_fb78d4
    - Operacion_cancelacion_de_garantias_comerciales_de_importaciones__ext_10_4_1_4_9ce2b8
    - Operacion_cancelacion_de_intereses_mediante_cobros_de_exportaciones__ext_7_11_2_7_c11f0b
    - Operacion_cancelacion_de_servicios_de_capital_e_intereses__ext_3_6_5_346588
    - Operacion_cancelacion_de_servicios_de_endeudamientos_financieros__ext_3_5_5_5c3e11
    - Operacion_cancelacion_en_el_pais_titulos_deuda_vencidos__ext_3_6_1_b24057
    - Operacion_cancelacion_lineas_credito_exterior_exportacion_importacion__ext_3_15_1_fe97bf
    - Operacion_canje_y_arbitraje_con_fondos_de_cuenta_local__ext_3_14_5_def304
    - Operacion_canje_y_arbitraje_con_fondos_depositados_en_cuenta_local__ext_3_14_5_2_8de877
    - Operacion_canje_y_arbitraje_con_fondos_depositados_repatriacion_de_inversiones_de_portafol_7dffc5
    - Operacion_canje_y_arbitraje_para_centrales_locales_de_deposito_colectivo__ext_3_14_6_ed0928
    - Operacion_canje_y_arbitraje_sin_conformidad_previa__ext_3_14_6_9bc66e
    - Operacion_canje_y_o_arbitraje_con_fondos_depositados__ext_4_8_1_11de21
    - Operacion_canje_y_o_arbitraje_con_fondos_en_moneda_extranjera__ext_10_10_2_14_325767
    - Operacion_canje_y_o_arbitraje_con_fondos_en_moneda_extranjera__ext_13_3_9_f12094
    - Operacion_canje_y_o_arbitraje_con_fondos_locales__ext_3_4_4_2_8687c5
    - Operacion_canje_y_o_arbitraje_de_moneda_extranjera__ext_8_5_20_2_421481
    - Operacion_canjes_y_arbitrajes_con_clientes__ext_2_8_29b742
    - Operacion_celebracion_de_acuerdo_preventivo_extrajudicial__cla_6_5_4_7_e661b9
    - Operacion_certificacion_aumento_exportaciones_bienes_plazo_60_dias__ext_3_18_3_2_53c58d
    - Operacion_certificacion_de_afectacion_importacion_temporal__ext_8_5_7_3_d61e54
    - Operacion_certificacion_de_aplicacion_de_anticipos__ext_9_5_e271ba
    - Operacion_certificacion_de_incumplido_en_gestion_de_cobro__ext_8_4_7_8918db
    - Operacion_cesion_de_beneficios_a_proveedores_directos__ext_3_17_3_1_40603b
    - Operacion_cesion_de_documento_en_el_exterior__ext_9_3_5_e6df11
    - Operacion_cesion_de_seguimiento_de_oficializacion__ext_11_1_6_c33f7e
    - Operacion_cesion_sin_recurso_de_operacion_en_entidad_del_exterior__ext_9_3_5_2_47cf54
    - Operacion_cheque_no_a_la_orden_movimiento_de_fondos__ext_2_9_153941
    - Operacion_cierre_de_incumplido__ext_8_4_6_dcfe7c
    - Operacion_clasificacion_con_alto_riesgo_de_insolvencia__cla_6_5_4_9_4697a1
    - Operacion_clasificacion_de_ccp_como_miembro_compensador__cap_4_3_1_2_3be2c3
    - Operacion_clasificacion_de_cliente_con_alto_riesgo_de_insolvencia__cla_6_5_4_3_259a9b
    - Operacion_clasificacion_de_cliente_con_alto_riesgo_de_insolvencia__cla_6_5_4_84f05b
    - Operacion_clasificacion_de_compania_de_seguros_por_mora__cla_4_6_b9df06
    - Operacion_clasificacion_de_deuda_segun_capacidad_de_pago__cla_4_2_501a0f
    - Operacion_clasificacion_de_deudor_con_alto_riesgo_de_insolvencia__cla_6_5_4_10_d287c5
    - Operacion_clasificacion_de_deudor_en_categoria_con_problemas__cla_6_5_3_9_4aa3d2
    - Operacion_clasificacion_de_deudores__cla_3_2_ccda30
    - Operacion_clasificacion_de_deudores__cla_3_3_2_aa3de8
    - Operacion_clasificacion_de_deudores__cla_4_5_0d8876
    - Operacion_clasificacion_de_deudores_de_creditos_fideicomitidos__cla_10_2_1_7fced3
    - Operacion_clasificacion_de_deudores_por_calidad_de_obligados__cla_1_1_148ee4
    - Operacion_clasificacion_de_deudores_por_mora__cla_10_1_fc8477
    - Operacion_clasificacion_de_deudores_por_mora_pscpp__cla_10_4_9aaf89
    - Operacion_clasificacion_de_deudores_y_calculo_de_previsiones__cla_3_6_e01997
    - Operacion_clasificacion_de_exposicion_grado_b__cap_2_6_2_2_aac24f
    - Operacion_clasificacion_de_exposiciones_a_bmd_por_calificacion__cap_2_12_3_2_16a2a6
    - Operacion_clasificacion_de_exposiciones_a_instrumentos__cap_2_11_1_de5fe0
    - Operacion_clasificacion_de_exposiciones_a_instrumentos__cap_2_11_2_48b152
    - Operacion_clasificacion_de_mipymes_por_sgr_y_fondos_de_garantia__cla_10_3_a3e7ae
    - Operacion_clasificacion_en_categoria_irrecuperable__cla_6_5_5_2_8c3036
    - Operacion_clasificacion_en_categoria_irrecuperable__cla_6_5_5_6_017f19
    - Operacion_clasificacion_en_categoria_irrecuperable__cla_6_5_5_8_a1c2c5
    - Operacion_clasificacion_en_situacion_normal__cla_6_5_1_2_470aa5
    - Operacion_clasificacion_mipyme_no_ajustadas_a_criterios__cap_2_12_5_2_60663b
    - Operacion_clasificacion_titulos_publicos_nacionales_rendimiento_dual__cap_2_5_8_33a834
    - Operacion_clasificacion_trimestral_de_clientes_cartera_comercial__cla_6_3_1_4b0e52
    - Operacion_cobertura_de_exposicion_con_activos_admitidos__cap_5_3_1_bc287d
    - Operacion_cobertura_de_pagos_del_deudor_por_garantia__cap_5_2_3_2_d6d663
    - Operacion_cobertura_del_riesgo_de_credito__cap_s5_7f7675
    - Operacion_cobertura_proporcional_de_exposicion_al_riesgo__cap_5_4_2_ddedc5
    - Operacion_cobro_de_comision_y_o_cargo_por_operaciones__ext_3_14_7b84e4
    - Operacion_cobro_de_exportacion_percibido_luego_del_embarque__ext_8_5_20_2_517d79
    - Operacion_cobro_de_exportacion_percibido_luego_del_embarque__ext_8_5_20_87ea45
    - Operacion_cobro_de_exportaciones_de_bienes_y_servicios__ext_14_1_5_c085ca
    - Operacion_cobro_de_exportaciones_ingreso_en_divisas__ext_7_2_1_aea488
    - Operacion_cobro_de_servicios_no_conexos_al_comercio_exterior__ext_4_2_7_2f4b7e
    - Operacion_cobro_efectivo_de_divisas_del_embarque__ext_9_3_5_1_81e6e3
    - Operacion_cobro_o_adeudo_de_importes_al_usuario__pro_2_3_5_1_fe9345
    - Operacion_cobros_anticipados_de_exportaciones_de_bienes__ext_14_1_4_935e19
    - Operacion_cobros_consumos_billeteras_electronicas_no_residentes__ext_2_2_2_3_fa6471
    - Operacion_cobros_consumos_tarjetas_no_residentes__ext_2_2_2_3_b46020
    - Operacion_cobros_de_exportaciones_argentinas_en_moneda_destino__ext_4_2_5_f34f79
    - Operacion_cobros_de_exportaciones_argentinas_en_pesos__ext_4_2_1_7170bf
    - Operacion_cobros_de_exportaciones_de_bienes_economia_del_conocimiento__ext_7_8_4_1_84376e
    - Operacion_cobros_de_exportaciones_de_bienes_en_mercado_de_cambios__ext_8_4_3_1_3ea154
    - Operacion_cobros_de_exportaciones_de_bienes_exceptuados_de_liquidacion__ext_7_2_5_fa6440
    - Operacion_cobros_de_exportaciones_de_bienes_o_servicios__ext_2_6_2_1f233e
    - Operacion_cobros_de_exportaciones_de_bienes_regimen_fomento_inversion__ext_7_10_55a1f4
    - Operacion_cobros_de_siniestros_por_coberturas_de_exportaciones__ext_7_1_1_83c219
    - Operacion_cobros_exportaciones_servicios_turismo_internacional__ext_2_2_2_3_290363
    - Operacion_cobros_o_pagos_en_moneda_extranjera_operaciones_cambiarias_propias__ext_5_10_1_1_ac782c
    - Operacion_cobros_servicios_turisticos_no_residentes__ext_2_2_2_3_042779
    - Operacion_cobros_transporte_pasajeros_no_residentes__ext_2_2_2_3_3fcbd2
    - Operacion_comercio_exterior_companias_financieras__cap_1_2_a8859d
    - Operacion_compensacion_a_tenedores_por_quita__cap_8_3_4_2_64f271
    - Operacion_compensacion_de_posiciones_ponderadas__cap_6_2_2_5_e889a3
    - Operacion_compensacion_de_riesgo_especifico_con_movimiento_direccional_opuesto__cap_6_2_1__7bf92c
    - Operacion_compensacion_integra_de_posiciones_cubiertas_con_derivados_de_credito__cap_6_2_1_53912d
    - Operacion_compensacion_parcial_de_riesgo_especifico_con_correlacion_negativa__cap_6_2_1_4_28f02e
    - Operacion_compensacion_posiciones_compradas_y_vendidas__cap_6_2_3_5_37cf4c
    - Operacion_compra_de_bienes_al_exterior_con_anticipo__ext_10_4_2_1_7c2c6f
    - Operacion_compra_de_billetes_en_moneda_extranjera__ext_3_8_0f0514
    - Operacion_compra_de_cartera_de_creditos__cap_2_5_10_d91ce9
    - Operacion_compra_de_divisas_linea_de_credito_del_exterior__ext_10_7_2_200425
    - Operacion_compra_de_instrumentos_con_financiacion_de_la_entidad__cap_8_3_3_9_5d52e4
    - Operacion_compra_de_instrumentos_pnc__cap_8_3_3_8_f1ce17
    - Operacion_compra_de_moneda_extranjera_acceso_anticipado__ext_3_11_2_29287f
    - Operacion_compra_de_moneda_extranjera_con_anterioridad_al_plazo__ext_3_11_2_1_6b125a
    - Operacion_compra_de_moneda_extranjera_con_aplicacion_especifica__ext_3_11_4_3a76ea
    - Operacion_compra_de_moneda_extranjera_con_debito_en_cuenta_local__ext_4_1_48fff8
    - Operacion_compra_de_moneda_extranjera_formacion_de_activos_externos__ext_3_9_5_b31762
    - Operacion_compra_de_moneda_extranjera_garantias_de_endeudamientos__ext_3_11_1_547342
    - Operacion_compra_de_moneda_extranjera_para_garantias__ext_3_11_1_260284
    - Operacion_compra_de_moneda_extranjera_para_garantias__ext_7_9_6_97386f
    - Operacion_compra_de_moneda_extranjera_para_garantias_de_endeudamientos__ext_3_11_1_3481d4
    - Operacion_compra_de_moneda_extranjera_por_clientes_no_residentes__ext_3_13_1_0045a3
    - Operacion_compra_de_obligaciones_negociables_de_emision_propia__cla_2_2_1_6_ebdfe4
    - Operacion_compra_de_opciones__cap_6_6_1_7bf0b9
    - Operacion_compra_de_titulos_valores_en_mercado_secundario__ext_5_9_3_32991a
    - Operacion_compra_y_venta_de_contratos_de_opciones__cap_6_11_649e46
    - Operacion_compras_moneda_extranjera_no_residentes__ext_3_13_1_47199c
    - Operacion_compraventa_de_titulos_valores_con_liquidacion_mixta__ext_7_5_2_6b8c4e
    - Operacion_compraventa_titulos_valores_liquidacion_cable__ext_4_3_2_2_c9db75
    - Operacion_comprension_de_caracteristicas_estructurales_de_titulizaciones__cap_3_1_3_3_10f9a5
    - Operacion_computacion_de_fondos_de_financiacion_en_mercado_de_cambios__ext_14_5_2_9529e7
    - Operacion_computo_de_aportes_inversion_directa_en_especie__ext_14_5_7_97c0f6
    - Operacion_computo_de_base_consolidada_trimestral__cap_2_3_2_7a3e80
    - Operacion_computo_de_conceptos_sobre_saldos_mensuales__cap_2_3_1_aba85b
    - Operacion_computo_de_datos_por_saldos_a_fin_de_periodo__ric_3_1_1_c3279e
    - Operacion_computo_de_diferencia_positiva_como_con1__cap_11_4_be23b5
    - Operacion_computo_de_financiaciones_en_mercado_de_cambios_por_vpu__ext_14_5_3_0df841
    - Operacion_computo_de_reservas_de_utilidades__cap_8_2_1_4_0d27e9
    - Operacion_computo_de_resultado_positivo_del_ejercicio__cap_8_2_1_5_47eeea
    - Operacion_computo_diario_de_integracion_de_capital__cap_6_7_1_9a9210
    - Operacion_computo_exposiciones_moneda_extranjera_dollar_linked__cap_2_5_8_e8c54c
    - Operacion_computo_fletes_documentacion_transporte_ingreso_aduanero__ext_3_5_1_10_3a4f87
    - Operacion_conceptos_deducibles_del_con1_no_incluidos_en_otros_codigos__ric_6_1_2_05229c
    - Operacion_concertacion_de_cambio__ext_5_6_179846
    - Operacion_confeccion_boleto_cambio_depositos_moneda_extranjera__ext_3_11_5_318517
    - Operacion_confeccion_boleto_compra_aplicacion_fondos__ext_3_11_5_55ff98
    - Operacion_confeccion_boleto_garantias_exportaciones__ext_3_11_5_2d6085
    - Operacion_confeccion_boleto_venta_cancelacion_deuda__ext_3_11_5_44601d
    - Operacion_confeccion_boleto_venta_pago_importaciones__ext_7_11_3_2_77bfe3
    - Operacion_confeccion_de_boleto_de_compra__ext_7_10_2_5_e4421d
    - Operacion_confeccion_de_boleto_de_venta__ext_7_10_2_5_4270f1
    - Operacion_confeccion_de_boletos_sin_movimiento_de_pesos__ext_2_7_7e815d
    - Operacion_consideracion_de_instrumentos_cer_a_tasa_fija__cap_6_1_1_4_461b24
    - Operacion_consignacion_exigencia_riesgo_general_acciones__ric_4_1_1_6_47967f
    - Operacion_consignacion_exigencia_riesgo_general_tasa_interes__ric_4_1_1_3_bc4ac6
    - Operacion_constatacion_de_compatibilidad_en_sistema_online__ext_3_9_4_044de5
    - Operacion_constatacion_de_monto_maximo_y_permisos__ext_3_18_4_063d08
    - Operacion_constitucion_de_depositos_en_moneda_extranjera__ext_3_8_7f1e54
    - Operacion_consulta_de_cotizaciones_minoristas_en_pagina_bcra__ext_5_2_1_727044
    - Operacion_consulta_o_pedido_de_conformidad_previa_operaciones_en_mercado_de_cambios__ext_1_b27b34
    - Operacion_consumos_en_exterior_con_tarjeta_debito__ext_4_1_2_68fcb9
    - Operacion_consumos_en_exterior_con_tarjeta_prepaga__ext_4_1_2_b2fe75
    - Operacion_contabilizacion_de_pasivos_por_derivados_a_valor_razonable__cap_8_4_1_18_968148
    - Operacion_contrato_a_termino_de_moneda_extranjera_u_oro__cap_6_4_2_2_24e69b
    - Operacion_contrato_multiproducto_escision_en_contratos_individuales__pro_2_3_1_2_b71ba8
    - Operacion_conversion_a_pesos_de_posicion_neta_en_moneda_extranjera_y_oro__cap_6_4_3_9e27a3
    - Operacion_conversion_de_compromisos_en_equivalentes_crediticios__cap_12_2_81c2ee
    - Operacion_conversion_de_derivados_a_posiciones_subyacentes__cap_6_2_3_2_58728f
    - Operacion_conversion_de_derivados_en_posiciones_subyacentes__cap_6_3_2_8cff00
    - Operacion_conversion_de_partidas_fuera_de_balance_con_ccf__cap_2_13_af175a
    - Operacion_conversion_en_acciones_ordinarias__cap_8_3_2_12_83dd75
    - Operacion_creditos_documentarios__cla_2_1_5_3_d674e1
    - Operacion_creditos_documentarios_utilizados_de_pago_diferido__cla_2_1_5_4_4febf5
    - Operacion_creditos_frente_al_bcra__cla_2_2_1_7_ccb294
    - Operacion_creditos_para_vivienda_propia__cla_5_1_2_2_5aac61
    - Operacion_creditos_sobre_documentos_o_valores_cedidos_por_deudor_en_concurso__cla_1_2_2_348a44
    - Operacion_cuentas_corrientes_y_especiales_en_el_bcra__cap_2_12_1_2_fdb9e4
    - Operacion_cuentas_de_corresponsalia_con_entidades_del_exterior_sin_investment_grade__ric_6_b792f1
    - Operacion_cumplido_de_embarque_del_permiso_definitivo__ext_7_8_2_5_8f3a2a
    - Operacion_cumplimiento_de_disposiciones_seccion_2_en_puntos_de_atencion__pro_3_1_1_5_81e955
    - Operacion_cumplimiento_parcial_o_total_del_seguimiento_de_permiso__ext_8_4_3_c96e58
    - Operacion_cumplimiento_parcial_o_total_del_seguimiento_de_permiso_de_embarque__ext_8_5_18_0142b3
    - Operacion_cumplimiento_parcial_total_seguimiento_permiso_embarque__ext_8_5_18_9cdb8c
    - Operacion_curso_de_operaciones_en_sml_paraguay_y_uruguay__ext_4_2_10e140
    - Operacion_custodia_de_titulos_del_fgs__ric_8_1_4_07397c
    - Operacion_declaracion_de_incumplimiento_de_contraparte__cap_5_2_2_2_145b43
    - Operacion_deduccion_de_inversiones_en_empresas_de_servicios_complementarios__ric_6_1_2_4b4e65
    - Operacion_deduccion_de_titulos_de_gobiernos_extranjeros__cap_8_4_1_5_a1372e
    - Operacion_deficiencia_diaria_de_capital_por_riesgo_de_mercado__cap_6_7_2_1_532f5d
    - Operacion_demostracion_de_gestion_de_cobro_por_exportador__ext_7_6_3_3_c7a575
    - Operacion_demostracion_de_gestion_de_cobro_sin_accion_judicial__ext_7_6_3_4_b031bb
    - Operacion_denuncia_de_incumplido__ext_8_4_5_4fa095
    - Operacion_depositos_a_plazo_con_riesgo_de_retiro_anticipado__ric_11_1_2_f18b60
    - Operacion_depositos_sin_vencimiento__ric_11_1_2_f9faf8
    - Operacion_derivados_en_mercado_de_valores_con_acuerdo_bilateral__cap_4_3_2_ab417a
    - Operacion_descalce_de_monedas_en_proteccion_crediticia__cap_5_4_6_e70370
    - Operacion_descalce_de_plazos_en_titulizacion_sintetica__cap_3_1_13_3_f8eb8b
    - Operacion_descripcion_del_procedimiento_de_clasificacion__cla_3_3_5_0303d0
    - Operacion_descuento_de_documento_en_el_exterior__ext_9_3_5_1c224b
    - Operacion_descuento_de_operacion_en_entidad_del_exterior__ext_9_3_5_3_a94c6b
    - Operacion_desestimacion_horizontal_de_posiciones_compensadas__cap_6_2_2_1_657a74
    - Operacion_desestimacion_vertical_de_posiciones_compensadas__cap_6_2_2_1_98e340
    - Operacion_designacion_de_personal_representante_del_responsable__pro_3_1_1_674b40
    - Operacion_destinacion_de_prestamos_a_spe__cap_2_9_2_7_23bc19
    - Operacion_destinaciones_suspensivas_exportaciones_temporarias__ext_8_5_17_21_f7b37a
    - Operacion_detalle_de_personas_con_control_directo_y_grupo_economico__ext_3_16_3_3_6215fd
    - Operacion_deteccion_de_transferencias_con_informacion_incompleta__ext_5_5_2_5f1a9b
    - Operacion_determinacion_de_exigencia_de_capital_titulizacion__cap_3_1_11_4282fe
    - Operacion_determinacion_de_exigencia_por_riesgo_de_credito_de_contraparte__ric_3_1_6_a11a94
    - Operacion_determinacion_de_exigencia_por_riesgo_especifico__cap_6_6_3_b94d7e
    - Operacion_determinacion_de_necesidad_de_ajustes_a_posiciones_menos_liquidas__cap_6_10_2_1_54f581
    - Operacion_determinacion_de_ponderador_riesgo_inversion_primer_fondo__cap_3_2_2_78f9ce
    - Operacion_determinacion_de_responsabilidad_patrimonial_computable__cap_1_3_8113e7
    - Operacion_determinacion_de_responsabilidad_patrimonial_computable__ric_6_1_e931c1
    - Operacion_determinacion_de_rpc_en_fusion__cap_11_2_99870b
    - Operacion_determinacion_del_plazo_para_ingreso_y_liquidacion__ext_8_4_2_80cb85
    - Operacion_determinacion_diaria_de_integracion_por_riesgo_de_mercado__cap_1_3_93d6d2
    - Operacion_determinacion_exigencia_capital_descalce_plazos__cap_3_1_13_3_54370a
    - Operacion_determinacion_exigencia_riesgo_de_mercado__ric_12_2_3d7459
    - Operacion_determinacion_exigencia_riesgo_de_mercado__ric_4_1_1_1_b7cee7
    - Operacion_determinacion_ponderador_riesgo_exposiciones__cap_2_5_4_02f9aa
    - Operacion_determinacion_ponderador_riesgo_tasa_variable__cap_6_2_2_3_26a875
    - Operacion_devolucion_de_fondos_al_emisor__ext_5_5_3_539e29
    - Operacion_devolucion_de_fondos_del_exterior_pago_con_registro_aduanero_pendiente__ext_10_5_3d3c12
    - Operacion_devoluciones_de_operaciones_sml__ext_4_2_4_b8553c
    - Operacion_diferencias_por_insuficiencia_de_previsiones_minimas__ric_6_1_2_0d5a43
    - Operacion_discriminacion_riesgo_por_mercado__ric_4_1_1_5_18d37d
    - Operacion_diversificacion_de_cartera_minorista__cap_2_8_3_2_720b6e
    - Operacion_division_de_conjunto_de_neteo_en_subconjuntos__cap_4_2_1_3_981363
    - Operacion_division_de_exposicion_con_multiples_tecnicas_crc__cap_5_2_1_5_a50635
    - Operacion_division_de_tramo_en_subtramos_cubierto_y_descubierto__cap_3_1_13_2_981355
    - Operacion_donacion_de_bienes_al_ministerio_de_salud__ext_10_6_5_09ae57
    - Operacion_donacion_de_organos_y_sangre_humana__ext_8_5_17_11_519d57
    - Operacion_efectivo_en_cajeros_automaticos__cap_2_12_1_1_1adcb2
    - Operacion_efectivo_en_transito_con_asuncion_de_responsabilidad__cap_2_12_1_1_318fbe
    - Operacion_ejercicio_de_opcion_de_exclusion__cap_3_1_4_3_b3a80d
    - Operacion_elaboracion_de_reportes_por_responsable_de_atencion__pro_3_2_3_4_52b5bd
    - Operacion_elegibilidad_operaciones_7_9_1_1_a_7_9_1_3__ext_7_9_2_5b990b
    - Operacion_emision_de_acciones_ordinarias_por_subsidiarias__cap_8_2_1_9_7e0e8b
    - Operacion_emision_de_certificacion_de_acceso_al_mercado_de_cambios__ext_11_1_1_5_d99af0
    - Operacion_emision_de_certificacion_de_aumento_de_exportaciones__ext_3_18_2_4_515653
    - Operacion_emision_de_certificacion_de_cumplido__ext_8_4_4_649ef1
    - Operacion_emision_de_certificacion_para_acceso_al_mercado_de_cambios__ext_11_1_3_970bee
    - Operacion_emision_de_certificaciones_a_pedido_del_importador__ext_11_1_1_11_05f6e3
    - Operacion_emision_de_certificaciones_bopreal__ext_11_1_1_8_fa0284
    - Operacion_emision_de_certificaciones_de_acceso__ext_11_1_1_9_beb9ac
    - Operacion_emision_de_certificaciones_de_acceso_al_mercado_de_cambios__ext_11_1_1_4_736b6e
    - Operacion_emision_de_certificaciones_de_acceso_al_mercado_de_cambios__ext_11_1_1_7_83b37e
    - Operacion_emision_de_certificaciones_de_aplicacion__ext_9_3_13_6303cb
    - Operacion_emision_de_certificaciones_de_aplicacion__ext_9_3_6_e1f723
    - Operacion_emision_de_certificaciones_de_aplicacion_con_imputacion__ext_9_3_1_d079ba
    - Operacion_emision_de_certificaciones_de_aplicacion_de_divisas__ext_9_3_1_e30f26
    - Operacion_emision_de_certificaciones_de_aplicacion_de_divisas__ext_9_3_9_b3b62e
    - Operacion_emision_de_certificaciones_de_aplicacion_posfinanciaciones_por_descuentos_cesion_795237
    - Operacion_emision_de_certificaciones_de_aumento_de_exportaciones__ext_3_17_2_1_a0fd83
    - Operacion_emision_de_certificaciones_de_aumento_de_exportaciones__ext_3_17_3_4_7ccd35
    - Operacion_emision_de_certificaciones_de_seguimiento_de_importacion__ext_11_1_1_10_82cd8e
    - Operacion_emision_de_certificaciones_decreto_277_22__ext_3_17_4_fdaf97
    - Operacion_emision_de_certificaciones_para_afectar_oficializacion__ext_11_1_1_6_28933d
    - Operacion_emision_de_certificaciones_por_porcion_no_liquidada_posfinanciaciones__ext_9_3_4_cf5f96
    - Operacion_emision_de_garantia_financiera_por_pedido_de_residente__ext_3_15_2_2_4503fd
    - Operacion_emision_de_instrumentos_por_subsidiarias_en_supervision_consolidada__cap_8_2_2_3_690b4e
    - Operacion_emision_de_nuevas_acciones__cap_8_3_4_4_dc4307
    - Operacion_emision_de_pagares_con_oferta_publica__ext_2_5_0fd59e
    - Operacion_emision_de_titulos_de_deuda_cobros_de_exportaciones__ext_7_11_1_6_ca9ba2
    - Operacion_emision_de_titulos_de_deuda_con_registro_exterior__ext_14_2_1_1_ac5df5
    - Operacion_emision_de_titulos_de_deuda_con_registro_publico__ext_2_5_f60769
    - Operacion_emision_de_valores_de_deuda_fiduciaria__ext_2_5_4fcec9
    - Operacion_emision_inmediata_de_acciones__cap_8_3_4_3_b1d187
    - Operacion_emision_instrumentos_pnc__cap_8_3_3_3_d5f5c6
    - Operacion_emision_titulos_deuda_con_registro_publico_exterior__ext_7_11_1_5_57fad4
    - Operacion_emision_titulos_valores_subordinados__cap_8_4_1_6_096280
    - Operacion_enajenacion_de_activos_no_financieros_no_producidos__ext_2_3_dae476
    - Operacion_encomendacion_de_tarea_de_clasificacion_al_sector_de_creditos__cla_3_5_2_4b4a6b
    - Operacion_encomienda_de_tarea_de_clasificacion_a_area_independiente__cla_3_5_1_07c20a
    - Operacion_encomienda_de_tarea_de_clasificacion_a_profesionales_externos__cla_3_5_3_26f15e
    - Operacion_endeudamiento_financiero_comprendido_en_3_5__ext_3_5_1_11_1d103f
    - Operacion_endeudamientos_financieros_con_el_exterior__ext_14_2_1_1_f0d73a
    - Operacion_endeudamientos_financieros_con_el_exterior__ext_9_1_6_0ad525
    - Operacion_enfoque_integral_calculo_de_exposicion_ajustada__ric_3_1_3_c77f27
    - Operacion_enfoque_simple_cobertura_con_garantias__ric_3_1_3_e0ffb1
    - Operacion_entrega_de_billetes_en_moneda_extranjera__ext_3_8_2_ca2041
    - Operacion_entrega_de_declaracion_jurada_por_exportador__ext_7_5_5_2_049066
    - Operacion_entrega_de_fondos_o_activos_a_personas_vinculadas__ext_3_16_3_95df57
    - Operacion_entrega_de_nuevos_titulos_en_canje_recompra_rescate__ext_3_5_1_6_a6d197
    - Operacion_equivalente_delta_neto_cartera_opciones_divisas__cap_6_4_2_1_f7c941
    - Operacion_equivalente_delta_neto_de_cartera_de_opciones_sobre_divisas__ric_4_4_3_b7932a
    - Operacion_evaluacion_crediticia_con_calificacion_internacional__cla_2_2_4_f3831a
    - Operacion_evaluacion_de_capacidad_de_repago__cla_4_4_329f10
    - Operacion_evaluacion_de_capacidad_de_repago_del_deudor__cla_6_2_ca1ceb
    - Operacion_excesos_a_limites_de_afectacion_de_activos_en_garantia__ric_6_1_2_74f0a0
    - Operacion_exclusion_de_instrumentos_de_capital_de_rpc__cap_11_3_ea90fc
    - Operacion_exclusion_futuros_y_forwards_con_subyacentes__cap_6_2_3_5_02bfe3
    - Operacion_exigencia_de_capital_para_derivado_de_credito_de_enesimo_incumplimiento_n_1__cap_30f74c
    - Operacion_exigencia_de_capital_para_derivado_de_credito_de_primer_incumplimiento__cap_6_2__7d35e1
    - Operacion_exigencia_de_capital_por_riesgo_de_commodities__cap_6_1_1_2_6682c9
    - Operacion_exigencia_de_capital_por_riesgo_de_tipo_de_cambio__cap_6_1_1_2_b9ed74
    - Operacion_exigencia_por_riesgo_de_posiciones_en_opciones__ric_4_1_1_8_7f54f0
    - Operacion_exigencia_por_riesgo_de_tipo_de_cambio__ric_4_1_1_7_1e3160
    - Operacion_expansion_de_posiciones_superpuestas__cap_3_1_9_684b19
    - Operacion_exportacion_a_consumo_automotores_nacionales_ley_19_486__ext_8_5_17_25_3427e8
    - Operacion_exportacion_a_consumo_bienes_excluidos_equipaje__ext_8_5_17_18_6336e1
    - Operacion_exportacion_a_consumo_con_destinacion_de_importacion_temporaria__ext_8_5_17_17_faed20
    - Operacion_exportacion_alcanzada_por_beneficios_rigi__ext_8_5_21_8d0b2c
    - Operacion_exportacion_amparada_por_decreto_929_13__ext_8_5_22_47c08d
    - Operacion_exportacion_area_aduanera_especial_a_areas_francas__ext_8_5_17_14_173f85
    - Operacion_exportacion_bienes_con_fines_promocionales__ext_8_5_17_20_03e510
    - Operacion_exportacion_con_incorporacion_de_bienes_importados_temporalmente__ext_8_5_7_4ed03c
    - Operacion_exportacion_de_bienes_con_certificacion_secoexpo__ext_3_18_2_1_caac8d
    - Operacion_exportacion_de_bienes_con_oficializacion_desde_02_09_19__ext_8_1_d64554
    - Operacion_exportacion_de_bienes_por_vpu_rigi__ext_14_1_2_784c12
    - Operacion_exportacion_de_bienes_vpu_rigi__ext_14_1_1_8da28c
    - Operacion_exportacion_de_valores_mediante_regimen_ec51__ext_8_5_17_27_54d919
    - Operacion_exportacion_desde_territorio_nacional_continental_al_area_franca__ext_8_5_17_15_07e9c0
    - Operacion_exportacion_efectos_personales_profesion_u_oficio__ext_8_5_17_26_f2de31
    - Operacion_exportacion_en_consignacion__ext_8_5_17_12_e66a22
    - Operacion_exportaciones_a_zonas_francas_nacionales__ext_8_5_17_22_8dc7d1
    - Operacion_exportaciones_al_area_aduanera_especial__ext_8_5_17_16_e90000
    - Operacion_exportaciones_por_cuenta_y_orden_de_terceros__ext_7_8_1_a48700
    - Operacion_exposicion_a_bmd_con_criterios_de_admisibilidad__cap_2_12_3_1_807bb4
    - Operacion_exposicion_a_deuda_subordinada__cap_2_12_10_2_a4e42a
    - Operacion_exposicion_a_empresas_con_grado_de_inversion__cap_2_12_5_1_2ff11c
    - Operacion_exposicion_a_empresas_demas__cap_2_12_5_4_4eb89a
    - Operacion_exposicion_a_entidades_financieras_corto_plazo__cap_2_12_4_2_28a4af
    - Operacion_exposicion_a_entidades_financieras_demas__cap_2_12_4_2_e2bceb
    - Operacion_exposicion_a_gobiernos_y_bancos_centrales__cap_2_12_2_2_674f2d
    - Operacion_exposicion_a_otros_estados_soberanos_o_sus_bancos_centrales__cap_2_12_2_5_55b981
    - Operacion_exposicion_a_participaciones_en_el_capital__cap_2_12_10_2_a3ee3e
    - Operacion_exposicion_a_sector_publico_no_financiero__cap_2_12_2_4_fd5dc9
    - Operacion_exposicion_al_bcra_en_pesos__cap_2_12_2_1_451997
    - Operacion_exposicion_con_garantia_hipotecaria_residencial__cap_2_12_8_1_e124d9
    - Operacion_exposicion_con_garantia_hipotecaria_sobre_inmuebles_comerciales__cap_2_12_8_2_b33e17
    - Operacion_exposicion_con_garantia_hipotecaria_sobre_inmuebles_residenciales__cap_2_12_9_1_0ab33d
    - Operacion_exposicion_crediticia_con_crc_reconocidas__cap_5_2_1_4_785a0e
    - Operacion_exposicion_frente_a_contraparte_individual__cap_2_8_3_3_84883a
    - Operacion_exposicion_garantizada_por_sgr_o_fondo_publico__cap_2_12_7_e096ae
    - Operacion_exposiciones_a_acciones__cap_2_12_10_1_df8cdd
    - Operacion_exposiciones_a_ccp__cap_2_12_14_dd0337
    - Operacion_exposiciones_a_deuda_subordinada_e_instrumentos_de_capital__cap_2_12_10_1_af9a13
    - Operacion_exposiciones_a_entidades_financieras_del_exterior__cap_2_6_1_164096
    - Operacion_exposiciones_a_entidades_financieras_del_pais__cap_2_6_1_e1efdb
    - Operacion_exposiciones_con_coberturas_de_riesgo_de_credito__cap_2_12_9_3_9a98bb
    - Operacion_exposiciones_de_clientes_transaccion_con_miembro_compensador_como_intermediario__8beb99
    - Operacion_exposiciones_de_miembros_compensadores_con_sus_clientes__cap_4_3_3_1_a81e94
    - Operacion_exposiciones_en_incumplimiento_sin_cobertura_de_riesgo__cap_2_12_9_2_60a4a8
    - Operacion_exposiciones_minoristas_no_normativas__cap_2_12_6_3_d9ae14
    - Operacion_exposiciones_por_operaciones_de_negociacion_miembros_compensadores_con_ccp__cap__2aeb63
    - Operacion_extension_de_constancia_de_consulta_o_reclamo__pro_3_2_2_2_063a11
    - Operacion_facilidades_de_liquidez_titulizacion__cap_3_1_10_6021f5
    - Operacion_financiacion_comercial_por_importacion_de_bienes__ext_7_11_1_1_9b325b
    - Operacion_financiacion_comercial_por_importacion_de_bienes__ext_7_11_1_2_dff428
    - Operacion_financiacion_de_consumos_en_moneda_extranjera__ext_3_6_4_1_f83d26
    - Operacion_financiacion_del_exterior_con_cambio_de_acreedor__ext_10_2_4_8_cc5abe
    - Operacion_financiacion_especializada_grandes_proyectos_infraestructura_etapa_preoperativa__4baf85
    - Operacion_financiacion_por_sucursal_subsidiaria_local__cap_2_2_3_3_fb925e
    - Operacion_financiacion_puntos_7_11_1_1_a_7_11_1_4__ext_7_11_2_4_c3ec14
    - Operacion_financiacion_puntos_7_11_1_5_a_7_11_1_6__ext_7_11_2_4_cbbd4c
    - Operacion_financiaciones_a_clientes_agricolas_no_mipyme_con_acopio__cap_11_5_532247
    - Operacion_financiaciones_a_clientes_agricolas_no_mipymes__ric_3_1_8_45aec0
    - Operacion_financiaciones_a_mipyme__cap_2_8_3_1_312f1e
    - Operacion_financiaciones_asociadas_a_importaciones_de_bienes__ext_9_1_8_aceaf0
    - Operacion_financiaciones_comerciales_en_moneda_extranjera__ext_14_2_1_7_adb88f
    - Operacion_financiaciones_comerciales_importacion_bienes_capital__ext_14_2_1_9_680390
    - Operacion_financiaciones_comerciales_o_financieras_importaciones_de_bienes__ext_7_3_10_abb286
    - Operacion_financiaciones_de_exportaciones_pendientes_al_31_08_19__ext_9_1_2_f3ca4d
    - Operacion_financiaciones_en_moneda_extranjera_entidades_financieras_locales__ext_14_2_1_5_e74a27
    - Operacion_financiaciones_financieras_en_moneda_extranjera__ext_14_2_1_6_755583
    - Operacion_financiaciones_minoristas_a_personas_humanas__cap_2_8_3_4_b042ab
    - Operacion_financiaciones_por_filiales_subsidiarias_locales__cla_2_2_4_3_735a97
    - Operacion_financiaciones_rotativas_revolving__cap_2_8_3_1_f03b91
    - Operacion_financiamiento_de_posiciones_en_commodities_con_exposicion_a_tasa_de_interes__ca_60d0c3
    - Operacion_financiamiento_de_posiciones_en_commodities_con_exposicion_a_tipo_de_cambio__cap_009871
    - Operacion_flujo_de_fondos_insuficiente_para_cobertura_de_intereses__cla_6_5_4_1_f40514
    - Operacion_fondo_de_garantia_para_incumplimientos_productos_mixtos__cap_4_3_3_2_53f405
    - Operacion_fondo_de_garantia_segregado_por_tipo_de_producto__cap_4_3_3_2_8645b5
    - Operacion_futuros_y_contratos_a_termino_como_combinacion_de_posiciones__cap_6_2_3_3_429df5
    - Operacion_ganancias_por_venta_o_cesion_de_cartera_con_responsabilidad__ric_6_1_2_8722e5
    - Operacion_ganancias_por_ventas_de_operaciones_de_titulizacion__ric_6_1_2_15bf20
    - Operacion_garantias_directas_explicitas_irrevocables_e_incondicionales__cap_5_4_1_68cb37
    - Operacion_garantias_otorgadas_en_moneda_extranjera__ric_4_4_3_3270ce
    - Operacion_giro_de_divisas_al_exterior_utilidades_y_dividendos__ext_3_4_4_1_245074
    - Operacion_giro_de_divisas_por_utilidades_y_dividendos__ext_3_4_66187e
    - Operacion_giro_de_fondos_a_entidad_financiera_del_exterior__ext_11_1_3_12_9075c0
    - Operacion_identificacion_cliente_mediante_firmas_electronicas_digitales__ext_5_4_2_1_8466d1
    - Operacion_identificacion_de_riesgos_significativos__cap_6_8_3_1_e56616
    - Operacion_importacion_posicion_ncm_8802_11_00__ext_12_1_61b5a6
    - Operacion_importacion_posicion_ncm_8802_12_10__ext_12_1_203c52
    - Operacion_importacion_posicion_ncm_8802_12_90__ext_12_1_1e8fdc
    - Operacion_importacion_posicion_ncm_8802_20_10__ext_12_1_483212
    - Operacion_importacion_posicion_ncm_8802_20_21__ext_12_1_0d7dd7
    - Operacion_importacion_posicion_ncm_8802_20_22__ext_12_1_24150c
    - Operacion_importacion_posicion_ncm_8802_20_90__ext_12_1_3e93ee
    - Operacion_importacion_posicion_ncm_8802_30_10__ext_12_1_2408b9
    - Operacion_importacion_posicion_ncm_8802_30_21__ext_12_1_56bea2
    - Operacion_importacion_posicion_ncm_8802_30_29__ext_12_1_9b71cd
    - Operacion_importacion_posicion_ncm_8802_30_31__ext_12_1_6b09d7
    - Operacion_importacion_posicion_ncm_8802_30_39__ext_12_1_6cc0f9
    - Operacion_importacion_posicion_ncm_8802_30_90__ext_12_1_6ccb8f
    - Operacion_importacion_posicion_ncm_8802_40_10__ext_12_1_d604ba
    - Operacion_importacion_posicion_ncm_8802_40_90__ext_12_1_e36051
    - Operacion_imputacion_complemento_operacion_precios_revisables__ext_8_5_15_bf5ab7
    - Operacion_imputacion_de_bienes_exportados_temporalmente_no_reimportables__ext_8_5_9_4fe825
    - Operacion_imputacion_de_conceptos_fob_no_pactados__ext_8_5_1_caf871
    - Operacion_imputacion_de_gastos_complementarios_fob__ext_8_5_1_24dfba
    - Operacion_imputacion_de_instrumento_a_cartera_de_negociacion__cap_6_1_2_1_efd8dd
    - Operacion_imputacion_de_liquidaciones_al_permiso_de_embarque__ext_7_8_2_3_892e74
    - Operacion_imputacion_de_liquidaciones_al_permiso_de_embarque_definitivo__ext_7_8_2_3_0db08a
    - Operacion_imputacion_de_oficializacion_a_excepcion_de_ingreso_y_liquidacion__ext_11_1_5_3_84da6d
    - Operacion_imputacion_en_sepaimpo_como_gestion_de_cobro__ext_10_5_5_2_00bb51
    - Operacion_imputacion_exportacion_bienes_sin_contravalor_en_divisas__ext_8_5_3_2_30d655
    - Operacion_imputacion_gastos_colocacion_bienes_exterior__ext_8_5_12_2f7dca
    - Operacion_imputacion_posiciones_titulos_deuda_escalas_vencimientos__cap_6_2_2_3_8f0a08
    - Operacion_inclusion_de_accion_en_co__cap_8_3_1_9f00e1
    - Operacion_inclusion_de_cliente_en_categoria_de_clasificacion__cla_6_5_05c324
    - Operacion_inclusion_de_instrumentos_en_el_ca__cap_8_3_2_a9a065
    - Operacion_inclusion_de_instrumentos_en_pnc__cap_8_2_3_4_d08a9c
    - Operacion_inclusion_de_intereses_y_otros_ingresos_en_posicion__cap_6_4_2_3_cb42a9
    - Operacion_inclusion_en_cartera_comercial_creditos_consumo_vivienda__cla_5_1_1_1_8f5956
    - Operacion_inclusion_ganancias_perdidas_instrumentos_financieros_valor_razonable__cap_8_2_1_d758f4
    - Operacion_inclusion_garantias_otorgadas_en_posicion_abierta__cap_6_4_2_1_63d752
    - Operacion_inclusion_ingresos_egresos_futuros_netos_con_cobertura_total__cap_6_4_2_1_fd08aa
    - Operacion_inclusion_revaluacion_propiedad_planta_equipo_intangibles__cap_8_2_1_7_07b07d
    - Operacion_inclusion_saldo_deudor_otros_resultados_integrales_no_mencionados__cap_8_2_1_7_578020
    - Operacion_incorporacion_de_dividendo_cupon_reajustable__cap_8_3_3_7_bed843
    - Operacion_incorporacion_de_informacion_al_sepaimpo__ext_10_2_6_55f84e
    - Operacion_incorporacion_de_inmuebles_al_patrimonio__cap_8_4_1_8_1cc4ea
    - Operacion_incorporacion_neto_delta_opciones_oro_monedas__cap_6_6_3_4_919d00
    - Operacion_incorporacion_posicion_ponderada_delta_opciones_productos_basicos__cap_6_6_3_5_2c5df3
    - Operacion_incremento_exigencia_activos_inmovilizados_determinado_por_sefyc__ric_9_2_1_1ee271
    - Operacion_incremento_exigencia_activos_inmovilizados_incumplimientos_reiterados__ric_9_2_1_263b4e
    - Operacion_incremento_exigencia_activos_inmovilizados_informacion_en_termino__ric_9_2_1_77ccc8
    - Operacion_incremento_exigencia_activos_inmovilizados_informacion_fuera_de_termino__ric_9_2_9b56c6
    - Operacion_incremento_exigencia_derivados_sobre_commodities_determinado_por_sefyc__ric_9_2__516b60
    - Operacion_incremento_exigencia_derivados_sobre_commodities_incumplimientos_reiterados__ric_8bb9bb
    - Operacion_incremento_exigencia_derivados_sobre_commodities_informacion_en_termino__ric_9_2_9d9873
    - Operacion_incremento_exigencia_derivados_sobre_commodities_informacion_fuera_de_termino__r_001b3a
    - Operacion_incremento_exigencia_fideicomisos_financieros_100__ric_9_2_1_888081
    - Operacion_incremento_exigencia_fideicomisos_financieros_25__ric_9_2_1_431212
    - Operacion_incremento_exigencia_fideicomisos_financieros_50__ric_9_2_1_a34494
    - Operacion_incremento_exigencia_graduacion_del_credito_determinado_por_sefyc__ric_9_2_1_202af8
    - Operacion_incremento_exigencia_graduacion_del_credito_incumplimientos_reiterados__ric_9_2__245132
    - Operacion_incremento_exigencia_graduacion_del_credito_informacion_en_termino__ric_9_2_1_f352e4
    - Operacion_incremento_exigencia_graduacion_del_credito_informacion_fuera_de_termino__ric_9__1b9788
    - Operacion_incremento_exigencia_grandes_exposiciones_determinado_por_sefyc__ric_9_2_1_83343b
    - Operacion_incremento_exigencia_grandes_exposiciones_incumplimientos_reiterados__ric_9_2_1_797b8c
    - Operacion_incremento_exigencia_grandes_exposiciones_informacion_en_termino__ric_9_2_1_ff414c
    - Operacion_incremento_exigencia_grandes_exposiciones_informacion_fuera_de_termino__ric_9_2__e94cb5
    - Operacion_incremento_exigencia_participaciones_en_capital_de_empresas__ric_9_2_1_d783eb
    - Operacion_incremento_exigencia_sector_publico_no_financiero_determinado_por_sefyc__ric_9_2_0b06e8
    - Operacion_incremento_exigencia_sector_publico_no_financiero_incumplimientos_reiterados__ri_2e4cb0
    - Operacion_incremento_exigencia_sector_publico_no_financiero_informacion_en_termino__ric_9__454f0d
    - Operacion_incremento_exigencia_sector_publico_no_financiero_informacion_fuera_de_termino___09d6d1
    - Operacion_incurrir_en_atrasos_hasta_un_ano__cla_6_5_4_2_941d2d
    - Operacion_inferencia_de_ponderador_para_coberturas_de_riesgo_de_mercado__cap_3_1_11_3_50609c
    - Operacion_informacion_de_excesos_fuera_de_termino__ric_9_1_2_1a4e6b
    - Operacion_informacion_de_exposiciones_por_derivados__ric_10_1_4_2_77b144
    - Operacion_informacion_de_incumplimientos_detectados_por_sefyc__ric_9_1_2_e23b5e
    - Operacion_informacion_de_letras_hipotecarias_escriturales__ric_8_1_5_196d3d
    - Operacion_informacion_de_reduccion_de_exigencia__ric_5_1_3_2_dfac4e
    - Operacion_informacion_exposiciones_derivados_sft__ric_10_1_4_3_5c883e
    - Operacion_informacion_exposiciones_fuera_de_balance__ric_10_1_4_3_6d669b
    - Operacion_informacion_sobre_futuros_y_contratos_a_termino__ric_4_5_2_eaee14
    - Operacion_informacion_sobre_opciones_derivados__ric_4_5_3_e317de
    - Operacion_informe_de_titulos_valores_no_fisicamente_en_poder__ric_6_1_2_b9ab42
    - Operacion_informe_ratio_apalancamiento_y_componentes__ric_10_1_1_dc3a53
    - Operacion_ingreso_contravalor_exportacion_divisas__ext_15_2_25a6d0
    - Operacion_ingreso_de_cobros_por_sistema_de_monedas_locales__ext_2_2_3_b672e2
    - Operacion_ingreso_de_cobros_servicios_a_residentes_paraguayos_o_uruguayos__ext_2_2_3_c85cb5
    - Operacion_ingreso_de_divisas_a_traves_de_empresa_procesadora_de_pagos__ext_5_8_2_22cbc5
    - Operacion_ingreso_de_divisas_a_traves_de_procesadora_de_pagos__ext_5_8_2_3_79137e
    - Operacion_ingreso_de_divisas_por_gastos_de_transporte_locales__ext_8_5_1_7bb1f1
    - Operacion_ingreso_en_divisas_del_contravalor__ext_2_3_5a7e76
    - Operacion_ingreso_exportacion_paraguay_uruguay_moneda_destino__ext_7_2_4_b8375e
    - Operacion_ingreso_exportacion_sml_moneda_nacional__ext_7_2_4_08b8c9
    - Operacion_ingreso_y_liquidacion_de_anticipos_prefinanciaciones_y_posfinanciaciones__ext_7__1f0985
    - Operacion_ingreso_y_liquidacion_de_cobros_de_exportaciones__ext_7_1_2_c3a616
    - Operacion_ingreso_y_liquidacion_de_cobros_por_servicios__ext_2_2_1_997433
    - Operacion_ingreso_y_liquidacion_de_contravalor_en_divisas__ext_7_1_1_be3c7b
    - Operacion_ingreso_y_liquidacion_de_divisas__ext_7_8_2_1_e545fc
    - Operacion_ingreso_y_liquidacion_de_divisas_de_financiaciones__ext_7_11_4_b03140
    - Operacion_ingreso_y_liquidacion_de_divisas_exportaciones__ext_7_1_1_d6806c
    - Operacion_ingreso_y_liquidacion_de_divisas_por_empresa_procesadora__ext_8_5_16_70a25b
    - Operacion_ingreso_y_liquidacion_de_divisas_por_exportacion__ext_7_8_1_1_620e2f
    - Operacion_ingreso_y_liquidacion_de_endeudamientos_e_inversion_extranjera__ext_3_5_6_6_e88e22
    - Operacion_ingreso_y_liquidacion_divisas_exportacion_exporta_simple__ext_7_1_1_5_06ce89
    - Operacion_ingreso_y_liquidacion_titulos_deuda_exterior__ext_2_4_ad5d7d
    - Operacion_ingreso_y_remision_de_transferencias_ayuda_familiar__ext_4_2_9_3948cd
    - Operacion_ingresos_y_egresos_futuros_netos_no_devengados_en_moneda_extranjera_con_cobertur_bb6ca1
    - Operacion_inhabilitacion_zfi_para_pagos__ext_11_1_1_9_149e3f
    - Operacion_integracion_de_capital_minimo__cap_1_1_716ce8
    - Operacion_intercambio_de_garantias_basado_en_valor_de_mercado_neto__cap_4_2_1_3_483b02
    - Operacion_intermediacion_de_contratos_de_seguros_generales__pro_2_3_13_90fbd2
    - Operacion_inversiones_en_capital_de_entidades_financieras_supervision_consolidada__cap_8_4_dff72d
    - Operacion_liquidacion_de_cambios_acreditacion_en_cuenta_local__ext_2_9_290c5c
    - Operacion_liquidacion_de_cobros_de_exportaciones_con_dit__ext_10_6_6_1_b27fa8
    - Operacion_liquidacion_de_divisas_del_embarque__ext_7_5_2_3579cf
    - Operacion_liquidacion_de_divisas_en_mercado_de_cambios__ext_10_3_2_4_8db3c7
    - Operacion_liquidacion_de_divisas_en_mercado_de_cambios__ext_9_1_1_ccb2b4
    - Operacion_liquidacion_de_divisas_por_procesadores_de_pagos__ext_7_2_3_4d81a6
    - Operacion_liquidacion_de_financiaciones_en_moneda_extranjera__ext_5_14_05d660
    - Operacion_liquidacion_de_garantia__cap_5_2_2_2_8c3e50
    - Operacion_liquidacion_de_montos_cubiertos_por_compania_de_seguro__ext_7_6_3_1_9a7fe9
    - Operacion_liquidacion_de_nuevo_endeudamiento_financiero__ext_3_6_4_5_9b77cb
    - Operacion_liquidacion_de_operaciones_de_futuros_en_mercados_regulados__ext_3_12_3_6cd4ca
    - Operacion_liquidacion_de_otras_ventas_de_titulos_valores__ext_4_8_3_450852
    - Operacion_liquidacion_en_mercado_de_cambios__ext_2_3_e731f3
    - Operacion_liquidacion_en_mercado_de_cambios_de_fondos_del_exterior__ext_3_16_2_2_c19068
    - Operacion_liquidacion_en_pesos_en_el_pais_titulos_valores__ext_4_3_1_4dec3e
    - Operacion_liquidacion_en_pesos_en_el_pais_titulos_valores_concertadas_en_el_pais__ext_4_3__688837
    - Operacion_liquidacion_simultanea_de_cobros_anticipados_o_prefinanciaciones__ext_10_6_6_2_213d3d
    - Operacion_liquidacion_simultanea_de_financiaciones_en_moneda_extranjera__ext_10_10_2_14_77eb84
    - Operacion_liquidaciones_de_fondos_en_moneda_extranjera_financiacion_a_importadores__ext_7__58e1f8
    - Operacion_llave_negativa_de_adquisiciones_de_participaciones__ric_6_1_2_5fb4c1
    - Operacion_llevar_legajo_de_cada_deudor__cla_3_4_1_07ab9b
    - Operacion_llevar_legajo_del_deudor_en_lugar_de_radicacion__cla_3_4_4_9ae76e
    - Operacion_llevar_legajo_en_medios_magneticos_electronicos_u_otra_tecnologia__cla_3_4_5_092427
    - Operacion_mantener_pendientes_transferencias_sin_informacion_minima__ext_5_5_4_34d713
    - Operacion_mantener_posiciones_en_moneda_extranjera__cap_6_4_b2131f
    - Operacion_mantener_posiciones_en_productos_basicos__cap_6_5_ad92d7
    - Operacion_mantener_registro_de_certificaciones__ext_11_1_1_14_bed3b5
    - Operacion_mantenimiento_de_legajos_en_medios_magneticos_o_electronicos__cla_3_3_672cb5
    - Operacion_mantenimiento_de_ponderador_en_exposicion_sin_cobertura__cap_5_4_83e62d
    - Operacion_mayor_saldo_de_asistencia_crediticia_al_sector_publico__ric_6_1_2_9418f4
    - Operacion_medicion_de_derivados_de_tasas_de_interes__cap_6_2_3_1_b5d830
    - Operacion_modificacion_de_entidad_nominada_para_emision_de_certificaciones__ext_3_17_5_9cd9df
    - Operacion_neteado_de_posicion_derivada_con_subyacente_identico__cap_6_3_2_2_0cbe00
    - Operacion_neteamiento_posiciones_cortas_y_largas__cap_6_5_2_02c7e4
    - Operacion_nominacion_de_entidad_financiera_responsable__ext_3_17_2_a9cf04
    - Operacion_nominacion_de_entidad_financiera_responsable__ext_3_18_2_c9b118
    - Operacion_notificacion_de_ajuste_de_previsiones_por_inspeccion__cla_6_4_3_5b0ed0
    - Operacion_obligaciones_en_moneda_extranjera_entre_residentes__ext_3_6_b7f12f
    - Operacion_obtencion_posicion_abierta_neta_por_moneda__ric_4_3_2_c43946
    - Operacion_ofrecimiento_de_caja_de_ahorros_en_pesos__pro_2_3_1_d67874
    - Operacion_opcion_de_compra_comprada__cap_6_6_2_2_c9b5e8
    - Operacion_opcion_de_venta_comprada__cap_6_6_2_2_c1b11a
    - Operacion_operacion_aduanera_regimen_de_corredores_de_comercio__ext_8_5_17_10_50052d
    - Operacion_operacion_aduanera_regimen_de_franquicia_diplomatica__ext_8_5_17_4_5ba5a5
    - Operacion_operacion_con_opciones_y_subyacentes__cap_6_6_2_305a01
    - Operacion_operacion_cubierta_por_poliza_de_seguro_de_credito__ext_7_6_3_1_b33103
    - Operacion_operacion_de_cambio__ext_5_3_241013
    - Operacion_operacion_de_cambio_en_puertos_y_aeropuertos__ext_5_2_2_f387fc
    - Operacion_operacion_de_cobro_de_exportacion_con_opcion_del_exportador__ext_7_9_4_13101e
    - Operacion_operacion_en_mercado_de_cambios__ext_5_7_1_809eac
    - Operacion_operacion_financiada_deuda_por_importaciones__ext_11_1_1_3_3e8337
    - Operacion_operacion_garantizada_con_activo__cap_5_2_2_4_0a8c8c
    - Operacion_operacion_no_dvp_con_pago_entrega__cap_4_1_2_2dab7c
    - Operacion_operacion_propia_alcanzada_por_obligacion_de_ingreso_y_liquidacion__ext_5_10_4_6b91ce
    - Operacion_operaciones_al_contado_a_liquidar_no_fallidas__cap_2_12_12_251b59
    - Operacion_operaciones_comerciales_brasil_sml__ext_4_2_4512dc
    - Operacion_operaciones_con_ccp_en_jurisdicciones_con_validez_legal_de_liquidacion_neta__cap_003108
    - Operacion_operaciones_con_contrapartes_tratadas_como_sector_privado__cap_2_5_6_0d7be4
    - Operacion_operaciones_con_derivados_no_comprendidas_en_2_12_14__cap_2_12_15_c88cfa
    - Operacion_operaciones_con_derivados_otc_o_negociados__cap_4_2_4_e22c9c
    - Operacion_operaciones_con_derivados_otc_o_regulados_con_liquidacion_diferida__cap_4_2_bee9a9
    - Operacion_operaciones_con_garantia_en_efectivo_o_titulos_publicos_con_aforo__cap_5_3_1_3_439ab1
    - Operacion_operaciones_con_titulos_valores_y_otros_activos__ext_3_16_3_d87fd5
    - Operacion_operaciones_de_cambio__ext_1_3_5a6b91
    - Operacion_operaciones_de_cambio_canje_o_arbitraje_con_bcra_y_entidades__ext_5_10_1_2_882c98
    - Operacion_operaciones_de_cambio_canje_y_o_arbitraje__ext_1_1_a58079
    - Operacion_operaciones_de_cambio_entre_entidades__ext_5_11_039dc2
    - Operacion_operaciones_de_financiacion__pro_2_3_3_f7bb24
    - Operacion_operaciones_de_financiacion_con_titulos_valores__cap_5_3_2_4_c8ca05
    - Operacion_operaciones_de_financiacion_con_titulos_valores_sin_ccp__cap_5_2_2_6_422c8c
    - Operacion_operaciones_de_financiacion_de_proyectos_de_inversion__ext_7_9_2_780272
    - Operacion_operaciones_de_liquidacion_diferida_definicion__cap_4_2_ed3e87
    - Operacion_operaciones_de_pase_participante_esencial__cap_5_3_1_3_cb7451
    - Operacion_operaciones_de_pase_participante_no_esencial__cap_5_3_1_3_c64bc5
    - Operacion_operaciones_de_pase_repo__cap_6_1_3_4_1c3ae2
    - Operacion_operaciones_de_renta_y_capital_rescates_y_ventas_de_titulos__ext_5_7_3_3_3768ba
    - Operacion_operaciones_de_trasbordo__ext_8_5_17_23_49eff0
    - Operacion_operaciones_derivados_con_liquidacion_centralizada_y_margenes_diarios__cap_4_2_1_841350
    - Operacion_operaciones_derivados_financieros_residentes_no_autorizados__ext_3_12_2_43d4fc
    - Operacion_operaciones_derivados_sin_liquidacion_centralizada_con_margenes_diarios__cap_4_2_446e7e
    - Operacion_operaciones_dvp_con_titulos_oro_o_moneda_extranjera__cap_4_1_891c0a
    - Operacion_operaciones_dvp_fallidas__cap_2_12_13_f8252c
    - Operacion_operaciones_financiacion_titulos_valores_acuerdos_marco_neteo__cap_5_3_2_5_2e4e6e
    - Operacion_operaciones_financieras_para_aplicar_cobros_de_exportaciones__ext_7_3_8_c8ab62
    - Operacion_operaciones_no_dvp__cap_2_12_13_c67844
    - Operacion_operaciones_no_dvp_con_titulos_oro_o_moneda_extranjera__cap_4_1_eddbb6
    - Operacion_operaciones_regimen_fomento_inversion_exportaciones__ext_7_10_6_a5d8d9
    - Operacion_ordenes_de_pago_a_cargo_del_bcra__cap_2_12_1_2_bb21d6
    - Operacion_orientacion_a_usuarios_sobre_canalizacion_de_reclamos__pro_4_1_19aa3e
    - Operacion_originacion_de_creditos_por_entidad__cap_2_5_10_1204d4
    - Operacion_otorgamiento_acceso_mercado_cambios_importaciones_temporales_porotos_soja__ext_1_6a9432
    - Operacion_otorgamiento_cumplido_permiso_embarque_provisorio__ext_7_8_2_4_a895bd
    - Operacion_otorgamiento_de_avales_sobre_cheques_de_pago_diferido__cla_2_1_5_2_16ab90
    - Operacion_otorgamiento_de_creditos_a_deudor_en_concurso_preventivo__cla_1_2_2_3e501d
    - Operacion_otorgamiento_de_garantias_localmente__cap_2_2_3_4_c238ac
    - Operacion_otorgamiento_de_garantias_localmente__cla_2_2_4_4_562d10
    - Operacion_otorgamiento_de_prorrogas_mercaderia_siniestrada__ext_10_5_5_1_981758
    - Operacion_otra_retransferencia_de_fondos__ext_5_5_3_7cf857
    - Operacion_otras_ventas_de_titulos_valores_a_partir_de_01_04_24__ext_4_3_2_3_57ce01
    - Operacion_otros_creditos_acordados__cla_2_1_5_3_23dbcb
    - Operacion_pago_a_la_vista_importaciones_bienes__ext_10_10_2_13_03350f
    - Operacion_pago_al_exterior_bienes_importados_alquiler__ext_10_6_1_3d619c
    - Operacion_pago_al_exterior_compras_sin_paso_por_pais__ext_10_9_4_0b5cd4
    - Operacion_pago_al_exterior_de_bienes_importados_obras_infraestructura__ext_10_6_3_646ac4
    - Operacion_pago_al_exterior_de_importaciones_por_solicitud_particular_o_courier__ext_10_3_3_7be50e
    - Operacion_pago_anticipado_de_importacion_con_registro_aduanero_pendiente__ext_10_4_2_6_15b4d8
    - Operacion_pago_anticipado_importacion_bienes_capital__ext_10_10_2_2_6aeb8c
    - Operacion_pago_anticipado_importaciones_bienes_capital__ext_10_10_2_14_412dbd
    - Operacion_pago_capital_e_intereses_compensatorios_deudas_contrapartes__ext_3_14_5_5_797c0a
    - Operacion_pago_capital_e_intereses_deudas_contrapartes_vinculadas__ext_4_8_1_5_80bbf0
    - Operacion_pago_capital_e_intereses_endeudamiento_exterior__ext_3_17_1_5_b35eff
    - Operacion_pago_capital_e_intereses_endeudamiento_financiero__ext_3_18_1_3_1532b1
    - Operacion_pago_capital_e_intereses_endeudamientos_financieros__ext_7_10_1_2_ff2c83
    - Operacion_pago_capital_e_intereses_endeudamientos_financieros__ext_7_9_1_1_f08d8a
    - Operacion_pago_capital_e_intereses_titulos_deuda_con_registro__ext_7_9_1_11_e67e56
    - Operacion_pago_capital_e_intereses_titulos_deuda_con_registro__ext_7_9_1_8_d1a595
    - Operacion_pago_capital_e_intereses_titulos_deuda_con_registro__ext_7_9_1_9_a33aa5
    - Operacion_pago_capital_e_intereses_titulos_deuda_exterior__ext_7_9_1_10_6fa4ee
    - Operacion_pago_contra_presentacion_documentacion_embarque__ext_10_3_1_1_6fcc8d
    - Operacion_pago_de_capital_adeudado_vpu__ext_14_2_1_80b2bb
    - Operacion_pago_de_capital_de_deuda_por_importacion_de_bienes__ext_3_17_1_1_cd19d2
    - Operacion_pago_de_capital_de_deudas_comerciales_por_importacion__ext_10_10_2_8_a71a38
    - Operacion_pago_de_capital_de_deudas_elegibles__ext_4_8_4_5ce201
    - Operacion_pago_de_capital_e_intereses_a_fideicomisos__ext_3_7_a4c90b
    - Operacion_pago_de_capital_e_intereses_de_endeudamientos_financieros__ext_7_9_1_4_6a52b3
    - Operacion_pago_de_capital_e_intereses_de_endeudamientos_financieros__ext_7_9_1_5_0837d0
    - Operacion_pago_de_capital_e_intereses_de_titulos_de_deuda__ext_3_6_1_3_f84054
    - Operacion_pago_de_capital_e_intereses_de_titulos_valores__ext_7_9_1_3_7e8ef1
    - Operacion_pago_de_capital_e_intereses_pagares_con_oferta_publica__ext_14_2_1_4_8cfa60
    - Operacion_pago_de_capital_financiaciones_locales_rigi__ext_14_4_ecd345
    - Operacion_pago_de_deuda_comercial_por_importacion_de_bienes__ext_10_3_1_2_097da9
    - Operacion_pago_de_deudas_con_accionistas_no_residentes_por_utilidades_y_dividendos__ext_4__ab6f78
    - Operacion_pago_de_dividendos_cupones__cap_8_3_2_8_ab0d28
    - Operacion_pago_de_fletes_de_exportacion_con_embarque__ext_13_2_3_e2997c
    - Operacion_pago_de_importacion_con_registro_aduanero_pendiente__ext_11_2_1_7_c32bcc
    - Operacion_pago_de_importacion_de_bien_con_registro_aduanero__ext_10_11_6_de7af6
    - Operacion_pago_de_importaciones_con_ingreso_aduanero_pendiente__ext_10_5_c49b34
    - Operacion_pago_de_importaciones_con_ingreso_aduanero_pendiente__ext_11_2_18e4d3
    - Operacion_pago_de_importaciones_en_moneda_local__ext_4_2_2_a99cf8
    - Operacion_pago_de_intereses_deuda_comercial_importacion__ext_3_17_1_3_b58e24
    - Operacion_pago_de_intereses_deuda_comercial_importacion__ext_3_3_abc8da
    - Operacion_pago_de_intereses_devengados_vpu__ext_14_2_1_066623
    - Operacion_pago_de_intereses_financiaciones_rigi__ext_14_4_51189b
    - Operacion_pago_de_intereses_y_capital_emisiones_de_titulos_de_deuda__ext_14_2_1_2_9fd0f7
    - Operacion_pago_de_pagares_con_oferta_publica_en_moneda_extranjera__ext_3_6_1_4_1056d5
    - Operacion_pago_de_servicio_no_comprendido_en_13_2_1_13_2_5__ext_13_2_6_597757
    - Operacion_pago_de_servicio_por_contraparte_vinculada__ext_13_2_7_ca58db
    - Operacion_pago_de_servicio_s24_de_no_residente_vinculado__ext_13_2_5_f98368
    - Operacion_pago_de_servicios_de_fletes_por_importacion__ext_13_2_4_7ebf0c
    - Operacion_pago_de_servicios_de_no_residentes_codigos_de_concepto__ext_13_2_1_d983bc
    - Operacion_pago_de_servicios_de_no_residentes_prestados_o_devengados_hasta_12_12_23__ext_13_81f1c5
    - Operacion_pago_de_servicios_de_recompra_rescate_de_deudas__ext_13_3_8_fd0bc6
    - Operacion_pago_de_servicios_prestados_con_antelacion__ext_13_3_1a0faa
    - Operacion_pago_de_titulos_de_deuda_con_registro_en_pais__ext_14_2_1_3_4a3d61
    - Operacion_pago_de_titulos_de_deuda_en_moneda_extranjera__ext_3_6_11016b
    - Operacion_pago_de_titulos_de_deuda_y_endeudamientos_financieros_con_el_exterior__ext_3_5_9b8054
    - Operacion_pago_de_utilidades_y_dividendos_a_accionistas_no_residentes__ext_3_17_1_4_cb9fe0
    - Operacion_pago_de_utilidades_y_dividendos_accionistas_no_residentes__ext_14_4_d8fc71
    - Operacion_pago_de_utilidades_y_dividendos_balances_auditados__ext_7_10_1_3_f8f7a8
    - Operacion_pago_de_valores_de_deuda_fiduciaria__ext_3_6_1_5_f717c2
    - Operacion_pago_deuda_comercial_exterior_compra_pactada__ext_10_4_1_3_a50f94
    - Operacion_pago_deudas_comerciales_importaciones_bienes__ext_4_8_1_1_cc6a8c
    - Operacion_pago_deudas_comerciales_importaciones_con_registro_aduanero__ext_3_14_5_1_6f0bf6
    - Operacion_pago_deudas_comerciales_importaciones_servicios__ext_3_14_5_2_ec9bf5
    - Operacion_pago_deudas_comerciales_importaciones_servicios__ext_4_8_1_2_0abf53
    - Operacion_pago_futuro_de_obligaciones_cubiertas_por_garantia__cap_5_2_3_2_727e1e
    - Operacion_pago_importacion_bienes_capital_con_aporte_inversion_extranjera__ext_10_10_2_7_a42194
    - Operacion_pago_importacion_bienes_capital_con_endeudamiento_financiero__ext_10_10_2_7_0d9a26
    - Operacion_pago_importacion_bienes_servicios_conexos_en_pesos__ext_4_2_6_b385ff
    - Operacion_pago_importacion_medicamento_critico__ext_10_10_2_11_a51558
    - Operacion_pago_importaciones_bienes_oficializadas_13_06_24__ext_10_10_2_12_7f8a98
    - Operacion_pago_jubilaciones_y_beneficios_previsionales__ext_4_2_3_ba0cb0
    - Operacion_pago_simultaneo_con_liquidacion_nuevos_aportes_inversion_directa__ext_3_3_3_4_7119b3
    - Operacion_pago_simultaneo_con_liquidacion_nuevos_endeudamientos__ext_3_3_3_4_44d874
    - Operacion_pago_titulos_deuda_ingreso_aduanero_bienes__ext_3_5_1_10_aa6e6e
    - Operacion_pago_unico_del_garante_cubriendo_totalidad_del_importe__cap_5_2_3_2_28ceb3
    - Operacion_pagos_a_la_vista_contra_documentacion_de_embarque__ext_10_4_1_2_83be93
    - Operacion_pagos_al_exterior_de_importaciones_sin_registro_aduanero__ext_10_4_1_1edc7b
    - Operacion_pagos_al_exterior_por_tarjetas_emitidas_localmente__ext_4_1_4_7d01c2
    - Operacion_pagos_anticipados_a_la_vista_y_o_diferidos_de_importaciones_de_bienes__ext_7_11__cf2f7e
    - Operacion_pagos_anticipados_al_exterior_importaciones_sin_registro_aduanero__ext_10_4_1_1_370dac
    - Operacion_pagos_de_fletes_de_importacion_de_bienes_de_capital_por_mercado_de_cambios__ext__3e2e65
    - Operacion_pagos_de_importaciones_de_bienes_de_capital_por_mercado_de_cambios__ext_14_2_1_7_6448c7
    - Operacion_pagos_de_intereses_devengados_impagos_y_capital_pendiente__ext_14_3_1_914e22
    - Operacion_pagos_de_servicios_no_conexos_sml_paraguay_uruguay__ext_4_2_8_8821bc
    - Operacion_pagos_en_el_exterior_con_fondos_de_libre_disponibilidad__ext_11_1_5_2_3936f5
    - Operacion_pagos_en_monedas_distintas_a_facturacion__ext_10_5_7_940d45
    - Operacion_pagos_por_deudas_de_bienes_o_servicios__ext_10_11_7_3_069e59
    - Operacion_pagos_por_importaciones_de_bienes_y_servicios_conexos_a_traves_del_sml__ext_10_1_bc0539
    - Operacion_pagos_por_proyectos_plan_gas__ext_3_17_3_5_735e21
    - Operacion_pagos_por_utilidades_y_dividendos_inversion_directa__ext_3_17_3_5_05ac6a
    - Operacion_pagos_y_movimientos_con_imputacion_al_despacho__ext_11_1_1_2_0af96a
    - Operacion_participacion_en_juegos_de_azar_y_apuestas__ext_4_1_4_1_24ff8a
    - Operacion_participaciones_en_empresas_de_arrendamiento_financiero__cap_8_4_1_14_310dc7
    - Operacion_participaciones_en_empresas_emisoras_de_tarjetas_y_proveedoras_de_credito__cap_8_320b6a
    - Operacion_participaciones_transitorias_en_empresas_para_facilitar_desarrollo__cap_8_4_1_14_3d9d30
    - Operacion_partidas_a_tasa_de_interes_fija__ric_11_1_2_f6a5a1
    - Operacion_partidas_a_tasa_de_interes_variable__ric_11_1_2_b74558
    - Operacion_partidas_de_efectivo_en_tramite_de_percepcion__cap_2_12_1_4_c9c203
    - Operacion_ponderacion_de_exposiciones_con_fondos__cap_3_2_1_1_02dc17
    - Operacion_ponderacion_de_inversion_en_fondo__cap_3_2_1_3_a0ac35
    - Operacion_ponderacion_de_riesgo_de_activos_por_ecai__cap_10_3_1_4_486426
    - Operacion_ponderacion_por_riesgo_de_exposiciones_no_calificadas__cap_10_3_4_c38685
    - Operacion_ponderador_de_riesgo_0_gobiernos_y_bancos_centrales__cap_2_12_2_7_e8d626
    - Operacion_posfinanciacion_de_exportaciones__ext_7_5_2_8a4ae4
    - Operacion_posfinanciacion_de_exportaciones_de_bienes_liquidada__ext_7_3_3_a5ba84
    - Operacion_posicion_abierta_neta_por_moneda__ric_4_4_3_9a9be2
    - Operacion_posicion_abierta_neta_total_negativa_vendida__ric_4_4_3_d5821a
    - Operacion_posicion_abierta_neta_total_positiva_comprada__ric_4_4_3_2b900f
    - Operacion_posicion_comprada_en_subyacente_y_comprada_en_put__cap_6_6_2_1_82851d
    - Operacion_posicion_en_commodities_riesgo_direccional__cap_6_5_3_1_a641f8
    - Operacion_posicion_en_oro__ric_4_4_3_7eb27c
    - Operacion_posicion_neta_a_plazo_en_moneda__cap_6_4_2_1_42d2aa
    - Operacion_posicion_neta_a_plazo_en_moneda_extranjera__ric_4_4_3_7d254d
    - Operacion_posicion_neta_al_contado_en_moneda__cap_6_4_2_1_13bfd3
    - Operacion_posicion_neta_al_contado_en_moneda_extranjera__ric_4_4_3_0b0067
    - Operacion_posicion_vendida_en_subyacente_y_comprada_en_call__cap_6_6_2_1_b233cc
    - Operacion_posiciones_de_titulizacion__cap_2_12_11_1a0c6c
    - Operacion_posiciones_de_titulizacion_en_cartera_de_negociacion__cap_6_2_1_2_fbb2e8
    - Operacion_posiciones_de_titulizacion_fuera_de_balance__cap_3_1_10_fbcc7e
    - Operacion_posiciones_en_cartera_de_negociacion__cap_6_9_2_1e5ac5
    - Operacion_posiciones_en_monedas_residuales__cap_6_2_2_7_6899bb
    - Operacion_posiciones_en_opciones_vendidas_cubiertas__cap_6_6_1_fd00f1
    - Operacion_precancelacion_de_capital_con_liquidacion_de_fondos__ext_3_5_3_1_b5fdf7
    - Operacion_precancelacion_de_capital_e_intereses_con_nuevo_endeudamiento__ext_3_5_3_4_466e1d
    - Operacion_precancelacion_de_capital_e_intereses_de_titulo_de_deuda__ext_3_6_4_5_220f56
    - Operacion_precancelacion_de_capital_e_intereses_por_vpu_rigi__ext_3_6_4_7_51b3dd
    - Operacion_precancelacion_de_capital_e_intereses_vpu_rigi__ext_3_5_3_5_69c1d3
    - Operacion_precancelacion_de_intereses_devengados__ext_3_5_3_1_f75772
    - Operacion_precancelacion_de_intereses_en_canje_de_titulos__ext_3_5_3_3_3d2b7d
    - Operacion_precancelacion_de_intereses_en_canje_de_titulos__ext_3_6_4_3_a8a33d
    - Operacion_precancelacion_simultanea_de_titulo_con_nueva_emision__ext_3_6_4_6_590fad
    - Operacion_precancelacion_total_o_parcial_de_financiaciones__pro_2_3_2_1_70e7d3
    - Operacion_prefinanciacion_de_exportaciones_de_bienes_liquidada__ext_7_3_2_5095aa
    - Operacion_prefinanciacion_de_exportaciones_locales_y_o_del_exterior__ext_7_5_2_43991d
    - Operacion_prefinanciaciones_a_importadores_del_exterior__ext_7_1_4_606279
    - Operacion_prefinanciaciones_de_exportaciones_pendientes_al_31_08_19__ext_9_1_2_5826eb
    - Operacion_prefinanciaciones_locales_o_del_exterior__ext_14_1_4_dda65b
    - Operacion_prefinanciaciones_y_financiaciones_de_exportaciones_otorgadas_o_garantizadas__ex_0f5508
    - Operacion_presentacion_de_constancia_de_publicaciones_de_insolvencia__ext_7_6_2_1_6400e7
    - Operacion_presentacion_de_declaracion_jurada_del_cliente__ext_3_9_3_b95a60
    - Operacion_presentacion_de_ingreso_bruto_del_periodo__ric_5_2_3_af5721
    - Operacion_presentacion_de_reclamo_ante_el_bcra__pro_4_2_1_c3644f
    - Operacion_prestamos_a_instituciones_de_microcredito__cla_5_1_2_3_c6c13a
    - Operacion_prestamos_a_microemprendedores__cla_5_1_2_3_2f472c
    - Operacion_prestamos_a_tasa_fija_con_riesgo_de_cancelacion_anticipada__ric_11_1_2_147253
    - Operacion_prestamos_financieros_con_aplicacion_de_divisas_de_exportaciones__ext_7_3_5_3f6c7c
    - Operacion_prestamos_financieros_de_contrapartes_vinculadas__ext_7_11_1_3_675a61
    - Operacion_prestamos_financieros_del_exterior_importacion_de_bienes_de_capital__ext_14_2_1__761626
    - Operacion_prestamos_financieros_liquidados_en_mercado_de_cambios__ext_7_11_1_4_3c89c9
    - Operacion_prestamos_personales__cap_2_8_3_1_5cdb22
    - Operacion_prestamos_prendarios__cap_2_8_3_1_11713e
    - Operacion_previsionamiento_de_acreencias__cla_3_3_2_3990a9
    - Operacion_previsiones_por_riesgo_de_incobrabilidad_cartera_deudores_normales__cap_8_2_3_3_6c71c4
    - Operacion_previsiones_por_riesgo_de_incobrabilidad_en_situacion_normal__ric_6_1_2_0fc858
    - Operacion_primas_de_emision_instrumentos_pnc__cap_8_2_3_2_672038
    - Operacion_primas_por_opciones_de_compra_y_venta_tomadas__cla_2_2_1_3_3a10c3
    - Operacion_primera_ronda_de_desestimaciones_horizontales__ric_4_4_2_df6bbc
    - Operacion_prorroga_de_plazo_en_operacion_de_importacion__ext_11_2_1_3_8255e4
    - Operacion_provision_de_copias_de_contratos_vigentes__pro_2_3_7_ae7c56
    - Operacion_provision_de_proteccion_crediticia_total_o_proporcional__cap_3_1_13_1_d255b1
    - Operacion_provision_de_respaldo_crediticio_total_a_titulos_valores__cap_3_1_9_354e5c
    - Operacion_publicidad_de_productos_y_o_servicios__pro_2_4_9e8f9d
    - Operacion_realizacion_de_operaciones_cambiarias_en_el_exterior__ext_4_1_4_4_3aa87d
    - Operacion_recategorizacion_de_deudor__cla_6_6_c4b6aa
    - Operacion_recategorizacion_del_deudor__cla_7_3_aa0ac0
    - Operacion_recepcion_de_activo_en_garantia_con_custodia__cap_5_2_2_3_75d0ab
    - Operacion_recepcion_de_comentarios_sugerencias_y_quejas__pro_4_1_7e6db3
    - Operacion_recepcion_de_presentaciones_por_multiples_canales__pro_3_1_6_7ac279
    - Operacion_reclasificacion_a_nivel_inmediato_superior_deudas_refinanciadas__cla_7_2_2_1_580070
    - Operacion_reclasificacion_de_deudor__cla_7_2_1_3a0aa9
    - Operacion_reclasificacion_en_nivel_inmediato_superior_deudores_refinanciados__cla_7_2_4_1d0089
    - Operacion_reclasificacion_en_tratamiento_especial__cla_6_5_2_3_453f6b
    - Operacion_reclasificacion_en_tratamiento_especial_refinanciacion_primera_vez__cla_7_2_2_2_3c5e78
    - Operacion_reclasificacion_inmediata_atrasos_en_pago_de_deuda_refinanciada__cla_7_2_4_63b112
    - Operacion_reclasificacion_inmediata_atrasos_mayores_a_31_dias__cla_7_2_2_1_41d5f2
    - Operacion_reclasificacion_inmediata_nivel_inferior_concurso_preventivo_con_atrasos__cla_7__00bf8e
    - Operacion_recompra_de_instrumentos_propios__cap_8_4_2_3_6a5387
    - Operacion_reconocimiento_cobertura_riesgo_de_credito__cap_10_3_3_3_749992
    - Operacion_reconocimiento_de_instrumentos_de_rpc_de_subsidiaria_en_rpc_de_entidad_financier_70ea75
    - Operacion_reconocimiento_de_participacion_minoritaria_en_co__cap_8_3_5_1_78bcb0
    - Operacion_reconocimiento_de_pnb_de_subsidiaria_en_pnb_de_entidad_financiera__cap_8_3_5_2_59d1b9
    - Operacion_redescuento_de_documentos_en_otras_entidades_financieras__cla_2_1_5_5_969db9
    - Operacion_reduccion_de_exigencia_grupos_a_b_c__ric_5_2_5_55b534
    - Operacion_reduccion_exigencia_entidad_b_calificacion_1_2__ric_5_1_3_3_25a4a2
    - Operacion_reduccion_exigencia_entidad_b_calificacion_1_3__ric_5_1_3_3_6f65e8
    - Operacion_reduccion_exigencia_entidad_c_calificacion_1_2__ric_5_1_3_3_9ccb01
    - Operacion_reduccion_exigencia_entidad_c_calificacion_1_3__ric_5_1_3_3_4faff8
    - Operacion_reduccion_o_transferencia_del_riesgo_de_credito__cap_5_2_1_6_403083
    - Operacion_reembarco_consignado_mediante_subregimenes_aduaneros__ext_8_5_17_24_f44f52
    - Operacion_reembarco_de_bienes_desde_zonas_francas_nacionales__ext_8_5_4_ff32f8
    - Operacion_reestructuracion_de_deudas_sin_desembolsos__ext_3_6_1_6_a44bd2
    - Operacion_reexportacion_mercaderia_raf_no_utilizada__ext_8_5_5_76f96b
    - Operacion_refinanciacion_de_capital_e_intereses__cla_6_5_4_5_1cbeba
    - Operacion_refinanciacion_de_deuda_comercial_por_importacion__ext_10_2_4_9_470a8d
    - Operacion_regimen_de_envios_de_asistencia_y_salvamento__ext_8_5_17_9_13246a
    - Operacion_regimen_de_equipaje_operacion_aduanera__ext_8_5_17_7_664ea7
    - Operacion_regimen_de_exportacion_para_compensar_envios_con_deficiencias__ext_8_5_17_8_ff971f
    - Operacion_regimen_de_material_promocional__ext_8_5_17_6_991045
    - Operacion_regimen_de_muestras_operacion_aduanera__ext_8_5_17_5_48d47b
    - Operacion_regimen_de_pacotilla__ext_8_5_17_3_fcfc92
    - Operacion_regimen_de_removido_operacion_aduanera__ext_8_5_17_13_3269ad
    - Operacion_registro_cambiario_por_operatoria_de_creditos_y_depositos__ext_5_10_3_a6d9db
    - Operacion_registro_de_aportes_a_valor_de_mercado__cap_8_6_b7576a
    - Operacion_registro_de_aportes_punto_8_6_3_a_valor_de_mercado_o_precio_de_autoridad__cap_8__bb5f07
    - Operacion_registro_de_boletos_en_fecha_de_origen__ext_7_11_3_3_e94287
    - Operacion_registro_de_circunstancias_que_reduzcan_monto_pendiente__ext_9_6_8b69d4
    - Operacion_registro_de_denuncias_ante_instancias_judiciales_administrativas__pro_3_1_5_78e337
    - Operacion_registro_de_depositos_y_obligaciones_a_valor_contable__cap_8_6_31fc93
    - Operacion_registro_de_ingreso_aduanero_de_bienes__ext_10_2_1_e8b73a
    - Operacion_registro_de_liquidaciones_de_divisas_devoluciones__ext_11_2_1_4_814bde
    - Operacion_registro_de_montos_de_beneficios_decreto_277_22__ext_3_17_3_e93845
    - Operacion_registro_de_operacion_con_cliente_ante_bcra__ext_5_7_3_0d1f24
    - Operacion_registro_de_operacion_con_identificador_cuit_o_cuil__ext_5_7_3_ed8d7f
    - Operacion_registro_de_operacion_en_sistema_online_bcra__ext_14_4_2_5c90f7
    - Operacion_registro_de_operacion_en_sistema_online_bcra__ext_3_8_3_ba4c1f
    - Operacion_registro_de_operaciones_en_rioc__ext_7_10_2_5_e494b2
    - Operacion_registro_de_operaciones_propias_en_fecha_de_efecto__ext_5_10_2_f59e26
    - Operacion_registro_de_permiso_de_embarque_como_incumplido__ext_7_6_05dbf0
    - Operacion_registro_de_reintegros_de_importes_rri__pro_3_1_4_c88408
    - Operacion_registro_en_sepaimpo_de_baja_de_valor__ext_11_1_1_13_b19ec8
    - Operacion_registro_operacion_con_cliente_codigo_cnv__ext_5_7_3_2_d8c98b
    - Operacion_regularizacion_de_pago_con_registro_aduanero_pendiente__ext_10_5_6_60628d
    - Operacion_reimportacion_de_mercaderia_rechazada__ext_8_5_6_e8f187
    - Operacion_relevamiento_de_activos_y_pasivos_externos__ext_1_9_62ba9d
    - Operacion_repago_de_financiaciones_con_garantia_hipotecaria__cap_2_9_2_6_3924bb
    - Operacion_repatriacion_aportes_inversion_directa_vpu_rigi__ext_14_2_3_d2f941
    - Operacion_repatriacion_aportes_inversion_directa_vpu_rigi__ext_3_13_1_11_3be6c9
    - Operacion_repatriacion_de_aportes_de_inversion_directa__ext_3_13_2_9484ed
    - Operacion_repatriacion_de_aportes_inversion_directa_vpu_rigi__ext_7_9_1_7_361c8e
    - Operacion_repatriacion_de_inversiones_de_no_residentes__ext_3_13_1_60e07b
    - Operacion_repatriacion_de_inversiones_directas_no_residentes__ext_7_10_1_4_48c957
    - Operacion_repatriacion_de_inversiones_directas_no_residentes__ext_7_9_1_2_ab0610
    - Operacion_repatriacion_de_servicios_de_capital_rentas_y_ventas_de_inversiones_de_portafoli_be2a24
    - Operacion_repatriacion_inversion_directa_no_residentes__ext_3_13_1_7_fa6676
    - Operacion_repatriacion_inversion_directa_no_residentes__ext_3_13_1_8_c88e8f
    - Operacion_repatriacion_inversion_directa_no_residentes__ext_3_13_1_9_d4e204
    - Operacion_repatriacion_inversion_directa_no_residentes__ext_3_17_1_6_22c487
    - Operacion_repatriacion_inversion_directa_reduccion_capital_devolucion_aportes__ext_3_13_1_bde0a6
    - Operacion_repatriacion_inversion_portafolio_no_residentes__ext_3_13_1_13_1ee014
    - Operacion_repatriacion_inversiones_no_residentes__ext_3_13_1_c29027
    - Operacion_repatriacion_inversiones_portafolio_no_residentes__ext_4_8_1_4_2d4a58
    - Operacion_repatriaciones_de_aportes_de_inversion_directa_de_accionistas_no_residentes__ext_1dd66e
    - Operacion_reporte_de_cotizaciones_comprador_y_vendedor_dolar_y_euro__ext_5_2_1_2f24f3
    - Operacion_reporte_de_incumplimientos_de_activos_inmovilizados__ric_9_2_2_019d79
    - Operacion_reporte_de_incumplimientos_de_derivados_sobre_commodities__ric_9_2_2_629d71
    - Operacion_reporte_de_incumplimientos_de_financiamiento_sector_publico__ric_9_2_2_059126
    - Operacion_reporte_de_incumplimientos_de_graduacion_del_credito__ric_9_2_2_23c854
    - Operacion_reporte_de_incumplimientos_de_grandes_exposiciones__ric_9_2_2_eefd8f
    - Operacion_reporte_de_posicion_comprada_por_banda_de_duracion__ric_4_4_2_86bd62
    - Operacion_reporte_de_posicion_ponderada_neta_comprada_o_vendida__ric_4_4_2_c1ce50
    - Operacion_reporte_de_posicion_vendida_por_banda_de_duracion__ric_4_4_2_a3ecdf
    - Operacion_reporte_en_sepaimpo_de_circunstancias_que_modifiquen_monto_pendiente__ext_11_2_1_a92902
    - Operacion_reporte_sepaimpo_afectaciones_despachos_importacion__ext_11_2_1_2_ed4359
    - Operacion_reporte_zfe_con_transferencia_aduanera__ext_11_1_1_9_06edd0
    - Operacion_requerimiento_de_quiebra__cla_6_5_4_7_687c3c
    - Operacion_rescate_de_posiciones_de_titulizacion__cap_3_1_4_9195a8
    - Operacion_rescision_de_relaciones_contractuales__pro_2_7_2_efd4d8
    - Operacion_respuesta_a_consultas_sobre_normativa_e_informacion__pro_4_1_7fb819
    - Operacion_retiros_de_efectivo_en_el_exterior_con_tarjeta_de_debito__ext_4_1_1_7083e9
    - Operacion_retransferencias_a_corresponsales__ext_5_5_3_516cb5
    - Operacion_revision_de_cartera_comercial__cla_6_3_3_cf7276
    - Operacion_revision_de_clientes_semestral_cartera_comercial__cla_6_3_2_fc45a0
    - Operacion_revision_exhaustiva_del_esquema_de_medicion_de_riesgo_de_mercado__cap_6_12_6c4298
    - Operacion_revocacion_de_aceptacion_del_producto_o_servicio__pro_2_7_1_959bb0
    - Operacion_saldo_a_favor_por_impuesto_a_ganancia_minima_presunta__ric_6_1_2_8438e0
    - Operacion_saldo_a_favor_por_impuesto_ganancia_minima_presunta__cap_8_4_1_2_ef551d
    - Operacion_saldos_a_favor_por_activos_impuestos_diferidos__cap_8_4_1_2_9a7e62
    - Operacion_saldos_en_cuentas_de_corresponsalia_bancos_del_exterior__cap_8_4_1_3_81cd6d
    - Operacion_seguimiento_activo_de_posiciones__cap_6_9_2_6_676d05
    - Operacion_seguimiento_de_negociaciones_de_divisas_por_exportaciones__ext_7_1_1_c73d6a
    - Operacion_seguimiento_de_pagos_de_importaciones_con_registro_pendiente__ext_10_4_1_b3646b
    - Operacion_seguimiento_de_permisos_de_embarques_con_cobros_en_exterior__ext_7_9_3_2_108d8f
    - Operacion_seguimiento_ejecucion_proyecto_y_financiacion__ext_7_9_3_6_f4691b
    - Operacion_segunda_ronda_de_desestimaciones_horizontales__ric_4_4_2_435668
    - Operacion_seleccion_de_calificaciones_multiples_ecai__cap_10_3_2_3_cf14e9
    - Operacion_seleccion_de_entidad_nominada_para_primera_exportacion__ext_3_18_4_32d0c7
    - Operacion_seleccion_entidad_por_primer_ingreso__ext_2_6_3_8ed416
    - Operacion_seleccion_inicial_de_entidad_nominada__ext_3_18_4_5a4d70
    - Operacion_separacion_de_posiciones_superpuestas__cap_3_1_9_baabfa
    - Operacion_servicios_de_banca_por_internet_y_banca_movil_accesibles__pro_2_2_2_146d4e
    - Operacion_situacion_financiera_iliquida_con_alto_endeudamiento__cla_6_5_4_1_940e44
    - Operacion_solicitud_de_autorizacion_de_aportes_de_capital__cap_8_7_28640c
    - Operacion_solicitud_de_concurso_preventivo__cla_6_5_4_7_e9ffe3
    - Operacion_subdivision_de_proteccion_crediticia_por_plazo_de_vencimiento__cap_5_2_1_5_bd94d5
    - Operacion_subordinacion_a_depositantes_y_acreedores__cap_8_3_2_2_52ffa1
    - Operacion_subrogacion_de_derechos_de_cobro__ext_7_6_3_1_72db14
    - Operacion_suma_de_creditos_para_consumo_o_vivienda_a_cartera_comercial_para_encuadramiento_1e1730
    - Operacion_supervision_consolidada_de_sucursales_subsidiarias__cap_2_2_3_1_2cc77c
    - Operacion_suscripcion_bopreal_por_deuda_pendiente__ext_13_1_4_cb2b7a
    - Operacion_suscripcion_bopreal_por_deudores__ext_4_7_9c5272
    - Operacion_suscripcion_bopreal_por_importadores__ext_4_4_39991d
    - Operacion_suscripcion_bopreal_por_importadores_de_servicios__ext_4_5_9d04d1
    - Operacion_suscripcion_bopreal_por_utilidades_y_dividendos__ext_4_6_1_f1b06c
    - Operacion_suscripcion_bopreal_por_utilidades_y_dividendos__ext_4_6_2_1_ff1ee1
    - Operacion_suscripcion_de_bonos_bopreal__ext_4_4_b998b5
    - Operacion_suscripcion_de_bonos_bopreal__ext_4_6_2_3_7576c6
    - Operacion_suscripcion_de_bonos_bopreal_por_deudor__ext_4_7_4_3_81d900
    - Operacion_suscripcion_e_integracion_de_instrumentos__cap_8_3_3_1_f92624
    - Operacion_suspension_de_operaciones_en_cambios__ext_5_15_d3bbf3
    - Operacion_suspension_de_operaciones_en_divisas__ext_5_15_d483b7
    - Operacion_sustitucion_de_ponderadores_garantias_personales__cap_5_4_771260
    - Operacion_swap_de_moneda_imputacion_a_escala_de_vencimientos__cap_6_2_3_4_1ff51c
    - Operacion_swap_de_tasa_de_interes__ric_4_5_1_332d9d
    - Operacion_swap_de_tasas_de_interes_posiciones_nocionales__cap_6_2_3_4_42fcd2
    - Operacion_swap_tasa_de_interes_contra_indice_bursatil_componente_tasa_e_imputacion_acciona_b06f74
    - Operacion_swap_tasa_variable_recibida_tasa_fija_pagada_posiciones_comprada_y_vendida__cap__d0f370
    - Operacion_tenencia_de_acciones_cuotas_o_partes_en_sociedades_de_inversion__cap_2_11_3_1_b09fee
    - Operacion_tenencia_de_activos_sujetos_a_capital_minimo_por_riesgo_de_mercado__cap_6_11_48a3d9
    - Operacion_tenencia_de_efectivo_en_caja__cap_2_12_1_1_a46f14
    - Operacion_tenencia_de_instrumentos_derivados_vinculados_a_acciones__cap_2_11_3_1_6a1d34
    - Operacion_tenencia_de_oro_amonedado_o_en_barras_de_buena_entrega__cap_2_12_1_3_134e48
    - Operacion_tenencia_de_posiciones_de_titulizacion_por_originante__cap_3_1_12_ea115e
    - Operacion_tenencia_de_titulos_de_credito_no_en_poder_de_la_entidad__cap_8_4_1_4_c2a2b7
    - Operacion_tenencia_de_titulos_subordinados_de_otras_entidades_financieras__ric_6_1_2_380237
    - Operacion_tercera_ronda_de_desestimaciones_horizontales__ric_4_4_2_20968e
    - Operacion_titulizacion__cap_3_1_2_1_ebb6d4
    - Operacion_titulizacion_con_opcion_de_exclusion_incompleta__cap_3_1_4_53aace
    - Operacion_titulizacion_sintetica_con_opcion_de_exclusion_incompleta__cap_3_1_4_38d613
    - Operacion_titulizacion_tradicional_con_opcion_de_exclusion_incompleta__cap_3_1_4_429029
    - Operacion_titulos_de_deuda_en_moneda_extranjera_con_registro_publico__ext_9_1_6_fb6cba
    - Operacion_titulos_de_deuda_replicando_accion__cap_2_11_3_5_4c6628
    - Operacion_titulos_de_gobiernos_extranjeros_con_calificacion_inferior__ric_6_1_2_bea198
    - Operacion_toma_de_registro_de_montos_de_beneficios__ext_3_17_3_b12127
    - Operacion_tramitacion_de_denuncias_por_afectacion_de_intereses_generales__pro_4_3_f0c7e7
    - Operacion_transferencia_al_exterior_de_agentes_locales_por_recaudaciones__ext_13_2_6_a76401
    - Operacion_transferencia_de_bonos_bopreal_a_depositarios_en_el_exterior__ext_4_8_2_f00f7d
    - Operacion_transferencia_de_divisas_al_exterior_centrales_de_deposito__ext_3_14_2_4b395c
    - Operacion_transferencia_de_divisas_boleto_global_diario__ext_5_8_2_2_f62bb0
    - Operacion_transferencia_de_fondos_a_cuentas_de_inversion_en_administradores_del_exterior___e361a2
    - Operacion_transferencia_de_fondos_a_cuentas_en_psp__ext_4_1_4_2_fdd6b0
    - Operacion_transferencia_de_fondos_compraventa_titulos_valores__ext_4_3_2_1_9902c1
    - Operacion_transferencia_de_fondos_con_exterior__ext_5_5_1_639e00
    - Operacion_transferencia_de_titulos_valores_a_depositarios_en_el_exterior__ext_4_8_2_e7e467
    - Operacion_transferencia_directa_desde_cuenta_operativa_movimiento_de_fondos__ext_2_9_da4878
    - Operacion_transferencia_divisas_exterior_pago_importaciones__ext_3_14_3_c0f2fd
    - Operacion_transferencia_en_misma_moneda_de_cuenta__ext_3_14_c46855
    - Operacion_transferencias_a_cuentas_bancarias_exterior_personas_humanas__ext_3_13_1_6_ca5a7d
    - Operacion_transferencias_jubilaciones_y_pensiones__ext_5_8_1_85bd75
    - Operacion_transferencias_por_representaciones_de_tribunales_autoridades_u_oficinas__ext_3__07b03b
    - Operacion_transmision_de_certificaciones_entre_entidades__ext_11_1_3_078632
    - Operacion_transmision_de_certificaciones_por_medio_seguro__ext_11_1_4_fe6949
    - Operacion_tratamiento_de_acciones_preferidas_convertibles__cap_6_2_180b1d
    - Operacion_tratamiento_de_garantias_activos_constituidos_en_garantia_de_operaciones__cap_4__d3ca7a
    - Operacion_tratamiento_de_margen_inicial_como_exposicion_a_fondo_de_garantia__cap_4_3_1_4_d03dc5
    - Operacion_tratamiento_de_posiciones_en_fondos__cap_3_2_64c644
    - Operacion_tratamiento_de_titulos_bopreal_recuperados__ext_4_8_6_3_ab9ad0
    - Operacion_tratamiento_de_titulos_en_operaciones_de_pase_pasivo__cap_6_2_b18fec
    - Operacion_tratamiento_de_transparencia_para_posicion_de_maxima_preferencia__cap_3_1_6_0d3a18
    - Operacion_uso_de_certificacion_de_acceso_al_mercado_de_cambios__ext_11_1_6_2_029a56
    - Operacion_utilizacion_de_calificacion_para_determinar_ponderador__cap_10_3_2_1_4d5b23
    - Operacion_utilizacion_de_calificaciones_ecai_para_ponderador_de_riesgo__cap_10_1_ba376a
    - Operacion_utilizacion_de_evaluaciones_externas_para_ponderacion_de_riesgo__cap_10_3_5_b06022
    - Operacion_valor_absoluto_de_posicion_ponderada_neta__cap_6_2_2_1_95051d
    - Operacion_valoracion_de_futuros_sobre_indice_de_bonos_corporativos__cap_6_2_3_3_bce60f
    - Operacion_valuacion_a_mercado_de_posiciones__cap_6_10_1_2_6ef249
    - Operacion_valuacion_a_modelo_de_posiciones__cap_6_10_1_2_b547e3
    - Operacion_valuacion_de_posiciones_a_modelo__cap_6_9_2_4_1306ef
    - Operacion_valuacion_de_posiciones_a_termino_en_moneda_extranjera_y_oro__cap_6_4_2_4_fd1511
    - Operacion_valuacion_de_productos_complejos__cap_6_10_2_3_2acdca
    - Operacion_valuacion_prudente_de_posiciones_a_valor_razonable__cap_6_10_9a3a4e
    - Operacion_vencimientos_de_capital_acumulados__ext_7_11_2_6_1d67de
    - Operacion_venta_con_obligacion_de_recompra_de_bopreal__ext_4_8_6_dd0490
    - Operacion_venta_de_bonos_bopreal_con_liquidacion_en_moneda_extranjera__ext_4_8_2_d682b7
    - Operacion_venta_de_bonos_bopreal_contra_cable__ext_4_3_2_3_f31d38
    - Operacion_venta_de_divisas_cancelacion_de_linea_de_credito__ext_10_7_2_4f2218
    - Operacion_venta_de_divisas_con_debito_en_cuentas__ext_10_3_2_2_46dbdd
    - Operacion_venta_de_divisas_con_debito_en_cuentas__ext_10_4_2_3_bd6009
    - Operacion_venta_de_operaciones_de_titulizacion__cap_8_4_1_17_19d89e
    - Operacion_venta_de_titulos_bopreal_con_obligacion_de_recompra__ext_4_8_6_53c9c1
    - Operacion_venta_de_titulos_en_mercado_secundario__ext_5_9_5_83dd05
    - Operacion_venta_de_titulos_valores_con_liquidacion_en_moneda_extranjera_en_el_exterior__ex_4d5e74
    - Operacion_venta_de_titulos_valores_contra_cable_sobre_cuenta_de_terceros__ext_4_8_3_cc277e
    - Operacion_venta_interna_de_bienes_importados__ext_10_6_4_8b30ee
    - Operacion_venta_o_cesion_de_cartera_con_responsabilidad__cap_8_4_1_17_d962a0
    - Operacion_verificacion_cumplimiento_plazos_importador__ext_11_2_1_1_644b31
    - Operacion_verificacion_de_cliente_en_listado_de_cuits_inconsistentes__ext_3_16_4_3800c7
    - Operacion_verificacion_de_documentacion_aduanera__ext_11_1_1_1_fbc997
    - Operacion_verificacion_de_requisitos_en_importaciones_encuadradas__ext_4_4_d82180
    - Operacion_verificacion_independiente_de_precios__cap_6_10_1_2_3cea78
Potestad: 100 sin aplica_a
    - Potestad_acceso_a_niveles_superiores_de_clasificacion__el_deudor_puede_acceder_a_niveles__0c0436
    - Potestad_acceso_admisible_para_pago_de_servicios_con_antelacion__se_autoriza_el_acceso_pa_f03d25
    - Potestad_acceso_al_mercado_de_cambios_con_conformidad_previa_del_bcra__el_acceso_al_merca_dc82ac
    - Potestad_acceso_mercado_cambios_mediante_canje_arbitraje_bopreal__los_clientes_tienen_la__855fb4
    - Potestad_acceso_mercado_cambios_para_pago_gastos_emision_y_servicios__la_entidad_podra_da_22952a
    - Potestad_acceso_mercado_cambios_para_pago_prima_recompra_rescate__la_entidad_podra_dar_ac_8dc333
    - Potestad_adicion_de_llave_negativa_a_rpc__facultad_de_adicionar_el_importe_de_la_llave_de_9f1762
    - Potestad_admision_acumulacion_cobros_en_cuentas_exteriores__se_admite_que_los_cobros_de_e_dee04e
    - Potestad_admision_aplicacion_divisas_a_operaciones__se_admite_la_aplicacion_de_las_divisa_cf6dfc
    - Potestad_admision_de_aplicacion_de_cobros_de_exportaciones__se_admitira_la_aplicacion_de__98294e
    - Potestad_admision_de_aplicacion_de_divisas_de_cobros__se_admite_la_aplicacion_de_divisas__4e6fd2
    - Potestad_admision_de_pago_desde_fecha_estimada_de_embarque__se_admitira_que_el_pago_garan_ba3ff0
    - Potestad_admision_de_repatriacion_de_aportes__la_repatriacion_de_aportes_de_inversion_dir_3805b6
    - Potestad_aforo_de_cero_para_operaciones_de_financiacion__las_operaciones_de_financiacion__50be54
    - Potestad_aplicacion_de_tratamiento_de_transparencia_para_maxima_preferencia__las_entidade_8ca2de
    - Potestad_aplicacion_de_tratamiento_segun_punto_4_3_3_o_4_3_4__se_aplicara_el_tratamiento__6cdf69
    - Potestad_aplicacion_del_plazo_del_pais_de_destino__es_aplicable_el_plazo_vigente_en_el_pa_0ba79b
    - Potestad_aplicar_limites_ponderador_maxima_preferencia__facultad_de_aplicar_limites_para__7a1d8a
    - Potestad_asignacion_de_ponderador_de_riesgo_especifico_para_partidas_12100000_y_1222000_c_d523ec
    - Potestad_autorizacion_previa_de_restitucion_de_capital__la_sefyc_tiene_la_facultad_de_aut_987f43
    - Potestad_autorizacion_previa_del_bcra_acceso_anticipado_al_mercado__el_bcra_puede_otorgar_c2ef1a
    - Potestad_autorizacion_previa_para_aportes_en_instrumentos_de_regulacion_monetaria__la_sef_82afd0
    - Potestad_bcra_conformidad_con_conclusion_sobre_exigibilidad_legal_del_neteo__el_bcra_debe_8cbe3d
    - Potestad_bcra_determinar_qccp_en_jurisdiccion_sin_principios__el_bcra_tiene_la_facultad_d_e7d13c
    - Potestad_clasificacion_en_situacion_normal_si_se_cumplen_condiciones__facultad_de_clasifi_cb98e3
    - Potestad_compensacion_de_posiciones_contrarias_mercados_diferentes__facultad_de_compensar_20ce7e
    - Potestad_computar_liquidaciones_en_permiso_provisorio_o_definitivo__las_entidades_autoriz_63e387
    - Potestad_confeccionar_unico_boleto_para_multiples_oficializaciones__facultad_de_confeccio_274a89
    - Potestad_conformidad_del_bcra_para_regularizacion_de_operacion__el_bcra_puede_otorgar_con_27678c
    - Potestad_conformidad_previa_del_bcra_pago_de_oficializaciones__el_bcra_tiene_la_facultad__74077a
    - Potestad_conformidad_previa_del_bcra_pagos_no_encuadrados__el_bcra_tiene_la_facultad_de_o_971e87
    - Potestad_cr_no_se_ve_afectado_por_garantias_en_exceso__el_cr_no_se_ve_afectado_cuando_la__479369
    - Potestad_decision_direccion_general_de_aduanas_procedencia_exencion__la_direccion_general_b695cb
    - Potestad_decision_direccion_general_de_aduanas_sobre_reexportacion__la_direccion_general__c432f8
    - Potestad_derecho_a_efectuar_seguimiento_de_presentacion__el_usuario_de_servicios_financie_7fed97
    - Potestad_designacion_de_veedor_por_sefyc__la_superintendencia_de_entidades_financieras_y__e748df
    - Potestad_disponibilidad_de_datos_en_base_sefyc__los_datos_de_posiciones_e_instrumentos_de_fb2d96
    - Potestad_emision_de_certificaciones_de_aplicacion_de_divisas__las_entidades_autorizadas_p_2b3f22
    - Potestad_emision_de_certificaciones_por_entidad_nominada__la_entidad_nominada_esta_facult_bdaa9d
    - Potestad_encomendar_tarea_de_clasificacion__la_tarea_de_clasificacion_podra_ser_encomenda_318b56
    - Potestad_establecer_condiciones_y_plazos_bcra__el_bcra_queda_facultado_para_establecer_la_fd0b4d
    - Potestad_establecer_reglamentaciones_elusion_bcra__el_bcra_queda_facultado_para_establece_5c42d1
    - Potestad_establecer_supuestos_autorizacion_previa_bcra__el_bcra_conforme_a_su_carta_organ_f604ff
    - Potestad_exclusion_de_tenencias_de_titulos_valores_para_colocacion__facultad_de_excluir_l_34bbe4
    - Potestad_extension_del_plazo_de_liquidacion_de_permiso_de_embarque__la_entidad_encargada__8266ae
    - Potestad_facilidad_de_liquidez_como_posicion_de_maxima_preferencia__la_facilidad_de_liqui_9a240d
    - Potestad_facultad_computar_fletes_condiciones_verificadas__las_entidades_podran_computar__599c54
    - Potestad_facultad_de_acceso_al_mercado_de_cambios__el_cliente_que_cuente_con_una_certific_ce3e5b
    - Potestad_facultad_de_aceptar_declaracion_jurada_cuando_activos_externos_liquidos_superan__df94d9
    - Potestad_facultad_de_calcular_facilidad_de_liquidez_expandida__la_entidad_queda_facultada_f6e0f7
    - Potestad_facultad_de_considerar_cumplido_ingreso_por_gastos_de_transferencia__se_podra_co_8d69cd
    - Potestad_facultad_de_considerar_importacion_como_bienes_de_capital__facultad_de_la_entida_1766b9
    - Potestad_facultad_de_consultar_cotizaciones_en_pagina_bcra__facultad_de_consultar_en_la_p_95a1fc
    - Potestad_facultad_de_consultar_tipos_de_cambio_minoristas_de_referencia__facultad_de_cons_3655bc
    - Potestad_facultad_de_encomendar_revision_a_auditoria_interna__la_revision_de_clasificacio_19eb6f
    - Potestad_facultad_de_excluir_posiciones_y_derivados__facultad_de_excluir_posiciones_opues_cd1892
    - Potestad_facultad_de_requerir_legajos_superintendencia__con_respecto_a_los_creditos_que_s_17bafd
    - Potestad_facultad_exportador_modificar_entidad_nominada__el_exportador_puede_modificar_la_0cdf48
    - Potestad_facultad_sefyc_ajustes_valuacion_posiciones_menos_liquidas__la_sefyc_tiene_facul_ccd652
    - Potestad_garantias_opcionales_financiacion_comercial__las_partes_pueden_acordar_que_la_fi_7ab413
    - Potestad_habilitacion_aplicacion_cobros_exportaciones_condicionada__la_aplicacion_de_cobr_4afebe
    - Potestad_habilitacion_aplicacion_cobros_exportaciones_y_servicios__la_aplicacion_de_cobro_3cfedd
    - Potestad_habilitacion_de_cancelacion_de_servicios_de_endeudamientos__se_habilita_a_los_en_f1d639
    - Potestad_habilitacion_para_cancelar_servicios_titulos_valores__las_emisiones_de_titulos_v_46880a
    - Potestad_habilitacion_para_emitir_nuevas_certificaciones__la_nueva_entidad_queda_habilita_220980
    - Potestad_importador_puede_modificar_entidad_nominada__el_importador_puede_posteriormente__b898d5
    - Potestad_importador_puede_seleccionar_entidad_posteriormente__si_el_importador_no_ha_nomi_253979
    - Potestad_imputar_diferencia_fob_permiso_provisorio_definitivo__cuando_el_valor_fob_del_pe_4206d6
    - Potestad_inclusion_de_ajustes_niif_no_asignados_en_partida_12700000__cuando_no_resulte_fa_647c45
    - Potestad_liberacion_de_pagos_a_cargo_de_arca__la_certificacion_de_cumplido_dara_lugar_a_l_0c5d6e
    - Potestad_modificacion_de_entidad_responsable_por_exportador__el_exportador_puede_modifica_0ff47a
    - Potestad_opcion_de_encomendar_clasificacion_a_profesionales_externos__los_sujetos_obligad_024eee
    - Potestad_permanencia_de_fondos_en_cuentas_de_entidades_financieras_del_exterior__se_autor_951505
    - Potestad_permanencia_de_fondos_en_cuentas_del_exterior__los_fondos_pueden_permanecer_en_c_5831ae
    - Potestad_permiso_descalce_monedas_sin_tratamiento__se_admite_el_descalce_de_monedas_entre_9a8209
    - Potestad_potestad_de_decidir_autorizacion_circunstancial_de_sobregiros__el_personal_con_a_5e68f3
    - Potestad_potestad_de_sefyc_para_exigir_acciones_correctivas_o_suspender_tratamiento_stc___5fd273
    - Potestad_recategorizacion_directa_a_niveles_superiores_aplicacion_de_metodologia__faculta_c711e6
    - Potestad_reclasificacion_a_nivel_superior_con_pago_del_15__la_entidad_podra_reclasificar__bde403
    - Potestad_reclasificacion_a_niveles_superiores_si_se_cumplen_condiciones__la_entidad_podra_2b469f
    - Potestad_reclasificacion_en_nivel_inmediato_superior_deudor_refinanciado__facultad_de_rec_d7d5a2
    - Potestad_reclasificacion_en_niveles_superiores_al_levantarse_pedido_de_quiebra__el_deudor_46a69b
    - Potestad_reclasificacion_en_niveles_superiores_levantamiento_de_quiebra__el_deudor_podra__5b8f51
    - Potestad_reclasificacion_inicial_en_acuerdos_superiores_a_2_5_veces__la_entidad_podra_rea_c78a90
    - Potestad_reconocer_activos_dados_en_garantia_por_spe__se_podran_reconocer_los_activos_dad_db01ee
    - Potestad_reconocer_proteccion_crediticia_en_titulizacion__se_podra_reconocer_la_proteccio_959e87
    - Potestad_reconocimiento_garantia_tramo_ccp_miembro_y_miembro_cliente__miembro_compensador_56d2e9
    - Potestad_reconocimiento_potestativo_de_participacion_minoritaria__la_entidad_financiera_t_d23373
    - Potestad_recurso_a_informacion_divulgada_enfoque_mba__las_fuentes_de_informacion_no_se_li_882e80
    - Potestad_signo_negativo_en_partida_12700000__la_partida_12700000_admite_signo_negativo__r_f7d2f5
    - Potestad_solicitud_ampliacion_plazo_liquidacion_divisas__el_exportador_podra_solicitar_qu_d29527
    - Potestad_solicitud_de_ampliacion_de_plazo_para_liquidacion__el_exportador_podra_solicitar_0b73a1
    - Potestad_solicitud_de_ampliacion_de_plazo_para_liquidacion_de_divisas__el_exportador_podr_a654d4
    - Potestad_supervision_de_actuacion_de_sujetos_obligados__el_bcra_supervisara_la_actuacion__569de9
    - Potestad_suscripcion_bopreal_hasta_monto_deuda_pendiente__los_clientes_pueden_suscribir_b_2a6a5b
    - Potestad_sustituir_posiciones_no_significativas_por_limites_internos__a_los_efectos_de_la_ef87b1
    - Potestad_tratamiento_exposicion_cliente_condiciones_de_proteccion_cumplidas__exposicion_d_8fc89e
    - Potestad_usuario_puede_informar_al_bcra_por_medios_habilitados__el_usuario_de_servicios_f_59b693
    - Potestad_utilizacion_de_correo_electronico_para_notificacion__se_admite_la_utilizacion_de_c2c4b3
    - Potestad_verificacion_de_saldos_y_sistemas_de_gestion_de_riesgo__la_sefyc_tiene_la_facult_141e3f
Restriccion: 434 sin aplica_a
    - Restriccion_a_los_compromisos_no_desembolsados_con_ccp_que_no_califican_se_debera_aplicar_un_7e1690
    - Restriccion_a_los_conceptos_citados_en_los_puntos_precedentes_se_les_restaran_los_conceptos__38377e
    - Restriccion_aforo_del_0_5_para_titulos_valores_emitidos_por_sector_publico_no_financiero_otr_5647c1
    - Restriccion_aforo_del_0_para_efectivo_en_deposito_todos_los_plazos_de_vencimiento_residual___1fbda4
    - Restriccion_aforo_del_0_para_titulos_valores_emitidos_por_sector_publico_no_financiero_otros_1a25ba
    - Restriccion_aforo_del_12_para_titulos_de_deuda_emitidos_por_empresas_con_grado_de_inversion__b97d95
    - Restriccion_aforo_del_12_para_titulos_de_deuda_emitidos_por_fideicomisos_financieros_plazo_d_ac2251
    - Restriccion_aforo_del_15_para_titulos_valores_emitidos_por_sector_publico_no_financiero_otro_45e86f
    - Restriccion_aforo_del_1_para_titulos_valores_emitidos_por_sector_publico_no_financiero_otros_b96fe1
    - Restriccion_aforo_del_20_o_50_para_titulos_valores_emitidos_por_sector_publico_no_financiero_af719a
    - Restriccion_aforo_del_20_para_acciones_y_bonos_convertibles_en_acciones_incluidas_en_indices_21f765
    - Restriccion_aforo_del_20_para_titulos_de_deuda_emitidos_por_empresas_con_grado_de_inversion__29773e
    - Restriccion_aforo_del_24_para_titulos_de_deuda_emitidos_por_fideicomisos_financieros_plazo_d_0142db
    - Restriccion_aforo_del_2_para_titulos_de_deuda_emitidos_por_empresas_con_grado_de_inversion_p_a4e6e5
    - Restriccion_aforo_del_2_para_titulos_valores_emitidos_por_sector_publico_no_financiero_otros_99ed5b
    - Restriccion_aforo_del_30_para_operaciones_de_financiacion_con_titulos_valores_sft_en_las_que_19672d
    - Restriccion_aforo_del_30_para_otras_acciones_y_bonos_convertibles_en_acciones_que_coticen_en_07ac74
    - Restriccion_aforo_del_30_para_otro_tipo_de_exposiciones_todos_los_plazos_de_vencimiento_resi_bb0a2f
    - Restriccion_aforo_del_3_para_titulos_valores_emitidos_por_sector_publico_no_financiero_otros_d797cc
    - Restriccion_aforo_del_4_para_titulos_de_deuda_emitidos_por_empresas_con_grado_de_inversion_p_0bc049
    - Restriccion_aforo_del_4_para_titulos_de_deuda_emitidos_por_fideicomisos_financieros_plazo_de_e047e9
    - Restriccion_aforo_del_4_para_titulos_valores_emitidos_por_sector_publico_no_financiero_otros_565512
    - Restriccion_aforo_del_4_para_titulos_valores_emitidos_por_sector_publico_no_financiero_otros_950e38
    - Restriccion_aforo_del_6_para_titulos_de_deuda_emitidos_por_empresas_con_grado_de_inversion_p_649b62
    - Restriccion_aforo_del_6_para_titulos_valores_emitidos_por_sector_publico_no_financiero_otros_24618b
    - Restriccion_aforo_del_6_para_titulos_valores_emitidos_por_sector_publico_no_financiero_otros_42dfb7
    - Restriccion_aforo_para_cuotapartes_emitidas_por_fondos_comunes_de_inversion_fci_depository_r_4a26a0
    - Restriccion_aforo_por_descalce_de_monedas_del_8_aplicable_cuando_la_exposicion_y_el_activo_r_c12a2f
    - Restriccion_cargo_de_capital_del_100_para_operaciones_dvp_fallidas_cuando_el_pago_no_se_real_d80be6
    - Restriccion_cargo_de_capital_del_50_para_operaciones_dvp_fallidas_cuando_el_pago_no_se_reali_84e6a4
    - Restriccion_cargo_de_capital_del_75_para_operaciones_dvp_fallidas_cuando_el_pago_no_se_reali_5b5bf2
    - Restriccion_cargo_de_capital_del_8_para_operaciones_dvp_fallidas_cuando_el_pago_no_se_realiz_8d4d77
    - Restriccion_cartas_de_credito_comercial_de_corto_plazo_plazo_residual_hasta_un_ano_autoliqui_514f67
    - Restriccion_compromisos_de_adquisicion_de_activos_no_contabilizados_en_el_balance_de_saldos__639458
    - Restriccion_compromisos_que_pueden_ser_cancelados_discrecional_y_unilateralmente_por_la_enti_355e50
    - Restriccion_cuando_a_es_mayor_o_igual_a_k_el_ponderador_sera_igual_a_k_multiplicado_por_12_5_5661b9
    - Restriccion_cuando_ccp_recibe_activos_en_garantia_se_aplica_ponderador_del_2_a_garantias_inc_a825a4
    - Restriccion_cuando_ccp_recibe_margen_de_variacion_y_activo_del_miembro_compensador_no_esta_p_c625af
    - Restriccion_cuando_cliente_no_esta_protegido_contra_perdidas_por_falta_de_pago_insolvencia_c_824645
    - Restriccion_cuando_d_es_menor_o_igual_a_k_el_ponderador_de_riesgo_sera_del_1250__cap_3_1_11__92ac49
    - Restriccion_cuando_el_bcra_autoriza_incrementos_al_valor_del_inmueble_tras_una_reduccion_gen_7c02f8
    - Restriccion_cuando_el_cliente_sea_beneficiario_directo_del_decreto_277_22_la_aplicacion_solo_a7f2c1
    - Restriccion_cuando_el_importe_del_derivado_de_credito_es_inferior_o_igual_al_de_la_obligacio_749a6c
    - Restriccion_cuando_el_importe_del_derivado_de_credito_es_superior_al_de_la_obligacion_subyac_efbb8b
    - Restriccion_cuando_falte_la_inclusion_en_los_documentos_de_la_tasa_de_interes_y_o_del_costo__f4a22c
    - Restriccion_cuando_hay_descalce_de_plazos_de_vencimiento_no_se_reconoce_la_crc_que_tenga_un__3b434d
    - Restriccion_cuando_k_es_mayor_que_a_y_menor_que_d_el_ponderador_sera_un_promedio_ponderado_e_2e4459
    - Restriccion_cuando_la_entidad_no_presenta_su_descargo_en_el_plazo_indicado_el_incumplimiento_e53177
    - Restriccion_cuando_la_medida_de_riesgo_eve_estandarizada_supere_el_15_del_nivel_de_capital_1_bd85a1
    - Restriccion_cuando_los_tramos_de_maxima_preferencia_comparten_asignacion_de_perdidas_a_prorr_c8bb57
    - Restriccion_cuando_se_cumplan_las_condiciones_del_inciso_i_ningun_lado_de_la_operacion_estar_d6102e
    - Restriccion_cuando_se_trate_de_entidades_financieras_controladas_y_corresponda_aplicar_lo_pr_04cc87
    - Restriccion_cuando_una_exposicion_podria_estar_sujeta_a_distintos_ponderadores_especificos_d_9070ee
    - Restriccion_de_los_rubros_contables_de_ingresos_financieros_y_por_servicios_menos_egresos_fi_0de869
    - Restriccion_de_los_rubros_contables_de_ingresos_financieros_y_por_servicios_menos_egresos_fi_1d517e
    - Restriccion_de_los_rubros_contables_de_ingresos_financieros_y_por_servicios_menos_egresos_fi_bfbdb1
    - Restriccion_deudor_clasificado_en_riesgo_medio_que_haya_refinanciado_su_deuda_y_recibido_cre_04bc05
    - Restriccion_deudores_con_atrasos_mayores_a_31_dias_en_obligaciones_refinanciadas_deben_recat_4665b9
    - Restriccion_el_acceso_al_mercado_de_cambios_esta_limitado_al_monto_de_la_certificacion_otorg_cec881
    - Restriccion_el_acceso_al_mercado_de_cambios_no_podra_exceder_el_monto_de_la_certificacion__e_6ec9a6
    - Restriccion_el_acceso_al_mercado_de_cambios_para_repatriacion_de_inversiones_de_no_residente_a81a32
    - Restriccion_el_activo_recibido_en_garantia_se_limitara_a_aquellos_listados_en_el_punto_5_3_1_ddaea1
    - Restriccion_el_aforo_por_descalce_de_monedas_entre_la_proteccion_crediticia_y_la_exposicion__56a32e
    - Restriccion_el_cambio_de_metodo_empleado_requiere_preaviso_a_la_sefyc__cap_5_1_1_fc5f3d
    - Restriccion_el_capital_ordinario_de_nivel_1_con1_calculado_como_70210000_70220000_debe_ser_c_d27191
    - Restriccion_el_cliente_no_debe_haber_adquirido_certificados_de_depositos_argentinos_represen_9646fa
    - Restriccion_el_cliente_no_debe_haber_adquirido_en_el_pais_titulos_valores_emitidos_por_no_re_9dff24
    - Restriccion_el_cliente_no_debe_haber_adquirido_titulos_valores_representativos_de_deuda_priv_e3e947
    - Restriccion_el_cliente_no_debe_haber_concertado_ventas_en_el_pais_de_titulos_valores_con_liq_24d681
    - Restriccion_el_cliente_no_debe_haber_entregado_fondos_en_moneda_local_ni_otros_activos_local_f08e6c
    - Restriccion_el_cliente_no_debe_haber_realizado_canjes_de_titulos_valores_emitidos_por_reside_eb6c6c
    - Restriccion_el_cliente_no_debe_haber_realizado_transferencias_de_titulos_valores_a_entidades_a5faa1
    - Restriccion_el_cliente_no_tendra_acceso_al_mercado_de_cambios_para_pagar_el_equivalente_de_l_a1765c
    - Restriccion_el_cliente_que_no_sea_persona_humana_residente_no_debe_haber_entregado_en_el_pai_07b9e1
    - Restriccion_el_cliente_que_se_encuentre_permanentemente_atrasado_en_el_pago_con_incumplimien_94acff
    - Restriccion_el_coeficiente_a_asignar_para_el_calculo_del_monto_maximo_de_certificaciones_de__9955d7
    - Restriccion_el_computo_de_las_participaciones_se_efectuara_neto_de_las_previsiones_por_riesg_3cac6f
    - Restriccion_el_computo_de_los_plazos_no_se_interrumpira_por_el_otorgamiento_de_renovaciones__0f0a32
    - Restriccion_el_contrato_de_neteo_no_debe_contener_clausulas_que_permitan_a_la_parte_cumplido_af1679
    - Restriccion_el_contrato_de_proteccion_crediticia_debe_ser_irrevocable_y_no_puede_contener_cl_d57ade
    - Restriccion_el_contrato_de_proteccion_no_debe_contener_clausulas_que_escapen_al_control_dire_eb3362
    - Restriccion_el_descalce_de_monedas_entre_la_exposicion_y_el_activo_recibido_en_garantia_se_a_c2084f
    - Restriccion_el_descalce_de_plazos_de_vencimiento_entre_la_exposicion_y_el_activo_admitido_co_0d01f1
    - Restriccion_el_desempeno_de_la_titulizacion_no_debe_depender_de_seleccion_de_subyacentes_med_348c42
    - Restriccion_el_deudor_clasificado_en_esta_categoria_que_haya_refinanciado_su_deuda_y_recibid_b6ce71
    - Restriccion_el_deudor_que_haya_refinanciado_su_deuda_aun_cuando_haya_cancelado_el_porcentaje_d07210
    - Restriccion_el_exceso_a_los_limites_para_la_afectacion_de_activos_en_garantia_segun_lo_dispu_a7eca2
    - Restriccion_el_importe_de_la_reduccion_de_exigencia_debe_ser_inferior_al_registrado_en_la_pa_8cda96
    - Restriccion_el_importe_de_pnb_admisible_como_ca_excluye_los_importes_reconocidos_como_co_con_22b710
    - Restriccion_el_importe_de_rpc_admisible_como_pnc_excluye_los_importes_reconocidos_en_el_co_c_e60c71
    - Restriccion_el_importe_resultante_de_aplicar_lo_dispuesto_en_la_seccion_2_debera_ser_multipl_67b85a
    - Restriccion_el_inversor_no_tendra_ningun_derecho_a_acelerar_la_devolucion_de_los_pagos_futur_0551d5
    - Restriccion_el_limite_de_reconocimiento_como_rpc_se_aplicara_por_separado_a_cada_instrumento_486d0b
    - Restriccion_el_limite_de_reconocimiento_como_rpc_se_reducira_cada_doce_meses_en_10_puntos_po_9f7e33
    - Restriccion_el_monto_acumulado_de_aplicaciones_de_capital_e_intereses_emitidas_por_las_opera_ed22b4
    - Restriccion_el_monto_acumulado_de_las_certificaciones_de_aplicacion_emitidas_no_puede_supera_f62bac
    - Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_no_podra_ex_b5cb86
    - Restriccion_el_monto_acumulado_de_los_beneficios_totales_reconocidos_al_cliente_por_la_secre_dcc561
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_de_los_nuevos_titulos_no_podra_6b89bd
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_de_los_nuevos_titulos_no_podra_ef021d
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_no_pod_4d5eb0
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_no_pod_60b35d
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_no_pod_69cd35
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_no_pod_864b9b
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_no_pod_dd4fee
    - Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_no_podra_superar_en_ningun_mom_c7b7bb
    - Restriccion_el_monto_anual_aplicado_no_podra_superar_el_60_del_monto_bruto_de_las_divisas_in_86c4b0
    - Restriccion_el_monto_anual_aplicado_no_podra_superar_el_equivalente_al_40_del_monto_bruto_de_9729eb
    - Restriccion_el_monto_aplicado_a_las_operaciones_de_cobro_de_exportaciones_no_podra_superar_e_c19f7a
    - Restriccion_el_monto_aplicado_en_el_beneficio_ampliado_no_podra_superar_el_60_del_valor_de_l_d0374c
    - Restriccion_el_monto_de_bopreal_a_suscribir_no_podra_exceder_el_monto_de_la_deuda_pendiente__5a0909
    - Restriccion_el_monto_de_capital_por_el_cual_se_accedio_al_mercado_de_cambios_hasta_el_31_12__8ee663
    - Restriccion_el_monto_de_las_aplicaciones_de_divisas_de_cobros_de_exportaciones_de_bienes_a_l_ecd061
    - Restriccion_el_monto_de_las_certificaciones_de_aumento_de_exportaciones_de_bienes_emitidas_d_769ce0
    - Restriccion_el_monto_de_las_certificaciones_obtenidas_para_el_periodo_trimestral_de_referenc_a84216
    - Restriccion_el_monto_de_los_prestamos_a_instituciones_de_microcredito_no_podra_exceder_el_eq_9b78d6
    - Restriccion_el_monto_de_los_vencimientos_de_capital_de_endeudamientos_financieros_comprendid_565f23
    - Restriccion_el_monto_de_suscripcion_de_bopreal_no_podra_exceder_el_equivalente_al_monto_en_m_ea0c47
    - Restriccion_el_monto_de_suscripcion_de_bopreal_no_podra_exceder_el_equivalente_en_moneda_loc_2bd421
    - Restriccion_el_monto_de_suscripcion_de_bopreal_no_podra_exceder_la_suma_adeudada_a_la_fecha__aa1534
    - Restriccion_el_monto_de_suscripcion_no_podra_exceder_el_equivalente_en_moneda_local_de_las_u_434b47
    - Restriccion_el_monto_del_beneficio_ampliado_no_podra_superar_el_40_del_valor_de_los_permisos_be2f66
    - Restriccion_el_monto_imputado_por_reimportacion_de_mercaderia_rechazada_no_podra_exceder_el__283161
    - Restriccion_el_monto_maximo_de_adelanto_en_efectivo_a_tarjetahabientes_en_el_exterior_es_usd_102065
    - Restriccion_el_monto_total_abonado_por_el_mecanismo_de_acceso_al_mercado_de_cambios_no_podra_b97a27
    - Restriccion_el_monto_total_de_deudas_abonadas_en_el_mes_calendario_bajo_este_mecanismo_no_pu_6ab320
    - Restriccion_el_monto_total_de_las_certificaciones_emitidas_incluyendo_la_que_se_solicita_emi_d76dc3
    - Restriccion_el_monto_total_de_las_exposiciones_a_un_deudor_en_particular_no_podra_exceder_el_cdf42d
    - Restriccion_el_oro_queda_excluido_del_alcance_de_la_exigencia_de_capital_por_riesgo_de_posic_f8546f
    - Restriccion_el_pago_no_podra_superar_el_equivalente_al_50_del_monto_liquidado_simultaneament_5510c3
    - Restriccion_el_patrimonio_neto_basico_pnb_calculado_como_70210000_70220000_70230000_70240000_03a0ce
    - Restriccion_el_periodo_de_vigencia_del_derivado_de_credito_debe_ser_suficiente_para_determin_46c39d
    - Restriccion_el_ponderador_aplicable_a_la_contraparte_i_se_establece_en_0_para_el_sector_publ_8fde2f
    - Restriccion_el_ponderador_aplicable_a_la_contraparte_i_se_establece_en_3_para_el_resto_de_la_4a2c59
    - Restriccion_el_ponderador_de_riesgo_aplicable_a_exposiciones_garantizadas_por_sociedades_de__8812df
    - Restriccion_el_ponderador_de_riesgo_aplicable_a_las_exposiciones_minoristas_no_normativas_es_dbad85
    - Restriccion_el_ponderador_de_riesgo_de_la_parte_de_la_exposicion_cubierta_podra_ser_inferior_4cad1e
    - Restriccion_el_ponderador_de_riesgo_de_las_exposiciones_a_entidades_financieras_no_puede_ser_132c38
    - Restriccion_el_ponderador_de_riesgo_de_las_exposiciones_a_entidades_financieras_no_puede_ser_5568ca
    - Restriccion_el_ponderador_de_riesgo_para_cuentas_corrientes_y_especiales_en_el_bcra_y_ordene_517715
    - Restriccion_el_ponderador_de_riesgo_para_exposiciones_a_empresas_con_grado_de_inversion_es_d_f4e5e9
    - Restriccion_el_ponderador_de_riesgo_para_exposiciones_a_mipyme_que_no_se_ajustan_a_los_crite_fe0ee3
    - Restriccion_el_ponderador_de_riesgo_para_exposiciones_al_bcra_en_pesos_cuando_su_fuente_de_f_dd2746
    - Restriccion_el_ponderador_de_riesgo_para_exposiciones_con_garantia_hipotecaria_normativa_sob_be354c
    - Restriccion_el_ponderador_de_riesgo_para_exposiciones_minoristas_normativas_no_transaccional_c61773
    - Restriccion_el_ponderador_de_riesgo_para_la_exposicion_a_entidades_que_cumplan_satisfactoria_ad1d65
    - Restriccion_el_ponderador_de_riesgo_para_operaciones_al_contado_a_liquidar_no_fallidas_es_0__503af2
    - Restriccion_el_ponderador_resultante_estara_sujeto_a_un_minimo_del_100_para_retitulizaciones_429fd6
    - Restriccion_el_ponderador_resultante_estara_sujeto_a_un_minimo_del_10_para_los_tramos_de_max_d5cf8d
    - Restriccion_el_ponderador_resultante_estara_sujeto_a_un_minimo_del_15_para_titulizaciones_qu_ffff06
    - Restriccion_el_producto_del_ponderador_de_riesgo_promedio_del_fondo_y_el_apalancamiento_del__8b3fb9
    - Restriccion_el_reconocimiento_como_rpc_se_limitara_al_90_del_valor_obtenido_mediante_la_apli_d62ea0
    - Restriccion_el_requerimiento_de_capital_para_una_exposicion_crediticia_con_coberturas_de_rie_2026d3
    - Restriccion_el_saldo_a_favor_por_aplicacion_del_impuesto_a_la_ganancia_minima_presunta_solo__01f477
    - Restriccion_el_sistema_online_considerara_exclusivamente_los_ingresos_de_divisas_desde_el_ex_878bf9
    - Restriccion_el_total_de_los_pagos_realizados_con_imputacion_a_la_oficializacion_de_importaci_693eb0
    - Restriccion_el_total_de_participaciones_en_el_capital_de_empresas_no_podra_exceder_el_60__ri_0d90e2
    - Restriccion_el_tratamiento_dispensado_en_el_marco_de_la_ley_de_emergencia_agropecuaria_no_po_536cea
    - Restriccion_el_valor_acumulado_pendiente_de_liquidacion_adeudado_al_exportador_por_el_no_res_f03637
    - Restriccion_el_valor_de_la_tasacion_del_inmueble_no_debe_resultar_mayor_al_precio_de_mercado_8e2d33
    - Restriccion_el_valor_de_las_exportaciones_de_bienes_enviados_al_exterior_con_fines_promocion_18f9b7
    - Restriccion_el_valor_de_mercado_de_las_otras_ventas_de_titulos_valores_no_debe_superar_la_di_c1d421
    - Restriccion_el_valor_de_mercado_de_las_otras_ventas_de_titulos_valores_no_puede_superar_la_d_19ec3e
    - Restriccion_el_valor_nominal_de_los_nuevos_titulos_entregados_como_prima_de_participacion_re_106b35
    - Restriccion_en_caso_de_discrepancias_entre_pautas_de_clasificacion_debe_considerarse_la_paut_b6e5b6
    - Restriccion_en_caso_de_reduccion_del_plazo_vigente_el_plazo_reducido_solo_rige_para_las_oper_e97c28
    - Restriccion_en_el_calculo_de_capital_por_riesgo_especifico_solo_se_permite_netear_posiciones_9364cc
    - Restriccion_en_el_calculo_de_capital_solo_se_incluiran_los_efectos_gamma_netos_que_sean_nega_7a6a4f
    - Restriccion_en_el_caso_de_una_extraccion_con_una_tarjeta_prepaga_sera_de_aplicacion_el_limit_7282fd
    - Restriccion_en_los_casos_en_que_el_prestamo_con_garantia_hipotecaria_financie_la_compra_del__6567f2
    - Restriccion_en_los_contratos_de_tarjeta_de_credito_el_consentimiento_a_modificaciones_en_las_996684
    - Restriccion_exigencia_adicional_de_capital_para_la_cobertura_del_riesgo_gamma_que_mide_la_ta_72fa25
    - Restriccion_exigencia_adicional_de_capital_para_la_cobertura_del_riesgo_vega_que_mide_la_sen_0616b8
    - Restriccion_exigencia_de_capital_adicional_de_2_de_la_posicion_neta_comprada_o_vendida_en_co_333a56
    - Restriccion_exigencia_de_capital_de_4_a_las_posiciones_que_surjan_de_estrategias_de_arbitraj_d7b1da
    - Restriccion_exigencia_de_capital_por_riesgo_especifico_en_concepto_de_riesgo_de_emisor_para__2d52ba
    - Restriccion_exigencia_de_capital_por_riesgo_especifico_en_concepto_de_riesgo_de_emisor_para__342a52
    - Restriccion_exigencia_de_capital_por_riesgo_especifico_en_concepto_de_riesgo_de_emisor_para__3a8b8a
    - Restriccion_exigencia_de_capital_por_riesgo_especifico_en_concepto_de_riesgo_de_emisor_para__3ad55b
    - Restriccion_exigencia_de_capital_por_riesgo_especifico_en_concepto_de_riesgo_de_emisor_para__4d9102
    - Restriccion_exigencia_de_capital_por_riesgo_especifico_en_concepto_de_riesgo_de_emisor_para__581763
    - Restriccion_exigencia_de_capital_por_riesgo_especifico_en_concepto_de_riesgo_de_emisor_para__cb523e
    - Restriccion_exigencia_de_capital_por_riesgo_especifico_en_concepto_de_riesgo_de_emisor_para__cb980d
    - Restriccion_exposicion_a_gobiernos_y_bancos_centrales_con_calificacion_a_hasta_a_se_pondera__31c941
    - Restriccion_exposicion_a_gobiernos_y_bancos_centrales_con_calificacion_aaa_hasta_aa_se_ponde_5fb677
    - Restriccion_exposicion_a_gobiernos_y_bancos_centrales_con_calificacion_bb_hasta_b_se_pondera_4c1bfb
    - Restriccion_exposicion_a_gobiernos_y_bancos_centrales_con_calificacion_bbb_hasta_bbb_se_pond_869423
    - Restriccion_exposicion_a_gobiernos_y_bancos_centrales_con_calificacion_inferior_a_b_se_ponde_9dbbbc
    - Restriccion_exposicion_a_gobiernos_y_bancos_centrales_sin_calificacion_se_pondera_al_100__ca_9b1b69
    - Restriccion_exposiciones_a_bancos_multilaterales_de_desarrollo_con_calificacion_a_hasta_a_ti_7772d4
    - Restriccion_exposiciones_a_bancos_multilaterales_de_desarrollo_con_calificacion_aaa_hasta_aa_316b93
    - Restriccion_exposiciones_a_bancos_multilaterales_de_desarrollo_con_calificacion_bb_hasta_b_t_a9848f
    - Restriccion_exposiciones_a_bancos_multilaterales_de_desarrollo_con_calificacion_bbb_hasta_bb_6d78af
    - Restriccion_exposiciones_a_bancos_multilaterales_de_desarrollo_con_calificacion_inferior_a_b_bd2ad1
    - Restriccion_exposiciones_a_bancos_multilaterales_de_desarrollo_sin_calificacion_tienen_ponde_e5e22c
    - Restriccion_factor_de_100_aplicable_cuando_han_transcurrido_46_o_mas_dias_habiles_posteriore_cc1e49
    - Restriccion_factor_de_50_aplicable_cuando_han_transcurrido_entre_16_y_30_dias_habiles_poster_f4b877
    - Restriccion_factor_de_75_aplicable_cuando_han_transcurrido_entre_31_y_45_dias_habiles_poster_597bac
    - Restriccion_factor_de_8_aplicable_cuando_han_transcurrido_entre_5_y_15_dias_habiles_posterio_a439cc
    - Restriccion_factor_de_conversion_de_credito_ccf_del_0_para_el_periodo_del_01_01_25_al_30_06__d38595
    - Restriccion_factor_de_conversion_de_credito_ccf_del_5_para_el_periodo_del_01_07_25_al_31_12__604740
    - Restriccion_indicador_de_clasificacion_en_categoria_de_alto_riesgo_de_insolvencia_refinancia_0811c3
    - Restriccion_la_acumulacion_de_fondos_de_exportacion_en_cuentas_del_exterior_y_o_del_pais_est_7045b4
    - Restriccion_la_acumulacion_de_fondos_estara_disponible_hasta_alcanzar_el_125_de_los_servicio_7aea97
    - Restriccion_la_acumulacion_de_fondos_estara_disponible_hasta_alcanzar_el_125_del_capital_e_i_9c25df
    - Restriccion_la_aplicacion_de_divisas_a_las_operaciones_sera_admitida_solo_si_se_cumplen_la_t_daa6c9
    - Restriccion_la_aplicacion_del_tratamiento_de_la_ley_de_emergencia_agropecuaria_no_podra_exte_f19cf2
    - Restriccion_la_calificacion_internacional_de_riesgo_debe_estar_comprendida_en_categoria_inve_02cb9c
    - Restriccion_la_capitalizacion_de_deuda_no_podra_implicar_una_limitacion_o_suspension_al_dere_be6c69
    - Restriccion_la_deduccion_de_ganancias_por_ventas_se_computara_en_la_medida_que_subsista_el_r_9db93a
    - Restriccion_la_deduccion_se_computara_en_la_proporcion_en_que_se_mantenga_la_exigencia_de_ca_e587db
    - Restriccion_la_deduccion_se_realizara_unicamente_por_el_mayor_saldo_en_cada_banco_que_se_reg_56e8f8
    - Restriccion_la_deuda_total_mas_la_financiacion_solicitada_no_podra_exceder_del_2_5_de_la_res_63da91
    - Restriccion_la_division_del_tramo_original_en_subtramos_cubierto_y_descubierto_no_constituye_c013ee
    - Restriccion_la_ead_para_un_conjunto_de_neteo_con_margenes_de_variacion_no_podra_exceder_la_e_248257
    - Restriccion_la_entidad_del_exterior_sobre_cuya_cuenta_bancaria_se_liquida_la_operacion_no_de_4ee9bb
    - Restriccion_la_exclusion_de_futuros_o_forwards_con_gama_de_instrumentos_solo_procede_si_la_e_428076
    - Restriccion_la_exigencia_de_capital_por_riesgo_de_tipo_de_cambio_sera_el_8_de_la_posicion_ne_b69517
    - Restriccion_la_exigencia_de_capital_por_riesgo_especifico_sera_del_8_de_ese_riesgo__cap_6_3__7a302b
    - Restriccion_la_exigencia_de_capital_por_riesgo_general_de_mercado_sera_del_8_de_ese_riesgo___486133
    - Restriccion_la_exigencia_de_capital_sera_el_menor_entre_i_el_valor_de_mercado_del_subyacente_1da650
    - Restriccion_la_exposicion_con_garantia_hipotecaria_debe_estar_garantizada_por_un_inmueble_te_9c2483
    - Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar_f97a2c
    - Restriccion_la_extension_de_plazos_para_pagos_anticipados_de_bienes_de_capital_no_podra_supe_3212e8
    - Restriccion_la_extension_de_plazos_para_restantes_pagos_no_podra_superar_365_dias_corridos_c_d16fb1
    - Restriccion_la_facilidad_de_liquidez_no_debera_ser_tratada_como_de_maxima_preferencia_si_se__c09c98
    - Restriccion_la_falta_de_cumplimiento_de_cualquiera_de_los_limites_minimos_sera_considerada_i_b603ec
    - Restriccion_la_figura_de_incumplido_en_gestion_de_cobro_no_podra_ser_aplicada_por_la_entidad_719de4
    - Restriccion_la_inversion_de_cuotapartes_emitidas_por_fondos_comunes_de_inversion_depository__5636a4
    - Restriccion_la_inversion_en_fondos_debe_ponderarse_al_1250_cuando_no_se_puede_recurrir_al_lt_e937b9
    - Restriccion_la_modificacion_de_condiciones_pactadas_no_debe_alterar_el_objeto_del_contrato_n_8b3e25
    - Restriccion_la_nueva_deuda_financiera_no_puede_anticipar_vencimientos_respecto_de_la_deuda_c_68f6e1
    - Restriccion_la_nueva_deuda_financiera_no_puede_implicar_la_realizacion_de_pagos_antes_de_la__662e53
    - Restriccion_la_opcion_de_ampliacion_del_plazo_estara_disponible_hasta_alcanzar_el_125_de_los_dd9b9a
    - Restriccion_la_parte_de_la_exposicion_cubierta_recibira_el_ponderador_de_riesgo_correspondie_0ab4b9
    - Restriccion_la_participacion_en_el_capital_de_cada_empresa_no_podra_exceder_el_15__ric_3_1_2_0d81e5
    - Restriccion_la_porcion_de_los_endeudamientos_financieros_utilizada_conforme_a_este_punto_no__e62d02
    - Restriccion_la_porcion_del_endeudamiento_financiero_utilizada_conforme_a_este_punto_no_puede_971a71
    - Restriccion_la_presencia_de_una_opcion_de_exclusion_no_originara_exigencia_de_capital_alguna_3980a9
    - Restriccion_la_prima_de_recompra_rescate_anticipado_o_similar_no_podra_exceder_el_5_del_mont_cfd51b
    - Restriccion_la_proteccion_crediticia_se_reconoce_solo_en_la_medida_en_que_el_ponderador_de_r_738efd
    - Restriccion_la_reduccion_de_la_ead_por_las_perdidas_por_cva_incurridas_no_se_aplica_para_la__e8e4f6
    - Restriccion_la_responsabilidad_patrimonial_computable_rpc_calculada_como_70200000_debe_ser_c_0b0121
    - Restriccion_la_sola_existencia_de_5_000_operaciones_o_mas_en_un_conjunto_de_neteo_no_determi_4c0fec
    - Restriccion_la_suma_de_los_pagos_anticipados_a_la_vista_y_de_deuda_comercial_sin_registro_de_9e1418
    - Restriccion_la_suma_de_los_pagos_anticipados_no_puede_superar_el_30_del_valor_fob_de_los_bie_1e360d
    - Restriccion_la_suscripcion_local_no_puede_superar_el_25_de_la_suscripcion_total__ext_3_5_1_8_0fe777
    - Restriccion_la_tasacion_del_inmueble_no_debe_basarse_en_la_expectativa_de_que_se_incrementar_89e39d
    - Restriccion_la_tasacion_del_inmueble_no_debe_depender_de_la_situacion_economica_del_prestata_12b3f7
    - Restriccion_la_titulizacion_no_contiene_clausulas_mediante_las_cuales_la_entidad_financiera__fdcd0c
    - Restriccion_la_titulizacion_no_contiene_clausulas_mediante_las_cuales_se_aumente_el_rendimie_2cfc94
    - Restriccion_la_titulizacion_no_contiene_clausulas_mediante_las_cuales_se_obligue_a_la_origin_3023ca
    - Restriccion_la_titulizacion_no_debe_ser_estructurada_como_una_cascada_inversa_de_modo_que_lo_180778
    - Restriccion_la_titulizacion_no_incluye_opciones_de_rescision_o_eventos_desencadenantes_de_la_bb3b27
    - Restriccion_la_venta_de_los_titulos_en_el_origen_de_la_operacion_no_debe_considerarse_a_efec_031712
    - Restriccion_las_certificaciones_tendran_una_validez_de_10_diez_dias_habiles_a_contar_desde_l_1d957d
    - Restriccion_las_coberturas_que_no_se_realicen_a_traves_de_derivados_solo_seran_admisibles_si_433e9f
    - Restriccion_las_compensaciones_horizontales_estan_sujetas_a_una_escala_de_desestimaciones_ho_8791ea
    - Restriccion_las_cuotas_de_todas_las_financiaciones_de_la_entidad_que_cuenten_con_sistema_de__bb7a4b
    - Restriccion_las_deudas_comprendidas_en_el_punto_3_5_6_permanecen_sujetas_al_requisito_de_con_c9a0a0
    - Restriccion_las_exportaciones_de_bienes_de_un_vpu_adherido_al_rigi_no_declarado_de_exportaci_04060c
    - Restriccion_las_exposiciones_deberan_reasignarse_al_grado_c_cuando_la_entidad_financiera_pre_a02cf6
    - Restriccion_las_financiaciones_de_los_puntos_7_11_1_1_a_7_11_1_4_no_deben_tener_vencimientos_0ad73c
    - Restriccion_las_financiaciones_de_los_puntos_7_11_1_5_a_7_11_1_6_no_deben_registrar_vencimie_8abb01
    - Restriccion_las_financiaciones_no_deben_haber_sido_fondeadas_con_una_linea_de_credito_de_una_1abe44
    - Restriccion_las_franquicias_posiciones_a_primera_perdida_deberan_ser_ponderadas_por_riesgo_a_946cde
    - Restriccion_las_garantias_acumuladas_en_moneda_extranjera_no_podran_superar_el_equivalente_a_adbf72
    - Restriccion_las_inversiones_en_capital_de_entidades_financieras_seran_netas_de_las_prevision_4d317b
    - Restriccion_las_opciones_y_sus_subyacentes_al_contado_o_a_termino_estan_sujetas_a_una_exigen_63036d
    - Restriccion_las_operaciones_bilaterales_con_acuerdo_de_margen_de_variacion_unidireccional_a__ab403f
    - Restriccion_las_operaciones_de_financiacion_con_titulos_valores_sft_tales_como_operaciones_d_cde3c0
    - Restriccion_las_operaciones_que_impliquen_la_importacion_de_billetes_de_pesos_argentinos_que_1f9e1c
    - Restriccion_las_posiciones_arancelarias_de_los_bienes_de_capital_a_importar_no_pueden_corres_e26cf6
    - Restriccion_las_posiciones_brutas_en_cada_banda_temporal_en_monedas_residuales_estaran_sujet_797b52
    - Restriccion_las_posiciones_brutas_en_cada_banda_temporal_en_monedas_residuales_estaran_sujet_c53aa2
    - Restriccion_las_posiciones_de_titulizacion_a_las_que_no_se_les_pueda_aplicar_el_enfoque_esta_bcb906
    - Restriccion_las_posiciones_estan_sujetas_a_limites_que_se_supervisan_para_comprobar_su_adecu_8a7a4f
    - Restriccion_las_posteriores_refinanciaciones_no_reciben_el_tratamiento_especial_de_reclasifi_f6249f
    - Restriccion_las_previsiones_por_riesgo_de_incobrabilidad_no_podran_superar_el_1_25_de_los_ac_87e310
    - Restriccion_las_reservas_a_integrar_con_ingresos_futuros_provenientes_de_los_activos_subyace_40f735
    - Restriccion_las_siguientes_partidas_no_contribuyen_a_ninguna_de_las_partidas_del_bi_cambios__de006c
    - Restriccion_las_siguientes_partidas_no_contribuyen_a_ninguna_de_las_partidas_del_bi_deprecia_c98f8b
    - Restriccion_las_siguientes_partidas_no_contribuyen_a_ninguna_de_las_partidas_del_bi_deterior_c61eda
    - Restriccion_las_siguientes_partidas_no_contribuyen_a_ninguna_de_las_partidas_del_bi_gastos_a_0f615c
    - Restriccion_las_siguientes_partidas_no_contribuyen_a_ninguna_de_las_partidas_del_bi_gastos_e_dd8252
    - Restriccion_las_siguientes_partidas_no_contribuyen_a_ninguna_de_las_partidas_del_bi_impuesto_425b6c
    - Restriccion_las_siguientes_partidas_no_contribuyen_a_ninguna_de_las_partidas_del_bi_ingresos_197b3a
    - Restriccion_las_siguientes_partidas_no_contribuyen_a_ninguna_de_las_partidas_del_bi_pago_de__3da797
    - Restriccion_las_siguientes_partidas_no_contribuyen_a_ninguna_de_las_partidas_del_bi_provisio_be4986
    - Restriccion_las_siguientes_partidas_no_contribuyen_a_ninguna_de_las_partidas_del_bi_recupero_818281
    - Restriccion_las_transacciones_de_titulos_valores_concertadas_en_el_exterior_no_podran_liquid_d30402
    - Restriccion_lineas_de_credito_comprometidas_independientemente_del_vencimiento_de_la_facilid_163808
    - Restriccion_lineas_de_emision_de_titulos_valores_de_corto_plazo_nif_y_lineas_rotativas_de_su_364918
    - Restriccion_los_activos_admitidos_como_garantia_se_limitan_a_los_enumerados_en_el_punto_5_3__d463af
    - Restriccion_los_activos_admitidos_como_garantia_se_limitan_a_los_especificados_en_los_puntos_abb1f3
    - Restriccion_los_beneficios_cambiarios_del_rigi_no_podran_ser_acumulados_con_otros_incentivos_fd334c
    - Restriccion_los_bienes_no_deben_corresponder_a_las_posiciones_arancelarias_comprendidas_en_e_7309b7
    - Restriccion_los_casos_que_no_cumplan_las_condiciones_requeridas_quedan_sujetos_a_conformidad_0777eb
    - Restriccion_los_cobros_de_exportaciones_que_pretenden_enmarcarse_en_este_mecanismo_no_pueden_1f272d
    - Restriccion_los_conceptos_que_deben_deducirse_a_los_fines_del_calculo_de_la_rpc_se_excluiran_9b6959
    - Restriccion_los_contratos_con_clausulas_de_abandono_o_ruptura_walkaway_clauses_que_permiten__4e5672
    - Restriccion_los_criterios_stc_deben_cumplirse_en_todo_momento_no_se_permite_su_incumplimient_dbe9e2
    - Restriccion_los_demas_activos_y_o_partidas_fuera_de_balance_tienen_un_ponderador_de_riesgo_d_213942
    - Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti_17ae50
    - Restriccion_los_deudores_en_operaciones_de_cesion_sin_responsabilidad_para_el_cedente_no_ser_29ad89
    - Restriccion_los_documentos_a_cobrar_y_creditos_transferidos_despues_de_la_fecha_de_concrecio_555244
    - Restriccion_los_entes_de_proposito_especial_spe_no_son_garantes_admisibles__cap_3_1_7_4857bf
    - Restriccion_los_estandares_de_originacion_no_deben_ser_menos_rigurosos_que_aquellos_aplicado_9d71b8
    - Restriccion_los_fondos_que_se_aplican_bajo_esta_modalidad_no_deben_exceder_los_limites_que_n_74abe0
    - Restriccion_los_garantes_admisibles_se_limitan_a_los_estipulados_en_el_punto_5_4_1__cap_3_1__e6ecef
    - Restriccion_los_garantes_y_contragarantes_admisibles_se_limitaran_a_aquellos_listados_en_el__ef19e9
    - Restriccion_los_importes_deben_consignarse_en_valores_absolutos__ric_11_1_1_69d71c
    - Restriccion_los_incumplimientos_en_el_envio_de_la_informacion_estaran_sujetos_a_la_aplicacio_1e726a
    - Restriccion_los_inmuebles_cuya_registracion_contable_no_este_respaldada_con_la_pertinente_es_215699
    - Restriccion_los_instrumentos_imputados_a_la_cartera_de_negociacion_deberan_estar_valuados_en_9097a4
    - Restriccion_los_instrumentos_incluidos_en_el_ca_no_podran_estar_asegurados_ni_cubiertos_por__c65d51
    - Restriccion_los_instrumentos_incluidos_en_el_ca_no_podran_haber_sido_comprados_con_la_financ_d30c96
    - Restriccion_los_instrumentos_incluidos_en_el_ca_no_podran_ser_objeto_de_cualquier_otro_acuer_be5e44
    - Restriccion_los_instrumentos_incluidos_en_el_pnc_no_deberan_contener_clausulas_de_remuneraci_42844d
    - Restriccion_los_instrumentos_incluidos_en_el_pnc_no_podran_estar_asegurados_ni_cubiertos_por_b0072f
    - Restriccion_los_instrumentos_incluidos_en_el_pnc_no_podran_ser_objeto_de_cualquier_otro_acue_0ca927
    - Restriccion_los_instrumentos_no_podran_tener_clausulas_de_remuneracion_escalonada_creciente__7f7788
    - Restriccion_los_instrumentos_no_podran_tener_otros_incentivos_para_su_amortizacion_anticipad_57b1dd
    - Restriccion_los_instrumentos_que_no_satisfacen_la_definicion_de_activos_admitidos_como_garan_1c6377
    - Restriccion_los_instrumentos_utilizados_para_transferir_el_riesgo_de_credito_no_pueden_conte_894f58
    - Restriccion_los_montos_de_divisas_afectadas_conforme_al_capitulo_ii_del_decreto_679_22_no_pu_8d3afe
    - Restriccion_los_montos_de_divisas_afectadas_por_el_decreto_679_22_no_pueden_ser_alcanzadas_p_d264c5
    - Restriccion_los_montos_de_la_certificacion_deben_estar_expresados_en_la_moneda_que_fue_liqui_ed12e6
    - Restriccion_los_nuevos_titulos_de_deuda_deben_contemplar_como_minimo_1_ano_de_gracia_para_el_247983
    - Restriccion_los_nuevos_titulos_de_deuda_deben_implicar_una_extension_minima_de_2_anos_respec_fef878
    - Restriccion_los_pagos_por_deudas_de_bienes_o_servicios_en_el_conjunto_de_las_entidades_y_por_8e95d5
    - Restriccion_los_proyectos_relacionados_con_la_actividad_inmobiliaria_no_se_incluyen_en_la_de_f83870
    - Restriccion_los_punitorios_u_otros_equivalentes_que_se_devenguen_desde_el_01_01_25_permanece_298dfa
    - Restriccion_los_subtramos_que_no_son_de_maxima_preferencia_deben_tratarse_como_posiciones_de_34eb2b
    - Restriccion_los_swaps_de_incumplimiento_crediticio_por_tramos_o_de_enesimo_incumplimiento_no_814a89
    - Restriccion_los_swaps_referidos_a_diferentes_productos_basicos_no_podran_compensarse__cap_6__6db5e8
    - Restriccion_los_titulos_valores_subordinados_no_deberan_tener_preferencia_de_pago_sobre_los__677a9b
    - Restriccion_los_unicos_derivados_admisibles_son_los_que_se_toman_para_la_genuina_cobertura_d_a9dfe5
    - Restriccion_maximo_mensual_equivalente_al_10_del_monto_total_de_los_anticipos_que_se_encuadr_b443cc
    - Restriccion_no_deben_considerarse_en_el_calculo_del_k_cva_otros_tipos_de_cobertura_del_riesg_94caf3
    - Restriccion_no_debera_existir_una_correlacion_positiva_sustancial_entre_la_calidad_creditici_412764
    - Restriccion_no_deberan_existir_disposiciones_que_requieran_la_inmediata_liquidacion_de_los_a_f49e0e
    - Restriccion_no_incorporar_un_dividendo_o_cupon_que_se_reajuste_periodicamente_en_funcion_en__5625f6
    - Restriccion_no_podran_reconocerse_los_spe_como_garantes_admisibles__cap_3_1_13_c53b59
    - Restriccion_no_pueden_incluirse_en_esta_categoria_deudores_cuyas_obligaciones_hayan_sido_ref_e1de78
    - Restriccion_no_se_admite_el_prorrateo_de_aportes_a_un_fondo_de_garantia_entre_las_clases_o_t_1999a9
    - Restriccion_no_se_admite_la_compensacion_entre_posiciones_en_diferentes_productos_basicos_ni_d671bf
    - Restriccion_no_se_admitira_el_descalce_de_plazos_de_vencimiento_entre_la_exposicion_y_el_act_19fc99
    - Restriccion_no_se_admitiran_los_aportes_de_instrumentos_del_punto_8_6_3_cuando_no_se_verifiq_0ce2c7
    - Restriccion_no_se_computaran_los_conceptos_correspondientes_a_derivados_y_operaciones_de_fin_18c654
    - Restriccion_no_se_debe_prever_pago_de_ningun_tipo_en_concepto_de_capital_excepto_en_caso_de__dc40ce
    - Restriccion_no_se_deducen_participaciones_en_entidades_financieras_cuando_rigen_franquicias__f6650d
    - Restriccion_no_se_otorgara_reconocimiento_a_la_cobertura_del_riesgo_de_credito_cuando_ese_ef_16f8ba
    - Restriccion_no_se_puede_recurrir_a_financiacion_directa_o_indirecta_de_la_entidad_para_la_ca_2d5663
    - Restriccion_no_se_pueden_transferir_activos_en_situacion_de_incumplimiento_o_mora_ni_obligac_f87528
    - Restriccion_no_se_reconoce_la_cobertura_del_riesgo_de_credito_crc_que_tenga_un_plazo_de_venc_326952
    - Restriccion_no_se_reconocen_como_cobertura_del_riesgo_de_credito_otros_tipos_de_derivados_de_539691
    - Restriccion_obligacion_de_ingreso_y_o_liquidacion_del_contravalor_en_divisas_por_un_porcenta_354dd5
    - Restriccion_pagos_de_intereses_de_deudas_comerciales_por_la_importacion_de_bienes_y_servicio_5974d6
    - Restriccion_para_derivados_de_credito_de_enesimo_incumplimiento_con_n_mayor_que_1_no_se_perm_679c91
    - Restriccion_para_futuros_la_exclusion_procede_solo_si_los_nocionales_e_instrumentos_subyacen_e84105
    - Restriccion_para_la_porcion_de_la_exposicion_hasta_el_55_del_valor_del_inmueble_se_aplica_el_35c61f
    - Restriccion_para_la_porcion_de_la_exposicion_que_supera_el_55_del_valor_del_inmueble_se_apli_bbcc7e
    - Restriccion_para_la_porcion_del_apoyo_crediticio_que_supere_el_55_del_valor_del_inmueble_se__ea3cfc
    - Restriccion_para_las_entidades_del_grupo_a_la_reduccion_de_exigencia_se_calcula_como_el_20_d_450a5a
    - Restriccion_para_las_entidades_del_grupo_b_la_reduccion_de_exigencia_se_calcula_como_el_17_d_53bb61
    - Restriccion_para_las_entidades_del_grupo_c_la_reduccion_de_exigencia_se_calcula_como_el_14_d_a3c45b
    - Restriccion_para_operaciones_liquidadas_en_el_mercado_de_cambios_entre_el_16_09_05_y_10_11_1_3faec3
    - Restriccion_para_swaps_fras_y_forwards_cuando_la_proxima_fecha_de_reajuste_o_vencimiento_es__5cf58e
    - Restriccion_para_swaps_fras_y_forwards_cuando_la_proxima_fecha_de_reajuste_o_vencimiento_es__907aa5
    - Restriccion_para_swaps_fras_y_forwards_cuando_la_proxima_fecha_de_reajuste_o_vencimiento_es__c967fa
    - Restriccion_para_swaps_y_fras_la_tasa_de_referencia_de_posiciones_a_interes_variable_debe_se_2feaaf
    - Restriccion_partidas_contingentes_relacionadas_con_operaciones_comerciales_del_cliente_garan_1a1358
    - Restriccion_partidas_fuera_de_balance_que_refieren_a_compromisos_se_sujetan_al_menor_de_los__da643f
    - Restriccion_ponderador_de_riesgo_del_0_para_exposiciones_a_otros_estados_soberanos_o_sus_ban_ccdc8d
    - Restriccion_ponderador_de_riesgo_del_100_para_exposicion_a_titulos_publicos_emitidos_en_peso_b27a3e
    - Restriccion_ponderador_de_riesgo_del_100_para_exposiciones_a_empresas_no_clasificadas_en_cat_23645e
    - Restriccion_ponderador_de_riesgo_del_100_para_exposiciones_a_entes_del_sector_publico_no_fin_31aab8
    - Restriccion_ponderador_de_riesgo_del_100_para_exposiciones_a_entes_del_sector_publico_no_fin_5eeb6b
    - Restriccion_ponderador_de_riesgo_del_100_para_exposiciones_a_entes_del_sector_publico_no_fin_6daf8d
    - Restriccion_ponderador_de_riesgo_del_100_para_exposiciones_a_otros_estados_soberanos_o_sus_b_52a4bb
    - Restriccion_ponderador_de_riesgo_del_100_para_exposiciones_a_otros_estados_soberanos_o_sus_b_bb0420
    - Restriccion_ponderador_de_riesgo_del_130_para_exposiciones_por_financiacion_especializada_de_7c8bd7
    - Restriccion_ponderador_de_riesgo_del_150_para_exposicion_a_titulos_publicos_emitidos_en_peso_b1558b
    - Restriccion_ponderador_de_riesgo_del_150_para_exposiciones_a_entes_del_sector_publico_no_fin_1758ef
    - Restriccion_ponderador_de_riesgo_del_150_para_exposiciones_a_entidades_financieras_de_grado__594200
    - Restriccion_ponderador_de_riesgo_del_150_para_exposiciones_a_otros_estados_soberanos_o_sus_b_13adab
    - Restriccion_ponderador_de_riesgo_del_150_para_exposiciones_de_corto_plazo_a_entidades_financ_ee49cd
    - Restriccion_ponderador_de_riesgo_del_200_para_exposicion_a_titulos_publicos_emitidos_en_peso_134875
    - Restriccion_ponderador_de_riesgo_del_200_para_exposicion_a_titulos_publicos_emitidos_en_peso_a51432
    - Restriccion_ponderador_de_riesgo_del_20_para_exposicion_a_titulos_publicos_emitidos_en_pesos_02e7f4
    - Restriccion_ponderador_de_riesgo_del_20_para_exposiciones_a_entes_del_sector_publico_no_fina_a63a20
    - Restriccion_ponderador_de_riesgo_del_20_para_exposiciones_a_otros_estados_soberanos_o_sus_ba_bce9b4
    - Restriccion_ponderador_de_riesgo_del_20_para_exposiciones_con_garantia_hipotecaria_sobre_inm_dace50
    - Restriccion_ponderador_de_riesgo_del_20_para_exposiciones_de_corto_plazo_a_entidades_financi_f7265c
    - Restriccion_ponderador_de_riesgo_del_2_aplicable_a_la_exposicion_al_fondo_de_garantia_para_i_2da0d4
    - Restriccion_ponderador_de_riesgo_del_40_para_exposiciones_a_entidades_financieras_de_grado_a_03609b
    - Restriccion_ponderador_de_riesgo_del_50_para_exposicion_a_titulos_publicos_emitidos_en_pesos_d08ae2
    - Restriccion_ponderador_de_riesgo_del_50_para_exposiciones_a_entes_del_sector_publico_no_fina_052882
    - Restriccion_ponderador_de_riesgo_del_50_para_exposiciones_a_otros_estados_soberanos_o_sus_ba_382920
    - Restriccion_ponderador_de_riesgo_del_50_para_exposiciones_de_corto_plazo_a_entidades_financi_e3f06c
    - Restriccion_ponderador_de_riesgo_del_75_para_exposiciones_a_entidades_financieras_de_grado_b_49cb96
    - Restriccion_prohibicion_de_aplicar_cobertura_del_riesgo_de_credito_en_operaciones_de_financi_9ee29a
    - Restriccion_prohibicion_de_exclusion_o_compensacion_de_posiciones_en_diferentes_monedas_los__a7df8c
    - Restriccion_prohibicion_de_realizar_pagos_de_capital_e_intereses_de_endeudamientos_financier_03fe7e
    - Restriccion_se_admitiran_unicamente_calificaciones_globales_de_caracter_internacional_quedan_98560d
    - Restriccion_se_aplica_ponderador_de_riesgo_del_4_si_se_da_el_caso_del_anteultimo_parrafo_del_ae8f2e
    - Restriccion_se_aplicara_una_exigencia_adicional_equivalente_al_10_de_la_menor_de_las_posicio_372819
    - Restriccion_se_excluyen_de_los_activos_admitidos_como_garantia_las_estructuras_en_las_que_se_0ae936
    - Restriccion_se_permite_compensar_el_80_del_riesgo_especifico_del_lado_de_la_operacion_con_la_60ea29
    - Restriccion_se_prohibe_cobrar_comisiones_y_o_cargos_diferenciales_a_usuarios_con_dificultade_ab5085
    - Restriccion_se_prohibe_el_acceso_al_mercado_de_cambios_para_el_pago_de_deudas_y_otras_obliga_2e5b05
    - Restriccion_se_prohibe_la_liquidacion_de_operaciones_de_compraventa_de_titulos_valores_con_l_7f7856
    - Restriccion_se_prohibe_realizar_pagos_de_capital_e_intereses_de_endeudamientos_financieros_c_12edad
    - Restriccion_se_prohiben_clausulas_de_amortizacion_anticipada_en_una_titulizacion_de_facilida_8e6bf9
    - Restriccion_se_prohiben_clausulas_que_contemplen_aumentos_de_la_posicion_a_primera_perdida_r_3979d8
    - Restriccion_se_prohiben_clausulas_que_incrementen_el_costo_de_la_proteccion_crediticia_para__1122d9
    - Restriccion_se_prohiben_clausulas_que_incrementen_el_rendimiento_pagadero_a_partes_distintas_68a07d
    - Restriccion_se_prohiben_clausulas_que_obliguen_a_la_entidad_originante_a_alterar_las_exposic_8f4e04
    - Restriccion_se_prohiben_clausulas_que_permitan_la_extincion_de_la_proteccion_debido_al_deter_271448
    - Restriccion_se_prohiben_umbrales_por_debajo_de_los_cuales_no_se_active_la_proteccion_crediti_a976cf
    - Restriccion_se_requiere_contar_con_calificacion_internacional_de_riesgo_comprendida_en_la_ca_0440b2
    - Restriccion_se_requiere_la_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios__b3822a
    - Restriccion_se_requiere_previa_conformidad_del_bcra_antes_del_acceso_al_mercado_de_cambios_c_8a0212
    - Restriccion_se_utilizara_un_mpor_minimo_de_10_dias_para_calculo_de_exposiciones_a_ccp_por_op_fc5691
    - Restriccion_si_el_cliente_es_beneficiario_directo_del_decreto_277_22_el_valor_de_los_benefic_e67451
    - Restriccion_si_garantia_de_cliente_es_mantenida_por_ccp_sin_proteccion_contra_su_quiebra_se__d24a2a
    - Restriccion_si_se_verifican_refinanciaciones_en_condiciones_distintas_a_las_excepciones_sena_ec131d
    - Restriccion_solo_la_parte_de_las_reservas_que_este_sujeta_a_la_absorcion_de_perdidas_y_propo_5e4c0e
    - Restriccion_solo_se_reconocen_garantias_emitidas_o_proteccion_provista_en_derivados_de_credi_b955de
    - Restriccion_solo_se_reconocen_swaps_de_incumplimiento_crediticio_y_de_rendimiento_total_que__4a555c
    - Restriccion_sustitutos_crediticios_directos_garantias_generales_de_endeudamiento_cartas_de_c_fb65a2
    - Restriccion_swaps_de_monedas_y_tasas_de_interes_fras_forwards_de_moneda_y_futuros_de_tasa_de_7b40d5
    - Restriccion_ventas_de_activos_con_pacto_de_recompra_incluso_en_operaciones_de_pase_o_con_res_38bdb4
```

### S12 — FAIL

ERROR — Toda Excepcion tiene >=1 arista saliente exceptua o exceptua_obligacion.

**Resultado:** 222 Excepciones sin salida exceptua/exceptua_obligacion.

```
    - Excepcion_cuando_el_cliente_sea_un_vpu_adherido_al_rigi_que_declaro_hacer_uso_de_los_benef_28134e
    - Excepcion_cuando_el_cobro_de_los_servicios_o_venta_de_la_inversion_sea_percibido_en_moneda_8686cc
    - Excepcion_cuando_la_entidad_emplea_valor_actual_neto_para_la_gestion_de_posiciones_se_util_63cb6b
    - Excepcion_cuando_la_garantia_cubre_unicamente_el_capital_los_intereses_y_otros_pagos_no_cu_5c61e7
    - Excepcion_cuando_la_nacionalizacion_requiere_plazo_mayor_y_el_pago_se_concreta_conforme_a__474c21
    - Excepcion_cuando_los_fletes_corresponden_a_una_operacion_de_importacion_encuadrada_en_el_p_4d69f1
    - Excepcion_cuando_margenes_de_credito_por_lineas_especificas_se_excedan_no_se_consideran_re_407e41
    - Excepcion_cuando_se_han_imputado_cobros_de_exportaciones_y_o_aplicaciones_de_divisas_al_pe_631959
    - Excepcion_demoras_en_la_oficializacion_por_decisiones_del_importador_motivadas_en_cuestion_14903e
    - Excepcion_el_acceso_al_mercado_de_cambios_se_extiende_tambien_a_los_fideicomisos_constitui_a589fd
    - Excepcion_el_acceso_al_mercado_de_cambios_tambien_se_extiende_a_los_fideicomisos_constitui_31fb86
    - Excepcion_el_deudor_puede_reclasificarse_a_situacion_normal_cuando_se_observen_las_situaci_576e53
    - Excepcion_el_deudor_puede_reclasificarse_al_nivel_superior_en_situacion_normal_cuando_se_h_e511de
    - Excepcion_el_factor_de_1_5_no_se_aplica_cuando_cva_no_es_aplicable_en_exposiciones_con_ent_a1691b
    - Excepcion_el_mantenimiento_por_parte_de_la_cedente_de_la_administracion_de_las_exposicione_154e1a
    - Excepcion_el_margen_inicial_no_comprende_los_aportes_a_la_ccp_en_concepto_de_acuerdos_para_482ca5
    - Excepcion_el_plazo_de_dos_anos_desde_el_primer_ingreso_de_divisas_puede_computarse_como_pa_0e125d
    - Excepcion_el_plazo_de_dos_anos_desde_el_primer_ingreso_de_divisas_puede_computarse_como_pa_6e1f70
    - Excepcion_el_punto_3_16_3_no_aplica_a_clientes_que_sean_personas_humanas_residentes__ext_4_d9364f
    - Excepcion_el_punto_3_16_3_no_es_aplicable_para_clientes_que_sean_personas_humanas_resident_1b5e2b
    - Excepcion_el_regimen_de_equipaje_queda_exceptuado_del_seguimiento_de_negociaciones_de_divi_c923b3
    - Excepcion_el_regimen_de_exportacion_para_compensar_envios_con_deficiencias_queda_exceptuad_d81053
    - Excepcion_el_regimen_de_muestras_queda_exceptuado_del_seguimiento_de_permisos_de_embarque__aff595
    - Excepcion_el_regimen_de_pacotilla_queda_exceptuado_del_seguimiento_de_divisas_por_exportac_3e5aed
    - Excepcion_el_regimen_de_removido_queda_exceptuado_del_seguimiento_de_negociaciones_de_divi_ba43a2
    - Excepcion_el_requisito_complementario_para_egresos_no_aplica_cuando_el_vpu_accede_al_merca_4ad6fe
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_aplica_cuando_la_operacion_encuad_4a6a75
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_no_resultara_aplicable_cuando_se_cum_1d239f
    - Excepcion_el_requisito_de_conformidad_previa_del_bcra_para_acceso_al_mercado_de_cambios_no_f72214
    - Excepcion_el_requisito_de_no_realizar_el_pago_con_anterioridad_al_vencimiento_no_aplica_cu_2b736e
    - Excepcion_el_requisito_de_que_el_cliente_no_registre_situaciones_de_demora_no_sera_de_apli_564910
    - Excepcion_el_requisito_de_que_el_cliente_no_registre_situaciones_de_demora_no_sera_de_apli_797559
    - Excepcion_el_requisito_de_que_el_cliente_no_registre_situaciones_de_demora_no_sera_de_apli_9392a4
    - Excepcion_el_requisito_de_que_el_cliente_no_registre_situaciones_de_demora_no_sera_de_apli_d20a1a
    - Excepcion_el_tratamiento_de_exposicion_al_sector_publico_no_financiero_no_aplica_cuando_el_7992a0
    - Excepcion_excepcion_a_la_exigencia_de_conformidad_previa_del_bcra_para_acceso_al_mercado_d_795196
    - Excepcion_excepcion_a_la_exigencia_de_conformidad_previa_del_bcra_para_pagos_de_servicios__739ad0
    - Excepcion_excepcion_a_la_exigencia_de_ead_positiva_la_ead_de_un_conjunto_de_neteo_que_comp_ba3faf
    - Excepcion_excepcion_a_la_inclusion_de_exposiciones_del_spe_la_entidad_puede_excluirlas_del_ccf31e
    - Excepcion_excepcion_al_computo_de_montos_de_instrumentos_con_vinculacion_crediticia_no_se__57164a
    - Excepcion_excepcion_al_limite_del_40_cuando_por_un_monto_igual_o_superior_al_excedente_el__6bec98
    - Excepcion_excepcion_al_ponderador_minimo_del_20_conforme_a_lo_dispuesto_en_el_punto_5_3_1__afd5e2
    - Excepcion_excepcion_al_requisito_de_conformidad_previa_del_bcra_cuando_el_pago_de_interese_9dc914
    - Excepcion_excepcion_al_requisito_de_conformidad_previa_del_bcra_cuando_el_pago_de_interese_b27a7b
    - Excepcion_excepcion_de_la_obligacion_de_ingreso_y_o_liquidacion_por_la_totalidad_del_contr_6d2268
    - Excepcion_excepcion_de_la_obligacion_de_liquidacion_para_cobros_de_exportaciones_de_servic_55ffbf
    - Excepcion_excepcion_de_liquidacion_de_cobros_de_exportaciones_de_bienes_y_servicios_para_l_a4c243
    - Excepcion_exceptua_del_seguimiento_de_permisos_de_embarque_las_exportaciones_de_efectos_pe_2de14d
    - Excepcion_exceptua_el_requisito_de_conformidad_previa_del_bcra_para_el_acceso_al_mercado_d_0e351b
    - Excepcion_exclusion_de_tenencias_de_titulos_valores_suscriptos_para_ser_colocados_dentro_d_45c622
    - Excepcion_exencion_de_la_exigencia_de_capital_adicional_de_2_cuando_la_entidad_asume_la_po_02af66
    - Excepcion_exencion_de_la_exigencia_de_capital_adicional_de_2_cuando_la_entidad_mantiene_la_64807b
    - Excepcion_exencion_del_requisito_de_ingreso_de_divisas_para_exportaciones_al_area_franca_c_9731bb
    - Excepcion_exencion_del_seguimiento_de_ingreso_de_divisas_para_exportaciones_del_area_aduan_c391ff
    - Excepcion_garantia_de_cliente_mantenida_por_custodio_y_protegida_contra_quiebra_de_ccp_mie_1b71a1
    - Excepcion_garantia_de_miembro_compensador_efectivo_titulos_otros_activos_excesos_de_margen_f1677a
    - Excepcion_gastos_en_inmuebles_y_otros_activos_fijos_derivados_de_eventos_de_perdida_por_ri_3977b6
    - Excepcion_la_cancelacion_discrecional_de_dividendos_o_intereses_no_constituye_por_si_sola__360a9e
    - Excepcion_la_cancelacion_discrecional_de_dividendos_o_intereses_no_faculta_a_los_tenedores_f6fe9b
    - Excepcion_la_condicion_de_que_conste_en_el_permiso_de_embarque_la_ventaja_aduanera_exponot_936d9e
    - Excepcion_la_conformidad_previa_del_bcra_se_considera_cumplida_cuando_el_cliente_registra__7da372
    - Excepcion_la_constancia_de_aceptacion_de_la_nueva_entidad_libera_a_la_entidad_previa_de_su_7aebd3
    - Excepcion_la_declaracion_jurada_del_cliente_respecto_a_sus_tenencias_de_activos_externos_l_9a2ec8
    - Excepcion_la_exportacion_en_consignacion_queda_exceptuada_del_seguimiento_de_divisas_por_e_57f81c
    - Excepcion_la_incorporacion_de_creditos_en_periodos_de_rotacion_o_su_sustitucion_recompra_p_49376d
    - Excepcion_la_liquidacion_de_las_divisas_remitidas_a_la_entidad_local_por_la_contraparte_pa_ed793b
    - Excepcion_la_operacion_no_queda_comprendida_por_el_requisito_de_conformidad_previa_cuando__49ca9d
    - Excepcion_la_renta_obtenida_por_el_alquiler_a_no_residentes_de_inmuebles_ubicados_en_el_pa_d256a4
    - Excepcion_las_asistencias_crediticias_otorgadas_a_clientes_sin_asistencia_previa_no_seran__c12237
    - Excepcion_las_cajas_de_ahorros_en_pesos_cuando_se_encuentren_abiertas_quedan_exceptuadas_d_536eb1
    - Excepcion_las_concertaciones_y_cancelaciones_de_operaciones_de_futuros_en_mercados_regulad_d69f60
    - Excepcion_las_condiciones_de_no_anticipacion_de_vencimientos_y_no_realizacion_de_pagos_ant_bfa635
    - Excepcion_las_entidades_originantes_pueden_deducir_de_las_posiciones_de_titulizacion_ponde_af5378
    - Excepcion_las_entidades_pueden_considerar_como_operacion_garantizada_por_una_agencia_ofici_b711f8
    - Excepcion_las_exportaciones_a_zonas_francas_nacionales_quedan_exceptuadas_del_seguimiento__614b11
    - Excepcion_las_exportaciones_de_bienes_efectuadas_por_un_vpu_adherido_al_rigi_por_un_proyec_71be79
    - Excepcion_las_exportaciones_de_bienes_enviados_al_exterior_con_fines_promocionales_amparad_17c336
    - Excepcion_las_exportaciones_desde_el_territorio_nacional_continental_al_area_aduanera_espe_7e7921
    - Excepcion_las_exposiciones_a_instrumentos_previstas_en_el_punto_2_11_quedan_excluidas_de_l_761376
    - Excepcion_las_garantias_otorgadas_a_favor_del_bcra_y_por_obligaciones_directas_quedan_excl_93e113
    - Excepcion_las_inversiones_directas_en_el_exterior_no_forman_parte_de_la_posicion_general_d_bc8382
    - Excepcion_las_inversiones_en_acciones_estructuradas_cuyo_objeto_es_replicar_la_realidad_ec_b1f258
    - Excepcion_las_modificaciones_que_resulten_economicamente_mas_beneficiosas_para_el_usuario__526fa3
    - Excepcion_las_obligaciones_negociables_compradas_que_constituyen_emisiones_propias_quedan__ed3fd2
    - Excepcion_las_operaciones_aduaneras_correspondientes_al_regimen_de_franquicia_diplomatica__8c20c8
    - Excepcion_las_operaciones_de_reembarco_consignadas_mediante_los_subregimenes_re01_re04_re0_af26a1
    - Excepcion_las_operaciones_de_repatriacion_de_inversiones_de_no_residentes_y_otras_compras__06b419
    - Excepcion_las_operaciones_de_trasbordo_quedan_exceptuadas_del_seguimiento_de_negociaciones_953d1f
    - Excepcion_las_operaciones_pueden_mantener_el_tratamiento_de_qccp_durante_tres_meses_despue_1b6715
    - Excepcion_las_personas_juridicas_inscriptas_en_el_registro_nacional_de_beneficiarios_del_r_40c235
    - Excepcion_las_personas_juridicas_inscriptas_en_el_registro_nacional_de_beneficiarios_del_r_5d94f5
    - Excepcion_las_primas_por_opciones_de_compra_y_de_venta_tomadas_quedan_excluidas_de_las_fin_03237b
    - Excepcion_las_refinanciaciones_otorgadas_a_productores_agropecuarios_derivadas_de_la_aplic_6ad645
    - Excepcion_las_ventas_y_compras_a_termino_de_divisas_o_valores_externos_no_forman_parte_de__2bd0ac
    - Excepcion_los_activos_externos_de_terceros_en_custodia_no_forman_parte_de_la_posicion_gene_073141
    - Excepcion_los_creditos_frente_al_banco_central_de_la_republica_argentina_quedan_excluidos__748419
    - Excepcion_los_creditos_para_consumo_o_vivienda_quedan_exceptuados_de_la_cartera_comercial__956a9c
    - Excepcion_los_defectos_originados_en_el_computo_del_50_en_lugar_del_100_de_los_resultados__0ee001
    - Excepcion_los_demas_activos_locales_en_moneda_extranjera_no_forman_parte_de_la_posicion_ge_843db8
    - Excepcion_los_depositos_en_el_bcra_en_moneda_extranjera_en_cuentas_a_nombre_de_la_entidad__e04a8a
    - Excepcion_los_incisos_i_iii_y_iv_del_punto_10_3_2_1_quedan_reemplazados_por_requisitos_dis_ef5b0e
    - Excepcion_los_permisos_que_revistan_la_condicion_de_incumplido_en_gestion_de_cobro_no_sera_91c91a
    - Excepcion_los_sobregiros_en_cuenta_corriente_bancaria_que_excedan_margenes_acordados_o_sin_411236
    - Excepcion_no_aplica_el_plazo_maximo_de_diez_10_dias_habiles_cuando_i_se_trata_de_la_situac_6123a1
    - Excepcion_no_aplica_la_facultad_de_exclusion_cuando_las_cantidades_de_ingresos_y_egresos_f_a5ea17
    - Excepcion_no_aplican_los_requisitos_de_declaracion_jurada_de_los_puntos_3_16_3_1_a_3_16_3__6e9660
    - Excepcion_no_aplican_los_requisitos_de_declaracion_jurada_de_los_puntos_3_16_3_1_a_3_16_3__8c538c
    - Excepcion_no_aplican_los_requisitos_de_declaracion_jurada_de_los_puntos_3_16_3_1_a_3_16_3__9fa252
    - Excepcion_no_aplican_los_requisitos_de_declaracion_jurada_de_los_puntos_3_16_3_1_a_3_16_3__e1d560
    - Excepcion_no_es_necesaria_la_presentacion_de_declaracion_jurada_por_parte_de_entes_del_sec_1e688a
    - Excepcion_no_es_obligatoria_evaluacion_de_capacidad_de_pago_por_ingresos_del_prestatario_c_51b967
    - Excepcion_no_es_obligatoria_la_apertura_del_legajo_en_los_casos_de_deudores_por_servicios__1fee27
    - Excepcion_no_es_obligatorio_incorporar_flujo_de_fondos_estados_contables_ni_informacion_pa_b350ee
    - Excepcion_no_es_requisito_que_una_ecai_evalue_empresas_en_mas_de_un_pais_para_ser_reconoci_327dba
    - Excepcion_no_resulta_aplicable_el_requisito_de_verificacion_de_la_fecha_de_vencimiento_del_902a1f
    - Excepcion_no_resultan_aplicables_los_requisitos_de_los_puntos_4_3_2_1_y_4_3_2_2_en_las_com_c4da8f
    - Excepcion_no_resultara_aplicable_el_requisito_de_conformidad_previa_del_bcra_cuando_se_tra_908c0e
    - Excepcion_no_se_aplica_el_plazo_minimo_de_20_dias_habiles_para_calculo_de_mpor_en_conjunto_55c988
    - Excepcion_no_se_clasifican_en_la_categoria_irrecuperable_los_deudores_cuando_las_financiac_b48e28
    - Excepcion_no_se_considera_refinanciacion_la_asistencia_a_deudores_en_situacion_normal_que__62369c
    - Excepcion_no_se_consideran_activos_externos_liquidos_disponibles_los_fondos_depositados_en_5cc339
    - Excepcion_no_se_consideran_en_el_computo_las_exportaciones_a_consumo_con_despacho_de_impor_06995e
    - Excepcion_no_se_consideran_en_el_computo_los_bienes_exportados_a_traves_de_operaciones_exc_17098a
    - Excepcion_no_se_consideran_en_el_computo_los_bienes_que_cuenten_con_las_ventajas_aduaneras_b40852
    - Excepcion_no_se_consideran_refinanciaciones_las_otorgadas_a_productores_cuando_resulten_de_59f60f
    - Excepcion_no_se_incluyen_los_ingresos_de_importaciones_temporarias_sin_giro_de_divisas_en__2f0aae
    - Excepcion_no_se_incluyen_los_registros_aduaneros_por_importaciones_suspensivas_de_deposito_37c1f3
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_cuando_el_cliente_es_un_vpu_adherido__7613fb
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_para_el_acceso_al_mercado_de_cambios__28d5ad
    - Excepcion_no_se_requiere_conformidad_previa_del_bcra_si_el_deudor_encuadra_en_alguna_de_la_642184
    - Excepcion_no_se_requiere_la_conformidad_previa_del_bcra_si_tal_requisito_estuviese_vigente_d1ad37
    - Excepcion_no_sera_aplicable_lo_dispuesto_en_el_articulo_197_de_la_ley_general_de_sociedade_b1a072
    - Excepcion_no_sera_exigible_la_liquidacion_en_el_mercado_de_cambios_de_fondos_en_moneda_ext_11e2d9
    - Excepcion_operacion_aduanera_exceptuada_del_seguimiento_de_divisas_por_exportaciones_de_bi_d09dfb
    - Excepcion_operacion_aduanera_exceptuada_del_seguimiento_de_permiso_de_embarque_por_el_valo_7a63d9
    - Excepcion_operacion_aduanera_exceptuada_del_seguimiento_de_permisos_de_embarque_por_el_reg_3f0d8c
    - Excepcion_operacion_exceptuada_del_seguimiento_de_divisas_por_exportaciones_de_bienes_por__6c3e8d
    - Excepcion_operacion_exceptuada_del_seguimiento_de_divisas_por_exportaciones_exportacion_a__11a101
    - Excepcion_operacion_exceptuada_del_seguimiento_de_permisos_de_embarque_por_el_valor_que_co_526246
    - Excepcion_operacion_exceptuada_del_seguimiento_de_permisos_de_embarque_por_el_valor_que_co_a2b7b5
    - Excepcion_operaciones_de_envios_de_asistencia_y_salvamento_quedan_exceptuadas_del_seguimie_9a7b16
    - Excepcion_para_exposiciones_subyacentes_a_operaciones_con_derivados_realizadas_por_el_fond_bd73d5
    - Excepcion_para_financiaciones_otorgadas_a_partir_del_14_04_25_se_admite_que_el_vencimiento_fd8077
    - Excepcion_para_modificaciones_en_los_valores_de_comisiones_y_o_cargos_debidamente_aceptado_be2e4c
    - Excepcion_para_operaciones_comprendidas_en_el_punto_7_11_1_6_se_admite_la_cancelacion_de_i_cfcb67
    - Excepcion_para_operaciones_del_concepto_s30_servicios_de_fletes_por_operaciones_de_importa_097d85
    - Excepcion_provisiones_relacionadas_con_eventos_de_perdidas_por_riesgo_operacional_si_contr_d394cd
    - Excepcion_queda_exceptuada_la_condicion_prevista_en_el_inciso_viii_del_punto_10_3_2_1_para_2af89a
    - Excepcion_queda_exceptuada_la_exigencia_de_conformidad_previa_del_bcra_para_el_acceso_al_m_925684
    - Excepcion_quedan_exceptuadas_de_la_clasificacion_de_financiaciones_las_compras_a_termino_p_d8cf5c
    - Excepcion_quedan_exceptuadas_de_la_clasificacion_las_garantias_otorgadas_a_favor_del_banco_6b6ab5
    - Excepcion_quedan_exceptuadas_de_la_exigencia_de_conformidad_previa_del_bcra_las_operacione_685962
    - Excepcion_quedan_exceptuadas_del_alcance_de_las_garantias_comprendidas_las_garantias_otorg_b97cd3
    - Excepcion_quedan_exceptuadas_del_alcance_de_las_normas_sobre_proveedores_no_financieros_de_f8a3ba
    - Excepcion_quedan_exceptuadas_del_plazo_de_60_dias_las_exportaciones_de_las_posiciones_aran_61ca34
    - Excepcion_quedan_exceptuadas_del_plazo_de_60_dias_las_exportaciones_de_las_posiciones_aran_7c43a6
    - Excepcion_quedan_exceptuadas_del_requisito_de_conformidad_previa_del_bcra_las_transferenci_11f54f
    - Excepcion_quedan_exceptuadas_del_seguimiento_las_exportaciones_a_consumo_de_bienes_excluid_91dc80
    - Excepcion_quedan_exceptuadas_del_seguimiento_las_exportaciones_a_consumo_de_bienes_que_con_0cdfce
    - Excepcion_quedan_exceptuadas_del_seguimiento_las_operaciones_aduaneras_correspondientes_al_02b73f
    - Excepcion_quedan_exceptuadas_del_seguimiento_las_operaciones_aduaneras_de_los_subregimenes_cb964d
    - Excepcion_quedan_exceptuadas_del_seguimiento_las_operaciones_aduaneras_detalladas_en_el_pu_755ad7
    - Excepcion_quedan_exceptuadas_del_seguimiento_las_operaciones_aduaneras_realizadas_mediante_7283c7
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_20_10_realizadas_po_681e4e
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_20_21_realizadas_po_935cb3
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_20_22_realizadas_po_d82fde
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_20_90_realizadas_po_ef78aa
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_30_10_realizadas_po_b41efb
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_30_21_realizadas_po_204741
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_30_29_realizadas_po_a6f183
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_30_31_realizadas_po_40a657
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_30_39_realizadas_po_cd1aa8
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_30_90_realizadas_po_09bc83
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_40_10_realizadas_po_486382
    - Excepcion_quedan_exceptuadas_las_importaciones_de_la_posicion_ncm_8802_40_90_realizadas_po_e049d8
    - Excepcion_quedan_exceptuados_de_esta_condicion_los_deudores_comprendidos_en_el_punto_6_5_2_0a6ac9
    - Excepcion_quedan_exceptuados_de_la_clasificacion_de_deudores_los_anticipos_por_pago_de_jub_393494
    - Excepcion_quedan_exceptuados_de_la_clasificacion_de_deudores_los_anticipos_y_prestamos_al__ea5289
    - Excepcion_quedan_exceptuados_de_la_clasificacion_de_deudores_los_deudores_por_pases_activo_4242cf
    - Excepcion_quedan_exceptuados_de_la_clasificacion_en_irrecuperable_los_deudores_en_concurso_e0afc3
    - Excepcion_quedan_exceptuados_de_la_obligacion_de_liquidacion_los_cobros_de_exportaciones_d_5097bc
    - Excepcion_quedan_exceptuados_de_la_obligacion_de_liquidacion_los_cobros_de_exportaciones_d_62ea28
    - Excepcion_quedan_exceptuados_de_la_obligacion_de_liquidacion_los_cobros_de_exportaciones_d_67a0b7
    - Excepcion_quedan_exceptuados_de_la_obligacion_de_liquidacion_los_cobros_de_exportaciones_d_697ee1
    - Excepcion_quedan_exceptuados_de_los_requisitos_de_anterioridad_y_plazo_minimo_desde_emisio_274e7c
    - Excepcion_quedan_exceptuados_del_requisito_de_conformidad_previa_los_pagos_de_intereses_co_c5d782
    - Excepcion_quedan_exceptuados_del_requisito_de_demostrar_ingreso_y_liquidacion_de_divisas_e_8a218a
    - Excepcion_quedan_excluidas_de_la_exigencia_de_capital_por_riesgo_de_credito_de_contraparte_6a7c99
    - Excepcion_quedan_excluidas_de_las_exposiciones_minoristas_las_exposiciones_con_garantia_hi_701361
    - Excepcion_quedan_excluidas_de_los_conceptos_comprendidos_las_posiciones_en_acciones_en_la__1d53cf
    - Excepcion_quedan_excluidas_del_alcance_de_este_punto_las_exposiciones_previstas_en_el_punt_5bd492
    - Excepcion_quedan_excluidas_del_computo_de_la_exigencia_de_capital_las_operaciones_de_pase__3b2a22
    - Excepcion_quedan_excluidos_de_la_definicion_de_divisas_en_moneda_extranjera_las_monedas_y__2658b5
    - Excepcion_quedan_excluidos_de_los_conceptos_comprendidos_los_activos_fijos__ric_11_1_9495fe
    - Excepcion_quedan_excluidos_de_los_conceptos_comprendidos_los_activos_que_se_deducen_del_ca_690cfb
    - Excepcion_se_admite_computar_el_valor_de_los_fletes_no_incluidos_en_la_condicion_de_compra_9b6f8a
    - Excepcion_se_admite_la_constitucion_de_garantias_en_cuentas_abiertas_en_entidades_financie_4dccaf
    - Excepcion_se_aplicara_un_ponderador_del_10_a_entidades_del_exterior_que_no_cumplan_con_lo__0482b5
    - Excepcion_se_considera_como_operacion_garantizada_por_agencia_oficial_de_credito_aquella_c_0cb920
    - Excepcion_se_exceptua_del_requisito_de_conformidad_previa_del_bcra_cuando_el_deudor_encuad_a23a55
    - Excepcion_se_exceptua_del_requisito_de_demostrar_ingreso_y_liquidacion_de_divisas_en_el_me_e2dc16
    - Excepcion_se_exceptua_el_requisito_de_cumplimiento_de_los_requisitos_establecidos_para_el__f53f5c
    - Excepcion_se_exceptua_la_exigencia_de_conformidad_previa_del_bcra_para_acceso_al_mercado_d_b49855
    - Excepcion_se_exceptua_la_exigencia_de_que_todos_los_bienes_sean_bienes_de_capital_cuando_l_7fbc72
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_la_asistencia_crediticia_conced_3867e8
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_la_casa_matriz_de_las_sucursale_7c8053
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_las_financiaciones_que_cuenten__9fe9db
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_las_financiaciones_vinculadas_a_6a7a2f
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_las_financiaciones_vinculadas_a_d63b84
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_las_sucursales_y_subsidiarias_d_15cc52
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_los_bancos_u_otras_institucione_808f11
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_los_pases_activos_de_dolares_es_c15c53
    - Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_otros_bancos_del_exterior_autor_9645c8
    - Excepcion_se_excluyen_los_casos_en_que_las_acciones_judiciales_se_refieren_a_la_discusion__cd1dc1
    - Excepcion_se_permite_emitir_certificaciones_por_la_porcion_no_liquidada_de_operaciones_del_42b5e8
    - Excepcion_se_permite_que_exista_descalce_entre_los_plazos_de_vencimiento_de_la_posicion_su_716bf8
    - Excepcion_se_permite_reconocimiento_parcial_del_derivado_de_credito_cuando_la_reestructura_9395d7
    - Excepcion_se_podra_excluir_del_computo_de_la_exigencia_de_capital_por_riesgo_general_de_me_a4468e
    - Excepcion_se_pueden_excluir_las_posiciones_opuestas_por_el_mismo_importe_en_una_misma_espe_40c628
    - Excepcion_se_pueden_excluir_los_derivados_swaps_forwards_futuros_y_fras_estrechamente_rela_3228ae
    - Excepcion_se_reduce_la_exigencia_para_entidades_financieras_del_grupo_2_que_pertenezcan_a__f0d76b
    - Excepcion_sera_aplicable_la_excepcion_prevista_en_el_punto_14_1_3_para_clientes_vpu_adheri_44947b
```

### S21 — WARN

INFORMATIVA — Coherencia de remisiones entre puntos (remite_a o referencia con rol_fuente=referencia_cruzada; scripts/remisiones.py): properties.destino sin el prefijo <to>:: pertenece al CONJUNTO {p.punto for p in provenances} del nodo destino; desglose por properties.alcance (las de alcance to_entero apuntan al TextoOrdenado y se cuentan como incoherentes por construcción del enunciado).

**Resultado:** 11374 remisiones ({'interna': 10933, 'externa': 425, 'to_entero': 16}); 16 incoherentes (por alcance: {'to_entero': 16}).

```
idx 3405: Condicion_incremento_cartera_irregular_10_anual__el_cociente_de_financiaciones_irregulares_e74074 -> TextoOrdenado_to_clasificacion_deudores_actual_pdf destino='cla::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '10.1', '10.2.1']...
idx 3408: Condicion_incremento_cartera_irregular_5_trimestral__el_cociente_de_financiaciones_irregul_dc90da -> TextoOrdenado_to_clasificacion_deudores_actual_pdf destino='cla::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '10.1', '10.2.1']...
idx 6375: Definicion_codigo_70810000_exigencia_metodologia_anterior__exigencia_por_riesgo_de_mercado__4d9360 -> TextoOrdenado_to_capitales_minimos_actual_pdf destino='cap::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.4.1']...
idx 6792: Definicion_ficc_cociente_cartera_irregular_entidad__cociente_expresado_en_porcentaje_entre__39ffc2 -> TextoOrdenado_to_clasificacion_deudores_actual_pdf destino='cla::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '10.1', '10.2.1']...
idx 6794: Definicion_ficcs_cociente_cartera_irregular_sistema__cociente_expresado_en_porcentaje_entre_2e3d31 -> TextoOrdenado_to_clasificacion_deudores_actual_pdf destino='cla::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '10.1', '10.2.1']...
idx 6966: Definicion_normas_sobre_proteccion_de_usuarios_caracter_complementario__son_complementarias_98bbe6 -> TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf destino='pro::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 7029: Definicion_operadores_de_cambio_sujetos_obligados__sujetos_obligados_a_cumplir_las_normas_d_8ed1f1 -> TextoOrdenado_to_exterior_cambios_actual_pdf destino='ext::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.5']...
idx 7249: Definicion_t_1_trimestres_anteriores_de_referencia__el_ultimo_dia_del_trimestre_calendario__35ffcd -> TextoOrdenado_to_clasificacion_deudores_actual_pdf destino='cla::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '10.1', '10.2.1']...
idx 7251: Definicion_t_ultimo_dia_trimestre_calendario__el_ultimo_dia_de_un_trimestre_calendario_al_q_2efb33 -> TextoOrdenado_to_clasificacion_deudores_actual_pdf destino='cla::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '10.1', '10.2.1']...
idx 11542: Obligacion_la_entidad_financiera_debe_informar_a_la_sefyc_el_origen_del_incremento_de_la_ca_a325e0 -> TextoOrdenado_to_clasificacion_deudores_actual_pdf destino='cla::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '10.1', '10.2.1']...
idx 11553: Obligacion_la_entidad_financiera_debe_presentar_cuando_corresponda_las_modificaciones_a_su__803fd4 -> TextoOrdenado_to_clasificacion_deudores_actual_pdf destino='cla::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '10.1', '10.2.1']...
idx 11556: Obligacion_la_entidad_financiera_debe_proporcionar_las_explicaciones_que_la_sefyc_requiera__e5a41c -> TextoOrdenado_to_clasificacion_deudores_actual_pdf destino='cla::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '10.1', '10.2.1']...
idx 11942: Obligacion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_se_determinara_ten_b9cec2 -> TextoOrdenado_to_capitales_minimos_actual_pdf destino='cap::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.4.1']...
idx 11993: Obligacion_la_informacion_debera_incluir_la_clasificacion_promedio_de_los_deudores_conforme_42c267 -> TextoOrdenado_to_clasificacion_deudores_actual_pdf destino='cla::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '10.1', '10.2.1']...
idx 14928: Operacion_admision_de_activos_como_garantia_metodo_simple__cap_5_3_1_2_f5db38 -> TextoOrdenado_to_exterior_cambios_actual_pdf destino='ext::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.5']...
idx 18290: Operacion_tenencia_de_oro_amonedado_o_en_barras_de_buena_entrega__cap_2_12_1_3_134e48 -> TextoOrdenado_to_exterior_cambios_actual_pdf destino='ext::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.3', '1.4', '1.5']...
```

### S22 — PASS

INFORMATIVA — Coherencia de padre_sugerido: el destino de la arista es properties.padre_sugerido del origen y el origen está en cuarentena.

**Resultado:** 66 aristas padre_sugerido; 0 incoherentes (0 con destino distinto, 0 con origen fuera de cuarentena).

Sin violaciones.

### S23 — WARN

INFORMATIVA — aplica_a hacia sujetos en cuarentena: aristas aplica_a cuyo destino es un Sujeto de nivel propuesto (conteo; nunca bloqueante).

**Resultado:** 1770 aristas aplica_a; 110 hacia Sujetos propuestos (64 destinos distintos).

```
idx 7405: Excepcion_cuando_la_entidad_es_notificada_a_traves_de_secoexpo_sobre_su_responsabilidad_en_f4501e -> Sujeto_propuesto_la_entidad__ext
idx 8719: Obligacion_activos_constituidos_en_garantia_estan_sujetos_al_requisito_de_riesgo_de_credito_53c52c -> Sujeto_propuesto_los_activos_constituidos_en_garantia
idx 8812: Obligacion_al_momento_de_la_aplicacion_de_los_fondos_adquiridos_se_debe_efectuar_un_boleto__10ac24 -> Sujeto_propuesto_la_entidad__ext
idx 8814: Obligacion_ambas_partes_documentante_y_propietario_de_la_mercaderia_son_responsables_del_cu_c81efd -> Sujeto_propuesto_ambas_partes_documentante_y_propietario_de_la_mercaderia
idx 8852: Obligacion_auditoria_anual_del_servicio_de_atencion_al_usuario__pro_3_2_1_3_07bd95 -> Sujeto_propuesto_la_auditoria_interna
idx 8912: Obligacion_con_respecto_a_los_creditos_que_se_asignen_a_los_tramos_i_y_ii_de_los_margenes_a_c54507 -> Sujeto_propuesto_el_prestatario
idx 9038: Obligacion_cuando_el_exportador_solicita_cambiar_la_entidad_responsable_del_seguimiento_la__a32e28 -> Sujeto_propuesto_la_entidad_a_cargo_del_seguimiento
idx 9062: Obligacion_cuando_la_adquisicion_de_titulos_valores_se_ha_concretado_con_liquidacion_en_el__c7447a -> Sujeto_propuesto_la_entidad_que_curso_la_operacion_de_canje_y_o_arbitraje
idx 9082: Obligacion_cuando_la_financiacion_es_otorgada_por_entidades_financieras_locales_el_seguimie_035c38 -> Sujeto_propuesto_la_entidad_que_otorgo_la_financiacion
idx 9084: Obligacion_cuando_la_importacion_encuadre_en_los_puntos_10_3_3_10_9_1_10_9_2_y_10_9_3_la_en_742af9 -> Sujeto_propuesto_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente
idx 9134: Obligacion_cuando_la_utilizacion_de_los_mecanismos_del_punto_7_9_redunde_en_un_monto_que_ex_c984af -> Sujeto_propuesto_la_entidad_encargada_del_seguimiento
idx 9143: Obligacion_cuando_los_activos_se_constituyen_en_garantia_de_una_cuenta_con_operaciones_sft__a30ac9 -> Sujeto_propuesto_el_miembro_o_cliente
idx 9199: Obligacion_cuando_se_trate_de_operaciones_destinadas_a_los_proyectos_comprendidos_en_el_pun_2421cb -> Sujeto_propuesto_la_entidad_encargada_del_seguimiento
idx 9252: Obligacion_dar_cumplimiento_en_su_presentacion_a_los_recaudos_pertinentes_del_punto_4_2_1___262857 -> Sujeto_propuesto_la_asociacion_denunciante
idx 9347: Obligacion_deber_de_considerar_lo_dispuesto_en_el_punto_3_1_12_cuando_se_trate_de_una_entid_4ab0ea -> Sujeto_propuesto_una_entidad_originante
idx 9640: Obligacion_el_beneficiario_debe_nominar_una_unica_entidad_financiera_local_que_sera_respons_ddc935 -> Sujeto_propuesto_el_beneficiario
idx 9644: Obligacion_el_boleto_de_cambio_debe_constar_con_el_caracter_de_declaracion_jurada_del_orden_242afb -> Sujeto_propuesto_el_ordenante_de_la_operacion_de_cambio
idx 9655: Obligacion_el_boleto_debe_constar_con_la_firma_del_cliente_que_realiza_la_operacion_de_camb_1e82ba -> Sujeto_propuesto_el_cliente_que_realiza_la_operacion_de_cambio
idx 9869: Obligacion_el_ingreso_y_liquidacion_de_divisas_por_el_mercado_de_cambios_debera_concretarse_507384 -> Sujeto_propuesto_los_exportadores
idx 9955: Obligacion_el_proveedor_de_proteccion_debe_calcular_su_exigencia_de_capital_como_si_mantuvi_4f3c57 -> Sujeto_propuesto_el_proveedor_de_proteccion
idx 9979: Obligacion_el_registro_de_un_ingreso_sera_responsabilidad_de_la_entidad_interviniente_en_la_949b00 -> Sujeto_propuesto_la_entidad_interviniente_en_la_operacion
idx 10429: Obligacion_en_titulizaciones_tradicionales_con_opcion_de_exclusion_incompleta_las_exposicio_5c4553 -> Sujeto_propuesto_las_exposiciones_subyacentes
idx 10438: Obligacion_en_todos_los_casos_en_que_se_considere_una_operacion_garantizada_por_una_asegura_c347fe -> Sujeto_propuesto_la_entidad_interviniente
idx 10808: Obligacion_la_asociacion_denunciante_debera_acreditar_su_condicion_de_entidad_reconocida__p_ec03f1 -> Sujeto_propuesto_la_asociacion_denunciante
idx 10810: Obligacion_la_auditoria_interna_debe_verificar_que_las_comisiones_y_cargos_aplicados_a_los__335271 -> Sujeto_propuesto_la_auditoria_interna
idx 10812: Obligacion_la_auditoria_interna_debe_verificar_que_los_registros_centralizados_de_consultas_ab8aa0 -> Sujeto_propuesto_la_auditoria_interna
idx 10814: Obligacion_la_auditoria_interna_debe_verificar_que_se_ha_notificado_a_los_usuarios_en_el_co_3d227e -> Sujeto_propuesto_la_auditoria_interna
idx 10816: Obligacion_la_auditoria_interna_debe_verificar_que_se_ha_notificado_a_los_usuarios_en_el_cu_747cb6 -> Sujeto_propuesto_la_auditoria_interna
idx 10818: Obligacion_la_auditoria_interna_debe_verificar_que_se_proporciona_a_los_usuarios_copia_de_l_907551 -> Sujeto_propuesto_la_auditoria_interna
idx 10830: Obligacion_la_cartera_de_negociacion_debera_ser_gestionada_de_forma_activa__cap_6_1_2_1_ba64df -> Sujeto_propuesto_la_cartera
idx 10835: Obligacion_la_certificacion_emitida_por_la_entidad_encargada_del_seguimiento_de_la_oficiali_cb52c3 -> Sujeto_propuesto_la_entidad_encargada_del_seguimiento_de_la_oficializacion_de_importacion
idx 10839: Obligacion_la_certificacion_presentada_en_el_bcra_debe_incluir_como_minimo_detalle_del_punt_5b0d80 -> Sujeto_propuesto_la_entidad__ext
idx 10847: Obligacion_la_circunstancia_de_que_la_capitalizacion_esta_ad_referendum_de_aprobacion_deber_afd416 -> Sujeto_propuesto_la_asamblea_o_autoridad_equivalente
idx 10857: Obligacion_la_compensacion_a_los_tenedores_de_estos_instrumentos_por_la_quita_realizada_deb_0fe053 -> Sujeto_propuesto_los_tenedores_de_estos_instrumentos
idx 10862: Obligacion_la_decision_de_capitalizacion_de_los_conceptos_indicados_en_los_puntos_8_6_1_a_8_321b07 -> Sujeto_propuesto_la_asamblea_o_autoridad_equivalente
idx 10868: Obligacion_la_decision_de_capitalizacion_de_los_conceptos_indicados_en_los_puntos_8_6_1_a_8_78ce2f -> Sujeto_propuesto_la_asamblea_o_autoridad_equivalente
idx 10905: Obligacion_la_devolucion_de_las_certificaciones_no_utilizadas_sera_efectuada_entre_las_enti_0063e2 -> Sujeto_propuesto_las_entidades_involucradas
idx 10930: Obligacion_la_documentacion_utilizada_por_la_entidad_financiera_y_hojas_de_trabajo_que_aval_5ca0a9 -> Sujeto_propuesto_la_entidad__ext
idx 10946: Obligacion_la_entidad_a_cargo_del_seguimiento_debe_exigir_una_declaracion_jurada_sobre_el_c_5453ec -> Sujeto_propuesto_la_entidad_a_cargo_del_seguimiento
idx 10948: Obligacion_la_entidad_a_cargo_del_seguimiento_debe_incorporar_en_el_sepaimpo_los_registros__7d9807 -> Sujeto_propuesto_la_entidad_a_cargo_del_seguimiento
idx 10955: Obligacion_la_entidad_a_cargo_del_seguimiento_debe_notificar_a_la_nueva_entidad_la_voluntad_e09e50 -> Sujeto_propuesto_la_entidad_a_cargo_del_seguimiento
idx 10959: Obligacion_la_entidad_a_cargo_del_seguimiento_debera_considerar_como_utilizada_toda_certifi_4429d9 -> Sujeto_propuesto_la_entidad_a_cargo_del_seguimiento
idx 11036: Obligacion_la_entidad_debe_contar_con_una_declaracion_jurada_del_cliente_en_la_que_conste_q_1a3040 -> Sujeto_propuesto_la_entidad__ext
idx 11064: Obligacion_la_entidad_debe_intervenir_en_la_operacion_dejando_constancia_de_la_fecha_y_mont_e676fc -> Sujeto_propuesto_la_entidad__ext
idx 11072: Obligacion_la_entidad_debe_realizar_la_correspondiente_intervencion_de_la_documentacion_adu_fc829f -> Sujeto_propuesto_la_entidad__ext
idx 11075: Obligacion_la_entidad_debe_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_importador_po_42a8cd -> Sujeto_propuesto_la_mencionada_entidad
idx 11088: Obligacion_la_entidad_debe_remitir_adicionalmente_la_certificacion_del_cumplimiento_de_cond_bc636d -> Sujeto_propuesto_la_entidad__ext
idx 11092: Obligacion_la_entidad_debe_solicitar_los_dictamenes_profesionales_que_estime_necesarios_par_76f50d -> Sujeto_propuesto_la_entidad__ext
idx 11298: Obligacion_la_entidad_debera_presentar_descargo_en_el_plazo_de_5_dias_habiles_conforme_a_lo_6fb9fc -> Sujeto_propuesto_la_entidad
idx 11340: Obligacion_la_entidad_debera_regularizar_el_incumplimiento_en_la_forma_prevista_en_el_punto_8fab6a -> Sujeto_propuesto_la_entidad
idx 11404: Obligacion_la_entidad_encargada_del_seguimiento_de_anticipos_y_otras_financiaciones_de_expo_d0dad1 -> Sujeto_propuesto_la_entidad_encargada_del_seguimiento_de_anticipos_y_otras_financiaciones_de_expo
idx 11406: Obligacion_la_entidad_encargada_del_seguimiento_de_la_oficializacion_del_despacho_de_import_46c5a3 -> Sujeto_propuesto_la_entidad_encargada_del_seguimiento_de_la_oficializacion_del_despacho_de_import
idx 11410: Obligacion_la_entidad_encargada_del_seguimiento_de_la_prefinanciacion_cancelada_debe_regist_ab62b2 -> Sujeto_propuesto_la_entidad_encargada_del_seguimiento_de_la_prefinanciacion_cancelada
idx 11416: Obligacion_la_entidad_encargada_del_seguimiento_debe_realizar_la_denuncia_de_incumplido_cua_2d9ddc -> Sujeto_propuesto_la_entidad_encargada_del_seguimiento
idx 11418: Obligacion_la_entidad_encargada_del_seguimiento_debe_realizar_la_denuncia_dentro_de_los_10__b56486 -> Sujeto_propuesto_la_entidad__ext
idx 11420: Obligacion_la_entidad_encargada_del_seguimiento_debe_reportar_cuando_otorgue_extensiones_de_3305df -> Sujeto_propuesto_la_entidad_encargada_del_seguimiento
idx 11437: Obligacion_la_entidad_encargada_del_seguimiento_debera_remitir_al_bcra_la_certificacion_de__339ea6 -> Sujeto_propuesto_la_entidad_encargada_del_seguimiento
idx 11447: Obligacion_la_entidad_encargada_del_seguimiento_del_pago_con_registro_de_ingreso_aduanero_p_fcb753 -> Sujeto_propuesto_la_entidad_encargada_del_seguimiento_del_pago_con_registro_de_ingreso_aduanero_p
idx 11449: Obligacion_la_entidad_encargada_del_seguimiento_del_pago_debe_considerar_los_tipos_de_pase__fd7018 -> Sujeto_propuesto_la_entidad_encargada_del_seguimiento_del_pago
idx 11656: Obligacion_la_entidad_interviniente_debe_contar_con_una_certificacion_de_la_entidad_encarga_20da6c -> Sujeto_propuesto_la_entidad_interviniente
idx 11724: Obligacion_la_entidad_nominada_debera_emitir_a_pedido_del_importador_certificaciones_con_el_f99c5c -> Sujeto_propuesto_la_entidad_nominada
idx 11764: Obligacion_la_entidad_nominada_es_la_unica_responsable_de_emitir_los_certificados_de_aplica_9fd09e -> Sujeto_propuesto_esta_entidad
idx 11767: Obligacion_la_entidad_nominada_por_el_exportador_debe_incorporar_la_operacion_al_seguimient_28ac80 -> Sujeto_propuesto_la_entidad_nominada_por_el_exportador
idx 11826: Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_debe_contar_con_una_declaracion_fe303d -> Sujeto_propuesto_la_entidad_que_concrete_la_oferta_de_suscripcion
idx 11830: Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debe_cont_460149 -> Sujeto_propuesto_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente
idx 11832: Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debe_cont_69bc3c -> Sujeto_propuesto_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente
idx 11856: Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debe_cont_6f147c -> Sujeto_propuesto_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente
idx 11859: Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debe_cont_f17172 -> Sujeto_propuesto_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente
idx 11861: Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debe_veri_13f6d3 -> Sujeto_propuesto_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente
idx 11889: Obligacion_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente_debera_ve_cd8203 -> Sujeto_propuesto_la_entidad_que_concrete_la_oferta_de_suscripcion_en_nombre_del_cliente
idx 11895: Obligacion_la_entidad_que_interviene_adicionalmente_debera_considerar_los_siguientes_elemen_876c3c -> Sujeto_propuesto_la_entidad_que_interviene_adicionalmente
idx 11897: Obligacion_la_entidad_que_interviene_adicionalmente_debera_presentar_copia_de_la_solicitud__49a4f5 -> Sujeto_propuesto_la_entidad_que_interviene_adicionalmente
idx 11899: Obligacion_la_entidad_que_interviene_adicionalmente_debera_presentar_copia_del_certificado__2e10f8 -> Sujeto_propuesto_la_entidad_que_interviene_adicionalmente
idx 12358: Obligacion_las_entidades_del_grupo_a_deben_separar_los_depositos_sin_vencimiento_consideran_29766b -> Sujeto_propuesto_las_entidades_del_grupo_a
idx 12362: Obligacion_las_entidades_encargadas_del_seguimiento_deberan_cumplimentar_los_reportes_de_in_9d4062 -> Sujeto_propuesto_las_entidades_encargadas_del_seguimiento
idx 12364: Obligacion_las_entidades_encargadas_del_seguimiento_en_el_sepaimpo_deberan_verificar_el_mon_356734 -> Sujeto_propuesto_la_s_entidad_es_encargada_s_del_seguimiento_de_las_oficializaciones_involucradas
idx 12366: Obligacion_las_entidades_encargadas_del_seguimiento_en_sepaimpo_deberan_verificar_las_condi_55ed79 -> Sujeto_propuesto_la_s_entidad_es_encargada_s_del_seguimiento_de_las_oficializaciones_involucradas
idx 12635: Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_0609fb -> Sujeto_propuesto_las_empresas_no_financieras_emisoras_de_tarjetas_locales
idx 12739: Obligacion_las_evaluaciones_crediticias_deberan_basarse_en_metodologias_que_combinen_enfoqu_f98d83 -> Sujeto_propuesto_dichas_evaluaciones
idx 12755: Obligacion_las_financiaciones_deberan_ser_atendidas_exclusivamente_solo_con_fondos_provenie_0be6ca -> Sujeto_propuesto_las_sucursales_o_subsidiarias_locales
idx 12762: Obligacion_las_inversiones_incluyen_las_participaciones_directas_indirectas_y_sinteticas__c_55b42f -> Sujeto_propuesto_las_inversiones
idx 12852: Obligacion_las_posiciones_de_la_cartera_de_negociacion_deberan_ser_valuadas_en_forma_diaria_1c8a06 -> Sujeto_propuesto_las_posiciones
idx 12926: Obligacion_los_administradores_de_las_carteras_crediticias_deberan_suministrar_informacion__7849dd -> Sujeto_propuesto_los_administradores_de_las_carteras_crediticias
idx 12979: Obligacion_los_aportes_de_capital_deben_ser_efectuados_en_efectivo_a_los_fines_de_todas_las_6e3ef1 -> Sujeto_propuesto_los_aportes
idx 13069: Obligacion_los_cobros_de_exportaciones_deben_ser_ingresados_y_liquidados_en_el_mercado_de_c_8549d2 -> Sujeto_propuesto_los_cobros_de_exportaciones
idx 13354: Obligacion_los_pedidos_de_conformidad_deberan_ser_presentados_ante_el_bcra_exclusivamente_p_49d9d3 -> Sujeto_propuesto_la_entidad_nominada_por_el_exportador
idx 13378: Obligacion_los_responsables_de_la_gestion_de_riesgos_deberan_conocer_las_debilidades_de_los_19980c -> Sujeto_propuesto_los_responsables_de_la_gestion_de_riesgos
idx 13385: Obligacion_los_restantes_derivados_sobre_acciones_futuros_forwards_swaps_de_acciones_indivi_87e5d4 -> Sujeto_propuesto_los_restantes_derivados_sobre_acciones_y_las_posiciones_fuera_de_balance_sensibl
idx 13883: Obligacion_para_operaciones_anteriores_al_02_09_19_la_entidad_debe_intervenir_la_documentac_ef4bc1 -> Sujeto_propuesto_la_entidad__ext
idx 13906: Obligacion_para_operaciones_del_punto_3_11_3_al_momento_de_constitucion_de_las_garantias_la_6c9af4 -> Sujeto_propuesto_la_entidad__ext
idx 13942: Obligacion_politica_que_contenga_los_criterios_sobre_cuya_base_el_personal_con_atribucion_e_a2f100 -> Sujeto_propuesto_el_personal_con_atribucion_en_materia_crediticia_de_la_entidad_financiera
idx 13989: Obligacion_proveer_informacion_que_permita_al_miembro_compensador_calcular_la_exigencia_de__b1295a -> Sujeto_propuesto_la_ccp_la_entidad_financiera_la_autoridad_de_control_de_la_ccp_u_otro_organismo_
idx 14163: Obligacion_se_debe_efectuar_un_boleto_de_venta_por_el_concepto_correspondiente_a_la_cancela_3e13b3 -> Sujeto_propuesto_la_entidad__ext
idx 14446: Obligacion_se_requiere_la_conformidad_previa_del_bcra_para_prefinanciaciones_de_exportacion_edc311 -> Sujeto_propuesto_la_entidad__ext
idx 14555: Obligacion_vencido_el_plazo_de_10_dias_habiles_sin_que_se_haya_regularizado_el_incumplimien_105ceb -> Sujeto_propuesto_la_entidad
idx 14575: Operacion_absorcion_de_perdidas_por_instrumentos_de_pasivo__cap_8_3_2_12_b2d35b -> Sujeto_propuesto_los_instrumentos_que_son_parte_del_pasivo
idx 16960: Operacion_inversiones_en_instrumentos_computables_como_capital_regulatorio__cap_8_4_2_2_cce289 -> Sujeto_propuesto_companias_de_seguro
idx 17403: Operacion_pago_de_importacion_de_bien_con_registro_aduanero__ext_10_11_5_4b359d -> Sujeto_propuesto_un_cliente
idx 18035: Operacion_registro_de_operacion_con_pasaporte_personal_diplomatico__ext_5_7_3_030a3b -> Sujeto_propuesto_personal_diplomatico_acreditado_en_el_pais
idx 18850: Potestad_autoaseguramiento_alternativo_riesgos_de_fallecimiento_e_invalidez__los_sujetos__a5f012 -> Sujeto_propuesto_podran
idx 18982: Potestad_excluir_partidas_del_bi_de_forma_inmediata__una_vez_aprobada_la_solicitud_de_exc_3fce4d -> Sujeto_propuesto_la_entidad
idx 19272: Potestad_facultad_de_emitir_certificacion__la_entidad_financiera_nominada_tiene_la_facult_6115b2 -> Sujeto_propuesto_la_entidad_nominada
idx 19575: Potestad_solicitud_de_ampliacion_de_plazo_hasta_fecha_estimada_de_aplicacion__el_exportad_f2314b -> Sujeto_propuesto_la_entidad_encargada_del_seguimiento_del_permiso
idx 19885: Restriccion_cuando_la_asistencia_se_otorgue_en_moneda_distinta_de_la_de_los_recursos_del_ext_087a73 -> Sujeto_propuesto_la_entidad_local
idx 20447: Restriccion_exigencia_basica_de_capital_minimo_para_restantes_entidades_salvo_cajas_de_credi_a4fc21 -> Sujeto_propuesto_restantes_entidades_salvo_cajas_de_credito_cooperativas
idx 20521: Restriccion_la_aplicacion_de_las_divisas_solo_podra_ser_convalidada_hasta_el_monto_que_resul_5272bf -> Sujeto_propuesto_la_entidad_encargada_del_seguimiento
idx 20534: Restriccion_la_cobertura_debera_extinguir_totalmente_el_monto_adeudado_en_caso_de_fallecimie_dca7ba -> Sujeto_propuesto_la_cobertura
idx 20885: Restriccion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_c492c2 -> Sujeto_propuesto_las_empresas_no_financieras_emisoras_de_tarjetas_locales
idx 21090: Restriccion_los_casos_que_no_cumplan_las_condiciones_requeridas_quedan_sujetos_a_la_conformi_055104 -> Sujeto_propuesto_los_casos
idx 21287: Restriccion_los_terminos_contractuales_de_la_accion_no_deberan_contener_clausula_alguna_que__ce92d0 -> Sujeto_propuesto_los_terminos_contractuales
```

### S32 — PASS

INFORMATIVA — Cuantía en la descripción => elemento en la lista (informativa; L-ESQ-R2 §1.5 y reports/u_umbral/reporte_u_umbral.md §2): en los tipos con lista de umbrales, un nodo cuya descripción trae una cuantía (reglas_comparacion.detectar_cuantias) tiene la lista no vacía o el umbral guardado (marca); aparte, las cuantías de la descripción sin un elemento de igual valor y unidad.

**Resultado:** 694 nodos con cuantía en la descripción: 694 con lista, 0 con el umbral guardado (marca), 0 sin ninguna {}; cuantías de la descripción 850, sin elemento de igual valor y unidad 137.

Sin violaciones.

## Tabla resumen

| Severidad | Regla | Resultado | Resumen |
|---|---|---|---|
| bloqueante | S1 | PASS | 22084/22084 aristas con relación admitida (19 relaciones admitidas); 0 violaciones. |
| bloqueante | S2 | PASS | 0 aristas colgantes sobre 22084. |
| bloqueante | S3 | PASS | 22084/22084 aristas conformes a firma; 0 violaciones. Evaluadas: 10518 por matriz, 11374 remite_a, 126 de esqueleto, 66 padre_sugerido. |
| bloqueante | S4 | PASS | Nodos OK: 6723/6723. Aristas OK: 22084/22084. Violaciones: 0. |
| bloqueante | S5 | PASS | Nodos con punto: 6723/6723. Aristas: 22084/22084. Violaciones: 0. |
| bloqueante | S6 | PASS | Archivos válidos (40): TextoOrdenado ['TO_capitales_minimos_actual.pdf', 'TO_clasificacion_deudores_actual.pdf', 'TO_exterior_cambios_actual.pdf', 'TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'TO_regimen_informativo_contable_mensual_actual.pdf'] ∪ esqueleto ['actgar.pdf', 'adrei.pdf', 'autenf.pdf', 'catalogo_sujetos_v3.json', 'ccbcra.pdf', 'convca.pdf', 'cryl.pdf', 'ctacor.pdf', 'depaho.pdf', 'efemin.pdf', 'esquema_v2_clases.json', 'esquema_v3_clases.json', 'fabcra.pdf', 'icmecma.pdf', 'lavdin.pdf', 'lingob.pdf', 'ordcom.pdf', 'osapsa.pdf', 'pagjub.pdf', 'pfmipyme.pdf', 'pimf.pdf', 'ratiofn.pdf', 'rdbcra.pdf', 'repefe.pdf', 'retype.pdf', 'rmrtsd.pdf', 'rrci.pdf', 'servco.pdf', 'snp_atm.pdf', 'snp_debin.pdf', 'snp_psp.pdf', 'snp_spd.pdf', 'snp_tr_nc.pdf', 'supcon.pdf', 'traval.pdf']. Violaciones: 0. |
| bloqueante | S15 | PASS | 35 roles, 51 aristas miembro_de; 12 huérfanos (12 declarados, 0 sin declarar); 0 miembros que no son clase. Lista declarada: 12 ({'sin_id_en_catalogo': 6, 'aplanamiento_rechazado': 5, 'instancia_rechazada': 1}). |
| bloqueante | S18 | PASS | 306 Restricciones limite_cuantitativo: 293 con lista, 13 con el umbral guardado sin lista (marca), 0 sin ninguna. |
| bloqueante | S19 | PASS | 176 Sujetos ({'clase': 70, 'instancia': 5, 'propuesto': 66, 'rol': 35}); catálogo de 110 ids; 0 fuera del catálogo, 0 con nivel inválido, 0 propuestos incompletos. |
| bloqueante | S20 | PASS | 1618 nodos Obligacion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 0. |
| bloqueante | S24 | PASS | 633 nodos Restriccion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 0. |
| bloqueante | S25 | PASS | 62 nodos Comunicacion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 24. |
| bloqueante | S26 | PASS | 6547 nodos evaluados; 0 violaciones {}; marcas de nodo admitidas: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']. |
| bloqueante | S28 | PASS | 66 Sujetos propuestos; 185 filas en el registro; 0 propuestos sin fila. |
| bloqueante | S29 | PASS | 66 aristas padre_sugerido; 0 con destino fuera del catálogo único (110 ids). |
| bloqueante | S30 | PASS | 11374 aristas remite_a ({'externa': 425, 'interna': 10933, 'to_entero': 16}); 0 violaciones. |
| bloqueante | S31 | PASS | 11374 aristas remite_a: {'en_un_tramo_del_chunk_de_la_arista': 11374}; 0 violaciones. |
| bloqueante | S27 | PASS | 1781 aristas de sujeto fuera del esqueleto; 0 sin mención, verificación o método ({}). |
| informativa | S7 | FAIL | 188 grupos violatorios (435 nodos involucrados). |
| informativa | S8 | WARN | 31 grupos con el mismo label normalizado en types distintos. |
| informativa | S9 | PASS | 0 nodos con ambas keys. |
| informativa | S10 | PASS | Sin establecida_en: Condicion=0, Definicion=0, Excepcion=0, Obligacion=0, Operacion=0, Potestad=0, Restriccion=0 (total 0). |
| informativa | S11 | WARN | Sin aplica_a: Excepcion=326, Obligacion=515, Operacion=1229, Potestad=100, Restriccion=434 (total 2604). |
| informativa | S12 | FAIL | 222 Excepciones sin salida exceptua/exceptua_obligacion. |
| informativa | S21 | WARN | 11374 remisiones ({'interna': 10933, 'externa': 425, 'to_entero': 16}); 16 incoherentes (por alcance: {'to_entero': 16}). |
| informativa | S22 | PASS | 66 aristas padre_sugerido; 0 incoherentes (0 con destino distinto, 0 con origen fuera de cuarentena). |
| informativa | S23 | WARN | 1770 aristas aplica_a; 110 hacia Sujetos propuestos (64 destinos distintos). |
| informativa | S32 | PASS | 694 nodos con cuantía en la descripción: 694 con lista, 0 con el umbral guardado (marca), 0 sin ninguna {}; cuantías de la descripción 850, sin elemento de igual valor y unidad 137. |

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
