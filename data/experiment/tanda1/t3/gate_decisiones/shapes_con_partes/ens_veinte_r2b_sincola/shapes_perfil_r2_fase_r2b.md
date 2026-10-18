# Validador de shapes — perfil r2

- **Grafo:** `data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b_sincola/r2/kg.json`
- **sha256 del grafo:** `384a6d5bc139cd7b74d86840c68e7034b7a9bcb4bc26da7c61567f3f053e624e`
- **Fecha:** 2026-10-18
- **Nodos:** 12452
- **Aristas:** 28320
- **Perfil:** r2 (fase r2b)
- **Vocabulario:** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/pyd_r2/generados/enums_r2.json` (sha256 `abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241`); marcas de nodo de `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/pyd_r2/code/modelos_r2.py`: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']
- **Catálogo único (S19, S29):** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json` — 110 ids
- **Lista de S15:** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json`
- **Registro (S28):** `data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b_sincola/r2/no_mapeados_sujetos.jsonl`
- **E0 (S31):** `<SCRATCHPAD>/t3f/e0p/e0_con_partes/tanda1_corrida1`
- **Veredicto global: PASA**

## Bloqueantes

### S1 — PASS

Toda arista usa una relación admitida por el perfil r2: los 13 predicados de enums_r2.json ∪ remite_a (enmienda 2 de L-ESQ-R2) ∪ las 4 de esqueleto ∪ padre_sugerido.

**Resultado:** 28320/28320 aristas con relación admitida (19 relaciones admitidas); 0 violaciones.

Sin violaciones.

### S2 — PASS

Integridad referencial: origen y destino de toda arista existen como nodos.

**Resultado:** 0 aristas colgantes sobre 28320.

Sin violaciones.

### S3 — PASS

Toda arista respeta las firmas del perfil r2: matriz ampliada de enums_r2.json (firmas_r2, con condicion_de -> Operacion|Potestad) ∪ remite_a con origen en los siete tipos de contenido y destino en esos siete o TextoOrdenado ∪ esqueleto solo Sujeto->Sujeto ∪ padre_sugerido solo de Sujeto propuesto a Sujeto clase|rol. Una referencia con origen distinto de TextoOrdenado es violación, con o sin rol_fuente.

**Resultado:** 28320/28320 aristas conformes a firma; 0 violaciones. Evaluadas: 19076 por matriz, 8838 remite_a, 126 de esqueleto, 280 padre_sugerido.

Sin violaciones.

### S4 — PASS

Todo nodo y toda arista tienen provenance dict con al menos {to, archivo, punto, rol_documental}, provenances lista no vacía con provenance == provenances[0]; para rol_documental distinto de esqueleto, to y archivo no vacíos (para esqueleto se admiten to nulo, chunk_id nulo y paginas vacía).

**Resultado:** Nodos OK: 12452/12452. Aristas OK: 28320/28320. Violaciones: 0.

Sin violaciones.

### S5 — PASS

Todo provenance.punto (de nodo y de arista) es una string no vacía.

**Resultado:** Nodos con punto: 12452/12452. Aristas: 28320/28320. Violaciones: 0.

Sin violaciones.

### S6 — PASS

Todo provenance.archivo pertenece a {properties.archivo de los nodos TextoOrdenado} ∪ {archivo de las provenances con rol_documental=esqueleto}; nada codificado a mano.

**Resultado:** Archivos válidos (57): TextoOrdenado ['adrei.pdf', 'ayccef.pdf', 'cajasc.pdf', 'ceninf.pdf', 'cirmo3.pdf', 'depaho.pdf', 'efemin.pdf', 'expaef.pdf', 'lingeef.pdf', 'manori.pdf', 'nmcief.pdf', 'opefci.pdf', 'ri_ccna.pdf', 'ri_dcpc.pdf', 'ri_gerc.pdf', 'ri_mmsef.pdf', 'ri_pgn.pdf', 'ri_rml.pdf', 'snp_cheq.pdf', 'snp_tr.pdf'] ∪ esqueleto ['TO_capitales_minimos_actual.pdf', 'TO_clasificacion_deudores_actual.pdf', 'TO_exterior_cambios_actual.pdf', 'TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'TO_regimen_informativo_contable_mensual_actual.pdf', 'actgar.pdf', 'autenf.pdf', 'catalogo_sujetos_v3.json', 'ccbcra.pdf', 'convca.pdf', 'cryl.pdf', 'ctacor.pdf', 'esquema_v2_clases.json', 'esquema_v3_clases.json', 'fabcra.pdf', 'icmecma.pdf', 'lavdin.pdf', 'lingob.pdf', 'ordcom.pdf', 'osapsa.pdf', 'pagjub.pdf', 'pfmipyme.pdf', 'pimf.pdf', 'ratiofn.pdf', 'rdbcra.pdf', 'repefe.pdf', 'retype.pdf', 'rmrtsd.pdf', 'rrci.pdf', 'servco.pdf', 'snp_atm.pdf', 'snp_debin.pdf', 'snp_psp.pdf', 'snp_spd.pdf', 'snp_tr_nc.pdf', 'supcon.pdf', 'traval.pdf']. Violaciones: 0.

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

**Resultado:** 358 Restricciones limite_cuantitativo: 341 con lista, 17 con el umbral guardado sin lista (marca), 0 sin ninguna.

Sin violaciones.

### S19 — PASS

ERROR — Catálogo de sujetos: todo Sujeto tiene nivel ∈ {clase, instancia, rol, propuesto}; si nivel ≠ propuesto, su id está en el catálogo (clases ∪ roles) del artefacto de --excepciones; si nivel = propuesto, tiene properties.cuarentena y properties.padre_sugerido.

**Resultado:** 390 Sujetos ({'clase': 70, 'instancia': 5, 'propuesto': 280, 'rol': 35}); catálogo de 110 ids; 0 fuera del catálogo, 0 con nivel inválido, 0 propuestos incompletos.

Sin violaciones.

### S20 — PASS

ERROR — Enum de Obligacion.tipo del perfil r2: en la lista o con la marca fuera_de_lista. Lista: {presentacion_informativa|calculo|asignacion|comunicacion_a_cliente|reporte_al_supervisor|otra}.

**Resultado:** 4751 nodos Obligacion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 0.

Sin violaciones.

### S24 — PASS

ERROR — Enum de Restriccion.tipo (bloqueante salvo la marca fuera_de_lista). Lista: {prohibicion|limite_cuantitativo|limite_cualitativo}.

**Resultado:** 914 nodos Restriccion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 0.

Sin violaciones.

### S25 — PASS

ERROR — Enum de Comunicacion.tipo, con «externa» (bloqueante salvo la marca fuera_de_lista). Lista: {A|B|C|externa}.

**Resultado:** 142 nodos Comunicacion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 32.

Sin violaciones.

### S26 — PASS

ERROR — Claves cerradas por tipo: las properties de cada nodo de los nueve tipos están en claves_por_tipo de enums_r2.json o en MARCAS_NODO de modelos_r2.py; lo demás vive en properties_no_definidas.

**Resultado:** 12062 nodos evaluados; 0 violaciones {}; marcas de nodo admitidas: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to'].

Sin violaciones.

### S28 — PASS

ERROR — Sujeto propuesto con fila en el registro de no mapeados (bloqueante).

**Resultado:** 280 Sujetos propuestos; 896 filas en el registro; 0 propuestos sin fila.

Sin violaciones.

### S29 — PASS

ERROR — Destino de padre_sugerido en el catálogo único (bloqueante: U-CAT-UNICO está cerrada).

**Resultado:** 280 aristas padre_sugerido; 0 con destino fuera del catálogo único (110 ids).

Sin violaciones.

### S30 — PASS

ERROR — alcance de remite_a en la lista cerrada y coherente con los extremos (bloqueante). Coherencia: to_entero si el destino es un TextoOrdenado (destino <to>::TO); si no, interna cuando el TO de la unidad citada es el de la procedencia de la arista y externa cuando es otro (enmienda 2 de L-ESQ-R2, §3).

**Resultado:** 8838 aristas remite_a ({'externa': 272, 'interna': 8539, 'to_entero': 27}); 0 violaciones.

Sin violaciones.

### S31 — PASS

ERROR — evidencia de remite_a: tramo literal de un único tramo del texto de E0 de su chunk_id (bloqueante; sin --e0, NO COMPUTABLE). Tramo = el texto propio del chunk o uno de sus tramos heredados, cada uno por separado; nunca la concatenación. Si la evidencia no está en el chunk de provenance, se busca en las otras procedencias de la arista (fusión).

**Resultado:** 8838 aristas remite_a: {'en_un_tramo_del_chunk_de_la_arista': 8838}; 0 violaciones.

Sin violaciones.

### S27 — PASS

ERROR — Arista de sujeto con mención y método (informativa en r2a, bloqueante desde r2b). Fase: r2b.

**Resultado:** 4374 aristas de sujeto fuera del esqueleto; 0 sin mención, verificación o método ({}).

Sin violaciones.

## Informativas

### S7 — FAIL

ERROR — Unicidad exacta: no puede haber dos nodos con el mismo (type, label normalizado).

**Resultado:** 400 grupos violatorios (903 nodos involucrados).

```
[Comunicacion] 'com. a 3500' (3 nodos):
    - Comunicacion_a_3500  (label: 'Com. A 3500')
    - Comunicacion_a_3500__depaho  (label: 'Com. A 3500')
    - Comunicacion_a_3500__snp_cheq  (label: 'Com. A 3500')
[Comunicacion] 'ley 19.359' (2 nodos):
    - Comunicacion_ley_19_359  (label: 'Ley 19.359')
    - Comunicacion_ley_19_359__efemin  (label: 'Ley 19.359')
[Comunicacion] 'ley 21.526' (6 nodos):
    - Comunicacion_ley_21_526  (label: 'Ley 21.526')
    - Comunicacion_ley_21_526__cajasc  (label: 'Ley 21.526')
    - Comunicacion_ley_21_526__depaho  (label: 'Ley 21.526')
    - Comunicacion_ley_21_526__efemin  (label: 'Ley 21.526')
    - Comunicacion_ley_21_526__ri_ccna  (label: 'Ley 21.526')
    - Comunicacion_ley_21_526__snp_cheq  (label: 'Ley 21.526')
[Comunicacion] 'ley 25.065' (3 nodos):
    - Comunicacion_ley_25_065  (label: 'Ley 25.065')
    - Comunicacion_ley_25_065__cajasc  (label: 'Ley 25.065')
    - Comunicacion_ley_25_065__efemin  (label: 'Ley 25.065')
[Comunicacion] 'ley 25.326' (2 nodos):
    - Comunicacion_ley_25_326  (label: 'Ley 25.326')
    - Comunicacion_ley_25_326__depaho  (label: 'Ley 25.326')
[Comunicacion] 'ley 26.173' (2 nodos):
    - Comunicacion_ley_26_173  (label: 'Ley 26.173')
    - Comunicacion_ley_26_173__cajasc  (label: 'Ley 26.173')
[Comunicacion] 'ley de entidades financieras' (4 nodos):
    - Comunicacion_ley_de_entidades_financieras  (label: 'Ley de Entidades Financieras')
    - Comunicacion_ley_de_entidades_financieras__ayccef  (label: 'Ley de Entidades Financieras')
    - Comunicacion_ley_de_entidades_financieras__cirmo3  (label: 'Ley de Entidades Financieras')
    - Comunicacion_ley_de_entidades_financieras__depaho  (label: 'Ley de Entidades Financieras')
[Comunicacion] 'proteccion de usuarios de servicios financieros' (2 nodos):
    - Comunicacion_proteccion_de_los_usuarios_de_servicios_financieros  (label: 'Protección de usuarios de servicios financieros')
    - Comunicacion_proteccion_de_los_usuarios_de_servicios_financieros__depaho  (label: 'Protección de usuarios de servicios financieros')
[Comunicacion] 'to documentos de identificacion en vigencia' (3 nodos):
    - Comunicacion_documentos_de_identificacion_en_vigencia  (label: 'TO Documentos de Identificación en Vigencia')
    - Comunicacion_documentos_de_identificacion_en_vigencia__depaho  (label: 'TO Documentos de Identificación en Vigencia')
    - Comunicacion_to_documentos_de_identificacion_en_vigencia  (label: 'TO Documentos de Identificación en Vigencia')
[Condicion] 'acuerdo y efectivizacion desde 1.8.06' (2 nodos):
    - Condicion_acuerdo_y_efectivizacion_desde_1_8_06__el_arrendamiento_debe_acordarse_y_efectiv_686745  (label: 'Acuerdo y efectivización desde 1.8.06')
    - Condicion_acuerdo_y_efectivizacion_desde_1_8_06__el_arrendamiento_debe_acordarse_y_efectiv_a48e3a  (label: 'Acuerdo y efectivización desde 1.8.06')
[Condicion] 'analisis crediticio efectuado' (2 nodos):
    - Condicion_analisis_crediticio_efectuado__se_ha_completado_el_analisis_crediticio_del_prest_edfcf3  (label: 'Análisis crediticio efectuado')
    - Condicion_analisis_crediticio_efectuado__se_ha_efectuado_el_analisis_crediticio_del_presta_e8cf29  (label: 'Análisis crediticio efectuado')
[Condicion] 'antiguedad en matricula tres anos o mas' (2 nodos):
    - Condicion_antiguedad_en_matricula_tres_anos_o_mas__el_auditor_externo_debe_contar_con_anti_ceec9f  (label: 'Antigüedad en matrícula tres años o más')
    - Condicion_antiguedad_en_matricula_tres_anos_o_mas__el_socio_responsable_debe_contar_con_an_f3a14c  (label: 'Antigüedad en matrícula tres años o más')
[Condicion] 'ausencia de prevision especifica' (2 nodos):
    - Condicion_ausencia_de_prevision_especifica__cuando_no_exista_prevision_especifica_en_las_n_20688e  (label: 'Ausencia de previsión específica')
    - Condicion_ausencia_de_prevision_especifica__cuando_no_exista_prevision_especifica_en_las_n_97cc87  (label: 'Ausencia de previsión específica')
[Condicion] 'caducidad del plan de facilidades' (2 nodos):
    - Condicion_caducidad_del_plan_de_facilidades__la_caducidad_del_plan_de_facilidades_de_pago__d6102f  (label: 'Caducidad del plan de facilidades')
    - Condicion_caducidad_del_plan_de_facilidades__si_el_plan_de_facilidades_de_pago_caduca_por__acdc08  (label: 'Caducidad del plan de facilidades')
[Condicion] 'cliente de riesgo bajo con medidas de inclusion financiera' (2 nodos):
    - Condicion_cliente_de_riesgo_bajo_con_medidas_de_inclusion_financiera__supuesto_en_que_el_c_ed91d4  (label: 'Cliente de riesgo bajo con medidas de inclusión financiera')
    - Condicion_cliente_de_riesgo_bajo_con_medidas_de_inclusion_financiera__supuesto_en_que_la_a_c26418  (label: 'Cliente de riesgo bajo con medidas de inclusión financiera')
[Condicion] 'condena con inhabilitacion de cargos publicos' (2 nodos):
    - Condicion_condena_con_inhabilitacion_de_cargos_publicos__haber_sido_condenado_con_accesori_05fe48  (label: 'Condena con inhabilitación de cargos públicos')
    - Condicion_condena_con_inhabilitacion_de_cargos_publicos__persona_condenada_con_accesoria_d_7197b7  (label: 'Condena con inhabilitación de cargos públicos')
[Condicion] 'condena por delitos contra la fe publica' (2 nodos):
    - Condicion_condena_por_delitos_contra_la_fe_publica__haber_sido_condenado_por_delitos_contr_ffb73c  (label: 'Condena por delitos contra la fe pública')
    - Condicion_condena_por_delitos_contra_la_fe_publica__persona_condenada_por_delitos_contra_l_9287f1  (label: 'Condena por delitos contra la fe pública')
[Condicion] 'condena por delitos en constitucion, funcionamiento y liquidacion de sociedades' (2 nodos):
    - Condicion_condena_por_delitos_en_constitucion_funcionamiento_y_liquidacion_de_sociedades___7c95ef  (label: 'Condena por delitos en constitución, funcionamiento y liquidación de sociedades')
    - Condicion_condena_por_delitos_en_constitucion_funcionamiento_y_liquidacion_de_sociedades___c732a3  (label: 'Condena por delitos en constitución, funcionamiento y liquidación de sociedades')
[Condicion] 'condiciones aceptadas por solicitantes' (2 nodos):
    - Condicion_condiciones_aceptadas_por_solicitantes__los_solicitantes_han_aceptado_las_condic_695231  (label: 'Condiciones aceptadas por solicitantes')
    - Condicion_condiciones_aceptadas_por_solicitantes__los_solicitantes_han_aceptado_las_condic_cc4f43  (label: 'Condiciones aceptadas por solicitantes')
[Condicion] 'condiciones del punto 1.7' (2 nodos):
    - Condicion_condiciones_del_punto_1_7__la_extraccion_de_fondos_esta_condicionada_al_cumplimi_2e2aef  (label: 'Condiciones del punto 1.7')
    - Condicion_condiciones_del_punto_1_7__la_extraccion_de_fondos_mediante_transferencias_debe__e35183  (label: 'Condiciones del punto 1.7')
[Condicion] 'conforme a normas e instrucciones aplicables' (2 nodos):
    - Condicion_conforme_a_normas_e_instrucciones_aplicables__la_conservacion_en_custodia_debe_r_48a67a  (label: 'Conforme a normas e instrucciones aplicables')
    - Condicion_conforme_a_normas_e_instrucciones_aplicables__la_entrega_debe_realizarse_conform_fce0ae  (label: 'Conforme a normas e instrucciones aplicables')
[Condicion] 'conocimiento previo del cliente — 5 dias habiles' (2 nodos):
    - Condicion_conocimiento_previo_del_cliente_5_dias_habiles__el_cliente_debe_tener_conocimien_7e2cdb  (label: 'Conocimiento previo del cliente — 5 días hábiles')
    - Condicion_conocimiento_previo_del_cliente_5_dias_habiles__el_cliente_debe_tener_conocimien_981a75  (label: 'Conocimiento previo del cliente — 5 días hábiles')
[Condicion] 'consentimiento autoridades pais radicacion' (2 nodos):
    - Condicion_consentimiento_autoridades_pais_radicacion__se_debe_obtener_el_consentimiento_pr_0f0c9c  (label: 'Consentimiento autoridades país radicación')
    - Condicion_consentimiento_autoridades_pais_radicacion__se_debe_obtener_el_consentimiento_pr_7e3b31  (label: 'Consentimiento autoridades país radicación')
[Condicion] 'conservacion tamano linea peso' (2 nodos):
    - Condicion_conservacion_tamano_linea_peso__el_billete_conserva_el_tamano_de_los_billetes_de_10b56c  (label: 'Conservación tamaño Línea Peso')
    - Condicion_conservacion_tamano_linea_peso__el_billete_conserva_el_tamano_de_los_billetes_de_fd3059  (label: 'Conservación tamaño Línea Peso')
[Condicion] 'cumplimiento de normas sobre clasificacion de deudores' (2 nodos):
    - Condicion_cumplimiento_de_normas_sobre_clasificacion_de_deudores__los_anexos_al_legajo_del_b7b58e  (label: 'Cumplimiento de normas sobre Clasificación de deudores')
    - Condicion_cumplimiento_de_normas_sobre_clasificacion_de_deudores__se_debe_cumplir_con_lo_d_e17580  (label: 'Cumplimiento de normas sobre Clasificación de deudores')
[Condicion] 'cumplimiento de requisitos de la seccion' (2 nodos):
    - Condicion_cumplimiento_de_requisitos_de_la_seccion__la_facultad_de_desarrollar_la_base_de__7062b7  (label: 'Cumplimiento de requisitos de la sección')
    - Condicion_cumplimiento_de_requisitos_de_la_seccion__la_facultad_de_desarrollar_la_base_de__cfdcfc  (label: 'Cumplimiento de requisitos de la Sección')
[Condicion] 'declaracion responsable de irregularidades en gobierno' (2 nodos):
    - Condicion_declaracion_responsable_de_irregularidades_en_gobierno__supuesto_que_inhabilita__04a3ef  (label: 'Declaración responsable de irregularidades en gobierno')
    - Condicion_declaracion_responsable_de_irregularidades_en_gobierno__supuesto_que_inhabilita__904e01  (label: 'Declaración responsable de irregularidades en gobierno')
[Condicion] 'efectiva tradicion o entrega de titulos valores' (2 nodos):
    - Condicion_efectiva_tradicion_o_entrega_de_titulos_valores__condicion_debe_verificarse_la_e_f53d20  (label: 'Efectiva tradición o entrega de títulos valores')
    - Condicion_efectiva_tradicion_o_entrega_de_titulos_valores__debe_verificarse_la_efectiva_tr_cd523d  (label: 'Efectiva tradición o entrega de títulos valores')
[Condicion] 'entidad acreedora en todos los grados' (3 nodos):
    - Condicion_entidad_acreedora_en_todos_los_grados__la_entidad_debe_ser_la_acreedora_en_todos_04f21c  (label: 'Entidad acreedora en todos los grados')
    - Condicion_entidad_acreedora_en_todos_los_grados__la_entidad_debe_ser_la_acreedora_en_todos_7d3726  (label: 'Entidad acreedora en todos los grados')
    - Condicion_entidad_acreedora_en_todos_los_grados__la_entidad_debe_ser_la_acreedora_en_todos_d2d0eb  (label: 'Entidad acreedora en todos los grados')
[Condicion] 'entidad del exterior sujeta a supervision consolidada' (3 nodos):
    - Condicion_entidad_del_exterior_sujeta_a_supervision_consolidada__la_entidad_del_exterior_q_4053c2  (label: 'Entidad del exterior sujeta a supervisión consolidada')
    - Condicion_entidad_del_exterior_sujeta_a_supervision_consolidada__la_entidad_del_exterior_q_da7cd1  (label: 'Entidad del exterior sujeta a supervisión consolidada')
    - Condicion_entidad_del_exterior_sujeta_a_supervision_consolidada__la_obligacion_de_suminist_5b5f1c  (label: 'Entidad del exterior sujeta a supervisión consolidada')
[Condicion] 'existencia de mas de un solicitante' (2 nodos):
    - Condicion_existencia_de_mas_de_un_solicitante__existe_mas_de_un_solicitante_en_el_prestamo_e27505  (label: 'Existencia de más de un solicitante')
    - Condicion_existencia_de_mas_de_un_solicitante__la_aplicacion_de_las_alternativas_de_cobert_7b2711  (label: 'Existencia de más de un solicitante')
[Condicion] 'existencia de mercado con valor de referencia' (4 nodos):
    - Condicion_existencia_de_mercado_con_valor_de_referencia__el_bien_debe_contar_con_un_mercad_5ca7ea  (label: 'Existencia de mercado con valor de referencia')
    - Condicion_existencia_de_mercado_con_valor_de_referencia__las_financiaciones_deben_contar_c_97fa83  (label: 'Existencia de mercado con valor de referencia')
    - Condicion_existencia_de_mercado_con_valor_de_referencia__los_bienes_objeto_del_arrendamien_8a8835  (label: 'Existencia de mercado con valor de referencia')
    - Condicion_existencia_de_mercado_con_valor_de_referencia__los_vehiculos_automotores_y_maqui_ae0dd4  (label: 'Existencia de mercado con valor de referencia')
[Condicion] 'experiencia dos anos o mas en auditoria' (2 nodos):
    - Condicion_experiencia_dos_anos_o_mas_en_auditoria__el_auditor_externo_debe_contar_con_expe_971fb8  (label: 'Experiencia dos años o más en auditoria')
    - Condicion_experiencia_dos_anos_o_mas_en_auditoria__el_socio_responsable_debe_contar_con_ex_fadaff  (label: 'Experiencia dos años o más en auditoría')
[Condicion] 'fondos destinados a constitucion o renovacion de plazos fijos' (2 nodos):
    - Condicion_fondos_destinados_a_constitucion_o_renovacion_de_plazos_fijos__cuando_los_fondos_5b77d9  (label: 'Fondos destinados a constitución o renovación de plazos fijos')
    - Condicion_fondos_destinados_a_constitucion_o_renovacion_de_plazos_fijos__cuando_los_fondos_876e29  (label: 'Fondos destinados a constitución o renovación de plazos fijos')
[Condicion] 'fondos destinados a inversion en destinos previstos' (2 nodos):
    - Condicion_fondos_destinados_a_inversion_en_destinos_previstos__cuando_los_fondos_depositad_081fc1  (label: 'Fondos destinados a inversión en destinos previstos')
    - Condicion_fondos_destinados_a_inversion_en_destinos_previstos__cuando_los_fondos_depositad_1874c9  (label: 'Fondos destinados a inversión en destinos previstos')
[Condicion] 'inactividad por 730 dias corridos' (2 nodos):
    - Condicion_inactividad_por_730_dias_corridos__la_facultad_de_cierre_se_habilita_cuando_no_s_4bc839  (label: 'Inactividad por 730 días corridos')
    - Condicion_inactividad_por_730_dias_corridos__no_se_han_registrado_acreditaciones_de_los_be_1172c0  (label: 'Inactividad por 730 días corridos')
[Condicion] 'incumplimiento de condiciones operativas' (2 nodos):
    - Condicion_incumplimiento_de_condiciones_operativas__el_cliente_no_ha_cumplido_las_condicio_a35809  (label: 'Incumplimiento de condiciones operativas')
    - Condicion_incumplimiento_de_condiciones_operativas__el_cliente_no_ha_cumplido_las_condicio_c46ed7  (label: 'Incumplimiento de condiciones operativas')
[Condicion] 'indicadores cualitativos o cuantitativos' (2 nodos):
    - Condicion_indicadores_cualitativos_o_cuantitativos__los_indicadores_disenados_pueden_ser_d_1dcc2b  (label: 'Indicadores cualitativos o cuantitativos')
    - Condicion_indicadores_cualitativos_o_cuantitativos__los_indicadores_pueden_adoptar_forma_c_3cee5e  (label: 'Indicadores cualitativos o cuantitativos')
[Condicion] 'modificaciones de tasa en el curso del mes' (2 nodos):
    - Condicion_modificaciones_de_tasa_en_el_curso_del_mes__cuando_se_verifiquen_modificaciones__13598b  (label: 'Modificaciones de tasa en el curso del mes')
    - Condicion_modificaciones_de_tasa_en_el_curso_del_mes__cuando_se_verifiquen_modificaciones__15e197  (label: 'Modificaciones de tasa en el curso del mes')
[Condicion] 'no alcanzado por inhabilidades art. 264 ley 19.550' (2 nodos):
    - Condicion_no_alcanzado_por_inhabilidades_art_264_ley_19_550__condicion_de_que_el_socio_res_d8d9b5  (label: 'No alcanzado por inhabilidades art. 264 Ley 19.550')
    - Condicion_no_alcanzado_por_inhabilidades_art_264_ley_19_550__el_auditor_externo_no_esta_al_397083  (label: 'No alcanzado por inhabilidades art. 264 Ley 19.550')
[Condicion] 'no exclusion del registro de auditores' (2 nodos):
    - Condicion_no_exclusion_del_registro_de_auditores__condicion_de_que_el_contador_publico_nac_d0180b  (label: 'No exclusión del Registro de auditores')
    - Condicion_no_exclusion_del_registro_de_auditores__el_socio_responsable_no_ha_sido_excluido_d070d6  (label: 'No exclusión del Registro de Auditores')
[Condicion] 'no oposicion a normas vigentes' (2 nodos):
    - Condicion_no_oposicion_a_normas_vigentes__siempre_que_las_disposiciones_aplicables_no_cont_fa08c4  (label: 'No oposición a normas vigentes')
    - Condicion_no_oposicion_a_normas_vigentes__siempre_que_las_disposiciones_aplicables_no_se_o_744c5a  (label: 'No oposición a normas vigentes')
[Condicion] 'no previsto en puntos precedentes' (4 nodos):
    - Condicion_no_previsto_en_puntos_precedentes__cuando_no_exista_prevision_especifica_en_los__7a6c4c  (label: 'No previsto en puntos precedentes')
    - Condicion_no_previsto_en_puntos_precedentes__supuesto_en_el_que_no_existe_prevision_especi_5f5bf0  (label: 'No previsto en puntos precedentes')
    - Condicion_no_previsto_en_puntos_precedentes__supuesto_en_el_que_no_existe_prevision_especi_6e450a  (label: 'No previsto en puntos precedentes')
    - Condicion_no_previsto_en_puntos_precedentes__supuesto_en_el_que_no_existe_prevision_especi_b4e052  (label: 'No previsto en puntos precedentes')
[Condicion] 'no renegociacion del contrato' (2 nodos):
    - Condicion_no_renegociacion_del_contrato__el_arrendamiento_no_debe_ser_una_renegociacion_de_4c57b6  (label: 'No renegociación del contrato')
    - Condicion_no_renegociacion_del_contrato__no_debe_tratarse_de_una_renegociacion_del_contrat_0027e6  (label: 'No renegociación del contrato')
[Condicion] 'no se opone a lo detallado en puntos precedentes' (2 nodos):
    - Condicion_no_se_opone_a_lo_detallado_en_puntos_precedentes__supuesto_en_el_que_la_aplicaci_f50032  (label: 'No se opone a lo detallado en puntos precedentes')
    - Condicion_no_se_opone_a_lo_detallado_en_puntos_precedentes__supuesto_en_el_que_las_disposi_ccce2e  (label: 'No se opone a lo detallado en puntos precedentes')
[Condicion] 'no superacion de validaciones' (2 nodos):
    - Condicion_no_superacion_de_validaciones__condicion_de_que_los_archivos_no_superen_las_vali_61c055  (label: 'No superación de validaciones')
    - Condicion_no_superacion_de_validaciones__se_verifica_cuando_el_archivo_recibido_no_supera__f5ebfd  (label: 'No superación de validaciones')
[Condicion] 'otorgamiento aprobado por entidad financiera' (2 nodos):
    - Condicion_otorgamiento_aprobado_por_entidad_financiera__la_entidad_financiera_ha_aprobado__32dd19  (label: 'Otorgamiento aprobado por entidad financiera')
    - Condicion_otorgamiento_aprobado_por_entidad_financiera__la_entidad_financiera_ha_aprobado__54bfb3  (label: 'Otorgamiento aprobado por entidad financiera')
[Condicion] 'pertenencia al grupo a al 30 de septiembre' (2 nodos):
    - Condicion_pertenencia_al_grupo_a_al_30_de_septiembre__la_entidad_financiera_debe_pertenece_641a0f  (label: 'Pertenencia al Grupo A al 30 de septiembre')
    - Condicion_pertenencia_al_grupo_a_al_30_de_septiembre__la_obligacion_de_divulgar_informacio_459910  (label: 'Pertenencia al Grupo A al 30 de septiembre')
[Condicion] 'plazo 60 dias sin reclamo' (2 nodos):
    - Condicion_plazo_60_dias_sin_reclamo__supuesto_de_conformidad_presunta_que_transcurran_60_d_002993  (label: 'Plazo 60 días sin reclamo')
    - Condicion_plazo_60_dias_sin_reclamo__supuesto_de_conformidad_presunta_que_transcurran_60_d_21706e  (label: 'Plazo 60 días sin reclamo')
[Condicion] 'plazo libremente convenido' (3 nodos):
    - Condicion_plazo_libremente_convenido__el_plazo_de_la_operacion_es_el_que_libremente_conven_6a88c5  (label: 'Plazo libremente convenido')
    - Condicion_plazo_libremente_convenido__el_plazo_de_la_operacion_es_el_que_libremente_conven_bd8095  (label: 'Plazo libremente convenido')
    - Condicion_plazo_libremente_convenido__el_plazo_es_el_que_libremente_convengan_las_partes___e69678  (label: 'Plazo libremente convenido')
[Condicion] 'plazo minimo antes del cierre' (2 nodos):
    - Condicion_plazo_minimo_antes_del_cierre__se_debe_otorgar_un_plazo_no_inferior_a_30_dias_co_fc1e7b  (label: 'Plazo mínimo antes del cierre')
    - Condicion_plazo_minimo_antes_del_cierre__se_otorga_un_plazo_no_inferior_a_30_dias_corridos_a642b9  (label: 'Plazo mínimo antes del cierre')
[Condicion] 'plazo previo a iniciacion de actividades' (2 nodos):
    - Condicion_plazo_previo_a_iniciacion_de_actividades__el_cumplimiento_de_las_exigencias_debe_4628d9  (label: 'Plazo previo a iniciación de actividades')
    - Condicion_plazo_previo_a_iniciacion_de_actividades__la_inscripcion_debe_realizarse_con_una_53fb0e  (label: 'Plazo previo a iniciación de actividades')
[Condicion] 'proporcionalidad a dimension e importancia economica' (3 nodos):
    - Condicion_proporcionalidad_a_dimension_e_importancia_economica__el_marco_debe_ser_proporci_287672  (label: 'Proporcionalidad a dimensión e importancia económica')
    - Condicion_proporcionalidad_a_dimension_e_importancia_economica__el_marco_debe_ser_proporci_6bf799  (label: 'Proporcionalidad a dimensión e importancia económica')
    - Condicion_proporcionalidad_a_dimension_e_importancia_economica__el_proceso_debe_ser_propor_d3273d  (label: 'Proporcionalidad a dimensión e importancia económica')
[Condicion] 'registro en registro nacional de propiedad del automotor' (4 nodos):
    - Condicion_registro_en_registro_nacional_de_propiedad_del_automotor__el_bien_vehiculo_autom_0944a1  (label: 'Registro en registro nacional de propiedad del automotor')
    - Condicion_registro_en_registro_nacional_de_propiedad_del_automotor__la_prenda_debe_estar_r_d80122  (label: 'Registro en registro nacional de propiedad del automotor')
    - Condicion_registro_en_registro_nacional_de_propiedad_del_automotor__las_financiaciones_deb_560904  (label: 'Registro en registro nacional de propiedad del automotor')
    - Condicion_registro_en_registro_nacional_de_propiedad_del_automotor__los_creditos_deben_est_a6b29e  (label: 'Registro en registro nacional de propiedad del automotor')
[Condicion] 'residencia en el pais — actividad agricola' (2 nodos):
    - Condicion_residencia_en_el_pais_actividad_agricola__el_cliente_debe_ser_residente_en_el_pa_9bd268  (label: 'Residencia en el país — actividad agrícola')
    - Condicion_residencia_en_el_pais_actividad_agricola__los_clientes_deben_ser_residentes_en_e_b4c135  (label: 'Residencia en el país — actividad agrícola')
[Condicion] 'solicitud de las entidades' (4 nodos):
    - Condicion_solicitud_de_las_entidades__la_autorizacion_del_bcra_esta_condicionada_a_que_las_4f16d6  (label: 'Solicitud de las entidades')
    - Condicion_solicitud_de_las_entidades__la_autorizacion_del_bcra_esta_condicionada_a_que_las_5299f8  (label: 'Solicitud de las entidades')
    - Condicion_solicitud_de_las_entidades__la_autorizacion_del_bcra_esta_condicionada_a_que_las_6f0826  (label: 'Solicitud de las entidades')
    - Condicion_solicitud_de_las_entidades__la_autorizacion_del_bcra_para_captar_depositos_en_ot_fdbc6a  (label: 'Solicitud de las entidades')
[Condicion] 'supuesto: no previsto en puntos precedentes' (2 nodos):
    - Condicion_supuesto_no_previsto_en_puntos_precedentes__cuando_una_materia_no_se_encuentre_p_25cd4e  (label: 'Supuesto: no previsto en puntos precedentes')
    - Condicion_supuesto_no_previsto_en_puntos_precedentes__cuando_una_materia_no_se_encuentre_p_c6399e  (label: 'Supuesto: no previsto en puntos precedentes')
[Condicion] 'supuesto: no se opone a lo detallado' (2 nodos):
    - Condicion_supuesto_no_se_opone_a_lo_detallado__cuando_las_disposiciones_aplicables_no_se_o_e975c8  (label: 'Supuesto: no se opone a lo detallado')
    - Condicion_supuesto_no_se_opone_a_lo_detallado__cuando_las_disposiciones_no_se_oponen_a_lo__5b450c  (label: 'Supuesto: no se opone a lo detallado')
[Condicion] 'uso de medios electronicos en lugar de papel' (2 nodos):
    - Condicion_uso_de_medios_electronicos_en_lugar_de_papel__cuando_se_utilicen_medios_electron_ba5b11  (label: 'Uso de medios electrónicos en lugar de papel')
    - Condicion_uso_de_medios_electronicos_en_lugar_de_papel__cuando_se_utilicen_medios_electron_fe7ec1  (label: 'Uso de medios electrónicos en lugar de papel')
[Definicion] 'ajustes — definicion' (2 nodos):
    - Definicion_ajustes_definicion__diferencias_encontradas_por_procesos_de_control_entre_los_im_df70d3  (label: 'Ajustes — definición')
    - Definicion_ajustes_definicion__presentaciones_que_no_hubieran_podido_enviar_dentro_los_plaz_3b30c2  (label: 'Ajustes — definición')
[Definicion] 'alta gerencia' (2 nodos):
    - Definicion_alta_gerencia__gerencia_general_y_aquellos_gerentes_que_tengan_poder_decisorio_y_65527e  (label: 'Alta Gerencia')
    - Definicion_alta_gerencia__gerencia_general_y_aquellos_gerentes_que_tengan_poder_decisorio_y_77f963  (label: 'Alta Gerencia')
[Definicion] 'billete sin valor' (2 nodos):
    - Definicion_billete_sin_valor__billete_que_se_encuentra_roto_perforado_quemado_o_cercenado_y_3916e6  (label: 'Billete sin valor')
    - Definicion_billete_sin_valor__el_que_presente_una_superficie_inferior_al_sesenta_por_ciento_1f5afe  (label: 'Billete sin valor')
[Definicion] 'caracteristicas de la moneda conmemorativa' (3 nodos):
    - Definicion_caracteristicas_de_la_moneda_conmemorativa__moneda_de_plata_900_calidad_proof_va_8a318f  (label: 'Características de la moneda conmemorativa')
    - Definicion_caracteristicas_de_la_moneda_conmemorativa__moneda_de_plata_900_valor_facial_de__cb6faf  (label: 'Características de la moneda conmemorativa')
    - Definicion_caracteristicas_de_la_moneda_conmemorativa__moneda_de_plata_ag_900_cu_100_con_va_b91f36  (label: 'Características de la moneda conmemorativa')
[Definicion] 'centro de transmision' (2 nodos):
    - Definicion_centro_de_transmision__elementos_de_telecomunicaciones_con_los_que_las_distintas_c8d00f  (label: 'Centro de Transmisión')
    - Definicion_centro_de_transmision__medios_de_telecomunicaciones_con_los_que_las_entidades_pa_2c8edd  (label: 'Centro de transmisión')
[Definicion] 'cheques truncados con imagen' (2 nodos):
    - Definicion_cheques_truncados_con_imagen__cheques_que_superan_el_importe_limite_definido_por_d93b61  (label: 'Cheques truncados con imagen')
    - Definicion_cheques_truncados_con_imagen__variante_de_cheques_truncados_en_la_que_se_remite__c04a4e  (label: 'Cheques truncados con imagen')
[Definicion] 'cheques truncados sin imagen' (2 nodos):
    - Definicion_cheques_truncados_sin_imagen__cheques_que_quedan_en_poder_de_la_entidad_deposita_9d583d  (label: 'Cheques truncados sin imagen')
    - Definicion_cheques_truncados_sin_imagen__variante_de_cheques_truncados_en_la_que_se_remite__67dc81  (label: 'Cheques truncados sin imagen')
[Definicion] 'codeudores — definicion' (2 nodos):
    - Definicion_codeudores_definicion__cuando_existe_mas_de_un_deudor_en_un_prestamo_hipotecario_574f4e  (label: 'Codeudores — definición')
    - Definicion_codeudores_definicion__en_caso_de_existir_mas_de_un_deudor_todos_en_su_conjunto__54c7d6  (label: 'Codeudores — definición')
[Definicion] 'codigo 10110 — efectivo' (2 nodos):
    - Definicion_codigo_10110_efectivo__componente_de_disponibilidades_en_moneda_extranjera__ri_p_c5b96a  (label: 'Código 10110 — Efectivo')
    - Definicion_codigo_10110_efectivo__efectivo_en_disponibilidades_de_activos_en_moneda_extranj_23ad14  (label: 'Código 10110 — Efectivo')
[Definicion] 'codigo 10120 — corresponsalia' (2 nodos):
    - Definicion_codigo_10120_corresponsalia__componente_de_disponibilidades_en_moneda_extranjera_c9de83  (label: 'Código 10120 — Corresponsalía')
    - Definicion_codigo_10120_corresponsalia__corresponsalia_en_disponibilidades_de_activos_en_mo_a84a53  (label: 'Código 10120 — Corresponsalía')
[Definicion] 'codigo 10130 — otros' (2 nodos):
    - Definicion_codigo_10130_otros__componente_residual_de_disponibilidades_en_moneda_extranjera_e4611d  (label: 'Código 10130 — Otros')
    - Definicion_codigo_10130_otros__otros_en_disponibilidades_de_activos_en_moneda_extranjera_re_b98a91  (label: 'Código 10130 — Otros')
[Definicion] 'codigo 10161x/001 — inversiones a plazo de uva' (2 nodos):
    - Definicion_codigo_10161x_001_inversiones_a_plazo_de_uva__incluye_inversiones_a_plazo_de_uva_e146de  (label: 'Código 10161X/001 — inversiones a plazo de UVA')
    - Definicion_codigo_10161x_001_inversiones_a_plazo_de_uva__inversiones_a_plazo_de_uva_sin_inc_789bc0  (label: 'Código 10161X/001 — Inversiones a plazo de UVA')
[Definicion] 'codigo 10180x/m — titulos valores de deuda' (2 nodos):
    - Definicion_codigo_10180x_m_titulos_valores_de_deuda__incluye_titulos_valores_de_deuda_compr_b76ad9  (label: 'Código 10180X/M — títulos valores de deuda')
    - Definicion_codigo_10180x_m_titulos_valores_de_deuda__titulos_valores_de_deuda_comprendiendo_f4b8e1  (label: 'Código 10180X/M — Títulos Valores de Deuda')
[Definicion] 'codigo 102100/m — saldos sin utilizar de adelantos en cuenta corriente' (2 nodos):
    - Definicion_codigo_102100_m_saldos_sin_utilizar_de_adelantos_en_cuenta_corriente__incluye_sa_6129e5  (label: 'Código 102100/M — saldos sin utilizar de adelantos en cuenta corriente')
    - Definicion_codigo_102100_m_saldos_sin_utilizar_de_adelantos_en_cuenta_corriente__saldos_sin_afba6c  (label: 'Código 102100/M — Saldos sin utilizar de adelantos en cuenta corriente')
[Definicion] 'codigo 10220 — titulos privados' (2 nodos):
    - Definicion_codigo_10220_titulos_privados__componente_de_titulos_de_deuda_en_moneda_extranje_d21a6a  (label: 'Código 10220 — Títulos privados')
    - Definicion_codigo_10220_titulos_privados__titulos_privados_en_titulos_de_deuda_reportado_di_f7ca9b  (label: 'Código 10220 — Títulos privados')
[Definicion] 'codigo 10230 — instrumentos de regulacion monetaria' (2 nodos):
    - Definicion_codigo_10230_instrumentos_de_regulacion_monetaria__componente_de_titulos_de_deud_8306d5  (label: 'Código 10230 — Instrumentos de regulación monetaria')
    - Definicion_codigo_10230_instrumentos_de_regulacion_monetaria__instrumentos_de_regulacion_mo_77818a  (label: 'Código 10230 — Instrumentos de regulación monetaria')
[Definicion] 'codigo 10300 — prestamos' (2 nodos):
    - Definicion_codigo_10300_prestamos__componente_de_activos_en_moneda_extranjera__ri_pgn_s3_e5d6fb  (label: 'Código 10300 — Préstamos')
    - Definicion_codigo_10300_prestamos__prestamos_en_activos_en_moneda_extranjera_reportado_diar_e251e0  (label: 'Código 10300 — Préstamos')
[Definicion] 'codigo 10400 — otros creditos por intermediacion financiera' (2 nodos):
    - Definicion_codigo_10400_otros_creditos_por_intermediacion_financiera__componente_de_activos_54e755  (label: 'Código 10400 — Otros créditos por intermediación financiera')
    - Definicion_codigo_10400_otros_creditos_por_intermediacion_financiera__otros_creditos_por_in_f9f04b  (label: 'Código 10400 — Otros créditos por intermediación financiera')
[Definicion] 'codigo 10500 — creditos por arrendamientos financieros' (2 nodos):
    - Definicion_codigo_10500_creditos_por_arrendamientos_financieros__componente_de_activos_en_m_3ded12  (label: 'Código 10500 — Créditos por arrendamientos financieros')
    - Definicion_codigo_10500_creditos_por_arrendamientos_financieros__creditos_por_arrendamiento_e3d03d  (label: 'Código 10500 — Créditos por arrendamientos financieros')
[Definicion] 'codigo 20100 — depositos' (2 nodos):
    - Definicion_codigo_20100_depositos__componente_de_pasivos_en_moneda_extranjera__ri_pgn_s3_3296e0  (label: 'Código 20100 — Depósitos')
    - Definicion_codigo_20100_depositos__depositos_en_pasivos_en_moneda_extranjera_reportado_diar_6c9387  (label: 'Código 20100 — Depósitos')
[Definicion] 'codigo 20200 — otras obligaciones por intermediacion financiera' (2 nodos):
    - Definicion_codigo_20200_otras_obligaciones_por_intermediacion_financiera__componente_de_pas_9f0499  (label: 'Código 20200 — Otras obligaciones por intermediación financiera')
    - Definicion_codigo_20200_otras_obligaciones_por_intermediacion_financiera__otras_obligacione_27ac7c  (label: 'Código 20200 — Otras obligaciones por intermediación financiera')
[Definicion] 'codigo 20300 — obligaciones negociables subordinadas' (2 nodos):
    - Definicion_codigo_20300_obligaciones_negociables_subordinadas__componente_de_pasivos_en_mon_eea89a  (label: 'Código 20300 — Obligaciones negociables subordinadas')
    - Definicion_codigo_20300_obligaciones_negociables_subordinadas__obligaciones_negociables_sub_adfcc9  (label: 'Código 20300 — Obligaciones negociables subordinadas')
[Definicion] 'codigo 30000 — derivados' (2 nodos):
    - Definicion_codigo_30000_derivados__categoria_de_derivados_que_agrupa_opciones_otros_derivad_8f37b8  (label: 'Código 30000 — Derivados')
    - Definicion_codigo_30000_derivados__derivados_reportado_diariamente_dd_con_signo_positivo_o__630a98  (label: 'Código 30000 — Derivados')
[Definicion] 'codigo 50000 — incremento por defecto de compensacion' (2 nodos):
    - Definicion_codigo_50000_incremento_por_defecto_de_compensacion__ajuste_positivo_a_la_posici_75a7ed  (label: 'Código 50000 — Incremento por defecto de compensación')
    - Definicion_codigo_50000_incremento_por_defecto_de_compensacion__incremento_por_defecto_de_c_9dccea  (label: 'Código 50000 — Incremento por defecto de compensación')
[Definicion] 'codigo 817000/001 — financiaciones ahora 12 hasta 30/09/2020' (2 nodos):
    - Definicion_codigo_817000_001_financiaciones_ahora_12_hasta_30_09_2020__saldo_de_financiacio_19aca2  (label: 'Código 817000/001 — financiaciones AHORA 12 hasta 30/09/2020')
    - Definicion_codigo_817000_001_financiaciones_ahora_12_hasta_30_09_2020__saldo_del_periodo_n__5fd27b  (label: 'Código 817000/001 — Financiaciones AHORA 12 hasta 30/09/2020')
[Definicion] 'codigo de clase de transaccion — 200' (2 nodos):
    - Definicion_codigo_de_clase_de_transaccion_200__codigo_200_que_identifica_transacciones_de_d_c4637b  (label: 'Código de clase de transacción — 200')
    - Definicion_codigo_de_clase_de_transaccion_200__el_codigo_200_identifica_transacciones_de_de_a016c2  (label: 'Código de clase de transacción — 200')
[Definicion] 'codigo de origen — entidad financiera' (2 nodos):
    - Definicion_codigo_de_origen_entidad_financiera__campo_que_contiene_el_codigo_de_origen_valo_c2b9bc  (label: 'Código de origen — Entidad financiera')
    - Definicion_codigo_de_origen_entidad_financiera__el_codigo_1_identifica_a_la_entidad_financi_e56dba  (label: 'Código de origen — Entidad financiera')
[Definicion] 'contador de registro (trace number)' (2 nodos):
    - Definicion_contador_de_registro_trace_number__campo_numerico_de_15_posiciones_posiciones_80_2169fb  (label: 'Contador de registro (Trace number)')
    - Definicion_contador_de_registro_trace_number__campo_que_contiene_el_mismo_contador_de_regis_db3a51  (label: 'Contador de registro (Trace number)')
[Definicion] 'controles de las aplicaciones' (2 nodos):
    - Definicion_controles_de_las_aplicaciones__parte_de_la_estructura_de_control_interno_que_cor_0a713e  (label: 'Controles de las aplicaciones')
    - Definicion_controles_de_las_aplicaciones__parte_de_la_estructura_de_control_interno_que_cor_599927  (label: 'Controles de las aplicaciones')
[Definicion] 'controles de monitoreo' (2 nodos):
    - Definicion_controles_de_monitoreo__parte_de_la_estructura_de_control_interno_que_correspond_2a2981  (label: 'Controles de monitoreo')
    - Definicion_controles_de_monitoreo__parte_de_la_estructura_de_control_interno_que_correspond_9b1b44  (label: 'Controles de monitoreo')
[Definicion] 'costo financiero total' (2 nodos):
    - Definicion_costo_financiero_total__porcentaje_efectivo_anual_calculado_por_aplicacion_de_lo_2ea1ae  (label: 'Costo financiero total')
    - Definicion_costo_financiero_total__porcentaje_efectivo_anual_que_resulta_de_la_aplicacion_d_9adb9d  (label: 'Costo financiero total')
[Definicion] 'cuentas corrientes especiales en el bcra para acreditacion de haberes previsionales' (2 nodos):
    - Definicion_cuentas_corrientes_especiales_en_el_bcra_para_acreditacion_de_haberes_previsiona_10ad0f  (label: 'Cuentas corrientes especiales en el BCRA para acreditación de haberes previsionales')
    - Definicion_cuentas_corrientes_especiales_en_el_bcra_para_acreditacion_de_haberes_previsiona_2a6409  (label: 'Cuentas corrientes especiales en el BCRA para acreditación de haberes previsionales')
[Definicion] 'depositos del sector financiero local' (2 nodos):
    - Definicion_depositos_del_sector_financiero_local__concepto_de_depositos_del_sector_financie_a89600  (label: 'Depósitos del sector financiero local')
    - Definicion_depositos_del_sector_financiero_local__concepto_de_informacion_a_reportar_con_co_28f9ad  (label: 'Depósitos del sector financiero local')
[Definicion] 'deudor — tomador del credito' (2 nodos):
    - Definicion_deudor_tomador_del_credito__tomador_del_credito__manori_1_1_2_1_f4e1d9  (label: 'Deudor — tomador del crédito')
    - Definicion_deudor_tomador_del_credito__tomador_del_credito__manori_3_1_2_1_b37b00  (label: 'Deudor — tomador del crédito')
[Definicion] 'dias habiles para compensacion' (3 nodos):
    - Definicion_dias_habiles_para_compensacion__todos_aquellos_dias_que_el_bcra_defina_como_tale_b07db2  (label: 'Días hábiles para compensación')
    - Definicion_dias_habiles_para_compensacion__todos_aquellos_dias_que_el_bcra_defina_como_tale_b462c7  (label: 'Días hábiles para compensación')
    - Definicion_dias_habiles_para_compensacion__todos_aquellos_que_el_bcra_defina_como_tales__sn_834f0b  (label: 'Días hábiles para compensación')
[Definicion] 'diseno anverso moneda conmemorativa' (2 nodos):
    - Definicion_diseno_anverso_moneda_conmemorativa__el_anverso_presenta_en_la_impronta_central__8ee13e  (label: 'Diseño anverso moneda conmemorativa')
    - Definicion_diseno_anverso_moneda_conmemorativa__en_el_centro_imagen_del_palacio_del_congres_403fb8  (label: 'Diseño anverso moneda conmemorativa')
[Definicion] 'diseno reverso moneda conmemorativa' (2 nodos):
    - Definicion_diseno_reverso_moneda_conmemorativa__el_reverso_muestra_en_el_centro_en_la_mitad_5b9d43  (label: 'Diseño reverso moneda conmemorativa')
    - Definicion_diseno_reverso_moneda_conmemorativa__en_el_centro_escudo_nacional_argentino_en_r_67c73b  (label: 'Diseño reverso moneda conmemorativa')
[Definicion] 'efectivo en custodia en otras entidades financieras' (2 nodos):
    - Definicion_efectivo_en_custodia_en_otras_entidades_financieras__concepto_de_efectivo_en_cus_0e87b1  (label: 'Efectivo en custodia en otras entidades financieras')
    - Definicion_efectivo_en_custodia_en_otras_entidades_financieras__concepto_de_informacion_a_r_848386  (label: 'Efectivo en custodia en otras entidades financieras')
[Definicion] 'efectivo en las casas de la entidad' (2 nodos):
    - Definicion_efectivo_en_las_casas_de_la_entidad__concepto_de_efectivo_en_las_casas_de_la_ent_e3539a  (label: 'Efectivo en las casas de la entidad')
    - Definicion_efectivo_en_las_casas_de_la_entidad__concepto_de_informacion_a_reportar_con_codi_423129  (label: 'Efectivo en las casas de la entidad')
[Definicion] 'efectivo en transportadoras de valores y en transito' (2 nodos):
    - Definicion_efectivo_en_transportadoras_de_valores_y_en_transito__concepto_de_efectivo_en_tr_4be415  (label: 'Efectivo en Transportadoras de Valores y en tránsito')
    - Definicion_efectivo_en_transportadoras_de_valores_y_en_transito__concepto_de_informacion_a__94f5b9  (label: 'Efectivo en Transportadoras de Valores y en tránsito')
[Definicion] 'entidad de la transaccion original' (2 nodos):
    - Definicion_entidad_de_la_transaccion_original__campo_de_registro_que_identifica_la_entidad__ae3e6c  (label: 'Entidad de la transacción original')
    - Definicion_entidad_de_la_transaccion_original__campo_que_contiene_la_identificacion_de_la_e_1ed0b3  (label: 'Entidad de la transacción original')
[Definicion] 'estado actual del prestamo' (2 nodos):
    - Definicion_estado_actual_del_prestamo__indicar_si_se_encuentra_en_situacion_normal_con_atra_2cf6cc  (label: 'Estado actual del préstamo')
    - Definicion_estado_actual_del_prestamo__situacion_del_prestamo_normal_con_atrasos_de_hasta_3_d8d612  (label: 'Estado actual del préstamo')
[Definicion] 'fecha de pago' (2 nodos):
    - Definicion_fecha_de_pago__indicar_la_fecha_de_efectivo_pago_realizado_por_el_deudor__manori_d53b00  (label: 'Fecha de pago')
    - Definicion_fecha_de_pago__la_fecha_de_efectivo_pago_realizado_por_el_deudor__manori_3_4_2_980fe0  (label: 'Fecha de pago')
[Definicion] 'fecha de vencimiento' (2 nodos):
    - Definicion_fecha_de_vencimiento__fecha_de_vencimiento_establecida_de_la_cuota__manori_1_4_2_e0e219  (label: 'Fecha de Vencimiento')
    - Definicion_fecha_de_vencimiento__fecha_de_vencimiento_establecida_de_la_cuota__manori_3_4_2_bba183  (label: 'Fecha de vencimiento')
[Definicion] 'historia de incumplimientos' (2 nodos):
    - Definicion_historia_de_incumplimientos__indicar_la_cantidad_de_veces_que_se_ha_incurrido_en_50ba99  (label: 'Historia de incumplimientos')
    - Definicion_historia_de_incumplimientos__la_cantidad_de_veces_que_se_ha_incurrido_en_atrasos_60f9d7  (label: 'Historia de incumplimientos')
[Definicion] 'identificacion de la entidad originante' (2 nodos):
    - Definicion_identificacion_de_la_entidad_originante__campo_numerico_que_contiene_el_numero_i_da18df  (label: 'Identificación de la entidad originante')
    - Definicion_identificacion_de_la_entidad_originante__campo_que_contiene_el_codigo_de_la_enti_5180fe  (label: 'Identificación de la entidad originante')
[Definicion] 'identificador de registro — cabecera de archivo' (2 nodos):
    - Definicion_identificador_de_registro_cabecera_de_archivo__codigo_que_identifica_el_tipo_de__b205bf  (label: 'Identificador de registro — Cabecera de archivo')
    - Definicion_identificador_de_registro_cabecera_de_archivo__codigo_que_se_asigna_para_identif_d37114  (label: 'Identificador de registro — cabecera de archivo')
[Definicion] 'identificador de registro — cabecera de lote' (2 nodos):
    - Definicion_identificador_de_registro_cabecera_de_lote__campo_que_identifica_el_registro_com_b99d91  (label: 'Identificador de registro — Cabecera de lote')
    - Definicion_identificador_de_registro_cabecera_de_lote__en_la_cabecera_de_lote_el_identifica_13a98a  (label: 'Identificador de registro — Cabecera de lote')
[Definicion] 'identificador de registro — tipo 6' (2 nodos):
    - Definicion_identificador_de_registro_tipo_6__campo_de_tipo_6_que_identifica_un_registro_ind_8c7515  (label: 'Identificador de registro — tipo 6')
    - Definicion_identificador_de_registro_tipo_6__registro_individual_identificado_con_el_codigo_1fa15f  (label: 'Identificador de registro — tipo 6')
[Definicion] 'ingresos computables — empleados dependencia' (2 nodos):
    - Definicion_ingresos_computables_empleados_dependencia__para_empleados_en_relacion_de_depend_b9c924  (label: 'Ingresos computables — empleados dependencia')
    - Definicion_ingresos_computables_empleados_dependencia__para_empleados_en_relacion_de_depend_ce3d62  (label: 'Ingresos computables — empleados dependencia')
[Definicion] 'ingresos computables — otras rentas' (2 nodos):
    - Definicion_ingresos_computables_otras_rentas__ingresos_por_rentas_promedio_mensual_ultimos__68049d  (label: 'Ingresos computables — otras rentas')
    - Definicion_ingresos_computables_otras_rentas__para_otras_rentas_ingresos_por_rentas_con_pro_ff1c6a  (label: 'Ingresos computables — otras rentas')
[Definicion] 'ingresos computables — trabajadores autonomos' (2 nodos):
    - Definicion_ingresos_computables_trabajadores_autonomos__para_trabajadores_autonomos_promedi_818151  (label: 'Ingresos computables — trabajadores autónomos')
    - Definicion_ingresos_computables_trabajadores_autonomos__para_trabajadores_autonomos_promedi_cf4a89  (label: 'Ingresos computables — trabajadores autónomos')
[Definicion] 'modificacion de terminos' (2 nodos):
    - Definicion_modificacion_de_terminos__indicar_si_los_terminos_originales_fueron_modificados__58a0ea  (label: 'Modificación de términos')
    - Definicion_modificacion_de_terminos__si_los_terminos_originales_fueron_modificados_con_post_5cd6b5  (label: 'Modificación de términos')
[Definicion] 'moneda de pago' (2 nodos):
    - Definicion_moneda_de_pago__la_moneda_de_pago_del_credito_es_pesos__manori_sbloque5_48fa98  (label: 'Moneda de pago')
    - Definicion_moneda_de_pago__pesos__manori_sbloque4_d9b2c1  (label: 'Moneda de pago')
[Definicion] 'monto de la cuota' (2 nodos):
    - Definicion_monto_de_la_cuota__capital_intereses_impuestos_comisiones_y_cargos_tales_como_el_3997ab  (label: 'Monto de la cuota')
    - Definicion_monto_de_la_cuota__indicar_capital_intereses_impuestos_comisiones_y_cargos_tales_90fd32  (label: 'Monto de la cuota')
[Definicion] 'monto de la proxima cuota' (2 nodos):
    - Definicion_monto_de_la_proxima_cuota__capital_intereses_impuestos_comisiones_y_cargos_tales_2e30bd  (label: 'Monto de la próxima cuota')
    - Definicion_monto_de_la_proxima_cuota__indicar_capital_intereses_impuestos_comisiones_y_carg_0f73c7  (label: 'Monto de la próxima cuota')
[Definicion] 'monto pagado' (2 nodos):
    - Definicion_monto_pagado__el_monto_pagado_por_el_deudor__manori_3_4_2_edc617  (label: 'Monto pagado')
    - Definicion_monto_pagado__indicar_el_monto_pagado_por_el_deudor__manori_1_4_2_c836d2  (label: 'Monto pagado')
[Definicion] 'monto precancelado' (2 nodos):
    - Definicion_monto_precancelado__indicar_los_montos_de_capital_precancelados_por_el_deudor_co_b0a7bc  (label: 'Monto precancelado')
    - Definicion_monto_precancelado__los_montos_de_capital_precancelados_por_el_deudor_entre_el_d_4152bc  (label: 'Monto precancelado')
[Definicion] 'monto promedio de facturas impagas' (2 nodos):
    - Definicion_monto_promedio_de_facturas_impagas__cociente_de_la_suma_de_los_montos_adeudados__c8e094  (label: 'Monto promedio de facturas impagas')
    - Definicion_monto_promedio_de_facturas_impagas__cociente_de_la_suma_de_los_montos_adeudados__d81962  (label: 'Monto promedio de facturas impagas')
[Definicion] 'numero de cuota' (2 nodos):
    - Definicion_numero_de_cuota__es_el_numero_de_la_cuota_que_corresponda__manori_1_4_2_8961dc  (label: 'Número de Cuota')
    - Definicion_numero_de_cuota__es_el_numero_de_la_cuota_que_corresponda__manori_3_4_2_e11ed0  (label: 'Número de cuota')
[Definicion] 'numero de lote' (3 nodos):
    - Definicion_numero_de_lote__campo_numerico_que_contiene_el_numero_de_lote_determinado_por_la_471c50  (label: 'Número de lote')
    - Definicion_numero_de_lote__campo_que_contiene_el_numero_de_lote_determinado_por_la_entidad__8fdc97  (label: 'Número de lote')
    - Definicion_numero_de_lote__contiene_el_numero_de_lote_determinado_por_la_entidad_de_origen__433b4f  (label: 'Número de lote')
[Definicion] 'plazo remanente en meses' (2 nodos):
    - Definicion_plazo_remanente_en_meses__el_plazo_remanente_actualizado_expresado_en_meses__man_71f034  (label: 'Plazo remanente en meses')
    - Definicion_plazo_remanente_en_meses__este_campo_debe_reflejar_el_plazo_remanente_actualizad_bbc62d  (label: 'Plazo remanente en meses')
[Definicion] 'porcentaje de facturas canceladas fuera de termino' (2 nodos):
    - Definicion_porcentaje_de_facturas_canceladas_fuera_de_termino__cociente_entre_la_sumatoria__101052  (label: 'Porcentaje de facturas canceladas fuera de término')
    - Definicion_porcentaje_de_facturas_canceladas_fuera_de_termino__cociente_entre_la_sumatoria__911cf2  (label: 'Porcentaje de facturas canceladas fuera de término')
[Definicion] 'promedio de dias de atraso' (2 nodos):
    - Definicion_promedio_de_dias_de_atraso__cociente_entre_la_sumatoria_de_la_cantidad_de_dias_d_3a2d3d  (label: 'Promedio de días de atraso')
    - Definicion_promedio_de_dias_de_atraso__cociente_entre_la_sumatoria_de_la_cantidad_de_dias_d_c0a7b9  (label: 'Promedio de días de atraso')
[Definicion] 'r02 — cuenta cerrada por orden judicial' (2 nodos):
    - Definicion_r02_cuenta_cerrada_por_orden_judicial__codigo_de_rechazo_utilizado_cuando_la_cue_80dc0e  (label: 'R02 — Cuenta cerrada por orden judicial')
    - Definicion_r02_cuenta_cerrada_por_orden_judicial__codigo_de_rechazo_utilizado_por_la_entida_a60672  (label: 'R02 — Cuenta cerrada por orden judicial')
[Definicion] 'r81 — fuerza mayor' (2 nodos):
    - Definicion_r81_fuerza_mayor__codigo_de_rechazo_utilizado_por_los_bancos_cuando_existen_caus_cbfd11  (label: 'R81 — Fuerza mayor')
    - Definicion_r81_fuerza_mayor__codigo_de_rechazo_utilizado_por_los_bancos_girados_cuando_exis_dd76b4  (label: 'R81 — Fuerza mayor')
[Definicion] 'rechazos de la entidad girada' (2 nodos):
    - Definicion_rechazos_de_la_entidad_girada__rechazos_que_la_entidad_girada_realiza_cuando_ver_69761d  (label: 'Rechazos de la entidad girada')
    - Definicion_rechazos_de_la_entidad_girada__son_los_rechazos_que_la_entidad_girada_realiza_cu_0f9cd2  (label: 'Rechazos de la entidad girada')
[Definicion] 'relacion cuota/ingreso — concepto' (2 nodos):
    - Definicion_relacion_cuota_ingreso_concepto__relacion_porcentual_entre_el_monto_total_de_la__ca9a13  (label: 'Relación Cuota/Ingreso — concepto')
    - Definicion_relacion_cuota_ingreso_concepto__relacion_porcentual_entre_el_monto_total_de_la__cb68d4  (label: 'Relación Cuota/Ingreso — concepto')
[Definicion] 'relacion total cuotas / ingreso' (2 nodos):
    - Definicion_relacion_total_cuotas_ingreso__la_relacion_sobre_los_ingresos_computables_de_los_c2b414  (label: 'Relación Total Cuotas / Ingreso')
    - Definicion_relacion_total_cuotas_ingreso__relacion_entre_los_ingresos_mensuales_computables_5e3934  (label: 'Relación Total Cuotas / Ingreso')
[Definicion] 'responsabilidad patrimonial computable (rpc)' (2 nodos):
    - Definicion_responsabilidad_patrimonial_computable_rpc__suma_algebraica_de_conceptos_segun_e_92f871  (label: 'Responsabilidad patrimonial computable (RPC)')
    - Definicion_responsabilidad_patrimonial_computable_rpc__suma_algebraica_de_conceptos_segun_e_daf6ed  (label: 'Responsabilidad patrimonial computable (RPC)')
[Definicion] 'riesgo de mercado' (2 nodos):
    - Definicion_riesgo_de_mercado__la_posibilidad_de_sufrir_perdidas_en_posiciones_dentro_y_fuer_485b3c  (label: 'Riesgo de mercado')
    - Definicion_riesgo_de_mercado__posibilidad_de_sufrir_perdidas_en_posiciones_dentro_y_fuera_d_969ce3  (label: 'Riesgo de mercado')
[Definicion] 'saldo de capital' (2 nodos):
    - Definicion_saldo_de_capital__el_saldo_de_capital_una_vez_abonada_la_cuota__manori_3_4_2_9c0ebf  (label: 'Saldo de Capital')
    - Definicion_saldo_de_capital__indicar_el_saldo_de_capital_una_vez_abonada_la_cuota__manori_1_34c853  (label: 'Saldo de capital')
[Definicion] 'sistema contable' (2 nodos):
    - Definicion_sistema_contable__parte_importante_de_la_estructura_de_control_interno_que_compr_333de2  (label: 'Sistema contable')
    - Definicion_sistema_contable__parte_importante_de_la_estructura_de_control_interno_que_compr_881247  (label: 'Sistema contable')
[Definicion] 'tasa de interes vigente' (2 nodos):
    - Definicion_tasa_de_interes_vigente__indicar_la_tasa_nominal_anual_aplicada_para_el_calculo__4992b9  (label: 'Tasa de interés vigente')
    - Definicion_tasa_de_interes_vigente__la_tasa_nominal_anual_aplicada_para_el_calculo_de_la_cu_38194e  (label: 'Tasa de interés vigente')
[Definicion] 'tipo y numero de clave de identificacion' (2 nodos):
    - Definicion_tipo_y_numero_de_clave_de_identificacion__cuit_cuil_o_cdi_segun_corresponda__cir_a157d7  (label: 'Tipo y número de clave de identificación')
    - Definicion_tipo_y_numero_de_clave_de_identificacion__cuit_cuil_o_cdi_segun_corresponda__cir_e1f5f7  (label: 'Tipo y número de clave de identificación')
[Excepcion] 'excepcion informacion historica del cliente' (2 nodos):
    - Excepcion_el_requisito_de_informe_comercial_o_crediticio_no_aplica_cuando_la_entidad_dispo_5a58f1  (label: 'Excepción información histórica del cliente')
    - Excepcion_el_requisito_de_requerir_un_informe_comercial_o_crediticio_puede_ser_exceptuado__f12283  (label: 'Excepción información histórica del cliente')
[Excepcion] 'excepcion limite punto 3.10.3' (2 nodos):
    - Excepcion_el_limite_previsto_en_el_punto_3_10_3_no_aplica_a_los_creditos_asociados_al_cobr_7afe59  (label: 'Excepción límite punto 3.10.3')
    - Excepcion_el_limite_previsto_en_el_punto_3_10_3_no_aplica_a_los_creditos_por_cobro_de_depo_0eb5c3  (label: 'Excepción límite punto 3.10.3')
[Excepcion] 'excepcion pases con bcra' (2 nodos):
    - Excepcion_las_disposiciones_de_estas_normas_no_se_aplican_a_las_operaciones_de_pases_que_l_ad04cb  (label: 'Excepción pases con BCRA')
    - Excepcion_quedan_exceptuadas_de_las_restricciones_sobre_operaciones_activas_las_operacione_7ef328  (label: 'Excepción pases con BCRA')
[Excepcion] 'excepcion por solicitud de facilidades de pago' (2 nodos):
    - Excepcion_la_exclusion_del_registro_no_aplica_cuando_se_solicitan_facilidades_para_la_canc_50e56f  (label: 'Excepción por solicitud de facilidades de pago')
    - Excepcion_la_exclusion_no_aplica_cuando_se_solicitan_facilidades_para_la_cancelacion_de_la_752e2a  (label: 'Excepción por solicitud de facilidades de pago')
[Excepcion] 'excepcion sector publico no financiero' (2 nodos):
    - Excepcion_el_sector_publico_no_financiero_queda_exceptuado_de_la_estimacion_del_deterioro__f9a2d6  (label: 'Excepción Sector Público no Financiero')
    - Excepcion_no_aplica_la_estimacion_de_deterioro_al_sector_publico_no_financiero__ri_dcpc_7__ef0553  (label: 'Excepción Sector Público no Financiero')
[Excepcion] 'exclusion de partidas sin codigo swift' (2 nodos):
    - Excepcion_se_excluyen_de_la_identificacion_segun_moneda_de_origen_aquellas_partidas_que_no_d4cc99  (label: 'Exclusión de partidas sin código SWIFT')
    - Excepcion_se_excluyen_de_la_identificacion_segun_siscen_tabla_t0003_aquellas_partidas_que__a84f6c  (label: 'Exclusión de partidas sin código SWIFT')
[Excepcion] 'separacion fisica de anexos al legajo' (3 nodos):
    - Excepcion_excepcion_a_la_exigencia_de_que_la_carpeta_legal_este_anexa_al_legajo_del_client_d82671  (label: 'Separación física de anexos al legajo')
    - Excepcion_los_anexos_al_legajo_del_cliente_pueden_estar_separados_fisicamente_si_se_cumple_03e726  (label: 'Separación física de anexos al legajo')
    - Excepcion_los_anexos_al_legajo_del_cliente_pueden_estar_separados_fisicamente_siempre_que__3ea131  (label: 'Separación física de anexos al legajo')
[Obligacion] 'acreditacion cumplimiento condiciones seguridad' (2 nodos):
    - Obligacion_en_la_comunicacion_de_instalacion_de_dependencias_automatizadas_mediante_la_inte_7bc966  (label: 'Acreditación cumplimiento condiciones seguridad')
    - Obligacion_en_la_comunicacion_de_instalacion_de_los_pertinentes_dispositivos_se_debera_cons_beaaf9  (label: 'Acreditación cumplimiento condiciones seguridad')
[Obligacion] 'actualizacion diaria de pagina de consultas' (2 nodos):
    - Obligacion_la_pagina_de_internet_del_bcra_sera_actualizada_diariamente_con_la_informacion_d_2a61e6  (label: 'Actualización diaria de página de consultas')
    - Obligacion_mantener_actualizada_diariamente_la_pagina_de_internet_del_bcra_que_permite_cons_22e4e6  (label: 'Actualización diaria de página de consultas')
[Obligacion] 'aplicacion de disposiciones de caja de ahorros' (2 nodos):
    - Obligacion_deber_de_aplicar_el_regimen_normativo_establecido_para_los_depositos_en_caja_de__f823e2  (label: 'Aplicación de disposiciones de caja de ahorros')
    - Obligacion_las_disposiciones_establecidas_para_los_depositos_en_caja_de_ahorros_en_los_punt_6a2162  (label: 'Aplicación de disposiciones de caja de ahorros')
[Obligacion] 'aplicacion de disposiciones de depositos en caja de ahorros' (3 nodos):
    - Obligacion_se_aplicaran_las_disposiciones_establecidas_para_los_depositos_en_caja_de_ahorro_c545bf  (label: 'Aplicación de disposiciones de depósitos en caja de ahorros')
    - Obligacion_seran_de_aplicacion_las_disposiciones_establecidas_para_los_depositos_en_caja_de_0a2af0  (label: 'Aplicación de disposiciones de depósitos en caja de ahorros')
    - Obligacion_seran_de_aplicacion_las_disposiciones_establecidas_para_los_depositos_en_caja_de_51343a  (label: 'Aplicación de disposiciones de depósitos en caja de ahorros')
[Obligacion] 'aplicar procedimientos sustantivos suficientes' (2 nodos):
    - Obligacion_la_auditoria_interna_debera_aplicar_procedimientos_sustantivos_suficientes_que_a_512b86  (label: 'Aplicar procedimientos sustantivos suficientes')
    - Obligacion_la_auditoria_interna_debera_aplicar_procedimientos_sustantivos_suficientes_que_a_d57f53  (label: 'Aplicar procedimientos sustantivos suficientes')
[Obligacion] 'aprobacion de excepciones a politicas y limites' (2 nodos):
    - Obligacion_el_directorio_debe_aprobar_las_excepciones_a_las_politicas_y_limites_que_impliqu_96f394  (label: 'Aprobación de excepciones a políticas y límites')
    - Obligacion_el_directorio_debera_aprobar_las_excepciones_a_las_politicas_y_limites_que_impli_b24182  (label: 'Aprobación de excepciones a políticas y límites')
[Obligacion] 'aprobacion nivel tolerancia riesgo' (2 nodos):
    - Obligacion_el_directorio_debe_aprobar_el_nivel_de_tolerancia_al_riesgo_de_la_entidad_defini_0fe21d  (label: 'Aprobación nivel tolerancia riesgo')
    - Obligacion_el_directorio_debera_aprobar_el_nivel_de_tolerancia_al_riesgo_de_la_entidad_fina_5ce46e  (label: 'Aprobación nivel tolerancia riesgo')
[Obligacion] 'asegurar controles internos para proteger integridad' (2 nodos):
    - Obligacion_la_alta_gerencia_debe_asegurar_la_existencia_de_controles_internos_adecuados_par_3e7d24  (label: 'Asegurar controles internos para proteger integridad')
    - Obligacion_la_alta_gerencia_es_responsable_de_asegurar_la_existencia_de_controles_internos__473b66  (label: 'Asegurar controles internos para proteger integridad')
[Obligacion] 'asignacion de responsabilidades y autoridad para activar plan' (3 nodos):
    - Obligacion_el_plan_debe_contemplar_el_establecimiento_de_una_asignacion_de_responsabilidade_6642b9  (label: 'Asignación de responsabilidades y autoridad para activar plan')
    - Obligacion_el_plan_debe_contemplar_la_asignacion_de_responsabilidades_incluyendo_la_designa_35e90d  (label: 'Asignación de responsabilidades y autoridad para activar plan')
    - Obligacion_el_plan_debe_incluir_el_establecimiento_de_una_asignacion_de_responsabilidades_i_db25b6  (label: 'Asignación de responsabilidades y autoridad para activar plan')
[Obligacion] 'cec: administrar red de telecomunicaciones' (2 nodos):
    - Obligacion_administrar_la_red_de_telecomunicaciones_entre_su_propio_centro_de_computos_y_el_83f06d  (label: 'CEC: administrar red de telecomunicaciones')
    - Obligacion_la_cec_debe_administrar_la_red_de_telecomunicaciones_entre_su_propio_centro_de_c_4efa72  (label: 'CEC: administrar red de telecomunicaciones')
[Obligacion] 'cec: almacenar informacion procesada' (2 nodos):
    - Obligacion_almacenar_la_informacion_procesada_en_medios_adecuados_de_manera_de_asegurar_su__437bfe  (label: 'CEC: almacenar información procesada')
    - Obligacion_la_cec_debe_almacenar_la_informacion_procesada_en_medios_adecuados_de_manera_de__8b1666  (label: 'CEC: almacenar información procesada')
[Obligacion] 'cec: efectuar controles sobre transacciones' (2 nodos):
    - Obligacion_efectuar_los_controles_correspondientes_sobre_las_transacciones_recibidas_y_pres_f65303  (label: 'CEC: efectuar controles sobre transacciones')
    - Obligacion_la_cec_debe_efectuar_los_controles_correspondientes_sobre_las_transacciones_reci_fe17bc  (label: 'CEC: efectuar controles sobre transacciones')
[Obligacion] 'cec: proveer informacion para calculo de facturacion' (2 nodos):
    - Obligacion_la_cec_debe_proveer_la_informacion_necesaria_a_las_entidades_para_el_calculo_de__555ad6  (label: 'CEC: proveer información para cálculo de facturación')
    - Obligacion_proveer_la_informacion_necesaria_a_las_entidades_para_el_calculo_de_facturacion__8e2748  (label: 'CEC: proveer información para cálculo de facturación')
[Obligacion] 'certificacion de firmas de autoridades extranjeras' (2 nodos):
    - Obligacion_las_firmas_de_las_autoridades_extranjeras_intervinientes_deberan_estar_certifica_42366a  (label: 'Certificación de firmas de autoridades extranjeras')
    - Obligacion_las_firmas_de_las_autoridades_extranjeras_intervinientes_deberan_estar_certifica_ad4acd  (label: 'Certificación de firmas de autoridades extranjeras')
[Obligacion] 'completar campo reservado con ceros' (2 nodos):
    - Obligacion_el_campo_16_reservado_debe_completarse_con_ceros__snp_cheq_7_1_12_14b576  (label: 'Completar campo reservado con ceros')
    - Obligacion_se_completara_el_campo_reservado_con_ceros__snp_cheq_7_1_13_79da1f  (label: 'Completar campo reservado con ceros')
[Obligacion] 'completar campos alfanumericos con blancos a derecha' (3 nodos):
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_de_los_requeridos_debe_complet_af5843  (label: 'Completar campos alfanuméricos con blancos a derecha')
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_de_los_requeridos_se_debe_llen_142562  (label: 'Completar campos alfanuméricos con blancos a derecha')
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_que_los_requeridos_se_debera_l_364c02  (label: 'Completar campos alfanuméricos con blancos a derecha')
[Obligacion] 'completar campos alfanumericos con blancos a la derecha' (3 nodos):
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_de_los_requeridos_para_la_info_d0f7b3  (label: 'Completar campos alfanuméricos con blancos a la derecha')
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_que_los_requeridos_para_la_inf_2da236  (label: 'Completar campos alfanuméricos con blancos a la derecha')
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_que_los_requeridos_para_la_inf_c8bff2  (label: 'Completar campos alfanuméricos con blancos a la derecha')
[Obligacion] 'completar campos numericos con ceros a izquierda' (5 nodos):
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_de_los_requeridos_debe_completarse_e66ee7  (label: 'Completar campos numéricos con ceros a izquierda')
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_de_los_requeridos_se_debe_llenar_c_495813  (label: 'Completar campos numéricos con ceros a izquierda')
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_de_los_requeridos_se_debera_llenar_870826  (label: 'Completar campos numéricos con ceros a izquierda')
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_que_los_requeridos_se_debera_llena_fdb507  (label: 'Completar campos numéricos con ceros a izquierda')
    - Obligacion_los_campos_numericos_que_posean_mas_caracteres_de_los_requeridos_deben_completar_634fa3  (label: 'Completar campos numéricos con ceros a izquierda')
[Obligacion] 'completar campos numericos con ceros a la izquierda' (3 nodos):
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_de_los_requeridos_para_la_informac_3a76ce  (label: 'Completar campos numéricos con ceros a la izquierda')
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_que_los_requeridos_para_la_informa_1f738d  (label: 'Completar campos numéricos con ceros a la izquierda')
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_que_los_requeridos_para_la_informa_e25567  (label: 'Completar campos numéricos con ceros a la izquierda')
[Obligacion] 'completar campos numericos sin ceros a la izquierda' (2 nodos):
    - Obligacion_los_campos_numericos_cuya_longitud_es_igual_a_la_maxima_longitud_definida_no_deb_58da2c  (label: 'Completar campos numéricos sin ceros a la izquierda')
    - Obligacion_los_campos_numericos_cuya_longitud_sea_igual_a_la_maxima_longitud_definida_no_de_520990  (label: 'Completar campos numéricos sin ceros a la izquierda')
[Obligacion] 'completar numero de cheque en 8 posiciones' (2 nodos):
    - Obligacion_el_campo_6_numero_de_cheque_debe_completarse_con_el_numero_de_cheque_en_8_posici_72dd68  (label: 'Completar número de cheque en 8 posiciones')
    - Obligacion_se_completara_con_el_numero_de_cheque_en_8_posiciones_incluido_en_las_posiciones_6495d0  (label: 'Completar número de cheque en 8 posiciones')
[Obligacion] 'completar numero de cuenta en 11 posiciones' (2 nodos):
    - Obligacion_el_campo_7_numero_de_cuenta_debe_completarse_con_el_numero_de_cuenta_en_11_posic_bf0cd9  (label: 'Completar número de cuenta en 11 posiciones')
    - Obligacion_se_completara_con_el_numero_de_cuenta_en_11_posiciones_incluido_en_las_posicione_dd1a0f  (label: 'Completar número de cuenta en 11 posiciones')
[Obligacion] 'completar y firmar solicitud de prestamo' (2 nodos):
    - Obligacion_los_solicitantes_deberan_completar_y_firmar_una_solicitud_de_prestamo__manori_1__eba4b9  (label: 'Completar y firmar solicitud de préstamo')
    - Obligacion_los_solicitantes_deberan_completar_y_firmar_una_solicitud_de_prestamo_que_debera_3c65a0  (label: 'Completar y firmar solicitud de préstamo')
[Obligacion] 'comunicacion a entidades de rechazo de solicitud' (2 nodos):
    - Obligacion_la_circunstancia_de_no_dar_curso_a_una_solicitud_sera_puesta_en_conocimiento_de__b97805  (label: 'Comunicación a entidades de rechazo de solicitud')
    - Obligacion_la_circunstancia_de_no_presentacion_ajustada_a_los_requisitos_sera_puesta_en_con_bce5cb  (label: 'Comunicación a entidades de rechazo de solicitud')
[Obligacion] 'comunicacion fehaciente si no hay respuesta' (2 nodos):
    - Obligacion_si_no_se_obtiene_respuesta_a_las_notificaciones_previas_debe_enviarse_una_comuni_1875b6  (label: 'Comunicación fehaciente si no hay respuesta')
    - Obligacion_si_no_se_obtiene_respuesta_a_las_notificaciones_previas_el_administrador_debe_en_7d1c32  (label: 'Comunicación fehaciente si no hay respuesta')
[Obligacion] 'comunicacion inmediata a sefyc' (3 nodos):
    - Obligacion_deber_de_comunicar_de_inmediato_a_la_superintendencia_de_entidades_financieras_y_7d248b  (label: 'Comunicación inmediata a SEFyC')
    - Obligacion_deber_de_comunicar_de_inmediato_a_la_superintendencia_de_entidades_financieras_y_9b0813  (label: 'Comunicación inmediata a SEFyC')
    - Obligacion_obligacion_de_comunicar_de_inmediato_a_la_sefyc__expaef_6_6_6033b8  (label: 'Comunicación inmediata a SEFyC')
[Obligacion] 'comunicacion inmediata a sefyc — informacion del desenvolvimiento' (3 nodos):
    - Obligacion_comunicar_de_inmediato_a_la_sefyc_cualquier_otra_informacion_relacionada_con_el__0219b6  (label: 'Comunicación inmediata a SEFyC — información del desenvolvimiento')
    - Obligacion_comunicar_de_inmediato_a_la_sefyc_cualquier_otra_informacion_relacionada_con_el__254b1b  (label: 'Comunicación inmediata a SEFyC — información del desenvolvimiento')
    - Obligacion_comunicar_de_inmediato_a_la_sefyc_cualquier_otra_informacion_relacionada_con_el__49e810  (label: 'Comunicación inmediata a SEFyC — información del desenvolvimiento')
[Obligacion] 'comunicacion previa a titulares — cierre de cuenta' (2 nodos):
    - Obligacion_comunicacion_previa_a_los_titulares_a_la_direccion_de_correo_electronico_informa_8d2a84  (label: 'Comunicación previa a titulares — cierre de cuenta')
    - Obligacion_la_entidad_debe_comunicar_previamente_a_los_titulares_por_correo_mediante_pieza__492291  (label: 'Comunicación previa a titulares — cierre de cuenta')
[Obligacion] 'conservacion de documentacion de transferencias' (2 nodos):
    - Obligacion_las_entidades_deben_conservar_en_el_legajo_de_la_cuenta_especial_una_copia_de_la_479846  (label: 'Conservación de documentación de transferencias')
    - Obligacion_las_entidades_deben_conservar_en_el_legajo_de_la_cuenta_una_copia_de_la_document_20bcbd  (label: 'Conservación de documentación de transferencias')
[Obligacion] 'consignar casa de la entidad' (2 nodos):
    - Obligacion_en_la_comunicacion_de_instalacion_de_dependencias_automatizadas_se_debera_consig_9da043  (label: 'Consignar casa de la entidad')
    - Obligacion_en_la_comunicacion_de_instalacion_del_puesto_se_debera_consignar_la_casa_de_la_e_ab38d9  (label: 'Consignar casa de la entidad')
[Obligacion] 'consignar datos en comunicacion de instalacion' (3 nodos):
    - Obligacion_en_la_comunicacion_de_instalacion_de_dependencias_automatizadas_mediante_la_inte_2ebb35  (label: 'Consignar datos en comunicación de instalación')
    - Obligacion_en_la_comunicacion_de_instalacion_de_los_pertinentes_dispositivos_se_debera_cons_e2c370  (label: 'Consignar datos en comunicación de instalación')
    - Obligacion_en_la_comunicacion_de_instalacion_del_puesto_se_debera_consignar_los_requisitos__bd203e  (label: 'Consignar datos en comunicación de instalación')
[Obligacion] 'constar comisiones en anexo' (2 nodos):
    - Obligacion_las_comisiones_o_cargos_por_servicios_adicionales_deben_constar_en_el_anexo_al_t_0ce965  (label: 'Constar comisiones en anexo')
    - Obligacion_las_comisiones_o_cargos_por_servicios_adicionales_deben_constar_en_el_anexo_refe_4e62cc  (label: 'Constar comisiones en anexo')
[Obligacion] 'constituir domicilio especial en caba' (2 nodos):
    - Obligacion_en_la_presentacion_se_consignara_y_acompanara_domicilio_especial_en_la_ciudad_au_3e86d1  (label: 'Constituir domicilio especial en CABA')
    - Obligacion_la_entidad_debe_constituir_un_domicilio_especial_en_la_ciudad_autonoma_de_buenos_507e1a  (label: 'Constituir domicilio especial en CABA')
[Obligacion] 'contacto inmediato con deudor en caso de atraso' (2 nodos):
    - Obligacion_en_caso_de_atraso_en_los_pagos_el_administrador_debe_mantener_contacto_inmediato_13d6d7  (label: 'Contacto inmediato con deudor en caso de atraso')
    - Obligacion_en_caso_de_atraso_en_los_pagos_el_administrador_debe_mantener_contacto_inmediato_c858d7  (label: 'Contacto inmediato con deudor en caso de atraso')
[Obligacion] 'contactos y notificaciones dentro de treinta dias' (2 nodos):
    - Obligacion_el_administrador_debe_continuar_contactos_con_el_deudor_y_enviar_notificaciones__b7715d  (label: 'Contactos y notificaciones dentro de treinta días')
    - Obligacion_el_administrador_debe_continuar_contactos_con_el_deudor_y_enviar_notificaciones__be81e9  (label: 'Contactos y notificaciones dentro de treinta días')
[Obligacion] 'contar con metodologias para evaluar y gestionar riesgos de mercado' (3 nodos):
    - Obligacion_contar_con_metodologias_que_permitan_evaluar_y_gestionar_activamente_los_riesgos_b12128  (label: 'Contar con metodologías para evaluar y gestionar riesgos de mercado')
    - Obligacion_las_entidades_deben_contar_con_metodologias_que_les_permitan_evaluar_y_gestionar_a585bc  (label: 'Contar con metodologías para evaluar y gestionar riesgos de mercado')
    - Obligacion_las_entidades_deben_contar_con_metodologias_que_les_permitan_evaluar_y_gestionar_a87321  (label: 'Contar con metodologías para evaluar y gestionar riesgos de mercado')
[Obligacion] 'cotejo de resultados con registros contables' (3 nodos):
    - Obligacion_cotejar_los_resultados_del_arqueo_sorpresivo_con_los_registros_contables_y_o_la__8497a1  (label: 'Cotejo de resultados con registros contables')
    - Obligacion_cotejar_los_resultados_del_arqueo_sorpresivo_de_inversiones_con_los_registros_co_f59fa1  (label: 'Cotejo de resultados con registros contables')
    - Obligacion_cotejo_de_los_resultados_del_arqueo_sorpresivo_con_los_registros_contables_y_o_l_76c2ac  (label: 'Cotejo de resultados con registros contables')
[Obligacion] 'debito o transferencia previa para cancelacion de compras' (2 nodos):
    - Obligacion_cuando_se_efectue_cancelacion_de_compras_a_personas_humanas_y_juridicas_en_el_ma_42e609  (label: 'Débito o transferencia previa para cancelación de compras')
    - Obligacion_los_titulares_deberan_debitar_los_fondos_de_las_cuentas_especiales_o_transferirl_00c667  (label: 'Débito o transferencia previa para cancelación de compras')
[Obligacion] 'debito o transferencia previa — cancelacion de compras' (2 nodos):
    - Obligacion_cuando_los_titulares_cancelen_compras_realizadas_a_personas_humanas_y_juridicas__a6dfcf  (label: 'Débito o transferencia previa — cancelación de compras')
    - Obligacion_cuando_los_titulares_efectuen_la_cancelacion_de_compras_realizadas_a_personas_hu_04e675  (label: 'Débito o transferencia previa — cancelación de compras')
[Obligacion] 'declaracion jurada del representante legal' (2 nodos):
    - Obligacion_el_representante_legal_debe_manifestar_mediante_nota_con_caracter_de_declaracion_0f00d0  (label: 'Declaración jurada del representante legal')
    - Obligacion_el_representante_legal_debe_manifestar_mediante_nota_con_caracter_de_declaracion_c8b520  (label: 'Declaración jurada del representante legal')
[Obligacion] 'definir procedimientos y nivel de aprobacion para excepciones' (2 nodos):
    - Obligacion_la_alta_gerencia_debe_definir_los_procedimientos_y_el_nivel_de_aprobacion_que_co_152a1b  (label: 'Definir procedimientos y nivel de aprobación para excepciones')
    - Obligacion_la_alta_gerencia_debe_definir_los_procedimientos_y_el_nivel_de_aprobacion_que_co_5c0bf6  (label: 'Definir procedimientos y nivel de aprobación para excepciones')
[Obligacion] 'devengo de intereses a tasa fijada' (2 nodos):
    - Obligacion_los_intereses_se_devengaran_a_la_tasa_que_se_fije_y_que_sera_transmitida_a_trave_4f7e62  (label: 'Devengo de intereses a tasa fijada')
    - Obligacion_los_intereses_se_devengaran_a_la_tasa_que_se_fije_y_que_sera_transmitida_a_trave_6744d5  (label: 'Devengo de intereses a tasa fijada')
[Obligacion] 'disenar indicadores de alerta temprana' (3 nodos):
    - Obligacion_las_entidades_deben_disenar_un_conjunto_de_indicadores_que_les_permitan_identifi_c779df  (label: 'Diseñar indicadores de alerta temprana')
    - Obligacion_las_entidades_deben_disenar_un_conjunto_de_indicadores_que_les_permitan_identifi_e10e3f  (label: 'Diseñar indicadores de alerta temprana')
    - Obligacion_las_entidades_deben_disenar_un_conjunto_de_indicadores_que_les_permitan_identifi_f7900a  (label: 'Diseñar indicadores de alerta temprana')
[Obligacion] 'disenar indicadores de alertas tempranas' (2 nodos):
    - Obligacion_las_entidades_deben_disenar_un_conjunto_de_indicadores_cualitativos_o_cuantitati_7c62cb  (label: 'Diseñar indicadores de alertas tempranas')
    - Obligacion_las_entidades_deben_disenar_un_conjunto_de_indicadores_que_les_permitan_identifi_02ad79  (label: 'Diseñar indicadores de alertas tempranas')
[Obligacion] 'divulgacion publica regular de informacion' (5 nodos):
    - Obligacion_las_entidades_financieras_deben_dar_a_conocer_al_publico_de_manera_regular_a_tra_0d7501  (label: 'Divulgación pública regular de información')
    - Obligacion_las_entidades_financieras_deben_dar_a_conocer_al_publico_de_manera_regular_a_tra_227e0f  (label: 'Divulgación pública regular de información')
    - Obligacion_las_entidades_financieras_deben_dar_a_conocer_al_publico_de_manera_regular_a_tra_98869e  (label: 'Divulgación pública regular de información')
    - Obligacion_las_entidades_financieras_deben_dar_a_conocer_al_publico_de_manera_regular_a_tra_a4b64f  (label: 'Divulgación pública regular de información')
    - Obligacion_las_entidades_financieras_deben_dar_a_conocer_al_publico_de_manera_regular_a_tra_fb301b  (label: 'Divulgación pública regular de información')
[Obligacion] 'documentacion adecuada del relevamiento del sistema contable' (2 nodos):
    - Obligacion_el_relevamiento_del_sistema_contable_debe_ser_documentado_adecuadamente_el_grado_0c411f  (label: 'Documentación adecuada del relevamiento del sistema contable')
    - Obligacion_el_relevamiento_del_sistema_contable_debera_ser_documentado_adecuadamente__nmcie_3a3a65  (label: 'Documentación adecuada del relevamiento del sistema contable')
[Obligacion] 'documentacion respaldatoria de bases de datos' (2 nodos):
    - Obligacion_desarrollar_documentacion_respaldatoria_de_las_bases_de_datos_incluyendo_las_def_3d8751  (label: 'Documentación respaldatoria de bases de datos')
    - Obligacion_la_entidad_financiera_debe_desarrollar_documentacion_que_respalda_las_bases_de_d_3ce1e3  (label: 'Documentación respaldatoria de bases de datos')
[Obligacion] 'entregar certificados y documentacion de echeq' (2 nodos):
    - Obligacion_deber_de_entregar_los_certificados_para_acciones_civiles_de_echeq_y_demas_docume_ca8497  (label: 'Entregar certificados y documentación de ECHEQ')
    - Obligacion_entregar_los_certificados_para_acciones_civiles_de_echeq_y_demas_documentacion_q_cad142  (label: 'Entregar certificados y documentación de ECHEQ')
[Obligacion] 'entrevistas personales con deudor cuando sea factible' (2 nodos):
    - Obligacion_cuando_sea_factible_o_recomendable_la_comunicacion_con_el_deudor_debe_incluir_en_5b7c5c  (label: 'Entrevistas personales con deudor cuando sea factible')
    - Obligacion_cuando_sea_factible_o_recomendable_la_comunicacion_con_el_deudor_debe_incluir_en_ef8353  (label: 'Entrevistas personales con deudor cuando sea factible')
[Obligacion] 'enviar archivo con registros de control y valor nulo' (2 nodos):
    - Obligacion_la_entidad_depositaria_debe_enviar_un_archivo_solo_con_los_registros_de_control__d67b8f  (label: 'Enviar archivo con registros de control y valor nulo')
    - Obligacion_la_entidad_girada_debe_enviar_un_archivo_solo_con_los_registros_de_control_y_de__4f01a3  (label: 'Enviar archivo con registros de control y valor nulo')
[Obligacion] 'envio cuatrimestral de resumen de cuenta' (3 nodos):
    - Obligacion_envio_al_titular_de_un_resumen_de_cuenta_con_indicacion_del_tipo_de_cuenta_confo_5b1d65  (label: 'Envío cuatrimestral de resumen de cuenta')
    - Obligacion_envio_cuatrimestral_de_resumen_de_cuenta_a_la_direccion_de_correo_electronico_in_1e7759  (label: 'Envío cuatrimestral de resumen de cuenta')
    - Obligacion_las_entidades_deberan_enviar_al_titular_un_resumen_de_cuenta_cuatrimestralmente__1251e2  (label: 'Envío cuatrimestral de resumen de cuenta')
[Obligacion] 'especificar situacion de cuenta en sistema de seguro' (2 nodos):
    - Obligacion_se_especificara_la_situacion_de_la_cuenta_frente_al_sistema_de_seguro_de_garanti_5a69b2  (label: 'Especificar situación de cuenta en sistema de seguro')
    - Obligacion_se_especificara_la_situacion_de_la_cuenta_frente_al_sistema_de_seguro_de_garanti_e7d6e1  (label: 'Especificar situación de cuenta en sistema de seguro')
[Obligacion] 'establecer acuerdos, procedimientos y elementos de seguridad' (2 nodos):
    - Obligacion_establecer_los_acuerdos_procedimientos_y_elementos_de_seguridad_que_impidan_inst_d7f159  (label: 'Establecer acuerdos, procedimientos y elementos de seguridad')
    - Obligacion_establecer_y_o_aplicar_los_acuerdos_procedimientos_y_elementos_de_seguridad_que__ca1675  (label: 'Establecer acuerdos, procedimientos y elementos de seguridad')
[Obligacion] 'estructura organizacional con caracteristicas para implementar estrategia' (2 nodos):
    - Obligacion_la_estructura_organizacional_debe_contar_con_las_caracteristicas_necesarias_para_6f1f75  (label: 'Estructura organizacional con características para implementar estrategia')
    - Obligacion_la_estructura_organizacional_debe_contar_con_las_caracteristicas_necesarias_para_94fd1b  (label: 'Estructura organizacional con características para implementar estrategia')
[Obligacion] 'exposicion en egresos financieros cuando saldo es deudor' (2 nodos):
    - Obligacion_cuando_al_cierre_de_un_periodo_mensual_las_cuentas_de_otros_resultados_integrale_1241eb  (label: 'Exposición en Egresos Financieros cuando saldo es deudor')
    - Obligacion_cuando_el_saldo_de_la_cuenta_sea_deudor_a_fin_de_un_periodo_mensual_se_expondra__36f4d9  (label: 'Exposición en Egresos Financieros cuando saldo es deudor')
[Obligacion] 'garantizar politica incentivos no contradictoria' (2 nodos):
    - Obligacion_el_directorio_debe_garantizar_que_la_politica_de_incentivos_economicos_al_person_0fec6f  (label: 'Garantizar política incentivos no contradictoria')
    - Obligacion_el_directorio_debe_garantizar_que_la_politica_de_incentivos_economicos_al_person_1af24e  (label: 'Garantizar política incentivos no contradictoria')
[Obligacion] 'guardar comunicacion con solicitantes' (2 nodos):
    - Obligacion_el_administrador_debe_guardar_en_la_carpeta_de_administracion_toda_comunicacion__e43d7f  (label: 'Guardar comunicación con solicitantes')
    - Obligacion_guardar_en_la_carpeta_de_administracion_toda_comunicacion_enviada_a_los_solicita_9e81ec  (label: 'Guardar comunicación con solicitantes')
[Obligacion] 'guardar documentacion cancelatoria' (2 nodos):
    - Obligacion_el_administrador_debe_guardar_en_la_carpeta_de_administracion_documentacion_canc_1c5a06  (label: 'Guardar documentación cancelatoria')
    - Obligacion_guardar_en_la_carpeta_de_administracion_documentacion_cancelatoria_del_prestamo__de87ef  (label: 'Guardar documentación cancelatoria')
[Obligacion] 'guardar documentacion de mora, ejecucion y remate' (2 nodos):
    - Obligacion_el_administrador_debe_guardar_en_la_carpeta_de_administracion_documentacion_rela_27c07a  (label: 'Guardar documentación de mora, ejecución y remate')
    - Obligacion_guardar_en_la_carpeta_de_administracion_documentacion_relacionada_con_la_mora_ej_bf50d7  (label: 'Guardar documentación de mora, ejecución y remate')
[Obligacion] 'guardar documentacion posterior al desembolso' (2 nodos):
    - Obligacion_el_administrador_debe_guardar_en_la_carpeta_de_administracion_toda_documentacion_8f1a50  (label: 'Guardar documentación posterior al desembolso')
    - Obligacion_guardar_en_la_carpeta_de_administracion_toda_documentacion_relacionada_con_el_pr_34670d  (label: 'Guardar documentación posterior al desembolso')
[Obligacion] 'guardar otros elementos relevantes' (2 nodos):
    - Obligacion_el_administrador_debe_guardar_en_la_carpeta_de_administracion_todo_otro_elemento_5af4a5  (label: 'Guardar otros elementos relevantes')
    - Obligacion_guardar_en_la_carpeta_de_administracion_todo_otro_elemento_incluyendo_el_registr_bc15dd  (label: 'Guardar otros elementos relevantes')
[Obligacion] 'identificacion de documentos de representada' (2 nodos):
    - Obligacion_la_entidad_representante_debe_identificar_en_el_proceso_de_intercambio_los_docum_3eb832  (label: 'Identificación de documentos de representada')
    - Obligacion_la_entidad_representante_debe_identificar_en_el_proceso_de_intercambio_los_docum_5b9194  (label: 'Identificación de documentos de representada')
[Obligacion] 'identificacion de partidas segun moneda de origen' (2 nodos):
    - Obligacion_las_restantes_partidas_se_identificaran_segun_su_moneda_de_origen_de_acuerdo_con_970406  (label: 'Identificación de partidas según moneda de origen')
    - Obligacion_todas_las_partidas_se_identificaran_segun_su_moneda_de_origen_de_acuerdo_con_la__eab5e5  (label: 'Identificación de partidas según moneda de origen')
[Obligacion] 'identificacion de personal responsable de implementacion' (2 nodos):
    - Obligacion_el_plan_debe_contemplar_la_identificacion_del_personal_responsable_de_la_impleme_adbaf2  (label: 'Identificación de personal responsable de implementación')
    - Obligacion_el_plan_debe_contemplar_la_identificacion_del_personal_responsable_de_la_impleme_f0e7e3  (label: 'Identificación de personal responsable de implementación')
[Obligacion] 'identificar informacion del cheque originalmente presentado' (2 nodos):
    - Obligacion_en_cualquier_caso_las_entidades_deben_identificar_en_el_archivo_a_transmitir_la__871bfa  (label: 'Identificar información del cheque originalmente presentado')
    - Obligacion_en_cualquier_caso_las_entidades_deberan_identificar_en_el_archivo_a_transmitir_l_d9f715  (label: 'Identificar información del cheque originalmente presentado')
[Obligacion] 'implementar mecanismos de seguridad informatica' (4 nodos):
    - Obligacion_las_entidades_deberan_tener_implementados_mecanismos_de_seguridad_informatica_qu_12bcd0  (label: 'Implementar mecanismos de seguridad informática')
    - Obligacion_las_entidades_deberan_tener_implementados_mecanismos_de_seguridad_informatica_qu_474525  (label: 'Implementar mecanismos de seguridad informática')
    - Obligacion_las_entidades_deberan_tener_implementados_mecanismos_de_seguridad_informatica_qu_9c8689  (label: 'Implementar mecanismos de seguridad informática')
    - Obligacion_las_entidades_deberan_tener_implementados_mecanismos_de_seguridad_informatica_qu_d12d0a  (label: 'Implementar mecanismos de seguridad informática')
[Obligacion] 'incluir campos en registros de cuotas' (2 nodos):
    - Obligacion_para_cada_registro_de_cuota_se_deberan_incluir_los_campos_especificados_numero_d_183ac1  (label: 'Incluir campos en registros de cuotas')
    - Obligacion_para_cada_registro_de_cuota_se_deberan_incluir_los_campos_especificados_numero_d_b2c00c  (label: 'Incluir campos en registros de cuotas')
[Obligacion] 'incorporar leyendas segun normas de seguro de depositos' (2 nodos):
    - Obligacion_la_incorporacion_de_las_leyendas_que_correspondan_se_formulara_con_ajuste_a_lo_e_5ac12c  (label: 'Incorporar leyendas según normas de seguro de depósitos')
    - Obligacion_la_incorporacion_de_las_leyendas_que_correspondan_se_formulara_con_ajuste_a_lo_e_ee17fc  (label: 'Incorporar leyendas según normas de seguro de depósitos')
[Obligacion] 'independencia segun normas de auditoria' (2 nodos):
    - Obligacion_el_auditor_externo_debe_tener_la_independencia_requerida_por_las_normas_de_audit_f3f087  (label: 'Independencia según Normas de Auditoría')
    - Obligacion_el_socio_responsable_debe_tener_la_independencia_requerida_por_las_normas_de_aud_e941f9  (label: 'Independencia según Normas de Auditoría')
[Obligacion] 'indicacion expresa de ausencia de objetivos no cumplidos' (2 nodos):
    - Obligacion_si_no_existieran_objetivos_no_cumplidos_se_lo_debera_indicar_expresamente__nmcie_70c95c  (label: 'Indicación expresa de ausencia de objetivos no cumplidos')
    - Obligacion_si_no_existieran_objetivos_no_cumplidos_se_lo_debera_indicar_expresamente__ri_cc_a5616b  (label: 'Indicación expresa de ausencia de objetivos no cumplidos')
[Obligacion] 'informacion de transferencias en resumen' (2 nodos):
    - Obligacion_las_entidades_deberan_incluir_en_el_resumen_de_cuenta_la_informacion_prevista_en_1a3378  (label: 'Información de transferencias en resumen')
    - Obligacion_las_entidades_deberan_incluir_en_el_resumen_de_cuenta_la_informacion_prevista_en_88ae1f  (label: 'Información de transferencias en resumen')
[Obligacion] 'informar a arca debitos y creditos' (2 nodos):
    - Obligacion_las_entidades_financieras_deberan_informar_a_la_arca_los_debitos_y_creditos_que__2f8bd5  (label: 'Informar a ARCA débitos y créditos')
    - Obligacion_las_entidades_financieras_deberan_informar_a_la_arca_los_debitos_y_creditos_que__5eb2df  (label: 'Informar a ARCA débitos y créditos')
[Obligacion] 'informar caracteres alfabeticos en mayusculas' (10 nodos):
    - Obligacion_los_caracteres_alfabeticos_de_los_campos_alfanumericos_deben_ser_siempre_informa_9faf13  (label: 'Informar caracteres alfabéticos en mayúsculas')
    - Obligacion_los_caracteres_alfabeticos_de_los_campos_alfanumericos_deben_ser_siempre_informa_ca9260  (label: 'Informar caracteres alfabéticos en mayúsculas')
    - Obligacion_los_caracteres_alfabeticos_de_los_campos_alfanumericos_deberan_ser_siempre_infor_2f83c6  (label: 'Informar caracteres alfabéticos en mayúsculas')
    - Obligacion_los_caracteres_alfabeticos_de_los_campos_alfanumericos_deberan_ser_siempre_infor_543558  (label: 'Informar caracteres alfabéticos en mayúsculas')
    - Obligacion_los_caracteres_alfabeticos_de_los_campos_alfanumericos_deberan_ser_siempre_infor_80dace  (label: 'Informar caracteres alfabéticos en mayúsculas')
    - Obligacion_los_caracteres_alfabeticos_de_los_campos_alfanumericos_deberan_ser_siempre_infor_cc1936  (label: 'Informar caracteres alfabéticos en mayúsculas')
    - Obligacion_los_caracteres_alfabeticos_deben_ser_siempre_informados_en_mayusculas__snp_cheq__23cd47  (label: 'Informar caracteres alfabéticos en mayúsculas')
    - Obligacion_los_caracteres_alfabeticos_deben_ser_siempre_informados_en_mayusculas__snp_cheq__a30473  (label: 'Informar caracteres alfabéticos en mayúsculas')
    - Obligacion_los_caracteres_alfabeticos_en_todos_los_campos_deberan_ser_informados_siempre_en_19d627  (label: 'Informar caracteres alfabéticos en mayúsculas')
    - Obligacion_todos_los_caracteres_alfabeticos_deben_ser_informados_en_mayusculas__snp_cheq_7__0b0998  (label: 'Informar caracteres alfabéticos en mayúsculas')
[Obligacion] 'informar cumplimiento elementos caja tesoro movil' (2 nodos):
    - Obligacion_deber_de_informar_el_cumplimiento_de_los_elementos_de_seguridad_establecidos_par_15550d  (label: 'Informar cumplimiento elementos Caja Tesoro Móvil')
    - Obligacion_deber_de_informar_el_cumplimiento_de_los_elementos_de_seguridad_establecidos_par_801354  (label: 'Informar cumplimiento elementos caja tesoro móvil')
[Obligacion] 'informar cumplimiento pulsador de alarma' (2 nodos):
    - Obligacion_informar_el_cumplimiento_de_la_medida_de_pulsador_de_alarma_segun_los_parametros_07c799  (label: 'Informar cumplimiento pulsador de alarma')
    - Obligacion_informar_el_cumplimiento_de_la_medida_minima_de_seguridad_consistente_en_pulsado_fe96f9  (label: 'Informar cumplimiento pulsador de alarma')
[Obligacion] 'informar debitos y creditos a arca' (2 nodos):
    - Obligacion_las_entidades_financieras_deberan_informar_a_la_arca_conforme_al_procedimiento_y_4cebd0  (label: 'Informar débitos y créditos a ARCA')
    - Obligacion_las_entidades_financieras_deberan_informar_a_la_arca_los_debitos_y_creditos_que__bca530  (label: 'Informar débitos y créditos a ARCA')
[Obligacion] 'informar numero de serie caja tesoro movil' (2 nodos):
    - Obligacion_las_entidades_financieras_deberan_proveer_informacion_del_numero_de_serie_de_la__35a81a  (label: 'Informar número de serie caja tesoro móvil')
    - Obligacion_las_entidades_financieras_deberan_proveer_informacion_respecto_de_los_tipos_de_u_0b4779  (label: 'Informar número de serie caja tesoro móvil')
[Obligacion] 'informatizacion de bases de datos' (2 nodos):
    - Obligacion_la_entidad_financiera_debe_llevar_la_informacion_de_manera_informatizada_dado_lo_4f056f  (label: 'Informatización de bases de datos')
    - Obligacion_la_entidad_financiera_debe_llevar_la_informacion_de_manera_informatizada_dado_lo_ae8c4e  (label: 'Informatización de bases de datos')
[Obligacion] 'ingresos demostrables, habituales y permanentes' (2 nodos):
    - Obligacion_los_ingresos_de_los_solicitantes_deberan_ser_demostrables_habituales_y_permanent_088f64  (label: 'Ingresos demostrables, habituales y permanentes')
    - Obligacion_los_ingresos_de_los_solicitantes_deberan_ser_demostrables_habituales_y_permanent_602660  (label: 'Ingresos demostrables, habituales y permanentes')
[Obligacion] 'legalizacion de firmas de profesionales' (2 nodos):
    - Obligacion_las_firmas_de_los_profesionales_cuya_intervencion_se_requiere_deberan_estar_lega_9f95d4  (label: 'Legalización de firmas de profesionales')
    - Obligacion_las_firmas_de_los_profesionales_cuya_intervencion_se_requiere_en_las_disposicion_4390e0  (label: 'Legalización de firmas de profesionales')
[Obligacion] 'llenar campos alfanumericos con blancos a derecha' (2 nodos):
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_de_los_requeridos_para_la_info_300d10  (label: 'Llenar campos alfanuméricos con blancos a derecha')
    - Obligacion_los_campos_alfanumericos_deben_llenarse_con_blancos_a_derecha_para_completar_la__b186bc  (label: 'Llenar campos alfanuméricos con blancos a derecha')
[Obligacion] 'llenar campos alfanumericos con blancos a la derecha' (2 nodos):
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_de_los_requeridos_para_la_info_684274  (label: 'Llenar campos alfanuméricos con blancos a la derecha')
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_de_los_requeridos_para_la_info_f5e5fc  (label: 'Llenar campos alfanuméricos con blancos a la derecha')
[Obligacion] 'llenar campos numericos con ceros a izquierda' (2 nodos):
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_de_los_requeridos_para_la_informac_f114b2  (label: 'Llenar campos numéricos con ceros a izquierda')
    - Obligacion_los_campos_numericos_que_posean_mas_caracteres_de_los_requeridos_deben_llenarse__b5a233  (label: 'Llenar campos numéricos con ceros a izquierda')
[Obligacion] 'llenar campos numericos con ceros a la izquierda' (2 nodos):
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_de_los_requeridos_para_la_informac_2d5d1b  (label: 'Llenar campos numéricos con ceros a la izquierda')
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_de_los_requeridos_para_la_informac_bc5f0b  (label: 'Llenar campos numéricos con ceros a la izquierda')
[Obligacion] 'llevar registros de procedimientos' (2 nodos):
    - Obligacion_actividad_recomendada_al_administrador_llevar_registros_de_los_distintos_procedi_0814f2  (label: 'Llevar registros de procedimientos')
    - Obligacion_recomendacion_al_administrador_de_llevar_registros_de_los_distintos_procedimient_18a888  (label: 'Llevar registros de procedimientos')
[Obligacion] 'mantener consistencia en adopcion de bandas o puntos medios' (2 nodos):
    - Obligacion_deber_de_mantener_consistencia_en_la_adopcion_de_bandas_temporales_o_sus_puntos__a70b1a  (label: 'Mantener consistencia en adopción de bandas o puntos medios')
    - Obligacion_las_entidades_deben_mantener_la_adopcion_de_bandas_temporales_o_sus_puntos_medio_d2857a  (label: 'Mantener consistencia en adopción de bandas o puntos medios')
[Obligacion] 'mantener correlaciones con cuentas de balance' (2 nodos):
    - Obligacion_las_partidas_informadas_deberan_mantener_las_correlaciones_con_cuentas_de_balanc_17494b  (label: 'Mantener correlaciones con cuentas de balance')
    - Obligacion_las_partidas_previstas_en_el_punto_10_1_2_mantendran_las_correlaciones_con_cuent_600b1e  (label: 'Mantener correlaciones con cuentas de balance')
[Obligacion] 'mantener documentacion actualizada' (2 nodos):
    - Obligacion_la_documentacion_de_los_controles_debera_mantenerse_actualizada__ri_ccna_d2a1p2__8b9dca  (label: 'Mantener documentación actualizada')
    - Obligacion_las_entidades_deberan_mantener_la_documentacion_de_controles_actualizada__nmcief_6155cf  (label: 'Mantener documentación actualizada')
[Obligacion] 'mecanismos de seguridad informatica' (2 nodos):
    - Obligacion_implementar_mecanismos_de_seguridad_informatica_que_garanticen_la_genuinidad_de__30fbdc  (label: 'Mecanismos de seguridad informática')
    - Obligacion_implementar_mecanismos_de_seguridad_informatica_que_garanticen_la_genuinidad_de__42d628  (label: 'Mecanismos de seguridad informática')
[Obligacion] 'mejores esfuerzos para cobro a vencimiento' (2 nodos):
    - Obligacion_el_administrador_debe_emplear_sus_mejores_esfuerzos_para_cobrar_los_pagos_period_3a6f44  (label: 'Mejores esfuerzos para cobro a vencimiento')
    - Obligacion_el_administrador_debe_emplear_sus_mejores_esfuerzos_para_cobrar_los_pagos_period_3e322c  (label: 'Mejores esfuerzos para cobro a vencimiento')
[Obligacion] 'notificacion de recomendaciones para cajeros automaticos' (3 nodos):
    - Obligacion_en_el_momento_de_la_apertura_de_una_cuenta_que_implique_la_entrega_de_tarjetas_p_6399ed  (label: 'Notificación de recomendaciones para cajeros automáticos')
    - Obligacion_en_el_momento_de_la_apertura_de_una_cuenta_que_implique_la_entrega_de_tarjetas_p_9f4cb4  (label: 'Notificación de recomendaciones para cajeros automáticos')
    - Obligacion_notificar_al_titular_acerca_de_las_recomendaciones_y_precauciones_que_deben_toma_775381  (label: 'Notificación de recomendaciones para cajeros automáticos')
[Obligacion] 'obligacion solidaria de codeudores' (2 nodos):
    - Obligacion_los_codeudores_deberan_asumir_su_obligacion_solidariamente__manori_3_1_2_2_e541e7  (label: 'Obligación solidaria de codeudores')
    - Obligacion_los_codeudores_deberan_asumir_su_obligacion_solidariamente_y_constituirse_en_dad_7f790f  (label: 'Obligación solidaria de codeudores')
[Obligacion] 'obtener conformidad expresa para debitos' (2 nodos):
    - Obligacion_como_requisito_previo_a_la_apertura_de_una_cuenta_debera_obtenerse_la_conformida_91f75e  (label: 'Obtener conformidad expresa para débitos')
    - Obligacion_requisito_previo_a_la_apertura_de_una_cuenta_obtener_la_conformidad_expresa_de_l_83cd6d  (label: 'Obtener conformidad expresa para débitos')
[Obligacion] 'operacion conforme a estandares y formatos' (2 nodos):
    - Obligacion_las_entidades_deben_operar_conforme_a_los_estandares_y_formatos_definidos_en_las_44113e  (label: 'Operación conforme a estándares y formatos')
    - Obligacion_las_entidades_participantes_deben_operar_conforme_a_los_estandares_y_formatos_de_1f9aee  (label: 'Operación conforme a estándares y formatos')
[Obligacion] 'politicas y procedimientos claros para decisiones de alta gerencia' (2 nodos):
    - Obligacion_el_plan_de_contingencia_debe_contener_politicas_y_procedimientos_claros_que_perm_050e74  (label: 'Políticas y procedimientos claros para decisiones de Alta Gerencia')
    - Obligacion_el_plan_de_fondeo_para_contingencias_debe_contener_politicas_y_procedimientos_cl_04529e  (label: 'Políticas y procedimientos claros para decisiones de Alta Gerencia')
[Obligacion] 'poner a disposicion servicio de consulta de cuentas activas' (2 nodos):
    - Obligacion_cada_esquema_de_pago_debera_poner_a_disposicion_de_sus_participantes_un_servicio_39aa84  (label: 'Poner a disposición servicio de consulta de cuentas activas')
    - Obligacion_el_administrador_de_un_esquema_de_transferencias_inmediatas_debe_poner_a_disposi_fd9949  (label: 'Poner a disposición servicio de consulta de cuentas activas')
[Obligacion] 'preparar entidad para escenarios severos de estres' (2 nodos):
    - Obligacion_las_entidades_deben_preparar_a_la_entidad_para_manejar_un_rango_de_escenarios_se_b288a2  (label: 'Preparar entidad para escenarios severos de estrés')
    - Obligacion_las_entidades_financieras_deben_preparar_a_la_entidad_para_manejar_un_rango_de_e_80ea50  (label: 'Preparar entidad para escenarios severos de estrés')
[Obligacion] 'presentacion de solicitud de autorizacion' (3 nodos):
    - Obligacion_la_solicitud_de_autorizacion_debera_ser_interpuesta_a_traves_del_correspondiente_1477c1  (label: 'Presentación de solicitud de autorización')
    - Obligacion_la_solicitud_de_autorizacion_debera_ser_interpuesta_mediante_nota_acompanada_de__adfcaa  (label: 'Presentación de solicitud de autorización')
    - Obligacion_las_entidades_que_se_fusionan_para_constituir_una_nueva_entidad_o_la_entidad_abs_ec1299  (label: 'Presentación de solicitud de autorización')
[Obligacion] 'procesos de aprobacion y valuacion de nuevos productos con metodologias documentadas' (2 nodos):
    - Obligacion_los_procesos_de_aprobacion_y_valuacion_de_los_nuevos_productos_se_deben_apoyar_e_0a4af0  (label: 'Procesos de aprobación y valuación de nuevos productos con metodologías documentadas')
    - Obligacion_los_procesos_de_aprobacion_y_valuacion_de_nuevos_productos_deben_apoyarse_en_met_2a851c  (label: 'Procesos de aprobación y valuación de nuevos productos con metodologías documentadas')
[Obligacion] 'pruebas de controles para determinar diseno y funcionamiento' (2 nodos):
    - Obligacion_el_auditor_interno_debera_completar_pruebas_para_determinar_si_los_controles_est_c6d9fb  (label: 'Pruebas de controles para determinar diseño y funcionamiento')
    - Obligacion_una_vez_identificadas_y_documentadas_las_actividades_de_control_la_auditoria_int_c32a52  (label: 'Pruebas de controles para determinar diseño y funcionamiento')
[Obligacion] 'recaudos operativos para estandares de performance y disponibilidad' (2 nodos):
    - Obligacion_el_aceptador_dentro_de_un_esquema_de_transferencias_inmediatas_debe_tomar_los_re_bf0c3c  (label: 'Recaudos operativos para estándares de performance y disponibilidad')
    - Obligacion_tomar_los_recaudos_operativos_necesarios_para_alcanzar_los_estandares_requeridos_f61a70  (label: 'Recaudos operativos para estándares de performance y disponibilidad')
[Obligacion] 'redondeo de magnitudes segun regla de digito' (2 nodos):
    - Obligacion_se_incrementaran_los_valores_en_una_unidad_cuando_el_primer_digito_de_las_fracci_5b1063  (label: 'Redondeo de magnitudes según regla de dígito')
    - Obligacion_se_incrementaran_los_valores_en_una_unidad_cuando_el_primer_digito_de_las_fracci_f2bdf6  (label: 'Redondeo de magnitudes según regla de dígito')
[Obligacion] 'reintegro de remanente al deudor' (2 nodos):
    - Obligacion_en_caso_de_existir_remanente_del_producido_de_la_ejecucion_debera_ser_reintegrad_3509d0  (label: 'Reintegro de remanente al deudor')
    - Obligacion_obligacion_de_reintegrar_al_deudor_el_remanente_del_producido_de_la_ejecucion_en_972fa5  (label: 'Reintegro de remanente al deudor')
[Obligacion] 'relacion de respuestas con registros contables' (2 nodos):
    - Obligacion_relacion_de_las_respuestas_recibidas_de_confirmaciones_directas_con_los_registro_cf8a5c  (label: 'Relación de respuestas con registros contables')
    - Obligacion_relacion_de_las_respuestas_recibidas_de_terceros_depositarios_con_los_registros__12206f  (label: 'Relación de respuestas con registros contables')
[Obligacion] 'relevamiento y comprension del sistema contable' (2 nodos):
    - Obligacion_es_necesario_relevar_y_entender_el_sistema_contable_como_parte_del_analisis_de_l_bcb4e6  (label: 'Relevamiento y comprensión del sistema contable')
    - Obligacion_necesidad_de_relevar_y_entender_el_sistema_contable_como_parte_del_analisis_de_l_c49ff3  (label: 'Relevamiento y comprensión del sistema contable')
[Obligacion] 'requerir informe comercial o crediticio' (2 nodos):
    - Obligacion_la_entidad_financiera_debe_requerir_un_informe_comercial_o_crediticio_de_reconoc_bb2b71  (label: 'Requerir informe comercial o crediticio')
    - Obligacion_la_entidad_financiera_debe_requerir_un_informe_comercial_o_crediticio_para_cada__8e1638  (label: 'Requerir informe comercial o crediticio')
[Obligacion] 'respuesta de aceptacion tras validaciones' (2 nodos):
    - Obligacion_la_cec_debe_enviar_una_respuesta_de_aceptacion_cuando_los_archivos_superan_todas_9ea759  (label: 'Respuesta de aceptación tras validaciones')
    - Obligacion_si_los_archivos_superan_todas_las_validaciones_la_cec_debe_enviar_una_respuesta__dc1dcb  (label: 'Respuesta de aceptación tras validaciones')
[Obligacion] 'reversion de debitos en cuentas de clientes' (2 nodos):
    - Obligacion_la_entidad_girada_debe_revertir_los_debitos_oportunamente_efectuados_en_las_cuen_35c2aa  (label: 'Reversión de débitos en cuentas de clientes')
    - Obligacion_la_entidad_girada_debe_revertir_los_debitos_oportunamente_efectuados_en_las_cuen_77f805  (label: 'Reversión de débitos en cuentas de clientes')
[Obligacion] 'seguimiento frecuente de tendencias de mercado' (2 nodos):
    - Obligacion_la_alta_gerencia_debe_seguir_en_forma_frecuente_las_tendencias_del_mercado_que_p_582b6f  (label: 'Seguimiento frecuente de tendencias de mercado')
    - Obligacion_la_alta_gerencia_debe_seguir_en_forma_frecuente_las_tendencias_del_mercado_que_p_df9a81  (label: 'Seguimiento frecuente de tendencias de mercado')
[Obligacion] 'seguimiento y regularizacion de mora' (2 nodos):
    - Obligacion_el_administrador_debe_efectuar_el_seguimiento_y_regularizacion_de_la_mora_de_acu_d5db50  (label: 'Seguimiento y regularización de mora')
    - Obligacion_el_administrador_debe_realizar_el_seguimiento_y_regularizacion_de_la_mora_en_los_5c0104  (label: 'Seguimiento y regularización de mora')
[Obligacion] 'sistema de gestion incluir metodologias var y pruebas de estres' (2 nodos):
    - Obligacion_el_sistema_de_gestion_del_riesgo_de_mercado_debe_incluir_la_utilizacion_de_metod_92eee1  (label: 'Sistema de gestión incluir metodologías VaR y pruebas de estrés')
    - Obligacion_el_sistema_de_gestion_del_riesgo_de_mercado_debe_incluir_la_utilizacion_de_metod_c78c20  (label: 'Sistema de gestión incluir metodologías VaR y pruebas de estrés')
[Obligacion] 'tenencia de certificado de aptitud' (3 nodos):
    - Obligacion_cumplimiento_de_la_medida_de_tenencia_de_certificado_de_aptitud_en_cajas_de_aten_33fb0a  (label: 'Tenencia de certificado de aptitud')
    - Obligacion_informar_sobre_la_tenencia_de_certificado_de_aptitud_como_medida_minima_de_segur_cfde6f  (label: 'Tenencia de certificado de aptitud')
    - Obligacion_se_informara_el_cumplimiento_de_la_tenencia_de_certificado_de_aptitud_en_recinto_188761  (label: 'Tenencia de certificado de aptitud')
[Obligacion] 'toma de medidas correctivas rapida' (2 nodos):
    - Obligacion_el_sistema_de_control_de_calidad_debe_prever_la_toma_de_medidas_correctivas_en_f_a65506  (label: 'Toma de medidas correctivas rápida')
    - Obligacion_el_sistema_de_control_de_calidad_debe_prever_la_toma_de_medidas_correctivas_en_f_f2839d  (label: 'Toma de medidas correctivas rápida')
[Obligacion] 'transmision por motivos de rechazo especificos' (2 nodos):
    - Obligacion_la_entidad_depositaria_debe_transmitir_por_los_motivos_de_rechazo_de_cheques_y_o_99eac4  (label: 'Transmisión por motivos de rechazo específicos')
    - Obligacion_la_entidad_girada_debe_transmitir_por_los_motivos_de_rechazo_de_cheques_y_o_tran_b1011b  (label: 'Transmisión por motivos de rechazo específicos')
[Operacion] 'acreditacion de importes netos en pesos' (2 nodos):
    - Operacion_acreditacion_de_importes_netos_en_pesos__depaho_3_13_3_6_9993ab  (label: 'Acreditación de importes netos en pesos')
    - Operacion_acreditacion_de_importes_netos_en_pesos__depaho_3_13_3_8_823572  (label: 'Acreditación de importes netos en pesos')
[Operacion] 'acreditacion de importes netos en pesos — actividad agricola' (3 nodos):
    - Operacion_acreditacion_de_importes_netos_en_pesos_actividad_agricola__depaho_3_12_3_2_942095  (label: 'Acreditación de importes netos en pesos — actividad agrícola')
    - Operacion_acreditacion_de_importes_netos_en_pesos_actividad_agricola__depaho_3_12_3_3_2a1fb9  (label: 'Acreditación de importes netos en pesos — actividad agrícola')
    - Operacion_acreditacion_de_importes_netos_en_pesos_actividad_agricola__depaho_3_12_3_8_9f4e13  (label: 'Acreditación de importes netos en pesos — actividad agrícola')
[Operacion] 'acreditacion diaria de retribucion' (2 nodos):
    - Operacion_acreditacion_diaria_de_retribucion__depaho_3_12_4_c94f92  (label: 'Acreditación diaria de retribución')
    - Operacion_acreditacion_diaria_de_retribucion__depaho_3_13_5_6403b9  (label: 'Acreditación diaria de retribución')
[Operacion] 'acunacion moneda plata 925 $ 25' (2 nodos):
    - Operacion_acunacion_moneda_plata_925_25__cirmo3_7_39_d0fec1  (label: 'Acuñación moneda Plata 925 $ 25')
    - Operacion_acunacion_moneda_plata_925_25__cirmo3_7_45_3546e0  (label: 'Acuñación moneda Plata 925 $ 25')
[Operacion] 'administracion del sca' (2 nodos):
    - Operacion_administracion_del_sca__snp_cheq_3_5_2_3_40059d  (label: 'Administración del SCA')
    - Operacion_administracion_del_sca__snp_cheq_3_5_2_4_5aedee  (label: 'Administración del SCA')
[Operacion] 'administracion del sce' (2 nodos):
    - Operacion_administracion_del_sce__snp_cheq_3_6_2_2_54aa5d  (label: 'Administración del SCE')
    - Operacion_administracion_del_sce__snp_cheq_3_6_7_1_92c039  (label: 'Administración del SCE')
[Operacion] 'agregacion de datos sobre riesgos' (2 nodos):
    - Operacion_agregacion_de_datos_sobre_riesgos__adrei_2_1_2_1_e9f3c4  (label: 'Agregación de datos sobre riesgos')
    - Operacion_agregacion_de_datos_sobre_riesgos__adrei_2_1_42799c  (label: 'Agregación de datos sobre riesgos')
[Operacion] 'alquiler de cajas de seguridad' (2 nodos):
    - Operacion_alquiler_de_cajas_de_seguridad__depaho_1_10_1_5ba775  (label: 'Alquiler de cajas de seguridad')
    - Operacion_alquiler_de_cajas_de_seguridad__depaho_3_4_8_1_be918e  (label: 'Alquiler de cajas de seguridad')
[Operacion] 'apertura de cuenta a nombre del beneficiario' (2 nodos):
    - Operacion_apertura_de_cuenta_a_nombre_del_beneficiario__depaho_2_2_2_2_63c424  (label: 'Apertura de cuenta a nombre del beneficiario')
    - Operacion_apertura_de_cuenta_a_nombre_del_beneficiario__depaho_2_2_2_3_a452ff  (label: 'Apertura de cuenta a nombre del beneficiario')
[Operacion] 'apertura de cuenta especial de inversion' (2 nodos):
    - Operacion_apertura_de_cuenta_especial_de_inversion__depaho_3_8_1_254782  (label: 'Apertura de Cuenta especial de inversión')
    - Operacion_apertura_de_cuenta_especial_de_inversion__depaho_3_8_5_96f9f9  (label: 'Apertura de cuenta especial de inversión')
[Operacion] 'apertura de cuenta especial repatriacion' (2 nodos):
    - Operacion_apertura_de_cuenta_especial_repatriacion__depaho_4_20_1_15c194  (label: 'Apertura de cuenta especial repatriación')
    - Operacion_apertura_de_cuenta_especial_repatriacion__depaho_4_21_1_bc3d84  (label: 'Apertura de cuenta especial repatriación')
[Operacion] 'apertura de cuentas especiales de depositos' (2 nodos):
    - Operacion_apertura_de_cuentas_especiales_de_depositos__depaho_3_17_fff088  (label: 'Apertura de cuentas especiales de depósitos')
    - Operacion_apertura_de_cuentas_especiales_de_depositos__depaho_3_1_1_60584b  (label: 'Apertura de cuentas especiales de depósitos')
[Operacion] 'apertura de oficinas de representacion en el exterior' (2 nodos):
    - Operacion_apertura_de_oficinas_de_representacion_en_el_exterior__expaef_5_1_436925  (label: 'Apertura de oficinas de representación en el exterior')
    - Operacion_apertura_de_oficinas_de_representacion_en_el_exterior__expaef_5_3_30f961  (label: 'Apertura de oficinas de representación en el exterior')
[Operacion] 'aplicacion de disposiciones de depositos en caja de ahorros' (2 nodos):
    - Operacion_aplicacion_de_disposiciones_de_depositos_en_caja_de_ahorros__depaho_3_10_9_94a276  (label: 'Aplicación de disposiciones de depósitos en caja de ahorros')
    - Operacion_aplicacion_de_disposiciones_de_depositos_en_caja_de_ahorros__depaho_3_12_5_6b47fa  (label: 'Aplicación de disposiciones de depósitos en caja de ahorros')
[Operacion] 'captacion de depositos en otras monedas' (3 nodos):
    - Operacion_captacion_de_depositos_en_otras_monedas__depaho_3_4_4_5_7208e2  (label: 'Captación de depósitos en otras monedas')
    - Operacion_captacion_de_depositos_en_otras_monedas__depaho_3_6_2_4_652f57  (label: 'Captación de depósitos en otras monedas')
    - Operacion_captacion_de_depositos_en_otras_monedas__depaho_3_8_6_4_27ec78  (label: 'Captación de depósitos en otras monedas')
[Operacion] 'cierre de cuenta por decision de la entidad' (3 nodos):
    - Operacion_cierre_de_cuenta_por_decision_de_la_entidad__depaho_1_13_2_631e7f  (label: 'Cierre de cuenta por decisión de la entidad')
    - Operacion_cierre_de_cuenta_por_decision_de_la_entidad__depaho_3_11_10_2_4f6042  (label: 'Cierre de cuenta por decisión de la entidad')
    - Operacion_cierre_de_cuenta_por_decision_de_la_entidad__depaho_3_8_13_2_33b582  (label: 'Cierre de cuenta por decisión de la entidad')
[Operacion] 'cierre de cuenta por decision del titular' (3 nodos):
    - Operacion_cierre_de_cuenta_por_decision_del_titular__depaho_1_13_1_0aad96  (label: 'Cierre de cuenta por decisión del titular')
    - Operacion_cierre_de_cuenta_por_decision_del_titular__depaho_3_11_10_1_fb8bc9  (label: 'Cierre de cuenta por decisión del titular')
    - Operacion_cierre_de_cuenta_por_decision_del_titular__depaho_3_8_13_1_2d381e  (label: 'Cierre de cuenta por decisión del titular')
[Operacion] 'cierre de sucursales' (2 nodos):
    - Operacion_cierre_de_sucursales__expaef_11_1_835183  (label: 'Cierre de sucursales')
    - Operacion_cierre_de_sucursales__expaef_1_7_5067df  (label: 'Cierre de sucursales')
[Operacion] 'compensacion electronica de cheques' (3 nodos):
    - Operacion_compensacion_electronica_de_cheques__snp_cheq_2_1_8ce45e  (label: 'Compensación electrónica de cheques')
    - Operacion_compensacion_electronica_de_cheques__snp_cheq_2_4_f1ef8a  (label: 'Compensación electrónica de cheques')
    - Operacion_compensacion_electronica_de_cheques__snp_cheq_s2_3e8a3a  (label: 'Compensación electrónica de cheques')
[Operacion] 'compensacion en la cec' (2 nodos):
    - Operacion_compensacion_en_la_cec__snp_cheq_3_1_2_2_612641  (label: 'Compensación en la CEC')
    - Operacion_compensacion_en_la_cec__snp_cheq_3_6_4_1_3_aaef05  (label: 'Compensación en la CEC')
[Operacion] 'compras y retiros de efectivo con tarjeta de debito' (2 nodos):
    - Operacion_compras_y_retiros_de_efectivo_con_tarjeta_de_debito__depaho_2_3_2_3_57a8e9  (label: 'Compras y retiros de efectivo con tarjeta de débito')
    - Operacion_compras_y_retiros_de_efectivo_con_tarjeta_de_debito__depaho_3_10_4_2_6b644e  (label: 'Compras y retiros de efectivo con tarjeta de débito')
[Operacion] 'contratacion de seguro sobre saldo deudor' (2 nodos):
    - Operacion_contratacion_de_seguro_sobre_saldo_deudor__manori_1_1_10_1_aa02a1  (label: 'Contratación de seguro sobre saldo deudor')
    - Operacion_contratacion_de_seguro_sobre_saldo_deudor__manori_3_1_10_1_7b4d6f  (label: 'Contratación de seguro sobre saldo deudor')
[Operacion] 'control fin de archivo' (3 nodos):
    - Operacion_control_fin_de_archivo__snp_cheq_7_1_8_8fa36f  (label: 'Control fin de archivo')
    - Operacion_control_fin_de_archivo__snp_cheq_sbloque10_02628f  (label: 'Control fin de archivo')
    - Operacion_control_fin_de_archivo__snp_tr_1_6_2_6_eaf45a  (label: 'Control fin de archivo')
[Operacion] 'control fin de lote' (2 nodos):
    - Operacion_control_fin_de_lote__snp_cheq_7_1_7_3fe86d  (label: 'Control fin de lote')
    - Operacion_control_fin_de_lote__snp_tr_1_6_2_5_b6d1db  (label: 'Control fin de lote')
[Operacion] 'cotejo listados con registros contables' (2 nodos):
    - Operacion_cotejo_listados_con_registros_contables__ri_ccna_d1a3l2_s19_7b4d88  (label: 'Cotejo listados con registros contables')
    - Operacion_cotejo_listados_con_registros_contables__ri_ccna_d1a3l2_s8_96dd7b  (label: 'Cotejo listados con registros contables')
[Operacion] 'creacion de carpeta crediticia' (2 nodos):
    - Operacion_creacion_de_carpeta_crediticia__manori_1_2_6_6c0e6d  (label: 'Creación de carpeta crediticia')
    - Operacion_creacion_de_carpeta_crediticia__manori_3_2_5_564f4a  (label: 'Creación de carpeta crediticia')
[Operacion] 'creacion de carpeta legal post-desembolso' (2 nodos):
    - Operacion_creacion_de_carpeta_legal_post_desembolso__manori_1_2_9_aac312  (label: 'Creación de carpeta legal post-desembolso')
    - Operacion_creacion_de_carpeta_legal_post_desembolso__manori_3_2_8_aa06b5  (label: 'Creación de carpeta legal post-desembolso')
[Operacion] 'creacion y emision de letra hipotecaria' (2 nodos):
    - Operacion_creacion_y_emision_de_letra_hipotecaria__manori_1_2_8_3_46a226  (label: 'Creación y emisión de Letra Hipotecaria')
    - Operacion_creacion_y_emision_de_letra_hipotecaria__manori_sbloque4_fd27b3  (label: 'Creación y emisión de letra hipotecaria')
[Operacion] 'debitos automaticos para servicios de cobranza' (2 nodos):
    - Operacion_debitos_automaticos_para_servicios_de_cobranza__depaho_1_10_2_75457c  (label: 'Débitos automáticos para servicios de cobranza')
    - Operacion_debitos_automaticos_para_servicios_de_cobranza__depaho_3_4_8_2_eb8637  (label: 'Débitos automáticos para servicios de cobranza')
[Operacion] 'depositos a plazo fijo en moneda extranjera' (2 nodos):
    - Operacion_depositos_a_plazo_fijo_en_moneda_extranjera__efemin_1_3_5_22cba2  (label: 'Depósitos a plazo fijo en moneda extranjera')
    - Operacion_depositos_a_plazo_fijo_en_moneda_extranjera__efemin_1_4_2_1aff73  (label: 'Depósitos a plazo fijo en moneda extranjera')
[Operacion] 'depositos a plazo fijo en pesos' (2 nodos):
    - Operacion_depositos_a_plazo_fijo_en_pesos__efemin_1_3_5_e40360  (label: 'Depósitos a plazo fijo en pesos')
    - Operacion_depositos_a_plazo_fijo_en_pesos__efemin_1_4_2_e49e11  (label: 'Depósitos a plazo fijo en pesos')
[Operacion] 'depositos en caja de ahorros' (2 nodos):
    - Operacion_depositos_en_caja_de_ahorros__depaho_3_3_e5e4b4  (label: 'Depósitos en caja de ahorros')
    - Operacion_depositos_en_caja_de_ahorros__depaho_4_20_4_c7879b  (label: 'Depósitos en caja de ahorros')
[Operacion] 'descuento de titulos de credito con responsabilidad cedente' (3 nodos):
    - Operacion_descuento_de_titulos_de_credito_con_responsabilidad_cedente__cajasc_5_1_10_6f3101  (label: 'Descuento de títulos de crédito con responsabilidad cedente')
    - Operacion_descuento_de_titulos_de_credito_con_responsabilidad_cedente__cajasc_5_1_5_11390f  (label: 'Descuento de títulos de crédito con responsabilidad cedente')
    - Operacion_descuento_de_titulos_de_credito_con_responsabilidad_cedente__cajasc_5_1_5_1_bde30c  (label: 'Descuento de títulos de crédito con responsabilidad cedente')
[Operacion] 'elaboracion de informes de riesgos' (2 nodos):
    - Operacion_elaboracion_de_informes_de_riesgos__adrei_2_1_2_1_f053f7  (label: 'Elaboración de informes de riesgos')
    - Operacion_elaboracion_de_informes_de_riesgos__adrei_2_1_8a428a  (label: 'Elaboración de informes de riesgos')
[Operacion] 'emision billete $ 100 taruca' (2 nodos):
    - Operacion_emision_billete_100_taruca__cirmo3_1_2_19_1_ef6239  (label: 'Emisión billete $ 100 Taruca')
    - Operacion_emision_billete_100_taruca__cirmo3_1_2_19_9a1afc  (label: 'Emisión billete $ 100 Taruca')
[Operacion] 'emision billete $ 1000 hornero' (2 nodos):
    - Operacion_emision_billete_1000_hornero__cirmo3_1_2_17_1_9a0470  (label: 'Emisión billete $ 1000 Hornero')
    - Operacion_emision_billete_1000_hornero__cirmo3_1_2_17_c1cc1a  (label: 'Emisión billete $ 1000 Hornero')
[Operacion] 'emision billete $ 20 guanaco' (2 nodos):
    - Operacion_emision_billete_20_guanaco__cirmo3_1_2_16_1_c43a85  (label: 'Emisión billete $ 20 Guanaco')
    - Operacion_emision_billete_20_guanaco__cirmo3_1_2_16_45d515  (label: 'Emisión billete $ 20 Guanaco')
[Operacion] 'emision billete $ 50 condor andino' (3 nodos):
    - Operacion_emision_billete_50_condor_andino__cirmo3_1_2_18_1_1f233b  (label: 'Emisión billete $ 50 Cóndor Andino')
    - Operacion_emision_billete_50_condor_andino__cirmo3_1_2_18_2_9ca864  (label: 'Emisión billete $ 50 Cóndor Andino')
    - Operacion_emision_billete_50_condor_andino__cirmo3_1_2_18_816720  (label: 'Emisión billete $ 50 Cóndor Andino')
[Operacion] 'emision billete $ 50 islas malvinas' (2 nodos):
    - Operacion_emision_billete_50_islas_malvinas__cirmo3_1_2_12_1_5ee052  (label: 'Emisión billete $ 50 Islas Malvinas')
    - Operacion_emision_billete_50_islas_malvinas__cirmo3_1_2_12_aef24f  (label: 'Emisión billete $ 50 Islas Malvinas')
[Operacion] 'emision billete $ 500 yaguarete' (2 nodos):
    - Operacion_emision_billete_500_yaguarete__cirmo3_1_2_14_1_ecbe98  (label: 'Emisión billete $ 500 Yaguareté')
    - Operacion_emision_billete_500_yaguarete__cirmo3_1_2_14_87ab63  (label: 'Emisión billete $ 500 Yaguareté')
[Operacion] 'emision billete $10 000 heroinas y heroes' (2 nodos):
    - Operacion_emision_billete_10_000_heroinas_y_heroes__cirmo3_1_2_22_0e3177  (label: 'Emisión billete $10 000 Heroínas y Héroes')
    - Operacion_emision_billete_10_000_heroinas_y_heroes__cirmo3_1_2_22_1_dcf499  (label: 'Emisión billete $10 000 Heroínas y Héroes')
[Operacion] 'emision billete $20 000 heroinas y heroes' (2 nodos):
    - Operacion_emision_billete_20_000_heroinas_y_heroes__cirmo3_1_2_23_1_ece296  (label: 'Emisión billete $20 000 Heroínas y Héroes')
    - Operacion_emision_billete_20_000_heroinas_y_heroes__cirmo3_1_2_23_324981  (label: 'Emisión billete $20 000 Heroínas y Héroes')
[Operacion] 'emision de cedip' (3 nodos):
    - Operacion_emision_de_cedip__snp_cheq_3_6_2_1_3f2fd9  (label: 'Emisión de CEDIP')
    - Operacion_emision_de_cedip__snp_cheq_3_6_5_1_c6c9cb  (label: 'Emisión de CEDIP')
    - Operacion_emision_de_cedip__snp_cheq_3_6_7_2_6ae637  (label: 'Emisión de CEDIP')
[Operacion] 'entrega de certificados para acciones civiles de echeq' (2 nodos):
    - Operacion_entrega_de_certificados_para_acciones_civiles_de_echeq__snp_cheq_8_4_2_11_5ac2a7  (label: 'Entrega de certificados para acciones civiles de ECHEQ')
    - Operacion_entrega_de_certificados_para_acciones_civiles_de_echeq__snp_cheq_8_4_4_9_9946da  (label: 'Entrega de certificados para acciones civiles de ECHEQ')
[Operacion] 'entrega de chc al bcra' (2 nodos):
    - Operacion_entrega_de_chc_al_bcra__cirmo3_8_6_1_dd8c3c  (label: 'Entrega de CHC al BCRA')
    - Operacion_entrega_de_chc_al_bcra__cirmo3_8_6_2_2_9b5d41  (label: 'Entrega de CHC al BCRA')
[Operacion] 'envio de informacion electronica a cec' (2 nodos):
    - Operacion_envio_de_informacion_electronica_a_cec__snp_cheq_5_2_2_d2ef9d  (label: 'Envío de información electrónica a CEC')
    - Operacion_envio_de_informacion_electronica_a_cec__snp_tr_1_5_2_2_05cec1  (label: 'Envío de información electrónica a CEC')
[Operacion] 'estres de credito o liquidez en el mercado' (2 nodos):
    - Operacion_estres_de_credito_o_liquidez_en_el_mercado__lingeef_3_5_4_0c35bd  (label: 'Estrés de crédito o liquidez en el mercado')
    - Operacion_estres_de_credito_o_liquidez_en_el_mercado__lingeef_3_5_4_4_8d8967  (label: 'Estrés de crédito o liquidez en el mercado')
[Operacion] 'evaluacion de solvencia de solicitantes' (2 nodos):
    - Operacion_evaluacion_de_solvencia_de_solicitantes__manori_1_1_4_4_0f597e  (label: 'Evaluación de solvencia de solicitantes')
    - Operacion_evaluacion_de_solvencia_de_solicitantes__manori_3_1_4_4_81e464  (label: 'Evaluación de solvencia de solicitantes')
[Operacion] 'extraccion de fondos mediante cajeros automaticos' (2 nodos):
    - Operacion_extraccion_de_fondos_mediante_cajeros_automaticos__depaho_2_3_2_1_6cfac8  (label: 'Extracción de fondos mediante cajeros automáticos')
    - Operacion_extraccion_de_fondos_mediante_cajeros_automaticos__depaho_3_11_5_1_d327d4  (label: 'Extracción de fondos mediante cajeros automáticos')
[Operacion] 'extraccion de fondos por ventanilla' (2 nodos):
    - Operacion_extraccion_de_fondos_por_ventanilla__depaho_1_7_1_d0a66c  (label: 'Extracción de fondos por ventanilla')
    - Operacion_extraccion_de_fondos_por_ventanilla__depaho_2_3_2_2_6c9664  (label: 'Extracción de fondos por ventanilla')
[Operacion] 'fondos de seguridad con efecto iris' (7 nodos):
    - Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_12_3_3a51d4  (label: 'Fondos de seguridad con efecto iris')
    - Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_14_3_1c6f96  (label: 'Fondos de seguridad con efecto iris')
    - Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_15_3_d06c9a  (label: 'Fondos de seguridad con efecto iris')
    - Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_18_3_fc5341  (label: 'Fondos de seguridad con efecto iris')
    - Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_19_3_5f90fe  (label: 'Fondos de seguridad con efecto iris')
    - Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_20_3_bbb5e3  (label: 'Fondos de seguridad con efecto iris')
    - Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_21_3_c9296b  (label: 'Fondos de seguridad con efecto iris')
[Operacion] 'fondos de seguridad con efecto iris — anverso' (3 nodos):
    - Operacion_fondos_de_seguridad_con_efecto_iris_anverso__cirmo3_1_2_16_3_0c3792  (label: 'Fondos de seguridad con efecto iris — anverso')
    - Operacion_fondos_de_seguridad_con_efecto_iris_anverso__cirmo3_1_2_17_3_d03160  (label: 'Fondos de seguridad con efecto iris — anverso')
    - Operacion_fondos_de_seguridad_con_efecto_iris_anverso__cirmo3_1_2_22_3_9dc625  (label: 'Fondos de seguridad con efecto iris — anverso')
[Operacion] 'gestion del riesgo operacional' (2 nodos):
    - Operacion_gestion_del_riesgo_operacional__lingeef_6_2_4_6_5722a0  (label: 'Gestión del riesgo operacional')
    - Operacion_gestion_del_riesgo_operacional__lingeef_6_3_8b6034  (label: 'Gestión del riesgo operacional')
[Operacion] 'hipoteca en primer grado sobre inmuebles' (2 nodos):
    - Operacion_hipoteca_en_primer_grado_sobre_inmuebles__cajasc_5_2_1_01cf08  (label: 'Hipoteca en primer grado sobre inmuebles')
    - Operacion_hipoteca_en_primer_grado_sobre_inmuebles__cajasc_5_5_10_72bdd0  (label: 'Hipoteca en primer grado sobre inmuebles')
[Operacion] 'identificacion capacidades visuales reducidas' (2 nodos):
    - Operacion_identificacion_capacidades_visuales_reducidas__cirmo3_1_2_14_3_ef36a3  (label: 'Identificación capacidades visuales reducidas')
    - Operacion_identificacion_capacidades_visuales_reducidas__cirmo3_1_2_15_3_ebfefd  (label: 'Identificación capacidades visuales reducidas')
[Operacion] 'identificacion para personas con ceguera' (2 nodos):
    - Operacion_identificacion_para_personas_con_ceguera__cirmo3_1_2_20_3_c4395f  (label: 'Identificación para personas con ceguera')
    - Operacion_identificacion_para_personas_con_ceguera__cirmo3_1_2_21_3_7114d8  (label: 'Identificación para personas con ceguera')
[Operacion] 'identificacion para personas con discapacidades visuales' (2 nodos):
    - Operacion_identificacion_para_personas_con_discapacidades_visuales__cirmo3_1_2_18_3_edb627  (label: 'Identificación para personas con discapacidades visuales')
    - Operacion_identificacion_para_personas_con_discapacidades_visuales__cirmo3_1_2_19_3_5092ad  (label: 'Identificación para personas con discapacidades visuales')
[Operacion] 'imagen latente con iniciales ra' (2 nodos):
    - Operacion_imagen_latente_con_iniciales_ra__cirmo3_1_2_18_3_81f628  (label: 'Imagen latente con iniciales RA')
    - Operacion_imagen_latente_con_iniciales_ra__cirmo3_1_2_19_3_1ca6b4  (label: 'Imagen latente con iniciales RA')
[Operacion] 'imagen latente iniciales ra' (2 nodos):
    - Operacion_imagen_latente_iniciales_ra__cirmo3_1_2_14_3_0673c4  (label: 'Imagen latente iniciales RA')
    - Operacion_imagen_latente_iniciales_ra__cirmo3_1_2_15_3_0c548c  (label: 'Imagen latente iniciales RA')
[Operacion] 'imagenes pendientes de envio y recepcion' (2 nodos):
    - Operacion_imagenes_pendientes_de_envio_y_recepcion__snp_cheq_7_1_12_0fa47c  (label: 'Imágenes pendientes de envío y recepción')
    - Operacion_imagenes_pendientes_de_envio_y_recepcion__snp_cheq_7_1_13_5270ad  (label: 'Imágenes pendientes de envío y recepción')
[Operacion] 'impresion calcografica con relieve' (5 nodos):
    - Operacion_impresion_calcografica_con_relieve__cirmo3_1_2_12_3_de0271  (label: 'Impresión calcográfica con relieve')
    - Operacion_impresion_calcografica_con_relieve__cirmo3_1_2_13_3_abba20  (label: 'Impresión calcográfica con relieve')
    - Operacion_impresion_calcografica_con_relieve__cirmo3_1_2_14_3_cc7c59  (label: 'Impresión calcográfica con relieve')
    - Operacion_impresion_calcografica_con_relieve__cirmo3_1_2_15_3_27ba20  (label: 'Impresión calcográfica con relieve')
    - Operacion_impresion_calcografica_con_relieve__cirmo3_1_2_19_3_1c3b21  (label: 'Impresión calcográfica con relieve')
[Operacion] 'impresion offset billete $1000' (2 nodos):
    - Operacion_impresion_offset_billete_1000__cirmo3_1_2_17_3_41b472  (label: 'Impresión offset billete $1000')
    - Operacion_impresion_offset_billete_1000__cirmo3_1_2_20_3_862ab8  (label: 'Impresión offset billete $1000')
[Operacion] 'iniciacion de actividades de sucursal' (2 nodos):
    - Operacion_iniciacion_de_actividades_de_sucursal__expaef_1_5_1_1_6f254b  (label: 'Iniciación de actividades de sucursal')
    - Operacion_iniciacion_de_actividades_de_sucursal__expaef_1_5_2_2_99f333  (label: 'Iniciación de actividades de sucursal')
[Operacion] 'instalacion de centro de transmision' (2 nodos):
    - Operacion_instalacion_de_centro_de_transmision__snp_cheq_2_2_2_4_ea3872  (label: 'Instalación de Centro de transmisión')
    - Operacion_instalacion_de_centro_de_transmision__snp_tr_1_1_2_994287  (label: 'Instalación de Centro de Transmisión')
[Operacion] 'instalacion pulsador de alarma' (2 nodos):
    - Operacion_instalacion_pulsador_de_alarma__ri_mmsef_2_2_2_4_c4f8a7  (label: 'Instalación pulsador de alarma')
    - Operacion_instalacion_pulsador_de_alarma__ri_mmsef_2_2_3_4_66b3f9  (label: 'Instalación pulsador de alarma')
[Operacion] 'intercambio fisico de cheques rechazados' (2 nodos):
    - Operacion_intercambio_fisico_de_cheques_rechazados__snp_cheq_2_2_2_5_c35437  (label: 'Intercambio físico de cheques rechazados')
    - Operacion_intercambio_fisico_de_cheques_rechazados__snp_cheq_3_2_7_2_d56608  (label: 'Intercambio físico de cheques rechazados')
[Operacion] 'liquidacion por diferencia' (2 nodos):
    - Operacion_liquidacion_por_diferencia__opefci_3_4_3_9c3877  (label: 'Liquidación por diferencia')
    - Operacion_liquidacion_por_diferencia__opefci_4_4_2_3_812b23  (label: 'Liquidación por diferencia')
[Operacion] 'motivo complementacion frente-dorso' (2 nodos):
    - Operacion_motivo_complementacion_frente_dorso__cirmo3_1_2_14_3_613288  (label: 'Motivo complementación frente-dorso')
    - Operacion_motivo_complementacion_frente_dorso__cirmo3_1_2_15_3_fdf782  (label: 'Motivo complementación frente-dorso')
[Operacion] 'motivo de complementacion frente-dorso' (5 nodos):
    - Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_12_3_bb0258  (label: 'Motivo de complementación frente-dorso')
    - Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_18_3_5670ff  (label: 'Motivo de complementación frente-dorso')
    - Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_19_3_739142  (label: 'Motivo de complementación frente-dorso')
    - Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_20_3_4b35d9  (label: 'Motivo de complementación frente-dorso')
    - Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_21_3_f48c2c  (label: 'Motivo de complementación frente-dorso')
[Operacion] 'numeracion horizontal en reverso' (3 nodos):
    - Operacion_numeracion_horizontal_en_reverso__cirmo3_1_2_18_3_90b13b  (label: 'Numeración horizontal en reverso')
    - Operacion_numeracion_horizontal_en_reverso__cirmo3_1_2_19_3_7aea0a  (label: 'Numeración horizontal en reverso')
    - Operacion_numeracion_horizontal_en_reverso__cirmo3_1_2_21_3_c8da52  (label: 'Numeración horizontal en reverso')
[Operacion] 'numeracion horizontal — reverso' (2 nodos):
    - Operacion_numeracion_horizontal_reverso__cirmo3_1_2_16_3_9261a3  (label: 'Numeración horizontal — reverso')
    - Operacion_numeracion_horizontal_reverso__cirmo3_1_2_17_3_9f8fdb  (label: 'Numeración horizontal — reverso')
[Operacion] 'numeracion vertical en reverso' (3 nodos):
    - Operacion_numeracion_vertical_en_reverso__cirmo3_1_2_18_3_1d5284  (label: 'Numeración vertical en reverso')
    - Operacion_numeracion_vertical_en_reverso__cirmo3_1_2_19_3_39a6d7  (label: 'Numeración vertical en reverso')
    - Operacion_numeracion_vertical_en_reverso__cirmo3_1_2_21_3_070788  (label: 'Numeración vertical en reverso')
[Operacion] 'numeracion vertical — reverso' (2 nodos):
    - Operacion_numeracion_vertical_reverso__cirmo3_1_2_16_3_e60396  (label: 'Numeración vertical — reverso')
    - Operacion_numeracion_vertical_reverso__cirmo3_1_2_17_3_14cbbe  (label: 'Numeración vertical — reverso')
[Operacion] 'otorgamiento de prestamos hipotecarios' (2 nodos):
    - Operacion_otorgamiento_de_prestamos_hipotecarios__cajasc_4_2_2_3_dc0924  (label: 'Otorgamiento de préstamos hipotecarios')
    - Operacion_otorgamiento_de_prestamos_hipotecarios__manori_1_1_5_3_170f67  (label: 'Otorgamiento de préstamos hipotecarios')
[Operacion] 'pago de impuestos y servicios por canales electronicos' (2 nodos):
    - Operacion_pago_de_impuestos_y_servicios_por_canales_electronicos__depaho_2_3_2_4_ac4b4c  (label: 'Pago de impuestos y servicios por canales electrónicos')
    - Operacion_pago_de_impuestos_y_servicios_por_canales_electronicos__depaho_3_11_5_4_376c3e  (label: 'Pago de impuestos y servicios por canales electrónicos')
[Operacion] 'pago de prestamos' (2 nodos):
    - Operacion_pago_de_prestamos__depaho_1_10_1_216e28  (label: 'Pago de préstamos')
    - Operacion_pago_de_prestamos__depaho_3_4_8_1_b49304  (label: 'Pago de préstamos')
[Operacion] 'plan para contingencias' (2 nodos):
    - Operacion_plan_para_contingencias__lingeef_1_4_8_fc7497  (label: 'Plan para contingencias')
    - Operacion_plan_para_contingencias__lingeef_2_3_5_0f0cbc  (label: 'Plan para contingencias')
[Operacion] 'precancelacion parcial de prestamo hipotecario' (2 nodos):
    - Operacion_precancelacion_parcial_de_prestamo_hipotecario__manori_1_1_9_1_803b26  (label: 'Precancelación parcial de préstamo hipotecario')
    - Operacion_precancelacion_parcial_de_prestamo_hipotecario__manori_1_1_9_2_d0fc55  (label: 'Precancelación parcial de préstamo hipotecario')
[Operacion] 'precancelacion total de prestamo hipotecario' (2 nodos):
    - Operacion_precancelacion_total_de_prestamo_hipotecario__manori_1_1_9_1_a780d1  (label: 'Precancelación total de préstamo hipotecario')
    - Operacion_precancelacion_total_de_prestamo_hipotecario__manori_1_1_9_2_12a284  (label: 'Precancelación total de préstamo hipotecario')
[Operacion] 'preparacion del archivo de rechazos' (2 nodos):
    - Operacion_preparacion_del_archivo_de_rechazos__snp_cheq_3_2_6_1_4d91de  (label: 'Preparación del archivo de rechazos')
    - Operacion_preparacion_del_archivo_de_rechazos__snp_cheq_3_3_5_1_84c1ae  (label: 'Preparación del archivo de rechazos')
[Operacion] 'preparacion para escenarios severos de estres' (2 nodos):
    - Operacion_preparacion_para_escenarios_severos_de_estres__lingeef_3_3_11_4_37e58c  (label: 'Preparación para escenarios severos de estrés')
    - Operacion_preparacion_para_escenarios_severos_de_estres__lingeef_4_3_5_3_046579  (label: 'Preparación para escenarios severos de estrés')
[Operacion] 'presentacion de cedip' (2 nodos):
    - Operacion_presentacion_de_cedip__snp_cheq_3_6_4_1_6df65c  (label: 'Presentación de CEDIP')
    - Operacion_presentacion_de_cedip__snp_cheq_7_2_3_b903c2  (label: 'Presentación de CEDIP')
[Operacion] 'presentacion de cheques y otros documentos compensables' (2 nodos):
    - Operacion_presentacion_de_cheques_y_otros_documentos_compensables__snp_cheq_7_1_3_cadf16  (label: 'Presentación de cheques y otros documentos compensables')
    - Operacion_presentacion_de_cheques_y_otros_documentos_compensables__snp_cheq_7_1_9_887e18  (label: 'Presentación de cheques y otros documentos compensables')
[Operacion] 'prestacion de servicios de auditoria externa' (2 nodos):
    - Operacion_prestacion_de_servicios_de_auditoria_externa__ri_ccna_d1a1_2_1_1_8f0c04  (label: 'Prestación de servicios de auditoría externa')
    - Operacion_prestacion_de_servicios_de_auditoria_externa__ri_ccna_d1a1_2_1_47781c  (label: 'Prestación de servicios de auditoría externa')
[Operacion] 'prestamos uva actualizables por cer' (2 nodos):
    - Operacion_prestamos_uva_actualizables_por_cer__manori_1_1_5_9_6abfcf  (label: 'Préstamos UVA actualizables por CER')
    - Operacion_prestamos_uva_actualizables_por_cer__manori_3_1_5_9_23d78c  (label: 'Préstamos UVA actualizables por CER')
[Operacion] 'procedimientos alternativos saldos confirmaciones no recibidas' (2 nodos):
    - Operacion_procedimientos_alternativos_saldos_confirmaciones_no_recibidas__ri_ccna_d1a3l2_s_4b85d4  (label: 'Procedimientos alternativos saldos confirmaciones no recibidas')
    - Operacion_procedimientos_alternativos_saldos_confirmaciones_no_recibidas__ri_ccna_d1a3l2_s_713175  (label: 'Procedimientos alternativos saldos confirmaciones no recibidas')
[Operacion] 'pruebas de estres' (6 nodos):
    - Operacion_pruebas_de_estres__lingeef_11_2_1_4_90e2af  (label: 'Pruebas de estrés')
    - Operacion_pruebas_de_estres__lingeef_11_2_3_1_93712f  (label: 'Pruebas de estrés')
    - Operacion_pruebas_de_estres__lingeef_4_2_1_5_781cac  (label: 'Pruebas de estrés')
    - Operacion_pruebas_de_estres__lingeef_4_2_2_4_3af163  (label: 'Pruebas de estrés')
    - Operacion_pruebas_de_estres__lingeef_4_3_4_9fbec6  (label: 'Pruebas de estrés')
    - Operacion_pruebas_de_estres__lingeef_7_3_3_6_2e6d6e  (label: 'Pruebas de estrés')
[Operacion] 'recepcion de archivos de compensacion' (4 nodos):
    - Operacion_recepcion_de_archivos_de_compensacion__snp_cheq_3_1_3_1_a85708  (label: 'Recepción de archivos de compensación')
    - Operacion_recepcion_de_archivos_de_compensacion__snp_cheq_3_1_3_2_5ef8b1  (label: 'Recepción de archivos de compensación')
    - Operacion_recepcion_de_archivos_de_compensacion__snp_tr_1_3_4_1_32e6b8  (label: 'Recepción de archivos de compensación')
    - Operacion_recepcion_de_archivos_de_compensacion__snp_tr_1_3_4_2_8f4b1d  (label: 'Recepción de archivos de compensación')
[Operacion] 'rechazo de entidad depositaria' (2 nodos):
    - Operacion_rechazo_de_entidad_depositaria__snp_cheq_7_1_3_e8c633  (label: 'Rechazo de entidad depositaria')
    - Operacion_rechazo_de_entidad_depositaria__snp_cheq_7_1_9_c784f3  (label: 'Rechazo de entidad depositaria')
[Operacion] 'reporte numero de serie caja tesoro movil' (2 nodos):
    - Operacion_reporte_numero_de_serie_caja_tesoro_movil__ri_mmsef_2_3_5_2_2da840  (label: 'Reporte número de serie caja tesoro móvil')
    - Operacion_reporte_numero_de_serie_caja_tesoro_movil__ri_mmsef_2_3_7_2_2_2bc1df  (label: 'Reporte número de serie caja tesoro móvil')
[Operacion] 'residencia en sitio seguro bcra' (2 nodos):
    - Operacion_residencia_en_sitio_seguro_bcra__ceninf_1_1_8437c1  (label: 'Residencia en sitio seguro BCRA')
    - Operacion_residencia_en_sitio_seguro_bcra__ceninf_s3_bbc90e  (label: 'Residencia en sitio seguro BCRA')
[Operacion] 'respaldo crediticio implicito a titulizacion' (2 nodos):
    - Operacion_respaldo_crediticio_implicito_a_titulizacion__lingeef_7_3_1_1_c06d49  (label: 'Respaldo crediticio implícito a titulización')
    - Operacion_respaldo_crediticio_implicito_a_titulizacion__lingeef_7_3_1_8f3ecb  (label: 'Respaldo crediticio implícito a titulización')
[Operacion] 'servicio de transferencias inmediatas' (2 nodos):
    - Operacion_servicio_de_transferencias_inmediatas__snp_tr_2_2_15_e302a8  (label: 'Servicio de transferencias inmediatas')
    - Operacion_servicio_de_transferencias_inmediatas__snp_tr_2_2_1_681d43  (label: 'Servicio de transferencias inmediatas')
[Operacion] 'solicitud de prestamo prendario automotor' (2 nodos):
    - Operacion_solicitud_de_prestamo_prendario_automotor__manori_3_1_3_962f45  (label: 'Solicitud de préstamo prendario automotor')
    - Operacion_solicitud_de_prestamo_prendario_automotor__manori_3_2_1_c3f807  (label: 'Solicitud de préstamo prendario automotor')
[Operacion] 'solicitud informe comercial o crediticio' (2 nodos):
    - Operacion_solicitud_informe_comercial_o_crediticio__manori_1_2_3_76c356  (label: 'Solicitud informe comercial o crediticio')
    - Operacion_solicitud_informe_comercial_o_crediticio__manori_3_2_3_eb2546  (label: 'Solicitud informe comercial o crediticio')
[Operacion] 'tinta de variabilidad optica' (5 nodos):
    - Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_14_3_51c1f2  (label: 'Tinta de variabilidad óptica')
    - Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_15_3_58046e  (label: 'Tinta de variabilidad óptica')
    - Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_19_3_d9a9bc  (label: 'Tinta de variabilidad óptica')
    - Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_20_3_7ae288  (label: 'Tinta de variabilidad óptica')
    - Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_21_3_f460f4  (label: 'Tinta de variabilidad óptica')
[Operacion] 'transferencia de fondos remanentes a saldos inmovilizados' (2 nodos):
    - Operacion_transferencia_de_fondos_remanentes_a_saldos_inmovilizados__depaho_2_8_79328a  (label: 'Transferencia de fondos remanentes a saldos inmovilizados')
    - Operacion_transferencia_de_fondos_remanentes_a_saldos_inmovilizados__depaho_3_5_7_c79bd3  (label: 'Transferencia de fondos remanentes a saldos inmovilizados')
[Operacion] 'transferencias electronicas y ordenes telefonicas' (2 nodos):
    - Operacion_transferencias_electronicas_y_ordenes_telefonicas__depaho_1_6_3_c29d27  (label: 'Transferencias electrónicas y órdenes telefónicas')
    - Operacion_transferencias_electronicas_y_ordenes_telefonicas__depaho_1_7_3_79bb57  (label: 'Transferencias electrónicas y órdenes telefónicas')
[Operacion] 'transferencias por medios electronicos' (2 nodos):
    - Operacion_transferencias_por_medios_electronicos__depaho_2_3_2_5_b443f9  (label: 'Transferencias por medios electrónicos')
    - Operacion_transferencias_por_medios_electronicos__depaho_3_11_5_5_473cae  (label: 'Transferencias por medios electrónicos')
[Operacion] 'transmision de archivos de cheques a cec' (2 nodos):
    - Operacion_transmision_de_archivos_de_cheques_a_cec__snp_cheq_3_1_1_4bd63d  (label: 'Transmisión de archivos de cheques a CEC')
    - Operacion_transmision_de_archivos_de_cheques_a_cec__snp_cheq_3_2_3_83b0e0  (label: 'Transmisión de archivos de cheques a CEC')
[Operacion] 'truncamiento de cheques' (2 nodos):
    - Operacion_truncamiento_de_cheques__snp_cheq_2_1_0eea74  (label: 'Truncamiento de cheques')
    - Operacion_truncamiento_de_cheques__snp_cheq_s4_db4792  (label: 'Truncamiento de cheques')
[Potestad] 'acreditacion de pagos en cuentas especiales u otra cuenta a la vista' (2 nodos):
    - Potestad_acreditacion_de_pagos_en_cuentas_especiales_u_otra_cuenta_a_la_vista__las_entida_782fcb  (label: 'Acreditación de pagos en cuentas especiales u otra cuenta a la vista')
    - Potestad_acreditacion_de_pagos_en_cuentas_especiales_u_otra_cuenta_a_la_vista__las_entida_7c0cb2  (label: 'Acreditación de pagos en cuentas especiales u otra cuenta a la vista')
[Potestad] 'agregar campos adicionales a la base de datos' (2 nodos):
    - Potestad_agregar_campos_adicionales_a_la_base_de_datos__cada_entidad_financiera_tiene_la__0ff748  (label: 'Agregar campos adicionales a la base de datos')
    - Potestad_agregar_campos_adicionales_a_la_base_de_datos__cada_entidad_financiera_tiene_la__6aca3b  (label: 'Agregar campos adicionales a la base de datos')
[Potestad] 'autorizacion emision moneda conmemorativa' (2 nodos):
    - Potestad_autorizacion_emision_moneda_conmemorativa__el_bcra_en_su_caracter_de_ente_emisor_8453bb  (label: 'Autorización emisión moneda conmemorativa')
    - Potestad_autorizacion_emision_moneda_conmemorativa__el_bcra_en_su_caracter_de_ente_emisor_ca8e58  (label: 'Autorización emisión moneda conmemorativa')
[Potestad] 'autorizar captacion de depositos en otras monedas' (3 nodos):
    - Potestad_autorizar_captacion_de_depositos_en_otras_monedas__el_bcra_tiene_la_facultad_de__8e7fd4  (label: 'Autorizar captación de depósitos en otras monedas')
    - Potestad_autorizar_captacion_de_depositos_en_otras_monedas__el_bcra_tiene_la_facultad_de__c00b90  (label: 'Autorizar captación de depósitos en otras monedas')
    - Potestad_autorizar_captacion_de_depositos_en_otras_monedas__el_bcra_tiene_la_facultad_de__c46af9  (label: 'Autorizar captación de depósitos en otras monedas')
[Potestad] 'desarrollar base de datos en forma conveniente' (2 nodos):
    - Potestad_desarrollar_base_de_datos_en_forma_conveniente__la_entidad_financiera_tiene_la_f_0a4374  (label: 'Desarrollar base de datos en forma conveniente')
    - Potestad_desarrollar_base_de_datos_en_forma_conveniente__la_entidad_financiera_tiene_la_f_b5b0e7  (label: 'Desarrollar base de datos en forma conveniente')
[Potestad] 'eleccion de sistemas de informacion' (2 nodos):
    - Potestad_eleccion_de_sistemas_de_informacion__cada_entidad_financiera_tiene_la_facultad_d_02a168  (label: 'Elección de sistemas de información')
    - Potestad_eleccion_de_sistemas_de_informacion__cada_entidad_financiera_tiene_la_facultad_d_e61581  (label: 'Elección de sistemas de información')
[Potestad] 'facultad de realizar consultas puntuales' (2 nodos):
    - Potestad_facultad_de_realizar_consultas_puntuales__el_publico_en_general_esta_facultado_p_54dd79  (label: 'Facultad de realizar consultas puntuales')
    - Potestad_facultad_de_realizar_consultas_puntuales__se_habilita_la_realizacion_de_consulta_3ed5cc  (label: 'Facultad de realizar consultas puntuales')
[Potestad] 'facultad de realizar rechazos' (2 nodos):
    - Potestad_facultad_de_realizar_rechazos__las_entidades_quedan_facultadas_a_realizar_rechaz_8aebb4  (label: 'Facultad de realizar rechazos')
    - Potestad_facultad_de_realizar_rechazos__las_entidades_tienen_la_facultad_de_realizar_rech_324e8d  (label: 'Facultad de realizar rechazos')
[Potestad] 'facultad de solicitar retransmision de archivo' (3 nodos):
    - Potestad_facultad_de_solicitar_retransmision_de_archivo__las_entidades_quedan_facultadas__17f031  (label: 'Facultad de solicitar retransmisión de archivo')
    - Potestad_facultad_de_solicitar_retransmision_de_archivo__las_entidades_se_reservan_el_der_a84dbf  (label: 'Facultad de solicitar retransmisión de archivo')
    - Potestad_facultad_de_solicitar_retransmision_de_archivo__las_entidades_tienen_la_facultad_7b35c4  (label: 'Facultad de solicitar retransmisión de archivo')
[Potestad] 'opcion de desafectacion o baja — cliente' (2 nodos):
    - Potestad_opcion_de_desafectacion_o_baja_cliente__el_cliente_tiene_la_facultad_de_manifest_ed6fb8  (label: 'Opción de desafectación o baja — cliente')
    - Potestad_opcion_de_desafectacion_o_baja_cliente__el_cliente_tiene_la_opcion_de_manifestar_6e995a  (label: 'Opción de desafectación o baja — cliente')
[Potestad] 'opcion de formalizar adhesion — cliente' (2 nodos):
    - Potestad_opcion_de_formalizar_adhesion_cliente__el_cliente_tiene_la_facultad_de_formaliza_84efab  (label: 'Opción de formalizar adhesión — cliente')
    - Potestad_opcion_de_formalizar_adhesion_cliente__el_cliente_tiene_la_opcion_de_formalizar__ec9834  (label: 'Opción de formalizar adhesión — cliente')
[Potestad] 'pactar otras formas de retribucion' (2 nodos):
    - Potestad_pactar_otras_formas_de_retribucion__las_entidades_podran_pactar_otras_formas_de__05f1bf  (label: 'Pactar otras formas de retribución')
    - Potestad_pactar_otras_formas_de_retribucion__las_entidades_podran_pactar_otras_formas_de__2b01c8  (label: 'Pactar otras formas de retribución')
[Potestad] 'precancelacion en cualquier momento' (2 nodos):
    - Potestad_precancelacion_en_cualquier_momento__facultad_de_precancelar_en_cualquier_moment_bc7970  (label: 'Precancelación en cualquier momento')
    - Potestad_precancelacion_en_cualquier_momento__facultad_de_precancelar_un_prestamo_prendar_f81e85  (label: 'Precancelación en cualquier momento')
[Potestad] 'solicitud de retransmision de archivos' (2 nodos):
    - Potestad_solicitud_de_retransmision_de_archivos__la_cec_tiene_la_facultad_de_solicitar_la_545809  (label: 'Solicitud de retransmisión de archivos')
    - Potestad_solicitud_de_retransmision_de_archivos__la_cec_tiene_la_facultad_de_solicitar_la_e59eec  (label: 'Solicitud de retransmisión de archivos')
[Potestad] 'transferencia de titularidad y administracion del prestamo' (2 nodos):
    - Potestad_transferencia_de_titularidad_y_administracion_del_prestamo__el_acreedor_podra_tr_e2068e  (label: 'Transferencia de titularidad y administración del préstamo')
    - Potestad_transferencia_de_titularidad_y_administracion_del_prestamo__el_acreedor_tiene_la_fdaa2b  (label: 'Transferencia de titularidad y administración del préstamo')
[Restriccion] 'comisiones solo por utilizacion efectiva' (2 nodos):
    - Restriccion_las_comisiones_o_cargos_por_servicios_adicionales_solo_podran_efectuarse_en_func_6a0723  (label: 'Comisiones solo por utilización efectiva')
    - Restriccion_las_comisiones_o_cargos_por_servicios_adicionales_solo_pueden_efectuarse_en_func_069982  (label: 'Comisiones solo por utilización efectiva')
[Restriccion] 'emisor: companias de seguros locales con reaseguros' (2 nodos):
    - Restriccion_el_seguro_debe_ser_emitido_por_companias_de_seguros_locales_que_cumplan_con_lo_p_ea3448  (label: 'Emisor: compañías de seguros locales con reaseguros')
    - Restriccion_el_seguro_puede_ser_emitido_por_companias_de_seguros_locales_que_cumplan_con_lo__064309  (label: 'Emisor: compañías de seguros locales con reaseguros')
[Restriccion] 'emisor: subsidiarias locales de aseguradoras del exterior' (3 nodos):
    - Restriccion_el_seguro_puede_ser_emitido_por_subsidiarias_locales_de_companias_aseguradoras_d_51c7b8  (label: 'Emisor: subsidiarias locales de aseguradoras del exterior')
    - Restriccion_el_seguro_puede_ser_emitido_por_subsidiarias_locales_de_companias_aseguradoras_d_69c8b5  (label: 'Emisor: subsidiarias locales de aseguradoras del exterior')
    - Restriccion_el_seguro_puede_ser_emitido_por_subsidiarias_locales_de_companias_aseguradoras_d_bfc7dc  (label: 'Emisor: subsidiarias locales de aseguradoras del exterior')
[Restriccion] 'emisor: sucursales locales de aseguradoras del exterior' (3 nodos):
    - Restriccion_el_seguro_puede_ser_emitido_por_sucursales_locales_de_companias_aseguradoras_del_1a3518  (label: 'Emisor: sucursales locales de aseguradoras del exterior')
    - Restriccion_el_seguro_puede_ser_emitido_por_sucursales_locales_de_companias_aseguradoras_del_4a54ce  (label: 'Emisor: sucursales locales de aseguradoras del exterior')
    - Restriccion_el_seguro_puede_ser_emitido_por_sucursales_locales_de_companias_aseguradoras_del_e17013  (label: 'Emisor: sucursales locales de aseguradoras del exterior')
[Restriccion] 'incumplimiento como causal de revocacion' (2 nodos):
    - Restriccion_el_incumplimiento_de_los_requisitos_de_autorizacion_puede_ser_considerado_causal_b0b386  (label: 'Incumplimiento como causal de revocación')
    - Restriccion_el_incumplimiento_de_los_requisitos_de_habilitacion_puede_ser_considerado_causal_b329c5  (label: 'Incumplimiento como causal de revocación')
[Restriccion] 'inhabilidad directores/administradores conducta culpable/fraudulenta' (2 nodos):
    - Restriccion_los_directores_o_administradores_de_sociedad_cuya_conducta_se_calificare_de_culp_9bcadd  (label: 'Inhabilidad directores/administradores conducta culpable/fraudulenta')
    - Restriccion_no_pueden_desempenarse_como_socio_responsable_los_directores_o_administradores_d_4eae4e  (label: 'Inhabilidad directores/administradores conducta culpable/fraudulenta')
[Restriccion] 'inhabilidad fallidos quiebra casual' (2 nodos):
    - Restriccion_los_fallidos_por_quiebra_casual_o_los_concursados_quedan_inhabilitados_hasta_cin_94e967  (label: 'Inhabilidad fallidos quiebra casual')
    - Restriccion_no_pueden_desempenarse_como_socio_responsable_los_fallidos_por_quiebra_casual_o__d4a592  (label: 'Inhabilidad fallidos quiebra casual')
[Restriccion] 'inhabilidad fallidos quiebra culpable/fraudulenta' (2 nodos):
    - Restriccion_los_fallidos_por_quiebra_culpable_o_fraudulenta_quedan_inhabilitados_hasta_diez__a84d9c  (label: 'Inhabilidad fallidos quiebra culpable/fraudulenta')
    - Restriccion_no_pueden_desempenarse_como_socio_responsable_los_fallidos_por_quiebra_culpable__d0c257  (label: 'Inhabilidad fallidos quiebra culpable/fraudulenta')
[Restriccion] 'inhabilidad funcionarios publicos — hasta 2 anos post-cese' (2 nodos):
    - Restriccion_los_funcionarios_de_la_administracion_publica_cuyo_desempeno_se_relacione_con_el_51154e  (label: 'Inhabilidad funcionarios públicos — hasta 2 años post-cese')
    - Restriccion_los_funcionarios_de_la_administracion_publica_cuyo_desempeno_se_relacione_con_el_e1497d  (label: 'Inhabilidad funcionarios públicos — hasta 2 años post-cese')
[Restriccion] 'permanencia minima 180 dias — deudor refinanciado con credito adicional' (3 nodos):
    - Restriccion_el_deudor_clasificado_en_categoria_irrecuperable_que_haya_refinanciado_su_deuda__45e7cc  (label: 'Permanencia mínima 180 días — deudor refinanciado con crédito adicional')
    - Restriccion_el_deudor_clasificado_en_riesgo_medio_que_haya_refinanciado_su_deuda_y_recibido__85cdb5  (label: 'Permanencia mínima 180 días — deudor refinanciado con crédito adicional')
    - Restriccion_limite_de_permanencia_minima_en_la_categoria_riesgo_alto_de_180_dias_para_deudor_95fd25  (label: 'Permanencia mínima 180 días — deudor refinanciado con crédito adicional')
[Restriccion] 'plazo maximo 120 dias para realizacion de procedimientos' (2 nodos):
    - Restriccion_el_plazo_maximo_para_la_realizacion_de_los_procedimientos_previstos_en_la_propue_a476be  (label: 'Plazo máximo 120 días para realización de procedimientos')
    - Restriccion_el_plazo_maximo_para_la_realizacion_de_los_procedimientos_previstos_en_la_propue_c4e3fc  (label: 'Plazo máximo 120 días para realización de procedimientos')
[Restriccion] 'plazo minimo 30 dias — pase pasivo con otras contrapartes' (2 nodos):
    - Restriccion_el_plazo_minimo_de_la_operacion_de_pase_pasivo_con_otras_contrapartes_es_de_30_d_f5f4a4  (label: 'Plazo mínimo 30 días — pase pasivo con otras contrapartes')
    - Restriccion_plazo_minimo_de_30_dias_para_pases_pasivos_con_otras_contrapartes__opefci_4_4_2__a6d6a5  (label: 'Plazo mínimo 30 días — pase pasivo con otras contrapartes')
[Restriccion] 'prohibicion de cargos por reemplazo de tarjetas de debito' (2 nodos):
    - Restriccion_las_entidades_no_podran_cobrar_cargos_ni_comisiones_por_los_reemplazos_de_tarjet_7f8d8c  (label: 'Prohibición de cargos por reemplazo de tarjetas de débito')
    - Restriccion_las_entidades_no_podran_cobrar_cargos_ni_comisiones_por_los_reemplazos_de_tarjet_e660f8  (label: 'Prohibición de cargos por reemplazo de tarjetas de débito')
[Restriccion] 'prohibicion de cobrar cargos y comisiones' (2 nodos):
    - Restriccion_las_entidades_no_podran_cobrar_cargos_ni_comisiones_por_la_apertura_de_cuentas_a_597b4c  (label: 'Prohibición de cobrar cargos y comisiones')
    - Restriccion_las_entidades_no_podran_cobrar_cargos_ni_comisiones_por_la_apertura_de_cuentas_s_cfb68c  (label: 'Prohibición de cobrar cargos y comisiones')
[Restriccion] 'prohibicion de saldo deudor' (2 nodos):
    - Restriccion_los_movimientos_de_cualquier_naturaleza_no_pueden_generar_saldo_deudor__depaho_3_151b67  (label: 'Prohibición de saldo deudor')
    - Restriccion_los_movimientos_de_cuentas_judiciales_no_pueden_generar_saldo_deudor__depaho_3_6_d3fb04  (label: 'Prohibición de saldo deudor')
[Restriccion] 'prohibicion desempeno en relacion de dependencia' (2 nodos):
    - Restriccion_el_auditor_externo_no_debe_desempenarse_en_relacion_de_dependencia_en_la_caja_de_297290  (label: 'Prohibición desempeño en relación de dependencia')
    - Restriccion_el_socio_responsable_no_debe_desempenarse_en_relacion_de_dependencia_en_la_entid_2e2686  (label: 'Prohibición desempeño en relación de dependencia')
[Restriccion] 'prohibicion saldo deudor — movimientos' (2 nodos):
    - Restriccion_los_movimientos_de_cualquier_naturaleza_no_podran_generar_saldo_deudor_en_cuenta_1b8aab  (label: 'Prohibición saldo deudor — movimientos')
    - Restriccion_los_movimientos_de_cualquier_naturaleza_no_podran_generar_saldo_deudor_en_la_cue_326fd2  (label: 'Prohibición saldo deudor — movimientos')
[Sujeto] 'cada una de estas sucursales' (2 nodos):
    - Sujeto_propuesto_cada_una_de_estas_sucursales  (label: 'cada una de estas sucursales')
    - Sujeto_propuesto_cada_una_de_estas_sucursales__snp_cheq  (label: 'cada una de estas sucursales')
[Sujeto] 'el representante legal de la entidad' (2 nodos):
    - Sujeto_propuesto_el_representante_legal_de_la_entidad  (label: 'El representante legal de la entidad')
    - Sujeto_propuesto_el_representante_legal_de_la_entidad__ayccef  (label: 'El representante legal de la entidad')
[Sujeto] 'entidades' (2 nodos):
    - Sujeto_propuesto_entidades  (label: 'entidades')
    - Sujeto_propuesto_entidades__snp_cheq  (label: 'entidades')
[Sujeto] 'la auditoria interna' (2 nodos):
    - Sujeto_propuesto_la_auditoria_interna  (label: 'La Auditoría Interna')
    - Sujeto_propuesto_la_auditoria_interna__lingeef  (label: 'la auditoría interna')
[Sujeto] 'la entidad' (2 nodos):
    - Sujeto_propuesto_la_entidad  (label: 'la entidad')
    - Sujeto_propuesto_la_entidad__snp_cheq  (label: 'la entidad')
[Sujeto] 'las citadas entidades' (2 nodos):
    - Sujeto_propuesto_las_citadas_entidades  (label: 'las citadas entidades')
    - Sujeto_propuesto_las_citadas_entidades__depaho  (label: 'Las citadas entidades')
[Sujeto] 'las entidades' (11 nodos):
    - Sujeto_propuesto_las_entidades  (label: 'Las entidades')
    - Sujeto_propuesto_las_entidades__cirmo3  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__manori  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__nmcief  (label: 'Las entidades')
    - Sujeto_propuesto_las_entidades__ri_ccna  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ri_dcpc  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ri_mmsef  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ri_pgn  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__ri_rml  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__snp_cheq  (label: 'las entidades')
    - Sujeto_propuesto_las_entidades__snp_tr  (label: 'las entidades')
[Sujeto] 'las que se vieran afectadas' (2 nodos):
    - Sujeto_propuesto_las_que_se_vieran_afectadas  (label: 'las que se vieran afectadas')
    - Sujeto_propuesto_las_que_se_vieran_afectadas__snp_cheq  (label: 'las que se vieran afectadas')
[Sujeto] 'los solicitantes' (3 nodos):
    - Sujeto_propuesto_los_solicitantes  (label: 'Los solicitantes')
    - Sujeto_propuesto_los_solicitantes__ayccef  (label: 'los solicitantes')
    - Sujeto_propuesto_los_solicitantes__cajasc  (label: 'los solicitantes')
[Sujeto] 'proveedores de servicios de pago' (2 nodos):
    - Sujeto_propuesto_proveedores_de_servicios_de_pago  (label: 'Proveedores de servicios de pago')
    - Sujeto_proveedor_de_servicios_de_pago  (label: 'Proveedores de servicios de pago')
[Sujeto] 'todo el personal' (2 nodos):
    - Sujeto_propuesto_todo_el_personal  (label: 'todo el personal')
    - Sujeto_propuesto_todo_el_personal__ri_ccna  (label: 'todo el personal')
[TextoOrdenado] 'regimen informativo contable mensual' (2 nodos):
    - TextoOrdenado_ri_gerc_pdf  (label: 'Régimen Informativo Contable Mensual')
    - TextoOrdenado_ri_rml_pdf  (label: 'Régimen Informativo Contable Mensual')
```

### S8 — WARN

WARN — Colisión de label normalizado entre types distintos.

**Resultado:** 85 grupos con el mismo label normalizado en types distintos.

```
'accionistas e integrantes de organos de gobierno' (2 nodos):
    - [Condicion] Condicion_accionistas_e_integrantes_de_organos_de_gobierno__la_declaracion_jurada_se_prese_ee277f
    - [Definicion] Definicion_accionistas_e_integrantes_de_organos_de_gobierno__accionistas_socios_o_equivalen_1faa1c
'adquisicion de participacion significativa' (2 nodos):
    - [Condicion] Condicion_adquisicion_de_participacion_significativa__cuando_la_entidad_financiera_conside_96320c
    - [Operacion] Operacion_adquisicion_de_participacion_significativa__adrei_2_1_2_2_947dea
'agregacion de datos sobre riesgos' (3 nodos):
    - [Definicion] Definicion_agregacion_de_datos_sobre_riesgos__definicion_recopilacion_y_procesamiento_de_da_81c7ec
    - [Operacion] Operacion_agregacion_de_datos_sobre_riesgos__adrei_2_1_2_1_e9f3c4
    - [Operacion] Operacion_agregacion_de_datos_sobre_riesgos__adrei_2_1_42799c
'alta gerencia' (3 nodos):
    - [Definicion] Definicion_alta_gerencia__gerencia_general_y_aquellos_gerentes_que_tengan_poder_decisorio_y_65527e
    - [Definicion] Definicion_alta_gerencia__gerencia_general_y_aquellos_gerentes_que_tengan_poder_decisorio_y_77f963
    - [Sujeto] Sujeto_alta_gerencia
'aplicacion de disposiciones de depositos en caja de ahorros' (5 nodos):
    - [Obligacion] Obligacion_se_aplicaran_las_disposiciones_establecidas_para_los_depositos_en_caja_de_ahorro_c545bf
    - [Obligacion] Obligacion_seran_de_aplicacion_las_disposiciones_establecidas_para_los_depositos_en_caja_de_0a2af0
    - [Obligacion] Obligacion_seran_de_aplicacion_las_disposiciones_establecidas_para_los_depositos_en_caja_de_51343a
    - [Operacion] Operacion_aplicacion_de_disposiciones_de_depositos_en_caja_de_ahorros__depaho_3_10_9_94a276
    - [Operacion] Operacion_aplicacion_de_disposiciones_de_depositos_en_caja_de_ahorros__depaho_3_12_5_6b47fa
'aplicacion de disposiciones depositos en caja de ahorros' (2 nodos):
    - [Obligacion] Obligacion_seran_de_aplicacion_las_disposiciones_establecidas_para_los_depositos_en_caja_de_a912ca
    - [Operacion] Operacion_aplicacion_de_disposiciones_depositos_en_caja_de_ahorros__depaho_4_22_4_e8e582
'aplicacion disposiciones depositos caja de ahorros' (2 nodos):
    - [Obligacion] Obligacion_cuando_no_se_encuentre_previsto_en_los_puntos_precedentes_y_en_la_medida_en_que__7835e8
    - [Operacion] Operacion_aplicacion_disposiciones_depositos_caja_de_ahorros__depaho_3_13_6_772fb6
'cabecera de archivo' (2 nodos):
    - [Definicion] Definicion_cabecera_de_archivo__registro_que_identifica_el_origen_inmediato_de_la_informaci_e5743e
    - [Operacion] Operacion_cabecera_de_archivo__snp_cheq_sbloque10_864be1
'cabecera de lote' (2 nodos):
    - [Definicion] Definicion_cabecera_de_lote__registro_que_identifica_la_entidad_de_origen_y_la_entidad_dest_58a0fc
    - [Operacion] Operacion_cabecera_de_lote__snp_cheq_sbloque10_84db78
'cajas de credito cooperativas' (2 nodos):
    - [Sujeto] Sujeto_caja_de_credito_cooperativa
    - [TextoOrdenado] TextoOrdenado_cajasc_pdf
'calculo de proporcion de exigencia' (2 nodos):
    - [Obligacion] Obligacion_determinar_la_proporcion_a_imputar_considerando_el_porcentaje_que_resulte_al_com_601160
    - [Operacion] Operacion_calculo_de_proporcion_de_exigencia__efemin_2_5_ed5d78
'camaras electronicas de compensacion (cec)' (2 nodos):
    - [Definicion] Definicion_camaras_electronicas_de_compensacion_cec__infraestructuras_que_trabajan_en_libre_106c70
    - [Sujeto] Sujeto_camara_electronica_de_compensacion
'cantidad de registros individuales y adicionales' (2 nodos):
    - [Definicion] Definicion_cantidad_de_registros_individuales_y_adicionales__campo_numerico_que_contiene_el_26a3eb
    - [Obligacion] Obligacion_el_campo_debe_contener_el_total_de_registros_individuales_y_adicionales_que_exis_a74f05
'cartera de negociacion' (2 nodos):
    - [Definicion] Definicion_cartera_de_negociacion__la_constituida_por_las_posiciones_en_instrumentos_que_ve_5aa1f0
    - [Operacion] Operacion_cartera_de_negociacion__lingeef_4_2_1_5_3c2c65
'compras debidamente documentadas' (2 nodos):
    - [Definicion] Definicion_compras_debidamente_documentadas__aquellas_que_cuenten_con_el_correspondiente_re_72047e
    - [Operacion] Operacion_compras_debidamente_documentadas__depaho_3_16_3_2_89f826
'cotejo de resultados con registros contables' (4 nodos):
    - [Obligacion] Obligacion_cotejar_los_resultados_del_arqueo_sorpresivo_con_los_registros_contables_y_o_la__8497a1
    - [Obligacion] Obligacion_cotejar_los_resultados_del_arqueo_sorpresivo_de_inversiones_con_los_registros_co_f59fa1
    - [Obligacion] Obligacion_cotejo_de_los_resultados_del_arqueo_sorpresivo_con_los_registros_contables_y_o_l_76c2ac
    - [Operacion] Operacion_cotejo_de_resultados_con_registros_contables__ri_ccna_d1a3l2_s9_856065
'determinacion libre de tasas de interes' (2 nodos):
    - [Operacion] Operacion_determinacion_libre_de_tasas_de_interes__depaho_1_9_1_4a66a8
    - [Potestad] Potestad_determinacion_libre_de_tasas_de_interes__las_tasas_de_interes_aplicables_se_dete_3e5504
'determinar naturaleza y alcance de procedimientos sustantivos' (2 nodos):
    - [Obligacion] Obligacion_el_auditor_interno_determinara_la_naturaleza_y_alcance_de_los_procedimientos_sus_1d8d89
    - [Potestad] Potestad_determinar_naturaleza_y_alcance_de_procedimientos_sustantivos__el_responsable_de_d44f4a
'diseno de indicadores de alerta temprana' (2 nodos):
    - [Obligacion] Obligacion_las_entidades_deben_disenar_un_conjunto_de_indicadores_que_les_permitan_identifi_f61243
    - [Operacion] Operacion_diseno_de_indicadores_de_alerta_temprana__lingeef_3_3_4_b9d8c7
'eliminacion del activo de deudas irrecuperables' (2 nodos):
    - [Obligacion] Obligacion_las_cajas_de_credito_cooperativas_deberan_eliminar_del_activo_las_deudas_de_clie_f11ee3
    - [Operacion] Operacion_eliminacion_del_activo_de_deudas_irrecuperables__cajasc_9_9_0f3f84
'escenarios de tecnologia e informacion integrados' (2 nodos):
    - [Condicion] Condicion_escenarios_de_tecnologia_e_informacion_integrados__los_escenarios_que_contemplen_a7e98f
    - [Obligacion] Obligacion_los_escenarios_que_contemplan_tecnologia_y_seguridad_de_la_informacion_deberan_c_1baae9
'establecer acuerdos, procedimientos y elementos de seguridad' (3 nodos):
    - [Obligacion] Obligacion_establecer_los_acuerdos_procedimientos_y_elementos_de_seguridad_que_impidan_inst_d7f159
    - [Obligacion] Obligacion_establecer_y_o_aplicar_los_acuerdos_procedimientos_y_elementos_de_seguridad_que__ca1675
    - [Operacion] Operacion_establecer_acuerdos_procedimientos_y_elementos_de_seguridad__snp_cheq_8_4_4_1_f5ee29
'exclusion del registro de auditores' (2 nodos):
    - [Operacion] Operacion_exclusion_del_registro_de_auditores__ri_ccna_d1a1_5_3_839e29
    - [Restriccion] Restriccion_el_auditor_externo_no_debe_haber_sido_excluido_por_la_superintendencia_de_entida_dd3668
'exclusion por sanciones pecuniarias impagadas' (2 nodos):
    - [Obligacion] Obligacion_corresponde_la_exclusion_del_socio_responsable_designado_del_registro_de_auditor_69c7fd
    - [Restriccion] Restriccion_el_auditor_externo_sera_excluido_del_registro_de_auditores_cuando_las_sanciones__34deaa
'exposicion de saldo acreedor en utilidades diversas' (2 nodos):
    - [Obligacion] Obligacion_exponer_el_saldo_acreedor_al_cierre_de_cada_periodo_mensual_en_utilidades_divers_ba3911
    - [Operacion] Operacion_exposicion_de_saldo_acreedor_en_utilidades_diversas__ri_dcpc_3_6_2_26162f
'fondos de seguridad con efecto iris' (8 nodos):
    - [Definicion] Definicion_fondos_de_seguridad_con_efecto_iris__elemento_de_seguridad_impreso_en_el_anverso_0322cc
    - [Operacion] Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_12_3_3a51d4
    - [Operacion] Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_14_3_1c6f96
    - [Operacion] Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_15_3_d06c9a
    - [Operacion] Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_18_3_fc5341
    - [Operacion] Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_19_3_5f90fe
    - [Operacion] Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_20_3_bbb5e3
    - [Operacion] Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_21_3_c9296b
'gestion del riesgo de mercado' (2 nodos):
    - [Definicion] Definicion_gestion_del_riesgo_de_mercado__proceso_de_identificacion_evaluacion_seguimiento__36b645
    - [Operacion] Operacion_gestion_del_riesgo_de_mercado__lingeef_4_1_3_1_5b69bb
'gestion del riesgo operacional' (3 nodos):
    - [Definicion] Definicion_gestion_del_riesgo_operacional__la_identificacion_evaluacion_seguimiento_control_433d6d
    - [Operacion] Operacion_gestion_del_riesgo_operacional__lingeef_6_2_4_6_5722a0
    - [Operacion] Operacion_gestion_del_riesgo_operacional__lingeef_6_3_8b6034
'identificacion para personas con ceguera' (3 nodos):
    - [Definicion] Definicion_identificacion_para_personas_con_ceguera__codigo_con_relieve_perceptible_al_tact_b6f000
    - [Operacion] Operacion_identificacion_para_personas_con_ceguera__cirmo3_1_2_20_3_c4395f
    - [Operacion] Operacion_identificacion_para_personas_con_ceguera__cirmo3_1_2_21_3_7114d8
'imagen latente' (2 nodos):
    - [Definicion] Definicion_imagen_latente__motivo_ornamental_situado_en_el_angulo_inferior_derecho_dentro_d_b4d3eb
    - [Operacion] Operacion_imagen_latente__cirmo3_1_2_20_3_8181da
'impresion calcografica' (2 nodos):
    - [Definicion] Definicion_impresion_calcografica__aplicada_en_el_retrato_de_juan_bautista_alberdi_textos_v_0c9c48
    - [Operacion] Operacion_impresion_calcografica__cirmo3_1_2_20_3_cd3eec
'infraestructuras de mercado financiero sistemicamente importantes' (2 nodos):
    - [Definicion] Definicion_infraestructuras_de_mercado_financiero_sistemicamente_importantes__las_infraestr_dc82b1
    - [Sujeto] Sujeto_propuesto_infraestructuras_de_mercado_financiero_sistemicamente_importantes
'liquidacion de intereses por periodos vencidos' (2 nodos):
    - [Obligacion] Obligacion_los_intereses_deben_liquidarse_por_periodos_vencidos_y_acreditarse_en_la_cuenta__ee2832
    - [Operacion] Operacion_liquidacion_de_intereses_por_periodos_vencidos__depaho_3_4_7_1_51291e
'marco adecuado para gestion del riesgo de credito' (2 nodos):
    - [Definicion] Definicion_marco_adecuado_para_gestion_del_riesgo_de_credito__marco_que_es_eficaz_viable_y__621704
    - [Obligacion] Obligacion_el_directorio_debe_asegurar_que_la_entidad_financiera_cuente_con_un_marco_adecua_be0a44
'marco contable' (2 nodos):
    - [Definicion] Definicion_marco_contable__el_marco_contable_mencionado_en_el_capitulo_1_que_fija_los_termi_1142a7
    - [TextoOrdenado] TextoOrdenado_ri_dcpc_pdf
'motivo de complementacion frente-dorso' (6 nodos):
    - [Definicion] Definicion_motivo_de_complementacion_frente_dorso__motivo_parcial_de_la_denominacion_20_000_288f8e
    - [Operacion] Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_12_3_bb0258
    - [Operacion] Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_18_3_5670ff
    - [Operacion] Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_19_3_739142
    - [Operacion] Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_20_3_4b35d9
    - [Operacion] Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_21_3_f48c2c
'multiples acreditaciones permitidas' (2 nodos):
    - [Excepcion] Excepcion_se_permite_mas_de_una_acreditacion_por_los_conceptos_de_repatriacion_de_fondos___76fa3f
    - [Potestad] Potestad_multiples_acreditaciones_permitidas__se_permite_mas_de_una_acreditacion_por_los__3d3efc
'no emision de comprobante por cajero' (2 nodos):
    - [Condicion] Condicion_no_emision_de_comprobante_por_cajero__el_supuesto_en_que_el_cajero_automatico_no_986d00
    - [Operacion] Operacion_no_emision_de_comprobante_por_cajero__depaho_4_3_2_9_6a31ae
'no registrar incumplimientos capital minimo' (2 nodos):
    - [Condicion] Condicion_no_registrar_incumplimientos_capital_minimo__no_registrar_incumplimientos_en_la__a21a50
    - [Restriccion] Restriccion_las_entidades_financieras_no_deberan_registrar_incumplimientos_en_la_integracion_e619e9
'numeracion horizontal — reverso' (3 nodos):
    - [Definicion] Definicion_numeracion_horizontal_reverso__en_el_angulo_superior_derecho_en_tinta_negra_con__2b55a5
    - [Operacion] Operacion_numeracion_horizontal_reverso__cirmo3_1_2_16_3_9261a3
    - [Operacion] Operacion_numeracion_horizontal_reverso__cirmo3_1_2_17_3_9f8fdb
'numeracion vertical — reverso' (3 nodos):
    - [Definicion] Definicion_numeracion_vertical_reverso__sobre_margen_izquierdo_en_color_rojo_con_luminosida_3f88a1
    - [Operacion] Operacion_numeracion_vertical_reverso__cirmo3_1_2_16_3_e60396
    - [Operacion] Operacion_numeracion_vertical_reverso__cirmo3_1_2_17_3_14cbbe
'otorgamiento de financiaciones a clientes mipyme' (2 nodos):
    - [Obligacion] Obligacion_las_financiaciones_comprendidas_en_el_cupo_mipyme_minimo_deberan_ser_otorgadas_a_cb0e6d
    - [Operacion] Operacion_otorgamiento_de_financiaciones_a_clientes_mipyme__efemin_6_3_044a85
'otorgamiento de prestamos hipotecarios en pesos' (2 nodos):
    - [Obligacion] Obligacion_deber_de_otorgar_los_prestamos_hipotecarios_en_moneda_pesos__manori_1_1_5_2_7d5b35
    - [Operacion] Operacion_otorgamiento_de_prestamos_hipotecarios_en_pesos__manori_1_1_5_2_570cf4
'plan de fondeo para contingencias' (2 nodos):
    - [Definicion] Definicion_plan_de_fondeo_para_contingencias__compilacion_de_politicas_procedimientos_y_acc_3de75e
    - [Operacion] Operacion_plan_de_fondeo_para_contingencias__lingeef_3_3_11_35c1f2
'presentacion anual de declaraciones juradas sobre parentesco' (2 nodos):
    - [Obligacion] Obligacion_las_entidades_financieras_deberan_requerir_la_presentacion_anual_de_declaracione_b3fcbf
    - [Operacion] Operacion_presentacion_anual_de_declaraciones_juradas_sobre_parentesco__ayccef_7_3_1_1_588ede
'presentacion constancia cuil — empleados dependencia' (2 nodos):
    - [Obligacion] Obligacion_los_solicitantes_empleados_en_relacion_de_dependencia_deberan_presentar_constanc_2b5743
    - [Operacion] Operacion_presentacion_constancia_cuil_empleados_dependencia__manori_1_2_2_2_f28e80
'presentacion constancia situacion impositiva — autonomos y monotributistas' (2 nodos):
    - [Obligacion] Obligacion_los_solicitantes_trabajadores_autonomos_y_monotributistas_deberan_presentar_cons_7310d8
    - [Operacion] Operacion_presentacion_constancia_situacion_impositiva_autonomos_y_monotributistas__manori_a5c834
'presentacion de ajustes a cheques compensados' (2 nodos):
    - [Obligacion] Obligacion_en_sesion_de_presentados_las_entidades_deberan_presentar_los_eventuales_ajustes__b60e8d
    - [Operacion] Operacion_presentacion_de_ajustes_a_cheques_compensados__snp_cheq_3_1_1_1_da9df1
'presentacion de billetes falsos al bcra' (2 nodos):
    - [Obligacion] Obligacion_las_entidades_financieras_deben_presentar_al_bcra_billetes_presumiblemente_falso_988ff4
    - [Operacion] Operacion_presentacion_de_billetes_falsos_al_bcra__cirmo3_4_1_2_f69687
'presentacion de declaracion jurada sobre antecedentes' (2 nodos):
    - [Obligacion] Obligacion_presentacion_de_declaracion_jurada_sobre_antecedentes_personales_y_penales_de_la_eefe4f
    - [Operacion] Operacion_presentacion_de_declaracion_jurada_sobre_antecedentes__ayccef_2_4_7_6_8f6979
'presentacion de declaraciones juradas' (2 nodos):
    - [Obligacion] Obligacion_las_entidades_financieras_deben_presentar_declaraciones_juradas_sobre_personas_v_707819
    - [Operacion] Operacion_presentacion_de_declaraciones_juradas__ayccef_7_1_2_1_bb70af
'presentacion de rechazos de entidades giradas' (2 nodos):
    - [Obligacion] Obligacion_en_sesion_de_rechazados_las_entidades_deberan_presentar_rechazos_de_las_entidade_154c40
    - [Operacion] Operacion_presentacion_de_rechazos_de_entidades_giradas__snp_cheq_3_1_1_1_9227d9
'presentacion de rechazos de reclamos' (2 nodos):
    - [Obligacion] Obligacion_en_sesion_de_rechazados_las_entidades_deberan_presentar_rechazos_de_reclamos_sob_3d3d61
    - [Operacion] Operacion_presentacion_de_rechazos_de_reclamos__snp_cheq_3_1_1_1_508d96
'presentacion de rechazos fuera de canje' (2 nodos):
    - [Obligacion] Obligacion_en_sesion_de_presentados_las_entidades_deberan_presentar_rechazos_fuera_de_canje_3fe871
    - [Operacion] Operacion_presentacion_de_rechazos_fuera_de_canje__snp_cheq_3_1_1_1_e5e856
'presentacion de rechazos por defectos verificables' (2 nodos):
    - [Obligacion] Obligacion_en_sesion_de_rechazados_las_entidades_deberan_presentar_rechazos_por_defectos_ve_5b408b
    - [Operacion] Operacion_presentacion_de_rechazos_por_defectos_verificables__snp_cheq_3_1_1_1_cc19a4
'presentacion de respuestas de rechazos fuera de canje' (2 nodos):
    - [Obligacion] Obligacion_en_sesion_de_rechazados_las_entidades_deberan_presentar_respuestas_de_rechazos_f_b00ff2
    - [Operacion] Operacion_presentacion_de_respuestas_de_rechazos_fuera_de_canje__snp_cheq_3_1_1_1_6eb194
'presentacion de solicitud de autorizacion' (4 nodos):
    - [Obligacion] Obligacion_la_solicitud_de_autorizacion_debera_ser_interpuesta_a_traves_del_correspondiente_1477c1
    - [Obligacion] Obligacion_la_solicitud_de_autorizacion_debera_ser_interpuesta_mediante_nota_acompanada_de__adfcaa
    - [Obligacion] Obligacion_las_entidades_que_se_fusionan_para_constituir_una_nueva_entidad_o_la_entidad_abs_ec1299
    - [Operacion] Operacion_presentacion_de_solicitud_de_autorizacion__cajasc_1_2_4_bc5097
'presentacion detalle aportes jubilatorios — autonomos y monotributistas' (2 nodos):
    - [Obligacion] Obligacion_los_solicitantes_trabajadores_autonomos_y_monotributistas_deberan_presentar_deta_7ee525
    - [Operacion] Operacion_presentacion_detalle_aportes_jubilatorios_autonomos_y_monotributistas__manori_1__8806a5
'presentacion detalle aportes monotributo — autonomos y monotributistas' (2 nodos):
    - [Obligacion] Obligacion_los_solicitantes_trabajadores_autonomos_y_monotributistas_deberan_presentar_deta_17fa2e
    - [Operacion] Operacion_presentacion_detalle_aportes_monotributo_autonomos_y_monotributistas__manori_1_2_178ef9
'presentacion documentacion laboral — empleados dependencia' (2 nodos):
    - [Obligacion] Obligacion_los_solicitantes_empleados_en_relacion_de_dependencia_deberan_presentar_copia_de_f64cf7
    - [Operacion] Operacion_presentacion_documentacion_laboral_empleados_dependencia__manori_1_2_2_2_40f363
'presuncion de conformidad con movimiento' (2 nodos):
    - [Operacion] Operacion_presuncion_de_conformidad_con_movimiento__depaho_3_4_10_470e43
    - [Potestad] Potestad_presuncion_de_conformidad_con_movimiento__se_presume_conformidad_de_la_administr_b036a3
'procedimiento de excepcion por falla en comunicaciones' (2 nodos):
    - [Definicion] Definicion_procedimiento_de_excepcion_por_falla_en_comunicaciones__procedimiento_basado_en__6501a8
    - [Operacion] Operacion_procedimiento_de_excepcion_por_falla_en_comunicaciones__snp_cheq_3_1_4_3_c530f6
'provision de talon en cajeros automaticos' (2 nodos):
    - [Obligacion] Obligacion_el_sistema_de_cajeros_automaticos_debe_permitir_la_provision_de_un_talon_que_mue_c922fb
    - [Operacion] Operacion_provision_de_talon_en_cajeros_automaticos__depaho_2_5_dab642
'puesta en circulacion de monedas conmemorativas' (2 nodos):
    - [Obligacion] Obligacion_el_bcra_en_su_caracter_de_ente_emisor_pone_en_circulacion_las_monedas_conmemorat_32ab28
    - [Operacion] Operacion_puesta_en_circulacion_de_monedas_conmemorativas__cirmo3_s7_1c7743
'puesta en circulacion monedas conmemorativas' (2 nodos):
    - [Obligacion] Obligacion_el_bcra_pone_en_circulacion_la_moneda_conmemorativa_del_80_aniversario_de_la_cre_7fec63
    - [Operacion] Operacion_puesta_en_circulacion_monedas_conmemorativas__cirmo3_s7_80016a
'recepcion de archivos de compensacion' (5 nodos):
    - [Obligacion] Obligacion_todas_las_entidades_participantes_recibiran_de_la_cec_los_archivos_con_el_detall_9c7d5f
    - [Operacion] Operacion_recepcion_de_archivos_de_compensacion__snp_cheq_3_1_3_1_a85708
    - [Operacion] Operacion_recepcion_de_archivos_de_compensacion__snp_cheq_3_1_3_2_5ef8b1
    - [Operacion] Operacion_recepcion_de_archivos_de_compensacion__snp_tr_1_3_4_1_32e6b8
    - [Operacion] Operacion_recepcion_de_archivos_de_compensacion__snp_tr_1_3_4_2_8f4b1d
'recepcion de informacion por entidades depositarias' (2 nodos):
    - [Obligacion] Obligacion_las_entidades_depositarias_recibiran_la_informacion_resultante_de_la_sesion_de_r_84d412
    - [Operacion] Operacion_recepcion_de_informacion_por_entidades_depositarias__snp_cheq_3_1_3_1_dcb449
'recepcion de informacion por entidades giradas' (2 nodos):
    - [Obligacion] Obligacion_las_entidades_giradas_seran_las_receptoras_de_la_informacion_resultante_de_la_co_6d7fa1
    - [Operacion] Operacion_recepcion_de_informacion_por_entidades_giradas__snp_cheq_3_1_3_1_1de284
'recepcion de rechazos por entidad girada' (2 nodos):
    - [Obligacion] Obligacion_la_entidad_girada_debe_recibir_de_la_cec_el_archivo_con_la_informacion_de_rechaz_a91921
    - [Operacion] Operacion_recepcion_de_rechazos_por_entidad_girada__snp_cheq_3_6_4_1_6_1298f4
'rechazo de entidad depositaria' (3 nodos):
    - [Definicion] Definicion_rechazo_de_entidad_depositaria__rechazos_que_la_entidad_depositaria_realiza_cuan_1dc813
    - [Operacion] Operacion_rechazo_de_entidad_depositaria__snp_cheq_7_1_3_e8c633
    - [Operacion] Operacion_rechazo_de_entidad_depositaria__snp_cheq_7_1_9_c784f3
'registro individual de transacciones' (2 nodos):
    - [Definicion] Definicion_registro_individual_de_transacciones__contiene_la_informacion_necesaria_para_env_55e443
    - [Operacion] Operacion_registro_individual_de_transacciones__snp_cheq_sbloque10_0bc698
'repeticion de saldo en dias sin movimiento' (2 nodos):
    - [Obligacion] Obligacion_en_los_dias_en_que_no_se_registre_movimiento_debera_repetirse_el_saldo_correspon_5bfdcc
    - [Operacion] Operacion_repeticion_de_saldo_en_dias_sin_movimiento__efemin_2_2_a77601
'retencion de tarjeta por cajero' (2 nodos):
    - [Condicion] Condicion_retencion_de_tarjeta_por_cajero__el_supuesto_en_que_el_cajero_automatico_retiene_9b86b2
    - [Operacion] Operacion_retencion_de_tarjeta_por_cajero__depaho_4_3_2_9_797a43
'sector privado no financiero' (2 nodos):
    - [Definicion] Definicion_sector_privado_no_financiero__esta_constituido_por_las_sociedades_comerciales_no_cb759c
    - [Sujeto] Sujeto_sector_privado_no_financiero
'sector publico no financiero' (2 nodos):
    - [Definicion] Definicion_sector_publico_no_financiero__esta_constituido_por_los_gobiernos_nacional_provin_9a3841
    - [Sujeto] Sujeto_sector_publico_no_financiero
'separacion fisica de anexos al legajo' (4 nodos):
    - [Condicion] Condicion_separacion_fisica_de_anexos_al_legajo__los_anexos_al_legajo_del_cliente_pueden_e_cf2736
    - [Excepcion] Excepcion_excepcion_a_la_exigencia_de_que_la_carpeta_legal_este_anexa_al_legajo_del_client_d82671
    - [Excepcion] Excepcion_los_anexos_al_legajo_del_cliente_pueden_estar_separados_fisicamente_si_se_cumple_03e726
    - [Excepcion] Excepcion_los_anexos_al_legajo_del_cliente_pueden_estar_separados_fisicamente_siempre_que__3ea131
'sin limite de adhesiones — pago por canales electronicos' (2 nodos):
    - [Excepcion] Excepcion_no_hay_limite_en_la_cantidad_de_adhesiones_al_sistema_de_debito_automatico_para__910da6
    - [Restriccion] Restriccion_no_hay_limite_en_la_cantidad_de_adhesiones_a_servicios_de_pago_por_canales_elect_eaca1f
'tenencia de certificado de aptitud' (4 nodos):
    - [Obligacion] Obligacion_cumplimiento_de_la_medida_de_tenencia_de_certificado_de_aptitud_en_cajas_de_aten_33fb0a
    - [Obligacion] Obligacion_informar_sobre_la_tenencia_de_certificado_de_aptitud_como_medida_minima_de_segur_cfde6f
    - [Obligacion] Obligacion_se_informara_el_cumplimiento_de_la_tenencia_de_certificado_de_aptitud_en_recinto_188761
    - [Operacion] Operacion_tenencia_de_certificado_de_aptitud__ri_mmsef_2_2_8_3_2_0589ab
'tinta de variabilidad optica' (6 nodos):
    - [Definicion] Definicion_tinta_de_variabilidad_optica__imagen_simbolica_de_la_constitucion_nacional_ubica_fb90b8
    - [Operacion] Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_14_3_51c1f2
    - [Operacion] Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_15_3_58046e
    - [Operacion] Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_19_3_d9a9bc
    - [Operacion] Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_20_3_7ae288
    - [Operacion] Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_21_3_f460f4
'tomar recaudos operativos para estandares de performance y disponibilidad' (2 nodos):
    - [Obligacion] Obligacion_tomar_los_recaudos_operativos_necesarios_para_alcanzar_los_estandares_requeridos_975a34
    - [Operacion] Operacion_tomar_recaudos_operativos_para_estandares_de_performance_y_disponibilidad__snp_t_7021b4
'transmision de imagenes a entidades giradas' (2 nodos):
    - [Obligacion] Obligacion_la_cec_transmitira_las_imagenes_de_cheques_rechazados_a_las_entidades_giradas__s_0faa4d
    - [Operacion] Operacion_transmision_de_imagenes_a_entidades_giradas__snp_cheq_3_2_8_210657
'truncamiento de cheques' (3 nodos):
    - [Definicion] Definicion_truncamiento_de_cheques__omision_del_traslado_y_entrega_de_la_totalidad_de_los_c_da1d1d
    - [Operacion] Operacion_truncamiento_de_cheques__snp_cheq_2_1_0eea74
    - [Operacion] Operacion_truncamiento_de_cheques__snp_cheq_s4_db4792
'utilizacion de multiples centros de transmision' (2 nodos):
    - [Condicion] Condicion_utilizacion_de_multiples_centros_de_transmision__la_entidad_utiliza_mas_de_un_ce_92ecac
    - [Potestad] Potestad_utilizacion_de_multiples_centros_de_transmision__facultad_de_cada_entidad_de_uti_7fdcc9
'valuacion prudente de instrumentos financieros' (2 nodos):
    - [Obligacion] Obligacion_la_entidad_debe_realizar_una_valuacion_prudente_de_los_instrumentos_financieros__5a44a6
    - [Operacion] Operacion_valuacion_prudente_de_instrumentos_financieros__lingeef_4_1_2_3_280a3e
'verificacion de que no es banco pantalla' (2 nodos):
    - [Condicion] Condicion_verificacion_de_que_no_es_banco_pantalla__condicion_de_que_la_entidad_solicitant_8097d4
    - [Operacion] Operacion_verificacion_de_que_no_es_banco_pantalla__ayccef_5_1_5_946069
```

### S9 — PASS

ERROR — Descripción canónica: ningún nodo tiene a la vez 'descripcion' y 'description'.

**Resultado:** 0 nodos con ambas keys.

```
Tabla por type (usa cada key / ambas / ninguna):
  Comunicacion: descripcion=0, description=0, ambas=0, ninguna=142 (total 142)
  Condicion: descripcion=1401, description=0, ambas=0, ninguna=0 (total 1401)
  Definicion: descripcion=1557, description=0, ambas=0, ninguna=0 (total 1557)
  Excepcion: descripcion=241, description=0, ambas=0, ninguna=0 (total 241)
  Obligacion: descripcion=4717, description=0, ambas=0, ninguna=34 (total 4751)
  Operacion: descripcion=2525, description=0, ambas=0, ninguna=0 (total 2525)
  Potestad: descripcion=511, description=0, ambas=0, ninguna=0 (total 511)
  Restriccion: descripcion=914, description=0, ambas=0, ninguna=0 (total 914)
  Sujeto: descripcion=0, description=0, ambas=0, ninguna=390 (total 390)
  TextoOrdenado: descripcion=0, description=0, ambas=0, ninguna=20 (total 20)

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

**Resultado:** Sin aplica_a: Excepcion=228, Obligacion=1427, Operacion=2356, Potestad=251, Restriccion=564 (total 4826).

```
Excepcion: 228 sin aplica_a
    - Excepcion_alternativamente_podra_utilizarse_el_capital_minimo_basico_partida_70700000_cuan_044301
    - Excepcion_cuando_exista_mas_de_un_solicitante_se_puede_optar_por_asegurar_a_cada_solicitan_723d3e
    - Excepcion_cuando_exista_mas_de_un_solicitante_se_puede_optar_por_asegurar_al_menos_a_uno_d_46e208
    - Excepcion_cuando_existe_saldo_acreedor_en_otros_resultados_integrales_acumulados_revaluaci_c564a3
    - Excepcion_cuando_la_actuacion_del_auditor_interino_no_exceda_de_un_ano_no_se_computa_a_los_c73c6e
    - Excepcion_cuando_la_auditoria_interna_se_delega_a_profesionales_independientes_el_responsa_ebf048
    - Excepcion_cuando_la_casa_matriz_y_todas_las_sucursales_esten_en_localidades_con_hasta_dos__0556d2
    - Excepcion_cuando_la_cuenta_se_cierra_por_decision_del_titular_la_entidad_no_esta_obligada__8aafff
    - Excepcion_cuando_la_persona_humana_adquirente_o_aportante_no_sea_sujeto_obligado_a_los_imp_26939d
    - Excepcion_cuando_los_cambios_signifiquen_disminuciones_en_las_comisiones_o_gastos_los_nuev_0efa42
    - Excepcion_cuando_los_datos_observados_no_sean_relevantes_liquidacion_forzada_o_ausencia_de_9f33cf
    - Excepcion_cuando_los_sujetos_obligados_al_pago_sean_prestatarios_de_la_caja_de_credito_la__abd086
    - Excepcion_cuando_no_se_disponga_de_la_calificacion_camels_de_la_sefyc_el_indice_de_correcc_960986
    - Excepcion_cuando_se_ha_designado_un_representante_legal_la_entrega_de_la_tarjeta_de_debito_8dec92
    - Excepcion_despues_de_cumplido_el_plazo_de_1_ano_el_reclamo_sera_admitido_a_traves_del_sist_39702c
    - Excepcion_el_criterio_de_consideracion_del_plazo_residual_no_aplica_cuando_el_banco_del_ex_c8b88d
    - Excepcion_el_dictamen_favorable_puede_incluir_salvedades_o_excepciones_cuando_se_trate_de__1c3930
    - Excepcion_el_envio_al_domicilio_no_aplica_si_el_titular_formula_expresamente_una_opcion_en_a85de6
    - Excepcion_el_financiamiento_adicional_es_independiente_de_la_asistencia_en_operaciones_tot_7463d9
    - Excepcion_el_incremento_del_25_no_se_aplica_a_cajas_de_credito_cooperativas_en_categoria_i_1863fd
    - Excepcion_el_legajo_del_cliente_puede_encontrarse_en_un_lugar_distinto_del_de_radicacion_d_8ae155
    - Excepcion_el_limite_de_acreditaciones_puede_ser_incrementado_cuando_existe_autorizacion_ex_5c9be4
    - Excepcion_el_limite_del_5_de_la_responsabilidad_patrimonial_computable_no_se_observara_cua_2260c8
    - Excepcion_el_limite_previsto_en_el_punto_3_10_3_no_aplica_a_los_creditos_asociados_al_cobr_7afe59
    - Excepcion_el_limite_previsto_en_el_punto_3_10_3_no_aplica_a_los_creditos_por_cobro_de_depo_0eb5c3
    - Excepcion_el_plan_de_cuentas_no_es_de_aplicacion_obligatoria_para_las_filiales_operativas__fbf0cd
    - Excepcion_el_plazo_de_devolucion_de_24_horas_puede_excederse_cuando_la_devolucion_sea_soli_424234
    - Excepcion_el_requerimiento_de_elaboracion_y_presentacion_de_estados_financieros_consolidad_cab2bc
    - Excepcion_el_requisito_de_constancia_de_inscripcion_puede_ser_suplido_por_una_declaracion__268200
    - Excepcion_el_requisito_de_informe_comercial_o_crediticio_no_aplica_cuando_la_entidad_dispo_5a58f1
    - Excepcion_el_requisito_de_informe_comercial_o_crediticio_no_aplica_para_prestamos_otorgado_e5836c
    - Excepcion_el_requisito_de_requerir_un_informe_comercial_o_crediticio_puede_ser_exceptuado__f12283
    - Excepcion_el_superintendente_puede_determinar_excepciones_al_plazo_de_120_dias_para_la_pre_93eec3
    - Excepcion_el_valor_facial_diferenciado_en_el_reverso_constituye_una_excepcion_al_diseno_id_219902
    - Excepcion_en_caso_de_destrucciones_parciales_se_puede_aceptar_que_la_indemnizacion_sea_des_e9a22c
    - Excepcion_en_caso_de_resultar_el_acreedor_o_sus_cesionarios_adquirentes_en_subasta_quedara_1388c6
    - Excepcion_en_defecto_de_testimonio_notarial_los_firmantes_deberan_acreditar_la_representat_e25ff1
    - Excepcion_en_depositos_a_plazo_fijo_de_uva_y_uvi_queda_excluido_del_computo_el_importe_dev_2a1095
    - Excepcion_en_fusiones_que_no_deriven_en_constitucion_de_nueva_sociedad_la_inscripcion_podr_fa26ac
    - Excepcion_en_sucursales_de_entidades_financieras_extranjeras_el_comite_se_integra_con_dos__448935
    - Excepcion_excepcion_a_la_acreditacion_preferente_mediante_cargos_directivos_la_experiencia_c847bd
    - Excepcion_excepcion_a_la_aplicacion_de_la_tasa_de_encaje_del_mes_anterior_para_depositos_e_c7e2d6
    - Excepcion_excepcion_a_la_ausencia_de_limites_de_importe_en_extracciones_por_cajeros_automa_293e37
    - Excepcion_excepcion_a_la_exigencia_de_que_la_carpeta_legal_este_anexa_al_legajo_del_client_d82671
    - Excepcion_excepcion_a_la_prohibicion_de_acceso_a_nuevas_operaciones_de_descuento_el_cedent_edee4f
    - Excepcion_excepcion_a_la_prohibicion_de_declarar_excedentes_cuando_se_hayan_recuperado_fon_e2b003
    - Excepcion_excepcion_a_la_prohibicion_de_desafectacion_cuando_este_cubierto_el_100_de_las_a_3af56d
    - Excepcion_excepcion_a_la_prohibicion_de_generar_utilidades_cuando_se_constituyan_prevision_48457c
    - Excepcion_excepcion_a_la_restriccion_de_tenencia_de_cuotapartes_se_exceptuan_las_cuotapart_2b586b
    - Excepcion_excepcion_a_la_restriccion_de_tenencia_de_cuotapartes_se_exceptuan_las_cuotapart_5d97d6
    - Excepcion_excepcion_a_la_restriccion_de_tenencia_de_cuotapartes_se_exceptuan_las_cuotapart_7113e0
    - Excepcion_excepcion_a_la_restriccion_de_tenencia_de_cuotapartes_se_exceptuan_las_cuotapart_7518a9
    - Excepcion_excepcion_a_la_restriccion_de_tenencia_de_cuotapartes_se_exceptuan_las_cuotapart_ea48e9
    - Excepcion_excepcion_al_deber_de_obtener_constancias_de_cuit_cdi_y_cuil_las_entidades_puede_7c89fa
    - Excepcion_excepcion_al_limite_de_6_meses_cuando_se_establezca_un_plazo_distinto__cajasc_5__04512f
    - Excepcion_excepcion_al_limite_del_5_de_responsabilidad_patrimonial_computable_no_se_observ_a2578c
    - Excepcion_excepcion_al_plazo_minimo_de_30_dias_se_admiten_pases_a_plazos_inferiores_o_canc_bd1b6b
    - Excepcion_exclusion_de_facturas_no_ingresadas_a_la_compensacion_por_haber_sido_emitidas_en_3b9c74
    - Excepcion_exclusion_de_facturas_no_ingresadas_a_la_compensacion_por_haber_sido_pagadas_pre_e075d5
    - Excepcion_exclusion_de_facturas_no_ingresadas_a_la_compensacion_por_no_tener_declarada_una_d52f84
    - Excepcion_financiaciones_excluidas_del_computo_del_cupo_mipyme_minimo__efemin_6_3_2ba505
    - Excepcion_fuera_de_los_casos_enumerados_en_los_items_siguientes_no_es_exigible_que_el_lega_736398
    - Excepcion_inhabilidad_de_personas_inhabilitadas_por_el_inciso_5_del_articulo_41_de_la_ley__42c80b
    - Excepcion_la_aceptacion_de_informaciones_del_sistema_de_almacenamiento_no_aplica_cuando_ex_2f592c
    - Excepcion_la_agencia_complementaria_puede_acceder_a_los_movimientos_y_o_saldos_de_las_cuen_70e668
    - Excepcion_la_apertura_de_cuentas_especiales_de_regularizacion_de_activos_en_una_moneda_ext_4c0031
    - Excepcion_la_apertura_de_la_cuenta_no_se_condiciona_a_que_el_trabajador_posea_la_credencia_a8a0be
    - Excepcion_la_autorizacion_conferida_a_un_menor_para_operar_la_cuenta_cesa_automaticamente__bad087
    - Excepcion_la_autorizacion_no_implica_compromiso_alguno_para_aprobar_futuros_requerimientos_a61480
    - Excepcion_la_comunicacion_de_rechazados_que_no_sea_enviada_en_la_sesion_correspondiente_pu_44d303
    - Excepcion_la_comunicacion_de_resultados_de_auditorias_a_la_alta_gerencia_no_aplica_cuando__743a0c
    - Excepcion_la_conformidad_otorgada_es_condicional_y_sujeta_al_resultado_de_la_posterior_ver_d31636
    - Excepcion_la_cuenta_de_acreditacion_puede_pertenecer_a_una_entidad_financiera_distinta_de__e2175e
    - Excepcion_la_cuenta_se_abre_incluso_cuando_el_trabajador_no_posee_credencial_de_registro_l_ee1a47
    - Excepcion_la_debida_diligencia_especial_al_inicio_de_la_relacion_comercial_no_exime_del_de_6742b4
    - Excepcion_la_deduccion_se_amplia_hasta_el_6_cuando_se_trata_de_financiaciones_acordadas_a__c12774
    - Excepcion_la_entrega_a_cualquiera_de_los_titulares_procede_incluso_en_caso_de_fallecimient_320cfc
    - Excepcion_la_evaluacion_de_la_capacidad_de_pago_incorporada_en_los_metodos_especificos_de__97c8a4
    - Excepcion_la_excepcion_a_la_obligacion_de_entrega_se_aplica_en_los_casos_de_cheque_falsifi_e3d634
    - Excepcion_la_excepcion_de_informacion_sobre_empresas_vinculadas_a_tenedores_del_5_o_mas_ap_8032fb
    - Excepcion_la_exclusion_del_registro_no_aplica_cuando_se_solicitan_facilidades_para_la_canc_50e56f
    - Excepcion_la_exclusion_del_socio_responsable_del_registro_de_auditores_no_sera_computable__2e1807
    - Excepcion_la_exclusion_no_aplica_cuando_se_solicitan_facilidades_para_la_cancelacion_de_la_752e2a
    - Excepcion_la_exclusion_no_aplica_cuando_se_soliciten_facilidades_para_la_cancelacion_de_la_76b670
    - Excepcion_la_exigencia_de_capital_por_riesgo_de_mercado_no_se_aplica_a_las_cajas_de_credit_2a7902
    - Excepcion_la_informacion_laboral_no_sera_obligatoria_cuando_los_prestamos_se_otorguen_medi_06656a
    - Excepcion_la_informacion_podra_ser_agregada_cuando_la_entidad_pueda_demostrar_que_puede_tr_117fcd
    - Excepcion_la_limitacion_del_20_del_valor_nominal_a_un_mismo_sujeto_obligado_al_pago_no_ser_9978a9
    - Excepcion_la_maxima_posicion_neta_negativa_de_la_cuenta_puede_calcularse_luego_del_cierre__f5d8fa
    - Excepcion_la_obligacion_de_permanecer_en_la_categoria_irrecuperable_por_180_dias_aplica_in_a997f5
    - Excepcion_la_prohibicion_de_autorizacion_no_impide_la_adopcion_de_otras_medidas_conforme_a_ff91e7
    - Excepcion_la_reposicion_por_el_bcra_solo_procede_en_los_casos_mencionados_precedentemente__3c3adb
    - Excepcion_la_responsabilidad_del_responsable_del_control_interno_por_incumplimientos_a_las_f22d97
    - Excepcion_la_restriccion_al_crecimiento_de_depositos_se_levanta_sujeto_a_la_resolucion_que_bbed17
    - Excepcion_la_sefyc_puede_prescindir_del_requisito_de_documentacion_sobre_regulaciones_de_l_149248
    - Excepcion_la_verificacion_de_comprobacion_de_ingresos_computables_queda_a_opcion_de_la_ent_0b5f18
    - Excepcion_las_actividades_que_involucren_atencion_de_clientes_y_publico_en_general_quedan__afcd2c
    - Excepcion_las_disposiciones_de_estas_normas_no_se_aplican_a_las_operaciones_de_pases_que_l_ad04cb
    - Excepcion_las_disposiciones_sobre_cierre_de_cuentas_no_operativas_no_aplican_a_operaciones_f19238
    - Excepcion_las_entidades_que_opten_por_la_metodologia_simplificada_quedan_exceptuadas_de_ap_f6f278
    - Excepcion_las_existencias_deterioradas_menores_a_un_millar_completo_se_contemplan_unicamen_d93c37
    - Excepcion_las_facturas_de_credito_electronicas_mipyme_impugnadas_conforme_al_procedimiento_4f055f
    - Excepcion_las_facturas_impugnadas_conforme_a_lo_establecido_en_el_punto_anterior_quedan_ex_a6cd9b
    - Excepcion_las_financiaciones_garantizadas_a_favor_del_banco_central_de_la_republica_argent_62429e
    - Excepcion_las_funcionalidades_de_fraccionamiento_y_transmision_para_negociacion_quedan_exc_db8a08
    - Excepcion_las_garantias_otorgadas_por_sgr_o_fondos_de_garantia_de_caracter_publico_quedan__48b224
    - Excepcion_las_garantias_otorgadas_por_sociedades_de_garantia_reciproca_o_por_fondos_de_gar_f9070b
    - Excepcion_las_garantias_reales_constituidas_en_un_pais_distinto_al_del_deudor_inmediato_se_3043e8
    - Excepcion_las_normas_pertinentes_se_aplicaran_a_las_entidades_publicas_o_mixtas_solo_en_cu_78add4
    - Excepcion_las_nuevas_entidades_financieras_no_estan_obligadas_a_contar_con_la_calificacion_d3b1f2
    - Excepcion_las_obligaciones_con_comercios_por_las_ventas_realizadas_mediante_tarjetas_de_de_96d87b
    - Excepcion_las_obligaciones_con_el_banco_central_de_la_republica_argentina_bcra_quedan_excl_5ef90c
    - Excepcion_las_obligaciones_con_entidades_financieras_locales_quedan_exceptuadas_de_las_obl_6c2015
    - Excepcion_las_operaciones_de_corresponsalia_en_el_exterior_quedan_exceptuadas_de_las_oblig_feeb3f
    - Excepcion_las_operaciones_de_servicios_quedan_exceptuadas_del_computo_del_minimo_del_51_de_a308dc
    - Excepcion_las_operaciones_referidas_en_el_punto_5_1_5_que_superen_el_termino_de_6_meses_qu_2d5813
    - Excepcion_las_solicitudes_de_apertura_de_oficina_de_representacion_en_reemplazo_de_una_suc_24596e
    - Excepcion_los_anexos_al_legajo_del_cliente_pueden_estar_separados_fisicamente_siempre_que__3ea131
    - Excepcion_los_antecedentes_comerciales_o_crediticios_negativos_no_aplican_cuando_a_criteri_baa2fa
    - Excepcion_los_creditos_con_el_banco_central_de_la_republica_argentina_quedan_excluidos_del_7be9de
    - Excepcion_los_creditos_frente_al_banco_central_de_la_republica_argentina_quedan_excluidos__e34dbd
    - Excepcion_los_depositos_en_pesos_en_cuentas_de_los_pspocp_en_las_que_se_encuentren_deposit_4ab8f5
    - Excepcion_los_deudores_cuyas_financiaciones_estan_totalmente_cubiertas_con_garantias_prefe_f30433
    - Excepcion_los_intereses_y_primas_devengados_vencidos_o_a_vencer_quedan_excluidos_del_compu_34118b
    - Excepcion_los_limites_podrian_tolerarse_en_determinadas_circunstancias_que_se_los_supere_d_3e41e6
    - Excepcion_los_saldos_de_las_financiaciones_computadas_para_la_deduccion_del_40_conforme_al_a083ac
    - Excepcion_no_aplica_el_envio_cuando_se_trate_de_personas_cuyas_informaciones_ya_obren_en_p_870339
    - Excepcion_no_aplica_el_requisito_de_presentacion_de_copia_certificada_del_estatuto_o_contr_d3d22e
    - Excepcion_no_aplica_la_clasificacion_de_activos_financieros_segun_criterios_de_niif_9_cuan_08a9cd
    - Excepcion_no_aplica_la_estimacion_de_deterioro_al_sector_publico_no_financiero__ri_dcpc_7__ef0553
    - Excepcion_no_aplica_la_exclusion_de_titulos_de_credito_no_custodiados_cuando_su_registro_y_0b0827
    - Excepcion_no_aplica_la_integracion_en_la_misma_moneda_en_los_casos_de_excepcion_previstos__0ceef1
    - Excepcion_no_aplica_la_obligacion_de_entrega_al_cliente_cuando_el_cheque_ha_sido_rechazado_bec139
    - Excepcion_no_aplica_la_obligacion_de_usar_el_procedimiento_de_la_ley_24_441_titulo_v_cuand_b94a8c
    - Excepcion_no_aplica_la_prevision_minima_si_la_entidad_opta_por_las_situaciones_mencionadas_4f2ee2
    - Excepcion_no_aplica_la_prohibicion_de_informacion_a_inversores_cuando_los_recursos_del_fon_a2a2f2
    - Excepcion_no_aplica_la_reclasificacion_automatica_cuando_se_trate_de_deudores_comprendidos_0b528f
    - Excepcion_no_aplica_la_reclasificacion_automatica_en_los_casos_a_que_se_refiere_el_punto_9_4bedc2
    - Excepcion_no_es_necesaria_la_inscripcion_en_el_registro_publico_de_la_correspondiente_juri_9d80ed
    - Excepcion_no_es_necesario_presentar_nuevamente_la_nota_si_ya_se_ha_cumplimentado_el_requis_f43997
    - Excepcion_no_es_obligatoria_la_evaluacion_de_capacidad_de_pago_en_funcion_de_ingresos_cuan_8de532
    - Excepcion_no_es_un_requerimiento_que_los_miembros_del_directorio_posean_conocimientos_tecn_bc6b5a
    - Excepcion_no_hay_limite_en_la_cantidad_de_adhesiones_al_sistema_de_debito_automatico_para__910da6
    - Excepcion_no_hay_limite_maximo_de_edad_para_los_solicitantes_salvo_el_que_surja_de_los_req_0cb7a4
    - Excepcion_no_se_computaran_las_exclusiones_establecidas_en_el_punto_1_2_de_las_normas_sobr_118106
    - Excepcion_no_se_consideraran_nuevos_accionistas_las_personas_que_ya_posean_una_participaci_8aa26c
    - Excepcion_no_se_excluyen_del_cupo_mipyme_minimo_las_mipyme_con_actividad_agricola_que_aunq_554241
    - Excepcion_no_se_exige_integracion_minima_diaria_para_depositos_en_titulos_valores_e_instru_3f4684
    - Excepcion_no_se_incluye_la_cobertura_por_responsabilidad_civil_cuando_el_automotor_no_sea__16cca8
    - Excepcion_no_se_interrumpe_el_computo_de_los_plazos_que_la_arca_establezca_cuando_los_fond_73c178
    - Excepcion_no_se_interrumpe_el_computo_de_los_plazos_que_la_arca_establezca_cuando_se_verif_86277f
    - Excepcion_no_se_producira_novacion_y_se_conservara_con_todos_sus_efectos_el_origen_del_cre_7a732d
    - Excepcion_no_se_requiere_acompanar_elementos_cuando_se_trata_de_personas_cuyos_antecedente_278410
    - Excepcion_no_se_requiere_el_sello_de_la_casa_receptora_cuando_se_utilizan_escrituras_mecan_c42bad
    - Excepcion_no_se_requiere_proveer_la_informacion_prevista_en_los_puntos_2_4_8_1_a_2_4_8_5_s_f5fc36
    - Excepcion_no_se_requiere_remitir_la_nomina_cuando_los_datos_de_las_personas_ya_se_encuentr_af9d0a
    - Excepcion_no_se_requiere_sello_de_la_casa_receptora_cuando_se_utilicen_escrituras_mecaniza_419f93
    - Excepcion_no_se_requiere_verificar_la_autenticidad_de_recibos_de_sueldo_lugar_de_trabajo_a_186806
    - Excepcion_no_sera_aplicable_el_regimen_de_traslados_contenido_en_el_punto_1_7_de_las_norma_0ecae7
    - Excepcion_no_sera_necesario_elaborar_reportes_para_los_sistemas_auxiliares_cuando_las_obli_dfe289
    - Excepcion_para_el_retiro_de_los_intereses_capitalizados_no_regira_la_disposicion_del_punto_8e7874
    - Excepcion_para_entidades_cuyas_acciones_se_encuentren_comprendidas_en_regimen_de_oferta_pu_785b5b
    - Excepcion_para_entidades_del_grupo_economico_bajo_supervision_consolidada_se_puede_optar_p_99cc2f
    - Excepcion_para_los_accionistas_existentes_al_27_7_17_la_limitacion_de_participacion_accion_347e77
    - Excepcion_podran_distribuirse_utilidades_una_vez_alcanzado_el_20_del_capital_social_mas_el_2ba013
    - Excepcion_queda_exceptuada_la_aplicacion_de_disposiciones_generales_en_materia_de_constitu_b8c061
    - Excepcion_queda_exceptuada_la_prohibicion_de_retencion_cuando_la_ley_o_disposicion_aplicab_8c3d0e
    - Excepcion_queda_exceptuada_la_prohibicion_de_solicitar_claves_cuando_se_trata_de_la_clave__fede09
    - Excepcion_quedan_exceptuadas_de_la_clasificacion_y_medicion_a_costo_amortizado_las_operaci_d0d4e3
    - Excepcion_quedan_exceptuadas_de_la_cobertura_del_sistema_de_seguro_de_garantia_de_los_depo_70f5ae
    - Excepcion_quedan_exceptuadas_de_la_prohibicion_de_imputacion_las_financiaciones_otorgadas__58a513
    - Excepcion_quedan_exceptuadas_de_las_restricciones_a_operaciones_activas_las_participacione_ca0e29
    - Excepcion_quedan_exceptuadas_de_las_restricciones_de_la_seccion_4_8_prohibiciones_los_sald_8cf7fd
    - Excepcion_quedan_exceptuadas_de_las_restricciones_de_operaciones_activas_la_tenencia_de_in_8b6678
    - Excepcion_quedan_exceptuadas_de_las_restricciones_sobre_operaciones_activas_las_operacione_7ef328
    - Excepcion_quedan_exceptuadas_del_fraccionamiento_del_credito_las_financiaciones_cubiertas__46255c
    - Excepcion_quedan_exceptuadas_las_exigencias_del_punto_2_9_2_que_no_sean_compatibles_con_la_90fd78
    - Excepcion_quedan_exceptuadas_las_operaciones_con_moneda_extranjera_y_o_con_metales_precios_b2d4ff
    - Excepcion_quedan_exceptuadas_las_operaciones_de_pase_con_el_banco_central_de_la_republica__d80346
    - Excepcion_quedan_exceptuadas_las_operaciones_de_pase_pasivo_con_otras_entidades_financiera_3317b1
    - Excepcion_quedan_exceptuadas_las_operaciones_en_mercados_autorizados_por_la_cnv_o_instituc_c46c2f
    - Excepcion_quedan_exceptuadas_las_participaciones_en_empresas_de_servicios_publicos_cuando__50b581
    - Excepcion_quedan_exceptuadas_las_transacciones_que_impliquen_instrumentos_de_regulacion_mo_a59efa
    - Excepcion_quedan_exceptuados_de_la_categoria_de_otras_obligaciones_a_plazo_los_depositos_c_96908e
    - Excepcion_quedan_exceptuados_de_la_clasificacion_como_irrecuperables_por_disposicion_tecni_76c0d3
    - Excepcion_quedan_exceptuados_de_la_deduccion_de_rpc_los_titulos_de_credito_cuyo_registro_y_12ce10
    - Excepcion_quedan_exceptuados_de_la_deduccion_de_titulos_de_credito_que_no_se_encuentren_en_997180
    - Excepcion_quedan_exceptuados_de_la_deduccion_los_inmuebles_adquiridos_mediante_subasta_jud_a310b2
    - Excepcion_quedan_exceptuados_de_la_exposicion_como_activos_por_impuesto_diferido_los_impor_771a8e
    - Excepcion_quedan_exceptuados_de_la_integracion_de_la_exigencia_de_efectivo_minimo_los_depo_785309
    - Excepcion_quedan_exceptuados_de_la_prohibicion_de_cobro_los_cargos_expresamente_autorizado_82eaa1
    - Excepcion_quedan_exceptuados_de_la_prohibicion_de_limites_de_importe_los_limites_que_expre_4b0938
    - Excepcion_quedan_exceptuados_de_las_condiciones_basicas_del_punto_1_1_2_3_los_casos_contem_7f4ac8
    - Excepcion_quedan_exceptuados_de_las_operaciones_admitidas_los_cajeros_automaticos_de_carga_66147f
    - Excepcion_quedan_exceptuados_del_ajuste_del_esquema_de_cobro_los_conceptos_que_deban_trasl_141f15
    - Excepcion_quedan_exceptuados_del_ajuste_del_esquema_de_cobro_los_servicios_adicionales_par_ec133c
    - Excepcion_quedan_exceptuados_los_cajeros_automaticos_del_pais_no_operados_por_entidades_fi_d5840c
    - Excepcion_quedan_exceptuados_los_limites_de_importe_que_expresamente_se_convengan_por_razo_29f07e
    - Excepcion_quedan_excluidas_de_las_obligaciones_comprendidas_en_la_exigencia_de_efectivo_mi_6eb99d
    - Excepcion_quedan_excluidas_del_computo_de_obligaciones_a_la_vista_las_transferencias_del_e_89fec0
    - Excepcion_quedan_excluidas_del_computo_del_cupo_mipyme_minimo_las_financiaciones_a_mipymes_773d2f
    - Excepcion_quedan_excluidas_del_computo_sobre_base_consolidada_las_tenencias_de_cuotapartes_6fd7bd
    - Excepcion_quedan_excluidas_del_previsionamiento_las_garantias_avales_y_otros_compromisos_e_3951ed
    - Excepcion_quedan_excluidas_del_regimen_de_efectivo_minimo_las_obligaciones_por_compras_al__fc4385
    - Excepcion_quedan_excluidos_de_la_integracion_los_titulos_publicos_nacionales_en_pesos_vinc_f7888c
    - Excepcion_quedan_excluidos_los_defectos_de_aplicacion_que_se_originen_en_operaciones_de_ca_0103df
    - Excepcion_salvo_lo_previsto_en_el_punto_4_5_3_2__depaho_4_5_3_1_7c06b5
    - Excepcion_se_admite_el_reemplazo_de_documentos_cedidos_antes_del_vencimiento_cuando_se_ver_63c847
    - Excepcion_se_admite_la_cancelacion_anticipada_de_pases_pasivos_con_otras_contrapartes_a_pa_6aa795
    - Excepcion_se_admite_la_realizacion_de_cauciones_bursatiles_a_plazos_inferiores_a_30_dias_o_0fc507
    - Excepcion_se_admite_una_extraccion_adicional_para_posibilitar_el_cierre_de_la_cuenta_condi_e1d181
    - Excepcion_se_admiten_acreditaciones_de_transferencias_del_exterior_originadas_en_cuentas_d_13ca84
    - Excepcion_se_admiten_acreditaciones_de_transferencias_del_exterior_originadas_en_cuentas_d_9691d7
    - Excepcion_se_exceptua_de_la_prohibicion_de_compensacion_lo_previsto_en_el_primer_parrafo_d_5c3f86
    - Excepcion_se_exceptua_del_impedimento_de_instalacion_de_oficinas_de_representacion_en_el_e_6f293e
    - Excepcion_se_exceptua_el_ordenamiento_por_liquidez_exigibilidad_cuando_se_privilegia_la_na_5f5fac
    - Excepcion_se_exceptua_la_exigencia_de_transferencia_previa_a_una_cuenta_a_la_vista_cuando__e368ec
    - Excepcion_se_exceptuan_las_asistencias_crediticias_relacionadas_con_actividades_de_servici_adc712
    - Excepcion_se_excluye_de_la_base_de_calculo_del_requerimiento_de_integracion_minima_diaria__5881b3
    - Excepcion_se_excluyen_de_la_identificacion_segun_moneda_de_origen_aquellas_partidas_que_no_d4cc99
    - Excepcion_se_excluyen_de_la_identificacion_segun_siscen_tabla_t0003_aquellas_partidas_que__a84f6c
    - Excepcion_se_excluyen_del_computo_de_la_posicion_global_neta_de_moneda_extranjera_los_conc_8e77e3
    - Excepcion_se_excluyen_los_bonos_vinculados_al_crecimiento_del_pbi_de_la_partida_titulos_pu_195f77
    - Excepcion_se_excluyen_los_derivados_contabilizados_en_partidas_fuera_de_balance_de_derivad_a9c3ff
    - Excepcion_se_permite_la_vinculacion_con_empresas_no_financieras_operadoras_de_cajeros_cuan_6e08c0
    - Excepcion_se_permite_mas_de_una_acreditacion_por_los_conceptos_de_repatriacion_de_fondos___76fa3f
    - Excepcion_se_suspende_el_requerimiento_de_integracion_minima_diaria_en_moneda_extranjera_a_a3ee06
    - Excepcion_subsistira_plenamente_el_derecho_real_de_hipoteca_incorporado_a_la_letra_en_gara_61637c
Obligacion: 1427 sin aplica_a
    - Obligacion_a_fin_de_informar_la_porcion_de_la_exigencia_en_pesos_integrada_en_forma_diaria__f331e8
    - Obligacion_a_la_cuota_de_capital_mas_los_intereses_pactados_segun_clausula_iii_3_se_adicion_6e27f8
    - Obligacion_a_las_partidas_previstas_en_el_punto_10_1_2_se_les_aplicara_la_misma_estructura__25e369
    - Obligacion_a_los_efectos_de_determinar_el_nivel_de_capital_adecuado_para_cubrir_el_rtici_se_423727
    - Obligacion_a_los_fines_de_que_el_exceso_no_sea_acumulativo_se_verificara_que_posicion_001_7_4784a5
    - Obligacion_a_los_fines_del_redondeo_de_las_magnitudes_se_incrementaran_los_valores_en_una_u_b5ce36
    - Obligacion_a_partir_de_la_incorporacion_en_situacion_normal_de_clientes_con_deudas_refinanc_ae07d7
    - Obligacion_a_partir_de_la_notificacion_el_deudor_debe_realizar_los_pagos_bajo_la_letra_en_e_978bf5
    - Obligacion_a_partir_de_los_datos_del_dia_18_y_hasta_el_31_de_agosto_tanto_las_partidas_de_i_f913f6
    - Obligacion_a_tal_fin_se_aplicaran_las_tasas_vigentes_en_cada_subperiodo__ri_rml_1_2_2_c9ea9b
    - Obligacion_acompanar_a_la_solicitud_de_autorizacion_de_sucursal_de_entidad_financiera_del_e_d7eb0a
    - Obligacion_acompanar_a_la_solicitud_de_autorizacion_documentacion_sobre_las_principales_reg_a77b73
    - Obligacion_acompanar_nota_de_debito_formula_3030_por_el_importe_del_cargo_indicando_como_co_facb58
    - Obligacion_actividad_recomendada_al_administrador_llevar_registros_de_los_distintos_procedi_0814f2
    - Obligacion_actividad_recomendada_al_administrador_realizar_inspecciones_frecuentes_a_la_pro_42f231
    - Obligacion_actividad_recomendada_al_administrador_realizar_uno_o_mas_informes_de_tasacion_c_65eb15
    - Obligacion_actividad_recomendada_al_administrador_una_vez_obtenida_la_tenencia_de_la_propie_ab35a1
    - Obligacion_adicionalmente_deben_considerarse_las_partidas_del_modelo_de_informacion_incluid_34ab01
    - Obligacion_adicionalmente_deberan_detallarse_todas_las_debilidades_significativas_que_se_de_3f21ba
    - Obligacion_administracion_de_las_comisiones_interbancarias_asociadas_al_proceso_de_compensa_f18e6a
    - Obligacion_administrar_en_linea_con_sus_objetivos_de_liquidez_intradiaria_los_momentos_del__f445c5
    - Obligacion_aforar_los_documentos_cedidos_con_la_categoria_asignada_al_sujeto_obligado_al_pa_213ade
    - Obligacion_ajustar_por_la_diferencia_respecto_de_las_previsiones_anteriormente_constituidas_e4a40b
    - Obligacion_al_cierre_de_cada_mes_si_un_instrumento_queda_con_saldo_negativo_debera_reclasif_d21df3
    - Obligacion_al_cierre_de_cada_mes_si_una_especie_de_titulo_publico_o_privado_queda_con_saldo_2a45c4
    - Obligacion_al_evaluar_el_grado_de_solvencia_de_los_solicitantes_debera_considerarse_no_solo_135512
    - Obligacion_al_evaluar_la_solvencia_de_los_solicitantes_debera_considerarse_no_solo_la_compo_d88839
    - Obligacion_al_inicio_de_cada_ejercicio_el_saldo_de_la_cuenta_450009_se_imputara_a_la_cuenta_2816b9
    - Obligacion_ante_el_cierre_de_la_cuenta_el_saldo_remanente_sera_puesto_a_disposicion_del_men_bdb020
    - Obligacion_ante_la_verificacion_de_infracciones_se_aplicaran_las_normas_sobre_regimen_disci_cf0f11
    - Obligacion_antes_de_recibir_autorizacion_para_su_uso_el_proceso_para_determinar_inputs_supu_040ede
    - Obligacion_aplicacion_obligatoria_del_regimen_de_incumplimientos_establecido_en_el_punto_1__80734d
    - Obligacion_aplicar_en_lo_pertinente_los_puntos_1_3_o_3_4_2_segun_se_trate_de_personas_human_aab026
    - Obligacion_aplicar_las_disposiciones_establecidas_para_cuentas_corrientes_especiales_para_p_8b07f5
    - Obligacion_aplicar_las_disposiciones_establecidas_para_los_depositos_en_caja_de_ahorros_o_c_1b5ce4
    - Obligacion_aprobacion_de_nuevos_productos_considerando_la_totalidad_de_las_posiciones_de_ti_a08f3b
    - Obligacion_asentar_en_el_acta_todas_las_caracteristicas_que_contribuyen_a_identificar_el_bi_ac70d9
    - Obligacion_ayudar_a_comprender_el_negocio_de_la_entidad_como_objetivo_del_relevamiento_del__0bad96
    - Obligacion_ayudar_a_identificar_los_riesgos_inherentes_caracteristicos_conocer_los_procedim_1b99f2
    - Obligacion_brindar_una_evaluacion_prospectiva_del_riesgo_como_parte_de_las_pruebas_de_estre_f9b76e
    - Obligacion_cada_agencia_complementaria_que_se_vincule_con_varias_entidades_financieras_debe_73b1f7
    - Obligacion_cada_beneficiario_debe_informar_al_juzgado_los_datos_de_identificacion_de_la_cue_b29ad8
    - Obligacion_cada_cac_debe_contar_con_un_codigo_de_visualizacion_para_verificar_la_informacio_027d0d
    - Obligacion_cada_entidad_debe_unificar_las_gestiones_logisticas_que_estime_corresponder_segu_81c7f7
    - Obligacion_cada_transferencia_inmediata_debe_incluir_las_descripciones_e_informacion_detall_04edd9
    - Obligacion_calcular_la_exigencia_sobre_el_promedio_mensual_de_la_suma_de_los_importes_exced_07aa86
    - Obligacion_calcular_plazos_residuales_computando_la_cantidad_de_dias_que_restan_hasta_el_ve_db4b21
    - Obligacion_calculo_de_posiciones_bilaterales_de_cada_entidad_y_envio_de_las_mismas_a_cada_u_968465
    - Obligacion_clasificar_a_los_clientes_al_cabo_de_cada_mes_exclusivamente_segun_pautas_objeti_588e4d
    - Obligacion_codigo_903200_001_exigencia_del_mes_sobre_depositos_y_obligaciones_a_plazo_en_pe_27d2a3
    - Obligacion_como_criterio_general_se_debe_aplicar_el_procedimiento_previsto_en_la_ley_24_441_6e3ff7
    - Obligacion_como_minimo_se_debe_considerar_el_efecto_del_rtici_en_el_valor_economico_de_la_e_575032
    - Obligacion_compilar_listados_de_deudores_por_operaciones_de_prestamos_u_otros_creditos_acre_5485fd
    - Obligacion_computar_las_financiaciones_comprendidas_que_cuenten_con_garantias_admitidas_seg_546449
    - Obligacion_computar_plazos_residuales_de_obligaciones_de_pago_en_cuotas_de_capital_en_forma_6de0a2
    - Obligacion_comunicacion_previa_a_la_entidad_depositaria_antes_del_cierre_de_la_cuenta__depa_ebe4ad
    - Obligacion_comunicar_sin_demora_al_banco_la_circunstancia_de_extravio_o_sustraccion_de_la_h_60aae5
    - Obligacion_con_caracter_general_los_fondos_radicados_en_cuentas_de_depositos_deberan_transf_e72c0b
    - Obligacion_con_la_informacion_de_rechazos_recibida_de_la_cec_la_entidad_girada_revertira_lo_4d8514
    - Obligacion_conjuntamente_con_la_posicion_de_noviembre_08_se_debera_informar_por_unica_vez_e_5d81bf
    - Obligacion_conocer_los_registros_contables_las_transacciones_significativas_y_el_flujo_de_i_a7c0f5
    - Obligacion_conservar_la_documentacion_vinculada_a_los_movimientos_en_cuentas_a_la_vista_par_5cc1db
    - Obligacion_consignar_en_codigo_824000_001_el_incremento_en_la_exigencia_proveniente_del_aum_155daf
    - Obligacion_consignar_promedio_mensual_de_saldos_diarios_de_depositos_y_obligaciones_que_ver_e943bc
    - Obligacion_continuara_computandose_para_la_correspondiente_deduccion_su_promedio_mensual_de_e06189
    - Obligacion_correspondera_reconocer_el_importe_de_los_gastos_realizados_para_la_obtencion_de_d8b7c3
    - Obligacion_cotejar_los_resultados_del_arqueo_sorpresivo_con_los_registros_contables_y_o_la__8497a1
    - Obligacion_cotejar_los_resultados_del_arqueo_sorpresivo_de_inversiones_con_los_registros_co_f59fa1
    - Obligacion_cotejo_de_los_resultados_del_arqueo_sorpresivo_con_los_registros_contables_y_o_l_76c2ac
    - Obligacion_cuando_al_cierre_de_un_periodo_mensual_las_cuentas_de_otros_resultados_integrale_1241eb
    - Obligacion_cuando_el_cliente_formaliza_su_adhesion_a_traves_de_la_empresa_prestadora_de_ser_931073
    - Obligacion_cuando_el_cliente_solicita_acceso_a_movimientos_y_saldos_la_agencia_complementar_a5f05a
    - Obligacion_cuando_el_importe_remanente_sea_superior_a_la_acreencia_neta_de_previsiones_no_s_0ec467
    - Obligacion_cuando_el_saldo_de_la_cuenta_de_resultado_por_reconocimiento_inicial_sea_acreedo_3bc147
    - Obligacion_cuando_el_saldo_de_la_cuenta_de_resultado_por_refinanciacion_sea_acreedor_al_cie_e33fec
    - Obligacion_cuando_el_saldo_de_la_cuenta_de_resultado_por_venta_o_baja_sea_deudor_al_cierre__be9f08
    - Obligacion_cuando_el_saldo_de_la_cuenta_sea_deudor_a_fin_de_un_periodo_mensual_se_expondra__36f4d9
    - Obligacion_cuando_el_valor_razonable_surge_de_tecnica_de_valoracion_sin_datos_de_mercado_ob_c05ef2
    - Obligacion_cuando_entre_los_accionistas_se_incluyan_personas_juridicas_debera_suministrarse_cfc0de
    - Obligacion_cuando_existe_diferencia_en_activos_medidos_a_valor_razonable_debe_imputarse_en__79c13b
    - Obligacion_cuando_la_suma_total_de_creditos_supere_la_cantidad_de_caracteres_disponibles_de_86ce05
    - Obligacion_cuando_la_suma_total_de_debitos_supere_la_cantidad_de_caracteres_disponibles_deb_a02ef9
    - Obligacion_cuando_no_se_encuentre_previsto_en_los_puntos_precedentes_y_en_la_medida_en_que__7835e8
    - Obligacion_cuando_profesionales_actuan_a_nombre_de_estudios_de_contadores_publicos_deben_in_8efdad
    - Obligacion_cuando_se_concedan_al_mismo_prestatario_otras_facilidades_crediticias_ademas_de__c46e96
    - Obligacion_cuando_se_efectue_cancelacion_de_compras_a_personas_humanas_y_juridicas_en_el_ma_42e609
    - Obligacion_cuando_se_hubiese_delegado_las_tareas_de_auditoria_interna_en_un_profesional_ind_084b83
    - Obligacion_cuando_se_reduzca_el_importe_en_libros_de_un_activo_por_revaluacion_la_disminuci_c39b28
    - Obligacion_cuando_se_utilicen_metodos_de_screening_o_scoring_las_variables_tenidas_en_cuent_212d94
    - Obligacion_cuando_se_verifiquen_concurrentemente_deficiencias_en_la_posicion_en_promedio_y__671ab8
    - Obligacion_cuando_sea_factible_o_recomendable_la_comunicacion_con_el_deudor_debe_incluir_en_5b7c5c
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_de_los_requeridos_debe_complet_af5843
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_de_los_requeridos_para_la_info_300d10
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_de_los_requeridos_para_la_info_d0f7b3
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_de_los_requeridos_para_la_info_f5e5fc
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_de_los_requeridos_se_debe_llen_142562
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_que_los_requeridos_para_la_inf_2da236
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_que_los_requeridos_para_la_inf_c8bff2
    - Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_que_los_requeridos_se_debera_l_364c02
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_de_los_requeridos_debe_completarse_e66ee7
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_de_los_requeridos_para_la_informac_3a76ce
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_de_los_requeridos_para_la_informac_bc5f0b
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_de_los_requeridos_para_la_informac_f114b2
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_de_los_requeridos_se_debe_llenar_c_495813
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_de_los_requeridos_se_debera_llenar_870826
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_que_los_requeridos_para_la_informa_1f738d
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_que_los_requeridos_para_la_informa_e25567
    - Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_que_los_requeridos_se_debera_llena_fdb507
    - Obligacion_cuando_una_operacion_iniciada_no_haya_podido_completarse_la_agencia_complementar_6dd29d
    - Obligacion_cumplimiento_de_las_exigencias_que_siguen_con_una_antelacion_no_inferior_a_30_di_94aca6
    - Obligacion_cumplimiento_obligatorio_en_todos_los_casos_de_la_normativa_en_materia_de_preven_95432c
    - Obligacion_dar_aviso_a_la_entidad_administradora_al_ultimo_domicilio_registrado__depaho_3_2_94f255
    - Obligacion_de_existir_franquicias_por_disminucion_de_cargos_codigos_681000_m_y_682000_m_se__b9facb
    - Obligacion_de_los_controles_de_monitoreo_surge_la_necesidad_de_investigar_los_errores_siend_478426
    - Obligacion_de_los_controles_de_monitoreo_surge_la_necesidad_de_investigar_los_errores_siend_52568c
    - Obligacion_de_registrar_defectos_de_integracion_en_promedio_en_el_bimestre_para_la_liquidac_90f6ba
    - Obligacion_debe_asegurarse_que_los_sistemas_aplicativos_operen_constantemente_de_acuerdo_co_3f5b96
    - Obligacion_debe_calcularse_la_suma_de_los_importes_de_los_creditos_incluidos_en_el_lote__sn_fb8327
    - Obligacion_debe_calcularse_la_suma_de_los_importes_de_los_debitos_incluidos_en_el_lote__snp_406b06
    - Obligacion_debe_calcularse_la_suma_del_campo_entidad_a_debitar_acreditar_de_los_registros_i_0c659e
    - Obligacion_debe_considerarse_el_riesgo_de_contraparte_para_cada_uno_de_los_instrumentos_fin_f078d6
    - Obligacion_debe_consignarse_la_leyenda_esta_operacion_en_una_entidad_financiera_podria_no_t_2be107
    - Obligacion_debe_constar_obligatoriamente_informacion_del_cliente_originante_nombre_o_razon__85b35a
    - Obligacion_debe_constar_obligatoriamente_informacion_del_movimiento_de_fondos_importe_y_mon_427829
    - Obligacion_debe_constar_obligatoriamente_la_cuenta_a_acreditar_mediante_clave_bancaria_unif_4f5f97
    - Obligacion_debe_constar_obligatoriamente_la_identificacion_del_movimiento_de_fondos_entidad_cf9fd0
    - Obligacion_debe_documentarse_el_proceso_de_validacion_entendido_como_la_comparacion_de_los__02a9dc
    - Obligacion_debe_efectuarse_el_cotejo_de_las_predicciones_realizadas_con_el_comportamiento_c_811fc3
    - Obligacion_debe_existir_suficiente_documentacion_de_las_principales_fuentes_de_datos_utiliz_b69334
    - Obligacion_debe_existir_un_procedimiento_documentado_que_permita_vincular_las_calificacione_21bde5
    - Obligacion_debe_existir_una_politica_clara_sobre_quien_sera_informado_como_se_realizara_la__935cab
    - Obligacion_debe_indicarse_la_fecha_a_partir_de_la_cual_el_auditor_interino_se_hace_cargo_e__227d9e
    - Obligacion_debe_registrarse_el_numero_de_lote_determinado_por_la_entidad_origen_el_cual_deb_00ac63
    - Obligacion_debe_registrarse_el_numero_identificatorio_de_la_entidad_origen_incluyendo_el_nu_3b4e0a
    - Obligacion_debe_registrarse_en_la_cuenta_los_siguientes_datos_especificados_en_los_items_qu_72cedf
    - Obligacion_debe_registrarse_la_cantidad_total_de_registros_individuales_y_adicionales_que_e_54e7f2
    - Obligacion_debe_revisar_que_las_funciones_comerciales_esten_separadas_del_area_responsable__e0ae3a
    - Obligacion_deben_aplicarse_los_parametros_que_se_establecen_en_esta_seccion_al_otorgamiento_0584c2
    - Obligacion_deben_implicar_acciones_apropiadas_cuando_las_perdidas_estimadas_sean_superiores_870a47
    - Obligacion_deben_realizar_analisis_previos_al_otorgamiento_de_financiaciones_y_refinanciaci_044046
    - Obligacion_deber_de_acompanar_copia_de_la_documentacion_que_justifique_la_realizacion_de_bi_728a9f
    - Obligacion_deber_de_agregar_certificacion_de_la_empresa_que_efectuo_el_pago_tratandose_de_i_924797
    - Obligacion_deber_de_agregar_una_descripcion_detallada_del_calculo_de_la_franquicia_para_el__516923
    - Obligacion_deber_de_aplicar_el_regimen_normativo_establecido_para_los_depositos_en_caja_de__f823e2
    - Obligacion_deber_de_aplicar_los_puntos_que_se_encontraban_vigentes_al_04_12_2020_hasta_tant_001186
    - Obligacion_deber_de_asignar_flujos_de_fondos_nocionales_de_posiciones_con_opciones_automati_a1a3ef
    - Obligacion_deber_de_asignar_todos_los_flujos_de_fondos_procedentes_del_pago_de_intereses_y__31be74
    - Obligacion_deber_de_comunicar_de_inmediato_a_la_superintendencia_de_entidades_financieras_y_7d248b
    - Obligacion_deber_de_considerar_el_porcentaje_que_corresponda_sobre_la_exigencia_del_mes_baj_bdf274
    - Obligacion_deber_de_considerar_en_forma_permanente_el_valor_de_mercado_de_los_activos_que_c_2b5a4e
    - Obligacion_deber_de_considerar_para_obtener_la_relacion_irpc_kmin_los_conceptos_del_regimen_680289
    - Obligacion_deber_de_consignar_el_numero_y_fecha_de_la_resolucion_a_traves_de_la_que_se_otor_3133b8
    - Obligacion_deber_de_contar_con_la_opinion_favorable_de_un_abogado_sobre_la_recuperacion_del_a973a1
    - Obligacion_deber_de_determinar_la_existencia_de_un_sistema_de_generacion_de_informacion_al__a02264
    - Obligacion_deber_de_determinar_la_existencia_de_un_sistema_de_informacion_de_gestion_para_u_0ebd03
    - Obligacion_deber_de_efectuar_recalculo_respecto_de_los_defectos_de_aplicacion_de_la_capacid_5fab77
    - Obligacion_deber_de_indicar_aspectos_minimos_de_cada_sistema_aplicativo_relevamientos_antec_a2bd72
    - Obligacion_deber_de_indicar_como_se_afrontara_la_cancelacion_de_saldos_con_indicacion_de_lo_ca9446
    - Obligacion_deber_de_informar_el_cumplimiento_de_los_elementos_de_seguridad_establecidos_par_15550d
    - Obligacion_deber_de_informar_el_cumplimiento_de_los_elementos_de_seguridad_establecidos_par_801354
    - Obligacion_deber_de_informar_la_cantidad_de_cofres_existentes_en_la_caja_tesoro_movil__ri_m_3ebe1e
    - Obligacion_deber_de_informar_los_intereses_correspondientes_a_los_recursos_computables__ri__29d454
    - Obligacion_deber_de_inscripcion_ante_el_registro_nacional_de_base_de_datos_en_los_casos_que_f32b75
    - Obligacion_deber_de_poseer_en_la_caja_billetes_y_monedas_de_distintas_denominaciones_y_en_c_70dca1
    - Obligacion_deber_de_presentar_declaracion_estrechamente_referida_al_patrimonio_o_los_ingres_9f7730
    - Obligacion_deber_de_presentar_elementos_de_juicio_probatorios_en_caso_de_haberse_declarado__a77b78
    - Obligacion_deber_de_prestar_especial_atencion_a_la_correcta_interpretacion_y_determinacion__712900
    - Obligacion_deber_de_proporcionar_estados_financieros_correspondientes_a_los_dos_ultimos_eje_859959
    - Obligacion_deber_de_proporcionar_la_nomina_de_los_integrantes_del_directorio_cuando_se_trat_863c90
    - Obligacion_deber_de_proveer_sin_cargo_una_tarjeta_magnetica_de_debito_al_titular_de_la_cuen_8a8d1d
    - Obligacion_deber_de_que_la_manifestacion_de_bienes_cuente_con_certificacion_emitida_por_con_ac12e9
    - Obligacion_deber_de_realizar_la_revision_de_la_razonabilidad_de_los_ajustes_de_resultados_d_de457c
    - Obligacion_deber_de_remitir_los_ejemplares_no_canjeables_billetes_sin_valor_al_bcra_para_su_b1e5d2
    - Obligacion_deber_de_revisar_el_efectivo_ingreso_de_los_fondos_correspondientes_a_los_aument_8655c2
    - Obligacion_deber_de_revisar_la_adecuada_compilacion_de_los_listados_de_deudores_por_prestam_6ccc4c
    - Obligacion_deber_de_revisar_procedimiento_implementado_que_asegure_generacion_y_almacenamie_5ecc2f
    - Obligacion_deber_de_tratar_la_opcion_automatica_implicita_sobre_tasas_de_interes_no_conside_ab8344
    - Obligacion_deber_de_tratar_posiciones_a_tasa_variable_como_una_serie_de_pagos_de_interes_fi_1bfb27
    - Obligacion_deber_de_verificar_cumplimiento_de_controles_de_autorizacion_sobre_incorporacion_0e0695
    - Obligacion_deber_de_verificar_el_valor_de_origen_de_los_bienes_tomados_en_defensa_de_credit_ef54ed
    - Obligacion_deber_de_verificar_la_identidad_del_titular_a_base_de_alguno_de_los_documentos_p_505c25
    - Obligacion_deber_de_verificar_que_en_los_archivos_de_sistemas_aplicativos_de_operaciones_pa_342cde
    - Obligacion_debera_adjuntarse_el_acta_de_directorio_aprobando_la_designacion_de_los_integran_f739b5
    - Obligacion_debera_aplicarse_el_procedimiento_previsto_en_el_punto_1_13_para_el_cierre_de_la_c488a5
    - Obligacion_debera_considerarse_el_codigo_70100000_del_tercer_mes_anterior_a_la_fecha_de_ven_e85fd0
    - Obligacion_debera_considerarse_los_codigos_70300000_menos_3600000y_de_corresponder_y_708000_b645b9
    - Obligacion_debera_consignarse_la_denominacion_de_la_entidad_girada_y_el_importe_de_cada_uno_bd6862
    - Obligacion_debera_dejarse_constancia_en_el_legajo_del_cliente_de_la_afectacion_directa_y_ex_dfe95f
    - Obligacion_debera_designarse_un_encargado_de_la_dependencia__expaef_4_5_3_1_7f3233
    - Obligacion_debera_emitirse_un_informe_por_cada_ciclo_relevante_evaluado_definido_en_la_etap_bb5114
    - Obligacion_debera_estar_expresamente_estipulado_en_el_contrato_de_tercerizacion_la_aceptaci_852435
    - Obligacion_debera_incluir_el_cumplimiento_de_requerimientos_informativos_de_organismos_de_r_e7c0d4
    - Obligacion_debera_incluir_los_resultados_de_la_evaluacion_del_area_de_sistemas_de_informaci_53f5c9
    - Obligacion_debera_incluir_observaciones_derivadas_de_su_evaluacion_de_los_procedimientos_se_f6b52e
    - Obligacion_debera_incluir_observaciones_resultantes_de_su_evaluacion_del_sistema_a_traves_d_e38611
    - Obligacion_debera_incluir_su_opinion_sobre_el_cumplimiento_dentro_de_los_plazos_informados__ac8374
    - Obligacion_debera_incluir_su_opinion_sobre_el_funcionamiento_del_area_de_auditoria_interna__c3a11e
    - Obligacion_debera_incluir_una_explicacion_sobre_las_areas_de_riesgo_significativas_en_relac_b71f45
    - Obligacion_debera_informarse_la_cantidad_de_cofres_existentes_en_el_tesoro_modular__ri_mmse_ef9041
    - Obligacion_debera_observarse_lo_previsto_en_las_normas_sobre_instrumentacion_conservacion_y_88bf99
    - Obligacion_debera_observarse_lo_previsto_en_las_normas_sobre_instrumentacion_conservacion_y_ac1b12
    - Obligacion_deberan_comunicarse_a_los_usuarios_las_recomendaciones_y_recaudos_que_como_minim_31b751
    - Obligacion_deberan_informar_tal_situacion_integrando_unicamente_los_datos_identificatorios__c03b3b
    - Obligacion_deberan_observarse_las_mismas_disposiciones_establecidas_en_el_punto_2_2__ri_dcp_f62cfd
    - Obligacion_deberan_tenerse_en_cuenta_las_pautas_incluidas_en_la_seccion_1_instrucciones_gen_aa2f7f
    - Obligacion_deberan_tomarse_los_recaudos_necesarios_para_la_destruccion_de_los_residuos_emer_6babcc
    - Obligacion_declaracion_de_contar_con_capacidad_de_atesoramiento_para_custodiar_por_cuenta_y_1ba9f0
    - Obligacion_declaracion_de_cumplimiento_con_medidas_minimas_de_seguridad_en_entidades_financ_b867b9
    - Obligacion_definir_adecuadamente_los_procesos_para_la_gestion_de_los_usuarios_y_asegurar_un_a2ee76
    - Obligacion_dejar_expresa_constancia_en_los_contratos_recibos_u_otros_documentos_de_relacion_3cb8c9
    - Obligacion_dentro_de_los_60_dias_corridos_siguientes_a_la_fecha_de_la_apertura_de_la_cuenta_c55fcb
    - Obligacion_desarrollar_canales_adecuados_de_revision_por_instancias_superiores_escalamiento_705696
    - Obligacion_desarrollar_pruebas_efectivas_sobre_el_sistema_contable_como_objetivo_del_releva_d52404
    - Obligacion_desarrollar_un_conjunto_especifico_de_limites_de_riesgo_para_seguir_la_evolucion_b0d44c
    - Obligacion_descargar_periodicamente_los_archivos_de_actualizacion_dispuestos_en_el_sitio_de_197e4e
    - Obligacion_determinar_la_proporcion_a_imputar_considerando_el_porcentaje_que_resulte_al_com_601160
    - Obligacion_determinar_los_procedimientos_a_aplicar_y_la_frecuencia_de_revision_de_los_ciclo_83d06c
    - Obligacion_devengar_el_interes_neto_sobre_el_pasivo_activo_neto_de_planes_de_beneficios_def_d43515
    - Obligacion_devolucion_del_ejemplar_deteriorado_al_cliente_o_presentante_para_que_tramite_su_9c46fd
    - Obligacion_difundir_en_forma_diaria_el_archivo_de_bajas_de_inhabilitados_para_cada_cuit_cui_13da25
    - Obligacion_distribuir_entre_los_titulares_en_partes_iguales_el_capital_impuesto_en_las_cuen_d99f81
    - Obligacion_durante_el_transcurso_normal_de_las_actividades_de_gestion_tiene_lugar_el_monito_c53eae
    - Obligacion_durante_junio_y_julio_se_considerara_el_incremento_de_exigencia_para_conceptos_e_f1a48c
    - Obligacion_durante_septiembre_y_meses_subsiguientes_se_considerara_el_incremento_de_exigenc_3a24b5
    - Obligacion_durante_septiembre_y_meses_subsiguientes_se_considerara_el_incremento_de_exigenc_e4cd27
    - Obligacion_efectuar_convenios_para_obtener_los_fondos_de_liquidez_intradiaria_suficientes_a_cf09de
    - Obligacion_el_acreedor_debe_comunicar_el_estado_de_deuda_al_agente_de_registro_correspondie_d4f901
    - Obligacion_el_acreedor_debe_extender_al_deudor_los_recibos_correspondientes_por_los_pagos_d_632379
    - Obligacion_el_acreedor_sus_agentes_sucesores_y_cesionarios_declaran_que_no_han_inducido_al__dda410
    - Obligacion_el_acta_debe_transcribirse_en_un_libro_especial_de_control_interno_y_enviarse_al_142e39
    - Obligacion_el_administrador_de_un_esquema_de_transferencias_inmediatas_debe_definir_los_pro_70d519
    - Obligacion_el_administrador_debe_cobrar_las_indemnizaciones_por_vida_correspondientes_y_apl_ec42f7
    - Obligacion_el_administrador_debe_comunicarse_con_el_deudor_para_reclamar_el_pago_y_advertir_43e560
    - Obligacion_el_administrador_debe_comunicarse_con_el_deudor_para_reclamar_el_pago_y_advertir_563b2e
    - Obligacion_el_administrador_debe_comunicarse_telefonicamente_con_el_deudor_codeudor_o_garan_6aca4d
    - Obligacion_el_administrador_debe_comunicarse_telefonicamente_con_el_deudor_codeudor_o_garan_b1047b
    - Obligacion_el_administrador_debe_continuar_contactos_con_el_deudor_y_enviar_notificaciones__b7715d
    - Obligacion_el_administrador_debe_continuar_contactos_con_el_deudor_y_enviar_notificaciones__be81e9
    - Obligacion_el_administrador_debe_controlar_y_supervisar_el_proceso_de_secuestro_del_automot_20cbb4
    - Obligacion_el_administrador_debe_efectuar_el_seguimiento_y_regularizacion_de_la_mora_de_acu_d5db50
    - Obligacion_el_administrador_debe_efectuar_las_modificaciones_a_los_terminos_y_condiciones_d_e70203
    - Obligacion_el_administrador_debe_efectuar_seguimiento_de_los_seguros_de_vida_y_de_danos_y_d_c9e435
    - Obligacion_el_administrador_debe_emplear_sus_mejores_esfuerzos_para_cobrar_los_pagos_period_3a6f44
    - Obligacion_el_administrador_debe_guardar_en_la_carpeta_de_administracion_documentacion_canc_1c5a06
    - Obligacion_el_administrador_debe_guardar_en_la_carpeta_de_administracion_documentacion_rela_27c07a
    - Obligacion_el_administrador_debe_guardar_en_la_carpeta_de_administracion_toda_comunicacion__e43d7f
    - Obligacion_el_administrador_debe_guardar_en_la_carpeta_de_administracion_toda_documentacion_8f1a50
    - Obligacion_el_administrador_debe_guardar_en_la_carpeta_de_administracion_todo_otro_elemento_5af4a5
    - Obligacion_el_administrador_debe_informar_con_anticipacion_razonable_a_la_fecha_de_vencimie_0c83a3
    - Obligacion_el_administrador_debe_iniciar_los_tramites_de_ejecucion_hipotecaria_cuando_se_ve_0236be
    - Obligacion_el_administrador_debe_llevar_un_registro_de_las_llamadas_telefonicas_incluyendo__331d38
    - Obligacion_el_administrador_debe_llevar_un_registro_de_las_llamadas_telefonicas_incluyendo__b687be
    - Obligacion_el_administrador_debe_mantener_archivos_y_registros_completos_de_cada_prestamo___b6a367
    - Obligacion_el_administrador_debe_mantener_permanentemente_actualizados_los_datos_relativos__f9c7b9
    - Obligacion_el_administrador_debe_mantener_registros_adecuados_de_las_cobranzas__manori_1_3__403a96
    - Obligacion_el_administrador_debe_mantener_registros_contables_completos_actualizados_y_prec_37bbfb
    - Obligacion_el_administrador_debe_mantener_y_dar_seguimiento_a_las_polizas_de_seguro_contrat_035902
    - Obligacion_el_administrador_debe_procesar_las_precancelaciones_de_prestamos__manori_1_3_2_969126
    - Obligacion_el_administrador_debe_procesar_los_reclamos_de_indemnizacion_por_siniestros__man_ccab05
    - Obligacion_el_administrador_debe_realizar_el_seguimiento_y_regularizacion_de_la_mora_en_los_5c0104
    - Obligacion_el_administrador_debe_realizar_la_cobranza_de_las_cuotas_del_prestamo_hipotecari_9f7f87
    - Obligacion_el_administrador_debe_realizar_las_ejecuciones_hipotecarias_y_remates_cuando_cor_df4be1
    - Obligacion_el_administrador_debe_recibir_e_imputar_los_pagos_que_efectuen_los_deudores__man_d72a15
    - Obligacion_el_administrador_debe_utilizar_profesionales_especializados_en_procedimientos_de_01196c
    - Obligacion_el_analisis_de_variaciones_debe_incluir_la_obtencion_de_variaciones_indicadores__f98f5d
    - Obligacion_el_analisis_debe_incluir_aspectos_estructurales_de_solvencia_liquidez_y_otros_ri_9d20cd
    - Obligacion_el_analisis_del_riesgo_debe_realizarse_con_una_frecuencia_adecuada_y_sus_resulta_62ba2f
    - Obligacion_el_analisis_especifico_debe_incluir_el_relevamiento_y_o_actualizacion_de_los_pro_ef9358
    - Obligacion_el_analisis_especifico_debe_incluir_la_evaluacion_de_si_los_procedimientos_son_s_4d5381
    - Obligacion_el_analisis_especifico_debe_incluir_la_evaluacion_del_riesgo_remanente_a_cubrir__f9abe0
    - Obligacion_el_analisis_especifico_debe_incluir_la_identificacion_de_las_areas_y_rubros_cont_2ba59d
    - Obligacion_el_analisis_especifico_debe_incluir_la_identificacion_de_los_tipos_de_errores_qu_114298
    - Obligacion_el_analisis_especifico_debe_incluir_la_seleccion_de_los_procedimientos_de_audito_285bc3
    - Obligacion_el_auditor_debe_aplicar_procedimientos_orientados_a_la_obtencion_de_evidencias_q_500061
    - Obligacion_el_auditor_debera_considerar_el_efecto_de_los_objetivos_no_cumplidos_sobre_la_es_041c13
    - Obligacion_el_auditor_debera_considerar_las_consecuencias_que_las_deficiencias_o_falta_de_c_ea41c2
    - Obligacion_el_auditor_debera_dejar_documentado_para_cada_actividad_de_control_identificada__896a28
    - Obligacion_el_auditor_externo_debe_considerar_el_funcionamiento_del_sistema_de_control_inte_f4754e
    - Obligacion_el_auditor_externo_debe_considerar_el_marco_regulatorio_y_societario_que_la_caja_cc9528
    - Obligacion_el_auditor_externo_debe_considerar_identificar_y_evaluar_como_minimo_los_control_005048
    - Obligacion_el_auditor_externo_debe_considerar_identificar_y_evaluar_como_minimo_los_control_1c85d1
    - Obligacion_el_auditor_externo_debe_considerar_identificar_y_evaluar_como_minimo_los_control_43aca8
    - Obligacion_el_auditor_externo_debe_efectuar_pruebas_de_cumplimiento_de_los_procedimientos_d_c07767
    - Obligacion_el_auditor_externo_debe_efectuar_un_analisis_de_variaciones_de_los_estados_conta_c77444
    - Obligacion_el_auditor_externo_debe_evaluar_como_el_consejo_de_administracion_de_la_caja_de__3429f5
    - Obligacion_el_auditor_externo_debe_evaluar_la_organizacion_del_area_de_auditoria_interna_la_c749f9
    - Obligacion_el_auditor_externo_debe_identificar_los_hechos_o_circunstancias_externos_o_inter_31349c
    - Obligacion_el_auditor_externo_debe_obtener_de_la_caja_de_credito_los_manuales_de_procedimie_494979
    - Obligacion_el_auditor_externo_debe_obtener_informacion_actualizada_sobre_la_estructura_line_a2ac5a
    - Obligacion_el_auditor_externo_debe_obtener_todos_los_elementos_de_juicio_validos_y_suficien_f966e7
    - Obligacion_el_auditor_externo_debe_realizar_un_analisis_de_la_informacion_contable_y_financ_613652
    - Obligacion_el_auditor_externo_debe_utilizar_el_relevamiento_y_evaluacion_del_control_intern_75f41e
    - Obligacion_el_auditor_externo_debera_evaluar_la_razonabilidad_de_las_variaciones_de_las_pri_6400a0
    - Obligacion_el_auditor_interno_debera_completar_pruebas_para_determinar_si_los_controles_est_c6d9fb
    - Obligacion_el_aumento_del_capital_regulatorio_podra_utilizarse_como_medida_transitoria_mien_46d45a
    - Obligacion_el_aumento_del_valor_se_reconocera_en_el_resultado_del_periodo_en_la_cuenta_util_8dd007
    - Obligacion_el_banco_central_de_la_republica_argentina_administrara_una_central_de_letras_de_d89fe3
    - Obligacion_el_bcra_debe_efectuar_el_recuento_de_numerario_de_acuerdo_con_las_normas_vigente_42ee06
    - Obligacion_el_bcra_debe_enviar_una_nota_al_presentante_comunicandole_el_resultado_de_la_per_d9be25
    - Obligacion_el_bcra_debe_poner_en_conocimiento_a_las_entidades_adheridas_sobre_las_modificac_c06f78
    - Obligacion_el_bcra_debe_registrar_el_embargo_en_la_base_de_datos_de_cheques_cancelatorios_e_48dcce
    - Obligacion_el_bcra_debitara_de_la_cuenta_corriente_de_la_entidad_financiera_declarante_el_i_873336
    - Obligacion_el_bcra_en_su_caracter_de_ente_emisor_pone_en_circulacion_las_monedas_conmemorat_32ab28
    - Obligacion_el_bcra_informara_a_las_entidades_requirentes_las_cantidades_asignadas_la_fecha__c37f06
    - Obligacion_el_bcra_pone_en_circulacion_la_moneda_conmemorativa_del_80_aniversario_de_la_cre_7fec63
    - Obligacion_el_bcra_remitira_al_auditor_externo_las_observaciones_formuladas_durante_la_ulti_3f3d50
    - Obligacion_el_campo_10_fecha_del_cheque_debe_completarse_utilizando_las_posiciones_50_a_55__a1feba
    - Obligacion_el_campo_11_reservado_debe_completarse_con_15_ceros__snp_cheq_7_1_12_b3d7fe
    - Obligacion_el_campo_13_nombre_de_la_imagen_reservado_debe_completarse_con_el_nombre_de_la_i_6ac337
    - Obligacion_el_campo_14_punto_de_intercambio_debe_completarse_con_el_codigo_del_punto_de_int_0db04e
    - Obligacion_el_campo_15_datos_del_reclamo_debe_completarse_con_el_valor_fijo_1__snp_cheq_7_1_3e2ec4
    - Obligacion_el_campo_16_reservado_debe_completarse_con_ceros__snp_cheq_7_1_12_14b576
    - Obligacion_el_campo_2_banco_depositario_debe_completarse_con_el_codigo_de_banco_depositario_f64fe8
    - Obligacion_el_campo_3_banco_girado_debe_completarse_con_el_codigo_de_banco_girado_en_3_posi_430b49
    - Obligacion_el_campo_4_sucursal_girada_debe_completarse_con_el_codigo_de_sucursal_girada_en__b324e0
    - Obligacion_el_campo_5_codigo_postal_debe_completarse_utilizando_las_posiciones_11_a_14_del__c31311
    - Obligacion_el_campo_6_numero_de_cheque_debe_completarse_con_el_numero_de_cheque_en_8_posici_72dd68
    - Obligacion_el_campo_7_numero_de_cuenta_debe_completarse_con_el_numero_de_cuenta_en_11_posic_bf0cd9
    - Obligacion_el_campo_8_importe_debe_completarse_utilizando_las_posiciones_34_a_43_del_regist_2d82b6
    - Obligacion_el_campo_9_fecha_de_compensacion_debe_completarse_utilizando_las_posiciones_44_a_134cd9
    - Obligacion_el_campo_contador_de_registro_debe_completarse_con_el_mismo_contador_de_registro_5f71ea
    - Obligacion_el_campo_de_primer_motivo_de_rechazo_debe_describir_la_razon_del_rechazo_utiliza_f0a014
    - Obligacion_el_campo_debe_contener_el_total_de_bloques_del_archivo_un_bloque_se_compone_de_9_c23cac
    - Obligacion_el_campo_debe_contener_el_total_de_lotes_que_contiene_el_archivo_con_longitud_de_52fede
    - Obligacion_el_campo_debe_contener_el_total_de_registros_individuales_y_adicionales_que_exis_a74f05
    - Obligacion_el_campo_debe_contener_la_identificacion_de_la_entidad_que_origina_el_rechazo_o__9ac3bc
    - Obligacion_el_campo_debe_contener_la_suma_de_los_importes_de_los_creditos_incluidos_en_el_a_fe408d
    - Obligacion_el_campo_debe_contener_la_suma_de_los_importes_de_los_debitos_incluidos_en_el_ar_c0ddcb
    - Obligacion_el_campo_debe_contener_la_suma_del_campo_totales_de_control_de_los_registros_de__13d8fe
    - Obligacion_el_campo_debe_incluir_el_numero_de_comunicado_del_rechazo_de_la_entidad_al_bcra__5099b7
    - Obligacion_el_campo_debe_llevar_el_contador_de_registro_de_la_transaccion_original_contador_21754f
    - Obligacion_el_campo_identificador_de_registro_debe_completarse_con_el_valor_7_para_indicar__37864d
    - Obligacion_el_canje_debe_prestarse_en_horario_habitual_de_atencion_al_publico_sin_discrimin_d7e650
    - Obligacion_el_cargo_se_calculara_sobre_los_excesos_determinados_conforme_al_punto_4_2_de_es_fca05b
    - Obligacion_el_cliente_debera_solicitar_la_apertura_de_la_cuenta_especial_cecon_ar_en_pesos__8558a2
    - Obligacion_el_codigo_de_barras_debe_encontrarse_en_el_cuerpo_principal_del_cheque_cancelato_3bf4a3
    - Obligacion_el_codigo_de_clase_de_transaccion_debe_completarse_con_200_para_identificar_tran_2a5197
    - Obligacion_el_codigo_tipo_de_registro_adicional_debe_completarse_con_el_valor_99__snp_cheq__0de1ee
    - Obligacion_el_comprobante_debe_detallar_el_monto_y_concepto_correspondiente_a_toda_comision_5f6355
    - Obligacion_el_computo_de_las_partidas_componentes_de_la_posicion_diaria_se_efectuara_sobre__3c05d1
    - Obligacion_el_consejo_de_administracion_debera_resolver_sobre_cada_una_de_las_recomendacion_61c807
    - Obligacion_el_consejo_de_administracion_debera_tomar_conocimiento_formal_del_informe_y_volc_6df795
    - Obligacion_el_consejo_de_administracion_o_autoridad_equivalente_debe_tomar_conocimiento_y_r_c45a1b
    - Obligacion_el_contador_publico_debe_firmar_con_aclaracion_y_certificacion_por_el_consejo_pr_544179
    - Obligacion_el_contrato_de_credito_debe_contener_las_pautas_minimas_establecidas_en_la_prese_dbc77a
    - Obligacion_el_contrato_debera_evaluar_la_constitucion_de_margenes_iniciales_en_operaciones__4de18f
    - Obligacion_el_contrato_debera_evaluar_la_constitucion_de_margenes_iniciales_y_prever_la_int_0f5b9e
    - Obligacion_el_contrato_debera_prever_la_integracion_diaria_de_margenes_de_variacion__opefci_554a38
    - Obligacion_el_contrato_entre_la_entidad_financiera_y_la_empresa_de_administracion_de_redes__618068
    - Obligacion_el_convenio_de_fusion_debe_incluir_constancia_de_que_la_operacion_esta_sujeta_a__6cde2e
    - Obligacion_el_credito_devengara_interes_compensatorio_vencido_sobre_saldos_pagadero_por_per_76ff04
    - Obligacion_el_declarante_asume_el_compromiso_de_informar_cualquier_modificacion_en_la_vincu_35f785
    - Obligacion_el_declarante_asume_el_compromiso_de_informar_cualquier_modificacion_en_las_empr_4d0c43
    - Obligacion_el_declarante_asume_el_compromiso_de_informar_cualquier_modificacion_que_se_prod_28682a
    - Obligacion_el_declarante_debe_informar_el_estado_de_vinculacion_al_31_de_diciembre_de_cada__194991
    - Obligacion_el_declarante_debe_informar_el_estado_de_vinculacion_con_empresas_o_entidades_al_4de48e
    - Obligacion_el_desempeno_de_las_tecnicas_de_mitigacion_del_riesgo_coberturas_neteo_uso_de_ga_9f6dd5
    - Obligacion_el_destino_de_los_fondos_debera_ser_uno_de_los_enunciados_en_los_apartados_a_a_j_90171d
    - Obligacion_el_destino_de_los_fondos_del_prestamo_prendario_automotor_debera_ser_uno_de_los__5d182d
    - Obligacion_el_deudor_autoriza_al_acreedor_a_debitar_los_cargos_de_seguro_y_sus_actualizacio_1f12c1
    - Obligacion_el_deudor_autoriza_que_los_intereses_por_saldos_deudores_en_cuenta_corriente_sea_a1d4e0
    - Obligacion_el_deudor_codeudor_es_o_garante_s_se_compromete_n_a_comunicar_cualquier_modifica_96174a
    - Obligacion_el_deudor_codeudor_es_y_garante_s_certifican_con_caracter_de_declaracion_jurada__ce9679
    - Obligacion_el_deudor_codeudor_es_y_garante_s_se_comprometen_a_comunicar_cualquier_modificac_b3ebdd
    - Obligacion_el_deudor_codeudor_es_y_garante_s_se_hacen_responsables_legalmente_frente_a_cual_3e163b
    - Obligacion_el_deudor_debe_aplicar_el_prestamo_exclusivamente_al_pago_del_saldo_del_precio_d_9cb886
    - Obligacion_el_deudor_debe_comunicar_al_acreedor_su_decision_de_cancelar_el_credito_en_forma_2a2f5c
    - Obligacion_el_deudor_debe_comunicar_al_acreedor_su_decision_de_precancelacion_mediante_cart_bc03c8
    - Obligacion_el_deudor_debe_efectuar_los_pagos_en_el_domicilio_del_acreedor_o_donde_este_indi_eef2c2
    - Obligacion_el_deudor_debe_hacerse_cargo_de_todos_los_cargos_e_impuestos_originados_por_la_p_5b24a2
    - Obligacion_el_deudor_debe_hacerse_cargo_de_todos_los_cargos_e_impuestos_que_la_precancelaci_a30652
    - Obligacion_el_deudor_debe_informar_al_acreedor_su_situacion_frente_al_iva_si_no_lo_hace_ser_d4bdb9
    - Obligacion_el_deudor_debe_pagar_el_seguro_sobre_el_bien_prendado_que_se_adiciona_a_la_cuota_da9c92
    - Obligacion_el_deudor_debe_pagar_importes_adicionales_para_compensar_retenciones_de_modo_que_f5481a
    - Obligacion_el_deudor_debe_pagar_interes_compensatorio_a_tasa_fija_expresada_en_porcentaje_n_6c17da
    - Obligacion_el_deudor_debe_pagar_interes_variable_calculado_sobre_el_saldo_del_capital_adeud_385728
    - Obligacion_el_deudor_debe_pagar_interes_variable_junto_con_cada_cuota_de_capital_calculado__c6be24
    - Obligacion_el_deudor_debe_reintegrar_de_inmediato_al_acreedor_los_importes_desembolsados_po_c4d575
    - Obligacion_el_deudor_debe_restituir_el_capital_en_cuotas_consecutivas_segun_sistema_aleman__6744c8
    - Obligacion_el_deudor_debe_restituir_el_capital_en_cuotas_consecutivas_segun_sistema_frances_a49d86
    - Obligacion_el_deudor_presta_conformidad_para_que_los_intereses_devengados_por_saldos_deudor_f76068
    - Obligacion_el_deudor_refinanciado_que_haya_cumplido_con_lo_dispuesto_en_los_parrafos_preced_2e2df0
    - Obligacion_el_deudor_se_obliga_a_cumplir_con_los_actos_personales_necesarios_para_la_contra_958ff8
    - Obligacion_el_dinero_en_efectivo_depositado_debe_ser_consumido_por_el_titular_de_manera_pre_37b794
    - Obligacion_el_directorio_debe_identificar_con_claridad_a_sus_delegados_para_la_gestion_del__373947
    - Obligacion_el_directorio_del_bcra_debe_tener_en_cuenta_las_caracteristicas_de_cada_proyecto_49a545
    - Obligacion_el_directorio_del_bcra_debe_verificar_el_cumplimiento_de_los_requisitos_establec_39fee1
    - Obligacion_el_directorio_o_autoridad_equivalente_de_las_entidades_designara_a_las_personas__3738b9
    - Obligacion_el_directorio_o_sus_delegados_deben_aprobar_las_iniciativas_relevantes_en_materi_c2c10a
    - Obligacion_el_directorio_y_la_alta_gerencia_deben_contemplar_la_planificacion_del_capital_c_2a2cb1
    - Obligacion_el_efecto_del_impuesto_a_las_ganancias_asociado_a_las_variaciones_de_activos_y_p_757fd3
    - Obligacion_el_empleador_debe_entregar_al_trabajador_uno_de_los_dos_ejemplares_de_las_normas_874d03
    - Obligacion_el_empleador_o_quien_solicite_la_apertura_de_la_cuenta_sera_responsable_por_la_i_56c6d0
    - Obligacion_el_encargado_del_centro_de_intercambio_debe_verificar_la_entrega_del_original_ca_3bcda8
    - Obligacion_el_envio_de_la_imagen_reclamada_o_el_rechazo_de_la_solicitud_por_no_corresponder_e61d3c
    - Obligacion_el_estudio_de_auditoria_se_compromete_a_comunicar_a_la_superintendencia_de_entid_7d6284
    - Obligacion_el_estudio_de_profesionales_se_obliga_como_fiador_solidario_con_renuncia_a_los_b_9a1d60
    - Obligacion_el_examen_se_centrara_basicamente_en_la_calidad_de_la_gestion_y_control_de_los_r_aa65cf
    - Obligacion_el_exceso_de_integracion_trasladable_se_informara_mediante_la_partida_760000_001_f8d17b
    - Obligacion_el_icaap_debe_considerar_las_necesidades_de_capital_de_corto_y_largo_plazo_y_pro_8f36b7
    - Obligacion_el_icaap_debe_permitir_que_el_directorio_y_la_alta_gerencia_cuenten_con_una_comp_2ae761
    - Obligacion_el_icaap_debe_realizarse_tanto_en_base_individual_como_consolidada_y_comprender__ca13a1
    - Obligacion_el_identificador_de_registro_debe_asignarse_con_el_valor_9_para_identificar_el_t_99382b
    - Obligacion_el_identificador_de_registro_debe_completarse_con_el_valor_8_para_identificar_el_ad9a58
    - Obligacion_el_importe_informado_en_esta_partida_en_febrero_2020_se_incluira_en_el_total_de__f709f1
    - Obligacion_el_informe_especial_debera_consignar_las_fechas_importes_y_datos_del_prestatario_497b71
    - Obligacion_el_informe_sobre_los_estados_contables_debe_acompanar_al_regimen_informativo_con_a848f1
    - Obligacion_el_legajo_debe_contar_con_los_datos_que_permitan_la_identificacion_del_cliente_d_23db11
    - Obligacion_el_marco_debe_definir_claramente_los_instrumentos_las_estrategias_de_cobertura_y_f65354
    - Obligacion_el_marco_debe_describir_las_facultades_delegadas_las_lineas_de_responsabilidad_y_4ccee5
    - Obligacion_el_memorandum_debe_contener_como_minimo_una_descripcion_de_las_deficiencias_sign_dd98f6
    - Obligacion_el_memorandum_debe_incluir_sugerencias_para_solucionar_las_deficiencias_signific_254361
    - Obligacion_el_menor_autorizado_podra_realizar_debitos_para_la_suscripcion_de_cuotapartes_de_31b1dd
    - Obligacion_el_mismo_criterio_de_promedio_se_aplicara_a_los_datos_del_codigo_801000_m_deposi_ce239c
    - Obligacion_el_monto_proveniente_de_la_declaracion_voluntaria_de_tenencia_de_moneda_extranje_4851cb
    - Obligacion_el_monto_proveniente_de_la_declaracion_voluntaria_de_tenencia_de_moneda_extranje_547073
    - Obligacion_el_monto_representado_por_los_billetes_excedentes_que_las_entidades_financieras__0b0b09
    - Obligacion_el_nivel_de_capital_debe_ser_suficiente_considerando_tanto_el_nivel_de_riesgo_ac_3785af
    - Obligacion_el_numero_de_lote_debe_ser_ascendente_determinado_por_la_entidad_origen__snp_che_690571
    - Obligacion_el_obligado_al_pago_puede_solicitar_el_detalle_de_las_fcem_que_conforman_la_info_5c8052
    - Obligacion_el_otorgamiento_de_asistencia_crediticia_de_monto_reducido_no_impide_que_si_se_c_630023
    - Obligacion_el_pagador_cliente_originante_y_el_beneficiario_cliente_receptor_deben_contar_co_0688d3
    - Obligacion_el_pago_circulacion_y_demas_aspectos_particulares_de_la_gestion_de_fcem_en_el_sc_a1d725
    - Obligacion_el_plan_de_contingencia_debe_ser_revisado_y_sometido_a_prueba_en_forma_regular_p_e88f21
    - Obligacion_el_plan_de_continuidad_de_negocios_debe_ser_prospectivo_al_evaluar_el_impacto_de_c51abd
    - Obligacion_el_plan_debe_desarrollar_implementar_y_realizar_regularmente_ejercicios_de_conti_c479cd
    - Obligacion_el_plan_debe_establecer_claramente_el_proceso_interno_de_toma_de_decisiones_y_de_dea220
    - Obligacion_el_plan_debe_estar_disenado_para_afrontar_los_escenarios_planteados_por_la_entid_b49dad
    - Obligacion_el_plan_debe_identificar_las_operaciones_criticas_y_las_dependencias_internas_y__6b7718
    - Obligacion_el_plan_debe_incorporar_un_analisis_del_impacto_de_esas_posibles_disrupciones_en_f26396
    - Obligacion_el_plan_debe_proporcionar_una_guia_detallada_y_clara_respecto_de_la_implementaci_e350f1
    - Obligacion_el_plan_debe_proporcionar_una_guia_detallada_y_clara_respecto_de_la_sucesion_de__e272ed
    - Obligacion_el_plan_estrategico_debe_recoger_con_claridad_las_necesidades_de_capital_de_la_e_ef6255
    - Obligacion_el_plazo_de_aprobacion_de_las_operaciones_sera_en_la_jornada_de_recepcion_de_las_69010f
    - Obligacion_el_plazo_de_la_operacion_de_pase_pasivo_con_entidades_financieras_se_pactara_lib_5bcd05
    - Obligacion_el_precio_de_venta_se_imputa_primero_a_gastos_de_secuestro_realizacion_e_impuest_424c6c
    - Obligacion_el_precio_debe_ser_el_mismo_independientemente_de_la_cantidad_y_tipo_de_transacc_ec40e8
    - Obligacion_el_procedimiento_de_analisis_de_variaciones_debe_quedar_adecuadamente_documentad_d9f1c6
    - Obligacion_el_procedimiento_de_homologacion_debera_repetirse_cada_vez_que_se_produzca_algun_824982
    - Obligacion_el_proceso_de_evaluacion_de_la_suficiencia_del_capital_debe_tener_en_cuenta_todo_30b113
    - Obligacion_el_proceso_de_gestion_de_riesgos_debe_incluir_aquellos_riesgos_que_si_bien_no_so_0d01fa
    - Obligacion_el_proceso_de_planeamiento_y_evaluacion_del_riesgo_debe_incluir_como_minimo_la_t_10d682
    - Obligacion_el_proceso_de_validacion_permanente_debe_establecer_un_conjunto_de_eventos_anoma_f063f8
    - Obligacion_el_proceso_debe_incluir_un_marco_eficaz_viable_y_consistente_que_permita_realiza_b54d86
    - Obligacion_el_proceso_sistematico_de_auditoria_continua_realizado_a_traves_de_medios_tecnol_0ab34a
    - Obligacion_el_proposito_y_responsabilidad_de_la_auditoria_interna_debe_estar_formalizado_en_e8ab66
    - Obligacion_el_registro_de_la_operacion_en_el_resumen_de_cuenta_constituye_el_comprobante_de_b201ef
    - Obligacion_el_registro_en_el_resumen_de_cuenta_constituye_comprobante_de_la_operacion_de_tr_57149a
    - Obligacion_el_registro_en_el_resumen_periodico_constituye_comprobante_de_la_operacion_de_tr_329267
    - Obligacion_el_relevamiento_de_los_ciclos_la_identificacion_evaluacion_y_prueba_de_los_contr_db1a01
    - Obligacion_el_relevamiento_del_sistema_contable_debera_ser_documentado_adecuadamente__nmcie_3a3a65
    - Obligacion_el_relevamiento_identificacion_evaluacion_y_prueba_de_los_controles_podra_ser_do_77c2c7
    - Obligacion_el_responsable_de_asignar_o_confirmar_las_calificaciones_debe_ser_un_area_indepe_75e676
    - Obligacion_el_responsable_del_control_interno_debera_remitir_al_consejo_de_administracion_u_edb407
    - Obligacion_el_responsable_del_control_interno_elaborara_informes_segun_las_modalidades_que__36f54d
    - Obligacion_el_responsable_del_grupo_de_auditoria_interna_integrara_el_comite_de_auditoria_d_1a5c29
    - Obligacion_el_resto_de_los_intereses_por_aplicacion_de_la_tasa_de_interes_efectiva_y_ajuste_882a82
    - Obligacion_el_resultado_del_analisis_de_solvencia_debera_reflejarse_en_el_formulario_de_apr_326d0b
    - Obligacion_el_resultado_del_analisis_de_solvencia_debera_reflejarse_en_el_formulario_de_apr_a770eb
    - Obligacion_el_resultado_final_se_redondeara_al_entero_mas_proximo__ri_rml_sbloque14_696a86
    - Obligacion_el_resultado_por_venta_incluye_la_reclasificacion_de_ganancia_o_perdida_acumulad_3c7785
    - Obligacion_el_retiro_de_los_valores_solicitados_se_realizara_al_dia_habil_siguiente_en_el_m_2dd6a3
    - Obligacion_el_saldo_acreedor_de_las_cuentas_de_corresponsalia_se_imputara_en_el_rubro_del_p_ad4548
    - Obligacion_el_saldo_del_aporte_debe_contabilizarse_en_la_cuenta_obligaciones_subordinadas_a_de45cf
    - Obligacion_el_saldo_deudor_de_la_cuenta_corriente_de_corresponsalia_se_imputara_en_el_rubro_e1b035
    - Obligacion_el_sim_para_el_rtici_debe_captar_el_efecto_de_multiples_escenarios_sobre_el_valo_cef859
    - Obligacion_el_sistema_de_calificaciones_debe_ofrecer_calificaciones_de_todos_los_deudores_y_b2b3ae
    - Obligacion_el_sistema_de_control_de_calidad_debe_prever_la_deteccion_de_discrepancias_entre_5dee49
    - Obligacion_el_sistema_de_control_de_calidad_debe_prever_la_toma_de_medidas_correctivas_en_f_f2839d
    - Obligacion_el_sistema_de_informacion_debe_permitir_realizar_el_seguimiento_de_los_creditos__817aac
    - Obligacion_el_sistema_de_informacion_para_la_gestion_de_riesgos_mis_debe_permitir_clasifica_7e0ba7
    - Obligacion_el_sistema_de_medicion_de_riesgos_debe_modelar_la_curva_de_rendimientos_por_ejem_f17493
    - Obligacion_el_sistema_de_medicion_del_riesgo_debe_ser_capaz_de_identificar_y_cuantificar_la_1263b9
    - Obligacion_el_sistema_interno_de_calificacion_debe_contribuir_a_evaluar_la_necesidad_de_cam_70194a
    - Obligacion_el_sistema_interno_de_calificacion_debe_facilitar_el_seguimiento_de_las_califica_e3e8a8
    - Obligacion_el_sistema_interno_de_calificacion_debe_reaccionar_a_indicadores_de_deterioro_ac_ff6f14
    - Obligacion_el_sistema_interno_de_calificacion_debe_servir_para_producir_informes_periodicos_fae5d2
    - Obligacion_el_socio_responsable_debe_declarar_bajo_juramento_que_cuenta_con_antiguedad_en_l_512348
    - Obligacion_el_socio_responsable_debe_declarar_bajo_juramento_su_responsabilidad_por_la_labo_a15600
    - Obligacion_el_socio_responsable_debe_tener_la_independencia_requerida_por_las_normas_de_aud_e941f9
    - Obligacion_el_socio_responsable_declara_conocer_y_aceptar_que_por_ejercer_su_funcion_queda__b664d3
    - Obligacion_el_socio_responsable_tiene_identica_responsabilidad_que_el_contador_publico_desi_02adce
    - Obligacion_el_tamano_del_descalce_de_moneda_extranjera_asumido_por_la_entidad_debe_tomar_en_0fe0b3
    - Obligacion_el_tamano_del_descalce_de_moneda_extranjera_asumido_por_la_entidad_debe_tomar_en_4dc3b8
    - Obligacion_el_tamano_del_descalce_de_moneda_extranjera_asumido_por_la_entidad_debe_tomar_en_9a3389
    - Obligacion_el_tamano_del_descalce_de_moneda_extranjera_asumido_por_la_entidad_debe_tomar_en_cc7af3
    - Obligacion_el_tenedor_debe_ingresar_los_datos_de_la_cuenta_en_la_que_se_acreditaran_los_fon_9db97a
    - Obligacion_el_titular_de_la_cuenta_es_responsable_ante_la_entidad_financiera_por_todas_las__7bf09f
    - Obligacion_el_titular_de_la_cuenta_sera_la_persona_indicada_en_primer_termino_quien_abre_la_81a5df
    - Obligacion_el_titular_debe_comunicar_previamente_a_la_entidad_depositaria_el_cierre_de_la_c_1ce108
    - Obligacion_el_titular_debe_solicitar_la_transferencia_de_los_fondos_correspondientes_a_una__fcf62c
    - Obligacion_el_titulo_de_propiedad_del_bien_prendado_queda_depositado_en_el_acreedor_o_sus_c_949754
    - Obligacion_el_total_de_facturas_ingresadas_a_la_compensacion_se_expresara_en_pesos_con_dos__4ae83a
    - Obligacion_el_trabajador_o_beneficiario_debe_requerir_fehacientemente_la_incorporacion_de_s_d854bf
    - Obligacion_el_trabajador_que_requiera_directamente_la_apertura_debera_presentar_la_informac_1da519
    - Obligacion_el_usuario_debe_comunicar_de_inmediato_al_banco_con_el_que_opera_y_al_banco_admi_a6477d
    - Obligacion_el_usuario_debera_proceder_al_retiro_total_del_saldo_o_a_su_opcion_se_procedera__5b5617
    - Obligacion_el_vencimiento_para_su_presentacion_operara_a_las_15_hs_del_dia_habil_siguiente__06c590
    - Obligacion_en_cada_cuenta_prevista_segun_la_clase_de_activo_se_incorporaran_todos_los_compo_e2f57a
    - Obligacion_en_cancelaciones_parciales_anticipadas_los_intereses_se_recalculan_sobre_el_nuev_0b7f59
    - Obligacion_en_caso_de_atraso_en_los_pagos_el_administrador_debe_mantener_contacto_inmediato_c858d7
    - Obligacion_en_caso_de_cancelaciones_parciales_anticipadas_los_intereses_se_recalcularan_sob_cee7ff
    - Obligacion_en_caso_de_corresponder_se_informara_en_octubre_el_computo_bimestral_del_defecto_39139a
    - Obligacion_en_caso_de_declarar_tenencia_de_moneda_extranjera_el_cliente_debera_solicitar_la_fc9061
    - Obligacion_en_caso_de_encontrarse_redactada_en_idioma_extranjero_debera_acompanarse_la_corr_bac244
    - Obligacion_en_caso_de_existir_remanente_del_producido_de_la_ejecucion_debera_ser_reintegrad_3509d0
    - Obligacion_en_caso_de_mora_ambos_intereses_compensatorio_y_punitorio_se_capitalizaran_en_fo_b91a6c
    - Obligacion_en_caso_de_mora_se_aplican_intereses_compensatorios_y_punitorios_capitalizados_s_69f0ec
    - Obligacion_en_caso_de_pago_de_impuestos_el_declarante_debe_presentar_a_la_entidad_el_volant_a5df80
    - Obligacion_en_caso_de_que_en_la_segunda_presentacion_algun_valor_resultara_rechazado_por_ca_961559
    - Obligacion_en_caso_de_siniestro_el_administrador_debe_efectuar_los_reclamos_pertinentes_ant_dd22a1
    - Obligacion_en_caso_de_siniestros_en_el_automotor_el_administrador_debe_determinar_si_las_in_46e5ab
    - Obligacion_en_casos_de_incumplimientos_seran_aplicables_a_los_responsables_las_disposicione_099155
    - Obligacion_en_cobertura_de_flujo_de_efectivo_la_cuenta_otros_resultados_integrales_disminuc_9b47ed
    - Obligacion_en_el_acceso_para_consultar_la_cenfiv_se_debera_dejar_constancia_de_que_la_infor_ea99cb
    - Obligacion_en_el_boleto_de_compraventa_se_debera_senalar_mediante_una_clausula_especifica_q_48cc29
    - Obligacion_en_el_caso_de_otras_monedas_extranjeras_se_convertiran_a_dolares_estadounidenses_18423e
    - Obligacion_en_el_caso_de_transferencias_de_fondos_el_comprobante_debe_contener_los_datos_de_e673e1
    - Obligacion_en_el_codigo_de_etica_se_debera_prever_la_obligacion_de_confidencialidad__nmcief_7c5f74
    - Obligacion_en_el_momento_de_la_disposicion_o_disposicion_parcial_del_negocio_en_el_extranje_67d88c
    - Obligacion_en_el_primer_calculo_de_exposicion_al_riesgo_pais_las_exposiciones_deben_imputar_2a568c
    - Obligacion_en_el_segundo_calculo_de_exposicion_al_riesgo_pais_las_exposiciones_deben_imputa_d9d540
    - Obligacion_en_esta_institucion_se_determinara_c_base_sobre_los_datos_informados_por_cada_en_0c82d4
    - Obligacion_en_funcion_de_la_complejidad_de_las_operaciones_y_para_asegurar_que_sea_suficien_c66922
    - Obligacion_en_la_comunicacion_de_instalacion_del_puesto_se_debera_consignar_declaracion_de__1c5b5c
    - Obligacion_en_la_comunicacion_de_instalacion_del_puesto_se_debera_consignar_los_requisitos__bd203e
    - Obligacion_en_la_comunicacion_de_tercerizacion_se_debera_consignar_los_datos_correspondient_8002d7
    - Obligacion_en_la_determinacion_de_margenes_de_cobertura_para_operaciones_cubiertas_con_gara_f0bd15
    - Obligacion_en_la_documentacion_que_suscriba_el_auditor_interino_debe_indicarse_que_su_actua_d89010
    - Obligacion_en_la_partida_285_010_se_incluiran_ademas_de_las_letras_internas_del_bcra_las_le_826623
    - Obligacion_en_la_partida_70400x_010_se_incluiran_en_promedio_de_saldos_diarios_las_posicion_55bda3
    - Obligacion_en_la_partida_70400x_010_se_incluiran_letras_y_notas_del_bcra_donde_las_letras_s_dfd65e
    - Obligacion_en_la_posicion_siguiente_a_la_de_pesos_la_exigencia_trasladada_debera_compensars_3311a7
    - Obligacion_en_la_presentacion_de_la_solicitud_de_autorizacion_se_debera_consignar_el_nombre_d081ba
    - Obligacion_en_la_presentacion_de_la_solicitud_se_consignara_y_acompanara_lo_siguiente__caja_0b47c5
    - Obligacion_en_las_3_posiciones_del_campo_no_3_primer_motivo_de_rechazo_se_debe_indicar_la_c_9389e0
    - Obligacion_en_los_activos_aptos_segun_la_definicion_de_la_nic_23_se_incluiran_en_las_cuenta_c790c7
    - Obligacion_en_los_casos_de_personas_humanas_que_posean_domicilio_real_en_el_extranjero_debe_66cf34
    - Obligacion_en_los_casos_de_prestamos_prendarios_expresados_en_uva_unidades_de_valor_adquisi_f6a37a
    - Obligacion_en_los_casos_en_que_existe_endoso_o_cesion_pendiente_de_aceptacion_al_momento_de_f9378d
    - Obligacion_en_los_casos_en_que_se_requiera_la_emision_de_la_cac_de_un_echeq_caducado_debera_c48c84
    - Obligacion_en_los_contratos_recibos_u_otros_documentos_de_relacion_con_los_clientes_donde_s_a971f2
    - Obligacion_en_los_documentos_que_instrumenten_los_respectivos_actos_juridicos_debera_consta_0b9c93
    - Obligacion_en_materia_de_documentos_de_identidad_se_debera_observar_lo_previsto_en_la_secci_cbc019
    - Obligacion_en_mora_el_saldo_de_capital_devenga_interes_punitorio_ademas_del_compensatorio_c_551828
    - Obligacion_en_refinanciaciones_para_determinar_una_mejora_en_la_clasificacion_del_deudor_se_30b089
    - Obligacion_en_relacion_con_la_preparacion_de_la_respuesta_ante_ciberincidentes_evaluar_norm_73d1dc
    - Obligacion_en_sucursales_de_entidades_extranjeras_del_grupo_a_la_casa_matriz_debe_designar__64bc71
    - Obligacion_en_todos_los_casos_de_mora_el_saldo_de_capital_adeudado_devenga_un_interes_punit_af2500
    - Obligacion_en_todos_los_casos_debera_consignarse_expresamente_la_fuente_a_partir_de_la_cual_8328bd
    - Obligacion_en_todos_los_casos_para_el_calculo_de_los_intereses_se_tomara_como_divisor_fijo__b7ab66
    - Obligacion_en_todos_los_casos_para_el_calculo_de_los_intereses_se_tomara_como_divisor_fijo__d68932
    - Obligacion_entre_los_procedimientos_sustantivos_a_aplicar_debera_incluir_arqueos_de_efectiv_f20f62
    - Obligacion_enviar_al_titular_mensualmente_a_traves_de_medios_electronicos_un_resumen_con_el_84a1a1
    - Obligacion_envio_de_informacion_estadistica_y_de_control_al_bcra__snp_tr_1_1_2_f0b320
    - Obligacion_envio_del_resumen_semestral_al_domicilio_del_titular_salvo_que_el_titular_opte_e_8a4608
    - Obligacion_es_funcion_de_la_auditoria_interna_asegurar_la_integridad_de_la_informacion_que__80c938
    - Obligacion_es_necesario_dejar_evidencia_del_impacto_de_los_resultados_obtenidos_mediante_la_6be4a7
    - Obligacion_es_necesario_relevar_y_entender_el_sistema_contable_como_parte_del_analisis_de_l_bcb4e6
    - Obligacion_es_recomendable_que_el_simple_dador_de_hipoteca_asuma_el_caracter_de_garante_se__ac5890
    - Obligacion_es_requisito_que_la_propiedad_este_cubierta_por_un_seguro_de_danos_que_cumpla_co_d3b223
    - Obligacion_estar_preparada_para_afrontar_alteraciones_graves_e_inesperadas_en_el_flujo_de_f_42f1bb
    - Obligacion_estimaciones_de_los_riesgos_de_mercado_credito_y_operacional_considerando_la_tot_4a7aac
    - Obligacion_evaluacion_integral_del_auditor_externo_que_debe_verificar_i_cumplimiento_de_nor_d28d5a
    - Obligacion_evaluar_el_funcionamiento_del_control_de_formalizacion_aplicado_a_aquellos_servi_d51eff
    - Obligacion_evaluar_el_marco_de_gestion_de_riesgos_de_tecnologia_y_seguridad_de_la_informaci_261b7b
    - Obligacion_evaluar_el_proceso_de_control_que_permita_realizar_un_seguimiento_y_evaluacion_d_cbd782
    - Obligacion_evaluar_el_proceso_de_gestion_de_actualizaciones_de_infraestructura_tecnologica__66ec1e
    - Obligacion_evaluar_el_proceso_de_gestion_de_actualizaciones_de_seguridad__nmcief_a6_sbloque_88973f
    - Obligacion_evaluar_el_proceso_de_gestion_de_cambios__nmcief_a6_sbloque9_95beac
    - Obligacion_evaluar_el_proceso_de_gestion_de_las_configuraciones__nmcief_a6_sbloque9_6e5ff3
    - Obligacion_evaluar_el_proceso_para_elaborar_el_analisis_de_impacto_del_negocio_bia_que_invo_4407cf
    - Obligacion_evaluar_el_proceso_para_la_gestion_de_las_comunicaciones__nmcief_a6_sbloque9_952a74
    - Obligacion_evaluar_el_sistema_aplicativo_de_prestatarios_y_sus_interfases_con_el_contable___7b7407
    - Obligacion_evaluar_la_perspectiva_de_continuidad_de_los_ingresos_computables_de_los_solicit_c5c6f9
    - Obligacion_evaluar_la_politica_y_el_marco_de_gestion_de_procesos_servicios_y_o_actividades__8ae849
    - Obligacion_evaluar_la_razonabilidad_de_las_previsiones_por_riesgo_de_incobrabilidad_y_de_de_3117d1
    - Obligacion_evaluar_las_estrategias_de_continuidad_del_negocio_y_corroborar_que_atiendan_los_229b06
    - Obligacion_evaluar_las_estructuras_procesos_y_procedimientos_definidos_por_la_entidad_para__f24339
    - Obligacion_evaluar_los_controles_relacionados_con_la_segregacion_de_funciones_en_el_marco_d_a0b465
    - Obligacion_evaluar_los_procesos_de_gestion_ejecucion_monitoreo_y_control_de_las_operaciones_b79c6c
    - Obligacion_evaluar_los_requisitos_para_la_generacion_de_los_regimenes_informativos_y_verifi_88c928
    - Obligacion_evaluar_los_requisitos_para_los_sistemas_y_aplicaciones_considerando_la_verifica_decc49
    - Obligacion_evaluar_los_resultados_de_la_gestion_de_riesgos_relacionados_con_la_tecnologia_y_ce29fa
    - Obligacion_evaluar_que_la_entidad_formalice_las_relaciones_con_terceras_partes_que_brinden__a3e8fc
    - Obligacion_evaluar_que_se_realicen_procesos_periodicos_de_control_y_depuracion_de_los_siste_230eb2
    - Obligacion_exponer_el_saldo_acreedor_al_cierre_de_cada_periodo_mensual_en_utilidades_divers_ba3911
    - Obligacion_exposicion_adicional_dentro_de_la_informacion_complementaria_correspondiente_cua_a05606
    - Obligacion_frecuencia_mensual_de_informacion__ri_gerc_s1_0ea807
    - Obligacion_gestionar_a_pedido_del_beneficiario_el_cobro_del_echeq_o_documento_electronico_c_6960cd
    - Obligacion_gestionar_activamente_los_activos_afectados_en_garantia__lingeef_3_3_8_9909bd
    - Obligacion_identificacion_y_evaluacion_de_los_riesgos_de_tecnologia_y_seguridad_de_la_infor_3bb47b
    - Obligacion_identificar_principales_deficiencias_en_el_sistema_contable_o_en_sus_controles_q_5892ad
    - Obligacion_implementar_medidas_de_mitigacion_de_riesgos_de_tecnologia_y_seguridad_de_la_inf_80076d
    - Obligacion_implementar_un_sistema_de_almacenamiento_de_echeq_cuya_funcion_sera_registrar_lo_afd1e2
    - Obligacion_imputar_las_ganancias_o_perdidas_actuariales_y_el_rendimiento_de_los_activos_del_dd8e86
    - Obligacion_imputar_los_pasivos_correspondientes_en_las_cuentas_previstas_en_obligaciones_di_c1529f
    - Obligacion_incluir_la_cantidad_de_lotes_incluidos_en_el_archivo_en_el_control_fin_de_archiv_d7d88e
    - Obligacion_indagacion_acerca_del_origen_de_las_partidas_pendientes_de_imputacion__ri_ccna_d_40b2f2
    - Obligacion_informacion_brindada_mensualmente__ceninf_1_1_daf795
    - Obligacion_informacion_mensual_base_de_datos__ceninf_4_1_9adb78
    - Obligacion_informar_depositos_y_obligaciones_a_plazo_considerando_sus_plazos_residuales__ri_ea10ee
    - Obligacion_informar_en_la_nota_una_casilla_de_correo_generica_institucional_para_recibir_la_0bb688
    - Obligacion_informar_la_porcion_de_los_saldos_promedio_de_bonos_del_tesoro_nacional_en_pesos_13a538
    - Obligacion_informar_obligaciones_respecto_de_las_cuales_se_hayan_dispuesto_aumentos_puntual_5b18a1
    - Obligacion_informar_un_subcodigo_por_cada_moneda_o_instrumento_de_deuda_en_que_se_encuentre_f6d5fe
    - Obligacion_integrar_con_claridad_todos_los_rubros_del_formulario_a_maquina_o_a_mano_con_let_ea5275
    - Obligacion_intercambio_de_transacciones_con_las_restantes_camaras_electronicas_de_compensac_6bd93f
    - Obligacion_la_absorcion_de_perdidas_acumuladas_al_cierre_de_cada_ejercicio_a_la_fecha_de_ab_fc1d25
    - Obligacion_la_acreditacion_sera_sin_costo_para_el_originante_y_o_el_depositante_cualquiera__263052
    - Obligacion_la_actividad_de_auditoria_interna_debe_ser_independiente_y_los_auditores_interno_85827c
    - Obligacion_la_agencia_complementaria_de_servicios_financieros_debe_utilizar_en_toda_operaci_056768
    - Obligacion_la_agencia_complementaria_debe_verificar_la_identidad_del_cliente_sobre_la_base__783693
    - Obligacion_la_agregacion_de_datos_sobre_riesgos_debe_realizarse_de_forma_automatizada__adre_0d5a32
    - Obligacion_la_alta_gerencia_recibira_informes_de_la_unidad_de_riesgo_operacional_o_persona__e6f3f4
    - Obligacion_la_asistencia_crediticia_que_exceda_los_respectivos_margenes_de_cobertura_se_imp_0a09a4
    - Obligacion_la_auditoria_interna_debe_aplicar_procedimientos_minimos_de_auditoria_en_oportun_b9deff
    - Obligacion_la_auditoria_interna_debe_evaluar_el_marco_de_gestion_de_ciberincidentes_y_verif_1c7068
    - Obligacion_la_auditoria_interna_debe_evaluar_el_marco_de_gestion_de_la_continuidad_del_nego_be9968
    - Obligacion_la_auditoria_interna_debe_evaluar_el_plan_de_ejercicios_y_pruebas_de_los_planes__ca3c0f
    - Obligacion_la_auditoria_interna_debe_evaluar_el_registro_y_repositorio_de_ciberincidentes___582b9e
    - Obligacion_la_auditoria_interna_debe_evaluar_la_designacion_de_responsables_la_elaboracion__367a2a
    - Obligacion_la_auditoria_interna_debe_evaluar_la_implementacion_de_un_registro_del_seguimien_0a732a
    - Obligacion_la_auditoria_interna_debe_evaluar_la_proteccion_de_los_registros_de_auditoria_en_3d0e87
    - Obligacion_la_auditoria_interna_debe_evaluar_las_politicas_para_la_gestion_de_ciberincident_f6a516
    - Obligacion_la_auditoria_interna_debe_evaluar_los_controles_en_el_mantenimiento_configuracio_c65f62
    - Obligacion_la_auditoria_interna_debe_evaluar_los_controles_fisicos_implementados_en_los_dis_16c98e
    - Obligacion_la_auditoria_interna_debe_evaluar_los_controles_relacionados_con_el_comprobante__c361e7
    - Obligacion_la_auditoria_interna_debe_evaluar_los_resultados_de_las_pruebas_de_los_planes_de_a45d06
    - Obligacion_la_auditoria_interna_debe_examinar_el_proceso_de_gestion_del_riesgo_de_modelo_co_7d6311
    - Obligacion_la_auditoria_interna_debe_mantener_una_adecuada_documentacion_sobre_las_tareas_l_0393d0
    - Obligacion_la_auditoria_interna_debe_relevar_la_infraestructura_tecnologica_de_la_entidad_p_71259b
    - Obligacion_la_auditoria_interna_debe_revisar_regularmente_la_implementacion_y_la_eficacia_d_fa677b
    - Obligacion_la_auditoria_interna_debe_verificar_que_la_entidad_haya_establecido_y_mantenga_u_b93063
    - Obligacion_la_auditoria_interna_debe_verificar_que_se_mantenga_un_registro_detallado_de_los_d45c02
    - Obligacion_la_auditoria_interna_debera_aplicar_un_enfoque_basado_en_riesgos_que_considere_l_26cc7b
    - Obligacion_la_auditoria_interna_debera_contar_con_un_codigo_de_etica_aprobado_por_el_direct_88aca7
    - Obligacion_la_auditoria_interna_debera_efectuar_procedimientos_dirigidos_a_identificar_y_ev_97919d
    - Obligacion_la_auditoria_interna_no_debe_duplicar_los_procesos_de_gestion_del_riesgo_de_mode_5a68a1
    - Obligacion_la_base_de_sancionados_vigentes_sera_actualizada_diariamente_en_la_medida_en_que_3535b2
    - Obligacion_la_boleta_debera_incluir_sello_de_la_casa_receptora_salvo_que_se_utilicen_escrit_3efdc9
    - Obligacion_la_cabecera_de_archivo_debe_desagregar_la_informacion_dependiendo_si_es_efectuad_b8f870
    - Obligacion_la_cabecera_de_archivo_debe_incluir_los_campos_de_fecha_de_presentacion_hora_de__9a73bd
    - Obligacion_la_cac_debe_incluir_el_texto_certificacion_para_ejercer_acciones_civiles_numero__42b7ef
    - Obligacion_la_cec_debe_extraer_las_imagenes_requeridas_del_reservorio_de_imagenes_generar_u_c4a8ea
    - Obligacion_la_cec_solicitara_a_las_entidades_giradas_que_informen_el_monto_total_a_percibir_4ceb3d
    - Obligacion_la_certificacion_debera_incluir_que_en_su_elaboracion_se_aplicaron_las_disposici_721974
    - Obligacion_la_certificacion_para_acciones_civiles_cac_debe_contener_los_datos_especificados_f0f2fc
    - Obligacion_la_condicion_ad_referendum_de_la_aprobacion_del_bcra_debera_constar_en_los_docum_3b14ce
    - Obligacion_la_condicion_de_origen_de_los_cheques_podra_verificarse_mediante_la_declaracion__7f6b6d
    - Obligacion_la_contabilizacion_de_las_previsiones_que_resulten_de_la_determinacion_final_de__a7fb09
    - Obligacion_la_contrapartida_del_ajuste_de_reclasificacion_debe_registrarse_en_resultados_de_d404db
    - Obligacion_la_contrapartida_del_ajuste_por_reclasificacion_debe_registrarse_en_ingresos_fin_876b11
    - Obligacion_la_copia_de_la_declaracion_jurada_sera_entregada_al_presentante_con_la_constanci_be0243
    - Obligacion_la_copia_original_de_la_solicitud_sera_retenida_por_el_acreedor_aunque_el_presta_9cfbf3
    - Obligacion_la_correspondencia_de_los_datos_debe_examinarse_periodicamente_y_contrastarse_co_4b3438
    - Obligacion_la_cuantificacion_del_riesgo_de_credito_de_contraparte_debe_incluir_el_seguimien_fd2c3f
    - Obligacion_la_cuenta_ajuste_por_reclasificacion_debe_utilizarse_en_los_casos_de_los_incisos_fb33c9
    - Obligacion_la_cuenta_de_corresponsalia_con_fijacion_de_limites_de_credito_plazos_e_interese_0c8e71
    - Obligacion_la_cuenta_debe_estar_operativa_el_dia_habil_bancario_siguiente_a_aquel_en_que_se_dc103f
    - Obligacion_la_declaracion_jurada_debe_ser_remitida_al_bcra_mediante_una_unica_nota_suscript_755c1b
    - Obligacion_la_definicion_debe_asegurar_que_la_estrategia_y_los_limites_de_riesgo_de_las_uni_84c680
    - Obligacion_la_definicion_debe_incluir_antecedentes_y_supuestos_que_contemplen_los_planes_de_01bee4
    - Obligacion_la_definicion_debe_incluir_los_motivos_para_asumir_o_evitar_ciertos_tipos_de_rie_c40877
    - Obligacion_la_definicion_debe_ser_prospectiva_y_de_ser_posible_estar_sujeta_a_escenarios_y__a681b3
    - Obligacion_la_definicion_efectiva_del_apetito_y_la_tolerancia_al_riesgo_debe_ser_facil_de_c_1438d3
    - Obligacion_la_determinacion_de_la_estructura_de_plazos_residuales_del_mes_anterior_para_los_616929
    - Obligacion_la_determinacion_de_la_posicion_bimestral_sera_efectuada_por_esta_institucion_so_61a368
    - Obligacion_la_determinacion_de_la_retribucion_siempre_se_efectuara_en_forma_mensual__efemin_9d8845
    - Obligacion_la_determinacion_del_importe_sujeto_a_exigencia_se_efectuara_mediante_la_formula_77e4d1
    - Obligacion_la_deuda_debe_calcularse_a_la_fecha_en_que_el_comprador_deba_depositar_el_saldo__48a03f
    - Obligacion_la_deuda_total_se_incrementa_con_los_gastos_de_seguro_soportados_por_el_acreedor_e496a2
    - Obligacion_la_direccion_es_responsable_de_la_generacion_de_los_canales_necesarios_para_que__acc683
    - Obligacion_la_distribucion_de_dividendos_y_o_constitucion_de_reservas_se_efectuaran_sobre_l_e1993c
    - Obligacion_la_documentacion_debe_contar_en_su_caso_con_certificacion_notarial_y_presentarse_6ec026
    - Obligacion_la_documentacion_debera_contener_para_cada_actividad_de_cada_ciclo_de_la_entidad_3a3847
    - Obligacion_la_documentacion_debera_estar_preparada_con_el_suficiente_detalle_de_manera_que__cc518e
    - Obligacion_la_documentacion_del_exterior_debera_estar_acompanada_de_su_traduccion_al_castel_b6f062
    - Obligacion_la_documentacion_del_exterior_que_se_obtenga_para_conformar_el_legajo_de_los_cli_1f1da1
    - Obligacion_la_documentacion_indicada_podra_ser_presentada_directamente_por_el_solicitante_o_82c8ba
    - Obligacion_la_entidad_administradora_debe_realizar_la_gestion_de_cobro_de_todo_importe_inst_cd80ac
    - Obligacion_la_entidad_administradora_debe_realizar_la_totalidad_de_los_actos_tendientes_a_l_19f11b
    - Obligacion_la_entidad_debe_dar_de_baja_los_cheques_cancelados_dentro_de_los_2_dias_habiles__9ef6c3
    - Obligacion_la_entidad_debe_remitir_dentro_de_los_plazos_dispuestos_las_formulas_3830c_3831c_d69d77
    - Obligacion_la_entidad_financiera_debe_efectuar_la_retencion_impositiva_de_acuerdo_con_la_re_7af60c
    - Obligacion_la_entidad_financiera_podra_efectuar_debitos_en_las_cuentas_especiales_de_regula_5e975e
    - Obligacion_la_estrategia_debe_alcanzar_las_actividades_con_exposicion_significativa_al_ries_b403d5
    - Obligacion_la_estrategia_debe_considerar_los_aspectos_coyunturales_de_la_economia_del_pais__be9306
    - Obligacion_la_estrategia_debe_enunciar_la_politica_de_riesgo_de_credito_que_llevara_adelant_ff9727
    - Obligacion_la_estrategia_debe_establecer_las_pautas_generales_que_seguira_la_entidad_para_g_eb9092
    - Obligacion_la_estrategia_debe_establecer_los_objetivos_que_guien_la_actividad_de_otorgamien_1460a6
    - Obligacion_la_estrategia_debe_identificar_el_tipo_de_mercado_al_cual_orientara_su_actividad_a3f417
    - Obligacion_la_estrategia_debe_identificar_los_niveles_de_riesgo_y_rendimiento_aceptables_da_9a87b8
    - Obligacion_la_estrategia_debe_incluir_objetivos_cuantitativos_y_cualitativos_que_dirijan_la_b68e9a
    - Obligacion_la_estrategia_debe_reflejar_la_tolerancia_al_riesgo_y_la_rentabilidad_esperada_p_71bdb6
    - Obligacion_la_estrategia_debe_ser_evaluada_y_actualizada_periodicamente__lingeef_2_1_3_1_087020
    - Obligacion_la_estrategia_debe_ser_viable_a_largo_plazo_y_a_traves_de_los_ciclos_economicos__dc01bb
    - Obligacion_la_estrategia_debera_definir_con_claridad_la_estructura_administrativa_relaciona_69173e
    - Obligacion_la_estrategia_debera_incluir_el_establecimiento_de_limites_que_reflejen_el_nivel_6fa292
    - Obligacion_la_estrategia_debera_incluir_la_realizacion_de_pruebas_de_estres__lingeef_4_2_1__391aa5
    - Obligacion_la_etiqueta_identificadora_debe_contener_nombre_de_la_entidad_financiera_numero__5fd8c6
    - Obligacion_la_evaluacion_de_la_capacidad_de_pago_incorporada_en_el_resultado_de_los_metodos_a2ec99
    - Obligacion_la_evaluacion_de_la_infraestructura_tecnologica_con_todos_sus_componentes_y_el_f_192928
    - Obligacion_la_evaluacion_de_los_controles_del_procesamiento_de_transacciones_debe_comprende_19dc44
    - Obligacion_la_evaluacion_de_los_controles_del_procesamiento_de_transacciones_debe_comprende_4f84cb
    - Obligacion_la_evaluacion_de_los_controles_del_procesamiento_de_transacciones_debe_comprende_88cbd6
    - Obligacion_la_evaluacion_de_los_controles_del_procesamiento_de_transacciones_debe_comprende_a34f50
    - Obligacion_la_evaluacion_de_los_controles_del_procesamiento_de_transacciones_debe_comprende_b18e05
    - Obligacion_la_evaluacion_del_ambiente_de_computacion_debera_comprender_los_siguientes_aspec_9c100b
    - Obligacion_la_evaluacion_del_control_interno_de_los_ciclos_de_la_entidad_debera_ser_documen_e4cd14
    - Obligacion_la_evaluacion_del_cumplimiento_de_las_politicas_debe_incluir_el_seguimiento_de_l_a829e4
    - Obligacion_la_evaluacion_del_cumplimiento_de_las_politicas_debe_incluir_la_evaluacion_de_la_968bda
    - Obligacion_la_evaluacion_del_cumplimiento_de_las_politicas_debe_incluir_la_revision_del_tra_08f52d
    - Obligacion_la_evaluacion_del_cumplimiento_de_las_politicas_debe_incluir_la_verificacion_del_a00ea8
    - Obligacion_la_evaluacion_del_cumplimiento_de_las_politicas_debe_incluir_revisiones_de_alto__e3c8ff
    - Obligacion_la_exigencia_de_efectivo_minimo_surgira_de_aplicar_las_tasas_establecidas_sobre__46f037
    - Obligacion_la_expedicion_de_la_cac_bloqueara_el_registro_del_echeq_en_el_sistema_de_almacen_9a0e5d
    - Obligacion_la_funcion_de_auditoria_interna_debera_ser_ejercida_por_personal_en_relacion_de__c5f85a
    - Obligacion_la_funcion_de_autorizacion_debe_considerar_como_minimo_disponibilidad_de_fondos__f94fc2
    - Obligacion_la_funcion_de_gestion_del_riesgo_operacional_debera_trabajar_junto_con_otras_fun_140378
    - Obligacion_la_ganancia_o_perdida_acumulada_anteriormente_reconocida_en_ori_se_debe_reclasif_4df6e9
    - Obligacion_la_gerencia_de_la_entidad_debe_emitir_una_expresa_manifestacion_acerca_de_la_int_698be9
    - Obligacion_la_gerencia_de_operaciones_de_tesoro_subgerencia_de_tesoreria_del_bcra_debe_dist_9d1bd0
    - Obligacion_la_gerencia_de_operaciones_de_tesoro_visualizara_los_debitos_mep_de_las_entidade_358be8
    - Obligacion_la_gerencia_debe_considerar_como_se_combinan_sus_lineas_de_negocio_y_las_caracte_6ad55a
    - Obligacion_la_gestion_de_riesgos_de_tecnologia_y_seguridad_de_la_informacion_debe_hacer_uso_3454fd
    - Obligacion_la_gestion_de_riesgos_de_tecnologia_y_seguridad_de_la_informacion_debe_ser_regul_c00cce
    - Obligacion_la_gestion_de_riesgos_de_tecnologia_y_seguridad_de_la_informacion_debe_ser_revis_1c2255
    - Obligacion_la_gestion_del_riesgo_de_modelo_para_las_medidas_del_rtici_debe_seguir_un_enfoqu_60e654
    - Obligacion_la_imputacion_de_las_financiaciones_de_los_puntos_7_2_1_y_7_2_2_se_ajustara_a_lo_573db3
    - Obligacion_la_incorporacion_de_las_leyendas_que_correspondan_se_formulara_con_ajuste_a_lo_e_5ac12c
    - Obligacion_la_incorporacion_de_las_leyendas_que_correspondan_se_formulara_con_ajuste_a_lo_e_79c202
    - Obligacion_la_incorporacion_de_las_leyendas_que_correspondan_se_formulara_con_ajuste_a_lo_e_ee17fc
    - Obligacion_la_incorporacion_de_un_registro_adicional_en_ordenes_de_transferencia_de_pago_a__ded407
    - Obligacion_la_incorporacion_de_un_registro_adicional_en_ordenes_de_transferencia_entre_clie_0f3cda
    - Obligacion_la_incorporacion_de_un_registro_adicional_en_registros_individuales_de_devolucio_25fffc
    - Obligacion_la_informacion_basica_a_considerar_en_la_evaluacion_de_solvencia_comprende_la_co_7e87f9
    - Obligacion_la_informacion_basica_a_considerar_en_la_evaluacion_de_solvencia_comprende_la_co_abe52b
    - Obligacion_la_informacion_de_consultas_puntuales_sera_actualizada_mensualmente__ceninf_4_2__8e1199
    - Obligacion_la_informacion_debe_procesarse_de_manera_sistematica_es_decir_en_un_orden_y_de_u_8e12a7
    - Obligacion_la_informacion_debe_ser_transmitida_en_archivos_cuya_estructura_contenido_y_form_c9401a
    - Obligacion_la_informacion_disponible_para_cada_entidad_sera_actualizada_mensualmente__cenin_373615
    - Obligacion_la_informacion_que_surja_del_legajo_unico_financiero_y_economico_sera_considerad_72191a
    - Obligacion_la_informacion_recibida_debe_servir_de_base_para_la_clasificacion_de_los_deudore_aaa3c0
    - Obligacion_la_informacion_se_expresara_en_cantidad_y_monto_en_todos_los_casos_que_fuera_pos_60ad92
    - Obligacion_la_informacion_se_integrara_con_los_saldos_del_mes_bajo_analisis__ri_gerc_s1_0a0d7b
    - Obligacion_la_informacion_se_presentara_teniendo_en_cuenta_las_disposiciones_vigentes_a_nov_9cf3b0
    - Obligacion_la_informacion_sobre_la_composicion_y_calidad_de_las_distintas_carteras_debe_per_27ee2e
    - Obligacion_la_integridad_la_calidad_el_detalle_y_la_oportunidad_de_la_informacion_en_los_si_0ed729
    - Obligacion_la_introduccion_de_datos_debe_automatizarse_a_fin_de_reducir_errores_administrat_b38449
    - Obligacion_la_labor_de_auditoria_interna_debe_realizarse_conforme_la_normativa_vigente_en_l_8fbeed
    - Obligacion_la_liquidacion_se_efectuara_considerando_por_separado_cada_cuenta_de_moneda_extr_cebca2
    - Obligacion_la_medicion_del_riesgo_de_credito_debe_tomar_en_cuenta_diversos_factores_como_la_2fe7b7
    - Obligacion_la_medicion_del_riesgo_de_credito_debe_tomar_en_cuenta_el_perfil_de_la_evolucion_c74b08
    - Obligacion_la_medicion_del_riesgo_de_credito_debe_tomar_en_cuenta_el_riesgo_de_incumplimien_9e85c2
    - Obligacion_la_medicion_del_riesgo_de_credito_debe_tomar_en_cuenta_la_existencia_de_mitigado_bdbc09
    - Obligacion_la_metodologia_e_informacion_empleada_para_sustituir_la_demostracion_de_ingresos_0793a2
    - Obligacion_la_nota_de_designacion_de_usuarios_debe_ingresarse_a_traves_de_la_gerencia_de_se_df21f5
    - Obligacion_la_nota_debe_contemplar_el_nombre_y_apellido_de_las_personas_designadas_para_ope_66ea39
    - Obligacion_la_nota_debe_especificar_el_rol_asignado_a_cada_usuario_rol_operador_o_rol_aprob_283e29
    - Obligacion_la_nota_debe_incluir_la_casilla_de_correo_laboral_de_cada_usuario_para_informar__b27805
    - Obligacion_la_obligacion_de_consignar_el_numero_de_identificacion_personal_o_cuit_o_cdi_seg_0be8d3
    - Obligacion_la_obligacion_de_consignar_el_numero_de_identificacion_personal_o_cuit_o_cdi_y_l_5132b7
    - Obligacion_la_operatoria_del_cedip_se_ajustara_a_lo_dispuesto_en_estas_normas_y_demas_regla_b198ca
    - Obligacion_la_opinion_sobre_cada_aspecto_debera_ser_efectuada_dentro_de_las_siguientes_cate_9ef479
    - Obligacion_la_pagina_de_internet_del_bcra_sera_actualizada_diariamente_con_la_informacion_d_2a61e6
    - Obligacion_la_periodicidad_de_la_cuota_debera_ser_mensual__manori_1_1_5_7_2fcea0
    - Obligacion_la_persona_juridica_debera_presentar_en_la_casa_en_la_cual_este_radicada_la_cuen_41e187
    - Obligacion_la_planificacion_de_auditorias_externas_debe_estar_formalizada_por_escrito_final_2b84bf
    - Obligacion_la_plantilla_de_perforacion_debera_ajustarse_a_alguno_de_los_modelos_homologados_6c2770
    - Obligacion_la_politica_debe_especificar_las_funciones_de_la_gerencia_y_designar_quien_es_re_c52478
    - Obligacion_la_politica_debe_prever_un_proceso_jerarquico_para_determinar_que_el_riesgo_de_m_8d69e9
    - Obligacion_la_posicion_bimestral_sera_determinada_sobre_la_base_de_los_datos_informados_par_4e8f32
    - Obligacion_la_posicion_neta_se_determinara_considerando_el_registro_horario_o_equivalente_c_f00051
    - Obligacion_la_presentacion_se_efectua_a_traves_de_servicios_generales_mesa_de_entrada_y_se__c7b946
    - Obligacion_la_recepcion_de_billetes_deteriorados_se_atendera_de_acuerdo_con_el_cronograma_d_9a84de
    - Obligacion_la_recepcion_de_solicitudes_se_realizara_en_horario_de_10_00_a_12_00_en_la_ubica_8ead9f
    - Obligacion_la_reserva_normativa_especial_por_aplicacion_por_primera_vez_de_las_niif_debera__e9f917
    - Obligacion_la_revision_interna_debe_detectar_de_manera_temprana_los_creditos_con_mayor_ries_6b8a76
    - Obligacion_la_revision_interna_debe_incluir_un_proceso_independiente_y_bien_definido_de_rev_2b6e15
    - Obligacion_la_sefyc_solicitara_la_adecuacion_de_la_sucursal_en_el_regimen_informativo_perti_110a75
    - Obligacion_la_segunda_linea_de_defensa_debe_revisar_la_relevancia_y_consistencia_de_la_impl_c29fd4
    - Obligacion_la_sociedad_del_estado_casa_de_moneda_argentina_es_responsable_de_la_acunacion_d_277d21
    - Obligacion_la_solicitud_debe_incluir_informacion_sobre_el_capital_que_se_aportara_inicialme_64f8f7
    - Obligacion_la_solicitud_se_remitira_acompanada_de_la_formula_a_traves_de_la_cual_la_asociac_4e5900
    - Obligacion_la_subgerencia_de_laboratorio_proveera_un_catalogo_con_las_imagenes_de_los_bille_67196a
    - Obligacion_la_sumatoria_de_las_operaciones_con_valor_razonable_negativo_al_cierre_de_cada_m_48c64a
    - Obligacion_la_sumatoria_de_las_operaciones_con_valor_razonable_negativo_al_cierre_de_cada_m_dd7e9c
    - Obligacion_la_sumatoria_de_las_operaciones_con_valor_razonable_positivo_al_cierre_de_cada_m_72fe32
    - Obligacion_la_sumatoria_de_las_operaciones_con_valor_razonable_positivo_al_cierre_de_cada_m_b4298b
    - Obligacion_la_superintendencia_de_entidades_financieras_y_cambiarias_comunica_a_la_entidad__9a1e9f
    - Obligacion_la_superintendencia_de_entidades_financieras_y_cambiarias_se_expide_dentro_de_lo_a01f0b
    - Obligacion_la_tasa_de_interes_utilizada_para_el_descuento_debe_extraerse_de_la_curva_cupon__11fa73
    - Obligacion_la_tercera_linea_de_defensa_debe_revisar_el_diseno_y_la_implementacion_de_los_si_f1a6ec
    - Obligacion_la_tercera_linea_de_defensa_debe_revisar_los_procesos_de_validacion_para_garanti_abecab
    - Obligacion_la_transmision_de_los_archivos_electronicos_de_los_rechazos_se_realizara_en_el_h_78c9ab
    - Obligacion_la_unidad_o_persona_responsable_de_implementar_el_programa_debe_organizar_la_dis_c8ca70
    - Obligacion_la_validacion_de_los_metodos_de_medicion_del_rtici_y_la_evaluacion_del_riesgo_de_3b4343
    - Obligacion_la_valuacion_determinada_conforme_a_los_metodos_establecidos_tasacion_precio_de__7d46f8
    - Obligacion_labrar_un_acta_de_retencion_formula_no_4394_integrada_unicamente_con_medios_info_e0c92a
    - Obligacion_las_aplicaciones_se_informaran_netas_de_las_previsiones_por_riesgos_de_incobrabi_1d92bb
    - Obligacion_las_asociaciones_de_profesionales_constituidas_de_acuerdo_con_un_tipo_societario_28aba4
    - Obligacion_las_autorizaciones_estan_condicionadas_al_cumplimiento_de_exigencias_que_se_espe_d37394
    - Obligacion_las_boletas_que_se_empleen_deberan_contener_como_minimo_los_siguientes_datos_nom_764674
    - Obligacion_las_calificaciones_de_riesgo_internas_deben_facilitar_la_identificacion_y_medici_0eeff5
    - Obligacion_las_calificaciones_deben_ser_revisadas_y_actualizadas_periodicamente_en_particul_a033e5
    - Obligacion_las_caracteristicas_y_funcionamiento_del_sistema_interno_de_calificacion_deben_e_d1e68f
    - Obligacion_las_cec_se_comunican_entre_si_para_intercambiar_transacciones_cruzadas_permitien_788332
    - Obligacion_las_clausulas_contractuales_de_rescision_deberan_contemplar_explicitamente_la_li_f7df31
    - Obligacion_las_clausulas_del_contrato_de_credito_que_no_esten_previstas_en_el_modelo_minimo_7379c8
    - Obligacion_las_clausulas_del_contrato_deberan_adecuarse_en_funcion_de_lo_establecido_en_las_d4f828
    - Obligacion_las_clausulas_del_contrato_que_no_esten_previstas_en_la_seccion_deben_ajustarse__00534a
    - Obligacion_las_comisiones_o_cargos_por_servicios_adicionales_deben_constar_en_el_anexo_al_t_0ce965
    - Obligacion_las_compras_y_ventas_a_termino_de_moneda_extranjera_y_demas_operaciones_de_instr_0e5425
    - Obligacion_las_conclusiones_se_volcaran_en_la_medida_de_su_significatividad_en_un_informe_p_18a40e
    - Obligacion_las_conclusiones_seran_informadas_en_un_informe_por_ciclo_que_se_elevara_al_comi_d491a1
    - Obligacion_las_costas_y_gastos_que_origine_el_deudor_con_motivo_del_incumplimiento_quedan_a_0c0101
    - Obligacion_las_cuentas_de_ingresos_financieros_resultado_por_venta_o_baja_en_cuentas_se_uti_22e196
    - Obligacion_las_cuentas_destino_se_regiran_por_las_normas_establecidas_para_cuentas_corrient_e2438f
    - Obligacion_las_declaraciones_juradas_deberan_ser_integradas_por_duplicado__ayccef_7_1_2_1_04a1ec
    - Obligacion_las_definiciones_de_la_seccion_1_de_las_normas_sistema_nacional_de_pagos_transfe_a03ff1
    - Obligacion_las_denuncias_formuladas_conforme_a_los_procedimientos_del_punto_8_7_tendran_vig_507074
    - Obligacion_las_diferencias_de_cambio_originadas_en_operaciones_a_termino_de_moneda_extranje_0cc15c
    - Obligacion_las_diferencias_respecto_de_los_saldos_determinados_segun_el_marco_contable_ante_3d2334
    - Obligacion_las_disposiciones_establecidas_para_los_depositos_en_caja_de_ahorros_en_los_punt_6a2162
    - Obligacion_las_disposiciones_establecidas_para_los_depositos_en_caja_de_ahorros_y_cuenta_co_c2b773
    - Obligacion_las_entidades_deberan_extender_la_pertinente_constancia_del_deposito_expedida_me_9bc962
    - Obligacion_las_entidades_financieras_deben_contar_con_politicas_y_procedimientos_para_garan_73a677
    - Obligacion_las_entidades_financieras_deben_contar_con_un_proceso_interno_de_controles_exame_d92833
    - Obligacion_las_entidades_financieras_deben_contar_con_un_proceso_interno_integrado_y_global_33d049
    - Obligacion_las_entidades_financieras_deben_contar_con_un_proceso_que_establezca_objetivos_d_8e7ee2
    - Obligacion_las_entidades_financieras_deben_contar_con_un_proceso_que_relacione_el_capital_e_4ad3dc
    - Obligacion_las_entidades_financieras_deben_demostrar_que_sus_objetivos_internos_de_capital__ee5190
    - Obligacion_las_entidades_financieras_deben_desarrollar_un_proceso_integral_para_la_gestion__9e2b67
    - Obligacion_las_entidades_financieras_deben_evaluar_sistematicamente_la_eficacia_de_las_tecn_650c19
    - Obligacion_las_entidades_financieras_deben_realizar_un_analisis_de_los_requerimientos_de_ca_b1d637
    - Obligacion_las_entidades_financieras_pagadoras_pueden_prever_sin_costo_para_el_beneficiario_f21849
    - Obligacion_las_evaluaciones_de_eficacia_de_controles_y_procedimientos_tambien_deberan_reali_2f6d0f
    - Obligacion_las_evaluaciones_de_la_suficiencia_de_capital_para_la_cobertura_del_rtici_deben__6297da
    - Obligacion_las_evaluaciones_de_la_suficiencia_de_capital_para_la_cobertura_del_rtici_deben__88fdc9
    - Obligacion_las_evaluaciones_de_la_suficiencia_de_capital_para_la_cobertura_del_rtici_deben__904bbe
    - Obligacion_las_evaluaciones_de_la_suficiencia_de_capital_para_la_cobertura_del_rtici_deben__91d5fe
    - Obligacion_las_evaluaciones_de_la_suficiencia_de_capital_para_la_cobertura_del_rtici_deben__c856ec
    - Obligacion_las_evaluaciones_de_la_suficiencia_de_capital_para_la_cobertura_del_rtici_deben__cb8657
    - Obligacion_las_evaluaciones_de_la_suficiencia_de_capital_para_la_cobertura_del_rtici_deben__e4f5df
    - Obligacion_las_evaluaciones_de_la_suficiencia_de_capital_para_la_cobertura_del_rtici_deben__f0dd43
    - Obligacion_las_evaluaciones_de_la_suficiencia_de_capital_para_la_cobertura_del_rtici_deben__f724cc
    - Obligacion_las_exposiciones_a_sucursales_de_entidades_financieras_se_deben_asignar_en_el_pr_ace7d3
    - Obligacion_las_exposiciones_a_sucursales_de_entidades_financieras_se_deben_asignar_en_el_se_c86ad3
    - Obligacion_las_fajas_deben_ser_intervenidas_con_fecha_sello_y_firmas_del_personal_responsab_0aaf1e
    - Obligacion_las_financiaciones_totalmente_cubiertas_con_garantias_preferidas_estaran_sujetas_85eb3a
    - Obligacion_las_firmas_de_las_autoridades_extranjeras_intervinientes_deberan_estar_certifica_42366a
    - Obligacion_las_firmas_de_las_autoridades_extranjeras_intervinientes_deberan_estar_certifica_ad4acd
    - Obligacion_las_firmas_de_los_auditores_externos_en_la_documentacion_deben_presentarse_debid_868a6c
    - Obligacion_las_firmas_de_los_profesionales_cuya_intervencion_se_requiere_deberan_estar_lega_9f95d4
    - Obligacion_las_firmas_de_los_profesionales_cuya_intervencion_se_requiere_en_las_disposicion_4390e0
    - Obligacion_las_formas_de_retribucion_adicionales_deberan_especificarse_claramente_y_de_mane_3dfa5d
    - Obligacion_las_funciones_respectivas_deben_identificar_analizar_y_documentar_las_personas_t_99ae25
    - Obligacion_las_funciones_respectivas_deberan_evaluar_periodicamente_la_eficacia_de_los_cont_873e7f
    - Obligacion_las_herramientas_prospectivas_de_medicion_deben_comprender_aquellas_vulnerabilid_b18b50
    - Obligacion_las_herramientas_prospectivas_deben_identificar_necesidades_derivadas_de_los_egr_81a7d0
    - Obligacion_las_herramientas_prospectivas_deben_ser_capaces_de_identificar_descalces_de_fond_55ef4b
    - Obligacion_las_imputaciones_de_activos_subyacentes_se_mantendran_en_las_cuentas_correspondi_e49594
    - Obligacion_las_imputaciones_se_realizaran_en_la_cuenta_correccion_de_valor_por_perdidas_cre_ae06c6
    - Obligacion_las_modificaciones_en_las_condiciones_o_importe_de_las_comisiones_o_gastos_cuyo__3337f7
    - Obligacion_las_operaciones_a_termino_asimilables_a_operaciones_de_pase_recibiran_el_tratami_6754e9
    - Obligacion_las_operaciones_de_los_entes_a_que_refieren_los_incisos_i_ii_y_iii_del_primer_pa_66f65c
    - Obligacion_las_partidas_400dd_y_410dd_se_informaran_conforme_las_disposiciones_habituales___02db3d
    - Obligacion_las_partidas_4520xx_incluiran_a_partir_del_21_06_18_de_corresponder_la_aplicacio_29b3dc
    - Obligacion_las_partidas_correspondientes_al_periodo_comprendido_entre_el_1_y_el_17_8_se_pre_035063
    - Obligacion_las_partidas_de_integracion_diaria_y_los_saldos_de_depositos_en_pesos_en_cuentas_de2b00
    - Obligacion_las_partidas_fuera_de_balance_se_informaran_para_fines_de_control_estadisticos_y_8c92e1
    - Obligacion_las_partidas_previstas_en_el_punto_10_1_2_mantendran_las_correlaciones_con_cuent_600b1e
    - Obligacion_las_partidas_que_componen_la_integracion_se_informaran_de_acuerdo_con_las_dispos_5419fc
    - Obligacion_las_partidas_vinculadas_con_la_exigencia_y_otras_de_calculo_mensual_se_presentar_4beec0
    - Obligacion_las_posiciones_denominadas_en_diferentes_monedas_pueden_estar_expuestas_al_rtici_7eee18
    - Obligacion_las_posiciones_por_opciones_de_futuros_se_deberan_medir_multiplicando_el_coefici_a1e37f
    - Obligacion_las_posiciones_restantes_en_el_registro_de_motivos_de_rechazo_se_completaran_con_81a263
    - Obligacion_las_presentaciones_o_actualizaciones_de_datos_y_declaraciones_juradas_pueden_rea_b5873a
    - Obligacion_las_previsiones_deberan_aumentarse_como_minimo_de_manera_que_el_valor_contable_n_2b9349
    - Obligacion_las_propiedades_de_inversion_medidas_a_valor_razonable_deberan_registrarse_en_la_ad3078
    - Obligacion_las_propuestas_para_utilizar_nuevos_tipos_de_instrumentos_o_nuevas_estrategias_i_ef3309
    - Obligacion_las_pruebas_de_estres_complementan_a_otras_herramientas_de_gestion_y_tienen_un_r_a5ef62
    - Obligacion_las_pruebas_de_estres_deben_facilitar_el_desarrollo_de_planes_de_contingencia_o__aa8af4
    - Obligacion_las_pruebas_de_estres_para_el_rtici_deben_desempenar_un_papel_importante_en_la_c_e7f24d
    - Obligacion_las_pruebas_deben_abarcar_desde_analisis_de_sensibilidad_simples_hasta_ejercicio_e28ec8
    - Obligacion_las_registraciones_de_operaciones_de_pase_deben_realizarse_de_acuerdo_con_las_pa_cd3adf
    - Obligacion_las_restantes_partidas_se_identificaran_segun_su_moneda_de_origen_de_acuerdo_con_970406
    - Obligacion_las_subvenciones_del_gobierno_vinculadas_con_activos_en_los_terminos_de_la_nic_2_fff991
    - Obligacion_las_sumas_representadas_por_los_billetes_en_buen_uso_que_las_entidades_financier_fe9f36
    - Obligacion_las_tecnicas_de_medicion_var_y_pruebas_de_estres_deben_evolucionar_a_medida_que__257c7a
    - Obligacion_las_transferencias_deben_estar_identificadas_con_las_denominaciones_pago_con_tra_73507f
    - Obligacion_las_transferencias_inmediatas_estan_alcanzadas_por_el_esquema_de_precios_detalla_29b6fd
    - Obligacion_las_transmisiones_de_acciones_o_integraciones_de_aportes_irrevocables_deberan_co_30fa2e
    - Obligacion_las_unidades_de_negocio_deben_establecer_controles_apropiados_para_mitigar_los_r_8c85a9
    - Obligacion_las_unidades_de_negocio_deben_evaluar_el_diseno_y_efectividad_de_los_controles_m_a387cc
    - Obligacion_las_unidades_de_negocio_deben_identificar_y_evaluar_los_riesgos_operacionales_si_dd0744
    - Obligacion_las_variables_tenidas_en_cuenta_en_los_modelos_de_evaluacion_que_no_hayan_sido_p_a649f0
    - Obligacion_las_variaciones_de_las_tasas_de_interes_sobre_las_que_se_basan_los_limites_deben_f9f700
    - Obligacion_las_variaciones_en_el_valor_que_surjan_del_modelo_de_revaluacion_se_imputaran_en_cd0236
    - Obligacion_las_variaciones_en_el_valor_razonable_de_propiedades_de_inversion_deben_registra_19a8f9
    - Obligacion_las_variaciones_positivas_generadas_por_revaluacion_se_registraran_con_contrapar_a31c8b
    - Obligacion_las_versiones_de_consulta_de_la_cac_a_traves_de_internet_deberan_corresponderse__08b18e
    - Obligacion_las_versiones_de_consulta_de_la_certificacion_para_acciones_civiles_cac_disponib_75adcc
    - Obligacion_liquidacion_de_saldos_en_las_cuentas_corrientes_abiertas_en_el_bcra__snp_tr_1_1__96602f
    - Obligacion_llevar_permanentemente_la_posicion_de_los_activos_en_garantia__lingeef_3_3_8_306cc1
    - Obligacion_llevar_un_registro_de_las_cuentas_abiertas_que_incluya_como_minimo_las_identidad_7b5226
    - Obligacion_los_10_diez_cientos_que_conforman_el_millar_deberan_estar_termosellados_con_peli_dbc065
    - Obligacion_los_activos_financieros_transferidos_no_dados_de_baja_se_informaran_por_un_impor_376468
    - Obligacion_los_ajustes_derivados_de_la_observacion_de_documentos_compensados_con_antiguedad_89685e
    - Obligacion_los_alcances_y_las_definiciones_referidas_a_sujetos_alcanzados_cuentas_y_datos_a_771368
    - Obligacion_los_analisis_de_sensibilidad_y_de_escenarios_deben_desarrollarse_regularmente_at_626d5e
    - Obligacion_los_aportes_irrevocables_deben_cumplir_requisitos_haber_sido_aprobados_por_la_as_0717a2
    - Obligacion_los_archivos_a_intercambiar_electronicamente_deberan_tener_la_estructura_especif_f297e5
    - Obligacion_los_aspectos_particulares_de_cheques_generados_por_medios_electronicos_deberan_a_84f4e8
    - Obligacion_los_aspectos_particulares_de_cheques_generados_por_medios_electronicos_echeq_deb_b20033
    - Obligacion_los_billetes_clasificados_deben_acondicionarse_en_paquetes_de_1000_unidades_del__7c68b2
    - Obligacion_los_billetes_de_100_de_la_serie_65_180_001_a_llevaran_facsimiles_de_las_firmas_d_9ddd9d
    - Obligacion_los_billetes_de_10_de_la_serie_25_000_001_b_llevaran_facsimiles_de_las_firmas_de_e82c37
    - Obligacion_los_billetes_de_20_de_la_serie_28_010_001_a_llevaran_facsimiles_de_las_firmas_de_58b702
    - Obligacion_los_billetes_de_50_de_la_serie_66_760_001_a_llevaran_facsimiles_de_las_firmas_de_52ec2e
    - Obligacion_los_cajeros_automaticos_deben_informar_previamente_al_cliente_las_operaciones_ad_38db05
    - Obligacion_los_cajeros_deben_permitir_al_cliente_desistir_de_su_uso_sin_costo_alguno__depah_0361aa
    - Obligacion_los_campos_alfanumericos_deben_llenarse_con_blancos_a_derecha_para_completar_la__b186bc
    - Obligacion_los_campos_alfanumericos_que_posean_mas_caracteres_de_los_requeridos_deben_compl_20ae2a
    - Obligacion_los_campos_definidos_como_alfabeticos_o_alfanumericos_deben_completarse_usando_c_9f10ab
    - Obligacion_los_campos_definidos_como_alfanumericos_deben_completarse_usando_comillas_dobles_ef434c
    - Obligacion_los_campos_definidos_como_alfanumericos_o_alfabeticos_deben_completarse_usando_c_716fe4
    - Obligacion_los_campos_numericos_con_longitud_igual_a_la_maxima_longitud_definida_no_deben_c_4ee0fb
    - Obligacion_los_campos_numericos_cuya_longitud_es_igual_a_la_maxima_longitud_definida_no_deb_58da2c
    - Obligacion_los_campos_numericos_cuya_longitud_sea_igual_a_la_maxima_longitud_definida_no_de_520990
    - Obligacion_los_campos_numericos_que_posean_mas_caracteres_de_los_requeridos_deben_completar_634fa3
    - Obligacion_los_campos_numericos_que_posean_mas_caracteres_de_los_requeridos_deben_llenarse__b5a233
    - Obligacion_los_caracteres_alfabeticos_de_los_campos_alfanumericos_deben_ser_siempre_informa_ca9260
    - Obligacion_los_caracteres_alfabeticos_de_los_campos_alfanumericos_deberan_ser_siempre_infor_2f83c6
    - Obligacion_los_caracteres_alfabeticos_de_los_campos_alfanumericos_deberan_ser_siempre_infor_543558
    - Obligacion_los_caracteres_alfabeticos_de_los_campos_alfanumericos_deberan_ser_siempre_infor_80dace
    - Obligacion_los_caracteres_alfabeticos_de_los_campos_alfanumericos_deberan_ser_siempre_infor_cc1936
    - Obligacion_los_caracteres_alfabeticos_de_los_campos_alfanumericos_deberan_ser_siempre_infor_d28c91
    - Obligacion_los_caracteres_alfabeticos_deben_ser_siempre_informados_en_mayusculas__snp_cheq__23cd47
    - Obligacion_los_caracteres_alfabeticos_deben_ser_siempre_informados_en_mayusculas__snp_cheq__a30473
    - Obligacion_los_caracteres_alfabeticos_en_todos_los_campos_deberan_ser_informados_siempre_en_19d627
    - Obligacion_los_certificados_de_antecedentes_penales_solicitados_deberan_haber_sido_expedido_f408bf
    - Obligacion_los_clientes_cuyas_deudas_hayan_sido_refinanciadas_mediante_obligaciones_de_pago_c3a4a7
    - Obligacion_los_conceptos_devengados_a_favor_del_cliente_se_reconocen_como_comisiones_en_la__9829f2
    - Obligacion_los_conceptos_que_no_registren_incrementos_de_tasas_de_exigencia_se_informaran_u_fb15aa
    - Obligacion_los_conceptos_que_registren_incrementos_en_las_tasas_se_trataran_conforme_al_pun_ee49bd
    - Obligacion_los_conflictos_de_intereses_deben_identificarse_minimizarse_y_sujetarse_a_un_cui_e7428b
    - Obligacion_los_contratos_de_fideicomisos_deben_contener_una_clausula_por_la_cual_el_fiducia_c7cec1
    - Obligacion_los_controles_respecto_de_las_partidas_210100_tp_y_500000_tp_se_realizaran_cuand_d0f2b7
    - Obligacion_los_convenios_deben_contener_clausula_expresa_por_la_que_las_asociaciones_de_pro_24057d
    - Obligacion_los_datos_del_beneficiario_final_deben_ser_integrados_en_el_cheque_cancelatorio__229af0
    - Obligacion_los_datos_se_calcularan_sobre_el_promedio_mensual_de_saldos_diarios_capitales_e__b98235
    - Obligacion_los_datos_y_declaraciones_consignados_en_la_solicitud_son_hechos_con_el_proposit_be618e
    - Obligacion_los_depositos_con_destino_a_la_plaza_sde_deberan_realizarse_en_cantidades_por_mi_b8defa
    - Obligacion_los_depositos_con_destino_caba_deberan_realizarse_en_cantidades_en_packs_multipl_1d41f3
    - Obligacion_los_derechos_de_acceso_a_los_datos_su_actualizacion_rectificacion_o_supresion_de_0ab73c
    - Obligacion_los_diez_cientos_que_conforman_el_millar_de_billetes_en_buen_uso_deberan_estar_s_8d45b3
    - Obligacion_los_diez_cientos_que_conforman_el_millar_de_las_denominaciones_deberan_estar_ter_b32c2b
    - Obligacion_los_diez_cientos_que_conforman_el_millar_deberan_estar_termosellados_con_una_pel_454f6d
    - Obligacion_los_diez_cientos_que_conforman_el_millar_deberan_ser_perforados_mediante_impacto_c149d8
    - Obligacion_los_directivos_del_comite_de_auditoria_permaneceran_en_sus_funciones_por_un_peri_f115e5
    - Obligacion_los_directores_o_funcionarios_de_entidades_financieras_extranjeras_en_el_comite__4f1b6c
    - Obligacion_los_dividendos_se_imputaran_en_ingresos_financieros_resultado_por_otros_titulos__4f2ece
    - Obligacion_los_documentos_deberan_reunir_los_requisitos_establecidos_por_la_legislacion_vig_6f1f88
    - Obligacion_los_endosos_de_cheques_cancelatorios_librados_en_usd_deberan_ser_certificados_po_81487f
    - Obligacion_los_facsimiles_de_las_firmas_se_mantienen_de_acuerdo_con_lo_estipulado_en_la_car_644967
    - Obligacion_los_fondos_debitados_indebidamente_por_comisiones_y_o_cargos_deberan_ser_reinteg_cacd88
    - Obligacion_los_fondos_debitados_por_comisiones_o_gastos_sin_el_previo_conocimiento_de_los_c_cf3fdd
    - Obligacion_los_funcionarios_designados_seran_responsables_en_caso_de_computos_indebidos_que_d925b3
    - Obligacion_los_gastos_de_operaciones_de_cambio_son_a_cargo_del_deudor__manori_sbloque5_6c30f1
    - Obligacion_los_gastos_y_honorarios_de_reinscripcion_de_la_prenda_estan_a_cargo_del_acreedor_d98766
    - Obligacion_los_importes_al_31_12_19_reexpresados_en_moneda_homogenea_de_esa_fecha_seran_los_dd42bd
    - Obligacion_los_importes_de_los_servicios_de_amortizacion_que_venzan_dentro_del_ano_seran_co_d3255d
    - Obligacion_los_importes_determinados_de_acuerdo_con_la_metodologia_anterior_ajustados_por_l_73b080
    - Obligacion_los_importes_en_dolares_estadounidenses_se_convertiran_a_pesos_utilizando_el_tip_718679
    - Obligacion_los_importes_en_moneda_extranjera_se_convertiran_a_pesos_utilizando_el_tipo_de_c_b89a63
    - Obligacion_los_importes_se_acreditaran_en_las_cuentas_que_correspondan_dentro_de_los_5_dias_28d57e
    - Obligacion_los_importes_se_acreditaran_en_las_cuentas_que_correspondan_dentro_de_los_5_dias_da067e
    - Obligacion_los_importes_se_registraran_en_miles_de_dolares_estadounidenses_sin_decimales__r_687034
    - Obligacion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales__ri_gerc_s1_caa151
    - Obligacion_los_incrementos_de_exigencia_derivados_de_aplicar_el_efectivo_minimo_vigente_al__e382d3
    - Obligacion_los_indices_seran_calculados_y_publicados_conforme_a_lo_expuesto_y_a_las_definic_f5328b
    - Obligacion_los_informes_basados_en_datos_sobre_riesgos_deben_ser_exactos_claros_y_completos_ee5475
    - Obligacion_los_informes_bimestrales_deberan_hacer_mencion_a_los_informes_parciales_elaborad_6e4939
    - Obligacion_los_informes_de_gestion_de_riesgos_deben_entregarse_a_los_destinatarios_pertinen_b1d568
    - Obligacion_los_informes_de_gestion_de_riesgos_deben_someterse_a_procesos_de_conciliacion_y__aa456d
    - Obligacion_los_informes_de_gestion_de_riesgos_deben_transmitir_de_forma_exacta_y_precisa_lo_d6b088
    - Obligacion_los_informes_de_riesgos_deben_satisfacer_los_criterios_que_a_continuacion_se_exp_db44c4
    - Obligacion_los_informes_deben_entregarse_con_tiempo_suficiente_a_las_personas_competentes_e_d2722a
    - Obligacion_los_informes_deberan_contener_descripcion_del_alcance_de_las_tareas_realizadas_l_c34645
    - Obligacion_los_informes_deberan_presentarse_al_consejo_de_administracion_dentro_de_quince_1_74d0f6
    - Obligacion_los_informes_deberan_ser_transcriptos_en_el_libro_mencionado_en_el_punto_ii_1_de_410d60
    - Obligacion_los_informes_especiales_deberan_contener_como_minimo_titulo_destinatario_identif_6998c9
    - Obligacion_los_informes_para_cada_uno_de_los_ciclos_relevantes_deberan_tener_una_periodicid_3d752b
    - Obligacion_los_informes_parciales_deberan_conservarse_como_anexo_al_libro_de_control_encuad_341446
    - Obligacion_los_ingresos_de_los_solicitantes_deberan_ser_demostrables_habituales_y_permanent_088f64
    - Obligacion_los_ingresos_de_los_solicitantes_deberan_ser_demostrables_habituales_y_permanent_602660
    - Obligacion_los_ingresos_por_rentas_se_demostraran_por_medio_de_la_documentacion_respaldator_3e722a
    - Obligacion_los_inputs_y_supuestos_de_los_modelos_pueden_obtenerse_de_procesos_de_modelizaci_4dd479
    - Obligacion_los_integrantes_del_equipo_de_auditoria_interna_deberan_guardar_secreto_incluso__e9fa9c
    - Obligacion_los_intereses_deben_liquidarse_por_periodos_vencidos_y_acreditarse_en_la_cuenta__ee2832
    - Obligacion_los_intereses_se_acreditaran_en_la_cuenta_con_la_periodicidad_diaria_semanal_men_99ae9b
    - Obligacion_los_intereses_se_capitalizaran_cada_treinta_dias_corridos__manori_sbloque4_d7c323
    - Obligacion_los_intereses_se_capitalizaran_o_abonaran_en_forma_vencida_de_acuerdo_con_las_co_4e5ad2
    - Obligacion_los_intereses_se_devengaran_a_la_tasa_que_se_fije_y_que_sera_transmitida_a_trave_4f7e62
    - Obligacion_los_intereses_se_devengaran_a_la_tasa_que_se_fije_y_que_sera_transmitida_a_trave_6744d5
    - Obligacion_los_intereses_y_ajustes_devengados_de_activos_financieros_transferidos_no_dados__4a9f68
    - Obligacion_los_libradores_deudores_codeudores_o_aceptante_de_los_respectivos_instrumentos_d_4fe8f9
    - Obligacion_los_limites_de_asistencia_crediticia_deben_considerar_los_diferentes_tipos_de_ex_d44081
    - Obligacion_los_limites_de_asistencia_crediticia_deben_contribuir_a_que_exista_una_cartera_d_ee1213
    - Obligacion_los_limites_de_asistencia_crediticia_deben_evitar_concentraciones_por_actividad__5313b9
    - Obligacion_los_limites_de_asistencia_crediticia_deben_ser_proporcionales_al_riesgo_del_deud_713047
    - Obligacion_los_limites_dispuestos_en_los_puntos_2_1_9_2_1_14_y_a_los_destinos_vinculados_a__71e19e
    - Obligacion_los_limites_internos_deben_ser_congruentes_con_el_modelo_de_medicion_de_riesgos__be930e
    - Obligacion_los_miembros_del_consejo_de_administracion_deberan_demostrar_idoneidad_para_la_f_8b2f07
    - Obligacion_los_modelos_utilizados_para_medir_el_rtici_deben_ser_comprehensivos_y_estar_cont_b605d5
    - Obligacion_los_montos_adeudados_por_costas_y_gastos_devengaran_desde_la_fecha_de_su_erogaci_2442b5
    - Obligacion_los_montos_de_las_facturas_emitidas_en_dolares_estadounidenses_se_expresaran_en__3f23c2
    - Obligacion_los_motivos_de_rechazos_indicados_deberan_estar_alineados_a_izquierda_respetando_45febe
    - Obligacion_los_oferentes_que_puedan_afectar_la_calificacion_de_la_entidad_o_la_estructura_d_e49598
    - Obligacion_los_pasivos_financieros_garantias_financieras_y_compromisos_de_concesion_de_un_p_951c85
    - Obligacion_los_periodos_de_permanencia_de_los_directivos_no_deben_ser_coincidentes_aseguran_b1eb2a
    - Obligacion_los_planes_de_financiamiento_deben_tener_en_consideracion_las_correlaciones_entr_29ecd5
    - Obligacion_los_plazos_residuales_de_las_operaciones_a_plazo_equivaldran_a_la_cantidad_de_di_bd8fe1
    - Obligacion_los_procedimientos_de_prueba_incluyen_la_realizacion_de_consultas_la_inspeccion__bd76a0
    - Obligacion_los_procedimientos_que_realice_la_auditoria_interna_para_verificar_el_diseno_y_o_dbc378
    - Obligacion_los_procesos_y_procedimientos_de_control_deben_incluir_un_sistema_que_asegure_el_231c95
    - Obligacion_los_programas_de_pruebas_de_estres_deben_cubrir_en_forma_coherente_y_exhaustiva__c959db
    - Obligacion_los_reemplazos_de_tarjeta_originados_por_desmagnetizacion_deterioro_hasta_uno_po_4dd6f2
    - Obligacion_los_requisitos_que_se_establecen_para_la_habilitacion_deberan_ser_observados_en__185e1f
    - Obligacion_los_resultados_a_fin_de_cada_mes_producto_de_la_medicion_de_estas_operaciones_a__5808ed
    - Obligacion_los_resultados_a_fin_de_cada_mes_producto_de_la_medicion_de_estas_operaciones_a__5bcf2e
    - Obligacion_los_resultados_a_fin_de_cada_mes_producto_de_la_medicion_de_estas_operaciones_a__d26cce
    - Obligacion_los_resultados_a_fin_de_cada_mes_producto_de_la_medicion_de_estas_operaciones_a__ffe88f
    - Obligacion_los_resultados_correspondientes_a_operaciones_a_termino_de_moneda_extranjera_pro_165c17
    - Obligacion_los_resultados_de_la_medicion_de_opciones_de_compra_lanzadas_a_fin_de_cada_mes_s_015fb2
    - Obligacion_los_resultados_de_la_medicion_de_opciones_de_compra_tomadas_a_fin_de_cada_mes_se_43b97c
    - Obligacion_los_resultados_de_la_medicion_de_opciones_de_venta_lanzadas_a_fin_de_cada_mes_se_c4b95d
    - Obligacion_los_resultados_de_la_medicion_de_opciones_de_venta_tomadas_a_fin_de_cada_mes_se__6006df
    - Obligacion_los_resultados_de_la_suficiencia_de_capital_frente_al_rtici_deben_considerarse_e_81cc79
    - Obligacion_los_resultados_de_las_pruebas_de_estres_deben_contribuir_a_adoptar_decisiones_es_8eb610
    - Obligacion_los_resultados_de_las_pruebas_de_estres_deben_ser_tenidos_en_cuenta_en_el_proces_8c1f84
    - Obligacion_los_resultados_de_las_tecnicas_de_medicion_deben_contribuir_a_evaluar_el_nivel_d_9a240d
    - Obligacion_los_resultados_de_medicion_a_valor_razonable_de_instrumentos_financieros_derivad_dca6f8
    - Obligacion_los_resultados_deben_ser_considerados_para_analizar_la_suficiencia_del_capital_y_64c2e7
    - Obligacion_los_resultados_del_examen_y_validacion_y_toda_recomendacion_sobre_la_utilizacion_0e643b
    - Obligacion_los_resultados_originados_por_la_diferencia_de_cotizacion_de_moneda_extranjera_s_eb45a5
    - Obligacion_los_resultados_por_medicion_a_valor_razonable_de_instrumentos_financieros_deriva_cfe7dc
    - Obligacion_los_resultados_por_venta_o_baja_de_componentes_del_rubro_otros_resultados_integr_fd503d
    - Obligacion_los_saldos_activos_y_pasivos_derivados_de_las_operaciones_de_corresponsalia_debe_06dbdc
    - Obligacion_los_saldos_promedio_correspondientes_se_expresaran_en_miles_de_pesos_o_dolares_e_638e5f
    - Obligacion_los_saldos_quedan_a_la_vista_sin_devengar_intereses_en_las_condiciones_generales_81d10a
    - Obligacion_los_servicios_adicionales_deben_quedar_claramente_establecidos_como_anexo_al_tex_6320f0
    - Obligacion_los_servicios_y_movimientos_en_la_caja_de_ahorros_destinada_a_menores_de_edad_ad_25b46f
    - Obligacion_los_sim_deben_ser_suficientemente_flexibles_para_incorporar_las_restricciones_qu_464b50
    - Obligacion_los_sistemas_de_informacion_deberan_registrar_el_hecho_de_que_se_permite_la_prec_536845
    - Obligacion_los_sistemas_de_informacion_deberan_registrar_la_modalidad_de_precancelacion_per_84b30f
    - Obligacion_los_sistemas_de_informacion_gerencial_deben_permitir_agregar_las_financiaciones__7f554f
    - Obligacion_los_sistemas_de_informacion_gerencial_deben_permitir_seguir_las_exposiciones_en__ee7014
    - Obligacion_los_sistemas_de_informacion_para_la_gestion_de_riesgos_mis_deben_permitir_recupe_bdb3e9
    - Obligacion_los_sistemas_deben_permitir_identificar_oportunamente_los_creditos_con_problemas_0200b3
    - Obligacion_los_sistemas_internos_de_medicion_sim_deben_ser_capaces_de_calcular_las_medidas__d8eecc
    - Obligacion_los_sistemas_y_modelos_de_medicion_para_calcular_el_rtici_deben_basarse_en_datos_9ff31f
    - Obligacion_los_solicitantes_de_prestamos_hipotecarios_deberan_reunir_los_siguientes_requisi_43237a
    - Obligacion_los_solicitantes_deben_cumplir_los_requerimientos_exigidos_por_el_seguro_de_vida_1463cb
    - Obligacion_los_solicitantes_deben_optar_por_una_modalidad_de_recepcion_de_la_informacion_de_1a263a
    - Obligacion_los_solicitantes_deben_ser_personas_humanas_y_poseer_capacidad_legal_para_contra_95780b
    - Obligacion_los_solicitantes_deberan_completar_y_firmar_una_solicitud_de_prestamo_que_debera_3c65a0
    - Obligacion_los_solicitantes_deberan_presentar_la_documentacion_respaldatoria_de_los_ingreso_90f46d
    - Obligacion_los_solicitantes_deberan_presentar_la_documentacion_respaldatoria_de_los_ingreso_c054ca
    - Obligacion_los_supuestos_sobre_saldos_y_comportamiento_de_nmd_deben_variar_segun_las_caract_f6ff04
    - Obligacion_los_titulos_denominados_en_moneda_extranjera_se_imputaran_en_cuentas_especificas_0b0163
    - Obligacion_los_titulos_publicos_nacionales_en_pesos_leliq_y_o_nobac_admitidos_para_la_integ_0182cc
    - Obligacion_los_titulos_publicos_nacionales_en_pesos_leliq_y_o_nobac_admitidos_para_la_integ_0bbd4e
    - Obligacion_los_titulos_publicos_y_privados_recibidos_a_plazo_fijo_o_en_prestamo_de_entidade_56aa06
    - Obligacion_los_titulos_publicos_y_privados_se_mantendran_en_las_cuentas_correspondientes_du_76db24
    - Obligacion_los_usuarios_deben_denunciar_de_inmediato_al_banco_la_perdida_o_robo_de_su_tarje_dd80db
    - Obligacion_los_valores_de_los_nocionales_vinculados_a_estas_operaciones_se_informaran_en_la_f1d6ee
    - Obligacion_luego_del_cierre_del_periodo_economico_las_cuentas_totalizadoras_del_rubro_otros_042aa9
    - Obligacion_mantener_actualizada_diariamente_la_pagina_de_internet_del_bcra_que_permite_cons_22e4e6
    - Obligacion_mantener_en_la_republica_argentina_todo_resguardo_de_documentacion_original_cuan_696b11
    - Obligacion_mantenimiento_de_archivos_y_registros_completos_de_cada_prestamo__manori_3_3_2_3648d3
    - Obligacion_mantenimiento_de_registros_adecuados_de_las_cobranzas__manori_3_3_2_23c2b2
    - Obligacion_mantenimiento_de_registros_contables_completos_actualizados_y_precisos__manori_3_0e9652
    - Obligacion_mantenimiento_y_seguimiento_de_las_polizas_de_seguro_seguro_de_vida_y_seguro_de__dbdd32
    - Obligacion_medir_aumentos_esperados_en_el_ingreso_y_egreso_diario_de_fondos_anticipando_cua_dbbd13
    - Obligacion_monitoreo_de_las_medidas_de_mitigacion_de_riesgos_de_tecnologia_y_seguridad_de_l_910ee1
    - Obligacion_no_digitar_la_clave_personal_en_presencia_de_personas_ajenas_aun_cuando_pretenda_fe592f
    - Obligacion_no_facilitar_la_tarjeta_magnetica_a_terceros_ya_que_ella_es_de_uso_personal_reco_bf386f
    - Obligacion_no_se_informaran_los_datos_correspondientes_a_las_partidas_451000_m_451200_m_y_4_716c90
    - Obligacion_obligacion_de_abonar_los_canones_de_habilitacion_que_se_especifican_a_continuaci_0020f1
    - Obligacion_obligacion_de_constituir_provision_del_100_sobre_el_total_de_la_deuda_en_las_res_57a94c
    - Obligacion_obligacion_de_constituir_provision_del_100_sobre_las_financiaciones_renovaciones_fb3a5f
    - Obligacion_obligacion_de_informar_a_la_superintendencia_de_entidades_financieras_y_cambiari_12ba9e
    - Obligacion_obligacion_de_reintegrar_al_deudor_el_remanente_del_producido_de_la_ejecucion_en_972fa5
    - Obligacion_obligacion_de_reportar_a_la_central_de_facturas_de_credito_electronicas_mipyme_i_a5f25d
    - Obligacion_obtener_confirmaciones_directas_de_los_asesores_legales_de_la_entidad_sobre_el_e_bc194d
    - Obligacion_obtener_del_registro_adicional_de_la_transferencia_campo_3_concepto_las_primeras_780e91
    - Obligacion_obtener_el_consentimiento_del_titular_para_las_modificaciones_en_las_condiciones_cd7c52
    - Obligacion_opciones_de_compra_lanzadas_se_imputaran_a_las_cuentas_de_opciones_de_compra_lan_627990
    - Obligacion_opciones_de_compra_tomadas_se_imputaran_a_las_cuentas_de_opciones_de_compra_toma_58706c
    - Obligacion_opciones_de_venta_lanzadas_se_imputaran_a_las_cuentas_de_opciones_de_venta_lanza_08bf39
    - Obligacion_opciones_de_venta_tomadas_se_imputaran_a_las_cuentas_de_opciones_de_venta_tomada_f28bf8
    - Obligacion_operara_diariamente_una_unica_sesion_de_presentados_para_las_transferencias_de_p_9b8a66
    - Obligacion_optimizar_los_procesos_administrativos_para_facilitar_la_apertura_de_cuentas_en__e0c6b3
    - Obligacion_para_cada_registro_de_cuota_se_deberan_incluir_los_campos_especificados_numero_d_183ac1
    - Obligacion_para_cada_registro_de_cuota_se_deberan_incluir_los_campos_especificados_numero_d_b2c00c
    - Obligacion_para_calcular_el_traslado_se_computaran_los_numerales_trasladados_del_periodo_de_6b76f9
    - Obligacion_para_constituir_la_prenda_con_registro_se_requiere_consentimiento_expreso_del_co_8cede9
    - Obligacion_para_cumplimentar_el_tramite_de_inscripcion_presentara_la_solicitud_de_inscripci_de0512
    - Obligacion_para_determinar_el_monto_de_pesos_que_surge_de_lo_previsto_en_los_acapites_i_y_i_591629
    - Obligacion_para_determinar_la_exigencia_minima_diaria_en_moneda_extranjera_a_informar_en_el_0610e8
    - Obligacion_para_determinar_los_cargos_e_intereses_sobre_aquellos_no_ingresados_en_tiempo_y__c20d43
    - Obligacion_para_determinar_los_intereses_aplicables_a_los_cargos_no_ingresados_en_tiempo_y__504d94
    - Obligacion_para_determinar_una_mejora_en_la_clasificacion_de_un_deudor_recategorizado_en_ni_15a3d5
    - Obligacion_para_devoluciones_de_pago_de_sueldo_pagos_previsionales_asignaciones_familiares__b652fc
    - Obligacion_para_devoluciones_de_transferencias_minoristas_en_pesos_pago_a_proveedores_entre_afb654
    - Obligacion_para_el_calculo_de_la_posicion_bimestral_se_debera_considerar_el_promedio_result_5da448
    - Obligacion_para_el_calculo_del_aporte_al_fondo_de_garantia_de_los_depositos_ademas_de_las_p_dab99f
    - Obligacion_para_el_calculo_del_traslado_a_noviembre_se_computaran_los_numerales_de_la_posic_95cd58
    - Obligacion_para_el_calculo_del_traslado_al_bimestre_septiembre_octubre_se_computaran_los_nu_eb1fe4
    - Obligacion_para_el_calculo_del_traslado_de_la_integracion_se_computaran_los_numerales_del_p_11adf5
    - Obligacion_para_el_funcionamiento_posterior_de_los_cajeros_automaticos_y_dispositivos_simil_b62121
    - Obligacion_para_el_periodo_abril_22_calcular_partida_713000_001_n_837000_001_n_30_17_30_34__50fe40
    - Obligacion_para_el_periodo_enero_22_calcular_100000_001_n_1_b1_9_31_a_100000_001_n_1_b2_22__e90ac2
    - Obligacion_para_el_periodo_enero_22_calcular_partida_713000_001_n_837000_001_n_14_9_31_30_2_f1bcda
    - Obligacion_para_el_periodo_julio_22_calcular_partida_713000_001_n_837000_001_n_34_28_31_40__79815d
    - Obligacion_para_el_redondeo_de_los_valores_del_cargo_c_e_interes_i_se_incrementaran_en_una__2a0630
    - Obligacion_para_fortalecer_la_resiliencia_operacional_en_toda_la_entidad_se_debera_coordina_2fd0e2
    - Obligacion_para_la_identificacion_e_inscripcion_fiscal_del_titular_de_cuentas_abiertas_por__dad4ec
    - Obligacion_para_la_instalacion_de_cajeros_automaticos_y_dispositivos_similares_deberan_obse_c5f8e9
    - Obligacion_para_la_partida_102200_001_se_informara_el_promedio_acumulado_desde_el_inicio_de_aa4ada
    - Obligacion_para_la_recategorizacion_del_deudor_en_niveles_superiores_despues_de_transcurrid_e3fa76
    - Obligacion_para_la_respuesta_de_rechazo_fuera_de_canje_se_deben_utilizar_los_registros_indi_ab1a59
    - Obligacion_para_las_partidas_previstas_en_el_punto_10_1_2_se_consideraran_las_categorias_pr_5792ae
    - Obligacion_para_las_tarjetas_de_credito_o_compra_se_sugiere_tomar_el_10_del_promedio_de_sal_68723b
    - Obligacion_para_los_calculos_intermedios_de_prorrateos_de_alicuotas_o_porcentajes_de_los_pu_9f5d37
    - Obligacion_para_los_calculos_intermedios_de_prorrateos_de_alicuotas_o_porcentajes_de_los_pu_f0535e
    - Obligacion_para_monedas_extranjeras_distintas_de_dolar_estadounidense_la_exigencia_debera_i_068d2e
    - Obligacion_para_obligaciones_a_la_vista_en_moneda_extranjera_distinta_del_dolar_estadounide_cda994
    - Obligacion_para_plazos_fijos_y_restantes_operaciones_a_plazo_en_pesos_considerar_para_el_ca_338d28
    - Obligacion_para_prestamos_otorgados_mediante_metodos_especificos_de_evaluacion_screening_y__7ad4d3
    - Obligacion_para_sociedades_por_acciones_simplificadas_sas_se_requiere_la_presentacion_de_la_d2eeab
    - Obligacion_para_sociedades_por_acciones_simplificadas_sas_se_requiere_la_presentacion_del_i_a9beb1
    - Obligacion_para_su_calculo_se_considerara_el_promedio_que_surja_de_dividir_la_suma_de_los_n_4b18b6
    - Obligacion_para_transferencias_entre_clientes_y_o_terceros_el_campo_concepto_del_registro_a_8e7190
    - Obligacion_participar_en_la_realizacion_de_inventarios_fisicos_de_bienes_de_uso_y_diversos__e6073f
    - Obligacion_por_razones_de_control_interno_es_preciso_separar_las_funciones_comerciales_de_l_8c5ce1
    - Obligacion_porcion_del_importe_declarado_en_la_partida_210106_13000_que_corresponda_al_prom_824788
    - Obligacion_preferentemente_por_medios_electronicos_cuando_se_trate_de_depositos_menores_o_i_ca8d97
    - Obligacion_presentacion_de_declaracion_jurada_del_titular_o_su_representante_para_acreditar_fcdccf
    - Obligacion_presentacion_de_documentos_de_identidad_conforme_a_las_normas_sobre_documentos_d_953384
    - Obligacion_presentacion_de_un_plan_de_regularizacion_y_saneamiento_cuando_se_determine_que__626d96
    - Obligacion_presentacion_en_forma_neta_como_activo_o_pasivo_por_impuesto_diferido_al_fin_de__0319e1
    - Obligacion_presentar_certificacion_de_la_autoridad_del_pais_de_origen_que_acredite_que_la_e_f9fcbd
    - Obligacion_presentar_copias_de_estatutos_y_demas_disposiciones_por_los_que_se_rige_la_entid_9e0f9f
    - Obligacion_presentar_declaracion_jurada_mediante_la_cual_manifieste_que_no_ha_sido_sujeta_a_17ea98
    - Obligacion_presentar_la_informacion_y_documentacion_prevista_en_los_puntos_2_4_8_1_a_2_4_8__eacb62
    - Obligacion_presentar_nomina_de_personas_comprometidas_a_aportar_capital_inicial_con_domicil_072abb
    - Obligacion_presentar_nomina_y_participaciones_de_los_accionistas_que_individualmente_tengan_cee5ec
    - Obligacion_presentar_una_nota_con_membrete_institucional_refrendada_con_dos_firmas_y_sellos_8584dc
    - Obligacion_presentaran_con_caracter_de_declaracion_jurada_la_nomina_de_la_totalidad_de_los__6ed2e2
    - Obligacion_prever_la_puesta_a_disposicion_de_resumenes_con_detalle_de_movimientos_de_las_cu_c2adf1
    - Obligacion_probar_para_una_muestra_de_las_obligaciones_la_correccion_de_las_tasas_de_intere_52f171
    - Obligacion_probar_para_una_muestra_de_los_activos_la_correccion_de_las_tasas_de_interes_apl_d41515
    - Obligacion_proceder_al_pago_del_chc_luego_de_ejecutar_las_acciones_dispuestas_en_el_punto_8_e6d528
    - Obligacion_provision_de_copia_de_certificados_de_liquidacion_de_prestaciones_de_seguridad_s_a6d1f5
    - Obligacion_provision_de_informaciones_sobre_antecedentes_personales_manifestaciones_de_bien_224f1a
    - Obligacion_proyectar_los_defectos_de_prevision_que_surjan_de_la_cartera_analizada__ri_ccna__d67f23
    - Obligacion_puede_transcribirse_un_resumen_ejecutivo_que_debe_contener_como_minimo_descripci_2b7ea4
    - Obligacion_realizacion_de_la_medicion_posterior_de_los_bienes_reclasificados_de_acuerdo_con_693515
    - Obligacion_realizar_actualizaciones_periodicas_de_la_tecnologia_y_seguridad_de_la_informaci_e33c86
    - Obligacion_realizar_control_al_fin_de_cada_lote_de_transacciones__snp_cheq_sbloque5_6b209b
    - Obligacion_realizar_el_cotejo_con_las_actas_de_las_asambleas_de_asociados_y_o_reuniones_del_493aee
    - Obligacion_realizar_la_secuencia_de_actualizacion_necesariamente_en_orden_cronologico_sin_s_9f353d
    - Obligacion_realizar_las_acciones_contempladas_en_el_punto_8_9_4__cirmo3_8_9_2_67e5de
    - Obligacion_realizar_las_acciones_previstas_en_el_punto_siguiente_8_9_4__cirmo3_8_9_3_6f8a6a
    - Obligacion_realizar_pruebas_de_eficacia_de_diseno_para_evaluar_si_las_actividades_de_contro_80992c
    - Obligacion_reclasificacion_inmediata_en_el_nivel_siguiente_inferior_de_deudores_que_hayan_s_fa5a19
    - Obligacion_recomendacion_al_administrador_de_llevar_registros_de_los_distintos_procedimient_18a888
    - Obligacion_recomendacion_al_administrador_de_tomar_recaudos_para_la_guarda_y_conservacion_d_7c738c
    - Obligacion_recomendacion_al_realizar_una_operacion_de_deposito_introducir_el_sobre_que_cont_9c8564
    - Obligacion_recomendacion_de_comunicar_al_banco_donde_se_realizo_la_operacion_y_al_administr_894086
    - Obligacion_recomendacion_retirar_el_comprobante_que_la_maquina_entregue_al_finalizar_la_ope_ded014
    - Obligacion_refundicion_de_archivos_enviados_por_entidades_receptoras_clasificacion_por_enti_b2e1d3
    - Obligacion_refundicion_de_archivos_recibidos_de_entidades_originantes_clasificacion_por_ent_cf7fdc
    - Obligacion_registrar_el_costo_de_los_servicios_prestados_por_los_empleados_y_por_la_termina_acd19a
    - Obligacion_registrar_el_costo_de_servicios_presente_y_pasado_y_las_ganancias_o_perdidas_en__9a204e
    - Obligacion_registrar_promedio_mensual_de_saldos_diarios_incluyendo_depositos_que_verifiquen_f734c8
    - Obligacion_regla_de_formato_campos_numericos_se_rellenan_con_ceros_desde_el_margen_izquierd_e46a2c
    - Obligacion_relacion_de_las_respuestas_recibidas_de_confirmaciones_directas_con_los_registro_cf8a5c
    - Obligacion_relacion_de_las_respuestas_recibidas_de_terceros_depositarios_con_los_registros__12206f
    - Obligacion_relacionar_los_asuntos_tratados_en_las_actas_de_asambleas_de_asociados_y_reunion_976bba
    - Obligacion_remitir_en_tiempo_oportuno_los_informes_a_todos_los_destinatarios_pertinentes__a_8d4316
    - Obligacion_requisito_previo_a_la_apertura_de_una_cuenta_obtener_la_conformidad_expresa_de_l_9d135a
    - Obligacion_respecto_de_la_nomina_de_autoridades_y_de_los_representantes_autorizados_para_ut_8f5881
    - Obligacion_revisar_el_cumplimiento_de_las_normas_del_bcra_en_materia_de_prevencion_del_lava_efcff1
    - Obligacion_revisar_el_cumplimiento_de_planes_de_saneamiento_cuando_existan__ri_ccna_d1a3l2__a00fb6
    - Obligacion_revisar_el_efectivo_ingreso_de_los_fondos_correspondientes_a_los_aumentos_de_cap_a81ef5
    - Obligacion_revisar_la_documentacion_presentada_al_bcra_para_el_cumplimiento_de_relaciones_t_e12a7f
    - Obligacion_revisar_la_razonabilidad_de_la_valuacion_de_bienes_de_uso_y_del_computo_de_las_d_9460cb
    - Obligacion_revisar_la_razonable_preparacion_de_los_estados_contables_al_cierre_del_ejercici_ac55eb
    - Obligacion_revisar_las_cuentas_de_resultados_mas_significativas_mediante_la_aplicacion_de_p_994ae2
    - Obligacion_revisar_los_movimientos_del_periodo_de_las_inversiones_y_bienes_en_locacion_fina_f5115a
    - Obligacion_revisar_que_todos_los_libros_de_contabilidad_obligatorios_se_encuentren_actualiz_3c36a1
    - Obligacion_revision_de_otras_obligaciones_no_mencionadas_precedentemente_evaluando_la_razon_bff491
    - Obligacion_se_admitiran_debitos_internos_para_el_pago_de_comisiones_y_otros_conceptos_deriv_b4146c
    - Obligacion_se_aplicaran_las_disposiciones_establecidas_para_los_depositos_en_caja_de_ahorro_c545bf
    - Obligacion_se_aplicaran_las_mismas_normas_e_instrucciones_que_regiran_para_los_cheques_comu_961e91
    - Obligacion_se_aplicaran_las_normas_establecidas_para_los_depositos_en_caja_de_ahorros_en_lo_c8bd6d
    - Obligacion_se_calcularan_los_promedios_mensuales_de_saldos_diarios_en_moneda_de_origen_y_se_c9d96c
    - Obligacion_se_completara_con_el_codigo_de_banco_depositario_en_3_posiciones_incluido_en_las_559b85
    - Obligacion_se_completara_con_el_codigo_de_banco_girado_en_3_posiciones_incluido_en_las_posi_366b5c
    - Obligacion_se_completara_con_el_codigo_de_sucursal_girada_en_3_posiciones_incluido_en_las_p_48d22e
    - Obligacion_se_completara_con_el_nombre_de_la_imagen_o_puntero_asociado_al_registro_de_contr_70a9f0
    - Obligacion_se_completara_con_el_numero_de_cheque_en_8_posiciones_incluido_en_las_posiciones_6495d0
    - Obligacion_se_completara_con_el_numero_de_cuenta_en_11_posiciones_incluido_en_las_posicione_dd1a0f
    - Obligacion_se_completara_con_el_trace_number_del_cheque_original_incluido_en_las_posiciones_3bdf6e
    - Obligacion_se_completara_el_campo_banco_depositario_con_el_codigo_del_banco_depositario_en__90751d
    - Obligacion_se_completara_el_campo_banco_girado_con_el_codigo_del_banco_girado_en_3_posicion_a8d5f0
    - Obligacion_se_completara_el_campo_codigo_postal_tomando_las_posiciones_57_a_60_del_registro_a9a15b
    - Obligacion_se_completara_el_campo_fecha_de_compensacion_con_7_ceros_y_la_fecha_de_compensac_809496
    - Obligacion_se_completara_el_campo_fecha_de_presentacion_con_4_ceros_y_la_fecha_de_presentac_b43f05
    - Obligacion_se_completara_el_campo_numero_de_cheque_en_8_posiciones_incluido_en_las_posicion_f75f4c
    - Obligacion_se_completara_el_campo_numero_de_cuenta_en_11_posiciones_incluido_en_las_posicio_ed38ea
    - Obligacion_se_completara_el_campo_reservado_con_ceros__snp_cheq_7_1_13_79da1f
    - Obligacion_se_completara_el_campo_sucursal_girada_con_el_codigo_de_sucursal_girada_incluido_60ab30
    - Obligacion_se_completara_el_campo_tipo_de_registro_con_los_codigos_1_para_presentacion_de_l_941342
    - Obligacion_se_computaran_las_financiaciones_cualquiera_sea_su_modalidad_incluyendo_renovaci_3151d5
    - Obligacion_se_considerara_el_saldo_promedio_mensual_de_las_financiaciones_alcanzadas_del_pe_4d679b
    - Obligacion_se_considerara_el_saldo_promedio_mensual_de_las_financiaciones_alcanzadas_del_pe_ac431c
    - Obligacion_se_consideraran_todas_las_financiaciones_vigentes_a_mipymes_para_el_computo_del__1d52f6
    - Obligacion_se_consignara_el_promedio_mensual_del_total_de_retiros_diarios_de_efectivo_corre_371e16
    - Obligacion_se_consignara_el_promedio_mensual_del_total_de_retiros_diarios_de_efectivo_corre_91ab46
    - Obligacion_se_consignara_el_saldo_promedio_movil_a_fin_de_los_ultimos_12_periodos_anteriore_de1fe4
    - Obligacion_se_consignara_por_unica_vez_el_importe_a_deducir_que_surja_de_la_siguiente_expre_cae5d1
    - Obligacion_se_consignara_una_denominacion_que_identifique_al_grupo_de_contrapartes_la_que_s_c58ae7
    - Obligacion_se_consignaran_los_importes_admitidos_en_pesos_integrables_con_leliq_y_o_nobac_y_ec5447
    - Obligacion_se_consignaran_los_importes_admitidos_para_las_entidades_del_grupo_a_o_sucursale_f9894a
    - Obligacion_se_consignaran_los_importes_admitidos_para_las_entidades_financieras_en_pesos_se_c8fce6
    - Obligacion_se_debe_acompanar_nota_de_debito_formula_3030_indicando_como_concepto_cargo_por__108877
    - Obligacion_se_debe_conservar_en_el_legajo_de_la_cuenta_una_copia_del_vep_y_de_las_transacci_df3392
    - Obligacion_se_debe_considerar_la_relevancia_del_efecto_de_las_opciones_de_comportamiento_en_a70b8a
    - Obligacion_se_debe_emitir_un_informe_de_tasacion_con_ajuste_a_la_politica_general_acordada__12b72f
    - Obligacion_se_debe_especificar_las_responsabilidades_de_supervision_de_los_modelos_e_integr_bf4272
    - Obligacion_se_debe_implementar_tecnicas_de_autenticacion_multifactor_acordes_a_los_niveles__dee4cf
    - Obligacion_se_deben_considerar_parametros_para_la_formulacion_del_plan_de_negocios_y_el_ana_33a706
    - Obligacion_se_deben_informar_las_partidas_110500_m_10120x_m_11010x7m_expresadas_en_pesos_au_0c2d26
    - Obligacion_se_debera_calcular_el_cargo_por_deficiencia_mediante_una_expresion_matematica_qu_833a01
    - Obligacion_se_debera_calcular_el_interes_correspondiente_al_periodo_de_mora_para_los_cargos_9dba4f
    - Obligacion_se_debera_completar_con_blancos_a_derecha_para_cubrir_las_61_posiciones_de_este__866a35
    - Obligacion_se_debera_consignar_al_dorso_la_firma_y_aclaracion_del_mandante_u_ordenante_de_l_6fd0f7
    - Obligacion_se_debera_consignar_el_numero_de_identificacion_personal_segun_normas_sobre_docu_2c65f7
    - Obligacion_se_debera_reclasificar_los_saldos_informados_en_la_cuenta_ajuste_por_aplicacion__80ba04
    - Obligacion_se_debera_registrar_la_modalidad_de_precancelacion_que_ha_sido_permitida__manori_388059
    - Obligacion_se_difundiran_los_indices_mencionados_en_el_punto_5_1_2_correspondientes_a_los_u_439a49
    - Obligacion_se_especificara_la_situacion_de_la_cuenta_frente_al_sistema_de_seguro_de_garanti_5a69b2
    - Obligacion_se_especificara_la_situacion_de_la_cuenta_frente_al_sistema_de_seguro_de_garanti_69996b
    - Obligacion_se_especificara_la_situacion_de_la_cuenta_frente_al_sistema_de_seguro_de_garanti_c16eea
    - Obligacion_se_especificara_la_situacion_de_la_cuenta_frente_al_sistema_de_seguro_de_garanti_e7d6e1
    - Obligacion_se_especificara_la_situacion_de_la_cuenta_frente_al_sistema_de_seguro_de_garanti_f29365
    - Obligacion_se_evaluara_la_informacion_que_surja_de_los_elementos_de_juicio_referidos_en_los_e911e2
    - Obligacion_se_exige_la_presentacion_de_constancia_de_inscripcion_en_el_pertinente_registro__bfd12b
    - Obligacion_se_exigira_la_presentacion_de_la_fecha_y_numero_de_inscripcion_en_el_pertinente__92a5cf
    - Obligacion_se_exigiran_como_minimo_los_datos_que_se_especifican_en_los_items_siguientes_del_e05e07
    - Obligacion_se_expondra_en_egresos_financieros_cuando_el_saldo_de_la_cuenta_de_adopcion_del__211698
    - Obligacion_se_expondra_en_egresos_financieros_cuando_el_saldo_de_la_cuenta_de_derivados_sea_f89b8a
    - Obligacion_se_expondra_en_egresos_financieros_cuando_el_saldo_de_la_cuenta_de_reclasificaci_297d87
    - Obligacion_se_expondra_en_egresos_financieros_cuando_el_saldo_sea_deudor_a_fin_de_periodo_m_db3790
    - Obligacion_se_expondra_en_egresos_financieros_resultado_por_venta_o_baja_cuando_el_saldo_se_2f3384
    - Obligacion_se_expondra_en_ingresos_financieros_cuando_el_saldo_de_la_cuenta_de_refinanciaci_48fdfc
    - Obligacion_se_identificaran_aquellos_deudores_cuya_informacion_se_encuentre_sometida_a_revi_102b9d
    - Obligacion_se_imputara_en_otros_resultados_integrales_el_importe_del_cambio_perdida_o_ganan_b2a9a4
    - Obligacion_se_imputara_la_diferencia_entre_el_valor_razonable_y_el_costo_amortizado_para_ot_0a0ffb
    - Obligacion_se_imputaran_en_ingresos_financieros_resultado_por_venta_o_baja_en_cuentas_de_ac_94f31e
    - Obligacion_se_imputaran_en_la_cuenta_resultado_por_venta_o_baja_de_activos_financieros_a_va_673a5e
    - Obligacion_se_imputaran_en_las_cuentas_habilitadas_por_tipo_de_activo_financiero_los_result_953d9f
    - Obligacion_se_imputaran_en_las_cuentas_habilitadas_segun_el_tipo_de_activo_los_resultados_o_6e5ed8
    - Obligacion_se_imputaran_las_diferencias_que_surjan_de_la_variacion_del_valor_razonable_de_i_265275
    - Obligacion_se_imputaran_los_resultados_originados_en_la_renegociacion_o_modificacion_sustan_877908
    - Obligacion_se_imputaran_los_resultados_provenientes_de_la_medicion_de_pasivos_financieros_a_9a5581
    - Obligacion_se_incluira_el_efectivo_en_transito_y_en_transportadoras_de_valores_tv_los_impor_05d0cd
    - Obligacion_se_incluira_el_promedio_mensual_por_capitales_de_los_depositos_del_sector_financ_19bcdf
    - Obligacion_se_incluira_el_saldo_promedio_movil_a_fin_de_los_ultimos_12_periodos_anteriores__211f54
    - Obligacion_se_incluira_el_saldo_promedio_movil_a_fin_de_los_ultimos_12_periodos_anteriores__63bd3b
    - Obligacion_se_incluiran_los_billetes_y_monedas_mantenidos_en_custodia_en_otras_entidades_fi_6055a0
    - Obligacion_se_incrementaran_los_valores_en_una_unidad_cuando_el_primer_digito_de_las_fracci_5b1063
    - Obligacion_se_indicara_el_promedio_de_los_excesos_diarios__ri_gerc_2_5_2_73c417
    - Obligacion_se_informara_el_importe_de_la_posicion_neta_de_las_operaciones_sobre_derivados_d_061f9c
    - Obligacion_se_informara_el_importe_resultante_de_la_suma_algebraica_de_las_partidas_cuando__a98654
    - Obligacion_se_informara_el_saldo_promedio_acumulado_del_trimestre_bajo_informe_de_las_finan_2dbff9
    - Obligacion_se_informara_el_saldo_promedio_acumulado_del_trimestre_bajo_informe_de_las_finan_67ec8b
    - Obligacion_se_informara_el_saldo_promedio_acumulado_del_trimestre_bajo_informe_de_las_finan_e30c50
    - Obligacion_se_informara_por_unica_vez_en_la_presentacion_de_febrero_2020_el_saldo_contractu_eaafe2
    - Obligacion_se_informara_segun_el_modelo_de_informacion_detallado_en_el_punto_1_10_2_respect_ffcc17
    - Obligacion_se_informara_sobre_el_estado_del_juicio_al_momento_del_informe__cajasc_9_5_2_1_c3c374
    - Obligacion_se_informara_sobre_la_calidad_de_instrumentacion_del_mutuo_y_del_titulo_de_la_pr_68ef8f
    - Obligacion_se_informara_sobre_la_descripcion_de_los_motivos_que_han_provocado_dilaciones_en_24cb75
    - Obligacion_se_informara_sobre_la_estimacion_del_tiempo_que_demandara_obtener_una_resolucion_1d2717
    - Obligacion_se_informara_sobre_las_gestiones_realizadas_para_el_cobro_del_credito_justifican_4e3889
    - Obligacion_se_informara_sobre_las_razones_que_eventualmente_haya_opuesto_la_parte_demandada_a22095
    - Obligacion_se_informaran_los_saldos_de_billetes_y_monedas_mantenidos_en_las_casas_de_la_ent_b528c1
    - Obligacion_se_informaran_por_separado_las_partidas_correspondientes_a_cada_uno_de_los_meses_54fb14
    - Obligacion_se_informaran_por_separado_las_partidas_sujetas_a_exigencia_correspondientes_a_c_7ec5cc
    - Obligacion_se_informaran_por_separado_los_capitales_de_los_depositos_a_plazo_a_la_vista_y_l_b86309
    - Obligacion_se_insertara_alguna_de_las_siguientes_expresiones_en_procuracion_valor_al_cobro__bf1811
    - Obligacion_se_insertara_alguna_de_las_siguientes_expresiones_en_procuracion_valor_al_cobro__c9f495
    - Obligacion_se_permitira_mas_de_una_acreditacion_en_la_cuenta_especial_cecon_ar__depaho_4_22_e3fb06
    - Obligacion_se_procedera_de_similar_modo_aumentar_previsiones_como_minimo_de_manera_que_el_v_d8134f
    - Obligacion_se_realizara_la_sesion_de_rechazados_correspondiente_a_los_presentados_del_dia_h_81133e
    - Obligacion_se_realizara_mediante_transferencias_electronicas_desde_cuentas_a_la_vista_abier_a7a147
    - Obligacion_se_recomienda_impartir_instrucciones_para_que_previo_a_dar_curso_al_deposito_de__f9f111
    - Obligacion_se_recomienda_minimizar_el_movimiento_de_documentos_originales_mediante_el_uso_d_2e8b35
    - Obligacion_se_recomienda_que_la_mayoria_de_los_directores_del_comite_de_auditoria_sean_inde_87c1f4
    - Obligacion_se_recomienda_que_las_entidades_financieras_no_incluidas_en_el_grupo_a_incluyan__b78633
    - Obligacion_se_recomienda_que_todos_los_directores_del_comite_tengan_experiencia_en_practica_b16d3a
    - Obligacion_se_recomienda_verificar_el_dominio_de_los_inmuebles_o_rodados_declarados_y_tener_fb12fc
    - Obligacion_se_reconoce_la_obligacion_en_la_cuenta_obligaciones_por_operaciones_con_titulos__7f7e01
    - Obligacion_se_reportaran_como_informacion_complementaria_los_importes_aplicados_en_cada_cas_7be1bf
    - Obligacion_se_solicitara_por_carta_certificada_con_aviso_de_recepcion_la_adecuacion_integra_96ac30
    - Obligacion_se_sugiere_que_el_administrador_realice_una_primera_inspeccion_de_la_propiedad_e_1bb256
    - Obligacion_se_suspende_el_envio_de_informaciones_con_codigo_de_consolidacion_3_siendo_marzo_cf5074
    - Obligacion_se_tendra_en_consideracion_si_la_persona_ha_sido_condenada_por_delitos_de_lavado_483018
    - Obligacion_se_tendran_en_consideracion_las_informaciones_y_o_sanciones_que_sean_comunicadas_ef6a4d
    - Obligacion_se_tendran_en_cuenta_las_disposiciones_del_punto_1_del_apartado_a_de_la_seccion__f2fb3f
    - Obligacion_se_tomara_el_monto_equivalente_en_dolares_estadounidenses_resultante_del_corresp_82987e
    - Obligacion_se_utilizara_en_los_procedimientos_administrativos_y_contables_el_idioma_castell_69a5f4
    - Obligacion_se_utilizara_la_letra_m_para_indicar_campos_mandatorios_y_la_letra_o_para_indica_eaacf8
    - Obligacion_se_utilizaran_las_referencias_univocas_pct_cct_dct_ect_en_las_operaciones_de_pag_9dbc96
    - Obligacion_se_utilizaran_medios_electronicos_de_pago_para_cuentas_en_moneda_extranjera_cuan_804467
    - Obligacion_se_verificara_la_inexistencia_de_inhabilidades_que_fija_el_articulo_10_de_la_ley_388251
    - Obligacion_segmentar_prestatarios_en_al_menos_tres_universos_homogeneos_los_que_mejoran_su__0ac120
    - Obligacion_segmentar_prestatarios_en_universos_homogeneos_para_determinar_muestras_destinad_bf58c0
    - Obligacion_seguimiento_y_regularizacion_de_la_mora__manori_3_3_2_9a8ec7
    - Obligacion_seguir_las_posiciones_intradiarias_de_liquidez_teniendo_en_cuenta_las_actividade_19a938
    - Obligacion_sera_de_aplicacion_lo_previsto_por_las_normas_sobre_pago_de_beneficios_de_la_seg_a8ac76
    - Obligacion_seran_de_aplicacion_en_funcion_de_la_operatoria_admitida_las_disposiciones_conte_0ac982
    - Obligacion_seran_de_aplicacion_las_disposiciones_establecidas_para_los_depositos_en_caja_de_0a2af0
    - Obligacion_seran_de_aplicacion_las_disposiciones_establecidas_para_los_depositos_en_caja_de_47cfbd
    - Obligacion_seran_de_aplicacion_las_disposiciones_establecidas_para_los_depositos_en_caja_de_51343a
    - Obligacion_seran_de_aplicacion_las_disposiciones_establecidas_para_los_depositos_en_caja_de_a912ca
    - Obligacion_si_el_proceso_interno_determina_que_el_capital_regulatorio_es_insuficiente_las_e_323992
    - Obligacion_si_el_vencimiento_cae_en_dia_inhabil_bancario_el_pago_debe_efectuarse_el_dia_hab_3280f9
    - Obligacion_si_en_el_6to_mes_el_resultado_es_positivo_se_debitara_el_cargo_aplicando_la_tasa_ba5e6c
    - Obligacion_si_en_oportunidad_del_envio_de_la_informacion_mensual_del_presente_regimen_infor_1860db
    - Obligacion_si_entre_los_accionistas_se_incluyen_personas_juridicas_debera_suministrarse_doc_ce34cc
    - Obligacion_si_la_cesion_implica_cambio_de_domicilio_de_pago_el_nuevo_domicilio_debe_notific_025db2
    - Obligacion_si_la_prestataria_deja_de_cumplir_la_condicion_de_mipyme_se_computaran_solo_las__6da888
    - Obligacion_si_la_reparacion_o_restauracion_no_es_economicamente_viable_o_afecta_la_garantia_cf1734
    - Obligacion_si_no_existieran_objetivos_no_cumplidos_se_lo_debera_indicar_expresamente__ri_cc_a5616b
    - Obligacion_si_no_se_obtiene_respuesta_a_las_notificaciones_previas_debe_enviarse_una_comuni_1875b6
    - Obligacion_si_no_se_obtiene_respuesta_a_las_notificaciones_previas_el_administrador_debe_en_7d1c32
    - Obligacion_si_se_trata_de_prestamos_expresados_en_unidades_de_valor_adquisitivo_actualizabl_fe6c76
    - Obligacion_solicitar_al_beneficiario_con_anterioridad_al_pago_certificacion_de_la_firma_del_fe4618
    - Obligacion_solicitar_autorizacion_con_anticipacion_y_por_escrito_a_la_gerencia_de_operacion_67d7c6
    - Obligacion_solicitar_confirmacion_de_saldos_de_deudores_por_prestamos_y_otros_creditos_y_ac_41865e
    - Obligacion_sumar_los_tramos_de_plazos_informados_en_la_posicion_del_mes_anterior_n_1_y_dete_6cebb0
    - Obligacion_sumar_los_tramos_de_plazos_informados_en_la_posicion_del_mes_bajo_informe_n_y_ap_539ab5
    - Obligacion_suministrar_como_minimo_en_todos_los_casos_apellido_s_y_nombre_s_completos_y_doc_a489ae
    - Obligacion_toda_informacion_relacionada_con_la_inscripcion_o_modificacion_de_datos_debera_r_8acb29
    - Obligacion_toda_modificacion_de_domicilio_solo_sera_oponible_a_la_otra_parte_si_mediare_una_9dd626
    - Obligacion_toda_modificacion_en_las_condiciones_pactadas_debera_efectuarse_de_conformidad_c_8640af
    - Obligacion_todas_las_partidas_se_identificaran_segun_su_moneda_de_origen_de_acuerdo_con_la__eab5e5
    - Obligacion_todas_las_tareas_de_administracion_respecto_del_seguimiento_de_los_atrasos_deben_637674
    - Obligacion_todo_el_personal_involucrado_en_el_proceso_de_gestion_del_riesgo_de_credito_debe_635762
    - Obligacion_todos_los_aspectos_de_las_operaciones_comprendidas_no_expresamente_contemplados__03e69c
    - Obligacion_todos_los_caracteres_alfabeticos_deben_ser_informados_en_mayusculas__snp_cheq_7__0b0998
    - Obligacion_todos_los_gastos_e_impuestos_actuales_o_futuros_que_graven_las_operaciones_seran_59f5ab
    - Obligacion_tras_finalizar_el_control_se_debe_proceder_al_escaneo_de_las_etiquetas_y_al_resg_34fe24
    - Obligacion_tras_la_aprobacion_el_modelo_debe_estar_sujeto_a_revision_verificacion_de_proces_c3b7f1
    - Obligacion_un_adecuado_programa_de_control_interno_debe_constar_de_4_componentes_evaluacion_66e1c0
    - Obligacion_un_entorno_de_control_efectivo_requiere_la_separacion_adecuada_de_las_responsabi_fa4493
    - Obligacion_un_marco_de_validacion_eficaz_debe_incluir_evaluacion_de_solidez_conceptual_meto_11d515
    - Obligacion_un_proceso_eficaz_de_evaluacion_y_aprobacion_debe_establecer_los_requisitos_mini_e4d054
    - Obligacion_un_sistema_eficaz_de_seguimiento_del_credito_debe_incluir_medidas_para_asegurar__67bc2c
    - Obligacion_un_sistema_eficaz_de_seguimiento_del_credito_debe_incluir_medidas_para_controlar_629c86
    - Obligacion_un_sistema_eficaz_de_seguimiento_del_credito_debe_incluir_medidas_para_evaluar_l_8d544b
    - Obligacion_un_sistema_eficaz_de_seguimiento_del_credito_debe_incluir_medidas_para_identific_4a56ba
    - Obligacion_un_sistema_eficaz_de_seguimiento_del_credito_debe_incluir_medidas_para_realizar__8e4bfc
    - Obligacion_un_sistema_interno_de_calificacion_de_riesgo_bien_estructurado_debe_clasificar_a_932dd9
    - Obligacion_una_solida_y_efectiva_politica_de_continuidad_del_negocio_requiere_el_compromiso_a7c276
    - Obligacion_una_solida_y_efectiva_politica_de_continuidad_del_negocio_requiere_el_involucram_829b52
    - Obligacion_una_solida_y_efectiva_politica_de_continuidad_del_negocio_requiere_la_revision_p_92dfb1
    - Obligacion_una_solida_y_efectiva_politica_de_continuidad_del_negocio_requiere_su_revision_p_c7ec09
    - Obligacion_una_vez_asignada_la_clave_bancaria_uniforme_por_la_entidad_financiera_es_respons_8d31d5
    - Obligacion_una_vez_determinada_la_relevancia_y_frecuencia_de_revision_de_los_ciclos_y_sucur_c55ea2
    - Obligacion_utilizacion_de_codigos_de_partidas_especificos_segun_el_sub_periodo_de_enero_201_282e7b
    - Obligacion_utilizar_la_letra_m_para_indicar_campos_mandatorios_y_la_letra_o_para_indicar_ca_7051ad
    - Obligacion_utilizar_las_cuentas_especificas_incluidas_en_los_rubros_provisiones_y_creditos__c027d9
    - Obligacion_vencido_el_plazo_de_30_dias_corridos_sin_que_se_haya_cumplido_con_la_adecuacion__d83814
    - Obligacion_verificacion_de_que_no_existan_partidas_pendientes_significativas_que_represente_f3c845
    - Obligacion_verificacion_especial_de_que_no_existan_partidas_pendientes_significativas_que_r_a3d7c2
    - Obligacion_verificar_adicionalmente_que_se_hayan_abonado_en_termino_los_anticipos_correspon_f1aa62
    - Obligacion_verificar_contra_lo_informado_por_la_consulta_si_el_beneficiario_tenedor_es_quie_c54e74
    - Obligacion_verificar_el_cumplimiento_de_lo_dispuesto_en_el_punto_8_4_1__cirmo3_8_9_2_1a5862
    - Obligacion_verificar_el_cumplimiento_de_obligaciones_de_informacion_incluyendo_informes_req_3ec8a2
    - Obligacion_verificar_el_establecimiento_de_un_sector_o_una_funcion_responsable_de_la_gestio_20c2c4
    - Obligacion_verificar_el_proceso_establecido_para_la_gestion_del_registro_y_la_respuesta_de__450204
    - Obligacion_verificar_existencia_y_tasacion_de_garantias_preferidas_recibidas_segmentando_pr_67a520
    - Obligacion_verificar_la_asignacion_formal_de_roles_y_responsabilidades_para_el_directorio_l_17c534
    - Obligacion_verificar_la_existencia_de_un_adecuado_sistema_de_consolidacion_de_deuda_por_pre_cec7d1
    - Obligacion_verificar_la_existencia_de_un_area_o_funcion_de_gestion_de_riesgos_de_tecnologia_34b19c
    - Obligacion_verificar_la_identificacion_y_situacion_fiscal_del_titular_a_base_de_los_documen_076bc4
    - Obligacion_verificar_las_conciliaciones_con_bancos_locales_analizando_las_partidas_pendient_b7c5d8
    - Obligacion_verificar_los_principales_elementos_de_control_de_la_cartera_de_prestatarios__ri_3c33f4
    - Obligacion_verificar_los_saldos_correspondientes_a_cobranzas_y_otras_operaciones_por_cuenta_26aedc
    - Obligacion_verificar_los_saldos_de_partidas_pendientes_de_imputacion_analizando_la_document_0398c5
    - Obligacion_verificar_que_ademas_del_pertinente_endoso_quede_constancia_de_la_transferencia__d71761
    - Obligacion_verificar_que_de_la_situacion_patrimonial_declarada_se_evidencie_la_suficiente_s_0f12f4
    - Obligacion_verificar_que_de_la_situacion_patrimonial_declarada_se_evidencie_la_suficiente_s_6f4a85
    - Obligacion_verificar_que_el_marco_de_gobierno_de_tecnologia_y_seguridad_de_la_informacion_c_25c94b
    - Obligacion_verificar_que_el_proceso_de_gestion_de_cambios_permita_registrar_evaluar_planifi_50dab8
    - Obligacion_verificar_que_exista_designacion_de_un_area_sector_o_responsable_de_la_coordinac_468f37
    - Obligacion_verificar_que_la_amortizacion_contabilizada_durante_el_periodo_sea_razonable__ri_11f72e
    - Obligacion_verificar_que_las_aperturas_funcionamiento_y_cierres_de_las_cuentas_a_la_vista_s_6d673b
    - Obligacion_verificar_que_las_causales_de_rechazos_y_reclamos_sean_validas__snp_cheq_5_2_4_cd55ed
    - Obligacion_verificar_que_las_operaciones_se_liquiden_a_traves_de_entidades_de_contraparte_c_8348d6
    - Obligacion_verificar_que_los_datos_coincidan_entre_la_transaccion_original_y_su_rechazo_aju_3aa15c
    - Obligacion_verificar_que_los_documentos_cedidos_provengan_de_operaciones_de_venta_o_de_pres_08ae96
    - Obligacion_verificar_que_los_planes_de_continuidad_del_negocio_respondan_a_las_estrategias__d058af
    - Obligacion_verificar_que_los_plazos_de_rechazos_ajustes_y_reclamos_sean_validos__snp_cheq_5_a5fea7
    - Obligacion_verificar_que_no_existan_saldos_sin_asignacion_especifica_a_los_prestatarios_de__ab4b87
    - Obligacion_verificar_que_no_se_hayan_activado_partidas_que_no_correspondan_de_acuerdo_con_l_4df046
    - Obligacion_verificar_que_se_establezcan_medidas_proactivas_en_el_diseno_de_operaciones_y_pr_68964e
    - Obligacion_verificar_que_se_realicen_evaluaciones_periodicas_de_los_riesgos_de_escenarios_d_71489b
    - Obligacion_vigilancia_de_los_limites_para_evitar_concentraciones_en_las_posiciones_de_titul_d541b4
Operacion: 2356 sin aplica_a
    - Operacion_abastecimiento_de_billetes__cirmo3_5_2_1_77cc29
    - Operacion_abono_a_entidad_depositaria__snp_cheq_2_2_2_2_6eb839
    - Operacion_abono_de_remuneraciones_a_trabajadores_no_alcanzados_por_regimen_legal__depaho_2_17d916
    - Operacion_acceso_a_datos_de_echeq_y_documentos_compensables__snp_cheq_8_4_1_14_bbb98c
    - Operacion_acceso_a_documentacion_de_respaldo__expaef_9_6_1_322c01
    - Operacion_acceso_a_sistemas_informaticos_y_registros__expaef_9_6_1_df2fc4
    - Operacion_acceso_indirecto_a_sistema_de_pagos_de_alto_valor__lingeef_3_5_5_3_2ba6ae
    - Operacion_acciones_correctivas_en_transferencia_fallida__snp_tr_2_2_13_66deb3
    - Operacion_acciones_para_proteger_el_inmueble__manori_sbloque4_a759a1
    - Operacion_acondicionamiento_de_billetes_en_buen_uso__cirmo3_5_1_3_1_98b1fe
    - Operacion_acreditacion_de_beneficios_de_asignacion_universal__depaho_3_5_3_d71cad
    - Operacion_acreditacion_de_depositos_cuenta_gratuita_universal__depaho_3_11_4_1_0e9689
    - Operacion_acreditacion_de_financiacion_de_exportaciones__depaho_3_14_3_b09671
    - Operacion_acreditacion_de_fondos_cedip_al_vencimiento__snp_cheq_3_6_4_1_6_5ba8fb
    - Operacion_acreditacion_de_fondos_cedip_tras_presentacion_al_cobro__snp_cheq_3_6_4_1_6_1c03dc
    - Operacion_acreditacion_de_fondos_en_ce_pro_ar__depaho_4_23_2_6188e7
    - Operacion_acreditacion_de_fondos_en_cecon_ar__depaho_4_22_2_02a159
    - Operacion_acreditacion_de_fondos_en_cuenta_sueldo_o_seguridad_social__depaho_2_2_4253c3
    - Operacion_acreditacion_de_fondos_por_transferencias_electronicas__depaho_3_9_2_2_a24d2e
    - Operacion_acreditacion_de_fondos_repatriados__depaho_4_20_1_0129cc
    - Operacion_acreditacion_de_fondos_repatriados_en_caja_de_ahorros__depaho_4_19_1_ada5ef
    - Operacion_acreditacion_de_importe_en_cuenta_corriente_billetes_legitimos__cirmo3_4_1_2_d93562
    - Operacion_acreditacion_de_importes_en_pesos_por_liquidacion_de_divisas__depaho_3_13_3_7_df97aa
    - Operacion_acreditacion_de_importes_judiciales__depaho_3_6_3_8b6a3b
    - Operacion_acreditacion_de_importes_netos_en_pesos__depaho_3_13_3_6_9993ab
    - Operacion_acreditacion_de_importes_netos_en_pesos__depaho_3_13_3_8_823572
    - Operacion_acreditacion_de_importes_netos_en_pesos_actividad_agricola__depaho_3_12_3_3_2a1fb9
    - Operacion_acreditacion_de_importes_netos_en_pesos_ventas_decreto_194_23__depaho_3_12_3_4_2c2692
    - Operacion_acreditacion_de_monto_de_regularizacion_en_cuenta_especial__depaho_3_16_1_943633
    - Operacion_acreditacion_de_pesos_por_liquidacion_de_divisas__depaho_3_13_3_4_c66446
    - Operacion_acreditacion_de_prestaciones_de_ayuda_social_jurisdicciones_provinciales__depaho_5cde86
    - Operacion_acreditacion_de_prestamos_precalificados_atm_autoservicio__expaef_4_5_1_1_7580df
    - Operacion_acreditacion_de_producido_en_pesos_de_fondos_en_moneda_extranjera__depaho_4_22_2_d7e1a1
    - Operacion_acreditacion_de_reintegros_y_prestaciones_de_salud__depaho_2_3_1_fd459d
    - Operacion_acreditacion_de_remuneraciones_normales_y_habituales__depaho_2_3_1_96ca28
    - Operacion_acreditacion_de_resultados_de_inversiones__depaho_3_16_2_5eb98c
    - Operacion_acreditacion_diaria_de_retribucion__depaho_3_12_4_c94f92
    - Operacion_acreditacion_diaria_de_retribucion__depaho_3_13_5_6403b9
    - Operacion_acreditacion_en_cuenta_a_la_vista_suplemento_excepcional__depaho_5_1_b97849
    - Operacion_acreditacion_en_cuenta_de_menor__depaho_3_10_3_cbad5d
    - Operacion_acreditacion_en_cuenta_especial_repatriacion__depaho_4_21_2_7634a2
    - Operacion_acreditacion_en_pesos_de_liquidaciones_en_mercado_de_cambios__depaho_3_12_3_5_980a3f
    - Operacion_acreditacion_en_pesos_de_pagos_a_no_residentes__depaho_3_12_3_5_123087
    - Operacion_acreditacion_en_pesos_de_pagos_de_intereses_no_cursados__depaho_3_12_3_5_4890c5
    - Operacion_acreditacion_importe_cheques_no_rechazados__snp_cheq_3_2_5_fb42fd
    - Operacion_acreditacion_mediante_deposito_en_efectivo__depaho_3_16_2_fc6c29
    - Operacion_acreditacion_mediante_transferencias__depaho_3_16_2_56a8c0
    - Operacion_acreditacion_mensual_de_interes__depaho_3_14_5_1bd595
    - Operacion_acreditacion_por_promociones_de_la_entidad__depaho_3_11_4_2_f433b1
    - Operacion_acreditacion_por_reintegros_fiscales__depaho_3_11_4_2_ba6641
    - Operacion_acreditacion_por_venta_tarjeta_alimentar__depaho_3_11_4_2_bc5167
    - Operacion_acreditaciones_en_cuenta_especial_repatriacion__depaho_4_20_2_c81ef8
    - Operacion_acreditaciones_en_repatriacion_de_fondos__depaho_4_19_2_bbf252
    - Operacion_acreditaciones_segun_punto_3_5_3__depaho_3_5_4_189901
    - Operacion_actividades_de_titulizacion__lingeef_7_1_1_86e09a
    - Operacion_actualizacion_de_tasacion_del_inmueble__manori_1_2_4_5b9c0f
    - Operacion_actuar_como_cajas_de_credito_cooperativas__cajasc_1_2_1_4c293a
    - Operacion_acuerdo_de_interes_en_financiacion__cajasc_4_2_3_7600eb
    - Operacion_acuerdo_de_tasa_de_interes__efemin_6_5_1_73e032
    - Operacion_acuerdos_de_margen_derivados_otc__lingeef_2_5_2_9fb166
    - Operacion_acunacion_de_monedas_conmemorativas_1978__cirmo3_7_16_b5d502
    - Operacion_acunacion_de_monedas_por_fabrica_nacional_de_moneda_y_timbre_de_espana__cirmo3_7_3cda5c
    - Operacion_acunacion_moneda_conmemorativa_casa_de_moneda__cirmo3_7_13_44e367
    - Operacion_acunacion_moneda_cuproniquel_2_circulacion__cirmo3_7_24_84a063
    - Operacion_acunacion_moneda_cuproniquel_2_estriado__cirmo3_7_24_537bc8
    - Operacion_acunacion_moneda_oro_999_copa_mundial_fifa_2026__cirmo3_7_53_779492
    - Operacion_acunacion_moneda_oro_malvinas__cirmo3_7_25_c43cae
    - Operacion_acunacion_moneda_plata_925_25__cirmo3_7_39_d0fec1
    - Operacion_acunacion_moneda_plata_925_25__cirmo3_7_45_3546e0
    - Operacion_acunacion_moneda_plata_925_copa_mundial_fifa_2026__cirmo3_7_53_5b3788
    - Operacion_acunacion_moneda_plata_malvinas__cirmo3_7_25_824818
    - Operacion_adhesion_a_servicios_de_debito_directo__depaho_1_12_7d397b
    - Operacion_adhesion_a_sistemas_de_debito_automatico__depaho_3_4_9_9acb73
    - Operacion_adjuncion_de_copia_del_contrato__expaef_2_2_3_4_1ed874
    - Operacion_administracion_credito_prendario_automotor__manori_3_3_1_c4fd40
    - Operacion_administracion_de_flujos_de_fondos__lingeef_3_1_2_1_1f8045
    - Operacion_administracion_del_acceso_a_los_mercados__lingeef_3_1_2_5_5beb6e
    - Operacion_administracion_del_sca__snp_cheq_3_5_2_3_40059d
    - Operacion_administracion_del_sca__snp_cheq_3_5_2_4_5aedee
    - Operacion_administracion_del_sce__snp_cheq_3_6_2_2_54aa5d
    - Operacion_administracion_del_sce__snp_cheq_3_6_7_1_92c039
    - Operacion_admision_de_depositos_en_pesos_de_liquidacion_de_divisas__depaho_3_12_3_7_049073
    - Operacion_adopcion_de_mecanismos_para_gestion_de_cedip__snp_cheq_3_6_3_1_33c34c
    - Operacion_adopcion_de_medidas_por_autoridades_del_pais_de_radicacion__expaef_1_6_1_1_86e11f
    - Operacion_adopcion_del_valor_razonable_activos__ri_dcpc_3_1_3_3_d231fb
    - Operacion_adquisicion_automotores_nuevos_alquiler__manori_3_1_5_1_557e97
    - Operacion_adquisicion_automotores_nuevos_uso_comercial__manori_3_1_5_1_5aeca9
    - Operacion_adquisicion_automotores_nuevos_uso_particular__manori_3_1_5_1_bf368a
    - Operacion_adquisicion_de_bienes_muebles_para_inversion_productiva__depaho_3_16_3_3_075594
    - Operacion_adquisicion_de_participacion_significativa__adrei_2_1_2_2_947dea
    - Operacion_adquisicion_de_titulos_valores_publicos_y_privados__depaho_3_8_8_1_4f5ac3
    - Operacion_adquisicion_vivienda_no_permanente__manori_1_1_5_1_263597
    - Operacion_adquisicion_vivienda_permanente__manori_1_1_5_1_53ad39
    - Operacion_agregacion_de_datos_de_riesgos_por_criterios_especificos__adrei_3_4_1_5_8bc988
    - Operacion_agregacion_de_datos_sobre_riesgos__adrei_2_1_2_1_e9f3c4
    - Operacion_agregacion_de_datos_sobre_riesgos__adrei_2_1_42799c
    - Operacion_agregacion_de_datos_sobre_riesgos_a_nivel_consolidado__adrei_2_1_2_3_2bf7d9
    - Operacion_agregacion_de_datos_sobre_riesgos_a_nivel_individual__adrei_2_1_2_3_cf8c85
    - Operacion_agregacion_de_informaciones_compromisos_y_documentacion__expaef_2_2_3_5_9bbfe6
    - Operacion_agregacion_de_partidas_de_disminucion_incremento_de_exigencia__ri_rml_1_2_4_749eb6
    - Operacion_agregacion_de_perdidas_eve_por_escenario__lingeef_5_4_4_2be750
    - Operacion_agregacion_flexible_de_datos_de_riesgos__adrei_3_4_1_1_e1a06e
    - Operacion_agregacion_validacion_y_conciliacion_de_datos_sobre_riesgos__adrei_3_1_1_5_9723b7
    - Operacion_ajuste__snp_cheq_7_1_9_adba07
    - Operacion_ajuste_comisiones_fondos_inmovilizados_cedip__snp_cheq_7_2_3_0bab5e
    - Operacion_ajuste_comisiones_por_fondos_inmovilizados__snp_cheq_6_2_1_9eb0db
    - Operacion_ajuste_de_cheques__snp_cheq_7_1_3_a2d1a1
    - Operacion_ajuste_de_importe_de_cheque__snp_cheq_3_1_2_5_f6cddd
    - Operacion_ajuste_de_importe_en_libros_de_partidas_cubiertas__ri_dcpc_3_4_3_1_8c5bf0
    - Operacion_ajuste_motivos_varios_cedip__snp_cheq_7_2_3_42aef6
    - Operacion_ajuste_por_interes__snp_cheq_6_2_1_40a2f0
    - Operacion_ajuste_por_interes_cedip__snp_cheq_7_2_3_d14a5b
    - Operacion_ajuste_por_motivos_varios__snp_cheq_6_2_1_4f855a
    - Operacion_ajuste_por_presentacion_fuera_de_termino__snp_cheq_6_2_1_4f9806
    - Operacion_ajuste_por_rechazo_fuera_de_termino__snp_cheq_6_2_1_ef4d51
    - Operacion_ajuste_presentacion_fuera_de_termino_cedip__snp_cheq_7_2_3_f56694
    - Operacion_ajuste_rechazo_fuera_de_termino_cedip__snp_cheq_7_2_3_a7734c
    - Operacion_alarma_a_distancia_policial_o_empresa_seguridad__ri_mmsef_2_2_4_d2f371
    - Operacion_alarma_local__ri_mmsef_2_2_7_cfec0b
    - Operacion_alarma_propia_en_recinto_remoto__ri_mmsef_2_2_5_874c15
    - Operacion_alquiler_de_cajas_de_seguridad__depaho_1_10_1_5ba775
    - Operacion_alquiler_de_cajas_de_seguridad__depaho_3_4_8_1_be918e
    - Operacion_amortizacion_aleman_credito_hipotecario__manori_sbloque4_59a439
    - Operacion_amortizacion_anticipada__lingeef_7_3_3_5_21e7bc
    - Operacion_amortizacion_anticipada_de_titulizacion__lingeef_7_3_3_3_fd40ba
    - Operacion_amortizacion_anticipada_por_nivel_de_rendimiento_diferencial__lingeef_7_3_3_4_e5497a
    - Operacion_amortizacion_de_ajustes_por_cobertura_en_instrumentos_a_costo_amortizado__ri_dcp_809f28
    - Operacion_amortizacion_frances_credito_hipotecario__manori_sbloque4_4e5257
    - Operacion_analisis_de_concentraciones_en_titulizaciones__lingeef_7_2_4_34ccd8
    - Operacion_analisis_de_descalces_de_liquidez__lingeef_3_3_2_5aca5c
    - Operacion_analisis_de_escenarios_de_riesgo_operacional__lingeef_6_3_1_2_5243ec
    - Operacion_analisis_de_supuestos_y_datos_de_entrada__lingeef_1_4_4_5_75ae2e
    - Operacion_analisis_de_variaciones__ri_ccna_d1a3l1_sa_3_c5fa28
    - Operacion_analisis_del_riesgo_crediticio_de_titulizaciones__lingeef_7_2_4_560d59
    - Operacion_analisis_estatico_de_recaudacion_de_efectivo__lingeef_7_3_3_6_74fe6f
    - Operacion_analisis_respuestas_confirmaciones__ri_ccna_d1a3l2_s19_423999
    - Operacion_analisis_respuestas_confirmaciones_deudores__ri_ccna_d1a3l2_s8_e4f816
    - Operacion_analisis_seguridad_teleprocesamiento__ri_ccna_d2a2_3_4_4_c67e22
    - Operacion_anotaciones_en_hoja_movil__depaho_3_1_7_6_35db2e
    - Operacion_apertura_automatica_subcuenta_60_efectivo_minimo__efemin_2_1_6_d4a536
    - Operacion_apertura_de_caja_de_ahorros_para_ayuda_social__depaho_3_5_1_cecaa8
    - Operacion_apertura_de_caja_de_ahorros_para_menores_autorizados__depaho_3_7_1_fbd22a
    - Operacion_apertura_de_caja_de_ahorros_por_menores__depaho_3_10_1_ae1711
    - Operacion_apertura_de_cuenta__depaho_3_1_9_1_a119cc
    - Operacion_apertura_de_cuenta_a_nombre_de_suscriptores__depaho_3_2_2_03a7bd
    - Operacion_apertura_de_cuenta_a_nombre_del_beneficiario__depaho_2_2_2_2_63c424
    - Operacion_apertura_de_cuenta_a_nombre_del_beneficiario__depaho_2_2_2_3_a452ff
    - Operacion_apertura_de_cuenta_a_nombre_del_trabajador__depaho_3_1_2_624a40
    - Operacion_apertura_de_cuenta_corriente_operativa_para_cec__snp_tr_1_2_1_12c72b
    - Operacion_apertura_de_cuenta_de_seguridad_social_a_nombre_del_beneficiario__depaho_2_2_2_1_b4215e
    - Operacion_apertura_de_cuenta_electoral_de_alianza__depaho_4_18_1_2_1e9476
    - Operacion_apertura_de_cuenta_especial_cecon_ar__depaho_4_22_1_a1adb1
    - Operacion_apertura_de_cuenta_especial_de_deposito__depaho_4_23_1_048c2e
    - Operacion_apertura_de_cuenta_especial_de_inversion__depaho_3_8_1_254782
    - Operacion_apertura_de_cuenta_especial_de_inversion__depaho_3_8_5_96f9f9
    - Operacion_apertura_de_cuenta_especial_de_regularizacion_de_activos__depaho_3_16_1_5390ff
    - Operacion_apertura_de_cuenta_especial_economia_del_conocimiento__depaho_3_15_1_9d3850
    - Operacion_apertura_de_cuenta_especial_en_dolares_estadounidenses__depaho_3_15_2_c58f94
    - Operacion_apertura_de_cuenta_especial_para_exportadores_en_pesos__depaho_3_13_2_26f70a
    - Operacion_apertura_de_cuenta_especial_repatriacion__depaho_4_20_1_15c194
    - Operacion_apertura_de_cuenta_especial_repatriacion__depaho_4_21_1_bc3d84
    - Operacion_apertura_de_cuenta_fondo_cese_laboral_colectivo__depaho_3_17_2_4ca4a4
    - Operacion_apertura_de_cuenta_gratuita_universal__depaho_3_11_a2b35b
    - Operacion_apertura_de_cuenta_individual_fondo_de_cese_laboral__depaho_3_17_1_1f96e1
    - Operacion_apertura_de_cuenta_no_presencial__depaho_4_16_2_021795
    - Operacion_apertura_de_cuenta_personas_humanas__depaho_4_1_1_37547a
    - Operacion_apertura_de_cuenta_por_persona_humana_o_juridica_para_recibir_transferencias__de_8c58c5
    - Operacion_apertura_de_cuenta_sueldo__depaho_2_1_232faf
    - Operacion_apertura_de_cuenta_sueldo_nominada_en_pesos__depaho_2_2_1_4a378e
    - Operacion_apertura_de_cuentas_corrientes_especiales__depaho_3_4_3_d25425
    - Operacion_apertura_de_cuentas_corrientes_o_a_la_vista__cajasc_11_2_792920
    - Operacion_apertura_de_cuentas_corrientes_o_a_la_vista_en_bancos_comerciales__cajasc_6_2_1__b4f7fe
    - Operacion_apertura_de_cuentas_corrientes_para_integracion_de_efectivo_minimo__efemin_2_1_4_6b27e9
    - Operacion_apertura_de_cuentas_especiales_de_depositos__depaho_3_17_fff088
    - Operacion_apertura_de_cuentas_especiales_de_depositos__depaho_3_1_1_60584b
    - Operacion_apertura_de_cuentas_especiales_financiacion_de_exportaciones_en_usd__depaho_3_14_220b47
    - Operacion_apertura_de_cuentas_especiales_moneda_pesos__depaho_3_12_2_1b2a45
    - Operacion_apertura_de_cuentas_especiales_para_circulos_cerrados__depaho_3_2_1_cb0aa1
    - Operacion_apertura_de_cuentas_especiales_titulares_agricolas__depaho_3_12_1_3_dc870a
    - Operacion_apertura_de_dependencias_automatizadas_por_personal_ajeno__expaef_4_5_2_4_add1c4
    - Operacion_apertura_de_legajo_del_deudor__cajasc_4_3_1_1_13d4e0
    - Operacion_apertura_de_legajo_del_firmante_en_creditos_cedidos__cajasc_4_3_1_1_6d01a8
    - Operacion_apertura_de_oficinas_de_representacion_en_el_exterior__expaef_5_3_30f961
    - Operacion_apertura_de_sucursales_de_entidades_financieras_del_exterior__ayccef_2_3_4_0a4f0b
    - Operacion_apertura_de_sucursales_en_el_exterior__expaef_1_2_866c7f
    - Operacion_apertura_no_presencial_de_cuentas__depaho_4_16_1_318bec
    - Operacion_apertura_remota_y_presencial_de_cgu__efemin_7_7_e016be
    - Operacion_apertura_y_funcionamiento_de_sucursal_en_el_exterior__expaef_1_2_1_cdbb32
    - Operacion_apertura_y_mantenimiento_de_cuenta__depaho_3_5_4_34ec85
    - Operacion_aplanamiento_de_la_pendiente__lingeef_5_4_5_994936
    - Operacion_aplicacion_de_disposiciones_cuenta_corriente_especial_para_personas_juridicas__d_14ad17
    - Operacion_aplicacion_de_disposiciones_de_cuentas_corrientes_especiales__depaho_3_12_5_6af684
    - Operacion_aplicacion_de_disposiciones_de_depositos_en_caja_de_ahorros__depaho_3_10_9_94a276
    - Operacion_aplicacion_de_disposiciones_de_depositos_en_caja_de_ahorros__depaho_3_12_5_6b47fa
    - Operacion_aplicacion_de_disposiciones_depositos_en_caja_de_ahorros__depaho_4_22_4_e8e582
    - Operacion_aplicacion_de_indemnizacion_al_pago_de_obligaciones__manori_sbloque4_45cc4b
    - Operacion_aplicacion_de_limites_de_riesgo_agregado_consolidados__lingeef_5_3_2_2_024b07
    - Operacion_aplicacion_del_metodo_de_revaluacion__ri_dcpc_4_1_2_0fa186
    - Operacion_aplicacion_disposiciones_cuentas_corrientes_especiales__depaho_3_13_6_4f6c80
    - Operacion_aplicacion_disposiciones_depositos_caja_de_ahorros__depaho_3_13_6_772fb6
    - Operacion_aplicacion_margen_cobertura_80_a_tasacion__cajasc_9_5_2_3_972cf8
    - Operacion_aplicacion_metodologia_ajuste_por_inflacion__ri_dcpc_7_1_1e7aab
    - Operacion_aplicacion_supletoria_cuentas_corrientes_especiales_para_personas_juridicas__dep_dc147b
    - Operacion_aplicacion_supletoria_depositos_en_caja_de_ahorros__depaho_3_14_6_0569cf
    - Operacion_aporte_adicional_20_cajas_de_credito_cooperativas__cajasc_11_1_2_5ee3e0
    - Operacion_aporte_de_capital__cajasc_2_8_e028a3
    - Operacion_aporte_de_capital_por_asociados_no_radicados__cajasc_1_3_5_4_0ed839
    - Operacion_aporte_normal_cajas_de_credito_cooperativas__cajasc_11_1_2_7f3de7
    - Operacion_aportes_adicionales_del_trabajador__depaho_3_17_1_0d6bd8
    - Operacion_aprobacion_de_estados_financieros_con_activos_y_pasivos_a_valor_razonable__ri_dc_e7038c
    - Operacion_aprobacion_de_estrategia_de_gestion_de_riesgo_de_mercado__lingeef_4_2_1_1_d2eaac
    - Operacion_aprobacion_de_proyecto_de_transformacion__ayccef_4_3_1_01ee9c
    - Operacion_archivo_de_actuaciones_sin_mas_tramite__ayccef_2_8_2_161ef9
    - Operacion_archivo_de_bajas_de_inhabilitados__ceninf_3_2_2_8467d7
    - Operacion_arqueo_sorpresivo_de_documentos_y_garantias__ri_ccna_d1a3l2_s9_35ad0d
    - Operacion_arqueo_sorpresivo_de_efectivo_en_tesoro__ri_ccna_d1a3l2_s1_d07335
    - Operacion_arqueo_sorpresivo_de_inversiones__ri_ccna_d1a3l2_s4_59113f
    - Operacion_arqueo_sorpresivo_de_valores_en_custodia__ri_ccna_d1a3l2_s31_45afcd
    - Operacion_arqueos_de_efectivo_y_valores__nmcief_a3_s1_4f98a7
    - Operacion_arrendamiento_financiero_de_inmuebles_para_vivienda__cajasc_5_5_12_3_2a008d
    - Operacion_arrendamiento_financiero_inmueble_vivienda_propia__cajasc_5_5_12_407ea1
    - Operacion_arrendamiento_financiero_vehiculos_automotores_y_maquinas_agricolas__cajasc_5_5__7a78be
    - Operacion_asesoramiento_en_servicios_y_operaciones__expaef_3_2_3dd91a
    - Operacion_asignacion_a_bandas_temporales_predefinidas__lingeef_5_4_1_df44dc
    - Operacion_asignacion_a_puntos_medios_de_bandas_temporales__lingeef_5_4_1_8a599d
    - Operacion_asignacion_de_capital_economico_riesgo_de_credito_titulizaciones_rotativas__ling_53ee24
    - Operacion_asignacion_de_capital_inicial_a_sucursal__expaef_1_2_7_c31a19
    - Operacion_asignacion_de_casa_de_la_entidad__expaef_4_5_3_1_94730d
    - Operacion_asignacion_de_clasificacion_de_deudores__cajasc_9_2_1_b77c6a
    - Operacion_asignacion_de_flujos_a_bandas_temporales__lingeef_5_4_2_32d8c4
    - Operacion_asignacion_de_flujos_a_bandas_temporales_tasa_fija__lingeef_5_4_2_1_43521b
    - Operacion_asignacion_de_flujos_a_bandas_temporales_tasa_variable__lingeef_5_4_2_1_027a0e
    - Operacion_asignacion_de_margenes_de_financiacion_mediante_screening_y_credit_scoring__caja_3bd044
    - Operacion_asignacion_de_numero_a_cuenta_especial__depaho_3_1_8_2_658018
    - Operacion_asistencia_crediticia_que_excede_margenes_de_cobertura__cajasc_7_4_ca22c0
    - Operacion_asuncion_de_obligaciones_eventuales__cajasc_7_6_3_906097
    - Operacion_atribucion_de_flujos_nocionales_a_bandas_temporales__lingeef_5_4_4_1_5f2a74
    - Operacion_auditoria_de_transacciones__snp_tr_2_3_2_7_a46593
    - Operacion_auditoria_independiente_de_procesos_rtici__lingeef_5_3_1_3_0dd6ee
    - Operacion_auditoria_interna_del_sistema_de_gestion_de_riesgo_de_contraparte__lingeef_2_4_6_c9faef
    - Operacion_aumento_de_integracion_de_capital__lingeef_5_6_ce32b8
    - Operacion_aumento_de_tasas_de_corto_plazo__lingeef_5_4_5_4403d9
    - Operacion_aumentos_significativos_del_costo_de_captacion__lingeef_3_3_4_12_6cd8ca
    - Operacion_autoevaluacion_de_riesgos_operacionales__lingeef_6_3_1_2_75f8f4
    - Operacion_autorizacion_del_bcra_tesoro_modular__ri_mmsef_2_2_8_3_1_b2749f
    - Operacion_aval_de_fcem__snp_cheq_3_5_2_2_3238da
    - Operacion_baja_de_cheques_actualizacion_de_registro__ceninf_1_1_2_1_f33700
    - Operacion_baja_de_cheques_cancelados_15_dias__ceninf_1_3_2a0aed
    - Operacion_baja_de_cheques_cancelados_16_a_90_dias__ceninf_1_3_2693b9
    - Operacion_baja_de_cheques_no_cancelados__ceninf_1_3_74e550
    - Operacion_baja_de_cheques_pagados_91_dias_o_mas__ceninf_1_3_eb169c
    - Operacion_baja_de_cheques_rechazados_criterios_de_pago_de_multas__ceninf_1_3_d98ed5
    - Operacion_baja_o_modificacion_sustancial_pasivos_financieros__ri_dcpc_3_2_2_1_668579
    - Operacion_base_de_datos_de_eventos_de_riesgo_operacional__lingeef_6_3_1_2_9baf6a
    - Operacion_blindaje_o_revestimiento_de_recinto_de_seguridad__ri_mmsef_2_2_3_3_f04bb5
    - Operacion_blindaje_revestimiento_castillete__ri_mmsef_2_2_2_3_a4c669
    - Operacion_boleto_de_compraventa_inmueble_de_emprendimiento__cajasc_5_2_5_8_6bf28f
    - Operacion_cabecera_de_archivo__snp_cheq_sbloque10_864be1
    - Operacion_cabecera_de_archivo_cheques__snp_cheq_7_1_1_65ee0c
    - Operacion_cabecera_de_archivo_identificacion_de_origen__snp_tr_1_6_2_1_17d883
    - Operacion_cabecera_de_lote__snp_cheq_sbloque10_84db78
    - Operacion_cabecera_de_lote_identificacion_de_entidades__snp_tr_1_6_2_2_ab5f7e
    - Operacion_cabecera_de_lote_indicacion_de_fecha_de_compensacion__snp_tr_1_6_2_2_a09a89
    - Operacion_calculo_capital_economico_metodologia_simplificada__lingeef_1_3_3_86812e
    - Operacion_calculo_cuota_periodica_sistema_frances__manori_3_1_5_8_99a23f
    - Operacion_calculo_cuota_sistema_aleman_tasa_fija__manori_3_1_6_4_baa108
    - Operacion_calculo_cuota_sistema_aleman_tasa_variable__manori_3_1_6_4_4573d9
    - Operacion_calculo_cuota_sistema_frances_tasa_fija__manori_3_1_6_4_c840ae
    - Operacion_calculo_cuota_sistema_frances_tasa_variable__manori_3_1_6_4_d11931
    - Operacion_calculo_de_ampliacion_del_exceso_admitido_aea__ri_pgn_6_4_e0eb6c
    - Operacion_calculo_de_cargo_por_exceso__ri_pgn_4_2_9df6b9
    - Operacion_calculo_de_cargos_por_defecto_de_integracion_minima__ri_rml_1_7_1_1db38b
    - Operacion_calculo_de_componente_por_opciones_automaticas__lingeef_5_4_3_694563
    - Operacion_calculo_de_cuota_mensualizada__manori_3_1_6_3_0d86e6
    - Operacion_calculo_de_cuota_periodica_sistema_frances__manori_1_1_5_8_b20115
    - Operacion_calculo_de_deduccion_por_retiros_de_cajeros__ri_rml_1_2_4_94b773
    - Operacion_calculo_de_deuda_externa_total_y_corto_plazo__lingeef_2_6_2_2_532b7d
    - Operacion_calculo_de_diferencia_de_cotizacion_de_moneda_extranjera__ri_dcpc_3_3_b300f6
    - Operacion_calculo_de_disminucion_incremento_de_exigencia_en_promedio__ri_rml_1_2_4_ef8da1
    - Operacion_calculo_de_eni_por_moneda_instrumento__ri_rml_1_4_f40154
    - Operacion_calculo_de_ingresos_computables_mensualizacion__manori_1_1_6_3_32a3c0
    - Operacion_calculo_de_ingresos_computables_mensualizacion__manori_3_1_6_3_042425
    - Operacion_calculo_de_ingresos_computables_sumatoria__manori_3_1_6_3_8682c5
    - Operacion_calculo_de_ingresos_computables_sumatoria_neta__manori_1_1_6_3_11b302
    - Operacion_calculo_de_ingresos_netos_con_deducciones__manori_1_1_6_5_38f3ce
    - Operacion_calculo_de_intereses_con_divisor_fijo__manori_1_1_5_6_b7de75
    - Operacion_calculo_de_intereses_divisor_360_dias__manori_3_1_5_6_236126
    - Operacion_calculo_de_perdida_eve_por_moneda__lingeef_5_4_4_4dfba6
    - Operacion_calculo_de_posiciones_de_liquidez__lingeef_3_3_5_2_6b0525
    - Operacion_calculo_de_posiciones_de_liquidez_intradiaria_y_diaria__lingeef_3_3_5_5_161e24
    - Operacion_calculo_de_proporcion_de_exigencia__efemin_2_5_ed5d78
    - Operacion_calculo_de_tasa_de_interes_efectiva_anual__depaho_4_4_6_6f6df6
    - Operacion_calculo_de_variacion_de_valor_de_opcion_automatica__lingeef_5_4_3_1_913af6
    - Operacion_calculo_de_variacion_de_valor_de_opcion_automatica_comprada__lingeef_5_4_3_2_235c99
    - Operacion_calculo_de_variacion_eve_por_moneda_y_escenario__lingeef_5_4_4_4_b09483
    - Operacion_calculo_del_aporte_al_fondo_de_garantia__ri_rml_s2_6edb17
    - Operacion_calculo_del_importe_total_a_acreditar_del_cedip__snp_cheq_3_6_4_3_601328
    - Operacion_calculo_eve_moneda_escenario__lingeef_5_4_4_3_f1464d
    - Operacion_calculo_exigencia_capital_minimo_riesgo_operacional__cajasc_2_6_2_a14ec7
    - Operacion_calculo_exigencia_depositos_a_plazo_codigo_903200_m__ri_rml_1_9_1_96a7bd
    - Operacion_calculo_exigencia_depositos_a_plazo_fijo_titulos_valores_codigo_905000_tp__ri_rm_621d6f
    - Operacion_calculo_exigencia_minima_depositos_plazo__ri_rml_sbloque13_e32655
    - Operacion_calculo_exigencia_minima_diaria__ri_rml_sbloque13_83853b
    - Operacion_calculo_exigencia_minima_diaria_mayo_2024__ri_rml_sbloque14_b3407a
    - Operacion_calculo_exigencia_moneda_extranjera_codigo_903000_m__ri_rml_1_9_1_012ff4
    - Operacion_calculo_exigencia_moneda_extranjera_codigo_907000_m__ri_rml_1_9_1_b89591
    - Operacion_calculo_exigencia_pesos_codigo_903000_001__ri_rml_1_9_1_ab4fb7
    - Operacion_calculo_exigencia_pesos_codigo_907000_001__ri_rml_1_9_1_15614b
    - Operacion_calculo_exigencia_promedio_grupo_a__ri_rml_sbloque14_10d0da
    - Operacion_calculo_exposicion_bruta_sin_cobertura__ri_gerc_2_4_1_1bed88
    - Operacion_calculo_ingresos_netos_con_deducciones__manori_3_1_6_5_4c5d85
    - Operacion_calculo_integracion_total_codigo_904000_m__ri_rml_1_9_1_3fca19
    - Operacion_calculo_integracion_total_titulos_valores_codigo_906000_tp__ri_rml_1_9_1_1b62c3
    - Operacion_calculo_margen_cobertura_titulos_privados__cajasc_5_5_9_49f8f0
    - Operacion_calculo_medida_riesgo_opcion_automatica_tasas_interes__lingeef_5_4_3_3_624ff2
    - Operacion_calculo_partida_760001_primer_subperiodo_agosto__ri_rml_s6_a938e7
    - Operacion_calculo_partida_760002_segundo_subperiodo__ri_rml_s6_c4c62f
    - Operacion_calculo_partida_760003_exceso_defecto_ajustado__ri_rml_s6_a4e89a
    - Operacion_calculo_posicion_001_por_moneda__ri_rml_1_9_2_1934f9
    - Operacion_calculo_posicion_m_por_moneda_extranjera__ri_rml_1_9_2_31400e
    - Operacion_calculo_posicion_tpnyrm_tp__ri_rml_1_9_2_94d5bd
    - Operacion_calculo_promedio_excesos_defectos_segundo_subperiodo__ri_rml_s6_14f8c6
    - Operacion_calculo_relacion_total_cuotas_ingresos__manori_1_1_8_2_77dd9d
    - Operacion_calculo_rtici_opciones_automaticas_explicitas__lingeef_5_4_2_2_f2df89
    - Operacion_calculo_rtici_opciones_automaticas_implicitas_separadas__lingeef_5_4_2_2_f67b4c
    - Operacion_calculo_y_vigilancia_de_riesgos_de_titulizacion__lingeef_7_3_3_1_e013a3
    - Operacion_calibracion_de_equipos_clasificadores__cirmo3_5_1_2_3_e2e035
    - Operacion_cambio_de_clase_de_entidad_financiera__ayccef_4_1_fe778d
    - Operacion_cambio_de_domicilio_de_oficina__expaef_5_7_1_3_e1b9fe
    - Operacion_cambio_de_domicilio_de_sucursal__expaef_1_6_1_3_88ac53
    - Operacion_cambio_de_numerario_al_publico__cirmo3_3_1_1_cf787a
    - Operacion_cambio_de_titularidad_de_participaciones__expaef_6_5_5_2ab2bf
    - Operacion_campana_de_difusion_masiva_neutralizacion_de_billetes__cirmo3_3_4_2_281145
    - Operacion_cancelacion_de_compras_con_debito_o_transferencia_previa__depaho_3_12_3_9_b7f82b
    - Operacion_cancelacion_de_compras_debito_o_transferencia_previa__depaho_3_12_3_4_9ff10c
    - Operacion_cancelacion_de_fcem_en_moneda_extranjera__snp_cheq_3_5_4_4_bb14ce
    - Operacion_cancelacion_de_saldos_de_cuentas_de_resultados__ri_dcpc_3_6_4_ef1b32
    - Operacion_cancelacion_en_moneda_extranjera_arbitraje__opefci_3_5_2_ae1628
    - Operacion_cancelacion_en_pesos__opefci_3_5_2_96a895
    - Operacion_canje_de_billete_con_falla__cirmo3_3_3_6bac12
    - Operacion_canje_de_billetes_deteriorados__cirmo3_3_2_1_439de4
    - Operacion_canje_de_billetes_en_buen_uso__cirmo3_5_2_1_1_28647f
    - Operacion_canje_de_billetes_y_monedas__cirmo3_3_1_2_b6f021
    - Operacion_canje_de_numerario_en_plataforma_electronica__cirmo3_5_2_1_cb4a33
    - Operacion_cantidad_de_lotes_registro_en_archivo__snp_cheq_7_2_6_d52e74
    - Operacion_cantidad_de_registros_individuales_archivo__snp_cheq_7_2_6_b2213c
    - Operacion_capitalizacion_aportes_irrevocables__ayccef_5_2_5_1_26b2af
    - Operacion_capitalizacion_de_intereses__depaho_3_2_4_2_859058
    - Operacion_captacion_de_depositos_en_otras_monedas__depaho_3_4_4_5_7208e2
    - Operacion_captacion_de_depositos_en_otras_monedas__depaho_3_6_2_4_652f57
    - Operacion_captacion_de_depositos_en_otras_monedas__depaho_3_8_6_4_27ec78
    - Operacion_captacion_de_imposiciones_con_fondos_del_exterior__ayccef_1_1_1_3320c3
    - Operacion_captura_de_datos_de_cheques_truncados__snp_cheq_3_2_1_7dcc7b
    - Operacion_cartera_de_negociacion__lingeef_4_2_1_5_3c2c65
    - Operacion_cartera_de_titulos_de_credito_descontados__cajasc_5_1_5_3_c95bc4
    - Operacion_caucion_bursatil_colocadora_en_pesos__opefci_5_1_be7a8a
    - Operacion_caucion_bursatil_en_bolsas_y_mercados_autorizados__opefci_5_2_2_1_93ef1d
    - Operacion_caucion_bursatil_tomadora_en_pesos__opefci_5_1_2c470a
    - Operacion_caucion_colocadora_activa_en_pesos__opefci_5_3_dc130c
    - Operacion_caucion_de_certificados_de_deposito_a_plazo_fijo__cajasc_5_1_2_59b5ed
    - Operacion_caucion_tomadora_con_otras_contrapartes__opefci_5_2_2_2_3c55b0
    - Operacion_cedip_a_compensar__snp_cheq_6_2_1_7dba10
    - Operacion_celebracion_del_acto_constitutivo__ayccef_2_9_1_82c513
    - Operacion_cerramiento_en_lineas_de_cajas__ri_mmsef_2_2_12_1_3bbac9
    - Operacion_certificados_de_depositos_a_plazo_fijo__cajasc_5_5_2_ee97ec
    - Operacion_cesion_de_derechos_y_obligaciones_del_contrato_de_custodia__manori_sbloque4_583eda
    - Operacion_cesion_de_fcem__snp_cheq_3_5_2_2_a656e0
    - Operacion_cesion_de_inmueble_al_fideicomiso_de_garantia__cajasc_5_2_5_1_e4d715
    - Operacion_cesion_irrevocable_de_indemnizacion_por_expropiacion__manori_sbloque4_6f37ec
    - Operacion_cesiones_de_creditos_sin_responsabilidad__cajasc_7_1_a3cd05
    - Operacion_chc_con_oposicion_gestion_de_cobro__cirmo3_8_9_1_019a4e
    - Operacion_chc_en_dolares__cirmo3_8_4_1_6_3a9fb3
    - Operacion_cheque_cancelatorio_en_dolares_compraventa_inmuebles__cirmo3_8_1_1_5_c1797f
    - Operacion_cheques_en_soporte_papel__snp_cheq_8_1_3_dafad5
    - Operacion_cheques_por_medios_electronicos_echeq__snp_cheq_8_1_3_ee53c3
    - Operacion_ciclo_de_pago_de_cheque_de_pago_diferido__snp_cheq_2_3_2_e064da
    - Operacion_cierre_de_cuenta__depaho_2_8_39c61b
    - Operacion_cierre_de_cuenta_comunicacion_certificada__depaho_1_13_2_1_0fa496
    - Operacion_cierre_de_cuenta_corriente_especial__depaho_3_4_11_2_9f90f0
    - Operacion_cierre_de_cuenta_corriente_especial_por_decision_del_titular__depaho_3_4_11_1_bf2d29
    - Operacion_cierre_de_cuenta_de_ahorros_para_menores__depaho_3_10_7_20fda6
    - Operacion_cierre_de_cuenta_de_seguridad_social__depaho_2_8_2_cd2511
    - Operacion_cierre_de_cuenta_entes_administradores_de_pagos__depaho_3_9_7_9d79f4
    - Operacion_cierre_de_cuenta_especial_de_regularizacion__depaho_3_16_6_fd914b
    - Operacion_cierre_de_cuenta_no_operativa__depaho_4_8_c2fff9
    - Operacion_cierre_de_cuenta_por_decision_de_la_entidad__depaho_3_8_13_2_33b582
    - Operacion_cierre_de_cuenta_por_decision_del_titular__depaho_1_13_1_0aad96
    - Operacion_cierre_de_cuenta_por_decision_del_titular__depaho_3_11_10_1_fb8bc9
    - Operacion_cierre_de_cuenta_por_decision_del_titular__depaho_3_8_13_1_2d381e
    - Operacion_cierre_de_cuenta_por_decision_del_titular_simples_asociaciones__depaho_3_5_7_056f2f
    - Operacion_cierre_de_cuenta_por_procedimiento_anses__depaho_3_5_7_33c266
    - Operacion_cierre_de_cuenta_restantes_casos__depaho_3_9_7_d8e895
    - Operacion_cierre_de_cuentas_a_la_vista__depaho_3_6_8_9cc675
    - Operacion_cierre_de_cuentas_en_forma_no_presencial__depaho_4_17_54cec5
    - Operacion_cierre_de_deposito_de_ahorro__depaho_3_2_7_90ee31
    - Operacion_cierre_de_ejercicio_irregular__ayccef_3_6_3_5f6f8e
    - Operacion_cierre_de_sucursales__expaef_11_1_835183
    - Operacion_cierre_de_sucursales__expaef_1_7_5067df
    - Operacion_circulacion_letras_de_cambio_por_camaras_electronicas__cajasc_3_2_1_45275d
    - Operacion_clasificacion_de_activos_financieros_segun_niif_9__ri_dcpc_3_1_e98a34
    - Operacion_clasificacion_de_billetes_con_maquinas_clasificadoras__cirmo3_5_1_2_1_4603d4
    - Operacion_clasificacion_de_billetes_en_buen_uso_y_deteriorados__cirmo3_5_1_1_4f465b
    - Operacion_clasificacion_de_billetes_por_cuenta_y_orden__cirmo3_5_1_2_728390
    - Operacion_clasificacion_de_deudas_comerciales__cajasc_9_13_8e1014
    - Operacion_clasificacion_de_deudor_en_categoria_1__cajasc_5_5_5_1_515b26
    - Operacion_clasificacion_de_prestatarios__cajasc_9_1_3b49c6
    - Operacion_clasificacion_destino_como_adquisicion_uso_particular_o_alquiler__manori_3_1_5_1_2469b1
    - Operacion_clasificacion_y_medicion_de_pasivos_financieros__ri_dcpc_3_2_4ee0fa
    - Operacion_clasificacion_y_presentacion_de_monedas_conmemorativas__cirmo3_7_16_6e1c85
    - Operacion_cobertura_con_garantias_preferidas_a__cajasc_5_5_2cb274
    - Operacion_cobertura_de_deficits_de_caja_en_situaciones_adversas__lingeef_3_3_11_5_8977ba
    - Operacion_cobertura_de_operacion_en_pesos__cajasc_5_5_1_1_1afdc3
    - Operacion_cobertura_de_operacion_en_pesos_con_efectivo_en_moneda_extranjera__cajasc_5_5_1__42e100
    - Operacion_cobertura_de_riesgos_en_titulizacion__lingeef_7_2_9_96d07a
    - Operacion_cobertura_de_seguro_de_danos_a_la_propiedad__manori_1_1_10_2_6b1071
    - Operacion_cobertura_de_seguro_de_danos_automotor__manori_3_1_11_6483a6
    - Operacion_cobertura_de_variacion_pgn_por_canje_con_aplicaciones_seccion_2__ri_pgn_sbloque1_f04619
    - Operacion_cobertura_de_variacion_pgn_por_canje_con_operaciones_a_termino__ri_pgn_sbloque1_2d5a20
    - Operacion_cobertura_parcial_de_asistencia_con_garantias__cajasc_5_6_72cc86
    - Operacion_cobertura_proporcional_del_saldo_por_contribucion_de_ingresos__manori_1_1_10_1_5f8a59
    - Operacion_cobertura_total_del_saldo_por_cada_solicitante__manori_1_1_10_1_ac8a55
    - Operacion_cobranza_cuotas_periodicas_capital_intereses_accesorios__manori_3_3_2_9653d0
    - Operacion_cobranza_de_chc_con_oposicion_sin_endoso_certificado__cirmo3_8_9_2_d603f4
    - Operacion_cobranza_de_chc_con_oposicion_y_endoso_certificado__cirmo3_8_9_2_fb3ceb
    - Operacion_cobranzas_y_pagos_con_cambio_justo__cirmo3_3_1_2_4068ef
    - Operacion_cobro_de_cedip__snp_cheq_3_6_5_3_856e32
    - Operacion_cobro_de_chc_por_persona_humana__cirmo3_8_1_1_8_5bb6c4
    - Operacion_cobro_de_echeq_en_ventanilla__snp_cheq_3_4_1_f7d5f8
    - Operacion_cobro_de_fcem__snp_cheq_3_5_5_1_cc1094
    - Operacion_codigo_50100_franquicia_de_integracion_rpc__ri_pgn_2_3_cbb443
    - Operacion_codigo_502dd_franquicia_de_disminucion_pgn__ri_pgn_2_3_f1d5dd
    - Operacion_codigo_503dd_franquicia_de_disminucion_exceso_pgn__ri_pgn_2_3_8deb12
    - Operacion_codigo_504dd_franquicia_de_disminucion_cargo_pgn_rpc__ri_pgn_2_3_0400c7
    - Operacion_codigo_banco_incompatible_con_moneda__snp_cheq_7_1_605db7
    - Operacion_codigo_de_barras_en_chc__cirmo3_8_1_1_3_ac355f
    - Operacion_codigo_de_transaccion_erroneo__snp_cheq_7_1_a4b081
    - Operacion_codigo_postal_erroneo__snp_cheq_7_1_94918a
    - Operacion_colocacion_de_posturas_bid_por_entidades_demandantes__cirmo3_5_2_1_3_b8e59e
    - Operacion_comparacion_de_cargos_por_defectos_coexistentes__ri_rml_1_7_1_ddc320
    - Operacion_comparacion_de_firmas_en_cheques_papel__snp_cheq_8_4_2_6_5682ae
    - Operacion_comparacion_importe_remanente_con_acreencia_neta__cajasc_9_5_2_4_532275
    - Operacion_compensacion_cheques_truncados_con_imagen__snp_cheq_3_3_2_f9f516
    - Operacion_compensacion_cheques_truncados_sin_imagen__snp_cheq_3_2_2_a82ea4
    - Operacion_compensacion_de_cedip__snp_cheq_3_6_0257cd
    - Operacion_compensacion_de_cheques_certificados__snp_cheq_2_3_3_3c1041
    - Operacion_compensacion_de_cheques_truncados_con_imagen__snp_cheq_3_3_9_1_a45c78
    - Operacion_compensacion_de_facturas_en_pesos_o_dolares__snp_cheq_3_5_7_3_fbcefc
    - Operacion_compensacion_de_fcem_al_vencimiento__snp_cheq_3_5_4_6_68a916
    - Operacion_compensacion_de_flujos_nocionales_dentro_de_banda_temporal__lingeef_5_4_4_1_ecbdae
    - Operacion_compensacion_de_movimientos_rechazados__snp_cheq_3_3_9_1_a8eae4
    - Operacion_compensacion_de_registro_electronico_e_imagen__snp_cheq_3_3_4_7ea1e2
    - Operacion_compensacion_electronica_de_cedip__snp_cheq_3_6_4_1_52a380
    - Operacion_compensacion_electronica_de_cheques__snp_cheq_2_1_8ce45e
    - Operacion_compensacion_electronica_de_cheques__snp_cheq_2_4_f1ef8a
    - Operacion_compensacion_electronica_de_cheques__snp_cheq_s2_3e8a3a
    - Operacion_compensacion_electronica_de_rechazos__snp_cheq_3_3_7_3_358668
    - Operacion_compensacion_electronica_transferencias_moneda_extranjera_48h__snp_tr_1_2_3_30a086
    - Operacion_compensacion_electronica_transferencias_pesos_24h__snp_tr_1_2_3_ed20cd
    - Operacion_compensacion_en_la_cec__snp_cheq_3_1_2_2_612641
    - Operacion_compensacion_en_la_cec__snp_cheq_3_6_4_1_3_aaef05
    - Operacion_compensacion_interbancaria_de_billetes_cib__cirmo3_5_5_e72a06
    - Operacion_compensacion_interbancaria_fcem__snp_cheq_3_5_4_3_2656fb
    - Operacion_compensacion_y_liquidacion_de_echeq__snp_cheq_3_4_2_2ce165
    - Operacion_compensacion_y_liquidacion_del_sca__snp_cheq_3_5_2_4_c0d067
    - Operacion_compensacion_y_liquidacion_en_cec_y_bcra_dia_d__snp_tr_1_2_1_dce4a1
    - Operacion_compensacion_y_liquidacion_fcem__snp_cheq_3_5_4_1_44f494
    - Operacion_compilacion_de_inventarios_de_deudores_y_acreedores__nmcief_a3_s1_f77d22
    - Operacion_complementacion_de_servicios_con_espacios_de_reunion__expaef_4_5_1_2_f105ea
    - Operacion_composicion_cuota_total_prestamo_prendario__manori_3_1_5_8_7bf735
    - Operacion_compra_al_contado_a_liquidar_con_moneda__ri_dcpc_3_4_6_5b4225
    - Operacion_compra_de_activos_de_fci__opefci_7_2_2_1_5c062f
    - Operacion_compra_de_cartera_de_creditos_de_otras_entidades__cajasc_4_8_6_1d55c8
    - Operacion_compra_de_chc_con_segundo_endoso__cirmo3_8_3_3_0fdba4
    - Operacion_compra_de_chc_por_clientes__cirmo3_8_3_1_8ec607
    - Operacion_compra_de_chc_por_persona_humana__cirmo3_8_1_1_8_d91816
    - Operacion_compra_de_facturas_de_credito_electronicas_mipyme__efemin_6_4_2_7edddd
    - Operacion_compra_de_titulos_al_contado_a_liquidar__ri_dcpc_3_4_6_b1a4ee
    - Operacion_compra_o_venta_a_termino_de_commodities__opefci_3_6_2_53c128
    - Operacion_compra_o_venta_a_termino_de_moneda_extranjera__opefci_3_5_3_457d42
    - Operacion_compra_venta_a_termino_de_commodities_en_mercados_autorizados__opefci_3_6_4_1_b2835a
    - Operacion_compra_venta_a_termino_de_commodities_fuera_de_mercados__opefci_3_6_4_1_3a3992
    - Operacion_compra_venta_a_termino_de_titulos_valores__opefci_3_4_5826d7
    - Operacion_compra_venta_a_termino_en_mercados_institucionalizados_ocde__opefci_3_6_4_2_a035f6
    - Operacion_compra_venta_a_termino_fuera_de_mercados_institucionalizados__opefci_3_6_4_2_858531
    - Operacion_compras_debidamente_documentadas__depaho_3_16_3_2_89f826
    - Operacion_compras_en_comercios_debito_ordenado__depaho_3_7_3_2_27c925
    - Operacion_compras_y_retiros_de_efectivo_con_tarjeta_de_debito__depaho_3_10_4_2_6b644e
    - Operacion_compras_y_retiros_de_efectivo_en_comercios_adheridos__depaho_3_5_4_592fc7
    - Operacion_compras_y_retiros_de_efectivo_en_comercios_adheridos_con_tarjeta_de_debito__depa_04ed6e
    - Operacion_compras_y_ventas_concertadas_con_mismo_cliente__opefci_2_3_2_2_871ca8
    - Operacion_comprension_del_negocio_de_la_caja_de_credito__ri_ccna_d2a2_3_1_cea1fb
    - Operacion_comprobacion_existencia_bienes_significativos__ri_ccna_d1a3l2_s13_6b210b
    - Operacion_computo_de_activos_inmovilizados__cajasc_10_3_1_a89d06
    - Operacion_computo_de_conceptos_por_riesgo_de_credito__cajasc_2_5_3_a722df
    - Operacion_computo_de_obligaciones_por_saldos_de_capitales__efemin_1_1_3_550fff
    - Operacion_computo_de_pases_pasivos_y_cauciones_bursatiles_por_posicion_neta__efemin_1_1_3_7ebdf8
    - Operacion_computo_de_responsabilidad_patrimonial_computable__cajasc_11_5_2_187879
    - Operacion_computo_de_saldos_de_financiaciones__cajasc_11_5_2_c31e11
    - Operacion_computo_de_saldos_promedios_de_fci_enero_2017__ri_rml_sbloque9_ba85f6
    - Operacion_computo_del_promedio_de_saldos_diarios__efemin_2_2_cb15e3
    - Operacion_computo_depreciaciones_bienes_en_defensa__ri_ccna_d1a3l2_s15_1cf09b
    - Operacion_comunicacion_a_clientes_de_delegacion_de_actividades__expaef_9_5_5_c2878e
    - Operacion_comunicacion_de_cheques_rechazados_a_entidad_girada__snp_cheq_8_4_1_9_747558
    - Operacion_comunicacion_de_estrategia_de_gestion_de_riesgo_de_mercado__lingeef_4_2_1_4_ea39fb
    - Operacion_comunicacion_externa_e_interna__lingeef_11_1_3_5bcaf6
    - Operacion_concentraciones_del_riesgo_de_mercado__lingeef_4_3_3_2_b67326
    - Operacion_concertacion_de_operaciones_con_numerario__cirmo3_5_2_1_4_26cb49
    - Operacion_concertacion_de_operaciones_de_arbitraje_exterior__opefci_3_5_2_0289db
    - Operacion_concertacion_de_operaciones_de_arbitraje_pais__opefci_3_5_2_f43bbb
    - Operacion_concertacion_de_operaciones_de_pagos_en_pantalla__cirmo3_5_2_1_10_520241
    - Operacion_concertacion_de_operaciones_declaradas__cirmo3_5_2_2_4_137d83
    - Operacion_concertacion_de_tasas_de_interes__depaho_4_4_1_a2c950
    - Operacion_concierto_de_convenios_o_contratos_de_opcion_de_refinanciacion__efemin_1_4_1_3_a0f5f9
    - Operacion_conformacion_de_solicitudes_de_autorizacion__expaef_6_4_249cb6
    - Operacion_conocimiento_del_objetivo_general_del_rtici_y_su_gestion__lingeef_5_7_3_bcf558
    - Operacion_consentimiento_del_conyuge_o_conviviente__manori_sbloque4_44ea3d
    - Operacion_conservacion_de_documentacion_de_antecesoras__ayccef_3_6_4_f6d3de
    - Operacion_consideracion_de_saldos_de_resumenes_de_cuenta__efemin_2_2_4a4dcc
    - Operacion_consideracion_explicita_de_concentraciones_en_icaap__lingeef_8_3_2_2_ddad9f
    - Operacion_consignacion_de_condiciones_operativas_en_comunicacion__expaef_4_3_4_80e4ba
    - Operacion_consignacion_de_exposiciones_al_riesgo_de_credito__ri_gerc_2_4_ef14f0
    - Operacion_consolidacion_de_entidad_con_filiales__ri_gerc_2_3_8409df
    - Operacion_consolidacion_de_entidad_sin_filiales__ri_gerc_2_3_9b5ab1
    - Operacion_consolidado_mensual_con_filiales_y_subsidiarias_significativas__ri_gerc_2_3_12b7e1
    - Operacion_consolidado_mensual_sin_consolidacion_con_otras_entidades__ri_gerc_2_3_9a5e43
    - Operacion_consolidado_trimestral_suspendido__ri_gerc_2_3_b89032
    - Operacion_constancia_de_rechazo_de_cheques_documentos__snp_cheq_8_4_1_10_aa4c51
    - Operacion_constitucion_de_depositos_e_inversiones_a_plazo_a_nombre_de_menores__efemin_1_3__4b5fb6
    - Operacion_constitucion_de_depositos_en_entidades_financieras__ayccef_2_9_4_2_71688e
    - Operacion_constitucion_de_domicilio_especial_en_caba__ayccef_2_4_1_387802
    - Operacion_constitucion_de_hipoteca_en_primer_grado__manori_1_5_1_6aef8c
    - Operacion_constitucion_de_previsiones_minimas_por_incobrabilidad__cajasc_2_7_11_a0d7f3
    - Operacion_constitucion_reserva_especial_por_superavit_revaluacion__ri_dcpc_7_1_91245e
    - Operacion_constitucion_y_liquidacion_de_garantias__snp_tr_2_2_7_35cd1e
    - Operacion_construccion_o_terminacion_vivienda_no_permanente__manori_1_1_5_1_3979a7
    - Operacion_construccion_o_terminacion_vivienda_permanente__manori_1_1_5_1_c2eb86
    - Operacion_consulta_a_base_de_cheques_cancelatorios__cirmo3_8_9_3_eefa06
    - Operacion_consulta_a_base_de_datos_de_chc__cirmo3_8_5_b127ec
    - Operacion_consulta_a_central_de_cheques_rechazados_y_central_de_deudores__ceninf_5_1_4_1868ad
    - Operacion_consulta_central_de_cuentacorrentistas_inhabilitados__cajasc_3_2_2_b9ab1b
    - Operacion_consulta_de_concordancia_de_cac_con_datos_del_sistema__snp_cheq_3_4_4_372beb
    - Operacion_consulta_de_cuentas_activas__snp_tr_2_2_10_f9edf8
    - Operacion_consulta_de_fcem_impagas_acceso_publico__ceninf_5_1_1_5747a1
    - Operacion_consulta_de_inhabilitados_por_tipo_y_numero_de_documento__ceninf_3_1_df8b44
    - Operacion_consulta_de_validez_en_sitio_bcra__cirmo3_8_4_1_9_556845
    - Operacion_consulta_por_estado_de_factura__snp_cheq_3_5_7_5_ff764e
    - Operacion_consulta_publica_de_deudores_por_cuit_cuil_cdi__ceninf_4_2_cfd900
    - Operacion_consulta_puntual_de_cheques_por_internet__ceninf_2_1_1dd728
    - Operacion_consulta_puntual_de_informacion_rechazos__ceninf_1_2_c1b98c
    - Operacion_consultas_de_saldos_y_movimientos_atm_autoservicio__expaef_4_5_1_1_f1d35c
    - Operacion_consultas_puntuales_por_deudor__ceninf_4_2_1_7b970b
    - Operacion_consultas_puntuales_por_deudor_ultimos_24_meses__ceninf_4_2_2_7e8216
    - Operacion_consultas_y_gestiones_en_sistema_de_almacenamiento__snp_cheq_8_5_2_5798e8
    - Operacion_contabilizacion_de_previsiones_requeridas__cajasc_9_12_57abc7
    - Operacion_contabilizacion_de_propiedad_planta_y_equipo_por_modelo_de_revaluacion__ri_dcpc__4d4171
    - Operacion_contenencia_de_dos_bases_de_datos__ceninf_s3_afb7b4
    - Operacion_contratacion_de_seguro_del_bien_cobertura_minima__manori_sbloque5_98bd85
    - Operacion_contrato_de_pase_activo__opefci_4_5_2_2_1b7c1e
    - Operacion_control_de_archivo__snp_cheq_sbloque10_2f020c
    - Operacion_control_de_calidad_de_prestamos_prendarios_automotores__manori_3_2_9_1_4eaf07
    - Operacion_control_de_lote__snp_cheq_sbloque10_ae0575
    - Operacion_control_de_supervivencia_de_beneficiarios__depaho_2_10_d0d5e1
    - Operacion_control_de_tareas_de_fideicomiso_de_garantia__cajasc_5_2_5_4_5d7b17
    - Operacion_control_directo_o_indirecto_de_entidad_financiera__ayccef_5_2_1_b1c2e7
    - Operacion_control_fin_de_archivo__snp_cheq_7_1_8_8fa36f
    - Operacion_control_fin_de_archivo__snp_cheq_sbloque10_02628f
    - Operacion_control_fin_de_archivo__snp_tr_1_6_2_6_eaf45a
    - Operacion_control_fin_de_archivo_identificacion_registro_tipo_9__snp_cheq_7_2_6_6a456c
    - Operacion_control_fin_de_archivo_registro_tipo_9__snp_tr_1_7_7_30aeeb
    - Operacion_control_fin_de_lote__snp_cheq_7_1_7_3fe86d
    - Operacion_control_fin_de_lote__snp_tr_1_6_2_5_b6d1db
    - Operacion_control_fin_de_lote_registro_de_cierre__snp_tr_1_7_6_c5ebec
    - Operacion_control_utilizacion_fondos_segun_destino_declarado__manori_3_3_2_9b6b16
    - Operacion_controles_electronicos_de_causales_de_rechazo__snp_cheq_3_2_6_1_bcee27
    - Operacion_controles_electronicos_sobre_informacion_recibida__snp_cheq_3_3_5_1_2045c5
    - Operacion_convenio_de_fusion__ayccef_3_3_1_24e401
    - Operacion_conversion_a_pesos_de_cargos_determinados__ri_rml_1_7_1_af0627
    - Operacion_conversion_de_caja_de_ahorros_para_menores__depaho_3_7_5_5d9f99
    - Operacion_conversion_de_cuenta_a_caja_de_ahorros_ordinaria_al_cumplir_mayoria_de_edad__dep_aad796
    - Operacion_conversion_de_cuenta_a_caja_de_ahorros_para_menores_autorizados__depaho_3_10_8_4e1255
    - Operacion_conversion_participaciones_moneda_funcional_distinta__ri_dcpc_7_1_9f6d13
    - Operacion_copia_de_documentacion_del_exterior__expaef_10_2_1_768c03
    - Operacion_cotejo_con_actas_de_asambleas_y_reuniones__ri_ccna_d1a3l2_26_1_165226
    - Operacion_cotejo_de_documentacion_y_verificacion_de_importes_significativos__ri_ccna_d1a3l_02ec56
    - Operacion_cotejo_de_resultados_con_registros_contables__ri_ccna_d1a3l2_s9_856065
    - Operacion_cotejo_de_saldos_contables_con_listados_analiticos__ri_ccna_d1a3l2_s40_8a77b7
    - Operacion_cotejo_listados_con_registros_contables__ri_ccna_d1a3l2_s19_7b4d88
    - Operacion_cotejo_listados_con_registros_contables__ri_ccna_d1a3l2_s8_96dd7b
    - Operacion_creacion_de_carpeta_crediticia__manori_3_2_5_564f4a
    - Operacion_creacion_de_carpeta_legal_post_desembolso__manori_3_2_8_aa06b5
    - Operacion_creacion_de_echeqs_y_documentos_compensables_electronicos__snp_cheq_8_4_2_8_789a2d
    - Operacion_creacion_y_emision_de_letra_hipotecaria__manori_1_2_8_3_46a226
    - Operacion_creacion_y_emision_de_letra_hipotecaria__manori_sbloque4_fd27b3
    - Operacion_creacion_y_emision_de_letras_hipotecarias_escriturales__manori_1_2_8_2_0dcd41
    - Operacion_credito_por_arrendamiento_financiero_garantia_inmueble__cajasc_5_5_12_074bef
    - Operacion_credito_por_arrendamiento_financiero_leasing__cajasc_5_2_4_294111
    - Operacion_credito_por_arrendamiento_financiero_maquinas_viales_e_industriales__cajasc_5_5__c30c60
    - Operacion_credito_prendario_sobre_automotores__manori_sbloque5_f36396
    - Operacion_creditos_a_tasa_cero_2021_decreto_512_21__efemin_7_2_4_4aaec5
    - Operacion_creditos_a_tasa_cero_decreto_332_2020__efemin_7_2_3_b8ef4f
    - Operacion_creditos_a_tasa_subsidiada_decreto_332_2020_desde_06_11_2020__efemin_7_2_3_e34e12
    - Operacion_creditos_asociados_al_cobro_de_operaciones__depaho_3_10_6_4_c95d36
    - Operacion_creditos_con_el_bcra__cajasc_7_3_1_96288f
    - Operacion_creditos_en_cuentas_especiales_repatriacion__depaho_4_21_3_099743
    - Operacion_creditos_por_arrendamientos_financieros_sobre_inmuebles__cajasc_2_5_4_9_e0c418
    - Operacion_creditos_por_cobro_de_depositos_a_plazo_fijo__depaho_3_10_6_2_887cbc
    - Operacion_creditos_por_cobro_de_depositos_e_inversiones_a_plazo__depaho_3_6_3_92157b
    - Operacion_cuantificacion_de_exposicion_bruta_y_neta__lingeef_2_4_6_1_0803f8
    - Operacion_cuantificacion_de_necesidades_de_capital_economico__lingeef_1_3_2_2_28e06f
    - Operacion_cuenta_corriente_de_corresponsalia_saldo_deudor__ri_dcpc_3_6_8_1_acb0b6
    - Operacion_cuenta_corriente_especial_para_personas_juridicas__depaho_4_20_4_a5f278
    - Operacion_cuenta_de_corresponsalia_con_limites_de_credito_y_plazos__ri_dcpc_3_6_8_1_e3c101
    - Operacion_cuentas_a_la_vista_en_cajas_de_credito_cooperativas_integracion_efectivo_minimo__3a26f5
    - Operacion_cuentas_especiales_de_garantias_para_cec__efemin_2_1_3_2380d7
    - Operacion_cuerpo_del_numero_repeticion_bcra_microletra_10__cirmo3_1_2_9_2_3a5299
    - Operacion_cumplimentacion_de_requisitos_de_vinculacion__cajasc_4_5_1e3871
    - Operacion_cumplimiento_medidas_minimas_seguridad__ri_mmsef_2_2_b37e1f
    - Operacion_cuota_de_prestamo_prendario_automotor__manori_3_1_5_7_9b8a32
    - Operacion_cupones_de_tarjetas_de_credito_emitidas_por_entidades_financieras__cajasc_5_5_4__f634eb
    - Operacion_debito_a_clientes_por_cheques__snp_cheq_2_2_2_2_623289
    - Operacion_debito_automatico_de_resumen_de_tarjeta_de_credito__depaho_1_10_5_baf7e9
    - Operacion_debito_automatico_informacion_en_resumen__depaho_3_4_10_1_c505f3
    - Operacion_debito_de_cuentas_para_transferencias_de_fondos__snp_tr_3_2_2_1_72e17a
    - Operacion_debito_en_cuentas_de_clientes__snp_cheq_3_2_6_1_726425
    - Operacion_debito_en_cuentas_de_clientes_por_monto_del_cheque__snp_cheq_3_3_5_1_bf9e4c
    - Operacion_debito_para_compra_de_moneda_extranjera_cancelacion_de_pagos__depaho_3_13_4_489b22
    - Operacion_debito_para_devolucion_de_fondos_no_utilizados_a_organismos_financiadores__depah_a0fe0f
    - Operacion_debito_por_transferencia_a_otras_cuentas__depaho_3_16_3_ff5321
    - Operacion_debito_por_ventanilla_con_documentos__depaho_3_4_6_1_5ad453
    - Operacion_debitos_automaticos_internos__depaho_1_10_5_5fd98f
    - Operacion_debitos_automaticos_para_servicios_de_cobranza__depaho_1_10_2_75457c
    - Operacion_debitos_automaticos_para_servicios_de_cobranza__depaho_3_4_8_2_eb8637
    - Operacion_debitos_en_caja_de_ahorros_cuentas_sueldo_y_cuentas_corrientes_especiales__cajas_0d325d
    - Operacion_debitos_en_cuentas_especiales_repatriacion__depaho_4_21_3_7fa5cb
    - Operacion_debitos_internos_automaticos_para_impuestos_y_servicios__depaho_3_4_6_3_c9a141
    - Operacion_debitos_internos_para_pago_de_comisiones__depaho_3_8_8_2_40751d
    - Operacion_debitos_para_constitucion_de_depositos_a_plazo_fijo_intransferibles__depaho_3_10_23ce21
    - Operacion_debitos_para_depositos_e_inversiones_a_plazo__depaho_3_6_4_a29d81
    - Operacion_debitos_para_liquidacion_en_mercado_de_cambios__depaho_3_14_4_ca6837
    - Operacion_debitos_para_operaciones_permitidas_por_cnv__depaho_3_10_6_3_ac386e
    - Operacion_debitos_y_creditos_en_cuentas_de_repatriacion__depaho_4_19_3_b6234e
    - Operacion_declaracion_de_deposito_de_billetes_deteriorados__cirmo3_5_2_2_1_4476db
    - Operacion_declaracion_de_excedente_de_billetes_en_buen_uso__cirmo3_5_5_4_1_5b427e
    - Operacion_declaracion_de_excedentes_de_billetes_en_buen_uso__cirmo3_5_5_5_2_e1d16b
    - Operacion_declaracion_de_excedentes_dentro_del_limite_global_autorizado__cirmo3_5_5_4_1_93a00f
    - Operacion_declaracion_jurada_de_inexistencia_de_vinculacion__ayccef_7_1_2_3_3cc43f
    - Operacion_declaracion_jurada_sobre_empresas_o_entidades_vinculadas__ayccef_7_1_2_3_e6851b
    - Operacion_deduccion_gastos_ejecucion_de_garantia__cajasc_9_5_2_3_263579
    - Operacion_defecto_de_aplicacion_de_recursos_en_moneda_extranjera__efemin_1_8_4a4ee4
    - Operacion_defectos_de_integracion_computo_y_registro__efemin_3_2_2_66de7d
    - Operacion_deficiencia_de_integracion_efectivo_minimo__efemin_3_1_1_962023
    - Operacion_definicion_de_horarios_de_corte_para_compensacion__snp_tr_2_2_8_09e3da
    - Operacion_definicion_de_procedimientos_ciclos_y_horarios_de_corte__snp_tr_2_3_2_2_a4a395
    - Operacion_delegacion_de_procesos_servicios_y_actividades_de_tecnologia__nmcief_a6_sbloque1_b929f8
    - Operacion_delegacion_en_agencias_complementarias__expaef_9_1_379324
    - Operacion_demas_facilidades_y_compromisos_patrimoniales__cajasc_7_6_4_c1c5c9
    - Operacion_demostracion_de_ingresos_solicitantes__manori_3_1_4_1_a82f38
    - Operacion_denominacion_de_cuenta_especial_electoral__depaho_4_18_1_1_c18986
    - Operacion_denominacion_de_fondos_comunes_de_inversion__opefci_7_1_06b655
    - Operacion_denuncia_de_extravio_sustraccion_o_destruccion_de_cheque_cancelatorio__cirmo3_8__ae5f6c
    - Operacion_deposito_a_plazo_fijo_30_dias__depaho_3_2_4_1_7ba391
    - Operacion_deposito_con_comprobante_incompleto__depaho_3_1_5_5_afd32d
    - Operacion_deposito_de_billetes_deteriorados__cirmo3_5_3_1_1a5410
    - Operacion_deposito_de_billetes_en_buen_uso__cirmo3_5_3_1_fd52d8
    - Operacion_deposito_de_bonos_del_tesoro_en_cryl__ri_rml_sbloque11_030bd3
    - Operacion_deposito_de_cheques__snp_cheq_3_4_3_3_684682
    - Operacion_deposito_de_cheques_al_portador_o_nominativos_con_endoso__depaho_1_6_1_5_5f3ec3
    - Operacion_deposito_de_cheques_atm_autoservicio__expaef_4_5_1_1_aec324
    - Operacion_deposito_de_cheques_en_echeq_usd__depaho_5_4_10a79b
    - Operacion_deposito_de_cheques_nominativos__depaho_1_6_1_5_6dfcc4
    - Operacion_deposito_de_cheques_y_documentos_compensables__depaho_1_12_7e2228
    - Operacion_deposito_de_echeq_en_ventanilla__snp_cheq_3_4_1_7bb9ef
    - Operacion_deposito_de_efectivo_atm_autoservicio__expaef_4_5_1_1_0f3f50
    - Operacion_deposito_de_garantias_de_operaciones_de_futuros_y_opciones__depaho_4_15_38fe57
    - Operacion_deposito_de_numerario_con_destino_a_caba__cirmo3_5_2_2_6_a2e0de
    - Operacion_deposito_de_numerario_con_destino_a_santiago_del_estero__cirmo3_5_2_2_6_97732e
    - Operacion_deposito_del_titulo_de_propiedad__manori_sbloque4_6c9dfa
    - Operacion_deposito_electronico_de_cedip_dia_tp__snp_cheq_3_6_4_1_6_d981c8
    - Operacion_deposito_electronico_de_cheques__snp_cheq_2_3_4_3c9a14
    - Operacion_deposito_en_caja_de_ahorros__depaho_3_2_4_1_19b132
    - Operacion_deposito_en_cajero_automatico__depaho_4_3_2_7_d00364
    - Operacion_deposito_en_efectivo__depaho_3_1_5_2_113d41
    - Operacion_deposito_en_efectivo_por_ventanilla_y_o_cajeros_automaticos__depaho_3_9_2_1_b80354
    - Operacion_deposito_en_pesos_de_venta_de_soja__depaho_3_12_3_1_521da3
    - Operacion_deposito_mediante_cheques__depaho_3_1_5_2_decb72
    - Operacion_deposito_mediante_transferencia_originada_en_cuenta__depaho_3_1_5_2_b9190d
    - Operacion_deposito_mediante_transferencias_electronicas__depaho_3_4_5_2_5eef16
    - Operacion_deposito_ordenado_por_ventanilla__depaho_3_1_5_2_6c896f
    - Operacion_deposito_por_ventanilla_con_medios_alternativos__depaho_1_6_1_355514
    - Operacion_deposito_por_ventanilla_o_cajero_automatico__depaho_3_4_5_1_fcb2e4
    - Operacion_depositos_a_la_vista_para_efectivo_minimo__efemin_7_5_2fecec
    - Operacion_depositos_a_la_vista_y_a_plazo_por_orden_de_la_justicia__efemin_1_3_7_f66f3e
    - Operacion_depositos_a_la_vista_y_plazo_en_moneda_extranjera__ri_rml_3_2_ace650
    - Operacion_depositos_a_plazo__cajasc_3_4_bcf22c
    - Operacion_depositos_a_plazo_fijo_e_inversiones_a_plazo_mediante_cedip__snp_cheq_3_6_b6ab88
    - Operacion_depositos_a_plazo_fijo_e_inversiones_a_plazo_para_integracion_de_efectivo_minimo_d96098
    - Operacion_depositos_a_plazo_fijo_en_moneda_extranjera__efemin_1_3_5_22cba2
    - Operacion_depositos_a_plazo_fijo_en_moneda_extranjera__efemin_1_4_2_1aff73
    - Operacion_depositos_a_plazo_fijo_en_pesos__efemin_1_3_5_e40360
    - Operacion_depositos_a_plazo_fijo_en_pesos__efemin_1_4_2_e49e11
    - Operacion_depositos_e_inversiones_a_plazo_de_uva_y_uvi__efemin_1_3_9_a81571
    - Operacion_depositos_en_caja_de_ahorros__depaho_3_3_e5e4b4
    - Operacion_depositos_en_caja_de_ahorros__depaho_4_20_4_c7879b
    - Operacion_depositos_en_caja_de_ahorros_en_moneda_extranjera__efemin_1_3_2_2_568bdb
    - Operacion_depositos_en_cuenta_corriente_integracion_efectivo_minimo__efemin_1_3_1_863a8e
    - Operacion_depositos_en_cuenta_especial_de_regularizacion_de_activos__efemin_7_5_345ffd
    - Operacion_depositos_en_cuentas_corrientes_de_entidades_no_bancarias__efemin_1_3_4_43f379
    - Operacion_depositos_en_cuentas_especiales_agricolas__efemin_1_3_15_1_9c6ad2
    - Operacion_depositos_en_cuentas_especiales_exportadores__efemin_1_3_15_1_f23171
    - Operacion_depositos_en_cuentas_especiales_usd__efemin_1_3_15_2_c45d21
    - Operacion_depositos_en_moneda_extranjera_en_cuenta_corriente__efemin_1_3_1_2_c22c2f
    - Operacion_depositos_en_pesos_a_la_vista_fondos_comunes_de_inversion__efemin_1_3_12_dd9528
    - Operacion_depositos_en_pesos_pspcp_fondos_de_clientes__efemin_1_3_14_e46241
    - Operacion_depuracion_del_efectivo__cirmo3_5_1_3_0346c5
    - Operacion_desarrollo_adquisicion_y_mantenimiento_de_software__nmcief_a6_sbloque12_111bd1
    - Operacion_desarrollo_de_nuevos_productos__adrei_2_1_2_2_8c29e4
    - Operacion_desarrollo_de_planes_de_contingencia_y_continuidad__lingeef_12_6_4_584464
    - Operacion_desarrollo_de_planes_de_contingencia_y_mitigacion__lingeef_11_1_6_e6cade
    - Operacion_desarrollo_de_pruebas_sobre_el_sistema_contable__ri_ccna_d2a2_3_1_4bff8e
    - Operacion_descarga_de_archivos_comprimidos_24dsfaaaamm__ceninf_4_1_2_1d98de
    - Operacion_descarga_de_base_de_inhabilitados_vigente__ceninf_3_1_fbed19
    - Operacion_descarga_de_informacion_en_archivos_comprimidos__ceninf_4_1_3_33bcb4
    - Operacion_descripcion_de_transferencias_electronicas_de_fondos__snp_tr_3_2_1_3_c82934
    - Operacion_descuento_de_cheques_de_pago_diferido__efemin_6_4_2_872970
    - Operacion_descuento_de_titulos_de_credito_con_responsabilidad__cajasc_5_1_10_1_6cc407
    - Operacion_descuento_de_titulos_de_credito_con_responsabilidad_cedente__cajasc_5_1_10_6f3101
    - Operacion_descuento_de_titulos_de_credito_con_responsabilidad_cedente__cajasc_5_1_5_11390f
    - Operacion_descuento_de_titulos_de_credito_con_responsabilidad_cedente__cajasc_5_1_5_1_bde30c
    - Operacion_desembolso_de_financiaciones_hasta_30_09_22__efemin_7_2_3ef300
    - Operacion_desembolso_de_fondos_para_integracion_de_aportes__cajasc_7_6_2_9fb51a
    - Operacion_desembolso_de_prestamo_hipotecario__manori_1_3_1_3d3876
    - Operacion_desembolso_en_efectivo_de_prestamos__cajasc_4_2_2_d77ce9
    - Operacion_desembolso_prestamo_prendario_automotor__manori_3_3_1_9afcae
    - Operacion_desinversion__adrei_2_1_2_2_0465cf
    - Operacion_desistimiento_de_pedido_de_autorizacion__cajasc_1_4_1_58ca9f
    - Operacion_desplazamiento_paralelo_hacia_abajo__lingeef_5_4_5_06914b
    - Operacion_desplazamiento_paralelo_hacia_arriba__lingeef_5_4_5_214f8a
    - Operacion_destino_del_producido_de_ejecucion_prendaria__manori_3_3_7_3_f78a87
    - Operacion_destruccion_de_billetes_no_canjeables__cirmo3_2_3_5587bd
    - Operacion_detalle_de_empresas_vinculadas_a_accionistas__ayccef_7_1_1_d77d9b
    - Operacion_detalle_de_empresas_vinculadas_a_autoridades__ayccef_7_1_1_9791c8
    - Operacion_deteccion_archivos_o_lotes_duplicados__snp_tr_1_5_1_5a088c
    - Operacion_deteccion_de_archivos_o_lotes_duplicados__snp_cheq_5_1_2_d29ad8
    - Operacion_deterioro_de_calificacion_crediticia__lingeef_3_3_4_9_2d681a
    - Operacion_determinacion_de_activos_y_pasivos_al_31_12_19_en_moneda_homogenea__ri_dcpc_7_2_908272
    - Operacion_determinacion_de_exposicion_neta_de_crc__ri_gerc_2_4_3_142cde
    - Operacion_determinacion_de_la_medida_de_riesgo_eve__lingeef_5_4_4_7df66a
    - Operacion_determinacion_de_margenes_de_cobertura_con_garantias_preferidas_a__cajasc_5_5_12bdcc
    - Operacion_determinacion_de_resultados_del_ejercicio_2019_en_moneda_de_cierre__ri_dcpc_7_2_33664a
    - Operacion_determinacion_de_tasas_de_interes__depaho_3_8_9_d91ccb
    - Operacion_determinacion_de_tasas_por_subperiodo__ri_rml_1_2_2_aa5356
    - Operacion_determinacion_del_horario_de_ruedas__cirmo3_5_2_1_8_8df07e
    - Operacion_determinacion_del_margen_de_cobertura_en_pases__opefci_4_3_5eb090
    - Operacion_determinacion_del_patrimonio_neto_al_31_12_19_por_diferencia__ri_dcpc_7_2_f98cc4
    - Operacion_determinacion_del_resultado_monetario__ri_dcpc_7_2_670c5d
    - Operacion_determinacion_del_valor_de_compra_en_escritura__manori_1_1_7_3_d4160e
    - Operacion_determinacion_exigencia_minima_depositos_y_obligaciones_a_plazo__ri_rml_1_5_722c7e
    - Operacion_determinacion_exigencia_minima_diaria_en_pesos__ri_rml_1_5_b3e980
    - Operacion_determinacion_exigencia_minima_diaria_mes_anterior__ri_rml_1_5_870c51
    - Operacion_determinacion_libre_de_tasas__depaho_3_15_4_499d07
    - Operacion_determinacion_libre_de_tasas_de_interes__depaho_1_9_1_4a66a8
    - Operacion_determinacion_resultado_acumulado_a_fecha_transicion__ri_dcpc_7_1_b3663d
    - Operacion_devengamiento_de_interes_neto_sobre_pasivo_de_beneficios_definidos__ri_dcpc_3_6__6f5c27
    - Operacion_devengamiento_tasa_interes_efectiva_pasivos__ri_dcpc_3_2_2_1_e1a672
    - Operacion_devengo_de_intereses_sobre_desembolsos__manori_sbloque4_042ef6
    - Operacion_devolucion_de_dolares_legitimos__cirmo3_4_1_2_94dc68
    - Operacion_devolucion_de_pago_con_transferencia__snp_tr_3_2_3_3_474e33
    - Operacion_devolucion_de_pago_de_sueldo__snp_tr_1_7_4_923cf1
    - Operacion_devolucion_de_transferencias_minoristas_en_pesos__snp_tr_1_7_4_28fe6a
    - Operacion_devolucion_o_rechazo__snp_tr_1_6_1_4fae3b
    - Operacion_devolucion_o_rechazo_de_transferencia__snp_tr_1_3_6_2_a5cf12
    - Operacion_devoluciones_de_transferencias__snp_tr_1_3_1_1_7b6615
    - Operacion_dia_no_laborable__snp_cheq_7_1_24ef15
    - Operacion_diferimiento_de_efectivizacion_de_transferencias_por_inconsistencia_de_seguridad_17aa18
    - Operacion_difusion_archivo_morexent_txt__ceninf_4_1_1_3_29e379
    - Operacion_difusion_de_fecha_origen_situacion_1__ceninf_4_1_3_e1b814
    - Operacion_diseno_artistico_monedas_conmemorativas_guemes__cirmo3_7_10_06fb91
    - Operacion_diseno_de_indicadores_de_alerta_temprana__lingeef_3_3_4_b9d8c7
    - Operacion_diseno_del_archivo_cheques__ceninf_1_1_1_ed0a80
    - Operacion_disminucion_de_instrumentos_de_deuda_por_canje_pen__ri_pgn_sbloque1_3d8907
    - Operacion_disminucion_de_tasas_de_corto_plazo__lingeef_5_4_5_ff5ebd
    - Operacion_disminuciones_en_el_precio_de_los_activos__lingeef_3_3_4_10_a2efd9
    - Operacion_disponibilidad_de_cheques_cancelatorios__cirmo3_8_2_4_d321d3
    - Operacion_disponibilidad_de_fondos_para_beneficiario_dia_d_1__snp_tr_1_2_1_1f039e
    - Operacion_disponibilidades_en_cuentas_corrientes_en_bcra__cajasc_2_5_4_1_ae5688
    - Operacion_disponibilizacion_de_fcem_aceptadas__snp_cheq_3_5_2_1_77edcc
    - Operacion_disponibilizacion_de_fondos_al_cliente_dia_tvto__snp_cheq_3_6_4_1_6_345152
    - Operacion_disposicion_de_fondos_por_causahabientes_tras_fallecimiento_del_titular__depaho__998fd9
    - Operacion_distribucion_de_chequeras_cancelatorias__cirmo3_8_2_1_c11941
    - Operacion_distribucion_del_capital_social__cajasc_2_9_254c56
    - Operacion_divulgacion_de_informacion_sobre_solidez_del_marco_de_gestion_de_liquidez__linge_bdc662
    - Operacion_divulgacion_de_variacion_eve__lingeef_5_7_4957ab
    - Operacion_divulgacion_de_variacion_nii__lingeef_5_7_7281a8
    - Operacion_doble_calculo_de_exposicion_al_riesgo_pais__lingeef_2_6_5_1_838807
    - Operacion_doble_vinculo__ri_mmsef_2_2_6_2e23d2
    - Operacion_documento_electronico_inexistente_rechazo_por_cec__snp_cheq_7_1_13a905
    - Operacion_ejecucion_de_garantias__lingeef_2_4_5_3_d1db36
    - Operacion_ejecucion_prendaria__manori_3_3_7_1_5542e6
    - Operacion_ejercicio_de_opciones_de_recompra_anticipada__lingeef_7_3_2_2_de1fc2
    - Operacion_elaboracion_de_estados_financieros_consolidados__ayccef_7_2_299aef
    - Operacion_elaboracion_de_informe_especial__cajasc_11_5_3_e78538
    - Operacion_elaboracion_de_informe_por_auditor__ri_ccna_d1a4_3_1_2_32765f
    - Operacion_elaboracion_de_informes_de_auditoria_interna__nmcief_a4_s3_08f623
    - Operacion_elaboracion_de_informes_de_gestion_de_riesgos__adrei_4_1_e38110
    - Operacion_elaboracion_de_informes_de_riesgos__adrei_2_1_2_1_f053f7
    - Operacion_elaboracion_de_informes_de_riesgos__adrei_2_1_8a428a
    - Operacion_eliminacion_de_registros_situacion_y_monto_en_cero__ceninf_4_1_1_2_ec4007
    - Operacion_eliminacion_del_activo_de_deudas_irrecuperables__cajasc_9_9_0f3f84
    - Operacion_eliminacion_superavit_revaluacion_acumulado__ri_dcpc_7_1_1d9c22
    - Operacion_emision_billete_1000_hornero__cirmo3_1_2_17_1_9a0470
    - Operacion_emision_billete_1000_hornero__cirmo3_1_2_17_c1cc1a
    - Operacion_emision_billete_1000_jose_de_san_martin__cirmo3_1_2_20_1_8d9b99
    - Operacion_emision_billete_1000_jose_de_san_martin__cirmo3_1_2_20_f721c7
    - Operacion_emision_billete_100_conmemorativo_evita__cirmo3_7_35_609eec
    - Operacion_emision_billete_100_papel_algodon__cirmo3_1_2_11_2_874a02
    - Operacion_emision_billete_100_taruca__cirmo3_1_2_19_1_ef6239
    - Operacion_emision_billete_100_taruca__cirmo3_1_2_19_9a1afc
    - Operacion_emision_billete_10_000_heroinas_y_heroes__cirmo3_1_2_22_0e3177
    - Operacion_emision_billete_10_000_heroinas_y_heroes__cirmo3_1_2_22_1_dcf499
    - Operacion_emision_billete_10__cirmo3_1_2_13_6e265d
    - Operacion_emision_billete_2000_familia_heroinas_y_heroes__cirmo3_1_2_21_1_412cef
    - Operacion_emision_billete_2000_heroinas_y_heroes__cirmo3_1_2_21_904272
    - Operacion_emision_billete_200_ballena_franca_austral__cirmo3_1_2_15_07ce29
    - Operacion_emision_billete_20_000_heroinas_y_heroes__cirmo3_1_2_23_1_ece296
    - Operacion_emision_billete_20_000_heroinas_y_heroes__cirmo3_1_2_23_324981
    - Operacion_emision_billete_20_guanaco__cirmo3_1_2_16_1_c43a85
    - Operacion_emision_billete_20_guanaco__cirmo3_1_2_16_45d515
    - Operacion_emision_billete_500_yaguarete__cirmo3_1_2_14_1_ecbe98
    - Operacion_emision_billete_500_yaguarete__cirmo3_1_2_14_87ab63
    - Operacion_emision_billete_50_condor_andino__cirmo3_1_2_18_1_1f233b
    - Operacion_emision_billete_50_condor_andino__cirmo3_1_2_18_2_9ca864
    - Operacion_emision_billete_50_condor_andino__cirmo3_1_2_18_816720
    - Operacion_emision_billete_50_islas_malvinas__cirmo3_1_2_12_1_5ee052
    - Operacion_emision_billete_50_islas_malvinas__cirmo3_1_2_12_aef24f
    - Operacion_emision_billete_conmemorativo_2000_salud_publica__cirmo3_7_50_6df10a
    - Operacion_emision_billetes_100_con_imagen_gral_julio_a_roca__cirmo3_1_2_10_61f2c6
    - Operacion_emision_chc_en_dolares_estadounidenses__cirmo3_8_1_1_7_965eb6
    - Operacion_emision_chc_en_pesos__cirmo3_8_1_1_7_4eeb41
    - Operacion_emision_conmemorativa_unicef_50_aniversario__cirmo3_7_5_353049
    - Operacion_emision_de_billetes_con_firmas_de_funcionarios__cirmo3_1_2_5_1563cf
    - Operacion_emision_de_billetes_con_numeracion_inicial__cirmo3_1_2_10_70d767
    - Operacion_emision_de_billetes_y_monedas_linea_monetaria_peso__cirmo3_1_1_80c20d
    - Operacion_emision_de_boleta_de_deposito_con_sello__depaho_1_6_1_6_152306
    - Operacion_emision_de_cedip__snp_cheq_3_6_2_1_3f2fd9
    - Operacion_emision_de_cedip__snp_cheq_3_6_5_1_c6c9cb
    - Operacion_emision_de_cedip__snp_cheq_3_6_7_2_6ae637
    - Operacion_emision_de_certificacion_para_cheques_echeq_rechazados__snp_cheq_sbloque4_67e586
    - Operacion_emision_de_cheques_cancelatorios_en_usd__cirmo3_8_1_1_4_8ee9c0
    - Operacion_emision_de_cheques_electronicos__snp_cheq_3_4_3_1_9d631f
    - Operacion_emision_de_cheques_en_formato_electronico__snp_cheq_2_3_6a99d0
    - Operacion_emision_de_comprobante_de_deposito__depaho_3_1_5_3_0330fb
    - Operacion_emision_de_comprobante_de_saldos_cedip__snp_cheq_3_6_6_fa81da
    - Operacion_emision_de_comprobante_de_transaccion__expaef_9_5_1_2_6fe672
    - Operacion_emision_de_comprobante_para_ejercer_acciones_legales__snp_cheq_3_5_6_1_1ba10a
    - Operacion_emision_de_comprobantes_de_deposito_en_papel__depaho_3_1_5_4_9f53c8
    - Operacion_emision_de_constancia_de_operacion__depaho_1_7_2_2560c3
    - Operacion_emision_de_constancia_deposito_cajero_automatico__depaho_1_6_2_f960e9
    - Operacion_emision_de_cupones_de_tarjeta_de_credito__cajasc_5_5_4_2_019e63
    - Operacion_emision_de_informes_sobre_estados_contables_de_cajas_de_credito__ri_ccna_d1a1_3__5282f2
    - Operacion_emision_de_monedas_conmemorativas_copa_del_mundo_2006__cirmo3_7_18_8cb79d
    - Operacion_emision_de_monedas_conmemorativas_mercosur__cirmo3_7_8_016d24
    - Operacion_emision_ix_serie_iberoamericana__cirmo3_7_39_ccd658
    - Operacion_emision_moneda_conmemorativa_1_gral_urquiza__cirmo3_7_15_5c3bee
    - Operacion_emision_moneda_conmemorativa_25_aniversario_gesta_malvinas__cirmo3_7_23_7d78e8
    - Operacion_emision_moneda_conmemorativa_2_bicentenario__cirmo3_7_44_2aed77
    - Operacion_emision_moneda_conmemorativa_40_aniversario_restauracion__cirmo3_7_51_6d4393
    - Operacion_emision_moneda_conmemorativa_50_aniversario_voto_femenino__cirmo3_7_6_b67dde
    - Operacion_emision_moneda_conmemorativa_80_aniversario_bcra__cirmo3_7_43_e637af
    - Operacion_emision_moneda_conmemorativa_belgrano__cirmo3_7_48_218f99
    - Operacion_emision_moneda_conmemorativa_bicentenario__cirmo3_7_38_d705fd
    - Operacion_emision_moneda_conmemorativa_borges_20_aniversario__cirmo3_7_22_3d65ab
    - Operacion_emision_moneda_conmemorativa_borges__cirmo3_7_9_2a82d1
    - Operacion_emision_moneda_conmemorativa_centenario_comodoro_rivadavia__cirmo3_7_13_99580d
    - Operacion_emision_moneda_conmemorativa_centenario_petroleo__cirmo3_7_24_2d6b07
    - Operacion_emision_moneda_conmemorativa_convencion_constituyente_1994__cirmo3_7_2_c84e94
    - Operacion_emision_moneda_conmemorativa_copa_mundial_fifa_2026__cirmo3_7_53_779d0f
    - Operacion_emision_moneda_conmemorativa_copa_mundial_rusia_2018__cirmo3_7_47_ff15b3
    - Operacion_emision_moneda_conmemorativa_defensa_derechos_humanos__cirmo3_7_28_03212c
    - Operacion_emision_moneda_conmemorativa_el_payador__cirmo3_7_42_8332f5
    - Operacion_emision_moneda_conmemorativa_gral_urquiza__cirmo3_7_14_afb379
    - Operacion_emision_moneda_conmemorativa_guemes_0_50__cirmo3_7_10_785a8a
    - Operacion_emision_moneda_conmemorativa_i_serie_iberoamericana__cirmo3_7_1_6c80b5
    - Operacion_emision_moneda_conmemorativa_ii_serie_iberoamericana__cirmo3_7_3_5372ac
    - Operacion_emision_moneda_conmemorativa_iii_serie_iberoamericana__cirmo3_7_7_21f39b
    - Operacion_emision_moneda_conmemorativa_iv_serie_iberoamericana__cirmo3_7_12_d96a83
    - Operacion_emision_moneda_conmemorativa_rally_dakar_2010__cirmo3_7_36_419e70
    - Operacion_emision_moneda_conmemorativa_san_martin__cirmo3_7_11_338cac
    - Operacion_emision_moneda_conmemorativa_v_serie_iberoamericana__cirmo3_7_19_da9aae
    - Operacion_emision_moneda_conmemorativa_vi_serie_iberoamericana__cirmo3_7_21_a93557
    - Operacion_emision_moneda_conmemorativa_xiii_serie_iberoamericana__cirmo3_7_52_ca3267
    - Operacion_emision_moneda_tango_fabulosos_15__cirmo3_7_41_1707e5
    - Operacion_emision_monedas_conmemorativas_1_bicentenario__cirmo3_7_31_bbb191
    - Operacion_emision_monedas_conmemorativas_70_aniversario_bcra__cirmo3_7_20_d6ab28
    - Operacion_emision_monedas_conmemorativas_75_aniversario_bcra__cirmo3_7_30_899ca1
    - Operacion_emision_monedas_conmemorativas_centenario_petroleo__cirmo3_7_29_79dc6d
    - Operacion_emision_monedas_conmemorativas_copa_mundial_catar_2022__cirmo3_7_49_51db9c
    - Operacion_emision_monedas_conmemorativas_malvinas__cirmo3_7_25_3f55b4
    - Operacion_emision_monedas_conmemorativas_mundial_sudafrica_2010__cirmo3_7_32_af0961
    - Operacion_emision_monedas_conmemorativas_plata_bicentenario__cirmo3_7_37_2039f9
    - Operacion_emision_nuevo_billete_100__cirmo3_1_2_11_abd8a4
    - Operacion_emision_pieza_oro_conmemorativa_guemes_5__cirmo3_7_10_4dbf58
    - Operacion_emision_semestral_de_resumen_de_cuenta__depaho_2_5_fa4f8c
    - Operacion_emision_x_serie_iberoamericana__cirmo3_7_45_819462
    - Operacion_empinamiento_de_la_pendiente__lingeef_5_4_5_619b8c
    - Operacion_empleo_de_papel_de_seguridad_en_chc__cirmo3_8_1_2_1_f9c57d
    - Operacion_empleo_del_sca__snp_cheq_3_5_2_5_a7df1d
    - Operacion_endoso_nominativo_del_chc__cirmo3_8_1_1_6_19344b
    - Operacion_entrega_de_certificados_para_acciones_civiles_de_echeq__snp_cheq_8_4_2_11_5ac2a7
    - Operacion_entrega_de_certificados_para_acciones_civiles_de_echeq__snp_cheq_8_4_4_9_9946da
    - Operacion_entrega_de_certificados_para_acciones_civiles_de_echeqs__snp_cheq_8_4_1_16_a13bbc
    - Operacion_entrega_de_chc_al_bcra__cirmo3_8_6_1_dd8c3c
    - Operacion_entrega_de_chc_al_bcra__cirmo3_8_6_2_2_9b5d41
    - Operacion_entrega_de_comprobante_de_transaccion__expaef_9_6_7_0353e6
    - Operacion_entrega_de_deposito_a_titular_de_orden__depaho_4_5_3_1_3e4ef5
    - Operacion_entrega_de_deposito_con_comprobante_firmado__depaho_4_5_2_b7aafb
    - Operacion_entrega_de_deposito_por_fallecimiento_del_ordenante__depaho_4_5_3_2_2b1d23
    - Operacion_entrega_de_fondos_en_cib__cirmo3_5_5_5_3_cb2517
    - Operacion_entrega_de_metalico_nuevo_por_cronograma_semanal__cirmo3_5_4_e61f05
    - Operacion_entrega_de_modelo_de_contrato_de_credito_prendario__manori_3_2_6_7d8b51
    - Operacion_entrega_de_normas_a_autoridades_judiciales__depaho_3_6_9_df0ae1
    - Operacion_entrega_de_numerario_por_bcra__cirmo3_5_4_01506e
    - Operacion_entrega_de_original_o_imagen_del_documento__snp_cheq_8_4_1_6_d9c5f6
    - Operacion_entrega_de_originales__snp_cheq_7_1_12_b63176
    - Operacion_entrega_de_originales_reclamados_en_centro_de_intercambio__snp_cheq_sbloque3_26a47e
    - Operacion_entrega_de_tarjeta_de_debito__depaho_2_4_1_230fd7
    - Operacion_entrega_de_tarjeta_de_debito_al_apoderado_o_representante_legal__depaho_3_9_4_40994b
    - Operacion_entrega_de_tarjeta_de_debito_al_menor_autorizado__depaho_3_9_4_87a526
    - Operacion_entrega_de_tarjeta_de_debito_al_titular__depaho_3_9_4_6b689d
    - Operacion_entrega_de_tarjeta_de_debito_menor_autorizado__depaho_3_7_7_32c682
    - Operacion_entrega_de_tarjeta_de_debito_titular__depaho_3_7_7_115594
    - Operacion_entrega_de_tarjetas_de_debito__depaho_3_11_7_a54545
    - Operacion_entrega_del_documento_original_en_centro_de_intercambio_fisico__snp_cheq_3_1_2_4_a15bb7
    - Operacion_envio_de_chc_pagados_al_bcra__cirmo3_8_6_2_1_4c2e94
    - Operacion_envio_de_devoluciones_de_transferencias_observadas_dia_d_1__snp_tr_1_2_1_4279cf
    - Operacion_envio_de_imagen_del_cheque_rechazado__snp_cheq_3_2_8_1_dbf8c8
    - Operacion_envio_de_imagenes_de_cheques_rechazados__snp_cheq_3_2_8_2_90cc1c
    - Operacion_envio_de_informacion_electronica_a_cec__snp_cheq_5_2_2_d2ef9d
    - Operacion_envio_de_informacion_electronica_a_cec__snp_tr_1_5_2_2_05cec1
    - Operacion_envio_de_memorandum_sobre_control_interno__ri_ccna_d1a4_s2_b8cfbd
    - Operacion_envio_de_monedas_sin_cargo__cirmo3_6_1_06ecb4
    - Operacion_envio_de_motivos_de_rechazos_a_entidades__snp_cheq_3_6_4_1_6_c2fb8f
    - Operacion_envio_de_transaccion_mep_de_solicitud_de_credito__cirmo3_8_4_3_3fbdaa
    - Operacion_envio_de_transferencias_por_cec_dia_d__snp_tr_1_2_1_80edef
    - Operacion_envio_del_reclamo_a_la_cec__snp_cheq_3_1_2_4_12047b
    - Operacion_equipo_de_procesamiento_alternativo_y_copias_de_respaldo__ri_ccna_d2a2_3_4_3_a759cd
    - Operacion_error_de_fecha_rechazo_por_cec__snp_cheq_7_1_28b6f2
    - Operacion_error_en_campo_11_cabecera_de_lote_rechazo_por_cec__snp_cheq_7_1_d9c032
    - Operacion_error_en_campo_4_registro_individual_rechazo_por_cec__snp_cheq_7_1_63ce78
    - Operacion_error_en_contador_de_registro_rechazo_por_cec__snp_cheq_7_1_55a510
    - Operacion_error_en_registro_adicional_rechazo_por_cec__snp_cheq_7_1_521f20
    - Operacion_error_formato_numero_de_cheque__snp_cheq_7_1_ef2008
    - Operacion_error_formato_numero_de_cuenta__snp_cheq_7_1_88ab78
    - Operacion_error_formato_registro_adicional__snp_cheq_7_1_55f142
    - Operacion_error_por_campo_mandatario_rechazo_por_cec__snp_cheq_7_1_ca5aeb
    - Operacion_errores_entidad_depositaria__snp_cheq_7_1_433c7c
    - Operacion_especificacion_de_factores_de_riesgo_de_mercado__lingeef_4_3_1_cc16ec
    - Operacion_establecer_acuerdos_procedimientos_y_elementos_de_seguridad__snp_cheq_8_4_4_1_f5ee29
    - Operacion_establecimiento_de_arquitectura_y_taxonomias_de_datos_integradas__adrei_2_2_2_2_44d7d0
    - Operacion_establecimiento_de_estrategias_de_mitigacion_del_riesgo_de_concentracion__lingee_59bcb7
    - Operacion_establecimiento_de_limites_de_perdida_maxima__lingeef_4_3_3_3_2d8b25
    - Operacion_establecimiento_de_limites_de_riesgo_de_mercado__lingeef_4_3_3_a35b28
    - Operacion_establecimiento_de_limites_gestion_del_riesgo_de_mercado__lingeef_4_1_2_2_9d8721
    - Operacion_estado_incorrecto_de_la_transaccion_rechazo_por_cec__snp_cheq_7_1_20cbd6
    - Operacion_estimacion_de_deterioro_de_activos_financieros__ri_dcpc_7_2_78d4c2
    - Operacion_estimar_nivel_y_tendencia_de_riesgos__lingeef_1_4_3_1_3f1707
    - Operacion_estrategias_de_cobertura__lingeef_5_3_4_761897
    - Operacion_estres_de_credito_o_liquidez_en_el_mercado__lingeef_3_5_4_0c35bd
    - Operacion_estres_de_credito_o_liquidez_en_el_mercado__lingeef_3_5_4_4_8d8967
    - Operacion_estres_de_la_contraparte__lingeef_3_5_4_46917e
    - Operacion_estres_de_la_entidad_como_cliente_de_corresponsal__lingeef_3_5_4_aef2ff
    - Operacion_estres_financiero_propio__lingeef_3_5_4_36537b
    - Operacion_estres_financiero_propio_participante_directo_mep__lingeef_3_5_4_1_b667dc
    - Operacion_estres_financiero_propio_usuario_de_corresponsalia__lingeef_3_5_4_1_6e789d
    - Operacion_estres_intradiario_de_contraparte_relevante__lingeef_3_5_4_2_fe7ee3
    - Operacion_estructuracion_de_titulizacion__lingeef_11_2_3_3_949a4f
    - Operacion_estudio_de_factibilidad_con_presupuesto_economico_y_financiero__ayccef_2_4_10_3b7155
    - Operacion_estudio_periodico_de_la_estructura_de_depositos__lingeef_3_1_2_2_bfe170
    - Operacion_evaluacion_de_adaptacion_vigilancia_gerencial__lingeef_6_2_2_5_7e7b9a
    - Operacion_evaluacion_de_adecuacion_de_capital__lingeef_1_4_2_b49f81
    - Operacion_evaluacion_de_calidad_del_equipo_de_trabajo__ri_ccna_d1a1_s8_a5f381
    - Operacion_evaluacion_de_capacidad_de_generacion_de_ingresos__lingeef_2_6_2_2_3d45ee
    - Operacion_evaluacion_de_capacidad_economica_financiera_del_solicitante__manori_1_2_5_bc9474
    - Operacion_evaluacion_de_irregularidades_en_transmision_de_datos__lingeef_2_4_5_3_8aaf9c
    - Operacion_evaluacion_de_la_calidad_de_la_informacion_financiera__lingeef_2_6_2_4_25035c
    - Operacion_evaluacion_de_la_forma_de_operacion_del_sistema_judicial_local__lingeef_2_6_2_4_2a8f5e
    - Operacion_evaluacion_de_procesos_de_control_interno__nmcief_a2_s1_f9aa5a
    - Operacion_evaluacion_de_proporcion_de_deuda_publica__lingeef_2_6_2_2_62c8ae
    - Operacion_evaluacion_de_razonabilidad_de_previsiones_y_amortizaciones__ri_ccna_d1a3l2_s7_c9185b
    - Operacion_evaluacion_de_riesgos_por_ciclo__nmcief_a2_2_1_e388c3
    - Operacion_evaluacion_de_riesgos_y_debida_diligencia_tercerizacion__lingeef_12_6_2_53f0a8
    - Operacion_evaluacion_de_solvencia_de_solicitantes__manori_1_1_4_4_0f597e
    - Operacion_evaluacion_de_solvencia_de_solicitantes__manori_3_1_4_4_81e464
    - Operacion_evaluacion_de_suficiencia_de_capital_para_rtici__lingeef_1_3_2_1_87fe61
    - Operacion_evaluacion_de_suficiencia_del_capital__lingeef_1_4_4_1_3ff820
    - Operacion_evaluacion_del_conocimiento_de_la_actividad_de_la_entidad_auditada__ri_ccna_d1a1_7ee9f1
    - Operacion_evaluacion_del_grado_de_desarrollo_humano__lingeef_2_6_2_4_d4f39d
    - Operacion_evaluacion_del_grado_de_independencia_frente_al_cliente__ri_ccna_d1a1_s8_aab08e
    - Operacion_evaluacion_del_historial_financiero_del_pais__lingeef_2_6_2_4_a4649e
    - Operacion_evaluacion_del_historial_regulatorio_del_pais__lingeef_2_6_2_4_781980
    - Operacion_evaluacion_del_riesgo_de_concentracion__lingeef_8_4_8_8d8c22
    - Operacion_evaluacion_del_riesgo_de_creditos_individuales_y_carteras__lingeef_2_3_4_da5f66
    - Operacion_evaluacion_del_tamano_y_estructura_de_deuda_externa__lingeef_2_6_2_2_078209
    - Operacion_evaluacion_marco_gobierno_tecnologia_y_seguridad__nmcief_a6_sbloque2_47c065
    - Operacion_evaluacion_nivel_riesgo_ciclos_y_sucursales__nmcief_a2_2_2_7edb82
    - Operacion_evaluacion_procesos_control_interno__nmcief_a2_s0_6f12e4
    - Operacion_evaluacion_razonabilidad_previsiones_contingencias__ri_ccna_d1a3l2_s25_9c633b
    - Operacion_evaluacion_rubros_patrimoniales_cartera_prestamos_previsiones_depreciaciones__ri_a97d2b
    - Operacion_evaluacion_y_analisis_comparativo_de_herramientas__lingeef_6_3_1_2_274478
    - Operacion_examen_de_estados_contables__ri_ccna_d1a2_s1_b0ba48
    - Operacion_examen_de_operaciones_especificas__ri_ccna_d1a4_3_3_3263da
    - Operacion_examen_de_saldos_iniciales_primera_auditoria__ri_ccna_d1a2_s6_264e40
    - Operacion_examen_de_suficiencia_de_capital__lingeef_1_4_4_aa33b0
    - Operacion_examen_detallado_de_documentacion_de_respaldo__ri_ccna_d1a3l2_29_3_0e98c9
    - Operacion_examen_periodico_del_proceso_de_gestion_de_riesgo__lingeef_1_4_4_40200f
    - Operacion_examen_previo_de_nuevos_productos_y_actividades__lingeef_5_1_2_1_ad9ba7
    - Operacion_excepciones_a_limites_de_credito__lingeef_2_2_2_7_4e584e
    - Operacion_exceso_a_la_relacion_de_punto_3_7__cajasc_6_4_1deadd
    - Operacion_exclusion_del_registro_de_auditores__ri_ccna_d1a1_5_3_839e29
    - Operacion_exhibicion_de_fcem_en_cenfiv__snp_cheq_3_5_7_1_ff1f71
    - Operacion_exigencia_efectivo_minimo_mensual_pesos_depositos_obligaciones_plazo__efemin_2_4_ca1d32
    - Operacion_exigencia_minima_diaria_periodo_01_09_a_18_09__ri_rml_sbloque14_b04530
    - Operacion_exigencia_minima_diaria_periodo_19_09_a_30_09__ri_rml_sbloque14_a431d1
    - Operacion_exigencia_minima_diaria_sobre_depositos_y_obligaciones_a_plazo_periodo_01_09_a_1_88934d
    - Operacion_exigencia_minima_diaria_sobre_depositos_y_obligaciones_a_plazo_periodo_19_09_a_3_e559c3
    - Operacion_exigencia_por_riesgo_de_credito__cajasc_2_5_1_f3d7e8
    - Operacion_expedicion_de_comprobante_cal__snp_cheq_3_5_6_2_303129
    - Operacion_expedicion_de_credencial_de_registro_laboral__depaho_3_1_7_1_692dc1
    - Operacion_exposicion_de_activos_por_impuesto_diferido__ri_dcpc_3_6_1_b51737
    - Operacion_exposicion_de_pasivos_por_impuesto_diferido__ri_dcpc_3_6_1_126c4c
    - Operacion_exposicion_de_saldo_acreedor_en_utilidades_diversas__ri_dcpc_3_6_2_26162f
    - Operacion_exposiciones_con_mismo_deudor_o_contraparte__lingeef_8_2_1_6de6a9
    - Operacion_exposiciones_crediticias_indirectas_cobertura_comun__lingeef_8_2_3_17c6ca
    - Operacion_exposiciones_en_proceso_de_titulizacion__lingeef_11_2_3_3_dffdfd
    - Operacion_exposiciones_en_region_geografica_industria_o_sector__lingeef_8_2_2_1df506
    - Operacion_exposiciones_fuera_de_balance_con_contraparte__lingeef_8_2_6_0a612e
    - Operacion_expresion_de_equivalente_en_uva_y_uvi__manori_1_1_5_2_7049ca
    - Operacion_expresion_de_saldos_en_uva__depaho_3_1_4_bd20d5
    - Operacion_extraccion_con_diferencia_entre_comprobante_e_importe__depaho_4_3_2_11_0a1984
    - Operacion_extraccion_de_efectivo_atm_autoservicio__expaef_4_5_1_1_347fc7
    - Operacion_extraccion_de_efectivo_en_cajeros_automaticos__depaho_5_2_a5d0d4
    - Operacion_extraccion_de_efectivo_por_menor_autorizado__depaho_3_7_3_1_815b16
    - Operacion_extraccion_de_fondos__depaho_3_2_5_894722
    - Operacion_extraccion_de_fondos_cajeros_automaticos__depaho_3_10_4_1_0d2377
    - Operacion_extraccion_de_fondos_en_el_pais__depaho_2_3_2_fefe8e
    - Operacion_extraccion_de_fondos_mediante_cajeros_automaticos__depaho_3_11_5_1_d327d4
    - Operacion_extraccion_de_fondos_mediante_canales_electronicos__depaho_3_10_4_3_b10e4f
    - Operacion_extraccion_de_fondos_por_ventanilla__depaho_1_7_1_d0a66c
    - Operacion_extraccion_de_fondos_por_ventanilla__depaho_2_3_2_2_6c9664
    - Operacion_extraccion_de_fondos_puntos_de_venta__depaho_3_10_4_1_0200aa
    - Operacion_extraccion_de_fondos_ventanilla__depaho_3_10_4_1_5c097e
    - Operacion_extraccion_de_imagenes_del_reservorio__snp_cheq_3_2_8_3_3ae3a8
    - Operacion_extraccion_por_transferencia_ventanilla_o_medios_electronicos__depaho_3_10_4_4_59490e
    - Operacion_extracciones_a_traves_de_cajeros_automaticos__depaho_3_4_6_4_a66089
    - Operacion_extracciones_de_efectivo_por_ventanilla__depaho_3_5_4_6ff587
    - Operacion_extracciones_de_fondos_mediante_cajeros_automaticos__depaho_3_5_4_53d215
    - Operacion_extravio_o_sustraccion_de_hoja_movil__depaho_3_1_7_3_337231
    - Operacion_extravio_sustraccion_o_destruccion_de_chc__cirmo3_8_7_efc3bd
    - Operacion_extravio_sustraccion_o_destruccion_de_chc_sin_nominar__cirmo3_8_7_1_2_93031e
    - Operacion_facturas_a_cobrar_a_consumidores_por_servicios_prestados__cajasc_2_5_4_8_a7419b
    - Operacion_facturas_a_consumidores_por_servicios_prestados__cajasc_5_5_8_878ad1
    - Operacion_falta_de_conformidad_rechazo_por_entidad_girada__snp_cheq_7_1_b0a92a
    - Operacion_falta_firma_recibo_para_deposito_rechazo_por_entidades__snp_cheq_7_1_a8a60e
    - Operacion_falta_leyenda_presentado_electronicamente_al_cobro_rechazo__snp_cheq_7_1_69d3ad
    - Operacion_fase_de_prueba_predefinida_de_nuevos_productos__lingeef_5_1_2_1_72b6a8
    - Operacion_fideicomiso_de_garantia_para_construccion_de_inmuebles__cajasc_5_2_5_6_8baa37
    - Operacion_fideicomiso_de_garantia_para_financiaciones_de_construccion__cajasc_5_2_5_9cf667
    - Operacion_fijacion_de_niveles_de_tolerancia_al_riesgo__lingeef_11_1_5_53894e
    - Operacion_fijacion_de_prima_en_pases_de_futuro__opefci_4_2_ce96e2
    - Operacion_financiacion_a_clientes_con_flujo_de_fondos_de_cobranza_de_creditos_de_consumo___ac813a
    - Operacion_financiacion_a_entidades_no_alcanzadas_y_empresas_de_leasing__efemin_6_4_3_2_acd44e
    - Operacion_financiacion_con_garantias_de_puntos_2_5_4_3_2_5_4_5_2_5_4_7_2_5_4_8_o_2_5_4_9___7f5db3
    - Operacion_financiacion_con_hipoteca_en_primer_grado__cajasc_2_5_4_4_3e3279
    - Operacion_financiacion_con_titulos_publicos_nacionales_cotizados__cajasc_2_5_4_10_95f081
    - Operacion_financiacion_cubierta_con_garantia_preferida_a_cupones_tarjeta__cajasc_2_5_4_3_52ef25
    - Operacion_financiacion_cubierta_con_garantia_preferida_a_efectivo__cajasc_2_5_4_3_9f0482
    - Operacion_financiacion_cubierta_con_garantia_preferida_a_titulos_publicos__cajasc_2_5_4_3_29b470
    - Operacion_financiacion_cubierta_con_prenda_fija_en_primer_grado__cajasc_2_5_4_5_9a903c
    - Operacion_financiacion_de_capital_de_trabajo__efemin_6_4_2_43b8c2
    - Operacion_financiacion_de_proyectos_de_inversion__efemin_6_4_1_c00f90
    - Operacion_financiacion_en_pesos__cajasc_4_2_5bfcc3
    - Operacion_financiacion_hipotecaria_vivienda_propia_margen_cobertura__cajasc_5_5_10_1_51d9be
    - Operacion_financiacion_mediante_pase_activo__ri_dcpc_3_4_4_1_1ab240
    - Operacion_financiacion_proyectos_inversion_sector_energetico__ri_rml_sbloque7_45be43
    - Operacion_financiacion_significativa__cajasc_4_6_dc11e1
    - Operacion_financiacion_sobre_inmueble_para_vivienda_propia__cajasc_5_5_10_2_2c7513
    - Operacion_financiacion_sobre_inmuebles_para_usos_distintos_de_vivienda_propia__cajasc_2_5__24f1a9
    - Operacion_financiacion_sobre_inmuebles_para_vivienda_propia_no_comprendida_en_inciso_i__ca_b29b56
    - Operacion_financiacion_sobre_inmuebles_para_vivienda_unica_familiar_y_de_ocupacion_permane_cc5379
    - Operacion_financiaciones_a_asociados__cajasc_4_2_1_1_c51ec4
    - Operacion_financiaciones_a_clientes_fuera_de_zona_de_actuacion__cajasc_4_2_1_2_8fa60a
    - Operacion_financiaciones_a_clientes_vinculados__cajasc_10_2_88c10d
    - Operacion_financiaciones_a_empresas_emisoras_de_tarjetas_ahora_12__efemin_7_4_1_ec3405
    - Operacion_financiaciones_a_mipyme_a_tasa_nominal_anual_hasta_24__efemin_7_2_2_30afdd
    - Operacion_financiaciones_a_mipyme_con_tasa_maxima__efemin_7_2_1_fbfcac
    - Operacion_financiaciones_a_mipymes_agricolas_productoras_de_cereales_oleaginosas__efemin_6_26603c
    - Operacion_financiaciones_a_plazo_36_meses__efemin_7_6_f5da2c
    - Operacion_financiaciones_a_prestadores_de_servicios_exportables__ri_rml_3_2_fb4376
    - Operacion_financiaciones_a_prestatarios__cajasc_7_1_d35284
    - Operacion_financiaciones_a_productores_de_bienes_exportables__ri_rml_3_2_8d6590
    - Operacion_financiaciones_a_productores_procesadores_o_acopiadores__ri_rml_3_2_d8a6fe
    - Operacion_financiaciones_a_proveedores_de_bienes_y_servicios_productivos__ri_rml_3_2_e3856d
    - Operacion_financiaciones_a_proveedores_de_servicios_de_exportacion__ri_rml_3_2_53d758
    - Operacion_financiaciones_bajo_modalidad_de_prestamos_para_cuentas_a_la_vista__cajasc_4_2_4_3a005e
    - Operacion_financiaciones_cartera_comercial_importacion_bienes_capital__ri_rml_sbloque7_a0b3b3
    - Operacion_financiaciones_comerciales_de_caja_de_credito_cooperativa__cajasc_8_2_2b2a56
    - Operacion_financiaciones_con_amortizacion_integra_al_vencimiento__cajasc_4_2_4_5827ae
    - Operacion_financiaciones_con_garantias_admitidas__cajasc_7_4_a22ced
    - Operacion_financiaciones_con_garantias_en_moneda_extranjera__ri_rml_3_2_7002fb
    - Operacion_financiaciones_cubiertas_con_garantias_preferidas__cajasc_9_2_2_0b4013
    - Operacion_financiaciones_cubiertas_con_garantias_sgr_fgp__cajasc_2_5_4_6_ca4965
    - Operacion_financiaciones_de_importaciones_temporarias_vinculadas_a_exportacion__ri_rml_3_2_eabf6f
    - Operacion_financiaciones_de_inversion_y_capital_de_trabajo_exportador__ri_rml_3_2_9ea805
    - Operacion_financiaciones_en_pesos_ahora_12__efemin_7_4_1_29f35a
    - Operacion_financiaciones_en_pesos_ahora_12_post_01_02_22__efemin_7_4_1_bb3192
    - Operacion_financiaciones_en_pesos_otorgadas_01_03_24_a_31_12_24__efemin_7_7_7bda17
    - Operacion_financiaciones_en_pesos_otorgadas_hasta_29_02_24__efemin_7_7_0222e9
    - Operacion_financiaciones_exportaciones_codigo_280_m__ri_rml_sbloque7_5cd556
    - Operacion_financiaciones_exportaciones_codigo_281_m__ri_rml_sbloque7_997e11
    - Operacion_financiaciones_importadores_exterior_adquisicion_bienes_servicios__ri_rml_sbloqu_341df5
    - Operacion_financiaciones_mediante_prestamos_sindicados__ri_rml_3_2_817563
    - Operacion_financiaciones_proyectos_ganaderia_bovina__ri_rml_sbloque7_f21016
    - Operacion_financiaciones_punto_6_4_1_en_pesos__efemin_6_5_2_fc7dce
    - Operacion_financiaciones_residentes_garantizadas_cartas_credito__ri_rml_sbloque7_35ab52
    - Operacion_financiaciones_totalmente_cubiertas_con_garantias_preferidas__cajasc_9_2_3_fc04ba
    - Operacion_financiamiento_al_sector_publico__cajasc_4_8_4_019812
    - Operacion_financiamiento_otro_destino_garantia_vivienda_no_permanente__manori_1_1_5_1_773f61
    - Operacion_financiamiento_otro_destino_garantia_vivienda_permanente__manori_1_1_5_1_e0108c
    - Operacion_firma_del_tenedor_o_beneficiario_en_reverso_del_chc__cirmo3_8_4_2_2972a3
    - Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_12_3_3a51d4
    - Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_14_3_1c6f96
    - Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_15_3_d06c9a
    - Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_18_3_fc5341
    - Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_19_3_5f90fe
    - Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_20_3_bbb5e3
    - Operacion_fondos_de_seguridad_con_efecto_iris__cirmo3_1_2_21_3_c9296b
    - Operacion_fondos_de_seguridad_con_efecto_iris_anverso__cirmo3_1_2_16_3_0c3792
    - Operacion_fondos_de_seguridad_con_efecto_iris_anverso__cirmo3_1_2_17_3_d03160
    - Operacion_fondos_de_seguridad_con_efecto_iris_anverso__cirmo3_1_2_22_3_9dc625
    - Operacion_fondos_de_seguridad_con_efecto_iris_y_fluorescencia__cirmo3_1_2_13_3_569a2d
    - Operacion_formulacion_de_parametros_objetivos_para_plan_de_negocios__cajasc_1_7_3_18ce6b
    - Operacion_fraccionamiento_de_cedip__snp_cheq_3_6_6d24c7
    - Operacion_funcion_de_autorizacion_para_transferencias_inmediatas__snp_tr_2_2_14_8ea2e5
    - Operacion_funcionamiento_de_cuentas_corrientes_especiales__depaho_3_4_3_294c99
    - Operacion_fusion_de_entidades_financieras__ayccef_3_1_446457
    - Operacion_garantia_o_caucion_de_titulos_valores_privados__cajasc_5_1_9_443d40
    - Operacion_garantia_por_sgr_o_fondo_publico_plazo_sin_limite__cajasc_5_1_6_95a0ab
    - Operacion_generacion_de_datos_precisos_y_fiables_sobre_riesgos__adrei_3_1_d890b9
    - Operacion_generacion_de_registro_de_control__snp_cheq_3_2_8_3_89386c
    - Operacion_generacion_prontitud_informacion_agregada_riesgos__adrei_3_3_d131f9
    - Operacion_gestion_activa_de_activos_en_garantia__lingeef_3_3_9_1_682c3a
    - Operacion_gestion_activa_de_posiciones_en_cartera_de_negociacion__lingeef_4_2_2_1_4a396c
    - Operacion_gestion_de_cedip_o_echeq__snp_cheq_3_6_5_2_e0c81a
    - Operacion_gestion_de_cumplimiento_cdi_por_entidades_financieras__opefci_7_4_2_3_01f14a
    - Operacion_gestion_de_dependencias_de_terceras_partes__lingeef_12_6_1_1b9bb6
    - Operacion_gestion_de_echeq_y_documentos_compensables__snp_cheq_8_4_1_14_fe3c4d
    - Operacion_gestion_de_eventos_de_riesgo_operacional__lingeef_6_3_1_2_98fbe9
    - Operacion_gestion_de_fcem__snp_cheq_3_5_5_1_7502a1
    - Operacion_gestion_de_presentaciones_de_numerario_apocrifo__cirmo3_4_2_8c8ec0
    - Operacion_gestion_de_riesgos_en_entidades_financieras__adrei_1_2_634522
    - Operacion_gestion_del_acceso_a_mercados_de_fondos__lingeef_3_3_7_2_f68a1d
    - Operacion_gestion_del_cobro_de_echeq_o_documento_electronico_compensable__snp_cheq_8_4_4_8_c19440
    - Operacion_gestion_del_riesgo_de_mercado__lingeef_4_1_3_1_5b69bb
    - Operacion_gestion_del_riesgo_operacional__lingeef_6_2_4_6_5722a0
    - Operacion_gestion_del_riesgo_operacional__lingeef_6_3_8b6034
    - Operacion_gestion_efectiva_del_riesgo_de_mercado__lingeef_4_2_1_4_47cb53
    - Operacion_gestion_y_custodia_de_echeqs__snp_cheq_8_10_2_f3a22f
    - Operacion_gestiones_de_organizacion_de_la_entidad__ayccef_2_9_4_1_79159e
    - Operacion_giro_de_divisas_por_importaciones__depaho_4_23_3_5d48a0
    - Operacion_grabacion_digital_de_video_circuito_cerrado__ri_mmsef_2_2_13_3_3eda42
    - Operacion_guarda_de_documentacion_de_apertura_y_deposito__depaho_3_5_9_cbe74b
    - Operacion_habilitacion_de_oficina_de_representacion__expaef_5_5_379a92
    - Operacion_hipoteca_en_primer_grado_sobre_inmuebles__cajasc_5_2_1_01cf08
    - Operacion_hipoteca_en_primer_grado_sobre_inmuebles_para_usos_distintos_de_vivienda_propia__e9070a
    - Operacion_hipoteca_primer_grado_vivienda_propia_financiaciones_restantes__cajasc_5_5_10_3_76371e
    - Operacion_identificacion_capacidades_visuales_reducidas__cirmo3_1_2_14_3_ef36a3
    - Operacion_identificacion_capacidades_visuales_reducidas__cirmo3_1_2_15_3_ebfefd
    - Operacion_identificacion_ceguera_codigo_relieve__cirmo3_1_2_22_3_6ed313
    - Operacion_identificacion_de_activos_de_informacion_criticos_e_infraestructura__lingeef_12__444c84
    - Operacion_identificacion_de_cliente_desconocido__ri_gerc_2_1_67e589
    - Operacion_identificacion_de_concentraciones_de_riesgo_incipientes__adrei_4_2_1_2_4a0ab7
    - Operacion_identificacion_de_contrapartes_individuales__ri_gerc_2_1_332cd4
    - Operacion_identificacion_de_deficiencias_en_el_sistema_contable__ri_ccna_d2a2_3_1_f98ef2
    - Operacion_identificacion_de_descalces_de_fondos_en_situaciones_de_estres__lingeef_3_3_2_a89d61
    - Operacion_identificacion_de_grandes_exposiciones_y_concentraciones_de_riesgos__lingeef_1_4_745ce0
    - Operacion_identificacion_de_grupos_de_contrapartes_conectadas__ri_gerc_2_1_b3b7eb
    - Operacion_identificacion_de_oficina_local_departamento__ri_mmsef_2_5_5_4_ab9330
    - Operacion_identificacion_de_punto_de_falla_en_transferencia__snp_tr_2_2_13_d9f751
    - Operacion_identificacion_de_registros_contables_y_transacciones_significativas__ri_ccna_d2_9bed60
    - Operacion_identificacion_de_riesgos_en_posicion_de_liquidez__lingeef_3_3_4_98f218
    - Operacion_identificacion_de_riesgos_inherentes_y_procedimientos_de_control__ri_ccna_d2a2_3_854404
    - Operacion_identificacion_de_sector_publico_municipal__ri_gerc_2_1_e3462e
    - Operacion_identificacion_de_sector_publico_nacional__ri_gerc_2_1_bd3b67
    - Operacion_identificacion_de_sector_publico_provincial_y_caba__ri_gerc_2_1_1c6f54
    - Operacion_identificacion_de_tendencias_negativas_en_riesgo_de_linea_de_producto__lingeef_3_2fdf59
    - Operacion_identificacion_de_vulnerabilidades_en_situaciones_normales__lingeef_3_3_2_bed1f0
    - Operacion_identificacion_del_inversor_nacional_o_extranjero__depaho_3_8_3_1_69148e
    - Operacion_identificacion_del_riesgo_operacional__lingeef_6_3_1_1_074a14
    - Operacion_identificacion_para_ciegos_cuadrados_en_relieve__cirmo3_1_2_9_2_e8642a
    - Operacion_identificacion_para_no_videntes__cirmo3_1_2_12_3_994eef
    - Operacion_identificacion_para_personas_con_capacidades_visuales_reducidas__cirmo3_1_2_13_3_966ed8
    - Operacion_identificacion_para_personas_con_ceguera__cirmo3_1_2_20_3_c4395f
    - Operacion_identificacion_para_personas_con_ceguera__cirmo3_1_2_21_3_7114d8
    - Operacion_identificacion_para_personas_con_discapacidades_visuales__cirmo3_1_2_18_3_edb627
    - Operacion_identificacion_para_personas_con_discapacidades_visuales__cirmo3_1_2_19_3_5092ad
    - Operacion_identificacion_para_personas_con_discapacidades_visuales_anverso__cirmo3_1_2_17__a625a5
    - Operacion_identificacion_personas_discapacidades_visuales__cirmo3_1_2_16_3_75de3c
    - Operacion_identificacion_y_agregacion_de_datos_de_riesgos_significativos__adrei_3_2_f4fb61
    - Operacion_identificacion_y_eliminacion_de_registros_por_coincidencia_de_numero_de_cheque___9e6371
    - Operacion_imagen_faltante_de_cheque__snp_cheq_7_1_00a6fd
    - Operacion_imagen_ilegible_deficiente_o_incompleta_rechazo_por_entidad_girada__snp_cheq_7_1_187fe1
    - Operacion_imagen_latente_20_50_y_100__cirmo3_1_2_9_2_70f71e
    - Operacion_imagen_latente__cirmo3_1_2_20_3_8181da
    - Operacion_imagen_latente_anverso__cirmo3_1_2_17_3_2d6957
    - Operacion_imagen_latente_con_iniciales_ra__cirmo3_1_2_18_3_81f628
    - Operacion_imagen_latente_con_iniciales_ra__cirmo3_1_2_19_3_1ca6b4
    - Operacion_imagen_latente_con_letras_ra__cirmo3_1_2_21_3_16b279
    - Operacion_imagen_latente_en_cuello_del_uniforme_militar__cirmo3_1_2_13_3_7a8cb6
    - Operacion_imagen_latente_en_motivo_del_albatros__cirmo3_1_2_12_3_892b69
    - Operacion_imagen_latente_iniciales_ra__cirmo3_1_2_14_3_0673c4
    - Operacion_imagen_latente_iniciales_ra__cirmo3_1_2_15_3_0c548c
    - Operacion_imagen_latente_iniciales_ra__cirmo3_1_2_16_3_52c17f
    - Operacion_imagen_latente_motivo_ornamental_angulo_inferior_derecho__cirmo3_1_2_22_3_f0415a
    - Operacion_imagen_latente_roseta_en_calcografia__cirmo3_1_2_4_2_9ea078
    - Operacion_imagen_no_encontrada_adeudada_como_girado__snp_cheq_7_1_a422f6
    - Operacion_imagen_no_encontrada_pendiente_de_entrega__snp_cheq_7_1_bcb377
    - Operacion_imagenes_pendientes_de_envio_y_recepcion__snp_cheq_7_1_12_0fa47c
    - Operacion_imagenes_pendientes_de_envio_y_recepcion__snp_cheq_7_1_13_5270ad
    - Operacion_implementacion_barreras_visuales_frontales__ri_mmsef_2_2_12_4_fcc03d
    - Operacion_implementacion_de_planes_de_contingencia__lingeef_4_2_2_5_13fdf5
    - Operacion_implementacion_de_procedimientos_operativos_y_sistemas_de_control__lingeef_5_1_2_deb201
    - Operacion_implementacion_sistema_informatico_acceso_remoto__depaho_3_6_7_a657db
    - Operacion_importe_no_coincide_rechazo_por_entidad_girada__snp_cheq_7_1_7e2d87
    - Operacion_imposicion_en_deposito_de_ahorro__depaho_3_2_3_237c77
    - Operacion_imposiciones_en_pesos__efemin_1_4_3_e1d35b
    - Operacion_impresion_billete_10_000_sistemas_offset_calcografico_serigrafico_tipografico__c_387633
    - Operacion_impresion_calcografica__cirmo3_1_2_20_3_cd3eec
    - Operacion_impresion_calcografica_anverso__cirmo3_1_2_17_3_ab78f0
    - Operacion_impresion_calcografica_con_relieve__cirmo3_1_2_12_3_de0271
    - Operacion_impresion_calcografica_con_relieve__cirmo3_1_2_13_3_abba20
    - Operacion_impresion_calcografica_con_relieve__cirmo3_1_2_14_3_cc7c59
    - Operacion_impresion_calcografica_con_relieve__cirmo3_1_2_15_3_27ba20
    - Operacion_impresion_calcografica_con_relieve__cirmo3_1_2_19_3_1c3b21
    - Operacion_impresion_calcografica_con_relieve_y_luminiscencia__cirmo3_1_2_18_3_888ff8
    - Operacion_impresion_calcografica_de_retratos_y_valores__cirmo3_1_2_21_3_77fc15
    - Operacion_impresion_calcografica_relieve_y_luminiscencia__cirmo3_1_2_16_3_e3da7a
    - Operacion_impresion_calcografica_retratos_y_valores__cirmo3_1_2_22_3_e3719f
    - Operacion_impresion_de_billete_de_100__cirmo3_1_2_11_3_cfe27c
    - Operacion_impresion_de_denominacion_2000_en_margen_superior__cirmo3_1_2_21_3_801d03
    - Operacion_impresion_de_digitos_2000_en_forma_vertical__cirmo3_1_2_21_3_616c6b
    - Operacion_impresion_de_serie_y_numeracion_en_chc__cirmo3_8_1_1_2_e2fdd4
    - Operacion_impresion_en_calcografia_y_offset__cirmo3_1_2_9_3_6c9adc
    - Operacion_impresion_en_tinta_invisible_valores_50_y_100__cirmo3_1_2_4_2_a09f06
    - Operacion_impresion_offset_billete_1000__cirmo3_1_2_17_3_41b472
    - Operacion_impresion_offset_billete_1000__cirmo3_1_2_20_3_862ab8
    - Operacion_impresion_offset_billete_100__cirmo3_1_2_19_3_c4fb23
    - Operacion_impresion_offset_billete_2000__cirmo3_1_2_21_3_1eae6b
    - Operacion_impresion_offset_billete_200__cirmo3_1_2_15_3_705f7e
    - Operacion_impresion_offset_billete_20__cirmo3_1_2_16_3_f14b65
    - Operacion_impresion_offset_billete_500__cirmo3_1_2_14_3_9ef3a0
    - Operacion_impresion_offset_billete_50__cirmo3_1_2_12_3_69e2e3
    - Operacion_impresion_offset_calcografica_serigrafica_y_tipografica__cirmo3_1_2_18_3_e3d511
    - Operacion_impresion_offset_del_billete_de_10__cirmo3_1_2_13_3_d1c80e
    - Operacion_impresion_roseta_en_tinta_ovi__cirmo3_1_2_4_2_718bbd
    - Operacion_impresiones_en_cheques_cancelatorios__cirmo3_8_1_2_2_fb565c
    - Operacion_imputacion_de_ajustes_niif_primera_aplicacion__ri_dcpc_3_6_7_07013f
    - Operacion_imputacion_de_flujos_a_bandas_temporales__lingeef_5_4_1_2_150d6f
    - Operacion_imputacion_de_ganancias_perdidas_actuariales_en_otros_resultados_integrales__ri__b6e1b2
    - Operacion_imputacion_de_mejoras_en_inmuebles_de_terceros__ri_dcpc_3_5_2_ca1b23
    - Operacion_imputacion_de_pasivos_en_cuentas_de_obligaciones_diversas_o_provisiones__ri_dcpc_432d21
    - Operacion_imputacion_de_resultado_de_cobertura_en_activos_a_valor_razonable_con_cambios_en_cddf31
    - Operacion_imputacion_de_resultados_por_cobertura_efectiva__ri_dcpc_3_4_3_2_592dcf
    - Operacion_imputacion_diferencia_tecnica_valoracion_pasivos__ri_dcpc_3_2_2_1_86082a
    - Operacion_imputacion_intereses_pasivos_transferencia_activos__ri_dcpc_3_2_2_1_fa286a
    - Operacion_imputacion_monetaria_en_colision_de_rechazos__snp_cheq_3_6_4_1_6_4e7b4a
    - Operacion_imputacion_resultados_baja_modificacion_pasivos__ri_dcpc_3_2_2_1_2594c0
    - Operacion_imputacion_resultados_reconocimiento_inicial_pasivos__ri_dcpc_3_2_2_1_2c18d9
    - Operacion_inclusion_de_datos_de_transferencias_en_canales_electronicos__snp_tr_3_2_2_3_2ca00b
    - Operacion_inclusion_de_deudores_en_categoria_6__cajasc_9_6_4ad69f
    - Operacion_inclusion_de_indicadores_especificos_en_el_conjunto__lingeef_3_3_4_2_39bf68
    - Operacion_inclusion_de_posiciones_de_titulizacion_en_mis__lingeef_7_2_1_7e8d53
    - Operacion_inclusion_de_promedios_mensuales_en_partida_102030_m__ri_rml_sbloque9_da6bff
    - Operacion_inclusion_en_categoria_inferior_inmediata__cajasc_8_1_4_2_1ce8c3
    - Operacion_inclusion_en_codigo_20100_diferencias_dolarizacion_depositos_judiciales__ri_pgn__3593e8
    - Operacion_inclusion_en_codigo_20100_saldos_subsistentes_desde_01_01_2018__ri_pgn_6_3_fbb9f8
    - Operacion_incorporacion_de_datos_biograficos_y_motivo_complementario__cirmo3_1_2_9_4_2b2921
    - Operacion_incorporacion_de_financiaciones_por_cesion_o_descuento__efemin_6_4_3_3_c7e4b2
    - Operacion_incorporacion_de_medidas_de_riesgo_a_procesos_de_gestion__lingeef_7_2_8_4200f8
    - Operacion_incorporacion_de_nuevos_fondos_de_seguridad__cirmo3_1_2_9_4_73fc13
    - Operacion_incorporacion_de_participaciones_en_capital__expaef_7_1_9bb108
    - Operacion_incorporacion_de_participaciones_en_capital_de_empresas__expaef_8_1_05c410
    - Operacion_incorporacion_de_servicios_financieros_adicionales__depaho_3_5_10_a8f76d
    - Operacion_incorporacion_de_titulos_de_deuda_y_certificados_de_participacion_de_fideicomiso_7cf9b4
    - Operacion_incorporacion_transitoria_bienes_defensa_creditos__ri_dcpc_3_5_3_060b3b
    - Operacion_incremento_participacion_en_entidades_financieras__ayccef_5_1_6_1586f5
    - Operacion_incrementos_en_descalces_de_monedas__lingeef_3_3_4_3_f6e7ba
    - Operacion_indicador_de_dano_reputacional__lingeef_3_3_4_8_ecb40d
    - Operacion_indicador_de_deterioro_en_calidad_de_activos__lingeef_3_3_4_7_ea85fb
    - Operacion_indicador_de_deterioro_en_condicion_financiera__lingeef_3_3_4_7_10ab76
    - Operacion_indicador_de_deterioro_en_ganancias__lingeef_3_3_4_7_771397
    - Operacion_indicador_de_disminucion_plazo_promedio_ponderado_pasivos__lingeef_3_3_4_4_f30f28
    - Operacion_individualizacion_de_operaciones_pago_con_transferencia__snp_tr_3_2_3_1_5da75d
    - Operacion_informacion_cantidad_de_cofres__ri_mmsef_2_3_7_1_3_04d203
    - Operacion_informacion_cantidad_de_cofres_tesoro_modular__ri_mmsef_2_3_7_3_3_818301
    - Operacion_informacion_de_ajustes_en_sesion_de_presentados__snp_cheq_3_3_8_1_da021f
    - Operacion_informacion_de_codigo_postal__ri_mmsef_2_5_5_7_47bfbf
    - Operacion_informacion_de_franquicias_en_codigo_de_partida__ri_pgn_2_3_6e7c92
    - Operacion_informacion_de_grupo_de_contrapartes_conectadas__ri_gerc_2_4_7a530b
    - Operacion_informacion_de_marca_tesoro_modular__ri_mmsef_2_3_7_3_1_49d52c
    - Operacion_informacion_de_provincia__ri_mmsef_2_5_5_7_1d5e87
    - Operacion_informar_al_sistema_de_almacenamiento__snp_cheq_8_4_2_9_26a5fe
    - Operacion_informar_cbu_o_alias_de_cuentas_en_fcem__snp_cheq_3_5_4_5_5fccdf
    - Operacion_informar_novedades_sobre_echeq_y_documentos_compensables__snp_cheq_8_4_2_9_40c2b1
    - Operacion_informe_de_causas_judiciales_en_tramite__ayccef_2_4_7_6_e848e2
    - Operacion_informe_de_exposicion_neta_crc__ri_gerc_2_5_1_d88404
    - Operacion_informe_posicion_global_neta_diaria__ri_pgn_2_2_1_9cc8b2
    - Operacion_infraestructura_de_pruebas_de_estres__lingeef_11_2_1_5_2ccc57
    - Operacion_ingreso_de_cargos_en_tiempo_y_forma__efemin_3_1_3_9e0a03
    - Operacion_ingreso_de_datos_de_cuenta_para_acreditacion__snp_cheq_3_6_4_2_4456b9
    - Operacion_ingreso_de_datos_en_pantalla_de_consulta__cirmo3_8_5_82f986
    - Operacion_ingreso_de_informacion_de_pago_cobro_en_sca__snp_cheq_3_5_4_2_4c13ad
    - Operacion_iniciacion_de_actividades_de_entidad_financiera__ayccef_2_8_2_a19bcf
    - Operacion_iniciacion_de_actividades_de_sucursal__expaef_1_5_1_1_6f254b
    - Operacion_iniciacion_de_actividades_de_sucursal__expaef_1_5_2_2_99f333
    - Operacion_iniciativas_de_cambio_de_tecnologia_de_la_informacion__adrei_2_1_2_2_0a117f
    - Operacion_inmovilizacion_de_remanente__depaho_3_9_7_e11a5d
    - Operacion_inscripcion_en_registro_de_asociaciones__ri_ccna_d1a1_4_1_6bf405
    - Operacion_inscripcion_en_registro_de_asociaciones_de_profesionales__ri_ccna_d1a1_5_1_a1665d
    - Operacion_inscripcion_en_registro_de_cooperativas__cajasc_1_5_2_69d3ba
    - Operacion_inscripcion_transferencia_registro_accionistas__ayccef_5_2_5_1_d59446
    - Operacion_inscripcion_y_permanencia_en_registro_de_auditores__ri_ccna_d1a1_2_2_392976
    - Operacion_insercion_de_registros_de_alta_al_padron__ceninf_1_1_2_cb5146
    - Operacion_insercion_de_registros_de_novedades_altas__ceninf_1_1_2_30a27e
    - Operacion_inspecciones_y_muestreos_periodicos_y_especificos__cirmo3_5_5_4_2_dfadfd
    - Operacion_instalacion_de_cajeros_automaticos_en_casas_operativas__expaef_4_1_1_84ad79
    - Operacion_instalacion_de_cajeros_automaticos_o_terminales_de_autoservicio__expaef_4_1_38332b
    - Operacion_instalacion_de_sucursales_en_el_exterior__expaef_1_1_2_3_631e88
    - Operacion_instalacion_mamparas_laterales_cajas_atencion__ri_mmsef_2_2_12_5_ecb0b1
    - Operacion_instalacion_pulsador_de_alarma__ri_mmsef_2_2_2_4_c4f8a7
    - Operacion_instalacion_pulsador_de_alarma__ri_mmsef_2_2_3_4_66b3f9
    - Operacion_instrumentacion_y_desembolso_de_prestamo_hipotecario__manori_1_2_8_1_e155bf
    - Operacion_instrumentos_deuda_tesoro_nacional_moneda_extranjera__ri_rml_sbloque7_bd7aeb
    - Operacion_integracion_de_bote_subcuenta_60_cryl_apartados_a_b_d__ri_rml_1_3_3e1755
    - Operacion_integracion_de_bote_subcuenta_60_cryl_pspcp__ri_rml_1_3_1e0c41
    - Operacion_integracion_de_capital_minimo_basico__ayccef_4_3_2_3_89eaaa
    - Operacion_integracion_de_capital_minimo_suscrito__ayccef_2_9_2_b3fb04
    - Operacion_integracion_de_chc_con_datos_y_firmas__cirmo3_8_3_2_aca259
    - Operacion_integracion_de_efectivo_minimo__efemin_2_1_5fd41b
    - Operacion_integracion_de_efectivo_minimo_con_leliq_para_garantias_de_compensacion__efemin__850416
    - Operacion_integracion_de_efectivo_minimo_con_titulos_publicos_nacionales__efemin_1_3_df70a8
    - Operacion_integracion_de_exigencia_con_cuenta_corriente_en_pesos_bcra__cajasc_6_2_1_1_9fdf53
    - Operacion_integracion_de_exigencia_con_cuentas_especiales_de_garantias__cajasc_6_2_1_3_e6e4e2
    - Operacion_integracion_de_exigencia_de_efectivo_minimo__efemin_1_7_e668e4
    - Operacion_integracion_de_exigencia_en_pesos_con_activos_elegibles__efemin_1_3_17_dc13e5
    - Operacion_integracion_de_exigencia_en_pesos_con_leliq_nobac_titulos__efemin_1_3_17_1_834ab9
    - Operacion_integracion_de_saldos_acreedores_en_cuentas_a_la_vista_bcra_moneda_extranjera__r_1fce85
    - Operacion_integracion_de_saldos_acreedores_en_cuentas_corrientes_bcra_pesos__ri_rml_1_3_814a53
    - Operacion_integracion_de_saldos_acreedores_en_cuentas_corrientes_entidades_no_bancarias__r_a60dfb
    - Operacion_integracion_de_saldos_acreedores_en_cuentas_especiales_beneficios_previsionales__dd77fe
    - Operacion_integracion_de_saldos_acreedores_en_cuentas_especiales_de_garantia_cec__ri_rml_1_b016e8
    - Operacion_integracion_de_saldos_cuentas_corrientes_entidades_no_bancarias_dolares_exigenci_0fc037
    - Operacion_integracion_de_saldos_cuentas_especiales_garantia_dolares_exigencias_otras_moned_5538ec
    - Operacion_integracion_de_saldos_en_dolares_estadounidenses_exigencias_otras_monedas__ri_rm_2339bd
    - Operacion_integracion_de_titulos_privados_publicos_dolares_subcuenta_60_cryl__ri_rml_1_3_a04424
    - Operacion_integracion_de_titulos_publicos_nacionales_en_pesos_subcuenta_60_cryl__ri_rml_1__efab3b
    - Operacion_integracion_de_titulos_publicos_nacionales_pesos_punto_1_3_17_subcuenta_60__ri_r_07aaa2
    - Operacion_integracion_de_titulos_valores_publicos_nacionales_instrumentos_regulacion_monet_7fc9ba
    - Operacion_integracion_diaria_de_efectivo_minimo__cajasc_6_2_2_55c9ab
    - Operacion_integracion_diaria_exigencia_minima__ri_rml_1_5_42a910
    - Operacion_integracion_efectivo_minimo_fondo_de_cese_laboral__efemin_1_3_10_ca627b
    - Operacion_integracion_en_efectivo_del_capital_minimo__ayccef_2_9_2_ecb515
    - Operacion_integracion_exigencia_pesos_con_titulos_publicos__efemin_1_3_16_03e9bb
    - Operacion_integracion_minima_diaria_depositos_y_obligaciones_a_plazo__efemin_2_4_2_45c62e
    - Operacion_integracion_minima_diaria_en_moneda_extranjera__efemin_7_1_1_4d655b
    - Operacion_intercambio_de_archivos_montos_totales_cedip_dia_tvto_2__snp_cheq_3_6_4_1_6_81c116
    - Operacion_intercambio_de_transacciones_cruzadas_entre_cec__snp_cheq_2_2_2_3_6eb346
    - Operacion_intercambio_electronico_de_archivos_cedip__snp_cheq_6_2_2_1_4469bc
    - Operacion_intercambio_electronico_de_archivos_de_cheques__snp_cheq_6_1_2_2_98d695
    - Operacion_intercambio_electronico_de_transacciones_y_mensajes__snp_cheq_6_1_1_33032c
    - Operacion_intercambio_fisico_de_cheques_rechazados__snp_cheq_2_2_2_5_c35437
    - Operacion_intercambio_fisico_de_cheques_rechazados__snp_cheq_3_2_7_2_d56608
    - Operacion_intervencion_de_profesionales__ayccef_6_4_4_acc830
    - Operacion_intervencion_del_chc_con_firma_y_sello__cirmo3_8_4_2_927033
    - Operacion_intervencion_en_regimen_de_caja_de_ahorros__depaho_1_1_1_696786
    - Operacion_inversiones_a_plazo__efemin_1_4_3_7a11fc
    - Operacion_inversiones_a_plazo_con_opcion_de_cancelacion_anticipada__efemin_1_4_1_2_1a84fe
    - Operacion_inversiones_a_plazo_con_opcion_de_cancelacion_anticipada_fondos_comunes_de_inver_b121d9
    - Operacion_inversiones_a_plazo_con_opcion_de_renovacion__efemin_1_4_1_2_ee741e
    - Operacion_inversiones_a_plazo_constante__efemin_1_4_1_2_eae214
    - Operacion_inversiones_directas_en_exterior_aportes_compras_participaciones__ri_rml_sbloque_9937b3
    - Operacion_lectura_de_actas_de_asambleas_de_asociados__ri_ccna_d1a3l2_s34_dbfcc0
    - Operacion_lectura_de_actas_de_reuniones_del_consejo_de_administracion__ri_ccna_d1a3l2_s34_d8b8a6
    - Operacion_legajo_unico_financiero_y_economico__depaho_4_24_7683d6
    - Operacion_letras_y_notas_bcra_en_dolares_estadounidenses__ri_rml_sbloque7_d99b83
    - Operacion_liquidacion_a_traves_de_cuentas_bcra_dia_tvto__snp_cheq_3_6_4_1_6_58e79f
    - Operacion_liquidacion_de_cheques_truncados__snp_cheq_3_3_9_2_7656bd
    - Operacion_liquidacion_de_intereses_por_periodos_vencidos__depaho_3_4_7_1_51291e
    - Operacion_liquidacion_de_intereses_sobre_capitales_impuestos__depaho_4_4_2_28a161
    - Operacion_liquidacion_de_operaciones_de_numerario__cirmo3_5_2_1_7_12fa8a
    - Operacion_liquidacion_de_operaciones_via_mep__cirmo3_5_2_1_9_0b222f
    - Operacion_liquidacion_de_pase_activo__opefci_4_5_2_3_53fa5a
    - Operacion_liquidacion_de_pase_activo_en_moneda_extranjera__opefci_4_5_3_4_19f37e
    - Operacion_liquidacion_de_pase_pasivo__opefci_4_4_2_3_68e55e
    - Operacion_liquidacion_de_pase_pasivo_en_moneda_extranjera__opefci_4_4_3_4_7d5674
    - Operacion_liquidacion_por_compensacion_sin_entrega__opefci_3_6_3_8a5c9f
    - Operacion_liquidacion_por_diferencia__opefci_3_4_3_9c3877
    - Operacion_liquidacion_por_diferencia__opefci_4_4_2_3_812b23
    - Operacion_liquidacion_por_diferencia_o_compensacion__opefci_3_5_4_b7f425
    - Operacion_liquidacion_por_tradicion_de_especie_y_contrapartida__opefci_3_4_3_fd0d77
    - Operacion_liquidacion_por_tradicion_efectiva__opefci_3_5_4_466611
    - Operacion_liquidacion_y_acreditacion_de_intereses__depaho_2_7_23f516
    - Operacion_lugar_o_recinto_para_operaciones_importantes__ri_mmsef_2_2_11_5962ac
    - Operacion_manifestacion_de_bienes_completa__ayccef_6_3_1_1_9da0bf
    - Operacion_mantener_cuentas_abiertas__depaho_3_1_9_6_7e5b40
    - Operacion_mantenimiento_base_datos_cuotas_prestamo__manori_3_4_2_02d17d
    - Operacion_mantenimiento_carpeta_administracion_prestamo__manori_3_3_4_5eb44c
    - Operacion_mantenimiento_de_base_de_datos_de_cuotas__manori_1_4_2_f69581
    - Operacion_mantenimiento_de_indemnizacion_como_garantia__manori_sbloque4_f0d04d
    - Operacion_mantenimiento_de_legajo_y_anexos_en_medios_magneticos__cajasc_4_3_4_edc114
    - Operacion_mantenimiento_de_legajos_de_deudores__expaef_2_2_6_3_5f0023
    - Operacion_mantenimiento_de_libros_y_registros_contables_originales__expaef_2_2_6_1_052f51
    - Operacion_mantenimiento_de_rubro_partidas_pendientes__ri_dcpc_3_6_6_c53409
    - Operacion_mapeo_de_interconexiones_e_interdependencias__lingeef_12_5_fb5937
    - Operacion_marco_de_monitoreo_y_pruebas_de_control__lingeef_6_3_1_2_0e79c3
    - Operacion_medicion_a_valor_razonable_activos_financieros__ri_dcpc_3_1_3_3_f9365d
    - Operacion_medicion_a_valor_razonable_derivados_financieros__ri_dcpc_3_4_1_c887e5
    - Operacion_medicion_a_valor_razonable_instrumentos_derivados__ri_dcpc_3_1_3_3_d29724
    - Operacion_medicion_a_valor_razonable_opciones_de_compra_lanzadas__ri_dcpc_3_4_2_3517bf
    - Operacion_medicion_a_valor_razonable_opciones_de_compra_tomadas__ri_dcpc_3_4_2_78bb91
    - Operacion_medicion_a_valor_razonable_opciones_de_venta_lanzadas__ri_dcpc_3_4_2_346604
    - Operacion_medicion_a_valor_razonable_venta_tomadas__ri_dcpc_3_4_2_3aec2e
    - Operacion_medicion_activos_financieros_a_valor_razonable_ori__ri_dcpc_3_1_3_2_4a1c1a
    - Operacion_medicion_de_activos_financieros_partidas_de_ajuste_niif__ri_dcpc_3_1_2_0a0707
    - Operacion_medicion_de_activos_y_pasivos_en_moneda_extranjera__ri_dcpc_3_3_721a75
    - Operacion_medicion_de_concentraciones_en_diversas_formas__lingeef_8_4_11_39edc5
    - Operacion_medicion_de_exposiciones_potenciales_reputacionales__lingeef_9_2_6_5a554d
    - Operacion_medicion_de_inversiones_en_subsidiarias_asociadas_y_negocios_conjuntos__ri_dcpc__60cd28
    - Operacion_medicion_de_pasivos_financieros_a_costo_amortizado__ri_dcpc_3_2_1_716276
    - Operacion_medicion_de_propiedades_de_inversion_a_valor_razonable__ri_dcpc_3_5_4_2_6cd1b9
    - Operacion_medicion_de_propiedades_de_inversion_mantenidas_para_la_venta__ri_dcpc_3_5_4_1_5b2b9b
    - Operacion_medicion_de_propiedades_de_inversion_modelo_de_costo__ri_dcpc_3_5_4_1_2d7f93
    - Operacion_medicion_del_riesgo_de_credito_de_contraparte_con_modelo_interno__lingeef_2_4_5__9fc2b7
    - Operacion_medicion_del_rtici__lingeef_5_3_4_1795c3
    - Operacion_medicion_del_rtici_mediante_sim__lingeef_5_3_3_1_9ca467
    - Operacion_medicion_exposicion_pais_base_consolidada__lingeef_2_6_5_2_d6464e
    - Operacion_medicion_exposicion_pais_base_individual__lingeef_2_6_5_2_669494
    - Operacion_medicion_inicial_de_garantias_financieras_y_compromisos_de_prestamo__ri_dcpc_3_2_1cbdc2
    - Operacion_medicion_instrumentos_financieros_derivados_a_valor_razonable__ri_dcpc_3_2_2_2_845b1a
    - Operacion_medicion_pasivos_financieros_a_valor_razonable__ri_dcpc_3_2_2_2_e4286d
    - Operacion_medicion_rtici_basada_en_resultados__lingeef_5_3_3_4cd0bd
    - Operacion_medicion_rtici_basada_en_valor_economico__lingeef_5_3_3_e01c6d
    - Operacion_medicion_var_de_posiciones__lingeef_4_3_3_5_d1ef73
    - Operacion_medicion_y_seguimiento_de_precision_de_datos__adrei_3_1_1_7_429632
    - Operacion_medicion_y_seguimiento_de_requerimientos_netos_de_fondos__lingeef_3_1_2_3_067ab4
    - Operacion_mejora_del_marco_de_gestion_del_riesgo__lingeef_5_6_ad87b1
    - Operacion_mejoras_vivienda_no_permanente__manori_1_1_5_1_659414
    - Operacion_mejoras_vivienda_permanente__manori_1_1_5_1_dedbaf
    - Operacion_metricas_de_riesgo_operacional__lingeef_6_3_1_2_9d89a5
    - Operacion_microimpresion_en_numero_10_central_del_reverso__cirmo3_1_2_13_3_09b30c
    - Operacion_microimpresion_en_reverso__cirmo3_1_2_12_3_b791a6
    - Operacion_microimpresiones__cirmo3_1_2_20_3_0f536b
    - Operacion_microimpresiones_borde_inferior_y_solapa__cirmo3_1_2_22_3_84830f
    - Operacion_microimpresiones_en_anteojos_y_saco__cirmo3_1_2_21_3_5371f5
    - Operacion_microimpresiones_mastil_bandera__cirmo3_1_2_22_3_5ba803
    - Operacion_microletra_20bcra_y_bcra__cirmo3_1_2_16_3_a7c183
    - Operacion_microletra_anverso__cirmo3_1_2_17_3_f783f6
    - Operacion_microletra_banco_central_de_la_republica_argentina__cirmo3_1_2_4_2_30c4d8
    - Operacion_microletra_base_silueta__cirmo3_1_2_14_3_1386bb
    - Operacion_microletra_bcra__cirmo3_1_2_19_3_e3e272
    - Operacion_microletra_en_base_de_silueta__cirmo3_1_2_15_3_ce370f
    - Operacion_microletra_en_base_y_valor__cirmo3_1_2_18_3_a7db66
    - Operacion_modelado_y_grabado_monedas_conmemorativas_guemes__cirmo3_7_10_175256
    - Operacion_modificacion_composicion_capital_social_incorporacion_nuevos_accionistas__ayccef_f503a3
    - Operacion_modificacion_composicion_capital_social_umbral_uif__ayccef_5_3_1_db9a56
    - Operacion_modificacion_de_diseno_billete_10__cirmo3_1_2_9_2_2c46c6
    - Operacion_modificacion_de_disenos_de_billetes__cirmo3_1_2_9_4_a75427
    - Operacion_modificacion_de_informacion_de_pago_cobro_en_sca__snp_cheq_3_5_4_2_06821d
    - Operacion_modificacion_de_instrucciones__snp_cheq_8_8_a24c24
    - Operacion_modificacion_tipografia_billetes_100_series_s_y_t__cirmo3_1_2_10_c40b1a
    - Operacion_modificaciones_composicion_capital_social__ayccef_5_3_2_96cc47
    - Operacion_modificaciones_significativas_composicion_accionaria__ayccef_5_5_cf1d68
    - Operacion_moneda_de_oro_proof_5__cirmo3_7_29_542857
    - Operacion_moneda_de_plata_proof_1__cirmo3_7_29_bbffec
    - Operacion_moneda_invalida_en_campo_10__snp_cheq_7_1_98f614
    - Operacion_monitoreo_de_disponibilidad_de_fondos_de_garantia__snp_tr_2_3_3_3_253973
    - Operacion_monitoreo_remoto_de_sistemas__ri_mmsef_2_5_952bbc
    - Operacion_motivo_complementacion_frente_dorso__cirmo3_1_2_14_3_613288
    - Operacion_motivo_complementacion_frente_dorso__cirmo3_1_2_15_3_fdf782
    - Operacion_motivo_complementacion_frente_dorso_anverso__cirmo3_1_2_17_3_adc769
    - Operacion_motivo_complementacion_frente_dorso_huella_guanaco__cirmo3_1_2_16_3_953b67
    - Operacion_motivo_complementacion_frente_dorso_transparencia__cirmo3_1_2_22_3_e134d4
    - Operacion_motivo_complementario_en_calcografia__cirmo3_1_2_9_2_548bca
    - Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_12_3_bb0258
    - Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_18_3_5670ff
    - Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_19_3_739142
    - Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_20_3_4b35d9
    - Operacion_motivo_de_complementacion_frente_dorso__cirmo3_1_2_21_3_f48c2c
    - Operacion_motivo_de_complementacion_frente_dorso_sol_de_mayo__cirmo3_1_2_13_3_f0ae16
    - Operacion_motivo_identificacion_ciegos_circulos_y_baston__cirmo3_1_2_4_2_14420d
    - Operacion_motivo_recto_verso_en_offset__cirmo3_1_2_4_2_fb36f4
    - Operacion_movimientos_de_fondos_en_cuenta_sueldo_con_cotitular__depaho_2_2_1_ae4e82
    - Operacion_movimientos_en_cuenta_gratuita_universal__depaho_3_11_5_757cfd
    - Operacion_movimientos_en_cuentas_sueldo_seguridad_social__depaho_2_3_be8ec3
    - Operacion_multiples_transferencias_para_varios_beneficiarios__depaho_3_6_4_8ecd69
    - Operacion_negociacion_de_acciones_sin_proporcionalidad_accionaria__ayccef_5_2_1_a6ef89
    - Operacion_negociacion_de_opciones_sobre_commodities__opefci_6_3_4c0f98
    - Operacion_no_corresponde_segunda_presentacion_rechazo_por_entidad_girada__snp_cheq_7_1_ac4617
    - Operacion_no_emision_de_comprobante_por_cajero__depaho_4_3_2_9_6a31ae
    - Operacion_nuevas_financiaciones_con_desembolsos_de_fondos__cajasc_9_7_258834
    - Operacion_nuevo_remate_sin_base_adjudicacion_al_mejor_postor__manori_sbloque4_9be848
    - Operacion_numeracion_en_negro_con_digitos_variables__cirmo3_1_2_12_3_dc9ad6
    - Operacion_numeracion_horizontal__cirmo3_1_2_20_3_282995
    - Operacion_numeracion_horizontal_angulo_superior_derecho__cirmo3_1_2_14_3_d65fdf
    - Operacion_numeracion_horizontal_en_angulo_superior_derecho__cirmo3_1_2_13_3_512952
    - Operacion_numeracion_horizontal_en_reverso__cirmo3_1_2_18_3_90b13b
    - Operacion_numeracion_horizontal_en_reverso__cirmo3_1_2_19_3_7aea0a
    - Operacion_numeracion_horizontal_en_reverso__cirmo3_1_2_21_3_c8da52
    - Operacion_numeracion_horizontal_reverso__cirmo3_1_2_15_3_335ce5
    - Operacion_numeracion_horizontal_reverso__cirmo3_1_2_16_3_9261a3
    - Operacion_numeracion_horizontal_reverso__cirmo3_1_2_17_3_9f8fdb
    - Operacion_numeracion_horizontal_reverso_negro__cirmo3_1_2_22_3_add845
    - Operacion_numeracion_vertical__cirmo3_1_2_20_3_7a26c0
    - Operacion_numeracion_vertical_en_margen_izquierdo__cirmo3_1_2_13_3_f3ab57
    - Operacion_numeracion_vertical_en_reverso__cirmo3_1_2_18_3_1d5284
    - Operacion_numeracion_vertical_en_reverso__cirmo3_1_2_19_3_39a6d7
    - Operacion_numeracion_vertical_en_reverso__cirmo3_1_2_21_3_070788
    - Operacion_numeracion_vertical_margen_izquierdo_y_derecho__cirmo3_1_2_9_2_52731f
    - Operacion_numeracion_vertical_reverso__cirmo3_1_2_15_3_659add
    - Operacion_numeracion_vertical_reverso__cirmo3_1_2_16_3_e60396
    - Operacion_numeracion_vertical_reverso__cirmo3_1_2_17_3_14cbbe
    - Operacion_numeracion_vertical_reverso_rojo__cirmo3_1_2_22_3_c50b48
    - Operacion_numeracion_vertical_roja__cirmo3_1_2_12_3_065ee9
    - Operacion_numeracion_vertical_rojo__cirmo3_1_2_14_3_32b743
    - Operacion_numero_angulo_superior_izquierdo_tinta_opticamente_variable__cirmo3_1_2_9_2_9aa630
    - Operacion_obligaciones_con_bancos_y_corresponsales_del_exterior__efemin_1_4_3_dbb1a3
    - Operacion_obligaciones_de_pago_en_cuotas_de_capital__efemin_1_4_3_d5ae62
    - Operacion_obtencion_confirmaciones_directas_acreedores__ri_ccna_d1a3l2_s19_facc89
    - Operacion_obtencion_confirmaciones_directas_deudores__ri_ccna_d1a3l2_s8_279490
    - Operacion_obtencion_de_autorizacion_para_funcionar_como_cooperativa__cajasc_1_5_2_c0edbc
    - Operacion_obtencion_de_cobertura_por_desempleo__manori_1_1_10_3_672763
    - Operacion_obtencion_de_confirmaciones_directas_de_entidades_financieras__ri_ccna_d1a3l2_s2_e9cfa8
    - Operacion_obtencion_de_confirmaciones_directas_de_terceros_depositarios__ri_ccna_d1a3l2_s5_d45727
    - Operacion_obtencion_de_conjunto_de_flujos_netos_por_banda_temporal__lingeef_5_4_4_1_6dbac9
    - Operacion_obtencion_de_copia_de_dorso_de_documento_de_identidad__depaho_4_2_798dad
    - Operacion_obtencion_de_declaracion_escrita_de_opcion_de_recepcion_de_informacion_de_cuota__0afd7b
    - Operacion_obtencion_de_elementos_de_juicio_por_auditor_externo__ri_ccna_d1a2_s2_0bbd16
    - Operacion_obtencion_de_financiaciones_elegibles_para_aplicacion_de_divisas__depaho_3_13_1__78e0b3
    - Operacion_obtencion_de_financiaciones_elegibles_para_aplicacion_de_divisas_de_cobros_de_ex_f5eb11
    - Operacion_obtencion_de_imagenes_del_reservorio_por_la_cec__snp_cheq_3_2_8_25ab26
    - Operacion_obtencion_de_irpc_desde_tabla_de_normas_de_seguro_de_garantia__ri_rml_sbloque4_9c5df3
    - Operacion_obtencion_de_lineas_financieras_del_exterior__efemin_1_3_6_95598f
    - Operacion_obtencion_electronica_de_constancia_de_cuil__depaho_4_2_b35dee
    - Operacion_obtencion_electronica_de_constancia_de_cuit_o_cdi__depaho_4_2_bd2e00
    - Operacion_oferta_de_excedentes_mediante_posturas_offer__cirmo3_5_2_1_3_3f7740
    - Operacion_ofrecimiento_de_herramientas_de_mitigacion_de_fraude__snp_tr_2_3_2_8_20e9fd
    - Operacion_operacion_de_sucursal_movil__expaef_1_5_1_3_a35223
    - Operacion_operacion_del_sca__snp_cheq_3_5_2_3_198751
    - Operacion_operacion_rueda_num_d_miercoles__cirmo3_5_2_2_3_258f7a
    - Operacion_operaciones_a_termino_de_moneda_extranjera__ri_dcpc_3_3_b72d09
    - Operacion_operaciones_a_termino_vinculadas_con_operaciones_al_contado__opefci_3_7_207345
    - Operacion_operaciones_a_traves_de_terminales_en_puntos_de_venta__depaho_3_4_6_4_1c62cf
    - Operacion_operaciones_activas_pasivas_y_de_servicios__ayccef_1_1_3_031df8
    - Operacion_operaciones_activas_pasivas_y_de_servicios_bancos_comerciales_de_primer_grado__a_4d00b0
    - Operacion_operaciones_al_contado_a_liquidar__opefci_2_1_6c920a
    - Operacion_operaciones_con_cajeros_automaticos__depaho_2_4_2_21cd49
    - Operacion_operaciones_con_moneda_extranjera_y_o_metales_preciosos__cajasc_11_4_1_9c4b7f
    - Operacion_operaciones_con_tasas_o_importes_de_intereses__depaho_4_4_5_2ec91f
    - Operacion_operaciones_de_cajas_de_credito_cooperativas__ayccef_1_1_2_dafc70
    - Operacion_operaciones_de_financiacion_con_titulos_valores_sft__lingeef_2_5_2_e2d221
    - Operacion_operaciones_de_pase__cajasc_3_6_1_d848b6
    - Operacion_operaciones_de_pase_financiaciones_con_garantia__ri_dcpc_3_4_4_00f95a
    - Operacion_operaciones_en_cajeros_automaticos_no_operados_por_ef__depaho_4_14_b1a06c
    - Operacion_operaciones_en_cajeros_y_terminales_de_autoservicio__depaho_3_5_4_f7bff9
    - Operacion_operaciones_en_moneda_extranjera_o_titulos_valores__efemin_1_4_3_2ed8fc
    - Operacion_operaciones_entre_entidades_financieras__opefci_2_3_2_1_f8ed0e
    - Operacion_operaciones_por_ventanilla__depaho_4_11_c91a48
    - Operacion_operaciones_punto_3_8_7__depaho_3_4_2_07bf22
    - Operacion_operaciones_punto_3_8_8__depaho_3_4_2_404cf3
    - Operacion_operaciones_punto_6_4_2_en_pesos__efemin_6_5_2_5dbdd3
    - Operacion_operatoria_de_echeq__snp_cheq_3_5_5_2_590fac
    - Operacion_operatoria_de_fcem__snp_cheq_3_5_5_2_409401
    - Operacion_opinion_favorable_supervisores_casa_matriz_sucursal_exterior__ayccef_2_4_11_4_af57f2
    - Operacion_ordenamiento_de_transferencias_inmediatas__snp_tr_2_2_3_543d2e
    - Operacion_ordenes_de_transferencia__snp_tr_1_3_1_1_779589
    - Operacion_otorgamiento_de_avales_fianzas_y_otras_garantias__cajasc_4_8_3_2_a66284
    - Operacion_otorgamiento_de_fianzas__expaef_6_5_1_f52864
    - Operacion_otorgamiento_de_financiaciones__cajasc_4_3_3_648e10
    - Operacion_otorgamiento_de_financiaciones_a_clientes_mipyme__efemin_6_3_044a85
    - Operacion_otorgamiento_de_financiaciones_con_garantia_de_cartera_de_creditos_de_consumo__c_632140
    - Operacion_otorgamiento_de_financiaciones_en_pesos__efemin_7_4_2_27e9ca
    - Operacion_otorgamiento_de_financiaciones_mipyme__efemin_7_3_7ac40e
    - Operacion_otorgamiento_de_garantias_por_intermediacion_en_operaciones_entre_terceros__caja_0f1410
    - Operacion_otorgamiento_de_garantias_por_sgr_o_fondos_publicos__cajasc_5_2_3_f1cb98
    - Operacion_otorgamiento_de_liquidez_a_fci__opefci_7_2_2_1_20e1c3
    - Operacion_otorgamiento_de_nuevas_refinanciaciones__cajasc_8_1_145a6e
    - Operacion_otorgamiento_de_otros_prestamos__cajasc_4_2_2_3_bd2a9e
    - Operacion_otorgamiento_de_prestamo_hipotecario__manori_sbloque2_624768
    - Operacion_otorgamiento_de_prestamos_comerciales__cajasc_4_2_2_3_ac8a08
    - Operacion_otorgamiento_de_prestamos_hipotecarios__cajasc_4_2_2_3_dc0924
    - Operacion_otorgamiento_de_prestamos_hipotecarios_en_pesos__manori_1_1_5_2_570cf4
    - Operacion_otorgamiento_de_prestamos_hipotecarios_mediante_metodos_especificos_de_evaluacio_070d85
    - Operacion_otorgamiento_de_prestamos_hipotecarios_sistema_aleman__manori_1_1_5_4_3dc243
    - Operacion_otorgamiento_de_prestamos_hipotecarios_sistema_frances__manori_1_1_5_4_73855c
    - Operacion_otorgamiento_de_prestamos_por_metodos_especificos_de_evaluacion__manori_1_1_4_5_79f1ef
    - Operacion_otorgamiento_prestamo_hipotecario_con_screening_scoring__manori_1_5_1_998e43
    - Operacion_otorgamiento_prestamo_prendario_automotor__manori_3_1_5_3_aeeb62
    - Operacion_otorgar_asistencia_crediticia_con_cdp_en_garantia__cajasc_4_8_1_0f507d
    - Operacion_otorgar_asistencia_en_condiciones_favorables__cajasc_4_8_2_17759b
    - Operacion_otras_financiaciones_a_exportadores__ri_rml_3_2_d444f8
    - Operacion_otros_activos__cajasc_2_5_4_10_661e89
    - Operacion_otros_creditos_otorgamiento_de_prestamos__depaho_3_4_5_3_c40b30
    - Operacion_otros_creditos_recaudacion_de_cobranzas__depaho_3_4_5_3_984f2b
    - Operacion_otros_documentos_compensables__snp_cheq_8_1_3_52f052
    - Operacion_pago_circulacion_y_gestion_de_fcem_en_sca__snp_cheq_3_5_1_5bfa1c
    - Operacion_pago_de_cedip__snp_cheq_3_6_2_1_420805
    - Operacion_pago_de_cheques_documentos_no_rechazados__snp_cheq_8_4_2_2_8a47d2
    - Operacion_pago_de_fcem__snp_cheq_3_5_2_2_c0d950
    - Operacion_pago_de_gastos_y_honorarios_ejecucion_hipotecaria__manori_1_3_6_2_4ecb2e
    - Operacion_pago_de_haberes_y_prestaciones_del_sipa__depaho_2_1_de53b7
    - Operacion_pago_de_importes_adeudados_ejecucion_hipotecaria__manori_1_3_6_2_487ab3
    - Operacion_pago_de_impuestos_servicios_y_otros_conceptos__depaho_3_5_4_946aa7
    - Operacion_pago_de_impuestos_y_servicios_por_canales_electronicos__depaho_2_3_2_4_ac4b4c
    - Operacion_pago_de_intereses_sobre_saldos__depaho_3_6_6_017fb1
    - Operacion_pago_de_prestamos__depaho_1_10_1_216e28
    - Operacion_pago_de_prestamos__depaho_3_4_8_1_b49304
    - Operacion_pago_de_remuneraciones_de_jurisdicciones_provinciales__depaho_2_1_39418c
    - Operacion_pago_de_retornos_y_distribuciones_de_utilidades__ri_ccna_d1a3l2_26_3_a2db5f
    - Operacion_pago_de_servicios_atm_autoservicio__expaef_4_5_1_1_b48bd4
    - Operacion_pago_en_moneda_extranjera_mediante_medios_electronicos__depaho_3_6_4_2fc9df
    - Operacion_pago_preferentemente_electronico_de_importes_menores__depaho_3_6_4_0b380b
    - Operacion_pago_saldo_de_precio__ayccef_5_2_5_1_8d0e1e
    - Operacion_parametrizacion_de_equipos_clasificadores__cirmo3_5_1_2_2_bc8b8b
    - Operacion_participacion_como_participante_directo_y_uso_de_corresponsal__lingeef_3_5_2_44973a
    - Operacion_participacion_en_capital_de_entidad_del_exterior__expaef_6_5_1_090d8d
    - Operacion_participacion_en_capital_de_entidad_financiera_del_exterior__expaef_6_1_2c60e5
    - Operacion_participacion_en_compras_ventas_a_termino_de_commodities__opefci_3_6_5_2573a0
    - Operacion_participacion_en_inventarios_fisicos_de_bienes__nmcief_a3_s1_e68853
    - Operacion_participacion_en_programas_de_pruebas_de_estres__lingeef_10_3_2_2d65f4
    - Operacion_participacion_en_sistema_de_compensacion_de_transferencias__snp_tr_1_1_1_6e412c
    - Operacion_partida_960dd_lediv__ri_pgn_6_5_8d5923
    - Operacion_partida_970dd_titulos_publicos_vinculados_a_moneda_extranjera__ri_pgn_6_5_34a8dc
    - Operacion_partida_980dd_titulos_publicos_en_moneda_extranjera__ri_pgn_6_5_8af46a
    - Operacion_pase_activo_con_instrumentos_de_regulacion_monetaria_del_bcra__opefci_4_5_2_1_9401a4
    - Operacion_pase_activo_con_titulos_valores__opefci_4_5_2_1_a12d54
    - Operacion_pase_pasivo_con_entidades_financieras__opefci_4_4_2_1_6901f2
    - Operacion_pase_pasivo_con_otras_contrapartes__opefci_4_4_2_1_8ae01f
    - Operacion_pase_pasivo_con_titulos_valores_e_instrumentos_de_regulacion_monetaria__opefci_4_47d068
    - Operacion_pase_pasivo_de_moneda_extranjera__opefci_4_4_3_3_971071
    - Operacion_pase_pasivo_en_bolsas_y_mercados_autorizados__opefci_4_4_2_1_0e0fbf
    - Operacion_pases_pasivos_de_instrumentos__cajasc_3_5_2_bcc521
    - Operacion_pases_pasivos_en_pesos_30_dias_o_mas__efemin_1_3_13_1_0cf959
    - Operacion_pases_pasivos_en_pesos_hasta_29_dias__efemin_1_3_13_1_bf35e6
    - Operacion_pases_pasivos_financiaciones_recibidas__ri_dcpc_3_4_4_2_4f167d
    - Operacion_pedidos_de_confirmacion_de_saldos__nmcief_a3_s1_ea5b9b
    - Operacion_pendientes_de_envio_y_o_recepcion_de_imagen__snp_cheq_7_1_10_702c7f
    - Operacion_perforacion_de_billetes_deteriorados_superiores_a_200__cirmo3_5_1_3_3_c65c7b
    - Operacion_permanencia_en_categorias_4_y_o_5_con_garantia_hipotecaria__cajasc_9_5_2_ae283b
    - Operacion_perturbacion_de_tasa_de_corto_plazo_moneda_c__lingeef_5_4_5_2_3c85d4
    - Operacion_perturbacion_tasa_largo_plazo_moneda_c_con_rotacion__lingeef_5_4_5_3_a21ebc
    - Operacion_perturbaciones_con_rotacion_estructura_temporal_de_tasas__lingeef_5_4_5_4_d6f78d
    - Operacion_plan_de_accion_apertura_de_sucursales_en_el_exterior__expaef_1_2_4_d28321
    - Operacion_plan_de_contingencia_con_politicas_y_procedimientos__lingeef_4_3_5_4_2ab647
    - Operacion_plan_de_contingencias__lingeef_4_3_5_842b9a
    - Operacion_plan_de_contingencias_y_emergencias__ri_ccna_d2a2_3_4_3_9f9514
    - Operacion_plan_de_fondeo_para_contingencias__lingeef_3_3_11_35c1f2
    - Operacion_plan_para_contingencias__lingeef_1_4_8_fc7497
    - Operacion_plan_para_contingencias__lingeef_2_3_5_0f0cbc
    - Operacion_planes_de_contingencia__lingeef_4_2_1_5_6340e1
    - Operacion_planificacion_del_trabajo_de_auditoria__ri_ccna_d1a2_s3_acb2b2
    - Operacion_planificacion_para_contingencias__lingeef_3_1_2_6_4c09de
    - Operacion_planilla_de_aprobacion_y_analisis_de_credito_prendario__manori_3_5_2_116289
    - Operacion_poder_especial_irrevocable_para_proteger_derechos__manori_sbloque4_500c46
    - Operacion_poder_especial_irrevocable_para_reinscripcion__manori_sbloque4_1fbe2a
    - Operacion_poder_irrevocable_para_notificar_cesion_de_indemnizacion__manori_sbloque4_9043aa
    - Operacion_ponderacion_de_flujos_nocionales_netos_por_factor_de_descuento__lingeef_5_4_4_2_965ddb
    - Operacion_posicion_promedio_lineas_financieras_exterior_noviembre_18__ri_rml_sbloque14_ce5a6b
    - Operacion_posicion_unificada_bimestral_efectivo_minimo_moneda_extranjera__ri_rml_sbloque14_385db1
    - Operacion_posiciones_acercandose_a_limites_internos_o_regulatorios__lingeef_3_3_4_5_0e57d1
    - Operacion_postura_de_billetes_en_siopel_t_1__cirmo3_5_4_071306
    - Operacion_postura_en_multiplos_de_millar__cirmo3_5_2_1_6_b73ea2
    - Operacion_postura_en_packs_de_8_millares__cirmo3_5_2_1_6_d5a97e
    - Operacion_postura_en_pallets__cirmo3_5_2_1_6_939101
    - Operacion_postura_en_rueda_num_d__cirmo3_5_2_2_2_029d61
    - Operacion_posturas_a_traves_de_ruedas_de_negociacion__cirmo3_5_2_1_2_0f746b
    - Operacion_precancelacion_parcial__manori_3_1_9_2_e2e500
    - Operacion_precancelacion_parcial_de_prestamo_hipotecario__manori_1_1_9_1_803b26
    - Operacion_precancelacion_parcial_de_prestamo_hipotecario__manori_1_1_9_2_d0fc55
    - Operacion_precancelacion_parcial_de_prestamo_prendario__manori_3_1_9_1_fce759
    - Operacion_precancelacion_total__manori_3_1_9_2_2861e6
    - Operacion_precancelacion_total_de_prestamo_hipotecario__manori_1_1_9_1_a780d1
    - Operacion_precancelacion_total_de_prestamo_hipotecario__manori_1_1_9_2_12a284
    - Operacion_precancelacion_total_de_prestamo_prendario__manori_3_1_9_1_770760
    - Operacion_precancelacion_total_del_credito__manori_sbloque4_e0224f
    - Operacion_precision_del_sistema_de_calificaciones_internas__lingeef_2_3_6_4_acd349
    - Operacion_prefinanciaciones_de_exportaciones__ri_rml_3_2_a56ab6
    - Operacion_prenda_fija_maquinas_industriales__cajasc_5_5_11_938e35
    - Operacion_prenda_fija_sobre_vehiculos_automotores_y_maquinas__cajasc_5_2_2_00d23d
    - Operacion_preparacion_agregada_de_informacion_para_reportes__lingeef_3_5_5_4_0945e9
    - Operacion_preparacion_archivo_de_rechazos__snp_cheq_3_2_5_d40aff
    - Operacion_preparacion_del_archivo_de_rechazos__snp_cheq_3_2_6_1_4d91de
    - Operacion_preparacion_del_archivo_de_rechazos__snp_cheq_3_3_5_1_84c1ae
    - Operacion_preparacion_para_escenarios_severos_de_estres__lingeef_3_3_11_4_37e58c
    - Operacion_preparacion_para_escenarios_severos_de_estres__lingeef_4_3_5_3_046579
    - Operacion_presentacion_al_cobro_de_chc__cirmo3_8_4_1_3_f14018
    - Operacion_presentacion_anual_de_declaraciones_juradas_sobre_parentesco__ayccef_7_3_1_1_588ede
    - Operacion_presentacion_constancia_cuil_empleados_dependencia__manori_1_2_2_2_f28e80
    - Operacion_presentacion_constancia_inscripcion_monotributo_autonomos_y_monotributistas__man_ac1a2a
    - Operacion_presentacion_constancia_situacion_impositiva_autonomos_y_monotributistas__manori_a5c834
    - Operacion_presentacion_de_ajustes__snp_cheq_6_1_1_f714ae
    - Operacion_presentacion_de_ajustes_a_cheques_compensados__snp_cheq_3_1_1_1_da9df1
    - Operacion_presentacion_de_asistencia_de_accionistas_registrada__ayccef_2_4_7_5_c2b4b7
    - Operacion_presentacion_de_billetes_deteriorados_sin_perforar__cirmo3_5_1_3_2_6b7234
    - Operacion_presentacion_de_billetes_falsos_al_bcra__cirmo3_4_1_2_f69687
    - Operacion_presentacion_de_cedip__snp_cheq_3_6_4_1_6df65c
    - Operacion_presentacion_de_cedip__snp_cheq_7_2_3_b903c2
    - Operacion_presentacion_de_cedip_a_compensar_dia_tvto_1__snp_cheq_3_6_4_1_6_ae04ce
    - Operacion_presentacion_de_cedip_para_compensacion__snp_cheq_3_6_4_1_1_3a3d7f
    - Operacion_presentacion_de_chc_al_cobro__cirmo3_8_4_1_2_17391d
    - Operacion_presentacion_de_cheques_a_compensar__snp_cheq_6_1_1_b8259e
    - Operacion_presentacion_de_cheques_y_documentos_compensables__snp_cheq_3_1_1_1_5058e9
    - Operacion_presentacion_de_cheques_y_otros_documentos_compensables__snp_cheq_7_1_3_cadf16
    - Operacion_presentacion_de_cheques_y_otros_documentos_compensables__snp_cheq_7_1_9_887e18
    - Operacion_presentacion_de_copia_de_documento_de_identidad__manori_1_2_2_1_b7475a
    - Operacion_presentacion_de_copia_del_acta_de_aprobacion__ayccef_3_4_5_1_227d16
    - Operacion_presentacion_de_declaracion_jurada__ayccef_2_4_8_5_b222c2
    - Operacion_presentacion_de_declaracion_jurada_sobre_antecedentes__ayccef_2_4_7_6_8f6979
    - Operacion_presentacion_de_declaracion_jurada_sobre_familiares__ayccef_7_3_4_a3a794
    - Operacion_presentacion_de_declaracion_jurada_y_documentacion__depaho_3_12_3_06c3b6
    - Operacion_presentacion_de_declaraciones_juradas__ayccef_7_1_2_1_bb70af
    - Operacion_presentacion_de_documentacion_del_exterior__expaef_10_2_3_139bb3
    - Operacion_presentacion_de_documentos_con_imagen_electronica__snp_cheq_3_3_3_1_d49076
    - Operacion_presentacion_de_hoja_movil_al_banco__depaho_3_1_7_4_793496
    - Operacion_presentacion_de_imagen_cfu__snp_cheq_7_1_13_e0b72e
    - Operacion_presentacion_de_imagen_con_datos_no_coincidentes__snp_cheq_7_1_12a628
    - Operacion_presentacion_de_imagen_de_cheque__snp_cheq_7_1_58d86f
    - Operacion_presentacion_de_imagen_de_cheque_rechazado__snp_cheq_7_1_10_eb14ba
    - Operacion_presentacion_de_imagen_erronea__snp_cheq_7_1_a10f50
    - Operacion_presentacion_de_imagen_ilegible__snp_cheq_7_1_bc9275
    - Operacion_presentacion_de_imagen_reclamada__snp_cheq_7_1_12_1ac947
    - Operacion_presentacion_de_imagenes_con_archivo_asociado__snp_cheq_6_1_2_2_7013a9
    - Operacion_presentacion_de_imagenes_de_cheques_rechazados__snp_cheq_6_1_1_266f22
    - Operacion_presentacion_de_imagenes_de_reclamos__snp_cheq_6_1_1_4127d6
    - Operacion_presentacion_de_informacion_comparativa_en_estados_financieros_trimestrales__ri__2a4983
    - Operacion_presentacion_de_nomina_de_accionistas_o_socios__ayccef_2_4_7_4_acf8ba
    - Operacion_presentacion_de_nomina_de_consejeros_del_comite_de_direccion_ejecutivo__cajasc_1_4f34c7
    - Operacion_presentacion_de_nomina_de_integrantes__cajasc_1_3_8_9f7c9f
    - Operacion_presentacion_de_nomina_de_organo_de_administracion_y_gerencia__ayccef_2_4_7_3_1a7afd
    - Operacion_presentacion_de_nomina_del_consejo_de_administracion__cajasc_1_3_6_b39045
    - Operacion_presentacion_de_plan_de_negocios_y_proyecciones__ayccef_3_4_9_5_ba21c7
    - Operacion_presentacion_de_programas_de_encuadramiento__ri_rml_1_7_2_243423
    - Operacion_presentacion_de_propuesta_de_solucion_de_observaciones__ri_ccna_d2a1p2_s4_fb14dc
    - Operacion_presentacion_de_proyecto_de_acta_constitutiva_y_estatuto__ayccef_2_4_5_64cb14
    - Operacion_presentacion_de_proyecto_de_estatuto__cajasc_1_3_14_cbad60
    - Operacion_presentacion_de_rechazo_fuera_de_canje__snp_cheq_3_1_2_3_3eac0f
    - Operacion_presentacion_de_rechazos_de_entidades_giradas__snp_cheq_3_1_1_1_9227d9
    - Operacion_presentacion_de_rechazos_de_reclamos__snp_cheq_3_1_1_1_508d96
    - Operacion_presentacion_de_rechazos_fuera_de_canje__snp_cheq_3_1_1_1_e5e856
    - Operacion_presentacion_de_rechazos_por_defectos_verificables__snp_cheq_3_1_1_1_cc19a4
    - Operacion_presentacion_de_reclamo_de_cheque__snp_cheq_7_1_11_731b79
    - Operacion_presentacion_de_reclamos__snp_cheq_3_1_1_1_3303d2
    - Operacion_presentacion_de_regimen_informativo_a_sefyc__ayccef_3_6_2_c430a5
    - Operacion_presentacion_de_respuestas_de_rechazos_fuera_de_canje__snp_cheq_3_1_1_1_6eb194
    - Operacion_presentacion_de_solicitud_de_autorizacion__cajasc_1_2_4_bc5097
    - Operacion_presentacion_de_transferencias_entre_clientes_o_terceros_en_pesos_y_usd__snp_tr__06b062
    - Operacion_presentacion_de_transferencias_pago_a_proveedores_en_pesos_y_usd__snp_tr_1_3_2_0e890a
    - Operacion_presentacion_declaracion_jurada_actividades_no_permanentes__depaho_3_8_3_5_c6ea87
    - Operacion_presentacion_detalle_aportes_jubilatorios_autonomos_y_monotributistas__manori_1__8806a5
    - Operacion_presentacion_detalle_aportes_monotributo_autonomos_y_monotributistas__manori_1_2_178ef9
    - Operacion_presentacion_documentacion_laboral_empleados_dependencia__manori_1_2_2_2_40f363
    - Operacion_presentacion_duplicada_de_documento_electronico_rechazo_por_cec__snp_cheq_7_1_a9edb8
    - Operacion_presentacion_estado_apertura_nueva_entidad__ayccef_3_6_2_1_fc1ee9
    - Operacion_presentacion_estados_patrimoniales_cierre_individual__ayccef_3_6_2_1_6894fe
    - Operacion_presentacion_modelo_informacion_accionistas__ayccef_5_7_799915
    - Operacion_presentacion_nomina_autoridades_inversores_extranjeros__depaho_3_8_3_6_6c0065
    - Operacion_presentacion_nomina_autoridades_inversores_nacionales__depaho_3_8_3_6_315020
    - Operacion_prestacion_de_servicios_de_auditoria_externa__ri_ccna_d1a1_2_1_1_8f0c04
    - Operacion_prestacion_de_servicios_de_auditoria_externa__ri_ccna_d1a1_2_1_47781c
    - Operacion_prestacion_del_servicio_de_auditoria_externa__ri_ccna_d1a1_s6_06d308
    - Operacion_prestamo_con_amortizacion_integra_al_vencimiento__cajasc_4_2_2_1_0e93bf
    - Operacion_prestamo_hipotecario_a_personas_humanas__manori_1_1_1_fa9168
    - Operacion_prestamo_hipotecario_a_tasa_fija__manori_1_1_5_5_db527b
    - Operacion_prestamo_hipotecario_a_tasa_variable__manori_1_1_5_5_4a97f8
    - Operacion_prestamo_hipotecario_sobre_inmuebles_mixtos__manori_1_1_1_80e9bf
    - Operacion_prestamo_prendario_automotor_a_personas_humanas__manori_3_1_1_519704
    - Operacion_prestamo_prendario_automotor_a_tasa_fija__manori_3_1_5_5_3a3cb5
    - Operacion_prestamo_prendario_automotor_a_tasa_variable__manori_3_1_5_5_78b1a7
    - Operacion_prestamos_hipotecarios_con_metodos_especificos_de_evaluacion__manori_1_1_6_dc337c
    - Operacion_prestamos_interfinancieros_recibidos__ri_rml_3_2_6dd78a
    - Operacion_prestamos_interfinancieros_tomados__cajasc_3_5_1_6dc3d3
    - Operacion_prestamos_uva_actualizables_por_cer__manori_1_1_5_9_6abfcf
    - Operacion_prestamos_uva_actualizables_por_cer__manori_3_1_5_9_23d78c
    - Operacion_prestamos_uvi_actualizables_por_icc__manori_1_1_5_9_e50d31
    - Operacion_presuncion_de_conformidad_con_movimiento__depaho_3_4_10_470e43
    - Operacion_presuncion_de_conformidad_con_movimiento_registrado__depaho_1_12_0f7544
    - Operacion_prevision_sobre_cartera_normal__cajasc_9_4_2b3fba
    - Operacion_prevision_sobre_demas_categorias__cajasc_9_4_88291c
    - Operacion_prima_de_futuro__opefci_3_2_a6ed75
    - Operacion_primera_linea_de_defensa_gestion_en_unidades_de_negocio__lingeef_6_1_4_1d315b
    - Operacion_primera_operacion_con_fci__opefci_7_4_1_f66e79
    - Operacion_procedimiento_alternativo_intercambio_informacion__snp_tr_1_3_5_3_6ced54
    - Operacion_procedimiento_de_excepcion_por_falla_en_comunicaciones__snp_cheq_3_1_4_3_c530f6
    - Operacion_procedimiento_interconexion_entre_cec__snp_tr_1_3_3_35a55d
    - Operacion_procedimiento_intereses_capitalizados__ri_dcpc_7_1_6c1944
    - Operacion_procedimientos_alternativos_saldos_confirmaciones_no_recibidas__ri_ccna_d1a3l2_s_4b85d4
    - Operacion_procedimientos_alternativos_saldos_confirmaciones_no_recibidas__ri_ccna_d1a3l2_s_713175
    - Operacion_procesamiento_de_archivos_por_cec_dia_tvto_1__snp_cheq_3_6_4_1_6_1b6810
    - Operacion_procesamiento_de_cedip_rechazados_por_cec__snp_cheq_3_6_4_1_6_926ceb
    - Operacion_procesamiento_de_cedip_rechazados_por_girada__snp_cheq_3_6_4_1_6_bd2e1f
    - Operacion_procesamiento_de_comprobantes_de_ajustes__snp_cheq_2_2_2_5_d21629
    - Operacion_procesamiento_de_rechazos_y_compensacion_final_dia_tvto__snp_cheq_3_6_4_1_6_2283c1
    - Operacion_procesamiento_de_reclamos__snp_cheq_2_2_2_5_43d92c
    - Operacion_procesamiento_electronico_de_informacion_cedip__snp_cheq_3_6_4_1_3_d330fc
    - Operacion_procesamiento_electronico_de_informacion_de_cheques__snp_cheq_3_1_2_1_1eb767
    - Operacion_procesamiento_electronico_de_transferencias_por_cec__snp_tr_1_3_2_f4439c
    - Operacion_procesamiento_precancelaciones__manori_3_3_2_b483e1
    - Operacion_procesamiento_reclamos_indemnizacion_siniestros__manori_3_3_2_65559d
    - Operacion_procesamiento_y_depuracion_de_efectivo__cirmo3_5_1_1_4edf55
    - Operacion_proceso_integral_de_gestion_de_riesgos__lingeef_1_1_12c083
    - Operacion_procesos_compensacion_dia_tp_1__snp_cheq_3_6_4_1_6_c3e7bb
    - Operacion_procesos_compensacion_dia_tp_2__snp_cheq_3_6_4_1_6_7b05a6
    - Operacion_procesos_compensacion_dia_tp_3__snp_cheq_3_6_4_1_6_0ada32
    - Operacion_procesos_servicios_y_o_actividades_tercerizados__expaef_2_2_1_0234bd
    - Operacion_produccion_de_efectos_de_pago_del_chc__cirmo3_8_1_1_6_4bd1ed
    - Operacion_programa_de_pruebas_de_estres__lingeef_4_3_4_cffc5b
    - Operacion_programas_de_pruebas_de_estres__lingeef_11_2_2_2_687471
    - Operacion_programas_de_pruebas_de_estres_rigurosos_y_prospectivos__lingeef_1_4_7_774471
    - Operacion_propuesta_de_solucion_de_observaciones__nmcief_a1p2_s3_ed28e3
    - Operacion_provision_de_comprobante_de_transaccion_electronica__depaho_3_1_5_4_7220df
    - Operacion_provision_de_informacion_sobre_limites_y_tolerancia_al_riesgo__adrei_4_2_1_2_5729ed
    - Operacion_provision_de_reportes_de_liquidez__lingeef_3_3_5_7_9f140c
    - Operacion_provision_de_respaldo_a_estructuras_de_titulizacion__lingeef_7_2_9_ac9925
    - Operacion_provision_de_talon_en_cajeros_automaticos__depaho_2_5_dab642
    - Operacion_provision_de_tarjeta_magnetica__depaho_2_4_2_76924e
    - Operacion_provision_de_tarjeta_magnetica_de_debito__depaho_3_5_5_3dd0aa
    - Operacion_provision_de_tarjetas_magneticas_cajeros_automaticos__depaho_4_3_1_9121b3
    - Operacion_proyeccion_de_flujos_de_fondos_activos_pasivos_patrimonio_y_operaciones_fuera_de_31a0d0
    - Operacion_proyeccion_de_flujos_de_fondos_bajo_escenarios_alternativos__lingeef_3_3_2_621a8c
    - Operacion_proyeccion_de_flujos_de_fondos_nocionales__lingeef_5_4_1_6d1a21
    - Operacion_proyecto_de_reformas_al_estatuto_social__ayccef_4_3_2_4_c0610f
    - Operacion_pruebas_de_diseno_de_actividad_de_control__nmcief_a2_3_3_1_a6ad7b
    - Operacion_pruebas_de_eficacia_operativa_de_actividades_de_control__nmcief_a2_3_3_2_ddf01a
    - Operacion_pruebas_de_estres__lingeef_11_2_1_4_90e2af
    - Operacion_pruebas_de_estres__lingeef_11_2_3_1_93712f
    - Operacion_pruebas_de_estres__lingeef_4_2_1_5_781cac
    - Operacion_pruebas_de_estres__lingeef_4_2_2_4_3af163
    - Operacion_pruebas_de_estres__lingeef_4_3_4_9fbec6
    - Operacion_pruebas_de_estres__lingeef_7_3_3_6_2e6d6e
    - Operacion_pruebas_de_estres_analisis_de_escenarios__lingeef_2_3_4_ddaa3a
    - Operacion_pruebas_de_estres_analisis_de_sensibilidad__lingeef_2_3_4_a57ce0
    - Operacion_pruebas_de_estres_cobertura_de_riesgos_y_areas__lingeef_11_2_2_1_0eda6d
    - Operacion_pruebas_de_estres_con_escenarios_adversos__lingeef_4_3_4_5_194354
    - Operacion_pruebas_de_estres_con_rango_de_factores_de_riesgo__lingeef_4_3_4_1_a154b9
    - Operacion_pruebas_de_estres_con_riesgo_de_reputacion__lingeef_11_2_3_4_3b9be9
    - Operacion_pruebas_de_estres_con_riesgo_reputacional__lingeef_9_2_4_f6e8a3
    - Operacion_pruebas_de_estres_contemplando_riesgo_de_concentracion__lingeef_8_5_1_b18a16
    - Operacion_pruebas_de_estres_extremas_para_revelar_vulnerabilidades__lingeef_11_2_2_3_a95c5c
    - Operacion_pruebas_de_estres_inversas_desde_resultado_conocido__lingeef_11_2_2_3_209692
    - Operacion_pruebas_de_estres_para_escenarios_de_liquidez__lingeef_3_3_10_cf0c8a
    - Operacion_pruebas_de_estres_periodicas__lingeef_8_5_1_20ad54
    - Operacion_pruebas_de_estres_periodicas_de_exposiciones__lingeef_2_6_4_4_5b823b
    - Operacion_pruebas_de_estres_productos_complejos__lingeef_11_2_3_2_5bf4f4
    - Operacion_pruebas_globales_y_razonabilidad_ingresos_y_egresos_financieros__ri_ccna_d1a3l1__f5f7df
    - Operacion_publicacion_agregada_de_datos_en_cenfiv__snp_cheq_3_5_7_4_802f51
    - Operacion_publicacion_de_comisiones_por_servicios_delegados__expaef_9_5_5_65a5f3
    - Operacion_publicacion_de_datos_en_cenfiv__ceninf_5_1_2_9237c7
    - Operacion_publicacion_de_nomina_actualizada_de_agencias__expaef_9_5_5_8a839a
    - Operacion_publicacion_de_reglas_operativas_en_internet__expaef_9_5_5_e4aa0d
    - Operacion_puerta_de_acceso_blindada_recinto_seguridad_cctv__ri_mmsef_2_2_3_2_63262f
    - Operacion_puerta_de_doble_chapa_en_cajas_de_atencion__ri_mmsef_2_2_12_2_dc4f70
    - Operacion_puesta_a_disposicion_de_excedente_de_billetes__cirmo3_5_5_4_1_d35680
    - Operacion_puesta_a_disposicion_de_funcionalidades_de_emision_gestion_o_deposito__snp_cheq__616961
    - Operacion_puesta_a_disposicion_de_resumenes_de_cuenta__depaho_3_6_5_fc1dd5
    - Operacion_puesta_en_circulacion_de_billetes_de_nuevo_diseno__cirmo3_1_2_6_16041e
    - Operacion_puesta_en_circulacion_monedas_conmemorativas__cirmo3_s7_80016a
    - Operacion_puesta_en_marcha_de_sucursal_en_el_exterior__expaef_1_2_8_eea15d
    - Operacion_reaccion_a_luz_ultravioleta_impresion_calcografica__cirmo3_1_2_9_2_4a98a5
    - Operacion_realizacion_de_controles_por_entidad_financiera__expaef_9_6_1_2635cb
    - Operacion_realizacion_de_funciones_de_supervision_de_oficinas_de_representacion__expaef_5__ed020f
    - Operacion_realizacion_de_inversiones_en_titulos_publicos_nacionales__ayccef_2_9_4_2_84411d
    - Operacion_realizacion_de_operaciones_delegadas__expaef_9_5_3_79c98f
    - Operacion_realizacion_de_pruebas_de_estres__lingeef_1_4_4_5_1d5ce9
    - Operacion_realizacion_ejecuciones_prendarias_remates__manori_3_3_2_10c0ce
    - Operacion_recalculo_otros_saldos_ori_acumulados__ri_dcpc_7_1_465587
    - Operacion_recalculo_participaciones_en_economia_hiperinflacionaria__ri_dcpc_7_1_98da14
    - Operacion_recepcion_de_archivos_de_compensacion__snp_cheq_3_1_3_1_a85708
    - Operacion_recepcion_de_archivos_de_compensacion__snp_tr_1_3_4_2_8f4b1d
    - Operacion_recepcion_de_archivos_por_entidad_girada__snp_cheq_3_6_4_1_6_2a0053
    - Operacion_recepcion_de_depositos_a_plazo_web__ayccef_1_1_1_2_0e8415
    - Operacion_recepcion_de_depositos_en_titulos_valores__ri_dcpc_3_4_5_66a471
    - Operacion_recepcion_de_depositos_inversores_con_imposiciones_a_plazo__ayccef_1_1_1_2_2a92c0
    - Operacion_recepcion_de_depositos_organismos_internacionales_de_credito__ayccef_1_1_1_2_685260
    - Operacion_recepcion_de_embargo_judicial_por_bcra__cirmo3_8_8_532f17
    - Operacion_recepcion_de_embargo_judicial_sobre_chc__cirmo3_8_8_3648dd
    - Operacion_recepcion_de_imagen_de_cheque__snp_cheq_3_3_6_2_a0ad4f
    - Operacion_recepcion_de_informacion_de_cheques__snp_cheq_2_2_2_2_5925cc
    - Operacion_recepcion_de_informacion_electronica_de_la_cec__snp_cheq_5_2_1_6fae08
    - Operacion_recepcion_de_informacion_por_entidades_depositarias__snp_cheq_3_1_3_1_dcb449
    - Operacion_recepcion_de_informacion_por_entidades_giradas__snp_cheq_3_1_3_1_1de284
    - Operacion_recepcion_de_numerario__cirmo3_5_2_1_0dbeeb
    - Operacion_recepcion_de_rechazos_por_entidad_depositaria__snp_cheq_3_6_4_1_6_c656aa
    - Operacion_recepcion_de_rechazos_por_entidad_girada__snp_cheq_3_6_4_1_6_1298f4
    - Operacion_recepcion_de_valores_en_plaza__cirmo3_5_2_2_5_698f3f
    - Operacion_recepcion_y_compensacion_de_cedip_por_cec__snp_cheq_3_6_4_1_6_e0c42e
    - Operacion_recepcion_y_verificacion_de_billetes_deteriorados__cirmo3_5_3_3_38ba54
    - Operacion_rechazo_de_ajuste__snp_cheq_7_1_9_7adff7
    - Operacion_rechazo_de_ajuste_comision_por_fondos_inmovilizados__snp_cheq_6_2_1_e90d27
    - Operacion_rechazo_de_ajuste_por_interes__snp_cheq_6_2_1_6a1e04
    - Operacion_rechazo_de_ajuste_por_motivos_varios__snp_cheq_6_2_1_e1db7b
    - Operacion_rechazo_de_ajuste_por_presentacion_fuera_de_termino__snp_cheq_6_2_1_d53f26
    - Operacion_rechazo_de_ajuste_por_rechazo_fuera_de_termino__snp_cheq_6_2_1_c92180
    - Operacion_rechazo_de_ajustes__snp_cheq_6_1_1_8519c7
    - Operacion_rechazo_de_camara_cfu__snp_cheq_7_1_13_59768c
    - Operacion_rechazo_de_cedip_por_entidades_depositarias__snp_cheq_6_2_1_df99f9
    - Operacion_rechazo_de_cedip_por_entidades_giradas__snp_cheq_6_2_1_f09cca
    - Operacion_rechazo_de_cheque_documento_compensable__snp_cheq_8_4_2_1_b7b77e
    - Operacion_rechazo_de_cheque_por_entidad_girada__snp_cheq_3_3_7_1_ae4f84
    - Operacion_rechazo_de_cheque_r11_limite_endosos__snp_cheq_3_3_7_2_deeb79
    - Operacion_rechazo_de_cheque_r16_no_es_cheque__snp_cheq_3_3_7_2_d6551a
    - Operacion_rechazo_de_cheque_r38_firma_no_coincide__snp_cheq_3_3_7_2_76a886
    - Operacion_rechazo_de_cheque_r46_diseno_no_compensable__snp_cheq_3_3_7_2_3052fa
    - Operacion_rechazo_de_cheque_r48_imagen_ilegible__snp_cheq_3_3_7_2_7c07a8
    - Operacion_rechazo_de_cheque_r49_falta_firma_recibo__snp_cheq_3_3_7_2_c94e8c
    - Operacion_rechazo_de_cheque_r51_falta_leyenda_electronica__snp_cheq_3_3_7_2_953294
    - Operacion_rechazo_de_cheque_r82_imagen_faltante__snp_cheq_3_3_7_2_d6d266
    - Operacion_rechazo_de_cheque_r83_irregularidad_endosos__snp_cheq_3_3_7_2_31a3ee
    - Operacion_rechazo_de_cheque_r94_codigo_postal_erroneo__snp_cheq_3_3_7_2_964c9a
    - Operacion_rechazo_de_cheque_r97_presentacion_adelantada__snp_cheq_3_3_7_2_ab4279
    - Operacion_rechazo_de_cheques__snp_cheq_6_1_1_8583e4
    - Operacion_rechazo_de_echeq_y_documentos_compensables__snp_cheq_8_4_2_10_ee49ce
    - Operacion_rechazo_de_entidad_depositaria__snp_cheq_7_1_3_e8c633
    - Operacion_rechazo_de_entidad_depositaria__snp_cheq_7_1_9_c784f3
    - Operacion_rechazo_de_entidad_girada__snp_cheq_7_1_9_9cf6ad
    - Operacion_rechazo_de_imagen__snp_cheq_7_1_12_07ffaf
    - Operacion_rechazo_de_imagen_de_cheque__snp_cheq_7_1_10_8bfd8d
    - Operacion_rechazo_de_imagen_erronea__snp_cheq_7_1_4d49a7
    - Operacion_rechazo_de_imagen_por_error_en_captura__snp_cheq_7_1_798c20
    - Operacion_rechazo_de_imagen_por_ilegibilidad__snp_cheq_7_1_c4d57a
    - Operacion_rechazo_de_imagenes_de_cheques_rechazados__snp_cheq_6_1_1_60bca9
    - Operacion_rechazo_de_imagenes_de_reclamos__snp_cheq_6_1_1_928a05
    - Operacion_rechazo_de_reclamo_de_cheque__snp_cheq_7_1_11_378e85
    - Operacion_rechazo_de_solicitud_de_reclamos__snp_cheq_6_1_1_5f535b
    - Operacion_rechazo_duplicado_de_entidades_giradas_y_depositarias__snp_cheq_5_1_2_412fe1
    - Operacion_rechazo_fuera_de_canje__snp_cheq_7_1_9_bd3260
    - Operacion_rechazo_por_cuenta_inexistente__snp_cheq_7_1_74f623
    - Operacion_rechazo_por_error_de_formato__snp_cheq_7_1_85e6ae
    - Operacion_rechazo_por_fecha_de_compensacion_erronea__snp_cheq_7_1_542e6a
    - Operacion_rechazo_por_feriado_local__snp_cheq_7_1_753ce5
    - Operacion_rechazo_por_importe_erroneo__snp_cheq_7_1_459e6c
    - Operacion_rechazo_por_numero_de_cuenta_invalido__snp_cheq_7_1_747f33
    - Operacion_rechazo_por_sucursal_entidad_destino_inexistente__snp_cheq_7_1_f30122
    - Operacion_rechazo_por_transaccion_duplicada__snp_cheq_7_1_8818ce
    - Operacion_rechazos_de_ajustes__snp_cheq_7_1_3_0dde33
    - Operacion_rechazos_de_entidad_girada__snp_cheq_7_1_3_e710db
    - Operacion_rechazos_por_entidades_dia_tvto__snp_cheq_3_6_4_1_6_1e5bb1
    - Operacion_recibir_documentos_originales_en_custodia__snp_cheq_8_4_1_5_841cce
    - Operacion_reclamo_o_requerimiento_sobre_acuerdo_de_cheques__snp_cheq_8_9_521cae
    - Operacion_reclasificacion_a_nivel_inmediato_superior__cajasc_8_1_4_2_fd1122
    - Operacion_reclasificacion_a_nivel_inmediato_superior_deudor_refinanciado__cajasc_8_1_4_5_d3d0e6
    - Operacion_reclasificacion_bienes_defensa_creditos__ri_dcpc_3_5_3_92bfab
    - Operacion_reclasificacion_inmediata_a_nivel_inferior__cajasc_8_1_4_2_588d25
    - Operacion_reclasificacion_ori_a_resultados__ri_dcpc_3_1_3_3_f0d98d
    - Operacion_reconocer_interacciones_riesgo_liquidez_otros_riesgos__lingeef_3_3_1_4_d3c33e
    - Operacion_reconocimiento_de_diferencia_en_importe_de_imagen__snp_cheq_3_3_8_2_3ae9cc
    - Operacion_reconocimiento_de_intereses_cuentas_en_moneda_extranjera__ri_rml_1_11_b6235b
    - Operacion_reconocimiento_de_intereses_cuentas_en_pesos__ri_rml_1_11_dcc4ea
    - Operacion_reconocimiento_de_intereses_sobre_cuentas_en_moneda_extranjera__efemin_2_5_901cb8
    - Operacion_reconocimiento_de_intereses_sobre_proporcion_de_cuentas__efemin_2_5_548184
    - Operacion_reconocimiento_de_intereses_sobre_saldos_de_cuentas__efemin_2_4_512089
    - Operacion_reconocimiento_inicial_pasivos_a_costo_amortizado__ri_dcpc_3_2_2_1_d5d279
    - Operacion_recuento_y_clasificacion_de_numerario__cirmo3_5_5_5_2_6d9cdb
    - Operacion_redescuento_y_o_adelantos_por_iliquidez__cajasc_3_6_2_80b7ad
    - Operacion_redistribucion_de_texto_e_inclusion_de_firmas__cirmo3_1_2_9_4_da250c
    - Operacion_redistribucion_de_valor_y_textos_billete__cirmo3_1_2_9_2_14f3ac
    - Operacion_reduccion_de_exposiciones_al_rtici__lingeef_5_6_a86fb7
    - Operacion_reemplazo_de_tarjetas_de_debito_por_seguridad__depaho_1_10_3_829dc4
    - Operacion_reexpresion_activos_con_pago_aplazado__ri_dcpc_7_1_8e19c4
    - Operacion_reexpresion_activos_revaluados_post_transicion__ri_dcpc_7_1_0a7183
    - Operacion_reexpresion_activos_y_pasivos_no_monetarios__ri_dcpc_7_1_3ea824
    - Operacion_reexpresion_aportes_irrevocables__ri_dcpc_7_1_26ec71
    - Operacion_reexpresion_capital_por_capitalizacion_de_resultados__ri_dcpc_7_1_a009dc
    - Operacion_reexpresion_capital_social_y_ajuste_de_capital__ri_dcpc_7_1_f02364
    - Operacion_reexpresion_componentes_patrimonio_instrumentos_financieros__ri_dcpc_7_1_f9d91c
    - Operacion_reexpresion_de_componentes_del_estado_de_resultados_en_moneda_de_cierre__ri_dcpc_af19ac
    - Operacion_reexpresion_de_componentes_del_patrimonio_al_31_12_19__ri_dcpc_7_2_55179d
    - Operacion_reexpresion_de_informacion_contable_en_moneda_homogenea__ri_dcpc_3_7_1_3d391b
    - Operacion_reexpresion_de_movimientos_del_patrimonio_neto_en_2019__ri_dcpc_7_2_289f2b
    - Operacion_reexpresion_desde_fecha_de_incorporacion__ri_dcpc_7_1_2ae231
    - Operacion_reexpresion_primas_de_emision__ri_dcpc_7_1_66269d
    - Operacion_referenciacion_de_transferencia_en_lote__snp_tr_3_2_2_2_d2ca64
    - Operacion_refinanciacion_activos_financieros__ri_dcpc_3_1_3_3_afdf71
    - Operacion_refinanciacion_de_deuda_con_quita_de_capital__cajasc_9_8_1498fd
    - Operacion_refinanciacion_prestamo_adquisicion_alquiler__manori_3_1_5_1_63bd6e
    - Operacion_refinanciacion_prestamo_adquisicion_uso_comercial__manori_3_1_5_1_1ab4c7
    - Operacion_refinanciacion_prestamo_adquisicion_uso_particular__manori_3_1_5_1_d2dfab
    - Operacion_refinanciacion_prestamo_vivienda_no_permanente__manori_1_1_5_1_d0946f
    - Operacion_refinanciacion_prestamo_vivienda_permanente__manori_1_1_5_1_327d67
    - Operacion_registracion_de_cpd__snp_cheq_2_2_2_5_a25dfb
    - Operacion_registracion_de_la_modalidad_de_precancelacion__manori_3_1_9_3_993342
    - Operacion_registracion_de_precancelacion_parcial__manori_1_1_9_3_1700c6
    - Operacion_registracion_en_cuentas_de_orden_de_saldos_no_utilizados__ri_ccna_d1a3l2_s32_6b3f4f
    - Operacion_registro_adicional_de_ordenes_de_transferencia__snp_tr_1_7_4_16b391
    - Operacion_registro_adicional_de_rechazos_de_ordenes_de_transferencia__snp_tr_1_7_5_ca6fa5
    - Operacion_registro_adicional_informacion_de_transaccion__snp_tr_1_6_2_4_946ad2
    - Operacion_registro_de_activos_subyacentes_en_pases_activos__ri_dcpc_3_6_9_392501
    - Operacion_registro_de_altas_de_cheques_rechazados__ceninf_1_1_2_2_656a8d
    - Operacion_registro_de_cheques_certificados__snp_cheq_2_3_3_2d3121
    - Operacion_registro_de_control_fin_de_lote__snp_cheq_7_2_5_740668
    - Operacion_registro_de_costo_de_servicios_presente_y_pasado_en_beneficios_definidos__ri_dcp_6e02ba
    - Operacion_registro_de_costo_de_servicios_prestados_por_empleados__ri_dcpc_3_6_2_287542
    - Operacion_registro_de_deudores_y_morosos_de_ex_entidades_financieras__ceninf_4_1_1_4_3f1684
    - Operacion_registro_de_diferencias_en_compromisos_en_firme_no_reconocidos__ri_dcpc_3_4_3_1_c8e1e1
    - Operacion_registro_de_ingreso_de_fcem__snp_cheq_3_5_2_2_cd266d
    - Operacion_registro_de_inhabilitaciones_en_archivo_inhab_txt__ceninf_3_2_1_9dce62
    - Operacion_registro_de_letras_hipotecarias_escriturales__manori_1_2_8_4_247aa4
    - Operacion_registro_de_nomina_de_autorizados_a_operar__depaho_4_18_1_5_582a1f
    - Operacion_registro_de_novedades_sobre_fcem__snp_cheq_3_5_2_2_d5762b
    - Operacion_registro_de_numero_de_inscripcion_electoral__depaho_4_18_1_4_76a5b9
    - Operacion_registro_de_operaciones_y_variaciones_patrimoniales__ri_dcpc_s2_80d6e4
    - Operacion_registro_de_planes_post_empleo_de_beneficios_definidos__ri_dcpc_3_6_2_b8bb44
    - Operacion_registro_de_prestamos_e_inversiones_a_plazo_en_pesos_con_retribucion_variable__r_0f128b
    - Operacion_registro_de_propiedad_planta_y_equipo_por_costo__ri_dcpc_3_5_1_2_7390d1
    - Operacion_registro_de_resultados_de_instrumentos_de_cobertura__ri_dcpc_3_4_3_1_d538b0
    - Operacion_registro_de_variaciones_de_activos_y_pasivos_en_ori__ri_dcpc_3_6_3_938816
    - Operacion_registro_en_ori_de_cobertura_de_patrimonio__ri_dcpc_3_4_3_1_3296f4
    - Operacion_registro_individual_de_rechazo_de_cedip_entidad_depositaria__snp_cheq_7_2_4_dc2c92
    - Operacion_registro_individual_de_rechazo_de_cedip_entidad_girada__snp_cheq_7_2_4_3b37cc
    - Operacion_registro_individual_de_rechazos_fuera_de_canje__snp_cheq_7_1_5_dcc0ab
    - Operacion_registro_individual_de_transaccion__snp_cheq_sbloque5_20af1a
    - Operacion_registro_individual_de_transacciones__snp_cheq_sbloque10_0bc698
    - Operacion_reject_de_imagenes_de_reclamos_presentadas__snp_cheq_7_1_12_6220a3
    - Operacion_reject_de_imagenes_rechazadas__snp_cheq_7_1_12_fb5373
    - Operacion_reject_de_presentacion_de_imagen__snp_cheq_7_1_10_05000a
    - Operacion_reject_de_presentacion_de_reclamo__snp_cheq_7_1_11_300438
    - Operacion_reject_de_rechazo_de_entidad_depositaria__snp_cheq_7_1_3_a3d193
    - Operacion_reject_de_rechazo_de_imagen__snp_cheq_7_1_10_2dafd1
    - Operacion_reject_de_rechazo_de_reclamo__snp_cheq_7_1_11_0a2bcf
    - Operacion_relevamiento_controles_teleprocesamiento__ri_ccna_d2a2_3_4_4_a1dc80
    - Operacion_relevamiento_de_medidas_de_continuidad_del_procesamiento__ri_ccna_d2a2_3_4_3_2c0fec
    - Operacion_relevamiento_seguridad_logica_implantada__ri_ccna_d2a2_3_4_2_65929c
    - Operacion_relevamiento_y_evaluacion_del_control_interno__ri_ccna_d1a3l1_sa_3_cecde5
    - Operacion_remensura_impuestos_diferidos__ri_dcpc_7_1_7c4bf9
    - Operacion_remision_a_estado_caducado_de_echeq_vencido__snp_cheq_3_4_5_943c4a
    - Operacion_remision_de_archivo_a_entidades_depositarias__snp_cheq_3_6_4_1_6_7e6975
    - Operacion_remision_de_archivo_cedip_a_presentar_dia_tvto_1__snp_cheq_3_6_4_1_6_1e54ef
    - Operacion_remision_de_billete_con_falla_al_bcra__cirmo3_3_3_670e90
    - Operacion_remision_de_billetes_no_canjeables_al_bcra__cirmo3_2_3_44aaf8
    - Operacion_remision_de_billetes_sin_valor_al_bcra__cirmo3_3_5_6e97d7
    - Operacion_remision_de_composicion_del_grupo_y_exposicion_de_integrantes__ri_gerc_2_4_0779eb
    - Operacion_remision_del_regimen_informativo_balance_de_saldos__ri_dcpc_s2_4103dd
    - Operacion_remuneracion_de_saldos_a_tasa_de_interes__depaho_3_11_8_6b445a
    - Operacion_repeticion_de_saldo_en_dias_sin_movimiento__efemin_2_2_a77601
    - Operacion_repeticion_de_sigla_bcra_en_microletra__cirmo3_1_2_9_4_80d741
    - Operacion_reporte_de_facturas_impagas_por_falta_de_fondos__snp_cheq_3_5_7_3_6648ec
    - Operacion_reporte_de_facturas_impagas_por_falta_de_informacion__snp_cheq_3_5_7_3_0612f8
    - Operacion_reporte_de_facturas_impagas_por_otros_motivos__snp_cheq_3_5_7_3_567747
    - Operacion_reporte_de_informacion_de_cuenta_de_cobro__snp_cheq_3_5_7_2_89d3bc
    - Operacion_reporte_de_resumenes_de_exposiciones_al_rtici__lingeef_5_3_4_1_ba6ca9
    - Operacion_reporte_numero_de_serie_caja_tesoro_movil__ri_mmsef_2_3_5_2_2da840
    - Operacion_reporte_numero_de_serie_caja_tesoro_movil__ri_mmsef_2_3_7_2_2_2bc1df
    - Operacion_representacion_de_personas_juridicas_apertura_de_cuenta__depaho_4_1_1_5fdf78
    - Operacion_reproduccion_de_efigies_en_anverso_de_billete_100__cirmo3_1_2_1_5f1c07
    - Operacion_reproduccion_de_efigies_en_anverso_de_billete_10__cirmo3_1_2_1_402a5f
    - Operacion_reproduccion_de_efigies_en_anverso_de_billete_20__cirmo3_1_2_1_167f7c
    - Operacion_reproduccion_de_efigies_en_anverso_de_billete_50__cirmo3_1_2_1_cb77fc
    - Operacion_reproduccion_de_vineta_en_reverso_de_billete_100__cirmo3_1_2_1_1b75fe
    - Operacion_reproduccion_de_vineta_en_reverso_de_billete_10__cirmo3_1_2_1_a2c449
    - Operacion_reproduccion_de_vineta_en_reverso_de_billete_20__cirmo3_1_2_1_f64350
    - Operacion_reproduccion_de_vineta_en_reverso_de_billete_50__cirmo3_1_2_1_35dc56
    - Operacion_residencia_en_sitio_seguro_bcra__ceninf_1_1_8437c1
    - Operacion_residencia_en_sitio_seguro_bcra__ceninf_s3_bbc90e
    - Operacion_resolucion_de_transferencia_inmediata__snp_tr_2_2_12_b1126e
    - Operacion_resolucion_inmediata_de_transaccion__snp_tr_2_2_13_9c5c2a
    - Operacion_respaldo_contractual_a_titulizacion__lingeef_7_3_1_bef5af
    - Operacion_respaldo_crediticio_implicito_a_titulizacion__lingeef_7_3_1_1_c06d49
    - Operacion_respaldo_crediticio_implicito_a_titulizacion__lingeef_7_3_1_8f3ecb
    - Operacion_respuesta_de_rechazo_fuera_de_canje__snp_cheq_7_1_9_1f1954
    - Operacion_respuesta_de_rechazos_fuera_de_canje__snp_cheq_6_1_1_f208a6
    - Operacion_respuesta_del_aplicativo_de_consulta__cirmo3_8_5_c70c70
    - Operacion_resultados_no_asignados_componente_de_rpc__cajasc_2_7_4_303c5e
    - Operacion_retencion_de_billetes_presuntamente_falsos_sin_valor_o_entintados__cirmo3_4_1_1_35b7bf
    - Operacion_retencion_de_billetes_y_monedas_falsos_o_sin_valor__cirmo3_4_1_450580
    - Operacion_retencion_de_chc_con_oposicion__cirmo3_8_9_4_f5e69f
    - Operacion_retencion_de_tarjeta_por_cajero__depaho_4_3_2_9_797a43
    - Operacion_retiro_de_circulacion_de_monedas_y_billetes__cirmo3_2_2_934165
    - Operacion_retiro_de_fondos__depaho_3_1_6_2_13ee78
    - Operacion_retiro_de_fondos_del_fondo_de_cese_laboral__depaho_3_1_6_1_22674b
    - Operacion_retiro_en_efectivo_de_fondos__depaho_3_1_6_4_ceb4da
    - Operacion_retiros_de_efectivo_cajeros_automaticos__efemin_1_5_2_a903dd
    - Operacion_retiros_de_fondos_del_fondo_de_cese_laboral__depaho_3_1_7_5_062b3b
    - Operacion_retiros_parciales_cese_de_relacion_laboral__depaho_3_17_2_feaae0
    - Operacion_reversion_de_debitos_y_creditos_por_inconsistencia_posterior__snp_tr_4_2_cae947
    - Operacion_reversion_preventiva_de_credito_por_ilegitimidad__cirmo3_8_6_2_1_e01fb1
    - Operacion_revision_compilacion_listados_acreedores_depositos__ri_ccna_d1a3l2_s19_b3dc28
    - Operacion_revision_compilacion_listados_deudores_por_prestamos__ri_ccna_d1a3l2_s8_7110d2
    - Operacion_revision_cumplimiento_normas_bcra_monetarias__ri_ccna_d1a3l2_s27_4e6858
    - Operacion_revision_de_adecuada_valuacion_de_otros_activos__ri_ccna_d1a3l2_s18_178229
    - Operacion_revision_de_adecuada_valuacion_de_otros_pasivos__ri_ccna_d1a3l2_s24_b4b4e1
    - Operacion_revision_de_conciliaciones_bancarias__ri_ccna_d1a3l2_s3_9b91d8
    - Operacion_revision_de_cuentas_de_resultados__nmcief_a3_s1_6a456a
    - Operacion_revision_de_documentacion_presentada_al_bcra__nmcief_a3_s1_d08f1b
    - Operacion_revision_de_hechos_y_transacciones_posteriores_al_cierre__ri_ccna_d1a3l2_s30_421e2d
    - Operacion_revision_de_liquidacion_de_remuneraciones_al_personal__ri_ccna_d1a3l2_s28_eb36a6
    - Operacion_revision_de_otros_creditos_no_mencionados__ri_ccna_d1a3l2_s12_7c947a
    - Operacion_revision_de_parametros_internos_de_riesgo__lingeef_5_6_f64ba7
    - Operacion_revision_de_razonabilidad_de_capitalizaciones_primas_e_intereses__ri_ccna_d1a3l2_6b30ae
    - Operacion_revision_de_regulaciones_especificas__nmcief_a3_s1_d33126
    - Operacion_revision_de_saldos_adeudados_al_bcra__ri_ccna_d1a3l2_s21_7d1c67
    - Operacion_revision_de_saldos_de_partidas_pendientes_de_imputacion__ri_ccna_d1a3l2_s17_312499
    - Operacion_revision_de_saldos_pagos_por_cuenta_de_terceros__ri_ccna_d1a3l2_s12_ad3766
    - Operacion_revision_incremento_exigencia_capital_minimo_riesgo_credito__ri_ccna_d1a3l2_s27_757160
    - Operacion_revision_ingreso_efectivo_fondos_aumentos_capital__ri_ccna_d1a3l2_26_2_377729
    - Operacion_revision_montos_comprometidos_por_asociados__ri_ccna_d1a3l2_26_2_1e096d
    - Operacion_revision_movimientos_bienes_de_uso_y_diversos__ri_ccna_d1a3l2_s13_747ccc
    - Operacion_revision_movimientos_periodo_y_valuacion_intangibles__ri_ccna_d1a3l2_s16_cfcf29
    - Operacion_revision_periodica_independiente_del_marco_de_gestion_del_riesgo_de_mercado__lin_b8a426
    - Operacion_revision_razonabilidad_ajustes_resultados_ejercicios_anteriores__ri_ccna_d1a3l2__7d2d64
    - Operacion_revision_razonabilidad_capitalizaciones_primas_e_intereses__ri_ccna_d1a3l2_s10_27f4ec
    - Operacion_revision_razonabilidad_deudas_sociales_y_fiscales__ri_ccna_d1a3l2_s22_2b0249
    - Operacion_revision_razonabilidad_valuacion_bienes_diversos__ri_ccna_d1a3l2_s15_6b9227
    - Operacion_saldos_inmovilizados_de_depositos_judiciales__efemin_1_3_7_9a43ed
    - Operacion_seguimiento_de_indices_de_liquidez__lingeef_3_1_2_4_0cdc72
    - Operacion_seguimiento_de_lineas_de_credito_intradiario__lingeef_3_5_3_2_17c182
    - Operacion_seguimiento_de_liquidez_intradiaria_disponible_al_inicio_del_dia__lingeef_3_5_3__f6e19b
    - Operacion_seguimiento_de_obligaciones_con_vencimiento_intradiario_especifico__lingeef_3_5__72538f
    - Operacion_seguimiento_de_pagos_brutos__lingeef_3_5_3_1_0b94c6
    - Operacion_seguimiento_de_pagos_por_corresponsalia__lingeef_3_5_3_2_15aa71
    - Operacion_seguimiento_de_sensibilidad_del_valor_economico_y_resultados__lingeef_5_7_1_2d36a8
    - Operacion_seguimiento_del_riesgo_de_liquidez__lingeef_3_3_5_171c03
    - Operacion_seguimiento_diario_de_cumplimiento_de_politicas_y_limites_de_liquidez__lingeef_3_47eee1
    - Operacion_seguimiento_diario_maximo_de_liquidez_intradiaria__lingeef_3_5_3_1_005351
    - Operacion_seguimiento_y_control_activo_de_exposicion_al_riesgo_de_liquidez__lingeef_3_3_6__f67f06
    - Operacion_seguimiento_y_control_del_riesgo_de_liquidez__lingeef_3_3_6_2_a8df68
    - Operacion_seguimiento_y_regularizacion_de_atrasos_en_pagos__manori_3_3_5_d988a0
    - Operacion_segunda_linea_de_defensa_gestion_independiente_del_riesgo_operacional__lingeef_6_dcc787
    - Operacion_seguridad_fisica_del_procesamiento_de_datos__ri_ccna_d2a2_3_4_3_74b14b
    - Operacion_separacion_de_financiaciones_con_garantias_preferidas_a__cajasc_9_2_4_aee0fa
    - Operacion_servicio_de_consulta_de_cuentas_activas__snp_tr_2_3_2_3_e0af19
    - Operacion_servicio_de_policia_adicional_vigilancia__ri_mmsef_2_2_10_1_428a8f
    - Operacion_servicio_de_transferencias_inmediatas__snp_tr_2_2_15_e302a8
    - Operacion_servicio_de_transferencias_inmediatas__snp_tr_2_2_1_681d43
    - Operacion_servicios_de_cobranza_por_cuenta_de_terceros__cajasc_3_1_2f0742
    - Operacion_servicios_y_movimientos_en_caja_de_ahorros_de_menores__depaho_3_10_5_cfee11
    - Operacion_servicios_y_movimientos_sin_costo__depaho_3_7_4_1d543c
    - Operacion_sesion_de_intercambio_de_imagenes_de_cheques_rechazados__snp_cheq_3_2_8_f75dd6
    - Operacion_sesion_de_presentacion_de_imagenes_rechazadas_y_o_faltantes__snp_cheq_sbloque3_2587b7
    - Operacion_sesion_de_presentacion_de_imagenes_reclamadas__snp_cheq_sbloque3_c7fe81
    - Operacion_sesion_de_presentacion_de_imagenes_requeridas__snp_cheq_3_2_8_2_efdbd7
    - Operacion_sesion_de_rechazo_de_imagenes__snp_cheq_sbloque3_fa7973
    - Operacion_sesion_de_rechazo_de_imagenes_e_informe_final__snp_cheq_3_2_8_2_27bb1b
    - Operacion_sesion_de_rechazos_de_imagenes_reenviadas_e_informe_final__snp_cheq_sbloque3_f300dd
    - Operacion_sesion_presentados__snp_cheq_3_1_2_2_b0a375
    - Operacion_sesion_rechazados__snp_cheq_3_1_2_2_2f7ba5
    - Operacion_sesiones_de_transmision_diarias_cec__snp_cheq_3_1_1_1_def5cb
    - Operacion_sistema_de_monitoreo_remoto__ri_mmsef_2_2_1_4ea604
    - Operacion_sistema_de_monitoreo_remoto_propio__ri_mmsef_2_5_6_1_7e641a
    - Operacion_situaciones_de_emergencia_rechazo_por_entidad_girada__snp_cheq_7_1_94c033
    - Operacion_sol_de_mayo_con_tinta_cromatica__cirmo3_1_2_12_3_7c14f7
    - Operacion_solicitud_de_autorizacion_para_incorporar_participaciones__expaef_6_3_d89c4a
    - Operacion_solicitud_de_chequeras_de_cheques_cancelatorios__cirmo3_8_2_2_1c1fc8
    - Operacion_solicitud_de_credito_prendario_automotor__manori_3_5_1_818787
    - Operacion_solicitud_de_informe_de_tasacion__manori_1_2_4_ba19a0
    - Operacion_solicitud_de_prestamo_hipotecario__manori_1_2_1_deeb93
    - Operacion_solicitud_de_prestamo_prendario_automotor__manori_3_1_3_962f45
    - Operacion_solicitud_de_prestamo_prendario_automotor__manori_3_2_1_c3f807
    - Operacion_solicitud_de_rechazos_fuera_de_canje__snp_cheq_6_1_1_067112
    - Operacion_solicitud_de_reclamos__snp_cheq_6_1_1_5dbcdb
    - Operacion_solicitud_de_transferencia_por_cliente_originante__snp_tr_1_3_1_827607
    - Operacion_solicitud_informe_comercial_o_crediticio__manori_1_2_3_76c356
    - Operacion_solicitud_informe_comercial_o_crediticio__manori_3_2_3_eb2546
    - Operacion_suma_total_creditos_archivo__snp_cheq_7_2_6_7136b2
    - Operacion_suma_total_debitos_archivo__snp_cheq_7_2_6_17e3ff
    - Operacion_suministro_de_base_de_titulares_a_cec__snp_tr_1_4_1_007498
    - Operacion_suministro_de_cambio_de_numerario__cirmo3_3_1_3_b3d809
    - Operacion_suministro_de_informacion_al_depositario__snp_cheq_8_4_2_7_a33f99
    - Operacion_sumision_a_jurisdiccion_de_tribunales_ordinarios__manori_sbloque4_72f6e1
    - Operacion_supervision_de_aprobacion_aplicacion_y_revision_de_politicas__lingeef_5_2_1_4_d489db
    - Operacion_suscripcion_de_acuerdo_sobre_truncamiento_y_gestion_electronica_de_cheques__snp__1a90f4
    - Operacion_suscripcion_de_cuotapartes_fci_mercado_de_dinero_menores_adolescentes__depaho_3__0d1fda
    - Operacion_suscripcion_del_capital_en_acto_constitutivo__ayccef_2_9_2_1_e9f9ed
    - Operacion_sustitucion_del_socio_responsable__ri_ccna_d1a1_5_4_ebc7d8
    - Operacion_tareas_de_auditoria_externa__ri_ccna_d1a2_s1_d239f4
    - Operacion_tasacion_de_propiedad__manori_1_1_11_b70f73
    - Operacion_tasacion_del_inmueble_dentro_de_90_dias__manori_1_1_7_3_215b0d
    - Operacion_tasacion_del_inmueble_hipotecado__cajasc_9_5_2_2_ea7a6d
    - Operacion_tasacion_interna_del_inmueble__manori_1_2_4_2_e65e7e
    - Operacion_tecnicas_de_mitigacion_de_riesgos__lingeef_11_2_3_1_521fa4
    - Operacion_tenencia_de_acciones_en_cartera_de_negociacion__lingeef_4_1_1_1_949c9c
    - Operacion_tenencia_de_billetes_en_buen_uso_cib__cirmo3_5_5_2_2c057d
    - Operacion_tenencia_de_certificado_de_aptitud__ri_mmsef_2_2_8_3_2_0589ab
    - Operacion_tenencia_de_certificado_de_aptitud_tesoro_blindado__ri_mmsef_2_2_9_1_6_0317fb
    - Operacion_tenencia_de_cuotapartes_de_fci__opefci_7_2_1_1_edb980
    - Operacion_tenencia_instrumentos_bcra_y_titulos_publicos__cajasc_4_8_7_1_0cc16c
    - Operacion_tercera_linea_de_defensa_revision_independiente__lingeef_6_1_4_dde614
    - Operacion_tercerizacion_de_procesos_servicios_y_o_actividades_de_tecnologia_y_seguridad__e_8a8234
    - Operacion_tercerizacion_del_control_de_fallas_tecnicas__expaef_4_5_2_4_e5f52e
    - Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_14_3_51c1f2
    - Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_15_3_58046e
    - Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_19_3_d9a9bc
    - Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_20_3_7ae288
    - Operacion_tinta_de_variabilidad_optica__cirmo3_1_2_21_3_f460f4
    - Operacion_tinta_de_variabilidad_optica_anverso__cirmo3_1_2_17_3_d611a9
    - Operacion_tinta_de_variabilidad_optica_en_escarapela_nacional__cirmo3_1_2_13_3_435a46
    - Operacion_tinta_iridiscente_en_reverso__cirmo3_1_2_18_3_116e13
    - Operacion_tinta_iridiscente_reverso__cirmo3_1_2_16_3_e900f1
    - Operacion_tinta_variabilidad_optica_imagen_del_sol__cirmo3_1_2_22_3_687855
    - Operacion_titulizacion_con_fines_de_fondeo__lingeef_7_1_3_b7220c
    - Operacion_titulos_deuda_certificados_fideicomisos_financieros_codigos_260_m_y_262_m__ri_rm_b8ea8d
    - Operacion_titulos_deuda_certificados_fideicomisos_financieros_codigos_261_m_y_263_m__ri_rm_147662
    - Operacion_toma_de_decisiones_en_entidades_financieras__adrei_1_2_821a9b
    - Operacion_toma_de_posiciones_30_39_del_registro_de_rechazo__snp_cheq_7_1_1a5c2d
    - Operacion_toma_de_posiciones_57_a_60_del_registro_de_rechazo__snp_cheq_7_1_928a15
    - Operacion_toma_de_posiciones_61_64_del_registro_de_rechazo__snp_cheq_7_1_536cdc
    - Operacion_tomar_recaudos_operativos_para_estandares_de_performance_y_disponibilidad__snp_t_7021b4
    - Operacion_tradicion_de_acciones__ayccef_5_2_5_1_6f87c7
    - Operacion_tradicion_de_especie_y_contrapartida__opefci_4_4_2_3_dc103f
    - Operacion_traduccion_de_documentacion_al_castellano__ayccef_6_4_3_2_a78476
    - Operacion_transaccion_inexistente__snp_cheq_7_1_43d66b
    - Operacion_transferencia__snp_tr_1_6_1_3faeaa
    - Operacion_transferencia_de_fondos_a_cuenta_del_trabajador__depaho_3_1_6_4_58d625
    - Operacion_transferencia_de_fondos_a_cuenta_especial__depaho_3_1_6_3_af13f3
    - Operacion_transferencia_de_fondos_a_saldos_inmovilizados__depaho_4_6_1_320de4
    - Operacion_transferencia_de_fondos_atp__snp_tr_3_2_4_2_f9b1f7
    - Operacion_transferencia_de_fondos_de_comercio__ayccef_3_7_fa72f2
    - Operacion_transferencia_de_fondos_remanentes_a_saldos_inmovilizados__depaho_2_8_79328a
    - Operacion_transferencia_de_fondos_remanentes_a_saldos_inmovilizados__depaho_3_5_7_c79bd3
    - Operacion_transferencia_de_fondos_tras_cese_laboral__depaho_3_17_1_9faf48
    - Operacion_transferencia_de_la_letra_hipotecaria__manori_sbloque4_d6d7b6
    - Operacion_transferencia_del_exterior_pendiente_de_liquidacion__efemin_1_1_2_7_87eacd
    - Operacion_transferencia_electronica_de_cedip__snp_cheq_3_6_11052f
    - Operacion_transferencia_electronica_de_pagos_judiciales__depaho_3_6_4_29bea7
    - Operacion_transferencia_entre_clientes_o_clientes_y_terceros__snp_tr_1_2_2_1_36ed5a
    - Operacion_transferencia_entre_clientes_y_o_terceros__snp_tr_1_7_4_563350
    - Operacion_transferencia_entre_cuentas_de_distintas_entidades__snp_tr_1_2_1_811f1c
    - Operacion_transferencia_fiduciaria_de_inmuebles_fideicomitidos__cajasc_5_2_5_7_9f7f7f
    - Operacion_transferencia_hacia_cuentas_con_registro_de_seguimiento_arca__depaho_3_16_3_1_f46311
    - Operacion_transferencia_hacia_otras_cuentas_especiales_de_regularizacion__depaho_3_16_3_1_ad8d09
    - Operacion_transferencia_mep_debito_y_acreditacion__cirmo3_8_3_4_27a86a
    - Operacion_transferencia_minorista_moneda_extranjera_plazo_48_horas__snp_tr_1_3_6_1_5e48a6
    - Operacion_transferencia_pago_a_proveedores__snp_tr_1_2_2_1_ac23e8
    - Operacion_transferencia_pesos_plazo_24_horas__snp_tr_1_3_6_1_94b54c
    - Operacion_transferencia_por_asignaciones_familiares__snp_tr_3_2_4_1_413a94
    - Operacion_transferencia_recibida_por_entidad_receptora__snp_tr_1_4_4_8e7358
    - Operacion_transferencias_a_cuentas_a_la_vista_para_uso_judicial__depaho_4_10_2_9c1f95
    - Operacion_transferencias_atm_autoservicio__expaef_4_5_1_1_60eaa0
    - Operacion_transferencias_de_fondos_del_fondo_de_cese_laboral__depaho_3_1_7_5_35ece1
    - Operacion_transferencias_electronicas_para_creditos__depaho_3_8_7_ac4d8b
    - Operacion_transferencias_electronicas_y_ordenes_telefonicas__depaho_1_6_3_c29d27
    - Operacion_transferencias_electronicas_y_ordenes_telefonicas__depaho_1_7_3_79bb57
    - Operacion_transferencias_en_lote_precios_a_clientes__snp_tr_1_2_4_cd601d
    - Operacion_transferencias_inmediatas__snp_tr_2_2_5_35b046
    - Operacion_transferencias_inmediatas_en_pesos_y_dolares__snp_tr_2_2_9_81739d
    - Operacion_transferencias_inmediatas_servicio_de_debito_y_acreditacion_instantanea__snp_tr__f79a48
    - Operacion_transferencias_minoristas_entre_entidades__snp_tr_1_2_2_1_66f80f
    - Operacion_transferencias_ordenadas_por_personas_humanas__depaho_3_4_6_2_3898c8
    - Operacion_transferencias_por_medios_electronicos__depaho_2_3_2_5_b443f9
    - Operacion_transferencias_por_medios_electronicos__depaho_3_11_5_5_473cae
    - Operacion_transferencias_y_pagos_por_medios_electronicos__depaho_3_7_3_3_baf26f
    - Operacion_transformacion_de_caja_de_ahorros_en_cuenta_sueldo__depaho_2_1_abba0d
    - Operacion_transmision_de_acciones_o_integracion_de_aportes_irrevocables__ayccef_5_2_2_1_6ced8b
    - Operacion_transmision_de_archivos_de_cheques_a_cec__snp_cheq_3_1_1_4bd63d
    - Operacion_transmision_de_cedip__snp_cheq_3_6_2_1_b37bcd
    - Operacion_transmision_de_datos_imagenes_a_entidad_girada__snp_cheq_8_4_1_13_ff0ce3
    - Operacion_transmision_de_fcem__snp_cheq_3_5_3_08b2c6
    - Operacion_transmision_de_fcem_a_terceros__snp_cheq_3_5_2_2_5c954b
    - Operacion_transmision_de_imagenes_a_entidades_giradas__snp_cheq_3_2_8_210657
    - Operacion_transmision_de_imagenes_y_registro_a_entidades_giradas__snp_cheq_3_2_8_3_265c2e
    - Operacion_transmision_electronica_de_cedip__snp_cheq_3_6_7_3_117a90
    - Operacion_transmision_electronica_de_informacion_de_cheques__snp_cheq_3_2_1_7667cd
    - Operacion_transmision_en_procuracion_cedip__snp_cheq_3_6_3_2_e5334d
    - Operacion_transmision_integra_de_instruccion_al_sistema_de_almacenamiento__snp_cheq_8_4_4__09db8c
    - Operacion_transmision_para_negociacion_bursatil_cedip__snp_cheq_3_6_3_2_664b8f
    - Operacion_transmisiones_sucesivas_por_sca__snp_cheq_3_5_2_5_a5ed54
    - Operacion_traslado_de_exigencia_de_efectivo_minimo__ri_rml_1_4_1_adf38a
    - Operacion_traslado_de_exigencia_no_integrada__efemin_1_7_2_cbcd79
    - Operacion_traslado_de_fondos_a_saldos_inmovilizados__depaho_1_13_2_1_3d3452
    - Operacion_traslado_de_sucursales_categorias_i_y_ii__expaef_11_2_e324d5
    - Operacion_traslado_de_sucursales_categorias_iii_a_vi_entre_provincias__expaef_11_2_35c337
    - Operacion_traslado_de_sucursales_en_el_pais__expaef_1_7_9ecae6
    - Operacion_traslado_exceso_defecto_subperiodo_1_al_subperiodo_2__ri_rml_s6_0e2c5b
    - Operacion_tratamiento_de_bono_a_tasa_fija_con_opcion_de_recompra__lingeef_5_4_2_1_780a0b
    - Operacion_tratamiento_de_cheques_fisicos_nominados_en_pesos__snp_cheq_2_3_89ca86
    - Operacion_tratamiento_de_titulo_de_deuda_a_tasa_variable_con_floor__lingeef_5_4_2_1_9249da
    - Operacion_tratamiento_exposiciones_no_alcanzadas__ri_gerc_2_4_1_73b537
    - Operacion_tratamiento_otros_componentes_de_patrimonio__ri_dcpc_7_1_014b06
    - Operacion_tratamiento_reservas_de_utilidades__ri_dcpc_7_1_e491bd
    - Operacion_truncamiento_de_cheques__snp_cheq_2_1_0eea74
    - Operacion_truncamiento_de_cheques__snp_cheq_s4_db4792
    - Operacion_uso_de_pruebas_de_estres__lingeef_4_1_2_4_3527bc
    - Operacion_utilizacion_de_banca_por_internet__depaho_3_5_4_e83336
    - Operacion_utilizacion_de_fondos_acreditados_capitulo_i_decreto_679_22__depaho_3_15_3_5ed0da
    - Operacion_utilizacion_de_herramientas_de_seguimiento_de_liquidez_intradiaria__lingeef_3_5__f7f266
    - Operacion_utilizacion_de_tecnicas_de_cobertura_del_riesgo_de_credito__lingeef_2_5_1_f094e6
    - Operacion_utilizacion_de_terminales_de_telefonia_movil__ri_mmsef_2_2_14_985a3a
    - Operacion_utilizacion_del_sistema_de_gestion_del_riesgo_de_credito_de_contraparte__lingeef_02022e
    - Operacion_valor_de_venta_de_proyectos_inmobiliarios_comparables__manori_1_1_7_3_d4dcb2
    - Operacion_valuacion_a_precios_de_mercado__lingeef_4_3_6_2_8699f0
    - Operacion_valuacion_de_inversiones_y_bienes_en_locacion_financiera__ri_ccna_d1a3l2_s7_95bde1
    - Operacion_valuacion_de_posiciones_en_cartera_de_negociacion__lingeef_4_3_6_3_967740
    - Operacion_valuacion_prudente_de_instrumentos_financieros__lingeef_4_1_2_3_280a3e
    - Operacion_valuacion_segun_modelo__lingeef_4_3_6_2_44a2e9
    - Operacion_variacion_de_valor_razonable_de_propiedades_de_inversion__ri_dcpc_3_5_4_2_5cd6b1
    - Operacion_venta_al_contado_a_liquidar_con_moneda__ri_dcpc_3_4_6_938b40
    - Operacion_venta_de_activos_inmovilizados__cajasc_10_3_2_2_7c7717
    - Operacion_venta_de_chc_a_cliente__cirmo3_8_3_4_81295c
    - Operacion_venta_de_contratos_de_opciones__opefci_6_2_34b216
    - Operacion_venta_de_mercaderias_por_agricultores_exportadores__depaho_3_12_1_2_24535a
    - Operacion_venta_de_moneda_extranjera_para_obtener_pesos__depaho_3_16_3_68e519
    - Operacion_venta_de_titulos_al_contado_a_liquidar__ri_dcpc_3_4_6_8103f7
    - Operacion_venta_o_baja_activos_financieros_a_valor_razonable__ri_dcpc_3_1_3_3_879bc4
    - Operacion_venta_o_compromiso_de_activos_en_estres_de_liquidez__lingeef_3_3_12_e9e7b6
    - Operacion_venta_y_gestion_de_cheque_cancelatorio__cirmo3_8_10_fb3fa5
    - Operacion_ventas_mediante_tarjetas_de_debito_prepagas_credito_y_o_compra__efemin_1_1_2_8_21d6fe
    - Operacion_verificacion_adhesion_a_cec__snp_tr_1_5_1_9d051d
    - Operacion_verificacion_adhesion_a_la_cec__snp_cheq_5_1_1_5e7894
    - Operacion_verificacion_campos_de_inclusion_mandatoria__snp_tr_1_5_1_603929
    - Operacion_verificacion_campos_mandatorios__snp_cheq_5_1_1_e52e52
    - Operacion_verificacion_cantidad_de_lotes__snp_cheq_5_1_1_6c3871
    - Operacion_verificacion_caracteres_validos__snp_cheq_5_1_1_884062
    - Operacion_verificacion_cuit_cuil_o_cdi_del_beneficiario__snp_tr_1_5_1_3aa763
    - Operacion_verificacion_cumplimiento_observaciones_inspeccion_bcra__ri_ccna_d1a3l2_s36_151497
    - Operacion_verificacion_de_caracteristicas_formales_y_de_seguridad__cirmo3_8_4_1_7_cffc46
    - Operacion_verificacion_de_causales_de_rechazo_segun_normativa_bcra__snp_cheq_3_3_5_1_325c7f
    - Operacion_verificacion_de_claridad_de_imagen_por_entidad_girada__snp_cheq_3_2_8_4_54bf91
    - Operacion_verificacion_de_cobranzas_y_operaciones_por_cuenta_de_terceros__nmcief_a3_s1_352143
    - Operacion_verificacion_de_coincidencia_de_saldos_consolidados__nmcief_a3_s1_899069
    - Operacion_verificacion_de_conciliaciones_con_bancos_corresponsales__nmcief_a3_s1_3d1210
    - Operacion_verificacion_de_cumplimiento_de_normas_de_auditoria_externa__ri_ccna_d1a1_s8_081e3d
    - Operacion_verificacion_de_datos_del_chc__cirmo3_8_4_1_11_2a3370
    - Operacion_verificacion_de_endosos_en_chc__cirmo3_8_4_1_5_3df482
    - Operacion_verificacion_de_identidad_de_asociaciones_beneficiarias__depaho_3_5_2_9db704
    - Operacion_verificacion_de_identidad_de_titulares__depaho_3_5_2_f0c035
    - Operacion_verificacion_de_identidad_del_titular__depaho_3_11_2_93506f
    - Operacion_verificacion_de_partidas_pendientes_de_imputacion__nmcief_a3_s1_a4f784
    - Operacion_verificacion_de_que_no_es_banco_pantalla__ayccef_5_1_5_946069
    - Operacion_verificacion_de_regularidad_de_endosos__cirmo3_8_4_1_4_664f88
    - Operacion_verificacion_de_validez_de_instruccion__snp_cheq_8_4_4_3_f879ed
    - Operacion_verificacion_del_cumplimiento_de_aspectos_formales__ri_ccna_d1a3l2_s9_cc8905
    - Operacion_verificacion_del_cumplimiento_de_obligaciones_de_informacion__ri_ccna_d2a2_3_1_fd751c
    - Operacion_verificacion_documentacion_respaldo_operaciones__ri_ccna_d1a3l2_s19_0cb2ca
    - Operacion_verificacion_existencia_entidades_depositarias__snp_cheq_5_1_1_801579
    - Operacion_verificacion_existencia_entidades_giradas__snp_cheq_5_1_1_2abe1b
    - Operacion_verificacion_existencia_entidades_originantes__snp_tr_1_5_1_d53a40
    - Operacion_verificacion_existencia_entidades_receptoras__snp_tr_1_5_1_b5d6fb
    - Operacion_verificacion_independiente_de_precios__lingeef_4_3_6_2_de9b3f
    - Operacion_verificacion_presentacion_previa_transferencia_minorista_devoluciones__snp_tr_1__12cbf9
    - Operacion_verificacion_registros_individuales_y_adicionales_del_archivo__snp_cheq_5_1_1_4fde2f
    - Operacion_verificacion_registros_individuales_y_adicionales_por_lote__snp_cheq_5_1_1_d8d027
    - Operacion_verificacion_requisitos_radicacion_asociados__ri_ccna_d1a3l2_26_5_2e9d00
    - Operacion_verificacion_totales_de_control_de_archivo__snp_tr_1_5_1_cf7e47
    - Operacion_verificacion_totales_de_control_de_lote__snp_tr_1_5_1_62f266
    - Operacion_verificacion_totales_de_control_del_archivo__snp_cheq_5_1_1_98a8a5
    - Operacion_verificacion_totales_de_control_por_lote__snp_cheq_5_1_1_b9ab02
    - Operacion_vigilancia_seguridad_privada__ri_mmsef_2_2_10_2_ae6691
    - Operacion_vinculacion_de_agencia_con_varias_entidades_financieras__expaef_9_4_9a1587
    - Operacion_vuelta_atras_de_camara_unwinding_rechazo_por_cec__snp_cheq_7_1_211933
    - Operacion_warrant_como_garantia_preferida__cajasc_5_5_7_575a99
    - Operacion_warrant_sobre_mercaderias_fungibles_cotizadas__cajasc_2_5_4_7_914f1f
Potestad: 251 sin aplica_a
    - Potestad_acreditacion_de_pagos_en_cuentas_especiales_alternativas__facultad_de_acordar_qu_9cfbdd
    - Potestad_acreditacion_de_pagos_en_cuentas_especiales_u_otra_cuenta_a_la_vista__las_entida_7c0cb2
    - Potestad_acreditacion_en_cuentas_especiales_alternativas__las_entidades_podran_acordar_qu_abdf23
    - Potestad_actualizacion_de_formato_y_atributos_de_visibilidad_de_datos_cac__facultad_de_ac_4d1c48
    - Potestad_admision_de_acreditaciones_de_entes_constituidos_en_exterior__se_permite_la_admi_0c8c27
    - Potestad_admision_de_creditos_por_cobro__se_admitiran_creditos_por_cobro_de_depositos_e_i_a1b7ca
    - Potestad_admision_de_multiples_acreditaciones__se_permite_mas_de_una_acreditacion_por_con_2e5b75
    - Potestad_adopcion_de_medidas_articulos_41_y_concordantes_lef__el_bcra_puede_adoptar_las_m_3e76e9
    - Potestad_adopcion_resolucion_sobre_operacion__facultad_de_adoptar_resolucion_sobre_la_cor_d87153
    - Potestad_apertura_cuentas_inversores_extranjeros__los_inversores_extranjeros_a_que_refier_2def17
    - Potestad_aplicacion_de_nuevas_condiciones_tras_plazo_de_30_dias_corridos__las_nuevas_cond_bc810b
    - Potestad_aplicacion_de_nuevas_condiciones_tras_plazo_de_5_dias_notificacion_fehaciente__e_51fb10
    - Potestad_aplicacion_de_regimen_disciplinario_y_tramitacion_de_sumarios__el_bcra_aplicara__4a06a9
    - Potestad_aplicacion_de_sanciones_por_incumplimiento__el_bcra_puede_aplicar_las_sanciones__1e4f55
    - Potestad_aplicacion_opcional_a_procesos_financieros_y_operativos__las_disposiciones_puede_3aabe0
    - Potestad_aplicar_procedimiento_punto_9_5_2_garantia_hipotecaria__las_cajas_de_credito_coo_86d9ab
    - Potestad_asesoramiento_y_servicios_complementarios__se_podra_brindar_asesoramiento_entreg_439034
    - Potestad_auditoria_periodica_de_cumplimiento_de_condiciones__la_sefyc_tiene_la_facultad_d_5146c6
    - Potestad_autorizacion_bcra_administracion_sce__las_infraestructuras_del_mercado_financier_62c1eb
    - Potestad_autorizacion_bcra_gestion_echeq__el_bcra_autoriza_a_las_infraestructuras_de_merc_773c51
    - Potestad_autorizacion_de_credito_y_emision_de_numero_de_transaccion_mep__el_bcra_cumplida_8806f9
    - Potestad_autorizacion_emision_moneda_conmemorativa__el_bcra_en_su_caracter_de_ente_emisor_8453bb
    - Potestad_autorizacion_emision_moneda_conmemorativa__el_bcra_en_su_caracter_de_ente_emisor_ca8e58
    - Potestad_autorizacion_para_participar_en_entidades_del_exterior__el_bcra_otorga_autorizac_ec3916
    - Potestad_basarse_en_debida_diligencia_simplificada_para_apertura_y_mantenimiento__faculta_3a6895
    - Potestad_bcra_requerimiento_de_resultados_de_auditoria_interna__el_bcra_tiene_la_facultad_63952a
    - Potestad_beneficio_de_pruebas_inversas_para_nuevos_productos_y_mercados__el_uso_de_las_pr_4f8948
    - Potestad_cancelacion_anticipada_permitida_a_partir_de_30_dias__se_permite_la_cancelacion__d2b15e
    - Potestad_cancelacion_de_autorizacion_por_incumplimiento__cancelacion_de_la_autorizacion_o_030e79
    - Potestad_canje_de_billetes_deteriorados_accidentalmente__el_bcra_tiene_la_facultad_de_can_ad73ad
    - Potestad_computacion_financiaciones_partida_837000_001__las_financiaciones_a_ser_informad_96b3c1
    - Potestad_comunicar_aceptacion_del_rechazo_fuera_de_canje__la_entidad_depositaria_puede_co_606356
    - Potestad_comunicar_no_aceptacion_del_rechazo_fuera_de_canje__la_entidad_depositaria_puede_3a1ef4
    - Potestad_conformacion_como_persona_unica_area_o_comite_de_riesgos__la_unidad_de_gestion_d_6273d8
    - Potestad_consideracion_de_liquidez_intercambiable_con_puente_directo__cuando_existe_un_pu_2ca83e
    - Potestad_consideracion_de_objeciones_como_causal_de_exclusion__podra_considerarse_como_ca_3d01a0
    - Potestad_consideracion_especial_de_regulaciones_del_pais_de_origen__cuando_el_solicitante_d2e893
    - Potestad_consulta_al_area_de_supervision_criterio_de_imputacion__facultad_del_area_de_sup_a1895d
    - Potestad_control_de_cheque_pendiente_y_validez_de_datos_mep__el_bcra_tiene_la_facultad_de_ca29c9
    - Potestad_coordinacion_de_tarea_con_auditoria_interna_satisfactoria__el_auditor_externo_po_551fa9
    - Potestad_criterios_mas_rigurosos_previsiones_por_incobrabilidad__pueden_adoptar_criterios_fcc8c2
    - Potestad_cumplimiento_alternativo_con_informe_de_auditoria_interna__la_entidad_podra_cump_8eb23b
    - Potestad_cursar_transferencias_en_lote_asignaciones_familiares__se_pueden_cursar_transfer_4abfe1
    - Potestad_cursar_transferencias_en_lote_embargos_sobre_haberes__se_pueden_cursar_transfere_db2204
    - Potestad_cursar_transferencias_en_lote_entre_clientes_o_terceros__se_pueden_cursar_transf_04d018
    - Potestad_cursar_transferencias_en_lote_pago_a_proveedores__se_pueden_cursar_transferencia_9f855f
    - Potestad_cursar_transferencias_en_lote_pago_de_sueldos__se_pueden_cursar_transferencias_e_650fc2
    - Potestad_cursar_transferencias_en_lote_pagos_previsionales__se_pueden_cursar_transferenci_fa0011
    - Potestad_debida_diligencia_simplificada_para_clientes_de_riesgo_bajo__la_apertura_y_el_po_68d4bd
    - Potestad_debito_automatico_por_incumplimiento_de_entrega__el_bcra_tiene_la_facultad_de_ap_6ddf55
    - Potestad_definir_horarios_de_corte_para_compensacion__el_administrador_de_cada_esquema_de_af4224
    - Potestad_dejar_sin_efecto_autorizacion_por_no_uso__las_autorizaciones_otorgadas_quedan_si_86a764
    - Potestad_delegacion_tareas_auditoria_en_profesionales_independientes__la_entidad_podra_de_1aa6bd
    - Potestad_demas_derivados_consulta_a_sefyc__la_sefyc_otorgara_el_tratamiento_singularizado_a88b14
    - Potestad_denegacion_o_disminucion_de_reduccion_de_requerimiento_de_capital__la_sefyc_podr_21f4c9
    - Potestad_denegar_reduccion_de_exigencia_de_capital_titulizacion__la_sefyc_tiene_la_facult_cbcca1
    - Potestad_derecho_del_acreedor_a_proteger_el_inmueble__el_acreedor_o_la_entidad_administra_55238f
    - Potestad_desafectacion_de_reserva_por_asamblea_de_accionistas__la_asamblea_de_accionistas_e38817
    - Potestad_desarrollar_base_de_datos_en_forma_conveniente__la_entidad_financiera_tiene_la_f_0a4374
    - Potestad_designacion_de_cotitular_de_la_cuenta_sueldo__el_trabajador_alcanzado_por_el_art_b1cbbe
    - Potestad_determinacion_de_cantidades_gerencia_de_operaciones_de_emision__la_gerencia_de_o_5918c6
    - Potestad_determinacion_libre_de_tasas_de_interes__las_tasas_de_interes_aplicables_se_dete_3e5504
    - Potestad_determinar_naturaleza_y_alcance_de_procedimientos_sustantivos__el_responsable_de_d44f4a
    - Potestad_devolucion_de_documentacion_por_discrepancias__el_bcra_procedera_a_devolver_a_la_40c290
    - Potestad_devolucion_de_triplicado_como_recibo_provisorio__el_triplicado_sera_devuelto_deb_55832f
    - Potestad_directorio_bcra_resuelve_sobre_apertura_sucursales_exterior__el_directorio_del_b_c1fc4f
    - Potestad_disponibilidad_publica_del_mecanismo_de_consulta__el_mecanismo_de_consulta_estar_ad1df9
    - Potestad_ejercicio_de_facultades_por_cuenta_propia_o_de_futuros_titulares__las_facultades_69c771
    - Potestad_eleccion_de_moneda_para_cheques_cancelatorios__el_solicitante_puede_elegir_entre_eb0d05
    - Potestad_elevacion_de_requisito_de_capital_por_proteccion_inadecuada__la_sefyc_podra_elev_75b02f
    - Potestad_establecer_multas_para_incentivar_adherencia__facultad_del_administrador_de_un_e_b5c8e7
    - Potestad_establecimiento_de_horarios_limite_por_cec__la_cec_tiene_la_facultad_de_definir__a1eaf9
    - Potestad_establecimiento_de_modalidad_de_revision_de_auditoria__la_superintendencia_de_en_45d26d
    - Potestad_evaluacion_de_razonabilidad_del_criterio_de_agregacion__la_sefyc_tiene_la_facult_52fe31
    - Potestad_exclusion_de_auditor_por_cambio_de_circunstancias__el_superintendente_de_entidad_15bdb9
    - Potestad_exclusion_facultativa_de_criterio_general_convenios_de_pago__facultad_de_excluir_56bc1f
    - Potestad_exigencia_de_aumento_del_requerimiento_de_capital__la_sefyc_podra_exigir_un_aume_41fa02
    - Potestad_exigir_adopcion_de_medidas_correctivas_o_capital_adicional__la_superintendencia__07853d
    - Potestad_exigir_capital_regulatorio_superior_a_coeficientes_minimos__la_superintendencia__52b75d
    - Potestad_exigir_capital_sobre_activos_titulizados_con_factor_de_conversion__la_superinten_6b8ef6
    - Potestad_exigir_informacion_sobre_personas_vinculadas__la_sefyc_podra_exigir_si_a_su_juic_deeead
    - Potestad_exigir_tratamiento_de_activos_titulizados_como_si_permanecieran_en_balance__la_s_cd428f
    - Potestad_expedicion_de_la_superintendencia_plazo_30_dias_habiles__la_superintendencia_de__e49903
    - Potestad_expedirse_mediante_resolucion_sobre_modificaciones__el_superintendente_de_entida_15bda5
    - Potestad_extraccion_de_fondos_a_opcion_del_titular__el_titular_de_la_caja_de_ahorros_para_86b1ac
    - Potestad_extracciones_unicamente_por_compras_en_comercios__las_extracciones_de_fondos_de__cc13a2
    - Potestad_facultad_auditor_externo_procedimientos_adicionales__el_auditor_externo_tiene_la_c531d4
    - Potestad_facultad_auditor_realizar_otros_procedimientos_evaluacion_razonabilidad__el_audi_a88947
    - Potestad_facultad_auditoria_interna_aportar_conocimientos_gestion_riesgo__la_auditoria_in_f8e981
    - Potestad_facultad_de_abrir_cuentas_sueldo_a_solicitud_de_trabajadores__las_entidades_fina_0b6ac4
    - Potestad_facultad_de_acordar_pagos_anticipados_parciales__si_el_deudor_acuerda_con_el_acr_ca2601
    - Potestad_facultad_de_aplicar_sanciones_por_incumplimiento__el_bcra_tiene_la_facultad_de_a_9139f7
    - Potestad_facultad_de_compensacion_de_credito_en_mora__en_casos_de_mora_e_incumplimiento_e_aaad62
    - Potestad_facultad_de_compensar_cheques_electronicamente__se_habilita_la_compensacion_elec_fe62cf
    - Potestad_facultad_de_considerar_exclusion_por_calificaciones__el_bcra_podra_considerar_en_6a480a
    - Potestad_facultad_de_debito_automatico_de_importes_adeudados__el_acreedor_queda_facultado_cc703b
    - Potestad_facultad_de_declarar_caducidad_de_plazos__el_acreedor_puede_declarar_la_caducida_18a12e
    - Potestad_facultad_de_descargar_informacion_en_archivos_comprimidos__facultad_de_descargar_fd0d04
    - Potestad_facultad_de_determinar_horario_de_ruedas__la_gerencia_de_operaciones_de_tesoro_t_3ffbe7
    - Potestad_facultad_de_efectuar_debitos_transferencias_a_cuentas_con_seguimiento_arca__la_e_f335e7
    - Potestad_facultad_de_efectuar_debitos_transferencias_a_otras_cuentas_especiales__la_entid_e2c0bc
    - Potestad_facultad_de_encomendar_supervision_a_delegados__el_directorio_puede_encomendar_l_5fe689
    - Potestad_facultad_de_incluir_indicadores_ejemplificativos__los_indicadores_pueden_incluir_1b4282
    - Potestad_facultad_de_iniciar_ejecucion_por_incumplimiento__el_incumplimiento_del_deudor_a_c5a9a9
    - Potestad_facultad_de_la_superintendencia_para_expedirse_sobre_previsiones__la_superintend_2b7d1c
    - Potestad_facultad_de_obtener_cobertura_por_desempleo__las_entidades_financieras_tienen_la_774b58
    - Potestad_facultad_de_ordenar_transferencias_inmediatas_24_7__el_cliente_tiene_la_facultad_c4cf0a
    - Potestad_facultad_de_presentacion_para_gestion_de_cobro__el_legitimo_beneficiario_final_d_40466a
    - Potestad_facultad_de_presentar_billetes_deteriorados_sin_perforar__las_entidades_financie_f239e4
    - Potestad_facultad_de_realizar_consultas_puntuales__el_publico_en_general_esta_facultado_p_54dd79
    - Potestad_facultad_de_realizar_consultas_puntuales__se_habilita_la_realizacion_de_consulta_3ed5cc
    - Potestad_facultad_de_solicitar_documentacion_en_cualquier_momento__la_superintendencia_de_cf8276
    - Potestad_facultad_de_solicitar_venta_judicial_del_inmueble__el_acreedor_puede_solicitar_l_525c29
    - Potestad_facultad_de_vender_moneda_extranjera__el_declarante_tiene_la_facultad_de_vender__422025
    - Potestad_facultad_del_acreedor_cesion_conforme_ley_24_441__el_acreedor_puede_ceder_el_cre_85904d
    - Potestad_facultad_del_acreedor_cesion_del_credito_prendario__el_acreedor_puede_transferir_f90972
    - Potestad_facultad_del_acreedor_compensacion_de_credito_en_mora__el_acreedor_puede_compens_3208b2
    - Potestad_facultad_del_acreedor_continuacion_de_accion_contra_patrimonio__si_el_precio_de__ec479b
    - Potestad_facultad_del_acreedor_contratacion_de_seguro_de_desempleo__el_acreedor_puede_con_98c9fb
    - Potestad_facultad_del_acreedor_contratacion_de_seguro_de_vida__el_acreedor_puede_contrata_97b586
    - Potestad_facultad_del_acreedor_debito_automatico_de_sumas_adeudadas__el_acreedor_puede_de_d788b7
    - Potestad_facultad_del_acreedor_declaracion_de_caducidad_de_plazos__el_acreedor_puede_decl_195200
    - Potestad_facultad_del_acreedor_ejercicio_de_debito_automatico_por_cesionarios__el_acreedo_b5a060
    - Potestad_facultad_del_acreedor_eleccion_de_via_de_ejecucion__el_acreedor_puede_elegir_ent_4ef796
    - Potestad_facultad_del_acreedor_inspeccion_del_bien_prendado__el_acreedor_tiene_facultad_d_a55b1f
    - Potestad_facultad_del_acreedor_opciones_ante_falta_de_pago_de_seguro__el_acreedor_tiene_f_f8fd23
    - Potestad_facultad_del_acreedor_procedimiento_ante_incumplimiento_de_seguro__el_acreedor_p_877c21
    - Potestad_facultad_del_acreedor_reinscripcion_de_prenda__el_acreedor_esta_autorizado_a_rei_6f8426
    - Potestad_facultad_del_acreedor_subsistencia_de_prenda_ante_novacion_interpretada__si_se_i_3df43e
    - Potestad_facultad_del_acreedor_venta_privada_del_bien_prendado__el_acreedor_puede_realiza_8dae05
    - Potestad_facultad_del_bcra_de_efectuar_pagos_con_depositos_de_billetes__el_bcra_tiene_la__6433b4
    - Potestad_facultad_del_deudor_de_requerir_comprobantes_de_titularidad__el_deudor_puede_req_022626
    - Potestad_facultad_del_deudor_pagos_anticipados_parciales__el_deudor_puede_acordar_con_el__6eab85
    - Potestad_facultad_del_deudor_precancelacion_del_credito__el_deudor_tiene_facultad_de_prec_f71118
    - Potestad_facultad_exclusiva_del_bcra_para_emision_de_numerario__facultad_propia_y_exclusi_047511
    - Potestad_facultad_informar_codigo_210200_tp__facultad_de_informar_el_codigo_210200_tp_cua_84dacf
    - Potestad_facultad_sefyc_otorgar_conformidad_cambio_titularidad__la_sefyc_tiene_la_faculta_96c93c
    - Potestad_funcion_de_registro_y_gestion_del_sca__el_sca_tiene_la_funcion_de_registrar_el_i_c06f77
    - Potestad_gerencia_puede_requerir_propuesta_de_solucion__la_gerencia_de_control_de_auditor_cb3344
    - Potestad_gestion_de_rechazados_mediante_ajustes_en_sesion_presentados__la_comunicacion_de_6feb39
    - Potestad_habilitacion_de_plazas_caba_y_sde__se_habilitan_dos_plazas_en_el_sistema_de_decl_7fe166
    - Potestad_habilitacion_transitoria_de_via_de_contingencia_por_e_mail__la_gerencia_de_opera_7dbf64
    - Potestad_homologacion_de_plantillas_de_perforacion__otras_plantillas_de_perforacion_puede_c7599e
    - Potestad_identificacion_del_firmante_por_solicitud_del_tenedor__la_identificacion_del_fir_00d710
    - Potestad_impedir_tratamiento_de_capital_favorable_en_activos_titulizados__la_superintende_0b3bc2
    - Potestad_implementacion_de_pagina_de_internet_para_consulta_centralizada__la_cec_de_bajo__a4d520
    - Potestad_incluir_cap_floor_o_collar_en_tasa_variable__facultad_de_incluir_en_los_prestamo_1981f1
    - Potestad_inclusion_de_cap_floor_o_collar_en_prestamo_variable__facultad_de_incluir_en_un__40c752
    - Potestad_inclusion_de_otros_elementos_en_legajo_a_criterio_de_la_caja__la_caja_de_credito_d26988
    - Potestad_inclusion_documento_acompanante_cac_con_instrucciones__podra_incluirse_un_docume_84afcd
    - Potestad_inclusion_opcional_de_documento_educativo_con_cac__facultad_de_incluir_un_docume_1ed1c4
    - Potestad_incorporacion_de_cotitulares_en_caja_de_ahorros__se_admite_la_incorporacion_de_c_a15add
    - Potestad_indicacion_del_bcra_para_traslado_de_excedentes_a_sus_tesoros__el_bcra_podra_ind_cbfcab
    - Potestad_indicar_otros_motivos_de_rechazo_opcional__el_campo_de_otros_motivos_de_rechazo__43afbf
    - Potestad_indicar_otros_motivos_de_rechazos__se_podran_indicar_otros_motivos_de_rechazos_l_15848d
    - Potestad_informar_cbu_o_alias_en_sca__facultad_de_informar_en_el_sistema_de_circulacion_a_655116
    - Potestad_iniciacion_de_acciones_de_ejecucion_a_partir_de_noventa_dias__el_administrador_p_46caf0
    - Potestad_iniciacion_de_acciones_de_ejecucion_de_garantia__el_administrador_puede_iniciar__73f4c2
    - Potestad_instruccion_de_procedimiento_sumarial_ley_de_entidades_financieras__sin_perjuici_31c8b6
    - Potestad_instrumentacion_mediante_certificado_electronico_cedip__los_depositos_a_plazo_fi_3a9c4e
    - Potestad_libertad_de_convencion_de_interes__las_partes_tienen_la_facultad_de_convenir_lib_63f8e1
    - Potestad_libertad_de_fijacion_de_prima_de_futuro__las_partes_pueden_fijar_libremente_el_m_c05bc3
    - Potestad_libre_acuerdo_entre_cliente_y_entidad_originante_sobre_momento_de_entrega__las_p_ae5d47
    - Potestad_mayor_frecuencia_de_emision_de_informes__el_auditor_podra_realizar_informes_con__6d43de
    - Potestad_modalidad_exclusiva_o_compartida_de_administracion_y_operacion__la_administracio_49d118
    - Potestad_modificacion_de_cbu_de_cobro_a_voluntad_del_titular__el_titular_del_cedip_puede__9a846b
    - Potestad_modificar_alcance_y_naturaleza_de_procedimientos_durante_ejecucion__el_responsab_dd7508
    - Potestad_multiples_acreditaciones_permitidas__se_permite_mas_de_una_acreditacion_por_los__3d3efc
    - Potestad_multiples_acreditaciones_por_concepto__se_admite_mas_de_una_acreditacion_por_los_6b7308
    - Potestad_no_contestar_rechazo_fuera_de_canje__la_entidad_depositaria_puede_optar_por_no_c_4082fb
    - Potestad_no_obligacion_de_reclasificar_por_mayor_cobertura_de_previsiones__la_mayor_cober_d55851
    - Potestad_objecion_a_informes_especiales__las_cajas_de_credito_podran_objetar_los_informes_daf137
    - Potestad_objecion_de_informes_por_deficiencias_significativas__la_superintendencia_de_ent_7368f4
    - Potestad_omision_de_procedimientos_minimos_no_significativos__el_auditor_externo_podra_de_da1376
    - Potestad_opcion_de_admitir_depositos_por_medios_electronicos__la_entidad_financiera_tiene_da1886
    - Potestad_opcion_de_apertura_de_cuenta_adicional_en_pesos__el_cliente_que_pretenda_realiza_624a08
    - Potestad_opcion_de_desafectacion_o_baja_cliente__el_cliente_tiene_la_facultad_de_manifest_ed6fb8
    - Potestad_opcion_de_desafectacion_o_baja_cliente__el_cliente_tiene_la_opcion_de_manifestar_6e995a
    - Potestad_opcion_de_extraccion_mediante_canales_electronicos__el_titular_de_la_caja_de_aho_1c1a89
    - Potestad_opcion_de_extraccion_por_compras_retiros_con_tarjeta_de_debito__el_titular_de_la_c31693
    - Potestad_opcion_de_extraccion_por_transferencia__el_titular_de_la_caja_de_ahorros_para_me_c0d914
    - Potestad_opcion_de_formalizar_adhesion_cliente__el_cliente_tiene_la_facultad_de_formaliza_84efab
    - Potestad_opcion_de_formalizar_adhesion_cliente__el_cliente_tiene_la_opcion_de_formalizar__ec9834
    - Potestad_opcion_de_incluir_todas_o_solo_opciones_de_cobertura__facultad_de_elegir_entre_i_35dbc4
    - Potestad_opcion_de_integracion_en_monedas_extranjeras_distintas_del_usd__las_entidades_pu_66366f
    - Potestad_opcion_de_titular_modalidad_de_extraccion__el_titular_de_la_caja_de_ahorros_para_1e5b61
    - Potestad_opcion_de_usar_calificaciones_para_tasas_activas_y_rentabilidad__las_calificacio_2262d0
    - Potestad_opcion_de_via_de_ejecucion_judicial_o_especial__el_acreedor_puede_optar_a_su_exc_786b2b
    - Potestad_opcion_realizar_control_conjuntamente_con_auditoria_interna__el_sistema_de_contr_0155be
    - Potestad_optar_por_requerir_tasacion__la_entidad_financiera_puede_optar_por_requerir_una__13781a
    - Potestad_pactar_formas_de_retribucion_adicionales__las_entidades_podran_pactar_otras_form_7b87ab
    - Potestad_pactar_libremente_plazo_pase_pasivo_con_entidades_financieras__las_partes_pueden_2c3366
    - Potestad_pactar_otras_formas_de_retribucion__las_entidades_podran_pactar_otras_formas_de__2b01c8
    - Potestad_pacto_libre_del_plazo__las_partes_pueden_pactar_libremente_el_plazo_del_pase_act_b49408
    - Potestad_pacto_libre_del_plazo_entre_partes__las_partes_tienen_la_facultad_de_pactar_libr_c06e06
    - Potestad_permiso_de_multiples_acreditaciones__se_permite_mas_de_una_acreditacion_en_la_cu_628881
    - Potestad_permitir_consulta_de_informacion_mediante_home_banking_o_mobile_banking__permiti_d9311c
    - Potestad_poder_especial_irrevocable_reinscripcion_de_prenda__el_deudor_confiere_poder_esp_594f78
    - Potestad_potestad_de_aplicar_sanciones_por_incumplimiento__la_falta_de_presentacion_en_te_271a97
    - Potestad_precancelacion_en_cualquier_momento__facultad_de_precancelar_en_cualquier_moment_bc7970
    - Potestad_precancelacion_parcial_con_combinacion_de_modalidades__facultad_de_aplicar_la_pr_b8254b
    - Potestad_precancelacion_parcial_con_reduccion_de_cuota__facultad_de_aplicar_la_precancela_be7716
    - Potestad_precancelacion_parcial_con_reduccion_de_plazo__facultad_de_aplicar_la_precancela_5cfec5
    - Potestad_presuncion_de_conformidad_con_movimiento__se_presume_conformidad_de_la_administr_b036a3
    - Potestad_rechazar_fuera_de_canje_por_cheque_no_presentado__la_entidad_depositaria_puede_r_0a5e75
    - Potestad_reclasificacion_a_nivel_superior_15_cancelado__facultad_de_reclasificar_en_el_ni_6e728e
    - Potestad_reclasificacion_a_nivel_superior_3_cuotas_consecutivas__facultad_de_reclasificar_58e23e
    - Potestad_reconocimiento_de_intereses_sobre_saldos__se_podra_reconocer_el_pago_de_interese_83db6b
    - Potestad_reduccion_de_cargos_en_casos_excepcionales__los_cargos_podran_ser_reducidos_en_c_b20691
    - Potestad_reeleccion_posterior_con_intervalo__los_miembros_pueden_ser_elegidos_nuevamente__6b38a1
    - Potestad_renovacion_de_mandatos_por_un_solo_periodo_consecutivo__los_mandatos_de_los_miem_a89b46
    - Potestad_requerimiento_bcra_procedimientos_verificacion_especificos__el_bcra_puede_requer_e3b662
    - Potestad_requerimiento_de_papeles_de_trabajo_por_sefyc__la_superintendencia_de_entidades__700b54
    - Potestad_requerimiento_papeles_de_trabajo_auditoria_interna__la_superintendencia_podra_re_e84755
    - Potestad_requerir_capital_adicional_titulizacion_insuficiente__la_sefyc_tiene_la_facultad_69ef9d
    - Potestad_reserva_de_subsistencia_de_garantia_hipotecaria__el_acreedor_formula_la_reserva__ef3122
    - Potestad_resolucion_en_unica_instancia_de_dudas_sobre_billetes_deteriorados__el_bcra_tien_16362a
    - Potestad_resolucion_sobre_condicion_de_billetes__el_bcra_tiene_la_facultad_de_resolver_so_06b793
    - Potestad_resolver_no_aplicacion_del_tratamiento_de_titulizaciones__hasta_tanto_llegue_a_u_d4c4b9
    - Potestad_responsabilidad_del_acreedor_por_omisiones_en_administracion__el_acreedor_es_res_1a4548
    - Potestad_responsabilidad_final_del_directorio_sobre_medicion__el_directorio_asume_la_resp_f38d39
    - Potestad_retencion_de_copia_original_de_solicitud__el_acreedor_tiene_la_facultad_de_reten_fbff9f
    - Potestad_sefyc_adoptar_medidas_ante_politicas_inadecuadas__la_sefyc_tiene_facultad_de_ado_36cdc9
    - Potestad_solicitar_bloqueo_de_factura_impaga__la_empresa_deudora_puede_solicitar_el_bloqu_506c6e
    - Potestad_solicitar_detalle_de_fcem__el_obligado_al_pago_tiene_la_facultad_de_solicitar_el_038c92
    - Potestad_solicitar_documentacion_en_cualquier_momento__la_superintendencia_de_entidades_f_0b5320
    - Potestad_solicitar_saldo_y_detalle_de_depositos__el_trabajador_y_el_empleador_tienen_la_f_21541e
    - Potestad_solicitud_de_cac_tenedor_legitimado_y_titular_de_echeq_caducado__el_tenedor_legi_0ebb4c
    - Potestad_solicitud_de_presentacion_del_deudor_en_oficinas__el_administrador_puede_solicit_afd929
    - Potestad_solicitud_de_presentacion_en_oficinas_del_administrador__el_administrador_puede__db10bc
    - Potestad_solicitud_de_resumen_en_sucursal__el_titular_y_o_apoderado_o_representante_legal_e380fc
    - Potestad_suministro_de_datos_a_empresas_de_informacion_crediticia__si_las_cuotas_del_pres_717a05
    - Potestad_suministro_de_informacion_a_empresas_de_informacion_crediticia__si_las_cuotas_de_fb5128
    - Potestad_tasa_contractualmente_convenida__la_tasa_de_interes_sera_la_que_contractualmente_3d1421
    - Potestad_tomar_medidas_para_ajustar_exigencia_de_capital_minimo__la_superintendencia_de_e_622b32
    - Potestad_transferencia_de_fondos_a_otra_entidad_financiera__se_permite_la_transferencia_d_a86675
    - Potestad_transferencia_de_superavit_de_revaluacion_a_resultados_no_asignados__el_superavi_3b2c42
    - Potestad_transferencia_de_titularidad_y_administracion_del_prestamo__el_acreedor_podra_tr_e2068e
    - Potestad_transferencia_de_titularidad_y_administracion_del_prestamo__el_acreedor_tiene_la_fdaa2b
    - Potestad_transferencia_parcial_de_superavit_a_medida_que_el_activo_es_utilizado__puede_tr_2bf387
    - Potestad_tratamiento_como_sistemas_auxiliares_sin_puente_directo__los_sistemas_de_pagos_d_f4d0fb
    - Potestad_uso_de_medios_alternativos_deposito_por_ventanilla__las_entidades_podran_emplear_b5e426
    - Potestad_uso_de_medios_alternativos_extraccion_de_fondos__las_entidades_podran_emplear_ot_a328d9
    - Potestad_utilizacion_de_fondos_capitulo_i_flexibilidad_de_aplicaciones__facultad_de_utili_b82c21
    - Potestad_verificacion_de_legitimidad_e_integracion_de_chc__el_bcra_tiene_la_facultad_de_v_3f0bba
    - Potestad_verificacion_periodica_cumplimiento_controles_internos__la_superintendencia_de_e_a363ca
    - Potestad_verificacion_periodica_de_cumplimiento_por_sefyc__la_superintendencia_de_entidad_d06de1
    - Potestad_verificacion_y_reverificacion_de_datos_por_acreedor__el_acreedor_sus_agentes_suc_bdd188
    - Potestad_verificacion_y_reverificacion_de_datos_por_el_acreedor__el_acreedor_sus_agentes__d179e2
    - Potestad_verificar_respaldo_crediticio_implicito__la_superintendencia_de_entidades_financ_c16275
    - Potestad_vinculacion_de_cuenta_con_tarjeta_de_debito_u_otros_medios_de_pago__a_solicitud__b41f11
Restriccion: 564 sin aplica_a
    - Restriccion_al_aplicar_la_reexpresion_de_activos_no_monetarios_el_importe_resultante_no_debe_da7233
    - Restriccion_al_discontinuar_su_tarea_por_cumplirse_el_plazo_maximo_o_un_termino_inferior_deb_650113
    - Restriccion_al_menos_el_50_del_monto_de_las_financiaciones_debe_destinarse_a_lineas_de_capit_f1bf8e
    - Restriccion_apoyo_crediticio_que_no_supere_el_50_del_valor_de_tasacion_de_los_bienes__cajasc_487e0d
    - Restriccion_apoyo_crediticio_que_no_supere_el_75_del_valor_de_tasacion_de_los_bienes__cajasc_32894b
    - Restriccion_cada_agujero_de_perforacion_debe_poseer_no_menos_de_0_85_cm_de_diametro__cirmo3__2ebc90
    - Restriccion_capital_inicial_minimo_exigido_para_cajas_de_credito_cooperativas_clasificadas_e_01b8f6
    - Restriccion_capital_inicial_minimo_exigido_para_cajas_de_credito_cooperativas_clasificadas_e_15d70e
    - Restriccion_capital_inicial_minimo_exigido_para_cajas_de_credito_cooperativas_clasificadas_e_50cffd
    - Restriccion_capital_inicial_minimo_exigido_para_cajas_de_credito_cooperativas_clasificadas_e_7a1d5c
    - Restriccion_correspondera_la_exclusion_de_la_asociacion_constituida_en_fiadora_solidaria_cua_765445
    - Restriccion_cuando_el_feriado_local_imprevisto_no_sea_conocido_con_antelacion_suficiente_o_n_472a2d
    - Restriccion_cuando_el_pack_resulta_de_un_proceso_automatico_los_millares_y_el_pack_deben_est_f41358
    - Restriccion_cuando_el_primer_beneficiario_presenta_al_cobro_debe_existir_unicamente_el_endos_eb7e4e
    - Restriccion_cuando_el_segundo_beneficiario_presenta_al_cobro_deben_existir_tanto_el_endoso_d_cfa92b
    - Restriccion_cuando_existe_un_endoso_o_cesion_pendiente_de_ser_aceptado_al_momento_de_caducid_0af389
    - Restriccion_cuando_la_funcion_sea_colegiada_la_comision_fiscalizadora_debe_estar_integrada_p_105242
    - Restriccion_cuando_la_refinanciacion_haya_sido_otorgada_encontrandose_el_deudor_clasificado__a9ff9b
    - Restriccion_cuando_la_suma_algebraica_sea_positiva_disminucion_de_exigencia_el_importe_a_com_85d3a9
    - Restriccion_cuando_la_suma_total_de_creditos_del_lote_supere_la_cantidad_de_caracteres_dispo_9b7979
    - Restriccion_cuando_la_suma_total_de_debitos_del_lote_supere_la_cantidad_de_caracteres_dispon_d01b3e
    - Restriccion_cuando_se_aplique_el_procedimiento_del_punto_9_5_2_a_financiaciones_con_garantia_5072e7
    - Restriccion_cuando_se_financien_vehiculos_utilitarios_rodados_y_aeronaves_solo_podran_ser_de_c72116
    - Restriccion_cuando_se_trate_de_tenencias_en_el_exterior_las_acreditaciones_deberan_provenir__9d8a36
    - Restriccion_cuando_se_verifiquen_atrasos_mayores_a_62_dias_en_el_pago_de_los_servicios_de_la_057931
    - Restriccion_de_los_miembros_de_la_comision_fiscalizadora_al_menos_dos_deben_estar_graduados__1f302b
    - Restriccion_debe_verificarse_la_cantidad_de_lotes_del_archivo__snp_tr_1_5_2_1_9d9695
    - Restriccion_debe_verificarse_la_coincidencia_de_los_datos_entre_la_transaccion_original_y_su_11f4bd
    - Restriccion_debe_verificarse_la_integracion_de_los_campos_de_inclusion_mandatoria__snp_tr_1__7feecf
    - Restriccion_debe_verificarse_la_validez_de_las_causales_de_devoluciones_o_rechazos__snp_tr_1_3a941b
    - Restriccion_debe_verificarse_la_validez_de_los_plazos_de_devoluciones_o_rechazos__snp_tr_1_5_ff5319
    - Restriccion_debe_verificarse_los_totales_de_control_de_cada_lote__snp_tr_1_5_2_1_a47d5d
    - Restriccion_debe_verificarse_los_totales_de_control_del_archivo__snp_tr_1_5_2_1_539219
    - Restriccion_deben_adicionarse_dos_etiquetas_iguales_indicando_la_procedencia_una_interna_sob_12ddc1
    - Restriccion_durante_el_intervalo_de_un_periodo_entre_la_finalizacion_de_la_renovacion_consec_2df729
    - Restriccion_durante_el_periodo_de_indisponibilidad_no_se_admitiran_debitos_diferentes_de_los_6edb70
    - Restriccion_el_acreedor_puede_exigir_compensacion_por_precancelacion_anticipada_si_se_realiz_cd63bf
    - Restriccion_el_acreedor_tiene_derecho_a_exigir_una_compensacion_por_cancelacion_anticipada_s_26a325
    - Restriccion_el_anverso_debe_incluir_microletra_dispuesta_en_renglones_y_en_guardas_verticale_ed0a48
    - Restriccion_el_anverso_debe_incluir_un_motivo_de_registro_perfecto__cirmo3_8_1_2_2_426dbb
    - Restriccion_el_anverso_debe_incluir_una_roseta_con_reaccion_al_fotocopiado_y_fluorescencia_a_d53483
    - Restriccion_el_archivo_solo_incluira_deudores_de_entidades_activas_y_registros_de_deudores_e_d46346
    - Restriccion_el_area_de_auditoria_interna_no_sera_responsable_de_la_gestion_del_riesgo_operac_d97e9f
    - Restriccion_el_arrendamiento_financiero_debe_ser_de_nuevas_financiaciones_de_hasta_200_000___a706de
    - Restriccion_el_arrendamiento_financiero_debe_ser_una_nueva_financiacion_con_monto_mayor_a_20_fe42a6
    - Restriccion_el_auditor_externo_no_debe_desempenarse_en_relacion_de_dependencia_en_la_caja_de_297290
    - Restriccion_el_auditor_externo_sera_excluido_del_registro_de_auditores_cuando_las_sanciones__34deaa
    - Restriccion_el_auditor_interino_no_puede_ejercer_el_cargo_de_auditor_externo_en_otra_entidad_8cbcb5
    - Restriccion_el_auditor_no_puede_ejercer_su_funcion_en_la_misma_entidad_por_mas_de_cinco_ejer_205624
    - Restriccion_el_cambio_de_domicilio_de_la_sucursal_solo_podra_realizarse_dentro_de_los_limite_ab5458
    - Restriccion_el_campo_8_hora_de_presentacion_es_opcional_o_mientras_que_los_demas_campos_de_l_854ce4
    - Restriccion_el_capital_adeudado_en_prestamos_hipotecarios_para_vivienda_no_podra_superar_150_3f1c7b
    - Restriccion_el_capital_adeudado_en_prestamos_personales_y_financiaciones_mediante_tarjetas_d_5dfc40
    - Restriccion_el_capital_adeudado_en_prestamos_prendarios_para_automotores_no_podra_superar_30_969fa5
    - Restriccion_el_cheque_cancelatorio_en_dolares_estadounidenses_solo_puede_utilizarse_para_la__1a61a2
    - Restriccion_el_ciclo_de_registracion_de_los_cheques_de_pago_diferido_no_estara_contemplado_e_359f76
    - Restriccion_el_cobro_de_comisiones_esta_limitado_al_saldo_disponible_en_la_cuenta_no_se_pued_ea64fa
    - Restriccion_el_cobro_de_diferencias_por_la_entidad_girada_se_admite_solo_en_documentos_compe_187104
    - Restriccion_el_codigo_210100_tp_no_podra_superar_la_posicion_tpnyrm_tp_cuando_tp_identifica__da9d78
    - Restriccion_el_codigo_210200_tp_no_podra_superar_la_posicion_tpnyrm_tp_cuando_tp_identifica__fa5460
    - Restriccion_el_codigo_81900x_010_se_detraera_de_la_base_de_calculo_del_aporte_al_fondo_de_ga_0c28f4
    - Restriccion_el_conjunto_de_facturas_cedidas_debe_representar_una_cantidad_no_inferior_a_1_00_dcb610
    - Restriccion_el_conjunto_de_los_creditos_de_monto_reducido_no_podra_superar_una_vez_la_respon_506643
    - Restriccion_el_consejo_de_administracion_debe_tener_como_minimo_5_miembros_y_maximo_9__cajas_9d69d0
    - Restriccion_el_cotitular_solo_puede_realizar_los_movimientos_de_fondos_que_se_encuentren_adm_5f90c4
    - Restriccion_el_desembolso_debe_ser_de_hasta_300_000__cajasc_5_5_10_2_1243ea
    - Restriccion_el_desembolso_debe_ser_mayor_de_200_000__cajasc_5_5_10_2_90de31
    - Restriccion_el_deudor_clasificado_en_riesgo_medio_que_haya_refinanciado_su_deuda_y_recibido__85cdb5
    - Restriccion_el_deudor_debe_abonar_los_cargos_de_seguro_dentro_de_diez_dias_de_requerido__man_e10b12
    - Restriccion_el_deudor_solo_puede_aceptar_la_indemnizacion_ofrecida_por_la_autoridad_que_disp_815749
    - Restriccion_el_diferimiento_de_transferencias_ordenadas_antes_de_las_13_horas_no_podra_exced_9d1389
    - Restriccion_el_diferimiento_de_transferencias_ordenadas_despues_de_las_13_horas_no_podra_exc_4279b0
    - Restriccion_el_envio_de_imagen_del_cheque_rechazado_puede_ser_anulado_cuando_la_entidad_depo_3374ee
    - Restriccion_el_importe_consignado_en_codigo_210200_tp_no_puede_superar_el_importe_de_las_exi_54b7dd
    - Restriccion_el_importe_de_intereses_reconocidos_en_moneda_extranjera_no_podra_superar_el_may_603021
    - Restriccion_el_importe_de_intereses_reconocidos_no_podra_superar_el_mayor_entre_dos_exigenci_ceedf5
    - Restriccion_el_importe_del_codigo_210100_tp_no_podra_superar_la_exigencia_determinada_expres_1d6735
    - Restriccion_el_importe_del_codigo_210200_tp_no_podra_superar_la_exigencia_determinada_expres_ffe923
    - Restriccion_el_importe_maximo_a_integrar_por_codigo_210104_tp_se_calcula_como_el_45_del_codi_93d69d
    - Restriccion_el_importe_remanente_del_codigo_210100_tp_que_exceda_la_suma_de_codigos_210104_t_3a9c22
    - Restriccion_el_importe_total_consolidado_que_registre_cada_titular_no_podra_exceder_a_partir_7b1003
    - Restriccion_el_importe_total_de_las_financiaciones_dirigidas_a_clientes_radicados_o_que_real_5da945
    - Restriccion_el_incumplimiento_de_los_requisitos_de_habilitacion_puede_ser_considerado_causal_b329c5
    - Restriccion_el_informe_especial_no_debera_contener_limitaciones_en_el_alcance_de_las_tareas__c9a0d1
    - Restriccion_el_margen_de_cobertura_de_la_garantia_preferida_es_del_90_del_valor_del_bien__ca_6eb3d6
    - Restriccion_el_margen_de_cobertura_de_una_operacion_en_pesos_con_efectivo_en_moneda_extranje_0f06a0
    - Restriccion_el_margen_de_cobertura_del_100_aplica_solo_cuando_los_desembolsos_sean_de_hasta__7b2f64
    - Restriccion_el_margen_de_cobertura_del_100_no_aplica_a_refinanciaciones__cajasc_5_5_10_1_d1118f
    - Restriccion_el_margen_de_cobertura_es_del_90_del_valor_de_tasacion_del_bien__cajasc_5_5_10_2_240cae
    - Restriccion_el_margen_de_cobertura_para_creditos_por_arrendamientos_financieros_de_inmuebles_53da8b
    - Restriccion_el_margen_de_cobertura_para_creditos_por_arrendamientos_financieros_de_maquinas__0e0862
    - Restriccion_el_margen_de_cobertura_para_creditos_por_arrendamientos_financieros_de_vehiculos_db6649
    - Restriccion_el_margen_de_cobertura_para_cupones_de_tarjetas_de_credito_emitidos_por_empresas_c38cf2
    - Restriccion_el_margen_de_cobertura_para_el_arrendamiento_financiero_de_inmuebles_para_vivien_61a7f9
    - Restriccion_el_margen_de_cobertura_para_facturas_a_consumidores_por_servicios_ya_prestados_e_a1a63b
    - Restriccion_el_margen_de_cobertura_para_hipoteca_en_primer_grado_sobre_inmuebles_para_usos_d_e492d5
    - Restriccion_el_margen_de_cobertura_para_operaciones_cubiertas_con_garantias_preferidas_a_con_54b27b
    - Restriccion_el_margen_de_cobertura_para_otros_inmuebles_en_operaciones_de_credito_por_arrend_ce8c6e
    - Restriccion_el_margen_de_cobertura_para_titulos_de_credito_correspondientes_a_sujetos_obliga_106190
    - Restriccion_el_margen_de_cobertura_para_titulos_valores_privados_no_podra_exceder_el_70_de_s_09265e
    - Restriccion_el_margen_de_cobertura_para_warrants_se_computa_al_80_del_valor_de_mercado_de_lo_78e59e
    - Restriccion_el_monto_cubierto_debe_ser_igual_al_saldo_impago_en_todo_momento_del_prestamo_pr_55d4e5
    - Restriccion_el_monto_cubierto_por_el_seguro_debe_ser_igual_al_saldo_impago_en_todo_momento_d_39813b
    - Restriccion_el_monto_de_intereses_reconocidos_no_podra_superar_el_mayor_de_los_importes_que__5c80c3
    - Restriccion_el_monto_de_intereses_reconocidos_no_podra_superar_el_mayor_de_los_importes_que__d4172e
    - Restriccion_el_monto_de_la_financiacion_no_podra_ascender_mas_de_6_000_por_cliente__cajasc_4_fc8d82
    - Restriccion_el_otorgamiento_de_nuevas_refinanciaciones_dentro_de_los_doce_meses_de_acordada__74e851
    - Restriccion_el_pack_contendra_cobertura_de_pelicula_plastica_termocontraible_transparente_co_1f5557
    - Restriccion_el_pack_debe_ser_armado_con_billetes_encarados_hacia_el_frente_en_dos_bloques_de_1243f9
    - Restriccion_el_pin_seleccionado_por_el_usuario_no_debera_ser_su_direccion_personal_su_fecha__52b5a3
    - Restriccion_el_plazo_computable_de_la_caucion_de_certificados_de_deposito_a_plazo_fijo_no_de_06e23f
    - Restriccion_el_plazo_de_la_caucion_tomadora_o_pasiva_en_pesos_pactada_con_otras_contrapartes_c848ed
    - Restriccion_el_plazo_de_los_prestamos_hipotecarios_no_podra_exceder_100_anos__manori_1_1_5_3_7dac88
    - Restriccion_el_plazo_de_los_prestamos_prendarios_sobre_automotores_no_podra_exceder_5_anos___33af2c
    - Restriccion_el_plazo_de_seis_periodos_se_cuenta_alternativamente_desde_la_primera_posicion_i_ff593a
    - Restriccion_el_plazo_maximo_para_efectuar_la_devolucion_a_traves_de_la_cec_de_una_transferen_635565
    - Restriccion_el_plazo_maximo_para_la_realizacion_de_los_procedimientos_previstos_en_la_propue_a476be
    - Restriccion_el_plazo_maximo_para_los_prestamos_transitorios_acordados_para_ser_acreditados_e_d4e76e
    - Restriccion_el_plazo_minimo_de_la_operacion_de_pase_pasivo_con_otras_contrapartes_es_de_30_d_f5f4a4
    - Restriccion_el_plazo_minimo_para_la_realizacion_de_cauciones_bursatiles_es_de_30_dias__opefc_498ddf
    - Restriccion_el_plazo_para_efectuar_la_devolucion_o_rechazo_de_una_transferencia_es_de_24_hor_0e4059
    - Restriccion_el_plazo_para_formular_objecion_o_reclamar_la_entrega_del_resumen_no_puede_ser_i_7d5ed6
    - Restriccion_el_plazo_para_la_realizacion_de_un_reclamo_a_traves_de_este_circuito_sera_de_un__322130
    - Restriccion_el_ponderador_de_riesgo_para_demas_financiaciones_incluidos_titulos_publicos_nac_846cd2
    - Restriccion_el_ponderador_de_riesgo_para_financiaciones_cubiertas_con_garantias_preferidas_a_371440
    - Restriccion_el_ponderador_de_riesgo_para_financiaciones_cubiertas_con_garantias_preferidas_a_398b88
    - Restriccion_el_ponderador_de_riesgo_para_financiaciones_cubiertas_con_garantias_preferidas_a_cc3c0b
    - Restriccion_el_proyecto_de_estatuto_debe_ajustarse_a_la_ley_de_cooperativas_a_la_ley_de_enti_c2dba0
    - Restriccion_el_registro_cabecera_de_lote_y_control_fin_de_lote_no_se_incluyen_en_la_suma_de__bdce39
    - Restriccion_el_resultado_por_reconocimiento_inicial_aplica_a_criterios_de_medicion_de_costo__83f8b6
    - Restriccion_el_saldo_del_codigo_210105_tp_no_podra_exceder_el_saldo_del_codigo_824000_001__r_18f09f
    - Restriccion_el_seguro_debe_cubrir_a_la_propiedad_durante_toda_la_vigencia_del_prestamo_hipot_e2b50b
    - Restriccion_el_seguro_debe_cubrir_a_los_solicitantes_por_el_saldo_de_deuda_del_prestamo_hipo_8ec778
    - Restriccion_el_seguro_debe_cubrir_al_automotor_durante_la_totalidad_de_la_vigencia_del_prest_694c7a
    - Restriccion_el_seguro_debe_estar_emitido_por_companias_de_seguros_locales_que_cumplan_con_lo_1a4d81
    - Restriccion_el_seguro_debe_ser_emitido_por_companias_de_seguros_locales_que_cumplan_con_lo_p_fc854f
    - Restriccion_el_seguro_puede_estar_emitido_por_subsidiarias_locales_de_companias_aseguradoras_ce6336
    - Restriccion_el_seguro_puede_estar_emitido_por_sucursales_locales_de_companias_aseguradoras_d_ec81fc
    - Restriccion_el_seguro_puede_ser_emitido_por_companias_de_seguros_locales_que_cumplan_con_lo__064309
    - Restriccion_el_seguro_puede_ser_emitido_por_subsidiarias_locales_de_companias_aseguradoras_d_51c7b8
    - Restriccion_el_seguro_puede_ser_emitido_por_subsidiarias_locales_de_companias_aseguradoras_d_69c8b5
    - Restriccion_el_seguro_puede_ser_emitido_por_sucursales_locales_de_companias_aseguradoras_del_1a3518
    - Restriccion_el_seguro_puede_ser_emitido_por_sucursales_locales_de_companias_aseguradoras_del_4a54ce
    - Restriccion_el_sindico_debe_cumplir_con_la_calificacion_de_estar_graduado_en_ciencias_econom_02911b
    - Restriccion_el_sistema_de_packs_se_utiliza_solo_en_caba_para_depositos_declarados_en_cib_o_d_13c107
    - Restriccion_el_sistema_informatico_debe_contar_con_niveles_adecuados_de_seguridad__depaho_3__c0656a
    - Restriccion_el_socio_responsable_puede_ser_excluido_del_registro_de_auditores_como_consecuen_83a9f7
    - Restriccion_el_tambor_es_la_unidad_menor_de_medida_para_la_provision_de_monedas__cirmo3_5_4__3feb78
    - Restriccion_el_total_de_operaciones_con_clientes_vinculados_no_podra_exceder_el_20_conforme__63d644
    - Restriccion_el_total_de_titulos_publicos_nacionales_en_pesos_que_tengan_cotizacion_normal_y__100d3c
    - Restriccion_el_traslado_de_la_exigencia_no_integrada_no_podra_exceder_seis_periodos_contados_05857d
    - Restriccion_el_valor_de_mercado_de_los_titulos_valores_debe_responder_a_una_cotizacion_norma_07e3f0
    - Restriccion_en_caso_de_detectarse_faltante_en_la_verificacion_de_billetes_deteriorados_ya_in_999d7a
    - Restriccion_en_caso_de_refinanciacion_el_monto_maximo_del_prestamo_sera_el_saldo_de_capital__4d5a7b
    - Restriccion_en_caso_de_refinanciacion_el_monto_maximo_sera_el_saldo_de_capital_del_prestamo__ca42ad
    - Restriccion_en_caso_de_siniestro_la_indemnizacion_debe_ser_cancelatoria_del_prestamo_si_la_d_c92933
    - Restriccion_en_la_gestion_de_riesgos_debe_considerarse_la_totalidad_de_las_posiciones_de_tit_db4ac4
    - Restriccion_en_la_valuacion_de_inmuebles_con_espacio_comercial_y_o_profesional_no_se_debe_co_23f6be
    - Restriccion_en_las_agencias_regionales_el_sistema_de_recepcion_para_depositos_de_billetes_en_53f3a8
    - Restriccion_en_ningun_dia_del_periodo_la_suma_de_los_saldos_de_los_conceptos_admitidos_como__dc136d
    - Restriccion_exigencia_basica_de_capital_minimo_para_cajas_de_credito_cooperativas_clasificad_037679
    - Restriccion_exigencia_basica_de_capital_minimo_para_cajas_de_credito_cooperativas_clasificad_3a4826
    - Restriccion_exigencia_basica_de_capital_minimo_para_cajas_de_credito_cooperativas_clasificad_867397
    - Restriccion_exigencia_basica_de_capital_minimo_para_cajas_de_credito_cooperativas_clasificad_d317e3
    - Restriccion_exigencia_de_efectivo_minimo_en_moneda_extranjera_para_depositos_en_cuenta_corri_7d3b84
    - Restriccion_habiendo_mediado_la_notificacion_el_deudor_no_puede_oponer_excepcion_de_pago_doc_110bf0
    - Restriccion_importe_que_supera_el_50_del_valor_de_tasacion_de_los_bienes__cajasc_2_5_4_4_d077d7
    - Restriccion_importe_que_supera_el_75_del_valor_de_tasacion_de_los_bienes__cajasc_2_5_4_4_5cf2f4
    - Restriccion_la_actualizacion_de_tasacion_aplica_unicamente_para_los_creditos_que_se_mantenga_3f49bc
    - Restriccion_la_agencia_complementaria_de_servicios_financieros_no_debe_tener_acceso_a_los_mo_4125ce
    - Restriccion_la_ampliacion_del_limite_no_podra_exceder_el_menor_de_los_montos_que_se_especifi_e80698
    - Restriccion_la_base_para_la_venta_es_el_importe_de_capital_adeudado_mas_un_treinta_por_cient_8ad9d1
    - Restriccion_la_cac_debe_emitirse_en_soporte_papel_sin_medidas_de_seguridad_especiales__snp_c_ed9b71
    - Restriccion_la_caducidad_del_plan_de_facilidades_de_pago_cualquiera_sea_el_motivo_que_la_ori_5515be
    - Restriccion_la_caja_de_ahorros_se_mantiene_en_la_moneda_extranjera_en_la_que_se_efectivice_l_864089
    - Restriccion_la_cantidad_de_monedas_de_cuproniquel_cu75_ni25_en_calidad_de_circulacion_acunad_144d86
    - Restriccion_la_cantidad_de_monedas_de_oro_au900_cu100_en_calidad_proof_acunadas_es_de_2_000__7bb4b5
    - Restriccion_la_cantidad_de_monedas_de_plata_ag900_en_calidad_proof_acunadas_es_de_5_000_piez_85a554
    - Restriccion_la_capacidad_del_banco_de_gestionar_eficazmente_sus_riesgos_no_debe_verse_afecta_fa8e38
    - Restriccion_la_captacion_de_imposiciones_con_fondos_del_exterior_queda_sujeta_a_la_normativa_36f7ae
    - Restriccion_la_comunicacion_de_datos_de_identidad_nacionalidad_y_domicilio_de_suscriptores_o_4f007c
    - Restriccion_la_cuenta_450009_resultados_del_ejercicio_se_utilizara_exclusivamente_para_cance_8d86af
    - Restriccion_la_cuenta_de_acreditacion_debe_estar_expresada_en_la_misma_moneda_en_que_fue_con_b59d56
    - Restriccion_la_cuenta_de_ahorro_abierta_por_asociaciones_beneficiarias_se_utilizara_exclusiv_0ed382
    - Restriccion_la_cuenta_de_la_seguridad_social_debe_estar_nominada_en_pesos__depaho_2_2_2_a7080f
    - Restriccion_la_cuenta_gratuita_universal_funciona_unicamente_en_pesos__depaho_3_11_15_59e71d
    - Restriccion_la_cuenta_gratuita_universal_no_tiene_costos_de_apertura_mantenimiento_movimient_e6d85d
    - Restriccion_la_cuenta_no_podra_tener_mas_de_un_menor_autorizado__depaho_3_7_1_bacebe
    - Restriccion_la_deduccion_no_podra_superar_el_4_de_los_conceptos_en_pesos_sujetos_a_exigencia_981404
    - Restriccion_la_deduccion_por_financiaciones_a_mipyme_no_podra_superar_el_2_de_los_conceptos__409c61
    - Restriccion_la_devolucion_debe_realizarse_dentro_de_24_horas_a_partir_de_la_recepcion_de_la__f15060
    - Restriccion_la_difusion_en_consultas_puntuales_se_limita_a_entidad_mes_ano_situacion_monto_i_011b4d
    - Restriccion_la_difusion_en_la_modalidad_de_consultas_puntuales_se_limita_a_los_siguientes_da_741cda
    - Restriccion_la_disminucion_de_exigencia_de_em_en_pesos_codigo_707000_001_no_podra_superar_el_eef4d8
    - Restriccion_la_disminucion_de_exigencia_de_em_por_financiaciones_a_personas_humanas_y_mipyme_006883
    - Restriccion_la_disminucion_de_exigencia_de_em_por_financiaciones_a_personas_humanas_y_mipyme_349397
    - Restriccion_la_duracion_de_la_cuenta_corriente_especial_electoral_no_podra_exceder_los_30_di_33cd6a
    - Restriccion_la_entidad_financiera_no_podra_ceder_el_contrato_de_delegacion_de_actividades_ni_fe8360
    - Restriccion_la_entidad_girada_debe_impedir_que_sus_clientes_creen_echeqs_y_documentos_compen_fc341b
    - Restriccion_la_etiqueta_identificadora_en_el_pack_con_codigo_de_barra_debe_tener_dimension_m_a1190a
    - Restriccion_la_evaluacion_de_la_suficiencia_del_capital_no_puede_basarse_exclusivamente_en_e_4ee053
    - Restriccion_la_exigencia_de_capital_minimo_por_riesgo_operacional_no_podra_ser_distinta_del__3a8a66
    - Restriccion_la_exigencia_de_efectivo_minimo_se_reducira_por_un_importe_equivalente_al_40_de__b5862e
    - Restriccion_la_expedicion_del_comprobante_cal_bloquea_el_registro_de_la_fcem_en_el_sistema_d_36c4f9
    - Restriccion_la_extraccion_de_fondos_se_rige_por_lo_previsto_en_los_puntos_3_1_6_1_y_3_1_6_3__509bff
    - Restriccion_la_extraccion_debe_realizarse_sin_distincion_alguna_entre_clientes_y_no_clientes_2301b1
    - Restriccion_la_falsedad_de_los_datos_contenidos_en_las_declaraciones_de_los_citados_integran_e129ad
    - Restriccion_la_falta_de_cumplimiento_dentro_del_plazo_fijado_de_cualesquiera_de_las_disposic_551bf9
    - Restriccion_la_falta_de_presentacion_de_la_nota_de_designacion_de_usuarios_implica_la_imposi_b10ea4
    - Restriccion_la_frecuencia_de_los_informes_de_gestion_de_riesgos_debe_aumentar_en_situaciones_eda659
    - Restriccion_la_garantia_otorgada_por_sgr_o_fondo_publico_solo_es_valida_si_efectiviza_los_cr_bade6e
    - Restriccion_la_garantia_preferida_b_se_aplica_cuando_el_plazo_residual_de_las_operaciones_su_71f0ba
    - Restriccion_la_imposicion_debe_permanecer_en_el_deposito_por_un_periodo_no_inferior_a_14_dia_1663a4
    - Restriccion_la_incorporacion_y_el_mantenimiento_de_servicios_adicionales_no_pueden_ser_exigi_af4bd8
    - Restriccion_la_informacion_debe_corresponder_a_la_entidad_destino__snp_tr_1_5_2_1_c6f7d6
    - Restriccion_la_informacion_debe_ser_restringida_a_las_personas_que_realmente_tengan_la_neces_e8d412
    - Restriccion_la_integracion_de_la_exigencia_en_pesos_con_los_titulos_mencionados_no_podra_sup_70cba6
    - Restriccion_la_integracion_de_la_exigencia_en_pesos_con_los_titulos_mencionados_no_podra_sup_752e5b
    - Restriccion_la_integracion_de_la_exigencia_en_pesos_con_los_titulos_mencionados_no_podra_sup_d052dc
    - Restriccion_la_leyenda_del_sistema_de_seguro_de_garantia_de_depositos_debe_adecuarse_a_la_mo_b2f6f2
    - Restriccion_la_modalidad_de_recepcion_de_informacion_de_cuota_elegida_no_exime_al_solicitant_055226
    - Restriccion_la_mora_se_produce_de_pleno_derecho_por_falsedad_de_cualquiera_de_las_declaracio_373acc
    - Restriccion_la_mora_se_produce_de_pleno_derecho_por_incumplimiento_de_disposiciones_legales__ef7356
    - Restriccion_la_mora_se_produce_de_pleno_derecho_por_incumplimiento_de_obligaciones_pactadas__9916a5
    - Restriccion_la_mora_se_produce_de_pleno_derecho_por_la_formacion_de_un_acuerdo_preconcursal__102418
    - Restriccion_la_mora_se_produce_de_pleno_derecho_por_solicitud_de_quiebra_peticion_por_tercer_936543
    - Restriccion_la_mora_se_produce_de_pleno_derecho_si_el_bien_prendado_sufre_deterioro_que_no_c_58aabb
    - Restriccion_la_mora_se_produce_de_pleno_derecho_si_el_deudor_traslada_definitivamente_el_bie_af1a52
    - Restriccion_la_mora_se_produce_de_pleno_derecho_y_sin_necesidad_de_requerimiento_o_interpela_cc97d9
    - Restriccion_la_numeracion_repetida_y_el_codigo_de_barras_en_el_anverso_deben_realizarse_en_l_e2fdaa
    - Restriccion_la_numeracion_tipografica_en_el_anverso_debe_ser_con_tinta_penetrante_fluorescen_e94aee
    - Restriccion_la_perforacion_debe_abarcar_como_minimo_el_60_sesenta_por_ciento_de_la_superfici_33cb46
    - Restriccion_la_periodicidad_de_la_cuota_no_podra_ser_superior_a_semestral__manori_3_1_5_7_e165bf
    - Restriccion_la_poliza_debe_ser_emitida_o_endosable_a_favor_de_la_entidad_financiera_o_de_qui_0879b0
    - Restriccion_la_poliza_debe_ser_emitida_o_endosable_a_favor_de_la_entidad_financiera_o_de_qui_79a33c
    - Restriccion_la_poliza_debe_ser_emitida_o_endosable_a_favor_de_la_entidad_financiera_o_de_qui_914da4
    - Restriccion_la_porcion_de_la_asistencia_al_prestatario_no_cubierta_por_garantias_admitidas_r_5a667d
    - Restriccion_la_posicion_a_termino_bimestral_no_podra_exceder_el_5_segun_la_metodologia_descr_e84392
    - Restriccion_la_posicion_global_bimestral_no_podra_exceder_el_10__ri_pgn_6_2_a1bf59
    - Restriccion_la_prevision_sobre_la_cartera_normal_debe_tener_caracter_global_no_individual__c_9decea
    - Restriccion_la_reserva_especial_se_constituye_solo_hasta_el_limite_de_los_resultados_no_asig_39877b
    - Restriccion_la_reserva_solo_podra_desafectarse_para_su_capitalizacion_o_para_absorber_eventu_4b7193
    - Restriccion_la_responsabilidad_en_el_cumplimiento_de_estas_normas_no_puede_ser_delegada_sera_d53463
    - Restriccion_la_retencion_o_recompra_de_posiciones_de_titulizacion_puede_limitar_la_transfere_6f6933
    - Restriccion_la_sena_o_pago_a_cuenta_no_podra_exceder_del_20_del_precio_o_del_ingreso_de_los__022a56
    - Restriccion_la_solicitud_debera_contener_como_minimo_la_informacion_descripta_en_el_formular_efc7ff
    - Restriccion_la_suma_de_las_tenencias_de_billetes_en_buen_uso_afectados_a_la_operatoria_de_ci_e81433
    - Restriccion_la_suma_del_codigo_210105_tp_no_puede_superar_la_suma_de_codigos_824100_001_y_82_3a916b
    - Restriccion_la_suma_del_codigo_255035_m_no_puede_superar_la_partida_205035_010__ri_rml_1_3_40c252
    - Restriccion_la_suma_del_codigo_255040_m_no_puede_superar_la_partida_205040_010__ri_rml_1_3_a1772f
    - Restriccion_la_suma_del_codigo_255050_m_no_puede_superar_la_partida_205050_010__ri_rml_1_3_6b1c19
    - Restriccion_la_tarjeta_magnetica_no_se_entrega_al_titular_cuando_se_ha_designado_un_represen_7c6179
    - Restriccion_la_tasa_de_efectivo_minimo_para_depositos_en_cuentas_especiales_para_exportadore_eebcf6
    - Restriccion_la_tasa_de_efectivo_minimo_para_depositos_en_cuentas_especiales_para_titulares_c_13006f
    - Restriccion_la_tasa_de_integracion_de_efectivo_minimo_para_pases_pasivos_en_pesos_con_plazo__32001c
    - Restriccion_la_tasa_de_integracion_de_efectivo_minimo_para_pases_pasivos_en_pesos_con_plazo__f69105
    - Restriccion_la_tasa_de_interes_no_podra_ser_inferior_a_la_tasa_vigente_para_depositos_en_caj_acbd67
    - Restriccion_la_tasa_de_interes_no_podra_ser_superior_a_la_ofrecida_el_dia_de_la_imposicion_p_2f88e3
    - Restriccion_la_tasa_de_interes_resultante_luego_de_aplicar_la_perturbacion_estara_sujeta_a_u_c161b7
    - Restriccion_la_tasa_de_interes_resultante_luego_de_aplicar_la_perturbacion_estara_sujeta_a_u_cb7ad6
    - Restriccion_la_tasa_de_interes_resultante_luego_de_aplicar_la_perturbacion_que_corresponda_e_7c1d32
    - Restriccion_la_tasa_de_interes_se_aplicara_sobre_el_total_del_deposito_sin_limitacion_alguna_9e2de2
    - Restriccion_la_transferencia_no_requiere_notificacion_al_deudor_salvo_cuando_medie_modificac_b2226c
    - Restriccion_las_acreditaciones_a_la_cuenta_especial_solo_se_admitiran_por_los_origenes_y_apl_112c3a
    - Restriccion_las_acreditaciones_adicionales_a_las_beneficiarias_mencionadas_por_todo_concepto_e5d452
    - Restriccion_las_acreditaciones_de_importes_netos_en_pesos_provenientes_de_la_liquidacion_de__b8eecd
    - Restriccion_las_acreditaciones_de_importes_netos_en_pesos_provenientes_de_liquidacion_de_div_772cb0
    - Restriccion_las_acreditaciones_deben_provenir_unicamente_de_transferencias_del_exterior__dep_1a9b5b
    - Restriccion_las_acreditaciones_deben_provenir_unicamente_de_transferencias_del_exterior_cuyo_dca2c2
    - Restriccion_las_acreditaciones_deben_provenir_unicamente_de_transferencias_del_exterior_cuyo_f98c9a
    - Restriccion_las_acreditaciones_en_cada_cuenta_abierta_y_por_moneda_no_podran_superar_el_impo_20c819
    - Restriccion_las_acreditaciones_en_cuentas_especiales_para_exportadores_se_admitiran_hasta_el_c8f226
    - Restriccion_las_acreditaciones_se_admitiran_solo_hasta_las_fechas_especificadas_en_el_decret_b169e0
    - Restriccion_las_actividades_de_la_sucursal_en_el_exterior_no_podran_iniciarse_si_no_se_cumpl_735515
    - Restriccion_las_actividades_de_las_oficinas_de_representacion_se_limitan_exclusivamente_a_ac_ff0c3b
    - Restriccion_las_cajas_de_ahorros_se_abriran_exclusivamente_a_nombre_y_a_la_orden_del_declara_981363
    - Restriccion_las_capacidades_de_agregacion_de_datos_sobre_riesgos_deben_ser_uniformes_indepen_057b9b
    - Restriccion_las_colocaciones_depositos_a_plazo_fijo_e_inversiones_a_plazo_cuya_titularidad_h_db6e2e
    - Restriccion_las_comisiones_o_cargos_por_servicios_adicionales_solo_pueden_efectuarse_en_func_069982
    - Restriccion_las_cuentas_abiertas_por_inversores_extranjeros_deben_utilizarse_exclusivamente__b7e859
    - Restriccion_las_cuentas_especiales_de_repatriacion_deberan_abrirse_exclusivamente_para_el_fi_f97ad1
    - Restriccion_las_deudas_por_adquisicion_de_activos_inmovilizados_no_pueden_superar_el_valor_r_d12cb8
    - Restriccion_las_disposiciones_sobre_deterioro_de_activos_financieros_se_aplican_solo_a_los_a_9d09e0
    - Restriccion_las_entidades_financieras_no_deberan_registrar_en_promedio_deficiencias_en_la_in_b14fcc
    - Restriccion_las_entidades_financieras_no_intervienen_en_la_compensacion_de_fcem_al_vencimien_f87106
    - Restriccion_las_entidades_financieras_no_podran_permitir_pagos_duplicados_totales_o_parciale_e56337
    - Restriccion_las_exposiciones_con_no_residentes_garantizadas_por_entidades_del_pais_tales_com_2348ae
    - Restriccion_las_exposiciones_con_residentes_en_el_pais_garantizadas_por_entidades_extranjera_d1cfa7
    - Restriccion_las_financiaciones_a_clientes_vinculados_quedan_alcanzadas_por_las_normas_sobre__ebe700
    - Restriccion_las_financiaciones_a_ser_informadas_en_los_codigos_808000_001_809000_001_841000__25ea79
    - Restriccion_las_financiaciones_computadas_para_la_deduccion_de_los_puntos_7_2_1_a_7_2_4_solo_e95889
    - Restriccion_las_financiaciones_de_naturaleza_comercial_que_superen_250_000_deben_ser_clasifi_d68e83
    - Restriccion_las_financiaciones_deben_haber_sido_acordadas_a_una_tasa_de_interes_nominal_anua_710636
    - Restriccion_las_financiaciones_del_punto_6_4_1_deben_tener_un_plazo_promedio_igual_o_superio_072374
    - Restriccion_las_financiaciones_otorgadas_a_partir_del_06_11_2020_inclusive_no_pueden_imputar_3abf94
    - Restriccion_las_financiaciones_otorgadas_estaran_sujetas_a_los_limites_por_cliente_previstos_e91b99
    - Restriccion_las_financiaciones_que_excedan_los_margenes_de_cobertura_de_garantias_preferidas_54c6d6
    - Restriccion_las_garantias_en_forma_de_prenda_fija_con_registro_en_primer_grado_o_con_desplaz_c477be
    - Restriccion_las_guardas_en_el_anverso_deben_ser_en_color_azul_con_tinta_que_tenga_fluorescen_c62a8d
    - Restriccion_las_leliq_admitidas_para_la_integracion_de_la_exigencia_de_efectivo_minimo_en_pe_9965a0
    - Restriccion_las_letras_de_cambio_implementadas_conforme_a_esta_norma_no_requeriran_aceptacio_d04218
    - Restriccion_las_letras_internas_intransferibles_del_banco_central_de_la_republica_argentina__4fb1f5
    - Restriccion_las_limitaciones_que_se_generen_al_definir_los_alcances_del_producto_deberan_ser_0de89f
    - Restriccion_las_manifestaciones_de_bienes_que_se_presenten_deben_corresponder_al_mes_inmedia_736640
    - Restriccion_las_maquinas_clasificadoras_deben_contar_con_un_minimo_de_tres_niveles_de_calida_c25cd7
    - Restriccion_las_opciones_de_recompra_anticipada_no_pueden_ejercerse_durante_el_plazo_de_la_d_ab5f7d
    - Restriccion_las_operaciones_de_credito_garantizadas_con_garantias_preferidas_a_no_pueden_sup_801a2a
    - Restriccion_las_operaciones_de_credito_no_podran_superar_medido_en_forma_residual_el_termino_61abbf
    - Restriccion_las_operaciones_del_punto_6_4_2_no_tienen_plazo_minimo__efemin_6_5_2_84a004
    - Restriccion_las_posturas_deben_tener_un_minimo_de_un_millar__cirmo3_5_2_1_6_bb033d
    - Restriccion_las_posturas_en_la_rueda_num_d_deben_ser_siempre_de_caracter_parcial_no_permitie_40912e
    - Restriccion_las_posturas_en_la_rueda_num_d_se_liquidan_en_t_0_mismo_dia_de_la_operacion__cir_18855b
    - Restriccion_las_precancelaciones_total_o_parcial_pueden_estar_sujetas_a_cargos_y_comisiones__468968
    - Restriccion_las_previsiones_sobre_las_demas_categorias_de_cartera_deben_tener_imputacion_ind_a2d239
    - Restriccion_las_transferencias_de_fondos_solo_se_realizaran_a_solicitud_del_empleador_que_ef_100747
    - Restriccion_las_transferencias_de_la_letra_tienen_los_efectos_previstos_en_el_articulo_40_de_f14964
    - Restriccion_las_transferencias_deben_ser_en_pesos_o_en_moneda_extranjera_autorizada_por_el_b_665572
    - Restriccion_las_transferencias_inmediatas_solo_pueden_realizarse_entre_cuentas_denominadas_e_9cbc99
    - Restriccion_las_transferencias_son_oponibles_al_deudor_y_terceros_a_partir_de_la_inscripcion_689c7b
    - Restriccion_las_tres_monedas_conmemorativas_tienen_el_mismo_diseno_en_anverso_y_reverso_con__c2b867
    - Restriccion_limite_de_permanencia_minima_en_la_categoria_riesgo_alto_de_180_dias_para_deudor_95fd25
    - Restriccion_limite_temporal_deudor_clasificado_en_riesgo_bajo_que_haya_refinanciado_su_deuda_6be6fa
    - Restriccion_los_analistas_de_riesgo_de_credito_deben_ser_independientes_del_area_de_operacio_88af70
    - Restriccion_los_anticipos_recibidos_por_la_venta_de_activos_no_pueden_superar_el_valor_resid_bca8b0
    - Restriccion_los_archivos_deben_transmitirse_hasta_el_horario_limite_definido__snp_cheq_3_2_3_bcadc8
    - Restriccion_los_archivos_seran_devueltos_cuando_exista_error_en_la_estructura_del_archivo__s_d197b9
    - Restriccion_los_archivos_seran_devueltos_cuando_exista_error_en_los_codigos_de_entidades_ori_d025bb
    - Restriccion_los_archivos_seran_devueltos_cuando_exista_falta_de_coincidencia_en_totales_de_c_fca638
    - Restriccion_los_archivos_seran_devueltos_cuando_exista_imposibilidad_de_lectura_del_archivo__9129ab
    - Restriccion_los_archivos_seran_devueltos_cuando_la_entidad_originante_no_este_adherida_a_la__fb1dd5
    - Restriccion_los_archivos_seran_devueltos_cuando_no_coincida_cuit_cuil_o_cdi_del_beneficiario_a1558d
    - Restriccion_los_archivos_seran_devueltos_cuando_se_trate_de_un_archivo_duplicado__snp_tr_1_3_098ef8
    - Restriccion_los_archivos_seran_rechazados_cuando_la_entidad_no_este_adherida_a_la_cec__snp_c_5e1363
    - Restriccion_los_archivos_seran_rechazados_por_error_en_la_estructura_del_archivo__snp_cheq_3_377ee9
    - Restriccion_los_archivos_seran_rechazados_por_error_en_los_codigos_de_entidades_giradas_y_de_a70439
    - Restriccion_los_archivos_seran_rechazados_por_falta_de_coincidencia_en_totales_de_control__s_2eda40
    - Restriccion_los_archivos_seran_rechazados_por_imposibilidad_de_lectura__snp_cheq_3_1_2_1_15cffb
    - Restriccion_los_archivos_seran_rechazados_si_son_duplicados__snp_cheq_3_1_2_1_aa8f9c
    - Restriccion_los_cambios_de_domicilio_de_la_oficina_solo_podran_tener_lugar_dentro_de_los_lim_d60994
    - Restriccion_los_campos_de_la_cabecera_de_archivo_tienen_requerimientos_de_completitud_difere_da365b
    - Restriccion_los_campos_numericos_que_alcanzan_su_longitud_maxima_no_deben_completarse_con_ce_4ee774
    - Restriccion_los_campos_numericos_que_alcanzan_su_longitud_maxima_no_deben_completarse_con_ce_749006
    - Restriccion_los_cargos_no_ingresados_en_tiempo_y_forma_estaran_sujetos_durante_el_periodo_de_047a0d
    - Restriccion_los_centros_de_transmision_no_tendran_efecto_en_la_compensacion_actuaran_solamen_18498b
    - Restriccion_los_centros_de_transmision_no_tendran_ningun_efecto_en_la_compensacion_actuaran__47dec9
    - Restriccion_los_certificados_de_depositos_a_plazo_fijo_se_computaran_por_un_porcentaje_del_1_f78007
    - Restriccion_los_cheques_librados_en_usd_solo_pueden_utilizarse_para_operaciones_de_compraven_0bb974
    - Restriccion_los_cheques_no_pueden_contener_endosos_que_excedan_el_limite_establecido_en_el_p_1f858e
    - Restriccion_los_contadores_publicos_auditores_no_pueden_desempenarse_al_mismo_tiempo_en_mas__4e74ea
    - Restriccion_los_conyuges_los_parientes_por_consanguinidad_en_linea_recta_los_colaterales_has_311297
    - Restriccion_los_cupones_de_tarjetas_de_credito_emitidas_por_entidades_financieras_se_computa_da9dbc
    - Restriccion_los_cupones_de_tarjetas_de_credito_emitidos_por_las_restantes_empresas_no_financ_0ae5dc
    - Restriccion_los_datos_de_riesgos_deben_ser_completos_cualquier_excepcion_debe_ser_identifica_2ea3fd
    - Restriccion_los_debitos_automaticos_no_configuran_novacion_por_lo_que_se_mantienen_vigentes__cffcc2
    - Restriccion_los_debitos_que_se_efectuen_en_caja_de_ahorros_cuentas_sueldo_y_cuentas_corrient_d9babf
    - Restriccion_los_defectos_de_aplicacion_excluidos_no_pueden_ser_compensados_con_compras_de_mo_b929d8
    - Restriccion_los_depositos_en_efectivo_en_cada_cuenta_estan_limitados_a_un_maximo_mensual_equ_d0181c
    - Restriccion_los_depositos_se_admitiran_hasta_el_equivalente_en_pesos_de_los_importes_previst_bdc940
    - Restriccion_los_depositos_y_financiaciones_recibidas_en_titulos_valores_no_deberan_incorpora_76feb2
    - Restriccion_los_directores_gerentes_y_empleados_de_la_misma_sociedad_o_de_otra_controlada_o__8fb8be
    - Restriccion_los_directores_o_administradores_de_sociedad_cuya_conducta_se_calificare_de_culp_9bcadd
    - Restriccion_los_documentos_cedidos_no_podran_ser_reemplazados_al_vencimiento_deberan_ser_pre_02f203
    - Restriccion_los_documentos_correspondientes_a_sujetos_obligados_al_pago_clasificados_en_cate_c487b9
    - Restriccion_los_escenarios_de_disrupcion_deben_estar_sujetos_a_umbrales_o_limites_para_la_ac_5b6d92
    - Restriccion_los_excesos_a_la_relacion_de_concentracion_de_depositos_estaran_sujetos_a_una_ex_4a40c5
    - Restriccion_los_excesos_a_la_relacion_de_efectivo_minimo_estaran_sujetos_a_una_exigencia_del_287ace
    - Restriccion_los_excesos_a_los_limites_fijados_en_materia_de_fraccionamiento_del_credito_esta_3e776e
    - Restriccion_los_excesos_a_los_limites_fijados_estaran_sujetos_a_las_disposiciones_establecid_c26f0a
    - Restriccion_los_excesos_que_se_registren_a_los_limites_previstos_en_esta_seccion_estaran_suj_2785f5
    - Restriccion_los_fallidos_por_quiebra_casual_o_los_concursados_quedan_inhabilitados_hasta_cin_94e967
    - Restriccion_los_fallidos_por_quiebra_culpable_o_fraudulenta_quedan_inhabilitados_hasta_diez__a84d9c
    - Restriccion_los_fondos_acreditados_conforme_al_capitulo_ii_del_decreto_n_679_22_solo_pueden__7e6082
    - Restriccion_los_fondos_de_seguridad_en_el_anverso_deben_incluir_tinta_invisible_con_fluoresc_038969
    - Restriccion_los_fondos_de_seguridad_en_el_anverso_deben_ser_a_dos_colores_con_tinta_fugitiva_6d3de0
    - Restriccion_los_fondos_de_seguridad_en_el_reverso_deben_incluir_tinta_invisible_con_fluoresc_f0eb81
    - Restriccion_los_fondos_de_seguridad_en_el_reverso_deben_ser_a_un_color_con_tinta_fugitiva_a__c6e88d
    - Restriccion_los_fondos_declarados_deben_afectarse_exclusivamente_al_giro_de_divisas_por_el_p_f8e7d0
    - Restriccion_los_fondos_depositados_deben_tener_como_destino_exclusivamente_las_cuentas_de_ex_90e698
    - Restriccion_los_fondos_depositados_en_estas_cuentas_no_pueden_afectarse_al_pago_del_impuesto_b687d9
    - Restriccion_los_funcionarios_de_la_administracion_publica_cuyo_desempeno_se_relacione_con_el_e1497d
    - Restriccion_los_importes_computables_por_codigo_286_m_no_podran_superar_un_tercio_1_3_del_to_0e3893
    - Restriccion_los_importes_consignados_en_codigos_280_m_y_281_m_deben_cumplir_la_siguiente_exp_f319f6
    - Restriccion_los_importes_de_leliq_utilizadas_para_integrar_garantias_en_procesos_de_compensa_56f9b6
    - Restriccion_los_importes_de_leliq_utilizadas_para_integrar_garantias_en_procesos_de_compensa_9988d6
    - Restriccion_los_incumplimientos_a_las_normas_minimas_sobre_controles_internos_haran_pasibles_4ea1a8
    - Restriccion_los_inhabilitados_conforme_al_articulo_10_de_la_ley_no_21_526_no_pueden_ser_titu_8eb953
    - Restriccion_los_inhabilitados_para_ser_titulares_de_cuentas_corrientes_u_otras_que_participe_5fd1aa
    - Restriccion_los_instrumentos_vendidos_a_terceros_durante_la_vigencia_de_la_operacion_de_pase_fd28ba
    - Restriccion_los_interesados_quedan_sometidos_a_las_condiciones_de_las_cuentas_especiales_sin_fb415a
    - Restriccion_los_intereses_correspondientes_a_los_saldos_sujetos_al_requisito_de_permanencia__1bbc72
    - Restriccion_los_intereses_reconocidos_no_podran_superar_el_mayor_de_los_importes_que_surja_d_c109f0
    - Restriccion_los_mensajes_de_ordenes_de_pago_en_cib_que_envia_el_bcra_tendran_validez_unicame_4b2eb3
    - Restriccion_los_movimientos_de_cualquier_naturaleza_en_las_cuentas_sueldo_de_la_seguridad_so_b3785d
    - Restriccion_los_movimientos_de_cualquier_naturaleza_no_podran_generar_saldo_deudor_en_cuenta_1b8aab
    - Restriccion_los_movimientos_de_cualquier_naturaleza_no_podran_generar_saldo_deudor_en_estas__906753
    - Restriccion_los_movimientos_de_cualquier_naturaleza_no_podran_generar_saldo_deudor_en_la_cue_326fd2
    - Restriccion_los_movimientos_de_cualquier_naturaleza_no_podran_generar_saldo_deudor_en_la_cue_46c8ab
    - Restriccion_los_movimientos_de_cualquier_naturaleza_no_pueden_generar_saldo_deudor__depaho_3_151b67
    - Restriccion_los_movimientos_en_cuentas_sueldo_de_la_seguridad_social_no_podran_generar_saldo_58beb6
    - Restriccion_los_movimientos_no_podran_generar_saldo_deudor__depaho_3_11_5_f8ed47
    - Restriccion_los_originantes_y_destinatarios_de_las_transferencias_deben_ser_titulares_de_la__c36b1a
    - Restriccion_los_prestamos_prendarios_automotores_deberan_estar_garantizados_con_prenda_en_pr_f23070
    - Restriccion_los_procedimientos_de_auditoria_cuya_documentacion_no_sea_puesta_a_disposicion_d_45e2f2
    - Restriccion_los_rechazos_fuera_de_canje_deben_presentarse_dentro_de_un_plazo_maximo_de_120_d_762da0
    - Restriccion_los_reemplazos_de_tarjeta_originados_por_desmagnetizacion_o_cumplimiento_de_requ_467677
    - Restriccion_los_reemplazos_de_tarjeta_por_desmagnetizacion_deterioro_hasta_uno_por_ano_o_cum_424b81
    - Restriccion_los_restantes_socios_del_auditor_externo_seran_excluidos_del_registro_de_auditor_4d60c9
    - Restriccion_los_retiros_solo_podran_realizarse_por_el_saldo_total_de_la_cuenta_comprendiendo_adfa35
    - Restriccion_los_sistemas_elegidos_deben_permitir_que_los_datos_sean_trasladados_facilmente_a_f36571
    - Restriccion_los_solicitantes_no_deben_mantener_litigios_o_causas_judiciales_pendientes_que_s_2a0272
    - Restriccion_los_solicitantes_no_deben_tener_antecedentes_comerciales_o_crediticios_negativos_f5dbad
    - Restriccion_los_titulares_de_la_cuenta_gratuita_universal_no_podran_disponer_de_ningun_tipo__1417fe
    - Restriccion_los_titulos_vendidos_a_terceros_durante_la_operacion_de_prestamo_o_plazo_fijo_no_04805e
    - Restriccion_ningun_asociado_persona_fisica_residente_en_el_pais_o_en_el_exterior_o_persona_j_466df8
    - Restriccion_no_correspondera_informar_la_partida_750000_m_en_septiembre__ri_rml_sbloque14_d0e5aa
    - Restriccion_no_debe_considerarse_el_importe_reexpresado_del_ano_2003_se_debe_partir_del_valo_f9bd53
    - Restriccion_no_debe_haber_caracteres_invalidos_en_la_informacion_recibida__snp_tr_1_5_2_1_71bcfc
    - Restriccion_no_debe_haber_inclusion_de_dias_no_laborables__snp_tr_1_5_2_1_072fcd
    - Restriccion_no_deben_haberse_activado_partidas_que_no_correspondan_de_acuerdo_con_las_normas_45893e
    - Restriccion_no_deben_reexpresarse_los_activos_y_pasivos_no_monetarios_medidos_a_valor_razona_5547d3
    - Restriccion_no_debera_consignarse_el_dato_de_denominacion_para_los_codigos_89_10_20_y_30__ri_bfae21
    - Restriccion_no_debera_informarse_la_partida_102400_en_septiembre__ri_rml_sbloque14_51e3c8
    - Restriccion_no_es_condicion_necesaria_que_el_deudor_y_o_codeudores_sean_ocupantes_del_inmueb_a1f411
    - Restriccion_no_es_obligatorio_el_envio_periodico_de_resumenes_con_detalle_de_movimientos_en__60b2db
    - Restriccion_no_es_obligatorio_que_todos_los_riesgos_sean_expresados_con_la_misma_medida__adr_967dd5
    - Restriccion_no_existe_limite_maximo_de_edad_para_los_solicitantes_excepto_el_que_derive_de_l_a6ac2c
    - Restriccion_no_hay_limite_alguno_para_las_acreditaciones_originadas_en_la_venta_de_bienes_y__1aa860
    - Restriccion_no_hay_limite_de_importe_para_las_extracciones_salvo_los_que_expresamente_se_con_e2b3da
    - Restriccion_no_hay_limite_en_la_cantidad_de_adhesiones_a_servicios_de_pago_por_canales_elect_eaca1f
    - Restriccion_no_hay_limite_en_la_cantidad_de_extracciones_que_pueden_realizarse__depaho_3_11__82eae7
    - Restriccion_no_podra_tener_lugar_el_pago_del_saldo_de_precio_en_operaciones_de_modificacion__3e7aa6
    - Restriccion_no_podra_tener_lugar_la_capitalizacion_de_los_aportes_irrevocables_para_futuros__9f7597
    - Restriccion_no_podra_tener_lugar_la_inscripcion_de_la_transferencia_en_el_registro_de_accion_06fd11
    - Restriccion_no_podra_tener_lugar_la_tradicion_de_las_acciones_a_los_adquirentes_o_sus_repres_aed263
    - Restriccion_no_podran_encuadrarse_como_aplicacion_elegible_las_financiaciones_que_se_acuerde_1617b5
    - Restriccion_no_podran_ser_accionistas_con_una_participacion_igual_o_superior_al_5_del_capita_42e942
    - Restriccion_no_puede_haber_distincion_alguna_entre_clientes_y_no_clientes_en_el_acceso_a_la__adf3c0
    - Restriccion_no_pueden_desempenarse_como_socio_responsable_los_directores_o_administradores_d_4eae4e
    - Restriccion_no_pueden_desempenarse_como_socio_responsable_los_fallidos_por_quiebra_casual_o__d4a592
    - Restriccion_no_pueden_desempenarse_como_socio_responsable_los_fallidos_por_quiebra_culpable__d0c257
    - Restriccion_no_pueden_imputarse_para_las_deducciones_de_los_puntos_7_2_1_y_7_2_2_las_financi_161176
    - Restriccion_no_pueden_imputarse_para_las_deducciones_de_los_puntos_7_2_1_y_7_2_2_las_financi_bf1df9
    - Restriccion_no_pueden_ser_titulares_de_la_cuenta_gratuita_universal_quienes_ya_sean_titulare_49b5e3
    - Restriccion_no_resulta_obligatoria_la_emision_periodica_de_resumenes_con_el_detalle_de_los_m_ef5fa7
    - Restriccion_no_se_aceptaran_los_depositos_en_cuyos_comprobantes_no_se_hayan_consignado_todos_75ef98
    - Restriccion_no_se_admite_la_aplicacion_anticipada_de_ninguna_niif_salvo_que_se_especifique_l_44d702
    - Restriccion_no_se_admitira_el_retiro_de_efectivo_de_estas_cuentas__depaho_3_9_3_81f80c
    - Restriccion_no_se_admitira_integrar_con_bonos_los_incrementos_de_exigencia_derivados_de_apli_1514e9
    - Restriccion_no_se_admitira_la_renuncia_del_cliente_a_prestaciones_especificamente_contemplad_d56556
    - Restriccion_no_se_admitiran_denominaciones_que_se_presten_a_confusiones_o_interpretaciones_e_abdef4
    - Restriccion_no_se_admitiran_denominaciones_que_se_presten_a_confusiones_o_interpretaciones_e_b00806
    - Restriccion_no_se_admitiran_extracciones_de_la_imposicion_antes_de_que_transcurra_el_periodo_cc186e
    - Restriccion_no_se_aplica_a_refinanciaciones__cajasc_5_5_10_2_51fdf9
    - Restriccion_no_se_considera_que_se_posee_adecuada_solvencia_propia_cuando_resulte_factible_p_d60c88
    - Restriccion_no_se_dara_curso_a_las_solicitudes_de_autorizacion_que_no_se_presenten_ajustadas_4b8e2f
    - Restriccion_no_se_dara_curso_a_ningun_nuevo_pedido_hasta_que_transcurra_un_ano_a_partir_de_l_a50176
    - Restriccion_no_se_dara_uso_a_la_propiedad_para_destinos_ilegales_o_distintos_a_los_manifesta_47e1fc
    - Restriccion_no_se_deberan_usar_separadores_de_ningun_tipo_en_la_indicacion_de_motivos_de_rec_7047f9
    - Restriccion_no_se_estableceran_limites_cuantitativos_importes_minimos_ni_maximos_para_los_de_d997d5
    - Restriccion_no_se_incluiran_en_la_difusion_los_deudores_alcanzados_por_el_articulo_16_inciso_9b06d8
    - Restriccion_no_se_informara_la_partida_81200x_010_correspondiente_a_depositos_en_dolares_cap_11da6e
    - Restriccion_no_se_informaran_en_ninguno_de_los_meses_del_bimestre_las_partidas_400_m_y_401_m_7c14ff
    - Restriccion_no_se_informaran_los_datos_correspondientes_a_las_partidas_451000_m_451200_m_y_4_dfba3a
    - Restriccion_no_se_pueden_utilizar_bandas_elasticas_de_ningun_tipo_para_la_sujecion_de_los_di_05012e
    - Restriccion_no_se_reconoce_como_activo_la_especie_recibida_en_depositos_y_financiaciones_en__5e3a82
    - Restriccion_no_se_reconoceran_intereses_por_la_integracion_correspondiente_a_los_depositos_y_3da7d7
    - Restriccion_no_se_reconoceran_intereses_por_la_integracion_correspondiente_a_los_depositos_y_bafe0d
    - Restriccion_no_se_utilizaran_carbonicos_en_la_integracion_del_formulario__depaho_sbloque5_a5f9d5
    - Restriccion_no_sera_posible_autorizar_una_transferencia_inmediata_en_funcion_de_la_expectati_bfc704
    - Restriccion_notificado_el_nuevo_domicilio_de_pago_no_puede_oponerse_excepcion_de_pago_docume_738ecd
    - Restriccion_nuevas_financiaciones_que_impliquen_desembolsos_de_fondos_de_hasta_200_000_que_n_1a8e9e
    - Restriccion_nuevas_financiaciones_que_impliquen_desembolsos_de_fondos_mayores_de_200_000_y_d_1e37a3
    - Restriccion_para_cajas_de_credito_cooperativas_clasificadas_en_categoria_i_con_una_o_mas_suc_3738bc
    - Restriccion_para_cajas_de_credito_cooperativas_clasificadas_en_categoria_ii_con_una_o_mas_su_15cec7
    - Restriccion_para_efectuar_el_control_sobre_la_partida_210100_a_partir_de_junio_18_se_detraer_32863e
    - Restriccion_para_entidades_comprendidas_en_el_grupo_a_y_sucursales_o_subsidiarias_de_g_sib_n_24f8b5
    - Restriccion_para_entidades_comprendidas_en_el_grupo_a_y_sucursales_o_subsidiarias_de_g_sib_n_65d667
    - Restriccion_para_entidades_comprendidas_en_el_grupo_a_y_sucursales_o_subsidiarias_de_g_sib_n_6d9232
    - Restriccion_para_entidades_comprendidas_en_el_grupo_a_y_sucursales_o_subsidiarias_de_g_sib_n_7a6bed
    - Restriccion_para_entidades_comprendidas_en_el_grupo_a_y_sucursales_o_subsidiarias_de_g_sib_n_c4aac4
    - Restriccion_para_entidades_comprendidas_en_el_grupo_a_y_sucursales_o_subsidiarias_de_g_sib_n_ccb4e3
    - Restriccion_para_entidades_del_grupo_b_el_porcentaje_minimo_a_aplicar_sera_del_25_del_previs_ce0ca2
    - Restriccion_para_entidades_no_comprendidas_en_el_grupo_a_ni_en_sucursales_o_subsidiarias_de__1d8001
    - Restriccion_para_entidades_no_comprendidas_en_el_grupo_a_ni_en_sucursales_o_subsidiarias_de__a763e5
    - Restriccion_para_entidades_no_comprendidas_en_el_grupo_a_ni_en_sucursales_o_subsidiarias_de__c315ef
    - Restriccion_para_la_categoria_i_los_restantes_asociados_restantes_personas_juridicas_con_3_a_8b846f
    - Restriccion_para_la_categoria_i_una_cooperativa_con_3_anos_de_funcionamiento_efectivo_como_m_81f880
    - Restriccion_para_la_categoria_i_una_persona_juridica_cuyo_objeto_social_sean_las_microfinanz_446d51
    - Restriccion_para_la_categoria_ii_los_restantes_asociados_restantes_personas_juridicas_con_3__1608e2
    - Restriccion_para_la_categoria_ii_una_cooperativa_con_3_anos_de_funcionamiento_efectivo_como__3d565e
    - Restriccion_para_la_categoria_ii_una_persona_juridica_cuyo_objeto_social_sean_las_microfinan_251688
    - Restriccion_para_la_categoria_iii_los_restantes_asociados_restantes_personas_juridicas_con_3_9c9a6f
    - Restriccion_para_la_categoria_iii_una_cooperativa_con_3_anos_de_funcionamiento_efectivo_como_7bb15f
    - Restriccion_para_la_categoria_iii_una_persona_juridica_cuyo_objeto_social_sean_las_microfina_161767
    - Restriccion_para_la_categoria_iv_los_restantes_asociados_restantes_personas_juridicas_con_3__0454c2
    - Restriccion_para_la_categoria_iv_una_cooperativa_con_3_anos_de_funcionamiento_efectivo_como__7cebb1
    - Restriccion_para_la_categoria_iv_una_persona_juridica_cuyo_objeto_social_sean_las_microfinan_f632dd
    - Restriccion_para_la_posicion_en_pesos_el_traslado_de_la_exigencia_no_integrada_se_admite_uni_e46325
    - Restriccion_para_lineas_financieras_del_exterior_obtenidas_de_personas_vinculadas_con_plazo__85b601
    - Restriccion_para_lineas_financieras_del_exterior_obtenidas_de_personas_vinculadas_con_plazo__8de217
    - Restriccion_plazo_minimo_de_30_dias_para_pases_pasivos_con_otras_contrapartes__opefci_4_4_2__a6d6a5
    - Restriccion_plazo_minimo_de_30_dias_para_pases_pasivos_en_bolsas_y_mercados_autorizados_por__78300e
    - Restriccion_ponderador_de_riesgo_de_credito_del_0_para_disponibilidades_en_cuentas_corriente_3eb34c
    - Restriccion_ponderador_de_riesgo_del_50_para_creditos_por_arrendamientos_financieros_sobre_i_353192
    - Restriccion_ponderador_de_riesgo_del_50_para_financiaciones_cubiertas_con_garantias_otorgada_60ec79
    - Restriccion_ponderador_de_riesgo_del_50_para_financiaciones_cubiertas_con_prenda_fija_con_re_886db4
    - Restriccion_prohibicion_de_cobrar_al_deudor_gastos_relacionados_con_el_prestamo_hipotecario__871dbf
    - Restriccion_prohibicion_de_desempenarse_en_cargos_de_promotor_fundador_miembro_de_consejo_de_88275b
    - Restriccion_prohibicion_de_devolver_al_interesado_los_billetes_retenidos_presuntamente_falso_7b70eb
    - Restriccion_prohibicion_de_realizar_con_otras_entidades_financieras_cooperativas_de_credito__4c178f
    - Restriccion_prohibicion_del_retiro_del_dinero_en_efectivo_depositado_en_las_cuentas_a_la_vis_c9fa82
    - Restriccion_prohibicion_para_desempenarse_como_promotores_fundadores_directores_administrado_39fcec
    - Restriccion_queda_prohibido_el_uso_de_cheques_vales_ordenes_de_pago_u_otros_documentos_disti_abec76
    - Restriccion_reclasificacion_inmediata_a_la_categoria_inferior_inmediata_cuando_se_verifiquen_9f17a0
    - Restriccion_reclasificacion_inmediata_al_nivel_siguiente_inferior_cuando_se_verifiquen_atras_1c49c1
    - Restriccion_restriccion_de_que_la_integracion_en_bote_leliq_nobac_y_tpn_en_pesos_no_podra_ex_a7ac72
    - Restriccion_riesgo_residual_generado_por_la_imposibilidad_de_tomar_posesion_o_realizar_el_ac_b7bdf8
    - Restriccion_riesgo_residual_generado_por_la_ineficacia_de_la_documentacion_de_la_tecnica_de__7bd5c5
    - Restriccion_riesgo_residual_generado_por_negativa_o_retraso_en_el_pago_por_parte_del_garante_d277a0
    - Restriccion_se_admitiran_acreditaciones_por_hasta_el_equivalente_en_pesos_del_monto_de_las_f_7e4c49
    - Restriccion_se_admitiran_acreditaciones_por_hasta_el_monto_en_pesos_proveniente_de_la_liquid_85f1f6
    - Restriccion_se_admitiran_acreditaciones_unicamente_hasta_el_30_11_22_por_el_monto_en_pesos_p_e2dd9b
    - Restriccion_se_admitiran_acreditaciones_unicamente_hasta_el_30_de_diciembre_de_2022_por_el_m_aa166b
    - Restriccion_se_admitiran_debitos_unicamente_por_los_conceptos_que_se_enumeran_a_continuacion_8b8161
    - Restriccion_se_admitiran_depositos_en_pesos_provenientes_de_ventas_de_soja_del_titular_que_n_52b9a0
    - Restriccion_se_admitiran_hasta_4_extracciones_por_todo_concepto_por_mes_calendario_sin_limit_ee26ec
    - Restriccion_se_admitiran_unicamente_acreditaciones_que_correspondan_a_aportes_al_fondo_de_ce_5acdf3
    - Restriccion_se_excluiran_del_registro_las_asociaciones_en_las_cuales_participen_o_hayan_part_50f5c9
    - Restriccion_se_excluye_transitoriamente_del_alcance_de_aplicacion_de_la_niif_9_a_los_instrum_1d9280
    - Restriccion_se_excluyen_de_la_agregacion_los_cambios_de_eve_que_no_representen_perdida_es_de_5b4dc3
    - Restriccion_se_interrumpira_el_devengamiento_de_intereses_y_accesorios_respecto_de_los_instr_c57695
    - Restriccion_se_prohibe_confeccionar_o_poner_en_circulacion_piezas_de_aspecto_semejante_a_bil_37711f
    - Restriccion_se_prohibe_efectuar_inversiones_de_caracter_transitorio_en_colocaciones_facilmen_d1952a
    - Restriccion_se_prohibe_el_incumplimiento_del_plazo_de_envio_de_chc_pagados_en_caso_de_incump_6cb6de
    - Restriccion_se_prohibe_la_aceptacion_de_valores_a_cargo_de_otras_entidades_financieras__depa_4cd9c1
    - Restriccion_se_prohibe_la_compensacion_de_posiciones_deficitarias_con_posiciones_excedentari_8509a7
    - Restriccion_se_prohibe_la_concertacion_de_operaciones_mediante_contratos_que_en_alguna_circu_64c1ab
    - Restriccion_se_prohibe_la_falsedad_de_contenido_en_la_declaracion_jurada_quien_incumpla_sera_f090e4
    - Restriccion_se_prohibe_retener_o_deducir_impuestos_tasas_o_gravamenes_de_las_sumas_pagaderas_0c9cd2
    - Restriccion_se_rechazara_total_o_parcialmente_el_deposito_si_los_packs_o_millares_no_estan_d_094396
    - Restriccion_si_la_suma_total_de_creditos_del_lote_supera_la_cantidad_de_caracteres_disponibl_96c25d
    - Restriccion_si_la_suma_total_de_debitos_del_lote_supera_la_cantidad_de_caracteres_disponible_203879
    - Restriccion_si_no_se_mantiene_el_cumplimiento_de_las_condiciones_basicas_establecidas_en_el__a62d83
    - Restriccion_si_vencido_el_plazo_de_un_ano_la_entidad_no_ha_iniciado_sus_actividades_la_autor_5ab4db
    - Restriccion_si_vencido_el_plazo_de_un_ano_no_se_ha_producido_la_iniciacion_de_actividades_de_8e8150
    - Restriccion_solo_se_admiten_rechazos_que_se_originan_en_motivos_de_rechazo_de_cheques_utiliz_348110
    - Restriccion_tasa_de_efectivo_minimo_del_0_para_depositos_a_plazo_fijo_en_moneda_extranjera_c_195b71
    - Restriccion_tasa_de_efectivo_minimo_del_11_para_depositos_a_plazo_fijo_en_moneda_extranjera__325319
    - Restriccion_tasa_de_efectivo_minimo_del_17_para_depositos_a_plazo_fijo_en_moneda_extranjera__f90da2
    - Restriccion_tasa_de_efectivo_minimo_del_23_para_depositos_a_plazo_fijo_en_moneda_extranjera__a11f82
    - Restriccion_tasa_de_efectivo_minimo_del_2_para_depositos_a_plazo_fijo_en_moneda_extranjera_c_b68975
    - Restriccion_tasa_de_efectivo_minimo_del_5_para_depositos_a_plazo_fijo_en_moneda_extranjera_c_dddf24
    - Restriccion_tasa_de_efectivo_minimo_en_moneda_extranjera_para_pases_pasivos_con_plazo_residu_233ad4
    - Restriccion_tasa_de_efectivo_minimo_en_moneda_extranjera_para_pases_pasivos_con_plazo_residu_3af087
    - Restriccion_tasa_de_efectivo_minimo_en_moneda_extranjera_para_pases_pasivos_con_plazo_residu_b04d83
    - Restriccion_tasa_de_efectivo_minimo_en_moneda_extranjera_para_pases_pasivos_con_plazo_residu_b98c85
    - Restriccion_tasa_de_efectivo_minimo_en_moneda_extranjera_para_pases_pasivos_con_plazo_residu_d10b85
    - Restriccion_tasa_de_efectivo_minimo_en_moneda_extranjera_para_pases_pasivos_con_plazo_residu_da29b0
    - Restriccion_tasa_de_efectivo_minimo_para_depositos_a_plazo_fijo_en_pesos_con_plazo_residual__03ebcf
    - Restriccion_tasa_de_efectivo_minimo_para_depositos_a_plazo_fijo_en_pesos_con_plazo_residual__660e76
    - Restriccion_tasa_de_efectivo_minimo_para_depositos_a_plazo_fijo_en_pesos_con_plazo_residual__8e9d18
    - Restriccion_tasa_de_efectivo_minimo_para_depositos_a_plazo_fijo_en_pesos_con_plazo_residual__c335c8
    - Restriccion_todo_deposito_que_no_se_ajuste_a_las_disposiciones_de_acondicionamiento_sera_rec_04f9a2
    - Restriccion_un_mismo_evento_de_perdida_no_podra_registrarse_en_mas_de_una_de_las_categorias__683b5a
```

### S12 — FAIL

ERROR — Toda Excepcion tiene >=1 arista saliente exceptua o exceptua_obligacion.

**Resultado:** 143 Excepciones sin salida exceptua/exceptua_obligacion.

```
    - Excepcion_alternativamente_podra_utilizarse_el_capital_minimo_basico_partida_70700000_cuan_044301
    - Excepcion_cuando_existe_saldo_acreedor_en_otros_resultados_integrales_acumulados_revaluaci_c564a3
    - Excepcion_cuando_la_actuacion_del_auditor_interino_no_exceda_de_un_ano_no_se_computa_a_los_c73c6e
    - Excepcion_cuando_la_auditoria_interna_se_delega_a_profesionales_independientes_el_responsa_ebf048
    - Excepcion_cuando_la_casa_matriz_y_todas_las_sucursales_esten_en_localidades_con_hasta_dos__0556d2
    - Excepcion_cuando_la_cuenta_se_cierra_por_decision_del_titular_la_entidad_no_esta_obligada__8aafff
    - Excepcion_cuando_no_se_disponga_de_la_calificacion_camels_de_la_sefyc_el_indice_de_correcc_960986
    - Excepcion_cuando_se_cumpla_la_condicion_de_localidades_con_hasta_dos_casas_operativas_se_a_37ff09
    - Excepcion_cuando_se_ha_designado_un_representante_legal_la_entrega_de_la_tarjeta_de_debito_8dec92
    - Excepcion_el_bcra_puede_considerar_excepcionalmente_solicitudes_de_ampliacion_estacional_q_b0a3ea
    - Excepcion_el_dictamen_favorable_puede_incluir_salvedades_o_excepciones_cuando_se_trate_de__1c3930
    - Excepcion_el_financiamiento_adicional_es_independiente_de_la_asistencia_en_operaciones_tot_7463d9
    - Excepcion_el_incremento_del_25_no_se_aplica_a_cajas_de_credito_cooperativas_en_categoria_i_1863fd
    - Excepcion_el_limite_previsto_en_el_punto_3_10_3_no_aplica_a_los_creditos_asociados_al_cobr_7afe59
    - Excepcion_el_limite_previsto_en_el_punto_3_10_3_no_aplica_a_los_creditos_por_cobro_de_depo_0eb5c3
    - Excepcion_el_sector_publico_no_financiero_queda_exceptuado_de_la_estimacion_del_deterioro__f9a2d6
    - Excepcion_el_superintendente_puede_determinar_excepciones_al_plazo_de_120_dias_para_la_pre_93eec3
    - Excepcion_en_caso_de_resultar_el_acreedor_o_sus_cesionarios_adquirentes_en_subasta_quedara_1388c6
    - Excepcion_en_depositos_a_plazo_fijo_de_uva_y_uvi_queda_excluido_del_computo_el_importe_dev_2a1095
    - Excepcion_en_el_caso_de_cobro_por_ventanilla_la_responsabilidad_de_emitir_la_cac_recae_en__70edd6
    - Excepcion_en_fusiones_que_no_deriven_en_constitucion_de_nueva_sociedad_la_inscripcion_podr_fa26ac
    - Excepcion_en_los_documentos_compensables_en_soporte_papel_la_responsabilidad_por_los_contr_e59a87
    - Excepcion_en_sucursales_de_entidades_financieras_extranjeras_el_comite_se_integra_con_dos__448935
    - Excepcion_excepcion_a_la_aplicacion_de_la_tasa_de_encaje_del_mes_anterior_para_depositos_e_c7e2d6
    - Excepcion_excepcion_a_la_ausencia_de_limites_de_importe_en_extracciones_por_cajeros_automa_293e37
    - Excepcion_excepcion_a_la_exigencia_de_que_la_carpeta_legal_este_anexa_al_legajo_del_client_d82671
    - Excepcion_excepcion_a_la_prohibicion_de_desafectacion_cuando_este_cubierto_el_100_de_las_a_3af56d
    - Excepcion_excepcion_a_la_prohibicion_de_generar_utilidades_cuando_se_constituyan_prevision_48457c
    - Excepcion_excepcion_a_la_restriccion_de_tenencia_de_cuotapartes_se_exceptuan_las_cuotapart_2b586b
    - Excepcion_excepcion_a_la_restriccion_de_tenencia_de_cuotapartes_se_exceptuan_las_cuotapart_5d97d6
    - Excepcion_excepcion_a_la_restriccion_de_tenencia_de_cuotapartes_se_exceptuan_las_cuotapart_7113e0
    - Excepcion_excepcion_a_la_restriccion_de_tenencia_de_cuotapartes_se_exceptuan_las_cuotapart_7518a9
    - Excepcion_excepcion_a_la_restriccion_de_tenencia_de_cuotapartes_se_exceptuan_las_cuotapart_ea48e9
    - Excepcion_excepcion_al_cierre_de_cuentas_por_decision_de_la_entidad_cuando_el_saldo_es_inf_37bb72
    - Excepcion_exclusion_de_facturas_no_ingresadas_a_la_compensacion_por_haber_sido_emitidas_en_3b9c74
    - Excepcion_exclusion_de_facturas_no_ingresadas_a_la_compensacion_por_haber_sido_pagadas_pre_e075d5
    - Excepcion_exclusion_de_facturas_no_ingresadas_a_la_compensacion_por_no_tener_declarada_una_d52f84
    - Excepcion_financiaciones_excluidas_del_computo_del_cupo_mipyme_minimo__efemin_6_3_2ba505
    - Excepcion_inhabilidad_de_personas_inhabilitadas_por_el_inciso_5_del_articulo_41_de_la_ley__42c80b
    - Excepcion_la_apertura_de_cuentas_especiales_de_regularizacion_de_activos_en_una_moneda_ext_4c0031
    - Excepcion_la_apertura_de_la_cuenta_no_se_condiciona_a_que_el_trabajador_posea_la_credencia_a8a0be
    - Excepcion_la_autorizacion_conferida_a_un_menor_para_operar_la_cuenta_cesa_automaticamente__bad087
    - Excepcion_la_autorizacion_no_implica_compromiso_alguno_para_aprobar_futuros_requerimientos_a61480
    - Excepcion_la_cuenta_se_abre_incluso_cuando_el_trabajador_no_posee_credencial_de_registro_l_ee1a47
    - Excepcion_la_debida_diligencia_especial_al_inicio_de_la_relacion_comercial_no_exime_del_de_6742b4
    - Excepcion_la_entrega_a_cualquiera_de_los_titulares_procede_incluso_en_caso_de_fallecimient_320cfc
    - Excepcion_la_evaluacion_de_la_capacidad_de_pago_incorporada_en_los_metodos_especificos_de__97c8a4
    - Excepcion_la_excepcion_a_la_obligacion_de_entrega_se_aplica_en_los_casos_de_cheque_falsifi_e3d634
    - Excepcion_la_excepcion_de_informacion_sobre_empresas_vinculadas_a_tenedores_del_5_o_mas_ap_8032fb
    - Excepcion_la_exigencia_de_capital_por_riesgo_de_mercado_no_se_aplica_a_las_cajas_de_credit_2a7902
    - Excepcion_la_limitacion_del_20_del_valor_nominal_a_un_mismo_sujeto_obligado_al_pago_no_ser_9978a9
    - Excepcion_la_maxima_posicion_neta_negativa_de_la_cuenta_puede_calcularse_luego_del_cierre__f5d8fa
    - Excepcion_la_obligacion_de_permanecer_en_la_categoria_irrecuperable_por_180_dias_aplica_in_a997f5
    - Excepcion_la_prohibicion_de_autorizacion_no_impide_la_adopcion_de_otras_medidas_conforme_a_ff91e7
    - Excepcion_la_responsabilidad_del_responsable_del_control_interno_por_incumplimientos_a_las_f22d97
    - Excepcion_las_actividades_que_involucren_atencion_de_clientes_y_publico_en_general_quedan__afcd2c
    - Excepcion_las_cajas_de_credito_cooperativas_solicitantes_quedan_exceptuadas_del_costo_de_e_dd51f9
    - Excepcion_las_disposiciones_de_estas_normas_no_se_aplican_a_las_operaciones_de_pases_que_l_ad04cb
    - Excepcion_las_disposiciones_sobre_cierre_de_cuentas_no_operativas_no_aplican_a_operaciones_f19238
    - Excepcion_las_entidades_financieras_publicas_cuyas_operaciones_esten_garantizadas_por_los__041460
    - Excepcion_las_entidades_pueden_prescindir_de_cumplir_con_todas_las_disposiciones_simultane_f16928
    - Excepcion_las_entidades_que_sean_sucursales_o_subsidiarias_de_entidades_g_sib_quedan_excep_6dddd1
    - Excepcion_las_existencias_deterioradas_menores_a_un_millar_completo_se_contemplan_unicamen_d93c37
    - Excepcion_las_facturas_de_credito_electronicas_mipyme_impugnadas_conforme_al_procedimiento_4f055f
    - Excepcion_las_facturas_impugnadas_conforme_a_lo_establecido_en_el_punto_anterior_quedan_ex_a6cd9b
    - Excepcion_las_financiaciones_garantizadas_a_favor_del_banco_central_de_la_republica_argent_62429e
    - Excepcion_las_funcionalidades_de_fraccionamiento_y_transmision_para_negociacion_quedan_exc_db8a08
    - Excepcion_las_garantias_otorgadas_por_sgr_o_fondos_de_garantia_de_caracter_publico_quedan__48b224
    - Excepcion_las_garantias_reales_constituidas_en_un_pais_distinto_al_del_deudor_inmediato_se_3043e8
    - Excepcion_las_normas_pertinentes_se_aplicaran_a_las_entidades_publicas_o_mixtas_solo_en_cu_78add4
    - Excepcion_las_nuevas_entidades_financieras_no_estan_obligadas_a_contar_con_la_calificacion_d3b1f2
    - Excepcion_las_obligaciones_con_comercios_por_las_ventas_realizadas_mediante_tarjetas_de_de_96d87b
    - Excepcion_las_obligaciones_con_el_banco_central_de_la_republica_argentina_bcra_quedan_excl_5ef90c
    - Excepcion_las_obligaciones_con_entidades_financieras_locales_quedan_exceptuadas_de_las_obl_6c2015
    - Excepcion_las_operaciones_de_corresponsalia_en_el_exterior_quedan_exceptuadas_de_las_oblig_feeb3f
    - Excepcion_las_operaciones_referidas_en_el_punto_5_1_5_que_superen_el_termino_de_6_meses_qu_2d5813
    - Excepcion_las_solicitudes_de_apertura_de_oficina_de_representacion_en_reemplazo_de_una_suc_24596e
    - Excepcion_los_anexos_al_legajo_del_cliente_pueden_estar_separados_fisicamente_si_se_cumple_03e726
    - Excepcion_los_anexos_al_legajo_del_cliente_pueden_estar_separados_fisicamente_siempre_que__3ea131
    - Excepcion_los_creditos_con_el_banco_central_de_la_republica_argentina_quedan_excluidos_del_7be9de
    - Excepcion_los_creditos_frente_al_banco_central_de_la_republica_argentina_quedan_excluidos__e34dbd
    - Excepcion_los_depositos_en_pesos_en_cuentas_de_los_pspocp_en_las_que_se_encuentren_deposit_4ab8f5
    - Excepcion_los_deudores_cuyas_financiaciones_estan_totalmente_cubiertas_con_garantias_prefe_f30433
    - Excepcion_los_intereses_y_primas_devengados_vencidos_o_a_vencer_quedan_excluidos_del_compu_34118b
    - Excepcion_los_limites_podrian_tolerarse_en_determinadas_circunstancias_que_se_los_supere_d_3e41e6
    - Excepcion_los_saldos_de_las_financiaciones_computadas_para_la_deduccion_del_40_conforme_al_a083ac
    - Excepcion_no_aplica_la_clasificacion_de_activos_financieros_segun_criterios_de_niif_9_cuan_08a9cd
    - Excepcion_no_aplica_la_estimacion_de_deterioro_al_sector_publico_no_financiero__ri_dcpc_7__ef0553
    - Excepcion_no_aplica_la_exclusion_de_titulos_de_credito_no_custodiados_cuando_su_registro_y_0b0827
    - Excepcion_no_aplica_la_obligacion_de_entrega_al_cliente_cuando_el_cheque_ha_sido_rechazado_bec139
    - Excepcion_no_aplica_la_prohibicion_de_informacion_a_inversores_cuando_los_recursos_del_fon_a2a2f2
    - Excepcion_no_es_necesaria_la_inscripcion_en_el_registro_publico_de_la_correspondiente_juri_9d80ed
    - Excepcion_no_es_obligatoria_la_evaluacion_de_capacidad_de_pago_en_funcion_de_ingresos_cuan_8de532
    - Excepcion_no_es_un_requerimiento_que_los_miembros_del_directorio_posean_conocimientos_tecn_bc6b5a
    - Excepcion_no_hay_limite_en_la_cantidad_de_adhesiones_al_sistema_de_debito_automatico_para__910da6
    - Excepcion_no_hay_limite_maximo_de_edad_para_los_solicitantes_salvo_el_que_surja_de_los_req_0cb7a4
    - Excepcion_no_se_computaran_las_exclusiones_establecidas_en_el_punto_1_2_de_las_normas_sobr_118106
    - Excepcion_no_se_excluyen_del_cupo_mipyme_minimo_las_mipyme_con_actividad_agricola_que_aunq_554241
    - Excepcion_no_se_exige_integracion_minima_diaria_para_depositos_en_titulos_valores_e_instru_3f4684
    - Excepcion_no_se_interrumpe_el_computo_de_los_plazos_que_la_arca_establezca_cuando_los_fond_73c178
    - Excepcion_no_se_interrumpe_el_computo_de_los_plazos_que_la_arca_establezca_cuando_se_verif_86277f
    - Excepcion_no_se_producira_novacion_y_se_conservara_con_todos_sus_efectos_el_origen_del_cre_7a732d
    - Excepcion_no_se_requiere_el_sello_de_la_casa_receptora_cuando_se_utilizan_escrituras_mecan_c42bad
    - Excepcion_no_se_requiere_remitir_la_nomina_cuando_los_datos_de_las_personas_ya_se_encuentr_af9d0a
    - Excepcion_no_sera_aplicable_el_regimen_de_traslados_contenido_en_el_punto_1_7_de_las_norma_0ecae7
    - Excepcion_no_sera_necesario_elaborar_reportes_para_los_sistemas_auxiliares_cuando_las_obli_dfe289
    - Excepcion_para_el_retiro_de_los_intereses_capitalizados_no_regira_la_disposicion_del_punto_8e7874
    - Excepcion_para_entidades_cuyas_acciones_se_encuentren_comprendidas_en_regimen_de_oferta_pu_785b5b
    - Excepcion_para_entidades_del_grupo_economico_bajo_supervision_consolidada_se_puede_optar_p_99cc2f
    - Excepcion_podran_distribuirse_utilidades_una_vez_alcanzado_el_20_del_capital_social_mas_el_2ba013
    - Excepcion_quedan_exceptuadas_de_la_clasificacion_y_medicion_a_costo_amortizado_las_operaci_d0d4e3
    - Excepcion_quedan_exceptuadas_de_las_restricciones_a_operaciones_activas_las_participacione_ca0e29
    - Excepcion_quedan_exceptuadas_de_las_restricciones_de_la_seccion_4_8_prohibiciones_los_sald_8cf7fd
    - Excepcion_quedan_exceptuadas_de_las_restricciones_de_operaciones_activas_la_tenencia_de_in_8b6678
    - Excepcion_quedan_exceptuadas_de_las_restricciones_sobre_operaciones_activas_las_operacione_7ef328
    - Excepcion_quedan_exceptuadas_del_fraccionamiento_del_credito_las_financiaciones_cubiertas__46255c
    - Excepcion_quedan_exceptuadas_las_exigencias_del_punto_2_9_2_que_no_sean_compatibles_con_la_90fd78
    - Excepcion_quedan_exceptuados_de_la_categoria_de_otras_obligaciones_a_plazo_los_depositos_c_96908e
    - Excepcion_quedan_exceptuados_de_la_clasificacion_como_irrecuperables_por_disposicion_tecni_76c0d3
    - Excepcion_quedan_exceptuados_de_la_deduccion_de_rpc_los_titulos_de_credito_cuyo_registro_y_12ce10
    - Excepcion_quedan_exceptuados_de_la_deduccion_de_titulos_de_credito_que_no_se_encuentren_en_997180
    - Excepcion_quedan_exceptuados_de_la_exposicion_como_activos_por_impuesto_diferido_los_impor_771a8e
    - Excepcion_quedan_exceptuados_de_la_integracion_de_la_exigencia_de_efectivo_minimo_los_depo_785309
    - Excepcion_quedan_exceptuados_de_la_prohibicion_de_limites_de_importe_los_limites_que_expre_4b0938
    - Excepcion_quedan_exceptuados_de_las_operaciones_admitidas_los_cajeros_automaticos_de_carga_66147f
    - Excepcion_quedan_exceptuados_del_ajuste_del_esquema_de_cobro_los_conceptos_que_deban_trasl_141f15
    - Excepcion_quedan_exceptuados_del_ajuste_del_esquema_de_cobro_los_servicios_adicionales_par_ec133c
    - Excepcion_quedan_excluidas_de_las_obligaciones_comprendidas_en_la_exigencia_de_efectivo_mi_6eb99d
    - Excepcion_quedan_excluidas_del_computo_de_obligaciones_a_la_vista_las_transferencias_del_e_89fec0
    - Excepcion_quedan_excluidas_del_computo_del_cupo_mipyme_minimo_las_financiaciones_a_mipymes_773d2f
    - Excepcion_quedan_excluidas_del_previsionamiento_las_garantias_avales_y_otros_compromisos_e_3951ed
    - Excepcion_quedan_excluidas_del_regimen_de_efectivo_minimo_las_obligaciones_por_compras_al__fc4385
    - Excepcion_quedan_excluidos_de_la_integracion_los_titulos_publicos_nacionales_en_pesos_vinc_f7888c
    - Excepcion_quedan_excluidos_los_defectos_de_aplicacion_que_se_originen_en_operaciones_de_ca_0103df
    - Excepcion_se_exceptua_el_ordenamiento_por_liquidez_exigibilidad_cuando_se_privilegia_la_na_5f5fac
    - Excepcion_se_exceptuan_las_asistencias_crediticias_relacionadas_con_actividades_de_servici_adc712
    - Excepcion_se_excluye_de_la_base_de_calculo_del_requerimiento_de_integracion_minima_diaria__5881b3
    - Excepcion_se_excluyen_de_la_identificacion_segun_moneda_de_origen_aquellas_partidas_que_no_d4cc99
    - Excepcion_se_excluyen_del_computo_de_la_posicion_global_neta_de_moneda_extranjera_los_conc_8e77e3
    - Excepcion_se_excluyen_los_bonos_vinculados_al_crecimiento_del_pbi_de_la_partida_titulos_pu_195f77
    - Excepcion_se_excluyen_los_derivados_contabilizados_en_partidas_fuera_de_balance_de_derivad_a9c3ff
    - Excepcion_se_suspende_el_requerimiento_de_integracion_minima_diaria_en_moneda_extranjera_a_a3ee06
    - Excepcion_subsistira_plenamente_el_derecho_real_de_hipoteca_incorporado_a_la_letra_en_gara_61637c
```

### S21 — WARN

INFORMATIVA — Coherencia de remisiones entre puntos (remite_a o referencia con rol_fuente=referencia_cruzada; scripts/remisiones.py): properties.destino sin el prefijo <to>:: pertenece al CONJUNTO {p.punto for p in provenances} del nodo destino; desglose por properties.alcance (las de alcance to_entero apuntan al TextoOrdenado y se cuentan como incoherentes por construcción del enunciado).

**Resultado:** 8838 remisiones ({'interna': 8539, 'externa': 272, 'to_entero': 27}); 27 incoherentes (por alcance: {'to_entero': 27}).

```
idx 2282: Condicion_no_haber_registrado_deficiencias_en_efectivo_minimo__no_haber_registrado_deficie_8dcc08 -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 2318: Condicion_no_registrar_incumplimientos_efectivo_minimo__condicion_de_que_no_se_registren_i_e3e818 -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 3919: Definicion_capacidades_de_agregacion_de_datos_sobre_riesgos__infraestructura_y_procesos_que_9bd90d -> TextoOrdenado_lingeef_pdf destino='lingeef::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.2.1', '1.2.2', '1.2.3']...
idx 4040: Definicion_codigo_100000_m_depositos_y_obligaciones__incluye_depositos_y_obligaciones_por_i_127313 -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 4080: Definicion_codigo_10145x_m_obligaciones_por_lineas_financieras_del_exterior__incluye_obliga_b6323e -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 4123: Definicion_codigo_10190x_001_cauciones_bursatiles_tomadoras__incluye_cauciones_bursatiles_t_1af4a2 -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 4165: Definicion_codigo_10206x_m_obligaciones_por_lineas_financieras_del_exterior_no_instrumentad_919e76 -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 4480: Definicion_codigos_10120x_m_11010x_m_y_110500_m_depositos_a_plazo_fijo_de_titulos__identifi_e0a405 -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 5463: Definicion_practicas_de_elaboracion_de_informes_de_riesgos__procesos_internos_mediante_los__b0fd97 -> TextoOrdenado_lingeef_pdf destino='lingeef::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.2.1', '1.2.2', '1.2.3']...
idx 7148: Obligacion_consignar_en_codigo_824000_001_el_incremento_en_la_exigencia_proveniente_del_aum_155daf -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 7170: Obligacion_consignar_promedio_mensual_de_saldos_diarios_de_depositos_y_obligaciones_que_ver_e943bc -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 14673: Obligacion_las_entidades_financieras_deberan_cumplir_la_condicion_de_no_haber_registrado_de_fd4352 -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 17688: Obligacion_reforzar_las_capacidades_de_agregacion_de_datos_sobre_riesgos_y_las_practicas_in_7ab0f9 -> TextoOrdenado_lingeef_pdf destino='lingeef::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.2.1', '1.2.2', '1.2.3']...
idx 17851: Obligacion_se_aplicaran_las_disposiciones_establecidas_en_la_materia_con_caracter_general_c_3bef9b -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 17914: Obligacion_se_consignaran_los_importes_admitidos_en_pesos_integrables_con_leliq_y_o_nobac_y_ec5447 -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 17918: Obligacion_se_consignaran_los_importes_admitidos_para_las_entidades_del_grupo_a_o_sucursale_f9894a -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 17922: Obligacion_se_consignaran_los_importes_admitidos_para_las_entidades_financieras_en_pesos_se_c8fce6 -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 18091: Obligacion_se_informara_el_saldo_promedio_acumulado_del_trimestre_bajo_informe_de_las_finan_2dbff9 -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 18097: Obligacion_se_informara_el_saldo_promedio_acumulado_del_trimestre_bajo_informe_de_las_finan_67ec8b -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 18105: Obligacion_se_informara_el_saldo_promedio_acumulado_del_trimestre_bajo_informe_de_las_finan_e30c50 -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 21067: Operacion_gestion_de_riesgos_en_entidades_financieras__adrei_1_2_634522 -> TextoOrdenado_lingeef_pdf destino='lingeef::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.2.1', '1.2.2', '1.2.3']...
idx 21491: Operacion_integracion_diaria_exigencia_minima__ri_rml_1_5_42a910 -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
idx 21781: Operacion_operaciones_de_cajas_de_credito_cooperativas__ayccef_1_1_2_dafc70 -> TextoOrdenado_cajasc_pdf destino='cajasc::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '1.2.4']...
idx 22978: Operacion_toma_de_decisiones_en_entidades_financieras__adrei_1_2_821a9b -> TextoOrdenado_lingeef_pdf destino='lingeef::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.2.1', '1.2.2', '1.2.3']...
idx 23739: Potestad_facultad_de_realizar_operaciones_cajas_de_credito_cooperativas__las_cajas_de_cre_7100c4 -> TextoOrdenado_cajasc_pdf destino='cajasc::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2.1', '1.2.2', '1.2.3', '1.2.4']...
idx 24050: Potestad_intensificar_supervision_y_requerir_capital_adicional__la_superintendencia_podra_a7c5c1 -> TextoOrdenado_lingeef_pdf destino='lingeef::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1', '1.2', '1.2.1', '1.2.2', '1.2.3']...
idx 27319: Restriccion_restriccion_de_que_la_integracion_en_bote_leliq_nobac_y_tpn_en_pesos_no_podra_ex_a7ac72 -> TextoOrdenado_efemin_pdf destino='efemin::TO' via='to_entero': punto 'TO' ∉ puntos del destino ['1.1.1.2', '1.1.2.1', '1.1.2.2', '1.1.2.3', '1.1.2.4']...
```

### S22 — PASS

INFORMATIVA — Coherencia de padre_sugerido: el destino de la arista es properties.padre_sugerido del origen y el origen está en cuarentena.

**Resultado:** 280 aristas padre_sugerido; 0 incoherentes (0 con destino distinto, 0 con origen fuera de cuarentena).

Sin violaciones.

### S23 — WARN

INFORMATIVA — aplica_a hacia sujetos en cuarentena: aristas aplica_a cuyo destino es un Sujeto de nivel propuesto (conteo; nunca bloqueante).

**Resultado:** 4233 aristas aplica_a; 687 hacia Sujetos propuestos (278 destinos distintos).

```
idx 6091: Excepcion_las_entidades_que_sean_sucursales_o_subsidiarias_de_entidades_g_sib_quedan_excep_6dddd1 -> Sujeto_propuesto_aquellas_entidades_que_revistan_el_caracter_de_sucursales_o_subsidiarias_de_enti
idx 6506: Obligacion_a_efectos_de_determinar_los_conceptos_computables_se_tomaran_como_referencia_las_d35f0f -> Sujeto_propuesto_las_entidades__ri_pgn
idx 6508: Obligacion_a_efectos_de_un_adecuado_analisis_y_documentacion_de_la_estructura_de_control_in_8bb18e -> Sujeto_propuesto_las_entidades__nmcief
idx 6533: Obligacion_a_fin_de_cada_mes_los_activos_se_mediran_de_acuerdo_con_la_categoria_que_poseian_f5d22d -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 6578: Obligacion_a_partir_del_01_01_2018_se_incluiran_en_el_codigo_20100_los_saldos_que_subsistan_3f5f2e -> Sujeto_propuesto_las_entidades__ri_pgn
idx 6609: Obligacion_actualizacion_de_relevamientos_minimo_anual__ri_ccna_d2a2_s3_24b7d7 -> Sujeto_propuesto_dicho_relevamiento
idx 6693: Obligacion_al_cierre_de_cada_mes_los_intereses_devengados_a_cobrar_se_imputaran_en_la_cuent_1bdb06 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 6696: Obligacion_al_cierre_de_cada_mes_los_intereses_devengados_a_pagar_se_imputaran_en_la_cuenta_db0a2d -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 6716: Obligacion_al_momento_de_la_liquidacion_de_las_operaciones_deberan_imputarlas_contra_la_cue_8fd3e5 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 6828: Obligacion_asegurar_que_tanto_los_procedimientos_como_los_controles_sean_adecuados_y_eficac_ee8cf9 -> Sujeto_propuesto_las_gerencias
idx 6902: Obligacion_cada_esquema_de_pago_debera_poner_a_disposicion_de_sus_participantes_un_servicio_39aa84 -> Sujeto_propuesto_cada_esquema_de_pago
idx 6906: Obligacion_cada_sistema_de_agregacion_de_datos_debe_especificar_con_claridad_el_enfoque_uti_ff8175 -> Sujeto_propuesto_cada_sistema_de_agregacion_de_datos
idx 6908: Obligacion_cada_sucursal_en_la_cec_que_le_preste_servicio_tendra_un_centro_de_transmision_a_440ecd -> Sujeto_propuesto_cada_una_de_estas_sucursales
idx 6917: Obligacion_calculo_de_activos_y_pasivos_por_impuesto_diferido_al_cierre_del_mes_comparando__18630c -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 6924: Obligacion_clasificacion_del_resultado_monetario_en_cuentas_620001_620002_o_620004_segun_or_0a00a8 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 6981: Obligacion_comunicacion_a_la_casa_operativa_de_la_cual_dependa_de_la_necesidad_de_requerir__c0758d -> Sujeto_propuesto_el_encargado_de_la_dependencia
idx 6989: Obligacion_comunicar_a_la_superintendencia_de_entidades_financieras_y_cambiarias_la_sustitu_f0a368 -> Sujeto_propuesto_las_cajas_de_credito
idx 7038: Obligacion_comunicar_de_inmediato_a_la_sefyc_las_sanciones_que_sean_impuestas_a_la_oficina__015ee4 -> Sujeto_propuesto_la_oficina
idx 7216: Obligacion_contenido_plan_auditoria_coordinacion_auditor_externo__nmcief_a2_s2_9e2131 -> Sujeto_propuesto_el_planeamiento_de_auditoria
idx 7218: Obligacion_contenido_plan_auditoria_evaluacion_riesgos__nmcief_a2_s2_c7da22 -> Sujeto_propuesto_el_planeamiento_de_auditoria
idx 7220: Obligacion_contenido_plan_auditoria_identificacion_riesgos__nmcief_a2_s2_498c31 -> Sujeto_propuesto_el_planeamiento_de_auditoria
idx 7222: Obligacion_contenido_plan_auditoria_procedimientos_sobre_ciclos_y_sucursales__nmcief_a2_s2_f751b4 -> Sujeto_propuesto_el_planeamiento_de_auditoria
idx 7224: Obligacion_contenido_plan_auditoria_recursos_necesarios__nmcief_a2_s2_c77ae7 -> Sujeto_propuesto_el_planeamiento_de_auditoria
idx 7237: Obligacion_convertir_otras_monedas_a_dolar_estadounidense__ri_pgn_s1_a5bdf4 -> Sujeto_propuesto_las_monedas_extranjeras_distintas_de_dolar_estadounidense
idx 7239: Obligacion_convertir_saldos_en_moneda_extranjera_diariamente__ri_pgn_s1_57ab63 -> Sujeto_propuesto_los_saldos_en_moneda_extranjera
idx 7243: Obligacion_corresponde_incluir_en_el_codigo_20100_el_importe_registrado_en_la_cuenta_340022_17c235 -> Sujeto_propuesto_las_entidades__ri_pgn
idx 7252: Obligacion_cuando_billetes_falsos_sean_detectados_en_operaciones_de_cajeros_automaticos_las_d3ac3b -> Sujeto_propuesto_las_entidades__cirmo3
idx 7274: Obligacion_cuando_corresponda_formular_salvedad_por_falta_de_uniformidad_respecto_a_pautas__40ef93 -> Sujeto_propuesto_el_auditor_externo
idx 7295: Obligacion_cuando_el_cliente_formaliza_su_adhesion_al_servicio_de_debito_automatico_a_trave_fdbcdb -> Sujeto_propuesto_la_empresa_o_ente
idx 7386: Obligacion_cuando_existan_saldos_disponibles_en_la_cuenta_al_momento_del_cierre_los_fondos__30d9a2 -> Sujeto_propuesto_los_fondos
idx 7393: Obligacion_cuando_hay_imposibilidad_de_cuantificar_razonablemente_los_montos_correspondient_db86d9 -> Sujeto_propuesto_el_auditor_externo
idx 7437: Obligacion_cuando_la_entidad_opte_por_recurrir_al_servicio_de_terceros_en_materia_de_tecnol_f4781b -> Sujeto_propuesto_el_proveedor_o_los_proveedores_que_se_contraten
idx 7450: Obligacion_cuando_las_cuentas_de_deposito_de_garantias_sean_utilizadas_exclusivamente_para__a3dd53 -> Sujeto_propuesto_mercados_o_camaras_compensadoras_de_capitales
idx 7456: Obligacion_cuando_los_titulares_cancelen_compras_realizadas_a_personas_humanas_y_juridicas__a6dfcf -> Sujeto_propuesto_los_titulares
idx 7569: Obligacion_cuando_sea_factible_o_recomendable_la_comunicacion_con_el_deudor_debe_incluir_en_ef8353 -> Sujeto_propuesto_la_comunicacion_con_el_deudor
idx 7578: Obligacion_cuando_un_campo_alfanumerico_posea_mas_caracteres_de_los_requeridos_para_la_info_9064a6 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 7592: Obligacion_cuando_un_campo_numerico_posea_mas_caracteres_de_los_requeridos_para_la_informac_59249c -> Sujeto_propuesto_las_entidades__snp_cheq
idx 7603: Obligacion_cuando_una_operacion_o_situacion_cuya_imputacion_no_este_prevista_en_el_plan_de__565d65 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 7608: Obligacion_cumplimiento_de_la_medida_de_tenencia_de_certificado_de_aptitud_en_cajas_de_aten_33fb0a -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 7637: Obligacion_dar_cumplimiento_a_los_requisitos_establecidos_en_el_punto_1_3_9__cajasc_1_3_10_cadfb0 -> Sujeto_propuesto_los_asociados
idx 7659: Obligacion_de_persistir_un_exceso_positivo_despues_de_la_atenuacion_el_cargo_a_ingresar_se__76015b -> Sujeto_propuesto_las_entidades__ri_pgn
idx 7669: Obligacion_debe_adjuntarse_a_la_nota_el_descargo_del_presentante_explicando_como_se_produjo_68376e -> Sujeto_propuesto_transportadoras_de_valores
idx 7748: Obligacion_debe_identificarse_en_el_archivo_a_transmitir_la_informacion_del_cedip_al_cual_c_900c20 -> Sujeto_propuesto_la_entidad__snp_cheq
idx 7862: Obligacion_deber_de_computar_los_conceptos_comprendidos_en_la_exigencia_de_capital_por_ries_b37b6f -> Sujeto_propuesto_los_conceptos_comprendidos
idx 7925: Obligacion_deber_de_incluir_datos_de_transferencias_para_clientes_receptores_y_ordenantes_e_b23fba -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 7928: Obligacion_deber_de_incluir_en_las_devoluciones_de_pago_con_transferencia_la_descripcion_de_98ecaf -> Sujeto_propuesto_las_entidades__snp_tr
idx 7937: Obligacion_deber_de_informar_al_bcra_sobre_la_retencion_de_billetes_y_o_monedas_argentinas__a24f02 -> Sujeto_propuesto_transportadoras_de_valores
idx 7942: Obligacion_deber_de_informar_la_exposicion_neta_de_crc_admisibles_conforme_a_lo_dispuesto_e_d5ba57 -> Sujeto_propuesto_las_entidades
idx 7944: Obligacion_deber_de_informar_la_posicion_global_neta_de_moneda_extranjera_de_cada_uno_de_lo_35913b -> Sujeto_propuesto_las_entidades__ri_pgn
idx 7968: Obligacion_deber_de_informar_la_totalidad_de_las_prefinanciaciones_y_financiaciones_de_expo_9022c6 -> Sujeto_propuesto_las_entidades__ri_rml
idx 7971: Obligacion_deber_de_informar_las_financiaciones_a_clientes_que_cuenten_con_garantias_en_mon_b81421 -> Sujeto_propuesto_las_entidades__ri_rml
idx 7974: Obligacion_deber_de_informar_las_financiaciones_a_prestadores_de_servicios_a_ser_exportados_8b1ce7 -> Sujeto_propuesto_las_entidades__ri_rml
idx 7977: Obligacion_deber_de_informar_las_financiaciones_a_productores_de_bienes_para_ser_exportados_4ac1a3 -> Sujeto_propuesto_las_entidades__ri_rml
idx 7980: Obligacion_deber_de_informar_las_financiaciones_a_productores_procesadores_o_acopiadores_de_51cc47 -> Sujeto_propuesto_las_entidades__ri_rml
idx 7983: Obligacion_deber_de_informar_las_financiaciones_a_proveedores_de_bienes_y_o_servicios_produ_740bbb -> Sujeto_propuesto_las_entidades__ri_rml
idx 7986: Obligacion_deber_de_informar_las_financiaciones_a_proveedores_de_servicios_de_exportacion___f5995c -> Sujeto_propuesto_las_entidades__ri_rml
idx 7989: Obligacion_deber_de_informar_las_financiaciones_de_importaciones_temporarias_vinculadas_a_e_b4bda8 -> Sujeto_propuesto_las_entidades__ri_rml
idx 7992: Obligacion_deber_de_informar_las_financiaciones_de_inversion_y_capital_de_trabajo_exportado_cb7d9e -> Sujeto_propuesto_las_entidades__ri_rml
idx 7998: Obligacion_deber_de_informar_las_posiciones_de_cada_uno_de_los_dias_del_mes_bajo_informe_in_bdabd7 -> Sujeto_propuesto_las_entidades__ri_pgn
idx 8003: Obligacion_deber_de_informar_los_depositos_a_la_vista_y_a_plazo_en_moneda_extranjera_y_sus__d194d8 -> Sujeto_propuesto_las_entidades__ri_rml
idx 8013: Obligacion_deber_de_informar_otras_financiaciones_a_exportadores__ri_rml_3_2_98368f -> Sujeto_propuesto_las_entidades__ri_rml
idx 8040: Obligacion_deber_de_practicar_el_procedimiento_de_aplicacion_inicial_conforme_a_seccion_7_d_f966db -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 8046: Obligacion_deber_de_presentar_declaracion_jurada_en_la_que_se_manifieste_que_no_se_encuentr_8ba8c3 -> Sujeto_propuesto_cada_uno_de_los_accionistas_e_integrantes_de_los_organos_de_gobierno_accionistas
idx 8049: Obligacion_deber_de_prestar_declaracion_jurada_sobre_conocimiento_de_disposiciones_y_sancio_b02194 -> Sujeto_propuesto_el_publico_en_general
idx 8057: Obligacion_deber_de_realizar_la_resolucion_de_cada_transferencia_inmediata_en_no_mas_de_15__0c9c96 -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 8091: Obligacion_deber_de_retener_los_billetes_y_o_monedas_argentinas_y_dolares_estadounidenses_p_eef29c -> Sujeto_propuesto_transportadoras_de_valores
idx 8093: Obligacion_deber_de_retirar_de_circulacion_y_remitir_al_bcra_para_su_canje_y_o_anulacion_y__5c54c4 -> Sujeto_propuesto_corresponde
idx 8095: Obligacion_deber_de_revender_las_posiciones_compradas_para_crear_mercado_dentro_de_un_perio_9c4116 -> Sujeto_propuesto_las_posiciones_compradas_para_crear_mercado
idx 8100: Obligacion_deber_de_satisfacer_los_requisitos_tecnico_operativos_de_seguridad_establecidos__3ea47e -> Sujeto_propuesto_los_sujetos_obligados
idx 8119: Obligacion_deber_de_verificar_que_un_cheque_cancelatorio_no_tenga_impedimento_de_pago_y_la__5237f6 -> Sujeto_propuesto_los_certificantes
idx 8120: Obligacion_deber_de_verificar_que_un_cheque_cancelatorio_no_tenga_impedimento_de_pago_y_la__5237f6 -> Sujeto_propuesto_los_tenedores_legitimados
idx 8191: Obligacion_debera_tenerse_en_cuenta_el_plan_de_cuentas_minimo_para_el_registro_de_las_opera_158fd2 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 8217: Obligacion_deberan_informar_el_numero_de_codigo_interno_asignado_al_sistema_de_monitoreo_re_d1d10c -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 8245: Obligacion_demostrar_que_poseen_la_solvencia_y_liquidez_adecuadas_para_efectivizar_los_apor_e6c38f -> Sujeto_propuesto_los_asociados
idx 8431: Obligacion_efectuar_la_reexpresion_de_la_informacion_contable_en_moneda_homogenea_con_frecu_026d1f -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 8443: Obligacion_el_aceptador_dentro_de_un_esquema_de_transferencias_inmediatas_debe_tomar_los_re_bf0c3c -> Sujeto_propuesto_aceptador_dentro_de_un_esquema_de_transferencias_inmediatas
idx 8453: Obligacion_el_activo_subyacente_se_reclasificara_a_las_cuentas_otros_creditos_por_intermedi_d49aab -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 8467: Obligacion_el_administrador_debe_cobrar_las_indemnizaciones_por_vida_correspondientes_y_apl_e55e24 -> Sujeto_propuesto_el_administrador
idx 8481: Obligacion_el_administrador_debe_controlar_y_supervisar_el_proceso_de_expropiacion_de_la_pr_01f74e -> Sujeto_propuesto_el_administrador
idx 8489: Obligacion_el_administrador_debe_determinar_el_cumplimiento_de_las_condiciones_para_efectua_3293ea -> Sujeto_propuesto_el_administrador
idx 8496: Obligacion_el_administrador_debe_efectuar_el_seguimiento_y_regularizacion_de_la_mora_de_acu_781a7d -> Sujeto_propuesto_el_administrador
idx 8504: Obligacion_el_administrador_debe_efectuar_las_modificaciones_a_los_terminos_y_condiciones_d_7269e4 -> Sujeto_propuesto_el_administrador
idx 8513: Obligacion_el_administrador_debe_efectuar_un_seguimiento_de_los_seguros_contratados_a_fin_d_9d2be9 -> Sujeto_propuesto_el_administrador
idx 8530: Obligacion_el_administrador_debe_informar_con_anticipacion_razonable_a_la_fecha_de_vencimie_a9e132 -> Sujeto_propuesto_el_administrador
idx 8538: Obligacion_el_administrador_debe_iniciar_los_tramites_de_ejecucion_prendaria_cuando_las_act_e3fd48 -> Sujeto_propuesto_el_administrador
idx 8544: Obligacion_el_administrador_debe_mantener_permanentemente_actualizados_los_datos_relativos__195bcd -> Sujeto_propuesto_el_administrador
idx 8560: Obligacion_el_administrador_debe_recibir_e_imputar_los_pagos_que_efectuen_los_deudores__man_1b918a -> Sujeto_propuesto_el_administrador
idx 8572: Obligacion_el_administrador_del_sca_debe_disponibilizar_a_traves_de_las_entidades_una_consu_e03693 -> Sujeto_propuesto_el_administrador_del_sca
idx 8593: Obligacion_el_apoderado_o_representante_legal_debe_contar_con_poder_o_facultades_suficiente_641c89 -> Sujeto_propuesto_el_apoderado_o_representante_legal
idx 8603: Obligacion_el_auditor_debe_hacer_referencia_en_su_dictamen_a_las_notas_y_determinar_cual_es_38c9a5 -> Sujeto_propuesto_el_auditor
idx 8616: Obligacion_el_auditor_externo_asume_el_compromiso_de_informar_cualquier_modificacion_que_se_ea4775 -> Sujeto_propuesto_auditor_externo
idx 8618: Obligacion_el_auditor_externo_de_la_caja_de_credito_declara_conocer_y_aceptar_que_por_ejerc_68314b -> Sujeto_propuesto_auditor_externo_de_la_entidad
idx 8620: Obligacion_el_auditor_externo_debe_conservar_en_su_poder_los_papeles_de_trabajo_como_eviden_0fa29d -> Sujeto_propuesto_el_profesional_interviniente
idx 8631: Obligacion_el_auditor_externo_debe_enviar_una_carta_dirigida_a_la_entidad_informando_acerca_f5b24d -> Sujeto_propuesto_el_auditor_externo
idx 8669: Obligacion_el_auditor_externo_designado_de_acuerdo_con_las_disposiciones_del_anexo_i_debera_bb232e -> Sujeto_propuesto_el_auditor_externo
idx 8674: Obligacion_el_auditor_interno_determinara_la_naturaleza_y_alcance_de_los_procedimientos_sus_1d8d89 -> Sujeto_propuesto_el_auditor_interno
idx 8688: Obligacion_el_bcra_debe_dar_cumplimiento_sin_cargo_a_todos_los_pedidos_de_envio_de_monedas__5317a1 -> Sujeto_propuesto_las_casas_centrales_de_las_entidades
idx 8853: Obligacion_el_contrato_debe_especificar_la_forma_en_que_la_agencia_respondera_ante_la_entid_123f2e -> Sujeto_propuesto_la_agencia
idx 8855: Obligacion_el_contrato_debe_identificar_los_riesgos_asociados_a_la_prestacion_de_los_servic_567fed -> Sujeto_propuesto_la_agencia_complementaria_de_servicios_financieros
idx 8901: Obligacion_el_convenio_que_formaliza_la_apertura_de_cuentas_en_el_marco_de_acuerdos_con_otr_9156a7 -> Sujeto_propuesto_la_entidad_autorizante
idx 8912: Obligacion_el_declarante_debe_declarar_bajo_juramento_que_los_datos_consignados_en_la_formu_9e6b9f -> Sujeto_propuesto_el_declarante
idx 9045: Obligacion_el_diferimiento_de_la_sesion_de_presentados_debera_ser_comunicado_a_las_entidade_853959 -> Sujeto_propuesto_sus_entidades_miembros
idx 9386: Obligacion_el_diseno_de_escenarios_prospectivos_requiere_combinar_el_conocimiento_y_el_juic_98f196 -> Sujeto_propuesto_el_diseno_de_esos_escenarios
idx 9402: Obligacion_el_encargado_de_la_dependencia_tendra_la_responsabilidad_primaria_de_mantener_en_096349 -> Sujeto_propuesto_el_encargado_de_la_dependencia
idx 9410: Obligacion_el_gerente_de_la_sucursal_administradora_sera_responsable_de_la_actividad_y_dese_cb0191 -> Sujeto_propuesto_el_gerente_de_la_sucursal_administradora
idx 9412: Obligacion_el_grupo_y_la_entidad_deben_mantener_capacidad_de_recuperacion_ante_eventos_de_e_1182cb -> Sujeto_propuesto_tanto_el_grupo_como_la_entidad
idx 9424: Obligacion_el_importe_a_computar_como_atenuacion_del_incumplimiento_entre_febrero_y_abril_2_cfa5af -> Sujeto_propuesto_esta_institucion
idx 9427: Obligacion_el_importe_positivo_de_la_diferencia_se_registrara_en_su_totalidad_en_las_cuenta_687a93 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 9514: Obligacion_el_informe_sobre_los_estados_contables_al_cierre_del_ejercicio_debe_contener_com_6dbebf -> Sujeto_propuesto_el_auditor
idx 9545: Obligacion_el_marco_de_gestion_del_riesgo_operacional_debe_ser_aplicado_en_forma_consistent_3dd8d9 -> Sujeto_propuesto_todos_los_niveles_de_la_organizacion
idx 9571: Obligacion_el_memorandum_debe_ser_enviado_con_treinta_30_dias_corridos_de_anticipacion_al_c_f4b8e5 -> Sujeto_propuesto_el_auditor_externo
idx 9581: Obligacion_el_metodo_de_participacion_para_subsidiarias_asociadas_y_negocios_conjuntos_se_a_e6aba3 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 9720: Obligacion_el_plan_debe_ser_revisado_regularmente_y_actualizado_para_asegurar_que_es_operac_beceac -> Sujeto_propuesto_el_plan
idx 9723: Obligacion_el_planeamiento_de_auditoria_debe_contener_referencias_a_las_tareas_de_evaluacio_e7c339 -> Sujeto_propuesto_el_responsable_del_control_interno
idx 9735: Obligacion_el_presentante_interesado_debe_demostrar_lo_contrario_mediante_gestion_ante_la_e_6feab6 -> Sujeto_propuesto_el_interesado_presentante
idx 9737: Obligacion_el_prestamo_debe_ser_garantizado_con_una_prenda_en_primer_grado_sobre_el_automot_de7761 -> Sujeto_propuesto_el_prestamo
idx 9764: Obligacion_el_proceso_de_recoleccion_de_datos_debe_ser_acompanado_de_una_politica_de_incent_c1808b -> Sujeto_propuesto_el_proceso_de_recoleccion_de_datos
idx 9766: Obligacion_el_proceso_de_revision_y_aprobacion_debe_asegurar_que_se_ha_realizado_la_inversi_040e0c -> Sujeto_propuesto_el_proceso_de_revision_y_aprobacion
idx 9778: Obligacion_el_programa_de_pruebas_de_estres_debe_estar_documentado_en_forma_apropiada_en_es_b8290f -> Sujeto_propuesto_el_programa_de_pruebas_de_estres
idx 9781: Obligacion_el_programa_de_pruebas_de_estres_para_el_rtici_debe_garantizar_que_las_opiniones_ee4c23 -> Sujeto_propuesto_el_programa_de_pruebas_de_estres_para_el_rtici
idx 9822: Obligacion_el_representante_legal_debe_manifestar_mediante_nota_con_caracter_de_declaracion_0f00d0 -> Sujeto_propuesto_el_representante_legal_de_la_entidad
idx 9824: Obligacion_el_representante_legal_debe_manifestar_mediante_nota_con_caracter_de_declaracion_c8b520 -> Sujeto_propuesto_el_representante_legal_de_la_entidad__ayccef
idx 9827: Obligacion_el_responsable_de_datos_de_la_unidad_de_negocio_debe_asegurarse_de_que_los_datos_a9920c -> Sujeto_propuesto_el_responsable_de_datos_de_la_unidad_de_negocio
idx 9829: Obligacion_el_responsable_de_datos_de_la_unidad_de_negocio_debe_tomar_los_recaudos_suficien_316800 -> Sujeto_propuesto_el_responsable_de_datos_de_la_unidad_de_negocio
idx 9831: Obligacion_el_responsable_de_la_auditoria_interna_debera_remitir_al_comite_de_auditoria_los_d0cafa -> Sujeto_propuesto_el_responsable_de_la_auditoria_interna_de_la_entidad
idx 9837: Obligacion_el_responsable_del_control_interno_debe_presentar_el_planeamiento_anual_de_sus_a_c17d66 -> Sujeto_propuesto_el_responsable_del_control_interno
idx 9861: Obligacion_el_saldo_imputado_en_la_reserva_normativa_especial_debera_mantenerse_hasta_tanto_7a59ff -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 9863: Obligacion_el_servicio_de_transferencias_inmediatas_debe_mantener_una_disponibilidad_operat_59fdaf -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 9915: Obligacion_el_socio_responsable_asume_identica_responsabilidad_que_el_auditor_externo_desig_58091a -> Sujeto_propuesto_el_sr
idx 9923: Obligacion_el_socio_responsable_se_constituye_en_fiador_solidario_con_expresa_renuncia_a_lo_de3d7f -> Sujeto_propuesto_el_sr
idx 9935: Obligacion_el_tenedor_debe_presentar_el_chc_para_su_cobro_en_la_entidad_donde_tiene_cuenta__a50681 -> Sujeto_propuesto_el_tenedor
idx 9965: Obligacion_elaborar_informacion_a_nivel_casa_central_y_filiales__ri_pgn_s1_da0114 -> Sujeto_propuesto_esta_informacion
idx 9977: Obligacion_en_baja_de_activos_no_monetarios_recalcular_resultado_considerando_saldo_inicial_eab268 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 10018: Obligacion_en_caso_de_que_una_entidad_financiera_que_presenta_informacion_consolidada_haya__4f1f04 -> Sujeto_propuesto_el_mencionado_auditor_interno
idx 10025: Obligacion_en_caso_de_siniestros_debe_adjuntarse_la_denuncia_policial_correspondiente_a_la__de6cab -> Sujeto_propuesto_transportadoras_de_valores
idx 10040: Obligacion_en_cualquier_caso_las_entidades_deben_identificar_en_el_archivo_a_transmitir_la__871bfa -> Sujeto_propuesto_las_entidades__snp_cheq
idx 10042: Obligacion_en_cualquier_caso_las_entidades_deberan_identificar_en_el_archivo_a_transmitir_l_d9f715 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 10049: Obligacion_en_el_caso_de_las_entidades_mas_sofisticadas_la_evaluacion_de_la_suficiencia_del_f32892 -> Sujeto_propuesto_las_entidades_mas_sofisticadas
idx 10054: Obligacion_en_el_caso_de_siniestro_el_administrador_debe_efectuar_los_reclamos_pertinentes__2e1305 -> Sujeto_propuesto_el_administrador
idx 10066: Obligacion_en_el_codigo_903200_001_exigencia_del_mes_sobre_depositos_y_obligaciones_a_plazo_f423e0 -> Sujeto_propuesto_las_entidades__ri_rml
idx 10117: Obligacion_en_el_codigo_903200_m_se_deberan_incluir_las_partidas_101450_m_y_10145x_m_corres_f0cc79 -> Sujeto_propuesto_las_entidades__ri_rml
idx 10158: Obligacion_en_el_estado_de_cambios_del_patrimonio_neto_se_reexpresaran_en_moneda_de_cierre__842f8f -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 10161: Obligacion_en_el_estado_de_flujo_de_efectivo_se_reexpresaran_en_moneda_de_cierre_los_saldos_26ce65 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 10166: Obligacion_en_el_libro_especial_de_control_interno_deben_transcribirse_los_informes_de_cont_42f9ab -> Sujeto_propuesto_la_entidad
idx 10196: Obligacion_en_la_cec_que_le_preste_servicio_cada_sucursal_debera_estar_asignada_a_un_centro_24a26e -> Sujeto_propuesto_cada_una_de_estas_sucursales__snp_cheq
idx 10260: Obligacion_en_las_cuentas_de_partidas_fuera_de_balance_se_mostraran_al_cierre_de_cada_mes_l_604171 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 10263: Obligacion_en_las_sociedades_anonimas_los_directores_deberan_continuar_en_funciones_durante_2651cd -> Sujeto_propuesto_las_sociedades_anonimas
idx 10268: Obligacion_en_los_casos_de_cheques_librados_al_portador_o_a_favor_de_una_persona_determinad_f567e0 -> Sujeto_propuesto_su_beneficiario
idx 10271: Obligacion_en_los_casos_de_motivos_de_rechazo_o_en_caso_de_vuelta_atras_de_una_cec_unwindin_2d6256 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 10346: Obligacion_en_sesion_de_presentados_las_entidades_deberan_presentar_la_totalidad_de_registr_0050c6 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 10349: Obligacion_en_sesion_de_presentados_las_entidades_deberan_presentar_los_eventuales_ajustes__b60e8d -> Sujeto_propuesto_las_entidades__snp_cheq
idx 10352: Obligacion_en_sesion_de_presentados_las_entidades_deberan_presentar_rechazos_fuera_de_canje_3fe871 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 10355: Obligacion_en_sesion_de_presentados_las_entidades_deberan_presentar_reclamos__snp_cheq_3_1__808f2d -> Sujeto_propuesto_las_entidades__snp_cheq
idx 10358: Obligacion_en_sesion_de_rechazados_las_entidades_deberan_presentar_rechazos_de_las_entidade_154c40 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 10361: Obligacion_en_sesion_de_rechazados_las_entidades_deberan_presentar_rechazos_de_reclamos_sob_3d3d61 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 10364: Obligacion_en_sesion_de_rechazados_las_entidades_deberan_presentar_rechazos_por_defectos_ve_5b408b -> Sujeto_propuesto_las_entidades__snp_cheq
idx 10367: Obligacion_en_sesion_de_rechazados_las_entidades_deberan_presentar_respuestas_de_rechazos_f_b00ff2 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 10383: Obligacion_enajenantes_y_adquirentes_de_acciones_estan_obligados_a_informar_a_la_sefyc_cual_9fcc9e -> Sujeto_propuesto_enajenantes_y_adquirentes_de_acciones
idx 10435: Obligacion_enviar_memorandum_con_frecuencia_minima_anual__ri_ccna_d1a4_s2_2070b0 -> Sujeto_propuesto_el_auditor_externo
idx 10462: Obligacion_es_fundamental_la_adecuada_documentacion_de_los_controles_de_las_aplicaciones_pa_432aab -> Sujeto_propuesto_la_auditoria_interna
idx 10520: Obligacion_evaluar_el_proceso_de_control_sobre_la_gestion_de_las_areas_de_seguridad_de_la_i_d2d57b -> Sujeto_propuesto_la_auditoria_interna
idx 10526: Obligacion_evaluar_el_proceso_de_gestion_que_permita_solicitar_aprobar_asignar_modificar_mo_0e7f65 -> Sujeto_propuesto_la_auditoria_interna
idx 10533: Obligacion_evaluar_la_implementacion_de_medidas_para_mantener_el_control_sobre_las_cuentas__4bcf6d -> Sujeto_propuesto_la_auditoria_interna
idx 10547: Obligacion_evaluar_normas_y_procedimientos_del_marco_normativo_para_gestionar_controlar_y_d_7598f6 -> Sujeto_propuesto_la_auditoria_interna
idx 10568: Obligacion_existen_ciertos_criterios_basicos_que_deben_seguirse_para_todas_las_exposiciones_34a593 -> Sujeto_propuesto_todas_las_exposiciones_significativas
idx 10574: Obligacion_expresar_importes_en_miles_de_pesos_sin_decimales__ri_pgn_s1_2e20b6 -> Sujeto_propuesto_los_importes
idx 10614: Obligacion_identificacion_de_las_exposiciones_que_dan_origen_a_los_excesos_a_los_limites_pr_36bf27 -> Sujeto_propuesto_las_entidades
idx 10662: Obligacion_importe_de_impuesto_diferido_a_imputar_en_impuesto_a_las_ganancias_surge_de_comp_9df236 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 10697: Obligacion_indicar_los_bienes_que_realizara_para_obtener_los_montos_necesarios_para_complet_747d53 -> Sujeto_propuesto_el_asociado
idx 10707: Obligacion_informar_a_la_unidad_de_riesgo_operacional_o_persona_responsable_acerca_de_los_r_96869b -> Sujeto_propuesto_las_gerencias
idx 10742: Obligacion_informar_el_cumplimiento_de_la_medida_de_alarma_local_de_acuerdo_con_los_paramet_216f93 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10745: Obligacion_informar_el_cumplimiento_de_la_medida_de_barreras_visuales_frontales_en_cajas_de_ca3d2e -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10748: Obligacion_informar_el_cumplimiento_de_la_medida_de_cerramiento_en_lineas_de_cajas_de_atenc_fae4fb -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10750: Obligacion_informar_el_cumplimiento_de_la_medida_de_grabador_digital_de_video_segun_los_par_857453 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10753: Obligacion_informar_el_cumplimiento_de_la_medida_de_mamparas_laterales_segun_los_parametros_756003 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10756: Obligacion_informar_el_cumplimiento_de_la_medida_de_puerta_de_acceso_blindada_en_recinto_de_61de73 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10759: Obligacion_informar_el_cumplimiento_de_la_medida_de_puerta_de_doble_chapa_en_cajas_de_atenc_e0281f -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10762: Obligacion_informar_el_cumplimiento_de_la_medida_de_pulsador_de_alarma_segun_los_parametros_07c799 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10765: Obligacion_informar_el_cumplimiento_de_la_medida_de_tenencia_de_certificado_de_aptitud_para_f7dfb7 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10767: Obligacion_informar_el_cumplimiento_de_la_medida_de_ubicacion_de_las_camaras_de_cctv_segun__9a4083 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10769: Obligacion_informar_el_cumplimiento_de_la_medida_de_ups_o_red_alternativa_de_alimentacion_e_3986ef -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10771: Obligacion_informar_el_cumplimiento_de_la_medida_minima_de_seguridad_consistente_en_pulsado_fe96f9 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10774: Obligacion_informar_el_cumplimiento_de_las_medidas_minimas_de_seguridad_de_acuerdo_con_los__b742e8 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10777: Obligacion_informar_el_cumplimiento_de_las_medidas_minimas_de_seguridad_respecto_de_segurid_494e2d -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10842: Obligacion_informar_sobre_la_tenencia_de_certificado_de_aptitud_como_medida_minima_de_segur_cfde6f -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 10844: Obligacion_informar_sobre_los_tramites_realizados_o_a_realizar_para_capitalizacion_de_aport_19d799 -> Sujeto_propuesto_el_asociado
idx 10861: Obligacion_informe_por_unica_vez_con_los_datos_de_agosto_de_2018_de_la_posicion_en_letras_d_cf9a5a -> Sujeto_propuesto_las_entidades__ri_pgn
idx 10863: Obligacion_informe_por_unica_vez_con_los_datos_de_mayo_de_2019_de_la_posicion_en_letras_del_2e9d23 -> Sujeto_propuesto_las_entidades__ri_pgn
idx 10873: Obligacion_integracion_de_importes_de_efectivo_minimo_aplicando_la_tasa_del_3_5_para_entida_b7ae35 -> Sujeto_propuesto_sucursales_o_subsidiarias_de_bancos_del_exterior_calificados_como_sistematicamen
idx 10898: Obligacion_la_aceptacion_de_la_autorizacion_conferida_al_menor_debera_ser_ejercida_a_traves_2443bf -> Sujeto_propuesto_su_representante_legal
idx 10906: Obligacion_la_agencia_complementaria_de_servicios_financieros_debe_cumplir_con_las_regulaci_2456c7 -> Sujeto_propuesto_la_agencia_complementaria_de_servicios_financieros
idx 10916: Obligacion_la_agencia_complementaria_de_servicios_financieros_debe_mantener_a_disposicion_d_642c8d -> Sujeto_propuesto_la_agencia_complementaria_de_servicios_financieros
idx 11074: Obligacion_la_ampliacion_temporal_de_limites_debe_contemplarse_especificamente_para_el_pago_9e30bd -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 11076: Obligacion_la_ampliacion_temporal_de_limites_para_realizar_transferencias_debe_encontrarse__6776fa -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 11078: Obligacion_la_aprobacion_debe_realizarse_de_acuerdo_con_pautas_escritas_y_aprobadas_por_el__0d29f2 -> Sujeto_propuesto_la_aprobacion
idx 11087: Obligacion_la_atenuacion_determinada_conforme_a_lo_indicado_precedentemente_se_detraera_del_aa7d82 -> Sujeto_propuesto_las_entidades__ri_pgn
idx 11089: Obligacion_la_atenuacion_determinada_conforme_al_punto_3_se_detraera_del_exceso_al_limite_g_7521b8 -> Sujeto_propuesto_las_entidades__ri_pgn
idx 11094: Obligacion_la_auditoria_interna_debe_considerar_los_riesgos_involucrados_y_la_naturaleza_de_fbc2f4 -> Sujeto_propuesto_la_auditoria_interna
idx 11098: Obligacion_la_auditoria_interna_debe_determinar_la_efectividad_de_los_controles_internos_ya_fdcde9 -> Sujeto_propuesto_la_auditoria_interna
idx 11109: Obligacion_la_auditoria_interna_debe_evaluar_el_marco_de_gestion_de_seguridad_de_la_informa_b883ff -> Sujeto_propuesto_la_auditoria_interna
idx 11147: Obligacion_la_auditoria_interna_debe_procurarse_los_mecanismos_necesarios_para_generar_y_en_e2cc22 -> Sujeto_propuesto_la_auditoria_interna
idx 11156: Obligacion_la_auditoria_interna_debe_revisar_regularmente_la_implementacion_y_la_eficacia_d_e49087 -> Sujeto_propuesto_la_auditoria_interna__lingeef
idx 11182: Obligacion_la_auditoria_interna_debera_considerar_las_consecuencias_que_sobre_los_objetivos_a49280 -> Sujeto_propuesto_la_auditoria_interna
idx 11188: Obligacion_la_auditoria_interna_debera_evaluar_el_marco_de_la_gestion_de_proyectos_consider_2458d0 -> Sujeto_propuesto_la_auditoria_interna
idx 11190: Obligacion_la_auditoria_interna_debera_evaluar_el_marco_normativo_definido_por_la_entidad_p_e8d1a4 -> Sujeto_propuesto_la_auditoria_interna
idx 11194: Obligacion_la_auditoria_interna_debera_evaluar_el_proceso_de_control_sobre_la_gestion_de_la_2c7861 -> Sujeto_propuesto_la_auditoria_interna
idx 11198: Obligacion_la_auditoria_interna_debera_evaluar_el_proceso_de_gestion_de_vulnerabilidades_es_f4670a -> Sujeto_propuesto_la_auditoria_interna
idx 11200: Obligacion_la_auditoria_interna_debera_evaluar_el_proceso_definido_para_la_gestion_de_datos_68a9bf -> Sujeto_propuesto_la_auditoria_interna
idx 11202: Obligacion_la_auditoria_interna_debera_evaluar_el_proceso_establecido_para_el_registro_y_el_ed33bf -> Sujeto_propuesto_la_auditoria_interna
idx 11204: Obligacion_la_auditoria_interna_debera_evaluar_el_proceso_establecido_para_recolectar_proce_68f9b8 -> Sujeto_propuesto_la_auditoria_interna
idx 11206: Obligacion_la_auditoria_interna_debera_evaluar_la_adecuada_implementacion_de_controles_que__8e8fb2 -> Sujeto_propuesto_la_auditoria_interna
idx 11208: Obligacion_la_auditoria_interna_debera_evaluar_la_utilizacion_de_autenticacion_multifactor__24653b -> Sujeto_propuesto_la_auditoria_interna
idx 11210: Obligacion_la_auditoria_interna_debera_evaluar_los_procesos_establecidos_para_la_gestion_de_3479b4 -> Sujeto_propuesto_la_auditoria_interna
idx 11212: Obligacion_la_auditoria_interna_debera_tener_la_capacidad_para_evaluar_aspectos_clave_de_la_3cbccb -> Sujeto_propuesto_la_auditoria_interna
idx 11214: Obligacion_la_auditoria_interna_debera_verificar_la_implementacion_de_medidas_que_permitan__45b418 -> Sujeto_propuesto_la_auditoria_interna
idx 11216: Obligacion_la_auditoria_interna_debera_verificar_que_se_apliquen_los_controles_minimos_esta_ced17f -> Sujeto_propuesto_la_auditoria_interna
idx 11219: Obligacion_la_auditoria_interna_sera_responsable_por_la_evaluacion_y_el_monitoreo_del_contr_4b82b7 -> Sujeto_propuesto_la_auditoria_interna
idx 11373: Obligacion_la_cec_y_las_entidades_deberan_efectuar_controles_basicos_y_particulares_sobre_l_850781 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 11397: Obligacion_la_comunicacion_debe_detallar_los_fundamentos_del_cumplimiento_de_la_propuesta_d_0a1371 -> Sujeto_propuesto_la_comunicacion
idx 11403: Obligacion_la_consolidacion_con_las_filiales_en_el_exterior_se_realizara_en_oportunidad_y_a_495cbe -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 11417: Obligacion_la_copia_de_la_documentacion_requerida_contratos_disposiciones_legales_etc_debe__cd08ad -> Sujeto_propuesto_la_copia_de_la_documentacion_requerida
idx 11434: Obligacion_la_cuenta_ajustes_al_patrimonio_ajuste_por_reexpresion_de_partidas_debe_quedar_s_22672b -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 11456: Obligacion_la_determinacion_de_las_posiciones_se_efectuara_sobre_la_base_de_los_saldos_diar_66cbd1 -> Sujeto_propuesto_las_entidades__ri_pgn
idx 11484: Obligacion_la_diferencia_entre_importe_original_y_reexpresado_debe_incrementar_la_cuenta_de_01d997 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 11492: Obligacion_la_documentacion_de_la_evaluacion_de_los_riesgos_para_cada_ciclo_debe_prever_el__b6f43a -> Sujeto_propuesto_la_documentacion_de_la_evaluacion_de_los_riesgos
idx 11496: Obligacion_la_documentacion_de_los_procedimientos_de_auditoria_interna_debe_proporcionar_un_ddd3d9 -> Sujeto_propuesto_la_documentacion_de_los_procedimientos_de_la_auditoria_interna
idx 11507: Obligacion_la_documentacion_debe_especificar_claramente_las_tecnicas_establecidas_por_las_e_ca4a6d -> Sujeto_propuesto_las_entidades__nmcief
idx 11532: Obligacion_la_eleccion_de_los_escenarios_y_los_supuestos_relacionados_deben_estar_documenta_c5f6fd -> Sujeto_propuesto_la_eleccion_de_los_escenarios_y_los_supuestos_relacionados
idx 11534: Obligacion_la_empresa_prestadora_de_servicios_u_organismo_recaudador_debe_comunicar_a_la_en_97e10b -> Sujeto_propuesto_la_empresa_prestadora_de_servicios_organismo_recaudador_de_impuestos_etc
idx 11623: Obligacion_la_entidad_debera_informar_a_la_sefyc_cuando_trata_sistemas_de_pagos_de_alto_val_0b3b0b -> Sujeto_propuesto_una_entidad
idx 12048: Obligacion_la_entidad_financiera_y_la_agencia_complementaria_de_servicios_financieros_deben_0b5401 -> Sujeto_propuesto_la_agencia_complementaria_de_servicios_financieros
idx 12176: Obligacion_la_entidad_representante_debe_identificar_en_el_proceso_de_intercambio_los_docum_5b9194 -> Sujeto_propuesto_la_entidad_representante
idx 12237: Obligacion_la_evaluacion_de_los_deudores_y_de_las_financiaciones_debe_realizarse_de_manera__bf53c4 -> Sujeto_propuesto_la_evaluacion_de_los_deudores_y_de_las_financiaciones
idx 12277: Obligacion_la_exposicion_al_riesgo_debe_mantenerse_dentro_de_limites_aceptables_y_estar_ade_5a2159 -> Sujeto_propuesto_la_exposicion_al_riesgo
idx 12282: Obligacion_la_firma_y_sello_del_personal_deben_figurar_en_los_registros_obrantes_en_la_gere_cc6287 -> Sujeto_propuesto_personal_de_la_respectiva_entidad
idx 12284: Obligacion_la_funcion_de_auditoria_interna_debe_realizar_examenes_independientes_de_la_gest_ca3f26 -> Sujeto_propuesto_la_funcion_de_auditoria_interna
idx 12290: Obligacion_la_funcion_de_revision_del_credito_debe_verificar_si_los_respectivos_legajos_est_2b2575 -> Sujeto_propuesto_la_funcion_de_revision_del_credito
idx 12299: Obligacion_la_gerencia_debe_comprender_los_supuestos_y_limitaciones_inherentes_a_las_medida_e9e08c -> Sujeto_propuesto_la_gerencia
idx 12333: Obligacion_la_gestion_debera_iniciarse_con_la_presentacion_de_una_solicitud_de_autorizacion_5f8785 -> Sujeto_propuesto_la_gestion
idx 12336: Obligacion_la_gestion_del_cambio_debe_evaluar_la_evolucion_de_los_riesgos_asociados_a_lo_la_a21971 -> Sujeto_propuesto_la_gestion_del_cambio
idx 12347: Obligacion_la_implementacion_de_los_cambios_debe_ser_monitoreada_por_controles_especificos__684803 -> Sujeto_propuesto_la_implementacion_de_los_cambios
idx 12381: Obligacion_la_imputacion_de_ori_de_partidas_no_monetarias_surge_por_diferencia_entre_medici_6d9c97 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 12399: Obligacion_la_informacion_comparativa_en_estados_financieros_trimestrales_debera_estar_expr_5d7aaf -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 12430: Obligacion_la_informacion_se_recibe_separadamente_por_cada_tipo_de_moneda_o_especie_para_ca_7c9537 -> Sujeto_propuesto_todas_las_entidades_participantes
idx 12432: Obligacion_la_informacion_se_recibe_separadamente_por_tipo_de_moneda_pesos_o_moneda_extranj_54d038 -> Sujeto_propuesto_las_entidades__snp_tr
idx 12478: Obligacion_la_nota_debera_estar_intervenida_con_firma_y_sello_aclaratorio_por_personal_de_l_8df873 -> Sujeto_propuesto_personal_de_la_respectiva_entidad
idx 12521: Obligacion_la_posicion_a_termino_se_calculara_en_esta_institucion_conforme_a_la_formula_par_4df6f1 -> Sujeto_propuesto_esta_institucion
idx 12528: Obligacion_la_presentacion_de_modificaciones_de_socios_se_remitira_acompanada_de_la_formula_6067d2 -> Sujeto_propuesto_la_asociacion_de_profesionales_universitarios
idx 12535: Obligacion_la_primera_linea_de_defensa_debe_realizar_evaluaciones_del_control_y_riesgo_oper_b01b43 -> Sujeto_propuesto_la_primera_linea_de_defensa
idx 12537: Obligacion_la_propuesta_de_solucion_debe_contener_una_descripcion_detallada_de_todos_los_pr_e104d1 -> Sujeto_propuesto_las_entidades__nmcief
idx 12559: Obligacion_la_rpc_y_la_posicion_de_activos_inmovilizados_seran_las_correspondientes_a_la_po_33dd24 -> Sujeto_propuesto_las_entidades__ri_pgn
idx 12566: Obligacion_la_segunda_linea_de_defensa_debe_cubrir_todas_las_fases_del_proceso_y_asegurar_q_ebc8ba -> Sujeto_propuesto_esta_linea_de_defensa
idx 12569: Obligacion_la_segunda_linea_de_defensa_debe_revisar_las_evaluaciones_del_control_y_del_ries_f73a40 -> Sujeto_propuesto_la_segunda_linea_de_defensa
idx 12576: Obligacion_la_situacion_patrimonial_y_de_resultados_de_las_filiales_operativas_radicadas_en_e6a25b -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 12579: Obligacion_la_solicitud_de_ampliacion_temporal_de_limites_debera_ser_cursada_independientem_6ba5ee -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 12587: Obligacion_la_solicitud_de_autorizacion_debera_incluir_la_clase_de_entidad_financiera_para__43cae8 -> Sujeto_propuesto_personas_que_reunan_la_condicion_de_futuros_fundadores
idx 12591: Obligacion_la_solicitud_de_autorizacion_debera_ser_interpuesta_a_traves_del_correspondiente_1477c1 -> Sujeto_propuesto_personas_que_reunan_la_condicion_de_futuros_fundadores
idx 12593: Obligacion_la_solicitud_de_autorizacion_debera_ser_interpuesta_mediante_nota_acompanada_de__adfcaa -> Sujeto_propuesto_la_solicitud
idx 12635: Obligacion_la_transmision_de_los_archivos_electronicos_de_los_rechazos_se_realizara_en_el_h_c51ac5 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 12646: Obligacion_la_unidad_encargada_de_la_gestion_del_riesgo_operacional_debera_depender_funcion_dc4887 -> Sujeto_propuesto_la_estructura_de_la_unidad_encargada_de_la_gestion_del_riesgo_operacional
idx 12648: Obligacion_la_unidad_encargada_de_la_gestion_del_riesgo_operacional_debera_recibir_de_las_g_72a6ab -> Sujeto_propuesto_la_unidad_encargada_de_la_gestion_del_riesgo_operacional
idx 12650: Obligacion_la_unidad_encargada_o_persona_responsable_de_la_gestion_del_riesgo_operacional_d_81ea0b -> Sujeto_propuesto_la_unidad_encargada_o_persona_responsable_de_la_gestion_del_riesgo_operacional
idx 12671: Obligacion_la_verificacion_de_precios_de_mercado_o_de_datos_ingresados_a_modelos_debe_ser_l_e61fee -> Sujeto_propuesto_un_area_independiente
idx 12684: Obligacion_las_actas_de_retencion_deben_ser_integradas_en_su_totalidad_y_remitidas_al_bcra__4a40da -> Sujeto_propuesto_las_actas_de_retencion
idx 12698: Obligacion_las_altas_de_activos_no_monetarios_expresados_en_moneda_del_periodo_no_se_reexpr_69fac1 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 12700: Obligacion_las_amortizaciones_de_activos_no_monetarios_deben_devengarse_sobre_la_base_del_v_ca72f2 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 12703: Obligacion_las_areas_auditadas_deben_adoptar_oportunamente_las_medidas_correctivas_identifi_e0eef4 -> Sujeto_propuesto_las_areas_auditadas
idx 12705: Obligacion_las_areas_de_gestion_del_riesgo_y_planificacion_estrategica_deben_comunicarse_pe_35cfff -> Sujeto_propuesto_las_areas_de_gestion_del_riesgo_y_planificacion_estrategica
idx 12709: Obligacion_las_asambleas_generales_de_accionistas_deben_aprobar_la_disolucion_de_las_entida_1f278e -> Sujeto_propuesto_las_respectivas_asambleas_generales_de_accionistas
idx 12711: Obligacion_las_asociaciones_de_profesionales_constituidas_de_acuerdo_con_un_tipo_societario_004831 -> Sujeto_propuesto_las_asociaciones_de_profesionales_constituidas_de_acuerdo_con_un_tipo_societario
idx 12714: Obligacion_las_asociaciones_de_profesionales_universitarios_cuyos_socios_cumplan_funciones__324084 -> Sujeto_propuesto_las_asociaciones_de_profesionales_universitarios_cuyos_socios_cumplan_funciones_
idx 12740: Obligacion_las_autoridades_de_la_entidad_deben_tomar_conocimiento_del_contenido_de_los_info_13980b -> Sujeto_propuesto_las_autoridades_de_la_entidad
idx 12857: Obligacion_las_capacidades_de_agregacion_de_datos_sobre_riesgos_y_las_practicas_de_elaborac_b8a26d -> Sujeto_propuesto_las_capacidades_de_agregacion_de_datos_sobre_riesgos_y_las_practicas_de_elaborac
idx 12861: Obligacion_las_capacidades_de_agregacion_de_datos_sobre_riesgos_y_las_practicas_de_elaborac_dd772e -> Sujeto_propuesto_las_capacidades_de_agregacion_de_datos_sobre_riesgos_y_las_practicas_de_elaborac
idx 12919: Obligacion_las_cec_y_las_entidades_deberan_efectuar_controles_sobre_los_archivos_intercambi_81e47c -> Sujeto_propuesto_las_entidades__snp_tr
idx 12941: Obligacion_las_consultas_y_o_gestiones_efectuadas_en_el_sistema_de_almacenamiento_deberan_l_5bff84 -> Sujeto_propuesto_camaras_electronicas_de_compensacion
idx 12944: Obligacion_las_contrapartidas_de_la_medicion_de_pasivos_financieros_al_momento_de_incorpora_8670ff -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 12946: Obligacion_las_contrapartidas_de_medicion_de_activos_financieros_al_momento_de_incorporacio_f57b9d -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 12972: Obligacion_las_disposiciones_del_regimen_de_control_interno_deben_observarse_en_las_filiale_cb6e44 -> Sujeto_propuesto_las_filiales_y_subsidiarias_que_consolidan_estados_financieros_con_la_entidad_fi
idx 12992: Obligacion_las_empresas_emisoras_locales_de_titulos_valores_que_constituyen_garantia_o_cauc_68d64e -> Sujeto_propuesto_las_empresas_emisoras_locales
idx 13003: Obligacion_las_entidades_b_y_c_remitiran_la_informacion_de_ambos_subperiodos_el_22_09__ri_r_785c98 -> Sujeto_propuesto_las_entidades_b_y_c
idx 13101: Obligacion_las_entidades_deben_adaptar_su_contabilidad_al_plan_de_cuentas_minimo_establecid_8ad1fd -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 13117: Obligacion_las_entidades_deben_calcular_al_31_12_2024_las_previsiones_totales_segun_las_nii_52beae -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 13183: Obligacion_las_entidades_deben_clasificar_y_medir_pasivos_financieros_a_costo_amortizado_co_127276 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 13185: Obligacion_las_entidades_deben_colocar_una_etiqueta_aclaratoria_que_indique_la_cantidad_par_300ff4 -> Sujeto_propuesto_las_entidades__cirmo3
idx 13305: Obligacion_las_entidades_deben_efectuar_validaciones_a_los_archivos_recibidos_y_devolverlos_3f22ec -> Sujeto_propuesto_las_entidades__snp_tr
idx 13366: Obligacion_las_entidades_deben_evaluar_si_las_actividades_de_control_han_sido_adecuadamente_c7a302 -> Sujeto_propuesto_las_entidades__nmcief
idx 13414: Obligacion_las_entidades_deben_informar_a_la_gerencia_de_control_de_auditores_de_la_superin_d67085 -> Sujeto_propuesto_las_entidades__nmcief
idx 13416: Obligacion_las_entidades_deben_informar_a_la_gerencia_de_control_de_auditores_la_nomina_de__eec33f -> Sujeto_propuesto_las_entidades__nmcief
idx 13447: Obligacion_las_entidades_deben_operar_conforme_a_los_estandares_y_formatos_definidos_en_las_44113e -> Sujeto_propuesto_las_entidades__snp_tr
idx 13461: Obligacion_las_entidades_deben_prever_la_unificacion_de_existencias_deterioradas_cuando_ten_ad88c4 -> Sujeto_propuesto_las_entidades__cirmo3
idx 13482: Obligacion_las_entidades_deben_registrar_mensualmente_1_36_de_la_diferencia_y_en_forma_acum_1fd6a9 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 13548: Obligacion_las_entidades_deben_registrar_sus_operaciones_variaciones_patrimoniales_y_elabor_9f65db -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 13614: Obligacion_las_entidades_deben_respetar_los_horarios_limite_de_presentacion_de_informacion__017527 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 13685: Obligacion_las_entidades_deberan_adoptar_los_mecanismos_necesarios_propios_o_a_traves_de_te_591149 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 13695: Obligacion_las_entidades_deberan_agregar_todas_las_exposiciones_desconocidas_como_si_estuvi_6b9d15 -> Sujeto_propuesto_las_entidades
idx 13697: Obligacion_las_entidades_deberan_agrupar_las_exposiciones_del_sector_publico_no_financiero__eccbe2 -> Sujeto_propuesto_las_entidades
idx 13701: Obligacion_las_entidades_deberan_cerrar_de_oficio_las_cuentas_especiales_de_regularizacion__545273 -> Sujeto_propuesto_estas_cuentas
idx 13706: Obligacion_las_entidades_deberan_comunicar_a_la_superintendencia_de_entidades_financieras_y_8abecb -> Sujeto_propuesto_deberan_comunicar
idx 13716: Obligacion_las_entidades_deberan_considerar_los_numerales_del_periodo_01_09_a_18_09_dividid_64e2ba -> Sujeto_propuesto_las_entidades__ri_rml
idx 13753: Obligacion_las_entidades_deberan_documentar_los_controles_de_monitoreo_como_minimo_para_tod_05b295 -> Sujeto_propuesto_las_entidades__nmcief
idx 13768: Obligacion_las_entidades_deberan_enviar_a_la_superintendencia_de_entidades_financieras_y_ca_a905ed -> Sujeto_propuesto_las_entidades__nmcief
idx 13773: Obligacion_las_entidades_deberan_enviar_dentro_de_los_diez_dias_habiles_posteriores_a_su_de_717320 -> Sujeto_propuesto_las_entidades__ri_ccna
idx 13821: Obligacion_las_entidades_deberan_incluir_por_unica_vez_junto_con_los_datos_de_febrero_2014__300f36 -> Sujeto_propuesto_las_entidades__ri_pgn
idx 13823: Obligacion_las_entidades_deberan_indicar_quien_realizara_el_transporte_o_el_deposito_ya_sea_10c0e2 -> Sujeto_propuesto_las_entidades__cirmo3
idx 13825: Obligacion_las_entidades_deberan_informar_la_cbu_o_alias_de_la_cuenta_pagadora_y_de_la_cuen_fc2edd -> Sujeto_propuesto_las_entidades__snp_cheq
idx 13845: Obligacion_las_entidades_deberan_mantener_la_documentacion_de_controles_actualizada__nmcief_6155cf -> Sujeto_propuesto_las_entidades__nmcief
idx 13847: Obligacion_las_entidades_deberan_ofrecer_a_los_solicitantes_que_sean_sus_clientes_y_se_encu_1670d4 -> Sujeto_propuesto_las_citadas_entidades__depaho
idx 13856: Obligacion_las_entidades_deberan_presentar_la_totalidad_de_los_registros_correspondientes_a_ef38b1 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 13858: Obligacion_las_entidades_deberan_presentar_los_cedip_no_compensados_por_no_haberse_presenta_33d4f2 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 13860: Obligacion_las_entidades_deberan_presentar_los_eventuales_ajustes_a_cedip_ya_presentados_y__4b31d1 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 13862: Obligacion_las_entidades_deberan_presentar_los_rechazos_de_ajustes_en_la_sesion_de_rechazad_34e25c -> Sujeto_propuesto_las_entidades__snp_cheq
idx 13864: Obligacion_las_entidades_deberan_presentar_los_rechazos_de_ajustes_por_presentacion_fuera_d_59a423 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 13866: Obligacion_las_entidades_deberan_presentar_los_rechazos_de_las_entidades_depositarias_por_l_8deb2c -> Sujeto_propuesto_las_entidades__snp_cheq
idx 13868: Obligacion_las_entidades_deberan_presentar_los_rechazos_de_las_entidades_giradas_por_las_ca_9d23cf -> Sujeto_propuesto_las_entidades__snp_cheq
idx 13870: Obligacion_las_entidades_deberan_proveer_informaciones_respecto_de_los_tipos_de_unidades_de_acfa5f -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 13874: Obligacion_las_entidades_deberan_registrar_en_el_sistema_de_circulacion_electronica_sce_la__8c2d11 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 13876: Obligacion_las_entidades_deberan_remitir_las_informaciones_correspondientes_a_cada_mes_en_l_da5a52 -> Sujeto_propuesto_las_entidades__ri_pgn
idx 13892: Obligacion_las_entidades_deberan_transmitir_a_la_s_cec_archivos_con_la_informacion_de_los_c_cfa235 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 13895: Obligacion_las_entidades_deberan_transmitir_diariamente_archivos_a_la_cec_en_dos_sesiones_s_9fc957 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 13897: Obligacion_las_entidades_deberan_utilizar_el_codigo_r96_cuando_la_entidad_depositaria_detec_3d0ff2 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 13901: Obligacion_las_entidades_deberan_utilizar_los_tipos_de_identificacion_especificados_segun_l_5e9c5c -> Sujeto_propuesto_las_entidades
idx 13905: Obligacion_las_entidades_deberan_utilizar_subcuentas_para_identificar_las_operaciones_al_co_f003ea -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 13907: Obligacion_las_entidades_depositantes_deben_informar_y_mantener_actualizados_sus_datos_de_c_1c4148 -> Sujeto_propuesto_las_entidades_depositantes
idx 13925: Obligacion_las_entidades_destinatarias_deberan_efectuar_como_minimo_controles_sobre_causale_4dcb7c -> Sujeto_propuesto_las_entidades_destinatarias
idx 13927: Obligacion_las_entidades_destinatarias_deberan_efectuar_como_minimo_controles_sobre_contado_101569 -> Sujeto_propuesto_las_entidades_destinatarias
idx 13929: Obligacion_las_entidades_destinatarias_deberan_efectuar_como_minimo_controles_sobre_datos_c_7c111a -> Sujeto_propuesto_las_entidades_destinatarias
idx 13931: Obligacion_las_entidades_destinatarias_deberan_efectuar_como_minimo_controles_sobre_dias_no_1bf52f -> Sujeto_propuesto_las_entidades_destinatarias
idx 13933: Obligacion_las_entidades_destinatarias_deberan_efectuar_como_minimo_controles_sobre_plazos__717d86 -> Sujeto_propuesto_las_entidades_destinatarias
idx 13935: Obligacion_las_entidades_destinatarias_deberan_efectuar_como_minimo_controles_sobre_transac_551ade -> Sujeto_propuesto_las_entidades_destinatarias
idx 14019: Obligacion_las_entidades_financieras_deben_ajustarse_a_los_codigos_numericos_de_seis_digito_90033c -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 14329: Obligacion_las_entidades_financieras_deben_divulgar_la_informacion_conforme_a_lo_establecid_1ed5b2 -> Sujeto_propuesto_la_divulgacion_de_la_informacion
idx 14449: Obligacion_las_entidades_financieras_deben_integrar_los_importes_de_efectivo_minimo_utiliza_a978ef -> Sujeto_propuesto_sucursales_o_subsidiarias_de_bancos_del_exterior_calificados_como_sistematicamen
idx 14647: Obligacion_las_entidades_financieras_deberan_comprobar_el_empleo_de_los_solicitantes_durant_7282e6 -> Sujeto_propuesto_las_entidades__manori
idx 14680: Obligacion_las_entidades_financieras_deberan_cumplir_las_restantes_normas_prudenciales_que__818e18 -> Sujeto_propuesto_las_tenencias_de_participaciones_en_entidades_financieras_del_exterior
idx 14804: Obligacion_las_entidades_financieras_deberan_informar_el_cumplimiento_de_las_medidas_minima_b984d1 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 14807: Obligacion_las_entidades_financieras_deberan_informar_el_cumplimiento_del_sistema_de_monito_2154ae -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 14810: Obligacion_las_entidades_financieras_deberan_informar_la_cantidad_de_cofres_existentes_en_e_1accd5 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 14826: Obligacion_las_entidades_financieras_deberan_medir_las_inversiones_en_subsidiarias_asociada_8f8aef -> Sujeto_propuesto_las_entidades_financieras
idx 14862: Obligacion_las_entidades_financieras_deberan_proveer_informacion_del_numero_de_serie_de_la__35a81a -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 14864: Obligacion_las_entidades_financieras_deberan_proveer_informacion_respecto_de_los_tipos_de_u_0b4779 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 14866: Obligacion_las_entidades_financieras_deberan_proveer_informacion_sobre_la_marca_del_tesoro__4f7b6f -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 14879: Obligacion_las_entidades_financieras_deberan_realizar_pruebas_de_funcionamiento_para_evalua_811a0f -> Sujeto_propuesto_las_entidades__nmcief
idx 14944: Obligacion_las_entidades_financieras_deberan_utilizar_la_denominacion_de_cuentas_establecid_aac56b -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 15009: Obligacion_las_entidades_financieras_no_pueden_dejar_de_calcular_y_registrar_los_conceptos__30e7f4 -> Sujeto_propuesto_las_entidades__manori
idx 15026: Obligacion_las_entidades_financieras_o_las_transportadoras_de_valores_que_operen_a_su_servi_e983f3 -> Sujeto_propuesto_las_transportadoras_de_valores_que_operen_a_su_servicio
idx 15188: Obligacion_las_entidades_financieras_que_sean_participantes_directas_o_que_utilicen_servici_64d9b0 -> Sujeto_propuesto_que_utilicen_servicios_de_corresponsalia
idx 15213: Obligacion_las_entidades_financieras_y_los_terceros_contratados_deben_comprometerse_a_permi_151e7e -> Sujeto_propuesto_los_terceros_que_estas_contraten
idx 15219: Obligacion_las_entidades_financieras_y_psp_deberan_tener_en_cuenta_las_normas_sobre_requisi_de1dde -> Sujeto_propuesto_proveedores_de_servicios_de_pago
idx 15221: Obligacion_las_entidades_gestoras_de_echeq_deben_remitir_la_informacion_requerida_al_sistem_8ef54a -> Sujeto_propuesto_las_entidades_gestoras_de_echeq
idx 15223: Obligacion_las_entidades_gestoras_de_echeq_tienen_la_exclusiva_responsabilidad_de_garantiza_e19c98 -> Sujeto_propuesto_las_entidades_gestoras_de_echeq
idx 15225: Obligacion_las_entidades_giradas_deben_extremar_reforzar_los_controles_electronicos_de_la_i_6c3b30 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 15244: Obligacion_las_entidades_intervinientes_deben_mantener_abierta_la_cuenta_por_180_dias_corri_888b9a -> Sujeto_propuesto_las_entidades_intervinientes
idx 15326: Obligacion_las_entidades_originantes_deben_transmitir_a_una_camara_electronica_de_compensac_2ae2b5 -> Sujeto_propuesto_las_entidades__snp_tr
idx 15343: Obligacion_las_entidades_participantes_deberan_suscribir_el_acuerdo_y_adherir_a_el_como_con_07937f -> Sujeto_propuesto_el_los_administrador_es_del_sistema_de_almacenamiento
idx 15344: Obligacion_las_entidades_participantes_deberan_suscribir_el_acuerdo_y_adherir_a_el_como_con_07937f -> Sujeto_propuesto_las_infraestructuras_de_mercado_financiero_gestoras_y_o_que_realicen_la_custodia
idx 15352: Obligacion_las_entidades_participantes_se_prestaran_entre_si_la_cooperacion_que_fuera_neces_81336a -> Sujeto_propuesto_las_entidades__snp_cheq
idx 15354: Obligacion_las_entidades_podran_imputar_los_movimientos_en_las_cuentas_de_sus_clientes_en_b_5623ae -> Sujeto_propuesto_las_entidades__snp_cheq
idx 15362: Obligacion_las_entidades_podran_transmitir_archivos_a_una_cec_durante_toda_la_jornada_desde_aa1d68 -> Sujeto_propuesto_las_entidades__snp_tr
idx 15367: Obligacion_las_entidades_publicas_o_mixtas_de_la_nacion_provincias_municipalidades_o_caba_t_dae94d -> Sujeto_propuesto_las_que_tengan_caracter_de_entidades_publicas_o_mixtas_de_la_nacion_de_las_provi
idx 15369: Obligacion_las_entidades_pueden_transmitir_archivos_a_una_cec_desde_el_horario_de_inicio_de_4d7d06 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 15373: Obligacion_las_entidades_que_brindan_el_servicio_de_gestion_para_echeq_deberan_brindar_tamb_b331d6 -> Sujeto_propuesto_aquellas_entidades_que_brinden_el_servicio_de_gestion_para_echeq
idx 15376: Obligacion_las_entidades_que_cumplan_la_condicion_de_depositos_spnf_deberan_computar_los_nu_8d823a -> Sujeto_propuesto_las_entidades__ri_rml
idx 15417: Obligacion_las_entidades_que_necesiten_en_determinadas_epocas_del_ano_cantidades_de_billete_42e6d3 -> Sujeto_propuesto_las_entidades__cirmo3
idx 15419: Obligacion_las_entidades_que_no_envien_la_informacion_antes_del_horario_limite_deben_espera_7620de -> Sujeto_propuesto_las_entidades__snp_cheq
idx 15421: Obligacion_las_entidades_que_no_envien_la_informacion_de_presentados_antes_del_horario_limi_f2424d -> Sujeto_propuesto_las_entidades__snp_cheq
idx 15458: Obligacion_las_entidades_que_se_retrasen_en_el_envio_de_la_informacion_en_la_sesion_de_pres_6b931e -> Sujeto_propuesto_las_entidades__snp_tr
idx 15460: Obligacion_las_entidades_que_suscriban_o_adhieran_al_acuerdo_otorgan_y_aceptan_mandatos_rec_21548c -> Sujeto_propuesto_las_entidades__snp_cheq
idx 15462: Obligacion_las_entidades_que_tengan_implementada_la_apertura_remota_de_cuentas_a_la_vista_d_aaf451 -> Sujeto_propuesto_aquellas_entidades
idx 15490: Obligacion_las_entidades_recibiran_de_la_cec_los_archivos_resultantes_de_la_compensacion_ha_afcb6c -> Sujeto_propuesto_las_entidades__snp_cheq
idx 15500: Obligacion_las_entidades_se_responsabilizaran_de_la_entrega_o_retiro_del_soporte_magnetico__d183a1 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 15504: Obligacion_las_entidades_utilizaran_la_variacion_del_indice_correspondiente_al_mes_anterior_1a1970 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 15508: Obligacion_las_especies_de_titulos_publicos_nacionales_o_instrumentos_de_regulacion_monetar_6d6c51 -> Sujeto_propuesto_las_entidades__ri_rml
idx 15524: Obligacion_las_excepciones_a_las_politicas_practicas_procedimientos_y_limites_establecidos__f0ce4d -> Sujeto_propuesto_el_nivel_funcional_con_capacidad_decisoria
idx 15543: Obligacion_las_financiaciones_deberan_cumplir_con_las_condiciones_establecidas_en_esta_secc_0aac98 -> Sujeto_propuesto_las_financiaciones
idx 15545: Obligacion_las_financiaciones_otorgadas_mediante_pases_activos_se_registraran_en_las_cuenta_d61f02 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 15548: Obligacion_las_financiaciones_recibidas_mediante_pases_pasivos_se_registraran_en_las_cuenta_9f414e -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 15570: Obligacion_las_funcionalidades_que_requieran_el_ingreso_de_datos_de_transferencias_deberan__317821 -> Sujeto_propuesto_las_funcionalidades_que_requieran_el_ingreso_de_los_datos_de_transferencias
idx 15577: Obligacion_las_gerencias_seran_responsables_de_aplicar_en_las_distintas_unidades_de_negocio_d044e7 -> Sujeto_propuesto_las_gerencias
idx 15581: Obligacion_las_herramientas_de_seguimiento_de_liquidez_intradiaria_deberan_observarse_confo_8a4df3 -> Sujeto_propuesto_las_herramientas_de_seguimiento
idx 15592: Obligacion_las_imagenes_faltantes_que_no_hayan_sido_publicadas_en_el_reservorio_y_el_reenvi_41f0cf -> Sujeto_propuesto_las_entidades__snp_cheq
idx 15596: Obligacion_las_incorporaciones_o_retiros_de_socios_deberan_ser_comunicados_a_la_superintend_dc93f1 -> Sujeto_propuesto_las_asociaciones_de_profesionales_universitarios
idx 15598: Obligacion_las_infraestructuras_de_mercado_financiero_sistemicamente_importantes_que_realic_63d0df -> Sujeto_propuesto_dichas_infraestructuras
idx 15608: Obligacion_las_modificaciones_a_la_composicion_del_capital_social_deberan_concertarse_ad_re_c28075 -> Sujeto_propuesto_las_modificaciones_a_la_composicion_del_capital_social
idx 15628: Obligacion_las_obligaciones_ya_sea_en_pesos_moneda_extranjera_o_titulos_se_clasificaran_en__df2d44 -> Sujeto_propuesto_las_entidades__ri_rml
idx 15696: Obligacion_las_partidas_informadas_deberan_mantener_las_correlaciones_con_cuentas_de_balanc_17494b -> Sujeto_propuesto_las_entidades__ri_rml
idx 15733: Obligacion_las_partidas_reimputadas_que_conformaron_el_saldo_inicial_de_otras_partidas_no_m_4e3c54 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 15762: Obligacion_las_personas_propuestas_para_integrar_organos_de_administracion_y_fiscalizacion__48d9a5 -> Sujeto_propuesto_las_personas_que_sean_propuestas_para_integrar_los_organos_de_administracion_y_f
idx 15764: Obligacion_las_personas_responsables_de_las_lineas_de_negocio_que_desarrollen_actividades_q_3defb4 -> Sujeto_propuesto_las_personas_responsables_de_las_lineas_de_negocio
idx 15766: Obligacion_las_personas_responsables_de_las_unidades_de_negocio_que_desarrollen_actividades_113e33 -> Sujeto_propuesto_las_personas_responsables_de_las_unidades_de_negocio
idx 15768: Obligacion_las_personas_responsables_por_la_gestion_del_credito_deben_estar_en_contacto_con_97d39e -> Sujeto_propuesto_las_personas_responsables_por_la_gestion_del_credito
idx 15806: Obligacion_las_politicas_y_los_procedimientos_de_gestion_del_cambio_deben_estar_sujetos_a_r_c4a8a8 -> Sujeto_propuesto_las_politicas_y_los_procedimientos_de_gestion_del_cambio
idx 15808: Obligacion_las_politicas_y_procedimientos_deben_contemplar_que_al_calcular_los_requerimient_71e071 -> Sujeto_propuesto_estas_politicas_y_procedimientos
idx 15815: Obligacion_las_presentaciones_deben_estar_agrupadas_segun_cada_unidad_monetaria_pesos_o_dol_f3c323 -> Sujeto_propuesto_las_presentaciones
idx 15823: Obligacion_las_pruebas_de_estres_con_fines_de_administracion_del_riesgo_deben_cubrir_period_022437 -> Sujeto_propuesto_las_pruebas_de_estres
idx 15827: Obligacion_las_pruebas_de_estres_deben_cumplir_un_rol_importante_en_la_comunicacion_del_rie_ac1cf5 -> Sujeto_propuesto_las_pruebas_de_estres
idx 15844: Obligacion_las_pruebas_de_estres_deben_incluir_varios_horizontes_de_tiempo_dependiendo_de_l_040683 -> Sujeto_propuesto_las_pruebas_de_estres
idx 15848: Obligacion_las_pruebas_de_estres_deben_proporcionar_una_perspectiva_del_riesgo_complementar_0f0fcf -> Sujeto_propuesto_las_pruebas_de_estres
idx 15850: Obligacion_las_pruebas_de_estres_deben_ser_consideradas_en_la_administracion_del_riesgo_en__915bd3 -> Sujeto_propuesto_las_pruebas_de_estres
idx 15854: Obligacion_las_pruebas_de_estres_deben_ser_una_herramienta_central_en_la_identificacion_eva_9a8221 -> Sujeto_propuesto_las_pruebas_de_estres
idx 15858: Obligacion_las_pruebas_de_estres_deben_tener_un_rol_importante_en_la_comunicacion_externa_c_7e6863 -> Sujeto_propuesto_las_pruebas_de_estres
idx 15860: Obligacion_las_pruebas_de_estres_deben_utilizarse_para_evaluar_la_solidez_de_los_modelos_fr_869d75 -> Sujeto_propuesto_las_pruebas_de_estres
idx 15879: Obligacion_las_salvedades_deben_fundamentarse_adecuadamente_precisando_las_cuentas_o_rubros_0d7da6 -> Sujeto_propuesto_el_auditor_externo
idx 15913: Obligacion_las_solicitudes_de_credito_deben_ser_analizadas_cuidadosamente_por_analistas_de__0d57a9 -> Sujeto_propuesto_las_solicitudes_de_credito
idx 15945: Obligacion_las_tecnicas_de_medicion_de_riesgos_deberan_evolucionar_a_medida_que_cambien_los_dabfb6 -> Sujeto_propuesto_sendas_tecnicas
idx 15953: Obligacion_las_transferencias_de_fondos_realizadas_con_motivo_de_acreditaciones_vinculadas__daad0d -> Sujeto_propuesto_las_entidades__snp_tr
idx 15959: Obligacion_las_transferencias_por_asignaciones_familiares_deberan_identificarse_con_la_leye_aa2c32 -> Sujeto_propuesto_las_entidades__snp_tr
idx 16003: Obligacion_los_activos_subyacentes_recibidos_por_las_operaciones_de_pases_activo_se_registr_364a67 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 16006: Obligacion_los_administradores_de_esquemas_de_transferencias_inmediatas_deben_monitorear_lo_29fcde -> Sujeto_propuesto_los_administradores_de_esquemas_de_transferencias_inmediatas
idx 16011: Obligacion_los_administradores_deben_prever_en_sus_contratos_la_aplicacion_de_multas_cuando_6c4a20 -> Sujeto_propuesto_los_administradores_de_esquemas_de_transferencias_inmediatas
idx 16020: Obligacion_los_aspectos_relativos_a_la_gestion_de_ciberincidentes_deberan_considerar_las_re_9e9a7c -> Sujeto_propuesto_los_aspectos_relativos_a_la_gestion_de_ciberincidentes
idx 16066: Obligacion_los_cambios_deben_monitorearse_durante_y_despues_de_su_implementacion_para_ident_82ec44 -> Sujeto_propuesto_los_cambios
idx 16079: Obligacion_los_caracteres_alfabeticos_de_los_campos_alfanumericos_deben_ser_siempre_informa_3d538b -> Sujeto_propuesto_las_entidades__snp_cheq
idx 16107: Obligacion_los_codigos_de_niveles_de_consolidacion_deberan_ser_coincidentes_con_los_informa_976c12 -> Sujeto_propuesto_las_entidades
idx 16111: Obligacion_los_compradores_o_suscriptores_deben_permitir_y_cooperar_con_las_inspecciones_qu_47b790 -> Sujeto_propuesto_los_compradores_o_suscriptores
idx 16233: Obligacion_los_controles_deben_asegurar_que_la_informacion_a_partir_de_la_cual_se_toman_las_062567 -> Sujeto_propuesto_los_controles
idx 16239: Obligacion_los_convenios_deben_contener_clausula_expresa_por_la_que_las_entidades_autoricen_f57292 -> Sujeto_propuesto_las_entidades__ri_ccna
idx 16249: Obligacion_los_datos_de_correo_electronico_y_telefonicos_pueden_ser_remitidos_por_email_a_e_26c44e -> Sujeto_propuesto_las_entidades_depositantes
idx 16251: Obligacion_los_datos_de_correo_electronico_y_telefonicos_pueden_ser_remitidos_por_email_a_e_892bdd -> Sujeto_propuesto_las_entidades_depositantes
idx 16253: Obligacion_los_datos_de_riesgos_deben_estar_disponibles_por_linea_de_negocio_persona_juridi_e23b92 -> Sujeto_propuesto_esos_datos
idx 16272: Obligacion_los_delegados_deben_contar_con_un_canal_de_comunicacion_claro_para_transmitir_su_02556d -> Sujeto_propuesto_los_delegados
idx 16274: Obligacion_los_delegados_deben_tener_una_clara_autoridad_jerarquica_sobre_las_unidades_resp_48a38c -> Sujeto_propuesto_los_delegados
idx 16323: Obligacion_los_empleadores_comprendidos_deberan_suministrar_informacion_que_contenga_como_m_575d2f -> Sujeto_propuesto_los_empleadores_comprendidos
idx 16325: Obligacion_los_empleadores_deben_avisar_inmediatamente_a_los_bancos_sus_cambios_de_domicili_258e81 -> Sujeto_propuesto_los_empleadores
idx 16328: Obligacion_los_endosos_deben_realizarse_al_dorso_del_documento_ante_escribano_funcionario_d_402f44 -> Sujeto_propuesto_los_endosos
idx 16353: Obligacion_los_fondos_remanentes_que_existan_luego_del_cierre_de_la_cuenta_deben_ser_transf_2a18d9 -> Sujeto_propuesto_los_fondos_remanentes
idx 16365: Obligacion_los_futuros_fundadores_deberan_constituir_un_domicilio_especial_en_la_ciudad_aut_5fe688 -> Sujeto_propuesto_personas_que_reunan_la_condicion_de_futuros_fundadores
idx 16368: Obligacion_los_futuros_fundadores_deberan_presentar_como_parte_de_la_solicitud_de_autorizac_3d9f79 -> Sujeto_propuesto_personas_que_reunan_la_condicion_de_futuros_fundadores
idx 16389: Obligacion_los_importes_deben_consignarse_en_promedios_mensuales_de_saldos_diarios__ri_rml__906cce -> Sujeto_propuesto_las_entidades__ri_rml
idx 16398: Obligacion_los_importes_se_registraran_en_miles_de_pesos_y_dolares_estadounidenses_segun_su_5a15a5 -> Sujeto_propuesto_las_entidades__ri_rml
idx 16406: Obligacion_los_informes_de_auditoria_interna_deben_conservarse_en_la_entidad_durante_un_per_eb02f2 -> Sujeto_propuesto_la_entidad
idx 16408: Obligacion_los_informes_de_gestion_de_riesgos_deben_comunicar_de_forma_clara_y_concisa_info_9b528e -> Sujeto_propuesto_los_informes_de_gestion_de_riesgos
idx 16425: Obligacion_los_informes_de_gestion_de_riesgos_tienen_que_ser_faciles_de_entender_y_lo_sufic_4c535a -> Sujeto_propuesto_los_informes_de_gestion_de_riesgos
idx 16463: Obligacion_los_integrantes_del_consejo_de_administracion_en_las_cooperativas_deberan_contin_5f2a56 -> Sujeto_propuesto_las_cooperativas
idx 16477: Obligacion_los_inversores_extranjeros_de_actividad_financiera_autorizada_regulada_y_supervi_54991c -> Sujeto_propuesto_inversores_extranjeros_de_actividad_financiera_autorizada_regulada_y_supervisada
idx 16479: Obligacion_los_inversores_nacionales_considerados_sujetos_obligados_de_actividad_financiera_35de47 -> Sujeto_propuesto_inversores_nacionales_considerados_sujetos_obligados_de_actividad_financiera_reg
idx 16509: Obligacion_los_limites_deben_ser_aprobados_por_el_directorio__lingeef_5_3_2_65b169 -> Sujeto_propuesto_tales_limites
idx 16511: Obligacion_los_limites_deben_ser_establecidos_por_escrito_en_forma_clara_detallando_el_nive_0738b5 -> Sujeto_propuesto_tales_limites
idx 16513: Obligacion_los_limites_deben_ser_implementados_mediante_un_marco_comprehensivo_para_el_apet_30cf23 -> Sujeto_propuesto_tales_limites
idx 16540: Obligacion_los_millares_o_packs_deben_poseer_en_su_interior_una_contrafaja_o_etiqueta_debid_7d0baa -> Sujeto_propuesto_los_millares_o_packs
idx 16568: Obligacion_los_planes_de_respuesta_y_recuperacion_deberan_ser_mejorados_continuamente_media_be2487 -> Sujeto_propuesto_estos_planes
idx 16592: Obligacion_los_procedimientos_para_la_gestion_del_riesgo_pais_deben_contemplar_la_revision__52b082 -> Sujeto_propuesto_los_procedimientos_para_la_gestion_del_riesgo_pais
idx 16611: Obligacion_los_procesos_deben_establecer_criterios_para_identificar_y_reportar_operaciones__3bedc7 -> Sujeto_propuesto_tales_procesos
idx 16621: Obligacion_los_programas_de_pruebas_de_estres_deben_contemplar_la_vision_de_distintas_areas_f6b56f -> Sujeto_propuesto_los_programas_de_pruebas_de_estres
idx 16632: Obligacion_los_programas_de_pruebas_de_estres_deben_incluir_escenarios_prospectivos_para_in_ffd7b1 -> Sujeto_propuesto_los_programas_de_pruebas_de_estres
idx 16638: Obligacion_los_programas_de_pruebas_de_estres_deben_promover_la_identificacion_y_control_de_bb468b -> Sujeto_propuesto_los_programas_de_pruebas_de_estres
idx 16640: Obligacion_los_programas_de_pruebas_de_estres_deben_ser_administrados_con_flexibilidad_para_70a627 -> Sujeto_propuesto_estos_programas
idx 16647: Obligacion_los_promotores_y_fundadores_que_representen_no_menos_del_25_del_capital_y_votos__28f450 -> Sujeto_propuesto_los_promotores_y_fundadores
idx 16649: Obligacion_los_puestos_de_promocion_deberan_estar_destinados_a_brindar_asesoramiento_y_a_en_c6794c -> Sujeto_propuesto_los_puestos_de_promocion
idx 16655: Obligacion_los_relevamientos_deben_contener_claramente_el_flujo_de_la_transaccion_el_ambien_ae1d57 -> Sujeto_propuesto_los_relevamientos
idx 16659: Obligacion_los_requisitos_de_precision_deben_estar_basados_en_los_procesos_y_resultados_de__89017d -> Sujeto_propuesto_los_requisitos_de_precision
idx 16664: Obligacion_los_responsables_de_cada_proceso_establecido_en_la_entidad_deberan_velar_por_el__73cefd -> Sujeto_propuesto_los_mencionados_responsables
idx 16666: Obligacion_los_responsables_de_cada_proceso_establecido_en_la_entidad_seran_quienes_deban_d_51fba1 -> Sujeto_propuesto_los_responsables_de_cada_proceso_establecido_en_la_entidad
idx 16668: Obligacion_los_responsables_de_cada_proceso_establecido_en_la_entidad_tendran_a_su_cargo_el_e9a5ea -> Sujeto_propuesto_los_responsables_de_cada_proceso_establecido_en_la_entidad
idx 16670: Obligacion_los_responsables_de_la_gestion_deben_mantener_una_relacion_fluida_con_aquellos_q_fc3cac -> Sujeto_propuesto_los_responsables_de_la_gestion
idx 16672: Obligacion_los_responsables_de_los_datos_en_colaboracion_con_los_gerentes_de_riesgos_o_auto_1e2a82 -> Sujeto_propuesto_los_responsables_de_los_datos
idx 16728: Obligacion_los_resultados_por_transacciones_expresados_en_moneda_del_periodo_no_se_ajustara_b9fe95 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 16735: Obligacion_los_saldos_que_se_incluyen_en_un_rubro_por_su_naturaleza_aunque_sean_menos_liqui_66c391 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 16774: Obligacion_los_sistemas_de_informacion_deben_cumplir_con_requisitos_que_se_enumeran_a_conti_05f367 -> Sujeto_propuesto_estos_sistemas
idx 16823: Obligacion_los_solicitantes_deberan_completar_y_firmar_una_solicitud_de_prestamo__manori_1__eba4b9 -> Sujeto_propuesto_los_solicitantes
idx 16839: Obligacion_los_solicitantes_deberan_presentar_copia_del_documento_de_identidad_conforme_a_l_7808ed -> Sujeto_propuesto_los_solicitantes
idx 16843: Obligacion_los_solicitantes_deberan_presentar_toda_la_documentacion_respaldatoria_necesaria_bb32c6 -> Sujeto_propuesto_los_solicitantes
idx 16845: Obligacion_los_solicitantes_empleados_en_relacion_de_dependencia_deberan_presentar_constanc_2b5743 -> Sujeto_propuesto_los_solicitantes
idx 16847: Obligacion_los_solicitantes_empleados_en_relacion_de_dependencia_deberan_presentar_copia_de_f64cf7 -> Sujeto_propuesto_los_solicitantes
idx 16849: Obligacion_los_solicitantes_trabajadores_autonomos_y_monotributistas_deberan_presentar_cons_32c4d5 -> Sujeto_propuesto_los_solicitantes
idx 16851: Obligacion_los_solicitantes_trabajadores_autonomos_y_monotributistas_deberan_presentar_cons_7310d8 -> Sujeto_propuesto_los_solicitantes
idx 16853: Obligacion_los_solicitantes_trabajadores_autonomos_y_monotributistas_deberan_presentar_deta_17fa2e -> Sujeto_propuesto_los_solicitantes
idx 16855: Obligacion_los_solicitantes_trabajadores_autonomos_y_monotributistas_deberan_presentar_deta_7ee525 -> Sujeto_propuesto_los_solicitantes
idx 16880: Obligacion_luego_de_la_determinacion_del_encolamiento_de_la_transaccion_los_esquemas_de_pag_19c588 -> Sujeto_propuesto_los_esquemas_de_pago
idx 16883: Obligacion_manifestar_en_declaracion_jurada_acerca_de_si_han_sido_sancionadas_con_inhabilit_42233e -> Sujeto_propuesto_cada_uno_de_los_accionistas_e_integrantes_de_los_organos_de_gobierno_de_administ
idx 16885: Obligacion_manifestar_en_declaracion_jurada_acerca_de_si_han_sido_sancionadas_con_inhabilit_57504a -> Sujeto_propuesto_cada_uno_de_los_accionistas_e_integrantes_de_los_organos_de_gobierno_de_administ
idx 16887: Obligacion_manifestar_en_declaracion_jurada_acerca_de_si_han_sido_sancionadas_con_multa_por_189a66 -> Sujeto_propuesto_cada_uno_de_los_accionistas_e_integrantes_de_los_organos_de_gobierno_de_administ
idx 16889: Obligacion_manifestar_en_declaracion_jurada_que_no_figuran_en_las_resoluciones_sobre_financ_dea76a -> Sujeto_propuesto_cada_uno_de_los_accionistas_e_integrantes_de_los_organos_de_gobierno_de_administ
idx 16891: Obligacion_manifestar_en_declaracion_jurada_que_no_han_sido_condenadas_por_delitos_de_lavad_ad50d0 -> Sujeto_propuesto_cada_uno_de_los_accionistas_e_integrantes_de_los_organos_de_gobierno_de_administ
idx 16893: Obligacion_manifestar_en_declaracion_jurada_que_no_han_sido_designadas_por_el_comite_de_seg_87d1a8 -> Sujeto_propuesto_cada_uno_de_los_accionistas_e_integrantes_de_los_organos_de_gobierno_de_administ
idx 16940: Obligacion_notificar_a_la_sefyc_el_cumplimiento_de_los_requisitos_para_que_se_expida_al_res_bea8b8 -> Sujeto_propuesto_las_autorizaciones_que_se_otorguen_para_la_fusion_de_entidades
idx 16958: Obligacion_obligacion_de_consignar_la_integracion_total_del_mes_por_cada_especie_de_titulos_7e5c68 -> Sujeto_propuesto_las_entidades__ri_rml
idx 16960: Obligacion_obligacion_de_consignar_la_integracion_total_del_mes_teniendo_en_cuenta_que_para_8fc76b -> Sujeto_propuesto_las_entidades__ri_rml
idx 16978: Obligacion_obligacion_de_informar_el_importe_total_de_los_conceptos_de_exigencia_del_mes_en_fd55f7 -> Sujeto_propuesto_las_entidades__ri_rml
idx 16980: Obligacion_obligacion_de_informar_el_total_de_exigencia_en_moneda_extranjera_que_surja_de_a_7d6866 -> Sujeto_propuesto_las_entidades__ri_rml
idx 16991: Obligacion_obligacion_de_informar_el_total_de_exigencia_en_pesos_que_surja_de_aplicar_la_ta_0b35a4 -> Sujeto_propuesto_las_entidades__ri_rml
idx 16995: Obligacion_obligacion_de_informar_la_exigencia_del_mes_sobre_depositos_a_plazo_fijo_de_titu_34253f -> Sujeto_propuesto_las_entidades__ri_rml
idx 16997: Obligacion_obligacion_de_informar_la_exigencia_del_mes_sobre_depositos_y_obligaciones_a_pla_64a1e9 -> Sujeto_propuesto_las_entidades__ri_rml
idx 17064: Obligacion_para_aquellos_objetivos_no_cumplidos_la_auditoria_interna_debera_considerar_el_e_dfda2f -> Sujeto_propuesto_la_auditoria_interna
idx 17068: Obligacion_para_cada_actividad_de_control_identificada_dentro_de_cada_ciclo_la_auditoria_in_1b41de -> Sujeto_propuesto_la_auditoria_interna
idx 17073: Obligacion_para_cada_grupo_de_contrapartes_conectadas_se_utilizara_un_numero_ascendente_cor_1dacde -> Sujeto_propuesto_las_entidades
idx 17078: Obligacion_para_cada_uno_de_los_objetivos_no_cumplidos_el_auditor_debe_analizar_y_documenta_d93636 -> Sujeto_propuesto_el_auditor
idx 17114: Obligacion_para_determinar_la_estructura_de_plazos_residuales_de_depositos_a_plazo_fijo_de__034b95 -> Sujeto_propuesto_las_entidades__ri_rml
idx 17173: Obligacion_para_documentar_los_controles_de_las_aplicaciones_se_debe_utilizar_un_proceso_de_cb4188 -> Sujeto_propuesto_la_auditoria_interna
idx 17224: Obligacion_para_el_calculo_del_aporte_al_fondo_de_garantia_de_los_depositos_se_deberan_cons_3e6ae1 -> Sujeto_propuesto_las_entidades__ri_rml
idx 17269: Obligacion_para_el_caso_de_siniestros_en_la_propiedad_el_administrador_debe_determinar_si_l_350f5f -> Sujeto_propuesto_el_administrador
idx 17289: Obligacion_para_incluir_el_detalle_de_la_s_franquicia_s_otorgada_s_por_el_bcra_debera_utili_1102d9 -> Sujeto_propuesto_las_entidades__ri_rml
idx 17336: Obligacion_para_las_entidades_mas_sofisticadas_la_evaluacion_de_la_suficiencia_del_capital__0baa6c -> Sujeto_propuesto_las_entidades_mas_sofisticadas
idx 17355: Obligacion_para_los_periodos_anteriores_a_agosto_2014_ya_validados_el_importe_del_codigo_99_9b05a2 -> Sujeto_propuesto_las_entidades__ri_pgn
idx 17357: Obligacion_para_los_tipos_de_registro_1_y_2_las_entidades_deben_utilizar_codigos_0_4_en_el__fac9bb -> Sujeto_propuesto_las_entidades__snp_cheq
idx 17374: Obligacion_para_realizar_la_compensacion_electronica_de_las_transferencias_las_entidades_de_767915 -> Sujeto_propuesto_las_entidades__snp_tr
idx 17376: Obligacion_para_resultados_de_medicion_a_valor_razonable_de_activos_no_monetarios_comparar__d37417 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 17400: Obligacion_ponderar_el_nivel_de_probidad_e_integridad_moral_de_la_persona_considerando_si_h_0a3cf7 -> Sujeto_propuesto_la_persona
idx 17421: Obligacion_presentacion_de_declaracion_jurada_sobre_antecedentes_personales_y_penales_de_la_eefe4f -> Sujeto_propuesto_las_personas_a_que_se_refieren_los_puntos_1_3_6_1_3_7_y_1_3_8
idx 17453: Obligacion_presentacion_de_la_declaracion_jurada_sobre_la_condicion_de_persona_expuesta_pol_048e7c -> Sujeto_propuesto_las_personas_a_que_se_refieren_los_puntos_1_3_6_1_3_7_y_1_3_8
idx 17485: Obligacion_presentar_datos_con_formalidades_ricm__ri_pgn_s1_f086c3 -> Sujeto_propuesto_los_datos
idx 17487: Obligacion_presentar_declaracion_jurada_manifestando_que_no_les_alcanza_ninguna_de_las_inha_40618c -> Sujeto_propuesto_cada_uno_de_los_accionistas_e_integrantes_de_los_organos_de_gobierno_de_administ
idx 17591: Obligacion_quienes_accedan_al_servicio_de_descarga_de_archivos_de_cheques_y_deudores_deben__741d0b -> Sujeto_propuesto_aquellos_que_seleccionen_esta_opcion
idx 17593: Obligacion_quienes_administren_sistemas_de_almacenamiento_de_valores_compensables_deben_efe_295e4c -> Sujeto_propuesto_quienes_administren_sistemas_de_almacenamiento_de_valores_compensables
idx 17595: Obligacion_quienes_administren_sistemas_de_almacenamiento_de_valores_compensables_deben_per_e83370 -> Sujeto_propuesto_quienes_administren_sistemas_de_almacenamiento_de_valores_compensables
idx 17597: Obligacion_quienes_administren_sistemas_de_almacenamiento_de_valores_compensables_deben_reg_0b04b7 -> Sujeto_propuesto_quienes_administren_sistemas_de_almacenamiento_de_valores_compensables
idx 17599: Obligacion_quienes_seleccionen_la_opcion_de_acceso_publico_general_deberan_prestar_declarac_b6fd90 -> Sujeto_propuesto_aquellos_que_seleccionen_esta_opcion
idx 17605: Obligacion_realizar_arqueo_sorpresivo_de_los_documentos_garantias_que_respaldan_la_cartera__80c751 -> Sujeto_propuesto_las_cajas_de_credito
idx 17676: Obligacion_reexpresion_de_saldos_iniciales_de_partidas_no_monetarias_al_cierre_de_cada_mes__21e0dd -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 17678: Obligacion_reexpresion_monetaria_del_capital_social_y_aportes_no_capitalizados_se_imputa_en_14d179 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 17779: Obligacion_remitir_billetes_sin_valor_entintados_o_adulterados_al_bcra_conforme_al_procedim_b8d311 -> Sujeto_propuesto_entidades
idx 17784: Obligacion_remitir_los_archivos_a_la_cec_antes_del_inicio_del_periodo_descripto_en_el_punto_d8fcb6 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 17789: Obligacion_remitir_un_plan_de_negocios_y_proyecciones_contemplando_un_periodo_de_cinco_anos_6f6274 -> Sujeto_propuesto_personas_que_reunan_la_condicion_de_futuros_fundadores
idx 17807: Obligacion_respecto_de_la_nomina_prevista_en_el_cuarto_parrafo_del_punto_4_1_en_el_caso_de__ac202f -> Sujeto_propuesto_las_asociaciones_de_profesionales
idx 17812: Obligacion_resultado_de_posicion_monetaria_calculado_como_producto_del_saldo_inicial_de_cad_21827c -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 17822: Obligacion_revisar_la_registracion_y_pago_de_los_retornos_y_otras_distribuciones_de_utilida_88d0df -> Sujeto_propuesto_los_organos_de_la_entidad
idx 17833: Obligacion_revisar_politicas_sobre_rtici_periodicamente__lingeef_5_3_2_821c58 -> Sujeto_propuesto_todas_las_politicas_sobre_el_rtici
idx 17847: Obligacion_se_agregara_una_descripcion_detallada_del_calculo_de_la_franquicia_para_el_perio_fecb50 -> Sujeto_propuesto_las_entidades__ri_rml
idx 17934: Obligacion_se_debe_demostrar_que_las_politicas_y_procedimientos_son_adecuados_en_virtud_de__3b756f -> Sujeto_propuesto_esas_politicas_y_procedimientos
idx 18078: Obligacion_se_incluiran_los_importes_que_surjan_como_consecuencia_de_la_aplicacion_de_franq_4d1548 -> Sujeto_propuesto_las_entidades__ri_rml
idx 18081: Obligacion_se_incrementaran_los_valores_en_una_unidad_cuando_el_primer_digito_de_las_fracci_f2bdf6 -> Sujeto_propuesto_los_valores
idx 18084: Obligacion_se_informara_el_cumplimiento_de_la_medida_de_tenencia_de_certificado_de_aptitud__2421e1 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 18086: Obligacion_se_informara_el_cumplimiento_de_la_tenencia_de_certificado_de_aptitud_en_recinto_188761 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 18144: Obligacion_se_llevara_adelante_la_sesion_de_rechazados_correspondiente_a_los_archivos_prese_2693a6 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 18151: Obligacion_se_recomienda_cumplir_en_lo_que_se_relaciona_con_cada_ciclo_como_minimo_con_las__09c85f -> Sujeto_propuesto_se_recomienda
idx 18194: Obligacion_si_el_auditor_externo_no_hubiera_observado_deficiencias_significativas_en_el_sis_fc69cb -> Sujeto_propuesto_el_auditor_externo
idx 18198: Obligacion_si_el_donante_no_cuenta_con_una_cuenta_abierta_a_su_nombre_requerirle_que_inform_a41360 -> Sujeto_propuesto_se_le_debera_requerir
idx 18200: Obligacion_si_el_feriado_local_imprevisto_es_conocido_con_antelacion_suficiente_las_entidad_590b3d -> Sujeto_propuesto_las_entidades__snp_cheq
idx 18227: Obligacion_si_la_administradora_no_recibe_el_resumen_dentro_del_plazo_de_8_dias_debe_reclam_113e5d -> Sujeto_propuesto_la_administradora
idx 18240: Obligacion_si_la_prestataria_deja_de_cumplir_con_la_condicion_de_mipyme_se_computaran_las_f_17005f -> Sujeto_propuesto_la_prestataria
idx 18277: Obligacion_si_los_archivos_superan_todas_las_validaciones_la_entidad_que_recibio_la_informa_c55fef -> Sujeto_propuesto_la_entidad_que_recibio_la_informacion
idx 18283: Obligacion_si_no_existieran_objetivos_no_cumplidos_se_lo_debera_indicar_expresamente__nmcie_70c95c -> Sujeto_propuesto_la_auditoria_interna
idx 18286: Obligacion_si_no_se_cuenta_con_la_informacion_el_funcionario_responsable_interviniente_debe_154068 -> Sujeto_propuesto_el_funcionario_responsable_interviniente
idx 18325: Obligacion_suministrar_al_receptor_de_la_transferencia_el_importe_total_transferido__snp_tr_074fc6 -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 18327: Obligacion_suministrar_al_receptor_de_la_transferencia_el_nombre_del_cliente_ordenante_cuan_ae89a3 -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 18329: Obligacion_suministrar_al_receptor_de_la_transferencia_el_numero_de_cuit_cuil_o_cdi_del_cli_b98d7f -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 18331: Obligacion_suministrar_al_receptor_de_la_transferencia_la_fecha_de_la_transferencia__snp_tr_5ad592 -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 18333: Obligacion_suministrar_al_receptor_de_la_transferencia_la_referencia_univoca_de_la_transfer_ecbe4d -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 18349: Obligacion_tanto_en_los_resumenes_como_en_cualquier_extracto_de_cuenta_en_forma_impresa_o_d_f326c4 -> Sujeto_propuesto_las_entidades__snp_tr
idx 18377: Obligacion_todas_las_entidades_participantes_aceptaran_como_verdaderas_las_informaciones_in_9433a1 -> Sujeto_propuesto_todas_las_entidades_participantes
idx 18401: Obligacion_todo_el_personal_debe_ser_responsable_de_comunicar_en_forma_ascendente_problemas_38b396 -> Sujeto_propuesto_todo_el_personal__ri_ccna
idx 18403: Obligacion_todo_el_personal_debe_ser_responsable_de_comunicar_en_forma_ascendente_problemas_dac045 -> Sujeto_propuesto_todo_el_personal
idx 18413: Obligacion_todos_los_estados_financieros_y_sus_anexos_deben_estar_expresados_en_moneda_homo_d9ccab -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 18417: Obligacion_todos_los_integrantes_del_comite_de_direccion_ejecutivo_deberan_demostrar_experi_3fb65e -> Sujeto_propuesto_todos_sus_integrantes
idx 18419: Obligacion_todos_los_requisitos_establecidos_en_las_exigencias_de_la_fusion_deberan_quedar__22fa39 -> Sujeto_propuesto_las_autorizaciones_que_se_otorguen_para_la_fusion_de_entidades
idx 18460: Obligacion_una_vez_documentado_el_primer_aspecto_debe_ponerse_especial_atencion_en_el_cumpl_2c6276 -> Sujeto_propuesto_la_auditoria_interna
idx 18465: Obligacion_una_vez_identificadas_y_documentadas_las_actividades_de_control_la_auditoria_int_c32a52 -> Sujeto_propuesto_la_auditoria_interna
idx 18472: Obligacion_utilizacion_del_aplicativo_antecedentes_personales_de_autoridades_de_entidades_f_70666e -> Sujeto_propuesto_las_personas_a_que_se_refieren_los_puntos_1_3_6_1_3_7_y_1_3_8
idx 18481: Obligacion_validar_la_efectividad_de_los_procedimientos_para_sustentar_los_modelos_de_acces_e3658e -> Sujeto_propuesto_la_auditoria_interna
idx 18492: Obligacion_verificar_el_orden_secuencial_de_lotes_y_registros_individuales_en_los_archivos__f07fcd -> Sujeto_propuesto_las_entidades__snp_cheq
idx 18497: Obligacion_verificar_la_ausencia_de_caracteres_invalidos_en_los_archivos_intercambiados_ele_aff80a -> Sujeto_propuesto_las_entidades__snp_cheq
idx 18512: Obligacion_verificar_la_implementacion_de_mecanismos_para_asegurar_que_las_actividades_de_t_401fce -> Sujeto_propuesto_la_auditoria_interna
idx 18541: Obligacion_verificar_que_la_estrategia_de_seguridad_de_la_informacion_este_alineada_con_la__0d6ee2 -> Sujeto_propuesto_la_auditoria_interna
idx 18543: Obligacion_verificar_que_la_informacion_en_los_archivos_intercambiados_electronicamente_sea_f51b78 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 18549: Obligacion_verificar_que_las_directivas_de_seguridad_definan_los_metodos_utilizados_para_la_ab5836 -> Sujeto_propuesto_la_auditoria_interna
idx 18570: Obligacion_verificar_que_se_consideren_los_factores_de_autenticacion_la_validacion_y_el_can_f0adfd -> Sujeto_propuesto_la_auditoria_interna
idx 18572: Obligacion_verificar_que_se_consideren_los_resultados_de_los_analisis_de_riesgos_y_el_cumpl_00d4b8 -> Sujeto_propuesto_la_auditoria_interna
idx 18585: Operacion_acceso_a_base_de_datos_en_sitio_seguro__ceninf_4_1_78aec0 -> Sujeto_propuesto_administradores_de_carteras_crediticias_de_ex_entidades_financieras
idx 18600: Operacion_acondicionamiento_de_billetes_en_millares_o_packs__cirmo3_5_3_1_1_d11f6c -> Sujeto_propuesto_transportadora_de_valores
idx 18841: Operacion_apertura_de_cuenta_especial_para_exportadores__depaho_3_13_1_2_364272 -> Sujeto_propuesto_los_entes_que_reciban_asistencias_financieras_y_o_aportes_no_reintegrables_de_or
idx 19166: Operacion_calculo_posicion_global_neta_positiva_atenuacion_incumplimiento__ri_pgn_6_1_b8837f -> Sujeto_propuesto_las_entidades__ri_pgn
idx 19431: Operacion_clasificacion_de_partidas_monetarias_y_no_monetarias__ri_dcpc_3_7_5_7e81c9 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 19619: Operacion_consignacion_de_excesos_a_limites__ri_gerc_2_5_29f893 -> Sujeto_propuesto_las_entidades
idx 19633: Operacion_constitucion_de_fiadora_solidaria__ri_ccna_d1f5_s0_90e6cd -> Sujeto_propuesto_asociaciones_de_profesionales_universitarios
idx 19825: Operacion_declaracion_de_existencias_de_denominaciones_en_rueda_num_d__cirmo3_5_2_2_8_35de20 -> Sujeto_propuesto_las_entidades__cirmo3
idx 19828: Operacion_declaracion_jurada_de_no_alcance_tributario__ayccef_6_3_1_2_e354da -> Sujeto_propuesto_sujetos_no_obligados_a_esos_tributos
idx 20188: Operacion_difusion_de_informacion_por_deudor__ceninf_s4_585df0 -> Sujeto_propuesto_administradores_de_carteras_crediticias_de_ex_entidades_financieras
idx 20189: Operacion_difusion_de_informacion_por_deudor__ceninf_s4_585df0 -> Sujeto_propuesto_sociedades_de_garantia_reciproca_y_fondos_de_garantia_de_caracter_publico_inscri
idx 20551: Operacion_estimacion_deterioro_activos_financieros_niif_9__ri_dcpc_7_1_7529e5 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 20642: Operacion_excesos_posicion_a_termino_operaciones_pase_no_computables__ri_pgn_6_1_33c575 -> Sujeto_propuesto_las_entidades__ri_pgn
idx 21055: Operacion_gestion_de_echeq__snp_cheq_3_4_3_2_4526ab -> Sujeto_propuesto_infraestructuras_de_mercado_financiero_sistemicamente_importantes
idx 21304: Operacion_informe_de_posiciones_en_letras_del_tesoro_nacional__ri_pgn_6_4_2248d3 -> Sujeto_propuesto_las_entidades__ri_pgn
idx 21346: Operacion_instalacion_de_centro_de_transmision__snp_cheq_2_2_2_4_ea3872 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 21348: Operacion_instalacion_de_centro_de_transmision__snp_tr_1_1_2_994287 -> Sujeto_propuesto_las_entidades__snp_tr
idx 21538: Operacion_liquidacion_de_saldos_compensados_entre_entidades__snp_cheq_s2_fa61b7 -> Sujeto_propuesto_entidades__snp_cheq
idx 21682: Operacion_notificacion_de_resolucion_de_autorizacion__cajasc_1_7_b65ed7 -> Sujeto_propuesto_los_solicitantes__cajasc
idx 21928: Operacion_participacion_directa_como_miembro_pleno__snp_cheq_2_2_1_baada9 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 21937: Operacion_participacion_indirecta_mediante_representante__snp_cheq_2_2_1_3a2d61 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 22422: Operacion_recepcion_de_archivos_de_compensacion__snp_cheq_3_1_3_2_5ef8b1 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 22545: Operacion_reduccion_de_exigencia_de_efectivo_minimo_grupo_a_y_g_sib__efemin_7_2_1_a77f15 -> Sujeto_propuesto_las_sucursales_o_subsidiarias_de_bancos_del_exterior_calificados_como_sistemicam
idx 22688: Operacion_remision_de_billetes_al_bcra__cirmo3_3_2_3_830150 -> Sujeto_propuesto_transportadoras_de_valores
idx 23077: Operacion_transmision_de_archivos_cedip_a_cec__snp_cheq_3_6_4_1_2_1a239e -> Sujeto_propuesto_las_entidades__snp_cheq
idx 23219: Potestad_acceso_publico_general_con_clave_arca__el_mecanismo_de_consulta_estara_disponibl_8ec20d -> Sujeto_propuesto_el_publico_en_general
idx 23301: Potestad_autorizacion_de_menores_para_operar_cuentas__los_representantes_legales_pueden_a_21fd7c -> Sujeto_propuesto_sus_representantes_legales
idx 23314: Potestad_autorizacion_modalidades_integracion_grupo_a_a_partir_febrero_2019__a_partir_de__7237a2 -> Sujeto_propuesto_las_entidades_citadas_en_el_parrafo_anterior
idx 23417: Potestad_coordinacion_con_auditor_externo_para_alcance_de_procedimientos__el_responsable__6afe3d -> Sujeto_propuesto_el_responsable_del_control_interno
idx 23446: Potestad_cursar_transferencias_inmediatas_sin_solicitudes_especiales__facultad_de_cursar__f3087d -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 23494: Potestad_derivar_billetes_al_bcra_previa_consulta__los_bancos_minoristas_y_las_transporta_c5c694 -> Sujeto_propuesto_las_transportadoras_de_valores
idx 23519: Potestad_disponibilidad_para_sujetos_enumerados__la_informacion_quedara_a_disposicion_de__a32197 -> Sujeto_propuesto_administradores_de_carteras_crediticias_de_ex_entidades_financieras
idx 23527: Potestad_documentacion_electronica_del_libro_especial__el_libro_especial_de_control_inter_b5c53a -> Sujeto_propuesto_la_entidad
idx 23537: Potestad_eleccion_entre_participacion_directa_e_indirecta__las_entidades_pueden_elegir_pa_5444ea -> Sujeto_propuesto_las_entidades__snp_tr
idx 23542: Potestad_encolamiento_admisible_transferencias_inmediatas_con_acuerdo_cliente__el_encolam_15eeb0 -> Sujeto_propuesto_las_entidades__snp_tr
idx 23592: Potestad_facultad_de_abrir_caja_de_ahorros_sin_intervencion_de_representantes__las_person_f5469c -> Sujeto_propuesto_las_personas_menores_de_edad
idx 23603: Potestad_facultad_de_acceso_a_informacion_de_cheques_y_deudores__el_publico_en_general_ti_2c1577 -> Sujeto_propuesto_el_publico_en_general
idx 23606: Potestad_facultad_de_apertura_asociaciones_beneficiarias__las_simples_asociaciones_benefi_1f8b49 -> Sujeto_propuesto_las_simples_asociaciones_beneficiarias_de_programas_de_ayuda_social_implementado
idx 23619: Potestad_facultad_de_colocar_posturas_bid__las_entidades_demandantes_quedan_facultadas_a__916c67 -> Sujeto_propuesto_las_entidades_demandantes
idx 23631: Potestad_facultad_de_configurar_documentacion_de_controles__las_entidades_tienen_la_facul_8d4d96 -> Sujeto_propuesto_las_entidades__nmcief
idx 23663: Potestad_facultad_de_elegir_otros_sistemas_de_amortizacion__las_entidades_financieras_que_bef1f7 -> Sujeto_propuesto_las_entidades__manori
idx 23671: Potestad_facultad_de_ingresar_informacion_de_pago_cobro__la_empresa_deudora_y_la_mipyme_o_da9570 -> Sujeto_propuesto_la_empresa_deudora_y_la_mipyme_o_quien_la_suceda_como_acreedor_del_pago_dentro_d
idx 23702: Potestad_facultad_de_ofrecer_gestion_imf_autorizadas_o_gestoras__toda_imf_que_el_bcra_aut_fe4473 -> Sujeto_propuesto_toda_imf_que_el_bcra_autorice_a_ese_efecto_o_que_sea_gestora_de_echeq_y_fcem
idx 23705: Potestad_facultad_de_otorgar_prestamos_hipotecarios_bajo_distintas_tipologias__las_entida_01f00b -> Sujeto_propuesto_las_entidades__manori
idx 23740: Potestad_facultad_de_realizar_rechazos__las_entidades_quedan_facultadas_a_realizar_rechaz_8aebb4 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 23748: Potestad_facultad_de_realizar_rechazos__las_entidades_tienen_la_facultad_de_realizar_rech_324e8d -> Sujeto_propuesto_las_entidades__snp_cheq
idx 23764: Potestad_facultad_de_ser_cotitulares_de_representantes_legales__los_representantes_legale_bfbee7 -> Sujeto_propuesto_sus_representantes_legales
idx 23767: Potestad_facultad_de_solicitar_retransmision_de_archivo__las_entidades_quedan_facultadas__17f031 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 23775: Potestad_facultad_de_solicitar_retransmision_de_archivo__las_entidades_se_reservan_el_der_a84dbf -> Sujeto_propuesto_las_entidades__snp_cheq
idx 23783: Potestad_facultad_de_solicitar_retransmision_de_archivo__las_entidades_tienen_la_facultad_7b35c4 -> Sujeto_propuesto_las_entidades__snp_tr
idx 23935: Potestad_facultad_sistemas_contables_con_mayor_numero_de_cuentas__los_sistemas_contables__375e9d -> Sujeto_propuesto_los_sistemas_contables_internos
idx 23970: Potestad_incremento_de_limites_minimos__los_limites_minimos_podran_ser_incrementados__snp_d2a3b1 -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 23993: Potestad_integracion_con_leliq_y_o_nobac_incrementos_exigencia__se_autoriza_a_las_entidad_663475 -> Sujeto_propuesto_las_entidades__ri_rml
idx 24051: Potestad_involucrar_personal_de_otras_areas__la_unidad_encargada_de_la_gestion_del_riesgo_77fe0e -> Sujeto_propuesto_la_unidad_encargada_de_la_gestion_del_riesgo_operacional
idx 24114: Potestad_opcion_de_recurrir_a_centro_de_transmision_alterno__las_entidades_afectadas_por__66006d -> Sujeto_propuesto_las_que_se_vieran_afectadas__snp_cheq
idx 24154: Potestad_opcion_prorrateo_impacto_niif_9_grupos_b_y_c__las_entidades_de_los_grupos_b_y_c__b2225a -> Sujeto_propuesto_las_entidades_pertenecientes_a_los_grupos_b_y_c
idx 24221: Potestad_opcion_recurrir_centro_transmision_otra_entidad__facultad_de_las_entidades_afect_b8eb72 -> Sujeto_propuesto_las_que_se_vieran_afectadas
idx 24237: Potestad_pacto_libre_de_plazo_caucion_con_entidades_financieras__las_partes_quedan_facult_22f364 -> Sujeto_propuesto_las_partes
idx 24277: Potestad_presentacion_en_bcra_despues_de_90_dias__despues_de_cumplidos_los_90_dias_el_ten_28dfd6 -> Sujeto_propuesto_el_tenedor
idx 24481: Potestad_solicitar_personalmente_resumen_de_cuenta__el_beneficiario_podra_solicitar_perso_65ba91 -> Sujeto_propuesto_el_beneficiario
idx 24558: Potestad_transmision_de_archivos_durante_la_jornada_hasta_horario_limite__las_entidades_t_873c4b -> Sujeto_propuesto_las_entidades__snp_cheq
idx 24576: Potestad_utilizar_otra_definicion_de_ingresos_computables__las_entidades_financieras_tien_0e8a79 -> Sujeto_propuesto_las_entidades__manori
idx 24584: Potestad_verificacion_validez_chc_entidades_tenedores_certificantes__las_entidades_financ_667d22 -> Sujeto_propuesto_los_certificantes
idx 24585: Potestad_verificacion_validez_chc_entidades_tenedores_certificantes__las_entidades_financ_667d22 -> Sujeto_propuesto_los_tenedores_legitimados
idx 24593: Restriccion_a_las_infraestructuras_que_administren_el_sistema_de_almacenamiento_de_echeq_y_a_7aadf8 -> Sujeto_propuesto_las_infraestructuras_que_administren_el_sistema_de_almacenamiento_de_echeq_asi_c
idx 24754: Restriccion_el_auditor_no_debe_incluir_en_el_apartado_de_aclaraciones_especiales_previas_al__91b020 -> Sujeto_propuesto_el_auditor
idx 24770: Restriccion_el_chc_puede_ser_endosado_un_maximo_de_dos_veces__cirmo3_8_1_1_6_367435 -> Sujeto_propuesto_este_documento
idx 24865: Restriccion_el_debito_mep_debe_remitirse_en_el_horario_de_8_00_a_10_00_si_no_se_cumple_no_se_0228f6 -> Sujeto_propuesto_las_entidades__cirmo3
idx 24902: Restriccion_el_efectivo_en_custodia_debe_estar_en_compartimentos_o_sectores_separados_de_los_4897c5 -> Sujeto_propuesto_sus_propios_recursos
idx 25011: Restriccion_el_importe_resultante_de_la_reexpresion_de_activos_no_monetarios_no_debe_exceder_ede9a8 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 25024: Restriccion_el_incumplimiento_en_la_presentacion_de_las_declaraciones_juradas_acarrea_la_apl_5f3a41 -> Sujeto_propuesto_los_obligados
idx 25090: Restriccion_el_menor_autorizado_esta_limitado_a_realizar_debitos_unicamente_por_los_concepto_befc2a -> Sujeto_propuesto_el_menor_autorizado
idx 25153: Restriccion_el_plazo_de_compensacion_entre_entidades_para_cheques_truncados_con_imagen_es_de_48cf6a -> Sujeto_propuesto_entidades__snp_cheq
idx 25156: Restriccion_el_plazo_de_compensacion_entre_entidades_para_cheques_truncados_sin_imagen_no_po_c1b64a -> Sujeto_propuesto_entidades__snp_cheq
idx 25302: Restriccion_el_socio_responsable_no_debe_desempenarse_en_relacion_de_dependencia_en_la_entid_2e2686 -> Sujeto_propuesto_socio_responsable
idx 25304: Restriccion_el_socio_responsable_no_debe_haber_sido_expresamente_inhabilitado_para_ejercer_l_d3120f -> Sujeto_propuesto_socio_responsable
idx 25306: Restriccion_el_socio_responsable_no_puede_ser_persona_condenada_con_inhabilitacion_de_cargos_2400b7 -> Sujeto_propuesto_el_socio_responsable
idx 25346: Restriccion_en_caba_podran_pagarse_billetes_en_buen_uso_en_millares_o_packs_de_8_millares__c_5f53ad -> Sujeto_propuesto_billetes_en_buen_uso
idx 25348: Restriccion_en_caba_podran_pagarse_billetes_nuevos_en_millares_o_pallets__cirmo3_5_4_1_49ff28 -> Sujeto_propuesto_billetes_nuevos
idx 25378: Restriccion_en_la_fase_de_liquidacion_en_cuentas_abiertas_en_el_bcra_solo_pueden_intervenir__2bfc11 -> Sujeto_propuesto_los_miembros_plenos_de_cada_camara
idx 25404: Restriccion_en_ningun_resumen_extracto_de_cuenta_u_otra_forma_de_comunicacion_de_informacion_cf5a0e -> Sujeto_propuesto_las_entidades__snp_tr
idx 25634: Restriccion_la_inclusion_de_una_cuenta_en_el_plan_de_cuentas_no_constituye_por_si_sola_autor_cef203 -> Sujeto_propuesto_las_entidades__ri_dcpc
idx 25847: Restriccion_la_unidad_menor_para_pagos_en_agencias_regionales_sera_de_un_millar__cirmo3_5_4__6b05b9 -> Sujeto_propuesto_pagos_en_agencias_regionales
idx 25921: Restriccion_las_cuentas_no_generaran_comisiones_ni_gastos_de_ninguna_indole_para_el_benefici_f2778d -> Sujeto_propuesto_el_beneficiario
idx 25931: Restriccion_las_dependencias_automatizadas_no_podran_tener_linea_de_cajas_de_atencion_al_pub_3e99e8 -> Sujeto_propuesto_las_dependencias_automatizadas
idx 26005: Restriccion_las_entidades_del_grupo_b_no_podran_hacer_uso_de_la_integracion_con_bote_2020_de_444bab -> Sujeto_propuesto_las_citadas_entidades
idx 26040: Restriccion_las_entidades_del_grupo_b_no_podran_hacer_uso_de_la_integracion_con_leliq_y_o_no_611082 -> Sujeto_propuesto_este_grupo_de_entidades
idx 26075: Restriccion_las_entidades_del_grupo_b_no_podran_informar_las_partidas_824000_001_tp_826000_0_d3d4bb -> Sujeto_propuesto_este_grupo_de_entidades
idx 26359: Restriccion_las_personas_imposibilitadas_para_operar_cuentas_corrientes_bancarias_no_podran__2da880 -> Sujeto_propuesto_las_personas_que_se_encuentren_imposibilitadas_para_operar_cuentas_corrientes_ba
idx 26381: Restriccion_las_tareas_de_revision_del_responsable_del_control_interno_no_podran_delegarse_e_aac32c -> Sujeto_propuesto_el_responsable_del_control_interno
idx 26460: Restriccion_los_auditores_internos_deben_tener_la_capacitacion_y_experiencia_necesarias_para_680674 -> Sujeto_propuesto_los_auditores_internos
idx 26551: Restriccion_los_fondos_depositados_en_la_cuenta_especial_de_regularizacion_deberan_permanece_ae6afe -> Sujeto_propuesto_los_fondos_depositados
idx 26556: Restriccion_los_gerentes_y_puestos_funcionales_de_nivel_superior_deben_poseer_una_adecuada_e_c36b1f -> Sujeto_propuesto_los_gerentes_y_puestos_funcionales_de_nivel_superior
idx 26594: Restriccion_los_miembros_cuyas_obligaciones_excedan_el_limite_establecido_en_el_punto_11_5_1_a14853 -> Sujeto_propuesto_los_miembros
idx 26640: Restriccion_los_promotores_y_fundadores_de_las_entidades_financieras_ni_las_otras_personas_q_24141e -> Sujeto_propuesto_las_otras_personas_que_resulten_titulares_del_5_o_mas_de_su_capital_social_y_o_v
idx 26647: Restriccion_los_requerimientos_via_mep_de_las_entidades_deben_coincidir_exactamente_con_lo_s_293df7 -> Sujeto_propuesto_las_entidades__cirmo3
idx 26659: Restriccion_los_sistemas_contables_internos_no_pueden_contener_cuentas_que_satisfagan_simult_0d7844 -> Sujeto_propuesto_los_sistemas_contables_internos
idx 26668: Restriccion_los_valores_representativos_de_las_participaciones_y_de_las_utilidades_capitaliz_eb8bf5 -> Sujeto_propuesto_los_valores_representativos_de_las_participaciones_y_de_las_utilidades_capitaliz
idx 26689: Restriccion_no_debera_exigirse_que_la_solicitud_de_ampliacion_temporal_de_limites_tenga_una__e526bc -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 26907: Restriccion_no_se_autorizara_a_los_solicitantes_que_figuren_en_las_resoluciones_sobre_financ_7a5677 -> Sujeto_propuesto_los_solicitantes__ayccef
idx 26909: Restriccion_no_se_autorizara_a_los_solicitantes_que_figuren_en_las_resoluciones_sobre_financ_8276c2 -> Sujeto_propuesto_los_solicitantes__ayccef
idx 26911: Restriccion_no_se_autorizara_a_quienes_figuren_en_las_listas_de_terroristas_y_asociaciones_t_b8d5bd -> Sujeto_propuesto_quienes_figuren_en_las_listas_de_terroristas_y_asociaciones_terroristas
idx 26914: Restriccion_no_se_cumple_el_requisito_de_independencia_cuando_el_profesional_auditor_o_algun_963585 -> Sujeto_propuesto_el_profesional_o_alguno_de_sus_socios
idx 26922: Restriccion_no_se_dara_curso_a_ningun_nuevo_pedido_de_autorizacion_hasta_que_transcurra_un_a_3a0c94 -> Sujeto_propuesto_los_postulantes
idx 26930: Restriccion_no_se_debera_utilizar_el_mecanismo_de_consulta_para_extraer_datos_en_forma_masiv_99625d -> Sujeto_propuesto_el_publico_en_general
idx 26942: Restriccion_no_se_permitira_el_encolamiento_de_transacciones_para_el_pago_con_transferencia__df47ef -> Sujeto_propuesto_las_entidades__snp_tr
idx 26944: Restriccion_no_se_permitira_el_encolamiento_de_transacciones_para_la_solicitud_de_pago__snp__cb76d0 -> Sujeto_propuesto_las_entidades__snp_tr
idx 26946: Restriccion_no_se_permitira_el_encolamiento_de_transacciones_para_las_extracciones_definidas_02e275 -> Sujeto_propuesto_las_entidades__snp_tr
idx 26948: Restriccion_no_se_podran_establecer_limites_inferiores_a_los_montos_minimos_senalados_para_t_3d2ee3 -> Sujeto_propuesto_entidades_financieras_proveedores_de_servicios_de_pago
idx 26955: Restriccion_no_se_recibiran_solicitudes_de_ampliacion_de_horario_mep_para_la_transmision_de__334067 -> Sujeto_propuesto_solicitudes_de_ampliacion_de_horario_mep
idx 27012: Restriccion_para_el_punto_1_4_2_el_traslado_se_admitira_unicamente_a_la_posicion_siguiente_e_12e526 -> Sujeto_propuesto_el_traslado
idx 27254: Restriccion_para_nuevas_entidades_autorizadas_a_instalarse_a_partir_de_los_49_meses_de_funci_955046 -> Sujeto_propuesto_nuevas_entidades_autorizadas_a_instalarse
idx 27256: Restriccion_para_nuevas_entidades_autorizadas_a_instalarse_durante_los_primeros_12_meses_de__900104 -> Sujeto_propuesto_nuevas_entidades_autorizadas_a_instalarse
idx 27258: Restriccion_para_nuevas_entidades_autorizadas_a_instalarse_entre_13_y_24_meses_de_funcionami_939cb4 -> Sujeto_propuesto_nuevas_entidades_autorizadas_a_instalarse
idx 27260: Restriccion_para_nuevas_entidades_autorizadas_a_instalarse_entre_25_y_36_meses_de_funcionami_50c770 -> Sujeto_propuesto_nuevas_entidades_autorizadas_a_instalarse
idx 27262: Restriccion_para_nuevas_entidades_autorizadas_a_instalarse_entre_37_y_48_meses_de_funcionami_5674c5 -> Sujeto_propuesto_nuevas_entidades_autorizadas_a_instalarse
idx 27482: Restriccion_se_prohibe_dar_al_automotor_un_uso_para_destinos_ilegales_o_distintos_de_los_man_ab5420 -> Sujeto_propuesto_el_automotor
idx 27510: Restriccion_se_prohibe_la_utilizacion_de_terminales_de_servicios_de_telefonia_movil_y_otros__883599 -> Sujeto_propuesto_las_entidades__ri_mmsef
idx 27536: Restriccion_se_tendra_en_consideracion_si_la_persona_ha_sido_condenada_por_delitos_de_lavado_690b2e -> Sujeto_propuesto_la_persona
idx 27538: Restriccion_se_tendran_en_consideracion_las_informaciones_y_o_sanciones_que_sean_comunicadas_9c5cfa -> Sujeto_propuesto_la_persona
idx 27555: Restriccion_solo_se_presentaran_imagenes_de_cheques_cuyos_importes_superen_el_umbral_fijado__e159d4 -> Sujeto_propuesto_las_entidades__snp_cheq
idx 27567: Restriccion_tasa_de_efectivo_minimo_del_100_para_depositos_en_cuentas_corrientes_de_entidade_ff4b4d -> Sujeto_propuesto_sucursales_o_subsidiarias_de_bancos_del_exterior_calificados_como_sistemicamente
idx 27571: Restriccion_tasa_de_efectivo_minimo_del_10_5_para_depositos_e_inversiones_a_plazo_de_uva_y_u_4d02ed -> Sujeto_propuesto_sucursales_o_subsidiarias_de_bancos_del_exterior_calificados_como_sistemicamente
idx 27575: Restriccion_tasa_de_efectivo_minimo_del_10_5_para_depositos_e_inversiones_a_plazo_de_uva_y_u_a2e79a -> Sujeto_propuesto_las_restantes_entidades_financieras
idx 27586: Restriccion_tasa_de_efectivo_minimo_del_3_5_para_depositos_e_inversiones_a_plazo_de_uva_y_uv_53ab11 -> Sujeto_propuesto_las_restantes_entidades_financieras
idx 27589: Restriccion_tasa_de_efectivo_minimo_del_3_5_para_depositos_e_inversiones_a_plazo_de_uva_y_uv_d1e459 -> Sujeto_propuesto_sucursales_o_subsidiarias_de_bancos_del_exterior_calificados_como_sistemicamente
idx 27595: Restriccion_tasa_de_efectivo_minimo_del_6_5_para_depositos_e_inversiones_a_plazo_de_uva_y_uv_8854bf -> Sujeto_propuesto_sucursales_o_subsidiarias_de_bancos_del_exterior_calificados_como_sistemicamente
idx 27599: Restriccion_tasa_de_efectivo_minimo_del_6_5_para_depositos_e_inversiones_a_plazo_de_uva_y_uv_af296f -> Sujeto_propuesto_las_restantes_entidades_financieras
idx 27602: Restriccion_tasa_de_efectivo_minimo_del_8_5_para_depositos_e_inversiones_a_plazo_de_uva_y_uv_16a292 -> Sujeto_propuesto_las_restantes_entidades_financieras
idx 27605: Restriccion_tasa_de_efectivo_minimo_del_8_5_para_depositos_e_inversiones_a_plazo_de_uva_y_uv_7ff0c0 -> Sujeto_propuesto_sucursales_o_subsidiarias_de_bancos_del_exterior_calificados_como_sistemicamente
```

### S32 — PASS

INFORMATIVA — Cuantía en la descripción => elemento en la lista (informativa; L-ESQ-R2 §1.5 y reports/u_umbral/reporte_u_umbral.md §2): en los tipos con lista de umbrales, un nodo cuya descripción trae una cuantía (reglas_comparacion.detectar_cuantias) tiene la lista no vacía o el umbral guardado (marca); aparte, las cuantías de la descripción sin un elemento de igual valor y unidad.

**Resultado:** 661 nodos con cuantía en la descripción: 661 con lista, 0 con el umbral guardado (marca), 0 sin ninguna {}; cuantías de la descripción 776, sin elemento de igual valor y unidad 112.

Sin violaciones.

## Tabla resumen

| Severidad | Regla | Resultado | Resumen |
|---|---|---|---|
| bloqueante | S1 | PASS | 28320/28320 aristas con relación admitida (19 relaciones admitidas); 0 violaciones. |
| bloqueante | S2 | PASS | 0 aristas colgantes sobre 28320. |
| bloqueante | S3 | PASS | 28320/28320 aristas conformes a firma; 0 violaciones. Evaluadas: 19076 por matriz, 8838 remite_a, 126 de esqueleto, 280 padre_sugerido. |
| bloqueante | S4 | PASS | Nodos OK: 12452/12452. Aristas OK: 28320/28320. Violaciones: 0. |
| bloqueante | S5 | PASS | Nodos con punto: 12452/12452. Aristas: 28320/28320. Violaciones: 0. |
| bloqueante | S6 | PASS | Archivos válidos (57): TextoOrdenado ['adrei.pdf', 'ayccef.pdf', 'cajasc.pdf', 'ceninf.pdf', 'cirmo3.pdf', 'depaho.pdf', 'efemin.pdf', 'expaef.pdf', 'lingeef.pdf', 'manori.pdf', 'nmcief.pdf', 'opefci.pdf', 'ri_ccna.pdf', 'ri_dcpc.pdf', 'ri_gerc.pdf', 'ri_mmsef.pdf', 'ri_pgn.pdf', 'ri_rml.pdf', 'snp_cheq.pdf', 'snp_tr.pdf'] ∪ esqueleto ['TO_capitales_minimos_actual.pdf', 'TO_clasificacion_deudores_actual.pdf', 'TO_exterior_cambios_actual.pdf', 'TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'TO_regimen_informativo_contable_mensual_actual.pdf', 'actgar.pdf', 'autenf.pdf', 'catalogo_sujetos_v3.json', 'ccbcra.pdf', 'convca.pdf', 'cryl.pdf', 'ctacor.pdf', 'esquema_v2_clases.json', 'esquema_v3_clases.json', 'fabcra.pdf', 'icmecma.pdf', 'lavdin.pdf', 'lingob.pdf', 'ordcom.pdf', 'osapsa.pdf', 'pagjub.pdf', 'pfmipyme.pdf', 'pimf.pdf', 'ratiofn.pdf', 'rdbcra.pdf', 'repefe.pdf', 'retype.pdf', 'rmrtsd.pdf', 'rrci.pdf', 'servco.pdf', 'snp_atm.pdf', 'snp_debin.pdf', 'snp_psp.pdf', 'snp_spd.pdf', 'snp_tr_nc.pdf', 'supcon.pdf', 'traval.pdf']. Violaciones: 0. |
| bloqueante | S15 | PASS | 35 roles, 51 aristas miembro_de; 12 huérfanos (12 declarados, 0 sin declarar); 0 miembros que no son clase. Lista declarada: 12 ({'sin_id_en_catalogo': 6, 'aplanamiento_rechazado': 5, 'instancia_rechazada': 1}). |
| bloqueante | S18 | PASS | 358 Restricciones limite_cuantitativo: 341 con lista, 17 con el umbral guardado sin lista (marca), 0 sin ninguna. |
| bloqueante | S19 | PASS | 390 Sujetos ({'clase': 70, 'instancia': 5, 'propuesto': 280, 'rol': 35}); catálogo de 110 ids; 0 fuera del catálogo, 0 con nivel inválido, 0 propuestos incompletos. |
| bloqueante | S20 | PASS | 4751 nodos Obligacion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 0. |
| bloqueante | S24 | PASS | 914 nodos Restriccion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 0. |
| bloqueante | S25 | PASS | 142 nodos Comunicacion; 0 violaciones; fuera de lista con marca: 0 {}; sin valor: 32. |
| bloqueante | S26 | PASS | 12062 nodos evaluados; 0 violaciones {}; marcas de nodo admitidas: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']. |
| bloqueante | S28 | PASS | 280 Sujetos propuestos; 896 filas en el registro; 0 propuestos sin fila. |
| bloqueante | S29 | PASS | 280 aristas padre_sugerido; 0 con destino fuera del catálogo único (110 ids). |
| bloqueante | S30 | PASS | 8838 aristas remite_a ({'externa': 272, 'interna': 8539, 'to_entero': 27}); 0 violaciones. |
| bloqueante | S31 | PASS | 8838 aristas remite_a: {'en_un_tramo_del_chunk_de_la_arista': 8838}; 0 violaciones. |
| bloqueante | S27 | PASS | 4374 aristas de sujeto fuera del esqueleto; 0 sin mención, verificación o método ({}). |
| informativa | S7 | FAIL | 400 grupos violatorios (903 nodos involucrados). |
| informativa | S8 | WARN | 85 grupos con el mismo label normalizado en types distintos. |
| informativa | S9 | PASS | 0 nodos con ambas keys. |
| informativa | S10 | PASS | Sin establecida_en: Condicion=0, Definicion=0, Excepcion=0, Obligacion=0, Operacion=0, Potestad=0, Restriccion=0 (total 0). |
| informativa | S11 | WARN | Sin aplica_a: Excepcion=228, Obligacion=1427, Operacion=2356, Potestad=251, Restriccion=564 (total 4826). |
| informativa | S12 | FAIL | 143 Excepciones sin salida exceptua/exceptua_obligacion. |
| informativa | S21 | WARN | 8838 remisiones ({'interna': 8539, 'externa': 272, 'to_entero': 27}); 27 incoherentes (por alcance: {'to_entero': 27}). |
| informativa | S22 | PASS | 280 aristas padre_sugerido; 0 incoherentes (0 con destino distinto, 0 con origen fuera de cuarentena). |
| informativa | S23 | WARN | 4233 aristas aplica_a; 687 hacia Sujetos propuestos (278 destinos distintos). |
| informativa | S32 | PASS | 661 nodos con cuantía en la descripción: 661 con lista, 0 con el umbral guardado (marca), 0 sin ninguna {}; cuantías de la descripción 776, sin elemento de igual valor y unidad 112. |

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
