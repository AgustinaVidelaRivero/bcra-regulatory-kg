# Material de T4 — aceptadas:no_items (30 fichas; B6.1, tanda final, T3, punto 7.5)

Sorteo: `aceptadas_no_items.json` (51bb8fd0…, 2026-10-20T14:08:58-03:00); material armado a las 2026-10-20T14:09:10-03:00. Sin el estado de E3 ni las marcas de E3.

## 1. `ri_acsf::Sbloque2` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 1):

```
[texto propio | punto Sbloque2]
II.b. Datos sobre las operaciones
Por cada una de las actividades detalladas en la “Tabla de actividades comprendidas” del presente
requerimiento, se deberá consignar:
- la cantidad total mensual de operaciones o servicios realizados durante el período informado
(celdas no grisadas de la tabla)
- el monto total mensual correspondiente a las operaciones realizadas durante el período infor-
mado, en los casos que proceda (celdas no grisadas de la tabla)
```

Versión: final (grafo sin cola). Nodos 4, aristas 5.
- **N1** Obligacion `Obligacion_por_cada_una_de_las_actividades_detalladas_en_la_tabla_de_actividades_comprendid_3dccc4` — Consignar cantidad mensual de operaciones · {"descripcion": "Por cada una de las actividades detalladas en la Tabla de actividades comprendidas, se deberá consignar la cantidad total mensual de operaciones o servicios realizados durante el período informado (celdas no grisadas de la tabla)", "tipo": "presentacion_informativa", "frecuencia": "mensual", "umbrales": [{"tramo": "cantidad total mensual", "comparacion": "no_determinada", "regla_c · tramo: se deberá consignar: - la cantidad total mensual de operaciones o servicios realizados durante el período informado
- **N2** Obligacion `Obligacion_por_cada_una_de_las_actividades_detalladas_en_la_tabla_de_actividades_comprendid_de99ed` — Consignar monto mensual de operaciones · {"descripcion": "Por cada una de las actividades detalladas en la Tabla de actividades comprendidas, se deberá consignar el monto total mensual correspondiente a las operaciones realizadas durante el período informado, en los casos que proceda (celdas no grisadas de la tabla)", "tipo": "presentacion_informativa", "frecuencia": "mensual", "umbrales": [{"tramo": "monto total mensual", "comparacion": · tramo: se deberá consignar: - el monto total mensual correspondiente a las operaciones realizadas durante el período informado, en los casos que proceda
- **N3** Sujeto `Sujeto_propuesto_las_entidades__ri_acsf` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_rol_entidad_comprendida_reginf", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N4** TextoOrdenado `TextoOrdenado_ri_acsf_pdf` — Régimen Informativo Agencias Complementarias · {"archivo": "ri_acsf.pdf", "materia": "RI Cont. Mensual - Agencias complementarias de servicios financieros", "version": "Comunicación A 7618 (vigencia 30/11/2022)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **A2** (extraccion) N2 —aplica_a→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **C1** (catalogo_sujetos) N3 —padre_sugerido→ Sujeto_rol_entidad_comprendida_reginf · {"flag": "padre_sugerido_no_laudado"}

## 2. `ri_ii_31_12_19::1.2` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 4):

```
[encabezado | punto S1]
1. DATOS GENERALES
[texto propio | punto 1.2]
1.2. Número de CUIT de la Entidad.
```

Versión: final (grafo sin cola). Nodos 1, aristas 0.
- **N1** TextoOrdenado `TextoOrdenado_ri_ii_31_12_19_pdf` — Información Institucional de Entidades Financieras y Cambiarias · {"archivo": "ri_ii_31_12_19.pdf", "materia": "RI Cont. Mensual - Información Institucional de Entidades Financieras y Cambiarias - Vigente a partir del 31.12.19", "version": "Comunicación A 8140 (vigencia 03/12/2024)"} · tramo: 

## 3. `ri_laft::S1::chapeau_seccion` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 1):

```
[encabezado | punto S1]
1. Instrucciones generales
[bloque chapeau_seccion | punto S1]
Los sujetos obligados, según corresponda y teniendo en cuenta la periodicidad determinada para
cada uno de ellos, deberán remitir los reportes e informes detallados a continuación.
Para su remisión se tendrán en cuenta las especificaciones establecidas en la Sección 8 del texto
ordenado de Presentación de informaciones al BCRA.
```

Versión: final (grafo sin cola). Nodos 4, aristas 4.
- **N1** Condicion `Condicion_remision_conforme_especificaciones_seccion_8__la_remision_de_los_reportes_e_info_35db76` — Remisión conforme especificaciones Sección 8 · {"descripcion": "La remisión de los reportes e informes debe realizarse conforme a las especificaciones establecidas en la Sección 8 del texto ordenado de Presentación de informaciones al BCRA."} · tramo: Para su remisión se tendrán en cuenta las especificaciones establecidas en la Sección 8 del texto ordenado de Presentación de informaciones al BCRA
- **N2** Obligacion `Obligacion_los_sujetos_obligados_deberan_remitir_los_reportes_e_informes_detallados_segun_c_f98814` — Remisión de reportes e informes · {"descripcion": "Los sujetos obligados deberán remitir los reportes e informes detallados, según corresponda y teniendo en cuenta la periodicidad determinada para cada uno de ellos.", "tipo": "reporte_al_supervisor", "frecuencia": "según la periodicidad determinada para cada uno de ellos"} · tramo: deberán remitir los reportes e informes detallados a continuación
- **N3** Sujeto `Sujeto_rol_alcance_lavdin` — Entidades alcanzadas (Prevención del lavado de activos) · {"nivel": "rol"} · tramo: 
- **N4** TextoOrdenado `TextoOrdenado_ri_laft_pdf` — Régimen Informativo LAFT · {"archivo": "ri_laft.pdf", "materia": "RI - Prevención del Lavado de Activos, del Financiamiento del Terrorismo y Otras Actividades Ilícitas", "version": "Comunicación A 8429 (vigencia 25/04/2026)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **A2** (extraccion) N2 —aplica_a→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}

## 4. `ri_iesinap::S2` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 1):

```
[texto propio | punto S2]
2. Contenido
Los sujetos referidos deberán remitir el citado Informe especial conforme al modelo inserto en el
Anexo, en observancia de las normas dictadas por el BCRA.
El informe deberá ser elaborado por profesionales o asociaciones de profesionales matriculados,
con la pertinente certificación por el Consejo Profesional de Ciencias Económicas en el que se
encuentren matriculados, no siendo requisito que se encuentren inscriptos en el registro de audi-
tores a que se refieren las “Normas mínimas sobre Auditorías Externas para Entidades Financie-
ras”.
```

Versión: final (grafo sin cola). Nodos 4, aristas 3.
- **N1** Excepcion `Excepcion_no_es_requisito_que_los_profesionales_o_asociaciones_de_profesionales_se_encuent_a22200` — No requisito inscripción registro de auditores · {"descripcion": "No es requisito que los profesionales o asociaciones de profesionales se encuentren inscriptos en el registro de auditores a que se refieren las Normas mínimas sobre Auditorías Externas para Entidades Financieras"} · tramo: no siendo requisito que se encuentren inscriptos en el registro de auditores a que se refieren las "Normas mínimas sobre Auditorías Externas para Entidades Financieras"
- **N2** Obligacion `Obligacion_el_informe_debera_ser_elaborado_por_profesionales_o_asociaciones_de_profesionale_2d782e` — Elaboración por profesionales matriculados con certificación · {"descripcion": "El informe deberá ser elaborado por profesionales o asociaciones de profesionales matriculados, con la pertinente certificación por el Consejo Profesional de Ciencias Económicas en el que se encuentren matriculados", "tipo": "otra"} · tramo: El informe deberá ser elaborado por profesionales o asociaciones de profesionales matriculados, con la pertinente certificación por el Consejo Profesional de Ciencias Económicas en el que se encuentren matriculados
- **N3** Obligacion `Obligacion_los_sujetos_referidos_deberan_remitir_el_informe_especial_conforme_al_modelo_ins_b32a58` — Remisión de Informe especial conforme modelo · {"descripcion": "Los sujetos referidos deberán remitir el Informe especial conforme al modelo inserto en el Anexo, en observancia de las normas dictadas por el BCRA", "tipo": "presentacion_informativa"} · tramo: Los sujetos referidos deberán remitir el citado Informe especial conforme al modelo inserto en el Anexo, en observancia de las normas dictadas por el BCRA
- **N4** TextoOrdenado `TextoOrdenado_ri_iesinap_pdf` — Régimen Informativo IESINAP · {"archivo": "ri_iesinap.pdf", "materia": "RI - Informe especial de cumplimiento requerido por el punto 1.5.5.10. de las normas sobre “Sistema Nacional de Pagos Transferencias Normas complementarias”", "version": "Comunicación A 7604 (vigencia 15/09/2022)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **E3** (estructural) N3 —establecida_en→ N4 · {}

## 5. `ri_secoexpo::Sbloque8` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 17):

```
[texto propio | punto Sbloque8]
APARTADO C – BAJA DE REPORTES DE LAS ENTIDADES / EN EL SEGUIMIENTO
Datos solicitados:
1. Código de reporte.
2. N° de destinación de exportación.
3. Nro. de identificación.
4. C.U.I.T. del exportador.
5. Motivo de baja.
En caso de requerirse la baja de los Reportes B.1., B.2. o B.3. en el dato “Nro. de identificación” se
deberá consignar el número de cumplido o incumplido, según corresponda, oportunamente
asignado por la entidad al Reporte que se solicita sea dado de baja. En los casos de los Reportes
B.4. y B.5., este dato no se informará.

En todos los casos, el número de destinación y/o CUIT a consignarse son aquellos que constan en
el Reporte que se solicita sea dado de baja, incluso cuando la baja sea solicitada porque dichos
datos fueron indicados incorrectamente en el registro remitido originalmente.
El dato “motivo de baja” deberá ser completado respetando la siguiente codificación:
1. Anulación de los datos remitidos.
2 Baja para rectificación de los datos incluidos en el reporte.
```

Versión: final (grafo sin cola). Nodos 11, aristas 18.
- **N1** Condicion `Condicion_datos_de_destinacion_y_cuit_los_que_constan_en_el_reporte_original__el_numero_de_5f3f45` — Datos de destinación y CUIT — los que constan en el reporte original · {"descripcion": "El número de destinación y CUIT a consignarse en la solicitud de baja son los que constan en el reporte que se solicita sea dado de baja, incluso si la baja se solicita porque esos datos fueron indicados incorrectamente en el registro remitido originalmente."} · tramo: En todos los casos, el número de destinación y/o CUIT a consignarse son aquellos que constan en el Reporte que se solicita sea dado de baja, incluso cuando la baja sea solicitada porque dichos datos fueron indicados incorrectamente en el registro remitido originalmente.
- **N2** Condicion `Condicion_reportes_b_1_b_2_o_b_3_consignar_numero_cumplido_o_incumplido__cuando_se_solicit_9d198f` — Reportes B.1., B.2. o B.3. — consignar número cumplido o incumplido · {"descripcion": "Cuando se solicita la baja de reportes B.1., B.2. o B.3., en el dato 'Nro. de identificación' se deberá consignar el número de cumplido o incumplido, según corresponda, oportunamente asignado por la entidad al reporte que se solicita sea dado de baja."} · tramo: En caso de requerirse la baja de los Reportes B.1., B.2. o B.3.
- **N3** Definicion `Definicion_codificacion_de_motivo_de_baja__codigo_que_debe_utilizarse_para_indicar_el_motiv_9fc20d` — Codificación de motivo de baja · {"termino": "motivo de baja", "descripcion": "Código que debe utilizarse para indicar el motivo de la solicitud de baja: 1. Anulación de los datos remitidos; 2. Baja para rectificación de los datos incluidos en el reporte."} · tramo: El dato "motivo de baja" deberá ser completado respetando la siguiente codificación: 1. Anulación de los datos remitidos. 2 Baja para rectificación de los datos incluidos en el reporte.
- **N4** Excepcion `Excepcion_para_los_reportes_b_4_y_b_5_el_dato_nro_de_identificacion_no_se_informara_except_f92a4b` — Excepción — reportes B.4. y B.5. no informan número de identificación · {"descripcion": "Para los reportes B.4. y B.5., el dato 'Nro. de identificación' no se informará, exceptuando la obligación general de consignar este dato."} · tramo: En los casos de los Reportes B.4. y B.5., este dato no se informará.
- **N5** Obligacion `Obligacion_dato_que_debe_consignarse_en_la_solicitud_de_baja_de_reportes_codigo_de_reporte__ecf083` — Consignar código de reporte en baja · {"tipo": "presentacion_informativa", "descripcion": "Dato que debe consignarse en la solicitud de baja de reportes: código de reporte."} · tramo: Código de reporte.
- **N6** Obligacion `Obligacion_dato_que_debe_consignarse_en_la_solicitud_de_baja_de_reportes_cuit_del_exportado_c47730` — Consignar CUIT del exportador en baja · {"tipo": "presentacion_informativa", "descripcion": "Dato que debe consignarse en la solicitud de baja de reportes: CUIT del exportador, el que consta en el reporte que se solicita sea dado de baja."} · tramo: C.U.I.T. del exportador.
- **N7** Obligacion `Obligacion_dato_que_debe_consignarse_en_la_solicitud_de_baja_de_reportes_motivo_de_baja_com_859eda` — Consignar motivo de baja · {"tipo": "presentacion_informativa", "descripcion": "Dato que debe consignarse en la solicitud de baja de reportes: motivo de baja, completado respetando la codificación establecida (1. Anulación de los datos remitidos; 2. Baja para rectificación de los datos incluidos en el reporte)."} · tramo: Motivo de baja.
- **N8** Obligacion `Obligacion_dato_que_debe_consignarse_en_la_solicitud_de_baja_de_reportes_numero_de_destinac_0a36d7` — Consignar número de destinación de exportación en baja · {"tipo": "presentacion_informativa", "descripcion": "Dato que debe consignarse en la solicitud de baja de reportes: número de destinación de exportación, el que consta en el reporte que se solicita sea dado de baja."} · tramo: N° de destinación de exportación.
- **N9** Obligacion `Obligacion_dato_que_debe_consignarse_en_la_solicitud_de_baja_de_reportes_numero_de_identifi_69e655` — Consignar número de identificación en baja · {"tipo": "presentacion_informativa", "descripcion": "Dato que debe consignarse en la solicitud de baja de reportes: número de identificación. Para reportes B.1., B.2. o B.3., se deberá consignar el número de cumplido o incumplido según corresponda, oportunamente asignado por la entidad al reporte que se solicita sea dado de baja. Para reportes B.4. y B.5., este dato no se informará."} · tramo: Nro. de identificación.
- **N10** Operacion `Operacion_baja_de_reportes_de_exportacion__ri_secoexpo_sbloque8_cc0baf` — Baja de reportes de exportación · {"tipo": "Baja de reporte", "descripcion": "Solicitud de baja de reportes de exportación (B.1., B.2., B.3., B.4. o B.5.) mediante consignación de datos específicos: código de reporte, número de destinación de exportación, número de identificación, CUIT del exportador y motivo de baja."} · tramo: baja de los Reportes B.1., B.2. o B.3.
- **N11** TextoOrdenado `TextoOrdenado_ri_secoexpo_pdf` — Régimen Informativo Secundario Exportaciones · {"archivo": "ri_secoexpo.pdf", "materia": "RI Cont. Mensual - Seguimiento de las negociaciones de divisas de exportaciones de bienes", "version": "Comunicación A 8158 (vigencia 19/12/2024)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N10 · {}
- **E1** (estructural) N1 —establecida_en→ N11 · {}
- **A2** (extraccion) N2 —condicion_de→ N9 · {}
- **E2** (estructural) N2 —establecida_en→ N11 · {}
- **E3** (estructural) N3 —establecida_en→ N11 · {}
- **E4** (estructural) N4 —establecida_en→ N11 · {}
- **A3** (extraccion) N4 —exceptua_obligacion→ N9 · {}
- **E5** (estructural) N5 —establecida_en→ N11 · {}
- **E6** (estructural) N6 —establecida_en→ N11 · {}
- **E7** (estructural) N7 —establecida_en→ N11 · {}
- **E8** (estructural) N8 —establecida_en→ N11 · {}
- **E9** (estructural) N9 —establecida_en→ N11 · {}
- **E10** (estructural) N10 —establecida_en→ N11 · {}
- **A4** (extraccion) N10 —requiere→ N5 · {}
- **A5** (extraccion) N10 —requiere→ N6 · {}
- **A6** (extraccion) N10 —requiere→ N7 · {}
- **A7** (extraccion) N10 —requiere→ N8 · {}
- **A8** (extraccion) N10 —requiere→ N9 · {}

## 6. `ri_ii_31_12_19::2.1` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 4, 5):

```
[encabezado | punto S2]
2. DIRECTIVOS
[texto propio | punto 2.1]
2.1. Tipo y número de documento de identidad: Se informará el Tipo de documento de iden-
tidad de acuerdo con el detalle de la Tabla Nº 1, teniendo en cuenta las siguientes indi-
caciones:
Las personas de nacionalidad argentina se identificarán con:
Documento Nacional de Identidad
Libreta de Enrolamiento o Libreta Cívica
Las personas extranjeras residentes en el país se identificarán con:
Documento Nacional de Identidad
Pasaporte
Las personas extranjeras residentes en el exterior se identificarán con:
Pasaporte
En caso de no contar con Pasaporte, se consignará “Otros” y se asignará una
numeración correlativa a partir de 1 (uno)
```

Versión: final (grafo sin cola). Nodos 6, aristas 5.
- **N1** Definicion `Definicion_identificacion_personas_extranjeras_residentes_exterior__se_identificaran_con_pa_b3ec04` — Identificación personas extranjeras residentes exterior · {"termino": "personas extranjeras residentes en el exterior", "descripcion": "Se identificarán con Pasaporte"} · tramo: Las personas extranjeras residentes en el exterior se identificarán con: Pasaporte
- **N2** Definicion `Definicion_identificacion_personas_extranjeras_residentes_pais__se_identificaran_con_docume_ea575c` — Identificación personas extranjeras residentes país · {"termino": "personas extranjeras residentes en el país", "descripcion": "Se identificarán con Documento Nacional de Identidad o Pasaporte"} · tramo: Las personas extranjeras residentes en el país se identificarán con: Documento Nacional de Identidad, Pasaporte
- **N3** Definicion `Definicion_identificacion_personas_nacionalidad_argentina__se_identificaran_con_documento_n_4734ac` — Identificación personas nacionalidad argentina · {"termino": "personas de nacionalidad argentina", "descripcion": "Se identificarán con Documento Nacional de Identidad, Libreta de Enrolamiento o Libreta Cívica"} · tramo: Las personas de nacionalidad argentina se identificarán con: Documento Nacional de Identidad, Libreta de Enrolamiento o Libreta Cívica
- **N4** Excepcion `Excepcion_cuando_no_se_cuente_con_pasaporte_se_consignara_otros_y_se_asignara_numeracion_c_eb5485` — Excepción sin Pasaporte — numeración correlativa · {"descripcion": "Cuando no se cuente con Pasaporte, se consignará 'Otros' y se asignará numeración correlativa", "umbrales": [{"tramo": "a partir de 1 (uno)", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]} · tramo: En caso de no contar con Pasaporte, se consignará "Otros" y se asignará una numeración correlativa a partir de 1 (uno)
- **N5** Obligacion `Obligacion_se_informara_el_tipo_de_documento_de_identidad_de_acuerdo_con_el_detalle_de_la_t_a55191` — Informar tipo de documento de identidad · {"descripcion": "Se informará el Tipo de documento de identidad de acuerdo con el detalle de la Tabla Nº 1, teniendo en cuenta las indicaciones sobre nacionalidad y residencia", "tipo": "presentacion_informativa"} · tramo: Se informará el Tipo de documento de identidad de acuerdo con el detalle de la Tabla Nº 1
- **N6** TextoOrdenado `TextoOrdenado_ri_ii_31_12_19_pdf` — Información Institucional de Entidades Financieras y Cambiarias · {"archivo": "ri_ii_31_12_19.pdf", "materia": "RI Cont. Mensual - Información Institucional de Entidades Financieras y Cambiarias - Vigente a partir del 31.12.19", "version": "Comunicación A 8140 (vigencia 03/12/2024)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N6 · {}
- **E2** (estructural) N2 —establecida_en→ N6 · {}
- **E3** (estructural) N3 —establecida_en→ N6 · {}
- **E4** (estructural) N4 —establecida_en→ N6 · {}
- **E5** (estructural) N5 —establecida_en→ N6 · {}

## 7. `ri_tar::2.2` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto S2]
2. CUADRO 1 – CANTIDAD DE TARJETAS EMITIDAS
[texto propio | punto 2.2]
2.2. CUADRO 1 – CANTIDAD DE TARJETAS EMITIDAS - Modelo de información
[TABLA ri_tar::tabla000 | página 3 | e0_tablas | posicional]
Fila 1: col2 = CONCEPTO | col3 = DATO A CONSIGNAR
Fila 2: col1 = RITxxxx11000 | col2 = 1. Cantidad de tarjetas titulares
Fila 3: col1 = RITxxxx12000 | col2 = 2. Cantidad de tarjetas adicionales
[FIN TABLA ri_tar::tabla000]
xxxx = código de marca asignado
```

Versión: final (grafo sin cola). Nodos 5, aristas 7.
- **N1** Obligacion `Obligacion_las_entidades_deben_consignar_en_el_modelo_de_informacion_la_cantidad_de_tarjeta_d7480a` — Informar cantidad de tarjetas emitidas · {"tipo": "presentacion_informativa", "descripcion": "Las entidades deben consignar en el modelo de información la cantidad de tarjetas titulares y adicionales emitidas, según los conceptos especificados en el cuadro"} · tramo: CUADRO 1 – CANTIDAD DE TARJETAS EMITIDAS - Modelo de información
- **N2** Operacion `Operacion_cantidad_de_tarjetas_adicionales_emitidas__ri_tar_2_2_e14d6b` — Cantidad de tarjetas adicionales emitidas · {"tipo": "presentación informativa", "descripcion": "Reporte de la cantidad de tarjetas adicionales emitidas, identificado con código RITxxxx12000 donde xxxx es el código de marca asignado"} · tramo: Cantidad de tarjetas adicionales
- **N3** Operacion `Operacion_cantidad_de_tarjetas_titulares_emitidas__ri_tar_2_2_448056` — Cantidad de tarjetas titulares emitidas · {"tipo": "presentación informativa", "descripcion": "Reporte de la cantidad de tarjetas titulares emitidas, identificado con código RITxxxx11000 donde xxxx es el código de marca asignado"} · tramo: Cantidad de tarjetas titulares
- **N4** Sujeto `Sujeto_propuesto_las_entidades__ri_tar` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_rol_entidad_comprendida_reginf", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N5** TextoOrdenado `TextoOrdenado_ri_tar_pdf` — Régimen Informativo Contable Mensual · {"archivo": "ri_tar.pdf", "materia": "RI Cont. Mensual - Financiamiento con tarjetas de crédito", "version": "Comunicación A 7855 (vigencia 02/01/2024)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N4 · {}
- **E1** (estructural) N1 —establecida_en→ N5 · {}
- **A2** (extraccion) N1 —regula→ N2 · {}
- **A3** (extraccion) N1 —regula→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N5 · {}
- **E3** (estructural) N3 —establecida_en→ N5 · {}
- **C1** (catalogo_sujetos) N4 —padre_sugerido→ Sujeto_rol_entidad_comprendida_reginf · {"flag": "padre_sugerido_no_laudado"}

## 8. `ri_secoexpo::S10` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto Sbloque1]
APARTADO A – DATOS A DISPOSICIÓN DE LAS ENTIDADES
[encabezado | punto SA]
APARTADO A: Información de las destinaciones de exportación de bienes a disposición de
las entidades (SECOEXPO).
[texto propio | punto S10]
10. Código de divisa del valor FOB: de acuerdo con codificación SWIFT.
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Definicion `Definicion_codigo_de_divisa_del_valor_fob__codigo_que_identifica_la_divisa_del_valor_fob_de_146e8b` — Código de divisa del valor FOB · {"termino": "Código de divisa del valor FOB", "descripcion": "Código que identifica la divisa del valor FOB de acuerdo con la codificación SWIFT"} · tramo: Código de divisa del valor FOB: de acuerdo con codificación SWIFT
- **N2** TextoOrdenado `TextoOrdenado_ri_secoexpo_pdf` — Régimen Informativo Secundario Exportaciones · {"archivo": "ri_secoexpo.pdf", "materia": "RI Cont. Mensual - Seguimiento de las negociaciones de divisas de exportaciones de bienes", "version": "Comunicación A 8158 (vigencia 19/12/2024)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 9. `ri_ii_31_12_19::3.6` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 8):

```
[encabezado | punto S3]
3. GERENTES
[texto propio | punto 3.6]
3.6. Descripción: Se informará el nombre del cargo funcional asignado en la estructura orga-
nizativa de la entidad (p.ej.: Gerente de Comercio Exterior, Subgerente de Contaduría
General, etc.); no corresponderá consignar descripciones relativas al nivel jerárquico o
escalafonario (p. ej.: Gerente; Subgerente Departamental de 1ra., etc.). Asimismo, en
aquellos cargos relacionados con el concepto “Responsable de otras gerencias” se de-
berá indicar a qué gerencia o área corresponde.
```

Versión: final (grafo sin cola). Nodos 4, aristas 3.
- **N1** Obligacion `Obligacion_en_aquellos_cargos_relacionados_con_el_concepto_responsable_de_otras_gerencias_s_7dce4d` — Indicar gerencia o área para cargos de responsable de otras gerencias · {"descripcion": "En aquellos cargos relacionados con el concepto 'Responsable de otras gerencias' se deberá indicar a qué gerencia o área corresponde.", "tipo": "presentacion_informativa"} · tramo: en aquellos cargos relacionados con el concepto "Responsable de otras gerencias" se deberá indicar a qué gerencia o área corresponde
- **N2** Obligacion `Obligacion_se_informara_el_nombre_del_cargo_funcional_asignado_en_la_estructura_organizativ_221a61` — Informar nombre del cargo funcional · {"descripcion": "Se informará el nombre del cargo funcional asignado en la estructura organizativa de la entidad (p.ej.: Gerente de Comercio Exterior, Subgerente de Contaduría General, etc.); no corresponderá consignar descripciones relativas al nivel jerárquico o escalafonario (p. ej.: Gerente; Subgerente Departamental de 1ra., etc.).", "tipo": "presentacion_informativa"} · tramo: Se informará el nombre del cargo funcional asignado en la estructura organizativa de la entidad
- **N3** Restriccion `Restriccion_no_correspondera_consignar_descripciones_relativas_al_nivel_jerarquico_o_escalaf_ba6043` — Prohibición de descripciones jerárquicas o escalafonarias · {"descripcion": "No corresponderá consignar descripciones relativas al nivel jerárquico o escalafonario (p. ej.: Gerente; Subgerente Departamental de 1ra., etc.).", "tipo": "prohibicion"} · tramo: no corresponderá consignar descripciones relativas al nivel jerárquico o escalafonario
- **N4** TextoOrdenado `TextoOrdenado_ri_ii_31_12_19_pdf` — Información Institucional de Entidades Financieras y Cambiarias · {"archivo": "ri_ii_31_12_19.pdf", "materia": "RI Cont. Mensual - Información Institucional de Entidades Financieras y Cambiarias - Vigente a partir del 31.12.19", "version": "Comunicación A 8140 (vigencia 03/12/2024)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **E3** (estructural) N3 —establecida_en→ N4 · {}

## 10. `ri_iesinap::A::S3` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 2):

```
[encabezado | punto A]
-ANEXO-
[encabezado | punto A::Sbloque1]
CUIT N° [completar]
[texto propio | punto A::S3]
3. Responsabilidad del Profesional
Nuestra responsabilidad consiste en la emisión del presente informe especial, basado en nuestra
tarea profesional, que se detalla en el capítulo siguiente, para cumplir con los requerimientos del
BCRA mencionados en el capítulo 1.
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Obligacion `Obligacion_emitir_el_presente_informe_especial_basado_en_la_tarea_profesional_detallada_en__d5c517` — Emisión de informe especial · {"descripcion": "Emitir el presente informe especial basado en la tarea profesional detallada en el capítulo siguiente, para cumplir con los requerimientos del BCRA mencionados en el capítulo 1.", "tipo": "otra"} · tramo: Nuestra responsabilidad consiste en la emisión del presente informe especial
- **N2** TextoOrdenado `TextoOrdenado_ri_iesinap_pdf` — Régimen Informativo IESINAP · {"archivo": "ri_iesinap.pdf", "materia": "RI - Informe especial de cumplimiento requerido por el punto 1.5.5.10. de las normas sobre “Sistema Nacional de Pagos Transferencias Normas complementarias”", "version": "Comunicación A 7604 (vigencia 15/09/2022)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 11. `ri_ai::2.2` — RI:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto S2]
Sección 2. Instrucciones generales
[texto propio | punto 2.2]
2.2. Los importes se registrarán en miles de pesos, sin decimales.
A los fines del redondeo de las magnitudes se incrementarán los valores en una
unidad cuando el primer dígito de las fracciones sea igual o mayor que 5, desechando
estas últimas si resultan inferiores.
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Obligacion `Obligacion_a_los_fines_del_redondeo_de_las_magnitudes_se_incrementaran_los_valores_en_una_u_c9ecd7` — Redondeo de magnitudes por dígito de fracción · {"tipo": "calculo", "descripcion": "A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad cuando el primer dígito de las fracciones sea igual o mayor que 5, desechando estas últimas si resultan inferiores.", "umbrales": [{"tramo": "cuando el primer dígito de las fracciones sea igual o mayor que 5", "comparacion": "minimo_inclusivo", "regla_comparacion": "limite_rela · tramo: A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad cuando el primer dígito de las fracciones sea igual o mayor que 5, desechando estas últimas si resultan inferiores.
- **N2** Obligacion `Obligacion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales__ri_ai_2_2_0beb2c` — Registro de importes en miles de pesos · {"tipo": "presentacion_informativa", "descripcion": "Los importes se registrarán en miles de pesos, sin decimales."} · tramo: Los importes se registrarán en miles de pesos, sin decimales.
- **N3** TextoOrdenado `TextoOrdenado_ri_ai_pdf` — Régimen Informativo sobre Bases Consolidadas · {"archivo": "ri_ai.pdf", "materia": "RI Cont. Mensual - Relación para los activos inmovilizados y otros conceptos", "version": "Comunicación A 8009 (vigencia 01/04/2024)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N3 · {}

## 12. `ri_tsa::2.3` — RI:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 78):

```
[encabezado | punto S2]
Sección 2. Ratio
[texto propio | punto 2.3]
2.3. Modelo de información
[TABLA ri_tsa::tabla025 | página 78 | e0_tablas | columnas]
Columnas: Código | Concepto
Fila 1: Código = 100 | Concepto = Ratio del último día de cada mes (NSFRn)
Fila 2: Código = 110 | Concepto = Valor mínimo (NSFRn min) de cada mes
Fila 3: Código = 120 | Concepto = Valor máximo (NSFRn máx) de cada mes
[FIN TABLA ri_tsa::tabla025]
```

Versión: final (grafo sin cola). Nodos 4, aristas 3.
- **N1** Definicion `Definicion_codigo_100_ratio_del_ultimo_dia_de_cada_mes__ratio_del_ultimo_dia_de_cada_mes_ns_1636d3` — Código 100 — Ratio del último día de cada mes · {"termino": "Código 100", "descripcion": "Ratio del último día de cada mes (NSFRn)"} · tramo: Código = 100 | Concepto = Ratio del último día de cada mes (NSFRn)
- **N2** Definicion `Definicion_codigo_110_valor_minimo_de_cada_mes__valor_minimo_nsfrn_min_de_cada_mes__ri_tsa__8fb5f1` — Código 110 — Valor mínimo de cada mes · {"termino": "Código 110", "descripcion": "Valor mínimo (NSFRn min) de cada mes"} · tramo: Código = 110 | Concepto = Valor mínimo (NSFRn min) de cada mes
- **N3** Definicion `Definicion_codigo_120_valor_maximo_de_cada_mes__valor_maximo_nsfrn_max_de_cada_mes__ri_tsa__f43a1e` — Código 120 — Valor máximo de cada mes · {"termino": "Código 120", "descripcion": "Valor máximo (NSFRn máx) de cada mes"} · tramo: Código = 120 | Concepto = Valor máximo (NSFRn máx) de cada mes
- **N4** TextoOrdenado `TextoOrdenado_ri_tsa_pdf` — Ratio de Cobertura de Liquidez · {"archivo": "ri_tsa.pdf", "materia": "RI para supervisión", "version": "Comunicación A 8465 (vigencia 31/07/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **E3** (estructural) N3 —establecida_en→ N4 · {}

## 13. `ri_tsa::3.1` — RI:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 79):

```
[encabezado | punto S3]
Sección 3. Medición del Ratio
[texto propio | punto 3.1]
3.1. Instrucciones particulares
Los importes se registrarán en miles de pesos, sin decimales.
A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad
cuando el primer dígito de las fracciones sea igual o mayor que 5, desechando estas úl-
timas si resultan inferiores.
Los importes en moneda extranjera se convertirán a pesos utilizando el tipo de cambio
de referencia publicado por el B.C.R.A. para el dólar estadounidense, previa aplicación
del tipo de pase correspondiente para las otras monedas comunicado por la Mesa de
Operaciones.
```

Versión: final (grafo sin cola). Nodos 5, aristas 7.
- **N1** Obligacion `Obligacion_a_los_fines_del_redondeo_de_las_magnitudes_se_incrementaran_los_valores_en_una_u_aa4a0f` — Redondeo de magnitudes según dígito de fracción · {"tipo": "calculo", "descripcion": "A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad cuando el primer dígito de las fracciones sea igual o mayor que 5, desechando estas últimas si resultan inferiores.", "umbrales": [{"tramo": "cuando el primer dígito de las fracciones sea igual o mayor que 5", "comparacion": "minimo_inclusivo", "regla_comparacion": "limite_rela · tramo: A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad cuando el primer dígito de las fracciones sea igual o mayor que 5, desechando estas últimas si resultan inferiores.
- **N2** Obligacion `Obligacion_los_importes_en_moneda_extranjera_se_convertiran_a_pesos_utilizando_el_tipo_de_c_ffc19e` — Conversión de moneda extranjera a pesos · {"tipo": "calculo", "descripcion": "Los importes en moneda extranjera se convertirán a pesos utilizando el tipo de cambio de referencia publicado por el B.C.R.A. para el dólar estadounidense, previa aplicación del tipo de pase correspondiente para las otras monedas comunicado por la Mesa de Operaciones."} · tramo: Los importes en moneda extranjera se convertirán a pesos utilizando el tipo de cambio de referencia publicado por el B.C.R.A. para el dólar estadounidense, previa aplicación del tipo de pase correspondiente para las otras monedas comunicado por la Mesa de Operaciones.
- **N3** Obligacion `Obligacion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales__ri_tsa_3_1_9fe2c6` — Registro de importes en miles de pesos · {"tipo": "otra", "descripcion": "Los importes se registrarán en miles de pesos, sin decimales."} · tramo: Los importes se registrarán en miles de pesos, sin decimales.
- **N4** Sujeto `Sujeto_propuesto_las_entidades__ri_tsa` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_entidad_financiera", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N5** TextoOrdenado `TextoOrdenado_ri_tsa_pdf` — Ratio de Cobertura de Liquidez · {"archivo": "ri_tsa.pdf", "materia": "RI para supervisión", "version": "Comunicación A 8465 (vigencia 31/07/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N4 · {}
- **E1** (estructural) N1 —establecida_en→ N5 · {}
- **A2** (extraccion) N2 —aplica_a→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N5 · {}
- **A3** (extraccion) N3 —aplica_a→ N4 · {}
- **E3** (estructural) N3 —establecida_en→ N5 · {}
- **C1** (catalogo_sujetos) N4 —padre_sugerido→ Sujeto_entidad_financiera · {"flag": "padre_sugerido_no_laudado"}

## 14. `ri_tsa::3.3.2` — RI:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 90):

```
[encabezado | punto S3]
Sección 3. Medición del Ratio
[encabezado | punto 3.3]
3.3. Modelo de información.
[texto propio | punto 3.3.2]
3.3.2. Totales de control.
[TABLA ri_tsa::tabla029 | página 90 | e0_tablas | columnas]
Columnas: Código | Componentes de la categoría FED | Importe
Fila 1: Código = 10000 | Componentes de la categoría FED = Fondeo Estable Disponible - FED | Importe = Monto Total ponderado
Fila 2: Código = 20000 | Componentes de la categoría FED = Fondeo Estable Requerido - FER | Importe = Monto Total ponderado ⟨combinada con fila 1⟩
[FIN TABLA ri_tsa::tabla029]
```

Versión: final (grafo sin cola). Nodos 5, aristas 4.
- **N1** Definicion `Definicion_fed_fondeo_estable_disponible__componente_de_la_categoria_fed_con_codigo_10000_c_ef0a34` — FED — Fondeo Estable Disponible · {"termino": "Fondeo Estable Disponible - FED", "descripcion": "Componente de la categoría FED con código 10000, cuyo importe se expresa como Monto Total ponderado"} · tramo: Fondeo Estable Disponible - FED
- **N2** Definicion `Definicion_fer_fondeo_estable_requerido__componente_de_la_categoria_fed_con_codigo_20000_cu_c52a87` — FER — Fondeo Estable Requerido · {"termino": "Fondeo Estable Requerido - FER", "descripcion": "Componente de la categoría FED con código 20000, cuyo importe se expresa como Monto Total ponderado"} · tramo: Fondeo Estable Requerido - FER
- **N3** Operacion `Operacion_calculo_de_monto_total_ponderado_fed__ri_tsa_3_3_2_ca0da6` — Cálculo de Monto Total ponderado FED · {"tipo": "cálculo", "descripcion": "Cálculo del Monto Total ponderado para el Fondeo Estable Disponible (FED), código 10000"} · tramo: Monto Total ponderado
- **N4** Operacion `Operacion_calculo_de_monto_total_ponderado_fer__ri_tsa_3_3_2_0d4065` — Cálculo de Monto Total ponderado FER · {"tipo": "cálculo", "descripcion": "Cálculo del Monto Total ponderado para el Fondeo Estable Requerido (FER), código 20000, con el mismo importe que el FED"} · tramo: Monto Total ponderado ⟨combinada con fila 1⟩
- **N5** TextoOrdenado `TextoOrdenado_ri_tsa_pdf` — Ratio de Cobertura de Liquidez · {"archivo": "ri_tsa.pdf", "materia": "RI para supervisión", "version": "Comunicación A 8465 (vigencia 31/07/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N5 · {}
- **E2** (estructural) N2 —establecida_en→ N5 · {}
- **E3** (estructural) N3 —establecida_en→ N5 · {}
- **E4** (estructural) N4 —establecida_en→ N5 · {}

## 15. `ri_ai::6.1` — RI:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 9):

```
[encabezado | punto S6]
Sección 6. Disposiciones transitorias
[texto propio | punto 6.1]
6.1. Tratamiento de los excesos originados en el cómputo del 50 % -en lugar del 100 %- de los re-
sultados provenientes de los ajustes NIIF por primera vez dentro de la RPC (Período enero –
marzo 2018).
Estos excesos se consideran admitidos (es decir que no constituirán incumplimientos) de veri-
ficarse las siguientes condiciones:
c) surjan de la última conciliación de los estados contables trimestrales en el marco de la
convergencia a NIIF que cuente con informe de auditor externo;
d) dicha conciliación evidencie que de haberse considerado los resultados positivos al
100 % -en lugar de al 50 %- no se hubiera registrado tal exceso.
De reunir los requisitos citados, se consignará en la partida 401 la porción pertinente para la
neutralización del exceso generado.
A tal fin, se consignará como “número” y “fecha de Resolución” la de la presente comunica-
ción.
También se agregará una descripción detallada del cálculo del importe para el período in-
formado.
```

Versión: final (grafo sin cola). Nodos 6, aristas 7.
- **N1** Condicion `Condicion_excesos_admitidos_si_conciliacion_evidencia_no_exceso_al_100__los_excesos_se_con_6a5884` — Excesos admitidos si conciliación evidencia no exceso al 100% · {"descripcion": "Los excesos se consideran admitidos si la conciliación evidencia que de haberse considerado los resultados positivos al 100% en lugar del 50% no se hubiera registrado tal exceso", "umbrales": [{"tramo": "al 100 % -en lugar de al 50 %-", "valor": "100", "unidad": "porcentaje", "comparacion": "no_determinada", "regla_comparacion": "sin_marcador", "origen": "e1", "tramo_verificado":  · tramo: dicha conciliación evidencie que de haberse considerado los resultados positivos al 100 % -en lugar de al 50 %- no se hubiera registrado tal exceso
- **N2** Condicion `Condicion_excesos_admitidos_si_surgen_de_ultima_conciliacion_niif__los_excesos_se_consider_258f8e` — Excesos admitidos si surgen de última conciliación NIIF · {"descripcion": "Los excesos se consideran admitidos si surgen de la última conciliación de los estados contables trimestrales en el marco de la convergencia a NIIF que cuente con informe de auditor externo"} · tramo: surjan de la última conciliación de los estados contables trimestrales en el marco de la convergencia a NIIF que cuente con informe de auditor externo
- **N3** Obligacion `Obligacion_de_reunir_los_requisitos_citados_se_consignara_en_la_partida_401_la_porcion_pert_149af4` — Consignar en partida 401 porción para neutralización · {"tipo": "asignacion", "descripcion": "De reunir los requisitos citados, se consignará en la partida 401 la porción pertinente para la neutralización del exceso generado"} · tramo: se consignará en la partida 401 la porción pertinente para la neutralización del exceso generado
- **N4** Obligacion `Obligacion_se_agregara_una_descripcion_detallada_del_calculo_del_importe_para_el_periodo_in_a96cd7` — Agregar descripción detallada del cálculo · {"tipo": "presentacion_informativa", "descripcion": "Se agregará una descripción detallada del cálculo del importe para el período informado"} · tramo: se agregará una descripción detallada del cálculo del importe para el período informado
- **N5** Obligacion `Obligacion_se_consignara_como_numero_y_fecha_de_resolucion_la_de_la_presente_comunicacion___794f2b` — Consignar número y fecha de Resolución · {"tipo": "asignacion", "descripcion": "Se consignará como número y fecha de Resolución la de la presente comunicación"} · tramo: se consignará como "número" y "fecha de Resolución" la de la presente comunicación
- **N6** TextoOrdenado `TextoOrdenado_ri_ai_pdf` — Régimen Informativo sobre Bases Consolidadas · {"archivo": "ri_ai.pdf", "materia": "RI Cont. Mensual - Relación para los activos inmovilizados y otros conceptos", "version": "Comunicación A 8009 (vigencia 01/04/2024)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N6 · {}
- **A2** (extraccion) N2 —condicion_de→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N6 · {}
- **E3** (estructural) N3 —establecida_en→ N6 · {}
- **E4** (estructural) N4 —establecida_en→ N6 · {}
- **E5** (estructural) N5 —establecida_en→ N6 · {}

## 16. `seggar::S8::cierre` — NG:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 16):

```
[encabezado | punto S8]
8. Legislación aplicable.
[bloque cierre | punto S8]
Artículo 25: De forma.
(*) Aplicable a los Decretos 540/95, 1292/96 y 1127/98, en sus respectivas fechas
```

Versión: final (grafo sin cola). Nodos 4, aristas 3.
- **N1** Comunicacion `Comunicacion_decreto_1127_98` — Decreto 1127/98 · {"codigo": "Decreto 1127/98", "tipo": "externa"} · tramo: Decretos 540/95, 1292/96 y 1127/98
- **N2** Comunicacion `Comunicacion_decreto_1292_96` — Decreto 1292/96 · {"codigo": "Decreto 1292/96", "tipo": "externa"} · tramo: Decretos 540/95, 1292/96
- **N3** Comunicacion `Comunicacion_decreto_540_95` — Decreto 540/95 · {"codigo": "Decreto 540/95", "tipo": "externa"} · tramo: Decretos 540/95
- **N4** TextoOrdenado `TextoOrdenado_seggar_pdf` — Seguro de Depósitos · {"archivo": "seggar.pdf", "materia": "Aplicación del sistema de seguro de garantía de depósitos", "version": "Comunicación A 8407 (vigencia 01/04/2026)"} · tramo: 
- **E1** (estructural) N4 —referencia→ N1 · {}
- **E2** (estructural) N4 —referencia→ N2 · {}
- **E3** (estructural) N4 —referencia→ N3 · {}

## 17. `consyr::1.4.2::intro` — NG:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto S1]
1. Instrumentación de documentos.
[encabezado | punto 1.4]
1.4. Requisitos de seguridad de la información.
[bloque intro | punto 1.4.2]
1.4.2. Se deberán satisfacer los siguientes requisitos generales para la protección de los
DFE en cada etapa de su ciclo de vida:
```

Versión: final (grafo sin cola). Nodos 3, aristas 3.
- **N1** Obligacion `Obligacion_las_entidades_financieras_deberan_satisfacer_los_requisitos_generales_para_la_pr_8d0937` — Satisfacer requisitos generales protección DFE · {"descripcion": "Las entidades financieras deberán satisfacer los requisitos generales para la protección de los documentos financieros electrónicos (DFE) en cada etapa de su ciclo de vida.", "tipo": "otra"} · tramo: Se deberán satisfacer los siguientes requisitos generales para la protección de los DFE en cada etapa de su ciclo de vida
- **N2** Sujeto `Sujeto_propuesto_las_entidades__consyr` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_entidad_financiera", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_consyr_pdf` — Instrumentación de documentos · {"archivo": "consyr.pdf", "materia": "Instrumentación, conservación y reproducción de documentos", "version": "Comunicación A 6112 (vigencia 01/11/2016)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}
- **C1** (catalogo_sujetos) N2 —padre_sugerido→ Sujeto_entidad_financiera · {"flag": "padre_sugerido_no_laudado"}

## 18. `cedin::2.1.2` — NG:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 4):

```
[encabezado | punto S2]
2. Características del CEDIN.
[encabezado | punto 2.1]
2.1. Formales.
[texto propio | punto 2.1.2]
2.1.2. Serie y numeración.
Constarán en el cuerpo del certificado y en el talón en forma digital.
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Obligacion `Obligacion_la_serie_y_numeracion_del_cedin_deberan_constar_en_el_cuerpo_del_certificado_y_e_b26853` — Serie y numeración en cuerpo y talón · {"descripcion": "La serie y numeración del CEDIN deberán constar en el cuerpo del certificado y en el talón en forma digital.", "tipo": "otra"} · tramo: Constarán en el cuerpo del certificado y en el talón en forma digital.
- **N2** TextoOrdenado `TextoOrdenado_cedin_pdf` — Texto Ordenado CEDIN · {"archivo": "cedin.pdf", "materia": "Certificados de depósitos para la inversión", "version": "Comunicación A 8131 (vigencia 13/11/2024)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 19. `asomut::S2::chapeau_seccion` — NG:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto S2]
2. Excepciones.
[bloque chapeau_seccion | punto S2]
La prestación del servicio de ayuda económica queda excluida de ese encuadramiento cuando
se verifiquen la totalidad de las siguientes características:
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Excepcion `Excepcion_la_prestacion_del_servicio_de_ayuda_economica_queda_excluida_del_encuadramiento__ff9f06` — Exclusión servicio ayuda económica · {"descripcion": "La prestación del servicio de ayuda económica queda excluida del encuadramiento normativo cuando se verifiquen la totalidad de las características que siguen."} · tramo: La prestación del servicio de ayuda económica queda excluida de ese encuadramiento cuando se verifiquen la totalidad de las siguientes características:
- **N2** TextoOrdenado `TextoOrdenado_asomut_pdf` — Texto Ordenado ASOMUT · {"archivo": "asomut.pdf", "materia": "Asociaciones mutuales. Reglamentación de su actividad financiera (Decreto 1367/93)", "version": "Comunicación A 6428 (vigencia 01/01/2018)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 20. `seggar::5.2.7` — NG:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 5):

```
[encabezado | punto S5]
5.Alcances de la garantía.
[encabezado | punto 5.2]
5.2. Exclusiones.
[texto propio | punto 5.2.7]
5.2.7. Los depósitos e inversiones a plazo instrumentados a través de certificados electróni-
cos para depósitos e inversiones a plazo (CEDIP) que sean transmitidos a partir de la
fecha en que la entidad financiera emisora quede comprendida en alguno de los su-
puestos previstos en los artículos 49 de la Carta Orgánica del BCRA o 35 bis de la Ley
de Entidades Financieras.
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Excepcion `Excepcion_quedan_excluidos_de_la_cobertura_del_seguro_de_garantia_los_cedip_transmitidos_a_537f53` — Exclusión CEDIP transmitidos post-compresión regulatoria · {"descripcion": "Quedan excluidos de la cobertura del seguro de garantía los CEDIP transmitidos a partir de que la entidad financiera emisora se encuentre comprendida en los supuestos de los artículos 49 de la Carta Orgánica del BCRA o 35 bis de la Ley de Entidades Financieras."} · tramo: Los depósitos e inversiones a plazo instrumentados a través de certificados electrónicos para depósitos e inversiones a plazo (CEDIP) que sean transmitidos a partir de la fecha en que la entidad financiera emisora quede comprendida en alguno de los supuestos previstos en los artículos 49 de la Carta
- **N2** TextoOrdenado `TextoOrdenado_seggar_pdf` — Seguro de Depósitos · {"archivo": "seggar.pdf", "materia": "Aplicación del sistema de seguro de garantía de depósitos", "version": "Comunicación A 8407 (vigencia 01/04/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 21. `traval::1.2.2` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 4):

```
[encabezado | punto S1]
Sección 1. Disposiciones generales.
[encabezado | punto 1.2]
1.2. Criterios de observancia.
[texto propio | punto 1.2.2]
1.2.2. La inclusión en la nómina de TV inscriptas en el citado registro y el cumplimiento de estas
disposiciones no obstan a que las TV deban también cumplir con las normas y los demás
recaudos exigidos por otras autoridades competentes en la materia.
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Excepcion `Excepcion_la_inclusion_en_la_nomina_de_tv_inscriptas_y_el_cumplimiento_de_las_disposicione_391d4a` — Excepción — cumplimiento de otras normas · {"descripcion": "La inclusión en la nómina de TV inscriptas y el cumplimiento de las disposiciones del presente Texto Ordenado no eximen a las TV de cumplir con normas y recaudos exigidos por otras autoridades competentes"} · tramo: La inclusión en la nómina de TV inscriptas en el citado registro y el cumplimiento de estas disposiciones no obstan a que las TV deban también cumplir con las normas y los demás recaudos exigidos por otras autoridades competentes en la materia
- **N2** Sujeto `Sujeto_rol_alcance_traval` — Sujetos comprendidos (Transportadoras de valores) · {"nivel": "rol"} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_traval_pdf` — Texto Ordenado Transportadoras de Valores · {"archivo": "traval.pdf", "materia": "Transportadoras de valores", "version": "Comunicación A 7447 (vigencia 27/01/2022)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}

## 22. `ratio::6.2.5.2` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 37):

```
[encabezado | punto S6]
Sección 6. Factores.
[encabezado | punto 6.2]
6.2. Entradas de efectivo.
[encabezado | punto 6.2.5]
6.2.5. Otras entradas en función de la contraparte (punto 5.2.3.).
[texto propio | punto 6.2.5.2]
6.2.5.2. Entradas a recibir de contrapartes mayoristas no financieras
–incluye sector privado no financiero (excepto que se trate de
Mipyme previstas en el punto 5.2.3.1. y de entidades cambia-
rias, aseguradoras y agentes regulados por la CNV, fiduciarios
de fideicomisos no financieros) y otros estados soberanos, y
de bancos multilaterales de desarrollo y del Gobierno Nacio-
nal– (acápite i) del punto 5.2.3.2.). 50%
```

Versión: final (grafo sin cola). Nodos 8, aristas 104.
- **N1** Excepcion `Excepcion_quedan_excluidas_del_regimen_de_entradas_de_contrapartes_mayoristas_no_financier_2a17f1` — Exclusión entidades cambiarias — entradas de contrapartes mayoristas · {"descripcion": "Quedan excluidas del régimen de entradas de contrapartes mayoristas no financieras las entidades cambiarias"} · tramo: excepto que se trate de [...] entidades cambiarias
- **N2** Excepcion `Excepcion_quedan_excluidas_del_regimen_de_entradas_de_contrapartes_mayoristas_no_financier_4461c9` — Exclusión agentes CNV — entradas de contrapartes mayoristas · {"descripcion": "Quedan excluidas del régimen de entradas de contrapartes mayoristas no financieras los agentes regulados por la CNV"} · tramo: excepto que se trate de [...] agentes regulados por la CNV
- **N3** Excepcion `Excepcion_quedan_excluidas_del_regimen_de_entradas_de_contrapartes_mayoristas_no_financier_7e4717` — Exclusión fiduciarios de fideicomisos no financieros — entradas de contrapartes mayoristas · {"descripcion": "Quedan excluidas del régimen de entradas de contrapartes mayoristas no financieras los fiduciarios de fideicomisos no financieros"} · tramo: excepto que se trate de [...] fiduciarios de fideicomisos no financieros
- **N4** Excepcion `Excepcion_quedan_excluidas_del_regimen_de_entradas_de_contrapartes_mayoristas_no_financier_9fc711` — Exclusión MiPyMEs — entradas de contrapartes mayoristas · {"descripcion": "Quedan excluidas del régimen de entradas de contrapartes mayoristas no financieras las MiPyMEs previstas en el punto 5.2.3.1."} · tramo: excepto que se trate de Mipyme previstas en el punto 5.2.3.1.
- **N5** Excepcion `Excepcion_quedan_excluidas_del_regimen_de_entradas_de_contrapartes_mayoristas_no_financier_fb5913` — Exclusión aseguradoras — entradas de contrapartes mayoristas · {"descripcion": "Quedan excluidas del régimen de entradas de contrapartes mayoristas no financieras las aseguradoras"} · tramo: excepto que se trate de [...] aseguradoras
- **N6** Operacion `Operacion_entradas_de_efectivo_de_contrapartes_mayoristas_no_financieras__ratio_6_2_5_2_c19ed6` — Entradas de efectivo de contrapartes mayoristas no financieras · {"tipo": "Recepción de efectivo", "descripcion": "Entradas de efectivo a recibir de contrapartes mayoristas no financieras, que incluye sector privado no financiero (excepto MiPyMEs previstas en punto 5.2.3.1., entidades cambiarias, aseguradoras, agentes regulados por la CNV, fiduciarios de fideicomisos no financieros), otros estados soberanos, bancos multilaterales de desarrollo y Gobierno Nacion · tramo: Entradas a recibir de contrapartes mayoristas no financieras
- **N7** Restriccion `Restriccion_el_factor_de_entrada_para_efectivo_a_recibir_de_contrapartes_mayoristas_no_finan_abf8a9` — Factor de entrada 50% — contrapartes mayoristas no financieras · {"tipo": "limite_cuantitativo", "descripcion": "El factor de entrada para efectivo a recibir de contrapartes mayoristas no financieras es del 50%", "umbrales": [{"tramo": "50%", "valor": "50", "unidad": "porcentaje", "comparacion": "no_determinada", "regla_comparacion": "sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]} · tramo: 50%
- **N8** TextoOrdenado `TextoOrdenado_ratio_pdf` — Ratio de fondeo neto estable · {"archivo": "ratio.pdf", "materia": "Ratio de cobertura de liquidez", "version": "Comunicación A 8445 (vigencia 05/06/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N8 · {}
- **R1** (remision_derivada) N1 —remite_a→ Condicion_creditos_sin_atraso_a_clientes_mayoristas__los_creditos_no_presentan_atraso_algu_528c72 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R2** (remision_derivada) N1 —remite_a→ Condicion_vencimiento_dentro_de_30_dias__los_pagos_tienen_vencimiento_contractual_dentro_d_e9556e · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R3** (remision_derivada) N1 —remite_a→ Definicion_contrapartes_mayoristas_no_financieras__incluye_sector_privado_no_financiero_sal_40778c · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R4** (remision_derivada) N1 —remite_a→ Definicion_entidades_financieras_cambiarias_aseguradoras_factor_aplicable__categoria_de_con_78f32d · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R5** (remision_derivada) N1 —remite_a→ Definicion_entradas_titulos_valores_30_dias_no_falac__incluye_titulos_valores_con_vencimien_f378a9 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R6** (remision_derivada) N1 —remite_a→ Excepcion_no_aplica_el_supuesto_del_50_de_continuacion_de_financiaciones_a_entidades_cambi_d1996d · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R7** (remision_derivada) N1 —remite_a→ Excepcion_se_excluyen_las_entradas_procedentes_de_titulos_valores_computables_en_el_falac__aff940 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R8** (remision_derivada) N1 —remite_a→ Obligacion_suponer_que_las_entradas_de_fondos_provenientes_de_entidades_financieras_cambiar_018748 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R9** (remision_derivada) N1 —remite_a→ Obligacion_suponer_que_se_continuaran_extendiendo_financiaciones_por_un_importe_equivalente_20b4ae · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R10** (remision_derivada) N1 —remite_a→ Obligacion_suponer_que_se_recibiran_todos_los_pagos_interes_y_capital_con_vencimiento_contr_4d22f3 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R11** (remision_derivada) N1 —remite_a→ Operacion_depositos_operativos_en_entidades_financieras__ratio_5_2_3_2_da890a · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R12** (remision_derivada) N1 —remite_a→ Restriccion_no_podran_computarse_entradas_procedentes_de_depositos_mantenidos_en_otras_entid_be9471 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **E2** (estructural) N2 —establecida_en→ N8 · {}
- **R13** (remision_derivada) N2 —remite_a→ Condicion_creditos_sin_atraso_a_clientes_mayoristas__los_creditos_no_presentan_atraso_algu_528c72 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R14** (remision_derivada) N2 —remite_a→ Condicion_vencimiento_dentro_de_30_dias__los_pagos_tienen_vencimiento_contractual_dentro_d_e9556e · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R15** (remision_derivada) N2 —remite_a→ Definicion_contrapartes_mayoristas_no_financieras__incluye_sector_privado_no_financiero_sal_40778c · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R16** (remision_derivada) N2 —remite_a→ Definicion_entidades_financieras_cambiarias_aseguradoras_factor_aplicable__categoria_de_con_78f32d · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R17** (remision_derivada) N2 —remite_a→ Definicion_entradas_titulos_valores_30_dias_no_falac__incluye_titulos_valores_con_vencimien_f378a9 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R18** (remision_derivada) N2 —remite_a→ Excepcion_no_aplica_el_supuesto_del_50_de_continuacion_de_financiaciones_a_entidades_cambi_d1996d · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R19** (remision_derivada) N2 —remite_a→ Excepcion_se_excluyen_las_entradas_procedentes_de_titulos_valores_computables_en_el_falac__aff940 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R20** (remision_derivada) N2 —remite_a→ Obligacion_suponer_que_las_entradas_de_fondos_provenientes_de_entidades_financieras_cambiar_018748 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R21** (remision_derivada) N2 —remite_a→ Obligacion_suponer_que_se_continuaran_extendiendo_financiaciones_por_un_importe_equivalente_20b4ae · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R22** (remision_derivada) N2 —remite_a→ Obligacion_suponer_que_se_recibiran_todos_los_pagos_interes_y_capital_con_vencimiento_contr_4d22f3 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R23** (remision_derivada) N2 —remite_a→ Operacion_depositos_operativos_en_entidades_financieras__ratio_5_2_3_2_da890a · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R24** (remision_derivada) N2 —remite_a→ Restriccion_no_podran_computarse_entradas_procedentes_de_depositos_mantenidos_en_otras_entid_be9471 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **E3** (estructural) N3 —establecida_en→ N8 · {}
- **R25** (remision_derivada) N3 —remite_a→ Condicion_creditos_sin_atraso_a_clientes_mayoristas__los_creditos_no_presentan_atraso_algu_528c72 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R26** (remision_derivada) N3 —remite_a→ Condicion_vencimiento_dentro_de_30_dias__los_pagos_tienen_vencimiento_contractual_dentro_d_e9556e · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R27** (remision_derivada) N3 —remite_a→ Definicion_contrapartes_mayoristas_no_financieras__incluye_sector_privado_no_financiero_sal_40778c · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R28** (remision_derivada) N3 —remite_a→ Definicion_entidades_financieras_cambiarias_aseguradoras_factor_aplicable__categoria_de_con_78f32d · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R29** (remision_derivada) N3 —remite_a→ Definicion_entradas_titulos_valores_30_dias_no_falac__incluye_titulos_valores_con_vencimien_f378a9 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R30** (remision_derivada) N3 —remite_a→ Excepcion_no_aplica_el_supuesto_del_50_de_continuacion_de_financiaciones_a_entidades_cambi_d1996d · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R31** (remision_derivada) N3 —remite_a→ Excepcion_se_excluyen_las_entradas_procedentes_de_titulos_valores_computables_en_el_falac__aff940 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R32** (remision_derivada) N3 —remite_a→ Obligacion_suponer_que_las_entradas_de_fondos_provenientes_de_entidades_financieras_cambiar_018748 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R33** (remision_derivada) N3 —remite_a→ Obligacion_suponer_que_se_continuaran_extendiendo_financiaciones_por_un_importe_equivalente_20b4ae · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R34** (remision_derivada) N3 —remite_a→ Obligacion_suponer_que_se_recibiran_todos_los_pagos_interes_y_capital_con_vencimiento_contr_4d22f3 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R35** (remision_derivada) N3 —remite_a→ Operacion_depositos_operativos_en_entidades_financieras__ratio_5_2_3_2_da890a · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R36** (remision_derivada) N3 —remite_a→ Restriccion_no_podran_computarse_entradas_procedentes_de_depositos_mantenidos_en_otras_entid_be9471 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **E4** (estructural) N4 —establecida_en→ N8 · {}
- **R37** (remision_derivada) N4 —remite_a→ Condicion_creditos_sin_atraso_a_clientes_mayoristas__los_creditos_no_presentan_atraso_algu_528c72 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R38** (remision_derivada) N4 —remite_a→ Condicion_creditos_sin_atraso_en_pagos__los_creditos_concedidos_a_clientes_minoristas_y_mi_c647c9 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "financiero (excepto que se trate de\nMipyme previstas en el punto 5.2.3.1. y de entidades cambia-\nrias"}
- **R39** (remision_derivada) N4 —remite_a→ Condicion_vencimiento_dentro_de_30_dias__los_pagos_tienen_vencimiento_contractual_dentro_d_e9556e · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R40** (remision_derivada) N4 —remite_a→ Definicion_contrapartes_mayoristas_no_financieras__incluye_sector_privado_no_financiero_sal_40778c · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R41** (remision_derivada) N4 —remite_a→ Definicion_entidades_financieras_cambiarias_aseguradoras_factor_aplicable__categoria_de_con_78f32d · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R42** (remision_derivada) N4 —remite_a→ Definicion_entradas_titulos_valores_30_dias_no_falac__incluye_titulos_valores_con_vencimien_f378a9 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R43** (remision_derivada) N4 —remite_a→ Excepcion_no_aplica_el_supuesto_del_50_de_continuacion_de_financiaciones_a_entidades_cambi_d1996d · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R44** (remision_derivada) N4 —remite_a→ Excepcion_se_excluyen_las_entradas_procedentes_de_titulos_valores_computables_en_el_falac__aff940 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R45** (remision_derivada) N4 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuan_otorgando_creditos_a_un_cb3a53 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "financiero (excepto que se trate de\nMipyme previstas en el punto 5.2.3.1. y de entidades cambia-\nrias"}
- **R46** (remision_derivada) N4 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuaran_otorgando_creditos_a__f53e8f · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "financiero (excepto que se trate de\nMipyme previstas en el punto 5.2.3.1. y de entidades cambia-\nrias"}
- **R47** (remision_derivada) N4 —remite_a→ Obligacion_las_entidades_financieras_deben_suponer_que_recibiran_todos_los_pagos_interes_y__26b8e7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "financiero (excepto que se trate de\nMipyme previstas en el punto 5.2.3.1. y de entidades cambia-\nrias"}
- **R48** (remision_derivada) N4 —remite_a→ Obligacion_para_el_saldo_excedente_al_pago_minimo_de_financiaciones_mediante_tarjetas_de_cr_6b37b7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "financiero (excepto que se trate de\nMipyme previstas en el punto 5.2.3.1. y de entidades cambia-\nrias"}
- **R49** (remision_derivada) N4 —remite_a→ Obligacion_suponer_que_las_entradas_de_fondos_provenientes_de_entidades_financieras_cambiar_018748 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R50** (remision_derivada) N4 —remite_a→ Obligacion_suponer_que_se_continuaran_extendiendo_financiaciones_por_un_importe_equivalente_20b4ae · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R51** (remision_derivada) N4 —remite_a→ Obligacion_suponer_que_se_recibiran_todos_los_pagos_interes_y_capital_con_vencimiento_contr_4d22f3 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R52** (remision_derivada) N4 —remite_a→ Operacion_depositos_operativos_en_entidades_financieras__ratio_5_2_3_2_da890a · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R53** (remision_derivada) N4 —remite_a→ Potestad_aplicacion_factores_punto_6_2_5_1__se_aplicaran_los_factores_previstos_en_el_pun_d01efe · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "financiero (excepto que se trate de\nMipyme previstas en el punto 5.2.3.1. y de entidades cambia-\nrias"}
- **R54** (remision_derivada) N4 —remite_a→ Restriccion_no_podran_computarse_entradas_procedentes_de_depositos_mantenidos_en_otras_entid_be9471 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **E5** (estructural) N5 —establecida_en→ N8 · {}
- **R55** (remision_derivada) N5 —remite_a→ Condicion_creditos_sin_atraso_a_clientes_mayoristas__los_creditos_no_presentan_atraso_algu_528c72 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R56** (remision_derivada) N5 —remite_a→ Condicion_vencimiento_dentro_de_30_dias__los_pagos_tienen_vencimiento_contractual_dentro_d_e9556e · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R57** (remision_derivada) N5 —remite_a→ Definicion_contrapartes_mayoristas_no_financieras__incluye_sector_privado_no_financiero_sal_40778c · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R58** (remision_derivada) N5 —remite_a→ Definicion_entidades_financieras_cambiarias_aseguradoras_factor_aplicable__categoria_de_con_78f32d · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R59** (remision_derivada) N5 —remite_a→ Definicion_entradas_titulos_valores_30_dias_no_falac__incluye_titulos_valores_con_vencimien_f378a9 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R60** (remision_derivada) N5 —remite_a→ Excepcion_no_aplica_el_supuesto_del_50_de_continuacion_de_financiaciones_a_entidades_cambi_d1996d · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R61** (remision_derivada) N5 —remite_a→ Excepcion_se_excluyen_las_entradas_procedentes_de_titulos_valores_computables_en_el_falac__aff940 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R62** (remision_derivada) N5 —remite_a→ Obligacion_suponer_que_las_entradas_de_fondos_provenientes_de_entidades_financieras_cambiar_018748 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R63** (remision_derivada) N5 —remite_a→ Obligacion_suponer_que_se_continuaran_extendiendo_financiaciones_por_un_importe_equivalente_20b4ae · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R64** (remision_derivada) N5 —remite_a→ Obligacion_suponer_que_se_recibiran_todos_los_pagos_interes_y_capital_con_vencimiento_contr_4d22f3 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R65** (remision_derivada) N5 —remite_a→ Operacion_depositos_operativos_en_entidades_financieras__ratio_5_2_3_2_da890a · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R66** (remision_derivada) N5 —remite_a→ Restriccion_no_podran_computarse_entradas_procedentes_de_depositos_mantenidos_en_otras_entid_be9471 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **E6** (estructural) N6 —establecida_en→ N8 · {}
- **R67** (remision_derivada) N6 —remite_a→ Condicion_creditos_sin_atraso_a_clientes_mayoristas__los_creditos_no_presentan_atraso_algu_528c72 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R68** (remision_derivada) N6 —remite_a→ Condicion_creditos_sin_atraso_en_pagos__los_creditos_concedidos_a_clientes_minoristas_y_mi_c647c9 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "financiero (excepto que se trate de\nMipyme previstas en el punto 5.2.3.1. y de entidades cambia-\nrias"}
- **R69** (remision_derivada) N6 —remite_a→ Condicion_vencimiento_dentro_de_30_dias__los_pagos_tienen_vencimiento_contractual_dentro_d_e9556e · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R70** (remision_derivada) N6 —remite_a→ Definicion_contrapartes_mayoristas_no_financieras__incluye_sector_privado_no_financiero_sal_40778c · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R71** (remision_derivada) N6 —remite_a→ Definicion_entidades_financieras_cambiarias_aseguradoras_factor_aplicable__categoria_de_con_78f32d · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R72** (remision_derivada) N6 —remite_a→ Definicion_entradas_titulos_valores_30_dias_no_falac__incluye_titulos_valores_con_vencimien_f378a9 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R73** (remision_derivada) N6 —remite_a→ Excepcion_no_aplica_el_supuesto_del_50_de_continuacion_de_financiaciones_a_entidades_cambi_d1996d · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R74** (remision_derivada) N6 —remite_a→ Excepcion_se_excluyen_las_entradas_procedentes_de_titulos_valores_computables_en_el_falac__aff940 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R75** (remision_derivada) N6 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuan_otorgando_creditos_a_un_cb3a53 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "financiero (excepto que se trate de\nMipyme previstas en el punto 5.2.3.1. y de entidades cambia-\nrias"}
- **R76** (remision_derivada) N6 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuaran_otorgando_creditos_a__f53e8f · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "financiero (excepto que se trate de\nMipyme previstas en el punto 5.2.3.1. y de entidades cambia-\nrias"}
- **R77** (remision_derivada) N6 —remite_a→ Obligacion_las_entidades_financieras_deben_suponer_que_recibiran_todos_los_pagos_interes_y__26b8e7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "financiero (excepto que se trate de\nMipyme previstas en el punto 5.2.3.1. y de entidades cambia-\nrias"}
- **R78** (remision_derivada) N6 —remite_a→ Obligacion_para_el_saldo_excedente_al_pago_minimo_de_financiaciones_mediante_tarjetas_de_cr_6b37b7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "financiero (excepto que se trate de\nMipyme previstas en el punto 5.2.3.1. y de entidades cambia-\nrias"}
- **R79** (remision_derivada) N6 —remite_a→ Obligacion_suponer_que_las_entradas_de_fondos_provenientes_de_entidades_financieras_cambiar_018748 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R80** (remision_derivada) N6 —remite_a→ Obligacion_suponer_que_se_continuaran_extendiendo_financiaciones_por_un_importe_equivalente_20b4ae · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R81** (remision_derivada) N6 —remite_a→ Obligacion_suponer_que_se_recibiran_todos_los_pagos_interes_y_capital_con_vencimiento_contr_4d22f3 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R82** (remision_derivada) N6 —remite_a→ Operacion_depositos_operativos_en_entidades_financieras__ratio_5_2_3_2_da890a · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R83** (remision_derivada) N6 —remite_a→ Potestad_aplicacion_factores_punto_6_2_5_1__se_aplicaran_los_factores_previstos_en_el_pun_d01efe · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "financiero (excepto que se trate de\nMipyme previstas en el punto 5.2.3.1. y de entidades cambia-\nrias"}
- **R84** (remision_derivada) N6 —remite_a→ Restriccion_no_podran_computarse_entradas_procedentes_de_depositos_mantenidos_en_otras_entid_be9471 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **E7** (estructural) N7 —establecida_en→ N8 · {}
- **A1** (extraccion) N7 —limita→ N6 · {}
- **R85** (remision_derivada) N7 —remite_a→ Condicion_creditos_sin_atraso_a_clientes_mayoristas__los_creditos_no_presentan_atraso_algu_528c72 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R86** (remision_derivada) N7 —remite_a→ Condicion_vencimiento_dentro_de_30_dias__los_pagos_tienen_vencimiento_contractual_dentro_d_e9556e · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R87** (remision_derivada) N7 —remite_a→ Definicion_contrapartes_mayoristas_no_financieras__incluye_sector_privado_no_financiero_sal_40778c · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R88** (remision_derivada) N7 —remite_a→ Definicion_entidades_financieras_cambiarias_aseguradoras_factor_aplicable__categoria_de_con_78f32d · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R89** (remision_derivada) N7 —remite_a→ Definicion_entradas_titulos_valores_30_dias_no_falac__incluye_titulos_valores_con_vencimien_f378a9 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R90** (remision_derivada) N7 —remite_a→ Excepcion_no_aplica_el_supuesto_del_50_de_continuacion_de_financiaciones_a_entidades_cambi_d1996d · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R91** (remision_derivada) N7 —remite_a→ Excepcion_se_excluyen_las_entradas_procedentes_de_titulos_valores_computables_en_el_falac__aff940 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R92** (remision_derivada) N7 —remite_a→ Obligacion_suponer_que_las_entradas_de_fondos_provenientes_de_entidades_financieras_cambiar_018748 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R93** (remision_derivada) N7 —remite_a→ Obligacion_suponer_que_se_continuaran_extendiendo_financiaciones_por_un_importe_equivalente_20b4ae · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R94** (remision_derivada) N7 —remite_a→ Obligacion_suponer_que_se_recibiran_todos_los_pagos_interes_y_capital_con_vencimiento_contr_4d22f3 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R95** (remision_derivada) N7 —remite_a→ Operacion_depositos_operativos_en_entidades_financieras__ratio_5_2_3_2_da890a · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}
- **R96** (remision_derivada) N7 —remite_a→ Restriccion_no_podran_computarse_entradas_procedentes_de_depositos_mantenidos_en_otras_entid_be9471 · {"alcance": "interna", "destino": "ratio::5.2.3.2", "evidencia": "multilaterales de desarrollo y del Gobierno Nacio-\nnal– (acápite i) del punto 5.2.3.2.). 50%"}

## 23. `snp_spd::8.1.1::intro` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 23):

```
[encabezado | punto S8]
Sección 8. Viaje con QR
[encabezado | punto 8.1]
8.1. Requisitos
[bloque intro | punto 8.1.1]
8.1.1. Las entidades financieras, PSPCP y PSI, que deseen ofrecer a sus clientes la posibili-
dad de pagar el transporte público mediante pagos iniciados con códigos QR (“viaje con
QR”, VQR) deberán:
```

Versión: final (grafo sin cola). Nodos 5, aristas 4.
- **N1** Obligacion `Obligacion_las_entidades_financieras_pspcp_y_psi_que_deseen_ofrecer_a_sus_clientes_la_posib_00b1a0` — Oferta de viaje con QR — requisitos · {"tipo": "otra", "descripcion": "Las entidades financieras, PSPCP y PSI que deseen ofrecer a sus clientes la posibilidad de pagar el transporte público mediante pagos iniciados con códigos QR (viaje con QR, VQR) deben cumplir con requisitos específicos que se enumeran a continuación."} · tramo: Las entidades financieras, PSPCP y PSI, que deseen ofrecer a sus clientes la posibilidad de pagar el transporte público mediante pagos iniciados con códigos QR ("viaje con QR", VQR) deberán:
- **N2** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N3** Sujeto `Sujeto_psi_billetera_digital` — Proveedores de servicios de pago iniciadores que prestan el servicio de billetera digital (PSI) · {"nivel": "clase", "alias": ["PSI"]} · tramo: 
- **N4** Sujeto `Sujeto_pspcp` — Proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP) · {"nivel": "clase", "alias": ["PSPCP"]} · tramo: 
- **N5** TextoOrdenado `TextoOrdenado_snp_spd_pdf` — Servicios de Pago — Clave Bancaria Uniforme · {"archivo": "snp_spd.pdf", "materia": "Sistema Nacional de Pagos - Servicios de pago", "version": "Comunicación A 8303 (vigencia 03/10/2025)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **A2** (extraccion) N1 —aplica_a→ N3 · {}
- **A3** (extraccion) N1 —aplica_a→ N4 · {}
- **E1** (estructural) N1 —establecida_en→ N5 · {}

## 24. `jafip::5.6.2` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 15):

```
[encabezado | punto S5]
Sección 5. Gestión de Oficios por COELSA.
[encabezado | punto 5.6]
5.6. Procesamiento del saldo pendiente a embargar.
[texto propio | punto 5.6.2]
5.6.2. En los casos de los incisos a) y b) del punto precedente la retención deberá ser in-
formada el mismo día. En el restante supuesto dentro de las 48 horas de efectua-
da.
```

Versión: final (grafo sin cola). Nodos 5, aristas 6.
- **N1** Condicion `Condicion_supuesto_incisos_a_y_b_punto_precedente__cuando_se_verifiquen_los_supuestos_de_l_476b10` — Supuesto incisos a) y b) punto precedente · {"descripcion": "Cuando se verifiquen los supuestos de los incisos a) y b) del punto precedente"} · tramo: En los casos de los incisos a) y b) del punto precedente
- **N2** Condicion `Condicion_supuesto_restante_distinto_de_incisos_a_y_b__cuando_no_se_verifiquen_los_supuest_4405da` — Supuesto restante distinto de incisos a) y b) · {"descripcion": "Cuando no se verifiquen los supuestos de los incisos a) y b) del punto precedente"} · tramo: En el restante supuesto
- **N3** Obligacion `Obligacion_en_el_restante_supuesto_la_retencion_debera_ser_informada_dentro_de_las_48_horas_f08bea` — Informe de retención dentro de 48 horas · {"descripcion": "En el restante supuesto, la retención deberá ser informada dentro de las 48 horas de efectuada.", "tipo": "comunicacion_a_cliente", "umbrales": [{"tramo": "dentro de las 48 horas de efectuada", "valor": "48", "unidad": "horas", "comparacion": "maximo_inclusivo", "regla_comparacion": "compuesta:dentro_de", "origen": "e1", "tramo_verificado": "exacta", "fuera_de_lista": ["unidad"]}] · tramo: la retención deberá ser informada [...] dentro de las 48 horas de efectuada
- **N4** Obligacion `Obligacion_en_los_casos_de_los_incisos_a_y_b_del_punto_precedente_la_retencion_debera_ser_i_2b33f5` — Informe de retención mismo día · {"descripcion": "En los casos de los incisos a) y b) del punto precedente, la retención deberá ser informada el mismo día.", "tipo": "comunicacion_a_cliente", "frecuencia": "el mismo día"} · tramo: la retención deberá ser informada el mismo día
- **N5** TextoOrdenado `TextoOrdenado_jafip_pdf` — Sistema de Oficios Judiciales · {"archivo": "jafip.pdf", "materia": "Disposiciones judiciales originadas en juicios entablados por ARCA", "version": "Comunicación A 8177 (vigencia 15/01/2025)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N4 · {}
- **E1** (estructural) N1 —establecida_en→ N5 · {}
- **A2** (extraccion) N2 —condicion_de→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N5 · {}
- **E3** (estructural) N3 —establecida_en→ N5 · {}
- **E4** (estructural) N4 —establecida_en→ N5 · {}

## 25. `rmrtsd::3.4.4.2` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 12):

```
[encabezado | punto S3]
Sección 3. Protección de los servicios financieros provistos por medios digitales.
[encabezado | punto 3.4]
3.4. Control de accesos. Requisitos para los factores de autenticación.
[encabezado | punto 3.4.4]
3.4.4. Tarjetas de pago (débito, crédito o prepago) y elementos físicos de autenticación.
[texto propio | punto 3.4.4.2]
3.4.4.2. Factores de autenticación retenidos o no entregados al cliente.
Estos factores deberán ser destruidos o desvinculados del cliente y sus cuentas
en un período no mayor a 30 días hábiles.
```

Versión: final (grafo sin cola). Nodos 4, aristas 5.
- **N1** Condicion `Condicion_factores_de_autenticacion_retenidos_o_no_entregados__cuando_los_factores_de_aute_63296b` — Factores de autenticación retenidos o no entregados · {"descripcion": "Cuando los factores de autenticación hayan sido retenidos o no entregados al cliente"} · tramo: Estos factores deberán ser destruidos o desvinculados del cliente y sus cuentas en un período no mayor a 30 días hábiles
- **N2** Obligacion `Obligacion_los_factores_de_autenticacion_retenidos_o_no_entregados_al_cliente_deberan_ser_d_edba21` — Plazo máximo 30 días hábiles — destrucción o desvinculación de factores · {"tipo": "otra", "descripcion": "Los factores de autenticación retenidos o no entregados al cliente deberán ser destruidos o desvinculados del cliente y sus cuentas dentro del plazo máximo establecido", "umbrales": [{"tramo": "no mayor a 30 días hábiles", "valor": "30", "unidad": "dias", "dias_tipo": "habiles", "comparacion": "maximo_inclusivo", "regla_comparacion": "negacion:mayor", "origen": "e1 · tramo: Estos factores deberán ser destruidos o desvinculados del cliente y sus cuentas en un período no mayor a 30 días hábiles
- **N3** Operacion `Operacion_destruccion_o_desvinculacion_de_factores_de_autenticacion__rmrtsd_3_4_4_2_19fab1` — Destrucción o desvinculación de factores de autenticación · {"tipo": "Destrucción o desvinculación de factores de autenticación", "descripcion": "Destrucción o desvinculación del cliente y sus cuentas de los factores de autenticación retenidos o no entregados al cliente"} · tramo: Estos factores deberán ser destruidos o desvinculados del cliente y sus cuentas
- **N4** TextoOrdenado `TextoOrdenado_rmrtsd_pdf` — Servicios financieros digitales · {"archivo": "rmrtsd.pdf", "materia": "Requisitos mínimos ges. y ctrol. tec. y seg. de la inf. asociados a los servicios financieros digitales", "version": "Comunicación A 7783 (vigencia 29/11/2023)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **E3** (estructural) N3 —establecida_en→ N4 · {}
- **A2** (extraccion) N3 —requiere→ N2 · {}

## 26. `retype::2.1.2` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 5):

```
[encabezado | punto S2]
Sección 2. Distribución de beneficios.
[encabezado | punto 2.1]
2.1. Designación de casas pagadoras.
[texto propio | punto 2.1.2]
2.1.2. Los beneficiarios serán informados de las casas bancarias a las que,
conforme a la distribución de pagos que se efectúe, deben concurrir para
hacer efectivo los haberes.
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Obligacion `Obligacion_los_beneficiarios_seran_informados_de_las_casas_bancarias_a_las_que_conforme_a_l_c015ed` — Informar beneficiarios de casas pagadoras · {"tipo": "comunicacion_a_cliente", "descripcion": "Los beneficiarios serán informados de las casas bancarias a las que, conforme a la distribución de pagos que se efectúe, deben concurrir para hacer efectivo los haberes."} · tramo: Los beneficiarios serán informados de las casas bancarias a las que, conforme a la distribución de pagos que se efectúe, deben concurrir para hacer efectivo los haberes
- **N2** Sujeto `Sujeto_usuario_de_servicios_financieros` — Usuarios de servicios financieros · {"nivel": "clase"} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_retype_pdf` — Pago de retiros y pensiones militares · {"archivo": "retype.pdf", "materia": "Pago de retiros y pensiones militares", "version": "Comunicación A 2949 (vigencia 16/07/2099)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}

## 27. `adfsp::4.2.4` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 21):

```
[encabezado | punto S4]
Sección 4. Obligaciones de las entidades financieras.
[encabezado | punto 4.2]
4.2. Cronogramas globales de amortización (capitales).
[texto propio | punto 4.2.4]
4.2.4. En el caso de préstamos con desembolsos sucesivos solicitados en el plazo de 180
días corridos contados desde el día hábil siguiente al de notificación del resultado de
cada subasta y/o en el plazo adicional de 360 días corridos, los distintos cronogramas
de pago de cada etapa deberán mantener las fechas de vencimiento informadas -en la
parte respectiva- en el primer cronograma global presentado respecto de la primera
acreditación de fondos efectuada por el Banco Central.
En los proyectos que se implementen en forma escalonada, el plazo máximo que co-
rresponda comenzará a partir de la fecha de la primera acreditación de fondos por el
Banco Central para ese proyecto.
Para los proyectos con desembolsos escalonados en los cuales la incidencia de dis-
tintos factores inherentes al grado de avance del respectivo proyecto amerite adecua-
ciones a los cronogramas de pago ya presentados al Banco Central, se admitirá -con
carácter de excepción y dejando constancia de ello en el legajo específico de crédito
del prestatario- la pertinente modificación de los vencimientos de dichos cronogramas
de pago, debiendo mantener inalterable el vencimiento final originalmente informado.
Los nuevos cronogramas de pago deberán ser presentados al Banco Central con el tí-
tulo de “Rectificativo” y acompañados en cada caso de una nota explicativa al efecto.
En los proyectos para financiar capital de trabajo a un plazo máximo de dos años (in-
cluyendo el período de gracia, de existir), las entidades deberán verificar que las con-
diciones de pago que los prestatarios acuerden con los compradores de los bienes de
capital a producir sean coincidentes con los vencimientos a informar en los respecti-
vos cronogramas de pago a presentar al Banco Central.
```

Versión: final (grafo sin cola). Nodos 9, aristas 12.
- **N1** Condicion `Condicion_proyectos_con_desembolsos_escalonados_y_factores_de_avance__cuando_en_proyectos__4e3b4f` — Proyectos con desembolsos escalonados y factores de avance · {"descripcion": "Cuando en proyectos con desembolsos escalonados la incidencia de distintos factores inherentes al grado de avance del proyecto amerite adecuaciones a los cronogramas de pago ya presentados"} · tramo: Para los proyectos con desembolsos escalonados en los cuales la incidencia de distintos factores inherentes al grado de avance del respectivo proyecto amerite adecuaciones a los cronogramas de pago ya presentados al Banco Central
- **N2** Condicion `Condicion_proyectos_implementados_en_forma_escalonada__cuando_los_proyectos_se_implementen_df0d9e` — Proyectos implementados en forma escalonada · {"descripcion": "Cuando los proyectos se implementen en forma escalonada, el plazo máximo comienza a partir de la fecha de la primera acreditación de fondos por el Banco Central para ese proyecto"} · tramo: En los proyectos que se implementen en forma escalonada
- **N3** Excepcion `Excepcion_se_admite_con_caracter_de_excepcion_la_modificacion_de_los_vencimientos_de_crono_68dea7` — Excepción modificación cronogramas por factores de avance · {"descripcion": "Se admite con carácter de excepción la modificación de los vencimientos de cronogramas de pago cuando la incidencia de distintos factores inherentes al grado de avance del proyecto lo amerite, siempre que se mantenga inalterable el vencimiento final originalmente informado"} · tramo: se admitirá -con carácter de excepción y dejando constancia de ello en el legajo específico de crédito del prestatario- la pertinente modificación de los vencimientos de dichos cronogramas de pago, debiendo mantener inalterable el vencimiento final originalmente informado
- **N4** Obligacion `Obligacion_las_entidades_deben_verificar_que_las_condiciones_de_pago_acordadas_entre_presta_57fbc9` — Verificar coincidencia condiciones de pago capital de trabajo · {"tipo": "otra", "descripcion": "Las entidades deben verificar que las condiciones de pago acordadas entre prestatarios y compradores de bienes de capital sean coincidentes con los vencimientos a informar en los cronogramas de pago presentados al Banco Central, en proyectos de financiamiento de capital de trabajo con plazo máximo de dos años incluyendo período de gracia", "umbrales": [{"tramo": "a · tramo: En los proyectos para financiar capital de trabajo a un plazo máximo de dos años (incluyendo el período de gracia, de existir), las entidades deberán verificar que las condiciones de pago que los prestatarios acuerden con los compradores de los bienes de capital a producir sean coincidentes con los 
- **N5** Obligacion `Obligacion_los_distintos_cronogramas_de_pago_de_cada_etapa_deben_mantener_las_fechas_de_ven_76b328` — Mantener fechas de vencimiento en cronogramas · {"tipo": "otra", "descripcion": "Los distintos cronogramas de pago de cada etapa deben mantener las fechas de vencimiento informadas en el primer cronograma global presentado respecto de la primera acreditación de fondos"} · tramo: los distintos cronogramas de pago de cada etapa deberán mantener las fechas de vencimiento informadas -en la parte respectiva- en el primer cronograma global presentado respecto de la primera acreditación de fondos efectuada por el Banco Central
- **N6** Obligacion `Obligacion_los_nuevos_cronogramas_de_pago_deben_ser_presentados_al_banco_central_con_el_tit_9e36dc` — Presentar cronogramas rectificativos con nota explicativa · {"tipo": "presentacion_informativa", "descripcion": "Los nuevos cronogramas de pago deben ser presentados al Banco Central con el título de 'Rectificativo' y acompañados de una nota explicativa"} · tramo: Los nuevos cronogramas de pago deberán ser presentados al Banco Central con el título de "Rectificativo" y acompañados en cada caso de una nota explicativa al efecto
- **N7** Operacion `Operacion_prestamos_con_desembolsos_sucesivos__adfsp_4_2_4_68a5e6` — Préstamos con desembolsos sucesivos · {"tipo": "Desembolso de préstamo", "descripcion": "Préstamos con desembolsos sucesivos solicitados dentro de 180 días corridos desde el día hábil siguiente a la notificación del resultado de cada subasta y/o en plazo adicional de 360 días corridos"} · tramo: préstamos con desembolsos sucesivos solicitados en el plazo de 180 días corridos contados desde el día hábil siguiente al de notificación del resultado de cada subasta y/o en el plazo adicional de 360 días corridos
- **N8** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N9** TextoOrdenado `TextoOrdenado_adfsp_pdf` — Adelantos a Entidades Financieras · {"archivo": "adfsp.pdf", "materia": "Adelantos del Banco Central a las entidades financieras con destino a financiaciones al sector productivo", "version": "Comunicación A 6428 (vigencia 01/01/2018)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N9 · {}
- **E2** (estructural) N2 —establecida_en→ N9 · {}
- **E3** (estructural) N3 —establecida_en→ N9 · {}
- **A2** (extraccion) N4 —aplica_a→ N8 · {}
- **E4** (estructural) N4 —establecida_en→ N9 · {}
- **A3** (extraccion) N5 —aplica_a→ N8 · {}
- **E5** (estructural) N5 —establecida_en→ N9 · {}
- **A4** (extraccion) N5 —regula→ N7 · {}
- **A5** (extraccion) N6 —aplica_a→ N8 · {}
- **E6** (estructural) N6 —establecida_en→ N9 · {}
- **E7** (estructural) N7 —establecida_en→ N9 · {}

## 28. `retype::1.6` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 4):

```
[encabezado | punto S1]
Sección 1. Disposiciones generales.
[texto propio | punto 1.6]
1.6. Compensación por el servicio.
Los bancos deducirán la comisión que corresponda del monto a pagar al
beneficiario, según lo establecido en la Sección 3.
```

Versión: final (grafo sin cola). Nodos 4, aristas 3.
- **N1** Obligacion `Obligacion_los_bancos_deduciran_la_comision_que_corresponda_del_monto_a_pagar_al_beneficiar_0de849` — Deducir comisión del monto a pagar · {"tipo": "otra", "descripcion": "Los bancos deducirán la comisión que corresponda del monto a pagar al beneficiario, según lo establecido en la Sección 3."} · tramo: Los bancos deducirán la comisión que corresponda del monto a pagar al beneficiario
- **N2** Operacion `Operacion_deduccion_de_comision_del_monto_a_pagar__retype_1_6_ad4af2` — Deducción de comisión del monto a pagar · {"tipo": "Deducción de comisión", "descripcion": "Los bancos deducirán la comisión que corresponda del monto a pagar al beneficiario, según lo establecido en la Sección 3."} · tramo: Los bancos deducirán la comisión que corresponda del monto a pagar al beneficiario
- **N3** Sujeto `Sujeto_banco` — Bancos · {"nivel": "clase"} · tramo: 
- **N4** TextoOrdenado `TextoOrdenado_retype_pdf` — Pago de retiros y pensiones militares · {"archivo": "retype.pdf", "materia": "Pago de retiros y pensiones militares", "version": "Comunicación A 2949 (vigencia 16/07/2099)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}

## 29. `ratio::6.2.5.1` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 37):

```
[encabezado | punto S6]
Sección 6. Factores.
[encabezado | punto 6.2]
6.2. Entradas de efectivo.
[encabezado | punto 6.2.5]
6.2.5. Otras entradas en función de la contraparte (punto 5.2.3.).
[texto propio | punto 6.2.5.1]
6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto
5.2.3.1.).
i) Financiaciones mediante tarjetas de crédito.
a) Pago mínimo de amortización de capital, comisiones o in-
tereses asociados a préstamos con vencimiento indefini-
do.
50%
b) Saldo excedente al pago mínimo a que se refiere el inciso
a).
20%
ii) Demás. 50%
```

Versión: final (grafo sin cola). Nodos 7, aristas 45.
- **N1** Operacion `Operacion_demas_entradas_clientes_minoristas_y_mipyme__ratio_6_2_5_1_247b33` — Demás entradas clientes minoristas y Mipyme · {"tipo": "Otras entradas de efectivo", "descripcion": "Demás entradas de efectivo procedentes de clientes minoristas y Mipyme, distintas de las financiaciones mediante tarjetas de crédito"} · tramo: Demás
- **N2** Operacion `Operacion_pago_minimo_amortizacion_tarjeta_credito__ratio_6_2_5_1_eae564` — Pago mínimo amortización tarjeta crédito · {"tipo": "Pago de obligaciones de crédito", "descripcion": "Pago mínimo de amortización de capital, comisiones o intereses asociados a préstamos con vencimiento indefinido, en el contexto de financiaciones mediante tarjetas de crédito de clientes minoristas y Mipyme"} · tramo: Pago mínimo de amortización de capital, comisiones o intereses asociados a préstamos con vencimiento indefinido
- **N3** Operacion `Operacion_saldo_excedente_pago_minimo_tarjeta_credito__ratio_6_2_5_1_d3d8e2` — Saldo excedente pago mínimo tarjeta crédito · {"tipo": "Saldo de crédito", "descripcion": "Saldo excedente al pago mínimo de amortización de capital, comisiones o intereses en financiaciones mediante tarjetas de crédito de clientes minoristas y Mipyme"} · tramo: Saldo excedente al pago mínimo a que se refiere el inciso a)
- **N4** Restriccion `Restriccion_el_pago_minimo_de_amortizacion_de_capital_comisiones_o_intereses_asociados_a_pre_e36457` — Factor entrada 50% — pago mínimo tarjeta · {"tipo": "limite_cuantitativo", "descripcion": "El pago mínimo de amortización de capital, comisiones o intereses asociados a préstamos con vencimiento indefinido en financiaciones mediante tarjetas de crédito se califica con un factor de entrada de efectivo del 50%", "umbrales": [{"tramo": "50%", "valor": "50", "unidad": "porcentaje", "comparacion": "no_determinada", "regla_comparacion": "sin_mar · tramo: Pago mínimo de amortización de capital, comisiones o intereses asociados a préstamos con vencimiento indefinido. 50%
- **N5** Restriccion `Restriccion_el_saldo_excedente_al_pago_minimo_en_financiaciones_mediante_tarjetas_de_credito_3fe23b` — Factor entrada 20% — saldo excedente tarjeta · {"tipo": "limite_cuantitativo", "descripcion": "El saldo excedente al pago mínimo en financiaciones mediante tarjetas de crédito se califica con un factor de entrada de efectivo del 20%", "umbrales": [{"tramo": "20%", "valor": "20", "unidad": "porcentaje", "comparacion": "no_determinada", "regla_comparacion": "sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]} · tramo: Saldo excedente al pago mínimo a que se refiere el inciso a). 20%
- **N6** Restriccion `Restriccion_las_demas_entradas_de_efectivo_procedentes_de_clientes_minoristas_y_mipyme_se_ca_a12808` — Factor entrada 50% — demás entradas · {"tipo": "limite_cuantitativo", "descripcion": "Las demás entradas de efectivo procedentes de clientes minoristas y Mipyme se califican con un factor de entrada de efectivo del 50%", "umbrales": [{"tramo": "50%", "valor": "50", "unidad": "porcentaje", "comparacion": "no_determinada", "regla_comparacion": "sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]} · tramo: Demás. 50%
- **N7** TextoOrdenado `TextoOrdenado_ratio_pdf` — Ratio de fondeo neto estable · {"archivo": "ratio.pdf", "materia": "Ratio de cobertura de liquidez", "version": "Comunicación A 8445 (vigencia 05/06/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N7 · {}
- **R1** (remision_derivada) N1 —remite_a→ Condicion_creditos_sin_atraso_en_pagos__los_creditos_concedidos_a_clientes_minoristas_y_mi_c647c9 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R2** (remision_derivada) N1 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuan_otorgando_creditos_a_un_cb3a53 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R3** (remision_derivada) N1 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuaran_otorgando_creditos_a__f53e8f · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R4** (remision_derivada) N1 —remite_a→ Obligacion_las_entidades_financieras_deben_suponer_que_recibiran_todos_los_pagos_interes_y__26b8e7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R5** (remision_derivada) N1 —remite_a→ Obligacion_para_el_saldo_excedente_al_pago_minimo_de_financiaciones_mediante_tarjetas_de_cr_6b37b7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R6** (remision_derivada) N1 —remite_a→ Potestad_aplicacion_factores_punto_6_2_5_1__se_aplicaran_los_factores_previstos_en_el_pun_d01efe · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **E2** (estructural) N2 —establecida_en→ N7 · {}
- **R7** (remision_derivada) N2 —remite_a→ Condicion_creditos_sin_atraso_en_pagos__los_creditos_concedidos_a_clientes_minoristas_y_mi_c647c9 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R8** (remision_derivada) N2 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuan_otorgando_creditos_a_un_cb3a53 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R9** (remision_derivada) N2 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuaran_otorgando_creditos_a__f53e8f · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R10** (remision_derivada) N2 —remite_a→ Obligacion_las_entidades_financieras_deben_suponer_que_recibiran_todos_los_pagos_interes_y__26b8e7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R11** (remision_derivada) N2 —remite_a→ Obligacion_para_el_saldo_excedente_al_pago_minimo_de_financiaciones_mediante_tarjetas_de_cr_6b37b7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R12** (remision_derivada) N2 —remite_a→ Potestad_aplicacion_factores_punto_6_2_5_1__se_aplicaran_los_factores_previstos_en_el_pun_d01efe · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **E3** (estructural) N3 —establecida_en→ N7 · {}
- **R13** (remision_derivada) N3 —remite_a→ Condicion_creditos_sin_atraso_en_pagos__los_creditos_concedidos_a_clientes_minoristas_y_mi_c647c9 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R14** (remision_derivada) N3 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuan_otorgando_creditos_a_un_cb3a53 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R15** (remision_derivada) N3 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuaran_otorgando_creditos_a__f53e8f · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R16** (remision_derivada) N3 —remite_a→ Obligacion_las_entidades_financieras_deben_suponer_que_recibiran_todos_los_pagos_interes_y__26b8e7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R17** (remision_derivada) N3 —remite_a→ Obligacion_para_el_saldo_excedente_al_pago_minimo_de_financiaciones_mediante_tarjetas_de_cr_6b37b7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R18** (remision_derivada) N3 —remite_a→ Potestad_aplicacion_factores_punto_6_2_5_1__se_aplicaran_los_factores_previstos_en_el_pun_d01efe · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **E4** (estructural) N4 —establecida_en→ N7 · {}
- **A1** (extraccion) N4 —limita→ N2 · {}
- **R19** (remision_derivada) N4 —remite_a→ Condicion_creditos_sin_atraso_en_pagos__los_creditos_concedidos_a_clientes_minoristas_y_mi_c647c9 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R20** (remision_derivada) N4 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuan_otorgando_creditos_a_un_cb3a53 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R21** (remision_derivada) N4 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuaran_otorgando_creditos_a__f53e8f · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R22** (remision_derivada) N4 —remite_a→ Obligacion_las_entidades_financieras_deben_suponer_que_recibiran_todos_los_pagos_interes_y__26b8e7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R23** (remision_derivada) N4 —remite_a→ Obligacion_para_el_saldo_excedente_al_pago_minimo_de_financiaciones_mediante_tarjetas_de_cr_6b37b7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R24** (remision_derivada) N4 —remite_a→ Potestad_aplicacion_factores_punto_6_2_5_1__se_aplicaran_los_factores_previstos_en_el_pun_d01efe · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **E5** (estructural) N5 —establecida_en→ N7 · {}
- **A2** (extraccion) N5 —limita→ N3 · {}
- **R25** (remision_derivada) N5 —remite_a→ Condicion_creditos_sin_atraso_en_pagos__los_creditos_concedidos_a_clientes_minoristas_y_mi_c647c9 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R26** (remision_derivada) N5 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuan_otorgando_creditos_a_un_cb3a53 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R27** (remision_derivada) N5 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuaran_otorgando_creditos_a__f53e8f · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R28** (remision_derivada) N5 —remite_a→ Obligacion_las_entidades_financieras_deben_suponer_que_recibiran_todos_los_pagos_interes_y__26b8e7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R29** (remision_derivada) N5 —remite_a→ Obligacion_para_el_saldo_excedente_al_pago_minimo_de_financiaciones_mediante_tarjetas_de_cr_6b37b7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R30** (remision_derivada) N5 —remite_a→ Potestad_aplicacion_factores_punto_6_2_5_1__se_aplicaran_los_factores_previstos_en_el_pun_d01efe · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **E6** (estructural) N6 —establecida_en→ N7 · {}
- **A3** (extraccion) N6 —limita→ N1 · {}
- **R31** (remision_derivada) N6 —remite_a→ Condicion_creditos_sin_atraso_en_pagos__los_creditos_concedidos_a_clientes_minoristas_y_mi_c647c9 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R32** (remision_derivada) N6 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuan_otorgando_creditos_a_un_cb3a53 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R33** (remision_derivada) N6 —remite_a→ Obligacion_las_entidades_financieras_deben_presuponer_que_continuaran_otorgando_creditos_a__f53e8f · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R34** (remision_derivada) N6 —remite_a→ Obligacion_las_entidades_financieras_deben_suponer_que_recibiran_todos_los_pagos_interes_y__26b8e7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R35** (remision_derivada) N6 —remite_a→ Obligacion_para_el_saldo_excedente_al_pago_minimo_de_financiaciones_mediante_tarjetas_de_cr_6b37b7 · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}
- **R36** (remision_derivada) N6 —remite_a→ Potestad_aplicacion_factores_punto_6_2_5_1__se_aplicaran_los_factores_previstos_en_el_pun_d01efe · {"alcance": "interna", "destino": "ratio::5.2.3.1", "evidencia": "6.2.5.1. Entradas procedentes de clientes minoristas y Mipyme (punto\n5.2.3.1.).\ni) Financiaciones"}

## 30. `snp_tr_nc::3.2.4.1` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 16):

```
[encabezado | punto S3]
Sección 3. Transferencias inmediatas. Modalidades
[encabezado | punto 3.2]
3.2. Pago con transferencia
[encabezado | punto 3.2.4]
3.2.4. Solicitud de PCT
[texto propio | punto 3.2.4.1]
3.2.4.1. Los esquemas de transferencias inmediatas admitirán solicitudes de pago acti-
vas y pasivas, las que también podrán estar disponibles para los clientes bajo el
modelo comercial “paga el cliente ordenante”, detallado en la Sección 5.
```

Versión: final (grafo sin cola). Nodos 5, aristas 4.
- **N1** Operacion `Operacion_solicitudes_de_pago_activas__snp_tr_nc_3_2_4_1_d0f9cc` — Solicitudes de pago activas · {"tipo": "solicitud de pago", "descripcion": "Solicitudes de pago activas admitidas en esquemas de transferencias inmediatas"} · tramo: solicitudes de pago activas
- **N2** Operacion `Operacion_solicitudes_de_pago_pasivas__snp_tr_nc_3_2_4_1_268fff` — Solicitudes de pago pasivas · {"tipo": "solicitud de pago", "descripcion": "Solicitudes de pago pasivas admitidas en esquemas de transferencias inmediatas"} · tramo: solicitudes de pago acti- vas y pasivas
- **N3** Potestad `Potestad_admision_de_solicitudes_de_pago__los_esquemas_de_transferencias_inmediatas_estan_952dcd` — Admisión de solicitudes de pago · {"descripcion": "Los esquemas de transferencias inmediatas están facultados para admitir solicitudes de pago activas y pasivas"} · tramo: Los esquemas de transferencias inmediatas admitirán solicitudes de pago activas y pasivas
- **N4** Potestad `Potestad_disponibilidad_de_solicitudes_para_clientes__los_esquemas_de_transferencias_inme_f23106` — Disponibilidad de solicitudes para clientes · {"descripcion": "Los esquemas de transferencias inmediatas pueden poner a disposición de los clientes las solicitudes de pago bajo el modelo comercial 'paga el cliente ordenante', conforme a lo detallado en la Sección 5"} · tramo: las que también podrán estar disponibles para los clientes bajo el modelo comercial "paga el cliente ordenante"
- **N5** TextoOrdenado `TextoOrdenado_snp_tr_nc_pdf` — Transferencias - Normas complementarias · {"archivo": "snp_tr_nc.pdf", "materia": "Sistema Nacional de Pagos - Transferencias - Normas complementarias", "version": "Comunicación A 8436 (vigencia 15/05/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N5 · {}
- **E2** (estructural) N2 —establecida_en→ N5 · {}
- **E3** (estructural) N3 —establecida_en→ N5 · {}
- **E4** (estructural) N4 —establecida_en→ N5 · {}

